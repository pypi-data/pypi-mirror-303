from .types import PayloadFilter
from gen import *
from typing import Any, Dict, List, Optional


class PulsejetBase:
    def __init__(self, **kwargs: Any):
        pass

    def close(self, **kwargs: Any) -> None:
        pass

    def create_collection(
            self,
            collection_name: str,
            vector_config: VectorParams,
            **kwargs: Any,
    ) -> bool:
        raise NotImplementedError()

    def update_collection(
            self,
            existing_name: str,
            vector_config: VectorParams,
            new_name: Optional[str] = None,
            **kwargs: Any,
    ) -> bool:
        raise NotImplementedError()

    def delete_collection(self, collection_name: str, **kwargs: Any) -> bool:
        raise NotImplementedError()

    def list_collections(self, filter: Optional[str], **kwargs: Any) -> bool:
        raise NotImplementedError()

    def insert_single(self, collection_name: str, vector: List[float], meta: Dict[str, str]) -> bool:
        raise NotImplementedError()

    def insert_multi(self, collection_name: str, embeds: List[RawEmbed]) -> bool:
        raise NotImplementedError()

    def delete(self, collection_name: str, embed_ids: List[int]) -> bool:
        raise NotImplementedError()

    def update(self, collection_name: str, embeds: List[Embed]) -> bool:
        raise NotImplementedError()

    def search_single(self, collection_name: str, vector: List[float], limit: int, filter: Optional[PayloadFilter]) -> bool:
        raise NotImplementedError()

    def search_multi(self, searches: List[OpSearchEmbed]) -> bool:
        raise NotImplementedError()

    def collection_info(self, collection_name: str) -> bool:
        raise NotImplementedError()