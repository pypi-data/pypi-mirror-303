"""
Type annotations for mediapackage service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/type_defs/)

Usage::

    ```python
    from mypy_boto3_mediapackage.type_defs import AuthorizationTypeDef

    data: AuthorizationTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AdMarkersType,
    AdsOnDeliveryRestrictionsType,
    AdTriggersElementType,
    CmafEncryptionMethodType,
    EncryptionMethodType,
    ManifestLayoutType,
    OriginationType,
    PlaylistTypeType,
    PresetSpeke20AudioType,
    PresetSpeke20VideoType,
    ProfileType,
    SegmentTemplateFormatType,
    StatusType,
    StreamOrderType,
    UtcTimingType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AuthorizationTypeDef",
    "EgressAccessLogsTypeDef",
    "IngressAccessLogsTypeDef",
    "HlsManifestCreateOrUpdateParametersTypeDef",
    "StreamSelectionTypeDef",
    "HlsManifestTypeDef",
    "ResponseMetadataTypeDef",
    "CreateChannelRequestRequestTypeDef",
    "S3DestinationTypeDef",
    "DeleteChannelRequestRequestTypeDef",
    "DeleteOriginEndpointRequestRequestTypeDef",
    "DescribeChannelRequestRequestTypeDef",
    "DescribeHarvestJobRequestRequestTypeDef",
    "DescribeOriginEndpointRequestRequestTypeDef",
    "EncryptionContractConfigurationTypeDef",
    "IngestEndpointTypeDef",
    "PaginatorConfigTypeDef",
    "ListChannelsRequestRequestTypeDef",
    "ListHarvestJobsRequestRequestTypeDef",
    "ListOriginEndpointsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "RotateChannelCredentialsRequestRequestTypeDef",
    "RotateIngestEndpointCredentialsRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateChannelRequestRequestTypeDef",
    "ConfigureLogsRequestRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "CreateHarvestJobRequestRequestTypeDef",
    "CreateHarvestJobResponseTypeDef",
    "DescribeHarvestJobResponseTypeDef",
    "HarvestJobTypeDef",
    "SpekeKeyProviderOutputTypeDef",
    "SpekeKeyProviderTypeDef",
    "HlsIngestTypeDef",
    "ListChannelsRequestListChannelsPaginateTypeDef",
    "ListHarvestJobsRequestListHarvestJobsPaginateTypeDef",
    "ListOriginEndpointsRequestListOriginEndpointsPaginateTypeDef",
    "ListHarvestJobsResponseTypeDef",
    "CmafEncryptionOutputTypeDef",
    "DashEncryptionOutputTypeDef",
    "HlsEncryptionOutputTypeDef",
    "MssEncryptionOutputTypeDef",
    "SpekeKeyProviderUnionTypeDef",
    "ChannelTypeDef",
    "ConfigureLogsResponseTypeDef",
    "CreateChannelResponseTypeDef",
    "DescribeChannelResponseTypeDef",
    "RotateChannelCredentialsResponseTypeDef",
    "RotateIngestEndpointCredentialsResponseTypeDef",
    "UpdateChannelResponseTypeDef",
    "CmafPackageTypeDef",
    "DashPackageOutputTypeDef",
    "HlsPackageOutputTypeDef",
    "MssPackageOutputTypeDef",
    "CmafEncryptionTypeDef",
    "DashEncryptionTypeDef",
    "HlsEncryptionTypeDef",
    "MssEncryptionTypeDef",
    "ListChannelsResponseTypeDef",
    "CreateOriginEndpointResponseTypeDef",
    "DescribeOriginEndpointResponseTypeDef",
    "OriginEndpointTypeDef",
    "UpdateOriginEndpointResponseTypeDef",
    "CmafEncryptionUnionTypeDef",
    "DashEncryptionUnionTypeDef",
    "HlsEncryptionUnionTypeDef",
    "MssEncryptionUnionTypeDef",
    "ListOriginEndpointsResponseTypeDef",
    "CmafPackageCreateOrUpdateParametersTypeDef",
    "DashPackageTypeDef",
    "HlsPackageTypeDef",
    "MssPackageTypeDef",
    "CreateOriginEndpointRequestRequestTypeDef",
    "UpdateOriginEndpointRequestRequestTypeDef",
)

AuthorizationTypeDef = TypedDict(
    "AuthorizationTypeDef",
    {
        "CdnIdentifierSecret": str,
        "SecretsRoleArn": str,
    },
)
EgressAccessLogsTypeDef = TypedDict(
    "EgressAccessLogsTypeDef",
    {
        "LogGroupName": NotRequired[str],
    },
)
IngressAccessLogsTypeDef = TypedDict(
    "IngressAccessLogsTypeDef",
    {
        "LogGroupName": NotRequired[str],
    },
)
HlsManifestCreateOrUpdateParametersTypeDef = TypedDict(
    "HlsManifestCreateOrUpdateParametersTypeDef",
    {
        "Id": str,
        "AdMarkers": NotRequired[AdMarkersType],
        "AdTriggers": NotRequired[Sequence[AdTriggersElementType]],
        "AdsOnDeliveryRestrictions": NotRequired[AdsOnDeliveryRestrictionsType],
        "IncludeIframeOnlyStream": NotRequired[bool],
        "ManifestName": NotRequired[str],
        "PlaylistType": NotRequired[PlaylistTypeType],
        "PlaylistWindowSeconds": NotRequired[int],
        "ProgramDateTimeIntervalSeconds": NotRequired[int],
    },
)
StreamSelectionTypeDef = TypedDict(
    "StreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": NotRequired[int],
        "MinVideoBitsPerSecond": NotRequired[int],
        "StreamOrder": NotRequired[StreamOrderType],
    },
)
HlsManifestTypeDef = TypedDict(
    "HlsManifestTypeDef",
    {
        "Id": str,
        "AdMarkers": NotRequired[AdMarkersType],
        "IncludeIframeOnlyStream": NotRequired[bool],
        "ManifestName": NotRequired[str],
        "PlaylistType": NotRequired[PlaylistTypeType],
        "PlaylistWindowSeconds": NotRequired[int],
        "ProgramDateTimeIntervalSeconds": NotRequired[int],
        "Url": NotRequired[str],
        "AdTriggers": NotRequired[List[AdTriggersElementType]],
        "AdsOnDeliveryRestrictions": NotRequired[AdsOnDeliveryRestrictionsType],
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
        "Id": str,
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
S3DestinationTypeDef = TypedDict(
    "S3DestinationTypeDef",
    {
        "BucketName": str,
        "ManifestKey": str,
        "RoleArn": str,
    },
)
DeleteChannelRequestRequestTypeDef = TypedDict(
    "DeleteChannelRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DeleteOriginEndpointRequestRequestTypeDef = TypedDict(
    "DeleteOriginEndpointRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DescribeChannelRequestRequestTypeDef = TypedDict(
    "DescribeChannelRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DescribeHarvestJobRequestRequestTypeDef = TypedDict(
    "DescribeHarvestJobRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DescribeOriginEndpointRequestRequestTypeDef = TypedDict(
    "DescribeOriginEndpointRequestRequestTypeDef",
    {
        "Id": str,
    },
)
EncryptionContractConfigurationTypeDef = TypedDict(
    "EncryptionContractConfigurationTypeDef",
    {
        "PresetSpeke20Audio": PresetSpeke20AudioType,
        "PresetSpeke20Video": PresetSpeke20VideoType,
    },
)
IngestEndpointTypeDef = TypedDict(
    "IngestEndpointTypeDef",
    {
        "Id": NotRequired[str],
        "Password": NotRequired[str],
        "Url": NotRequired[str],
        "Username": NotRequired[str],
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
ListChannelsRequestRequestTypeDef = TypedDict(
    "ListChannelsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListHarvestJobsRequestRequestTypeDef = TypedDict(
    "ListHarvestJobsRequestRequestTypeDef",
    {
        "IncludeChannelId": NotRequired[str],
        "IncludeStatus": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListOriginEndpointsRequestRequestTypeDef = TypedDict(
    "ListOriginEndpointsRequestRequestTypeDef",
    {
        "ChannelId": NotRequired[str],
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
RotateChannelCredentialsRequestRequestTypeDef = TypedDict(
    "RotateChannelCredentialsRequestRequestTypeDef",
    {
        "Id": str,
    },
)
RotateIngestEndpointCredentialsRequestRequestTypeDef = TypedDict(
    "RotateIngestEndpointCredentialsRequestRequestTypeDef",
    {
        "Id": str,
        "IngestEndpointId": str,
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
UpdateChannelRequestRequestTypeDef = TypedDict(
    "UpdateChannelRequestRequestTypeDef",
    {
        "Id": str,
        "Description": NotRequired[str],
    },
)
ConfigureLogsRequestRequestTypeDef = TypedDict(
    "ConfigureLogsRequestRequestTypeDef",
    {
        "Id": str,
        "EgressAccessLogs": NotRequired[EgressAccessLogsTypeDef],
        "IngressAccessLogs": NotRequired[IngressAccessLogsTypeDef],
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
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateHarvestJobRequestRequestTypeDef = TypedDict(
    "CreateHarvestJobRequestRequestTypeDef",
    {
        "EndTime": str,
        "Id": str,
        "OriginEndpointId": str,
        "S3Destination": S3DestinationTypeDef,
        "StartTime": str,
    },
)
CreateHarvestJobResponseTypeDef = TypedDict(
    "CreateHarvestJobResponseTypeDef",
    {
        "Arn": str,
        "ChannelId": str,
        "CreatedAt": str,
        "EndTime": str,
        "Id": str,
        "OriginEndpointId": str,
        "S3Destination": S3DestinationTypeDef,
        "StartTime": str,
        "Status": StatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeHarvestJobResponseTypeDef = TypedDict(
    "DescribeHarvestJobResponseTypeDef",
    {
        "Arn": str,
        "ChannelId": str,
        "CreatedAt": str,
        "EndTime": str,
        "Id": str,
        "OriginEndpointId": str,
        "S3Destination": S3DestinationTypeDef,
        "StartTime": str,
        "Status": StatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
HarvestJobTypeDef = TypedDict(
    "HarvestJobTypeDef",
    {
        "Arn": NotRequired[str],
        "ChannelId": NotRequired[str],
        "CreatedAt": NotRequired[str],
        "EndTime": NotRequired[str],
        "Id": NotRequired[str],
        "OriginEndpointId": NotRequired[str],
        "S3Destination": NotRequired[S3DestinationTypeDef],
        "StartTime": NotRequired[str],
        "Status": NotRequired[StatusType],
    },
)
SpekeKeyProviderOutputTypeDef = TypedDict(
    "SpekeKeyProviderOutputTypeDef",
    {
        "ResourceId": str,
        "RoleArn": str,
        "SystemIds": List[str],
        "Url": str,
        "CertificateArn": NotRequired[str],
        "EncryptionContractConfiguration": NotRequired[EncryptionContractConfigurationTypeDef],
    },
)
SpekeKeyProviderTypeDef = TypedDict(
    "SpekeKeyProviderTypeDef",
    {
        "ResourceId": str,
        "RoleArn": str,
        "SystemIds": Sequence[str],
        "Url": str,
        "CertificateArn": NotRequired[str],
        "EncryptionContractConfiguration": NotRequired[EncryptionContractConfigurationTypeDef],
    },
)
HlsIngestTypeDef = TypedDict(
    "HlsIngestTypeDef",
    {
        "IngestEndpoints": NotRequired[List[IngestEndpointTypeDef]],
    },
)
ListChannelsRequestListChannelsPaginateTypeDef = TypedDict(
    "ListChannelsRequestListChannelsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListHarvestJobsRequestListHarvestJobsPaginateTypeDef = TypedDict(
    "ListHarvestJobsRequestListHarvestJobsPaginateTypeDef",
    {
        "IncludeChannelId": NotRequired[str],
        "IncludeStatus": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOriginEndpointsRequestListOriginEndpointsPaginateTypeDef = TypedDict(
    "ListOriginEndpointsRequestListOriginEndpointsPaginateTypeDef",
    {
        "ChannelId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListHarvestJobsResponseTypeDef = TypedDict(
    "ListHarvestJobsResponseTypeDef",
    {
        "HarvestJobs": List[HarvestJobTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CmafEncryptionOutputTypeDef = TypedDict(
    "CmafEncryptionOutputTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderOutputTypeDef,
        "ConstantInitializationVector": NotRequired[str],
        "EncryptionMethod": NotRequired[CmafEncryptionMethodType],
        "KeyRotationIntervalSeconds": NotRequired[int],
    },
)
DashEncryptionOutputTypeDef = TypedDict(
    "DashEncryptionOutputTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderOutputTypeDef,
        "KeyRotationIntervalSeconds": NotRequired[int],
    },
)
HlsEncryptionOutputTypeDef = TypedDict(
    "HlsEncryptionOutputTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderOutputTypeDef,
        "ConstantInitializationVector": NotRequired[str],
        "EncryptionMethod": NotRequired[EncryptionMethodType],
        "KeyRotationIntervalSeconds": NotRequired[int],
        "RepeatExtXKey": NotRequired[bool],
    },
)
MssEncryptionOutputTypeDef = TypedDict(
    "MssEncryptionOutputTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderOutputTypeDef,
    },
)
SpekeKeyProviderUnionTypeDef = Union[SpekeKeyProviderTypeDef, SpekeKeyProviderOutputTypeDef]
ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "Arn": NotRequired[str],
        "CreatedAt": NotRequired[str],
        "Description": NotRequired[str],
        "EgressAccessLogs": NotRequired[EgressAccessLogsTypeDef],
        "HlsIngest": NotRequired[HlsIngestTypeDef],
        "Id": NotRequired[str],
        "IngressAccessLogs": NotRequired[IngressAccessLogsTypeDef],
        "Tags": NotRequired[Dict[str, str]],
    },
)
ConfigureLogsResponseTypeDef = TypedDict(
    "ConfigureLogsResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "Description": str,
        "EgressAccessLogs": EgressAccessLogsTypeDef,
        "HlsIngest": HlsIngestTypeDef,
        "Id": str,
        "IngressAccessLogs": IngressAccessLogsTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateChannelResponseTypeDef = TypedDict(
    "CreateChannelResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "Description": str,
        "EgressAccessLogs": EgressAccessLogsTypeDef,
        "HlsIngest": HlsIngestTypeDef,
        "Id": str,
        "IngressAccessLogs": IngressAccessLogsTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeChannelResponseTypeDef = TypedDict(
    "DescribeChannelResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "Description": str,
        "EgressAccessLogs": EgressAccessLogsTypeDef,
        "HlsIngest": HlsIngestTypeDef,
        "Id": str,
        "IngressAccessLogs": IngressAccessLogsTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RotateChannelCredentialsResponseTypeDef = TypedDict(
    "RotateChannelCredentialsResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "Description": str,
        "EgressAccessLogs": EgressAccessLogsTypeDef,
        "HlsIngest": HlsIngestTypeDef,
        "Id": str,
        "IngressAccessLogs": IngressAccessLogsTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RotateIngestEndpointCredentialsResponseTypeDef = TypedDict(
    "RotateIngestEndpointCredentialsResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "Description": str,
        "EgressAccessLogs": EgressAccessLogsTypeDef,
        "HlsIngest": HlsIngestTypeDef,
        "Id": str,
        "IngressAccessLogs": IngressAccessLogsTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateChannelResponseTypeDef = TypedDict(
    "UpdateChannelResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "Description": str,
        "EgressAccessLogs": EgressAccessLogsTypeDef,
        "HlsIngest": HlsIngestTypeDef,
        "Id": str,
        "IngressAccessLogs": IngressAccessLogsTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CmafPackageTypeDef = TypedDict(
    "CmafPackageTypeDef",
    {
        "Encryption": NotRequired[CmafEncryptionOutputTypeDef],
        "HlsManifests": NotRequired[List[HlsManifestTypeDef]],
        "SegmentDurationSeconds": NotRequired[int],
        "SegmentPrefix": NotRequired[str],
        "StreamSelection": NotRequired[StreamSelectionTypeDef],
    },
)
DashPackageOutputTypeDef = TypedDict(
    "DashPackageOutputTypeDef",
    {
        "AdTriggers": NotRequired[List[AdTriggersElementType]],
        "AdsOnDeliveryRestrictions": NotRequired[AdsOnDeliveryRestrictionsType],
        "Encryption": NotRequired[DashEncryptionOutputTypeDef],
        "IncludeIframeOnlyStream": NotRequired[bool],
        "ManifestLayout": NotRequired[ManifestLayoutType],
        "ManifestWindowSeconds": NotRequired[int],
        "MinBufferTimeSeconds": NotRequired[int],
        "MinUpdatePeriodSeconds": NotRequired[int],
        "PeriodTriggers": NotRequired[List[Literal["ADS"]]],
        "Profile": NotRequired[ProfileType],
        "SegmentDurationSeconds": NotRequired[int],
        "SegmentTemplateFormat": NotRequired[SegmentTemplateFormatType],
        "StreamSelection": NotRequired[StreamSelectionTypeDef],
        "SuggestedPresentationDelaySeconds": NotRequired[int],
        "UtcTiming": NotRequired[UtcTimingType],
        "UtcTimingUri": NotRequired[str],
    },
)
HlsPackageOutputTypeDef = TypedDict(
    "HlsPackageOutputTypeDef",
    {
        "AdMarkers": NotRequired[AdMarkersType],
        "AdTriggers": NotRequired[List[AdTriggersElementType]],
        "AdsOnDeliveryRestrictions": NotRequired[AdsOnDeliveryRestrictionsType],
        "Encryption": NotRequired[HlsEncryptionOutputTypeDef],
        "IncludeDvbSubtitles": NotRequired[bool],
        "IncludeIframeOnlyStream": NotRequired[bool],
        "PlaylistType": NotRequired[PlaylistTypeType],
        "PlaylistWindowSeconds": NotRequired[int],
        "ProgramDateTimeIntervalSeconds": NotRequired[int],
        "SegmentDurationSeconds": NotRequired[int],
        "StreamSelection": NotRequired[StreamSelectionTypeDef],
        "UseAudioRenditionGroup": NotRequired[bool],
    },
)
MssPackageOutputTypeDef = TypedDict(
    "MssPackageOutputTypeDef",
    {
        "Encryption": NotRequired[MssEncryptionOutputTypeDef],
        "ManifestWindowSeconds": NotRequired[int],
        "SegmentDurationSeconds": NotRequired[int],
        "StreamSelection": NotRequired[StreamSelectionTypeDef],
    },
)
CmafEncryptionTypeDef = TypedDict(
    "CmafEncryptionTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderUnionTypeDef,
        "ConstantInitializationVector": NotRequired[str],
        "EncryptionMethod": NotRequired[CmafEncryptionMethodType],
        "KeyRotationIntervalSeconds": NotRequired[int],
    },
)
DashEncryptionTypeDef = TypedDict(
    "DashEncryptionTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderUnionTypeDef,
        "KeyRotationIntervalSeconds": NotRequired[int],
    },
)
HlsEncryptionTypeDef = TypedDict(
    "HlsEncryptionTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderUnionTypeDef,
        "ConstantInitializationVector": NotRequired[str],
        "EncryptionMethod": NotRequired[EncryptionMethodType],
        "KeyRotationIntervalSeconds": NotRequired[int],
        "RepeatExtXKey": NotRequired[bool],
    },
)
MssEncryptionTypeDef = TypedDict(
    "MssEncryptionTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderUnionTypeDef,
    },
)
ListChannelsResponseTypeDef = TypedDict(
    "ListChannelsResponseTypeDef",
    {
        "Channels": List[ChannelTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateOriginEndpointResponseTypeDef = TypedDict(
    "CreateOriginEndpointResponseTypeDef",
    {
        "Arn": str,
        "Authorization": AuthorizationTypeDef,
        "ChannelId": str,
        "CmafPackage": CmafPackageTypeDef,
        "CreatedAt": str,
        "DashPackage": DashPackageOutputTypeDef,
        "Description": str,
        "HlsPackage": HlsPackageOutputTypeDef,
        "Id": str,
        "ManifestName": str,
        "MssPackage": MssPackageOutputTypeDef,
        "Origination": OriginationType,
        "StartoverWindowSeconds": int,
        "Tags": Dict[str, str],
        "TimeDelaySeconds": int,
        "Url": str,
        "Whitelist": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeOriginEndpointResponseTypeDef = TypedDict(
    "DescribeOriginEndpointResponseTypeDef",
    {
        "Arn": str,
        "Authorization": AuthorizationTypeDef,
        "ChannelId": str,
        "CmafPackage": CmafPackageTypeDef,
        "CreatedAt": str,
        "DashPackage": DashPackageOutputTypeDef,
        "Description": str,
        "HlsPackage": HlsPackageOutputTypeDef,
        "Id": str,
        "ManifestName": str,
        "MssPackage": MssPackageOutputTypeDef,
        "Origination": OriginationType,
        "StartoverWindowSeconds": int,
        "Tags": Dict[str, str],
        "TimeDelaySeconds": int,
        "Url": str,
        "Whitelist": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OriginEndpointTypeDef = TypedDict(
    "OriginEndpointTypeDef",
    {
        "Arn": NotRequired[str],
        "Authorization": NotRequired[AuthorizationTypeDef],
        "ChannelId": NotRequired[str],
        "CmafPackage": NotRequired[CmafPackageTypeDef],
        "CreatedAt": NotRequired[str],
        "DashPackage": NotRequired[DashPackageOutputTypeDef],
        "Description": NotRequired[str],
        "HlsPackage": NotRequired[HlsPackageOutputTypeDef],
        "Id": NotRequired[str],
        "ManifestName": NotRequired[str],
        "MssPackage": NotRequired[MssPackageOutputTypeDef],
        "Origination": NotRequired[OriginationType],
        "StartoverWindowSeconds": NotRequired[int],
        "Tags": NotRequired[Dict[str, str]],
        "TimeDelaySeconds": NotRequired[int],
        "Url": NotRequired[str],
        "Whitelist": NotRequired[List[str]],
    },
)
UpdateOriginEndpointResponseTypeDef = TypedDict(
    "UpdateOriginEndpointResponseTypeDef",
    {
        "Arn": str,
        "Authorization": AuthorizationTypeDef,
        "ChannelId": str,
        "CmafPackage": CmafPackageTypeDef,
        "CreatedAt": str,
        "DashPackage": DashPackageOutputTypeDef,
        "Description": str,
        "HlsPackage": HlsPackageOutputTypeDef,
        "Id": str,
        "ManifestName": str,
        "MssPackage": MssPackageOutputTypeDef,
        "Origination": OriginationType,
        "StartoverWindowSeconds": int,
        "Tags": Dict[str, str],
        "TimeDelaySeconds": int,
        "Url": str,
        "Whitelist": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CmafEncryptionUnionTypeDef = Union[CmafEncryptionTypeDef, CmafEncryptionOutputTypeDef]
DashEncryptionUnionTypeDef = Union[DashEncryptionTypeDef, DashEncryptionOutputTypeDef]
HlsEncryptionUnionTypeDef = Union[HlsEncryptionTypeDef, HlsEncryptionOutputTypeDef]
MssEncryptionUnionTypeDef = Union[MssEncryptionTypeDef, MssEncryptionOutputTypeDef]
ListOriginEndpointsResponseTypeDef = TypedDict(
    "ListOriginEndpointsResponseTypeDef",
    {
        "OriginEndpoints": List[OriginEndpointTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CmafPackageCreateOrUpdateParametersTypeDef = TypedDict(
    "CmafPackageCreateOrUpdateParametersTypeDef",
    {
        "Encryption": NotRequired[CmafEncryptionUnionTypeDef],
        "HlsManifests": NotRequired[Sequence[HlsManifestCreateOrUpdateParametersTypeDef]],
        "SegmentDurationSeconds": NotRequired[int],
        "SegmentPrefix": NotRequired[str],
        "StreamSelection": NotRequired[StreamSelectionTypeDef],
    },
)
DashPackageTypeDef = TypedDict(
    "DashPackageTypeDef",
    {
        "AdTriggers": NotRequired[Sequence[AdTriggersElementType]],
        "AdsOnDeliveryRestrictions": NotRequired[AdsOnDeliveryRestrictionsType],
        "Encryption": NotRequired[DashEncryptionUnionTypeDef],
        "IncludeIframeOnlyStream": NotRequired[bool],
        "ManifestLayout": NotRequired[ManifestLayoutType],
        "ManifestWindowSeconds": NotRequired[int],
        "MinBufferTimeSeconds": NotRequired[int],
        "MinUpdatePeriodSeconds": NotRequired[int],
        "PeriodTriggers": NotRequired[Sequence[Literal["ADS"]]],
        "Profile": NotRequired[ProfileType],
        "SegmentDurationSeconds": NotRequired[int],
        "SegmentTemplateFormat": NotRequired[SegmentTemplateFormatType],
        "StreamSelection": NotRequired[StreamSelectionTypeDef],
        "SuggestedPresentationDelaySeconds": NotRequired[int],
        "UtcTiming": NotRequired[UtcTimingType],
        "UtcTimingUri": NotRequired[str],
    },
)
HlsPackageTypeDef = TypedDict(
    "HlsPackageTypeDef",
    {
        "AdMarkers": NotRequired[AdMarkersType],
        "AdTriggers": NotRequired[Sequence[AdTriggersElementType]],
        "AdsOnDeliveryRestrictions": NotRequired[AdsOnDeliveryRestrictionsType],
        "Encryption": NotRequired[HlsEncryptionUnionTypeDef],
        "IncludeDvbSubtitles": NotRequired[bool],
        "IncludeIframeOnlyStream": NotRequired[bool],
        "PlaylistType": NotRequired[PlaylistTypeType],
        "PlaylistWindowSeconds": NotRequired[int],
        "ProgramDateTimeIntervalSeconds": NotRequired[int],
        "SegmentDurationSeconds": NotRequired[int],
        "StreamSelection": NotRequired[StreamSelectionTypeDef],
        "UseAudioRenditionGroup": NotRequired[bool],
    },
)
MssPackageTypeDef = TypedDict(
    "MssPackageTypeDef",
    {
        "Encryption": NotRequired[MssEncryptionUnionTypeDef],
        "ManifestWindowSeconds": NotRequired[int],
        "SegmentDurationSeconds": NotRequired[int],
        "StreamSelection": NotRequired[StreamSelectionTypeDef],
    },
)
CreateOriginEndpointRequestRequestTypeDef = TypedDict(
    "CreateOriginEndpointRequestRequestTypeDef",
    {
        "ChannelId": str,
        "Id": str,
        "Authorization": NotRequired[AuthorizationTypeDef],
        "CmafPackage": NotRequired[CmafPackageCreateOrUpdateParametersTypeDef],
        "DashPackage": NotRequired[DashPackageTypeDef],
        "Description": NotRequired[str],
        "HlsPackage": NotRequired[HlsPackageTypeDef],
        "ManifestName": NotRequired[str],
        "MssPackage": NotRequired[MssPackageTypeDef],
        "Origination": NotRequired[OriginationType],
        "StartoverWindowSeconds": NotRequired[int],
        "Tags": NotRequired[Mapping[str, str]],
        "TimeDelaySeconds": NotRequired[int],
        "Whitelist": NotRequired[Sequence[str]],
    },
)
UpdateOriginEndpointRequestRequestTypeDef = TypedDict(
    "UpdateOriginEndpointRequestRequestTypeDef",
    {
        "Id": str,
        "Authorization": NotRequired[AuthorizationTypeDef],
        "CmafPackage": NotRequired[CmafPackageCreateOrUpdateParametersTypeDef],
        "DashPackage": NotRequired[DashPackageTypeDef],
        "Description": NotRequired[str],
        "HlsPackage": NotRequired[HlsPackageTypeDef],
        "ManifestName": NotRequired[str],
        "MssPackage": NotRequired[MssPackageTypeDef],
        "Origination": NotRequired[OriginationType],
        "StartoverWindowSeconds": NotRequired[int],
        "TimeDelaySeconds": NotRequired[int],
        "Whitelist": NotRequired[Sequence[str]],
    },
)
