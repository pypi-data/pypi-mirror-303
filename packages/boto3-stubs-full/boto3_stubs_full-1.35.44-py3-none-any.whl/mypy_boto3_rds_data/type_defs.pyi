"""
Type annotations for rds-data service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds_data/type_defs/)

Usage::

    ```python
    from mypy_boto3_rds_data.type_defs import ArrayValueOutputTypeDef

    data: ArrayValueOutputTypeDef = ...
    ```
"""

import sys
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import DecimalReturnTypeType, LongReturnTypeType, RecordsFormatTypeType, TypeHintType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "ArrayValueOutputTypeDef",
    "ArrayValueTypeDef",
    "ResponseMetadataTypeDef",
    "BeginTransactionRequestRequestTypeDef",
    "BlobTypeDef",
    "ColumnMetadataTypeDef",
    "CommitTransactionRequestRequestTypeDef",
    "ExecuteSqlRequestRequestTypeDef",
    "ResultSetOptionsTypeDef",
    "RollbackTransactionRequestRequestTypeDef",
    "StructValueTypeDef",
    "FieldOutputTypeDef",
    "ArrayValueUnionTypeDef",
    "BeginTransactionResponseTypeDef",
    "CommitTransactionResponseTypeDef",
    "RollbackTransactionResponseTypeDef",
    "ResultSetMetadataTypeDef",
    "ValueTypeDef",
    "ExecuteStatementResponseTypeDef",
    "UpdateResultTypeDef",
    "FieldTypeDef",
    "RecordTypeDef",
    "BatchExecuteStatementResponseTypeDef",
    "FieldUnionTypeDef",
    "ResultFrameTypeDef",
    "SqlParameterTypeDef",
    "SqlStatementResultTypeDef",
    "BatchExecuteStatementRequestRequestTypeDef",
    "ExecuteStatementRequestRequestTypeDef",
    "ExecuteSqlResponseTypeDef",
)

