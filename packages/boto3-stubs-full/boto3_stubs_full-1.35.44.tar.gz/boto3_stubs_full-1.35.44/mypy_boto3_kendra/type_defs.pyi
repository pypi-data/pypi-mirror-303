"""
Type annotations for kendra service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/type_defs/)

Usage::

    ```python
    from mypy_boto3_kendra.type_defs import AccessControlConfigurationSummaryTypeDef

    data: AccessControlConfigurationSummaryTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    AlfrescoEntityType,
    AttributeSuggestionsModeType,
    ConditionOperatorType,
    ConfluenceAttachmentFieldNameType,
    ConfluenceAuthenticationTypeType,
    ConfluenceBlogFieldNameType,
    ConfluencePageFieldNameType,
    ConfluenceSpaceFieldNameType,
    ConfluenceVersionType,
    ContentTypeType,
    DatabaseEngineTypeType,
    DataSourceStatusType,
    DataSourceSyncJobStatusType,
    DataSourceTypeType,
    DocumentAttributeValueTypeType,
    DocumentStatusType,
    EntityTypeType,
    ErrorCodeType,
    ExperienceStatusType,
    FaqFileFormatType,
    FaqStatusType,
    FeaturedResultsSetStatusType,
    HighlightTypeType,
    IndexEditionType,
    IndexStatusType,
    IntervalType,
    IssueSubEntityType,
    KeyLocationType,
    MetricTypeType,
    MissingAttributeKeyStrategyType,
    ModeType,
    OrderType,
    PersonaType,
    PrincipalMappingStatusType,
    PrincipalTypeType,
    QueryIdentifiersEnclosingOptionType,
    QueryResultFormatType,
    QueryResultTypeType,
    QuerySuggestionsBlockListStatusType,
    QuerySuggestionsStatusType,
    ReadAccessTypeType,
    RelevanceTypeType,
    SalesforceChatterFeedIncludeFilterTypeType,
    SalesforceKnowledgeArticleStateType,
    SalesforceStandardObjectNameType,
    ScoreConfidenceType,
    ServiceNowAuthenticationTypeType,
    ServiceNowBuildVersionTypeType,
    SharePointOnlineAuthenticationTypeType,
    SharePointVersionType,
    SlackEntityType,
    SortOrderType,
    SuggestionTypeType,
    ThesaurusStatusType,
    TypeType,
    UserContextPolicyType,
    UserGroupResolutionModeType,
    WebCrawlerModeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AccessControlConfigurationSummaryTypeDef",
    "AccessControlListConfigurationTypeDef",
    "AclConfigurationTypeDef",
    "DataSourceToIndexFieldMappingTypeDef",
    "DataSourceVpcConfigurationOutputTypeDef",
    "S3PathTypeDef",
    "EntityConfigurationTypeDef",
    "FailedEntityTypeDef",
    "ResponseMetadataTypeDef",
    "EntityPersonaConfigurationTypeDef",
    "SuggestableConfigTypeDef",
    "BasicAuthenticationConfigurationTypeDef",
    "DataSourceSyncJobMetricTargetTypeDef",
    "BatchDeleteDocumentResponseFailedDocumentTypeDef",
    "BatchDeleteFeaturedResultsSetErrorTypeDef",
    "BatchDeleteFeaturedResultsSetRequestRequestTypeDef",
    "BatchGetDocumentStatusResponseErrorTypeDef",
    "StatusTypeDef",
    "BatchPutDocumentResponseFailedDocumentTypeDef",
    "BlobTypeDef",
    "CapacityUnitsConfigurationTypeDef",
    "ClearQuerySuggestionsRequestRequestTypeDef",
    "TimestampTypeDef",
    "ExpandConfigurationTypeDef",
    "SortingConfigurationTypeDef",
    "ConfluenceAttachmentToIndexFieldMappingTypeDef",
    "ConfluenceBlogToIndexFieldMappingTypeDef",
    "ProxyConfigurationTypeDef",
    "ConfluencePageToIndexFieldMappingTypeDef",
    "ConfluenceSpaceToIndexFieldMappingTypeDef",
    "ConnectionConfigurationTypeDef",
    "ContentSourceConfigurationOutputTypeDef",
    "ContentSourceConfigurationTypeDef",
    "CorrectionTypeDef",
    "PrincipalTypeDef",
    "DataSourceVpcConfigurationTypeDef",
    "TagTypeDef",
    "FeaturedDocumentTypeDef",
    "ServerSideEncryptionConfigurationTypeDef",
    "UserGroupResolutionConfigurationTypeDef",
    "TemplateConfigurationOutputTypeDef",
    "DataSourceGroupTypeDef",
    "DataSourceSummaryTypeDef",
    "DataSourceSyncJobMetricsTypeDef",
    "SqlConfigurationTypeDef",
    "DeleteAccessControlConfigurationRequestRequestTypeDef",
    "DeleteDataSourceRequestRequestTypeDef",
    "DeleteExperienceRequestRequestTypeDef",
    "DeleteFaqRequestRequestTypeDef",
    "DeleteIndexRequestRequestTypeDef",
    "DeletePrincipalMappingRequestRequestTypeDef",
    "DeleteQuerySuggestionsBlockListRequestRequestTypeDef",
    "DeleteThesaurusRequestRequestTypeDef",
    "DescribeAccessControlConfigurationRequestRequestTypeDef",
    "DescribeDataSourceRequestRequestTypeDef",
    "DescribeExperienceRequestRequestTypeDef",
    "ExperienceEndpointTypeDef",
    "DescribeFaqRequestRequestTypeDef",
    "DescribeFeaturedResultsSetRequestRequestTypeDef",
    "FeaturedDocumentMissingTypeDef",
    "FeaturedDocumentWithMetadataTypeDef",
    "DescribeIndexRequestRequestTypeDef",
    "DescribePrincipalMappingRequestRequestTypeDef",
    "GroupOrderingIdSummaryTypeDef",
    "DescribeQuerySuggestionsBlockListRequestRequestTypeDef",
    "DescribeQuerySuggestionsConfigRequestRequestTypeDef",
    "DescribeThesaurusRequestRequestTypeDef",
    "DisassociatePersonasFromEntitiesRequestRequestTypeDef",
    "DocumentAttributeValueOutputTypeDef",
    "RelevanceOutputTypeDef",
    "SearchTypeDef",
    "DocumentsMetadataConfigurationTypeDef",
    "EntityDisplayDataTypeDef",
    "UserIdentityConfigurationTypeDef",
    "FacetTypeDef",
    "FaqStatisticsTypeDef",
    "FaqSummaryTypeDef",
    "FeaturedResultsSetSummaryTypeDef",
    "GetSnapshotsRequestRequestTypeDef",
    "TimeRangeOutputTypeDef",
    "GitHubDocumentCrawlPropertiesTypeDef",
    "SaaSConfigurationTypeDef",
    "MemberGroupTypeDef",
    "MemberUserTypeDef",
    "GroupSummaryTypeDef",
    "HighlightTypeDef",
    "IndexConfigurationSummaryTypeDef",
    "TextDocumentStatisticsTypeDef",
    "JsonTokenTypeConfigurationTypeDef",
    "JwtTokenTypeConfigurationTypeDef",
    "ListAccessControlConfigurationsRequestRequestTypeDef",
    "ListDataSourcesRequestRequestTypeDef",
    "ListEntityPersonasRequestRequestTypeDef",
    "PersonasSummaryTypeDef",
    "ListExperienceEntitiesRequestRequestTypeDef",
    "ListExperiencesRequestRequestTypeDef",
    "ListFaqsRequestRequestTypeDef",
    "ListFeaturedResultsSetsRequestRequestTypeDef",
    "ListGroupsOlderThanOrderingIdRequestRequestTypeDef",
    "ListIndicesRequestRequestTypeDef",
    "ListQuerySuggestionsBlockListsRequestRequestTypeDef",
    "QuerySuggestionsBlockListSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListThesauriRequestRequestTypeDef",
    "ThesaurusSummaryTypeDef",
    "SpellCorrectionConfigurationTypeDef",
    "ScoreAttributesTypeDef",
    "WarningTypeDef",
    "RelevanceFeedbackTypeDef",
    "RelevanceTypeDef",
    "SeedUrlConfigurationOutputTypeDef",
    "SeedUrlConfigurationTypeDef",
    "SiteMapsConfigurationOutputTypeDef",
    "SiteMapsConfigurationTypeDef",
    "StartDataSourceSyncJobRequestRequestTypeDef",
    "StopDataSourceSyncJobRequestRequestTypeDef",
    "SuggestionHighlightTypeDef",
    "TableCellTypeDef",
    "TemplateConfigurationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "ColumnConfigurationOutputTypeDef",
    "ColumnConfigurationTypeDef",
    "GoogleDriveConfigurationOutputTypeDef",
    "GoogleDriveConfigurationTypeDef",
    "SalesforceChatterFeedConfigurationOutputTypeDef",
    "SalesforceChatterFeedConfigurationTypeDef",
    "SalesforceCustomKnowledgeArticleTypeConfigurationOutputTypeDef",
    "SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef",
    "SalesforceStandardKnowledgeArticleTypeConfigurationOutputTypeDef",
    "SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef",
    "SalesforceStandardObjectAttachmentConfigurationOutputTypeDef",
    "SalesforceStandardObjectAttachmentConfigurationTypeDef",
    "SalesforceStandardObjectConfigurationOutputTypeDef",
    "SalesforceStandardObjectConfigurationTypeDef",
    "ServiceNowKnowledgeArticleConfigurationOutputTypeDef",
    "ServiceNowKnowledgeArticleConfigurationTypeDef",
    "ServiceNowServiceCatalogConfigurationOutputTypeDef",
    "ServiceNowServiceCatalogConfigurationTypeDef",
    "WorkDocsConfigurationOutputTypeDef",
    "WorkDocsConfigurationTypeDef",
    "BoxConfigurationOutputTypeDef",
    "FsxConfigurationOutputTypeDef",
    "JiraConfigurationOutputTypeDef",
    "QuipConfigurationOutputTypeDef",
    "SlackConfigurationOutputTypeDef",
    "AlfrescoConfigurationOutputTypeDef",
    "OnPremiseConfigurationTypeDef",
    "OneDriveUsersOutputTypeDef",
    "OneDriveUsersTypeDef",
    "UpdateQuerySuggestionsBlockListRequestRequestTypeDef",
    "UpdateThesaurusRequestRequestTypeDef",
    "AssociateEntitiesToExperienceRequestRequestTypeDef",
    "DisassociateEntitiesFromExperienceRequestRequestTypeDef",
    "AssociateEntitiesToExperienceResponseTypeDef",
    "AssociatePersonasToEntitiesResponseTypeDef",
    "CreateAccessControlConfigurationResponseTypeDef",
    "CreateDataSourceResponseTypeDef",
    "CreateExperienceResponseTypeDef",
    "CreateFaqResponseTypeDef",
    "CreateIndexResponseTypeDef",
    "CreateQuerySuggestionsBlockListResponseTypeDef",
    "CreateThesaurusResponseTypeDef",
    "DescribeFaqResponseTypeDef",
    "DescribeQuerySuggestionsBlockListResponseTypeDef",
    "DescribeThesaurusResponseTypeDef",
    "DisassociateEntitiesFromExperienceResponseTypeDef",
    "DisassociatePersonasFromEntitiesResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ListAccessControlConfigurationsResponseTypeDef",
    "StartDataSourceSyncJobResponseTypeDef",
    "AssociatePersonasToEntitiesRequestRequestTypeDef",
    "AttributeSuggestionsDescribeConfigTypeDef",
    "AttributeSuggestionsUpdateConfigTypeDef",
    "AuthenticationConfigurationOutputTypeDef",
    "AuthenticationConfigurationTypeDef",
    "BatchDeleteDocumentRequestRequestTypeDef",
    "BatchDeleteDocumentResponseTypeDef",
    "BatchDeleteFeaturedResultsSetResponseTypeDef",
    "BatchGetDocumentStatusResponseTypeDef",
    "BatchPutDocumentResponseTypeDef",
    "ClickFeedbackTypeDef",
    "DocumentAttributeValueTypeDef",
    "TimeRangeTypeDef",
    "CollapseConfigurationTypeDef",
    "ConfluenceAttachmentConfigurationOutputTypeDef",
    "ConfluenceAttachmentConfigurationTypeDef",
    "ConfluenceBlogConfigurationOutputTypeDef",
    "ConfluenceBlogConfigurationTypeDef",
    "SharePointConfigurationOutputTypeDef",
    "ConfluencePageConfigurationOutputTypeDef",
    "ConfluencePageConfigurationTypeDef",
    "ConfluenceSpaceConfigurationOutputTypeDef",
    "ConfluenceSpaceConfigurationTypeDef",
    "ContentSourceConfigurationUnionTypeDef",
    "SpellCorrectedQueryTypeDef",
    "HierarchicalPrincipalOutputTypeDef",
    "HierarchicalPrincipalTypeDef",
    "DataSourceVpcConfigurationUnionTypeDef",
    "CreateFaqRequestRequestTypeDef",
    "CreateQuerySuggestionsBlockListRequestRequestTypeDef",
    "CreateThesaurusRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateFeaturedResultsSetRequestRequestTypeDef",
    "FeaturedResultsSetTypeDef",
    "UpdateFeaturedResultsSetRequestRequestTypeDef",
    "UserContextTypeDef",
    "ListDataSourcesResponseTypeDef",
    "DataSourceSyncJobTypeDef",
    "ExperiencesSummaryTypeDef",
    "DescribeFeaturedResultsSetResponseTypeDef",
    "DescribePrincipalMappingResponseTypeDef",
    "DocumentAttributeConditionOutputTypeDef",
    "DocumentAttributeOutputTypeDef",
    "DocumentAttributeTargetOutputTypeDef",
    "DocumentAttributeValueCountPairTypeDef",
    "DocumentMetadataConfigurationOutputTypeDef",
    "S3DataSourceConfigurationOutputTypeDef",
    "S3DataSourceConfigurationTypeDef",
    "ExperienceEntitiesSummaryTypeDef",
    "ExperienceConfigurationOutputTypeDef",
    "ListFaqsResponseTypeDef",
    "ListFeaturedResultsSetsResponseTypeDef",
    "GetSnapshotsResponseTypeDef",
    "GroupMembersTypeDef",
    "ListGroupsOlderThanOrderingIdResponseTypeDef",
    "TextWithHighlightsTypeDef",
    "ListIndicesResponseTypeDef",
    "IndexStatisticsTypeDef",
    "UserTokenConfigurationTypeDef",
    "ListEntityPersonasResponseTypeDef",
    "ListQuerySuggestionsBlockListsResponseTypeDef",
    "ListThesauriResponseTypeDef",
    "RelevanceUnionTypeDef",
    "SeedUrlConfigurationUnionTypeDef",
    "UrlsOutputTypeDef",
    "SiteMapsConfigurationUnionTypeDef",
    "SuggestionTextWithHighlightsTypeDef",
    "TableRowTypeDef",
    "TemplateConfigurationUnionTypeDef",
    "DatabaseConfigurationOutputTypeDef",
    "ColumnConfigurationUnionTypeDef",
    "GoogleDriveConfigurationUnionTypeDef",
    "SalesforceChatterFeedConfigurationUnionTypeDef",
    "SalesforceCustomKnowledgeArticleTypeConfigurationUnionTypeDef",
    "SalesforceKnowledgeArticleConfigurationOutputTypeDef",
    "SalesforceStandardKnowledgeArticleTypeConfigurationUnionTypeDef",
    "SalesforceStandardObjectAttachmentConfigurationUnionTypeDef",
    "SalesforceStandardObjectConfigurationUnionTypeDef",
    "ServiceNowKnowledgeArticleConfigurationUnionTypeDef",
    "ServiceNowConfigurationOutputTypeDef",
    "ServiceNowServiceCatalogConfigurationUnionTypeDef",
    "WorkDocsConfigurationUnionTypeDef",
    "GitHubConfigurationOutputTypeDef",
    "OneDriveConfigurationOutputTypeDef",
    "OneDriveUsersUnionTypeDef",
    "DescribeQuerySuggestionsConfigResponseTypeDef",
    "UpdateQuerySuggestionsConfigRequestRequestTypeDef",
    "AuthenticationConfigurationUnionTypeDef",
    "SubmitFeedbackRequestRequestTypeDef",
    "DocumentAttributeValueUnionTypeDef",
    "ListDataSourceSyncJobsRequestRequestTypeDef",
    "ConfluenceAttachmentConfigurationUnionTypeDef",
    "ConfluenceBlogConfigurationUnionTypeDef",
    "ConfluencePageConfigurationUnionTypeDef",
    "ConfluenceConfigurationOutputTypeDef",
    "ConfluenceSpaceConfigurationUnionTypeDef",
    "ExperienceConfigurationTypeDef",
    "DescribeAccessControlConfigurationResponseTypeDef",
    "HierarchicalPrincipalUnionTypeDef",
    "UpdateAccessControlConfigurationRequestRequestTypeDef",
    "AlfrescoConfigurationTypeDef",
    "BoxConfigurationTypeDef",
    "FsxConfigurationTypeDef",
    "GitHubConfigurationTypeDef",
    "JiraConfigurationTypeDef",
    "QuipConfigurationTypeDef",
    "SharePointConfigurationTypeDef",
    "SlackConfigurationTypeDef",
    "CreateFeaturedResultsSetResponseTypeDef",
    "UpdateFeaturedResultsSetResponseTypeDef",
    "ListDataSourceSyncJobsResponseTypeDef",
    "ListExperiencesResponseTypeDef",
    "HookConfigurationOutputTypeDef",
    "RetrieveResultItemTypeDef",
    "SourceDocumentTypeDef",
    "InlineCustomDocumentEnrichmentConfigurationOutputTypeDef",
    "FacetResultTypeDef",
    "S3DataSourceConfigurationUnionTypeDef",
    "ListExperienceEntitiesResponseTypeDef",
    "DescribeExperienceResponseTypeDef",
    "PutPrincipalMappingRequestRequestTypeDef",
    "AdditionalResultAttributeValueTypeDef",
    "ExpandedResultItemTypeDef",
    "CreateIndexRequestRequestTypeDef",
    "DescribeIndexResponseTypeDef",
    "DocumentMetadataConfigurationTypeDef",
    "DocumentRelevanceConfigurationTypeDef",
    "WebCrawlerConfigurationOutputTypeDef",
    "UrlsTypeDef",
    "SuggestionValueTypeDef",
    "TableExcerptTypeDef",
    "DatabaseConfigurationTypeDef",
    "SalesforceConfigurationOutputTypeDef",
    "SalesforceKnowledgeArticleConfigurationTypeDef",
    "ServiceNowConfigurationTypeDef",
    "OneDriveConfigurationTypeDef",
    "DocumentAttributeConditionTypeDef",
    "DocumentAttributeTargetTypeDef",
    "DocumentAttributeTypeDef",
    "ConfluenceConfigurationTypeDef",
    "CreateExperienceRequestRequestTypeDef",
    "UpdateExperienceRequestRequestTypeDef",
    "CreateAccessControlConfigurationRequestRequestTypeDef",
    "AlfrescoConfigurationUnionTypeDef",
    "BoxConfigurationUnionTypeDef",
    "FsxConfigurationUnionTypeDef",
    "GitHubConfigurationUnionTypeDef",
    "JiraConfigurationUnionTypeDef",
    "QuipConfigurationUnionTypeDef",
    "SharePointConfigurationUnionTypeDef",
    "SlackConfigurationUnionTypeDef",
    "RetrieveResultTypeDef",
    "CustomDocumentEnrichmentConfigurationOutputTypeDef",
    "AdditionalResultAttributeTypeDef",
    "CollapsedResultDetailTypeDef",
    "DocumentMetadataConfigurationUnionTypeDef",
    "UrlsUnionTypeDef",
    "SuggestionTypeDef",
    "DatabaseConfigurationUnionTypeDef",
    "DataSourceConfigurationOutputTypeDef",
    "SalesforceKnowledgeArticleConfigurationUnionTypeDef",
    "ServiceNowConfigurationUnionTypeDef",
    "OneDriveConfigurationUnionTypeDef",
    "DocumentAttributeConditionUnionTypeDef",
    "DocumentAttributeTargetUnionTypeDef",
    "DocumentAttributeUnionTypeDef",
    "ConfluenceConfigurationUnionTypeDef",
    "FeaturedResultsItemTypeDef",
    "QueryResultItemTypeDef",
    "UpdateIndexRequestRequestTypeDef",
    "WebCrawlerConfigurationTypeDef",
    "GetQuerySuggestionsResponseTypeDef",
    "DescribeDataSourceResponseTypeDef",
    "SalesforceConfigurationTypeDef",
    "HookConfigurationTypeDef",
    "InlineCustomDocumentEnrichmentConfigurationTypeDef",
    "AttributeFilterTypeDef",
    "DocumentInfoTypeDef",
    "DocumentTypeDef",
    "QueryResultTypeDef",
    "WebCrawlerConfigurationUnionTypeDef",
    "SalesforceConfigurationUnionTypeDef",
    "HookConfigurationUnionTypeDef",
    "InlineCustomDocumentEnrichmentConfigurationUnionTypeDef",
    "AttributeSuggestionsGetConfigTypeDef",
    "QueryRequestRequestTypeDef",
    "RetrieveRequestRequestTypeDef",
    "BatchGetDocumentStatusRequestRequestTypeDef",
    "DataSourceConfigurationTypeDef",
    "CustomDocumentEnrichmentConfigurationTypeDef",
    "GetQuerySuggestionsRequestRequestTypeDef",
    "BatchPutDocumentRequestRequestTypeDef",
    "CreateDataSourceRequestRequestTypeDef",
    "UpdateDataSourceRequestRequestTypeDef",
)

AccessControlConfigurationSummaryTypeDef = TypedDict(
    "AccessControlConfigurationSummaryTypeDef",
    {
        "Id": str,
    },
)
AccessControlListConfigurationTypeDef = TypedDict(
    "AccessControlListConfigurationTypeDef",
    {
        "KeyPath": NotRequired[str],
    },
)
AclConfigurationTypeDef = TypedDict(
    "AclConfigurationTypeDef",
    {
        "AllowedGroupsColumnName": str,
    },
)
DataSourceToIndexFieldMappingTypeDef = TypedDict(
    "DataSourceToIndexFieldMappingTypeDef",
    {
        "DataSourceFieldName": str,
        "IndexFieldName": str,
        "DateFieldFormat": NotRequired[str],
    },
)
DataSourceVpcConfigurationOutputTypeDef = TypedDict(
    "DataSourceVpcConfigurationOutputTypeDef",
    {
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
    },
)
S3PathTypeDef = TypedDict(
    "S3PathTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
EntityConfigurationTypeDef = TypedDict(
    "EntityConfigurationTypeDef",
    {
        "EntityId": str,
        "EntityType": EntityTypeType,
    },
)
FailedEntityTypeDef = TypedDict(
    "FailedEntityTypeDef",
    {
        "EntityId": NotRequired[str],
        "ErrorMessage": NotRequired[str],
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
EntityPersonaConfigurationTypeDef = TypedDict(
    "EntityPersonaConfigurationTypeDef",
    {
        "EntityId": str,
        "Persona": PersonaType,
    },
)
SuggestableConfigTypeDef = TypedDict(
    "SuggestableConfigTypeDef",
    {
        "AttributeName": NotRequired[str],
        "Suggestable": NotRequired[bool],
    },
)
BasicAuthenticationConfigurationTypeDef = TypedDict(
    "BasicAuthenticationConfigurationTypeDef",
    {
        "Host": str,
        "Port": int,
        "Credentials": str,
    },
)
DataSourceSyncJobMetricTargetTypeDef = TypedDict(
    "DataSourceSyncJobMetricTargetTypeDef",
    {
        "DataSourceId": str,
        "DataSourceSyncJobId": NotRequired[str],
    },
)
BatchDeleteDocumentResponseFailedDocumentTypeDef = TypedDict(
    "BatchDeleteDocumentResponseFailedDocumentTypeDef",
    {
        "Id": NotRequired[str],
        "ErrorCode": NotRequired[ErrorCodeType],
        "ErrorMessage": NotRequired[str],
    },
)
BatchDeleteFeaturedResultsSetErrorTypeDef = TypedDict(
    "BatchDeleteFeaturedResultsSetErrorTypeDef",
    {
        "Id": str,
        "ErrorCode": ErrorCodeType,
        "ErrorMessage": str,
    },
)
BatchDeleteFeaturedResultsSetRequestRequestTypeDef = TypedDict(
    "BatchDeleteFeaturedResultsSetRequestRequestTypeDef",
    {
        "IndexId": str,
        "FeaturedResultsSetIds": Sequence[str],
    },
)
BatchGetDocumentStatusResponseErrorTypeDef = TypedDict(
    "BatchGetDocumentStatusResponseErrorTypeDef",
    {
        "DocumentId": NotRequired[str],
        "ErrorCode": NotRequired[ErrorCodeType],
        "ErrorMessage": NotRequired[str],
    },
)
StatusTypeDef = TypedDict(
    "StatusTypeDef",
    {
        "DocumentId": NotRequired[str],
        "DocumentStatus": NotRequired[DocumentStatusType],
        "FailureCode": NotRequired[str],
        "FailureReason": NotRequired[str],
    },
)
BatchPutDocumentResponseFailedDocumentTypeDef = TypedDict(
    "BatchPutDocumentResponseFailedDocumentTypeDef",
    {
        "Id": NotRequired[str],
        "ErrorCode": NotRequired[ErrorCodeType],
        "ErrorMessage": NotRequired[str],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
CapacityUnitsConfigurationTypeDef = TypedDict(
    "CapacityUnitsConfigurationTypeDef",
    {
        "StorageCapacityUnits": int,
        "QueryCapacityUnits": int,
    },
)
ClearQuerySuggestionsRequestRequestTypeDef = TypedDict(
    "ClearQuerySuggestionsRequestRequestTypeDef",
    {
        "IndexId": str,
    },
)
TimestampTypeDef = Union[datetime, str]
ExpandConfigurationTypeDef = TypedDict(
    "ExpandConfigurationTypeDef",
    {
        "MaxResultItemsToExpand": NotRequired[int],
        "MaxExpandedResultsPerItem": NotRequired[int],
    },
)
SortingConfigurationTypeDef = TypedDict(
    "SortingConfigurationTypeDef",
    {
        "DocumentAttributeKey": str,
        "SortOrder": SortOrderType,
    },
)
ConfluenceAttachmentToIndexFieldMappingTypeDef = TypedDict(
    "ConfluenceAttachmentToIndexFieldMappingTypeDef",
    {
        "DataSourceFieldName": NotRequired[ConfluenceAttachmentFieldNameType],
        "DateFieldFormat": NotRequired[str],
        "IndexFieldName": NotRequired[str],
    },
)
ConfluenceBlogToIndexFieldMappingTypeDef = TypedDict(
    "ConfluenceBlogToIndexFieldMappingTypeDef",
    {
        "DataSourceFieldName": NotRequired[ConfluenceBlogFieldNameType],
        "DateFieldFormat": NotRequired[str],
        "IndexFieldName": NotRequired[str],
    },
)
ProxyConfigurationTypeDef = TypedDict(
    "ProxyConfigurationTypeDef",
    {
        "Host": str,
        "Port": int,
        "Credentials": NotRequired[str],
    },
)
ConfluencePageToIndexFieldMappingTypeDef = TypedDict(
    "ConfluencePageToIndexFieldMappingTypeDef",
    {
        "DataSourceFieldName": NotRequired[ConfluencePageFieldNameType],
        "DateFieldFormat": NotRequired[str],
        "IndexFieldName": NotRequired[str],
    },
)
ConfluenceSpaceToIndexFieldMappingTypeDef = TypedDict(
    "ConfluenceSpaceToIndexFieldMappingTypeDef",
    {
        "DataSourceFieldName": NotRequired[ConfluenceSpaceFieldNameType],
        "DateFieldFormat": NotRequired[str],
        "IndexFieldName": NotRequired[str],
    },
)
ConnectionConfigurationTypeDef = TypedDict(
    "ConnectionConfigurationTypeDef",
    {
        "DatabaseHost": str,
        "DatabasePort": int,
        "DatabaseName": str,
        "TableName": str,
        "SecretArn": str,
    },
)
ContentSourceConfigurationOutputTypeDef = TypedDict(
    "ContentSourceConfigurationOutputTypeDef",
    {
        "DataSourceIds": NotRequired[List[str]],
        "FaqIds": NotRequired[List[str]],
        "DirectPutContent": NotRequired[bool],
    },
)
ContentSourceConfigurationTypeDef = TypedDict(
    "ContentSourceConfigurationTypeDef",
    {
        "DataSourceIds": NotRequired[Sequence[str]],
        "FaqIds": NotRequired[Sequence[str]],
        "DirectPutContent": NotRequired[bool],
    },
)
CorrectionTypeDef = TypedDict(
    "CorrectionTypeDef",
    {
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
        "Term": NotRequired[str],
        "CorrectedTerm": NotRequired[str],
    },
)
PrincipalTypeDef = TypedDict(
    "PrincipalTypeDef",
    {
        "Name": str,
        "Type": PrincipalTypeType,
        "Access": ReadAccessTypeType,
        "DataSourceId": NotRequired[str],
    },
)
DataSourceVpcConfigurationTypeDef = TypedDict(
    "DataSourceVpcConfigurationTypeDef",
    {
        "SubnetIds": Sequence[str],
        "SecurityGroupIds": Sequence[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
FeaturedDocumentTypeDef = TypedDict(
    "FeaturedDocumentTypeDef",
    {
        "Id": NotRequired[str],
    },
)
ServerSideEncryptionConfigurationTypeDef = TypedDict(
    "ServerSideEncryptionConfigurationTypeDef",
    {
        "KmsKeyId": NotRequired[str],
    },
)
UserGroupResolutionConfigurationTypeDef = TypedDict(
    "UserGroupResolutionConfigurationTypeDef",
    {
        "UserGroupResolutionMode": UserGroupResolutionModeType,
    },
)
TemplateConfigurationOutputTypeDef = TypedDict(
    "TemplateConfigurationOutputTypeDef",
    {
        "Template": NotRequired[Dict[str, Any]],
    },
)
DataSourceGroupTypeDef = TypedDict(
    "DataSourceGroupTypeDef",
    {
        "GroupId": str,
        "DataSourceId": str,
    },
)
DataSourceSummaryTypeDef = TypedDict(
    "DataSourceSummaryTypeDef",
    {
        "Name": NotRequired[str],
        "Id": NotRequired[str],
        "Type": NotRequired[DataSourceTypeType],
        "CreatedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
        "Status": NotRequired[DataSourceStatusType],
        "LanguageCode": NotRequired[str],
    },
)
DataSourceSyncJobMetricsTypeDef = TypedDict(
    "DataSourceSyncJobMetricsTypeDef",
    {
        "DocumentsAdded": NotRequired[str],
        "DocumentsModified": NotRequired[str],
        "DocumentsDeleted": NotRequired[str],
        "DocumentsFailed": NotRequired[str],
        "DocumentsScanned": NotRequired[str],
    },
)
SqlConfigurationTypeDef = TypedDict(
    "SqlConfigurationTypeDef",
    {
        "QueryIdentifiersEnclosingOption": NotRequired[QueryIdentifiersEnclosingOptionType],
    },
)
DeleteAccessControlConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteAccessControlConfigurationRequestRequestTypeDef",
    {
        "IndexId": str,
        "Id": str,
    },
)
DeleteDataSourceRequestRequestTypeDef = TypedDict(
    "DeleteDataSourceRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)
DeleteExperienceRequestRequestTypeDef = TypedDict(
    "DeleteExperienceRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)
DeleteFaqRequestRequestTypeDef = TypedDict(
    "DeleteFaqRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)
DeleteIndexRequestRequestTypeDef = TypedDict(
    "DeleteIndexRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DeletePrincipalMappingRequestRequestTypeDef = TypedDict(
    "DeletePrincipalMappingRequestRequestTypeDef",
    {
        "IndexId": str,
        "GroupId": str,
        "DataSourceId": NotRequired[str],
        "OrderingId": NotRequired[int],
    },
)
DeleteQuerySuggestionsBlockListRequestRequestTypeDef = TypedDict(
    "DeleteQuerySuggestionsBlockListRequestRequestTypeDef",
    {
        "IndexId": str,
        "Id": str,
    },
)
DeleteThesaurusRequestRequestTypeDef = TypedDict(
    "DeleteThesaurusRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)
DescribeAccessControlConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeAccessControlConfigurationRequestRequestTypeDef",
    {
        "IndexId": str,
        "Id": str,
    },
)
DescribeDataSourceRequestRequestTypeDef = TypedDict(
    "DescribeDataSourceRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)
DescribeExperienceRequestRequestTypeDef = TypedDict(
    "DescribeExperienceRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)
ExperienceEndpointTypeDef = TypedDict(
    "ExperienceEndpointTypeDef",
    {
        "EndpointType": NotRequired[Literal["HOME"]],
        "Endpoint": NotRequired[str],
    },
)
DescribeFaqRequestRequestTypeDef = TypedDict(
    "DescribeFaqRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)
DescribeFeaturedResultsSetRequestRequestTypeDef = TypedDict(
    "DescribeFeaturedResultsSetRequestRequestTypeDef",
    {
        "IndexId": str,
        "FeaturedResultsSetId": str,
    },
)
FeaturedDocumentMissingTypeDef = TypedDict(
    "FeaturedDocumentMissingTypeDef",
    {
        "Id": NotRequired[str],
    },
)
FeaturedDocumentWithMetadataTypeDef = TypedDict(
    "FeaturedDocumentWithMetadataTypeDef",
    {
        "Id": NotRequired[str],
        "Title": NotRequired[str],
        "URI": NotRequired[str],
    },
)
DescribeIndexRequestRequestTypeDef = TypedDict(
    "DescribeIndexRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DescribePrincipalMappingRequestRequestTypeDef = TypedDict(
    "DescribePrincipalMappingRequestRequestTypeDef",
    {
        "IndexId": str,
        "GroupId": str,
        "DataSourceId": NotRequired[str],
    },
)
GroupOrderingIdSummaryTypeDef = TypedDict(
    "GroupOrderingIdSummaryTypeDef",
    {
        "Status": NotRequired[PrincipalMappingStatusType],
        "LastUpdatedAt": NotRequired[datetime],
        "ReceivedAt": NotRequired[datetime],
        "OrderingId": NotRequired[int],
        "FailureReason": NotRequired[str],
    },
)
DescribeQuerySuggestionsBlockListRequestRequestTypeDef = TypedDict(
    "DescribeQuerySuggestionsBlockListRequestRequestTypeDef",
    {
        "IndexId": str,
        "Id": str,
    },
)
DescribeQuerySuggestionsConfigRequestRequestTypeDef = TypedDict(
    "DescribeQuerySuggestionsConfigRequestRequestTypeDef",
    {
        "IndexId": str,
    },
)
DescribeThesaurusRequestRequestTypeDef = TypedDict(
    "DescribeThesaurusRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)
DisassociatePersonasFromEntitiesRequestRequestTypeDef = TypedDict(
    "DisassociatePersonasFromEntitiesRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "EntityIds": Sequence[str],
    },
)
DocumentAttributeValueOutputTypeDef = TypedDict(
    "DocumentAttributeValueOutputTypeDef",
    {
        "StringValue": NotRequired[str],
        "StringListValue": NotRequired[List[str]],
        "LongValue": NotRequired[int],
        "DateValue": NotRequired[datetime],
    },
)
RelevanceOutputTypeDef = TypedDict(
    "RelevanceOutputTypeDef",
    {
        "Freshness": NotRequired[bool],
        "Importance": NotRequired[int],
        "Duration": NotRequired[str],
        "RankOrder": NotRequired[OrderType],
        "ValueImportanceMap": NotRequired[Dict[str, int]],
    },
)
SearchTypeDef = TypedDict(
    "SearchTypeDef",
    {
        "Facetable": NotRequired[bool],
        "Searchable": NotRequired[bool],
        "Displayable": NotRequired[bool],
        "Sortable": NotRequired[bool],
    },
)
DocumentsMetadataConfigurationTypeDef = TypedDict(
    "DocumentsMetadataConfigurationTypeDef",
    {
        "S3Prefix": NotRequired[str],
    },
)
EntityDisplayDataTypeDef = TypedDict(
    "EntityDisplayDataTypeDef",
    {
        "UserName": NotRequired[str],
        "GroupName": NotRequired[str],
        "IdentifiedUserName": NotRequired[str],
        "FirstName": NotRequired[str],
        "LastName": NotRequired[str],
    },
)
UserIdentityConfigurationTypeDef = TypedDict(
    "UserIdentityConfigurationTypeDef",
    {
        "IdentityAttributeName": NotRequired[str],
    },
)
FacetTypeDef = TypedDict(
    "FacetTypeDef",
    {
        "DocumentAttributeKey": NotRequired[str],
        "Facets": NotRequired[Sequence[Mapping[str, Any]]],
        "MaxResults": NotRequired[int],
    },
)
FaqStatisticsTypeDef = TypedDict(
    "FaqStatisticsTypeDef",
    {
        "IndexedQuestionAnswersCount": int,
    },
)
FaqSummaryTypeDef = TypedDict(
    "FaqSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired[FaqStatusType],
        "CreatedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
        "FileFormat": NotRequired[FaqFileFormatType],
        "LanguageCode": NotRequired[str],
    },
)
FeaturedResultsSetSummaryTypeDef = TypedDict(
    "FeaturedResultsSetSummaryTypeDef",
    {
        "FeaturedResultsSetId": NotRequired[str],
        "FeaturedResultsSetName": NotRequired[str],
        "Status": NotRequired[FeaturedResultsSetStatusType],
        "LastUpdatedTimestamp": NotRequired[int],
        "CreationTimestamp": NotRequired[int],
    },
)
GetSnapshotsRequestRequestTypeDef = TypedDict(
    "GetSnapshotsRequestRequestTypeDef",
    {
        "IndexId": str,
        "Interval": IntervalType,
        "MetricType": MetricTypeType,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
TimeRangeOutputTypeDef = TypedDict(
    "TimeRangeOutputTypeDef",
    {
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
    },
)
GitHubDocumentCrawlPropertiesTypeDef = TypedDict(
    "GitHubDocumentCrawlPropertiesTypeDef",
    {
        "CrawlRepositoryDocuments": NotRequired[bool],
        "CrawlIssue": NotRequired[bool],
        "CrawlIssueComment": NotRequired[bool],
        "CrawlIssueCommentAttachment": NotRequired[bool],
        "CrawlPullRequest": NotRequired[bool],
        "CrawlPullRequestComment": NotRequired[bool],
        "CrawlPullRequestCommentAttachment": NotRequired[bool],
    },
)
SaaSConfigurationTypeDef = TypedDict(
    "SaaSConfigurationTypeDef",
    {
        "OrganizationName": str,
        "HostUrl": str,
    },
)
MemberGroupTypeDef = TypedDict(
    "MemberGroupTypeDef",
    {
        "GroupId": str,
        "DataSourceId": NotRequired[str],
    },
)
MemberUserTypeDef = TypedDict(
    "MemberUserTypeDef",
    {
        "UserId": str,
    },
)
GroupSummaryTypeDef = TypedDict(
    "GroupSummaryTypeDef",
    {
        "GroupId": NotRequired[str],
        "OrderingId": NotRequired[int],
    },
)
HighlightTypeDef = TypedDict(
    "HighlightTypeDef",
    {
        "BeginOffset": int,
        "EndOffset": int,
        "TopAnswer": NotRequired[bool],
        "Type": NotRequired[HighlightTypeType],
    },
)
IndexConfigurationSummaryTypeDef = TypedDict(
    "IndexConfigurationSummaryTypeDef",
    {
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Status": IndexStatusType,
        "Name": NotRequired[str],
        "Id": NotRequired[str],
        "Edition": NotRequired[IndexEditionType],
    },
)
TextDocumentStatisticsTypeDef = TypedDict(
    "TextDocumentStatisticsTypeDef",
    {
        "IndexedTextDocumentsCount": int,
        "IndexedTextBytes": int,
    },
)
JsonTokenTypeConfigurationTypeDef = TypedDict(
    "JsonTokenTypeConfigurationTypeDef",
    {
        "UserNameAttributeField": str,
        "GroupAttributeField": str,
    },
)
JwtTokenTypeConfigurationTypeDef = TypedDict(
    "JwtTokenTypeConfigurationTypeDef",
    {
        "KeyLocation": KeyLocationType,
        "URL": NotRequired[str],
        "SecretManagerArn": NotRequired[str],
        "UserNameAttributeField": NotRequired[str],
        "GroupAttributeField": NotRequired[str],
        "Issuer": NotRequired[str],
        "ClaimRegex": NotRequired[str],
    },
)
ListAccessControlConfigurationsRequestRequestTypeDef = TypedDict(
    "ListAccessControlConfigurationsRequestRequestTypeDef",
    {
        "IndexId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListDataSourcesRequestRequestTypeDef = TypedDict(
    "ListDataSourcesRequestRequestTypeDef",
    {
        "IndexId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListEntityPersonasRequestRequestTypeDef = TypedDict(
    "ListEntityPersonasRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
PersonasSummaryTypeDef = TypedDict(
    "PersonasSummaryTypeDef",
    {
        "EntityId": NotRequired[str],
        "Persona": NotRequired[PersonaType],
        "CreatedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
    },
)
ListExperienceEntitiesRequestRequestTypeDef = TypedDict(
    "ListExperienceEntitiesRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "NextToken": NotRequired[str],
    },
)
ListExperiencesRequestRequestTypeDef = TypedDict(
    "ListExperiencesRequestRequestTypeDef",
    {
        "IndexId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListFaqsRequestRequestTypeDef = TypedDict(
    "ListFaqsRequestRequestTypeDef",
    {
        "IndexId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListFeaturedResultsSetsRequestRequestTypeDef = TypedDict(
    "ListFeaturedResultsSetsRequestRequestTypeDef",
    {
        "IndexId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListGroupsOlderThanOrderingIdRequestRequestTypeDef = TypedDict(
    "ListGroupsOlderThanOrderingIdRequestRequestTypeDef",
    {
        "IndexId": str,
        "OrderingId": int,
        "DataSourceId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListIndicesRequestRequestTypeDef = TypedDict(
    "ListIndicesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListQuerySuggestionsBlockListsRequestRequestTypeDef = TypedDict(
    "ListQuerySuggestionsBlockListsRequestRequestTypeDef",
    {
        "IndexId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
QuerySuggestionsBlockListSummaryTypeDef = TypedDict(
    "QuerySuggestionsBlockListSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired[QuerySuggestionsBlockListStatusType],
        "CreatedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
        "ItemCount": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
ListThesauriRequestRequestTypeDef = TypedDict(
    "ListThesauriRequestRequestTypeDef",
    {
        "IndexId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ThesaurusSummaryTypeDef = TypedDict(
    "ThesaurusSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired[ThesaurusStatusType],
        "CreatedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
    },
)
SpellCorrectionConfigurationTypeDef = TypedDict(
    "SpellCorrectionConfigurationTypeDef",
    {
        "IncludeQuerySpellCheckSuggestions": bool,
    },
)
ScoreAttributesTypeDef = TypedDict(
    "ScoreAttributesTypeDef",
    {
        "ScoreConfidence": NotRequired[ScoreConfidenceType],
    },
)
WarningTypeDef = TypedDict(
    "WarningTypeDef",
    {
        "Message": NotRequired[str],
        "Code": NotRequired[Literal["QUERY_LANGUAGE_INVALID_SYNTAX"]],
    },
)
RelevanceFeedbackTypeDef = TypedDict(
    "RelevanceFeedbackTypeDef",
    {
        "ResultId": str,
        "RelevanceValue": RelevanceTypeType,
    },
)
RelevanceTypeDef = TypedDict(
    "RelevanceTypeDef",
    {
        "Freshness": NotRequired[bool],
        "Importance": NotRequired[int],
        "Duration": NotRequired[str],
        "RankOrder": NotRequired[OrderType],
        "ValueImportanceMap": NotRequired[Mapping[str, int]],
    },
)
SeedUrlConfigurationOutputTypeDef = TypedDict(
    "SeedUrlConfigurationOutputTypeDef",
    {
        "SeedUrls": List[str],
        "WebCrawlerMode": NotRequired[WebCrawlerModeType],
    },
)
SeedUrlConfigurationTypeDef = TypedDict(
    "SeedUrlConfigurationTypeDef",
    {
        "SeedUrls": Sequence[str],
        "WebCrawlerMode": NotRequired[WebCrawlerModeType],
    },
)
SiteMapsConfigurationOutputTypeDef = TypedDict(
    "SiteMapsConfigurationOutputTypeDef",
    {
        "SiteMaps": List[str],
    },
)
SiteMapsConfigurationTypeDef = TypedDict(
    "SiteMapsConfigurationTypeDef",
    {
        "SiteMaps": Sequence[str],
    },
)
StartDataSourceSyncJobRequestRequestTypeDef = TypedDict(
    "StartDataSourceSyncJobRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)
StopDataSourceSyncJobRequestRequestTypeDef = TypedDict(
    "StopDataSourceSyncJobRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)
SuggestionHighlightTypeDef = TypedDict(
    "SuggestionHighlightTypeDef",
    {
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
    },
)
TableCellTypeDef = TypedDict(
    "TableCellTypeDef",
    {
        "Value": NotRequired[str],
        "TopAnswer": NotRequired[bool],
        "Highlighted": NotRequired[bool],
        "Header": NotRequired[bool],
    },
)
TemplateConfigurationTypeDef = TypedDict(
    "TemplateConfigurationTypeDef",
    {
        "Template": NotRequired[Mapping[str, Any]],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
ColumnConfigurationOutputTypeDef = TypedDict(
    "ColumnConfigurationOutputTypeDef",
    {
        "DocumentIdColumnName": str,
        "DocumentDataColumnName": str,
        "ChangeDetectingColumns": List[str],
        "DocumentTitleColumnName": NotRequired[str],
        "FieldMappings": NotRequired[List[DataSourceToIndexFieldMappingTypeDef]],
    },
)
ColumnConfigurationTypeDef = TypedDict(
    "ColumnConfigurationTypeDef",
    {
        "DocumentIdColumnName": str,
        "DocumentDataColumnName": str,
        "ChangeDetectingColumns": Sequence[str],
        "DocumentTitleColumnName": NotRequired[str],
        "FieldMappings": NotRequired[Sequence[DataSourceToIndexFieldMappingTypeDef]],
    },
)
GoogleDriveConfigurationOutputTypeDef = TypedDict(
    "GoogleDriveConfigurationOutputTypeDef",
    {
        "SecretArn": str,
        "InclusionPatterns": NotRequired[List[str]],
        "ExclusionPatterns": NotRequired[List[str]],
        "FieldMappings": NotRequired[List[DataSourceToIndexFieldMappingTypeDef]],
        "ExcludeMimeTypes": NotRequired[List[str]],
        "ExcludeUserAccounts": NotRequired[List[str]],
        "ExcludeSharedDrives": NotRequired[List[str]],
    },
)
GoogleDriveConfigurationTypeDef = TypedDict(
    "GoogleDriveConfigurationTypeDef",
    {
        "SecretArn": str,
        "InclusionPatterns": NotRequired[Sequence[str]],
        "ExclusionPatterns": NotRequired[Sequence[str]],
        "FieldMappings": NotRequired[Sequence[DataSourceToIndexFieldMappingTypeDef]],
        "ExcludeMimeTypes": NotRequired[Sequence[str]],
        "ExcludeUserAccounts": NotRequired[Sequence[str]],
        "ExcludeSharedDrives": NotRequired[Sequence[str]],
    },
)
SalesforceChatterFeedConfigurationOutputTypeDef = TypedDict(
    "SalesforceChatterFeedConfigurationOutputTypeDef",
    {
        "DocumentDataFieldName": str,
        "DocumentTitleFieldName": NotRequired[str],
        "FieldMappings": NotRequired[List[DataSourceToIndexFieldMappingTypeDef]],
        "IncludeFilterTypes": NotRequired[List[SalesforceChatterFeedIncludeFilterTypeType]],
    },
)
SalesforceChatterFeedConfigurationTypeDef = TypedDict(
    "SalesforceChatterFeedConfigurationTypeDef",
    {
        "DocumentDataFieldName": str,
        "DocumentTitleFieldName": NotRequired[str],
        "FieldMappings": NotRequired[Sequence[DataSourceToIndexFieldMappingTypeDef]],
        "IncludeFilterTypes": NotRequired[Sequence[SalesforceChatterFeedIncludeFilterTypeType]],
    },
)
SalesforceCustomKnowledgeArticleTypeConfigurationOutputTypeDef = TypedDict(
    "SalesforceCustomKnowledgeArticleTypeConfigurationOutputTypeDef",
    {
        "Name": str,
        "DocumentDataFieldName": str,
        "DocumentTitleFieldName": NotRequired[str],
        "FieldMappings": NotRequired[List[DataSourceToIndexFieldMappingTypeDef]],
    },
)
SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef = TypedDict(
    "SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef",
    {
        "Name": str,
        "DocumentDataFieldName": str,
        "DocumentTitleFieldName": NotRequired[str],
        "FieldMappings": NotRequired[Sequence[DataSourceToIndexFieldMappingTypeDef]],
    },
)
SalesforceStandardKnowledgeArticleTypeConfigurationOutputTypeDef = TypedDict(
    "SalesforceStandardKnowledgeArticleTypeConfigurationOutputTypeDef",
    {
        "DocumentDataFieldName": str,
        "DocumentTitleFieldName": NotRequired[str],
        "FieldMappings": NotRequired[List[DataSourceToIndexFieldMappingTypeDef]],
    },
)
SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef = TypedDict(
    "SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef",
    {
        "DocumentDataFieldName": str,
        "DocumentTitleFieldName": NotRequired[str],
        "FieldMappings": NotRequired[Sequence[DataSourceToIndexFieldMappingTypeDef]],
    },
)
SalesforceStandardObjectAttachmentConfigurationOutputTypeDef = TypedDict(
    "SalesforceStandardObjectAttachmentConfigurationOutputTypeDef",
    {
        "DocumentTitleFieldName": NotRequired[str],
        "FieldMappings": NotRequired[List[DataSourceToIndexFieldMappingTypeDef]],
    },
)
SalesforceStandardObjectAttachmentConfigurationTypeDef = TypedDict(
    "SalesforceStandardObjectAttachmentConfigurationTypeDef",
    {
        "DocumentTitleFieldName": NotRequired[str],
        "FieldMappings": NotRequired[Sequence[DataSourceToIndexFieldMappingTypeDef]],
    },
)
SalesforceStandardObjectConfigurationOutputTypeDef = TypedDict(
    "SalesforceStandardObjectConfigurationOutputTypeDef",
    {
        "Name": SalesforceStandardObjectNameType,
        "DocumentDataFieldName": str,
        "DocumentTitleFieldName": NotRequired[str],
        "FieldMappings": NotRequired[List[DataSourceToIndexFieldMappingTypeDef]],
    },
)
SalesforceStandardObjectConfigurationTypeDef = TypedDict(
    "SalesforceStandardObjectConfigurationTypeDef",
    {
        "Name": SalesforceStandardObjectNameType,
        "DocumentDataFieldName": str,
        "DocumentTitleFieldName": NotRequired[str],
        "FieldMappings": NotRequired[Sequence[DataSourceToIndexFieldMappingTypeDef]],
    },
)
ServiceNowKnowledgeArticleConfigurationOutputTypeDef = TypedDict(
    "ServiceNowKnowledgeArticleConfigurationOutputTypeDef",
    {
        "DocumentDataFieldName": str,
        "CrawlAttachments": NotRequired[bool],
        "IncludeAttachmentFilePatterns": NotRequired[List[str]],
        "ExcludeAttachmentFilePatterns": NotRequired[List[str]],
        "DocumentTitleFieldName": NotRequired[str],
        "FieldMappings": NotRequired[List[DataSourceToIndexFieldMappingTypeDef]],
        "FilterQuery": NotRequired[str],
    },
)
ServiceNowKnowledgeArticleConfigurationTypeDef = TypedDict(
    "ServiceNowKnowledgeArticleConfigurationTypeDef",
    {
        "DocumentDataFieldName": str,
        "CrawlAttachments": NotRequired[bool],
        "IncludeAttachmentFilePatterns": NotRequired[Sequence[str]],
        "ExcludeAttachmentFilePatterns": NotRequired[Sequence[str]],
        "DocumentTitleFieldName": NotRequired[str],
        "FieldMappings": NotRequired[Sequence[DataSourceToIndexFieldMappingTypeDef]],
        "FilterQuery": NotRequired[str],
    },
)
ServiceNowServiceCatalogConfigurationOutputTypeDef = TypedDict(
    "ServiceNowServiceCatalogConfigurationOutputTypeDef",
    {
        "DocumentDataFieldName": str,
        "CrawlAttachments": NotRequired[bool],
        "IncludeAttachmentFilePatterns": NotRequired[List[str]],
        "ExcludeAttachmentFilePatterns": NotRequired[List[str]],
        "DocumentTitleFieldName": NotRequired[str],
        "FieldMappings": NotRequired[List[DataSourceToIndexFieldMappingTypeDef]],
    },
)
ServiceNowServiceCatalogConfigurationTypeDef = TypedDict(
    "ServiceNowServiceCatalogConfigurationTypeDef",
    {
        "DocumentDataFieldName": str,
        "CrawlAttachments": NotRequired[bool],
        "IncludeAttachmentFilePatterns": NotRequired[Sequence[str]],
        "ExcludeAttachmentFilePatterns": NotRequired[Sequence[str]],
        "DocumentTitleFieldName": NotRequired[str],
        "FieldMappings": NotRequired[Sequence[DataSourceToIndexFieldMappingTypeDef]],
    },
)
WorkDocsConfigurationOutputTypeDef = TypedDict(
    "WorkDocsConfigurationOutputTypeDef",
    {
        "OrganizationId": str,
        "CrawlComments": NotRequired[bool],
        "UseChangeLog": NotRequired[bool],
        "InclusionPatterns": NotRequired[List[str]],
        "ExclusionPatterns": NotRequired[List[str]],
        "FieldMappings": NotRequired[List[DataSourceToIndexFieldMappingTypeDef]],
    },
)
WorkDocsConfigurationTypeDef = TypedDict(
    "WorkDocsConfigurationTypeDef",
    {
        "OrganizationId": str,
        "CrawlComments": NotRequired[bool],
        "UseChangeLog": NotRequired[bool],
        "InclusionPatterns": NotRequired[Sequence[str]],
        "ExclusionPatterns": NotRequired[Sequence[str]],
        "FieldMappings": NotRequired[Sequence[DataSourceToIndexFieldMappingTypeDef]],
    },
)
BoxConfigurationOutputTypeDef = TypedDict(
    "BoxConfigurationOutputTypeDef",
    {
        "EnterpriseId": str,
        "SecretArn": str,
        "UseChangeLog": NotRequired[bool],
        "CrawlComments": NotRequired[bool],
        "CrawlTasks": NotRequired[bool],
        "CrawlWebLinks": NotRequired[bool],
        "FileFieldMappings": NotRequired[List[DataSourceToIndexFieldMappingTypeDef]],
        "TaskFieldMappings": NotRequired[List[DataSourceToIndexFieldMappingTypeDef]],
        "CommentFieldMappings": NotRequired[List[DataSourceToIndexFieldMappingTypeDef]],
        "WebLinkFieldMappings": NotRequired[List[DataSourceToIndexFieldMappingTypeDef]],
        "InclusionPatterns": NotRequired[List[str]],
        "ExclusionPatterns": NotRequired[List[str]],
        "VpcConfiguration": NotRequired[DataSourceVpcConfigurationOutputTypeDef],
    },
)
FsxConfigurationOutputTypeDef = TypedDict(
    "FsxConfigurationOutputTypeDef",
    {
        "FileSystemId": str,
        "FileSystemType": Literal["WINDOWS"],
        "VpcConfiguration": DataSourceVpcConfigurationOutputTypeDef,
        "SecretArn": NotRequired[str],
        "InclusionPatterns": NotRequired[List[str]],
        "ExclusionPatterns": NotRequired[List[str]],
        "FieldMappings": NotRequired[List[DataSourceToIndexFieldMappingTypeDef]],
    },
)
JiraConfigurationOutputTypeDef = TypedDict(
    "JiraConfigurationOutputTypeDef",
    {
        "JiraAccountUrl": str,
        "SecretArn": str,
        "UseChangeLog": NotRequired[bool],
        "Project": NotRequired[List[str]],
        "IssueType": NotRequired[List[str]],
        "Status": NotRequired[List[str]],
        "IssueSubEntityFilter": NotRequired[List[IssueSubEntityType]],
        "AttachmentFieldMappings": NotRequired[List[DataSourceToIndexFieldMappingTypeDef]],
        "CommentFieldMappings": NotRequired[List[DataSourceToIndexFieldMappingTypeDef]],
        "IssueFieldMappings": NotRequired[List[DataSourceToIndexFieldMappingTypeDef]],
        "ProjectFieldMappings": NotRequired[List[DataSourceToIndexFieldMappingTypeDef]],
        "WorkLogFieldMappings": NotRequired[List[DataSourceToIndexFieldMappingTypeDef]],
        "InclusionPatterns": NotRequired[List[str]],
        "ExclusionPatterns": NotRequired[List[str]],
        "VpcConfiguration": NotRequired[DataSourceVpcConfigurationOutputTypeDef],
    },
)
QuipConfigurationOutputTypeDef = TypedDict(
    "QuipConfigurationOutputTypeDef",
    {
        "Domain": str,
        "SecretArn": str,
        "CrawlFileComments": NotRequired[bool],
        "CrawlChatRooms": NotRequired[bool],
        "CrawlAttachments": NotRequired[bool],
        "FolderIds": NotRequired[List[str]],
        "ThreadFieldMappings": NotRequired[List[DataSourceToIndexFieldMappingTypeDef]],
        "MessageFieldMappings": NotRequired[List[DataSourceToIndexFieldMappingTypeDef]],
        "AttachmentFieldMappings": NotRequired[List[DataSourceToIndexFieldMappingTypeDef]],
        "InclusionPatterns": NotRequired[List[str]],
        "ExclusionPatterns": NotRequired[List[str]],
        "VpcConfiguration": NotRequired[DataSourceVpcConfigurationOutputTypeDef],
    },
)
SlackConfigurationOutputTypeDef = TypedDict(
    "SlackConfigurationOutputTypeDef",
    {
        "TeamId": str,
        "SecretArn": str,
        "SlackEntityList": List[SlackEntityType],
        "SinceCrawlDate": str,
        "VpcConfiguration": NotRequired[DataSourceVpcConfigurationOutputTypeDef],
        "UseChangeLog": NotRequired[bool],
        "CrawlBotMessage": NotRequired[bool],
        "ExcludeArchived": NotRequired[bool],
        "LookBackPeriod": NotRequired[int],
        "PrivateChannelFilter": NotRequired[List[str]],
        "PublicChannelFilter": NotRequired[List[str]],
        "InclusionPatterns": NotRequired[List[str]],
        "ExclusionPatterns": NotRequired[List[str]],
        "FieldMappings": NotRequired[List[DataSourceToIndexFieldMappingTypeDef]],
    },
)
AlfrescoConfigurationOutputTypeDef = TypedDict(
    "AlfrescoConfigurationOutputTypeDef",
    {
        "SiteUrl": str,
        "SiteId": str,
        "SecretArn": str,
        "SslCertificateS3Path": S3PathTypeDef,
        "CrawlSystemFolders": NotRequired[bool],
        "CrawlComments": NotRequired[bool],
        "EntityFilter": NotRequired[List[AlfrescoEntityType]],
        "DocumentLibraryFieldMappings": NotRequired[List[DataSourceToIndexFieldMappingTypeDef]],
        "BlogFieldMappings": NotRequired[List[DataSourceToIndexFieldMappingTypeDef]],
        "WikiFieldMappings": NotRequired[List[DataSourceToIndexFieldMappingTypeDef]],
        "InclusionPatterns": NotRequired[List[str]],
        "ExclusionPatterns": NotRequired[List[str]],
        "VpcConfiguration": NotRequired[DataSourceVpcConfigurationOutputTypeDef],
    },
)
OnPremiseConfigurationTypeDef = TypedDict(
    "OnPremiseConfigurationTypeDef",
    {
        "HostUrl": str,
        "OrganizationName": str,
        "SslCertificateS3Path": S3PathTypeDef,
    },
)
OneDriveUsersOutputTypeDef = TypedDict(
    "OneDriveUsersOutputTypeDef",
    {
        "OneDriveUserList": NotRequired[List[str]],
        "OneDriveUserS3Path": NotRequired[S3PathTypeDef],
    },
)
OneDriveUsersTypeDef = TypedDict(
    "OneDriveUsersTypeDef",
    {
        "OneDriveUserList": NotRequired[Sequence[str]],
        "OneDriveUserS3Path": NotRequired[S3PathTypeDef],
    },
)
UpdateQuerySuggestionsBlockListRequestRequestTypeDef = TypedDict(
    "UpdateQuerySuggestionsBlockListRequestRequestTypeDef",
    {
        "IndexId": str,
        "Id": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "SourceS3Path": NotRequired[S3PathTypeDef],
        "RoleArn": NotRequired[str],
    },
)
UpdateThesaurusRequestRequestTypeDef = TypedDict(
    "UpdateThesaurusRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "RoleArn": NotRequired[str],
        "SourceS3Path": NotRequired[S3PathTypeDef],
    },
)
AssociateEntitiesToExperienceRequestRequestTypeDef = TypedDict(
    "AssociateEntitiesToExperienceRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "EntityList": Sequence[EntityConfigurationTypeDef],
    },
)
DisassociateEntitiesFromExperienceRequestRequestTypeDef = TypedDict(
    "DisassociateEntitiesFromExperienceRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "EntityList": Sequence[EntityConfigurationTypeDef],
    },
)
AssociateEntitiesToExperienceResponseTypeDef = TypedDict(
    "AssociateEntitiesToExperienceResponseTypeDef",
    {
        "FailedEntityList": List[FailedEntityTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociatePersonasToEntitiesResponseTypeDef = TypedDict(
    "AssociatePersonasToEntitiesResponseTypeDef",
    {
        "FailedEntityList": List[FailedEntityTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAccessControlConfigurationResponseTypeDef = TypedDict(
    "CreateAccessControlConfigurationResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDataSourceResponseTypeDef = TypedDict(
    "CreateDataSourceResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateExperienceResponseTypeDef = TypedDict(
    "CreateExperienceResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFaqResponseTypeDef = TypedDict(
    "CreateFaqResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateIndexResponseTypeDef = TypedDict(
    "CreateIndexResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateQuerySuggestionsBlockListResponseTypeDef = TypedDict(
    "CreateQuerySuggestionsBlockListResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateThesaurusResponseTypeDef = TypedDict(
    "CreateThesaurusResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeFaqResponseTypeDef = TypedDict(
    "DescribeFaqResponseTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "Name": str,
        "Description": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "S3Path": S3PathTypeDef,
        "Status": FaqStatusType,
        "RoleArn": str,
        "ErrorMessage": str,
        "FileFormat": FaqFileFormatType,
        "LanguageCode": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeQuerySuggestionsBlockListResponseTypeDef = TypedDict(
    "DescribeQuerySuggestionsBlockListResponseTypeDef",
    {
        "IndexId": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "Status": QuerySuggestionsBlockListStatusType,
        "ErrorMessage": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "SourceS3Path": S3PathTypeDef,
        "ItemCount": int,
        "FileSizeBytes": int,
        "RoleArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeThesaurusResponseTypeDef = TypedDict(
    "DescribeThesaurusResponseTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "Name": str,
        "Description": str,
        "Status": ThesaurusStatusType,
        "ErrorMessage": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "RoleArn": str,
        "SourceS3Path": S3PathTypeDef,
        "FileSizeBytes": int,
        "TermCount": int,
        "SynonymRuleCount": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateEntitiesFromExperienceResponseTypeDef = TypedDict(
    "DisassociateEntitiesFromExperienceResponseTypeDef",
    {
        "FailedEntityList": List[FailedEntityTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociatePersonasFromEntitiesResponseTypeDef = TypedDict(
    "DisassociatePersonasFromEntitiesResponseTypeDef",
    {
        "FailedEntityList": List[FailedEntityTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAccessControlConfigurationsResponseTypeDef = TypedDict(
    "ListAccessControlConfigurationsResponseTypeDef",
    {
        "AccessControlConfigurations": List[AccessControlConfigurationSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
StartDataSourceSyncJobResponseTypeDef = TypedDict(
    "StartDataSourceSyncJobResponseTypeDef",
    {
        "ExecutionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociatePersonasToEntitiesRequestRequestTypeDef = TypedDict(
    "AssociatePersonasToEntitiesRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "Personas": Sequence[EntityPersonaConfigurationTypeDef],
    },
)
AttributeSuggestionsDescribeConfigTypeDef = TypedDict(
    "AttributeSuggestionsDescribeConfigTypeDef",
    {
        "SuggestableConfigList": NotRequired[List[SuggestableConfigTypeDef]],
        "AttributeSuggestionsMode": NotRequired[AttributeSuggestionsModeType],
    },
)
AttributeSuggestionsUpdateConfigTypeDef = TypedDict(
    "AttributeSuggestionsUpdateConfigTypeDef",
    {
        "SuggestableConfigList": NotRequired[Sequence[SuggestableConfigTypeDef]],
        "AttributeSuggestionsMode": NotRequired[AttributeSuggestionsModeType],
    },
)
AuthenticationConfigurationOutputTypeDef = TypedDict(
    "AuthenticationConfigurationOutputTypeDef",
    {
        "BasicAuthentication": NotRequired[List[BasicAuthenticationConfigurationTypeDef]],
    },
)
AuthenticationConfigurationTypeDef = TypedDict(
    "AuthenticationConfigurationTypeDef",
    {
        "BasicAuthentication": NotRequired[Sequence[BasicAuthenticationConfigurationTypeDef]],
    },
)
BatchDeleteDocumentRequestRequestTypeDef = TypedDict(
    "BatchDeleteDocumentRequestRequestTypeDef",
    {
        "IndexId": str,
        "DocumentIdList": Sequence[str],
        "DataSourceSyncJobMetricTarget": NotRequired[DataSourceSyncJobMetricTargetTypeDef],
    },
)
BatchDeleteDocumentResponseTypeDef = TypedDict(
    "BatchDeleteDocumentResponseTypeDef",
    {
        "FailedDocuments": List[BatchDeleteDocumentResponseFailedDocumentTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDeleteFeaturedResultsSetResponseTypeDef = TypedDict(
    "BatchDeleteFeaturedResultsSetResponseTypeDef",
    {
        "Errors": List[BatchDeleteFeaturedResultsSetErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetDocumentStatusResponseTypeDef = TypedDict(
    "BatchGetDocumentStatusResponseTypeDef",
    {
        "Errors": List[BatchGetDocumentStatusResponseErrorTypeDef],
        "DocumentStatusList": List[StatusTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchPutDocumentResponseTypeDef = TypedDict(
    "BatchPutDocumentResponseTypeDef",
    {
        "FailedDocuments": List[BatchPutDocumentResponseFailedDocumentTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ClickFeedbackTypeDef = TypedDict(
    "ClickFeedbackTypeDef",
    {
        "ResultId": str,
        "ClickTime": TimestampTypeDef,
    },
)
DocumentAttributeValueTypeDef = TypedDict(
    "DocumentAttributeValueTypeDef",
    {
        "StringValue": NotRequired[str],
        "StringListValue": NotRequired[Sequence[str]],
        "LongValue": NotRequired[int],
        "DateValue": NotRequired[TimestampTypeDef],
    },
)
TimeRangeTypeDef = TypedDict(
    "TimeRangeTypeDef",
    {
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
    },
)
CollapseConfigurationTypeDef = TypedDict(
    "CollapseConfigurationTypeDef",
    {
        "DocumentAttributeKey": str,
        "SortingConfigurations": NotRequired[Sequence[SortingConfigurationTypeDef]],
        "MissingAttributeKeyStrategy": NotRequired[MissingAttributeKeyStrategyType],
        "Expand": NotRequired[bool],
        "ExpandConfiguration": NotRequired[ExpandConfigurationTypeDef],
    },
)
ConfluenceAttachmentConfigurationOutputTypeDef = TypedDict(
    "ConfluenceAttachmentConfigurationOutputTypeDef",
    {
        "CrawlAttachments": NotRequired[bool],
        "AttachmentFieldMappings": NotRequired[
            List[ConfluenceAttachmentToIndexFieldMappingTypeDef]
        ],
    },
)
ConfluenceAttachmentConfigurationTypeDef = TypedDict(
    "ConfluenceAttachmentConfigurationTypeDef",
    {
        "CrawlAttachments": NotRequired[bool],
        "AttachmentFieldMappings": NotRequired[
            Sequence[ConfluenceAttachmentToIndexFieldMappingTypeDef]
        ],
    },
)
ConfluenceBlogConfigurationOutputTypeDef = TypedDict(
    "ConfluenceBlogConfigurationOutputTypeDef",
    {
        "BlogFieldMappings": NotRequired[List[ConfluenceBlogToIndexFieldMappingTypeDef]],
    },
)
ConfluenceBlogConfigurationTypeDef = TypedDict(
    "ConfluenceBlogConfigurationTypeDef",
    {
        "BlogFieldMappings": NotRequired[Sequence[ConfluenceBlogToIndexFieldMappingTypeDef]],
    },
)
SharePointConfigurationOutputTypeDef = TypedDict(
    "SharePointConfigurationOutputTypeDef",
    {
        "SharePointVersion": SharePointVersionType,
        "Urls": List[str],
        "SecretArn": str,
        "CrawlAttachments": NotRequired[bool],
        "UseChangeLog": NotRequired[bool],
        "InclusionPatterns": NotRequired[List[str]],
        "ExclusionPatterns": NotRequired[List[str]],
        "VpcConfiguration": NotRequired[DataSourceVpcConfigurationOutputTypeDef],
        "FieldMappings": NotRequired[List[DataSourceToIndexFieldMappingTypeDef]],
        "DocumentTitleFieldName": NotRequired[str],
        "DisableLocalGroups": NotRequired[bool],
        "SslCertificateS3Path": NotRequired[S3PathTypeDef],
        "AuthenticationType": NotRequired[SharePointOnlineAuthenticationTypeType],
        "ProxyConfiguration": NotRequired[ProxyConfigurationTypeDef],
    },
)
ConfluencePageConfigurationOutputTypeDef = TypedDict(
    "ConfluencePageConfigurationOutputTypeDef",
    {
        "PageFieldMappings": NotRequired[List[ConfluencePageToIndexFieldMappingTypeDef]],
    },
)
ConfluencePageConfigurationTypeDef = TypedDict(
    "ConfluencePageConfigurationTypeDef",
    {
        "PageFieldMappings": NotRequired[Sequence[ConfluencePageToIndexFieldMappingTypeDef]],
    },
)
ConfluenceSpaceConfigurationOutputTypeDef = TypedDict(
    "ConfluenceSpaceConfigurationOutputTypeDef",
    {
        "CrawlPersonalSpaces": NotRequired[bool],
        "CrawlArchivedSpaces": NotRequired[bool],
        "IncludeSpaces": NotRequired[List[str]],
        "ExcludeSpaces": NotRequired[List[str]],
        "SpaceFieldMappings": NotRequired[List[ConfluenceSpaceToIndexFieldMappingTypeDef]],
    },
)
ConfluenceSpaceConfigurationTypeDef = TypedDict(
    "ConfluenceSpaceConfigurationTypeDef",
    {
        "CrawlPersonalSpaces": NotRequired[bool],
        "CrawlArchivedSpaces": NotRequired[bool],
        "IncludeSpaces": NotRequired[Sequence[str]],
        "ExcludeSpaces": NotRequired[Sequence[str]],
        "SpaceFieldMappings": NotRequired[Sequence[ConfluenceSpaceToIndexFieldMappingTypeDef]],
    },
)
ContentSourceConfigurationUnionTypeDef = Union[
    ContentSourceConfigurationTypeDef, ContentSourceConfigurationOutputTypeDef
]
SpellCorrectedQueryTypeDef = TypedDict(
    "SpellCorrectedQueryTypeDef",
    {
        "SuggestedQueryText": NotRequired[str],
        "Corrections": NotRequired[List[CorrectionTypeDef]],
    },
)
HierarchicalPrincipalOutputTypeDef = TypedDict(
    "HierarchicalPrincipalOutputTypeDef",
    {
        "PrincipalList": List[PrincipalTypeDef],
    },
)
HierarchicalPrincipalTypeDef = TypedDict(
    "HierarchicalPrincipalTypeDef",
    {
        "PrincipalList": Sequence[PrincipalTypeDef],
    },
)
DataSourceVpcConfigurationUnionTypeDef = Union[
    DataSourceVpcConfigurationTypeDef, DataSourceVpcConfigurationOutputTypeDef
]
CreateFaqRequestRequestTypeDef = TypedDict(
    "CreateFaqRequestRequestTypeDef",
    {
        "IndexId": str,
        "Name": str,
        "S3Path": S3PathTypeDef,
        "RoleArn": str,
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "FileFormat": NotRequired[FaqFileFormatType],
        "ClientToken": NotRequired[str],
        "LanguageCode": NotRequired[str],
    },
)
CreateQuerySuggestionsBlockListRequestRequestTypeDef = TypedDict(
    "CreateQuerySuggestionsBlockListRequestRequestTypeDef",
    {
        "IndexId": str,
        "Name": str,
        "SourceS3Path": S3PathTypeDef,
        "RoleArn": str,
        "Description": NotRequired[str],
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateThesaurusRequestRequestTypeDef = TypedDict(
    "CreateThesaurusRequestRequestTypeDef",
    {
        "IndexId": str,
        "Name": str,
        "RoleArn": str,
        "SourceS3Path": S3PathTypeDef,
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ClientToken": NotRequired[str],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CreateFeaturedResultsSetRequestRequestTypeDef = TypedDict(
    "CreateFeaturedResultsSetRequestRequestTypeDef",
    {
        "IndexId": str,
        "FeaturedResultsSetName": str,
        "Description": NotRequired[str],
        "ClientToken": NotRequired[str],
        "Status": NotRequired[FeaturedResultsSetStatusType],
        "QueryTexts": NotRequired[Sequence[str]],
        "FeaturedDocuments": NotRequired[Sequence[FeaturedDocumentTypeDef]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
FeaturedResultsSetTypeDef = TypedDict(
    "FeaturedResultsSetTypeDef",
    {
        "FeaturedResultsSetId": NotRequired[str],
        "FeaturedResultsSetName": NotRequired[str],
        "Description": NotRequired[str],
        "Status": NotRequired[FeaturedResultsSetStatusType],
        "QueryTexts": NotRequired[List[str]],
        "FeaturedDocuments": NotRequired[List[FeaturedDocumentTypeDef]],
        "LastUpdatedTimestamp": NotRequired[int],
        "CreationTimestamp": NotRequired[int],
    },
)
UpdateFeaturedResultsSetRequestRequestTypeDef = TypedDict(
    "UpdateFeaturedResultsSetRequestRequestTypeDef",
    {
        "IndexId": str,
        "FeaturedResultsSetId": str,
        "FeaturedResultsSetName": NotRequired[str],
        "Description": NotRequired[str],
        "Status": NotRequired[FeaturedResultsSetStatusType],
        "QueryTexts": NotRequired[Sequence[str]],
        "FeaturedDocuments": NotRequired[Sequence[FeaturedDocumentTypeDef]],
    },
)
UserContextTypeDef = TypedDict(
    "UserContextTypeDef",
    {
        "Token": NotRequired[str],
        "UserId": NotRequired[str],
        "Groups": NotRequired[Sequence[str]],
        "DataSourceGroups": NotRequired[Sequence[DataSourceGroupTypeDef]],
    },
)
ListDataSourcesResponseTypeDef = TypedDict(
    "ListDataSourcesResponseTypeDef",
    {
        "SummaryItems": List[DataSourceSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DataSourceSyncJobTypeDef = TypedDict(
    "DataSourceSyncJobTypeDef",
    {
        "ExecutionId": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "Status": NotRequired[DataSourceSyncJobStatusType],
        "ErrorMessage": NotRequired[str],
        "ErrorCode": NotRequired[ErrorCodeType],
        "DataSourceErrorCode": NotRequired[str],
        "Metrics": NotRequired[DataSourceSyncJobMetricsTypeDef],
    },
)
ExperiencesSummaryTypeDef = TypedDict(
    "ExperiencesSummaryTypeDef",
    {
        "Name": NotRequired[str],
        "Id": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "Status": NotRequired[ExperienceStatusType],
        "Endpoints": NotRequired[List[ExperienceEndpointTypeDef]],
    },
)
DescribeFeaturedResultsSetResponseTypeDef = TypedDict(
    "DescribeFeaturedResultsSetResponseTypeDef",
    {
        "FeaturedResultsSetId": str,
        "FeaturedResultsSetName": str,
        "Description": str,
        "Status": FeaturedResultsSetStatusType,
        "QueryTexts": List[str],
        "FeaturedDocumentsWithMetadata": List[FeaturedDocumentWithMetadataTypeDef],
        "FeaturedDocumentsMissing": List[FeaturedDocumentMissingTypeDef],
        "LastUpdatedTimestamp": int,
        "CreationTimestamp": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePrincipalMappingResponseTypeDef = TypedDict(
    "DescribePrincipalMappingResponseTypeDef",
    {
        "IndexId": str,
        "DataSourceId": str,
        "GroupId": str,
        "GroupOrderingIdSummaries": List[GroupOrderingIdSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DocumentAttributeConditionOutputTypeDef = TypedDict(
    "DocumentAttributeConditionOutputTypeDef",
    {
        "ConditionDocumentAttributeKey": str,
        "Operator": ConditionOperatorType,
        "ConditionOnValue": NotRequired[DocumentAttributeValueOutputTypeDef],
    },
)
DocumentAttributeOutputTypeDef = TypedDict(
    "DocumentAttributeOutputTypeDef",
    {
        "Key": str,
        "Value": DocumentAttributeValueOutputTypeDef,
    },
)
DocumentAttributeTargetOutputTypeDef = TypedDict(
    "DocumentAttributeTargetOutputTypeDef",
    {
        "TargetDocumentAttributeKey": NotRequired[str],
        "TargetDocumentAttributeValueDeletion": NotRequired[bool],
        "TargetDocumentAttributeValue": NotRequired[DocumentAttributeValueOutputTypeDef],
    },
)
DocumentAttributeValueCountPairTypeDef = TypedDict(
    "DocumentAttributeValueCountPairTypeDef",
    {
        "DocumentAttributeValue": NotRequired[DocumentAttributeValueOutputTypeDef],
        "Count": NotRequired[int],
        "FacetResults": NotRequired[List[Dict[str, Any]]],
    },
)
DocumentMetadataConfigurationOutputTypeDef = TypedDict(
    "DocumentMetadataConfigurationOutputTypeDef",
    {
        "Name": str,
        "Type": DocumentAttributeValueTypeType,
        "Relevance": NotRequired[RelevanceOutputTypeDef],
        "Search": NotRequired[SearchTypeDef],
    },
)
S3DataSourceConfigurationOutputTypeDef = TypedDict(
    "S3DataSourceConfigurationOutputTypeDef",
    {
        "BucketName": str,
        "InclusionPrefixes": NotRequired[List[str]],
        "InclusionPatterns": NotRequired[List[str]],
        "ExclusionPatterns": NotRequired[List[str]],
        "DocumentsMetadataConfiguration": NotRequired[DocumentsMetadataConfigurationTypeDef],
        "AccessControlListConfiguration": NotRequired[AccessControlListConfigurationTypeDef],
    },
)
S3DataSourceConfigurationTypeDef = TypedDict(
    "S3DataSourceConfigurationTypeDef",
    {
        "BucketName": str,
        "InclusionPrefixes": NotRequired[Sequence[str]],
        "InclusionPatterns": NotRequired[Sequence[str]],
        "ExclusionPatterns": NotRequired[Sequence[str]],
        "DocumentsMetadataConfiguration": NotRequired[DocumentsMetadataConfigurationTypeDef],
        "AccessControlListConfiguration": NotRequired[AccessControlListConfigurationTypeDef],
    },
)
ExperienceEntitiesSummaryTypeDef = TypedDict(
    "ExperienceEntitiesSummaryTypeDef",
    {
        "EntityId": NotRequired[str],
        "EntityType": NotRequired[EntityTypeType],
        "DisplayData": NotRequired[EntityDisplayDataTypeDef],
    },
)
ExperienceConfigurationOutputTypeDef = TypedDict(
    "ExperienceConfigurationOutputTypeDef",
    {
        "ContentSourceConfiguration": NotRequired[ContentSourceConfigurationOutputTypeDef],
        "UserIdentityConfiguration": NotRequired[UserIdentityConfigurationTypeDef],
    },
)
ListFaqsResponseTypeDef = TypedDict(
    "ListFaqsResponseTypeDef",
    {
        "FaqSummaryItems": List[FaqSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListFeaturedResultsSetsResponseTypeDef = TypedDict(
    "ListFeaturedResultsSetsResponseTypeDef",
    {
        "FeaturedResultsSetSummaryItems": List[FeaturedResultsSetSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetSnapshotsResponseTypeDef = TypedDict(
    "GetSnapshotsResponseTypeDef",
    {
        "SnapShotTimeFilter": TimeRangeOutputTypeDef,
        "SnapshotsDataHeader": List[str],
        "SnapshotsData": List[List[str]],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GroupMembersTypeDef = TypedDict(
    "GroupMembersTypeDef",
    {
        "MemberGroups": NotRequired[Sequence[MemberGroupTypeDef]],
        "MemberUsers": NotRequired[Sequence[MemberUserTypeDef]],
        "S3PathforGroupMembers": NotRequired[S3PathTypeDef],
    },
)
ListGroupsOlderThanOrderingIdResponseTypeDef = TypedDict(
    "ListGroupsOlderThanOrderingIdResponseTypeDef",
    {
        "GroupsSummaries": List[GroupSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
TextWithHighlightsTypeDef = TypedDict(
    "TextWithHighlightsTypeDef",
    {
        "Text": NotRequired[str],
        "Highlights": NotRequired[List[HighlightTypeDef]],
    },
)
ListIndicesResponseTypeDef = TypedDict(
    "ListIndicesResponseTypeDef",
    {
        "IndexConfigurationSummaryItems": List[IndexConfigurationSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
IndexStatisticsTypeDef = TypedDict(
    "IndexStatisticsTypeDef",
    {
        "FaqStatistics": FaqStatisticsTypeDef,
        "TextDocumentStatistics": TextDocumentStatisticsTypeDef,
    },
)
UserTokenConfigurationTypeDef = TypedDict(
    "UserTokenConfigurationTypeDef",
    {
        "JwtTokenTypeConfiguration": NotRequired[JwtTokenTypeConfigurationTypeDef],
        "JsonTokenTypeConfiguration": NotRequired[JsonTokenTypeConfigurationTypeDef],
    },
)
ListEntityPersonasResponseTypeDef = TypedDict(
    "ListEntityPersonasResponseTypeDef",
    {
        "SummaryItems": List[PersonasSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListQuerySuggestionsBlockListsResponseTypeDef = TypedDict(
    "ListQuerySuggestionsBlockListsResponseTypeDef",
    {
        "BlockListSummaryItems": List[QuerySuggestionsBlockListSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListThesauriResponseTypeDef = TypedDict(
    "ListThesauriResponseTypeDef",
    {
        "ThesaurusSummaryItems": List[ThesaurusSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
RelevanceUnionTypeDef = Union[RelevanceTypeDef, RelevanceOutputTypeDef]
SeedUrlConfigurationUnionTypeDef = Union[
    SeedUrlConfigurationTypeDef, SeedUrlConfigurationOutputTypeDef
]
UrlsOutputTypeDef = TypedDict(
    "UrlsOutputTypeDef",
    {
        "SeedUrlConfiguration": NotRequired[SeedUrlConfigurationOutputTypeDef],
        "SiteMapsConfiguration": NotRequired[SiteMapsConfigurationOutputTypeDef],
    },
)
SiteMapsConfigurationUnionTypeDef = Union[
    SiteMapsConfigurationTypeDef, SiteMapsConfigurationOutputTypeDef
]
SuggestionTextWithHighlightsTypeDef = TypedDict(
    "SuggestionTextWithHighlightsTypeDef",
    {
        "Text": NotRequired[str],
        "Highlights": NotRequired[List[SuggestionHighlightTypeDef]],
    },
)
TableRowTypeDef = TypedDict(
    "TableRowTypeDef",
    {
        "Cells": NotRequired[List[TableCellTypeDef]],
    },
)
TemplateConfigurationUnionTypeDef = Union[
    TemplateConfigurationTypeDef, TemplateConfigurationOutputTypeDef
]
DatabaseConfigurationOutputTypeDef = TypedDict(
    "DatabaseConfigurationOutputTypeDef",
    {
        "DatabaseEngineType": DatabaseEngineTypeType,
        "ConnectionConfiguration": ConnectionConfigurationTypeDef,
        "ColumnConfiguration": ColumnConfigurationOutputTypeDef,
        "VpcConfiguration": NotRequired[DataSourceVpcConfigurationOutputTypeDef],
        "AclConfiguration": NotRequired[AclConfigurationTypeDef],
        "SqlConfiguration": NotRequired[SqlConfigurationTypeDef],
    },
)
ColumnConfigurationUnionTypeDef = Union[
    ColumnConfigurationTypeDef, ColumnConfigurationOutputTypeDef
]
GoogleDriveConfigurationUnionTypeDef = Union[
    GoogleDriveConfigurationTypeDef, GoogleDriveConfigurationOutputTypeDef
]
SalesforceChatterFeedConfigurationUnionTypeDef = Union[
    SalesforceChatterFeedConfigurationTypeDef, SalesforceChatterFeedConfigurationOutputTypeDef
]
SalesforceCustomKnowledgeArticleTypeConfigurationUnionTypeDef = Union[
    SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef,
    SalesforceCustomKnowledgeArticleTypeConfigurationOutputTypeDef,
]
SalesforceKnowledgeArticleConfigurationOutputTypeDef = TypedDict(
    "SalesforceKnowledgeArticleConfigurationOutputTypeDef",
    {
        "IncludedStates": List[SalesforceKnowledgeArticleStateType],
        "StandardKnowledgeArticleTypeConfiguration": NotRequired[
            SalesforceStandardKnowledgeArticleTypeConfigurationOutputTypeDef
        ],
        "CustomKnowledgeArticleTypeConfigurations": NotRequired[
            List[SalesforceCustomKnowledgeArticleTypeConfigurationOutputTypeDef]
        ],
    },
)
SalesforceStandardKnowledgeArticleTypeConfigurationUnionTypeDef = Union[
    SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef,
    SalesforceStandardKnowledgeArticleTypeConfigurationOutputTypeDef,
]
SalesforceStandardObjectAttachmentConfigurationUnionTypeDef = Union[
    SalesforceStandardObjectAttachmentConfigurationTypeDef,
    SalesforceStandardObjectAttachmentConfigurationOutputTypeDef,
]
SalesforceStandardObjectConfigurationUnionTypeDef = Union[
    SalesforceStandardObjectConfigurationTypeDef, SalesforceStandardObjectConfigurationOutputTypeDef
]
ServiceNowKnowledgeArticleConfigurationUnionTypeDef = Union[
    ServiceNowKnowledgeArticleConfigurationTypeDef,
    ServiceNowKnowledgeArticleConfigurationOutputTypeDef,
]
ServiceNowConfigurationOutputTypeDef = TypedDict(
    "ServiceNowConfigurationOutputTypeDef",
    {
        "HostUrl": str,
        "SecretArn": str,
        "ServiceNowBuildVersion": ServiceNowBuildVersionTypeType,
        "KnowledgeArticleConfiguration": NotRequired[
            ServiceNowKnowledgeArticleConfigurationOutputTypeDef
        ],
        "ServiceCatalogConfiguration": NotRequired[
            ServiceNowServiceCatalogConfigurationOutputTypeDef
        ],
        "AuthenticationType": NotRequired[ServiceNowAuthenticationTypeType],
    },
)
ServiceNowServiceCatalogConfigurationUnionTypeDef = Union[
    ServiceNowServiceCatalogConfigurationTypeDef, ServiceNowServiceCatalogConfigurationOutputTypeDef
]
WorkDocsConfigurationUnionTypeDef = Union[
    WorkDocsConfigurationTypeDef, WorkDocsConfigurationOutputTypeDef
]
GitHubConfigurationOutputTypeDef = TypedDict(
    "GitHubConfigurationOutputTypeDef",
    {
        "SecretArn": str,
        "SaaSConfiguration": NotRequired[SaaSConfigurationTypeDef],
        "OnPremiseConfiguration": NotRequired[OnPremiseConfigurationTypeDef],
        "Type": NotRequired[TypeType],
        "UseChangeLog": NotRequired[bool],
        "GitHubDocumentCrawlProperties": NotRequired[GitHubDocumentCrawlPropertiesTypeDef],
        "RepositoryFilter": NotRequired[List[str]],
        "InclusionFolderNamePatterns": NotRequired[List[str]],
        "InclusionFileTypePatterns": NotRequired[List[str]],
        "InclusionFileNamePatterns": NotRequired[List[str]],
        "ExclusionFolderNamePatterns": NotRequired[List[str]],
        "ExclusionFileTypePatterns": NotRequired[List[str]],
        "ExclusionFileNamePatterns": NotRequired[List[str]],
        "VpcConfiguration": NotRequired[DataSourceVpcConfigurationOutputTypeDef],
        "GitHubRepositoryConfigurationFieldMappings": NotRequired[
            List[DataSourceToIndexFieldMappingTypeDef]
        ],
        "GitHubCommitConfigurationFieldMappings": NotRequired[
            List[DataSourceToIndexFieldMappingTypeDef]
        ],
        "GitHubIssueDocumentConfigurationFieldMappings": NotRequired[
            List[DataSourceToIndexFieldMappingTypeDef]
        ],
        "GitHubIssueCommentConfigurationFieldMappings": NotRequired[
            List[DataSourceToIndexFieldMappingTypeDef]
        ],
        "GitHubIssueAttachmentConfigurationFieldMappings": NotRequired[
            List[DataSourceToIndexFieldMappingTypeDef]
        ],
        "GitHubPullRequestCommentConfigurationFieldMappings": NotRequired[
            List[DataSourceToIndexFieldMappingTypeDef]
        ],
        "GitHubPullRequestDocumentConfigurationFieldMappings": NotRequired[
            List[DataSourceToIndexFieldMappingTypeDef]
        ],
        "GitHubPullRequestDocumentAttachmentConfigurationFieldMappings": NotRequired[
            List[DataSourceToIndexFieldMappingTypeDef]
        ],
    },
)
OneDriveConfigurationOutputTypeDef = TypedDict(
    "OneDriveConfigurationOutputTypeDef",
    {
        "TenantDomain": str,
        "SecretArn": str,
        "OneDriveUsers": OneDriveUsersOutputTypeDef,
        "InclusionPatterns": NotRequired[List[str]],
        "ExclusionPatterns": NotRequired[List[str]],
        "FieldMappings": NotRequired[List[DataSourceToIndexFieldMappingTypeDef]],
        "DisableLocalGroups": NotRequired[bool],
    },
)
OneDriveUsersUnionTypeDef = Union[OneDriveUsersTypeDef, OneDriveUsersOutputTypeDef]
DescribeQuerySuggestionsConfigResponseTypeDef = TypedDict(
    "DescribeQuerySuggestionsConfigResponseTypeDef",
    {
        "Mode": ModeType,
        "Status": QuerySuggestionsStatusType,
        "QueryLogLookBackWindowInDays": int,
        "IncludeQueriesWithoutUserInformation": bool,
        "MinimumNumberOfQueryingUsers": int,
        "MinimumQueryCount": int,
        "LastSuggestionsBuildTime": datetime,
        "LastClearTime": datetime,
        "TotalSuggestionsCount": int,
        "AttributeSuggestionsConfig": AttributeSuggestionsDescribeConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateQuerySuggestionsConfigRequestRequestTypeDef = TypedDict(
    "UpdateQuerySuggestionsConfigRequestRequestTypeDef",
    {
        "IndexId": str,
        "Mode": NotRequired[ModeType],
        "QueryLogLookBackWindowInDays": NotRequired[int],
        "IncludeQueriesWithoutUserInformation": NotRequired[bool],
        "MinimumNumberOfQueryingUsers": NotRequired[int],
        "MinimumQueryCount": NotRequired[int],
        "AttributeSuggestionsConfig": NotRequired[AttributeSuggestionsUpdateConfigTypeDef],
    },
)
AuthenticationConfigurationUnionTypeDef = Union[
    AuthenticationConfigurationTypeDef, AuthenticationConfigurationOutputTypeDef
]
SubmitFeedbackRequestRequestTypeDef = TypedDict(
    "SubmitFeedbackRequestRequestTypeDef",
    {
        "IndexId": str,
        "QueryId": str,
        "ClickFeedbackItems": NotRequired[Sequence[ClickFeedbackTypeDef]],
        "RelevanceFeedbackItems": NotRequired[Sequence[RelevanceFeedbackTypeDef]],
    },
)
DocumentAttributeValueUnionTypeDef = Union[
    DocumentAttributeValueTypeDef, DocumentAttributeValueOutputTypeDef
]
ListDataSourceSyncJobsRequestRequestTypeDef = TypedDict(
    "ListDataSourceSyncJobsRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "StartTimeFilter": NotRequired[TimeRangeTypeDef],
        "StatusFilter": NotRequired[DataSourceSyncJobStatusType],
    },
)
ConfluenceAttachmentConfigurationUnionTypeDef = Union[
    ConfluenceAttachmentConfigurationTypeDef, ConfluenceAttachmentConfigurationOutputTypeDef
]
ConfluenceBlogConfigurationUnionTypeDef = Union[
    ConfluenceBlogConfigurationTypeDef, ConfluenceBlogConfigurationOutputTypeDef
]
ConfluencePageConfigurationUnionTypeDef = Union[
    ConfluencePageConfigurationTypeDef, ConfluencePageConfigurationOutputTypeDef
]
ConfluenceConfigurationOutputTypeDef = TypedDict(
    "ConfluenceConfigurationOutputTypeDef",
    {
        "ServerUrl": str,
        "SecretArn": str,
        "Version": ConfluenceVersionType,
        "SpaceConfiguration": NotRequired[ConfluenceSpaceConfigurationOutputTypeDef],
        "PageConfiguration": NotRequired[ConfluencePageConfigurationOutputTypeDef],
        "BlogConfiguration": NotRequired[ConfluenceBlogConfigurationOutputTypeDef],
        "AttachmentConfiguration": NotRequired[ConfluenceAttachmentConfigurationOutputTypeDef],
        "VpcConfiguration": NotRequired[DataSourceVpcConfigurationOutputTypeDef],
        "InclusionPatterns": NotRequired[List[str]],
        "ExclusionPatterns": NotRequired[List[str]],
        "ProxyConfiguration": NotRequired[ProxyConfigurationTypeDef],
        "AuthenticationType": NotRequired[ConfluenceAuthenticationTypeType],
    },
)
ConfluenceSpaceConfigurationUnionTypeDef = Union[
    ConfluenceSpaceConfigurationTypeDef, ConfluenceSpaceConfigurationOutputTypeDef
]
ExperienceConfigurationTypeDef = TypedDict(
    "ExperienceConfigurationTypeDef",
    {
        "ContentSourceConfiguration": NotRequired[ContentSourceConfigurationUnionTypeDef],
        "UserIdentityConfiguration": NotRequired[UserIdentityConfigurationTypeDef],
    },
)
DescribeAccessControlConfigurationResponseTypeDef = TypedDict(
    "DescribeAccessControlConfigurationResponseTypeDef",
    {
        "Name": str,
        "Description": str,
        "ErrorMessage": str,
        "AccessControlList": List[PrincipalTypeDef],
        "HierarchicalAccessControlList": List[HierarchicalPrincipalOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
HierarchicalPrincipalUnionTypeDef = Union[
    HierarchicalPrincipalTypeDef, HierarchicalPrincipalOutputTypeDef
]
UpdateAccessControlConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateAccessControlConfigurationRequestRequestTypeDef",
    {
        "IndexId": str,
        "Id": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "AccessControlList": NotRequired[Sequence[PrincipalTypeDef]],
        "HierarchicalAccessControlList": NotRequired[Sequence[HierarchicalPrincipalTypeDef]],
    },
)
AlfrescoConfigurationTypeDef = TypedDict(
    "AlfrescoConfigurationTypeDef",
    {
        "SiteUrl": str,
        "SiteId": str,
        "SecretArn": str,
        "SslCertificateS3Path": S3PathTypeDef,
        "CrawlSystemFolders": NotRequired[bool],
        "CrawlComments": NotRequired[bool],
        "EntityFilter": NotRequired[Sequence[AlfrescoEntityType]],
        "DocumentLibraryFieldMappings": NotRequired[Sequence[DataSourceToIndexFieldMappingTypeDef]],
        "BlogFieldMappings": NotRequired[Sequence[DataSourceToIndexFieldMappingTypeDef]],
        "WikiFieldMappings": NotRequired[Sequence[DataSourceToIndexFieldMappingTypeDef]],
        "InclusionPatterns": NotRequired[Sequence[str]],
        "ExclusionPatterns": NotRequired[Sequence[str]],
        "VpcConfiguration": NotRequired[DataSourceVpcConfigurationUnionTypeDef],
    },
)
BoxConfigurationTypeDef = TypedDict(
    "BoxConfigurationTypeDef",
    {
        "EnterpriseId": str,
        "SecretArn": str,
        "UseChangeLog": NotRequired[bool],
        "CrawlComments": NotRequired[bool],
        "CrawlTasks": NotRequired[bool],
        "CrawlWebLinks": NotRequired[bool],
        "FileFieldMappings": NotRequired[Sequence[DataSourceToIndexFieldMappingTypeDef]],
        "TaskFieldMappings": NotRequired[Sequence[DataSourceToIndexFieldMappingTypeDef]],
        "CommentFieldMappings": NotRequired[Sequence[DataSourceToIndexFieldMappingTypeDef]],
        "WebLinkFieldMappings": NotRequired[Sequence[DataSourceToIndexFieldMappingTypeDef]],
        "InclusionPatterns": NotRequired[Sequence[str]],
        "ExclusionPatterns": NotRequired[Sequence[str]],
        "VpcConfiguration": NotRequired[DataSourceVpcConfigurationUnionTypeDef],
    },
)
FsxConfigurationTypeDef = TypedDict(
    "FsxConfigurationTypeDef",
    {
        "FileSystemId": str,
        "FileSystemType": Literal["WINDOWS"],
        "VpcConfiguration": DataSourceVpcConfigurationUnionTypeDef,
        "SecretArn": NotRequired[str],
        "InclusionPatterns": NotRequired[Sequence[str]],
        "ExclusionPatterns": NotRequired[Sequence[str]],
        "FieldMappings": NotRequired[Sequence[DataSourceToIndexFieldMappingTypeDef]],
    },
)
GitHubConfigurationTypeDef = TypedDict(
    "GitHubConfigurationTypeDef",
    {
        "SecretArn": str,
        "SaaSConfiguration": NotRequired[SaaSConfigurationTypeDef],
        "OnPremiseConfiguration": NotRequired[OnPremiseConfigurationTypeDef],
        "Type": NotRequired[TypeType],
        "UseChangeLog": NotRequired[bool],
        "GitHubDocumentCrawlProperties": NotRequired[GitHubDocumentCrawlPropertiesTypeDef],
        "RepositoryFilter": NotRequired[Sequence[str]],
        "InclusionFolderNamePatterns": NotRequired[Sequence[str]],
        "InclusionFileTypePatterns": NotRequired[Sequence[str]],
        "InclusionFileNamePatterns": NotRequired[Sequence[str]],
        "ExclusionFolderNamePatterns": NotRequired[Sequence[str]],
        "ExclusionFileTypePatterns": NotRequired[Sequence[str]],
        "ExclusionFileNamePatterns": NotRequired[Sequence[str]],
        "VpcConfiguration": NotRequired[DataSourceVpcConfigurationUnionTypeDef],
        "GitHubRepositoryConfigurationFieldMappings": NotRequired[
            Sequence[DataSourceToIndexFieldMappingTypeDef]
        ],
        "GitHubCommitConfigurationFieldMappings": NotRequired[
            Sequence[DataSourceToIndexFieldMappingTypeDef]
        ],
        "GitHubIssueDocumentConfigurationFieldMappings": NotRequired[
            Sequence[DataSourceToIndexFieldMappingTypeDef]
        ],
        "GitHubIssueCommentConfigurationFieldMappings": NotRequired[
            Sequence[DataSourceToIndexFieldMappingTypeDef]
        ],
        "GitHubIssueAttachmentConfigurationFieldMappings": NotRequired[
            Sequence[DataSourceToIndexFieldMappingTypeDef]
        ],
        "GitHubPullRequestCommentConfigurationFieldMappings": NotRequired[
            Sequence[DataSourceToIndexFieldMappingTypeDef]
        ],
        "GitHubPullRequestDocumentConfigurationFieldMappings": NotRequired[
            Sequence[DataSourceToIndexFieldMappingTypeDef]
        ],
        "GitHubPullRequestDocumentAttachmentConfigurationFieldMappings": NotRequired[
            Sequence[DataSourceToIndexFieldMappingTypeDef]
        ],
    },
)
JiraConfigurationTypeDef = TypedDict(
    "JiraConfigurationTypeDef",
    {
        "JiraAccountUrl": str,
        "SecretArn": str,
        "UseChangeLog": NotRequired[bool],
        "Project": NotRequired[Sequence[str]],
        "IssueType": NotRequired[Sequence[str]],
        "Status": NotRequired[Sequence[str]],
        "IssueSubEntityFilter": NotRequired[Sequence[IssueSubEntityType]],
        "AttachmentFieldMappings": NotRequired[Sequence[DataSourceToIndexFieldMappingTypeDef]],
        "CommentFieldMappings": NotRequired[Sequence[DataSourceToIndexFieldMappingTypeDef]],
        "IssueFieldMappings": NotRequired[Sequence[DataSourceToIndexFieldMappingTypeDef]],
        "ProjectFieldMappings": NotRequired[Sequence[DataSourceToIndexFieldMappingTypeDef]],
        "WorkLogFieldMappings": NotRequired[Sequence[DataSourceToIndexFieldMappingTypeDef]],
        "InclusionPatterns": NotRequired[Sequence[str]],
        "ExclusionPatterns": NotRequired[Sequence[str]],
        "VpcConfiguration": NotRequired[DataSourceVpcConfigurationUnionTypeDef],
    },
)
QuipConfigurationTypeDef = TypedDict(
    "QuipConfigurationTypeDef",
    {
        "Domain": str,
        "SecretArn": str,
        "CrawlFileComments": NotRequired[bool],
        "CrawlChatRooms": NotRequired[bool],
        "CrawlAttachments": NotRequired[bool],
        "FolderIds": NotRequired[Sequence[str]],
        "ThreadFieldMappings": NotRequired[Sequence[DataSourceToIndexFieldMappingTypeDef]],
        "MessageFieldMappings": NotRequired[Sequence[DataSourceToIndexFieldMappingTypeDef]],
        "AttachmentFieldMappings": NotRequired[Sequence[DataSourceToIndexFieldMappingTypeDef]],
        "InclusionPatterns": NotRequired[Sequence[str]],
        "ExclusionPatterns": NotRequired[Sequence[str]],
        "VpcConfiguration": NotRequired[DataSourceVpcConfigurationUnionTypeDef],
    },
)
SharePointConfigurationTypeDef = TypedDict(
    "SharePointConfigurationTypeDef",
    {
        "SharePointVersion": SharePointVersionType,
        "Urls": Sequence[str],
        "SecretArn": str,
        "CrawlAttachments": NotRequired[bool],
        "UseChangeLog": NotRequired[bool],
        "InclusionPatterns": NotRequired[Sequence[str]],
        "ExclusionPatterns": NotRequired[Sequence[str]],
        "VpcConfiguration": NotRequired[DataSourceVpcConfigurationUnionTypeDef],
        "FieldMappings": NotRequired[Sequence[DataSourceToIndexFieldMappingTypeDef]],
        "DocumentTitleFieldName": NotRequired[str],
        "DisableLocalGroups": NotRequired[bool],
        "SslCertificateS3Path": NotRequired[S3PathTypeDef],
        "AuthenticationType": NotRequired[SharePointOnlineAuthenticationTypeType],
        "ProxyConfiguration": NotRequired[ProxyConfigurationTypeDef],
    },
)
SlackConfigurationTypeDef = TypedDict(
    "SlackConfigurationTypeDef",
    {
        "TeamId": str,
        "SecretArn": str,
        "SlackEntityList": Sequence[SlackEntityType],
        "SinceCrawlDate": str,
        "VpcConfiguration": NotRequired[DataSourceVpcConfigurationUnionTypeDef],
        "UseChangeLog": NotRequired[bool],
        "CrawlBotMessage": NotRequired[bool],
        "ExcludeArchived": NotRequired[bool],
        "LookBackPeriod": NotRequired[int],
        "PrivateChannelFilter": NotRequired[Sequence[str]],
        "PublicChannelFilter": NotRequired[Sequence[str]],
        "InclusionPatterns": NotRequired[Sequence[str]],
        "ExclusionPatterns": NotRequired[Sequence[str]],
        "FieldMappings": NotRequired[Sequence[DataSourceToIndexFieldMappingTypeDef]],
    },
)
CreateFeaturedResultsSetResponseTypeDef = TypedDict(
    "CreateFeaturedResultsSetResponseTypeDef",
    {
        "FeaturedResultsSet": FeaturedResultsSetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFeaturedResultsSetResponseTypeDef = TypedDict(
    "UpdateFeaturedResultsSetResponseTypeDef",
    {
        "FeaturedResultsSet": FeaturedResultsSetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDataSourceSyncJobsResponseTypeDef = TypedDict(
    "ListDataSourceSyncJobsResponseTypeDef",
    {
        "History": List[DataSourceSyncJobTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListExperiencesResponseTypeDef = TypedDict(
    "ListExperiencesResponseTypeDef",
    {
        "SummaryItems": List[ExperiencesSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
HookConfigurationOutputTypeDef = TypedDict(
    "HookConfigurationOutputTypeDef",
    {
        "LambdaArn": str,
        "S3Bucket": str,
        "InvocationCondition": NotRequired[DocumentAttributeConditionOutputTypeDef],
    },
)
RetrieveResultItemTypeDef = TypedDict(
    "RetrieveResultItemTypeDef",
    {
        "Id": NotRequired[str],
        "DocumentId": NotRequired[str],
        "DocumentTitle": NotRequired[str],
        "Content": NotRequired[str],
        "DocumentURI": NotRequired[str],
        "DocumentAttributes": NotRequired[List[DocumentAttributeOutputTypeDef]],
        "ScoreAttributes": NotRequired[ScoreAttributesTypeDef],
    },
)
SourceDocumentTypeDef = TypedDict(
    "SourceDocumentTypeDef",
    {
        "DocumentId": NotRequired[str],
        "SuggestionAttributes": NotRequired[List[str]],
        "AdditionalAttributes": NotRequired[List[DocumentAttributeOutputTypeDef]],
    },
)
InlineCustomDocumentEnrichmentConfigurationOutputTypeDef = TypedDict(
    "InlineCustomDocumentEnrichmentConfigurationOutputTypeDef",
    {
        "Condition": NotRequired[DocumentAttributeConditionOutputTypeDef],
        "Target": NotRequired[DocumentAttributeTargetOutputTypeDef],
        "DocumentContentDeletion": NotRequired[bool],
    },
)
FacetResultTypeDef = TypedDict(
    "FacetResultTypeDef",
    {
        "DocumentAttributeKey": NotRequired[str],
        "DocumentAttributeValueType": NotRequired[DocumentAttributeValueTypeType],
        "DocumentAttributeValueCountPairs": NotRequired[
            List[DocumentAttributeValueCountPairTypeDef]
        ],
    },
)
S3DataSourceConfigurationUnionTypeDef = Union[
    S3DataSourceConfigurationTypeDef, S3DataSourceConfigurationOutputTypeDef
]
ListExperienceEntitiesResponseTypeDef = TypedDict(
    "ListExperienceEntitiesResponseTypeDef",
    {
        "SummaryItems": List[ExperienceEntitiesSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeExperienceResponseTypeDef = TypedDict(
    "DescribeExperienceResponseTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "Name": str,
        "Endpoints": List[ExperienceEndpointTypeDef],
        "Configuration": ExperienceConfigurationOutputTypeDef,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Description": str,
        "Status": ExperienceStatusType,
        "RoleArn": str,
        "ErrorMessage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutPrincipalMappingRequestRequestTypeDef = TypedDict(
    "PutPrincipalMappingRequestRequestTypeDef",
    {
        "IndexId": str,
        "GroupId": str,
        "GroupMembers": GroupMembersTypeDef,
        "DataSourceId": NotRequired[str],
        "OrderingId": NotRequired[int],
        "RoleArn": NotRequired[str],
    },
)
AdditionalResultAttributeValueTypeDef = TypedDict(
    "AdditionalResultAttributeValueTypeDef",
    {
        "TextWithHighlightsValue": NotRequired[TextWithHighlightsTypeDef],
    },
)
ExpandedResultItemTypeDef = TypedDict(
    "ExpandedResultItemTypeDef",
    {
        "Id": NotRequired[str],
        "DocumentId": NotRequired[str],
        "DocumentTitle": NotRequired[TextWithHighlightsTypeDef],
        "DocumentExcerpt": NotRequired[TextWithHighlightsTypeDef],
        "DocumentURI": NotRequired[str],
        "DocumentAttributes": NotRequired[List[DocumentAttributeOutputTypeDef]],
    },
)
CreateIndexRequestRequestTypeDef = TypedDict(
    "CreateIndexRequestRequestTypeDef",
    {
        "Name": str,
        "RoleArn": str,
        "Edition": NotRequired[IndexEditionType],
        "ServerSideEncryptionConfiguration": NotRequired[ServerSideEncryptionConfigurationTypeDef],
        "Description": NotRequired[str],
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "UserTokenConfigurations": NotRequired[Sequence[UserTokenConfigurationTypeDef]],
        "UserContextPolicy": NotRequired[UserContextPolicyType],
        "UserGroupResolutionConfiguration": NotRequired[UserGroupResolutionConfigurationTypeDef],
    },
)
DescribeIndexResponseTypeDef = TypedDict(
    "DescribeIndexResponseTypeDef",
    {
        "Name": str,
        "Id": str,
        "Edition": IndexEditionType,
        "RoleArn": str,
        "ServerSideEncryptionConfiguration": ServerSideEncryptionConfigurationTypeDef,
        "Status": IndexStatusType,
        "Description": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "DocumentMetadataConfigurations": List[DocumentMetadataConfigurationOutputTypeDef],
        "IndexStatistics": IndexStatisticsTypeDef,
        "ErrorMessage": str,
        "CapacityUnits": CapacityUnitsConfigurationTypeDef,
        "UserTokenConfigurations": List[UserTokenConfigurationTypeDef],
        "UserContextPolicy": UserContextPolicyType,
        "UserGroupResolutionConfiguration": UserGroupResolutionConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DocumentMetadataConfigurationTypeDef = TypedDict(
    "DocumentMetadataConfigurationTypeDef",
    {
        "Name": str,
        "Type": DocumentAttributeValueTypeType,
        "Relevance": NotRequired[RelevanceUnionTypeDef],
        "Search": NotRequired[SearchTypeDef],
    },
)
DocumentRelevanceConfigurationTypeDef = TypedDict(
    "DocumentRelevanceConfigurationTypeDef",
    {
        "Name": str,
        "Relevance": RelevanceUnionTypeDef,
    },
)
WebCrawlerConfigurationOutputTypeDef = TypedDict(
    "WebCrawlerConfigurationOutputTypeDef",
    {
        "Urls": UrlsOutputTypeDef,
        "CrawlDepth": NotRequired[int],
        "MaxLinksPerPage": NotRequired[int],
        "MaxContentSizePerPageInMegaBytes": NotRequired[float],
        "MaxUrlsPerMinuteCrawlRate": NotRequired[int],
        "UrlInclusionPatterns": NotRequired[List[str]],
        "UrlExclusionPatterns": NotRequired[List[str]],
        "ProxyConfiguration": NotRequired[ProxyConfigurationTypeDef],
        "AuthenticationConfiguration": NotRequired[AuthenticationConfigurationOutputTypeDef],
    },
)
UrlsTypeDef = TypedDict(
    "UrlsTypeDef",
    {
        "SeedUrlConfiguration": NotRequired[SeedUrlConfigurationUnionTypeDef],
        "SiteMapsConfiguration": NotRequired[SiteMapsConfigurationUnionTypeDef],
    },
)
SuggestionValueTypeDef = TypedDict(
    "SuggestionValueTypeDef",
    {
        "Text": NotRequired[SuggestionTextWithHighlightsTypeDef],
    },
)
TableExcerptTypeDef = TypedDict(
    "TableExcerptTypeDef",
    {
        "Rows": NotRequired[List[TableRowTypeDef]],
        "TotalNumberOfRows": NotRequired[int],
    },
)
DatabaseConfigurationTypeDef = TypedDict(
    "DatabaseConfigurationTypeDef",
    {
        "DatabaseEngineType": DatabaseEngineTypeType,
        "ConnectionConfiguration": ConnectionConfigurationTypeDef,
        "ColumnConfiguration": ColumnConfigurationUnionTypeDef,
        "VpcConfiguration": NotRequired[DataSourceVpcConfigurationUnionTypeDef],
        "AclConfiguration": NotRequired[AclConfigurationTypeDef],
        "SqlConfiguration": NotRequired[SqlConfigurationTypeDef],
    },
)
SalesforceConfigurationOutputTypeDef = TypedDict(
    "SalesforceConfigurationOutputTypeDef",
    {
        "ServerUrl": str,
        "SecretArn": str,
        "StandardObjectConfigurations": NotRequired[
            List[SalesforceStandardObjectConfigurationOutputTypeDef]
        ],
        "KnowledgeArticleConfiguration": NotRequired[
            SalesforceKnowledgeArticleConfigurationOutputTypeDef
        ],
        "ChatterFeedConfiguration": NotRequired[SalesforceChatterFeedConfigurationOutputTypeDef],
        "CrawlAttachments": NotRequired[bool],
        "StandardObjectAttachmentConfiguration": NotRequired[
            SalesforceStandardObjectAttachmentConfigurationOutputTypeDef
        ],
        "IncludeAttachmentFilePatterns": NotRequired[List[str]],
        "ExcludeAttachmentFilePatterns": NotRequired[List[str]],
    },
)
SalesforceKnowledgeArticleConfigurationTypeDef = TypedDict(
    "SalesforceKnowledgeArticleConfigurationTypeDef",
    {
        "IncludedStates": Sequence[SalesforceKnowledgeArticleStateType],
        "StandardKnowledgeArticleTypeConfiguration": NotRequired[
            SalesforceStandardKnowledgeArticleTypeConfigurationUnionTypeDef
        ],
        "CustomKnowledgeArticleTypeConfigurations": NotRequired[
            Sequence[SalesforceCustomKnowledgeArticleTypeConfigurationUnionTypeDef]
        ],
    },
)
ServiceNowConfigurationTypeDef = TypedDict(
    "ServiceNowConfigurationTypeDef",
    {
        "HostUrl": str,
        "SecretArn": str,
        "ServiceNowBuildVersion": ServiceNowBuildVersionTypeType,
        "KnowledgeArticleConfiguration": NotRequired[
            ServiceNowKnowledgeArticleConfigurationUnionTypeDef
        ],
        "ServiceCatalogConfiguration": NotRequired[
            ServiceNowServiceCatalogConfigurationUnionTypeDef
        ],
        "AuthenticationType": NotRequired[ServiceNowAuthenticationTypeType],
    },
)
OneDriveConfigurationTypeDef = TypedDict(
    "OneDriveConfigurationTypeDef",
    {
        "TenantDomain": str,
        "SecretArn": str,
        "OneDriveUsers": OneDriveUsersUnionTypeDef,
        "InclusionPatterns": NotRequired[Sequence[str]],
        "ExclusionPatterns": NotRequired[Sequence[str]],
        "FieldMappings": NotRequired[Sequence[DataSourceToIndexFieldMappingTypeDef]],
        "DisableLocalGroups": NotRequired[bool],
    },
)
DocumentAttributeConditionTypeDef = TypedDict(
    "DocumentAttributeConditionTypeDef",
    {
        "ConditionDocumentAttributeKey": str,
        "Operator": ConditionOperatorType,
        "ConditionOnValue": NotRequired[DocumentAttributeValueUnionTypeDef],
    },
)
DocumentAttributeTargetTypeDef = TypedDict(
    "DocumentAttributeTargetTypeDef",
    {
        "TargetDocumentAttributeKey": NotRequired[str],
        "TargetDocumentAttributeValueDeletion": NotRequired[bool],
        "TargetDocumentAttributeValue": NotRequired[DocumentAttributeValueUnionTypeDef],
    },
)
DocumentAttributeTypeDef = TypedDict(
    "DocumentAttributeTypeDef",
    {
        "Key": str,
        "Value": DocumentAttributeValueUnionTypeDef,
    },
)
ConfluenceConfigurationTypeDef = TypedDict(
    "ConfluenceConfigurationTypeDef",
    {
        "ServerUrl": str,
        "SecretArn": str,
        "Version": ConfluenceVersionType,
        "SpaceConfiguration": NotRequired[ConfluenceSpaceConfigurationUnionTypeDef],
        "PageConfiguration": NotRequired[ConfluencePageConfigurationUnionTypeDef],
        "BlogConfiguration": NotRequired[ConfluenceBlogConfigurationUnionTypeDef],
        "AttachmentConfiguration": NotRequired[ConfluenceAttachmentConfigurationUnionTypeDef],
        "VpcConfiguration": NotRequired[DataSourceVpcConfigurationUnionTypeDef],
        "InclusionPatterns": NotRequired[Sequence[str]],
        "ExclusionPatterns": NotRequired[Sequence[str]],
        "ProxyConfiguration": NotRequired[ProxyConfigurationTypeDef],
        "AuthenticationType": NotRequired[ConfluenceAuthenticationTypeType],
    },
)
CreateExperienceRequestRequestTypeDef = TypedDict(
    "CreateExperienceRequestRequestTypeDef",
    {
        "Name": str,
        "IndexId": str,
        "RoleArn": NotRequired[str],
        "Configuration": NotRequired[ExperienceConfigurationTypeDef],
        "Description": NotRequired[str],
        "ClientToken": NotRequired[str],
    },
)
UpdateExperienceRequestRequestTypeDef = TypedDict(
    "UpdateExperienceRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "Name": NotRequired[str],
        "RoleArn": NotRequired[str],
        "Configuration": NotRequired[ExperienceConfigurationTypeDef],
        "Description": NotRequired[str],
    },
)
CreateAccessControlConfigurationRequestRequestTypeDef = TypedDict(
    "CreateAccessControlConfigurationRequestRequestTypeDef",
    {
        "IndexId": str,
        "Name": str,
        "Description": NotRequired[str],
        "AccessControlList": NotRequired[Sequence[PrincipalTypeDef]],
        "HierarchicalAccessControlList": NotRequired[Sequence[HierarchicalPrincipalUnionTypeDef]],
        "ClientToken": NotRequired[str],
    },
)
AlfrescoConfigurationUnionTypeDef = Union[
    AlfrescoConfigurationTypeDef, AlfrescoConfigurationOutputTypeDef
]
BoxConfigurationUnionTypeDef = Union[BoxConfigurationTypeDef, BoxConfigurationOutputTypeDef]
FsxConfigurationUnionTypeDef = Union[FsxConfigurationTypeDef, FsxConfigurationOutputTypeDef]
GitHubConfigurationUnionTypeDef = Union[
    GitHubConfigurationTypeDef, GitHubConfigurationOutputTypeDef
]
JiraConfigurationUnionTypeDef = Union[JiraConfigurationTypeDef, JiraConfigurationOutputTypeDef]
QuipConfigurationUnionTypeDef = Union[QuipConfigurationTypeDef, QuipConfigurationOutputTypeDef]
SharePointConfigurationUnionTypeDef = Union[
    SharePointConfigurationTypeDef, SharePointConfigurationOutputTypeDef
]
SlackConfigurationUnionTypeDef = Union[SlackConfigurationTypeDef, SlackConfigurationOutputTypeDef]
RetrieveResultTypeDef = TypedDict(
    "RetrieveResultTypeDef",
    {
        "QueryId": str,
        "ResultItems": List[RetrieveResultItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CustomDocumentEnrichmentConfigurationOutputTypeDef = TypedDict(
    "CustomDocumentEnrichmentConfigurationOutputTypeDef",
    {
        "InlineConfigurations": NotRequired[
            List[InlineCustomDocumentEnrichmentConfigurationOutputTypeDef]
        ],
        "PreExtractionHookConfiguration": NotRequired[HookConfigurationOutputTypeDef],
        "PostExtractionHookConfiguration": NotRequired[HookConfigurationOutputTypeDef],
        "RoleArn": NotRequired[str],
    },
)
AdditionalResultAttributeTypeDef = TypedDict(
    "AdditionalResultAttributeTypeDef",
    {
        "Key": str,
        "ValueType": Literal["TEXT_WITH_HIGHLIGHTS_VALUE"],
        "Value": AdditionalResultAttributeValueTypeDef,
    },
)
CollapsedResultDetailTypeDef = TypedDict(
    "CollapsedResultDetailTypeDef",
    {
        "DocumentAttribute": DocumentAttributeOutputTypeDef,
        "ExpandedResults": NotRequired[List[ExpandedResultItemTypeDef]],
    },
)
DocumentMetadataConfigurationUnionTypeDef = Union[
    DocumentMetadataConfigurationTypeDef, DocumentMetadataConfigurationOutputTypeDef
]
UrlsUnionTypeDef = Union[UrlsTypeDef, UrlsOutputTypeDef]
SuggestionTypeDef = TypedDict(
    "SuggestionTypeDef",
    {
        "Id": NotRequired[str],
        "Value": NotRequired[SuggestionValueTypeDef],
        "SourceDocuments": NotRequired[List[SourceDocumentTypeDef]],
    },
)
DatabaseConfigurationUnionTypeDef = Union[
    DatabaseConfigurationTypeDef, DatabaseConfigurationOutputTypeDef
]
DataSourceConfigurationOutputTypeDef = TypedDict(
    "DataSourceConfigurationOutputTypeDef",
    {
        "S3Configuration": NotRequired[S3DataSourceConfigurationOutputTypeDef],
        "SharePointConfiguration": NotRequired[SharePointConfigurationOutputTypeDef],
        "DatabaseConfiguration": NotRequired[DatabaseConfigurationOutputTypeDef],
        "SalesforceConfiguration": NotRequired[SalesforceConfigurationOutputTypeDef],
        "OneDriveConfiguration": NotRequired[OneDriveConfigurationOutputTypeDef],
        "ServiceNowConfiguration": NotRequired[ServiceNowConfigurationOutputTypeDef],
        "ConfluenceConfiguration": NotRequired[ConfluenceConfigurationOutputTypeDef],
        "GoogleDriveConfiguration": NotRequired[GoogleDriveConfigurationOutputTypeDef],
        "WebCrawlerConfiguration": NotRequired[WebCrawlerConfigurationOutputTypeDef],
        "WorkDocsConfiguration": NotRequired[WorkDocsConfigurationOutputTypeDef],
        "FsxConfiguration": NotRequired[FsxConfigurationOutputTypeDef],
        "SlackConfiguration": NotRequired[SlackConfigurationOutputTypeDef],
        "BoxConfiguration": NotRequired[BoxConfigurationOutputTypeDef],
        "QuipConfiguration": NotRequired[QuipConfigurationOutputTypeDef],
        "JiraConfiguration": NotRequired[JiraConfigurationOutputTypeDef],
        "GitHubConfiguration": NotRequired[GitHubConfigurationOutputTypeDef],
        "AlfrescoConfiguration": NotRequired[AlfrescoConfigurationOutputTypeDef],
        "TemplateConfiguration": NotRequired[TemplateConfigurationOutputTypeDef],
    },
)
SalesforceKnowledgeArticleConfigurationUnionTypeDef = Union[
    SalesforceKnowledgeArticleConfigurationTypeDef,
    SalesforceKnowledgeArticleConfigurationOutputTypeDef,
]
ServiceNowConfigurationUnionTypeDef = Union[
    ServiceNowConfigurationTypeDef, ServiceNowConfigurationOutputTypeDef
]
OneDriveConfigurationUnionTypeDef = Union[
    OneDriveConfigurationTypeDef, OneDriveConfigurationOutputTypeDef
]
DocumentAttributeConditionUnionTypeDef = Union[
    DocumentAttributeConditionTypeDef, DocumentAttributeConditionOutputTypeDef
]
DocumentAttributeTargetUnionTypeDef = Union[
    DocumentAttributeTargetTypeDef, DocumentAttributeTargetOutputTypeDef
]
DocumentAttributeUnionTypeDef = Union[DocumentAttributeTypeDef, DocumentAttributeOutputTypeDef]
ConfluenceConfigurationUnionTypeDef = Union[
    ConfluenceConfigurationTypeDef, ConfluenceConfigurationOutputTypeDef
]
FeaturedResultsItemTypeDef = TypedDict(
    "FeaturedResultsItemTypeDef",
    {
        "Id": NotRequired[str],
        "Type": NotRequired[QueryResultTypeType],
        "AdditionalAttributes": NotRequired[List[AdditionalResultAttributeTypeDef]],
        "DocumentId": NotRequired[str],
        "DocumentTitle": NotRequired[TextWithHighlightsTypeDef],
        "DocumentExcerpt": NotRequired[TextWithHighlightsTypeDef],
        "DocumentURI": NotRequired[str],
        "DocumentAttributes": NotRequired[List[DocumentAttributeOutputTypeDef]],
        "FeedbackToken": NotRequired[str],
    },
)
QueryResultItemTypeDef = TypedDict(
    "QueryResultItemTypeDef",
    {
        "Id": NotRequired[str],
        "Type": NotRequired[QueryResultTypeType],
        "Format": NotRequired[QueryResultFormatType],
        "AdditionalAttributes": NotRequired[List[AdditionalResultAttributeTypeDef]],
        "DocumentId": NotRequired[str],
        "DocumentTitle": NotRequired[TextWithHighlightsTypeDef],
        "DocumentExcerpt": NotRequired[TextWithHighlightsTypeDef],
        "DocumentURI": NotRequired[str],
        "DocumentAttributes": NotRequired[List[DocumentAttributeOutputTypeDef]],
        "ScoreAttributes": NotRequired[ScoreAttributesTypeDef],
        "FeedbackToken": NotRequired[str],
        "TableExcerpt": NotRequired[TableExcerptTypeDef],
        "CollapsedResultDetail": NotRequired[CollapsedResultDetailTypeDef],
    },
)
UpdateIndexRequestRequestTypeDef = TypedDict(
    "UpdateIndexRequestRequestTypeDef",
    {
        "Id": str,
        "Name": NotRequired[str],
        "RoleArn": NotRequired[str],
        "Description": NotRequired[str],
        "DocumentMetadataConfigurationUpdates": NotRequired[
            Sequence[DocumentMetadataConfigurationUnionTypeDef]
        ],
        "CapacityUnits": NotRequired[CapacityUnitsConfigurationTypeDef],
        "UserTokenConfigurations": NotRequired[Sequence[UserTokenConfigurationTypeDef]],
        "UserContextPolicy": NotRequired[UserContextPolicyType],
        "UserGroupResolutionConfiguration": NotRequired[UserGroupResolutionConfigurationTypeDef],
    },
)
WebCrawlerConfigurationTypeDef = TypedDict(
    "WebCrawlerConfigurationTypeDef",
    {
        "Urls": UrlsUnionTypeDef,
        "CrawlDepth": NotRequired[int],
        "MaxLinksPerPage": NotRequired[int],
        "MaxContentSizePerPageInMegaBytes": NotRequired[float],
        "MaxUrlsPerMinuteCrawlRate": NotRequired[int],
        "UrlInclusionPatterns": NotRequired[Sequence[str]],
        "UrlExclusionPatterns": NotRequired[Sequence[str]],
        "ProxyConfiguration": NotRequired[ProxyConfigurationTypeDef],
        "AuthenticationConfiguration": NotRequired[AuthenticationConfigurationUnionTypeDef],
    },
)
GetQuerySuggestionsResponseTypeDef = TypedDict(
    "GetQuerySuggestionsResponseTypeDef",
    {
        "QuerySuggestionsId": str,
        "Suggestions": List[SuggestionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDataSourceResponseTypeDef = TypedDict(
    "DescribeDataSourceResponseTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "Name": str,
        "Type": DataSourceTypeType,
        "Configuration": DataSourceConfigurationOutputTypeDef,
        "VpcConfiguration": DataSourceVpcConfigurationOutputTypeDef,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Description": str,
        "Status": DataSourceStatusType,
        "Schedule": str,
        "RoleArn": str,
        "ErrorMessage": str,
        "LanguageCode": str,
        "CustomDocumentEnrichmentConfiguration": CustomDocumentEnrichmentConfigurationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SalesforceConfigurationTypeDef = TypedDict(
    "SalesforceConfigurationTypeDef",
    {
        "ServerUrl": str,
        "SecretArn": str,
        "StandardObjectConfigurations": NotRequired[
            Sequence[SalesforceStandardObjectConfigurationUnionTypeDef]
        ],
        "KnowledgeArticleConfiguration": NotRequired[
            SalesforceKnowledgeArticleConfigurationUnionTypeDef
        ],
        "ChatterFeedConfiguration": NotRequired[SalesforceChatterFeedConfigurationUnionTypeDef],
        "CrawlAttachments": NotRequired[bool],
        "StandardObjectAttachmentConfiguration": NotRequired[
            SalesforceStandardObjectAttachmentConfigurationUnionTypeDef
        ],
        "IncludeAttachmentFilePatterns": NotRequired[Sequence[str]],
        "ExcludeAttachmentFilePatterns": NotRequired[Sequence[str]],
    },
)
HookConfigurationTypeDef = TypedDict(
    "HookConfigurationTypeDef",
    {
        "LambdaArn": str,
        "S3Bucket": str,
        "InvocationCondition": NotRequired[DocumentAttributeConditionUnionTypeDef],
    },
)
InlineCustomDocumentEnrichmentConfigurationTypeDef = TypedDict(
    "InlineCustomDocumentEnrichmentConfigurationTypeDef",
    {
        "Condition": NotRequired[DocumentAttributeConditionUnionTypeDef],
        "Target": NotRequired[DocumentAttributeTargetUnionTypeDef],
        "DocumentContentDeletion": NotRequired[bool],
    },
)
AttributeFilterTypeDef = TypedDict(
    "AttributeFilterTypeDef",
    {
        "AndAllFilters": NotRequired[Sequence[Mapping[str, Any]]],
        "OrAllFilters": NotRequired[Sequence[Mapping[str, Any]]],
        "NotFilter": NotRequired[Mapping[str, Any]],
        "EqualsTo": NotRequired[DocumentAttributeUnionTypeDef],
        "ContainsAll": NotRequired[DocumentAttributeUnionTypeDef],
        "ContainsAny": NotRequired[DocumentAttributeUnionTypeDef],
        "GreaterThan": NotRequired[DocumentAttributeUnionTypeDef],
        "GreaterThanOrEquals": NotRequired[DocumentAttributeUnionTypeDef],
        "LessThan": NotRequired[DocumentAttributeUnionTypeDef],
        "LessThanOrEquals": NotRequired[DocumentAttributeUnionTypeDef],
    },
)
DocumentInfoTypeDef = TypedDict(
    "DocumentInfoTypeDef",
    {
        "DocumentId": str,
        "Attributes": NotRequired[Sequence[DocumentAttributeUnionTypeDef]],
    },
)
DocumentTypeDef = TypedDict(
    "DocumentTypeDef",
    {
        "Id": str,
        "Title": NotRequired[str],
        "Blob": NotRequired[BlobTypeDef],
        "S3Path": NotRequired[S3PathTypeDef],
        "Attributes": NotRequired[Sequence[DocumentAttributeUnionTypeDef]],
        "AccessControlList": NotRequired[Sequence[PrincipalTypeDef]],
        "HierarchicalAccessControlList": NotRequired[Sequence[HierarchicalPrincipalUnionTypeDef]],
        "ContentType": NotRequired[ContentTypeType],
        "AccessControlConfigurationId": NotRequired[str],
    },
)
QueryResultTypeDef = TypedDict(
    "QueryResultTypeDef",
    {
        "QueryId": str,
        "ResultItems": List[QueryResultItemTypeDef],
        "FacetResults": List[FacetResultTypeDef],
        "TotalNumberOfResults": int,
        "Warnings": List[WarningTypeDef],
        "SpellCorrectedQueries": List[SpellCorrectedQueryTypeDef],
        "FeaturedResultsItems": List[FeaturedResultsItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
WebCrawlerConfigurationUnionTypeDef = Union[
    WebCrawlerConfigurationTypeDef, WebCrawlerConfigurationOutputTypeDef
]
SalesforceConfigurationUnionTypeDef = Union[
    SalesforceConfigurationTypeDef, SalesforceConfigurationOutputTypeDef
]
HookConfigurationUnionTypeDef = Union[HookConfigurationTypeDef, HookConfigurationOutputTypeDef]
InlineCustomDocumentEnrichmentConfigurationUnionTypeDef = Union[
    InlineCustomDocumentEnrichmentConfigurationTypeDef,
    InlineCustomDocumentEnrichmentConfigurationOutputTypeDef,
]
AttributeSuggestionsGetConfigTypeDef = TypedDict(
    "AttributeSuggestionsGetConfigTypeDef",
    {
        "SuggestionAttributes": NotRequired[Sequence[str]],
        "AdditionalResponseAttributes": NotRequired[Sequence[str]],
        "AttributeFilter": NotRequired[AttributeFilterTypeDef],
        "UserContext": NotRequired[UserContextTypeDef],
    },
)
QueryRequestRequestTypeDef = TypedDict(
    "QueryRequestRequestTypeDef",
    {
        "IndexId": str,
        "QueryText": NotRequired[str],
        "AttributeFilter": NotRequired[AttributeFilterTypeDef],
        "Facets": NotRequired[Sequence[FacetTypeDef]],
        "RequestedDocumentAttributes": NotRequired[Sequence[str]],
        "QueryResultTypeFilter": NotRequired[QueryResultTypeType],
        "DocumentRelevanceOverrideConfigurations": NotRequired[
            Sequence[DocumentRelevanceConfigurationTypeDef]
        ],
        "PageNumber": NotRequired[int],
        "PageSize": NotRequired[int],
        "SortingConfiguration": NotRequired[SortingConfigurationTypeDef],
        "SortingConfigurations": NotRequired[Sequence[SortingConfigurationTypeDef]],
        "UserContext": NotRequired[UserContextTypeDef],
        "VisitorId": NotRequired[str],
        "SpellCorrectionConfiguration": NotRequired[SpellCorrectionConfigurationTypeDef],
        "CollapseConfiguration": NotRequired[CollapseConfigurationTypeDef],
    },
)
RetrieveRequestRequestTypeDef = TypedDict(
    "RetrieveRequestRequestTypeDef",
    {
        "IndexId": str,
        "QueryText": str,
        "AttributeFilter": NotRequired[AttributeFilterTypeDef],
        "RequestedDocumentAttributes": NotRequired[Sequence[str]],
        "DocumentRelevanceOverrideConfigurations": NotRequired[
            Sequence[DocumentRelevanceConfigurationTypeDef]
        ],
        "PageNumber": NotRequired[int],
        "PageSize": NotRequired[int],
        "UserContext": NotRequired[UserContextTypeDef],
    },
)
BatchGetDocumentStatusRequestRequestTypeDef = TypedDict(
    "BatchGetDocumentStatusRequestRequestTypeDef",
    {
        "IndexId": str,
        "DocumentInfoList": Sequence[DocumentInfoTypeDef],
    },
)
DataSourceConfigurationTypeDef = TypedDict(
    "DataSourceConfigurationTypeDef",
    {
        "S3Configuration": NotRequired[S3DataSourceConfigurationUnionTypeDef],
        "SharePointConfiguration": NotRequired[SharePointConfigurationUnionTypeDef],
        "DatabaseConfiguration": NotRequired[DatabaseConfigurationUnionTypeDef],
        "SalesforceConfiguration": NotRequired[SalesforceConfigurationUnionTypeDef],
        "OneDriveConfiguration": NotRequired[OneDriveConfigurationUnionTypeDef],
        "ServiceNowConfiguration": NotRequired[ServiceNowConfigurationUnionTypeDef],
        "ConfluenceConfiguration": NotRequired[ConfluenceConfigurationUnionTypeDef],
        "GoogleDriveConfiguration": NotRequired[GoogleDriveConfigurationUnionTypeDef],
        "WebCrawlerConfiguration": NotRequired[WebCrawlerConfigurationUnionTypeDef],
        "WorkDocsConfiguration": NotRequired[WorkDocsConfigurationUnionTypeDef],
        "FsxConfiguration": NotRequired[FsxConfigurationUnionTypeDef],
        "SlackConfiguration": NotRequired[SlackConfigurationUnionTypeDef],
        "BoxConfiguration": NotRequired[BoxConfigurationUnionTypeDef],
        "QuipConfiguration": NotRequired[QuipConfigurationUnionTypeDef],
        "JiraConfiguration": NotRequired[JiraConfigurationUnionTypeDef],
        "GitHubConfiguration": NotRequired[GitHubConfigurationUnionTypeDef],
        "AlfrescoConfiguration": NotRequired[AlfrescoConfigurationUnionTypeDef],
        "TemplateConfiguration": NotRequired[TemplateConfigurationUnionTypeDef],
    },
)
CustomDocumentEnrichmentConfigurationTypeDef = TypedDict(
    "CustomDocumentEnrichmentConfigurationTypeDef",
    {
        "InlineConfigurations": NotRequired[
            Sequence[InlineCustomDocumentEnrichmentConfigurationUnionTypeDef]
        ],
        "PreExtractionHookConfiguration": NotRequired[HookConfigurationUnionTypeDef],
        "PostExtractionHookConfiguration": NotRequired[HookConfigurationUnionTypeDef],
        "RoleArn": NotRequired[str],
    },
)
GetQuerySuggestionsRequestRequestTypeDef = TypedDict(
    "GetQuerySuggestionsRequestRequestTypeDef",
    {
        "IndexId": str,
        "QueryText": str,
        "MaxSuggestionsCount": NotRequired[int],
        "SuggestionTypes": NotRequired[Sequence[SuggestionTypeType]],
        "AttributeSuggestionsConfig": NotRequired[AttributeSuggestionsGetConfigTypeDef],
    },
)
BatchPutDocumentRequestRequestTypeDef = TypedDict(
    "BatchPutDocumentRequestRequestTypeDef",
    {
        "IndexId": str,
        "Documents": Sequence[DocumentTypeDef],
        "RoleArn": NotRequired[str],
        "CustomDocumentEnrichmentConfiguration": NotRequired[
            CustomDocumentEnrichmentConfigurationTypeDef
        ],
    },
)
CreateDataSourceRequestRequestTypeDef = TypedDict(
    "CreateDataSourceRequestRequestTypeDef",
    {
        "Name": str,
        "IndexId": str,
        "Type": DataSourceTypeType,
        "Configuration": NotRequired[DataSourceConfigurationTypeDef],
        "VpcConfiguration": NotRequired[DataSourceVpcConfigurationTypeDef],
        "Description": NotRequired[str],
        "Schedule": NotRequired[str],
        "RoleArn": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ClientToken": NotRequired[str],
        "LanguageCode": NotRequired[str],
        "CustomDocumentEnrichmentConfiguration": NotRequired[
            CustomDocumentEnrichmentConfigurationTypeDef
        ],
    },
)
UpdateDataSourceRequestRequestTypeDef = TypedDict(
    "UpdateDataSourceRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "Name": NotRequired[str],
        "Configuration": NotRequired[DataSourceConfigurationTypeDef],
        "VpcConfiguration": NotRequired[DataSourceVpcConfigurationTypeDef],
        "Description": NotRequired[str],
        "Schedule": NotRequired[str],
        "RoleArn": NotRequired[str],
        "LanguageCode": NotRequired[str],
        "CustomDocumentEnrichmentConfiguration": NotRequired[
            CustomDocumentEnrichmentConfigurationTypeDef
        ],
    },
)
