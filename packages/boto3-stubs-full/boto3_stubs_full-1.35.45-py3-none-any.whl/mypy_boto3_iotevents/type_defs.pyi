"""
Type annotations for iotevents service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotevents/type_defs/)

Usage::

    ```python
    from mypy_boto3_iotevents.type_defs import AcknowledgeFlowTypeDef

    data: AcknowledgeFlowTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    AlarmModelVersionStatusType,
    AnalysisResultLevelType,
    AnalysisStatusType,
    ComparisonOperatorType,
    DetectorModelVersionStatusType,
    EvaluationMethodType,
    InputStatusType,
    LoggingLevelType,
    PayloadTypeType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AcknowledgeFlowTypeDef",
    "ClearTimerActionTypeDef",
    "ResetTimerActionTypeDef",
    "SetTimerActionTypeDef",
    "SetVariableActionTypeDef",
    "InitializationConfigurationTypeDef",
    "AlarmModelSummaryTypeDef",
    "AlarmModelVersionSummaryTypeDef",
    "SimpleRuleTypeDef",
    "AnalysisResultLocationTypeDef",
    "AssetPropertyTimestampTypeDef",
    "AssetPropertyVariantTypeDef",
    "AttributeTypeDef",
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "DetectorModelConfigurationTypeDef",
    "InputConfigurationTypeDef",
    "DeleteAlarmModelRequestRequestTypeDef",
    "DeleteDetectorModelRequestRequestTypeDef",
    "DeleteInputRequestRequestTypeDef",
    "DescribeAlarmModelRequestRequestTypeDef",
    "DescribeDetectorModelAnalysisRequestRequestTypeDef",
    "DescribeDetectorModelRequestRequestTypeDef",
    "DescribeInputRequestRequestTypeDef",
    "DetectorDebugOptionTypeDef",
    "DetectorModelSummaryTypeDef",
    "DetectorModelVersionSummaryTypeDef",
    "PayloadTypeDef",
    "EmailContentTypeDef",
    "GetDetectorModelAnalysisResultsRequestRequestTypeDef",
    "IotEventsInputIdentifierTypeDef",
    "InputSummaryTypeDef",
    "IotSiteWiseAssetModelPropertyIdentifierTypeDef",
    "ListAlarmModelVersionsRequestRequestTypeDef",
    "ListAlarmModelsRequestRequestTypeDef",
    "ListDetectorModelVersionsRequestRequestTypeDef",
    "ListDetectorModelsRequestRequestTypeDef",
    "RoutedResourceTypeDef",
    "ListInputsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "SSOIdentityTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "AlarmCapabilitiesTypeDef",
    "AlarmRuleTypeDef",
    "AnalysisResultTypeDef",
    "AssetPropertyValueTypeDef",
    "InputDefinitionOutputTypeDef",
    "InputDefinitionTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateAlarmModelResponseTypeDef",
    "DescribeDetectorModelAnalysisResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ListAlarmModelVersionsResponseTypeDef",
    "ListAlarmModelsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartDetectorModelAnalysisResponseTypeDef",
    "UpdateAlarmModelResponseTypeDef",
    "CreateDetectorModelResponseTypeDef",
    "UpdateDetectorModelResponseTypeDef",
    "CreateInputResponseTypeDef",
    "UpdateInputResponseTypeDef",
    "LoggingOptionsOutputTypeDef",
    "LoggingOptionsTypeDef",
    "ListDetectorModelsResponseTypeDef",
    "ListDetectorModelVersionsResponseTypeDef",
    "DynamoDBActionTypeDef",
    "DynamoDBv2ActionTypeDef",
    "FirehoseActionTypeDef",
    "IotEventsActionTypeDef",
    "IotTopicPublishActionTypeDef",
    "LambdaActionTypeDef",
    "SNSTopicPublishActionTypeDef",
    "SqsActionTypeDef",
    "ListInputsResponseTypeDef",
    "IotSiteWiseInputIdentifierTypeDef",
    "ListInputRoutingsResponseTypeDef",
    "RecipientDetailTypeDef",
    "GetDetectorModelAnalysisResultsResponseTypeDef",
    "IotSiteWiseActionTypeDef",
    "InputTypeDef",
    "CreateInputRequestRequestTypeDef",
    "UpdateInputRequestRequestTypeDef",
    "DescribeLoggingOptionsResponseTypeDef",
    "PutLoggingOptionsRequestRequestTypeDef",
    "NotificationTargetActionsTypeDef",
    "InputIdentifierTypeDef",
    "EmailRecipientsOutputTypeDef",
    "EmailRecipientsTypeDef",
    "SMSConfigurationOutputTypeDef",
    "SMSConfigurationTypeDef",
    "ActionTypeDef",
    "AlarmActionTypeDef",
    "DescribeInputResponseTypeDef",
    "ListInputRoutingsRequestRequestTypeDef",
    "EmailConfigurationOutputTypeDef",
    "EmailRecipientsUnionTypeDef",
    "SMSConfigurationUnionTypeDef",
    "EventOutputTypeDef",
    "EventTypeDef",
    "TransitionEventOutputTypeDef",
    "TransitionEventTypeDef",
    "AlarmEventActionsOutputTypeDef",
    "AlarmEventActionsTypeDef",
    "NotificationActionOutputTypeDef",
    "EmailConfigurationTypeDef",
    "OnEnterLifecycleOutputTypeDef",
    "OnExitLifecycleOutputTypeDef",
    "EventUnionTypeDef",
    "OnEnterLifecycleTypeDef",
    "OnExitLifecycleTypeDef",
    "OnInputLifecycleOutputTypeDef",
    "TransitionEventUnionTypeDef",
    "AlarmNotificationOutputTypeDef",
    "EmailConfigurationUnionTypeDef",
    "OnEnterLifecycleUnionTypeDef",
    "OnExitLifecycleUnionTypeDef",
    "StateOutputTypeDef",
    "OnInputLifecycleTypeDef",
    "DescribeAlarmModelResponseTypeDef",
    "NotificationActionTypeDef",
    "DetectorModelDefinitionOutputTypeDef",
    "OnInputLifecycleUnionTypeDef",
    "NotificationActionUnionTypeDef",
    "DetectorModelTypeDef",
    "StateTypeDef",
    "AlarmNotificationTypeDef",
    "DescribeDetectorModelResponseTypeDef",
    "StateUnionTypeDef",
    "CreateAlarmModelRequestRequestTypeDef",
    "UpdateAlarmModelRequestRequestTypeDef",
    "DetectorModelDefinitionTypeDef",
    "CreateDetectorModelRequestRequestTypeDef",
    "StartDetectorModelAnalysisRequestRequestTypeDef",
    "UpdateDetectorModelRequestRequestTypeDef",
)

AcknowledgeFlowTypeDef = TypedDict(
    "AcknowledgeFlowTypeDef",
    {
        "enabled": bool,
    },
)
ClearTimerActionTypeDef = TypedDict(
    "ClearTimerActionTypeDef",
    {
        "timerName": str,
    },
)
ResetTimerActionTypeDef = TypedDict(
    "ResetTimerActionTypeDef",
    {
        "timerName": str,
    },
)
SetTimerActionTypeDef = TypedDict(
    "SetTimerActionTypeDef",
    {
        "timerName": str,
        "seconds": NotRequired[int],
        "durationExpression": NotRequired[str],
    },
)
SetVariableActionTypeDef = TypedDict(
    "SetVariableActionTypeDef",
    {
        "variableName": str,
        "value": str,
    },
)
InitializationConfigurationTypeDef = TypedDict(
    "InitializationConfigurationTypeDef",
    {
        "disabledOnInitialization": bool,
    },
)
AlarmModelSummaryTypeDef = TypedDict(
    "AlarmModelSummaryTypeDef",
    {
        "creationTime": NotRequired[datetime],
        "alarmModelDescription": NotRequired[str],
        "alarmModelName": NotRequired[str],
    },
)
AlarmModelVersionSummaryTypeDef = TypedDict(
    "AlarmModelVersionSummaryTypeDef",
    {
        "alarmModelName": NotRequired[str],
        "alarmModelArn": NotRequired[str],
        "alarmModelVersion": NotRequired[str],
        "roleArn": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "status": NotRequired[AlarmModelVersionStatusType],
        "statusMessage": NotRequired[str],
    },
)
SimpleRuleTypeDef = TypedDict(
    "SimpleRuleTypeDef",
    {
        "inputProperty": str,
        "comparisonOperator": ComparisonOperatorType,
        "threshold": str,
    },
)
AnalysisResultLocationTypeDef = TypedDict(
    "AnalysisResultLocationTypeDef",
    {
        "path": NotRequired[str],
    },
)
AssetPropertyTimestampTypeDef = TypedDict(
    "AssetPropertyTimestampTypeDef",
    {
        "timeInSeconds": str,
        "offsetInNanos": NotRequired[str],
    },
)
AssetPropertyVariantTypeDef = TypedDict(
    "AssetPropertyVariantTypeDef",
    {
        "stringValue": NotRequired[str],
        "integerValue": NotRequired[str],
        "doubleValue": NotRequired[str],
        "booleanValue": NotRequired[str],
    },
)
AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "jsonPath": str,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
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
DetectorModelConfigurationTypeDef = TypedDict(
    "DetectorModelConfigurationTypeDef",
    {
        "detectorModelName": NotRequired[str],
        "detectorModelVersion": NotRequired[str],
        "detectorModelDescription": NotRequired[str],
        "detectorModelArn": NotRequired[str],
        "roleArn": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "status": NotRequired[DetectorModelVersionStatusType],
        "key": NotRequired[str],
        "evaluationMethod": NotRequired[EvaluationMethodType],
    },
)
InputConfigurationTypeDef = TypedDict(
    "InputConfigurationTypeDef",
    {
        "inputName": str,
        "inputArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": InputStatusType,
        "inputDescription": NotRequired[str],
    },
)
DeleteAlarmModelRequestRequestTypeDef = TypedDict(
    "DeleteAlarmModelRequestRequestTypeDef",
    {
        "alarmModelName": str,
    },
)
DeleteDetectorModelRequestRequestTypeDef = TypedDict(
    "DeleteDetectorModelRequestRequestTypeDef",
    {
        "detectorModelName": str,
    },
)
DeleteInputRequestRequestTypeDef = TypedDict(
    "DeleteInputRequestRequestTypeDef",
    {
        "inputName": str,
    },
)
DescribeAlarmModelRequestRequestTypeDef = TypedDict(
    "DescribeAlarmModelRequestRequestTypeDef",
    {
        "alarmModelName": str,
        "alarmModelVersion": NotRequired[str],
    },
)
DescribeDetectorModelAnalysisRequestRequestTypeDef = TypedDict(
    "DescribeDetectorModelAnalysisRequestRequestTypeDef",
    {
        "analysisId": str,
    },
)
DescribeDetectorModelRequestRequestTypeDef = TypedDict(
    "DescribeDetectorModelRequestRequestTypeDef",
    {
        "detectorModelName": str,
        "detectorModelVersion": NotRequired[str],
    },
)
DescribeInputRequestRequestTypeDef = TypedDict(
    "DescribeInputRequestRequestTypeDef",
    {
        "inputName": str,
    },
)
DetectorDebugOptionTypeDef = TypedDict(
    "DetectorDebugOptionTypeDef",
    {
        "detectorModelName": str,
        "keyValue": NotRequired[str],
    },
)
DetectorModelSummaryTypeDef = TypedDict(
    "DetectorModelSummaryTypeDef",
    {
        "detectorModelName": NotRequired[str],
        "detectorModelDescription": NotRequired[str],
        "creationTime": NotRequired[datetime],
    },
)
DetectorModelVersionSummaryTypeDef = TypedDict(
    "DetectorModelVersionSummaryTypeDef",
    {
        "detectorModelName": NotRequired[str],
        "detectorModelVersion": NotRequired[str],
        "detectorModelArn": NotRequired[str],
        "roleArn": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "status": NotRequired[DetectorModelVersionStatusType],
        "evaluationMethod": NotRequired[EvaluationMethodType],
    },
)
PayloadTypeDef = TypedDict(
    "PayloadTypeDef",
    {
        "contentExpression": str,
        "type": PayloadTypeType,
    },
)
EmailContentTypeDef = TypedDict(
    "EmailContentTypeDef",
    {
        "subject": NotRequired[str],
        "additionalMessage": NotRequired[str],
    },
)
GetDetectorModelAnalysisResultsRequestRequestTypeDef = TypedDict(
    "GetDetectorModelAnalysisResultsRequestRequestTypeDef",
    {
        "analysisId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
IotEventsInputIdentifierTypeDef = TypedDict(
    "IotEventsInputIdentifierTypeDef",
    {
        "inputName": str,
    },
)
InputSummaryTypeDef = TypedDict(
    "InputSummaryTypeDef",
    {
        "inputName": NotRequired[str],
        "inputDescription": NotRequired[str],
        "inputArn": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "status": NotRequired[InputStatusType],
    },
)
IotSiteWiseAssetModelPropertyIdentifierTypeDef = TypedDict(
    "IotSiteWiseAssetModelPropertyIdentifierTypeDef",
    {
        "assetModelId": str,
        "propertyId": str,
    },
)
ListAlarmModelVersionsRequestRequestTypeDef = TypedDict(
    "ListAlarmModelVersionsRequestRequestTypeDef",
    {
        "alarmModelName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListAlarmModelsRequestRequestTypeDef = TypedDict(
    "ListAlarmModelsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListDetectorModelVersionsRequestRequestTypeDef = TypedDict(
    "ListDetectorModelVersionsRequestRequestTypeDef",
    {
        "detectorModelName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListDetectorModelsRequestRequestTypeDef = TypedDict(
    "ListDetectorModelsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
RoutedResourceTypeDef = TypedDict(
    "RoutedResourceTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
    },
)
ListInputsRequestRequestTypeDef = TypedDict(
    "ListInputsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
SSOIdentityTypeDef = TypedDict(
    "SSOIdentityTypeDef",
    {
        "identityStoreId": str,
        "userId": NotRequired[str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
AlarmCapabilitiesTypeDef = TypedDict(
    "AlarmCapabilitiesTypeDef",
    {
        "initializationConfiguration": NotRequired[InitializationConfigurationTypeDef],
        "acknowledgeFlow": NotRequired[AcknowledgeFlowTypeDef],
    },
)
AlarmRuleTypeDef = TypedDict(
    "AlarmRuleTypeDef",
    {
        "simpleRule": NotRequired[SimpleRuleTypeDef],
    },
)
AnalysisResultTypeDef = TypedDict(
    "AnalysisResultTypeDef",
    {
        "type": NotRequired[str],
        "level": NotRequired[AnalysisResultLevelType],
        "message": NotRequired[str],
        "locations": NotRequired[List[AnalysisResultLocationTypeDef]],
    },
)
AssetPropertyValueTypeDef = TypedDict(
    "AssetPropertyValueTypeDef",
    {
        "value": NotRequired[AssetPropertyVariantTypeDef],
        "timestamp": NotRequired[AssetPropertyTimestampTypeDef],
        "quality": NotRequired[str],
    },
)
InputDefinitionOutputTypeDef = TypedDict(
    "InputDefinitionOutputTypeDef",
    {
        "attributes": List[AttributeTypeDef],
    },
)
InputDefinitionTypeDef = TypedDict(
    "InputDefinitionTypeDef",
    {
        "attributes": Sequence[AttributeTypeDef],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[TagTypeDef],
    },
)
CreateAlarmModelResponseTypeDef = TypedDict(
    "CreateAlarmModelResponseTypeDef",
    {
        "creationTime": datetime,
        "alarmModelArn": str,
        "alarmModelVersion": str,
        "lastUpdateTime": datetime,
        "status": AlarmModelVersionStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDetectorModelAnalysisResponseTypeDef = TypedDict(
    "DescribeDetectorModelAnalysisResponseTypeDef",
    {
        "status": AnalysisStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAlarmModelVersionsResponseTypeDef = TypedDict(
    "ListAlarmModelVersionsResponseTypeDef",
    {
        "alarmModelVersionSummaries": List[AlarmModelVersionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAlarmModelsResponseTypeDef = TypedDict(
    "ListAlarmModelsResponseTypeDef",
    {
        "alarmModelSummaries": List[AlarmModelSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartDetectorModelAnalysisResponseTypeDef = TypedDict(
    "StartDetectorModelAnalysisResponseTypeDef",
    {
        "analysisId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAlarmModelResponseTypeDef = TypedDict(
    "UpdateAlarmModelResponseTypeDef",
    {
        "creationTime": datetime,
        "alarmModelArn": str,
        "alarmModelVersion": str,
        "lastUpdateTime": datetime,
        "status": AlarmModelVersionStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDetectorModelResponseTypeDef = TypedDict(
    "CreateDetectorModelResponseTypeDef",
    {
        "detectorModelConfiguration": DetectorModelConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDetectorModelResponseTypeDef = TypedDict(
    "UpdateDetectorModelResponseTypeDef",
    {
        "detectorModelConfiguration": DetectorModelConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateInputResponseTypeDef = TypedDict(
    "CreateInputResponseTypeDef",
    {
        "inputConfiguration": InputConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateInputResponseTypeDef = TypedDict(
    "UpdateInputResponseTypeDef",
    {
        "inputConfiguration": InputConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LoggingOptionsOutputTypeDef = TypedDict(
    "LoggingOptionsOutputTypeDef",
    {
        "roleArn": str,
        "level": LoggingLevelType,
        "enabled": bool,
        "detectorDebugOptions": NotRequired[List[DetectorDebugOptionTypeDef]],
    },
)
LoggingOptionsTypeDef = TypedDict(
    "LoggingOptionsTypeDef",
    {
        "roleArn": str,
        "level": LoggingLevelType,
        "enabled": bool,
        "detectorDebugOptions": NotRequired[Sequence[DetectorDebugOptionTypeDef]],
    },
)
ListDetectorModelsResponseTypeDef = TypedDict(
    "ListDetectorModelsResponseTypeDef",
    {
        "detectorModelSummaries": List[DetectorModelSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDetectorModelVersionsResponseTypeDef = TypedDict(
    "ListDetectorModelVersionsResponseTypeDef",
    {
        "detectorModelVersionSummaries": List[DetectorModelVersionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DynamoDBActionTypeDef = TypedDict(
    "DynamoDBActionTypeDef",
    {
        "hashKeyField": str,
        "hashKeyValue": str,
        "tableName": str,
        "hashKeyType": NotRequired[str],
        "rangeKeyType": NotRequired[str],
        "rangeKeyField": NotRequired[str],
        "rangeKeyValue": NotRequired[str],
        "operation": NotRequired[str],
        "payloadField": NotRequired[str],
        "payload": NotRequired[PayloadTypeDef],
    },
)
DynamoDBv2ActionTypeDef = TypedDict(
    "DynamoDBv2ActionTypeDef",
    {
        "tableName": str,
        "payload": NotRequired[PayloadTypeDef],
    },
)
FirehoseActionTypeDef = TypedDict(
    "FirehoseActionTypeDef",
    {
        "deliveryStreamName": str,
        "separator": NotRequired[str],
        "payload": NotRequired[PayloadTypeDef],
    },
)
IotEventsActionTypeDef = TypedDict(
    "IotEventsActionTypeDef",
    {
        "inputName": str,
        "payload": NotRequired[PayloadTypeDef],
    },
)
IotTopicPublishActionTypeDef = TypedDict(
    "IotTopicPublishActionTypeDef",
    {
        "mqttTopic": str,
        "payload": NotRequired[PayloadTypeDef],
    },
)
LambdaActionTypeDef = TypedDict(
    "LambdaActionTypeDef",
    {
        "functionArn": str,
        "payload": NotRequired[PayloadTypeDef],
    },
)
SNSTopicPublishActionTypeDef = TypedDict(
    "SNSTopicPublishActionTypeDef",
    {
        "targetArn": str,
        "payload": NotRequired[PayloadTypeDef],
    },
)
SqsActionTypeDef = TypedDict(
    "SqsActionTypeDef",
    {
        "queueUrl": str,
        "useBase64": NotRequired[bool],
        "payload": NotRequired[PayloadTypeDef],
    },
)
ListInputsResponseTypeDef = TypedDict(
    "ListInputsResponseTypeDef",
    {
        "inputSummaries": List[InputSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IotSiteWiseInputIdentifierTypeDef = TypedDict(
    "IotSiteWiseInputIdentifierTypeDef",
    {
        "iotSiteWiseAssetModelPropertyIdentifier": NotRequired[
            IotSiteWiseAssetModelPropertyIdentifierTypeDef
        ],
    },
)
ListInputRoutingsResponseTypeDef = TypedDict(
    "ListInputRoutingsResponseTypeDef",
    {
        "routedResources": List[RoutedResourceTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RecipientDetailTypeDef = TypedDict(
    "RecipientDetailTypeDef",
    {
        "ssoIdentity": NotRequired[SSOIdentityTypeDef],
    },
)
GetDetectorModelAnalysisResultsResponseTypeDef = TypedDict(
    "GetDetectorModelAnalysisResultsResponseTypeDef",
    {
        "analysisResults": List[AnalysisResultTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IotSiteWiseActionTypeDef = TypedDict(
    "IotSiteWiseActionTypeDef",
    {
        "entryId": NotRequired[str],
        "assetId": NotRequired[str],
        "propertyId": NotRequired[str],
        "propertyAlias": NotRequired[str],
        "propertyValue": NotRequired[AssetPropertyValueTypeDef],
    },
)
InputTypeDef = TypedDict(
    "InputTypeDef",
    {
        "inputConfiguration": NotRequired[InputConfigurationTypeDef],
        "inputDefinition": NotRequired[InputDefinitionOutputTypeDef],
    },
)
CreateInputRequestRequestTypeDef = TypedDict(
    "CreateInputRequestRequestTypeDef",
    {
        "inputName": str,
        "inputDefinition": InputDefinitionTypeDef,
        "inputDescription": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
UpdateInputRequestRequestTypeDef = TypedDict(
    "UpdateInputRequestRequestTypeDef",
    {
        "inputName": str,
        "inputDefinition": InputDefinitionTypeDef,
        "inputDescription": NotRequired[str],
    },
)
DescribeLoggingOptionsResponseTypeDef = TypedDict(
    "DescribeLoggingOptionsResponseTypeDef",
    {
        "loggingOptions": LoggingOptionsOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutLoggingOptionsRequestRequestTypeDef = TypedDict(
    "PutLoggingOptionsRequestRequestTypeDef",
    {
        "loggingOptions": LoggingOptionsTypeDef,
    },
)
NotificationTargetActionsTypeDef = TypedDict(
    "NotificationTargetActionsTypeDef",
    {
        "lambdaAction": NotRequired[LambdaActionTypeDef],
    },
)
InputIdentifierTypeDef = TypedDict(
    "InputIdentifierTypeDef",
    {
        "iotEventsInputIdentifier": NotRequired[IotEventsInputIdentifierTypeDef],
        "iotSiteWiseInputIdentifier": NotRequired[IotSiteWiseInputIdentifierTypeDef],
    },
)
EmailRecipientsOutputTypeDef = TypedDict(
    "EmailRecipientsOutputTypeDef",
    {
        "to": NotRequired[List[RecipientDetailTypeDef]],
    },
)
EmailRecipientsTypeDef = TypedDict(
    "EmailRecipientsTypeDef",
    {
        "to": NotRequired[Sequence[RecipientDetailTypeDef]],
    },
)
SMSConfigurationOutputTypeDef = TypedDict(
    "SMSConfigurationOutputTypeDef",
    {
        "recipients": List[RecipientDetailTypeDef],
        "senderId": NotRequired[str],
        "additionalMessage": NotRequired[str],
    },
)
SMSConfigurationTypeDef = TypedDict(
    "SMSConfigurationTypeDef",
    {
        "recipients": Sequence[RecipientDetailTypeDef],
        "senderId": NotRequired[str],
        "additionalMessage": NotRequired[str],
    },
)
ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "setVariable": NotRequired[SetVariableActionTypeDef],
        "sns": NotRequired[SNSTopicPublishActionTypeDef],
        "iotTopicPublish": NotRequired[IotTopicPublishActionTypeDef],
        "setTimer": NotRequired[SetTimerActionTypeDef],
        "clearTimer": NotRequired[ClearTimerActionTypeDef],
        "resetTimer": NotRequired[ResetTimerActionTypeDef],
        "lambda": NotRequired[LambdaActionTypeDef],
        "iotEvents": NotRequired[IotEventsActionTypeDef],
        "sqs": NotRequired[SqsActionTypeDef],
        "firehose": NotRequired[FirehoseActionTypeDef],
        "dynamoDB": NotRequired[DynamoDBActionTypeDef],
        "dynamoDBv2": NotRequired[DynamoDBv2ActionTypeDef],
        "iotSiteWise": NotRequired[IotSiteWiseActionTypeDef],
    },
)
AlarmActionTypeDef = TypedDict(
    "AlarmActionTypeDef",
    {
        "sns": NotRequired[SNSTopicPublishActionTypeDef],
        "iotTopicPublish": NotRequired[IotTopicPublishActionTypeDef],
        "lambda": NotRequired[LambdaActionTypeDef],
        "iotEvents": NotRequired[IotEventsActionTypeDef],
        "sqs": NotRequired[SqsActionTypeDef],
        "firehose": NotRequired[FirehoseActionTypeDef],
        "dynamoDB": NotRequired[DynamoDBActionTypeDef],
        "dynamoDBv2": NotRequired[DynamoDBv2ActionTypeDef],
        "iotSiteWise": NotRequired[IotSiteWiseActionTypeDef],
    },
)
DescribeInputResponseTypeDef = TypedDict(
    "DescribeInputResponseTypeDef",
    {
        "input": InputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListInputRoutingsRequestRequestTypeDef = TypedDict(
    "ListInputRoutingsRequestRequestTypeDef",
    {
        "inputIdentifier": InputIdentifierTypeDef,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
EmailConfigurationOutputTypeDef = TypedDict(
    "EmailConfigurationOutputTypeDef",
    {
        "from": str,
        "recipients": EmailRecipientsOutputTypeDef,
        "content": NotRequired[EmailContentTypeDef],
    },
)
EmailRecipientsUnionTypeDef = Union[EmailRecipientsTypeDef, EmailRecipientsOutputTypeDef]
SMSConfigurationUnionTypeDef = Union[SMSConfigurationTypeDef, SMSConfigurationOutputTypeDef]
EventOutputTypeDef = TypedDict(
    "EventOutputTypeDef",
    {
        "eventName": str,
        "condition": NotRequired[str],
        "actions": NotRequired[List[ActionTypeDef]],
    },
)
EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "eventName": str,
        "condition": NotRequired[str],
        "actions": NotRequired[Sequence[ActionTypeDef]],
    },
)
TransitionEventOutputTypeDef = TypedDict(
    "TransitionEventOutputTypeDef",
    {
        "eventName": str,
        "condition": str,
        "nextState": str,
        "actions": NotRequired[List[ActionTypeDef]],
    },
)
TransitionEventTypeDef = TypedDict(
    "TransitionEventTypeDef",
    {
        "eventName": str,
        "condition": str,
        "nextState": str,
        "actions": NotRequired[Sequence[ActionTypeDef]],
    },
)
AlarmEventActionsOutputTypeDef = TypedDict(
    "AlarmEventActionsOutputTypeDef",
    {
        "alarmActions": NotRequired[List[AlarmActionTypeDef]],
    },
)
AlarmEventActionsTypeDef = TypedDict(
    "AlarmEventActionsTypeDef",
    {
        "alarmActions": NotRequired[Sequence[AlarmActionTypeDef]],
    },
)
NotificationActionOutputTypeDef = TypedDict(
    "NotificationActionOutputTypeDef",
    {
        "action": NotificationTargetActionsTypeDef,
        "smsConfigurations": NotRequired[List[SMSConfigurationOutputTypeDef]],
        "emailConfigurations": NotRequired[List[EmailConfigurationOutputTypeDef]],
    },
)
EmailConfigurationTypeDef = TypedDict(
    "EmailConfigurationTypeDef",
    {
        "from": str,
        "recipients": EmailRecipientsUnionTypeDef,
        "content": NotRequired[EmailContentTypeDef],
    },
)
OnEnterLifecycleOutputTypeDef = TypedDict(
    "OnEnterLifecycleOutputTypeDef",
    {
        "events": NotRequired[List[EventOutputTypeDef]],
    },
)
OnExitLifecycleOutputTypeDef = TypedDict(
    "OnExitLifecycleOutputTypeDef",
    {
        "events": NotRequired[List[EventOutputTypeDef]],
    },
)
EventUnionTypeDef = Union[EventTypeDef, EventOutputTypeDef]
OnEnterLifecycleTypeDef = TypedDict(
    "OnEnterLifecycleTypeDef",
    {
        "events": NotRequired[Sequence[EventTypeDef]],
    },
)
OnExitLifecycleTypeDef = TypedDict(
    "OnExitLifecycleTypeDef",
    {
        "events": NotRequired[Sequence[EventTypeDef]],
    },
)
OnInputLifecycleOutputTypeDef = TypedDict(
    "OnInputLifecycleOutputTypeDef",
    {
        "events": NotRequired[List[EventOutputTypeDef]],
        "transitionEvents": NotRequired[List[TransitionEventOutputTypeDef]],
    },
)
TransitionEventUnionTypeDef = Union[TransitionEventTypeDef, TransitionEventOutputTypeDef]
AlarmNotificationOutputTypeDef = TypedDict(
    "AlarmNotificationOutputTypeDef",
    {
        "notificationActions": NotRequired[List[NotificationActionOutputTypeDef]],
    },
)
EmailConfigurationUnionTypeDef = Union[EmailConfigurationTypeDef, EmailConfigurationOutputTypeDef]
OnEnterLifecycleUnionTypeDef = Union[OnEnterLifecycleTypeDef, OnEnterLifecycleOutputTypeDef]
OnExitLifecycleUnionTypeDef = Union[OnExitLifecycleTypeDef, OnExitLifecycleOutputTypeDef]
StateOutputTypeDef = TypedDict(
    "StateOutputTypeDef",
    {
        "stateName": str,
        "onInput": NotRequired[OnInputLifecycleOutputTypeDef],
        "onEnter": NotRequired[OnEnterLifecycleOutputTypeDef],
        "onExit": NotRequired[OnExitLifecycleOutputTypeDef],
    },
)
OnInputLifecycleTypeDef = TypedDict(
    "OnInputLifecycleTypeDef",
    {
        "events": NotRequired[Sequence[EventUnionTypeDef]],
        "transitionEvents": NotRequired[Sequence[TransitionEventUnionTypeDef]],
    },
)
DescribeAlarmModelResponseTypeDef = TypedDict(
    "DescribeAlarmModelResponseTypeDef",
    {
        "creationTime": datetime,
        "alarmModelArn": str,
        "alarmModelVersion": str,
        "lastUpdateTime": datetime,
        "status": AlarmModelVersionStatusType,
        "statusMessage": str,
        "alarmModelName": str,
        "alarmModelDescription": str,
        "roleArn": str,
        "key": str,
        "severity": int,
        "alarmRule": AlarmRuleTypeDef,
        "alarmNotification": AlarmNotificationOutputTypeDef,
        "alarmEventActions": AlarmEventActionsOutputTypeDef,
        "alarmCapabilities": AlarmCapabilitiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NotificationActionTypeDef = TypedDict(
    "NotificationActionTypeDef",
    {
        "action": NotificationTargetActionsTypeDef,
        "smsConfigurations": NotRequired[Sequence[SMSConfigurationUnionTypeDef]],
        "emailConfigurations": NotRequired[Sequence[EmailConfigurationUnionTypeDef]],
    },
)
DetectorModelDefinitionOutputTypeDef = TypedDict(
    "DetectorModelDefinitionOutputTypeDef",
    {
        "states": List[StateOutputTypeDef],
        "initialStateName": str,
    },
)
OnInputLifecycleUnionTypeDef = Union[OnInputLifecycleTypeDef, OnInputLifecycleOutputTypeDef]
NotificationActionUnionTypeDef = Union[NotificationActionTypeDef, NotificationActionOutputTypeDef]
DetectorModelTypeDef = TypedDict(
    "DetectorModelTypeDef",
    {
        "detectorModelDefinition": NotRequired[DetectorModelDefinitionOutputTypeDef],
        "detectorModelConfiguration": NotRequired[DetectorModelConfigurationTypeDef],
    },
)
StateTypeDef = TypedDict(
    "StateTypeDef",
    {
        "stateName": str,
        "onInput": NotRequired[OnInputLifecycleUnionTypeDef],
        "onEnter": NotRequired[OnEnterLifecycleUnionTypeDef],
        "onExit": NotRequired[OnExitLifecycleUnionTypeDef],
    },
)
AlarmNotificationTypeDef = TypedDict(
    "AlarmNotificationTypeDef",
    {
        "notificationActions": NotRequired[Sequence[NotificationActionUnionTypeDef]],
    },
)
DescribeDetectorModelResponseTypeDef = TypedDict(
    "DescribeDetectorModelResponseTypeDef",
    {
        "detectorModel": DetectorModelTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StateUnionTypeDef = Union[StateTypeDef, StateOutputTypeDef]
CreateAlarmModelRequestRequestTypeDef = TypedDict(
    "CreateAlarmModelRequestRequestTypeDef",
    {
        "alarmModelName": str,
        "roleArn": str,
        "alarmRule": AlarmRuleTypeDef,
        "alarmModelDescription": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "key": NotRequired[str],
        "severity": NotRequired[int],
        "alarmNotification": NotRequired[AlarmNotificationTypeDef],
        "alarmEventActions": NotRequired[AlarmEventActionsTypeDef],
        "alarmCapabilities": NotRequired[AlarmCapabilitiesTypeDef],
    },
)
UpdateAlarmModelRequestRequestTypeDef = TypedDict(
    "UpdateAlarmModelRequestRequestTypeDef",
    {
        "alarmModelName": str,
        "roleArn": str,
        "alarmRule": AlarmRuleTypeDef,
        "alarmModelDescription": NotRequired[str],
        "severity": NotRequired[int],
        "alarmNotification": NotRequired[AlarmNotificationTypeDef],
        "alarmEventActions": NotRequired[AlarmEventActionsTypeDef],
        "alarmCapabilities": NotRequired[AlarmCapabilitiesTypeDef],
    },
)
DetectorModelDefinitionTypeDef = TypedDict(
    "DetectorModelDefinitionTypeDef",
    {
        "states": Sequence[StateUnionTypeDef],
        "initialStateName": str,
    },
)
CreateDetectorModelRequestRequestTypeDef = TypedDict(
    "CreateDetectorModelRequestRequestTypeDef",
    {
        "detectorModelName": str,
        "detectorModelDefinition": DetectorModelDefinitionTypeDef,
        "roleArn": str,
        "detectorModelDescription": NotRequired[str],
        "key": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "evaluationMethod": NotRequired[EvaluationMethodType],
    },
)
StartDetectorModelAnalysisRequestRequestTypeDef = TypedDict(
    "StartDetectorModelAnalysisRequestRequestTypeDef",
    {
        "detectorModelDefinition": DetectorModelDefinitionTypeDef,
    },
)
UpdateDetectorModelRequestRequestTypeDef = TypedDict(
    "UpdateDetectorModelRequestRequestTypeDef",
    {
        "detectorModelName": str,
        "detectorModelDefinition": DetectorModelDefinitionTypeDef,
        "roleArn": str,
        "detectorModelDescription": NotRequired[str],
        "evaluationMethod": NotRequired[EvaluationMethodType],
    },
)
