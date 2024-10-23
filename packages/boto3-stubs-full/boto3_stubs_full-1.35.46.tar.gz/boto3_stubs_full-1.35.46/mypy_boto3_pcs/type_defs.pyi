"""
Type annotations for pcs service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/type_defs/)

Usage::

    ```python
    from mypy_boto3_pcs.type_defs import SlurmCustomSettingTypeDef

    data: SlurmCustomSettingTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    ClusterStatusType,
    ComputeNodeGroupStatusType,
    EndpointTypeType,
    PurchaseOptionType,
    QueueStatusType,
    SizeType,
    SpotAllocationStrategyType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "SlurmCustomSettingTypeDef",
    "SlurmAuthKeyTypeDef",
    "ClusterSummaryTypeDef",
    "EndpointTypeDef",
    "ErrorInfoTypeDef",
    "NetworkingTypeDef",
    "SchedulerTypeDef",
    "ComputeNodeGroupConfigurationTypeDef",
    "ComputeNodeGroupSummaryTypeDef",
    "CustomLaunchTemplateTypeDef",
    "InstanceConfigTypeDef",
    "ScalingConfigurationTypeDef",
    "SpotOptionsTypeDef",
    "NetworkingRequestTypeDef",
    "SchedulerRequestTypeDef",
    "ResponseMetadataTypeDef",
    "ScalingConfigurationRequestTypeDef",
    "DeleteClusterRequestRequestTypeDef",
    "DeleteComputeNodeGroupRequestRequestTypeDef",
    "DeleteQueueRequestRequestTypeDef",
    "GetClusterRequestRequestTypeDef",
    "GetComputeNodeGroupRequestRequestTypeDef",
    "GetQueueRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListClustersRequestRequestTypeDef",
    "ListComputeNodeGroupsRequestRequestTypeDef",
    "ListQueuesRequestRequestTypeDef",
    "QueueSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "RegisterComputeNodeGroupInstanceRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "ClusterSlurmConfigurationRequestTypeDef",
    "ComputeNodeGroupSlurmConfigurationRequestTypeDef",
    "ComputeNodeGroupSlurmConfigurationTypeDef",
    "UpdateComputeNodeGroupSlurmConfigurationRequestTypeDef",
    "ClusterSlurmConfigurationTypeDef",
    "CreateQueueRequestRequestTypeDef",
    "QueueTypeDef",
    "UpdateQueueRequestRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ListClustersResponseTypeDef",
    "ListComputeNodeGroupsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "RegisterComputeNodeGroupInstanceResponseTypeDef",
    "ListClustersRequestListClustersPaginateTypeDef",
    "ListComputeNodeGroupsRequestListComputeNodeGroupsPaginateTypeDef",
    "ListQueuesRequestListQueuesPaginateTypeDef",
    "ListQueuesResponseTypeDef",
    "CreateClusterRequestRequestTypeDef",
    "CreateComputeNodeGroupRequestRequestTypeDef",
    "ComputeNodeGroupTypeDef",
    "UpdateComputeNodeGroupRequestRequestTypeDef",
    "ClusterTypeDef",
    "CreateQueueResponseTypeDef",
    "GetQueueResponseTypeDef",
    "UpdateQueueResponseTypeDef",
    "CreateComputeNodeGroupResponseTypeDef",
    "GetComputeNodeGroupResponseTypeDef",
    "UpdateComputeNodeGroupResponseTypeDef",
    "CreateClusterResponseTypeDef",
    "GetClusterResponseTypeDef",
)

SlurmCustomSettingTypeDef = TypedDict(
    "SlurmCustomSettingTypeDef",
    {
        "parameterName": str,
        "parameterValue": str,
    },
)
SlurmAuthKeyTypeDef = TypedDict(
    "SlurmAuthKeyTypeDef",
    {
        "secretArn": str,
        "secretVersion": str,
    },
)
ClusterSummaryTypeDef = TypedDict(
    "ClusterSummaryTypeDef",
    {
        "name": str,
        "id": str,
        "arn": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "status": ClusterStatusType,
    },
)
EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "type": EndpointTypeType,
        "privateIpAddress": str,
        "port": str,
        "publicIpAddress": NotRequired[str],
    },
)
ErrorInfoTypeDef = TypedDict(
    "ErrorInfoTypeDef",
    {
        "code": NotRequired[str],
        "message": NotRequired[str],
    },
)
NetworkingTypeDef = TypedDict(
    "NetworkingTypeDef",
    {
        "subnetIds": NotRequired[List[str]],
        "securityGroupIds": NotRequired[List[str]],
    },
)
SchedulerTypeDef = TypedDict(
    "SchedulerTypeDef",
    {
        "type": Literal["SLURM"],
        "version": str,
    },
)
ComputeNodeGroupConfigurationTypeDef = TypedDict(
    "ComputeNodeGroupConfigurationTypeDef",
    {
        "computeNodeGroupId": NotRequired[str],
    },
)
ComputeNodeGroupSummaryTypeDef = TypedDict(
    "ComputeNodeGroupSummaryTypeDef",
    {
        "name": str,
        "id": str,
        "arn": str,
        "clusterId": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "status": ComputeNodeGroupStatusType,
    },
)
CustomLaunchTemplateTypeDef = TypedDict(
    "CustomLaunchTemplateTypeDef",
    {
        "id": str,
        "version": str,
    },
)
InstanceConfigTypeDef = TypedDict(
    "InstanceConfigTypeDef",
    {
        "instanceType": NotRequired[str],
    },
)
ScalingConfigurationTypeDef = TypedDict(
    "ScalingConfigurationTypeDef",
    {
        "minInstanceCount": int,
        "maxInstanceCount": int,
    },
)
SpotOptionsTypeDef = TypedDict(
    "SpotOptionsTypeDef",
    {
        "allocationStrategy": NotRequired[SpotAllocationStrategyType],
    },
)
NetworkingRequestTypeDef = TypedDict(
    "NetworkingRequestTypeDef",
    {
        "subnetIds": NotRequired[Sequence[str]],
        "securityGroupIds": NotRequired[Sequence[str]],
    },
)
SchedulerRequestTypeDef = TypedDict(
    "SchedulerRequestTypeDef",
    {
        "type": Literal["SLURM"],
        "version": str,
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
ScalingConfigurationRequestTypeDef = TypedDict(
    "ScalingConfigurationRequestTypeDef",
    {
        "minInstanceCount": int,
        "maxInstanceCount": int,
    },
)
DeleteClusterRequestRequestTypeDef = TypedDict(
    "DeleteClusterRequestRequestTypeDef",
    {
        "clusterIdentifier": str,
        "clientToken": NotRequired[str],
    },
)
DeleteComputeNodeGroupRequestRequestTypeDef = TypedDict(
    "DeleteComputeNodeGroupRequestRequestTypeDef",
    {
        "clusterIdentifier": str,
        "computeNodeGroupIdentifier": str,
        "clientToken": NotRequired[str],
    },
)
DeleteQueueRequestRequestTypeDef = TypedDict(
    "DeleteQueueRequestRequestTypeDef",
    {
        "clusterIdentifier": str,
        "queueIdentifier": str,
        "clientToken": NotRequired[str],
    },
)
GetClusterRequestRequestTypeDef = TypedDict(
    "GetClusterRequestRequestTypeDef",
    {
        "clusterIdentifier": str,
    },
)
GetComputeNodeGroupRequestRequestTypeDef = TypedDict(
    "GetComputeNodeGroupRequestRequestTypeDef",
    {
        "clusterIdentifier": str,
        "computeNodeGroupIdentifier": str,
    },
)
GetQueueRequestRequestTypeDef = TypedDict(
    "GetQueueRequestRequestTypeDef",
    {
        "clusterIdentifier": str,
        "queueIdentifier": str,
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
ListClustersRequestRequestTypeDef = TypedDict(
    "ListClustersRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListComputeNodeGroupsRequestRequestTypeDef = TypedDict(
    "ListComputeNodeGroupsRequestRequestTypeDef",
    {
        "clusterIdentifier": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListQueuesRequestRequestTypeDef = TypedDict(
    "ListQueuesRequestRequestTypeDef",
    {
        "clusterIdentifier": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
QueueSummaryTypeDef = TypedDict(
    "QueueSummaryTypeDef",
    {
        "name": str,
        "id": str,
        "arn": str,
        "clusterId": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "status": QueueStatusType,
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
RegisterComputeNodeGroupInstanceRequestRequestTypeDef = TypedDict(
    "RegisterComputeNodeGroupInstanceRequestRequestTypeDef",
    {
        "clusterIdentifier": str,
        "bootstrapId": str,
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
ClusterSlurmConfigurationRequestTypeDef = TypedDict(
    "ClusterSlurmConfigurationRequestTypeDef",
    {
        "scaleDownIdleTimeInSeconds": NotRequired[int],
        "slurmCustomSettings": NotRequired[Sequence[SlurmCustomSettingTypeDef]],
    },
)
ComputeNodeGroupSlurmConfigurationRequestTypeDef = TypedDict(
    "ComputeNodeGroupSlurmConfigurationRequestTypeDef",
    {
        "slurmCustomSettings": NotRequired[Sequence[SlurmCustomSettingTypeDef]],
    },
)
ComputeNodeGroupSlurmConfigurationTypeDef = TypedDict(
    "ComputeNodeGroupSlurmConfigurationTypeDef",
    {
        "slurmCustomSettings": NotRequired[List[SlurmCustomSettingTypeDef]],
    },
)
UpdateComputeNodeGroupSlurmConfigurationRequestTypeDef = TypedDict(
    "UpdateComputeNodeGroupSlurmConfigurationRequestTypeDef",
    {
        "slurmCustomSettings": NotRequired[Sequence[SlurmCustomSettingTypeDef]],
    },
)
ClusterSlurmConfigurationTypeDef = TypedDict(
    "ClusterSlurmConfigurationTypeDef",
    {
        "scaleDownIdleTimeInSeconds": NotRequired[int],
        "slurmCustomSettings": NotRequired[List[SlurmCustomSettingTypeDef]],
        "authKey": NotRequired[SlurmAuthKeyTypeDef],
    },
)
CreateQueueRequestRequestTypeDef = TypedDict(
    "CreateQueueRequestRequestTypeDef",
    {
        "clusterIdentifier": str,
        "queueName": str,
        "computeNodeGroupConfigurations": NotRequired[
            Sequence[ComputeNodeGroupConfigurationTypeDef]
        ],
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
QueueTypeDef = TypedDict(
    "QueueTypeDef",
    {
        "name": str,
        "id": str,
        "arn": str,
        "clusterId": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "status": QueueStatusType,
        "computeNodeGroupConfigurations": List[ComputeNodeGroupConfigurationTypeDef],
        "errorInfo": NotRequired[List[ErrorInfoTypeDef]],
    },
)
UpdateQueueRequestRequestTypeDef = TypedDict(
    "UpdateQueueRequestRequestTypeDef",
    {
        "clusterIdentifier": str,
        "queueIdentifier": str,
        "computeNodeGroupConfigurations": NotRequired[
            Sequence[ComputeNodeGroupConfigurationTypeDef]
        ],
        "clientToken": NotRequired[str],
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListClustersResponseTypeDef = TypedDict(
    "ListClustersResponseTypeDef",
    {
        "clusters": List[ClusterSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListComputeNodeGroupsResponseTypeDef = TypedDict(
    "ListComputeNodeGroupsResponseTypeDef",
    {
        "computeNodeGroups": List[ComputeNodeGroupSummaryTypeDef],
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
RegisterComputeNodeGroupInstanceResponseTypeDef = TypedDict(
    "RegisterComputeNodeGroupInstanceResponseTypeDef",
    {
        "nodeID": str,
        "sharedSecret": str,
        "endpoints": List[EndpointTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListClustersRequestListClustersPaginateTypeDef = TypedDict(
    "ListClustersRequestListClustersPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListComputeNodeGroupsRequestListComputeNodeGroupsPaginateTypeDef = TypedDict(
    "ListComputeNodeGroupsRequestListComputeNodeGroupsPaginateTypeDef",
    {
        "clusterIdentifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListQueuesRequestListQueuesPaginateTypeDef = TypedDict(
    "ListQueuesRequestListQueuesPaginateTypeDef",
    {
        "clusterIdentifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListQueuesResponseTypeDef = TypedDict(
    "ListQueuesResponseTypeDef",
    {
        "queues": List[QueueSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateClusterRequestRequestTypeDef = TypedDict(
    "CreateClusterRequestRequestTypeDef",
    {
        "clusterName": str,
        "scheduler": SchedulerRequestTypeDef,
        "size": SizeType,
        "networking": NetworkingRequestTypeDef,
        "slurmConfiguration": NotRequired[ClusterSlurmConfigurationRequestTypeDef],
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateComputeNodeGroupRequestRequestTypeDef = TypedDict(
    "CreateComputeNodeGroupRequestRequestTypeDef",
    {
        "clusterIdentifier": str,
        "computeNodeGroupName": str,
        "subnetIds": Sequence[str],
        "customLaunchTemplate": CustomLaunchTemplateTypeDef,
        "iamInstanceProfileArn": str,
        "scalingConfiguration": ScalingConfigurationRequestTypeDef,
        "instanceConfigs": Sequence[InstanceConfigTypeDef],
        "amiId": NotRequired[str],
        "purchaseOption": NotRequired[PurchaseOptionType],
        "spotOptions": NotRequired[SpotOptionsTypeDef],
        "slurmConfiguration": NotRequired[ComputeNodeGroupSlurmConfigurationRequestTypeDef],
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
ComputeNodeGroupTypeDef = TypedDict(
    "ComputeNodeGroupTypeDef",
    {
        "name": str,
        "id": str,
        "arn": str,
        "clusterId": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "status": ComputeNodeGroupStatusType,
        "subnetIds": List[str],
        "customLaunchTemplate": CustomLaunchTemplateTypeDef,
        "iamInstanceProfileArn": str,
        "scalingConfiguration": ScalingConfigurationTypeDef,
        "instanceConfigs": List[InstanceConfigTypeDef],
        "amiId": NotRequired[str],
        "purchaseOption": NotRequired[PurchaseOptionType],
        "spotOptions": NotRequired[SpotOptionsTypeDef],
        "slurmConfiguration": NotRequired[ComputeNodeGroupSlurmConfigurationTypeDef],
        "errorInfo": NotRequired[List[ErrorInfoTypeDef]],
    },
)
UpdateComputeNodeGroupRequestRequestTypeDef = TypedDict(
    "UpdateComputeNodeGroupRequestRequestTypeDef",
    {
        "clusterIdentifier": str,
        "computeNodeGroupIdentifier": str,
        "amiId": NotRequired[str],
        "subnetIds": NotRequired[Sequence[str]],
        "customLaunchTemplate": NotRequired[CustomLaunchTemplateTypeDef],
        "purchaseOption": NotRequired[PurchaseOptionType],
        "spotOptions": NotRequired[SpotOptionsTypeDef],
        "scalingConfiguration": NotRequired[ScalingConfigurationRequestTypeDef],
        "iamInstanceProfileArn": NotRequired[str],
        "slurmConfiguration": NotRequired[UpdateComputeNodeGroupSlurmConfigurationRequestTypeDef],
        "clientToken": NotRequired[str],
    },
)
ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "name": str,
        "id": str,
        "arn": str,
        "status": ClusterStatusType,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "scheduler": SchedulerTypeDef,
        "size": SizeType,
        "networking": NetworkingTypeDef,
        "slurmConfiguration": NotRequired[ClusterSlurmConfigurationTypeDef],
        "endpoints": NotRequired[List[EndpointTypeDef]],
        "errorInfo": NotRequired[List[ErrorInfoTypeDef]],
    },
)
CreateQueueResponseTypeDef = TypedDict(
    "CreateQueueResponseTypeDef",
    {
        "queue": QueueTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetQueueResponseTypeDef = TypedDict(
    "GetQueueResponseTypeDef",
    {
        "queue": QueueTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateQueueResponseTypeDef = TypedDict(
    "UpdateQueueResponseTypeDef",
    {
        "queue": QueueTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateComputeNodeGroupResponseTypeDef = TypedDict(
    "CreateComputeNodeGroupResponseTypeDef",
    {
        "computeNodeGroup": ComputeNodeGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetComputeNodeGroupResponseTypeDef = TypedDict(
    "GetComputeNodeGroupResponseTypeDef",
    {
        "computeNodeGroup": ComputeNodeGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateComputeNodeGroupResponseTypeDef = TypedDict(
    "UpdateComputeNodeGroupResponseTypeDef",
    {
        "computeNodeGroup": ComputeNodeGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateClusterResponseTypeDef = TypedDict(
    "CreateClusterResponseTypeDef",
    {
        "cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetClusterResponseTypeDef = TypedDict(
    "GetClusterResponseTypeDef",
    {
        "cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
