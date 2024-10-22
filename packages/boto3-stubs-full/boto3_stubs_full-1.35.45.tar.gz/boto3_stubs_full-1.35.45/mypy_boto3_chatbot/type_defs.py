"""
Type annotations for chatbot service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/type_defs/)

Usage::

    ```python
    from mypy_boto3_chatbot.type_defs import AccountPreferencesTypeDef

    data: AccountPreferencesTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Sequence

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "AccountPreferencesTypeDef",
    "TagTypeDef",
    "ConfiguredTeamTypeDef",
    "ResponseMetadataTypeDef",
    "DeleteChimeWebhookConfigurationRequestRequestTypeDef",
    "DeleteMicrosoftTeamsUserIdentityRequestRequestTypeDef",
    "DeleteSlackChannelConfigurationRequestRequestTypeDef",
    "DeleteSlackUserIdentityRequestRequestTypeDef",
    "DeleteSlackWorkspaceAuthorizationRequestRequestTypeDef",
    "DeleteTeamsChannelConfigurationRequestRequestTypeDef",
    "DeleteTeamsConfiguredTeamRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeChimeWebhookConfigurationsRequestRequestTypeDef",
    "DescribeSlackChannelConfigurationsRequestRequestTypeDef",
    "DescribeSlackUserIdentitiesRequestRequestTypeDef",
    "SlackUserIdentityTypeDef",
    "DescribeSlackWorkspacesRequestRequestTypeDef",
    "SlackWorkspaceTypeDef",
    "GetTeamsChannelConfigurationRequestRequestTypeDef",
    "ListMicrosoftTeamsConfiguredTeamsRequestRequestTypeDef",
    "ListMicrosoftTeamsUserIdentitiesRequestRequestTypeDef",
    "TeamsUserIdentityTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTeamsChannelConfigurationsRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAccountPreferencesRequestRequestTypeDef",
    "UpdateChimeWebhookConfigurationRequestRequestTypeDef",
    "UpdateSlackChannelConfigurationRequestRequestTypeDef",
    "UpdateTeamsChannelConfigurationRequestRequestTypeDef",
    "ChimeWebhookConfigurationTypeDef",
    "CreateChimeWebhookConfigurationRequestRequestTypeDef",
    "CreateSlackChannelConfigurationRequestRequestTypeDef",
    "CreateTeamsChannelConfigurationRequestRequestTypeDef",
    "SlackChannelConfigurationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TeamsChannelConfigurationTypeDef",
    "GetAccountPreferencesResultTypeDef",
    "ListMicrosoftTeamsConfiguredTeamsResultTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "UpdateAccountPreferencesResultTypeDef",
    "DescribeChimeWebhookConfigurationsRequestDescribeChimeWebhookConfigurationsPaginateTypeDef",
    "DescribeSlackChannelConfigurationsRequestDescribeSlackChannelConfigurationsPaginateTypeDef",
    "DescribeSlackUserIdentitiesRequestDescribeSlackUserIdentitiesPaginateTypeDef",
    "DescribeSlackWorkspacesRequestDescribeSlackWorkspacesPaginateTypeDef",
    "ListMicrosoftTeamsConfiguredTeamsRequestListMicrosoftTeamsConfiguredTeamsPaginateTypeDef",
    "ListMicrosoftTeamsUserIdentitiesRequestListMicrosoftTeamsUserIdentitiesPaginateTypeDef",
    "ListTeamsChannelConfigurationsRequestListMicrosoftTeamsChannelConfigurationsPaginateTypeDef",
    "DescribeSlackUserIdentitiesResultTypeDef",
    "DescribeSlackWorkspacesResultTypeDef",
    "ListMicrosoftTeamsUserIdentitiesResultTypeDef",
    "CreateChimeWebhookConfigurationResultTypeDef",
    "DescribeChimeWebhookConfigurationsResultTypeDef",
    "UpdateChimeWebhookConfigurationResultTypeDef",
    "CreateSlackChannelConfigurationResultTypeDef",
    "DescribeSlackChannelConfigurationsResultTypeDef",
    "UpdateSlackChannelConfigurationResultTypeDef",
    "CreateTeamsChannelConfigurationResultTypeDef",
    "GetTeamsChannelConfigurationResultTypeDef",
    "ListTeamsChannelConfigurationsResultTypeDef",
    "UpdateTeamsChannelConfigurationResultTypeDef",
)

AccountPreferencesTypeDef = TypedDict(
    "AccountPreferencesTypeDef",
    {
        "UserAuthorizationRequired": NotRequired[bool],
        "TrainingDataCollectionEnabled": NotRequired[bool],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "TagKey": str,
        "TagValue": str,
    },
)
ConfiguredTeamTypeDef = TypedDict(
    "ConfiguredTeamTypeDef",
    {
        "TenantId": str,
        "TeamId": str,
        "TeamName": NotRequired[str],
        "State": NotRequired[str],
        "StateReason": NotRequired[str],
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
DeleteChimeWebhookConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteChimeWebhookConfigurationRequestRequestTypeDef",
    {
        "ChatConfigurationArn": str,
    },
)
DeleteMicrosoftTeamsUserIdentityRequestRequestTypeDef = TypedDict(
    "DeleteMicrosoftTeamsUserIdentityRequestRequestTypeDef",
    {
        "ChatConfigurationArn": str,
        "UserId": str,
    },
)
DeleteSlackChannelConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteSlackChannelConfigurationRequestRequestTypeDef",
    {
        "ChatConfigurationArn": str,
    },
)
DeleteSlackUserIdentityRequestRequestTypeDef = TypedDict(
    "DeleteSlackUserIdentityRequestRequestTypeDef",
    {
        "ChatConfigurationArn": str,
        "SlackTeamId": str,
        "SlackUserId": str,
    },
)
DeleteSlackWorkspaceAuthorizationRequestRequestTypeDef = TypedDict(
    "DeleteSlackWorkspaceAuthorizationRequestRequestTypeDef",
    {
        "SlackTeamId": str,
    },
)
DeleteTeamsChannelConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteTeamsChannelConfigurationRequestRequestTypeDef",
    {
        "ChatConfigurationArn": str,
    },
)
DeleteTeamsConfiguredTeamRequestRequestTypeDef = TypedDict(
    "DeleteTeamsConfiguredTeamRequestRequestTypeDef",
    {
        "TeamId": str,
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
DescribeChimeWebhookConfigurationsRequestRequestTypeDef = TypedDict(
    "DescribeChimeWebhookConfigurationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ChatConfigurationArn": NotRequired[str],
    },
)
DescribeSlackChannelConfigurationsRequestRequestTypeDef = TypedDict(
    "DescribeSlackChannelConfigurationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ChatConfigurationArn": NotRequired[str],
    },
)
DescribeSlackUserIdentitiesRequestRequestTypeDef = TypedDict(
    "DescribeSlackUserIdentitiesRequestRequestTypeDef",
    {
        "ChatConfigurationArn": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
SlackUserIdentityTypeDef = TypedDict(
    "SlackUserIdentityTypeDef",
    {
        "IamRoleArn": str,
        "ChatConfigurationArn": str,
        "SlackTeamId": str,
        "SlackUserId": str,
        "AwsUserIdentity": NotRequired[str],
    },
)
DescribeSlackWorkspacesRequestRequestTypeDef = TypedDict(
    "DescribeSlackWorkspacesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
SlackWorkspaceTypeDef = TypedDict(
    "SlackWorkspaceTypeDef",
    {
        "SlackTeamId": str,
        "SlackTeamName": str,
        "State": NotRequired[str],
        "StateReason": NotRequired[str],
    },
)
GetTeamsChannelConfigurationRequestRequestTypeDef = TypedDict(
    "GetTeamsChannelConfigurationRequestRequestTypeDef",
    {
        "ChatConfigurationArn": str,
    },
)
ListMicrosoftTeamsConfiguredTeamsRequestRequestTypeDef = TypedDict(
    "ListMicrosoftTeamsConfiguredTeamsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListMicrosoftTeamsUserIdentitiesRequestRequestTypeDef = TypedDict(
    "ListMicrosoftTeamsUserIdentitiesRequestRequestTypeDef",
    {
        "ChatConfigurationArn": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
TeamsUserIdentityTypeDef = TypedDict(
    "TeamsUserIdentityTypeDef",
    {
        "IamRoleArn": str,
        "ChatConfigurationArn": str,
        "TeamId": str,
        "UserId": NotRequired[str],
        "AwsUserIdentity": NotRequired[str],
        "TeamsChannelId": NotRequired[str],
        "TeamsTenantId": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
ListTeamsChannelConfigurationsRequestRequestTypeDef = TypedDict(
    "ListTeamsChannelConfigurationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "TeamId": NotRequired[str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
UpdateAccountPreferencesRequestRequestTypeDef = TypedDict(
    "UpdateAccountPreferencesRequestRequestTypeDef",
    {
        "UserAuthorizationRequired": NotRequired[bool],
        "TrainingDataCollectionEnabled": NotRequired[bool],
    },
)
UpdateChimeWebhookConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateChimeWebhookConfigurationRequestRequestTypeDef",
    {
        "ChatConfigurationArn": str,
        "WebhookDescription": NotRequired[str],
        "WebhookUrl": NotRequired[str],
        "SnsTopicArns": NotRequired[Sequence[str]],
        "IamRoleArn": NotRequired[str],
        "LoggingLevel": NotRequired[str],
    },
)
UpdateSlackChannelConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateSlackChannelConfigurationRequestRequestTypeDef",
    {
        "ChatConfigurationArn": str,
        "SlackChannelId": str,
        "SlackChannelName": NotRequired[str],
        "SnsTopicArns": NotRequired[Sequence[str]],
        "IamRoleArn": NotRequired[str],
        "LoggingLevel": NotRequired[str],
        "GuardrailPolicyArns": NotRequired[Sequence[str]],
        "UserAuthorizationRequired": NotRequired[bool],
    },
)
UpdateTeamsChannelConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateTeamsChannelConfigurationRequestRequestTypeDef",
    {
        "ChatConfigurationArn": str,
        "ChannelId": str,
        "ChannelName": NotRequired[str],
        "SnsTopicArns": NotRequired[Sequence[str]],
        "IamRoleArn": NotRequired[str],
        "LoggingLevel": NotRequired[str],
        "GuardrailPolicyArns": NotRequired[Sequence[str]],
        "UserAuthorizationRequired": NotRequired[bool],
    },
)
ChimeWebhookConfigurationTypeDef = TypedDict(
    "ChimeWebhookConfigurationTypeDef",
    {
        "WebhookDescription": str,
        "ChatConfigurationArn": str,
        "IamRoleArn": str,
        "SnsTopicArns": List[str],
        "ConfigurationName": NotRequired[str],
        "LoggingLevel": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "State": NotRequired[str],
        "StateReason": NotRequired[str],
    },
)
CreateChimeWebhookConfigurationRequestRequestTypeDef = TypedDict(
    "CreateChimeWebhookConfigurationRequestRequestTypeDef",
    {
        "WebhookDescription": str,
        "WebhookUrl": str,
        "SnsTopicArns": Sequence[str],
        "IamRoleArn": str,
        "ConfigurationName": str,
        "LoggingLevel": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateSlackChannelConfigurationRequestRequestTypeDef = TypedDict(
    "CreateSlackChannelConfigurationRequestRequestTypeDef",
    {
        "SlackTeamId": str,
        "SlackChannelId": str,
        "IamRoleArn": str,
        "ConfigurationName": str,
        "SlackChannelName": NotRequired[str],
        "SnsTopicArns": NotRequired[Sequence[str]],
        "LoggingLevel": NotRequired[str],
        "GuardrailPolicyArns": NotRequired[Sequence[str]],
        "UserAuthorizationRequired": NotRequired[bool],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateTeamsChannelConfigurationRequestRequestTypeDef = TypedDict(
    "CreateTeamsChannelConfigurationRequestRequestTypeDef",
    {
        "ChannelId": str,
        "TeamId": str,
        "TenantId": str,
        "IamRoleArn": str,
        "ConfigurationName": str,
        "ChannelName": NotRequired[str],
        "TeamName": NotRequired[str],
        "SnsTopicArns": NotRequired[Sequence[str]],
        "LoggingLevel": NotRequired[str],
        "GuardrailPolicyArns": NotRequired[Sequence[str]],
        "UserAuthorizationRequired": NotRequired[bool],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
SlackChannelConfigurationTypeDef = TypedDict(
    "SlackChannelConfigurationTypeDef",
    {
        "SlackTeamName": str,
        "SlackTeamId": str,
        "SlackChannelId": str,
        "SlackChannelName": str,
        "ChatConfigurationArn": str,
        "IamRoleArn": str,
        "SnsTopicArns": List[str],
        "ConfigurationName": NotRequired[str],
        "LoggingLevel": NotRequired[str],
        "GuardrailPolicyArns": NotRequired[List[str]],
        "UserAuthorizationRequired": NotRequired[bool],
        "Tags": NotRequired[List[TagTypeDef]],
        "State": NotRequired[str],
        "StateReason": NotRequired[str],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)
TeamsChannelConfigurationTypeDef = TypedDict(
    "TeamsChannelConfigurationTypeDef",
    {
        "ChannelId": str,
        "TeamId": str,
        "TenantId": str,
        "ChatConfigurationArn": str,
        "IamRoleArn": str,
        "SnsTopicArns": List[str],
        "ChannelName": NotRequired[str],
        "TeamName": NotRequired[str],
        "ConfigurationName": NotRequired[str],
        "LoggingLevel": NotRequired[str],
        "GuardrailPolicyArns": NotRequired[List[str]],
        "UserAuthorizationRequired": NotRequired[bool],
        "Tags": NotRequired[List[TagTypeDef]],
        "State": NotRequired[str],
        "StateReason": NotRequired[str],
    },
)
GetAccountPreferencesResultTypeDef = TypedDict(
    "GetAccountPreferencesResultTypeDef",
    {
        "AccountPreferences": AccountPreferencesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListMicrosoftTeamsConfiguredTeamsResultTypeDef = TypedDict(
    "ListMicrosoftTeamsConfiguredTeamsResultTypeDef",
    {
        "ConfiguredTeams": List[ConfiguredTeamTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAccountPreferencesResultTypeDef = TypedDict(
    "UpdateAccountPreferencesResultTypeDef",
    {
        "AccountPreferences": AccountPreferencesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeChimeWebhookConfigurationsRequestDescribeChimeWebhookConfigurationsPaginateTypeDef = TypedDict(
    "DescribeChimeWebhookConfigurationsRequestDescribeChimeWebhookConfigurationsPaginateTypeDef",
    {
        "ChatConfigurationArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeSlackChannelConfigurationsRequestDescribeSlackChannelConfigurationsPaginateTypeDef = TypedDict(
    "DescribeSlackChannelConfigurationsRequestDescribeSlackChannelConfigurationsPaginateTypeDef",
    {
        "ChatConfigurationArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeSlackUserIdentitiesRequestDescribeSlackUserIdentitiesPaginateTypeDef = TypedDict(
    "DescribeSlackUserIdentitiesRequestDescribeSlackUserIdentitiesPaginateTypeDef",
    {
        "ChatConfigurationArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeSlackWorkspacesRequestDescribeSlackWorkspacesPaginateTypeDef = TypedDict(
    "DescribeSlackWorkspacesRequestDescribeSlackWorkspacesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMicrosoftTeamsConfiguredTeamsRequestListMicrosoftTeamsConfiguredTeamsPaginateTypeDef = (
    TypedDict(
        "ListMicrosoftTeamsConfiguredTeamsRequestListMicrosoftTeamsConfiguredTeamsPaginateTypeDef",
        {
            "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
        },
    )
)
ListMicrosoftTeamsUserIdentitiesRequestListMicrosoftTeamsUserIdentitiesPaginateTypeDef = TypedDict(
    "ListMicrosoftTeamsUserIdentitiesRequestListMicrosoftTeamsUserIdentitiesPaginateTypeDef",
    {
        "ChatConfigurationArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTeamsChannelConfigurationsRequestListMicrosoftTeamsChannelConfigurationsPaginateTypeDef = TypedDict(
    "ListTeamsChannelConfigurationsRequestListMicrosoftTeamsChannelConfigurationsPaginateTypeDef",
    {
        "TeamId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeSlackUserIdentitiesResultTypeDef = TypedDict(
    "DescribeSlackUserIdentitiesResultTypeDef",
    {
        "SlackUserIdentities": List[SlackUserIdentityTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeSlackWorkspacesResultTypeDef = TypedDict(
    "DescribeSlackWorkspacesResultTypeDef",
    {
        "SlackWorkspaces": List[SlackWorkspaceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListMicrosoftTeamsUserIdentitiesResultTypeDef = TypedDict(
    "ListMicrosoftTeamsUserIdentitiesResultTypeDef",
    {
        "TeamsUserIdentities": List[TeamsUserIdentityTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateChimeWebhookConfigurationResultTypeDef = TypedDict(
    "CreateChimeWebhookConfigurationResultTypeDef",
    {
        "WebhookConfiguration": ChimeWebhookConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeChimeWebhookConfigurationsResultTypeDef = TypedDict(
    "DescribeChimeWebhookConfigurationsResultTypeDef",
    {
        "WebhookConfigurations": List[ChimeWebhookConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateChimeWebhookConfigurationResultTypeDef = TypedDict(
    "UpdateChimeWebhookConfigurationResultTypeDef",
    {
        "WebhookConfiguration": ChimeWebhookConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSlackChannelConfigurationResultTypeDef = TypedDict(
    "CreateSlackChannelConfigurationResultTypeDef",
    {
        "ChannelConfiguration": SlackChannelConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSlackChannelConfigurationsResultTypeDef = TypedDict(
    "DescribeSlackChannelConfigurationsResultTypeDef",
    {
        "SlackChannelConfigurations": List[SlackChannelConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateSlackChannelConfigurationResultTypeDef = TypedDict(
    "UpdateSlackChannelConfigurationResultTypeDef",
    {
        "ChannelConfiguration": SlackChannelConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTeamsChannelConfigurationResultTypeDef = TypedDict(
    "CreateTeamsChannelConfigurationResultTypeDef",
    {
        "ChannelConfiguration": TeamsChannelConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTeamsChannelConfigurationResultTypeDef = TypedDict(
    "GetTeamsChannelConfigurationResultTypeDef",
    {
        "ChannelConfiguration": TeamsChannelConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTeamsChannelConfigurationsResultTypeDef = TypedDict(
    "ListTeamsChannelConfigurationsResultTypeDef",
    {
        "TeamChannelConfigurations": List[TeamsChannelConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateTeamsChannelConfigurationResultTypeDef = TypedDict(
    "UpdateTeamsChannelConfigurationResultTypeDef",
    {
        "ChannelConfiguration": TeamsChannelConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
