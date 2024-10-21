import logging
from typing import (
    Any,
    Dict,
    Optional,
    List,
)
from .pj_base import *
from .pj_remote import *
from .types import PayloadFilter

class PulsejetClient(PulsejetBase):
    def __init__(self,
                 https: Optional[bool] = None,
                 host: Optional[str] = "127.0.0.1",
                 port: int = 47045,
                 prefer_grpc: bool = True,
                 timeout: Optional[int] = None,
                 prod_name: Optional[str] = "pulsejetdb",
                 **kwargs: Any,
                 ):

        self.port = port

        if https:
            self.grpc_address = "https://{}.{}".format(host, self.port)
        else:
            self.grpc_address = "http://{}.{}".format(host, self.port)


        # XXX: Doing the launch here with options.
        logging.info(f"PulseJet™ DB - Connecting remote instance on '{host}' and port: '{port}'.")
        self._client = PulsejetRemote(
            host=host,
            grpc_port=port,
            prefer_grpc=prefer_grpc,
            https=https,
            timeout=timeout,
            **kwargs,
        )

    def __del__(self) -> None:
        self.close()

    def close(self, grpc_grace: Optional[float] = None, **kwargs: Any) -> None:
        """Closes the connection to PulseJet

        Args:
            grpc_grace: Grace period for gRPC connection close. Default: None
        """
        if hasattr(self, "_client"):
            self._client.close(grpc_grace=grpc_grace, **kwargs)

    def create_collection(self, collection_name: str, vector_config: VectorParams, **kwargs: Any) -> bool:
        assert len(kwargs) == 0, f"Unknown arguments: {list(kwargs.keys())}"
        return self._client.create_collection(
            collection_name=collection_name,
            vector_config=vector_config,
            **kwargs
        )

    def update_collection(self, existing_name: str, vector_config: VectorParams, new_name: Optional[str] = None,
                          **kwargs: Any) -> bool:
        assert len(kwargs) == 0, f"Unknown arguments: {list(kwargs.keys())}"
        return self._client.update_collection(
            existing_name=existing_name,
            vector_config=vector_config,
            new_name=new_name,
            **kwargs
        )

    def delete_collection(self, collection_name: str, **kwargs: Any) -> bool:
        assert len(kwargs) == 0, f"Unknown arguments: {list(kwargs.keys())}"
        return self._client.delete_collection(
            collection_name=collection_name,
            **kwargs
        )

    def list_collections(self, filter: Optional[str], **kwargs: Any) -> bool:
        assert len(kwargs) == 0, f"Unknown arguments: {list(kwargs.keys())}"
        return self._client.list_collections(
            filter=filter,
            **kwargs
        )

    def insert_single(self, collection_name: str, vector: List[float], meta: Dict[str, str]) -> bool:
        return self._client.insert_single(
            collection_name=collection_name,
            vector=vector,
            meta=meta
        )
    def insert_multi(self, collection_name: str, embeds: List[RawEmbed]) -> bool:
        return self._client.insert_multi(
            collection_name=collection_name,
            embeds=embeds
        )

    def delete(self, collection_name: str, embed_ids: List[int]) -> bool:
        return self._client.delete(
            collection_name=collection_name,
            embed_ids=embed_ids
        )

    def update(self, collection_name: str, embeds: List[Embed]) -> bool:
        return self._client.update(
            collection_name=collection_name,
            embeds=embeds
        )

    def search_single(self, collection_name: str, vector: List[float], limit: int, filter: Optional[PayloadFilter]) -> bool:
        return self._client.search_single(
            collection_name=collection_name,
            vector=vector,
            limit=limit,
            filter=filter
        )

    def search_multi(self, searches: List[OpSearchEmbed]) -> bool:
        return self._client.search_multi(
            searches=searches
        )

    def collection_info(self, collection_name: str) -> bool:
        return self._client.collection_info(collection_name)

