import logging
from typing import Any, Generator, Iterable, Optional

from gen.embeds_pb2 import OpMultiInsertEmbed
from gen.embeds_service_pb2_grpc import EmbedsStub


from .connections import *

def multi_insert_grpc(
        embeds_client: EmbedsStub,
        collection_name: str,
        batch: str,
        max_retries: int,
        wait: bool = False,
) -> bool:
    for attempt in range(max_retries):
        try:
            op = OpMultiInsertEmbed.FromString(batch)
            embeds_client.InsertMultiEmbeds(op)
            break
        except Exception as e:
            logging.warning(f"Multi insertion failed {attempt + 1} times. Retrying...")

            if attempt == max_retries - 1:
                raise e
    return True


class GrpcMultiInserter():
    def __init__(
            self,
            host: str,
            port: int,
            collection_name: str,
            max_retries: int,
            wait: bool = False,
            **kwargs: Any,
    ):
        self.collection_name = collection_name
        self._host = host
        self._port = port
        self.max_retries = max_retries
        self._kwargs = kwargs
        self._wait = wait

    @classmethod
    def start(
            cls,
            collection_name: Optional[str] = None,
            host: str = "localhost",
            port: int = 6334,
            max_retries: int = 3,
            **kwargs: Any,
    ) -> "GrpcMultiInserter":
        if not collection_name:
            raise RuntimeError("Collection name could not be empty")

        return cls(
            host=host,
            port=port,
            collection_name=collection_name,
            max_retries=max_retries,
            **kwargs,
        )

    def process_upload(self, items: Iterable[Any]) -> Generator[bool, None, None]:
        channel = get_channel(host=self._host, port=self._port, **self._kwargs)
        embeds_client = EmbedsStub(channel)
        for batch in items:
            yield multi_insert_grpc(
                embeds_client,
                self.collection_name,
                batch,
                max_retries=self.max_retries,
                wait=self._wait,
            )

    def process(self, items: Iterable[Any]) -> Generator[bool, None, None]:
        yield from self.process_upload(items)
