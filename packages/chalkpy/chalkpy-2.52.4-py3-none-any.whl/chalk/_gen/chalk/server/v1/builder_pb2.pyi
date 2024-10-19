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
