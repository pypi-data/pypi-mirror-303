"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
from abc import (
    ABCMeta,
    abstractmethod,
)
from chalk._gen.chalk.server.v1.graph_pb2 import (
    GetFeatureSQLRequest,
    GetFeatureSQLResponse,
    GetFeaturesMetadataRequest,
    GetFeaturesMetadataResponse,
    GetGraphRequest,
    GetGraphResponse,
    UpdateGraphRequest,
    UpdateGraphResponse,
)
from grpc import (
    Channel,
    Server,
    ServicerContext,
    UnaryUnaryMultiCallable,
)

class GraphServiceStub:
    def __init__(self, channel: Channel) -> None: ...
    GetFeatureSQL: UnaryUnaryMultiCallable[
        GetFeatureSQLRequest,
        GetFeatureSQLResponse,
    ]
    """GetFeatureSQL returns the feature SQLs for a given deployment."""
    GetFeaturesMetadata: UnaryUnaryMultiCallable[
        GetFeaturesMetadataRequest,
        GetFeaturesMetadataResponse,
    ]
    GetGraph: UnaryUnaryMultiCallable[
        GetGraphRequest,
        GetGraphResponse,
    ]
    UpdateGraph: UnaryUnaryMultiCallable[
        UpdateGraphRequest,
        UpdateGraphResponse,
    ]
    """UpdateGraph uploads the protobuf graph for a given deployment."""

class GraphServiceServicer(metaclass=ABCMeta):
    @abstractmethod
    def GetFeatureSQL(
        self,
        request: GetFeatureSQLRequest,
        context: ServicerContext,
    ) -> GetFeatureSQLResponse:
        """GetFeatureSQL returns the feature SQLs for a given deployment."""
    @abstractmethod
    def GetFeaturesMetadata(
        self,
        request: GetFeaturesMetadataRequest,
        context: ServicerContext,
    ) -> GetFeaturesMetadataResponse: ...
    @abstractmethod
    def GetGraph(
        self,
        request: GetGraphRequest,
        context: ServicerContext,
    ) -> GetGraphResponse: ...
    @abstractmethod
    def UpdateGraph(
        self,
        request: UpdateGraphRequest,
        context: ServicerContext,
    ) -> UpdateGraphResponse:
        """UpdateGraph uploads the protobuf graph for a given deployment."""

def add_GraphServiceServicer_to_server(servicer: GraphServiceServicer, server: Server) -> None: ...
