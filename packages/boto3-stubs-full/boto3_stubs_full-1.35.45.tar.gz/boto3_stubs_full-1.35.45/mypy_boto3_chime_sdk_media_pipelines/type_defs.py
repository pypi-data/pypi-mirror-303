"""
Type annotations for chime-sdk-media-pipelines service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/type_defs/)

Usage::

    ```python
    from mypy_boto3_chime_sdk_media_pipelines.type_defs import ActiveSpeakerOnlyConfigurationTypeDef

    data: ActiveSpeakerOnlyConfigurationTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    ActiveSpeakerPositionType,
    ArtifactsConcatenationStateType,
    ArtifactsStateType,
    AudioChannelsOptionType,
    AudioMuxTypeType,
    BorderColorType,
    CallAnalyticsLanguageCodeType,
    CanvasOrientationType,
    ContentRedactionOutputType,
    ContentShareLayoutOptionType,
    FragmentSelectorTypeType,
    HighlightColorType,
    HorizontalTilePositionType,
    KinesisVideoStreamPoolStatusType,
    LiveConnectorMuxTypeType,
    MediaInsightsPipelineConfigurationElementTypeType,
    MediaPipelineElementStatusType,
    MediaPipelineStatusType,
    MediaPipelineStatusUpdateType,
    MediaPipelineTaskStatusType,
    MediaStreamTypeType,
    PartialResultsStabilityType,
    ParticipantRoleType,
    PresenterPositionType,
    RealTimeAlertRuleTypeType,
    RecordingFileFormatType,
    ResolutionOptionType,
    TileOrderType,
    VerticalTilePositionType,
    VocabularyFilterMethodType,
    VoiceAnalyticsConfigurationStatusType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "ActiveSpeakerOnlyConfigurationTypeDef",
    "PostCallAnalyticsSettingsTypeDef",
    "AmazonTranscribeProcessorConfigurationTypeDef",
    "AudioConcatenationConfigurationTypeDef",
    "CompositedVideoConcatenationConfigurationTypeDef",
    "ContentConcatenationConfigurationTypeDef",
    "DataChannelConcatenationConfigurationTypeDef",
    "MeetingEventsConcatenationConfigurationTypeDef",
    "TranscriptionMessagesConcatenationConfigurationTypeDef",
    "VideoConcatenationConfigurationTypeDef",
    "AudioArtifactsConfigurationTypeDef",
    "ContentArtifactsConfigurationTypeDef",
    "VideoArtifactsConfigurationTypeDef",
    "ChannelDefinitionTypeDef",
    "S3BucketSinkConfigurationTypeDef",
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "S3RecordingSinkRuntimeConfigurationTypeDef",
    "KinesisVideoStreamConfigurationTypeDef",
    "MediaStreamSinkTypeDef",
    "MediaStreamSourceTypeDef",
    "DeleteMediaCapturePipelineRequestRequestTypeDef",
    "DeleteMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    "DeleteMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef",
    "DeleteMediaPipelineRequestRequestTypeDef",
    "TimestampRangeOutputTypeDef",
    "GetMediaCapturePipelineRequestRequestTypeDef",
    "GetMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    "GetMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef",
    "GetMediaPipelineRequestRequestTypeDef",
    "GetSpeakerSearchTaskRequestRequestTypeDef",
    "SpeakerSearchTaskTypeDef",
    "GetVoiceToneAnalysisTaskRequestRequestTypeDef",
    "VoiceToneAnalysisTaskTypeDef",
    "HorizontalLayoutConfigurationTypeDef",
    "PresenterOnlyConfigurationTypeDef",
    "VerticalLayoutConfigurationTypeDef",
    "VideoAttributeTypeDef",
    "IssueDetectionConfigurationTypeDef",
    "KeywordMatchConfigurationOutputTypeDef",
    "KeywordMatchConfigurationTypeDef",
    "KinesisDataStreamSinkConfigurationTypeDef",
    "KinesisVideoStreamConfigurationUpdateTypeDef",
    "KinesisVideoStreamPoolSummaryTypeDef",
    "RecordingStreamConfigurationTypeDef",
    "KinesisVideoStreamSourceTaskConfigurationTypeDef",
    "LambdaFunctionSinkConfigurationTypeDef",
    "ListMediaCapturePipelinesRequestRequestTypeDef",
    "MediaCapturePipelineSummaryTypeDef",
    "ListMediaInsightsPipelineConfigurationsRequestRequestTypeDef",
    "MediaInsightsPipelineConfigurationSummaryTypeDef",
    "ListMediaPipelineKinesisVideoStreamPoolsRequestRequestTypeDef",
    "ListMediaPipelinesRequestRequestTypeDef",
    "MediaPipelineSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "LiveConnectorRTMPConfigurationTypeDef",
    "S3RecordingSinkConfigurationTypeDef",
    "SnsTopicSinkConfigurationTypeDef",
    "SqsQueueSinkConfigurationTypeDef",
    "VoiceAnalyticsProcessorConfigurationTypeDef",
    "VoiceEnhancementSinkConfigurationTypeDef",
    "MediaInsightsPipelineElementStatusTypeDef",
    "SentimentConfigurationTypeDef",
    "SelectedVideoStreamsOutputTypeDef",
    "SelectedVideoStreamsTypeDef",
    "StopSpeakerSearchTaskRequestRequestTypeDef",
    "StopVoiceToneAnalysisTaskRequestRequestTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateMediaInsightsPipelineStatusRequestRequestTypeDef",
    "AmazonTranscribeCallAnalyticsProcessorConfigurationOutputTypeDef",
    "AmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef",
    "ArtifactsConcatenationConfigurationTypeDef",
    "StreamChannelDefinitionOutputTypeDef",
    "StreamChannelDefinitionTypeDef",
    "ConcatenationSinkTypeDef",
    "TagResourceRequestRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "CreateMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef",
    "KinesisVideoStreamPoolConfigurationTypeDef",
    "CreateMediaStreamPipelineRequestRequestTypeDef",
    "MediaStreamPipelineTypeDef",
    "FragmentSelectorOutputTypeDef",
    "GetSpeakerSearchTaskResponseTypeDef",
    "StartSpeakerSearchTaskResponseTypeDef",
    "GetVoiceToneAnalysisTaskResponseTypeDef",
    "StartVoiceToneAnalysisTaskResponseTypeDef",
    "GridViewConfigurationTypeDef",
    "KeywordMatchConfigurationUnionTypeDef",
    "UpdateMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef",
    "ListMediaPipelineKinesisVideoStreamPoolsResponseTypeDef",
    "StartSpeakerSearchTaskRequestRequestTypeDef",
    "StartVoiceToneAnalysisTaskRequestRequestTypeDef",
    "ListMediaCapturePipelinesResponseTypeDef",
    "ListMediaInsightsPipelineConfigurationsResponseTypeDef",
    "ListMediaPipelinesResponseTypeDef",
    "LiveConnectorSinkConfigurationTypeDef",
    "RealTimeAlertRuleOutputTypeDef",
    "SourceConfigurationOutputTypeDef",
    "SelectedVideoStreamsUnionTypeDef",
    "TimestampRangeTypeDef",
    "MediaInsightsPipelineConfigurationElementOutputTypeDef",
    "AmazonTranscribeCallAnalyticsProcessorConfigurationUnionTypeDef",
    "ChimeSdkMeetingConcatenationConfigurationTypeDef",
    "StreamConfigurationOutputTypeDef",
    "StreamChannelDefinitionUnionTypeDef",
    "CreateMediaPipelineKinesisVideoStreamPoolResponseTypeDef",
    "GetMediaPipelineKinesisVideoStreamPoolResponseTypeDef",
    "UpdateMediaPipelineKinesisVideoStreamPoolResponseTypeDef",
    "CreateMediaStreamPipelineResponseTypeDef",
    "KinesisVideoStreamRecordingSourceRuntimeConfigurationOutputTypeDef",
    "CompositedVideoArtifactsConfigurationTypeDef",
    "RealTimeAlertRuleTypeDef",
    "RealTimeAlertConfigurationOutputTypeDef",
    "SourceConfigurationTypeDef",
    "TimestampRangeUnionTypeDef",
    "MediaInsightsPipelineConfigurationElementTypeDef",
    "MediaCapturePipelineSourceConfigurationTypeDef",
    "KinesisVideoStreamSourceRuntimeConfigurationOutputTypeDef",
    "StreamConfigurationTypeDef",
    "ArtifactsConfigurationTypeDef",
    "ChimeSdkMeetingLiveConnectorConfigurationOutputTypeDef",
    "RealTimeAlertRuleUnionTypeDef",
    "MediaInsightsPipelineConfigurationTypeDef",
    "SourceConfigurationUnionTypeDef",
    "FragmentSelectorTypeDef",
    "MediaInsightsPipelineConfigurationElementUnionTypeDef",
    "ConcatenationSourceTypeDef",
    "MediaInsightsPipelineTypeDef",
    "StreamConfigurationUnionTypeDef",
    "ChimeSdkMeetingConfigurationOutputTypeDef",
    "LiveConnectorSourceConfigurationOutputTypeDef",
    "RealTimeAlertConfigurationTypeDef",
    "CreateMediaInsightsPipelineConfigurationResponseTypeDef",
    "GetMediaInsightsPipelineConfigurationResponseTypeDef",
    "UpdateMediaInsightsPipelineConfigurationResponseTypeDef",
    "ChimeSdkMeetingConfigurationTypeDef",
    "ChimeSdkMeetingLiveConnectorConfigurationTypeDef",
    "FragmentSelectorUnionTypeDef",
    "CreateMediaConcatenationPipelineRequestRequestTypeDef",
    "MediaConcatenationPipelineTypeDef",
    "CreateMediaInsightsPipelineResponseTypeDef",
    "KinesisVideoStreamSourceRuntimeConfigurationTypeDef",
    "MediaCapturePipelineTypeDef",
    "MediaLiveConnectorPipelineTypeDef",
    "CreateMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    "UpdateMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    "CreateMediaCapturePipelineRequestRequestTypeDef",
    "ChimeSdkMeetingLiveConnectorConfigurationUnionTypeDef",
    "KinesisVideoStreamRecordingSourceRuntimeConfigurationTypeDef",
    "CreateMediaConcatenationPipelineResponseTypeDef",
    "CreateMediaCapturePipelineResponseTypeDef",
    "GetMediaCapturePipelineResponseTypeDef",
    "CreateMediaLiveConnectorPipelineResponseTypeDef",
    "MediaPipelineTypeDef",
    "LiveConnectorSourceConfigurationTypeDef",
    "CreateMediaInsightsPipelineRequestRequestTypeDef",
    "GetMediaPipelineResponseTypeDef",
    "LiveConnectorSourceConfigurationUnionTypeDef",
    "CreateMediaLiveConnectorPipelineRequestRequestTypeDef",
)

ActiveSpeakerOnlyConfigurationTypeDef = TypedDict(
    "ActiveSpeakerOnlyConfigurationTypeDef",
    {
        "ActiveSpeakerPosition": NotRequired[ActiveSpeakerPositionType],
    },
)
PostCallAnalyticsSettingsTypeDef = TypedDict(
    "PostCallAnalyticsSettingsTypeDef",
    {
        "OutputLocation": str,
        "DataAccessRoleArn": str,
        "ContentRedactionOutput": NotRequired[ContentRedactionOutputType],
        "OutputEncryptionKMSKeyId": NotRequired[str],
    },
)
AmazonTranscribeProcessorConfigurationTypeDef = TypedDict(
    "AmazonTranscribeProcessorConfigurationTypeDef",
    {
        "LanguageCode": NotRequired[CallAnalyticsLanguageCodeType],
        "VocabularyName": NotRequired[str],
        "VocabularyFilterName": NotRequired[str],
        "VocabularyFilterMethod": NotRequired[VocabularyFilterMethodType],
        "ShowSpeakerLabel": NotRequired[bool],
        "EnablePartialResultsStabilization": NotRequired[bool],
        "PartialResultsStability": NotRequired[PartialResultsStabilityType],
        "ContentIdentificationType": NotRequired[Literal["PII"]],
        "ContentRedactionType": NotRequired[Literal["PII"]],
        "PiiEntityTypes": NotRequired[str],
        "LanguageModelName": NotRequired[str],
        "FilterPartialResults": NotRequired[bool],
        "IdentifyLanguage": NotRequired[bool],
        "IdentifyMultipleLanguages": NotRequired[bool],
        "LanguageOptions": NotRequired[str],
        "PreferredLanguage": NotRequired[CallAnalyticsLanguageCodeType],
        "VocabularyNames": NotRequired[str],
        "VocabularyFilterNames": NotRequired[str],
    },
)
AudioConcatenationConfigurationTypeDef = TypedDict(
    "AudioConcatenationConfigurationTypeDef",
    {
        "State": Literal["Enabled"],
    },
)
CompositedVideoConcatenationConfigurationTypeDef = TypedDict(
    "CompositedVideoConcatenationConfigurationTypeDef",
    {
        "State": ArtifactsConcatenationStateType,
    },
)
ContentConcatenationConfigurationTypeDef = TypedDict(
    "ContentConcatenationConfigurationTypeDef",
    {
        "State": ArtifactsConcatenationStateType,
    },
)
DataChannelConcatenationConfigurationTypeDef = TypedDict(
    "DataChannelConcatenationConfigurationTypeDef",
    {
        "State": ArtifactsConcatenationStateType,
    },
)
MeetingEventsConcatenationConfigurationTypeDef = TypedDict(
    "MeetingEventsConcatenationConfigurationTypeDef",
    {
        "State": ArtifactsConcatenationStateType,
    },
)
TranscriptionMessagesConcatenationConfigurationTypeDef = TypedDict(
    "TranscriptionMessagesConcatenationConfigurationTypeDef",
    {
        "State": ArtifactsConcatenationStateType,
    },
)
VideoConcatenationConfigurationTypeDef = TypedDict(
    "VideoConcatenationConfigurationTypeDef",
    {
        "State": ArtifactsConcatenationStateType,
    },
)
AudioArtifactsConfigurationTypeDef = TypedDict(
    "AudioArtifactsConfigurationTypeDef",
    {
        "MuxType": AudioMuxTypeType,
    },
)
ContentArtifactsConfigurationTypeDef = TypedDict(
    "ContentArtifactsConfigurationTypeDef",
    {
        "State": ArtifactsStateType,
        "MuxType": NotRequired[Literal["ContentOnly"]],
    },
)
VideoArtifactsConfigurationTypeDef = TypedDict(
    "VideoArtifactsConfigurationTypeDef",
    {
        "State": ArtifactsStateType,
        "MuxType": NotRequired[Literal["VideoOnly"]],
    },
)
ChannelDefinitionTypeDef = TypedDict(
    "ChannelDefinitionTypeDef",
    {
        "ChannelId": int,
        "ParticipantRole": NotRequired[ParticipantRoleType],
    },
)
S3BucketSinkConfigurationTypeDef = TypedDict(
    "S3BucketSinkConfigurationTypeDef",
    {
        "Destination": str,
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
S3RecordingSinkRuntimeConfigurationTypeDef = TypedDict(
    "S3RecordingSinkRuntimeConfigurationTypeDef",
    {
        "Destination": str,
        "RecordingFileFormat": RecordingFileFormatType,
    },
)
KinesisVideoStreamConfigurationTypeDef = TypedDict(
    "KinesisVideoStreamConfigurationTypeDef",
    {
        "Region": str,
        "DataRetentionInHours": NotRequired[int],
    },
)
MediaStreamSinkTypeDef = TypedDict(
    "MediaStreamSinkTypeDef",
    {
        "SinkArn": str,
        "SinkType": Literal["KinesisVideoStreamPool"],
        "ReservedStreamCapacity": int,
        "MediaStreamType": MediaStreamTypeType,
    },
)
MediaStreamSourceTypeDef = TypedDict(
    "MediaStreamSourceTypeDef",
    {
        "SourceType": Literal["ChimeSdkMeeting"],
        "SourceArn": str,
    },
)
DeleteMediaCapturePipelineRequestRequestTypeDef = TypedDict(
    "DeleteMediaCapturePipelineRequestRequestTypeDef",
    {
        "MediaPipelineId": str,
    },
)
DeleteMediaInsightsPipelineConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)
DeleteMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef = TypedDict(
    "DeleteMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)
DeleteMediaPipelineRequestRequestTypeDef = TypedDict(
    "DeleteMediaPipelineRequestRequestTypeDef",
    {
        "MediaPipelineId": str,
    },
)
TimestampRangeOutputTypeDef = TypedDict(
    "TimestampRangeOutputTypeDef",
    {
        "StartTimestamp": datetime,
        "EndTimestamp": datetime,
    },
)
GetMediaCapturePipelineRequestRequestTypeDef = TypedDict(
    "GetMediaCapturePipelineRequestRequestTypeDef",
    {
        "MediaPipelineId": str,
    },
)
GetMediaInsightsPipelineConfigurationRequestRequestTypeDef = TypedDict(
    "GetMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)
GetMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef = TypedDict(
    "GetMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)
GetMediaPipelineRequestRequestTypeDef = TypedDict(
    "GetMediaPipelineRequestRequestTypeDef",
    {
        "MediaPipelineId": str,
    },
)
GetSpeakerSearchTaskRequestRequestTypeDef = TypedDict(
    "GetSpeakerSearchTaskRequestRequestTypeDef",
    {
        "Identifier": str,
        "SpeakerSearchTaskId": str,
    },
)
SpeakerSearchTaskTypeDef = TypedDict(
    "SpeakerSearchTaskTypeDef",
    {
        "SpeakerSearchTaskId": NotRequired[str],
        "SpeakerSearchTaskStatus": NotRequired[MediaPipelineTaskStatusType],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
    },
)
GetVoiceToneAnalysisTaskRequestRequestTypeDef = TypedDict(
    "GetVoiceToneAnalysisTaskRequestRequestTypeDef",
    {
        "Identifier": str,
        "VoiceToneAnalysisTaskId": str,
    },
)
VoiceToneAnalysisTaskTypeDef = TypedDict(
    "VoiceToneAnalysisTaskTypeDef",
    {
        "VoiceToneAnalysisTaskId": NotRequired[str],
        "VoiceToneAnalysisTaskStatus": NotRequired[MediaPipelineTaskStatusType],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
    },
)
HorizontalLayoutConfigurationTypeDef = TypedDict(
    "HorizontalLayoutConfigurationTypeDef",
    {
        "TileOrder": NotRequired[TileOrderType],
        "TilePosition": NotRequired[HorizontalTilePositionType],
        "TileCount": NotRequired[int],
        "TileAspectRatio": NotRequired[str],
    },
)
PresenterOnlyConfigurationTypeDef = TypedDict(
    "PresenterOnlyConfigurationTypeDef",
    {
        "PresenterPosition": NotRequired[PresenterPositionType],
    },
)
VerticalLayoutConfigurationTypeDef = TypedDict(
    "VerticalLayoutConfigurationTypeDef",
    {
        "TileOrder": NotRequired[TileOrderType],
        "TilePosition": NotRequired[VerticalTilePositionType],
        "TileCount": NotRequired[int],
        "TileAspectRatio": NotRequired[str],
    },
)
VideoAttributeTypeDef = TypedDict(
    "VideoAttributeTypeDef",
    {
        "CornerRadius": NotRequired[int],
        "BorderColor": NotRequired[BorderColorType],
        "HighlightColor": NotRequired[HighlightColorType],
        "BorderThickness": NotRequired[int],
    },
)
IssueDetectionConfigurationTypeDef = TypedDict(
    "IssueDetectionConfigurationTypeDef",
    {
        "RuleName": str,
    },
)
KeywordMatchConfigurationOutputTypeDef = TypedDict(
    "KeywordMatchConfigurationOutputTypeDef",
    {
        "RuleName": str,
        "Keywords": List[str],
        "Negate": NotRequired[bool],
    },
)
KeywordMatchConfigurationTypeDef = TypedDict(
    "KeywordMatchConfigurationTypeDef",
    {
        "RuleName": str,
        "Keywords": Sequence[str],
        "Negate": NotRequired[bool],
    },
)
KinesisDataStreamSinkConfigurationTypeDef = TypedDict(
    "KinesisDataStreamSinkConfigurationTypeDef",
    {
        "InsightsTarget": NotRequired[str],
    },
)
KinesisVideoStreamConfigurationUpdateTypeDef = TypedDict(
    "KinesisVideoStreamConfigurationUpdateTypeDef",
    {
        "DataRetentionInHours": NotRequired[int],
    },
)
KinesisVideoStreamPoolSummaryTypeDef = TypedDict(
    "KinesisVideoStreamPoolSummaryTypeDef",
    {
        "PoolName": NotRequired[str],
        "PoolId": NotRequired[str],
        "PoolArn": NotRequired[str],
    },
)
RecordingStreamConfigurationTypeDef = TypedDict(
    "RecordingStreamConfigurationTypeDef",
    {
        "StreamArn": NotRequired[str],
    },
)
KinesisVideoStreamSourceTaskConfigurationTypeDef = TypedDict(
    "KinesisVideoStreamSourceTaskConfigurationTypeDef",
    {
        "StreamArn": str,
        "ChannelId": int,
        "FragmentNumber": NotRequired[str],
    },
)
LambdaFunctionSinkConfigurationTypeDef = TypedDict(
    "LambdaFunctionSinkConfigurationTypeDef",
    {
        "InsightsTarget": NotRequired[str],
    },
)
ListMediaCapturePipelinesRequestRequestTypeDef = TypedDict(
    "ListMediaCapturePipelinesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
MediaCapturePipelineSummaryTypeDef = TypedDict(
    "MediaCapturePipelineSummaryTypeDef",
    {
        "MediaPipelineId": NotRequired[str],
        "MediaPipelineArn": NotRequired[str],
    },
)
ListMediaInsightsPipelineConfigurationsRequestRequestTypeDef = TypedDict(
    "ListMediaInsightsPipelineConfigurationsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
MediaInsightsPipelineConfigurationSummaryTypeDef = TypedDict(
    "MediaInsightsPipelineConfigurationSummaryTypeDef",
    {
        "MediaInsightsPipelineConfigurationName": NotRequired[str],
        "MediaInsightsPipelineConfigurationId": NotRequired[str],
        "MediaInsightsPipelineConfigurationArn": NotRequired[str],
    },
)
ListMediaPipelineKinesisVideoStreamPoolsRequestRequestTypeDef = TypedDict(
    "ListMediaPipelineKinesisVideoStreamPoolsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListMediaPipelinesRequestRequestTypeDef = TypedDict(
    "ListMediaPipelinesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
MediaPipelineSummaryTypeDef = TypedDict(
    "MediaPipelineSummaryTypeDef",
    {
        "MediaPipelineId": NotRequired[str],
        "MediaPipelineArn": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
LiveConnectorRTMPConfigurationTypeDef = TypedDict(
    "LiveConnectorRTMPConfigurationTypeDef",
    {
        "Url": str,
        "AudioChannels": NotRequired[AudioChannelsOptionType],
        "AudioSampleRate": NotRequired[str],
    },
)
S3RecordingSinkConfigurationTypeDef = TypedDict(
    "S3RecordingSinkConfigurationTypeDef",
    {
        "Destination": NotRequired[str],
        "RecordingFileFormat": NotRequired[RecordingFileFormatType],
    },
)
SnsTopicSinkConfigurationTypeDef = TypedDict(
    "SnsTopicSinkConfigurationTypeDef",
    {
        "InsightsTarget": NotRequired[str],
    },
)
SqsQueueSinkConfigurationTypeDef = TypedDict(
    "SqsQueueSinkConfigurationTypeDef",
    {
        "InsightsTarget": NotRequired[str],
    },
)
VoiceAnalyticsProcessorConfigurationTypeDef = TypedDict(
    "VoiceAnalyticsProcessorConfigurationTypeDef",
    {
        "SpeakerSearchStatus": NotRequired[VoiceAnalyticsConfigurationStatusType],
        "VoiceToneAnalysisStatus": NotRequired[VoiceAnalyticsConfigurationStatusType],
    },
)
VoiceEnhancementSinkConfigurationTypeDef = TypedDict(
    "VoiceEnhancementSinkConfigurationTypeDef",
    {
        "Disabled": NotRequired[bool],
    },
)
MediaInsightsPipelineElementStatusTypeDef = TypedDict(
    "MediaInsightsPipelineElementStatusTypeDef",
    {
        "Type": NotRequired[MediaInsightsPipelineConfigurationElementTypeType],
        "Status": NotRequired[MediaPipelineElementStatusType],
    },
)
SentimentConfigurationTypeDef = TypedDict(
    "SentimentConfigurationTypeDef",
    {
        "RuleName": str,
        "SentimentType": Literal["NEGATIVE"],
        "TimePeriod": int,
    },
)
SelectedVideoStreamsOutputTypeDef = TypedDict(
    "SelectedVideoStreamsOutputTypeDef",
    {
        "AttendeeIds": NotRequired[List[str]],
        "ExternalUserIds": NotRequired[List[str]],
    },
)
SelectedVideoStreamsTypeDef = TypedDict(
    "SelectedVideoStreamsTypeDef",
    {
        "AttendeeIds": NotRequired[Sequence[str]],
        "ExternalUserIds": NotRequired[Sequence[str]],
    },
)
StopSpeakerSearchTaskRequestRequestTypeDef = TypedDict(
    "StopSpeakerSearchTaskRequestRequestTypeDef",
    {
        "Identifier": str,
        "SpeakerSearchTaskId": str,
    },
)
StopVoiceToneAnalysisTaskRequestRequestTypeDef = TypedDict(
    "StopVoiceToneAnalysisTaskRequestRequestTypeDef",
    {
        "Identifier": str,
        "VoiceToneAnalysisTaskId": str,
    },
)
TimestampTypeDef = Union[datetime, str]
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
UpdateMediaInsightsPipelineStatusRequestRequestTypeDef = TypedDict(
    "UpdateMediaInsightsPipelineStatusRequestRequestTypeDef",
    {
        "Identifier": str,
        "UpdateStatus": MediaPipelineStatusUpdateType,
    },
)
AmazonTranscribeCallAnalyticsProcessorConfigurationOutputTypeDef = TypedDict(
    "AmazonTranscribeCallAnalyticsProcessorConfigurationOutputTypeDef",
    {
        "LanguageCode": CallAnalyticsLanguageCodeType,
        "VocabularyName": NotRequired[str],
        "VocabularyFilterName": NotRequired[str],
        "VocabularyFilterMethod": NotRequired[VocabularyFilterMethodType],
        "LanguageModelName": NotRequired[str],
        "EnablePartialResultsStabilization": NotRequired[bool],
        "PartialResultsStability": NotRequired[PartialResultsStabilityType],
        "ContentIdentificationType": NotRequired[Literal["PII"]],
        "ContentRedactionType": NotRequired[Literal["PII"]],
        "PiiEntityTypes": NotRequired[str],
        "FilterPartialResults": NotRequired[bool],
        "PostCallAnalyticsSettings": NotRequired[PostCallAnalyticsSettingsTypeDef],
        "CallAnalyticsStreamCategories": NotRequired[List[str]],
    },
)
AmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef = TypedDict(
    "AmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef",
    {
        "LanguageCode": CallAnalyticsLanguageCodeType,
        "VocabularyName": NotRequired[str],
        "VocabularyFilterName": NotRequired[str],
        "VocabularyFilterMethod": NotRequired[VocabularyFilterMethodType],
        "LanguageModelName": NotRequired[str],
        "EnablePartialResultsStabilization": NotRequired[bool],
        "PartialResultsStability": NotRequired[PartialResultsStabilityType],
        "ContentIdentificationType": NotRequired[Literal["PII"]],
        "ContentRedactionType": NotRequired[Literal["PII"]],
        "PiiEntityTypes": NotRequired[str],
        "FilterPartialResults": NotRequired[bool],
        "PostCallAnalyticsSettings": NotRequired[PostCallAnalyticsSettingsTypeDef],
        "CallAnalyticsStreamCategories": NotRequired[Sequence[str]],
    },
)
ArtifactsConcatenationConfigurationTypeDef = TypedDict(
    "ArtifactsConcatenationConfigurationTypeDef",
    {
        "Audio": AudioConcatenationConfigurationTypeDef,
        "Video": VideoConcatenationConfigurationTypeDef,
        "Content": ContentConcatenationConfigurationTypeDef,
        "DataChannel": DataChannelConcatenationConfigurationTypeDef,
        "TranscriptionMessages": TranscriptionMessagesConcatenationConfigurationTypeDef,
        "MeetingEvents": MeetingEventsConcatenationConfigurationTypeDef,
        "CompositedVideo": CompositedVideoConcatenationConfigurationTypeDef,
    },
)
StreamChannelDefinitionOutputTypeDef = TypedDict(
    "StreamChannelDefinitionOutputTypeDef",
    {
        "NumberOfChannels": int,
        "ChannelDefinitions": NotRequired[List[ChannelDefinitionTypeDef]],
    },
)
StreamChannelDefinitionTypeDef = TypedDict(
    "StreamChannelDefinitionTypeDef",
    {
        "NumberOfChannels": int,
        "ChannelDefinitions": NotRequired[Sequence[ChannelDefinitionTypeDef]],
    },
)
ConcatenationSinkTypeDef = TypedDict(
    "ConcatenationSinkTypeDef",
    {
        "Type": Literal["S3Bucket"],
        "S3BucketSinkConfiguration": S3BucketSinkConfigurationTypeDef,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
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
CreateMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef = TypedDict(
    "CreateMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef",
    {
        "StreamConfiguration": KinesisVideoStreamConfigurationTypeDef,
        "PoolName": str,
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
KinesisVideoStreamPoolConfigurationTypeDef = TypedDict(
    "KinesisVideoStreamPoolConfigurationTypeDef",
    {
        "PoolArn": NotRequired[str],
        "PoolName": NotRequired[str],
        "PoolId": NotRequired[str],
        "PoolStatus": NotRequired[KinesisVideoStreamPoolStatusType],
        "PoolSize": NotRequired[int],
        "StreamConfiguration": NotRequired[KinesisVideoStreamConfigurationTypeDef],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
    },
)
CreateMediaStreamPipelineRequestRequestTypeDef = TypedDict(
    "CreateMediaStreamPipelineRequestRequestTypeDef",
    {
        "Sources": Sequence[MediaStreamSourceTypeDef],
        "Sinks": Sequence[MediaStreamSinkTypeDef],
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
MediaStreamPipelineTypeDef = TypedDict(
    "MediaStreamPipelineTypeDef",
    {
        "MediaPipelineId": NotRequired[str],
        "MediaPipelineArn": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
        "Status": NotRequired[MediaPipelineStatusType],
        "Sources": NotRequired[List[MediaStreamSourceTypeDef]],
        "Sinks": NotRequired[List[MediaStreamSinkTypeDef]],
    },
)
FragmentSelectorOutputTypeDef = TypedDict(
    "FragmentSelectorOutputTypeDef",
    {
        "FragmentSelectorType": FragmentSelectorTypeType,
        "TimestampRange": TimestampRangeOutputTypeDef,
    },
)
GetSpeakerSearchTaskResponseTypeDef = TypedDict(
    "GetSpeakerSearchTaskResponseTypeDef",
    {
        "SpeakerSearchTask": SpeakerSearchTaskTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartSpeakerSearchTaskResponseTypeDef = TypedDict(
    "StartSpeakerSearchTaskResponseTypeDef",
    {
        "SpeakerSearchTask": SpeakerSearchTaskTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetVoiceToneAnalysisTaskResponseTypeDef = TypedDict(
    "GetVoiceToneAnalysisTaskResponseTypeDef",
    {
        "VoiceToneAnalysisTask": VoiceToneAnalysisTaskTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartVoiceToneAnalysisTaskResponseTypeDef = TypedDict(
    "StartVoiceToneAnalysisTaskResponseTypeDef",
    {
        "VoiceToneAnalysisTask": VoiceToneAnalysisTaskTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GridViewConfigurationTypeDef = TypedDict(
    "GridViewConfigurationTypeDef",
    {
        "ContentShareLayout": ContentShareLayoutOptionType,
        "PresenterOnlyConfiguration": NotRequired[PresenterOnlyConfigurationTypeDef],
        "ActiveSpeakerOnlyConfiguration": NotRequired[ActiveSpeakerOnlyConfigurationTypeDef],
        "HorizontalLayoutConfiguration": NotRequired[HorizontalLayoutConfigurationTypeDef],
        "VerticalLayoutConfiguration": NotRequired[VerticalLayoutConfigurationTypeDef],
        "VideoAttribute": NotRequired[VideoAttributeTypeDef],
        "CanvasOrientation": NotRequired[CanvasOrientationType],
    },
)
KeywordMatchConfigurationUnionTypeDef = Union[
    KeywordMatchConfigurationTypeDef, KeywordMatchConfigurationOutputTypeDef
]
UpdateMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef = TypedDict(
    "UpdateMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef",
    {
        "Identifier": str,
        "StreamConfiguration": NotRequired[KinesisVideoStreamConfigurationUpdateTypeDef],
    },
)
ListMediaPipelineKinesisVideoStreamPoolsResponseTypeDef = TypedDict(
    "ListMediaPipelineKinesisVideoStreamPoolsResponseTypeDef",
    {
        "KinesisVideoStreamPools": List[KinesisVideoStreamPoolSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
StartSpeakerSearchTaskRequestRequestTypeDef = TypedDict(
    "StartSpeakerSearchTaskRequestRequestTypeDef",
    {
        "Identifier": str,
        "VoiceProfileDomainArn": str,
        "KinesisVideoStreamSourceTaskConfiguration": NotRequired[
            KinesisVideoStreamSourceTaskConfigurationTypeDef
        ],
        "ClientRequestToken": NotRequired[str],
    },
)
StartVoiceToneAnalysisTaskRequestRequestTypeDef = TypedDict(
    "StartVoiceToneAnalysisTaskRequestRequestTypeDef",
    {
        "Identifier": str,
        "LanguageCode": Literal["en-US"],
        "KinesisVideoStreamSourceTaskConfiguration": NotRequired[
            KinesisVideoStreamSourceTaskConfigurationTypeDef
        ],
        "ClientRequestToken": NotRequired[str],
    },
)
ListMediaCapturePipelinesResponseTypeDef = TypedDict(
    "ListMediaCapturePipelinesResponseTypeDef",
    {
        "MediaCapturePipelines": List[MediaCapturePipelineSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListMediaInsightsPipelineConfigurationsResponseTypeDef = TypedDict(
    "ListMediaInsightsPipelineConfigurationsResponseTypeDef",
    {
        "MediaInsightsPipelineConfigurations": List[
            MediaInsightsPipelineConfigurationSummaryTypeDef
        ],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListMediaPipelinesResponseTypeDef = TypedDict(
    "ListMediaPipelinesResponseTypeDef",
    {
        "MediaPipelines": List[MediaPipelineSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
LiveConnectorSinkConfigurationTypeDef = TypedDict(
    "LiveConnectorSinkConfigurationTypeDef",
    {
        "SinkType": Literal["RTMP"],
        "RTMPConfiguration": LiveConnectorRTMPConfigurationTypeDef,
    },
)
RealTimeAlertRuleOutputTypeDef = TypedDict(
    "RealTimeAlertRuleOutputTypeDef",
    {
        "Type": RealTimeAlertRuleTypeType,
        "KeywordMatchConfiguration": NotRequired[KeywordMatchConfigurationOutputTypeDef],
        "SentimentConfiguration": NotRequired[SentimentConfigurationTypeDef],
        "IssueDetectionConfiguration": NotRequired[IssueDetectionConfigurationTypeDef],
    },
)
SourceConfigurationOutputTypeDef = TypedDict(
    "SourceConfigurationOutputTypeDef",
    {
        "SelectedVideoStreams": NotRequired[SelectedVideoStreamsOutputTypeDef],
    },
)
SelectedVideoStreamsUnionTypeDef = Union[
    SelectedVideoStreamsTypeDef, SelectedVideoStreamsOutputTypeDef
]
TimestampRangeTypeDef = TypedDict(
    "TimestampRangeTypeDef",
    {
        "StartTimestamp": TimestampTypeDef,
        "EndTimestamp": TimestampTypeDef,
    },
)
MediaInsightsPipelineConfigurationElementOutputTypeDef = TypedDict(
    "MediaInsightsPipelineConfigurationElementOutputTypeDef",
    {
        "Type": MediaInsightsPipelineConfigurationElementTypeType,
        "AmazonTranscribeCallAnalyticsProcessorConfiguration": NotRequired[
            AmazonTranscribeCallAnalyticsProcessorConfigurationOutputTypeDef
        ],
        "AmazonTranscribeProcessorConfiguration": NotRequired[
            AmazonTranscribeProcessorConfigurationTypeDef
        ],
        "KinesisDataStreamSinkConfiguration": NotRequired[
            KinesisDataStreamSinkConfigurationTypeDef
        ],
        "S3RecordingSinkConfiguration": NotRequired[S3RecordingSinkConfigurationTypeDef],
        "VoiceAnalyticsProcessorConfiguration": NotRequired[
            VoiceAnalyticsProcessorConfigurationTypeDef
        ],
        "LambdaFunctionSinkConfiguration": NotRequired[LambdaFunctionSinkConfigurationTypeDef],
        "SqsQueueSinkConfiguration": NotRequired[SqsQueueSinkConfigurationTypeDef],
        "SnsTopicSinkConfiguration": NotRequired[SnsTopicSinkConfigurationTypeDef],
        "VoiceEnhancementSinkConfiguration": NotRequired[VoiceEnhancementSinkConfigurationTypeDef],
    },
)
AmazonTranscribeCallAnalyticsProcessorConfigurationUnionTypeDef = Union[
    AmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef,
    AmazonTranscribeCallAnalyticsProcessorConfigurationOutputTypeDef,
]
ChimeSdkMeetingConcatenationConfigurationTypeDef = TypedDict(
    "ChimeSdkMeetingConcatenationConfigurationTypeDef",
    {
        "ArtifactsConfiguration": ArtifactsConcatenationConfigurationTypeDef,
    },
)
StreamConfigurationOutputTypeDef = TypedDict(
    "StreamConfigurationOutputTypeDef",
    {
        "StreamArn": str,
        "StreamChannelDefinition": StreamChannelDefinitionOutputTypeDef,
        "FragmentNumber": NotRequired[str],
    },
)
StreamChannelDefinitionUnionTypeDef = Union[
    StreamChannelDefinitionTypeDef, StreamChannelDefinitionOutputTypeDef
]
CreateMediaPipelineKinesisVideoStreamPoolResponseTypeDef = TypedDict(
    "CreateMediaPipelineKinesisVideoStreamPoolResponseTypeDef",
    {
        "KinesisVideoStreamPoolConfiguration": KinesisVideoStreamPoolConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMediaPipelineKinesisVideoStreamPoolResponseTypeDef = TypedDict(
    "GetMediaPipelineKinesisVideoStreamPoolResponseTypeDef",
    {
        "KinesisVideoStreamPoolConfiguration": KinesisVideoStreamPoolConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateMediaPipelineKinesisVideoStreamPoolResponseTypeDef = TypedDict(
    "UpdateMediaPipelineKinesisVideoStreamPoolResponseTypeDef",
    {
        "KinesisVideoStreamPoolConfiguration": KinesisVideoStreamPoolConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMediaStreamPipelineResponseTypeDef = TypedDict(
    "CreateMediaStreamPipelineResponseTypeDef",
    {
        "MediaStreamPipeline": MediaStreamPipelineTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
KinesisVideoStreamRecordingSourceRuntimeConfigurationOutputTypeDef = TypedDict(
    "KinesisVideoStreamRecordingSourceRuntimeConfigurationOutputTypeDef",
    {
        "Streams": List[RecordingStreamConfigurationTypeDef],
        "FragmentSelector": FragmentSelectorOutputTypeDef,
    },
)
CompositedVideoArtifactsConfigurationTypeDef = TypedDict(
    "CompositedVideoArtifactsConfigurationTypeDef",
    {
        "GridViewConfiguration": GridViewConfigurationTypeDef,
        "Layout": NotRequired[Literal["GridView"]],
        "Resolution": NotRequired[ResolutionOptionType],
    },
)
RealTimeAlertRuleTypeDef = TypedDict(
    "RealTimeAlertRuleTypeDef",
    {
        "Type": RealTimeAlertRuleTypeType,
        "KeywordMatchConfiguration": NotRequired[KeywordMatchConfigurationUnionTypeDef],
        "SentimentConfiguration": NotRequired[SentimentConfigurationTypeDef],
        "IssueDetectionConfiguration": NotRequired[IssueDetectionConfigurationTypeDef],
    },
)
RealTimeAlertConfigurationOutputTypeDef = TypedDict(
    "RealTimeAlertConfigurationOutputTypeDef",
    {
        "Disabled": NotRequired[bool],
        "Rules": NotRequired[List[RealTimeAlertRuleOutputTypeDef]],
    },
)
SourceConfigurationTypeDef = TypedDict(
    "SourceConfigurationTypeDef",
    {
        "SelectedVideoStreams": NotRequired[SelectedVideoStreamsUnionTypeDef],
    },
)
TimestampRangeUnionTypeDef = Union[TimestampRangeTypeDef, TimestampRangeOutputTypeDef]
MediaInsightsPipelineConfigurationElementTypeDef = TypedDict(
    "MediaInsightsPipelineConfigurationElementTypeDef",
    {
        "Type": MediaInsightsPipelineConfigurationElementTypeType,
        "AmazonTranscribeCallAnalyticsProcessorConfiguration": NotRequired[
            AmazonTranscribeCallAnalyticsProcessorConfigurationUnionTypeDef
        ],
        "AmazonTranscribeProcessorConfiguration": NotRequired[
            AmazonTranscribeProcessorConfigurationTypeDef
        ],
        "KinesisDataStreamSinkConfiguration": NotRequired[
            KinesisDataStreamSinkConfigurationTypeDef
        ],
        "S3RecordingSinkConfiguration": NotRequired[S3RecordingSinkConfigurationTypeDef],
        "VoiceAnalyticsProcessorConfiguration": NotRequired[
            VoiceAnalyticsProcessorConfigurationTypeDef
        ],
        "LambdaFunctionSinkConfiguration": NotRequired[LambdaFunctionSinkConfigurationTypeDef],
        "SqsQueueSinkConfiguration": NotRequired[SqsQueueSinkConfigurationTypeDef],
        "SnsTopicSinkConfiguration": NotRequired[SnsTopicSinkConfigurationTypeDef],
        "VoiceEnhancementSinkConfiguration": NotRequired[VoiceEnhancementSinkConfigurationTypeDef],
    },
)
MediaCapturePipelineSourceConfigurationTypeDef = TypedDict(
    "MediaCapturePipelineSourceConfigurationTypeDef",
    {
        "MediaPipelineArn": str,
        "ChimeSdkMeetingConfiguration": ChimeSdkMeetingConcatenationConfigurationTypeDef,
    },
)
KinesisVideoStreamSourceRuntimeConfigurationOutputTypeDef = TypedDict(
    "KinesisVideoStreamSourceRuntimeConfigurationOutputTypeDef",
    {
        "Streams": List[StreamConfigurationOutputTypeDef],
        "MediaEncoding": Literal["pcm"],
        "MediaSampleRate": int,
    },
)
StreamConfigurationTypeDef = TypedDict(
    "StreamConfigurationTypeDef",
    {
        "StreamArn": str,
        "StreamChannelDefinition": StreamChannelDefinitionUnionTypeDef,
        "FragmentNumber": NotRequired[str],
    },
)
ArtifactsConfigurationTypeDef = TypedDict(
    "ArtifactsConfigurationTypeDef",
    {
        "Audio": AudioArtifactsConfigurationTypeDef,
        "Video": VideoArtifactsConfigurationTypeDef,
        "Content": ContentArtifactsConfigurationTypeDef,
        "CompositedVideo": NotRequired[CompositedVideoArtifactsConfigurationTypeDef],
    },
)
ChimeSdkMeetingLiveConnectorConfigurationOutputTypeDef = TypedDict(
    "ChimeSdkMeetingLiveConnectorConfigurationOutputTypeDef",
    {
        "Arn": str,
        "MuxType": LiveConnectorMuxTypeType,
        "CompositedVideo": NotRequired[CompositedVideoArtifactsConfigurationTypeDef],
        "SourceConfiguration": NotRequired[SourceConfigurationOutputTypeDef],
    },
)
RealTimeAlertRuleUnionTypeDef = Union[RealTimeAlertRuleTypeDef, RealTimeAlertRuleOutputTypeDef]
MediaInsightsPipelineConfigurationTypeDef = TypedDict(
    "MediaInsightsPipelineConfigurationTypeDef",
    {
        "MediaInsightsPipelineConfigurationName": NotRequired[str],
        "MediaInsightsPipelineConfigurationArn": NotRequired[str],
        "ResourceAccessRoleArn": NotRequired[str],
        "RealTimeAlertConfiguration": NotRequired[RealTimeAlertConfigurationOutputTypeDef],
        "Elements": NotRequired[List[MediaInsightsPipelineConfigurationElementOutputTypeDef]],
        "MediaInsightsPipelineConfigurationId": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
    },
)
SourceConfigurationUnionTypeDef = Union[
    SourceConfigurationTypeDef, SourceConfigurationOutputTypeDef
]
FragmentSelectorTypeDef = TypedDict(
    "FragmentSelectorTypeDef",
    {
        "FragmentSelectorType": FragmentSelectorTypeType,
        "TimestampRange": TimestampRangeUnionTypeDef,
    },
)
MediaInsightsPipelineConfigurationElementUnionTypeDef = Union[
    MediaInsightsPipelineConfigurationElementTypeDef,
    MediaInsightsPipelineConfigurationElementOutputTypeDef,
]
ConcatenationSourceTypeDef = TypedDict(
    "ConcatenationSourceTypeDef",
    {
        "Type": Literal["MediaCapturePipeline"],
        "MediaCapturePipelineSourceConfiguration": MediaCapturePipelineSourceConfigurationTypeDef,
    },
)
MediaInsightsPipelineTypeDef = TypedDict(
    "MediaInsightsPipelineTypeDef",
    {
        "MediaPipelineId": NotRequired[str],
        "MediaPipelineArn": NotRequired[str],
        "MediaInsightsPipelineConfigurationArn": NotRequired[str],
        "Status": NotRequired[MediaPipelineStatusType],
        "KinesisVideoStreamSourceRuntimeConfiguration": NotRequired[
            KinesisVideoStreamSourceRuntimeConfigurationOutputTypeDef
        ],
        "MediaInsightsRuntimeMetadata": NotRequired[Dict[str, str]],
        "KinesisVideoStreamRecordingSourceRuntimeConfiguration": NotRequired[
            KinesisVideoStreamRecordingSourceRuntimeConfigurationOutputTypeDef
        ],
        "S3RecordingSinkRuntimeConfiguration": NotRequired[
            S3RecordingSinkRuntimeConfigurationTypeDef
        ],
        "CreatedTimestamp": NotRequired[datetime],
        "ElementStatuses": NotRequired[List[MediaInsightsPipelineElementStatusTypeDef]],
    },
)
StreamConfigurationUnionTypeDef = Union[
    StreamConfigurationTypeDef, StreamConfigurationOutputTypeDef
]
ChimeSdkMeetingConfigurationOutputTypeDef = TypedDict(
    "ChimeSdkMeetingConfigurationOutputTypeDef",
    {
        "SourceConfiguration": NotRequired[SourceConfigurationOutputTypeDef],
        "ArtifactsConfiguration": NotRequired[ArtifactsConfigurationTypeDef],
    },
)
LiveConnectorSourceConfigurationOutputTypeDef = TypedDict(
    "LiveConnectorSourceConfigurationOutputTypeDef",
    {
        "SourceType": Literal["ChimeSdkMeeting"],
        "ChimeSdkMeetingLiveConnectorConfiguration": ChimeSdkMeetingLiveConnectorConfigurationOutputTypeDef,
    },
)
RealTimeAlertConfigurationTypeDef = TypedDict(
    "RealTimeAlertConfigurationTypeDef",
    {
        "Disabled": NotRequired[bool],
        "Rules": NotRequired[Sequence[RealTimeAlertRuleUnionTypeDef]],
    },
)
CreateMediaInsightsPipelineConfigurationResponseTypeDef = TypedDict(
    "CreateMediaInsightsPipelineConfigurationResponseTypeDef",
    {
        "MediaInsightsPipelineConfiguration": MediaInsightsPipelineConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMediaInsightsPipelineConfigurationResponseTypeDef = TypedDict(
    "GetMediaInsightsPipelineConfigurationResponseTypeDef",
    {
        "MediaInsightsPipelineConfiguration": MediaInsightsPipelineConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateMediaInsightsPipelineConfigurationResponseTypeDef = TypedDict(
    "UpdateMediaInsightsPipelineConfigurationResponseTypeDef",
    {
        "MediaInsightsPipelineConfiguration": MediaInsightsPipelineConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ChimeSdkMeetingConfigurationTypeDef = TypedDict(
    "ChimeSdkMeetingConfigurationTypeDef",
    {
        "SourceConfiguration": NotRequired[SourceConfigurationUnionTypeDef],
        "ArtifactsConfiguration": NotRequired[ArtifactsConfigurationTypeDef],
    },
)
ChimeSdkMeetingLiveConnectorConfigurationTypeDef = TypedDict(
    "ChimeSdkMeetingLiveConnectorConfigurationTypeDef",
    {
        "Arn": str,
        "MuxType": LiveConnectorMuxTypeType,
        "CompositedVideo": NotRequired[CompositedVideoArtifactsConfigurationTypeDef],
        "SourceConfiguration": NotRequired[SourceConfigurationUnionTypeDef],
    },
)
FragmentSelectorUnionTypeDef = Union[FragmentSelectorTypeDef, FragmentSelectorOutputTypeDef]
CreateMediaConcatenationPipelineRequestRequestTypeDef = TypedDict(
    "CreateMediaConcatenationPipelineRequestRequestTypeDef",
    {
        "Sources": Sequence[ConcatenationSourceTypeDef],
        "Sinks": Sequence[ConcatenationSinkTypeDef],
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
MediaConcatenationPipelineTypeDef = TypedDict(
    "MediaConcatenationPipelineTypeDef",
    {
        "MediaPipelineId": NotRequired[str],
        "MediaPipelineArn": NotRequired[str],
        "Sources": NotRequired[List[ConcatenationSourceTypeDef]],
        "Sinks": NotRequired[List[ConcatenationSinkTypeDef]],
        "Status": NotRequired[MediaPipelineStatusType],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
    },
)
CreateMediaInsightsPipelineResponseTypeDef = TypedDict(
    "CreateMediaInsightsPipelineResponseTypeDef",
    {
        "MediaInsightsPipeline": MediaInsightsPipelineTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
KinesisVideoStreamSourceRuntimeConfigurationTypeDef = TypedDict(
    "KinesisVideoStreamSourceRuntimeConfigurationTypeDef",
    {
        "Streams": Sequence[StreamConfigurationUnionTypeDef],
        "MediaEncoding": Literal["pcm"],
        "MediaSampleRate": int,
    },
)
MediaCapturePipelineTypeDef = TypedDict(
    "MediaCapturePipelineTypeDef",
    {
        "MediaPipelineId": NotRequired[str],
        "MediaPipelineArn": NotRequired[str],
        "SourceType": NotRequired[Literal["ChimeSdkMeeting"]],
        "SourceArn": NotRequired[str],
        "Status": NotRequired[MediaPipelineStatusType],
        "SinkType": NotRequired[Literal["S3Bucket"]],
        "SinkArn": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
        "ChimeSdkMeetingConfiguration": NotRequired[ChimeSdkMeetingConfigurationOutputTypeDef],
    },
)
MediaLiveConnectorPipelineTypeDef = TypedDict(
    "MediaLiveConnectorPipelineTypeDef",
    {
        "Sources": NotRequired[List[LiveConnectorSourceConfigurationOutputTypeDef]],
        "Sinks": NotRequired[List[LiveConnectorSinkConfigurationTypeDef]],
        "MediaPipelineId": NotRequired[str],
        "MediaPipelineArn": NotRequired[str],
        "Status": NotRequired[MediaPipelineStatusType],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
    },
)
CreateMediaInsightsPipelineConfigurationRequestRequestTypeDef = TypedDict(
    "CreateMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    {
        "MediaInsightsPipelineConfigurationName": str,
        "ResourceAccessRoleArn": str,
        "Elements": Sequence[MediaInsightsPipelineConfigurationElementUnionTypeDef],
        "RealTimeAlertConfiguration": NotRequired[RealTimeAlertConfigurationTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ClientRequestToken": NotRequired[str],
    },
)
UpdateMediaInsightsPipelineConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    {
        "Identifier": str,
        "ResourceAccessRoleArn": str,
        "Elements": Sequence[MediaInsightsPipelineConfigurationElementTypeDef],
        "RealTimeAlertConfiguration": NotRequired[RealTimeAlertConfigurationTypeDef],
    },
)
CreateMediaCapturePipelineRequestRequestTypeDef = TypedDict(
    "CreateMediaCapturePipelineRequestRequestTypeDef",
    {
        "SourceType": Literal["ChimeSdkMeeting"],
        "SourceArn": str,
        "SinkType": Literal["S3Bucket"],
        "SinkArn": str,
        "ClientRequestToken": NotRequired[str],
        "ChimeSdkMeetingConfiguration": NotRequired[ChimeSdkMeetingConfigurationTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ChimeSdkMeetingLiveConnectorConfigurationUnionTypeDef = Union[
    ChimeSdkMeetingLiveConnectorConfigurationTypeDef,
    ChimeSdkMeetingLiveConnectorConfigurationOutputTypeDef,
]
KinesisVideoStreamRecordingSourceRuntimeConfigurationTypeDef = TypedDict(
    "KinesisVideoStreamRecordingSourceRuntimeConfigurationTypeDef",
    {
        "Streams": Sequence[RecordingStreamConfigurationTypeDef],
        "FragmentSelector": FragmentSelectorUnionTypeDef,
    },
)
CreateMediaConcatenationPipelineResponseTypeDef = TypedDict(
    "CreateMediaConcatenationPipelineResponseTypeDef",
    {
        "MediaConcatenationPipeline": MediaConcatenationPipelineTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMediaCapturePipelineResponseTypeDef = TypedDict(
    "CreateMediaCapturePipelineResponseTypeDef",
    {
        "MediaCapturePipeline": MediaCapturePipelineTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMediaCapturePipelineResponseTypeDef = TypedDict(
    "GetMediaCapturePipelineResponseTypeDef",
    {
        "MediaCapturePipeline": MediaCapturePipelineTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMediaLiveConnectorPipelineResponseTypeDef = TypedDict(
    "CreateMediaLiveConnectorPipelineResponseTypeDef",
    {
        "MediaLiveConnectorPipeline": MediaLiveConnectorPipelineTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MediaPipelineTypeDef = TypedDict(
    "MediaPipelineTypeDef",
    {
        "MediaCapturePipeline": NotRequired[MediaCapturePipelineTypeDef],
        "MediaLiveConnectorPipeline": NotRequired[MediaLiveConnectorPipelineTypeDef],
        "MediaConcatenationPipeline": NotRequired[MediaConcatenationPipelineTypeDef],
        "MediaInsightsPipeline": NotRequired[MediaInsightsPipelineTypeDef],
        "MediaStreamPipeline": NotRequired[MediaStreamPipelineTypeDef],
    },
)
LiveConnectorSourceConfigurationTypeDef = TypedDict(
    "LiveConnectorSourceConfigurationTypeDef",
    {
        "SourceType": Literal["ChimeSdkMeeting"],
        "ChimeSdkMeetingLiveConnectorConfiguration": ChimeSdkMeetingLiveConnectorConfigurationUnionTypeDef,
    },
)
CreateMediaInsightsPipelineRequestRequestTypeDef = TypedDict(
    "CreateMediaInsightsPipelineRequestRequestTypeDef",
    {
        "MediaInsightsPipelineConfigurationArn": str,
        "KinesisVideoStreamSourceRuntimeConfiguration": NotRequired[
            KinesisVideoStreamSourceRuntimeConfigurationTypeDef
        ],
        "MediaInsightsRuntimeMetadata": NotRequired[Mapping[str, str]],
        "KinesisVideoStreamRecordingSourceRuntimeConfiguration": NotRequired[
            KinesisVideoStreamRecordingSourceRuntimeConfigurationTypeDef
        ],
        "S3RecordingSinkRuntimeConfiguration": NotRequired[
            S3RecordingSinkRuntimeConfigurationTypeDef
        ],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ClientRequestToken": NotRequired[str],
    },
)
GetMediaPipelineResponseTypeDef = TypedDict(
    "GetMediaPipelineResponseTypeDef",
    {
        "MediaPipeline": MediaPipelineTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LiveConnectorSourceConfigurationUnionTypeDef = Union[
    LiveConnectorSourceConfigurationTypeDef, LiveConnectorSourceConfigurationOutputTypeDef
]
CreateMediaLiveConnectorPipelineRequestRequestTypeDef = TypedDict(
    "CreateMediaLiveConnectorPipelineRequestRequestTypeDef",
    {
        "Sources": Sequence[LiveConnectorSourceConfigurationUnionTypeDef],
        "Sinks": Sequence[LiveConnectorSinkConfigurationTypeDef],
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
