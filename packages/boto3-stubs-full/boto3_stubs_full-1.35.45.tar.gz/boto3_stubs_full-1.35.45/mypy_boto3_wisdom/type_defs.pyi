"""
Type annotations for wisdom service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/type_defs/)

Usage::

    ```python
    from mypy_boto3_wisdom.type_defs import AppIntegrationsConfigurationOutputTypeDef

    data: AppIntegrationsConfigurationOutputTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AssistantStatusType,
    ContentStatusType,
    ImportJobStatusType,
    KnowledgeBaseStatusType,
    KnowledgeBaseTypeType,
    OrderType,
    PriorityType,
    QuickResponseFilterOperatorType,
    QuickResponseQueryOperatorType,
    QuickResponseStatusType,
    RecommendationSourceTypeType,
    RelevanceLevelType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AppIntegrationsConfigurationOutputTypeDef",
    "AppIntegrationsConfigurationTypeDef",
    "AssistantAssociationInputDataTypeDef",
    "KnowledgeBaseAssociationDataTypeDef",
    "AssistantIntegrationConfigurationTypeDef",
    "ServerSideEncryptionConfigurationTypeDef",
    "ConnectConfigurationTypeDef",
    "ContentDataTypeDef",
    "ContentReferenceTypeDef",
    "ContentSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "CreateContentRequestRequestTypeDef",
    "RenderingConfigurationTypeDef",
    "GroupingConfigurationTypeDef",
    "QuickResponseDataProviderTypeDef",
    "CreateSessionRequestRequestTypeDef",
    "DeleteAssistantAssociationRequestRequestTypeDef",
    "DeleteAssistantRequestRequestTypeDef",
    "DeleteContentRequestRequestTypeDef",
    "DeleteImportJobRequestRequestTypeDef",
    "DeleteKnowledgeBaseRequestRequestTypeDef",
    "DeleteQuickResponseRequestRequestTypeDef",
    "HighlightTypeDef",
    "FilterTypeDef",
    "GetAssistantAssociationRequestRequestTypeDef",
    "GetAssistantRequestRequestTypeDef",
    "GetContentRequestRequestTypeDef",
    "GetContentSummaryRequestRequestTypeDef",
    "GetImportJobRequestRequestTypeDef",
    "GetKnowledgeBaseRequestRequestTypeDef",
    "GetQuickResponseRequestRequestTypeDef",
    "GetRecommendationsRequestRequestTypeDef",
    "GetSessionRequestRequestTypeDef",
    "GroupingConfigurationOutputTypeDef",
    "PaginatorConfigTypeDef",
    "ListAssistantAssociationsRequestRequestTypeDef",
    "ListAssistantsRequestRequestTypeDef",
    "ListContentsRequestRequestTypeDef",
    "ListImportJobsRequestRequestTypeDef",
    "ListKnowledgeBasesRequestRequestTypeDef",
    "ListQuickResponsesRequestRequestTypeDef",
    "QuickResponseSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "NotifyRecommendationsReceivedErrorTypeDef",
    "NotifyRecommendationsReceivedRequestRequestTypeDef",
    "QueryAssistantRequestRequestTypeDef",
    "QueryRecommendationTriggerDataTypeDef",
    "QuickResponseContentProviderTypeDef",
    "QuickResponseFilterFieldTypeDef",
    "QuickResponseOrderFieldTypeDef",
    "QuickResponseQueryFieldTypeDef",
    "RemoveKnowledgeBaseTemplateUriRequestRequestTypeDef",
    "SessionSummaryTypeDef",
    "SessionIntegrationConfigurationTypeDef",
    "StartContentUploadRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateContentRequestRequestTypeDef",
    "UpdateKnowledgeBaseTemplateUriRequestRequestTypeDef",
    "SourceConfigurationOutputTypeDef",
    "AppIntegrationsConfigurationUnionTypeDef",
    "CreateAssistantAssociationRequestRequestTypeDef",
    "AssistantAssociationOutputDataTypeDef",
    "AssistantDataTypeDef",
    "AssistantSummaryTypeDef",
    "CreateAssistantRequestRequestTypeDef",
    "ConfigurationTypeDef",
    "CreateContentResponseTypeDef",
    "GetContentResponseTypeDef",
    "GetContentSummaryResponseTypeDef",
    "ListContentsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "SearchContentResponseTypeDef",
    "StartContentUploadResponseTypeDef",
    "UpdateContentResponseTypeDef",
    "CreateQuickResponseRequestRequestTypeDef",
    "UpdateQuickResponseRequestRequestTypeDef",
    "DocumentTextTypeDef",
    "SearchExpressionTypeDef",
    "ListAssistantAssociationsRequestListAssistantAssociationsPaginateTypeDef",
    "ListAssistantsRequestListAssistantsPaginateTypeDef",
    "ListContentsRequestListContentsPaginateTypeDef",
    "ListImportJobsRequestListImportJobsPaginateTypeDef",
    "ListKnowledgeBasesRequestListKnowledgeBasesPaginateTypeDef",
    "ListQuickResponsesRequestListQuickResponsesPaginateTypeDef",
    "QueryAssistantRequestQueryAssistantPaginateTypeDef",
    "ListQuickResponsesResponseTypeDef",
    "NotifyRecommendationsReceivedResponseTypeDef",
    "RecommendationTriggerDataTypeDef",
    "QuickResponseContentsTypeDef",
    "QuickResponseSearchExpressionTypeDef",
    "SearchSessionsResponseTypeDef",
    "SessionDataTypeDef",
    "KnowledgeBaseDataTypeDef",
    "KnowledgeBaseSummaryTypeDef",
    "SourceConfigurationTypeDef",
    "AssistantAssociationDataTypeDef",
    "AssistantAssociationSummaryTypeDef",
    "CreateAssistantResponseTypeDef",
    "GetAssistantResponseTypeDef",
    "ListAssistantsResponseTypeDef",
    "ExternalSourceConfigurationTypeDef",
    "DocumentTypeDef",
    "SearchContentRequestRequestTypeDef",
    "SearchContentRequestSearchContentPaginateTypeDef",
    "SearchSessionsRequestRequestTypeDef",
    "SearchSessionsRequestSearchSessionsPaginateTypeDef",
    "RecommendationTriggerTypeDef",
    "QuickResponseDataTypeDef",
    "QuickResponseSearchResultDataTypeDef",
    "SearchQuickResponsesRequestRequestTypeDef",
    "SearchQuickResponsesRequestSearchQuickResponsesPaginateTypeDef",
    "CreateSessionResponseTypeDef",
    "GetSessionResponseTypeDef",
    "CreateKnowledgeBaseResponseTypeDef",
    "GetKnowledgeBaseResponseTypeDef",
    "UpdateKnowledgeBaseTemplateUriResponseTypeDef",
    "ListKnowledgeBasesResponseTypeDef",
    "CreateKnowledgeBaseRequestRequestTypeDef",
    "CreateAssistantAssociationResponseTypeDef",
    "GetAssistantAssociationResponseTypeDef",
    "ListAssistantAssociationsResponseTypeDef",
    "ImportJobDataTypeDef",
    "ImportJobSummaryTypeDef",
    "StartImportJobRequestRequestTypeDef",
    "RecommendationDataTypeDef",
    "ResultDataTypeDef",
    "CreateQuickResponseResponseTypeDef",
    "GetQuickResponseResponseTypeDef",
    "UpdateQuickResponseResponseTypeDef",
    "SearchQuickResponsesResponseTypeDef",
    "GetImportJobResponseTypeDef",
    "StartImportJobResponseTypeDef",
    "ListImportJobsResponseTypeDef",
    "GetRecommendationsResponseTypeDef",
    "QueryAssistantResponseTypeDef",
)

AppIntegrationsConfigurationOutputTypeDef = TypedDict(
    "AppIntegrationsConfigurationOutputTypeDef",
    {
        "appIntegrationArn": str,
        "objectFields": NotRequired[List[str]],
    },
)
AppIntegrationsConfigurationTypeDef = TypedDict(
    "AppIntegrationsConfigurationTypeDef",
    {
        "appIntegrationArn": str,
        "objectFields": NotRequired[Sequence[str]],
    },
)
AssistantAssociationInputDataTypeDef = TypedDict(
    "AssistantAssociationInputDataTypeDef",
    {
        "knowledgeBaseId": NotRequired[str],
    },
)
KnowledgeBaseAssociationDataTypeDef = TypedDict(
    "KnowledgeBaseAssociationDataTypeDef",
    {
        "knowledgeBaseArn": NotRequired[str],
        "knowledgeBaseId": NotRequired[str],
    },
)
AssistantIntegrationConfigurationTypeDef = TypedDict(
    "AssistantIntegrationConfigurationTypeDef",
    {
        "topicIntegrationArn": NotRequired[str],
    },
)
ServerSideEncryptionConfigurationTypeDef = TypedDict(
    "ServerSideEncryptionConfigurationTypeDef",
    {
        "kmsKeyId": NotRequired[str],
    },
)
ConnectConfigurationTypeDef = TypedDict(
    "ConnectConfigurationTypeDef",
    {
        "instanceId": NotRequired[str],
    },
)
ContentDataTypeDef = TypedDict(
    "ContentDataTypeDef",
    {
        "contentArn": str,
        "contentId": str,
        "contentType": str,
        "knowledgeBaseArn": str,
        "knowledgeBaseId": str,
        "metadata": Dict[str, str],
        "name": str,
        "revisionId": str,
        "status": ContentStatusType,
        "title": str,
        "url": str,
        "urlExpiry": datetime,
        "linkOutUri": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)
ContentReferenceTypeDef = TypedDict(
    "ContentReferenceTypeDef",
    {
        "contentArn": NotRequired[str],
        "contentId": NotRequired[str],
        "knowledgeBaseArn": NotRequired[str],
        "knowledgeBaseId": NotRequired[str],
    },
)
ContentSummaryTypeDef = TypedDict(
    "ContentSummaryTypeDef",
    {
        "contentArn": str,
        "contentId": str,
        "contentType": str,
        "knowledgeBaseArn": str,
        "knowledgeBaseId": str,
        "metadata": Dict[str, str],
        "name": str,
        "revisionId": str,
        "status": ContentStatusType,
        "title": str,
        "tags": NotRequired[Dict[str, str]],
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
CreateContentRequestRequestTypeDef = TypedDict(
    "CreateContentRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "name": str,
        "uploadId": str,
        "clientToken": NotRequired[str],
        "metadata": NotRequired[Mapping[str, str]],
        "overrideLinkOutUri": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "title": NotRequired[str],
    },
)
RenderingConfigurationTypeDef = TypedDict(
    "RenderingConfigurationTypeDef",
    {
        "templateUri": NotRequired[str],
    },
)
GroupingConfigurationTypeDef = TypedDict(
    "GroupingConfigurationTypeDef",
    {
        "criteria": NotRequired[str],
        "values": NotRequired[Sequence[str]],
    },
)
QuickResponseDataProviderTypeDef = TypedDict(
    "QuickResponseDataProviderTypeDef",
    {
        "content": NotRequired[str],
    },
)
CreateSessionRequestRequestTypeDef = TypedDict(
    "CreateSessionRequestRequestTypeDef",
    {
        "assistantId": str,
        "name": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
DeleteAssistantAssociationRequestRequestTypeDef = TypedDict(
    "DeleteAssistantAssociationRequestRequestTypeDef",
    {
        "assistantAssociationId": str,
        "assistantId": str,
    },
)
DeleteAssistantRequestRequestTypeDef = TypedDict(
    "DeleteAssistantRequestRequestTypeDef",
    {
        "assistantId": str,
    },
)
DeleteContentRequestRequestTypeDef = TypedDict(
    "DeleteContentRequestRequestTypeDef",
    {
        "contentId": str,
        "knowledgeBaseId": str,
    },
)
DeleteImportJobRequestRequestTypeDef = TypedDict(
    "DeleteImportJobRequestRequestTypeDef",
    {
        "importJobId": str,
        "knowledgeBaseId": str,
    },
)
DeleteKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "DeleteKnowledgeBaseRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
    },
)
DeleteQuickResponseRequestRequestTypeDef = TypedDict(
    "DeleteQuickResponseRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "quickResponseId": str,
    },
)
HighlightTypeDef = TypedDict(
    "HighlightTypeDef",
    {
        "beginOffsetInclusive": NotRequired[int],
        "endOffsetExclusive": NotRequired[int],
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "field": Literal["NAME"],
        "operator": Literal["EQUALS"],
        "value": str,
    },
)
GetAssistantAssociationRequestRequestTypeDef = TypedDict(
    "GetAssistantAssociationRequestRequestTypeDef",
    {
        "assistantAssociationId": str,
        "assistantId": str,
    },
)
GetAssistantRequestRequestTypeDef = TypedDict(
    "GetAssistantRequestRequestTypeDef",
    {
        "assistantId": str,
    },
)
GetContentRequestRequestTypeDef = TypedDict(
    "GetContentRequestRequestTypeDef",
    {
        "contentId": str,
        "knowledgeBaseId": str,
    },
)
GetContentSummaryRequestRequestTypeDef = TypedDict(
    "GetContentSummaryRequestRequestTypeDef",
    {
        "contentId": str,
        "knowledgeBaseId": str,
    },
)
GetImportJobRequestRequestTypeDef = TypedDict(
    "GetImportJobRequestRequestTypeDef",
    {
        "importJobId": str,
        "knowledgeBaseId": str,
    },
)
GetKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "GetKnowledgeBaseRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
    },
)
GetQuickResponseRequestRequestTypeDef = TypedDict(
    "GetQuickResponseRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "quickResponseId": str,
    },
)
GetRecommendationsRequestRequestTypeDef = TypedDict(
    "GetRecommendationsRequestRequestTypeDef",
    {
        "assistantId": str,
        "sessionId": str,
        "maxResults": NotRequired[int],
        "waitTimeSeconds": NotRequired[int],
    },
)
GetSessionRequestRequestTypeDef = TypedDict(
    "GetSessionRequestRequestTypeDef",
    {
        "assistantId": str,
        "sessionId": str,
    },
)
GroupingConfigurationOutputTypeDef = TypedDict(
    "GroupingConfigurationOutputTypeDef",
    {
        "criteria": NotRequired[str],
        "values": NotRequired[List[str]],
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
ListAssistantAssociationsRequestRequestTypeDef = TypedDict(
    "ListAssistantAssociationsRequestRequestTypeDef",
    {
        "assistantId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListAssistantsRequestRequestTypeDef = TypedDict(
    "ListAssistantsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListContentsRequestRequestTypeDef = TypedDict(
    "ListContentsRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListImportJobsRequestRequestTypeDef = TypedDict(
    "ListImportJobsRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListKnowledgeBasesRequestRequestTypeDef = TypedDict(
    "ListKnowledgeBasesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListQuickResponsesRequestRequestTypeDef = TypedDict(
    "ListQuickResponsesRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
QuickResponseSummaryTypeDef = TypedDict(
    "QuickResponseSummaryTypeDef",
    {
        "contentType": str,
        "createdTime": datetime,
        "knowledgeBaseArn": str,
        "knowledgeBaseId": str,
        "lastModifiedTime": datetime,
        "name": str,
        "quickResponseArn": str,
        "quickResponseId": str,
        "status": QuickResponseStatusType,
        "channels": NotRequired[List[str]],
        "description": NotRequired[str],
        "isActive": NotRequired[bool],
        "lastModifiedBy": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
NotifyRecommendationsReceivedErrorTypeDef = TypedDict(
    "NotifyRecommendationsReceivedErrorTypeDef",
    {
        "message": NotRequired[str],
        "recommendationId": NotRequired[str],
    },
)
NotifyRecommendationsReceivedRequestRequestTypeDef = TypedDict(
    "NotifyRecommendationsReceivedRequestRequestTypeDef",
    {
        "assistantId": str,
        "recommendationIds": Sequence[str],
        "sessionId": str,
    },
)
QueryAssistantRequestRequestTypeDef = TypedDict(
    "QueryAssistantRequestRequestTypeDef",
    {
        "assistantId": str,
        "queryText": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
QueryRecommendationTriggerDataTypeDef = TypedDict(
    "QueryRecommendationTriggerDataTypeDef",
    {
        "text": NotRequired[str],
    },
)
QuickResponseContentProviderTypeDef = TypedDict(
    "QuickResponseContentProviderTypeDef",
    {
        "content": NotRequired[str],
    },
)
QuickResponseFilterFieldTypeDef = TypedDict(
    "QuickResponseFilterFieldTypeDef",
    {
        "name": str,
        "operator": QuickResponseFilterOperatorType,
        "includeNoExistence": NotRequired[bool],
        "values": NotRequired[Sequence[str]],
    },
)
QuickResponseOrderFieldTypeDef = TypedDict(
    "QuickResponseOrderFieldTypeDef",
    {
        "name": str,
        "order": NotRequired[OrderType],
    },
)
QuickResponseQueryFieldTypeDef = TypedDict(
    "QuickResponseQueryFieldTypeDef",
    {
        "name": str,
        "operator": QuickResponseQueryOperatorType,
        "values": Sequence[str],
        "allowFuzziness": NotRequired[bool],
        "priority": NotRequired[PriorityType],
    },
)
RemoveKnowledgeBaseTemplateUriRequestRequestTypeDef = TypedDict(
    "RemoveKnowledgeBaseTemplateUriRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
    },
)
SessionSummaryTypeDef = TypedDict(
    "SessionSummaryTypeDef",
    {
        "assistantArn": str,
        "assistantId": str,
        "sessionArn": str,
        "sessionId": str,
    },
)
SessionIntegrationConfigurationTypeDef = TypedDict(
    "SessionIntegrationConfigurationTypeDef",
    {
        "topicIntegrationArn": NotRequired[str],
    },
)
StartContentUploadRequestRequestTypeDef = TypedDict(
    "StartContentUploadRequestRequestTypeDef",
    {
        "contentType": str,
        "knowledgeBaseId": str,
        "presignedUrlTimeToLive": NotRequired[int],
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
UpdateContentRequestRequestTypeDef = TypedDict(
    "UpdateContentRequestRequestTypeDef",
    {
        "contentId": str,
        "knowledgeBaseId": str,
        "metadata": NotRequired[Mapping[str, str]],
        "overrideLinkOutUri": NotRequired[str],
        "removeOverrideLinkOutUri": NotRequired[bool],
        "revisionId": NotRequired[str],
        "title": NotRequired[str],
        "uploadId": NotRequired[str],
    },
)
UpdateKnowledgeBaseTemplateUriRequestRequestTypeDef = TypedDict(
    "UpdateKnowledgeBaseTemplateUriRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "templateUri": str,
    },
)
SourceConfigurationOutputTypeDef = TypedDict(
    "SourceConfigurationOutputTypeDef",
    {
        "appIntegrations": NotRequired[AppIntegrationsConfigurationOutputTypeDef],
    },
)
AppIntegrationsConfigurationUnionTypeDef = Union[
    AppIntegrationsConfigurationTypeDef, AppIntegrationsConfigurationOutputTypeDef
]
CreateAssistantAssociationRequestRequestTypeDef = TypedDict(
    "CreateAssistantAssociationRequestRequestTypeDef",
    {
        "assistantId": str,
        "association": AssistantAssociationInputDataTypeDef,
        "associationType": Literal["KNOWLEDGE_BASE"],
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
AssistantAssociationOutputDataTypeDef = TypedDict(
    "AssistantAssociationOutputDataTypeDef",
    {
        "knowledgeBaseAssociation": NotRequired[KnowledgeBaseAssociationDataTypeDef],
    },
)
AssistantDataTypeDef = TypedDict(
    "AssistantDataTypeDef",
    {
        "assistantArn": str,
        "assistantId": str,
        "name": str,
        "status": AssistantStatusType,
        "type": Literal["AGENT"],
        "description": NotRequired[str],
        "integrationConfiguration": NotRequired[AssistantIntegrationConfigurationTypeDef],
        "serverSideEncryptionConfiguration": NotRequired[ServerSideEncryptionConfigurationTypeDef],
        "tags": NotRequired[Dict[str, str]],
    },
)
AssistantSummaryTypeDef = TypedDict(
    "AssistantSummaryTypeDef",
    {
        "assistantArn": str,
        "assistantId": str,
        "name": str,
        "status": AssistantStatusType,
        "type": Literal["AGENT"],
        "description": NotRequired[str],
        "integrationConfiguration": NotRequired[AssistantIntegrationConfigurationTypeDef],
        "serverSideEncryptionConfiguration": NotRequired[ServerSideEncryptionConfigurationTypeDef],
        "tags": NotRequired[Dict[str, str]],
    },
)
CreateAssistantRequestRequestTypeDef = TypedDict(
    "CreateAssistantRequestRequestTypeDef",
    {
        "name": str,
        "type": Literal["AGENT"],
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "serverSideEncryptionConfiguration": NotRequired[ServerSideEncryptionConfigurationTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "connectConfiguration": NotRequired[ConnectConfigurationTypeDef],
    },
)
CreateContentResponseTypeDef = TypedDict(
    "CreateContentResponseTypeDef",
    {
        "content": ContentDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetContentResponseTypeDef = TypedDict(
    "GetContentResponseTypeDef",
    {
        "content": ContentDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetContentSummaryResponseTypeDef = TypedDict(
    "GetContentSummaryResponseTypeDef",
    {
        "contentSummary": ContentSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListContentsResponseTypeDef = TypedDict(
    "ListContentsResponseTypeDef",
    {
        "contentSummaries": List[ContentSummaryTypeDef],
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
SearchContentResponseTypeDef = TypedDict(
    "SearchContentResponseTypeDef",
    {
        "contentSummaries": List[ContentSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartContentUploadResponseTypeDef = TypedDict(
    "StartContentUploadResponseTypeDef",
    {
        "headersToInclude": Dict[str, str],
        "uploadId": str,
        "url": str,
        "urlExpiry": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateContentResponseTypeDef = TypedDict(
    "UpdateContentResponseTypeDef",
    {
        "content": ContentDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateQuickResponseRequestRequestTypeDef = TypedDict(
    "CreateQuickResponseRequestRequestTypeDef",
    {
        "content": QuickResponseDataProviderTypeDef,
        "knowledgeBaseId": str,
        "name": str,
        "channels": NotRequired[Sequence[str]],
        "clientToken": NotRequired[str],
        "contentType": NotRequired[str],
        "description": NotRequired[str],
        "groupingConfiguration": NotRequired[GroupingConfigurationTypeDef],
        "isActive": NotRequired[bool],
        "language": NotRequired[str],
        "shortcutKey": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
UpdateQuickResponseRequestRequestTypeDef = TypedDict(
    "UpdateQuickResponseRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "quickResponseId": str,
        "channels": NotRequired[Sequence[str]],
        "content": NotRequired[QuickResponseDataProviderTypeDef],
        "contentType": NotRequired[str],
        "description": NotRequired[str],
        "groupingConfiguration": NotRequired[GroupingConfigurationTypeDef],
        "isActive": NotRequired[bool],
        "language": NotRequired[str],
        "name": NotRequired[str],
        "removeDescription": NotRequired[bool],
        "removeGroupingConfiguration": NotRequired[bool],
        "removeShortcutKey": NotRequired[bool],
        "shortcutKey": NotRequired[str],
    },
)
DocumentTextTypeDef = TypedDict(
    "DocumentTextTypeDef",
    {
        "highlights": NotRequired[List[HighlightTypeDef]],
        "text": NotRequired[str],
    },
)
SearchExpressionTypeDef = TypedDict(
    "SearchExpressionTypeDef",
    {
        "filters": Sequence[FilterTypeDef],
    },
)
ListAssistantAssociationsRequestListAssistantAssociationsPaginateTypeDef = TypedDict(
    "ListAssistantAssociationsRequestListAssistantAssociationsPaginateTypeDef",
    {
        "assistantId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAssistantsRequestListAssistantsPaginateTypeDef = TypedDict(
    "ListAssistantsRequestListAssistantsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListContentsRequestListContentsPaginateTypeDef = TypedDict(
    "ListContentsRequestListContentsPaginateTypeDef",
    {
        "knowledgeBaseId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListImportJobsRequestListImportJobsPaginateTypeDef = TypedDict(
    "ListImportJobsRequestListImportJobsPaginateTypeDef",
    {
        "knowledgeBaseId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListKnowledgeBasesRequestListKnowledgeBasesPaginateTypeDef = TypedDict(
    "ListKnowledgeBasesRequestListKnowledgeBasesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListQuickResponsesRequestListQuickResponsesPaginateTypeDef = TypedDict(
    "ListQuickResponsesRequestListQuickResponsesPaginateTypeDef",
    {
        "knowledgeBaseId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
QueryAssistantRequestQueryAssistantPaginateTypeDef = TypedDict(
    "QueryAssistantRequestQueryAssistantPaginateTypeDef",
    {
        "assistantId": str,
        "queryText": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListQuickResponsesResponseTypeDef = TypedDict(
    "ListQuickResponsesResponseTypeDef",
    {
        "nextToken": str,
        "quickResponseSummaries": List[QuickResponseSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NotifyRecommendationsReceivedResponseTypeDef = TypedDict(
    "NotifyRecommendationsReceivedResponseTypeDef",
    {
        "errors": List[NotifyRecommendationsReceivedErrorTypeDef],
        "recommendationIds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RecommendationTriggerDataTypeDef = TypedDict(
    "RecommendationTriggerDataTypeDef",
    {
        "query": NotRequired[QueryRecommendationTriggerDataTypeDef],
    },
)
QuickResponseContentsTypeDef = TypedDict(
    "QuickResponseContentsTypeDef",
    {
        "markdown": NotRequired[QuickResponseContentProviderTypeDef],
        "plainText": NotRequired[QuickResponseContentProviderTypeDef],
    },
)
QuickResponseSearchExpressionTypeDef = TypedDict(
    "QuickResponseSearchExpressionTypeDef",
    {
        "filters": NotRequired[Sequence[QuickResponseFilterFieldTypeDef]],
        "orderOnField": NotRequired[QuickResponseOrderFieldTypeDef],
        "queries": NotRequired[Sequence[QuickResponseQueryFieldTypeDef]],
    },
)
SearchSessionsResponseTypeDef = TypedDict(
    "SearchSessionsResponseTypeDef",
    {
        "nextToken": str,
        "sessionSummaries": List[SessionSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SessionDataTypeDef = TypedDict(
    "SessionDataTypeDef",
    {
        "name": str,
        "sessionArn": str,
        "sessionId": str,
        "description": NotRequired[str],
        "integrationConfiguration": NotRequired[SessionIntegrationConfigurationTypeDef],
        "tags": NotRequired[Dict[str, str]],
    },
)
KnowledgeBaseDataTypeDef = TypedDict(
    "KnowledgeBaseDataTypeDef",
    {
        "knowledgeBaseArn": str,
        "knowledgeBaseId": str,
        "knowledgeBaseType": KnowledgeBaseTypeType,
        "name": str,
        "status": KnowledgeBaseStatusType,
        "description": NotRequired[str],
        "lastContentModificationTime": NotRequired[datetime],
        "renderingConfiguration": NotRequired[RenderingConfigurationTypeDef],
        "serverSideEncryptionConfiguration": NotRequired[ServerSideEncryptionConfigurationTypeDef],
        "sourceConfiguration": NotRequired[SourceConfigurationOutputTypeDef],
        "tags": NotRequired[Dict[str, str]],
    },
)
KnowledgeBaseSummaryTypeDef = TypedDict(
    "KnowledgeBaseSummaryTypeDef",
    {
        "knowledgeBaseArn": str,
        "knowledgeBaseId": str,
        "knowledgeBaseType": KnowledgeBaseTypeType,
        "name": str,
        "status": KnowledgeBaseStatusType,
        "description": NotRequired[str],
        "renderingConfiguration": NotRequired[RenderingConfigurationTypeDef],
        "serverSideEncryptionConfiguration": NotRequired[ServerSideEncryptionConfigurationTypeDef],
        "sourceConfiguration": NotRequired[SourceConfigurationOutputTypeDef],
        "tags": NotRequired[Dict[str, str]],
    },
)
SourceConfigurationTypeDef = TypedDict(
    "SourceConfigurationTypeDef",
    {
        "appIntegrations": NotRequired[AppIntegrationsConfigurationUnionTypeDef],
    },
)
AssistantAssociationDataTypeDef = TypedDict(
    "AssistantAssociationDataTypeDef",
    {
        "assistantArn": str,
        "assistantAssociationArn": str,
        "assistantAssociationId": str,
        "assistantId": str,
        "associationData": AssistantAssociationOutputDataTypeDef,
        "associationType": Literal["KNOWLEDGE_BASE"],
        "tags": NotRequired[Dict[str, str]],
    },
)
AssistantAssociationSummaryTypeDef = TypedDict(
    "AssistantAssociationSummaryTypeDef",
    {
        "assistantArn": str,
        "assistantAssociationArn": str,
        "assistantAssociationId": str,
        "assistantId": str,
        "associationData": AssistantAssociationOutputDataTypeDef,
        "associationType": Literal["KNOWLEDGE_BASE"],
        "tags": NotRequired[Dict[str, str]],
    },
)
CreateAssistantResponseTypeDef = TypedDict(
    "CreateAssistantResponseTypeDef",
    {
        "assistant": AssistantDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAssistantResponseTypeDef = TypedDict(
    "GetAssistantResponseTypeDef",
    {
        "assistant": AssistantDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssistantsResponseTypeDef = TypedDict(
    "ListAssistantsResponseTypeDef",
    {
        "assistantSummaries": List[AssistantSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExternalSourceConfigurationTypeDef = TypedDict(
    "ExternalSourceConfigurationTypeDef",
    {
        "configuration": ConfigurationTypeDef,
        "source": Literal["AMAZON_CONNECT"],
    },
)
DocumentTypeDef = TypedDict(
    "DocumentTypeDef",
    {
        "contentReference": ContentReferenceTypeDef,
        "excerpt": NotRequired[DocumentTextTypeDef],
        "title": NotRequired[DocumentTextTypeDef],
    },
)
SearchContentRequestRequestTypeDef = TypedDict(
    "SearchContentRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "searchExpression": SearchExpressionTypeDef,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
SearchContentRequestSearchContentPaginateTypeDef = TypedDict(
    "SearchContentRequestSearchContentPaginateTypeDef",
    {
        "knowledgeBaseId": str,
        "searchExpression": SearchExpressionTypeDef,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchSessionsRequestRequestTypeDef = TypedDict(
    "SearchSessionsRequestRequestTypeDef",
    {
        "assistantId": str,
        "searchExpression": SearchExpressionTypeDef,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
SearchSessionsRequestSearchSessionsPaginateTypeDef = TypedDict(
    "SearchSessionsRequestSearchSessionsPaginateTypeDef",
    {
        "assistantId": str,
        "searchExpression": SearchExpressionTypeDef,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
RecommendationTriggerTypeDef = TypedDict(
    "RecommendationTriggerTypeDef",
    {
        "data": RecommendationTriggerDataTypeDef,
        "id": str,
        "recommendationIds": List[str],
        "source": RecommendationSourceTypeType,
        "type": Literal["QUERY"],
    },
)
QuickResponseDataTypeDef = TypedDict(
    "QuickResponseDataTypeDef",
    {
        "contentType": str,
        "createdTime": datetime,
        "knowledgeBaseArn": str,
        "knowledgeBaseId": str,
        "lastModifiedTime": datetime,
        "name": str,
        "quickResponseArn": str,
        "quickResponseId": str,
        "status": QuickResponseStatusType,
        "channels": NotRequired[List[str]],
        "contents": NotRequired[QuickResponseContentsTypeDef],
        "description": NotRequired[str],
        "groupingConfiguration": NotRequired[GroupingConfigurationOutputTypeDef],
        "isActive": NotRequired[bool],
        "language": NotRequired[str],
        "lastModifiedBy": NotRequired[str],
        "shortcutKey": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)
QuickResponseSearchResultDataTypeDef = TypedDict(
    "QuickResponseSearchResultDataTypeDef",
    {
        "contentType": str,
        "contents": QuickResponseContentsTypeDef,
        "createdTime": datetime,
        "isActive": bool,
        "knowledgeBaseArn": str,
        "knowledgeBaseId": str,
        "lastModifiedTime": datetime,
        "name": str,
        "quickResponseArn": str,
        "quickResponseId": str,
        "status": QuickResponseStatusType,
        "attributesInterpolated": NotRequired[List[str]],
        "attributesNotInterpolated": NotRequired[List[str]],
        "channels": NotRequired[List[str]],
        "description": NotRequired[str],
        "groupingConfiguration": NotRequired[GroupingConfigurationOutputTypeDef],
        "language": NotRequired[str],
        "lastModifiedBy": NotRequired[str],
        "shortcutKey": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)
SearchQuickResponsesRequestRequestTypeDef = TypedDict(
    "SearchQuickResponsesRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "searchExpression": QuickResponseSearchExpressionTypeDef,
        "attributes": NotRequired[Mapping[str, str]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
SearchQuickResponsesRequestSearchQuickResponsesPaginateTypeDef = TypedDict(
    "SearchQuickResponsesRequestSearchQuickResponsesPaginateTypeDef",
    {
        "knowledgeBaseId": str,
        "searchExpression": QuickResponseSearchExpressionTypeDef,
        "attributes": NotRequired[Mapping[str, str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
CreateSessionResponseTypeDef = TypedDict(
    "CreateSessionResponseTypeDef",
    {
        "session": SessionDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSessionResponseTypeDef = TypedDict(
    "GetSessionResponseTypeDef",
    {
        "session": SessionDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateKnowledgeBaseResponseTypeDef = TypedDict(
    "CreateKnowledgeBaseResponseTypeDef",
    {
        "knowledgeBase": KnowledgeBaseDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetKnowledgeBaseResponseTypeDef = TypedDict(
    "GetKnowledgeBaseResponseTypeDef",
    {
        "knowledgeBase": KnowledgeBaseDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateKnowledgeBaseTemplateUriResponseTypeDef = TypedDict(
    "UpdateKnowledgeBaseTemplateUriResponseTypeDef",
    {
        "knowledgeBase": KnowledgeBaseDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListKnowledgeBasesResponseTypeDef = TypedDict(
    "ListKnowledgeBasesResponseTypeDef",
    {
        "knowledgeBaseSummaries": List[KnowledgeBaseSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "CreateKnowledgeBaseRequestRequestTypeDef",
    {
        "knowledgeBaseType": KnowledgeBaseTypeType,
        "name": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "renderingConfiguration": NotRequired[RenderingConfigurationTypeDef],
        "serverSideEncryptionConfiguration": NotRequired[ServerSideEncryptionConfigurationTypeDef],
        "sourceConfiguration": NotRequired[SourceConfigurationTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateAssistantAssociationResponseTypeDef = TypedDict(
    "CreateAssistantAssociationResponseTypeDef",
    {
        "assistantAssociation": AssistantAssociationDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAssistantAssociationResponseTypeDef = TypedDict(
    "GetAssistantAssociationResponseTypeDef",
    {
        "assistantAssociation": AssistantAssociationDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssistantAssociationsResponseTypeDef = TypedDict(
    "ListAssistantAssociationsResponseTypeDef",
    {
        "assistantAssociationSummaries": List[AssistantAssociationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportJobDataTypeDef = TypedDict(
    "ImportJobDataTypeDef",
    {
        "createdTime": datetime,
        "importJobId": str,
        "importJobType": Literal["QUICK_RESPONSES"],
        "knowledgeBaseArn": str,
        "knowledgeBaseId": str,
        "lastModifiedTime": datetime,
        "status": ImportJobStatusType,
        "uploadId": str,
        "url": str,
        "urlExpiry": datetime,
        "externalSourceConfiguration": NotRequired[ExternalSourceConfigurationTypeDef],
        "failedRecordReport": NotRequired[str],
        "metadata": NotRequired[Dict[str, str]],
    },
)
ImportJobSummaryTypeDef = TypedDict(
    "ImportJobSummaryTypeDef",
    {
        "createdTime": datetime,
        "importJobId": str,
        "importJobType": Literal["QUICK_RESPONSES"],
        "knowledgeBaseArn": str,
        "knowledgeBaseId": str,
        "lastModifiedTime": datetime,
        "status": ImportJobStatusType,
        "uploadId": str,
        "externalSourceConfiguration": NotRequired[ExternalSourceConfigurationTypeDef],
        "metadata": NotRequired[Dict[str, str]],
    },
)
StartImportJobRequestRequestTypeDef = TypedDict(
    "StartImportJobRequestRequestTypeDef",
    {
        "importJobType": Literal["QUICK_RESPONSES"],
        "knowledgeBaseId": str,
        "uploadId": str,
        "clientToken": NotRequired[str],
        "externalSourceConfiguration": NotRequired[ExternalSourceConfigurationTypeDef],
        "metadata": NotRequired[Mapping[str, str]],
    },
)
RecommendationDataTypeDef = TypedDict(
    "RecommendationDataTypeDef",
    {
        "document": DocumentTypeDef,
        "recommendationId": str,
        "relevanceLevel": NotRequired[RelevanceLevelType],
        "relevanceScore": NotRequired[float],
        "type": NotRequired[Literal["KNOWLEDGE_CONTENT"]],
    },
)
ResultDataTypeDef = TypedDict(
    "ResultDataTypeDef",
    {
        "document": DocumentTypeDef,
        "resultId": str,
        "relevanceScore": NotRequired[float],
    },
)
CreateQuickResponseResponseTypeDef = TypedDict(
    "CreateQuickResponseResponseTypeDef",
    {
        "quickResponse": QuickResponseDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetQuickResponseResponseTypeDef = TypedDict(
    "GetQuickResponseResponseTypeDef",
    {
        "quickResponse": QuickResponseDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateQuickResponseResponseTypeDef = TypedDict(
    "UpdateQuickResponseResponseTypeDef",
    {
        "quickResponse": QuickResponseDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchQuickResponsesResponseTypeDef = TypedDict(
    "SearchQuickResponsesResponseTypeDef",
    {
        "nextToken": str,
        "results": List[QuickResponseSearchResultDataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetImportJobResponseTypeDef = TypedDict(
    "GetImportJobResponseTypeDef",
    {
        "importJob": ImportJobDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartImportJobResponseTypeDef = TypedDict(
    "StartImportJobResponseTypeDef",
    {
        "importJob": ImportJobDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListImportJobsResponseTypeDef = TypedDict(
    "ListImportJobsResponseTypeDef",
    {
        "importJobSummaries": List[ImportJobSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRecommendationsResponseTypeDef = TypedDict(
    "GetRecommendationsResponseTypeDef",
    {
        "recommendations": List[RecommendationDataTypeDef],
        "triggers": List[RecommendationTriggerTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
QueryAssistantResponseTypeDef = TypedDict(
    "QueryAssistantResponseTypeDef",
    {
        "nextToken": str,
        "results": List[ResultDataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
