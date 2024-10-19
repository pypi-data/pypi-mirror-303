"""
Type annotations for elastictranscoder service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/type_defs/)

Usage::

    ```python
    from mypy_boto3_elastictranscoder.type_defs import EncryptionTypeDef

    data: EncryptionTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Mapping, Sequence, Union

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "EncryptionTypeDef",
    "AudioCodecOptionsTypeDef",
    "CancelJobRequestRequestTypeDef",
    "TimeSpanTypeDef",
    "HlsContentProtectionTypeDef",
    "PlayReadyDrmTypeDef",
    "ResponseMetadataTypeDef",
    "NotificationsTypeDef",
    "WarningTypeDef",
    "ThumbnailsTypeDef",
    "DeletePipelineRequestRequestTypeDef",
    "DeletePresetRequestRequestTypeDef",
    "DetectedPropertiesTypeDef",
    "TimingTypeDef",
    "PaginatorConfigTypeDef",
    "ListJobsByPipelineRequestRequestTypeDef",
    "ListJobsByStatusRequestRequestTypeDef",
    "ListPipelinesRequestRequestTypeDef",
    "ListPresetsRequestRequestTypeDef",
    "PermissionOutputTypeDef",
    "PermissionTypeDef",
    "PresetWatermarkTypeDef",
    "WaiterConfigTypeDef",
    "ReadJobRequestRequestTypeDef",
    "ReadPipelineRequestRequestTypeDef",
    "ReadPresetRequestRequestTypeDef",
    "TestRoleRequestRequestTypeDef",
    "UpdatePipelineStatusRequestRequestTypeDef",
    "ArtworkTypeDef",
    "CaptionFormatTypeDef",
    "CaptionSourceTypeDef",
    "JobWatermarkTypeDef",
    "AudioParametersTypeDef",
    "ClipTypeDef",
    "CreateJobPlaylistTypeDef",
    "PlaylistTypeDef",
    "TestRoleResponseTypeDef",
    "UpdatePipelineNotificationsRequestRequestTypeDef",
    "ListJobsByPipelineRequestListJobsByPipelinePaginateTypeDef",
    "ListJobsByStatusRequestListJobsByStatusPaginateTypeDef",
    "ListPipelinesRequestListPipelinesPaginateTypeDef",
    "ListPresetsRequestListPresetsPaginateTypeDef",
    "PipelineOutputConfigOutputTypeDef",
    "PermissionUnionTypeDef",
    "VideoParametersOutputTypeDef",
    "VideoParametersTypeDef",
    "ReadJobRequestJobCompleteWaitTypeDef",
    "JobAlbumArtOutputTypeDef",
    "JobAlbumArtTypeDef",
    "CaptionsOutputTypeDef",
    "CaptionsTypeDef",
    "InputCaptionsOutputTypeDef",
    "InputCaptionsTypeDef",
    "PipelineTypeDef",
    "PipelineOutputConfigTypeDef",
    "PresetTypeDef",
    "CreatePresetRequestRequestTypeDef",
    "JobAlbumArtUnionTypeDef",
    "JobOutputTypeDef",
    "CaptionsUnionTypeDef",
    "JobInputOutputTypeDef",
    "InputCaptionsUnionTypeDef",
    "CreatePipelineResponseTypeDef",
    "ListPipelinesResponseTypeDef",
    "ReadPipelineResponseTypeDef",
    "UpdatePipelineNotificationsResponseTypeDef",
    "UpdatePipelineResponseTypeDef",
    "UpdatePipelineStatusResponseTypeDef",
    "CreatePipelineRequestRequestTypeDef",
    "UpdatePipelineRequestRequestTypeDef",
    "CreatePresetResponseTypeDef",
    "ListPresetsResponseTypeDef",
    "ReadPresetResponseTypeDef",
    "CreateJobOutputTypeDef",
    "JobTypeDef",
    "JobInputTypeDef",
    "CreateJobResponseTypeDef",
    "ListJobsByPipelineResponseTypeDef",
    "ListJobsByStatusResponseTypeDef",
    "ReadJobResponseTypeDef",
    "JobInputUnionTypeDef",
    "CreateJobRequestRequestTypeDef",
)

EncryptionTypeDef = TypedDict(
    "EncryptionTypeDef",
    {
        "Mode": NotRequired[str],
        "Key": NotRequired[str],
        "KeyMd5": NotRequired[str],
        "InitializationVector": NotRequired[str],
    },
)
AudioCodecOptionsTypeDef = TypedDict(
    "AudioCodecOptionsTypeDef",
    {
        "Profile": NotRequired[str],
        "BitDepth": NotRequired[str],
        "BitOrder": NotRequired[str],
        "Signed": NotRequired[str],
    },
)
CancelJobRequestRequestTypeDef = TypedDict(
    "CancelJobRequestRequestTypeDef",
    {
        "Id": str,
    },
)
TimeSpanTypeDef = TypedDict(
    "TimeSpanTypeDef",
    {
        "StartTime": NotRequired[str],
        "Duration": NotRequired[str],
    },
)
HlsContentProtectionTypeDef = TypedDict(
    "HlsContentProtectionTypeDef",
    {
        "Method": NotRequired[str],
        "Key": NotRequired[str],
        "KeyMd5": NotRequired[str],
        "InitializationVector": NotRequired[str],
        "LicenseAcquisitionUrl": NotRequired[str],
        "KeyStoragePolicy": NotRequired[str],
    },
)
PlayReadyDrmTypeDef = TypedDict(
    "PlayReadyDrmTypeDef",
    {
        "Format": NotRequired[str],
        "Key": NotRequired[str],
        "KeyMd5": NotRequired[str],
        "KeyId": NotRequired[str],
        "InitializationVector": NotRequired[str],
        "LicenseAcquisitionUrl": NotRequired[str],
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
NotificationsTypeDef = TypedDict(
    "NotificationsTypeDef",
    {
        "Progressing": NotRequired[str],
        "Completed": NotRequired[str],
        "Warning": NotRequired[str],
        "Error": NotRequired[str],
    },
)
WarningTypeDef = TypedDict(
    "WarningTypeDef",
    {
        "Code": NotRequired[str],
        "Message": NotRequired[str],
    },
)
ThumbnailsTypeDef = TypedDict(
    "ThumbnailsTypeDef",
    {
        "Format": NotRequired[str],
        "Interval": NotRequired[str],
        "Resolution": NotRequired[str],
        "AspectRatio": NotRequired[str],
        "MaxWidth": NotRequired[str],
        "MaxHeight": NotRequired[str],
        "SizingPolicy": NotRequired[str],
        "PaddingPolicy": NotRequired[str],
    },
)
DeletePipelineRequestRequestTypeDef = TypedDict(
    "DeletePipelineRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DeletePresetRequestRequestTypeDef = TypedDict(
    "DeletePresetRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DetectedPropertiesTypeDef = TypedDict(
    "DetectedPropertiesTypeDef",
    {
        "Width": NotRequired[int],
        "Height": NotRequired[int],
        "FrameRate": NotRequired[str],
        "FileSize": NotRequired[int],
        "DurationMillis": NotRequired[int],
    },
)
TimingTypeDef = TypedDict(
    "TimingTypeDef",
    {
        "SubmitTimeMillis": NotRequired[int],
        "StartTimeMillis": NotRequired[int],
        "FinishTimeMillis": NotRequired[int],
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
ListJobsByPipelineRequestRequestTypeDef = TypedDict(
    "ListJobsByPipelineRequestRequestTypeDef",
    {
        "PipelineId": str,
        "Ascending": NotRequired[str],
        "PageToken": NotRequired[str],
    },
)
ListJobsByStatusRequestRequestTypeDef = TypedDict(
    "ListJobsByStatusRequestRequestTypeDef",
    {
        "Status": str,
        "Ascending": NotRequired[str],
        "PageToken": NotRequired[str],
    },
)
ListPipelinesRequestRequestTypeDef = TypedDict(
    "ListPipelinesRequestRequestTypeDef",
    {
        "Ascending": NotRequired[str],
        "PageToken": NotRequired[str],
    },
)
ListPresetsRequestRequestTypeDef = TypedDict(
    "ListPresetsRequestRequestTypeDef",
    {
        "Ascending": NotRequired[str],
        "PageToken": NotRequired[str],
    },
)
PermissionOutputTypeDef = TypedDict(
    "PermissionOutputTypeDef",
    {
        "GranteeType": NotRequired[str],
        "Grantee": NotRequired[str],
        "Access": NotRequired[List[str]],
    },
)
PermissionTypeDef = TypedDict(
    "PermissionTypeDef",
    {
        "GranteeType": NotRequired[str],
        "Grantee": NotRequired[str],
        "Access": NotRequired[Sequence[str]],
    },
)
PresetWatermarkTypeDef = TypedDict(
    "PresetWatermarkTypeDef",
    {
        "Id": NotRequired[str],
        "MaxWidth": NotRequired[str],
        "MaxHeight": NotRequired[str],
        "SizingPolicy": NotRequired[str],
        "HorizontalAlign": NotRequired[str],
        "HorizontalOffset": NotRequired[str],
        "VerticalAlign": NotRequired[str],
        "VerticalOffset": NotRequired[str],
        "Opacity": NotRequired[str],
        "Target": NotRequired[str],
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
ReadJobRequestRequestTypeDef = TypedDict(
    "ReadJobRequestRequestTypeDef",
    {
        "Id": str,
    },
)
ReadPipelineRequestRequestTypeDef = TypedDict(
    "ReadPipelineRequestRequestTypeDef",
    {
        "Id": str,
    },
)
ReadPresetRequestRequestTypeDef = TypedDict(
    "ReadPresetRequestRequestTypeDef",
    {
        "Id": str,
    },
)
TestRoleRequestRequestTypeDef = TypedDict(
    "TestRoleRequestRequestTypeDef",
    {
        "Role": str,
        "InputBucket": str,
        "OutputBucket": str,
        "Topics": Sequence[str],
    },
)
UpdatePipelineStatusRequestRequestTypeDef = TypedDict(
    "UpdatePipelineStatusRequestRequestTypeDef",
    {
        "Id": str,
        "Status": str,
    },
)
ArtworkTypeDef = TypedDict(
    "ArtworkTypeDef",
    {
        "InputKey": NotRequired[str],
        "MaxWidth": NotRequired[str],
        "MaxHeight": NotRequired[str],
        "SizingPolicy": NotRequired[str],
        "PaddingPolicy": NotRequired[str],
        "AlbumArtFormat": NotRequired[str],
        "Encryption": NotRequired[EncryptionTypeDef],
    },
)
CaptionFormatTypeDef = TypedDict(
    "CaptionFormatTypeDef",
    {
        "Format": NotRequired[str],
        "Pattern": NotRequired[str],
        "Encryption": NotRequired[EncryptionTypeDef],
    },
)
CaptionSourceTypeDef = TypedDict(
    "CaptionSourceTypeDef",
    {
        "Key": NotRequired[str],
        "Language": NotRequired[str],
        "TimeOffset": NotRequired[str],
        "Label": NotRequired[str],
        "Encryption": NotRequired[EncryptionTypeDef],
    },
)
JobWatermarkTypeDef = TypedDict(
    "JobWatermarkTypeDef",
    {
        "PresetWatermarkId": NotRequired[str],
        "InputKey": NotRequired[str],
        "Encryption": NotRequired[EncryptionTypeDef],
    },
)
AudioParametersTypeDef = TypedDict(
    "AudioParametersTypeDef",
    {
        "Codec": NotRequired[str],
        "SampleRate": NotRequired[str],
        "BitRate": NotRequired[str],
        "Channels": NotRequired[str],
        "AudioPackingMode": NotRequired[str],
        "CodecOptions": NotRequired[AudioCodecOptionsTypeDef],
    },
)
ClipTypeDef = TypedDict(
    "ClipTypeDef",
    {
        "TimeSpan": NotRequired[TimeSpanTypeDef],
    },
)
CreateJobPlaylistTypeDef = TypedDict(
    "CreateJobPlaylistTypeDef",
    {
        "Name": NotRequired[str],
        "Format": NotRequired[str],
        "OutputKeys": NotRequired[Sequence[str]],
        "HlsContentProtection": NotRequired[HlsContentProtectionTypeDef],
        "PlayReadyDrm": NotRequired[PlayReadyDrmTypeDef],
    },
)
PlaylistTypeDef = TypedDict(
    "PlaylistTypeDef",
    {
        "Name": NotRequired[str],
        "Format": NotRequired[str],
        "OutputKeys": NotRequired[List[str]],
        "HlsContentProtection": NotRequired[HlsContentProtectionTypeDef],
        "PlayReadyDrm": NotRequired[PlayReadyDrmTypeDef],
        "Status": NotRequired[str],
        "StatusDetail": NotRequired[str],
    },
)
TestRoleResponseTypeDef = TypedDict(
    "TestRoleResponseTypeDef",
    {
        "Success": str,
        "Messages": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePipelineNotificationsRequestRequestTypeDef = TypedDict(
    "UpdatePipelineNotificationsRequestRequestTypeDef",
    {
        "Id": str,
        "Notifications": NotificationsTypeDef,
    },
)
ListJobsByPipelineRequestListJobsByPipelinePaginateTypeDef = TypedDict(
    "ListJobsByPipelineRequestListJobsByPipelinePaginateTypeDef",
    {
        "PipelineId": str,
        "Ascending": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListJobsByStatusRequestListJobsByStatusPaginateTypeDef = TypedDict(
    "ListJobsByStatusRequestListJobsByStatusPaginateTypeDef",
    {
        "Status": str,
        "Ascending": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPipelinesRequestListPipelinesPaginateTypeDef = TypedDict(
    "ListPipelinesRequestListPipelinesPaginateTypeDef",
    {
        "Ascending": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPresetsRequestListPresetsPaginateTypeDef = TypedDict(
    "ListPresetsRequestListPresetsPaginateTypeDef",
    {
        "Ascending": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
PipelineOutputConfigOutputTypeDef = TypedDict(
    "PipelineOutputConfigOutputTypeDef",
    {
        "Bucket": NotRequired[str],
        "StorageClass": NotRequired[str],
        "Permissions": NotRequired[List[PermissionOutputTypeDef]],
    },
)
PermissionUnionTypeDef = Union[PermissionTypeDef, PermissionOutputTypeDef]
VideoParametersOutputTypeDef = TypedDict(
    "VideoParametersOutputTypeDef",
    {
        "Codec": NotRequired[str],
        "CodecOptions": NotRequired[Dict[str, str]],
        "KeyframesMaxDist": NotRequired[str],
        "FixedGOP": NotRequired[str],
        "BitRate": NotRequired[str],
        "FrameRate": NotRequired[str],
        "MaxFrameRate": NotRequired[str],
        "Resolution": NotRequired[str],
        "AspectRatio": NotRequired[str],
        "MaxWidth": NotRequired[str],
        "MaxHeight": NotRequired[str],
        "DisplayAspectRatio": NotRequired[str],
        "SizingPolicy": NotRequired[str],
        "PaddingPolicy": NotRequired[str],
        "Watermarks": NotRequired[List[PresetWatermarkTypeDef]],
    },
)
VideoParametersTypeDef = TypedDict(
    "VideoParametersTypeDef",
    {
        "Codec": NotRequired[str],
        "CodecOptions": NotRequired[Mapping[str, str]],
        "KeyframesMaxDist": NotRequired[str],
        "FixedGOP": NotRequired[str],
        "BitRate": NotRequired[str],
        "FrameRate": NotRequired[str],
        "MaxFrameRate": NotRequired[str],
        "Resolution": NotRequired[str],
        "AspectRatio": NotRequired[str],
        "MaxWidth": NotRequired[str],
        "MaxHeight": NotRequired[str],
        "DisplayAspectRatio": NotRequired[str],
        "SizingPolicy": NotRequired[str],
        "PaddingPolicy": NotRequired[str],
        "Watermarks": NotRequired[Sequence[PresetWatermarkTypeDef]],
    },
)
ReadJobRequestJobCompleteWaitTypeDef = TypedDict(
    "ReadJobRequestJobCompleteWaitTypeDef",
    {
        "Id": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
JobAlbumArtOutputTypeDef = TypedDict(
    "JobAlbumArtOutputTypeDef",
    {
        "MergePolicy": NotRequired[str],
        "Artwork": NotRequired[List[ArtworkTypeDef]],
    },
)
JobAlbumArtTypeDef = TypedDict(
    "JobAlbumArtTypeDef",
    {
        "MergePolicy": NotRequired[str],
        "Artwork": NotRequired[Sequence[ArtworkTypeDef]],
    },
)
CaptionsOutputTypeDef = TypedDict(
    "CaptionsOutputTypeDef",
    {
        "MergePolicy": NotRequired[str],
        "CaptionSources": NotRequired[List[CaptionSourceTypeDef]],
        "CaptionFormats": NotRequired[List[CaptionFormatTypeDef]],
    },
)
CaptionsTypeDef = TypedDict(
    "CaptionsTypeDef",
    {
        "MergePolicy": NotRequired[str],
        "CaptionSources": NotRequired[Sequence[CaptionSourceTypeDef]],
        "CaptionFormats": NotRequired[Sequence[CaptionFormatTypeDef]],
    },
)
InputCaptionsOutputTypeDef = TypedDict(
    "InputCaptionsOutputTypeDef",
    {
        "MergePolicy": NotRequired[str],
        "CaptionSources": NotRequired[List[CaptionSourceTypeDef]],
    },
)
InputCaptionsTypeDef = TypedDict(
    "InputCaptionsTypeDef",
    {
        "MergePolicy": NotRequired[str],
        "CaptionSources": NotRequired[Sequence[CaptionSourceTypeDef]],
    },
)
PipelineTypeDef = TypedDict(
    "PipelineTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired[str],
        "InputBucket": NotRequired[str],
        "OutputBucket": NotRequired[str],
        "Role": NotRequired[str],
        "AwsKmsKeyArn": NotRequired[str],
        "Notifications": NotRequired[NotificationsTypeDef],
        "ContentConfig": NotRequired[PipelineOutputConfigOutputTypeDef],
        "ThumbnailConfig": NotRequired[PipelineOutputConfigOutputTypeDef],
    },
)
PipelineOutputConfigTypeDef = TypedDict(
    "PipelineOutputConfigTypeDef",
    {
        "Bucket": NotRequired[str],
        "StorageClass": NotRequired[str],
        "Permissions": NotRequired[Sequence[PermissionUnionTypeDef]],
    },
)
PresetTypeDef = TypedDict(
    "PresetTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Container": NotRequired[str],
        "Audio": NotRequired[AudioParametersTypeDef],
        "Video": NotRequired[VideoParametersOutputTypeDef],
        "Thumbnails": NotRequired[ThumbnailsTypeDef],
        "Type": NotRequired[str],
    },
)
CreatePresetRequestRequestTypeDef = TypedDict(
    "CreatePresetRequestRequestTypeDef",
    {
        "Name": str,
        "Container": str,
        "Description": NotRequired[str],
        "Video": NotRequired[VideoParametersTypeDef],
        "Audio": NotRequired[AudioParametersTypeDef],
        "Thumbnails": NotRequired[ThumbnailsTypeDef],
    },
)
JobAlbumArtUnionTypeDef = Union[JobAlbumArtTypeDef, JobAlbumArtOutputTypeDef]
JobOutputTypeDef = TypedDict(
    "JobOutputTypeDef",
    {
        "Id": NotRequired[str],
        "Key": NotRequired[str],
        "ThumbnailPattern": NotRequired[str],
        "ThumbnailEncryption": NotRequired[EncryptionTypeDef],
        "Rotate": NotRequired[str],
        "PresetId": NotRequired[str],
        "SegmentDuration": NotRequired[str],
        "Status": NotRequired[str],
        "StatusDetail": NotRequired[str],
        "Duration": NotRequired[int],
        "Width": NotRequired[int],
        "Height": NotRequired[int],
        "FrameRate": NotRequired[str],
        "FileSize": NotRequired[int],
        "DurationMillis": NotRequired[int],
        "Watermarks": NotRequired[List[JobWatermarkTypeDef]],
        "AlbumArt": NotRequired[JobAlbumArtOutputTypeDef],
        "Composition": NotRequired[List[ClipTypeDef]],
        "Captions": NotRequired[CaptionsOutputTypeDef],
        "Encryption": NotRequired[EncryptionTypeDef],
        "AppliedColorSpaceConversion": NotRequired[str],
    },
)
CaptionsUnionTypeDef = Union[CaptionsTypeDef, CaptionsOutputTypeDef]
JobInputOutputTypeDef = TypedDict(
    "JobInputOutputTypeDef",
    {
        "Key": NotRequired[str],
        "FrameRate": NotRequired[str],
        "Resolution": NotRequired[str],
        "AspectRatio": NotRequired[str],
        "Interlaced": NotRequired[str],
        "Container": NotRequired[str],
        "Encryption": NotRequired[EncryptionTypeDef],
        "TimeSpan": NotRequired[TimeSpanTypeDef],
        "InputCaptions": NotRequired[InputCaptionsOutputTypeDef],
        "DetectedProperties": NotRequired[DetectedPropertiesTypeDef],
    },
)
InputCaptionsUnionTypeDef = Union[InputCaptionsTypeDef, InputCaptionsOutputTypeDef]
CreatePipelineResponseTypeDef = TypedDict(
    "CreatePipelineResponseTypeDef",
    {
        "Pipeline": PipelineTypeDef,
        "Warnings": List[WarningTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPipelinesResponseTypeDef = TypedDict(
    "ListPipelinesResponseTypeDef",
    {
        "Pipelines": List[PipelineTypeDef],
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReadPipelineResponseTypeDef = TypedDict(
    "ReadPipelineResponseTypeDef",
    {
        "Pipeline": PipelineTypeDef,
        "Warnings": List[WarningTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePipelineNotificationsResponseTypeDef = TypedDict(
    "UpdatePipelineNotificationsResponseTypeDef",
    {
        "Pipeline": PipelineTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePipelineResponseTypeDef = TypedDict(
    "UpdatePipelineResponseTypeDef",
    {
        "Pipeline": PipelineTypeDef,
        "Warnings": List[WarningTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePipelineStatusResponseTypeDef = TypedDict(
    "UpdatePipelineStatusResponseTypeDef",
    {
        "Pipeline": PipelineTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePipelineRequestRequestTypeDef = TypedDict(
    "CreatePipelineRequestRequestTypeDef",
    {
        "Name": str,
        "InputBucket": str,
        "Role": str,
        "OutputBucket": NotRequired[str],
        "AwsKmsKeyArn": NotRequired[str],
        "Notifications": NotRequired[NotificationsTypeDef],
        "ContentConfig": NotRequired[PipelineOutputConfigTypeDef],
        "ThumbnailConfig": NotRequired[PipelineOutputConfigTypeDef],
    },
)
UpdatePipelineRequestRequestTypeDef = TypedDict(
    "UpdatePipelineRequestRequestTypeDef",
    {
        "Id": str,
        "Name": NotRequired[str],
        "InputBucket": NotRequired[str],
        "Role": NotRequired[str],
        "AwsKmsKeyArn": NotRequired[str],
        "Notifications": NotRequired[NotificationsTypeDef],
        "ContentConfig": NotRequired[PipelineOutputConfigTypeDef],
        "ThumbnailConfig": NotRequired[PipelineOutputConfigTypeDef],
    },
)
CreatePresetResponseTypeDef = TypedDict(
    "CreatePresetResponseTypeDef",
    {
        "Preset": PresetTypeDef,
        "Warning": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPresetsResponseTypeDef = TypedDict(
    "ListPresetsResponseTypeDef",
    {
        "Presets": List[PresetTypeDef],
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReadPresetResponseTypeDef = TypedDict(
    "ReadPresetResponseTypeDef",
    {
        "Preset": PresetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateJobOutputTypeDef = TypedDict(
    "CreateJobOutputTypeDef",
    {
        "Key": NotRequired[str],
        "ThumbnailPattern": NotRequired[str],
        "ThumbnailEncryption": NotRequired[EncryptionTypeDef],
        "Rotate": NotRequired[str],
        "PresetId": NotRequired[str],
        "SegmentDuration": NotRequired[str],
        "Watermarks": NotRequired[Sequence[JobWatermarkTypeDef]],
        "AlbumArt": NotRequired[JobAlbumArtUnionTypeDef],
        "Composition": NotRequired[Sequence[ClipTypeDef]],
        "Captions": NotRequired[CaptionsUnionTypeDef],
        "Encryption": NotRequired[EncryptionTypeDef],
    },
)
JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "PipelineId": NotRequired[str],
        "Input": NotRequired[JobInputOutputTypeDef],
        "Inputs": NotRequired[List[JobInputOutputTypeDef]],
        "Output": NotRequired[JobOutputTypeDef],
        "Outputs": NotRequired[List[JobOutputTypeDef]],
        "OutputKeyPrefix": NotRequired[str],
        "Playlists": NotRequired[List[PlaylistTypeDef]],
        "Status": NotRequired[str],
        "UserMetadata": NotRequired[Dict[str, str]],
        "Timing": NotRequired[TimingTypeDef],
    },
)
JobInputTypeDef = TypedDict(
    "JobInputTypeDef",
    {
        "Key": NotRequired[str],
        "FrameRate": NotRequired[str],
        "Resolution": NotRequired[str],
        "AspectRatio": NotRequired[str],
        "Interlaced": NotRequired[str],
        "Container": NotRequired[str],
        "Encryption": NotRequired[EncryptionTypeDef],
        "TimeSpan": NotRequired[TimeSpanTypeDef],
        "InputCaptions": NotRequired[InputCaptionsUnionTypeDef],
        "DetectedProperties": NotRequired[DetectedPropertiesTypeDef],
    },
)
CreateJobResponseTypeDef = TypedDict(
    "CreateJobResponseTypeDef",
    {
        "Job": JobTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListJobsByPipelineResponseTypeDef = TypedDict(
    "ListJobsByPipelineResponseTypeDef",
    {
        "Jobs": List[JobTypeDef],
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListJobsByStatusResponseTypeDef = TypedDict(
    "ListJobsByStatusResponseTypeDef",
    {
        "Jobs": List[JobTypeDef],
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReadJobResponseTypeDef = TypedDict(
    "ReadJobResponseTypeDef",
    {
        "Job": JobTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
JobInputUnionTypeDef = Union[JobInputTypeDef, JobInputOutputTypeDef]
CreateJobRequestRequestTypeDef = TypedDict(
    "CreateJobRequestRequestTypeDef",
    {
        "PipelineId": str,
        "Input": NotRequired[JobInputTypeDef],
        "Inputs": NotRequired[Sequence[JobInputUnionTypeDef]],
        "Output": NotRequired[CreateJobOutputTypeDef],
        "Outputs": NotRequired[Sequence[CreateJobOutputTypeDef]],
        "OutputKeyPrefix": NotRequired[str],
        "Playlists": NotRequired[Sequence[CreateJobPlaylistTypeDef]],
        "UserMetadata": NotRequired[Mapping[str, str]],
    },
)