ArrayValueOutputTypeDef = TypedDict(
    "ArrayValueOutputTypeDef",
    {
        "booleanValues": NotRequired[List[bool]],
        "longValues": NotRequired[List[int]],
        "doubleValues": NotRequired[List[float]],
        "stringValues": NotRequired[List[str]],
        "arrayValues": NotRequired[List[Dict[str, Any]]],
    },
)
ArrayValueTypeDef = TypedDict(
    "ArrayValueTypeDef",
    {
        "booleanValues": NotRequired[Sequence[bool]],
        "longValues": NotRequired[Sequence[int]],
        "doubleValues": NotRequired[Sequence[float]],
        "stringValues": NotRequired[Sequence[str]],
        "arrayValues": NotRequired[Sequence[Mapping[str, Any]]],
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
BeginTransactionRequestRequestTypeDef = TypedDict(
    "BeginTransactionRequestRequestTypeDef",
    {
        "resourceArn": str,
        "secretArn": str,
        "database": NotRequired[str],
        "schema": NotRequired[str],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
ColumnMetadataTypeDef = TypedDict(
    "ColumnMetadataTypeDef",
    {
        "name": NotRequired[str],
        "type": NotRequired[int],
        "typeName": NotRequired[str],
        "label": NotRequired[str],
        "schemaName": NotRequired[str],
        "tableName": NotRequired[str],
        "isAutoIncrement": NotRequired[bool],
        "isSigned": NotRequired[bool],
        "isCurrency": NotRequired[bool],
        "isCaseSensitive": NotRequired[bool],
        "nullable": NotRequired[int],
        "precision": NotRequired[int],
        "scale": NotRequired[int],
        "arrayBaseColumnType": NotRequired[int],
    },
)
CommitTransactionRequestRequestTypeDef = TypedDict(
    "CommitTransactionRequestRequestTypeDef",
    {
        "resourceArn": str,
        "secretArn": str,
        "transactionId": str,
    },
)
ExecuteSqlRequestRequestTypeDef = TypedDict(
    "ExecuteSqlRequestRequestTypeDef",
    {
        "dbClusterOrInstanceArn": str,
        "awsSecretStoreArn": str,
        "sqlStatements": str,
        "database": NotRequired[str],
        "schema": NotRequired[str],
    },
)
ResultSetOptionsTypeDef = TypedDict(
    "ResultSetOptionsTypeDef",
    {
        "decimalReturnType": NotRequired[DecimalReturnTypeType],
        "longReturnType": NotRequired[LongReturnTypeType],
    },
)
RollbackTransactionRequestRequestTypeDef = TypedDict(
    "RollbackTransactionRequestRequestTypeDef",
    {
        "resourceArn": str,
        "secretArn": str,
        "transactionId": str,
    },
)
StructValueTypeDef = TypedDict(
    "StructValueTypeDef",
    {
        "attributes": NotRequired[List[Dict[str, Any]]],
    },
)
FieldOutputTypeDef = TypedDict(
    "FieldOutputTypeDef",
    {
        "isNull": NotRequired[bool],
        "booleanValue": NotRequired[bool],
        "longValue": NotRequired[int],
        "doubleValue": NotRequired[float],
        "stringValue": NotRequired[str],
        "blobValue": NotRequired[bytes],
        "arrayValue": NotRequired[ArrayValueOutputTypeDef],
    },
)
ArrayValueUnionTypeDef = Union[ArrayValueTypeDef, ArrayValueOutputTypeDef]
BeginTransactionResponseTypeDef = TypedDict(
    "BeginTransactionResponseTypeDef",
    {
        "transactionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CommitTransactionResponseTypeDef = TypedDict(
    "CommitTransactionResponseTypeDef",
    {
        "transactionStatus": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RollbackTransactionResponseTypeDef = TypedDict(
    "RollbackTransactionResponseTypeDef",
    {
        "transactionStatus": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResultSetMetadataTypeDef = TypedDict(
    "ResultSetMetadataTypeDef",
    {
        "columnCount": NotRequired[int],
        "columnMetadata": NotRequired[List[ColumnMetadataTypeDef]],
    },
)
ValueTypeDef = TypedDict(
    "ValueTypeDef",
    {
        "isNull": NotRequired[bool],
        "bitValue": NotRequired[bool],
        "bigIntValue": NotRequired[int],
        "intValue": NotRequired[int],
        "doubleValue": NotRequired[float],
        "realValue": NotRequired[float],
        "stringValue": NotRequired[str],
        "blobValue": NotRequired[bytes],
        "arrayValues": NotRequired[List[Dict[str, Any]]],
        "structValue": NotRequired[StructValueTypeDef],
    },
)
ExecuteStatementResponseTypeDef = TypedDict(
    "ExecuteStatementResponseTypeDef",
    {
        "records": List[List[FieldOutputTypeDef]],
        "columnMetadata": List[ColumnMetadataTypeDef],
        "numberOfRecordsUpdated": int,
        "generatedFields": List[FieldOutputTypeDef],
        "formattedRecords": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateResultTypeDef = TypedDict(
    "UpdateResultTypeDef",
    {
        "generatedFields": NotRequired[List[FieldOutputTypeDef]],
    },
)
FieldTypeDef = TypedDict(
    "FieldTypeDef",
    {
        "isNull": NotRequired[bool],
        "booleanValue": NotRequired[bool],
        "longValue": NotRequired[int],
        "doubleValue": NotRequired[float],
        "stringValue": NotRequired[str],
        "blobValue": NotRequired[BlobTypeDef],
        "arrayValue": NotRequired[ArrayValueUnionTypeDef],
    },
)
RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "values": NotRequired[List[ValueTypeDef]],
    },
)
BatchExecuteStatementResponseTypeDef = TypedDict(
    "BatchExecuteStatementResponseTypeDef",
    {
        "updateResults": List[UpdateResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FieldUnionTypeDef = Union[FieldTypeDef, FieldOutputTypeDef]
ResultFrameTypeDef = TypedDict(
    "ResultFrameTypeDef",
    {
        "resultSetMetadata": NotRequired[ResultSetMetadataTypeDef],
        "records": NotRequired[List[RecordTypeDef]],
    },
)
SqlParameterTypeDef = TypedDict(
    "SqlParameterTypeDef",
    {
        "name": NotRequired[str],
        "value": NotRequired[FieldUnionTypeDef],
        "typeHint": NotRequired[TypeHintType],
    },
)
SqlStatementResultTypeDef = TypedDict(
    "SqlStatementResultTypeDef",
    {
        "resultFrame": NotRequired[ResultFrameTypeDef],
        "numberOfRecordsUpdated": NotRequired[int],
    },
)
BatchExecuteStatementRequestRequestTypeDef = TypedDict(
    "BatchExecuteStatementRequestRequestTypeDef",
    {
        "resourceArn": str,
        "secretArn": str,
        "sql": str,
        "database": NotRequired[str],
        "schema": NotRequired[str],
        "parameterSets": NotRequired[Sequence[Sequence[SqlParameterTypeDef]]],
        "transactionId": NotRequired[str],
    },
)
ExecuteStatementRequestRequestTypeDef = TypedDict(
    "ExecuteStatementRequestRequestTypeDef",
    {
        "resourceArn": str,
        "secretArn": str,
        "sql": str,
        "database": NotRequired[str],
        "schema": NotRequired[str],
        "parameters": NotRequired[Sequence[SqlParameterTypeDef]],
        "transactionId": NotRequired[str],
        "includeResultMetadata": NotRequired[bool],
        "continueAfterTimeout": NotRequired[bool],
        "resultSetOptions": NotRequired[ResultSetOptionsTypeDef],
        "formatRecordsAs": NotRequired[RecordsFormatTypeType],
    },
)
ExecuteSqlResponseTypeDef = TypedDict(
    "ExecuteSqlResponseTypeDef",
    {
        "sqlStatementResults": List[SqlStatementResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
