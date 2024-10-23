"""
Type annotations for dax service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dax/type_defs/)

Usage::

    ```python
    from mypy_boto3_dax.type_defs import EndpointTypeDef

    data: EndpointTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    ChangeTypeType,
    ClusterEndpointEncryptionTypeType,
    IsModifiableType,
    ParameterTypeType,
    SourceTypeType,
    SSEStatusType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "EndpointTypeDef",
    "NotificationConfigurationTypeDef",
    "ParameterGroupStatusTypeDef",
    "SSEDescriptionTypeDef",
    "SecurityGroupMembershipTypeDef",
    "SSESpecificationTypeDef",
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "CreateParameterGroupRequestRequestTypeDef",
    "ParameterGroupTypeDef",
    "CreateSubnetGroupRequestRequestTypeDef",
    "DecreaseReplicationFactorRequestRequestTypeDef",
    "DeleteClusterRequestRequestTypeDef",
    "DeleteParameterGroupRequestRequestTypeDef",
    "DeleteSubnetGroupRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeClustersRequestRequestTypeDef",
    "DescribeDefaultParametersRequestRequestTypeDef",
    "TimestampTypeDef",
    "EventTypeDef",
    "DescribeParameterGroupsRequestRequestTypeDef",
    "DescribeParametersRequestRequestTypeDef",
    "DescribeSubnetGroupsRequestRequestTypeDef",
    "IncreaseReplicationFactorRequestRequestTypeDef",
    "ListTagsRequestRequestTypeDef",
    "NodeTypeSpecificValueTypeDef",
    "ParameterNameValueTypeDef",
    "RebootNodeRequestRequestTypeDef",
    "SubnetTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateClusterRequestRequestTypeDef",
    "UpdateSubnetGroupRequestRequestTypeDef",
    "NodeTypeDef",
    "CreateClusterRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "DeleteParameterGroupResponseTypeDef",
    "DeleteSubnetGroupResponseTypeDef",
    "ListTagsResponseTypeDef",
    "TagResourceResponseTypeDef",
    "UntagResourceResponseTypeDef",
    "CreateParameterGroupResponseTypeDef",
    "DescribeParameterGroupsResponseTypeDef",
    "UpdateParameterGroupResponseTypeDef",
    "DescribeClustersRequestDescribeClustersPaginateTypeDef",
    "DescribeDefaultParametersRequestDescribeDefaultParametersPaginateTypeDef",
    "DescribeParameterGroupsRequestDescribeParameterGroupsPaginateTypeDef",
    "DescribeParametersRequestDescribeParametersPaginateTypeDef",
    "DescribeSubnetGroupsRequestDescribeSubnetGroupsPaginateTypeDef",
    "ListTagsRequestListTagsPaginateTypeDef",
    "DescribeEventsRequestDescribeEventsPaginateTypeDef",
    "DescribeEventsRequestRequestTypeDef",
    "DescribeEventsResponseTypeDef",
    "ParameterTypeDef",
    "UpdateParameterGroupRequestRequestTypeDef",
    "SubnetGroupTypeDef",
    "ClusterTypeDef",
    "DescribeDefaultParametersResponseTypeDef",
    "DescribeParametersResponseTypeDef",
    "CreateSubnetGroupResponseTypeDef",
    "DescribeSubnetGroupsResponseTypeDef",
    "UpdateSubnetGroupResponseTypeDef",
    "CreateClusterResponseTypeDef",
    "DecreaseReplicationFactorResponseTypeDef",
    "DeleteClusterResponseTypeDef",
    "DescribeClustersResponseTypeDef",
    "IncreaseReplicationFactorResponseTypeDef",
    "RebootNodeResponseTypeDef",
    "UpdateClusterResponseTypeDef",
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": NotRequired[str],
        "Port": NotRequired[int],
        "URL": NotRequired[str],
    },
)
NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef",
    {
        "TopicArn": NotRequired[str],
        "TopicStatus": NotRequired[str],
    },
)
ParameterGroupStatusTypeDef = TypedDict(
    "ParameterGroupStatusTypeDef",
    {
        "ParameterGroupName": NotRequired[str],
        "ParameterApplyStatus": NotRequired[str],
        "NodeIdsToReboot": NotRequired[List[str]],
    },
)
SSEDescriptionTypeDef = TypedDict(
    "SSEDescriptionTypeDef",
    {
        "Status": NotRequired[SSEStatusType],
    },
)
SecurityGroupMembershipTypeDef = TypedDict(
    "SecurityGroupMembershipTypeDef",
    {
        "SecurityGroupIdentifier": NotRequired[str],
        "Status": NotRequired[str],
    },
)
SSESpecificationTypeDef = TypedDict(
    "SSESpecificationTypeDef",
    {
        "Enabled": bool,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
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
CreateParameterGroupRequestRequestTypeDef = TypedDict(
    "CreateParameterGroupRequestRequestTypeDef",
    {
        "ParameterGroupName": str,
        "Description": NotRequired[str],
    },
)
ParameterGroupTypeDef = TypedDict(
    "ParameterGroupTypeDef",
    {
        "ParameterGroupName": NotRequired[str],
        "Description": NotRequired[str],
    },
)
CreateSubnetGroupRequestRequestTypeDef = TypedDict(
    "CreateSubnetGroupRequestRequestTypeDef",
    {
        "SubnetGroupName": str,
        "SubnetIds": Sequence[str],
        "Description": NotRequired[str],
    },
)
DecreaseReplicationFactorRequestRequestTypeDef = TypedDict(
    "DecreaseReplicationFactorRequestRequestTypeDef",
    {
        "ClusterName": str,
        "NewReplicationFactor": int,
        "AvailabilityZones": NotRequired[Sequence[str]],
        "NodeIdsToRemove": NotRequired[Sequence[str]],
    },
)
DeleteClusterRequestRequestTypeDef = TypedDict(
    "DeleteClusterRequestRequestTypeDef",
    {
        "ClusterName": str,
    },
)
DeleteParameterGroupRequestRequestTypeDef = TypedDict(
    "DeleteParameterGroupRequestRequestTypeDef",
    {
        "ParameterGroupName": str,
    },
)
DeleteSubnetGroupRequestRequestTypeDef = TypedDict(
    "DeleteSubnetGroupRequestRequestTypeDef",
    {
        "SubnetGroupName": str,
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
DescribeClustersRequestRequestTypeDef = TypedDict(
    "DescribeClustersRequestRequestTypeDef",
    {
        "ClusterNames": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeDefaultParametersRequestRequestTypeDef = TypedDict(
    "DescribeDefaultParametersRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "SourceName": NotRequired[str],
        "SourceType": NotRequired[SourceTypeType],
        "Message": NotRequired[str],
        "Date": NotRequired[datetime],
    },
)
DescribeParameterGroupsRequestRequestTypeDef = TypedDict(
    "DescribeParameterGroupsRequestRequestTypeDef",
    {
        "ParameterGroupNames": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeParametersRequestRequestTypeDef = TypedDict(
    "DescribeParametersRequestRequestTypeDef",
    {
        "ParameterGroupName": str,
        "Source": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeSubnetGroupsRequestRequestTypeDef = TypedDict(
    "DescribeSubnetGroupsRequestRequestTypeDef",
    {
        "SubnetGroupNames": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
IncreaseReplicationFactorRequestRequestTypeDef = TypedDict(
    "IncreaseReplicationFactorRequestRequestTypeDef",
    {
        "ClusterName": str,
        "NewReplicationFactor": int,
        "AvailabilityZones": NotRequired[Sequence[str]],
    },
)
ListTagsRequestRequestTypeDef = TypedDict(
    "ListTagsRequestRequestTypeDef",
    {
        "ResourceName": str,
        "NextToken": NotRequired[str],
    },
)
NodeTypeSpecificValueTypeDef = TypedDict(
    "NodeTypeSpecificValueTypeDef",
    {
        "NodeType": NotRequired[str],
        "Value": NotRequired[str],
    },
)
ParameterNameValueTypeDef = TypedDict(
    "ParameterNameValueTypeDef",
    {
        "ParameterName": NotRequired[str],
        "ParameterValue": NotRequired[str],
    },
)
RebootNodeRequestRequestTypeDef = TypedDict(
    "RebootNodeRequestRequestTypeDef",
    {
        "ClusterName": str,
        "NodeId": str,
    },
)
SubnetTypeDef = TypedDict(
    "SubnetTypeDef",
    {
        "SubnetIdentifier": NotRequired[str],
        "SubnetAvailabilityZone": NotRequired[str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceName": str,
        "TagKeys": Sequence[str],
    },
)
UpdateClusterRequestRequestTypeDef = TypedDict(
    "UpdateClusterRequestRequestTypeDef",
    {
        "ClusterName": str,
        "Description": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "NotificationTopicArn": NotRequired[str],
        "NotificationTopicStatus": NotRequired[str],
        "ParameterGroupName": NotRequired[str],
        "SecurityGroupIds": NotRequired[Sequence[str]],
    },
)
UpdateSubnetGroupRequestRequestTypeDef = TypedDict(
    "UpdateSubnetGroupRequestRequestTypeDef",
    {
        "SubnetGroupName": str,
        "Description": NotRequired[str],
        "SubnetIds": NotRequired[Sequence[str]],
    },
)
NodeTypeDef = TypedDict(
    "NodeTypeDef",
    {
        "NodeId": NotRequired[str],
        "Endpoint": NotRequired[EndpointTypeDef],
        "NodeCreateTime": NotRequired[datetime],
        "AvailabilityZone": NotRequired[str],
        "NodeStatus": NotRequired[str],
        "ParameterGroupStatus": NotRequired[str],
    },
)
CreateClusterRequestRequestTypeDef = TypedDict(
    "CreateClusterRequestRequestTypeDef",
    {
        "ClusterName": str,
        "NodeType": str,
        "ReplicationFactor": int,
        "IamRoleArn": str,
        "Description": NotRequired[str],
        "AvailabilityZones": NotRequired[Sequence[str]],
        "SubnetGroupName": NotRequired[str],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "PreferredMaintenanceWindow": NotRequired[str],
        "NotificationTopicArn": NotRequired[str],
        "ParameterGroupName": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "SSESpecification": NotRequired[SSESpecificationTypeDef],
        "ClusterEndpointEncryptionType": NotRequired[ClusterEndpointEncryptionTypeType],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceName": str,
        "Tags": Sequence[TagTypeDef],
    },
)
DeleteParameterGroupResponseTypeDef = TypedDict(
    "DeleteParameterGroupResponseTypeDef",
    {
        "DeletionMessage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteSubnetGroupResponseTypeDef = TypedDict(
    "DeleteSubnetGroupResponseTypeDef",
    {
        "DeletionMessage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
TagResourceResponseTypeDef = TypedDict(
    "TagResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UntagResourceResponseTypeDef = TypedDict(
    "UntagResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateParameterGroupResponseTypeDef = TypedDict(
    "CreateParameterGroupResponseTypeDef",
    {
        "ParameterGroup": ParameterGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeParameterGroupsResponseTypeDef = TypedDict(
    "DescribeParameterGroupsResponseTypeDef",
    {
        "ParameterGroups": List[ParameterGroupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateParameterGroupResponseTypeDef = TypedDict(
    "UpdateParameterGroupResponseTypeDef",
    {
        "ParameterGroup": ParameterGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeClustersRequestDescribeClustersPaginateTypeDef = TypedDict(
    "DescribeClustersRequestDescribeClustersPaginateTypeDef",
    {
        "ClusterNames": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDefaultParametersRequestDescribeDefaultParametersPaginateTypeDef = TypedDict(
    "DescribeDefaultParametersRequestDescribeDefaultParametersPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeParameterGroupsRequestDescribeParameterGroupsPaginateTypeDef = TypedDict(
    "DescribeParameterGroupsRequestDescribeParameterGroupsPaginateTypeDef",
    {
        "ParameterGroupNames": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeParametersRequestDescribeParametersPaginateTypeDef = TypedDict(
    "DescribeParametersRequestDescribeParametersPaginateTypeDef",
    {
        "ParameterGroupName": str,
        "Source": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeSubnetGroupsRequestDescribeSubnetGroupsPaginateTypeDef = TypedDict(
    "DescribeSubnetGroupsRequestDescribeSubnetGroupsPaginateTypeDef",
    {
        "SubnetGroupNames": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTagsRequestListTagsPaginateTypeDef = TypedDict(
    "ListTagsRequestListTagsPaginateTypeDef",
    {
        "ResourceName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEventsRequestDescribeEventsPaginateTypeDef = TypedDict(
    "DescribeEventsRequestDescribeEventsPaginateTypeDef",
    {
        "SourceName": NotRequired[str],
        "SourceType": NotRequired[SourceTypeType],
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "Duration": NotRequired[int],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEventsRequestRequestTypeDef = TypedDict(
    "DescribeEventsRequestRequestTypeDef",
    {
        "SourceName": NotRequired[str],
        "SourceType": NotRequired[SourceTypeType],
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "Duration": NotRequired[int],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeEventsResponseTypeDef = TypedDict(
    "DescribeEventsResponseTypeDef",
    {
        "Events": List[EventTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "ParameterName": NotRequired[str],
        "ParameterType": NotRequired[ParameterTypeType],
        "ParameterValue": NotRequired[str],
        "NodeTypeSpecificValues": NotRequired[List[NodeTypeSpecificValueTypeDef]],
        "Description": NotRequired[str],
        "Source": NotRequired[str],
        "DataType": NotRequired[str],
        "AllowedValues": NotRequired[str],
        "IsModifiable": NotRequired[IsModifiableType],
        "ChangeType": NotRequired[ChangeTypeType],
    },
)
UpdateParameterGroupRequestRequestTypeDef = TypedDict(
    "UpdateParameterGroupRequestRequestTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterNameValues": Sequence[ParameterNameValueTypeDef],
    },
)
SubnetGroupTypeDef = TypedDict(
    "SubnetGroupTypeDef",
    {
        "SubnetGroupName": NotRequired[str],
        "Description": NotRequired[str],
        "VpcId": NotRequired[str],
        "Subnets": NotRequired[List[SubnetTypeDef]],
    },
)
ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "ClusterName": NotRequired[str],
        "Description": NotRequired[str],
        "ClusterArn": NotRequired[str],
        "TotalNodes": NotRequired[int],
        "ActiveNodes": NotRequired[int],
        "NodeType": NotRequired[str],
        "Status": NotRequired[str],
        "ClusterDiscoveryEndpoint": NotRequired[EndpointTypeDef],
        "NodeIdsToRemove": NotRequired[List[str]],
        "Nodes": NotRequired[List[NodeTypeDef]],
        "PreferredMaintenanceWindow": NotRequired[str],
        "NotificationConfiguration": NotRequired[NotificationConfigurationTypeDef],
        "SubnetGroup": NotRequired[str],
        "SecurityGroups": NotRequired[List[SecurityGroupMembershipTypeDef]],
        "IamRoleArn": NotRequired[str],
        "ParameterGroup": NotRequired[ParameterGroupStatusTypeDef],
        "SSEDescription": NotRequired[SSEDescriptionTypeDef],
        "ClusterEndpointEncryptionType": NotRequired[ClusterEndpointEncryptionTypeType],
    },
)
DescribeDefaultParametersResponseTypeDef = TypedDict(
    "DescribeDefaultParametersResponseTypeDef",
    {
        "Parameters": List[ParameterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeParametersResponseTypeDef = TypedDict(
    "DescribeParametersResponseTypeDef",
    {
        "Parameters": List[ParameterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateSubnetGroupResponseTypeDef = TypedDict(
    "CreateSubnetGroupResponseTypeDef",
    {
        "SubnetGroup": SubnetGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSubnetGroupsResponseTypeDef = TypedDict(
    "DescribeSubnetGroupsResponseTypeDef",
    {
        "SubnetGroups": List[SubnetGroupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateSubnetGroupResponseTypeDef = TypedDict(
    "UpdateSubnetGroupResponseTypeDef",
    {
        "SubnetGroup": SubnetGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateClusterResponseTypeDef = TypedDict(
    "CreateClusterResponseTypeDef",
    {
        "Cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DecreaseReplicationFactorResponseTypeDef = TypedDict(
    "DecreaseReplicationFactorResponseTypeDef",
    {
        "Cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteClusterResponseTypeDef = TypedDict(
    "DeleteClusterResponseTypeDef",
    {
        "Cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeClustersResponseTypeDef = TypedDict(
    "DescribeClustersResponseTypeDef",
    {
        "Clusters": List[ClusterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
IncreaseReplicationFactorResponseTypeDef = TypedDict(
    "IncreaseReplicationFactorResponseTypeDef",
    {
        "Cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RebootNodeResponseTypeDef = TypedDict(
    "RebootNodeResponseTypeDef",
    {
        "Cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateClusterResponseTypeDef = TypedDict(
    "UpdateClusterResponseTypeDef",
    {
        "Cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
