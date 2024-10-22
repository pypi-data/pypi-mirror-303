"""
Type annotations for redshift-data service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/type_defs/)

Usage::

    ```python
    from mypy_boto3_redshift_data.type_defs import BatchExecuteStatementInputRequestTypeDef

    data: BatchExecuteStatementInputRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import StatementStatusStringType, StatusStringType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "BatchExecuteStatementInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CancelStatementRequestRequestTypeDef",
    "ColumnMetadataTypeDef",
    "DescribeStatementRequestRequestTypeDef",
    "SqlParameterTypeDef",
    "SubStatementDataTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeTableRequestRequestTypeDef",
    "FieldTypeDef",
    "GetStatementResultRequestRequestTypeDef",
    "ListDatabasesRequestRequestTypeDef",
    "ListSchemasRequestRequestTypeDef",
    "ListStatementsRequestRequestTypeDef",
    "ListTablesRequestRequestTypeDef",
    "TableMemberTypeDef",
    "BatchExecuteStatementOutputTypeDef",
    "CancelStatementResponseTypeDef",
    "ExecuteStatementOutputTypeDef",
    "ListDatabasesResponseTypeDef",
    "ListSchemasResponseTypeDef",
    "DescribeTableResponseTypeDef",
    "ExecuteStatementInputRequestTypeDef",
    "StatementDataTypeDef",
    "DescribeStatementResponseTypeDef",
    "DescribeTableRequestDescribeTablePaginateTypeDef",
    "GetStatementResultRequestGetStatementResultPaginateTypeDef",
    "ListDatabasesRequestListDatabasesPaginateTypeDef",
    "ListSchemasRequestListSchemasPaginateTypeDef",
    "ListStatementsRequestListStatementsPaginateTypeDef",
    "ListTablesRequestListTablesPaginateTypeDef",
    "GetStatementResultResponseTypeDef",
    "ListTablesResponseTypeDef",
    "ListStatementsResponseTypeDef",
)

BatchExecuteStatementInputRequestTypeDef = TypedDict(
    "BatchExecuteStatementInputRequestTypeDef",
    {
        "Sqls": Sequence[str],
        "ClientToken": NotRequired[str],
        "ClusterIdentifier": NotRequired[str],
        "Database": NotRequired[str],
        "DbUser": NotRequired[str],
        "SecretArn": NotRequired[str],
        "SessionId": NotRequired[str],
        "SessionKeepAliveSeconds": NotRequired[int],
        "StatementName": NotRequired[str],
        "WithEvent": NotRequired[bool],
        "WorkgroupName": NotRequired[str],
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
CancelStatementRequestRequestTypeDef = TypedDict(
    "CancelStatementRequestRequestTypeDef",
    {
        "Id": str,
    },
)
ColumnMetadataTypeDef = TypedDict(
    "ColumnMetadataTypeDef",
    {
        "columnDefault": NotRequired[str],
        "isCaseSensitive": NotRequired[bool],
        "isCurrency": NotRequired[bool],
        "isSigned": NotRequired[bool],
        "label": NotRequired[str],
        "length": NotRequired[int],
        "name": NotRequired[str],
        "nullable": NotRequired[int],
        "precision": NotRequired[int],
        "scale": NotRequired[int],
        "schemaName": NotRequired[str],
        "tableName": NotRequired[str],
        "typeName": NotRequired[str],
    },
)
DescribeStatementRequestRequestTypeDef = TypedDict(
    "DescribeStatementRequestRequestTypeDef",
    {
        "Id": str,
    },
)
SqlParameterTypeDef = TypedDict(
    "SqlParameterTypeDef",
    {
        "name": str,
        "value": str,
    },
)
SubStatementDataTypeDef = TypedDict(
    "SubStatementDataTypeDef",
    {
        "Id": str,
        "CreatedAt": NotRequired[datetime],
        "Duration": NotRequired[int],
        "Error": NotRequired[str],
        "HasResultSet": NotRequired[bool],
        "QueryString": NotRequired[str],
        "RedshiftQueryId": NotRequired[int],
        "ResultRows": NotRequired[int],
        "ResultSize": NotRequired[int],
        "Status": NotRequired[StatementStatusStringType],
        "UpdatedAt": NotRequired[datetime],
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
DescribeTableRequestRequestTypeDef = TypedDict(
    "DescribeTableRequestRequestTypeDef",
    {
        "Database": str,
        "ClusterIdentifier": NotRequired[str],
        "ConnectedDatabase": NotRequired[str],
        "DbUser": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Schema": NotRequired[str],
        "SecretArn": NotRequired[str],
        "Table": NotRequired[str],
        "WorkgroupName": NotRequired[str],
    },
)
FieldTypeDef = TypedDict(
    "FieldTypeDef",
    {
        "blobValue": NotRequired[bytes],
        "booleanValue": NotRequired[bool],
        "doubleValue": NotRequired[float],
        "isNull": NotRequired[bool],
        "longValue": NotRequired[int],
        "stringValue": NotRequired[str],
    },
)
GetStatementResultRequestRequestTypeDef = TypedDict(
    "GetStatementResultRequestRequestTypeDef",
    {
        "Id": str,
        "NextToken": NotRequired[str],
    },
)
ListDatabasesRequestRequestTypeDef = TypedDict(
    "ListDatabasesRequestRequestTypeDef",
    {
        "Database": str,
        "ClusterIdentifier": NotRequired[str],
        "DbUser": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "SecretArn": NotRequired[str],
        "WorkgroupName": NotRequired[str],
    },
)
ListSchemasRequestRequestTypeDef = TypedDict(
    "ListSchemasRequestRequestTypeDef",
    {
        "Database": str,
        "ClusterIdentifier": NotRequired[str],
        "ConnectedDatabase": NotRequired[str],
        "DbUser": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "SchemaPattern": NotRequired[str],
        "SecretArn": NotRequired[str],
        "WorkgroupName": NotRequired[str],
    },
)
ListStatementsRequestRequestTypeDef = TypedDict(
    "ListStatementsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "RoleLevel": NotRequired[bool],
        "StatementName": NotRequired[str],
        "Status": NotRequired[StatusStringType],
    },
)
ListTablesRequestRequestTypeDef = TypedDict(
    "ListTablesRequestRequestTypeDef",
    {
        "Database": str,
        "ClusterIdentifier": NotRequired[str],
        "ConnectedDatabase": NotRequired[str],
        "DbUser": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "SchemaPattern": NotRequired[str],
        "SecretArn": NotRequired[str],
        "TablePattern": NotRequired[str],
        "WorkgroupName": NotRequired[str],
    },
)
TableMemberTypeDef = TypedDict(
    "TableMemberTypeDef",
    {
        "name": NotRequired[str],
        "schema": NotRequired[str],
        "type": NotRequired[str],
    },
)
BatchExecuteStatementOutputTypeDef = TypedDict(
    "BatchExecuteStatementOutputTypeDef",
    {
        "ClusterIdentifier": str,
        "CreatedAt": datetime,
        "Database": str,
        "DbGroups": List[str],
        "DbUser": str,
        "Id": str,
        "SecretArn": str,
        "SessionId": str,
        "WorkgroupName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CancelStatementResponseTypeDef = TypedDict(
    "CancelStatementResponseTypeDef",
    {
        "Status": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExecuteStatementOutputTypeDef = TypedDict(
    "ExecuteStatementOutputTypeDef",
    {
        "ClusterIdentifier": str,
        "CreatedAt": datetime,
        "Database": str,
        "DbGroups": List[str],
        "DbUser": str,
        "Id": str,
        "SecretArn": str,
        "SessionId": str,
        "WorkgroupName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDatabasesResponseTypeDef = TypedDict(
    "ListDatabasesResponseTypeDef",
    {
        "Databases": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListSchemasResponseTypeDef = TypedDict(
    "ListSchemasResponseTypeDef",
    {
        "Schemas": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeTableResponseTypeDef = TypedDict(
    "DescribeTableResponseTypeDef",
    {
        "ColumnList": List[ColumnMetadataTypeDef],
        "TableName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ExecuteStatementInputRequestTypeDef = TypedDict(
    "ExecuteStatementInputRequestTypeDef",
    {
        "Sql": str,
        "ClientToken": NotRequired[str],
        "ClusterIdentifier": NotRequired[str],
        "Database": NotRequired[str],
        "DbUser": NotRequired[str],
        "Parameters": NotRequired[Sequence[SqlParameterTypeDef]],
        "SecretArn": NotRequired[str],
        "SessionId": NotRequired[str],
        "SessionKeepAliveSeconds": NotRequired[int],
        "StatementName": NotRequired[str],
        "WithEvent": NotRequired[bool],
        "WorkgroupName": NotRequired[str],
    },
)
StatementDataTypeDef = TypedDict(
    "StatementDataTypeDef",
    {
        "Id": str,
        "CreatedAt": NotRequired[datetime],
        "IsBatchStatement": NotRequired[bool],
        "QueryParameters": NotRequired[List[SqlParameterTypeDef]],
        "QueryString": NotRequired[str],
        "QueryStrings": NotRequired[List[str]],
        "SecretArn": NotRequired[str],
        "SessionId": NotRequired[str],
        "StatementName": NotRequired[str],
        "Status": NotRequired[StatusStringType],
        "UpdatedAt": NotRequired[datetime],
    },
)
DescribeStatementResponseTypeDef = TypedDict(
    "DescribeStatementResponseTypeDef",
    {
        "ClusterIdentifier": str,
        "CreatedAt": datetime,
        "Database": str,
        "DbUser": str,
        "Duration": int,
        "Error": str,
        "HasResultSet": bool,
        "Id": str,
        "QueryParameters": List[SqlParameterTypeDef],
        "QueryString": str,
        "RedshiftPid": int,
        "RedshiftQueryId": int,
        "ResultRows": int,
        "ResultSize": int,
        "SecretArn": str,
        "SessionId": str,
        "Status": StatusStringType,
        "SubStatements": List[SubStatementDataTypeDef],
        "UpdatedAt": datetime,
        "WorkgroupName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTableRequestDescribeTablePaginateTypeDef = TypedDict(
    "DescribeTableRequestDescribeTablePaginateTypeDef",
    {
        "Database": str,
        "ClusterIdentifier": NotRequired[str],
        "ConnectedDatabase": NotRequired[str],
        "DbUser": NotRequired[str],
        "Schema": NotRequired[str],
        "SecretArn": NotRequired[str],
        "Table": NotRequired[str],
        "WorkgroupName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetStatementResultRequestGetStatementResultPaginateTypeDef = TypedDict(
    "GetStatementResultRequestGetStatementResultPaginateTypeDef",
    {
        "Id": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDatabasesRequestListDatabasesPaginateTypeDef = TypedDict(
    "ListDatabasesRequestListDatabasesPaginateTypeDef",
    {
        "Database": str,
        "ClusterIdentifier": NotRequired[str],
        "DbUser": NotRequired[str],
        "SecretArn": NotRequired[str],
        "WorkgroupName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSchemasRequestListSchemasPaginateTypeDef = TypedDict(
    "ListSchemasRequestListSchemasPaginateTypeDef",
    {
        "Database": str,
        "ClusterIdentifier": NotRequired[str],
        "ConnectedDatabase": NotRequired[str],
        "DbUser": NotRequired[str],
        "SchemaPattern": NotRequired[str],
        "SecretArn": NotRequired[str],
        "WorkgroupName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListStatementsRequestListStatementsPaginateTypeDef = TypedDict(
    "ListStatementsRequestListStatementsPaginateTypeDef",
    {
        "RoleLevel": NotRequired[bool],
        "StatementName": NotRequired[str],
        "Status": NotRequired[StatusStringType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTablesRequestListTablesPaginateTypeDef = TypedDict(
    "ListTablesRequestListTablesPaginateTypeDef",
    {
        "Database": str,
        "ClusterIdentifier": NotRequired[str],
        "ConnectedDatabase": NotRequired[str],
        "DbUser": NotRequired[str],
        "SchemaPattern": NotRequired[str],
        "SecretArn": NotRequired[str],
        "TablePattern": NotRequired[str],
        "WorkgroupName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetStatementResultResponseTypeDef = TypedDict(
    "GetStatementResultResponseTypeDef",
    {
        "ColumnMetadata": List[ColumnMetadataTypeDef],
        "Records": List[List[FieldTypeDef]],
        "TotalNumRows": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTablesResponseTypeDef = TypedDict(
    "ListTablesResponseTypeDef",
    {
        "Tables": List[TableMemberTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListStatementsResponseTypeDef = TypedDict(
    "ListStatementsResponseTypeDef",
    {
        "Statements": List[StatementDataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
