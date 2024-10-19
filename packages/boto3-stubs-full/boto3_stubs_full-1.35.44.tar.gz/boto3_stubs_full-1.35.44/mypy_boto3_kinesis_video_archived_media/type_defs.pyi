"""
Type annotations for kinesis-video-archived-media service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/type_defs/)

Usage::

    ```python
    from mypy_boto3_kinesis_video_archived_media.type_defs import TimestampTypeDef

    data: TimestampTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    ClipFragmentSelectorTypeType,
    ContainerFormatType,
    DASHDisplayFragmentNumberType,
    DASHDisplayFragmentTimestampType,
    DASHFragmentSelectorTypeType,
    DASHPlaybackModeType,
    FormatType,
    FragmentSelectorTypeType,
    HLSDiscontinuityModeType,
    HLSDisplayFragmentTimestampType,
    HLSFragmentSelectorTypeType,
    HLSPlaybackModeType,
    ImageErrorType,
    ImageSelectorTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "TimestampTypeDef",
    "FragmentTypeDef",
    "ResponseMetadataTypeDef",
    "PaginatorConfigTypeDef",
    "ImageTypeDef",
    "GetMediaForFragmentListInputRequestTypeDef",
    "ClipTimestampRangeTypeDef",
    "DASHTimestampRangeTypeDef",
    "GetImagesInputRequestTypeDef",
    "HLSTimestampRangeTypeDef",
    "TimestampRangeTypeDef",
    "GetClipOutputTypeDef",
    "GetDASHStreamingSessionURLOutputTypeDef",
    "GetHLSStreamingSessionURLOutputTypeDef",
    "GetMediaForFragmentListOutputTypeDef",
    "ListFragmentsOutputTypeDef",
    "GetImagesInputGetImagesPaginateTypeDef",
    "GetImagesOutputTypeDef",
    "ClipFragmentSelectorTypeDef",
    "DASHFragmentSelectorTypeDef",
    "HLSFragmentSelectorTypeDef",
    "FragmentSelectorTypeDef",
    "GetClipInputRequestTypeDef",
    "GetDASHStreamingSessionURLInputRequestTypeDef",
    "GetHLSStreamingSessionURLInputRequestTypeDef",
    "ListFragmentsInputListFragmentsPaginateTypeDef",
    "ListFragmentsInputRequestTypeDef",
)

TimestampTypeDef = Union[datetime, str]
FragmentTypeDef = TypedDict(
    "FragmentTypeDef",
    {
        "FragmentNumber": NotRequired[str],
        "FragmentSizeInBytes": NotRequired[int],
        "ProducerTimestamp": NotRequired[datetime],
        "ServerTimestamp": NotRequired[datetime],
        "FragmentLengthInMilliseconds": NotRequired[int],
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
PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
    },
)
ImageTypeDef = TypedDict(
    "ImageTypeDef",
    {
        "TimeStamp": NotRequired[datetime],
        "Error": NotRequired[ImageErrorType],
        "ImageContent": NotRequired[str],
    },
)
GetMediaForFragmentListInputRequestTypeDef = TypedDict(
    "GetMediaForFragmentListInputRequestTypeDef",
    {
        "Fragments": Sequence[str],
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
    },
)
ClipTimestampRangeTypeDef = TypedDict(
    "ClipTimestampRangeTypeDef",
    {
        "StartTimestamp": TimestampTypeDef,
        "EndTimestamp": TimestampTypeDef,
    },
)
DASHTimestampRangeTypeDef = TypedDict(
    "DASHTimestampRangeTypeDef",
    {
        "StartTimestamp": NotRequired[TimestampTypeDef],
        "EndTimestamp": NotRequired[TimestampTypeDef],
    },
)
GetImagesInputRequestTypeDef = TypedDict(
    "GetImagesInputRequestTypeDef",
    {
        "ImageSelectorType": ImageSelectorTypeType,
        "StartTimestamp": TimestampTypeDef,
        "EndTimestamp": TimestampTypeDef,
        "Format": FormatType,
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
        "SamplingInterval": NotRequired[int],
        "FormatConfig": NotRequired[Mapping[Literal["JPEGQuality"], str]],
        "WidthPixels": NotRequired[int],
        "HeightPixels": NotRequired[int],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
HLSTimestampRangeTypeDef = TypedDict(
    "HLSTimestampRangeTypeDef",
    {
        "StartTimestamp": NotRequired[TimestampTypeDef],
        "EndTimestamp": NotRequired[TimestampTypeDef],
    },
)
TimestampRangeTypeDef = TypedDict(
    "TimestampRangeTypeDef",
    {
        "StartTimestamp": TimestampTypeDef,
        "EndTimestamp": TimestampTypeDef,
    },
)
GetClipOutputTypeDef = TypedDict(
    "GetClipOutputTypeDef",
    {
        "ContentType": str,
        "Payload": StreamingBody,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDASHStreamingSessionURLOutputTypeDef = TypedDict(
    "GetDASHStreamingSessionURLOutputTypeDef",
    {
        "DASHStreamingSessionURL": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetHLSStreamingSessionURLOutputTypeDef = TypedDict(
    "GetHLSStreamingSessionURLOutputTypeDef",
    {
        "HLSStreamingSessionURL": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMediaForFragmentListOutputTypeDef = TypedDict(
    "GetMediaForFragmentListOutputTypeDef",
    {
        "ContentType": str,
        "Payload": StreamingBody,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListFragmentsOutputTypeDef = TypedDict(
    "ListFragmentsOutputTypeDef",
    {
        "Fragments": List[FragmentTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetImagesInputGetImagesPaginateTypeDef = TypedDict(
    "GetImagesInputGetImagesPaginateTypeDef",
    {
        "ImageSelectorType": ImageSelectorTypeType,
        "StartTimestamp": TimestampTypeDef,
        "EndTimestamp": TimestampTypeDef,
        "Format": FormatType,
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
        "SamplingInterval": NotRequired[int],
        "FormatConfig": NotRequired[Mapping[Literal["JPEGQuality"], str]],
        "WidthPixels": NotRequired[int],
        "HeightPixels": NotRequired[int],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetImagesOutputTypeDef = TypedDict(
    "GetImagesOutputTypeDef",
    {
        "Images": List[ImageTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ClipFragmentSelectorTypeDef = TypedDict(
    "ClipFragmentSelectorTypeDef",
    {
        "FragmentSelectorType": ClipFragmentSelectorTypeType,
        "TimestampRange": ClipTimestampRangeTypeDef,
    },
)
DASHFragmentSelectorTypeDef = TypedDict(
    "DASHFragmentSelectorTypeDef",
    {
        "FragmentSelectorType": NotRequired[DASHFragmentSelectorTypeType],
        "TimestampRange": NotRequired[DASHTimestampRangeTypeDef],
    },
)
HLSFragmentSelectorTypeDef = TypedDict(
    "HLSFragmentSelectorTypeDef",
    {
        "FragmentSelectorType": NotRequired[HLSFragmentSelectorTypeType],
        "TimestampRange": NotRequired[HLSTimestampRangeTypeDef],
    },
)
FragmentSelectorTypeDef = TypedDict(
    "FragmentSelectorTypeDef",
    {
        "FragmentSelectorType": FragmentSelectorTypeType,
        "TimestampRange": TimestampRangeTypeDef,
    },
)
GetClipInputRequestTypeDef = TypedDict(
    "GetClipInputRequestTypeDef",
    {
        "ClipFragmentSelector": ClipFragmentSelectorTypeDef,
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
    },
)
GetDASHStreamingSessionURLInputRequestTypeDef = TypedDict(
    "GetDASHStreamingSessionURLInputRequestTypeDef",
    {
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
        "PlaybackMode": NotRequired[DASHPlaybackModeType],
        "DisplayFragmentTimestamp": NotRequired[DASHDisplayFragmentTimestampType],
        "DisplayFragmentNumber": NotRequired[DASHDisplayFragmentNumberType],
        "DASHFragmentSelector": NotRequired[DASHFragmentSelectorTypeDef],
        "Expires": NotRequired[int],
        "MaxManifestFragmentResults": NotRequired[int],
    },
)
GetHLSStreamingSessionURLInputRequestTypeDef = TypedDict(
    "GetHLSStreamingSessionURLInputRequestTypeDef",
    {
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
        "PlaybackMode": NotRequired[HLSPlaybackModeType],
        "HLSFragmentSelector": NotRequired[HLSFragmentSelectorTypeDef],
        "ContainerFormat": NotRequired[ContainerFormatType],
        "DiscontinuityMode": NotRequired[HLSDiscontinuityModeType],
        "DisplayFragmentTimestamp": NotRequired[HLSDisplayFragmentTimestampType],
        "Expires": NotRequired[int],
        "MaxMediaPlaylistFragmentResults": NotRequired[int],
    },
)
ListFragmentsInputListFragmentsPaginateTypeDef = TypedDict(
    "ListFragmentsInputListFragmentsPaginateTypeDef",
    {
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
        "FragmentSelector": NotRequired[FragmentSelectorTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFragmentsInputRequestTypeDef = TypedDict(
    "ListFragmentsInputRequestTypeDef",
    {
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "FragmentSelector": NotRequired[FragmentSelectorTypeDef],
    },
)
