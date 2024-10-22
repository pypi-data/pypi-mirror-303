"""
Type annotations for kinesisvideo service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/type_defs/)

Usage::

    ```python
    from mypy_boto3_kinesisvideo.type_defs import SingleMasterConfigurationTypeDef

    data: SingleMasterConfigurationTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    APINameType,
    ChannelProtocolType,
    ChannelRoleType,
    ChannelTypeType,
    ConfigurationStatusType,
    FormatType,
    ImageSelectorTypeType,
    MediaStorageConfigurationStatusType,
    MediaUriTypeType,
    RecorderStatusType,
    StatusType,
    StrategyOnFullSizeType,
    SyncStatusType,
    UpdateDataRetentionOperationType,
    UploaderStatusType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "SingleMasterConfigurationTypeDef",
    "ChannelNameConditionTypeDef",
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "CreateStreamInputRequestTypeDef",
    "DeleteEdgeConfigurationInputRequestTypeDef",
    "DeleteSignalingChannelInputRequestTypeDef",
    "DeleteStreamInputRequestTypeDef",
    "LocalSizeConfigTypeDef",
    "DescribeEdgeConfigurationInputRequestTypeDef",
    "DescribeImageGenerationConfigurationInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeMappedResourceConfigurationInputRequestTypeDef",
    "MappedResourceConfigurationListItemTypeDef",
    "DescribeMediaStorageConfigurationInputRequestTypeDef",
    "MediaStorageConfigurationTypeDef",
    "DescribeNotificationConfigurationInputRequestTypeDef",
    "DescribeSignalingChannelInputRequestTypeDef",
    "DescribeStreamInputRequestTypeDef",
    "StreamInfoTypeDef",
    "LastRecorderStatusTypeDef",
    "LastUploaderStatusTypeDef",
    "GetDataEndpointInputRequestTypeDef",
    "SingleMasterChannelEndpointConfigurationTypeDef",
    "ResourceEndpointListItemTypeDef",
    "ImageGenerationDestinationConfigTypeDef",
    "ListEdgeAgentConfigurationsInputRequestTypeDef",
    "StreamNameConditionTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForStreamInputRequestTypeDef",
    "MediaSourceConfigTypeDef",
    "NotificationDestinationConfigTypeDef",
    "ScheduleConfigTypeDef",
    "TagStreamInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UntagStreamInputRequestTypeDef",
    "UpdateDataRetentionInputRequestTypeDef",
    "UpdateStreamInputRequestTypeDef",
    "ChannelInfoTypeDef",
    "UpdateSignalingChannelInputRequestTypeDef",
    "ListSignalingChannelsInputRequestTypeDef",
    "CreateSignalingChannelInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "CreateSignalingChannelOutputTypeDef",
    "CreateStreamOutputTypeDef",
    "GetDataEndpointOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListTagsForStreamOutputTypeDef",
    "DeletionConfigTypeDef",
    "DescribeMappedResourceConfigurationInputDescribeMappedResourceConfigurationPaginateTypeDef",
    "ListEdgeAgentConfigurationsInputListEdgeAgentConfigurationsPaginateTypeDef",
    "ListSignalingChannelsInputListSignalingChannelsPaginateTypeDef",
    "DescribeMappedResourceConfigurationOutputTypeDef",
    "DescribeMediaStorageConfigurationOutputTypeDef",
    "UpdateMediaStorageConfigurationInputRequestTypeDef",
    "DescribeStreamOutputTypeDef",
    "ListStreamsOutputTypeDef",
    "EdgeAgentStatusTypeDef",
    "GetSignalingChannelEndpointInputRequestTypeDef",
    "GetSignalingChannelEndpointOutputTypeDef",
    "ImageGenerationConfigurationOutputTypeDef",
    "ImageGenerationConfigurationTypeDef",
    "ListStreamsInputListStreamsPaginateTypeDef",
    "ListStreamsInputRequestTypeDef",
    "NotificationConfigurationTypeDef",
    "RecorderConfigTypeDef",
    "UploaderConfigTypeDef",
    "DescribeSignalingChannelOutputTypeDef",
    "ListSignalingChannelsOutputTypeDef",
    "DescribeImageGenerationConfigurationOutputTypeDef",
    "UpdateImageGenerationConfigurationInputRequestTypeDef",
    "DescribeNotificationConfigurationOutputTypeDef",
    "UpdateNotificationConfigurationInputRequestTypeDef",
    "EdgeConfigTypeDef",
    "DescribeEdgeConfigurationOutputTypeDef",
    "ListEdgeAgentConfigurationsEdgeConfigTypeDef",
    "StartEdgeConfigurationUpdateInputRequestTypeDef",
    "StartEdgeConfigurationUpdateOutputTypeDef",
    "ListEdgeAgentConfigurationsOutputTypeDef",
)

SingleMasterConfigurationTypeDef = TypedDict(
    "SingleMasterConfigurationTypeDef",
    {
        "MessageTtlSeconds": NotRequired[int],
    },
)
ChannelNameConditionTypeDef = TypedDict(
    "ChannelNameConditionTypeDef",
    {
        "ComparisonOperator": NotRequired[Literal["BEGINS_WITH"]],
        "ComparisonValue": NotRequired[str],
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
CreateStreamInputRequestTypeDef = TypedDict(
    "CreateStreamInputRequestTypeDef",
    {
        "StreamName": str,
        "DeviceName": NotRequired[str],
        "MediaType": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "DataRetentionInHours": NotRequired[int],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
DeleteEdgeConfigurationInputRequestTypeDef = TypedDict(
    "DeleteEdgeConfigurationInputRequestTypeDef",
    {
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
    },
)
DeleteSignalingChannelInputRequestTypeDef = TypedDict(
    "DeleteSignalingChannelInputRequestTypeDef",
    {
        "ChannelARN": str,
        "CurrentVersion": NotRequired[str],
    },
)
DeleteStreamInputRequestTypeDef = TypedDict(
    "DeleteStreamInputRequestTypeDef",
    {
        "StreamARN": str,
        "CurrentVersion": NotRequired[str],
    },
)
LocalSizeConfigTypeDef = TypedDict(
    "LocalSizeConfigTypeDef",
    {
        "MaxLocalMediaSizeInMB": NotRequired[int],
        "StrategyOnFullSize": NotRequired[StrategyOnFullSizeType],
    },
)
DescribeEdgeConfigurationInputRequestTypeDef = TypedDict(
    "DescribeEdgeConfigurationInputRequestTypeDef",
    {
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
    },
)
DescribeImageGenerationConfigurationInputRequestTypeDef = TypedDict(
    "DescribeImageGenerationConfigurationInputRequestTypeDef",
    {
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
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
DescribeMappedResourceConfigurationInputRequestTypeDef = TypedDict(
    "DescribeMappedResourceConfigurationInputRequestTypeDef",
    {
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
MappedResourceConfigurationListItemTypeDef = TypedDict(
    "MappedResourceConfigurationListItemTypeDef",
    {
        "Type": NotRequired[str],
        "ARN": NotRequired[str],
    },
)
DescribeMediaStorageConfigurationInputRequestTypeDef = TypedDict(
    "DescribeMediaStorageConfigurationInputRequestTypeDef",
    {
        "ChannelName": NotRequired[str],
        "ChannelARN": NotRequired[str],
    },
)
MediaStorageConfigurationTypeDef = TypedDict(
    "MediaStorageConfigurationTypeDef",
    {
        "Status": MediaStorageConfigurationStatusType,
        "StreamARN": NotRequired[str],
    },
)
DescribeNotificationConfigurationInputRequestTypeDef = TypedDict(
    "DescribeNotificationConfigurationInputRequestTypeDef",
    {
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
    },
)
DescribeSignalingChannelInputRequestTypeDef = TypedDict(
    "DescribeSignalingChannelInputRequestTypeDef",
    {
        "ChannelName": NotRequired[str],
        "ChannelARN": NotRequired[str],
    },
)
DescribeStreamInputRequestTypeDef = TypedDict(
    "DescribeStreamInputRequestTypeDef",
    {
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
    },
)
StreamInfoTypeDef = TypedDict(
    "StreamInfoTypeDef",
    {
        "DeviceName": NotRequired[str],
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
        "MediaType": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "Version": NotRequired[str],
        "Status": NotRequired[StatusType],
        "CreationTime": NotRequired[datetime],
        "DataRetentionInHours": NotRequired[int],
    },
)
LastRecorderStatusTypeDef = TypedDict(
    "LastRecorderStatusTypeDef",
    {
        "JobStatusDetails": NotRequired[str],
        "LastCollectedTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "RecorderStatus": NotRequired[RecorderStatusType],
    },
)
LastUploaderStatusTypeDef = TypedDict(
    "LastUploaderStatusTypeDef",
    {
        "JobStatusDetails": NotRequired[str],
        "LastCollectedTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "UploaderStatus": NotRequired[UploaderStatusType],
    },
)
GetDataEndpointInputRequestTypeDef = TypedDict(
    "GetDataEndpointInputRequestTypeDef",
    {
        "APIName": APINameType,
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
    },
)
SingleMasterChannelEndpointConfigurationTypeDef = TypedDict(
    "SingleMasterChannelEndpointConfigurationTypeDef",
    {
        "Protocols": NotRequired[Sequence[ChannelProtocolType]],
        "Role": NotRequired[ChannelRoleType],
    },
)
ResourceEndpointListItemTypeDef = TypedDict(
    "ResourceEndpointListItemTypeDef",
    {
        "Protocol": NotRequired[ChannelProtocolType],
        "ResourceEndpoint": NotRequired[str],
    },
)
ImageGenerationDestinationConfigTypeDef = TypedDict(
    "ImageGenerationDestinationConfigTypeDef",
    {
        "Uri": str,
        "DestinationRegion": str,
    },
)
ListEdgeAgentConfigurationsInputRequestTypeDef = TypedDict(
    "ListEdgeAgentConfigurationsInputRequestTypeDef",
    {
        "HubDeviceArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
StreamNameConditionTypeDef = TypedDict(
    "StreamNameConditionTypeDef",
    {
        "ComparisonOperator": NotRequired[Literal["BEGINS_WITH"]],
        "ComparisonValue": NotRequired[str],
    },
)
ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "NextToken": NotRequired[str],
    },
)
ListTagsForStreamInputRequestTypeDef = TypedDict(
    "ListTagsForStreamInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "StreamARN": NotRequired[str],
        "StreamName": NotRequired[str],
    },
)
MediaSourceConfigTypeDef = TypedDict(
    "MediaSourceConfigTypeDef",
    {
        "MediaUriSecretArn": str,
        "MediaUriType": MediaUriTypeType,
    },
)
NotificationDestinationConfigTypeDef = TypedDict(
    "NotificationDestinationConfigTypeDef",
    {
        "Uri": str,
    },
)
ScheduleConfigTypeDef = TypedDict(
    "ScheduleConfigTypeDef",
    {
        "ScheduleExpression": str,
        "DurationInSeconds": int,
    },
)
TagStreamInputRequestTypeDef = TypedDict(
    "TagStreamInputRequestTypeDef",
    {
        "Tags": Mapping[str, str],
        "StreamARN": NotRequired[str],
        "StreamName": NotRequired[str],
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeyList": Sequence[str],
    },
)
UntagStreamInputRequestTypeDef = TypedDict(
    "UntagStreamInputRequestTypeDef",
    {
        "TagKeyList": Sequence[str],
        "StreamARN": NotRequired[str],
        "StreamName": NotRequired[str],
    },
)
UpdateDataRetentionInputRequestTypeDef = TypedDict(
    "UpdateDataRetentionInputRequestTypeDef",
    {
        "CurrentVersion": str,
        "Operation": UpdateDataRetentionOperationType,
        "DataRetentionChangeInHours": int,
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
    },
)
UpdateStreamInputRequestTypeDef = TypedDict(
    "UpdateStreamInputRequestTypeDef",
    {
        "CurrentVersion": str,
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
        "DeviceName": NotRequired[str],
        "MediaType": NotRequired[str],
    },
)
ChannelInfoTypeDef = TypedDict(
    "ChannelInfoTypeDef",
    {
        "ChannelName": NotRequired[str],
        "ChannelARN": NotRequired[str],
        "ChannelType": NotRequired[ChannelTypeType],
        "ChannelStatus": NotRequired[StatusType],
        "CreationTime": NotRequired[datetime],
        "SingleMasterConfiguration": NotRequired[SingleMasterConfigurationTypeDef],
        "Version": NotRequired[str],
    },
)
UpdateSignalingChannelInputRequestTypeDef = TypedDict(
    "UpdateSignalingChannelInputRequestTypeDef",
    {
        "ChannelARN": str,
        "CurrentVersion": str,
        "SingleMasterConfiguration": NotRequired[SingleMasterConfigurationTypeDef],
    },
)
ListSignalingChannelsInputRequestTypeDef = TypedDict(
    "ListSignalingChannelsInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ChannelNameCondition": NotRequired[ChannelNameConditionTypeDef],
    },
)
CreateSignalingChannelInputRequestTypeDef = TypedDict(
    "CreateSignalingChannelInputRequestTypeDef",
    {
        "ChannelName": str,
        "ChannelType": NotRequired[ChannelTypeType],
        "SingleMasterConfiguration": NotRequired[SingleMasterConfigurationTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CreateSignalingChannelOutputTypeDef = TypedDict(
    "CreateSignalingChannelOutputTypeDef",
    {
        "ChannelARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateStreamOutputTypeDef = TypedDict(
    "CreateStreamOutputTypeDef",
    {
        "StreamARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDataEndpointOutputTypeDef = TypedDict(
    "GetDataEndpointOutputTypeDef",
    {
        "DataEndpoint": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTagsForStreamOutputTypeDef = TypedDict(
    "ListTagsForStreamOutputTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DeletionConfigTypeDef = TypedDict(
    "DeletionConfigTypeDef",
    {
        "EdgeRetentionInHours": NotRequired[int],
        "LocalSizeConfig": NotRequired[LocalSizeConfigTypeDef],
        "DeleteAfterUpload": NotRequired[bool],
    },
)
DescribeMappedResourceConfigurationInputDescribeMappedResourceConfigurationPaginateTypeDef = TypedDict(
    "DescribeMappedResourceConfigurationInputDescribeMappedResourceConfigurationPaginateTypeDef",
    {
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEdgeAgentConfigurationsInputListEdgeAgentConfigurationsPaginateTypeDef = TypedDict(
    "ListEdgeAgentConfigurationsInputListEdgeAgentConfigurationsPaginateTypeDef",
    {
        "HubDeviceArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSignalingChannelsInputListSignalingChannelsPaginateTypeDef = TypedDict(
    "ListSignalingChannelsInputListSignalingChannelsPaginateTypeDef",
    {
        "ChannelNameCondition": NotRequired[ChannelNameConditionTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeMappedResourceConfigurationOutputTypeDef = TypedDict(
    "DescribeMappedResourceConfigurationOutputTypeDef",
    {
        "MappedResourceConfigurationList": List[MappedResourceConfigurationListItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeMediaStorageConfigurationOutputTypeDef = TypedDict(
    "DescribeMediaStorageConfigurationOutputTypeDef",
    {
        "MediaStorageConfiguration": MediaStorageConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateMediaStorageConfigurationInputRequestTypeDef = TypedDict(
    "UpdateMediaStorageConfigurationInputRequestTypeDef",
    {
        "ChannelARN": str,
        "MediaStorageConfiguration": MediaStorageConfigurationTypeDef,
    },
)
DescribeStreamOutputTypeDef = TypedDict(
    "DescribeStreamOutputTypeDef",
    {
        "StreamInfo": StreamInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListStreamsOutputTypeDef = TypedDict(
    "ListStreamsOutputTypeDef",
    {
        "StreamInfoList": List[StreamInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
EdgeAgentStatusTypeDef = TypedDict(
    "EdgeAgentStatusTypeDef",
    {
        "LastRecorderStatus": NotRequired[LastRecorderStatusTypeDef],
        "LastUploaderStatus": NotRequired[LastUploaderStatusTypeDef],
    },
)
GetSignalingChannelEndpointInputRequestTypeDef = TypedDict(
    "GetSignalingChannelEndpointInputRequestTypeDef",
    {
        "ChannelARN": str,
        "SingleMasterChannelEndpointConfiguration": NotRequired[
            SingleMasterChannelEndpointConfigurationTypeDef
        ],
    },
)
GetSignalingChannelEndpointOutputTypeDef = TypedDict(
    "GetSignalingChannelEndpointOutputTypeDef",
    {
        "ResourceEndpointList": List[ResourceEndpointListItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImageGenerationConfigurationOutputTypeDef = TypedDict(
    "ImageGenerationConfigurationOutputTypeDef",
    {
        "Status": ConfigurationStatusType,
        "ImageSelectorType": ImageSelectorTypeType,
        "DestinationConfig": ImageGenerationDestinationConfigTypeDef,
        "SamplingInterval": int,
        "Format": FormatType,
        "FormatConfig": NotRequired[Dict[Literal["JPEGQuality"], str]],
        "WidthPixels": NotRequired[int],
        "HeightPixels": NotRequired[int],
    },
)
ImageGenerationConfigurationTypeDef = TypedDict(
    "ImageGenerationConfigurationTypeDef",
    {
        "Status": ConfigurationStatusType,
        "ImageSelectorType": ImageSelectorTypeType,
        "DestinationConfig": ImageGenerationDestinationConfigTypeDef,
        "SamplingInterval": int,
        "Format": FormatType,
        "FormatConfig": NotRequired[Mapping[Literal["JPEGQuality"], str]],
        "WidthPixels": NotRequired[int],
        "HeightPixels": NotRequired[int],
    },
)
ListStreamsInputListStreamsPaginateTypeDef = TypedDict(
    "ListStreamsInputListStreamsPaginateTypeDef",
    {
        "StreamNameCondition": NotRequired[StreamNameConditionTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListStreamsInputRequestTypeDef = TypedDict(
    "ListStreamsInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "StreamNameCondition": NotRequired[StreamNameConditionTypeDef],
    },
)
NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef",
    {
        "Status": ConfigurationStatusType,
        "DestinationConfig": NotificationDestinationConfigTypeDef,
    },
)
RecorderConfigTypeDef = TypedDict(
    "RecorderConfigTypeDef",
    {
        "MediaSourceConfig": MediaSourceConfigTypeDef,
        "ScheduleConfig": NotRequired[ScheduleConfigTypeDef],
    },
)
UploaderConfigTypeDef = TypedDict(
    "UploaderConfigTypeDef",
    {
        "ScheduleConfig": ScheduleConfigTypeDef,
    },
)
DescribeSignalingChannelOutputTypeDef = TypedDict(
    "DescribeSignalingChannelOutputTypeDef",
    {
        "ChannelInfo": ChannelInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSignalingChannelsOutputTypeDef = TypedDict(
    "ListSignalingChannelsOutputTypeDef",
    {
        "ChannelInfoList": List[ChannelInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeImageGenerationConfigurationOutputTypeDef = TypedDict(
    "DescribeImageGenerationConfigurationOutputTypeDef",
    {
        "ImageGenerationConfiguration": ImageGenerationConfigurationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateImageGenerationConfigurationInputRequestTypeDef = TypedDict(
    "UpdateImageGenerationConfigurationInputRequestTypeDef",
    {
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
        "ImageGenerationConfiguration": NotRequired[ImageGenerationConfigurationTypeDef],
    },
)
DescribeNotificationConfigurationOutputTypeDef = TypedDict(
    "DescribeNotificationConfigurationOutputTypeDef",
    {
        "NotificationConfiguration": NotificationConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateNotificationConfigurationInputRequestTypeDef = TypedDict(
    "UpdateNotificationConfigurationInputRequestTypeDef",
    {
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
        "NotificationConfiguration": NotRequired[NotificationConfigurationTypeDef],
    },
)
EdgeConfigTypeDef = TypedDict(
    "EdgeConfigTypeDef",
    {
        "HubDeviceArn": str,
        "RecorderConfig": RecorderConfigTypeDef,
        "UploaderConfig": NotRequired[UploaderConfigTypeDef],
        "DeletionConfig": NotRequired[DeletionConfigTypeDef],
    },
)
DescribeEdgeConfigurationOutputTypeDef = TypedDict(
    "DescribeEdgeConfigurationOutputTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
        "SyncStatus": SyncStatusType,
        "FailedStatusDetails": str,
        "EdgeConfig": EdgeConfigTypeDef,
        "EdgeAgentStatus": EdgeAgentStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEdgeAgentConfigurationsEdgeConfigTypeDef = TypedDict(
    "ListEdgeAgentConfigurationsEdgeConfigTypeDef",
    {
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "SyncStatus": NotRequired[SyncStatusType],
        "FailedStatusDetails": NotRequired[str],
        "EdgeConfig": NotRequired[EdgeConfigTypeDef],
    },
)
StartEdgeConfigurationUpdateInputRequestTypeDef = TypedDict(
    "StartEdgeConfigurationUpdateInputRequestTypeDef",
    {
        "EdgeConfig": EdgeConfigTypeDef,
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
    },
)
StartEdgeConfigurationUpdateOutputTypeDef = TypedDict(
    "StartEdgeConfigurationUpdateOutputTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
        "SyncStatus": SyncStatusType,
        "FailedStatusDetails": str,
        "EdgeConfig": EdgeConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEdgeAgentConfigurationsOutputTypeDef = TypedDict(
    "ListEdgeAgentConfigurationsOutputTypeDef",
    {
        "EdgeConfigs": List[ListEdgeAgentConfigurationsEdgeConfigTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
