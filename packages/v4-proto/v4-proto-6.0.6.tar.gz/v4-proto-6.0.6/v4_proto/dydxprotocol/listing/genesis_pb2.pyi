from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ("hard_cap_for_markets",)
    HARD_CAP_FOR_MARKETS_FIELD_NUMBER: _ClassVar[int]
    hard_cap_for_markets: int
    def __init__(self, hard_cap_for_markets: _Optional[int] = ...) -> None: ...
