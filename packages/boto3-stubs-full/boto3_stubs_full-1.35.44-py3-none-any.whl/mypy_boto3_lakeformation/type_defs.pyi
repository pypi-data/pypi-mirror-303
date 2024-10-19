"""
Type annotations for lakeformation service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/type_defs/)

Usage::

    ```python
    from mypy_boto3_lakeformation.type_defs import ResponseMetadataTypeDef

    data: ResponseMetadataTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    ApplicationStatusType,
    ComparisonOperatorType,
    DataLakeResourceTypeType,
    EnableStatusType,
    FieldNameStringType,
    OptimizerTypeType,
    PermissionType,
    PermissionTypeType,
    QueryStateStringType,
    ResourceShareTypeType,
    ResourceTypeType,
    TransactionStatusFilterType,
    TransactionStatusType,
    TransactionTypeType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "ResponseMetadataTypeDef",
    "AddObjectInputTypeDef",
    "AssumeDecoratedRoleWithSAMLRequestRequestTypeDef",
    "AuditContextTypeDef",
    "ErrorDetailTypeDef",
    "DataLakePrincipalTypeDef",
    "CancelTransactionRequestRequestTypeDef",
    "LFTagPairOutputTypeDef",
    "ColumnWildcardOutputTypeDef",
    "ColumnWildcardTypeDef",
    "CommitTransactionRequestRequestTypeDef",
    "CreateLFTagRequestRequestTypeDef",
    "ExternalFilteringConfigurationTypeDef",
    "RowFilterOutputTypeDef",
    "DataCellsFilterResourceTypeDef",
    "DataLocationResourceTypeDef",
    "DatabaseResourceTypeDef",
    "DeleteDataCellsFilterRequestRequestTypeDef",
    "DeleteLFTagRequestRequestTypeDef",
    "DeleteLakeFormationIdentityCenterConfigurationRequestRequestTypeDef",
    "DeleteObjectInputTypeDef",
    "VirtualObjectTypeDef",
    "DeregisterResourceRequestRequestTypeDef",
    "DescribeLakeFormationIdentityCenterConfigurationRequestRequestTypeDef",
    "ExternalFilteringConfigurationOutputTypeDef",
    "DescribeResourceRequestRequestTypeDef",
    "ResourceInfoTypeDef",
    "DescribeTransactionRequestRequestTypeDef",
    "TransactionDescriptionTypeDef",
    "DetailsMapTypeDef",
    "ExecutionStatisticsTypeDef",
    "ExtendTransactionRequestRequestTypeDef",
    "FilterConditionTypeDef",
    "GetDataCellsFilterRequestRequestTypeDef",
    "GetDataLakeSettingsRequestRequestTypeDef",
    "GetEffectivePermissionsForPathRequestRequestTypeDef",
    "GetLFTagRequestRequestTypeDef",
    "GetQueryStateRequestRequestTypeDef",
    "GetQueryStatisticsRequestRequestTypeDef",
    "PlanningStatisticsTypeDef",
    "TimestampTypeDef",
    "PartitionValueListTypeDef",
    "GetWorkUnitResultsRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "GetWorkUnitsRequestRequestTypeDef",
    "WorkUnitRangeTypeDef",
    "LFTagKeyResourceOutputTypeDef",
    "LFTagKeyResourceTypeDef",
    "LFTagOutputTypeDef",
    "LFTagPairTypeDef",
    "LFTagTypeDef",
    "TableResourceTypeDef",
    "ListLFTagsRequestRequestTypeDef",
    "ListTableStorageOptimizersRequestRequestTypeDef",
    "StorageOptimizerTypeDef",
    "ListTransactionsRequestRequestTypeDef",
    "TableObjectTypeDef",
    "RegisterResourceRequestRequestTypeDef",
    "TableResourceOutputTypeDef",
    "RowFilterTypeDef",
    "StartTransactionRequestRequestTypeDef",
    "UpdateLFTagRequestRequestTypeDef",
    "UpdateResourceRequestRequestTypeDef",
    "UpdateTableStorageOptimizerRequestRequestTypeDef",
    "AssumeDecoratedRoleWithSAMLResponseTypeDef",
    "CommitTransactionResponseTypeDef",
    "CreateLakeFormationIdentityCenterConfigurationResponseTypeDef",
    "GetDataLakePrincipalResponseTypeDef",
    "GetLFTagResponseTypeDef",
    "GetQueryStateResponseTypeDef",
    "GetTemporaryGluePartitionCredentialsResponseTypeDef",
    "GetTemporaryGlueTableCredentialsResponseTypeDef",
    "GetWorkUnitResultsResponseTypeDef",
    "StartQueryPlanningResponseTypeDef",
    "StartTransactionResponseTypeDef",
    "UpdateTableStorageOptimizerResponseTypeDef",
    "PrincipalPermissionsOutputTypeDef",
    "PrincipalPermissionsTypeDef",
    "ColumnLFTagTypeDef",
    "LFTagErrorTypeDef",
    "ListLFTagsResponseTypeDef",
    "TableWithColumnsResourceOutputTypeDef",
    "ColumnWildcardUnionTypeDef",
    "CreateLakeFormationIdentityCenterConfigurationRequestRequestTypeDef",
    "UpdateLakeFormationIdentityCenterConfigurationRequestRequestTypeDef",
    "DataCellsFilterOutputTypeDef",
    "TaggedDatabaseTypeDef",
    "WriteOperationTypeDef",
    "DeleteObjectsOnCancelRequestRequestTypeDef",
    "DescribeLakeFormationIdentityCenterConfigurationResponseTypeDef",
    "DescribeResourceResponseTypeDef",
    "ListResourcesResponseTypeDef",
    "DescribeTransactionResponseTypeDef",
    "ListTransactionsResponseTypeDef",
    "ListResourcesRequestRequestTypeDef",
    "GetQueryStatisticsResponseTypeDef",
    "GetTableObjectsRequestRequestTypeDef",
    "QueryPlanningContextTypeDef",
    "QuerySessionContextTypeDef",
    "GetTemporaryGluePartitionCredentialsRequestRequestTypeDef",
    "GetWorkUnitsRequestGetWorkUnitsPaginateTypeDef",
    "ListLFTagsRequestListLFTagsPaginateTypeDef",
    "GetWorkUnitsResponseTypeDef",
    "LFTagKeyResourceUnionTypeDef",
    "LFTagPolicyResourceOutputTypeDef",
    "LFTagPairUnionTypeDef",
    "LFTagUnionTypeDef",
    "SearchDatabasesByLFTagsRequestSearchDatabasesByLFTagsPaginateTypeDef",
    "SearchTablesByLFTagsRequestRequestTypeDef",
    "SearchTablesByLFTagsRequestSearchTablesByLFTagsPaginateTypeDef",
    "ListDataCellsFilterRequestListDataCellsFilterPaginateTypeDef",
    "ListDataCellsFilterRequestRequestTypeDef",
    "ListTableStorageOptimizersResponseTypeDef",
    "PartitionObjectsTypeDef",
    "TableResourceUnionTypeDef",
    "RowFilterUnionTypeDef",
    "DataLakeSettingsOutputTypeDef",
    "PrincipalPermissionsUnionTypeDef",
    "GetResourceLFTagsResponseTypeDef",
    "TaggedTableTypeDef",
    "AddLFTagsToResourceResponseTypeDef",
    "RemoveLFTagsFromResourceResponseTypeDef",
    "TableWithColumnsResourceTypeDef",
    "GetDataCellsFilterResponseTypeDef",
    "ListDataCellsFilterResponseTypeDef",
    "SearchDatabasesByLFTagsResponseTypeDef",
    "UpdateTableObjectsRequestRequestTypeDef",
    "StartQueryPlanningRequestRequestTypeDef",
    "GetTemporaryGlueTableCredentialsRequestRequestTypeDef",
    "ResourceOutputTypeDef",
    "LFTagPolicyResourceTypeDef",
    "SearchDatabasesByLFTagsRequestRequestTypeDef",
    "GetTableObjectsResponseTypeDef",
    "DataCellsFilterTypeDef",
    "GetDataLakeSettingsResponseTypeDef",
    "DataLakeSettingsTypeDef",
    "SearchTablesByLFTagsResponseTypeDef",
    "TableWithColumnsResourceUnionTypeDef",
    "BatchPermissionsRequestEntryOutputTypeDef",
    "LakeFormationOptInsInfoTypeDef",
    "PrincipalResourcePermissionsTypeDef",
    "LFTagPolicyResourceUnionTypeDef",
    "CreateDataCellsFilterRequestRequestTypeDef",
    "UpdateDataCellsFilterRequestRequestTypeDef",
    "PutDataLakeSettingsRequestRequestTypeDef",
    "BatchPermissionsFailureEntryTypeDef",
    "ListLakeFormationOptInsResponseTypeDef",
    "GetEffectivePermissionsForPathResponseTypeDef",
    "ListPermissionsResponseTypeDef",
    "ResourceTypeDef",
    "BatchGrantPermissionsResponseTypeDef",
    "BatchRevokePermissionsResponseTypeDef",
    "AddLFTagsToResourceRequestRequestTypeDef",
    "CreateLakeFormationOptInRequestRequestTypeDef",
    "DeleteLakeFormationOptInRequestRequestTypeDef",
    "GetResourceLFTagsRequestRequestTypeDef",
    "GrantPermissionsRequestRequestTypeDef",
    "ListLakeFormationOptInsRequestRequestTypeDef",
    "ListPermissionsRequestRequestTypeDef",
    "RemoveLFTagsFromResourceRequestRequestTypeDef",
    "ResourceUnionTypeDef",
    "RevokePermissionsRequestRequestTypeDef",
    "BatchPermissionsRequestEntryTypeDef",
    "BatchPermissionsRequestEntryUnionTypeDef",
    "BatchRevokePermissionsRequestRequestTypeDef",
    "BatchGrantPermissionsRequestRequestTypeDef",
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
AddObjectInputTypeDef = TypedDict(
    "AddObjectInputTypeDef",
    {
        "Uri": str,
        "ETag": str,
        "Size": int,
        "PartitionValues": NotRequired[Sequence[str]],
    },
)
AssumeDecoratedRoleWithSAMLRequestRequestTypeDef = TypedDict(
    "AssumeDecoratedRoleWithSAMLRequestRequestTypeDef",
    {
        "SAMLAssertion": str,
        "RoleArn": str,
        "PrincipalArn": str,
        "DurationSeconds": NotRequired[int],
    },
)
AuditContextTypeDef = TypedDict(
    "AuditContextTypeDef",
    {
        "AdditionalAuditContext": NotRequired[str],
    },
)
ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef",
    {
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)
DataLakePrincipalTypeDef = TypedDict(
    "DataLakePrincipalTypeDef",
    {
        "DataLakePrincipalIdentifier": NotRequired[str],
    },
)
CancelTransactionRequestRequestTypeDef = TypedDict(
    "CancelTransactionRequestRequestTypeDef",
    {
        "TransactionId": str,
    },
)
LFTagPairOutputTypeDef = TypedDict(
    "LFTagPairOutputTypeDef",
    {
        "TagKey": str,
        "TagValues": List[str],
        "CatalogId": NotRequired[str],
    },
)
ColumnWildcardOutputTypeDef = TypedDict(
    "ColumnWildcardOutputTypeDef",
    {
        "ExcludedColumnNames": NotRequired[List[str]],
    },
)
ColumnWildcardTypeDef = TypedDict(
    "ColumnWildcardTypeDef",
    {
        "ExcludedColumnNames": NotRequired[Sequence[str]],
    },
)
CommitTransactionRequestRequestTypeDef = TypedDict(
    "CommitTransactionRequestRequestTypeDef",
    {
        "TransactionId": str,
    },
)
CreateLFTagRequestRequestTypeDef = TypedDict(
    "CreateLFTagRequestRequestTypeDef",
    {
        "TagKey": str,
        "TagValues": Sequence[str],
        "CatalogId": NotRequired[str],
    },
)
ExternalFilteringConfigurationTypeDef = TypedDict(
    "ExternalFilteringConfigurationTypeDef",
    {
        "Status": EnableStatusType,
        "AuthorizedTargets": Sequence[str],
    },
)
RowFilterOutputTypeDef = TypedDict(
    "RowFilterOutputTypeDef",
    {
        "FilterExpression": NotRequired[str],
        "AllRowsWildcard": NotRequired[Dict[str, Any]],
    },
)
DataCellsFilterResourceTypeDef = TypedDict(
    "DataCellsFilterResourceTypeDef",
    {
        "TableCatalogId": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "TableName": NotRequired[str],
        "Name": NotRequired[str],
    },
)
DataLocationResourceTypeDef = TypedDict(
    "DataLocationResourceTypeDef",
    {
        "ResourceArn": str,
        "CatalogId": NotRequired[str],
    },
)
DatabaseResourceTypeDef = TypedDict(
    "DatabaseResourceTypeDef",
    {
        "Name": str,
        "CatalogId": NotRequired[str],
    },
)
DeleteDataCellsFilterRequestRequestTypeDef = TypedDict(
    "DeleteDataCellsFilterRequestRequestTypeDef",
    {
        "TableCatalogId": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "TableName": NotRequired[str],
        "Name": NotRequired[str],
    },
)
DeleteLFTagRequestRequestTypeDef = TypedDict(
    "DeleteLFTagRequestRequestTypeDef",
    {
        "TagKey": str,
        "CatalogId": NotRequired[str],
    },
)
DeleteLakeFormationIdentityCenterConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteLakeFormationIdentityCenterConfigurationRequestRequestTypeDef",
    {
        "CatalogId": NotRequired[str],
    },
)
DeleteObjectInputTypeDef = TypedDict(
    "DeleteObjectInputTypeDef",
    {
        "Uri": str,
        "ETag": NotRequired[str],
        "PartitionValues": NotRequired[Sequence[str]],
    },
)
VirtualObjectTypeDef = TypedDict(
    "VirtualObjectTypeDef",
    {
        "Uri": str,
        "ETag": NotRequired[str],
    },
)
DeregisterResourceRequestRequestTypeDef = TypedDict(
    "DeregisterResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
DescribeLakeFormationIdentityCenterConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeLakeFormationIdentityCenterConfigurationRequestRequestTypeDef",
    {
        "CatalogId": NotRequired[str],
    },
)
ExternalFilteringConfigurationOutputTypeDef = TypedDict(
    "ExternalFilteringConfigurationOutputTypeDef",
    {
        "Status": EnableStatusType,
        "AuthorizedTargets": List[str],
    },
)
DescribeResourceRequestRequestTypeDef = TypedDict(
    "DescribeResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
ResourceInfoTypeDef = TypedDict(
    "ResourceInfoTypeDef",
    {
        "ResourceArn": NotRequired[str],
        "RoleArn": NotRequired[str],
        "LastModified": NotRequired[datetime],
        "WithFederation": NotRequired[bool],
        "HybridAccessEnabled": NotRequired[bool],
    },
)
DescribeTransactionRequestRequestTypeDef = TypedDict(
    "DescribeTransactionRequestRequestTypeDef",
    {
        "TransactionId": str,
    },
)
TransactionDescriptionTypeDef = TypedDict(
    "TransactionDescriptionTypeDef",
    {
        "TransactionId": NotRequired[str],
        "TransactionStatus": NotRequired[TransactionStatusType],
        "TransactionStartTime": NotRequired[datetime],
        "TransactionEndTime": NotRequired[datetime],
    },
)
DetailsMapTypeDef = TypedDict(
    "DetailsMapTypeDef",
    {
        "ResourceShare": NotRequired[List[str]],
    },
)
ExecutionStatisticsTypeDef = TypedDict(
    "ExecutionStatisticsTypeDef",
    {
        "AverageExecutionTimeMillis": NotRequired[int],
        "DataScannedBytes": NotRequired[int],
        "WorkUnitsExecutedCount": NotRequired[int],
    },
)
ExtendTransactionRequestRequestTypeDef = TypedDict(
    "ExtendTransactionRequestRequestTypeDef",
    {
        "TransactionId": NotRequired[str],
    },
)
FilterConditionTypeDef = TypedDict(
    "FilterConditionTypeDef",
    {
        "Field": NotRequired[FieldNameStringType],
        "ComparisonOperator": NotRequired[ComparisonOperatorType],
        "StringValueList": NotRequired[Sequence[str]],
    },
)
GetDataCellsFilterRequestRequestTypeDef = TypedDict(
    "GetDataCellsFilterRequestRequestTypeDef",
    {
        "TableCatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "Name": str,
    },
)
GetDataLakeSettingsRequestRequestTypeDef = TypedDict(
    "GetDataLakeSettingsRequestRequestTypeDef",
    {
        "CatalogId": NotRequired[str],
    },
)
GetEffectivePermissionsForPathRequestRequestTypeDef = TypedDict(
    "GetEffectivePermissionsForPathRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "CatalogId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GetLFTagRequestRequestTypeDef = TypedDict(
    "GetLFTagRequestRequestTypeDef",
    {
        "TagKey": str,
        "CatalogId": NotRequired[str],
    },
)
GetQueryStateRequestRequestTypeDef = TypedDict(
    "GetQueryStateRequestRequestTypeDef",
    {
        "QueryId": str,
    },
)
GetQueryStatisticsRequestRequestTypeDef = TypedDict(
    "GetQueryStatisticsRequestRequestTypeDef",
    {
        "QueryId": str,
    },
)
PlanningStatisticsTypeDef = TypedDict(
    "PlanningStatisticsTypeDef",
    {
        "EstimatedDataToScanBytes": NotRequired[int],
        "PlanningTimeMillis": NotRequired[int],
        "QueueTimeMillis": NotRequired[int],
        "WorkUnitsGeneratedCount": NotRequired[int],
    },
)
TimestampTypeDef = Union[datetime, str]
PartitionValueListTypeDef = TypedDict(
    "PartitionValueListTypeDef",
    {
        "Values": Sequence[str],
    },
)
GetWorkUnitResultsRequestRequestTypeDef = TypedDict(
    "GetWorkUnitResultsRequestRequestTypeDef",
    {
        "QueryId": str,
        "WorkUnitId": int,
        "WorkUnitToken": str,
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
GetWorkUnitsRequestRequestTypeDef = TypedDict(
    "GetWorkUnitsRequestRequestTypeDef",
    {
        "QueryId": str,
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
WorkUnitRangeTypeDef = TypedDict(
    "WorkUnitRangeTypeDef",
    {
        "WorkUnitIdMax": int,
        "WorkUnitIdMin": int,
        "WorkUnitToken": str,
    },
)
LFTagKeyResourceOutputTypeDef = TypedDict(
    "LFTagKeyResourceOutputTypeDef",
    {
        "TagKey": str,
        "TagValues": List[str],
        "CatalogId": NotRequired[str],
    },
)
LFTagKeyResourceTypeDef = TypedDict(
    "LFTagKeyResourceTypeDef",
    {
        "TagKey": str,
        "TagValues": Sequence[str],
        "CatalogId": NotRequired[str],
    },
)
LFTagOutputTypeDef = TypedDict(
    "LFTagOutputTypeDef",
    {
        "TagKey": str,
        "TagValues": List[str],
    },
)
LFTagPairTypeDef = TypedDict(
    "LFTagPairTypeDef",
    {
        "TagKey": str,
        "TagValues": Sequence[str],
        "CatalogId": NotRequired[str],
    },
)
LFTagTypeDef = TypedDict(
    "LFTagTypeDef",
    {
        "TagKey": str,
        "TagValues": Sequence[str],
    },
)
TableResourceTypeDef = TypedDict(
    "TableResourceTypeDef",
    {
        "DatabaseName": str,
        "CatalogId": NotRequired[str],
        "Name": NotRequired[str],
        "TableWildcard": NotRequired[Mapping[str, Any]],
    },
)
ListLFTagsRequestRequestTypeDef = TypedDict(
    "ListLFTagsRequestRequestTypeDef",
    {
        "CatalogId": NotRequired[str],
        "ResourceShareType": NotRequired[ResourceShareTypeType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTableStorageOptimizersRequestRequestTypeDef = TypedDict(
    "ListTableStorageOptimizersRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "CatalogId": NotRequired[str],
        "StorageOptimizerType": NotRequired[OptimizerTypeType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
StorageOptimizerTypeDef = TypedDict(
    "StorageOptimizerTypeDef",
    {
        "StorageOptimizerType": NotRequired[OptimizerTypeType],
        "Config": NotRequired[Dict[str, str]],
        "ErrorMessage": NotRequired[str],
        "Warnings": NotRequired[str],
        "LastRunDetails": NotRequired[str],
    },
)
ListTransactionsRequestRequestTypeDef = TypedDict(
    "ListTransactionsRequestRequestTypeDef",
    {
        "CatalogId": NotRequired[str],
        "StatusFilter": NotRequired[TransactionStatusFilterType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
TableObjectTypeDef = TypedDict(
    "TableObjectTypeDef",
    {
        "Uri": NotRequired[str],
        "ETag": NotRequired[str],
        "Size": NotRequired[int],
    },
)
RegisterResourceRequestRequestTypeDef = TypedDict(
    "RegisterResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "UseServiceLinkedRole": NotRequired[bool],
        "RoleArn": NotRequired[str],
        "WithFederation": NotRequired[bool],
        "HybridAccessEnabled": NotRequired[bool],
    },
)
TableResourceOutputTypeDef = TypedDict(
    "TableResourceOutputTypeDef",
    {
        "DatabaseName": str,
        "CatalogId": NotRequired[str],
        "Name": NotRequired[str],
        "TableWildcard": NotRequired[Dict[str, Any]],
    },
)
RowFilterTypeDef = TypedDict(
    "RowFilterTypeDef",
    {
        "FilterExpression": NotRequired[str],
        "AllRowsWildcard": NotRequired[Mapping[str, Any]],
    },
)
StartTransactionRequestRequestTypeDef = TypedDict(
    "StartTransactionRequestRequestTypeDef",
    {
        "TransactionType": NotRequired[TransactionTypeType],
    },
)
UpdateLFTagRequestRequestTypeDef = TypedDict(
    "UpdateLFTagRequestRequestTypeDef",
    {
        "TagKey": str,
        "CatalogId": NotRequired[str],
        "TagValuesToDelete": NotRequired[Sequence[str]],
        "TagValuesToAdd": NotRequired[Sequence[str]],
    },
)
UpdateResourceRequestRequestTypeDef = TypedDict(
    "UpdateResourceRequestRequestTypeDef",
    {
        "RoleArn": str,
        "ResourceArn": str,
        "WithFederation": NotRequired[bool],
        "HybridAccessEnabled": NotRequired[bool],
    },
)
UpdateTableStorageOptimizerRequestRequestTypeDef = TypedDict(
    "UpdateTableStorageOptimizerRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "StorageOptimizerConfig": Mapping[OptimizerTypeType, Mapping[str, str]],
        "CatalogId": NotRequired[str],
    },
)
AssumeDecoratedRoleWithSAMLResponseTypeDef = TypedDict(
    "AssumeDecoratedRoleWithSAMLResponseTypeDef",
    {
        "AccessKeyId": str,
        "SecretAccessKey": str,
        "SessionToken": str,
        "Expiration": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CommitTransactionResponseTypeDef = TypedDict(
    "CommitTransactionResponseTypeDef",
    {
        "TransactionStatus": TransactionStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateLakeFormationIdentityCenterConfigurationResponseTypeDef = TypedDict(
    "CreateLakeFormationIdentityCenterConfigurationResponseTypeDef",
    {
        "ApplicationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDataLakePrincipalResponseTypeDef = TypedDict(
    "GetDataLakePrincipalResponseTypeDef",
    {
        "Identity": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLFTagResponseTypeDef = TypedDict(
    "GetLFTagResponseTypeDef",
    {
        "CatalogId": str,
        "TagKey": str,
        "TagValues": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetQueryStateResponseTypeDef = TypedDict(
    "GetQueryStateResponseTypeDef",
    {
        "Error": str,
        "State": QueryStateStringType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTemporaryGluePartitionCredentialsResponseTypeDef = TypedDict(
    "GetTemporaryGluePartitionCredentialsResponseTypeDef",
    {
        "AccessKeyId": str,
        "SecretAccessKey": str,
        "SessionToken": str,
        "Expiration": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTemporaryGlueTableCredentialsResponseTypeDef = TypedDict(
    "GetTemporaryGlueTableCredentialsResponseTypeDef",
    {
        "AccessKeyId": str,
        "SecretAccessKey": str,
        "SessionToken": str,
        "Expiration": datetime,
        "VendedS3Path": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetWorkUnitResultsResponseTypeDef = TypedDict(
    "GetWorkUnitResultsResponseTypeDef",
    {
        "ResultStream": StreamingBody,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartQueryPlanningResponseTypeDef = TypedDict(
    "StartQueryPlanningResponseTypeDef",
    {
        "QueryId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartTransactionResponseTypeDef = TypedDict(
    "StartTransactionResponseTypeDef",
    {
        "TransactionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTableStorageOptimizerResponseTypeDef = TypedDict(
    "UpdateTableStorageOptimizerResponseTypeDef",
    {
        "Result": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PrincipalPermissionsOutputTypeDef = TypedDict(
    "PrincipalPermissionsOutputTypeDef",
    {
        "Principal": NotRequired[DataLakePrincipalTypeDef],
        "Permissions": NotRequired[List[PermissionType]],
    },
)
PrincipalPermissionsTypeDef = TypedDict(
    "PrincipalPermissionsTypeDef",
    {
        "Principal": NotRequired[DataLakePrincipalTypeDef],
        "Permissions": NotRequired[Sequence[PermissionType]],
    },
)
ColumnLFTagTypeDef = TypedDict(
    "ColumnLFTagTypeDef",
    {
        "Name": NotRequired[str],
        "LFTags": NotRequired[List[LFTagPairOutputTypeDef]],
    },
)
LFTagErrorTypeDef = TypedDict(
    "LFTagErrorTypeDef",
    {
        "LFTag": NotRequired[LFTagPairOutputTypeDef],
        "Error": NotRequired[ErrorDetailTypeDef],
    },
)
ListLFTagsResponseTypeDef = TypedDict(
    "ListLFTagsResponseTypeDef",
    {
        "LFTags": List[LFTagPairOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
TableWithColumnsResourceOutputTypeDef = TypedDict(
    "TableWithColumnsResourceOutputTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "CatalogId": NotRequired[str],
        "ColumnNames": NotRequired[List[str]],
        "ColumnWildcard": NotRequired[ColumnWildcardOutputTypeDef],
    },
)
ColumnWildcardUnionTypeDef = Union[ColumnWildcardTypeDef, ColumnWildcardOutputTypeDef]
CreateLakeFormationIdentityCenterConfigurationRequestRequestTypeDef = TypedDict(
    "CreateLakeFormationIdentityCenterConfigurationRequestRequestTypeDef",
    {
        "CatalogId": NotRequired[str],
        "InstanceArn": NotRequired[str],
        "ExternalFiltering": NotRequired[ExternalFilteringConfigurationTypeDef],
        "ShareRecipients": NotRequired[Sequence[DataLakePrincipalTypeDef]],
    },
)
UpdateLakeFormationIdentityCenterConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateLakeFormationIdentityCenterConfigurationRequestRequestTypeDef",
    {
        "CatalogId": NotRequired[str],
        "ShareRecipients": NotRequired[Sequence[DataLakePrincipalTypeDef]],
        "ApplicationStatus": NotRequired[ApplicationStatusType],
        "ExternalFiltering": NotRequired[ExternalFilteringConfigurationTypeDef],
    },
)
DataCellsFilterOutputTypeDef = TypedDict(
    "DataCellsFilterOutputTypeDef",
    {
        "TableCatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "Name": str,
        "RowFilter": NotRequired[RowFilterOutputTypeDef],
        "ColumnNames": NotRequired[List[str]],
        "ColumnWildcard": NotRequired[ColumnWildcardOutputTypeDef],
        "VersionId": NotRequired[str],
    },
)
TaggedDatabaseTypeDef = TypedDict(
    "TaggedDatabaseTypeDef",
    {
        "Database": NotRequired[DatabaseResourceTypeDef],
        "LFTags": NotRequired[List[LFTagPairOutputTypeDef]],
    },
)
WriteOperationTypeDef = TypedDict(
    "WriteOperationTypeDef",
    {
        "AddObject": NotRequired[AddObjectInputTypeDef],
        "DeleteObject": NotRequired[DeleteObjectInputTypeDef],
    },
)
DeleteObjectsOnCancelRequestRequestTypeDef = TypedDict(
    "DeleteObjectsOnCancelRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "TransactionId": str,
        "Objects": Sequence[VirtualObjectTypeDef],
        "CatalogId": NotRequired[str],
    },
)
DescribeLakeFormationIdentityCenterConfigurationResponseTypeDef = TypedDict(
    "DescribeLakeFormationIdentityCenterConfigurationResponseTypeDef",
    {
        "CatalogId": str,
        "InstanceArn": str,
        "ApplicationArn": str,
        "ExternalFiltering": ExternalFilteringConfigurationOutputTypeDef,
        "ShareRecipients": List[DataLakePrincipalTypeDef],
        "ResourceShare": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeResourceResponseTypeDef = TypedDict(
    "DescribeResourceResponseTypeDef",
    {
        "ResourceInfo": ResourceInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListResourcesResponseTypeDef = TypedDict(
    "ListResourcesResponseTypeDef",
    {
        "ResourceInfoList": List[ResourceInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeTransactionResponseTypeDef = TypedDict(
    "DescribeTransactionResponseTypeDef",
    {
        "TransactionDescription": TransactionDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTransactionsResponseTypeDef = TypedDict(
    "ListTransactionsResponseTypeDef",
    {
        "Transactions": List[TransactionDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListResourcesRequestRequestTypeDef = TypedDict(
    "ListResourcesRequestRequestTypeDef",
    {
        "FilterConditionList": NotRequired[Sequence[FilterConditionTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetQueryStatisticsResponseTypeDef = TypedDict(
    "GetQueryStatisticsResponseTypeDef",
    {
        "ExecutionStatistics": ExecutionStatisticsTypeDef,
        "PlanningStatistics": PlanningStatisticsTypeDef,
        "QuerySubmissionTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTableObjectsRequestRequestTypeDef = TypedDict(
    "GetTableObjectsRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "CatalogId": NotRequired[str],
        "TransactionId": NotRequired[str],
        "QueryAsOfTime": NotRequired[TimestampTypeDef],
        "PartitionPredicate": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
QueryPlanningContextTypeDef = TypedDict(
    "QueryPlanningContextTypeDef",
    {
        "DatabaseName": str,
        "CatalogId": NotRequired[str],
        "QueryAsOfTime": NotRequired[TimestampTypeDef],
        "QueryParameters": NotRequired[Mapping[str, str]],
        "TransactionId": NotRequired[str],
    },
)
QuerySessionContextTypeDef = TypedDict(
    "QuerySessionContextTypeDef",
    {
        "QueryId": NotRequired[str],
        "QueryStartTime": NotRequired[TimestampTypeDef],
        "ClusterId": NotRequired[str],
        "QueryAuthorizationId": NotRequired[str],
        "AdditionalContext": NotRequired[Mapping[str, str]],
    },
)
GetTemporaryGluePartitionCredentialsRequestRequestTypeDef = TypedDict(
    "GetTemporaryGluePartitionCredentialsRequestRequestTypeDef",
    {
        "TableArn": str,
        "Partition": PartitionValueListTypeDef,
        "Permissions": NotRequired[Sequence[PermissionType]],
        "DurationSeconds": NotRequired[int],
        "AuditContext": NotRequired[AuditContextTypeDef],
        "SupportedPermissionTypes": NotRequired[Sequence[PermissionTypeType]],
    },
)
GetWorkUnitsRequestGetWorkUnitsPaginateTypeDef = TypedDict(
    "GetWorkUnitsRequestGetWorkUnitsPaginateTypeDef",
    {
        "QueryId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListLFTagsRequestListLFTagsPaginateTypeDef = TypedDict(
    "ListLFTagsRequestListLFTagsPaginateTypeDef",
    {
        "CatalogId": NotRequired[str],
        "ResourceShareType": NotRequired[ResourceShareTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetWorkUnitsResponseTypeDef = TypedDict(
    "GetWorkUnitsResponseTypeDef",
    {
        "QueryId": str,
        "WorkUnitRanges": List[WorkUnitRangeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
LFTagKeyResourceUnionTypeDef = Union[LFTagKeyResourceTypeDef, LFTagKeyResourceOutputTypeDef]
LFTagPolicyResourceOutputTypeDef = TypedDict(
    "LFTagPolicyResourceOutputTypeDef",
    {
        "ResourceType": ResourceTypeType,
        "Expression": List[LFTagOutputTypeDef],
        "CatalogId": NotRequired[str],
    },
)
LFTagPairUnionTypeDef = Union[LFTagPairTypeDef, LFTagPairOutputTypeDef]
LFTagUnionTypeDef = Union[LFTagTypeDef, LFTagOutputTypeDef]
SearchDatabasesByLFTagsRequestSearchDatabasesByLFTagsPaginateTypeDef = TypedDict(
    "SearchDatabasesByLFTagsRequestSearchDatabasesByLFTagsPaginateTypeDef",
    {
        "Expression": Sequence[LFTagTypeDef],
        "CatalogId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchTablesByLFTagsRequestRequestTypeDef = TypedDict(
    "SearchTablesByLFTagsRequestRequestTypeDef",
    {
        "Expression": Sequence[LFTagTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "CatalogId": NotRequired[str],
    },
)
SearchTablesByLFTagsRequestSearchTablesByLFTagsPaginateTypeDef = TypedDict(
    "SearchTablesByLFTagsRequestSearchTablesByLFTagsPaginateTypeDef",
    {
        "Expression": Sequence[LFTagTypeDef],
        "CatalogId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDataCellsFilterRequestListDataCellsFilterPaginateTypeDef = TypedDict(
    "ListDataCellsFilterRequestListDataCellsFilterPaginateTypeDef",
    {
        "Table": NotRequired[TableResourceTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDataCellsFilterRequestRequestTypeDef = TypedDict(
    "ListDataCellsFilterRequestRequestTypeDef",
    {
        "Table": NotRequired[TableResourceTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListTableStorageOptimizersResponseTypeDef = TypedDict(
    "ListTableStorageOptimizersResponseTypeDef",
    {
        "StorageOptimizerList": List[StorageOptimizerTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PartitionObjectsTypeDef = TypedDict(
    "PartitionObjectsTypeDef",
    {
        "PartitionValues": NotRequired[List[str]],
        "Objects": NotRequired[List[TableObjectTypeDef]],
    },
)
TableResourceUnionTypeDef = Union[TableResourceTypeDef, TableResourceOutputTypeDef]
RowFilterUnionTypeDef = Union[RowFilterTypeDef, RowFilterOutputTypeDef]
DataLakeSettingsOutputTypeDef = TypedDict(
    "DataLakeSettingsOutputTypeDef",
    {
        "DataLakeAdmins": NotRequired[List[DataLakePrincipalTypeDef]],
        "ReadOnlyAdmins": NotRequired[List[DataLakePrincipalTypeDef]],
        "CreateDatabaseDefaultPermissions": NotRequired[List[PrincipalPermissionsOutputTypeDef]],
        "CreateTableDefaultPermissions": NotRequired[List[PrincipalPermissionsOutputTypeDef]],
        "Parameters": NotRequired[Dict[str, str]],
        "TrustedResourceOwners": NotRequired[List[str]],
        "AllowExternalDataFiltering": NotRequired[bool],
        "AllowFullTableExternalDataAccess": NotRequired[bool],
        "ExternalDataFilteringAllowList": NotRequired[List[DataLakePrincipalTypeDef]],
        "AuthorizedSessionTagValueList": NotRequired[List[str]],
    },
)
PrincipalPermissionsUnionTypeDef = Union[
    PrincipalPermissionsTypeDef, PrincipalPermissionsOutputTypeDef
]
GetResourceLFTagsResponseTypeDef = TypedDict(
    "GetResourceLFTagsResponseTypeDef",
    {
        "LFTagOnDatabase": List[LFTagPairOutputTypeDef],
        "LFTagsOnTable": List[LFTagPairOutputTypeDef],
        "LFTagsOnColumns": List[ColumnLFTagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TaggedTableTypeDef = TypedDict(
    "TaggedTableTypeDef",
    {
        "Table": NotRequired[TableResourceOutputTypeDef],
        "LFTagOnDatabase": NotRequired[List[LFTagPairOutputTypeDef]],
        "LFTagsOnTable": NotRequired[List[LFTagPairOutputTypeDef]],
        "LFTagsOnColumns": NotRequired[List[ColumnLFTagTypeDef]],
    },
)
AddLFTagsToResourceResponseTypeDef = TypedDict(
    "AddLFTagsToResourceResponseTypeDef",
    {
        "Failures": List[LFTagErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RemoveLFTagsFromResourceResponseTypeDef = TypedDict(
    "RemoveLFTagsFromResourceResponseTypeDef",
    {
        "Failures": List[LFTagErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TableWithColumnsResourceTypeDef = TypedDict(
    "TableWithColumnsResourceTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "CatalogId": NotRequired[str],
        "ColumnNames": NotRequired[Sequence[str]],
        "ColumnWildcard": NotRequired[ColumnWildcardUnionTypeDef],
    },
)
GetDataCellsFilterResponseTypeDef = TypedDict(
    "GetDataCellsFilterResponseTypeDef",
    {
        "DataCellsFilter": DataCellsFilterOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDataCellsFilterResponseTypeDef = TypedDict(
    "ListDataCellsFilterResponseTypeDef",
    {
        "DataCellsFilters": List[DataCellsFilterOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
SearchDatabasesByLFTagsResponseTypeDef = TypedDict(
    "SearchDatabasesByLFTagsResponseTypeDef",
    {
        "DatabaseList": List[TaggedDatabaseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateTableObjectsRequestRequestTypeDef = TypedDict(
    "UpdateTableObjectsRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "WriteOperations": Sequence[WriteOperationTypeDef],
        "CatalogId": NotRequired[str],
        "TransactionId": NotRequired[str],
    },
)
StartQueryPlanningRequestRequestTypeDef = TypedDict(
    "StartQueryPlanningRequestRequestTypeDef",
    {
        "QueryPlanningContext": QueryPlanningContextTypeDef,
        "QueryString": str,
    },
)
GetTemporaryGlueTableCredentialsRequestRequestTypeDef = TypedDict(
    "GetTemporaryGlueTableCredentialsRequestRequestTypeDef",
    {
        "TableArn": str,
        "Permissions": NotRequired[Sequence[PermissionType]],
        "DurationSeconds": NotRequired[int],
        "AuditContext": NotRequired[AuditContextTypeDef],
        "SupportedPermissionTypes": NotRequired[Sequence[PermissionTypeType]],
        "S3Path": NotRequired[str],
        "QuerySessionContext": NotRequired[QuerySessionContextTypeDef],
    },
)
ResourceOutputTypeDef = TypedDict(
    "ResourceOutputTypeDef",
    {
        "Catalog": NotRequired[Dict[str, Any]],
        "Database": NotRequired[DatabaseResourceTypeDef],
        "Table": NotRequired[TableResourceOutputTypeDef],
        "TableWithColumns": NotRequired[TableWithColumnsResourceOutputTypeDef],
        "DataLocation": NotRequired[DataLocationResourceTypeDef],
        "DataCellsFilter": NotRequired[DataCellsFilterResourceTypeDef],
        "LFTag": NotRequired[LFTagKeyResourceOutputTypeDef],
        "LFTagPolicy": NotRequired[LFTagPolicyResourceOutputTypeDef],
    },
)
LFTagPolicyResourceTypeDef = TypedDict(
    "LFTagPolicyResourceTypeDef",
    {
        "ResourceType": ResourceTypeType,
        "Expression": Sequence[LFTagUnionTypeDef],
        "CatalogId": NotRequired[str],
    },
)
SearchDatabasesByLFTagsRequestRequestTypeDef = TypedDict(
    "SearchDatabasesByLFTagsRequestRequestTypeDef",
    {
        "Expression": Sequence[LFTagUnionTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "CatalogId": NotRequired[str],
    },
)
GetTableObjectsResponseTypeDef = TypedDict(
    "GetTableObjectsResponseTypeDef",
    {
        "Objects": List[PartitionObjectsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DataCellsFilterTypeDef = TypedDict(
    "DataCellsFilterTypeDef",
    {
        "TableCatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "Name": str,
        "RowFilter": NotRequired[RowFilterUnionTypeDef],
        "ColumnNames": NotRequired[Sequence[str]],
        "ColumnWildcard": NotRequired[ColumnWildcardUnionTypeDef],
        "VersionId": NotRequired[str],
    },
)
GetDataLakeSettingsResponseTypeDef = TypedDict(
    "GetDataLakeSettingsResponseTypeDef",
    {
        "DataLakeSettings": DataLakeSettingsOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DataLakeSettingsTypeDef = TypedDict(
    "DataLakeSettingsTypeDef",
    {
        "DataLakeAdmins": NotRequired[Sequence[DataLakePrincipalTypeDef]],
        "ReadOnlyAdmins": NotRequired[Sequence[DataLakePrincipalTypeDef]],
        "CreateDatabaseDefaultPermissions": NotRequired[Sequence[PrincipalPermissionsUnionTypeDef]],
        "CreateTableDefaultPermissions": NotRequired[Sequence[PrincipalPermissionsTypeDef]],
        "Parameters": NotRequired[Mapping[str, str]],
        "TrustedResourceOwners": NotRequired[Sequence[str]],
        "AllowExternalDataFiltering": NotRequired[bool],
        "AllowFullTableExternalDataAccess": NotRequired[bool],
        "ExternalDataFilteringAllowList": NotRequired[Sequence[DataLakePrincipalTypeDef]],
        "AuthorizedSessionTagValueList": NotRequired[Sequence[str]],
    },
)
SearchTablesByLFTagsResponseTypeDef = TypedDict(
    "SearchTablesByLFTagsResponseTypeDef",
    {
        "TableList": List[TaggedTableTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
TableWithColumnsResourceUnionTypeDef = Union[
    TableWithColumnsResourceTypeDef, TableWithColumnsResourceOutputTypeDef
]
BatchPermissionsRequestEntryOutputTypeDef = TypedDict(
    "BatchPermissionsRequestEntryOutputTypeDef",
    {
        "Id": str,
        "Principal": NotRequired[DataLakePrincipalTypeDef],
        "Resource": NotRequired[ResourceOutputTypeDef],
        "Permissions": NotRequired[List[PermissionType]],
        "PermissionsWithGrantOption": NotRequired[List[PermissionType]],
    },
)
LakeFormationOptInsInfoTypeDef = TypedDict(
    "LakeFormationOptInsInfoTypeDef",
    {
        "Resource": NotRequired[ResourceOutputTypeDef],
        "Principal": NotRequired[DataLakePrincipalTypeDef],
        "LastModified": NotRequired[datetime],
        "LastUpdatedBy": NotRequired[str],
    },
)
PrincipalResourcePermissionsTypeDef = TypedDict(
    "PrincipalResourcePermissionsTypeDef",
    {
        "Principal": NotRequired[DataLakePrincipalTypeDef],
        "Resource": NotRequired[ResourceOutputTypeDef],
        "Permissions": NotRequired[List[PermissionType]],
        "PermissionsWithGrantOption": NotRequired[List[PermissionType]],
        "AdditionalDetails": NotRequired[DetailsMapTypeDef],
        "LastUpdated": NotRequired[datetime],
        "LastUpdatedBy": NotRequired[str],
    },
)
LFTagPolicyResourceUnionTypeDef = Union[
    LFTagPolicyResourceTypeDef, LFTagPolicyResourceOutputTypeDef
]
CreateDataCellsFilterRequestRequestTypeDef = TypedDict(
    "CreateDataCellsFilterRequestRequestTypeDef",
    {
        "TableData": DataCellsFilterTypeDef,
    },
)
UpdateDataCellsFilterRequestRequestTypeDef = TypedDict(
    "UpdateDataCellsFilterRequestRequestTypeDef",
    {
        "TableData": DataCellsFilterTypeDef,
    },
)
PutDataLakeSettingsRequestRequestTypeDef = TypedDict(
    "PutDataLakeSettingsRequestRequestTypeDef",
    {
        "DataLakeSettings": DataLakeSettingsTypeDef,
        "CatalogId": NotRequired[str],
    },
)
BatchPermissionsFailureEntryTypeDef = TypedDict(
    "BatchPermissionsFailureEntryTypeDef",
    {
        "RequestEntry": NotRequired[BatchPermissionsRequestEntryOutputTypeDef],
        "Error": NotRequired[ErrorDetailTypeDef],
    },
)
ListLakeFormationOptInsResponseTypeDef = TypedDict(
    "ListLakeFormationOptInsResponseTypeDef",
    {
        "LakeFormationOptInsInfoList": List[LakeFormationOptInsInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetEffectivePermissionsForPathResponseTypeDef = TypedDict(
    "GetEffectivePermissionsForPathResponseTypeDef",
    {
        "Permissions": List[PrincipalResourcePermissionsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListPermissionsResponseTypeDef = TypedDict(
    "ListPermissionsResponseTypeDef",
    {
        "PrincipalResourcePermissions": List[PrincipalResourcePermissionsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "Catalog": NotRequired[Mapping[str, Any]],
        "Database": NotRequired[DatabaseResourceTypeDef],
        "Table": NotRequired[TableResourceUnionTypeDef],
        "TableWithColumns": NotRequired[TableWithColumnsResourceUnionTypeDef],
        "DataLocation": NotRequired[DataLocationResourceTypeDef],
        "DataCellsFilter": NotRequired[DataCellsFilterResourceTypeDef],
        "LFTag": NotRequired[LFTagKeyResourceUnionTypeDef],
        "LFTagPolicy": NotRequired[LFTagPolicyResourceUnionTypeDef],
    },
)
BatchGrantPermissionsResponseTypeDef = TypedDict(
    "BatchGrantPermissionsResponseTypeDef",
    {
        "Failures": List[BatchPermissionsFailureEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchRevokePermissionsResponseTypeDef = TypedDict(
    "BatchRevokePermissionsResponseTypeDef",
    {
        "Failures": List[BatchPermissionsFailureEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AddLFTagsToResourceRequestRequestTypeDef = TypedDict(
    "AddLFTagsToResourceRequestRequestTypeDef",
    {
        "Resource": ResourceTypeDef,
        "LFTags": Sequence[LFTagPairUnionTypeDef],
        "CatalogId": NotRequired[str],
    },
)
CreateLakeFormationOptInRequestRequestTypeDef = TypedDict(
    "CreateLakeFormationOptInRequestRequestTypeDef",
    {
        "Principal": DataLakePrincipalTypeDef,
        "Resource": ResourceTypeDef,
    },
)
DeleteLakeFormationOptInRequestRequestTypeDef = TypedDict(
    "DeleteLakeFormationOptInRequestRequestTypeDef",
    {
        "Principal": DataLakePrincipalTypeDef,
        "Resource": ResourceTypeDef,
    },
)
GetResourceLFTagsRequestRequestTypeDef = TypedDict(
    "GetResourceLFTagsRequestRequestTypeDef",
    {
        "Resource": ResourceTypeDef,
        "CatalogId": NotRequired[str],
        "ShowAssignedLFTags": NotRequired[bool],
    },
)
GrantPermissionsRequestRequestTypeDef = TypedDict(
    "GrantPermissionsRequestRequestTypeDef",
    {
        "Principal": DataLakePrincipalTypeDef,
        "Resource": ResourceTypeDef,
        "Permissions": Sequence[PermissionType],
        "CatalogId": NotRequired[str],
        "PermissionsWithGrantOption": NotRequired[Sequence[PermissionType]],
    },
)
ListLakeFormationOptInsRequestRequestTypeDef = TypedDict(
    "ListLakeFormationOptInsRequestRequestTypeDef",
    {
        "Principal": NotRequired[DataLakePrincipalTypeDef],
        "Resource": NotRequired[ResourceTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListPermissionsRequestRequestTypeDef = TypedDict(
    "ListPermissionsRequestRequestTypeDef",
    {
        "CatalogId": NotRequired[str],
        "Principal": NotRequired[DataLakePrincipalTypeDef],
        "ResourceType": NotRequired[DataLakeResourceTypeType],
        "Resource": NotRequired[ResourceTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "IncludeRelated": NotRequired[str],
    },
)
RemoveLFTagsFromResourceRequestRequestTypeDef = TypedDict(
    "RemoveLFTagsFromResourceRequestRequestTypeDef",
    {
        "Resource": ResourceTypeDef,
        "LFTags": Sequence[LFTagPairTypeDef],
        "CatalogId": NotRequired[str],
    },
)
ResourceUnionTypeDef = Union[ResourceTypeDef, ResourceOutputTypeDef]
RevokePermissionsRequestRequestTypeDef = TypedDict(
    "RevokePermissionsRequestRequestTypeDef",
    {
        "Principal": DataLakePrincipalTypeDef,
        "Resource": ResourceTypeDef,
        "Permissions": Sequence[PermissionType],
        "CatalogId": NotRequired[str],
        "PermissionsWithGrantOption": NotRequired[Sequence[PermissionType]],
    },
)
BatchPermissionsRequestEntryTypeDef = TypedDict(
    "BatchPermissionsRequestEntryTypeDef",
    {
        "Id": str,
        "Principal": NotRequired[DataLakePrincipalTypeDef],
        "Resource": NotRequired[ResourceUnionTypeDef],
        "Permissions": NotRequired[Sequence[PermissionType]],
        "PermissionsWithGrantOption": NotRequired[Sequence[PermissionType]],
    },
)
BatchPermissionsRequestEntryUnionTypeDef = Union[
    BatchPermissionsRequestEntryTypeDef, BatchPermissionsRequestEntryOutputTypeDef
]
BatchRevokePermissionsRequestRequestTypeDef = TypedDict(
    "BatchRevokePermissionsRequestRequestTypeDef",
    {
        "Entries": Sequence[BatchPermissionsRequestEntryTypeDef],
        "CatalogId": NotRequired[str],
    },
)
BatchGrantPermissionsRequestRequestTypeDef = TypedDict(
    "BatchGrantPermissionsRequestRequestTypeDef",
    {
        "Entries": Sequence[BatchPermissionsRequestEntryUnionTypeDef],
        "CatalogId": NotRequired[str],
    },
)
