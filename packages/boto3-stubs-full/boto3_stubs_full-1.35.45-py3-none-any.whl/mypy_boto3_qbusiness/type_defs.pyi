"""
Type annotations for qbusiness service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qbusiness/type_defs/)

Usage::

    ```python
    from mypy_boto3_qbusiness.type_defs import S3TypeDef

    data: S3TypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    ActionPayloadFieldTypeType,
    ApplicationStatusType,
    AttachmentsControlModeType,
    AttachmentStatusType,
    AttributeTypeType,
    AutoSubscriptionStatusType,
    ChatModeType,
    ContentTypeType,
    CreatorModeControlType,
    DataSourceStatusType,
    DataSourceSyncJobStatusType,
    DocumentAttributeBoostingLevelType,
    DocumentEnrichmentConditionOperatorType,
    DocumentStatusType,
    ErrorCodeType,
    GroupStatusType,
    IdentityTypeType,
    IndexStatusType,
    IndexTypeType,
    MemberRelationType,
    MembershipTypeType,
    MessageTypeType,
    MessageUsefulnessReasonType,
    MessageUsefulnessType,
    NumberAttributeBoostingTypeType,
    PersonalizationControlModeType,
    PluginBuildStatusType,
    PluginStateType,
    PluginTypeType,
    QAppsControlModeType,
    ReadAccessTypeType,
    ResponseScopeType,
    RetrieverStatusType,
    RetrieverTypeType,
    RuleTypeType,
    StatusType,
    StringAttributeValueBoostingLevelType,
    SubscriptionTypeType,
    WebExperienceSamplePromptsControlModeType,
    WebExperienceStatusType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "S3TypeDef",
    "ActionExecutionPayloadFieldOutputTypeDef",
    "ActionExecutionPayloadFieldTypeDef",
    "ActionReviewPayloadFieldAllowedValueTypeDef",
    "ApplicationTypeDef",
    "AppliedAttachmentsConfigurationTypeDef",
    "AppliedCreatorModeConfigurationTypeDef",
    "BlobTypeDef",
    "ErrorDetailTypeDef",
    "AttachmentsConfigurationTypeDef",
    "AuthChallengeRequestTypeDef",
    "AuthChallengeResponseTypeDef",
    "AutoSubscriptionConfigurationTypeDef",
    "BasicAuthConfigurationTypeDef",
    "DeleteDocumentTypeDef",
    "ResponseMetadataTypeDef",
    "BlockedPhrasesConfigurationTypeDef",
    "BlockedPhrasesConfigurationUpdateTypeDef",
    "PluginConfigurationTypeDef",
    "ContentBlockerRuleTypeDef",
    "EligibleDataSourceTypeDef",
    "ConversationTypeDef",
    "EncryptionConfigurationTypeDef",
    "PersonalizationConfigurationTypeDef",
    "QAppsConfigurationTypeDef",
    "TagTypeDef",
    "DataSourceVpcConfigurationTypeDef",
    "IndexCapacityConfigurationTypeDef",
    "UserAliasTypeDef",
    "CreatorModeConfigurationTypeDef",
    "DataSourceSyncJobMetricsTypeDef",
    "DataSourceTypeDef",
    "DataSourceVpcConfigurationOutputTypeDef",
    "DateAttributeBoostingConfigurationTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "DeleteChatControlsConfigurationRequestRequestTypeDef",
    "DeleteConversationRequestRequestTypeDef",
    "DeleteDataSourceRequestRequestTypeDef",
    "DeleteGroupRequestRequestTypeDef",
    "DeleteIndexRequestRequestTypeDef",
    "DeletePluginRequestRequestTypeDef",
    "DeleteRetrieverRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DeleteWebExperienceRequestRequestTypeDef",
    "NumberAttributeBoostingConfigurationTypeDef",
    "StringAttributeBoostingConfigurationOutputTypeDef",
    "StringListAttributeBoostingConfigurationTypeDef",
    "DocumentAttributeValueOutputTypeDef",
    "DocumentAttributeConfigurationTypeDef",
    "TimestampTypeDef",
    "GetApplicationRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "GetChatControlsConfigurationRequestRequestTypeDef",
    "GetDataSourceRequestRequestTypeDef",
    "GetGroupRequestRequestTypeDef",
    "GetIndexRequestRequestTypeDef",
    "GetPluginRequestRequestTypeDef",
    "GetRetrieverRequestRequestTypeDef",
    "GetUserRequestRequestTypeDef",
    "GetWebExperienceRequestRequestTypeDef",
    "MemberGroupTypeDef",
    "MemberUserTypeDef",
    "GroupSummaryTypeDef",
    "OpenIDConnectProviderConfigurationTypeDef",
    "SamlProviderConfigurationTypeDef",
    "TextDocumentStatisticsTypeDef",
    "IndexTypeDef",
    "KendraIndexConfigurationTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "ListConversationsRequestRequestTypeDef",
    "ListDataSourcesRequestRequestTypeDef",
    "ListDocumentsRequestRequestTypeDef",
    "ListIndicesRequestRequestTypeDef",
    "ListMessagesRequestRequestTypeDef",
    "ListPluginsRequestRequestTypeDef",
    "PluginTypeDef",
    "ListRetrieversRequestRequestTypeDef",
    "RetrieverTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListWebExperiencesRequestRequestTypeDef",
    "WebExperienceTypeDef",
    "OAuth2ClientCredentialConfigurationTypeDef",
    "PrincipalGroupTypeDef",
    "PrincipalUserTypeDef",
    "UsersAndGroupsOutputTypeDef",
    "SamlConfigurationTypeDef",
    "SnippetExcerptTypeDef",
    "StartDataSourceSyncJobRequestRequestTypeDef",
    "StopDataSourceSyncJobRequestRequestTypeDef",
    "StringAttributeBoostingConfigurationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UsersAndGroupsTypeDef",
    "APISchemaTypeDef",
    "ActionExecutionOutputTypeDef",
    "ActionExecutionPayloadFieldUnionTypeDef",
    "ActionReviewPayloadFieldTypeDef",
    "AttachmentInputTypeDef",
    "DocumentContentTypeDef",
    "AttachmentOutputTypeDef",
    "DocumentDetailsTypeDef",
    "FailedDocumentTypeDef",
    "GroupStatusDetailTypeDef",
    "BatchDeleteDocumentRequestRequestTypeDef",
    "CreateApplicationResponseTypeDef",
    "CreateDataSourceResponseTypeDef",
    "CreateIndexResponseTypeDef",
    "CreatePluginResponseTypeDef",
    "CreateRetrieverResponseTypeDef",
    "CreateWebExperienceResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ListApplicationsResponseTypeDef",
    "StartDataSourceSyncJobResponseTypeDef",
    "ChatModeConfigurationTypeDef",
    "ContentRetrievalRuleOutputTypeDef",
    "ContentRetrievalRuleTypeDef",
    "ListConversationsResponseTypeDef",
    "GetApplicationResponseTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateIndexRequestRequestTypeDef",
    "CreateUserRequestRequestTypeDef",
    "GetUserResponseTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "UpdateUserResponseTypeDef",
    "DataSourceSyncJobTypeDef",
    "ListDataSourcesResponseTypeDef",
    "DocumentAttributeBoostingConfigurationOutputTypeDef",
    "DocumentAttributeConditionOutputTypeDef",
    "DocumentAttributeTargetOutputTypeDef",
    "UpdateIndexRequestRequestTypeDef",
    "DocumentAttributeValueTypeDef",
    "ListDataSourceSyncJobsRequestRequestTypeDef",
    "ListGroupsRequestRequestTypeDef",
    "MessageUsefulnessFeedbackTypeDef",
    "GetChatControlsConfigurationRequestGetChatControlsConfigurationPaginateTypeDef",
    "ListApplicationsRequestListApplicationsPaginateTypeDef",
    "ListConversationsRequestListConversationsPaginateTypeDef",
    "ListDataSourceSyncJobsRequestListDataSourceSyncJobsPaginateTypeDef",
    "ListDataSourcesRequestListDataSourcesPaginateTypeDef",
    "ListDocumentsRequestListDocumentsPaginateTypeDef",
    "ListGroupsRequestListGroupsPaginateTypeDef",
    "ListIndicesRequestListIndicesPaginateTypeDef",
    "ListMessagesRequestListMessagesPaginateTypeDef",
    "ListPluginsRequestListPluginsPaginateTypeDef",
    "ListRetrieversRequestListRetrieversPaginateTypeDef",
    "ListWebExperiencesRequestListWebExperiencesPaginateTypeDef",
    "GroupMembersTypeDef",
    "ListGroupsResponseTypeDef",
    "IdentityProviderConfigurationTypeDef",
    "IndexStatisticsTypeDef",
    "ListIndicesResponseTypeDef",
    "ListPluginsResponseTypeDef",
    "ListRetrieversResponseTypeDef",
    "ListWebExperiencesResponseTypeDef",
    "PluginAuthConfigurationOutputTypeDef",
    "PluginAuthConfigurationTypeDef",
    "PrincipalTypeDef",
    "WebExperienceAuthConfigurationTypeDef",
    "TextSegmentTypeDef",
    "StringAttributeBoostingConfigurationUnionTypeDef",
    "UsersAndGroupsUnionTypeDef",
    "CustomPluginConfigurationTypeDef",
    "ActionExecutionTypeDef",
    "ActionReviewTypeDef",
    "ListDocumentsResponseTypeDef",
    "BatchDeleteDocumentResponseTypeDef",
    "BatchPutDocumentResponseTypeDef",
    "GetGroupResponseTypeDef",
    "RuleConfigurationOutputTypeDef",
    "ContentRetrievalRuleUnionTypeDef",
    "ListDataSourceSyncJobsResponseTypeDef",
    "NativeIndexConfigurationOutputTypeDef",
    "HookConfigurationOutputTypeDef",
    "InlineDocumentEnrichmentConfigurationOutputTypeDef",
    "DocumentAttributeValueUnionTypeDef",
    "PutFeedbackRequestRequestTypeDef",
    "PutGroupRequestRequestTypeDef",
    "CreateWebExperienceRequestRequestTypeDef",
    "GetIndexResponseTypeDef",
    "AccessControlTypeDef",
    "GetWebExperienceResponseTypeDef",
    "UpdateWebExperienceRequestRequestTypeDef",
    "SourceAttributionTypeDef",
    "DocumentAttributeBoostingConfigurationTypeDef",
    "CreatePluginRequestRequestTypeDef",
    "GetPluginResponseTypeDef",
    "UpdatePluginRequestRequestTypeDef",
    "RuleOutputTypeDef",
    "RuleConfigurationTypeDef",
    "RetrieverConfigurationOutputTypeDef",
    "DocumentEnrichmentConfigurationOutputTypeDef",
    "DocumentAttributeConditionTypeDef",
    "DocumentAttributeTargetTypeDef",
    "DocumentAttributeTypeDef",
    "AccessConfigurationTypeDef",
    "ChatSyncOutputTypeDef",
    "MessageTypeDef",
    "DocumentAttributeBoostingConfigurationUnionTypeDef",
    "TopicConfigurationOutputTypeDef",
    "RuleConfigurationUnionTypeDef",
    "GetRetrieverResponseTypeDef",
    "GetDataSourceResponseTypeDef",
    "DocumentAttributeConditionUnionTypeDef",
    "DocumentAttributeTargetUnionTypeDef",
    "AttributeFilterTypeDef",
    "ListMessagesResponseTypeDef",
    "NativeIndexConfigurationTypeDef",
    "GetChatControlsConfigurationResponseTypeDef",
    "RuleTypeDef",
    "HookConfigurationTypeDef",
    "InlineDocumentEnrichmentConfigurationTypeDef",
    "ChatSyncInputRequestTypeDef",
    "NativeIndexConfigurationUnionTypeDef",
    "RuleUnionTypeDef",
    "HookConfigurationUnionTypeDef",
    "InlineDocumentEnrichmentConfigurationUnionTypeDef",
    "RetrieverConfigurationTypeDef",
    "TopicConfigurationTypeDef",
    "DocumentEnrichmentConfigurationTypeDef",
    "CreateRetrieverRequestRequestTypeDef",
    "UpdateRetrieverRequestRequestTypeDef",
    "TopicConfigurationUnionTypeDef",
    "CreateDataSourceRequestRequestTypeDef",
    "DocumentEnrichmentConfigurationUnionTypeDef",
    "UpdateDataSourceRequestRequestTypeDef",
    "UpdateChatControlsConfigurationRequestRequestTypeDef",
    "DocumentTypeDef",
    "BatchPutDocumentRequestRequestTypeDef",
)

S3TypeDef = TypedDict(
    "S3TypeDef",
    {
        "bucket": str,
        "key": str,
    },
)
ActionExecutionPayloadFieldOutputTypeDef = TypedDict(
    "ActionExecutionPayloadFieldOutputTypeDef",
    {
        "value": Dict[str, Any],
    },
)
ActionExecutionPayloadFieldTypeDef = TypedDict(
    "ActionExecutionPayloadFieldTypeDef",
    {
        "value": Mapping[str, Any],
    },
)
ActionReviewPayloadFieldAllowedValueTypeDef = TypedDict(
    "ActionReviewPayloadFieldAllowedValueTypeDef",
    {
        "value": NotRequired[Dict[str, Any]],
        "displayValue": NotRequired[Dict[str, Any]],
    },
)
ApplicationTypeDef = TypedDict(
    "ApplicationTypeDef",
    {
        "displayName": NotRequired[str],
        "applicationId": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
        "status": NotRequired[ApplicationStatusType],
        "identityType": NotRequired[IdentityTypeType],
    },
)
AppliedAttachmentsConfigurationTypeDef = TypedDict(
    "AppliedAttachmentsConfigurationTypeDef",
    {
        "attachmentsControlMode": NotRequired[AttachmentsControlModeType],
    },
)
AppliedCreatorModeConfigurationTypeDef = TypedDict(
    "AppliedCreatorModeConfigurationTypeDef",
    {
        "creatorModeControl": CreatorModeControlType,
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef",
    {
        "errorMessage": NotRequired[str],
        "errorCode": NotRequired[ErrorCodeType],
    },
)
AttachmentsConfigurationTypeDef = TypedDict(
    "AttachmentsConfigurationTypeDef",
    {
        "attachmentsControlMode": AttachmentsControlModeType,
    },
)
AuthChallengeRequestTypeDef = TypedDict(
    "AuthChallengeRequestTypeDef",
    {
        "authorizationUrl": str,
    },
)
AuthChallengeResponseTypeDef = TypedDict(
    "AuthChallengeResponseTypeDef",
    {
        "responseMap": Mapping[str, str],
    },
)
AutoSubscriptionConfigurationTypeDef = TypedDict(
    "AutoSubscriptionConfigurationTypeDef",
    {
        "autoSubscribe": AutoSubscriptionStatusType,
        "defaultSubscriptionType": NotRequired[SubscriptionTypeType],
    },
)
BasicAuthConfigurationTypeDef = TypedDict(
    "BasicAuthConfigurationTypeDef",
    {
        "secretArn": str,
        "roleArn": str,
    },
)
DeleteDocumentTypeDef = TypedDict(
    "DeleteDocumentTypeDef",
    {
        "documentId": str,
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
BlockedPhrasesConfigurationTypeDef = TypedDict(
    "BlockedPhrasesConfigurationTypeDef",
    {
        "blockedPhrases": NotRequired[List[str]],
        "systemMessageOverride": NotRequired[str],
    },
)
BlockedPhrasesConfigurationUpdateTypeDef = TypedDict(
    "BlockedPhrasesConfigurationUpdateTypeDef",
    {
        "blockedPhrasesToCreateOrUpdate": NotRequired[Sequence[str]],
        "blockedPhrasesToDelete": NotRequired[Sequence[str]],
        "systemMessageOverride": NotRequired[str],
    },
)
PluginConfigurationTypeDef = TypedDict(
    "PluginConfigurationTypeDef",
    {
        "pluginId": str,
    },
)
ContentBlockerRuleTypeDef = TypedDict(
    "ContentBlockerRuleTypeDef",
    {
        "systemMessageOverride": NotRequired[str],
    },
)
EligibleDataSourceTypeDef = TypedDict(
    "EligibleDataSourceTypeDef",
    {
        "indexId": NotRequired[str],
        "dataSourceId": NotRequired[str],
    },
)
ConversationTypeDef = TypedDict(
    "ConversationTypeDef",
    {
        "conversationId": NotRequired[str],
        "title": NotRequired[str],
        "startTime": NotRequired[datetime],
    },
)
EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "kmsKeyId": NotRequired[str],
    },
)
PersonalizationConfigurationTypeDef = TypedDict(
    "PersonalizationConfigurationTypeDef",
    {
        "personalizationControlMode": PersonalizationControlModeType,
    },
)
QAppsConfigurationTypeDef = TypedDict(
    "QAppsConfigurationTypeDef",
    {
        "qAppsControlMode": QAppsControlModeType,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)
DataSourceVpcConfigurationTypeDef = TypedDict(
    "DataSourceVpcConfigurationTypeDef",
    {
        "subnetIds": Sequence[str],
        "securityGroupIds": Sequence[str],
    },
)
IndexCapacityConfigurationTypeDef = TypedDict(
    "IndexCapacityConfigurationTypeDef",
    {
        "units": NotRequired[int],
    },
)
UserAliasTypeDef = TypedDict(
    "UserAliasTypeDef",
    {
        "userId": str,
        "indexId": NotRequired[str],
        "dataSourceId": NotRequired[str],
    },
)
CreatorModeConfigurationTypeDef = TypedDict(
    "CreatorModeConfigurationTypeDef",
    {
        "creatorModeControl": CreatorModeControlType,
    },
)
DataSourceSyncJobMetricsTypeDef = TypedDict(
    "DataSourceSyncJobMetricsTypeDef",
    {
        "documentsAdded": NotRequired[str],
        "documentsModified": NotRequired[str],
        "documentsDeleted": NotRequired[str],
        "documentsFailed": NotRequired[str],
        "documentsScanned": NotRequired[str],
    },
)
DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "displayName": NotRequired[str],
        "dataSourceId": NotRequired[str],
        "type": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
        "status": NotRequired[DataSourceStatusType],
    },
)
DataSourceVpcConfigurationOutputTypeDef = TypedDict(
    "DataSourceVpcConfigurationOutputTypeDef",
    {
        "subnetIds": List[str],
        "securityGroupIds": List[str],
    },
)
DateAttributeBoostingConfigurationTypeDef = TypedDict(
    "DateAttributeBoostingConfigurationTypeDef",
    {
        "boostingLevel": DocumentAttributeBoostingLevelType,
        "boostingDurationInSeconds": NotRequired[int],
    },
)
DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)
DeleteChatControlsConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteChatControlsConfigurationRequestRequestTypeDef",
    {
        "applicationId": str,
    },
)
DeleteConversationRequestRequestTypeDef = TypedDict(
    "DeleteConversationRequestRequestTypeDef",
    {
        "conversationId": str,
        "applicationId": str,
        "userId": NotRequired[str],
    },
)
DeleteDataSourceRequestRequestTypeDef = TypedDict(
    "DeleteDataSourceRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "dataSourceId": str,
    },
)
DeleteGroupRequestRequestTypeDef = TypedDict(
    "DeleteGroupRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "groupName": str,
        "dataSourceId": NotRequired[str],
    },
)
DeleteIndexRequestRequestTypeDef = TypedDict(
    "DeleteIndexRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
    },
)
DeletePluginRequestRequestTypeDef = TypedDict(
    "DeletePluginRequestRequestTypeDef",
    {
        "applicationId": str,
        "pluginId": str,
    },
)
DeleteRetrieverRequestRequestTypeDef = TypedDict(
    "DeleteRetrieverRequestRequestTypeDef",
    {
        "applicationId": str,
        "retrieverId": str,
    },
)
DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "applicationId": str,
        "userId": str,
    },
)
DeleteWebExperienceRequestRequestTypeDef = TypedDict(
    "DeleteWebExperienceRequestRequestTypeDef",
    {
        "applicationId": str,
        "webExperienceId": str,
    },
)
NumberAttributeBoostingConfigurationTypeDef = TypedDict(
    "NumberAttributeBoostingConfigurationTypeDef",
    {
        "boostingLevel": DocumentAttributeBoostingLevelType,
        "boostingType": NotRequired[NumberAttributeBoostingTypeType],
    },
)
StringAttributeBoostingConfigurationOutputTypeDef = TypedDict(
    "StringAttributeBoostingConfigurationOutputTypeDef",
    {
        "boostingLevel": DocumentAttributeBoostingLevelType,
        "attributeValueBoosting": NotRequired[Dict[str, StringAttributeValueBoostingLevelType]],
    },
)
StringListAttributeBoostingConfigurationTypeDef = TypedDict(
    "StringListAttributeBoostingConfigurationTypeDef",
    {
        "boostingLevel": DocumentAttributeBoostingLevelType,
    },
)
DocumentAttributeValueOutputTypeDef = TypedDict(
    "DocumentAttributeValueOutputTypeDef",
    {
        "stringValue": NotRequired[str],
        "stringListValue": NotRequired[List[str]],
        "longValue": NotRequired[int],
        "dateValue": NotRequired[datetime],
    },
)
DocumentAttributeConfigurationTypeDef = TypedDict(
    "DocumentAttributeConfigurationTypeDef",
    {
        "name": NotRequired[str],
        "type": NotRequired[AttributeTypeType],
        "search": NotRequired[StatusType],
    },
)
TimestampTypeDef = Union[datetime, str]
GetApplicationRequestRequestTypeDef = TypedDict(
    "GetApplicationRequestRequestTypeDef",
    {
        "applicationId": str,
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
GetChatControlsConfigurationRequestRequestTypeDef = TypedDict(
    "GetChatControlsConfigurationRequestRequestTypeDef",
    {
        "applicationId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
GetDataSourceRequestRequestTypeDef = TypedDict(
    "GetDataSourceRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "dataSourceId": str,
    },
)
GetGroupRequestRequestTypeDef = TypedDict(
    "GetGroupRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "groupName": str,
        "dataSourceId": NotRequired[str],
    },
)
GetIndexRequestRequestTypeDef = TypedDict(
    "GetIndexRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
    },
)
GetPluginRequestRequestTypeDef = TypedDict(
    "GetPluginRequestRequestTypeDef",
    {
        "applicationId": str,
        "pluginId": str,
    },
)
GetRetrieverRequestRequestTypeDef = TypedDict(
    "GetRetrieverRequestRequestTypeDef",
    {
        "applicationId": str,
        "retrieverId": str,
    },
)
GetUserRequestRequestTypeDef = TypedDict(
    "GetUserRequestRequestTypeDef",
    {
        "applicationId": str,
        "userId": str,
    },
)
GetWebExperienceRequestRequestTypeDef = TypedDict(
    "GetWebExperienceRequestRequestTypeDef",
    {
        "applicationId": str,
        "webExperienceId": str,
    },
)
MemberGroupTypeDef = TypedDict(
    "MemberGroupTypeDef",
    {
        "groupName": str,
        "type": NotRequired[MembershipTypeType],
    },
)
MemberUserTypeDef = TypedDict(
    "MemberUserTypeDef",
    {
        "userId": str,
        "type": NotRequired[MembershipTypeType],
    },
)
GroupSummaryTypeDef = TypedDict(
    "GroupSummaryTypeDef",
    {
        "groupName": NotRequired[str],
    },
)
OpenIDConnectProviderConfigurationTypeDef = TypedDict(
    "OpenIDConnectProviderConfigurationTypeDef",
    {
        "secretsArn": str,
        "secretsRole": str,
    },
)
SamlProviderConfigurationTypeDef = TypedDict(
    "SamlProviderConfigurationTypeDef",
    {
        "authenticationUrl": str,
    },
)
TextDocumentStatisticsTypeDef = TypedDict(
    "TextDocumentStatisticsTypeDef",
    {
        "indexedTextBytes": NotRequired[int],
        "indexedTextDocumentCount": NotRequired[int],
    },
)
IndexTypeDef = TypedDict(
    "IndexTypeDef",
    {
        "displayName": NotRequired[str],
        "indexId": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
        "status": NotRequired[IndexStatusType],
    },
)
KendraIndexConfigurationTypeDef = TypedDict(
    "KendraIndexConfigurationTypeDef",
    {
        "indexId": str,
    },
)
ListApplicationsRequestRequestTypeDef = TypedDict(
    "ListApplicationsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListConversationsRequestRequestTypeDef = TypedDict(
    "ListConversationsRequestRequestTypeDef",
    {
        "applicationId": str,
        "userId": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListDataSourcesRequestRequestTypeDef = TypedDict(
    "ListDataSourcesRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListDocumentsRequestRequestTypeDef = TypedDict(
    "ListDocumentsRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "dataSourceIds": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListIndicesRequestRequestTypeDef = TypedDict(
    "ListIndicesRequestRequestTypeDef",
    {
        "applicationId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListMessagesRequestRequestTypeDef = TypedDict(
    "ListMessagesRequestRequestTypeDef",
    {
        "conversationId": str,
        "applicationId": str,
        "userId": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListPluginsRequestRequestTypeDef = TypedDict(
    "ListPluginsRequestRequestTypeDef",
    {
        "applicationId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
PluginTypeDef = TypedDict(
    "PluginTypeDef",
    {
        "pluginId": NotRequired[str],
        "displayName": NotRequired[str],
        "type": NotRequired[PluginTypeType],
        "serverUrl": NotRequired[str],
        "state": NotRequired[PluginStateType],
        "buildStatus": NotRequired[PluginBuildStatusType],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
    },
)
ListRetrieversRequestRequestTypeDef = TypedDict(
    "ListRetrieversRequestRequestTypeDef",
    {
        "applicationId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
RetrieverTypeDef = TypedDict(
    "RetrieverTypeDef",
    {
        "applicationId": NotRequired[str],
        "retrieverId": NotRequired[str],
        "type": NotRequired[RetrieverTypeType],
        "status": NotRequired[RetrieverStatusType],
        "displayName": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
    },
)
ListWebExperiencesRequestRequestTypeDef = TypedDict(
    "ListWebExperiencesRequestRequestTypeDef",
    {
        "applicationId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
WebExperienceTypeDef = TypedDict(
    "WebExperienceTypeDef",
    {
        "webExperienceId": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
        "defaultEndpoint": NotRequired[str],
        "status": NotRequired[WebExperienceStatusType],
    },
)
OAuth2ClientCredentialConfigurationTypeDef = TypedDict(
    "OAuth2ClientCredentialConfigurationTypeDef",
    {
        "secretArn": str,
        "roleArn": str,
    },
)
PrincipalGroupTypeDef = TypedDict(
    "PrincipalGroupTypeDef",
    {
        "access": ReadAccessTypeType,
        "name": NotRequired[str],
        "membershipType": NotRequired[MembershipTypeType],
    },
)
PrincipalUserTypeDef = TypedDict(
    "PrincipalUserTypeDef",
    {
        "access": ReadAccessTypeType,
        "id": NotRequired[str],
        "membershipType": NotRequired[MembershipTypeType],
    },
)
UsersAndGroupsOutputTypeDef = TypedDict(
    "UsersAndGroupsOutputTypeDef",
    {
        "userIds": NotRequired[List[str]],
        "userGroups": NotRequired[List[str]],
    },
)
SamlConfigurationTypeDef = TypedDict(
    "SamlConfigurationTypeDef",
    {
        "metadataXML": str,
        "roleArn": str,
        "userIdAttribute": str,
        "userGroupAttribute": NotRequired[str],
    },
)
SnippetExcerptTypeDef = TypedDict(
    "SnippetExcerptTypeDef",
    {
        "text": NotRequired[str],
    },
)
StartDataSourceSyncJobRequestRequestTypeDef = TypedDict(
    "StartDataSourceSyncJobRequestRequestTypeDef",
    {
        "dataSourceId": str,
        "applicationId": str,
        "indexId": str,
    },
)
StopDataSourceSyncJobRequestRequestTypeDef = TypedDict(
    "StopDataSourceSyncJobRequestRequestTypeDef",
    {
        "dataSourceId": str,
        "applicationId": str,
        "indexId": str,
    },
)
StringAttributeBoostingConfigurationTypeDef = TypedDict(
    "StringAttributeBoostingConfigurationTypeDef",
    {
        "boostingLevel": DocumentAttributeBoostingLevelType,
        "attributeValueBoosting": NotRequired[Mapping[str, StringAttributeValueBoostingLevelType]],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
        "tagKeys": Sequence[str],
    },
)
UsersAndGroupsTypeDef = TypedDict(
    "UsersAndGroupsTypeDef",
    {
        "userIds": NotRequired[Sequence[str]],
        "userGroups": NotRequired[Sequence[str]],
    },
)
APISchemaTypeDef = TypedDict(
    "APISchemaTypeDef",
    {
        "payload": NotRequired[str],
        "s3": NotRequired[S3TypeDef],
    },
)
ActionExecutionOutputTypeDef = TypedDict(
    "ActionExecutionOutputTypeDef",
    {
        "pluginId": str,
        "payload": Dict[str, ActionExecutionPayloadFieldOutputTypeDef],
        "payloadFieldNameSeparator": str,
    },
)
ActionExecutionPayloadFieldUnionTypeDef = Union[
    ActionExecutionPayloadFieldTypeDef, ActionExecutionPayloadFieldOutputTypeDef
]
ActionReviewPayloadFieldTypeDef = TypedDict(
    "ActionReviewPayloadFieldTypeDef",
    {
        "displayName": NotRequired[str],
        "displayOrder": NotRequired[int],
        "displayDescription": NotRequired[str],
        "type": NotRequired[ActionPayloadFieldTypeType],
        "value": NotRequired[Dict[str, Any]],
        "allowedValues": NotRequired[List[ActionReviewPayloadFieldAllowedValueTypeDef]],
        "allowedFormat": NotRequired[str],
        "required": NotRequired[bool],
    },
)
AttachmentInputTypeDef = TypedDict(
    "AttachmentInputTypeDef",
    {
        "name": str,
        "data": BlobTypeDef,
    },
)
DocumentContentTypeDef = TypedDict(
    "DocumentContentTypeDef",
    {
        "blob": NotRequired[BlobTypeDef],
        "s3": NotRequired[S3TypeDef],
    },
)
AttachmentOutputTypeDef = TypedDict(
    "AttachmentOutputTypeDef",
    {
        "name": NotRequired[str],
        "status": NotRequired[AttachmentStatusType],
        "error": NotRequired[ErrorDetailTypeDef],
    },
)
DocumentDetailsTypeDef = TypedDict(
    "DocumentDetailsTypeDef",
    {
        "documentId": NotRequired[str],
        "status": NotRequired[DocumentStatusType],
        "error": NotRequired[ErrorDetailTypeDef],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
    },
)
FailedDocumentTypeDef = TypedDict(
    "FailedDocumentTypeDef",
    {
        "id": NotRequired[str],
        "error": NotRequired[ErrorDetailTypeDef],
        "dataSourceId": NotRequired[str],
    },
)
GroupStatusDetailTypeDef = TypedDict(
    "GroupStatusDetailTypeDef",
    {
        "status": NotRequired[GroupStatusType],
        "lastUpdatedAt": NotRequired[datetime],
        "errorDetail": NotRequired[ErrorDetailTypeDef],
    },
)
BatchDeleteDocumentRequestRequestTypeDef = TypedDict(
    "BatchDeleteDocumentRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "documents": Sequence[DeleteDocumentTypeDef],
        "dataSourceSyncId": NotRequired[str],
    },
)
CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "applicationId": str,
        "applicationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDataSourceResponseTypeDef = TypedDict(
    "CreateDataSourceResponseTypeDef",
    {
        "dataSourceId": str,
        "dataSourceArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateIndexResponseTypeDef = TypedDict(
    "CreateIndexResponseTypeDef",
    {
        "indexId": str,
        "indexArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePluginResponseTypeDef = TypedDict(
    "CreatePluginResponseTypeDef",
    {
        "pluginId": str,
        "pluginArn": str,
        "buildStatus": PluginBuildStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRetrieverResponseTypeDef = TypedDict(
    "CreateRetrieverResponseTypeDef",
    {
        "retrieverId": str,
        "retrieverArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWebExperienceResponseTypeDef = TypedDict(
    "CreateWebExperienceResponseTypeDef",
    {
        "webExperienceId": str,
        "webExperienceArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {
        "nextToken": str,
        "applications": List[ApplicationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartDataSourceSyncJobResponseTypeDef = TypedDict(
    "StartDataSourceSyncJobResponseTypeDef",
    {
        "executionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ChatModeConfigurationTypeDef = TypedDict(
    "ChatModeConfigurationTypeDef",
    {
        "pluginConfiguration": NotRequired[PluginConfigurationTypeDef],
    },
)
ContentRetrievalRuleOutputTypeDef = TypedDict(
    "ContentRetrievalRuleOutputTypeDef",
    {
        "eligibleDataSources": NotRequired[List[EligibleDataSourceTypeDef]],
    },
)
ContentRetrievalRuleTypeDef = TypedDict(
    "ContentRetrievalRuleTypeDef",
    {
        "eligibleDataSources": NotRequired[Sequence[EligibleDataSourceTypeDef]],
    },
)
ListConversationsResponseTypeDef = TypedDict(
    "ListConversationsResponseTypeDef",
    {
        "nextToken": str,
        "conversations": List[ConversationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetApplicationResponseTypeDef = TypedDict(
    "GetApplicationResponseTypeDef",
    {
        "displayName": str,
        "applicationId": str,
        "applicationArn": str,
        "identityType": IdentityTypeType,
        "iamIdentityProviderArn": str,
        "identityCenterApplicationArn": str,
        "roleArn": str,
        "status": ApplicationStatusType,
        "description": str,
        "encryptionConfiguration": EncryptionConfigurationTypeDef,
        "createdAt": datetime,
        "updatedAt": datetime,
        "error": ErrorDetailTypeDef,
        "attachmentsConfiguration": AppliedAttachmentsConfigurationTypeDef,
        "qAppsConfiguration": QAppsConfigurationTypeDef,
        "personalizationConfiguration": PersonalizationConfigurationTypeDef,
        "autoSubscriptionConfiguration": AutoSubscriptionConfigurationTypeDef,
        "clientIdsForOIDC": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateApplicationRequestRequestTypeDef = TypedDict(
    "UpdateApplicationRequestRequestTypeDef",
    {
        "applicationId": str,
        "identityCenterInstanceArn": NotRequired[str],
        "displayName": NotRequired[str],
        "description": NotRequired[str],
        "roleArn": NotRequired[str],
        "attachmentsConfiguration": NotRequired[AttachmentsConfigurationTypeDef],
        "qAppsConfiguration": NotRequired[QAppsConfigurationTypeDef],
        "personalizationConfiguration": NotRequired[PersonalizationConfigurationTypeDef],
        "autoSubscriptionConfiguration": NotRequired[AutoSubscriptionConfigurationTypeDef],
    },
)
CreateApplicationRequestRequestTypeDef = TypedDict(
    "CreateApplicationRequestRequestTypeDef",
    {
        "displayName": str,
        "roleArn": NotRequired[str],
        "identityType": NotRequired[IdentityTypeType],
        "iamIdentityProviderArn": NotRequired[str],
        "identityCenterInstanceArn": NotRequired[str],
        "clientIdsForOIDC": NotRequired[Sequence[str]],
        "description": NotRequired[str],
        "encryptionConfiguration": NotRequired[EncryptionConfigurationTypeDef],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "clientToken": NotRequired[str],
        "attachmentsConfiguration": NotRequired[AttachmentsConfigurationTypeDef],
        "qAppsConfiguration": NotRequired[QAppsConfigurationTypeDef],
        "personalizationConfiguration": NotRequired[PersonalizationConfigurationTypeDef],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
        "tags": Sequence[TagTypeDef],
    },
)
CreateIndexRequestRequestTypeDef = TypedDict(
    "CreateIndexRequestRequestTypeDef",
    {
        "applicationId": str,
        "displayName": str,
        "type": NotRequired[IndexTypeType],
        "description": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "capacityConfiguration": NotRequired[IndexCapacityConfigurationTypeDef],
        "clientToken": NotRequired[str],
    },
)
CreateUserRequestRequestTypeDef = TypedDict(
    "CreateUserRequestRequestTypeDef",
    {
        "applicationId": str,
        "userId": str,
        "userAliases": NotRequired[Sequence[UserAliasTypeDef]],
        "clientToken": NotRequired[str],
    },
)
GetUserResponseTypeDef = TypedDict(
    "GetUserResponseTypeDef",
    {
        "userAliases": List[UserAliasTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateUserRequestRequestTypeDef = TypedDict(
    "UpdateUserRequestRequestTypeDef",
    {
        "applicationId": str,
        "userId": str,
        "userAliasesToUpdate": NotRequired[Sequence[UserAliasTypeDef]],
        "userAliasesToDelete": NotRequired[Sequence[UserAliasTypeDef]],
    },
)
UpdateUserResponseTypeDef = TypedDict(
    "UpdateUserResponseTypeDef",
    {
        "userAliasesAdded": List[UserAliasTypeDef],
        "userAliasesUpdated": List[UserAliasTypeDef],
        "userAliasesDeleted": List[UserAliasTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DataSourceSyncJobTypeDef = TypedDict(
    "DataSourceSyncJobTypeDef",
    {
        "executionId": NotRequired[str],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
        "status": NotRequired[DataSourceSyncJobStatusType],
        "error": NotRequired[ErrorDetailTypeDef],
        "dataSourceErrorCode": NotRequired[str],
        "metrics": NotRequired[DataSourceSyncJobMetricsTypeDef],
    },
)
ListDataSourcesResponseTypeDef = TypedDict(
    "ListDataSourcesResponseTypeDef",
    {
        "dataSources": List[DataSourceTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DocumentAttributeBoostingConfigurationOutputTypeDef = TypedDict(
    "DocumentAttributeBoostingConfigurationOutputTypeDef",
    {
        "numberConfiguration": NotRequired[NumberAttributeBoostingConfigurationTypeDef],
        "stringConfiguration": NotRequired[StringAttributeBoostingConfigurationOutputTypeDef],
        "dateConfiguration": NotRequired[DateAttributeBoostingConfigurationTypeDef],
        "stringListConfiguration": NotRequired[StringListAttributeBoostingConfigurationTypeDef],
    },
)
DocumentAttributeConditionOutputTypeDef = TypedDict(
    "DocumentAttributeConditionOutputTypeDef",
    {
        "key": str,
        "operator": DocumentEnrichmentConditionOperatorType,
        "value": NotRequired[DocumentAttributeValueOutputTypeDef],
    },
)
DocumentAttributeTargetOutputTypeDef = TypedDict(
    "DocumentAttributeTargetOutputTypeDef",
    {
        "key": str,
        "value": NotRequired[DocumentAttributeValueOutputTypeDef],
        "attributeValueOperator": NotRequired[Literal["DELETE"]],
    },
)
UpdateIndexRequestRequestTypeDef = TypedDict(
    "UpdateIndexRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "displayName": NotRequired[str],
        "description": NotRequired[str],
        "capacityConfiguration": NotRequired[IndexCapacityConfigurationTypeDef],
        "documentAttributeConfigurations": NotRequired[
            Sequence[DocumentAttributeConfigurationTypeDef]
        ],
    },
)
DocumentAttributeValueTypeDef = TypedDict(
    "DocumentAttributeValueTypeDef",
    {
        "stringValue": NotRequired[str],
        "stringListValue": NotRequired[Sequence[str]],
        "longValue": NotRequired[int],
        "dateValue": NotRequired[TimestampTypeDef],
    },
)
ListDataSourceSyncJobsRequestRequestTypeDef = TypedDict(
    "ListDataSourceSyncJobsRequestRequestTypeDef",
    {
        "dataSourceId": str,
        "applicationId": str,
        "indexId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "startTime": NotRequired[TimestampTypeDef],
        "endTime": NotRequired[TimestampTypeDef],
        "statusFilter": NotRequired[DataSourceSyncJobStatusType],
    },
)
ListGroupsRequestRequestTypeDef = TypedDict(
    "ListGroupsRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "updatedEarlierThan": TimestampTypeDef,
        "dataSourceId": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
MessageUsefulnessFeedbackTypeDef = TypedDict(
    "MessageUsefulnessFeedbackTypeDef",
    {
        "usefulness": MessageUsefulnessType,
        "submittedAt": TimestampTypeDef,
        "reason": NotRequired[MessageUsefulnessReasonType],
        "comment": NotRequired[str],
    },
)
GetChatControlsConfigurationRequestGetChatControlsConfigurationPaginateTypeDef = TypedDict(
    "GetChatControlsConfigurationRequestGetChatControlsConfigurationPaginateTypeDef",
    {
        "applicationId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListApplicationsRequestListApplicationsPaginateTypeDef = TypedDict(
    "ListApplicationsRequestListApplicationsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListConversationsRequestListConversationsPaginateTypeDef = TypedDict(
    "ListConversationsRequestListConversationsPaginateTypeDef",
    {
        "applicationId": str,
        "userId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDataSourceSyncJobsRequestListDataSourceSyncJobsPaginateTypeDef = TypedDict(
    "ListDataSourceSyncJobsRequestListDataSourceSyncJobsPaginateTypeDef",
    {
        "dataSourceId": str,
        "applicationId": str,
        "indexId": str,
        "startTime": NotRequired[TimestampTypeDef],
        "endTime": NotRequired[TimestampTypeDef],
        "statusFilter": NotRequired[DataSourceSyncJobStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDataSourcesRequestListDataSourcesPaginateTypeDef = TypedDict(
    "ListDataSourcesRequestListDataSourcesPaginateTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDocumentsRequestListDocumentsPaginateTypeDef = TypedDict(
    "ListDocumentsRequestListDocumentsPaginateTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "dataSourceIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGroupsRequestListGroupsPaginateTypeDef = TypedDict(
    "ListGroupsRequestListGroupsPaginateTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "updatedEarlierThan": TimestampTypeDef,
        "dataSourceId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListIndicesRequestListIndicesPaginateTypeDef = TypedDict(
    "ListIndicesRequestListIndicesPaginateTypeDef",
    {
        "applicationId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMessagesRequestListMessagesPaginateTypeDef = TypedDict(
    "ListMessagesRequestListMessagesPaginateTypeDef",
    {
        "conversationId": str,
        "applicationId": str,
        "userId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPluginsRequestListPluginsPaginateTypeDef = TypedDict(
    "ListPluginsRequestListPluginsPaginateTypeDef",
    {
        "applicationId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRetrieversRequestListRetrieversPaginateTypeDef = TypedDict(
    "ListRetrieversRequestListRetrieversPaginateTypeDef",
    {
        "applicationId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWebExperiencesRequestListWebExperiencesPaginateTypeDef = TypedDict(
    "ListWebExperiencesRequestListWebExperiencesPaginateTypeDef",
    {
        "applicationId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GroupMembersTypeDef = TypedDict(
    "GroupMembersTypeDef",
    {
        "memberGroups": NotRequired[Sequence[MemberGroupTypeDef]],
        "memberUsers": NotRequired[Sequence[MemberUserTypeDef]],
    },
)
ListGroupsResponseTypeDef = TypedDict(
    "ListGroupsResponseTypeDef",
    {
        "nextToken": str,
        "items": List[GroupSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IdentityProviderConfigurationTypeDef = TypedDict(
    "IdentityProviderConfigurationTypeDef",
    {
        "samlConfiguration": NotRequired[SamlProviderConfigurationTypeDef],
        "openIDConnectConfiguration": NotRequired[OpenIDConnectProviderConfigurationTypeDef],
    },
)
IndexStatisticsTypeDef = TypedDict(
    "IndexStatisticsTypeDef",
    {
        "textDocumentStatistics": NotRequired[TextDocumentStatisticsTypeDef],
    },
)
ListIndicesResponseTypeDef = TypedDict(
    "ListIndicesResponseTypeDef",
    {
        "nextToken": str,
        "indices": List[IndexTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPluginsResponseTypeDef = TypedDict(
    "ListPluginsResponseTypeDef",
    {
        "nextToken": str,
        "plugins": List[PluginTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRetrieversResponseTypeDef = TypedDict(
    "ListRetrieversResponseTypeDef",
    {
        "retrievers": List[RetrieverTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListWebExperiencesResponseTypeDef = TypedDict(
    "ListWebExperiencesResponseTypeDef",
    {
        "webExperiences": List[WebExperienceTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PluginAuthConfigurationOutputTypeDef = TypedDict(
    "PluginAuthConfigurationOutputTypeDef",
    {
        "basicAuthConfiguration": NotRequired[BasicAuthConfigurationTypeDef],
        "oAuth2ClientCredentialConfiguration": NotRequired[
            OAuth2ClientCredentialConfigurationTypeDef
        ],
        "noAuthConfiguration": NotRequired[Dict[str, Any]],
    },
)
PluginAuthConfigurationTypeDef = TypedDict(
    "PluginAuthConfigurationTypeDef",
    {
        "basicAuthConfiguration": NotRequired[BasicAuthConfigurationTypeDef],
        "oAuth2ClientCredentialConfiguration": NotRequired[
            OAuth2ClientCredentialConfigurationTypeDef
        ],
        "noAuthConfiguration": NotRequired[Mapping[str, Any]],
    },
)
PrincipalTypeDef = TypedDict(
    "PrincipalTypeDef",
    {
        "user": NotRequired[PrincipalUserTypeDef],
        "group": NotRequired[PrincipalGroupTypeDef],
    },
)
WebExperienceAuthConfigurationTypeDef = TypedDict(
    "WebExperienceAuthConfigurationTypeDef",
    {
        "samlConfiguration": NotRequired[SamlConfigurationTypeDef],
    },
)
TextSegmentTypeDef = TypedDict(
    "TextSegmentTypeDef",
    {
        "beginOffset": NotRequired[int],
        "endOffset": NotRequired[int],
        "snippetExcerpt": NotRequired[SnippetExcerptTypeDef],
    },
)
StringAttributeBoostingConfigurationUnionTypeDef = Union[
    StringAttributeBoostingConfigurationTypeDef, StringAttributeBoostingConfigurationOutputTypeDef
]
UsersAndGroupsUnionTypeDef = Union[UsersAndGroupsTypeDef, UsersAndGroupsOutputTypeDef]
CustomPluginConfigurationTypeDef = TypedDict(
    "CustomPluginConfigurationTypeDef",
    {
        "description": str,
        "apiSchemaType": Literal["OPEN_API_V3"],
        "apiSchema": APISchemaTypeDef,
    },
)
ActionExecutionTypeDef = TypedDict(
    "ActionExecutionTypeDef",
    {
        "pluginId": str,
        "payload": Mapping[str, ActionExecutionPayloadFieldUnionTypeDef],
        "payloadFieldNameSeparator": str,
    },
)
ActionReviewTypeDef = TypedDict(
    "ActionReviewTypeDef",
    {
        "pluginId": NotRequired[str],
        "pluginType": NotRequired[PluginTypeType],
        "payload": NotRequired[Dict[str, ActionReviewPayloadFieldTypeDef]],
        "payloadFieldNameSeparator": NotRequired[str],
    },
)
ListDocumentsResponseTypeDef = TypedDict(
    "ListDocumentsResponseTypeDef",
    {
        "documentDetailList": List[DocumentDetailsTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDeleteDocumentResponseTypeDef = TypedDict(
    "BatchDeleteDocumentResponseTypeDef",
    {
        "failedDocuments": List[FailedDocumentTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchPutDocumentResponseTypeDef = TypedDict(
    "BatchPutDocumentResponseTypeDef",
    {
        "failedDocuments": List[FailedDocumentTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetGroupResponseTypeDef = TypedDict(
    "GetGroupResponseTypeDef",
    {
        "status": GroupStatusDetailTypeDef,
        "statusHistory": List[GroupStatusDetailTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RuleConfigurationOutputTypeDef = TypedDict(
    "RuleConfigurationOutputTypeDef",
    {
        "contentBlockerRule": NotRequired[ContentBlockerRuleTypeDef],
        "contentRetrievalRule": NotRequired[ContentRetrievalRuleOutputTypeDef],
    },
)
ContentRetrievalRuleUnionTypeDef = Union[
    ContentRetrievalRuleTypeDef, ContentRetrievalRuleOutputTypeDef
]
ListDataSourceSyncJobsResponseTypeDef = TypedDict(
    "ListDataSourceSyncJobsResponseTypeDef",
    {
        "history": List[DataSourceSyncJobTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NativeIndexConfigurationOutputTypeDef = TypedDict(
    "NativeIndexConfigurationOutputTypeDef",
    {
        "indexId": str,
        "boostingOverride": NotRequired[
            Dict[str, DocumentAttributeBoostingConfigurationOutputTypeDef]
        ],
    },
)
HookConfigurationOutputTypeDef = TypedDict(
    "HookConfigurationOutputTypeDef",
    {
        "invocationCondition": NotRequired[DocumentAttributeConditionOutputTypeDef],
        "lambdaArn": NotRequired[str],
        "s3BucketName": NotRequired[str],
        "roleArn": NotRequired[str],
    },
)
InlineDocumentEnrichmentConfigurationOutputTypeDef = TypedDict(
    "InlineDocumentEnrichmentConfigurationOutputTypeDef",
    {
        "condition": NotRequired[DocumentAttributeConditionOutputTypeDef],
        "target": NotRequired[DocumentAttributeTargetOutputTypeDef],
        "documentContentOperator": NotRequired[Literal["DELETE"]],
    },
)
DocumentAttributeValueUnionTypeDef = Union[
    DocumentAttributeValueTypeDef, DocumentAttributeValueOutputTypeDef
]
PutFeedbackRequestRequestTypeDef = TypedDict(
    "PutFeedbackRequestRequestTypeDef",
    {
        "applicationId": str,
        "conversationId": str,
        "messageId": str,
        "userId": NotRequired[str],
        "messageCopiedAt": NotRequired[TimestampTypeDef],
        "messageUsefulness": NotRequired[MessageUsefulnessFeedbackTypeDef],
    },
)
PutGroupRequestRequestTypeDef = TypedDict(
    "PutGroupRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "groupName": str,
        "type": MembershipTypeType,
        "groupMembers": GroupMembersTypeDef,
        "dataSourceId": NotRequired[str],
    },
)
CreateWebExperienceRequestRequestTypeDef = TypedDict(
    "CreateWebExperienceRequestRequestTypeDef",
    {
        "applicationId": str,
        "title": NotRequired[str],
        "subtitle": NotRequired[str],
        "welcomeMessage": NotRequired[str],
        "samplePromptsControlMode": NotRequired[WebExperienceSamplePromptsControlModeType],
        "origins": NotRequired[Sequence[str]],
        "roleArn": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "clientToken": NotRequired[str],
        "identityProviderConfiguration": NotRequired[IdentityProviderConfigurationTypeDef],
    },
)
GetIndexResponseTypeDef = TypedDict(
    "GetIndexResponseTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "displayName": str,
        "type": IndexTypeType,
        "indexArn": str,
        "status": IndexStatusType,
        "description": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "capacityConfiguration": IndexCapacityConfigurationTypeDef,
        "documentAttributeConfigurations": List[DocumentAttributeConfigurationTypeDef],
        "error": ErrorDetailTypeDef,
        "indexStatistics": IndexStatisticsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AccessControlTypeDef = TypedDict(
    "AccessControlTypeDef",
    {
        "principals": Sequence[PrincipalTypeDef],
        "memberRelation": NotRequired[MemberRelationType],
    },
)
GetWebExperienceResponseTypeDef = TypedDict(
    "GetWebExperienceResponseTypeDef",
    {
        "applicationId": str,
        "webExperienceId": str,
        "webExperienceArn": str,
        "defaultEndpoint": str,
        "status": WebExperienceStatusType,
        "createdAt": datetime,
        "updatedAt": datetime,
        "title": str,
        "subtitle": str,
        "welcomeMessage": str,
        "samplePromptsControlMode": WebExperienceSamplePromptsControlModeType,
        "origins": List[str],
        "roleArn": str,
        "identityProviderConfiguration": IdentityProviderConfigurationTypeDef,
        "authenticationConfiguration": WebExperienceAuthConfigurationTypeDef,
        "error": ErrorDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateWebExperienceRequestRequestTypeDef = TypedDict(
    "UpdateWebExperienceRequestRequestTypeDef",
    {
        "applicationId": str,
        "webExperienceId": str,
        "roleArn": NotRequired[str],
        "authenticationConfiguration": NotRequired[WebExperienceAuthConfigurationTypeDef],
        "title": NotRequired[str],
        "subtitle": NotRequired[str],
        "welcomeMessage": NotRequired[str],
        "samplePromptsControlMode": NotRequired[WebExperienceSamplePromptsControlModeType],
        "identityProviderConfiguration": NotRequired[IdentityProviderConfigurationTypeDef],
        "origins": NotRequired[Sequence[str]],
    },
)
SourceAttributionTypeDef = TypedDict(
    "SourceAttributionTypeDef",
    {
        "title": NotRequired[str],
        "snippet": NotRequired[str],
        "url": NotRequired[str],
        "citationNumber": NotRequired[int],
        "updatedAt": NotRequired[datetime],
        "textMessageSegments": NotRequired[List[TextSegmentTypeDef]],
    },
)
DocumentAttributeBoostingConfigurationTypeDef = TypedDict(
    "DocumentAttributeBoostingConfigurationTypeDef",
    {
        "numberConfiguration": NotRequired[NumberAttributeBoostingConfigurationTypeDef],
        "stringConfiguration": NotRequired[StringAttributeBoostingConfigurationUnionTypeDef],
        "dateConfiguration": NotRequired[DateAttributeBoostingConfigurationTypeDef],
        "stringListConfiguration": NotRequired[StringListAttributeBoostingConfigurationTypeDef],
    },
)
CreatePluginRequestRequestTypeDef = TypedDict(
    "CreatePluginRequestRequestTypeDef",
    {
        "applicationId": str,
        "displayName": str,
        "type": PluginTypeType,
        "authConfiguration": PluginAuthConfigurationTypeDef,
        "serverUrl": NotRequired[str],
        "customPluginConfiguration": NotRequired[CustomPluginConfigurationTypeDef],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "clientToken": NotRequired[str],
    },
)
GetPluginResponseTypeDef = TypedDict(
    "GetPluginResponseTypeDef",
    {
        "applicationId": str,
        "pluginId": str,
        "displayName": str,
        "type": PluginTypeType,
        "serverUrl": str,
        "authConfiguration": PluginAuthConfigurationOutputTypeDef,
        "customPluginConfiguration": CustomPluginConfigurationTypeDef,
        "buildStatus": PluginBuildStatusType,
        "pluginArn": str,
        "state": PluginStateType,
        "createdAt": datetime,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePluginRequestRequestTypeDef = TypedDict(
    "UpdatePluginRequestRequestTypeDef",
    {
        "applicationId": str,
        "pluginId": str,
        "displayName": NotRequired[str],
        "state": NotRequired[PluginStateType],
        "serverUrl": NotRequired[str],
        "customPluginConfiguration": NotRequired[CustomPluginConfigurationTypeDef],
        "authConfiguration": NotRequired[PluginAuthConfigurationTypeDef],
    },
)
RuleOutputTypeDef = TypedDict(
    "RuleOutputTypeDef",
    {
        "ruleType": RuleTypeType,
        "includedUsersAndGroups": NotRequired[UsersAndGroupsOutputTypeDef],
        "excludedUsersAndGroups": NotRequired[UsersAndGroupsOutputTypeDef],
        "ruleConfiguration": NotRequired[RuleConfigurationOutputTypeDef],
    },
)
RuleConfigurationTypeDef = TypedDict(
    "RuleConfigurationTypeDef",
    {
        "contentBlockerRule": NotRequired[ContentBlockerRuleTypeDef],
        "contentRetrievalRule": NotRequired[ContentRetrievalRuleUnionTypeDef],
    },
)
RetrieverConfigurationOutputTypeDef = TypedDict(
    "RetrieverConfigurationOutputTypeDef",
    {
        "nativeIndexConfiguration": NotRequired[NativeIndexConfigurationOutputTypeDef],
        "kendraIndexConfiguration": NotRequired[KendraIndexConfigurationTypeDef],
    },
)
DocumentEnrichmentConfigurationOutputTypeDef = TypedDict(
    "DocumentEnrichmentConfigurationOutputTypeDef",
    {
        "inlineConfigurations": NotRequired[
            List[InlineDocumentEnrichmentConfigurationOutputTypeDef]
        ],
        "preExtractionHookConfiguration": NotRequired[HookConfigurationOutputTypeDef],
        "postExtractionHookConfiguration": NotRequired[HookConfigurationOutputTypeDef],
    },
)
DocumentAttributeConditionTypeDef = TypedDict(
    "DocumentAttributeConditionTypeDef",
    {
        "key": str,
        "operator": DocumentEnrichmentConditionOperatorType,
        "value": NotRequired[DocumentAttributeValueUnionTypeDef],
    },
)
DocumentAttributeTargetTypeDef = TypedDict(
    "DocumentAttributeTargetTypeDef",
    {
        "key": str,
        "value": NotRequired[DocumentAttributeValueUnionTypeDef],
        "attributeValueOperator": NotRequired[Literal["DELETE"]],
    },
)
DocumentAttributeTypeDef = TypedDict(
    "DocumentAttributeTypeDef",
    {
        "name": str,
        "value": DocumentAttributeValueUnionTypeDef,
    },
)
AccessConfigurationTypeDef = TypedDict(
    "AccessConfigurationTypeDef",
    {
        "accessControls": Sequence[AccessControlTypeDef],
        "memberRelation": NotRequired[MemberRelationType],
    },
)
ChatSyncOutputTypeDef = TypedDict(
    "ChatSyncOutputTypeDef",
    {
        "conversationId": str,
        "systemMessage": str,
        "systemMessageId": str,
        "userMessageId": str,
        "actionReview": ActionReviewTypeDef,
        "authChallengeRequest": AuthChallengeRequestTypeDef,
        "sourceAttributions": List[SourceAttributionTypeDef],
        "failedAttachments": List[AttachmentOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "messageId": NotRequired[str],
        "body": NotRequired[str],
        "time": NotRequired[datetime],
        "type": NotRequired[MessageTypeType],
        "attachments": NotRequired[List[AttachmentOutputTypeDef]],
        "sourceAttribution": NotRequired[List[SourceAttributionTypeDef]],
        "actionReview": NotRequired[ActionReviewTypeDef],
        "actionExecution": NotRequired[ActionExecutionOutputTypeDef],
    },
)
DocumentAttributeBoostingConfigurationUnionTypeDef = Union[
    DocumentAttributeBoostingConfigurationTypeDef,
    DocumentAttributeBoostingConfigurationOutputTypeDef,
]
TopicConfigurationOutputTypeDef = TypedDict(
    "TopicConfigurationOutputTypeDef",
    {
        "name": str,
        "rules": List[RuleOutputTypeDef],
        "description": NotRequired[str],
        "exampleChatMessages": NotRequired[List[str]],
    },
)
RuleConfigurationUnionTypeDef = Union[RuleConfigurationTypeDef, RuleConfigurationOutputTypeDef]
GetRetrieverResponseTypeDef = TypedDict(
    "GetRetrieverResponseTypeDef",
    {
        "applicationId": str,
        "retrieverId": str,
        "retrieverArn": str,
        "type": RetrieverTypeType,
        "status": RetrieverStatusType,
        "displayName": str,
        "configuration": RetrieverConfigurationOutputTypeDef,
        "roleArn": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDataSourceResponseTypeDef = TypedDict(
    "GetDataSourceResponseTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "dataSourceId": str,
        "dataSourceArn": str,
        "displayName": str,
        "type": str,
        "configuration": Dict[str, Any],
        "vpcConfiguration": DataSourceVpcConfigurationOutputTypeDef,
        "createdAt": datetime,
        "updatedAt": datetime,
        "description": str,
        "status": DataSourceStatusType,
        "syncSchedule": str,
        "roleArn": str,
        "error": ErrorDetailTypeDef,
        "documentEnrichmentConfiguration": DocumentEnrichmentConfigurationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DocumentAttributeConditionUnionTypeDef = Union[
    DocumentAttributeConditionTypeDef, DocumentAttributeConditionOutputTypeDef
]
DocumentAttributeTargetUnionTypeDef = Union[
    DocumentAttributeTargetTypeDef, DocumentAttributeTargetOutputTypeDef
]
AttributeFilterTypeDef = TypedDict(
    "AttributeFilterTypeDef",
    {
        "andAllFilters": NotRequired[Sequence[Mapping[str, Any]]],
        "orAllFilters": NotRequired[Sequence[Mapping[str, Any]]],
        "notFilter": NotRequired[Mapping[str, Any]],
        "equalsTo": NotRequired[DocumentAttributeTypeDef],
        "containsAll": NotRequired[DocumentAttributeTypeDef],
        "containsAny": NotRequired[DocumentAttributeTypeDef],
        "greaterThan": NotRequired[DocumentAttributeTypeDef],
        "greaterThanOrEquals": NotRequired[DocumentAttributeTypeDef],
        "lessThan": NotRequired[DocumentAttributeTypeDef],
        "lessThanOrEquals": NotRequired[DocumentAttributeTypeDef],
    },
)
ListMessagesResponseTypeDef = TypedDict(
    "ListMessagesResponseTypeDef",
    {
        "messages": List[MessageTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NativeIndexConfigurationTypeDef = TypedDict(
    "NativeIndexConfigurationTypeDef",
    {
        "indexId": str,
        "boostingOverride": NotRequired[
            Mapping[str, DocumentAttributeBoostingConfigurationUnionTypeDef]
        ],
    },
)
GetChatControlsConfigurationResponseTypeDef = TypedDict(
    "GetChatControlsConfigurationResponseTypeDef",
    {
        "responseScope": ResponseScopeType,
        "blockedPhrases": BlockedPhrasesConfigurationTypeDef,
        "topicConfigurations": List[TopicConfigurationOutputTypeDef],
        "creatorModeConfiguration": AppliedCreatorModeConfigurationTypeDef,
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "ruleType": RuleTypeType,
        "includedUsersAndGroups": NotRequired[UsersAndGroupsUnionTypeDef],
        "excludedUsersAndGroups": NotRequired[UsersAndGroupsUnionTypeDef],
        "ruleConfiguration": NotRequired[RuleConfigurationUnionTypeDef],
    },
)
HookConfigurationTypeDef = TypedDict(
    "HookConfigurationTypeDef",
    {
        "invocationCondition": NotRequired[DocumentAttributeConditionUnionTypeDef],
        "lambdaArn": NotRequired[str],
        "s3BucketName": NotRequired[str],
        "roleArn": NotRequired[str],
    },
)
InlineDocumentEnrichmentConfigurationTypeDef = TypedDict(
    "InlineDocumentEnrichmentConfigurationTypeDef",
    {
        "condition": NotRequired[DocumentAttributeConditionUnionTypeDef],
        "target": NotRequired[DocumentAttributeTargetUnionTypeDef],
        "documentContentOperator": NotRequired[Literal["DELETE"]],
    },
)
ChatSyncInputRequestTypeDef = TypedDict(
    "ChatSyncInputRequestTypeDef",
    {
        "applicationId": str,
        "userId": NotRequired[str],
        "userGroups": NotRequired[Sequence[str]],
        "userMessage": NotRequired[str],
        "attachments": NotRequired[Sequence[AttachmentInputTypeDef]],
        "actionExecution": NotRequired[ActionExecutionTypeDef],
        "authChallengeResponse": NotRequired[AuthChallengeResponseTypeDef],
        "conversationId": NotRequired[str],
        "parentMessageId": NotRequired[str],
        "attributeFilter": NotRequired[AttributeFilterTypeDef],
        "chatMode": NotRequired[ChatModeType],
        "chatModeConfiguration": NotRequired[ChatModeConfigurationTypeDef],
        "clientToken": NotRequired[str],
    },
)
NativeIndexConfigurationUnionTypeDef = Union[
    NativeIndexConfigurationTypeDef, NativeIndexConfigurationOutputTypeDef
]
RuleUnionTypeDef = Union[RuleTypeDef, RuleOutputTypeDef]
HookConfigurationUnionTypeDef = Union[HookConfigurationTypeDef, HookConfigurationOutputTypeDef]
InlineDocumentEnrichmentConfigurationUnionTypeDef = Union[
    InlineDocumentEnrichmentConfigurationTypeDef, InlineDocumentEnrichmentConfigurationOutputTypeDef
]
RetrieverConfigurationTypeDef = TypedDict(
    "RetrieverConfigurationTypeDef",
    {
        "nativeIndexConfiguration": NotRequired[NativeIndexConfigurationUnionTypeDef],
        "kendraIndexConfiguration": NotRequired[KendraIndexConfigurationTypeDef],
    },
)
TopicConfigurationTypeDef = TypedDict(
    "TopicConfigurationTypeDef",
    {
        "name": str,
        "rules": Sequence[RuleUnionTypeDef],
        "description": NotRequired[str],
        "exampleChatMessages": NotRequired[Sequence[str]],
    },
)
DocumentEnrichmentConfigurationTypeDef = TypedDict(
    "DocumentEnrichmentConfigurationTypeDef",
    {
        "inlineConfigurations": NotRequired[
            Sequence[InlineDocumentEnrichmentConfigurationUnionTypeDef]
        ],
        "preExtractionHookConfiguration": NotRequired[HookConfigurationUnionTypeDef],
        "postExtractionHookConfiguration": NotRequired[HookConfigurationUnionTypeDef],
    },
)
CreateRetrieverRequestRequestTypeDef = TypedDict(
    "CreateRetrieverRequestRequestTypeDef",
    {
        "applicationId": str,
        "type": RetrieverTypeType,
        "displayName": str,
        "configuration": RetrieverConfigurationTypeDef,
        "roleArn": NotRequired[str],
        "clientToken": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
UpdateRetrieverRequestRequestTypeDef = TypedDict(
    "UpdateRetrieverRequestRequestTypeDef",
    {
        "applicationId": str,
        "retrieverId": str,
        "configuration": NotRequired[RetrieverConfigurationTypeDef],
        "displayName": NotRequired[str],
        "roleArn": NotRequired[str],
    },
)
TopicConfigurationUnionTypeDef = Union[TopicConfigurationTypeDef, TopicConfigurationOutputTypeDef]
CreateDataSourceRequestRequestTypeDef = TypedDict(
    "CreateDataSourceRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "displayName": str,
        "configuration": Mapping[str, Any],
        "vpcConfiguration": NotRequired[DataSourceVpcConfigurationTypeDef],
        "description": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "syncSchedule": NotRequired[str],
        "roleArn": NotRequired[str],
        "clientToken": NotRequired[str],
        "documentEnrichmentConfiguration": NotRequired[DocumentEnrichmentConfigurationTypeDef],
    },
)
DocumentEnrichmentConfigurationUnionTypeDef = Union[
    DocumentEnrichmentConfigurationTypeDef, DocumentEnrichmentConfigurationOutputTypeDef
]
UpdateDataSourceRequestRequestTypeDef = TypedDict(
    "UpdateDataSourceRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "dataSourceId": str,
        "displayName": NotRequired[str],
        "configuration": NotRequired[Mapping[str, Any]],
        "vpcConfiguration": NotRequired[DataSourceVpcConfigurationTypeDef],
        "description": NotRequired[str],
        "syncSchedule": NotRequired[str],
        "roleArn": NotRequired[str],
        "documentEnrichmentConfiguration": NotRequired[DocumentEnrichmentConfigurationTypeDef],
    },
)
UpdateChatControlsConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateChatControlsConfigurationRequestRequestTypeDef",
    {
        "applicationId": str,
        "clientToken": NotRequired[str],
        "responseScope": NotRequired[ResponseScopeType],
        "blockedPhrasesConfigurationUpdate": NotRequired[BlockedPhrasesConfigurationUpdateTypeDef],
        "topicConfigurationsToCreateOrUpdate": NotRequired[
            Sequence[TopicConfigurationUnionTypeDef]
        ],
        "topicConfigurationsToDelete": NotRequired[Sequence[TopicConfigurationTypeDef]],
        "creatorModeConfiguration": NotRequired[CreatorModeConfigurationTypeDef],
    },
)
DocumentTypeDef = TypedDict(
    "DocumentTypeDef",
    {
        "id": str,
        "attributes": NotRequired[Sequence[DocumentAttributeTypeDef]],
        "content": NotRequired[DocumentContentTypeDef],
        "contentType": NotRequired[ContentTypeType],
        "title": NotRequired[str],
        "accessConfiguration": NotRequired[AccessConfigurationTypeDef],
        "documentEnrichmentConfiguration": NotRequired[DocumentEnrichmentConfigurationUnionTypeDef],
    },
)
BatchPutDocumentRequestRequestTypeDef = TypedDict(
    "BatchPutDocumentRequestRequestTypeDef",
    {
        "applicationId": str,
        "indexId": str,
        "documents": Sequence[DocumentTypeDef],
        "roleArn": NotRequired[str],
        "dataSourceSyncId": NotRequired[str],
    },
)
