"""
Type annotations for swf service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_swf/type_defs/)

Usage::

    ```python
    from mypy_boto3_swf.type_defs import ActivityTaskCancelRequestedEventAttributesTypeDef

    data: ActivityTaskCancelRequestedEventAttributesTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    ActivityTaskTimeoutTypeType,
    CancelTimerFailedCauseType,
    CancelWorkflowExecutionFailedCauseType,
    ChildPolicyType,
    CloseStatusType,
    CompleteWorkflowExecutionFailedCauseType,
    ContinueAsNewWorkflowExecutionFailedCauseType,
    DecisionTaskTimeoutTypeType,
    DecisionTypeType,
    EventTypeType,
    ExecutionStatusType,
    FailWorkflowExecutionFailedCauseType,
    RegistrationStatusType,
    RequestCancelActivityTaskFailedCauseType,
    RequestCancelExternalWorkflowExecutionFailedCauseType,
    ScheduleActivityTaskFailedCauseType,
    ScheduleLambdaFunctionFailedCauseType,
    SignalExternalWorkflowExecutionFailedCauseType,
    StartChildWorkflowExecutionFailedCauseType,
    StartTimerFailedCauseType,
    WorkflowExecutionTerminatedCauseType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "ActivityTaskCancelRequestedEventAttributesTypeDef",
    "ActivityTaskCanceledEventAttributesTypeDef",
    "ActivityTaskCompletedEventAttributesTypeDef",
    "ActivityTaskFailedEventAttributesTypeDef",
    "ActivityTypeTypeDef",
    "TaskListTypeDef",
    "ActivityTaskStartedEventAttributesTypeDef",
    "ResponseMetadataTypeDef",
    "ActivityTaskTimedOutEventAttributesTypeDef",
    "WorkflowExecutionTypeDef",
    "CancelTimerDecisionAttributesTypeDef",
    "CancelTimerFailedEventAttributesTypeDef",
    "CancelWorkflowExecutionDecisionAttributesTypeDef",
    "CancelWorkflowExecutionFailedEventAttributesTypeDef",
    "WorkflowTypeTypeDef",
    "CloseStatusFilterTypeDef",
    "CompleteWorkflowExecutionDecisionAttributesTypeDef",
    "CompleteWorkflowExecutionFailedEventAttributesTypeDef",
    "ContinueAsNewWorkflowExecutionFailedEventAttributesTypeDef",
    "TagFilterTypeDef",
    "WorkflowExecutionFilterTypeDef",
    "WorkflowTypeFilterTypeDef",
    "DecisionTaskStartedEventAttributesTypeDef",
    "DecisionTaskTimedOutEventAttributesTypeDef",
    "FailWorkflowExecutionDecisionAttributesTypeDef",
    "RecordMarkerDecisionAttributesTypeDef",
    "RequestCancelActivityTaskDecisionAttributesTypeDef",
    "RequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef",
    "ScheduleLambdaFunctionDecisionAttributesTypeDef",
    "SignalExternalWorkflowExecutionDecisionAttributesTypeDef",
    "StartTimerDecisionAttributesTypeDef",
    "DeprecateDomainInputRequestTypeDef",
    "DescribeDomainInputRequestTypeDef",
    "DomainConfigurationTypeDef",
    "DomainInfoTypeDef",
    "TimestampTypeDef",
    "FailWorkflowExecutionFailedEventAttributesTypeDef",
    "PaginatorConfigTypeDef",
    "LambdaFunctionCompletedEventAttributesTypeDef",
    "LambdaFunctionFailedEventAttributesTypeDef",
    "LambdaFunctionScheduledEventAttributesTypeDef",
    "LambdaFunctionStartedEventAttributesTypeDef",
    "LambdaFunctionTimedOutEventAttributesTypeDef",
    "MarkerRecordedEventAttributesTypeDef",
    "RecordMarkerFailedEventAttributesTypeDef",
    "RequestCancelActivityTaskFailedEventAttributesTypeDef",
    "RequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef",
    "RequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    "ScheduleLambdaFunctionFailedEventAttributesTypeDef",
    "SignalExternalWorkflowExecutionFailedEventAttributesTypeDef",
    "SignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    "StartLambdaFunctionFailedEventAttributesTypeDef",
    "StartTimerFailedEventAttributesTypeDef",
    "TimerCanceledEventAttributesTypeDef",
    "TimerFiredEventAttributesTypeDef",
    "TimerStartedEventAttributesTypeDef",
    "WorkflowExecutionCanceledEventAttributesTypeDef",
    "WorkflowExecutionCompletedEventAttributesTypeDef",
    "WorkflowExecutionFailedEventAttributesTypeDef",
    "WorkflowExecutionTerminatedEventAttributesTypeDef",
    "WorkflowExecutionTimedOutEventAttributesTypeDef",
    "ListActivityTypesInputRequestTypeDef",
    "ListDomainsInputRequestTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ResourceTagTypeDef",
    "ListWorkflowTypesInputRequestTypeDef",
    "RecordActivityTaskHeartbeatInputRequestTypeDef",
    "RequestCancelWorkflowExecutionInputRequestTypeDef",
    "RespondActivityTaskCanceledInputRequestTypeDef",
    "RespondActivityTaskCompletedInputRequestTypeDef",
    "RespondActivityTaskFailedInputRequestTypeDef",
    "SignalWorkflowExecutionInputRequestTypeDef",
    "TerminateWorkflowExecutionInputRequestTypeDef",
    "UndeprecateDomainInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "WorkflowExecutionOpenCountsTypeDef",
    "ActivityTypeInfoTypeDef",
    "DeleteActivityTypeInputRequestTypeDef",
    "DeprecateActivityTypeInputRequestTypeDef",
    "DescribeActivityTypeInputRequestTypeDef",
    "ScheduleActivityTaskFailedEventAttributesTypeDef",
    "UndeprecateActivityTypeInputRequestTypeDef",
    "ActivityTaskScheduledEventAttributesTypeDef",
    "ActivityTypeConfigurationTypeDef",
    "ContinueAsNewWorkflowExecutionDecisionAttributesTypeDef",
    "CountPendingActivityTasksInputRequestTypeDef",
    "CountPendingDecisionTasksInputRequestTypeDef",
    "DecisionTaskCompletedEventAttributesTypeDef",
    "DecisionTaskScheduledEventAttributesTypeDef",
    "PollForActivityTaskInputRequestTypeDef",
    "PollForDecisionTaskInputRequestTypeDef",
    "RegisterActivityTypeInputRequestTypeDef",
    "RegisterWorkflowTypeInputRequestTypeDef",
    "ScheduleActivityTaskDecisionAttributesTypeDef",
    "WorkflowExecutionConfigurationTypeDef",
    "WorkflowTypeConfigurationTypeDef",
    "ActivityTaskStatusTypeDef",
    "EmptyResponseMetadataTypeDef",
    "PendingTaskCountTypeDef",
    "RunTypeDef",
    "WorkflowExecutionCountTypeDef",
    "ActivityTaskTypeDef",
    "DescribeWorkflowExecutionInputRequestTypeDef",
    "ExternalWorkflowExecutionCancelRequestedEventAttributesTypeDef",
    "ExternalWorkflowExecutionSignaledEventAttributesTypeDef",
    "GetWorkflowExecutionHistoryInputRequestTypeDef",
    "WorkflowExecutionCancelRequestedEventAttributesTypeDef",
    "WorkflowExecutionSignaledEventAttributesTypeDef",
    "ChildWorkflowExecutionCanceledEventAttributesTypeDef",
    "ChildWorkflowExecutionCompletedEventAttributesTypeDef",
    "ChildWorkflowExecutionFailedEventAttributesTypeDef",
    "ChildWorkflowExecutionStartedEventAttributesTypeDef",
    "ChildWorkflowExecutionTerminatedEventAttributesTypeDef",
    "ChildWorkflowExecutionTimedOutEventAttributesTypeDef",
    "DeleteWorkflowTypeInputRequestTypeDef",
    "DeprecateWorkflowTypeInputRequestTypeDef",
    "DescribeWorkflowTypeInputRequestTypeDef",
    "StartChildWorkflowExecutionDecisionAttributesTypeDef",
    "StartChildWorkflowExecutionFailedEventAttributesTypeDef",
    "StartChildWorkflowExecutionInitiatedEventAttributesTypeDef",
    "StartWorkflowExecutionInputRequestTypeDef",
    "UndeprecateWorkflowTypeInputRequestTypeDef",
    "WorkflowExecutionContinuedAsNewEventAttributesTypeDef",
    "WorkflowExecutionInfoTypeDef",
    "WorkflowExecutionStartedEventAttributesTypeDef",
    "WorkflowTypeInfoTypeDef",
    "DomainDetailTypeDef",
    "DomainInfosTypeDef",
    "ExecutionTimeFilterTypeDef",
    "GetWorkflowExecutionHistoryInputGetWorkflowExecutionHistoryPaginateTypeDef",
    "ListActivityTypesInputListActivityTypesPaginateTypeDef",
    "ListDomainsInputListDomainsPaginateTypeDef",
    "ListWorkflowTypesInputListWorkflowTypesPaginateTypeDef",
    "PollForDecisionTaskInputPollForDecisionTaskPaginateTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "RegisterDomainInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "ActivityTypeInfosTypeDef",
    "ActivityTypeDetailTypeDef",
    "DecisionTypeDef",
    "WorkflowExecutionDetailTypeDef",
    "WorkflowExecutionInfosTypeDef",
    "HistoryEventTypeDef",
    "WorkflowTypeDetailTypeDef",
    "WorkflowTypeInfosTypeDef",
    "CountClosedWorkflowExecutionsInputRequestTypeDef",
    "CountOpenWorkflowExecutionsInputRequestTypeDef",
    "ListClosedWorkflowExecutionsInputListClosedWorkflowExecutionsPaginateTypeDef",
    "ListClosedWorkflowExecutionsInputRequestTypeDef",
    "ListOpenWorkflowExecutionsInputListOpenWorkflowExecutionsPaginateTypeDef",
    "ListOpenWorkflowExecutionsInputRequestTypeDef",
    "RespondDecisionTaskCompletedInputRequestTypeDef",
    "DecisionTaskTypeDef",
    "HistoryTypeDef",
)

ActivityTaskCancelRequestedEventAttributesTypeDef = TypedDict(
    "ActivityTaskCancelRequestedEventAttributesTypeDef",
    {
        "decisionTaskCompletedEventId": int,
        "activityId": str,
    },
)
ActivityTaskCanceledEventAttributesTypeDef = TypedDict(
    "ActivityTaskCanceledEventAttributesTypeDef",
    {
        "scheduledEventId": int,
        "startedEventId": int,
        "details": NotRequired[str],
        "latestCancelRequestedEventId": NotRequired[int],
    },
)
ActivityTaskCompletedEventAttributesTypeDef = TypedDict(
    "ActivityTaskCompletedEventAttributesTypeDef",
    {
        "scheduledEventId": int,
        "startedEventId": int,
        "result": NotRequired[str],
    },
)
ActivityTaskFailedEventAttributesTypeDef = TypedDict(
    "ActivityTaskFailedEventAttributesTypeDef",
    {
        "scheduledEventId": int,
        "startedEventId": int,
        "reason": NotRequired[str],
        "details": NotRequired[str],
    },
)
ActivityTypeTypeDef = TypedDict(
    "ActivityTypeTypeDef",
    {
        "name": str,
        "version": str,
    },
)
TaskListTypeDef = TypedDict(
    "TaskListTypeDef",
    {
        "name": str,
    },
)
ActivityTaskStartedEventAttributesTypeDef = TypedDict(
    "ActivityTaskStartedEventAttributesTypeDef",
    {
        "scheduledEventId": int,
        "identity": NotRequired[str],
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
ActivityTaskTimedOutEventAttributesTypeDef = TypedDict(
    "ActivityTaskTimedOutEventAttributesTypeDef",
    {
        "timeoutType": ActivityTaskTimeoutTypeType,
        "scheduledEventId": int,
        "startedEventId": int,
        "details": NotRequired[str],
    },
)
WorkflowExecutionTypeDef = TypedDict(
    "WorkflowExecutionTypeDef",
    {
        "workflowId": str,
        "runId": str,
    },
)
CancelTimerDecisionAttributesTypeDef = TypedDict(
    "CancelTimerDecisionAttributesTypeDef",
    {
        "timerId": str,
    },
)
CancelTimerFailedEventAttributesTypeDef = TypedDict(
    "CancelTimerFailedEventAttributesTypeDef",
    {
        "timerId": str,
        "cause": CancelTimerFailedCauseType,
        "decisionTaskCompletedEventId": int,
    },
)
CancelWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "CancelWorkflowExecutionDecisionAttributesTypeDef",
    {
        "details": NotRequired[str],
    },
)
CancelWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "CancelWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": CancelWorkflowExecutionFailedCauseType,
        "decisionTaskCompletedEventId": int,
    },
)
WorkflowTypeTypeDef = TypedDict(
    "WorkflowTypeTypeDef",
    {
        "name": str,
        "version": str,
    },
)
CloseStatusFilterTypeDef = TypedDict(
    "CloseStatusFilterTypeDef",
    {
        "status": CloseStatusType,
    },
)
CompleteWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "CompleteWorkflowExecutionDecisionAttributesTypeDef",
    {
        "result": NotRequired[str],
    },
)
CompleteWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "CompleteWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": CompleteWorkflowExecutionFailedCauseType,
        "decisionTaskCompletedEventId": int,
    },
)
ContinueAsNewWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ContinueAsNewWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": ContinueAsNewWorkflowExecutionFailedCauseType,
        "decisionTaskCompletedEventId": int,
    },
)
TagFilterTypeDef = TypedDict(
    "TagFilterTypeDef",
    {
        "tag": str,
    },
)
WorkflowExecutionFilterTypeDef = TypedDict(
    "WorkflowExecutionFilterTypeDef",
    {
        "workflowId": str,
    },
)
WorkflowTypeFilterTypeDef = TypedDict(
    "WorkflowTypeFilterTypeDef",
    {
        "name": str,
        "version": NotRequired[str],
    },
)
DecisionTaskStartedEventAttributesTypeDef = TypedDict(
    "DecisionTaskStartedEventAttributesTypeDef",
    {
        "scheduledEventId": int,
        "identity": NotRequired[str],
    },
)
DecisionTaskTimedOutEventAttributesTypeDef = TypedDict(
    "DecisionTaskTimedOutEventAttributesTypeDef",
    {
        "timeoutType": DecisionTaskTimeoutTypeType,
        "scheduledEventId": int,
        "startedEventId": int,
    },
)
FailWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "FailWorkflowExecutionDecisionAttributesTypeDef",
    {
        "reason": NotRequired[str],
        "details": NotRequired[str],
    },
)
RecordMarkerDecisionAttributesTypeDef = TypedDict(
    "RecordMarkerDecisionAttributesTypeDef",
    {
        "markerName": str,
        "details": NotRequired[str],
    },
)
RequestCancelActivityTaskDecisionAttributesTypeDef = TypedDict(
    "RequestCancelActivityTaskDecisionAttributesTypeDef",
    {
        "activityId": str,
    },
)
RequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "RequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef",
    {
        "workflowId": str,
        "runId": NotRequired[str],
        "control": NotRequired[str],
    },
)
ScheduleLambdaFunctionDecisionAttributesTypeDef = TypedDict(
    "ScheduleLambdaFunctionDecisionAttributesTypeDef",
    {
        "id": str,
        "name": str,
        "control": NotRequired[str],
        "input": NotRequired[str],
        "startToCloseTimeout": NotRequired[str],
    },
)
SignalExternalWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "SignalExternalWorkflowExecutionDecisionAttributesTypeDef",
    {
        "workflowId": str,
        "signalName": str,
        "runId": NotRequired[str],
        "input": NotRequired[str],
        "control": NotRequired[str],
    },
)
StartTimerDecisionAttributesTypeDef = TypedDict(
    "StartTimerDecisionAttributesTypeDef",
    {
        "timerId": str,
        "startToFireTimeout": str,
        "control": NotRequired[str],
    },
)
DeprecateDomainInputRequestTypeDef = TypedDict(
    "DeprecateDomainInputRequestTypeDef",
    {
        "name": str,
    },
)
DescribeDomainInputRequestTypeDef = TypedDict(
    "DescribeDomainInputRequestTypeDef",
    {
        "name": str,
    },
)
DomainConfigurationTypeDef = TypedDict(
    "DomainConfigurationTypeDef",
    {
        "workflowExecutionRetentionPeriodInDays": str,
    },
)
DomainInfoTypeDef = TypedDict(
    "DomainInfoTypeDef",
    {
        "name": str,
        "status": RegistrationStatusType,
        "description": NotRequired[str],
        "arn": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
FailWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "FailWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "cause": FailWorkflowExecutionFailedCauseType,
        "decisionTaskCompletedEventId": int,
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
LambdaFunctionCompletedEventAttributesTypeDef = TypedDict(
    "LambdaFunctionCompletedEventAttributesTypeDef",
    {
        "scheduledEventId": int,
        "startedEventId": int,
        "result": NotRequired[str],
    },
)
LambdaFunctionFailedEventAttributesTypeDef = TypedDict(
    "LambdaFunctionFailedEventAttributesTypeDef",
    {
        "scheduledEventId": int,
        "startedEventId": int,
        "reason": NotRequired[str],
        "details": NotRequired[str],
    },
)
LambdaFunctionScheduledEventAttributesTypeDef = TypedDict(
    "LambdaFunctionScheduledEventAttributesTypeDef",
    {
        "id": str,
        "name": str,
        "decisionTaskCompletedEventId": int,
        "control": NotRequired[str],
        "input": NotRequired[str],
        "startToCloseTimeout": NotRequired[str],
    },
)
LambdaFunctionStartedEventAttributesTypeDef = TypedDict(
    "LambdaFunctionStartedEventAttributesTypeDef",
    {
        "scheduledEventId": int,
    },
)
LambdaFunctionTimedOutEventAttributesTypeDef = TypedDict(
    "LambdaFunctionTimedOutEventAttributesTypeDef",
    {
        "scheduledEventId": int,
        "startedEventId": int,
        "timeoutType": NotRequired[Literal["START_TO_CLOSE"]],
    },
)
MarkerRecordedEventAttributesTypeDef = TypedDict(
    "MarkerRecordedEventAttributesTypeDef",
    {
        "markerName": str,
        "decisionTaskCompletedEventId": int,
        "details": NotRequired[str],
    },
)
RecordMarkerFailedEventAttributesTypeDef = TypedDict(
    "RecordMarkerFailedEventAttributesTypeDef",
    {
        "markerName": str,
        "cause": Literal["OPERATION_NOT_PERMITTED"],
        "decisionTaskCompletedEventId": int,
    },
)
RequestCancelActivityTaskFailedEventAttributesTypeDef = TypedDict(
    "RequestCancelActivityTaskFailedEventAttributesTypeDef",
    {
        "activityId": str,
        "cause": RequestCancelActivityTaskFailedCauseType,
        "decisionTaskCompletedEventId": int,
    },
)
RequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "RequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowId": str,
        "cause": RequestCancelExternalWorkflowExecutionFailedCauseType,
        "initiatedEventId": int,
        "decisionTaskCompletedEventId": int,
        "runId": NotRequired[str],
        "control": NotRequired[str],
    },
)
RequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "RequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    {
        "workflowId": str,
        "decisionTaskCompletedEventId": int,
        "runId": NotRequired[str],
        "control": NotRequired[str],
    },
)
ScheduleLambdaFunctionFailedEventAttributesTypeDef = TypedDict(
    "ScheduleLambdaFunctionFailedEventAttributesTypeDef",
    {
        "id": str,
        "name": str,
        "cause": ScheduleLambdaFunctionFailedCauseType,
        "decisionTaskCompletedEventId": int,
    },
)
SignalExternalWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "SignalExternalWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowId": str,
        "cause": SignalExternalWorkflowExecutionFailedCauseType,
        "initiatedEventId": int,
        "decisionTaskCompletedEventId": int,
        "runId": NotRequired[str],
        "control": NotRequired[str],
    },
)
SignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "SignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    {
        "workflowId": str,
        "signalName": str,
        "decisionTaskCompletedEventId": int,
        "runId": NotRequired[str],
        "input": NotRequired[str],
        "control": NotRequired[str],
    },
)
StartLambdaFunctionFailedEventAttributesTypeDef = TypedDict(
    "StartLambdaFunctionFailedEventAttributesTypeDef",
    {
        "scheduledEventId": NotRequired[int],
        "cause": NotRequired[Literal["ASSUME_ROLE_FAILED"]],
        "message": NotRequired[str],
    },
)
StartTimerFailedEventAttributesTypeDef = TypedDict(
    "StartTimerFailedEventAttributesTypeDef",
    {
        "timerId": str,
        "cause": StartTimerFailedCauseType,
        "decisionTaskCompletedEventId": int,
    },
)
TimerCanceledEventAttributesTypeDef = TypedDict(
    "TimerCanceledEventAttributesTypeDef",
    {
        "timerId": str,
        "startedEventId": int,
        "decisionTaskCompletedEventId": int,
    },
)
TimerFiredEventAttributesTypeDef = TypedDict(
    "TimerFiredEventAttributesTypeDef",
    {
        "timerId": str,
        "startedEventId": int,
    },
)
TimerStartedEventAttributesTypeDef = TypedDict(
    "TimerStartedEventAttributesTypeDef",
    {
        "timerId": str,
        "startToFireTimeout": str,
        "decisionTaskCompletedEventId": int,
        "control": NotRequired[str],
    },
)
WorkflowExecutionCanceledEventAttributesTypeDef = TypedDict(
    "WorkflowExecutionCanceledEventAttributesTypeDef",
    {
        "decisionTaskCompletedEventId": int,
        "details": NotRequired[str],
    },
)
WorkflowExecutionCompletedEventAttributesTypeDef = TypedDict(
    "WorkflowExecutionCompletedEventAttributesTypeDef",
    {
        "decisionTaskCompletedEventId": int,
        "result": NotRequired[str],
    },
)
WorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "WorkflowExecutionFailedEventAttributesTypeDef",
    {
        "decisionTaskCompletedEventId": int,
        "reason": NotRequired[str],
        "details": NotRequired[str],
    },
)
WorkflowExecutionTerminatedEventAttributesTypeDef = TypedDict(
    "WorkflowExecutionTerminatedEventAttributesTypeDef",
    {
        "childPolicy": ChildPolicyType,
        "reason": NotRequired[str],
        "details": NotRequired[str],
        "cause": NotRequired[WorkflowExecutionTerminatedCauseType],
    },
)
WorkflowExecutionTimedOutEventAttributesTypeDef = TypedDict(
    "WorkflowExecutionTimedOutEventAttributesTypeDef",
    {
        "timeoutType": Literal["START_TO_CLOSE"],
        "childPolicy": ChildPolicyType,
    },
)
ListActivityTypesInputRequestTypeDef = TypedDict(
    "ListActivityTypesInputRequestTypeDef",
    {
        "domain": str,
        "registrationStatus": RegistrationStatusType,
        "name": NotRequired[str],
        "nextPageToken": NotRequired[str],
        "maximumPageSize": NotRequired[int],
        "reverseOrder": NotRequired[bool],
    },
)
ListDomainsInputRequestTypeDef = TypedDict(
    "ListDomainsInputRequestTypeDef",
    {
        "registrationStatus": RegistrationStatusType,
        "nextPageToken": NotRequired[str],
        "maximumPageSize": NotRequired[int],
        "reverseOrder": NotRequired[bool],
    },
)
ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)
ResourceTagTypeDef = TypedDict(
    "ResourceTagTypeDef",
    {
        "key": str,
        "value": NotRequired[str],
    },
)
ListWorkflowTypesInputRequestTypeDef = TypedDict(
    "ListWorkflowTypesInputRequestTypeDef",
    {
        "domain": str,
        "registrationStatus": RegistrationStatusType,
        "name": NotRequired[str],
        "nextPageToken": NotRequired[str],
        "maximumPageSize": NotRequired[int],
        "reverseOrder": NotRequired[bool],
    },
)
RecordActivityTaskHeartbeatInputRequestTypeDef = TypedDict(
    "RecordActivityTaskHeartbeatInputRequestTypeDef",
    {
        "taskToken": str,
        "details": NotRequired[str],
    },
)
RequestCancelWorkflowExecutionInputRequestTypeDef = TypedDict(
    "RequestCancelWorkflowExecutionInputRequestTypeDef",
    {
        "domain": str,
        "workflowId": str,
        "runId": NotRequired[str],
    },
)
RespondActivityTaskCanceledInputRequestTypeDef = TypedDict(
    "RespondActivityTaskCanceledInputRequestTypeDef",
    {
        "taskToken": str,
        "details": NotRequired[str],
    },
)
RespondActivityTaskCompletedInputRequestTypeDef = TypedDict(
    "RespondActivityTaskCompletedInputRequestTypeDef",
    {
        "taskToken": str,
        "result": NotRequired[str],
    },
)
RespondActivityTaskFailedInputRequestTypeDef = TypedDict(
    "RespondActivityTaskFailedInputRequestTypeDef",
    {
        "taskToken": str,
        "reason": NotRequired[str],
        "details": NotRequired[str],
    },
)
SignalWorkflowExecutionInputRequestTypeDef = TypedDict(
    "SignalWorkflowExecutionInputRequestTypeDef",
    {
        "domain": str,
        "workflowId": str,
        "signalName": str,
        "runId": NotRequired[str],
        "input": NotRequired[str],
    },
)
TerminateWorkflowExecutionInputRequestTypeDef = TypedDict(
    "TerminateWorkflowExecutionInputRequestTypeDef",
    {
        "domain": str,
        "workflowId": str,
        "runId": NotRequired[str],
        "reason": NotRequired[str],
        "details": NotRequired[str],
        "childPolicy": NotRequired[ChildPolicyType],
    },
)
UndeprecateDomainInputRequestTypeDef = TypedDict(
    "UndeprecateDomainInputRequestTypeDef",
    {
        "name": str,
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
WorkflowExecutionOpenCountsTypeDef = TypedDict(
    "WorkflowExecutionOpenCountsTypeDef",
    {
        "openActivityTasks": int,
        "openDecisionTasks": int,
        "openTimers": int,
        "openChildWorkflowExecutions": int,
        "openLambdaFunctions": NotRequired[int],
    },
)
ActivityTypeInfoTypeDef = TypedDict(
    "ActivityTypeInfoTypeDef",
    {
        "activityType": ActivityTypeTypeDef,
        "status": RegistrationStatusType,
        "creationDate": datetime,
        "description": NotRequired[str],
        "deprecationDate": NotRequired[datetime],
    },
)
DeleteActivityTypeInputRequestTypeDef = TypedDict(
    "DeleteActivityTypeInputRequestTypeDef",
    {
        "domain": str,
        "activityType": ActivityTypeTypeDef,
    },
)
DeprecateActivityTypeInputRequestTypeDef = TypedDict(
    "DeprecateActivityTypeInputRequestTypeDef",
    {
        "domain": str,
        "activityType": ActivityTypeTypeDef,
    },
)
DescribeActivityTypeInputRequestTypeDef = TypedDict(
    "DescribeActivityTypeInputRequestTypeDef",
    {
        "domain": str,
        "activityType": ActivityTypeTypeDef,
    },
)
ScheduleActivityTaskFailedEventAttributesTypeDef = TypedDict(
    "ScheduleActivityTaskFailedEventAttributesTypeDef",
    {
        "activityType": ActivityTypeTypeDef,
        "activityId": str,
        "cause": ScheduleActivityTaskFailedCauseType,
        "decisionTaskCompletedEventId": int,
    },
)
UndeprecateActivityTypeInputRequestTypeDef = TypedDict(
    "UndeprecateActivityTypeInputRequestTypeDef",
    {
        "domain": str,
        "activityType": ActivityTypeTypeDef,
    },
)
ActivityTaskScheduledEventAttributesTypeDef = TypedDict(
    "ActivityTaskScheduledEventAttributesTypeDef",
    {
        "activityType": ActivityTypeTypeDef,
        "activityId": str,
        "taskList": TaskListTypeDef,
        "decisionTaskCompletedEventId": int,
        "input": NotRequired[str],
        "control": NotRequired[str],
        "scheduleToStartTimeout": NotRequired[str],
        "scheduleToCloseTimeout": NotRequired[str],
        "startToCloseTimeout": NotRequired[str],
        "taskPriority": NotRequired[str],
        "heartbeatTimeout": NotRequired[str],
    },
)
ActivityTypeConfigurationTypeDef = TypedDict(
    "ActivityTypeConfigurationTypeDef",
    {
        "defaultTaskStartToCloseTimeout": NotRequired[str],
        "defaultTaskHeartbeatTimeout": NotRequired[str],
        "defaultTaskList": NotRequired[TaskListTypeDef],
        "defaultTaskPriority": NotRequired[str],
        "defaultTaskScheduleToStartTimeout": NotRequired[str],
        "defaultTaskScheduleToCloseTimeout": NotRequired[str],
    },
)
ContinueAsNewWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "ContinueAsNewWorkflowExecutionDecisionAttributesTypeDef",
    {
        "input": NotRequired[str],
        "executionStartToCloseTimeout": NotRequired[str],
        "taskList": NotRequired[TaskListTypeDef],
        "taskPriority": NotRequired[str],
        "taskStartToCloseTimeout": NotRequired[str],
        "childPolicy": NotRequired[ChildPolicyType],
        "tagList": NotRequired[Sequence[str]],
        "workflowTypeVersion": NotRequired[str],
        "lambdaRole": NotRequired[str],
    },
)
CountPendingActivityTasksInputRequestTypeDef = TypedDict(
    "CountPendingActivityTasksInputRequestTypeDef",
    {
        "domain": str,
        "taskList": TaskListTypeDef,
    },
)
CountPendingDecisionTasksInputRequestTypeDef = TypedDict(
    "CountPendingDecisionTasksInputRequestTypeDef",
    {
        "domain": str,
        "taskList": TaskListTypeDef,
    },
)
DecisionTaskCompletedEventAttributesTypeDef = TypedDict(
    "DecisionTaskCompletedEventAttributesTypeDef",
    {
        "scheduledEventId": int,
        "startedEventId": int,
        "executionContext": NotRequired[str],
        "taskList": NotRequired[TaskListTypeDef],
        "taskListScheduleToStartTimeout": NotRequired[str],
    },
)
DecisionTaskScheduledEventAttributesTypeDef = TypedDict(
    "DecisionTaskScheduledEventAttributesTypeDef",
    {
        "taskList": TaskListTypeDef,
        "taskPriority": NotRequired[str],
        "startToCloseTimeout": NotRequired[str],
        "scheduleToStartTimeout": NotRequired[str],
    },
)
PollForActivityTaskInputRequestTypeDef = TypedDict(
    "PollForActivityTaskInputRequestTypeDef",
    {
        "domain": str,
        "taskList": TaskListTypeDef,
        "identity": NotRequired[str],
    },
)
PollForDecisionTaskInputRequestTypeDef = TypedDict(
    "PollForDecisionTaskInputRequestTypeDef",
    {
        "domain": str,
        "taskList": TaskListTypeDef,
        "identity": NotRequired[str],
        "nextPageToken": NotRequired[str],
        "maximumPageSize": NotRequired[int],
        "reverseOrder": NotRequired[bool],
        "startAtPreviousStartedEvent": NotRequired[bool],
    },
)
RegisterActivityTypeInputRequestTypeDef = TypedDict(
    "RegisterActivityTypeInputRequestTypeDef",
    {
        "domain": str,
        "name": str,
        "version": str,
        "description": NotRequired[str],
        "defaultTaskStartToCloseTimeout": NotRequired[str],
        "defaultTaskHeartbeatTimeout": NotRequired[str],
        "defaultTaskList": NotRequired[TaskListTypeDef],
        "defaultTaskPriority": NotRequired[str],
        "defaultTaskScheduleToStartTimeout": NotRequired[str],
        "defaultTaskScheduleToCloseTimeout": NotRequired[str],
    },
)
RegisterWorkflowTypeInputRequestTypeDef = TypedDict(
    "RegisterWorkflowTypeInputRequestTypeDef",
    {
        "domain": str,
        "name": str,
        "version": str,
        "description": NotRequired[str],
        "defaultTaskStartToCloseTimeout": NotRequired[str],
        "defaultExecutionStartToCloseTimeout": NotRequired[str],
        "defaultTaskList": NotRequired[TaskListTypeDef],
        "defaultTaskPriority": NotRequired[str],
        "defaultChildPolicy": NotRequired[ChildPolicyType],
        "defaultLambdaRole": NotRequired[str],
    },
)
ScheduleActivityTaskDecisionAttributesTypeDef = TypedDict(
    "ScheduleActivityTaskDecisionAttributesTypeDef",
    {
        "activityType": ActivityTypeTypeDef,
        "activityId": str,
        "control": NotRequired[str],
        "input": NotRequired[str],
        "scheduleToCloseTimeout": NotRequired[str],
        "taskList": NotRequired[TaskListTypeDef],
        "taskPriority": NotRequired[str],
        "scheduleToStartTimeout": NotRequired[str],
        "startToCloseTimeout": NotRequired[str],
        "heartbeatTimeout": NotRequired[str],
    },
)
WorkflowExecutionConfigurationTypeDef = TypedDict(
    "WorkflowExecutionConfigurationTypeDef",
    {
        "taskStartToCloseTimeout": str,
        "executionStartToCloseTimeout": str,
        "taskList": TaskListTypeDef,
        "childPolicy": ChildPolicyType,
        "taskPriority": NotRequired[str],
        "lambdaRole": NotRequired[str],
    },
)
WorkflowTypeConfigurationTypeDef = TypedDict(
    "WorkflowTypeConfigurationTypeDef",
    {
        "defaultTaskStartToCloseTimeout": NotRequired[str],
        "defaultExecutionStartToCloseTimeout": NotRequired[str],
        "defaultTaskList": NotRequired[TaskListTypeDef],
        "defaultTaskPriority": NotRequired[str],
        "defaultChildPolicy": NotRequired[ChildPolicyType],
        "defaultLambdaRole": NotRequired[str],
    },
)
ActivityTaskStatusTypeDef = TypedDict(
    "ActivityTaskStatusTypeDef",
    {
        "cancelRequested": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PendingTaskCountTypeDef = TypedDict(
    "PendingTaskCountTypeDef",
    {
        "count": int,
        "truncated": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RunTypeDef = TypedDict(
    "RunTypeDef",
    {
        "runId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
WorkflowExecutionCountTypeDef = TypedDict(
    "WorkflowExecutionCountTypeDef",
    {
        "count": int,
        "truncated": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ActivityTaskTypeDef = TypedDict(
    "ActivityTaskTypeDef",
    {
        "taskToken": str,
        "activityId": str,
        "startedEventId": int,
        "workflowExecution": WorkflowExecutionTypeDef,
        "activityType": ActivityTypeTypeDef,
        "input": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeWorkflowExecutionInputRequestTypeDef = TypedDict(
    "DescribeWorkflowExecutionInputRequestTypeDef",
    {
        "domain": str,
        "execution": WorkflowExecutionTypeDef,
    },
)
ExternalWorkflowExecutionCancelRequestedEventAttributesTypeDef = TypedDict(
    "ExternalWorkflowExecutionCancelRequestedEventAttributesTypeDef",
    {
        "workflowExecution": WorkflowExecutionTypeDef,
        "initiatedEventId": int,
    },
)
ExternalWorkflowExecutionSignaledEventAttributesTypeDef = TypedDict(
    "ExternalWorkflowExecutionSignaledEventAttributesTypeDef",
    {
        "workflowExecution": WorkflowExecutionTypeDef,
        "initiatedEventId": int,
    },
)
GetWorkflowExecutionHistoryInputRequestTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryInputRequestTypeDef",
    {
        "domain": str,
        "execution": WorkflowExecutionTypeDef,
        "nextPageToken": NotRequired[str],
        "maximumPageSize": NotRequired[int],
        "reverseOrder": NotRequired[bool],
    },
)
WorkflowExecutionCancelRequestedEventAttributesTypeDef = TypedDict(
    "WorkflowExecutionCancelRequestedEventAttributesTypeDef",
    {
        "externalWorkflowExecution": NotRequired[WorkflowExecutionTypeDef],
        "externalInitiatedEventId": NotRequired[int],
        "cause": NotRequired[Literal["CHILD_POLICY_APPLIED"]],
    },
)
WorkflowExecutionSignaledEventAttributesTypeDef = TypedDict(
    "WorkflowExecutionSignaledEventAttributesTypeDef",
    {
        "signalName": str,
        "input": NotRequired[str],
        "externalWorkflowExecution": NotRequired[WorkflowExecutionTypeDef],
        "externalInitiatedEventId": NotRequired[int],
    },
)
ChildWorkflowExecutionCanceledEventAttributesTypeDef = TypedDict(
    "ChildWorkflowExecutionCanceledEventAttributesTypeDef",
    {
        "workflowExecution": WorkflowExecutionTypeDef,
        "workflowType": WorkflowTypeTypeDef,
        "initiatedEventId": int,
        "startedEventId": int,
        "details": NotRequired[str],
    },
)
ChildWorkflowExecutionCompletedEventAttributesTypeDef = TypedDict(
    "ChildWorkflowExecutionCompletedEventAttributesTypeDef",
    {
        "workflowExecution": WorkflowExecutionTypeDef,
        "workflowType": WorkflowTypeTypeDef,
        "initiatedEventId": int,
        "startedEventId": int,
        "result": NotRequired[str],
    },
)
ChildWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "ChildWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowExecution": WorkflowExecutionTypeDef,
        "workflowType": WorkflowTypeTypeDef,
        "initiatedEventId": int,
        "startedEventId": int,
        "reason": NotRequired[str],
        "details": NotRequired[str],
    },
)
ChildWorkflowExecutionStartedEventAttributesTypeDef = TypedDict(
    "ChildWorkflowExecutionStartedEventAttributesTypeDef",
    {
        "workflowExecution": WorkflowExecutionTypeDef,
        "workflowType": WorkflowTypeTypeDef,
        "initiatedEventId": int,
    },
)
ChildWorkflowExecutionTerminatedEventAttributesTypeDef = TypedDict(
    "ChildWorkflowExecutionTerminatedEventAttributesTypeDef",
    {
        "workflowExecution": WorkflowExecutionTypeDef,
        "workflowType": WorkflowTypeTypeDef,
        "initiatedEventId": int,
        "startedEventId": int,
    },
)
ChildWorkflowExecutionTimedOutEventAttributesTypeDef = TypedDict(
    "ChildWorkflowExecutionTimedOutEventAttributesTypeDef",
    {
        "workflowExecution": WorkflowExecutionTypeDef,
        "workflowType": WorkflowTypeTypeDef,
        "timeoutType": Literal["START_TO_CLOSE"],
        "initiatedEventId": int,
        "startedEventId": int,
    },
)
DeleteWorkflowTypeInputRequestTypeDef = TypedDict(
    "DeleteWorkflowTypeInputRequestTypeDef",
    {
        "domain": str,
        "workflowType": WorkflowTypeTypeDef,
    },
)
DeprecateWorkflowTypeInputRequestTypeDef = TypedDict(
    "DeprecateWorkflowTypeInputRequestTypeDef",
    {
        "domain": str,
        "workflowType": WorkflowTypeTypeDef,
    },
)
DescribeWorkflowTypeInputRequestTypeDef = TypedDict(
    "DescribeWorkflowTypeInputRequestTypeDef",
    {
        "domain": str,
        "workflowType": WorkflowTypeTypeDef,
    },
)
StartChildWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "StartChildWorkflowExecutionDecisionAttributesTypeDef",
    {
        "workflowType": WorkflowTypeTypeDef,
        "workflowId": str,
        "control": NotRequired[str],
        "input": NotRequired[str],
        "executionStartToCloseTimeout": NotRequired[str],
        "taskList": NotRequired[TaskListTypeDef],
        "taskPriority": NotRequired[str],
        "taskStartToCloseTimeout": NotRequired[str],
        "childPolicy": NotRequired[ChildPolicyType],
        "tagList": NotRequired[Sequence[str]],
        "lambdaRole": NotRequired[str],
    },
)
StartChildWorkflowExecutionFailedEventAttributesTypeDef = TypedDict(
    "StartChildWorkflowExecutionFailedEventAttributesTypeDef",
    {
        "workflowType": WorkflowTypeTypeDef,
        "cause": StartChildWorkflowExecutionFailedCauseType,
        "workflowId": str,
        "initiatedEventId": int,
        "decisionTaskCompletedEventId": int,
        "control": NotRequired[str],
    },
)
StartChildWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "StartChildWorkflowExecutionInitiatedEventAttributesTypeDef",
    {
        "workflowId": str,
        "workflowType": WorkflowTypeTypeDef,
        "taskList": TaskListTypeDef,
        "decisionTaskCompletedEventId": int,
        "childPolicy": ChildPolicyType,
        "control": NotRequired[str],
        "input": NotRequired[str],
        "executionStartToCloseTimeout": NotRequired[str],
        "taskPriority": NotRequired[str],
        "taskStartToCloseTimeout": NotRequired[str],
        "tagList": NotRequired[List[str]],
        "lambdaRole": NotRequired[str],
    },
)
StartWorkflowExecutionInputRequestTypeDef = TypedDict(
    "StartWorkflowExecutionInputRequestTypeDef",
    {
        "domain": str,
        "workflowId": str,
        "workflowType": WorkflowTypeTypeDef,
        "taskList": NotRequired[TaskListTypeDef],
        "taskPriority": NotRequired[str],
        "input": NotRequired[str],
        "executionStartToCloseTimeout": NotRequired[str],
        "tagList": NotRequired[Sequence[str]],
        "taskStartToCloseTimeout": NotRequired[str],
        "childPolicy": NotRequired[ChildPolicyType],
        "lambdaRole": NotRequired[str],
    },
)
UndeprecateWorkflowTypeInputRequestTypeDef = TypedDict(
    "UndeprecateWorkflowTypeInputRequestTypeDef",
    {
        "domain": str,
        "workflowType": WorkflowTypeTypeDef,
    },
)
WorkflowExecutionContinuedAsNewEventAttributesTypeDef = TypedDict(
    "WorkflowExecutionContinuedAsNewEventAttributesTypeDef",
    {
        "decisionTaskCompletedEventId": int,
        "newExecutionRunId": str,
        "taskList": TaskListTypeDef,
        "childPolicy": ChildPolicyType,
        "workflowType": WorkflowTypeTypeDef,
        "input": NotRequired[str],
        "executionStartToCloseTimeout": NotRequired[str],
        "taskPriority": NotRequired[str],
        "taskStartToCloseTimeout": NotRequired[str],
        "tagList": NotRequired[List[str]],
        "lambdaRole": NotRequired[str],
    },
)
WorkflowExecutionInfoTypeDef = TypedDict(
    "WorkflowExecutionInfoTypeDef",
    {
        "execution": WorkflowExecutionTypeDef,
        "workflowType": WorkflowTypeTypeDef,
        "startTimestamp": datetime,
        "executionStatus": ExecutionStatusType,
        "closeTimestamp": NotRequired[datetime],
        "closeStatus": NotRequired[CloseStatusType],
        "parent": NotRequired[WorkflowExecutionTypeDef],
        "tagList": NotRequired[List[str]],
        "cancelRequested": NotRequired[bool],
    },
)
WorkflowExecutionStartedEventAttributesTypeDef = TypedDict(
    "WorkflowExecutionStartedEventAttributesTypeDef",
    {
        "childPolicy": ChildPolicyType,
        "taskList": TaskListTypeDef,
        "workflowType": WorkflowTypeTypeDef,
        "input": NotRequired[str],
        "executionStartToCloseTimeout": NotRequired[str],
        "taskStartToCloseTimeout": NotRequired[str],
        "taskPriority": NotRequired[str],
        "tagList": NotRequired[List[str]],
        "continuedExecutionRunId": NotRequired[str],
        "parentWorkflowExecution": NotRequired[WorkflowExecutionTypeDef],
        "parentInitiatedEventId": NotRequired[int],
        "lambdaRole": NotRequired[str],
    },
)
WorkflowTypeInfoTypeDef = TypedDict(
    "WorkflowTypeInfoTypeDef",
    {
        "workflowType": WorkflowTypeTypeDef,
        "status": RegistrationStatusType,
        "creationDate": datetime,
        "description": NotRequired[str],
        "deprecationDate": NotRequired[datetime],
    },
)
DomainDetailTypeDef = TypedDict(
    "DomainDetailTypeDef",
    {
        "domainInfo": DomainInfoTypeDef,
        "configuration": DomainConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DomainInfosTypeDef = TypedDict(
    "DomainInfosTypeDef",
    {
        "domainInfos": List[DomainInfoTypeDef],
        "nextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExecutionTimeFilterTypeDef = TypedDict(
    "ExecutionTimeFilterTypeDef",
    {
        "oldestDate": TimestampTypeDef,
        "latestDate": NotRequired[TimestampTypeDef],
    },
)
GetWorkflowExecutionHistoryInputGetWorkflowExecutionHistoryPaginateTypeDef = TypedDict(
    "GetWorkflowExecutionHistoryInputGetWorkflowExecutionHistoryPaginateTypeDef",
    {
        "domain": str,
        "execution": WorkflowExecutionTypeDef,
        "reverseOrder": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListActivityTypesInputListActivityTypesPaginateTypeDef = TypedDict(
    "ListActivityTypesInputListActivityTypesPaginateTypeDef",
    {
        "domain": str,
        "registrationStatus": RegistrationStatusType,
        "name": NotRequired[str],
        "reverseOrder": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDomainsInputListDomainsPaginateTypeDef = TypedDict(
    "ListDomainsInputListDomainsPaginateTypeDef",
    {
        "registrationStatus": RegistrationStatusType,
        "reverseOrder": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWorkflowTypesInputListWorkflowTypesPaginateTypeDef = TypedDict(
    "ListWorkflowTypesInputListWorkflowTypesPaginateTypeDef",
    {
        "domain": str,
        "registrationStatus": RegistrationStatusType,
        "name": NotRequired[str],
        "reverseOrder": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
PollForDecisionTaskInputPollForDecisionTaskPaginateTypeDef = TypedDict(
    "PollForDecisionTaskInputPollForDecisionTaskPaginateTypeDef",
    {
        "domain": str,
        "taskList": TaskListTypeDef,
        "identity": NotRequired[str],
        "reverseOrder": NotRequired[bool],
        "startAtPreviousStartedEvent": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "tags": List[ResourceTagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterDomainInputRequestTypeDef = TypedDict(
    "RegisterDomainInputRequestTypeDef",
    {
        "name": str,
        "workflowExecutionRetentionPeriodInDays": str,
        "description": NotRequired[str],
        "tags": NotRequired[Sequence[ResourceTagTypeDef]],
    },
)
TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[ResourceTagTypeDef],
    },
)
ActivityTypeInfosTypeDef = TypedDict(
    "ActivityTypeInfosTypeDef",
    {
        "typeInfos": List[ActivityTypeInfoTypeDef],
        "nextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ActivityTypeDetailTypeDef = TypedDict(
    "ActivityTypeDetailTypeDef",
    {
        "typeInfo": ActivityTypeInfoTypeDef,
        "configuration": ActivityTypeConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DecisionTypeDef = TypedDict(
    "DecisionTypeDef",
    {
        "decisionType": DecisionTypeType,
        "scheduleActivityTaskDecisionAttributes": NotRequired[
            ScheduleActivityTaskDecisionAttributesTypeDef
        ],
        "requestCancelActivityTaskDecisionAttributes": NotRequired[
            RequestCancelActivityTaskDecisionAttributesTypeDef
        ],
        "completeWorkflowExecutionDecisionAttributes": NotRequired[
            CompleteWorkflowExecutionDecisionAttributesTypeDef
        ],
        "failWorkflowExecutionDecisionAttributes": NotRequired[
            FailWorkflowExecutionDecisionAttributesTypeDef
        ],
        "cancelWorkflowExecutionDecisionAttributes": NotRequired[
            CancelWorkflowExecutionDecisionAttributesTypeDef
        ],
        "continueAsNewWorkflowExecutionDecisionAttributes": NotRequired[
            ContinueAsNewWorkflowExecutionDecisionAttributesTypeDef
        ],
        "recordMarkerDecisionAttributes": NotRequired[RecordMarkerDecisionAttributesTypeDef],
        "startTimerDecisionAttributes": NotRequired[StartTimerDecisionAttributesTypeDef],
        "cancelTimerDecisionAttributes": NotRequired[CancelTimerDecisionAttributesTypeDef],
        "signalExternalWorkflowExecutionDecisionAttributes": NotRequired[
            SignalExternalWorkflowExecutionDecisionAttributesTypeDef
        ],
        "requestCancelExternalWorkflowExecutionDecisionAttributes": NotRequired[
            RequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef
        ],
        "startChildWorkflowExecutionDecisionAttributes": NotRequired[
            StartChildWorkflowExecutionDecisionAttributesTypeDef
        ],
        "scheduleLambdaFunctionDecisionAttributes": NotRequired[
            ScheduleLambdaFunctionDecisionAttributesTypeDef
        ],
    },
)
WorkflowExecutionDetailTypeDef = TypedDict(
    "WorkflowExecutionDetailTypeDef",
    {
        "executionInfo": WorkflowExecutionInfoTypeDef,
        "executionConfiguration": WorkflowExecutionConfigurationTypeDef,
        "openCounts": WorkflowExecutionOpenCountsTypeDef,
        "latestActivityTaskTimestamp": datetime,
        "latestExecutionContext": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
WorkflowExecutionInfosTypeDef = TypedDict(
    "WorkflowExecutionInfosTypeDef",
    {
        "executionInfos": List[WorkflowExecutionInfoTypeDef],
        "nextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
HistoryEventTypeDef = TypedDict(
    "HistoryEventTypeDef",
    {
        "eventTimestamp": datetime,
        "eventType": EventTypeType,
        "eventId": int,
        "workflowExecutionStartedEventAttributes": NotRequired[
            WorkflowExecutionStartedEventAttributesTypeDef
        ],
        "workflowExecutionCompletedEventAttributes": NotRequired[
            WorkflowExecutionCompletedEventAttributesTypeDef
        ],
        "completeWorkflowExecutionFailedEventAttributes": NotRequired[
            CompleteWorkflowExecutionFailedEventAttributesTypeDef
        ],
        "workflowExecutionFailedEventAttributes": NotRequired[
            WorkflowExecutionFailedEventAttributesTypeDef
        ],
        "failWorkflowExecutionFailedEventAttributes": NotRequired[
            FailWorkflowExecutionFailedEventAttributesTypeDef
        ],
        "workflowExecutionTimedOutEventAttributes": NotRequired[
            WorkflowExecutionTimedOutEventAttributesTypeDef
        ],
        "workflowExecutionCanceledEventAttributes": NotRequired[
            WorkflowExecutionCanceledEventAttributesTypeDef
        ],
        "cancelWorkflowExecutionFailedEventAttributes": NotRequired[
            CancelWorkflowExecutionFailedEventAttributesTypeDef
        ],
        "workflowExecutionContinuedAsNewEventAttributes": NotRequired[
            WorkflowExecutionContinuedAsNewEventAttributesTypeDef
        ],
        "continueAsNewWorkflowExecutionFailedEventAttributes": NotRequired[
            ContinueAsNewWorkflowExecutionFailedEventAttributesTypeDef
        ],
        "workflowExecutionTerminatedEventAttributes": NotRequired[
            WorkflowExecutionTerminatedEventAttributesTypeDef
        ],
        "workflowExecutionCancelRequestedEventAttributes": NotRequired[
            WorkflowExecutionCancelRequestedEventAttributesTypeDef
        ],
        "decisionTaskScheduledEventAttributes": NotRequired[
            DecisionTaskScheduledEventAttributesTypeDef
        ],
        "decisionTaskStartedEventAttributes": NotRequired[
            DecisionTaskStartedEventAttributesTypeDef
        ],
        "decisionTaskCompletedEventAttributes": NotRequired[
            DecisionTaskCompletedEventAttributesTypeDef
        ],
        "decisionTaskTimedOutEventAttributes": NotRequired[
            DecisionTaskTimedOutEventAttributesTypeDef
        ],
        "activityTaskScheduledEventAttributes": NotRequired[
            ActivityTaskScheduledEventAttributesTypeDef
        ],
        "activityTaskStartedEventAttributes": NotRequired[
            ActivityTaskStartedEventAttributesTypeDef
        ],
        "activityTaskCompletedEventAttributes": NotRequired[
            ActivityTaskCompletedEventAttributesTypeDef
        ],
        "activityTaskFailedEventAttributes": NotRequired[ActivityTaskFailedEventAttributesTypeDef],
        "activityTaskTimedOutEventAttributes": NotRequired[
            ActivityTaskTimedOutEventAttributesTypeDef
        ],
        "activityTaskCanceledEventAttributes": NotRequired[
            ActivityTaskCanceledEventAttributesTypeDef
        ],
        "activityTaskCancelRequestedEventAttributes": NotRequired[
            ActivityTaskCancelRequestedEventAttributesTypeDef
        ],
        "workflowExecutionSignaledEventAttributes": NotRequired[
            WorkflowExecutionSignaledEventAttributesTypeDef
        ],
        "markerRecordedEventAttributes": NotRequired[MarkerRecordedEventAttributesTypeDef],
        "recordMarkerFailedEventAttributes": NotRequired[RecordMarkerFailedEventAttributesTypeDef],
        "timerStartedEventAttributes": NotRequired[TimerStartedEventAttributesTypeDef],
        "timerFiredEventAttributes": NotRequired[TimerFiredEventAttributesTypeDef],
        "timerCanceledEventAttributes": NotRequired[TimerCanceledEventAttributesTypeDef],
        "startChildWorkflowExecutionInitiatedEventAttributes": NotRequired[
            StartChildWorkflowExecutionInitiatedEventAttributesTypeDef
        ],
        "childWorkflowExecutionStartedEventAttributes": NotRequired[
            ChildWorkflowExecutionStartedEventAttributesTypeDef
        ],
        "childWorkflowExecutionCompletedEventAttributes": NotRequired[
            ChildWorkflowExecutionCompletedEventAttributesTypeDef
        ],
        "childWorkflowExecutionFailedEventAttributes": NotRequired[
            ChildWorkflowExecutionFailedEventAttributesTypeDef
        ],
        "childWorkflowExecutionTimedOutEventAttributes": NotRequired[
            ChildWorkflowExecutionTimedOutEventAttributesTypeDef
        ],
        "childWorkflowExecutionCanceledEventAttributes": NotRequired[
            ChildWorkflowExecutionCanceledEventAttributesTypeDef
        ],
        "childWorkflowExecutionTerminatedEventAttributes": NotRequired[
            ChildWorkflowExecutionTerminatedEventAttributesTypeDef
        ],
        "signalExternalWorkflowExecutionInitiatedEventAttributes": NotRequired[
            SignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef
        ],
        "externalWorkflowExecutionSignaledEventAttributes": NotRequired[
            ExternalWorkflowExecutionSignaledEventAttributesTypeDef
        ],
        "signalExternalWorkflowExecutionFailedEventAttributes": NotRequired[
            SignalExternalWorkflowExecutionFailedEventAttributesTypeDef
        ],
        "externalWorkflowExecutionCancelRequestedEventAttributes": NotRequired[
            ExternalWorkflowExecutionCancelRequestedEventAttributesTypeDef
        ],
        "requestCancelExternalWorkflowExecutionInitiatedEventAttributes": NotRequired[
            RequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef
        ],
        "requestCancelExternalWorkflowExecutionFailedEventAttributes": NotRequired[
            RequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef
        ],
        "scheduleActivityTaskFailedEventAttributes": NotRequired[
            ScheduleActivityTaskFailedEventAttributesTypeDef
        ],
        "requestCancelActivityTaskFailedEventAttributes": NotRequired[
            RequestCancelActivityTaskFailedEventAttributesTypeDef
        ],
        "startTimerFailedEventAttributes": NotRequired[StartTimerFailedEventAttributesTypeDef],
        "cancelTimerFailedEventAttributes": NotRequired[CancelTimerFailedEventAttributesTypeDef],
        "startChildWorkflowExecutionFailedEventAttributes": NotRequired[
            StartChildWorkflowExecutionFailedEventAttributesTypeDef
        ],
        "lambdaFunctionScheduledEventAttributes": NotRequired[
            LambdaFunctionScheduledEventAttributesTypeDef
        ],
        "lambdaFunctionStartedEventAttributes": NotRequired[
            LambdaFunctionStartedEventAttributesTypeDef
        ],
        "lambdaFunctionCompletedEventAttributes": NotRequired[
            LambdaFunctionCompletedEventAttributesTypeDef
        ],
        "lambdaFunctionFailedEventAttributes": NotRequired[
            LambdaFunctionFailedEventAttributesTypeDef
        ],
        "lambdaFunctionTimedOutEventAttributes": NotRequired[
            LambdaFunctionTimedOutEventAttributesTypeDef
        ],
        "scheduleLambdaFunctionFailedEventAttributes": NotRequired[
            ScheduleLambdaFunctionFailedEventAttributesTypeDef
        ],
        "startLambdaFunctionFailedEventAttributes": NotRequired[
            StartLambdaFunctionFailedEventAttributesTypeDef
        ],
    },
)
WorkflowTypeDetailTypeDef = TypedDict(
    "WorkflowTypeDetailTypeDef",
    {
        "typeInfo": WorkflowTypeInfoTypeDef,
        "configuration": WorkflowTypeConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
WorkflowTypeInfosTypeDef = TypedDict(
    "WorkflowTypeInfosTypeDef",
    {
        "typeInfos": List[WorkflowTypeInfoTypeDef],
        "nextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CountClosedWorkflowExecutionsInputRequestTypeDef = TypedDict(
    "CountClosedWorkflowExecutionsInputRequestTypeDef",
    {
        "domain": str,
        "startTimeFilter": NotRequired[ExecutionTimeFilterTypeDef],
        "closeTimeFilter": NotRequired[ExecutionTimeFilterTypeDef],
        "executionFilter": NotRequired[WorkflowExecutionFilterTypeDef],
        "typeFilter": NotRequired[WorkflowTypeFilterTypeDef],
        "tagFilter": NotRequired[TagFilterTypeDef],
        "closeStatusFilter": NotRequired[CloseStatusFilterTypeDef],
    },
)
CountOpenWorkflowExecutionsInputRequestTypeDef = TypedDict(
    "CountOpenWorkflowExecutionsInputRequestTypeDef",
    {
        "domain": str,
        "startTimeFilter": ExecutionTimeFilterTypeDef,
        "typeFilter": NotRequired[WorkflowTypeFilterTypeDef],
        "tagFilter": NotRequired[TagFilterTypeDef],
        "executionFilter": NotRequired[WorkflowExecutionFilterTypeDef],
    },
)
ListClosedWorkflowExecutionsInputListClosedWorkflowExecutionsPaginateTypeDef = TypedDict(
    "ListClosedWorkflowExecutionsInputListClosedWorkflowExecutionsPaginateTypeDef",
    {
        "domain": str,
        "startTimeFilter": NotRequired[ExecutionTimeFilterTypeDef],
        "closeTimeFilter": NotRequired[ExecutionTimeFilterTypeDef],
        "executionFilter": NotRequired[WorkflowExecutionFilterTypeDef],
        "closeStatusFilter": NotRequired[CloseStatusFilterTypeDef],
        "typeFilter": NotRequired[WorkflowTypeFilterTypeDef],
        "tagFilter": NotRequired[TagFilterTypeDef],
        "reverseOrder": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListClosedWorkflowExecutionsInputRequestTypeDef = TypedDict(
    "ListClosedWorkflowExecutionsInputRequestTypeDef",
    {
        "domain": str,
        "startTimeFilter": NotRequired[ExecutionTimeFilterTypeDef],
        "closeTimeFilter": NotRequired[ExecutionTimeFilterTypeDef],
        "executionFilter": NotRequired[WorkflowExecutionFilterTypeDef],
        "closeStatusFilter": NotRequired[CloseStatusFilterTypeDef],
        "typeFilter": NotRequired[WorkflowTypeFilterTypeDef],
        "tagFilter": NotRequired[TagFilterTypeDef],
        "nextPageToken": NotRequired[str],
        "maximumPageSize": NotRequired[int],
        "reverseOrder": NotRequired[bool],
    },
)
ListOpenWorkflowExecutionsInputListOpenWorkflowExecutionsPaginateTypeDef = TypedDict(
    "ListOpenWorkflowExecutionsInputListOpenWorkflowExecutionsPaginateTypeDef",
    {
        "domain": str,
        "startTimeFilter": ExecutionTimeFilterTypeDef,
        "typeFilter": NotRequired[WorkflowTypeFilterTypeDef],
        "tagFilter": NotRequired[TagFilterTypeDef],
        "reverseOrder": NotRequired[bool],
        "executionFilter": NotRequired[WorkflowExecutionFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOpenWorkflowExecutionsInputRequestTypeDef = TypedDict(
    "ListOpenWorkflowExecutionsInputRequestTypeDef",
    {
        "domain": str,
        "startTimeFilter": ExecutionTimeFilterTypeDef,
        "typeFilter": NotRequired[WorkflowTypeFilterTypeDef],
        "tagFilter": NotRequired[TagFilterTypeDef],
        "nextPageToken": NotRequired[str],
        "maximumPageSize": NotRequired[int],
        "reverseOrder": NotRequired[bool],
        "executionFilter": NotRequired[WorkflowExecutionFilterTypeDef],
    },
)
RespondDecisionTaskCompletedInputRequestTypeDef = TypedDict(
    "RespondDecisionTaskCompletedInputRequestTypeDef",
    {
        "taskToken": str,
        "decisions": NotRequired[Sequence[DecisionTypeDef]],
        "executionContext": NotRequired[str],
        "taskList": NotRequired[TaskListTypeDef],
        "taskListScheduleToStartTimeout": NotRequired[str],
    },
)
DecisionTaskTypeDef = TypedDict(
    "DecisionTaskTypeDef",
    {
        "taskToken": str,
        "startedEventId": int,
        "workflowExecution": WorkflowExecutionTypeDef,
        "workflowType": WorkflowTypeTypeDef,
        "events": List[HistoryEventTypeDef],
        "nextPageToken": str,
        "previousStartedEventId": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
HistoryTypeDef = TypedDict(
    "HistoryTypeDef",
    {
        "events": List[HistoryEventTypeDef],
        "nextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
