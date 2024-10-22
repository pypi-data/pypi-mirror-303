"""
Type annotations for finspace service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/type_defs/)

Usage::

    ```python
    from mypy_boto3_finspace.type_defs import AutoScalingConfigurationTypeDef

    data: AutoScalingConfigurationTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    ChangesetStatusType,
    ChangeTypeType,
    DnsStatusType,
    EnvironmentStatusType,
    ErrorDetailsType,
    FederationModeType,
    KxAzModeType,
    KxClusterCodeDeploymentStrategyType,
    KxClusterStatusType,
    KxClusterTypeType,
    KxDataviewStatusType,
    KxDeploymentStrategyType,
    KxNAS1TypeType,
    KxNodeStatusType,
    KxScalingGroupStatusType,
    KxVolumeStatusType,
    RuleActionType,
    TgwStatusType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AutoScalingConfigurationTypeDef",
    "CapacityConfigurationTypeDef",
    "ChangeRequestTypeDef",
    "CodeConfigurationTypeDef",
    "FederationParametersTypeDef",
    "SuperuserParametersTypeDef",
    "ResponseMetadataTypeDef",
    "ErrorInfoTypeDef",
    "KxCacheStorageConfigurationTypeDef",
    "KxCommandLineArgumentTypeDef",
    "KxSavedownStorageConfigurationTypeDef",
    "KxScalingGroupConfigurationTypeDef",
    "TickerplantLogConfigurationTypeDef",
    "VpcConfigurationTypeDef",
    "TickerplantLogConfigurationOutputTypeDef",
    "VolumeTypeDef",
    "VpcConfigurationOutputTypeDef",
    "CreateKxDatabaseRequestRequestTypeDef",
    "KxDataviewSegmentConfigurationOutputTypeDef",
    "CreateKxEnvironmentRequestRequestTypeDef",
    "CreateKxScalingGroupRequestRequestTypeDef",
    "CreateKxUserRequestRequestTypeDef",
    "KxNAS1ConfigurationTypeDef",
    "CustomDNSServerTypeDef",
    "DeleteEnvironmentRequestRequestTypeDef",
    "DeleteKxClusterNodeRequestRequestTypeDef",
    "DeleteKxClusterRequestRequestTypeDef",
    "DeleteKxDatabaseRequestRequestTypeDef",
    "DeleteKxDataviewRequestRequestTypeDef",
    "DeleteKxEnvironmentRequestRequestTypeDef",
    "DeleteKxScalingGroupRequestRequestTypeDef",
    "DeleteKxUserRequestRequestTypeDef",
    "DeleteKxVolumeRequestRequestTypeDef",
    "FederationParametersOutputTypeDef",
    "GetEnvironmentRequestRequestTypeDef",
    "GetKxChangesetRequestRequestTypeDef",
    "GetKxClusterRequestRequestTypeDef",
    "GetKxConnectionStringRequestRequestTypeDef",
    "GetKxDatabaseRequestRequestTypeDef",
    "GetKxDataviewRequestRequestTypeDef",
    "GetKxEnvironmentRequestRequestTypeDef",
    "GetKxScalingGroupRequestRequestTypeDef",
    "GetKxUserRequestRequestTypeDef",
    "GetKxVolumeRequestRequestTypeDef",
    "KxAttachedClusterTypeDef",
    "IcmpTypeCodeTypeDef",
    "KxChangesetListEntryTypeDef",
    "KxClusterCodeDeploymentConfigurationTypeDef",
    "KxDatabaseCacheConfigurationOutputTypeDef",
    "KxDatabaseCacheConfigurationTypeDef",
    "KxDatabaseListEntryTypeDef",
    "KxDataviewSegmentConfigurationTypeDef",
    "KxDeploymentConfigurationTypeDef",
    "KxNodeTypeDef",
    "KxScalingGroupTypeDef",
    "KxUserTypeDef",
    "KxVolumeTypeDef",
    "ListEnvironmentsRequestRequestTypeDef",
    "ListKxChangesetsRequestRequestTypeDef",
    "ListKxClusterNodesRequestRequestTypeDef",
    "ListKxClustersRequestRequestTypeDef",
    "ListKxDatabasesRequestRequestTypeDef",
    "ListKxDataviewsRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListKxEnvironmentsRequestRequestTypeDef",
    "ListKxScalingGroupsRequestRequestTypeDef",
    "ListKxUsersRequestRequestTypeDef",
    "ListKxVolumesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "PortRangeTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateKxDatabaseRequestRequestTypeDef",
    "UpdateKxEnvironmentRequestRequestTypeDef",
    "UpdateKxUserRequestRequestTypeDef",
    "CreateKxChangesetRequestRequestTypeDef",
    "UpdateEnvironmentRequestRequestTypeDef",
    "CreateEnvironmentRequestRequestTypeDef",
    "CreateEnvironmentResponseTypeDef",
    "CreateKxDatabaseResponseTypeDef",
    "CreateKxEnvironmentResponseTypeDef",
    "CreateKxScalingGroupResponseTypeDef",
    "CreateKxUserResponseTypeDef",
    "GetKxConnectionStringResponseTypeDef",
    "GetKxDatabaseResponseTypeDef",
    "GetKxScalingGroupResponseTypeDef",
    "GetKxUserResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "UpdateKxDatabaseResponseTypeDef",
    "UpdateKxUserResponseTypeDef",
    "CreateKxChangesetResponseTypeDef",
    "GetKxChangesetResponseTypeDef",
    "KxClusterTypeDef",
    "CreateKxDataviewResponseTypeDef",
    "KxDataviewActiveVersionTypeDef",
    "KxDataviewConfigurationOutputTypeDef",
    "CreateKxVolumeRequestRequestTypeDef",
    "CreateKxVolumeResponseTypeDef",
    "UpdateKxVolumeRequestRequestTypeDef",
    "EnvironmentTypeDef",
    "GetKxVolumeResponseTypeDef",
    "UpdateKxVolumeResponseTypeDef",
    "ListKxChangesetsResponseTypeDef",
    "UpdateKxClusterCodeConfigurationRequestRequestTypeDef",
    "KxDatabaseCacheConfigurationUnionTypeDef",
    "ListKxDatabasesResponseTypeDef",
    "KxDataviewSegmentConfigurationUnionTypeDef",
    "UpdateKxDataviewRequestRequestTypeDef",
    "ListKxClusterNodesResponseTypeDef",
    "ListKxScalingGroupsResponseTypeDef",
    "ListKxUsersResponseTypeDef",
    "ListKxVolumesResponseTypeDef",
    "ListKxEnvironmentsRequestListKxEnvironmentsPaginateTypeDef",
    "NetworkACLEntryTypeDef",
    "ListKxClustersResponseTypeDef",
    "GetKxDataviewResponseTypeDef",
    "KxDataviewListEntryTypeDef",
    "UpdateKxDataviewResponseTypeDef",
    "KxDatabaseConfigurationOutputTypeDef",
    "GetEnvironmentResponseTypeDef",
    "ListEnvironmentsResponseTypeDef",
    "UpdateEnvironmentResponseTypeDef",
    "CreateKxDataviewRequestRequestTypeDef",
    "KxDataviewConfigurationTypeDef",
    "TransitGatewayConfigurationOutputTypeDef",
    "TransitGatewayConfigurationTypeDef",
    "ListKxDataviewsResponseTypeDef",
    "CreateKxClusterResponseTypeDef",
    "GetKxClusterResponseTypeDef",
    "KxDataviewConfigurationUnionTypeDef",
    "GetKxEnvironmentResponseTypeDef",
    "KxEnvironmentTypeDef",
    "UpdateKxEnvironmentNetworkResponseTypeDef",
    "UpdateKxEnvironmentResponseTypeDef",
    "UpdateKxEnvironmentNetworkRequestRequestTypeDef",
    "KxDatabaseConfigurationTypeDef",
    "ListKxEnvironmentsResponseTypeDef",
    "KxDatabaseConfigurationUnionTypeDef",
    "UpdateKxClusterDatabasesRequestRequestTypeDef",
    "CreateKxClusterRequestRequestTypeDef",
)

AutoScalingConfigurationTypeDef = TypedDict(
    "AutoScalingConfigurationTypeDef",
    {
        "minNodeCount": NotRequired[int],
        "maxNodeCount": NotRequired[int],
        "autoScalingMetric": NotRequired[Literal["CPU_UTILIZATION_PERCENTAGE"]],
        "metricTarget": NotRequired[float],
        "scaleInCooldownSeconds": NotRequired[float],
        "scaleOutCooldownSeconds": NotRequired[float],
    },
)
CapacityConfigurationTypeDef = TypedDict(
    "CapacityConfigurationTypeDef",
    {
        "nodeType": NotRequired[str],
        "nodeCount": NotRequired[int],
    },
)
ChangeRequestTypeDef = TypedDict(
    "ChangeRequestTypeDef",
    {
        "changeType": ChangeTypeType,
        "dbPath": str,
        "s3Path": NotRequired[str],
    },
)
CodeConfigurationTypeDef = TypedDict(
    "CodeConfigurationTypeDef",
    {
        "s3Bucket": NotRequired[str],
        "s3Key": NotRequired[str],
        "s3ObjectVersion": NotRequired[str],
    },
)
FederationParametersTypeDef = TypedDict(
    "FederationParametersTypeDef",
    {
        "samlMetadataDocument": NotRequired[str],
        "samlMetadataURL": NotRequired[str],
        "applicationCallBackURL": NotRequired[str],
        "federationURN": NotRequired[str],
        "federationProviderName": NotRequired[str],
        "attributeMap": NotRequired[Mapping[str, str]],
    },
)
SuperuserParametersTypeDef = TypedDict(
    "SuperuserParametersTypeDef",
    {
        "emailAddress": str,
        "firstName": str,
        "lastName": str,
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
ErrorInfoTypeDef = TypedDict(
    "ErrorInfoTypeDef",
    {
        "errorMessage": NotRequired[str],
        "errorType": NotRequired[ErrorDetailsType],
    },
)
KxCacheStorageConfigurationTypeDef = TypedDict(
    "KxCacheStorageConfigurationTypeDef",
    {
        "type": str,
        "size": int,
    },
)
KxCommandLineArgumentTypeDef = TypedDict(
    "KxCommandLineArgumentTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[str],
    },
)
KxSavedownStorageConfigurationTypeDef = TypedDict(
    "KxSavedownStorageConfigurationTypeDef",
    {
        "type": NotRequired[Literal["SDS01"]],
        "size": NotRequired[int],
        "volumeName": NotRequired[str],
    },
)
KxScalingGroupConfigurationTypeDef = TypedDict(
    "KxScalingGroupConfigurationTypeDef",
    {
        "scalingGroupName": str,
        "memoryReservation": int,
        "nodeCount": int,
        "memoryLimit": NotRequired[int],
        "cpu": NotRequired[float],
    },
)
TickerplantLogConfigurationTypeDef = TypedDict(
    "TickerplantLogConfigurationTypeDef",
    {
        "tickerplantLogVolumes": NotRequired[Sequence[str]],
    },
)
VpcConfigurationTypeDef = TypedDict(
    "VpcConfigurationTypeDef",
    {
        "vpcId": NotRequired[str],
        "securityGroupIds": NotRequired[Sequence[str]],
        "subnetIds": NotRequired[Sequence[str]],
        "ipAddressType": NotRequired[Literal["IP_V4"]],
    },
)
TickerplantLogConfigurationOutputTypeDef = TypedDict(
    "TickerplantLogConfigurationOutputTypeDef",
    {
        "tickerplantLogVolumes": NotRequired[List[str]],
    },
)
VolumeTypeDef = TypedDict(
    "VolumeTypeDef",
    {
        "volumeName": NotRequired[str],
        "volumeType": NotRequired[Literal["NAS_1"]],
    },
)
VpcConfigurationOutputTypeDef = TypedDict(
    "VpcConfigurationOutputTypeDef",
    {
        "vpcId": NotRequired[str],
        "securityGroupIds": NotRequired[List[str]],
        "subnetIds": NotRequired[List[str]],
        "ipAddressType": NotRequired[Literal["IP_V4"]],
    },
)
CreateKxDatabaseRequestRequestTypeDef = TypedDict(
    "CreateKxDatabaseRequestRequestTypeDef",
    {
        "environmentId": str,
        "databaseName": str,
        "clientToken": str,
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
KxDataviewSegmentConfigurationOutputTypeDef = TypedDict(
    "KxDataviewSegmentConfigurationOutputTypeDef",
    {
        "dbPaths": List[str],
        "volumeName": str,
        "onDemand": NotRequired[bool],
    },
)
CreateKxEnvironmentRequestRequestTypeDef = TypedDict(
    "CreateKxEnvironmentRequestRequestTypeDef",
    {
        "name": str,
        "kmsKeyId": str,
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "clientToken": NotRequired[str],
    },
)
CreateKxScalingGroupRequestRequestTypeDef = TypedDict(
    "CreateKxScalingGroupRequestRequestTypeDef",
    {
        "clientToken": str,
        "environmentId": str,
        "scalingGroupName": str,
        "hostType": str,
        "availabilityZoneId": str,
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateKxUserRequestRequestTypeDef = TypedDict(
    "CreateKxUserRequestRequestTypeDef",
    {
        "environmentId": str,
        "userName": str,
        "iamRole": str,
        "tags": NotRequired[Mapping[str, str]],
        "clientToken": NotRequired[str],
    },
)
KxNAS1ConfigurationTypeDef = TypedDict(
    "KxNAS1ConfigurationTypeDef",
    {
        "type": NotRequired[KxNAS1TypeType],
        "size": NotRequired[int],
    },
)
CustomDNSServerTypeDef = TypedDict(
    "CustomDNSServerTypeDef",
    {
        "customDNSServerName": str,
        "customDNSServerIP": str,
    },
)
DeleteEnvironmentRequestRequestTypeDef = TypedDict(
    "DeleteEnvironmentRequestRequestTypeDef",
    {
        "environmentId": str,
    },
)
DeleteKxClusterNodeRequestRequestTypeDef = TypedDict(
    "DeleteKxClusterNodeRequestRequestTypeDef",
    {
        "environmentId": str,
        "clusterName": str,
        "nodeId": str,
    },
)
DeleteKxClusterRequestRequestTypeDef = TypedDict(
    "DeleteKxClusterRequestRequestTypeDef",
    {
        "environmentId": str,
        "clusterName": str,
        "clientToken": NotRequired[str],
    },
)
DeleteKxDatabaseRequestRequestTypeDef = TypedDict(
    "DeleteKxDatabaseRequestRequestTypeDef",
    {
        "environmentId": str,
        "databaseName": str,
        "clientToken": str,
    },
)
DeleteKxDataviewRequestRequestTypeDef = TypedDict(
    "DeleteKxDataviewRequestRequestTypeDef",
    {
        "environmentId": str,
        "databaseName": str,
        "dataviewName": str,
        "clientToken": str,
    },
)
DeleteKxEnvironmentRequestRequestTypeDef = TypedDict(
    "DeleteKxEnvironmentRequestRequestTypeDef",
    {
        "environmentId": str,
        "clientToken": NotRequired[str],
    },
)
DeleteKxScalingGroupRequestRequestTypeDef = TypedDict(
    "DeleteKxScalingGroupRequestRequestTypeDef",
    {
        "environmentId": str,
        "scalingGroupName": str,
        "clientToken": NotRequired[str],
    },
)
DeleteKxUserRequestRequestTypeDef = TypedDict(
    "DeleteKxUserRequestRequestTypeDef",
    {
        "userName": str,
        "environmentId": str,
        "clientToken": NotRequired[str],
    },
)
DeleteKxVolumeRequestRequestTypeDef = TypedDict(
    "DeleteKxVolumeRequestRequestTypeDef",
    {
        "environmentId": str,
        "volumeName": str,
        "clientToken": NotRequired[str],
    },
)
FederationParametersOutputTypeDef = TypedDict(
    "FederationParametersOutputTypeDef",
    {
        "samlMetadataDocument": NotRequired[str],
        "samlMetadataURL": NotRequired[str],
        "applicationCallBackURL": NotRequired[str],
        "federationURN": NotRequired[str],
        "federationProviderName": NotRequired[str],
        "attributeMap": NotRequired[Dict[str, str]],
    },
)
GetEnvironmentRequestRequestTypeDef = TypedDict(
    "GetEnvironmentRequestRequestTypeDef",
    {
        "environmentId": str,
    },
)
GetKxChangesetRequestRequestTypeDef = TypedDict(
    "GetKxChangesetRequestRequestTypeDef",
    {
        "environmentId": str,
        "databaseName": str,
        "changesetId": str,
    },
)
GetKxClusterRequestRequestTypeDef = TypedDict(
    "GetKxClusterRequestRequestTypeDef",
    {
        "environmentId": str,
        "clusterName": str,
    },
)
GetKxConnectionStringRequestRequestTypeDef = TypedDict(
    "GetKxConnectionStringRequestRequestTypeDef",
    {
        "userArn": str,
        "environmentId": str,
        "clusterName": str,
    },
)
GetKxDatabaseRequestRequestTypeDef = TypedDict(
    "GetKxDatabaseRequestRequestTypeDef",
    {
        "environmentId": str,
        "databaseName": str,
    },
)
GetKxDataviewRequestRequestTypeDef = TypedDict(
    "GetKxDataviewRequestRequestTypeDef",
    {
        "environmentId": str,
        "databaseName": str,
        "dataviewName": str,
    },
)
GetKxEnvironmentRequestRequestTypeDef = TypedDict(
    "GetKxEnvironmentRequestRequestTypeDef",
    {
        "environmentId": str,
    },
)
GetKxScalingGroupRequestRequestTypeDef = TypedDict(
    "GetKxScalingGroupRequestRequestTypeDef",
    {
        "environmentId": str,
        "scalingGroupName": str,
    },
)
GetKxUserRequestRequestTypeDef = TypedDict(
    "GetKxUserRequestRequestTypeDef",
    {
        "userName": str,
        "environmentId": str,
    },
)
GetKxVolumeRequestRequestTypeDef = TypedDict(
    "GetKxVolumeRequestRequestTypeDef",
    {
        "environmentId": str,
        "volumeName": str,
    },
)
KxAttachedClusterTypeDef = TypedDict(
    "KxAttachedClusterTypeDef",
    {
        "clusterName": NotRequired[str],
        "clusterType": NotRequired[KxClusterTypeType],
        "clusterStatus": NotRequired[KxClusterStatusType],
    },
)
IcmpTypeCodeTypeDef = TypedDict(
    "IcmpTypeCodeTypeDef",
    {
        "type": int,
        "code": int,
    },
)
KxChangesetListEntryTypeDef = TypedDict(
    "KxChangesetListEntryTypeDef",
    {
        "changesetId": NotRequired[str],
        "createdTimestamp": NotRequired[datetime],
        "activeFromTimestamp": NotRequired[datetime],
        "lastModifiedTimestamp": NotRequired[datetime],
        "status": NotRequired[ChangesetStatusType],
    },
)
KxClusterCodeDeploymentConfigurationTypeDef = TypedDict(
    "KxClusterCodeDeploymentConfigurationTypeDef",
    {
        "deploymentStrategy": KxClusterCodeDeploymentStrategyType,
    },
)
KxDatabaseCacheConfigurationOutputTypeDef = TypedDict(
    "KxDatabaseCacheConfigurationOutputTypeDef",
    {
        "cacheType": str,
        "dbPaths": List[str],
        "dataviewName": NotRequired[str],
    },
)
KxDatabaseCacheConfigurationTypeDef = TypedDict(
    "KxDatabaseCacheConfigurationTypeDef",
    {
        "cacheType": str,
        "dbPaths": Sequence[str],
        "dataviewName": NotRequired[str],
    },
)
KxDatabaseListEntryTypeDef = TypedDict(
    "KxDatabaseListEntryTypeDef",
    {
        "databaseName": NotRequired[str],
        "createdTimestamp": NotRequired[datetime],
        "lastModifiedTimestamp": NotRequired[datetime],
    },
)
KxDataviewSegmentConfigurationTypeDef = TypedDict(
    "KxDataviewSegmentConfigurationTypeDef",
    {
        "dbPaths": Sequence[str],
        "volumeName": str,
        "onDemand": NotRequired[bool],
    },
)
KxDeploymentConfigurationTypeDef = TypedDict(
    "KxDeploymentConfigurationTypeDef",
    {
        "deploymentStrategy": KxDeploymentStrategyType,
    },
)
KxNodeTypeDef = TypedDict(
    "KxNodeTypeDef",
    {
        "nodeId": NotRequired[str],
        "availabilityZoneId": NotRequired[str],
        "launchTime": NotRequired[datetime],
        "status": NotRequired[KxNodeStatusType],
    },
)
KxScalingGroupTypeDef = TypedDict(
    "KxScalingGroupTypeDef",
    {
        "scalingGroupName": NotRequired[str],
        "hostType": NotRequired[str],
        "clusters": NotRequired[List[str]],
        "availabilityZoneId": NotRequired[str],
        "status": NotRequired[KxScalingGroupStatusType],
        "statusReason": NotRequired[str],
        "lastModifiedTimestamp": NotRequired[datetime],
        "createdTimestamp": NotRequired[datetime],
    },
)
KxUserTypeDef = TypedDict(
    "KxUserTypeDef",
    {
        "userArn": NotRequired[str],
        "userName": NotRequired[str],
        "iamRole": NotRequired[str],
        "createTimestamp": NotRequired[datetime],
        "updateTimestamp": NotRequired[datetime],
    },
)
KxVolumeTypeDef = TypedDict(
    "KxVolumeTypeDef",
    {
        "volumeName": NotRequired[str],
        "volumeType": NotRequired[Literal["NAS_1"]],
        "status": NotRequired[KxVolumeStatusType],
        "description": NotRequired[str],
        "statusReason": NotRequired[str],
        "azMode": NotRequired[KxAzModeType],
        "availabilityZoneIds": NotRequired[List[str]],
        "createdTimestamp": NotRequired[datetime],
        "lastModifiedTimestamp": NotRequired[datetime],
    },
)
ListEnvironmentsRequestRequestTypeDef = TypedDict(
    "ListEnvironmentsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListKxChangesetsRequestRequestTypeDef = TypedDict(
    "ListKxChangesetsRequestRequestTypeDef",
    {
        "environmentId": str,
        "databaseName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListKxClusterNodesRequestRequestTypeDef = TypedDict(
    "ListKxClusterNodesRequestRequestTypeDef",
    {
        "environmentId": str,
        "clusterName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListKxClustersRequestRequestTypeDef = TypedDict(
    "ListKxClustersRequestRequestTypeDef",
    {
        "environmentId": str,
        "clusterType": NotRequired[KxClusterTypeType],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListKxDatabasesRequestRequestTypeDef = TypedDict(
    "ListKxDatabasesRequestRequestTypeDef",
    {
        "environmentId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListKxDataviewsRequestRequestTypeDef = TypedDict(
    "ListKxDataviewsRequestRequestTypeDef",
    {
        "environmentId": str,
        "databaseName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
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
ListKxEnvironmentsRequestRequestTypeDef = TypedDict(
    "ListKxEnvironmentsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListKxScalingGroupsRequestRequestTypeDef = TypedDict(
    "ListKxScalingGroupsRequestRequestTypeDef",
    {
        "environmentId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListKxUsersRequestRequestTypeDef = TypedDict(
    "ListKxUsersRequestRequestTypeDef",
    {
        "environmentId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListKxVolumesRequestRequestTypeDef = TypedDict(
    "ListKxVolumesRequestRequestTypeDef",
    {
        "environmentId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "volumeType": NotRequired[Literal["NAS_1"]],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
PortRangeTypeDef = TypedDict(
    "PortRangeTypeDef",
    {
        "from": int,
        "to": int,
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
UpdateKxDatabaseRequestRequestTypeDef = TypedDict(
    "UpdateKxDatabaseRequestRequestTypeDef",
    {
        "environmentId": str,
        "databaseName": str,
        "clientToken": str,
        "description": NotRequired[str],
    },
)
UpdateKxEnvironmentRequestRequestTypeDef = TypedDict(
    "UpdateKxEnvironmentRequestRequestTypeDef",
    {
        "environmentId": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "clientToken": NotRequired[str],
    },
)
UpdateKxUserRequestRequestTypeDef = TypedDict(
    "UpdateKxUserRequestRequestTypeDef",
    {
        "environmentId": str,
        "userName": str,
        "iamRole": str,
        "clientToken": NotRequired[str],
    },
)
CreateKxChangesetRequestRequestTypeDef = TypedDict(
    "CreateKxChangesetRequestRequestTypeDef",
    {
        "environmentId": str,
        "databaseName": str,
        "changeRequests": Sequence[ChangeRequestTypeDef],
        "clientToken": str,
    },
)
UpdateEnvironmentRequestRequestTypeDef = TypedDict(
    "UpdateEnvironmentRequestRequestTypeDef",
    {
        "environmentId": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "federationMode": NotRequired[FederationModeType],
        "federationParameters": NotRequired[FederationParametersTypeDef],
    },
)
CreateEnvironmentRequestRequestTypeDef = TypedDict(
    "CreateEnvironmentRequestRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "kmsKeyId": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "federationMode": NotRequired[FederationModeType],
        "federationParameters": NotRequired[FederationParametersTypeDef],
        "superuserParameters": NotRequired[SuperuserParametersTypeDef],
        "dataBundles": NotRequired[Sequence[str]],
    },
)
CreateEnvironmentResponseTypeDef = TypedDict(
    "CreateEnvironmentResponseTypeDef",
    {
        "environmentId": str,
        "environmentArn": str,
        "environmentUrl": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateKxDatabaseResponseTypeDef = TypedDict(
    "CreateKxDatabaseResponseTypeDef",
    {
        "databaseName": str,
        "databaseArn": str,
        "environmentId": str,
        "description": str,
        "createdTimestamp": datetime,
        "lastModifiedTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateKxEnvironmentResponseTypeDef = TypedDict(
    "CreateKxEnvironmentResponseTypeDef",
    {
        "name": str,
        "status": EnvironmentStatusType,
        "environmentId": str,
        "description": str,
        "environmentArn": str,
        "kmsKeyId": str,
        "creationTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateKxScalingGroupResponseTypeDef = TypedDict(
    "CreateKxScalingGroupResponseTypeDef",
    {
        "environmentId": str,
        "scalingGroupName": str,
        "hostType": str,
        "availabilityZoneId": str,
        "status": KxScalingGroupStatusType,
        "lastModifiedTimestamp": datetime,
        "createdTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateKxUserResponseTypeDef = TypedDict(
    "CreateKxUserResponseTypeDef",
    {
        "userName": str,
        "userArn": str,
        "environmentId": str,
        "iamRole": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetKxConnectionStringResponseTypeDef = TypedDict(
    "GetKxConnectionStringResponseTypeDef",
    {
        "signedConnectionString": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetKxDatabaseResponseTypeDef = TypedDict(
    "GetKxDatabaseResponseTypeDef",
    {
        "databaseName": str,
        "databaseArn": str,
        "environmentId": str,
        "description": str,
        "createdTimestamp": datetime,
        "lastModifiedTimestamp": datetime,
        "lastCompletedChangesetId": str,
        "numBytes": int,
        "numChangesets": int,
        "numFiles": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetKxScalingGroupResponseTypeDef = TypedDict(
    "GetKxScalingGroupResponseTypeDef",
    {
        "scalingGroupName": str,
        "scalingGroupArn": str,
        "hostType": str,
        "clusters": List[str],
        "availabilityZoneId": str,
        "status": KxScalingGroupStatusType,
        "statusReason": str,
        "lastModifiedTimestamp": datetime,
        "createdTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetKxUserResponseTypeDef = TypedDict(
    "GetKxUserResponseTypeDef",
    {
        "userName": str,
        "userArn": str,
        "environmentId": str,
        "iamRole": str,
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
UpdateKxDatabaseResponseTypeDef = TypedDict(
    "UpdateKxDatabaseResponseTypeDef",
    {
        "databaseName": str,
        "environmentId": str,
        "description": str,
        "lastModifiedTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateKxUserResponseTypeDef = TypedDict(
    "UpdateKxUserResponseTypeDef",
    {
        "userName": str,
        "userArn": str,
        "environmentId": str,
        "iamRole": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateKxChangesetResponseTypeDef = TypedDict(
    "CreateKxChangesetResponseTypeDef",
    {
        "changesetId": str,
        "databaseName": str,
        "environmentId": str,
        "changeRequests": List[ChangeRequestTypeDef],
        "createdTimestamp": datetime,
        "lastModifiedTimestamp": datetime,
        "status": ChangesetStatusType,
        "errorInfo": ErrorInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetKxChangesetResponseTypeDef = TypedDict(
    "GetKxChangesetResponseTypeDef",
    {
        "changesetId": str,
        "databaseName": str,
        "environmentId": str,
        "changeRequests": List[ChangeRequestTypeDef],
        "createdTimestamp": datetime,
        "activeFromTimestamp": datetime,
        "lastModifiedTimestamp": datetime,
        "status": ChangesetStatusType,
        "errorInfo": ErrorInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
KxClusterTypeDef = TypedDict(
    "KxClusterTypeDef",
    {
        "status": NotRequired[KxClusterStatusType],
        "statusReason": NotRequired[str],
        "clusterName": NotRequired[str],
        "clusterType": NotRequired[KxClusterTypeType],
        "clusterDescription": NotRequired[str],
        "releaseLabel": NotRequired[str],
        "volumes": NotRequired[List[VolumeTypeDef]],
        "initializationScript": NotRequired[str],
        "executionRole": NotRequired[str],
        "azMode": NotRequired[KxAzModeType],
        "availabilityZoneId": NotRequired[str],
        "lastModifiedTimestamp": NotRequired[datetime],
        "createdTimestamp": NotRequired[datetime],
    },
)
CreateKxDataviewResponseTypeDef = TypedDict(
    "CreateKxDataviewResponseTypeDef",
    {
        "dataviewName": str,
        "databaseName": str,
        "environmentId": str,
        "azMode": KxAzModeType,
        "availabilityZoneId": str,
        "changesetId": str,
        "segmentConfigurations": List[KxDataviewSegmentConfigurationOutputTypeDef],
        "description": str,
        "autoUpdate": bool,
        "readWrite": bool,
        "createdTimestamp": datetime,
        "lastModifiedTimestamp": datetime,
        "status": KxDataviewStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
KxDataviewActiveVersionTypeDef = TypedDict(
    "KxDataviewActiveVersionTypeDef",
    {
        "changesetId": NotRequired[str],
        "segmentConfigurations": NotRequired[List[KxDataviewSegmentConfigurationOutputTypeDef]],
        "attachedClusters": NotRequired[List[str]],
        "createdTimestamp": NotRequired[datetime],
        "versionId": NotRequired[str],
    },
)
KxDataviewConfigurationOutputTypeDef = TypedDict(
    "KxDataviewConfigurationOutputTypeDef",
    {
        "dataviewName": NotRequired[str],
        "dataviewVersionId": NotRequired[str],
        "changesetId": NotRequired[str],
        "segmentConfigurations": NotRequired[List[KxDataviewSegmentConfigurationOutputTypeDef]],
    },
)
CreateKxVolumeRequestRequestTypeDef = TypedDict(
    "CreateKxVolumeRequestRequestTypeDef",
    {
        "environmentId": str,
        "volumeType": Literal["NAS_1"],
        "volumeName": str,
        "azMode": KxAzModeType,
        "availabilityZoneIds": Sequence[str],
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "nas1Configuration": NotRequired[KxNAS1ConfigurationTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateKxVolumeResponseTypeDef = TypedDict(
    "CreateKxVolumeResponseTypeDef",
    {
        "environmentId": str,
        "volumeName": str,
        "volumeType": Literal["NAS_1"],
        "volumeArn": str,
        "nas1Configuration": KxNAS1ConfigurationTypeDef,
        "status": KxVolumeStatusType,
        "statusReason": str,
        "azMode": KxAzModeType,
        "description": str,
        "availabilityZoneIds": List[str],
        "createdTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateKxVolumeRequestRequestTypeDef = TypedDict(
    "UpdateKxVolumeRequestRequestTypeDef",
    {
        "environmentId": str,
        "volumeName": str,
        "description": NotRequired[str],
        "clientToken": NotRequired[str],
        "nas1Configuration": NotRequired[KxNAS1ConfigurationTypeDef],
    },
)
EnvironmentTypeDef = TypedDict(
    "EnvironmentTypeDef",
    {
        "name": NotRequired[str],
        "environmentId": NotRequired[str],
        "awsAccountId": NotRequired[str],
        "status": NotRequired[EnvironmentStatusType],
        "environmentUrl": NotRequired[str],
        "description": NotRequired[str],
        "environmentArn": NotRequired[str],
        "sageMakerStudioDomainUrl": NotRequired[str],
        "kmsKeyId": NotRequired[str],
        "dedicatedServiceAccountId": NotRequired[str],
        "federationMode": NotRequired[FederationModeType],
        "federationParameters": NotRequired[FederationParametersOutputTypeDef],
    },
)
GetKxVolumeResponseTypeDef = TypedDict(
    "GetKxVolumeResponseTypeDef",
    {
        "environmentId": str,
        "volumeName": str,
        "volumeType": Literal["NAS_1"],
        "volumeArn": str,
        "nas1Configuration": KxNAS1ConfigurationTypeDef,
        "status": KxVolumeStatusType,
        "statusReason": str,
        "createdTimestamp": datetime,
        "description": str,
        "azMode": KxAzModeType,
        "availabilityZoneIds": List[str],
        "lastModifiedTimestamp": datetime,
        "attachedClusters": List[KxAttachedClusterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateKxVolumeResponseTypeDef = TypedDict(
    "UpdateKxVolumeResponseTypeDef",
    {
        "environmentId": str,
        "volumeName": str,
        "volumeType": Literal["NAS_1"],
        "volumeArn": str,
        "nas1Configuration": KxNAS1ConfigurationTypeDef,
        "status": KxVolumeStatusType,
        "description": str,
        "statusReason": str,
        "createdTimestamp": datetime,
        "azMode": KxAzModeType,
        "availabilityZoneIds": List[str],
        "lastModifiedTimestamp": datetime,
        "attachedClusters": List[KxAttachedClusterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListKxChangesetsResponseTypeDef = TypedDict(
    "ListKxChangesetsResponseTypeDef",
    {
        "kxChangesets": List[KxChangesetListEntryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateKxClusterCodeConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateKxClusterCodeConfigurationRequestRequestTypeDef",
    {
        "environmentId": str,
        "clusterName": str,
        "code": CodeConfigurationTypeDef,
        "clientToken": NotRequired[str],
        "initializationScript": NotRequired[str],
        "commandLineArguments": NotRequired[Sequence[KxCommandLineArgumentTypeDef]],
        "deploymentConfiguration": NotRequired[KxClusterCodeDeploymentConfigurationTypeDef],
    },
)
KxDatabaseCacheConfigurationUnionTypeDef = Union[
    KxDatabaseCacheConfigurationTypeDef, KxDatabaseCacheConfigurationOutputTypeDef
]
ListKxDatabasesResponseTypeDef = TypedDict(
    "ListKxDatabasesResponseTypeDef",
    {
        "kxDatabases": List[KxDatabaseListEntryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
KxDataviewSegmentConfigurationUnionTypeDef = Union[
    KxDataviewSegmentConfigurationTypeDef, KxDataviewSegmentConfigurationOutputTypeDef
]
UpdateKxDataviewRequestRequestTypeDef = TypedDict(
    "UpdateKxDataviewRequestRequestTypeDef",
    {
        "environmentId": str,
        "databaseName": str,
        "dataviewName": str,
        "clientToken": str,
        "description": NotRequired[str],
        "changesetId": NotRequired[str],
        "segmentConfigurations": NotRequired[Sequence[KxDataviewSegmentConfigurationTypeDef]],
    },
)
ListKxClusterNodesResponseTypeDef = TypedDict(
    "ListKxClusterNodesResponseTypeDef",
    {
        "nodes": List[KxNodeTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListKxScalingGroupsResponseTypeDef = TypedDict(
    "ListKxScalingGroupsResponseTypeDef",
    {
        "scalingGroups": List[KxScalingGroupTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListKxUsersResponseTypeDef = TypedDict(
    "ListKxUsersResponseTypeDef",
    {
        "users": List[KxUserTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListKxVolumesResponseTypeDef = TypedDict(
    "ListKxVolumesResponseTypeDef",
    {
        "kxVolumeSummaries": List[KxVolumeTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListKxEnvironmentsRequestListKxEnvironmentsPaginateTypeDef = TypedDict(
    "ListKxEnvironmentsRequestListKxEnvironmentsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
NetworkACLEntryTypeDef = TypedDict(
    "NetworkACLEntryTypeDef",
    {
        "ruleNumber": int,
        "protocol": str,
        "ruleAction": RuleActionType,
        "cidrBlock": str,
        "portRange": NotRequired[PortRangeTypeDef],
        "icmpTypeCode": NotRequired[IcmpTypeCodeTypeDef],
    },
)
ListKxClustersResponseTypeDef = TypedDict(
    "ListKxClustersResponseTypeDef",
    {
        "kxClusterSummaries": List[KxClusterTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetKxDataviewResponseTypeDef = TypedDict(
    "GetKxDataviewResponseTypeDef",
    {
        "databaseName": str,
        "dataviewName": str,
        "azMode": KxAzModeType,
        "availabilityZoneId": str,
        "changesetId": str,
        "segmentConfigurations": List[KxDataviewSegmentConfigurationOutputTypeDef],
        "activeVersions": List[KxDataviewActiveVersionTypeDef],
        "description": str,
        "autoUpdate": bool,
        "readWrite": bool,
        "environmentId": str,
        "createdTimestamp": datetime,
        "lastModifiedTimestamp": datetime,
        "status": KxDataviewStatusType,
        "statusReason": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
KxDataviewListEntryTypeDef = TypedDict(
    "KxDataviewListEntryTypeDef",
    {
        "environmentId": NotRequired[str],
        "databaseName": NotRequired[str],
        "dataviewName": NotRequired[str],
        "azMode": NotRequired[KxAzModeType],
        "availabilityZoneId": NotRequired[str],
        "changesetId": NotRequired[str],
        "segmentConfigurations": NotRequired[List[KxDataviewSegmentConfigurationOutputTypeDef]],
        "activeVersions": NotRequired[List[KxDataviewActiveVersionTypeDef]],
        "status": NotRequired[KxDataviewStatusType],
        "description": NotRequired[str],
        "autoUpdate": NotRequired[bool],
        "readWrite": NotRequired[bool],
        "createdTimestamp": NotRequired[datetime],
        "lastModifiedTimestamp": NotRequired[datetime],
        "statusReason": NotRequired[str],
    },
)
UpdateKxDataviewResponseTypeDef = TypedDict(
    "UpdateKxDataviewResponseTypeDef",
    {
        "environmentId": str,
        "databaseName": str,
        "dataviewName": str,
        "azMode": KxAzModeType,
        "availabilityZoneId": str,
        "changesetId": str,
        "segmentConfigurations": List[KxDataviewSegmentConfigurationOutputTypeDef],
        "activeVersions": List[KxDataviewActiveVersionTypeDef],
        "status": KxDataviewStatusType,
        "autoUpdate": bool,
        "readWrite": bool,
        "description": str,
        "createdTimestamp": datetime,
        "lastModifiedTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
KxDatabaseConfigurationOutputTypeDef = TypedDict(
    "KxDatabaseConfigurationOutputTypeDef",
    {
        "databaseName": str,
        "cacheConfigurations": NotRequired[List[KxDatabaseCacheConfigurationOutputTypeDef]],
        "changesetId": NotRequired[str],
        "dataviewName": NotRequired[str],
        "dataviewConfiguration": NotRequired[KxDataviewConfigurationOutputTypeDef],
    },
)
GetEnvironmentResponseTypeDef = TypedDict(
    "GetEnvironmentResponseTypeDef",
    {
        "environment": EnvironmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEnvironmentsResponseTypeDef = TypedDict(
    "ListEnvironmentsResponseTypeDef",
    {
        "environments": List[EnvironmentTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEnvironmentResponseTypeDef = TypedDict(
    "UpdateEnvironmentResponseTypeDef",
    {
        "environment": EnvironmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateKxDataviewRequestRequestTypeDef = TypedDict(
    "CreateKxDataviewRequestRequestTypeDef",
    {
        "environmentId": str,
        "databaseName": str,
        "dataviewName": str,
        "azMode": KxAzModeType,
        "clientToken": str,
        "availabilityZoneId": NotRequired[str],
        "changesetId": NotRequired[str],
        "segmentConfigurations": NotRequired[Sequence[KxDataviewSegmentConfigurationUnionTypeDef]],
        "autoUpdate": NotRequired[bool],
        "readWrite": NotRequired[bool],
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
KxDataviewConfigurationTypeDef = TypedDict(
    "KxDataviewConfigurationTypeDef",
    {
        "dataviewName": NotRequired[str],
        "dataviewVersionId": NotRequired[str],
        "changesetId": NotRequired[str],
        "segmentConfigurations": NotRequired[Sequence[KxDataviewSegmentConfigurationUnionTypeDef]],
    },
)
TransitGatewayConfigurationOutputTypeDef = TypedDict(
    "TransitGatewayConfigurationOutputTypeDef",
    {
        "transitGatewayID": str,
        "routableCIDRSpace": str,
        "attachmentNetworkAclConfiguration": NotRequired[List[NetworkACLEntryTypeDef]],
    },
)
TransitGatewayConfigurationTypeDef = TypedDict(
    "TransitGatewayConfigurationTypeDef",
    {
        "transitGatewayID": str,
        "routableCIDRSpace": str,
        "attachmentNetworkAclConfiguration": NotRequired[Sequence[NetworkACLEntryTypeDef]],
    },
)
ListKxDataviewsResponseTypeDef = TypedDict(
    "ListKxDataviewsResponseTypeDef",
    {
        "kxDataviews": List[KxDataviewListEntryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateKxClusterResponseTypeDef = TypedDict(
    "CreateKxClusterResponseTypeDef",
    {
        "environmentId": str,
        "status": KxClusterStatusType,
        "statusReason": str,
        "clusterName": str,
        "clusterType": KxClusterTypeType,
        "tickerplantLogConfiguration": TickerplantLogConfigurationOutputTypeDef,
        "volumes": List[VolumeTypeDef],
        "databases": List[KxDatabaseConfigurationOutputTypeDef],
        "cacheStorageConfigurations": List[KxCacheStorageConfigurationTypeDef],
        "autoScalingConfiguration": AutoScalingConfigurationTypeDef,
        "clusterDescription": str,
        "capacityConfiguration": CapacityConfigurationTypeDef,
        "releaseLabel": str,
        "vpcConfiguration": VpcConfigurationOutputTypeDef,
        "initializationScript": str,
        "commandLineArguments": List[KxCommandLineArgumentTypeDef],
        "code": CodeConfigurationTypeDef,
        "executionRole": str,
        "lastModifiedTimestamp": datetime,
        "savedownStorageConfiguration": KxSavedownStorageConfigurationTypeDef,
        "azMode": KxAzModeType,
        "availabilityZoneId": str,
        "createdTimestamp": datetime,
        "scalingGroupConfiguration": KxScalingGroupConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetKxClusterResponseTypeDef = TypedDict(
    "GetKxClusterResponseTypeDef",
    {
        "status": KxClusterStatusType,
        "statusReason": str,
        "clusterName": str,
        "clusterType": KxClusterTypeType,
        "tickerplantLogConfiguration": TickerplantLogConfigurationOutputTypeDef,
        "volumes": List[VolumeTypeDef],
        "databases": List[KxDatabaseConfigurationOutputTypeDef],
        "cacheStorageConfigurations": List[KxCacheStorageConfigurationTypeDef],
        "autoScalingConfiguration": AutoScalingConfigurationTypeDef,
        "clusterDescription": str,
        "capacityConfiguration": CapacityConfigurationTypeDef,
        "releaseLabel": str,
        "vpcConfiguration": VpcConfigurationOutputTypeDef,
        "initializationScript": str,
        "commandLineArguments": List[KxCommandLineArgumentTypeDef],
        "code": CodeConfigurationTypeDef,
        "executionRole": str,
        "lastModifiedTimestamp": datetime,
        "savedownStorageConfiguration": KxSavedownStorageConfigurationTypeDef,
        "azMode": KxAzModeType,
        "availabilityZoneId": str,
        "createdTimestamp": datetime,
        "scalingGroupConfiguration": KxScalingGroupConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
KxDataviewConfigurationUnionTypeDef = Union[
    KxDataviewConfigurationTypeDef, KxDataviewConfigurationOutputTypeDef
]
GetKxEnvironmentResponseTypeDef = TypedDict(
    "GetKxEnvironmentResponseTypeDef",
    {
        "name": str,
        "environmentId": str,
        "awsAccountId": str,
        "status": EnvironmentStatusType,
        "tgwStatus": TgwStatusType,
        "dnsStatus": DnsStatusType,
        "errorMessage": str,
        "description": str,
        "environmentArn": str,
        "kmsKeyId": str,
        "dedicatedServiceAccountId": str,
        "transitGatewayConfiguration": TransitGatewayConfigurationOutputTypeDef,
        "customDNSConfiguration": List[CustomDNSServerTypeDef],
        "creationTimestamp": datetime,
        "updateTimestamp": datetime,
        "availabilityZoneIds": List[str],
        "certificateAuthorityArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
KxEnvironmentTypeDef = TypedDict(
    "KxEnvironmentTypeDef",
    {
        "name": NotRequired[str],
        "environmentId": NotRequired[str],
        "awsAccountId": NotRequired[str],
        "status": NotRequired[EnvironmentStatusType],
        "tgwStatus": NotRequired[TgwStatusType],
        "dnsStatus": NotRequired[DnsStatusType],
        "errorMessage": NotRequired[str],
        "description": NotRequired[str],
        "environmentArn": NotRequired[str],
        "kmsKeyId": NotRequired[str],
        "dedicatedServiceAccountId": NotRequired[str],
        "transitGatewayConfiguration": NotRequired[TransitGatewayConfigurationOutputTypeDef],
        "customDNSConfiguration": NotRequired[List[CustomDNSServerTypeDef]],
        "creationTimestamp": NotRequired[datetime],
        "updateTimestamp": NotRequired[datetime],
        "availabilityZoneIds": NotRequired[List[str]],
        "certificateAuthorityArn": NotRequired[str],
    },
)
UpdateKxEnvironmentNetworkResponseTypeDef = TypedDict(
    "UpdateKxEnvironmentNetworkResponseTypeDef",
    {
        "name": str,
        "environmentId": str,
        "awsAccountId": str,
        "status": EnvironmentStatusType,
        "tgwStatus": TgwStatusType,
        "dnsStatus": DnsStatusType,
        "errorMessage": str,
        "description": str,
        "environmentArn": str,
        "kmsKeyId": str,
        "dedicatedServiceAccountId": str,
        "transitGatewayConfiguration": TransitGatewayConfigurationOutputTypeDef,
        "customDNSConfiguration": List[CustomDNSServerTypeDef],
        "creationTimestamp": datetime,
        "updateTimestamp": datetime,
        "availabilityZoneIds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateKxEnvironmentResponseTypeDef = TypedDict(
    "UpdateKxEnvironmentResponseTypeDef",
    {
        "name": str,
        "environmentId": str,
        "awsAccountId": str,
        "status": EnvironmentStatusType,
        "tgwStatus": TgwStatusType,
        "dnsStatus": DnsStatusType,
        "errorMessage": str,
        "description": str,
        "environmentArn": str,
        "kmsKeyId": str,
        "dedicatedServiceAccountId": str,
        "transitGatewayConfiguration": TransitGatewayConfigurationOutputTypeDef,
        "customDNSConfiguration": List[CustomDNSServerTypeDef],
        "creationTimestamp": datetime,
        "updateTimestamp": datetime,
        "availabilityZoneIds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateKxEnvironmentNetworkRequestRequestTypeDef = TypedDict(
    "UpdateKxEnvironmentNetworkRequestRequestTypeDef",
    {
        "environmentId": str,
        "transitGatewayConfiguration": NotRequired[TransitGatewayConfigurationTypeDef],
        "customDNSConfiguration": NotRequired[Sequence[CustomDNSServerTypeDef]],
        "clientToken": NotRequired[str],
    },
)
KxDatabaseConfigurationTypeDef = TypedDict(
    "KxDatabaseConfigurationTypeDef",
    {
        "databaseName": str,
        "cacheConfigurations": NotRequired[Sequence[KxDatabaseCacheConfigurationUnionTypeDef]],
        "changesetId": NotRequired[str],
        "dataviewName": NotRequired[str],
        "dataviewConfiguration": NotRequired[KxDataviewConfigurationUnionTypeDef],
    },
)
ListKxEnvironmentsResponseTypeDef = TypedDict(
    "ListKxEnvironmentsResponseTypeDef",
    {
        "environments": List[KxEnvironmentTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
KxDatabaseConfigurationUnionTypeDef = Union[
    KxDatabaseConfigurationTypeDef, KxDatabaseConfigurationOutputTypeDef
]
UpdateKxClusterDatabasesRequestRequestTypeDef = TypedDict(
    "UpdateKxClusterDatabasesRequestRequestTypeDef",
    {
        "environmentId": str,
        "clusterName": str,
        "databases": Sequence[KxDatabaseConfigurationTypeDef],
        "clientToken": NotRequired[str],
        "deploymentConfiguration": NotRequired[KxDeploymentConfigurationTypeDef],
    },
)
CreateKxClusterRequestRequestTypeDef = TypedDict(
    "CreateKxClusterRequestRequestTypeDef",
    {
        "environmentId": str,
        "clusterName": str,
        "clusterType": KxClusterTypeType,
        "releaseLabel": str,
        "vpcConfiguration": VpcConfigurationTypeDef,
        "azMode": KxAzModeType,
        "clientToken": NotRequired[str],
        "tickerplantLogConfiguration": NotRequired[TickerplantLogConfigurationTypeDef],
        "databases": NotRequired[Sequence[KxDatabaseConfigurationUnionTypeDef]],
        "cacheStorageConfigurations": NotRequired[Sequence[KxCacheStorageConfigurationTypeDef]],
        "autoScalingConfiguration": NotRequired[AutoScalingConfigurationTypeDef],
        "clusterDescription": NotRequired[str],
        "capacityConfiguration": NotRequired[CapacityConfigurationTypeDef],
        "initializationScript": NotRequired[str],
        "commandLineArguments": NotRequired[Sequence[KxCommandLineArgumentTypeDef]],
        "code": NotRequired[CodeConfigurationTypeDef],
        "executionRole": NotRequired[str],
        "savedownStorageConfiguration": NotRequired[KxSavedownStorageConfigurationTypeDef],
        "availabilityZoneId": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "scalingGroupConfiguration": NotRequired[KxScalingGroupConfigurationTypeDef],
    },
)
