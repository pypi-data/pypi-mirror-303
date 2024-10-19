"""
Type annotations for cur service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cur/type_defs/)

Usage::

    ```python
    from mypy_boto3_cur.type_defs import DeleteReportDefinitionRequestRequestTypeDef

    data: DeleteReportDefinitionRequestRequestTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Sequence

from .literals import (
    AdditionalArtifactType,
    AWSRegionType,
    CompressionFormatType,
    LastStatusType,
    ReportFormatType,
    ReportVersioningType,
    SchemaElementType,
    TimeUnitType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "DeleteReportDefinitionRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeReportDefinitionsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagTypeDef",
    "ReportStatusTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "DeleteReportDefinitionResponseTypeDef",
    "DescribeReportDefinitionsRequestDescribeReportDefinitionsPaginateTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "ReportDefinitionOutputTypeDef",
    "ReportDefinitionTypeDef",
    "DescribeReportDefinitionsResponseTypeDef",
    "ModifyReportDefinitionRequestRequestTypeDef",
    "PutReportDefinitionRequestRequestTypeDef",
)

DeleteReportDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteReportDefinitionRequestRequestTypeDef",
    {
        "ReportName": str,
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
PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
    },
)
DescribeReportDefinitionsRequestRequestTypeDef = TypedDict(
    "DescribeReportDefinitionsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ReportName": str,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
ReportStatusTypeDef = TypedDict(
    "ReportStatusTypeDef",
    {
        "lastDelivery": NotRequired[str],
        "lastStatus": NotRequired[LastStatusType],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ReportName": str,
        "TagKeys": Sequence[str],
    },
)
DeleteReportDefinitionResponseTypeDef = TypedDict(
    "DeleteReportDefinitionResponseTypeDef",
    {
        "ResponseMessage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeReportDefinitionsRequestDescribeReportDefinitionsPaginateTypeDef = TypedDict(
    "DescribeReportDefinitionsRequestDescribeReportDefinitionsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ReportName": str,
        "Tags": Sequence[TagTypeDef],
    },
)
ReportDefinitionOutputTypeDef = TypedDict(
    "ReportDefinitionOutputTypeDef",
    {
        "ReportName": str,
        "TimeUnit": TimeUnitType,
        "Format": ReportFormatType,
        "Compression": CompressionFormatType,
        "AdditionalSchemaElements": List[SchemaElementType],
        "S3Bucket": str,
        "S3Prefix": str,
        "S3Region": AWSRegionType,
        "AdditionalArtifacts": NotRequired[List[AdditionalArtifactType]],
        "RefreshClosedReports": NotRequired[bool],
        "ReportVersioning": NotRequired[ReportVersioningType],
        "BillingViewArn": NotRequired[str],
        "ReportStatus": NotRequired[ReportStatusTypeDef],
    },
)
ReportDefinitionTypeDef = TypedDict(
    "ReportDefinitionTypeDef",
    {
        "ReportName": str,
        "TimeUnit": TimeUnitType,
        "Format": ReportFormatType,
        "Compression": CompressionFormatType,
        "AdditionalSchemaElements": Sequence[SchemaElementType],
        "S3Bucket": str,
        "S3Prefix": str,
        "S3Region": AWSRegionType,
        "AdditionalArtifacts": NotRequired[Sequence[AdditionalArtifactType]],
        "RefreshClosedReports": NotRequired[bool],
        "ReportVersioning": NotRequired[ReportVersioningType],
        "BillingViewArn": NotRequired[str],
        "ReportStatus": NotRequired[ReportStatusTypeDef],
    },
)
DescribeReportDefinitionsResponseTypeDef = TypedDict(
    "DescribeReportDefinitionsResponseTypeDef",
    {
        "ReportDefinitions": List[ReportDefinitionOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ModifyReportDefinitionRequestRequestTypeDef = TypedDict(
    "ModifyReportDefinitionRequestRequestTypeDef",
    {
        "ReportName": str,
        "ReportDefinition": ReportDefinitionTypeDef,
    },
)
PutReportDefinitionRequestRequestTypeDef = TypedDict(
    "PutReportDefinitionRequestRequestTypeDef",
    {
        "ReportDefinition": ReportDefinitionTypeDef,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
