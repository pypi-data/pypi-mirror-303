"""
Type annotations for config service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_config/type_defs/)

Usage::

    ```python
    from mypy_boto3_config.type_defs import AccountAggregationSourceOutputTypeDef

    data: AccountAggregationSourceOutputTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AggregateConformancePackComplianceSummaryGroupKeyType,
    AggregatedSourceStatusTypeType,
    AggregatedSourceTypeType,
    ChronologicalOrderType,
    ComplianceTypeType,
    ConfigRuleComplianceSummaryGroupKeyType,
    ConfigRuleStateType,
    ConfigurationItemStatusType,
    ConformancePackComplianceTypeType,
    ConformancePackStateType,
    DeliveryStatusType,
    EvaluationModeType,
    MaximumExecutionFrequencyType,
    MemberAccountRuleStatusType,
    MessageTypeType,
    OrganizationConfigRuleTriggerTypeNoSNType,
    OrganizationConfigRuleTriggerTypeType,
    OrganizationResourceDetailedStatusType,
    OrganizationResourceStatusType,
    OrganizationRuleStatusType,
    OwnerType,
    RecorderStatusType,
    RecordingFrequencyType,
    RecordingStrategyTypeType,
    RemediationExecutionStateType,
    RemediationExecutionStepStateType,
    ResourceCountGroupKeyType,
    ResourceEvaluationStatusType,
    ResourceTypeType,
    SortOrderType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AccountAggregationSourceOutputTypeDef",
    "AccountAggregationSourceTypeDef",
    "AggregateConformancePackComplianceTypeDef",
    "AggregateConformancePackComplianceCountTypeDef",
    "AggregateConformancePackComplianceFiltersTypeDef",
    "AggregateConformancePackComplianceSummaryFiltersTypeDef",
    "AggregateResourceIdentifierTypeDef",
    "AggregatedSourceStatusTypeDef",
    "AggregationAuthorizationTypeDef",
    "BaseConfigurationItemTypeDef",
    "ResponseMetadataTypeDef",
    "ResourceKeyTypeDef",
    "ComplianceContributorCountTypeDef",
    "ConfigExportDeliveryInfoTypeDef",
    "ConfigRuleComplianceFiltersTypeDef",
    "ConfigRuleComplianceSummaryFiltersTypeDef",
    "ConfigRuleEvaluationStatusTypeDef",
    "EvaluationModeConfigurationTypeDef",
    "ScopeOutputTypeDef",
    "ConfigSnapshotDeliveryPropertiesTypeDef",
    "ConfigStreamDeliveryInfoTypeDef",
    "OrganizationAggregationSourceOutputTypeDef",
    "RelationshipTypeDef",
    "ConfigurationRecorderStatusTypeDef",
    "ConformancePackComplianceFiltersTypeDef",
    "ConformancePackComplianceScoreTypeDef",
    "ConformancePackComplianceScoresFiltersTypeDef",
    "ConformancePackComplianceSummaryTypeDef",
    "ConformancePackInputParameterTypeDef",
    "TemplateSSMDocumentDetailsTypeDef",
    "ConformancePackEvaluationFiltersTypeDef",
    "ConformancePackRuleComplianceTypeDef",
    "ConformancePackStatusDetailTypeDef",
    "CustomPolicyDetailsTypeDef",
    "DeleteAggregationAuthorizationRequestRequestTypeDef",
    "DeleteConfigRuleRequestRequestTypeDef",
    "DeleteConfigurationAggregatorRequestRequestTypeDef",
    "DeleteConfigurationRecorderRequestRequestTypeDef",
    "DeleteConformancePackRequestRequestTypeDef",
    "DeleteDeliveryChannelRequestRequestTypeDef",
    "DeleteEvaluationResultsRequestRequestTypeDef",
    "DeleteOrganizationConfigRuleRequestRequestTypeDef",
    "DeleteOrganizationConformancePackRequestRequestTypeDef",
    "DeletePendingAggregationRequestRequestRequestTypeDef",
    "DeleteRemediationConfigurationRequestRequestTypeDef",
    "RemediationExceptionResourceKeyTypeDef",
    "DeleteResourceConfigRequestRequestTypeDef",
    "DeleteRetentionConfigurationRequestRequestTypeDef",
    "DeleteStoredQueryRequestRequestTypeDef",
    "DeliverConfigSnapshotRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeAggregationAuthorizationsRequestRequestTypeDef",
    "DescribeComplianceByConfigRuleRequestRequestTypeDef",
    "DescribeComplianceByResourceRequestRequestTypeDef",
    "DescribeConfigRuleEvaluationStatusRequestRequestTypeDef",
    "DescribeConfigRulesFiltersTypeDef",
    "DescribeConfigurationAggregatorSourcesStatusRequestRequestTypeDef",
    "DescribeConfigurationAggregatorsRequestRequestTypeDef",
    "DescribeConfigurationRecorderStatusRequestRequestTypeDef",
    "DescribeConfigurationRecordersRequestRequestTypeDef",
    "DescribeConformancePackStatusRequestRequestTypeDef",
    "DescribeConformancePacksRequestRequestTypeDef",
    "DescribeDeliveryChannelStatusRequestRequestTypeDef",
    "DescribeDeliveryChannelsRequestRequestTypeDef",
    "DescribeOrganizationConfigRuleStatusesRequestRequestTypeDef",
    "OrganizationConfigRuleStatusTypeDef",
    "DescribeOrganizationConfigRulesRequestRequestTypeDef",
    "DescribeOrganizationConformancePackStatusesRequestRequestTypeDef",
    "OrganizationConformancePackStatusTypeDef",
    "DescribeOrganizationConformancePacksRequestRequestTypeDef",
    "DescribePendingAggregationRequestsRequestRequestTypeDef",
    "PendingAggregationRequestTypeDef",
    "DescribeRemediationConfigurationsRequestRequestTypeDef",
    "RemediationExceptionTypeDef",
    "DescribeRetentionConfigurationsRequestRequestTypeDef",
    "RetentionConfigurationTypeDef",
    "EvaluationContextTypeDef",
    "EvaluationOutputTypeDef",
    "EvaluationResultQualifierTypeDef",
    "EvaluationStatusTypeDef",
    "TimestampTypeDef",
    "ExclusionByResourceTypesOutputTypeDef",
    "ExclusionByResourceTypesTypeDef",
    "SsmControlsTypeDef",
    "FieldInfoTypeDef",
    "GetAggregateComplianceDetailsByConfigRuleRequestRequestTypeDef",
    "ResourceCountFiltersTypeDef",
    "GroupedResourceCountTypeDef",
    "GetComplianceDetailsByConfigRuleRequestRequestTypeDef",
    "GetComplianceDetailsByResourceRequestRequestTypeDef",
    "GetComplianceSummaryByResourceTypeRequestRequestTypeDef",
    "GetConformancePackComplianceSummaryRequestRequestTypeDef",
    "GetCustomRulePolicyRequestRequestTypeDef",
    "GetDiscoveredResourceCountsRequestRequestTypeDef",
    "ResourceCountTypeDef",
    "StatusDetailFiltersTypeDef",
    "MemberAccountStatusTypeDef",
    "OrganizationResourceDetailedStatusFiltersTypeDef",
    "OrganizationConformancePackDetailedStatusTypeDef",
    "GetOrganizationCustomRulePolicyRequestRequestTypeDef",
    "GetResourceEvaluationSummaryRequestRequestTypeDef",
    "ResourceDetailsTypeDef",
    "GetStoredQueryRequestRequestTypeDef",
    "StoredQueryTypeDef",
    "ResourceFiltersTypeDef",
    "ListDiscoveredResourcesRequestRequestTypeDef",
    "ResourceIdentifierTypeDef",
    "ResourceEvaluationTypeDef",
    "ListStoredQueriesRequestRequestTypeDef",
    "StoredQueryMetadataTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagTypeDef",
    "OrganizationAggregationSourceTypeDef",
    "OrganizationCustomPolicyRuleMetadataNoPolicyTypeDef",
    "OrganizationCustomRuleMetadataOutputTypeDef",
    "OrganizationManagedRuleMetadataOutputTypeDef",
    "OrganizationCustomPolicyRuleMetadataTypeDef",
    "OrganizationCustomRuleMetadataTypeDef",
    "OrganizationManagedRuleMetadataTypeDef",
    "PutResourceConfigRequestRequestTypeDef",
    "PutRetentionConfigurationRequestRequestTypeDef",
    "RecordingStrategyTypeDef",
    "RecordingModeOverrideOutputTypeDef",
    "RecordingModeOverrideTypeDef",
    "RemediationExecutionStepTypeDef",
    "ResourceValueTypeDef",
    "StaticValueOutputTypeDef",
    "ScopeTypeDef",
    "SelectAggregateResourceConfigRequestRequestTypeDef",
    "SelectResourceConfigRequestRequestTypeDef",
    "SourceDetailTypeDef",
    "StartConfigRulesEvaluationRequestRequestTypeDef",
    "StartConfigurationRecorderRequestRequestTypeDef",
    "StaticValueTypeDef",
    "StopConfigurationRecorderRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "AccountAggregationSourceUnionTypeDef",
    "AggregateComplianceByConformancePackTypeDef",
    "AggregateConformancePackComplianceSummaryTypeDef",
    "DescribeAggregateComplianceByConformancePacksRequestRequestTypeDef",
    "GetAggregateConformancePackComplianceSummaryRequestRequestTypeDef",
    "BatchGetAggregateResourceConfigRequestRequestTypeDef",
    "GetAggregateResourceConfigRequestRequestTypeDef",
    "BatchGetAggregateResourceConfigResponseTypeDef",
    "DeliverConfigSnapshotResponseTypeDef",
    "DescribeAggregationAuthorizationsResponseTypeDef",
    "DescribeConfigurationAggregatorSourcesStatusResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetCustomRulePolicyResponseTypeDef",
    "GetOrganizationCustomRulePolicyResponseTypeDef",
    "ListAggregateDiscoveredResourcesResponseTypeDef",
    "PutAggregationAuthorizationResponseTypeDef",
    "PutConformancePackResponseTypeDef",
    "PutOrganizationConfigRuleResponseTypeDef",
    "PutOrganizationConformancePackResponseTypeDef",
    "PutStoredQueryResponseTypeDef",
    "StartResourceEvaluationResponseTypeDef",
    "BatchGetResourceConfigRequestRequestTypeDef",
    "BatchGetResourceConfigResponseTypeDef",
    "DescribeRemediationExecutionStatusRequestRequestTypeDef",
    "StartRemediationExecutionRequestRequestTypeDef",
    "StartRemediationExecutionResponseTypeDef",
    "ComplianceSummaryTypeDef",
    "ComplianceTypeDef",
    "DescribeAggregateComplianceByConfigRulesRequestRequestTypeDef",
    "GetAggregateConfigRuleComplianceSummaryRequestRequestTypeDef",
    "DescribeConfigRuleEvaluationStatusResponseTypeDef",
    "DeliveryChannelTypeDef",
    "DeliveryChannelStatusTypeDef",
    "ConfigurationAggregatorTypeDef",
    "ConfigurationItemTypeDef",
    "DescribeConfigurationRecorderStatusResponseTypeDef",
    "DescribeConformancePackComplianceRequestRequestTypeDef",
    "ListConformancePackComplianceScoresResponseTypeDef",
    "ListConformancePackComplianceScoresRequestRequestTypeDef",
    "GetConformancePackComplianceSummaryResponseTypeDef",
    "OrganizationConformancePackTypeDef",
    "PutOrganizationConformancePackRequestRequestTypeDef",
    "ConformancePackDetailTypeDef",
    "PutConformancePackRequestRequestTypeDef",
    "GetConformancePackComplianceDetailsRequestRequestTypeDef",
    "DescribeConformancePackComplianceResponseTypeDef",
    "DescribeConformancePackStatusResponseTypeDef",
    "DeleteRemediationExceptionsRequestRequestTypeDef",
    "DescribeRemediationExceptionsRequestRequestTypeDef",
    "FailedDeleteRemediationExceptionsBatchTypeDef",
    "DescribeAggregateComplianceByConfigRulesRequestDescribeAggregateComplianceByConfigRulesPaginateTypeDef",
    "DescribeAggregateComplianceByConformancePacksRequestDescribeAggregateComplianceByConformancePacksPaginateTypeDef",
    "DescribeAggregationAuthorizationsRequestDescribeAggregationAuthorizationsPaginateTypeDef",
    "DescribeComplianceByConfigRuleRequestDescribeComplianceByConfigRulePaginateTypeDef",
    "DescribeComplianceByResourceRequestDescribeComplianceByResourcePaginateTypeDef",
    "DescribeConfigRuleEvaluationStatusRequestDescribeConfigRuleEvaluationStatusPaginateTypeDef",
    "DescribeConfigurationAggregatorSourcesStatusRequestDescribeConfigurationAggregatorSourcesStatusPaginateTypeDef",
    "DescribeConfigurationAggregatorsRequestDescribeConfigurationAggregatorsPaginateTypeDef",
    "DescribeConformancePackStatusRequestDescribeConformancePackStatusPaginateTypeDef",
    "DescribeConformancePacksRequestDescribeConformancePacksPaginateTypeDef",
    "DescribeOrganizationConfigRuleStatusesRequestDescribeOrganizationConfigRuleStatusesPaginateTypeDef",
    "DescribeOrganizationConfigRulesRequestDescribeOrganizationConfigRulesPaginateTypeDef",
    "DescribeOrganizationConformancePackStatusesRequestDescribeOrganizationConformancePackStatusesPaginateTypeDef",
    "DescribeOrganizationConformancePacksRequestDescribeOrganizationConformancePacksPaginateTypeDef",
    "DescribePendingAggregationRequestsRequestDescribePendingAggregationRequestsPaginateTypeDef",
    "DescribeRemediationExecutionStatusRequestDescribeRemediationExecutionStatusPaginateTypeDef",
    "DescribeRetentionConfigurationsRequestDescribeRetentionConfigurationsPaginateTypeDef",
    "GetAggregateComplianceDetailsByConfigRuleRequestGetAggregateComplianceDetailsByConfigRulePaginateTypeDef",
    "GetComplianceDetailsByConfigRuleRequestGetComplianceDetailsByConfigRulePaginateTypeDef",
    "GetComplianceDetailsByResourceRequestGetComplianceDetailsByResourcePaginateTypeDef",
    "GetConformancePackComplianceSummaryRequestGetConformancePackComplianceSummaryPaginateTypeDef",
    "ListDiscoveredResourcesRequestListDiscoveredResourcesPaginateTypeDef",
    "ListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    "SelectAggregateResourceConfigRequestSelectAggregateResourceConfigPaginateTypeDef",
    "SelectResourceConfigRequestSelectResourceConfigPaginateTypeDef",
    "DescribeConfigRulesRequestDescribeConfigRulesPaginateTypeDef",
    "DescribeConfigRulesRequestRequestTypeDef",
    "DescribeOrganizationConfigRuleStatusesResponseTypeDef",
    "DescribeOrganizationConformancePackStatusesResponseTypeDef",
    "DescribePendingAggregationRequestsResponseTypeDef",
    "DescribeRemediationExceptionsResponseTypeDef",
    "FailedRemediationExceptionBatchTypeDef",
    "DescribeRetentionConfigurationsResponseTypeDef",
    "PutRetentionConfigurationResponseTypeDef",
    "PutEvaluationsResponseTypeDef",
    "EvaluationResultIdentifierTypeDef",
    "EvaluationTypeDef",
    "ExternalEvaluationTypeDef",
    "GetResourceConfigHistoryRequestGetResourceConfigHistoryPaginateTypeDef",
    "GetResourceConfigHistoryRequestRequestTypeDef",
    "PutRemediationExceptionsRequestRequestTypeDef",
    "TimeWindowTypeDef",
    "ExclusionByResourceTypesUnionTypeDef",
    "ExecutionControlsTypeDef",
    "QueryInfoTypeDef",
    "GetAggregateDiscoveredResourceCountsRequestRequestTypeDef",
    "GetAggregateDiscoveredResourceCountsResponseTypeDef",
    "GetDiscoveredResourceCountsResponseTypeDef",
    "GetOrganizationConfigRuleDetailedStatusRequestGetOrganizationConfigRuleDetailedStatusPaginateTypeDef",
    "GetOrganizationConfigRuleDetailedStatusRequestRequestTypeDef",
    "GetOrganizationConfigRuleDetailedStatusResponseTypeDef",
    "GetOrganizationConformancePackDetailedStatusRequestGetOrganizationConformancePackDetailedStatusPaginateTypeDef",
    "GetOrganizationConformancePackDetailedStatusRequestRequestTypeDef",
    "GetOrganizationConformancePackDetailedStatusResponseTypeDef",
    "GetResourceEvaluationSummaryResponseTypeDef",
    "StartResourceEvaluationRequestRequestTypeDef",
    "GetStoredQueryResponseTypeDef",
    "ListAggregateDiscoveredResourcesRequestListAggregateDiscoveredResourcesPaginateTypeDef",
    "ListAggregateDiscoveredResourcesRequestRequestTypeDef",
    "ListDiscoveredResourcesResponseTypeDef",
    "ListResourceEvaluationsResponseTypeDef",
    "ListStoredQueriesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PutAggregationAuthorizationRequestRequestTypeDef",
    "PutStoredQueryRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "OrganizationConfigRuleTypeDef",
    "PutOrganizationConfigRuleRequestRequestTypeDef",
    "RecordingGroupOutputTypeDef",
    "RecordingModeOutputTypeDef",
    "RecordingModeOverrideUnionTypeDef",
    "RemediationExecutionStatusTypeDef",
    "RemediationParameterValueOutputTypeDef",
    "ScopeUnionTypeDef",
    "SourceOutputTypeDef",
    "SourceTypeDef",
    "StaticValueUnionTypeDef",
    "PutConfigurationAggregatorRequestRequestTypeDef",
    "DescribeAggregateComplianceByConformancePacksResponseTypeDef",
    "GetAggregateConformancePackComplianceSummaryResponseTypeDef",
    "AggregateComplianceCountTypeDef",
    "ComplianceSummaryByResourceTypeTypeDef",
    "GetComplianceSummaryByConfigRuleResponseTypeDef",
    "AggregateComplianceByConfigRuleTypeDef",
    "ComplianceByConfigRuleTypeDef",
    "ComplianceByResourceTypeDef",
    "DescribeDeliveryChannelsResponseTypeDef",
    "PutDeliveryChannelRequestRequestTypeDef",
    "DescribeDeliveryChannelStatusResponseTypeDef",
    "DescribeConfigurationAggregatorsResponseTypeDef",
    "PutConfigurationAggregatorResponseTypeDef",
    "GetAggregateResourceConfigResponseTypeDef",
    "GetResourceConfigHistoryResponseTypeDef",
    "DescribeOrganizationConformancePacksResponseTypeDef",
    "DescribeConformancePacksResponseTypeDef",
    "DeleteRemediationExceptionsResponseTypeDef",
    "PutRemediationExceptionsResponseTypeDef",
    "AggregateEvaluationResultTypeDef",
    "ConformancePackEvaluationResultTypeDef",
    "EvaluationResultTypeDef",
    "EvaluationUnionTypeDef",
    "PutExternalEvaluationRequestRequestTypeDef",
    "ResourceEvaluationFiltersTypeDef",
    "RecordingGroupTypeDef",
    "SelectAggregateResourceConfigResponseTypeDef",
    "SelectResourceConfigResponseTypeDef",
    "DescribeOrganizationConfigRulesResponseTypeDef",
    "ConfigurationRecorderOutputTypeDef",
    "RecordingModeTypeDef",
    "DescribeRemediationExecutionStatusResponseTypeDef",
    "RemediationConfigurationOutputTypeDef",
    "ConfigRuleOutputTypeDef",
    "SourceUnionTypeDef",
    "RemediationParameterValueTypeDef",
    "GetAggregateConfigRuleComplianceSummaryResponseTypeDef",
    "GetComplianceSummaryByResourceTypeResponseTypeDef",
    "DescribeAggregateComplianceByConfigRulesResponseTypeDef",
    "DescribeComplianceByConfigRuleResponseTypeDef",
    "DescribeComplianceByResourceResponseTypeDef",
    "GetAggregateComplianceDetailsByConfigRuleResponseTypeDef",
    "GetConformancePackComplianceDetailsResponseTypeDef",
    "GetComplianceDetailsByConfigRuleResponseTypeDef",
    "GetComplianceDetailsByResourceResponseTypeDef",
    "PutEvaluationsRequestRequestTypeDef",
    "ListResourceEvaluationsRequestListResourceEvaluationsPaginateTypeDef",
    "ListResourceEvaluationsRequestRequestTypeDef",
    "RecordingGroupUnionTypeDef",
    "DescribeConfigurationRecordersResponseTypeDef",
    "RecordingModeUnionTypeDef",
    "DescribeRemediationConfigurationsResponseTypeDef",
    "FailedRemediationBatchTypeDef",
    "DescribeConfigRulesResponseTypeDef",
    "ConfigRuleTypeDef",
    "RemediationParameterValueUnionTypeDef",
    "ConfigurationRecorderTypeDef",
    "PutRemediationConfigurationsResponseTypeDef",
    "PutConfigRuleRequestRequestTypeDef",
    "RemediationConfigurationTypeDef",
    "PutConfigurationRecorderRequestRequestTypeDef",
    "RemediationConfigurationUnionTypeDef",
    "PutRemediationConfigurationsRequestRequestTypeDef",
)

AccountAggregationSourceOutputTypeDef = TypedDict(
    "AccountAggregationSourceOutputTypeDef",
    {
        "AccountIds": List[str],
        "AllAwsRegions": NotRequired[bool],
        "AwsRegions": NotRequired[List[str]],
    },
)
AccountAggregationSourceTypeDef = TypedDict(
    "AccountAggregationSourceTypeDef",
    {
        "AccountIds": Sequence[str],
        "AllAwsRegions": NotRequired[bool],
        "AwsRegions": NotRequired[Sequence[str]],
    },
)
AggregateConformancePackComplianceTypeDef = TypedDict(
    "AggregateConformancePackComplianceTypeDef",
    {
        "ComplianceType": NotRequired[ConformancePackComplianceTypeType],
        "CompliantRuleCount": NotRequired[int],
        "NonCompliantRuleCount": NotRequired[int],
        "TotalRuleCount": NotRequired[int],
    },
)
AggregateConformancePackComplianceCountTypeDef = TypedDict(
    "AggregateConformancePackComplianceCountTypeDef",
    {
        "CompliantConformancePackCount": NotRequired[int],
        "NonCompliantConformancePackCount": NotRequired[int],
    },
)
AggregateConformancePackComplianceFiltersTypeDef = TypedDict(
    "AggregateConformancePackComplianceFiltersTypeDef",
    {
        "ConformancePackName": NotRequired[str],
        "ComplianceType": NotRequired[ConformancePackComplianceTypeType],
        "AccountId": NotRequired[str],
        "AwsRegion": NotRequired[str],
    },
)
AggregateConformancePackComplianceSummaryFiltersTypeDef = TypedDict(
    "AggregateConformancePackComplianceSummaryFiltersTypeDef",
    {
        "AccountId": NotRequired[str],
        "AwsRegion": NotRequired[str],
    },
)
AggregateResourceIdentifierTypeDef = TypedDict(
    "AggregateResourceIdentifierTypeDef",
    {
        "SourceAccountId": str,
        "SourceRegion": str,
        "ResourceId": str,
        "ResourceType": ResourceTypeType,
        "ResourceName": NotRequired[str],
    },
)
AggregatedSourceStatusTypeDef = TypedDict(
    "AggregatedSourceStatusTypeDef",
    {
        "SourceId": NotRequired[str],
        "SourceType": NotRequired[AggregatedSourceTypeType],
        "AwsRegion": NotRequired[str],
        "LastUpdateStatus": NotRequired[AggregatedSourceStatusTypeType],
        "LastUpdateTime": NotRequired[datetime],
        "LastErrorCode": NotRequired[str],
        "LastErrorMessage": NotRequired[str],
    },
)
AggregationAuthorizationTypeDef = TypedDict(
    "AggregationAuthorizationTypeDef",
    {
        "AggregationAuthorizationArn": NotRequired[str],
        "AuthorizedAccountId": NotRequired[str],
        "AuthorizedAwsRegion": NotRequired[str],
        "CreationTime": NotRequired[datetime],
    },
)
BaseConfigurationItemTypeDef = TypedDict(
    "BaseConfigurationItemTypeDef",
    {
        "version": NotRequired[str],
        "accountId": NotRequired[str],
        "configurationItemCaptureTime": NotRequired[datetime],
        "configurationItemStatus": NotRequired[ConfigurationItemStatusType],
        "configurationStateId": NotRequired[str],
        "arn": NotRequired[str],
        "resourceType": NotRequired[ResourceTypeType],
        "resourceId": NotRequired[str],
        "resourceName": NotRequired[str],
        "awsRegion": NotRequired[str],
        "availabilityZone": NotRequired[str],
        "resourceCreationTime": NotRequired[datetime],
        "configuration": NotRequired[str],
        "supplementaryConfiguration": NotRequired[Dict[str, str]],
        "recordingFrequency": NotRequired[RecordingFrequencyType],
        "configurationItemDeliveryTime": NotRequired[datetime],
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
ResourceKeyTypeDef = TypedDict(
    "ResourceKeyTypeDef",
    {
        "resourceType": ResourceTypeType,
        "resourceId": str,
    },
)
ComplianceContributorCountTypeDef = TypedDict(
    "ComplianceContributorCountTypeDef",
    {
        "CappedCount": NotRequired[int],
        "CapExceeded": NotRequired[bool],
    },
)
ConfigExportDeliveryInfoTypeDef = TypedDict(
    "ConfigExportDeliveryInfoTypeDef",
    {
        "lastStatus": NotRequired[DeliveryStatusType],
        "lastErrorCode": NotRequired[str],
        "lastErrorMessage": NotRequired[str],
        "lastAttemptTime": NotRequired[datetime],
        "lastSuccessfulTime": NotRequired[datetime],
        "nextDeliveryTime": NotRequired[datetime],
    },
)
ConfigRuleComplianceFiltersTypeDef = TypedDict(
    "ConfigRuleComplianceFiltersTypeDef",
    {
        "ConfigRuleName": NotRequired[str],
        "ComplianceType": NotRequired[ComplianceTypeType],
        "AccountId": NotRequired[str],
        "AwsRegion": NotRequired[str],
    },
)
ConfigRuleComplianceSummaryFiltersTypeDef = TypedDict(
    "ConfigRuleComplianceSummaryFiltersTypeDef",
    {
        "AccountId": NotRequired[str],
        "AwsRegion": NotRequired[str],
    },
)
ConfigRuleEvaluationStatusTypeDef = TypedDict(
    "ConfigRuleEvaluationStatusTypeDef",
    {
        "ConfigRuleName": NotRequired[str],
        "ConfigRuleArn": NotRequired[str],
        "ConfigRuleId": NotRequired[str],
        "LastSuccessfulInvocationTime": NotRequired[datetime],
        "LastFailedInvocationTime": NotRequired[datetime],
        "LastSuccessfulEvaluationTime": NotRequired[datetime],
        "LastFailedEvaluationTime": NotRequired[datetime],
        "FirstActivatedTime": NotRequired[datetime],
        "LastDeactivatedTime": NotRequired[datetime],
        "LastErrorCode": NotRequired[str],
        "LastErrorMessage": NotRequired[str],
        "FirstEvaluationStarted": NotRequired[bool],
        "LastDebugLogDeliveryStatus": NotRequired[str],
        "LastDebugLogDeliveryStatusReason": NotRequired[str],
        "LastDebugLogDeliveryTime": NotRequired[datetime],
    },
)
EvaluationModeConfigurationTypeDef = TypedDict(
    "EvaluationModeConfigurationTypeDef",
    {
        "Mode": NotRequired[EvaluationModeType],
    },
)
ScopeOutputTypeDef = TypedDict(
    "ScopeOutputTypeDef",
    {
        "ComplianceResourceTypes": NotRequired[List[str]],
        "TagKey": NotRequired[str],
        "TagValue": NotRequired[str],
        "ComplianceResourceId": NotRequired[str],
    },
)
ConfigSnapshotDeliveryPropertiesTypeDef = TypedDict(
    "ConfigSnapshotDeliveryPropertiesTypeDef",
    {
        "deliveryFrequency": NotRequired[MaximumExecutionFrequencyType],
    },
)
ConfigStreamDeliveryInfoTypeDef = TypedDict(
    "ConfigStreamDeliveryInfoTypeDef",
    {
        "lastStatus": NotRequired[DeliveryStatusType],
        "lastErrorCode": NotRequired[str],
        "lastErrorMessage": NotRequired[str],
        "lastStatusChangeTime": NotRequired[datetime],
    },
)
OrganizationAggregationSourceOutputTypeDef = TypedDict(
    "OrganizationAggregationSourceOutputTypeDef",
    {
        "RoleArn": str,
        "AwsRegions": NotRequired[List[str]],
        "AllAwsRegions": NotRequired[bool],
    },
)
RelationshipTypeDef = TypedDict(
    "RelationshipTypeDef",
    {
        "resourceType": NotRequired[ResourceTypeType],
        "resourceId": NotRequired[str],
        "resourceName": NotRequired[str],
        "relationshipName": NotRequired[str],
    },
)
ConfigurationRecorderStatusTypeDef = TypedDict(
    "ConfigurationRecorderStatusTypeDef",
    {
        "name": NotRequired[str],
        "lastStartTime": NotRequired[datetime],
        "lastStopTime": NotRequired[datetime],
        "recording": NotRequired[bool],
        "lastStatus": NotRequired[RecorderStatusType],
        "lastErrorCode": NotRequired[str],
        "lastErrorMessage": NotRequired[str],
        "lastStatusChangeTime": NotRequired[datetime],
    },
)
ConformancePackComplianceFiltersTypeDef = TypedDict(
    "ConformancePackComplianceFiltersTypeDef",
    {
        "ConfigRuleNames": NotRequired[Sequence[str]],
        "ComplianceType": NotRequired[ConformancePackComplianceTypeType],
    },
)
ConformancePackComplianceScoreTypeDef = TypedDict(
    "ConformancePackComplianceScoreTypeDef",
    {
        "Score": NotRequired[str],
        "ConformancePackName": NotRequired[str],
        "LastUpdatedTime": NotRequired[datetime],
    },
)
ConformancePackComplianceScoresFiltersTypeDef = TypedDict(
    "ConformancePackComplianceScoresFiltersTypeDef",
    {
        "ConformancePackNames": Sequence[str],
    },
)
ConformancePackComplianceSummaryTypeDef = TypedDict(
    "ConformancePackComplianceSummaryTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackComplianceStatus": ConformancePackComplianceTypeType,
    },
)
ConformancePackInputParameterTypeDef = TypedDict(
    "ConformancePackInputParameterTypeDef",
    {
        "ParameterName": str,
        "ParameterValue": str,
    },
)
TemplateSSMDocumentDetailsTypeDef = TypedDict(
    "TemplateSSMDocumentDetailsTypeDef",
    {
        "DocumentName": str,
        "DocumentVersion": NotRequired[str],
    },
)
ConformancePackEvaluationFiltersTypeDef = TypedDict(
    "ConformancePackEvaluationFiltersTypeDef",
    {
        "ConfigRuleNames": NotRequired[Sequence[str]],
        "ComplianceType": NotRequired[ConformancePackComplianceTypeType],
        "ResourceType": NotRequired[str],
        "ResourceIds": NotRequired[Sequence[str]],
    },
)
ConformancePackRuleComplianceTypeDef = TypedDict(
    "ConformancePackRuleComplianceTypeDef",
    {
        "ConfigRuleName": NotRequired[str],
        "ComplianceType": NotRequired[ConformancePackComplianceTypeType],
        "Controls": NotRequired[List[str]],
    },
)
ConformancePackStatusDetailTypeDef = TypedDict(
    "ConformancePackStatusDetailTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackId": str,
        "ConformancePackArn": str,
        "ConformancePackState": ConformancePackStateType,
        "StackArn": str,
        "LastUpdateRequestedTime": datetime,
        "ConformancePackStatusReason": NotRequired[str],
        "LastUpdateCompletedTime": NotRequired[datetime],
    },
)
CustomPolicyDetailsTypeDef = TypedDict(
    "CustomPolicyDetailsTypeDef",
    {
        "PolicyRuntime": str,
        "PolicyText": str,
        "EnableDebugLogDelivery": NotRequired[bool],
    },
)
DeleteAggregationAuthorizationRequestRequestTypeDef = TypedDict(
    "DeleteAggregationAuthorizationRequestRequestTypeDef",
    {
        "AuthorizedAccountId": str,
        "AuthorizedAwsRegion": str,
    },
)
DeleteConfigRuleRequestRequestTypeDef = TypedDict(
    "DeleteConfigRuleRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
    },
)
DeleteConfigurationAggregatorRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationAggregatorRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
    },
)
DeleteConfigurationRecorderRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationRecorderRequestRequestTypeDef",
    {
        "ConfigurationRecorderName": str,
    },
)
DeleteConformancePackRequestRequestTypeDef = TypedDict(
    "DeleteConformancePackRequestRequestTypeDef",
    {
        "ConformancePackName": str,
    },
)
DeleteDeliveryChannelRequestRequestTypeDef = TypedDict(
    "DeleteDeliveryChannelRequestRequestTypeDef",
    {
        "DeliveryChannelName": str,
    },
)
DeleteEvaluationResultsRequestRequestTypeDef = TypedDict(
    "DeleteEvaluationResultsRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
    },
)
DeleteOrganizationConfigRuleRequestRequestTypeDef = TypedDict(
    "DeleteOrganizationConfigRuleRequestRequestTypeDef",
    {
        "OrganizationConfigRuleName": str,
    },
)
DeleteOrganizationConformancePackRequestRequestTypeDef = TypedDict(
    "DeleteOrganizationConformancePackRequestRequestTypeDef",
    {
        "OrganizationConformancePackName": str,
    },
)
DeletePendingAggregationRequestRequestRequestTypeDef = TypedDict(
    "DeletePendingAggregationRequestRequestRequestTypeDef",
    {
        "RequesterAccountId": str,
        "RequesterAwsRegion": str,
    },
)
DeleteRemediationConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteRemediationConfigurationRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceType": NotRequired[str],
    },
)
RemediationExceptionResourceKeyTypeDef = TypedDict(
    "RemediationExceptionResourceKeyTypeDef",
    {
        "ResourceType": NotRequired[str],
        "ResourceId": NotRequired[str],
    },
)
DeleteResourceConfigRequestRequestTypeDef = TypedDict(
    "DeleteResourceConfigRequestRequestTypeDef",
    {
        "ResourceType": str,
        "ResourceId": str,
    },
)
DeleteRetentionConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteRetentionConfigurationRequestRequestTypeDef",
    {
        "RetentionConfigurationName": str,
    },
)
DeleteStoredQueryRequestRequestTypeDef = TypedDict(
    "DeleteStoredQueryRequestRequestTypeDef",
    {
        "QueryName": str,
    },
)
DeliverConfigSnapshotRequestRequestTypeDef = TypedDict(
    "DeliverConfigSnapshotRequestRequestTypeDef",
    {
        "deliveryChannelName": str,
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
DescribeAggregationAuthorizationsRequestRequestTypeDef = TypedDict(
    "DescribeAggregationAuthorizationsRequestRequestTypeDef",
    {
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeComplianceByConfigRuleRequestRequestTypeDef = TypedDict(
    "DescribeComplianceByConfigRuleRequestRequestTypeDef",
    {
        "ConfigRuleNames": NotRequired[Sequence[str]],
        "ComplianceTypes": NotRequired[Sequence[ComplianceTypeType]],
        "NextToken": NotRequired[str],
    },
)
DescribeComplianceByResourceRequestRequestTypeDef = TypedDict(
    "DescribeComplianceByResourceRequestRequestTypeDef",
    {
        "ResourceType": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ComplianceTypes": NotRequired[Sequence[ComplianceTypeType]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeConfigRuleEvaluationStatusRequestRequestTypeDef = TypedDict(
    "DescribeConfigRuleEvaluationStatusRequestRequestTypeDef",
    {
        "ConfigRuleNames": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
DescribeConfigRulesFiltersTypeDef = TypedDict(
    "DescribeConfigRulesFiltersTypeDef",
    {
        "EvaluationMode": NotRequired[EvaluationModeType],
    },
)
DescribeConfigurationAggregatorSourcesStatusRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationAggregatorSourcesStatusRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "UpdateStatus": NotRequired[Sequence[AggregatedSourceStatusTypeType]],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
DescribeConfigurationAggregatorsRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationAggregatorsRequestRequestTypeDef",
    {
        "ConfigurationAggregatorNames": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
DescribeConfigurationRecorderStatusRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationRecorderStatusRequestRequestTypeDef",
    {
        "ConfigurationRecorderNames": NotRequired[Sequence[str]],
    },
)
DescribeConfigurationRecordersRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationRecordersRequestRequestTypeDef",
    {
        "ConfigurationRecorderNames": NotRequired[Sequence[str]],
    },
)
DescribeConformancePackStatusRequestRequestTypeDef = TypedDict(
    "DescribeConformancePackStatusRequestRequestTypeDef",
    {
        "ConformancePackNames": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeConformancePacksRequestRequestTypeDef = TypedDict(
    "DescribeConformancePacksRequestRequestTypeDef",
    {
        "ConformancePackNames": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeDeliveryChannelStatusRequestRequestTypeDef = TypedDict(
    "DescribeDeliveryChannelStatusRequestRequestTypeDef",
    {
        "DeliveryChannelNames": NotRequired[Sequence[str]],
    },
)
DescribeDeliveryChannelsRequestRequestTypeDef = TypedDict(
    "DescribeDeliveryChannelsRequestRequestTypeDef",
    {
        "DeliveryChannelNames": NotRequired[Sequence[str]],
    },
)
DescribeOrganizationConfigRuleStatusesRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationConfigRuleStatusesRequestRequestTypeDef",
    {
        "OrganizationConfigRuleNames": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
OrganizationConfigRuleStatusTypeDef = TypedDict(
    "OrganizationConfigRuleStatusTypeDef",
    {
        "OrganizationConfigRuleName": str,
        "OrganizationRuleStatus": OrganizationRuleStatusType,
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
        "LastUpdateTime": NotRequired[datetime],
    },
)
DescribeOrganizationConfigRulesRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationConfigRulesRequestRequestTypeDef",
    {
        "OrganizationConfigRuleNames": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeOrganizationConformancePackStatusesRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationConformancePackStatusesRequestRequestTypeDef",
    {
        "OrganizationConformancePackNames": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
OrganizationConformancePackStatusTypeDef = TypedDict(
    "OrganizationConformancePackStatusTypeDef",
    {
        "OrganizationConformancePackName": str,
        "Status": OrganizationResourceStatusType,
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
        "LastUpdateTime": NotRequired[datetime],
    },
)
DescribeOrganizationConformancePacksRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationConformancePacksRequestRequestTypeDef",
    {
        "OrganizationConformancePackNames": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribePendingAggregationRequestsRequestRequestTypeDef = TypedDict(
    "DescribePendingAggregationRequestsRequestRequestTypeDef",
    {
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
PendingAggregationRequestTypeDef = TypedDict(
    "PendingAggregationRequestTypeDef",
    {
        "RequesterAccountId": NotRequired[str],
        "RequesterAwsRegion": NotRequired[str],
    },
)
DescribeRemediationConfigurationsRequestRequestTypeDef = TypedDict(
    "DescribeRemediationConfigurationsRequestRequestTypeDef",
    {
        "ConfigRuleNames": Sequence[str],
    },
)
RemediationExceptionTypeDef = TypedDict(
    "RemediationExceptionTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceType": str,
        "ResourceId": str,
        "Message": NotRequired[str],
        "ExpirationTime": NotRequired[datetime],
    },
)
DescribeRetentionConfigurationsRequestRequestTypeDef = TypedDict(
    "DescribeRetentionConfigurationsRequestRequestTypeDef",
    {
        "RetentionConfigurationNames": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
    },
)
RetentionConfigurationTypeDef = TypedDict(
    "RetentionConfigurationTypeDef",
    {
        "Name": str,
        "RetentionPeriodInDays": int,
    },
)
EvaluationContextTypeDef = TypedDict(
    "EvaluationContextTypeDef",
    {
        "EvaluationContextIdentifier": NotRequired[str],
    },
)
EvaluationOutputTypeDef = TypedDict(
    "EvaluationOutputTypeDef",
    {
        "ComplianceResourceType": str,
        "ComplianceResourceId": str,
        "ComplianceType": ComplianceTypeType,
        "OrderingTimestamp": datetime,
        "Annotation": NotRequired[str],
    },
)
EvaluationResultQualifierTypeDef = TypedDict(
    "EvaluationResultQualifierTypeDef",
    {
        "ConfigRuleName": NotRequired[str],
        "ResourceType": NotRequired[str],
        "ResourceId": NotRequired[str],
        "EvaluationMode": NotRequired[EvaluationModeType],
    },
)
EvaluationStatusTypeDef = TypedDict(
    "EvaluationStatusTypeDef",
    {
        "Status": ResourceEvaluationStatusType,
        "FailureReason": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
ExclusionByResourceTypesOutputTypeDef = TypedDict(
    "ExclusionByResourceTypesOutputTypeDef",
    {
        "resourceTypes": NotRequired[List[ResourceTypeType]],
    },
)
ExclusionByResourceTypesTypeDef = TypedDict(
    "ExclusionByResourceTypesTypeDef",
    {
        "resourceTypes": NotRequired[Sequence[ResourceTypeType]],
    },
)
SsmControlsTypeDef = TypedDict(
    "SsmControlsTypeDef",
    {
        "ConcurrentExecutionRatePercentage": NotRequired[int],
        "ErrorPercentage": NotRequired[int],
    },
)
FieldInfoTypeDef = TypedDict(
    "FieldInfoTypeDef",
    {
        "Name": NotRequired[str],
    },
)
GetAggregateComplianceDetailsByConfigRuleRequestRequestTypeDef = TypedDict(
    "GetAggregateComplianceDetailsByConfigRuleRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ConfigRuleName": str,
        "AccountId": str,
        "AwsRegion": str,
        "ComplianceType": NotRequired[ComplianceTypeType],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ResourceCountFiltersTypeDef = TypedDict(
    "ResourceCountFiltersTypeDef",
    {
        "ResourceType": NotRequired[ResourceTypeType],
        "AccountId": NotRequired[str],
        "Region": NotRequired[str],
    },
)
GroupedResourceCountTypeDef = TypedDict(
    "GroupedResourceCountTypeDef",
    {
        "GroupName": str,
        "ResourceCount": int,
    },
)
GetComplianceDetailsByConfigRuleRequestRequestTypeDef = TypedDict(
    "GetComplianceDetailsByConfigRuleRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
        "ComplianceTypes": NotRequired[Sequence[ComplianceTypeType]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetComplianceDetailsByResourceRequestRequestTypeDef = TypedDict(
    "GetComplianceDetailsByResourceRequestRequestTypeDef",
    {
        "ResourceType": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ComplianceTypes": NotRequired[Sequence[ComplianceTypeType]],
        "NextToken": NotRequired[str],
        "ResourceEvaluationId": NotRequired[str],
    },
)
GetComplianceSummaryByResourceTypeRequestRequestTypeDef = TypedDict(
    "GetComplianceSummaryByResourceTypeRequestRequestTypeDef",
    {
        "ResourceTypes": NotRequired[Sequence[str]],
    },
)
GetConformancePackComplianceSummaryRequestRequestTypeDef = TypedDict(
    "GetConformancePackComplianceSummaryRequestRequestTypeDef",
    {
        "ConformancePackNames": Sequence[str],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetCustomRulePolicyRequestRequestTypeDef = TypedDict(
    "GetCustomRulePolicyRequestRequestTypeDef",
    {
        "ConfigRuleName": NotRequired[str],
    },
)
GetDiscoveredResourceCountsRequestRequestTypeDef = TypedDict(
    "GetDiscoveredResourceCountsRequestRequestTypeDef",
    {
        "resourceTypes": NotRequired[Sequence[str]],
        "limit": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ResourceCountTypeDef = TypedDict(
    "ResourceCountTypeDef",
    {
        "resourceType": NotRequired[ResourceTypeType],
        "count": NotRequired[int],
    },
)
StatusDetailFiltersTypeDef = TypedDict(
    "StatusDetailFiltersTypeDef",
    {
        "AccountId": NotRequired[str],
        "MemberAccountRuleStatus": NotRequired[MemberAccountRuleStatusType],
    },
)
MemberAccountStatusTypeDef = TypedDict(
    "MemberAccountStatusTypeDef",
    {
        "AccountId": str,
        "ConfigRuleName": str,
        "MemberAccountRuleStatus": MemberAccountRuleStatusType,
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
        "LastUpdateTime": NotRequired[datetime],
    },
)
OrganizationResourceDetailedStatusFiltersTypeDef = TypedDict(
    "OrganizationResourceDetailedStatusFiltersTypeDef",
    {
        "AccountId": NotRequired[str],
        "Status": NotRequired[OrganizationResourceDetailedStatusType],
    },
)
OrganizationConformancePackDetailedStatusTypeDef = TypedDict(
    "OrganizationConformancePackDetailedStatusTypeDef",
    {
        "AccountId": str,
        "ConformancePackName": str,
        "Status": OrganizationResourceDetailedStatusType,
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
        "LastUpdateTime": NotRequired[datetime],
    },
)
GetOrganizationCustomRulePolicyRequestRequestTypeDef = TypedDict(
    "GetOrganizationCustomRulePolicyRequestRequestTypeDef",
    {
        "OrganizationConfigRuleName": str,
    },
)
GetResourceEvaluationSummaryRequestRequestTypeDef = TypedDict(
    "GetResourceEvaluationSummaryRequestRequestTypeDef",
    {
        "ResourceEvaluationId": str,
    },
)
ResourceDetailsTypeDef = TypedDict(
    "ResourceDetailsTypeDef",
    {
        "ResourceId": str,
        "ResourceType": str,
        "ResourceConfiguration": str,
        "ResourceConfigurationSchemaType": NotRequired[Literal["CFN_RESOURCE_SCHEMA"]],
    },
)
GetStoredQueryRequestRequestTypeDef = TypedDict(
    "GetStoredQueryRequestRequestTypeDef",
    {
        "QueryName": str,
    },
)
StoredQueryTypeDef = TypedDict(
    "StoredQueryTypeDef",
    {
        "QueryName": str,
        "QueryId": NotRequired[str],
        "QueryArn": NotRequired[str],
        "Description": NotRequired[str],
        "Expression": NotRequired[str],
    },
)
ResourceFiltersTypeDef = TypedDict(
    "ResourceFiltersTypeDef",
    {
        "AccountId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceName": NotRequired[str],
        "Region": NotRequired[str],
    },
)
ListDiscoveredResourcesRequestRequestTypeDef = TypedDict(
    "ListDiscoveredResourcesRequestRequestTypeDef",
    {
        "resourceType": ResourceTypeType,
        "resourceIds": NotRequired[Sequence[str]],
        "resourceName": NotRequired[str],
        "limit": NotRequired[int],
        "includeDeletedResources": NotRequired[bool],
        "nextToken": NotRequired[str],
    },
)
ResourceIdentifierTypeDef = TypedDict(
    "ResourceIdentifierTypeDef",
    {
        "resourceType": NotRequired[ResourceTypeType],
        "resourceId": NotRequired[str],
        "resourceName": NotRequired[str],
        "resourceDeletionTime": NotRequired[datetime],
    },
)
ResourceEvaluationTypeDef = TypedDict(
    "ResourceEvaluationTypeDef",
    {
        "ResourceEvaluationId": NotRequired[str],
        "EvaluationMode": NotRequired[EvaluationModeType],
        "EvaluationStartTimestamp": NotRequired[datetime],
    },
)
ListStoredQueriesRequestRequestTypeDef = TypedDict(
    "ListStoredQueriesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
StoredQueryMetadataTypeDef = TypedDict(
    "StoredQueryMetadataTypeDef",
    {
        "QueryId": str,
        "QueryArn": str,
        "QueryName": str,
        "Description": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
OrganizationAggregationSourceTypeDef = TypedDict(
    "OrganizationAggregationSourceTypeDef",
    {
        "RoleArn": str,
        "AwsRegions": NotRequired[Sequence[str]],
        "AllAwsRegions": NotRequired[bool],
    },
)
OrganizationCustomPolicyRuleMetadataNoPolicyTypeDef = TypedDict(
    "OrganizationCustomPolicyRuleMetadataNoPolicyTypeDef",
    {
        "Description": NotRequired[str],
        "OrganizationConfigRuleTriggerTypes": NotRequired[
            List[OrganizationConfigRuleTriggerTypeNoSNType]
        ],
        "InputParameters": NotRequired[str],
        "MaximumExecutionFrequency": NotRequired[MaximumExecutionFrequencyType],
        "ResourceTypesScope": NotRequired[List[str]],
        "ResourceIdScope": NotRequired[str],
        "TagKeyScope": NotRequired[str],
        "TagValueScope": NotRequired[str],
        "PolicyRuntime": NotRequired[str],
        "DebugLogDeliveryAccounts": NotRequired[List[str]],
    },
)
OrganizationCustomRuleMetadataOutputTypeDef = TypedDict(
    "OrganizationCustomRuleMetadataOutputTypeDef",
    {
        "LambdaFunctionArn": str,
        "OrganizationConfigRuleTriggerTypes": List[OrganizationConfigRuleTriggerTypeType],
        "Description": NotRequired[str],
        "InputParameters": NotRequired[str],
        "MaximumExecutionFrequency": NotRequired[MaximumExecutionFrequencyType],
        "ResourceTypesScope": NotRequired[List[str]],
        "ResourceIdScope": NotRequired[str],
        "TagKeyScope": NotRequired[str],
        "TagValueScope": NotRequired[str],
    },
)
OrganizationManagedRuleMetadataOutputTypeDef = TypedDict(
    "OrganizationManagedRuleMetadataOutputTypeDef",
    {
        "RuleIdentifier": str,
        "Description": NotRequired[str],
        "InputParameters": NotRequired[str],
        "MaximumExecutionFrequency": NotRequired[MaximumExecutionFrequencyType],
        "ResourceTypesScope": NotRequired[List[str]],
        "ResourceIdScope": NotRequired[str],
        "TagKeyScope": NotRequired[str],
        "TagValueScope": NotRequired[str],
    },
)
OrganizationCustomPolicyRuleMetadataTypeDef = TypedDict(
    "OrganizationCustomPolicyRuleMetadataTypeDef",
    {
        "PolicyRuntime": str,
        "PolicyText": str,
        "Description": NotRequired[str],
        "OrganizationConfigRuleTriggerTypes": NotRequired[
            Sequence[OrganizationConfigRuleTriggerTypeNoSNType]
        ],
        "InputParameters": NotRequired[str],
        "MaximumExecutionFrequency": NotRequired[MaximumExecutionFrequencyType],
        "ResourceTypesScope": NotRequired[Sequence[str]],
        "ResourceIdScope": NotRequired[str],
        "TagKeyScope": NotRequired[str],
        "TagValueScope": NotRequired[str],
        "DebugLogDeliveryAccounts": NotRequired[Sequence[str]],
    },
)
OrganizationCustomRuleMetadataTypeDef = TypedDict(
    "OrganizationCustomRuleMetadataTypeDef",
    {
        "LambdaFunctionArn": str,
        "OrganizationConfigRuleTriggerTypes": Sequence[OrganizationConfigRuleTriggerTypeType],
        "Description": NotRequired[str],
        "InputParameters": NotRequired[str],
        "MaximumExecutionFrequency": NotRequired[MaximumExecutionFrequencyType],
        "ResourceTypesScope": NotRequired[Sequence[str]],
        "ResourceIdScope": NotRequired[str],
        "TagKeyScope": NotRequired[str],
        "TagValueScope": NotRequired[str],
    },
)
OrganizationManagedRuleMetadataTypeDef = TypedDict(
    "OrganizationManagedRuleMetadataTypeDef",
    {
        "RuleIdentifier": str,
        "Description": NotRequired[str],
        "InputParameters": NotRequired[str],
        "MaximumExecutionFrequency": NotRequired[MaximumExecutionFrequencyType],
        "ResourceTypesScope": NotRequired[Sequence[str]],
        "ResourceIdScope": NotRequired[str],
        "TagKeyScope": NotRequired[str],
        "TagValueScope": NotRequired[str],
    },
)
PutResourceConfigRequestRequestTypeDef = TypedDict(
    "PutResourceConfigRequestRequestTypeDef",
    {
        "ResourceType": str,
        "SchemaVersionId": str,
        "ResourceId": str,
        "Configuration": str,
        "ResourceName": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
PutRetentionConfigurationRequestRequestTypeDef = TypedDict(
    "PutRetentionConfigurationRequestRequestTypeDef",
    {
        "RetentionPeriodInDays": int,
    },
)
RecordingStrategyTypeDef = TypedDict(
    "RecordingStrategyTypeDef",
    {
        "useOnly": NotRequired[RecordingStrategyTypeType],
    },
)
RecordingModeOverrideOutputTypeDef = TypedDict(
    "RecordingModeOverrideOutputTypeDef",
    {
        "resourceTypes": List[ResourceTypeType],
        "recordingFrequency": RecordingFrequencyType,
        "description": NotRequired[str],
    },
)
RecordingModeOverrideTypeDef = TypedDict(
    "RecordingModeOverrideTypeDef",
    {
        "resourceTypes": Sequence[ResourceTypeType],
        "recordingFrequency": RecordingFrequencyType,
        "description": NotRequired[str],
    },
)
RemediationExecutionStepTypeDef = TypedDict(
    "RemediationExecutionStepTypeDef",
    {
        "Name": NotRequired[str],
        "State": NotRequired[RemediationExecutionStepStateType],
        "ErrorMessage": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "StopTime": NotRequired[datetime],
    },
)
ResourceValueTypeDef = TypedDict(
    "ResourceValueTypeDef",
    {
        "Value": Literal["RESOURCE_ID"],
    },
)
StaticValueOutputTypeDef = TypedDict(
    "StaticValueOutputTypeDef",
    {
        "Values": List[str],
    },
)
ScopeTypeDef = TypedDict(
    "ScopeTypeDef",
    {
        "ComplianceResourceTypes": NotRequired[Sequence[str]],
        "TagKey": NotRequired[str],
        "TagValue": NotRequired[str],
        "ComplianceResourceId": NotRequired[str],
    },
)
SelectAggregateResourceConfigRequestRequestTypeDef = TypedDict(
    "SelectAggregateResourceConfigRequestRequestTypeDef",
    {
        "Expression": str,
        "ConfigurationAggregatorName": str,
        "Limit": NotRequired[int],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
SelectResourceConfigRequestRequestTypeDef = TypedDict(
    "SelectResourceConfigRequestRequestTypeDef",
    {
        "Expression": str,
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
SourceDetailTypeDef = TypedDict(
    "SourceDetailTypeDef",
    {
        "EventSource": NotRequired[Literal["aws.config"]],
        "MessageType": NotRequired[MessageTypeType],
        "MaximumExecutionFrequency": NotRequired[MaximumExecutionFrequencyType],
    },
)
StartConfigRulesEvaluationRequestRequestTypeDef = TypedDict(
    "StartConfigRulesEvaluationRequestRequestTypeDef",
    {
        "ConfigRuleNames": NotRequired[Sequence[str]],
    },
)
StartConfigurationRecorderRequestRequestTypeDef = TypedDict(
    "StartConfigurationRecorderRequestRequestTypeDef",
    {
        "ConfigurationRecorderName": str,
    },
)
StaticValueTypeDef = TypedDict(
    "StaticValueTypeDef",
    {
        "Values": Sequence[str],
    },
)
StopConfigurationRecorderRequestRequestTypeDef = TypedDict(
    "StopConfigurationRecorderRequestRequestTypeDef",
    {
        "ConfigurationRecorderName": str,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
AccountAggregationSourceUnionTypeDef = Union[
    AccountAggregationSourceTypeDef, AccountAggregationSourceOutputTypeDef
]
AggregateComplianceByConformancePackTypeDef = TypedDict(
    "AggregateComplianceByConformancePackTypeDef",
    {
        "ConformancePackName": NotRequired[str],
        "Compliance": NotRequired[AggregateConformancePackComplianceTypeDef],
        "AccountId": NotRequired[str],
        "AwsRegion": NotRequired[str],
    },
)
AggregateConformancePackComplianceSummaryTypeDef = TypedDict(
    "AggregateConformancePackComplianceSummaryTypeDef",
    {
        "ComplianceSummary": NotRequired[AggregateConformancePackComplianceCountTypeDef],
        "GroupName": NotRequired[str],
    },
)
DescribeAggregateComplianceByConformancePacksRequestRequestTypeDef = TypedDict(
    "DescribeAggregateComplianceByConformancePacksRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "Filters": NotRequired[AggregateConformancePackComplianceFiltersTypeDef],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetAggregateConformancePackComplianceSummaryRequestRequestTypeDef = TypedDict(
    "GetAggregateConformancePackComplianceSummaryRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "Filters": NotRequired[AggregateConformancePackComplianceSummaryFiltersTypeDef],
        "GroupByKey": NotRequired[AggregateConformancePackComplianceSummaryGroupKeyType],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
BatchGetAggregateResourceConfigRequestRequestTypeDef = TypedDict(
    "BatchGetAggregateResourceConfigRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ResourceIdentifiers": Sequence[AggregateResourceIdentifierTypeDef],
    },
)
GetAggregateResourceConfigRequestRequestTypeDef = TypedDict(
    "GetAggregateResourceConfigRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ResourceIdentifier": AggregateResourceIdentifierTypeDef,
    },
)
BatchGetAggregateResourceConfigResponseTypeDef = TypedDict(
    "BatchGetAggregateResourceConfigResponseTypeDef",
    {
        "BaseConfigurationItems": List[BaseConfigurationItemTypeDef],
        "UnprocessedResourceIdentifiers": List[AggregateResourceIdentifierTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeliverConfigSnapshotResponseTypeDef = TypedDict(
    "DeliverConfigSnapshotResponseTypeDef",
    {
        "configSnapshotId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAggregationAuthorizationsResponseTypeDef = TypedDict(
    "DescribeAggregationAuthorizationsResponseTypeDef",
    {
        "AggregationAuthorizations": List[AggregationAuthorizationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeConfigurationAggregatorSourcesStatusResponseTypeDef = TypedDict(
    "DescribeConfigurationAggregatorSourcesStatusResponseTypeDef",
    {
        "AggregatedSourceStatusList": List[AggregatedSourceStatusTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCustomRulePolicyResponseTypeDef = TypedDict(
    "GetCustomRulePolicyResponseTypeDef",
    {
        "PolicyText": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetOrganizationCustomRulePolicyResponseTypeDef = TypedDict(
    "GetOrganizationCustomRulePolicyResponseTypeDef",
    {
        "PolicyText": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAggregateDiscoveredResourcesResponseTypeDef = TypedDict(
    "ListAggregateDiscoveredResourcesResponseTypeDef",
    {
        "ResourceIdentifiers": List[AggregateResourceIdentifierTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PutAggregationAuthorizationResponseTypeDef = TypedDict(
    "PutAggregationAuthorizationResponseTypeDef",
    {
        "AggregationAuthorization": AggregationAuthorizationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutConformancePackResponseTypeDef = TypedDict(
    "PutConformancePackResponseTypeDef",
    {
        "ConformancePackArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutOrganizationConfigRuleResponseTypeDef = TypedDict(
    "PutOrganizationConfigRuleResponseTypeDef",
    {
        "OrganizationConfigRuleArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutOrganizationConformancePackResponseTypeDef = TypedDict(
    "PutOrganizationConformancePackResponseTypeDef",
    {
        "OrganizationConformancePackArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutStoredQueryResponseTypeDef = TypedDict(
    "PutStoredQueryResponseTypeDef",
    {
        "QueryArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartResourceEvaluationResponseTypeDef = TypedDict(
    "StartResourceEvaluationResponseTypeDef",
    {
        "ResourceEvaluationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetResourceConfigRequestRequestTypeDef = TypedDict(
    "BatchGetResourceConfigRequestRequestTypeDef",
    {
        "resourceKeys": Sequence[ResourceKeyTypeDef],
    },
)
BatchGetResourceConfigResponseTypeDef = TypedDict(
    "BatchGetResourceConfigResponseTypeDef",
    {
        "baseConfigurationItems": List[BaseConfigurationItemTypeDef],
        "unprocessedResourceKeys": List[ResourceKeyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRemediationExecutionStatusRequestRequestTypeDef = TypedDict(
    "DescribeRemediationExecutionStatusRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceKeys": NotRequired[Sequence[ResourceKeyTypeDef]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
StartRemediationExecutionRequestRequestTypeDef = TypedDict(
    "StartRemediationExecutionRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceKeys": Sequence[ResourceKeyTypeDef],
    },
)
StartRemediationExecutionResponseTypeDef = TypedDict(
    "StartRemediationExecutionResponseTypeDef",
    {
        "FailureMessage": str,
        "FailedItems": List[ResourceKeyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ComplianceSummaryTypeDef = TypedDict(
    "ComplianceSummaryTypeDef",
    {
        "CompliantResourceCount": NotRequired[ComplianceContributorCountTypeDef],
        "NonCompliantResourceCount": NotRequired[ComplianceContributorCountTypeDef],
        "ComplianceSummaryTimestamp": NotRequired[datetime],
    },
)
ComplianceTypeDef = TypedDict(
    "ComplianceTypeDef",
    {
        "ComplianceType": NotRequired[ComplianceTypeType],
        "ComplianceContributorCount": NotRequired[ComplianceContributorCountTypeDef],
    },
)
DescribeAggregateComplianceByConfigRulesRequestRequestTypeDef = TypedDict(
    "DescribeAggregateComplianceByConfigRulesRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "Filters": NotRequired[ConfigRuleComplianceFiltersTypeDef],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetAggregateConfigRuleComplianceSummaryRequestRequestTypeDef = TypedDict(
    "GetAggregateConfigRuleComplianceSummaryRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "Filters": NotRequired[ConfigRuleComplianceSummaryFiltersTypeDef],
        "GroupByKey": NotRequired[ConfigRuleComplianceSummaryGroupKeyType],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeConfigRuleEvaluationStatusResponseTypeDef = TypedDict(
    "DescribeConfigRuleEvaluationStatusResponseTypeDef",
    {
        "ConfigRulesEvaluationStatus": List[ConfigRuleEvaluationStatusTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DeliveryChannelTypeDef = TypedDict(
    "DeliveryChannelTypeDef",
    {
        "name": NotRequired[str],
        "s3BucketName": NotRequired[str],
        "s3KeyPrefix": NotRequired[str],
        "s3KmsKeyArn": NotRequired[str],
        "snsTopicARN": NotRequired[str],
        "configSnapshotDeliveryProperties": NotRequired[ConfigSnapshotDeliveryPropertiesTypeDef],
    },
)
DeliveryChannelStatusTypeDef = TypedDict(
    "DeliveryChannelStatusTypeDef",
    {
        "name": NotRequired[str],
        "configSnapshotDeliveryInfo": NotRequired[ConfigExportDeliveryInfoTypeDef],
        "configHistoryDeliveryInfo": NotRequired[ConfigExportDeliveryInfoTypeDef],
        "configStreamDeliveryInfo": NotRequired[ConfigStreamDeliveryInfoTypeDef],
    },
)
ConfigurationAggregatorTypeDef = TypedDict(
    "ConfigurationAggregatorTypeDef",
    {
        "ConfigurationAggregatorName": NotRequired[str],
        "ConfigurationAggregatorArn": NotRequired[str],
        "AccountAggregationSources": NotRequired[List[AccountAggregationSourceOutputTypeDef]],
        "OrganizationAggregationSource": NotRequired[OrganizationAggregationSourceOutputTypeDef],
        "CreationTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "CreatedBy": NotRequired[str],
    },
)
ConfigurationItemTypeDef = TypedDict(
    "ConfigurationItemTypeDef",
    {
        "version": NotRequired[str],
        "accountId": NotRequired[str],
        "configurationItemCaptureTime": NotRequired[datetime],
        "configurationItemStatus": NotRequired[ConfigurationItemStatusType],
        "configurationStateId": NotRequired[str],
        "configurationItemMD5Hash": NotRequired[str],
        "arn": NotRequired[str],
        "resourceType": NotRequired[ResourceTypeType],
        "resourceId": NotRequired[str],
        "resourceName": NotRequired[str],
        "awsRegion": NotRequired[str],
        "availabilityZone": NotRequired[str],
        "resourceCreationTime": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
        "relatedEvents": NotRequired[List[str]],
        "relationships": NotRequired[List[RelationshipTypeDef]],
        "configuration": NotRequired[str],
        "supplementaryConfiguration": NotRequired[Dict[str, str]],
        "recordingFrequency": NotRequired[RecordingFrequencyType],
        "configurationItemDeliveryTime": NotRequired[datetime],
    },
)
DescribeConfigurationRecorderStatusResponseTypeDef = TypedDict(
    "DescribeConfigurationRecorderStatusResponseTypeDef",
    {
        "ConfigurationRecordersStatus": List[ConfigurationRecorderStatusTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeConformancePackComplianceRequestRequestTypeDef = TypedDict(
    "DescribeConformancePackComplianceRequestRequestTypeDef",
    {
        "ConformancePackName": str,
        "Filters": NotRequired[ConformancePackComplianceFiltersTypeDef],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListConformancePackComplianceScoresResponseTypeDef = TypedDict(
    "ListConformancePackComplianceScoresResponseTypeDef",
    {
        "ConformancePackComplianceScores": List[ConformancePackComplianceScoreTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListConformancePackComplianceScoresRequestRequestTypeDef = TypedDict(
    "ListConformancePackComplianceScoresRequestRequestTypeDef",
    {
        "Filters": NotRequired[ConformancePackComplianceScoresFiltersTypeDef],
        "SortOrder": NotRequired[SortOrderType],
        "SortBy": NotRequired[Literal["SCORE"]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetConformancePackComplianceSummaryResponseTypeDef = TypedDict(
    "GetConformancePackComplianceSummaryResponseTypeDef",
    {
        "ConformancePackComplianceSummaryList": List[ConformancePackComplianceSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
OrganizationConformancePackTypeDef = TypedDict(
    "OrganizationConformancePackTypeDef",
    {
        "OrganizationConformancePackName": str,
        "OrganizationConformancePackArn": str,
        "LastUpdateTime": datetime,
        "DeliveryS3Bucket": NotRequired[str],
        "DeliveryS3KeyPrefix": NotRequired[str],
        "ConformancePackInputParameters": NotRequired[List[ConformancePackInputParameterTypeDef]],
        "ExcludedAccounts": NotRequired[List[str]],
    },
)
PutOrganizationConformancePackRequestRequestTypeDef = TypedDict(
    "PutOrganizationConformancePackRequestRequestTypeDef",
    {
        "OrganizationConformancePackName": str,
        "TemplateS3Uri": NotRequired[str],
        "TemplateBody": NotRequired[str],
        "DeliveryS3Bucket": NotRequired[str],
        "DeliveryS3KeyPrefix": NotRequired[str],
        "ConformancePackInputParameters": NotRequired[
            Sequence[ConformancePackInputParameterTypeDef]
        ],
        "ExcludedAccounts": NotRequired[Sequence[str]],
    },
)
ConformancePackDetailTypeDef = TypedDict(
    "ConformancePackDetailTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackArn": str,
        "ConformancePackId": str,
        "DeliveryS3Bucket": NotRequired[str],
        "DeliveryS3KeyPrefix": NotRequired[str],
        "ConformancePackInputParameters": NotRequired[List[ConformancePackInputParameterTypeDef]],
        "LastUpdateRequestedTime": NotRequired[datetime],
        "CreatedBy": NotRequired[str],
        "TemplateSSMDocumentDetails": NotRequired[TemplateSSMDocumentDetailsTypeDef],
    },
)
PutConformancePackRequestRequestTypeDef = TypedDict(
    "PutConformancePackRequestRequestTypeDef",
    {
        "ConformancePackName": str,
        "TemplateS3Uri": NotRequired[str],
        "TemplateBody": NotRequired[str],
        "DeliveryS3Bucket": NotRequired[str],
        "DeliveryS3KeyPrefix": NotRequired[str],
        "ConformancePackInputParameters": NotRequired[
            Sequence[ConformancePackInputParameterTypeDef]
        ],
        "TemplateSSMDocumentDetails": NotRequired[TemplateSSMDocumentDetailsTypeDef],
    },
)
GetConformancePackComplianceDetailsRequestRequestTypeDef = TypedDict(
    "GetConformancePackComplianceDetailsRequestRequestTypeDef",
    {
        "ConformancePackName": str,
        "Filters": NotRequired[ConformancePackEvaluationFiltersTypeDef],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeConformancePackComplianceResponseTypeDef = TypedDict(
    "DescribeConformancePackComplianceResponseTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackRuleComplianceList": List[ConformancePackRuleComplianceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeConformancePackStatusResponseTypeDef = TypedDict(
    "DescribeConformancePackStatusResponseTypeDef",
    {
        "ConformancePackStatusDetails": List[ConformancePackStatusDetailTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DeleteRemediationExceptionsRequestRequestTypeDef = TypedDict(
    "DeleteRemediationExceptionsRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceKeys": Sequence[RemediationExceptionResourceKeyTypeDef],
    },
)
DescribeRemediationExceptionsRequestRequestTypeDef = TypedDict(
    "DescribeRemediationExceptionsRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceKeys": NotRequired[Sequence[RemediationExceptionResourceKeyTypeDef]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
FailedDeleteRemediationExceptionsBatchTypeDef = TypedDict(
    "FailedDeleteRemediationExceptionsBatchTypeDef",
    {
        "FailureMessage": NotRequired[str],
        "FailedItems": NotRequired[List[RemediationExceptionResourceKeyTypeDef]],
    },
)
DescribeAggregateComplianceByConfigRulesRequestDescribeAggregateComplianceByConfigRulesPaginateTypeDef = TypedDict(
    "DescribeAggregateComplianceByConfigRulesRequestDescribeAggregateComplianceByConfigRulesPaginateTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "Filters": NotRequired[ConfigRuleComplianceFiltersTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeAggregateComplianceByConformancePacksRequestDescribeAggregateComplianceByConformancePacksPaginateTypeDef = TypedDict(
    "DescribeAggregateComplianceByConformancePacksRequestDescribeAggregateComplianceByConformancePacksPaginateTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "Filters": NotRequired[AggregateConformancePackComplianceFiltersTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeAggregationAuthorizationsRequestDescribeAggregationAuthorizationsPaginateTypeDef = (
    TypedDict(
        "DescribeAggregationAuthorizationsRequestDescribeAggregationAuthorizationsPaginateTypeDef",
        {
            "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
        },
    )
)
DescribeComplianceByConfigRuleRequestDescribeComplianceByConfigRulePaginateTypeDef = TypedDict(
    "DescribeComplianceByConfigRuleRequestDescribeComplianceByConfigRulePaginateTypeDef",
    {
        "ConfigRuleNames": NotRequired[Sequence[str]],
        "ComplianceTypes": NotRequired[Sequence[ComplianceTypeType]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeComplianceByResourceRequestDescribeComplianceByResourcePaginateTypeDef = TypedDict(
    "DescribeComplianceByResourceRequestDescribeComplianceByResourcePaginateTypeDef",
    {
        "ResourceType": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ComplianceTypes": NotRequired[Sequence[ComplianceTypeType]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeConfigRuleEvaluationStatusRequestDescribeConfigRuleEvaluationStatusPaginateTypeDef = TypedDict(
    "DescribeConfigRuleEvaluationStatusRequestDescribeConfigRuleEvaluationStatusPaginateTypeDef",
    {
        "ConfigRuleNames": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeConfigurationAggregatorSourcesStatusRequestDescribeConfigurationAggregatorSourcesStatusPaginateTypeDef = TypedDict(
    "DescribeConfigurationAggregatorSourcesStatusRequestDescribeConfigurationAggregatorSourcesStatusPaginateTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "UpdateStatus": NotRequired[Sequence[AggregatedSourceStatusTypeType]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeConfigurationAggregatorsRequestDescribeConfigurationAggregatorsPaginateTypeDef = TypedDict(
    "DescribeConfigurationAggregatorsRequestDescribeConfigurationAggregatorsPaginateTypeDef",
    {
        "ConfigurationAggregatorNames": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeConformancePackStatusRequestDescribeConformancePackStatusPaginateTypeDef = TypedDict(
    "DescribeConformancePackStatusRequestDescribeConformancePackStatusPaginateTypeDef",
    {
        "ConformancePackNames": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeConformancePacksRequestDescribeConformancePacksPaginateTypeDef = TypedDict(
    "DescribeConformancePacksRequestDescribeConformancePacksPaginateTypeDef",
    {
        "ConformancePackNames": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeOrganizationConfigRuleStatusesRequestDescribeOrganizationConfigRuleStatusesPaginateTypeDef = TypedDict(
    "DescribeOrganizationConfigRuleStatusesRequestDescribeOrganizationConfigRuleStatusesPaginateTypeDef",
    {
        "OrganizationConfigRuleNames": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeOrganizationConfigRulesRequestDescribeOrganizationConfigRulesPaginateTypeDef = TypedDict(
    "DescribeOrganizationConfigRulesRequestDescribeOrganizationConfigRulesPaginateTypeDef",
    {
        "OrganizationConfigRuleNames": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeOrganizationConformancePackStatusesRequestDescribeOrganizationConformancePackStatusesPaginateTypeDef = TypedDict(
    "DescribeOrganizationConformancePackStatusesRequestDescribeOrganizationConformancePackStatusesPaginateTypeDef",
    {
        "OrganizationConformancePackNames": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeOrganizationConformancePacksRequestDescribeOrganizationConformancePacksPaginateTypeDef = TypedDict(
    "DescribeOrganizationConformancePacksRequestDescribeOrganizationConformancePacksPaginateTypeDef",
    {
        "OrganizationConformancePackNames": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribePendingAggregationRequestsRequestDescribePendingAggregationRequestsPaginateTypeDef = TypedDict(
    "DescribePendingAggregationRequestsRequestDescribePendingAggregationRequestsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeRemediationExecutionStatusRequestDescribeRemediationExecutionStatusPaginateTypeDef = TypedDict(
    "DescribeRemediationExecutionStatusRequestDescribeRemediationExecutionStatusPaginateTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceKeys": NotRequired[Sequence[ResourceKeyTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeRetentionConfigurationsRequestDescribeRetentionConfigurationsPaginateTypeDef = TypedDict(
    "DescribeRetentionConfigurationsRequestDescribeRetentionConfigurationsPaginateTypeDef",
    {
        "RetentionConfigurationNames": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetAggregateComplianceDetailsByConfigRuleRequestGetAggregateComplianceDetailsByConfigRulePaginateTypeDef = TypedDict(
    "GetAggregateComplianceDetailsByConfigRuleRequestGetAggregateComplianceDetailsByConfigRulePaginateTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ConfigRuleName": str,
        "AccountId": str,
        "AwsRegion": str,
        "ComplianceType": NotRequired[ComplianceTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetComplianceDetailsByConfigRuleRequestGetComplianceDetailsByConfigRulePaginateTypeDef = TypedDict(
    "GetComplianceDetailsByConfigRuleRequestGetComplianceDetailsByConfigRulePaginateTypeDef",
    {
        "ConfigRuleName": str,
        "ComplianceTypes": NotRequired[Sequence[ComplianceTypeType]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetComplianceDetailsByResourceRequestGetComplianceDetailsByResourcePaginateTypeDef = TypedDict(
    "GetComplianceDetailsByResourceRequestGetComplianceDetailsByResourcePaginateTypeDef",
    {
        "ResourceType": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ComplianceTypes": NotRequired[Sequence[ComplianceTypeType]],
        "ResourceEvaluationId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetConformancePackComplianceSummaryRequestGetConformancePackComplianceSummaryPaginateTypeDef = TypedDict(
    "GetConformancePackComplianceSummaryRequestGetConformancePackComplianceSummaryPaginateTypeDef",
    {
        "ConformancePackNames": Sequence[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDiscoveredResourcesRequestListDiscoveredResourcesPaginateTypeDef = TypedDict(
    "ListDiscoveredResourcesRequestListDiscoveredResourcesPaginateTypeDef",
    {
        "resourceType": ResourceTypeType,
        "resourceIds": NotRequired[Sequence[str]],
        "resourceName": NotRequired[str],
        "includeDeletedResources": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTagsForResourceRequestListTagsForResourcePaginateTypeDef = TypedDict(
    "ListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    {
        "ResourceArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SelectAggregateResourceConfigRequestSelectAggregateResourceConfigPaginateTypeDef = TypedDict(
    "SelectAggregateResourceConfigRequestSelectAggregateResourceConfigPaginateTypeDef",
    {
        "Expression": str,
        "ConfigurationAggregatorName": str,
        "MaxResults": NotRequired[int],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SelectResourceConfigRequestSelectResourceConfigPaginateTypeDef = TypedDict(
    "SelectResourceConfigRequestSelectResourceConfigPaginateTypeDef",
    {
        "Expression": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeConfigRulesRequestDescribeConfigRulesPaginateTypeDef = TypedDict(
    "DescribeConfigRulesRequestDescribeConfigRulesPaginateTypeDef",
    {
        "ConfigRuleNames": NotRequired[Sequence[str]],
        "Filters": NotRequired[DescribeConfigRulesFiltersTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeConfigRulesRequestRequestTypeDef = TypedDict(
    "DescribeConfigRulesRequestRequestTypeDef",
    {
        "ConfigRuleNames": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[DescribeConfigRulesFiltersTypeDef],
    },
)
DescribeOrganizationConfigRuleStatusesResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigRuleStatusesResponseTypeDef",
    {
        "OrganizationConfigRuleStatuses": List[OrganizationConfigRuleStatusTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeOrganizationConformancePackStatusesResponseTypeDef = TypedDict(
    "DescribeOrganizationConformancePackStatusesResponseTypeDef",
    {
        "OrganizationConformancePackStatuses": List[OrganizationConformancePackStatusTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribePendingAggregationRequestsResponseTypeDef = TypedDict(
    "DescribePendingAggregationRequestsResponseTypeDef",
    {
        "PendingAggregationRequests": List[PendingAggregationRequestTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeRemediationExceptionsResponseTypeDef = TypedDict(
    "DescribeRemediationExceptionsResponseTypeDef",
    {
        "RemediationExceptions": List[RemediationExceptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
FailedRemediationExceptionBatchTypeDef = TypedDict(
    "FailedRemediationExceptionBatchTypeDef",
    {
        "FailureMessage": NotRequired[str],
        "FailedItems": NotRequired[List[RemediationExceptionTypeDef]],
    },
)
DescribeRetentionConfigurationsResponseTypeDef = TypedDict(
    "DescribeRetentionConfigurationsResponseTypeDef",
    {
        "RetentionConfigurations": List[RetentionConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PutRetentionConfigurationResponseTypeDef = TypedDict(
    "PutRetentionConfigurationResponseTypeDef",
    {
        "RetentionConfiguration": RetentionConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutEvaluationsResponseTypeDef = TypedDict(
    "PutEvaluationsResponseTypeDef",
    {
        "FailedEvaluations": List[EvaluationOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EvaluationResultIdentifierTypeDef = TypedDict(
    "EvaluationResultIdentifierTypeDef",
    {
        "EvaluationResultQualifier": NotRequired[EvaluationResultQualifierTypeDef],
        "OrderingTimestamp": NotRequired[datetime],
        "ResourceEvaluationId": NotRequired[str],
    },
)
EvaluationTypeDef = TypedDict(
    "EvaluationTypeDef",
    {
        "ComplianceResourceType": str,
        "ComplianceResourceId": str,
        "ComplianceType": ComplianceTypeType,
        "OrderingTimestamp": TimestampTypeDef,
        "Annotation": NotRequired[str],
    },
)
ExternalEvaluationTypeDef = TypedDict(
    "ExternalEvaluationTypeDef",
    {
        "ComplianceResourceType": str,
        "ComplianceResourceId": str,
        "ComplianceType": ComplianceTypeType,
        "OrderingTimestamp": TimestampTypeDef,
        "Annotation": NotRequired[str],
    },
)
GetResourceConfigHistoryRequestGetResourceConfigHistoryPaginateTypeDef = TypedDict(
    "GetResourceConfigHistoryRequestGetResourceConfigHistoryPaginateTypeDef",
    {
        "resourceType": ResourceTypeType,
        "resourceId": str,
        "laterTime": NotRequired[TimestampTypeDef],
        "earlierTime": NotRequired[TimestampTypeDef],
        "chronologicalOrder": NotRequired[ChronologicalOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetResourceConfigHistoryRequestRequestTypeDef = TypedDict(
    "GetResourceConfigHistoryRequestRequestTypeDef",
    {
        "resourceType": ResourceTypeType,
        "resourceId": str,
        "laterTime": NotRequired[TimestampTypeDef],
        "earlierTime": NotRequired[TimestampTypeDef],
        "chronologicalOrder": NotRequired[ChronologicalOrderType],
        "limit": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
PutRemediationExceptionsRequestRequestTypeDef = TypedDict(
    "PutRemediationExceptionsRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
        "ResourceKeys": Sequence[RemediationExceptionResourceKeyTypeDef],
        "Message": NotRequired[str],
        "ExpirationTime": NotRequired[TimestampTypeDef],
    },
)
TimeWindowTypeDef = TypedDict(
    "TimeWindowTypeDef",
    {
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
    },
)
ExclusionByResourceTypesUnionTypeDef = Union[
    ExclusionByResourceTypesTypeDef, ExclusionByResourceTypesOutputTypeDef
]
ExecutionControlsTypeDef = TypedDict(
    "ExecutionControlsTypeDef",
    {
        "SsmControls": NotRequired[SsmControlsTypeDef],
    },
)
QueryInfoTypeDef = TypedDict(
    "QueryInfoTypeDef",
    {
        "SelectFields": NotRequired[List[FieldInfoTypeDef]],
    },
)
GetAggregateDiscoveredResourceCountsRequestRequestTypeDef = TypedDict(
    "GetAggregateDiscoveredResourceCountsRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "Filters": NotRequired[ResourceCountFiltersTypeDef],
        "GroupByKey": NotRequired[ResourceCountGroupKeyType],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetAggregateDiscoveredResourceCountsResponseTypeDef = TypedDict(
    "GetAggregateDiscoveredResourceCountsResponseTypeDef",
    {
        "TotalDiscoveredResources": int,
        "GroupByKey": str,
        "GroupedResourceCounts": List[GroupedResourceCountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetDiscoveredResourceCountsResponseTypeDef = TypedDict(
    "GetDiscoveredResourceCountsResponseTypeDef",
    {
        "totalDiscoveredResources": int,
        "resourceCounts": List[ResourceCountTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetOrganizationConfigRuleDetailedStatusRequestGetOrganizationConfigRuleDetailedStatusPaginateTypeDef = TypedDict(
    "GetOrganizationConfigRuleDetailedStatusRequestGetOrganizationConfigRuleDetailedStatusPaginateTypeDef",
    {
        "OrganizationConfigRuleName": str,
        "Filters": NotRequired[StatusDetailFiltersTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetOrganizationConfigRuleDetailedStatusRequestRequestTypeDef = TypedDict(
    "GetOrganizationConfigRuleDetailedStatusRequestRequestTypeDef",
    {
        "OrganizationConfigRuleName": str,
        "Filters": NotRequired[StatusDetailFiltersTypeDef],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetOrganizationConfigRuleDetailedStatusResponseTypeDef = TypedDict(
    "GetOrganizationConfigRuleDetailedStatusResponseTypeDef",
    {
        "OrganizationConfigRuleDetailedStatus": List[MemberAccountStatusTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetOrganizationConformancePackDetailedStatusRequestGetOrganizationConformancePackDetailedStatusPaginateTypeDef = TypedDict(
    "GetOrganizationConformancePackDetailedStatusRequestGetOrganizationConformancePackDetailedStatusPaginateTypeDef",
    {
        "OrganizationConformancePackName": str,
        "Filters": NotRequired[OrganizationResourceDetailedStatusFiltersTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetOrganizationConformancePackDetailedStatusRequestRequestTypeDef = TypedDict(
    "GetOrganizationConformancePackDetailedStatusRequestRequestTypeDef",
    {
        "OrganizationConformancePackName": str,
        "Filters": NotRequired[OrganizationResourceDetailedStatusFiltersTypeDef],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetOrganizationConformancePackDetailedStatusResponseTypeDef = TypedDict(
    "GetOrganizationConformancePackDetailedStatusResponseTypeDef",
    {
        "OrganizationConformancePackDetailedStatuses": List[
            OrganizationConformancePackDetailedStatusTypeDef
        ],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetResourceEvaluationSummaryResponseTypeDef = TypedDict(
    "GetResourceEvaluationSummaryResponseTypeDef",
    {
        "ResourceEvaluationId": str,
        "EvaluationMode": EvaluationModeType,
        "EvaluationStatus": EvaluationStatusTypeDef,
        "EvaluationStartTimestamp": datetime,
        "Compliance": ComplianceTypeType,
        "EvaluationContext": EvaluationContextTypeDef,
        "ResourceDetails": ResourceDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartResourceEvaluationRequestRequestTypeDef = TypedDict(
    "StartResourceEvaluationRequestRequestTypeDef",
    {
        "ResourceDetails": ResourceDetailsTypeDef,
        "EvaluationMode": EvaluationModeType,
        "EvaluationContext": NotRequired[EvaluationContextTypeDef],
        "EvaluationTimeout": NotRequired[int],
        "ClientToken": NotRequired[str],
    },
)
GetStoredQueryResponseTypeDef = TypedDict(
    "GetStoredQueryResponseTypeDef",
    {
        "StoredQuery": StoredQueryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAggregateDiscoveredResourcesRequestListAggregateDiscoveredResourcesPaginateTypeDef = TypedDict(
    "ListAggregateDiscoveredResourcesRequestListAggregateDiscoveredResourcesPaginateTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ResourceType": ResourceTypeType,
        "Filters": NotRequired[ResourceFiltersTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAggregateDiscoveredResourcesRequestRequestTypeDef = TypedDict(
    "ListAggregateDiscoveredResourcesRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "ResourceType": ResourceTypeType,
        "Filters": NotRequired[ResourceFiltersTypeDef],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListDiscoveredResourcesResponseTypeDef = TypedDict(
    "ListDiscoveredResourcesResponseTypeDef",
    {
        "resourceIdentifiers": List[ResourceIdentifierTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListResourceEvaluationsResponseTypeDef = TypedDict(
    "ListResourceEvaluationsResponseTypeDef",
    {
        "ResourceEvaluations": List[ResourceEvaluationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListStoredQueriesResponseTypeDef = TypedDict(
    "ListStoredQueriesResponseTypeDef",
    {
        "StoredQueryMetadata": List[StoredQueryMetadataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PutAggregationAuthorizationRequestRequestTypeDef = TypedDict(
    "PutAggregationAuthorizationRequestRequestTypeDef",
    {
        "AuthorizedAccountId": str,
        "AuthorizedAwsRegion": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
PutStoredQueryRequestRequestTypeDef = TypedDict(
    "PutStoredQueryRequestRequestTypeDef",
    {
        "StoredQuery": StoredQueryTypeDef,
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
OrganizationConfigRuleTypeDef = TypedDict(
    "OrganizationConfigRuleTypeDef",
    {
        "OrganizationConfigRuleName": str,
        "OrganizationConfigRuleArn": str,
        "OrganizationManagedRuleMetadata": NotRequired[
            OrganizationManagedRuleMetadataOutputTypeDef
        ],
        "OrganizationCustomRuleMetadata": NotRequired[OrganizationCustomRuleMetadataOutputTypeDef],
        "ExcludedAccounts": NotRequired[List[str]],
        "LastUpdateTime": NotRequired[datetime],
        "OrganizationCustomPolicyRuleMetadata": NotRequired[
            OrganizationCustomPolicyRuleMetadataNoPolicyTypeDef
        ],
    },
)
PutOrganizationConfigRuleRequestRequestTypeDef = TypedDict(
    "PutOrganizationConfigRuleRequestRequestTypeDef",
    {
        "OrganizationConfigRuleName": str,
        "OrganizationManagedRuleMetadata": NotRequired[OrganizationManagedRuleMetadataTypeDef],
        "OrganizationCustomRuleMetadata": NotRequired[OrganizationCustomRuleMetadataTypeDef],
        "ExcludedAccounts": NotRequired[Sequence[str]],
        "OrganizationCustomPolicyRuleMetadata": NotRequired[
            OrganizationCustomPolicyRuleMetadataTypeDef
        ],
    },
)
RecordingGroupOutputTypeDef = TypedDict(
    "RecordingGroupOutputTypeDef",
    {
        "allSupported": NotRequired[bool],
        "includeGlobalResourceTypes": NotRequired[bool],
        "resourceTypes": NotRequired[List[ResourceTypeType]],
        "exclusionByResourceTypes": NotRequired[ExclusionByResourceTypesOutputTypeDef],
        "recordingStrategy": NotRequired[RecordingStrategyTypeDef],
    },
)
RecordingModeOutputTypeDef = TypedDict(
    "RecordingModeOutputTypeDef",
    {
        "recordingFrequency": RecordingFrequencyType,
        "recordingModeOverrides": NotRequired[List[RecordingModeOverrideOutputTypeDef]],
    },
)
RecordingModeOverrideUnionTypeDef = Union[
    RecordingModeOverrideTypeDef, RecordingModeOverrideOutputTypeDef
]
RemediationExecutionStatusTypeDef = TypedDict(
    "RemediationExecutionStatusTypeDef",
    {
        "ResourceKey": NotRequired[ResourceKeyTypeDef],
        "State": NotRequired[RemediationExecutionStateType],
        "StepDetails": NotRequired[List[RemediationExecutionStepTypeDef]],
        "InvocationTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
    },
)
RemediationParameterValueOutputTypeDef = TypedDict(
    "RemediationParameterValueOutputTypeDef",
    {
        "ResourceValue": NotRequired[ResourceValueTypeDef],
        "StaticValue": NotRequired[StaticValueOutputTypeDef],
    },
)
ScopeUnionTypeDef = Union[ScopeTypeDef, ScopeOutputTypeDef]
SourceOutputTypeDef = TypedDict(
    "SourceOutputTypeDef",
    {
        "Owner": OwnerType,
        "SourceIdentifier": NotRequired[str],
        "SourceDetails": NotRequired[List[SourceDetailTypeDef]],
        "CustomPolicyDetails": NotRequired[CustomPolicyDetailsTypeDef],
    },
)
SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "Owner": OwnerType,
        "SourceIdentifier": NotRequired[str],
        "SourceDetails": NotRequired[Sequence[SourceDetailTypeDef]],
        "CustomPolicyDetails": NotRequired[CustomPolicyDetailsTypeDef],
    },
)
StaticValueUnionTypeDef = Union[StaticValueTypeDef, StaticValueOutputTypeDef]
PutConfigurationAggregatorRequestRequestTypeDef = TypedDict(
    "PutConfigurationAggregatorRequestRequestTypeDef",
    {
        "ConfigurationAggregatorName": str,
        "AccountAggregationSources": NotRequired[Sequence[AccountAggregationSourceUnionTypeDef]],
        "OrganizationAggregationSource": NotRequired[OrganizationAggregationSourceTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
DescribeAggregateComplianceByConformancePacksResponseTypeDef = TypedDict(
    "DescribeAggregateComplianceByConformancePacksResponseTypeDef",
    {
        "AggregateComplianceByConformancePacks": List[AggregateComplianceByConformancePackTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetAggregateConformancePackComplianceSummaryResponseTypeDef = TypedDict(
    "GetAggregateConformancePackComplianceSummaryResponseTypeDef",
    {
        "AggregateConformancePackComplianceSummaries": List[
            AggregateConformancePackComplianceSummaryTypeDef
        ],
        "GroupByKey": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
AggregateComplianceCountTypeDef = TypedDict(
    "AggregateComplianceCountTypeDef",
    {
        "GroupName": NotRequired[str],
        "ComplianceSummary": NotRequired[ComplianceSummaryTypeDef],
    },
)
ComplianceSummaryByResourceTypeTypeDef = TypedDict(
    "ComplianceSummaryByResourceTypeTypeDef",
    {
        "ResourceType": NotRequired[str],
        "ComplianceSummary": NotRequired[ComplianceSummaryTypeDef],
    },
)
GetComplianceSummaryByConfigRuleResponseTypeDef = TypedDict(
    "GetComplianceSummaryByConfigRuleResponseTypeDef",
    {
        "ComplianceSummary": ComplianceSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AggregateComplianceByConfigRuleTypeDef = TypedDict(
    "AggregateComplianceByConfigRuleTypeDef",
    {
        "ConfigRuleName": NotRequired[str],
        "Compliance": NotRequired[ComplianceTypeDef],
        "AccountId": NotRequired[str],
        "AwsRegion": NotRequired[str],
    },
)
ComplianceByConfigRuleTypeDef = TypedDict(
    "ComplianceByConfigRuleTypeDef",
    {
        "ConfigRuleName": NotRequired[str],
        "Compliance": NotRequired[ComplianceTypeDef],
    },
)
ComplianceByResourceTypeDef = TypedDict(
    "ComplianceByResourceTypeDef",
    {
        "ResourceType": NotRequired[str],
        "ResourceId": NotRequired[str],
        "Compliance": NotRequired[ComplianceTypeDef],
    },
)
DescribeDeliveryChannelsResponseTypeDef = TypedDict(
    "DescribeDeliveryChannelsResponseTypeDef",
    {
        "DeliveryChannels": List[DeliveryChannelTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutDeliveryChannelRequestRequestTypeDef = TypedDict(
    "PutDeliveryChannelRequestRequestTypeDef",
    {
        "DeliveryChannel": DeliveryChannelTypeDef,
    },
)
DescribeDeliveryChannelStatusResponseTypeDef = TypedDict(
    "DescribeDeliveryChannelStatusResponseTypeDef",
    {
        "DeliveryChannelsStatus": List[DeliveryChannelStatusTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeConfigurationAggregatorsResponseTypeDef = TypedDict(
    "DescribeConfigurationAggregatorsResponseTypeDef",
    {
        "ConfigurationAggregators": List[ConfigurationAggregatorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PutConfigurationAggregatorResponseTypeDef = TypedDict(
    "PutConfigurationAggregatorResponseTypeDef",
    {
        "ConfigurationAggregator": ConfigurationAggregatorTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAggregateResourceConfigResponseTypeDef = TypedDict(
    "GetAggregateResourceConfigResponseTypeDef",
    {
        "ConfigurationItem": ConfigurationItemTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResourceConfigHistoryResponseTypeDef = TypedDict(
    "GetResourceConfigHistoryResponseTypeDef",
    {
        "configurationItems": List[ConfigurationItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeOrganizationConformancePacksResponseTypeDef = TypedDict(
    "DescribeOrganizationConformancePacksResponseTypeDef",
    {
        "OrganizationConformancePacks": List[OrganizationConformancePackTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeConformancePacksResponseTypeDef = TypedDict(
    "DescribeConformancePacksResponseTypeDef",
    {
        "ConformancePackDetails": List[ConformancePackDetailTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DeleteRemediationExceptionsResponseTypeDef = TypedDict(
    "DeleteRemediationExceptionsResponseTypeDef",
    {
        "FailedBatches": List[FailedDeleteRemediationExceptionsBatchTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutRemediationExceptionsResponseTypeDef = TypedDict(
    "PutRemediationExceptionsResponseTypeDef",
    {
        "FailedBatches": List[FailedRemediationExceptionBatchTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AggregateEvaluationResultTypeDef = TypedDict(
    "AggregateEvaluationResultTypeDef",
    {
        "EvaluationResultIdentifier": NotRequired[EvaluationResultIdentifierTypeDef],
        "ComplianceType": NotRequired[ComplianceTypeType],
        "ResultRecordedTime": NotRequired[datetime],
        "ConfigRuleInvokedTime": NotRequired[datetime],
        "Annotation": NotRequired[str],
        "AccountId": NotRequired[str],
        "AwsRegion": NotRequired[str],
    },
)
ConformancePackEvaluationResultTypeDef = TypedDict(
    "ConformancePackEvaluationResultTypeDef",
    {
        "ComplianceType": ConformancePackComplianceTypeType,
        "EvaluationResultIdentifier": EvaluationResultIdentifierTypeDef,
        "ConfigRuleInvokedTime": datetime,
        "ResultRecordedTime": datetime,
        "Annotation": NotRequired[str],
    },
)
EvaluationResultTypeDef = TypedDict(
    "EvaluationResultTypeDef",
    {
        "EvaluationResultIdentifier": NotRequired[EvaluationResultIdentifierTypeDef],
        "ComplianceType": NotRequired[ComplianceTypeType],
        "ResultRecordedTime": NotRequired[datetime],
        "ConfigRuleInvokedTime": NotRequired[datetime],
        "Annotation": NotRequired[str],
        "ResultToken": NotRequired[str],
    },
)
EvaluationUnionTypeDef = Union[EvaluationTypeDef, EvaluationOutputTypeDef]
PutExternalEvaluationRequestRequestTypeDef = TypedDict(
    "PutExternalEvaluationRequestRequestTypeDef",
    {
        "ConfigRuleName": str,
        "ExternalEvaluation": ExternalEvaluationTypeDef,
    },
)
ResourceEvaluationFiltersTypeDef = TypedDict(
    "ResourceEvaluationFiltersTypeDef",
    {
        "EvaluationMode": NotRequired[EvaluationModeType],
        "TimeWindow": NotRequired[TimeWindowTypeDef],
        "EvaluationContextIdentifier": NotRequired[str],
    },
)
RecordingGroupTypeDef = TypedDict(
    "RecordingGroupTypeDef",
    {
        "allSupported": NotRequired[bool],
        "includeGlobalResourceTypes": NotRequired[bool],
        "resourceTypes": NotRequired[Sequence[ResourceTypeType]],
        "exclusionByResourceTypes": NotRequired[ExclusionByResourceTypesUnionTypeDef],
        "recordingStrategy": NotRequired[RecordingStrategyTypeDef],
    },
)
SelectAggregateResourceConfigResponseTypeDef = TypedDict(
    "SelectAggregateResourceConfigResponseTypeDef",
    {
        "Results": List[str],
        "QueryInfo": QueryInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
SelectResourceConfigResponseTypeDef = TypedDict(
    "SelectResourceConfigResponseTypeDef",
    {
        "Results": List[str],
        "QueryInfo": QueryInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeOrganizationConfigRulesResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigRulesResponseTypeDef",
    {
        "OrganizationConfigRules": List[OrganizationConfigRuleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ConfigurationRecorderOutputTypeDef = TypedDict(
    "ConfigurationRecorderOutputTypeDef",
    {
        "name": NotRequired[str],
        "roleARN": NotRequired[str],
        "recordingGroup": NotRequired[RecordingGroupOutputTypeDef],
        "recordingMode": NotRequired[RecordingModeOutputTypeDef],
    },
)
RecordingModeTypeDef = TypedDict(
    "RecordingModeTypeDef",
    {
        "recordingFrequency": RecordingFrequencyType,
        "recordingModeOverrides": NotRequired[Sequence[RecordingModeOverrideUnionTypeDef]],
    },
)
DescribeRemediationExecutionStatusResponseTypeDef = TypedDict(
    "DescribeRemediationExecutionStatusResponseTypeDef",
    {
        "RemediationExecutionStatuses": List[RemediationExecutionStatusTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
RemediationConfigurationOutputTypeDef = TypedDict(
    "RemediationConfigurationOutputTypeDef",
    {
        "ConfigRuleName": str,
        "TargetType": Literal["SSM_DOCUMENT"],
        "TargetId": str,
        "TargetVersion": NotRequired[str],
        "Parameters": NotRequired[Dict[str, RemediationParameterValueOutputTypeDef]],
        "ResourceType": NotRequired[str],
        "Automatic": NotRequired[bool],
        "ExecutionControls": NotRequired[ExecutionControlsTypeDef],
        "MaximumAutomaticAttempts": NotRequired[int],
        "RetryAttemptSeconds": NotRequired[int],
        "Arn": NotRequired[str],
        "CreatedByService": NotRequired[str],
    },
)
ConfigRuleOutputTypeDef = TypedDict(
    "ConfigRuleOutputTypeDef",
    {
        "Source": SourceOutputTypeDef,
        "ConfigRuleName": NotRequired[str],
        "ConfigRuleArn": NotRequired[str],
        "ConfigRuleId": NotRequired[str],
        "Description": NotRequired[str],
        "Scope": NotRequired[ScopeOutputTypeDef],
        "InputParameters": NotRequired[str],
        "MaximumExecutionFrequency": NotRequired[MaximumExecutionFrequencyType],
        "ConfigRuleState": NotRequired[ConfigRuleStateType],
        "CreatedBy": NotRequired[str],
        "EvaluationModes": NotRequired[List[EvaluationModeConfigurationTypeDef]],
    },
)
SourceUnionTypeDef = Union[SourceTypeDef, SourceOutputTypeDef]
RemediationParameterValueTypeDef = TypedDict(
    "RemediationParameterValueTypeDef",
    {
        "ResourceValue": NotRequired[ResourceValueTypeDef],
        "StaticValue": NotRequired[StaticValueUnionTypeDef],
    },
)
GetAggregateConfigRuleComplianceSummaryResponseTypeDef = TypedDict(
    "GetAggregateConfigRuleComplianceSummaryResponseTypeDef",
    {
        "GroupByKey": str,
        "AggregateComplianceCounts": List[AggregateComplianceCountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetComplianceSummaryByResourceTypeResponseTypeDef = TypedDict(
    "GetComplianceSummaryByResourceTypeResponseTypeDef",
    {
        "ComplianceSummariesByResourceType": List[ComplianceSummaryByResourceTypeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAggregateComplianceByConfigRulesResponseTypeDef = TypedDict(
    "DescribeAggregateComplianceByConfigRulesResponseTypeDef",
    {
        "AggregateComplianceByConfigRules": List[AggregateComplianceByConfigRuleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeComplianceByConfigRuleResponseTypeDef = TypedDict(
    "DescribeComplianceByConfigRuleResponseTypeDef",
    {
        "ComplianceByConfigRules": List[ComplianceByConfigRuleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeComplianceByResourceResponseTypeDef = TypedDict(
    "DescribeComplianceByResourceResponseTypeDef",
    {
        "ComplianceByResources": List[ComplianceByResourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetAggregateComplianceDetailsByConfigRuleResponseTypeDef = TypedDict(
    "GetAggregateComplianceDetailsByConfigRuleResponseTypeDef",
    {
        "AggregateEvaluationResults": List[AggregateEvaluationResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetConformancePackComplianceDetailsResponseTypeDef = TypedDict(
    "GetConformancePackComplianceDetailsResponseTypeDef",
    {
        "ConformancePackName": str,
        "ConformancePackRuleEvaluationResults": List[ConformancePackEvaluationResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetComplianceDetailsByConfigRuleResponseTypeDef = TypedDict(
    "GetComplianceDetailsByConfigRuleResponseTypeDef",
    {
        "EvaluationResults": List[EvaluationResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetComplianceDetailsByResourceResponseTypeDef = TypedDict(
    "GetComplianceDetailsByResourceResponseTypeDef",
    {
        "EvaluationResults": List[EvaluationResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PutEvaluationsRequestRequestTypeDef = TypedDict(
    "PutEvaluationsRequestRequestTypeDef",
    {
        "ResultToken": str,
        "Evaluations": NotRequired[Sequence[EvaluationUnionTypeDef]],
        "TestMode": NotRequired[bool],
    },
)
ListResourceEvaluationsRequestListResourceEvaluationsPaginateTypeDef = TypedDict(
    "ListResourceEvaluationsRequestListResourceEvaluationsPaginateTypeDef",
    {
        "Filters": NotRequired[ResourceEvaluationFiltersTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResourceEvaluationsRequestRequestTypeDef = TypedDict(
    "ListResourceEvaluationsRequestRequestTypeDef",
    {
        "Filters": NotRequired[ResourceEvaluationFiltersTypeDef],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
RecordingGroupUnionTypeDef = Union[RecordingGroupTypeDef, RecordingGroupOutputTypeDef]
DescribeConfigurationRecordersResponseTypeDef = TypedDict(
    "DescribeConfigurationRecordersResponseTypeDef",
    {
        "ConfigurationRecorders": List[ConfigurationRecorderOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RecordingModeUnionTypeDef = Union[RecordingModeTypeDef, RecordingModeOutputTypeDef]
DescribeRemediationConfigurationsResponseTypeDef = TypedDict(
    "DescribeRemediationConfigurationsResponseTypeDef",
    {
        "RemediationConfigurations": List[RemediationConfigurationOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FailedRemediationBatchTypeDef = TypedDict(
    "FailedRemediationBatchTypeDef",
    {
        "FailureMessage": NotRequired[str],
        "FailedItems": NotRequired[List[RemediationConfigurationOutputTypeDef]],
    },
)
DescribeConfigRulesResponseTypeDef = TypedDict(
    "DescribeConfigRulesResponseTypeDef",
    {
        "ConfigRules": List[ConfigRuleOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ConfigRuleTypeDef = TypedDict(
    "ConfigRuleTypeDef",
    {
        "Source": SourceUnionTypeDef,
        "ConfigRuleName": NotRequired[str],
        "ConfigRuleArn": NotRequired[str],
        "ConfigRuleId": NotRequired[str],
        "Description": NotRequired[str],
        "Scope": NotRequired[ScopeUnionTypeDef],
        "InputParameters": NotRequired[str],
        "MaximumExecutionFrequency": NotRequired[MaximumExecutionFrequencyType],
        "ConfigRuleState": NotRequired[ConfigRuleStateType],
        "CreatedBy": NotRequired[str],
        "EvaluationModes": NotRequired[Sequence[EvaluationModeConfigurationTypeDef]],
    },
)
RemediationParameterValueUnionTypeDef = Union[
    RemediationParameterValueTypeDef, RemediationParameterValueOutputTypeDef
]
ConfigurationRecorderTypeDef = TypedDict(
    "ConfigurationRecorderTypeDef",
    {
        "name": NotRequired[str],
        "roleARN": NotRequired[str],
        "recordingGroup": NotRequired[RecordingGroupUnionTypeDef],
        "recordingMode": NotRequired[RecordingModeUnionTypeDef],
    },
)
PutRemediationConfigurationsResponseTypeDef = TypedDict(
    "PutRemediationConfigurationsResponseTypeDef",
    {
        "FailedBatches": List[FailedRemediationBatchTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutConfigRuleRequestRequestTypeDef = TypedDict(
    "PutConfigRuleRequestRequestTypeDef",
    {
        "ConfigRule": ConfigRuleTypeDef,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
RemediationConfigurationTypeDef = TypedDict(
    "RemediationConfigurationTypeDef",
    {
        "ConfigRuleName": str,
        "TargetType": Literal["SSM_DOCUMENT"],
        "TargetId": str,
        "TargetVersion": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, RemediationParameterValueUnionTypeDef]],
        "ResourceType": NotRequired[str],
        "Automatic": NotRequired[bool],
        "ExecutionControls": NotRequired[ExecutionControlsTypeDef],
        "MaximumAutomaticAttempts": NotRequired[int],
        "RetryAttemptSeconds": NotRequired[int],
        "Arn": NotRequired[str],
        "CreatedByService": NotRequired[str],
    },
)
PutConfigurationRecorderRequestRequestTypeDef = TypedDict(
    "PutConfigurationRecorderRequestRequestTypeDef",
    {
        "ConfigurationRecorder": ConfigurationRecorderTypeDef,
    },
)
RemediationConfigurationUnionTypeDef = Union[
    RemediationConfigurationTypeDef, RemediationConfigurationOutputTypeDef
]
PutRemediationConfigurationsRequestRequestTypeDef = TypedDict(
    "PutRemediationConfigurationsRequestRequestTypeDef",
    {
        "RemediationConfigurations": Sequence[RemediationConfigurationUnionTypeDef],
    },
)
