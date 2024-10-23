"""
Type annotations for mediapackage-vod service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/type_defs/)

Usage::

    ```python
    from mypy_boto3_mediapackage_vod.type_defs import AssetShallowTypeDef

    data: AssetShallowTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AdMarkersType,
    EncryptionMethodType,
    ManifestLayoutType,
    PresetSpeke20AudioType,
    PresetSpeke20VideoType,
    ProfileType,
    ScteMarkersSourceType,
    SegmentTemplateFormatType,
    StreamOrderType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AssetShallowTypeDef",
    "AuthorizationTypeDef",
    "EgressAccessLogsTypeDef",
    "ResponseMetadataTypeDef",
    "CreateAssetRequestRequestTypeDef",
    "EgressEndpointTypeDef",
    "StreamSelectionTypeDef",
    "DeleteAssetRequestRequestTypeDef",
    "DeletePackagingConfigurationRequestRequestTypeDef",
    "DeletePackagingGroupRequestRequestTypeDef",
    "DescribeAssetRequestRequestTypeDef",
    "DescribePackagingConfigurationRequestRequestTypeDef",
    "DescribePackagingGroupRequestRequestTypeDef",
    "EncryptionContractConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ListAssetsRequestRequestTypeDef",
    "ListPackagingConfigurationsRequestRequestTypeDef",
    "ListPackagingGroupsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdatePackagingGroupRequestRequestTypeDef",
    "ConfigureLogsRequestRequestTypeDef",
    "CreatePackagingGroupRequestRequestTypeDef",
    "PackagingGroupTypeDef",
    "ConfigureLogsResponseTypeDef",
    "CreatePackagingGroupResponseTypeDef",
    "DescribePackagingGroupResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ListAssetsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "UpdatePackagingGroupResponseTypeDef",
    "CreateAssetResponseTypeDef",
    "DescribeAssetResponseTypeDef",
    "DashManifestTypeDef",
    "HlsManifestTypeDef",
    "MssManifestTypeDef",
    "SpekeKeyProviderOutputTypeDef",
    "SpekeKeyProviderTypeDef",
    "ListAssetsRequestListAssetsPaginateTypeDef",
    "ListPackagingConfigurationsRequestListPackagingConfigurationsPaginateTypeDef",
    "ListPackagingGroupsRequestListPackagingGroupsPaginateTypeDef",
    "ListPackagingGroupsResponseTypeDef",
    "CmafEncryptionOutputTypeDef",
    "DashEncryptionOutputTypeDef",
    "HlsEncryptionOutputTypeDef",
    "MssEncryptionOutputTypeDef",
    "SpekeKeyProviderUnionTypeDef",
    "CmafPackageOutputTypeDef",
    "DashPackageOutputTypeDef",
    "HlsPackageOutputTypeDef",
    "MssPackageOutputTypeDef",
    "CmafEncryptionTypeDef",
    "DashEncryptionTypeDef",
    "HlsEncryptionTypeDef",
    "MssEncryptionTypeDef",
    "CreatePackagingConfigurationResponseTypeDef",
    "DescribePackagingConfigurationResponseTypeDef",
    "PackagingConfigurationTypeDef",
    "CmafEncryptionUnionTypeDef",
    "DashEncryptionUnionTypeDef",
    "HlsEncryptionUnionTypeDef",
    "MssEncryptionUnionTypeDef",
    "ListPackagingConfigurationsResponseTypeDef",
    "CmafPackageTypeDef",
    "DashPackageTypeDef",
    "HlsPackageTypeDef",
    "MssPackageTypeDef",
    "CreatePackagingConfigurationRequestRequestTypeDef",
)

AssetShallowTypeDef = TypedDict(
    "AssetShallowTypeDef",
    {
        "Arn": NotRequired[str],
        "CreatedAt": NotRequired[str],
        "Id": NotRequired[str],
        "PackagingGroupId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "SourceArn": NotRequired[str],
        "SourceRoleArn": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
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
CreateAssetRequestRequestTypeDef = TypedDict(
    "CreateAssetRequestRequestTypeDef",
    {
        "Id": str,
        "PackagingGroupId": str,
        "SourceArn": str,
        "SourceRoleArn": str,
        "ResourceId": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
EgressEndpointTypeDef = TypedDict(
    "EgressEndpointTypeDef",
    {
        "PackagingConfigurationId": NotRequired[str],
        "Status": NotRequired[str],
        "Url": NotRequired[str],
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
DeleteAssetRequestRequestTypeDef = TypedDict(
    "DeleteAssetRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DeletePackagingConfigurationRequestRequestTypeDef = TypedDict(
    "DeletePackagingConfigurationRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DeletePackagingGroupRequestRequestTypeDef = TypedDict(
    "DeletePackagingGroupRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DescribeAssetRequestRequestTypeDef = TypedDict(
    "DescribeAssetRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DescribePackagingConfigurationRequestRequestTypeDef = TypedDict(
    "DescribePackagingConfigurationRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DescribePackagingGroupRequestRequestTypeDef = TypedDict(
    "DescribePackagingGroupRequestRequestTypeDef",
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
PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
    },
)
ListAssetsRequestRequestTypeDef = TypedDict(
    "ListAssetsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "PackagingGroupId": NotRequired[str],
    },
)
ListPackagingConfigurationsRequestRequestTypeDef = TypedDict(
    "ListPackagingConfigurationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "PackagingGroupId": NotRequired[str],
    },
)
ListPackagingGroupsRequestRequestTypeDef = TypedDict(
    "ListPackagingGroupsRequestRequestTypeDef",
    {
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
UpdatePackagingGroupRequestRequestTypeDef = TypedDict(
    "UpdatePackagingGroupRequestRequestTypeDef",
    {
        "Id": str,
        "Authorization": NotRequired[AuthorizationTypeDef],
    },
)
ConfigureLogsRequestRequestTypeDef = TypedDict(
    "ConfigureLogsRequestRequestTypeDef",
    {
        "Id": str,
        "EgressAccessLogs": NotRequired[EgressAccessLogsTypeDef],
    },
)
CreatePackagingGroupRequestRequestTypeDef = TypedDict(
    "CreatePackagingGroupRequestRequestTypeDef",
    {
        "Id": str,
        "Authorization": NotRequired[AuthorizationTypeDef],
        "EgressAccessLogs": NotRequired[EgressAccessLogsTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
PackagingGroupTypeDef = TypedDict(
    "PackagingGroupTypeDef",
    {
        "ApproximateAssetCount": NotRequired[int],
        "Arn": NotRequired[str],
        "Authorization": NotRequired[AuthorizationTypeDef],
        "CreatedAt": NotRequired[str],
        "DomainName": NotRequired[str],
        "EgressAccessLogs": NotRequired[EgressAccessLogsTypeDef],
        "Id": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)
ConfigureLogsResponseTypeDef = TypedDict(
    "ConfigureLogsResponseTypeDef",
    {
        "Arn": str,
        "Authorization": AuthorizationTypeDef,
        "CreatedAt": str,
        "DomainName": str,
        "EgressAccessLogs": EgressAccessLogsTypeDef,
        "Id": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePackagingGroupResponseTypeDef = TypedDict(
    "CreatePackagingGroupResponseTypeDef",
    {
        "Arn": str,
        "Authorization": AuthorizationTypeDef,
        "CreatedAt": str,
        "DomainName": str,
        "EgressAccessLogs": EgressAccessLogsTypeDef,
        "Id": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePackagingGroupResponseTypeDef = TypedDict(
    "DescribePackagingGroupResponseTypeDef",
    {
        "ApproximateAssetCount": int,
        "Arn": str,
        "Authorization": AuthorizationTypeDef,
        "CreatedAt": str,
        "DomainName": str,
        "EgressAccessLogs": EgressAccessLogsTypeDef,
        "Id": str,
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
ListAssetsResponseTypeDef = TypedDict(
    "ListAssetsResponseTypeDef",
    {
        "Assets": List[AssetShallowTypeDef],
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
UpdatePackagingGroupResponseTypeDef = TypedDict(
    "UpdatePackagingGroupResponseTypeDef",
    {
        "ApproximateAssetCount": int,
        "Arn": str,
        "Authorization": AuthorizationTypeDef,
        "CreatedAt": str,
        "DomainName": str,
        "EgressAccessLogs": EgressAccessLogsTypeDef,
        "Id": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAssetResponseTypeDef = TypedDict(
    "CreateAssetResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "EgressEndpoints": List[EgressEndpointTypeDef],
        "Id": str,
        "PackagingGroupId": str,
        "ResourceId": str,
        "SourceArn": str,
        "SourceRoleArn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAssetResponseTypeDef = TypedDict(
    "DescribeAssetResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "EgressEndpoints": List[EgressEndpointTypeDef],
        "Id": str,
        "PackagingGroupId": str,
        "ResourceId": str,
        "SourceArn": str,
        "SourceRoleArn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DashManifestTypeDef = TypedDict(
    "DashManifestTypeDef",
    {
        "ManifestLayout": NotRequired[ManifestLayoutType],
        "ManifestName": NotRequired[str],
        "MinBufferTimeSeconds": NotRequired[int],
        "Profile": NotRequired[ProfileType],
        "ScteMarkersSource": NotRequired[ScteMarkersSourceType],
        "StreamSelection": NotRequired[StreamSelectionTypeDef],
    },
)
HlsManifestTypeDef = TypedDict(
    "HlsManifestTypeDef",
    {
        "AdMarkers": NotRequired[AdMarkersType],
        "IncludeIframeOnlyStream": NotRequired[bool],
        "ManifestName": NotRequired[str],
        "ProgramDateTimeIntervalSeconds": NotRequired[int],
        "RepeatExtXKey": NotRequired[bool],
        "StreamSelection": NotRequired[StreamSelectionTypeDef],
    },
)
MssManifestTypeDef = TypedDict(
    "MssManifestTypeDef",
    {
        "ManifestName": NotRequired[str],
        "StreamSelection": NotRequired[StreamSelectionTypeDef],
    },
)
SpekeKeyProviderOutputTypeDef = TypedDict(
    "SpekeKeyProviderOutputTypeDef",
    {
        "RoleArn": str,
        "SystemIds": List[str],
        "Url": str,
        "EncryptionContractConfiguration": NotRequired[EncryptionContractConfigurationTypeDef],
    },
)
SpekeKeyProviderTypeDef = TypedDict(
    "SpekeKeyProviderTypeDef",
    {
        "RoleArn": str,
        "SystemIds": Sequence[str],
        "Url": str,
        "EncryptionContractConfiguration": NotRequired[EncryptionContractConfigurationTypeDef],
    },
)
ListAssetsRequestListAssetsPaginateTypeDef = TypedDict(
    "ListAssetsRequestListAssetsPaginateTypeDef",
    {
        "PackagingGroupId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPackagingConfigurationsRequestListPackagingConfigurationsPaginateTypeDef = TypedDict(
    "ListPackagingConfigurationsRequestListPackagingConfigurationsPaginateTypeDef",
    {
        "PackagingGroupId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPackagingGroupsRequestListPackagingGroupsPaginateTypeDef = TypedDict(
    "ListPackagingGroupsRequestListPackagingGroupsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPackagingGroupsResponseTypeDef = TypedDict(
    "ListPackagingGroupsResponseTypeDef",
    {
        "PackagingGroups": List[PackagingGroupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CmafEncryptionOutputTypeDef = TypedDict(
    "CmafEncryptionOutputTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderOutputTypeDef,
        "ConstantInitializationVector": NotRequired[str],
    },
)
DashEncryptionOutputTypeDef = TypedDict(
    "DashEncryptionOutputTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderOutputTypeDef,
    },
)
HlsEncryptionOutputTypeDef = TypedDict(
    "HlsEncryptionOutputTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderOutputTypeDef,
        "ConstantInitializationVector": NotRequired[str],
        "EncryptionMethod": NotRequired[EncryptionMethodType],
    },
)
MssEncryptionOutputTypeDef = TypedDict(
    "MssEncryptionOutputTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderOutputTypeDef,
    },
)
SpekeKeyProviderUnionTypeDef = Union[SpekeKeyProviderTypeDef, SpekeKeyProviderOutputTypeDef]
CmafPackageOutputTypeDef = TypedDict(
    "CmafPackageOutputTypeDef",
    {
        "HlsManifests": List[HlsManifestTypeDef],
        "Encryption": NotRequired[CmafEncryptionOutputTypeDef],
        "IncludeEncoderConfigurationInSegments": NotRequired[bool],
        "SegmentDurationSeconds": NotRequired[int],
    },
)
DashPackageOutputTypeDef = TypedDict(
    "DashPackageOutputTypeDef",
    {
        "DashManifests": List[DashManifestTypeDef],
        "Encryption": NotRequired[DashEncryptionOutputTypeDef],
        "IncludeEncoderConfigurationInSegments": NotRequired[bool],
        "IncludeIframeOnlyStream": NotRequired[bool],
        "PeriodTriggers": NotRequired[List[Literal["ADS"]]],
        "SegmentDurationSeconds": NotRequired[int],
        "SegmentTemplateFormat": NotRequired[SegmentTemplateFormatType],
    },
)
HlsPackageOutputTypeDef = TypedDict(
    "HlsPackageOutputTypeDef",
    {
        "HlsManifests": List[HlsManifestTypeDef],
        "Encryption": NotRequired[HlsEncryptionOutputTypeDef],
        "IncludeDvbSubtitles": NotRequired[bool],
        "SegmentDurationSeconds": NotRequired[int],
        "UseAudioRenditionGroup": NotRequired[bool],
    },
)
MssPackageOutputTypeDef = TypedDict(
    "MssPackageOutputTypeDef",
    {
        "MssManifests": List[MssManifestTypeDef],
        "Encryption": NotRequired[MssEncryptionOutputTypeDef],
        "SegmentDurationSeconds": NotRequired[int],
    },
)
CmafEncryptionTypeDef = TypedDict(
    "CmafEncryptionTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderUnionTypeDef,
        "ConstantInitializationVector": NotRequired[str],
    },
)
DashEncryptionTypeDef = TypedDict(
    "DashEncryptionTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderUnionTypeDef,
    },
)
HlsEncryptionTypeDef = TypedDict(
    "HlsEncryptionTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderUnionTypeDef,
        "ConstantInitializationVector": NotRequired[str],
        "EncryptionMethod": NotRequired[EncryptionMethodType],
    },
)
MssEncryptionTypeDef = TypedDict(
    "MssEncryptionTypeDef",
    {
        "SpekeKeyProvider": SpekeKeyProviderUnionTypeDef,
    },
)
CreatePackagingConfigurationResponseTypeDef = TypedDict(
    "CreatePackagingConfigurationResponseTypeDef",
    {
        "Arn": str,
        "CmafPackage": CmafPackageOutputTypeDef,
        "CreatedAt": str,
        "DashPackage": DashPackageOutputTypeDef,
        "HlsPackage": HlsPackageOutputTypeDef,
        "Id": str,
        "MssPackage": MssPackageOutputTypeDef,
        "PackagingGroupId": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePackagingConfigurationResponseTypeDef = TypedDict(
    "DescribePackagingConfigurationResponseTypeDef",
    {
        "Arn": str,
        "CmafPackage": CmafPackageOutputTypeDef,
        "CreatedAt": str,
        "DashPackage": DashPackageOutputTypeDef,
        "HlsPackage": HlsPackageOutputTypeDef,
        "Id": str,
        "MssPackage": MssPackageOutputTypeDef,
        "PackagingGroupId": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PackagingConfigurationTypeDef = TypedDict(
    "PackagingConfigurationTypeDef",
    {
        "Arn": NotRequired[str],
        "CmafPackage": NotRequired[CmafPackageOutputTypeDef],
        "CreatedAt": NotRequired[str],
        "DashPackage": NotRequired[DashPackageOutputTypeDef],
        "HlsPackage": NotRequired[HlsPackageOutputTypeDef],
        "Id": NotRequired[str],
        "MssPackage": NotRequired[MssPackageOutputTypeDef],
        "PackagingGroupId": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)
CmafEncryptionUnionTypeDef = Union[CmafEncryptionTypeDef, CmafEncryptionOutputTypeDef]
DashEncryptionUnionTypeDef = Union[DashEncryptionTypeDef, DashEncryptionOutputTypeDef]
HlsEncryptionUnionTypeDef = Union[HlsEncryptionTypeDef, HlsEncryptionOutputTypeDef]
MssEncryptionUnionTypeDef = Union[MssEncryptionTypeDef, MssEncryptionOutputTypeDef]
ListPackagingConfigurationsResponseTypeDef = TypedDict(
    "ListPackagingConfigurationsResponseTypeDef",
    {
        "PackagingConfigurations": List[PackagingConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CmafPackageTypeDef = TypedDict(
    "CmafPackageTypeDef",
    {
        "HlsManifests": Sequence[HlsManifestTypeDef],
        "Encryption": NotRequired[CmafEncryptionUnionTypeDef],
        "IncludeEncoderConfigurationInSegments": NotRequired[bool],
        "SegmentDurationSeconds": NotRequired[int],
    },
)
DashPackageTypeDef = TypedDict(
    "DashPackageTypeDef",
    {
        "DashManifests": Sequence[DashManifestTypeDef],
        "Encryption": NotRequired[DashEncryptionUnionTypeDef],
        "IncludeEncoderConfigurationInSegments": NotRequired[bool],
        "IncludeIframeOnlyStream": NotRequired[bool],
        "PeriodTriggers": NotRequired[Sequence[Literal["ADS"]]],
        "SegmentDurationSeconds": NotRequired[int],
        "SegmentTemplateFormat": NotRequired[SegmentTemplateFormatType],
    },
)
HlsPackageTypeDef = TypedDict(
    "HlsPackageTypeDef",
    {
        "HlsManifests": Sequence[HlsManifestTypeDef],
        "Encryption": NotRequired[HlsEncryptionUnionTypeDef],
        "IncludeDvbSubtitles": NotRequired[bool],
        "SegmentDurationSeconds": NotRequired[int],
        "UseAudioRenditionGroup": NotRequired[bool],
    },
)
MssPackageTypeDef = TypedDict(
    "MssPackageTypeDef",
    {
        "MssManifests": Sequence[MssManifestTypeDef],
        "Encryption": NotRequired[MssEncryptionUnionTypeDef],
        "SegmentDurationSeconds": NotRequired[int],
    },
)
CreatePackagingConfigurationRequestRequestTypeDef = TypedDict(
    "CreatePackagingConfigurationRequestRequestTypeDef",
    {
        "Id": str,
        "PackagingGroupId": str,
        "CmafPackage": NotRequired[CmafPackageTypeDef],
        "DashPackage": NotRequired[DashPackageTypeDef],
        "HlsPackage": NotRequired[HlsPackageTypeDef],
        "MssPackage": NotRequired[MssPackageTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
