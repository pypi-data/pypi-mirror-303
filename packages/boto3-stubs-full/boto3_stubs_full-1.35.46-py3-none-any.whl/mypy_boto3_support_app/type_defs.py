"""
Type annotations for support-app service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support_app/type_defs/)

Usage::

    ```python
    from mypy_boto3_support_app.type_defs import CreateSlackChannelConfigurationRequestRequestTypeDef

    data: CreateSlackChannelConfigurationRequestRequestTypeDef = ...
    ```
"""

import sys
from typing import Dict, List

from .literals import AccountTypeType, NotificationSeverityLevelType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "CreateSlackChannelConfigurationRequestRequestTypeDef",
    "DeleteSlackChannelConfigurationRequestRequestTypeDef",
    "DeleteSlackWorkspaceConfigurationRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "ListSlackChannelConfigurationsRequestRequestTypeDef",
    "SlackChannelConfigurationTypeDef",
    "ListSlackWorkspaceConfigurationsRequestRequestTypeDef",
    "SlackWorkspaceConfigurationTypeDef",
    "PutAccountAliasRequestRequestTypeDef",
    "RegisterSlackWorkspaceForOrganizationRequestRequestTypeDef",
    "UpdateSlackChannelConfigurationRequestRequestTypeDef",
    "GetAccountAliasResultTypeDef",
    "RegisterSlackWorkspaceForOrganizationResultTypeDef",
    "UpdateSlackChannelConfigurationResultTypeDef",
    "ListSlackChannelConfigurationsResultTypeDef",
    "ListSlackWorkspaceConfigurationsResultTypeDef",
)

CreateSlackChannelConfigurationRequestRequestTypeDef = TypedDict(
    "CreateSlackChannelConfigurationRequestRequestTypeDef",
    {
        "channelId": str,
        "channelRoleArn": str,
        "notifyOnCaseSeverity": NotificationSeverityLevelType,
        "teamId": str,
        "channelName": NotRequired[str],
        "notifyOnAddCorrespondenceToCase": NotRequired[bool],
        "notifyOnCreateOrReopenCase": NotRequired[bool],
        "notifyOnResolveCase": NotRequired[bool],
    },
)
DeleteSlackChannelConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteSlackChannelConfigurationRequestRequestTypeDef",
    {
        "channelId": str,
        "teamId": str,
    },
)
DeleteSlackWorkspaceConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteSlackWorkspaceConfigurationRequestRequestTypeDef",
    {
        "teamId": str,
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
ListSlackChannelConfigurationsRequestRequestTypeDef = TypedDict(
    "ListSlackChannelConfigurationsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
    },
)
SlackChannelConfigurationTypeDef = TypedDict(
    "SlackChannelConfigurationTypeDef",
    {
        "channelId": str,
        "teamId": str,
        "channelName": NotRequired[str],
        "channelRoleArn": NotRequired[str],
        "notifyOnAddCorrespondenceToCase": NotRequired[bool],
        "notifyOnCaseSeverity": NotRequired[NotificationSeverityLevelType],
        "notifyOnCreateOrReopenCase": NotRequired[bool],
        "notifyOnResolveCase": NotRequired[bool],
    },
)
ListSlackWorkspaceConfigurationsRequestRequestTypeDef = TypedDict(
    "ListSlackWorkspaceConfigurationsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
    },
)
SlackWorkspaceConfigurationTypeDef = TypedDict(
    "SlackWorkspaceConfigurationTypeDef",
    {
        "teamId": str,
        "allowOrganizationMemberAccount": NotRequired[bool],
        "teamName": NotRequired[str],
    },
)
PutAccountAliasRequestRequestTypeDef = TypedDict(
    "PutAccountAliasRequestRequestTypeDef",
    {
        "accountAlias": str,
    },
)
RegisterSlackWorkspaceForOrganizationRequestRequestTypeDef = TypedDict(
    "RegisterSlackWorkspaceForOrganizationRequestRequestTypeDef",
    {
        "teamId": str,
    },
)
UpdateSlackChannelConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateSlackChannelConfigurationRequestRequestTypeDef",
    {
        "channelId": str,
        "teamId": str,
        "channelName": NotRequired[str],
        "channelRoleArn": NotRequired[str],
        "notifyOnAddCorrespondenceToCase": NotRequired[bool],
        "notifyOnCaseSeverity": NotRequired[NotificationSeverityLevelType],
        "notifyOnCreateOrReopenCase": NotRequired[bool],
        "notifyOnResolveCase": NotRequired[bool],
    },
)
GetAccountAliasResultTypeDef = TypedDict(
    "GetAccountAliasResultTypeDef",
    {
        "accountAlias": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterSlackWorkspaceForOrganizationResultTypeDef = TypedDict(
    "RegisterSlackWorkspaceForOrganizationResultTypeDef",
    {
        "accountType": AccountTypeType,
        "teamId": str,
        "teamName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSlackChannelConfigurationResultTypeDef = TypedDict(
    "UpdateSlackChannelConfigurationResultTypeDef",
    {
        "channelId": str,
        "channelName": str,
        "channelRoleArn": str,
        "notifyOnAddCorrespondenceToCase": bool,
        "notifyOnCaseSeverity": NotificationSeverityLevelType,
        "notifyOnCreateOrReopenCase": bool,
        "notifyOnResolveCase": bool,
        "teamId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSlackChannelConfigurationsResultTypeDef = TypedDict(
    "ListSlackChannelConfigurationsResultTypeDef",
    {
        "nextToken": str,
        "slackChannelConfigurations": List[SlackChannelConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSlackWorkspaceConfigurationsResultTypeDef = TypedDict(
    "ListSlackWorkspaceConfigurationsResultTypeDef",
    {
        "nextToken": str,
        "slackWorkspaceConfigurations": List[SlackWorkspaceConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
