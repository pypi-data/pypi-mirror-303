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

class OpGetEmbed(_message.Message):
    __slots__ = ("collection_name", "id")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    id: int
    def __init__(self, collection_name: _Optional[str] = ..., id: _Optional[int] = ...) -> None: ...

class OpGetEmbeds(_message.Message):
    __slots__ = ("collection_name", "ids")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, collection_name: _Optional[str] = ..., ids: _Optional[_Iterable[int]] = ...) -> None: ...

class OpListEmbeds(_message.Message):
    __slots__ = ("collection_name",)
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    def __init__(self, collection_name: _Optional[str] = ...) -> None: ...

class OpInsertEmbed(_message.Message):
    __slots__ = ("collection_name", "id", "vector", "meta")
    class MetaEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    VECTOR_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    id: int
    vector: _containers.RepeatedScalarFieldContainer[float]
    meta: _containers.ScalarMap[str, str]
    def __init__(self, collection_name: _Optional[str] = ..., id: _Optional[int] = ..., vector: _Optional[_Iterable[float]] = ..., meta: _Optional[_Mapping[str, str]] = ...) -> None: ...

class OpMultiInsertEmbed(_message.Message):
    __slots__ = ("collection_name", "embeds")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    EMBEDS_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    embeds: _containers.RepeatedCompositeFieldContainer[_common_pb2.RawEmbed]
    def __init__(self, collection_name: _Optional[str] = ..., embeds: _Optional[_Iterable[_Union[_common_pb2.RawEmbed, _Mapping]]] = ...) -> None: ...

class OpUpdateEmbed(_message.Message):
    __slots__ = ("collection_name", "embed")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    EMBED_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    embed: _common_pb2.Embed
    def __init__(self, collection_name: _Optional[str] = ..., embed: _Optional[_Union[_common_pb2.Embed, _Mapping]] = ...) -> None: ...

class OpMultiUpdateEmbed(_message.Message):
    __slots__ = ("collection_name", "embeds")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    EMBEDS_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    embeds: _containers.RepeatedCompositeFieldContainer[_common_pb2.Embed]
    def __init__(self, collection_name: _Optional[str] = ..., embeds: _Optional[_Iterable[_Union[_common_pb2.Embed, _Mapping]]] = ...) -> None: ...

class OpMultiDeleteEmbed(_message.Message):
    __slots__ = ("collection_name", "embed_ids")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    EMBED_IDS_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    embed_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, collection_name: _Optional[str] = ..., embed_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class GetEmbedResponse(_message.Message):
    __slots__ = ("response", "status")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    response: _common_pb2.OperationStatus
    status: _common_pb2.Embed
    def __init__(self, response: _Optional[_Union[_common_pb2.OperationStatus, str]] = ..., status: _Optional[_Union[_common_pb2.Embed, _Mapping]] = ...) -> None: ...

class GetEmbedsResponse(_message.Message):
    __slots__ = ("response", "status")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    response: _common_pb2.OperationStatus
    status: _containers.RepeatedCompositeFieldContainer[_common_pb2.Embed]
    def __init__(self, response: _Optional[_Union[_common_pb2.OperationStatus, str]] = ..., status: _Optional[_Iterable[_Union[_common_pb2.Embed, _Mapping]]] = ...) -> None: ...

class ListEmbedsResponse(_message.Message):
    __slots__ = ("response", "status")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    response: _common_pb2.OperationStatus
    status: _containers.RepeatedCompositeFieldContainer[_common_pb2.Embed]
    def __init__(self, response: _Optional[_Union[_common_pb2.OperationStatus, str]] = ..., status: _Optional[_Iterable[_Union[_common_pb2.Embed, _Mapping]]] = ...) -> None: ...

class InsertEmbedResponse(_message.Message):
    __slots__ = ("response", "status")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    response: _common_pb2.OperationStatus
    status: int
    def __init__(self, response: _Optional[_Union[_common_pb2.OperationStatus, str]] = ..., status: _Optional[int] = ...) -> None: ...

class InsertMultiEmbedsResponse(_message.Message):
    __slots__ = ("response", "status")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    response: _common_pb2.OperationStatus
    status: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, response: _Optional[_Union[_common_pb2.OperationStatus, str]] = ..., status: _Optional[_Iterable[int]] = ...) -> None: ...

class UpdateEmbedResponse(_message.Message):
    __slots__ = ("response", "status")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    response: _common_pb2.OperationStatus
    status: _common_pb2.Embed
    def __init__(self, response: _Optional[_Union[_common_pb2.OperationStatus, str]] = ..., status: _Optional[_Union[_common_pb2.Embed, _Mapping]] = ...) -> None: ...

class UpdateMultiEmbedResponse(_message.Message):
    __slots__ = ("response", "status")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    response: _common_pb2.OperationStatus
    status: _containers.RepeatedCompositeFieldContainer[_common_pb2.Embed]
    def __init__(self, response: _Optional[_Union[_common_pb2.OperationStatus, str]] = ..., status: _Optional[_Iterable[_Union[_common_pb2.Embed, _Mapping]]] = ...) -> None: ...

class DeleteEmbedsResponse(_message.Message):
    __slots__ = ("response", "status")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    response: _common_pb2.OperationStatus
    status: str
    def __init__(self, response: _Optional[_Union[_common_pb2.OperationStatus, str]] = ..., status: _Optional[str] = ...) -> None: ...
