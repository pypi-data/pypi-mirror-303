"""
Type annotations for lex-runtime service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_runtime/type_defs/)

Usage::

    ```python
    from mypy_boto3_lex_runtime.type_defs import ActiveContextTimeToLiveTypeDef

    data: ActiveContextTimeToLiveTypeDef = ...
    ```
"""

import sys
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    ConfirmationStatusType,
    DialogActionTypeType,
    DialogStateType,
    FulfillmentStateType,
    MessageFormatTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "ActiveContextTimeToLiveTypeDef",
    "BlobTypeDef",
    "ButtonTypeDef",
    "DeleteSessionRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "DialogActionOutputTypeDef",
    "DialogActionTypeDef",
    "GetSessionRequestRequestTypeDef",
    "IntentSummaryOutputTypeDef",
    "IntentConfidenceTypeDef",
    "IntentSummaryTypeDef",
    "SentimentResponseTypeDef",
    "ActiveContextOutputTypeDef",
    "ActiveContextTypeDef",
    "PostContentRequestRequestTypeDef",
    "GenericAttachmentTypeDef",
    "DeleteSessionResponseTypeDef",
    "PostContentResponseTypeDef",
    "PutSessionResponseTypeDef",
    "PredictedIntentTypeDef",
    "IntentSummaryUnionTypeDef",
    "GetSessionResponseTypeDef",
    "ActiveContextUnionTypeDef",
    "ResponseCardTypeDef",
    "PutSessionRequestRequestTypeDef",
    "PostTextRequestRequestTypeDef",
    "PostTextResponseTypeDef",
)

