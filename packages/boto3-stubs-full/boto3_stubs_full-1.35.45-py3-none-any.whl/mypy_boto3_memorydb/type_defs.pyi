"""
Type annotations for memorydb service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/type_defs/)

Usage::

    ```python
    from mypy_boto3_memorydb.type_defs import ACLPendingChangesTypeDef

    data: ACLPendingChangesTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    AuthenticationTypeType,
    AZStatusType,
    DataTieringStatusType,
    InputAuthenticationTypeType,
    ServiceUpdateStatusType,
    SourceTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "ACLPendingChangesTypeDef",
    "ACLsUpdateStatusTypeDef",
    "AuthenticationModeTypeDef",
    "AuthenticationTypeDef",
    "AvailabilityZoneTypeDef",
    "ServiceUpdateRequestTypeDef",
    "ResponseMetadataTypeDef",
    "UnprocessedClusterTypeDef",
    "PendingModifiedServiceUpdateTypeDef",
    "EndpointTypeDef",
    "SecurityGroupMembershipTypeDef",
    "TagTypeDef",
    "ParameterGroupTypeDef",
    "DeleteACLRequestRequestTypeDef",
    "DeleteClusterRequestRequestTypeDef",
    "DeleteParameterGroupRequestRequestTypeDef",
    "DeleteSnapshotRequestRequestTypeDef",
    "DeleteSubnetGroupRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeACLsRequestRequestTypeDef",
    "DescribeClustersRequestRequestTypeDef",
    "DescribeEngineVersionsRequestRequestTypeDef",
    "EngineVersionInfoTypeDef",
    "TimestampTypeDef",
    "EventTypeDef",
    "DescribeParameterGroupsRequestRequestTypeDef",
    "DescribeParametersRequestRequestTypeDef",
    "ParameterTypeDef",
    "DescribeReservedNodesOfferingsRequestRequestTypeDef",
    "DescribeReservedNodesRequestRequestTypeDef",
    "DescribeServiceUpdatesRequestRequestTypeDef",
    "ServiceUpdateTypeDef",
    "DescribeSnapshotsRequestRequestTypeDef",
    "DescribeSubnetGroupsRequestRequestTypeDef",
    "FilterTypeDef",
    "FailoverShardRequestRequestTypeDef",
    "ListAllowedNodeTypeUpdatesRequestRequestTypeDef",
    "ListTagsRequestRequestTypeDef",
    "ParameterNameValueTypeDef",
    "RecurringChargeTypeDef",
    "ReplicaConfigurationRequestTypeDef",
    "ResetParameterGroupRequestRequestTypeDef",
    "SlotMigrationTypeDef",
    "ShardConfigurationRequestTypeDef",
    "ShardConfigurationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateACLRequestRequestTypeDef",
    "UpdateSubnetGroupRequestRequestTypeDef",
    "ACLTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "UserTypeDef",
    "SubnetTypeDef",
    "BatchUpdateClusterRequestRequestTypeDef",
    "ListAllowedNodeTypeUpdatesResponseTypeDef",
    "NodeTypeDef",
    "CopySnapshotRequestRequestTypeDef",
    "CreateACLRequestRequestTypeDef",
    "CreateClusterRequestRequestTypeDef",
    "CreateParameterGroupRequestRequestTypeDef",
    "CreateSnapshotRequestRequestTypeDef",
    "CreateSubnetGroupRequestRequestTypeDef",
    "CreateUserRequestRequestTypeDef",
    "ListTagsResponseTypeDef",
    "PurchaseReservedNodesOfferingRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagResourceResponseTypeDef",
    "UntagResourceResponseTypeDef",
    "CreateParameterGroupResponseTypeDef",
    "DeleteParameterGroupResponseTypeDef",
    "DescribeParameterGroupsResponseTypeDef",
    "ResetParameterGroupResponseTypeDef",
    "UpdateParameterGroupResponseTypeDef",
    "DescribeACLsRequestDescribeACLsPaginateTypeDef",
    "DescribeClustersRequestDescribeClustersPaginateTypeDef",
    "DescribeEngineVersionsRequestDescribeEngineVersionsPaginateTypeDef",
    "DescribeParameterGroupsRequestDescribeParameterGroupsPaginateTypeDef",
    "DescribeParametersRequestDescribeParametersPaginateTypeDef",
    "DescribeReservedNodesOfferingsRequestDescribeReservedNodesOfferingsPaginateTypeDef",
    "DescribeReservedNodesRequestDescribeReservedNodesPaginateTypeDef",
    "DescribeServiceUpdatesRequestDescribeServiceUpdatesPaginateTypeDef",
    "DescribeSnapshotsRequestDescribeSnapshotsPaginateTypeDef",
    "DescribeSubnetGroupsRequestDescribeSubnetGroupsPaginateTypeDef",
    "DescribeEngineVersionsResponseTypeDef",
    "DescribeEventsRequestDescribeEventsPaginateTypeDef",
    "DescribeEventsRequestRequestTypeDef",
    "DescribeEventsResponseTypeDef",
    "DescribeParametersResponseTypeDef",
    "DescribeServiceUpdatesResponseTypeDef",
    "DescribeUsersRequestDescribeUsersPaginateTypeDef",
    "DescribeUsersRequestRequestTypeDef",
    "UpdateParameterGroupRequestRequestTypeDef",
    "ReservedNodeTypeDef",
    "ReservedNodesOfferingTypeDef",
    "ReshardingStatusTypeDef",
    "UpdateClusterRequestRequestTypeDef",
    "ShardDetailTypeDef",
    "CreateACLResponseTypeDef",
    "DeleteACLResponseTypeDef",
    "DescribeACLsResponseTypeDef",
    "UpdateACLResponseTypeDef",
    "CreateUserResponseTypeDef",
    "DeleteUserResponseTypeDef",
    "DescribeUsersResponseTypeDef",
    "UpdateUserResponseTypeDef",
    "SubnetGroupTypeDef",
    "ShardTypeDef",
    "DescribeReservedNodesResponseTypeDef",
    "PurchaseReservedNodesOfferingResponseTypeDef",
    "DescribeReservedNodesOfferingsResponseTypeDef",
    "ClusterPendingUpdatesTypeDef",
    "ClusterConfigurationTypeDef",
    "CreateSubnetGroupResponseTypeDef",
    "DeleteSubnetGroupResponseTypeDef",
    "DescribeSubnetGroupsResponseTypeDef",
    "UpdateSubnetGroupResponseTypeDef",
    "ClusterTypeDef",
    "SnapshotTypeDef",
    "BatchUpdateClusterResponseTypeDef",
    "CreateClusterResponseTypeDef",
    "DeleteClusterResponseTypeDef",
    "DescribeClustersResponseTypeDef",
    "FailoverShardResponseTypeDef",
    "UpdateClusterResponseTypeDef",
    "CopySnapshotResponseTypeDef",
    "CreateSnapshotResponseTypeDef",
    "DeleteSnapshotResponseTypeDef",
    "DescribeSnapshotsResponseTypeDef",
)

ACLPendingChangesTypeDef = TypedDict(
    "ACLPendingChangesTypeDef",
    {
        "UserNamesToRemove": NotRequired[List[str]],
        "UserNamesToAdd": NotRequired[List[str]],
    },
)
ACLsUpdateStatusTypeDef = TypedDict(
    "ACLsUpdateStatusTypeDef",
    {
        "ACLToApply": NotRequired[str],
    },
)
AuthenticationModeTypeDef = TypedDict(
    "AuthenticationModeTypeDef",
    {
        "Type": NotRequired[InputAuthenticationTypeType],
        "Passwords": NotRequired[Sequence[str]],
    },
)
AuthenticationTypeDef = TypedDict(
    "AuthenticationTypeDef",
    {
        "Type": NotRequired[AuthenticationTypeType],
        "PasswordCount": NotRequired[int],
    },
)
AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "Name": NotRequired[str],
    },
)
ServiceUpdateRequestTypeDef = TypedDict(
    "ServiceUpdateRequestTypeDef",
    {
        "ServiceUpdateNameToApply": NotRequired[str],
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
UnprocessedClusterTypeDef = TypedDict(
    "UnprocessedClusterTypeDef",
    {
        "ClusterName": NotRequired[str],
        "ErrorType": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)
PendingModifiedServiceUpdateTypeDef = TypedDict(
    "PendingModifiedServiceUpdateTypeDef",
    {
        "ServiceUpdateName": NotRequired[str],
        "Status": NotRequired[ServiceUpdateStatusType],
    },
)
EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": NotRequired[str],
        "Port": NotRequired[int],
    },
)
SecurityGroupMembershipTypeDef = TypedDict(
    "SecurityGroupMembershipTypeDef",
    {
        "SecurityGroupId": NotRequired[str],
        "Status": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
ParameterGroupTypeDef = TypedDict(
    "ParameterGroupTypeDef",
    {
        "Name": NotRequired[str],
        "Family": NotRequired[str],
        "Description": NotRequired[str],
        "ARN": NotRequired[str],
    },
)
DeleteACLRequestRequestTypeDef = TypedDict(
    "DeleteACLRequestRequestTypeDef",
    {
        "ACLName": str,
    },
)
DeleteClusterRequestRequestTypeDef = TypedDict(
    "DeleteClusterRequestRequestTypeDef",
    {
        "ClusterName": str,
        "FinalSnapshotName": NotRequired[str],
    },
)
DeleteParameterGroupRequestRequestTypeDef = TypedDict(
    "DeleteParameterGroupRequestRequestTypeDef",
    {
        "ParameterGroupName": str,
    },
)
DeleteSnapshotRequestRequestTypeDef = TypedDict(
    "DeleteSnapshotRequestRequestTypeDef",
    {
        "SnapshotName": str,
    },
)
DeleteSubnetGroupRequestRequestTypeDef = TypedDict(
    "DeleteSubnetGroupRequestRequestTypeDef",
    {
        "SubnetGroupName": str,
    },
)
DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "UserName": str,
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
DescribeACLsRequestRequestTypeDef = TypedDict(
    "DescribeACLsRequestRequestTypeDef",
    {
        "ACLName": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeClustersRequestRequestTypeDef = TypedDict(
    "DescribeClustersRequestRequestTypeDef",
    {
        "ClusterName": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ShowShardDetails": NotRequired[bool],
    },
)
DescribeEngineVersionsRequestRequestTypeDef = TypedDict(
    "DescribeEngineVersionsRequestRequestTypeDef",
    {
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "ParameterGroupFamily": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DefaultOnly": NotRequired[bool],
    },
)
EngineVersionInfoTypeDef = TypedDict(
    "EngineVersionInfoTypeDef",
    {
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "EnginePatchVersion": NotRequired[str],
        "ParameterGroupFamily": NotRequired[str],
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
        "ParameterGroupName": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeParametersRequestRequestTypeDef = TypedDict(
    "DescribeParametersRequestRequestTypeDef",
    {
        "ParameterGroupName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
        "Description": NotRequired[str],
        "DataType": NotRequired[str],
        "AllowedValues": NotRequired[str],
        "MinimumEngineVersion": NotRequired[str],
    },
)
DescribeReservedNodesOfferingsRequestRequestTypeDef = TypedDict(
    "DescribeReservedNodesOfferingsRequestRequestTypeDef",
    {
        "ReservedNodesOfferingId": NotRequired[str],
        "NodeType": NotRequired[str],
        "Duration": NotRequired[str],
        "OfferingType": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeReservedNodesRequestRequestTypeDef = TypedDict(
    "DescribeReservedNodesRequestRequestTypeDef",
    {
        "ReservationId": NotRequired[str],
        "ReservedNodesOfferingId": NotRequired[str],
        "NodeType": NotRequired[str],
        "Duration": NotRequired[str],
        "OfferingType": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeServiceUpdatesRequestRequestTypeDef = TypedDict(
    "DescribeServiceUpdatesRequestRequestTypeDef",
    {
        "ServiceUpdateName": NotRequired[str],
        "ClusterNames": NotRequired[Sequence[str]],
        "Status": NotRequired[Sequence[ServiceUpdateStatusType]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ServiceUpdateTypeDef = TypedDict(
    "ServiceUpdateTypeDef",
    {
        "ClusterName": NotRequired[str],
        "ServiceUpdateName": NotRequired[str],
        "ReleaseDate": NotRequired[datetime],
        "Description": NotRequired[str],
        "Status": NotRequired[ServiceUpdateStatusType],
        "Type": NotRequired[Literal["security-update"]],
        "Engine": NotRequired[str],
        "NodesUpdated": NotRequired[str],
        "AutoUpdateStartDate": NotRequired[datetime],
    },
)
DescribeSnapshotsRequestRequestTypeDef = TypedDict(
    "DescribeSnapshotsRequestRequestTypeDef",
    {
        "ClusterName": NotRequired[str],
        "SnapshotName": NotRequired[str],
        "Source": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ShowDetail": NotRequired[bool],
    },
)
DescribeSubnetGroupsRequestRequestTypeDef = TypedDict(
    "DescribeSubnetGroupsRequestRequestTypeDef",
    {
        "SubnetGroupName": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "Values": Sequence[str],
    },
)
FailoverShardRequestRequestTypeDef = TypedDict(
    "FailoverShardRequestRequestTypeDef",
    {
        "ClusterName": str,
        "ShardName": str,
    },
)
ListAllowedNodeTypeUpdatesRequestRequestTypeDef = TypedDict(
    "ListAllowedNodeTypeUpdatesRequestRequestTypeDef",
    {
        "ClusterName": str,
    },
)
ListTagsRequestRequestTypeDef = TypedDict(
    "ListTagsRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
ParameterNameValueTypeDef = TypedDict(
    "ParameterNameValueTypeDef",
    {
        "ParameterName": NotRequired[str],
        "ParameterValue": NotRequired[str],
    },
)
RecurringChargeTypeDef = TypedDict(
    "RecurringChargeTypeDef",
    {
        "RecurringChargeAmount": NotRequired[float],
        "RecurringChargeFrequency": NotRequired[str],
    },
)
ReplicaConfigurationRequestTypeDef = TypedDict(
    "ReplicaConfigurationRequestTypeDef",
    {
        "ReplicaCount": NotRequired[int],
    },
)
ResetParameterGroupRequestRequestTypeDef = TypedDict(
    "ResetParameterGroupRequestRequestTypeDef",
    {
        "ParameterGroupName": str,
        "AllParameters": NotRequired[bool],
        "ParameterNames": NotRequired[Sequence[str]],
    },
)
SlotMigrationTypeDef = TypedDict(
    "SlotMigrationTypeDef",
    {
        "ProgressPercentage": NotRequired[float],
    },
)
ShardConfigurationRequestTypeDef = TypedDict(
    "ShardConfigurationRequestTypeDef",
    {
        "ShardCount": NotRequired[int],
    },
)
ShardConfigurationTypeDef = TypedDict(
    "ShardConfigurationTypeDef",
    {
        "Slots": NotRequired[str],
        "ReplicaCount": NotRequired[int],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateACLRequestRequestTypeDef = TypedDict(
    "UpdateACLRequestRequestTypeDef",
    {
        "ACLName": str,
        "UserNamesToAdd": NotRequired[Sequence[str]],
        "UserNamesToRemove": NotRequired[Sequence[str]],
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
ACLTypeDef = TypedDict(
    "ACLTypeDef",
    {
        "Name": NotRequired[str],
        "Status": NotRequired[str],
        "UserNames": NotRequired[List[str]],
        "MinimumEngineVersion": NotRequired[str],
        "PendingChanges": NotRequired[ACLPendingChangesTypeDef],
        "Clusters": NotRequired[List[str]],
        "ARN": NotRequired[str],
    },
)
UpdateUserRequestRequestTypeDef = TypedDict(
    "UpdateUserRequestRequestTypeDef",
    {
        "UserName": str,
        "AuthenticationMode": NotRequired[AuthenticationModeTypeDef],
        "AccessString": NotRequired[str],
    },
)
UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "Name": NotRequired[str],
        "Status": NotRequired[str],
        "AccessString": NotRequired[str],
        "ACLNames": NotRequired[List[str]],
        "MinimumEngineVersion": NotRequired[str],
        "Authentication": NotRequired[AuthenticationTypeDef],
        "ARN": NotRequired[str],
    },
)
SubnetTypeDef = TypedDict(
    "SubnetTypeDef",
    {
        "Identifier": NotRequired[str],
        "AvailabilityZone": NotRequired[AvailabilityZoneTypeDef],
    },
)
BatchUpdateClusterRequestRequestTypeDef = TypedDict(
    "BatchUpdateClusterRequestRequestTypeDef",
    {
        "ClusterNames": Sequence[str],
        "ServiceUpdate": NotRequired[ServiceUpdateRequestTypeDef],
    },
)
ListAllowedNodeTypeUpdatesResponseTypeDef = TypedDict(
    "ListAllowedNodeTypeUpdatesResponseTypeDef",
    {
        "ScaleUpNodeTypes": List[str],
        "ScaleDownNodeTypes": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NodeTypeDef = TypedDict(
    "NodeTypeDef",
    {
        "Name": NotRequired[str],
        "Status": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "CreateTime": NotRequired[datetime],
        "Endpoint": NotRequired[EndpointTypeDef],
    },
)
CopySnapshotRequestRequestTypeDef = TypedDict(
    "CopySnapshotRequestRequestTypeDef",
    {
        "SourceSnapshotName": str,
        "TargetSnapshotName": str,
        "TargetBucket": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateACLRequestRequestTypeDef = TypedDict(
    "CreateACLRequestRequestTypeDef",
    {
        "ACLName": str,
        "UserNames": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateClusterRequestRequestTypeDef = TypedDict(
    "CreateClusterRequestRequestTypeDef",
    {
        "ClusterName": str,
        "NodeType": str,
        "ACLName": str,
        "ParameterGroupName": NotRequired[str],
        "Description": NotRequired[str],
        "NumShards": NotRequired[int],
        "NumReplicasPerShard": NotRequired[int],
        "SubnetGroupName": NotRequired[str],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "MaintenanceWindow": NotRequired[str],
        "Port": NotRequired[int],
        "SnsTopicArn": NotRequired[str],
        "TLSEnabled": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "SnapshotArns": NotRequired[Sequence[str]],
        "SnapshotName": NotRequired[str],
        "SnapshotRetentionLimit": NotRequired[int],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "SnapshotWindow": NotRequired[str],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "DataTiering": NotRequired[bool],
    },
)
CreateParameterGroupRequestRequestTypeDef = TypedDict(
    "CreateParameterGroupRequestRequestTypeDef",
    {
        "ParameterGroupName": str,
        "Family": str,
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateSnapshotRequestRequestTypeDef = TypedDict(
    "CreateSnapshotRequestRequestTypeDef",
    {
        "ClusterName": str,
        "SnapshotName": str,
        "KmsKeyId": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateSubnetGroupRequestRequestTypeDef = TypedDict(
    "CreateSubnetGroupRequestRequestTypeDef",
    {
        "SubnetGroupName": str,
        "SubnetIds": Sequence[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateUserRequestRequestTypeDef = TypedDict(
    "CreateUserRequestRequestTypeDef",
    {
        "UserName": str,
        "AuthenticationMode": AuthenticationModeTypeDef,
        "AccessString": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef",
    {
        "TagList": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PurchaseReservedNodesOfferingRequestRequestTypeDef = TypedDict(
    "PurchaseReservedNodesOfferingRequestRequestTypeDef",
    {
        "ReservedNodesOfferingId": str,
        "ReservationId": NotRequired[str],
        "NodeCount": NotRequired[int],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
TagResourceResponseTypeDef = TypedDict(
    "TagResourceResponseTypeDef",
    {
        "TagList": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UntagResourceResponseTypeDef = TypedDict(
    "UntagResourceResponseTypeDef",
    {
        "TagList": List[TagTypeDef],
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
DeleteParameterGroupResponseTypeDef = TypedDict(
    "DeleteParameterGroupResponseTypeDef",
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
ResetParameterGroupResponseTypeDef = TypedDict(
    "ResetParameterGroupResponseTypeDef",
    {
        "ParameterGroup": ParameterGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateParameterGroupResponseTypeDef = TypedDict(
    "UpdateParameterGroupResponseTypeDef",
    {
        "ParameterGroup": ParameterGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeACLsRequestDescribeACLsPaginateTypeDef = TypedDict(
    "DescribeACLsRequestDescribeACLsPaginateTypeDef",
    {
        "ACLName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeClustersRequestDescribeClustersPaginateTypeDef = TypedDict(
    "DescribeClustersRequestDescribeClustersPaginateTypeDef",
    {
        "ClusterName": NotRequired[str],
        "ShowShardDetails": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEngineVersionsRequestDescribeEngineVersionsPaginateTypeDef = TypedDict(
    "DescribeEngineVersionsRequestDescribeEngineVersionsPaginateTypeDef",
    {
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "ParameterGroupFamily": NotRequired[str],
        "DefaultOnly": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeParameterGroupsRequestDescribeParameterGroupsPaginateTypeDef = TypedDict(
    "DescribeParameterGroupsRequestDescribeParameterGroupsPaginateTypeDef",
    {
        "ParameterGroupName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeParametersRequestDescribeParametersPaginateTypeDef = TypedDict(
    "DescribeParametersRequestDescribeParametersPaginateTypeDef",
    {
        "ParameterGroupName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeReservedNodesOfferingsRequestDescribeReservedNodesOfferingsPaginateTypeDef = TypedDict(
    "DescribeReservedNodesOfferingsRequestDescribeReservedNodesOfferingsPaginateTypeDef",
    {
        "ReservedNodesOfferingId": NotRequired[str],
        "NodeType": NotRequired[str],
        "Duration": NotRequired[str],
        "OfferingType": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeReservedNodesRequestDescribeReservedNodesPaginateTypeDef = TypedDict(
    "DescribeReservedNodesRequestDescribeReservedNodesPaginateTypeDef",
    {
        "ReservationId": NotRequired[str],
        "ReservedNodesOfferingId": NotRequired[str],
        "NodeType": NotRequired[str],
        "Duration": NotRequired[str],
        "OfferingType": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeServiceUpdatesRequestDescribeServiceUpdatesPaginateTypeDef = TypedDict(
    "DescribeServiceUpdatesRequestDescribeServiceUpdatesPaginateTypeDef",
    {
        "ServiceUpdateName": NotRequired[str],
        "ClusterNames": NotRequired[Sequence[str]],
        "Status": NotRequired[Sequence[ServiceUpdateStatusType]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeSnapshotsRequestDescribeSnapshotsPaginateTypeDef = TypedDict(
    "DescribeSnapshotsRequestDescribeSnapshotsPaginateTypeDef",
    {
        "ClusterName": NotRequired[str],
        "SnapshotName": NotRequired[str],
        "Source": NotRequired[str],
        "ShowDetail": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeSubnetGroupsRequestDescribeSubnetGroupsPaginateTypeDef = TypedDict(
    "DescribeSubnetGroupsRequestDescribeSubnetGroupsPaginateTypeDef",
    {
        "SubnetGroupName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEngineVersionsResponseTypeDef = TypedDict(
    "DescribeEngineVersionsResponseTypeDef",
    {
        "EngineVersions": List[EngineVersionInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
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
DescribeParametersResponseTypeDef = TypedDict(
    "DescribeParametersResponseTypeDef",
    {
        "Parameters": List[ParameterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeServiceUpdatesResponseTypeDef = TypedDict(
    "DescribeServiceUpdatesResponseTypeDef",
    {
        "ServiceUpdates": List[ServiceUpdateTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeUsersRequestDescribeUsersPaginateTypeDef = TypedDict(
    "DescribeUsersRequestDescribeUsersPaginateTypeDef",
    {
        "UserName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeUsersRequestRequestTypeDef = TypedDict(
    "DescribeUsersRequestRequestTypeDef",
    {
        "UserName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
UpdateParameterGroupRequestRequestTypeDef = TypedDict(
    "UpdateParameterGroupRequestRequestTypeDef",
    {
        "ParameterGroupName": str,
        "ParameterNameValues": Sequence[ParameterNameValueTypeDef],
    },
)
ReservedNodeTypeDef = TypedDict(
    "ReservedNodeTypeDef",
    {
        "ReservationId": NotRequired[str],
        "ReservedNodesOfferingId": NotRequired[str],
        "NodeType": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "Duration": NotRequired[int],
        "FixedPrice": NotRequired[float],
        "NodeCount": NotRequired[int],
        "OfferingType": NotRequired[str],
        "State": NotRequired[str],
        "RecurringCharges": NotRequired[List[RecurringChargeTypeDef]],
        "ARN": NotRequired[str],
    },
)
ReservedNodesOfferingTypeDef = TypedDict(
    "ReservedNodesOfferingTypeDef",
    {
        "ReservedNodesOfferingId": NotRequired[str],
        "NodeType": NotRequired[str],
        "Duration": NotRequired[int],
        "FixedPrice": NotRequired[float],
        "OfferingType": NotRequired[str],
        "RecurringCharges": NotRequired[List[RecurringChargeTypeDef]],
    },
)
ReshardingStatusTypeDef = TypedDict(
    "ReshardingStatusTypeDef",
    {
        "SlotMigration": NotRequired[SlotMigrationTypeDef],
    },
)
UpdateClusterRequestRequestTypeDef = TypedDict(
    "UpdateClusterRequestRequestTypeDef",
    {
        "ClusterName": str,
        "Description": NotRequired[str],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "MaintenanceWindow": NotRequired[str],
        "SnsTopicArn": NotRequired[str],
        "SnsTopicStatus": NotRequired[str],
        "ParameterGroupName": NotRequired[str],
        "SnapshotWindow": NotRequired[str],
        "SnapshotRetentionLimit": NotRequired[int],
        "NodeType": NotRequired[str],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "ReplicaConfiguration": NotRequired[ReplicaConfigurationRequestTypeDef],
        "ShardConfiguration": NotRequired[ShardConfigurationRequestTypeDef],
        "ACLName": NotRequired[str],
    },
)
ShardDetailTypeDef = TypedDict(
    "ShardDetailTypeDef",
    {
        "Name": NotRequired[str],
        "Configuration": NotRequired[ShardConfigurationTypeDef],
        "Size": NotRequired[str],
        "SnapshotCreationTime": NotRequired[datetime],
    },
)
CreateACLResponseTypeDef = TypedDict(
    "CreateACLResponseTypeDef",
    {
        "ACL": ACLTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteACLResponseTypeDef = TypedDict(
    "DeleteACLResponseTypeDef",
    {
        "ACL": ACLTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeACLsResponseTypeDef = TypedDict(
    "DescribeACLsResponseTypeDef",
    {
        "ACLs": List[ACLTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateACLResponseTypeDef = TypedDict(
    "UpdateACLResponseTypeDef",
    {
        "ACL": ACLTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef",
    {
        "User": UserTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteUserResponseTypeDef = TypedDict(
    "DeleteUserResponseTypeDef",
    {
        "User": UserTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeUsersResponseTypeDef = TypedDict(
    "DescribeUsersResponseTypeDef",
    {
        "Users": List[UserTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateUserResponseTypeDef = TypedDict(
    "UpdateUserResponseTypeDef",
    {
        "User": UserTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SubnetGroupTypeDef = TypedDict(
    "SubnetGroupTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "VpcId": NotRequired[str],
        "Subnets": NotRequired[List[SubnetTypeDef]],
        "ARN": NotRequired[str],
    },
)
ShardTypeDef = TypedDict(
    "ShardTypeDef",
    {
        "Name": NotRequired[str],
        "Status": NotRequired[str],
        "Slots": NotRequired[str],
        "Nodes": NotRequired[List[NodeTypeDef]],
        "NumberOfNodes": NotRequired[int],
    },
)
DescribeReservedNodesResponseTypeDef = TypedDict(
    "DescribeReservedNodesResponseTypeDef",
    {
        "ReservedNodes": List[ReservedNodeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PurchaseReservedNodesOfferingResponseTypeDef = TypedDict(
    "PurchaseReservedNodesOfferingResponseTypeDef",
    {
        "ReservedNode": ReservedNodeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeReservedNodesOfferingsResponseTypeDef = TypedDict(
    "DescribeReservedNodesOfferingsResponseTypeDef",
    {
        "ReservedNodesOfferings": List[ReservedNodesOfferingTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ClusterPendingUpdatesTypeDef = TypedDict(
    "ClusterPendingUpdatesTypeDef",
    {
        "Resharding": NotRequired[ReshardingStatusTypeDef],
        "ACLs": NotRequired[ACLsUpdateStatusTypeDef],
        "ServiceUpdates": NotRequired[List[PendingModifiedServiceUpdateTypeDef]],
    },
)
ClusterConfigurationTypeDef = TypedDict(
    "ClusterConfigurationTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "NodeType": NotRequired[str],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "MaintenanceWindow": NotRequired[str],
        "TopicArn": NotRequired[str],
        "Port": NotRequired[int],
        "ParameterGroupName": NotRequired[str],
        "SubnetGroupName": NotRequired[str],
        "VpcId": NotRequired[str],
        "SnapshotRetentionLimit": NotRequired[int],
        "SnapshotWindow": NotRequired[str],
        "NumShards": NotRequired[int],
        "Shards": NotRequired[List[ShardDetailTypeDef]],
    },
)
CreateSubnetGroupResponseTypeDef = TypedDict(
    "CreateSubnetGroupResponseTypeDef",
    {
        "SubnetGroup": SubnetGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteSubnetGroupResponseTypeDef = TypedDict(
    "DeleteSubnetGroupResponseTypeDef",
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
ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Status": NotRequired[str],
        "PendingUpdates": NotRequired[ClusterPendingUpdatesTypeDef],
        "NumberOfShards": NotRequired[int],
        "Shards": NotRequired[List[ShardTypeDef]],
        "AvailabilityMode": NotRequired[AZStatusType],
        "ClusterEndpoint": NotRequired[EndpointTypeDef],
        "NodeType": NotRequired[str],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "EnginePatchVersion": NotRequired[str],
        "ParameterGroupName": NotRequired[str],
        "ParameterGroupStatus": NotRequired[str],
        "SecurityGroups": NotRequired[List[SecurityGroupMembershipTypeDef]],
        "SubnetGroupName": NotRequired[str],
        "TLSEnabled": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "ARN": NotRequired[str],
        "SnsTopicArn": NotRequired[str],
        "SnsTopicStatus": NotRequired[str],
        "SnapshotRetentionLimit": NotRequired[int],
        "MaintenanceWindow": NotRequired[str],
        "SnapshotWindow": NotRequired[str],
        "ACLName": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "DataTiering": NotRequired[DataTieringStatusType],
    },
)
SnapshotTypeDef = TypedDict(
    "SnapshotTypeDef",
    {
        "Name": NotRequired[str],
        "Status": NotRequired[str],
        "Source": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "ARN": NotRequired[str],
        "ClusterConfiguration": NotRequired[ClusterConfigurationTypeDef],
        "DataTiering": NotRequired[DataTieringStatusType],
    },
)
BatchUpdateClusterResponseTypeDef = TypedDict(
    "BatchUpdateClusterResponseTypeDef",
    {
        "ProcessedClusters": List[ClusterTypeDef],
        "UnprocessedClusters": List[UnprocessedClusterTypeDef],
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
FailoverShardResponseTypeDef = TypedDict(
    "FailoverShardResponseTypeDef",
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
CopySnapshotResponseTypeDef = TypedDict(
    "CopySnapshotResponseTypeDef",
    {
        "Snapshot": SnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSnapshotResponseTypeDef = TypedDict(
    "CreateSnapshotResponseTypeDef",
    {
        "Snapshot": SnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteSnapshotResponseTypeDef = TypedDict(
    "DeleteSnapshotResponseTypeDef",
    {
        "Snapshot": SnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSnapshotsResponseTypeDef = TypedDict(
    "DescribeSnapshotsResponseTypeDef",
    {
        "Snapshots": List[SnapshotTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
