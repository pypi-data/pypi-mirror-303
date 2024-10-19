"""
Type annotations for controltower service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/type_defs/)

Usage::

    ```python
    from mypy_boto3_controltower.type_defs import BaselineOperationTypeDef

    data: BaselineOperationTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence

from .literals import (
    BaselineOperationStatusType,
    BaselineOperationTypeType,
    ControlOperationStatusType,
    ControlOperationTypeType,
    DriftStatusType,
    EnablementStatusType,
    LandingZoneDriftStatusType,
    LandingZoneOperationStatusType,
    LandingZoneOperationTypeType,
    LandingZoneStatusType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "BaselineOperationTypeDef",
    "BaselineSummaryTypeDef",
    "ControlOperationFilterTypeDef",
    "ControlOperationSummaryTypeDef",
    "ControlOperationTypeDef",
    "CreateLandingZoneInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "DeleteLandingZoneInputRequestTypeDef",
    "DisableBaselineInputRequestTypeDef",
    "DisableControlInputRequestTypeDef",
    "DriftStatusSummaryTypeDef",
    "EnabledBaselineParameterTypeDef",
    "EnabledControlParameterTypeDef",
    "EnabledBaselineParameterSummaryTypeDef",
    "EnablementStatusSummaryTypeDef",
    "EnabledBaselineFilterTypeDef",
    "EnabledControlParameterSummaryTypeDef",
    "RegionTypeDef",
    "EnabledControlFilterTypeDef",
    "GetBaselineInputRequestTypeDef",
    "GetBaselineOperationInputRequestTypeDef",
    "GetControlOperationInputRequestTypeDef",
    "GetEnabledBaselineInputRequestTypeDef",
    "GetEnabledControlInputRequestTypeDef",
    "GetLandingZoneInputRequestTypeDef",
    "GetLandingZoneOperationInputRequestTypeDef",
    "LandingZoneOperationDetailTypeDef",
    "LandingZoneDriftStatusSummaryTypeDef",
    "LandingZoneOperationFilterTypeDef",
    "LandingZoneOperationSummaryTypeDef",
    "LandingZoneSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "ListBaselinesInputRequestTypeDef",
    "ListLandingZonesInputRequestTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ResetEnabledBaselineInputRequestTypeDef",
    "ResetLandingZoneInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateLandingZoneInputRequestTypeDef",
    "ListControlOperationsInputRequestTypeDef",
    "CreateLandingZoneOutputTypeDef",
    "DeleteLandingZoneOutputTypeDef",
    "DisableBaselineOutputTypeDef",
    "DisableControlOutputTypeDef",
    "EnableBaselineOutputTypeDef",
    "EnableControlOutputTypeDef",
    "GetBaselineOperationOutputTypeDef",
    "GetBaselineOutputTypeDef",
    "GetControlOperationOutputTypeDef",
    "ListBaselinesOutputTypeDef",
    "ListControlOperationsOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ResetEnabledBaselineOutputTypeDef",
    "ResetLandingZoneOutputTypeDef",
    "UpdateEnabledBaselineOutputTypeDef",
    "UpdateEnabledControlOutputTypeDef",
    "UpdateLandingZoneOutputTypeDef",
    "EnableBaselineInputRequestTypeDef",
    "UpdateEnabledBaselineInputRequestTypeDef",
    "EnableControlInputRequestTypeDef",
    "UpdateEnabledControlInputRequestTypeDef",
    "EnabledBaselineDetailsTypeDef",
    "EnabledBaselineSummaryTypeDef",
    "EnabledControlSummaryTypeDef",
    "ListEnabledBaselinesInputRequestTypeDef",
    "EnabledControlDetailsTypeDef",
    "ListEnabledControlsInputRequestTypeDef",
    "GetLandingZoneOperationOutputTypeDef",
    "LandingZoneDetailTypeDef",
    "ListLandingZoneOperationsInputRequestTypeDef",
    "ListLandingZoneOperationsOutputTypeDef",
    "ListLandingZonesOutputTypeDef",
    "ListBaselinesInputListBaselinesPaginateTypeDef",
    "ListControlOperationsInputListControlOperationsPaginateTypeDef",
    "ListEnabledBaselinesInputListEnabledBaselinesPaginateTypeDef",
    "ListEnabledControlsInputListEnabledControlsPaginateTypeDef",
    "ListLandingZoneOperationsInputListLandingZoneOperationsPaginateTypeDef",
    "ListLandingZonesInputListLandingZonesPaginateTypeDef",
    "GetEnabledBaselineOutputTypeDef",
    "ListEnabledBaselinesOutputTypeDef",
    "ListEnabledControlsOutputTypeDef",
    "GetEnabledControlOutputTypeDef",
    "GetLandingZoneOutputTypeDef",
)

BaselineOperationTypeDef = TypedDict(
    "BaselineOperationTypeDef",
    {
        "endTime": NotRequired[datetime],
        "operationIdentifier": NotRequired[str],
        "operationType": NotRequired[BaselineOperationTypeType],
        "startTime": NotRequired[datetime],
        "status": NotRequired[BaselineOperationStatusType],
        "statusMessage": NotRequired[str],
    },
)
BaselineSummaryTypeDef = TypedDict(
    "BaselineSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "description": NotRequired[str],
    },
)
ControlOperationFilterTypeDef = TypedDict(
    "ControlOperationFilterTypeDef",
    {
        "controlIdentifiers": NotRequired[Sequence[str]],
        "controlOperationTypes": NotRequired[Sequence[ControlOperationTypeType]],
        "enabledControlIdentifiers": NotRequired[Sequence[str]],
        "statuses": NotRequired[Sequence[ControlOperationStatusType]],
        "targetIdentifiers": NotRequired[Sequence[str]],
    },
)
ControlOperationSummaryTypeDef = TypedDict(
    "ControlOperationSummaryTypeDef",
    {
        "controlIdentifier": NotRequired[str],
        "enabledControlIdentifier": NotRequired[str],
        "endTime": NotRequired[datetime],
        "operationIdentifier": NotRequired[str],
        "operationType": NotRequired[ControlOperationTypeType],
        "startTime": NotRequired[datetime],
        "status": NotRequired[ControlOperationStatusType],
        "statusMessage": NotRequired[str],
        "targetIdentifier": NotRequired[str],
    },
)
ControlOperationTypeDef = TypedDict(
    "ControlOperationTypeDef",
    {
        "controlIdentifier": NotRequired[str],
        "enabledControlIdentifier": NotRequired[str],
        "endTime": NotRequired[datetime],
        "operationIdentifier": NotRequired[str],
        "operationType": NotRequired[ControlOperationTypeType],
        "startTime": NotRequired[datetime],
        "status": NotRequired[ControlOperationStatusType],
        "statusMessage": NotRequired[str],
        "targetIdentifier": NotRequired[str],
    },
)
CreateLandingZoneInputRequestTypeDef = TypedDict(
    "CreateLandingZoneInputRequestTypeDef",
    {
        "manifest": Mapping[str, Any],
        "version": str,
        "tags": NotRequired[Mapping[str, str]],
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
DeleteLandingZoneInputRequestTypeDef = TypedDict(
    "DeleteLandingZoneInputRequestTypeDef",
    {
        "landingZoneIdentifier": str,
    },
)
DisableBaselineInputRequestTypeDef = TypedDict(
    "DisableBaselineInputRequestTypeDef",
    {
        "enabledBaselineIdentifier": str,
    },
)
DisableControlInputRequestTypeDef = TypedDict(
    "DisableControlInputRequestTypeDef",
    {
        "controlIdentifier": str,
        "targetIdentifier": str,
    },
)
DriftStatusSummaryTypeDef = TypedDict(
    "DriftStatusSummaryTypeDef",
    {
        "driftStatus": NotRequired[DriftStatusType],
    },
)
EnabledBaselineParameterTypeDef = TypedDict(
    "EnabledBaselineParameterTypeDef",
    {
        "key": str,
        "value": Mapping[str, Any],
    },
)
EnabledControlParameterTypeDef = TypedDict(
    "EnabledControlParameterTypeDef",
    {
        "key": str,
        "value": Mapping[str, Any],
    },
)
EnabledBaselineParameterSummaryTypeDef = TypedDict(
    "EnabledBaselineParameterSummaryTypeDef",
    {
        "key": str,
        "value": Dict[str, Any],
    },
)
EnablementStatusSummaryTypeDef = TypedDict(
    "EnablementStatusSummaryTypeDef",
    {
        "lastOperationIdentifier": NotRequired[str],
        "status": NotRequired[EnablementStatusType],
    },
)
EnabledBaselineFilterTypeDef = TypedDict(
    "EnabledBaselineFilterTypeDef",
    {
        "baselineIdentifiers": NotRequired[Sequence[str]],
        "targetIdentifiers": NotRequired[Sequence[str]],
    },
)
EnabledControlParameterSummaryTypeDef = TypedDict(
    "EnabledControlParameterSummaryTypeDef",
    {
        "key": str,
        "value": Dict[str, Any],
    },
)
RegionTypeDef = TypedDict(
    "RegionTypeDef",
    {
        "name": NotRequired[str],
    },
)
EnabledControlFilterTypeDef = TypedDict(
    "EnabledControlFilterTypeDef",
    {
        "controlIdentifiers": NotRequired[Sequence[str]],
        "driftStatuses": NotRequired[Sequence[DriftStatusType]],
        "statuses": NotRequired[Sequence[EnablementStatusType]],
    },
)
GetBaselineInputRequestTypeDef = TypedDict(
    "GetBaselineInputRequestTypeDef",
    {
        "baselineIdentifier": str,
    },
)
GetBaselineOperationInputRequestTypeDef = TypedDict(
    "GetBaselineOperationInputRequestTypeDef",
    {
        "operationIdentifier": str,
    },
)
GetControlOperationInputRequestTypeDef = TypedDict(
    "GetControlOperationInputRequestTypeDef",
    {
        "operationIdentifier": str,
    },
)
GetEnabledBaselineInputRequestTypeDef = TypedDict(
    "GetEnabledBaselineInputRequestTypeDef",
    {
        "enabledBaselineIdentifier": str,
    },
)
GetEnabledControlInputRequestTypeDef = TypedDict(
    "GetEnabledControlInputRequestTypeDef",
    {
        "enabledControlIdentifier": str,
    },
)
GetLandingZoneInputRequestTypeDef = TypedDict(
    "GetLandingZoneInputRequestTypeDef",
    {
        "landingZoneIdentifier": str,
    },
)
GetLandingZoneOperationInputRequestTypeDef = TypedDict(
    "GetLandingZoneOperationInputRequestTypeDef",
    {
        "operationIdentifier": str,
    },
)
LandingZoneOperationDetailTypeDef = TypedDict(
    "LandingZoneOperationDetailTypeDef",
    {
        "endTime": NotRequired[datetime],
        "operationIdentifier": NotRequired[str],
        "operationType": NotRequired[LandingZoneOperationTypeType],
        "startTime": NotRequired[datetime],
        "status": NotRequired[LandingZoneOperationStatusType],
        "statusMessage": NotRequired[str],
    },
)
LandingZoneDriftStatusSummaryTypeDef = TypedDict(
    "LandingZoneDriftStatusSummaryTypeDef",
    {
        "status": NotRequired[LandingZoneDriftStatusType],
    },
)
LandingZoneOperationFilterTypeDef = TypedDict(
    "LandingZoneOperationFilterTypeDef",
    {
        "statuses": NotRequired[Sequence[LandingZoneOperationStatusType]],
        "types": NotRequired[Sequence[LandingZoneOperationTypeType]],
    },
)
LandingZoneOperationSummaryTypeDef = TypedDict(
    "LandingZoneOperationSummaryTypeDef",
    {
        "operationIdentifier": NotRequired[str],
        "operationType": NotRequired[LandingZoneOperationTypeType],
        "status": NotRequired[LandingZoneOperationStatusType],
    },
)
LandingZoneSummaryTypeDef = TypedDict(
    "LandingZoneSummaryTypeDef",
    {
        "arn": NotRequired[str],
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
ListBaselinesInputRequestTypeDef = TypedDict(
    "ListBaselinesInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListLandingZonesInputRequestTypeDef = TypedDict(
    "ListLandingZonesInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)
ResetEnabledBaselineInputRequestTypeDef = TypedDict(
    "ResetEnabledBaselineInputRequestTypeDef",
    {
        "enabledBaselineIdentifier": str,
    },
)
ResetLandingZoneInputRequestTypeDef = TypedDict(
    "ResetLandingZoneInputRequestTypeDef",
    {
        "landingZoneIdentifier": str,
    },
)
TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UpdateLandingZoneInputRequestTypeDef = TypedDict(
    "UpdateLandingZoneInputRequestTypeDef",
    {
        "landingZoneIdentifier": str,
        "manifest": Mapping[str, Any],
        "version": str,
    },
)
ListControlOperationsInputRequestTypeDef = TypedDict(
    "ListControlOperationsInputRequestTypeDef",
    {
        "filter": NotRequired[ControlOperationFilterTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
CreateLandingZoneOutputTypeDef = TypedDict(
    "CreateLandingZoneOutputTypeDef",
    {
        "arn": str,
        "operationIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteLandingZoneOutputTypeDef = TypedDict(
    "DeleteLandingZoneOutputTypeDef",
    {
        "operationIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisableBaselineOutputTypeDef = TypedDict(
    "DisableBaselineOutputTypeDef",
    {
        "operationIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisableControlOutputTypeDef = TypedDict(
    "DisableControlOutputTypeDef",
    {
        "operationIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableBaselineOutputTypeDef = TypedDict(
    "EnableBaselineOutputTypeDef",
    {
        "arn": str,
        "operationIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableControlOutputTypeDef = TypedDict(
    "EnableControlOutputTypeDef",
    {
        "arn": str,
        "operationIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBaselineOperationOutputTypeDef = TypedDict(
    "GetBaselineOperationOutputTypeDef",
    {
        "baselineOperation": BaselineOperationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBaselineOutputTypeDef = TypedDict(
    "GetBaselineOutputTypeDef",
    {
        "arn": str,
        "description": str,
        "name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetControlOperationOutputTypeDef = TypedDict(
    "GetControlOperationOutputTypeDef",
    {
        "controlOperation": ControlOperationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListBaselinesOutputTypeDef = TypedDict(
    "ListBaselinesOutputTypeDef",
    {
        "baselines": List[BaselineSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListControlOperationsOutputTypeDef = TypedDict(
    "ListControlOperationsOutputTypeDef",
    {
        "controlOperations": List[ControlOperationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResetEnabledBaselineOutputTypeDef = TypedDict(
    "ResetEnabledBaselineOutputTypeDef",
    {
        "operationIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResetLandingZoneOutputTypeDef = TypedDict(
    "ResetLandingZoneOutputTypeDef",
    {
        "operationIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEnabledBaselineOutputTypeDef = TypedDict(
    "UpdateEnabledBaselineOutputTypeDef",
    {
        "operationIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEnabledControlOutputTypeDef = TypedDict(
    "UpdateEnabledControlOutputTypeDef",
    {
        "operationIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateLandingZoneOutputTypeDef = TypedDict(
    "UpdateLandingZoneOutputTypeDef",
    {
        "operationIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableBaselineInputRequestTypeDef = TypedDict(
    "EnableBaselineInputRequestTypeDef",
    {
        "baselineIdentifier": str,
        "baselineVersion": str,
        "targetIdentifier": str,
        "parameters": NotRequired[Sequence[EnabledBaselineParameterTypeDef]],
        "tags": NotRequired[Mapping[str, str]],
    },
)
UpdateEnabledBaselineInputRequestTypeDef = TypedDict(
    "UpdateEnabledBaselineInputRequestTypeDef",
    {
        "baselineVersion": str,
        "enabledBaselineIdentifier": str,
        "parameters": NotRequired[Sequence[EnabledBaselineParameterTypeDef]],
    },
)
EnableControlInputRequestTypeDef = TypedDict(
    "EnableControlInputRequestTypeDef",
    {
        "controlIdentifier": str,
        "targetIdentifier": str,
        "parameters": NotRequired[Sequence[EnabledControlParameterTypeDef]],
        "tags": NotRequired[Mapping[str, str]],
    },
)
UpdateEnabledControlInputRequestTypeDef = TypedDict(
    "UpdateEnabledControlInputRequestTypeDef",
    {
        "enabledControlIdentifier": str,
        "parameters": Sequence[EnabledControlParameterTypeDef],
    },
)
EnabledBaselineDetailsTypeDef = TypedDict(
    "EnabledBaselineDetailsTypeDef",
    {
        "arn": str,
        "baselineIdentifier": str,
        "statusSummary": EnablementStatusSummaryTypeDef,
        "targetIdentifier": str,
        "baselineVersion": NotRequired[str],
        "parameters": NotRequired[List[EnabledBaselineParameterSummaryTypeDef]],
    },
)
EnabledBaselineSummaryTypeDef = TypedDict(
    "EnabledBaselineSummaryTypeDef",
    {
        "arn": str,
        "baselineIdentifier": str,
        "statusSummary": EnablementStatusSummaryTypeDef,
        "targetIdentifier": str,
        "baselineVersion": NotRequired[str],
    },
)
EnabledControlSummaryTypeDef = TypedDict(
    "EnabledControlSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "controlIdentifier": NotRequired[str],
        "driftStatusSummary": NotRequired[DriftStatusSummaryTypeDef],
        "statusSummary": NotRequired[EnablementStatusSummaryTypeDef],
        "targetIdentifier": NotRequired[str],
    },
)
ListEnabledBaselinesInputRequestTypeDef = TypedDict(
    "ListEnabledBaselinesInputRequestTypeDef",
    {
        "filter": NotRequired[EnabledBaselineFilterTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
EnabledControlDetailsTypeDef = TypedDict(
    "EnabledControlDetailsTypeDef",
    {
        "arn": NotRequired[str],
        "controlIdentifier": NotRequired[str],
        "driftStatusSummary": NotRequired[DriftStatusSummaryTypeDef],
        "parameters": NotRequired[List[EnabledControlParameterSummaryTypeDef]],
        "statusSummary": NotRequired[EnablementStatusSummaryTypeDef],
        "targetIdentifier": NotRequired[str],
        "targetRegions": NotRequired[List[RegionTypeDef]],
    },
)
ListEnabledControlsInputRequestTypeDef = TypedDict(
    "ListEnabledControlsInputRequestTypeDef",
    {
        "filter": NotRequired[EnabledControlFilterTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "targetIdentifier": NotRequired[str],
    },
)
GetLandingZoneOperationOutputTypeDef = TypedDict(
    "GetLandingZoneOperationOutputTypeDef",
    {
        "operationDetails": LandingZoneOperationDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LandingZoneDetailTypeDef = TypedDict(
    "LandingZoneDetailTypeDef",
    {
        "manifest": Dict[str, Any],
        "version": str,
        "arn": NotRequired[str],
        "driftStatus": NotRequired[LandingZoneDriftStatusSummaryTypeDef],
        "latestAvailableVersion": NotRequired[str],
        "status": NotRequired[LandingZoneStatusType],
    },
)
ListLandingZoneOperationsInputRequestTypeDef = TypedDict(
    "ListLandingZoneOperationsInputRequestTypeDef",
    {
        "filter": NotRequired[LandingZoneOperationFilterTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListLandingZoneOperationsOutputTypeDef = TypedDict(
    "ListLandingZoneOperationsOutputTypeDef",
    {
        "landingZoneOperations": List[LandingZoneOperationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListLandingZonesOutputTypeDef = TypedDict(
    "ListLandingZonesOutputTypeDef",
    {
        "landingZones": List[LandingZoneSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListBaselinesInputListBaselinesPaginateTypeDef = TypedDict(
    "ListBaselinesInputListBaselinesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListControlOperationsInputListControlOperationsPaginateTypeDef = TypedDict(
    "ListControlOperationsInputListControlOperationsPaginateTypeDef",
    {
        "filter": NotRequired[ControlOperationFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEnabledBaselinesInputListEnabledBaselinesPaginateTypeDef = TypedDict(
    "ListEnabledBaselinesInputListEnabledBaselinesPaginateTypeDef",
    {
        "filter": NotRequired[EnabledBaselineFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEnabledControlsInputListEnabledControlsPaginateTypeDef = TypedDict(
    "ListEnabledControlsInputListEnabledControlsPaginateTypeDef",
    {
        "filter": NotRequired[EnabledControlFilterTypeDef],
        "targetIdentifier": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListLandingZoneOperationsInputListLandingZoneOperationsPaginateTypeDef = TypedDict(
    "ListLandingZoneOperationsInputListLandingZoneOperationsPaginateTypeDef",
    {
        "filter": NotRequired[LandingZoneOperationFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListLandingZonesInputListLandingZonesPaginateTypeDef = TypedDict(
    "ListLandingZonesInputListLandingZonesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetEnabledBaselineOutputTypeDef = TypedDict(
    "GetEnabledBaselineOutputTypeDef",
    {
        "enabledBaselineDetails": EnabledBaselineDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEnabledBaselinesOutputTypeDef = TypedDict(
    "ListEnabledBaselinesOutputTypeDef",
    {
        "enabledBaselines": List[EnabledBaselineSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEnabledControlsOutputTypeDef = TypedDict(
    "ListEnabledControlsOutputTypeDef",
    {
        "enabledControls": List[EnabledControlSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEnabledControlOutputTypeDef = TypedDict(
    "GetEnabledControlOutputTypeDef",
    {
        "enabledControlDetails": EnabledControlDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLandingZoneOutputTypeDef = TypedDict(
    "GetLandingZoneOutputTypeDef",
    {
        "landingZone": LandingZoneDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
