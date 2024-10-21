import logging
import math
import asyncio
from multiprocessing import get_all_start_methods
from typing import (
    Any,
    Dict,
    Optional,
    List,
)

from gen.collections_service_pb2_grpc import CollectionsStub
from gen.search_service_pb2_grpc import SearchStub
from .async_pj_base import *

from .connections import *
from gen import *
from .parallel_processor import *
from .grpc_multi_inserter import *
from grpc import Compression


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


class AsyncPulsejetRemote(AsyncPulsejetBase):
    def __init__(
            self,
            host: Optional[str] = None,
            port: Optional[int] = 47044,
            grpc_port: int = 47045,
            https: Optional[bool] = None,
            timeout: Optional[int] = None,
            grpc_options: Optional[Dict[str, Any]] = None,
            **kwargs: Any,
    ):
        super().__init__(**kwargs)
        self._host = host
        self._port = port

        self._grpc_port = grpc_port
        self._grpc_options = grpc_options
        self._https = https if https is not None else False
        self._scheme = "https" if self._https else "http"

        self._grpc_headers = []

        # GRPC Channel-Level Compression
        grpc_compression: Optional[Compression] = kwargs.pop("grpc_compression", None)
        if grpc_compression is not None and not isinstance(grpc_compression, Compression):
            raise TypeError(
                f"Expected 'grpc_compression' to be of type "
                f"grpc.Compression or None, but got {type(grpc_compression)}"
            )
        if grpc_compression == Compression.Deflate:
            raise ValueError(
                "grpc.Compression.Deflate is not supported. Try grpc.Compression.Gzip or grpc.Compression.NoCompression"
            )
        self._grpc_compression = grpc_compression

        # TODO: Implement Auth Token Provider
        self._auth_token_provider = None

        self._aio_grpc_channel = None
        self._aio_grpc_collections_client: Optional[CollectionsStub] = None
        self._aio_grpc_embeds_client: Optional[EmbedsStub] = None
        self._aio_grpc_search_client: Optional[SearchStub] = None

        self._closed: bool = False
        self._timeout = math.ceil(timeout) if timeout is not None else None


    def _init_async_grpc_channel(self) -> None:
        if self._closed:
            raise RuntimeError("Client was closed. Create a new PulsejetClient instance.")

        if self._aio_grpc_channel is None:
            self._aio_grpc_channel = get_async_channel(
                host=self._host,
                port=self._grpc_port,
                ssl=self._https,
                metadata=self._grpc_headers,
                options=self._grpc_options,
                compression=self._grpc_compression,
                auth_token_provider=self._auth_token_provider,
            )

    def _init_async_grpc_collections_client(self) -> None:
        self._init_async_grpc_channel()
        self._aio_grpc_collections_client = CollectionsStub(self._aio_grpc_channel)

    def _init_async_grpc_embeds_client(self) -> None:
        self._init_async_grpc_channel()
        self._aio_grpc_embeds_client = EmbedsStub(self._aio_grpc_channel)

    def _init_async_grpc_search_client(self) -> None:
        self._init_async_grpc_channel()
        self._aio_grpc_search_client = SearchStub(self._aio_grpc_channel)

    @property
    def grpc_collections(self) -> CollectionsStub:
        """gRPC pulsejet_client for collection methods

        Returns:
            An instance of raw gRPC pulsejet_client, generated from Protobuf
        """
        if self._aio_grpc_collections_client is None:
            self._init_async_grpc_collections_client()
        return self._aio_grpc_collections_client

    @property
    def grpc_embeds(self) -> EmbedsStub:
        """gRPC pulsejet_client for embeds methods

        Returns:
            An instance of raw gRPC pulsejet_client, generated from Protobuf
        """
        if self._aio_grpc_embeds_client is None:
            self._init_async_grpc_embeds_client()
        return self._aio_grpc_embeds_client

    @property
    def grpc_search(self) -> SearchStub:
        """gRPC pulsejet_client for search methods

        Returns:
            An instance of raw gRPC pulsejet_client, generated from Protobuf
        """
        if self._aio_grpc_search_client is None:
            self._init_async_grpc_search_client()
        return self._aio_grpc_search_client

    async def create_collection(self, collection_name: str, vector_config: VectorParams, **kwargs: Any) -> bool:
        create_col_req = OpCreateCollection(name=collection_name, vector_config=vector_config)
        return await self.grpc_collections.Create(create_col_req, timeout=self._timeout)

    async def update_collection(self, existing_name: str, vector_config: VectorParams, new_name: Optional[str] = None,
                                **kwargs: Any) -> bool:
        update_col_req = OpUpdateCollection(name=existing_name, new_name=new_name, vector_config=vector_config)
        return await self.grpc_collections.Update(update_col_req, timeout=self._timeout)

    async def delete_collection(self, collection_name: str, **kwargs: Any) -> bool:
        del_col_req = OpDeleteCollection(name=collection_name)
        return await self.grpc_collections.Delete(del_col_req, timeout=self._timeout)

    async def list_collections(self, filter: Optional[str], **kwargs: Any) -> bool:
        list_col_req = OpListCollections(filter=filter)
        return await self.grpc_collections.List(list_col_req, timeout=self._timeout)

    async def collection_info(self, collection_name: str) -> bool:
        collection_info = OpCollectionInfo(name=collection_name)
        return await self.grpc_collections.CollectionInfo(collection_info, timeout=self._timeout)

    async def insert_single(self, collection_name: str, vector: List[float], meta: Dict[str, str]) -> bool:
        insert_embed_req = OpInsertEmbed(collection_name=collection_name, vector=vector, meta=meta)
        return await self.grpc_embeds.InsertEmbed(insert_embed_req, timeout=self._timeout)

    async def insert_multi(self, collection_name: str, embeds: List[RawEmbed], num_workers: int = 1) -> bool:
        if num_workers > 1:
            start_method = "forkserver" if "forkserver" in get_all_start_methods() else "spawn"
            reqs = [OpMultiInsertEmbed(collection_name=collection_name, embeds=chk).SerializeToString() for chk in
                    chunks(embeds, 512)]
            pool = ParallelWorkerPool(32, GrpcMultiInserter, start_method=start_method)
            updater_kwargs = {
                "collection_name": collection_name,
                "host": self._host,
                "port": self._grpc_port,
                "max_retries": 20,
                "ssl": self._https,
                "metadata": self._grpc_headers,
                "wait": False,
            }
            for _ in pool.unordered_map(reqs, **updater_kwargs):
                pass
            return True
        else:
            reqs = [self.grpc_embeds.InsertMultiEmbeds(OpMultiInsertEmbed(collection_name=collection_name, embeds=chk),
                                                       timeout=self._timeout) for chk in chunks(embeds, 512)]
            return await asyncio.gather(*reqs, return_exceptions=True)

    async def delete(self, collection_name: str, embed_ids: List[int]) -> bool:
        delete_req = OpMultiDeleteEmbed(collection_name=collection_name, embed_ids=embed_ids)
        return await self.grpc_embeds.DeleteEmbeds(delete_req, timeout=self._timeout)

    async def update(self, collection_name: str, embeds: List[Embed]) -> bool:
        update_multi_req = OpMultiUpdateEmbed(collection_name=collection_name, embeds=embeds)
        return await self.grpc_embeds.UpdateEmbeds(update_multi_req, timeout=self._timeout)

    async def search_single(self, collection_name: str, vector: List[float], limit: int,
                            filter: Optional[PayloadFilter]) -> bool:
        search_req = OpSearchEmbed(collection_name=collection_name, vector=vector, limit=limit)
        return await self.grpc_search.Search(search_req, timeout=self._timeout)

    async def search_multi(self, searches: List[OpSearchEmbed]) -> bool:
        search_multi_req = OpMultiSearchEmbed(searches=searches)
        return await self.grpc_search.SearchMulti(search_multi_req, timeout=self._timeout)

    async def close(self, grpc_grace: Optional[float] = None, **kwargs: Any) -> None:
        if hasattr(self, "_grpc_channel") and self._grpc_channel is not None:
            try:
                self._grpc_channel.close()
            except AttributeError:
                logging.warning(
                    "Unable to close grpc_channel. Connection was interrupted on the server side"
                )

        if hasattr(self, "_aio_grpc_channel") and self._aio_grpc_channel is not None:
            try:
                loop = asyncio.get_running_loop()
                loop.create_task(self._aio_grpc_channel.close(grace=grpc_grace))
            except AttributeError:
                logging.warning(
                    "Unable to close aio_grpc_channel. Connection was interrupted on the server side"
                )
            except RuntimeError:
                pass

        try:
            self.openapi_client.close()
        except Exception:
            logging.warning(
                "Unable to close http connection. Connection was interrupted on the server side"
            )

        self._closed = True
