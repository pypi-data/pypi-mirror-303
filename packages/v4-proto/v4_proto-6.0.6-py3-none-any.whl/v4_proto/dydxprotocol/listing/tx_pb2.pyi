from v4_proto.cosmos_proto import cosmos_pb2 as _cosmos_pb2
from v4_proto.cosmos.msg.v1 import msg_pb2 as _msg_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MsgSetMarketsHardCap(_message.Message):
    __slots__ = ("authority", "hard_cap_for_markets")
    AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    HARD_CAP_FOR_MARKETS_FIELD_NUMBER: _ClassVar[int]
    authority: str
    hard_cap_for_markets: int
    def __init__(self, authority: _Optional[str] = ..., hard_cap_for_markets: _Optional[int] = ...) -> None: ...

class MsgSetMarketsHardCapResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
