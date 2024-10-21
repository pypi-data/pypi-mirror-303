import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
from common_pb2 import RawEmbed as RawEmbed
from common_pb2 import Embed as Embed
from common_pb2 import Embeds as Embeds
from common_pb2 import OperationStatus as OperationStatus

DESCRIPTOR: _descriptor.FileDescriptor
OK: _common_pb2.OperationStatus
Error: _common_pb2.OperationStatus

class OpSearchEmbed(_message.Message):
    __slots__ = ("collection_name", "vector", "limit")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    VECTOR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    vector: _containers.RepeatedScalarFieldContainer[float]
    limit: int
    def __init__(self, collection_name: _Optional[str] = ..., vector: _Optional[_Iterable[float]] = ..., limit: _Optional[int] = ...) -> None: ...

class OpMultiSearchEmbed(_message.Message):
    __slots__ = ("searches",)
    SEARCHES_FIELD_NUMBER: _ClassVar[int]
    searches: _containers.RepeatedCompositeFieldContainer[OpSearchEmbed]
    def __init__(self, searches: _Optional[_Iterable[_Union[OpSearchEmbed, _Mapping]]] = ...) -> None: ...

class SearchEmbedResponse(_message.Message):
    __slots__ = ("response", "status")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    response: _common_pb2.OperationStatus
    status: _common_pb2.Embeds
    def __init__(self, response: _Optional[_Union[_common_pb2.OperationStatus, str]] = ..., status: _Optional[_Union[_common_pb2.Embeds, _Mapping]] = ...) -> None: ...

class SearchMultiEmbedResponse(_message.Message):
    __slots__ = ("response", "status")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    response: _common_pb2.OperationStatus
    status: _containers.RepeatedCompositeFieldContainer[_common_pb2.Embeds]
    def __init__(self, response: _Optional[_Union[_common_pb2.OperationStatus, str]] = ..., status: _Optional[_Iterable[_Union[_common_pb2.Embeds, _Mapping]]] = ...) -> None: ...
