"""
Type annotations for cost-optimization-hub service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/type_defs/)

Usage::

    ```python
    from mypy_boto3_cost_optimization_hub.type_defs import AccountEnrollmentStatusTypeDef

    data: AccountEnrollmentStatusTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import (
    ActionTypeType,
    EnrollmentStatusType,
    ImplementationEffortType,
    MemberAccountDiscountVisibilityType,
    OrderType,
    ResourceTypeType,
    SavingsEstimationModeType,
    SourceType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AccountEnrollmentStatusTypeDef",
    "BlockStoragePerformanceConfigurationTypeDef",
    "ComputeConfigurationTypeDef",
    "ComputeSavingsPlansConfigurationTypeDef",
    "DbInstanceConfigurationTypeDef",
    "StorageConfigurationTypeDef",
    "InstanceConfigurationTypeDef",
    "Ec2InstanceSavingsPlansConfigurationTypeDef",
    "Ec2ReservedInstancesConfigurationTypeDef",
    "ElastiCacheReservedInstancesConfigurationTypeDef",
    "EstimatedDiscountsTypeDef",
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "GetRecommendationRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListEnrollmentStatusesRequestRequestTypeDef",
    "RecommendationSummaryTypeDef",
    "SummaryMetricsResultTypeDef",
    "OrderByTypeDef",
    "OpenSearchReservedInstancesConfigurationTypeDef",
    "RdsDbInstanceStorageConfigurationTypeDef",
    "RdsReservedInstancesConfigurationTypeDef",
    "RedshiftReservedInstancesConfigurationTypeDef",
    "ReservedInstancesPricingTypeDef",
    "UsageTypeDef",
    "SageMakerSavingsPlansConfigurationTypeDef",
    "SavingsPlansPricingTypeDef",
    "UpdateEnrollmentStatusRequestRequestTypeDef",
    "UpdatePreferencesRequestRequestTypeDef",
    "EcsServiceConfigurationTypeDef",
    "LambdaFunctionConfigurationTypeDef",
    "RdsDbInstanceConfigurationTypeDef",
    "EbsVolumeConfigurationTypeDef",
    "Ec2AutoScalingGroupConfigurationTypeDef",
    "Ec2InstanceConfigurationTypeDef",
    "ResourcePricingTypeDef",
    "FilterTypeDef",
    "RecommendationTypeDef",
    "GetPreferencesResponseTypeDef",
    "ListEnrollmentStatusesResponseTypeDef",
    "UpdateEnrollmentStatusResponseTypeDef",
    "UpdatePreferencesResponseTypeDef",
    "ListEnrollmentStatusesRequestListEnrollmentStatusesPaginateTypeDef",
    "ListRecommendationSummariesResponseTypeDef",
    "ReservedInstancesCostCalculationTypeDef",
    "SavingsPlansCostCalculationTypeDef",
    "ResourceCostCalculationTypeDef",
    "ListRecommendationSummariesRequestListRecommendationSummariesPaginateTypeDef",
    "ListRecommendationSummariesRequestRequestTypeDef",
    "ListRecommendationsRequestListRecommendationsPaginateTypeDef",
    "ListRecommendationsRequestRequestTypeDef",
    "ListRecommendationsResponseTypeDef",
    "Ec2ReservedInstancesTypeDef",
    "ElastiCacheReservedInstancesTypeDef",
    "OpenSearchReservedInstancesTypeDef",
    "RdsReservedInstancesTypeDef",
    "RedshiftReservedInstancesTypeDef",
    "ComputeSavingsPlansTypeDef",
    "Ec2InstanceSavingsPlansTypeDef",
    "SageMakerSavingsPlansTypeDef",
    "EbsVolumeTypeDef",
    "Ec2AutoScalingGroupTypeDef",
    "Ec2InstanceTypeDef",
    "EcsServiceTypeDef",
    "LambdaFunctionTypeDef",
    "RdsDbInstanceStorageTypeDef",
    "RdsDbInstanceTypeDef",
    "ResourceDetailsTypeDef",
    "GetRecommendationResponseTypeDef",
)

AccountEnrollmentStatusTypeDef = TypedDict(
    "AccountEnrollmentStatusTypeDef",
    {
        "accountId": NotRequired[str],
        "status": NotRequired[EnrollmentStatusType],
        "lastUpdatedTimestamp": NotRequired[datetime],
        "createdTimestamp": NotRequired[datetime],
    },
)
BlockStoragePerformanceConfigurationTypeDef = TypedDict(
    "BlockStoragePerformanceConfigurationTypeDef",
    {
        "iops": NotRequired[float],
        "throughput": NotRequired[float],
    },
)
ComputeConfigurationTypeDef = TypedDict(
    "ComputeConfigurationTypeDef",
    {
        "vCpu": NotRequired[float],
        "memorySizeInMB": NotRequired[int],
        "architecture": NotRequired[str],
        "platform": NotRequired[str],
    },
)
ComputeSavingsPlansConfigurationTypeDef = TypedDict(
    "ComputeSavingsPlansConfigurationTypeDef",
    {
        "accountScope": NotRequired[str],
        "term": NotRequired[str],
        "paymentOption": NotRequired[str],
        "hourlyCommitment": NotRequired[str],
    },
)
DbInstanceConfigurationTypeDef = TypedDict(
    "DbInstanceConfigurationTypeDef",
    {
        "dbInstanceClass": NotRequired[str],
    },
)
StorageConfigurationTypeDef = TypedDict(
    "StorageConfigurationTypeDef",
    {
        "type": NotRequired[str],
        "sizeInGb": NotRequired[float],
    },
)
InstanceConfigurationTypeDef = TypedDict(
    "InstanceConfigurationTypeDef",
    {
        "type": NotRequired[str],
    },
)
Ec2InstanceSavingsPlansConfigurationTypeDef = TypedDict(
    "Ec2InstanceSavingsPlansConfigurationTypeDef",
    {
        "accountScope": NotRequired[str],
        "term": NotRequired[str],
        "paymentOption": NotRequired[str],
        "hourlyCommitment": NotRequired[str],
        "instanceFamily": NotRequired[str],
        "savingsPlansRegion": NotRequired[str],
    },
)
Ec2ReservedInstancesConfigurationTypeDef = TypedDict(
    "Ec2ReservedInstancesConfigurationTypeDef",
    {
        "accountScope": NotRequired[str],
        "service": NotRequired[str],
        "normalizedUnitsToPurchase": NotRequired[str],
        "term": NotRequired[str],
        "paymentOption": NotRequired[str],
        "numberOfInstancesToPurchase": NotRequired[str],
        "offeringClass": NotRequired[str],
        "instanceFamily": NotRequired[str],
        "instanceType": NotRequired[str],
        "reservedInstancesRegion": NotRequired[str],
        "currentGeneration": NotRequired[str],
        "platform": NotRequired[str],
        "tenancy": NotRequired[str],
        "sizeFlexEligible": NotRequired[bool],
        "upfrontCost": NotRequired[str],
        "monthlyRecurringCost": NotRequired[str],
    },
)
ElastiCacheReservedInstancesConfigurationTypeDef = TypedDict(
    "ElastiCacheReservedInstancesConfigurationTypeDef",
    {
        "accountScope": NotRequired[str],
        "service": NotRequired[str],
        "normalizedUnitsToPurchase": NotRequired[str],
        "term": NotRequired[str],
        "paymentOption": NotRequired[str],
        "numberOfInstancesToPurchase": NotRequired[str],
        "instanceFamily": NotRequired[str],
        "instanceType": NotRequired[str],
        "reservedInstancesRegion": NotRequired[str],
        "currentGeneration": NotRequired[str],
        "sizeFlexEligible": NotRequired[bool],
        "upfrontCost": NotRequired[str],
        "monthlyRecurringCost": NotRequired[str],
    },
)
EstimatedDiscountsTypeDef = TypedDict(
    "EstimatedDiscountsTypeDef",
    {
        "savingsPlansDiscount": NotRequired[float],
        "reservedInstancesDiscount": NotRequired[float],
        "otherDiscount": NotRequired[float],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[str],
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
GetRecommendationRequestRequestTypeDef = TypedDict(
    "GetRecommendationRequestRequestTypeDef",
    {
        "recommendationId": str,
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
ListEnrollmentStatusesRequestRequestTypeDef = TypedDict(
    "ListEnrollmentStatusesRequestRequestTypeDef",
    {
        "includeOrganizationInfo": NotRequired[bool],
        "accountId": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
RecommendationSummaryTypeDef = TypedDict(
    "RecommendationSummaryTypeDef",
    {
        "group": NotRequired[str],
        "estimatedMonthlySavings": NotRequired[float],
        "recommendationCount": NotRequired[int],
    },
)
SummaryMetricsResultTypeDef = TypedDict(
    "SummaryMetricsResultTypeDef",
    {
        "savingsPercentage": NotRequired[str],
    },
)
OrderByTypeDef = TypedDict(
    "OrderByTypeDef",
    {
        "dimension": NotRequired[str],
        "order": NotRequired[OrderType],
    },
)
OpenSearchReservedInstancesConfigurationTypeDef = TypedDict(
    "OpenSearchReservedInstancesConfigurationTypeDef",
    {
        "accountScope": NotRequired[str],
        "service": NotRequired[str],
        "normalizedUnitsToPurchase": NotRequired[str],
        "term": NotRequired[str],
        "paymentOption": NotRequired[str],
        "numberOfInstancesToPurchase": NotRequired[str],
        "instanceType": NotRequired[str],
        "reservedInstancesRegion": NotRequired[str],
        "currentGeneration": NotRequired[str],
        "sizeFlexEligible": NotRequired[bool],
        "upfrontCost": NotRequired[str],
        "monthlyRecurringCost": NotRequired[str],
    },
)
RdsDbInstanceStorageConfigurationTypeDef = TypedDict(
    "RdsDbInstanceStorageConfigurationTypeDef",
    {
        "storageType": NotRequired[str],
        "allocatedStorageInGb": NotRequired[float],
        "iops": NotRequired[float],
        "storageThroughput": NotRequired[float],
    },
)
RdsReservedInstancesConfigurationTypeDef = TypedDict(
    "RdsReservedInstancesConfigurationTypeDef",
    {
        "accountScope": NotRequired[str],
        "service": NotRequired[str],
        "normalizedUnitsToPurchase": NotRequired[str],
        "term": NotRequired[str],
        "paymentOption": NotRequired[str],
        "numberOfInstancesToPurchase": NotRequired[str],
        "instanceFamily": NotRequired[str],
        "instanceType": NotRequired[str],
        "reservedInstancesRegion": NotRequired[str],
        "sizeFlexEligible": NotRequired[bool],
        "currentGeneration": NotRequired[str],
        "upfrontCost": NotRequired[str],
        "monthlyRecurringCost": NotRequired[str],
        "licenseModel": NotRequired[str],
        "databaseEdition": NotRequired[str],
        "databaseEngine": NotRequired[str],
        "deploymentOption": NotRequired[str],
    },
)
RedshiftReservedInstancesConfigurationTypeDef = TypedDict(
    "RedshiftReservedInstancesConfigurationTypeDef",
    {
        "accountScope": NotRequired[str],
        "service": NotRequired[str],
        "normalizedUnitsToPurchase": NotRequired[str],
        "term": NotRequired[str],
        "paymentOption": NotRequired[str],
        "numberOfInstancesToPurchase": NotRequired[str],
        "instanceFamily": NotRequired[str],
        "instanceType": NotRequired[str],
        "reservedInstancesRegion": NotRequired[str],
        "sizeFlexEligible": NotRequired[bool],
        "currentGeneration": NotRequired[str],
        "upfrontCost": NotRequired[str],
        "monthlyRecurringCost": NotRequired[str],
    },
)
ReservedInstancesPricingTypeDef = TypedDict(
    "ReservedInstancesPricingTypeDef",
    {
        "estimatedOnDemandCost": NotRequired[float],
        "monthlyReservationEligibleCost": NotRequired[float],
        "savingsPercentage": NotRequired[float],
        "estimatedMonthlyAmortizedReservationCost": NotRequired[float],
    },
)
UsageTypeDef = TypedDict(
    "UsageTypeDef",
    {
        "usageType": NotRequired[str],
        "usageAmount": NotRequired[float],
        "operation": NotRequired[str],
        "productCode": NotRequired[str],
        "unit": NotRequired[str],
    },
)
SageMakerSavingsPlansConfigurationTypeDef = TypedDict(
    "SageMakerSavingsPlansConfigurationTypeDef",
    {
        "accountScope": NotRequired[str],
        "term": NotRequired[str],
        "paymentOption": NotRequired[str],
        "hourlyCommitment": NotRequired[str],
    },
)
SavingsPlansPricingTypeDef = TypedDict(
    "SavingsPlansPricingTypeDef",
    {
        "monthlySavingsPlansEligibleCost": NotRequired[float],
        "estimatedMonthlyCommitment": NotRequired[float],
        "savingsPercentage": NotRequired[float],
        "estimatedOnDemandCost": NotRequired[float],
    },
)
UpdateEnrollmentStatusRequestRequestTypeDef = TypedDict(
    "UpdateEnrollmentStatusRequestRequestTypeDef",
    {
        "status": EnrollmentStatusType,
        "includeMemberAccounts": NotRequired[bool],
    },
)
UpdatePreferencesRequestRequestTypeDef = TypedDict(
    "UpdatePreferencesRequestRequestTypeDef",
    {
        "savingsEstimationMode": NotRequired[SavingsEstimationModeType],
        "memberAccountDiscountVisibility": NotRequired[MemberAccountDiscountVisibilityType],
    },
)
EcsServiceConfigurationTypeDef = TypedDict(
    "EcsServiceConfigurationTypeDef",
    {
        "compute": NotRequired[ComputeConfigurationTypeDef],
    },
)
LambdaFunctionConfigurationTypeDef = TypedDict(
    "LambdaFunctionConfigurationTypeDef",
    {
        "compute": NotRequired[ComputeConfigurationTypeDef],
    },
)
RdsDbInstanceConfigurationTypeDef = TypedDict(
    "RdsDbInstanceConfigurationTypeDef",
    {
        "instance": NotRequired[DbInstanceConfigurationTypeDef],
    },
)
EbsVolumeConfigurationTypeDef = TypedDict(
    "EbsVolumeConfigurationTypeDef",
    {
        "storage": NotRequired[StorageConfigurationTypeDef],
        "performance": NotRequired[BlockStoragePerformanceConfigurationTypeDef],
        "attachmentState": NotRequired[str],
    },
)
Ec2AutoScalingGroupConfigurationTypeDef = TypedDict(
    "Ec2AutoScalingGroupConfigurationTypeDef",
    {
        "instance": NotRequired[InstanceConfigurationTypeDef],
    },
)
Ec2InstanceConfigurationTypeDef = TypedDict(
    "Ec2InstanceConfigurationTypeDef",
    {
        "instance": NotRequired[InstanceConfigurationTypeDef],
    },
)
ResourcePricingTypeDef = TypedDict(
    "ResourcePricingTypeDef",
    {
        "estimatedCostBeforeDiscounts": NotRequired[float],
        "estimatedNetUnusedAmortizedCommitments": NotRequired[float],
        "estimatedDiscounts": NotRequired[EstimatedDiscountsTypeDef],
        "estimatedCostAfterDiscounts": NotRequired[float],
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "restartNeeded": NotRequired[bool],
        "rollbackPossible": NotRequired[bool],
        "implementationEfforts": NotRequired[Sequence[ImplementationEffortType]],
        "accountIds": NotRequired[Sequence[str]],
        "regions": NotRequired[Sequence[str]],
        "resourceTypes": NotRequired[Sequence[ResourceTypeType]],
        "actionTypes": NotRequired[Sequence[ActionTypeType]],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "resourceIds": NotRequired[Sequence[str]],
        "resourceArns": NotRequired[Sequence[str]],
        "recommendationIds": NotRequired[Sequence[str]],
    },
)
RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "recommendationId": NotRequired[str],
        "accountId": NotRequired[str],
        "region": NotRequired[str],
        "resourceId": NotRequired[str],
        "resourceArn": NotRequired[str],
        "currentResourceType": NotRequired[str],
        "recommendedResourceType": NotRequired[str],
        "estimatedMonthlySavings": NotRequired[float],
        "estimatedSavingsPercentage": NotRequired[float],
        "estimatedMonthlyCost": NotRequired[float],
        "currencyCode": NotRequired[str],
        "implementationEffort": NotRequired[str],
        "restartNeeded": NotRequired[bool],
        "actionType": NotRequired[str],
        "rollbackPossible": NotRequired[bool],
        "currentResourceSummary": NotRequired[str],
        "recommendedResourceSummary": NotRequired[str],
        "lastRefreshTimestamp": NotRequired[datetime],
        "recommendationLookbackPeriodInDays": NotRequired[int],
        "source": NotRequired[SourceType],
        "tags": NotRequired[List[TagTypeDef]],
    },
)
GetPreferencesResponseTypeDef = TypedDict(
    "GetPreferencesResponseTypeDef",
    {
        "savingsEstimationMode": SavingsEstimationModeType,
        "memberAccountDiscountVisibility": MemberAccountDiscountVisibilityType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEnrollmentStatusesResponseTypeDef = TypedDict(
    "ListEnrollmentStatusesResponseTypeDef",
    {
        "items": List[AccountEnrollmentStatusTypeDef],
        "includeMemberAccounts": bool,
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEnrollmentStatusResponseTypeDef = TypedDict(
    "UpdateEnrollmentStatusResponseTypeDef",
    {
        "status": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePreferencesResponseTypeDef = TypedDict(
    "UpdatePreferencesResponseTypeDef",
    {
        "savingsEstimationMode": SavingsEstimationModeType,
        "memberAccountDiscountVisibility": MemberAccountDiscountVisibilityType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEnrollmentStatusesRequestListEnrollmentStatusesPaginateTypeDef = TypedDict(
    "ListEnrollmentStatusesRequestListEnrollmentStatusesPaginateTypeDef",
    {
        "includeOrganizationInfo": NotRequired[bool],
        "accountId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRecommendationSummariesResponseTypeDef = TypedDict(
    "ListRecommendationSummariesResponseTypeDef",
    {
        "estimatedTotalDedupedSavings": float,
        "items": List[RecommendationSummaryTypeDef],
        "groupBy": str,
        "currencyCode": str,
        "metrics": SummaryMetricsResultTypeDef,
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReservedInstancesCostCalculationTypeDef = TypedDict(
    "ReservedInstancesCostCalculationTypeDef",
    {
        "pricing": NotRequired[ReservedInstancesPricingTypeDef],
    },
)
SavingsPlansCostCalculationTypeDef = TypedDict(
    "SavingsPlansCostCalculationTypeDef",
    {
        "pricing": NotRequired[SavingsPlansPricingTypeDef],
    },
)
ResourceCostCalculationTypeDef = TypedDict(
    "ResourceCostCalculationTypeDef",
    {
        "usages": NotRequired[List[UsageTypeDef]],
        "pricing": NotRequired[ResourcePricingTypeDef],
    },
)
ListRecommendationSummariesRequestListRecommendationSummariesPaginateTypeDef = TypedDict(
    "ListRecommendationSummariesRequestListRecommendationSummariesPaginateTypeDef",
    {
        "groupBy": str,
        "filter": NotRequired[FilterTypeDef],
        "metrics": NotRequired[Sequence[Literal["SavingsPercentage"]]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRecommendationSummariesRequestRequestTypeDef = TypedDict(
    "ListRecommendationSummariesRequestRequestTypeDef",
    {
        "groupBy": str,
        "filter": NotRequired[FilterTypeDef],
        "maxResults": NotRequired[int],
        "metrics": NotRequired[Sequence[Literal["SavingsPercentage"]]],
        "nextToken": NotRequired[str],
    },
)
ListRecommendationsRequestListRecommendationsPaginateTypeDef = TypedDict(
    "ListRecommendationsRequestListRecommendationsPaginateTypeDef",
    {
        "filter": NotRequired[FilterTypeDef],
        "orderBy": NotRequired[OrderByTypeDef],
        "includeAllRecommendations": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRecommendationsRequestRequestTypeDef = TypedDict(
    "ListRecommendationsRequestRequestTypeDef",
    {
        "filter": NotRequired[FilterTypeDef],
        "orderBy": NotRequired[OrderByTypeDef],
        "includeAllRecommendations": NotRequired[bool],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListRecommendationsResponseTypeDef = TypedDict(
    "ListRecommendationsResponseTypeDef",
    {
        "items": List[RecommendationTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
Ec2ReservedInstancesTypeDef = TypedDict(
    "Ec2ReservedInstancesTypeDef",
    {
        "configuration": NotRequired[Ec2ReservedInstancesConfigurationTypeDef],
        "costCalculation": NotRequired[ReservedInstancesCostCalculationTypeDef],
    },
)
ElastiCacheReservedInstancesTypeDef = TypedDict(
    "ElastiCacheReservedInstancesTypeDef",
    {
        "configuration": NotRequired[ElastiCacheReservedInstancesConfigurationTypeDef],
        "costCalculation": NotRequired[ReservedInstancesCostCalculationTypeDef],
    },
)
OpenSearchReservedInstancesTypeDef = TypedDict(
    "OpenSearchReservedInstancesTypeDef",
    {
        "configuration": NotRequired[OpenSearchReservedInstancesConfigurationTypeDef],
        "costCalculation": NotRequired[ReservedInstancesCostCalculationTypeDef],
    },
)
RdsReservedInstancesTypeDef = TypedDict(
    "RdsReservedInstancesTypeDef",
    {
        "configuration": NotRequired[RdsReservedInstancesConfigurationTypeDef],
        "costCalculation": NotRequired[ReservedInstancesCostCalculationTypeDef],
    },
)
RedshiftReservedInstancesTypeDef = TypedDict(
    "RedshiftReservedInstancesTypeDef",
    {
        "configuration": NotRequired[RedshiftReservedInstancesConfigurationTypeDef],
        "costCalculation": NotRequired[ReservedInstancesCostCalculationTypeDef],
    },
)
ComputeSavingsPlansTypeDef = TypedDict(
    "ComputeSavingsPlansTypeDef",
    {
        "configuration": NotRequired[ComputeSavingsPlansConfigurationTypeDef],
        "costCalculation": NotRequired[SavingsPlansCostCalculationTypeDef],
    },
)
Ec2InstanceSavingsPlansTypeDef = TypedDict(
    "Ec2InstanceSavingsPlansTypeDef",
    {
        "configuration": NotRequired[Ec2InstanceSavingsPlansConfigurationTypeDef],
        "costCalculation": NotRequired[SavingsPlansCostCalculationTypeDef],
    },
)
SageMakerSavingsPlansTypeDef = TypedDict(
    "SageMakerSavingsPlansTypeDef",
    {
        "configuration": NotRequired[SageMakerSavingsPlansConfigurationTypeDef],
        "costCalculation": NotRequired[SavingsPlansCostCalculationTypeDef],
    },
)
EbsVolumeTypeDef = TypedDict(
    "EbsVolumeTypeDef",
    {
        "configuration": NotRequired[EbsVolumeConfigurationTypeDef],
        "costCalculation": NotRequired[ResourceCostCalculationTypeDef],
    },
)
Ec2AutoScalingGroupTypeDef = TypedDict(
    "Ec2AutoScalingGroupTypeDef",
    {
        "configuration": NotRequired[Ec2AutoScalingGroupConfigurationTypeDef],
        "costCalculation": NotRequired[ResourceCostCalculationTypeDef],
    },
)
Ec2InstanceTypeDef = TypedDict(
    "Ec2InstanceTypeDef",
    {
        "configuration": NotRequired[Ec2InstanceConfigurationTypeDef],
        "costCalculation": NotRequired[ResourceCostCalculationTypeDef],
    },
)
EcsServiceTypeDef = TypedDict(
    "EcsServiceTypeDef",
    {
        "configuration": NotRequired[EcsServiceConfigurationTypeDef],
        "costCalculation": NotRequired[ResourceCostCalculationTypeDef],
    },
)
LambdaFunctionTypeDef = TypedDict(
    "LambdaFunctionTypeDef",
    {
        "configuration": NotRequired[LambdaFunctionConfigurationTypeDef],
        "costCalculation": NotRequired[ResourceCostCalculationTypeDef],
    },
)
RdsDbInstanceStorageTypeDef = TypedDict(
    "RdsDbInstanceStorageTypeDef",
    {
        "configuration": NotRequired[RdsDbInstanceStorageConfigurationTypeDef],
        "costCalculation": NotRequired[ResourceCostCalculationTypeDef],
    },
)
RdsDbInstanceTypeDef = TypedDict(
    "RdsDbInstanceTypeDef",
    {
        "configuration": NotRequired[RdsDbInstanceConfigurationTypeDef],
        "costCalculation": NotRequired[ResourceCostCalculationTypeDef],
    },
)
ResourceDetailsTypeDef = TypedDict(
    "ResourceDetailsTypeDef",
    {
        "lambdaFunction": NotRequired[LambdaFunctionTypeDef],
        "ecsService": NotRequired[EcsServiceTypeDef],
        "ec2Instance": NotRequired[Ec2InstanceTypeDef],
        "ebsVolume": NotRequired[EbsVolumeTypeDef],
        "ec2AutoScalingGroup": NotRequired[Ec2AutoScalingGroupTypeDef],
        "ec2ReservedInstances": NotRequired[Ec2ReservedInstancesTypeDef],
        "rdsReservedInstances": NotRequired[RdsReservedInstancesTypeDef],
        "elastiCacheReservedInstances": NotRequired[ElastiCacheReservedInstancesTypeDef],
        "openSearchReservedInstances": NotRequired[OpenSearchReservedInstancesTypeDef],
        "redshiftReservedInstances": NotRequired[RedshiftReservedInstancesTypeDef],
        "ec2InstanceSavingsPlans": NotRequired[Ec2InstanceSavingsPlansTypeDef],
        "computeSavingsPlans": NotRequired[ComputeSavingsPlansTypeDef],
        "sageMakerSavingsPlans": NotRequired[SageMakerSavingsPlansTypeDef],
        "rdsDbInstance": NotRequired[RdsDbInstanceTypeDef],
        "rdsDbInstanceStorage": NotRequired[RdsDbInstanceStorageTypeDef],
    },
)
GetRecommendationResponseTypeDef = TypedDict(
    "GetRecommendationResponseTypeDef",
    {
        "recommendationId": str,
        "resourceId": str,
        "resourceArn": str,
        "accountId": str,
        "currencyCode": str,
        "recommendationLookbackPeriodInDays": int,
        "costCalculationLookbackPeriodInDays": int,
        "estimatedSavingsPercentage": float,
        "estimatedSavingsOverCostCalculationLookbackPeriod": float,
        "currentResourceType": ResourceTypeType,
        "recommendedResourceType": ResourceTypeType,
        "region": str,
        "source": SourceType,
        "lastRefreshTimestamp": datetime,
        "estimatedMonthlySavings": float,
        "estimatedMonthlyCost": float,
        "implementationEffort": ImplementationEffortType,
        "restartNeeded": bool,
        "actionType": ActionTypeType,
        "rollbackPossible": bool,
        "currentResourceDetails": ResourceDetailsTypeDef,
        "recommendedResourceDetails": ResourceDetailsTypeDef,
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
