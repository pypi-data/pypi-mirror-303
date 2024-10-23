from chalk._gen.chalk.auth.v1 import permissions_pb2 as _permissions_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ActivateDeploymentRequest(_message.Message):
    __slots__ = ("existing_deployment_id",)
    EXISTING_DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    existing_deployment_id: str
    def __init__(self, existing_deployment_id: _Optional[str] = ...) -> None: ...

class ActivateDeploymentResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IndexDeploymentRequest(_message.Message):
    __slots__ = ("existing_deployment_id",)
    EXISTING_DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    existing_deployment_id: str
    def __init__(self, existing_deployment_id: _Optional[str] = ...) -> None: ...

class IndexDeploymentResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeployKubeComponentsRequest(_message.Message):
    __slots__ = ("existing_deployment_id",)
    EXISTING_DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    existing_deployment_id: str
    def __init__(self, existing_deployment_id: _Optional[str] = ...) -> None: ...

class DeployKubeComponentsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RebuildDeploymentRequest(_message.Message):
    __slots__ = ("existing_deployment_id", "new_image_tag", "base_image_override", "enable_profiling")
    EXISTING_DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_IMAGE_TAG_FIELD_NUMBER: _ClassVar[int]
    BASE_IMAGE_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PROFILING_FIELD_NUMBER: _ClassVar[int]
    existing_deployment_id: str
    new_image_tag: str
    base_image_override: str
    enable_profiling: bool
    def __init__(
        self,
        existing_deployment_id: _Optional[str] = ...,
        new_image_tag: _Optional[str] = ...,
        base_image_override: _Optional[str] = ...,
        enable_profiling: bool = ...,
    ) -> None: ...

class RebuildDeploymentResponse(_message.Message):
    __slots__ = ("build_id",)
    BUILD_ID_FIELD_NUMBER: _ClassVar[int]
    build_id: str
    def __init__(self, build_id: _Optional[str] = ...) -> None: ...
