"""
Type annotations for autoscaling-plans service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/type_defs/)

Usage::

    ```python
    from mypy_boto3_autoscaling_plans.type_defs import TagFilterOutputTypeDef

    data: TagFilterOutputTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    ForecastDataTypeType,
    LoadMetricTypeType,
    MetricStatisticType,
    PredictiveScalingMaxCapacityBehaviorType,
    PredictiveScalingModeType,
    ScalableDimensionType,
    ScalingMetricTypeType,
    ScalingPlanStatusCodeType,
    ScalingPolicyUpdateBehaviorType,
    ScalingStatusCodeType,
    ServiceNamespaceType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "TagFilterOutputTypeDef",
    "ResponseMetadataTypeDef",
    "MetricDimensionTypeDef",
    "DatapointTypeDef",
    "DeleteScalingPlanRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeScalingPlanResourcesRequestRequestTypeDef",
    "TimestampTypeDef",
    "PredefinedLoadMetricSpecificationTypeDef",
    "PredefinedScalingMetricSpecificationTypeDef",
    "TagFilterTypeDef",
    "ApplicationSourceOutputTypeDef",
    "CreateScalingPlanResponseTypeDef",
    "CustomizedLoadMetricSpecificationOutputTypeDef",
    "CustomizedLoadMetricSpecificationTypeDef",
    "CustomizedScalingMetricSpecificationOutputTypeDef",
    "CustomizedScalingMetricSpecificationTypeDef",
    "GetScalingPlanResourceForecastDataResponseTypeDef",
    "DescribeScalingPlanResourcesRequestDescribeScalingPlanResourcesPaginateTypeDef",
    "GetScalingPlanResourceForecastDataRequestRequestTypeDef",
    "TagFilterUnionTypeDef",
    "CustomizedLoadMetricSpecificationUnionTypeDef",
    "TargetTrackingConfigurationOutputTypeDef",
    "CustomizedScalingMetricSpecificationUnionTypeDef",
    "ApplicationSourceTypeDef",
    "ScalingInstructionOutputTypeDef",
    "ScalingPolicyTypeDef",
    "TargetTrackingConfigurationTypeDef",
    "ApplicationSourceUnionTypeDef",
    "DescribeScalingPlansRequestDescribeScalingPlansPaginateTypeDef",
    "ScalingPlanTypeDef",
    "ScalingPlanResourceTypeDef",
    "TargetTrackingConfigurationUnionTypeDef",
    "DescribeScalingPlansRequestRequestTypeDef",
    "DescribeScalingPlansResponseTypeDef",
    "DescribeScalingPlanResourcesResponseTypeDef",
    "ScalingInstructionTypeDef",
    "ScalingInstructionUnionTypeDef",
    "UpdateScalingPlanRequestRequestTypeDef",
    "CreateScalingPlanRequestRequestTypeDef",
)

TagFilterOutputTypeDef = TypedDict(
    "TagFilterOutputTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[List[str]],
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
MetricDimensionTypeDef = TypedDict(
    "MetricDimensionTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)
DatapointTypeDef = TypedDict(
    "DatapointTypeDef",
    {
        "Timestamp": NotRequired[datetime],
        "Value": NotRequired[float],
    },
)
DeleteScalingPlanRequestRequestTypeDef = TypedDict(
    "DeleteScalingPlanRequestRequestTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
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
DescribeScalingPlanResourcesRequestRequestTypeDef = TypedDict(
    "DescribeScalingPlanResourcesRequestRequestTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
PredefinedLoadMetricSpecificationTypeDef = TypedDict(
    "PredefinedLoadMetricSpecificationTypeDef",
    {
        "PredefinedLoadMetricType": LoadMetricTypeType,
        "ResourceLabel": NotRequired[str],
    },
)
PredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "PredefinedScalingMetricSpecificationTypeDef",
    {
        "PredefinedScalingMetricType": ScalingMetricTypeType,
        "ResourceLabel": NotRequired[str],
    },
)
TagFilterTypeDef = TypedDict(
    "TagFilterTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)
ApplicationSourceOutputTypeDef = TypedDict(
    "ApplicationSourceOutputTypeDef",
    {
        "CloudFormationStackARN": NotRequired[str],
        "TagFilters": NotRequired[List[TagFilterOutputTypeDef]],
    },
)
CreateScalingPlanResponseTypeDef = TypedDict(
    "CreateScalingPlanResponseTypeDef",
    {
        "ScalingPlanVersion": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CustomizedLoadMetricSpecificationOutputTypeDef = TypedDict(
    "CustomizedLoadMetricSpecificationOutputTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Statistic": MetricStatisticType,
        "Dimensions": NotRequired[List[MetricDimensionTypeDef]],
        "Unit": NotRequired[str],
    },
)
CustomizedLoadMetricSpecificationTypeDef = TypedDict(
    "CustomizedLoadMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Statistic": MetricStatisticType,
        "Dimensions": NotRequired[Sequence[MetricDimensionTypeDef]],
        "Unit": NotRequired[str],
    },
)
CustomizedScalingMetricSpecificationOutputTypeDef = TypedDict(
    "CustomizedScalingMetricSpecificationOutputTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Statistic": MetricStatisticType,
        "Dimensions": NotRequired[List[MetricDimensionTypeDef]],
        "Unit": NotRequired[str],
    },
)
CustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "CustomizedScalingMetricSpecificationTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Statistic": MetricStatisticType,
        "Dimensions": NotRequired[Sequence[MetricDimensionTypeDef]],
        "Unit": NotRequired[str],
    },
)
GetScalingPlanResourceForecastDataResponseTypeDef = TypedDict(
    "GetScalingPlanResourceForecastDataResponseTypeDef",
    {
        "Datapoints": List[DatapointTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeScalingPlanResourcesRequestDescribeScalingPlanResourcesPaginateTypeDef = TypedDict(
    "DescribeScalingPlanResourcesRequestDescribeScalingPlanResourcesPaginateTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetScalingPlanResourceForecastDataRequestRequestTypeDef = TypedDict(
    "GetScalingPlanResourceForecastDataRequestRequestTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "ForecastDataType": ForecastDataTypeType,
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
    },
)
TagFilterUnionTypeDef = Union[TagFilterTypeDef, TagFilterOutputTypeDef]
CustomizedLoadMetricSpecificationUnionTypeDef = Union[
    CustomizedLoadMetricSpecificationTypeDef, CustomizedLoadMetricSpecificationOutputTypeDef
]
TargetTrackingConfigurationOutputTypeDef = TypedDict(
    "TargetTrackingConfigurationOutputTypeDef",
    {
        "TargetValue": float,
        "PredefinedScalingMetricSpecification": NotRequired[
            PredefinedScalingMetricSpecificationTypeDef
        ],
        "CustomizedScalingMetricSpecification": NotRequired[
            CustomizedScalingMetricSpecificationOutputTypeDef
        ],
        "DisableScaleIn": NotRequired[bool],
        "ScaleOutCooldown": NotRequired[int],
        "ScaleInCooldown": NotRequired[int],
        "EstimatedInstanceWarmup": NotRequired[int],
    },
)
CustomizedScalingMetricSpecificationUnionTypeDef = Union[
    CustomizedScalingMetricSpecificationTypeDef, CustomizedScalingMetricSpecificationOutputTypeDef
]
ApplicationSourceTypeDef = TypedDict(
    "ApplicationSourceTypeDef",
    {
        "CloudFormationStackARN": NotRequired[str],
        "TagFilters": NotRequired[Sequence[TagFilterUnionTypeDef]],
    },
)
ScalingInstructionOutputTypeDef = TypedDict(
    "ScalingInstructionOutputTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "MinCapacity": int,
        "MaxCapacity": int,
        "TargetTrackingConfigurations": List[TargetTrackingConfigurationOutputTypeDef],
        "PredefinedLoadMetricSpecification": NotRequired[PredefinedLoadMetricSpecificationTypeDef],
        "CustomizedLoadMetricSpecification": NotRequired[
            CustomizedLoadMetricSpecificationOutputTypeDef
        ],
        "ScheduledActionBufferTime": NotRequired[int],
        "PredictiveScalingMaxCapacityBehavior": NotRequired[
            PredictiveScalingMaxCapacityBehaviorType
        ],
        "PredictiveScalingMaxCapacityBuffer": NotRequired[int],
        "PredictiveScalingMode": NotRequired[PredictiveScalingModeType],
        "ScalingPolicyUpdateBehavior": NotRequired[ScalingPolicyUpdateBehaviorType],
        "DisableDynamicScaling": NotRequired[bool],
    },
)
ScalingPolicyTypeDef = TypedDict(
    "ScalingPolicyTypeDef",
    {
        "PolicyName": str,
        "PolicyType": Literal["TargetTrackingScaling"],
        "TargetTrackingConfiguration": NotRequired[TargetTrackingConfigurationOutputTypeDef],
    },
)
TargetTrackingConfigurationTypeDef = TypedDict(
    "TargetTrackingConfigurationTypeDef",
    {
        "TargetValue": float,
        "PredefinedScalingMetricSpecification": NotRequired[
            PredefinedScalingMetricSpecificationTypeDef
        ],
        "CustomizedScalingMetricSpecification": NotRequired[
            CustomizedScalingMetricSpecificationUnionTypeDef
        ],
        "DisableScaleIn": NotRequired[bool],
        "ScaleOutCooldown": NotRequired[int],
        "ScaleInCooldown": NotRequired[int],
        "EstimatedInstanceWarmup": NotRequired[int],
    },
)
ApplicationSourceUnionTypeDef = Union[ApplicationSourceTypeDef, ApplicationSourceOutputTypeDef]
DescribeScalingPlansRequestDescribeScalingPlansPaginateTypeDef = TypedDict(
    "DescribeScalingPlansRequestDescribeScalingPlansPaginateTypeDef",
    {
        "ScalingPlanNames": NotRequired[Sequence[str]],
        "ScalingPlanVersion": NotRequired[int],
        "ApplicationSources": NotRequired[Sequence[ApplicationSourceTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ScalingPlanTypeDef = TypedDict(
    "ScalingPlanTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ApplicationSource": ApplicationSourceOutputTypeDef,
        "ScalingInstructions": List[ScalingInstructionOutputTypeDef],
        "StatusCode": ScalingPlanStatusCodeType,
        "StatusMessage": NotRequired[str],
        "StatusStartTime": NotRequired[datetime],
        "CreationTime": NotRequired[datetime],
    },
)
ScalingPlanResourceTypeDef = TypedDict(
    "ScalingPlanResourceTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "ScalingStatusCode": ScalingStatusCodeType,
        "ScalingPolicies": NotRequired[List[ScalingPolicyTypeDef]],
        "ScalingStatusMessage": NotRequired[str],
    },
)
TargetTrackingConfigurationUnionTypeDef = Union[
    TargetTrackingConfigurationTypeDef, TargetTrackingConfigurationOutputTypeDef
]
DescribeScalingPlansRequestRequestTypeDef = TypedDict(
    "DescribeScalingPlansRequestRequestTypeDef",
    {
        "ScalingPlanNames": NotRequired[Sequence[str]],
        "ScalingPlanVersion": NotRequired[int],
        "ApplicationSources": NotRequired[Sequence[ApplicationSourceUnionTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeScalingPlansResponseTypeDef = TypedDict(
    "DescribeScalingPlansResponseTypeDef",
    {
        "ScalingPlans": List[ScalingPlanTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeScalingPlanResourcesResponseTypeDef = TypedDict(
    "DescribeScalingPlanResourcesResponseTypeDef",
    {
        "ScalingPlanResources": List[ScalingPlanResourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ScalingInstructionTypeDef = TypedDict(
    "ScalingInstructionTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "MinCapacity": int,
        "MaxCapacity": int,
        "TargetTrackingConfigurations": Sequence[TargetTrackingConfigurationUnionTypeDef],
        "PredefinedLoadMetricSpecification": NotRequired[PredefinedLoadMetricSpecificationTypeDef],
        "CustomizedLoadMetricSpecification": NotRequired[
            CustomizedLoadMetricSpecificationUnionTypeDef
        ],
        "ScheduledActionBufferTime": NotRequired[int],
        "PredictiveScalingMaxCapacityBehavior": NotRequired[
            PredictiveScalingMaxCapacityBehaviorType
        ],
        "PredictiveScalingMaxCapacityBuffer": NotRequired[int],
        "PredictiveScalingMode": NotRequired[PredictiveScalingModeType],
        "ScalingPolicyUpdateBehavior": NotRequired[ScalingPolicyUpdateBehaviorType],
        "DisableDynamicScaling": NotRequired[bool],
    },
)
ScalingInstructionUnionTypeDef = Union[ScalingInstructionTypeDef, ScalingInstructionOutputTypeDef]
UpdateScalingPlanRequestRequestTypeDef = TypedDict(
    "UpdateScalingPlanRequestRequestTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ApplicationSource": NotRequired[ApplicationSourceTypeDef],
        "ScalingInstructions": NotRequired[Sequence[ScalingInstructionTypeDef]],
    },
)
CreateScalingPlanRequestRequestTypeDef = TypedDict(
    "CreateScalingPlanRequestRequestTypeDef",
    {
        "ScalingPlanName": str,
        "ApplicationSource": ApplicationSourceTypeDef,
        "ScalingInstructions": Sequence[ScalingInstructionUnionTypeDef],
    },
)
