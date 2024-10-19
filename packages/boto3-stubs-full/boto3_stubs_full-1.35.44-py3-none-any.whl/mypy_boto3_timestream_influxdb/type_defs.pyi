"""
Type annotations for timestream-influxdb service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_influxdb/type_defs/)

Usage::

    ```python
    from mypy_boto3_timestream_influxdb.type_defs import ResponseMetadataTypeDef

    data: ResponseMetadataTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Mapping, Sequence

from .literals import (
    DbInstanceTypeType,
    DbStorageTypeType,
    DeploymentTypeType,
    DurationTypeType,
    LogLevelType,
    StatusType,
    TracingTypeType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "ResponseMetadataTypeDef",
    "DbInstanceSummaryTypeDef",
    "DbParameterGroupSummaryTypeDef",
    "DeleteDbInstanceInputRequestTypeDef",
    "DurationTypeDef",
    "GetDbInstanceInputRequestTypeDef",
    "GetDbParameterGroupInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListDbInstancesInputRequestTypeDef",
    "ListDbParameterGroupsInputRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "S3ConfigurationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListDbInstancesOutputTypeDef",
    "ListDbParameterGroupsOutputTypeDef",
    "InfluxDBv2ParametersTypeDef",
    "ListDbInstancesInputListDbInstancesPaginateTypeDef",
    "ListDbParameterGroupsInputListDbParameterGroupsPaginateTypeDef",
    "LogDeliveryConfigurationTypeDef",
    "ParametersTypeDef",
    "CreateDbInstanceInputRequestTypeDef",
    "CreateDbInstanceOutputTypeDef",
    "DeleteDbInstanceOutputTypeDef",
    "GetDbInstanceOutputTypeDef",
    "UpdateDbInstanceInputRequestTypeDef",
    "UpdateDbInstanceOutputTypeDef",
    "CreateDbParameterGroupInputRequestTypeDef",
    "CreateDbParameterGroupOutputTypeDef",
    "GetDbParameterGroupOutputTypeDef",
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
DbInstanceSummaryTypeDef = TypedDict(
    "DbInstanceSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "status": NotRequired[StatusType],
        "endpoint": NotRequired[str],
        "port": NotRequired[int],
        "dbInstanceType": NotRequired[DbInstanceTypeType],
        "dbStorageType": NotRequired[DbStorageTypeType],
        "allocatedStorage": NotRequired[int],
        "deploymentType": NotRequired[DeploymentTypeType],
    },
)
DbParameterGroupSummaryTypeDef = TypedDict(
    "DbParameterGroupSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "description": NotRequired[str],
    },
)
DeleteDbInstanceInputRequestTypeDef = TypedDict(
    "DeleteDbInstanceInputRequestTypeDef",
    {
        "identifier": str,
    },
)
DurationTypeDef = TypedDict(
    "DurationTypeDef",
    {
        "durationType": DurationTypeType,
        "value": int,
    },
)
GetDbInstanceInputRequestTypeDef = TypedDict(
    "GetDbInstanceInputRequestTypeDef",
    {
        "identifier": str,
    },
)
GetDbParameterGroupInputRequestTypeDef = TypedDict(
    "GetDbParameterGroupInputRequestTypeDef",
    {
        "identifier": str,
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
ListDbInstancesInputRequestTypeDef = TypedDict(
    "ListDbInstancesInputRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListDbParameterGroupsInputRequestTypeDef = TypedDict(
    "ListDbParameterGroupsInputRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
S3ConfigurationTypeDef = TypedDict(
    "S3ConfigurationTypeDef",
    {
        "bucketName": str,
        "enabled": bool,
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
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
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
ListDbInstancesOutputTypeDef = TypedDict(
    "ListDbInstancesOutputTypeDef",
    {
        "items": List[DbInstanceSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDbParameterGroupsOutputTypeDef = TypedDict(
    "ListDbParameterGroupsOutputTypeDef",
    {
        "items": List[DbParameterGroupSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InfluxDBv2ParametersTypeDef = TypedDict(
    "InfluxDBv2ParametersTypeDef",
    {
        "fluxLogEnabled": NotRequired[bool],
        "logLevel": NotRequired[LogLevelType],
        "noTasks": NotRequired[bool],
        "queryConcurrency": NotRequired[int],
        "queryQueueSize": NotRequired[int],
        "tracingType": NotRequired[TracingTypeType],
        "metricsDisabled": NotRequired[bool],
        "httpIdleTimeout": NotRequired[DurationTypeDef],
        "httpReadHeaderTimeout": NotRequired[DurationTypeDef],
        "httpReadTimeout": NotRequired[DurationTypeDef],
        "httpWriteTimeout": NotRequired[DurationTypeDef],
        "influxqlMaxSelectBuckets": NotRequired[int],
        "influxqlMaxSelectPoint": NotRequired[int],
        "influxqlMaxSelectSeries": NotRequired[int],
        "pprofDisabled": NotRequired[bool],
        "queryInitialMemoryBytes": NotRequired[int],
        "queryMaxMemoryBytes": NotRequired[int],
        "queryMemoryBytes": NotRequired[int],
        "sessionLength": NotRequired[int],
        "sessionRenewDisabled": NotRequired[bool],
        "storageCacheMaxMemorySize": NotRequired[int],
        "storageCacheSnapshotMemorySize": NotRequired[int],
        "storageCacheSnapshotWriteColdDuration": NotRequired[DurationTypeDef],
        "storageCompactFullWriteColdDuration": NotRequired[DurationTypeDef],
        "storageCompactThroughputBurst": NotRequired[int],
        "storageMaxConcurrentCompactions": NotRequired[int],
        "storageMaxIndexLogFileSize": NotRequired[int],
        "storageNoValidateFieldSize": NotRequired[bool],
        "storageRetentionCheckInterval": NotRequired[DurationTypeDef],
        "storageSeriesFileMaxConcurrentSnapshotCompactions": NotRequired[int],
        "storageSeriesIdSetCacheSize": NotRequired[int],
        "storageWalMaxConcurrentWrites": NotRequired[int],
        "storageWalMaxWriteDelay": NotRequired[DurationTypeDef],
        "uiDisabled": NotRequired[bool],
    },
)
ListDbInstancesInputListDbInstancesPaginateTypeDef = TypedDict(
    "ListDbInstancesInputListDbInstancesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDbParameterGroupsInputListDbParameterGroupsPaginateTypeDef = TypedDict(
    "ListDbParameterGroupsInputListDbParameterGroupsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
LogDeliveryConfigurationTypeDef = TypedDict(
    "LogDeliveryConfigurationTypeDef",
    {
        "s3Configuration": S3ConfigurationTypeDef,
    },
)
ParametersTypeDef = TypedDict(
    "ParametersTypeDef",
    {
        "InfluxDBv2": NotRequired[InfluxDBv2ParametersTypeDef],
    },
)
CreateDbInstanceInputRequestTypeDef = TypedDict(
    "CreateDbInstanceInputRequestTypeDef",
    {
        "name": str,
        "password": str,
        "dbInstanceType": DbInstanceTypeType,
        "vpcSubnetIds": Sequence[str],
        "vpcSecurityGroupIds": Sequence[str],
        "allocatedStorage": int,
        "username": NotRequired[str],
        "organization": NotRequired[str],
        "bucket": NotRequired[str],
        "publiclyAccessible": NotRequired[bool],
        "dbStorageType": NotRequired[DbStorageTypeType],
        "dbParameterGroupIdentifier": NotRequired[str],
        "deploymentType": NotRequired[DeploymentTypeType],
        "logDeliveryConfiguration": NotRequired[LogDeliveryConfigurationTypeDef],
        "tags": NotRequired[Mapping[str, str]],
        "port": NotRequired[int],
    },
)
CreateDbInstanceOutputTypeDef = TypedDict(
    "CreateDbInstanceOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "status": StatusType,
        "endpoint": str,
        "port": int,
        "dbInstanceType": DbInstanceTypeType,
        "dbStorageType": DbStorageTypeType,
        "allocatedStorage": int,
        "deploymentType": DeploymentTypeType,
        "vpcSubnetIds": List[str],
        "publiclyAccessible": bool,
        "vpcSecurityGroupIds": List[str],
        "dbParameterGroupIdentifier": str,
        "availabilityZone": str,
        "secondaryAvailabilityZone": str,
        "logDeliveryConfiguration": LogDeliveryConfigurationTypeDef,
        "influxAuthParametersSecretArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDbInstanceOutputTypeDef = TypedDict(
    "DeleteDbInstanceOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "status": StatusType,
        "endpoint": str,
        "port": int,
        "dbInstanceType": DbInstanceTypeType,
        "dbStorageType": DbStorageTypeType,
        "allocatedStorage": int,
        "deploymentType": DeploymentTypeType,
        "vpcSubnetIds": List[str],
        "publiclyAccessible": bool,
        "vpcSecurityGroupIds": List[str],
        "dbParameterGroupIdentifier": str,
        "availabilityZone": str,
        "secondaryAvailabilityZone": str,
        "logDeliveryConfiguration": LogDeliveryConfigurationTypeDef,
        "influxAuthParametersSecretArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDbInstanceOutputTypeDef = TypedDict(
    "GetDbInstanceOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "status": StatusType,
        "endpoint": str,
        "port": int,
        "dbInstanceType": DbInstanceTypeType,
        "dbStorageType": DbStorageTypeType,
        "allocatedStorage": int,
        "deploymentType": DeploymentTypeType,
        "vpcSubnetIds": List[str],
        "publiclyAccessible": bool,
        "vpcSecurityGroupIds": List[str],
        "dbParameterGroupIdentifier": str,
        "availabilityZone": str,
        "secondaryAvailabilityZone": str,
        "logDeliveryConfiguration": LogDeliveryConfigurationTypeDef,
        "influxAuthParametersSecretArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDbInstanceInputRequestTypeDef = TypedDict(
    "UpdateDbInstanceInputRequestTypeDef",
    {
        "identifier": str,
        "logDeliveryConfiguration": NotRequired[LogDeliveryConfigurationTypeDef],
        "dbParameterGroupIdentifier": NotRequired[str],
        "port": NotRequired[int],
        "dbInstanceType": NotRequired[DbInstanceTypeType],
        "deploymentType": NotRequired[DeploymentTypeType],
    },
)
UpdateDbInstanceOutputTypeDef = TypedDict(
    "UpdateDbInstanceOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "status": StatusType,
        "endpoint": str,
        "port": int,
        "dbInstanceType": DbInstanceTypeType,
        "dbStorageType": DbStorageTypeType,
        "allocatedStorage": int,
        "deploymentType": DeploymentTypeType,
        "vpcSubnetIds": List[str],
        "publiclyAccessible": bool,
        "vpcSecurityGroupIds": List[str],
        "dbParameterGroupIdentifier": str,
        "availabilityZone": str,
        "secondaryAvailabilityZone": str,
        "logDeliveryConfiguration": LogDeliveryConfigurationTypeDef,
        "influxAuthParametersSecretArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDbParameterGroupInputRequestTypeDef = TypedDict(
    "CreateDbParameterGroupInputRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "parameters": NotRequired[ParametersTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateDbParameterGroupOutputTypeDef = TypedDict(
    "CreateDbParameterGroupOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "description": str,
        "parameters": ParametersTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDbParameterGroupOutputTypeDef = TypedDict(
    "GetDbParameterGroupOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "description": str,
        "parameters": ParametersTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
