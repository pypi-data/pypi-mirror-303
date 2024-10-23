from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MaskedClientSecret(_message.Message):
    __slots__ = ["created_at", "masked_secret", "secret_id", "status", "updated_at"]
    CREATED_AT_FIELD_NUMBER: ClassVar[int]
    MASKED_SECRET_FIELD_NUMBER: ClassVar[int]
    SECRET_ID_FIELD_NUMBER: ClassVar[int]
    STATUS_FIELD_NUMBER: ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: ClassVar[int]
    created_at: str
    masked_secret: str
    secret_id: str
    status: str
    updated_at: str
    def __init__(self, secret_id: Optional[str] = ..., created_at: Optional[str] = ..., updated_at: Optional[str] = ..., status: Optional[str] = ..., masked_secret: Optional[str] = ...) -> None: ...