ActiveContextTimeToLiveTypeDef = TypedDict(
    "ActiveContextTimeToLiveTypeDef",
    {
        "timeToLiveInSeconds": NotRequired[int],
        "turnsToLive": NotRequired[int],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
ButtonTypeDef = TypedDict(
    "ButtonTypeDef",
    {
        "text": str,
        "value": str,
    },
)
DeleteSessionRequestRequestTypeDef = TypedDict(
    "DeleteSessionRequestRequestTypeDef",
    {
        "botName": str,
        "botAlias": str,
        "userId": str,
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
DialogActionOutputTypeDef = TypedDict(
    "DialogActionOutputTypeDef",
    {
        "type": DialogActionTypeType,
        "intentName": NotRequired[str],
        "slots": NotRequired[Dict[str, str]],
        "slotToElicit": NotRequired[str],
        "fulfillmentState": NotRequired[FulfillmentStateType],
        "message": NotRequired[str],
        "messageFormat": NotRequired[MessageFormatTypeType],
    },
)
DialogActionTypeDef = TypedDict(
    "DialogActionTypeDef",
    {
        "type": DialogActionTypeType,
        "intentName": NotRequired[str],
        "slots": NotRequired[Mapping[str, str]],
        "slotToElicit": NotRequired[str],
        "fulfillmentState": NotRequired[FulfillmentStateType],
        "message": NotRequired[str],
        "messageFormat": NotRequired[MessageFormatTypeType],
    },
)
GetSessionRequestRequestTypeDef = TypedDict(
    "GetSessionRequestRequestTypeDef",
    {
        "botName": str,
        "botAlias": str,
        "userId": str,
        "checkpointLabelFilter": NotRequired[str],
    },
)
IntentSummaryOutputTypeDef = TypedDict(
    "IntentSummaryOutputTypeDef",
    {
        "dialogActionType": DialogActionTypeType,
        "intentName": NotRequired[str],
        "checkpointLabel": NotRequired[str],
        "slots": NotRequired[Dict[str, str]],
        "confirmationStatus": NotRequired[ConfirmationStatusType],
        "fulfillmentState": NotRequired[FulfillmentStateType],
        "slotToElicit": NotRequired[str],
    },
)
IntentConfidenceTypeDef = TypedDict(
    "IntentConfidenceTypeDef",
    {
        "score": NotRequired[float],
    },
)
IntentSummaryTypeDef = TypedDict(
    "IntentSummaryTypeDef",
    {
        "dialogActionType": DialogActionTypeType,
        "intentName": NotRequired[str],
        "checkpointLabel": NotRequired[str],
        "slots": NotRequired[Mapping[str, str]],
        "confirmationStatus": NotRequired[ConfirmationStatusType],
        "fulfillmentState": NotRequired[FulfillmentStateType],
        "slotToElicit": NotRequired[str],
    },
)
SentimentResponseTypeDef = TypedDict(
    "SentimentResponseTypeDef",
    {
        "sentimentLabel": NotRequired[str],
        "sentimentScore": NotRequired[str],
    },
)
ActiveContextOutputTypeDef = TypedDict(
    "ActiveContextOutputTypeDef",
    {
        "name": str,
        "timeToLive": ActiveContextTimeToLiveTypeDef,
        "parameters": Dict[str, str],
    },
)
ActiveContextTypeDef = TypedDict(
    "ActiveContextTypeDef",
    {
        "name": str,
        "timeToLive": ActiveContextTimeToLiveTypeDef,
        "parameters": Mapping[str, str],
    },
)
PostContentRequestRequestTypeDef = TypedDict(
    "PostContentRequestRequestTypeDef",
    {
        "botName": str,
        "botAlias": str,
        "userId": str,
        "contentType": str,
        "inputStream": BlobTypeDef,
        "sessionAttributes": NotRequired[str],
        "requestAttributes": NotRequired[str],
        "accept": NotRequired[str],
        "activeContexts": NotRequired[str],
    },
)
GenericAttachmentTypeDef = TypedDict(
    "GenericAttachmentTypeDef",
    {
        "title": NotRequired[str],
        "subTitle": NotRequired[str],
        "attachmentLinkUrl": NotRequired[str],
        "imageUrl": NotRequired[str],
        "buttons": NotRequired[List[ButtonTypeDef]],
    },
)
DeleteSessionResponseTypeDef = TypedDict(
    "DeleteSessionResponseTypeDef",
    {
        "botName": str,
        "botAlias": str,
        "userId": str,
        "sessionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PostContentResponseTypeDef = TypedDict(
    "PostContentResponseTypeDef",
    {
        "contentType": str,
        "intentName": str,
        "nluIntentConfidence": str,
        "alternativeIntents": str,
        "slots": str,
        "sessionAttributes": str,
        "sentimentResponse": str,
        "message": str,
        "encodedMessage": str,
        "messageFormat": MessageFormatTypeType,
        "dialogState": DialogStateType,
        "slotToElicit": str,
        "inputTranscript": str,
        "encodedInputTranscript": str,
        "audioStream": StreamingBody,
        "botVersion": str,
        "sessionId": str,
        "activeContexts": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutSessionResponseTypeDef = TypedDict(
    "PutSessionResponseTypeDef",
    {
        "contentType": str,
        "intentName": str,
        "slots": str,
        "sessionAttributes": str,
        "message": str,
        "encodedMessage": str,
        "messageFormat": MessageFormatTypeType,
        "dialogState": DialogStateType,
        "slotToElicit": str,
        "audioStream": StreamingBody,
        "sessionId": str,
        "activeContexts": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PredictedIntentTypeDef = TypedDict(
    "PredictedIntentTypeDef",
    {
        "intentName": NotRequired[str],
        "nluIntentConfidence": NotRequired[IntentConfidenceTypeDef],
        "slots": NotRequired[Dict[str, str]],
    },
)
IntentSummaryUnionTypeDef = Union[IntentSummaryTypeDef, IntentSummaryOutputTypeDef]
GetSessionResponseTypeDef = TypedDict(
    "GetSessionResponseTypeDef",
    {
        "recentIntentSummaryView": List[IntentSummaryOutputTypeDef],
        "sessionAttributes": Dict[str, str],
        "sessionId": str,
        "dialogAction": DialogActionOutputTypeDef,
        "activeContexts": List[ActiveContextOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ActiveContextUnionTypeDef = Union[ActiveContextTypeDef, ActiveContextOutputTypeDef]
ResponseCardTypeDef = TypedDict(
    "ResponseCardTypeDef",
    {
        "version": NotRequired[str],
        "contentType": NotRequired[Literal["application/vnd.amazonaws.card.generic"]],
        "genericAttachments": NotRequired[List[GenericAttachmentTypeDef]],
    },
)
PutSessionRequestRequestTypeDef = TypedDict(
    "PutSessionRequestRequestTypeDef",
    {
        "botName": str,
        "botAlias": str,
        "userId": str,
        "sessionAttributes": NotRequired[Mapping[str, str]],
        "dialogAction": NotRequired[DialogActionTypeDef],
        "recentIntentSummaryView": NotRequired[Sequence[IntentSummaryUnionTypeDef]],
        "accept": NotRequired[str],
        "activeContexts": NotRequired[Sequence[ActiveContextTypeDef]],
    },
)
PostTextRequestRequestTypeDef = TypedDict(
    "PostTextRequestRequestTypeDef",
    {
        "botName": str,
        "botAlias": str,
        "userId": str,
        "inputText": str,
        "sessionAttributes": NotRequired[Mapping[str, str]],
        "requestAttributes": NotRequired[Mapping[str, str]],
        "activeContexts": NotRequired[Sequence[ActiveContextUnionTypeDef]],
    },
)
PostTextResponseTypeDef = TypedDict(
    "PostTextResponseTypeDef",
    {
        "intentName": str,
        "nluIntentConfidence": IntentConfidenceTypeDef,
        "alternativeIntents": List[PredictedIntentTypeDef],
        "slots": Dict[str, str],
        "sessionAttributes": Dict[str, str],
        "message": str,
        "sentimentResponse": SentimentResponseTypeDef,
        "messageFormat": MessageFormatTypeType,
        "dialogState": DialogStateType,
        "slotToElicit": str,
        "responseCard": ResponseCardTypeDef,
        "sessionId": str,
        "botVersion": str,
        "activeContexts": List[ActiveContextOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
