from gen import *
from typing import Any, Dict, List, Optional
from .types import PayloadFilter


class AsyncPulsejetBase:
    def __init__(self, **kwargs: Any):
        pass

    async def close(self, **kwargs: Any) -> None:
        pass

    async def create_collection(
            self,
            collection_name: str,
            vector_config: VectorParams,
            **kwargs: Any,
    ) -> bool:
        raise NotImplementedError()

    async def update_collection(
            self,
            existing_name: str,
            vector_config: VectorParams,
            new_name: Optional[str] = None,
            **kwargs: Any,
    ) -> bool:
        raise NotImplementedError()

    async def delete_collection(self, collection_name: str, **kwargs: Any) -> bool:
        raise NotImplementedError()

    async def list_collections(self, filter: Optional[str], **kwargs: Any) -> bool:
        raise NotImplementedError()

    async def insert_single(self, collection_name: str, vector: List[float], meta: Dict[str, str]) -> bool:
        raise NotImplementedError()

    async def insert_multi(self, collection_name: str, embeds: List[RawEmbed]) -> bool:
        raise NotImplementedError()

    async def delete(self, collection_name: str, embed_ids: List[int]) -> bool:
        raise NotImplementedError()

    async def update(self, collection_name: str, embeds: List[Embed]) -> bool:
        raise NotImplementedError()

    async def search_single(self, collection_name: str, vector: List[float], limit: int, filter: Optional[PayloadFilter]) -> bool:
        raise NotImplementedError()

    async def search_multi(self, searches: List[OpSearchEmbed]) -> bool:
        raise NotImplementedError()

    async def collection_info(self, collection_name: str) -> bool:
        raise NotImplementedError()