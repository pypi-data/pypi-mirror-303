"""
Type annotations for location service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_location/type_defs/)

Usage::

    ```python
    from mypy_boto3_location.type_defs import ApiKeyFilterTypeDef

    data: ApiKeyFilterTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    BatchItemErrorCodeType,
    DimensionUnitType,
    DistanceUnitType,
    ForecastedGeofenceEventTypeType,
    IntendedUseType,
    OptimizationModeType,
    PositionFilteringType,
    PricingPlanType,
    RouteMatrixErrorCodeType,
    SpeedUnitType,
    StatusType,
    TravelModeType,
    VehicleWeightUnitType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "ApiKeyFilterTypeDef",
    "ApiKeyRestrictionsOutputTypeDef",
    "ApiKeyRestrictionsTypeDef",
    "AssociateTrackerConsumerRequestRequestTypeDef",
    "BatchItemErrorTypeDef",
    "BatchDeleteDevicePositionHistoryRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "BatchDeleteGeofenceRequestRequestTypeDef",
    "BatchGetDevicePositionRequestRequestTypeDef",
    "BatchPutGeofenceSuccessTypeDef",
    "BlobTypeDef",
    "CalculateRouteCarModeOptionsTypeDef",
    "TimestampTypeDef",
    "CalculateRouteMatrixSummaryTypeDef",
    "CalculateRouteSummaryTypeDef",
    "TruckDimensionsTypeDef",
    "TruckWeightTypeDef",
    "CircleOutputTypeDef",
    "CircleTypeDef",
    "CreateGeofenceCollectionRequestRequestTypeDef",
    "MapConfigurationTypeDef",
    "DataSourceConfigurationTypeDef",
    "CreateRouteCalculatorRequestRequestTypeDef",
    "CreateTrackerRequestRequestTypeDef",
    "DeleteGeofenceCollectionRequestRequestTypeDef",
    "DeleteKeyRequestRequestTypeDef",
    "DeleteMapRequestRequestTypeDef",
    "DeletePlaceIndexRequestRequestTypeDef",
    "DeleteRouteCalculatorRequestRequestTypeDef",
    "DeleteTrackerRequestRequestTypeDef",
    "DescribeGeofenceCollectionRequestRequestTypeDef",
    "DescribeKeyRequestRequestTypeDef",
    "DescribeMapRequestRequestTypeDef",
    "MapConfigurationOutputTypeDef",
    "DescribePlaceIndexRequestRequestTypeDef",
    "DescribeRouteCalculatorRequestRequestTypeDef",
    "DescribeTrackerRequestRequestTypeDef",
    "PositionalAccuracyTypeDef",
    "WiFiAccessPointTypeDef",
    "DisassociateTrackerConsumerRequestRequestTypeDef",
    "ForecastGeofenceEventsDeviceStateTypeDef",
    "PaginatorConfigTypeDef",
    "ForecastedEventTypeDef",
    "GetDevicePositionRequestRequestTypeDef",
    "GetGeofenceRequestRequestTypeDef",
    "GetMapGlyphsRequestRequestTypeDef",
    "GetMapSpritesRequestRequestTypeDef",
    "GetMapStyleDescriptorRequestRequestTypeDef",
    "GetMapTileRequestRequestTypeDef",
    "GetPlaceRequestRequestTypeDef",
    "LegGeometryTypeDef",
    "StepTypeDef",
    "TrackingFilterGeometryTypeDef",
    "ListGeofenceCollectionsRequestRequestTypeDef",
    "ListGeofenceCollectionsResponseEntryTypeDef",
    "ListGeofencesRequestRequestTypeDef",
    "ListMapsRequestRequestTypeDef",
    "ListMapsResponseEntryTypeDef",
    "ListPlaceIndexesRequestRequestTypeDef",
    "ListPlaceIndexesResponseEntryTypeDef",
    "ListRouteCalculatorsRequestRequestTypeDef",
    "ListRouteCalculatorsResponseEntryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTrackerConsumersRequestRequestTypeDef",
    "ListTrackersRequestRequestTypeDef",
    "ListTrackersResponseEntryTypeDef",
    "LteLocalIdTypeDef",
    "LteNetworkMeasurementsTypeDef",
    "MapConfigurationUpdateTypeDef",
    "PlaceGeometryTypeDef",
    "TimeZoneTypeDef",
    "RouteMatrixEntryErrorTypeDef",
    "SearchForSuggestionsResultTypeDef",
    "SearchPlaceIndexForPositionRequestRequestTypeDef",
    "SearchPlaceIndexForPositionSummaryTypeDef",
    "SearchPlaceIndexForSuggestionsRequestRequestTypeDef",
    "SearchPlaceIndexForSuggestionsSummaryTypeDef",
    "SearchPlaceIndexForTextRequestRequestTypeDef",
    "SearchPlaceIndexForTextSummaryTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateGeofenceCollectionRequestRequestTypeDef",
    "UpdateRouteCalculatorRequestRequestTypeDef",
    "UpdateTrackerRequestRequestTypeDef",
    "ListKeysRequestRequestTypeDef",
    "ListKeysResponseEntryTypeDef",
    "BatchDeleteDevicePositionHistoryErrorTypeDef",
    "BatchDeleteGeofenceErrorTypeDef",
    "BatchEvaluateGeofencesErrorTypeDef",
    "BatchGetDevicePositionErrorTypeDef",
    "BatchPutGeofenceErrorTypeDef",
    "BatchUpdateDevicePositionErrorTypeDef",
    "CreateGeofenceCollectionResponseTypeDef",
    "CreateKeyResponseTypeDef",
    "CreateMapResponseTypeDef",
    "CreatePlaceIndexResponseTypeDef",
    "CreateRouteCalculatorResponseTypeDef",
    "CreateTrackerResponseTypeDef",
    "DescribeGeofenceCollectionResponseTypeDef",
    "DescribeKeyResponseTypeDef",
    "DescribeRouteCalculatorResponseTypeDef",
    "DescribeTrackerResponseTypeDef",
    "GetMapGlyphsResponseTypeDef",
    "GetMapSpritesResponseTypeDef",
    "GetMapStyleDescriptorResponseTypeDef",
    "GetMapTileResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTrackerConsumersResponseTypeDef",
    "PutGeofenceResponseTypeDef",
    "UpdateGeofenceCollectionResponseTypeDef",
    "UpdateKeyResponseTypeDef",
    "UpdateMapResponseTypeDef",
    "UpdatePlaceIndexResponseTypeDef",
    "UpdateRouteCalculatorResponseTypeDef",
    "UpdateTrackerResponseTypeDef",
    "CreateKeyRequestRequestTypeDef",
    "GetDevicePositionHistoryRequestRequestTypeDef",
    "UpdateKeyRequestRequestTypeDef",
    "CalculateRouteTruckModeOptionsTypeDef",
    "GeofenceGeometryOutputTypeDef",
    "CircleUnionTypeDef",
    "CreateMapRequestRequestTypeDef",
    "CreatePlaceIndexRequestRequestTypeDef",
    "DescribePlaceIndexResponseTypeDef",
    "UpdatePlaceIndexRequestRequestTypeDef",
    "DescribeMapResponseTypeDef",
    "DevicePositionTypeDef",
    "DevicePositionUpdateTypeDef",
    "GetDevicePositionResponseTypeDef",
    "InferredStateTypeDef",
    "ListDevicePositionsResponseEntryTypeDef",
    "ForecastGeofenceEventsRequestRequestTypeDef",
    "ForecastGeofenceEventsRequestForecastGeofenceEventsPaginateTypeDef",
    "GetDevicePositionHistoryRequestGetDevicePositionHistoryPaginateTypeDef",
    "ListGeofenceCollectionsRequestListGeofenceCollectionsPaginateTypeDef",
    "ListGeofencesRequestListGeofencesPaginateTypeDef",
    "ListKeysRequestListKeysPaginateTypeDef",
    "ListMapsRequestListMapsPaginateTypeDef",
    "ListPlaceIndexesRequestListPlaceIndexesPaginateTypeDef",
    "ListRouteCalculatorsRequestListRouteCalculatorsPaginateTypeDef",
    "ListTrackerConsumersRequestListTrackerConsumersPaginateTypeDef",
    "ListTrackersRequestListTrackersPaginateTypeDef",
    "ForecastGeofenceEventsResponseTypeDef",
    "LegTypeDef",
    "ListDevicePositionsRequestListDevicePositionsPaginateTypeDef",
    "ListDevicePositionsRequestRequestTypeDef",
    "ListGeofenceCollectionsResponseTypeDef",
    "ListMapsResponseTypeDef",
    "ListPlaceIndexesResponseTypeDef",
    "ListRouteCalculatorsResponseTypeDef",
    "ListTrackersResponseTypeDef",
    "LteCellDetailsTypeDef",
    "UpdateMapRequestRequestTypeDef",
    "PlaceTypeDef",
    "RouteMatrixEntryTypeDef",
    "SearchPlaceIndexForSuggestionsResponseTypeDef",
    "ListKeysResponseTypeDef",
    "BatchDeleteDevicePositionHistoryResponseTypeDef",
    "BatchDeleteGeofenceResponseTypeDef",
    "BatchEvaluateGeofencesResponseTypeDef",
    "BatchPutGeofenceResponseTypeDef",
    "BatchUpdateDevicePositionResponseTypeDef",
    "CalculateRouteMatrixRequestRequestTypeDef",
    "CalculateRouteRequestRequestTypeDef",
    "GetGeofenceResponseTypeDef",
    "ListGeofenceResponseEntryTypeDef",
    "GeofenceGeometryTypeDef",
    "BatchGetDevicePositionResponseTypeDef",
    "GetDevicePositionHistoryResponseTypeDef",
    "BatchEvaluateGeofencesRequestRequestTypeDef",
    "BatchUpdateDevicePositionRequestRequestTypeDef",
    "VerifyDevicePositionResponseTypeDef",
    "ListDevicePositionsResponseTypeDef",
    "CalculateRouteResponseTypeDef",
    "CellSignalsTypeDef",
    "GetPlaceResponseTypeDef",
    "SearchForPositionResultTypeDef",
    "SearchForTextResultTypeDef",
    "CalculateRouteMatrixResponseTypeDef",
    "ListGeofencesResponseTypeDef",
    "GeofenceGeometryUnionTypeDef",
    "PutGeofenceRequestRequestTypeDef",
    "DeviceStateTypeDef",
    "SearchPlaceIndexForPositionResponseTypeDef",
    "SearchPlaceIndexForTextResponseTypeDef",
    "BatchPutGeofenceRequestEntryTypeDef",
    "VerifyDevicePositionRequestRequestTypeDef",
    "BatchPutGeofenceRequestRequestTypeDef",
)

ApiKeyFilterTypeDef = TypedDict(
    "ApiKeyFilterTypeDef",
    {
        "KeyStatus": NotRequired[StatusType],
    },
)
ApiKeyRestrictionsOutputTypeDef = TypedDict(
    "ApiKeyRestrictionsOutputTypeDef",
    {
        "AllowActions": List[str],
        "AllowResources": List[str],
        "AllowReferers": NotRequired[List[str]],
    },
)
ApiKeyRestrictionsTypeDef = TypedDict(
    "ApiKeyRestrictionsTypeDef",
    {
        "AllowActions": Sequence[str],
        "AllowResources": Sequence[str],
        "AllowReferers": NotRequired[Sequence[str]],
    },
)
AssociateTrackerConsumerRequestRequestTypeDef = TypedDict(
    "AssociateTrackerConsumerRequestRequestTypeDef",
    {
        "TrackerName": str,
        "ConsumerArn": str,
    },
)
BatchItemErrorTypeDef = TypedDict(
    "BatchItemErrorTypeDef",
    {
        "Code": NotRequired[BatchItemErrorCodeType],
        "Message": NotRequired[str],
    },
)
BatchDeleteDevicePositionHistoryRequestRequestTypeDef = TypedDict(
    "BatchDeleteDevicePositionHistoryRequestRequestTypeDef",
    {
        "TrackerName": str,
        "DeviceIds": Sequence[str],
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
BatchDeleteGeofenceRequestRequestTypeDef = TypedDict(
    "BatchDeleteGeofenceRequestRequestTypeDef",
    {
        "CollectionName": str,
        "GeofenceIds": Sequence[str],
    },
)
BatchGetDevicePositionRequestRequestTypeDef = TypedDict(
    "BatchGetDevicePositionRequestRequestTypeDef",
    {
        "TrackerName": str,
        "DeviceIds": Sequence[str],
    },
)
BatchPutGeofenceSuccessTypeDef = TypedDict(
    "BatchPutGeofenceSuccessTypeDef",
    {
        "GeofenceId": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
CalculateRouteCarModeOptionsTypeDef = TypedDict(
    "CalculateRouteCarModeOptionsTypeDef",
    {
        "AvoidFerries": NotRequired[bool],
        "AvoidTolls": NotRequired[bool],
    },
)
TimestampTypeDef = Union[datetime, str]
CalculateRouteMatrixSummaryTypeDef = TypedDict(
    "CalculateRouteMatrixSummaryTypeDef",
    {
        "DataSource": str,
        "RouteCount": int,
        "ErrorCount": int,
        "DistanceUnit": DistanceUnitType,
    },
)
CalculateRouteSummaryTypeDef = TypedDict(
    "CalculateRouteSummaryTypeDef",
    {
        "RouteBBox": List[float],
        "DataSource": str,
        "Distance": float,
        "DurationSeconds": float,
        "DistanceUnit": DistanceUnitType,
    },
)
TruckDimensionsTypeDef = TypedDict(
    "TruckDimensionsTypeDef",
    {
        "Length": NotRequired[float],
        "Height": NotRequired[float],
        "Width": NotRequired[float],
        "Unit": NotRequired[DimensionUnitType],
    },
)
TruckWeightTypeDef = TypedDict(
    "TruckWeightTypeDef",
    {
        "Total": NotRequired[float],
        "Unit": NotRequired[VehicleWeightUnitType],
    },
)
CircleOutputTypeDef = TypedDict(
    "CircleOutputTypeDef",
    {
        "Center": List[float],
        "Radius": float,
    },
)
CircleTypeDef = TypedDict(
    "CircleTypeDef",
    {
        "Center": Sequence[float],
        "Radius": float,
    },
)
CreateGeofenceCollectionRequestRequestTypeDef = TypedDict(
    "CreateGeofenceCollectionRequestRequestTypeDef",
    {
        "CollectionName": str,
        "PricingPlan": NotRequired[PricingPlanType],
        "PricingPlanDataSource": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "KmsKeyId": NotRequired[str],
    },
)
MapConfigurationTypeDef = TypedDict(
    "MapConfigurationTypeDef",
    {
        "Style": str,
        "PoliticalView": NotRequired[str],
        "CustomLayers": NotRequired[Sequence[str]],
    },
)
DataSourceConfigurationTypeDef = TypedDict(
    "DataSourceConfigurationTypeDef",
    {
        "IntendedUse": NotRequired[IntendedUseType],
    },
)
CreateRouteCalculatorRequestRequestTypeDef = TypedDict(
    "CreateRouteCalculatorRequestRequestTypeDef",
    {
        "CalculatorName": str,
        "DataSource": str,
        "PricingPlan": NotRequired[PricingPlanType],
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CreateTrackerRequestRequestTypeDef = TypedDict(
    "CreateTrackerRequestRequestTypeDef",
    {
        "TrackerName": str,
        "PricingPlan": NotRequired[PricingPlanType],
        "KmsKeyId": NotRequired[str],
        "PricingPlanDataSource": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "PositionFiltering": NotRequired[PositionFilteringType],
        "EventBridgeEnabled": NotRequired[bool],
        "KmsKeyEnableGeospatialQueries": NotRequired[bool],
    },
)
DeleteGeofenceCollectionRequestRequestTypeDef = TypedDict(
    "DeleteGeofenceCollectionRequestRequestTypeDef",
    {
        "CollectionName": str,
    },
)
DeleteKeyRequestRequestTypeDef = TypedDict(
    "DeleteKeyRequestRequestTypeDef",
    {
        "KeyName": str,
        "ForceDelete": NotRequired[bool],
    },
)
DeleteMapRequestRequestTypeDef = TypedDict(
    "DeleteMapRequestRequestTypeDef",
    {
        "MapName": str,
    },
)
DeletePlaceIndexRequestRequestTypeDef = TypedDict(
    "DeletePlaceIndexRequestRequestTypeDef",
    {
        "IndexName": str,
    },
)
DeleteRouteCalculatorRequestRequestTypeDef = TypedDict(
    "DeleteRouteCalculatorRequestRequestTypeDef",
    {
        "CalculatorName": str,
    },
)
DeleteTrackerRequestRequestTypeDef = TypedDict(
    "DeleteTrackerRequestRequestTypeDef",
    {
        "TrackerName": str,
    },
)
DescribeGeofenceCollectionRequestRequestTypeDef = TypedDict(
    "DescribeGeofenceCollectionRequestRequestTypeDef",
    {
        "CollectionName": str,
    },
)
DescribeKeyRequestRequestTypeDef = TypedDict(
    "DescribeKeyRequestRequestTypeDef",
    {
        "KeyName": str,
    },
)
DescribeMapRequestRequestTypeDef = TypedDict(
    "DescribeMapRequestRequestTypeDef",
    {
        "MapName": str,
    },
)
MapConfigurationOutputTypeDef = TypedDict(
    "MapConfigurationOutputTypeDef",
    {
        "Style": str,
        "PoliticalView": NotRequired[str],
        "CustomLayers": NotRequired[List[str]],
    },
)
DescribePlaceIndexRequestRequestTypeDef = TypedDict(
    "DescribePlaceIndexRequestRequestTypeDef",
    {
        "IndexName": str,
    },
)
DescribeRouteCalculatorRequestRequestTypeDef = TypedDict(
    "DescribeRouteCalculatorRequestRequestTypeDef",
    {
        "CalculatorName": str,
    },
)
DescribeTrackerRequestRequestTypeDef = TypedDict(
    "DescribeTrackerRequestRequestTypeDef",
    {
        "TrackerName": str,
    },
)
PositionalAccuracyTypeDef = TypedDict(
    "PositionalAccuracyTypeDef",
    {
        "Horizontal": float,
    },
)
WiFiAccessPointTypeDef = TypedDict(
    "WiFiAccessPointTypeDef",
    {
        "MacAddress": str,
        "Rss": int,
    },
)
DisassociateTrackerConsumerRequestRequestTypeDef = TypedDict(
    "DisassociateTrackerConsumerRequestRequestTypeDef",
    {
        "TrackerName": str,
        "ConsumerArn": str,
    },
)
ForecastGeofenceEventsDeviceStateTypeDef = TypedDict(
    "ForecastGeofenceEventsDeviceStateTypeDef",
    {
        "Position": Sequence[float],
        "Speed": NotRequired[float],
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
ForecastedEventTypeDef = TypedDict(
    "ForecastedEventTypeDef",
    {
        "EventId": str,
        "GeofenceId": str,
        "IsDeviceInGeofence": bool,
        "NearestDistance": float,
        "EventType": ForecastedGeofenceEventTypeType,
        "ForecastedBreachTime": NotRequired[datetime],
        "GeofenceProperties": NotRequired[Dict[str, str]],
    },
)
GetDevicePositionRequestRequestTypeDef = TypedDict(
    "GetDevicePositionRequestRequestTypeDef",
    {
        "TrackerName": str,
        "DeviceId": str,
    },
)
GetGeofenceRequestRequestTypeDef = TypedDict(
    "GetGeofenceRequestRequestTypeDef",
    {
        "CollectionName": str,
        "GeofenceId": str,
    },
)
GetMapGlyphsRequestRequestTypeDef = TypedDict(
    "GetMapGlyphsRequestRequestTypeDef",
    {
        "MapName": str,
        "FontStack": str,
        "FontUnicodeRange": str,
        "Key": NotRequired[str],
    },
)
GetMapSpritesRequestRequestTypeDef = TypedDict(
    "GetMapSpritesRequestRequestTypeDef",
    {
        "MapName": str,
        "FileName": str,
        "Key": NotRequired[str],
    },
)
GetMapStyleDescriptorRequestRequestTypeDef = TypedDict(
    "GetMapStyleDescriptorRequestRequestTypeDef",
    {
        "MapName": str,
        "Key": NotRequired[str],
    },
)
GetMapTileRequestRequestTypeDef = TypedDict(
    "GetMapTileRequestRequestTypeDef",
    {
        "MapName": str,
        "Z": str,
        "X": str,
        "Y": str,
        "Key": NotRequired[str],
    },
)
GetPlaceRequestRequestTypeDef = TypedDict(
    "GetPlaceRequestRequestTypeDef",
    {
        "IndexName": str,
        "PlaceId": str,
        "Language": NotRequired[str],
        "Key": NotRequired[str],
    },
)
LegGeometryTypeDef = TypedDict(
    "LegGeometryTypeDef",
    {
        "LineString": NotRequired[List[List[float]]],
    },
)
StepTypeDef = TypedDict(
    "StepTypeDef",
    {
        "StartPosition": List[float],
        "EndPosition": List[float],
        "Distance": float,
        "DurationSeconds": float,
        "GeometryOffset": NotRequired[int],
    },
)
TrackingFilterGeometryTypeDef = TypedDict(
    "TrackingFilterGeometryTypeDef",
    {
        "Polygon": NotRequired[Sequence[Sequence[Sequence[float]]]],
    },
)
ListGeofenceCollectionsRequestRequestTypeDef = TypedDict(
    "ListGeofenceCollectionsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListGeofenceCollectionsResponseEntryTypeDef = TypedDict(
    "ListGeofenceCollectionsResponseEntryTypeDef",
    {
        "CollectionName": str,
        "Description": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "PricingPlan": NotRequired[PricingPlanType],
        "PricingPlanDataSource": NotRequired[str],
    },
)
ListGeofencesRequestRequestTypeDef = TypedDict(
    "ListGeofencesRequestRequestTypeDef",
    {
        "CollectionName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListMapsRequestRequestTypeDef = TypedDict(
    "ListMapsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListMapsResponseEntryTypeDef = TypedDict(
    "ListMapsResponseEntryTypeDef",
    {
        "MapName": str,
        "Description": str,
        "DataSource": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "PricingPlan": NotRequired[PricingPlanType],
    },
)
ListPlaceIndexesRequestRequestTypeDef = TypedDict(
    "ListPlaceIndexesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListPlaceIndexesResponseEntryTypeDef = TypedDict(
    "ListPlaceIndexesResponseEntryTypeDef",
    {
        "IndexName": str,
        "Description": str,
        "DataSource": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "PricingPlan": NotRequired[PricingPlanType],
    },
)
ListRouteCalculatorsRequestRequestTypeDef = TypedDict(
    "ListRouteCalculatorsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListRouteCalculatorsResponseEntryTypeDef = TypedDict(
    "ListRouteCalculatorsResponseEntryTypeDef",
    {
        "CalculatorName": str,
        "Description": str,
        "DataSource": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "PricingPlan": NotRequired[PricingPlanType],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
ListTrackerConsumersRequestRequestTypeDef = TypedDict(
    "ListTrackerConsumersRequestRequestTypeDef",
    {
        "TrackerName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTrackersRequestRequestTypeDef = TypedDict(
    "ListTrackersRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTrackersResponseEntryTypeDef = TypedDict(
    "ListTrackersResponseEntryTypeDef",
    {
        "TrackerName": str,
        "Description": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "PricingPlan": NotRequired[PricingPlanType],
        "PricingPlanDataSource": NotRequired[str],
    },
)
LteLocalIdTypeDef = TypedDict(
    "LteLocalIdTypeDef",
    {
        "Earfcn": int,
        "Pci": int,
    },
)
LteNetworkMeasurementsTypeDef = TypedDict(
    "LteNetworkMeasurementsTypeDef",
    {
        "Earfcn": int,
        "CellId": int,
        "Pci": int,
        "Rsrp": NotRequired[int],
        "Rsrq": NotRequired[float],
    },
)
MapConfigurationUpdateTypeDef = TypedDict(
    "MapConfigurationUpdateTypeDef",
    {
        "PoliticalView": NotRequired[str],
        "CustomLayers": NotRequired[Sequence[str]],
    },
)
PlaceGeometryTypeDef = TypedDict(
    "PlaceGeometryTypeDef",
    {
        "Point": NotRequired[List[float]],
    },
)
TimeZoneTypeDef = TypedDict(
    "TimeZoneTypeDef",
    {
        "Name": str,
        "Offset": NotRequired[int],
    },
)
RouteMatrixEntryErrorTypeDef = TypedDict(
    "RouteMatrixEntryErrorTypeDef",
    {
        "Code": RouteMatrixErrorCodeType,
        "Message": NotRequired[str],
    },
)
SearchForSuggestionsResultTypeDef = TypedDict(
    "SearchForSuggestionsResultTypeDef",
    {
        "Text": str,
        "PlaceId": NotRequired[str],
        "Categories": NotRequired[List[str]],
        "SupplementalCategories": NotRequired[List[str]],
    },
)
SearchPlaceIndexForPositionRequestRequestTypeDef = TypedDict(
    "SearchPlaceIndexForPositionRequestRequestTypeDef",
    {
        "IndexName": str,
        "Position": Sequence[float],
        "MaxResults": NotRequired[int],
        "Language": NotRequired[str],
        "Key": NotRequired[str],
    },
)
SearchPlaceIndexForPositionSummaryTypeDef = TypedDict(
    "SearchPlaceIndexForPositionSummaryTypeDef",
    {
        "Position": List[float],
        "DataSource": str,
        "MaxResults": NotRequired[int],
        "Language": NotRequired[str],
    },
)
SearchPlaceIndexForSuggestionsRequestRequestTypeDef = TypedDict(
    "SearchPlaceIndexForSuggestionsRequestRequestTypeDef",
    {
        "IndexName": str,
        "Text": str,
        "BiasPosition": NotRequired[Sequence[float]],
        "FilterBBox": NotRequired[Sequence[float]],
        "FilterCountries": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "Language": NotRequired[str],
        "FilterCategories": NotRequired[Sequence[str]],
        "Key": NotRequired[str],
    },
)
SearchPlaceIndexForSuggestionsSummaryTypeDef = TypedDict(
    "SearchPlaceIndexForSuggestionsSummaryTypeDef",
    {
        "Text": str,
        "DataSource": str,
        "BiasPosition": NotRequired[List[float]],
        "FilterBBox": NotRequired[List[float]],
        "FilterCountries": NotRequired[List[str]],
        "MaxResults": NotRequired[int],
        "Language": NotRequired[str],
        "FilterCategories": NotRequired[List[str]],
    },
)
SearchPlaceIndexForTextRequestRequestTypeDef = TypedDict(
    "SearchPlaceIndexForTextRequestRequestTypeDef",
    {
        "IndexName": str,
        "Text": str,
        "BiasPosition": NotRequired[Sequence[float]],
        "FilterBBox": NotRequired[Sequence[float]],
        "FilterCountries": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "Language": NotRequired[str],
        "FilterCategories": NotRequired[Sequence[str]],
        "Key": NotRequired[str],
    },
)
SearchPlaceIndexForTextSummaryTypeDef = TypedDict(
    "SearchPlaceIndexForTextSummaryTypeDef",
    {
        "Text": str,
        "DataSource": str,
        "BiasPosition": NotRequired[List[float]],
        "FilterBBox": NotRequired[List[float]],
        "FilterCountries": NotRequired[List[str]],
        "MaxResults": NotRequired[int],
        "ResultBBox": NotRequired[List[float]],
        "Language": NotRequired[str],
        "FilterCategories": NotRequired[List[str]],
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
UpdateGeofenceCollectionRequestRequestTypeDef = TypedDict(
    "UpdateGeofenceCollectionRequestRequestTypeDef",
    {
        "CollectionName": str,
        "PricingPlan": NotRequired[PricingPlanType],
        "PricingPlanDataSource": NotRequired[str],
        "Description": NotRequired[str],
    },
)
UpdateRouteCalculatorRequestRequestTypeDef = TypedDict(
    "UpdateRouteCalculatorRequestRequestTypeDef",
    {
        "CalculatorName": str,
        "PricingPlan": NotRequired[PricingPlanType],
        "Description": NotRequired[str],
    },
)
UpdateTrackerRequestRequestTypeDef = TypedDict(
    "UpdateTrackerRequestRequestTypeDef",
    {
        "TrackerName": str,
        "PricingPlan": NotRequired[PricingPlanType],
        "PricingPlanDataSource": NotRequired[str],
        "Description": NotRequired[str],
        "PositionFiltering": NotRequired[PositionFilteringType],
        "EventBridgeEnabled": NotRequired[bool],
        "KmsKeyEnableGeospatialQueries": NotRequired[bool],
    },
)
ListKeysRequestRequestTypeDef = TypedDict(
    "ListKeysRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filter": NotRequired[ApiKeyFilterTypeDef],
    },
)
ListKeysResponseEntryTypeDef = TypedDict(
    "ListKeysResponseEntryTypeDef",
    {
        "KeyName": str,
        "ExpireTime": datetime,
        "Restrictions": ApiKeyRestrictionsOutputTypeDef,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "Description": NotRequired[str],
    },
)
BatchDeleteDevicePositionHistoryErrorTypeDef = TypedDict(
    "BatchDeleteDevicePositionHistoryErrorTypeDef",
    {
        "DeviceId": str,
        "Error": BatchItemErrorTypeDef,
    },
)
BatchDeleteGeofenceErrorTypeDef = TypedDict(
    "BatchDeleteGeofenceErrorTypeDef",
    {
        "GeofenceId": str,
        "Error": BatchItemErrorTypeDef,
    },
)
BatchEvaluateGeofencesErrorTypeDef = TypedDict(
    "BatchEvaluateGeofencesErrorTypeDef",
    {
        "DeviceId": str,
        "SampleTime": datetime,
        "Error": BatchItemErrorTypeDef,
    },
)
BatchGetDevicePositionErrorTypeDef = TypedDict(
    "BatchGetDevicePositionErrorTypeDef",
    {
        "DeviceId": str,
        "Error": BatchItemErrorTypeDef,
    },
)
BatchPutGeofenceErrorTypeDef = TypedDict(
    "BatchPutGeofenceErrorTypeDef",
    {
        "GeofenceId": str,
        "Error": BatchItemErrorTypeDef,
    },
)
BatchUpdateDevicePositionErrorTypeDef = TypedDict(
    "BatchUpdateDevicePositionErrorTypeDef",
    {
        "DeviceId": str,
        "SampleTime": datetime,
        "Error": BatchItemErrorTypeDef,
    },
)
CreateGeofenceCollectionResponseTypeDef = TypedDict(
    "CreateGeofenceCollectionResponseTypeDef",
    {
        "CollectionName": str,
        "CollectionArn": str,
        "CreateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateKeyResponseTypeDef = TypedDict(
    "CreateKeyResponseTypeDef",
    {
        "Key": str,
        "KeyArn": str,
        "KeyName": str,
        "CreateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMapResponseTypeDef = TypedDict(
    "CreateMapResponseTypeDef",
    {
        "MapName": str,
        "MapArn": str,
        "CreateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePlaceIndexResponseTypeDef = TypedDict(
    "CreatePlaceIndexResponseTypeDef",
    {
        "IndexName": str,
        "IndexArn": str,
        "CreateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRouteCalculatorResponseTypeDef = TypedDict(
    "CreateRouteCalculatorResponseTypeDef",
    {
        "CalculatorName": str,
        "CalculatorArn": str,
        "CreateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTrackerResponseTypeDef = TypedDict(
    "CreateTrackerResponseTypeDef",
    {
        "TrackerName": str,
        "TrackerArn": str,
        "CreateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeGeofenceCollectionResponseTypeDef = TypedDict(
    "DescribeGeofenceCollectionResponseTypeDef",
    {
        "CollectionName": str,
        "CollectionArn": str,
        "Description": str,
        "PricingPlan": PricingPlanType,
        "PricingPlanDataSource": str,
        "KmsKeyId": str,
        "Tags": Dict[str, str],
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "GeofenceCount": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeKeyResponseTypeDef = TypedDict(
    "DescribeKeyResponseTypeDef",
    {
        "Key": str,
        "KeyArn": str,
        "KeyName": str,
        "Restrictions": ApiKeyRestrictionsOutputTypeDef,
        "CreateTime": datetime,
        "ExpireTime": datetime,
        "UpdateTime": datetime,
        "Description": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRouteCalculatorResponseTypeDef = TypedDict(
    "DescribeRouteCalculatorResponseTypeDef",
    {
        "CalculatorName": str,
        "CalculatorArn": str,
        "PricingPlan": PricingPlanType,
        "Description": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "DataSource": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTrackerResponseTypeDef = TypedDict(
    "DescribeTrackerResponseTypeDef",
    {
        "TrackerName": str,
        "TrackerArn": str,
        "Description": str,
        "PricingPlan": PricingPlanType,
        "PricingPlanDataSource": str,
        "Tags": Dict[str, str],
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "KmsKeyId": str,
        "PositionFiltering": PositionFilteringType,
        "EventBridgeEnabled": bool,
        "KmsKeyEnableGeospatialQueries": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMapGlyphsResponseTypeDef = TypedDict(
    "GetMapGlyphsResponseTypeDef",
    {
        "Blob": StreamingBody,
        "ContentType": str,
        "CacheControl": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMapSpritesResponseTypeDef = TypedDict(
    "GetMapSpritesResponseTypeDef",
    {
        "Blob": StreamingBody,
        "ContentType": str,
        "CacheControl": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMapStyleDescriptorResponseTypeDef = TypedDict(
    "GetMapStyleDescriptorResponseTypeDef",
    {
        "Blob": StreamingBody,
        "ContentType": str,
        "CacheControl": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMapTileResponseTypeDef = TypedDict(
    "GetMapTileResponseTypeDef",
    {
        "Blob": StreamingBody,
        "ContentType": str,
        "CacheControl": str,
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
ListTrackerConsumersResponseTypeDef = TypedDict(
    "ListTrackerConsumersResponseTypeDef",
    {
        "ConsumerArns": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PutGeofenceResponseTypeDef = TypedDict(
    "PutGeofenceResponseTypeDef",
    {
        "GeofenceId": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateGeofenceCollectionResponseTypeDef = TypedDict(
    "UpdateGeofenceCollectionResponseTypeDef",
    {
        "CollectionName": str,
        "CollectionArn": str,
        "UpdateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateKeyResponseTypeDef = TypedDict(
    "UpdateKeyResponseTypeDef",
    {
        "KeyArn": str,
        "KeyName": str,
        "UpdateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateMapResponseTypeDef = TypedDict(
    "UpdateMapResponseTypeDef",
    {
        "MapName": str,
        "MapArn": str,
        "UpdateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePlaceIndexResponseTypeDef = TypedDict(
    "UpdatePlaceIndexResponseTypeDef",
    {
        "IndexName": str,
        "IndexArn": str,
        "UpdateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRouteCalculatorResponseTypeDef = TypedDict(
    "UpdateRouteCalculatorResponseTypeDef",
    {
        "CalculatorName": str,
        "CalculatorArn": str,
        "UpdateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTrackerResponseTypeDef = TypedDict(
    "UpdateTrackerResponseTypeDef",
    {
        "TrackerName": str,
        "TrackerArn": str,
        "UpdateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateKeyRequestRequestTypeDef = TypedDict(
    "CreateKeyRequestRequestTypeDef",
    {
        "KeyName": str,
        "Restrictions": ApiKeyRestrictionsTypeDef,
        "Description": NotRequired[str],
        "ExpireTime": NotRequired[TimestampTypeDef],
        "NoExpiry": NotRequired[bool],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
GetDevicePositionHistoryRequestRequestTypeDef = TypedDict(
    "GetDevicePositionHistoryRequestRequestTypeDef",
    {
        "TrackerName": str,
        "DeviceId": str,
        "NextToken": NotRequired[str],
        "StartTimeInclusive": NotRequired[TimestampTypeDef],
        "EndTimeExclusive": NotRequired[TimestampTypeDef],
        "MaxResults": NotRequired[int],
    },
)
UpdateKeyRequestRequestTypeDef = TypedDict(
    "UpdateKeyRequestRequestTypeDef",
    {
        "KeyName": str,
        "Description": NotRequired[str],
        "ExpireTime": NotRequired[TimestampTypeDef],
        "NoExpiry": NotRequired[bool],
        "ForceUpdate": NotRequired[bool],
        "Restrictions": NotRequired[ApiKeyRestrictionsTypeDef],
    },
)
CalculateRouteTruckModeOptionsTypeDef = TypedDict(
    "CalculateRouteTruckModeOptionsTypeDef",
    {
        "AvoidFerries": NotRequired[bool],
        "AvoidTolls": NotRequired[bool],
        "Dimensions": NotRequired[TruckDimensionsTypeDef],
        "Weight": NotRequired[TruckWeightTypeDef],
    },
)
GeofenceGeometryOutputTypeDef = TypedDict(
    "GeofenceGeometryOutputTypeDef",
    {
        "Polygon": NotRequired[List[List[List[float]]]],
        "Circle": NotRequired[CircleOutputTypeDef],
        "Geobuf": NotRequired[bytes],
    },
)
CircleUnionTypeDef = Union[CircleTypeDef, CircleOutputTypeDef]
CreateMapRequestRequestTypeDef = TypedDict(
    "CreateMapRequestRequestTypeDef",
    {
        "MapName": str,
        "Configuration": MapConfigurationTypeDef,
        "PricingPlan": NotRequired[PricingPlanType],
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CreatePlaceIndexRequestRequestTypeDef = TypedDict(
    "CreatePlaceIndexRequestRequestTypeDef",
    {
        "IndexName": str,
        "DataSource": str,
        "PricingPlan": NotRequired[PricingPlanType],
        "Description": NotRequired[str],
        "DataSourceConfiguration": NotRequired[DataSourceConfigurationTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
DescribePlaceIndexResponseTypeDef = TypedDict(
    "DescribePlaceIndexResponseTypeDef",
    {
        "IndexName": str,
        "IndexArn": str,
        "PricingPlan": PricingPlanType,
        "Description": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "DataSource": str,
        "DataSourceConfiguration": DataSourceConfigurationTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePlaceIndexRequestRequestTypeDef = TypedDict(
    "UpdatePlaceIndexRequestRequestTypeDef",
    {
        "IndexName": str,
        "PricingPlan": NotRequired[PricingPlanType],
        "Description": NotRequired[str],
        "DataSourceConfiguration": NotRequired[DataSourceConfigurationTypeDef],
    },
)
DescribeMapResponseTypeDef = TypedDict(
    "DescribeMapResponseTypeDef",
    {
        "MapName": str,
        "MapArn": str,
        "PricingPlan": PricingPlanType,
        "DataSource": str,
        "Configuration": MapConfigurationOutputTypeDef,
        "Description": str,
        "Tags": Dict[str, str],
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DevicePositionTypeDef = TypedDict(
    "DevicePositionTypeDef",
    {
        "SampleTime": datetime,
        "ReceivedTime": datetime,
        "Position": List[float],
        "DeviceId": NotRequired[str],
        "Accuracy": NotRequired[PositionalAccuracyTypeDef],
        "PositionProperties": NotRequired[Dict[str, str]],
    },
)
DevicePositionUpdateTypeDef = TypedDict(
    "DevicePositionUpdateTypeDef",
    {
        "DeviceId": str,
        "SampleTime": TimestampTypeDef,
        "Position": Sequence[float],
        "Accuracy": NotRequired[PositionalAccuracyTypeDef],
        "PositionProperties": NotRequired[Mapping[str, str]],
    },
)
GetDevicePositionResponseTypeDef = TypedDict(
    "GetDevicePositionResponseTypeDef",
    {
        "DeviceId": str,
        "SampleTime": datetime,
        "ReceivedTime": datetime,
        "Position": List[float],
        "Accuracy": PositionalAccuracyTypeDef,
        "PositionProperties": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InferredStateTypeDef = TypedDict(
    "InferredStateTypeDef",
    {
        "ProxyDetected": bool,
        "Position": NotRequired[List[float]],
        "Accuracy": NotRequired[PositionalAccuracyTypeDef],
        "DeviationDistance": NotRequired[float],
    },
)
ListDevicePositionsResponseEntryTypeDef = TypedDict(
    "ListDevicePositionsResponseEntryTypeDef",
    {
        "DeviceId": str,
        "SampleTime": datetime,
        "Position": List[float],
        "Accuracy": NotRequired[PositionalAccuracyTypeDef],
        "PositionProperties": NotRequired[Dict[str, str]],
    },
)
ForecastGeofenceEventsRequestRequestTypeDef = TypedDict(
    "ForecastGeofenceEventsRequestRequestTypeDef",
    {
        "CollectionName": str,
        "DeviceState": ForecastGeofenceEventsDeviceStateTypeDef,
        "TimeHorizonMinutes": NotRequired[float],
        "DistanceUnit": NotRequired[DistanceUnitType],
        "SpeedUnit": NotRequired[SpeedUnitType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ForecastGeofenceEventsRequestForecastGeofenceEventsPaginateTypeDef = TypedDict(
    "ForecastGeofenceEventsRequestForecastGeofenceEventsPaginateTypeDef",
    {
        "CollectionName": str,
        "DeviceState": ForecastGeofenceEventsDeviceStateTypeDef,
        "TimeHorizonMinutes": NotRequired[float],
        "DistanceUnit": NotRequired[DistanceUnitType],
        "SpeedUnit": NotRequired[SpeedUnitType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetDevicePositionHistoryRequestGetDevicePositionHistoryPaginateTypeDef = TypedDict(
    "GetDevicePositionHistoryRequestGetDevicePositionHistoryPaginateTypeDef",
    {
        "TrackerName": str,
        "DeviceId": str,
        "StartTimeInclusive": NotRequired[TimestampTypeDef],
        "EndTimeExclusive": NotRequired[TimestampTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGeofenceCollectionsRequestListGeofenceCollectionsPaginateTypeDef = TypedDict(
    "ListGeofenceCollectionsRequestListGeofenceCollectionsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGeofencesRequestListGeofencesPaginateTypeDef = TypedDict(
    "ListGeofencesRequestListGeofencesPaginateTypeDef",
    {
        "CollectionName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListKeysRequestListKeysPaginateTypeDef = TypedDict(
    "ListKeysRequestListKeysPaginateTypeDef",
    {
        "Filter": NotRequired[ApiKeyFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMapsRequestListMapsPaginateTypeDef = TypedDict(
    "ListMapsRequestListMapsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPlaceIndexesRequestListPlaceIndexesPaginateTypeDef = TypedDict(
    "ListPlaceIndexesRequestListPlaceIndexesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRouteCalculatorsRequestListRouteCalculatorsPaginateTypeDef = TypedDict(
    "ListRouteCalculatorsRequestListRouteCalculatorsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTrackerConsumersRequestListTrackerConsumersPaginateTypeDef = TypedDict(
    "ListTrackerConsumersRequestListTrackerConsumersPaginateTypeDef",
    {
        "TrackerName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTrackersRequestListTrackersPaginateTypeDef = TypedDict(
    "ListTrackersRequestListTrackersPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ForecastGeofenceEventsResponseTypeDef = TypedDict(
    "ForecastGeofenceEventsResponseTypeDef",
    {
        "ForecastedEvents": List[ForecastedEventTypeDef],
        "DistanceUnit": DistanceUnitType,
        "SpeedUnit": SpeedUnitType,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
LegTypeDef = TypedDict(
    "LegTypeDef",
    {
        "StartPosition": List[float],
        "EndPosition": List[float],
        "Distance": float,
        "DurationSeconds": float,
        "Steps": List[StepTypeDef],
        "Geometry": NotRequired[LegGeometryTypeDef],
    },
)
ListDevicePositionsRequestListDevicePositionsPaginateTypeDef = TypedDict(
    "ListDevicePositionsRequestListDevicePositionsPaginateTypeDef",
    {
        "TrackerName": str,
        "FilterGeometry": NotRequired[TrackingFilterGeometryTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDevicePositionsRequestRequestTypeDef = TypedDict(
    "ListDevicePositionsRequestRequestTypeDef",
    {
        "TrackerName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "FilterGeometry": NotRequired[TrackingFilterGeometryTypeDef],
    },
)
ListGeofenceCollectionsResponseTypeDef = TypedDict(
    "ListGeofenceCollectionsResponseTypeDef",
    {
        "Entries": List[ListGeofenceCollectionsResponseEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListMapsResponseTypeDef = TypedDict(
    "ListMapsResponseTypeDef",
    {
        "Entries": List[ListMapsResponseEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListPlaceIndexesResponseTypeDef = TypedDict(
    "ListPlaceIndexesResponseTypeDef",
    {
        "Entries": List[ListPlaceIndexesResponseEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListRouteCalculatorsResponseTypeDef = TypedDict(
    "ListRouteCalculatorsResponseTypeDef",
    {
        "Entries": List[ListRouteCalculatorsResponseEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTrackersResponseTypeDef = TypedDict(
    "ListTrackersResponseTypeDef",
    {
        "Entries": List[ListTrackersResponseEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
LteCellDetailsTypeDef = TypedDict(
    "LteCellDetailsTypeDef",
    {
        "CellId": int,
        "Mcc": int,
        "Mnc": int,
        "LocalId": NotRequired[LteLocalIdTypeDef],
        "NetworkMeasurements": NotRequired[Sequence[LteNetworkMeasurementsTypeDef]],
        "TimingAdvance": NotRequired[int],
        "NrCapable": NotRequired[bool],
        "Rsrp": NotRequired[int],
        "Rsrq": NotRequired[float],
        "Tac": NotRequired[int],
    },
)
UpdateMapRequestRequestTypeDef = TypedDict(
    "UpdateMapRequestRequestTypeDef",
    {
        "MapName": str,
        "PricingPlan": NotRequired[PricingPlanType],
        "Description": NotRequired[str],
        "ConfigurationUpdate": NotRequired[MapConfigurationUpdateTypeDef],
    },
)
PlaceTypeDef = TypedDict(
    "PlaceTypeDef",
    {
        "Geometry": PlaceGeometryTypeDef,
        "Label": NotRequired[str],
        "AddressNumber": NotRequired[str],
        "Street": NotRequired[str],
        "Neighborhood": NotRequired[str],
        "Municipality": NotRequired[str],
        "SubRegion": NotRequired[str],
        "Region": NotRequired[str],
        "Country": NotRequired[str],
        "PostalCode": NotRequired[str],
        "Interpolated": NotRequired[bool],
        "TimeZone": NotRequired[TimeZoneTypeDef],
        "UnitType": NotRequired[str],
        "UnitNumber": NotRequired[str],
        "Categories": NotRequired[List[str]],
        "SupplementalCategories": NotRequired[List[str]],
        "SubMunicipality": NotRequired[str],
    },
)
RouteMatrixEntryTypeDef = TypedDict(
    "RouteMatrixEntryTypeDef",
    {
        "Distance": NotRequired[float],
        "DurationSeconds": NotRequired[float],
        "Error": NotRequired[RouteMatrixEntryErrorTypeDef],
    },
)
SearchPlaceIndexForSuggestionsResponseTypeDef = TypedDict(
    "SearchPlaceIndexForSuggestionsResponseTypeDef",
    {
        "Summary": SearchPlaceIndexForSuggestionsSummaryTypeDef,
        "Results": List[SearchForSuggestionsResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListKeysResponseTypeDef = TypedDict(
    "ListKeysResponseTypeDef",
    {
        "Entries": List[ListKeysResponseEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
BatchDeleteDevicePositionHistoryResponseTypeDef = TypedDict(
    "BatchDeleteDevicePositionHistoryResponseTypeDef",
    {
        "Errors": List[BatchDeleteDevicePositionHistoryErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDeleteGeofenceResponseTypeDef = TypedDict(
    "BatchDeleteGeofenceResponseTypeDef",
    {
        "Errors": List[BatchDeleteGeofenceErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchEvaluateGeofencesResponseTypeDef = TypedDict(
    "BatchEvaluateGeofencesResponseTypeDef",
    {
        "Errors": List[BatchEvaluateGeofencesErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchPutGeofenceResponseTypeDef = TypedDict(
    "BatchPutGeofenceResponseTypeDef",
    {
        "Successes": List[BatchPutGeofenceSuccessTypeDef],
        "Errors": List[BatchPutGeofenceErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchUpdateDevicePositionResponseTypeDef = TypedDict(
    "BatchUpdateDevicePositionResponseTypeDef",
    {
        "Errors": List[BatchUpdateDevicePositionErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CalculateRouteMatrixRequestRequestTypeDef = TypedDict(
    "CalculateRouteMatrixRequestRequestTypeDef",
    {
        "CalculatorName": str,
        "DeparturePositions": Sequence[Sequence[float]],
        "DestinationPositions": Sequence[Sequence[float]],
        "TravelMode": NotRequired[TravelModeType],
        "DepartureTime": NotRequired[TimestampTypeDef],
        "DepartNow": NotRequired[bool],
        "DistanceUnit": NotRequired[DistanceUnitType],
        "CarModeOptions": NotRequired[CalculateRouteCarModeOptionsTypeDef],
        "TruckModeOptions": NotRequired[CalculateRouteTruckModeOptionsTypeDef],
        "Key": NotRequired[str],
    },
)
CalculateRouteRequestRequestTypeDef = TypedDict(
    "CalculateRouteRequestRequestTypeDef",
    {
        "CalculatorName": str,
        "DeparturePosition": Sequence[float],
        "DestinationPosition": Sequence[float],
        "WaypointPositions": NotRequired[Sequence[Sequence[float]]],
        "TravelMode": NotRequired[TravelModeType],
        "DepartureTime": NotRequired[TimestampTypeDef],
        "DepartNow": NotRequired[bool],
        "DistanceUnit": NotRequired[DistanceUnitType],
        "IncludeLegGeometry": NotRequired[bool],
        "CarModeOptions": NotRequired[CalculateRouteCarModeOptionsTypeDef],
        "TruckModeOptions": NotRequired[CalculateRouteTruckModeOptionsTypeDef],
        "ArrivalTime": NotRequired[TimestampTypeDef],
        "OptimizeFor": NotRequired[OptimizationModeType],
        "Key": NotRequired[str],
    },
)
GetGeofenceResponseTypeDef = TypedDict(
    "GetGeofenceResponseTypeDef",
    {
        "GeofenceId": str,
        "Geometry": GeofenceGeometryOutputTypeDef,
        "Status": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "GeofenceProperties": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListGeofenceResponseEntryTypeDef = TypedDict(
    "ListGeofenceResponseEntryTypeDef",
    {
        "GeofenceId": str,
        "Geometry": GeofenceGeometryOutputTypeDef,
        "Status": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "GeofenceProperties": NotRequired[Dict[str, str]],
    },
)
GeofenceGeometryTypeDef = TypedDict(
    "GeofenceGeometryTypeDef",
    {
        "Polygon": NotRequired[Sequence[Sequence[Sequence[float]]]],
        "Circle": NotRequired[CircleUnionTypeDef],
        "Geobuf": NotRequired[BlobTypeDef],
    },
)
BatchGetDevicePositionResponseTypeDef = TypedDict(
    "BatchGetDevicePositionResponseTypeDef",
    {
        "Errors": List[BatchGetDevicePositionErrorTypeDef],
        "DevicePositions": List[DevicePositionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDevicePositionHistoryResponseTypeDef = TypedDict(
    "GetDevicePositionHistoryResponseTypeDef",
    {
        "DevicePositions": List[DevicePositionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
BatchEvaluateGeofencesRequestRequestTypeDef = TypedDict(
    "BatchEvaluateGeofencesRequestRequestTypeDef",
    {
        "CollectionName": str,
        "DevicePositionUpdates": Sequence[DevicePositionUpdateTypeDef],
    },
)
BatchUpdateDevicePositionRequestRequestTypeDef = TypedDict(
    "BatchUpdateDevicePositionRequestRequestTypeDef",
    {
        "TrackerName": str,
        "Updates": Sequence[DevicePositionUpdateTypeDef],
    },
)
VerifyDevicePositionResponseTypeDef = TypedDict(
    "VerifyDevicePositionResponseTypeDef",
    {
        "InferredState": InferredStateTypeDef,
        "DeviceId": str,
        "SampleTime": datetime,
        "ReceivedTime": datetime,
        "DistanceUnit": DistanceUnitType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDevicePositionsResponseTypeDef = TypedDict(
    "ListDevicePositionsResponseTypeDef",
    {
        "Entries": List[ListDevicePositionsResponseEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CalculateRouteResponseTypeDef = TypedDict(
    "CalculateRouteResponseTypeDef",
    {
        "Legs": List[LegTypeDef],
        "Summary": CalculateRouteSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CellSignalsTypeDef = TypedDict(
    "CellSignalsTypeDef",
    {
        "LteCellDetails": Sequence[LteCellDetailsTypeDef],
    },
)
GetPlaceResponseTypeDef = TypedDict(
    "GetPlaceResponseTypeDef",
    {
        "Place": PlaceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchForPositionResultTypeDef = TypedDict(
    "SearchForPositionResultTypeDef",
    {
        "Place": PlaceTypeDef,
        "Distance": float,
        "PlaceId": NotRequired[str],
    },
)
SearchForTextResultTypeDef = TypedDict(
    "SearchForTextResultTypeDef",
    {
        "Place": PlaceTypeDef,
        "Distance": NotRequired[float],
        "Relevance": NotRequired[float],
        "PlaceId": NotRequired[str],
    },
)
CalculateRouteMatrixResponseTypeDef = TypedDict(
    "CalculateRouteMatrixResponseTypeDef",
    {
        "RouteMatrix": List[List[RouteMatrixEntryTypeDef]],
        "SnappedDeparturePositions": List[List[float]],
        "SnappedDestinationPositions": List[List[float]],
        "Summary": CalculateRouteMatrixSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListGeofencesResponseTypeDef = TypedDict(
    "ListGeofencesResponseTypeDef",
    {
        "Entries": List[ListGeofenceResponseEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GeofenceGeometryUnionTypeDef = Union[GeofenceGeometryTypeDef, GeofenceGeometryOutputTypeDef]
PutGeofenceRequestRequestTypeDef = TypedDict(
    "PutGeofenceRequestRequestTypeDef",
    {
        "CollectionName": str,
        "GeofenceId": str,
        "Geometry": GeofenceGeometryTypeDef,
        "GeofenceProperties": NotRequired[Mapping[str, str]],
    },
)
DeviceStateTypeDef = TypedDict(
    "DeviceStateTypeDef",
    {
        "DeviceId": str,
        "SampleTime": TimestampTypeDef,
        "Position": Sequence[float],
        "Accuracy": NotRequired[PositionalAccuracyTypeDef],
        "Ipv4Address": NotRequired[str],
        "WiFiAccessPoints": NotRequired[Sequence[WiFiAccessPointTypeDef]],
        "CellSignals": NotRequired[CellSignalsTypeDef],
    },
)
SearchPlaceIndexForPositionResponseTypeDef = TypedDict(
    "SearchPlaceIndexForPositionResponseTypeDef",
    {
        "Summary": SearchPlaceIndexForPositionSummaryTypeDef,
        "Results": List[SearchForPositionResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchPlaceIndexForTextResponseTypeDef = TypedDict(
    "SearchPlaceIndexForTextResponseTypeDef",
    {
        "Summary": SearchPlaceIndexForTextSummaryTypeDef,
        "Results": List[SearchForTextResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchPutGeofenceRequestEntryTypeDef = TypedDict(
    "BatchPutGeofenceRequestEntryTypeDef",
    {
        "GeofenceId": str,
        "Geometry": GeofenceGeometryUnionTypeDef,
        "GeofenceProperties": NotRequired[Mapping[str, str]],
    },
)
VerifyDevicePositionRequestRequestTypeDef = TypedDict(
    "VerifyDevicePositionRequestRequestTypeDef",
    {
        "TrackerName": str,
        "DeviceState": DeviceStateTypeDef,
        "DistanceUnit": NotRequired[DistanceUnitType],
    },
)
BatchPutGeofenceRequestRequestTypeDef = TypedDict(
    "BatchPutGeofenceRequestRequestTypeDef",
    {
        "CollectionName": str,
        "Entries": Sequence[BatchPutGeofenceRequestEntryTypeDef],
    },
)
