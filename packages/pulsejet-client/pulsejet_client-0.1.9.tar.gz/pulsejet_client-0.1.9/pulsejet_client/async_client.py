import logging
from typing import (
    Any,
    Dict,
    List,
    Optional,
)
from gen import *
from .async_pj_base import *
from .async_pj_remote import *
from .async_pj_remote import AsyncPulsejetRemote

import tomllib

class AsyncPulsejetClient(AsyncPulsejetBase):
    def __init__(self,
                 location: Optional[str] = "local",
                 https: Optional[bool] = None,
                 host: Optional[str] = "127.0.0.1",
                 grpc_port: int = 47045,
                 prefer_grpc: bool = True,
                 timeout: Optional[int] = None,
                 grpc_options: Optional[Dict[str, Any]] = None,
                 prod_name: Optional[str] = "pulsejetdb",
                 shard_id: Optional[int] = 0,
                 **kwargs: Any,
                 ):

        self.prod_name = prod_name
        self.shard_id = shard_id

        self.grpc_port = grpc_port

        if https:
            self.grpc_address = "https://{}.{}".format(host, self.grpc_port)
        else:
            self.grpc_address = "http://{}.{}".format(host, self.grpc_port)

        # PulseJet Base
        self._client = AsyncPulsejetRemote(
            host=host,
            grpc_port=grpc_port,
            https=https,
            timeout=timeout,
            grpc_options=grpc_options,
            **kwargs,
        )

    def __del__(self) -> None:
        self.close()

    async def close(self, grpc_grace: Optional[float] = None, **kwargs: Any) -> None:
        """Closes the connection to PulseJet

        Args:
            grpc_grace: Grace period for gRPC connection close. Default: None
        """
        if hasattr(self, "_client"):
            self._client.close(grpc_grace=grpc_grace, **kwargs)

    async def create_collection(self, collection_name: str, vector_config: VectorParams, **kwargs: Any) -> bool:
        assert len(kwargs) == 0, f"Unknown arguments: {list(kwargs.keys())}"
        return await self._client.create_collection(
            collection_name=collection_name,
            vector_config=vector_config,
            **kwargs
        )

    async def update_collection(self, existing_name: str, vector_config: VectorParams, new_name: Optional[str] = None,
                          **kwargs: Any) -> bool:
        assert len(kwargs) == 0, f"Unknown arguments: {list(kwargs.keys())}"
        return await self._client.update_collection(
            existing_name=existing_name,
            vector_config=vector_config,
            new_name=new_name,
            **kwargs
        )

    async def delete_collection(self, collection_name: str, **kwargs: Any) -> bool:
        assert len(kwargs) == 0, f"Unknown arguments: {list(kwargs.keys())}"
        return await self._client.delete_collection(
            collection_name=collection_name,
            **kwargs
        )

    async def list_collections(self, filter: Optional[str], **kwargs: Any) -> bool:
        assert len(kwargs) == 0, f"Unknown arguments: {list(kwargs.keys())}"
        return await self._client.list_collections(
            filter=filter,
            **kwargs
        )

    async def insert_single(self, collection_name: str, vector: List[float], meta: Dict[str, str]) -> bool:
        return await self._client.insert_single(
            collection_name=collection_name,
            vector=vector,
            meta=meta
        )

    async def insert_multi(self, collection_name: str, embeds: List[RawEmbed], num_workers: int = 1) -> bool:
        return await self._client.insert_multi(
            collection_name=collection_name,
            embeds=embeds,
            num_workers=num_workers
        )

    async def delete(self, collection_name: str, embed_ids: List[int]) -> bool:
        return await self._client.delete(
            collection_name=collection_name,
            embed_ids=embed_ids
        )

    async def update(self, collection_name: str, embeds: List[Embed]) -> bool:
        return await self._client.update(
            collection_name=collection_name,
            embeds=embeds
        )

    async def search_single(self, collection_name: str, vector: List[float], limit: int, filter: Optional[PayloadFilter]) -> bool:
        return await self._client.search_single(
            collection_name=collection_name,
            vector=vector,
            limit=limit,
            filter=filter
        )

    async def search_multi(self, searches: List[OpSearchEmbed]) -> bool:
        return await self._client.search_multi(
            searches=searches
        )

    async def collection_info(self, collection_name: str) -> bool:
        return await self._client.collection_info(collection_name)