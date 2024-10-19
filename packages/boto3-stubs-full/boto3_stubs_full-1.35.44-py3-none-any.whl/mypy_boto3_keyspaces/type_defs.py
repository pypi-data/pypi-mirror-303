"""
Type annotations for keyspaces service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/type_defs/)

Usage::

    ```python
    from mypy_boto3_keyspaces.type_defs import TargetTrackingScalingPolicyConfigurationTypeDef

    data: TargetTrackingScalingPolicyConfigurationTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    EncryptionTypeType,
    PointInTimeRecoveryStatusType,
    RsType,
    SortOrderType,
    TableStatusType,
    ThroughputModeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "TargetTrackingScalingPolicyConfigurationTypeDef",
    "CapacitySpecificationSummaryTypeDef",
    "CapacitySpecificationTypeDef",
    "ClientSideTimestampsTypeDef",
    "ClusteringKeyTypeDef",
    "ColumnDefinitionTypeDef",
    "CommentTypeDef",
    "ReplicationSpecificationTypeDef",
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "EncryptionSpecificationTypeDef",
    "PointInTimeRecoveryTypeDef",
    "TimeToLiveTypeDef",
    "DeleteKeyspaceRequestRequestTypeDef",
    "DeleteTableRequestRequestTypeDef",
    "GetKeyspaceRequestRequestTypeDef",
    "GetTableAutoScalingSettingsRequestRequestTypeDef",
    "GetTableRequestRequestTypeDef",
    "PointInTimeRecoverySummaryTypeDef",
    "KeyspaceSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "ListKeyspacesRequestRequestTypeDef",
    "ListTablesRequestRequestTypeDef",
    "TableSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "PartitionKeyTypeDef",
    "TimestampTypeDef",
    "StaticColumnTypeDef",
    "AutoScalingPolicyTypeDef",
    "ReplicaSpecificationSummaryTypeDef",
    "CreateKeyspaceRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "CreateKeyspaceResponseTypeDef",
    "CreateTableResponseTypeDef",
    "GetKeyspaceResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "RestoreTableResponseTypeDef",
    "UpdateTableResponseTypeDef",
    "ListKeyspacesResponseTypeDef",
    "ListKeyspacesRequestListKeyspacesPaginateTypeDef",
    "ListTablesRequestListTablesPaginateTypeDef",
    "ListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    "ListTablesResponseTypeDef",
    "SchemaDefinitionOutputTypeDef",
    "SchemaDefinitionTypeDef",
    "AutoScalingSettingsTypeDef",
    "GetTableResponseTypeDef",
    "AutoScalingSpecificationTypeDef",
    "ReplicaSpecificationTypeDef",
    "ReplicaAutoScalingSpecificationTypeDef",
    "CreateTableRequestRequestTypeDef",
    "RestoreTableRequestRequestTypeDef",
    "UpdateTableRequestRequestTypeDef",
    "GetTableAutoScalingSettingsResponseTypeDef",
)

TargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "TargetTrackingScalingPolicyConfigurationTypeDef",
    {
        "targetValue": float,
        "disableScaleIn": NotRequired[bool],
        "scaleInCooldown": NotRequired[int],
        "scaleOutCooldown": NotRequired[int],
    },
)
CapacitySpecificationSummaryTypeDef = TypedDict(
    "CapacitySpecificationSummaryTypeDef",
    {
        "throughputMode": ThroughputModeType,
        "readCapacityUnits": NotRequired[int],
        "writeCapacityUnits": NotRequired[int],
        "lastUpdateToPayPerRequestTimestamp": NotRequired[datetime],
    },
)
CapacitySpecificationTypeDef = TypedDict(
    "CapacitySpecificationTypeDef",
    {
        "throughputMode": ThroughputModeType,
        "readCapacityUnits": NotRequired[int],
        "writeCapacityUnits": NotRequired[int],
    },
)
ClientSideTimestampsTypeDef = TypedDict(
    "ClientSideTimestampsTypeDef",
    {
        "status": Literal["ENABLED"],
    },
)
ClusteringKeyTypeDef = TypedDict(
    "ClusteringKeyTypeDef",
    {
        "name": str,
        "orderBy": SortOrderType,
    },
)
ColumnDefinitionTypeDef = TypedDict(
    "ColumnDefinitionTypeDef",
    {
        "name": str,
        "type": str,
    },
)
CommentTypeDef = TypedDict(
    "CommentTypeDef",
    {
        "message": str,
    },
)
ReplicationSpecificationTypeDef = TypedDict(
    "ReplicationSpecificationTypeDef",
    {
        "replicationStrategy": RsType,
        "regionList": NotRequired[Sequence[str]],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
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
EncryptionSpecificationTypeDef = TypedDict(
    "EncryptionSpecificationTypeDef",
    {
        "type": EncryptionTypeType,
        "kmsKeyIdentifier": NotRequired[str],
    },
)
PointInTimeRecoveryTypeDef = TypedDict(
    "PointInTimeRecoveryTypeDef",
    {
        "status": PointInTimeRecoveryStatusType,
    },
)
TimeToLiveTypeDef = TypedDict(
    "TimeToLiveTypeDef",
    {
        "status": Literal["ENABLED"],
    },
)
DeleteKeyspaceRequestRequestTypeDef = TypedDict(
    "DeleteKeyspaceRequestRequestTypeDef",
    {
        "keyspaceName": str,
    },
)
DeleteTableRequestRequestTypeDef = TypedDict(
    "DeleteTableRequestRequestTypeDef",
    {
        "keyspaceName": str,
        "tableName": str,
    },
)
GetKeyspaceRequestRequestTypeDef = TypedDict(
    "GetKeyspaceRequestRequestTypeDef",
    {
        "keyspaceName": str,
    },
)
GetTableAutoScalingSettingsRequestRequestTypeDef = TypedDict(
    "GetTableAutoScalingSettingsRequestRequestTypeDef",
    {
        "keyspaceName": str,
        "tableName": str,
    },
)
GetTableRequestRequestTypeDef = TypedDict(
    "GetTableRequestRequestTypeDef",
    {
        "keyspaceName": str,
        "tableName": str,
    },
)
PointInTimeRecoverySummaryTypeDef = TypedDict(
    "PointInTimeRecoverySummaryTypeDef",
    {
        "status": PointInTimeRecoveryStatusType,
        "earliestRestorableTimestamp": NotRequired[datetime],
    },
)
KeyspaceSummaryTypeDef = TypedDict(
    "KeyspaceSummaryTypeDef",
    {
        "keyspaceName": str,
        "resourceArn": str,
        "replicationStrategy": RsType,
        "replicationRegions": NotRequired[List[str]],
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
ListKeyspacesRequestRequestTypeDef = TypedDict(
    "ListKeyspacesRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListTablesRequestRequestTypeDef = TypedDict(
    "ListTablesRequestRequestTypeDef",
    {
        "keyspaceName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
TableSummaryTypeDef = TypedDict(
    "TableSummaryTypeDef",
    {
        "keyspaceName": str,
        "tableName": str,
        "resourceArn": str,
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
PartitionKeyTypeDef = TypedDict(
    "PartitionKeyTypeDef",
    {
        "name": str,
    },
)
TimestampTypeDef = Union[datetime, str]
StaticColumnTypeDef = TypedDict(
    "StaticColumnTypeDef",
    {
        "name": str,
    },
)
AutoScalingPolicyTypeDef = TypedDict(
    "AutoScalingPolicyTypeDef",
    {
        "targetTrackingScalingPolicyConfiguration": NotRequired[
            TargetTrackingScalingPolicyConfigurationTypeDef
        ],
    },
)
ReplicaSpecificationSummaryTypeDef = TypedDict(
    "ReplicaSpecificationSummaryTypeDef",
    {
        "region": NotRequired[str],
        "status": NotRequired[TableStatusType],
        "capacitySpecification": NotRequired[CapacitySpecificationSummaryTypeDef],
    },
)
CreateKeyspaceRequestRequestTypeDef = TypedDict(
    "CreateKeyspaceRequestRequestTypeDef",
    {
        "keyspaceName": str,
        "tags": NotRequired[Sequence[TagTypeDef]],
        "replicationSpecification": NotRequired[ReplicationSpecificationTypeDef],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[TagTypeDef],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[TagTypeDef],
    },
)
CreateKeyspaceResponseTypeDef = TypedDict(
    "CreateKeyspaceResponseTypeDef",
    {
        "resourceArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTableResponseTypeDef = TypedDict(
    "CreateTableResponseTypeDef",
    {
        "resourceArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetKeyspaceResponseTypeDef = TypedDict(
    "GetKeyspaceResponseTypeDef",
    {
        "keyspaceName": str,
        "resourceArn": str,
        "replicationStrategy": RsType,
        "replicationRegions": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "nextToken": str,
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreTableResponseTypeDef = TypedDict(
    "RestoreTableResponseTypeDef",
    {
        "restoredTableARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTableResponseTypeDef = TypedDict(
    "UpdateTableResponseTypeDef",
    {
        "resourceArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListKeyspacesResponseTypeDef = TypedDict(
    "ListKeyspacesResponseTypeDef",
    {
        "nextToken": str,
        "keyspaces": List[KeyspaceSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListKeyspacesRequestListKeyspacesPaginateTypeDef = TypedDict(
    "ListKeyspacesRequestListKeyspacesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTablesRequestListTablesPaginateTypeDef = TypedDict(
    "ListTablesRequestListTablesPaginateTypeDef",
    {
        "keyspaceName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTagsForResourceRequestListTagsForResourcePaginateTypeDef = TypedDict(
    "ListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    {
        "resourceArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTablesResponseTypeDef = TypedDict(
    "ListTablesResponseTypeDef",
    {
        "nextToken": str,
        "tables": List[TableSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SchemaDefinitionOutputTypeDef = TypedDict(
    "SchemaDefinitionOutputTypeDef",
    {
        "allColumns": List[ColumnDefinitionTypeDef],
        "partitionKeys": List[PartitionKeyTypeDef],
        "clusteringKeys": NotRequired[List[ClusteringKeyTypeDef]],
        "staticColumns": NotRequired[List[StaticColumnTypeDef]],
    },
)
SchemaDefinitionTypeDef = TypedDict(
    "SchemaDefinitionTypeDef",
    {
        "allColumns": Sequence[ColumnDefinitionTypeDef],
        "partitionKeys": Sequence[PartitionKeyTypeDef],
        "clusteringKeys": NotRequired[Sequence[ClusteringKeyTypeDef]],
        "staticColumns": NotRequired[Sequence[StaticColumnTypeDef]],
    },
)
AutoScalingSettingsTypeDef = TypedDict(
    "AutoScalingSettingsTypeDef",
    {
        "autoScalingDisabled": NotRequired[bool],
        "minimumUnits": NotRequired[int],
        "maximumUnits": NotRequired[int],
        "scalingPolicy": NotRequired[AutoScalingPolicyTypeDef],
    },
)
GetTableResponseTypeDef = TypedDict(
    "GetTableResponseTypeDef",
    {
        "keyspaceName": str,
        "tableName": str,
        "resourceArn": str,
        "creationTimestamp": datetime,
        "status": TableStatusType,
        "schemaDefinition": SchemaDefinitionOutputTypeDef,
        "capacitySpecification": CapacitySpecificationSummaryTypeDef,
        "encryptionSpecification": EncryptionSpecificationTypeDef,
        "pointInTimeRecovery": PointInTimeRecoverySummaryTypeDef,
        "ttl": TimeToLiveTypeDef,
        "defaultTimeToLive": int,
        "comment": CommentTypeDef,
        "clientSideTimestamps": ClientSideTimestampsTypeDef,
        "replicaSpecifications": List[ReplicaSpecificationSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AutoScalingSpecificationTypeDef = TypedDict(
    "AutoScalingSpecificationTypeDef",
    {
        "writeCapacityAutoScaling": NotRequired[AutoScalingSettingsTypeDef],
        "readCapacityAutoScaling": NotRequired[AutoScalingSettingsTypeDef],
    },
)
ReplicaSpecificationTypeDef = TypedDict(
    "ReplicaSpecificationTypeDef",
    {
        "region": str,
        "readCapacityUnits": NotRequired[int],
        "readCapacityAutoScaling": NotRequired[AutoScalingSettingsTypeDef],
    },
)
ReplicaAutoScalingSpecificationTypeDef = TypedDict(
    "ReplicaAutoScalingSpecificationTypeDef",
    {
        "region": NotRequired[str],
        "autoScalingSpecification": NotRequired[AutoScalingSpecificationTypeDef],
    },
)
CreateTableRequestRequestTypeDef = TypedDict(
    "CreateTableRequestRequestTypeDef",
    {
        "keyspaceName": str,
        "tableName": str,
        "schemaDefinition": SchemaDefinitionTypeDef,
        "comment": NotRequired[CommentTypeDef],
        "capacitySpecification": NotRequired[CapacitySpecificationTypeDef],
        "encryptionSpecification": NotRequired[EncryptionSpecificationTypeDef],
        "pointInTimeRecovery": NotRequired[PointInTimeRecoveryTypeDef],
        "ttl": NotRequired[TimeToLiveTypeDef],
        "defaultTimeToLive": NotRequired[int],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "clientSideTimestamps": NotRequired[ClientSideTimestampsTypeDef],
        "autoScalingSpecification": NotRequired[AutoScalingSpecificationTypeDef],
        "replicaSpecifications": NotRequired[Sequence[ReplicaSpecificationTypeDef]],
    },
)
RestoreTableRequestRequestTypeDef = TypedDict(
    "RestoreTableRequestRequestTypeDef",
    {
        "sourceKeyspaceName": str,
        "sourceTableName": str,
        "targetKeyspaceName": str,
        "targetTableName": str,
        "restoreTimestamp": NotRequired[TimestampTypeDef],
        "capacitySpecificationOverride": NotRequired[CapacitySpecificationTypeDef],
        "encryptionSpecificationOverride": NotRequired[EncryptionSpecificationTypeDef],
        "pointInTimeRecoveryOverride": NotRequired[PointInTimeRecoveryTypeDef],
        "tagsOverride": NotRequired[Sequence[TagTypeDef]],
        "autoScalingSpecification": NotRequired[AutoScalingSpecificationTypeDef],
        "replicaSpecifications": NotRequired[Sequence[ReplicaSpecificationTypeDef]],
    },
)
UpdateTableRequestRequestTypeDef = TypedDict(
    "UpdateTableRequestRequestTypeDef",
    {
        "keyspaceName": str,
        "tableName": str,
        "addColumns": NotRequired[Sequence[ColumnDefinitionTypeDef]],
        "capacitySpecification": NotRequired[CapacitySpecificationTypeDef],
        "encryptionSpecification": NotRequired[EncryptionSpecificationTypeDef],
        "pointInTimeRecovery": NotRequired[PointInTimeRecoveryTypeDef],
        "ttl": NotRequired[TimeToLiveTypeDef],
        "defaultTimeToLive": NotRequired[int],
        "clientSideTimestamps": NotRequired[ClientSideTimestampsTypeDef],
        "autoScalingSpecification": NotRequired[AutoScalingSpecificationTypeDef],
        "replicaSpecifications": NotRequired[Sequence[ReplicaSpecificationTypeDef]],
    },
)
GetTableAutoScalingSettingsResponseTypeDef = TypedDict(
    "GetTableAutoScalingSettingsResponseTypeDef",
    {
        "keyspaceName": str,
        "tableName": str,
        "resourceArn": str,
        "autoScalingSpecification": AutoScalingSpecificationTypeDef,
        "replicaSpecifications": List[ReplicaAutoScalingSpecificationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
