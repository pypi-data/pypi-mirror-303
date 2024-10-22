"""
Type annotations for iotevents-data service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/type_defs/)

Usage::

    ```python
    from mypy_boto3_iotevents_data.type_defs import AcknowledgeActionConfigurationTypeDef

    data: AcknowledgeActionConfigurationTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    AlarmStateNameType,
    ComparisonOperatorType,
    CustomerActionNameType,
    ErrorCodeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AcknowledgeActionConfigurationTypeDef",
    "AcknowledgeAlarmActionRequestTypeDef",
    "AlarmSummaryTypeDef",
    "BatchAlarmActionErrorEntryTypeDef",
    "ResponseMetadataTypeDef",
    "BatchDeleteDetectorErrorEntryTypeDef",
    "DeleteDetectorRequestTypeDef",
    "DisableAlarmActionRequestTypeDef",
    "EnableAlarmActionRequestTypeDef",
    "BatchPutMessageErrorEntryTypeDef",
    "ResetAlarmActionRequestTypeDef",
    "SnoozeAlarmActionRequestTypeDef",
    "BatchUpdateDetectorErrorEntryTypeDef",
    "BlobTypeDef",
    "DisableActionConfigurationTypeDef",
    "EnableActionConfigurationTypeDef",
    "ResetActionConfigurationTypeDef",
    "SnoozeActionConfigurationTypeDef",
    "DescribeAlarmRequestRequestTypeDef",
    "DescribeDetectorRequestRequestTypeDef",
    "TimerDefinitionTypeDef",
    "VariableDefinitionTypeDef",
    "DetectorStateSummaryTypeDef",
    "TimerTypeDef",
    "VariableTypeDef",
    "ListAlarmsRequestRequestTypeDef",
    "ListDetectorsRequestRequestTypeDef",
    "TimestampValueTypeDef",
    "SimpleRuleEvaluationTypeDef",
    "StateChangeConfigurationTypeDef",
    "BatchAcknowledgeAlarmRequestRequestTypeDef",
    "BatchAcknowledgeAlarmResponseTypeDef",
    "BatchDisableAlarmResponseTypeDef",
    "BatchEnableAlarmResponseTypeDef",
    "BatchResetAlarmResponseTypeDef",
    "BatchSnoozeAlarmResponseTypeDef",
    "ListAlarmsResponseTypeDef",
    "BatchDeleteDetectorResponseTypeDef",
    "BatchDeleteDetectorRequestRequestTypeDef",
    "BatchDisableAlarmRequestRequestTypeDef",
    "BatchEnableAlarmRequestRequestTypeDef",
    "BatchPutMessageResponseTypeDef",
    "BatchResetAlarmRequestRequestTypeDef",
    "BatchSnoozeAlarmRequestRequestTypeDef",
    "BatchUpdateDetectorResponseTypeDef",
    "CustomerActionTypeDef",
    "DetectorStateDefinitionTypeDef",
    "DetectorSummaryTypeDef",
    "DetectorStateTypeDef",
    "MessageTypeDef",
    "RuleEvaluationTypeDef",
    "SystemEventTypeDef",
    "UpdateDetectorRequestTypeDef",
    "ListDetectorsResponseTypeDef",
    "DetectorTypeDef",
    "BatchPutMessageRequestRequestTypeDef",
    "AlarmStateTypeDef",
    "BatchUpdateDetectorRequestRequestTypeDef",
    "DescribeDetectorResponseTypeDef",
    "AlarmTypeDef",
    "DescribeAlarmResponseTypeDef",
)

AcknowledgeActionConfigurationTypeDef = TypedDict(
    "AcknowledgeActionConfigurationTypeDef",
    {
        "note": NotRequired[str],
    },
)
AcknowledgeAlarmActionRequestTypeDef = TypedDict(
    "AcknowledgeAlarmActionRequestTypeDef",
    {
        "requestId": str,
        "alarmModelName": str,
        "keyValue": NotRequired[str],
        "note": NotRequired[str],
    },
)
AlarmSummaryTypeDef = TypedDict(
    "AlarmSummaryTypeDef",
    {
        "alarmModelName": NotRequired[str],
        "alarmModelVersion": NotRequired[str],
        "keyValue": NotRequired[str],
        "stateName": NotRequired[AlarmStateNameType],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
    },
)
BatchAlarmActionErrorEntryTypeDef = TypedDict(
    "BatchAlarmActionErrorEntryTypeDef",
    {
        "requestId": NotRequired[str],
        "errorCode": NotRequired[ErrorCodeType],
        "errorMessage": NotRequired[str],
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
BatchDeleteDetectorErrorEntryTypeDef = TypedDict(
    "BatchDeleteDetectorErrorEntryTypeDef",
    {
        "messageId": NotRequired[str],
        "errorCode": NotRequired[ErrorCodeType],
        "errorMessage": NotRequired[str],
    },
)
DeleteDetectorRequestTypeDef = TypedDict(
    "DeleteDetectorRequestTypeDef",
    {
        "messageId": str,
        "detectorModelName": str,
        "keyValue": NotRequired[str],
    },
)
DisableAlarmActionRequestTypeDef = TypedDict(
    "DisableAlarmActionRequestTypeDef",
    {
        "requestId": str,
        "alarmModelName": str,
        "keyValue": NotRequired[str],
        "note": NotRequired[str],
    },
)
EnableAlarmActionRequestTypeDef = TypedDict(
    "EnableAlarmActionRequestTypeDef",
    {
        "requestId": str,
        "alarmModelName": str,
        "keyValue": NotRequired[str],
        "note": NotRequired[str],
    },
)
BatchPutMessageErrorEntryTypeDef = TypedDict(
    "BatchPutMessageErrorEntryTypeDef",
    {
        "messageId": NotRequired[str],
        "errorCode": NotRequired[ErrorCodeType],
        "errorMessage": NotRequired[str],
    },
)
ResetAlarmActionRequestTypeDef = TypedDict(
    "ResetAlarmActionRequestTypeDef",
    {
        "requestId": str,
        "alarmModelName": str,
        "keyValue": NotRequired[str],
        "note": NotRequired[str],
    },
)
SnoozeAlarmActionRequestTypeDef = TypedDict(
    "SnoozeAlarmActionRequestTypeDef",
    {
        "requestId": str,
        "alarmModelName": str,
        "snoozeDuration": int,
        "keyValue": NotRequired[str],
        "note": NotRequired[str],
    },
)
BatchUpdateDetectorErrorEntryTypeDef = TypedDict(
    "BatchUpdateDetectorErrorEntryTypeDef",
    {
        "messageId": NotRequired[str],
        "errorCode": NotRequired[ErrorCodeType],
        "errorMessage": NotRequired[str],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
DisableActionConfigurationTypeDef = TypedDict(
    "DisableActionConfigurationTypeDef",
    {
        "note": NotRequired[str],
    },
)
EnableActionConfigurationTypeDef = TypedDict(
    "EnableActionConfigurationTypeDef",
    {
        "note": NotRequired[str],
    },
)
ResetActionConfigurationTypeDef = TypedDict(
    "ResetActionConfigurationTypeDef",
    {
        "note": NotRequired[str],
    },
)
SnoozeActionConfigurationTypeDef = TypedDict(
    "SnoozeActionConfigurationTypeDef",
    {
        "snoozeDuration": NotRequired[int],
        "note": NotRequired[str],
    },
)
DescribeAlarmRequestRequestTypeDef = TypedDict(
    "DescribeAlarmRequestRequestTypeDef",
    {
        "alarmModelName": str,
        "keyValue": NotRequired[str],
    },
)
DescribeDetectorRequestRequestTypeDef = TypedDict(
    "DescribeDetectorRequestRequestTypeDef",
    {
        "detectorModelName": str,
        "keyValue": NotRequired[str],
    },
)
TimerDefinitionTypeDef = TypedDict(
    "TimerDefinitionTypeDef",
    {
        "name": str,
        "seconds": int,
    },
)
VariableDefinitionTypeDef = TypedDict(
    "VariableDefinitionTypeDef",
    {
        "name": str,
        "value": str,
    },
)
DetectorStateSummaryTypeDef = TypedDict(
    "DetectorStateSummaryTypeDef",
    {
        "stateName": NotRequired[str],
    },
)
TimerTypeDef = TypedDict(
    "TimerTypeDef",
    {
        "name": str,
        "timestamp": datetime,
    },
)
VariableTypeDef = TypedDict(
    "VariableTypeDef",
    {
        "name": str,
        "value": str,
    },
)
ListAlarmsRequestRequestTypeDef = TypedDict(
    "ListAlarmsRequestRequestTypeDef",
    {
        "alarmModelName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListDetectorsRequestRequestTypeDef = TypedDict(
    "ListDetectorsRequestRequestTypeDef",
    {
        "detectorModelName": str,
        "stateName": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
TimestampValueTypeDef = TypedDict(
    "TimestampValueTypeDef",
    {
        "timeInMillis": NotRequired[int],
    },
)
SimpleRuleEvaluationTypeDef = TypedDict(
    "SimpleRuleEvaluationTypeDef",
    {
        "inputPropertyValue": NotRequired[str],
        "operator": NotRequired[ComparisonOperatorType],
        "thresholdValue": NotRequired[str],
    },
)
StateChangeConfigurationTypeDef = TypedDict(
    "StateChangeConfigurationTypeDef",
    {
        "triggerType": NotRequired[Literal["SNOOZE_TIMEOUT"]],
    },
)
BatchAcknowledgeAlarmRequestRequestTypeDef = TypedDict(
    "BatchAcknowledgeAlarmRequestRequestTypeDef",
    {
        "acknowledgeActionRequests": Sequence[AcknowledgeAlarmActionRequestTypeDef],
    },
)
BatchAcknowledgeAlarmResponseTypeDef = TypedDict(
    "BatchAcknowledgeAlarmResponseTypeDef",
    {
        "errorEntries": List[BatchAlarmActionErrorEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDisableAlarmResponseTypeDef = TypedDict(
    "BatchDisableAlarmResponseTypeDef",
    {
        "errorEntries": List[BatchAlarmActionErrorEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchEnableAlarmResponseTypeDef = TypedDict(
    "BatchEnableAlarmResponseTypeDef",
    {
        "errorEntries": List[BatchAlarmActionErrorEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchResetAlarmResponseTypeDef = TypedDict(
    "BatchResetAlarmResponseTypeDef",
    {
        "errorEntries": List[BatchAlarmActionErrorEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchSnoozeAlarmResponseTypeDef = TypedDict(
    "BatchSnoozeAlarmResponseTypeDef",
    {
        "errorEntries": List[BatchAlarmActionErrorEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAlarmsResponseTypeDef = TypedDict(
    "ListAlarmsResponseTypeDef",
    {
        "alarmSummaries": List[AlarmSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDeleteDetectorResponseTypeDef = TypedDict(
    "BatchDeleteDetectorResponseTypeDef",
    {
        "batchDeleteDetectorErrorEntries": List[BatchDeleteDetectorErrorEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDeleteDetectorRequestRequestTypeDef = TypedDict(
    "BatchDeleteDetectorRequestRequestTypeDef",
    {
        "detectors": Sequence[DeleteDetectorRequestTypeDef],
    },
)
BatchDisableAlarmRequestRequestTypeDef = TypedDict(
    "BatchDisableAlarmRequestRequestTypeDef",
    {
        "disableActionRequests": Sequence[DisableAlarmActionRequestTypeDef],
    },
)
BatchEnableAlarmRequestRequestTypeDef = TypedDict(
    "BatchEnableAlarmRequestRequestTypeDef",
    {
        "enableActionRequests": Sequence[EnableAlarmActionRequestTypeDef],
    },
)
BatchPutMessageResponseTypeDef = TypedDict(
    "BatchPutMessageResponseTypeDef",
    {
        "BatchPutMessageErrorEntries": List[BatchPutMessageErrorEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchResetAlarmRequestRequestTypeDef = TypedDict(
    "BatchResetAlarmRequestRequestTypeDef",
    {
        "resetActionRequests": Sequence[ResetAlarmActionRequestTypeDef],
    },
)
BatchSnoozeAlarmRequestRequestTypeDef = TypedDict(
    "BatchSnoozeAlarmRequestRequestTypeDef",
    {
        "snoozeActionRequests": Sequence[SnoozeAlarmActionRequestTypeDef],
    },
)
BatchUpdateDetectorResponseTypeDef = TypedDict(
    "BatchUpdateDetectorResponseTypeDef",
    {
        "batchUpdateDetectorErrorEntries": List[BatchUpdateDetectorErrorEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CustomerActionTypeDef = TypedDict(
    "CustomerActionTypeDef",
    {
        "actionName": NotRequired[CustomerActionNameType],
        "snoozeActionConfiguration": NotRequired[SnoozeActionConfigurationTypeDef],
        "enableActionConfiguration": NotRequired[EnableActionConfigurationTypeDef],
        "disableActionConfiguration": NotRequired[DisableActionConfigurationTypeDef],
        "acknowledgeActionConfiguration": NotRequired[AcknowledgeActionConfigurationTypeDef],
        "resetActionConfiguration": NotRequired[ResetActionConfigurationTypeDef],
    },
)
DetectorStateDefinitionTypeDef = TypedDict(
    "DetectorStateDefinitionTypeDef",
    {
        "stateName": str,
        "variables": Sequence[VariableDefinitionTypeDef],
        "timers": Sequence[TimerDefinitionTypeDef],
    },
)
DetectorSummaryTypeDef = TypedDict(
    "DetectorSummaryTypeDef",
    {
        "detectorModelName": NotRequired[str],
        "keyValue": NotRequired[str],
        "detectorModelVersion": NotRequired[str],
        "state": NotRequired[DetectorStateSummaryTypeDef],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
    },
)
DetectorStateTypeDef = TypedDict(
    "DetectorStateTypeDef",
    {
        "stateName": str,
        "variables": List[VariableTypeDef],
        "timers": List[TimerTypeDef],
    },
)
MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "messageId": str,
        "inputName": str,
        "payload": BlobTypeDef,
        "timestamp": NotRequired[TimestampValueTypeDef],
    },
)
RuleEvaluationTypeDef = TypedDict(
    "RuleEvaluationTypeDef",
    {
        "simpleRuleEvaluation": NotRequired[SimpleRuleEvaluationTypeDef],
    },
)
SystemEventTypeDef = TypedDict(
    "SystemEventTypeDef",
    {
        "eventType": NotRequired[Literal["STATE_CHANGE"]],
        "stateChangeConfiguration": NotRequired[StateChangeConfigurationTypeDef],
    },
)
UpdateDetectorRequestTypeDef = TypedDict(
    "UpdateDetectorRequestTypeDef",
    {
        "messageId": str,
        "detectorModelName": str,
        "state": DetectorStateDefinitionTypeDef,
        "keyValue": NotRequired[str],
    },
)
ListDetectorsResponseTypeDef = TypedDict(
    "ListDetectorsResponseTypeDef",
    {
        "detectorSummaries": List[DetectorSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DetectorTypeDef = TypedDict(
    "DetectorTypeDef",
    {
        "detectorModelName": NotRequired[str],
        "keyValue": NotRequired[str],
        "detectorModelVersion": NotRequired[str],
        "state": NotRequired[DetectorStateTypeDef],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
    },
)
BatchPutMessageRequestRequestTypeDef = TypedDict(
    "BatchPutMessageRequestRequestTypeDef",
    {
        "messages": Sequence[MessageTypeDef],
    },
)
AlarmStateTypeDef = TypedDict(
    "AlarmStateTypeDef",
    {
        "stateName": NotRequired[AlarmStateNameType],
        "ruleEvaluation": NotRequired[RuleEvaluationTypeDef],
        "customerAction": NotRequired[CustomerActionTypeDef],
        "systemEvent": NotRequired[SystemEventTypeDef],
    },
)
BatchUpdateDetectorRequestRequestTypeDef = TypedDict(
    "BatchUpdateDetectorRequestRequestTypeDef",
    {
        "detectors": Sequence[UpdateDetectorRequestTypeDef],
    },
)
DescribeDetectorResponseTypeDef = TypedDict(
    "DescribeDetectorResponseTypeDef",
    {
        "detector": DetectorTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AlarmTypeDef = TypedDict(
    "AlarmTypeDef",
    {
        "alarmModelName": NotRequired[str],
        "alarmModelVersion": NotRequired[str],
        "keyValue": NotRequired[str],
        "alarmState": NotRequired[AlarmStateTypeDef],
        "severity": NotRequired[int],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
    },
)
DescribeAlarmResponseTypeDef = TypedDict(
    "DescribeAlarmResponseTypeDef",
    {
        "alarm": AlarmTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
