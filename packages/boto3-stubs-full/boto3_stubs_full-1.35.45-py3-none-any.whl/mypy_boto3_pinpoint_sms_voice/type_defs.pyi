"""
Type annotations for pinpoint-sms-voice service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice/type_defs/)

Usage::

    ```python
    from mypy_boto3_pinpoint_sms_voice.type_defs import CallInstructionsMessageTypeTypeDef

    data: CallInstructionsMessageTypeTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Sequence

from .literals import EventTypeType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "CallInstructionsMessageTypeTypeDef",
    "CloudWatchLogsDestinationTypeDef",
    "CreateConfigurationSetRequestRequestTypeDef",
    "DeleteConfigurationSetEventDestinationRequestRequestTypeDef",
    "DeleteConfigurationSetRequestRequestTypeDef",
    "KinesisFirehoseDestinationTypeDef",
    "SnsDestinationTypeDef",
    "GetConfigurationSetEventDestinationsRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "PlainTextMessageTypeTypeDef",
    "SSMLMessageTypeTypeDef",
    "EventDestinationDefinitionTypeDef",
    "EventDestinationTypeDef",
    "SendVoiceMessageResponseTypeDef",
    "VoiceMessageContentTypeDef",
    "CreateConfigurationSetEventDestinationRequestRequestTypeDef",
    "UpdateConfigurationSetEventDestinationRequestRequestTypeDef",
    "GetConfigurationSetEventDestinationsResponseTypeDef",
    "SendVoiceMessageRequestRequestTypeDef",
)

CallInstructionsMessageTypeTypeDef = TypedDict(
    "CallInstructionsMessageTypeTypeDef",
    {
        "Text": NotRequired[str],
    },
)
CloudWatchLogsDestinationTypeDef = TypedDict(
    "CloudWatchLogsDestinationTypeDef",
    {
        "IamRoleArn": NotRequired[str],
        "LogGroupArn": NotRequired[str],
    },
)
CreateConfigurationSetRequestRequestTypeDef = TypedDict(
    "CreateConfigurationSetRequestRequestTypeDef",
    {
        "ConfigurationSetName": NotRequired[str],
    },
)
DeleteConfigurationSetEventDestinationRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationSetEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestinationName": str,
    },
)
DeleteConfigurationSetRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationSetRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)
KinesisFirehoseDestinationTypeDef = TypedDict(
    "KinesisFirehoseDestinationTypeDef",
    {
        "DeliveryStreamArn": NotRequired[str],
        "IamRoleArn": NotRequired[str],
    },
)
SnsDestinationTypeDef = TypedDict(
    "SnsDestinationTypeDef",
    {
        "TopicArn": NotRequired[str],
    },
)
GetConfigurationSetEventDestinationsRequestRequestTypeDef = TypedDict(
    "GetConfigurationSetEventDestinationsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
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
PlainTextMessageTypeTypeDef = TypedDict(
    "PlainTextMessageTypeTypeDef",
    {
        "LanguageCode": NotRequired[str],
        "Text": NotRequired[str],
        "VoiceId": NotRequired[str],
    },
)
SSMLMessageTypeTypeDef = TypedDict(
    "SSMLMessageTypeTypeDef",
    {
        "LanguageCode": NotRequired[str],
        "Text": NotRequired[str],
        "VoiceId": NotRequired[str],
    },
)
EventDestinationDefinitionTypeDef = TypedDict(
    "EventDestinationDefinitionTypeDef",
    {
        "CloudWatchLogsDestination": NotRequired[CloudWatchLogsDestinationTypeDef],
        "Enabled": NotRequired[bool],
        "KinesisFirehoseDestination": NotRequired[KinesisFirehoseDestinationTypeDef],
        "MatchingEventTypes": NotRequired[Sequence[EventTypeType]],
        "SnsDestination": NotRequired[SnsDestinationTypeDef],
    },
)
EventDestinationTypeDef = TypedDict(
    "EventDestinationTypeDef",
    {
        "CloudWatchLogsDestination": NotRequired[CloudWatchLogsDestinationTypeDef],
        "Enabled": NotRequired[bool],
        "KinesisFirehoseDestination": NotRequired[KinesisFirehoseDestinationTypeDef],
        "MatchingEventTypes": NotRequired[List[EventTypeType]],
        "Name": NotRequired[str],
        "SnsDestination": NotRequired[SnsDestinationTypeDef],
    },
)
SendVoiceMessageResponseTypeDef = TypedDict(
    "SendVoiceMessageResponseTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VoiceMessageContentTypeDef = TypedDict(
    "VoiceMessageContentTypeDef",
    {
        "CallInstructionsMessage": NotRequired[CallInstructionsMessageTypeTypeDef],
        "PlainTextMessage": NotRequired[PlainTextMessageTypeTypeDef],
        "SSMLMessage": NotRequired[SSMLMessageTypeTypeDef],
    },
)
CreateConfigurationSetEventDestinationRequestRequestTypeDef = TypedDict(
    "CreateConfigurationSetEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestination": NotRequired[EventDestinationDefinitionTypeDef],
        "EventDestinationName": NotRequired[str],
    },
)
UpdateConfigurationSetEventDestinationRequestRequestTypeDef = TypedDict(
    "UpdateConfigurationSetEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestinationName": str,
        "EventDestination": NotRequired[EventDestinationDefinitionTypeDef],
    },
)
GetConfigurationSetEventDestinationsResponseTypeDef = TypedDict(
    "GetConfigurationSetEventDestinationsResponseTypeDef",
    {
        "EventDestinations": List[EventDestinationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendVoiceMessageRequestRequestTypeDef = TypedDict(
    "SendVoiceMessageRequestRequestTypeDef",
    {
        "CallerId": NotRequired[str],
        "ConfigurationSetName": NotRequired[str],
        "Content": NotRequired[VoiceMessageContentTypeDef],
        "DestinationPhoneNumber": NotRequired[str],
        "OriginationPhoneNumber": NotRequired[str],
    },
)
