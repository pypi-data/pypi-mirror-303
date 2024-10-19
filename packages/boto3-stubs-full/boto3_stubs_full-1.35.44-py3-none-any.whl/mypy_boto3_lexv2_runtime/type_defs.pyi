"""
Type annotations for lexv2-runtime service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_runtime/type_defs/)

Usage::

    ```python
    from mypy_boto3_lexv2_runtime.type_defs import ActiveContextTimeToLiveTypeDef

    data: ActiveContextTimeToLiveTypeDef = ...
    ```
"""

import sys
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    ConfirmationStateType,
    DialogActionTypeType,
    IntentStateType,
    InterpretationSourceType,
    MessageContentTypeType,
    SentimentTypeType,
    ShapeType,
    StyleTypeType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "ActiveContextTimeToLiveTypeDef",
    "BlobTypeDef",
    "ButtonTypeDef",
    "ConfidenceScoreTypeDef",
    "DeleteSessionRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "ElicitSubSlotOutputTypeDef",
    "ElicitSubSlotTypeDef",
    "GetSessionRequestRequestTypeDef",
    "RecognizedBotMemberTypeDef",
    "RuntimeHintValueTypeDef",
    "SentimentScoreTypeDef",
    "ValueOutputTypeDef",
    "ValueTypeDef",
    "ActiveContextOutputTypeDef",
    "ActiveContextTypeDef",
    "RecognizeUtteranceRequestRequestTypeDef",
    "ImageResponseCardOutputTypeDef",
    "ImageResponseCardTypeDef",
    "DeleteSessionResponseTypeDef",
    "PutSessionResponseTypeDef",
    "RecognizeUtteranceResponseTypeDef",
    "DialogActionOutputTypeDef",
    "ElicitSubSlotUnionTypeDef",
    "RuntimeHintDetailsOutputTypeDef",
    "RuntimeHintDetailsTypeDef",
    "SentimentResponseTypeDef",
    "SlotOutputTypeDef",
    "ValueUnionTypeDef",
    "ActiveContextUnionTypeDef",
    "MessageOutputTypeDef",
    "ImageResponseCardUnionTypeDef",
    "DialogActionTypeDef",
    "RuntimeHintsOutputTypeDef",
    "RuntimeHintDetailsUnionTypeDef",
    "IntentOutputTypeDef",
    "SlotTypeDef",
    "MessageTypeDef",
    "DialogActionUnionTypeDef",
    "RuntimeHintsTypeDef",
    "InterpretationTypeDef",
    "SessionStateOutputTypeDef",
    "SlotUnionTypeDef",
    "MessageUnionTypeDef",
    "RuntimeHintsUnionTypeDef",
    "GetSessionResponseTypeDef",
    "RecognizeTextResponseTypeDef",
    "IntentTypeDef",
    "IntentUnionTypeDef",
    "SessionStateTypeDef",
    "PutSessionRequestRequestTypeDef",
    "RecognizeTextRequestRequestTypeDef",
)

