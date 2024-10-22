"""
Type annotations for bcm-data-exports service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_data_exports/type_defs/)

Usage::

    ```python
    from mypy_boto3_bcm_data_exports.type_defs import ColumnTypeDef

    data: ColumnTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    CompressionOptionType,
    ExecutionStatusCodeType,
    ExecutionStatusReasonType,
    ExportStatusCodeType,
    FormatOptionType,
    OverwriteOptionType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "ColumnTypeDef",
    "ResourceTagTypeDef",
    "ResponseMetadataTypeDef",
    "DataQueryOutputTypeDef",
    "DataQueryTypeDef",
    "DeleteExportRequestRequestTypeDef",
    "ExecutionStatusTypeDef",
    "RefreshCadenceTypeDef",
    "ExportStatusTypeDef",
    "GetExecutionRequestRequestTypeDef",
    "GetExportRequestRequestTypeDef",
    "GetTableRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListExecutionsRequestRequestTypeDef",
    "ListExportsRequestRequestTypeDef",
    "ListTablesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "S3OutputConfigurationsTypeDef",
    "TablePropertyDescriptionTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateExportResponseTypeDef",
    "DeleteExportResponseTypeDef",
    "GetTableResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "UpdateExportResponseTypeDef",
    "DataQueryUnionTypeDef",
    "ExecutionReferenceTypeDef",
    "ExportReferenceTypeDef",
    "ListExecutionsRequestListExecutionsPaginateTypeDef",
    "ListExportsRequestListExportsPaginateTypeDef",
    "ListTablesRequestListTablesPaginateTypeDef",
    "S3DestinationTypeDef",
    "TableTypeDef",
    "ListExecutionsResponseTypeDef",
    "ListExportsResponseTypeDef",
    "DestinationConfigurationsTypeDef",
    "ListTablesResponseTypeDef",
    "ExportOutputTypeDef",
    "ExportTypeDef",
    "GetExecutionResponseTypeDef",
    "GetExportResponseTypeDef",
    "CreateExportRequestRequestTypeDef",
    "UpdateExportRequestRequestTypeDef",
)

ColumnTypeDef = TypedDict(
    "ColumnTypeDef",
    {
        "Description": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[str],
    },
)
ResourceTagTypeDef = TypedDict(
    "ResourceTagTypeDef",
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
DataQueryOutputTypeDef = TypedDict(
    "DataQueryOutputTypeDef",
    {
        "QueryStatement": str,
        "TableConfigurations": NotRequired[Dict[str, Dict[str, str]]],
    },
)
DataQueryTypeDef = TypedDict(
    "DataQueryTypeDef",
    {
        "QueryStatement": str,
        "TableConfigurations": NotRequired[Mapping[str, Mapping[str, str]]],
    },
)
DeleteExportRequestRequestTypeDef = TypedDict(
    "DeleteExportRequestRequestTypeDef",
    {
        "ExportArn": str,
    },
)
ExecutionStatusTypeDef = TypedDict(
    "ExecutionStatusTypeDef",
    {
        "CompletedAt": NotRequired[datetime],
        "CreatedAt": NotRequired[datetime],
        "LastUpdatedAt": NotRequired[datetime],
        "StatusCode": NotRequired[ExecutionStatusCodeType],
        "StatusReason": NotRequired[ExecutionStatusReasonType],
    },
)
RefreshCadenceTypeDef = TypedDict(
    "RefreshCadenceTypeDef",
    {
        "Frequency": Literal["SYNCHRONOUS"],
    },
)
ExportStatusTypeDef = TypedDict(
    "ExportStatusTypeDef",
    {
        "CreatedAt": NotRequired[datetime],
        "LastRefreshedAt": NotRequired[datetime],
        "LastUpdatedAt": NotRequired[datetime],
        "StatusCode": NotRequired[ExportStatusCodeType],
        "StatusReason": NotRequired[ExecutionStatusReasonType],
    },
)
GetExecutionRequestRequestTypeDef = TypedDict(
    "GetExecutionRequestRequestTypeDef",
    {
        "ExecutionId": str,
        "ExportArn": str,
    },
)
GetExportRequestRequestTypeDef = TypedDict(
    "GetExportRequestRequestTypeDef",
    {
        "ExportArn": str,
    },
)
GetTableRequestRequestTypeDef = TypedDict(
    "GetTableRequestRequestTypeDef",
    {
        "TableName": str,
        "TableProperties": NotRequired[Mapping[str, str]],
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
ListExecutionsRequestRequestTypeDef = TypedDict(
    "ListExecutionsRequestRequestTypeDef",
    {
        "ExportArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListExportsRequestRequestTypeDef = TypedDict(
    "ListExportsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTablesRequestRequestTypeDef = TypedDict(
    "ListTablesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
S3OutputConfigurationsTypeDef = TypedDict(
    "S3OutputConfigurationsTypeDef",
    {
        "Compression": CompressionOptionType,
        "Format": FormatOptionType,
        "OutputType": Literal["CUSTOM"],
        "Overwrite": OverwriteOptionType,
    },
)
TablePropertyDescriptionTypeDef = TypedDict(
    "TablePropertyDescriptionTypeDef",
    {
        "DefaultValue": NotRequired[str],
        "Description": NotRequired[str],
        "Name": NotRequired[str],
        "ValidValues": NotRequired[List[str]],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "ResourceTagKeys": Sequence[str],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "ResourceTags": Sequence[ResourceTagTypeDef],
    },
)
CreateExportResponseTypeDef = TypedDict(
    "CreateExportResponseTypeDef",
    {
        "ExportArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteExportResponseTypeDef = TypedDict(
    "DeleteExportResponseTypeDef",
    {
        "ExportArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTableResponseTypeDef = TypedDict(
    "GetTableResponseTypeDef",
    {
        "Description": str,
        "Schema": List[ColumnTypeDef],
        "TableName": str,
        "TableProperties": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "ResourceTags": List[ResourceTagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateExportResponseTypeDef = TypedDict(
    "UpdateExportResponseTypeDef",
    {
        "ExportArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DataQueryUnionTypeDef = Union[DataQueryTypeDef, DataQueryOutputTypeDef]
ExecutionReferenceTypeDef = TypedDict(
    "ExecutionReferenceTypeDef",
    {
        "ExecutionId": str,
        "ExecutionStatus": ExecutionStatusTypeDef,
    },
)
ExportReferenceTypeDef = TypedDict(
    "ExportReferenceTypeDef",
    {
        "ExportArn": str,
        "ExportName": str,
        "ExportStatus": ExportStatusTypeDef,
    },
)
ListExecutionsRequestListExecutionsPaginateTypeDef = TypedDict(
    "ListExecutionsRequestListExecutionsPaginateTypeDef",
    {
        "ExportArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListExportsRequestListExportsPaginateTypeDef = TypedDict(
    "ListExportsRequestListExportsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTablesRequestListTablesPaginateTypeDef = TypedDict(
    "ListTablesRequestListTablesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
S3DestinationTypeDef = TypedDict(
    "S3DestinationTypeDef",
    {
        "S3Bucket": str,
        "S3OutputConfigurations": S3OutputConfigurationsTypeDef,
        "S3Prefix": str,
        "S3Region": str,
    },
)
TableTypeDef = TypedDict(
    "TableTypeDef",
    {
        "Description": NotRequired[str],
        "TableName": NotRequired[str],
        "TableProperties": NotRequired[List[TablePropertyDescriptionTypeDef]],
    },
)
ListExecutionsResponseTypeDef = TypedDict(
    "ListExecutionsResponseTypeDef",
    {
        "Executions": List[ExecutionReferenceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListExportsResponseTypeDef = TypedDict(
    "ListExportsResponseTypeDef",
    {
        "Exports": List[ExportReferenceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DestinationConfigurationsTypeDef = TypedDict(
    "DestinationConfigurationsTypeDef",
    {
        "S3Destination": S3DestinationTypeDef,
    },
)
ListTablesResponseTypeDef = TypedDict(
    "ListTablesResponseTypeDef",
    {
        "Tables": List[TableTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ExportOutputTypeDef = TypedDict(
    "ExportOutputTypeDef",
    {
        "DataQuery": DataQueryOutputTypeDef,
        "DestinationConfigurations": DestinationConfigurationsTypeDef,
        "Name": str,
        "RefreshCadence": RefreshCadenceTypeDef,
        "Description": NotRequired[str],
        "ExportArn": NotRequired[str],
    },
)
ExportTypeDef = TypedDict(
    "ExportTypeDef",
    {
        "DataQuery": DataQueryUnionTypeDef,
        "DestinationConfigurations": DestinationConfigurationsTypeDef,
        "Name": str,
        "RefreshCadence": RefreshCadenceTypeDef,
        "Description": NotRequired[str],
        "ExportArn": NotRequired[str],
    },
)
GetExecutionResponseTypeDef = TypedDict(
    "GetExecutionResponseTypeDef",
    {
        "ExecutionId": str,
        "ExecutionStatus": ExecutionStatusTypeDef,
        "Export": ExportOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetExportResponseTypeDef = TypedDict(
    "GetExportResponseTypeDef",
    {
        "Export": ExportOutputTypeDef,
        "ExportStatus": ExportStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateExportRequestRequestTypeDef = TypedDict(
    "CreateExportRequestRequestTypeDef",
    {
        "Export": ExportTypeDef,
        "ResourceTags": NotRequired[Sequence[ResourceTagTypeDef]],
    },
)
UpdateExportRequestRequestTypeDef = TypedDict(
    "UpdateExportRequestRequestTypeDef",
    {
        "Export": ExportTypeDef,
        "ExportArn": str,
    },
)
