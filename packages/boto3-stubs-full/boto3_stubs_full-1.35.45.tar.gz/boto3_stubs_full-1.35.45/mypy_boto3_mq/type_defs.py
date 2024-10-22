"""
Type annotations for mq service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mq/type_defs/)

Usage::

    ```python
    from mypy_boto3_mq.type_defs import ActionRequiredTypeDef

    data: ActionRequiredTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AuthenticationStrategyType,
    BrokerStateType,
    BrokerStorageTypeType,
    ChangeTypeType,
    DataReplicationModeType,
    DayOfWeekType,
    DeploymentModeType,
    EngineTypeType,
    PromoteModeType,
    SanitizationWarningReasonType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "ActionRequiredTypeDef",
    "AvailabilityZoneTypeDef",
    "EngineVersionTypeDef",
    "BrokerInstanceTypeDef",
    "BrokerSummaryTypeDef",
    "ConfigurationIdTypeDef",
    "ConfigurationRevisionTypeDef",
    "EncryptionOptionsTypeDef",
    "LdapServerMetadataInputTypeDef",
    "LogsTypeDef",
    "UserTypeDef",
    "WeeklyStartTimeTypeDef",
    "ResponseMetadataTypeDef",
    "CreateConfigurationRequestRequestTypeDef",
    "CreateTagsRequestRequestTypeDef",
    "CreateUserRequestRequestTypeDef",
    "DataReplicationCounterpartTypeDef",
    "DeleteBrokerRequestRequestTypeDef",
    "DeleteTagsRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DescribeBrokerEngineTypesRequestRequestTypeDef",
    "DescribeBrokerInstanceOptionsRequestRequestTypeDef",
    "DescribeBrokerRequestRequestTypeDef",
    "LdapServerMetadataOutputTypeDef",
    "UserSummaryTypeDef",
    "DescribeConfigurationRequestRequestTypeDef",
    "DescribeConfigurationRevisionRequestRequestTypeDef",
    "DescribeUserRequestRequestTypeDef",
    "UserPendingChangesTypeDef",
    "PaginatorConfigTypeDef",
    "ListBrokersRequestRequestTypeDef",
    "ListConfigurationRevisionsRequestRequestTypeDef",
    "ListConfigurationsRequestRequestTypeDef",
    "ListTagsRequestRequestTypeDef",
    "ListUsersRequestRequestTypeDef",
    "PendingLogsTypeDef",
    "PromoteRequestRequestTypeDef",
    "RebootBrokerRequestRequestTypeDef",
    "SanitizationWarningTypeDef",
    "UpdateConfigurationRequestRequestTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "BrokerInstanceOptionTypeDef",
    "BrokerEngineTypeTypeDef",
    "ConfigurationsTypeDef",
    "ConfigurationTypeDef",
    "CreateBrokerRequestRequestTypeDef",
    "UpdateBrokerRequestRequestTypeDef",
    "CreateBrokerResponseTypeDef",
    "CreateConfigurationResponseTypeDef",
    "DeleteBrokerResponseTypeDef",
    "DescribeConfigurationResponseTypeDef",
    "DescribeConfigurationRevisionResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ListBrokersResponseTypeDef",
    "ListConfigurationRevisionsResponseTypeDef",
    "ListTagsResponseTypeDef",
    "PromoteResponseTypeDef",
    "DataReplicationMetadataOutputTypeDef",
    "ListUsersResponseTypeDef",
    "DescribeUserResponseTypeDef",
    "ListBrokersRequestListBrokersPaginateTypeDef",
    "LogsSummaryTypeDef",
    "UpdateConfigurationResponseTypeDef",
    "DescribeBrokerInstanceOptionsResponseTypeDef",
    "DescribeBrokerEngineTypesResponseTypeDef",
    "ListConfigurationsResponseTypeDef",
    "UpdateBrokerResponseTypeDef",
    "DescribeBrokerResponseTypeDef",
)

ActionRequiredTypeDef = TypedDict(
    "ActionRequiredTypeDef",
    {
        "ActionRequiredCode": NotRequired[str],
        "ActionRequiredInfo": NotRequired[str],
    },
)
AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "Name": NotRequired[str],
    },
)
EngineVersionTypeDef = TypedDict(
    "EngineVersionTypeDef",
    {
        "Name": NotRequired[str],
    },
)
BrokerInstanceTypeDef = TypedDict(
    "BrokerInstanceTypeDef",
    {
        "ConsoleURL": NotRequired[str],
        "Endpoints": NotRequired[List[str]],
        "IpAddress": NotRequired[str],
    },
)
BrokerSummaryTypeDef = TypedDict(
    "BrokerSummaryTypeDef",
    {
        "DeploymentMode": DeploymentModeType,
        "EngineType": EngineTypeType,
        "BrokerArn": NotRequired[str],
        "BrokerId": NotRequired[str],
        "BrokerName": NotRequired[str],
        "BrokerState": NotRequired[BrokerStateType],
        "Created": NotRequired[datetime],
        "HostInstanceType": NotRequired[str],
    },
)
ConfigurationIdTypeDef = TypedDict(
    "ConfigurationIdTypeDef",
    {
        "Id": str,
        "Revision": NotRequired[int],
    },
)
ConfigurationRevisionTypeDef = TypedDict(
    "ConfigurationRevisionTypeDef",
    {
        "Created": datetime,
        "Revision": int,
        "Description": NotRequired[str],
    },
)
EncryptionOptionsTypeDef = TypedDict(
    "EncryptionOptionsTypeDef",
    {
        "UseAwsOwnedKey": bool,
        "KmsKeyId": NotRequired[str],
    },
)
LdapServerMetadataInputTypeDef = TypedDict(
    "LdapServerMetadataInputTypeDef",
    {
        "Hosts": Sequence[str],
        "RoleBase": str,
        "RoleSearchMatching": str,
        "ServiceAccountPassword": str,
        "ServiceAccountUsername": str,
        "UserBase": str,
        "UserSearchMatching": str,
        "RoleName": NotRequired[str],
        "RoleSearchSubtree": NotRequired[bool],
        "UserRoleName": NotRequired[str],
        "UserSearchSubtree": NotRequired[bool],
    },
)
LogsTypeDef = TypedDict(
    "LogsTypeDef",
    {
        "Audit": NotRequired[bool],
        "General": NotRequired[bool],
    },
)
UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "Password": str,
        "Username": str,
        "ConsoleAccess": NotRequired[bool],
        "Groups": NotRequired[Sequence[str]],
        "ReplicationUser": NotRequired[bool],
    },
)
WeeklyStartTimeTypeDef = TypedDict(
    "WeeklyStartTimeTypeDef",
    {
        "DayOfWeek": DayOfWeekType,
        "TimeOfDay": str,
        "TimeZone": NotRequired[str],
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
CreateConfigurationRequestRequestTypeDef = TypedDict(
    "CreateConfigurationRequestRequestTypeDef",
    {
        "EngineType": EngineTypeType,
        "Name": str,
        "AuthenticationStrategy": NotRequired[AuthenticationStrategyType],
        "EngineVersion": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CreateTagsRequestRequestTypeDef = TypedDict(
    "CreateTagsRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CreateUserRequestRequestTypeDef = TypedDict(
    "CreateUserRequestRequestTypeDef",
    {
        "BrokerId": str,
        "Password": str,
        "Username": str,
        "ConsoleAccess": NotRequired[bool],
        "Groups": NotRequired[Sequence[str]],
        "ReplicationUser": NotRequired[bool],
    },
)
DataReplicationCounterpartTypeDef = TypedDict(
    "DataReplicationCounterpartTypeDef",
    {
        "BrokerId": str,
        "Region": str,
    },
)
DeleteBrokerRequestRequestTypeDef = TypedDict(
    "DeleteBrokerRequestRequestTypeDef",
    {
        "BrokerId": str,
    },
)
DeleteTagsRequestRequestTypeDef = TypedDict(
    "DeleteTagsRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "BrokerId": str,
        "Username": str,
    },
)
DescribeBrokerEngineTypesRequestRequestTypeDef = TypedDict(
    "DescribeBrokerEngineTypesRequestRequestTypeDef",
    {
        "EngineType": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeBrokerInstanceOptionsRequestRequestTypeDef = TypedDict(
    "DescribeBrokerInstanceOptionsRequestRequestTypeDef",
    {
        "EngineType": NotRequired[str],
        "HostInstanceType": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "StorageType": NotRequired[str],
    },
)
DescribeBrokerRequestRequestTypeDef = TypedDict(
    "DescribeBrokerRequestRequestTypeDef",
    {
        "BrokerId": str,
    },
)
LdapServerMetadataOutputTypeDef = TypedDict(
    "LdapServerMetadataOutputTypeDef",
    {
        "Hosts": List[str],
        "RoleBase": str,
        "RoleSearchMatching": str,
        "ServiceAccountUsername": str,
        "UserBase": str,
        "UserSearchMatching": str,
        "RoleName": NotRequired[str],
        "RoleSearchSubtree": NotRequired[bool],
        "UserRoleName": NotRequired[str],
        "UserSearchSubtree": NotRequired[bool],
    },
)
UserSummaryTypeDef = TypedDict(
    "UserSummaryTypeDef",
    {
        "Username": str,
        "PendingChange": NotRequired[ChangeTypeType],
    },
)
DescribeConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationRequestRequestTypeDef",
    {
        "ConfigurationId": str,
    },
)
DescribeConfigurationRevisionRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationRevisionRequestRequestTypeDef",
    {
        "ConfigurationId": str,
        "ConfigurationRevision": str,
    },
)
DescribeUserRequestRequestTypeDef = TypedDict(
    "DescribeUserRequestRequestTypeDef",
    {
        "BrokerId": str,
        "Username": str,
    },
)
UserPendingChangesTypeDef = TypedDict(
    "UserPendingChangesTypeDef",
    {
        "PendingChange": ChangeTypeType,
        "ConsoleAccess": NotRequired[bool],
        "Groups": NotRequired[List[str]],
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
ListBrokersRequestRequestTypeDef = TypedDict(
    "ListBrokersRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListConfigurationRevisionsRequestRequestTypeDef = TypedDict(
    "ListConfigurationRevisionsRequestRequestTypeDef",
    {
        "ConfigurationId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListConfigurationsRequestRequestTypeDef = TypedDict(
    "ListConfigurationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTagsRequestRequestTypeDef = TypedDict(
    "ListTagsRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
ListUsersRequestRequestTypeDef = TypedDict(
    "ListUsersRequestRequestTypeDef",
    {
        "BrokerId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
PendingLogsTypeDef = TypedDict(
    "PendingLogsTypeDef",
    {
        "Audit": NotRequired[bool],
        "General": NotRequired[bool],
    },
)
PromoteRequestRequestTypeDef = TypedDict(
    "PromoteRequestRequestTypeDef",
    {
        "BrokerId": str,
        "Mode": PromoteModeType,
    },
)
RebootBrokerRequestRequestTypeDef = TypedDict(
    "RebootBrokerRequestRequestTypeDef",
    {
        "BrokerId": str,
    },
)
SanitizationWarningTypeDef = TypedDict(
    "SanitizationWarningTypeDef",
    {
        "Reason": SanitizationWarningReasonType,
        "AttributeName": NotRequired[str],
        "ElementName": NotRequired[str],
    },
)
UpdateConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateConfigurationRequestRequestTypeDef",
    {
        "ConfigurationId": str,
        "Data": str,
        "Description": NotRequired[str],
    },
)
UpdateUserRequestRequestTypeDef = TypedDict(
    "UpdateUserRequestRequestTypeDef",
    {
        "BrokerId": str,
        "Username": str,
        "ConsoleAccess": NotRequired[bool],
        "Groups": NotRequired[Sequence[str]],
        "Password": NotRequired[str],
        "ReplicationUser": NotRequired[bool],
    },
)
BrokerInstanceOptionTypeDef = TypedDict(
    "BrokerInstanceOptionTypeDef",
    {
        "AvailabilityZones": NotRequired[List[AvailabilityZoneTypeDef]],
        "EngineType": NotRequired[EngineTypeType],
        "HostInstanceType": NotRequired[str],
        "StorageType": NotRequired[BrokerStorageTypeType],
        "SupportedDeploymentModes": NotRequired[List[DeploymentModeType]],
        "SupportedEngineVersions": NotRequired[List[str]],
    },
)
BrokerEngineTypeTypeDef = TypedDict(
    "BrokerEngineTypeTypeDef",
    {
        "EngineType": NotRequired[EngineTypeType],
        "EngineVersions": NotRequired[List[EngineVersionTypeDef]],
    },
)
ConfigurationsTypeDef = TypedDict(
    "ConfigurationsTypeDef",
    {
        "Current": NotRequired[ConfigurationIdTypeDef],
        "History": NotRequired[List[ConfigurationIdTypeDef]],
        "Pending": NotRequired[ConfigurationIdTypeDef],
    },
)
ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "Arn": str,
        "AuthenticationStrategy": AuthenticationStrategyType,
        "Created": datetime,
        "Description": str,
        "EngineType": EngineTypeType,
        "EngineVersion": str,
        "Id": str,
        "LatestRevision": ConfigurationRevisionTypeDef,
        "Name": str,
        "Tags": NotRequired[Dict[str, str]],
    },
)
CreateBrokerRequestRequestTypeDef = TypedDict(
    "CreateBrokerRequestRequestTypeDef",
    {
        "BrokerName": str,
        "DeploymentMode": DeploymentModeType,
        "EngineType": EngineTypeType,
        "HostInstanceType": str,
        "PubliclyAccessible": bool,
        "Users": Sequence[UserTypeDef],
        "AuthenticationStrategy": NotRequired[AuthenticationStrategyType],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "Configuration": NotRequired[ConfigurationIdTypeDef],
        "CreatorRequestId": NotRequired[str],
        "EncryptionOptions": NotRequired[EncryptionOptionsTypeDef],
        "EngineVersion": NotRequired[str],
        "LdapServerMetadata": NotRequired[LdapServerMetadataInputTypeDef],
        "Logs": NotRequired[LogsTypeDef],
        "MaintenanceWindowStartTime": NotRequired[WeeklyStartTimeTypeDef],
        "SecurityGroups": NotRequired[Sequence[str]],
        "StorageType": NotRequired[BrokerStorageTypeType],
        "SubnetIds": NotRequired[Sequence[str]],
        "Tags": NotRequired[Mapping[str, str]],
        "DataReplicationMode": NotRequired[DataReplicationModeType],
        "DataReplicationPrimaryBrokerArn": NotRequired[str],
    },
)
UpdateBrokerRequestRequestTypeDef = TypedDict(
    "UpdateBrokerRequestRequestTypeDef",
    {
        "BrokerId": str,
        "AuthenticationStrategy": NotRequired[AuthenticationStrategyType],
        "AutoMinorVersionUpgrade": NotRequired[bool],
        "Configuration": NotRequired[ConfigurationIdTypeDef],
        "EngineVersion": NotRequired[str],
        "HostInstanceType": NotRequired[str],
        "LdapServerMetadata": NotRequired[LdapServerMetadataInputTypeDef],
        "Logs": NotRequired[LogsTypeDef],
        "MaintenanceWindowStartTime": NotRequired[WeeklyStartTimeTypeDef],
        "SecurityGroups": NotRequired[Sequence[str]],
        "DataReplicationMode": NotRequired[DataReplicationModeType],
    },
)
CreateBrokerResponseTypeDef = TypedDict(
    "CreateBrokerResponseTypeDef",
    {
        "BrokerArn": str,
        "BrokerId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateConfigurationResponseTypeDef = TypedDict(
    "CreateConfigurationResponseTypeDef",
    {
        "Arn": str,
        "AuthenticationStrategy": AuthenticationStrategyType,
        "Created": datetime,
        "Id": str,
        "LatestRevision": ConfigurationRevisionTypeDef,
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteBrokerResponseTypeDef = TypedDict(
    "DeleteBrokerResponseTypeDef",
    {
        "BrokerId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeConfigurationResponseTypeDef = TypedDict(
    "DescribeConfigurationResponseTypeDef",
    {
        "Arn": str,
        "AuthenticationStrategy": AuthenticationStrategyType,
        "Created": datetime,
        "Description": str,
        "EngineType": EngineTypeType,
        "EngineVersion": str,
        "Id": str,
        "LatestRevision": ConfigurationRevisionTypeDef,
        "Name": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeConfigurationRevisionResponseTypeDef = TypedDict(
    "DescribeConfigurationRevisionResponseTypeDef",
    {
        "ConfigurationId": str,
        "Created": datetime,
        "Data": str,
        "Description": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListBrokersResponseTypeDef = TypedDict(
    "ListBrokersResponseTypeDef",
    {
        "BrokerSummaries": List[BrokerSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListConfigurationRevisionsResponseTypeDef = TypedDict(
    "ListConfigurationRevisionsResponseTypeDef",
    {
        "ConfigurationId": str,
        "MaxResults": int,
        "Revisions": List[ConfigurationRevisionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PromoteResponseTypeDef = TypedDict(
    "PromoteResponseTypeDef",
    {
        "BrokerId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DataReplicationMetadataOutputTypeDef = TypedDict(
    "DataReplicationMetadataOutputTypeDef",
    {
        "DataReplicationRole": str,
        "DataReplicationCounterpart": NotRequired[DataReplicationCounterpartTypeDef],
    },
)
ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "BrokerId": str,
        "MaxResults": int,
        "Users": List[UserSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeUserResponseTypeDef = TypedDict(
    "DescribeUserResponseTypeDef",
    {
        "BrokerId": str,
        "ConsoleAccess": bool,
        "Groups": List[str],
        "Pending": UserPendingChangesTypeDef,
        "Username": str,
        "ReplicationUser": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListBrokersRequestListBrokersPaginateTypeDef = TypedDict(
    "ListBrokersRequestListBrokersPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
LogsSummaryTypeDef = TypedDict(
    "LogsSummaryTypeDef",
    {
        "General": bool,
        "GeneralLogGroup": str,
        "Audit": NotRequired[bool],
        "AuditLogGroup": NotRequired[str],
        "Pending": NotRequired[PendingLogsTypeDef],
    },
)
UpdateConfigurationResponseTypeDef = TypedDict(
    "UpdateConfigurationResponseTypeDef",
    {
        "Arn": str,
        "Created": datetime,
        "Id": str,
        "LatestRevision": ConfigurationRevisionTypeDef,
        "Name": str,
        "Warnings": List[SanitizationWarningTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeBrokerInstanceOptionsResponseTypeDef = TypedDict(
    "DescribeBrokerInstanceOptionsResponseTypeDef",
    {
        "BrokerInstanceOptions": List[BrokerInstanceOptionTypeDef],
        "MaxResults": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeBrokerEngineTypesResponseTypeDef = TypedDict(
    "DescribeBrokerEngineTypesResponseTypeDef",
    {
        "BrokerEngineTypes": List[BrokerEngineTypeTypeDef],
        "MaxResults": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListConfigurationsResponseTypeDef = TypedDict(
    "ListConfigurationsResponseTypeDef",
    {
        "Configurations": List[ConfigurationTypeDef],
        "MaxResults": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateBrokerResponseTypeDef = TypedDict(
    "UpdateBrokerResponseTypeDef",
    {
        "AuthenticationStrategy": AuthenticationStrategyType,
        "AutoMinorVersionUpgrade": bool,
        "BrokerId": str,
        "Configuration": ConfigurationIdTypeDef,
        "EngineVersion": str,
        "HostInstanceType": str,
        "LdapServerMetadata": LdapServerMetadataOutputTypeDef,
        "Logs": LogsTypeDef,
        "MaintenanceWindowStartTime": WeeklyStartTimeTypeDef,
        "SecurityGroups": List[str],
        "DataReplicationMetadata": DataReplicationMetadataOutputTypeDef,
        "DataReplicationMode": DataReplicationModeType,
        "PendingDataReplicationMetadata": DataReplicationMetadataOutputTypeDef,
        "PendingDataReplicationMode": DataReplicationModeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeBrokerResponseTypeDef = TypedDict(
    "DescribeBrokerResponseTypeDef",
    {
        "ActionsRequired": List[ActionRequiredTypeDef],
        "AuthenticationStrategy": AuthenticationStrategyType,
        "AutoMinorVersionUpgrade": bool,
        "BrokerArn": str,
        "BrokerId": str,
        "BrokerInstances": List[BrokerInstanceTypeDef],
        "BrokerName": str,
        "BrokerState": BrokerStateType,
        "Configurations": ConfigurationsTypeDef,
        "Created": datetime,
        "DeploymentMode": DeploymentModeType,
        "EncryptionOptions": EncryptionOptionsTypeDef,
        "EngineType": EngineTypeType,
        "EngineVersion": str,
        "HostInstanceType": str,
        "LdapServerMetadata": LdapServerMetadataOutputTypeDef,
        "Logs": LogsSummaryTypeDef,
        "MaintenanceWindowStartTime": WeeklyStartTimeTypeDef,
        "PendingAuthenticationStrategy": AuthenticationStrategyType,
        "PendingEngineVersion": str,
        "PendingHostInstanceType": str,
        "PendingLdapServerMetadata": LdapServerMetadataOutputTypeDef,
        "PendingSecurityGroups": List[str],
        "PubliclyAccessible": bool,
        "SecurityGroups": List[str],
        "StorageType": BrokerStorageTypeType,
        "SubnetIds": List[str],
        "Tags": Dict[str, str],
        "Users": List[UserSummaryTypeDef],
        "DataReplicationMetadata": DataReplicationMetadataOutputTypeDef,
        "DataReplicationMode": DataReplicationModeType,
        "PendingDataReplicationMetadata": DataReplicationMetadataOutputTypeDef,
        "PendingDataReplicationMode": DataReplicationModeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