ActiveContextTimeToLiveTypeDef = TypedDict(
    "ActiveContextTimeToLiveTypeDef",
    {
        "timeToLiveInSeconds": int,
        "turnsToLive": int,
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
ConfidenceScoreTypeDef = TypedDict(
    "ConfidenceScoreTypeDef",
    {
        "score": NotRequired[float],
    },
)
DeleteSessionRequestRequestTypeDef = TypedDict(
    "DeleteSessionRequestRequestTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
        "sessionId": str,
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
ElicitSubSlotOutputTypeDef = TypedDict(
    "ElicitSubSlotOutputTypeDef",
    {
        "name": str,
        "subSlotToElicit": NotRequired[Dict[str, Any]],
    },
)
ElicitSubSlotTypeDef = TypedDict(
    "ElicitSubSlotTypeDef",
    {
        "name": str,
        "subSlotToElicit": NotRequired[Mapping[str, Any]],
    },
)
GetSessionRequestRequestTypeDef = TypedDict(
    "GetSessionRequestRequestTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
        "sessionId": str,
    },
)
RecognizedBotMemberTypeDef = TypedDict(
    "RecognizedBotMemberTypeDef",
    {
        "botId": str,
        "botName": NotRequired[str],
    },
)
RuntimeHintValueTypeDef = TypedDict(
    "RuntimeHintValueTypeDef",
    {
        "phrase": str,
    },
)
SentimentScoreTypeDef = TypedDict(
    "SentimentScoreTypeDef",
    {
        "positive": NotRequired[float],
        "negative": NotRequired[float],
        "neutral": NotRequired[float],
        "mixed": NotRequired[float],
    },
)
ValueOutputTypeDef = TypedDict(
    "ValueOutputTypeDef",
    {
        "interpretedValue": str,
        "originalValue": NotRequired[str],
        "resolvedValues": NotRequired[List[str]],
    },
)
ValueTypeDef = TypedDict(
    "ValueTypeDef",
    {
        "interpretedValue": str,
        "originalValue": NotRequired[str],
        "resolvedValues": NotRequired[Sequence[str]],
    },
)
ActiveContextOutputTypeDef = TypedDict(
    "ActiveContextOutputTypeDef",
    {
        "name": str,
        "timeToLive": ActiveContextTimeToLiveTypeDef,
        "contextAttributes": Dict[str, str],
    },
)
ActiveContextTypeDef = TypedDict(
    "ActiveContextTypeDef",
    {
        "name": str,
        "timeToLive": ActiveContextTimeToLiveTypeDef,
        "contextAttributes": Mapping[str, str],
    },
)
RecognizeUtteranceRequestRequestTypeDef = TypedDict(
    "RecognizeUtteranceRequestRequestTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
        "sessionId": str,
        "requestContentType": str,
        "sessionState": NotRequired[str],
        "requestAttributes": NotRequired[str],
        "responseContentType": NotRequired[str],
        "inputStream": NotRequired[BlobTypeDef],
    },
)
ImageResponseCardOutputTypeDef = TypedDict(
    "ImageResponseCardOutputTypeDef",
    {
        "title": str,
        "subtitle": NotRequired[str],
        "imageUrl": NotRequired[str],
        "buttons": NotRequired[List[ButtonTypeDef]],
    },
)
ImageResponseCardTypeDef = TypedDict(
    "ImageResponseCardTypeDef",
    {
        "title": str,
        "subtitle": NotRequired[str],
        "imageUrl": NotRequired[str],
        "buttons": NotRequired[Sequence[ButtonTypeDef]],
    },
)
DeleteSessionResponseTypeDef = TypedDict(
    "DeleteSessionResponseTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
        "sessionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutSessionResponseTypeDef = TypedDict(
    "PutSessionResponseTypeDef",
    {
        "contentType": str,
        "messages": str,
        "sessionState": str,
        "requestAttributes": str,
        "sessionId": str,
        "audioStream": StreamingBody,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RecognizeUtteranceResponseTypeDef = TypedDict(
    "RecognizeUtteranceResponseTypeDef",
    {
        "inputMode": str,
        "contentType": str,
        "messages": str,
        "interpretations": str,
        "sessionState": str,
        "requestAttributes": str,
        "sessionId": str,
        "inputTranscript": str,
        "audioStream": StreamingBody,
        "recognizedBotMember": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DialogActionOutputTypeDef = TypedDict(
    "DialogActionOutputTypeDef",
    {
        "type": DialogActionTypeType,
        "slotToElicit": NotRequired[str],
        "slotElicitationStyle": NotRequired[StyleTypeType],
        "subSlotToElicit": NotRequired[ElicitSubSlotOutputTypeDef],
    },
)
ElicitSubSlotUnionTypeDef = Union[ElicitSubSlotTypeDef, ElicitSubSlotOutputTypeDef]
RuntimeHintDetailsOutputTypeDef = TypedDict(
    "RuntimeHintDetailsOutputTypeDef",
    {
        "runtimeHintValues": NotRequired[List[RuntimeHintValueTypeDef]],
        "subSlotHints": NotRequired[Dict[str, Dict[str, Any]]],
    },
)
RuntimeHintDetailsTypeDef = TypedDict(
    "RuntimeHintDetailsTypeDef",
    {
        "runtimeHintValues": NotRequired[Sequence[RuntimeHintValueTypeDef]],
        "subSlotHints": NotRequired[Mapping[str, Mapping[str, Any]]],
    },
)
SentimentResponseTypeDef = TypedDict(
    "SentimentResponseTypeDef",
    {
        "sentiment": NotRequired[SentimentTypeType],
        "sentimentScore": NotRequired[SentimentScoreTypeDef],
    },
)
SlotOutputTypeDef = TypedDict(
    "SlotOutputTypeDef",
    {
        "value": NotRequired[ValueOutputTypeDef],
        "shape": NotRequired[ShapeType],
        "values": NotRequired[List[Dict[str, Any]]],
        "subSlots": NotRequired[Dict[str, Dict[str, Any]]],
    },
)
ValueUnionTypeDef = Union[ValueTypeDef, ValueOutputTypeDef]
ActiveContextUnionTypeDef = Union[ActiveContextTypeDef, ActiveContextOutputTypeDef]
MessageOutputTypeDef = TypedDict(
    "MessageOutputTypeDef",
    {
        "contentType": MessageContentTypeType,
        "content": NotRequired[str],
        "imageResponseCard": NotRequired[ImageResponseCardOutputTypeDef],
    },
)
ImageResponseCardUnionTypeDef = Union[ImageResponseCardTypeDef, ImageResponseCardOutputTypeDef]
DialogActionTypeDef = TypedDict(
    "DialogActionTypeDef",
    {
        "type": DialogActionTypeType,
        "slotToElicit": NotRequired[str],
        "slotElicitationStyle": NotRequired[StyleTypeType],
        "subSlotToElicit": NotRequired[ElicitSubSlotUnionTypeDef],
    },
)
RuntimeHintsOutputTypeDef = TypedDict(
    "RuntimeHintsOutputTypeDef",
    {
        "slotHints": NotRequired[Dict[str, Dict[str, RuntimeHintDetailsOutputTypeDef]]],
    },
)
RuntimeHintDetailsUnionTypeDef = Union[RuntimeHintDetailsTypeDef, RuntimeHintDetailsOutputTypeDef]
IntentOutputTypeDef = TypedDict(
    "IntentOutputTypeDef",
    {
        "name": str,
        "slots": NotRequired[Dict[str, SlotOutputTypeDef]],
        "state": NotRequired[IntentStateType],
        "confirmationState": NotRequired[ConfirmationStateType],
    },
)
SlotTypeDef = TypedDict(
    "SlotTypeDef",
    {
        "value": NotRequired[ValueUnionTypeDef],
        "shape": NotRequired[ShapeType],
        "values": NotRequired[Sequence[Mapping[str, Any]]],
        "subSlots": NotRequired[Mapping[str, Mapping[str, Any]]],
    },
)
MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "contentType": MessageContentTypeType,
        "content": NotRequired[str],
        "imageResponseCard": NotRequired[ImageResponseCardUnionTypeDef],
    },
)
DialogActionUnionTypeDef = Union[DialogActionTypeDef, DialogActionOutputTypeDef]
RuntimeHintsTypeDef = TypedDict(
    "RuntimeHintsTypeDef",
    {
        "slotHints": NotRequired[Mapping[str, Mapping[str, RuntimeHintDetailsUnionTypeDef]]],
    },
)
InterpretationTypeDef = TypedDict(
    "InterpretationTypeDef",
    {
        "nluConfidence": NotRequired[ConfidenceScoreTypeDef],
        "sentimentResponse": NotRequired[SentimentResponseTypeDef],
        "intent": NotRequired[IntentOutputTypeDef],
        "interpretationSource": NotRequired[InterpretationSourceType],
    },
)
SessionStateOutputTypeDef = TypedDict(
    "SessionStateOutputTypeDef",
    {
        "dialogAction": NotRequired[DialogActionOutputTypeDef],
        "intent": NotRequired[IntentOutputTypeDef],
        "activeContexts": NotRequired[List[ActiveContextOutputTypeDef]],
        "sessionAttributes": NotRequired[Dict[str, str]],
        "originatingRequestId": NotRequired[str],
        "runtimeHints": NotRequired[RuntimeHintsOutputTypeDef],
    },
)
SlotUnionTypeDef = Union[SlotTypeDef, SlotOutputTypeDef]
MessageUnionTypeDef = Union[MessageTypeDef, MessageOutputTypeDef]
RuntimeHintsUnionTypeDef = Union[RuntimeHintsTypeDef, RuntimeHintsOutputTypeDef]
GetSessionResponseTypeDef = TypedDict(
    "GetSessionResponseTypeDef",
    {
        "sessionId": str,
        "messages": List[MessageOutputTypeDef],
        "interpretations": List[InterpretationTypeDef],
        "sessionState": SessionStateOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RecognizeTextResponseTypeDef = TypedDict(
    "RecognizeTextResponseTypeDef",
    {
        "messages": List[MessageOutputTypeDef],
        "sessionState": SessionStateOutputTypeDef,
        "interpretations": List[InterpretationTypeDef],
        "requestAttributes": Dict[str, str],
        "sessionId": str,
        "recognizedBotMember": RecognizedBotMemberTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IntentTypeDef = TypedDict(
    "IntentTypeDef",
    {
        "name": str,
        "slots": NotRequired[Mapping[str, SlotUnionTypeDef]],
        "state": NotRequired[IntentStateType],
        "confirmationState": NotRequired[ConfirmationStateType],
    },
)
IntentUnionTypeDef = Union[IntentTypeDef, IntentOutputTypeDef]
SessionStateTypeDef = TypedDict(
    "SessionStateTypeDef",
    {
        "dialogAction": NotRequired[DialogActionUnionTypeDef],
        "intent": NotRequired[IntentUnionTypeDef],
        "activeContexts": NotRequired[Sequence[ActiveContextUnionTypeDef]],
        "sessionAttributes": NotRequired[Mapping[str, str]],
        "originatingRequestId": NotRequired[str],
        "runtimeHints": NotRequired[RuntimeHintsUnionTypeDef],
    },
)
PutSessionRequestRequestTypeDef = TypedDict(
    "PutSessionRequestRequestTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
        "sessionId": str,
        "sessionState": SessionStateTypeDef,
        "messages": NotRequired[Sequence[MessageUnionTypeDef]],
        "requestAttributes": NotRequired[Mapping[str, str]],
        "responseContentType": NotRequired[str],
    },
)
RecognizeTextRequestRequestTypeDef = TypedDict(
    "RecognizeTextRequestRequestTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
        "sessionId": str,
        "text": str,
        "sessionState": NotRequired[SessionStateTypeDef],
        "requestAttributes": NotRequired[Mapping[str, str]],
    },
)
