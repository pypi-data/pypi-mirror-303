"""
Type annotations for artifact service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_artifact/type_defs/)

Usage::

    ```python
    from mypy_boto3_artifact.type_defs import AccountSettingsTypeDef

    data: AccountSettingsTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List

from .literals import (
    AcceptanceTypeType,
    NotificationSubscriptionStatusType,
    PublishedStateType,
    UploadStateType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AccountSettingsTypeDef",
    "ResponseMetadataTypeDef",
    "GetReportMetadataRequestRequestTypeDef",
    "ReportDetailTypeDef",
    "GetReportRequestRequestTypeDef",
    "GetTermForReportRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListReportsRequestRequestTypeDef",
    "ReportSummaryTypeDef",
    "PutAccountSettingsRequestRequestTypeDef",
    "GetAccountSettingsResponseTypeDef",
    "GetReportResponseTypeDef",
    "GetTermForReportResponseTypeDef",
    "PutAccountSettingsResponseTypeDef",
    "GetReportMetadataResponseTypeDef",
    "ListReportsRequestListReportsPaginateTypeDef",
    "ListReportsResponseTypeDef",
)

AccountSettingsTypeDef = TypedDict(
    "AccountSettingsTypeDef",
    {
        "notificationSubscriptionStatus": NotRequired[NotificationSubscriptionStatusType],
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
GetReportMetadataRequestRequestTypeDef = TypedDict(
    "GetReportMetadataRequestRequestTypeDef",
    {
        "reportId": str,
        "reportVersion": NotRequired[int],
    },
)
ReportDetailTypeDef = TypedDict(
    "ReportDetailTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "periodStart": NotRequired[datetime],
        "periodEnd": NotRequired[datetime],
        "createdAt": NotRequired[datetime],
        "lastModifiedAt": NotRequired[datetime],
        "deletedAt": NotRequired[datetime],
        "state": NotRequired[PublishedStateType],
        "arn": NotRequired[str],
        "series": NotRequired[str],
        "category": NotRequired[str],
        "companyName": NotRequired[str],
        "productName": NotRequired[str],
        "termArn": NotRequired[str],
        "version": NotRequired[int],
        "acceptanceType": NotRequired[AcceptanceTypeType],
        "sequenceNumber": NotRequired[int],
        "uploadState": NotRequired[UploadStateType],
        "statusMessage": NotRequired[str],
    },
)
GetReportRequestRequestTypeDef = TypedDict(
    "GetReportRequestRequestTypeDef",
    {
        "reportId": str,
        "termToken": str,
        "reportVersion": NotRequired[int],
    },
)
GetTermForReportRequestRequestTypeDef = TypedDict(
    "GetTermForReportRequestRequestTypeDef",
    {
        "reportId": str,
        "reportVersion": NotRequired[int],
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
ListReportsRequestRequestTypeDef = TypedDict(
    "ListReportsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ReportSummaryTypeDef = TypedDict(
    "ReportSummaryTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "state": NotRequired[PublishedStateType],
        "arn": NotRequired[str],
        "version": NotRequired[int],
        "uploadState": NotRequired[UploadStateType],
        "description": NotRequired[str],
        "periodStart": NotRequired[datetime],
        "periodEnd": NotRequired[datetime],
        "series": NotRequired[str],
        "category": NotRequired[str],
        "companyName": NotRequired[str],
        "productName": NotRequired[str],
        "statusMessage": NotRequired[str],
        "acceptanceType": NotRequired[AcceptanceTypeType],
    },
)
PutAccountSettingsRequestRequestTypeDef = TypedDict(
    "PutAccountSettingsRequestRequestTypeDef",
    {
        "notificationSubscriptionStatus": NotRequired[NotificationSubscriptionStatusType],
    },
)
GetAccountSettingsResponseTypeDef = TypedDict(
    "GetAccountSettingsResponseTypeDef",
    {
        "accountSettings": AccountSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetReportResponseTypeDef = TypedDict(
    "GetReportResponseTypeDef",
    {
        "documentPresignedUrl": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTermForReportResponseTypeDef = TypedDict(
    "GetTermForReportResponseTypeDef",
    {
        "documentPresignedUrl": str,
        "termToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutAccountSettingsResponseTypeDef = TypedDict(
    "PutAccountSettingsResponseTypeDef",
    {
        "accountSettings": AccountSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetReportMetadataResponseTypeDef = TypedDict(
    "GetReportMetadataResponseTypeDef",
    {
        "reportDetails": ReportDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListReportsRequestListReportsPaginateTypeDef = TypedDict(
    "ListReportsRequestListReportsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListReportsResponseTypeDef = TypedDict(
    "ListReportsResponseTypeDef",
    {
        "reports": List[ReportSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
