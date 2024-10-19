"""
Type annotations for docdb-elastic service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/type_defs/)

Usage::

    ```python
    from mypy_boto3_docdb_elastic.type_defs import ClusterInListTypeDef

    data: ClusterInListTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Mapping, Sequence

from .literals import AuthType, SnapshotTypeType, StatusType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "ClusterInListTypeDef",
    "ClusterSnapshotInListTypeDef",
    "ClusterSnapshotTypeDef",
    "ShardTypeDef",
    "CopyClusterSnapshotInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CreateClusterInputRequestTypeDef",
    "CreateClusterSnapshotInputRequestTypeDef",
    "DeleteClusterInputRequestTypeDef",
    "DeleteClusterSnapshotInputRequestTypeDef",
    "GetClusterInputRequestTypeDef",
    "GetClusterSnapshotInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListClusterSnapshotsInputRequestTypeDef",
    "ListClustersInputRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "RestoreClusterFromSnapshotInputRequestTypeDef",
    "StartClusterInputRequestTypeDef",
    "StopClusterInputRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateClusterInputRequestTypeDef",
    "ClusterTypeDef",
    "CopyClusterSnapshotOutputTypeDef",
    "CreateClusterSnapshotOutputTypeDef",
    "DeleteClusterSnapshotOutputTypeDef",
    "GetClusterSnapshotOutputTypeDef",
    "ListClusterSnapshotsOutputTypeDef",
    "ListClustersOutputTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListClusterSnapshotsInputListClusterSnapshotsPaginateTypeDef",
    "ListClustersInputListClustersPaginateTypeDef",
    "CreateClusterOutputTypeDef",
    "DeleteClusterOutputTypeDef",
    "GetClusterOutputTypeDef",
    "RestoreClusterFromSnapshotOutputTypeDef",
    "StartClusterOutputTypeDef",
    "StopClusterOutputTypeDef",
    "UpdateClusterOutputTypeDef",
)

ClusterInListTypeDef = TypedDict(
    "ClusterInListTypeDef",
    {
        "clusterArn": str,
        "clusterName": str,
        "status": StatusType,
    },
)
ClusterSnapshotInListTypeDef = TypedDict(
    "ClusterSnapshotInListTypeDef",
    {
        "clusterArn": str,
        "snapshotArn": str,
        "snapshotCreationTime": str,
        "snapshotName": str,
        "status": StatusType,
    },
)
ClusterSnapshotTypeDef = TypedDict(
    "ClusterSnapshotTypeDef",
    {
        "adminUserName": str,
        "clusterArn": str,
        "clusterCreationTime": str,
        "kmsKeyId": str,
        "snapshotArn": str,
        "snapshotCreationTime": str,
        "snapshotName": str,
        "status": StatusType,
        "subnetIds": List[str],
        "vpcSecurityGroupIds": List[str],
        "snapshotType": NotRequired[SnapshotTypeType],
    },
)
ShardTypeDef = TypedDict(
    "ShardTypeDef",
    {
        "createTime": str,
        "shardId": str,
        "status": StatusType,
    },
)
CopyClusterSnapshotInputRequestTypeDef = TypedDict(
    "CopyClusterSnapshotInputRequestTypeDef",
    {
        "snapshotArn": str,
        "targetSnapshotName": str,
        "copyTags": NotRequired[bool],
        "kmsKeyId": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
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
CreateClusterInputRequestTypeDef = TypedDict(
    "CreateClusterInputRequestTypeDef",
    {
        "adminUserName": str,
        "adminUserPassword": str,
        "authType": AuthType,
        "clusterName": str,
        "shardCapacity": int,
        "shardCount": int,
        "backupRetentionPeriod": NotRequired[int],
        "clientToken": NotRequired[str],
        "kmsKeyId": NotRequired[str],
        "preferredBackupWindow": NotRequired[str],
        "preferredMaintenanceWindow": NotRequired[str],
        "shardInstanceCount": NotRequired[int],
        "subnetIds": NotRequired[Sequence[str]],
        "tags": NotRequired[Mapping[str, str]],
        "vpcSecurityGroupIds": NotRequired[Sequence[str]],
    },
)
CreateClusterSnapshotInputRequestTypeDef = TypedDict(
    "CreateClusterSnapshotInputRequestTypeDef",
    {
        "clusterArn": str,
        "snapshotName": str,
        "tags": NotRequired[Mapping[str, str]],
    },
)
DeleteClusterInputRequestTypeDef = TypedDict(
    "DeleteClusterInputRequestTypeDef",
    {
        "clusterArn": str,
    },
)
DeleteClusterSnapshotInputRequestTypeDef = TypedDict(
    "DeleteClusterSnapshotInputRequestTypeDef",
    {
        "snapshotArn": str,
    },
)
GetClusterInputRequestTypeDef = TypedDict(
    "GetClusterInputRequestTypeDef",
    {
        "clusterArn": str,
    },
)
GetClusterSnapshotInputRequestTypeDef = TypedDict(
    "GetClusterSnapshotInputRequestTypeDef",
    {
        "snapshotArn": str,
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
ListClusterSnapshotsInputRequestTypeDef = TypedDict(
    "ListClusterSnapshotsInputRequestTypeDef",
    {
        "clusterArn": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "snapshotType": NotRequired[str],
    },
)
ListClustersInputRequestTypeDef = TypedDict(
    "ListClustersInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
RestoreClusterFromSnapshotInputRequestTypeDef = TypedDict(
    "RestoreClusterFromSnapshotInputRequestTypeDef",
    {
        "clusterName": str,
        "snapshotArn": str,
        "kmsKeyId": NotRequired[str],
        "shardCapacity": NotRequired[int],
        "shardInstanceCount": NotRequired[int],
        "subnetIds": NotRequired[Sequence[str]],
        "tags": NotRequired[Mapping[str, str]],
        "vpcSecurityGroupIds": NotRequired[Sequence[str]],
    },
)
StartClusterInputRequestTypeDef = TypedDict(
    "StartClusterInputRequestTypeDef",
    {
        "clusterArn": str,
    },
)
StopClusterInputRequestTypeDef = TypedDict(
    "StopClusterInputRequestTypeDef",
    {
        "clusterArn": str,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UpdateClusterInputRequestTypeDef = TypedDict(
    "UpdateClusterInputRequestTypeDef",
    {
        "clusterArn": str,
        "adminUserPassword": NotRequired[str],
        "authType": NotRequired[AuthType],
        "backupRetentionPeriod": NotRequired[int],
        "clientToken": NotRequired[str],
        "preferredBackupWindow": NotRequired[str],
        "preferredMaintenanceWindow": NotRequired[str],
        "shardCapacity": NotRequired[int],
        "shardCount": NotRequired[int],
        "shardInstanceCount": NotRequired[int],
        "subnetIds": NotRequired[Sequence[str]],
        "vpcSecurityGroupIds": NotRequired[Sequence[str]],
    },
)
ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "adminUserName": str,
        "authType": AuthType,
        "clusterArn": str,
        "clusterEndpoint": str,
        "clusterName": str,
        "createTime": str,
        "kmsKeyId": str,
        "preferredMaintenanceWindow": str,
        "shardCapacity": int,
        "shardCount": int,
        "status": StatusType,
        "subnetIds": List[str],
        "vpcSecurityGroupIds": List[str],
        "backupRetentionPeriod": NotRequired[int],
        "preferredBackupWindow": NotRequired[str],
        "shardInstanceCount": NotRequired[int],
        "shards": NotRequired[List[ShardTypeDef]],
    },
)
CopyClusterSnapshotOutputTypeDef = TypedDict(
    "CopyClusterSnapshotOutputTypeDef",
    {
        "snapshot": ClusterSnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateClusterSnapshotOutputTypeDef = TypedDict(
    "CreateClusterSnapshotOutputTypeDef",
    {
        "snapshot": ClusterSnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteClusterSnapshotOutputTypeDef = TypedDict(
    "DeleteClusterSnapshotOutputTypeDef",
    {
        "snapshot": ClusterSnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetClusterSnapshotOutputTypeDef = TypedDict(
    "GetClusterSnapshotOutputTypeDef",
    {
        "snapshot": ClusterSnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListClusterSnapshotsOutputTypeDef = TypedDict(
    "ListClusterSnapshotsOutputTypeDef",
    {
        "nextToken": str,
        "snapshots": List[ClusterSnapshotInListTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListClustersOutputTypeDef = TypedDict(
    "ListClustersOutputTypeDef",
    {
        "clusters": List[ClusterInListTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListClusterSnapshotsInputListClusterSnapshotsPaginateTypeDef = TypedDict(
    "ListClusterSnapshotsInputListClusterSnapshotsPaginateTypeDef",
    {
        "clusterArn": NotRequired[str],
        "snapshotType": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListClustersInputListClustersPaginateTypeDef = TypedDict(
    "ListClustersInputListClustersPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
CreateClusterOutputTypeDef = TypedDict(
    "CreateClusterOutputTypeDef",
    {
        "cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteClusterOutputTypeDef = TypedDict(
    "DeleteClusterOutputTypeDef",
    {
        "cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetClusterOutputTypeDef = TypedDict(
    "GetClusterOutputTypeDef",
    {
        "cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreClusterFromSnapshotOutputTypeDef = TypedDict(
    "RestoreClusterFromSnapshotOutputTypeDef",
    {
        "cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartClusterOutputTypeDef = TypedDict(
    "StartClusterOutputTypeDef",
    {
        "cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopClusterOutputTypeDef = TypedDict(
    "StopClusterOutputTypeDef",
    {
        "cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateClusterOutputTypeDef = TypedDict(
    "UpdateClusterOutputTypeDef",
    {
        "cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
