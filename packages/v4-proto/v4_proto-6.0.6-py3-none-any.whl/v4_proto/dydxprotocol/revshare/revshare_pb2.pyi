from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MarketMapperRevShareDetails(_message.Message):
    __slots__ = ("expiration_ts",)
    EXPIRATION_TS_FIELD_NUMBER: _ClassVar[int]
    expiration_ts: int
    def __init__(self, expiration_ts: _Optional[int] = ...) -> None: ...
