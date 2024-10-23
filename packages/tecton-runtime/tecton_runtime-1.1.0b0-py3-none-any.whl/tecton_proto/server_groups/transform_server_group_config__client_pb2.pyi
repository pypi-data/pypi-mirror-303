from google.protobuf import timestamp_pb2 as _timestamp_pb2
from tecton_proto.common import id__client_pb2 as _id__client_pb2
from tecton_proto.common import secret__client_pb2 as _secret__client_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class FeatureViewSecretConfig(_message.Message):
    __slots__ = ["secrets_map"]
    class SecretsMapEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: _secret__client_pb2.SecretReference
        def __init__(self, key: Optional[str] = ..., value: Optional[Union[_secret__client_pb2.SecretReference, Mapping]] = ...) -> None: ...
    SECRETS_MAP_FIELD_NUMBER: ClassVar[int]
    secrets_map: _containers.MessageMap[str, _secret__client_pb2.SecretReference]
    def __init__(self, secrets_map: Optional[Mapping[str, _secret__client_pb2.SecretReference]] = ...) -> None: ...

class SecretMetadata(_message.Message):
    __slots__ = ["last_updated", "secret_reference"]
    LAST_UPDATED_FIELD_NUMBER: ClassVar[int]
    SECRET_REFERENCE_FIELD_NUMBER: ClassVar[int]
    last_updated: _timestamp_pb2.Timestamp
    secret_reference: _secret__client_pb2.SecretReference
    def __init__(self, secret_reference: Optional[Union[_secret__client_pb2.SecretReference, Mapping]] = ..., last_updated: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...) -> None: ...

class TransformServerGroupConfiguration(_message.Message):
    __slots__ = ["computed_time", "secrets_config", "server_group_id", "workspace", "workspace_state_id"]
    COMPUTED_TIME_FIELD_NUMBER: ClassVar[int]
    SECRETS_CONFIG_FIELD_NUMBER: ClassVar[int]
    SERVER_GROUP_ID_FIELD_NUMBER: ClassVar[int]
    WORKSPACE_FIELD_NUMBER: ClassVar[int]
    WORKSPACE_STATE_ID_FIELD_NUMBER: ClassVar[int]
    computed_time: _timestamp_pb2.Timestamp
    secrets_config: TransformServerGroupSecretsConfig
    server_group_id: str
    workspace: str
    workspace_state_id: str
    def __init__(self, server_group_id: Optional[str] = ..., workspace: Optional[str] = ..., workspace_state_id: Optional[str] = ..., secrets_config: Optional[Union[TransformServerGroupSecretsConfig, Mapping]] = ..., computed_time: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...) -> None: ...

class TransformServerGroupSecretsConfig(_message.Message):
    __slots__ = ["all_secrets_metadata", "feature_view_secret_references", "service_account_key"]
    class FeatureViewSecretReferencesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: FeatureViewSecretConfig
        def __init__(self, key: Optional[str] = ..., value: Optional[Union[FeatureViewSecretConfig, Mapping]] = ...) -> None: ...
    ALL_SECRETS_METADATA_FIELD_NUMBER: ClassVar[int]
    FEATURE_VIEW_SECRET_REFERENCES_FIELD_NUMBER: ClassVar[int]
    SERVICE_ACCOUNT_KEY_FIELD_NUMBER: ClassVar[int]
    all_secrets_metadata: _containers.RepeatedCompositeFieldContainer[SecretMetadata]
    feature_view_secret_references: _containers.MessageMap[str, FeatureViewSecretConfig]
    service_account_key: str
    def __init__(self, service_account_key: Optional[str] = ..., all_secrets_metadata: Optional[Iterable[Union[SecretMetadata, Mapping]]] = ..., feature_view_secret_references: Optional[Mapping[str, FeatureViewSecretConfig]] = ...) -> None: ...
