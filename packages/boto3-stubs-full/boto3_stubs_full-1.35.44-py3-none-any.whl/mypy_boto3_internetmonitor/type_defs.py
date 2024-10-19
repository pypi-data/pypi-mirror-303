"""
Type annotations for internetmonitor service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/type_defs/)

Usage::

    ```python
    from mypy_boto3_internetmonitor.type_defs import AvailabilityMeasurementTypeDef

    data: AvailabilityMeasurementTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    HealthEventImpactTypeType,
    HealthEventStatusType,
    InternetEventStatusType,
    InternetEventTypeType,
    LocalHealthEventsConfigStatusType,
    LogDeliveryStatusType,
    MonitorConfigStateType,
    MonitorProcessingStatusCodeType,
    OperatorType,
    QueryStatusType,
    QueryTypeType,
    TriangulationEventTypeType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "AvailabilityMeasurementTypeDef",
    "ClientLocationTypeDef",
    "ResponseMetadataTypeDef",
    "DeleteMonitorInputRequestTypeDef",
    "FilterParameterTypeDef",
    "GetHealthEventInputRequestTypeDef",
    "GetInternetEventInputRequestTypeDef",
    "GetMonitorInputRequestTypeDef",
    "GetQueryResultsInputRequestTypeDef",
    "QueryFieldTypeDef",
    "GetQueryStatusInputRequestTypeDef",
    "LocalHealthEventsConfigTypeDef",
    "S3ConfigTypeDef",
    "PaginatorConfigTypeDef",
    "TimestampTypeDef",
    "ListMonitorsInputRequestTypeDef",
    "MonitorTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "NetworkTypeDef",
    "RoundTripTimeTypeDef",
    "StopQueryInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "InternetEventSummaryTypeDef",
    "CreateMonitorOutputTypeDef",
    "GetInternetEventOutputTypeDef",
    "GetQueryStatusOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "StartQueryOutputTypeDef",
    "UpdateMonitorOutputTypeDef",
    "GetQueryResultsOutputTypeDef",
    "HealthEventsConfigTypeDef",
    "InternetMeasurementsLogDeliveryTypeDef",
    "ListMonitorsInputListMonitorsPaginateTypeDef",
    "ListHealthEventsInputListHealthEventsPaginateTypeDef",
    "ListHealthEventsInputRequestTypeDef",
    "ListInternetEventsInputListInternetEventsPaginateTypeDef",
    "ListInternetEventsInputRequestTypeDef",
    "StartQueryInputRequestTypeDef",
    "ListMonitorsOutputTypeDef",
    "NetworkImpairmentTypeDef",
    "PerformanceMeasurementTypeDef",
    "ListInternetEventsOutputTypeDef",
    "CreateMonitorInputRequestTypeDef",
    "GetMonitorOutputTypeDef",
    "UpdateMonitorInputRequestTypeDef",
    "InternetHealthTypeDef",
    "ImpactedLocationTypeDef",
    "GetHealthEventOutputTypeDef",
    "HealthEventTypeDef",
    "ListHealthEventsOutputTypeDef",
)

AvailabilityMeasurementTypeDef = TypedDict(
    "AvailabilityMeasurementTypeDef",
    {
        "ExperienceScore": NotRequired[float],
        "PercentOfTotalTrafficImpacted": NotRequired[float],
        "PercentOfClientLocationImpacted": NotRequired[float],
    },
)
ClientLocationTypeDef = TypedDict(
    "ClientLocationTypeDef",
    {
        "ASName": str,
        "ASNumber": int,
        "Country": str,
        "City": str,
        "Latitude": float,
        "Longitude": float,
        "Subdivision": NotRequired[str],
        "Metro": NotRequired[str],
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
DeleteMonitorInputRequestTypeDef = TypedDict(
    "DeleteMonitorInputRequestTypeDef",
    {
        "MonitorName": str,
    },
)
FilterParameterTypeDef = TypedDict(
    "FilterParameterTypeDef",
    {
        "Field": NotRequired[str],
        "Operator": NotRequired[OperatorType],
        "Values": NotRequired[Sequence[str]],
    },
)
GetHealthEventInputRequestTypeDef = TypedDict(
    "GetHealthEventInputRequestTypeDef",
    {
        "MonitorName": str,
        "EventId": str,
        "LinkedAccountId": NotRequired[str],
    },
)
GetInternetEventInputRequestTypeDef = TypedDict(
    "GetInternetEventInputRequestTypeDef",
    {
        "EventId": str,
    },
)
GetMonitorInputRequestTypeDef = TypedDict(
    "GetMonitorInputRequestTypeDef",
    {
        "MonitorName": str,
        "LinkedAccountId": NotRequired[str],
    },
)
GetQueryResultsInputRequestTypeDef = TypedDict(
    "GetQueryResultsInputRequestTypeDef",
    {
        "MonitorName": str,
        "QueryId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
QueryFieldTypeDef = TypedDict(
    "QueryFieldTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
    },
)
GetQueryStatusInputRequestTypeDef = TypedDict(
    "GetQueryStatusInputRequestTypeDef",
    {
        "MonitorName": str,
        "QueryId": str,
    },
)
LocalHealthEventsConfigTypeDef = TypedDict(
    "LocalHealthEventsConfigTypeDef",
    {
        "Status": NotRequired[LocalHealthEventsConfigStatusType],
        "HealthScoreThreshold": NotRequired[float],
        "MinTrafficImpact": NotRequired[float],
    },
)
S3ConfigTypeDef = TypedDict(
    "S3ConfigTypeDef",
    {
        "BucketName": NotRequired[str],
        "BucketPrefix": NotRequired[str],
        "LogDeliveryStatus": NotRequired[LogDeliveryStatusType],
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
TimestampTypeDef = Union[datetime, str]
ListMonitorsInputRequestTypeDef = TypedDict(
    "ListMonitorsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "MonitorStatus": NotRequired[str],
        "IncludeLinkedAccounts": NotRequired[bool],
    },
)
MonitorTypeDef = TypedDict(
    "MonitorTypeDef",
    {
        "MonitorName": str,
        "MonitorArn": str,
        "Status": MonitorConfigStateType,
        "ProcessingStatus": NotRequired[MonitorProcessingStatusCodeType],
    },
)
ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
NetworkTypeDef = TypedDict(
    "NetworkTypeDef",
    {
        "ASName": str,
        "ASNumber": int,
    },
)
RoundTripTimeTypeDef = TypedDict(
    "RoundTripTimeTypeDef",
    {
        "P50": NotRequired[float],
        "P90": NotRequired[float],
        "P95": NotRequired[float],
    },
)
StopQueryInputRequestTypeDef = TypedDict(
    "StopQueryInputRequestTypeDef",
    {
        "MonitorName": str,
        "QueryId": str,
    },
)
TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
InternetEventSummaryTypeDef = TypedDict(
    "InternetEventSummaryTypeDef",
    {
        "EventId": str,
        "EventArn": str,
        "StartedAt": datetime,
        "ClientLocation": ClientLocationTypeDef,
        "EventType": InternetEventTypeType,
        "EventStatus": InternetEventStatusType,
        "EndedAt": NotRequired[datetime],
    },
)
CreateMonitorOutputTypeDef = TypedDict(
    "CreateMonitorOutputTypeDef",
    {
        "Arn": str,
        "Status": MonitorConfigStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetInternetEventOutputTypeDef = TypedDict(
    "GetInternetEventOutputTypeDef",
    {
        "EventId": str,
        "EventArn": str,
        "StartedAt": datetime,
        "EndedAt": datetime,
        "ClientLocation": ClientLocationTypeDef,
        "EventType": InternetEventTypeType,
        "EventStatus": InternetEventStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetQueryStatusOutputTypeDef = TypedDict(
    "GetQueryStatusOutputTypeDef",
    {
        "Status": QueryStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartQueryOutputTypeDef = TypedDict(
    "StartQueryOutputTypeDef",
    {
        "QueryId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateMonitorOutputTypeDef = TypedDict(
    "UpdateMonitorOutputTypeDef",
    {
        "MonitorArn": str,
        "Status": MonitorConfigStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetQueryResultsOutputTypeDef = TypedDict(
    "GetQueryResultsOutputTypeDef",
    {
        "Fields": List[QueryFieldTypeDef],
        "Data": List[List[str]],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
HealthEventsConfigTypeDef = TypedDict(
    "HealthEventsConfigTypeDef",
    {
        "AvailabilityScoreThreshold": NotRequired[float],
        "PerformanceScoreThreshold": NotRequired[float],
        "AvailabilityLocalHealthEventsConfig": NotRequired[LocalHealthEventsConfigTypeDef],
        "PerformanceLocalHealthEventsConfig": NotRequired[LocalHealthEventsConfigTypeDef],
    },
)
InternetMeasurementsLogDeliveryTypeDef = TypedDict(
    "InternetMeasurementsLogDeliveryTypeDef",
    {
        "S3Config": NotRequired[S3ConfigTypeDef],
    },
)
ListMonitorsInputListMonitorsPaginateTypeDef = TypedDict(
    "ListMonitorsInputListMonitorsPaginateTypeDef",
    {
        "MonitorStatus": NotRequired[str],
        "IncludeLinkedAccounts": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListHealthEventsInputListHealthEventsPaginateTypeDef = TypedDict(
    "ListHealthEventsInputListHealthEventsPaginateTypeDef",
    {
        "MonitorName": str,
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "EventStatus": NotRequired[HealthEventStatusType],
        "LinkedAccountId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListHealthEventsInputRequestTypeDef = TypedDict(
    "ListHealthEventsInputRequestTypeDef",
    {
        "MonitorName": str,
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "EventStatus": NotRequired[HealthEventStatusType],
        "LinkedAccountId": NotRequired[str],
    },
)
ListInternetEventsInputListInternetEventsPaginateTypeDef = TypedDict(
    "ListInternetEventsInputListInternetEventsPaginateTypeDef",
    {
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "EventStatus": NotRequired[str],
        "EventType": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListInternetEventsInputRequestTypeDef = TypedDict(
    "ListInternetEventsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "EventStatus": NotRequired[str],
        "EventType": NotRequired[str],
    },
)
StartQueryInputRequestTypeDef = TypedDict(
    "StartQueryInputRequestTypeDef",
    {
        "MonitorName": str,
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
        "QueryType": QueryTypeType,
        "FilterParameters": NotRequired[Sequence[FilterParameterTypeDef]],
        "LinkedAccountId": NotRequired[str],
    },
)
ListMonitorsOutputTypeDef = TypedDict(
    "ListMonitorsOutputTypeDef",
    {
        "Monitors": List[MonitorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
NetworkImpairmentTypeDef = TypedDict(
    "NetworkImpairmentTypeDef",
    {
        "Networks": List[NetworkTypeDef],
        "AsPath": List[NetworkTypeDef],
        "NetworkEventType": TriangulationEventTypeType,
    },
)
PerformanceMeasurementTypeDef = TypedDict(
    "PerformanceMeasurementTypeDef",
    {
        "ExperienceScore": NotRequired[float],
        "PercentOfTotalTrafficImpacted": NotRequired[float],
        "PercentOfClientLocationImpacted": NotRequired[float],
        "RoundTripTime": NotRequired[RoundTripTimeTypeDef],
    },
)
ListInternetEventsOutputTypeDef = TypedDict(
    "ListInternetEventsOutputTypeDef",
    {
        "InternetEvents": List[InternetEventSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateMonitorInputRequestTypeDef = TypedDict(
    "CreateMonitorInputRequestTypeDef",
    {
        "MonitorName": str,
        "Resources": NotRequired[Sequence[str]],
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "MaxCityNetworksToMonitor": NotRequired[int],
        "InternetMeasurementsLogDelivery": NotRequired[InternetMeasurementsLogDeliveryTypeDef],
        "TrafficPercentageToMonitor": NotRequired[int],
        "HealthEventsConfig": NotRequired[HealthEventsConfigTypeDef],
    },
)
GetMonitorOutputTypeDef = TypedDict(
    "GetMonitorOutputTypeDef",
    {
        "MonitorName": str,
        "MonitorArn": str,
        "Resources": List[str],
        "Status": MonitorConfigStateType,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
        "ProcessingStatus": MonitorProcessingStatusCodeType,
        "ProcessingStatusInfo": str,
        "Tags": Dict[str, str],
        "MaxCityNetworksToMonitor": int,
        "InternetMeasurementsLogDelivery": InternetMeasurementsLogDeliveryTypeDef,
        "TrafficPercentageToMonitor": int,
        "HealthEventsConfig": HealthEventsConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateMonitorInputRequestTypeDef = TypedDict(
    "UpdateMonitorInputRequestTypeDef",
    {
        "MonitorName": str,
        "ResourcesToAdd": NotRequired[Sequence[str]],
        "ResourcesToRemove": NotRequired[Sequence[str]],
        "Status": NotRequired[MonitorConfigStateType],
        "ClientToken": NotRequired[str],
        "MaxCityNetworksToMonitor": NotRequired[int],
        "InternetMeasurementsLogDelivery": NotRequired[InternetMeasurementsLogDeliveryTypeDef],
        "TrafficPercentageToMonitor": NotRequired[int],
        "HealthEventsConfig": NotRequired[HealthEventsConfigTypeDef],
    },
)
InternetHealthTypeDef = TypedDict(
    "InternetHealthTypeDef",
    {
        "Availability": NotRequired[AvailabilityMeasurementTypeDef],
        "Performance": NotRequired[PerformanceMeasurementTypeDef],
    },
)
ImpactedLocationTypeDef = TypedDict(
    "ImpactedLocationTypeDef",
    {
        "ASName": str,
        "ASNumber": int,
        "Country": str,
        "Status": HealthEventStatusType,
        "Subdivision": NotRequired[str],
        "Metro": NotRequired[str],
        "City": NotRequired[str],
        "Latitude": NotRequired[float],
        "Longitude": NotRequired[float],
        "CountryCode": NotRequired[str],
        "SubdivisionCode": NotRequired[str],
        "ServiceLocation": NotRequired[str],
        "CausedBy": NotRequired[NetworkImpairmentTypeDef],
        "InternetHealth": NotRequired[InternetHealthTypeDef],
        "Ipv4Prefixes": NotRequired[List[str]],
    },
)
GetHealthEventOutputTypeDef = TypedDict(
    "GetHealthEventOutputTypeDef",
    {
        "EventArn": str,
        "EventId": str,
        "StartedAt": datetime,
        "EndedAt": datetime,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "ImpactedLocations": List[ImpactedLocationTypeDef],
        "Status": HealthEventStatusType,
        "PercentOfTotalTrafficImpacted": float,
        "ImpactType": HealthEventImpactTypeType,
        "HealthScoreThreshold": float,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
HealthEventTypeDef = TypedDict(
    "HealthEventTypeDef",
    {
        "EventArn": str,
        "EventId": str,
        "StartedAt": datetime,
        "LastUpdatedAt": datetime,
        "ImpactedLocations": List[ImpactedLocationTypeDef],
        "Status": HealthEventStatusType,
        "ImpactType": HealthEventImpactTypeType,
        "EndedAt": NotRequired[datetime],
        "CreatedAt": NotRequired[datetime],
        "PercentOfTotalTrafficImpacted": NotRequired[float],
        "HealthScoreThreshold": NotRequired[float],
    },
)
ListHealthEventsOutputTypeDef = TypedDict(
    "ListHealthEventsOutputTypeDef",
    {
        "HealthEvents": List[HealthEventTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
