"""
Type annotations for application-autoscaling service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/type_defs/)

Usage::

    ```python
    from mypy_boto3_application_autoscaling.type_defs import AlarmTypeDef

    data: AlarmTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AdjustmentTypeType,
    MetricAggregationTypeType,
    MetricStatisticType,
    MetricTypeType,
    PolicyTypeType,
    ScalableDimensionType,
    ScalingActivityStatusCodeType,
    ServiceNamespaceType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AlarmTypeDef",
    "MetricDimensionTypeDef",
    "DeleteScalingPolicyRequestRequestTypeDef",
    "DeleteScheduledActionRequestRequestTypeDef",
    "DeregisterScalableTargetRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeScalableTargetsRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "DescribeScalingActivitiesRequestRequestTypeDef",
    "DescribeScalingPoliciesRequestRequestTypeDef",
    "DescribeScheduledActionsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "NotScaledReasonTypeDef",
    "PredefinedMetricSpecificationTypeDef",
    "ScalableTargetActionTypeDef",
    "TimestampTypeDef",
    "SuspendedStateTypeDef",
    "StepAdjustmentTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TargetTrackingMetricDimensionTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "DescribeScalableTargetsRequestDescribeScalableTargetsPaginateTypeDef",
    "DescribeScalingActivitiesRequestDescribeScalingActivitiesPaginateTypeDef",
    "DescribeScalingPoliciesRequestDescribeScalingPoliciesPaginateTypeDef",
    "DescribeScheduledActionsRequestDescribeScheduledActionsPaginateTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PutScalingPolicyResponseTypeDef",
    "RegisterScalableTargetResponseTypeDef",
    "ScalingActivityTypeDef",
    "ScheduledActionTypeDef",
    "PutScheduledActionRequestRequestTypeDef",
    "RegisterScalableTargetRequestRequestTypeDef",
    "ScalableTargetTypeDef",
    "StepScalingPolicyConfigurationOutputTypeDef",
    "StepScalingPolicyConfigurationTypeDef",
    "TargetTrackingMetricOutputTypeDef",
    "TargetTrackingMetricTypeDef",
    "DescribeScalingActivitiesResponseTypeDef",
    "DescribeScheduledActionsResponseTypeDef",
    "DescribeScalableTargetsResponseTypeDef",
    "TargetTrackingMetricStatOutputTypeDef",
    "TargetTrackingMetricUnionTypeDef",
    "TargetTrackingMetricDataQueryOutputTypeDef",
    "TargetTrackingMetricStatTypeDef",
    "CustomizedMetricSpecificationOutputTypeDef",
    "TargetTrackingMetricStatUnionTypeDef",
    "TargetTrackingScalingPolicyConfigurationOutputTypeDef",
    "TargetTrackingMetricDataQueryTypeDef",
    "ScalingPolicyTypeDef",
    "TargetTrackingMetricDataQueryUnionTypeDef",
    "DescribeScalingPoliciesResponseTypeDef",
    "CustomizedMetricSpecificationTypeDef",
    "CustomizedMetricSpecificationUnionTypeDef",
    "TargetTrackingScalingPolicyConfigurationTypeDef",
    "PutScalingPolicyRequestRequestTypeDef",
)

AlarmTypeDef = TypedDict(
    "AlarmTypeDef",
    {
        "AlarmName": str,
        "AlarmARN": str,
    },
)
MetricDimensionTypeDef = TypedDict(
    "MetricDimensionTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)
DeleteScalingPolicyRequestRequestTypeDef = TypedDict(
    "DeleteScalingPolicyRequestRequestTypeDef",
    {
        "PolicyName": str,
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
    },
)
DeleteScheduledActionRequestRequestTypeDef = TypedDict(
    "DeleteScheduledActionRequestRequestTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ScheduledActionName": str,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
    },
)
DeregisterScalableTargetRequestRequestTypeDef = TypedDict(
    "DeregisterScalableTargetRequestRequestTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
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
DescribeScalableTargetsRequestRequestTypeDef = TypedDict(
    "DescribeScalableTargetsRequestRequestTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceIds": NotRequired[Sequence[str]],
        "ScalableDimension": NotRequired[ScalableDimensionType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
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
DescribeScalingActivitiesRequestRequestTypeDef = TypedDict(
    "DescribeScalingActivitiesRequestRequestTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": NotRequired[str],
        "ScalableDimension": NotRequired[ScalableDimensionType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "IncludeNotScaledActivities": NotRequired[bool],
    },
)
DescribeScalingPoliciesRequestRequestTypeDef = TypedDict(
    "DescribeScalingPoliciesRequestRequestTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "PolicyNames": NotRequired[Sequence[str]],
        "ResourceId": NotRequired[str],
        "ScalableDimension": NotRequired[ScalableDimensionType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeScheduledActionsRequestRequestTypeDef = TypedDict(
    "DescribeScheduledActionsRequestRequestTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ScheduledActionNames": NotRequired[Sequence[str]],
        "ResourceId": NotRequired[str],
        "ScalableDimension": NotRequired[ScalableDimensionType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
NotScaledReasonTypeDef = TypedDict(
    "NotScaledReasonTypeDef",
    {
        "Code": str,
        "MaxCapacity": NotRequired[int],
        "MinCapacity": NotRequired[int],
        "CurrentCapacity": NotRequired[int],
    },
)
PredefinedMetricSpecificationTypeDef = TypedDict(
    "PredefinedMetricSpecificationTypeDef",
    {
        "PredefinedMetricType": MetricTypeType,
        "ResourceLabel": NotRequired[str],
    },
)
ScalableTargetActionTypeDef = TypedDict(
    "ScalableTargetActionTypeDef",
    {
        "MinCapacity": NotRequired[int],
        "MaxCapacity": NotRequired[int],
    },
)
TimestampTypeDef = Union[datetime, str]
SuspendedStateTypeDef = TypedDict(
    "SuspendedStateTypeDef",
    {
        "DynamicScalingInSuspended": NotRequired[bool],
        "DynamicScalingOutSuspended": NotRequired[bool],
        "ScheduledScalingSuspended": NotRequired[bool],
    },
)
StepAdjustmentTypeDef = TypedDict(
    "StepAdjustmentTypeDef",
    {
        "ScalingAdjustment": int,
        "MetricIntervalLowerBound": NotRequired[float],
        "MetricIntervalUpperBound": NotRequired[float],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Mapping[str, str],
    },
)
TargetTrackingMetricDimensionTypeDef = TypedDict(
    "TargetTrackingMetricDimensionTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
DescribeScalableTargetsRequestDescribeScalableTargetsPaginateTypeDef = TypedDict(
    "DescribeScalableTargetsRequestDescribeScalableTargetsPaginateTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceIds": NotRequired[Sequence[str]],
        "ScalableDimension": NotRequired[ScalableDimensionType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeScalingActivitiesRequestDescribeScalingActivitiesPaginateTypeDef = TypedDict(
    "DescribeScalingActivitiesRequestDescribeScalingActivitiesPaginateTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": NotRequired[str],
        "ScalableDimension": NotRequired[ScalableDimensionType],
        "IncludeNotScaledActivities": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeScalingPoliciesRequestDescribeScalingPoliciesPaginateTypeDef = TypedDict(
    "DescribeScalingPoliciesRequestDescribeScalingPoliciesPaginateTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "PolicyNames": NotRequired[Sequence[str]],
        "ResourceId": NotRequired[str],
        "ScalableDimension": NotRequired[ScalableDimensionType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeScheduledActionsRequestDescribeScheduledActionsPaginateTypeDef = TypedDict(
    "DescribeScheduledActionsRequestDescribeScheduledActionsPaginateTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ScheduledActionNames": NotRequired[Sequence[str]],
        "ResourceId": NotRequired[str],
        "ScalableDimension": NotRequired[ScalableDimensionType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutScalingPolicyResponseTypeDef = TypedDict(
    "PutScalingPolicyResponseTypeDef",
    {
        "PolicyARN": str,
        "Alarms": List[AlarmTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterScalableTargetResponseTypeDef = TypedDict(
    "RegisterScalableTargetResponseTypeDef",
    {
        "ScalableTargetARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ScalingActivityTypeDef = TypedDict(
    "ScalingActivityTypeDef",
    {
        "ActivityId": str,
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "Description": str,
        "Cause": str,
        "StartTime": datetime,
        "StatusCode": ScalingActivityStatusCodeType,
        "EndTime": NotRequired[datetime],
        "StatusMessage": NotRequired[str],
        "Details": NotRequired[str],
        "NotScaledReasons": NotRequired[List[NotScaledReasonTypeDef]],
    },
)
ScheduledActionTypeDef = TypedDict(
    "ScheduledActionTypeDef",
    {
        "ScheduledActionName": str,
        "ScheduledActionARN": str,
        "ServiceNamespace": ServiceNamespaceType,
        "Schedule": str,
        "ResourceId": str,
        "CreationTime": datetime,
        "Timezone": NotRequired[str],
        "ScalableDimension": NotRequired[ScalableDimensionType],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "ScalableTargetAction": NotRequired[ScalableTargetActionTypeDef],
    },
)
PutScheduledActionRequestRequestTypeDef = TypedDict(
    "PutScheduledActionRequestRequestTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ScheduledActionName": str,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "Schedule": NotRequired[str],
        "Timezone": NotRequired[str],
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "ScalableTargetAction": NotRequired[ScalableTargetActionTypeDef],
    },
)
RegisterScalableTargetRequestRequestTypeDef = TypedDict(
    "RegisterScalableTargetRequestRequestTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "MinCapacity": NotRequired[int],
        "MaxCapacity": NotRequired[int],
        "RoleARN": NotRequired[str],
        "SuspendedState": NotRequired[SuspendedStateTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
ScalableTargetTypeDef = TypedDict(
    "ScalableTargetTypeDef",
    {
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "MinCapacity": int,
        "MaxCapacity": int,
        "RoleARN": str,
        "CreationTime": datetime,
        "SuspendedState": NotRequired[SuspendedStateTypeDef],
        "ScalableTargetARN": NotRequired[str],
    },
)
StepScalingPolicyConfigurationOutputTypeDef = TypedDict(
    "StepScalingPolicyConfigurationOutputTypeDef",
    {
        "AdjustmentType": NotRequired[AdjustmentTypeType],
        "StepAdjustments": NotRequired[List[StepAdjustmentTypeDef]],
        "MinAdjustmentMagnitude": NotRequired[int],
        "Cooldown": NotRequired[int],
        "MetricAggregationType": NotRequired[MetricAggregationTypeType],
    },
)
StepScalingPolicyConfigurationTypeDef = TypedDict(
    "StepScalingPolicyConfigurationTypeDef",
    {
        "AdjustmentType": NotRequired[AdjustmentTypeType],
        "StepAdjustments": NotRequired[Sequence[StepAdjustmentTypeDef]],
        "MinAdjustmentMagnitude": NotRequired[int],
        "Cooldown": NotRequired[int],
        "MetricAggregationType": NotRequired[MetricAggregationTypeType],
    },
)
TargetTrackingMetricOutputTypeDef = TypedDict(
    "TargetTrackingMetricOutputTypeDef",
    {
        "Dimensions": NotRequired[List[TargetTrackingMetricDimensionTypeDef]],
        "MetricName": NotRequired[str],
        "Namespace": NotRequired[str],
    },
)
TargetTrackingMetricTypeDef = TypedDict(
    "TargetTrackingMetricTypeDef",
    {
        "Dimensions": NotRequired[Sequence[TargetTrackingMetricDimensionTypeDef]],
        "MetricName": NotRequired[str],
        "Namespace": NotRequired[str],
    },
)
DescribeScalingActivitiesResponseTypeDef = TypedDict(
    "DescribeScalingActivitiesResponseTypeDef",
    {
        "ScalingActivities": List[ScalingActivityTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeScheduledActionsResponseTypeDef = TypedDict(
    "DescribeScheduledActionsResponseTypeDef",
    {
        "ScheduledActions": List[ScheduledActionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeScalableTargetsResponseTypeDef = TypedDict(
    "DescribeScalableTargetsResponseTypeDef",
    {
        "ScalableTargets": List[ScalableTargetTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
TargetTrackingMetricStatOutputTypeDef = TypedDict(
    "TargetTrackingMetricStatOutputTypeDef",
    {
        "Metric": TargetTrackingMetricOutputTypeDef,
        "Stat": str,
        "Unit": NotRequired[str],
    },
)
TargetTrackingMetricUnionTypeDef = Union[
    TargetTrackingMetricTypeDef, TargetTrackingMetricOutputTypeDef
]
TargetTrackingMetricDataQueryOutputTypeDef = TypedDict(
    "TargetTrackingMetricDataQueryOutputTypeDef",
    {
        "Id": str,
        "Expression": NotRequired[str],
        "Label": NotRequired[str],
        "MetricStat": NotRequired[TargetTrackingMetricStatOutputTypeDef],
        "ReturnData": NotRequired[bool],
    },
)
TargetTrackingMetricStatTypeDef = TypedDict(
    "TargetTrackingMetricStatTypeDef",
    {
        "Metric": TargetTrackingMetricUnionTypeDef,
        "Stat": str,
        "Unit": NotRequired[str],
    },
)
CustomizedMetricSpecificationOutputTypeDef = TypedDict(
    "CustomizedMetricSpecificationOutputTypeDef",
    {
        "MetricName": NotRequired[str],
        "Namespace": NotRequired[str],
        "Dimensions": NotRequired[List[MetricDimensionTypeDef]],
        "Statistic": NotRequired[MetricStatisticType],
        "Unit": NotRequired[str],
        "Metrics": NotRequired[List[TargetTrackingMetricDataQueryOutputTypeDef]],
    },
)
TargetTrackingMetricStatUnionTypeDef = Union[
    TargetTrackingMetricStatTypeDef, TargetTrackingMetricStatOutputTypeDef
]
TargetTrackingScalingPolicyConfigurationOutputTypeDef = TypedDict(
    "TargetTrackingScalingPolicyConfigurationOutputTypeDef",
    {
        "TargetValue": float,
        "PredefinedMetricSpecification": NotRequired[PredefinedMetricSpecificationTypeDef],
        "CustomizedMetricSpecification": NotRequired[CustomizedMetricSpecificationOutputTypeDef],
        "ScaleOutCooldown": NotRequired[int],
        "ScaleInCooldown": NotRequired[int],
        "DisableScaleIn": NotRequired[bool],
    },
)
TargetTrackingMetricDataQueryTypeDef = TypedDict(
    "TargetTrackingMetricDataQueryTypeDef",
    {
        "Id": str,
        "Expression": NotRequired[str],
        "Label": NotRequired[str],
        "MetricStat": NotRequired[TargetTrackingMetricStatUnionTypeDef],
        "ReturnData": NotRequired[bool],
    },
)
ScalingPolicyTypeDef = TypedDict(
    "ScalingPolicyTypeDef",
    {
        "PolicyARN": str,
        "PolicyName": str,
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "PolicyType": PolicyTypeType,
        "CreationTime": datetime,
        "StepScalingPolicyConfiguration": NotRequired[StepScalingPolicyConfigurationOutputTypeDef],
        "TargetTrackingScalingPolicyConfiguration": NotRequired[
            TargetTrackingScalingPolicyConfigurationOutputTypeDef
        ],
        "Alarms": NotRequired[List[AlarmTypeDef]],
    },
)
TargetTrackingMetricDataQueryUnionTypeDef = Union[
    TargetTrackingMetricDataQueryTypeDef, TargetTrackingMetricDataQueryOutputTypeDef
]
DescribeScalingPoliciesResponseTypeDef = TypedDict(
    "DescribeScalingPoliciesResponseTypeDef",
    {
        "ScalingPolicies": List[ScalingPolicyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CustomizedMetricSpecificationTypeDef = TypedDict(
    "CustomizedMetricSpecificationTypeDef",
    {
        "MetricName": NotRequired[str],
        "Namespace": NotRequired[str],
        "Dimensions": NotRequired[Sequence[MetricDimensionTypeDef]],
        "Statistic": NotRequired[MetricStatisticType],
        "Unit": NotRequired[str],
        "Metrics": NotRequired[Sequence[TargetTrackingMetricDataQueryUnionTypeDef]],
    },
)
CustomizedMetricSpecificationUnionTypeDef = Union[
    CustomizedMetricSpecificationTypeDef, CustomizedMetricSpecificationOutputTypeDef
]
TargetTrackingScalingPolicyConfigurationTypeDef = TypedDict(
    "TargetTrackingScalingPolicyConfigurationTypeDef",
    {
        "TargetValue": float,
        "PredefinedMetricSpecification": NotRequired[PredefinedMetricSpecificationTypeDef],
        "CustomizedMetricSpecification": NotRequired[CustomizedMetricSpecificationUnionTypeDef],
        "ScaleOutCooldown": NotRequired[int],
        "ScaleInCooldown": NotRequired[int],
        "DisableScaleIn": NotRequired[bool],
    },
)
PutScalingPolicyRequestRequestTypeDef = TypedDict(
    "PutScalingPolicyRequestRequestTypeDef",
    {
        "PolicyName": str,
        "ServiceNamespace": ServiceNamespaceType,
        "ResourceId": str,
        "ScalableDimension": ScalableDimensionType,
        "PolicyType": NotRequired[PolicyTypeType],
        "StepScalingPolicyConfiguration": NotRequired[StepScalingPolicyConfigurationTypeDef],
        "TargetTrackingScalingPolicyConfiguration": NotRequired[
            TargetTrackingScalingPolicyConfigurationTypeDef
        ],
    },
)
