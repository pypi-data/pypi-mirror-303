from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class QueryMarketsHardCap(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class QueryMarketsHardCapResponse(_message.Message):
    __slots__ = ("hard_cap",)
    HARD_CAP_FIELD_NUMBER: _ClassVar[int]
    hard_cap: int
    def __init__(self, hard_cap: _Optional[int] = ...) -> None: ...
