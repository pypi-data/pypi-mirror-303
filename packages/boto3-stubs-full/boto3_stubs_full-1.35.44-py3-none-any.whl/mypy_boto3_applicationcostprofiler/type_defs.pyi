"""
Type annotations for applicationcostprofiler service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_applicationcostprofiler/type_defs/)

Usage::

    ```python
    from mypy_boto3_applicationcostprofiler.type_defs import DeleteReportDefinitionRequestRequestTypeDef

    data: DeleteReportDefinitionRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List

from .literals import FormatType, ReportFrequencyType, S3BucketRegionType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "DeleteReportDefinitionRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "GetReportDefinitionRequestRequestTypeDef",
    "S3LocationTypeDef",
    "SourceS3LocationTypeDef",
    "PaginatorConfigTypeDef",
    "ListReportDefinitionsRequestRequestTypeDef",
    "DeleteReportDefinitionResultTypeDef",
    "ImportApplicationUsageResultTypeDef",
    "PutReportDefinitionResultTypeDef",
    "UpdateReportDefinitionResultTypeDef",
    "GetReportDefinitionResultTypeDef",
    "PutReportDefinitionRequestRequestTypeDef",
    "ReportDefinitionTypeDef",
    "UpdateReportDefinitionRequestRequestTypeDef",
    "ImportApplicationUsageRequestRequestTypeDef",
    "ListReportDefinitionsRequestListReportDefinitionsPaginateTypeDef",
    "ListReportDefinitionsResultTypeDef",
)

DeleteReportDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteReportDefinitionRequestRequestTypeDef",
    {
        "reportId": str,
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
GetReportDefinitionRequestRequestTypeDef = TypedDict(
    "GetReportDefinitionRequestRequestTypeDef",
    {
        "reportId": str,
    },
)
S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucket": str,
        "prefix": str,
    },
)
SourceS3LocationTypeDef = TypedDict(
    "SourceS3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
        "region": NotRequired[S3BucketRegionType],
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
ListReportDefinitionsRequestRequestTypeDef = TypedDict(
    "ListReportDefinitionsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
DeleteReportDefinitionResultTypeDef = TypedDict(
    "DeleteReportDefinitionResultTypeDef",
    {
        "reportId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportApplicationUsageResultTypeDef = TypedDict(
    "ImportApplicationUsageResultTypeDef",
    {
        "importId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutReportDefinitionResultTypeDef = TypedDict(
    "PutReportDefinitionResultTypeDef",
    {
        "reportId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateReportDefinitionResultTypeDef = TypedDict(
    "UpdateReportDefinitionResultTypeDef",
    {
        "reportId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetReportDefinitionResultTypeDef = TypedDict(
    "GetReportDefinitionResultTypeDef",
    {
        "reportId": str,
        "reportDescription": str,
        "reportFrequency": ReportFrequencyType,
        "format": FormatType,
        "destinationS3Location": S3LocationTypeDef,
        "createdAt": datetime,
        "lastUpdated": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutReportDefinitionRequestRequestTypeDef = TypedDict(
    "PutReportDefinitionRequestRequestTypeDef",
    {
        "reportId": str,
        "reportDescription": str,
        "reportFrequency": ReportFrequencyType,
        "format": FormatType,
        "destinationS3Location": S3LocationTypeDef,
    },
)
ReportDefinitionTypeDef = TypedDict(
    "ReportDefinitionTypeDef",
    {
        "reportId": NotRequired[str],
        "reportDescription": NotRequired[str],
        "reportFrequency": NotRequired[ReportFrequencyType],
        "format": NotRequired[FormatType],
        "destinationS3Location": NotRequired[S3LocationTypeDef],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
    },
)
UpdateReportDefinitionRequestRequestTypeDef = TypedDict(
    "UpdateReportDefinitionRequestRequestTypeDef",
    {
        "reportId": str,
        "reportDescription": str,
        "reportFrequency": ReportFrequencyType,
        "format": FormatType,
        "destinationS3Location": S3LocationTypeDef,
    },
)
ImportApplicationUsageRequestRequestTypeDef = TypedDict(
    "ImportApplicationUsageRequestRequestTypeDef",
    {
        "sourceS3Location": SourceS3LocationTypeDef,
    },
)
ListReportDefinitionsRequestListReportDefinitionsPaginateTypeDef = TypedDict(
    "ListReportDefinitionsRequestListReportDefinitionsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListReportDefinitionsResultTypeDef = TypedDict(
    "ListReportDefinitionsResultTypeDef",
    {
        "reportDefinitions": List[ReportDefinitionTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
