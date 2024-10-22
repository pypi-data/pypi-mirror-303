"""
Type annotations for docdb service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb/type_defs/)

Usage::

    ```python
    from mypy_boto3_docdb.type_defs import AddSourceIdentifierToSubscriptionMessageRequestTypeDef

    data: AddSourceIdentifierToSubscriptionMessageRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import ApplyMethodType, SourceTypeType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AddSourceIdentifierToSubscriptionMessageRequestTypeDef",
    "EventSubscriptionTypeDef",
    "ResponseMetadataTypeDef",
    "TagTypeDef",
    "ApplyPendingMaintenanceActionMessageRequestTypeDef",
    "AvailabilityZoneTypeDef",
    "CertificateDetailsTypeDef",
    "CertificateTypeDef",
    "CloudwatchLogsExportConfigurationTypeDef",
    "DBClusterParameterGroupTypeDef",
    "DBClusterSnapshotTypeDef",
    "CreateGlobalClusterMessageRequestTypeDef",
    "DBClusterMemberTypeDef",
    "ParameterTypeDef",
    "DBClusterRoleTypeDef",
    "DBClusterSnapshotAttributeTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "UpgradeTargetTypeDef",
    "DBInstanceStatusInfoTypeDef",
    "EndpointTypeDef",
    "DeleteDBClusterMessageRequestTypeDef",
    "DeleteDBClusterParameterGroupMessageRequestTypeDef",
    "DeleteDBClusterSnapshotMessageRequestTypeDef",
    "DeleteDBInstanceMessageRequestTypeDef",
    "DeleteDBSubnetGroupMessageRequestTypeDef",
    "DeleteEventSubscriptionMessageRequestTypeDef",
    "DeleteGlobalClusterMessageRequestTypeDef",
    "FilterTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeDBClusterSnapshotAttributesMessageRequestTypeDef",
    "WaiterConfigTypeDef",
    "TimestampTypeDef",
    "EventCategoriesMapTypeDef",
    "EventTypeDef",
    "FailoverDBClusterMessageRequestTypeDef",
    "FailoverGlobalClusterMessageRequestTypeDef",
    "GlobalClusterMemberTypeDef",
    "ModifyDBClusterSnapshotAttributeMessageRequestTypeDef",
    "ModifyDBInstanceMessageRequestTypeDef",
    "ModifyDBSubnetGroupMessageRequestTypeDef",
    "ModifyEventSubscriptionMessageRequestTypeDef",
    "ModifyGlobalClusterMessageRequestTypeDef",
    "PendingCloudwatchLogsExportsTypeDef",
    "PendingMaintenanceActionTypeDef",
    "RebootDBInstanceMessageRequestTypeDef",
    "RemoveFromGlobalClusterMessageRequestTypeDef",
    "RemoveSourceIdentifierFromSubscriptionMessageRequestTypeDef",
    "RemoveTagsFromResourceMessageRequestTypeDef",
    "StartDBClusterMessageRequestTypeDef",
    "StopDBClusterMessageRequestTypeDef",
    "SwitchoverGlobalClusterMessageRequestTypeDef",
    "AddSourceIdentifierToSubscriptionResultTypeDef",
    "CreateEventSubscriptionResultTypeDef",
    "DBClusterParameterGroupNameMessageTypeDef",
    "DeleteEventSubscriptionResultTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EventSubscriptionsMessageTypeDef",
    "ModifyEventSubscriptionResultTypeDef",
    "RemoveSourceIdentifierFromSubscriptionResultTypeDef",
    "AddTagsToResourceMessageRequestTypeDef",
    "CopyDBClusterParameterGroupMessageRequestTypeDef",
    "CopyDBClusterSnapshotMessageRequestTypeDef",
    "CreateDBClusterMessageRequestTypeDef",
    "CreateDBClusterParameterGroupMessageRequestTypeDef",
    "CreateDBClusterSnapshotMessageRequestTypeDef",
    "CreateDBInstanceMessageRequestTypeDef",
    "CreateDBSubnetGroupMessageRequestTypeDef",
    "CreateEventSubscriptionMessageRequestTypeDef",
    "RestoreDBClusterFromSnapshotMessageRequestTypeDef",
    "TagListMessageTypeDef",
    "OrderableDBInstanceOptionTypeDef",
    "SubnetTypeDef",
    "CertificateMessageTypeDef",
    "ModifyDBClusterMessageRequestTypeDef",
    "CopyDBClusterParameterGroupResultTypeDef",
    "CreateDBClusterParameterGroupResultTypeDef",
    "DBClusterParameterGroupsMessageTypeDef",
    "CopyDBClusterSnapshotResultTypeDef",
    "CreateDBClusterSnapshotResultTypeDef",
    "DBClusterSnapshotMessageTypeDef",
    "DeleteDBClusterSnapshotResultTypeDef",
    "DBClusterParameterGroupDetailsTypeDef",
    "EngineDefaultsTypeDef",
    "ModifyDBClusterParameterGroupMessageRequestTypeDef",
    "ResetDBClusterParameterGroupMessageRequestTypeDef",
    "DBClusterSnapshotAttributesResultTypeDef",
    "DBClusterTypeDef",
    "DBEngineVersionTypeDef",
    "DescribeCertificatesMessageRequestTypeDef",
    "DescribeDBClusterParameterGroupsMessageRequestTypeDef",
    "DescribeDBClusterParametersMessageRequestTypeDef",
    "DescribeDBClusterSnapshotsMessageRequestTypeDef",
    "DescribeDBClustersMessageRequestTypeDef",
    "DescribeDBEngineVersionsMessageRequestTypeDef",
    "DescribeDBInstancesMessageRequestTypeDef",
    "DescribeDBSubnetGroupsMessageRequestTypeDef",
    "DescribeEngineDefaultClusterParametersMessageRequestTypeDef",
    "DescribeEventCategoriesMessageRequestTypeDef",
    "DescribeEventSubscriptionsMessageRequestTypeDef",
    "DescribeGlobalClustersMessageRequestTypeDef",
    "DescribeOrderableDBInstanceOptionsMessageRequestTypeDef",
    "DescribePendingMaintenanceActionsMessageRequestTypeDef",
    "ListTagsForResourceMessageRequestTypeDef",
    "DescribeCertificatesMessageDescribeCertificatesPaginateTypeDef",
    "DescribeDBClusterParameterGroupsMessageDescribeDBClusterParameterGroupsPaginateTypeDef",
    "DescribeDBClusterParametersMessageDescribeDBClusterParametersPaginateTypeDef",
    "DescribeDBClusterSnapshotsMessageDescribeDBClusterSnapshotsPaginateTypeDef",
    "DescribeDBClustersMessageDescribeDBClustersPaginateTypeDef",
    "DescribeDBEngineVersionsMessageDescribeDBEngineVersionsPaginateTypeDef",
    "DescribeDBInstancesMessageDescribeDBInstancesPaginateTypeDef",
    "DescribeDBSubnetGroupsMessageDescribeDBSubnetGroupsPaginateTypeDef",
    "DescribeEventSubscriptionsMessageDescribeEventSubscriptionsPaginateTypeDef",
    "DescribeGlobalClustersMessageDescribeGlobalClustersPaginateTypeDef",
    "DescribeOrderableDBInstanceOptionsMessageDescribeOrderableDBInstanceOptionsPaginateTypeDef",
    "DescribePendingMaintenanceActionsMessageDescribePendingMaintenanceActionsPaginateTypeDef",
    "DescribeDBInstancesMessageDBInstanceAvailableWaitTypeDef",
    "DescribeDBInstancesMessageDBInstanceDeletedWaitTypeDef",
    "DescribeEventsMessageDescribeEventsPaginateTypeDef",
    "DescribeEventsMessageRequestTypeDef",
    "RestoreDBClusterToPointInTimeMessageRequestTypeDef",
    "EventCategoriesMessageTypeDef",
    "EventsMessageTypeDef",
    "GlobalClusterTypeDef",
    "PendingModifiedValuesTypeDef",
    "ResourcePendingMaintenanceActionsTypeDef",
    "OrderableDBInstanceOptionsMessageTypeDef",
    "DBSubnetGroupTypeDef",
    "DescribeEngineDefaultClusterParametersResultTypeDef",
    "DescribeDBClusterSnapshotAttributesResultTypeDef",
    "ModifyDBClusterSnapshotAttributeResultTypeDef",
    "CreateDBClusterResultTypeDef",
    "DBClusterMessageTypeDef",
    "DeleteDBClusterResultTypeDef",
    "FailoverDBClusterResultTypeDef",
    "ModifyDBClusterResultTypeDef",
    "RestoreDBClusterFromSnapshotResultTypeDef",
    "RestoreDBClusterToPointInTimeResultTypeDef",
    "StartDBClusterResultTypeDef",
    "StopDBClusterResultTypeDef",
    "DBEngineVersionMessageTypeDef",
    "CreateGlobalClusterResultTypeDef",
    "DeleteGlobalClusterResultTypeDef",
    "FailoverGlobalClusterResultTypeDef",
    "GlobalClustersMessageTypeDef",
    "ModifyGlobalClusterResultTypeDef",
    "RemoveFromGlobalClusterResultTypeDef",
    "SwitchoverGlobalClusterResultTypeDef",
    "ApplyPendingMaintenanceActionResultTypeDef",
    "PendingMaintenanceActionsMessageTypeDef",
    "CreateDBSubnetGroupResultTypeDef",
    "DBInstanceTypeDef",
    "DBSubnetGroupMessageTypeDef",
    "ModifyDBSubnetGroupResultTypeDef",
    "CreateDBInstanceResultTypeDef",
    "DBInstanceMessageTypeDef",
    "DeleteDBInstanceResultTypeDef",
    "ModifyDBInstanceResultTypeDef",
    "RebootDBInstanceResultTypeDef",
)

AddSourceIdentifierToSubscriptionMessageRequestTypeDef = TypedDict(
    "AddSourceIdentifierToSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
        "SourceIdentifier": str,
    },
)
EventSubscriptionTypeDef = TypedDict(
    "EventSubscriptionTypeDef",
    {
        "CustomerAwsId": NotRequired[str],
        "CustSubscriptionId": NotRequired[str],
        "SnsTopicArn": NotRequired[str],
        "Status": NotRequired[str],
        "SubscriptionCreationTime": NotRequired[str],
        "SourceType": NotRequired[str],
        "SourceIdsList": NotRequired[List[str]],
        "EventCategoriesList": NotRequired[List[str]],
        "Enabled": NotRequired[bool],
        "EventSubscriptionArn": NotRequired[str],
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
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
ApplyPendingMaintenanceActionMessageRequestTypeDef = TypedDict(
    "ApplyPendingMaintenanceActionMessageRequestTypeDef",
    {
        "ResourceIdentifier": str,
        "ApplyAction": str,
        "OptInType": str,
    },
)
AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "Name": NotRequired[str],
    },
)
CertificateDetailsTypeDef = TypedDict(
    "CertificateDetailsTypeDef",
    {
        "CAIdentifier": NotRequired[str],
        "ValidTill": NotRequired[datetime],
    },
)
CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "CertificateIdentifier": NotRequired[str],
        "CertificateType": NotRequired[str],
        "Thumbprint": NotRequired[str],
        "ValidFrom": NotRequired[datetime],
        "ValidTill": NotRequired[datetime],
        "CertificateArn": NotRequired[str],
    },
)
CloudwatchLogsExportConfigurationTypeDef = TypedDict(
    "CloudwatchLogsExportConfigurationTypeDef",
    {
        "EnableLogTypes": NotRequired[Sequence[str]],
        "DisableLogTypes": NotRequired[Sequence[str]],
    },
)
DBClusterParameterGroupTypeDef = TypedDict(
    "DBClusterParameterGroupTypeDef",
    {
        "DBClusterParameterGroupName": NotRequired[str],
        "DBParameterGroupFamily": NotRequired[str],
        "Description": NotRequired[str],
        "DBClusterParameterGroupArn": NotRequired[str],
    },
)
DBClusterSnapshotTypeDef = TypedDict(
    "DBClusterSnapshotTypeDef",
    {
        "AvailabilityZones": NotRequired[List[str]],
        "DBClusterSnapshotIdentifier": NotRequired[str],
        "DBClusterIdentifier": NotRequired[str],
        "SnapshotCreateTime": NotRequired[datetime],
        "Engine": NotRequired[str],
        "Status": NotRequired[str],
        "Port": NotRequired[int],
        "VpcId": NotRequired[str],
        "ClusterCreateTime": NotRequired[datetime],
        "MasterUsername": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "PercentProgress": NotRequired[int],
        "StorageEncrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "DBClusterSnapshotArn": NotRequired[str],
        "SourceDBClusterSnapshotArn": NotRequired[str],
        "StorageType": NotRequired[str],
    },
)
CreateGlobalClusterMessageRequestTypeDef = TypedDict(
    "CreateGlobalClusterMessageRequestTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "SourceDBClusterIdentifier": NotRequired[str],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "DeletionProtection": NotRequired[bool],
        "DatabaseName": NotRequired[str],
        "StorageEncrypted": NotRequired[bool],
    },
)
DBClusterMemberTypeDef = TypedDict(
    "DBClusterMemberTypeDef",
    {
        "DBInstanceIdentifier": NotRequired[str],
        "IsClusterWriter": NotRequired[bool],
        "DBClusterParameterGroupStatus": NotRequired[str],
        "PromotionTier": NotRequired[int],
    },
)
ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "ParameterName": NotRequired[str],
        "ParameterValue": NotRequired[str],
        "Description": NotRequired[str],
        "Source": NotRequired[str],
        "ApplyType": NotRequired[str],
        "DataType": NotRequired[str],
        "AllowedValues": NotRequired[str],
        "IsModifiable": NotRequired[bool],
        "MinimumEngineVersion": NotRequired[str],
        "ApplyMethod": NotRequired[ApplyMethodType],
    },
)
DBClusterRoleTypeDef = TypedDict(
    "DBClusterRoleTypeDef",
    {
        "RoleArn": NotRequired[str],
        "Status": NotRequired[str],
    },
)
DBClusterSnapshotAttributeTypeDef = TypedDict(
    "DBClusterSnapshotAttributeTypeDef",
    {
        "AttributeName": NotRequired[str],
        "AttributeValues": NotRequired[List[str]],
    },
)
VpcSecurityGroupMembershipTypeDef = TypedDict(
    "VpcSecurityGroupMembershipTypeDef",
    {
        "VpcSecurityGroupId": NotRequired[str],
        "Status": NotRequired[str],
    },
)
UpgradeTargetTypeDef = TypedDict(
    "UpgradeTargetTypeDef",
    {
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "Description": NotRequired[str],
        "AutoUpgrade": NotRequired[bool],
        "IsMajorVersionUpgrade": NotRequired[bool],
    },
)
DBInstanceStatusInfoTypeDef = TypedDict(
    "DBInstanceStatusInfoTypeDef",
    {
        "StatusType": NotRequired[str],
        "Normal": NotRequired[bool],
        "Status": NotRequired[str],
        "Message": NotRequired[str],
    },
)
EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": NotRequired[str],
        "Port": NotRequired[int],
        "HostedZoneId": NotRequired[str],
    },
)
DeleteDBClusterMessageRequestTypeDef = TypedDict(
    "DeleteDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "SkipFinalSnapshot": NotRequired[bool],
        "FinalDBSnapshotIdentifier": NotRequired[str],
    },
)
DeleteDBClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "DeleteDBClusterParameterGroupMessageRequestTypeDef",
    {
        "DBClusterParameterGroupName": str,
    },
)
DeleteDBClusterSnapshotMessageRequestTypeDef = TypedDict(
    "DeleteDBClusterSnapshotMessageRequestTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
    },
)
DeleteDBInstanceMessageRequestTypeDef = TypedDict(
    "DeleteDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
    },
)
DeleteDBSubnetGroupMessageRequestTypeDef = TypedDict(
    "DeleteDBSubnetGroupMessageRequestTypeDef",
    {
        "DBSubnetGroupName": str,
    },
)
DeleteEventSubscriptionMessageRequestTypeDef = TypedDict(
    "DeleteEventSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
    },
)
DeleteGlobalClusterMessageRequestTypeDef = TypedDict(
    "DeleteGlobalClusterMessageRequestTypeDef",
    {
        "GlobalClusterIdentifier": str,
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "Values": Sequence[str],
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
DescribeDBClusterSnapshotAttributesMessageRequestTypeDef = TypedDict(
    "DescribeDBClusterSnapshotAttributesMessageRequestTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
TimestampTypeDef = Union[datetime, str]
EventCategoriesMapTypeDef = TypedDict(
    "EventCategoriesMapTypeDef",
    {
        "SourceType": NotRequired[str],
        "EventCategories": NotRequired[List[str]],
    },
)
EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "SourceIdentifier": NotRequired[str],
        "SourceType": NotRequired[SourceTypeType],
        "Message": NotRequired[str],
        "EventCategories": NotRequired[List[str]],
        "Date": NotRequired[datetime],
        "SourceArn": NotRequired[str],
    },
)
FailoverDBClusterMessageRequestTypeDef = TypedDict(
    "FailoverDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": NotRequired[str],
        "TargetDBInstanceIdentifier": NotRequired[str],
    },
)
FailoverGlobalClusterMessageRequestTypeDef = TypedDict(
    "FailoverGlobalClusterMessageRequestTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "TargetDbClusterIdentifier": str,
        "AllowDataLoss": NotRequired[bool],
        "Switchover": NotRequired[bool],
    },
)
GlobalClusterMemberTypeDef = TypedDict(
    "GlobalClusterMemberTypeDef",
    {
        "DBClusterArn": NotRequired[str],
        "Readers": NotRequired[List[str]],
        "IsWriter": NotRequired[bool],
    },
)
ModifyDBClusterSnapshotAttributeMessageRequestTypeDef = TypedDict(
    "ModifyDBClusterSnapshotAttributeMessageRequestTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
        "AttributeName": str,
        "ValuesToAdd": NotRequired[Sequence[str]],
        "ValuesToRemove": NotRequired[Sequence[str]],
    },
)
ModifyDBInstanceMessageRequestTypeDef = TypedDict(
    "ModifyDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": NotRequired[str],
        "ApplyImmediately": NotRequired[bool],
        "PreferredMaintenanceWindow": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "NewDBInstanceIdentifier": NotRequired[str],
        "CACertificateIdentifier": NotRequired[str],
        "CopyTagsToSnapshot": NotRequired[bool],
        "PromotionTier": NotRequired[int],
        "EnablePerformanceInsights": NotRequired[bool],
        "PerformanceInsightsKMSKeyId": NotRequired[str],
        "CertificateRotationRestart": NotRequired[bool],
    },
)
ModifyDBSubnetGroupMessageRequestTypeDef = TypedDict(
    "ModifyDBSubnetGroupMessageRequestTypeDef",
    {
        "DBSubnetGroupName": str,
        "SubnetIds": Sequence[str],
        "DBSubnetGroupDescription": NotRequired[str],
    },
)
ModifyEventSubscriptionMessageRequestTypeDef = TypedDict(
    "ModifyEventSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
        "SnsTopicArn": NotRequired[str],
        "SourceType": NotRequired[str],
        "EventCategories": NotRequired[Sequence[str]],
        "Enabled": NotRequired[bool],
    },
)
ModifyGlobalClusterMessageRequestTypeDef = TypedDict(
    "ModifyGlobalClusterMessageRequestTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "NewGlobalClusterIdentifier": NotRequired[str],
        "DeletionProtection": NotRequired[bool],
    },
)
PendingCloudwatchLogsExportsTypeDef = TypedDict(
    "PendingCloudwatchLogsExportsTypeDef",
    {
        "LogTypesToEnable": NotRequired[List[str]],
        "LogTypesToDisable": NotRequired[List[str]],
    },
)
PendingMaintenanceActionTypeDef = TypedDict(
    "PendingMaintenanceActionTypeDef",
    {
        "Action": NotRequired[str],
        "AutoAppliedAfterDate": NotRequired[datetime],
        "ForcedApplyDate": NotRequired[datetime],
        "OptInStatus": NotRequired[str],
        "CurrentApplyDate": NotRequired[datetime],
        "Description": NotRequired[str],
    },
)
RebootDBInstanceMessageRequestTypeDef = TypedDict(
    "RebootDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "ForceFailover": NotRequired[bool],
    },
)
RemoveFromGlobalClusterMessageRequestTypeDef = TypedDict(
    "RemoveFromGlobalClusterMessageRequestTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "DbClusterIdentifier": str,
    },
)
RemoveSourceIdentifierFromSubscriptionMessageRequestTypeDef = TypedDict(
    "RemoveSourceIdentifierFromSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
        "SourceIdentifier": str,
    },
)
RemoveTagsFromResourceMessageRequestTypeDef = TypedDict(
    "RemoveTagsFromResourceMessageRequestTypeDef",
    {
        "ResourceName": str,
        "TagKeys": Sequence[str],
    },
)
StartDBClusterMessageRequestTypeDef = TypedDict(
    "StartDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
    },
)
StopDBClusterMessageRequestTypeDef = TypedDict(
    "StopDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
    },
)
SwitchoverGlobalClusterMessageRequestTypeDef = TypedDict(
    "SwitchoverGlobalClusterMessageRequestTypeDef",
    {
        "GlobalClusterIdentifier": str,
        "TargetDbClusterIdentifier": str,
    },
)
AddSourceIdentifierToSubscriptionResultTypeDef = TypedDict(
    "AddSourceIdentifierToSubscriptionResultTypeDef",
    {
        "EventSubscription": EventSubscriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEventSubscriptionResultTypeDef = TypedDict(
    "CreateEventSubscriptionResultTypeDef",
    {
        "EventSubscription": EventSubscriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DBClusterParameterGroupNameMessageTypeDef = TypedDict(
    "DBClusterParameterGroupNameMessageTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteEventSubscriptionResultTypeDef = TypedDict(
    "DeleteEventSubscriptionResultTypeDef",
    {
        "EventSubscription": EventSubscriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EventSubscriptionsMessageTypeDef = TypedDict(
    "EventSubscriptionsMessageTypeDef",
    {
        "Marker": str,
        "EventSubscriptionsList": List[EventSubscriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyEventSubscriptionResultTypeDef = TypedDict(
    "ModifyEventSubscriptionResultTypeDef",
    {
        "EventSubscription": EventSubscriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RemoveSourceIdentifierFromSubscriptionResultTypeDef = TypedDict(
    "RemoveSourceIdentifierFromSubscriptionResultTypeDef",
    {
        "EventSubscription": EventSubscriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AddTagsToResourceMessageRequestTypeDef = TypedDict(
    "AddTagsToResourceMessageRequestTypeDef",
    {
        "ResourceName": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CopyDBClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "CopyDBClusterParameterGroupMessageRequestTypeDef",
    {
        "SourceDBClusterParameterGroupIdentifier": str,
        "TargetDBClusterParameterGroupIdentifier": str,
        "TargetDBClusterParameterGroupDescription": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CopyDBClusterSnapshotMessageRequestTypeDef = TypedDict(
    "CopyDBClusterSnapshotMessageRequestTypeDef",
    {
        "SourceDBClusterSnapshotIdentifier": str,
        "TargetDBClusterSnapshotIdentifier": str,
        "KmsKeyId": NotRequired[str],
        "PreSignedUrl": NotRequired[str],
        "CopyTags": NotRequired[bool],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "SourceRegion": NotRequired[str],
    },
)
CreateDBClusterMessageRequestTypeDef = TypedDict(
    "CreateDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "Engine": str,
        "AvailabilityZones": NotRequired[Sequence[str]],
        "BackupRetentionPeriod": NotRequired[int],
        "DBClusterParameterGroupName": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "DBSubnetGroupName": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "Port": NotRequired[int],
        "MasterUsername": NotRequired[str],
        "MasterUserPassword": NotRequired[str],
        "PreferredBackupWindow": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "StorageEncrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "PreSignedUrl": NotRequired[str],
        "EnableCloudwatchLogsExports": NotRequired[Sequence[str]],
        "DeletionProtection": NotRequired[bool],
        "GlobalClusterIdentifier": NotRequired[str],
        "StorageType": NotRequired[str],
        "SourceRegion": NotRequired[str],
    },
)
CreateDBClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "CreateDBClusterParameterGroupMessageRequestTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "DBParameterGroupFamily": str,
        "Description": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateDBClusterSnapshotMessageRequestTypeDef = TypedDict(
    "CreateDBClusterSnapshotMessageRequestTypeDef",
    {
        "DBClusterSnapshotIdentifier": str,
        "DBClusterIdentifier": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateDBInstanceMessageRequestTypeDef = TypedDict(
    "CreateDBInstanceMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": str,
        "DBInstanceClass": str,
        "Engine": str,
        "DBClusterIdentifier": str,
        "AvailabilityZone": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "CopyTagsToSnapshot": NotRequired[bool],
        "PromotionTier": NotRequired[int],
        "EnablePerformanceInsights": NotRequired[bool],
        "PerformanceInsightsKMSKeyId": NotRequired[str],
        "CACertificateIdentifier": NotRequired[str],
    },
)
CreateDBSubnetGroupMessageRequestTypeDef = TypedDict(
    "CreateDBSubnetGroupMessageRequestTypeDef",
    {
        "DBSubnetGroupName": str,
        "DBSubnetGroupDescription": str,
        "SubnetIds": Sequence[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateEventSubscriptionMessageRequestTypeDef = TypedDict(
    "CreateEventSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
        "SnsTopicArn": str,
        "SourceType": NotRequired[str],
        "EventCategories": NotRequired[Sequence[str]],
        "SourceIds": NotRequired[Sequence[str]],
        "Enabled": NotRequired[bool],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
RestoreDBClusterFromSnapshotMessageRequestTypeDef = TypedDict(
    "RestoreDBClusterFromSnapshotMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "SnapshotIdentifier": str,
        "Engine": str,
        "AvailabilityZones": NotRequired[Sequence[str]],
        "EngineVersion": NotRequired[str],
        "Port": NotRequired[int],
        "DBSubnetGroupName": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "KmsKeyId": NotRequired[str],
        "EnableCloudwatchLogsExports": NotRequired[Sequence[str]],
        "DeletionProtection": NotRequired[bool],
        "DBClusterParameterGroupName": NotRequired[str],
        "StorageType": NotRequired[str],
    },
)
TagListMessageTypeDef = TypedDict(
    "TagListMessageTypeDef",
    {
        "TagList": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OrderableDBInstanceOptionTypeDef = TypedDict(
    "OrderableDBInstanceOptionTypeDef",
    {
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "DBInstanceClass": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "AvailabilityZones": NotRequired[List[AvailabilityZoneTypeDef]],
        "Vpc": NotRequired[bool],
        "StorageType": NotRequired[str],
    },
)
SubnetTypeDef = TypedDict(
    "SubnetTypeDef",
    {
        "SubnetIdentifier": NotRequired[str],
        "SubnetAvailabilityZone": NotRequired[AvailabilityZoneTypeDef],
        "SubnetStatus": NotRequired[str],
    },
)
CertificateMessageTypeDef = TypedDict(
    "CertificateMessageTypeDef",
    {
        "Certificates": List[CertificateTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyDBClusterMessageRequestTypeDef = TypedDict(
    "ModifyDBClusterMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "NewDBClusterIdentifier": NotRequired[str],
        "ApplyImmediately": NotRequired[bool],
        "BackupRetentionPeriod": NotRequired[int],
        "DBClusterParameterGroupName": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "Port": NotRequired[int],
        "MasterUserPassword": NotRequired[str],
        "PreferredBackupWindow": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "CloudwatchLogsExportConfiguration": NotRequired[CloudwatchLogsExportConfigurationTypeDef],
        "EngineVersion": NotRequired[str],
        "AllowMajorVersionUpgrade": NotRequired[bool],
        "DeletionProtection": NotRequired[bool],
        "StorageType": NotRequired[str],
    },
)
CopyDBClusterParameterGroupResultTypeDef = TypedDict(
    "CopyDBClusterParameterGroupResultTypeDef",
    {
        "DBClusterParameterGroup": DBClusterParameterGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDBClusterParameterGroupResultTypeDef = TypedDict(
    "CreateDBClusterParameterGroupResultTypeDef",
    {
        "DBClusterParameterGroup": DBClusterParameterGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DBClusterParameterGroupsMessageTypeDef = TypedDict(
    "DBClusterParameterGroupsMessageTypeDef",
    {
        "Marker": str,
        "DBClusterParameterGroups": List[DBClusterParameterGroupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CopyDBClusterSnapshotResultTypeDef = TypedDict(
    "CopyDBClusterSnapshotResultTypeDef",
    {
        "DBClusterSnapshot": DBClusterSnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDBClusterSnapshotResultTypeDef = TypedDict(
    "CreateDBClusterSnapshotResultTypeDef",
    {
        "DBClusterSnapshot": DBClusterSnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DBClusterSnapshotMessageTypeDef = TypedDict(
    "DBClusterSnapshotMessageTypeDef",
    {
        "Marker": str,
        "DBClusterSnapshots": List[DBClusterSnapshotTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDBClusterSnapshotResultTypeDef = TypedDict(
    "DeleteDBClusterSnapshotResultTypeDef",
    {
        "DBClusterSnapshot": DBClusterSnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DBClusterParameterGroupDetailsTypeDef = TypedDict(
    "DBClusterParameterGroupDetailsTypeDef",
    {
        "Parameters": List[ParameterTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EngineDefaultsTypeDef = TypedDict(
    "EngineDefaultsTypeDef",
    {
        "DBParameterGroupFamily": NotRequired[str],
        "Marker": NotRequired[str],
        "Parameters": NotRequired[List[ParameterTypeDef]],
    },
)
ModifyDBClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "ModifyDBClusterParameterGroupMessageRequestTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "Parameters": Sequence[ParameterTypeDef],
    },
)
ResetDBClusterParameterGroupMessageRequestTypeDef = TypedDict(
    "ResetDBClusterParameterGroupMessageRequestTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "ResetAllParameters": NotRequired[bool],
        "Parameters": NotRequired[Sequence[ParameterTypeDef]],
    },
)
DBClusterSnapshotAttributesResultTypeDef = TypedDict(
    "DBClusterSnapshotAttributesResultTypeDef",
    {
        "DBClusterSnapshotIdentifier": NotRequired[str],
        "DBClusterSnapshotAttributes": NotRequired[List[DBClusterSnapshotAttributeTypeDef]],
    },
)
DBClusterTypeDef = TypedDict(
    "DBClusterTypeDef",
    {
        "AvailabilityZones": NotRequired[List[str]],
        "BackupRetentionPeriod": NotRequired[int],
        "DBClusterIdentifier": NotRequired[str],
        "DBClusterParameterGroup": NotRequired[str],
        "DBSubnetGroup": NotRequired[str],
        "Status": NotRequired[str],
        "PercentProgress": NotRequired[str],
        "EarliestRestorableTime": NotRequired[datetime],
        "Endpoint": NotRequired[str],
        "ReaderEndpoint": NotRequired[str],
        "MultiAZ": NotRequired[bool],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "LatestRestorableTime": NotRequired[datetime],
        "Port": NotRequired[int],
        "MasterUsername": NotRequired[str],
        "PreferredBackupWindow": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "ReplicationSourceIdentifier": NotRequired[str],
        "ReadReplicaIdentifiers": NotRequired[List[str]],
        "DBClusterMembers": NotRequired[List[DBClusterMemberTypeDef]],
        "VpcSecurityGroups": NotRequired[List[VpcSecurityGroupMembershipTypeDef]],
        "HostedZoneId": NotRequired[str],
        "StorageEncrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "DbClusterResourceId": NotRequired[str],
        "DBClusterArn": NotRequired[str],
        "AssociatedRoles": NotRequired[List[DBClusterRoleTypeDef]],
        "CloneGroupId": NotRequired[str],
        "ClusterCreateTime": NotRequired[datetime],
        "EnabledCloudwatchLogsExports": NotRequired[List[str]],
        "DeletionProtection": NotRequired[bool],
        "StorageType": NotRequired[str],
    },
)
DBEngineVersionTypeDef = TypedDict(
    "DBEngineVersionTypeDef",
    {
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "DBParameterGroupFamily": NotRequired[str],
        "DBEngineDescription": NotRequired[str],
        "DBEngineVersionDescription": NotRequired[str],
        "ValidUpgradeTarget": NotRequired[List[UpgradeTargetTypeDef]],
        "ExportableLogTypes": NotRequired[List[str]],
        "SupportsLogExportsToCloudwatchLogs": NotRequired[bool],
        "SupportedCACertificateIdentifiers": NotRequired[List[str]],
        "SupportsCertificateRotationWithoutRestart": NotRequired[bool],
    },
)
DescribeCertificatesMessageRequestTypeDef = TypedDict(
    "DescribeCertificatesMessageRequestTypeDef",
    {
        "CertificateIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeDBClusterParameterGroupsMessageRequestTypeDef = TypedDict(
    "DescribeDBClusterParameterGroupsMessageRequestTypeDef",
    {
        "DBClusterParameterGroupName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeDBClusterParametersMessageRequestTypeDef = TypedDict(
    "DescribeDBClusterParametersMessageRequestTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "Source": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeDBClusterSnapshotsMessageRequestTypeDef = TypedDict(
    "DescribeDBClusterSnapshotsMessageRequestTypeDef",
    {
        "DBClusterIdentifier": NotRequired[str],
        "DBClusterSnapshotIdentifier": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "IncludeShared": NotRequired[bool],
        "IncludePublic": NotRequired[bool],
    },
)
DescribeDBClustersMessageRequestTypeDef = TypedDict(
    "DescribeDBClustersMessageRequestTypeDef",
    {
        "DBClusterIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeDBEngineVersionsMessageRequestTypeDef = TypedDict(
    "DescribeDBEngineVersionsMessageRequestTypeDef",
    {
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "DBParameterGroupFamily": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "DefaultOnly": NotRequired[bool],
        "ListSupportedCharacterSets": NotRequired[bool],
        "ListSupportedTimezones": NotRequired[bool],
    },
)
DescribeDBInstancesMessageRequestTypeDef = TypedDict(
    "DescribeDBInstancesMessageRequestTypeDef",
    {
        "DBInstanceIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeDBSubnetGroupsMessageRequestTypeDef = TypedDict(
    "DescribeDBSubnetGroupsMessageRequestTypeDef",
    {
        "DBSubnetGroupName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeEngineDefaultClusterParametersMessageRequestTypeDef = TypedDict(
    "DescribeEngineDefaultClusterParametersMessageRequestTypeDef",
    {
        "DBParameterGroupFamily": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeEventCategoriesMessageRequestTypeDef = TypedDict(
    "DescribeEventCategoriesMessageRequestTypeDef",
    {
        "SourceType": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
DescribeEventSubscriptionsMessageRequestTypeDef = TypedDict(
    "DescribeEventSubscriptionsMessageRequestTypeDef",
    {
        "SubscriptionName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeGlobalClustersMessageRequestTypeDef = TypedDict(
    "DescribeGlobalClustersMessageRequestTypeDef",
    {
        "GlobalClusterIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeOrderableDBInstanceOptionsMessageRequestTypeDef = TypedDict(
    "DescribeOrderableDBInstanceOptionsMessageRequestTypeDef",
    {
        "Engine": str,
        "EngineVersion": NotRequired[str],
        "DBInstanceClass": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "Vpc": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribePendingMaintenanceActionsMessageRequestTypeDef = TypedDict(
    "DescribePendingMaintenanceActionsMessageRequestTypeDef",
    {
        "ResourceIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "Marker": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)
ListTagsForResourceMessageRequestTypeDef = TypedDict(
    "ListTagsForResourceMessageRequestTypeDef",
    {
        "ResourceName": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
DescribeCertificatesMessageDescribeCertificatesPaginateTypeDef = TypedDict(
    "DescribeCertificatesMessageDescribeCertificatesPaginateTypeDef",
    {
        "CertificateIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDBClusterParameterGroupsMessageDescribeDBClusterParameterGroupsPaginateTypeDef = TypedDict(
    "DescribeDBClusterParameterGroupsMessageDescribeDBClusterParameterGroupsPaginateTypeDef",
    {
        "DBClusterParameterGroupName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDBClusterParametersMessageDescribeDBClusterParametersPaginateTypeDef = TypedDict(
    "DescribeDBClusterParametersMessageDescribeDBClusterParametersPaginateTypeDef",
    {
        "DBClusterParameterGroupName": str,
        "Source": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDBClusterSnapshotsMessageDescribeDBClusterSnapshotsPaginateTypeDef = TypedDict(
    "DescribeDBClusterSnapshotsMessageDescribeDBClusterSnapshotsPaginateTypeDef",
    {
        "DBClusterIdentifier": NotRequired[str],
        "DBClusterSnapshotIdentifier": NotRequired[str],
        "SnapshotType": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "IncludeShared": NotRequired[bool],
        "IncludePublic": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDBClustersMessageDescribeDBClustersPaginateTypeDef = TypedDict(
    "DescribeDBClustersMessageDescribeDBClustersPaginateTypeDef",
    {
        "DBClusterIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDBEngineVersionsMessageDescribeDBEngineVersionsPaginateTypeDef = TypedDict(
    "DescribeDBEngineVersionsMessageDescribeDBEngineVersionsPaginateTypeDef",
    {
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "DBParameterGroupFamily": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "DefaultOnly": NotRequired[bool],
        "ListSupportedCharacterSets": NotRequired[bool],
        "ListSupportedTimezones": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDBInstancesMessageDescribeDBInstancesPaginateTypeDef = TypedDict(
    "DescribeDBInstancesMessageDescribeDBInstancesPaginateTypeDef",
    {
        "DBInstanceIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDBSubnetGroupsMessageDescribeDBSubnetGroupsPaginateTypeDef = TypedDict(
    "DescribeDBSubnetGroupsMessageDescribeDBSubnetGroupsPaginateTypeDef",
    {
        "DBSubnetGroupName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEventSubscriptionsMessageDescribeEventSubscriptionsPaginateTypeDef = TypedDict(
    "DescribeEventSubscriptionsMessageDescribeEventSubscriptionsPaginateTypeDef",
    {
        "SubscriptionName": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeGlobalClustersMessageDescribeGlobalClustersPaginateTypeDef = TypedDict(
    "DescribeGlobalClustersMessageDescribeGlobalClustersPaginateTypeDef",
    {
        "GlobalClusterIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeOrderableDBInstanceOptionsMessageDescribeOrderableDBInstanceOptionsPaginateTypeDef = TypedDict(
    "DescribeOrderableDBInstanceOptionsMessageDescribeOrderableDBInstanceOptionsPaginateTypeDef",
    {
        "Engine": str,
        "EngineVersion": NotRequired[str],
        "DBInstanceClass": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "Vpc": NotRequired[bool],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribePendingMaintenanceActionsMessageDescribePendingMaintenanceActionsPaginateTypeDef = (
    TypedDict(
        "DescribePendingMaintenanceActionsMessageDescribePendingMaintenanceActionsPaginateTypeDef",
        {
            "ResourceIdentifier": NotRequired[str],
            "Filters": NotRequired[Sequence[FilterTypeDef]],
            "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
        },
    )
)
DescribeDBInstancesMessageDBInstanceAvailableWaitTypeDef = TypedDict(
    "DescribeDBInstancesMessageDBInstanceAvailableWaitTypeDef",
    {
        "DBInstanceIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeDBInstancesMessageDBInstanceDeletedWaitTypeDef = TypedDict(
    "DescribeDBInstancesMessageDBInstanceDeletedWaitTypeDef",
    {
        "DBInstanceIdentifier": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
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
        "EventCategories": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
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
        "EventCategories": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
RestoreDBClusterToPointInTimeMessageRequestTypeDef = TypedDict(
    "RestoreDBClusterToPointInTimeMessageRequestTypeDef",
    {
        "DBClusterIdentifier": str,
        "SourceDBClusterIdentifier": str,
        "RestoreType": NotRequired[str],
        "RestoreToTime": NotRequired[TimestampTypeDef],
        "UseLatestRestorableTime": NotRequired[bool],
        "Port": NotRequired[int],
        "DBSubnetGroupName": NotRequired[str],
        "VpcSecurityGroupIds": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "KmsKeyId": NotRequired[str],
        "EnableCloudwatchLogsExports": NotRequired[Sequence[str]],
        "DeletionProtection": NotRequired[bool],
        "StorageType": NotRequired[str],
    },
)
EventCategoriesMessageTypeDef = TypedDict(
    "EventCategoriesMessageTypeDef",
    {
        "EventCategoriesMapList": List[EventCategoriesMapTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
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
GlobalClusterTypeDef = TypedDict(
    "GlobalClusterTypeDef",
    {
        "GlobalClusterIdentifier": NotRequired[str],
        "GlobalClusterResourceId": NotRequired[str],
        "GlobalClusterArn": NotRequired[str],
        "Status": NotRequired[str],
        "Engine": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "StorageEncrypted": NotRequired[bool],
        "DeletionProtection": NotRequired[bool],
        "GlobalClusterMembers": NotRequired[List[GlobalClusterMemberTypeDef]],
    },
)
PendingModifiedValuesTypeDef = TypedDict(
    "PendingModifiedValuesTypeDef",
    {
        "DBInstanceClass": NotRequired[str],
        "AllocatedStorage": NotRequired[int],
        "MasterUserPassword": NotRequired[str],
        "Port": NotRequired[int],
        "BackupRetentionPeriod": NotRequired[int],
        "MultiAZ": NotRequired[bool],
        "EngineVersion": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "Iops": NotRequired[int],
        "DBInstanceIdentifier": NotRequired[str],
        "StorageType": NotRequired[str],
        "CACertificateIdentifier": NotRequired[str],
        "DBSubnetGroupName": NotRequired[str],
        "PendingCloudwatchLogsExports": NotRequired[PendingCloudwatchLogsExportsTypeDef],
    },
)
ResourcePendingMaintenanceActionsTypeDef = TypedDict(
    "ResourcePendingMaintenanceActionsTypeDef",
    {
        "ResourceIdentifier": NotRequired[str],
        "PendingMaintenanceActionDetails": NotRequired[List[PendingMaintenanceActionTypeDef]],
    },
)
OrderableDBInstanceOptionsMessageTypeDef = TypedDict(
    "OrderableDBInstanceOptionsMessageTypeDef",
    {
        "OrderableDBInstanceOptions": List[OrderableDBInstanceOptionTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DBSubnetGroupTypeDef = TypedDict(
    "DBSubnetGroupTypeDef",
    {
        "DBSubnetGroupName": NotRequired[str],
        "DBSubnetGroupDescription": NotRequired[str],
        "VpcId": NotRequired[str],
        "SubnetGroupStatus": NotRequired[str],
        "Subnets": NotRequired[List[SubnetTypeDef]],
        "DBSubnetGroupArn": NotRequired[str],
    },
)
DescribeEngineDefaultClusterParametersResultTypeDef = TypedDict(
    "DescribeEngineDefaultClusterParametersResultTypeDef",
    {
        "EngineDefaults": EngineDefaultsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDBClusterSnapshotAttributesResultTypeDef = TypedDict(
    "DescribeDBClusterSnapshotAttributesResultTypeDef",
    {
        "DBClusterSnapshotAttributesResult": DBClusterSnapshotAttributesResultTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyDBClusterSnapshotAttributeResultTypeDef = TypedDict(
    "ModifyDBClusterSnapshotAttributeResultTypeDef",
    {
        "DBClusterSnapshotAttributesResult": DBClusterSnapshotAttributesResultTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDBClusterResultTypeDef = TypedDict(
    "CreateDBClusterResultTypeDef",
    {
        "DBCluster": DBClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DBClusterMessageTypeDef = TypedDict(
    "DBClusterMessageTypeDef",
    {
        "Marker": str,
        "DBClusters": List[DBClusterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDBClusterResultTypeDef = TypedDict(
    "DeleteDBClusterResultTypeDef",
    {
        "DBCluster": DBClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FailoverDBClusterResultTypeDef = TypedDict(
    "FailoverDBClusterResultTypeDef",
    {
        "DBCluster": DBClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyDBClusterResultTypeDef = TypedDict(
    "ModifyDBClusterResultTypeDef",
    {
        "DBCluster": DBClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreDBClusterFromSnapshotResultTypeDef = TypedDict(
    "RestoreDBClusterFromSnapshotResultTypeDef",
    {
        "DBCluster": DBClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreDBClusterToPointInTimeResultTypeDef = TypedDict(
    "RestoreDBClusterToPointInTimeResultTypeDef",
    {
        "DBCluster": DBClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartDBClusterResultTypeDef = TypedDict(
    "StartDBClusterResultTypeDef",
    {
        "DBCluster": DBClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopDBClusterResultTypeDef = TypedDict(
    "StopDBClusterResultTypeDef",
    {
        "DBCluster": DBClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DBEngineVersionMessageTypeDef = TypedDict(
    "DBEngineVersionMessageTypeDef",
    {
        "Marker": str,
        "DBEngineVersions": List[DBEngineVersionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGlobalClusterResultTypeDef = TypedDict(
    "CreateGlobalClusterResultTypeDef",
    {
        "GlobalCluster": GlobalClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteGlobalClusterResultTypeDef = TypedDict(
    "DeleteGlobalClusterResultTypeDef",
    {
        "GlobalCluster": GlobalClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FailoverGlobalClusterResultTypeDef = TypedDict(
    "FailoverGlobalClusterResultTypeDef",
    {
        "GlobalCluster": GlobalClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GlobalClustersMessageTypeDef = TypedDict(
    "GlobalClustersMessageTypeDef",
    {
        "Marker": str,
        "GlobalClusters": List[GlobalClusterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyGlobalClusterResultTypeDef = TypedDict(
    "ModifyGlobalClusterResultTypeDef",
    {
        "GlobalCluster": GlobalClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RemoveFromGlobalClusterResultTypeDef = TypedDict(
    "RemoveFromGlobalClusterResultTypeDef",
    {
        "GlobalCluster": GlobalClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SwitchoverGlobalClusterResultTypeDef = TypedDict(
    "SwitchoverGlobalClusterResultTypeDef",
    {
        "GlobalCluster": GlobalClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ApplyPendingMaintenanceActionResultTypeDef = TypedDict(
    "ApplyPendingMaintenanceActionResultTypeDef",
    {
        "ResourcePendingMaintenanceActions": ResourcePendingMaintenanceActionsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PendingMaintenanceActionsMessageTypeDef = TypedDict(
    "PendingMaintenanceActionsMessageTypeDef",
    {
        "PendingMaintenanceActions": List[ResourcePendingMaintenanceActionsTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDBSubnetGroupResultTypeDef = TypedDict(
    "CreateDBSubnetGroupResultTypeDef",
    {
        "DBSubnetGroup": DBSubnetGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DBInstanceTypeDef = TypedDict(
    "DBInstanceTypeDef",
    {
        "DBInstanceIdentifier": NotRequired[str],
        "DBInstanceClass": NotRequired[str],
        "Engine": NotRequired[str],
        "DBInstanceStatus": NotRequired[str],
        "Endpoint": NotRequired[EndpointTypeDef],
        "InstanceCreateTime": NotRequired[datetime],
        "PreferredBackupWindow": NotRequired[str],
        "BackupRetentionPeriod": NotRequired[int],
        "VpcSecurityGroups": NotRequired[List[VpcSecurityGroupMembershipTypeDef]],
        "AvailabilityZone": NotRequired[str],
        "DBSubnetGroup": NotRequired[DBSubnetGroupTypeDef],
        "PreferredMaintenanceWindow": NotRequired[str],
        "PendingModifiedValues": NotRequired[PendingModifiedValuesTypeDef],
        "LatestRestorableTime": NotRequired[datetime],
        "EngineVersion": NotRequired[str],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "PubliclyAccessible": NotRequired[bool],
        "StatusInfos": NotRequired[List[DBInstanceStatusInfoTypeDef]],
        "DBClusterIdentifier": NotRequired[str],
        "StorageEncrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "DbiResourceId": NotRequired[str],
        "CACertificateIdentifier": NotRequired[str],
        "CopyTagsToSnapshot": NotRequired[bool],
        "PromotionTier": NotRequired[int],
        "DBInstanceArn": NotRequired[str],
        "EnabledCloudwatchLogsExports": NotRequired[List[str]],
        "CertificateDetails": NotRequired[CertificateDetailsTypeDef],
        "PerformanceInsightsEnabled": NotRequired[bool],
        "PerformanceInsightsKMSKeyId": NotRequired[str],
    },
)
DBSubnetGroupMessageTypeDef = TypedDict(
    "DBSubnetGroupMessageTypeDef",
    {
        "Marker": str,
        "DBSubnetGroups": List[DBSubnetGroupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyDBSubnetGroupResultTypeDef = TypedDict(
    "ModifyDBSubnetGroupResultTypeDef",
    {
        "DBSubnetGroup": DBSubnetGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDBInstanceResultTypeDef = TypedDict(
    "CreateDBInstanceResultTypeDef",
    {
        "DBInstance": DBInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DBInstanceMessageTypeDef = TypedDict(
    "DBInstanceMessageTypeDef",
    {
        "Marker": str,
        "DBInstances": List[DBInstanceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDBInstanceResultTypeDef = TypedDict(
    "DeleteDBInstanceResultTypeDef",
    {
        "DBInstance": DBInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyDBInstanceResultTypeDef = TypedDict(
    "ModifyDBInstanceResultTypeDef",
    {
        "DBInstance": DBInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RebootDBInstanceResultTypeDef = TypedDict(
    "RebootDBInstanceResultTypeDef",
    {
        "DBInstance": DBInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
