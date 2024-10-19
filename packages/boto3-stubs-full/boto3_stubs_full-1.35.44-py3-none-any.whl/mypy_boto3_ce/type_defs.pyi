"""
Type annotations for ce service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/type_defs/)

Usage::

    ```python
    from mypy_boto3_ce.type_defs import AnomalyDateIntervalTypeDef

    data: AnomalyDateIntervalTypeDef = ...
    ```
"""

import sys
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    AccountScopeType,
    AnomalyFeedbackTypeType,
    AnomalySubscriptionFrequencyType,
    ApproximationDimensionType,
    ContextType,
    CostAllocationTagBackfillStatusType,
    CostAllocationTagStatusType,
    CostAllocationTagTypeType,
    CostCategoryInheritedValueDimensionNameType,
    CostCategoryRuleTypeType,
    CostCategorySplitChargeMethodType,
    CostCategoryStatusType,
    DimensionType,
    FindingReasonCodeType,
    GenerationStatusType,
    GranularityType,
    GroupDefinitionTypeType,
    LookbackPeriodInDaysType,
    MatchOptionType,
    MetricType,
    MonitorTypeType,
    NumericOperatorType,
    OfferingClassType,
    PaymentOptionType,
    PlatformDifferenceType,
    RecommendationTargetType,
    RightsizingTypeType,
    SavingsPlansDataTypeType,
    SortOrderType,
    SubscriberStatusType,
    SubscriberTypeType,
    SupportedSavingsPlansTypeType,
    TermInYearsType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AnomalyDateIntervalTypeDef",
    "AnomalyScoreTypeDef",
    "SubscriberTypeDef",
    "ImpactTypeDef",
    "RootCauseTypeDef",
    "CostAllocationTagBackfillRequestTypeDef",
    "CostAllocationTagStatusEntryTypeDef",
    "CostAllocationTagTypeDef",
    "CostCategoryInheritedValueDimensionTypeDef",
    "CostCategoryProcessingStatusTypeDef",
    "CostCategorySplitChargeRuleParameterOutputTypeDef",
    "CostCategorySplitChargeRuleParameterTypeDef",
    "CostCategoryValuesOutputTypeDef",
    "CostCategoryValuesTypeDef",
    "DateIntervalTypeDef",
    "CoverageCostTypeDef",
    "CoverageHoursTypeDef",
    "CoverageNormalizedUnitsTypeDef",
    "ResourceTagTypeDef",
    "ResponseMetadataTypeDef",
    "TagValuesOutputTypeDef",
    "DeleteAnomalyMonitorRequestRequestTypeDef",
    "DeleteAnomalySubscriptionRequestRequestTypeDef",
    "DeleteCostCategoryDefinitionRequestRequestTypeDef",
    "DescribeCostCategoryDefinitionRequestRequestTypeDef",
    "DimensionValuesOutputTypeDef",
    "DimensionValuesTypeDef",
    "DimensionValuesWithAttributesTypeDef",
    "DiskResourceUtilizationTypeDef",
    "DynamoDBCapacityDetailsTypeDef",
    "EBSResourceUtilizationTypeDef",
    "EC2InstanceDetailsTypeDef",
    "EC2ResourceDetailsTypeDef",
    "NetworkResourceUtilizationTypeDef",
    "EC2SpecificationTypeDef",
    "ESInstanceDetailsTypeDef",
    "ElastiCacheInstanceDetailsTypeDef",
    "GenerationSummaryTypeDef",
    "TotalImpactFilterTypeDef",
    "GetAnomalyMonitorsRequestRequestTypeDef",
    "GetAnomalySubscriptionsRequestRequestTypeDef",
    "GetApproximateUsageRecordsRequestRequestTypeDef",
    "GroupDefinitionTypeDef",
    "SortDefinitionTypeDef",
    "MetricValueTypeDef",
    "ReservationPurchaseRecommendationMetadataTypeDef",
    "ReservationAggregatesTypeDef",
    "RightsizingRecommendationConfigurationTypeDef",
    "RightsizingRecommendationMetadataTypeDef",
    "RightsizingRecommendationSummaryTypeDef",
    "GetSavingsPlanPurchaseRecommendationDetailsRequestRequestTypeDef",
    "SavingsPlansPurchaseRecommendationMetadataTypeDef",
    "MemoryDBInstanceDetailsTypeDef",
    "RDSInstanceDetailsTypeDef",
    "RedshiftInstanceDetailsTypeDef",
    "ListCostAllocationTagBackfillHistoryRequestRequestTypeDef",
    "ListCostAllocationTagsRequestRequestTypeDef",
    "ListCostCategoryDefinitionsRequestRequestTypeDef",
    "ListSavingsPlansPurchaseRecommendationGenerationRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ProvideAnomalyFeedbackRequestRequestTypeDef",
    "RecommendationDetailHourlyMetricsTypeDef",
    "ReservationPurchaseRecommendationSummaryTypeDef",
    "TerminateRecommendationDetailTypeDef",
    "SavingsPlansAmortizedCommitmentTypeDef",
    "SavingsPlansCoverageDataTypeDef",
    "SavingsPlansDetailsTypeDef",
    "SavingsPlansPurchaseRecommendationSummaryTypeDef",
    "SavingsPlansSavingsTypeDef",
    "SavingsPlansUtilizationTypeDef",
    "StartCostAllocationTagBackfillRequestRequestTypeDef",
    "TagValuesTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAnomalyMonitorRequestRequestTypeDef",
    "UpdateCostAllocationTagsStatusErrorTypeDef",
    "AnomalyTypeDef",
    "UpdateCostAllocationTagsStatusRequestRequestTypeDef",
    "CostCategoryReferenceTypeDef",
    "CostCategorySplitChargeRuleOutputTypeDef",
    "CostCategorySplitChargeRuleParameterUnionTypeDef",
    "CostCategoryValuesUnionTypeDef",
    "ForecastResultTypeDef",
    "CoverageTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateAnomalyMonitorResponseTypeDef",
    "CreateAnomalySubscriptionResponseTypeDef",
    "CreateCostCategoryDefinitionResponseTypeDef",
    "DeleteCostCategoryDefinitionResponseTypeDef",
    "GetApproximateUsageRecordsResponseTypeDef",
    "GetCostCategoriesResponseTypeDef",
    "GetTagsResponseTypeDef",
    "ListCostAllocationTagBackfillHistoryResponseTypeDef",
    "ListCostAllocationTagsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ProvideAnomalyFeedbackResponseTypeDef",
    "StartCostAllocationTagBackfillResponseTypeDef",
    "StartSavingsPlansPurchaseRecommendationGenerationResponseTypeDef",
    "UpdateAnomalyMonitorResponseTypeDef",
    "UpdateAnomalySubscriptionResponseTypeDef",
    "UpdateCostCategoryDefinitionResponseTypeDef",
    "ExpressionOutputTypeDef",
    "DimensionValuesUnionTypeDef",
    "GetDimensionValuesResponseTypeDef",
    "ReservedCapacityDetailsTypeDef",
    "ResourceDetailsTypeDef",
    "EC2ResourceUtilizationTypeDef",
    "ServiceSpecificationTypeDef",
    "ListSavingsPlansPurchaseRecommendationGenerationResponseTypeDef",
    "GetAnomaliesRequestRequestTypeDef",
    "GroupTypeDef",
    "ReservationUtilizationGroupTypeDef",
    "InstanceDetailsTypeDef",
    "RecommendationDetailDataTypeDef",
    "SavingsPlansCoverageTypeDef",
    "SavingsPlansPurchaseRecommendationDetailTypeDef",
    "SavingsPlansUtilizationAggregatesTypeDef",
    "SavingsPlansUtilizationByTimeTypeDef",
    "SavingsPlansUtilizationDetailTypeDef",
    "TagValuesUnionTypeDef",
    "UpdateCostAllocationTagsStatusResponseTypeDef",
    "GetAnomaliesResponseTypeDef",
    "ListCostCategoryDefinitionsResponseTypeDef",
    "CostCategorySplitChargeRuleTypeDef",
    "GetCostForecastResponseTypeDef",
    "GetUsageForecastResponseTypeDef",
    "ReservationCoverageGroupTypeDef",
    "AnomalyMonitorOutputTypeDef",
    "AnomalySubscriptionOutputTypeDef",
    "CostCategoryRuleOutputTypeDef",
    "ResourceUtilizationTypeDef",
    "ResultByTimeTypeDef",
    "UtilizationByTimeTypeDef",
    "ReservationPurchaseRecommendationDetailTypeDef",
    "GetSavingsPlanPurchaseRecommendationDetailsResponseTypeDef",
    "GetSavingsPlansCoverageResponseTypeDef",
    "SavingsPlansPurchaseRecommendationTypeDef",
    "GetSavingsPlansUtilizationResponseTypeDef",
    "GetSavingsPlansUtilizationDetailsResponseTypeDef",
    "ExpressionTypeDef",
    "CostCategorySplitChargeRuleUnionTypeDef",
    "CoverageByTimeTypeDef",
    "GetAnomalyMonitorsResponseTypeDef",
    "GetAnomalySubscriptionsResponseTypeDef",
    "CostCategoryTypeDef",
    "CurrentInstanceTypeDef",
    "TargetInstanceTypeDef",
    "GetCostAndUsageResponseTypeDef",
    "GetCostAndUsageWithResourcesResponseTypeDef",
    "GetReservationUtilizationResponseTypeDef",
    "ReservationPurchaseRecommendationTypeDef",
    "GetSavingsPlansPurchaseRecommendationResponseTypeDef",
    "ExpressionUnionTypeDef",
    "GetCostAndUsageRequestRequestTypeDef",
    "GetCostAndUsageWithResourcesRequestRequestTypeDef",
    "GetCostCategoriesRequestRequestTypeDef",
    "GetCostForecastRequestRequestTypeDef",
    "GetDimensionValuesRequestRequestTypeDef",
    "GetReservationCoverageRequestRequestTypeDef",
    "GetReservationPurchaseRecommendationRequestRequestTypeDef",
    "GetReservationUtilizationRequestRequestTypeDef",
    "GetRightsizingRecommendationRequestRequestTypeDef",
    "GetSavingsPlansCoverageRequestRequestTypeDef",
    "GetSavingsPlansPurchaseRecommendationRequestRequestTypeDef",
    "GetSavingsPlansUtilizationDetailsRequestRequestTypeDef",
    "GetSavingsPlansUtilizationRequestRequestTypeDef",
    "GetTagsRequestRequestTypeDef",
    "GetUsageForecastRequestRequestTypeDef",
    "UpdateAnomalySubscriptionRequestRequestTypeDef",
    "GetReservationCoverageResponseTypeDef",
    "DescribeCostCategoryDefinitionResponseTypeDef",
    "ModifyRecommendationDetailTypeDef",
    "GetReservationPurchaseRecommendationResponseTypeDef",
    "AnomalyMonitorTypeDef",
    "AnomalySubscriptionTypeDef",
    "CostCategoryRuleTypeDef",
    "RightsizingRecommendationTypeDef",
    "CreateAnomalyMonitorRequestRequestTypeDef",
    "CreateAnomalySubscriptionRequestRequestTypeDef",
    "CostCategoryRuleUnionTypeDef",
    "UpdateCostCategoryDefinitionRequestRequestTypeDef",
    "GetRightsizingRecommendationResponseTypeDef",
    "CreateCostCategoryDefinitionRequestRequestTypeDef",
)

