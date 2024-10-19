"""
Type annotations for scheduler service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_scheduler/type_defs/)

Usage::

    ```python
    from mypy_boto3_scheduler.type_defs import AwsVpcConfigurationOutputTypeDef

    data: AwsVpcConfigurationOutputTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    ActionAfterCompletionType,
    AssignPublicIpType,
    FlexibleTimeWindowModeType,
    LaunchTypeType,
    PlacementConstraintTypeType,
    PlacementStrategyTypeType,
    ScheduleGroupStateType,
    ScheduleStateType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AwsVpcConfigurationOutputTypeDef",
    "AwsVpcConfigurationTypeDef",
    "CapacityProviderStrategyItemTypeDef",
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "FlexibleTimeWindowTypeDef",
    "TimestampTypeDef",
    "DeadLetterConfigTypeDef",
    "DeleteScheduleGroupInputRequestTypeDef",
    "DeleteScheduleInputRequestTypeDef",
    "PlacementConstraintTypeDef",
    "PlacementStrategyTypeDef",
    "EventBridgeParametersTypeDef",
    "GetScheduleGroupInputRequestTypeDef",
    "GetScheduleInputRequestTypeDef",
    "KinesisParametersTypeDef",
    "PaginatorConfigTypeDef",
    "ListScheduleGroupsInputRequestTypeDef",
    "ScheduleGroupSummaryTypeDef",
    "ListSchedulesInputRequestTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "RetryPolicyTypeDef",
    "SageMakerPipelineParameterTypeDef",
    "TargetSummaryTypeDef",
    "SqsParametersTypeDef",
    "UntagResourceInputRequestTypeDef",
    "NetworkConfigurationOutputTypeDef",
    "AwsVpcConfigurationUnionTypeDef",
    "CreateScheduleGroupInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "CreateScheduleGroupOutputTypeDef",
    "CreateScheduleOutputTypeDef",
    "GetScheduleGroupOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "UpdateScheduleOutputTypeDef",
    "ListScheduleGroupsInputListScheduleGroupsPaginateTypeDef",
    "ListSchedulesInputListSchedulesPaginateTypeDef",
    "ListScheduleGroupsOutputTypeDef",
    "SageMakerPipelineParametersOutputTypeDef",
    "SageMakerPipelineParametersTypeDef",
    "ScheduleSummaryTypeDef",
    "EcsParametersOutputTypeDef",
    "NetworkConfigurationTypeDef",
    "SageMakerPipelineParametersUnionTypeDef",
    "ListSchedulesOutputTypeDef",
    "TargetOutputTypeDef",
    "NetworkConfigurationUnionTypeDef",
    "GetScheduleOutputTypeDef",
    "EcsParametersTypeDef",
    "EcsParametersUnionTypeDef",
    "TargetTypeDef",
    "CreateScheduleInputRequestTypeDef",
    "UpdateScheduleInputRequestTypeDef",
)

AwsVpcConfigurationOutputTypeDef = TypedDict(
    "AwsVpcConfigurationOutputTypeDef",
    {
        "Subnets": List[str],
        "AssignPublicIp": NotRequired[AssignPublicIpType],
        "SecurityGroups": NotRequired[List[str]],
    },
)
AwsVpcConfigurationTypeDef = TypedDict(
    "AwsVpcConfigurationTypeDef",
    {
        "Subnets": Sequence[str],
        "AssignPublicIp": NotRequired[AssignPublicIpType],
        "SecurityGroups": NotRequired[Sequence[str]],
    },
)
CapacityProviderStrategyItemTypeDef = TypedDict(
    "CapacityProviderStrategyItemTypeDef",
    {
        "capacityProvider": str,
        "base": NotRequired[int],
        "weight": NotRequired[int],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
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
FlexibleTimeWindowTypeDef = TypedDict(
    "FlexibleTimeWindowTypeDef",
    {
        "Mode": FlexibleTimeWindowModeType,
        "MaximumWindowInMinutes": NotRequired[int],
    },
)
TimestampTypeDef = Union[datetime, str]
DeadLetterConfigTypeDef = TypedDict(
    "DeadLetterConfigTypeDef",
    {
        "Arn": NotRequired[str],
    },
)
DeleteScheduleGroupInputRequestTypeDef = TypedDict(
    "DeleteScheduleGroupInputRequestTypeDef",
    {
        "Name": str,
        "ClientToken": NotRequired[str],
    },
)
DeleteScheduleInputRequestTypeDef = TypedDict(
    "DeleteScheduleInputRequestTypeDef",
    {
        "Name": str,
        "ClientToken": NotRequired[str],
        "GroupName": NotRequired[str],
    },
)
PlacementConstraintTypeDef = TypedDict(
    "PlacementConstraintTypeDef",
    {
        "expression": NotRequired[str],
        "type": NotRequired[PlacementConstraintTypeType],
    },
)
PlacementStrategyTypeDef = TypedDict(
    "PlacementStrategyTypeDef",
    {
        "field": NotRequired[str],
        "type": NotRequired[PlacementStrategyTypeType],
    },
)
EventBridgeParametersTypeDef = TypedDict(
    "EventBridgeParametersTypeDef",
    {
        "DetailType": str,
        "Source": str,
    },
)
GetScheduleGroupInputRequestTypeDef = TypedDict(
    "GetScheduleGroupInputRequestTypeDef",
    {
        "Name": str,
    },
)
GetScheduleInputRequestTypeDef = TypedDict(
    "GetScheduleInputRequestTypeDef",
    {
        "Name": str,
        "GroupName": NotRequired[str],
    },
)
KinesisParametersTypeDef = TypedDict(
    "KinesisParametersTypeDef",
    {
        "PartitionKey": str,
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
ListScheduleGroupsInputRequestTypeDef = TypedDict(
    "ListScheduleGroupsInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NamePrefix": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
ScheduleGroupSummaryTypeDef = TypedDict(
    "ScheduleGroupSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "CreationDate": NotRequired[datetime],
        "LastModificationDate": NotRequired[datetime],
        "Name": NotRequired[str],
        "State": NotRequired[ScheduleGroupStateType],
    },
)
ListSchedulesInputRequestTypeDef = TypedDict(
    "ListSchedulesInputRequestTypeDef",
    {
        "GroupName": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NamePrefix": NotRequired[str],
        "NextToken": NotRequired[str],
        "State": NotRequired[ScheduleStateType],
    },
)
ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
RetryPolicyTypeDef = TypedDict(
    "RetryPolicyTypeDef",
    {
        "MaximumEventAgeInSeconds": NotRequired[int],
        "MaximumRetryAttempts": NotRequired[int],
    },
)
SageMakerPipelineParameterTypeDef = TypedDict(
    "SageMakerPipelineParameterTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)
TargetSummaryTypeDef = TypedDict(
    "TargetSummaryTypeDef",
    {
        "Arn": str,
    },
)
SqsParametersTypeDef = TypedDict(
    "SqsParametersTypeDef",
    {
        "MessageGroupId": NotRequired[str],
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
NetworkConfigurationOutputTypeDef = TypedDict(
    "NetworkConfigurationOutputTypeDef",
    {
        "awsvpcConfiguration": NotRequired[AwsVpcConfigurationOutputTypeDef],
    },
)
AwsVpcConfigurationUnionTypeDef = Union[
    AwsVpcConfigurationTypeDef, AwsVpcConfigurationOutputTypeDef
]
CreateScheduleGroupInputRequestTypeDef = TypedDict(
    "CreateScheduleGroupInputRequestTypeDef",
    {
        "Name": str,
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CreateScheduleGroupOutputTypeDef = TypedDict(
    "CreateScheduleGroupOutputTypeDef",
    {
        "ScheduleGroupArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateScheduleOutputTypeDef = TypedDict(
    "CreateScheduleOutputTypeDef",
    {
        "ScheduleArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetScheduleGroupOutputTypeDef = TypedDict(
    "GetScheduleGroupOutputTypeDef",
    {
        "Arn": str,
        "CreationDate": datetime,
        "LastModificationDate": datetime,
        "Name": str,
        "State": ScheduleGroupStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateScheduleOutputTypeDef = TypedDict(
    "UpdateScheduleOutputTypeDef",
    {
        "ScheduleArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListScheduleGroupsInputListScheduleGroupsPaginateTypeDef = TypedDict(
    "ListScheduleGroupsInputListScheduleGroupsPaginateTypeDef",
    {
        "NamePrefix": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSchedulesInputListSchedulesPaginateTypeDef = TypedDict(
    "ListSchedulesInputListSchedulesPaginateTypeDef",
    {
        "GroupName": NotRequired[str],
        "NamePrefix": NotRequired[str],
        "State": NotRequired[ScheduleStateType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListScheduleGroupsOutputTypeDef = TypedDict(
    "ListScheduleGroupsOutputTypeDef",
    {
        "ScheduleGroups": List[ScheduleGroupSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
SageMakerPipelineParametersOutputTypeDef = TypedDict(
    "SageMakerPipelineParametersOutputTypeDef",
    {
        "PipelineParameterList": NotRequired[List[SageMakerPipelineParameterTypeDef]],
    },
)
SageMakerPipelineParametersTypeDef = TypedDict(
    "SageMakerPipelineParametersTypeDef",
    {
        "PipelineParameterList": NotRequired[Sequence[SageMakerPipelineParameterTypeDef]],
    },
)
ScheduleSummaryTypeDef = TypedDict(
    "ScheduleSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "CreationDate": NotRequired[datetime],
        "GroupName": NotRequired[str],
        "LastModificationDate": NotRequired[datetime],
        "Name": NotRequired[str],
        "State": NotRequired[ScheduleStateType],
        "Target": NotRequired[TargetSummaryTypeDef],
    },
)
EcsParametersOutputTypeDef = TypedDict(
    "EcsParametersOutputTypeDef",
    {
        "TaskDefinitionArn": str,
        "CapacityProviderStrategy": NotRequired[List[CapacityProviderStrategyItemTypeDef]],
        "EnableECSManagedTags": NotRequired[bool],
        "EnableExecuteCommand": NotRequired[bool],
        "Group": NotRequired[str],
        "LaunchType": NotRequired[LaunchTypeType],
        "NetworkConfiguration": NotRequired[NetworkConfigurationOutputTypeDef],
        "PlacementConstraints": NotRequired[List[PlacementConstraintTypeDef]],
        "PlacementStrategy": NotRequired[List[PlacementStrategyTypeDef]],
        "PlatformVersion": NotRequired[str],
        "PropagateTags": NotRequired[Literal["TASK_DEFINITION"]],
        "ReferenceId": NotRequired[str],
        "Tags": NotRequired[List[Dict[str, str]]],
        "TaskCount": NotRequired[int],
    },
)
NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": NotRequired[AwsVpcConfigurationUnionTypeDef],
    },
)
SageMakerPipelineParametersUnionTypeDef = Union[
    SageMakerPipelineParametersTypeDef, SageMakerPipelineParametersOutputTypeDef
]
ListSchedulesOutputTypeDef = TypedDict(
    "ListSchedulesOutputTypeDef",
    {
        "Schedules": List[ScheduleSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
TargetOutputTypeDef = TypedDict(
    "TargetOutputTypeDef",
    {
        "Arn": str,
        "RoleArn": str,
        "DeadLetterConfig": NotRequired[DeadLetterConfigTypeDef],
        "EcsParameters": NotRequired[EcsParametersOutputTypeDef],
        "EventBridgeParameters": NotRequired[EventBridgeParametersTypeDef],
        "Input": NotRequired[str],
        "KinesisParameters": NotRequired[KinesisParametersTypeDef],
        "RetryPolicy": NotRequired[RetryPolicyTypeDef],
        "SageMakerPipelineParameters": NotRequired[SageMakerPipelineParametersOutputTypeDef],
        "SqsParameters": NotRequired[SqsParametersTypeDef],
    },
)
NetworkConfigurationUnionTypeDef = Union[
    NetworkConfigurationTypeDef, NetworkConfigurationOutputTypeDef
]
GetScheduleOutputTypeDef = TypedDict(
    "GetScheduleOutputTypeDef",
    {
        "ActionAfterCompletion": ActionAfterCompletionType,
        "Arn": str,
        "CreationDate": datetime,
        "Description": str,
        "EndDate": datetime,
        "FlexibleTimeWindow": FlexibleTimeWindowTypeDef,
        "GroupName": str,
        "KmsKeyArn": str,
        "LastModificationDate": datetime,
        "Name": str,
        "ScheduleExpression": str,
        "ScheduleExpressionTimezone": str,
        "StartDate": datetime,
        "State": ScheduleStateType,
        "Target": TargetOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EcsParametersTypeDef = TypedDict(
    "EcsParametersTypeDef",
    {
        "TaskDefinitionArn": str,
        "CapacityProviderStrategy": NotRequired[Sequence[CapacityProviderStrategyItemTypeDef]],
        "EnableECSManagedTags": NotRequired[bool],
        "EnableExecuteCommand": NotRequired[bool],
        "Group": NotRequired[str],
        "LaunchType": NotRequired[LaunchTypeType],
        "NetworkConfiguration": NotRequired[NetworkConfigurationUnionTypeDef],
        "PlacementConstraints": NotRequired[Sequence[PlacementConstraintTypeDef]],
        "PlacementStrategy": NotRequired[Sequence[PlacementStrategyTypeDef]],
        "PlatformVersion": NotRequired[str],
        "PropagateTags": NotRequired[Literal["TASK_DEFINITION"]],
        "ReferenceId": NotRequired[str],
        "Tags": NotRequired[Sequence[Mapping[str, str]]],
        "TaskCount": NotRequired[int],
    },
)
EcsParametersUnionTypeDef = Union[EcsParametersTypeDef, EcsParametersOutputTypeDef]
TargetTypeDef = TypedDict(
    "TargetTypeDef",
    {
        "Arn": str,
        "RoleArn": str,
        "DeadLetterConfig": NotRequired[DeadLetterConfigTypeDef],
        "EcsParameters": NotRequired[EcsParametersUnionTypeDef],
        "EventBridgeParameters": NotRequired[EventBridgeParametersTypeDef],
        "Input": NotRequired[str],
        "KinesisParameters": NotRequired[KinesisParametersTypeDef],
        "RetryPolicy": NotRequired[RetryPolicyTypeDef],
        "SageMakerPipelineParameters": NotRequired[SageMakerPipelineParametersUnionTypeDef],
        "SqsParameters": NotRequired[SqsParametersTypeDef],
    },
)
CreateScheduleInputRequestTypeDef = TypedDict(
    "CreateScheduleInputRequestTypeDef",
    {
        "FlexibleTimeWindow": FlexibleTimeWindowTypeDef,
        "Name": str,
        "ScheduleExpression": str,
        "Target": TargetTypeDef,
        "ActionAfterCompletion": NotRequired[ActionAfterCompletionType],
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
        "EndDate": NotRequired[TimestampTypeDef],
        "GroupName": NotRequired[str],
        "KmsKeyArn": NotRequired[str],
        "ScheduleExpressionTimezone": NotRequired[str],
        "StartDate": NotRequired[TimestampTypeDef],
        "State": NotRequired[ScheduleStateType],
    },
)
UpdateScheduleInputRequestTypeDef = TypedDict(
    "UpdateScheduleInputRequestTypeDef",
    {
        "FlexibleTimeWindow": FlexibleTimeWindowTypeDef,
        "Name": str,
        "ScheduleExpression": str,
        "Target": TargetTypeDef,
        "ActionAfterCompletion": NotRequired[ActionAfterCompletionType],
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
        "EndDate": NotRequired[TimestampTypeDef],
        "GroupName": NotRequired[str],
        "KmsKeyArn": NotRequired[str],
        "ScheduleExpressionTimezone": NotRequired[str],
        "StartDate": NotRequired[TimestampTypeDef],
        "State": NotRequired[ScheduleStateType],
    },
)
