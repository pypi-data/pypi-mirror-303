from tecton_proto.common import data_type__client_pb2 as _data_type__client_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

ADDITION: OperationType
COALESCE: OperationType
DESCRIPTOR: _descriptor.FileDescriptor
DIVISION: OperationType
MULTIPLICATION: OperationType
OPERATION_UNSPECIFIED: OperationType
SUBTRACTION: OperationType

class AbstractSyntaxTreeNode(_message.Message):
    __slots__ = ["column_reference", "dtype", "literal_value", "operation"]
    COLUMN_REFERENCE_FIELD_NUMBER: ClassVar[int]
    DTYPE_FIELD_NUMBER: ClassVar[int]
    LITERAL_VALUE_FIELD_NUMBER: ClassVar[int]
    OPERATION_FIELD_NUMBER: ClassVar[int]
    column_reference: str
    dtype: _data_type__client_pb2.DataType
    literal_value: LiteralValue
    operation: Operation
    def __init__(self, dtype: Optional[Union[_data_type__client_pb2.DataType, Mapping]] = ..., literal_value: Optional[Union[LiteralValue, Mapping]] = ..., column_reference: Optional[str] = ..., operation: Optional[Union[Operation, Mapping]] = ...) -> None: ...

class LiteralValue(_message.Message):
    __slots__ = ["bool_value", "float32_value", "float64_value", "int64_value", "null_value", "string_value"]
    BOOL_VALUE_FIELD_NUMBER: ClassVar[int]
    FLOAT32_VALUE_FIELD_NUMBER: ClassVar[int]
    FLOAT64_VALUE_FIELD_NUMBER: ClassVar[int]
    INT64_VALUE_FIELD_NUMBER: ClassVar[int]
    NULL_VALUE_FIELD_NUMBER: ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: ClassVar[int]
    bool_value: bool
    float32_value: float
    float64_value: float
    int64_value: int
    null_value: NullLiteralValue
    string_value: str
    def __init__(self, float32_value: Optional[float] = ..., float64_value: Optional[float] = ..., int64_value: Optional[int] = ..., bool_value: bool = ..., string_value: Optional[str] = ..., null_value: Optional[Union[NullLiteralValue, Mapping]] = ...) -> None: ...

class NullLiteralValue(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Operation(_message.Message):
    __slots__ = ["operands", "operation"]
    OPERANDS_FIELD_NUMBER: ClassVar[int]
    OPERATION_FIELD_NUMBER: ClassVar[int]
    operands: _containers.RepeatedCompositeFieldContainer[AbstractSyntaxTreeNode]
    operation: OperationType
    def __init__(self, operation: Optional[Union[OperationType, str]] = ..., operands: Optional[Iterable[Union[AbstractSyntaxTreeNode, Mapping]]] = ...) -> None: ...

class OperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
