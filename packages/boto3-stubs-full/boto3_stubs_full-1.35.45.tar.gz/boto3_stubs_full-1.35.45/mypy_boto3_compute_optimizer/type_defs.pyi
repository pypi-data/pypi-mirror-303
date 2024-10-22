"""
Type annotations for compute-optimizer service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/type_defs/)

Usage::

    ```python
    from mypy_boto3_compute_optimizer.type_defs import AccountEnrollmentStatusTypeDef

    data: AccountEnrollmentStatusTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    AutoScalingConfigurationType,
    CpuVendorArchitectureType,
    CurrencyType,
    CurrentPerformanceRiskType,
    CustomizableMetricHeadroomType,
    CustomizableMetricNameType,
    CustomizableMetricThresholdType,
    EBSFindingType,
    EBSMetricNameType,
    EBSSavingsEstimationModeSourceType,
    ECSSavingsEstimationModeSourceType,
    ECSServiceLaunchTypeType,
    ECSServiceMetricNameType,
    ECSServiceMetricStatisticType,
    ECSServiceRecommendationFilterNameType,
    ECSServiceRecommendationFindingReasonCodeType,
    ECSServiceRecommendationFindingType,
    EnhancedInfrastructureMetricsType,
    ExportableAutoScalingGroupFieldType,
    ExportableECSServiceFieldType,
    ExportableInstanceFieldType,
    ExportableLambdaFunctionFieldType,
    ExportableLicenseFieldType,
    ExportableRDSDBFieldType,
    ExportableVolumeFieldType,
    ExternalMetricsSourceType,
    ExternalMetricStatusCodeType,
    FilterNameType,
    FindingReasonCodeType,
    FindingType,
    IdleType,
    InferredWorkloadTypesPreferenceType,
    InferredWorkloadTypeType,
    InstanceIdleType,
    InstanceRecommendationFindingReasonCodeType,
    InstanceSavingsEstimationModeSourceType,
    InstanceStateType,
    JobFilterNameType,
    JobStatusType,
    LambdaFunctionMemoryMetricStatisticType,
    LambdaFunctionMetricNameType,
    LambdaFunctionMetricStatisticType,
    LambdaFunctionRecommendationFilterNameType,
    LambdaFunctionRecommendationFindingReasonCodeType,
    LambdaFunctionRecommendationFindingType,
    LambdaSavingsEstimationModeSourceType,
    LicenseEditionType,
    LicenseFindingReasonCodeType,
    LicenseFindingType,
    LicenseModelType,
    LicenseRecommendationFilterNameType,
    LookBackPeriodPreferenceType,
    MetricNameType,
    MetricStatisticType,
    MigrationEffortType,
    PlatformDifferenceType,
    RDSDBMetricNameType,
    RDSDBMetricStatisticType,
    RDSDBRecommendationFilterNameType,
    RDSInstanceFindingReasonCodeType,
    RDSInstanceFindingType,
    RDSSavingsEstimationModeSourceType,
    RDSStorageFindingReasonCodeType,
    RDSStorageFindingType,
    RecommendationPreferenceNameType,
    RecommendationSourceTypeType,
    ResourceTypeType,
    SavingsEstimationModeType,
    ScopeNameType,
    StatusType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AccountEnrollmentStatusTypeDef",
    "AutoScalingGroupConfigurationTypeDef",
    "AutoScalingGroupEstimatedMonthlySavingsTypeDef",
    "UtilizationMetricTypeDef",
    "MemorySizeConfigurationTypeDef",
    "CurrentPerformanceRiskRatingsTypeDef",
    "CustomizableMetricParametersTypeDef",
    "DBStorageConfigurationTypeDef",
    "ScopeTypeDef",
    "JobFilterTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "EBSSavingsEstimationModeTypeDef",
    "EBSEstimatedMonthlySavingsTypeDef",
    "EBSFilterTypeDef",
    "EBSUtilizationMetricTypeDef",
    "ECSSavingsEstimationModeTypeDef",
    "ECSEstimatedMonthlySavingsTypeDef",
    "ECSServiceProjectedMetricTypeDef",
    "ECSServiceProjectedUtilizationMetricTypeDef",
    "ECSServiceRecommendationFilterTypeDef",
    "ECSServiceUtilizationMetricTypeDef",
    "TagTypeDef",
    "EffectivePreferredResourceTypeDef",
    "ExternalMetricsPreferenceTypeDef",
    "InstanceSavingsEstimationModeTypeDef",
    "EnrollmentFilterTypeDef",
    "EstimatedMonthlySavingsTypeDef",
    "FilterTypeDef",
    "RecommendationPreferencesTypeDef",
    "S3DestinationConfigTypeDef",
    "S3DestinationTypeDef",
    "LambdaFunctionRecommendationFilterTypeDef",
    "LicenseRecommendationFilterTypeDef",
    "RDSDBRecommendationFilterTypeDef",
    "ExternalMetricStatusTypeDef",
    "GetRecommendationErrorTypeDef",
    "TimestampTypeDef",
    "GetEffectiveRecommendationPreferencesRequestRequestTypeDef",
    "GetRecommendationSummariesRequestRequestTypeDef",
    "GpuTypeDef",
    "InstanceEstimatedMonthlySavingsTypeDef",
    "RecommendationSourceTypeDef",
    "LambdaSavingsEstimationModeTypeDef",
    "LambdaEstimatedMonthlySavingsTypeDef",
    "LambdaFunctionMemoryProjectedMetricTypeDef",
    "LambdaFunctionUtilizationMetricTypeDef",
    "MetricSourceTypeDef",
    "PreferredResourceTypeDef",
    "ProjectedMetricTypeDef",
    "RDSDBUtilizationMetricTypeDef",
    "RDSDatabaseProjectedMetricTypeDef",
    "RDSSavingsEstimationModeTypeDef",
    "RDSInstanceEstimatedMonthlySavingsTypeDef",
    "RDSStorageEstimatedMonthlySavingsTypeDef",
    "ReasonCodeSummaryTypeDef",
    "UpdateEnrollmentStatusRequestRequestTypeDef",
    "VolumeConfigurationTypeDef",
    "AutoScalingGroupSavingsOpportunityAfterDiscountsTypeDef",
    "ContainerConfigurationTypeDef",
    "ContainerRecommendationTypeDef",
    "UtilizationPreferenceTypeDef",
    "DeleteRecommendationPreferencesRequestRequestTypeDef",
    "GetRecommendationPreferencesRequestRequestTypeDef",
    "DescribeRecommendationExportJobsRequestRequestTypeDef",
    "DescribeRecommendationExportJobsRequestDescribeRecommendationExportJobsPaginateTypeDef",
    "GetRecommendationPreferencesRequestGetRecommendationPreferencesPaginateTypeDef",
    "GetRecommendationSummariesRequestGetRecommendationSummariesPaginateTypeDef",
    "GetEnrollmentStatusResponseTypeDef",
    "GetEnrollmentStatusesForOrganizationResponseTypeDef",
    "UpdateEnrollmentStatusResponseTypeDef",
    "EBSEffectiveRecommendationPreferencesTypeDef",
    "EBSSavingsOpportunityAfterDiscountsTypeDef",
    "GetEBSVolumeRecommendationsRequestRequestTypeDef",
    "ECSEffectiveRecommendationPreferencesTypeDef",
    "ECSSavingsOpportunityAfterDiscountsTypeDef",
    "ECSServiceRecommendedOptionProjectedMetricTypeDef",
    "GetECSServiceRecommendationsRequestRequestTypeDef",
    "GetEnrollmentStatusesForOrganizationRequestGetEnrollmentStatusesForOrganizationPaginateTypeDef",
    "GetEnrollmentStatusesForOrganizationRequestRequestTypeDef",
    "InferredWorkloadSavingTypeDef",
    "SavingsOpportunityTypeDef",
    "GetAutoScalingGroupRecommendationsRequestRequestTypeDef",
    "GetEC2InstanceRecommendationsRequestRequestTypeDef",
    "ExportAutoScalingGroupRecommendationsRequestRequestTypeDef",
    "ExportEBSVolumeRecommendationsRequestRequestTypeDef",
    "ExportEC2InstanceRecommendationsRequestRequestTypeDef",
    "ExportECSServiceRecommendationsRequestRequestTypeDef",
    "ExportAutoScalingGroupRecommendationsResponseTypeDef",
    "ExportDestinationTypeDef",
    "ExportEBSVolumeRecommendationsResponseTypeDef",
    "ExportEC2InstanceRecommendationsResponseTypeDef",
    "ExportECSServiceRecommendationsResponseTypeDef",
    "ExportLambdaFunctionRecommendationsResponseTypeDef",
    "ExportLicenseRecommendationsResponseTypeDef",
    "ExportRDSDatabaseRecommendationsResponseTypeDef",
    "ExportLambdaFunctionRecommendationsRequestRequestTypeDef",
    "GetLambdaFunctionRecommendationsRequestGetLambdaFunctionRecommendationsPaginateTypeDef",
    "GetLambdaFunctionRecommendationsRequestRequestTypeDef",
    "ExportLicenseRecommendationsRequestRequestTypeDef",
    "GetLicenseRecommendationsRequestRequestTypeDef",
    "ExportRDSDatabaseRecommendationsRequestRequestTypeDef",
    "GetRDSDatabaseRecommendationsRequestRequestTypeDef",
    "GetEC2RecommendationProjectedMetricsRequestRequestTypeDef",
    "GetECSServiceRecommendationProjectedMetricsRequestRequestTypeDef",
    "GetRDSDatabaseRecommendationProjectedMetricsRequestRequestTypeDef",
    "GpuInfoTypeDef",
    "InstanceSavingsOpportunityAfterDiscountsTypeDef",
    "LambdaEffectiveRecommendationPreferencesTypeDef",
    "LambdaSavingsOpportunityAfterDiscountsTypeDef",
    "LicenseConfigurationTypeDef",
    "RecommendedOptionProjectedMetricTypeDef",
    "RDSDatabaseRecommendedOptionProjectedMetricTypeDef",
    "RDSEffectiveRecommendationPreferencesTypeDef",
    "RDSInstanceSavingsOpportunityAfterDiscountsTypeDef",
    "RDSStorageSavingsOpportunityAfterDiscountsTypeDef",
    "SummaryTypeDef",
    "ServiceConfigurationTypeDef",
    "EffectiveRecommendationPreferencesTypeDef",
    "GetEffectiveRecommendationPreferencesResponseTypeDef",
    "PutRecommendationPreferencesRequestRequestTypeDef",
    "RecommendationPreferencesDetailTypeDef",
    "GetECSServiceRecommendationProjectedMetricsResponseTypeDef",
    "ECSServiceRecommendationOptionTypeDef",
    "LicenseRecommendationOptionTypeDef",
    "VolumeRecommendationOptionTypeDef",
    "RecommendationExportJobTypeDef",
    "AutoScalingGroupRecommendationOptionTypeDef",
    "InstanceRecommendationOptionTypeDef",
    "LambdaFunctionMemoryRecommendationOptionTypeDef",
    "GetEC2RecommendationProjectedMetricsResponseTypeDef",
    "GetRDSDatabaseRecommendationProjectedMetricsResponseTypeDef",
    "RDSDBInstanceRecommendationOptionTypeDef",
    "RDSDBStorageRecommendationOptionTypeDef",
    "RecommendationSummaryTypeDef",
    "GetRecommendationPreferencesResponseTypeDef",
    "ECSServiceRecommendationTypeDef",
    "LicenseRecommendationTypeDef",
    "VolumeRecommendationTypeDef",
    "DescribeRecommendationExportJobsResponseTypeDef",
    "AutoScalingGroupRecommendationTypeDef",
    "InstanceRecommendationTypeDef",
    "LambdaFunctionRecommendationTypeDef",
    "RDSDBRecommendationTypeDef",
    "GetRecommendationSummariesResponseTypeDef",
    "GetECSServiceRecommendationsResponseTypeDef",
    "GetLicenseRecommendationsResponseTypeDef",
    "GetEBSVolumeRecommendationsResponseTypeDef",
    "GetAutoScalingGroupRecommendationsResponseTypeDef",
    "GetEC2InstanceRecommendationsResponseTypeDef",
    "GetLambdaFunctionRecommendationsResponseTypeDef",
    "GetRDSDatabaseRecommendationsResponseTypeDef",
)

AccountEnrollmentStatusTypeDef = TypedDict(
    "AccountEnrollmentStatusTypeDef",
    {
        "accountId": NotRequired[str],
        "status": NotRequired[StatusType],
        "statusReason": NotRequired[str],
        "lastUpdatedTimestamp": NotRequired[datetime],
    },
)
AutoScalingGroupConfigurationTypeDef = TypedDict(
    "AutoScalingGroupConfigurationTypeDef",
    {
        "desiredCapacity": NotRequired[int],
        "minSize": NotRequired[int],
        "maxSize": NotRequired[int],
        "instanceType": NotRequired[str],
    },
)
AutoScalingGroupEstimatedMonthlySavingsTypeDef = TypedDict(
    "AutoScalingGroupEstimatedMonthlySavingsTypeDef",
    {
        "currency": NotRequired[CurrencyType],
        "value": NotRequired[float],
    },
)
UtilizationMetricTypeDef = TypedDict(
    "UtilizationMetricTypeDef",
    {
        "name": NotRequired[MetricNameType],
        "statistic": NotRequired[MetricStatisticType],
        "value": NotRequired[float],
    },
)
MemorySizeConfigurationTypeDef = TypedDict(
    "MemorySizeConfigurationTypeDef",
    {
        "memory": NotRequired[int],
        "memoryReservation": NotRequired[int],
    },
)
CurrentPerformanceRiskRatingsTypeDef = TypedDict(
    "CurrentPerformanceRiskRatingsTypeDef",
    {
        "high": NotRequired[int],
        "medium": NotRequired[int],
        "low": NotRequired[int],
        "veryLow": NotRequired[int],
    },
)
CustomizableMetricParametersTypeDef = TypedDict(
    "CustomizableMetricParametersTypeDef",
    {
        "threshold": NotRequired[CustomizableMetricThresholdType],
        "headroom": NotRequired[CustomizableMetricHeadroomType],
    },
)
DBStorageConfigurationTypeDef = TypedDict(
    "DBStorageConfigurationTypeDef",
    {
        "storageType": NotRequired[str],
        "allocatedStorage": NotRequired[int],
        "iops": NotRequired[int],
        "maxAllocatedStorage": NotRequired[int],
        "storageThroughput": NotRequired[int],
    },
)
ScopeTypeDef = TypedDict(
    "ScopeTypeDef",
    {
        "name": NotRequired[ScopeNameType],
        "value": NotRequired[str],
    },
)
JobFilterTypeDef = TypedDict(
    "JobFilterTypeDef",
    {
        "name": NotRequired[JobFilterNameType],
        "values": NotRequired[Sequence[str]],
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
EBSSavingsEstimationModeTypeDef = TypedDict(
    "EBSSavingsEstimationModeTypeDef",
    {
        "source": NotRequired[EBSSavingsEstimationModeSourceType],
    },
)
EBSEstimatedMonthlySavingsTypeDef = TypedDict(
    "EBSEstimatedMonthlySavingsTypeDef",
    {
        "currency": NotRequired[CurrencyType],
        "value": NotRequired[float],
    },
)
EBSFilterTypeDef = TypedDict(
    "EBSFilterTypeDef",
    {
        "name": NotRequired[Literal["Finding"]],
        "values": NotRequired[Sequence[str]],
    },
)
EBSUtilizationMetricTypeDef = TypedDict(
    "EBSUtilizationMetricTypeDef",
    {
        "name": NotRequired[EBSMetricNameType],
        "statistic": NotRequired[MetricStatisticType],
        "value": NotRequired[float],
    },
)
ECSSavingsEstimationModeTypeDef = TypedDict(
    "ECSSavingsEstimationModeTypeDef",
    {
        "source": NotRequired[ECSSavingsEstimationModeSourceType],
    },
)
ECSEstimatedMonthlySavingsTypeDef = TypedDict(
    "ECSEstimatedMonthlySavingsTypeDef",
    {
        "currency": NotRequired[CurrencyType],
        "value": NotRequired[float],
    },
)
ECSServiceProjectedMetricTypeDef = TypedDict(
    "ECSServiceProjectedMetricTypeDef",
    {
        "name": NotRequired[ECSServiceMetricNameType],
        "timestamps": NotRequired[List[datetime]],
        "upperBoundValues": NotRequired[List[float]],
        "lowerBoundValues": NotRequired[List[float]],
    },
)
ECSServiceProjectedUtilizationMetricTypeDef = TypedDict(
    "ECSServiceProjectedUtilizationMetricTypeDef",
    {
        "name": NotRequired[ECSServiceMetricNameType],
        "statistic": NotRequired[ECSServiceMetricStatisticType],
        "lowerBoundValue": NotRequired[float],
        "upperBoundValue": NotRequired[float],
    },
)
ECSServiceRecommendationFilterTypeDef = TypedDict(
    "ECSServiceRecommendationFilterTypeDef",
    {
        "name": NotRequired[ECSServiceRecommendationFilterNameType],
        "values": NotRequired[Sequence[str]],
    },
)
ECSServiceUtilizationMetricTypeDef = TypedDict(
    "ECSServiceUtilizationMetricTypeDef",
    {
        "name": NotRequired[ECSServiceMetricNameType],
        "statistic": NotRequired[ECSServiceMetricStatisticType],
        "value": NotRequired[float],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[str],
    },
)
EffectivePreferredResourceTypeDef = TypedDict(
    "EffectivePreferredResourceTypeDef",
    {
        "name": NotRequired[Literal["Ec2InstanceTypes"]],
        "includeList": NotRequired[List[str]],
        "effectiveIncludeList": NotRequired[List[str]],
        "excludeList": NotRequired[List[str]],
    },
)
ExternalMetricsPreferenceTypeDef = TypedDict(
    "ExternalMetricsPreferenceTypeDef",
    {
        "source": NotRequired[ExternalMetricsSourceType],
    },
)
InstanceSavingsEstimationModeTypeDef = TypedDict(
    "InstanceSavingsEstimationModeTypeDef",
    {
        "source": NotRequired[InstanceSavingsEstimationModeSourceType],
    },
)
EnrollmentFilterTypeDef = TypedDict(
    "EnrollmentFilterTypeDef",
    {
        "name": NotRequired[Literal["Status"]],
        "values": NotRequired[Sequence[str]],
    },
)
EstimatedMonthlySavingsTypeDef = TypedDict(
    "EstimatedMonthlySavingsTypeDef",
    {
        "currency": NotRequired[CurrencyType],
        "value": NotRequired[float],
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "name": NotRequired[FilterNameType],
        "values": NotRequired[Sequence[str]],
    },
)
RecommendationPreferencesTypeDef = TypedDict(
    "RecommendationPreferencesTypeDef",
    {
        "cpuVendorArchitectures": NotRequired[Sequence[CpuVendorArchitectureType]],
    },
)
S3DestinationConfigTypeDef = TypedDict(
    "S3DestinationConfigTypeDef",
    {
        "bucket": NotRequired[str],
        "keyPrefix": NotRequired[str],
    },
)
S3DestinationTypeDef = TypedDict(
    "S3DestinationTypeDef",
    {
        "bucket": NotRequired[str],
        "key": NotRequired[str],
        "metadataKey": NotRequired[str],
    },
)
LambdaFunctionRecommendationFilterTypeDef = TypedDict(
    "LambdaFunctionRecommendationFilterTypeDef",
    {
        "name": NotRequired[LambdaFunctionRecommendationFilterNameType],
        "values": NotRequired[Sequence[str]],
    },
)
LicenseRecommendationFilterTypeDef = TypedDict(
    "LicenseRecommendationFilterTypeDef",
    {
        "name": NotRequired[LicenseRecommendationFilterNameType],
        "values": NotRequired[Sequence[str]],
    },
)
RDSDBRecommendationFilterTypeDef = TypedDict(
    "RDSDBRecommendationFilterTypeDef",
    {
        "name": NotRequired[RDSDBRecommendationFilterNameType],
        "values": NotRequired[Sequence[str]],
    },
)
ExternalMetricStatusTypeDef = TypedDict(
    "ExternalMetricStatusTypeDef",
    {
        "statusCode": NotRequired[ExternalMetricStatusCodeType],
        "statusReason": NotRequired[str],
    },
)
GetRecommendationErrorTypeDef = TypedDict(
    "GetRecommendationErrorTypeDef",
    {
        "identifier": NotRequired[str],
        "code": NotRequired[str],
        "message": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
GetEffectiveRecommendationPreferencesRequestRequestTypeDef = TypedDict(
    "GetEffectiveRecommendationPreferencesRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
GetRecommendationSummariesRequestRequestTypeDef = TypedDict(
    "GetRecommendationSummariesRequestRequestTypeDef",
    {
        "accountIds": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
GpuTypeDef = TypedDict(
    "GpuTypeDef",
    {
        "gpuCount": NotRequired[int],
        "gpuMemorySizeInMiB": NotRequired[int],
    },
)
InstanceEstimatedMonthlySavingsTypeDef = TypedDict(
    "InstanceEstimatedMonthlySavingsTypeDef",
    {
        "currency": NotRequired[CurrencyType],
        "value": NotRequired[float],
    },
)
RecommendationSourceTypeDef = TypedDict(
    "RecommendationSourceTypeDef",
    {
        "recommendationSourceArn": NotRequired[str],
        "recommendationSourceType": NotRequired[RecommendationSourceTypeType],
    },
)
LambdaSavingsEstimationModeTypeDef = TypedDict(
    "LambdaSavingsEstimationModeTypeDef",
    {
        "source": NotRequired[LambdaSavingsEstimationModeSourceType],
    },
)
LambdaEstimatedMonthlySavingsTypeDef = TypedDict(
    "LambdaEstimatedMonthlySavingsTypeDef",
    {
        "currency": NotRequired[CurrencyType],
        "value": NotRequired[float],
    },
)
LambdaFunctionMemoryProjectedMetricTypeDef = TypedDict(
    "LambdaFunctionMemoryProjectedMetricTypeDef",
    {
        "name": NotRequired[Literal["Duration"]],
        "statistic": NotRequired[LambdaFunctionMemoryMetricStatisticType],
        "value": NotRequired[float],
    },
)
LambdaFunctionUtilizationMetricTypeDef = TypedDict(
    "LambdaFunctionUtilizationMetricTypeDef",
    {
        "name": NotRequired[LambdaFunctionMetricNameType],
        "statistic": NotRequired[LambdaFunctionMetricStatisticType],
        "value": NotRequired[float],
    },
)
MetricSourceTypeDef = TypedDict(
    "MetricSourceTypeDef",
    {
        "provider": NotRequired[Literal["CloudWatchApplicationInsights"]],
        "providerArn": NotRequired[str],
    },
)
PreferredResourceTypeDef = TypedDict(
    "PreferredResourceTypeDef",
    {
        "name": NotRequired[Literal["Ec2InstanceTypes"]],
        "includeList": NotRequired[Sequence[str]],
        "excludeList": NotRequired[Sequence[str]],
    },
)
ProjectedMetricTypeDef = TypedDict(
    "ProjectedMetricTypeDef",
    {
        "name": NotRequired[MetricNameType],
        "timestamps": NotRequired[List[datetime]],
        "values": NotRequired[List[float]],
    },
)
RDSDBUtilizationMetricTypeDef = TypedDict(
    "RDSDBUtilizationMetricTypeDef",
    {
        "name": NotRequired[RDSDBMetricNameType],
        "statistic": NotRequired[RDSDBMetricStatisticType],
        "value": NotRequired[float],
    },
)
RDSDatabaseProjectedMetricTypeDef = TypedDict(
    "RDSDatabaseProjectedMetricTypeDef",
    {
        "name": NotRequired[RDSDBMetricNameType],
        "timestamps": NotRequired[List[datetime]],
        "values": NotRequired[List[float]],
    },
)
RDSSavingsEstimationModeTypeDef = TypedDict(
    "RDSSavingsEstimationModeTypeDef",
    {
        "source": NotRequired[RDSSavingsEstimationModeSourceType],
    },
)
RDSInstanceEstimatedMonthlySavingsTypeDef = TypedDict(
    "RDSInstanceEstimatedMonthlySavingsTypeDef",
    {
        "currency": NotRequired[CurrencyType],
        "value": NotRequired[float],
    },
)
RDSStorageEstimatedMonthlySavingsTypeDef = TypedDict(
    "RDSStorageEstimatedMonthlySavingsTypeDef",
    {
        "currency": NotRequired[CurrencyType],
        "value": NotRequired[float],
    },
)
ReasonCodeSummaryTypeDef = TypedDict(
    "ReasonCodeSummaryTypeDef",
    {
        "name": NotRequired[FindingReasonCodeType],
        "value": NotRequired[float],
    },
)
UpdateEnrollmentStatusRequestRequestTypeDef = TypedDict(
    "UpdateEnrollmentStatusRequestRequestTypeDef",
    {
        "status": StatusType,
        "includeMemberAccounts": NotRequired[bool],
    },
)
VolumeConfigurationTypeDef = TypedDict(
    "VolumeConfigurationTypeDef",
    {
        "volumeType": NotRequired[str],
        "volumeSize": NotRequired[int],
        "volumeBaselineIOPS": NotRequired[int],
        "volumeBurstIOPS": NotRequired[int],
        "volumeBaselineThroughput": NotRequired[int],
        "volumeBurstThroughput": NotRequired[int],
        "rootVolume": NotRequired[bool],
    },
)
AutoScalingGroupSavingsOpportunityAfterDiscountsTypeDef = TypedDict(
    "AutoScalingGroupSavingsOpportunityAfterDiscountsTypeDef",
    {
        "savingsOpportunityPercentage": NotRequired[float],
        "estimatedMonthlySavings": NotRequired[AutoScalingGroupEstimatedMonthlySavingsTypeDef],
    },
)
ContainerConfigurationTypeDef = TypedDict(
    "ContainerConfigurationTypeDef",
    {
        "containerName": NotRequired[str],
        "memorySizeConfiguration": NotRequired[MemorySizeConfigurationTypeDef],
        "cpu": NotRequired[int],
    },
)
ContainerRecommendationTypeDef = TypedDict(
    "ContainerRecommendationTypeDef",
    {
        "containerName": NotRequired[str],
        "memorySizeConfiguration": NotRequired[MemorySizeConfigurationTypeDef],
        "cpu": NotRequired[int],
    },
)
UtilizationPreferenceTypeDef = TypedDict(
    "UtilizationPreferenceTypeDef",
    {
        "metricName": NotRequired[CustomizableMetricNameType],
        "metricParameters": NotRequired[CustomizableMetricParametersTypeDef],
    },
)
DeleteRecommendationPreferencesRequestRequestTypeDef = TypedDict(
    "DeleteRecommendationPreferencesRequestRequestTypeDef",
    {
        "resourceType": ResourceTypeType,
        "recommendationPreferenceNames": Sequence[RecommendationPreferenceNameType],
        "scope": NotRequired[ScopeTypeDef],
    },
)
GetRecommendationPreferencesRequestRequestTypeDef = TypedDict(
    "GetRecommendationPreferencesRequestRequestTypeDef",
    {
        "resourceType": ResourceTypeType,
        "scope": NotRequired[ScopeTypeDef],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
DescribeRecommendationExportJobsRequestRequestTypeDef = TypedDict(
    "DescribeRecommendationExportJobsRequestRequestTypeDef",
    {
        "jobIds": NotRequired[Sequence[str]],
        "filters": NotRequired[Sequence[JobFilterTypeDef]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
DescribeRecommendationExportJobsRequestDescribeRecommendationExportJobsPaginateTypeDef = TypedDict(
    "DescribeRecommendationExportJobsRequestDescribeRecommendationExportJobsPaginateTypeDef",
    {
        "jobIds": NotRequired[Sequence[str]],
        "filters": NotRequired[Sequence[JobFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetRecommendationPreferencesRequestGetRecommendationPreferencesPaginateTypeDef = TypedDict(
    "GetRecommendationPreferencesRequestGetRecommendationPreferencesPaginateTypeDef",
    {
        "resourceType": ResourceTypeType,
        "scope": NotRequired[ScopeTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetRecommendationSummariesRequestGetRecommendationSummariesPaginateTypeDef = TypedDict(
    "GetRecommendationSummariesRequestGetRecommendationSummariesPaginateTypeDef",
    {
        "accountIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetEnrollmentStatusResponseTypeDef = TypedDict(
    "GetEnrollmentStatusResponseTypeDef",
    {
        "status": StatusType,
        "statusReason": str,
        "memberAccountsEnrolled": bool,
        "lastUpdatedTimestamp": datetime,
        "numberOfMemberAccountsOptedIn": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEnrollmentStatusesForOrganizationResponseTypeDef = TypedDict(
    "GetEnrollmentStatusesForOrganizationResponseTypeDef",
    {
        "accountEnrollmentStatuses": List[AccountEnrollmentStatusTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEnrollmentStatusResponseTypeDef = TypedDict(
    "UpdateEnrollmentStatusResponseTypeDef",
    {
        "status": StatusType,
        "statusReason": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EBSEffectiveRecommendationPreferencesTypeDef = TypedDict(
    "EBSEffectiveRecommendationPreferencesTypeDef",
    {
        "savingsEstimationMode": NotRequired[EBSSavingsEstimationModeTypeDef],
    },
)
EBSSavingsOpportunityAfterDiscountsTypeDef = TypedDict(
    "EBSSavingsOpportunityAfterDiscountsTypeDef",
    {
        "savingsOpportunityPercentage": NotRequired[float],
        "estimatedMonthlySavings": NotRequired[EBSEstimatedMonthlySavingsTypeDef],
    },
)
GetEBSVolumeRecommendationsRequestRequestTypeDef = TypedDict(
    "GetEBSVolumeRecommendationsRequestRequestTypeDef",
    {
        "volumeArns": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filters": NotRequired[Sequence[EBSFilterTypeDef]],
        "accountIds": NotRequired[Sequence[str]],
    },
)
ECSEffectiveRecommendationPreferencesTypeDef = TypedDict(
    "ECSEffectiveRecommendationPreferencesTypeDef",
    {
        "savingsEstimationMode": NotRequired[ECSSavingsEstimationModeTypeDef],
    },
)
ECSSavingsOpportunityAfterDiscountsTypeDef = TypedDict(
    "ECSSavingsOpportunityAfterDiscountsTypeDef",
    {
        "savingsOpportunityPercentage": NotRequired[float],
        "estimatedMonthlySavings": NotRequired[ECSEstimatedMonthlySavingsTypeDef],
    },
)
ECSServiceRecommendedOptionProjectedMetricTypeDef = TypedDict(
    "ECSServiceRecommendedOptionProjectedMetricTypeDef",
    {
        "recommendedCpuUnits": NotRequired[int],
        "recommendedMemorySize": NotRequired[int],
        "projectedMetrics": NotRequired[List[ECSServiceProjectedMetricTypeDef]],
    },
)
GetECSServiceRecommendationsRequestRequestTypeDef = TypedDict(
    "GetECSServiceRecommendationsRequestRequestTypeDef",
    {
        "serviceArns": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filters": NotRequired[Sequence[ECSServiceRecommendationFilterTypeDef]],
        "accountIds": NotRequired[Sequence[str]],
    },
)
GetEnrollmentStatusesForOrganizationRequestGetEnrollmentStatusesForOrganizationPaginateTypeDef = TypedDict(
    "GetEnrollmentStatusesForOrganizationRequestGetEnrollmentStatusesForOrganizationPaginateTypeDef",
    {
        "filters": NotRequired[Sequence[EnrollmentFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetEnrollmentStatusesForOrganizationRequestRequestTypeDef = TypedDict(
    "GetEnrollmentStatusesForOrganizationRequestRequestTypeDef",
    {
        "filters": NotRequired[Sequence[EnrollmentFilterTypeDef]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
InferredWorkloadSavingTypeDef = TypedDict(
    "InferredWorkloadSavingTypeDef",
    {
        "inferredWorkloadTypes": NotRequired[List[InferredWorkloadTypeType]],
        "estimatedMonthlySavings": NotRequired[EstimatedMonthlySavingsTypeDef],
    },
)
SavingsOpportunityTypeDef = TypedDict(
    "SavingsOpportunityTypeDef",
    {
        "savingsOpportunityPercentage": NotRequired[float],
        "estimatedMonthlySavings": NotRequired[EstimatedMonthlySavingsTypeDef],
    },
)
GetAutoScalingGroupRecommendationsRequestRequestTypeDef = TypedDict(
    "GetAutoScalingGroupRecommendationsRequestRequestTypeDef",
    {
        "accountIds": NotRequired[Sequence[str]],
        "autoScalingGroupArns": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "recommendationPreferences": NotRequired[RecommendationPreferencesTypeDef],
    },
)
GetEC2InstanceRecommendationsRequestRequestTypeDef = TypedDict(
    "GetEC2InstanceRecommendationsRequestRequestTypeDef",
    {
        "instanceArns": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "accountIds": NotRequired[Sequence[str]],
        "recommendationPreferences": NotRequired[RecommendationPreferencesTypeDef],
    },
)
ExportAutoScalingGroupRecommendationsRequestRequestTypeDef = TypedDict(
    "ExportAutoScalingGroupRecommendationsRequestRequestTypeDef",
    {
        "s3DestinationConfig": S3DestinationConfigTypeDef,
        "accountIds": NotRequired[Sequence[str]],
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "fieldsToExport": NotRequired[Sequence[ExportableAutoScalingGroupFieldType]],
        "fileFormat": NotRequired[Literal["Csv"]],
        "includeMemberAccounts": NotRequired[bool],
        "recommendationPreferences": NotRequired[RecommendationPreferencesTypeDef],
    },
)
ExportEBSVolumeRecommendationsRequestRequestTypeDef = TypedDict(
    "ExportEBSVolumeRecommendationsRequestRequestTypeDef",
    {
        "s3DestinationConfig": S3DestinationConfigTypeDef,
        "accountIds": NotRequired[Sequence[str]],
        "filters": NotRequired[Sequence[EBSFilterTypeDef]],
        "fieldsToExport": NotRequired[Sequence[ExportableVolumeFieldType]],
        "fileFormat": NotRequired[Literal["Csv"]],
        "includeMemberAccounts": NotRequired[bool],
    },
)
ExportEC2InstanceRecommendationsRequestRequestTypeDef = TypedDict(
    "ExportEC2InstanceRecommendationsRequestRequestTypeDef",
    {
        "s3DestinationConfig": S3DestinationConfigTypeDef,
        "accountIds": NotRequired[Sequence[str]],
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "fieldsToExport": NotRequired[Sequence[ExportableInstanceFieldType]],
        "fileFormat": NotRequired[Literal["Csv"]],
        "includeMemberAccounts": NotRequired[bool],
        "recommendationPreferences": NotRequired[RecommendationPreferencesTypeDef],
    },
)
ExportECSServiceRecommendationsRequestRequestTypeDef = TypedDict(
    "ExportECSServiceRecommendationsRequestRequestTypeDef",
    {
        "s3DestinationConfig": S3DestinationConfigTypeDef,
        "accountIds": NotRequired[Sequence[str]],
        "filters": NotRequired[Sequence[ECSServiceRecommendationFilterTypeDef]],
        "fieldsToExport": NotRequired[Sequence[ExportableECSServiceFieldType]],
        "fileFormat": NotRequired[Literal["Csv"]],
        "includeMemberAccounts": NotRequired[bool],
    },
)
ExportAutoScalingGroupRecommendationsResponseTypeDef = TypedDict(
    "ExportAutoScalingGroupRecommendationsResponseTypeDef",
    {
        "jobId": str,
        "s3Destination": S3DestinationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportDestinationTypeDef = TypedDict(
    "ExportDestinationTypeDef",
    {
        "s3": NotRequired[S3DestinationTypeDef],
    },
)
ExportEBSVolumeRecommendationsResponseTypeDef = TypedDict(
    "ExportEBSVolumeRecommendationsResponseTypeDef",
    {
        "jobId": str,
        "s3Destination": S3DestinationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportEC2InstanceRecommendationsResponseTypeDef = TypedDict(
    "ExportEC2InstanceRecommendationsResponseTypeDef",
    {
        "jobId": str,
        "s3Destination": S3DestinationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportECSServiceRecommendationsResponseTypeDef = TypedDict(
    "ExportECSServiceRecommendationsResponseTypeDef",
    {
        "jobId": str,
        "s3Destination": S3DestinationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportLambdaFunctionRecommendationsResponseTypeDef = TypedDict(
    "ExportLambdaFunctionRecommendationsResponseTypeDef",
    {
        "jobId": str,
        "s3Destination": S3DestinationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportLicenseRecommendationsResponseTypeDef = TypedDict(
    "ExportLicenseRecommendationsResponseTypeDef",
    {
        "jobId": str,
        "s3Destination": S3DestinationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportRDSDatabaseRecommendationsResponseTypeDef = TypedDict(
    "ExportRDSDatabaseRecommendationsResponseTypeDef",
    {
        "jobId": str,
        "s3Destination": S3DestinationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportLambdaFunctionRecommendationsRequestRequestTypeDef = TypedDict(
    "ExportLambdaFunctionRecommendationsRequestRequestTypeDef",
    {
        "s3DestinationConfig": S3DestinationConfigTypeDef,
        "accountIds": NotRequired[Sequence[str]],
        "filters": NotRequired[Sequence[LambdaFunctionRecommendationFilterTypeDef]],
        "fieldsToExport": NotRequired[Sequence[ExportableLambdaFunctionFieldType]],
        "fileFormat": NotRequired[Literal["Csv"]],
        "includeMemberAccounts": NotRequired[bool],
    },
)
GetLambdaFunctionRecommendationsRequestGetLambdaFunctionRecommendationsPaginateTypeDef = TypedDict(
    "GetLambdaFunctionRecommendationsRequestGetLambdaFunctionRecommendationsPaginateTypeDef",
    {
        "functionArns": NotRequired[Sequence[str]],
        "accountIds": NotRequired[Sequence[str]],
        "filters": NotRequired[Sequence[LambdaFunctionRecommendationFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetLambdaFunctionRecommendationsRequestRequestTypeDef = TypedDict(
    "GetLambdaFunctionRecommendationsRequestRequestTypeDef",
    {
        "functionArns": NotRequired[Sequence[str]],
        "accountIds": NotRequired[Sequence[str]],
        "filters": NotRequired[Sequence[LambdaFunctionRecommendationFilterTypeDef]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ExportLicenseRecommendationsRequestRequestTypeDef = TypedDict(
    "ExportLicenseRecommendationsRequestRequestTypeDef",
    {
        "s3DestinationConfig": S3DestinationConfigTypeDef,
        "accountIds": NotRequired[Sequence[str]],
        "filters": NotRequired[Sequence[LicenseRecommendationFilterTypeDef]],
        "fieldsToExport": NotRequired[Sequence[ExportableLicenseFieldType]],
        "fileFormat": NotRequired[Literal["Csv"]],
        "includeMemberAccounts": NotRequired[bool],
    },
)
GetLicenseRecommendationsRequestRequestTypeDef = TypedDict(
    "GetLicenseRecommendationsRequestRequestTypeDef",
    {
        "resourceArns": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filters": NotRequired[Sequence[LicenseRecommendationFilterTypeDef]],
        "accountIds": NotRequired[Sequence[str]],
    },
)
ExportRDSDatabaseRecommendationsRequestRequestTypeDef = TypedDict(
    "ExportRDSDatabaseRecommendationsRequestRequestTypeDef",
    {
        "s3DestinationConfig": S3DestinationConfigTypeDef,
        "accountIds": NotRequired[Sequence[str]],
        "filters": NotRequired[Sequence[RDSDBRecommendationFilterTypeDef]],
        "fieldsToExport": NotRequired[Sequence[ExportableRDSDBFieldType]],
        "fileFormat": NotRequired[Literal["Csv"]],
        "includeMemberAccounts": NotRequired[bool],
        "recommendationPreferences": NotRequired[RecommendationPreferencesTypeDef],
    },
)
GetRDSDatabaseRecommendationsRequestRequestTypeDef = TypedDict(
    "GetRDSDatabaseRecommendationsRequestRequestTypeDef",
    {
        "resourceArns": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filters": NotRequired[Sequence[RDSDBRecommendationFilterTypeDef]],
        "accountIds": NotRequired[Sequence[str]],
        "recommendationPreferences": NotRequired[RecommendationPreferencesTypeDef],
    },
)
GetEC2RecommendationProjectedMetricsRequestRequestTypeDef = TypedDict(
    "GetEC2RecommendationProjectedMetricsRequestRequestTypeDef",
    {
        "instanceArn": str,
        "stat": MetricStatisticType,
        "period": int,
        "startTime": TimestampTypeDef,
        "endTime": TimestampTypeDef,
        "recommendationPreferences": NotRequired[RecommendationPreferencesTypeDef],
    },
)
GetECSServiceRecommendationProjectedMetricsRequestRequestTypeDef = TypedDict(
    "GetECSServiceRecommendationProjectedMetricsRequestRequestTypeDef",
    {
        "serviceArn": str,
        "stat": MetricStatisticType,
        "period": int,
        "startTime": TimestampTypeDef,
        "endTime": TimestampTypeDef,
    },
)
GetRDSDatabaseRecommendationProjectedMetricsRequestRequestTypeDef = TypedDict(
    "GetRDSDatabaseRecommendationProjectedMetricsRequestRequestTypeDef",
    {
        "resourceArn": str,
        "stat": MetricStatisticType,
        "period": int,
        "startTime": TimestampTypeDef,
        "endTime": TimestampTypeDef,
        "recommendationPreferences": NotRequired[RecommendationPreferencesTypeDef],
    },
)
GpuInfoTypeDef = TypedDict(
    "GpuInfoTypeDef",
    {
        "gpus": NotRequired[List[GpuTypeDef]],
    },
)
InstanceSavingsOpportunityAfterDiscountsTypeDef = TypedDict(
    "InstanceSavingsOpportunityAfterDiscountsTypeDef",
    {
        "savingsOpportunityPercentage": NotRequired[float],
        "estimatedMonthlySavings": NotRequired[InstanceEstimatedMonthlySavingsTypeDef],
    },
)
LambdaEffectiveRecommendationPreferencesTypeDef = TypedDict(
    "LambdaEffectiveRecommendationPreferencesTypeDef",
    {
        "savingsEstimationMode": NotRequired[LambdaSavingsEstimationModeTypeDef],
    },
)
LambdaSavingsOpportunityAfterDiscountsTypeDef = TypedDict(
    "LambdaSavingsOpportunityAfterDiscountsTypeDef",
    {
        "savingsOpportunityPercentage": NotRequired[float],
        "estimatedMonthlySavings": NotRequired[LambdaEstimatedMonthlySavingsTypeDef],
    },
)
LicenseConfigurationTypeDef = TypedDict(
    "LicenseConfigurationTypeDef",
    {
        "numberOfCores": NotRequired[int],
        "instanceType": NotRequired[str],
        "operatingSystem": NotRequired[str],
        "licenseEdition": NotRequired[LicenseEditionType],
        "licenseName": NotRequired[Literal["SQLServer"]],
        "licenseModel": NotRequired[LicenseModelType],
        "licenseVersion": NotRequired[str],
        "metricsSource": NotRequired[List[MetricSourceTypeDef]],
    },
)
RecommendedOptionProjectedMetricTypeDef = TypedDict(
    "RecommendedOptionProjectedMetricTypeDef",
    {
        "recommendedInstanceType": NotRequired[str],
        "rank": NotRequired[int],
        "projectedMetrics": NotRequired[List[ProjectedMetricTypeDef]],
    },
)
RDSDatabaseRecommendedOptionProjectedMetricTypeDef = TypedDict(
    "RDSDatabaseRecommendedOptionProjectedMetricTypeDef",
    {
        "recommendedDBInstanceClass": NotRequired[str],
        "rank": NotRequired[int],
        "projectedMetrics": NotRequired[List[RDSDatabaseProjectedMetricTypeDef]],
    },
)
RDSEffectiveRecommendationPreferencesTypeDef = TypedDict(
    "RDSEffectiveRecommendationPreferencesTypeDef",
    {
        "cpuVendorArchitectures": NotRequired[List[CpuVendorArchitectureType]],
        "enhancedInfrastructureMetrics": NotRequired[EnhancedInfrastructureMetricsType],
        "lookBackPeriod": NotRequired[LookBackPeriodPreferenceType],
        "savingsEstimationMode": NotRequired[RDSSavingsEstimationModeTypeDef],
    },
)
RDSInstanceSavingsOpportunityAfterDiscountsTypeDef = TypedDict(
    "RDSInstanceSavingsOpportunityAfterDiscountsTypeDef",
    {
        "savingsOpportunityPercentage": NotRequired[float],
        "estimatedMonthlySavings": NotRequired[RDSInstanceEstimatedMonthlySavingsTypeDef],
    },
)
RDSStorageSavingsOpportunityAfterDiscountsTypeDef = TypedDict(
    "RDSStorageSavingsOpportunityAfterDiscountsTypeDef",
    {
        "savingsOpportunityPercentage": NotRequired[float],
        "estimatedMonthlySavings": NotRequired[RDSStorageEstimatedMonthlySavingsTypeDef],
    },
)
SummaryTypeDef = TypedDict(
    "SummaryTypeDef",
    {
        "name": NotRequired[FindingType],
        "value": NotRequired[float],
        "reasonCodeSummaries": NotRequired[List[ReasonCodeSummaryTypeDef]],
    },
)
ServiceConfigurationTypeDef = TypedDict(
    "ServiceConfigurationTypeDef",
    {
        "memory": NotRequired[int],
        "cpu": NotRequired[int],
        "containerConfigurations": NotRequired[List[ContainerConfigurationTypeDef]],
        "autoScalingConfiguration": NotRequired[AutoScalingConfigurationType],
        "taskDefinitionArn": NotRequired[str],
    },
)
EffectiveRecommendationPreferencesTypeDef = TypedDict(
    "EffectiveRecommendationPreferencesTypeDef",
    {
        "cpuVendorArchitectures": NotRequired[List[CpuVendorArchitectureType]],
        "enhancedInfrastructureMetrics": NotRequired[EnhancedInfrastructureMetricsType],
        "inferredWorkloadTypes": NotRequired[InferredWorkloadTypesPreferenceType],
        "externalMetricsPreference": NotRequired[ExternalMetricsPreferenceTypeDef],
        "lookBackPeriod": NotRequired[LookBackPeriodPreferenceType],
        "utilizationPreferences": NotRequired[List[UtilizationPreferenceTypeDef]],
        "preferredResources": NotRequired[List[EffectivePreferredResourceTypeDef]],
        "savingsEstimationMode": NotRequired[InstanceSavingsEstimationModeTypeDef],
    },
)
GetEffectiveRecommendationPreferencesResponseTypeDef = TypedDict(
    "GetEffectiveRecommendationPreferencesResponseTypeDef",
    {
        "enhancedInfrastructureMetrics": EnhancedInfrastructureMetricsType,
        "externalMetricsPreference": ExternalMetricsPreferenceTypeDef,
        "lookBackPeriod": LookBackPeriodPreferenceType,
        "utilizationPreferences": List[UtilizationPreferenceTypeDef],
        "preferredResources": List[EffectivePreferredResourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutRecommendationPreferencesRequestRequestTypeDef = TypedDict(
    "PutRecommendationPreferencesRequestRequestTypeDef",
    {
        "resourceType": ResourceTypeType,
        "scope": NotRequired[ScopeTypeDef],
        "enhancedInfrastructureMetrics": NotRequired[EnhancedInfrastructureMetricsType],
        "inferredWorkloadTypes": NotRequired[InferredWorkloadTypesPreferenceType],
        "externalMetricsPreference": NotRequired[ExternalMetricsPreferenceTypeDef],
        "lookBackPeriod": NotRequired[LookBackPeriodPreferenceType],
        "utilizationPreferences": NotRequired[Sequence[UtilizationPreferenceTypeDef]],
        "preferredResources": NotRequired[Sequence[PreferredResourceTypeDef]],
        "savingsEstimationMode": NotRequired[SavingsEstimationModeType],
    },
)
RecommendationPreferencesDetailTypeDef = TypedDict(
    "RecommendationPreferencesDetailTypeDef",
    {
        "scope": NotRequired[ScopeTypeDef],
        "resourceType": NotRequired[ResourceTypeType],
        "enhancedInfrastructureMetrics": NotRequired[EnhancedInfrastructureMetricsType],
        "inferredWorkloadTypes": NotRequired[InferredWorkloadTypesPreferenceType],
        "externalMetricsPreference": NotRequired[ExternalMetricsPreferenceTypeDef],
        "lookBackPeriod": NotRequired[LookBackPeriodPreferenceType],
        "utilizationPreferences": NotRequired[List[UtilizationPreferenceTypeDef]],
        "preferredResources": NotRequired[List[EffectivePreferredResourceTypeDef]],
        "savingsEstimationMode": NotRequired[SavingsEstimationModeType],
    },
)
GetECSServiceRecommendationProjectedMetricsResponseTypeDef = TypedDict(
    "GetECSServiceRecommendationProjectedMetricsResponseTypeDef",
    {
        "recommendedOptionProjectedMetrics": List[
            ECSServiceRecommendedOptionProjectedMetricTypeDef
        ],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ECSServiceRecommendationOptionTypeDef = TypedDict(
    "ECSServiceRecommendationOptionTypeDef",
    {
        "memory": NotRequired[int],
        "cpu": NotRequired[int],
        "savingsOpportunity": NotRequired[SavingsOpportunityTypeDef],
        "savingsOpportunityAfterDiscounts": NotRequired[ECSSavingsOpportunityAfterDiscountsTypeDef],
        "projectedUtilizationMetrics": NotRequired[
            List[ECSServiceProjectedUtilizationMetricTypeDef]
        ],
        "containerRecommendations": NotRequired[List[ContainerRecommendationTypeDef]],
    },
)
LicenseRecommendationOptionTypeDef = TypedDict(
    "LicenseRecommendationOptionTypeDef",
    {
        "rank": NotRequired[int],
        "operatingSystem": NotRequired[str],
        "licenseEdition": NotRequired[LicenseEditionType],
        "licenseModel": NotRequired[LicenseModelType],
        "savingsOpportunity": NotRequired[SavingsOpportunityTypeDef],
    },
)
VolumeRecommendationOptionTypeDef = TypedDict(
    "VolumeRecommendationOptionTypeDef",
    {
        "configuration": NotRequired[VolumeConfigurationTypeDef],
        "performanceRisk": NotRequired[float],
        "rank": NotRequired[int],
        "savingsOpportunity": NotRequired[SavingsOpportunityTypeDef],
        "savingsOpportunityAfterDiscounts": NotRequired[EBSSavingsOpportunityAfterDiscountsTypeDef],
    },
)
RecommendationExportJobTypeDef = TypedDict(
    "RecommendationExportJobTypeDef",
    {
        "jobId": NotRequired[str],
        "destination": NotRequired[ExportDestinationTypeDef],
        "resourceType": NotRequired[ResourceTypeType],
        "status": NotRequired[JobStatusType],
        "creationTimestamp": NotRequired[datetime],
        "lastUpdatedTimestamp": NotRequired[datetime],
        "failureReason": NotRequired[str],
    },
)
AutoScalingGroupRecommendationOptionTypeDef = TypedDict(
    "AutoScalingGroupRecommendationOptionTypeDef",
    {
        "configuration": NotRequired[AutoScalingGroupConfigurationTypeDef],
        "instanceGpuInfo": NotRequired[GpuInfoTypeDef],
        "projectedUtilizationMetrics": NotRequired[List[UtilizationMetricTypeDef]],
        "performanceRisk": NotRequired[float],
        "rank": NotRequired[int],
        "savingsOpportunity": NotRequired[SavingsOpportunityTypeDef],
        "savingsOpportunityAfterDiscounts": NotRequired[
            AutoScalingGroupSavingsOpportunityAfterDiscountsTypeDef
        ],
        "migrationEffort": NotRequired[MigrationEffortType],
    },
)
InstanceRecommendationOptionTypeDef = TypedDict(
    "InstanceRecommendationOptionTypeDef",
    {
        "instanceType": NotRequired[str],
        "instanceGpuInfo": NotRequired[GpuInfoTypeDef],
        "projectedUtilizationMetrics": NotRequired[List[UtilizationMetricTypeDef]],
        "platformDifferences": NotRequired[List[PlatformDifferenceType]],
        "performanceRisk": NotRequired[float],
        "rank": NotRequired[int],
        "savingsOpportunity": NotRequired[SavingsOpportunityTypeDef],
        "savingsOpportunityAfterDiscounts": NotRequired[
            InstanceSavingsOpportunityAfterDiscountsTypeDef
        ],
        "migrationEffort": NotRequired[MigrationEffortType],
    },
)
LambdaFunctionMemoryRecommendationOptionTypeDef = TypedDict(
    "LambdaFunctionMemoryRecommendationOptionTypeDef",
    {
        "rank": NotRequired[int],
        "memorySize": NotRequired[int],
        "projectedUtilizationMetrics": NotRequired[
            List[LambdaFunctionMemoryProjectedMetricTypeDef]
        ],
        "savingsOpportunity": NotRequired[SavingsOpportunityTypeDef],
        "savingsOpportunityAfterDiscounts": NotRequired[
            LambdaSavingsOpportunityAfterDiscountsTypeDef
        ],
    },
)
GetEC2RecommendationProjectedMetricsResponseTypeDef = TypedDict(
    "GetEC2RecommendationProjectedMetricsResponseTypeDef",
    {
        "recommendedOptionProjectedMetrics": List[RecommendedOptionProjectedMetricTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRDSDatabaseRecommendationProjectedMetricsResponseTypeDef = TypedDict(
    "GetRDSDatabaseRecommendationProjectedMetricsResponseTypeDef",
    {
        "recommendedOptionProjectedMetrics": List[
            RDSDatabaseRecommendedOptionProjectedMetricTypeDef
        ],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RDSDBInstanceRecommendationOptionTypeDef = TypedDict(
    "RDSDBInstanceRecommendationOptionTypeDef",
    {
        "dbInstanceClass": NotRequired[str],
        "projectedUtilizationMetrics": NotRequired[List[RDSDBUtilizationMetricTypeDef]],
        "performanceRisk": NotRequired[float],
        "rank": NotRequired[int],
        "savingsOpportunity": NotRequired[SavingsOpportunityTypeDef],
        "savingsOpportunityAfterDiscounts": NotRequired[
            RDSInstanceSavingsOpportunityAfterDiscountsTypeDef
        ],
    },
)
RDSDBStorageRecommendationOptionTypeDef = TypedDict(
    "RDSDBStorageRecommendationOptionTypeDef",
    {
        "storageConfiguration": NotRequired[DBStorageConfigurationTypeDef],
        "rank": NotRequired[int],
        "savingsOpportunity": NotRequired[SavingsOpportunityTypeDef],
        "savingsOpportunityAfterDiscounts": NotRequired[
            RDSStorageSavingsOpportunityAfterDiscountsTypeDef
        ],
    },
)
RecommendationSummaryTypeDef = TypedDict(
    "RecommendationSummaryTypeDef",
    {
        "summaries": NotRequired[List[SummaryTypeDef]],
        "recommendationResourceType": NotRequired[RecommendationSourceTypeType],
        "accountId": NotRequired[str],
        "savingsOpportunity": NotRequired[SavingsOpportunityTypeDef],
        "currentPerformanceRiskRatings": NotRequired[CurrentPerformanceRiskRatingsTypeDef],
        "inferredWorkloadSavings": NotRequired[List[InferredWorkloadSavingTypeDef]],
    },
)
GetRecommendationPreferencesResponseTypeDef = TypedDict(
    "GetRecommendationPreferencesResponseTypeDef",
    {
        "nextToken": str,
        "recommendationPreferencesDetails": List[RecommendationPreferencesDetailTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ECSServiceRecommendationTypeDef = TypedDict(
    "ECSServiceRecommendationTypeDef",
    {
        "serviceArn": NotRequired[str],
        "accountId": NotRequired[str],
        "currentServiceConfiguration": NotRequired[ServiceConfigurationTypeDef],
        "utilizationMetrics": NotRequired[List[ECSServiceUtilizationMetricTypeDef]],
        "lookbackPeriodInDays": NotRequired[float],
        "launchType": NotRequired[ECSServiceLaunchTypeType],
        "lastRefreshTimestamp": NotRequired[datetime],
        "finding": NotRequired[ECSServiceRecommendationFindingType],
        "findingReasonCodes": NotRequired[List[ECSServiceRecommendationFindingReasonCodeType]],
        "serviceRecommendationOptions": NotRequired[List[ECSServiceRecommendationOptionTypeDef]],
        "currentPerformanceRisk": NotRequired[CurrentPerformanceRiskType],
        "effectiveRecommendationPreferences": NotRequired[
            ECSEffectiveRecommendationPreferencesTypeDef
        ],
        "tags": NotRequired[List[TagTypeDef]],
    },
)
LicenseRecommendationTypeDef = TypedDict(
    "LicenseRecommendationTypeDef",
    {
        "resourceArn": NotRequired[str],
        "accountId": NotRequired[str],
        "currentLicenseConfiguration": NotRequired[LicenseConfigurationTypeDef],
        "lookbackPeriodInDays": NotRequired[float],
        "lastRefreshTimestamp": NotRequired[datetime],
        "finding": NotRequired[LicenseFindingType],
        "findingReasonCodes": NotRequired[List[LicenseFindingReasonCodeType]],
        "licenseRecommendationOptions": NotRequired[List[LicenseRecommendationOptionTypeDef]],
        "tags": NotRequired[List[TagTypeDef]],
    },
)
VolumeRecommendationTypeDef = TypedDict(
    "VolumeRecommendationTypeDef",
    {
        "volumeArn": NotRequired[str],
        "accountId": NotRequired[str],
        "currentConfiguration": NotRequired[VolumeConfigurationTypeDef],
        "finding": NotRequired[EBSFindingType],
        "utilizationMetrics": NotRequired[List[EBSUtilizationMetricTypeDef]],
        "lookBackPeriodInDays": NotRequired[float],
        "volumeRecommendationOptions": NotRequired[List[VolumeRecommendationOptionTypeDef]],
        "lastRefreshTimestamp": NotRequired[datetime],
        "currentPerformanceRisk": NotRequired[CurrentPerformanceRiskType],
        "effectiveRecommendationPreferences": NotRequired[
            EBSEffectiveRecommendationPreferencesTypeDef
        ],
        "tags": NotRequired[List[TagTypeDef]],
    },
)
DescribeRecommendationExportJobsResponseTypeDef = TypedDict(
    "DescribeRecommendationExportJobsResponseTypeDef",
    {
        "recommendationExportJobs": List[RecommendationExportJobTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AutoScalingGroupRecommendationTypeDef = TypedDict(
    "AutoScalingGroupRecommendationTypeDef",
    {
        "accountId": NotRequired[str],
        "autoScalingGroupArn": NotRequired[str],
        "autoScalingGroupName": NotRequired[str],
        "finding": NotRequired[FindingType],
        "utilizationMetrics": NotRequired[List[UtilizationMetricTypeDef]],
        "lookBackPeriodInDays": NotRequired[float],
        "currentConfiguration": NotRequired[AutoScalingGroupConfigurationTypeDef],
        "currentInstanceGpuInfo": NotRequired[GpuInfoTypeDef],
        "recommendationOptions": NotRequired[List[AutoScalingGroupRecommendationOptionTypeDef]],
        "lastRefreshTimestamp": NotRequired[datetime],
        "currentPerformanceRisk": NotRequired[CurrentPerformanceRiskType],
        "effectiveRecommendationPreferences": NotRequired[
            EffectiveRecommendationPreferencesTypeDef
        ],
        "inferredWorkloadTypes": NotRequired[List[InferredWorkloadTypeType]],
    },
)
InstanceRecommendationTypeDef = TypedDict(
    "InstanceRecommendationTypeDef",
    {
        "instanceArn": NotRequired[str],
        "accountId": NotRequired[str],
        "instanceName": NotRequired[str],
        "currentInstanceType": NotRequired[str],
        "finding": NotRequired[FindingType],
        "findingReasonCodes": NotRequired[List[InstanceRecommendationFindingReasonCodeType]],
        "utilizationMetrics": NotRequired[List[UtilizationMetricTypeDef]],
        "lookBackPeriodInDays": NotRequired[float],
        "recommendationOptions": NotRequired[List[InstanceRecommendationOptionTypeDef]],
        "recommendationSources": NotRequired[List[RecommendationSourceTypeDef]],
        "lastRefreshTimestamp": NotRequired[datetime],
        "currentPerformanceRisk": NotRequired[CurrentPerformanceRiskType],
        "effectiveRecommendationPreferences": NotRequired[
            EffectiveRecommendationPreferencesTypeDef
        ],
        "inferredWorkloadTypes": NotRequired[List[InferredWorkloadTypeType]],
        "instanceState": NotRequired[InstanceStateType],
        "tags": NotRequired[List[TagTypeDef]],
        "externalMetricStatus": NotRequired[ExternalMetricStatusTypeDef],
        "currentInstanceGpuInfo": NotRequired[GpuInfoTypeDef],
        "idle": NotRequired[InstanceIdleType],
    },
)
LambdaFunctionRecommendationTypeDef = TypedDict(
    "LambdaFunctionRecommendationTypeDef",
    {
        "functionArn": NotRequired[str],
        "functionVersion": NotRequired[str],
        "accountId": NotRequired[str],
        "currentMemorySize": NotRequired[int],
        "numberOfInvocations": NotRequired[int],
        "utilizationMetrics": NotRequired[List[LambdaFunctionUtilizationMetricTypeDef]],
        "lookbackPeriodInDays": NotRequired[float],
        "lastRefreshTimestamp": NotRequired[datetime],
        "finding": NotRequired[LambdaFunctionRecommendationFindingType],
        "findingReasonCodes": NotRequired[List[LambdaFunctionRecommendationFindingReasonCodeType]],
        "memorySizeRecommendationOptions": NotRequired[
            List[LambdaFunctionMemoryRecommendationOptionTypeDef]
        ],
        "currentPerformanceRisk": NotRequired[CurrentPerformanceRiskType],
        "effectiveRecommendationPreferences": NotRequired[
            LambdaEffectiveRecommendationPreferencesTypeDef
        ],
        "tags": NotRequired[List[TagTypeDef]],
    },
)
RDSDBRecommendationTypeDef = TypedDict(
    "RDSDBRecommendationTypeDef",
    {
        "resourceArn": NotRequired[str],
        "accountId": NotRequired[str],
        "engine": NotRequired[str],
        "engineVersion": NotRequired[str],
        "currentDBInstanceClass": NotRequired[str],
        "currentStorageConfiguration": NotRequired[DBStorageConfigurationTypeDef],
        "idle": NotRequired[IdleType],
        "instanceFinding": NotRequired[RDSInstanceFindingType],
        "storageFinding": NotRequired[RDSStorageFindingType],
        "instanceFindingReasonCodes": NotRequired[List[RDSInstanceFindingReasonCodeType]],
        "storageFindingReasonCodes": NotRequired[List[RDSStorageFindingReasonCodeType]],
        "instanceRecommendationOptions": NotRequired[
            List[RDSDBInstanceRecommendationOptionTypeDef]
        ],
        "storageRecommendationOptions": NotRequired[List[RDSDBStorageRecommendationOptionTypeDef]],
        "utilizationMetrics": NotRequired[List[RDSDBUtilizationMetricTypeDef]],
        "effectiveRecommendationPreferences": NotRequired[
            RDSEffectiveRecommendationPreferencesTypeDef
        ],
        "lookbackPeriodInDays": NotRequired[float],
        "lastRefreshTimestamp": NotRequired[datetime],
        "tags": NotRequired[List[TagTypeDef]],
    },
)
GetRecommendationSummariesResponseTypeDef = TypedDict(
    "GetRecommendationSummariesResponseTypeDef",
    {
        "nextToken": str,
        "recommendationSummaries": List[RecommendationSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetECSServiceRecommendationsResponseTypeDef = TypedDict(
    "GetECSServiceRecommendationsResponseTypeDef",
    {
        "nextToken": str,
        "ecsServiceRecommendations": List[ECSServiceRecommendationTypeDef],
        "errors": List[GetRecommendationErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLicenseRecommendationsResponseTypeDef = TypedDict(
    "GetLicenseRecommendationsResponseTypeDef",
    {
        "nextToken": str,
        "licenseRecommendations": List[LicenseRecommendationTypeDef],
        "errors": List[GetRecommendationErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEBSVolumeRecommendationsResponseTypeDef = TypedDict(
    "GetEBSVolumeRecommendationsResponseTypeDef",
    {
        "nextToken": str,
        "volumeRecommendations": List[VolumeRecommendationTypeDef],
        "errors": List[GetRecommendationErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAutoScalingGroupRecommendationsResponseTypeDef = TypedDict(
    "GetAutoScalingGroupRecommendationsResponseTypeDef",
    {
        "nextToken": str,
        "autoScalingGroupRecommendations": List[AutoScalingGroupRecommendationTypeDef],
        "errors": List[GetRecommendationErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEC2InstanceRecommendationsResponseTypeDef = TypedDict(
    "GetEC2InstanceRecommendationsResponseTypeDef",
    {
        "nextToken": str,
        "instanceRecommendations": List[InstanceRecommendationTypeDef],
        "errors": List[GetRecommendationErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLambdaFunctionRecommendationsResponseTypeDef = TypedDict(
    "GetLambdaFunctionRecommendationsResponseTypeDef",
    {
        "nextToken": str,
        "lambdaFunctionRecommendations": List[LambdaFunctionRecommendationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRDSDatabaseRecommendationsResponseTypeDef = TypedDict(
    "GetRDSDatabaseRecommendationsResponseTypeDef",
    {
        "nextToken": str,
        "rdsDBRecommendations": List[RDSDBRecommendationTypeDef],
        "errors": List[GetRecommendationErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
