"""
Type annotations for neptune-graph service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/type_defs/)

Usage::

    ```python
    from mypy_boto3_neptune_graph.type_defs import CancelImportTaskInputRequestTypeDef

    data: CancelImportTaskInputRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence

from botocore.response import StreamingBody

from .literals import (
    ExplainModeType,
    FormatType,
    GraphStatusType,
    GraphSummaryModeType,
    ImportTaskStatusType,
    PlanCacheTypeType,
    PrivateGraphEndpointStatusType,
    QueryStateInputType,
    QueryStateType,
    SnapshotStatusType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "CancelImportTaskInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CancelQueryInputRequestTypeDef",
    "VectorSearchConfigurationTypeDef",
    "CreateGraphSnapshotInputRequestTypeDef",
    "CreatePrivateGraphEndpointInputRequestTypeDef",
    "DeleteGraphInputRequestTypeDef",
    "DeleteGraphSnapshotInputRequestTypeDef",
    "DeletePrivateGraphEndpointInputRequestTypeDef",
    "EdgeStructureTypeDef",
    "ExecuteQueryInputRequestTypeDef",
    "WaiterConfigTypeDef",
    "GetGraphInputRequestTypeDef",
    "GetGraphSnapshotInputRequestTypeDef",
    "GetGraphSummaryInputRequestTypeDef",
    "GetImportTaskInputRequestTypeDef",
    "ImportTaskDetailsTypeDef",
    "GetPrivateGraphEndpointInputRequestTypeDef",
    "GetQueryInputRequestTypeDef",
    "NodeStructureTypeDef",
    "GraphSnapshotSummaryTypeDef",
    "GraphSummaryTypeDef",
    "NeptuneImportOptionsTypeDef",
    "ImportTaskSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "ListGraphSnapshotsInputRequestTypeDef",
    "ListGraphsInputRequestTypeDef",
    "ListImportTasksInputRequestTypeDef",
    "ListPrivateGraphEndpointsInputRequestTypeDef",
    "PrivateGraphEndpointSummaryTypeDef",
    "ListQueriesInputRequestTypeDef",
    "QuerySummaryTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ResetGraphInputRequestTypeDef",
    "RestoreGraphFromSnapshotInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateGraphInputRequestTypeDef",
    "CancelImportTaskOutputTypeDef",
    "CreateGraphSnapshotOutputTypeDef",
    "CreatePrivateGraphEndpointOutputTypeDef",
    "DeleteGraphSnapshotOutputTypeDef",
    "DeletePrivateGraphEndpointOutputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ExecuteQueryOutputTypeDef",
    "GetGraphSnapshotOutputTypeDef",
    "GetPrivateGraphEndpointOutputTypeDef",
    "GetQueryOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "CreateGraphInputRequestTypeDef",
    "CreateGraphOutputTypeDef",
    "DeleteGraphOutputTypeDef",
    "GetGraphOutputTypeDef",
    "ResetGraphOutputTypeDef",
    "RestoreGraphFromSnapshotOutputTypeDef",
    "UpdateGraphOutputTypeDef",
    "GetGraphInputGraphAvailableWaitTypeDef",
    "GetGraphInputGraphDeletedWaitTypeDef",
    "GetGraphSnapshotInputGraphSnapshotAvailableWaitTypeDef",
    "GetGraphSnapshotInputGraphSnapshotDeletedWaitTypeDef",
    "GetImportTaskInputImportTaskCancelledWaitTypeDef",
    "GetImportTaskInputImportTaskSuccessfulWaitTypeDef",
    "GetPrivateGraphEndpointInputPrivateGraphEndpointAvailableWaitTypeDef",
    "GetPrivateGraphEndpointInputPrivateGraphEndpointDeletedWaitTypeDef",
    "GraphDataSummaryTypeDef",
    "ListGraphSnapshotsOutputTypeDef",
    "ListGraphsOutputTypeDef",
    "ImportOptionsTypeDef",
    "ListImportTasksOutputTypeDef",
    "ListGraphSnapshotsInputListGraphSnapshotsPaginateTypeDef",
    "ListGraphsInputListGraphsPaginateTypeDef",
    "ListImportTasksInputListImportTasksPaginateTypeDef",
    "ListPrivateGraphEndpointsInputListPrivateGraphEndpointsPaginateTypeDef",
    "ListPrivateGraphEndpointsOutputTypeDef",
    "ListQueriesOutputTypeDef",
    "GetGraphSummaryOutputTypeDef",
    "CreateGraphUsingImportTaskInputRequestTypeDef",
    "CreateGraphUsingImportTaskOutputTypeDef",
    "GetImportTaskOutputTypeDef",
    "StartImportTaskInputRequestTypeDef",
    "StartImportTaskOutputTypeDef",
)

CancelImportTaskInputRequestTypeDef = TypedDict(
    "CancelImportTaskInputRequestTypeDef",
    {
        "taskIdentifier": str,
    },
)
ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
        "HostId": NotRequired[str],
    },
)
CancelQueryInputRequestTypeDef = TypedDict(
    "CancelQueryInputRequestTypeDef",
    {
        "graphIdentifier": str,
        "queryId": str,
    },
)
VectorSearchConfigurationTypeDef = TypedDict(
    "VectorSearchConfigurationTypeDef",
    {
        "dimension": int,
    },
)
CreateGraphSnapshotInputRequestTypeDef = TypedDict(
    "CreateGraphSnapshotInputRequestTypeDef",
    {
        "graphIdentifier": str,
        "snapshotName": str,
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreatePrivateGraphEndpointInputRequestTypeDef = TypedDict(
    "CreatePrivateGraphEndpointInputRequestTypeDef",
    {
        "graphIdentifier": str,
        "vpcId": NotRequired[str],
        "subnetIds": NotRequired[Sequence[str]],
        "vpcSecurityGroupIds": NotRequired[Sequence[str]],
    },
)
DeleteGraphInputRequestTypeDef = TypedDict(
    "DeleteGraphInputRequestTypeDef",
    {
        "graphIdentifier": str,
        "skipSnapshot": bool,
    },
)
DeleteGraphSnapshotInputRequestTypeDef = TypedDict(
    "DeleteGraphSnapshotInputRequestTypeDef",
    {
        "snapshotIdentifier": str,
    },
)
DeletePrivateGraphEndpointInputRequestTypeDef = TypedDict(
    "DeletePrivateGraphEndpointInputRequestTypeDef",
    {
        "graphIdentifier": str,
        "vpcId": str,
    },
)
EdgeStructureTypeDef = TypedDict(
    "EdgeStructureTypeDef",
    {
        "count": NotRequired[int],
        "edgeProperties": NotRequired[List[str]],
    },
)
ExecuteQueryInputRequestTypeDef = TypedDict(
    "ExecuteQueryInputRequestTypeDef",
    {
        "graphIdentifier": str,
        "queryString": str,
        "language": Literal["OPEN_CYPHER"],
        "parameters": NotRequired[Mapping[str, Mapping[str, Any]]],
        "planCache": NotRequired[PlanCacheTypeType],
        "explainMode": NotRequired[ExplainModeType],
        "queryTimeoutMilliseconds": NotRequired[int],
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
GetGraphInputRequestTypeDef = TypedDict(
    "GetGraphInputRequestTypeDef",
    {
        "graphIdentifier": str,
    },
)
GetGraphSnapshotInputRequestTypeDef = TypedDict(
    "GetGraphSnapshotInputRequestTypeDef",
    {
        "snapshotIdentifier": str,
    },
)
GetGraphSummaryInputRequestTypeDef = TypedDict(
    "GetGraphSummaryInputRequestTypeDef",
    {
        "graphIdentifier": str,
        "mode": NotRequired[GraphSummaryModeType],
    },
)
GetImportTaskInputRequestTypeDef = TypedDict(
    "GetImportTaskInputRequestTypeDef",
    {
        "taskIdentifier": str,
    },
)
ImportTaskDetailsTypeDef = TypedDict(
    "ImportTaskDetailsTypeDef",
    {
        "status": str,
        "startTime": datetime,
        "timeElapsedSeconds": int,
        "progressPercentage": int,
        "errorCount": int,
        "statementCount": int,
        "dictionaryEntryCount": int,
        "errorDetails": NotRequired[str],
    },
)
GetPrivateGraphEndpointInputRequestTypeDef = TypedDict(
    "GetPrivateGraphEndpointInputRequestTypeDef",
    {
        "graphIdentifier": str,
        "vpcId": str,
    },
)
GetQueryInputRequestTypeDef = TypedDict(
    "GetQueryInputRequestTypeDef",
    {
        "graphIdentifier": str,
        "queryId": str,
    },
)
NodeStructureTypeDef = TypedDict(
    "NodeStructureTypeDef",
    {
        "count": NotRequired[int],
        "nodeProperties": NotRequired[List[str]],
        "distinctOutgoingEdgeLabels": NotRequired[List[str]],
    },
)
GraphSnapshotSummaryTypeDef = TypedDict(
    "GraphSnapshotSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "sourceGraphId": NotRequired[str],
        "snapshotCreateTime": NotRequired[datetime],
        "status": NotRequired[SnapshotStatusType],
        "kmsKeyIdentifier": NotRequired[str],
    },
)
GraphSummaryTypeDef = TypedDict(
    "GraphSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "status": NotRequired[GraphStatusType],
        "provisionedMemory": NotRequired[int],
        "publicConnectivity": NotRequired[bool],
        "endpoint": NotRequired[str],
        "replicaCount": NotRequired[int],
        "kmsKeyIdentifier": NotRequired[str],
        "deletionProtection": NotRequired[bool],
    },
)
NeptuneImportOptionsTypeDef = TypedDict(
    "NeptuneImportOptionsTypeDef",
    {
        "s3ExportPath": str,
        "s3ExportKmsKeyId": str,
        "preserveDefaultVertexLabels": NotRequired[bool],
        "preserveEdgeIds": NotRequired[bool],
    },
)
ImportTaskSummaryTypeDef = TypedDict(
    "ImportTaskSummaryTypeDef",
    {
        "taskId": str,
        "source": str,
        "roleArn": str,
        "status": ImportTaskStatusType,
        "graphId": NotRequired[str],
        "format": NotRequired[FormatType],
    },
)
PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
    },
)
ListGraphSnapshotsInputRequestTypeDef = TypedDict(
    "ListGraphSnapshotsInputRequestTypeDef",
    {
        "graphIdentifier": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListGraphsInputRequestTypeDef = TypedDict(
    "ListGraphsInputRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListImportTasksInputRequestTypeDef = TypedDict(
    "ListImportTasksInputRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListPrivateGraphEndpointsInputRequestTypeDef = TypedDict(
    "ListPrivateGraphEndpointsInputRequestTypeDef",
    {
        "graphIdentifier": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
PrivateGraphEndpointSummaryTypeDef = TypedDict(
    "PrivateGraphEndpointSummaryTypeDef",
    {
        "vpcId": str,
        "subnetIds": List[str],
        "status": PrivateGraphEndpointStatusType,
        "vpcEndpointId": NotRequired[str],
    },
)
ListQueriesInputRequestTypeDef = TypedDict(
    "ListQueriesInputRequestTypeDef",
    {
        "graphIdentifier": str,
        "maxResults": int,
        "state": NotRequired[QueryStateInputType],
    },
)
QuerySummaryTypeDef = TypedDict(
    "QuerySummaryTypeDef",
    {
        "id": NotRequired[str],
        "queryString": NotRequired[str],
        "waited": NotRequired[int],
        "elapsed": NotRequired[int],
        "state": NotRequired[QueryStateType],
    },
)
ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)
ResetGraphInputRequestTypeDef = TypedDict(
    "ResetGraphInputRequestTypeDef",
    {
        "graphIdentifier": str,
        "skipSnapshot": bool,
    },
)
RestoreGraphFromSnapshotInputRequestTypeDef = TypedDict(
    "RestoreGraphFromSnapshotInputRequestTypeDef",
    {
        "snapshotIdentifier": str,
        "graphName": str,
        "provisionedMemory": NotRequired[int],
        "deletionProtection": NotRequired[bool],
        "tags": NotRequired[Mapping[str, str]],
        "replicaCount": NotRequired[int],
        "publicConnectivity": NotRequired[bool],
    },
)
TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UpdateGraphInputRequestTypeDef = TypedDict(
    "UpdateGraphInputRequestTypeDef",
    {
        "graphIdentifier": str,
        "publicConnectivity": NotRequired[bool],
        "provisionedMemory": NotRequired[int],
        "deletionProtection": NotRequired[bool],
    },
)
CancelImportTaskOutputTypeDef = TypedDict(
    "CancelImportTaskOutputTypeDef",
    {
        "graphId": str,
        "taskId": str,
        "source": str,
        "format": FormatType,
        "roleArn": str,
        "status": ImportTaskStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGraphSnapshotOutputTypeDef = TypedDict(
    "CreateGraphSnapshotOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "sourceGraphId": str,
        "snapshotCreateTime": datetime,
        "status": SnapshotStatusType,
        "kmsKeyIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePrivateGraphEndpointOutputTypeDef = TypedDict(
    "CreatePrivateGraphEndpointOutputTypeDef",
    {
        "vpcId": str,
        "subnetIds": List[str],
        "status": PrivateGraphEndpointStatusType,
        "vpcEndpointId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteGraphSnapshotOutputTypeDef = TypedDict(
    "DeleteGraphSnapshotOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "sourceGraphId": str,
        "snapshotCreateTime": datetime,
        "status": SnapshotStatusType,
        "kmsKeyIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeletePrivateGraphEndpointOutputTypeDef = TypedDict(
    "DeletePrivateGraphEndpointOutputTypeDef",
    {
        "vpcId": str,
        "subnetIds": List[str],
        "status": PrivateGraphEndpointStatusType,
        "vpcEndpointId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExecuteQueryOutputTypeDef = TypedDict(
    "ExecuteQueryOutputTypeDef",
    {
        "payload": StreamingBody,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetGraphSnapshotOutputTypeDef = TypedDict(
    "GetGraphSnapshotOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "sourceGraphId": str,
        "snapshotCreateTime": datetime,
        "status": SnapshotStatusType,
        "kmsKeyIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPrivateGraphEndpointOutputTypeDef = TypedDict(
    "GetPrivateGraphEndpointOutputTypeDef",
    {
        "vpcId": str,
        "subnetIds": List[str],
        "status": PrivateGraphEndpointStatusType,
        "vpcEndpointId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetQueryOutputTypeDef = TypedDict(
    "GetQueryOutputTypeDef",
    {
        "id": str,
        "queryString": str,
        "waited": int,
        "elapsed": int,
        "state": QueryStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGraphInputRequestTypeDef = TypedDict(
    "CreateGraphInputRequestTypeDef",
    {
        "graphName": str,
        "provisionedMemory": int,
        "tags": NotRequired[Mapping[str, str]],
        "publicConnectivity": NotRequired[bool],
        "kmsKeyIdentifier": NotRequired[str],
        "vectorSearchConfiguration": NotRequired[VectorSearchConfigurationTypeDef],
        "replicaCount": NotRequired[int],
        "deletionProtection": NotRequired[bool],
    },
)
CreateGraphOutputTypeDef = TypedDict(
    "CreateGraphOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "status": GraphStatusType,
        "statusReason": str,
        "createTime": datetime,
        "provisionedMemory": int,
        "endpoint": str,
        "publicConnectivity": bool,
        "vectorSearchConfiguration": VectorSearchConfigurationTypeDef,
        "replicaCount": int,
        "kmsKeyIdentifier": str,
        "sourceSnapshotId": str,
        "deletionProtection": bool,
        "buildNumber": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteGraphOutputTypeDef = TypedDict(
    "DeleteGraphOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "status": GraphStatusType,
        "statusReason": str,
        "createTime": datetime,
        "provisionedMemory": int,
        "endpoint": str,
        "publicConnectivity": bool,
        "vectorSearchConfiguration": VectorSearchConfigurationTypeDef,
        "replicaCount": int,
        "kmsKeyIdentifier": str,
        "sourceSnapshotId": str,
        "deletionProtection": bool,
        "buildNumber": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetGraphOutputTypeDef = TypedDict(
    "GetGraphOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "status": GraphStatusType,
        "statusReason": str,
        "createTime": datetime,
        "provisionedMemory": int,
        "endpoint": str,
        "publicConnectivity": bool,
        "vectorSearchConfiguration": VectorSearchConfigurationTypeDef,
        "replicaCount": int,
        "kmsKeyIdentifier": str,
        "sourceSnapshotId": str,
        "deletionProtection": bool,
        "buildNumber": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResetGraphOutputTypeDef = TypedDict(
    "ResetGraphOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "status": GraphStatusType,
        "statusReason": str,
        "createTime": datetime,
        "provisionedMemory": int,
        "endpoint": str,
        "publicConnectivity": bool,
        "vectorSearchConfiguration": VectorSearchConfigurationTypeDef,
        "replicaCount": int,
        "kmsKeyIdentifier": str,
        "sourceSnapshotId": str,
        "deletionProtection": bool,
        "buildNumber": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreGraphFromSnapshotOutputTypeDef = TypedDict(
    "RestoreGraphFromSnapshotOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "status": GraphStatusType,
        "statusReason": str,
        "createTime": datetime,
        "provisionedMemory": int,
        "endpoint": str,
        "publicConnectivity": bool,
        "vectorSearchConfiguration": VectorSearchConfigurationTypeDef,
        "replicaCount": int,
        "kmsKeyIdentifier": str,
        "sourceSnapshotId": str,
        "deletionProtection": bool,
        "buildNumber": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateGraphOutputTypeDef = TypedDict(
    "UpdateGraphOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "status": GraphStatusType,
        "statusReason": str,
        "createTime": datetime,
        "provisionedMemory": int,
        "endpoint": str,
        "publicConnectivity": bool,
        "vectorSearchConfiguration": VectorSearchConfigurationTypeDef,
        "replicaCount": int,
        "kmsKeyIdentifier": str,
        "sourceSnapshotId": str,
        "deletionProtection": bool,
        "buildNumber": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetGraphInputGraphAvailableWaitTypeDef = TypedDict(
    "GetGraphInputGraphAvailableWaitTypeDef",
    {
        "graphIdentifier": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetGraphInputGraphDeletedWaitTypeDef = TypedDict(
    "GetGraphInputGraphDeletedWaitTypeDef",
    {
        "graphIdentifier": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetGraphSnapshotInputGraphSnapshotAvailableWaitTypeDef = TypedDict(
    "GetGraphSnapshotInputGraphSnapshotAvailableWaitTypeDef",
    {
        "snapshotIdentifier": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetGraphSnapshotInputGraphSnapshotDeletedWaitTypeDef = TypedDict(
    "GetGraphSnapshotInputGraphSnapshotDeletedWaitTypeDef",
    {
        "snapshotIdentifier": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetImportTaskInputImportTaskCancelledWaitTypeDef = TypedDict(
    "GetImportTaskInputImportTaskCancelledWaitTypeDef",
    {
        "taskIdentifier": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetImportTaskInputImportTaskSuccessfulWaitTypeDef = TypedDict(
    "GetImportTaskInputImportTaskSuccessfulWaitTypeDef",
    {
        "taskIdentifier": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetPrivateGraphEndpointInputPrivateGraphEndpointAvailableWaitTypeDef = TypedDict(
    "GetPrivateGraphEndpointInputPrivateGraphEndpointAvailableWaitTypeDef",
    {
        "graphIdentifier": str,
        "vpcId": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetPrivateGraphEndpointInputPrivateGraphEndpointDeletedWaitTypeDef = TypedDict(
    "GetPrivateGraphEndpointInputPrivateGraphEndpointDeletedWaitTypeDef",
    {
        "graphIdentifier": str,
        "vpcId": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GraphDataSummaryTypeDef = TypedDict(
    "GraphDataSummaryTypeDef",
    {
        "numNodes": NotRequired[int],
        "numEdges": NotRequired[int],
        "numNodeLabels": NotRequired[int],
        "numEdgeLabels": NotRequired[int],
        "nodeLabels": NotRequired[List[str]],
        "edgeLabels": NotRequired[List[str]],
        "numNodeProperties": NotRequired[int],
        "numEdgeProperties": NotRequired[int],
        "nodeProperties": NotRequired[List[Dict[str, int]]],
        "edgeProperties": NotRequired[List[Dict[str, int]]],
        "totalNodePropertyValues": NotRequired[int],
        "totalEdgePropertyValues": NotRequired[int],
        "nodeStructures": NotRequired[List[NodeStructureTypeDef]],
        "edgeStructures": NotRequired[List[EdgeStructureTypeDef]],
    },
)
ListGraphSnapshotsOutputTypeDef = TypedDict(
    "ListGraphSnapshotsOutputTypeDef",
    {
        "graphSnapshots": List[GraphSnapshotSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListGraphsOutputTypeDef = TypedDict(
    "ListGraphsOutputTypeDef",
    {
        "graphs": List[GraphSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportOptionsTypeDef = TypedDict(
    "ImportOptionsTypeDef",
    {
        "neptune": NotRequired[NeptuneImportOptionsTypeDef],
    },
)
ListImportTasksOutputTypeDef = TypedDict(
    "ListImportTasksOutputTypeDef",
    {
        "tasks": List[ImportTaskSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListGraphSnapshotsInputListGraphSnapshotsPaginateTypeDef = TypedDict(
    "ListGraphSnapshotsInputListGraphSnapshotsPaginateTypeDef",
    {
        "graphIdentifier": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGraphsInputListGraphsPaginateTypeDef = TypedDict(
    "ListGraphsInputListGraphsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListImportTasksInputListImportTasksPaginateTypeDef = TypedDict(
    "ListImportTasksInputListImportTasksPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPrivateGraphEndpointsInputListPrivateGraphEndpointsPaginateTypeDef = TypedDict(
    "ListPrivateGraphEndpointsInputListPrivateGraphEndpointsPaginateTypeDef",
    {
        "graphIdentifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPrivateGraphEndpointsOutputTypeDef = TypedDict(
    "ListPrivateGraphEndpointsOutputTypeDef",
    {
        "privateGraphEndpoints": List[PrivateGraphEndpointSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListQueriesOutputTypeDef = TypedDict(
    "ListQueriesOutputTypeDef",
    {
        "queries": List[QuerySummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetGraphSummaryOutputTypeDef = TypedDict(
    "GetGraphSummaryOutputTypeDef",
    {
        "version": str,
        "lastStatisticsComputationTime": datetime,
        "graphSummary": GraphDataSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGraphUsingImportTaskInputRequestTypeDef = TypedDict(
    "CreateGraphUsingImportTaskInputRequestTypeDef",
    {
        "graphName": str,
        "source": str,
        "roleArn": str,
        "tags": NotRequired[Mapping[str, str]],
        "publicConnectivity": NotRequired[bool],
        "kmsKeyIdentifier": NotRequired[str],
        "vectorSearchConfiguration": NotRequired[VectorSearchConfigurationTypeDef],
        "replicaCount": NotRequired[int],
        "deletionProtection": NotRequired[bool],
        "importOptions": NotRequired[ImportOptionsTypeDef],
        "maxProvisionedMemory": NotRequired[int],
        "minProvisionedMemory": NotRequired[int],
        "failOnError": NotRequired[bool],
        "format": NotRequired[FormatType],
        "blankNodeHandling": NotRequired[Literal["convertToIri"]],
    },
)
CreateGraphUsingImportTaskOutputTypeDef = TypedDict(
    "CreateGraphUsingImportTaskOutputTypeDef",
    {
        "graphId": str,
        "taskId": str,
        "source": str,
        "format": FormatType,
        "roleArn": str,
        "status": ImportTaskStatusType,
        "importOptions": ImportOptionsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetImportTaskOutputTypeDef = TypedDict(
    "GetImportTaskOutputTypeDef",
    {
        "graphId": str,
        "taskId": str,
        "source": str,
        "format": FormatType,
        "roleArn": str,
        "status": ImportTaskStatusType,
        "importOptions": ImportOptionsTypeDef,
        "importTaskDetails": ImportTaskDetailsTypeDef,
        "attemptNumber": int,
        "statusReason": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartImportTaskInputRequestTypeDef = TypedDict(
    "StartImportTaskInputRequestTypeDef",
    {
        "source": str,
        "graphIdentifier": str,
        "roleArn": str,
        "importOptions": NotRequired[ImportOptionsTypeDef],
        "failOnError": NotRequired[bool],
        "format": NotRequired[FormatType],
        "blankNodeHandling": NotRequired[Literal["convertToIri"]],
    },
)
StartImportTaskOutputTypeDef = TypedDict(
    "StartImportTaskOutputTypeDef",
    {
        "graphId": str,
        "taskId": str,
        "source": str,
        "format": FormatType,
        "roleArn": str,
        "status": ImportTaskStatusType,
        "importOptions": ImportOptionsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
