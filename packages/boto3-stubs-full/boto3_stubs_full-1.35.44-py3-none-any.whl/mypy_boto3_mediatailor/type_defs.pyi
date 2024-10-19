"""
Type annotations for mediatailor service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/type_defs/)

Usage::

    ```python
    from mypy_boto3_mediatailor.type_defs import SecretsManagerAccessTokenConfigurationTypeDef

    data: SecretsManagerAccessTokenConfigurationTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AccessTypeType,
    AdMarkupTypeType,
    AlertCategoryType,
    ChannelStateType,
    FillPolicyType,
    InsertionModeType,
    MessageTypeType,
    ModeType,
    OriginManifestTypeType,
    PlaybackModeType,
    RelativePositionType,
    ScheduleEntryTypeType,
    TierType,
    TypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "SecretsManagerAccessTokenConfigurationTypeDef",
    "AdBreakOpportunityTypeDef",
    "KeyValuePairTypeDef",
    "SlateSourceTypeDef",
    "SpliceInsertMessageTypeDef",
    "AdMarkerPassthroughTypeDef",
    "AlertTypeDef",
    "ClipRangeTypeDef",
    "AvailMatchingCriteriaTypeDef",
    "AvailSuppressionTypeDef",
    "BumperTypeDef",
    "CdnConfigurationTypeDef",
    "LogConfigurationForChannelTypeDef",
    "ConfigureLogsForChannelRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "ConfigureLogsForPlaybackConfigurationRequestRequestTypeDef",
    "TimeShiftConfigurationTypeDef",
    "HttpPackageConfigurationTypeDef",
    "PrefetchRetrievalOutputTypeDef",
    "DefaultSegmentDeliveryConfigurationTypeDef",
    "HttpConfigurationTypeDef",
    "SegmentDeliveryConfigurationTypeDef",
    "DashConfigurationForPutTypeDef",
    "DashConfigurationTypeDef",
    "DashPlaylistSettingsTypeDef",
    "DeleteChannelPolicyRequestRequestTypeDef",
    "DeleteChannelRequestRequestTypeDef",
    "DeleteLiveSourceRequestRequestTypeDef",
    "DeletePlaybackConfigurationRequestRequestTypeDef",
    "DeletePrefetchScheduleRequestRequestTypeDef",
    "DeleteProgramRequestRequestTypeDef",
    "DeleteSourceLocationRequestRequestTypeDef",
    "DeleteVodSourceRequestRequestTypeDef",
    "DescribeChannelRequestRequestTypeDef",
    "DescribeLiveSourceRequestRequestTypeDef",
    "DescribeProgramRequestRequestTypeDef",
    "DescribeSourceLocationRequestRequestTypeDef",
    "DescribeVodSourceRequestRequestTypeDef",
    "GetChannelPolicyRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "GetChannelScheduleRequestRequestTypeDef",
    "GetPlaybackConfigurationRequestRequestTypeDef",
    "HlsConfigurationTypeDef",
    "LivePreRollConfigurationTypeDef",
    "LogConfigurationTypeDef",
    "GetPrefetchScheduleRequestRequestTypeDef",
    "HlsPlaylistSettingsOutputTypeDef",
    "HlsPlaylistSettingsTypeDef",
    "ListAlertsRequestRequestTypeDef",
    "ListChannelsRequestRequestTypeDef",
    "ListLiveSourcesRequestRequestTypeDef",
    "ListPlaybackConfigurationsRequestRequestTypeDef",
    "ListPrefetchSchedulesRequestRequestTypeDef",
    "ListSourceLocationsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListVodSourcesRequestRequestTypeDef",
    "TimestampTypeDef",
    "PutChannelPolicyRequestRequestTypeDef",
    "ScheduleAdBreakTypeDef",
    "TransitionTypeDef",
    "SegmentationDescriptorTypeDef",
    "StartChannelRequestRequestTypeDef",
    "StopChannelRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateProgramTransitionTypeDef",
    "AccessConfigurationTypeDef",
    "ManifestProcessingRulesTypeDef",
    "PrefetchConsumptionOutputTypeDef",
    "ConfigureLogsForChannelResponseTypeDef",
    "ConfigureLogsForPlaybackConfigurationResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetChannelPolicyResponseTypeDef",
    "ListAlertsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "CreateLiveSourceRequestRequestTypeDef",
    "CreateLiveSourceResponseTypeDef",
    "CreateVodSourceRequestRequestTypeDef",
    "CreateVodSourceResponseTypeDef",
    "DescribeLiveSourceResponseTypeDef",
    "DescribeVodSourceResponseTypeDef",
    "LiveSourceTypeDef",
    "UpdateLiveSourceRequestRequestTypeDef",
    "UpdateLiveSourceResponseTypeDef",
    "UpdateVodSourceRequestRequestTypeDef",
    "UpdateVodSourceResponseTypeDef",
    "VodSourceTypeDef",
    "GetChannelScheduleRequestGetChannelSchedulePaginateTypeDef",
    "ListAlertsRequestListAlertsPaginateTypeDef",
    "ListChannelsRequestListChannelsPaginateTypeDef",
    "ListLiveSourcesRequestListLiveSourcesPaginateTypeDef",
    "ListPlaybackConfigurationsRequestListPlaybackConfigurationsPaginateTypeDef",
    "ListPrefetchSchedulesRequestListPrefetchSchedulesPaginateTypeDef",
    "ListSourceLocationsRequestListSourceLocationsPaginateTypeDef",
    "ListVodSourcesRequestListVodSourcesPaginateTypeDef",
    "ResponseOutputItemTypeDef",
    "HlsPlaylistSettingsUnionTypeDef",
    "PrefetchConsumptionTypeDef",
    "PrefetchRetrievalTypeDef",
    "ScheduleEntryTypeDef",
    "ScheduleConfigurationTypeDef",
    "TimeSignalMessageOutputTypeDef",
    "TimeSignalMessageTypeDef",
    "UpdateProgramScheduleConfigurationTypeDef",
    "CreateSourceLocationRequestRequestTypeDef",
    "CreateSourceLocationResponseTypeDef",
    "DescribeSourceLocationResponseTypeDef",
    "SourceLocationTypeDef",
    "UpdateSourceLocationRequestRequestTypeDef",
    "UpdateSourceLocationResponseTypeDef",
    "GetPlaybackConfigurationResponseTypeDef",
    "PlaybackConfigurationTypeDef",
    "PutPlaybackConfigurationRequestRequestTypeDef",
    "PutPlaybackConfigurationResponseTypeDef",
    "CreatePrefetchScheduleResponseTypeDef",
    "GetPrefetchScheduleResponseTypeDef",
    "PrefetchScheduleTypeDef",
    "ListLiveSourcesResponseTypeDef",
    "ListVodSourcesResponseTypeDef",
    "ChannelTypeDef",
    "CreateChannelResponseTypeDef",
    "DescribeChannelResponseTypeDef",
    "UpdateChannelResponseTypeDef",
    "RequestOutputItemTypeDef",
    "CreatePrefetchScheduleRequestRequestTypeDef",
    "GetChannelScheduleResponseTypeDef",
    "AdBreakOutputTypeDef",
    "TimeSignalMessageUnionTypeDef",
    "ListSourceLocationsResponseTypeDef",
    "ListPlaybackConfigurationsResponseTypeDef",
    "ListPrefetchSchedulesResponseTypeDef",
    "ListChannelsResponseTypeDef",
    "CreateChannelRequestRequestTypeDef",
    "UpdateChannelRequestRequestTypeDef",
    "AlternateMediaOutputTypeDef",
    "AdBreakTypeDef",
    "AudienceMediaOutputTypeDef",
    "AdBreakUnionTypeDef",
    "CreateProgramResponseTypeDef",
    "DescribeProgramResponseTypeDef",
    "UpdateProgramResponseTypeDef",
    "AlternateMediaTypeDef",
    "AlternateMediaUnionTypeDef",
    "AudienceMediaTypeDef",
    "AudienceMediaUnionTypeDef",
    "UpdateProgramRequestRequestTypeDef",
    "CreateProgramRequestRequestTypeDef",
)

SecretsManagerAccessTokenConfigurationTypeDef = TypedDict(
    "SecretsManagerAccessTokenConfigurationTypeDef",
    {
        "HeaderName": NotRequired[str],
        "SecretArn": NotRequired[str],
        "SecretStringKey": NotRequired[str],
    },
)
AdBreakOpportunityTypeDef = TypedDict(
    "AdBreakOpportunityTypeDef",
    {
        "OffsetMillis": int,
    },
)
KeyValuePairTypeDef = TypedDict(
    "KeyValuePairTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
SlateSourceTypeDef = TypedDict(
    "SlateSourceTypeDef",
    {
        "SourceLocationName": NotRequired[str],
        "VodSourceName": NotRequired[str],
    },
)
SpliceInsertMessageTypeDef = TypedDict(
    "SpliceInsertMessageTypeDef",
    {
        "AvailNum": NotRequired[int],
        "AvailsExpected": NotRequired[int],
        "SpliceEventId": NotRequired[int],
        "UniqueProgramId": NotRequired[int],
    },
)
AdMarkerPassthroughTypeDef = TypedDict(
    "AdMarkerPassthroughTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)
AlertTypeDef = TypedDict(
    "AlertTypeDef",
    {
        "AlertCode": str,
        "AlertMessage": str,
        "LastModifiedTime": datetime,
        "RelatedResourceArns": List[str],
        "ResourceArn": str,
        "Category": NotRequired[AlertCategoryType],
    },
)
ClipRangeTypeDef = TypedDict(
    "ClipRangeTypeDef",
    {
        "EndOffsetMillis": NotRequired[int],
        "StartOffsetMillis": NotRequired[int],
    },
)
AvailMatchingCriteriaTypeDef = TypedDict(
    "AvailMatchingCriteriaTypeDef",
    {
        "DynamicVariable": str,
        "Operator": Literal["EQUALS"],
    },
)
AvailSuppressionTypeDef = TypedDict(
    "AvailSuppressionTypeDef",
    {
        "FillPolicy": NotRequired[FillPolicyType],
        "Mode": NotRequired[ModeType],
        "Value": NotRequired[str],
    },
)
BumperTypeDef = TypedDict(
    "BumperTypeDef",
    {
        "EndUrl": NotRequired[str],
        "StartUrl": NotRequired[str],
    },
)
CdnConfigurationTypeDef = TypedDict(
    "CdnConfigurationTypeDef",
    {
        "AdSegmentUrlPrefix": NotRequired[str],
        "ContentSegmentUrlPrefix": NotRequired[str],
    },
)
LogConfigurationForChannelTypeDef = TypedDict(
    "LogConfigurationForChannelTypeDef",
    {
        "LogTypes": NotRequired[List[Literal["AS_RUN"]]],
    },
)
ConfigureLogsForChannelRequestRequestTypeDef = TypedDict(
    "ConfigureLogsForChannelRequestRequestTypeDef",
    {
        "ChannelName": str,
        "LogTypes": Sequence[Literal["AS_RUN"]],
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
ConfigureLogsForPlaybackConfigurationRequestRequestTypeDef = TypedDict(
    "ConfigureLogsForPlaybackConfigurationRequestRequestTypeDef",
    {
        "PercentEnabled": int,
        "PlaybackConfigurationName": str,
    },
)
TimeShiftConfigurationTypeDef = TypedDict(
    "TimeShiftConfigurationTypeDef",
    {
        "MaxTimeDelaySeconds": int,
    },
)
HttpPackageConfigurationTypeDef = TypedDict(
    "HttpPackageConfigurationTypeDef",
    {
        "Path": str,
        "SourceGroup": str,
        "Type": TypeType,
    },
)
PrefetchRetrievalOutputTypeDef = TypedDict(
    "PrefetchRetrievalOutputTypeDef",
    {
        "EndTime": datetime,
        "DynamicVariables": NotRequired[Dict[str, str]],
        "StartTime": NotRequired[datetime],
    },
)
DefaultSegmentDeliveryConfigurationTypeDef = TypedDict(
    "DefaultSegmentDeliveryConfigurationTypeDef",
    {
        "BaseUrl": NotRequired[str],
    },
)
HttpConfigurationTypeDef = TypedDict(
    "HttpConfigurationTypeDef",
    {
        "BaseUrl": str,
    },
)
SegmentDeliveryConfigurationTypeDef = TypedDict(
    "SegmentDeliveryConfigurationTypeDef",
    {
        "BaseUrl": NotRequired[str],
        "Name": NotRequired[str],
    },
)
DashConfigurationForPutTypeDef = TypedDict(
    "DashConfigurationForPutTypeDef",
    {
        "MpdLocation": NotRequired[str],
        "OriginManifestType": NotRequired[OriginManifestTypeType],
    },
)
DashConfigurationTypeDef = TypedDict(
    "DashConfigurationTypeDef",
    {
        "ManifestEndpointPrefix": NotRequired[str],
        "MpdLocation": NotRequired[str],
        "OriginManifestType": NotRequired[OriginManifestTypeType],
    },
)
DashPlaylistSettingsTypeDef = TypedDict(
    "DashPlaylistSettingsTypeDef",
    {
        "ManifestWindowSeconds": NotRequired[int],
        "MinBufferTimeSeconds": NotRequired[int],
        "MinUpdatePeriodSeconds": NotRequired[int],
        "SuggestedPresentationDelaySeconds": NotRequired[int],
    },
)
DeleteChannelPolicyRequestRequestTypeDef = TypedDict(
    "DeleteChannelPolicyRequestRequestTypeDef",
    {
        "ChannelName": str,
    },
)
DeleteChannelRequestRequestTypeDef = TypedDict(
    "DeleteChannelRequestRequestTypeDef",
    {
        "ChannelName": str,
    },
)
DeleteLiveSourceRequestRequestTypeDef = TypedDict(
    "DeleteLiveSourceRequestRequestTypeDef",
    {
        "LiveSourceName": str,
        "SourceLocationName": str,
    },
)
DeletePlaybackConfigurationRequestRequestTypeDef = TypedDict(
    "DeletePlaybackConfigurationRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeletePrefetchScheduleRequestRequestTypeDef = TypedDict(
    "DeletePrefetchScheduleRequestRequestTypeDef",
    {
        "Name": str,
        "PlaybackConfigurationName": str,
    },
)
DeleteProgramRequestRequestTypeDef = TypedDict(
    "DeleteProgramRequestRequestTypeDef",
    {
        "ChannelName": str,
        "ProgramName": str,
    },
)
DeleteSourceLocationRequestRequestTypeDef = TypedDict(
    "DeleteSourceLocationRequestRequestTypeDef",
    {
        "SourceLocationName": str,
    },
)
DeleteVodSourceRequestRequestTypeDef = TypedDict(
    "DeleteVodSourceRequestRequestTypeDef",
    {
        "SourceLocationName": str,
        "VodSourceName": str,
    },
)
DescribeChannelRequestRequestTypeDef = TypedDict(
    "DescribeChannelRequestRequestTypeDef",
    {
        "ChannelName": str,
    },
)
DescribeLiveSourceRequestRequestTypeDef = TypedDict(
    "DescribeLiveSourceRequestRequestTypeDef",
    {
        "LiveSourceName": str,
        "SourceLocationName": str,
    },
)
DescribeProgramRequestRequestTypeDef = TypedDict(
    "DescribeProgramRequestRequestTypeDef",
    {
        "ChannelName": str,
        "ProgramName": str,
    },
)
DescribeSourceLocationRequestRequestTypeDef = TypedDict(
    "DescribeSourceLocationRequestRequestTypeDef",
    {
        "SourceLocationName": str,
    },
)
DescribeVodSourceRequestRequestTypeDef = TypedDict(
    "DescribeVodSourceRequestRequestTypeDef",
    {
        "SourceLocationName": str,
        "VodSourceName": str,
    },
)
GetChannelPolicyRequestRequestTypeDef = TypedDict(
    "GetChannelPolicyRequestRequestTypeDef",
    {
        "ChannelName": str,
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
GetChannelScheduleRequestRequestTypeDef = TypedDict(
    "GetChannelScheduleRequestRequestTypeDef",
    {
        "ChannelName": str,
        "Audience": NotRequired[str],
        "DurationMinutes": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetPlaybackConfigurationRequestRequestTypeDef = TypedDict(
    "GetPlaybackConfigurationRequestRequestTypeDef",
    {
        "Name": str,
    },
)
HlsConfigurationTypeDef = TypedDict(
    "HlsConfigurationTypeDef",
    {
        "ManifestEndpointPrefix": NotRequired[str],
    },
)
LivePreRollConfigurationTypeDef = TypedDict(
    "LivePreRollConfigurationTypeDef",
    {
        "AdDecisionServerUrl": NotRequired[str],
        "MaxDurationSeconds": NotRequired[int],
    },
)
LogConfigurationTypeDef = TypedDict(
    "LogConfigurationTypeDef",
    {
        "PercentEnabled": int,
    },
)
GetPrefetchScheduleRequestRequestTypeDef = TypedDict(
    "GetPrefetchScheduleRequestRequestTypeDef",
    {
        "Name": str,
        "PlaybackConfigurationName": str,
    },
)
HlsPlaylistSettingsOutputTypeDef = TypedDict(
    "HlsPlaylistSettingsOutputTypeDef",
    {
        "AdMarkupType": NotRequired[List[AdMarkupTypeType]],
        "ManifestWindowSeconds": NotRequired[int],
    },
)
HlsPlaylistSettingsTypeDef = TypedDict(
    "HlsPlaylistSettingsTypeDef",
    {
        "AdMarkupType": NotRequired[Sequence[AdMarkupTypeType]],
        "ManifestWindowSeconds": NotRequired[int],
    },
)
ListAlertsRequestRequestTypeDef = TypedDict(
    "ListAlertsRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListChannelsRequestRequestTypeDef = TypedDict(
    "ListChannelsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListLiveSourcesRequestRequestTypeDef = TypedDict(
    "ListLiveSourcesRequestRequestTypeDef",
    {
        "SourceLocationName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListPlaybackConfigurationsRequestRequestTypeDef = TypedDict(
    "ListPlaybackConfigurationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListPrefetchSchedulesRequestRequestTypeDef = TypedDict(
    "ListPrefetchSchedulesRequestRequestTypeDef",
    {
        "PlaybackConfigurationName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "StreamId": NotRequired[str],
    },
)
ListSourceLocationsRequestRequestTypeDef = TypedDict(
    "ListSourceLocationsRequestRequestTypeDef",
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
ListVodSourcesRequestRequestTypeDef = TypedDict(
    "ListVodSourcesRequestRequestTypeDef",
    {
        "SourceLocationName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
PutChannelPolicyRequestRequestTypeDef = TypedDict(
    "PutChannelPolicyRequestRequestTypeDef",
    {
        "ChannelName": str,
        "Policy": str,
    },
)
ScheduleAdBreakTypeDef = TypedDict(
    "ScheduleAdBreakTypeDef",
    {
        "ApproximateDurationSeconds": NotRequired[int],
        "ApproximateStartTime": NotRequired[datetime],
        "SourceLocationName": NotRequired[str],
        "VodSourceName": NotRequired[str],
    },
)
TransitionTypeDef = TypedDict(
    "TransitionTypeDef",
    {
        "RelativePosition": RelativePositionType,
        "Type": str,
        "DurationMillis": NotRequired[int],
        "RelativeProgram": NotRequired[str],
        "ScheduledStartTimeMillis": NotRequired[int],
    },
)
SegmentationDescriptorTypeDef = TypedDict(
    "SegmentationDescriptorTypeDef",
    {
        "SegmentNum": NotRequired[int],
        "SegmentationEventId": NotRequired[int],
        "SegmentationTypeId": NotRequired[int],
        "SegmentationUpid": NotRequired[str],
        "SegmentationUpidType": NotRequired[int],
        "SegmentsExpected": NotRequired[int],
        "SubSegmentNum": NotRequired[int],
        "SubSegmentsExpected": NotRequired[int],
    },
)
StartChannelRequestRequestTypeDef = TypedDict(
    "StartChannelRequestRequestTypeDef",
    {
        "ChannelName": str,
    },
)
StopChannelRequestRequestTypeDef = TypedDict(
    "StopChannelRequestRequestTypeDef",
    {
        "ChannelName": str,
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
UpdateProgramTransitionTypeDef = TypedDict(
    "UpdateProgramTransitionTypeDef",
    {
        "DurationMillis": NotRequired[int],
        "ScheduledStartTimeMillis": NotRequired[int],
    },
)
AccessConfigurationTypeDef = TypedDict(
    "AccessConfigurationTypeDef",
    {
        "AccessType": NotRequired[AccessTypeType],
        "SecretsManagerAccessTokenConfiguration": NotRequired[
            SecretsManagerAccessTokenConfigurationTypeDef
        ],
    },
)
ManifestProcessingRulesTypeDef = TypedDict(
    "ManifestProcessingRulesTypeDef",
    {
        "AdMarkerPassthrough": NotRequired[AdMarkerPassthroughTypeDef],
    },
)
PrefetchConsumptionOutputTypeDef = TypedDict(
    "PrefetchConsumptionOutputTypeDef",
    {
        "EndTime": datetime,
        "AvailMatchingCriteria": NotRequired[List[AvailMatchingCriteriaTypeDef]],
        "StartTime": NotRequired[datetime],
    },
)
ConfigureLogsForChannelResponseTypeDef = TypedDict(
    "ConfigureLogsForChannelResponseTypeDef",
    {
        "ChannelName": str,
        "LogTypes": List[Literal["AS_RUN"]],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConfigureLogsForPlaybackConfigurationResponseTypeDef = TypedDict(
    "ConfigureLogsForPlaybackConfigurationResponseTypeDef",
    {
        "PercentEnabled": int,
        "PlaybackConfigurationName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetChannelPolicyResponseTypeDef = TypedDict(
    "GetChannelPolicyResponseTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAlertsResponseTypeDef = TypedDict(
    "ListAlertsResponseTypeDef",
    {
        "Items": List[AlertTypeDef],
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
CreateLiveSourceRequestRequestTypeDef = TypedDict(
    "CreateLiveSourceRequestRequestTypeDef",
    {
        "HttpPackageConfigurations": Sequence[HttpPackageConfigurationTypeDef],
        "LiveSourceName": str,
        "SourceLocationName": str,
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CreateLiveSourceResponseTypeDef = TypedDict(
    "CreateLiveSourceResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "HttpPackageConfigurations": List[HttpPackageConfigurationTypeDef],
        "LastModifiedTime": datetime,
        "LiveSourceName": str,
        "SourceLocationName": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateVodSourceRequestRequestTypeDef = TypedDict(
    "CreateVodSourceRequestRequestTypeDef",
    {
        "HttpPackageConfigurations": Sequence[HttpPackageConfigurationTypeDef],
        "SourceLocationName": str,
        "VodSourceName": str,
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CreateVodSourceResponseTypeDef = TypedDict(
    "CreateVodSourceResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "HttpPackageConfigurations": List[HttpPackageConfigurationTypeDef],
        "LastModifiedTime": datetime,
        "SourceLocationName": str,
        "Tags": Dict[str, str],
        "VodSourceName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeLiveSourceResponseTypeDef = TypedDict(
    "DescribeLiveSourceResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "HttpPackageConfigurations": List[HttpPackageConfigurationTypeDef],
        "LastModifiedTime": datetime,
        "LiveSourceName": str,
        "SourceLocationName": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeVodSourceResponseTypeDef = TypedDict(
    "DescribeVodSourceResponseTypeDef",
    {
        "AdBreakOpportunities": List[AdBreakOpportunityTypeDef],
        "Arn": str,
        "CreationTime": datetime,
        "HttpPackageConfigurations": List[HttpPackageConfigurationTypeDef],
        "LastModifiedTime": datetime,
        "SourceLocationName": str,
        "Tags": Dict[str, str],
        "VodSourceName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LiveSourceTypeDef = TypedDict(
    "LiveSourceTypeDef",
    {
        "Arn": str,
        "HttpPackageConfigurations": List[HttpPackageConfigurationTypeDef],
        "LiveSourceName": str,
        "SourceLocationName": str,
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
        "Tags": NotRequired[Dict[str, str]],
    },
)
UpdateLiveSourceRequestRequestTypeDef = TypedDict(
    "UpdateLiveSourceRequestRequestTypeDef",
    {
        "HttpPackageConfigurations": Sequence[HttpPackageConfigurationTypeDef],
        "LiveSourceName": str,
        "SourceLocationName": str,
    },
)
UpdateLiveSourceResponseTypeDef = TypedDict(
    "UpdateLiveSourceResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "HttpPackageConfigurations": List[HttpPackageConfigurationTypeDef],
        "LastModifiedTime": datetime,
        "LiveSourceName": str,
        "SourceLocationName": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateVodSourceRequestRequestTypeDef = TypedDict(
    "UpdateVodSourceRequestRequestTypeDef",
    {
        "HttpPackageConfigurations": Sequence[HttpPackageConfigurationTypeDef],
        "SourceLocationName": str,
        "VodSourceName": str,
    },
)
UpdateVodSourceResponseTypeDef = TypedDict(
    "UpdateVodSourceResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "HttpPackageConfigurations": List[HttpPackageConfigurationTypeDef],
        "LastModifiedTime": datetime,
        "SourceLocationName": str,
        "Tags": Dict[str, str],
        "VodSourceName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VodSourceTypeDef = TypedDict(
    "VodSourceTypeDef",
    {
        "Arn": str,
        "HttpPackageConfigurations": List[HttpPackageConfigurationTypeDef],
        "SourceLocationName": str,
        "VodSourceName": str,
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
        "Tags": NotRequired[Dict[str, str]],
    },
)
GetChannelScheduleRequestGetChannelSchedulePaginateTypeDef = TypedDict(
    "GetChannelScheduleRequestGetChannelSchedulePaginateTypeDef",
    {
        "ChannelName": str,
        "Audience": NotRequired[str],
        "DurationMinutes": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAlertsRequestListAlertsPaginateTypeDef = TypedDict(
    "ListAlertsRequestListAlertsPaginateTypeDef",
    {
        "ResourceArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListChannelsRequestListChannelsPaginateTypeDef = TypedDict(
    "ListChannelsRequestListChannelsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListLiveSourcesRequestListLiveSourcesPaginateTypeDef = TypedDict(
    "ListLiveSourcesRequestListLiveSourcesPaginateTypeDef",
    {
        "SourceLocationName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPlaybackConfigurationsRequestListPlaybackConfigurationsPaginateTypeDef = TypedDict(
    "ListPlaybackConfigurationsRequestListPlaybackConfigurationsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPrefetchSchedulesRequestListPrefetchSchedulesPaginateTypeDef = TypedDict(
    "ListPrefetchSchedulesRequestListPrefetchSchedulesPaginateTypeDef",
    {
        "PlaybackConfigurationName": str,
        "StreamId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSourceLocationsRequestListSourceLocationsPaginateTypeDef = TypedDict(
    "ListSourceLocationsRequestListSourceLocationsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListVodSourcesRequestListVodSourcesPaginateTypeDef = TypedDict(
    "ListVodSourcesRequestListVodSourcesPaginateTypeDef",
    {
        "SourceLocationName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ResponseOutputItemTypeDef = TypedDict(
    "ResponseOutputItemTypeDef",
    {
        "ManifestName": str,
        "PlaybackUrl": str,
        "SourceGroup": str,
        "DashPlaylistSettings": NotRequired[DashPlaylistSettingsTypeDef],
        "HlsPlaylistSettings": NotRequired[HlsPlaylistSettingsOutputTypeDef],
    },
)
HlsPlaylistSettingsUnionTypeDef = Union[
    HlsPlaylistSettingsTypeDef, HlsPlaylistSettingsOutputTypeDef
]
PrefetchConsumptionTypeDef = TypedDict(
    "PrefetchConsumptionTypeDef",
    {
        "EndTime": TimestampTypeDef,
        "AvailMatchingCriteria": NotRequired[Sequence[AvailMatchingCriteriaTypeDef]],
        "StartTime": NotRequired[TimestampTypeDef],
    },
)
PrefetchRetrievalTypeDef = TypedDict(
    "PrefetchRetrievalTypeDef",
    {
        "EndTime": TimestampTypeDef,
        "DynamicVariables": NotRequired[Mapping[str, str]],
        "StartTime": NotRequired[TimestampTypeDef],
    },
)
ScheduleEntryTypeDef = TypedDict(
    "ScheduleEntryTypeDef",
    {
        "Arn": str,
        "ChannelName": str,
        "ProgramName": str,
        "SourceLocationName": str,
        "ApproximateDurationSeconds": NotRequired[int],
        "ApproximateStartTime": NotRequired[datetime],
        "Audiences": NotRequired[List[str]],
        "LiveSourceName": NotRequired[str],
        "ScheduleAdBreaks": NotRequired[List[ScheduleAdBreakTypeDef]],
        "ScheduleEntryType": NotRequired[ScheduleEntryTypeType],
        "VodSourceName": NotRequired[str],
    },
)
ScheduleConfigurationTypeDef = TypedDict(
    "ScheduleConfigurationTypeDef",
    {
        "Transition": TransitionTypeDef,
        "ClipRange": NotRequired[ClipRangeTypeDef],
    },
)
TimeSignalMessageOutputTypeDef = TypedDict(
    "TimeSignalMessageOutputTypeDef",
    {
        "SegmentationDescriptors": NotRequired[List[SegmentationDescriptorTypeDef]],
    },
)
TimeSignalMessageTypeDef = TypedDict(
    "TimeSignalMessageTypeDef",
    {
        "SegmentationDescriptors": NotRequired[Sequence[SegmentationDescriptorTypeDef]],
    },
)
UpdateProgramScheduleConfigurationTypeDef = TypedDict(
    "UpdateProgramScheduleConfigurationTypeDef",
    {
        "ClipRange": NotRequired[ClipRangeTypeDef],
        "Transition": NotRequired[UpdateProgramTransitionTypeDef],
    },
)
CreateSourceLocationRequestRequestTypeDef = TypedDict(
    "CreateSourceLocationRequestRequestTypeDef",
    {
        "HttpConfiguration": HttpConfigurationTypeDef,
        "SourceLocationName": str,
        "AccessConfiguration": NotRequired[AccessConfigurationTypeDef],
        "DefaultSegmentDeliveryConfiguration": NotRequired[
            DefaultSegmentDeliveryConfigurationTypeDef
        ],
        "SegmentDeliveryConfigurations": NotRequired[Sequence[SegmentDeliveryConfigurationTypeDef]],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CreateSourceLocationResponseTypeDef = TypedDict(
    "CreateSourceLocationResponseTypeDef",
    {
        "AccessConfiguration": AccessConfigurationTypeDef,
        "Arn": str,
        "CreationTime": datetime,
        "DefaultSegmentDeliveryConfiguration": DefaultSegmentDeliveryConfigurationTypeDef,
        "HttpConfiguration": HttpConfigurationTypeDef,
        "LastModifiedTime": datetime,
        "SegmentDeliveryConfigurations": List[SegmentDeliveryConfigurationTypeDef],
        "SourceLocationName": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSourceLocationResponseTypeDef = TypedDict(
    "DescribeSourceLocationResponseTypeDef",
    {
        "AccessConfiguration": AccessConfigurationTypeDef,
        "Arn": str,
        "CreationTime": datetime,
        "DefaultSegmentDeliveryConfiguration": DefaultSegmentDeliveryConfigurationTypeDef,
        "HttpConfiguration": HttpConfigurationTypeDef,
        "LastModifiedTime": datetime,
        "SegmentDeliveryConfigurations": List[SegmentDeliveryConfigurationTypeDef],
        "SourceLocationName": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SourceLocationTypeDef = TypedDict(
    "SourceLocationTypeDef",
    {
        "Arn": str,
        "HttpConfiguration": HttpConfigurationTypeDef,
        "SourceLocationName": str,
        "AccessConfiguration": NotRequired[AccessConfigurationTypeDef],
        "CreationTime": NotRequired[datetime],
        "DefaultSegmentDeliveryConfiguration": NotRequired[
            DefaultSegmentDeliveryConfigurationTypeDef
        ],
        "LastModifiedTime": NotRequired[datetime],
        "SegmentDeliveryConfigurations": NotRequired[List[SegmentDeliveryConfigurationTypeDef]],
        "Tags": NotRequired[Dict[str, str]],
    },
)
UpdateSourceLocationRequestRequestTypeDef = TypedDict(
    "UpdateSourceLocationRequestRequestTypeDef",
    {
        "HttpConfiguration": HttpConfigurationTypeDef,
        "SourceLocationName": str,
        "AccessConfiguration": NotRequired[AccessConfigurationTypeDef],
        "DefaultSegmentDeliveryConfiguration": NotRequired[
            DefaultSegmentDeliveryConfigurationTypeDef
        ],
        "SegmentDeliveryConfigurations": NotRequired[Sequence[SegmentDeliveryConfigurationTypeDef]],
    },
)
UpdateSourceLocationResponseTypeDef = TypedDict(
    "UpdateSourceLocationResponseTypeDef",
    {
        "AccessConfiguration": AccessConfigurationTypeDef,
        "Arn": str,
        "CreationTime": datetime,
        "DefaultSegmentDeliveryConfiguration": DefaultSegmentDeliveryConfigurationTypeDef,
        "HttpConfiguration": HttpConfigurationTypeDef,
        "LastModifiedTime": datetime,
        "SegmentDeliveryConfigurations": List[SegmentDeliveryConfigurationTypeDef],
        "SourceLocationName": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPlaybackConfigurationResponseTypeDef = TypedDict(
    "GetPlaybackConfigurationResponseTypeDef",
    {
        "AdDecisionServerUrl": str,
        "AvailSuppression": AvailSuppressionTypeDef,
        "Bumper": BumperTypeDef,
        "CdnConfiguration": CdnConfigurationTypeDef,
        "ConfigurationAliases": Dict[str, Dict[str, str]],
        "DashConfiguration": DashConfigurationTypeDef,
        "HlsConfiguration": HlsConfigurationTypeDef,
        "InsertionMode": InsertionModeType,
        "LivePreRollConfiguration": LivePreRollConfigurationTypeDef,
        "LogConfiguration": LogConfigurationTypeDef,
        "ManifestProcessingRules": ManifestProcessingRulesTypeDef,
        "Name": str,
        "PersonalizationThresholdSeconds": int,
        "PlaybackConfigurationArn": str,
        "PlaybackEndpointPrefix": str,
        "SessionInitializationEndpointPrefix": str,
        "SlateAdUrl": str,
        "Tags": Dict[str, str],
        "TranscodeProfileName": str,
        "VideoContentSourceUrl": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PlaybackConfigurationTypeDef = TypedDict(
    "PlaybackConfigurationTypeDef",
    {
        "AdDecisionServerUrl": NotRequired[str],
        "AvailSuppression": NotRequired[AvailSuppressionTypeDef],
        "Bumper": NotRequired[BumperTypeDef],
        "CdnConfiguration": NotRequired[CdnConfigurationTypeDef],
        "ConfigurationAliases": NotRequired[Dict[str, Dict[str, str]]],
        "DashConfiguration": NotRequired[DashConfigurationTypeDef],
        "HlsConfiguration": NotRequired[HlsConfigurationTypeDef],
        "InsertionMode": NotRequired[InsertionModeType],
        "LivePreRollConfiguration": NotRequired[LivePreRollConfigurationTypeDef],
        "LogConfiguration": NotRequired[LogConfigurationTypeDef],
        "ManifestProcessingRules": NotRequired[ManifestProcessingRulesTypeDef],
        "Name": NotRequired[str],
        "PersonalizationThresholdSeconds": NotRequired[int],
        "PlaybackConfigurationArn": NotRequired[str],
        "PlaybackEndpointPrefix": NotRequired[str],
        "SessionInitializationEndpointPrefix": NotRequired[str],
        "SlateAdUrl": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
        "TranscodeProfileName": NotRequired[str],
        "VideoContentSourceUrl": NotRequired[str],
    },
)
PutPlaybackConfigurationRequestRequestTypeDef = TypedDict(
    "PutPlaybackConfigurationRequestRequestTypeDef",
    {
        "Name": str,
        "AdDecisionServerUrl": NotRequired[str],
        "AvailSuppression": NotRequired[AvailSuppressionTypeDef],
        "Bumper": NotRequired[BumperTypeDef],
        "CdnConfiguration": NotRequired[CdnConfigurationTypeDef],
        "ConfigurationAliases": NotRequired[Mapping[str, Mapping[str, str]]],
        "DashConfiguration": NotRequired[DashConfigurationForPutTypeDef],
        "InsertionMode": NotRequired[InsertionModeType],
        "LivePreRollConfiguration": NotRequired[LivePreRollConfigurationTypeDef],
        "ManifestProcessingRules": NotRequired[ManifestProcessingRulesTypeDef],
        "PersonalizationThresholdSeconds": NotRequired[int],
        "SlateAdUrl": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "TranscodeProfileName": NotRequired[str],
        "VideoContentSourceUrl": NotRequired[str],
    },
)
PutPlaybackConfigurationResponseTypeDef = TypedDict(
    "PutPlaybackConfigurationResponseTypeDef",
    {
        "AdDecisionServerUrl": str,
        "AvailSuppression": AvailSuppressionTypeDef,
        "Bumper": BumperTypeDef,
        "CdnConfiguration": CdnConfigurationTypeDef,
        "ConfigurationAliases": Dict[str, Dict[str, str]],
        "DashConfiguration": DashConfigurationTypeDef,
        "HlsConfiguration": HlsConfigurationTypeDef,
        "InsertionMode": InsertionModeType,
        "LivePreRollConfiguration": LivePreRollConfigurationTypeDef,
        "LogConfiguration": LogConfigurationTypeDef,
        "ManifestProcessingRules": ManifestProcessingRulesTypeDef,
        "Name": str,
        "PersonalizationThresholdSeconds": int,
        "PlaybackConfigurationArn": str,
        "PlaybackEndpointPrefix": str,
        "SessionInitializationEndpointPrefix": str,
        "SlateAdUrl": str,
        "Tags": Dict[str, str],
        "TranscodeProfileName": str,
        "VideoContentSourceUrl": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePrefetchScheduleResponseTypeDef = TypedDict(
    "CreatePrefetchScheduleResponseTypeDef",
    {
        "Arn": str,
        "Consumption": PrefetchConsumptionOutputTypeDef,
        "Name": str,
        "PlaybackConfigurationName": str,
        "Retrieval": PrefetchRetrievalOutputTypeDef,
        "StreamId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPrefetchScheduleResponseTypeDef = TypedDict(
    "GetPrefetchScheduleResponseTypeDef",
    {
        "Arn": str,
        "Consumption": PrefetchConsumptionOutputTypeDef,
        "Name": str,
        "PlaybackConfigurationName": str,
        "Retrieval": PrefetchRetrievalOutputTypeDef,
        "StreamId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PrefetchScheduleTypeDef = TypedDict(
    "PrefetchScheduleTypeDef",
    {
        "Arn": str,
        "Consumption": PrefetchConsumptionOutputTypeDef,
        "Name": str,
        "PlaybackConfigurationName": str,
        "Retrieval": PrefetchRetrievalOutputTypeDef,
        "StreamId": NotRequired[str],
    },
)
ListLiveSourcesResponseTypeDef = TypedDict(
    "ListLiveSourcesResponseTypeDef",
    {
        "Items": List[LiveSourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListVodSourcesResponseTypeDef = TypedDict(
    "ListVodSourcesResponseTypeDef",
    {
        "Items": List[VodSourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "Arn": str,
        "ChannelName": str,
        "ChannelState": str,
        "LogConfiguration": LogConfigurationForChannelTypeDef,
        "Outputs": List[ResponseOutputItemTypeDef],
        "PlaybackMode": str,
        "Tier": str,
        "Audiences": NotRequired[List[str]],
        "CreationTime": NotRequired[datetime],
        "FillerSlate": NotRequired[SlateSourceTypeDef],
        "LastModifiedTime": NotRequired[datetime],
        "Tags": NotRequired[Dict[str, str]],
    },
)
CreateChannelResponseTypeDef = TypedDict(
    "CreateChannelResponseTypeDef",
    {
        "Arn": str,
        "Audiences": List[str],
        "ChannelName": str,
        "ChannelState": ChannelStateType,
        "CreationTime": datetime,
        "FillerSlate": SlateSourceTypeDef,
        "LastModifiedTime": datetime,
        "Outputs": List[ResponseOutputItemTypeDef],
        "PlaybackMode": str,
        "Tags": Dict[str, str],
        "Tier": str,
        "TimeShiftConfiguration": TimeShiftConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeChannelResponseTypeDef = TypedDict(
    "DescribeChannelResponseTypeDef",
    {
        "Arn": str,
        "Audiences": List[str],
        "ChannelName": str,
        "ChannelState": ChannelStateType,
        "CreationTime": datetime,
        "FillerSlate": SlateSourceTypeDef,
        "LastModifiedTime": datetime,
        "LogConfiguration": LogConfigurationForChannelTypeDef,
        "Outputs": List[ResponseOutputItemTypeDef],
        "PlaybackMode": str,
        "Tags": Dict[str, str],
        "Tier": str,
        "TimeShiftConfiguration": TimeShiftConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateChannelResponseTypeDef = TypedDict(
    "UpdateChannelResponseTypeDef",
    {
        "Arn": str,
        "Audiences": List[str],
        "ChannelName": str,
        "ChannelState": ChannelStateType,
        "CreationTime": datetime,
        "FillerSlate": SlateSourceTypeDef,
        "LastModifiedTime": datetime,
        "Outputs": List[ResponseOutputItemTypeDef],
        "PlaybackMode": str,
        "Tags": Dict[str, str],
        "Tier": str,
        "TimeShiftConfiguration": TimeShiftConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RequestOutputItemTypeDef = TypedDict(
    "RequestOutputItemTypeDef",
    {
        "ManifestName": str,
        "SourceGroup": str,
        "DashPlaylistSettings": NotRequired[DashPlaylistSettingsTypeDef],
        "HlsPlaylistSettings": NotRequired[HlsPlaylistSettingsUnionTypeDef],
    },
)
CreatePrefetchScheduleRequestRequestTypeDef = TypedDict(
    "CreatePrefetchScheduleRequestRequestTypeDef",
    {
        "Consumption": PrefetchConsumptionTypeDef,
        "Name": str,
        "PlaybackConfigurationName": str,
        "Retrieval": PrefetchRetrievalTypeDef,
        "StreamId": NotRequired[str],
    },
)
GetChannelScheduleResponseTypeDef = TypedDict(
    "GetChannelScheduleResponseTypeDef",
    {
        "Items": List[ScheduleEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
AdBreakOutputTypeDef = TypedDict(
    "AdBreakOutputTypeDef",
    {
        "OffsetMillis": int,
        "AdBreakMetadata": NotRequired[List[KeyValuePairTypeDef]],
        "MessageType": NotRequired[MessageTypeType],
        "Slate": NotRequired[SlateSourceTypeDef],
        "SpliceInsertMessage": NotRequired[SpliceInsertMessageTypeDef],
        "TimeSignalMessage": NotRequired[TimeSignalMessageOutputTypeDef],
    },
)
TimeSignalMessageUnionTypeDef = Union[TimeSignalMessageTypeDef, TimeSignalMessageOutputTypeDef]
ListSourceLocationsResponseTypeDef = TypedDict(
    "ListSourceLocationsResponseTypeDef",
    {
        "Items": List[SourceLocationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListPlaybackConfigurationsResponseTypeDef = TypedDict(
    "ListPlaybackConfigurationsResponseTypeDef",
    {
        "Items": List[PlaybackConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListPrefetchSchedulesResponseTypeDef = TypedDict(
    "ListPrefetchSchedulesResponseTypeDef",
    {
        "Items": List[PrefetchScheduleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListChannelsResponseTypeDef = TypedDict(
    "ListChannelsResponseTypeDef",
    {
        "Items": List[ChannelTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateChannelRequestRequestTypeDef = TypedDict(
    "CreateChannelRequestRequestTypeDef",
    {
        "ChannelName": str,
        "Outputs": Sequence[RequestOutputItemTypeDef],
        "PlaybackMode": PlaybackModeType,
        "Audiences": NotRequired[Sequence[str]],
        "FillerSlate": NotRequired[SlateSourceTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
        "Tier": NotRequired[TierType],
        "TimeShiftConfiguration": NotRequired[TimeShiftConfigurationTypeDef],
    },
)
UpdateChannelRequestRequestTypeDef = TypedDict(
    "UpdateChannelRequestRequestTypeDef",
    {
        "ChannelName": str,
        "Outputs": Sequence[RequestOutputItemTypeDef],
        "Audiences": NotRequired[Sequence[str]],
        "FillerSlate": NotRequired[SlateSourceTypeDef],
        "TimeShiftConfiguration": NotRequired[TimeShiftConfigurationTypeDef],
    },
)
AlternateMediaOutputTypeDef = TypedDict(
    "AlternateMediaOutputTypeDef",
    {
        "AdBreaks": NotRequired[List[AdBreakOutputTypeDef]],
        "ClipRange": NotRequired[ClipRangeTypeDef],
        "DurationMillis": NotRequired[int],
        "LiveSourceName": NotRequired[str],
        "ScheduledStartTimeMillis": NotRequired[int],
        "SourceLocationName": NotRequired[str],
        "VodSourceName": NotRequired[str],
    },
)
AdBreakTypeDef = TypedDict(
    "AdBreakTypeDef",
    {
        "OffsetMillis": int,
        "AdBreakMetadata": NotRequired[Sequence[KeyValuePairTypeDef]],
        "MessageType": NotRequired[MessageTypeType],
        "Slate": NotRequired[SlateSourceTypeDef],
        "SpliceInsertMessage": NotRequired[SpliceInsertMessageTypeDef],
        "TimeSignalMessage": NotRequired[TimeSignalMessageUnionTypeDef],
    },
)
AudienceMediaOutputTypeDef = TypedDict(
    "AudienceMediaOutputTypeDef",
    {
        "AlternateMedia": NotRequired[List[AlternateMediaOutputTypeDef]],
        "Audience": NotRequired[str],
    },
)
AdBreakUnionTypeDef = Union[AdBreakTypeDef, AdBreakOutputTypeDef]
CreateProgramResponseTypeDef = TypedDict(
    "CreateProgramResponseTypeDef",
    {
        "AdBreaks": List[AdBreakOutputTypeDef],
        "Arn": str,
        "AudienceMedia": List[AudienceMediaOutputTypeDef],
        "ChannelName": str,
        "ClipRange": ClipRangeTypeDef,
        "CreationTime": datetime,
        "DurationMillis": int,
        "LiveSourceName": str,
        "ProgramName": str,
        "ScheduledStartTime": datetime,
        "SourceLocationName": str,
        "VodSourceName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeProgramResponseTypeDef = TypedDict(
    "DescribeProgramResponseTypeDef",
    {
        "AdBreaks": List[AdBreakOutputTypeDef],
        "Arn": str,
        "AudienceMedia": List[AudienceMediaOutputTypeDef],
        "ChannelName": str,
        "ClipRange": ClipRangeTypeDef,
        "CreationTime": datetime,
        "DurationMillis": int,
        "LiveSourceName": str,
        "ProgramName": str,
        "ScheduledStartTime": datetime,
        "SourceLocationName": str,
        "VodSourceName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateProgramResponseTypeDef = TypedDict(
    "UpdateProgramResponseTypeDef",
    {
        "AdBreaks": List[AdBreakOutputTypeDef],
        "Arn": str,
        "AudienceMedia": List[AudienceMediaOutputTypeDef],
        "ChannelName": str,
        "ClipRange": ClipRangeTypeDef,
        "CreationTime": datetime,
        "DurationMillis": int,
        "LiveSourceName": str,
        "ProgramName": str,
        "ScheduledStartTime": datetime,
        "SourceLocationName": str,
        "VodSourceName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AlternateMediaTypeDef = TypedDict(
    "AlternateMediaTypeDef",
    {
        "AdBreaks": NotRequired[Sequence[AdBreakUnionTypeDef]],
        "ClipRange": NotRequired[ClipRangeTypeDef],
        "DurationMillis": NotRequired[int],
        "LiveSourceName": NotRequired[str],
        "ScheduledStartTimeMillis": NotRequired[int],
        "SourceLocationName": NotRequired[str],
        "VodSourceName": NotRequired[str],
    },
)
AlternateMediaUnionTypeDef = Union[AlternateMediaTypeDef, AlternateMediaOutputTypeDef]
AudienceMediaTypeDef = TypedDict(
    "AudienceMediaTypeDef",
    {
        "AlternateMedia": NotRequired[Sequence[AlternateMediaUnionTypeDef]],
        "Audience": NotRequired[str],
    },
)
AudienceMediaUnionTypeDef = Union[AudienceMediaTypeDef, AudienceMediaOutputTypeDef]
UpdateProgramRequestRequestTypeDef = TypedDict(
    "UpdateProgramRequestRequestTypeDef",
    {
        "ChannelName": str,
        "ProgramName": str,
        "ScheduleConfiguration": UpdateProgramScheduleConfigurationTypeDef,
        "AdBreaks": NotRequired[Sequence[AdBreakTypeDef]],
        "AudienceMedia": NotRequired[Sequence[AudienceMediaTypeDef]],
    },
)
CreateProgramRequestRequestTypeDef = TypedDict(
    "CreateProgramRequestRequestTypeDef",
    {
        "ChannelName": str,
        "ProgramName": str,
        "ScheduleConfiguration": ScheduleConfigurationTypeDef,
        "SourceLocationName": str,
        "AdBreaks": NotRequired[Sequence[AdBreakUnionTypeDef]],
        "AudienceMedia": NotRequired[Sequence[AudienceMediaUnionTypeDef]],
        "LiveSourceName": NotRequired[str],
        "VodSourceName": NotRequired[str],
    },
)
