from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OperationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OK: _ClassVar[OperationStatus]
    Error: _ClassVar[OperationStatus]
OK: OperationStatus
Error: OperationStatus

class RawEmbed(_message.Message):
    __slots__ = ("id", "vector", "meta")
    class MetaEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    VECTOR_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    id: int
    vector: _containers.RepeatedScalarFieldContainer[float]
    meta: _containers.ScalarMap[str, str]
    def __init__(self, id: _Optional[int] = ..., vector: _Optional[_Iterable[float]] = ..., meta: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Embed(_message.Message):
    __slots__ = ("id", "vector", "distance", "meta")
    class MetaEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    VECTOR_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    id: int
    vector: _containers.RepeatedScalarFieldContainer[float]
    distance: float
    meta: _containers.ScalarMap[str, str]
    def __init__(self, id: _Optional[int] = ..., vector: _Optional[_Iterable[float]] = ..., distance: _Optional[float] = ..., meta: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Embeds(_message.Message):
    __slots__ = ("element",)
    ELEMENT_FIELD_NUMBER: _ClassVar[int]
    element: _containers.RepeatedCompositeFieldContainer[Embed]
    def __init__(self, element: _Optional[_Iterable[_Union[Embed, _Mapping]]] = ...) -> None: ...