AnomalyDateIntervalTypeDef = TypedDict(
    "AnomalyDateIntervalTypeDef",
    {
        "StartDate": str,
        "EndDate": NotRequired[str],
    },
)
AnomalyScoreTypeDef = TypedDict(
    "AnomalyScoreTypeDef",
    {
        "MaxScore": float,
        "CurrentScore": float,
    },
)
SubscriberTypeDef = TypedDict(
    "SubscriberTypeDef",
    {
        "Address": NotRequired[str],
        "Type": NotRequired[SubscriberTypeType],
        "Status": NotRequired[SubscriberStatusType],
    },
)
ImpactTypeDef = TypedDict(
    "ImpactTypeDef",
    {
        "MaxImpact": float,
        "TotalImpact": NotRequired[float],
        "TotalActualSpend": NotRequired[float],
        "TotalExpectedSpend": NotRequired[float],
        "TotalImpactPercentage": NotRequired[float],
    },
)
RootCauseTypeDef = TypedDict(
    "RootCauseTypeDef",
    {
        "Service": NotRequired[str],
        "Region": NotRequired[str],
        "LinkedAccount": NotRequired[str],
        "UsageType": NotRequired[str],
        "LinkedAccountName": NotRequired[str],
    },
)
CostAllocationTagBackfillRequestTypeDef = TypedDict(
    "CostAllocationTagBackfillRequestTypeDef",
    {
        "BackfillFrom": NotRequired[str],
        "RequestedAt": NotRequired[str],
        "CompletedAt": NotRequired[str],
        "BackfillStatus": NotRequired[CostAllocationTagBackfillStatusType],
        "LastUpdatedAt": NotRequired[str],
    },
)
CostAllocationTagStatusEntryTypeDef = TypedDict(
    "CostAllocationTagStatusEntryTypeDef",
    {
        "TagKey": str,
        "Status": CostAllocationTagStatusType,
    },
)
CostAllocationTagTypeDef = TypedDict(
    "CostAllocationTagTypeDef",
    {
        "TagKey": str,
        "Type": CostAllocationTagTypeType,
        "Status": CostAllocationTagStatusType,
        "LastUpdatedDate": NotRequired[str],
        "LastUsedDate": NotRequired[str],
    },
)
CostCategoryInheritedValueDimensionTypeDef = TypedDict(
    "CostCategoryInheritedValueDimensionTypeDef",
    {
        "DimensionName": NotRequired[CostCategoryInheritedValueDimensionNameType],
        "DimensionKey": NotRequired[str],
    },
)
CostCategoryProcessingStatusTypeDef = TypedDict(
    "CostCategoryProcessingStatusTypeDef",
    {
        "Component": NotRequired[Literal["COST_EXPLORER"]],
        "Status": NotRequired[CostCategoryStatusType],
    },
)
CostCategorySplitChargeRuleParameterOutputTypeDef = TypedDict(
    "CostCategorySplitChargeRuleParameterOutputTypeDef",
    {
        "Type": Literal["ALLOCATION_PERCENTAGES"],
        "Values": List[str],
    },
)
CostCategorySplitChargeRuleParameterTypeDef = TypedDict(
    "CostCategorySplitChargeRuleParameterTypeDef",
    {
        "Type": Literal["ALLOCATION_PERCENTAGES"],
        "Values": Sequence[str],
    },
)
CostCategoryValuesOutputTypeDef = TypedDict(
    "CostCategoryValuesOutputTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[List[str]],
        "MatchOptions": NotRequired[List[MatchOptionType]],
    },
)
CostCategoryValuesTypeDef = TypedDict(
    "CostCategoryValuesTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
        "MatchOptions": NotRequired[Sequence[MatchOptionType]],
    },
)
DateIntervalTypeDef = TypedDict(
    "DateIntervalTypeDef",
    {
        "Start": str,
        "End": str,
    },
)
CoverageCostTypeDef = TypedDict(
    "CoverageCostTypeDef",
    {
        "OnDemandCost": NotRequired[str],
    },
)
CoverageHoursTypeDef = TypedDict(
    "CoverageHoursTypeDef",
    {
        "OnDemandHours": NotRequired[str],
        "ReservedHours": NotRequired[str],
        "TotalRunningHours": NotRequired[str],
        "CoverageHoursPercentage": NotRequired[str],
    },
)
CoverageNormalizedUnitsTypeDef = TypedDict(
    "CoverageNormalizedUnitsTypeDef",
    {
        "OnDemandNormalizedUnits": NotRequired[str],
        "ReservedNormalizedUnits": NotRequired[str],
        "TotalRunningNormalizedUnits": NotRequired[str],
        "CoverageNormalizedUnitsPercentage": NotRequired[str],
    },
)
ResourceTagTypeDef = TypedDict(
    "ResourceTagTypeDef",
    {
        "Key": str,
        "Value": str,
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
TagValuesOutputTypeDef = TypedDict(
    "TagValuesOutputTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[List[str]],
        "MatchOptions": NotRequired[List[MatchOptionType]],
    },
)
DeleteAnomalyMonitorRequestRequestTypeDef = TypedDict(
    "DeleteAnomalyMonitorRequestRequestTypeDef",
    {
        "MonitorArn": str,
    },
)
DeleteAnomalySubscriptionRequestRequestTypeDef = TypedDict(
    "DeleteAnomalySubscriptionRequestRequestTypeDef",
    {
        "SubscriptionArn": str,
    },
)
DeleteCostCategoryDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteCostCategoryDefinitionRequestRequestTypeDef",
    {
        "CostCategoryArn": str,
    },
)
DescribeCostCategoryDefinitionRequestRequestTypeDef = TypedDict(
    "DescribeCostCategoryDefinitionRequestRequestTypeDef",
    {
        "CostCategoryArn": str,
        "EffectiveOn": NotRequired[str],
    },
)
DimensionValuesOutputTypeDef = TypedDict(
    "DimensionValuesOutputTypeDef",
    {
        "Key": NotRequired[DimensionType],
        "Values": NotRequired[List[str]],
        "MatchOptions": NotRequired[List[MatchOptionType]],
    },
)
DimensionValuesTypeDef = TypedDict(
    "DimensionValuesTypeDef",
    {
        "Key": NotRequired[DimensionType],
        "Values": NotRequired[Sequence[str]],
        "MatchOptions": NotRequired[Sequence[MatchOptionType]],
    },
)
DimensionValuesWithAttributesTypeDef = TypedDict(
    "DimensionValuesWithAttributesTypeDef",
    {
        "Value": NotRequired[str],
        "Attributes": NotRequired[Dict[str, str]],
    },
)
DiskResourceUtilizationTypeDef = TypedDict(
    "DiskResourceUtilizationTypeDef",
    {
        "DiskReadOpsPerSecond": NotRequired[str],
        "DiskWriteOpsPerSecond": NotRequired[str],
        "DiskReadBytesPerSecond": NotRequired[str],
        "DiskWriteBytesPerSecond": NotRequired[str],
    },
)
DynamoDBCapacityDetailsTypeDef = TypedDict(
    "DynamoDBCapacityDetailsTypeDef",
    {
        "CapacityUnits": NotRequired[str],
        "Region": NotRequired[str],
    },
)
EBSResourceUtilizationTypeDef = TypedDict(
    "EBSResourceUtilizationTypeDef",
    {
        "EbsReadOpsPerSecond": NotRequired[str],
        "EbsWriteOpsPerSecond": NotRequired[str],
        "EbsReadBytesPerSecond": NotRequired[str],
        "EbsWriteBytesPerSecond": NotRequired[str],
    },
)
EC2InstanceDetailsTypeDef = TypedDict(
    "EC2InstanceDetailsTypeDef",
    {
        "Family": NotRequired[str],
        "InstanceType": NotRequired[str],
        "Region": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "Platform": NotRequired[str],
        "Tenancy": NotRequired[str],
        "CurrentGeneration": NotRequired[bool],
        "SizeFlexEligible": NotRequired[bool],
    },
)
EC2ResourceDetailsTypeDef = TypedDict(
    "EC2ResourceDetailsTypeDef",
    {
        "HourlyOnDemandRate": NotRequired[str],
        "InstanceType": NotRequired[str],
        "Platform": NotRequired[str],
        "Region": NotRequired[str],
        "Sku": NotRequired[str],
        "Memory": NotRequired[str],
        "NetworkPerformance": NotRequired[str],
        "Storage": NotRequired[str],
        "Vcpu": NotRequired[str],
    },
)
NetworkResourceUtilizationTypeDef = TypedDict(
    "NetworkResourceUtilizationTypeDef",
    {
        "NetworkInBytesPerSecond": NotRequired[str],
        "NetworkOutBytesPerSecond": NotRequired[str],
        "NetworkPacketsInPerSecond": NotRequired[str],
        "NetworkPacketsOutPerSecond": NotRequired[str],
    },
)
EC2SpecificationTypeDef = TypedDict(
    "EC2SpecificationTypeDef",
    {
        "OfferingClass": NotRequired[OfferingClassType],
    },
)
ESInstanceDetailsTypeDef = TypedDict(
    "ESInstanceDetailsTypeDef",
    {
        "InstanceClass": NotRequired[str],
        "InstanceSize": NotRequired[str],
        "Region": NotRequired[str],
        "CurrentGeneration": NotRequired[bool],
        "SizeFlexEligible": NotRequired[bool],
    },
)
ElastiCacheInstanceDetailsTypeDef = TypedDict(
    "ElastiCacheInstanceDetailsTypeDef",
    {
        "Family": NotRequired[str],
        "NodeType": NotRequired[str],
        "Region": NotRequired[str],
        "ProductDescription": NotRequired[str],
        "CurrentGeneration": NotRequired[bool],
        "SizeFlexEligible": NotRequired[bool],
    },
)
GenerationSummaryTypeDef = TypedDict(
    "GenerationSummaryTypeDef",
    {
        "RecommendationId": NotRequired[str],
        "GenerationStatus": NotRequired[GenerationStatusType],
        "GenerationStartedTime": NotRequired[str],
        "GenerationCompletionTime": NotRequired[str],
        "EstimatedCompletionTime": NotRequired[str],
    },
)
TotalImpactFilterTypeDef = TypedDict(
    "TotalImpactFilterTypeDef",
    {
        "NumericOperator": NumericOperatorType,
        "StartValue": float,
        "EndValue": NotRequired[float],
    },
)
GetAnomalyMonitorsRequestRequestTypeDef = TypedDict(
    "GetAnomalyMonitorsRequestRequestTypeDef",
    {
        "MonitorArnList": NotRequired[Sequence[str]],
        "NextPageToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GetAnomalySubscriptionsRequestRequestTypeDef = TypedDict(
    "GetAnomalySubscriptionsRequestRequestTypeDef",
    {
        "SubscriptionArnList": NotRequired[Sequence[str]],
        "MonitorArn": NotRequired[str],
        "NextPageToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GetApproximateUsageRecordsRequestRequestTypeDef = TypedDict(
    "GetApproximateUsageRecordsRequestRequestTypeDef",
    {
        "Granularity": GranularityType,
        "ApproximationDimension": ApproximationDimensionType,
        "Services": NotRequired[Sequence[str]],
    },
)
GroupDefinitionTypeDef = TypedDict(
    "GroupDefinitionTypeDef",
    {
        "Type": NotRequired[GroupDefinitionTypeType],
        "Key": NotRequired[str],
    },
)
SortDefinitionTypeDef = TypedDict(
    "SortDefinitionTypeDef",
    {
        "Key": str,
        "SortOrder": NotRequired[SortOrderType],
    },
)
MetricValueTypeDef = TypedDict(
    "MetricValueTypeDef",
    {
        "Amount": NotRequired[str],
        "Unit": NotRequired[str],
    },
)
ReservationPurchaseRecommendationMetadataTypeDef = TypedDict(
    "ReservationPurchaseRecommendationMetadataTypeDef",
    {
        "RecommendationId": NotRequired[str],
        "GenerationTimestamp": NotRequired[str],
        "AdditionalMetadata": NotRequired[str],
    },
)
ReservationAggregatesTypeDef = TypedDict(
    "ReservationAggregatesTypeDef",
    {
        "UtilizationPercentage": NotRequired[str],
        "UtilizationPercentageInUnits": NotRequired[str],
        "PurchasedHours": NotRequired[str],
        "PurchasedUnits": NotRequired[str],
        "TotalActualHours": NotRequired[str],
        "TotalActualUnits": NotRequired[str],
        "UnusedHours": NotRequired[str],
        "UnusedUnits": NotRequired[str],
        "OnDemandCostOfRIHoursUsed": NotRequired[str],
        "NetRISavings": NotRequired[str],
        "TotalPotentialRISavings": NotRequired[str],
        "AmortizedUpfrontFee": NotRequired[str],
        "AmortizedRecurringFee": NotRequired[str],
        "TotalAmortizedFee": NotRequired[str],
        "RICostForUnusedHours": NotRequired[str],
        "RealizedSavings": NotRequired[str],
        "UnrealizedSavings": NotRequired[str],
    },
)
RightsizingRecommendationConfigurationTypeDef = TypedDict(
    "RightsizingRecommendationConfigurationTypeDef",
    {
        "RecommendationTarget": RecommendationTargetType,
        "BenefitsConsidered": bool,
    },
)
RightsizingRecommendationMetadataTypeDef = TypedDict(
    "RightsizingRecommendationMetadataTypeDef",
    {
        "RecommendationId": NotRequired[str],
        "GenerationTimestamp": NotRequired[str],
        "LookbackPeriodInDays": NotRequired[LookbackPeriodInDaysType],
        "AdditionalMetadata": NotRequired[str],
    },
)
RightsizingRecommendationSummaryTypeDef = TypedDict(
    "RightsizingRecommendationSummaryTypeDef",
    {
        "TotalRecommendationCount": NotRequired[str],
        "EstimatedTotalMonthlySavingsAmount": NotRequired[str],
        "SavingsCurrencyCode": NotRequired[str],
        "SavingsPercentage": NotRequired[str],
    },
)
GetSavingsPlanPurchaseRecommendationDetailsRequestRequestTypeDef = TypedDict(
    "GetSavingsPlanPurchaseRecommendationDetailsRequestRequestTypeDef",
    {
        "RecommendationDetailId": str,
    },
)
SavingsPlansPurchaseRecommendationMetadataTypeDef = TypedDict(
    "SavingsPlansPurchaseRecommendationMetadataTypeDef",
    {
        "RecommendationId": NotRequired[str],
        "GenerationTimestamp": NotRequired[str],
        "AdditionalMetadata": NotRequired[str],
    },
)
MemoryDBInstanceDetailsTypeDef = TypedDict(
    "MemoryDBInstanceDetailsTypeDef",
    {
        "Family": NotRequired[str],
        "NodeType": NotRequired[str],
        "Region": NotRequired[str],
        "CurrentGeneration": NotRequired[bool],
        "SizeFlexEligible": NotRequired[bool],
    },
)
RDSInstanceDetailsTypeDef = TypedDict(
    "RDSInstanceDetailsTypeDef",
    {
        "Family": NotRequired[str],
        "InstanceType": NotRequired[str],
        "Region": NotRequired[str],
        "DatabaseEngine": NotRequired[str],
        "DatabaseEdition": NotRequired[str],
        "DeploymentOption": NotRequired[str],
        "LicenseModel": NotRequired[str],
        "CurrentGeneration": NotRequired[bool],
        "SizeFlexEligible": NotRequired[bool],
    },
)
RedshiftInstanceDetailsTypeDef = TypedDict(
    "RedshiftInstanceDetailsTypeDef",
    {
        "Family": NotRequired[str],
        "NodeType": NotRequired[str],
        "Region": NotRequired[str],
        "CurrentGeneration": NotRequired[bool],
        "SizeFlexEligible": NotRequired[bool],
    },
)
ListCostAllocationTagBackfillHistoryRequestRequestTypeDef = TypedDict(
    "ListCostAllocationTagBackfillHistoryRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListCostAllocationTagsRequestRequestTypeDef = TypedDict(
    "ListCostAllocationTagsRequestRequestTypeDef",
    {
        "Status": NotRequired[CostAllocationTagStatusType],
        "TagKeys": NotRequired[Sequence[str]],
        "Type": NotRequired[CostAllocationTagTypeType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListCostCategoryDefinitionsRequestRequestTypeDef = TypedDict(
    "ListCostCategoryDefinitionsRequestRequestTypeDef",
    {
        "EffectiveOn": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListSavingsPlansPurchaseRecommendationGenerationRequestRequestTypeDef = TypedDict(
    "ListSavingsPlansPurchaseRecommendationGenerationRequestRequestTypeDef",
    {
        "GenerationStatus": NotRequired[GenerationStatusType],
        "RecommendationIds": NotRequired[Sequence[str]],
        "PageSize": NotRequired[int],
        "NextPageToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
ProvideAnomalyFeedbackRequestRequestTypeDef = TypedDict(
    "ProvideAnomalyFeedbackRequestRequestTypeDef",
    {
        "AnomalyId": str,
        "Feedback": AnomalyFeedbackTypeType,
    },
)
RecommendationDetailHourlyMetricsTypeDef = TypedDict(
    "RecommendationDetailHourlyMetricsTypeDef",
    {
        "StartTime": NotRequired[str],
        "EstimatedOnDemandCost": NotRequired[str],
        "CurrentCoverage": NotRequired[str],
        "EstimatedCoverage": NotRequired[str],
        "EstimatedNewCommitmentUtilization": NotRequired[str],
    },
)
ReservationPurchaseRecommendationSummaryTypeDef = TypedDict(
    "ReservationPurchaseRecommendationSummaryTypeDef",
    {
        "TotalEstimatedMonthlySavingsAmount": NotRequired[str],
        "TotalEstimatedMonthlySavingsPercentage": NotRequired[str],
        "CurrencyCode": NotRequired[str],
    },
)
TerminateRecommendationDetailTypeDef = TypedDict(
    "TerminateRecommendationDetailTypeDef",
    {
        "EstimatedMonthlySavings": NotRequired[str],
        "CurrencyCode": NotRequired[str],
    },
)
SavingsPlansAmortizedCommitmentTypeDef = TypedDict(
    "SavingsPlansAmortizedCommitmentTypeDef",
    {
        "AmortizedRecurringCommitment": NotRequired[str],
        "AmortizedUpfrontCommitment": NotRequired[str],
        "TotalAmortizedCommitment": NotRequired[str],
    },
)
SavingsPlansCoverageDataTypeDef = TypedDict(
    "SavingsPlansCoverageDataTypeDef",
    {
        "SpendCoveredBySavingsPlans": NotRequired[str],
        "OnDemandCost": NotRequired[str],
        "TotalCost": NotRequired[str],
        "CoveragePercentage": NotRequired[str],
    },
)
SavingsPlansDetailsTypeDef = TypedDict(
    "SavingsPlansDetailsTypeDef",
    {
        "Region": NotRequired[str],
        "InstanceFamily": NotRequired[str],
        "OfferingId": NotRequired[str],
    },
)
SavingsPlansPurchaseRecommendationSummaryTypeDef = TypedDict(
    "SavingsPlansPurchaseRecommendationSummaryTypeDef",
    {
        "EstimatedROI": NotRequired[str],
        "CurrencyCode": NotRequired[str],
        "EstimatedTotalCost": NotRequired[str],
        "CurrentOnDemandSpend": NotRequired[str],
        "EstimatedSavingsAmount": NotRequired[str],
        "TotalRecommendationCount": NotRequired[str],
        "DailyCommitmentToPurchase": NotRequired[str],
        "HourlyCommitmentToPurchase": NotRequired[str],
        "EstimatedSavingsPercentage": NotRequired[str],
        "EstimatedMonthlySavingsAmount": NotRequired[str],
        "EstimatedOnDemandCostWithCurrentCommitment": NotRequired[str],
    },
)
SavingsPlansSavingsTypeDef = TypedDict(
    "SavingsPlansSavingsTypeDef",
    {
        "NetSavings": NotRequired[str],
        "OnDemandCostEquivalent": NotRequired[str],
    },
)
SavingsPlansUtilizationTypeDef = TypedDict(
    "SavingsPlansUtilizationTypeDef",
    {
        "TotalCommitment": NotRequired[str],
        "UsedCommitment": NotRequired[str],
        "UnusedCommitment": NotRequired[str],
        "UtilizationPercentage": NotRequired[str],
    },
)
StartCostAllocationTagBackfillRequestRequestTypeDef = TypedDict(
    "StartCostAllocationTagBackfillRequestRequestTypeDef",
    {
        "BackfillFrom": str,
    },
)
TagValuesTypeDef = TypedDict(
    "TagValuesTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
        "MatchOptions": NotRequired[Sequence[MatchOptionType]],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "ResourceTagKeys": Sequence[str],
    },
)
UpdateAnomalyMonitorRequestRequestTypeDef = TypedDict(
    "UpdateAnomalyMonitorRequestRequestTypeDef",
    {
        "MonitorArn": str,
        "MonitorName": NotRequired[str],
    },
)
UpdateCostAllocationTagsStatusErrorTypeDef = TypedDict(
    "UpdateCostAllocationTagsStatusErrorTypeDef",
    {
        "TagKey": NotRequired[str],
        "Code": NotRequired[str],
        "Message": NotRequired[str],
    },
)
AnomalyTypeDef = TypedDict(
    "AnomalyTypeDef",
    {
        "AnomalyId": str,
        "AnomalyScore": AnomalyScoreTypeDef,
        "Impact": ImpactTypeDef,
        "MonitorArn": str,
        "AnomalyStartDate": NotRequired[str],
        "AnomalyEndDate": NotRequired[str],
        "DimensionValue": NotRequired[str],
        "RootCauses": NotRequired[List[RootCauseTypeDef]],
        "Feedback": NotRequired[AnomalyFeedbackTypeType],
    },
)
UpdateCostAllocationTagsStatusRequestRequestTypeDef = TypedDict(
    "UpdateCostAllocationTagsStatusRequestRequestTypeDef",
    {
        "CostAllocationTagsStatus": Sequence[CostAllocationTagStatusEntryTypeDef],
    },
)
CostCategoryReferenceTypeDef = TypedDict(
    "CostCategoryReferenceTypeDef",
    {
        "CostCategoryArn": NotRequired[str],
        "Name": NotRequired[str],
        "EffectiveStart": NotRequired[str],
        "EffectiveEnd": NotRequired[str],
        "NumberOfRules": NotRequired[int],
        "ProcessingStatus": NotRequired[List[CostCategoryProcessingStatusTypeDef]],
        "Values": NotRequired[List[str]],
        "DefaultValue": NotRequired[str],
    },
)
CostCategorySplitChargeRuleOutputTypeDef = TypedDict(
    "CostCategorySplitChargeRuleOutputTypeDef",
    {
        "Source": str,
        "Targets": List[str],
        "Method": CostCategorySplitChargeMethodType,
        "Parameters": NotRequired[List[CostCategorySplitChargeRuleParameterOutputTypeDef]],
    },
)
CostCategorySplitChargeRuleParameterUnionTypeDef = Union[
    CostCategorySplitChargeRuleParameterTypeDef, CostCategorySplitChargeRuleParameterOutputTypeDef
]
CostCategoryValuesUnionTypeDef = Union[CostCategoryValuesTypeDef, CostCategoryValuesOutputTypeDef]
ForecastResultTypeDef = TypedDict(
    "ForecastResultTypeDef",
    {
        "TimePeriod": NotRequired[DateIntervalTypeDef],
        "MeanValue": NotRequired[str],
        "PredictionIntervalLowerBound": NotRequired[str],
        "PredictionIntervalUpperBound": NotRequired[str],
    },
)
CoverageTypeDef = TypedDict(
    "CoverageTypeDef",
    {
        "CoverageHours": NotRequired[CoverageHoursTypeDef],
        "CoverageNormalizedUnits": NotRequired[CoverageNormalizedUnitsTypeDef],
        "CoverageCost": NotRequired[CoverageCostTypeDef],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "ResourceTags": Sequence[ResourceTagTypeDef],
    },
)
CreateAnomalyMonitorResponseTypeDef = TypedDict(
    "CreateAnomalyMonitorResponseTypeDef",
    {
        "MonitorArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAnomalySubscriptionResponseTypeDef = TypedDict(
    "CreateAnomalySubscriptionResponseTypeDef",
    {
        "SubscriptionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCostCategoryDefinitionResponseTypeDef = TypedDict(
    "CreateCostCategoryDefinitionResponseTypeDef",
    {
        "CostCategoryArn": str,
        "EffectiveStart": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteCostCategoryDefinitionResponseTypeDef = TypedDict(
    "DeleteCostCategoryDefinitionResponseTypeDef",
    {
        "CostCategoryArn": str,
        "EffectiveEnd": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetApproximateUsageRecordsResponseTypeDef = TypedDict(
    "GetApproximateUsageRecordsResponseTypeDef",
    {
        "Services": Dict[str, int],
        "TotalRecords": int,
        "LookbackPeriod": DateIntervalTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCostCategoriesResponseTypeDef = TypedDict(
    "GetCostCategoriesResponseTypeDef",
    {
        "NextPageToken": str,
        "CostCategoryNames": List[str],
        "CostCategoryValues": List[str],
        "ReturnSize": int,
        "TotalSize": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTagsResponseTypeDef = TypedDict(
    "GetTagsResponseTypeDef",
    {
        "NextPageToken": str,
        "Tags": List[str],
        "ReturnSize": int,
        "TotalSize": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCostAllocationTagBackfillHistoryResponseTypeDef = TypedDict(
    "ListCostAllocationTagBackfillHistoryResponseTypeDef",
    {
        "BackfillRequests": List[CostAllocationTagBackfillRequestTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListCostAllocationTagsResponseTypeDef = TypedDict(
    "ListCostAllocationTagsResponseTypeDef",
    {
        "CostAllocationTags": List[CostAllocationTagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "ResourceTags": List[ResourceTagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProvideAnomalyFeedbackResponseTypeDef = TypedDict(
    "ProvideAnomalyFeedbackResponseTypeDef",
    {
        "AnomalyId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartCostAllocationTagBackfillResponseTypeDef = TypedDict(
    "StartCostAllocationTagBackfillResponseTypeDef",
    {
        "BackfillRequest": CostAllocationTagBackfillRequestTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartSavingsPlansPurchaseRecommendationGenerationResponseTypeDef = TypedDict(
    "StartSavingsPlansPurchaseRecommendationGenerationResponseTypeDef",
    {
        "RecommendationId": str,
        "GenerationStartedTime": str,
        "EstimatedCompletionTime": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAnomalyMonitorResponseTypeDef = TypedDict(
    "UpdateAnomalyMonitorResponseTypeDef",
    {
        "MonitorArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAnomalySubscriptionResponseTypeDef = TypedDict(
    "UpdateAnomalySubscriptionResponseTypeDef",
    {
        "SubscriptionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateCostCategoryDefinitionResponseTypeDef = TypedDict(
    "UpdateCostCategoryDefinitionResponseTypeDef",
    {
        "CostCategoryArn": str,
        "EffectiveStart": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExpressionOutputTypeDef = TypedDict(
    "ExpressionOutputTypeDef",
    {
        "Or": NotRequired[List[Dict[str, Any]]],
        "And": NotRequired[List[Dict[str, Any]]],
        "Not": NotRequired[Dict[str, Any]],
        "Dimensions": NotRequired[DimensionValuesOutputTypeDef],
        "Tags": NotRequired[TagValuesOutputTypeDef],
        "CostCategories": NotRequired[CostCategoryValuesOutputTypeDef],
    },
)
DimensionValuesUnionTypeDef = Union[DimensionValuesTypeDef, DimensionValuesOutputTypeDef]
GetDimensionValuesResponseTypeDef = TypedDict(
    "GetDimensionValuesResponseTypeDef",
    {
        "DimensionValues": List[DimensionValuesWithAttributesTypeDef],
        "ReturnSize": int,
        "TotalSize": int,
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReservedCapacityDetailsTypeDef = TypedDict(
    "ReservedCapacityDetailsTypeDef",
    {
        "DynamoDBCapacityDetails": NotRequired[DynamoDBCapacityDetailsTypeDef],
    },
)
ResourceDetailsTypeDef = TypedDict(
    "ResourceDetailsTypeDef",
    {
        "EC2ResourceDetails": NotRequired[EC2ResourceDetailsTypeDef],
    },
)
EC2ResourceUtilizationTypeDef = TypedDict(
    "EC2ResourceUtilizationTypeDef",
    {
        "MaxCpuUtilizationPercentage": NotRequired[str],
        "MaxMemoryUtilizationPercentage": NotRequired[str],
        "MaxStorageUtilizationPercentage": NotRequired[str],
        "EBSResourceUtilization": NotRequired[EBSResourceUtilizationTypeDef],
        "DiskResourceUtilization": NotRequired[DiskResourceUtilizationTypeDef],
        "NetworkResourceUtilization": NotRequired[NetworkResourceUtilizationTypeDef],
    },
)
ServiceSpecificationTypeDef = TypedDict(
    "ServiceSpecificationTypeDef",
    {
        "EC2Specification": NotRequired[EC2SpecificationTypeDef],
    },
)
ListSavingsPlansPurchaseRecommendationGenerationResponseTypeDef = TypedDict(
    "ListSavingsPlansPurchaseRecommendationGenerationResponseTypeDef",
    {
        "GenerationSummaryList": List[GenerationSummaryTypeDef],
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAnomaliesRequestRequestTypeDef = TypedDict(
    "GetAnomaliesRequestRequestTypeDef",
    {
        "DateInterval": AnomalyDateIntervalTypeDef,
        "MonitorArn": NotRequired[str],
        "Feedback": NotRequired[AnomalyFeedbackTypeType],
        "TotalImpact": NotRequired[TotalImpactFilterTypeDef],
        "NextPageToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "Keys": NotRequired[List[str]],
        "Metrics": NotRequired[Dict[str, MetricValueTypeDef]],
    },
)
ReservationUtilizationGroupTypeDef = TypedDict(
    "ReservationUtilizationGroupTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
        "Attributes": NotRequired[Dict[str, str]],
        "Utilization": NotRequired[ReservationAggregatesTypeDef],
    },
)
InstanceDetailsTypeDef = TypedDict(
    "InstanceDetailsTypeDef",
    {
        "EC2InstanceDetails": NotRequired[EC2InstanceDetailsTypeDef],
        "RDSInstanceDetails": NotRequired[RDSInstanceDetailsTypeDef],
        "RedshiftInstanceDetails": NotRequired[RedshiftInstanceDetailsTypeDef],
        "ElastiCacheInstanceDetails": NotRequired[ElastiCacheInstanceDetailsTypeDef],
        "ESInstanceDetails": NotRequired[ESInstanceDetailsTypeDef],
        "MemoryDBInstanceDetails": NotRequired[MemoryDBInstanceDetailsTypeDef],
    },
)
RecommendationDetailDataTypeDef = TypedDict(
    "RecommendationDetailDataTypeDef",
    {
        "AccountScope": NotRequired[AccountScopeType],
        "LookbackPeriodInDays": NotRequired[LookbackPeriodInDaysType],
        "SavingsPlansType": NotRequired[SupportedSavingsPlansTypeType],
        "TermInYears": NotRequired[TermInYearsType],
        "PaymentOption": NotRequired[PaymentOptionType],
        "AccountId": NotRequired[str],
        "CurrencyCode": NotRequired[str],
        "InstanceFamily": NotRequired[str],
        "Region": NotRequired[str],
        "OfferingId": NotRequired[str],
        "GenerationTimestamp": NotRequired[str],
        "LatestUsageTimestamp": NotRequired[str],
        "CurrentAverageHourlyOnDemandSpend": NotRequired[str],
        "CurrentMaximumHourlyOnDemandSpend": NotRequired[str],
        "CurrentMinimumHourlyOnDemandSpend": NotRequired[str],
        "EstimatedAverageUtilization": NotRequired[str],
        "EstimatedMonthlySavingsAmount": NotRequired[str],
        "EstimatedOnDemandCost": NotRequired[str],
        "EstimatedOnDemandCostWithCurrentCommitment": NotRequired[str],
        "EstimatedROI": NotRequired[str],
        "EstimatedSPCost": NotRequired[str],
        "EstimatedSavingsAmount": NotRequired[str],
        "EstimatedSavingsPercentage": NotRequired[str],
        "ExistingHourlyCommitment": NotRequired[str],
        "HourlyCommitmentToPurchase": NotRequired[str],
        "UpfrontCost": NotRequired[str],
        "CurrentAverageCoverage": NotRequired[str],
        "EstimatedAverageCoverage": NotRequired[str],
        "MetricsOverLookbackPeriod": NotRequired[List[RecommendationDetailHourlyMetricsTypeDef]],
    },
)
SavingsPlansCoverageTypeDef = TypedDict(
    "SavingsPlansCoverageTypeDef",
    {
        "Attributes": NotRequired[Dict[str, str]],
        "Coverage": NotRequired[SavingsPlansCoverageDataTypeDef],
        "TimePeriod": NotRequired[DateIntervalTypeDef],
    },
)
SavingsPlansPurchaseRecommendationDetailTypeDef = TypedDict(
    "SavingsPlansPurchaseRecommendationDetailTypeDef",
    {
        "SavingsPlansDetails": NotRequired[SavingsPlansDetailsTypeDef],
        "AccountId": NotRequired[str],
        "UpfrontCost": NotRequired[str],
        "EstimatedROI": NotRequired[str],
        "CurrencyCode": NotRequired[str],
        "EstimatedSPCost": NotRequired[str],
        "EstimatedOnDemandCost": NotRequired[str],
        "EstimatedOnDemandCostWithCurrentCommitment": NotRequired[str],
        "EstimatedSavingsAmount": NotRequired[str],
        "EstimatedSavingsPercentage": NotRequired[str],
        "HourlyCommitmentToPurchase": NotRequired[str],
        "EstimatedAverageUtilization": NotRequired[str],
        "EstimatedMonthlySavingsAmount": NotRequired[str],
        "CurrentMinimumHourlyOnDemandSpend": NotRequired[str],
        "CurrentMaximumHourlyOnDemandSpend": NotRequired[str],
        "CurrentAverageHourlyOnDemandSpend": NotRequired[str],
        "RecommendationDetailId": NotRequired[str],
    },
)
SavingsPlansUtilizationAggregatesTypeDef = TypedDict(
    "SavingsPlansUtilizationAggregatesTypeDef",
    {
        "Utilization": SavingsPlansUtilizationTypeDef,
        "Savings": NotRequired[SavingsPlansSavingsTypeDef],
        "AmortizedCommitment": NotRequired[SavingsPlansAmortizedCommitmentTypeDef],
    },
)
SavingsPlansUtilizationByTimeTypeDef = TypedDict(
    "SavingsPlansUtilizationByTimeTypeDef",
    {
        "TimePeriod": DateIntervalTypeDef,
        "Utilization": SavingsPlansUtilizationTypeDef,
        "Savings": NotRequired[SavingsPlansSavingsTypeDef],
        "AmortizedCommitment": NotRequired[SavingsPlansAmortizedCommitmentTypeDef],
    },
)
SavingsPlansUtilizationDetailTypeDef = TypedDict(
    "SavingsPlansUtilizationDetailTypeDef",
    {
        "SavingsPlanArn": NotRequired[str],
        "Attributes": NotRequired[Dict[str, str]],
        "Utilization": NotRequired[SavingsPlansUtilizationTypeDef],
        "Savings": NotRequired[SavingsPlansSavingsTypeDef],
        "AmortizedCommitment": NotRequired[SavingsPlansAmortizedCommitmentTypeDef],
    },
)
TagValuesUnionTypeDef = Union[TagValuesTypeDef, TagValuesOutputTypeDef]
UpdateCostAllocationTagsStatusResponseTypeDef = TypedDict(
    "UpdateCostAllocationTagsStatusResponseTypeDef",
    {
        "Errors": List[UpdateCostAllocationTagsStatusErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAnomaliesResponseTypeDef = TypedDict(
    "GetAnomaliesResponseTypeDef",
    {
        "Anomalies": List[AnomalyTypeDef],
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCostCategoryDefinitionsResponseTypeDef = TypedDict(
    "ListCostCategoryDefinitionsResponseTypeDef",
    {
        "CostCategoryReferences": List[CostCategoryReferenceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CostCategorySplitChargeRuleTypeDef = TypedDict(
    "CostCategorySplitChargeRuleTypeDef",
    {
        "Source": str,
        "Targets": Sequence[str],
        "Method": CostCategorySplitChargeMethodType,
        "Parameters": NotRequired[Sequence[CostCategorySplitChargeRuleParameterUnionTypeDef]],
    },
)
GetCostForecastResponseTypeDef = TypedDict(
    "GetCostForecastResponseTypeDef",
    {
        "Total": MetricValueTypeDef,
        "ForecastResultsByTime": List[ForecastResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetUsageForecastResponseTypeDef = TypedDict(
    "GetUsageForecastResponseTypeDef",
    {
        "Total": MetricValueTypeDef,
        "ForecastResultsByTime": List[ForecastResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReservationCoverageGroupTypeDef = TypedDict(
    "ReservationCoverageGroupTypeDef",
    {
        "Attributes": NotRequired[Dict[str, str]],
        "Coverage": NotRequired[CoverageTypeDef],
    },
)
AnomalyMonitorOutputTypeDef = TypedDict(
    "AnomalyMonitorOutputTypeDef",
    {
        "MonitorName": str,
        "MonitorType": MonitorTypeType,
        "MonitorArn": NotRequired[str],
        "CreationDate": NotRequired[str],
        "LastUpdatedDate": NotRequired[str],
        "LastEvaluatedDate": NotRequired[str],
        "MonitorDimension": NotRequired[Literal["SERVICE"]],
        "MonitorSpecification": NotRequired[ExpressionOutputTypeDef],
        "DimensionalValueCount": NotRequired[int],
    },
)
AnomalySubscriptionOutputTypeDef = TypedDict(
    "AnomalySubscriptionOutputTypeDef",
    {
        "MonitorArnList": List[str],
        "Subscribers": List[SubscriberTypeDef],
        "Frequency": AnomalySubscriptionFrequencyType,
        "SubscriptionName": str,
        "SubscriptionArn": NotRequired[str],
        "AccountId": NotRequired[str],
        "Threshold": NotRequired[float],
        "ThresholdExpression": NotRequired[ExpressionOutputTypeDef],
    },
)
CostCategoryRuleOutputTypeDef = TypedDict(
    "CostCategoryRuleOutputTypeDef",
    {
        "Value": NotRequired[str],
        "Rule": NotRequired[ExpressionOutputTypeDef],
        "InheritedValue": NotRequired[CostCategoryInheritedValueDimensionTypeDef],
        "Type": NotRequired[CostCategoryRuleTypeType],
    },
)
ResourceUtilizationTypeDef = TypedDict(
    "ResourceUtilizationTypeDef",
    {
        "EC2ResourceUtilization": NotRequired[EC2ResourceUtilizationTypeDef],
    },
)
ResultByTimeTypeDef = TypedDict(
    "ResultByTimeTypeDef",
    {
        "TimePeriod": NotRequired[DateIntervalTypeDef],
        "Total": NotRequired[Dict[str, MetricValueTypeDef]],
        "Groups": NotRequired[List[GroupTypeDef]],
        "Estimated": NotRequired[bool],
    },
)
UtilizationByTimeTypeDef = TypedDict(
    "UtilizationByTimeTypeDef",
    {
        "TimePeriod": NotRequired[DateIntervalTypeDef],
        "Groups": NotRequired[List[ReservationUtilizationGroupTypeDef]],
        "Total": NotRequired[ReservationAggregatesTypeDef],
    },
)
ReservationPurchaseRecommendationDetailTypeDef = TypedDict(
    "ReservationPurchaseRecommendationDetailTypeDef",
    {
        "AccountId": NotRequired[str],
        "InstanceDetails": NotRequired[InstanceDetailsTypeDef],
        "RecommendedNumberOfInstancesToPurchase": NotRequired[str],
        "RecommendedNormalizedUnitsToPurchase": NotRequired[str],
        "MinimumNumberOfInstancesUsedPerHour": NotRequired[str],
        "MinimumNormalizedUnitsUsedPerHour": NotRequired[str],
        "MaximumNumberOfInstancesUsedPerHour": NotRequired[str],
        "MaximumNormalizedUnitsUsedPerHour": NotRequired[str],
        "AverageNumberOfInstancesUsedPerHour": NotRequired[str],
        "AverageNormalizedUnitsUsedPerHour": NotRequired[str],
        "AverageUtilization": NotRequired[str],
        "EstimatedBreakEvenInMonths": NotRequired[str],
        "CurrencyCode": NotRequired[str],
        "EstimatedMonthlySavingsAmount": NotRequired[str],
        "EstimatedMonthlySavingsPercentage": NotRequired[str],
        "EstimatedMonthlyOnDemandCost": NotRequired[str],
        "EstimatedReservationCostForLookbackPeriod": NotRequired[str],
        "UpfrontCost": NotRequired[str],
        "RecurringStandardMonthlyCost": NotRequired[str],
        "ReservedCapacityDetails": NotRequired[ReservedCapacityDetailsTypeDef],
        "RecommendedNumberOfCapacityUnitsToPurchase": NotRequired[str],
        "MinimumNumberOfCapacityUnitsUsedPerHour": NotRequired[str],
        "MaximumNumberOfCapacityUnitsUsedPerHour": NotRequired[str],
        "AverageNumberOfCapacityUnitsUsedPerHour": NotRequired[str],
    },
)
GetSavingsPlanPurchaseRecommendationDetailsResponseTypeDef = TypedDict(
    "GetSavingsPlanPurchaseRecommendationDetailsResponseTypeDef",
    {
        "RecommendationDetailId": str,
        "RecommendationDetailData": RecommendationDetailDataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSavingsPlansCoverageResponseTypeDef = TypedDict(
    "GetSavingsPlansCoverageResponseTypeDef",
    {
        "SavingsPlansCoverages": List[SavingsPlansCoverageTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
SavingsPlansPurchaseRecommendationTypeDef = TypedDict(
    "SavingsPlansPurchaseRecommendationTypeDef",
    {
        "AccountScope": NotRequired[AccountScopeType],
        "SavingsPlansType": NotRequired[SupportedSavingsPlansTypeType],
        "TermInYears": NotRequired[TermInYearsType],
        "PaymentOption": NotRequired[PaymentOptionType],
        "LookbackPeriodInDays": NotRequired[LookbackPeriodInDaysType],
        "SavingsPlansPurchaseRecommendationDetails": NotRequired[
            List[SavingsPlansPurchaseRecommendationDetailTypeDef]
        ],
        "SavingsPlansPurchaseRecommendationSummary": NotRequired[
            SavingsPlansPurchaseRecommendationSummaryTypeDef
        ],
    },
)
GetSavingsPlansUtilizationResponseTypeDef = TypedDict(
    "GetSavingsPlansUtilizationResponseTypeDef",
    {
        "SavingsPlansUtilizationsByTime": List[SavingsPlansUtilizationByTimeTypeDef],
        "Total": SavingsPlansUtilizationAggregatesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSavingsPlansUtilizationDetailsResponseTypeDef = TypedDict(
    "GetSavingsPlansUtilizationDetailsResponseTypeDef",
    {
        "SavingsPlansUtilizationDetails": List[SavingsPlansUtilizationDetailTypeDef],
        "Total": SavingsPlansUtilizationAggregatesTypeDef,
        "TimePeriod": DateIntervalTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ExpressionTypeDef = TypedDict(
    "ExpressionTypeDef",
    {
        "Or": NotRequired[Sequence[Mapping[str, Any]]],
        "And": NotRequired[Sequence[Mapping[str, Any]]],
        "Not": NotRequired[Mapping[str, Any]],
        "Dimensions": NotRequired[DimensionValuesUnionTypeDef],
        "Tags": NotRequired[TagValuesUnionTypeDef],
        "CostCategories": NotRequired[CostCategoryValuesUnionTypeDef],
    },
)
CostCategorySplitChargeRuleUnionTypeDef = Union[
    CostCategorySplitChargeRuleTypeDef, CostCategorySplitChargeRuleOutputTypeDef
]
CoverageByTimeTypeDef = TypedDict(
    "CoverageByTimeTypeDef",
    {
        "TimePeriod": NotRequired[DateIntervalTypeDef],
        "Groups": NotRequired[List[ReservationCoverageGroupTypeDef]],
        "Total": NotRequired[CoverageTypeDef],
    },
)
GetAnomalyMonitorsResponseTypeDef = TypedDict(
    "GetAnomalyMonitorsResponseTypeDef",
    {
        "AnomalyMonitors": List[AnomalyMonitorOutputTypeDef],
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAnomalySubscriptionsResponseTypeDef = TypedDict(
    "GetAnomalySubscriptionsResponseTypeDef",
    {
        "AnomalySubscriptions": List[AnomalySubscriptionOutputTypeDef],
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CostCategoryTypeDef = TypedDict(
    "CostCategoryTypeDef",
    {
        "CostCategoryArn": str,
        "EffectiveStart": str,
        "Name": str,
        "RuleVersion": Literal["CostCategoryExpression.v1"],
        "Rules": List[CostCategoryRuleOutputTypeDef],
        "EffectiveEnd": NotRequired[str],
        "SplitChargeRules": NotRequired[List[CostCategorySplitChargeRuleOutputTypeDef]],
        "ProcessingStatus": NotRequired[List[CostCategoryProcessingStatusTypeDef]],
        "DefaultValue": NotRequired[str],
    },
)
CurrentInstanceTypeDef = TypedDict(
    "CurrentInstanceTypeDef",
    {
        "ResourceId": NotRequired[str],
        "InstanceName": NotRequired[str],
        "Tags": NotRequired[List[TagValuesOutputTypeDef]],
        "ResourceDetails": NotRequired[ResourceDetailsTypeDef],
        "ResourceUtilization": NotRequired[ResourceUtilizationTypeDef],
        "ReservationCoveredHoursInLookbackPeriod": NotRequired[str],
        "SavingsPlansCoveredHoursInLookbackPeriod": NotRequired[str],
        "OnDemandHoursInLookbackPeriod": NotRequired[str],
        "TotalRunningHoursInLookbackPeriod": NotRequired[str],
        "MonthlyCost": NotRequired[str],
        "CurrencyCode": NotRequired[str],
    },
)
TargetInstanceTypeDef = TypedDict(
    "TargetInstanceTypeDef",
    {
        "EstimatedMonthlyCost": NotRequired[str],
        "EstimatedMonthlySavings": NotRequired[str],
        "CurrencyCode": NotRequired[str],
        "DefaultTargetInstance": NotRequired[bool],
        "ResourceDetails": NotRequired[ResourceDetailsTypeDef],
        "ExpectedResourceUtilization": NotRequired[ResourceUtilizationTypeDef],
        "PlatformDifferences": NotRequired[List[PlatformDifferenceType]],
    },
)
GetCostAndUsageResponseTypeDef = TypedDict(
    "GetCostAndUsageResponseTypeDef",
    {
        "NextPageToken": str,
        "GroupDefinitions": List[GroupDefinitionTypeDef],
        "ResultsByTime": List[ResultByTimeTypeDef],
        "DimensionValueAttributes": List[DimensionValuesWithAttributesTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCostAndUsageWithResourcesResponseTypeDef = TypedDict(
    "GetCostAndUsageWithResourcesResponseTypeDef",
    {
        "NextPageToken": str,
        "GroupDefinitions": List[GroupDefinitionTypeDef],
        "ResultsByTime": List[ResultByTimeTypeDef],
        "DimensionValueAttributes": List[DimensionValuesWithAttributesTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetReservationUtilizationResponseTypeDef = TypedDict(
    "GetReservationUtilizationResponseTypeDef",
    {
        "UtilizationsByTime": List[UtilizationByTimeTypeDef],
        "Total": ReservationAggregatesTypeDef,
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReservationPurchaseRecommendationTypeDef = TypedDict(
    "ReservationPurchaseRecommendationTypeDef",
    {
        "AccountScope": NotRequired[AccountScopeType],
        "LookbackPeriodInDays": NotRequired[LookbackPeriodInDaysType],
        "TermInYears": NotRequired[TermInYearsType],
        "PaymentOption": NotRequired[PaymentOptionType],
        "ServiceSpecification": NotRequired[ServiceSpecificationTypeDef],
        "RecommendationDetails": NotRequired[List[ReservationPurchaseRecommendationDetailTypeDef]],
        "RecommendationSummary": NotRequired[ReservationPurchaseRecommendationSummaryTypeDef],
    },
)
GetSavingsPlansPurchaseRecommendationResponseTypeDef = TypedDict(
    "GetSavingsPlansPurchaseRecommendationResponseTypeDef",
    {
        "Metadata": SavingsPlansPurchaseRecommendationMetadataTypeDef,
        "SavingsPlansPurchaseRecommendation": SavingsPlansPurchaseRecommendationTypeDef,
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExpressionUnionTypeDef = Union[ExpressionTypeDef, ExpressionOutputTypeDef]
GetCostAndUsageRequestRequestTypeDef = TypedDict(
    "GetCostAndUsageRequestRequestTypeDef",
    {
        "TimePeriod": DateIntervalTypeDef,
        "Granularity": GranularityType,
        "Metrics": Sequence[str],
        "Filter": NotRequired[ExpressionTypeDef],
        "GroupBy": NotRequired[Sequence[GroupDefinitionTypeDef]],
        "NextPageToken": NotRequired[str],
    },
)
GetCostAndUsageWithResourcesRequestRequestTypeDef = TypedDict(
    "GetCostAndUsageWithResourcesRequestRequestTypeDef",
    {
        "TimePeriod": DateIntervalTypeDef,
        "Granularity": GranularityType,
        "Filter": ExpressionTypeDef,
        "Metrics": NotRequired[Sequence[str]],
        "GroupBy": NotRequired[Sequence[GroupDefinitionTypeDef]],
        "NextPageToken": NotRequired[str],
    },
)
GetCostCategoriesRequestRequestTypeDef = TypedDict(
    "GetCostCategoriesRequestRequestTypeDef",
    {
        "TimePeriod": DateIntervalTypeDef,
        "SearchString": NotRequired[str],
        "CostCategoryName": NotRequired[str],
        "Filter": NotRequired[ExpressionTypeDef],
        "SortBy": NotRequired[Sequence[SortDefinitionTypeDef]],
        "MaxResults": NotRequired[int],
        "NextPageToken": NotRequired[str],
    },
)
GetCostForecastRequestRequestTypeDef = TypedDict(
    "GetCostForecastRequestRequestTypeDef",
    {
        "TimePeriod": DateIntervalTypeDef,
        "Metric": MetricType,
        "Granularity": GranularityType,
        "Filter": NotRequired[ExpressionTypeDef],
        "PredictionIntervalLevel": NotRequired[int],
    },
)
GetDimensionValuesRequestRequestTypeDef = TypedDict(
    "GetDimensionValuesRequestRequestTypeDef",
    {
        "TimePeriod": DateIntervalTypeDef,
        "Dimension": DimensionType,
        "SearchString": NotRequired[str],
        "Context": NotRequired[ContextType],
        "Filter": NotRequired[ExpressionTypeDef],
        "SortBy": NotRequired[Sequence[SortDefinitionTypeDef]],
        "MaxResults": NotRequired[int],
        "NextPageToken": NotRequired[str],
    },
)
GetReservationCoverageRequestRequestTypeDef = TypedDict(
    "GetReservationCoverageRequestRequestTypeDef",
    {
        "TimePeriod": DateIntervalTypeDef,
        "GroupBy": NotRequired[Sequence[GroupDefinitionTypeDef]],
        "Granularity": NotRequired[GranularityType],
        "Filter": NotRequired[ExpressionTypeDef],
        "Metrics": NotRequired[Sequence[str]],
        "NextPageToken": NotRequired[str],
        "SortBy": NotRequired[SortDefinitionTypeDef],
        "MaxResults": NotRequired[int],
    },
)
GetReservationPurchaseRecommendationRequestRequestTypeDef = TypedDict(
    "GetReservationPurchaseRecommendationRequestRequestTypeDef",
    {
        "Service": str,
        "AccountId": NotRequired[str],
        "Filter": NotRequired[ExpressionTypeDef],
        "AccountScope": NotRequired[AccountScopeType],
        "LookbackPeriodInDays": NotRequired[LookbackPeriodInDaysType],
        "TermInYears": NotRequired[TermInYearsType],
        "PaymentOption": NotRequired[PaymentOptionType],
        "ServiceSpecification": NotRequired[ServiceSpecificationTypeDef],
        "PageSize": NotRequired[int],
        "NextPageToken": NotRequired[str],
    },
)
GetReservationUtilizationRequestRequestTypeDef = TypedDict(
    "GetReservationUtilizationRequestRequestTypeDef",
    {
        "TimePeriod": DateIntervalTypeDef,
        "GroupBy": NotRequired[Sequence[GroupDefinitionTypeDef]],
        "Granularity": NotRequired[GranularityType],
        "Filter": NotRequired[ExpressionTypeDef],
        "SortBy": NotRequired[SortDefinitionTypeDef],
        "NextPageToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GetRightsizingRecommendationRequestRequestTypeDef = TypedDict(
    "GetRightsizingRecommendationRequestRequestTypeDef",
    {
        "Service": str,
        "Filter": NotRequired[ExpressionTypeDef],
        "Configuration": NotRequired[RightsizingRecommendationConfigurationTypeDef],
        "PageSize": NotRequired[int],
        "NextPageToken": NotRequired[str],
    },
)
GetSavingsPlansCoverageRequestRequestTypeDef = TypedDict(
    "GetSavingsPlansCoverageRequestRequestTypeDef",
    {
        "TimePeriod": DateIntervalTypeDef,
        "GroupBy": NotRequired[Sequence[GroupDefinitionTypeDef]],
        "Granularity": NotRequired[GranularityType],
        "Filter": NotRequired[ExpressionTypeDef],
        "Metrics": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "SortBy": NotRequired[SortDefinitionTypeDef],
    },
)
GetSavingsPlansPurchaseRecommendationRequestRequestTypeDef = TypedDict(
    "GetSavingsPlansPurchaseRecommendationRequestRequestTypeDef",
    {
        "SavingsPlansType": SupportedSavingsPlansTypeType,
        "TermInYears": TermInYearsType,
        "PaymentOption": PaymentOptionType,
        "LookbackPeriodInDays": LookbackPeriodInDaysType,
        "AccountScope": NotRequired[AccountScopeType],
        "NextPageToken": NotRequired[str],
        "PageSize": NotRequired[int],
        "Filter": NotRequired[ExpressionTypeDef],
    },
)
GetSavingsPlansUtilizationDetailsRequestRequestTypeDef = TypedDict(
    "GetSavingsPlansUtilizationDetailsRequestRequestTypeDef",
    {
        "TimePeriod": DateIntervalTypeDef,
        "Filter": NotRequired[ExpressionTypeDef],
        "DataType": NotRequired[Sequence[SavingsPlansDataTypeType]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "SortBy": NotRequired[SortDefinitionTypeDef],
    },
)
GetSavingsPlansUtilizationRequestRequestTypeDef = TypedDict(
    "GetSavingsPlansUtilizationRequestRequestTypeDef",
    {
        "TimePeriod": DateIntervalTypeDef,
        "Granularity": NotRequired[GranularityType],
        "Filter": NotRequired[ExpressionTypeDef],
        "SortBy": NotRequired[SortDefinitionTypeDef],
    },
)
GetTagsRequestRequestTypeDef = TypedDict(
    "GetTagsRequestRequestTypeDef",
    {
        "TimePeriod": DateIntervalTypeDef,
        "SearchString": NotRequired[str],
        "TagKey": NotRequired[str],
        "Filter": NotRequired[ExpressionTypeDef],
        "SortBy": NotRequired[Sequence[SortDefinitionTypeDef]],
        "MaxResults": NotRequired[int],
        "NextPageToken": NotRequired[str],
    },
)
GetUsageForecastRequestRequestTypeDef = TypedDict(
    "GetUsageForecastRequestRequestTypeDef",
    {
        "TimePeriod": DateIntervalTypeDef,
        "Metric": MetricType,
        "Granularity": GranularityType,
        "Filter": NotRequired[ExpressionTypeDef],
        "PredictionIntervalLevel": NotRequired[int],
    },
)
UpdateAnomalySubscriptionRequestRequestTypeDef = TypedDict(
    "UpdateAnomalySubscriptionRequestRequestTypeDef",
    {
        "SubscriptionArn": str,
        "Threshold": NotRequired[float],
        "Frequency": NotRequired[AnomalySubscriptionFrequencyType],
        "MonitorArnList": NotRequired[Sequence[str]],
        "Subscribers": NotRequired[Sequence[SubscriberTypeDef]],
        "SubscriptionName": NotRequired[str],
        "ThresholdExpression": NotRequired[ExpressionTypeDef],
    },
)
GetReservationCoverageResponseTypeDef = TypedDict(
    "GetReservationCoverageResponseTypeDef",
    {
        "CoveragesByTime": List[CoverageByTimeTypeDef],
        "Total": CoverageTypeDef,
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeCostCategoryDefinitionResponseTypeDef = TypedDict(
    "DescribeCostCategoryDefinitionResponseTypeDef",
    {
        "CostCategory": CostCategoryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyRecommendationDetailTypeDef = TypedDict(
    "ModifyRecommendationDetailTypeDef",
    {
        "TargetInstances": NotRequired[List[TargetInstanceTypeDef]],
    },
)
GetReservationPurchaseRecommendationResponseTypeDef = TypedDict(
    "GetReservationPurchaseRecommendationResponseTypeDef",
    {
        "Metadata": ReservationPurchaseRecommendationMetadataTypeDef,
        "Recommendations": List[ReservationPurchaseRecommendationTypeDef],
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AnomalyMonitorTypeDef = TypedDict(
    "AnomalyMonitorTypeDef",
    {
        "MonitorName": str,
        "MonitorType": MonitorTypeType,
        "MonitorArn": NotRequired[str],
        "CreationDate": NotRequired[str],
        "LastUpdatedDate": NotRequired[str],
        "LastEvaluatedDate": NotRequired[str],
        "MonitorDimension": NotRequired[Literal["SERVICE"]],
        "MonitorSpecification": NotRequired[ExpressionUnionTypeDef],
        "DimensionalValueCount": NotRequired[int],
    },
)
AnomalySubscriptionTypeDef = TypedDict(
    "AnomalySubscriptionTypeDef",
    {
        "MonitorArnList": Sequence[str],
        "Subscribers": Sequence[SubscriberTypeDef],
        "Frequency": AnomalySubscriptionFrequencyType,
        "SubscriptionName": str,
        "SubscriptionArn": NotRequired[str],
        "AccountId": NotRequired[str],
        "Threshold": NotRequired[float],
        "ThresholdExpression": NotRequired[ExpressionUnionTypeDef],
    },
)
CostCategoryRuleTypeDef = TypedDict(
    "CostCategoryRuleTypeDef",
    {
        "Value": NotRequired[str],
        "Rule": NotRequired[ExpressionUnionTypeDef],
        "InheritedValue": NotRequired[CostCategoryInheritedValueDimensionTypeDef],
        "Type": NotRequired[CostCategoryRuleTypeType],
    },
)
RightsizingRecommendationTypeDef = TypedDict(
    "RightsizingRecommendationTypeDef",
    {
        "AccountId": NotRequired[str],
        "CurrentInstance": NotRequired[CurrentInstanceTypeDef],
        "RightsizingType": NotRequired[RightsizingTypeType],
        "ModifyRecommendationDetail": NotRequired[ModifyRecommendationDetailTypeDef],
        "TerminateRecommendationDetail": NotRequired[TerminateRecommendationDetailTypeDef],
        "FindingReasonCodes": NotRequired[List[FindingReasonCodeType]],
    },
)
CreateAnomalyMonitorRequestRequestTypeDef = TypedDict(
    "CreateAnomalyMonitorRequestRequestTypeDef",
    {
        "AnomalyMonitor": AnomalyMonitorTypeDef,
        "ResourceTags": NotRequired[Sequence[ResourceTagTypeDef]],
    },
)
CreateAnomalySubscriptionRequestRequestTypeDef = TypedDict(
    "CreateAnomalySubscriptionRequestRequestTypeDef",
    {
        "AnomalySubscription": AnomalySubscriptionTypeDef,
        "ResourceTags": NotRequired[Sequence[ResourceTagTypeDef]],
    },
)
CostCategoryRuleUnionTypeDef = Union[CostCategoryRuleTypeDef, CostCategoryRuleOutputTypeDef]
UpdateCostCategoryDefinitionRequestRequestTypeDef = TypedDict(
    "UpdateCostCategoryDefinitionRequestRequestTypeDef",
    {
        "CostCategoryArn": str,
        "RuleVersion": Literal["CostCategoryExpression.v1"],
        "Rules": Sequence[CostCategoryRuleTypeDef],
        "EffectiveStart": NotRequired[str],
        "DefaultValue": NotRequired[str],
        "SplitChargeRules": NotRequired[Sequence[CostCategorySplitChargeRuleTypeDef]],
    },
)
GetRightsizingRecommendationResponseTypeDef = TypedDict(
    "GetRightsizingRecommendationResponseTypeDef",
    {
        "Metadata": RightsizingRecommendationMetadataTypeDef,
        "Summary": RightsizingRecommendationSummaryTypeDef,
        "RightsizingRecommendations": List[RightsizingRecommendationTypeDef],
        "NextPageToken": str,
        "Configuration": RightsizingRecommendationConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCostCategoryDefinitionRequestRequestTypeDef = TypedDict(
    "CreateCostCategoryDefinitionRequestRequestTypeDef",
    {
        "Name": str,
        "RuleVersion": Literal["CostCategoryExpression.v1"],
        "Rules": Sequence[CostCategoryRuleUnionTypeDef],
        "EffectiveStart": NotRequired[str],
        "DefaultValue": NotRequired[str],
        "SplitChargeRules": NotRequired[Sequence[CostCategorySplitChargeRuleUnionTypeDef]],
        "ResourceTags": NotRequired[Sequence[ResourceTagTypeDef]],
    },
)
