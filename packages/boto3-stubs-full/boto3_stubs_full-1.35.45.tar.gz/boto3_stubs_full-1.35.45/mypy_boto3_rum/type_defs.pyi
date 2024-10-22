"""
Type annotations for rum service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/type_defs/)

Usage::

    ```python
    from mypy_boto3_rum.type_defs import AppMonitorConfigurationOutputTypeDef

    data: AppMonitorConfigurationOutputTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import CustomEventsStatusType, MetricDestinationType, StateEnumType, TelemetryType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AppMonitorConfigurationOutputTypeDef",
    "AppMonitorConfigurationTypeDef",
    "AppMonitorDetailsTypeDef",
    "AppMonitorSummaryTypeDef",
    "CustomEventsTypeDef",
    "MetricDefinitionRequestOutputTypeDef",
    "MetricDefinitionTypeDef",
    "ResponseMetadataTypeDef",
    "BatchDeleteRumMetricDefinitionsErrorTypeDef",
    "BatchDeleteRumMetricDefinitionsRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "BatchGetRumMetricDefinitionsRequestRequestTypeDef",
    "CwLogTypeDef",
    "DeleteAppMonitorRequestRequestTypeDef",
    "DeleteRumMetricsDestinationRequestRequestTypeDef",
    "QueryFilterTypeDef",
    "TimeRangeTypeDef",
    "GetAppMonitorRequestRequestTypeDef",
    "ListAppMonitorsRequestRequestTypeDef",
    "ListRumMetricsDestinationsRequestRequestTypeDef",
    "MetricDestinationSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "MetricDefinitionRequestTypeDef",
    "UserDetailsTypeDef",
    "PutRumMetricsDestinationRequestRequestTypeDef",
    "TimestampTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "CreateAppMonitorRequestRequestTypeDef",
    "UpdateAppMonitorRequestRequestTypeDef",
    "BatchCreateRumMetricDefinitionsErrorTypeDef",
    "BatchGetRumMetricDefinitionsResponseTypeDef",
    "CreateAppMonitorResponseTypeDef",
    "GetAppMonitorDataResponseTypeDef",
    "ListAppMonitorsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "BatchDeleteRumMetricDefinitionsResponseTypeDef",
    "BatchGetRumMetricDefinitionsRequestBatchGetRumMetricDefinitionsPaginateTypeDef",
    "ListAppMonitorsRequestListAppMonitorsPaginateTypeDef",
    "ListRumMetricsDestinationsRequestListRumMetricsDestinationsPaginateTypeDef",
    "DataStorageTypeDef",
    "GetAppMonitorDataRequestGetAppMonitorDataPaginateTypeDef",
    "GetAppMonitorDataRequestRequestTypeDef",
    "ListRumMetricsDestinationsResponseTypeDef",
    "MetricDefinitionRequestUnionTypeDef",
    "UpdateRumMetricDefinitionRequestRequestTypeDef",
    "RumEventTypeDef",
    "BatchCreateRumMetricDefinitionsResponseTypeDef",
    "AppMonitorTypeDef",
    "BatchCreateRumMetricDefinitionsRequestRequestTypeDef",
    "PutRumEventsRequestRequestTypeDef",
    "GetAppMonitorResponseTypeDef",
)

AppMonitorConfigurationOutputTypeDef = TypedDict(
    "AppMonitorConfigurationOutputTypeDef",
    {
        "AllowCookies": NotRequired[bool],
        "EnableXRay": NotRequired[bool],
        "ExcludedPages": NotRequired[List[str]],
        "FavoritePages": NotRequired[List[str]],
        "GuestRoleArn": NotRequired[str],
        "IdentityPoolId": NotRequired[str],
        "IncludedPages": NotRequired[List[str]],
        "SessionSampleRate": NotRequired[float],
        "Telemetries": NotRequired[List[TelemetryType]],
    },
)
AppMonitorConfigurationTypeDef = TypedDict(
    "AppMonitorConfigurationTypeDef",
    {
        "AllowCookies": NotRequired[bool],
        "EnableXRay": NotRequired[bool],
        "ExcludedPages": NotRequired[Sequence[str]],
        "FavoritePages": NotRequired[Sequence[str]],
        "GuestRoleArn": NotRequired[str],
        "IdentityPoolId": NotRequired[str],
        "IncludedPages": NotRequired[Sequence[str]],
        "SessionSampleRate": NotRequired[float],
        "Telemetries": NotRequired[Sequence[TelemetryType]],
    },
)
AppMonitorDetailsTypeDef = TypedDict(
    "AppMonitorDetailsTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "version": NotRequired[str],
    },
)
AppMonitorSummaryTypeDef = TypedDict(
    "AppMonitorSummaryTypeDef",
    {
        "Created": NotRequired[str],
        "Id": NotRequired[str],
        "LastModified": NotRequired[str],
        "Name": NotRequired[str],
        "State": NotRequired[StateEnumType],
    },
)
CustomEventsTypeDef = TypedDict(
    "CustomEventsTypeDef",
    {
        "Status": NotRequired[CustomEventsStatusType],
    },
)
MetricDefinitionRequestOutputTypeDef = TypedDict(
    "MetricDefinitionRequestOutputTypeDef",
    {
        "Name": str,
        "DimensionKeys": NotRequired[Dict[str, str]],
        "EventPattern": NotRequired[str],
        "Namespace": NotRequired[str],
        "UnitLabel": NotRequired[str],
        "ValueKey": NotRequired[str],
    },
)
MetricDefinitionTypeDef = TypedDict(
    "MetricDefinitionTypeDef",
    {
        "MetricDefinitionId": str,
        "Name": str,
        "DimensionKeys": NotRequired[Dict[str, str]],
        "EventPattern": NotRequired[str],
        "Namespace": NotRequired[str],
        "UnitLabel": NotRequired[str],
        "ValueKey": NotRequired[str],
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
BatchDeleteRumMetricDefinitionsErrorTypeDef = TypedDict(
    "BatchDeleteRumMetricDefinitionsErrorTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
        "MetricDefinitionId": str,
    },
)
BatchDeleteRumMetricDefinitionsRequestRequestTypeDef = TypedDict(
    "BatchDeleteRumMetricDefinitionsRequestRequestTypeDef",
    {
        "AppMonitorName": str,
        "Destination": MetricDestinationType,
        "MetricDefinitionIds": Sequence[str],
        "DestinationArn": NotRequired[str],
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
BatchGetRumMetricDefinitionsRequestRequestTypeDef = TypedDict(
    "BatchGetRumMetricDefinitionsRequestRequestTypeDef",
    {
        "AppMonitorName": str,
        "Destination": MetricDestinationType,
        "DestinationArn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
CwLogTypeDef = TypedDict(
    "CwLogTypeDef",
    {
        "CwLogEnabled": NotRequired[bool],
        "CwLogGroup": NotRequired[str],
    },
)
DeleteAppMonitorRequestRequestTypeDef = TypedDict(
    "DeleteAppMonitorRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteRumMetricsDestinationRequestRequestTypeDef = TypedDict(
    "DeleteRumMetricsDestinationRequestRequestTypeDef",
    {
        "AppMonitorName": str,
        "Destination": MetricDestinationType,
        "DestinationArn": NotRequired[str],
    },
)
QueryFilterTypeDef = TypedDict(
    "QueryFilterTypeDef",
    {
        "Name": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)
TimeRangeTypeDef = TypedDict(
    "TimeRangeTypeDef",
    {
        "After": int,
        "Before": NotRequired[int],
    },
)
GetAppMonitorRequestRequestTypeDef = TypedDict(
    "GetAppMonitorRequestRequestTypeDef",
    {
        "Name": str,
    },
)
ListAppMonitorsRequestRequestTypeDef = TypedDict(
    "ListAppMonitorsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListRumMetricsDestinationsRequestRequestTypeDef = TypedDict(
    "ListRumMetricsDestinationsRequestRequestTypeDef",
    {
        "AppMonitorName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
MetricDestinationSummaryTypeDef = TypedDict(
    "MetricDestinationSummaryTypeDef",
    {
        "Destination": NotRequired[MetricDestinationType],
        "DestinationArn": NotRequired[str],
        "IamRoleArn": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
MetricDefinitionRequestTypeDef = TypedDict(
    "MetricDefinitionRequestTypeDef",
    {
        "Name": str,
        "DimensionKeys": NotRequired[Mapping[str, str]],
        "EventPattern": NotRequired[str],
        "Namespace": NotRequired[str],
        "UnitLabel": NotRequired[str],
        "ValueKey": NotRequired[str],
    },
)
UserDetailsTypeDef = TypedDict(
    "UserDetailsTypeDef",
    {
        "sessionId": NotRequired[str],
        "userId": NotRequired[str],
    },
)
PutRumMetricsDestinationRequestRequestTypeDef = TypedDict(
    "PutRumMetricsDestinationRequestRequestTypeDef",
    {
        "AppMonitorName": str,
        "Destination": MetricDestinationType,
        "DestinationArn": NotRequired[str],
        "IamRoleArn": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
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
CreateAppMonitorRequestRequestTypeDef = TypedDict(
    "CreateAppMonitorRequestRequestTypeDef",
    {
        "Domain": str,
        "Name": str,
        "AppMonitorConfiguration": NotRequired[AppMonitorConfigurationTypeDef],
        "CustomEvents": NotRequired[CustomEventsTypeDef],
        "CwLogEnabled": NotRequired[bool],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
UpdateAppMonitorRequestRequestTypeDef = TypedDict(
    "UpdateAppMonitorRequestRequestTypeDef",
    {
        "Name": str,
        "AppMonitorConfiguration": NotRequired[AppMonitorConfigurationTypeDef],
        "CustomEvents": NotRequired[CustomEventsTypeDef],
        "CwLogEnabled": NotRequired[bool],
        "Domain": NotRequired[str],
    },
)
BatchCreateRumMetricDefinitionsErrorTypeDef = TypedDict(
    "BatchCreateRumMetricDefinitionsErrorTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
        "MetricDefinition": MetricDefinitionRequestOutputTypeDef,
    },
)
BatchGetRumMetricDefinitionsResponseTypeDef = TypedDict(
    "BatchGetRumMetricDefinitionsResponseTypeDef",
    {
        "MetricDefinitions": List[MetricDefinitionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateAppMonitorResponseTypeDef = TypedDict(
    "CreateAppMonitorResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAppMonitorDataResponseTypeDef = TypedDict(
    "GetAppMonitorDataResponseTypeDef",
    {
        "Events": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListAppMonitorsResponseTypeDef = TypedDict(
    "ListAppMonitorsResponseTypeDef",
    {
        "AppMonitorSummaries": List[AppMonitorSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDeleteRumMetricDefinitionsResponseTypeDef = TypedDict(
    "BatchDeleteRumMetricDefinitionsResponseTypeDef",
    {
        "Errors": List[BatchDeleteRumMetricDefinitionsErrorTypeDef],
        "MetricDefinitionIds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetRumMetricDefinitionsRequestBatchGetRumMetricDefinitionsPaginateTypeDef = TypedDict(
    "BatchGetRumMetricDefinitionsRequestBatchGetRumMetricDefinitionsPaginateTypeDef",
    {
        "AppMonitorName": str,
        "Destination": MetricDestinationType,
        "DestinationArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAppMonitorsRequestListAppMonitorsPaginateTypeDef = TypedDict(
    "ListAppMonitorsRequestListAppMonitorsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRumMetricsDestinationsRequestListRumMetricsDestinationsPaginateTypeDef = TypedDict(
    "ListRumMetricsDestinationsRequestListRumMetricsDestinationsPaginateTypeDef",
    {
        "AppMonitorName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DataStorageTypeDef = TypedDict(
    "DataStorageTypeDef",
    {
        "CwLog": NotRequired[CwLogTypeDef],
    },
)
GetAppMonitorDataRequestGetAppMonitorDataPaginateTypeDef = TypedDict(
    "GetAppMonitorDataRequestGetAppMonitorDataPaginateTypeDef",
    {
        "Name": str,
        "TimeRange": TimeRangeTypeDef,
        "Filters": NotRequired[Sequence[QueryFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetAppMonitorDataRequestRequestTypeDef = TypedDict(
    "GetAppMonitorDataRequestRequestTypeDef",
    {
        "Name": str,
        "TimeRange": TimeRangeTypeDef,
        "Filters": NotRequired[Sequence[QueryFilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListRumMetricsDestinationsResponseTypeDef = TypedDict(
    "ListRumMetricsDestinationsResponseTypeDef",
    {
        "Destinations": List[MetricDestinationSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
MetricDefinitionRequestUnionTypeDef = Union[
    MetricDefinitionRequestTypeDef, MetricDefinitionRequestOutputTypeDef
]
UpdateRumMetricDefinitionRequestRequestTypeDef = TypedDict(
    "UpdateRumMetricDefinitionRequestRequestTypeDef",
    {
        "AppMonitorName": str,
        "Destination": MetricDestinationType,
        "MetricDefinition": MetricDefinitionRequestTypeDef,
        "MetricDefinitionId": str,
        "DestinationArn": NotRequired[str],
    },
)
RumEventTypeDef = TypedDict(
    "RumEventTypeDef",
    {
        "details": str,
        "id": str,
        "timestamp": TimestampTypeDef,
        "type": str,
        "metadata": NotRequired[str],
    },
)
BatchCreateRumMetricDefinitionsResponseTypeDef = TypedDict(
    "BatchCreateRumMetricDefinitionsResponseTypeDef",
    {
        "Errors": List[BatchCreateRumMetricDefinitionsErrorTypeDef],
        "MetricDefinitions": List[MetricDefinitionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AppMonitorTypeDef = TypedDict(
    "AppMonitorTypeDef",
    {
        "AppMonitorConfiguration": NotRequired[AppMonitorConfigurationOutputTypeDef],
        "Created": NotRequired[str],
        "CustomEvents": NotRequired[CustomEventsTypeDef],
        "DataStorage": NotRequired[DataStorageTypeDef],
        "Domain": NotRequired[str],
        "Id": NotRequired[str],
        "LastModified": NotRequired[str],
        "Name": NotRequired[str],
        "State": NotRequired[StateEnumType],
        "Tags": NotRequired[Dict[str, str]],
    },
)
BatchCreateRumMetricDefinitionsRequestRequestTypeDef = TypedDict(
    "BatchCreateRumMetricDefinitionsRequestRequestTypeDef",
    {
        "AppMonitorName": str,
        "Destination": MetricDestinationType,
        "MetricDefinitions": Sequence[MetricDefinitionRequestUnionTypeDef],
        "DestinationArn": NotRequired[str],
    },
)
PutRumEventsRequestRequestTypeDef = TypedDict(
    "PutRumEventsRequestRequestTypeDef",
    {
        "AppMonitorDetails": AppMonitorDetailsTypeDef,
        "BatchId": str,
        "Id": str,
        "RumEvents": Sequence[RumEventTypeDef],
        "UserDetails": UserDetailsTypeDef,
    },
)
GetAppMonitorResponseTypeDef = TypedDict(
    "GetAppMonitorResponseTypeDef",
    {
        "AppMonitor": AppMonitorTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
