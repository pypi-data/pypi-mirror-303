from v4_proto.gogoproto import gogo_pb2 as _gogo_pb2
from v4_proto.dydxprotocol.vault import params_pb2 as _params_pb2
from v4_proto.dydxprotocol.vault import share_pb2 as _share_pb2
from v4_proto.dydxprotocol.vault import vault_pb2 as _vault_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenesisState(_message.Message):
    __slots__ = ("vaults", "default_quoting_params")
    VAULTS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_QUOTING_PARAMS_FIELD_NUMBER: _ClassVar[int]
    vaults: _containers.RepeatedCompositeFieldContainer[Vault]
    default_quoting_params: _params_pb2.QuotingParams
    def __init__(self, vaults: _Optional[_Iterable[_Union[Vault, _Mapping]]] = ..., default_quoting_params: _Optional[_Union[_params_pb2.QuotingParams, _Mapping]] = ...) -> None: ...

class Vault(_message.Message):
    __slots__ = ("vault_id", "total_shares", "owner_shares", "quoting_params", "most_recent_client_ids")
    VAULT_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SHARES_FIELD_NUMBER: _ClassVar[int]
    OWNER_SHARES_FIELD_NUMBER: _ClassVar[int]
    QUOTING_PARAMS_FIELD_NUMBER: _ClassVar[int]
    MOST_RECENT_CLIENT_IDS_FIELD_NUMBER: _ClassVar[int]
    vault_id: _vault_pb2.VaultId
    total_shares: _share_pb2.NumShares
    owner_shares: _containers.RepeatedCompositeFieldContainer[_share_pb2.OwnerShare]
    quoting_params: _params_pb2.QuotingParams
    most_recent_client_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, vault_id: _Optional[_Union[_vault_pb2.VaultId, _Mapping]] = ..., total_shares: _Optional[_Union[_share_pb2.NumShares, _Mapping]] = ..., owner_shares: _Optional[_Iterable[_Union[_share_pb2.OwnerShare, _Mapping]]] = ..., quoting_params: _Optional[_Union[_params_pb2.QuotingParams, _Mapping]] = ..., most_recent_client_ids: _Optional[_Iterable[int]] = ...) -> None: ...
