"""
Type annotations for timestream-write service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/type_defs/)

Usage::

    ```python
    from mypy_boto3_timestream_write.type_defs import BatchLoadProgressReportTypeDef

    data: BatchLoadProgressReportTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    BatchLoadStatusType,
    MeasureValueTypeType,
    PartitionKeyEnforcementLevelType,
    PartitionKeyTypeType,
    S3EncryptionOptionType,
    ScalarMeasureValueTypeType,
    TableStatusType,
    TimeUnitType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "BatchLoadProgressReportTypeDef",
    "BatchLoadTaskTypeDef",
    "ResponseMetadataTypeDef",
    "TagTypeDef",
    "DatabaseTypeDef",
    "RetentionPropertiesTypeDef",
    "CsvConfigurationTypeDef",
    "DataModelS3ConfigurationTypeDef",
    "DimensionMappingTypeDef",
    "DataSourceS3ConfigurationTypeDef",
    "DeleteDatabaseRequestRequestTypeDef",
    "DeleteTableRequestRequestTypeDef",
    "DescribeBatchLoadTaskRequestRequestTypeDef",
    "DescribeDatabaseRequestRequestTypeDef",
    "EndpointTypeDef",
    "DescribeTableRequestRequestTypeDef",
    "DimensionTypeDef",
    "ListBatchLoadTasksRequestRequestTypeDef",
    "ListDatabasesRequestRequestTypeDef",
    "ListTablesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "S3ConfigurationTypeDef",
    "MeasureValueTypeDef",
    "MultiMeasureAttributeMappingTypeDef",
    "PartitionKeyTypeDef",
    "RecordsIngestedTypeDef",
    "ReportS3ConfigurationTypeDef",
    "ResumeBatchLoadTaskRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDatabaseRequestRequestTypeDef",
    "CreateBatchLoadTaskResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ListBatchLoadTasksResponseTypeDef",
    "CreateDatabaseRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateDatabaseResponseTypeDef",
    "DescribeDatabaseResponseTypeDef",
    "ListDatabasesResponseTypeDef",
    "UpdateDatabaseResponseTypeDef",
    "DataSourceConfigurationTypeDef",
    "DescribeEndpointsResponseTypeDef",
    "MagneticStoreRejectedDataLocationTypeDef",
    "RecordTypeDef",
    "MixedMeasureMappingOutputTypeDef",
    "MixedMeasureMappingTypeDef",
    "MultiMeasureMappingsOutputTypeDef",
    "MultiMeasureMappingsTypeDef",
    "SchemaOutputTypeDef",
    "SchemaTypeDef",
    "WriteRecordsResponseTypeDef",
    "ReportConfigurationTypeDef",
    "MagneticStoreWritePropertiesTypeDef",
    "WriteRecordsRequestRequestTypeDef",
    "MixedMeasureMappingUnionTypeDef",
    "DataModelOutputTypeDef",
    "MultiMeasureMappingsUnionTypeDef",
    "CreateTableRequestRequestTypeDef",
    "TableTypeDef",
    "UpdateTableRequestRequestTypeDef",
    "DataModelConfigurationOutputTypeDef",
    "DataModelTypeDef",
    "CreateTableResponseTypeDef",
    "DescribeTableResponseTypeDef",
    "ListTablesResponseTypeDef",
    "UpdateTableResponseTypeDef",
    "BatchLoadTaskDescriptionTypeDef",
    "DataModelUnionTypeDef",
    "DescribeBatchLoadTaskResponseTypeDef",
    "DataModelConfigurationTypeDef",
    "CreateBatchLoadTaskRequestRequestTypeDef",
)

BatchLoadProgressReportTypeDef = TypedDict(
    "BatchLoadProgressReportTypeDef",
    {
        "RecordsProcessed": NotRequired[int],
        "RecordsIngested": NotRequired[int],
        "ParseFailures": NotRequired[int],
        "RecordIngestionFailures": NotRequired[int],
        "FileFailures": NotRequired[int],
        "BytesMetered": NotRequired[int],
    },
)
BatchLoadTaskTypeDef = TypedDict(
    "BatchLoadTaskTypeDef",
    {
        "TaskId": NotRequired[str],
        "TaskStatus": NotRequired[BatchLoadStatusType],
        "DatabaseName": NotRequired[str],
        "TableName": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "ResumableUntil": NotRequired[datetime],
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
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
DatabaseTypeDef = TypedDict(
    "DatabaseTypeDef",
    {
        "Arn": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "TableCount": NotRequired[int],
        "KmsKeyId": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
    },
)
RetentionPropertiesTypeDef = TypedDict(
    "RetentionPropertiesTypeDef",
    {
        "MemoryStoreRetentionPeriodInHours": int,
        "MagneticStoreRetentionPeriodInDays": int,
    },
)
CsvConfigurationTypeDef = TypedDict(
    "CsvConfigurationTypeDef",
    {
        "ColumnSeparator": NotRequired[str],
        "EscapeChar": NotRequired[str],
        "QuoteChar": NotRequired[str],
        "NullValue": NotRequired[str],
        "TrimWhiteSpace": NotRequired[bool],
    },
)
DataModelS3ConfigurationTypeDef = TypedDict(
    "DataModelS3ConfigurationTypeDef",
    {
        "BucketName": NotRequired[str],
        "ObjectKey": NotRequired[str],
    },
)
DimensionMappingTypeDef = TypedDict(
    "DimensionMappingTypeDef",
    {
        "SourceColumn": NotRequired[str],
        "DestinationColumn": NotRequired[str],
    },
)
DataSourceS3ConfigurationTypeDef = TypedDict(
    "DataSourceS3ConfigurationTypeDef",
    {
        "BucketName": str,
        "ObjectKeyPrefix": NotRequired[str],
    },
)
DeleteDatabaseRequestRequestTypeDef = TypedDict(
    "DeleteDatabaseRequestRequestTypeDef",
    {
        "DatabaseName": str,
    },
)
DeleteTableRequestRequestTypeDef = TypedDict(
    "DeleteTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)
DescribeBatchLoadTaskRequestRequestTypeDef = TypedDict(
    "DescribeBatchLoadTaskRequestRequestTypeDef",
    {
        "TaskId": str,
    },
)
DescribeDatabaseRequestRequestTypeDef = TypedDict(
    "DescribeDatabaseRequestRequestTypeDef",
    {
        "DatabaseName": str,
    },
)
EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": str,
        "CachePeriodInMinutes": int,
    },
)
DescribeTableRequestRequestTypeDef = TypedDict(
    "DescribeTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)
DimensionTypeDef = TypedDict(
    "DimensionTypeDef",
    {
        "Name": str,
        "Value": str,
        "DimensionValueType": NotRequired[Literal["VARCHAR"]],
    },
)
ListBatchLoadTasksRequestRequestTypeDef = TypedDict(
    "ListBatchLoadTasksRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "TaskStatus": NotRequired[BatchLoadStatusType],
    },
)
ListDatabasesRequestRequestTypeDef = TypedDict(
    "ListDatabasesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListTablesRequestRequestTypeDef = TypedDict(
    "ListTablesRequestRequestTypeDef",
    {
        "DatabaseName": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
S3ConfigurationTypeDef = TypedDict(
    "S3ConfigurationTypeDef",
    {
        "BucketName": NotRequired[str],
        "ObjectKeyPrefix": NotRequired[str],
        "EncryptionOption": NotRequired[S3EncryptionOptionType],
        "KmsKeyId": NotRequired[str],
    },
)
MeasureValueTypeDef = TypedDict(
    "MeasureValueTypeDef",
    {
        "Name": str,
        "Value": str,
        "Type": MeasureValueTypeType,
    },
)
MultiMeasureAttributeMappingTypeDef = TypedDict(
    "MultiMeasureAttributeMappingTypeDef",
    {
        "SourceColumn": str,
        "TargetMultiMeasureAttributeName": NotRequired[str],
        "MeasureValueType": NotRequired[ScalarMeasureValueTypeType],
    },
)
PartitionKeyTypeDef = TypedDict(
    "PartitionKeyTypeDef",
    {
        "Type": PartitionKeyTypeType,
        "Name": NotRequired[str],
        "EnforcementInRecord": NotRequired[PartitionKeyEnforcementLevelType],
    },
)
RecordsIngestedTypeDef = TypedDict(
    "RecordsIngestedTypeDef",
    {
        "Total": NotRequired[int],
        "MemoryStore": NotRequired[int],
        "MagneticStore": NotRequired[int],
    },
)
ReportS3ConfigurationTypeDef = TypedDict(
    "ReportS3ConfigurationTypeDef",
    {
        "BucketName": str,
        "ObjectKeyPrefix": NotRequired[str],
        "EncryptionOption": NotRequired[S3EncryptionOptionType],
        "KmsKeyId": NotRequired[str],
    },
)
ResumeBatchLoadTaskRequestRequestTypeDef = TypedDict(
    "ResumeBatchLoadTaskRequestRequestTypeDef",
    {
        "TaskId": str,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
UpdateDatabaseRequestRequestTypeDef = TypedDict(
    "UpdateDatabaseRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "KmsKeyId": str,
    },
)
CreateBatchLoadTaskResponseTypeDef = TypedDict(
    "CreateBatchLoadTaskResponseTypeDef",
    {
        "TaskId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListBatchLoadTasksResponseTypeDef = TypedDict(
    "ListBatchLoadTasksResponseTypeDef",
    {
        "BatchLoadTasks": List[BatchLoadTaskTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateDatabaseRequestRequestTypeDef = TypedDict(
    "CreateDatabaseRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "KmsKeyId": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
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
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CreateDatabaseResponseTypeDef = TypedDict(
    "CreateDatabaseResponseTypeDef",
    {
        "Database": DatabaseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDatabaseResponseTypeDef = TypedDict(
    "DescribeDatabaseResponseTypeDef",
    {
        "Database": DatabaseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDatabasesResponseTypeDef = TypedDict(
    "ListDatabasesResponseTypeDef",
    {
        "Databases": List[DatabaseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateDatabaseResponseTypeDef = TypedDict(
    "UpdateDatabaseResponseTypeDef",
    {
        "Database": DatabaseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DataSourceConfigurationTypeDef = TypedDict(
    "DataSourceConfigurationTypeDef",
    {
        "DataSourceS3Configuration": DataSourceS3ConfigurationTypeDef,
        "DataFormat": Literal["CSV"],
        "CsvConfiguration": NotRequired[CsvConfigurationTypeDef],
    },
)
DescribeEndpointsResponseTypeDef = TypedDict(
    "DescribeEndpointsResponseTypeDef",
    {
        "Endpoints": List[EndpointTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MagneticStoreRejectedDataLocationTypeDef = TypedDict(
    "MagneticStoreRejectedDataLocationTypeDef",
    {
        "S3Configuration": NotRequired[S3ConfigurationTypeDef],
    },
)
RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "Dimensions": NotRequired[Sequence[DimensionTypeDef]],
        "MeasureName": NotRequired[str],
        "MeasureValue": NotRequired[str],
        "MeasureValueType": NotRequired[MeasureValueTypeType],
        "Time": NotRequired[str],
        "TimeUnit": NotRequired[TimeUnitType],
        "Version": NotRequired[int],
        "MeasureValues": NotRequired[Sequence[MeasureValueTypeDef]],
    },
)
MixedMeasureMappingOutputTypeDef = TypedDict(
    "MixedMeasureMappingOutputTypeDef",
    {
        "MeasureValueType": MeasureValueTypeType,
        "MeasureName": NotRequired[str],
        "SourceColumn": NotRequired[str],
        "TargetMeasureName": NotRequired[str],
        "MultiMeasureAttributeMappings": NotRequired[List[MultiMeasureAttributeMappingTypeDef]],
    },
)
MixedMeasureMappingTypeDef = TypedDict(
    "MixedMeasureMappingTypeDef",
    {
        "MeasureValueType": MeasureValueTypeType,
        "MeasureName": NotRequired[str],
        "SourceColumn": NotRequired[str],
        "TargetMeasureName": NotRequired[str],
        "MultiMeasureAttributeMappings": NotRequired[Sequence[MultiMeasureAttributeMappingTypeDef]],
    },
)
MultiMeasureMappingsOutputTypeDef = TypedDict(
    "MultiMeasureMappingsOutputTypeDef",
    {
        "MultiMeasureAttributeMappings": List[MultiMeasureAttributeMappingTypeDef],
        "TargetMultiMeasureName": NotRequired[str],
    },
)
MultiMeasureMappingsTypeDef = TypedDict(
    "MultiMeasureMappingsTypeDef",
    {
        "MultiMeasureAttributeMappings": Sequence[MultiMeasureAttributeMappingTypeDef],
        "TargetMultiMeasureName": NotRequired[str],
    },
)
SchemaOutputTypeDef = TypedDict(
    "SchemaOutputTypeDef",
    {
        "CompositePartitionKey": NotRequired[List[PartitionKeyTypeDef]],
    },
)
SchemaTypeDef = TypedDict(
    "SchemaTypeDef",
    {
        "CompositePartitionKey": NotRequired[Sequence[PartitionKeyTypeDef]],
    },
)
WriteRecordsResponseTypeDef = TypedDict(
    "WriteRecordsResponseTypeDef",
    {
        "RecordsIngested": RecordsIngestedTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReportConfigurationTypeDef = TypedDict(
    "ReportConfigurationTypeDef",
    {
        "ReportS3Configuration": NotRequired[ReportS3ConfigurationTypeDef],
    },
)
MagneticStoreWritePropertiesTypeDef = TypedDict(
    "MagneticStoreWritePropertiesTypeDef",
    {
        "EnableMagneticStoreWrites": bool,
        "MagneticStoreRejectedDataLocation": NotRequired[MagneticStoreRejectedDataLocationTypeDef],
    },
)
WriteRecordsRequestRequestTypeDef = TypedDict(
    "WriteRecordsRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "Records": Sequence[RecordTypeDef],
        "CommonAttributes": NotRequired[RecordTypeDef],
    },
)
MixedMeasureMappingUnionTypeDef = Union[
    MixedMeasureMappingTypeDef, MixedMeasureMappingOutputTypeDef
]
DataModelOutputTypeDef = TypedDict(
    "DataModelOutputTypeDef",
    {
        "DimensionMappings": List[DimensionMappingTypeDef],
        "TimeColumn": NotRequired[str],
        "TimeUnit": NotRequired[TimeUnitType],
        "MultiMeasureMappings": NotRequired[MultiMeasureMappingsOutputTypeDef],
        "MixedMeasureMappings": NotRequired[List[MixedMeasureMappingOutputTypeDef]],
        "MeasureNameColumn": NotRequired[str],
    },
)
MultiMeasureMappingsUnionTypeDef = Union[
    MultiMeasureMappingsTypeDef, MultiMeasureMappingsOutputTypeDef
]
CreateTableRequestRequestTypeDef = TypedDict(
    "CreateTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "RetentionProperties": NotRequired[RetentionPropertiesTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "MagneticStoreWriteProperties": NotRequired[MagneticStoreWritePropertiesTypeDef],
        "Schema": NotRequired[SchemaTypeDef],
    },
)
TableTypeDef = TypedDict(
    "TableTypeDef",
    {
        "Arn": NotRequired[str],
        "TableName": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "TableStatus": NotRequired[TableStatusType],
        "RetentionProperties": NotRequired[RetentionPropertiesTypeDef],
        "CreationTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "MagneticStoreWriteProperties": NotRequired[MagneticStoreWritePropertiesTypeDef],
        "Schema": NotRequired[SchemaOutputTypeDef],
    },
)
UpdateTableRequestRequestTypeDef = TypedDict(
    "UpdateTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "RetentionProperties": NotRequired[RetentionPropertiesTypeDef],
        "MagneticStoreWriteProperties": NotRequired[MagneticStoreWritePropertiesTypeDef],
        "Schema": NotRequired[SchemaTypeDef],
    },
)
DataModelConfigurationOutputTypeDef = TypedDict(
    "DataModelConfigurationOutputTypeDef",
    {
        "DataModel": NotRequired[DataModelOutputTypeDef],
        "DataModelS3Configuration": NotRequired[DataModelS3ConfigurationTypeDef],
    },
)
DataModelTypeDef = TypedDict(
    "DataModelTypeDef",
    {
        "DimensionMappings": Sequence[DimensionMappingTypeDef],
        "TimeColumn": NotRequired[str],
        "TimeUnit": NotRequired[TimeUnitType],
        "MultiMeasureMappings": NotRequired[MultiMeasureMappingsUnionTypeDef],
        "MixedMeasureMappings": NotRequired[Sequence[MixedMeasureMappingUnionTypeDef]],
        "MeasureNameColumn": NotRequired[str],
    },
)
CreateTableResponseTypeDef = TypedDict(
    "CreateTableResponseTypeDef",
    {
        "Table": TableTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTableResponseTypeDef = TypedDict(
    "DescribeTableResponseTypeDef",
    {
        "Table": TableTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
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
UpdateTableResponseTypeDef = TypedDict(
    "UpdateTableResponseTypeDef",
    {
        "Table": TableTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchLoadTaskDescriptionTypeDef = TypedDict(
    "BatchLoadTaskDescriptionTypeDef",
    {
        "TaskId": NotRequired[str],
        "ErrorMessage": NotRequired[str],
        "DataSourceConfiguration": NotRequired[DataSourceConfigurationTypeDef],
        "ProgressReport": NotRequired[BatchLoadProgressReportTypeDef],
        "ReportConfiguration": NotRequired[ReportConfigurationTypeDef],
        "DataModelConfiguration": NotRequired[DataModelConfigurationOutputTypeDef],
        "TargetDatabaseName": NotRequired[str],
        "TargetTableName": NotRequired[str],
        "TaskStatus": NotRequired[BatchLoadStatusType],
        "RecordVersion": NotRequired[int],
        "CreationTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "ResumableUntil": NotRequired[datetime],
    },
)
DataModelUnionTypeDef = Union[DataModelTypeDef, DataModelOutputTypeDef]
DescribeBatchLoadTaskResponseTypeDef = TypedDict(
    "DescribeBatchLoadTaskResponseTypeDef",
    {
        "BatchLoadTaskDescription": BatchLoadTaskDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DataModelConfigurationTypeDef = TypedDict(
    "DataModelConfigurationTypeDef",
    {
        "DataModel": NotRequired[DataModelUnionTypeDef],
        "DataModelS3Configuration": NotRequired[DataModelS3ConfigurationTypeDef],
    },
)
CreateBatchLoadTaskRequestRequestTypeDef = TypedDict(
    "CreateBatchLoadTaskRequestRequestTypeDef",
    {
        "DataSourceConfiguration": DataSourceConfigurationTypeDef,
        "ReportConfiguration": ReportConfigurationTypeDef,
        "TargetDatabaseName": str,
        "TargetTableName": str,
        "ClientToken": NotRequired[str],
        "DataModelConfiguration": NotRequired[DataModelConfigurationTypeDef],
        "RecordVersion": NotRequired[int],
    },
)
