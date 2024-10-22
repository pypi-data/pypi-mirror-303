"""
Type annotations for mediapackagev2 service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/type_defs/)

Usage::

    ```python
    from mypy_boto3_mediapackagev2.type_defs import ChannelGroupListConfigurationTypeDef

    data: ChannelGroupListConfigurationTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AdMarkerDashType,
    CmafEncryptionMethodType,
    ContainerTypeType,
    DashDrmSignalingType,
    DashPeriodTriggerType,
    DashUtcTimingModeType,
    DrmSystemType,
    EndpointErrorConditionType,
    InputTypeType,
    PresetSpeke20AudioType,
    PresetSpeke20VideoType,
    ScteFilterType,
    TsEncryptionMethodType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "ChannelGroupListConfigurationTypeDef",
    "ChannelListConfigurationTypeDef",
    "CreateChannelGroupRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CreateChannelRequestRequestTypeDef",
    "IngestEndpointTypeDef",
    "DashUtcTimingTypeDef",
    "ScteDashTypeDef",
    "ScteHlsTypeDef",
    "StartTagTypeDef",
    "ForceEndpointErrorConfigurationTypeDef",
    "ForceEndpointErrorConfigurationOutputTypeDef",
    "DeleteChannelGroupRequestRequestTypeDef",
    "DeleteChannelPolicyRequestRequestTypeDef",
    "DeleteChannelRequestRequestTypeDef",
    "DeleteOriginEndpointPolicyRequestRequestTypeDef",
    "DeleteOriginEndpointRequestRequestTypeDef",
    "EncryptionContractConfigurationTypeDef",
    "EncryptionMethodTypeDef",
    "FilterConfigurationOutputTypeDef",
    "TimestampTypeDef",
    "GetChannelGroupRequestRequestTypeDef",
    "GetChannelPolicyRequestRequestTypeDef",
    "GetChannelRequestRequestTypeDef",
    "GetOriginEndpointPolicyRequestRequestTypeDef",
    "GetOriginEndpointRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListChannelGroupsRequestRequestTypeDef",
    "ListChannelsRequestRequestTypeDef",
    "ListDashManifestConfigurationTypeDef",
    "ListHlsManifestConfigurationTypeDef",
    "ListLowLatencyHlsManifestConfigurationTypeDef",
    "ListOriginEndpointsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "PutChannelPolicyRequestRequestTypeDef",
    "PutOriginEndpointPolicyRequestRequestTypeDef",
    "ScteOutputTypeDef",
    "ScteTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateChannelGroupRequestRequestTypeDef",
    "UpdateChannelRequestRequestTypeDef",
    "CreateChannelGroupResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetChannelGroupResponseTypeDef",
    "GetChannelPolicyResponseTypeDef",
    "GetOriginEndpointPolicyResponseTypeDef",
    "ListChannelGroupsResponseTypeDef",
    "ListChannelsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "UpdateChannelGroupResponseTypeDef",
    "CreateChannelResponseTypeDef",
    "GetChannelResponseTypeDef",
    "UpdateChannelResponseTypeDef",
    "SpekeKeyProviderOutputTypeDef",
    "SpekeKeyProviderTypeDef",
    "GetDashManifestConfigurationTypeDef",
    "GetHlsManifestConfigurationTypeDef",
    "GetLowLatencyHlsManifestConfigurationTypeDef",
    "FilterConfigurationTypeDef",
    "ListChannelGroupsRequestListChannelGroupsPaginateTypeDef",
    "ListChannelsRequestListChannelsPaginateTypeDef",
    "ListOriginEndpointsRequestListOriginEndpointsPaginateTypeDef",
    "OriginEndpointListConfigurationTypeDef",
    "ScteUnionTypeDef",
    "EncryptionOutputTypeDef",
    "SpekeKeyProviderUnionTypeDef",
    "FilterConfigurationUnionTypeDef",
    "ListOriginEndpointsResponseTypeDef",
    "SegmentOutputTypeDef",
    "EncryptionTypeDef",
    "CreateDashManifestConfigurationTypeDef",
    "CreateHlsManifestConfigurationTypeDef",
    "CreateLowLatencyHlsManifestConfigurationTypeDef",
    "CreateOriginEndpointResponseTypeDef",
    "GetOriginEndpointResponseTypeDef",
    "UpdateOriginEndpointResponseTypeDef",
    "EncryptionUnionTypeDef",
    "SegmentTypeDef",
    "CreateOriginEndpointRequestRequestTypeDef",
    "UpdateOriginEndpointRequestRequestTypeDef",
)

ChannelGroupListConfigurationTypeDef = TypedDict(
    "ChannelGroupListConfigurationTypeDef",
    {
        "ChannelGroupName": str,
        "Arn": str,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
        "Description": NotRequired[str],
    },
)
ChannelListConfigurationTypeDef = TypedDict(
    "ChannelListConfigurationTypeDef",
    {
        "Arn": str,
        "ChannelName": str,
        "ChannelGroupName": str,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
        "Description": NotRequired[str],
        "InputType": NotRequired[InputTypeType],
    },
)
CreateChannelGroupRequestRequestTypeDef = TypedDict(
    "CreateChannelGroupRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
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
CreateChannelRequestRequestTypeDef = TypedDict(
    "CreateChannelRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
        "ClientToken": NotRequired[str],
        "InputType": NotRequired[InputTypeType],
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
IngestEndpointTypeDef = TypedDict(
    "IngestEndpointTypeDef",
    {
        "Id": NotRequired[str],
        "Url": NotRequired[str],
    },
)
DashUtcTimingTypeDef = TypedDict(
    "DashUtcTimingTypeDef",
    {
        "TimingMode": NotRequired[DashUtcTimingModeType],
        "TimingSource": NotRequired[str],
    },
)
ScteDashTypeDef = TypedDict(
    "ScteDashTypeDef",
    {
        "AdMarkerDash": NotRequired[AdMarkerDashType],
    },
)
ScteHlsTypeDef = TypedDict(
    "ScteHlsTypeDef",
    {
        "AdMarkerHls": NotRequired[Literal["DATERANGE"]],
    },
)
StartTagTypeDef = TypedDict(
    "StartTagTypeDef",
    {
        "TimeOffset": float,
        "Precise": NotRequired[bool],
    },
)
ForceEndpointErrorConfigurationTypeDef = TypedDict(
    "ForceEndpointErrorConfigurationTypeDef",
    {
        "EndpointErrorConditions": NotRequired[Sequence[EndpointErrorConditionType]],
    },
)
ForceEndpointErrorConfigurationOutputTypeDef = TypedDict(
    "ForceEndpointErrorConfigurationOutputTypeDef",
    {
        "EndpointErrorConditions": NotRequired[List[EndpointErrorConditionType]],
    },
)
DeleteChannelGroupRequestRequestTypeDef = TypedDict(
    "DeleteChannelGroupRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
    },
)
DeleteChannelPolicyRequestRequestTypeDef = TypedDict(
    "DeleteChannelPolicyRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
    },
)
DeleteChannelRequestRequestTypeDef = TypedDict(
    "DeleteChannelRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
    },
)
DeleteOriginEndpointPolicyRequestRequestTypeDef = TypedDict(
    "DeleteOriginEndpointPolicyRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
        "OriginEndpointName": str,
    },
)
DeleteOriginEndpointRequestRequestTypeDef = TypedDict(
    "DeleteOriginEndpointRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
        "OriginEndpointName": str,
    },
)
EncryptionContractConfigurationTypeDef = TypedDict(
    "EncryptionContractConfigurationTypeDef",
    {
        "PresetSpeke20Audio": PresetSpeke20AudioType,
        "PresetSpeke20Video": PresetSpeke20VideoType,
    },
)
EncryptionMethodTypeDef = TypedDict(
    "EncryptionMethodTypeDef",
    {
        "TsEncryptionMethod": NotRequired[TsEncryptionMethodType],
        "CmafEncryptionMethod": NotRequired[CmafEncryptionMethodType],
    },
)
FilterConfigurationOutputTypeDef = TypedDict(
    "FilterConfigurationOutputTypeDef",
    {
        "ManifestFilter": NotRequired[str],
        "Start": NotRequired[datetime],
        "End": NotRequired[datetime],
        "TimeDelaySeconds": NotRequired[int],
        "ClipStartTime": NotRequired[datetime],
    },
)
TimestampTypeDef = Union[datetime, str]
GetChannelGroupRequestRequestTypeDef = TypedDict(
    "GetChannelGroupRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
    },
)
GetChannelPolicyRequestRequestTypeDef = TypedDict(
    "GetChannelPolicyRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
    },
)
GetChannelRequestRequestTypeDef = TypedDict(
    "GetChannelRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
    },
)
GetOriginEndpointPolicyRequestRequestTypeDef = TypedDict(
    "GetOriginEndpointPolicyRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
        "OriginEndpointName": str,
    },
)
GetOriginEndpointRequestRequestTypeDef = TypedDict(
    "GetOriginEndpointRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
        "OriginEndpointName": str,
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
ListChannelGroupsRequestRequestTypeDef = TypedDict(
    "ListChannelGroupsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListChannelsRequestRequestTypeDef = TypedDict(
    "ListChannelsRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListDashManifestConfigurationTypeDef = TypedDict(
    "ListDashManifestConfigurationTypeDef",
    {
        "ManifestName": str,
        "Url": NotRequired[str],
    },
)
ListHlsManifestConfigurationTypeDef = TypedDict(
    "ListHlsManifestConfigurationTypeDef",
    {
        "ManifestName": str,
        "ChildManifestName": NotRequired[str],
        "Url": NotRequired[str],
    },
)
ListLowLatencyHlsManifestConfigurationTypeDef = TypedDict(
    "ListLowLatencyHlsManifestConfigurationTypeDef",
    {
        "ManifestName": str,
        "ChildManifestName": NotRequired[str],
        "Url": NotRequired[str],
    },
)
ListOriginEndpointsRequestRequestTypeDef = TypedDict(
    "ListOriginEndpointsRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
PutChannelPolicyRequestRequestTypeDef = TypedDict(
    "PutChannelPolicyRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
        "Policy": str,
    },
)
PutOriginEndpointPolicyRequestRequestTypeDef = TypedDict(
    "PutOriginEndpointPolicyRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
        "OriginEndpointName": str,
        "Policy": str,
    },
)
ScteOutputTypeDef = TypedDict(
    "ScteOutputTypeDef",
    {
        "ScteFilter": NotRequired[List[ScteFilterType]],
    },
)
ScteTypeDef = TypedDict(
    "ScteTypeDef",
    {
        "ScteFilter": NotRequired[Sequence[ScteFilterType]],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateChannelGroupRequestRequestTypeDef = TypedDict(
    "UpdateChannelGroupRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
        "ETag": NotRequired[str],
        "Description": NotRequired[str],
    },
)
UpdateChannelRequestRequestTypeDef = TypedDict(
    "UpdateChannelRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
        "ETag": NotRequired[str],
        "Description": NotRequired[str],
    },
)
CreateChannelGroupResponseTypeDef = TypedDict(
    "CreateChannelGroupResponseTypeDef",
    {
        "ChannelGroupName": str,
        "Arn": str,
        "EgressDomain": str,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
        "ETag": str,
        "Description": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetChannelGroupResponseTypeDef = TypedDict(
    "GetChannelGroupResponseTypeDef",
    {
        "ChannelGroupName": str,
        "Arn": str,
        "EgressDomain": str,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
        "Description": str,
        "ETag": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetChannelPolicyResponseTypeDef = TypedDict(
    "GetChannelPolicyResponseTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
        "Policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetOriginEndpointPolicyResponseTypeDef = TypedDict(
    "GetOriginEndpointPolicyResponseTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
        "OriginEndpointName": str,
        "Policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListChannelGroupsResponseTypeDef = TypedDict(
    "ListChannelGroupsResponseTypeDef",
    {
        "Items": List[ChannelGroupListConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListChannelsResponseTypeDef = TypedDict(
    "ListChannelsResponseTypeDef",
    {
        "Items": List[ChannelListConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateChannelGroupResponseTypeDef = TypedDict(
    "UpdateChannelGroupResponseTypeDef",
    {
        "ChannelGroupName": str,
        "Arn": str,
        "EgressDomain": str,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
        "Description": str,
        "ETag": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateChannelResponseTypeDef = TypedDict(
    "CreateChannelResponseTypeDef",
    {
        "Arn": str,
        "ChannelName": str,
        "ChannelGroupName": str,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
        "Description": str,
        "IngestEndpoints": List[IngestEndpointTypeDef],
        "InputType": InputTypeType,
        "ETag": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetChannelResponseTypeDef = TypedDict(
    "GetChannelResponseTypeDef",
    {
        "Arn": str,
        "ChannelName": str,
        "ChannelGroupName": str,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
        "Description": str,
        "IngestEndpoints": List[IngestEndpointTypeDef],
        "InputType": InputTypeType,
        "ETag": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateChannelResponseTypeDef = TypedDict(
    "UpdateChannelResponseTypeDef",
    {
        "Arn": str,
        "ChannelName": str,
        "ChannelGroupName": str,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
        "Description": str,
        "IngestEndpoints": List[IngestEndpointTypeDef],
        "InputType": InputTypeType,
        "ETag": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SpekeKeyProviderOutputTypeDef = TypedDict(
    "SpekeKeyProviderOutputTypeDef",
    {
        "EncryptionContractConfiguration": EncryptionContractConfigurationTypeDef,
        "ResourceId": str,
        "DrmSystems": List[DrmSystemType],
        "RoleArn": str,
        "Url": str,
    },
)
SpekeKeyProviderTypeDef = TypedDict(
    "SpekeKeyProviderTypeDef",
    {
        "EncryptionContractConfiguration": EncryptionContractConfigurationTypeDef,
        "ResourceId": str,
        "DrmSystems": Sequence[DrmSystemType],
        "RoleArn": str,
        "Url": str,
    },
)
GetDashManifestConfigurationTypeDef = TypedDict(
    "GetDashManifestConfigurationTypeDef",
    {
        "ManifestName": str,
        "Url": str,
        "ManifestWindowSeconds": NotRequired[int],
        "FilterConfiguration": NotRequired[FilterConfigurationOutputTypeDef],
        "MinUpdatePeriodSeconds": NotRequired[int],
        "MinBufferTimeSeconds": NotRequired[int],
        "SuggestedPresentationDelaySeconds": NotRequired[int],
        "SegmentTemplateFormat": NotRequired[Literal["NUMBER_WITH_TIMELINE"]],
        "PeriodTriggers": NotRequired[List[DashPeriodTriggerType]],
        "ScteDash": NotRequired[ScteDashTypeDef],
        "DrmSignaling": NotRequired[DashDrmSignalingType],
        "UtcTiming": NotRequired[DashUtcTimingTypeDef],
    },
)
GetHlsManifestConfigurationTypeDef = TypedDict(
    "GetHlsManifestConfigurationTypeDef",
    {
        "ManifestName": str,
        "Url": str,
        "ChildManifestName": NotRequired[str],
        "ManifestWindowSeconds": NotRequired[int],
        "ProgramDateTimeIntervalSeconds": NotRequired[int],
        "ScteHls": NotRequired[ScteHlsTypeDef],
        "FilterConfiguration": NotRequired[FilterConfigurationOutputTypeDef],
        "StartTag": NotRequired[StartTagTypeDef],
    },
)
GetLowLatencyHlsManifestConfigurationTypeDef = TypedDict(
    "GetLowLatencyHlsManifestConfigurationTypeDef",
    {
        "ManifestName": str,
        "Url": str,
        "ChildManifestName": NotRequired[str],
        "ManifestWindowSeconds": NotRequired[int],
        "ProgramDateTimeIntervalSeconds": NotRequired[int],
        "ScteHls": NotRequired[ScteHlsTypeDef],
        "FilterConfiguration": NotRequired[FilterConfigurationOutputTypeDef],
        "StartTag": NotRequired[StartTagTypeDef],
    },
)
FilterConfigurationTypeDef = TypedDict(
    "FilterConfigurationTypeDef",
    {
        "ManifestFilter": NotRequired[str],
        "Start": NotRequired[TimestampTypeDef],
        "End": NotRequired[TimestampTypeDef],
        "TimeDelaySeconds": NotRequired[int],
        "ClipStartTime": NotRequired[TimestampTypeDef],
    },
)
ListChannelGroupsRequestListChannelGroupsPaginateTypeDef = TypedDict(
    "ListChannelGroupsRequestListChannelGroupsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListChannelsRequestListChannelsPaginateTypeDef = TypedDict(
    "ListChannelsRequestListChannelsPaginateTypeDef",
    {
        "ChannelGroupName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOriginEndpointsRequestListOriginEndpointsPaginateTypeDef = TypedDict(
    "ListOriginEndpointsRequestListOriginEndpointsPaginateTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
OriginEndpointListConfigurationTypeDef = TypedDict(
    "OriginEndpointListConfigurationTypeDef",
    {
        "Arn": str,
        "ChannelGroupName": str,
        "ChannelName": str,
        "OriginEndpointName": str,
        "ContainerType": ContainerTypeType,
        "Description": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "ModifiedAt": NotRequired[datetime],
        "HlsManifests": NotRequired[List[ListHlsManifestConfigurationTypeDef]],
        "LowLatencyHlsManifests": NotRequired[List[ListLowLatencyHlsManifestConfigurationTypeDef]],
        "DashManifests": NotRequired[List[ListDashManifestConfigurationTypeDef]],
        "ForceEndpointErrorConfiguration": NotRequired[
            ForceEndpointErrorConfigurationOutputTypeDef
        ],
    },
)
ScteUnionTypeDef = Union[ScteTypeDef, ScteOutputTypeDef]
EncryptionOutputTypeDef = TypedDict(
    "EncryptionOutputTypeDef",
    {
        "EncryptionMethod": EncryptionMethodTypeDef,
        "SpekeKeyProvider": SpekeKeyProviderOutputTypeDef,
        "ConstantInitializationVector": NotRequired[str],
        "KeyRotationIntervalSeconds": NotRequired[int],
    },
)
SpekeKeyProviderUnionTypeDef = Union[SpekeKeyProviderTypeDef, SpekeKeyProviderOutputTypeDef]
FilterConfigurationUnionTypeDef = Union[
    FilterConfigurationTypeDef, FilterConfigurationOutputTypeDef
]
ListOriginEndpointsResponseTypeDef = TypedDict(
    "ListOriginEndpointsResponseTypeDef",
    {
        "Items": List[OriginEndpointListConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
SegmentOutputTypeDef = TypedDict(
    "SegmentOutputTypeDef",
    {
        "SegmentDurationSeconds": NotRequired[int],
        "SegmentName": NotRequired[str],
        "TsUseAudioRenditionGroup": NotRequired[bool],
        "IncludeIframeOnlyStreams": NotRequired[bool],
        "TsIncludeDvbSubtitles": NotRequired[bool],
        "Scte": NotRequired[ScteOutputTypeDef],
        "Encryption": NotRequired[EncryptionOutputTypeDef],
    },
)
EncryptionTypeDef = TypedDict(
    "EncryptionTypeDef",
    {
        "EncryptionMethod": EncryptionMethodTypeDef,
        "SpekeKeyProvider": SpekeKeyProviderUnionTypeDef,
        "ConstantInitializationVector": NotRequired[str],
        "KeyRotationIntervalSeconds": NotRequired[int],
    },
)
CreateDashManifestConfigurationTypeDef = TypedDict(
    "CreateDashManifestConfigurationTypeDef",
    {
        "ManifestName": str,
        "ManifestWindowSeconds": NotRequired[int],
        "FilterConfiguration": NotRequired[FilterConfigurationUnionTypeDef],
        "MinUpdatePeriodSeconds": NotRequired[int],
        "MinBufferTimeSeconds": NotRequired[int],
        "SuggestedPresentationDelaySeconds": NotRequired[int],
        "SegmentTemplateFormat": NotRequired[Literal["NUMBER_WITH_TIMELINE"]],
        "PeriodTriggers": NotRequired[Sequence[DashPeriodTriggerType]],
        "ScteDash": NotRequired[ScteDashTypeDef],
        "DrmSignaling": NotRequired[DashDrmSignalingType],
        "UtcTiming": NotRequired[DashUtcTimingTypeDef],
    },
)
CreateHlsManifestConfigurationTypeDef = TypedDict(
    "CreateHlsManifestConfigurationTypeDef",
    {
        "ManifestName": str,
        "ChildManifestName": NotRequired[str],
        "ScteHls": NotRequired[ScteHlsTypeDef],
        "StartTag": NotRequired[StartTagTypeDef],
        "ManifestWindowSeconds": NotRequired[int],
        "ProgramDateTimeIntervalSeconds": NotRequired[int],
        "FilterConfiguration": NotRequired[FilterConfigurationUnionTypeDef],
    },
)
CreateLowLatencyHlsManifestConfigurationTypeDef = TypedDict(
    "CreateLowLatencyHlsManifestConfigurationTypeDef",
    {
        "ManifestName": str,
        "ChildManifestName": NotRequired[str],
        "ScteHls": NotRequired[ScteHlsTypeDef],
        "StartTag": NotRequired[StartTagTypeDef],
        "ManifestWindowSeconds": NotRequired[int],
        "ProgramDateTimeIntervalSeconds": NotRequired[int],
        "FilterConfiguration": NotRequired[FilterConfigurationUnionTypeDef],
    },
)
CreateOriginEndpointResponseTypeDef = TypedDict(
    "CreateOriginEndpointResponseTypeDef",
    {
        "Arn": str,
        "ChannelGroupName": str,
        "ChannelName": str,
        "OriginEndpointName": str,
        "ContainerType": ContainerTypeType,
        "Segment": SegmentOutputTypeDef,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
        "Description": str,
        "StartoverWindowSeconds": int,
        "HlsManifests": List[GetHlsManifestConfigurationTypeDef],
        "LowLatencyHlsManifests": List[GetLowLatencyHlsManifestConfigurationTypeDef],
        "DashManifests": List[GetDashManifestConfigurationTypeDef],
        "ForceEndpointErrorConfiguration": ForceEndpointErrorConfigurationOutputTypeDef,
        "ETag": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetOriginEndpointResponseTypeDef = TypedDict(
    "GetOriginEndpointResponseTypeDef",
    {
        "Arn": str,
        "ChannelGroupName": str,
        "ChannelName": str,
        "OriginEndpointName": str,
        "ContainerType": ContainerTypeType,
        "Segment": SegmentOutputTypeDef,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
        "Description": str,
        "StartoverWindowSeconds": int,
        "HlsManifests": List[GetHlsManifestConfigurationTypeDef],
        "LowLatencyHlsManifests": List[GetLowLatencyHlsManifestConfigurationTypeDef],
        "DashManifests": List[GetDashManifestConfigurationTypeDef],
        "ForceEndpointErrorConfiguration": ForceEndpointErrorConfigurationOutputTypeDef,
        "ETag": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateOriginEndpointResponseTypeDef = TypedDict(
    "UpdateOriginEndpointResponseTypeDef",
    {
        "Arn": str,
        "ChannelGroupName": str,
        "ChannelName": str,
        "OriginEndpointName": str,
        "ContainerType": ContainerTypeType,
        "Segment": SegmentOutputTypeDef,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
        "Description": str,
        "StartoverWindowSeconds": int,
        "HlsManifests": List[GetHlsManifestConfigurationTypeDef],
        "LowLatencyHlsManifests": List[GetLowLatencyHlsManifestConfigurationTypeDef],
        "ForceEndpointErrorConfiguration": ForceEndpointErrorConfigurationOutputTypeDef,
        "ETag": str,
        "Tags": Dict[str, str],
        "DashManifests": List[GetDashManifestConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EncryptionUnionTypeDef = Union[EncryptionTypeDef, EncryptionOutputTypeDef]
SegmentTypeDef = TypedDict(
    "SegmentTypeDef",
    {
        "SegmentDurationSeconds": NotRequired[int],
        "SegmentName": NotRequired[str],
        "TsUseAudioRenditionGroup": NotRequired[bool],
        "IncludeIframeOnlyStreams": NotRequired[bool],
        "TsIncludeDvbSubtitles": NotRequired[bool],
        "Scte": NotRequired[ScteUnionTypeDef],
        "Encryption": NotRequired[EncryptionUnionTypeDef],
    },
)
CreateOriginEndpointRequestRequestTypeDef = TypedDict(
    "CreateOriginEndpointRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
        "OriginEndpointName": str,
        "ContainerType": ContainerTypeType,
        "Segment": NotRequired[SegmentTypeDef],
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
        "StartoverWindowSeconds": NotRequired[int],
        "HlsManifests": NotRequired[Sequence[CreateHlsManifestConfigurationTypeDef]],
        "LowLatencyHlsManifests": NotRequired[
            Sequence[CreateLowLatencyHlsManifestConfigurationTypeDef]
        ],
        "DashManifests": NotRequired[Sequence[CreateDashManifestConfigurationTypeDef]],
        "ForceEndpointErrorConfiguration": NotRequired[ForceEndpointErrorConfigurationTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
UpdateOriginEndpointRequestRequestTypeDef = TypedDict(
    "UpdateOriginEndpointRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
        "OriginEndpointName": str,
        "ContainerType": ContainerTypeType,
        "Segment": NotRequired[SegmentTypeDef],
        "Description": NotRequired[str],
        "StartoverWindowSeconds": NotRequired[int],
        "HlsManifests": NotRequired[Sequence[CreateHlsManifestConfigurationTypeDef]],
        "LowLatencyHlsManifests": NotRequired[
            Sequence[CreateLowLatencyHlsManifestConfigurationTypeDef]
        ],
        "DashManifests": NotRequired[Sequence[CreateDashManifestConfigurationTypeDef]],
        "ForceEndpointErrorConfiguration": NotRequired[ForceEndpointErrorConfigurationTypeDef],
        "ETag": NotRequired[str],
    },
)
