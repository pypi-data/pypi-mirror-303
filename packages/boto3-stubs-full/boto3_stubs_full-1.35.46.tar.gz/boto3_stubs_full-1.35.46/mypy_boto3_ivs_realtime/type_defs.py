"""
Type annotations for ivs-realtime service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/type_defs/)

Usage::

    ```python
    from mypy_boto3_ivs_realtime.type_defs import AutoParticipantRecordingConfigurationOutputTypeDef

    data: AutoParticipantRecordingConfigurationOutputTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    CompositionStateType,
    DestinationStateType,
    EventErrorCodeType,
    EventNameType,
    IngestConfigurationStateType,
    IngestProtocolType,
    ParticipantProtocolType,
    ParticipantRecordingFilterByRecordingStateType,
    ParticipantRecordingMediaTypeType,
    ParticipantRecordingStateType,
    ParticipantStateType,
    ParticipantTokenCapabilityType,
    PipBehaviorType,
    PipPositionType,
    VideoAspectRatioType,
    VideoFillModeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AutoParticipantRecordingConfigurationOutputTypeDef",
    "AutoParticipantRecordingConfigurationTypeDef",
    "ChannelDestinationConfigurationTypeDef",
    "DestinationSummaryTypeDef",
    "VideoTypeDef",
    "ResponseMetadataTypeDef",
    "CreateIngestConfigurationRequestRequestTypeDef",
    "IngestConfigurationTypeDef",
    "CreateParticipantTokenRequestRequestTypeDef",
    "ParticipantTokenTypeDef",
    "ParticipantTokenConfigurationTypeDef",
    "S3StorageConfigurationTypeDef",
    "DeleteEncoderConfigurationRequestRequestTypeDef",
    "DeleteIngestConfigurationRequestRequestTypeDef",
    "DeletePublicKeyRequestRequestTypeDef",
    "DeleteStageRequestRequestTypeDef",
    "DeleteStorageConfigurationRequestRequestTypeDef",
    "S3DetailTypeDef",
    "DisconnectParticipantRequestRequestTypeDef",
    "EncoderConfigurationSummaryTypeDef",
    "EventTypeDef",
    "GetCompositionRequestRequestTypeDef",
    "GetEncoderConfigurationRequestRequestTypeDef",
    "GetIngestConfigurationRequestRequestTypeDef",
    "GetParticipantRequestRequestTypeDef",
    "ParticipantTypeDef",
    "GetPublicKeyRequestRequestTypeDef",
    "PublicKeyTypeDef",
    "GetStageRequestRequestTypeDef",
    "GetStageSessionRequestRequestTypeDef",
    "StageSessionTypeDef",
    "GetStorageConfigurationRequestRequestTypeDef",
    "GridConfigurationTypeDef",
    "ImportPublicKeyRequestRequestTypeDef",
    "IngestConfigurationSummaryTypeDef",
    "PipConfigurationTypeDef",
    "ListCompositionsRequestRequestTypeDef",
    "ListEncoderConfigurationsRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListIngestConfigurationsRequestRequestTypeDef",
    "ListParticipantEventsRequestRequestTypeDef",
    "ListParticipantsRequestRequestTypeDef",
    "ParticipantSummaryTypeDef",
    "ListPublicKeysRequestRequestTypeDef",
    "PublicKeySummaryTypeDef",
    "ListStageSessionsRequestRequestTypeDef",
    "StageSessionSummaryTypeDef",
    "ListStagesRequestRequestTypeDef",
    "StageSummaryTypeDef",
    "ListStorageConfigurationsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "RecordingConfigurationTypeDef",
    "StageEndpointsTypeDef",
    "StopCompositionRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateIngestConfigurationRequestRequestTypeDef",
    "UpdateStageRequestRequestTypeDef",
    "CompositionSummaryTypeDef",
    "CreateEncoderConfigurationRequestRequestTypeDef",
    "EncoderConfigurationTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "CreateIngestConfigurationResponseTypeDef",
    "GetIngestConfigurationResponseTypeDef",
    "UpdateIngestConfigurationResponseTypeDef",
    "CreateParticipantTokenResponseTypeDef",
    "CreateStageRequestRequestTypeDef",
    "CreateStorageConfigurationRequestRequestTypeDef",
    "StorageConfigurationSummaryTypeDef",
    "StorageConfigurationTypeDef",
    "DestinationDetailTypeDef",
    "ListEncoderConfigurationsResponseTypeDef",
    "ListParticipantEventsResponseTypeDef",
    "GetParticipantResponseTypeDef",
    "GetPublicKeyResponseTypeDef",
    "ImportPublicKeyResponseTypeDef",
    "GetStageSessionResponseTypeDef",
    "ListIngestConfigurationsResponseTypeDef",
    "LayoutConfigurationTypeDef",
    "ListIngestConfigurationsRequestListIngestConfigurationsPaginateTypeDef",
    "ListPublicKeysRequestListPublicKeysPaginateTypeDef",
    "ListParticipantsResponseTypeDef",
    "ListPublicKeysResponseTypeDef",
    "ListStageSessionsResponseTypeDef",
    "ListStagesResponseTypeDef",
    "S3DestinationConfigurationOutputTypeDef",
    "S3DestinationConfigurationTypeDef",
    "StageTypeDef",
    "ListCompositionsResponseTypeDef",
    "CreateEncoderConfigurationResponseTypeDef",
    "GetEncoderConfigurationResponseTypeDef",
    "ListStorageConfigurationsResponseTypeDef",
    "CreateStorageConfigurationResponseTypeDef",
    "GetStorageConfigurationResponseTypeDef",
    "DestinationConfigurationOutputTypeDef",
    "S3DestinationConfigurationUnionTypeDef",
    "CreateStageResponseTypeDef",
    "GetStageResponseTypeDef",
    "UpdateStageResponseTypeDef",
    "DestinationTypeDef",
    "DestinationConfigurationTypeDef",
    "CompositionTypeDef",
    "DestinationConfigurationUnionTypeDef",
    "GetCompositionResponseTypeDef",
    "StartCompositionResponseTypeDef",
    "StartCompositionRequestRequestTypeDef",
)

AutoParticipantRecordingConfigurationOutputTypeDef = TypedDict(
    "AutoParticipantRecordingConfigurationOutputTypeDef",
    {
        "storageConfigurationArn": str,
        "mediaTypes": NotRequired[List[ParticipantRecordingMediaTypeType]],
    },
)
AutoParticipantRecordingConfigurationTypeDef = TypedDict(
    "AutoParticipantRecordingConfigurationTypeDef",
    {
        "storageConfigurationArn": str,
        "mediaTypes": NotRequired[Sequence[ParticipantRecordingMediaTypeType]],
    },
)
ChannelDestinationConfigurationTypeDef = TypedDict(
    "ChannelDestinationConfigurationTypeDef",
    {
        "channelArn": str,
        "encoderConfigurationArn": NotRequired[str],
    },
)
DestinationSummaryTypeDef = TypedDict(
    "DestinationSummaryTypeDef",
    {
        "id": str,
        "state": DestinationStateType,
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
    },
)
VideoTypeDef = TypedDict(
    "VideoTypeDef",
    {
        "width": NotRequired[int],
        "height": NotRequired[int],
        "framerate": NotRequired[float],
        "bitrate": NotRequired[int],
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
CreateIngestConfigurationRequestRequestTypeDef = TypedDict(
    "CreateIngestConfigurationRequestRequestTypeDef",
    {
        "ingestProtocol": IngestProtocolType,
        "name": NotRequired[str],
        "stageArn": NotRequired[str],
        "userId": NotRequired[str],
        "attributes": NotRequired[Mapping[str, str]],
        "insecureIngest": NotRequired[bool],
        "tags": NotRequired[Mapping[str, str]],
    },
)
IngestConfigurationTypeDef = TypedDict(
    "IngestConfigurationTypeDef",
    {
        "arn": str,
        "ingestProtocol": IngestProtocolType,
        "streamKey": str,
        "stageArn": str,
        "participantId": str,
        "state": IngestConfigurationStateType,
        "name": NotRequired[str],
        "userId": NotRequired[str],
        "attributes": NotRequired[Dict[str, str]],
        "tags": NotRequired[Dict[str, str]],
    },
)
CreateParticipantTokenRequestRequestTypeDef = TypedDict(
    "CreateParticipantTokenRequestRequestTypeDef",
    {
        "stageArn": str,
        "duration": NotRequired[int],
        "userId": NotRequired[str],
        "attributes": NotRequired[Mapping[str, str]],
        "capabilities": NotRequired[Sequence[ParticipantTokenCapabilityType]],
    },
)
ParticipantTokenTypeDef = TypedDict(
    "ParticipantTokenTypeDef",
    {
        "participantId": NotRequired[str],
        "token": NotRequired[str],
        "userId": NotRequired[str],
        "attributes": NotRequired[Dict[str, str]],
        "duration": NotRequired[int],
        "capabilities": NotRequired[List[ParticipantTokenCapabilityType]],
        "expirationTime": NotRequired[datetime],
    },
)
ParticipantTokenConfigurationTypeDef = TypedDict(
    "ParticipantTokenConfigurationTypeDef",
    {
        "duration": NotRequired[int],
        "userId": NotRequired[str],
        "attributes": NotRequired[Mapping[str, str]],
        "capabilities": NotRequired[Sequence[ParticipantTokenCapabilityType]],
    },
)
S3StorageConfigurationTypeDef = TypedDict(
    "S3StorageConfigurationTypeDef",
    {
        "bucketName": str,
    },
)
DeleteEncoderConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteEncoderConfigurationRequestRequestTypeDef",
    {
        "arn": str,
    },
)
DeleteIngestConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteIngestConfigurationRequestRequestTypeDef",
    {
        "arn": str,
        "force": NotRequired[bool],
    },
)
DeletePublicKeyRequestRequestTypeDef = TypedDict(
    "DeletePublicKeyRequestRequestTypeDef",
    {
        "arn": str,
    },
)
DeleteStageRequestRequestTypeDef = TypedDict(
    "DeleteStageRequestRequestTypeDef",
    {
        "arn": str,
    },
)
DeleteStorageConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteStorageConfigurationRequestRequestTypeDef",
    {
        "arn": str,
    },
)
S3DetailTypeDef = TypedDict(
    "S3DetailTypeDef",
    {
        "recordingPrefix": str,
    },
)
DisconnectParticipantRequestRequestTypeDef = TypedDict(
    "DisconnectParticipantRequestRequestTypeDef",
    {
        "stageArn": str,
        "participantId": str,
        "reason": NotRequired[str],
    },
)
EncoderConfigurationSummaryTypeDef = TypedDict(
    "EncoderConfigurationSummaryTypeDef",
    {
        "arn": str,
        "name": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)
EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "name": NotRequired[EventNameType],
        "participantId": NotRequired[str],
        "eventTime": NotRequired[datetime],
        "remoteParticipantId": NotRequired[str],
        "errorCode": NotRequired[EventErrorCodeType],
    },
)
GetCompositionRequestRequestTypeDef = TypedDict(
    "GetCompositionRequestRequestTypeDef",
    {
        "arn": str,
    },
)
GetEncoderConfigurationRequestRequestTypeDef = TypedDict(
    "GetEncoderConfigurationRequestRequestTypeDef",
    {
        "arn": str,
    },
)
GetIngestConfigurationRequestRequestTypeDef = TypedDict(
    "GetIngestConfigurationRequestRequestTypeDef",
    {
        "arn": str,
    },
)
GetParticipantRequestRequestTypeDef = TypedDict(
    "GetParticipantRequestRequestTypeDef",
    {
        "stageArn": str,
        "sessionId": str,
        "participantId": str,
    },
)
ParticipantTypeDef = TypedDict(
    "ParticipantTypeDef",
    {
        "participantId": NotRequired[str],
        "userId": NotRequired[str],
        "state": NotRequired[ParticipantStateType],
        "firstJoinTime": NotRequired[datetime],
        "attributes": NotRequired[Dict[str, str]],
        "published": NotRequired[bool],
        "ispName": NotRequired[str],
        "osName": NotRequired[str],
        "osVersion": NotRequired[str],
        "browserName": NotRequired[str],
        "browserVersion": NotRequired[str],
        "sdkVersion": NotRequired[str],
        "recordingS3BucketName": NotRequired[str],
        "recordingS3Prefix": NotRequired[str],
        "recordingState": NotRequired[ParticipantRecordingStateType],
        "protocol": NotRequired[ParticipantProtocolType],
    },
)
GetPublicKeyRequestRequestTypeDef = TypedDict(
    "GetPublicKeyRequestRequestTypeDef",
    {
        "arn": str,
    },
)
PublicKeyTypeDef = TypedDict(
    "PublicKeyTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "publicKeyMaterial": NotRequired[str],
        "fingerprint": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)
GetStageRequestRequestTypeDef = TypedDict(
    "GetStageRequestRequestTypeDef",
    {
        "arn": str,
    },
)
GetStageSessionRequestRequestTypeDef = TypedDict(
    "GetStageSessionRequestRequestTypeDef",
    {
        "stageArn": str,
        "sessionId": str,
    },
)
StageSessionTypeDef = TypedDict(
    "StageSessionTypeDef",
    {
        "sessionId": NotRequired[str],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
    },
)
GetStorageConfigurationRequestRequestTypeDef = TypedDict(
    "GetStorageConfigurationRequestRequestTypeDef",
    {
        "arn": str,
    },
)
GridConfigurationTypeDef = TypedDict(
    "GridConfigurationTypeDef",
    {
        "featuredParticipantAttribute": NotRequired[str],
        "omitStoppedVideo": NotRequired[bool],
        "videoAspectRatio": NotRequired[VideoAspectRatioType],
        "videoFillMode": NotRequired[VideoFillModeType],
        "gridGap": NotRequired[int],
    },
)
ImportPublicKeyRequestRequestTypeDef = TypedDict(
    "ImportPublicKeyRequestRequestTypeDef",
    {
        "publicKeyMaterial": str,
        "name": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
IngestConfigurationSummaryTypeDef = TypedDict(
    "IngestConfigurationSummaryTypeDef",
    {
        "arn": str,
        "ingestProtocol": IngestProtocolType,
        "stageArn": str,
        "participantId": str,
        "state": IngestConfigurationStateType,
        "name": NotRequired[str],
        "userId": NotRequired[str],
    },
)
PipConfigurationTypeDef = TypedDict(
    "PipConfigurationTypeDef",
    {
        "featuredParticipantAttribute": NotRequired[str],
        "omitStoppedVideo": NotRequired[bool],
        "videoFillMode": NotRequired[VideoFillModeType],
        "gridGap": NotRequired[int],
        "pipParticipantAttribute": NotRequired[str],
        "pipBehavior": NotRequired[PipBehaviorType],
        "pipOffset": NotRequired[int],
        "pipPosition": NotRequired[PipPositionType],
        "pipWidth": NotRequired[int],
        "pipHeight": NotRequired[int],
    },
)
ListCompositionsRequestRequestTypeDef = TypedDict(
    "ListCompositionsRequestRequestTypeDef",
    {
        "filterByStageArn": NotRequired[str],
        "filterByEncoderConfigurationArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListEncoderConfigurationsRequestRequestTypeDef = TypedDict(
    "ListEncoderConfigurationsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
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
ListIngestConfigurationsRequestRequestTypeDef = TypedDict(
    "ListIngestConfigurationsRequestRequestTypeDef",
    {
        "filterByStageArn": NotRequired[str],
        "filterByState": NotRequired[IngestConfigurationStateType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListParticipantEventsRequestRequestTypeDef = TypedDict(
    "ListParticipantEventsRequestRequestTypeDef",
    {
        "stageArn": str,
        "sessionId": str,
        "participantId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListParticipantsRequestRequestTypeDef = TypedDict(
    "ListParticipantsRequestRequestTypeDef",
    {
        "stageArn": str,
        "sessionId": str,
        "filterByUserId": NotRequired[str],
        "filterByPublished": NotRequired[bool],
        "filterByState": NotRequired[ParticipantStateType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filterByRecordingState": NotRequired[ParticipantRecordingFilterByRecordingStateType],
    },
)
ParticipantSummaryTypeDef = TypedDict(
    "ParticipantSummaryTypeDef",
    {
        "participantId": NotRequired[str],
        "userId": NotRequired[str],
        "state": NotRequired[ParticipantStateType],
        "firstJoinTime": NotRequired[datetime],
        "published": NotRequired[bool],
        "recordingState": NotRequired[ParticipantRecordingStateType],
    },
)
ListPublicKeysRequestRequestTypeDef = TypedDict(
    "ListPublicKeysRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
PublicKeySummaryTypeDef = TypedDict(
    "PublicKeySummaryTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)
ListStageSessionsRequestRequestTypeDef = TypedDict(
    "ListStageSessionsRequestRequestTypeDef",
    {
        "stageArn": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
StageSessionSummaryTypeDef = TypedDict(
    "StageSessionSummaryTypeDef",
    {
        "sessionId": NotRequired[str],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
    },
)
ListStagesRequestRequestTypeDef = TypedDict(
    "ListStagesRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
StageSummaryTypeDef = TypedDict(
    "StageSummaryTypeDef",
    {
        "arn": str,
        "name": NotRequired[str],
        "activeSessionId": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)
ListStorageConfigurationsRequestRequestTypeDef = TypedDict(
    "ListStorageConfigurationsRequestRequestTypeDef",
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
RecordingConfigurationTypeDef = TypedDict(
    "RecordingConfigurationTypeDef",
    {
        "format": NotRequired[Literal["HLS"]],
    },
)
StageEndpointsTypeDef = TypedDict(
    "StageEndpointsTypeDef",
    {
        "events": NotRequired[str],
        "whip": NotRequired[str],
        "rtmp": NotRequired[str],
        "rtmps": NotRequired[str],
    },
)
StopCompositionRequestRequestTypeDef = TypedDict(
    "StopCompositionRequestRequestTypeDef",
    {
        "arn": str,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UpdateIngestConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateIngestConfigurationRequestRequestTypeDef",
    {
        "arn": str,
        "stageArn": NotRequired[str],
    },
)
UpdateStageRequestRequestTypeDef = TypedDict(
    "UpdateStageRequestRequestTypeDef",
    {
        "arn": str,
        "name": NotRequired[str],
        "autoParticipantRecordingConfiguration": NotRequired[
            AutoParticipantRecordingConfigurationTypeDef
        ],
    },
)
CompositionSummaryTypeDef = TypedDict(
    "CompositionSummaryTypeDef",
    {
        "arn": str,
        "stageArn": str,
        "destinations": List[DestinationSummaryTypeDef],
        "state": CompositionStateType,
        "tags": NotRequired[Dict[str, str]],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
    },
)
CreateEncoderConfigurationRequestRequestTypeDef = TypedDict(
    "CreateEncoderConfigurationRequestRequestTypeDef",
    {
        "name": NotRequired[str],
        "video": NotRequired[VideoTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
EncoderConfigurationTypeDef = TypedDict(
    "EncoderConfigurationTypeDef",
    {
        "arn": str,
        "name": NotRequired[str],
        "video": NotRequired[VideoTypeDef],
        "tags": NotRequired[Dict[str, str]],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateIngestConfigurationResponseTypeDef = TypedDict(
    "CreateIngestConfigurationResponseTypeDef",
    {
        "ingestConfiguration": IngestConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIngestConfigurationResponseTypeDef = TypedDict(
    "GetIngestConfigurationResponseTypeDef",
    {
        "ingestConfiguration": IngestConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateIngestConfigurationResponseTypeDef = TypedDict(
    "UpdateIngestConfigurationResponseTypeDef",
    {
        "ingestConfiguration": IngestConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateParticipantTokenResponseTypeDef = TypedDict(
    "CreateParticipantTokenResponseTypeDef",
    {
        "participantToken": ParticipantTokenTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateStageRequestRequestTypeDef = TypedDict(
    "CreateStageRequestRequestTypeDef",
    {
        "name": NotRequired[str],
        "participantTokenConfigurations": NotRequired[
            Sequence[ParticipantTokenConfigurationTypeDef]
        ],
        "tags": NotRequired[Mapping[str, str]],
        "autoParticipantRecordingConfiguration": NotRequired[
            AutoParticipantRecordingConfigurationTypeDef
        ],
    },
)
CreateStorageConfigurationRequestRequestTypeDef = TypedDict(
    "CreateStorageConfigurationRequestRequestTypeDef",
    {
        "s3": S3StorageConfigurationTypeDef,
        "name": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
StorageConfigurationSummaryTypeDef = TypedDict(
    "StorageConfigurationSummaryTypeDef",
    {
        "arn": str,
        "name": NotRequired[str],
        "s3": NotRequired[S3StorageConfigurationTypeDef],
        "tags": NotRequired[Dict[str, str]],
    },
)
StorageConfigurationTypeDef = TypedDict(
    "StorageConfigurationTypeDef",
    {
        "arn": str,
        "name": NotRequired[str],
        "s3": NotRequired[S3StorageConfigurationTypeDef],
        "tags": NotRequired[Dict[str, str]],
    },
)
DestinationDetailTypeDef = TypedDict(
    "DestinationDetailTypeDef",
    {
        "s3": NotRequired[S3DetailTypeDef],
    },
)
ListEncoderConfigurationsResponseTypeDef = TypedDict(
    "ListEncoderConfigurationsResponseTypeDef",
    {
        "encoderConfigurations": List[EncoderConfigurationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListParticipantEventsResponseTypeDef = TypedDict(
    "ListParticipantEventsResponseTypeDef",
    {
        "events": List[EventTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetParticipantResponseTypeDef = TypedDict(
    "GetParticipantResponseTypeDef",
    {
        "participant": ParticipantTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPublicKeyResponseTypeDef = TypedDict(
    "GetPublicKeyResponseTypeDef",
    {
        "publicKey": PublicKeyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportPublicKeyResponseTypeDef = TypedDict(
    "ImportPublicKeyResponseTypeDef",
    {
        "publicKey": PublicKeyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetStageSessionResponseTypeDef = TypedDict(
    "GetStageSessionResponseTypeDef",
    {
        "stageSession": StageSessionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListIngestConfigurationsResponseTypeDef = TypedDict(
    "ListIngestConfigurationsResponseTypeDef",
    {
        "ingestConfigurations": List[IngestConfigurationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LayoutConfigurationTypeDef = TypedDict(
    "LayoutConfigurationTypeDef",
    {
        "grid": NotRequired[GridConfigurationTypeDef],
        "pip": NotRequired[PipConfigurationTypeDef],
    },
)
ListIngestConfigurationsRequestListIngestConfigurationsPaginateTypeDef = TypedDict(
    "ListIngestConfigurationsRequestListIngestConfigurationsPaginateTypeDef",
    {
        "filterByStageArn": NotRequired[str],
        "filterByState": NotRequired[IngestConfigurationStateType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPublicKeysRequestListPublicKeysPaginateTypeDef = TypedDict(
    "ListPublicKeysRequestListPublicKeysPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListParticipantsResponseTypeDef = TypedDict(
    "ListParticipantsResponseTypeDef",
    {
        "participants": List[ParticipantSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPublicKeysResponseTypeDef = TypedDict(
    "ListPublicKeysResponseTypeDef",
    {
        "publicKeys": List[PublicKeySummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListStageSessionsResponseTypeDef = TypedDict(
    "ListStageSessionsResponseTypeDef",
    {
        "stageSessions": List[StageSessionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListStagesResponseTypeDef = TypedDict(
    "ListStagesResponseTypeDef",
    {
        "stages": List[StageSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
S3DestinationConfigurationOutputTypeDef = TypedDict(
    "S3DestinationConfigurationOutputTypeDef",
    {
        "storageConfigurationArn": str,
        "encoderConfigurationArns": List[str],
        "recordingConfiguration": NotRequired[RecordingConfigurationTypeDef],
    },
)
S3DestinationConfigurationTypeDef = TypedDict(
    "S3DestinationConfigurationTypeDef",
    {
        "storageConfigurationArn": str,
        "encoderConfigurationArns": Sequence[str],
        "recordingConfiguration": NotRequired[RecordingConfigurationTypeDef],
    },
)
StageTypeDef = TypedDict(
    "StageTypeDef",
    {
        "arn": str,
        "name": NotRequired[str],
        "activeSessionId": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "autoParticipantRecordingConfiguration": NotRequired[
            AutoParticipantRecordingConfigurationOutputTypeDef
        ],
        "endpoints": NotRequired[StageEndpointsTypeDef],
    },
)
ListCompositionsResponseTypeDef = TypedDict(
    "ListCompositionsResponseTypeDef",
    {
        "compositions": List[CompositionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEncoderConfigurationResponseTypeDef = TypedDict(
    "CreateEncoderConfigurationResponseTypeDef",
    {
        "encoderConfiguration": EncoderConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEncoderConfigurationResponseTypeDef = TypedDict(
    "GetEncoderConfigurationResponseTypeDef",
    {
        "encoderConfiguration": EncoderConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListStorageConfigurationsResponseTypeDef = TypedDict(
    "ListStorageConfigurationsResponseTypeDef",
    {
        "storageConfigurations": List[StorageConfigurationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateStorageConfigurationResponseTypeDef = TypedDict(
    "CreateStorageConfigurationResponseTypeDef",
    {
        "storageConfiguration": StorageConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetStorageConfigurationResponseTypeDef = TypedDict(
    "GetStorageConfigurationResponseTypeDef",
    {
        "storageConfiguration": StorageConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DestinationConfigurationOutputTypeDef = TypedDict(
    "DestinationConfigurationOutputTypeDef",
    {
        "name": NotRequired[str],
        "channel": NotRequired[ChannelDestinationConfigurationTypeDef],
        "s3": NotRequired[S3DestinationConfigurationOutputTypeDef],
    },
)
S3DestinationConfigurationUnionTypeDef = Union[
    S3DestinationConfigurationTypeDef, S3DestinationConfigurationOutputTypeDef
]
CreateStageResponseTypeDef = TypedDict(
    "CreateStageResponseTypeDef",
    {
        "stage": StageTypeDef,
        "participantTokens": List[ParticipantTokenTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetStageResponseTypeDef = TypedDict(
    "GetStageResponseTypeDef",
    {
        "stage": StageTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateStageResponseTypeDef = TypedDict(
    "UpdateStageResponseTypeDef",
    {
        "stage": StageTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "id": str,
        "state": DestinationStateType,
        "configuration": DestinationConfigurationOutputTypeDef,
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
        "detail": NotRequired[DestinationDetailTypeDef],
    },
)
DestinationConfigurationTypeDef = TypedDict(
    "DestinationConfigurationTypeDef",
    {
        "name": NotRequired[str],
        "channel": NotRequired[ChannelDestinationConfigurationTypeDef],
        "s3": NotRequired[S3DestinationConfigurationUnionTypeDef],
    },
)
CompositionTypeDef = TypedDict(
    "CompositionTypeDef",
    {
        "arn": str,
        "stageArn": str,
        "state": CompositionStateType,
        "layout": LayoutConfigurationTypeDef,
        "destinations": List[DestinationTypeDef],
        "tags": NotRequired[Dict[str, str]],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
    },
)
DestinationConfigurationUnionTypeDef = Union[
    DestinationConfigurationTypeDef, DestinationConfigurationOutputTypeDef
]
GetCompositionResponseTypeDef = TypedDict(
    "GetCompositionResponseTypeDef",
    {
        "composition": CompositionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartCompositionResponseTypeDef = TypedDict(
    "StartCompositionResponseTypeDef",
    {
        "composition": CompositionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartCompositionRequestRequestTypeDef = TypedDict(
    "StartCompositionRequestRequestTypeDef",
    {
        "stageArn": str,
        "destinations": Sequence[DestinationConfigurationUnionTypeDef],
        "idempotencyToken": NotRequired[str],
        "layout": NotRequired[LayoutConfigurationTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
