"""
Type annotations for autoscaling service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/type_defs/)

Usage::

    ```python
    from mypy_boto3_autoscaling.type_defs import AcceleratorCountRequestTypeDef

    data: AcceleratorCountRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    AcceleratorManufacturerType,
    AcceleratorNameType,
    AcceleratorTypeType,
    BareMetalType,
    BurstablePerformanceType,
    CpuManufacturerType,
    InstanceGenerationType,
    InstanceMetadataEndpointStateType,
    InstanceMetadataHttpTokensStateType,
    InstanceRefreshStatusType,
    LifecycleStateType,
    LocalStorageType,
    LocalStorageTypeType,
    MetricStatisticType,
    MetricTypeType,
    PredefinedLoadMetricTypeType,
    PredefinedMetricPairTypeType,
    PredefinedScalingMetricTypeType,
    PredictiveScalingMaxCapacityBreachBehaviorType,
    PredictiveScalingModeType,
    ScaleInProtectedInstancesType,
    ScalingActivityStatusCodeType,
    StandbyInstancesType,
    WarmPoolStateType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AcceleratorCountRequestTypeDef",
    "AcceleratorTotalMemoryMiBRequestTypeDef",
    "ActivityTypeDef",
    "ResponseMetadataTypeDef",
    "AdjustmentTypeTypeDef",
    "AlarmSpecificationOutputTypeDef",
    "AlarmSpecificationTypeDef",
    "AlarmTypeDef",
    "AttachInstancesQueryRequestTypeDef",
    "AttachLoadBalancerTargetGroupsTypeRequestTypeDef",
    "AttachLoadBalancersTypeRequestTypeDef",
    "TrafficSourceIdentifierTypeDef",
    "FilterTypeDef",
    "PaginatorConfigTypeDef",
    "EnabledMetricTypeDef",
    "InstanceMaintenancePolicyTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "SuspendedProcessTypeDef",
    "TagDescriptionTypeDef",
    "BaselineEbsBandwidthMbpsRequestTypeDef",
    "FailedScheduledUpdateGroupActionRequestTypeDef",
    "BatchDeleteScheduledActionTypeRequestTypeDef",
    "EbsTypeDef",
    "CancelInstanceRefreshTypeRequestTypeDef",
    "CapacityForecastTypeDef",
    "CompleteLifecycleActionTypeRequestTypeDef",
    "LifecycleHookSpecificationTypeDef",
    "TagTypeDef",
    "InstanceMetadataOptionsTypeDef",
    "InstanceMonitoringTypeDef",
    "MetricDimensionTypeDef",
    "DeleteAutoScalingGroupTypeRequestTypeDef",
    "DeleteLifecycleHookTypeRequestTypeDef",
    "DeleteNotificationConfigurationTypeRequestTypeDef",
    "DeletePolicyTypeRequestTypeDef",
    "DeleteScheduledActionTypeRequestTypeDef",
    "DeleteWarmPoolTypeRequestTypeDef",
    "DescribeAutoScalingInstancesTypeRequestTypeDef",
    "DescribeInstanceRefreshesTypeRequestTypeDef",
    "LifecycleHookTypeDef",
    "DescribeLifecycleHooksTypeRequestTypeDef",
    "DescribeLoadBalancerTargetGroupsRequestRequestTypeDef",
    "LoadBalancerTargetGroupStateTypeDef",
    "DescribeLoadBalancersRequestRequestTypeDef",
    "LoadBalancerStateTypeDef",
    "MetricCollectionTypeTypeDef",
    "MetricGranularityTypeTypeDef",
    "NotificationConfigurationTypeDef",
    "DescribeNotificationConfigurationsTypeRequestTypeDef",
    "DescribePoliciesTypeRequestTypeDef",
    "DescribeScalingActivitiesTypeRequestTypeDef",
    "TimestampTypeDef",
    "DescribeTrafficSourcesRequestRequestTypeDef",
    "TrafficSourceStateTypeDef",
    "DescribeWarmPoolTypeRequestTypeDef",
    "DetachInstancesQueryRequestTypeDef",
    "DetachLoadBalancerTargetGroupsTypeRequestTypeDef",
    "DetachLoadBalancersTypeRequestTypeDef",
    "DisableMetricsCollectionQueryRequestTypeDef",
    "EnableMetricsCollectionQueryRequestTypeDef",
    "EnterStandbyQueryRequestTypeDef",
    "ExecutePolicyTypeRequestTypeDef",
    "ExitStandbyQueryRequestTypeDef",
    "InstanceRefreshLivePoolProgressTypeDef",
    "InstanceRefreshWarmPoolProgressTypeDef",
    "MemoryGiBPerVCpuRequestTypeDef",
    "MemoryMiBRequestTypeDef",
    "NetworkBandwidthGbpsRequestTypeDef",
    "NetworkInterfaceCountRequestTypeDef",
    "TotalLocalStorageGBRequestTypeDef",
    "VCpuCountRequestTypeDef",
    "InstanceReusePolicyTypeDef",
    "InstancesDistributionTypeDef",
    "LaunchConfigurationNameTypeRequestTypeDef",
    "LaunchConfigurationNamesTypeRequestTypeDef",
    "PredefinedMetricSpecificationTypeDef",
    "PredictiveScalingPredefinedLoadMetricTypeDef",
    "PredictiveScalingPredefinedMetricPairTypeDef",
    "PredictiveScalingPredefinedScalingMetricTypeDef",
    "ProcessTypeTypeDef",
    "PutLifecycleHookTypeRequestTypeDef",
    "PutNotificationConfigurationTypeRequestTypeDef",
    "StepAdjustmentTypeDef",
    "RecordLifecycleActionHeartbeatTypeRequestTypeDef",
    "RollbackInstanceRefreshTypeRequestTypeDef",
    "ScalingProcessQueryRequestTypeDef",
    "ScheduledUpdateGroupActionTypeDef",
    "SetDesiredCapacityTypeRequestTypeDef",
    "SetInstanceHealthQueryRequestTypeDef",
    "SetInstanceProtectionQueryRequestTypeDef",
    "TerminateInstanceInAutoScalingGroupTypeRequestTypeDef",
    "ActivitiesTypeTypeDef",
    "ActivityTypeTypeDef",
    "CancelInstanceRefreshAnswerTypeDef",
    "DescribeAccountLimitsAnswerTypeDef",
    "DescribeAutoScalingNotificationTypesAnswerTypeDef",
    "DescribeLifecycleHookTypesAnswerTypeDef",
    "DescribeTerminationPolicyTypesAnswerTypeDef",
    "DetachInstancesAnswerTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EnterStandbyAnswerTypeDef",
    "ExitStandbyAnswerTypeDef",
    "RollbackInstanceRefreshAnswerTypeDef",
    "StartInstanceRefreshAnswerTypeDef",
    "DescribeAdjustmentTypesAnswerTypeDef",
    "RefreshPreferencesOutputTypeDef",
    "AlarmSpecificationUnionTypeDef",
    "PolicyARNTypeTypeDef",
    "AttachTrafficSourcesTypeRequestTypeDef",
    "DetachTrafficSourcesTypeRequestTypeDef",
    "AutoScalingGroupNamesTypeRequestTypeDef",
    "DescribeTagsTypeRequestTypeDef",
    "AutoScalingGroupNamesTypeDescribeAutoScalingGroupsPaginateTypeDef",
    "DescribeAutoScalingInstancesTypeDescribeAutoScalingInstancesPaginateTypeDef",
    "DescribeLoadBalancerTargetGroupsRequestDescribeLoadBalancerTargetGroupsPaginateTypeDef",
    "DescribeLoadBalancersRequestDescribeLoadBalancersPaginateTypeDef",
    "DescribeNotificationConfigurationsTypeDescribeNotificationConfigurationsPaginateTypeDef",
    "DescribePoliciesTypeDescribePoliciesPaginateTypeDef",
    "DescribeScalingActivitiesTypeDescribeScalingActivitiesPaginateTypeDef",
    "DescribeTagsTypeDescribeTagsPaginateTypeDef",
    "DescribeWarmPoolTypeDescribeWarmPoolPaginateTypeDef",
    "LaunchConfigurationNamesTypeDescribeLaunchConfigurationsPaginateTypeDef",
    "AutoScalingInstanceDetailsTypeDef",
    "InstanceTypeDef",
    "TagsTypeTypeDef",
    "BatchDeleteScheduledActionAnswerTypeDef",
    "BatchPutScheduledUpdateGroupActionAnswerTypeDef",
    "BlockDeviceMappingTypeDef",
    "CreateOrUpdateTagsTypeRequestTypeDef",
    "DeleteTagsTypeRequestTypeDef",
    "MetricOutputTypeDef",
    "MetricTypeDef",
    "DescribeLifecycleHooksAnswerTypeDef",
    "DescribeLoadBalancerTargetGroupsResponseTypeDef",
    "DescribeLoadBalancersResponseTypeDef",
    "DescribeMetricCollectionTypesAnswerTypeDef",
    "DescribeNotificationConfigurationsAnswerTypeDef",
    "DescribeScheduledActionsTypeDescribeScheduledActionsPaginateTypeDef",
    "DescribeScheduledActionsTypeRequestTypeDef",
    "GetPredictiveScalingForecastTypeRequestTypeDef",
    "PutScheduledUpdateGroupActionTypeRequestTypeDef",
    "ScheduledUpdateGroupActionRequestTypeDef",
    "DescribeTrafficSourcesResponseTypeDef",
    "InstanceRefreshProgressDetailsTypeDef",
    "InstanceRequirementsOutputTypeDef",
    "InstanceRequirementsTypeDef",
    "PutWarmPoolTypeRequestTypeDef",
    "WarmPoolConfigurationTypeDef",
    "ProcessesTypeTypeDef",
    "ScheduledActionsTypeTypeDef",
    "RefreshPreferencesTypeDef",
    "AutoScalingInstancesTypeTypeDef",
    "CreateLaunchConfigurationTypeRequestTypeDef",
    "LaunchConfigurationTypeDef",
    "MetricStatOutputTypeDef",
    "TargetTrackingMetricStatOutputTypeDef",
    "MetricUnionTypeDef",
    "BatchPutScheduledUpdateGroupActionTypeRequestTypeDef",
    "RollbackDetailsTypeDef",
    "LaunchTemplateOverridesOutputTypeDef",
    "InstanceRequirementsUnionTypeDef",
    "DescribeWarmPoolAnswerTypeDef",
    "LaunchConfigurationsTypeTypeDef",
    "MetricDataQueryOutputTypeDef",
    "TargetTrackingMetricDataQueryOutputTypeDef",
    "MetricStatTypeDef",
    "TargetTrackingMetricStatTypeDef",
    "LaunchTemplateOutputTypeDef",
    "LaunchTemplateOverridesTypeDef",
    "PredictiveScalingCustomizedCapacityMetricOutputTypeDef",
    "PredictiveScalingCustomizedLoadMetricOutputTypeDef",
    "PredictiveScalingCustomizedScalingMetricOutputTypeDef",
    "CustomizedMetricSpecificationOutputTypeDef",
    "MetricStatUnionTypeDef",
    "TargetTrackingMetricStatUnionTypeDef",
    "MixedInstancesPolicyOutputTypeDef",
    "LaunchTemplateOverridesUnionTypeDef",
    "PredictiveScalingMetricSpecificationOutputTypeDef",
    "TargetTrackingConfigurationOutputTypeDef",
    "MetricDataQueryTypeDef",
    "TargetTrackingMetricDataQueryTypeDef",
    "AutoScalingGroupTypeDef",
    "DesiredConfigurationOutputTypeDef",
    "LaunchTemplateTypeDef",
    "LoadForecastTypeDef",
    "PredictiveScalingConfigurationOutputTypeDef",
    "MetricDataQueryUnionTypeDef",
    "PredictiveScalingCustomizedCapacityMetricTypeDef",
    "PredictiveScalingCustomizedLoadMetricTypeDef",
    "TargetTrackingMetricDataQueryUnionTypeDef",
    "AutoScalingGroupsTypeTypeDef",
    "InstanceRefreshTypeDef",
    "LaunchTemplateUnionTypeDef",
    "GetPredictiveScalingForecastAnswerTypeDef",
    "ScalingPolicyTypeDef",
    "PredictiveScalingCustomizedScalingMetricTypeDef",
    "PredictiveScalingCustomizedCapacityMetricUnionTypeDef",
    "PredictiveScalingCustomizedLoadMetricUnionTypeDef",
    "CustomizedMetricSpecificationTypeDef",
    "DescribeInstanceRefreshesAnswerTypeDef",
    "MixedInstancesPolicyTypeDef",
    "PoliciesTypeTypeDef",
    "PredictiveScalingCustomizedScalingMetricUnionTypeDef",
    "CustomizedMetricSpecificationUnionTypeDef",
    "CreateAutoScalingGroupTypeRequestTypeDef",
    "MixedInstancesPolicyUnionTypeDef",
    "UpdateAutoScalingGroupTypeRequestTypeDef",
    "PredictiveScalingMetricSpecificationTypeDef",
    "TargetTrackingConfigurationTypeDef",
    "DesiredConfigurationTypeDef",
    "PredictiveScalingMetricSpecificationUnionTypeDef",
    "StartInstanceRefreshTypeRequestTypeDef",
    "PredictiveScalingConfigurationTypeDef",
    "PutScalingPolicyTypeRequestTypeDef",
)

AcceleratorCountRequestTypeDef = TypedDict(
    "AcceleratorCountRequestTypeDef",
    {
        "Min": NotRequired[int],
        "Max": NotRequired[int],
    },
)
AcceleratorTotalMemoryMiBRequestTypeDef = TypedDict(
    "AcceleratorTotalMemoryMiBRequestTypeDef",
    {
        "Min": NotRequired[int],
        "Max": NotRequired[int],
    },
)
ActivityTypeDef = TypedDict(
    "ActivityTypeDef",
    {
        "ActivityId": str,
        "AutoScalingGroupName": str,
        "Cause": str,
        "StartTime": datetime,
        "StatusCode": ScalingActivityStatusCodeType,
        "Description": NotRequired[str],
        "EndTime": NotRequired[datetime],
        "StatusMessage": NotRequired[str],
        "Progress": NotRequired[int],
        "Details": NotRequired[str],
        "AutoScalingGroupState": NotRequired[str],
        "AutoScalingGroupARN": NotRequired[str],
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
AdjustmentTypeTypeDef = TypedDict(
    "AdjustmentTypeTypeDef",
    {
        "AdjustmentType": NotRequired[str],
    },
)
AlarmSpecificationOutputTypeDef = TypedDict(
    "AlarmSpecificationOutputTypeDef",
    {
        "Alarms": NotRequired[List[str]],
    },
)
AlarmSpecificationTypeDef = TypedDict(
    "AlarmSpecificationTypeDef",
    {
        "Alarms": NotRequired[Sequence[str]],
    },
)
AlarmTypeDef = TypedDict(
    "AlarmTypeDef",
    {
        "AlarmName": NotRequired[str],
        "AlarmARN": NotRequired[str],
    },
)
AttachInstancesQueryRequestTypeDef = TypedDict(
    "AttachInstancesQueryRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "InstanceIds": NotRequired[Sequence[str]],
    },
)
AttachLoadBalancerTargetGroupsTypeRequestTypeDef = TypedDict(
    "AttachLoadBalancerTargetGroupsTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "TargetGroupARNs": Sequence[str],
    },
)
AttachLoadBalancersTypeRequestTypeDef = TypedDict(
    "AttachLoadBalancersTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "LoadBalancerNames": Sequence[str],
    },
)
TrafficSourceIdentifierTypeDef = TypedDict(
    "TrafficSourceIdentifierTypeDef",
    {
        "Identifier": str,
        "Type": NotRequired[str],
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
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
EnabledMetricTypeDef = TypedDict(
    "EnabledMetricTypeDef",
    {
        "Metric": NotRequired[str],
        "Granularity": NotRequired[str],
    },
)
InstanceMaintenancePolicyTypeDef = TypedDict(
    "InstanceMaintenancePolicyTypeDef",
    {
        "MinHealthyPercentage": NotRequired[int],
        "MaxHealthyPercentage": NotRequired[int],
    },
)
LaunchTemplateSpecificationTypeDef = TypedDict(
    "LaunchTemplateSpecificationTypeDef",
    {
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
        "Version": NotRequired[str],
    },
)
SuspendedProcessTypeDef = TypedDict(
    "SuspendedProcessTypeDef",
    {
        "ProcessName": NotRequired[str],
        "SuspensionReason": NotRequired[str],
    },
)
TagDescriptionTypeDef = TypedDict(
    "TagDescriptionTypeDef",
    {
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[str],
        "Key": NotRequired[str],
        "Value": NotRequired[str],
        "PropagateAtLaunch": NotRequired[bool],
    },
)
BaselineEbsBandwidthMbpsRequestTypeDef = TypedDict(
    "BaselineEbsBandwidthMbpsRequestTypeDef",
    {
        "Min": NotRequired[int],
        "Max": NotRequired[int],
    },
)
FailedScheduledUpdateGroupActionRequestTypeDef = TypedDict(
    "FailedScheduledUpdateGroupActionRequestTypeDef",
    {
        "ScheduledActionName": str,
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)
BatchDeleteScheduledActionTypeRequestTypeDef = TypedDict(
    "BatchDeleteScheduledActionTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "ScheduledActionNames": Sequence[str],
    },
)
EbsTypeDef = TypedDict(
    "EbsTypeDef",
    {
        "SnapshotId": NotRequired[str],
        "VolumeSize": NotRequired[int],
        "VolumeType": NotRequired[str],
        "DeleteOnTermination": NotRequired[bool],
        "Iops": NotRequired[int],
        "Encrypted": NotRequired[bool],
        "Throughput": NotRequired[int],
    },
)
CancelInstanceRefreshTypeRequestTypeDef = TypedDict(
    "CancelInstanceRefreshTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
    },
)
CapacityForecastTypeDef = TypedDict(
    "CapacityForecastTypeDef",
    {
        "Timestamps": List[datetime],
        "Values": List[float],
    },
)
CompleteLifecycleActionTypeRequestTypeDef = TypedDict(
    "CompleteLifecycleActionTypeRequestTypeDef",
    {
        "LifecycleHookName": str,
        "AutoScalingGroupName": str,
        "LifecycleActionResult": str,
        "LifecycleActionToken": NotRequired[str],
        "InstanceId": NotRequired[str],
    },
)
LifecycleHookSpecificationTypeDef = TypedDict(
    "LifecycleHookSpecificationTypeDef",
    {
        "LifecycleHookName": str,
        "LifecycleTransition": str,
        "NotificationMetadata": NotRequired[str],
        "HeartbeatTimeout": NotRequired[int],
        "DefaultResult": NotRequired[str],
        "NotificationTargetARN": NotRequired[str],
        "RoleARN": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "ResourceId": NotRequired[str],
        "ResourceType": NotRequired[str],
        "Value": NotRequired[str],
        "PropagateAtLaunch": NotRequired[bool],
    },
)
InstanceMetadataOptionsTypeDef = TypedDict(
    "InstanceMetadataOptionsTypeDef",
    {
        "HttpTokens": NotRequired[InstanceMetadataHttpTokensStateType],
        "HttpPutResponseHopLimit": NotRequired[int],
        "HttpEndpoint": NotRequired[InstanceMetadataEndpointStateType],
    },
)
InstanceMonitoringTypeDef = TypedDict(
    "InstanceMonitoringTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
MetricDimensionTypeDef = TypedDict(
    "MetricDimensionTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)
DeleteAutoScalingGroupTypeRequestTypeDef = TypedDict(
    "DeleteAutoScalingGroupTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "ForceDelete": NotRequired[bool],
    },
)
DeleteLifecycleHookTypeRequestTypeDef = TypedDict(
    "DeleteLifecycleHookTypeRequestTypeDef",
    {
        "LifecycleHookName": str,
        "AutoScalingGroupName": str,
    },
)
DeleteNotificationConfigurationTypeRequestTypeDef = TypedDict(
    "DeleteNotificationConfigurationTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "TopicARN": str,
    },
)
DeletePolicyTypeRequestTypeDef = TypedDict(
    "DeletePolicyTypeRequestTypeDef",
    {
        "PolicyName": str,
        "AutoScalingGroupName": NotRequired[str],
    },
)
DeleteScheduledActionTypeRequestTypeDef = TypedDict(
    "DeleteScheduledActionTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "ScheduledActionName": str,
    },
)
DeleteWarmPoolTypeRequestTypeDef = TypedDict(
    "DeleteWarmPoolTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "ForceDelete": NotRequired[bool],
    },
)
DescribeAutoScalingInstancesTypeRequestTypeDef = TypedDict(
    "DescribeAutoScalingInstancesTypeRequestTypeDef",
    {
        "InstanceIds": NotRequired[Sequence[str]],
        "MaxRecords": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeInstanceRefreshesTypeRequestTypeDef = TypedDict(
    "DescribeInstanceRefreshesTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "InstanceRefreshIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)
LifecycleHookTypeDef = TypedDict(
    "LifecycleHookTypeDef",
    {
        "LifecycleHookName": NotRequired[str],
        "AutoScalingGroupName": NotRequired[str],
        "LifecycleTransition": NotRequired[str],
        "NotificationTargetARN": NotRequired[str],
        "RoleARN": NotRequired[str],
        "NotificationMetadata": NotRequired[str],
        "HeartbeatTimeout": NotRequired[int],
        "GlobalTimeout": NotRequired[int],
        "DefaultResult": NotRequired[str],
    },
)
DescribeLifecycleHooksTypeRequestTypeDef = TypedDict(
    "DescribeLifecycleHooksTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "LifecycleHookNames": NotRequired[Sequence[str]],
    },
)
DescribeLoadBalancerTargetGroupsRequestRequestTypeDef = TypedDict(
    "DescribeLoadBalancerTargetGroupsRequestRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "NextToken": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)
LoadBalancerTargetGroupStateTypeDef = TypedDict(
    "LoadBalancerTargetGroupStateTypeDef",
    {
        "LoadBalancerTargetGroupARN": NotRequired[str],
        "State": NotRequired[str],
    },
)
DescribeLoadBalancersRequestRequestTypeDef = TypedDict(
    "DescribeLoadBalancersRequestRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "NextToken": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)
LoadBalancerStateTypeDef = TypedDict(
    "LoadBalancerStateTypeDef",
    {
        "LoadBalancerName": NotRequired[str],
        "State": NotRequired[str],
    },
)
MetricCollectionTypeTypeDef = TypedDict(
    "MetricCollectionTypeTypeDef",
    {
        "Metric": NotRequired[str],
    },
)
MetricGranularityTypeTypeDef = TypedDict(
    "MetricGranularityTypeTypeDef",
    {
        "Granularity": NotRequired[str],
    },
)
NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef",
    {
        "AutoScalingGroupName": NotRequired[str],
        "TopicARN": NotRequired[str],
        "NotificationType": NotRequired[str],
    },
)
DescribeNotificationConfigurationsTypeRequestTypeDef = TypedDict(
    "DescribeNotificationConfigurationsTypeRequestTypeDef",
    {
        "AutoScalingGroupNames": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)
DescribePoliciesTypeRequestTypeDef = TypedDict(
    "DescribePoliciesTypeRequestTypeDef",
    {
        "AutoScalingGroupName": NotRequired[str],
        "PolicyNames": NotRequired[Sequence[str]],
        "PolicyTypes": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)
DescribeScalingActivitiesTypeRequestTypeDef = TypedDict(
    "DescribeScalingActivitiesTypeRequestTypeDef",
    {
        "ActivityIds": NotRequired[Sequence[str]],
        "AutoScalingGroupName": NotRequired[str],
        "IncludeDeletedGroups": NotRequired[bool],
        "MaxRecords": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
DescribeTrafficSourcesRequestRequestTypeDef = TypedDict(
    "DescribeTrafficSourcesRequestRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "TrafficSourceType": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)
TrafficSourceStateTypeDef = TypedDict(
    "TrafficSourceStateTypeDef",
    {
        "TrafficSource": NotRequired[str],
        "State": NotRequired[str],
        "Identifier": NotRequired[str],
        "Type": NotRequired[str],
    },
)
DescribeWarmPoolTypeRequestTypeDef = TypedDict(
    "DescribeWarmPoolTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "MaxRecords": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DetachInstancesQueryRequestTypeDef = TypedDict(
    "DetachInstancesQueryRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "ShouldDecrementDesiredCapacity": bool,
        "InstanceIds": NotRequired[Sequence[str]],
    },
)
DetachLoadBalancerTargetGroupsTypeRequestTypeDef = TypedDict(
    "DetachLoadBalancerTargetGroupsTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "TargetGroupARNs": Sequence[str],
    },
)
DetachLoadBalancersTypeRequestTypeDef = TypedDict(
    "DetachLoadBalancersTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "LoadBalancerNames": Sequence[str],
    },
)
DisableMetricsCollectionQueryRequestTypeDef = TypedDict(
    "DisableMetricsCollectionQueryRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "Metrics": NotRequired[Sequence[str]],
    },
)
EnableMetricsCollectionQueryRequestTypeDef = TypedDict(
    "EnableMetricsCollectionQueryRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "Granularity": str,
        "Metrics": NotRequired[Sequence[str]],
    },
)
EnterStandbyQueryRequestTypeDef = TypedDict(
    "EnterStandbyQueryRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "ShouldDecrementDesiredCapacity": bool,
        "InstanceIds": NotRequired[Sequence[str]],
    },
)
ExecutePolicyTypeRequestTypeDef = TypedDict(
    "ExecutePolicyTypeRequestTypeDef",
    {
        "PolicyName": str,
        "AutoScalingGroupName": NotRequired[str],
        "HonorCooldown": NotRequired[bool],
        "MetricValue": NotRequired[float],
        "BreachThreshold": NotRequired[float],
    },
)
ExitStandbyQueryRequestTypeDef = TypedDict(
    "ExitStandbyQueryRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "InstanceIds": NotRequired[Sequence[str]],
    },
)
InstanceRefreshLivePoolProgressTypeDef = TypedDict(
    "InstanceRefreshLivePoolProgressTypeDef",
    {
        "PercentageComplete": NotRequired[int],
        "InstancesToUpdate": NotRequired[int],
    },
)
InstanceRefreshWarmPoolProgressTypeDef = TypedDict(
    "InstanceRefreshWarmPoolProgressTypeDef",
    {
        "PercentageComplete": NotRequired[int],
        "InstancesToUpdate": NotRequired[int],
    },
)
MemoryGiBPerVCpuRequestTypeDef = TypedDict(
    "MemoryGiBPerVCpuRequestTypeDef",
    {
        "Min": NotRequired[float],
        "Max": NotRequired[float],
    },
)
MemoryMiBRequestTypeDef = TypedDict(
    "MemoryMiBRequestTypeDef",
    {
        "Min": int,
        "Max": NotRequired[int],
    },
)
NetworkBandwidthGbpsRequestTypeDef = TypedDict(
    "NetworkBandwidthGbpsRequestTypeDef",
    {
        "Min": NotRequired[float],
        "Max": NotRequired[float],
    },
)
NetworkInterfaceCountRequestTypeDef = TypedDict(
    "NetworkInterfaceCountRequestTypeDef",
    {
        "Min": NotRequired[int],
        "Max": NotRequired[int],
    },
)
TotalLocalStorageGBRequestTypeDef = TypedDict(
    "TotalLocalStorageGBRequestTypeDef",
    {
        "Min": NotRequired[float],
        "Max": NotRequired[float],
    },
)
VCpuCountRequestTypeDef = TypedDict(
    "VCpuCountRequestTypeDef",
    {
        "Min": int,
        "Max": NotRequired[int],
    },
)
InstanceReusePolicyTypeDef = TypedDict(
    "InstanceReusePolicyTypeDef",
    {
        "ReuseOnScaleIn": NotRequired[bool],
    },
)
InstancesDistributionTypeDef = TypedDict(
    "InstancesDistributionTypeDef",
    {
        "OnDemandAllocationStrategy": NotRequired[str],
        "OnDemandBaseCapacity": NotRequired[int],
        "OnDemandPercentageAboveBaseCapacity": NotRequired[int],
        "SpotAllocationStrategy": NotRequired[str],
        "SpotInstancePools": NotRequired[int],
        "SpotMaxPrice": NotRequired[str],
    },
)
LaunchConfigurationNameTypeRequestTypeDef = TypedDict(
    "LaunchConfigurationNameTypeRequestTypeDef",
    {
        "LaunchConfigurationName": str,
    },
)
LaunchConfigurationNamesTypeRequestTypeDef = TypedDict(
    "LaunchConfigurationNamesTypeRequestTypeDef",
    {
        "LaunchConfigurationNames": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)
PredefinedMetricSpecificationTypeDef = TypedDict(
    "PredefinedMetricSpecificationTypeDef",
    {
        "PredefinedMetricType": MetricTypeType,
        "ResourceLabel": NotRequired[str],
    },
)
PredictiveScalingPredefinedLoadMetricTypeDef = TypedDict(
    "PredictiveScalingPredefinedLoadMetricTypeDef",
    {
        "PredefinedMetricType": PredefinedLoadMetricTypeType,
        "ResourceLabel": NotRequired[str],
    },
)
PredictiveScalingPredefinedMetricPairTypeDef = TypedDict(
    "PredictiveScalingPredefinedMetricPairTypeDef",
    {
        "PredefinedMetricType": PredefinedMetricPairTypeType,
        "ResourceLabel": NotRequired[str],
    },
)
PredictiveScalingPredefinedScalingMetricTypeDef = TypedDict(
    "PredictiveScalingPredefinedScalingMetricTypeDef",
    {
        "PredefinedMetricType": PredefinedScalingMetricTypeType,
        "ResourceLabel": NotRequired[str],
    },
)
ProcessTypeTypeDef = TypedDict(
    "ProcessTypeTypeDef",
    {
        "ProcessName": str,
    },
)
PutLifecycleHookTypeRequestTypeDef = TypedDict(
    "PutLifecycleHookTypeRequestTypeDef",
    {
        "LifecycleHookName": str,
        "AutoScalingGroupName": str,
        "LifecycleTransition": NotRequired[str],
        "RoleARN": NotRequired[str],
        "NotificationTargetARN": NotRequired[str],
        "NotificationMetadata": NotRequired[str],
        "HeartbeatTimeout": NotRequired[int],
        "DefaultResult": NotRequired[str],
    },
)
PutNotificationConfigurationTypeRequestTypeDef = TypedDict(
    "PutNotificationConfigurationTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "TopicARN": str,
        "NotificationTypes": Sequence[str],
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
RecordLifecycleActionHeartbeatTypeRequestTypeDef = TypedDict(
    "RecordLifecycleActionHeartbeatTypeRequestTypeDef",
    {
        "LifecycleHookName": str,
        "AutoScalingGroupName": str,
        "LifecycleActionToken": NotRequired[str],
        "InstanceId": NotRequired[str],
    },
)
RollbackInstanceRefreshTypeRequestTypeDef = TypedDict(
    "RollbackInstanceRefreshTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
    },
)
ScalingProcessQueryRequestTypeDef = TypedDict(
    "ScalingProcessQueryRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "ScalingProcesses": NotRequired[Sequence[str]],
    },
)
ScheduledUpdateGroupActionTypeDef = TypedDict(
    "ScheduledUpdateGroupActionTypeDef",
    {
        "AutoScalingGroupName": NotRequired[str],
        "ScheduledActionName": NotRequired[str],
        "ScheduledActionARN": NotRequired[str],
        "Time": NotRequired[datetime],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "Recurrence": NotRequired[str],
        "MinSize": NotRequired[int],
        "MaxSize": NotRequired[int],
        "DesiredCapacity": NotRequired[int],
        "TimeZone": NotRequired[str],
    },
)
SetDesiredCapacityTypeRequestTypeDef = TypedDict(
    "SetDesiredCapacityTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "DesiredCapacity": int,
        "HonorCooldown": NotRequired[bool],
    },
)
SetInstanceHealthQueryRequestTypeDef = TypedDict(
    "SetInstanceHealthQueryRequestTypeDef",
    {
        "InstanceId": str,
        "HealthStatus": str,
        "ShouldRespectGracePeriod": NotRequired[bool],
    },
)
SetInstanceProtectionQueryRequestTypeDef = TypedDict(
    "SetInstanceProtectionQueryRequestTypeDef",
    {
        "InstanceIds": Sequence[str],
        "AutoScalingGroupName": str,
        "ProtectedFromScaleIn": bool,
    },
)
TerminateInstanceInAutoScalingGroupTypeRequestTypeDef = TypedDict(
    "TerminateInstanceInAutoScalingGroupTypeRequestTypeDef",
    {
        "InstanceId": str,
        "ShouldDecrementDesiredCapacity": bool,
    },
)
ActivitiesTypeTypeDef = TypedDict(
    "ActivitiesTypeTypeDef",
    {
        "Activities": List[ActivityTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ActivityTypeTypeDef = TypedDict(
    "ActivityTypeTypeDef",
    {
        "Activity": ActivityTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CancelInstanceRefreshAnswerTypeDef = TypedDict(
    "CancelInstanceRefreshAnswerTypeDef",
    {
        "InstanceRefreshId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAccountLimitsAnswerTypeDef = TypedDict(
    "DescribeAccountLimitsAnswerTypeDef",
    {
        "MaxNumberOfAutoScalingGroups": int,
        "MaxNumberOfLaunchConfigurations": int,
        "NumberOfAutoScalingGroups": int,
        "NumberOfLaunchConfigurations": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAutoScalingNotificationTypesAnswerTypeDef = TypedDict(
    "DescribeAutoScalingNotificationTypesAnswerTypeDef",
    {
        "AutoScalingNotificationTypes": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeLifecycleHookTypesAnswerTypeDef = TypedDict(
    "DescribeLifecycleHookTypesAnswerTypeDef",
    {
        "LifecycleHookTypes": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTerminationPolicyTypesAnswerTypeDef = TypedDict(
    "DescribeTerminationPolicyTypesAnswerTypeDef",
    {
        "TerminationPolicyTypes": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DetachInstancesAnswerTypeDef = TypedDict(
    "DetachInstancesAnswerTypeDef",
    {
        "Activities": List[ActivityTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnterStandbyAnswerTypeDef = TypedDict(
    "EnterStandbyAnswerTypeDef",
    {
        "Activities": List[ActivityTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExitStandbyAnswerTypeDef = TypedDict(
    "ExitStandbyAnswerTypeDef",
    {
        "Activities": List[ActivityTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RollbackInstanceRefreshAnswerTypeDef = TypedDict(
    "RollbackInstanceRefreshAnswerTypeDef",
    {
        "InstanceRefreshId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartInstanceRefreshAnswerTypeDef = TypedDict(
    "StartInstanceRefreshAnswerTypeDef",
    {
        "InstanceRefreshId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAdjustmentTypesAnswerTypeDef = TypedDict(
    "DescribeAdjustmentTypesAnswerTypeDef",
    {
        "AdjustmentTypes": List[AdjustmentTypeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RefreshPreferencesOutputTypeDef = TypedDict(
    "RefreshPreferencesOutputTypeDef",
    {
        "MinHealthyPercentage": NotRequired[int],
        "InstanceWarmup": NotRequired[int],
        "CheckpointPercentages": NotRequired[List[int]],
        "CheckpointDelay": NotRequired[int],
        "SkipMatching": NotRequired[bool],
        "AutoRollback": NotRequired[bool],
        "ScaleInProtectedInstances": NotRequired[ScaleInProtectedInstancesType],
        "StandbyInstances": NotRequired[StandbyInstancesType],
        "AlarmSpecification": NotRequired[AlarmSpecificationOutputTypeDef],
        "MaxHealthyPercentage": NotRequired[int],
    },
)
AlarmSpecificationUnionTypeDef = Union[AlarmSpecificationTypeDef, AlarmSpecificationOutputTypeDef]
PolicyARNTypeTypeDef = TypedDict(
    "PolicyARNTypeTypeDef",
    {
        "PolicyARN": str,
        "Alarms": List[AlarmTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AttachTrafficSourcesTypeRequestTypeDef = TypedDict(
    "AttachTrafficSourcesTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "TrafficSources": Sequence[TrafficSourceIdentifierTypeDef],
    },
)
DetachTrafficSourcesTypeRequestTypeDef = TypedDict(
    "DetachTrafficSourcesTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "TrafficSources": Sequence[TrafficSourceIdentifierTypeDef],
    },
)
AutoScalingGroupNamesTypeRequestTypeDef = TypedDict(
    "AutoScalingGroupNamesTypeRequestTypeDef",
    {
        "AutoScalingGroupNames": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
DescribeTagsTypeRequestTypeDef = TypedDict(
    "DescribeTagsTypeRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)
AutoScalingGroupNamesTypeDescribeAutoScalingGroupsPaginateTypeDef = TypedDict(
    "AutoScalingGroupNamesTypeDescribeAutoScalingGroupsPaginateTypeDef",
    {
        "AutoScalingGroupNames": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeAutoScalingInstancesTypeDescribeAutoScalingInstancesPaginateTypeDef = TypedDict(
    "DescribeAutoScalingInstancesTypeDescribeAutoScalingInstancesPaginateTypeDef",
    {
        "InstanceIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeLoadBalancerTargetGroupsRequestDescribeLoadBalancerTargetGroupsPaginateTypeDef = TypedDict(
    "DescribeLoadBalancerTargetGroupsRequestDescribeLoadBalancerTargetGroupsPaginateTypeDef",
    {
        "AutoScalingGroupName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeLoadBalancersRequestDescribeLoadBalancersPaginateTypeDef = TypedDict(
    "DescribeLoadBalancersRequestDescribeLoadBalancersPaginateTypeDef",
    {
        "AutoScalingGroupName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeNotificationConfigurationsTypeDescribeNotificationConfigurationsPaginateTypeDef = TypedDict(
    "DescribeNotificationConfigurationsTypeDescribeNotificationConfigurationsPaginateTypeDef",
    {
        "AutoScalingGroupNames": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribePoliciesTypeDescribePoliciesPaginateTypeDef = TypedDict(
    "DescribePoliciesTypeDescribePoliciesPaginateTypeDef",
    {
        "AutoScalingGroupName": NotRequired[str],
        "PolicyNames": NotRequired[Sequence[str]],
        "PolicyTypes": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeScalingActivitiesTypeDescribeScalingActivitiesPaginateTypeDef = TypedDict(
    "DescribeScalingActivitiesTypeDescribeScalingActivitiesPaginateTypeDef",
    {
        "ActivityIds": NotRequired[Sequence[str]],
        "AutoScalingGroupName": NotRequired[str],
        "IncludeDeletedGroups": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeTagsTypeDescribeTagsPaginateTypeDef = TypedDict(
    "DescribeTagsTypeDescribeTagsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeWarmPoolTypeDescribeWarmPoolPaginateTypeDef = TypedDict(
    "DescribeWarmPoolTypeDescribeWarmPoolPaginateTypeDef",
    {
        "AutoScalingGroupName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
LaunchConfigurationNamesTypeDescribeLaunchConfigurationsPaginateTypeDef = TypedDict(
    "LaunchConfigurationNamesTypeDescribeLaunchConfigurationsPaginateTypeDef",
    {
        "LaunchConfigurationNames": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
AutoScalingInstanceDetailsTypeDef = TypedDict(
    "AutoScalingInstanceDetailsTypeDef",
    {
        "InstanceId": str,
        "AutoScalingGroupName": str,
        "AvailabilityZone": str,
        "LifecycleState": str,
        "HealthStatus": str,
        "ProtectedFromScaleIn": bool,
        "InstanceType": NotRequired[str],
        "LaunchConfigurationName": NotRequired[str],
        "LaunchTemplate": NotRequired[LaunchTemplateSpecificationTypeDef],
        "WeightedCapacity": NotRequired[str],
    },
)
InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "InstanceId": str,
        "AvailabilityZone": str,
        "LifecycleState": LifecycleStateType,
        "HealthStatus": str,
        "ProtectedFromScaleIn": bool,
        "InstanceType": NotRequired[str],
        "LaunchConfigurationName": NotRequired[str],
        "LaunchTemplate": NotRequired[LaunchTemplateSpecificationTypeDef],
        "WeightedCapacity": NotRequired[str],
    },
)
TagsTypeTypeDef = TypedDict(
    "TagsTypeTypeDef",
    {
        "Tags": List[TagDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
BatchDeleteScheduledActionAnswerTypeDef = TypedDict(
    "BatchDeleteScheduledActionAnswerTypeDef",
    {
        "FailedScheduledActions": List[FailedScheduledUpdateGroupActionRequestTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchPutScheduledUpdateGroupActionAnswerTypeDef = TypedDict(
    "BatchPutScheduledUpdateGroupActionAnswerTypeDef",
    {
        "FailedScheduledUpdateGroupActions": List[FailedScheduledUpdateGroupActionRequestTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BlockDeviceMappingTypeDef = TypedDict(
    "BlockDeviceMappingTypeDef",
    {
        "DeviceName": str,
        "VirtualName": NotRequired[str],
        "Ebs": NotRequired[EbsTypeDef],
        "NoDevice": NotRequired[bool],
    },
)
CreateOrUpdateTagsTypeRequestTypeDef = TypedDict(
    "CreateOrUpdateTagsTypeRequestTypeDef",
    {
        "Tags": Sequence[TagTypeDef],
    },
)
DeleteTagsTypeRequestTypeDef = TypedDict(
    "DeleteTagsTypeRequestTypeDef",
    {
        "Tags": Sequence[TagTypeDef],
    },
)
MetricOutputTypeDef = TypedDict(
    "MetricOutputTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": NotRequired[List[MetricDimensionTypeDef]],
    },
)
MetricTypeDef = TypedDict(
    "MetricTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "Dimensions": NotRequired[Sequence[MetricDimensionTypeDef]],
    },
)
DescribeLifecycleHooksAnswerTypeDef = TypedDict(
    "DescribeLifecycleHooksAnswerTypeDef",
    {
        "LifecycleHooks": List[LifecycleHookTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeLoadBalancerTargetGroupsResponseTypeDef = TypedDict(
    "DescribeLoadBalancerTargetGroupsResponseTypeDef",
    {
        "LoadBalancerTargetGroups": List[LoadBalancerTargetGroupStateTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeLoadBalancersResponseTypeDef = TypedDict(
    "DescribeLoadBalancersResponseTypeDef",
    {
        "LoadBalancers": List[LoadBalancerStateTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeMetricCollectionTypesAnswerTypeDef = TypedDict(
    "DescribeMetricCollectionTypesAnswerTypeDef",
    {
        "Metrics": List[MetricCollectionTypeTypeDef],
        "Granularities": List[MetricGranularityTypeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeNotificationConfigurationsAnswerTypeDef = TypedDict(
    "DescribeNotificationConfigurationsAnswerTypeDef",
    {
        "NotificationConfigurations": List[NotificationConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeScheduledActionsTypeDescribeScheduledActionsPaginateTypeDef = TypedDict(
    "DescribeScheduledActionsTypeDescribeScheduledActionsPaginateTypeDef",
    {
        "AutoScalingGroupName": NotRequired[str],
        "ScheduledActionNames": NotRequired[Sequence[str]],
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeScheduledActionsTypeRequestTypeDef = TypedDict(
    "DescribeScheduledActionsTypeRequestTypeDef",
    {
        "AutoScalingGroupName": NotRequired[str],
        "ScheduledActionNames": NotRequired[Sequence[str]],
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "NextToken": NotRequired[str],
        "MaxRecords": NotRequired[int],
    },
)
GetPredictiveScalingForecastTypeRequestTypeDef = TypedDict(
    "GetPredictiveScalingForecastTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "PolicyName": str,
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
    },
)
PutScheduledUpdateGroupActionTypeRequestTypeDef = TypedDict(
    "PutScheduledUpdateGroupActionTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "ScheduledActionName": str,
        "Time": NotRequired[TimestampTypeDef],
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "Recurrence": NotRequired[str],
        "MinSize": NotRequired[int],
        "MaxSize": NotRequired[int],
        "DesiredCapacity": NotRequired[int],
        "TimeZone": NotRequired[str],
    },
)
ScheduledUpdateGroupActionRequestTypeDef = TypedDict(
    "ScheduledUpdateGroupActionRequestTypeDef",
    {
        "ScheduledActionName": str,
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "Recurrence": NotRequired[str],
        "MinSize": NotRequired[int],
        "MaxSize": NotRequired[int],
        "DesiredCapacity": NotRequired[int],
        "TimeZone": NotRequired[str],
    },
)
DescribeTrafficSourcesResponseTypeDef = TypedDict(
    "DescribeTrafficSourcesResponseTypeDef",
    {
        "TrafficSources": List[TrafficSourceStateTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
InstanceRefreshProgressDetailsTypeDef = TypedDict(
    "InstanceRefreshProgressDetailsTypeDef",
    {
        "LivePoolProgress": NotRequired[InstanceRefreshLivePoolProgressTypeDef],
        "WarmPoolProgress": NotRequired[InstanceRefreshWarmPoolProgressTypeDef],
    },
)
InstanceRequirementsOutputTypeDef = TypedDict(
    "InstanceRequirementsOutputTypeDef",
    {
        "VCpuCount": VCpuCountRequestTypeDef,
        "MemoryMiB": MemoryMiBRequestTypeDef,
        "CpuManufacturers": NotRequired[List[CpuManufacturerType]],
        "MemoryGiBPerVCpu": NotRequired[MemoryGiBPerVCpuRequestTypeDef],
        "ExcludedInstanceTypes": NotRequired[List[str]],
        "InstanceGenerations": NotRequired[List[InstanceGenerationType]],
        "SpotMaxPricePercentageOverLowestPrice": NotRequired[int],
        "MaxSpotPriceAsPercentageOfOptimalOnDemandPrice": NotRequired[int],
        "OnDemandMaxPricePercentageOverLowestPrice": NotRequired[int],
        "BareMetal": NotRequired[BareMetalType],
        "BurstablePerformance": NotRequired[BurstablePerformanceType],
        "RequireHibernateSupport": NotRequired[bool],
        "NetworkInterfaceCount": NotRequired[NetworkInterfaceCountRequestTypeDef],
        "LocalStorage": NotRequired[LocalStorageType],
        "LocalStorageTypes": NotRequired[List[LocalStorageTypeType]],
        "TotalLocalStorageGB": NotRequired[TotalLocalStorageGBRequestTypeDef],
        "BaselineEbsBandwidthMbps": NotRequired[BaselineEbsBandwidthMbpsRequestTypeDef],
        "AcceleratorTypes": NotRequired[List[AcceleratorTypeType]],
        "AcceleratorCount": NotRequired[AcceleratorCountRequestTypeDef],
        "AcceleratorManufacturers": NotRequired[List[AcceleratorManufacturerType]],
        "AcceleratorNames": NotRequired[List[AcceleratorNameType]],
        "AcceleratorTotalMemoryMiB": NotRequired[AcceleratorTotalMemoryMiBRequestTypeDef],
        "NetworkBandwidthGbps": NotRequired[NetworkBandwidthGbpsRequestTypeDef],
        "AllowedInstanceTypes": NotRequired[List[str]],
    },
)
InstanceRequirementsTypeDef = TypedDict(
    "InstanceRequirementsTypeDef",
    {
        "VCpuCount": VCpuCountRequestTypeDef,
        "MemoryMiB": MemoryMiBRequestTypeDef,
        "CpuManufacturers": NotRequired[Sequence[CpuManufacturerType]],
        "MemoryGiBPerVCpu": NotRequired[MemoryGiBPerVCpuRequestTypeDef],
        "ExcludedInstanceTypes": NotRequired[Sequence[str]],
        "InstanceGenerations": NotRequired[Sequence[InstanceGenerationType]],
        "SpotMaxPricePercentageOverLowestPrice": NotRequired[int],
        "MaxSpotPriceAsPercentageOfOptimalOnDemandPrice": NotRequired[int],
        "OnDemandMaxPricePercentageOverLowestPrice": NotRequired[int],
        "BareMetal": NotRequired[BareMetalType],
        "BurstablePerformance": NotRequired[BurstablePerformanceType],
        "RequireHibernateSupport": NotRequired[bool],
        "NetworkInterfaceCount": NotRequired[NetworkInterfaceCountRequestTypeDef],
        "LocalStorage": NotRequired[LocalStorageType],
        "LocalStorageTypes": NotRequired[Sequence[LocalStorageTypeType]],
        "TotalLocalStorageGB": NotRequired[TotalLocalStorageGBRequestTypeDef],
        "BaselineEbsBandwidthMbps": NotRequired[BaselineEbsBandwidthMbpsRequestTypeDef],
        "AcceleratorTypes": NotRequired[Sequence[AcceleratorTypeType]],
        "AcceleratorCount": NotRequired[AcceleratorCountRequestTypeDef],
        "AcceleratorManufacturers": NotRequired[Sequence[AcceleratorManufacturerType]],
        "AcceleratorNames": NotRequired[Sequence[AcceleratorNameType]],
        "AcceleratorTotalMemoryMiB": NotRequired[AcceleratorTotalMemoryMiBRequestTypeDef],
        "NetworkBandwidthGbps": NotRequired[NetworkBandwidthGbpsRequestTypeDef],
        "AllowedInstanceTypes": NotRequired[Sequence[str]],
    },
)
PutWarmPoolTypeRequestTypeDef = TypedDict(
    "PutWarmPoolTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "MaxGroupPreparedCapacity": NotRequired[int],
        "MinSize": NotRequired[int],
        "PoolState": NotRequired[WarmPoolStateType],
        "InstanceReusePolicy": NotRequired[InstanceReusePolicyTypeDef],
    },
)
WarmPoolConfigurationTypeDef = TypedDict(
    "WarmPoolConfigurationTypeDef",
    {
        "MaxGroupPreparedCapacity": NotRequired[int],
        "MinSize": NotRequired[int],
        "PoolState": NotRequired[WarmPoolStateType],
        "Status": NotRequired[Literal["PendingDelete"]],
        "InstanceReusePolicy": NotRequired[InstanceReusePolicyTypeDef],
    },
)
ProcessesTypeTypeDef = TypedDict(
    "ProcessesTypeTypeDef",
    {
        "Processes": List[ProcessTypeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ScheduledActionsTypeTypeDef = TypedDict(
    "ScheduledActionsTypeTypeDef",
    {
        "ScheduledUpdateGroupActions": List[ScheduledUpdateGroupActionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
RefreshPreferencesTypeDef = TypedDict(
    "RefreshPreferencesTypeDef",
    {
        "MinHealthyPercentage": NotRequired[int],
        "InstanceWarmup": NotRequired[int],
        "CheckpointPercentages": NotRequired[Sequence[int]],
        "CheckpointDelay": NotRequired[int],
        "SkipMatching": NotRequired[bool],
        "AutoRollback": NotRequired[bool],
        "ScaleInProtectedInstances": NotRequired[ScaleInProtectedInstancesType],
        "StandbyInstances": NotRequired[StandbyInstancesType],
        "AlarmSpecification": NotRequired[AlarmSpecificationUnionTypeDef],
        "MaxHealthyPercentage": NotRequired[int],
    },
)
AutoScalingInstancesTypeTypeDef = TypedDict(
    "AutoScalingInstancesTypeTypeDef",
    {
        "AutoScalingInstances": List[AutoScalingInstanceDetailsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateLaunchConfigurationTypeRequestTypeDef = TypedDict(
    "CreateLaunchConfigurationTypeRequestTypeDef",
    {
        "LaunchConfigurationName": str,
        "ImageId": NotRequired[str],
        "KeyName": NotRequired[str],
        "SecurityGroups": NotRequired[Sequence[str]],
        "ClassicLinkVPCId": NotRequired[str],
        "ClassicLinkVPCSecurityGroups": NotRequired[Sequence[str]],
        "UserData": NotRequired[str],
        "InstanceId": NotRequired[str],
        "InstanceType": NotRequired[str],
        "KernelId": NotRequired[str],
        "RamdiskId": NotRequired[str],
        "BlockDeviceMappings": NotRequired[Sequence[BlockDeviceMappingTypeDef]],
        "InstanceMonitoring": NotRequired[InstanceMonitoringTypeDef],
        "SpotPrice": NotRequired[str],
        "IamInstanceProfile": NotRequired[str],
        "EbsOptimized": NotRequired[bool],
        "AssociatePublicIpAddress": NotRequired[bool],
        "PlacementTenancy": NotRequired[str],
        "MetadataOptions": NotRequired[InstanceMetadataOptionsTypeDef],
    },
)
LaunchConfigurationTypeDef = TypedDict(
    "LaunchConfigurationTypeDef",
    {
        "LaunchConfigurationName": str,
        "ImageId": str,
        "InstanceType": str,
        "CreatedTime": datetime,
        "LaunchConfigurationARN": NotRequired[str],
        "KeyName": NotRequired[str],
        "SecurityGroups": NotRequired[List[str]],
        "ClassicLinkVPCId": NotRequired[str],
        "ClassicLinkVPCSecurityGroups": NotRequired[List[str]],
        "UserData": NotRequired[str],
        "KernelId": NotRequired[str],
        "RamdiskId": NotRequired[str],
        "BlockDeviceMappings": NotRequired[List[BlockDeviceMappingTypeDef]],
        "InstanceMonitoring": NotRequired[InstanceMonitoringTypeDef],
        "SpotPrice": NotRequired[str],
        "IamInstanceProfile": NotRequired[str],
        "EbsOptimized": NotRequired[bool],
        "AssociatePublicIpAddress": NotRequired[bool],
        "PlacementTenancy": NotRequired[str],
        "MetadataOptions": NotRequired[InstanceMetadataOptionsTypeDef],
    },
)
MetricStatOutputTypeDef = TypedDict(
    "MetricStatOutputTypeDef",
    {
        "Metric": MetricOutputTypeDef,
        "Stat": str,
        "Unit": NotRequired[str],
    },
)
TargetTrackingMetricStatOutputTypeDef = TypedDict(
    "TargetTrackingMetricStatOutputTypeDef",
    {
        "Metric": MetricOutputTypeDef,
        "Stat": str,
        "Unit": NotRequired[str],
    },
)
MetricUnionTypeDef = Union[MetricTypeDef, MetricOutputTypeDef]
BatchPutScheduledUpdateGroupActionTypeRequestTypeDef = TypedDict(
    "BatchPutScheduledUpdateGroupActionTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "ScheduledUpdateGroupActions": Sequence[ScheduledUpdateGroupActionRequestTypeDef],
    },
)
RollbackDetailsTypeDef = TypedDict(
    "RollbackDetailsTypeDef",
    {
        "RollbackReason": NotRequired[str],
        "RollbackStartTime": NotRequired[datetime],
        "PercentageCompleteOnRollback": NotRequired[int],
        "InstancesToUpdateOnRollback": NotRequired[int],
        "ProgressDetailsOnRollback": NotRequired[InstanceRefreshProgressDetailsTypeDef],
    },
)
LaunchTemplateOverridesOutputTypeDef = TypedDict(
    "LaunchTemplateOverridesOutputTypeDef",
    {
        "InstanceType": NotRequired[str],
        "WeightedCapacity": NotRequired[str],
        "LaunchTemplateSpecification": NotRequired[LaunchTemplateSpecificationTypeDef],
        "InstanceRequirements": NotRequired[InstanceRequirementsOutputTypeDef],
    },
)
InstanceRequirementsUnionTypeDef = Union[
    InstanceRequirementsTypeDef, InstanceRequirementsOutputTypeDef
]
DescribeWarmPoolAnswerTypeDef = TypedDict(
    "DescribeWarmPoolAnswerTypeDef",
    {
        "WarmPoolConfiguration": WarmPoolConfigurationTypeDef,
        "Instances": List[InstanceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
LaunchConfigurationsTypeTypeDef = TypedDict(
    "LaunchConfigurationsTypeTypeDef",
    {
        "LaunchConfigurations": List[LaunchConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
MetricDataQueryOutputTypeDef = TypedDict(
    "MetricDataQueryOutputTypeDef",
    {
        "Id": str,
        "Expression": NotRequired[str],
        "MetricStat": NotRequired[MetricStatOutputTypeDef],
        "Label": NotRequired[str],
        "ReturnData": NotRequired[bool],
    },
)
TargetTrackingMetricDataQueryOutputTypeDef = TypedDict(
    "TargetTrackingMetricDataQueryOutputTypeDef",
    {
        "Id": str,
        "Expression": NotRequired[str],
        "MetricStat": NotRequired[TargetTrackingMetricStatOutputTypeDef],
        "Label": NotRequired[str],
        "ReturnData": NotRequired[bool],
    },
)
MetricStatTypeDef = TypedDict(
    "MetricStatTypeDef",
    {
        "Metric": MetricUnionTypeDef,
        "Stat": str,
        "Unit": NotRequired[str],
    },
)
TargetTrackingMetricStatTypeDef = TypedDict(
    "TargetTrackingMetricStatTypeDef",
    {
        "Metric": MetricUnionTypeDef,
        "Stat": str,
        "Unit": NotRequired[str],
    },
)
LaunchTemplateOutputTypeDef = TypedDict(
    "LaunchTemplateOutputTypeDef",
    {
        "LaunchTemplateSpecification": NotRequired[LaunchTemplateSpecificationTypeDef],
        "Overrides": NotRequired[List[LaunchTemplateOverridesOutputTypeDef]],
    },
)
LaunchTemplateOverridesTypeDef = TypedDict(
    "LaunchTemplateOverridesTypeDef",
    {
        "InstanceType": NotRequired[str],
        "WeightedCapacity": NotRequired[str],
        "LaunchTemplateSpecification": NotRequired[LaunchTemplateSpecificationTypeDef],
        "InstanceRequirements": NotRequired[InstanceRequirementsUnionTypeDef],
    },
)
PredictiveScalingCustomizedCapacityMetricOutputTypeDef = TypedDict(
    "PredictiveScalingCustomizedCapacityMetricOutputTypeDef",
    {
        "MetricDataQueries": List[MetricDataQueryOutputTypeDef],
    },
)
PredictiveScalingCustomizedLoadMetricOutputTypeDef = TypedDict(
    "PredictiveScalingCustomizedLoadMetricOutputTypeDef",
    {
        "MetricDataQueries": List[MetricDataQueryOutputTypeDef],
    },
)
PredictiveScalingCustomizedScalingMetricOutputTypeDef = TypedDict(
    "PredictiveScalingCustomizedScalingMetricOutputTypeDef",
    {
        "MetricDataQueries": List[MetricDataQueryOutputTypeDef],
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
MetricStatUnionTypeDef = Union[MetricStatTypeDef, MetricStatOutputTypeDef]
TargetTrackingMetricStatUnionTypeDef = Union[
    TargetTrackingMetricStatTypeDef, TargetTrackingMetricStatOutputTypeDef
]
MixedInstancesPolicyOutputTypeDef = TypedDict(
    "MixedInstancesPolicyOutputTypeDef",
    {
        "LaunchTemplate": NotRequired[LaunchTemplateOutputTypeDef],
        "InstancesDistribution": NotRequired[InstancesDistributionTypeDef],
    },
)
LaunchTemplateOverridesUnionTypeDef = Union[
    LaunchTemplateOverridesTypeDef, LaunchTemplateOverridesOutputTypeDef
]
PredictiveScalingMetricSpecificationOutputTypeDef = TypedDict(
    "PredictiveScalingMetricSpecificationOutputTypeDef",
    {
        "TargetValue": float,
        "PredefinedMetricPairSpecification": NotRequired[
            PredictiveScalingPredefinedMetricPairTypeDef
        ],
        "PredefinedScalingMetricSpecification": NotRequired[
            PredictiveScalingPredefinedScalingMetricTypeDef
        ],
        "PredefinedLoadMetricSpecification": NotRequired[
            PredictiveScalingPredefinedLoadMetricTypeDef
        ],
        "CustomizedScalingMetricSpecification": NotRequired[
            PredictiveScalingCustomizedScalingMetricOutputTypeDef
        ],
        "CustomizedLoadMetricSpecification": NotRequired[
            PredictiveScalingCustomizedLoadMetricOutputTypeDef
        ],
        "CustomizedCapacityMetricSpecification": NotRequired[
            PredictiveScalingCustomizedCapacityMetricOutputTypeDef
        ],
    },
)
TargetTrackingConfigurationOutputTypeDef = TypedDict(
    "TargetTrackingConfigurationOutputTypeDef",
    {
        "TargetValue": float,
        "PredefinedMetricSpecification": NotRequired[PredefinedMetricSpecificationTypeDef],
        "CustomizedMetricSpecification": NotRequired[CustomizedMetricSpecificationOutputTypeDef],
        "DisableScaleIn": NotRequired[bool],
    },
)
MetricDataQueryTypeDef = TypedDict(
    "MetricDataQueryTypeDef",
    {
        "Id": str,
        "Expression": NotRequired[str],
        "MetricStat": NotRequired[MetricStatUnionTypeDef],
        "Label": NotRequired[str],
        "ReturnData": NotRequired[bool],
    },
)
TargetTrackingMetricDataQueryTypeDef = TypedDict(
    "TargetTrackingMetricDataQueryTypeDef",
    {
        "Id": str,
        "Expression": NotRequired[str],
        "MetricStat": NotRequired[TargetTrackingMetricStatUnionTypeDef],
        "Label": NotRequired[str],
        "ReturnData": NotRequired[bool],
    },
)
AutoScalingGroupTypeDef = TypedDict(
    "AutoScalingGroupTypeDef",
    {
        "AutoScalingGroupName": str,
        "MinSize": int,
        "MaxSize": int,
        "DesiredCapacity": int,
        "DefaultCooldown": int,
        "AvailabilityZones": List[str],
        "HealthCheckType": str,
        "CreatedTime": datetime,
        "AutoScalingGroupARN": NotRequired[str],
        "LaunchConfigurationName": NotRequired[str],
        "LaunchTemplate": NotRequired[LaunchTemplateSpecificationTypeDef],
        "MixedInstancesPolicy": NotRequired[MixedInstancesPolicyOutputTypeDef],
        "PredictedCapacity": NotRequired[int],
        "LoadBalancerNames": NotRequired[List[str]],
        "TargetGroupARNs": NotRequired[List[str]],
        "HealthCheckGracePeriod": NotRequired[int],
        "Instances": NotRequired[List[InstanceTypeDef]],
        "SuspendedProcesses": NotRequired[List[SuspendedProcessTypeDef]],
        "PlacementGroup": NotRequired[str],
        "VPCZoneIdentifier": NotRequired[str],
        "EnabledMetrics": NotRequired[List[EnabledMetricTypeDef]],
        "Status": NotRequired[str],
        "Tags": NotRequired[List[TagDescriptionTypeDef]],
        "TerminationPolicies": NotRequired[List[str]],
        "NewInstancesProtectedFromScaleIn": NotRequired[bool],
        "ServiceLinkedRoleARN": NotRequired[str],
        "MaxInstanceLifetime": NotRequired[int],
        "CapacityRebalance": NotRequired[bool],
        "WarmPoolConfiguration": NotRequired[WarmPoolConfigurationTypeDef],
        "WarmPoolSize": NotRequired[int],
        "Context": NotRequired[str],
        "DesiredCapacityType": NotRequired[str],
        "DefaultInstanceWarmup": NotRequired[int],
        "TrafficSources": NotRequired[List[TrafficSourceIdentifierTypeDef]],
        "InstanceMaintenancePolicy": NotRequired[InstanceMaintenancePolicyTypeDef],
    },
)
DesiredConfigurationOutputTypeDef = TypedDict(
    "DesiredConfigurationOutputTypeDef",
    {
        "LaunchTemplate": NotRequired[LaunchTemplateSpecificationTypeDef],
        "MixedInstancesPolicy": NotRequired[MixedInstancesPolicyOutputTypeDef],
    },
)
LaunchTemplateTypeDef = TypedDict(
    "LaunchTemplateTypeDef",
    {
        "LaunchTemplateSpecification": NotRequired[LaunchTemplateSpecificationTypeDef],
        "Overrides": NotRequired[Sequence[LaunchTemplateOverridesUnionTypeDef]],
    },
)
LoadForecastTypeDef = TypedDict(
    "LoadForecastTypeDef",
    {
        "Timestamps": List[datetime],
        "Values": List[float],
        "MetricSpecification": PredictiveScalingMetricSpecificationOutputTypeDef,
    },
)
PredictiveScalingConfigurationOutputTypeDef = TypedDict(
    "PredictiveScalingConfigurationOutputTypeDef",
    {
        "MetricSpecifications": List[PredictiveScalingMetricSpecificationOutputTypeDef],
        "Mode": NotRequired[PredictiveScalingModeType],
        "SchedulingBufferTime": NotRequired[int],
        "MaxCapacityBreachBehavior": NotRequired[PredictiveScalingMaxCapacityBreachBehaviorType],
        "MaxCapacityBuffer": NotRequired[int],
    },
)
MetricDataQueryUnionTypeDef = Union[MetricDataQueryTypeDef, MetricDataQueryOutputTypeDef]
PredictiveScalingCustomizedCapacityMetricTypeDef = TypedDict(
    "PredictiveScalingCustomizedCapacityMetricTypeDef",
    {
        "MetricDataQueries": Sequence[MetricDataQueryTypeDef],
    },
)
PredictiveScalingCustomizedLoadMetricTypeDef = TypedDict(
    "PredictiveScalingCustomizedLoadMetricTypeDef",
    {
        "MetricDataQueries": Sequence[MetricDataQueryTypeDef],
    },
)
TargetTrackingMetricDataQueryUnionTypeDef = Union[
    TargetTrackingMetricDataQueryTypeDef, TargetTrackingMetricDataQueryOutputTypeDef
]
AutoScalingGroupsTypeTypeDef = TypedDict(
    "AutoScalingGroupsTypeTypeDef",
    {
        "AutoScalingGroups": List[AutoScalingGroupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
InstanceRefreshTypeDef = TypedDict(
    "InstanceRefreshTypeDef",
    {
        "InstanceRefreshId": NotRequired[str],
        "AutoScalingGroupName": NotRequired[str],
        "Status": NotRequired[InstanceRefreshStatusType],
        "StatusReason": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "PercentageComplete": NotRequired[int],
        "InstancesToUpdate": NotRequired[int],
        "ProgressDetails": NotRequired[InstanceRefreshProgressDetailsTypeDef],
        "Preferences": NotRequired[RefreshPreferencesOutputTypeDef],
        "DesiredConfiguration": NotRequired[DesiredConfigurationOutputTypeDef],
        "RollbackDetails": NotRequired[RollbackDetailsTypeDef],
    },
)
LaunchTemplateUnionTypeDef = Union[LaunchTemplateTypeDef, LaunchTemplateOutputTypeDef]
GetPredictiveScalingForecastAnswerTypeDef = TypedDict(
    "GetPredictiveScalingForecastAnswerTypeDef",
    {
        "LoadForecast": List[LoadForecastTypeDef],
        "CapacityForecast": CapacityForecastTypeDef,
        "UpdateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ScalingPolicyTypeDef = TypedDict(
    "ScalingPolicyTypeDef",
    {
        "AutoScalingGroupName": NotRequired[str],
        "PolicyName": NotRequired[str],
        "PolicyARN": NotRequired[str],
        "PolicyType": NotRequired[str],
        "AdjustmentType": NotRequired[str],
        "MinAdjustmentStep": NotRequired[int],
        "MinAdjustmentMagnitude": NotRequired[int],
        "ScalingAdjustment": NotRequired[int],
        "Cooldown": NotRequired[int],
        "StepAdjustments": NotRequired[List[StepAdjustmentTypeDef]],
        "MetricAggregationType": NotRequired[str],
        "EstimatedInstanceWarmup": NotRequired[int],
        "Alarms": NotRequired[List[AlarmTypeDef]],
        "TargetTrackingConfiguration": NotRequired[TargetTrackingConfigurationOutputTypeDef],
        "Enabled": NotRequired[bool],
        "PredictiveScalingConfiguration": NotRequired[PredictiveScalingConfigurationOutputTypeDef],
    },
)
PredictiveScalingCustomizedScalingMetricTypeDef = TypedDict(
    "PredictiveScalingCustomizedScalingMetricTypeDef",
    {
        "MetricDataQueries": Sequence[MetricDataQueryUnionTypeDef],
    },
)
PredictiveScalingCustomizedCapacityMetricUnionTypeDef = Union[
    PredictiveScalingCustomizedCapacityMetricTypeDef,
    PredictiveScalingCustomizedCapacityMetricOutputTypeDef,
]
PredictiveScalingCustomizedLoadMetricUnionTypeDef = Union[
    PredictiveScalingCustomizedLoadMetricTypeDef, PredictiveScalingCustomizedLoadMetricOutputTypeDef
]
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
DescribeInstanceRefreshesAnswerTypeDef = TypedDict(
    "DescribeInstanceRefreshesAnswerTypeDef",
    {
        "InstanceRefreshes": List[InstanceRefreshTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
MixedInstancesPolicyTypeDef = TypedDict(
    "MixedInstancesPolicyTypeDef",
    {
        "LaunchTemplate": NotRequired[LaunchTemplateUnionTypeDef],
        "InstancesDistribution": NotRequired[InstancesDistributionTypeDef],
    },
)
PoliciesTypeTypeDef = TypedDict(
    "PoliciesTypeTypeDef",
    {
        "ScalingPolicies": List[ScalingPolicyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PredictiveScalingCustomizedScalingMetricUnionTypeDef = Union[
    PredictiveScalingCustomizedScalingMetricTypeDef,
    PredictiveScalingCustomizedScalingMetricOutputTypeDef,
]
CustomizedMetricSpecificationUnionTypeDef = Union[
    CustomizedMetricSpecificationTypeDef, CustomizedMetricSpecificationOutputTypeDef
]
CreateAutoScalingGroupTypeRequestTypeDef = TypedDict(
    "CreateAutoScalingGroupTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "MinSize": int,
        "MaxSize": int,
        "LaunchConfigurationName": NotRequired[str],
        "LaunchTemplate": NotRequired[LaunchTemplateSpecificationTypeDef],
        "MixedInstancesPolicy": NotRequired[MixedInstancesPolicyTypeDef],
        "InstanceId": NotRequired[str],
        "DesiredCapacity": NotRequired[int],
        "DefaultCooldown": NotRequired[int],
        "AvailabilityZones": NotRequired[Sequence[str]],
        "LoadBalancerNames": NotRequired[Sequence[str]],
        "TargetGroupARNs": NotRequired[Sequence[str]],
        "HealthCheckType": NotRequired[str],
        "HealthCheckGracePeriod": NotRequired[int],
        "PlacementGroup": NotRequired[str],
        "VPCZoneIdentifier": NotRequired[str],
        "TerminationPolicies": NotRequired[Sequence[str]],
        "NewInstancesProtectedFromScaleIn": NotRequired[bool],
        "CapacityRebalance": NotRequired[bool],
        "LifecycleHookSpecificationList": NotRequired[Sequence[LifecycleHookSpecificationTypeDef]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ServiceLinkedRoleARN": NotRequired[str],
        "MaxInstanceLifetime": NotRequired[int],
        "Context": NotRequired[str],
        "DesiredCapacityType": NotRequired[str],
        "DefaultInstanceWarmup": NotRequired[int],
        "TrafficSources": NotRequired[Sequence[TrafficSourceIdentifierTypeDef]],
        "InstanceMaintenancePolicy": NotRequired[InstanceMaintenancePolicyTypeDef],
    },
)
MixedInstancesPolicyUnionTypeDef = Union[
    MixedInstancesPolicyTypeDef, MixedInstancesPolicyOutputTypeDef
]
UpdateAutoScalingGroupTypeRequestTypeDef = TypedDict(
    "UpdateAutoScalingGroupTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "LaunchConfigurationName": NotRequired[str],
        "LaunchTemplate": NotRequired[LaunchTemplateSpecificationTypeDef],
        "MixedInstancesPolicy": NotRequired[MixedInstancesPolicyTypeDef],
        "MinSize": NotRequired[int],
        "MaxSize": NotRequired[int],
        "DesiredCapacity": NotRequired[int],
        "DefaultCooldown": NotRequired[int],
        "AvailabilityZones": NotRequired[Sequence[str]],
        "HealthCheckType": NotRequired[str],
        "HealthCheckGracePeriod": NotRequired[int],
        "PlacementGroup": NotRequired[str],
        "VPCZoneIdentifier": NotRequired[str],
        "TerminationPolicies": NotRequired[Sequence[str]],
        "NewInstancesProtectedFromScaleIn": NotRequired[bool],
        "ServiceLinkedRoleARN": NotRequired[str],
        "MaxInstanceLifetime": NotRequired[int],
        "CapacityRebalance": NotRequired[bool],
        "Context": NotRequired[str],
        "DesiredCapacityType": NotRequired[str],
        "DefaultInstanceWarmup": NotRequired[int],
        "InstanceMaintenancePolicy": NotRequired[InstanceMaintenancePolicyTypeDef],
    },
)
PredictiveScalingMetricSpecificationTypeDef = TypedDict(
    "PredictiveScalingMetricSpecificationTypeDef",
    {
        "TargetValue": float,
        "PredefinedMetricPairSpecification": NotRequired[
            PredictiveScalingPredefinedMetricPairTypeDef
        ],
        "PredefinedScalingMetricSpecification": NotRequired[
            PredictiveScalingPredefinedScalingMetricTypeDef
        ],
        "PredefinedLoadMetricSpecification": NotRequired[
            PredictiveScalingPredefinedLoadMetricTypeDef
        ],
        "CustomizedScalingMetricSpecification": NotRequired[
            PredictiveScalingCustomizedScalingMetricUnionTypeDef
        ],
        "CustomizedLoadMetricSpecification": NotRequired[
            PredictiveScalingCustomizedLoadMetricUnionTypeDef
        ],
        "CustomizedCapacityMetricSpecification": NotRequired[
            PredictiveScalingCustomizedCapacityMetricUnionTypeDef
        ],
    },
)
TargetTrackingConfigurationTypeDef = TypedDict(
    "TargetTrackingConfigurationTypeDef",
    {
        "TargetValue": float,
        "PredefinedMetricSpecification": NotRequired[PredefinedMetricSpecificationTypeDef],
        "CustomizedMetricSpecification": NotRequired[CustomizedMetricSpecificationUnionTypeDef],
        "DisableScaleIn": NotRequired[bool],
    },
)
DesiredConfigurationTypeDef = TypedDict(
    "DesiredConfigurationTypeDef",
    {
        "LaunchTemplate": NotRequired[LaunchTemplateSpecificationTypeDef],
        "MixedInstancesPolicy": NotRequired[MixedInstancesPolicyUnionTypeDef],
    },
)
PredictiveScalingMetricSpecificationUnionTypeDef = Union[
    PredictiveScalingMetricSpecificationTypeDef, PredictiveScalingMetricSpecificationOutputTypeDef
]
StartInstanceRefreshTypeRequestTypeDef = TypedDict(
    "StartInstanceRefreshTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "Strategy": NotRequired[Literal["Rolling"]],
        "DesiredConfiguration": NotRequired[DesiredConfigurationTypeDef],
        "Preferences": NotRequired[RefreshPreferencesTypeDef],
    },
)
PredictiveScalingConfigurationTypeDef = TypedDict(
    "PredictiveScalingConfigurationTypeDef",
    {
        "MetricSpecifications": Sequence[PredictiveScalingMetricSpecificationUnionTypeDef],
        "Mode": NotRequired[PredictiveScalingModeType],
        "SchedulingBufferTime": NotRequired[int],
        "MaxCapacityBreachBehavior": NotRequired[PredictiveScalingMaxCapacityBreachBehaviorType],
        "MaxCapacityBuffer": NotRequired[int],
    },
)
PutScalingPolicyTypeRequestTypeDef = TypedDict(
    "PutScalingPolicyTypeRequestTypeDef",
    {
        "AutoScalingGroupName": str,
        "PolicyName": str,
        "PolicyType": NotRequired[str],
        "AdjustmentType": NotRequired[str],
        "MinAdjustmentStep": NotRequired[int],
        "MinAdjustmentMagnitude": NotRequired[int],
        "ScalingAdjustment": NotRequired[int],
        "Cooldown": NotRequired[int],
        "MetricAggregationType": NotRequired[str],
        "StepAdjustments": NotRequired[Sequence[StepAdjustmentTypeDef]],
        "EstimatedInstanceWarmup": NotRequired[int],
        "TargetTrackingConfiguration": NotRequired[TargetTrackingConfigurationTypeDef],
        "Enabled": NotRequired[bool],
        "PredictiveScalingConfiguration": NotRequired[PredictiveScalingConfigurationTypeDef],
    },
)
