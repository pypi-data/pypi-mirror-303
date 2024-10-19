"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
from abc import (
    ABCMeta,
    abstractmethod,
)
from chalk._gen.chalk.server.v1.named_query_pb2 import (
    GetAllNamedQueriesActiveDeploymentRequest,
    GetAllNamedQueriesActiveDeploymentResponse,
    GetAllNamedQueriesRequest,
    GetAllNamedQueriesResponse,
    GetNamedQueryByNameRequest,
    GetNamedQueryByNameResponse,
)
from grpc import (
    Channel,
    Server,
    ServicerContext,
    UnaryUnaryMultiCallable,
)

class NamedQueryServiceStub:
    def __init__(self, channel: Channel) -> None: ...
    GetAllNamedQueries: UnaryUnaryMultiCallable[
        GetAllNamedQueriesRequest,
        GetAllNamedQueriesResponse,
    ]
    GetAllNamedQueriesActiveDeployment: UnaryUnaryMultiCallable[
        GetAllNamedQueriesActiveDeploymentRequest,
        GetAllNamedQueriesActiveDeploymentResponse,
    ]
    GetNamedQueryByName: UnaryUnaryMultiCallable[
        GetNamedQueryByNameRequest,
        GetNamedQueryByNameResponse,
    ]

class NamedQueryServiceServicer(metaclass=ABCMeta):
    @abstractmethod
    def GetAllNamedQueries(
        self,
        request: GetAllNamedQueriesRequest,
        context: ServicerContext,
    ) -> GetAllNamedQueriesResponse: ...
    @abstractmethod
    def GetAllNamedQueriesActiveDeployment(
        self,
        request: GetAllNamedQueriesActiveDeploymentRequest,
        context: ServicerContext,
    ) -> GetAllNamedQueriesActiveDeploymentResponse: ...
    @abstractmethod
    def GetNamedQueryByName(
        self,
        request: GetNamedQueryByNameRequest,
        context: ServicerContext,
    ) -> GetNamedQueryByNameResponse: ...

def add_NamedQueryServiceServicer_to_server(servicer: NamedQueryServiceServicer, server: Server) -> None: ...
