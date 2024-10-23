"""
Type annotations for athena service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_athena/type_defs/)

Usage::

    ```python
    from mypy_boto3_athena.type_defs import AclConfigurationTypeDef

    data: AclConfigurationTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    CalculationExecutionStateType,
    CapacityAllocationStatusType,
    CapacityReservationStatusType,
    ColumnNullableType,
    DataCatalogTypeType,
    EncryptionOptionType,
    ExecutorStateType,
    ExecutorTypeType,
    QueryExecutionStateType,
    SessionStateType,
    StatementTypeType,
    WorkGroupStateType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AclConfigurationTypeDef",
    "ApplicationDPUSizesTypeDef",
    "AthenaErrorTypeDef",
    "BatchGetNamedQueryInputRequestTypeDef",
    "NamedQueryTypeDef",
    "ResponseMetadataTypeDef",
    "UnprocessedNamedQueryIdTypeDef",
    "BatchGetPreparedStatementInputRequestTypeDef",
    "PreparedStatementTypeDef",
    "UnprocessedPreparedStatementNameTypeDef",
    "BatchGetQueryExecutionInputRequestTypeDef",
    "UnprocessedQueryExecutionIdTypeDef",
    "CalculationConfigurationTypeDef",
    "CalculationResultTypeDef",
    "CalculationStatisticsTypeDef",
    "CalculationStatusTypeDef",
    "CancelCapacityReservationInputRequestTypeDef",
    "CapacityAllocationTypeDef",
    "CapacityAssignmentOutputTypeDef",
    "CapacityAssignmentTypeDef",
    "ColumnInfoTypeDef",
    "ColumnTypeDef",
    "TagTypeDef",
    "CreateNamedQueryInputRequestTypeDef",
    "CreateNotebookInputRequestTypeDef",
    "CreatePreparedStatementInputRequestTypeDef",
    "CreatePresignedNotebookUrlRequestRequestTypeDef",
    "CustomerContentEncryptionConfigurationTypeDef",
    "DataCatalogSummaryTypeDef",
    "DataCatalogTypeDef",
    "DatabaseTypeDef",
    "DatumTypeDef",
    "DeleteCapacityReservationInputRequestTypeDef",
    "DeleteDataCatalogInputRequestTypeDef",
    "DeleteNamedQueryInputRequestTypeDef",
    "DeleteNotebookInputRequestTypeDef",
    "DeletePreparedStatementInputRequestTypeDef",
    "DeleteWorkGroupInputRequestTypeDef",
    "EncryptionConfigurationTypeDef",
    "EngineConfigurationOutputTypeDef",
    "EngineConfigurationTypeDef",
    "EngineVersionTypeDef",
    "ExecutorsSummaryTypeDef",
    "ExportNotebookInputRequestTypeDef",
    "NotebookMetadataTypeDef",
    "FilterDefinitionTypeDef",
    "GetCalculationExecutionCodeRequestRequestTypeDef",
    "GetCalculationExecutionRequestRequestTypeDef",
    "GetCalculationExecutionStatusRequestRequestTypeDef",
    "GetCapacityAssignmentConfigurationInputRequestTypeDef",
    "GetCapacityReservationInputRequestTypeDef",
    "GetDataCatalogInputRequestTypeDef",
    "GetDatabaseInputRequestTypeDef",
    "GetNamedQueryInputRequestTypeDef",
    "GetNotebookMetadataInputRequestTypeDef",
    "GetPreparedStatementInputRequestTypeDef",
    "GetQueryExecutionInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "GetQueryResultsInputRequestTypeDef",
    "GetQueryRuntimeStatisticsInputRequestTypeDef",
    "GetSessionRequestRequestTypeDef",
    "SessionStatisticsTypeDef",
    "SessionStatusTypeDef",
    "GetSessionStatusRequestRequestTypeDef",
    "GetTableMetadataInputRequestTypeDef",
    "GetWorkGroupInputRequestTypeDef",
    "IdentityCenterConfigurationTypeDef",
    "ImportNotebookInputRequestTypeDef",
    "ListApplicationDPUSizesInputRequestTypeDef",
    "ListCalculationExecutionsRequestRequestTypeDef",
    "ListCapacityReservationsInputRequestTypeDef",
    "ListDataCatalogsInputRequestTypeDef",
    "ListDatabasesInputRequestTypeDef",
    "ListEngineVersionsInputRequestTypeDef",
    "ListExecutorsRequestRequestTypeDef",
    "ListNamedQueriesInputRequestTypeDef",
    "ListNotebookSessionsRequestRequestTypeDef",
    "NotebookSessionSummaryTypeDef",
    "ListPreparedStatementsInputRequestTypeDef",
    "PreparedStatementSummaryTypeDef",
    "ListQueryExecutionsInputRequestTypeDef",
    "ListSessionsRequestRequestTypeDef",
    "ListTableMetadataInputRequestTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListWorkGroupsInputRequestTypeDef",
    "QueryExecutionContextTypeDef",
    "ResultReuseInformationTypeDef",
    "QueryResultsS3AccessGrantsConfigurationTypeDef",
    "QueryRuntimeStatisticsRowsTypeDef",
    "QueryRuntimeStatisticsTimelineTypeDef",
    "QueryStagePlanNodeTypeDef",
    "ResultReuseByAgeConfigurationTypeDef",
    "StopCalculationExecutionRequestRequestTypeDef",
    "StopQueryExecutionInputRequestTypeDef",
    "TerminateSessionRequestRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateCapacityReservationInputRequestTypeDef",
    "UpdateDataCatalogInputRequestTypeDef",
    "UpdateNamedQueryInputRequestTypeDef",
    "UpdateNotebookInputRequestTypeDef",
    "UpdateNotebookMetadataInputRequestTypeDef",
    "UpdatePreparedStatementInputRequestTypeDef",
    "QueryExecutionStatusTypeDef",
    "CreateNamedQueryOutputTypeDef",
    "CreateNotebookOutputTypeDef",
    "CreatePresignedNotebookUrlResponseTypeDef",
    "GetCalculationExecutionCodeResponseTypeDef",
    "GetNamedQueryOutputTypeDef",
    "ImportNotebookOutputTypeDef",
    "ListApplicationDPUSizesOutputTypeDef",
    "ListNamedQueriesOutputTypeDef",
    "ListQueryExecutionsOutputTypeDef",
    "StartCalculationExecutionResponseTypeDef",
    "StartQueryExecutionOutputTypeDef",
    "StartSessionResponseTypeDef",
    "StopCalculationExecutionResponseTypeDef",
    "TerminateSessionResponseTypeDef",
    "BatchGetNamedQueryOutputTypeDef",
    "GetPreparedStatementOutputTypeDef",
    "BatchGetPreparedStatementOutputTypeDef",
    "StartCalculationExecutionRequestRequestTypeDef",
    "CalculationSummaryTypeDef",
    "GetCalculationExecutionResponseTypeDef",
    "GetCalculationExecutionStatusResponseTypeDef",
    "CapacityReservationTypeDef",
    "CapacityAssignmentConfigurationTypeDef",
    "CapacityAssignmentUnionTypeDef",
    "ResultSetMetadataTypeDef",
    "TableMetadataTypeDef",
    "CreateCapacityReservationInputRequestTypeDef",
    "CreateDataCatalogInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "TagResourceInputRequestTypeDef",
    "ListDataCatalogsOutputTypeDef",
    "GetDataCatalogOutputTypeDef",
    "GetDatabaseOutputTypeDef",
    "ListDatabasesOutputTypeDef",
    "RowTypeDef",
    "ResultConfigurationTypeDef",
    "ResultConfigurationUpdatesTypeDef",
    "SessionConfigurationTypeDef",
    "StartSessionRequestRequestTypeDef",
    "ListEngineVersionsOutputTypeDef",
    "WorkGroupSummaryTypeDef",
    "ListExecutorsResponseTypeDef",
    "ExportNotebookOutputTypeDef",
    "GetNotebookMetadataOutputTypeDef",
    "ListNotebookMetadataOutputTypeDef",
    "ListNotebookMetadataInputRequestTypeDef",
    "GetQueryResultsInputGetQueryResultsPaginateTypeDef",
    "ListDataCatalogsInputListDataCatalogsPaginateTypeDef",
    "ListDatabasesInputListDatabasesPaginateTypeDef",
    "ListNamedQueriesInputListNamedQueriesPaginateTypeDef",
    "ListQueryExecutionsInputListQueryExecutionsPaginateTypeDef",
    "ListTableMetadataInputListTableMetadataPaginateTypeDef",
    "ListTagsForResourceInputListTagsForResourcePaginateTypeDef",
    "GetSessionStatusResponseTypeDef",
    "SessionSummaryTypeDef",
    "ListNotebookSessionsResponseTypeDef",
    "ListPreparedStatementsOutputTypeDef",
    "QueryExecutionStatisticsTypeDef",
    "QueryStageTypeDef",
    "ResultReuseConfigurationTypeDef",
    "ListCalculationExecutionsResponseTypeDef",
    "GetCapacityReservationOutputTypeDef",
    "ListCapacityReservationsOutputTypeDef",
    "GetCapacityAssignmentConfigurationOutputTypeDef",
    "PutCapacityAssignmentConfigurationInputRequestTypeDef",
    "GetTableMetadataOutputTypeDef",
    "ListTableMetadataOutputTypeDef",
    "ResultSetTypeDef",
    "WorkGroupConfigurationTypeDef",
    "WorkGroupConfigurationUpdatesTypeDef",
    "GetSessionResponseTypeDef",
    "ListWorkGroupsOutputTypeDef",
    "ListSessionsResponseTypeDef",
    "QueryRuntimeStatisticsTypeDef",
    "QueryExecutionTypeDef",
    "StartQueryExecutionInputRequestTypeDef",
    "GetQueryResultsOutputTypeDef",
    "CreateWorkGroupInputRequestTypeDef",
    "WorkGroupTypeDef",
    "UpdateWorkGroupInputRequestTypeDef",
    "GetQueryRuntimeStatisticsOutputTypeDef",
    "BatchGetQueryExecutionOutputTypeDef",
    "GetQueryExecutionOutputTypeDef",
    "GetWorkGroupOutputTypeDef",
)

AclConfigurationTypeDef = TypedDict(
    "AclConfigurationTypeDef",
    {
        "S3AclOption": Literal["BUCKET_OWNER_FULL_CONTROL"],
    },
)
ApplicationDPUSizesTypeDef = TypedDict(
    "ApplicationDPUSizesTypeDef",
    {
        "ApplicationRuntimeId": NotRequired[str],
        "SupportedDPUSizes": NotRequired[List[int]],
    },
)
AthenaErrorTypeDef = TypedDict(
    "AthenaErrorTypeDef",
    {
        "ErrorCategory": NotRequired[int],
        "ErrorType": NotRequired[int],
        "Retryable": NotRequired[bool],
        "ErrorMessage": NotRequired[str],
    },
)
BatchGetNamedQueryInputRequestTypeDef = TypedDict(
    "BatchGetNamedQueryInputRequestTypeDef",
    {
        "NamedQueryIds": Sequence[str],
    },
)
NamedQueryTypeDef = TypedDict(
    "NamedQueryTypeDef",
    {
        "Name": str,
        "Database": str,
        "QueryString": str,
        "Description": NotRequired[str],
        "NamedQueryId": NotRequired[str],
        "WorkGroup": NotRequired[str],
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
UnprocessedNamedQueryIdTypeDef = TypedDict(
    "UnprocessedNamedQueryIdTypeDef",
    {
        "NamedQueryId": NotRequired[str],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)
BatchGetPreparedStatementInputRequestTypeDef = TypedDict(
    "BatchGetPreparedStatementInputRequestTypeDef",
    {
        "PreparedStatementNames": Sequence[str],
        "WorkGroup": str,
    },
)
PreparedStatementTypeDef = TypedDict(
    "PreparedStatementTypeDef",
    {
        "StatementName": NotRequired[str],
        "QueryStatement": NotRequired[str],
        "WorkGroupName": NotRequired[str],
        "Description": NotRequired[str],
        "LastModifiedTime": NotRequired[datetime],
    },
)
UnprocessedPreparedStatementNameTypeDef = TypedDict(
    "UnprocessedPreparedStatementNameTypeDef",
    {
        "StatementName": NotRequired[str],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)
BatchGetQueryExecutionInputRequestTypeDef = TypedDict(
    "BatchGetQueryExecutionInputRequestTypeDef",
    {
        "QueryExecutionIds": Sequence[str],
    },
)
UnprocessedQueryExecutionIdTypeDef = TypedDict(
    "UnprocessedQueryExecutionIdTypeDef",
    {
        "QueryExecutionId": NotRequired[str],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)
CalculationConfigurationTypeDef = TypedDict(
    "CalculationConfigurationTypeDef",
    {
        "CodeBlock": NotRequired[str],
    },
)
CalculationResultTypeDef = TypedDict(
    "CalculationResultTypeDef",
    {
        "StdOutS3Uri": NotRequired[str],
        "StdErrorS3Uri": NotRequired[str],
        "ResultS3Uri": NotRequired[str],
        "ResultType": NotRequired[str],
    },
)
CalculationStatisticsTypeDef = TypedDict(
    "CalculationStatisticsTypeDef",
    {
        "DpuExecutionInMillis": NotRequired[int],
        "Progress": NotRequired[str],
    },
)
CalculationStatusTypeDef = TypedDict(
    "CalculationStatusTypeDef",
    {
        "SubmissionDateTime": NotRequired[datetime],
        "CompletionDateTime": NotRequired[datetime],
        "State": NotRequired[CalculationExecutionStateType],
        "StateChangeReason": NotRequired[str],
    },
)
CancelCapacityReservationInputRequestTypeDef = TypedDict(
    "CancelCapacityReservationInputRequestTypeDef",
    {
        "Name": str,
    },
)
CapacityAllocationTypeDef = TypedDict(
    "CapacityAllocationTypeDef",
    {
        "Status": CapacityAllocationStatusType,
        "RequestTime": datetime,
        "StatusMessage": NotRequired[str],
        "RequestCompletionTime": NotRequired[datetime],
    },
)
CapacityAssignmentOutputTypeDef = TypedDict(
    "CapacityAssignmentOutputTypeDef",
    {
        "WorkGroupNames": NotRequired[List[str]],
    },
)
CapacityAssignmentTypeDef = TypedDict(
    "CapacityAssignmentTypeDef",
    {
        "WorkGroupNames": NotRequired[Sequence[str]],
    },
)
ColumnInfoTypeDef = TypedDict(
    "ColumnInfoTypeDef",
    {
        "Name": str,
        "Type": str,
        "CatalogName": NotRequired[str],
        "SchemaName": NotRequired[str],
        "TableName": NotRequired[str],
        "Label": NotRequired[str],
        "Precision": NotRequired[int],
        "Scale": NotRequired[int],
        "Nullable": NotRequired[ColumnNullableType],
        "CaseSensitive": NotRequired[bool],
    },
)
ColumnTypeDef = TypedDict(
    "ColumnTypeDef",
    {
        "Name": str,
        "Type": NotRequired[str],
        "Comment": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
CreateNamedQueryInputRequestTypeDef = TypedDict(
    "CreateNamedQueryInputRequestTypeDef",
    {
        "Name": str,
        "Database": str,
        "QueryString": str,
        "Description": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "WorkGroup": NotRequired[str],
    },
)
CreateNotebookInputRequestTypeDef = TypedDict(
    "CreateNotebookInputRequestTypeDef",
    {
        "WorkGroup": str,
        "Name": str,
        "ClientRequestToken": NotRequired[str],
    },
)
CreatePreparedStatementInputRequestTypeDef = TypedDict(
    "CreatePreparedStatementInputRequestTypeDef",
    {
        "StatementName": str,
        "WorkGroup": str,
        "QueryStatement": str,
        "Description": NotRequired[str],
    },
)
CreatePresignedNotebookUrlRequestRequestTypeDef = TypedDict(
    "CreatePresignedNotebookUrlRequestRequestTypeDef",
    {
        "SessionId": str,
    },
)
CustomerContentEncryptionConfigurationTypeDef = TypedDict(
    "CustomerContentEncryptionConfigurationTypeDef",
    {
        "KmsKey": str,
    },
)
DataCatalogSummaryTypeDef = TypedDict(
    "DataCatalogSummaryTypeDef",
    {
        "CatalogName": NotRequired[str],
        "Type": NotRequired[DataCatalogTypeType],
    },
)
DataCatalogTypeDef = TypedDict(
    "DataCatalogTypeDef",
    {
        "Name": str,
        "Type": DataCatalogTypeType,
        "Description": NotRequired[str],
        "Parameters": NotRequired[Dict[str, str]],
    },
)
DatabaseTypeDef = TypedDict(
    "DatabaseTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "Parameters": NotRequired[Dict[str, str]],
    },
)
DatumTypeDef = TypedDict(
    "DatumTypeDef",
    {
        "VarCharValue": NotRequired[str],
    },
)
DeleteCapacityReservationInputRequestTypeDef = TypedDict(
    "DeleteCapacityReservationInputRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteDataCatalogInputRequestTypeDef = TypedDict(
    "DeleteDataCatalogInputRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteNamedQueryInputRequestTypeDef = TypedDict(
    "DeleteNamedQueryInputRequestTypeDef",
    {
        "NamedQueryId": str,
    },
)
DeleteNotebookInputRequestTypeDef = TypedDict(
    "DeleteNotebookInputRequestTypeDef",
    {
        "NotebookId": str,
    },
)
DeletePreparedStatementInputRequestTypeDef = TypedDict(
    "DeletePreparedStatementInputRequestTypeDef",
    {
        "StatementName": str,
        "WorkGroup": str,
    },
)
DeleteWorkGroupInputRequestTypeDef = TypedDict(
    "DeleteWorkGroupInputRequestTypeDef",
    {
        "WorkGroup": str,
        "RecursiveDeleteOption": NotRequired[bool],
    },
)
EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "EncryptionOption": EncryptionOptionType,
        "KmsKey": NotRequired[str],
    },
)
EngineConfigurationOutputTypeDef = TypedDict(
    "EngineConfigurationOutputTypeDef",
    {
        "MaxConcurrentDpus": int,
        "CoordinatorDpuSize": NotRequired[int],
        "DefaultExecutorDpuSize": NotRequired[int],
        "AdditionalConfigs": NotRequired[Dict[str, str]],
        "SparkProperties": NotRequired[Dict[str, str]],
    },
)
EngineConfigurationTypeDef = TypedDict(
    "EngineConfigurationTypeDef",
    {
        "MaxConcurrentDpus": int,
        "CoordinatorDpuSize": NotRequired[int],
        "DefaultExecutorDpuSize": NotRequired[int],
        "AdditionalConfigs": NotRequired[Mapping[str, str]],
        "SparkProperties": NotRequired[Mapping[str, str]],
    },
)
EngineVersionTypeDef = TypedDict(
    "EngineVersionTypeDef",
    {
        "SelectedEngineVersion": NotRequired[str],
        "EffectiveEngineVersion": NotRequired[str],
    },
)
ExecutorsSummaryTypeDef = TypedDict(
    "ExecutorsSummaryTypeDef",
    {
        "ExecutorId": str,
        "ExecutorType": NotRequired[ExecutorTypeType],
        "StartDateTime": NotRequired[int],
        "TerminationDateTime": NotRequired[int],
        "ExecutorState": NotRequired[ExecutorStateType],
        "ExecutorSize": NotRequired[int],
    },
)
ExportNotebookInputRequestTypeDef = TypedDict(
    "ExportNotebookInputRequestTypeDef",
    {
        "NotebookId": str,
    },
)
NotebookMetadataTypeDef = TypedDict(
    "NotebookMetadataTypeDef",
    {
        "NotebookId": NotRequired[str],
        "Name": NotRequired[str],
        "WorkGroup": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "Type": NotRequired[Literal["IPYNB"]],
        "LastModifiedTime": NotRequired[datetime],
    },
)
FilterDefinitionTypeDef = TypedDict(
    "FilterDefinitionTypeDef",
    {
        "Name": NotRequired[str],
    },
)
GetCalculationExecutionCodeRequestRequestTypeDef = TypedDict(
    "GetCalculationExecutionCodeRequestRequestTypeDef",
    {
        "CalculationExecutionId": str,
    },
)
GetCalculationExecutionRequestRequestTypeDef = TypedDict(
    "GetCalculationExecutionRequestRequestTypeDef",
    {
        "CalculationExecutionId": str,
    },
)
GetCalculationExecutionStatusRequestRequestTypeDef = TypedDict(
    "GetCalculationExecutionStatusRequestRequestTypeDef",
    {
        "CalculationExecutionId": str,
    },
)
GetCapacityAssignmentConfigurationInputRequestTypeDef = TypedDict(
    "GetCapacityAssignmentConfigurationInputRequestTypeDef",
    {
        "CapacityReservationName": str,
    },
)
GetCapacityReservationInputRequestTypeDef = TypedDict(
    "GetCapacityReservationInputRequestTypeDef",
    {
        "Name": str,
    },
)
GetDataCatalogInputRequestTypeDef = TypedDict(
    "GetDataCatalogInputRequestTypeDef",
    {
        "Name": str,
        "WorkGroup": NotRequired[str],
    },
)
GetDatabaseInputRequestTypeDef = TypedDict(
    "GetDatabaseInputRequestTypeDef",
    {
        "CatalogName": str,
        "DatabaseName": str,
        "WorkGroup": NotRequired[str],
    },
)
GetNamedQueryInputRequestTypeDef = TypedDict(
    "GetNamedQueryInputRequestTypeDef",
    {
        "NamedQueryId": str,
    },
)
GetNotebookMetadataInputRequestTypeDef = TypedDict(
    "GetNotebookMetadataInputRequestTypeDef",
    {
        "NotebookId": str,
    },
)
GetPreparedStatementInputRequestTypeDef = TypedDict(
    "GetPreparedStatementInputRequestTypeDef",
    {
        "StatementName": str,
        "WorkGroup": str,
    },
)
GetQueryExecutionInputRequestTypeDef = TypedDict(
    "GetQueryExecutionInputRequestTypeDef",
    {
        "QueryExecutionId": str,
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
GetQueryResultsInputRequestTypeDef = TypedDict(
    "GetQueryResultsInputRequestTypeDef",
    {
        "QueryExecutionId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GetQueryRuntimeStatisticsInputRequestTypeDef = TypedDict(
    "GetQueryRuntimeStatisticsInputRequestTypeDef",
    {
        "QueryExecutionId": str,
    },
)
GetSessionRequestRequestTypeDef = TypedDict(
    "GetSessionRequestRequestTypeDef",
    {
        "SessionId": str,
    },
)
SessionStatisticsTypeDef = TypedDict(
    "SessionStatisticsTypeDef",
    {
        "DpuExecutionInMillis": NotRequired[int],
    },
)
SessionStatusTypeDef = TypedDict(
    "SessionStatusTypeDef",
    {
        "StartDateTime": NotRequired[datetime],
        "LastModifiedDateTime": NotRequired[datetime],
        "EndDateTime": NotRequired[datetime],
        "IdleSinceDateTime": NotRequired[datetime],
        "State": NotRequired[SessionStateType],
        "StateChangeReason": NotRequired[str],
    },
)
GetSessionStatusRequestRequestTypeDef = TypedDict(
    "GetSessionStatusRequestRequestTypeDef",
    {
        "SessionId": str,
    },
)
GetTableMetadataInputRequestTypeDef = TypedDict(
    "GetTableMetadataInputRequestTypeDef",
    {
        "CatalogName": str,
        "DatabaseName": str,
        "TableName": str,
        "WorkGroup": NotRequired[str],
    },
)
GetWorkGroupInputRequestTypeDef = TypedDict(
    "GetWorkGroupInputRequestTypeDef",
    {
        "WorkGroup": str,
    },
)
IdentityCenterConfigurationTypeDef = TypedDict(
    "IdentityCenterConfigurationTypeDef",
    {
        "EnableIdentityCenter": NotRequired[bool],
        "IdentityCenterInstanceArn": NotRequired[str],
    },
)
ImportNotebookInputRequestTypeDef = TypedDict(
    "ImportNotebookInputRequestTypeDef",
    {
        "WorkGroup": str,
        "Name": str,
        "Type": Literal["IPYNB"],
        "Payload": NotRequired[str],
        "NotebookS3LocationUri": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
    },
)
ListApplicationDPUSizesInputRequestTypeDef = TypedDict(
    "ListApplicationDPUSizesInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListCalculationExecutionsRequestRequestTypeDef = TypedDict(
    "ListCalculationExecutionsRequestRequestTypeDef",
    {
        "SessionId": str,
        "StateFilter": NotRequired[CalculationExecutionStateType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListCapacityReservationsInputRequestTypeDef = TypedDict(
    "ListCapacityReservationsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListDataCatalogsInputRequestTypeDef = TypedDict(
    "ListDataCatalogsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "WorkGroup": NotRequired[str],
    },
)
ListDatabasesInputRequestTypeDef = TypedDict(
    "ListDatabasesInputRequestTypeDef",
    {
        "CatalogName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "WorkGroup": NotRequired[str],
    },
)
ListEngineVersionsInputRequestTypeDef = TypedDict(
    "ListEngineVersionsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListExecutorsRequestRequestTypeDef = TypedDict(
    "ListExecutorsRequestRequestTypeDef",
    {
        "SessionId": str,
        "ExecutorStateFilter": NotRequired[ExecutorStateType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListNamedQueriesInputRequestTypeDef = TypedDict(
    "ListNamedQueriesInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "WorkGroup": NotRequired[str],
    },
)
ListNotebookSessionsRequestRequestTypeDef = TypedDict(
    "ListNotebookSessionsRequestRequestTypeDef",
    {
        "NotebookId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
NotebookSessionSummaryTypeDef = TypedDict(
    "NotebookSessionSummaryTypeDef",
    {
        "SessionId": NotRequired[str],
        "CreationTime": NotRequired[datetime],
    },
)
ListPreparedStatementsInputRequestTypeDef = TypedDict(
    "ListPreparedStatementsInputRequestTypeDef",
    {
        "WorkGroup": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
PreparedStatementSummaryTypeDef = TypedDict(
    "PreparedStatementSummaryTypeDef",
    {
        "StatementName": NotRequired[str],
        "LastModifiedTime": NotRequired[datetime],
    },
)
ListQueryExecutionsInputRequestTypeDef = TypedDict(
    "ListQueryExecutionsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "WorkGroup": NotRequired[str],
    },
)
ListSessionsRequestRequestTypeDef = TypedDict(
    "ListSessionsRequestRequestTypeDef",
    {
        "WorkGroup": str,
        "StateFilter": NotRequired[SessionStateType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTableMetadataInputRequestTypeDef = TypedDict(
    "ListTableMetadataInputRequestTypeDef",
    {
        "CatalogName": str,
        "DatabaseName": str,
        "Expression": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "WorkGroup": NotRequired[str],
    },
)
ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListWorkGroupsInputRequestTypeDef = TypedDict(
    "ListWorkGroupsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
QueryExecutionContextTypeDef = TypedDict(
    "QueryExecutionContextTypeDef",
    {
        "Database": NotRequired[str],
        "Catalog": NotRequired[str],
    },
)
ResultReuseInformationTypeDef = TypedDict(
    "ResultReuseInformationTypeDef",
    {
        "ReusedPreviousResult": bool,
    },
)
QueryResultsS3AccessGrantsConfigurationTypeDef = TypedDict(
    "QueryResultsS3AccessGrantsConfigurationTypeDef",
    {
        "EnableS3AccessGrants": bool,
        "AuthenticationType": Literal["DIRECTORY_IDENTITY"],
        "CreateUserLevelPrefix": NotRequired[bool],
    },
)
QueryRuntimeStatisticsRowsTypeDef = TypedDict(
    "QueryRuntimeStatisticsRowsTypeDef",
    {
        "InputRows": NotRequired[int],
        "InputBytes": NotRequired[int],
        "OutputBytes": NotRequired[int],
        "OutputRows": NotRequired[int],
    },
)
QueryRuntimeStatisticsTimelineTypeDef = TypedDict(
    "QueryRuntimeStatisticsTimelineTypeDef",
    {
        "QueryQueueTimeInMillis": NotRequired[int],
        "ServicePreProcessingTimeInMillis": NotRequired[int],
        "QueryPlanningTimeInMillis": NotRequired[int],
        "EngineExecutionTimeInMillis": NotRequired[int],
        "ServiceProcessingTimeInMillis": NotRequired[int],
        "TotalExecutionTimeInMillis": NotRequired[int],
    },
)
QueryStagePlanNodeTypeDef = TypedDict(
    "QueryStagePlanNodeTypeDef",
    {
        "Name": NotRequired[str],
        "Identifier": NotRequired[str],
        "Children": NotRequired[List[Dict[str, Any]]],
        "RemoteSources": NotRequired[List[str]],
    },
)
ResultReuseByAgeConfigurationTypeDef = TypedDict(
    "ResultReuseByAgeConfigurationTypeDef",
    {
        "Enabled": bool,
        "MaxAgeInMinutes": NotRequired[int],
    },
)
StopCalculationExecutionRequestRequestTypeDef = TypedDict(
    "StopCalculationExecutionRequestRequestTypeDef",
    {
        "CalculationExecutionId": str,
    },
)
StopQueryExecutionInputRequestTypeDef = TypedDict(
    "StopQueryExecutionInputRequestTypeDef",
    {
        "QueryExecutionId": str,
    },
)
TerminateSessionRequestRequestTypeDef = TypedDict(
    "TerminateSessionRequestRequestTypeDef",
    {
        "SessionId": str,
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
UpdateCapacityReservationInputRequestTypeDef = TypedDict(
    "UpdateCapacityReservationInputRequestTypeDef",
    {
        "TargetDpus": int,
        "Name": str,
    },
)
UpdateDataCatalogInputRequestTypeDef = TypedDict(
    "UpdateDataCatalogInputRequestTypeDef",
    {
        "Name": str,
        "Type": DataCatalogTypeType,
        "Description": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, str]],
    },
)
UpdateNamedQueryInputRequestTypeDef = TypedDict(
    "UpdateNamedQueryInputRequestTypeDef",
    {
        "NamedQueryId": str,
        "Name": str,
        "QueryString": str,
        "Description": NotRequired[str],
    },
)
UpdateNotebookInputRequestTypeDef = TypedDict(
    "UpdateNotebookInputRequestTypeDef",
    {
        "NotebookId": str,
        "Payload": str,
        "Type": Literal["IPYNB"],
        "SessionId": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
    },
)
UpdateNotebookMetadataInputRequestTypeDef = TypedDict(
    "UpdateNotebookMetadataInputRequestTypeDef",
    {
        "NotebookId": str,
        "Name": str,
        "ClientRequestToken": NotRequired[str],
    },
)
UpdatePreparedStatementInputRequestTypeDef = TypedDict(
    "UpdatePreparedStatementInputRequestTypeDef",
    {
        "StatementName": str,
        "WorkGroup": str,
        "QueryStatement": str,
        "Description": NotRequired[str],
    },
)
QueryExecutionStatusTypeDef = TypedDict(
    "QueryExecutionStatusTypeDef",
    {
        "State": NotRequired[QueryExecutionStateType],
        "StateChangeReason": NotRequired[str],
        "SubmissionDateTime": NotRequired[datetime],
        "CompletionDateTime": NotRequired[datetime],
        "AthenaError": NotRequired[AthenaErrorTypeDef],
    },
)
CreateNamedQueryOutputTypeDef = TypedDict(
    "CreateNamedQueryOutputTypeDef",
    {
        "NamedQueryId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateNotebookOutputTypeDef = TypedDict(
    "CreateNotebookOutputTypeDef",
    {
        "NotebookId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePresignedNotebookUrlResponseTypeDef = TypedDict(
    "CreatePresignedNotebookUrlResponseTypeDef",
    {
        "NotebookUrl": str,
        "AuthToken": str,
        "AuthTokenExpirationTime": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCalculationExecutionCodeResponseTypeDef = TypedDict(
    "GetCalculationExecutionCodeResponseTypeDef",
    {
        "CodeBlock": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetNamedQueryOutputTypeDef = TypedDict(
    "GetNamedQueryOutputTypeDef",
    {
        "NamedQuery": NamedQueryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportNotebookOutputTypeDef = TypedDict(
    "ImportNotebookOutputTypeDef",
    {
        "NotebookId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListApplicationDPUSizesOutputTypeDef = TypedDict(
    "ListApplicationDPUSizesOutputTypeDef",
    {
        "ApplicationDPUSizes": List[ApplicationDPUSizesTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListNamedQueriesOutputTypeDef = TypedDict(
    "ListNamedQueriesOutputTypeDef",
    {
        "NamedQueryIds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListQueryExecutionsOutputTypeDef = TypedDict(
    "ListQueryExecutionsOutputTypeDef",
    {
        "QueryExecutionIds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
StartCalculationExecutionResponseTypeDef = TypedDict(
    "StartCalculationExecutionResponseTypeDef",
    {
        "CalculationExecutionId": str,
        "State": CalculationExecutionStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartQueryExecutionOutputTypeDef = TypedDict(
    "StartQueryExecutionOutputTypeDef",
    {
        "QueryExecutionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartSessionResponseTypeDef = TypedDict(
    "StartSessionResponseTypeDef",
    {
        "SessionId": str,
        "State": SessionStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopCalculationExecutionResponseTypeDef = TypedDict(
    "StopCalculationExecutionResponseTypeDef",
    {
        "State": CalculationExecutionStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TerminateSessionResponseTypeDef = TypedDict(
    "TerminateSessionResponseTypeDef",
    {
        "State": SessionStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetNamedQueryOutputTypeDef = TypedDict(
    "BatchGetNamedQueryOutputTypeDef",
    {
        "NamedQueries": List[NamedQueryTypeDef],
        "UnprocessedNamedQueryIds": List[UnprocessedNamedQueryIdTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPreparedStatementOutputTypeDef = TypedDict(
    "GetPreparedStatementOutputTypeDef",
    {
        "PreparedStatement": PreparedStatementTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetPreparedStatementOutputTypeDef = TypedDict(
    "BatchGetPreparedStatementOutputTypeDef",
    {
        "PreparedStatements": List[PreparedStatementTypeDef],
        "UnprocessedPreparedStatementNames": List[UnprocessedPreparedStatementNameTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartCalculationExecutionRequestRequestTypeDef = TypedDict(
    "StartCalculationExecutionRequestRequestTypeDef",
    {
        "SessionId": str,
        "Description": NotRequired[str],
        "CalculationConfiguration": NotRequired[CalculationConfigurationTypeDef],
        "CodeBlock": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
    },
)
CalculationSummaryTypeDef = TypedDict(
    "CalculationSummaryTypeDef",
    {
        "CalculationExecutionId": NotRequired[str],
        "Description": NotRequired[str],
        "Status": NotRequired[CalculationStatusTypeDef],
    },
)
GetCalculationExecutionResponseTypeDef = TypedDict(
    "GetCalculationExecutionResponseTypeDef",
    {
        "CalculationExecutionId": str,
        "SessionId": str,
        "Description": str,
        "WorkingDirectory": str,
        "Status": CalculationStatusTypeDef,
        "Statistics": CalculationStatisticsTypeDef,
        "Result": CalculationResultTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCalculationExecutionStatusResponseTypeDef = TypedDict(
    "GetCalculationExecutionStatusResponseTypeDef",
    {
        "Status": CalculationStatusTypeDef,
        "Statistics": CalculationStatisticsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CapacityReservationTypeDef = TypedDict(
    "CapacityReservationTypeDef",
    {
        "Name": str,
        "Status": CapacityReservationStatusType,
        "TargetDpus": int,
        "AllocatedDpus": int,
        "CreationTime": datetime,
        "LastAllocation": NotRequired[CapacityAllocationTypeDef],
        "LastSuccessfulAllocationTime": NotRequired[datetime],
    },
)
CapacityAssignmentConfigurationTypeDef = TypedDict(
    "CapacityAssignmentConfigurationTypeDef",
    {
        "CapacityReservationName": NotRequired[str],
        "CapacityAssignments": NotRequired[List[CapacityAssignmentOutputTypeDef]],
    },
)
CapacityAssignmentUnionTypeDef = Union[CapacityAssignmentTypeDef, CapacityAssignmentOutputTypeDef]
ResultSetMetadataTypeDef = TypedDict(
    "ResultSetMetadataTypeDef",
    {
        "ColumnInfo": NotRequired[List[ColumnInfoTypeDef]],
    },
)
TableMetadataTypeDef = TypedDict(
    "TableMetadataTypeDef",
    {
        "Name": str,
        "CreateTime": NotRequired[datetime],
        "LastAccessTime": NotRequired[datetime],
        "TableType": NotRequired[str],
        "Columns": NotRequired[List[ColumnTypeDef]],
        "PartitionKeys": NotRequired[List[ColumnTypeDef]],
        "Parameters": NotRequired[Dict[str, str]],
    },
)
CreateCapacityReservationInputRequestTypeDef = TypedDict(
    "CreateCapacityReservationInputRequestTypeDef",
    {
        "TargetDpus": int,
        "Name": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateDataCatalogInputRequestTypeDef = TypedDict(
    "CreateDataCatalogInputRequestTypeDef",
    {
        "Name": str,
        "Type": DataCatalogTypeType,
        "Description": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)
ListDataCatalogsOutputTypeDef = TypedDict(
    "ListDataCatalogsOutputTypeDef",
    {
        "DataCatalogsSummary": List[DataCatalogSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetDataCatalogOutputTypeDef = TypedDict(
    "GetDataCatalogOutputTypeDef",
    {
        "DataCatalog": DataCatalogTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDatabaseOutputTypeDef = TypedDict(
    "GetDatabaseOutputTypeDef",
    {
        "Database": DatabaseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDatabasesOutputTypeDef = TypedDict(
    "ListDatabasesOutputTypeDef",
    {
        "DatabaseList": List[DatabaseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
RowTypeDef = TypedDict(
    "RowTypeDef",
    {
        "Data": NotRequired[List[DatumTypeDef]],
    },
)
ResultConfigurationTypeDef = TypedDict(
    "ResultConfigurationTypeDef",
    {
        "OutputLocation": NotRequired[str],
        "EncryptionConfiguration": NotRequired[EncryptionConfigurationTypeDef],
        "ExpectedBucketOwner": NotRequired[str],
        "AclConfiguration": NotRequired[AclConfigurationTypeDef],
    },
)
ResultConfigurationUpdatesTypeDef = TypedDict(
    "ResultConfigurationUpdatesTypeDef",
    {
        "OutputLocation": NotRequired[str],
        "RemoveOutputLocation": NotRequired[bool],
        "EncryptionConfiguration": NotRequired[EncryptionConfigurationTypeDef],
        "RemoveEncryptionConfiguration": NotRequired[bool],
        "ExpectedBucketOwner": NotRequired[str],
        "RemoveExpectedBucketOwner": NotRequired[bool],
        "AclConfiguration": NotRequired[AclConfigurationTypeDef],
        "RemoveAclConfiguration": NotRequired[bool],
    },
)
SessionConfigurationTypeDef = TypedDict(
    "SessionConfigurationTypeDef",
    {
        "ExecutionRole": NotRequired[str],
        "WorkingDirectory": NotRequired[str],
        "IdleTimeoutSeconds": NotRequired[int],
        "EncryptionConfiguration": NotRequired[EncryptionConfigurationTypeDef],
    },
)
StartSessionRequestRequestTypeDef = TypedDict(
    "StartSessionRequestRequestTypeDef",
    {
        "WorkGroup": str,
        "EngineConfiguration": EngineConfigurationTypeDef,
        "Description": NotRequired[str],
        "NotebookVersion": NotRequired[str],
        "SessionIdleTimeoutInMinutes": NotRequired[int],
        "ClientRequestToken": NotRequired[str],
    },
)
ListEngineVersionsOutputTypeDef = TypedDict(
    "ListEngineVersionsOutputTypeDef",
    {
        "EngineVersions": List[EngineVersionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
WorkGroupSummaryTypeDef = TypedDict(
    "WorkGroupSummaryTypeDef",
    {
        "Name": NotRequired[str],
        "State": NotRequired[WorkGroupStateType],
        "Description": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "EngineVersion": NotRequired[EngineVersionTypeDef],
        "IdentityCenterApplicationArn": NotRequired[str],
    },
)
ListExecutorsResponseTypeDef = TypedDict(
    "ListExecutorsResponseTypeDef",
    {
        "SessionId": str,
        "ExecutorsSummary": List[ExecutorsSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ExportNotebookOutputTypeDef = TypedDict(
    "ExportNotebookOutputTypeDef",
    {
        "NotebookMetadata": NotebookMetadataTypeDef,
        "Payload": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetNotebookMetadataOutputTypeDef = TypedDict(
    "GetNotebookMetadataOutputTypeDef",
    {
        "NotebookMetadata": NotebookMetadataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListNotebookMetadataOutputTypeDef = TypedDict(
    "ListNotebookMetadataOutputTypeDef",
    {
        "NotebookMetadataList": List[NotebookMetadataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListNotebookMetadataInputRequestTypeDef = TypedDict(
    "ListNotebookMetadataInputRequestTypeDef",
    {
        "WorkGroup": str,
        "Filters": NotRequired[FilterDefinitionTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GetQueryResultsInputGetQueryResultsPaginateTypeDef = TypedDict(
    "GetQueryResultsInputGetQueryResultsPaginateTypeDef",
    {
        "QueryExecutionId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDataCatalogsInputListDataCatalogsPaginateTypeDef = TypedDict(
    "ListDataCatalogsInputListDataCatalogsPaginateTypeDef",
    {
        "WorkGroup": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDatabasesInputListDatabasesPaginateTypeDef = TypedDict(
    "ListDatabasesInputListDatabasesPaginateTypeDef",
    {
        "CatalogName": str,
        "WorkGroup": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListNamedQueriesInputListNamedQueriesPaginateTypeDef = TypedDict(
    "ListNamedQueriesInputListNamedQueriesPaginateTypeDef",
    {
        "WorkGroup": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListQueryExecutionsInputListQueryExecutionsPaginateTypeDef = TypedDict(
    "ListQueryExecutionsInputListQueryExecutionsPaginateTypeDef",
    {
        "WorkGroup": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTableMetadataInputListTableMetadataPaginateTypeDef = TypedDict(
    "ListTableMetadataInputListTableMetadataPaginateTypeDef",
    {
        "CatalogName": str,
        "DatabaseName": str,
        "Expression": NotRequired[str],
        "WorkGroup": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTagsForResourceInputListTagsForResourcePaginateTypeDef = TypedDict(
    "ListTagsForResourceInputListTagsForResourcePaginateTypeDef",
    {
        "ResourceARN": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetSessionStatusResponseTypeDef = TypedDict(
    "GetSessionStatusResponseTypeDef",
    {
        "SessionId": str,
        "Status": SessionStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SessionSummaryTypeDef = TypedDict(
    "SessionSummaryTypeDef",
    {
        "SessionId": NotRequired[str],
        "Description": NotRequired[str],
        "EngineVersion": NotRequired[EngineVersionTypeDef],
        "NotebookVersion": NotRequired[str],
        "Status": NotRequired[SessionStatusTypeDef],
    },
)
ListNotebookSessionsResponseTypeDef = TypedDict(
    "ListNotebookSessionsResponseTypeDef",
    {
        "NotebookSessionsList": List[NotebookSessionSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListPreparedStatementsOutputTypeDef = TypedDict(
    "ListPreparedStatementsOutputTypeDef",
    {
        "PreparedStatements": List[PreparedStatementSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
QueryExecutionStatisticsTypeDef = TypedDict(
    "QueryExecutionStatisticsTypeDef",
    {
        "EngineExecutionTimeInMillis": NotRequired[int],
        "DataScannedInBytes": NotRequired[int],
        "DataManifestLocation": NotRequired[str],
        "TotalExecutionTimeInMillis": NotRequired[int],
        "QueryQueueTimeInMillis": NotRequired[int],
        "ServicePreProcessingTimeInMillis": NotRequired[int],
        "QueryPlanningTimeInMillis": NotRequired[int],
        "ServiceProcessingTimeInMillis": NotRequired[int],
        "ResultReuseInformation": NotRequired[ResultReuseInformationTypeDef],
    },
)
QueryStageTypeDef = TypedDict(
    "QueryStageTypeDef",
    {
        "StageId": NotRequired[int],
        "State": NotRequired[str],
        "OutputBytes": NotRequired[int],
        "OutputRows": NotRequired[int],
        "InputBytes": NotRequired[int],
        "InputRows": NotRequired[int],
        "ExecutionTime": NotRequired[int],
        "QueryStagePlan": NotRequired[QueryStagePlanNodeTypeDef],
        "SubStages": NotRequired[List[Dict[str, Any]]],
    },
)
ResultReuseConfigurationTypeDef = TypedDict(
    "ResultReuseConfigurationTypeDef",
    {
        "ResultReuseByAgeConfiguration": NotRequired[ResultReuseByAgeConfigurationTypeDef],
    },
)
ListCalculationExecutionsResponseTypeDef = TypedDict(
    "ListCalculationExecutionsResponseTypeDef",
    {
        "Calculations": List[CalculationSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetCapacityReservationOutputTypeDef = TypedDict(
    "GetCapacityReservationOutputTypeDef",
    {
        "CapacityReservation": CapacityReservationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCapacityReservationsOutputTypeDef = TypedDict(
    "ListCapacityReservationsOutputTypeDef",
    {
        "CapacityReservations": List[CapacityReservationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetCapacityAssignmentConfigurationOutputTypeDef = TypedDict(
    "GetCapacityAssignmentConfigurationOutputTypeDef",
    {
        "CapacityAssignmentConfiguration": CapacityAssignmentConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutCapacityAssignmentConfigurationInputRequestTypeDef = TypedDict(
    "PutCapacityAssignmentConfigurationInputRequestTypeDef",
    {
        "CapacityReservationName": str,
        "CapacityAssignments": Sequence[CapacityAssignmentUnionTypeDef],
    },
)
GetTableMetadataOutputTypeDef = TypedDict(
    "GetTableMetadataOutputTypeDef",
    {
        "TableMetadata": TableMetadataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTableMetadataOutputTypeDef = TypedDict(
    "ListTableMetadataOutputTypeDef",
    {
        "TableMetadataList": List[TableMetadataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ResultSetTypeDef = TypedDict(
    "ResultSetTypeDef",
    {
        "Rows": NotRequired[List[RowTypeDef]],
        "ResultSetMetadata": NotRequired[ResultSetMetadataTypeDef],
    },
)
WorkGroupConfigurationTypeDef = TypedDict(
    "WorkGroupConfigurationTypeDef",
    {
        "ResultConfiguration": NotRequired[ResultConfigurationTypeDef],
        "EnforceWorkGroupConfiguration": NotRequired[bool],
        "PublishCloudWatchMetricsEnabled": NotRequired[bool],
        "BytesScannedCutoffPerQuery": NotRequired[int],
        "RequesterPaysEnabled": NotRequired[bool],
        "EngineVersion": NotRequired[EngineVersionTypeDef],
        "AdditionalConfiguration": NotRequired[str],
        "ExecutionRole": NotRequired[str],
        "CustomerContentEncryptionConfiguration": NotRequired[
            CustomerContentEncryptionConfigurationTypeDef
        ],
        "EnableMinimumEncryptionConfiguration": NotRequired[bool],
        "IdentityCenterConfiguration": NotRequired[IdentityCenterConfigurationTypeDef],
        "QueryResultsS3AccessGrantsConfiguration": NotRequired[
            QueryResultsS3AccessGrantsConfigurationTypeDef
        ],
    },
)
WorkGroupConfigurationUpdatesTypeDef = TypedDict(
    "WorkGroupConfigurationUpdatesTypeDef",
    {
        "EnforceWorkGroupConfiguration": NotRequired[bool],
        "ResultConfigurationUpdates": NotRequired[ResultConfigurationUpdatesTypeDef],
        "PublishCloudWatchMetricsEnabled": NotRequired[bool],
        "BytesScannedCutoffPerQuery": NotRequired[int],
        "RemoveBytesScannedCutoffPerQuery": NotRequired[bool],
        "RequesterPaysEnabled": NotRequired[bool],
        "EngineVersion": NotRequired[EngineVersionTypeDef],
        "RemoveCustomerContentEncryptionConfiguration": NotRequired[bool],
        "AdditionalConfiguration": NotRequired[str],
        "ExecutionRole": NotRequired[str],
        "CustomerContentEncryptionConfiguration": NotRequired[
            CustomerContentEncryptionConfigurationTypeDef
        ],
        "EnableMinimumEncryptionConfiguration": NotRequired[bool],
        "QueryResultsS3AccessGrantsConfiguration": NotRequired[
            QueryResultsS3AccessGrantsConfigurationTypeDef
        ],
    },
)
GetSessionResponseTypeDef = TypedDict(
    "GetSessionResponseTypeDef",
    {
        "SessionId": str,
        "Description": str,
        "WorkGroup": str,
        "EngineVersion": str,
        "EngineConfiguration": EngineConfigurationOutputTypeDef,
        "NotebookVersion": str,
        "SessionConfiguration": SessionConfigurationTypeDef,
        "Status": SessionStatusTypeDef,
        "Statistics": SessionStatisticsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListWorkGroupsOutputTypeDef = TypedDict(
    "ListWorkGroupsOutputTypeDef",
    {
        "WorkGroups": List[WorkGroupSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListSessionsResponseTypeDef = TypedDict(
    "ListSessionsResponseTypeDef",
    {
        "Sessions": List[SessionSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
QueryRuntimeStatisticsTypeDef = TypedDict(
    "QueryRuntimeStatisticsTypeDef",
    {
        "Timeline": NotRequired[QueryRuntimeStatisticsTimelineTypeDef],
        "Rows": NotRequired[QueryRuntimeStatisticsRowsTypeDef],
        "OutputStage": NotRequired[QueryStageTypeDef],
    },
)
QueryExecutionTypeDef = TypedDict(
    "QueryExecutionTypeDef",
    {
        "QueryExecutionId": NotRequired[str],
        "Query": NotRequired[str],
        "StatementType": NotRequired[StatementTypeType],
        "ResultConfiguration": NotRequired[ResultConfigurationTypeDef],
        "ResultReuseConfiguration": NotRequired[ResultReuseConfigurationTypeDef],
        "QueryExecutionContext": NotRequired[QueryExecutionContextTypeDef],
        "Status": NotRequired[QueryExecutionStatusTypeDef],
        "Statistics": NotRequired[QueryExecutionStatisticsTypeDef],
        "WorkGroup": NotRequired[str],
        "EngineVersion": NotRequired[EngineVersionTypeDef],
        "ExecutionParameters": NotRequired[List[str]],
        "SubstatementType": NotRequired[str],
        "QueryResultsS3AccessGrantsConfiguration": NotRequired[
            QueryResultsS3AccessGrantsConfigurationTypeDef
        ],
    },
)
StartQueryExecutionInputRequestTypeDef = TypedDict(
    "StartQueryExecutionInputRequestTypeDef",
    {
        "QueryString": str,
        "ClientRequestToken": NotRequired[str],
        "QueryExecutionContext": NotRequired[QueryExecutionContextTypeDef],
        "ResultConfiguration": NotRequired[ResultConfigurationTypeDef],
        "WorkGroup": NotRequired[str],
        "ExecutionParameters": NotRequired[Sequence[str]],
        "ResultReuseConfiguration": NotRequired[ResultReuseConfigurationTypeDef],
    },
)
GetQueryResultsOutputTypeDef = TypedDict(
    "GetQueryResultsOutputTypeDef",
    {
        "UpdateCount": int,
        "ResultSet": ResultSetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateWorkGroupInputRequestTypeDef = TypedDict(
    "CreateWorkGroupInputRequestTypeDef",
    {
        "Name": str,
        "Configuration": NotRequired[WorkGroupConfigurationTypeDef],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
WorkGroupTypeDef = TypedDict(
    "WorkGroupTypeDef",
    {
        "Name": str,
        "State": NotRequired[WorkGroupStateType],
        "Configuration": NotRequired[WorkGroupConfigurationTypeDef],
        "Description": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "IdentityCenterApplicationArn": NotRequired[str],
    },
)
UpdateWorkGroupInputRequestTypeDef = TypedDict(
    "UpdateWorkGroupInputRequestTypeDef",
    {
        "WorkGroup": str,
        "Description": NotRequired[str],
        "ConfigurationUpdates": NotRequired[WorkGroupConfigurationUpdatesTypeDef],
        "State": NotRequired[WorkGroupStateType],
    },
)
GetQueryRuntimeStatisticsOutputTypeDef = TypedDict(
    "GetQueryRuntimeStatisticsOutputTypeDef",
    {
        "QueryRuntimeStatistics": QueryRuntimeStatisticsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetQueryExecutionOutputTypeDef = TypedDict(
    "BatchGetQueryExecutionOutputTypeDef",
    {
        "QueryExecutions": List[QueryExecutionTypeDef],
        "UnprocessedQueryExecutionIds": List[UnprocessedQueryExecutionIdTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetQueryExecutionOutputTypeDef = TypedDict(
    "GetQueryExecutionOutputTypeDef",
    {
        "QueryExecution": QueryExecutionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetWorkGroupOutputTypeDef = TypedDict(
    "GetWorkGroupOutputTypeDef",
    {
        "WorkGroup": WorkGroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
