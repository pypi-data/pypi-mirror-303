"""
Type annotations for chime-sdk-meetings service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/type_defs/)

Usage::

    ```python
    from mypy_boto3_chime_sdk_meetings.type_defs import AttendeeCapabilitiesTypeDef

    data: AttendeeCapabilitiesTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Sequence

from .literals import (
    ContentResolutionType,
    MediaCapabilitiesType,
    MeetingFeatureStatusType,
    TranscribeLanguageCodeType,
    TranscribeMedicalRegionType,
    TranscribeMedicalSpecialtyType,
    TranscribeMedicalTypeType,
    TranscribePartialResultsStabilityType,
    TranscribeRegionType,
    TranscribeVocabularyFilterMethodType,
    VideoResolutionType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AttendeeCapabilitiesTypeDef",
    "AttendeeFeaturesTypeDef",
    "AttendeeIdItemTypeDef",
    "AudioFeaturesTypeDef",
    "CreateAttendeeErrorTypeDef",
    "ResponseMetadataTypeDef",
    "ContentFeaturesTypeDef",
    "NotificationsConfigurationTypeDef",
    "TagTypeDef",
    "DeleteAttendeeRequestRequestTypeDef",
    "DeleteMeetingRequestRequestTypeDef",
    "EngineTranscribeMedicalSettingsTypeDef",
    "EngineTranscribeSettingsTypeDef",
    "GetAttendeeRequestRequestTypeDef",
    "GetMeetingRequestRequestTypeDef",
    "ListAttendeesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "MediaPlacementTypeDef",
    "VideoFeaturesTypeDef",
    "StopMeetingTranscriptionRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "AttendeeTypeDef",
    "CreateAttendeeRequestItemTypeDef",
    "CreateAttendeeRequestRequestTypeDef",
    "UpdateAttendeeCapabilitiesRequestRequestTypeDef",
    "BatchUpdateAttendeeCapabilitiesExceptRequestRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TranscriptionConfigurationTypeDef",
    "MeetingFeaturesConfigurationTypeDef",
    "BatchCreateAttendeeResponseTypeDef",
    "CreateAttendeeResponseTypeDef",
    "GetAttendeeResponseTypeDef",
    "ListAttendeesResponseTypeDef",
    "UpdateAttendeeCapabilitiesResponseTypeDef",
    "BatchCreateAttendeeRequestRequestTypeDef",
    "StartMeetingTranscriptionRequestRequestTypeDef",
    "CreateMeetingRequestRequestTypeDef",
    "CreateMeetingWithAttendeesRequestRequestTypeDef",
    "MeetingTypeDef",
    "CreateMeetingResponseTypeDef",
    "CreateMeetingWithAttendeesResponseTypeDef",
    "GetMeetingResponseTypeDef",
)

AttendeeCapabilitiesTypeDef = TypedDict(
    "AttendeeCapabilitiesTypeDef",
    {
        "Audio": MediaCapabilitiesType,
        "Video": MediaCapabilitiesType,
        "Content": MediaCapabilitiesType,
    },
)
AttendeeFeaturesTypeDef = TypedDict(
    "AttendeeFeaturesTypeDef",
    {
        "MaxCount": NotRequired[int],
    },
)
AttendeeIdItemTypeDef = TypedDict(
    "AttendeeIdItemTypeDef",
    {
        "AttendeeId": str,
    },
)
AudioFeaturesTypeDef = TypedDict(
    "AudioFeaturesTypeDef",
    {
        "EchoReduction": NotRequired[MeetingFeatureStatusType],
    },
)
CreateAttendeeErrorTypeDef = TypedDict(
    "CreateAttendeeErrorTypeDef",
    {
        "ExternalUserId": NotRequired[str],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
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
ContentFeaturesTypeDef = TypedDict(
    "ContentFeaturesTypeDef",
    {
        "MaxResolution": NotRequired[ContentResolutionType],
    },
)
NotificationsConfigurationTypeDef = TypedDict(
    "NotificationsConfigurationTypeDef",
    {
        "LambdaFunctionArn": NotRequired[str],
        "SnsTopicArn": NotRequired[str],
        "SqsQueueArn": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
DeleteAttendeeRequestRequestTypeDef = TypedDict(
    "DeleteAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "AttendeeId": str,
    },
)
DeleteMeetingRequestRequestTypeDef = TypedDict(
    "DeleteMeetingRequestRequestTypeDef",
    {
        "MeetingId": str,
    },
)
EngineTranscribeMedicalSettingsTypeDef = TypedDict(
    "EngineTranscribeMedicalSettingsTypeDef",
    {
        "LanguageCode": Literal["en-US"],
        "Specialty": TranscribeMedicalSpecialtyType,
        "Type": TranscribeMedicalTypeType,
        "VocabularyName": NotRequired[str],
        "Region": NotRequired[TranscribeMedicalRegionType],
        "ContentIdentificationType": NotRequired[Literal["PHI"]],
    },
)
EngineTranscribeSettingsTypeDef = TypedDict(
    "EngineTranscribeSettingsTypeDef",
    {
        "LanguageCode": NotRequired[TranscribeLanguageCodeType],
        "VocabularyFilterMethod": NotRequired[TranscribeVocabularyFilterMethodType],
        "VocabularyFilterName": NotRequired[str],
        "VocabularyName": NotRequired[str],
        "Region": NotRequired[TranscribeRegionType],
        "EnablePartialResultsStabilization": NotRequired[bool],
        "PartialResultsStability": NotRequired[TranscribePartialResultsStabilityType],
        "ContentIdentificationType": NotRequired[Literal["PII"]],
        "ContentRedactionType": NotRequired[Literal["PII"]],
        "PiiEntityTypes": NotRequired[str],
        "LanguageModelName": NotRequired[str],
        "IdentifyLanguage": NotRequired[bool],
        "LanguageOptions": NotRequired[str],
        "PreferredLanguage": NotRequired[TranscribeLanguageCodeType],
        "VocabularyNames": NotRequired[str],
        "VocabularyFilterNames": NotRequired[str],
    },
)
GetAttendeeRequestRequestTypeDef = TypedDict(
    "GetAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "AttendeeId": str,
    },
)
GetMeetingRequestRequestTypeDef = TypedDict(
    "GetMeetingRequestRequestTypeDef",
    {
        "MeetingId": str,
    },
)
ListAttendeesRequestRequestTypeDef = TypedDict(
    "ListAttendeesRequestRequestTypeDef",
    {
        "MeetingId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
MediaPlacementTypeDef = TypedDict(
    "MediaPlacementTypeDef",
    {
        "AudioHostUrl": NotRequired[str],
        "AudioFallbackUrl": NotRequired[str],
        "SignalingUrl": NotRequired[str],
        "TurnControlUrl": NotRequired[str],
        "ScreenDataUrl": NotRequired[str],
        "ScreenViewingUrl": NotRequired[str],
        "ScreenSharingUrl": NotRequired[str],
        "EventIngestionUrl": NotRequired[str],
    },
)
VideoFeaturesTypeDef = TypedDict(
    "VideoFeaturesTypeDef",
    {
        "MaxResolution": NotRequired[VideoResolutionType],
    },
)
StopMeetingTranscriptionRequestRequestTypeDef = TypedDict(
    "StopMeetingTranscriptionRequestRequestTypeDef",
    {
        "MeetingId": str,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
AttendeeTypeDef = TypedDict(
    "AttendeeTypeDef",
    {
        "ExternalUserId": NotRequired[str],
        "AttendeeId": NotRequired[str],
        "JoinToken": NotRequired[str],
        "Capabilities": NotRequired[AttendeeCapabilitiesTypeDef],
    },
)
CreateAttendeeRequestItemTypeDef = TypedDict(
    "CreateAttendeeRequestItemTypeDef",
    {
        "ExternalUserId": str,
        "Capabilities": NotRequired[AttendeeCapabilitiesTypeDef],
    },
)
CreateAttendeeRequestRequestTypeDef = TypedDict(
    "CreateAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "ExternalUserId": str,
        "Capabilities": NotRequired[AttendeeCapabilitiesTypeDef],
    },
)
UpdateAttendeeCapabilitiesRequestRequestTypeDef = TypedDict(
    "UpdateAttendeeCapabilitiesRequestRequestTypeDef",
    {
        "MeetingId": str,
        "AttendeeId": str,
        "Capabilities": AttendeeCapabilitiesTypeDef,
    },
)
BatchUpdateAttendeeCapabilitiesExceptRequestRequestTypeDef = TypedDict(
    "BatchUpdateAttendeeCapabilitiesExceptRequestRequestTypeDef",
    {
        "MeetingId": str,
        "ExcludedAttendeeIds": Sequence[AttendeeIdItemTypeDef],
        "Capabilities": AttendeeCapabilitiesTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)
TranscriptionConfigurationTypeDef = TypedDict(
    "TranscriptionConfigurationTypeDef",
    {
        "EngineTranscribeSettings": NotRequired[EngineTranscribeSettingsTypeDef],
        "EngineTranscribeMedicalSettings": NotRequired[EngineTranscribeMedicalSettingsTypeDef],
    },
)
MeetingFeaturesConfigurationTypeDef = TypedDict(
    "MeetingFeaturesConfigurationTypeDef",
    {
        "Audio": NotRequired[AudioFeaturesTypeDef],
        "Video": NotRequired[VideoFeaturesTypeDef],
        "Content": NotRequired[ContentFeaturesTypeDef],
        "Attendee": NotRequired[AttendeeFeaturesTypeDef],
    },
)
BatchCreateAttendeeResponseTypeDef = TypedDict(
    "BatchCreateAttendeeResponseTypeDef",
    {
        "Attendees": List[AttendeeTypeDef],
        "Errors": List[CreateAttendeeErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAttendeeResponseTypeDef = TypedDict(
    "CreateAttendeeResponseTypeDef",
    {
        "Attendee": AttendeeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAttendeeResponseTypeDef = TypedDict(
    "GetAttendeeResponseTypeDef",
    {
        "Attendee": AttendeeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAttendeesResponseTypeDef = TypedDict(
    "ListAttendeesResponseTypeDef",
    {
        "Attendees": List[AttendeeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateAttendeeCapabilitiesResponseTypeDef = TypedDict(
    "UpdateAttendeeCapabilitiesResponseTypeDef",
    {
        "Attendee": AttendeeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchCreateAttendeeRequestRequestTypeDef = TypedDict(
    "BatchCreateAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "Attendees": Sequence[CreateAttendeeRequestItemTypeDef],
    },
)
StartMeetingTranscriptionRequestRequestTypeDef = TypedDict(
    "StartMeetingTranscriptionRequestRequestTypeDef",
    {
        "MeetingId": str,
        "TranscriptionConfiguration": TranscriptionConfigurationTypeDef,
    },
)
CreateMeetingRequestRequestTypeDef = TypedDict(
    "CreateMeetingRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "MediaRegion": str,
        "ExternalMeetingId": str,
        "MeetingHostId": NotRequired[str],
        "NotificationsConfiguration": NotRequired[NotificationsConfigurationTypeDef],
        "MeetingFeatures": NotRequired[MeetingFeaturesConfigurationTypeDef],
        "PrimaryMeetingId": NotRequired[str],
        "TenantIds": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateMeetingWithAttendeesRequestRequestTypeDef = TypedDict(
    "CreateMeetingWithAttendeesRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "MediaRegion": str,
        "ExternalMeetingId": str,
        "Attendees": Sequence[CreateAttendeeRequestItemTypeDef],
        "MeetingHostId": NotRequired[str],
        "MeetingFeatures": NotRequired[MeetingFeaturesConfigurationTypeDef],
        "NotificationsConfiguration": NotRequired[NotificationsConfigurationTypeDef],
        "PrimaryMeetingId": NotRequired[str],
        "TenantIds": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
MeetingTypeDef = TypedDict(
    "MeetingTypeDef",
    {
        "MeetingId": NotRequired[str],
        "MeetingHostId": NotRequired[str],
        "ExternalMeetingId": NotRequired[str],
        "MediaRegion": NotRequired[str],
        "MediaPlacement": NotRequired[MediaPlacementTypeDef],
        "MeetingFeatures": NotRequired[MeetingFeaturesConfigurationTypeDef],
        "PrimaryMeetingId": NotRequired[str],
        "TenantIds": NotRequired[List[str]],
        "MeetingArn": NotRequired[str],
    },
)
CreateMeetingResponseTypeDef = TypedDict(
    "CreateMeetingResponseTypeDef",
    {
        "Meeting": MeetingTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMeetingWithAttendeesResponseTypeDef = TypedDict(
    "CreateMeetingWithAttendeesResponseTypeDef",
    {
        "Meeting": MeetingTypeDef,
        "Attendees": List[AttendeeTypeDef],
        "Errors": List[CreateAttendeeErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMeetingResponseTypeDef = TypedDict(
    "GetMeetingResponseTypeDef",
    {
        "Meeting": MeetingTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
