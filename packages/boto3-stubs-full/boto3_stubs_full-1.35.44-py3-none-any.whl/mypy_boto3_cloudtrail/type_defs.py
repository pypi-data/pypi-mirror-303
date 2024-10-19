"""
Type annotations for cloudtrail service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/type_defs/)

Usage::

    ```python
    from mypy_boto3_cloudtrail.type_defs import TagTypeDef

    data: TagTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    BillingModeType,
    DeliveryStatusType,
    DestinationTypeType,
    EventDataStoreStatusType,
    FederationStatusType,
    ImportFailureStatusType,
    ImportStatusType,
    InsightsMetricDataTypeType,
    InsightTypeType,
    LookupAttributeKeyType,
    QueryStatusType,
    ReadWriteTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "TagTypeDef",
    "AdvancedFieldSelectorOutputTypeDef",
    "AdvancedFieldSelectorTypeDef",
    "CancelQueryRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "ChannelTypeDef",
    "DestinationTypeDef",
    "DataResourceOutputTypeDef",
    "DataResourceTypeDef",
    "DeleteChannelRequestRequestTypeDef",
    "DeleteEventDataStoreRequestRequestTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DeleteTrailRequestRequestTypeDef",
    "DeregisterOrganizationDelegatedAdminRequestRequestTypeDef",
    "DescribeQueryRequestRequestTypeDef",
    "QueryStatisticsForDescribeQueryTypeDef",
    "DescribeTrailsRequestRequestTypeDef",
    "TrailTypeDef",
    "DisableFederationRequestRequestTypeDef",
    "EnableFederationRequestRequestTypeDef",
    "ResourceTypeDef",
    "GetChannelRequestRequestTypeDef",
    "IngestionStatusTypeDef",
    "GetEventDataStoreRequestRequestTypeDef",
    "PartitionKeyTypeDef",
    "GetEventSelectorsRequestRequestTypeDef",
    "GetImportRequestRequestTypeDef",
    "ImportStatisticsTypeDef",
    "GetInsightSelectorsRequestRequestTypeDef",
    "InsightSelectorTypeDef",
    "GetQueryResultsRequestRequestTypeDef",
    "QueryStatisticsTypeDef",
    "GetResourcePolicyRequestRequestTypeDef",
    "GetTrailRequestRequestTypeDef",
    "GetTrailStatusRequestRequestTypeDef",
    "ImportFailureListItemTypeDef",
    "S3ImportSourceTypeDef",
    "ImportsListItemTypeDef",
    "ListChannelsRequestRequestTypeDef",
    "ListEventDataStoresRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListImportFailuresRequestRequestTypeDef",
    "ListImportsRequestRequestTypeDef",
    "TimestampTypeDef",
    "PublicKeyTypeDef",
    "QueryTypeDef",
    "ListTagsRequestRequestTypeDef",
    "ListTrailsRequestRequestTypeDef",
    "TrailInfoTypeDef",
    "LookupAttributeTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "RegisterOrganizationDelegatedAdminRequestRequestTypeDef",
    "RestoreEventDataStoreRequestRequestTypeDef",
    "StartEventDataStoreIngestionRequestRequestTypeDef",
    "StartLoggingRequestRequestTypeDef",
    "StartQueryRequestRequestTypeDef",
    "StopEventDataStoreIngestionRequestRequestTypeDef",
    "StopImportRequestRequestTypeDef",
    "StopLoggingRequestRequestTypeDef",
    "UpdateTrailRequestRequestTypeDef",
    "AddTagsRequestRequestTypeDef",
    "CreateTrailRequestRequestTypeDef",
    "RemoveTagsRequestRequestTypeDef",
    "ResourceTagTypeDef",
    "AdvancedEventSelectorOutputTypeDef",
    "AdvancedFieldSelectorUnionTypeDef",
    "CancelQueryResponseTypeDef",
    "CreateTrailResponseTypeDef",
    "DisableFederationResponseTypeDef",
    "EnableFederationResponseTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "GetTrailStatusResponseTypeDef",
    "ListInsightsMetricDataResponseTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "StartQueryResponseTypeDef",
    "UpdateTrailResponseTypeDef",
    "ListChannelsResponseTypeDef",
    "CreateChannelRequestRequestTypeDef",
    "CreateChannelResponseTypeDef",
    "UpdateChannelRequestRequestTypeDef",
    "UpdateChannelResponseTypeDef",
    "EventSelectorOutputTypeDef",
    "DataResourceUnionTypeDef",
    "DescribeQueryResponseTypeDef",
    "DescribeTrailsResponseTypeDef",
    "GetTrailResponseTypeDef",
    "EventTypeDef",
    "GetInsightSelectorsResponseTypeDef",
    "PutInsightSelectorsRequestRequestTypeDef",
    "PutInsightSelectorsResponseTypeDef",
    "GetQueryResultsResponseTypeDef",
    "ListImportFailuresResponseTypeDef",
    "ImportSourceTypeDef",
    "ListImportsResponseTypeDef",
    "ListImportFailuresRequestListImportFailuresPaginateTypeDef",
    "ListImportsRequestListImportsPaginateTypeDef",
    "ListTagsRequestListTagsPaginateTypeDef",
    "ListTrailsRequestListTrailsPaginateTypeDef",
    "ListInsightsMetricDataRequestRequestTypeDef",
    "ListPublicKeysRequestListPublicKeysPaginateTypeDef",
    "ListPublicKeysRequestRequestTypeDef",
    "ListQueriesRequestRequestTypeDef",
    "ListPublicKeysResponseTypeDef",
    "ListQueriesResponseTypeDef",
    "ListTrailsResponseTypeDef",
    "LookupEventsRequestLookupEventsPaginateTypeDef",
    "LookupEventsRequestRequestTypeDef",
    "ListTagsResponseTypeDef",
    "CreateEventDataStoreResponseTypeDef",
    "EventDataStoreTypeDef",
    "GetEventDataStoreResponseTypeDef",
    "RestoreEventDataStoreResponseTypeDef",
    "SourceConfigTypeDef",
    "UpdateEventDataStoreResponseTypeDef",
    "AdvancedEventSelectorTypeDef",
    "GetEventSelectorsResponseTypeDef",
    "PutEventSelectorsResponseTypeDef",
    "EventSelectorTypeDef",
    "LookupEventsResponseTypeDef",
    "GetImportResponseTypeDef",
    "StartImportRequestRequestTypeDef",
    "StartImportResponseTypeDef",
    "StopImportResponseTypeDef",
    "ListEventDataStoresResponseTypeDef",
    "GetChannelResponseTypeDef",
    "AdvancedEventSelectorUnionTypeDef",
    "UpdateEventDataStoreRequestRequestTypeDef",
    "EventSelectorUnionTypeDef",
    "CreateEventDataStoreRequestRequestTypeDef",
    "PutEventSelectorsRequestRequestTypeDef",
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": NotRequired[str],
    },
)
AdvancedFieldSelectorOutputTypeDef = TypedDict(
    "AdvancedFieldSelectorOutputTypeDef",
    {
        "Field": str,
        "Equals": NotRequired[List[str]],
        "StartsWith": NotRequired[List[str]],
        "EndsWith": NotRequired[List[str]],
        "NotEquals": NotRequired[List[str]],
        "NotStartsWith": NotRequired[List[str]],
        "NotEndsWith": NotRequired[List[str]],
    },
)
AdvancedFieldSelectorTypeDef = TypedDict(
    "AdvancedFieldSelectorTypeDef",
    {
        "Field": str,
        "Equals": NotRequired[Sequence[str]],
        "StartsWith": NotRequired[Sequence[str]],
        "EndsWith": NotRequired[Sequence[str]],
        "NotEquals": NotRequired[Sequence[str]],
        "NotStartsWith": NotRequired[Sequence[str]],
        "NotEndsWith": NotRequired[Sequence[str]],
    },
)
CancelQueryRequestRequestTypeDef = TypedDict(
    "CancelQueryRequestRequestTypeDef",
    {
        "QueryId": str,
        "EventDataStore": NotRequired[str],
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
ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "ChannelArn": NotRequired[str],
        "Name": NotRequired[str],
    },
)
DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "Type": DestinationTypeType,
        "Location": str,
    },
)
DataResourceOutputTypeDef = TypedDict(
    "DataResourceOutputTypeDef",
    {
        "Type": NotRequired[str],
        "Values": NotRequired[List[str]],
    },
)
DataResourceTypeDef = TypedDict(
    "DataResourceTypeDef",
    {
        "Type": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)
DeleteChannelRequestRequestTypeDef = TypedDict(
    "DeleteChannelRequestRequestTypeDef",
    {
        "Channel": str,
    },
)
DeleteEventDataStoreRequestRequestTypeDef = TypedDict(
    "DeleteEventDataStoreRequestRequestTypeDef",
    {
        "EventDataStore": str,
    },
)
DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
DeleteTrailRequestRequestTypeDef = TypedDict(
    "DeleteTrailRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeregisterOrganizationDelegatedAdminRequestRequestTypeDef = TypedDict(
    "DeregisterOrganizationDelegatedAdminRequestRequestTypeDef",
    {
        "DelegatedAdminAccountId": str,
    },
)
DescribeQueryRequestRequestTypeDef = TypedDict(
    "DescribeQueryRequestRequestTypeDef",
    {
        "EventDataStore": NotRequired[str],
        "QueryId": NotRequired[str],
        "QueryAlias": NotRequired[str],
    },
)
QueryStatisticsForDescribeQueryTypeDef = TypedDict(
    "QueryStatisticsForDescribeQueryTypeDef",
    {
        "EventsMatched": NotRequired[int],
        "EventsScanned": NotRequired[int],
        "BytesScanned": NotRequired[int],
        "ExecutionTimeInMillis": NotRequired[int],
        "CreationTime": NotRequired[datetime],
    },
)
DescribeTrailsRequestRequestTypeDef = TypedDict(
    "DescribeTrailsRequestRequestTypeDef",
    {
        "trailNameList": NotRequired[Sequence[str]],
        "includeShadowTrails": NotRequired[bool],
    },
)
TrailTypeDef = TypedDict(
    "TrailTypeDef",
    {
        "Name": NotRequired[str],
        "S3BucketName": NotRequired[str],
        "S3KeyPrefix": NotRequired[str],
        "SnsTopicName": NotRequired[str],
        "SnsTopicARN": NotRequired[str],
        "IncludeGlobalServiceEvents": NotRequired[bool],
        "IsMultiRegionTrail": NotRequired[bool],
        "HomeRegion": NotRequired[str],
        "TrailARN": NotRequired[str],
        "LogFileValidationEnabled": NotRequired[bool],
        "CloudWatchLogsLogGroupArn": NotRequired[str],
        "CloudWatchLogsRoleArn": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "HasCustomEventSelectors": NotRequired[bool],
        "HasInsightSelectors": NotRequired[bool],
        "IsOrganizationTrail": NotRequired[bool],
    },
)
DisableFederationRequestRequestTypeDef = TypedDict(
    "DisableFederationRequestRequestTypeDef",
    {
        "EventDataStore": str,
    },
)
EnableFederationRequestRequestTypeDef = TypedDict(
    "EnableFederationRequestRequestTypeDef",
    {
        "EventDataStore": str,
        "FederationRoleArn": str,
    },
)
ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "ResourceType": NotRequired[str],
        "ResourceName": NotRequired[str],
    },
)
GetChannelRequestRequestTypeDef = TypedDict(
    "GetChannelRequestRequestTypeDef",
    {
        "Channel": str,
    },
)
IngestionStatusTypeDef = TypedDict(
    "IngestionStatusTypeDef",
    {
        "LatestIngestionSuccessTime": NotRequired[datetime],
        "LatestIngestionSuccessEventID": NotRequired[str],
        "LatestIngestionErrorCode": NotRequired[str],
        "LatestIngestionAttemptTime": NotRequired[datetime],
        "LatestIngestionAttemptEventID": NotRequired[str],
    },
)
GetEventDataStoreRequestRequestTypeDef = TypedDict(
    "GetEventDataStoreRequestRequestTypeDef",
    {
        "EventDataStore": str,
    },
)
PartitionKeyTypeDef = TypedDict(
    "PartitionKeyTypeDef",
    {
        "Name": str,
        "Type": str,
    },
)
GetEventSelectorsRequestRequestTypeDef = TypedDict(
    "GetEventSelectorsRequestRequestTypeDef",
    {
        "TrailName": str,
    },
)
GetImportRequestRequestTypeDef = TypedDict(
    "GetImportRequestRequestTypeDef",
    {
        "ImportId": str,
    },
)
ImportStatisticsTypeDef = TypedDict(
    "ImportStatisticsTypeDef",
    {
        "PrefixesFound": NotRequired[int],
        "PrefixesCompleted": NotRequired[int],
        "FilesCompleted": NotRequired[int],
        "EventsCompleted": NotRequired[int],
        "FailedEntries": NotRequired[int],
    },
)
GetInsightSelectorsRequestRequestTypeDef = TypedDict(
    "GetInsightSelectorsRequestRequestTypeDef",
    {
        "TrailName": NotRequired[str],
        "EventDataStore": NotRequired[str],
    },
)
InsightSelectorTypeDef = TypedDict(
    "InsightSelectorTypeDef",
    {
        "InsightType": NotRequired[InsightTypeType],
    },
)
GetQueryResultsRequestRequestTypeDef = TypedDict(
    "GetQueryResultsRequestRequestTypeDef",
    {
        "QueryId": str,
        "EventDataStore": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxQueryResults": NotRequired[int],
    },
)
QueryStatisticsTypeDef = TypedDict(
    "QueryStatisticsTypeDef",
    {
        "ResultsCount": NotRequired[int],
        "TotalResultsCount": NotRequired[int],
        "BytesScanned": NotRequired[int],
    },
)
GetResourcePolicyRequestRequestTypeDef = TypedDict(
    "GetResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
GetTrailRequestRequestTypeDef = TypedDict(
    "GetTrailRequestRequestTypeDef",
    {
        "Name": str,
    },
)
GetTrailStatusRequestRequestTypeDef = TypedDict(
    "GetTrailStatusRequestRequestTypeDef",
    {
        "Name": str,
    },
)
ImportFailureListItemTypeDef = TypedDict(
    "ImportFailureListItemTypeDef",
    {
        "Location": NotRequired[str],
        "Status": NotRequired[ImportFailureStatusType],
        "ErrorType": NotRequired[str],
        "ErrorMessage": NotRequired[str],
        "LastUpdatedTime": NotRequired[datetime],
    },
)
S3ImportSourceTypeDef = TypedDict(
    "S3ImportSourceTypeDef",
    {
        "S3LocationUri": str,
        "S3BucketRegion": str,
        "S3BucketAccessRoleArn": str,
    },
)
ImportsListItemTypeDef = TypedDict(
    "ImportsListItemTypeDef",
    {
        "ImportId": NotRequired[str],
        "ImportStatus": NotRequired[ImportStatusType],
        "Destinations": NotRequired[List[str]],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
    },
)
ListChannelsRequestRequestTypeDef = TypedDict(
    "ListChannelsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListEventDataStoresRequestRequestTypeDef = TypedDict(
    "ListEventDataStoresRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
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
ListImportFailuresRequestRequestTypeDef = TypedDict(
    "ListImportFailuresRequestRequestTypeDef",
    {
        "ImportId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListImportsRequestRequestTypeDef = TypedDict(
    "ListImportsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "Destination": NotRequired[str],
        "ImportStatus": NotRequired[ImportStatusType],
        "NextToken": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
PublicKeyTypeDef = TypedDict(
    "PublicKeyTypeDef",
    {
        "Value": NotRequired[bytes],
        "ValidityStartTime": NotRequired[datetime],
        "ValidityEndTime": NotRequired[datetime],
        "Fingerprint": NotRequired[str],
    },
)
QueryTypeDef = TypedDict(
    "QueryTypeDef",
    {
        "QueryId": NotRequired[str],
        "QueryStatus": NotRequired[QueryStatusType],
        "CreationTime": NotRequired[datetime],
    },
)
ListTagsRequestRequestTypeDef = TypedDict(
    "ListTagsRequestRequestTypeDef",
    {
        "ResourceIdList": Sequence[str],
        "NextToken": NotRequired[str],
    },
)
ListTrailsRequestRequestTypeDef = TypedDict(
    "ListTrailsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)
TrailInfoTypeDef = TypedDict(
    "TrailInfoTypeDef",
    {
        "TrailARN": NotRequired[str],
        "Name": NotRequired[str],
        "HomeRegion": NotRequired[str],
    },
)
LookupAttributeTypeDef = TypedDict(
    "LookupAttributeTypeDef",
    {
        "AttributeKey": LookupAttributeKeyType,
        "AttributeValue": str,
    },
)
PutResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "ResourcePolicy": str,
    },
)
RegisterOrganizationDelegatedAdminRequestRequestTypeDef = TypedDict(
    "RegisterOrganizationDelegatedAdminRequestRequestTypeDef",
    {
        "MemberAccountId": str,
    },
)
RestoreEventDataStoreRequestRequestTypeDef = TypedDict(
    "RestoreEventDataStoreRequestRequestTypeDef",
    {
        "EventDataStore": str,
    },
)
StartEventDataStoreIngestionRequestRequestTypeDef = TypedDict(
    "StartEventDataStoreIngestionRequestRequestTypeDef",
    {
        "EventDataStore": str,
    },
)
StartLoggingRequestRequestTypeDef = TypedDict(
    "StartLoggingRequestRequestTypeDef",
    {
        "Name": str,
    },
)
StartQueryRequestRequestTypeDef = TypedDict(
    "StartQueryRequestRequestTypeDef",
    {
        "QueryStatement": NotRequired[str],
        "DeliveryS3Uri": NotRequired[str],
        "QueryAlias": NotRequired[str],
        "QueryParameters": NotRequired[Sequence[str]],
    },
)
StopEventDataStoreIngestionRequestRequestTypeDef = TypedDict(
    "StopEventDataStoreIngestionRequestRequestTypeDef",
    {
        "EventDataStore": str,
    },
)
StopImportRequestRequestTypeDef = TypedDict(
    "StopImportRequestRequestTypeDef",
    {
        "ImportId": str,
    },
)
StopLoggingRequestRequestTypeDef = TypedDict(
    "StopLoggingRequestRequestTypeDef",
    {
        "Name": str,
    },
)
UpdateTrailRequestRequestTypeDef = TypedDict(
    "UpdateTrailRequestRequestTypeDef",
    {
        "Name": str,
        "S3BucketName": NotRequired[str],
        "S3KeyPrefix": NotRequired[str],
        "SnsTopicName": NotRequired[str],
        "IncludeGlobalServiceEvents": NotRequired[bool],
        "IsMultiRegionTrail": NotRequired[bool],
        "EnableLogFileValidation": NotRequired[bool],
        "CloudWatchLogsLogGroupArn": NotRequired[str],
        "CloudWatchLogsRoleArn": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "IsOrganizationTrail": NotRequired[bool],
    },
)
AddTagsRequestRequestTypeDef = TypedDict(
    "AddTagsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "TagsList": Sequence[TagTypeDef],
    },
)
CreateTrailRequestRequestTypeDef = TypedDict(
    "CreateTrailRequestRequestTypeDef",
    {
        "Name": str,
        "S3BucketName": str,
        "S3KeyPrefix": NotRequired[str],
        "SnsTopicName": NotRequired[str],
        "IncludeGlobalServiceEvents": NotRequired[bool],
        "IsMultiRegionTrail": NotRequired[bool],
        "EnableLogFileValidation": NotRequired[bool],
        "CloudWatchLogsLogGroupArn": NotRequired[str],
        "CloudWatchLogsRoleArn": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "IsOrganizationTrail": NotRequired[bool],
        "TagsList": NotRequired[Sequence[TagTypeDef]],
    },
)
RemoveTagsRequestRequestTypeDef = TypedDict(
    "RemoveTagsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "TagsList": Sequence[TagTypeDef],
    },
)
ResourceTagTypeDef = TypedDict(
    "ResourceTagTypeDef",
    {
        "ResourceId": NotRequired[str],
        "TagsList": NotRequired[List[TagTypeDef]],
    },
)
AdvancedEventSelectorOutputTypeDef = TypedDict(
    "AdvancedEventSelectorOutputTypeDef",
    {
        "FieldSelectors": List[AdvancedFieldSelectorOutputTypeDef],
        "Name": NotRequired[str],
    },
)
AdvancedFieldSelectorUnionTypeDef = Union[
    AdvancedFieldSelectorTypeDef, AdvancedFieldSelectorOutputTypeDef
]
CancelQueryResponseTypeDef = TypedDict(
    "CancelQueryResponseTypeDef",
    {
        "QueryId": str,
        "QueryStatus": QueryStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTrailResponseTypeDef = TypedDict(
    "CreateTrailResponseTypeDef",
    {
        "Name": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "SnsTopicName": str,
        "SnsTopicARN": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "TrailARN": str,
        "LogFileValidationEnabled": bool,
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "KmsKeyId": str,
        "IsOrganizationTrail": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisableFederationResponseTypeDef = TypedDict(
    "DisableFederationResponseTypeDef",
    {
        "EventDataStoreArn": str,
        "FederationStatus": FederationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableFederationResponseTypeDef = TypedDict(
    "EnableFederationResponseTypeDef",
    {
        "EventDataStoreArn": str,
        "FederationStatus": FederationStatusType,
        "FederationRoleArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResourcePolicyResponseTypeDef = TypedDict(
    "GetResourcePolicyResponseTypeDef",
    {
        "ResourceArn": str,
        "ResourcePolicy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTrailStatusResponseTypeDef = TypedDict(
    "GetTrailStatusResponseTypeDef",
    {
        "IsLogging": bool,
        "LatestDeliveryError": str,
        "LatestNotificationError": str,
        "LatestDeliveryTime": datetime,
        "LatestNotificationTime": datetime,
        "StartLoggingTime": datetime,
        "StopLoggingTime": datetime,
        "LatestCloudWatchLogsDeliveryError": str,
        "LatestCloudWatchLogsDeliveryTime": datetime,
        "LatestDigestDeliveryTime": datetime,
        "LatestDigestDeliveryError": str,
        "LatestDeliveryAttemptTime": str,
        "LatestNotificationAttemptTime": str,
        "LatestNotificationAttemptSucceeded": str,
        "LatestDeliveryAttemptSucceeded": str,
        "TimeLoggingStarted": str,
        "TimeLoggingStopped": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListInsightsMetricDataResponseTypeDef = TypedDict(
    "ListInsightsMetricDataResponseTypeDef",
    {
        "EventSource": str,
        "EventName": str,
        "InsightType": InsightTypeType,
        "ErrorCode": str,
        "Timestamps": List[datetime],
        "Values": List[float],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PutResourcePolicyResponseTypeDef = TypedDict(
    "PutResourcePolicyResponseTypeDef",
    {
        "ResourceArn": str,
        "ResourcePolicy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartQueryResponseTypeDef = TypedDict(
    "StartQueryResponseTypeDef",
    {
        "QueryId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTrailResponseTypeDef = TypedDict(
    "UpdateTrailResponseTypeDef",
    {
        "Name": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "SnsTopicName": str,
        "SnsTopicARN": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "TrailARN": str,
        "LogFileValidationEnabled": bool,
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "KmsKeyId": str,
        "IsOrganizationTrail": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
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
CreateChannelRequestRequestTypeDef = TypedDict(
    "CreateChannelRequestRequestTypeDef",
    {
        "Name": str,
        "Source": str,
        "Destinations": Sequence[DestinationTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateChannelResponseTypeDef = TypedDict(
    "CreateChannelResponseTypeDef",
    {
        "ChannelArn": str,
        "Name": str,
        "Source": str,
        "Destinations": List[DestinationTypeDef],
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateChannelRequestRequestTypeDef = TypedDict(
    "UpdateChannelRequestRequestTypeDef",
    {
        "Channel": str,
        "Destinations": NotRequired[Sequence[DestinationTypeDef]],
        "Name": NotRequired[str],
    },
)
UpdateChannelResponseTypeDef = TypedDict(
    "UpdateChannelResponseTypeDef",
    {
        "ChannelArn": str,
        "Name": str,
        "Source": str,
        "Destinations": List[DestinationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EventSelectorOutputTypeDef = TypedDict(
    "EventSelectorOutputTypeDef",
    {
        "ReadWriteType": NotRequired[ReadWriteTypeType],
        "IncludeManagementEvents": NotRequired[bool],
        "DataResources": NotRequired[List[DataResourceOutputTypeDef]],
        "ExcludeManagementEventSources": NotRequired[List[str]],
    },
)
DataResourceUnionTypeDef = Union[DataResourceTypeDef, DataResourceOutputTypeDef]
DescribeQueryResponseTypeDef = TypedDict(
    "DescribeQueryResponseTypeDef",
    {
        "QueryId": str,
        "QueryString": str,
        "QueryStatus": QueryStatusType,
        "QueryStatistics": QueryStatisticsForDescribeQueryTypeDef,
        "ErrorMessage": str,
        "DeliveryS3Uri": str,
        "DeliveryStatus": DeliveryStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTrailsResponseTypeDef = TypedDict(
    "DescribeTrailsResponseTypeDef",
    {
        "trailList": List[TrailTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTrailResponseTypeDef = TypedDict(
    "GetTrailResponseTypeDef",
    {
        "Trail": TrailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "EventId": NotRequired[str],
        "EventName": NotRequired[str],
        "ReadOnly": NotRequired[str],
        "AccessKeyId": NotRequired[str],
        "EventTime": NotRequired[datetime],
        "EventSource": NotRequired[str],
        "Username": NotRequired[str],
        "Resources": NotRequired[List[ResourceTypeDef]],
        "CloudTrailEvent": NotRequired[str],
    },
)
GetInsightSelectorsResponseTypeDef = TypedDict(
    "GetInsightSelectorsResponseTypeDef",
    {
        "TrailARN": str,
        "InsightSelectors": List[InsightSelectorTypeDef],
        "EventDataStoreArn": str,
        "InsightsDestination": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutInsightSelectorsRequestRequestTypeDef = TypedDict(
    "PutInsightSelectorsRequestRequestTypeDef",
    {
        "InsightSelectors": Sequence[InsightSelectorTypeDef],
        "TrailName": NotRequired[str],
        "EventDataStore": NotRequired[str],
        "InsightsDestination": NotRequired[str],
    },
)
PutInsightSelectorsResponseTypeDef = TypedDict(
    "PutInsightSelectorsResponseTypeDef",
    {
        "TrailARN": str,
        "InsightSelectors": List[InsightSelectorTypeDef],
        "EventDataStoreArn": str,
        "InsightsDestination": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetQueryResultsResponseTypeDef = TypedDict(
    "GetQueryResultsResponseTypeDef",
    {
        "QueryStatus": QueryStatusType,
        "QueryStatistics": QueryStatisticsTypeDef,
        "QueryResultRows": List[List[Dict[str, str]]],
        "ErrorMessage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListImportFailuresResponseTypeDef = TypedDict(
    "ListImportFailuresResponseTypeDef",
    {
        "Failures": List[ImportFailureListItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ImportSourceTypeDef = TypedDict(
    "ImportSourceTypeDef",
    {
        "S3": S3ImportSourceTypeDef,
    },
)
ListImportsResponseTypeDef = TypedDict(
    "ListImportsResponseTypeDef",
    {
        "Imports": List[ImportsListItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListImportFailuresRequestListImportFailuresPaginateTypeDef = TypedDict(
    "ListImportFailuresRequestListImportFailuresPaginateTypeDef",
    {
        "ImportId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListImportsRequestListImportsPaginateTypeDef = TypedDict(
    "ListImportsRequestListImportsPaginateTypeDef",
    {
        "Destination": NotRequired[str],
        "ImportStatus": NotRequired[ImportStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTagsRequestListTagsPaginateTypeDef = TypedDict(
    "ListTagsRequestListTagsPaginateTypeDef",
    {
        "ResourceIdList": Sequence[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTrailsRequestListTrailsPaginateTypeDef = TypedDict(
    "ListTrailsRequestListTrailsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListInsightsMetricDataRequestRequestTypeDef = TypedDict(
    "ListInsightsMetricDataRequestRequestTypeDef",
    {
        "EventSource": str,
        "EventName": str,
        "InsightType": InsightTypeType,
        "ErrorCode": NotRequired[str],
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "Period": NotRequired[int],
        "DataType": NotRequired[InsightsMetricDataTypeType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListPublicKeysRequestListPublicKeysPaginateTypeDef = TypedDict(
    "ListPublicKeysRequestListPublicKeysPaginateTypeDef",
    {
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPublicKeysRequestRequestTypeDef = TypedDict(
    "ListPublicKeysRequestRequestTypeDef",
    {
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "NextToken": NotRequired[str],
    },
)
ListQueriesRequestRequestTypeDef = TypedDict(
    "ListQueriesRequestRequestTypeDef",
    {
        "EventDataStore": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "QueryStatus": NotRequired[QueryStatusType],
    },
)
ListPublicKeysResponseTypeDef = TypedDict(
    "ListPublicKeysResponseTypeDef",
    {
        "PublicKeyList": List[PublicKeyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListQueriesResponseTypeDef = TypedDict(
    "ListQueriesResponseTypeDef",
    {
        "Queries": List[QueryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTrailsResponseTypeDef = TypedDict(
    "ListTrailsResponseTypeDef",
    {
        "Trails": List[TrailInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
LookupEventsRequestLookupEventsPaginateTypeDef = TypedDict(
    "LookupEventsRequestLookupEventsPaginateTypeDef",
    {
        "LookupAttributes": NotRequired[Sequence[LookupAttributeTypeDef]],
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "EventCategory": NotRequired[Literal["insight"]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
LookupEventsRequestRequestTypeDef = TypedDict(
    "LookupEventsRequestRequestTypeDef",
    {
        "LookupAttributes": NotRequired[Sequence[LookupAttributeTypeDef]],
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "EventCategory": NotRequired[Literal["insight"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef",
    {
        "ResourceTagList": List[ResourceTagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateEventDataStoreResponseTypeDef = TypedDict(
    "CreateEventDataStoreResponseTypeDef",
    {
        "EventDataStoreArn": str,
        "Name": str,
        "Status": EventDataStoreStatusType,
        "AdvancedEventSelectors": List[AdvancedEventSelectorOutputTypeDef],
        "MultiRegionEnabled": bool,
        "OrganizationEnabled": bool,
        "RetentionPeriod": int,
        "TerminationProtectionEnabled": bool,
        "TagsList": List[TagTypeDef],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "KmsKeyId": str,
        "BillingMode": BillingModeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EventDataStoreTypeDef = TypedDict(
    "EventDataStoreTypeDef",
    {
        "EventDataStoreArn": NotRequired[str],
        "Name": NotRequired[str],
        "TerminationProtectionEnabled": NotRequired[bool],
        "Status": NotRequired[EventDataStoreStatusType],
        "AdvancedEventSelectors": NotRequired[List[AdvancedEventSelectorOutputTypeDef]],
        "MultiRegionEnabled": NotRequired[bool],
        "OrganizationEnabled": NotRequired[bool],
        "RetentionPeriod": NotRequired[int],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
    },
)
GetEventDataStoreResponseTypeDef = TypedDict(
    "GetEventDataStoreResponseTypeDef",
    {
        "EventDataStoreArn": str,
        "Name": str,
        "Status": EventDataStoreStatusType,
        "AdvancedEventSelectors": List[AdvancedEventSelectorOutputTypeDef],
        "MultiRegionEnabled": bool,
        "OrganizationEnabled": bool,
        "RetentionPeriod": int,
        "TerminationProtectionEnabled": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "KmsKeyId": str,
        "BillingMode": BillingModeType,
        "FederationStatus": FederationStatusType,
        "FederationRoleArn": str,
        "PartitionKeys": List[PartitionKeyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreEventDataStoreResponseTypeDef = TypedDict(
    "RestoreEventDataStoreResponseTypeDef",
    {
        "EventDataStoreArn": str,
        "Name": str,
        "Status": EventDataStoreStatusType,
        "AdvancedEventSelectors": List[AdvancedEventSelectorOutputTypeDef],
        "MultiRegionEnabled": bool,
        "OrganizationEnabled": bool,
        "RetentionPeriod": int,
        "TerminationProtectionEnabled": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "KmsKeyId": str,
        "BillingMode": BillingModeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SourceConfigTypeDef = TypedDict(
    "SourceConfigTypeDef",
    {
        "ApplyToAllRegions": NotRequired[bool],
        "AdvancedEventSelectors": NotRequired[List[AdvancedEventSelectorOutputTypeDef]],
    },
)
UpdateEventDataStoreResponseTypeDef = TypedDict(
    "UpdateEventDataStoreResponseTypeDef",
    {
        "EventDataStoreArn": str,
        "Name": str,
        "Status": EventDataStoreStatusType,
        "AdvancedEventSelectors": List[AdvancedEventSelectorOutputTypeDef],
        "MultiRegionEnabled": bool,
        "OrganizationEnabled": bool,
        "RetentionPeriod": int,
        "TerminationProtectionEnabled": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "KmsKeyId": str,
        "BillingMode": BillingModeType,
        "FederationStatus": FederationStatusType,
        "FederationRoleArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AdvancedEventSelectorTypeDef = TypedDict(
    "AdvancedEventSelectorTypeDef",
    {
        "FieldSelectors": Sequence[AdvancedFieldSelectorUnionTypeDef],
        "Name": NotRequired[str],
    },
)
GetEventSelectorsResponseTypeDef = TypedDict(
    "GetEventSelectorsResponseTypeDef",
    {
        "TrailARN": str,
        "EventSelectors": List[EventSelectorOutputTypeDef],
        "AdvancedEventSelectors": List[AdvancedEventSelectorOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutEventSelectorsResponseTypeDef = TypedDict(
    "PutEventSelectorsResponseTypeDef",
    {
        "TrailARN": str,
        "EventSelectors": List[EventSelectorOutputTypeDef],
        "AdvancedEventSelectors": List[AdvancedEventSelectorOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EventSelectorTypeDef = TypedDict(
    "EventSelectorTypeDef",
    {
        "ReadWriteType": NotRequired[ReadWriteTypeType],
        "IncludeManagementEvents": NotRequired[bool],
        "DataResources": NotRequired[Sequence[DataResourceUnionTypeDef]],
        "ExcludeManagementEventSources": NotRequired[Sequence[str]],
    },
)
LookupEventsResponseTypeDef = TypedDict(
    "LookupEventsResponseTypeDef",
    {
        "Events": List[EventTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetImportResponseTypeDef = TypedDict(
    "GetImportResponseTypeDef",
    {
        "ImportId": str,
        "Destinations": List[str],
        "ImportSource": ImportSourceTypeDef,
        "StartEventTime": datetime,
        "EndEventTime": datetime,
        "ImportStatus": ImportStatusType,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "ImportStatistics": ImportStatisticsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartImportRequestRequestTypeDef = TypedDict(
    "StartImportRequestRequestTypeDef",
    {
        "Destinations": NotRequired[Sequence[str]],
        "ImportSource": NotRequired[ImportSourceTypeDef],
        "StartEventTime": NotRequired[TimestampTypeDef],
        "EndEventTime": NotRequired[TimestampTypeDef],
        "ImportId": NotRequired[str],
    },
)
StartImportResponseTypeDef = TypedDict(
    "StartImportResponseTypeDef",
    {
        "ImportId": str,
        "Destinations": List[str],
        "ImportSource": ImportSourceTypeDef,
        "StartEventTime": datetime,
        "EndEventTime": datetime,
        "ImportStatus": ImportStatusType,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopImportResponseTypeDef = TypedDict(
    "StopImportResponseTypeDef",
    {
        "ImportId": str,
        "ImportSource": ImportSourceTypeDef,
        "Destinations": List[str],
        "ImportStatus": ImportStatusType,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "StartEventTime": datetime,
        "EndEventTime": datetime,
        "ImportStatistics": ImportStatisticsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEventDataStoresResponseTypeDef = TypedDict(
    "ListEventDataStoresResponseTypeDef",
    {
        "EventDataStores": List[EventDataStoreTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetChannelResponseTypeDef = TypedDict(
    "GetChannelResponseTypeDef",
    {
        "ChannelArn": str,
        "Name": str,
        "Source": str,
        "SourceConfig": SourceConfigTypeDef,
        "Destinations": List[DestinationTypeDef],
        "IngestionStatus": IngestionStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AdvancedEventSelectorUnionTypeDef = Union[
    AdvancedEventSelectorTypeDef, AdvancedEventSelectorOutputTypeDef
]
UpdateEventDataStoreRequestRequestTypeDef = TypedDict(
    "UpdateEventDataStoreRequestRequestTypeDef",
    {
        "EventDataStore": str,
        "Name": NotRequired[str],
        "AdvancedEventSelectors": NotRequired[Sequence[AdvancedEventSelectorTypeDef]],
        "MultiRegionEnabled": NotRequired[bool],
        "OrganizationEnabled": NotRequired[bool],
        "RetentionPeriod": NotRequired[int],
        "TerminationProtectionEnabled": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "BillingMode": NotRequired[BillingModeType],
    },
)
EventSelectorUnionTypeDef = Union[EventSelectorTypeDef, EventSelectorOutputTypeDef]
CreateEventDataStoreRequestRequestTypeDef = TypedDict(
    "CreateEventDataStoreRequestRequestTypeDef",
    {
        "Name": str,
        "AdvancedEventSelectors": NotRequired[Sequence[AdvancedEventSelectorUnionTypeDef]],
        "MultiRegionEnabled": NotRequired[bool],
        "OrganizationEnabled": NotRequired[bool],
        "RetentionPeriod": NotRequired[int],
        "TerminationProtectionEnabled": NotRequired[bool],
        "TagsList": NotRequired[Sequence[TagTypeDef]],
        "KmsKeyId": NotRequired[str],
        "StartIngestion": NotRequired[bool],
        "BillingMode": NotRequired[BillingModeType],
    },
)
PutEventSelectorsRequestRequestTypeDef = TypedDict(
    "PutEventSelectorsRequestRequestTypeDef",
    {
        "TrailName": str,
        "EventSelectors": NotRequired[Sequence[EventSelectorUnionTypeDef]],
        "AdvancedEventSelectors": NotRequired[Sequence[AdvancedEventSelectorTypeDef]],
    },
)
