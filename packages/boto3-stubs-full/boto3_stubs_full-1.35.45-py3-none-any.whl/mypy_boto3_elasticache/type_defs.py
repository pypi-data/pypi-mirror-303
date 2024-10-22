"""
Type annotations for elasticache service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticache/type_defs/)

Usage::

    ```python
    from mypy_boto3_elasticache.type_defs import TagTypeDef

    data: TagTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    AuthenticationTypeType,
    AuthTokenUpdateStatusType,
    AuthTokenUpdateStrategyTypeType,
    AutomaticFailoverStatusType,
    AZModeType,
    ChangeTypeType,
    ClusterModeType,
    DataTieringStatusType,
    DestinationTypeType,
    InputAuthenticationTypeType,
    IpDiscoveryType,
    LogDeliveryConfigurationStatusType,
    LogFormatType,
    LogTypeType,
    MultiAZStatusType,
    NetworkTypeType,
    NodeUpdateInitiatedByType,
    NodeUpdateStatusType,
    OutpostModeType,
    PendingAutomaticFailoverStatusType,
    ServiceUpdateSeverityType,
    ServiceUpdateStatusType,
    SlaMetType,
    SourceTypeType,
    TransitEncryptionModeType,
    UpdateActionStatusType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "AuthenticationModeTypeDef",
    "AuthenticationTypeDef",
    "AuthorizeCacheSecurityGroupIngressMessageRequestTypeDef",
    "AvailabilityZoneTypeDef",
    "BatchApplyUpdateActionMessageRequestTypeDef",
    "BatchStopUpdateActionMessageRequestTypeDef",
    "CacheParameterGroupStatusTypeDef",
    "CacheSecurityGroupMembershipTypeDef",
    "EndpointTypeDef",
    "NotificationConfigurationTypeDef",
    "SecurityGroupMembershipTypeDef",
    "CacheEngineVersionTypeDef",
    "CacheNodeTypeSpecificValueTypeDef",
    "CacheNodeUpdateStatusTypeDef",
    "ParameterTypeDef",
    "CacheParameterGroupTypeDef",
    "EC2SecurityGroupTypeDef",
    "DataStorageTypeDef",
    "ECPUPerSecondTypeDef",
    "CloudWatchLogsDestinationDetailsTypeDef",
    "CompleteMigrationMessageRequestTypeDef",
    "ConfigureShardTypeDef",
    "CreateGlobalReplicationGroupMessageRequestTypeDef",
    "CustomerNodeEndpointTypeDef",
    "DecreaseNodeGroupsInGlobalReplicationGroupMessageRequestTypeDef",
    "DeleteCacheClusterMessageRequestTypeDef",
    "DeleteCacheParameterGroupMessageRequestTypeDef",
    "DeleteCacheSecurityGroupMessageRequestTypeDef",
    "DeleteCacheSubnetGroupMessageRequestTypeDef",
    "DeleteGlobalReplicationGroupMessageRequestTypeDef",
    "DeleteReplicationGroupMessageRequestTypeDef",
    "DeleteServerlessCacheRequestRequestTypeDef",
    "DeleteServerlessCacheSnapshotRequestRequestTypeDef",
    "DeleteSnapshotMessageRequestTypeDef",
    "DeleteUserGroupMessageRequestTypeDef",
    "DeleteUserMessageRequestTypeDef",
    "WaiterConfigTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeCacheClustersMessageRequestTypeDef",
    "DescribeCacheEngineVersionsMessageRequestTypeDef",
    "DescribeCacheParameterGroupsMessageRequestTypeDef",
    "DescribeCacheParametersMessageRequestTypeDef",
    "DescribeCacheSecurityGroupsMessageRequestTypeDef",
    "DescribeCacheSubnetGroupsMessageRequestTypeDef",
    "DescribeEngineDefaultParametersMessageRequestTypeDef",
    "TimestampTypeDef",
    "DescribeGlobalReplicationGroupsMessageRequestTypeDef",
    "DescribeReplicationGroupsMessageRequestTypeDef",
    "DescribeReservedCacheNodesMessageRequestTypeDef",
    "DescribeReservedCacheNodesOfferingsMessageRequestTypeDef",
    "DescribeServerlessCacheSnapshotsRequestRequestTypeDef",
    "DescribeServerlessCachesRequestRequestTypeDef",
    "DescribeServiceUpdatesMessageRequestTypeDef",
    "DescribeSnapshotsMessageRequestTypeDef",
    "DescribeUserGroupsMessageRequestTypeDef",
    "FilterTypeDef",
    "KinesisFirehoseDestinationDetailsTypeDef",
    "DisassociateGlobalReplicationGroupMessageRequestTypeDef",
    "EventTypeDef",
    "ExportServerlessCacheSnapshotRequestRequestTypeDef",
    "FailoverGlobalReplicationGroupMessageRequestTypeDef",
    "GlobalNodeGroupTypeDef",
    "GlobalReplicationGroupInfoTypeDef",
    "GlobalReplicationGroupMemberTypeDef",
    "ListAllowedNodeTypeModificationsMessageRequestTypeDef",
    "ListTagsForResourceMessageRequestTypeDef",
    "ParameterNameValueTypeDef",
    "ModifyCacheSubnetGroupMessageRequestTypeDef",
    "ModifyGlobalReplicationGroupMessageRequestTypeDef",
    "ReshardingConfigurationTypeDef",
    "ModifyUserGroupMessageRequestTypeDef",
    "NodeGroupConfigurationOutputTypeDef",
    "NodeGroupConfigurationTypeDef",
    "NodeGroupMemberUpdateStatusTypeDef",
    "ProcessedUpdateActionTypeDef",
    "RebalanceSlotsInGlobalReplicationGroupMessageRequestTypeDef",
    "RebootCacheClusterMessageRequestTypeDef",
    "RecurringChargeTypeDef",
    "RemoveTagsFromResourceMessageRequestTypeDef",
    "UserGroupsUpdateStatusTypeDef",
    "SlotMigrationTypeDef",
    "RevokeCacheSecurityGroupIngressMessageRequestTypeDef",
    "ServerlessCacheConfigurationTypeDef",
    "ServiceUpdateTypeDef",
    "SubnetOutpostTypeDef",
    "TestFailoverMessageRequestTypeDef",
    "UnprocessedUpdateActionTypeDef",
    "UserGroupPendingChangesTypeDef",
    "AddTagsToResourceMessageRequestTypeDef",
    "CopyServerlessCacheSnapshotRequestRequestTypeDef",
    "CopySnapshotMessageRequestTypeDef",
    "CreateCacheParameterGroupMessageRequestTypeDef",
    "CreateCacheSecurityGroupMessageRequestTypeDef",
    "CreateCacheSubnetGroupMessageRequestTypeDef",
    "CreateServerlessCacheSnapshotRequestRequestTypeDef",
    "CreateSnapshotMessageRequestTypeDef",
    "CreateUserGroupMessageRequestTypeDef",
    "PurchaseReservedCacheNodesOfferingMessageRequestTypeDef",
    "AllowedNodeTypeModificationsMessageTypeDef",
    "CacheParameterGroupNameMessageTypeDef",
    "EmptyResponseMetadataTypeDef",
    "TagListMessageTypeDef",
    "CreateUserMessageRequestTypeDef",
    "ModifyUserMessageRequestTypeDef",
    "UserResponseTypeDef",
    "UserTypeDef",
    "CacheNodeTypeDef",
    "NodeGroupMemberTypeDef",
    "CacheEngineVersionMessageTypeDef",
    "CacheNodeTypeSpecificParameterTypeDef",
    "CacheParameterGroupsMessageTypeDef",
    "CreateCacheParameterGroupResultTypeDef",
    "CacheSecurityGroupTypeDef",
    "CacheUsageLimitsTypeDef",
    "DecreaseReplicaCountMessageRequestTypeDef",
    "IncreaseReplicaCountMessageRequestTypeDef",
    "StartMigrationMessageRequestTypeDef",
    "TestMigrationMessageRequestTypeDef",
    "DescribeCacheClustersMessageCacheClusterAvailableWaitTypeDef",
    "DescribeCacheClustersMessageCacheClusterDeletedWaitTypeDef",
    "DescribeReplicationGroupsMessageReplicationGroupAvailableWaitTypeDef",
    "DescribeReplicationGroupsMessageReplicationGroupDeletedWaitTypeDef",
    "DescribeCacheClustersMessageDescribeCacheClustersPaginateTypeDef",
    "DescribeCacheEngineVersionsMessageDescribeCacheEngineVersionsPaginateTypeDef",
    "DescribeCacheParameterGroupsMessageDescribeCacheParameterGroupsPaginateTypeDef",
    "DescribeCacheParametersMessageDescribeCacheParametersPaginateTypeDef",
    "DescribeCacheSecurityGroupsMessageDescribeCacheSecurityGroupsPaginateTypeDef",
    "DescribeCacheSubnetGroupsMessageDescribeCacheSubnetGroupsPaginateTypeDef",
    "DescribeEngineDefaultParametersMessageDescribeEngineDefaultParametersPaginateTypeDef",
    "DescribeGlobalReplicationGroupsMessageDescribeGlobalReplicationGroupsPaginateTypeDef",
    "DescribeReplicationGroupsMessageDescribeReplicationGroupsPaginateTypeDef",
    "DescribeReservedCacheNodesMessageDescribeReservedCacheNodesPaginateTypeDef",
    "DescribeReservedCacheNodesOfferingsMessageDescribeReservedCacheNodesOfferingsPaginateTypeDef",
    "DescribeServerlessCacheSnapshotsRequestDescribeServerlessCacheSnapshotsPaginateTypeDef",
    "DescribeServerlessCachesRequestDescribeServerlessCachesPaginateTypeDef",
    "DescribeServiceUpdatesMessageDescribeServiceUpdatesPaginateTypeDef",
    "DescribeSnapshotsMessageDescribeSnapshotsPaginateTypeDef",
    "DescribeUserGroupsMessageDescribeUserGroupsPaginateTypeDef",
    "DescribeEventsMessageDescribeEventsPaginateTypeDef",
    "DescribeEventsMessageRequestTypeDef",
    "TimeRangeFilterTypeDef",
    "DescribeUsersMessageDescribeUsersPaginateTypeDef",
    "DescribeUsersMessageRequestTypeDef",
    "DestinationDetailsTypeDef",
    "EventsMessageTypeDef",
    "GlobalReplicationGroupTypeDef",
    "ModifyCacheParameterGroupMessageRequestTypeDef",
    "ResetCacheParameterGroupMessageRequestTypeDef",
    "ModifyReplicationGroupShardConfigurationMessageRequestTypeDef",
    "RegionalConfigurationTypeDef",
    "NodeSnapshotTypeDef",
    "NodeGroupConfigurationUnionTypeDef",
    "NodeGroupUpdateStatusTypeDef",
    "ReservedCacheNodeTypeDef",
    "ReservedCacheNodesOfferingTypeDef",
    "ReshardingStatusTypeDef",
    "ServerlessCacheSnapshotTypeDef",
    "ServiceUpdatesMessageTypeDef",
    "SubnetTypeDef",
    "UpdateActionResultsMessageTypeDef",
    "UserGroupResponseTypeDef",
    "UserGroupTypeDef",
    "DescribeUsersResultTypeDef",
    "NodeGroupTypeDef",
    "CacheParameterGroupDetailsTypeDef",
    "EngineDefaultsTypeDef",
    "AuthorizeCacheSecurityGroupIngressResultTypeDef",
    "CacheSecurityGroupMessageTypeDef",
    "CreateCacheSecurityGroupResultTypeDef",
    "RevokeCacheSecurityGroupIngressResultTypeDef",
    "CreateServerlessCacheRequestRequestTypeDef",
    "ModifyServerlessCacheRequestRequestTypeDef",
    "ServerlessCacheTypeDef",
    "DescribeUpdateActionsMessageDescribeUpdateActionsPaginateTypeDef",
    "DescribeUpdateActionsMessageRequestTypeDef",
    "LogDeliveryConfigurationRequestTypeDef",
    "LogDeliveryConfigurationTypeDef",
    "PendingLogDeliveryConfigurationTypeDef",
    "CreateGlobalReplicationGroupResultTypeDef",
    "DecreaseNodeGroupsInGlobalReplicationGroupResultTypeDef",
    "DeleteGlobalReplicationGroupResultTypeDef",
    "DescribeGlobalReplicationGroupsResultTypeDef",
    "DisassociateGlobalReplicationGroupResultTypeDef",
    "FailoverGlobalReplicationGroupResultTypeDef",
    "IncreaseNodeGroupsInGlobalReplicationGroupResultTypeDef",
    "ModifyGlobalReplicationGroupResultTypeDef",
    "RebalanceSlotsInGlobalReplicationGroupResultTypeDef",
    "IncreaseNodeGroupsInGlobalReplicationGroupMessageRequestTypeDef",
    "SnapshotTypeDef",
    "UpdateActionTypeDef",
    "PurchaseReservedCacheNodesOfferingResultTypeDef",
    "ReservedCacheNodeMessageTypeDef",
    "ReservedCacheNodesOfferingMessageTypeDef",
    "CopyServerlessCacheSnapshotResponseTypeDef",
    "CreateServerlessCacheSnapshotResponseTypeDef",
    "DeleteServerlessCacheSnapshotResponseTypeDef",
    "DescribeServerlessCacheSnapshotsResponseTypeDef",
    "ExportServerlessCacheSnapshotResponseTypeDef",
    "CacheSubnetGroupTypeDef",
    "DescribeUserGroupsResultTypeDef",
    "DescribeEngineDefaultParametersResultTypeDef",
    "CreateServerlessCacheResponseTypeDef",
    "DeleteServerlessCacheResponseTypeDef",
    "DescribeServerlessCachesResponseTypeDef",
    "ModifyServerlessCacheResponseTypeDef",
    "CreateCacheClusterMessageRequestTypeDef",
    "CreateReplicationGroupMessageRequestTypeDef",
    "ModifyCacheClusterMessageRequestTypeDef",
    "ModifyReplicationGroupMessageRequestTypeDef",
    "PendingModifiedValuesTypeDef",
    "ReplicationGroupPendingModifiedValuesTypeDef",
    "CopySnapshotResultTypeDef",
    "CreateSnapshotResultTypeDef",
    "DeleteSnapshotResultTypeDef",
    "DescribeSnapshotsListMessageTypeDef",
    "UpdateActionsMessageTypeDef",
    "CacheSubnetGroupMessageTypeDef",
    "CreateCacheSubnetGroupResultTypeDef",
    "ModifyCacheSubnetGroupResultTypeDef",
    "CacheClusterTypeDef",
    "ReplicationGroupTypeDef",
    "CacheClusterMessageTypeDef",
    "CreateCacheClusterResultTypeDef",
    "DeleteCacheClusterResultTypeDef",
    "ModifyCacheClusterResultTypeDef",
    "RebootCacheClusterResultTypeDef",
    "CompleteMigrationResponseTypeDef",
    "CreateReplicationGroupResultTypeDef",
    "DecreaseReplicaCountResultTypeDef",
    "DeleteReplicationGroupResultTypeDef",
    "IncreaseReplicaCountResultTypeDef",
    "ModifyReplicationGroupResultTypeDef",
    "ModifyReplicationGroupShardConfigurationResultTypeDef",
    "ReplicationGroupMessageTypeDef",
    "StartMigrationResponseTypeDef",
    "TestFailoverResultTypeDef",
    "TestMigrationResponseTypeDef",
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
AuthorizeCacheSecurityGroupIngressMessageRequestTypeDef = TypedDict(
    "AuthorizeCacheSecurityGroupIngressMessageRequestTypeDef",
    {
        "CacheSecurityGroupName": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupOwnerId": str,
    },
)
AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "Name": NotRequired[str],
    },
)
BatchApplyUpdateActionMessageRequestTypeDef = TypedDict(
    "BatchApplyUpdateActionMessageRequestTypeDef",
    {
        "ServiceUpdateName": str,
        "ReplicationGroupIds": NotRequired[Sequence[str]],
        "CacheClusterIds": NotRequired[Sequence[str]],
    },
)
BatchStopUpdateActionMessageRequestTypeDef = TypedDict(
    "BatchStopUpdateActionMessageRequestTypeDef",
    {
        "ServiceUpdateName": str,
        "ReplicationGroupIds": NotRequired[Sequence[str]],
        "CacheClusterIds": NotRequired[Sequence[str]],
    },
)
CacheParameterGroupStatusTypeDef = TypedDict(
    "CacheParameterGroupStatusTypeDef",
    {
        "CacheParameterGroupName": NotRequired[str],
        "ParameterApplyStatus": NotRequired[str],
        "CacheNodeIdsToReboot": NotRequired[List[str]],
    },
)
CacheSecurityGroupMembershipTypeDef = TypedDict(
    "CacheSecurityGroupMembershipTypeDef",
    {
        "CacheSecurityGroupName": NotRequired[str],
        "Status": NotRequired[str],
    },
)
EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": NotRequired[str],
        "Port": NotRequired[int],
    },
)
NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef",
    {
        "TopicArn": NotRequired[str],
        "TopicStatus": NotRequired[str],
    },
)
SecurityGroupMembershipTypeDef = TypedDict(
    "SecurityGroupMembershipTypeDef",
    {
        "SecurityGroupId": NotRequired[str],
        "Status": NotRequired[str],
    },
)
CacheEngineVersionTypeDef = TypedDict(
    "CacheEngineVersionTypeDef",
    {
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "CacheParameterGroupFamily": NotRequired[str],
        "CacheEngineDescription": NotRequired[str],
        "CacheEngineVersionDescription": NotRequired[str],
    },
)
CacheNodeTypeSpecificValueTypeDef = TypedDict(
    "CacheNodeTypeSpecificValueTypeDef",
    {
        "CacheNodeType": NotRequired[str],
        "Value": NotRequired[str],
    },
)
CacheNodeUpdateStatusTypeDef = TypedDict(
    "CacheNodeUpdateStatusTypeDef",
    {
        "CacheNodeId": NotRequired[str],
        "NodeUpdateStatus": NotRequired[NodeUpdateStatusType],
        "NodeDeletionDate": NotRequired[datetime],
        "NodeUpdateStartDate": NotRequired[datetime],
        "NodeUpdateEndDate": NotRequired[datetime],
        "NodeUpdateInitiatedBy": NotRequired[NodeUpdateInitiatedByType],
        "NodeUpdateInitiatedDate": NotRequired[datetime],
        "NodeUpdateStatusModifiedDate": NotRequired[datetime],
    },
)
ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "ParameterName": NotRequired[str],
        "ParameterValue": NotRequired[str],
        "Description": NotRequired[str],
        "Source": NotRequired[str],
        "DataType": NotRequired[str],
        "AllowedValues": NotRequired[str],
        "IsModifiable": NotRequired[bool],
        "MinimumEngineVersion": NotRequired[str],
        "ChangeType": NotRequired[ChangeTypeType],
    },
)
CacheParameterGroupTypeDef = TypedDict(
    "CacheParameterGroupTypeDef",
    {
        "CacheParameterGroupName": NotRequired[str],
        "CacheParameterGroupFamily": NotRequired[str],
        "Description": NotRequired[str],
        "IsGlobal": NotRequired[bool],
        "ARN": NotRequired[str],
    },
)
EC2SecurityGroupTypeDef = TypedDict(
    "EC2SecurityGroupTypeDef",
    {
        "Status": NotRequired[str],
        "EC2SecurityGroupName": NotRequired[str],
        "EC2SecurityGroupOwnerId": NotRequired[str],
    },
)
DataStorageTypeDef = TypedDict(
    "DataStorageTypeDef",
    {
        "Unit": Literal["GB"],
        "Maximum": NotRequired[int],
        "Minimum": NotRequired[int],
    },
)
ECPUPerSecondTypeDef = TypedDict(
    "ECPUPerSecondTypeDef",
    {
        "Maximum": NotRequired[int],
        "Minimum": NotRequired[int],
    },
)
CloudWatchLogsDestinationDetailsTypeDef = TypedDict(
    "CloudWatchLogsDestinationDetailsTypeDef",
    {
        "LogGroup": NotRequired[str],
    },
)
CompleteMigrationMessageRequestTypeDef = TypedDict(
    "CompleteMigrationMessageRequestTypeDef",
    {
        "ReplicationGroupId": str,
        "Force": NotRequired[bool],
    },
)
ConfigureShardTypeDef = TypedDict(
    "ConfigureShardTypeDef",
    {
        "NodeGroupId": str,
        "NewReplicaCount": int,
        "PreferredAvailabilityZones": NotRequired[Sequence[str]],
        "PreferredOutpostArns": NotRequired[Sequence[str]],
    },
)
CreateGlobalReplicationGroupMessageRequestTypeDef = TypedDict(
    "CreateGlobalReplicationGroupMessageRequestTypeDef",
    {
        "GlobalReplicationGroupIdSuffix": str,
        "PrimaryReplicationGroupId": str,
        "GlobalReplicationGroupDescription": NotRequired[str],
    },
)
CustomerNodeEndpointTypeDef = TypedDict(
    "CustomerNodeEndpointTypeDef",
    {
        "Address": NotRequired[str],
        "Port": NotRequired[int],
    },
)
DecreaseNodeGroupsInGlobalReplicationGroupMessageRequestTypeDef = TypedDict(
    "DecreaseNodeGroupsInGlobalReplicationGroupMessageRequestTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "NodeGroupCount": int,
        "ApplyImmediately": bool,
        "GlobalNodeGroupsToRemove": NotRequired[Sequence[str]],
        "GlobalNodeGroupsToRetain": NotRequired[Sequence[str]],
    },
)
DeleteCacheClusterMessageRequestTypeDef = TypedDict(
    "DeleteCacheClusterMessageRequestTypeDef",
    {
        "CacheClusterId": str,
        "FinalSnapshotIdentifier": NotRequired[str],
    },
)
DeleteCacheParameterGroupMessageRequestTypeDef = TypedDict(
    "DeleteCacheParameterGroupMessageRequestTypeDef",
    {
        "CacheParameterGroupName": str,
    },
)
DeleteCacheSecurityGroupMessageRequestTypeDef = TypedDict(
    "DeleteCacheSecurityGroupMessageRequestTypeDef",
    {
        "CacheSecurityGroupName": str,
    },
)
DeleteCacheSubnetGroupMessageRequestTypeDef = TypedDict(
    "DeleteCacheSubnetGroupMessageRequestTypeDef",
    {
        "CacheSubnetGroupName": str,
    },
)
DeleteGlobalReplicationGroupMessageRequestTypeDef = TypedDict(
    "DeleteGlobalReplicationGroupMessageRequestTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "RetainPrimaryReplicationGroup": bool,
    },
)
DeleteReplicationGroupMessageRequestTypeDef = TypedDict(
    "DeleteReplicationGroupMessageRequestTypeDef",
    {
        "ReplicationGroupId": str,
        "RetainPrimaryCluster": NotRequired[bool],
        "FinalSnapshotIdentifier": NotRequired[str],
    },
)
DeleteServerlessCacheRequestRequestTypeDef = TypedDict(
    "DeleteServerlessCacheRequestRequestTypeDef",
    {
        "ServerlessCacheName": str,
        "FinalSnapshotName": NotRequired[str],
    },
)
DeleteServerlessCacheSnapshotRequestRequestTypeDef = TypedDict(
    "DeleteServerlessCacheSnapshotRequestRequestTypeDef",
    {
        "ServerlessCacheSnapshotName": str,
    },
)
DeleteSnapshotMessageRequestTypeDef = TypedDict(
    "DeleteSnapshotMessageRequestTypeDef",
    {
        "SnapshotName": str,
    },
)
DeleteUserGroupMessageRequestTypeDef = TypedDict(
    "DeleteUserGroupMessageRequestTypeDef",
    {
        "UserGroupId": str,
    },
)
DeleteUserMessageRequestTypeDef = TypedDict(
    "DeleteUserMessageRequestTypeDef",
    {
        "UserId": str,
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
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
DescribeCacheClustersMessageRequestTypeDef = TypedDict(
    "DescribeCacheClustersMessageRequestTypeDef",
    {
        "CacheClusterId": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "ShowCacheNodeInfo": NotRequired[bool],
        "ShowCacheClustersNotInReplicationGroups": NotRequired[bool],
    },
)
DescribeCacheEngineVersionsMessageRequestTypeDef = TypedDict(
    "DescribeCacheEngineVersionsMessageRequestTypeDef",
    {
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "CacheParameterGroupFamily": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "DefaultOnly": NotRequired[bool],
    },
)
DescribeCacheParameterGroupsMessageRequestTypeDef = TypedDict(
    "DescribeCacheParameterGroupsMessageRequestTypeDef",
    {
        "CacheParameterGroupName": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeCacheParametersMessageRequestTypeDef = TypedDict(
    "DescribeCacheParametersMessageRequestTypeDef",
    {
        "CacheParameterGroupName": str,
        "Source": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeCacheSecurityGroupsMessageRequestTypeDef = TypedDict(
    "DescribeCacheSecurityGroupsMessageRequestTypeDef",
    {
        "CacheSecurityGroupName": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeCacheSubnetGroupsMessageRequestTypeDef = TypedDict(
    "DescribeCacheSubnetGroupsMessageRequestTypeDef",
    {
        "CacheSubnetGroupName": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeEngineDefaultParametersMessageRequestTypeDef = TypedDict(
    "DescribeEngineDefaultParametersMessageRequestTypeDef",
    {
        "CacheParameterGroupFamily": str,
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
DescribeGlobalReplicationGroupsMessageRequestTypeDef = TypedDict(
    "DescribeGlobalReplicationGroupsMessageRequestTypeDef",
    {
        "GlobalReplicationGroupId": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "ShowMemberInfo": NotRequired[bool],
    },
)
DescribeReplicationGroupsMessageRequestTypeDef = TypedDict(
    "DescribeReplicationGroupsMessageRequestTypeDef",
    {
        "ReplicationGroupId": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeReservedCacheNodesMessageRequestTypeDef = TypedDict(
    "DescribeReservedCacheNodesMessageRequestTypeDef",
    {
        "ReservedCacheNodeId": NotRequired[str],
        "ReservedCacheNodesOfferingId": NotRequired[str],
        "CacheNodeType": NotRequired[str],
        "Duration": NotRequired[str],
        "ProductDescription": NotRequired[str],
        "OfferingType": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeReservedCacheNodesOfferingsMessageRequestTypeDef = TypedDict(
    "DescribeReservedCacheNodesOfferingsMessageRequestTypeDef",
    {
        "ReservedCacheNodesOfferingId": NotRequired[str],
        "CacheNodeType": NotRequired[str],
        "Duration": NotRequired[str],
        "ProductDescription": NotRequired[str],
        "OfferingType": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeServerlessCacheSnapshotsRequestRequestTypeDef = TypedDict(
    "DescribeServerlessCacheSnapshotsRequestRequestTypeDef",
    {
        "ServerlessCacheName": NotRequired[str],
        "ServerlessCacheSnapshotName": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeServerlessCachesRequestRequestTypeDef = TypedDict(
    "DescribeServerlessCachesRequestRequestTypeDef",
    {
        "ServerlessCacheName": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeServiceUpdatesMessageRequestTypeDef = TypedDict(
    "DescribeServiceUpdatesMessageRequestTypeDef",
    {
        "ServiceUpdateName": NotRequired[str],
        "ServiceUpdateStatus": NotRequired[Sequence[ServiceUpdateStatusType]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeSnapshotsMessageRequestTypeDef = TypedDict(
    "DescribeSnapshotsMessageRequestTypeDef",
    {
        "ReplicationGroupId": NotRequired[str],
        "CacheClusterId": NotRequired[str],
        "SnapshotName": NotRequired[str],
        "SnapshotSource": NotRequired[str],
        "Marker": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "ShowNodeGroupConfig": NotRequired[bool],
    },
)
DescribeUserGroupsMessageRequestTypeDef = TypedDict(
    "DescribeUserGroupsMessageRequestTypeDef",
    {
        "UserGroupId": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "Values": Sequence[str],
    },
)
KinesisFirehoseDestinationDetailsTypeDef = TypedDict(
    "KinesisFirehoseDestinationDetailsTypeDef",
    {
        "DeliveryStream": NotRequired[str],
    },
)
DisassociateGlobalReplicationGroupMessageRequestTypeDef = TypedDict(
    "DisassociateGlobalReplicationGroupMessageRequestTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "ReplicationGroupId": str,
        "ReplicationGroupRegion": str,
    },
)
EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "SourceIdentifier": NotRequired[str],
        "SourceType": NotRequired[SourceTypeType],
        "Message": NotRequired[str],
        "Date": NotRequired[datetime],
    },
)
ExportServerlessCacheSnapshotRequestRequestTypeDef = TypedDict(
    "ExportServerlessCacheSnapshotRequestRequestTypeDef",
    {
        "ServerlessCacheSnapshotName": str,
        "S3BucketName": str,
    },
)
FailoverGlobalReplicationGroupMessageRequestTypeDef = TypedDict(
    "FailoverGlobalReplicationGroupMessageRequestTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "PrimaryRegion": str,
        "PrimaryReplicationGroupId": str,
    },
)
GlobalNodeGroupTypeDef = TypedDict(
    "GlobalNodeGroupTypeDef",
    {
        "GlobalNodeGroupId": NotRequired[str],
        "Slots": NotRequired[str],
    },
)
GlobalReplicationGroupInfoTypeDef = TypedDict(
    "GlobalReplicationGroupInfoTypeDef",
    {
        "GlobalReplicationGroupId": NotRequired[str],
        "GlobalReplicationGroupMemberRole": NotRequired[str],
    },
)
GlobalReplicationGroupMemberTypeDef = TypedDict(
    "GlobalReplicationGroupMemberTypeDef",
    {
        "ReplicationGroupId": NotRequired[str],
        "ReplicationGroupRegion": NotRequired[str],
        "Role": NotRequired[str],
        "AutomaticFailover": NotRequired[AutomaticFailoverStatusType],
        "Status": NotRequired[str],
    },
)
ListAllowedNodeTypeModificationsMessageRequestTypeDef = TypedDict(
    "ListAllowedNodeTypeModificationsMessageRequestTypeDef",
    {
        "CacheClusterId": NotRequired[str],
        "ReplicationGroupId": NotRequired[str],
    },
)
ListTagsForResourceMessageRequestTypeDef = TypedDict(
    "ListTagsForResourceMessageRequestTypeDef",
    {
        "ResourceName": str,
    },
)
ParameterNameValueTypeDef = TypedDict(
    "ParameterNameValueTypeDef",
    {
        "ParameterName": NotRequired[str],
        "ParameterValue": NotRequired[str],
    },
)
ModifyCacheSubnetGroupMessageRequestTypeDef = TypedDict(
    "ModifyCacheSubnetGroupMessageRequestTypeDef",
    {
        "CacheSubnetGroupName": str,
        "CacheSubnetGroupDescription": NotRequired[str],
        "SubnetIds": NotRequired[Sequence[str]],
    },
)
ModifyGlobalReplicationGroupMessageRequestTypeDef = TypedDict(
    "ModifyGlobalReplicationGroupMessageRequestTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "ApplyImmediately": bool,
        "CacheNodeType": NotRequired[str],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "CacheParameterGroupName": NotRequired[str],
        "GlobalReplicationGroupDescription": NotRequired[str],
        "AutomaticFailoverEnabled": NotRequired[bool],
    },
)
ReshardingConfigurationTypeDef = TypedDict(
    "ReshardingConfigurationTypeDef",
    {
        "NodeGroupId": NotRequired[str],
        "PreferredAvailabilityZones": NotRequired[Sequence[str]],
    },
)
ModifyUserGroupMessageRequestTypeDef = TypedDict(
    "ModifyUserGroupMessageRequestTypeDef",
    {
        "UserGroupId": str,
        "UserIdsToAdd": NotRequired[Sequence[str]],
        "UserIdsToRemove": NotRequired[Sequence[str]],
    },
)
NodeGroupConfigurationOutputTypeDef = TypedDict(
    "NodeGroupConfigurationOutputTypeDef",
    {
        "NodeGroupId": NotRequired[str],
        "Slots": NotRequired[str],
        "ReplicaCount": NotRequired[int],
        "PrimaryAvailabilityZone": NotRequired[str],
        "ReplicaAvailabilityZones": NotRequired[List[str]],
        "PrimaryOutpostArn": NotRequired[str],
        "ReplicaOutpostArns": NotRequired[List[str]],
    },
)
NodeGroupConfigurationTypeDef = TypedDict(
    "NodeGroupConfigurationTypeDef",
    {
        "NodeGroupId": NotRequired[str],
        "Slots": NotRequired[str],
        "ReplicaCount": NotRequired[int],
        "PrimaryAvailabilityZone": NotRequired[str],
        "ReplicaAvailabilityZones": NotRequired[Sequence[str]],
        "PrimaryOutpostArn": NotRequired[str],
        "ReplicaOutpostArns": NotRequired[Sequence[str]],
    },
)
NodeGroupMemberUpdateStatusTypeDef = TypedDict(
    "NodeGroupMemberUpdateStatusTypeDef",
    {
        "CacheClusterId": NotRequired[str],
        "CacheNodeId": NotRequired[str],
        "NodeUpdateStatus": NotRequired[NodeUpdateStatusType],
        "NodeDeletionDate": NotRequired[datetime],
        "NodeUpdateStartDate": NotRequired[datetime],
        "NodeUpdateEndDate": NotRequired[datetime],
        "NodeUpdateInitiatedBy": NotRequired[NodeUpdateInitiatedByType],
        "NodeUpdateInitiatedDate": NotRequired[datetime],
        "NodeUpdateStatusModifiedDate": NotRequired[datetime],
    },
)
ProcessedUpdateActionTypeDef = TypedDict(
    "ProcessedUpdateActionTypeDef",
    {
        "ReplicationGroupId": NotRequired[str],
        "CacheClusterId": NotRequired[str],
        "ServiceUpdateName": NotRequired[str],
        "UpdateActionStatus": NotRequired[UpdateActionStatusType],
    },
)
RebalanceSlotsInGlobalReplicationGroupMessageRequestTypeDef = TypedDict(
    "RebalanceSlotsInGlobalReplicationGroupMessageRequestTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "ApplyImmediately": bool,
    },
)
RebootCacheClusterMessageRequestTypeDef = TypedDict(
    "RebootCacheClusterMessageRequestTypeDef",
    {
        "CacheClusterId": str,
        "CacheNodeIdsToReboot": Sequence[str],
    },
)
RecurringChargeTypeDef = TypedDict(
    "RecurringChargeTypeDef",
    {
        "RecurringChargeAmount": NotRequired[float],
        "RecurringChargeFrequency": NotRequired[str],
    },
)
RemoveTagsFromResourceMessageRequestTypeDef = TypedDict(
    "RemoveTagsFromResourceMessageRequestTypeDef",
    {
        "ResourceName": str,
        "TagKeys": Sequence[str],
    },
)
UserGroupsUpdateStatusTypeDef = TypedDict(
    "UserGroupsUpdateStatusTypeDef",
    {
        "UserGroupIdsToAdd": NotRequired[List[str]],
        "UserGroupIdsToRemove": NotRequired[List[str]],
    },
)
SlotMigrationTypeDef = TypedDict(
    "SlotMigrationTypeDef",
    {
        "ProgressPercentage": NotRequired[float],
    },
)
RevokeCacheSecurityGroupIngressMessageRequestTypeDef = TypedDict(
    "RevokeCacheSecurityGroupIngressMessageRequestTypeDef",
    {
        "CacheSecurityGroupName": str,
        "EC2SecurityGroupName": str,
        "EC2SecurityGroupOwnerId": str,
    },
)
ServerlessCacheConfigurationTypeDef = TypedDict(
    "ServerlessCacheConfigurationTypeDef",
    {
        "ServerlessCacheName": NotRequired[str],
        "Engine": NotRequired[str],
        "MajorEngineVersion": NotRequired[str],
    },
)
ServiceUpdateTypeDef = TypedDict(
    "ServiceUpdateTypeDef",
    {
        "ServiceUpdateName": NotRequired[str],
        "ServiceUpdateReleaseDate": NotRequired[datetime],
        "ServiceUpdateEndDate": NotRequired[datetime],
        "ServiceUpdateSeverity": NotRequired[ServiceUpdateSeverityType],
        "ServiceUpdateRecommendedApplyByDate": NotRequired[datetime],
        "ServiceUpdateStatus": NotRequired[ServiceUpdateStatusType],
        "ServiceUpdateDescription": NotRequired[str],
        "ServiceUpdateType": NotRequired[Literal["security-update"]],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "AutoUpdateAfterRecommendedApplyByDate": NotRequired[bool],
        "EstimatedUpdateTime": NotRequired[str],
    },
)
SubnetOutpostTypeDef = TypedDict(
    "SubnetOutpostTypeDef",
    {
        "SubnetOutpostArn": NotRequired[str],
    },
)
TestFailoverMessageRequestTypeDef = TypedDict(
    "TestFailoverMessageRequestTypeDef",
    {
        "ReplicationGroupId": str,
        "NodeGroupId": str,
    },
)
UnprocessedUpdateActionTypeDef = TypedDict(
    "UnprocessedUpdateActionTypeDef",
    {
        "ReplicationGroupId": NotRequired[str],
        "CacheClusterId": NotRequired[str],
        "ServiceUpdateName": NotRequired[str],
        "ErrorType": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)
UserGroupPendingChangesTypeDef = TypedDict(
    "UserGroupPendingChangesTypeDef",
    {
        "UserIdsToRemove": NotRequired[List[str]],
        "UserIdsToAdd": NotRequired[List[str]],
    },
)
AddTagsToResourceMessageRequestTypeDef = TypedDict(
    "AddTagsToResourceMessageRequestTypeDef",
    {
        "ResourceName": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CopyServerlessCacheSnapshotRequestRequestTypeDef = TypedDict(
    "CopyServerlessCacheSnapshotRequestRequestTypeDef",
    {
        "SourceServerlessCacheSnapshotName": str,
        "TargetServerlessCacheSnapshotName": str,
        "KmsKeyId": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CopySnapshotMessageRequestTypeDef = TypedDict(
    "CopySnapshotMessageRequestTypeDef",
    {
        "SourceSnapshotName": str,
        "TargetSnapshotName": str,
        "TargetBucket": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateCacheParameterGroupMessageRequestTypeDef = TypedDict(
    "CreateCacheParameterGroupMessageRequestTypeDef",
    {
        "CacheParameterGroupName": str,
        "CacheParameterGroupFamily": str,
        "Description": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateCacheSecurityGroupMessageRequestTypeDef = TypedDict(
    "CreateCacheSecurityGroupMessageRequestTypeDef",
    {
        "CacheSecurityGroupName": str,
        "Description": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateCacheSubnetGroupMessageRequestTypeDef = TypedDict(
    "CreateCacheSubnetGroupMessageRequestTypeDef",
    {
        "CacheSubnetGroupName": str,
        "CacheSubnetGroupDescription": str,
        "SubnetIds": Sequence[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateServerlessCacheSnapshotRequestRequestTypeDef = TypedDict(
    "CreateServerlessCacheSnapshotRequestRequestTypeDef",
    {
        "ServerlessCacheSnapshotName": str,
        "ServerlessCacheName": str,
        "KmsKeyId": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateSnapshotMessageRequestTypeDef = TypedDict(
    "CreateSnapshotMessageRequestTypeDef",
    {
        "SnapshotName": str,
        "ReplicationGroupId": NotRequired[str],
        "CacheClusterId": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateUserGroupMessageRequestTypeDef = TypedDict(
    "CreateUserGroupMessageRequestTypeDef",
    {
        "UserGroupId": str,
        "Engine": str,
        "UserIds": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
PurchaseReservedCacheNodesOfferingMessageRequestTypeDef = TypedDict(
    "PurchaseReservedCacheNodesOfferingMessageRequestTypeDef",
    {
        "ReservedCacheNodesOfferingId": str,
        "ReservedCacheNodeId": NotRequired[str],
        "CacheNodeCount": NotRequired[int],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
AllowedNodeTypeModificationsMessageTypeDef = TypedDict(
    "AllowedNodeTypeModificationsMessageTypeDef",
    {
        "ScaleUpModifications": List[str],
        "ScaleDownModifications": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CacheParameterGroupNameMessageTypeDef = TypedDict(
    "CacheParameterGroupNameMessageTypeDef",
    {
        "CacheParameterGroupName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagListMessageTypeDef = TypedDict(
    "TagListMessageTypeDef",
    {
        "TagList": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateUserMessageRequestTypeDef = TypedDict(
    "CreateUserMessageRequestTypeDef",
    {
        "UserId": str,
        "UserName": str,
        "Engine": str,
        "AccessString": str,
        "Passwords": NotRequired[Sequence[str]],
        "NoPasswordRequired": NotRequired[bool],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "AuthenticationMode": NotRequired[AuthenticationModeTypeDef],
    },
)
ModifyUserMessageRequestTypeDef = TypedDict(
    "ModifyUserMessageRequestTypeDef",
    {
        "UserId": str,
        "AccessString": NotRequired[str],
        "AppendAccessString": NotRequired[str],
        "Passwords": NotRequired[Sequence[str]],
        "NoPasswordRequired": NotRequired[bool],
        "AuthenticationMode": NotRequired[AuthenticationModeTypeDef],
    },
)
UserResponseTypeDef = TypedDict(
    "UserResponseTypeDef",
    {
        "UserId": str,
        "UserName": str,
        "Status": str,
        "Engine": str,
        "MinimumEngineVersion": str,
        "AccessString": str,
        "UserGroupIds": List[str],
        "Authentication": AuthenticationTypeDef,
        "ARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "UserId": NotRequired[str],
        "UserName": NotRequired[str],
        "Status": NotRequired[str],
        "Engine": NotRequired[str],
        "MinimumEngineVersion": NotRequired[str],
        "AccessString": NotRequired[str],
        "UserGroupIds": NotRequired[List[str]],
        "Authentication": NotRequired[AuthenticationTypeDef],
        "ARN": NotRequired[str],
    },
)
CacheNodeTypeDef = TypedDict(
    "CacheNodeTypeDef",
    {
        "CacheNodeId": NotRequired[str],
        "CacheNodeStatus": NotRequired[str],
        "CacheNodeCreateTime": NotRequired[datetime],
        "Endpoint": NotRequired[EndpointTypeDef],
        "ParameterGroupStatus": NotRequired[str],
        "SourceCacheNodeId": NotRequired[str],
        "CustomerAvailabilityZone": NotRequired[str],
        "CustomerOutpostArn": NotRequired[str],
    },
)
NodeGroupMemberTypeDef = TypedDict(
    "NodeGroupMemberTypeDef",
    {
        "CacheClusterId": NotRequired[str],
        "CacheNodeId": NotRequired[str],
        "ReadEndpoint": NotRequired[EndpointTypeDef],
        "PreferredAvailabilityZone": NotRequired[str],
        "PreferredOutpostArn": NotRequired[str],
        "CurrentRole": NotRequired[str],
    },
)
CacheEngineVersionMessageTypeDef = TypedDict(
    "CacheEngineVersionMessageTypeDef",
    {
        "Marker": str,
        "CacheEngineVersions": List[CacheEngineVersionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CacheNodeTypeSpecificParameterTypeDef = TypedDict(
    "CacheNodeTypeSpecificParameterTypeDef",
    {
        "ParameterName": NotRequired[str],
        "Description": NotRequired[str],
        "Source": NotRequired[str],
        "DataType": NotRequired[str],
        "AllowedValues": NotRequired[str],
        "IsModifiable": NotRequired[bool],
        "MinimumEngineVersion": NotRequired[str],
        "CacheNodeTypeSpecificValues": NotRequired[List[CacheNodeTypeSpecificValueTypeDef]],
        "ChangeType": NotRequired[ChangeTypeType],
    },
)
CacheParameterGroupsMessageTypeDef = TypedDict(
    "CacheParameterGroupsMessageTypeDef",
    {
        "Marker": str,
        "CacheParameterGroups": List[CacheParameterGroupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCacheParameterGroupResultTypeDef = TypedDict(
    "CreateCacheParameterGroupResultTypeDef",
    {
        "CacheParameterGroup": CacheParameterGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CacheSecurityGroupTypeDef = TypedDict(
    "CacheSecurityGroupTypeDef",
    {
        "OwnerId": NotRequired[str],
        "CacheSecurityGroupName": NotRequired[str],
        "Description": NotRequired[str],
        "EC2SecurityGroups": NotRequired[List[EC2SecurityGroupTypeDef]],
        "ARN": NotRequired[str],
    },
)
CacheUsageLimitsTypeDef = TypedDict(
    "CacheUsageLimitsTypeDef",
    {
        "DataStorage": NotRequired[DataStorageTypeDef],
        "ECPUPerSecond": NotRequired[ECPUPerSecondTypeDef],
    },
)
DecreaseReplicaCountMessageRequestTypeDef = TypedDict(
    "DecreaseReplicaCountMessageRequestTypeDef",
    {
        "ReplicationGroupId": str,
        "ApplyImmediately": bool,
        "NewReplicaCount": NotRequired[int],
        "ReplicaConfiguration": NotRequired[Sequence[ConfigureShardTypeDef]],
        "ReplicasToRemove": NotRequired[Sequence[str]],
    },
)
IncreaseReplicaCountMessageRequestTypeDef = TypedDict(
    "IncreaseReplicaCountMessageRequestTypeDef",
    {
        "ReplicationGroupId": str,
        "ApplyImmediately": bool,
        "NewReplicaCount": NotRequired[int],
        "ReplicaConfiguration": NotRequired[Sequence[ConfigureShardTypeDef]],
    },
)
StartMigrationMessageRequestTypeDef = TypedDict(
    "StartMigrationMessageRequestTypeDef",
    {
        "ReplicationGroupId": str,
        "CustomerNodeEndpointList": Sequence[CustomerNodeEndpointTypeDef],
    },
)
TestMigrationMessageRequestTypeDef = TypedDict(
    "TestMigrationMessageRequestTypeDef",
    {
        "ReplicationGroupId": str,
        "CustomerNodeEndpointList": Sequence[CustomerNodeEndpointTypeDef],
    },
)
DescribeCacheClustersMessageCacheClusterAvailableWaitTypeDef = TypedDict(
    "DescribeCacheClustersMessageCacheClusterAvailableWaitTypeDef",
    {
        "CacheClusterId": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "ShowCacheNodeInfo": NotRequired[bool],
        "ShowCacheClustersNotInReplicationGroups": NotRequired[bool],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeCacheClustersMessageCacheClusterDeletedWaitTypeDef = TypedDict(
    "DescribeCacheClustersMessageCacheClusterDeletedWaitTypeDef",
    {
        "CacheClusterId": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "ShowCacheNodeInfo": NotRequired[bool],
        "ShowCacheClustersNotInReplicationGroups": NotRequired[bool],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeReplicationGroupsMessageReplicationGroupAvailableWaitTypeDef = TypedDict(
    "DescribeReplicationGroupsMessageReplicationGroupAvailableWaitTypeDef",
    {
        "ReplicationGroupId": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeReplicationGroupsMessageReplicationGroupDeletedWaitTypeDef = TypedDict(
    "DescribeReplicationGroupsMessageReplicationGroupDeletedWaitTypeDef",
    {
        "ReplicationGroupId": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeCacheClustersMessageDescribeCacheClustersPaginateTypeDef = TypedDict(
    "DescribeCacheClustersMessageDescribeCacheClustersPaginateTypeDef",
    {
        "CacheClusterId": NotRequired[str],
        "ShowCacheNodeInfo": NotRequired[bool],
        "ShowCacheClustersNotInReplicationGroups": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeCacheEngineVersionsMessageDescribeCacheEngineVersionsPaginateTypeDef = TypedDict(
    "DescribeCacheEngineVersionsMessageDescribeCacheEngineVersionsPaginateTypeDef",
    {
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "CacheParameterGroupFamily": NotRequired[str],
        "DefaultOnly": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeCacheParameterGroupsMessageDescribeCacheParameterGroupsPaginateTypeDef = TypedDict(
    "DescribeCacheParameterGroupsMessageDescribeCacheParameterGroupsPaginateTypeDef",
    {
        "CacheParameterGroupName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeCacheParametersMessageDescribeCacheParametersPaginateTypeDef = TypedDict(
    "DescribeCacheParametersMessageDescribeCacheParametersPaginateTypeDef",
    {
        "CacheParameterGroupName": str,
        "Source": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeCacheSecurityGroupsMessageDescribeCacheSecurityGroupsPaginateTypeDef = TypedDict(
    "DescribeCacheSecurityGroupsMessageDescribeCacheSecurityGroupsPaginateTypeDef",
    {
        "CacheSecurityGroupName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeCacheSubnetGroupsMessageDescribeCacheSubnetGroupsPaginateTypeDef = TypedDict(
    "DescribeCacheSubnetGroupsMessageDescribeCacheSubnetGroupsPaginateTypeDef",
    {
        "CacheSubnetGroupName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEngineDefaultParametersMessageDescribeEngineDefaultParametersPaginateTypeDef = TypedDict(
    "DescribeEngineDefaultParametersMessageDescribeEngineDefaultParametersPaginateTypeDef",
    {
        "CacheParameterGroupFamily": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeGlobalReplicationGroupsMessageDescribeGlobalReplicationGroupsPaginateTypeDef = TypedDict(
    "DescribeGlobalReplicationGroupsMessageDescribeGlobalReplicationGroupsPaginateTypeDef",
    {
        "GlobalReplicationGroupId": NotRequired[str],
        "ShowMemberInfo": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeReplicationGroupsMessageDescribeReplicationGroupsPaginateTypeDef = TypedDict(
    "DescribeReplicationGroupsMessageDescribeReplicationGroupsPaginateTypeDef",
    {
        "ReplicationGroupId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeReservedCacheNodesMessageDescribeReservedCacheNodesPaginateTypeDef = TypedDict(
    "DescribeReservedCacheNodesMessageDescribeReservedCacheNodesPaginateTypeDef",
    {
        "ReservedCacheNodeId": NotRequired[str],
        "ReservedCacheNodesOfferingId": NotRequired[str],
        "CacheNodeType": NotRequired[str],
        "Duration": NotRequired[str],
        "ProductDescription": NotRequired[str],
        "OfferingType": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeReservedCacheNodesOfferingsMessageDescribeReservedCacheNodesOfferingsPaginateTypeDef = TypedDict(
    "DescribeReservedCacheNodesOfferingsMessageDescribeReservedCacheNodesOfferingsPaginateTypeDef",
    {
        "ReservedCacheNodesOfferingId": NotRequired[str],
        "CacheNodeType": NotRequired[str],
        "Duration": NotRequired[str],
        "ProductDescription": NotRequired[str],
        "OfferingType": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeServerlessCacheSnapshotsRequestDescribeServerlessCacheSnapshotsPaginateTypeDef = TypedDict(
    "DescribeServerlessCacheSnapshotsRequestDescribeServerlessCacheSnapshotsPaginateTypeDef",
    {
        "ServerlessCacheName": NotRequired[str],
        "ServerlessCacheSnapshotName": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeServerlessCachesRequestDescribeServerlessCachesPaginateTypeDef = TypedDict(
    "DescribeServerlessCachesRequestDescribeServerlessCachesPaginateTypeDef",
    {
        "ServerlessCacheName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeServiceUpdatesMessageDescribeServiceUpdatesPaginateTypeDef = TypedDict(
    "DescribeServiceUpdatesMessageDescribeServiceUpdatesPaginateTypeDef",
    {
        "ServiceUpdateName": NotRequired[str],
        "ServiceUpdateStatus": NotRequired[Sequence[ServiceUpdateStatusType]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeSnapshotsMessageDescribeSnapshotsPaginateTypeDef = TypedDict(
    "DescribeSnapshotsMessageDescribeSnapshotsPaginateTypeDef",
    {
        "ReplicationGroupId": NotRequired[str],
        "CacheClusterId": NotRequired[str],
        "SnapshotName": NotRequired[str],
        "SnapshotSource": NotRequired[str],
        "ShowNodeGroupConfig": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeUserGroupsMessageDescribeUserGroupsPaginateTypeDef = TypedDict(
    "DescribeUserGroupsMessageDescribeUserGroupsPaginateTypeDef",
    {
        "UserGroupId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEventsMessageDescribeEventsPaginateTypeDef = TypedDict(
    "DescribeEventsMessageDescribeEventsPaginateTypeDef",
    {
        "SourceIdentifier": NotRequired[str],
        "SourceType": NotRequired[SourceTypeType],
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "Duration": NotRequired[int],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEventsMessageRequestTypeDef = TypedDict(
    "DescribeEventsMessageRequestTypeDef",
    {
        "SourceIdentifier": NotRequired[str],
        "SourceType": NotRequired[SourceTypeType],
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "Duration": NotRequired[int],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
TimeRangeFilterTypeDef = TypedDict(
    "TimeRangeFilterTypeDef",
    {
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
    },
)
DescribeUsersMessageDescribeUsersPaginateTypeDef = TypedDict(
    "DescribeUsersMessageDescribeUsersPaginateTypeDef",
    {
        "Engine": NotRequired[str],
        "UserId": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeUsersMessageRequestTypeDef = TypedDict(
    "DescribeUsersMessageRequestTypeDef",
    {
        "Engine": NotRequired[str],
        "UserId": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DestinationDetailsTypeDef = TypedDict(
    "DestinationDetailsTypeDef",
    {
        "CloudWatchLogsDetails": NotRequired[CloudWatchLogsDestinationDetailsTypeDef],
        "KinesisFirehoseDetails": NotRequired[KinesisFirehoseDestinationDetailsTypeDef],
    },
)
EventsMessageTypeDef = TypedDict(
    "EventsMessageTypeDef",
    {
        "Marker": str,
        "Events": List[EventTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GlobalReplicationGroupTypeDef = TypedDict(
    "GlobalReplicationGroupTypeDef",
    {
        "GlobalReplicationGroupId": NotRequired[str],
        "GlobalReplicationGroupDescription": NotRequired[str],
        "Status": NotRequired[str],
        "CacheNodeType": NotRequired[str],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "Members": NotRequired[List[GlobalReplicationGroupMemberTypeDef]],
        "ClusterEnabled": NotRequired[bool],
        "GlobalNodeGroups": NotRequired[List[GlobalNodeGroupTypeDef]],
        "AuthTokenEnabled": NotRequired[bool],
        "TransitEncryptionEnabled": NotRequired[bool],
        "AtRestEncryptionEnabled": NotRequired[bool],
        "ARN": NotRequired[str],
    },
)
ModifyCacheParameterGroupMessageRequestTypeDef = TypedDict(
    "ModifyCacheParameterGroupMessageRequestTypeDef",
    {
        "CacheParameterGroupName": str,
        "ParameterNameValues": Sequence[ParameterNameValueTypeDef],
    },
)
ResetCacheParameterGroupMessageRequestTypeDef = TypedDict(
    "ResetCacheParameterGroupMessageRequestTypeDef",
    {
        "CacheParameterGroupName": str,
        "ResetAllParameters": NotRequired[bool],
        "ParameterNameValues": NotRequired[Sequence[ParameterNameValueTypeDef]],
    },
)
ModifyReplicationGroupShardConfigurationMessageRequestTypeDef = TypedDict(
    "ModifyReplicationGroupShardConfigurationMessageRequestTypeDef",
    {
        "ReplicationGroupId": str,
        "NodeGroupCount": int,
        "ApplyImmediately": bool,
        "ReshardingConfiguration": NotRequired[Sequence[ReshardingConfigurationTypeDef]],
        "NodeGroupsToRemove": NotRequired[Sequence[str]],
        "NodeGroupsToRetain": NotRequired[Sequence[str]],
    },
)
RegionalConfigurationTypeDef = TypedDict(
    "RegionalConfigurationTypeDef",
    {
        "ReplicationGroupId": str,
        "ReplicationGroupRegion": str,
        "ReshardingConfiguration": Sequence[ReshardingConfigurationTypeDef],
    },
)
NodeSnapshotTypeDef = TypedDict(
    "NodeSnapshotTypeDef",
    {
        "CacheClusterId": NotRequired[str],
        "NodeGroupId": NotRequired[str],
        "CacheNodeId": NotRequired[str],
        "NodeGroupConfiguration": NotRequired[NodeGroupConfigurationOutputTypeDef],
        "CacheSize": NotRequired[str],
        "CacheNodeCreateTime": NotRequired[datetime],
        "SnapshotCreateTime": NotRequired[datetime],
    },
)
NodeGroupConfigurationUnionTypeDef = Union[
    NodeGroupConfigurationTypeDef, NodeGroupConfigurationOutputTypeDef
]
NodeGroupUpdateStatusTypeDef = TypedDict(
    "NodeGroupUpdateStatusTypeDef",
    {
        "NodeGroupId": NotRequired[str],
        "NodeGroupMemberUpdateStatus": NotRequired[List[NodeGroupMemberUpdateStatusTypeDef]],
    },
)
ReservedCacheNodeTypeDef = TypedDict(
    "ReservedCacheNodeTypeDef",
    {
        "ReservedCacheNodeId": NotRequired[str],
        "ReservedCacheNodesOfferingId": NotRequired[str],
        "CacheNodeType": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "Duration": NotRequired[int],
        "FixedPrice": NotRequired[float],
        "UsagePrice": NotRequired[float],
        "CacheNodeCount": NotRequired[int],
        "ProductDescription": NotRequired[str],
        "OfferingType": NotRequired[str],
        "State": NotRequired[str],
        "RecurringCharges": NotRequired[List[RecurringChargeTypeDef]],
        "ReservationARN": NotRequired[str],
    },
)
ReservedCacheNodesOfferingTypeDef = TypedDict(
    "ReservedCacheNodesOfferingTypeDef",
    {
        "ReservedCacheNodesOfferingId": NotRequired[str],
        "CacheNodeType": NotRequired[str],
        "Duration": NotRequired[int],
        "FixedPrice": NotRequired[float],
        "UsagePrice": NotRequired[float],
        "ProductDescription": NotRequired[str],
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
ServerlessCacheSnapshotTypeDef = TypedDict(
    "ServerlessCacheSnapshotTypeDef",
    {
        "ServerlessCacheSnapshotName": NotRequired[str],
        "ARN": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "Status": NotRequired[str],
        "CreateTime": NotRequired[datetime],
        "ExpiryTime": NotRequired[datetime],
        "BytesUsedForCache": NotRequired[str],
        "ServerlessCacheConfiguration": NotRequired[ServerlessCacheConfigurationTypeDef],
    },
)
ServiceUpdatesMessageTypeDef = TypedDict(
    "ServiceUpdatesMessageTypeDef",
    {
        "Marker": str,
        "ServiceUpdates": List[ServiceUpdateTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SubnetTypeDef = TypedDict(
    "SubnetTypeDef",
    {
        "SubnetIdentifier": NotRequired[str],
        "SubnetAvailabilityZone": NotRequired[AvailabilityZoneTypeDef],
        "SubnetOutpost": NotRequired[SubnetOutpostTypeDef],
        "SupportedNetworkTypes": NotRequired[List[NetworkTypeType]],
    },
)
UpdateActionResultsMessageTypeDef = TypedDict(
    "UpdateActionResultsMessageTypeDef",
    {
        "ProcessedUpdateActions": List[ProcessedUpdateActionTypeDef],
        "UnprocessedUpdateActions": List[UnprocessedUpdateActionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UserGroupResponseTypeDef = TypedDict(
    "UserGroupResponseTypeDef",
    {
        "UserGroupId": str,
        "Status": str,
        "Engine": str,
        "UserIds": List[str],
        "MinimumEngineVersion": str,
        "PendingChanges": UserGroupPendingChangesTypeDef,
        "ReplicationGroups": List[str],
        "ServerlessCaches": List[str],
        "ARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UserGroupTypeDef = TypedDict(
    "UserGroupTypeDef",
    {
        "UserGroupId": NotRequired[str],
        "Status": NotRequired[str],
        "Engine": NotRequired[str],
        "UserIds": NotRequired[List[str]],
        "MinimumEngineVersion": NotRequired[str],
        "PendingChanges": NotRequired[UserGroupPendingChangesTypeDef],
        "ReplicationGroups": NotRequired[List[str]],
        "ServerlessCaches": NotRequired[List[str]],
        "ARN": NotRequired[str],
    },
)
DescribeUsersResultTypeDef = TypedDict(
    "DescribeUsersResultTypeDef",
    {
        "Users": List[UserTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NodeGroupTypeDef = TypedDict(
    "NodeGroupTypeDef",
    {
        "NodeGroupId": NotRequired[str],
        "Status": NotRequired[str],
        "PrimaryEndpoint": NotRequired[EndpointTypeDef],
        "ReaderEndpoint": NotRequired[EndpointTypeDef],
        "Slots": NotRequired[str],
        "NodeGroupMembers": NotRequired[List[NodeGroupMemberTypeDef]],
    },
)
CacheParameterGroupDetailsTypeDef = TypedDict(
    "CacheParameterGroupDetailsTypeDef",
    {
        "Marker": str,
        "Parameters": List[ParameterTypeDef],
        "CacheNodeTypeSpecificParameters": List[CacheNodeTypeSpecificParameterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EngineDefaultsTypeDef = TypedDict(
    "EngineDefaultsTypeDef",
    {
        "CacheParameterGroupFamily": NotRequired[str],
        "Marker": NotRequired[str],
        "Parameters": NotRequired[List[ParameterTypeDef]],
        "CacheNodeTypeSpecificParameters": NotRequired[List[CacheNodeTypeSpecificParameterTypeDef]],
    },
)
AuthorizeCacheSecurityGroupIngressResultTypeDef = TypedDict(
    "AuthorizeCacheSecurityGroupIngressResultTypeDef",
    {
        "CacheSecurityGroup": CacheSecurityGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CacheSecurityGroupMessageTypeDef = TypedDict(
    "CacheSecurityGroupMessageTypeDef",
    {
        "Marker": str,
        "CacheSecurityGroups": List[CacheSecurityGroupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCacheSecurityGroupResultTypeDef = TypedDict(
    "CreateCacheSecurityGroupResultTypeDef",
    {
        "CacheSecurityGroup": CacheSecurityGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RevokeCacheSecurityGroupIngressResultTypeDef = TypedDict(
    "RevokeCacheSecurityGroupIngressResultTypeDef",
    {
        "CacheSecurityGroup": CacheSecurityGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateServerlessCacheRequestRequestTypeDef = TypedDict(
    "CreateServerlessCacheRequestRequestTypeDef",
    {
        "ServerlessCacheName": str,
        "Engine": str,
        "Description": NotRequired[str],
        "MajorEngineVersion": NotRequired[str],
        "CacheUsageLimits": NotRequired[CacheUsageLimitsTypeDef],
        "KmsKeyId": NotRequired[str],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "SnapshotArnsToRestore": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "UserGroupId": NotRequired[str],
        "SubnetIds": NotRequired[Sequence[str]],
        "SnapshotRetentionLimit": NotRequired[int],
        "DailySnapshotTime": NotRequired[str],
    },
)
ModifyServerlessCacheRequestRequestTypeDef = TypedDict(
    "ModifyServerlessCacheRequestRequestTypeDef",
    {
        "ServerlessCacheName": str,
        "Description": NotRequired[str],
        "CacheUsageLimits": NotRequired[CacheUsageLimitsTypeDef],
        "RemoveUserGroup": NotRequired[bool],
        "UserGroupId": NotRequired[str],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "SnapshotRetentionLimit": NotRequired[int],
        "DailySnapshotTime": NotRequired[str],
        "Engine": NotRequired[str],
        "MajorEngineVersion": NotRequired[str],
    },
)
ServerlessCacheTypeDef = TypedDict(
    "ServerlessCacheTypeDef",
    {
        "ServerlessCacheName": NotRequired[str],
        "Description": NotRequired[str],
        "CreateTime": NotRequired[datetime],
        "Status": NotRequired[str],
        "Engine": NotRequired[str],
        "MajorEngineVersion": NotRequired[str],
        "FullEngineVersion": NotRequired[str],
        "CacheUsageLimits": NotRequired[CacheUsageLimitsTypeDef],
        "KmsKeyId": NotRequired[str],
        "SecurityGroupIds": NotRequired[List[str]],
        "Endpoint": NotRequired[EndpointTypeDef],
        "ReaderEndpoint": NotRequired[EndpointTypeDef],
        "ARN": NotRequired[str],
        "UserGroupId": NotRequired[str],
        "SubnetIds": NotRequired[List[str]],
        "SnapshotRetentionLimit": NotRequired[int],
        "DailySnapshotTime": NotRequired[str],
    },
)
DescribeUpdateActionsMessageDescribeUpdateActionsPaginateTypeDef = TypedDict(
    "DescribeUpdateActionsMessageDescribeUpdateActionsPaginateTypeDef",
    {
        "ServiceUpdateName": NotRequired[str],
        "ReplicationGroupIds": NotRequired[Sequence[str]],
        "CacheClusterIds": NotRequired[Sequence[str]],
        "Engine": NotRequired[str],
        "ServiceUpdateStatus": NotRequired[Sequence[ServiceUpdateStatusType]],
        "ServiceUpdateTimeRange": NotRequired[TimeRangeFilterTypeDef],
        "UpdateActionStatus": NotRequired[Sequence[UpdateActionStatusType]],
        "ShowNodeLevelUpdateStatus": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeUpdateActionsMessageRequestTypeDef = TypedDict(
    "DescribeUpdateActionsMessageRequestTypeDef",
    {
        "ServiceUpdateName": NotRequired[str],
        "ReplicationGroupIds": NotRequired[Sequence[str]],
        "CacheClusterIds": NotRequired[Sequence[str]],
        "Engine": NotRequired[str],
        "ServiceUpdateStatus": NotRequired[Sequence[ServiceUpdateStatusType]],
        "ServiceUpdateTimeRange": NotRequired[TimeRangeFilterTypeDef],
        "UpdateActionStatus": NotRequired[Sequence[UpdateActionStatusType]],
        "ShowNodeLevelUpdateStatus": NotRequired[bool],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
LogDeliveryConfigurationRequestTypeDef = TypedDict(
    "LogDeliveryConfigurationRequestTypeDef",
    {
        "LogType": NotRequired[LogTypeType],
        "DestinationType": NotRequired[DestinationTypeType],
        "DestinationDetails": NotRequired[DestinationDetailsTypeDef],
        "LogFormat": NotRequired[LogFormatType],
        "Enabled": NotRequired[bool],
    },
)
LogDeliveryConfigurationTypeDef = TypedDict(
    "LogDeliveryConfigurationTypeDef",
    {
        "LogType": NotRequired[LogTypeType],
        "DestinationType": NotRequired[DestinationTypeType],
        "DestinationDetails": NotRequired[DestinationDetailsTypeDef],
        "LogFormat": NotRequired[LogFormatType],
        "Status": NotRequired[LogDeliveryConfigurationStatusType],
        "Message": NotRequired[str],
    },
)
PendingLogDeliveryConfigurationTypeDef = TypedDict(
    "PendingLogDeliveryConfigurationTypeDef",
    {
        "LogType": NotRequired[LogTypeType],
        "DestinationType": NotRequired[DestinationTypeType],
        "DestinationDetails": NotRequired[DestinationDetailsTypeDef],
        "LogFormat": NotRequired[LogFormatType],
    },
)
CreateGlobalReplicationGroupResultTypeDef = TypedDict(
    "CreateGlobalReplicationGroupResultTypeDef",
    {
        "GlobalReplicationGroup": GlobalReplicationGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DecreaseNodeGroupsInGlobalReplicationGroupResultTypeDef = TypedDict(
    "DecreaseNodeGroupsInGlobalReplicationGroupResultTypeDef",
    {
        "GlobalReplicationGroup": GlobalReplicationGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteGlobalReplicationGroupResultTypeDef = TypedDict(
    "DeleteGlobalReplicationGroupResultTypeDef",
    {
        "GlobalReplicationGroup": GlobalReplicationGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeGlobalReplicationGroupsResultTypeDef = TypedDict(
    "DescribeGlobalReplicationGroupsResultTypeDef",
    {
        "Marker": str,
        "GlobalReplicationGroups": List[GlobalReplicationGroupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateGlobalReplicationGroupResultTypeDef = TypedDict(
    "DisassociateGlobalReplicationGroupResultTypeDef",
    {
        "GlobalReplicationGroup": GlobalReplicationGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FailoverGlobalReplicationGroupResultTypeDef = TypedDict(
    "FailoverGlobalReplicationGroupResultTypeDef",
    {
        "GlobalReplicationGroup": GlobalReplicationGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IncreaseNodeGroupsInGlobalReplicationGroupResultTypeDef = TypedDict(
    "IncreaseNodeGroupsInGlobalReplicationGroupResultTypeDef",
    {
        "GlobalReplicationGroup": GlobalReplicationGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyGlobalReplicationGroupResultTypeDef = TypedDict(
    "ModifyGlobalReplicationGroupResultTypeDef",
    {
        "GlobalReplicationGroup": GlobalReplicationGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RebalanceSlotsInGlobalReplicationGroupResultTypeDef = TypedDict(
    "RebalanceSlotsInGlobalReplicationGroupResultTypeDef",
    {
        "GlobalReplicationGroup": GlobalReplicationGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IncreaseNodeGroupsInGlobalReplicationGroupMessageRequestTypeDef = TypedDict(
    "IncreaseNodeGroupsInGlobalReplicationGroupMessageRequestTypeDef",
    {
        "GlobalReplicationGroupId": str,
        "NodeGroupCount": int,
        "ApplyImmediately": bool,
        "RegionalConfigurations": NotRequired[Sequence[RegionalConfigurationTypeDef]],
    },
)
SnapshotTypeDef = TypedDict(
    "SnapshotTypeDef",
    {
        "SnapshotName": NotRequired[str],
        "ReplicationGroupId": NotRequired[str],
        "ReplicationGroupDescription": NotRequired[str],
        "CacheClusterId": NotRequired[str],
        "SnapshotStatus": NotRequired[str],
        "SnapshotSource": NotRequired[str],
        "CacheNodeType": NotRequired[str],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "NumCacheNodes": NotRequired[int],
        "PreferredAvailabilityZone": NotRequired[str],
        "PreferredOutpostArn": NotRequired[str],
        "CacheClusterCreateTime": NotRequired[datetime],
        "PreferredMaintenanceWindow": NotRequired[str],
        "TopicArn": NotRequired[str],
        "Port": NotRequired[int],
        "CacheParameterGroupName": NotRequired[str],
        "CacheSubnetGroupName": NotRequired[str],
        "VpcId": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "SnapshotRetentionLimit": NotRequired[int],
        "SnapshotWindow": NotRequired[str],
        "NumNodeGroups": NotRequired[int],
        "AutomaticFailover": NotRequired[AutomaticFailoverStatusType],
        "NodeSnapshots": NotRequired[List[NodeSnapshotTypeDef]],
        "KmsKeyId": NotRequired[str],
        "ARN": NotRequired[str],
        "DataTiering": NotRequired[DataTieringStatusType],
    },
)
UpdateActionTypeDef = TypedDict(
    "UpdateActionTypeDef",
    {
        "ReplicationGroupId": NotRequired[str],
        "CacheClusterId": NotRequired[str],
        "ServiceUpdateName": NotRequired[str],
        "ServiceUpdateReleaseDate": NotRequired[datetime],
        "ServiceUpdateSeverity": NotRequired[ServiceUpdateSeverityType],
        "ServiceUpdateStatus": NotRequired[ServiceUpdateStatusType],
        "ServiceUpdateRecommendedApplyByDate": NotRequired[datetime],
        "ServiceUpdateType": NotRequired[Literal["security-update"]],
        "UpdateActionAvailableDate": NotRequired[datetime],
        "UpdateActionStatus": NotRequired[UpdateActionStatusType],
        "NodesUpdated": NotRequired[str],
        "UpdateActionStatusModifiedDate": NotRequired[datetime],
        "SlaMet": NotRequired[SlaMetType],
        "NodeGroupUpdateStatus": NotRequired[List[NodeGroupUpdateStatusTypeDef]],
        "CacheNodeUpdateStatus": NotRequired[List[CacheNodeUpdateStatusTypeDef]],
        "EstimatedUpdateTime": NotRequired[str],
        "Engine": NotRequired[str],
    },
)
PurchaseReservedCacheNodesOfferingResultTypeDef = TypedDict(
    "PurchaseReservedCacheNodesOfferingResultTypeDef",
    {
        "ReservedCacheNode": ReservedCacheNodeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReservedCacheNodeMessageTypeDef = TypedDict(
    "ReservedCacheNodeMessageTypeDef",
    {
        "Marker": str,
        "ReservedCacheNodes": List[ReservedCacheNodeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReservedCacheNodesOfferingMessageTypeDef = TypedDict(
    "ReservedCacheNodesOfferingMessageTypeDef",
    {
        "Marker": str,
        "ReservedCacheNodesOfferings": List[ReservedCacheNodesOfferingTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CopyServerlessCacheSnapshotResponseTypeDef = TypedDict(
    "CopyServerlessCacheSnapshotResponseTypeDef",
    {
        "ServerlessCacheSnapshot": ServerlessCacheSnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateServerlessCacheSnapshotResponseTypeDef = TypedDict(
    "CreateServerlessCacheSnapshotResponseTypeDef",
    {
        "ServerlessCacheSnapshot": ServerlessCacheSnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteServerlessCacheSnapshotResponseTypeDef = TypedDict(
    "DeleteServerlessCacheSnapshotResponseTypeDef",
    {
        "ServerlessCacheSnapshot": ServerlessCacheSnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeServerlessCacheSnapshotsResponseTypeDef = TypedDict(
    "DescribeServerlessCacheSnapshotsResponseTypeDef",
    {
        "ServerlessCacheSnapshots": List[ServerlessCacheSnapshotTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ExportServerlessCacheSnapshotResponseTypeDef = TypedDict(
    "ExportServerlessCacheSnapshotResponseTypeDef",
    {
        "ServerlessCacheSnapshot": ServerlessCacheSnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CacheSubnetGroupTypeDef = TypedDict(
    "CacheSubnetGroupTypeDef",
    {
        "CacheSubnetGroupName": NotRequired[str],
        "CacheSubnetGroupDescription": NotRequired[str],
        "VpcId": NotRequired[str],
        "Subnets": NotRequired[List[SubnetTypeDef]],
        "ARN": NotRequired[str],
        "SupportedNetworkTypes": NotRequired[List[NetworkTypeType]],
    },
)
DescribeUserGroupsResultTypeDef = TypedDict(
    "DescribeUserGroupsResultTypeDef",
    {
        "UserGroups": List[UserGroupTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEngineDefaultParametersResultTypeDef = TypedDict(
    "DescribeEngineDefaultParametersResultTypeDef",
    {
        "EngineDefaults": EngineDefaultsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateServerlessCacheResponseTypeDef = TypedDict(
    "CreateServerlessCacheResponseTypeDef",
    {
        "ServerlessCache": ServerlessCacheTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteServerlessCacheResponseTypeDef = TypedDict(
    "DeleteServerlessCacheResponseTypeDef",
    {
        "ServerlessCache": ServerlessCacheTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeServerlessCachesResponseTypeDef = TypedDict(
    "DescribeServerlessCachesResponseTypeDef",
    {
        "ServerlessCaches": List[ServerlessCacheTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ModifyServerlessCacheResponseTypeDef = TypedDict(
    "ModifyServerlessCacheResponseTypeDef",
    {
        "ServerlessCache": ServerlessCacheTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCacheClusterMessageRequestTypeDef = TypedDict(
    "CreateCacheClusterMessageRequestTypeDef",
    {
        "CacheClusterId": str,
        "ReplicationGroupId": NotRequired[str],
        "AZMode": NotRequired[AZModeType],
        "PreferredAvailabilityZone": NotRequired[str],
        "PreferredAvailabilityZones": NotRequired[Sequence[str]],
        "NumCacheNodes": NotRequired[int],
        "CacheNodeType": NotRequired[str],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "CacheParameterGroupName": NotRequired[str],
        "CacheSubnetGroupName": NotRequired[str],
        "CacheSecurityGroupNames": NotRequired[Sequence[str]],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "SnapshotArns": NotRequired[Sequence[str]],
        "SnapshotName": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "Port": NotRequired[int],
        "NotificationTopicArn": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "SnapshotRetentionLimit": NotRequired[int],
        "SnapshotWindow": NotRequired[str],
        "AuthToken": NotRequired[str],
        "OutpostMode": NotRequired[OutpostModeType],
        "PreferredOutpostArn": NotRequired[str],
        "PreferredOutpostArns": NotRequired[Sequence[str]],
        "LogDeliveryConfigurations": NotRequired[Sequence[LogDeliveryConfigurationRequestTypeDef]],
        "TransitEncryptionEnabled": NotRequired[bool],
        "NetworkType": NotRequired[NetworkTypeType],
        "IpDiscovery": NotRequired[IpDiscoveryType],
    },
)
CreateReplicationGroupMessageRequestTypeDef = TypedDict(
    "CreateReplicationGroupMessageRequestTypeDef",
    {
        "ReplicationGroupId": str,
        "ReplicationGroupDescription": str,
        "GlobalReplicationGroupId": NotRequired[str],
        "PrimaryClusterId": NotRequired[str],
        "AutomaticFailoverEnabled": NotRequired[bool],
        "MultiAZEnabled": NotRequired[bool],
        "NumCacheClusters": NotRequired[int],
        "PreferredCacheClusterAZs": NotRequired[Sequence[str]],
        "NumNodeGroups": NotRequired[int],
        "ReplicasPerNodeGroup": NotRequired[int],
        "NodeGroupConfiguration": NotRequired[Sequence[NodeGroupConfigurationUnionTypeDef]],
        "CacheNodeType": NotRequired[str],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "CacheParameterGroupName": NotRequired[str],
        "CacheSubnetGroupName": NotRequired[str],
        "CacheSecurityGroupNames": NotRequired[Sequence[str]],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "SnapshotArns": NotRequired[Sequence[str]],
        "SnapshotName": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "Port": NotRequired[int],
        "NotificationTopicArn": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "SnapshotRetentionLimit": NotRequired[int],
        "SnapshotWindow": NotRequired[str],
        "AuthToken": NotRequired[str],
        "TransitEncryptionEnabled": NotRequired[bool],
        "AtRestEncryptionEnabled": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "UserGroupIds": NotRequired[Sequence[str]],
        "LogDeliveryConfigurations": NotRequired[Sequence[LogDeliveryConfigurationRequestTypeDef]],
        "DataTieringEnabled": NotRequired[bool],
        "NetworkType": NotRequired[NetworkTypeType],
        "IpDiscovery": NotRequired[IpDiscoveryType],
        "TransitEncryptionMode": NotRequired[TransitEncryptionModeType],
        "ClusterMode": NotRequired[ClusterModeType],
        "ServerlessCacheSnapshotName": NotRequired[str],
    },
)
ModifyCacheClusterMessageRequestTypeDef = TypedDict(
    "ModifyCacheClusterMessageRequestTypeDef",
    {
        "CacheClusterId": str,
        "NumCacheNodes": NotRequired[int],
        "CacheNodeIdsToRemove": NotRequired[Sequence[str]],
        "AZMode": NotRequired[AZModeType],
        "NewAvailabilityZones": NotRequired[Sequence[str]],
        "CacheSecurityGroupNames": NotRequired[Sequence[str]],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "PreferredMaintenanceWindow": NotRequired[str],
        "NotificationTopicArn": NotRequired[str],
        "CacheParameterGroupName": NotRequired[str],
        "NotificationTopicStatus": NotRequired[str],
        "ApplyImmediately": NotRequired[bool],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "SnapshotRetentionLimit": NotRequired[int],
        "SnapshotWindow": NotRequired[str],
        "CacheNodeType": NotRequired[str],
        "AuthToken": NotRequired[str],
        "AuthTokenUpdateStrategy": NotRequired[AuthTokenUpdateStrategyTypeType],
        "LogDeliveryConfigurations": NotRequired[Sequence[LogDeliveryConfigurationRequestTypeDef]],
        "IpDiscovery": NotRequired[IpDiscoveryType],
    },
)
ModifyReplicationGroupMessageRequestTypeDef = TypedDict(
    "ModifyReplicationGroupMessageRequestTypeDef",
    {
        "ReplicationGroupId": str,
        "ReplicationGroupDescription": NotRequired[str],
        "PrimaryClusterId": NotRequired[str],
        "SnapshottingClusterId": NotRequired[str],
        "AutomaticFailoverEnabled": NotRequired[bool],
        "MultiAZEnabled": NotRequired[bool],
        "NodeGroupId": NotRequired[str],
        "CacheSecurityGroupNames": NotRequired[Sequence[str]],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "PreferredMaintenanceWindow": NotRequired[str],
        "NotificationTopicArn": NotRequired[str],
        "CacheParameterGroupName": NotRequired[str],
        "NotificationTopicStatus": NotRequired[str],
        "ApplyImmediately": NotRequired[bool],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "SnapshotRetentionLimit": NotRequired[int],
        "SnapshotWindow": NotRequired[str],
        "CacheNodeType": NotRequired[str],
        "AuthToken": NotRequired[str],
        "AuthTokenUpdateStrategy": NotRequired[AuthTokenUpdateStrategyTypeType],
        "UserGroupIdsToAdd": NotRequired[Sequence[str]],
        "UserGroupIdsToRemove": NotRequired[Sequence[str]],
        "RemoveUserGroups": NotRequired[bool],
        "LogDeliveryConfigurations": NotRequired[Sequence[LogDeliveryConfigurationRequestTypeDef]],
        "IpDiscovery": NotRequired[IpDiscoveryType],
        "TransitEncryptionEnabled": NotRequired[bool],
        "TransitEncryptionMode": NotRequired[TransitEncryptionModeType],
        "ClusterMode": NotRequired[ClusterModeType],
    },
)
PendingModifiedValuesTypeDef = TypedDict(
    "PendingModifiedValuesTypeDef",
    {
        "NumCacheNodes": NotRequired[int],
        "CacheNodeIdsToRemove": NotRequired[List[str]],
        "EngineVersion": NotRequired[str],
        "CacheNodeType": NotRequired[str],
        "AuthTokenStatus": NotRequired[AuthTokenUpdateStatusType],
        "LogDeliveryConfigurations": NotRequired[List[PendingLogDeliveryConfigurationTypeDef]],
        "TransitEncryptionEnabled": NotRequired[bool],
        "TransitEncryptionMode": NotRequired[TransitEncryptionModeType],
    },
)
ReplicationGroupPendingModifiedValuesTypeDef = TypedDict(
    "ReplicationGroupPendingModifiedValuesTypeDef",
    {
        "PrimaryClusterId": NotRequired[str],
        "AutomaticFailoverStatus": NotRequired[PendingAutomaticFailoverStatusType],
        "Resharding": NotRequired[ReshardingStatusTypeDef],
        "AuthTokenStatus": NotRequired[AuthTokenUpdateStatusType],
        "UserGroups": NotRequired[UserGroupsUpdateStatusTypeDef],
        "LogDeliveryConfigurations": NotRequired[List[PendingLogDeliveryConfigurationTypeDef]],
        "TransitEncryptionEnabled": NotRequired[bool],
        "TransitEncryptionMode": NotRequired[TransitEncryptionModeType],
        "ClusterMode": NotRequired[ClusterModeType],
    },
)
CopySnapshotResultTypeDef = TypedDict(
    "CopySnapshotResultTypeDef",
    {
        "Snapshot": SnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSnapshotResultTypeDef = TypedDict(
    "CreateSnapshotResultTypeDef",
    {
        "Snapshot": SnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteSnapshotResultTypeDef = TypedDict(
    "DeleteSnapshotResultTypeDef",
    {
        "Snapshot": SnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSnapshotsListMessageTypeDef = TypedDict(
    "DescribeSnapshotsListMessageTypeDef",
    {
        "Marker": str,
        "Snapshots": List[SnapshotTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateActionsMessageTypeDef = TypedDict(
    "UpdateActionsMessageTypeDef",
    {
        "Marker": str,
        "UpdateActions": List[UpdateActionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CacheSubnetGroupMessageTypeDef = TypedDict(
    "CacheSubnetGroupMessageTypeDef",
    {
        "Marker": str,
        "CacheSubnetGroups": List[CacheSubnetGroupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCacheSubnetGroupResultTypeDef = TypedDict(
    "CreateCacheSubnetGroupResultTypeDef",
    {
        "CacheSubnetGroup": CacheSubnetGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyCacheSubnetGroupResultTypeDef = TypedDict(
    "ModifyCacheSubnetGroupResultTypeDef",
    {
        "CacheSubnetGroup": CacheSubnetGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CacheClusterTypeDef = TypedDict(
    "CacheClusterTypeDef",
    {
        "CacheClusterId": NotRequired[str],
        "ConfigurationEndpoint": NotRequired[EndpointTypeDef],
        "ClientDownloadLandingPage": NotRequired[str],
        "CacheNodeType": NotRequired[str],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "CacheClusterStatus": NotRequired[str],
        "NumCacheNodes": NotRequired[int],
        "PreferredAvailabilityZone": NotRequired[str],
        "PreferredOutpostArn": NotRequired[str],
        "CacheClusterCreateTime": NotRequired[datetime],
        "PreferredMaintenanceWindow": NotRequired[str],
        "PendingModifiedValues": NotRequired[PendingModifiedValuesTypeDef],
        "NotificationConfiguration": NotRequired[NotificationConfigurationTypeDef],
        "CacheSecurityGroups": NotRequired[List[CacheSecurityGroupMembershipTypeDef]],
        "CacheParameterGroup": NotRequired[CacheParameterGroupStatusTypeDef],
        "CacheSubnetGroupName": NotRequired[str],
        "CacheNodes": NotRequired[List[CacheNodeTypeDef]],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "SecurityGroups": NotRequired[List[SecurityGroupMembershipTypeDef]],
        "ReplicationGroupId": NotRequired[str],
        "SnapshotRetentionLimit": NotRequired[int],
        "SnapshotWindow": NotRequired[str],
        "AuthTokenEnabled": NotRequired[bool],
        "AuthTokenLastModifiedDate": NotRequired[datetime],
        "TransitEncryptionEnabled": NotRequired[bool],
        "AtRestEncryptionEnabled": NotRequired[bool],
        "ARN": NotRequired[str],
        "ReplicationGroupLogDeliveryEnabled": NotRequired[bool],
        "LogDeliveryConfigurations": NotRequired[List[LogDeliveryConfigurationTypeDef]],
        "NetworkType": NotRequired[NetworkTypeType],
        "IpDiscovery": NotRequired[IpDiscoveryType],
        "TransitEncryptionMode": NotRequired[TransitEncryptionModeType],
    },
)
ReplicationGroupTypeDef = TypedDict(
    "ReplicationGroupTypeDef",
    {
        "ReplicationGroupId": NotRequired[str],
        "Description": NotRequired[str],
        "GlobalReplicationGroupInfo": NotRequired[GlobalReplicationGroupInfoTypeDef],
        "Status": NotRequired[str],
        "PendingModifiedValues": NotRequired[ReplicationGroupPendingModifiedValuesTypeDef],
        "MemberClusters": NotRequired[List[str]],
        "NodeGroups": NotRequired[List[NodeGroupTypeDef]],
        "SnapshottingClusterId": NotRequired[str],
        "AutomaticFailover": NotRequired[AutomaticFailoverStatusType],
        "MultiAZ": NotRequired[MultiAZStatusType],
        "ConfigurationEndpoint": NotRequired[EndpointTypeDef],
        "SnapshotRetentionLimit": NotRequired[int],
        "SnapshotWindow": NotRequired[str],
        "ClusterEnabled": NotRequired[bool],
        "CacheNodeType": NotRequired[str],
        "AuthTokenEnabled": NotRequired[bool],
        "AuthTokenLastModifiedDate": NotRequired[datetime],
        "TransitEncryptionEnabled": NotRequired[bool],
        "AtRestEncryptionEnabled": NotRequired[bool],
        "MemberClustersOutpostArns": NotRequired[List[str]],
        "KmsKeyId": NotRequired[str],
        "ARN": NotRequired[str],
        "UserGroupIds": NotRequired[List[str]],
        "LogDeliveryConfigurations": NotRequired[List[LogDeliveryConfigurationTypeDef]],
        "ReplicationGroupCreateTime": NotRequired[datetime],
        "DataTiering": NotRequired[DataTieringStatusType],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "NetworkType": NotRequired[NetworkTypeType],
        "IpDiscovery": NotRequired[IpDiscoveryType],
        "TransitEncryptionMode": NotRequired[TransitEncryptionModeType],
        "ClusterMode": NotRequired[ClusterModeType],
        "Engine": NotRequired[str],
    },
)
CacheClusterMessageTypeDef = TypedDict(
    "CacheClusterMessageTypeDef",
    {
        "Marker": str,
        "CacheClusters": List[CacheClusterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCacheClusterResultTypeDef = TypedDict(
    "CreateCacheClusterResultTypeDef",
    {
        "CacheCluster": CacheClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteCacheClusterResultTypeDef = TypedDict(
    "DeleteCacheClusterResultTypeDef",
    {
        "CacheCluster": CacheClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyCacheClusterResultTypeDef = TypedDict(
    "ModifyCacheClusterResultTypeDef",
    {
        "CacheCluster": CacheClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RebootCacheClusterResultTypeDef = TypedDict(
    "RebootCacheClusterResultTypeDef",
    {
        "CacheCluster": CacheClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CompleteMigrationResponseTypeDef = TypedDict(
    "CompleteMigrationResponseTypeDef",
    {
        "ReplicationGroup": ReplicationGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateReplicationGroupResultTypeDef = TypedDict(
    "CreateReplicationGroupResultTypeDef",
    {
        "ReplicationGroup": ReplicationGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DecreaseReplicaCountResultTypeDef = TypedDict(
    "DecreaseReplicaCountResultTypeDef",
    {
        "ReplicationGroup": ReplicationGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteReplicationGroupResultTypeDef = TypedDict(
    "DeleteReplicationGroupResultTypeDef",
    {
        "ReplicationGroup": ReplicationGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IncreaseReplicaCountResultTypeDef = TypedDict(
    "IncreaseReplicaCountResultTypeDef",
    {
        "ReplicationGroup": ReplicationGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyReplicationGroupResultTypeDef = TypedDict(
    "ModifyReplicationGroupResultTypeDef",
    {
        "ReplicationGroup": ReplicationGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyReplicationGroupShardConfigurationResultTypeDef = TypedDict(
    "ModifyReplicationGroupShardConfigurationResultTypeDef",
    {
        "ReplicationGroup": ReplicationGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReplicationGroupMessageTypeDef = TypedDict(
    "ReplicationGroupMessageTypeDef",
    {
        "Marker": str,
        "ReplicationGroups": List[ReplicationGroupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartMigrationResponseTypeDef = TypedDict(
    "StartMigrationResponseTypeDef",
    {
        "ReplicationGroup": ReplicationGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TestFailoverResultTypeDef = TypedDict(
    "TestFailoverResultTypeDef",
    {
        "ReplicationGroup": ReplicationGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TestMigrationResponseTypeDef = TypedDict(
    "TestMigrationResponseTypeDef",
    {
        "ReplicationGroup": ReplicationGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
