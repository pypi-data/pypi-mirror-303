"""
Type annotations for neptune-graph service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_neptune_graph.client import NeptuneGraphClient

    session = Session()
    client: NeptuneGraphClient = session.client("neptune-graph")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    ListGraphSnapshotsPaginator,
    ListGraphsPaginator,
    ListImportTasksPaginator,
    ListPrivateGraphEndpointsPaginator,
)
from .type_defs import (
    CancelImportTaskInputRequestTypeDef,
    CancelImportTaskOutputTypeDef,
    CancelQueryInputRequestTypeDef,
    CreateGraphInputRequestTypeDef,
    CreateGraphOutputTypeDef,
    CreateGraphSnapshotInputRequestTypeDef,
    CreateGraphSnapshotOutputTypeDef,
    CreateGraphUsingImportTaskInputRequestTypeDef,
    CreateGraphUsingImportTaskOutputTypeDef,
    CreatePrivateGraphEndpointInputRequestTypeDef,
    CreatePrivateGraphEndpointOutputTypeDef,
    DeleteGraphInputRequestTypeDef,
    DeleteGraphOutputTypeDef,
    DeleteGraphSnapshotInputRequestTypeDef,
    DeleteGraphSnapshotOutputTypeDef,
    DeletePrivateGraphEndpointInputRequestTypeDef,
    DeletePrivateGraphEndpointOutputTypeDef,
    EmptyResponseMetadataTypeDef,
    ExecuteQueryInputRequestTypeDef,
    ExecuteQueryOutputTypeDef,
    GetGraphInputRequestTypeDef,
    GetGraphOutputTypeDef,
    GetGraphSnapshotInputRequestTypeDef,
    GetGraphSnapshotOutputTypeDef,
    GetGraphSummaryInputRequestTypeDef,
    GetGraphSummaryOutputTypeDef,
    GetImportTaskInputRequestTypeDef,
    GetImportTaskOutputTypeDef,
    GetPrivateGraphEndpointInputRequestTypeDef,
    GetPrivateGraphEndpointOutputTypeDef,
    GetQueryInputRequestTypeDef,
    GetQueryOutputTypeDef,
    ListGraphsInputRequestTypeDef,
    ListGraphSnapshotsInputRequestTypeDef,
    ListGraphSnapshotsOutputTypeDef,
    ListGraphsOutputTypeDef,
    ListImportTasksInputRequestTypeDef,
    ListImportTasksOutputTypeDef,
    ListPrivateGraphEndpointsInputRequestTypeDef,
    ListPrivateGraphEndpointsOutputTypeDef,
    ListQueriesInputRequestTypeDef,
    ListQueriesOutputTypeDef,
    ListTagsForResourceInputRequestTypeDef,
    ListTagsForResourceOutputTypeDef,
    ResetGraphInputRequestTypeDef,
    ResetGraphOutputTypeDef,
    RestoreGraphFromSnapshotInputRequestTypeDef,
    RestoreGraphFromSnapshotOutputTypeDef,
    StartImportTaskInputRequestTypeDef,
    StartImportTaskOutputTypeDef,
    TagResourceInputRequestTypeDef,
    UntagResourceInputRequestTypeDef,
    UpdateGraphInputRequestTypeDef,
    UpdateGraphOutputTypeDef,
)
from .waiter import (
    GraphAvailableWaiter,
    GraphDeletedWaiter,
    GraphSnapshotAvailableWaiter,
    GraphSnapshotDeletedWaiter,
    ImportTaskCancelledWaiter,
    ImportTaskSuccessfulWaiter,
    PrivateGraphEndpointAvailableWaiter,
    PrivateGraphEndpointDeletedWaiter,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("NeptuneGraphClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnprocessableException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class NeptuneGraphClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        NeptuneGraphClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#can_paginate)
        """

    def cancel_import_task(
        self, **kwargs: Unpack[CancelImportTaskInputRequestTypeDef]
    ) -> CancelImportTaskOutputTypeDef:
        """
        Deletes the specified import task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.cancel_import_task)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#cancel_import_task)
        """

    def cancel_query(
        self, **kwargs: Unpack[CancelQueryInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Cancels a specified query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.cancel_query)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#cancel_query)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#close)
        """

    def create_graph(
        self, **kwargs: Unpack[CreateGraphInputRequestTypeDef]
    ) -> CreateGraphOutputTypeDef:
        """
        Creates a new Neptune Analytics graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.create_graph)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#create_graph)
        """

    def create_graph_snapshot(
        self, **kwargs: Unpack[CreateGraphSnapshotInputRequestTypeDef]
    ) -> CreateGraphSnapshotOutputTypeDef:
        """
        Creates a snapshot of the specific graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.create_graph_snapshot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#create_graph_snapshot)
        """

    def create_graph_using_import_task(
        self, **kwargs: Unpack[CreateGraphUsingImportTaskInputRequestTypeDef]
    ) -> CreateGraphUsingImportTaskOutputTypeDef:
        """
        Creates a new Neptune Analytics graph and imports data into it, either from
        Amazon Simple Storage Service (S3) or from a Neptune database or a Neptune
        database
        snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.create_graph_using_import_task)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#create_graph_using_import_task)
        """

    def create_private_graph_endpoint(
        self, **kwargs: Unpack[CreatePrivateGraphEndpointInputRequestTypeDef]
    ) -> CreatePrivateGraphEndpointOutputTypeDef:
        """
        Create a private graph endpoint to allow private access from to the graph from
        within a
        VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.create_private_graph_endpoint)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#create_private_graph_endpoint)
        """

    def delete_graph(
        self, **kwargs: Unpack[DeleteGraphInputRequestTypeDef]
    ) -> DeleteGraphOutputTypeDef:
        """
        Deletes the specified graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.delete_graph)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#delete_graph)
        """

    def delete_graph_snapshot(
        self, **kwargs: Unpack[DeleteGraphSnapshotInputRequestTypeDef]
    ) -> DeleteGraphSnapshotOutputTypeDef:
        """
        Deletes the specifed graph snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.delete_graph_snapshot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#delete_graph_snapshot)
        """

    def delete_private_graph_endpoint(
        self, **kwargs: Unpack[DeletePrivateGraphEndpointInputRequestTypeDef]
    ) -> DeletePrivateGraphEndpointOutputTypeDef:
        """
        Deletes a private graph endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.delete_private_graph_endpoint)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#delete_private_graph_endpoint)
        """

    def execute_query(
        self, **kwargs: Unpack[ExecuteQueryInputRequestTypeDef]
    ) -> ExecuteQueryOutputTypeDef:
        """
        Execute an openCypher query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.execute_query)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#execute_query)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#generate_presigned_url)
        """

    def get_graph(self, **kwargs: Unpack[GetGraphInputRequestTypeDef]) -> GetGraphOutputTypeDef:
        """
        Gets information about a specified graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_graph)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#get_graph)
        """

    def get_graph_snapshot(
        self, **kwargs: Unpack[GetGraphSnapshotInputRequestTypeDef]
    ) -> GetGraphSnapshotOutputTypeDef:
        """
        Retrieves a specified graph snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_graph_snapshot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#get_graph_snapshot)
        """

    def get_graph_summary(
        self, **kwargs: Unpack[GetGraphSummaryInputRequestTypeDef]
    ) -> GetGraphSummaryOutputTypeDef:
        """
        Gets a graph summary for a property graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_graph_summary)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#get_graph_summary)
        """

    def get_import_task(
        self, **kwargs: Unpack[GetImportTaskInputRequestTypeDef]
    ) -> GetImportTaskOutputTypeDef:
        """
        Retrieves a specified import task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_import_task)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#get_import_task)
        """

    def get_private_graph_endpoint(
        self, **kwargs: Unpack[GetPrivateGraphEndpointInputRequestTypeDef]
    ) -> GetPrivateGraphEndpointOutputTypeDef:
        """
        Retrieves information about a specified private endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_private_graph_endpoint)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#get_private_graph_endpoint)
        """

    def get_query(self, **kwargs: Unpack[GetQueryInputRequestTypeDef]) -> GetQueryOutputTypeDef:
        """
        Retrieves the status of a specified query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_query)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#get_query)
        """

    def list_graph_snapshots(
        self, **kwargs: Unpack[ListGraphSnapshotsInputRequestTypeDef]
    ) -> ListGraphSnapshotsOutputTypeDef:
        """
        Lists available snapshots of a specified Neptune Analytics graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.list_graph_snapshots)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#list_graph_snapshots)
        """

    def list_graphs(
        self, **kwargs: Unpack[ListGraphsInputRequestTypeDef]
    ) -> ListGraphsOutputTypeDef:
        """
        Lists available Neptune Analytics graphs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.list_graphs)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#list_graphs)
        """

    def list_import_tasks(
        self, **kwargs: Unpack[ListImportTasksInputRequestTypeDef]
    ) -> ListImportTasksOutputTypeDef:
        """
        Lists import tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.list_import_tasks)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#list_import_tasks)
        """

    def list_private_graph_endpoints(
        self, **kwargs: Unpack[ListPrivateGraphEndpointsInputRequestTypeDef]
    ) -> ListPrivateGraphEndpointsOutputTypeDef:
        """
        Lists private endpoints for a specified Neptune Analytics graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.list_private_graph_endpoints)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#list_private_graph_endpoints)
        """

    def list_queries(
        self, **kwargs: Unpack[ListQueriesInputRequestTypeDef]
    ) -> ListQueriesOutputTypeDef:
        """
        Lists active openCypher queries.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.list_queries)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#list_queries)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputRequestTypeDef]
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Lists tags associated with a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.list_tags_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#list_tags_for_resource)
        """

    def reset_graph(
        self, **kwargs: Unpack[ResetGraphInputRequestTypeDef]
    ) -> ResetGraphOutputTypeDef:
        """
        Empties the data from a specified Neptune Analytics graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.reset_graph)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#reset_graph)
        """

    def restore_graph_from_snapshot(
        self, **kwargs: Unpack[RestoreGraphFromSnapshotInputRequestTypeDef]
    ) -> RestoreGraphFromSnapshotOutputTypeDef:
        """
        Restores a graph from a snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.restore_graph_from_snapshot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#restore_graph_from_snapshot)
        """

    def start_import_task(
        self, **kwargs: Unpack[StartImportTaskInputRequestTypeDef]
    ) -> StartImportTaskOutputTypeDef:
        """
        Import data into existing Neptune Analytics graph from Amazon Simple Storage
        Service
        (S3).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.start_import_task)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#start_import_task)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceInputRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceInputRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#untag_resource)
        """

    def update_graph(
        self, **kwargs: Unpack[UpdateGraphInputRequestTypeDef]
    ) -> UpdateGraphOutputTypeDef:
        """
        Updates the configuration of a specified Neptune Analytics graph See also: [AWS
        API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/neptune-graph-2023-11-29/UpdateGraph).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.update_graph)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#update_graph)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_graph_snapshots"]
    ) -> ListGraphSnapshotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_graphs"]) -> ListGraphsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_import_tasks"]
    ) -> ListImportTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_private_graph_endpoints"]
    ) -> ListPrivateGraphEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#get_paginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["graph_available"]) -> GraphAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["graph_deleted"]) -> GraphDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["graph_snapshot_available"]
    ) -> GraphSnapshotAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["graph_snapshot_deleted"]
    ) -> GraphSnapshotDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["import_task_cancelled"]
    ) -> ImportTaskCancelledWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["import_task_successful"]
    ) -> ImportTaskSuccessfulWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["private_graph_endpoint_available"]
    ) -> PrivateGraphEndpointAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["private_graph_endpoint_deleted"]
    ) -> PrivateGraphEndpointDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html#NeptuneGraph.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client/#get_waiter)
        """
