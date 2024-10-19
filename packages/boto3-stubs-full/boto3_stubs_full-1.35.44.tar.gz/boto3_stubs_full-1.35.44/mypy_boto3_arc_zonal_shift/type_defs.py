"""
Type annotations for arc-zonal-shift service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/type_defs/)

Usage::

    ```python
    from mypy_boto3_arc_zonal_shift.type_defs import AutoshiftInResourceTypeDef

    data: AutoshiftInResourceTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import (
    AppliedStatusType,
    AutoshiftAppliedStatusType,
    AutoshiftExecutionStatusType,
    AutoshiftObserverNotificationStatusType,
    PracticeRunOutcomeType,
    ZonalAutoshiftStatusType,
    ZonalShiftStatusType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AutoshiftInResourceTypeDef",
    "AutoshiftSummaryTypeDef",
    "CancelZonalShiftRequestRequestTypeDef",
    "ControlConditionTypeDef",
    "ResponseMetadataTypeDef",
    "DeletePracticeRunConfigurationRequestRequestTypeDef",
    "GetManagedResourceRequestRequestTypeDef",
    "ZonalShiftInResourceTypeDef",
    "PaginatorConfigTypeDef",
    "ListAutoshiftsRequestRequestTypeDef",
    "ListManagedResourcesRequestRequestTypeDef",
    "ListZonalShiftsRequestRequestTypeDef",
    "ZonalShiftSummaryTypeDef",
    "StartZonalShiftRequestRequestTypeDef",
    "UpdateAutoshiftObserverNotificationStatusRequestRequestTypeDef",
    "UpdateZonalAutoshiftConfigurationRequestRequestTypeDef",
    "UpdateZonalShiftRequestRequestTypeDef",
    "CreatePracticeRunConfigurationRequestRequestTypeDef",
    "PracticeRunConfigurationTypeDef",
    "UpdatePracticeRunConfigurationRequestRequestTypeDef",
    "DeletePracticeRunConfigurationResponseTypeDef",
    "GetAutoshiftObserverNotificationStatusResponseTypeDef",
    "ListAutoshiftsResponseTypeDef",
    "UpdateAutoshiftObserverNotificationStatusResponseTypeDef",
    "UpdateZonalAutoshiftConfigurationResponseTypeDef",
    "ZonalShiftTypeDef",
    "ManagedResourceSummaryTypeDef",
    "ListAutoshiftsRequestListAutoshiftsPaginateTypeDef",
    "ListManagedResourcesRequestListManagedResourcesPaginateTypeDef",
    "ListZonalShiftsRequestListZonalShiftsPaginateTypeDef",
    "ListZonalShiftsResponseTypeDef",
    "CreatePracticeRunConfigurationResponseTypeDef",
    "GetManagedResourceResponseTypeDef",
    "UpdatePracticeRunConfigurationResponseTypeDef",
    "ListManagedResourcesResponseTypeDef",
)

AutoshiftInResourceTypeDef = TypedDict(
    "AutoshiftInResourceTypeDef",
    {
        "appliedStatus": AutoshiftAppliedStatusType,
        "awayFrom": str,
        "startTime": datetime,
    },
)
AutoshiftSummaryTypeDef = TypedDict(
    "AutoshiftSummaryTypeDef",
    {
        "awayFrom": str,
        "endTime": datetime,
        "startTime": datetime,
        "status": AutoshiftExecutionStatusType,
    },
)
CancelZonalShiftRequestRequestTypeDef = TypedDict(
    "CancelZonalShiftRequestRequestTypeDef",
    {
        "zonalShiftId": str,
    },
)
ControlConditionTypeDef = TypedDict(
    "ControlConditionTypeDef",
    {
        "alarmIdentifier": str,
        "type": Literal["CLOUDWATCH"],
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
DeletePracticeRunConfigurationRequestRequestTypeDef = TypedDict(
    "DeletePracticeRunConfigurationRequestRequestTypeDef",
    {
        "resourceIdentifier": str,
    },
)
GetManagedResourceRequestRequestTypeDef = TypedDict(
    "GetManagedResourceRequestRequestTypeDef",
    {
        "resourceIdentifier": str,
    },
)
ZonalShiftInResourceTypeDef = TypedDict(
    "ZonalShiftInResourceTypeDef",
    {
        "appliedStatus": AppliedStatusType,
        "awayFrom": str,
        "comment": str,
        "expiryTime": datetime,
        "resourceIdentifier": str,
        "startTime": datetime,
        "zonalShiftId": str,
        "practiceRunOutcome": NotRequired[PracticeRunOutcomeType],
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
ListAutoshiftsRequestRequestTypeDef = TypedDict(
    "ListAutoshiftsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "status": NotRequired[AutoshiftExecutionStatusType],
    },
)
ListManagedResourcesRequestRequestTypeDef = TypedDict(
    "ListManagedResourcesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListZonalShiftsRequestRequestTypeDef = TypedDict(
    "ListZonalShiftsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "resourceIdentifier": NotRequired[str],
        "status": NotRequired[ZonalShiftStatusType],
    },
)
ZonalShiftSummaryTypeDef = TypedDict(
    "ZonalShiftSummaryTypeDef",
    {
        "awayFrom": str,
        "comment": str,
        "expiryTime": datetime,
        "resourceIdentifier": str,
        "startTime": datetime,
        "status": ZonalShiftStatusType,
        "zonalShiftId": str,
        "practiceRunOutcome": NotRequired[PracticeRunOutcomeType],
    },
)
StartZonalShiftRequestRequestTypeDef = TypedDict(
    "StartZonalShiftRequestRequestTypeDef",
    {
        "awayFrom": str,
        "comment": str,
        "expiresIn": str,
        "resourceIdentifier": str,
    },
)
UpdateAutoshiftObserverNotificationStatusRequestRequestTypeDef = TypedDict(
    "UpdateAutoshiftObserverNotificationStatusRequestRequestTypeDef",
    {
        "status": AutoshiftObserverNotificationStatusType,
    },
)
UpdateZonalAutoshiftConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateZonalAutoshiftConfigurationRequestRequestTypeDef",
    {
        "resourceIdentifier": str,
        "zonalAutoshiftStatus": ZonalAutoshiftStatusType,
    },
)
UpdateZonalShiftRequestRequestTypeDef = TypedDict(
    "UpdateZonalShiftRequestRequestTypeDef",
    {
        "zonalShiftId": str,
        "comment": NotRequired[str],
        "expiresIn": NotRequired[str],
    },
)
CreatePracticeRunConfigurationRequestRequestTypeDef = TypedDict(
    "CreatePracticeRunConfigurationRequestRequestTypeDef",
    {
        "outcomeAlarms": Sequence[ControlConditionTypeDef],
        "resourceIdentifier": str,
        "blockedDates": NotRequired[Sequence[str]],
        "blockedWindows": NotRequired[Sequence[str]],
        "blockingAlarms": NotRequired[Sequence[ControlConditionTypeDef]],
    },
)
PracticeRunConfigurationTypeDef = TypedDict(
    "PracticeRunConfigurationTypeDef",
    {
        "outcomeAlarms": List[ControlConditionTypeDef],
        "blockedDates": NotRequired[List[str]],
        "blockedWindows": NotRequired[List[str]],
        "blockingAlarms": NotRequired[List[ControlConditionTypeDef]],
    },
)
UpdatePracticeRunConfigurationRequestRequestTypeDef = TypedDict(
    "UpdatePracticeRunConfigurationRequestRequestTypeDef",
    {
        "resourceIdentifier": str,
        "blockedDates": NotRequired[Sequence[str]],
        "blockedWindows": NotRequired[Sequence[str]],
        "blockingAlarms": NotRequired[Sequence[ControlConditionTypeDef]],
        "outcomeAlarms": NotRequired[Sequence[ControlConditionTypeDef]],
    },
)
DeletePracticeRunConfigurationResponseTypeDef = TypedDict(
    "DeletePracticeRunConfigurationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "zonalAutoshiftStatus": ZonalAutoshiftStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAutoshiftObserverNotificationStatusResponseTypeDef = TypedDict(
    "GetAutoshiftObserverNotificationStatusResponseTypeDef",
    {
        "status": AutoshiftObserverNotificationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAutoshiftsResponseTypeDef = TypedDict(
    "ListAutoshiftsResponseTypeDef",
    {
        "items": List[AutoshiftSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAutoshiftObserverNotificationStatusResponseTypeDef = TypedDict(
    "UpdateAutoshiftObserverNotificationStatusResponseTypeDef",
    {
        "status": AutoshiftObserverNotificationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateZonalAutoshiftConfigurationResponseTypeDef = TypedDict(
    "UpdateZonalAutoshiftConfigurationResponseTypeDef",
    {
        "resourceIdentifier": str,
        "zonalAutoshiftStatus": ZonalAutoshiftStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ZonalShiftTypeDef = TypedDict(
    "ZonalShiftTypeDef",
    {
        "awayFrom": str,
        "comment": str,
        "expiryTime": datetime,
        "resourceIdentifier": str,
        "startTime": datetime,
        "status": ZonalShiftStatusType,
        "zonalShiftId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ManagedResourceSummaryTypeDef = TypedDict(
    "ManagedResourceSummaryTypeDef",
    {
        "availabilityZones": List[str],
        "appliedWeights": NotRequired[Dict[str, float]],
        "arn": NotRequired[str],
        "autoshifts": NotRequired[List[AutoshiftInResourceTypeDef]],
        "name": NotRequired[str],
        "practiceRunStatus": NotRequired[ZonalAutoshiftStatusType],
        "zonalAutoshiftStatus": NotRequired[ZonalAutoshiftStatusType],
        "zonalShifts": NotRequired[List[ZonalShiftInResourceTypeDef]],
    },
)
ListAutoshiftsRequestListAutoshiftsPaginateTypeDef = TypedDict(
    "ListAutoshiftsRequestListAutoshiftsPaginateTypeDef",
    {
        "status": NotRequired[AutoshiftExecutionStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListManagedResourcesRequestListManagedResourcesPaginateTypeDef = TypedDict(
    "ListManagedResourcesRequestListManagedResourcesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListZonalShiftsRequestListZonalShiftsPaginateTypeDef = TypedDict(
    "ListZonalShiftsRequestListZonalShiftsPaginateTypeDef",
    {
        "resourceIdentifier": NotRequired[str],
        "status": NotRequired[ZonalShiftStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListZonalShiftsResponseTypeDef = TypedDict(
    "ListZonalShiftsResponseTypeDef",
    {
        "items": List[ZonalShiftSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePracticeRunConfigurationResponseTypeDef = TypedDict(
    "CreatePracticeRunConfigurationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "practiceRunConfiguration": PracticeRunConfigurationTypeDef,
        "zonalAutoshiftStatus": ZonalAutoshiftStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetManagedResourceResponseTypeDef = TypedDict(
    "GetManagedResourceResponseTypeDef",
    {
        "appliedWeights": Dict[str, float],
        "arn": str,
        "autoshifts": List[AutoshiftInResourceTypeDef],
        "name": str,
        "practiceRunConfiguration": PracticeRunConfigurationTypeDef,
        "zonalAutoshiftStatus": ZonalAutoshiftStatusType,
        "zonalShifts": List[ZonalShiftInResourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePracticeRunConfigurationResponseTypeDef = TypedDict(
    "UpdatePracticeRunConfigurationResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "practiceRunConfiguration": PracticeRunConfigurationTypeDef,
        "zonalAutoshiftStatus": ZonalAutoshiftStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListManagedResourcesResponseTypeDef = TypedDict(
    "ListManagedResourcesResponseTypeDef",
    {
        "items": List[ManagedResourceSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
