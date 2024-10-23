"""
Type annotations for qconnect service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/type_defs/)

Usage::

    ```python
    from mypy_boto3_qconnect.type_defs import AIAgentConfigurationDataTypeDef

    data: AIAgentConfigurationDataTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    AIAgentTypeType,
    AIPromptAPIFormatType,
    AIPromptTypeType,
    AssistantCapabilityTypeType,
    AssistantStatusType,
    ChunkingStrategyType,
    ContentStatusType,
    ImportJobStatusType,
    KnowledgeBaseSearchTypeType,
    KnowledgeBaseStatusType,
    KnowledgeBaseTypeType,
    OrderType,
    OriginType,
    PriorityType,
    QueryResultTypeType,
    QuickResponseFilterOperatorType,
    QuickResponseQueryOperatorType,
    QuickResponseStatusType,
    RecommendationSourceTypeType,
    RecommendationTriggerTypeType,
    RecommendationTypeType,
    ReferenceTypeType,
    RelevanceLevelType,
    RelevanceType,
    StatusType,
    SyncStatusType,
    TargetTypeType,
    VisibilityStatusType,
    WebScopeTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AIAgentConfigurationDataTypeDef",
    "AIPromptSummaryTypeDef",
    "TextFullAIPromptEditTemplateConfigurationTypeDef",
    "AmazonConnectGuideAssociationDataTypeDef",
    "AppIntegrationsConfigurationOutputTypeDef",
    "AppIntegrationsConfigurationTypeDef",
    "AssistantAssociationInputDataTypeDef",
    "KnowledgeBaseAssociationDataTypeDef",
    "AssistantCapabilityConfigurationTypeDef",
    "AssistantIntegrationConfigurationTypeDef",
    "ServerSideEncryptionConfigurationTypeDef",
    "ParsingPromptTypeDef",
    "FixedSizeChunkingConfigurationTypeDef",
    "SemanticChunkingConfigurationTypeDef",
    "CitationSpanTypeDef",
    "ConnectConfigurationTypeDef",
    "RankingDataTypeDef",
    "ContentDataTypeDef",
    "GenerativeContentFeedbackDataTypeDef",
    "ContentReferenceTypeDef",
    "ContentSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "TimestampTypeDef",
    "CreateContentRequestRequestTypeDef",
    "RenderingConfigurationTypeDef",
    "GroupingConfigurationTypeDef",
    "QuickResponseDataProviderTypeDef",
    "IntentDetectedDataDetailsTypeDef",
    "GenerativeReferenceTypeDef",
    "DeleteAIAgentRequestRequestTypeDef",
    "DeleteAIAgentVersionRequestRequestTypeDef",
    "DeleteAIPromptRequestRequestTypeDef",
    "DeleteAIPromptVersionRequestRequestTypeDef",
    "DeleteAssistantAssociationRequestRequestTypeDef",
    "DeleteAssistantRequestRequestTypeDef",
    "DeleteContentAssociationRequestRequestTypeDef",
    "DeleteContentRequestRequestTypeDef",
    "DeleteImportJobRequestRequestTypeDef",
    "DeleteKnowledgeBaseRequestRequestTypeDef",
    "DeleteQuickResponseRequestRequestTypeDef",
    "HighlightTypeDef",
    "FilterTypeDef",
    "GetAIAgentRequestRequestTypeDef",
    "GetAIPromptRequestRequestTypeDef",
    "GetAssistantAssociationRequestRequestTypeDef",
    "GetAssistantRequestRequestTypeDef",
    "GetContentAssociationRequestRequestTypeDef",
    "GetContentRequestRequestTypeDef",
    "GetContentSummaryRequestRequestTypeDef",
    "GetImportJobRequestRequestTypeDef",
    "GetKnowledgeBaseRequestRequestTypeDef",
    "GetQuickResponseRequestRequestTypeDef",
    "GetRecommendationsRequestRequestTypeDef",
    "GetSessionRequestRequestTypeDef",
    "GroupingConfigurationOutputTypeDef",
    "HierarchicalChunkingLevelConfigurationTypeDef",
    "IntentInputDataTypeDef",
    "PaginatorConfigTypeDef",
    "ListAIAgentVersionsRequestRequestTypeDef",
    "ListAIAgentsRequestRequestTypeDef",
    "ListAIPromptVersionsRequestRequestTypeDef",
    "ListAIPromptsRequestRequestTypeDef",
    "ListAssistantAssociationsRequestRequestTypeDef",
    "ListAssistantsRequestRequestTypeDef",
    "ListContentAssociationsRequestRequestTypeDef",
    "ListContentsRequestRequestTypeDef",
    "ListImportJobsRequestRequestTypeDef",
    "ListKnowledgeBasesRequestRequestTypeDef",
    "ListQuickResponsesRequestRequestTypeDef",
    "QuickResponseSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "NotifyRecommendationsReceivedErrorTypeDef",
    "NotifyRecommendationsReceivedRequestRequestTypeDef",
    "TagConditionTypeDef",
    "QueryConditionItemTypeDef",
    "QueryTextInputDataTypeDef",
    "QueryRecommendationTriggerDataTypeDef",
    "QuickResponseContentProviderTypeDef",
    "QuickResponseFilterFieldTypeDef",
    "QuickResponseOrderFieldTypeDef",
    "QuickResponseQueryFieldTypeDef",
    "RemoveAssistantAIAgentRequestRequestTypeDef",
    "RemoveKnowledgeBaseTemplateUriRequestRequestTypeDef",
    "RuntimeSessionDataValueTypeDef",
    "SessionSummaryTypeDef",
    "SeedUrlTypeDef",
    "SessionIntegrationConfigurationTypeDef",
    "StartContentUploadRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateContentRequestRequestTypeDef",
    "UpdateKnowledgeBaseTemplateUriRequestRequestTypeDef",
    "WebCrawlerLimitsTypeDef",
    "UpdateAssistantAIAgentRequestRequestTypeDef",
    "AIPromptVersionSummaryTypeDef",
    "AIPromptTemplateConfigurationTypeDef",
    "ContentAssociationContentsTypeDef",
    "AppIntegrationsConfigurationUnionTypeDef",
    "CreateAssistantAssociationRequestRequestTypeDef",
    "AssistantAssociationOutputDataTypeDef",
    "AssistantDataTypeDef",
    "AssistantSummaryTypeDef",
    "CreateAssistantRequestRequestTypeDef",
    "BedrockFoundationModelConfigurationForParsingTypeDef",
    "ConfigurationTypeDef",
    "GenerativeDataDetailsPaginatorTypeDef",
    "GenerativeDataDetailsTypeDef",
    "ContentFeedbackDataTypeDef",
    "CreateContentResponseTypeDef",
    "GetContentResponseTypeDef",
    "GetContentSummaryResponseTypeDef",
    "ListAIPromptsResponseTypeDef",
    "ListContentsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "SearchContentResponseTypeDef",
    "StartContentUploadResponseTypeDef",
    "UpdateContentResponseTypeDef",
    "CreateAIAgentVersionRequestRequestTypeDef",
    "CreateAIPromptVersionRequestRequestTypeDef",
    "CreateQuickResponseRequestRequestTypeDef",
    "UpdateQuickResponseRequestRequestTypeDef",
    "DataReferenceTypeDef",
    "DocumentTextTypeDef",
    "SearchExpressionTypeDef",
    "HierarchicalChunkingConfigurationOutputTypeDef",
    "HierarchicalChunkingConfigurationTypeDef",
    "ListAIAgentVersionsRequestListAIAgentVersionsPaginateTypeDef",
    "ListAIAgentsRequestListAIAgentsPaginateTypeDef",
    "ListAIPromptVersionsRequestListAIPromptVersionsPaginateTypeDef",
    "ListAIPromptsRequestListAIPromptsPaginateTypeDef",
    "ListAssistantAssociationsRequestListAssistantAssociationsPaginateTypeDef",
    "ListAssistantsRequestListAssistantsPaginateTypeDef",
    "ListContentAssociationsRequestListContentAssociationsPaginateTypeDef",
    "ListContentsRequestListContentsPaginateTypeDef",
    "ListImportJobsRequestListImportJobsPaginateTypeDef",
    "ListKnowledgeBasesRequestListKnowledgeBasesPaginateTypeDef",
    "ListQuickResponsesRequestListQuickResponsesPaginateTypeDef",
    "ListQuickResponsesResponseTypeDef",
    "NotifyRecommendationsReceivedResponseTypeDef",
    "OrConditionOutputTypeDef",
    "OrConditionTypeDef",
    "QueryConditionTypeDef",
    "QueryInputDataTypeDef",
    "RecommendationTriggerDataTypeDef",
    "QuickResponseContentsTypeDef",
    "QuickResponseSearchExpressionTypeDef",
    "RuntimeSessionDataTypeDef",
    "SearchSessionsResponseTypeDef",
    "UrlConfigurationOutputTypeDef",
    "UrlConfigurationTypeDef",
    "ListAIPromptVersionsResponseTypeDef",
    "AIPromptDataTypeDef",
    "CreateAIPromptRequestRequestTypeDef",
    "UpdateAIPromptRequestRequestTypeDef",
    "ContentAssociationDataTypeDef",
    "ContentAssociationSummaryTypeDef",
    "CreateContentAssociationRequestRequestTypeDef",
    "AssistantAssociationDataTypeDef",
    "AssistantAssociationSummaryTypeDef",
    "CreateAssistantResponseTypeDef",
    "GetAssistantResponseTypeDef",
    "UpdateAssistantAIAgentResponseTypeDef",
    "ListAssistantsResponseTypeDef",
    "ParsingConfigurationTypeDef",
    "ExternalSourceConfigurationTypeDef",
    "PutFeedbackRequestRequestTypeDef",
    "PutFeedbackResponseTypeDef",
    "DocumentTypeDef",
    "TextDataTypeDef",
    "SearchContentRequestRequestTypeDef",
    "SearchContentRequestSearchContentPaginateTypeDef",
    "SearchSessionsRequestRequestTypeDef",
    "SearchSessionsRequestSearchSessionsPaginateTypeDef",
    "ChunkingConfigurationOutputTypeDef",
    "HierarchicalChunkingConfigurationUnionTypeDef",
    "TagFilterOutputTypeDef",
    "OrConditionUnionTypeDef",
    "QueryAssistantRequestQueryAssistantPaginateTypeDef",
    "QueryAssistantRequestRequestTypeDef",
    "RecommendationTriggerTypeDef",
    "QuickResponseDataTypeDef",
    "QuickResponseSearchResultDataTypeDef",
    "SearchQuickResponsesRequestRequestTypeDef",
    "SearchQuickResponsesRequestSearchQuickResponsesPaginateTypeDef",
    "UpdateSessionDataRequestRequestTypeDef",
    "UpdateSessionDataResponseTypeDef",
    "WebCrawlerConfigurationOutputTypeDef",
    "UrlConfigurationUnionTypeDef",
    "CreateAIPromptResponseTypeDef",
    "CreateAIPromptVersionResponseTypeDef",
    "GetAIPromptResponseTypeDef",
    "UpdateAIPromptResponseTypeDef",
    "CreateContentAssociationResponseTypeDef",
    "GetContentAssociationResponseTypeDef",
    "ListContentAssociationsResponseTypeDef",
    "CreateAssistantAssociationResponseTypeDef",
    "GetAssistantAssociationResponseTypeDef",
    "ListAssistantAssociationsResponseTypeDef",
    "ImportJobDataTypeDef",
    "ImportJobSummaryTypeDef",
    "StartImportJobRequestRequestTypeDef",
    "ContentDataDetailsTypeDef",
    "SourceContentDataDetailsTypeDef",
    "VectorIngestionConfigurationOutputTypeDef",
    "ChunkingConfigurationTypeDef",
    "KnowledgeBaseAssociationConfigurationDataOutputTypeDef",
    "SessionDataTypeDef",
    "TagFilterTypeDef",
    "CreateQuickResponseResponseTypeDef",
    "GetQuickResponseResponseTypeDef",
    "UpdateQuickResponseResponseTypeDef",
    "SearchQuickResponsesResponseTypeDef",
    "ManagedSourceConfigurationOutputTypeDef",
    "WebCrawlerConfigurationTypeDef",
    "GetImportJobResponseTypeDef",
    "StartImportJobResponseTypeDef",
    "ListImportJobsResponseTypeDef",
    "DataDetailsPaginatorTypeDef",
    "DataDetailsTypeDef",
    "ChunkingConfigurationUnionTypeDef",
    "AssociationConfigurationDataOutputTypeDef",
    "CreateSessionResponseTypeDef",
    "GetSessionResponseTypeDef",
    "UpdateSessionResponseTypeDef",
    "CreateSessionRequestRequestTypeDef",
    "TagFilterUnionTypeDef",
    "UpdateSessionRequestRequestTypeDef",
    "SourceConfigurationOutputTypeDef",
    "WebCrawlerConfigurationUnionTypeDef",
    "DataSummaryPaginatorTypeDef",
    "DataSummaryTypeDef",
    "VectorIngestionConfigurationTypeDef",
    "AssociationConfigurationOutputTypeDef",
    "KnowledgeBaseAssociationConfigurationDataTypeDef",
    "KnowledgeBaseDataTypeDef",
    "KnowledgeBaseSummaryTypeDef",
    "ManagedSourceConfigurationTypeDef",
    "ResultDataPaginatorTypeDef",
    "RecommendationDataTypeDef",
    "ResultDataTypeDef",
    "AnswerRecommendationAIAgentConfigurationOutputTypeDef",
    "ManualSearchAIAgentConfigurationOutputTypeDef",
    "KnowledgeBaseAssociationConfigurationDataUnionTypeDef",
    "CreateKnowledgeBaseResponseTypeDef",
    "GetKnowledgeBaseResponseTypeDef",
    "UpdateKnowledgeBaseTemplateUriResponseTypeDef",
    "ListKnowledgeBasesResponseTypeDef",
    "ManagedSourceConfigurationUnionTypeDef",
    "QueryAssistantResponsePaginatorTypeDef",
    "GetRecommendationsResponseTypeDef",
    "QueryAssistantResponseTypeDef",
    "AIAgentConfigurationOutputTypeDef",
    "AssociationConfigurationDataTypeDef",
    "SourceConfigurationTypeDef",
    "AIAgentDataTypeDef",
    "AIAgentSummaryTypeDef",
    "AssociationConfigurationDataUnionTypeDef",
    "CreateKnowledgeBaseRequestRequestTypeDef",
    "CreateAIAgentResponseTypeDef",
    "CreateAIAgentVersionResponseTypeDef",
    "GetAIAgentResponseTypeDef",
    "UpdateAIAgentResponseTypeDef",
    "AIAgentVersionSummaryTypeDef",
    "ListAIAgentsResponseTypeDef",
    "AssociationConfigurationTypeDef",
    "ListAIAgentVersionsResponseTypeDef",
    "AssociationConfigurationUnionTypeDef",
    "ManualSearchAIAgentConfigurationTypeDef",
    "AnswerRecommendationAIAgentConfigurationTypeDef",
    "ManualSearchAIAgentConfigurationUnionTypeDef",
    "AnswerRecommendationAIAgentConfigurationUnionTypeDef",
    "AIAgentConfigurationTypeDef",
    "CreateAIAgentRequestRequestTypeDef",
    "UpdateAIAgentRequestRequestTypeDef",
)

AIAgentConfigurationDataTypeDef = TypedDict(
    "AIAgentConfigurationDataTypeDef",
    {
        "aiAgentId": str,
    },
)
AIPromptSummaryTypeDef = TypedDict(
    "AIPromptSummaryTypeDef",
    {
        "aiPromptArn": str,
        "aiPromptId": str,
        "apiFormat": AIPromptAPIFormatType,
        "assistantArn": str,
        "assistantId": str,
        "modelId": str,
        "name": str,
        "templateType": Literal["TEXT"],
        "type": AIPromptTypeType,
        "visibilityStatus": VisibilityStatusType,
        "description": NotRequired[str],
        "modifiedTime": NotRequired[datetime],
        "origin": NotRequired[OriginType],
        "status": NotRequired[StatusType],
        "tags": NotRequired[Dict[str, str]],
    },
)
TextFullAIPromptEditTemplateConfigurationTypeDef = TypedDict(
    "TextFullAIPromptEditTemplateConfigurationTypeDef",
    {
        "text": str,
    },
)
AmazonConnectGuideAssociationDataTypeDef = TypedDict(
    "AmazonConnectGuideAssociationDataTypeDef",
    {
        "flowId": NotRequired[str],
    },
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
AssistantCapabilityConfigurationTypeDef = TypedDict(
    "AssistantCapabilityConfigurationTypeDef",
    {
        "type": NotRequired[AssistantCapabilityTypeType],
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
ParsingPromptTypeDef = TypedDict(
    "ParsingPromptTypeDef",
    {
        "parsingPromptText": str,
    },
)
FixedSizeChunkingConfigurationTypeDef = TypedDict(
    "FixedSizeChunkingConfigurationTypeDef",
    {
        "maxTokens": int,
        "overlapPercentage": int,
    },
)
SemanticChunkingConfigurationTypeDef = TypedDict(
    "SemanticChunkingConfigurationTypeDef",
    {
        "breakpointPercentileThreshold": int,
        "bufferSize": int,
        "maxTokens": int,
    },
)
CitationSpanTypeDef = TypedDict(
    "CitationSpanTypeDef",
    {
        "beginOffsetInclusive": NotRequired[int],
        "endOffsetExclusive": NotRequired[int],
    },
)
ConnectConfigurationTypeDef = TypedDict(
    "ConnectConfigurationTypeDef",
    {
        "instanceId": NotRequired[str],
    },
)
RankingDataTypeDef = TypedDict(
    "RankingDataTypeDef",
    {
        "relevanceLevel": NotRequired[RelevanceLevelType],
        "relevanceScore": NotRequired[float],
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
GenerativeContentFeedbackDataTypeDef = TypedDict(
    "GenerativeContentFeedbackDataTypeDef",
    {
        "relevance": RelevanceType,
    },
)
ContentReferenceTypeDef = TypedDict(
    "ContentReferenceTypeDef",
    {
        "contentArn": NotRequired[str],
        "contentId": NotRequired[str],
        "knowledgeBaseArn": NotRequired[str],
        "knowledgeBaseId": NotRequired[str],
        "referenceType": NotRequired[ReferenceTypeType],
        "sourceURL": NotRequired[str],
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
TimestampTypeDef = Union[datetime, str]
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
IntentDetectedDataDetailsTypeDef = TypedDict(
    "IntentDetectedDataDetailsTypeDef",
    {
        "intent": str,
        "intentId": str,
    },
)
GenerativeReferenceTypeDef = TypedDict(
    "GenerativeReferenceTypeDef",
    {
        "generationId": NotRequired[str],
        "modelId": NotRequired[str],
    },
)
DeleteAIAgentRequestRequestTypeDef = TypedDict(
    "DeleteAIAgentRequestRequestTypeDef",
    {
        "aiAgentId": str,
        "assistantId": str,
    },
)
DeleteAIAgentVersionRequestRequestTypeDef = TypedDict(
    "DeleteAIAgentVersionRequestRequestTypeDef",
    {
        "aiAgentId": str,
        "assistantId": str,
        "versionNumber": int,
    },
)
DeleteAIPromptRequestRequestTypeDef = TypedDict(
    "DeleteAIPromptRequestRequestTypeDef",
    {
        "aiPromptId": str,
        "assistantId": str,
    },
)
DeleteAIPromptVersionRequestRequestTypeDef = TypedDict(
    "DeleteAIPromptVersionRequestRequestTypeDef",
    {
        "aiPromptId": str,
        "assistantId": str,
        "versionNumber": int,
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
DeleteContentAssociationRequestRequestTypeDef = TypedDict(
    "DeleteContentAssociationRequestRequestTypeDef",
    {
        "contentAssociationId": str,
        "contentId": str,
        "knowledgeBaseId": str,
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
GetAIAgentRequestRequestTypeDef = TypedDict(
    "GetAIAgentRequestRequestTypeDef",
    {
        "aiAgentId": str,
        "assistantId": str,
    },
)
GetAIPromptRequestRequestTypeDef = TypedDict(
    "GetAIPromptRequestRequestTypeDef",
    {
        "aiPromptId": str,
        "assistantId": str,
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
GetContentAssociationRequestRequestTypeDef = TypedDict(
    "GetContentAssociationRequestRequestTypeDef",
    {
        "contentAssociationId": str,
        "contentId": str,
        "knowledgeBaseId": str,
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
HierarchicalChunkingLevelConfigurationTypeDef = TypedDict(
    "HierarchicalChunkingLevelConfigurationTypeDef",
    {
        "maxTokens": int,
    },
)
IntentInputDataTypeDef = TypedDict(
    "IntentInputDataTypeDef",
    {
        "intentId": str,
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
ListAIAgentVersionsRequestRequestTypeDef = TypedDict(
    "ListAIAgentVersionsRequestRequestTypeDef",
    {
        "aiAgentId": str,
        "assistantId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "origin": NotRequired[OriginType],
    },
)
ListAIAgentsRequestRequestTypeDef = TypedDict(
    "ListAIAgentsRequestRequestTypeDef",
    {
        "assistantId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "origin": NotRequired[OriginType],
    },
)
ListAIPromptVersionsRequestRequestTypeDef = TypedDict(
    "ListAIPromptVersionsRequestRequestTypeDef",
    {
        "aiPromptId": str,
        "assistantId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "origin": NotRequired[OriginType],
    },
)
ListAIPromptsRequestRequestTypeDef = TypedDict(
    "ListAIPromptsRequestRequestTypeDef",
    {
        "assistantId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "origin": NotRequired[OriginType],
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
ListContentAssociationsRequestRequestTypeDef = TypedDict(
    "ListContentAssociationsRequestRequestTypeDef",
    {
        "contentId": str,
        "knowledgeBaseId": str,
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
TagConditionTypeDef = TypedDict(
    "TagConditionTypeDef",
    {
        "key": str,
        "value": NotRequired[str],
    },
)
QueryConditionItemTypeDef = TypedDict(
    "QueryConditionItemTypeDef",
    {
        "comparator": Literal["EQUALS"],
        "field": Literal["RESULT_TYPE"],
        "value": str,
    },
)
QueryTextInputDataTypeDef = TypedDict(
    "QueryTextInputDataTypeDef",
    {
        "text": str,
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
RemoveAssistantAIAgentRequestRequestTypeDef = TypedDict(
    "RemoveAssistantAIAgentRequestRequestTypeDef",
    {
        "aiAgentType": AIAgentTypeType,
        "assistantId": str,
    },
)
RemoveKnowledgeBaseTemplateUriRequestRequestTypeDef = TypedDict(
    "RemoveKnowledgeBaseTemplateUriRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
    },
)
RuntimeSessionDataValueTypeDef = TypedDict(
    "RuntimeSessionDataValueTypeDef",
    {
        "stringValue": NotRequired[str],
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
SeedUrlTypeDef = TypedDict(
    "SeedUrlTypeDef",
    {
        "url": NotRequired[str],
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
WebCrawlerLimitsTypeDef = TypedDict(
    "WebCrawlerLimitsTypeDef",
    {
        "rateLimit": NotRequired[int],
    },
)
UpdateAssistantAIAgentRequestRequestTypeDef = TypedDict(
    "UpdateAssistantAIAgentRequestRequestTypeDef",
    {
        "aiAgentType": AIAgentTypeType,
        "assistantId": str,
        "configuration": AIAgentConfigurationDataTypeDef,
    },
)
AIPromptVersionSummaryTypeDef = TypedDict(
    "AIPromptVersionSummaryTypeDef",
    {
        "aiPromptSummary": NotRequired[AIPromptSummaryTypeDef],
        "versionNumber": NotRequired[int],
    },
)
AIPromptTemplateConfigurationTypeDef = TypedDict(
    "AIPromptTemplateConfigurationTypeDef",
    {
        "textFullAIPromptEditTemplateConfiguration": NotRequired[
            TextFullAIPromptEditTemplateConfigurationTypeDef
        ],
    },
)
ContentAssociationContentsTypeDef = TypedDict(
    "ContentAssociationContentsTypeDef",
    {
        "amazonConnectGuideAssociation": NotRequired[AmazonConnectGuideAssociationDataTypeDef],
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
        "aiAgentConfiguration": NotRequired[Dict[AIAgentTypeType, AIAgentConfigurationDataTypeDef]],
        "capabilityConfiguration": NotRequired[AssistantCapabilityConfigurationTypeDef],
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
        "aiAgentConfiguration": NotRequired[Dict[AIAgentTypeType, AIAgentConfigurationDataTypeDef]],
        "capabilityConfiguration": NotRequired[AssistantCapabilityConfigurationTypeDef],
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
BedrockFoundationModelConfigurationForParsingTypeDef = TypedDict(
    "BedrockFoundationModelConfigurationForParsingTypeDef",
    {
        "modelArn": str,
        "parsingPrompt": NotRequired[ParsingPromptTypeDef],
    },
)
ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "connectConfiguration": NotRequired[ConnectConfigurationTypeDef],
    },
)
GenerativeDataDetailsPaginatorTypeDef = TypedDict(
    "GenerativeDataDetailsPaginatorTypeDef",
    {
        "completion": str,
        "rankingData": RankingDataTypeDef,
        "references": List[Dict[str, Any]],
    },
)
GenerativeDataDetailsTypeDef = TypedDict(
    "GenerativeDataDetailsTypeDef",
    {
        "completion": str,
        "rankingData": RankingDataTypeDef,
        "references": List[Dict[str, Any]],
    },
)
ContentFeedbackDataTypeDef = TypedDict(
    "ContentFeedbackDataTypeDef",
    {
        "generativeContentFeedbackData": NotRequired[GenerativeContentFeedbackDataTypeDef],
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
ListAIPromptsResponseTypeDef = TypedDict(
    "ListAIPromptsResponseTypeDef",
    {
        "aiPromptSummaries": List[AIPromptSummaryTypeDef],
        "nextToken": str,
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
CreateAIAgentVersionRequestRequestTypeDef = TypedDict(
    "CreateAIAgentVersionRequestRequestTypeDef",
    {
        "aiAgentId": str,
        "assistantId": str,
        "clientToken": NotRequired[str],
        "modifiedTime": NotRequired[TimestampTypeDef],
    },
)
CreateAIPromptVersionRequestRequestTypeDef = TypedDict(
    "CreateAIPromptVersionRequestRequestTypeDef",
    {
        "aiPromptId": str,
        "assistantId": str,
        "clientToken": NotRequired[str],
        "modifiedTime": NotRequired[TimestampTypeDef],
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
DataReferenceTypeDef = TypedDict(
    "DataReferenceTypeDef",
    {
        "contentReference": NotRequired[ContentReferenceTypeDef],
        "generativeReference": NotRequired[GenerativeReferenceTypeDef],
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
HierarchicalChunkingConfigurationOutputTypeDef = TypedDict(
    "HierarchicalChunkingConfigurationOutputTypeDef",
    {
        "levelConfigurations": List[HierarchicalChunkingLevelConfigurationTypeDef],
        "overlapTokens": int,
    },
)
HierarchicalChunkingConfigurationTypeDef = TypedDict(
    "HierarchicalChunkingConfigurationTypeDef",
    {
        "levelConfigurations": Sequence[HierarchicalChunkingLevelConfigurationTypeDef],
        "overlapTokens": int,
    },
)
ListAIAgentVersionsRequestListAIAgentVersionsPaginateTypeDef = TypedDict(
    "ListAIAgentVersionsRequestListAIAgentVersionsPaginateTypeDef",
    {
        "aiAgentId": str,
        "assistantId": str,
        "origin": NotRequired[OriginType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAIAgentsRequestListAIAgentsPaginateTypeDef = TypedDict(
    "ListAIAgentsRequestListAIAgentsPaginateTypeDef",
    {
        "assistantId": str,
        "origin": NotRequired[OriginType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAIPromptVersionsRequestListAIPromptVersionsPaginateTypeDef = TypedDict(
    "ListAIPromptVersionsRequestListAIPromptVersionsPaginateTypeDef",
    {
        "aiPromptId": str,
        "assistantId": str,
        "origin": NotRequired[OriginType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAIPromptsRequestListAIPromptsPaginateTypeDef = TypedDict(
    "ListAIPromptsRequestListAIPromptsPaginateTypeDef",
    {
        "assistantId": str,
        "origin": NotRequired[OriginType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
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
ListContentAssociationsRequestListContentAssociationsPaginateTypeDef = TypedDict(
    "ListContentAssociationsRequestListContentAssociationsPaginateTypeDef",
    {
        "contentId": str,
        "knowledgeBaseId": str,
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
OrConditionOutputTypeDef = TypedDict(
    "OrConditionOutputTypeDef",
    {
        "andConditions": NotRequired[List[TagConditionTypeDef]],
        "tagCondition": NotRequired[TagConditionTypeDef],
    },
)
OrConditionTypeDef = TypedDict(
    "OrConditionTypeDef",
    {
        "andConditions": NotRequired[Sequence[TagConditionTypeDef]],
        "tagCondition": NotRequired[TagConditionTypeDef],
    },
)
QueryConditionTypeDef = TypedDict(
    "QueryConditionTypeDef",
    {
        "single": NotRequired[QueryConditionItemTypeDef],
    },
)
QueryInputDataTypeDef = TypedDict(
    "QueryInputDataTypeDef",
    {
        "intentInputData": NotRequired[IntentInputDataTypeDef],
        "queryTextInputData": NotRequired[QueryTextInputDataTypeDef],
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
RuntimeSessionDataTypeDef = TypedDict(
    "RuntimeSessionDataTypeDef",
    {
        "key": str,
        "value": RuntimeSessionDataValueTypeDef,
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
UrlConfigurationOutputTypeDef = TypedDict(
    "UrlConfigurationOutputTypeDef",
    {
        "seedUrls": NotRequired[List[SeedUrlTypeDef]],
    },
)
UrlConfigurationTypeDef = TypedDict(
    "UrlConfigurationTypeDef",
    {
        "seedUrls": NotRequired[Sequence[SeedUrlTypeDef]],
    },
)
ListAIPromptVersionsResponseTypeDef = TypedDict(
    "ListAIPromptVersionsResponseTypeDef",
    {
        "aiPromptVersionSummaries": List[AIPromptVersionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AIPromptDataTypeDef = TypedDict(
    "AIPromptDataTypeDef",
    {
        "aiPromptArn": str,
        "aiPromptId": str,
        "apiFormat": AIPromptAPIFormatType,
        "assistantArn": str,
        "assistantId": str,
        "modelId": str,
        "name": str,
        "templateConfiguration": AIPromptTemplateConfigurationTypeDef,
        "templateType": Literal["TEXT"],
        "type": AIPromptTypeType,
        "visibilityStatus": VisibilityStatusType,
        "description": NotRequired[str],
        "modifiedTime": NotRequired[datetime],
        "origin": NotRequired[OriginType],
        "status": NotRequired[StatusType],
        "tags": NotRequired[Dict[str, str]],
    },
)
CreateAIPromptRequestRequestTypeDef = TypedDict(
    "CreateAIPromptRequestRequestTypeDef",
    {
        "apiFormat": AIPromptAPIFormatType,
        "assistantId": str,
        "modelId": str,
        "name": str,
        "templateConfiguration": AIPromptTemplateConfigurationTypeDef,
        "templateType": Literal["TEXT"],
        "type": AIPromptTypeType,
        "visibilityStatus": VisibilityStatusType,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
UpdateAIPromptRequestRequestTypeDef = TypedDict(
    "UpdateAIPromptRequestRequestTypeDef",
    {
        "aiPromptId": str,
        "assistantId": str,
        "visibilityStatus": VisibilityStatusType,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "templateConfiguration": NotRequired[AIPromptTemplateConfigurationTypeDef],
    },
)
ContentAssociationDataTypeDef = TypedDict(
    "ContentAssociationDataTypeDef",
    {
        "associationData": ContentAssociationContentsTypeDef,
        "associationType": Literal["AMAZON_CONNECT_GUIDE"],
        "contentArn": str,
        "contentAssociationArn": str,
        "contentAssociationId": str,
        "contentId": str,
        "knowledgeBaseArn": str,
        "knowledgeBaseId": str,
        "tags": NotRequired[Dict[str, str]],
    },
)
ContentAssociationSummaryTypeDef = TypedDict(
    "ContentAssociationSummaryTypeDef",
    {
        "associationData": ContentAssociationContentsTypeDef,
        "associationType": Literal["AMAZON_CONNECT_GUIDE"],
        "contentArn": str,
        "contentAssociationArn": str,
        "contentAssociationId": str,
        "contentId": str,
        "knowledgeBaseArn": str,
        "knowledgeBaseId": str,
        "tags": NotRequired[Dict[str, str]],
    },
)
CreateContentAssociationRequestRequestTypeDef = TypedDict(
    "CreateContentAssociationRequestRequestTypeDef",
    {
        "association": ContentAssociationContentsTypeDef,
        "associationType": Literal["AMAZON_CONNECT_GUIDE"],
        "contentId": str,
        "knowledgeBaseId": str,
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
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
UpdateAssistantAIAgentResponseTypeDef = TypedDict(
    "UpdateAssistantAIAgentResponseTypeDef",
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
ParsingConfigurationTypeDef = TypedDict(
    "ParsingConfigurationTypeDef",
    {
        "parsingStrategy": Literal["BEDROCK_FOUNDATION_MODEL"],
        "bedrockFoundationModelConfiguration": NotRequired[
            BedrockFoundationModelConfigurationForParsingTypeDef
        ],
    },
)
ExternalSourceConfigurationTypeDef = TypedDict(
    "ExternalSourceConfigurationTypeDef",
    {
        "configuration": ConfigurationTypeDef,
        "source": Literal["AMAZON_CONNECT"],
    },
)
PutFeedbackRequestRequestTypeDef = TypedDict(
    "PutFeedbackRequestRequestTypeDef",
    {
        "assistantId": str,
        "contentFeedback": ContentFeedbackDataTypeDef,
        "targetId": str,
        "targetType": TargetTypeType,
    },
)
PutFeedbackResponseTypeDef = TypedDict(
    "PutFeedbackResponseTypeDef",
    {
        "assistantArn": str,
        "assistantId": str,
        "contentFeedback": ContentFeedbackDataTypeDef,
        "targetId": str,
        "targetType": TargetTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
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
TextDataTypeDef = TypedDict(
    "TextDataTypeDef",
    {
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
ChunkingConfigurationOutputTypeDef = TypedDict(
    "ChunkingConfigurationOutputTypeDef",
    {
        "chunkingStrategy": ChunkingStrategyType,
        "fixedSizeChunkingConfiguration": NotRequired[FixedSizeChunkingConfigurationTypeDef],
        "hierarchicalChunkingConfiguration": NotRequired[
            HierarchicalChunkingConfigurationOutputTypeDef
        ],
        "semanticChunkingConfiguration": NotRequired[SemanticChunkingConfigurationTypeDef],
    },
)
HierarchicalChunkingConfigurationUnionTypeDef = Union[
    HierarchicalChunkingConfigurationTypeDef, HierarchicalChunkingConfigurationOutputTypeDef
]
TagFilterOutputTypeDef = TypedDict(
    "TagFilterOutputTypeDef",
    {
        "andConditions": NotRequired[List[TagConditionTypeDef]],
        "orConditions": NotRequired[List[OrConditionOutputTypeDef]],
        "tagCondition": NotRequired[TagConditionTypeDef],
    },
)
OrConditionUnionTypeDef = Union[OrConditionTypeDef, OrConditionOutputTypeDef]
QueryAssistantRequestQueryAssistantPaginateTypeDef = TypedDict(
    "QueryAssistantRequestQueryAssistantPaginateTypeDef",
    {
        "assistantId": str,
        "overrideKnowledgeBaseSearchType": NotRequired[KnowledgeBaseSearchTypeType],
        "queryCondition": NotRequired[Sequence[QueryConditionTypeDef]],
        "queryInputData": NotRequired[QueryInputDataTypeDef],
        "queryText": NotRequired[str],
        "sessionId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
QueryAssistantRequestRequestTypeDef = TypedDict(
    "QueryAssistantRequestRequestTypeDef",
    {
        "assistantId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "overrideKnowledgeBaseSearchType": NotRequired[KnowledgeBaseSearchTypeType],
        "queryCondition": NotRequired[Sequence[QueryConditionTypeDef]],
        "queryInputData": NotRequired[QueryInputDataTypeDef],
        "queryText": NotRequired[str],
        "sessionId": NotRequired[str],
    },
)
RecommendationTriggerTypeDef = TypedDict(
    "RecommendationTriggerTypeDef",
    {
        "data": RecommendationTriggerDataTypeDef,
        "id": str,
        "recommendationIds": List[str],
        "source": RecommendationSourceTypeType,
        "type": RecommendationTriggerTypeType,
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
UpdateSessionDataRequestRequestTypeDef = TypedDict(
    "UpdateSessionDataRequestRequestTypeDef",
    {
        "assistantId": str,
        "data": Sequence[RuntimeSessionDataTypeDef],
        "sessionId": str,
        "namespace": NotRequired[Literal["Custom"]],
    },
)
UpdateSessionDataResponseTypeDef = TypedDict(
    "UpdateSessionDataResponseTypeDef",
    {
        "data": List[RuntimeSessionDataTypeDef],
        "namespace": Literal["Custom"],
        "sessionArn": str,
        "sessionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
WebCrawlerConfigurationOutputTypeDef = TypedDict(
    "WebCrawlerConfigurationOutputTypeDef",
    {
        "urlConfiguration": UrlConfigurationOutputTypeDef,
        "crawlerLimits": NotRequired[WebCrawlerLimitsTypeDef],
        "exclusionFilters": NotRequired[List[str]],
        "inclusionFilters": NotRequired[List[str]],
        "scope": NotRequired[WebScopeTypeType],
    },
)
UrlConfigurationUnionTypeDef = Union[UrlConfigurationTypeDef, UrlConfigurationOutputTypeDef]
CreateAIPromptResponseTypeDef = TypedDict(
    "CreateAIPromptResponseTypeDef",
    {
        "aiPrompt": AIPromptDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAIPromptVersionResponseTypeDef = TypedDict(
    "CreateAIPromptVersionResponseTypeDef",
    {
        "aiPrompt": AIPromptDataTypeDef,
        "versionNumber": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAIPromptResponseTypeDef = TypedDict(
    "GetAIPromptResponseTypeDef",
    {
        "aiPrompt": AIPromptDataTypeDef,
        "versionNumber": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAIPromptResponseTypeDef = TypedDict(
    "UpdateAIPromptResponseTypeDef",
    {
        "aiPrompt": AIPromptDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateContentAssociationResponseTypeDef = TypedDict(
    "CreateContentAssociationResponseTypeDef",
    {
        "contentAssociation": ContentAssociationDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetContentAssociationResponseTypeDef = TypedDict(
    "GetContentAssociationResponseTypeDef",
    {
        "contentAssociation": ContentAssociationDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListContentAssociationsResponseTypeDef = TypedDict(
    "ListContentAssociationsResponseTypeDef",
    {
        "contentAssociationSummaries": List[ContentAssociationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
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
ContentDataDetailsTypeDef = TypedDict(
    "ContentDataDetailsTypeDef",
    {
        "rankingData": RankingDataTypeDef,
        "textData": TextDataTypeDef,
    },
)
SourceContentDataDetailsTypeDef = TypedDict(
    "SourceContentDataDetailsTypeDef",
    {
        "id": str,
        "rankingData": RankingDataTypeDef,
        "textData": TextDataTypeDef,
        "type": Literal["KNOWLEDGE_CONTENT"],
        "citationSpan": NotRequired[CitationSpanTypeDef],
    },
)
VectorIngestionConfigurationOutputTypeDef = TypedDict(
    "VectorIngestionConfigurationOutputTypeDef",
    {
        "chunkingConfiguration": NotRequired[ChunkingConfigurationOutputTypeDef],
        "parsingConfiguration": NotRequired[ParsingConfigurationTypeDef],
    },
)
ChunkingConfigurationTypeDef = TypedDict(
    "ChunkingConfigurationTypeDef",
    {
        "chunkingStrategy": ChunkingStrategyType,
        "fixedSizeChunkingConfiguration": NotRequired[FixedSizeChunkingConfigurationTypeDef],
        "hierarchicalChunkingConfiguration": NotRequired[
            HierarchicalChunkingConfigurationUnionTypeDef
        ],
        "semanticChunkingConfiguration": NotRequired[SemanticChunkingConfigurationTypeDef],
    },
)
KnowledgeBaseAssociationConfigurationDataOutputTypeDef = TypedDict(
    "KnowledgeBaseAssociationConfigurationDataOutputTypeDef",
    {
        "contentTagFilter": NotRequired[TagFilterOutputTypeDef],
        "maxResults": NotRequired[int],
        "overrideKnowledgeBaseSearchType": NotRequired[KnowledgeBaseSearchTypeType],
    },
)
SessionDataTypeDef = TypedDict(
    "SessionDataTypeDef",
    {
        "name": str,
        "sessionArn": str,
        "sessionId": str,
        "aiAgentConfiguration": NotRequired[Dict[AIAgentTypeType, AIAgentConfigurationDataTypeDef]],
        "description": NotRequired[str],
        "integrationConfiguration": NotRequired[SessionIntegrationConfigurationTypeDef],
        "tagFilter": NotRequired[TagFilterOutputTypeDef],
        "tags": NotRequired[Dict[str, str]],
    },
)
TagFilterTypeDef = TypedDict(
    "TagFilterTypeDef",
    {
        "andConditions": NotRequired[Sequence[TagConditionTypeDef]],
        "orConditions": NotRequired[Sequence[OrConditionUnionTypeDef]],
        "tagCondition": NotRequired[TagConditionTypeDef],
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
ManagedSourceConfigurationOutputTypeDef = TypedDict(
    "ManagedSourceConfigurationOutputTypeDef",
    {
        "webCrawlerConfiguration": NotRequired[WebCrawlerConfigurationOutputTypeDef],
    },
)
WebCrawlerConfigurationTypeDef = TypedDict(
    "WebCrawlerConfigurationTypeDef",
    {
        "urlConfiguration": UrlConfigurationUnionTypeDef,
        "crawlerLimits": NotRequired[WebCrawlerLimitsTypeDef],
        "exclusionFilters": NotRequired[Sequence[str]],
        "inclusionFilters": NotRequired[Sequence[str]],
        "scope": NotRequired[WebScopeTypeType],
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
DataDetailsPaginatorTypeDef = TypedDict(
    "DataDetailsPaginatorTypeDef",
    {
        "contentData": NotRequired[ContentDataDetailsTypeDef],
        "generativeData": NotRequired[GenerativeDataDetailsPaginatorTypeDef],
        "intentDetectedData": NotRequired[IntentDetectedDataDetailsTypeDef],
        "sourceContentData": NotRequired[SourceContentDataDetailsTypeDef],
    },
)
DataDetailsTypeDef = TypedDict(
    "DataDetailsTypeDef",
    {
        "contentData": NotRequired[ContentDataDetailsTypeDef],
        "generativeData": NotRequired[GenerativeDataDetailsTypeDef],
        "intentDetectedData": NotRequired[IntentDetectedDataDetailsTypeDef],
        "sourceContentData": NotRequired[SourceContentDataDetailsTypeDef],
    },
)
ChunkingConfigurationUnionTypeDef = Union[
    ChunkingConfigurationTypeDef, ChunkingConfigurationOutputTypeDef
]
AssociationConfigurationDataOutputTypeDef = TypedDict(
    "AssociationConfigurationDataOutputTypeDef",
    {
        "knowledgeBaseAssociationConfigurationData": NotRequired[
            KnowledgeBaseAssociationConfigurationDataOutputTypeDef
        ],
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
UpdateSessionResponseTypeDef = TypedDict(
    "UpdateSessionResponseTypeDef",
    {
        "session": SessionDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSessionRequestRequestTypeDef = TypedDict(
    "CreateSessionRequestRequestTypeDef",
    {
        "assistantId": str,
        "name": str,
        "aiAgentConfiguration": NotRequired[
            Mapping[AIAgentTypeType, AIAgentConfigurationDataTypeDef]
        ],
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "tagFilter": NotRequired[TagFilterTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
TagFilterUnionTypeDef = Union[TagFilterTypeDef, TagFilterOutputTypeDef]
UpdateSessionRequestRequestTypeDef = TypedDict(
    "UpdateSessionRequestRequestTypeDef",
    {
        "assistantId": str,
        "sessionId": str,
        "aiAgentConfiguration": NotRequired[
            Mapping[AIAgentTypeType, AIAgentConfigurationDataTypeDef]
        ],
        "description": NotRequired[str],
        "tagFilter": NotRequired[TagFilterTypeDef],
    },
)
SourceConfigurationOutputTypeDef = TypedDict(
    "SourceConfigurationOutputTypeDef",
    {
        "appIntegrations": NotRequired[AppIntegrationsConfigurationOutputTypeDef],
        "managedSourceConfiguration": NotRequired[ManagedSourceConfigurationOutputTypeDef],
    },
)
WebCrawlerConfigurationUnionTypeDef = Union[
    WebCrawlerConfigurationTypeDef, WebCrawlerConfigurationOutputTypeDef
]
DataSummaryPaginatorTypeDef = TypedDict(
    "DataSummaryPaginatorTypeDef",
    {
        "details": DataDetailsPaginatorTypeDef,
        "reference": DataReferenceTypeDef,
    },
)
DataSummaryTypeDef = TypedDict(
    "DataSummaryTypeDef",
    {
        "details": DataDetailsTypeDef,
        "reference": DataReferenceTypeDef,
    },
)
VectorIngestionConfigurationTypeDef = TypedDict(
    "VectorIngestionConfigurationTypeDef",
    {
        "chunkingConfiguration": NotRequired[ChunkingConfigurationUnionTypeDef],
        "parsingConfiguration": NotRequired[ParsingConfigurationTypeDef],
    },
)
AssociationConfigurationOutputTypeDef = TypedDict(
    "AssociationConfigurationOutputTypeDef",
    {
        "associationConfigurationData": NotRequired[AssociationConfigurationDataOutputTypeDef],
        "associationId": NotRequired[str],
        "associationType": NotRequired[Literal["KNOWLEDGE_BASE"]],
    },
)
KnowledgeBaseAssociationConfigurationDataTypeDef = TypedDict(
    "KnowledgeBaseAssociationConfigurationDataTypeDef",
    {
        "contentTagFilter": NotRequired[TagFilterUnionTypeDef],
        "maxResults": NotRequired[int],
        "overrideKnowledgeBaseSearchType": NotRequired[KnowledgeBaseSearchTypeType],
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
        "ingestionFailureReasons": NotRequired[List[str]],
        "ingestionStatus": NotRequired[SyncStatusType],
        "lastContentModificationTime": NotRequired[datetime],
        "renderingConfiguration": NotRequired[RenderingConfigurationTypeDef],
        "serverSideEncryptionConfiguration": NotRequired[ServerSideEncryptionConfigurationTypeDef],
        "sourceConfiguration": NotRequired[SourceConfigurationOutputTypeDef],
        "tags": NotRequired[Dict[str, str]],
        "vectorIngestionConfiguration": NotRequired[VectorIngestionConfigurationOutputTypeDef],
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
        "vectorIngestionConfiguration": NotRequired[VectorIngestionConfigurationOutputTypeDef],
    },
)
ManagedSourceConfigurationTypeDef = TypedDict(
    "ManagedSourceConfigurationTypeDef",
    {
        "webCrawlerConfiguration": NotRequired[WebCrawlerConfigurationUnionTypeDef],
    },
)
ResultDataPaginatorTypeDef = TypedDict(
    "ResultDataPaginatorTypeDef",
    {
        "resultId": str,
        "data": NotRequired[DataSummaryPaginatorTypeDef],
        "document": NotRequired[DocumentTypeDef],
        "relevanceScore": NotRequired[float],
        "type": NotRequired[QueryResultTypeType],
    },
)
RecommendationDataTypeDef = TypedDict(
    "RecommendationDataTypeDef",
    {
        "recommendationId": str,
        "data": NotRequired[DataSummaryTypeDef],
        "document": NotRequired[DocumentTypeDef],
        "relevanceLevel": NotRequired[RelevanceLevelType],
        "relevanceScore": NotRequired[float],
        "type": NotRequired[RecommendationTypeType],
    },
)
ResultDataTypeDef = TypedDict(
    "ResultDataTypeDef",
    {
        "resultId": str,
        "data": NotRequired[DataSummaryTypeDef],
        "document": NotRequired[DocumentTypeDef],
        "relevanceScore": NotRequired[float],
        "type": NotRequired[QueryResultTypeType],
    },
)
AnswerRecommendationAIAgentConfigurationOutputTypeDef = TypedDict(
    "AnswerRecommendationAIAgentConfigurationOutputTypeDef",
    {
        "answerGenerationAIPromptId": NotRequired[str],
        "associationConfigurations": NotRequired[List[AssociationConfigurationOutputTypeDef]],
        "intentLabelingGenerationAIPromptId": NotRequired[str],
        "queryReformulationAIPromptId": NotRequired[str],
    },
)
ManualSearchAIAgentConfigurationOutputTypeDef = TypedDict(
    "ManualSearchAIAgentConfigurationOutputTypeDef",
    {
        "answerGenerationAIPromptId": NotRequired[str],
        "associationConfigurations": NotRequired[List[AssociationConfigurationOutputTypeDef]],
    },
)
KnowledgeBaseAssociationConfigurationDataUnionTypeDef = Union[
    KnowledgeBaseAssociationConfigurationDataTypeDef,
    KnowledgeBaseAssociationConfigurationDataOutputTypeDef,
]
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
ManagedSourceConfigurationUnionTypeDef = Union[
    ManagedSourceConfigurationTypeDef, ManagedSourceConfigurationOutputTypeDef
]
QueryAssistantResponsePaginatorTypeDef = TypedDict(
    "QueryAssistantResponsePaginatorTypeDef",
    {
        "nextToken": str,
        "results": List[ResultDataPaginatorTypeDef],
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
AIAgentConfigurationOutputTypeDef = TypedDict(
    "AIAgentConfigurationOutputTypeDef",
    {
        "answerRecommendationAIAgentConfiguration": NotRequired[
            AnswerRecommendationAIAgentConfigurationOutputTypeDef
        ],
        "manualSearchAIAgentConfiguration": NotRequired[
            ManualSearchAIAgentConfigurationOutputTypeDef
        ],
    },
)
AssociationConfigurationDataTypeDef = TypedDict(
    "AssociationConfigurationDataTypeDef",
    {
        "knowledgeBaseAssociationConfigurationData": NotRequired[
            KnowledgeBaseAssociationConfigurationDataUnionTypeDef
        ],
    },
)
SourceConfigurationTypeDef = TypedDict(
    "SourceConfigurationTypeDef",
    {
        "appIntegrations": NotRequired[AppIntegrationsConfigurationUnionTypeDef],
        "managedSourceConfiguration": NotRequired[ManagedSourceConfigurationUnionTypeDef],
    },
)
AIAgentDataTypeDef = TypedDict(
    "AIAgentDataTypeDef",
    {
        "aiAgentArn": str,
        "aiAgentId": str,
        "assistantArn": str,
        "assistantId": str,
        "configuration": AIAgentConfigurationOutputTypeDef,
        "name": str,
        "type": AIAgentTypeType,
        "visibilityStatus": VisibilityStatusType,
        "description": NotRequired[str],
        "modifiedTime": NotRequired[datetime],
        "origin": NotRequired[OriginType],
        "status": NotRequired[StatusType],
        "tags": NotRequired[Dict[str, str]],
    },
)
AIAgentSummaryTypeDef = TypedDict(
    "AIAgentSummaryTypeDef",
    {
        "aiAgentArn": str,
        "aiAgentId": str,
        "assistantArn": str,
        "assistantId": str,
        "name": str,
        "type": AIAgentTypeType,
        "visibilityStatus": VisibilityStatusType,
        "configuration": NotRequired[AIAgentConfigurationOutputTypeDef],
        "description": NotRequired[str],
        "modifiedTime": NotRequired[datetime],
        "origin": NotRequired[OriginType],
        "status": NotRequired[StatusType],
        "tags": NotRequired[Dict[str, str]],
    },
)
AssociationConfigurationDataUnionTypeDef = Union[
    AssociationConfigurationDataTypeDef, AssociationConfigurationDataOutputTypeDef
]
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
        "vectorIngestionConfiguration": NotRequired[VectorIngestionConfigurationTypeDef],
    },
)
CreateAIAgentResponseTypeDef = TypedDict(
    "CreateAIAgentResponseTypeDef",
    {
        "aiAgent": AIAgentDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAIAgentVersionResponseTypeDef = TypedDict(
    "CreateAIAgentVersionResponseTypeDef",
    {
        "aiAgent": AIAgentDataTypeDef,
        "versionNumber": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAIAgentResponseTypeDef = TypedDict(
    "GetAIAgentResponseTypeDef",
    {
        "aiAgent": AIAgentDataTypeDef,
        "versionNumber": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAIAgentResponseTypeDef = TypedDict(
    "UpdateAIAgentResponseTypeDef",
    {
        "aiAgent": AIAgentDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AIAgentVersionSummaryTypeDef = TypedDict(
    "AIAgentVersionSummaryTypeDef",
    {
        "aiAgentSummary": NotRequired[AIAgentSummaryTypeDef],
        "versionNumber": NotRequired[int],
    },
)
ListAIAgentsResponseTypeDef = TypedDict(
    "ListAIAgentsResponseTypeDef",
    {
        "aiAgentSummaries": List[AIAgentSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociationConfigurationTypeDef = TypedDict(
    "AssociationConfigurationTypeDef",
    {
        "associationConfigurationData": NotRequired[AssociationConfigurationDataUnionTypeDef],
        "associationId": NotRequired[str],
        "associationType": NotRequired[Literal["KNOWLEDGE_BASE"]],
    },
)
ListAIAgentVersionsResponseTypeDef = TypedDict(
    "ListAIAgentVersionsResponseTypeDef",
    {
        "aiAgentVersionSummaries": List[AIAgentVersionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociationConfigurationUnionTypeDef = Union[
    AssociationConfigurationTypeDef, AssociationConfigurationOutputTypeDef
]
ManualSearchAIAgentConfigurationTypeDef = TypedDict(
    "ManualSearchAIAgentConfigurationTypeDef",
    {
        "answerGenerationAIPromptId": NotRequired[str],
        "associationConfigurations": NotRequired[Sequence[AssociationConfigurationTypeDef]],
    },
)
AnswerRecommendationAIAgentConfigurationTypeDef = TypedDict(
    "AnswerRecommendationAIAgentConfigurationTypeDef",
    {
        "answerGenerationAIPromptId": NotRequired[str],
        "associationConfigurations": NotRequired[Sequence[AssociationConfigurationUnionTypeDef]],
        "intentLabelingGenerationAIPromptId": NotRequired[str],
        "queryReformulationAIPromptId": NotRequired[str],
    },
)
ManualSearchAIAgentConfigurationUnionTypeDef = Union[
    ManualSearchAIAgentConfigurationTypeDef, ManualSearchAIAgentConfigurationOutputTypeDef
]
AnswerRecommendationAIAgentConfigurationUnionTypeDef = Union[
    AnswerRecommendationAIAgentConfigurationTypeDef,
    AnswerRecommendationAIAgentConfigurationOutputTypeDef,
]
AIAgentConfigurationTypeDef = TypedDict(
    "AIAgentConfigurationTypeDef",
    {
        "answerRecommendationAIAgentConfiguration": NotRequired[
            AnswerRecommendationAIAgentConfigurationUnionTypeDef
        ],
        "manualSearchAIAgentConfiguration": NotRequired[
            ManualSearchAIAgentConfigurationUnionTypeDef
        ],
    },
)
CreateAIAgentRequestRequestTypeDef = TypedDict(
    "CreateAIAgentRequestRequestTypeDef",
    {
        "assistantId": str,
        "configuration": AIAgentConfigurationTypeDef,
        "name": str,
        "type": AIAgentTypeType,
        "visibilityStatus": VisibilityStatusType,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
UpdateAIAgentRequestRequestTypeDef = TypedDict(
    "UpdateAIAgentRequestRequestTypeDef",
    {
        "aiAgentId": str,
        "assistantId": str,
        "visibilityStatus": VisibilityStatusType,
        "clientToken": NotRequired[str],
        "configuration": NotRequired[AIAgentConfigurationTypeDef],
        "description": NotRequired[str],
    },
)
