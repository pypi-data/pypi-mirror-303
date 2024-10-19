"""
Type annotations for iotanalytics service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/type_defs/)

Usage::

    ```python
    from mypy_boto3_iotanalytics.type_defs import AddAttributesActivityOutputTypeDef

    data: AddAttributesActivityOutputTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    ChannelStatusType,
    ComputeTypeType,
    DatasetActionTypeType,
    DatasetContentStateType,
    DatasetStatusType,
    DatastoreStatusType,
    FileFormatTypeType,
    ReprocessingStatusType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AddAttributesActivityOutputTypeDef",
    "AddAttributesActivityTypeDef",
    "BatchPutMessageErrorEntryTypeDef",
    "ResponseMetadataTypeDef",
    "BlobTypeDef",
    "CancelPipelineReprocessingRequestRequestTypeDef",
    "ChannelActivityTypeDef",
    "ChannelMessagesTypeDef",
    "EstimatedResourceSizeTypeDef",
    "CustomerManagedChannelS3StorageTypeDef",
    "CustomerManagedChannelS3StorageSummaryTypeDef",
    "RetentionPeriodTypeDef",
    "ColumnTypeDef",
    "ResourceConfigurationTypeDef",
    "TagTypeDef",
    "CreateDatasetContentRequestRequestTypeDef",
    "VersioningConfigurationTypeDef",
    "CustomerManagedDatastoreS3StorageSummaryTypeDef",
    "CustomerManagedDatastoreS3StorageTypeDef",
    "DatasetActionSummaryTypeDef",
    "IotEventsDestinationConfigurationTypeDef",
    "DatasetContentStatusTypeDef",
    "DatasetContentVersionValueTypeDef",
    "DatasetEntryTypeDef",
    "ScheduleTypeDef",
    "TriggeringDatasetTypeDef",
    "DatastoreActivityTypeDef",
    "IotSiteWiseCustomerManagedDatastoreS3StorageSummaryTypeDef",
    "IotSiteWiseCustomerManagedDatastoreS3StorageTypeDef",
    "PartitionTypeDef",
    "TimestampPartitionTypeDef",
    "DeleteChannelRequestRequestTypeDef",
    "DeleteDatasetContentRequestRequestTypeDef",
    "DeleteDatasetRequestRequestTypeDef",
    "DeleteDatastoreRequestRequestTypeDef",
    "DeletePipelineRequestRequestTypeDef",
    "DeltaTimeSessionWindowConfigurationTypeDef",
    "DeltaTimeTypeDef",
    "DescribeChannelRequestRequestTypeDef",
    "DescribeDatasetRequestRequestTypeDef",
    "DescribeDatastoreRequestRequestTypeDef",
    "LoggingOptionsTypeDef",
    "DescribePipelineRequestRequestTypeDef",
    "DeviceRegistryEnrichActivityTypeDef",
    "DeviceShadowEnrichActivityTypeDef",
    "FilterActivityTypeDef",
    "GetDatasetContentRequestRequestTypeDef",
    "GlueConfigurationTypeDef",
    "LambdaActivityTypeDef",
    "PaginatorConfigTypeDef",
    "ListChannelsRequestRequestTypeDef",
    "TimestampTypeDef",
    "ListDatasetsRequestRequestTypeDef",
    "ListDatastoresRequestRequestTypeDef",
    "ListPipelinesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "MathActivityTypeDef",
    "OutputFileUriValueTypeDef",
    "RemoveAttributesActivityOutputTypeDef",
    "SelectAttributesActivityOutputTypeDef",
    "ReprocessingSummaryTypeDef",
    "RemoveAttributesActivityTypeDef",
    "SelectAttributesActivityTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "AddAttributesActivityUnionTypeDef",
    "BatchPutMessageResponseTypeDef",
    "CreateDatasetContentResponseTypeDef",
    "CreatePipelineResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "RunPipelineActivityResponseTypeDef",
    "SampleChannelDataResponseTypeDef",
    "StartPipelineReprocessingResponseTypeDef",
    "MessageTypeDef",
    "ChannelStatisticsTypeDef",
    "DatastoreStatisticsTypeDef",
    "ChannelStorageOutputTypeDef",
    "ChannelStorageTypeDef",
    "ChannelStorageSummaryTypeDef",
    "CreateChannelResponseTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateDatastoreResponseTypeDef",
    "SchemaDefinitionOutputTypeDef",
    "SchemaDefinitionTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "DatasetContentSummaryTypeDef",
    "GetDatasetContentResponseTypeDef",
    "DatasetTriggerTypeDef",
    "DatastoreIotSiteWiseMultiLayerStorageSummaryTypeDef",
    "DatastoreIotSiteWiseMultiLayerStorageTypeDef",
    "DatastorePartitionTypeDef",
    "LateDataRuleConfigurationTypeDef",
    "QueryFilterTypeDef",
    "DescribeLoggingOptionsResponseTypeDef",
    "PutLoggingOptionsRequestRequestTypeDef",
    "S3DestinationConfigurationTypeDef",
    "ListChannelsRequestListChannelsPaginateTypeDef",
    "ListDatasetsRequestListDatasetsPaginateTypeDef",
    "ListDatastoresRequestListDatastoresPaginateTypeDef",
    "ListPipelinesRequestListPipelinesPaginateTypeDef",
    "ListDatasetContentsRequestListDatasetContentsPaginateTypeDef",
    "ListDatasetContentsRequestRequestTypeDef",
    "SampleChannelDataRequestRequestTypeDef",
    "StartPipelineReprocessingRequestRequestTypeDef",
    "VariableTypeDef",
    "PipelineActivityOutputTypeDef",
    "PipelineSummaryTypeDef",
    "RemoveAttributesActivityUnionTypeDef",
    "SelectAttributesActivityUnionTypeDef",
    "BatchPutMessageRequestRequestTypeDef",
    "ChannelTypeDef",
    "CreateChannelRequestRequestTypeDef",
    "UpdateChannelRequestRequestTypeDef",
    "ChannelSummaryTypeDef",
    "ParquetConfigurationOutputTypeDef",
    "SchemaDefinitionUnionTypeDef",
    "ListDatasetContentsResponseTypeDef",
    "DatasetSummaryTypeDef",
    "DatastoreStorageSummaryTypeDef",
    "DatastoreStorageOutputTypeDef",
    "DatastoreStorageTypeDef",
    "DatastorePartitionsOutputTypeDef",
    "DatastorePartitionsTypeDef",
    "LateDataRuleTypeDef",
    "SqlQueryDatasetActionOutputTypeDef",
    "SqlQueryDatasetActionTypeDef",
    "DatasetContentDeliveryDestinationTypeDef",
    "ContainerDatasetActionOutputTypeDef",
    "ContainerDatasetActionTypeDef",
    "PipelineTypeDef",
    "ListPipelinesResponseTypeDef",
    "PipelineActivityTypeDef",
    "DescribeChannelResponseTypeDef",
    "ListChannelsResponseTypeDef",
    "FileFormatConfigurationOutputTypeDef",
    "ParquetConfigurationTypeDef",
    "ListDatasetsResponseTypeDef",
    "DatastoreSummaryTypeDef",
    "SqlQueryDatasetActionUnionTypeDef",
    "DatasetContentDeliveryRuleTypeDef",
    "DatasetActionOutputTypeDef",
    "ContainerDatasetActionUnionTypeDef",
    "DescribePipelineResponseTypeDef",
    "PipelineActivityUnionTypeDef",
    "RunPipelineActivityRequestRequestTypeDef",
    "UpdatePipelineRequestRequestTypeDef",
    "DatastoreTypeDef",
    "ParquetConfigurationUnionTypeDef",
    "ListDatastoresResponseTypeDef",
    "DatasetTypeDef",
    "DatasetActionTypeDef",
    "CreatePipelineRequestRequestTypeDef",
    "DescribeDatastoreResponseTypeDef",
    "FileFormatConfigurationTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DatasetActionUnionTypeDef",
    "UpdateDatasetRequestRequestTypeDef",
    "CreateDatastoreRequestRequestTypeDef",
    "UpdateDatastoreRequestRequestTypeDef",
    "CreateDatasetRequestRequestTypeDef",
)

AddAttributesActivityOutputTypeDef = TypedDict(
    "AddAttributesActivityOutputTypeDef",
    {
        "name": str,
        "attributes": Dict[str, str],
        "next": NotRequired[str],
    },
)
AddAttributesActivityTypeDef = TypedDict(
    "AddAttributesActivityTypeDef",
    {
        "name": str,
        "attributes": Mapping[str, str],
        "next": NotRequired[str],
    },
)
BatchPutMessageErrorEntryTypeDef = TypedDict(
    "BatchPutMessageErrorEntryTypeDef",
    {
        "messageId": NotRequired[str],
        "errorCode": NotRequired[str],
        "errorMessage": NotRequired[str],
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
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
CancelPipelineReprocessingRequestRequestTypeDef = TypedDict(
    "CancelPipelineReprocessingRequestRequestTypeDef",
    {
        "pipelineName": str,
        "reprocessingId": str,
    },
)
ChannelActivityTypeDef = TypedDict(
    "ChannelActivityTypeDef",
    {
        "name": str,
        "channelName": str,
        "next": NotRequired[str],
    },
)
ChannelMessagesTypeDef = TypedDict(
    "ChannelMessagesTypeDef",
    {
        "s3Paths": NotRequired[Sequence[str]],
    },
)
EstimatedResourceSizeTypeDef = TypedDict(
    "EstimatedResourceSizeTypeDef",
    {
        "estimatedSizeInBytes": NotRequired[float],
        "estimatedOn": NotRequired[datetime],
    },
)
CustomerManagedChannelS3StorageTypeDef = TypedDict(
    "CustomerManagedChannelS3StorageTypeDef",
    {
        "bucket": str,
        "roleArn": str,
        "keyPrefix": NotRequired[str],
    },
)
CustomerManagedChannelS3StorageSummaryTypeDef = TypedDict(
    "CustomerManagedChannelS3StorageSummaryTypeDef",
    {
        "bucket": NotRequired[str],
        "keyPrefix": NotRequired[str],
        "roleArn": NotRequired[str],
    },
)
RetentionPeriodTypeDef = TypedDict(
    "RetentionPeriodTypeDef",
    {
        "unlimited": NotRequired[bool],
        "numberOfDays": NotRequired[int],
    },
)
ColumnTypeDef = TypedDict(
    "ColumnTypeDef",
    {
        "name": str,
        "type": str,
    },
)
ResourceConfigurationTypeDef = TypedDict(
    "ResourceConfigurationTypeDef",
    {
        "computeType": ComputeTypeType,
        "volumeSizeInGB": int,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)
CreateDatasetContentRequestRequestTypeDef = TypedDict(
    "CreateDatasetContentRequestRequestTypeDef",
    {
        "datasetName": str,
        "versionId": NotRequired[str],
    },
)
VersioningConfigurationTypeDef = TypedDict(
    "VersioningConfigurationTypeDef",
    {
        "unlimited": NotRequired[bool],
        "maxVersions": NotRequired[int],
    },
)
CustomerManagedDatastoreS3StorageSummaryTypeDef = TypedDict(
    "CustomerManagedDatastoreS3StorageSummaryTypeDef",
    {
        "bucket": NotRequired[str],
        "keyPrefix": NotRequired[str],
        "roleArn": NotRequired[str],
    },
)
CustomerManagedDatastoreS3StorageTypeDef = TypedDict(
    "CustomerManagedDatastoreS3StorageTypeDef",
    {
        "bucket": str,
        "roleArn": str,
        "keyPrefix": NotRequired[str],
    },
)
DatasetActionSummaryTypeDef = TypedDict(
    "DatasetActionSummaryTypeDef",
    {
        "actionName": NotRequired[str],
        "actionType": NotRequired[DatasetActionTypeType],
    },
)
IotEventsDestinationConfigurationTypeDef = TypedDict(
    "IotEventsDestinationConfigurationTypeDef",
    {
        "inputName": str,
        "roleArn": str,
    },
)
DatasetContentStatusTypeDef = TypedDict(
    "DatasetContentStatusTypeDef",
    {
        "state": NotRequired[DatasetContentStateType],
        "reason": NotRequired[str],
    },
)
DatasetContentVersionValueTypeDef = TypedDict(
    "DatasetContentVersionValueTypeDef",
    {
        "datasetName": str,
    },
)
DatasetEntryTypeDef = TypedDict(
    "DatasetEntryTypeDef",
    {
        "entryName": NotRequired[str],
        "dataURI": NotRequired[str],
    },
)
ScheduleTypeDef = TypedDict(
    "ScheduleTypeDef",
    {
        "expression": NotRequired[str],
    },
)
TriggeringDatasetTypeDef = TypedDict(
    "TriggeringDatasetTypeDef",
    {
        "name": str,
    },
)
DatastoreActivityTypeDef = TypedDict(
    "DatastoreActivityTypeDef",
    {
        "name": str,
        "datastoreName": str,
    },
)
IotSiteWiseCustomerManagedDatastoreS3StorageSummaryTypeDef = TypedDict(
    "IotSiteWiseCustomerManagedDatastoreS3StorageSummaryTypeDef",
    {
        "bucket": NotRequired[str],
        "keyPrefix": NotRequired[str],
    },
)
IotSiteWiseCustomerManagedDatastoreS3StorageTypeDef = TypedDict(
    "IotSiteWiseCustomerManagedDatastoreS3StorageTypeDef",
    {
        "bucket": str,
        "keyPrefix": NotRequired[str],
    },
)
PartitionTypeDef = TypedDict(
    "PartitionTypeDef",
    {
        "attributeName": str,
    },
)
TimestampPartitionTypeDef = TypedDict(
    "TimestampPartitionTypeDef",
    {
        "attributeName": str,
        "timestampFormat": NotRequired[str],
    },
)
DeleteChannelRequestRequestTypeDef = TypedDict(
    "DeleteChannelRequestRequestTypeDef",
    {
        "channelName": str,
    },
)
DeleteDatasetContentRequestRequestTypeDef = TypedDict(
    "DeleteDatasetContentRequestRequestTypeDef",
    {
        "datasetName": str,
        "versionId": NotRequired[str],
    },
)
DeleteDatasetRequestRequestTypeDef = TypedDict(
    "DeleteDatasetRequestRequestTypeDef",
    {
        "datasetName": str,
    },
)
DeleteDatastoreRequestRequestTypeDef = TypedDict(
    "DeleteDatastoreRequestRequestTypeDef",
    {
        "datastoreName": str,
    },
)
DeletePipelineRequestRequestTypeDef = TypedDict(
    "DeletePipelineRequestRequestTypeDef",
    {
        "pipelineName": str,
    },
)
DeltaTimeSessionWindowConfigurationTypeDef = TypedDict(
    "DeltaTimeSessionWindowConfigurationTypeDef",
    {
        "timeoutInMinutes": int,
    },
)
DeltaTimeTypeDef = TypedDict(
    "DeltaTimeTypeDef",
    {
        "offsetSeconds": int,
        "timeExpression": str,
    },
)
DescribeChannelRequestRequestTypeDef = TypedDict(
    "DescribeChannelRequestRequestTypeDef",
    {
        "channelName": str,
        "includeStatistics": NotRequired[bool],
    },
)
DescribeDatasetRequestRequestTypeDef = TypedDict(
    "DescribeDatasetRequestRequestTypeDef",
    {
        "datasetName": str,
    },
)
DescribeDatastoreRequestRequestTypeDef = TypedDict(
    "DescribeDatastoreRequestRequestTypeDef",
    {
        "datastoreName": str,
        "includeStatistics": NotRequired[bool],
    },
)
LoggingOptionsTypeDef = TypedDict(
    "LoggingOptionsTypeDef",
    {
        "roleArn": str,
        "level": Literal["ERROR"],
        "enabled": bool,
    },
)
DescribePipelineRequestRequestTypeDef = TypedDict(
    "DescribePipelineRequestRequestTypeDef",
    {
        "pipelineName": str,
    },
)
DeviceRegistryEnrichActivityTypeDef = TypedDict(
    "DeviceRegistryEnrichActivityTypeDef",
    {
        "name": str,
        "attribute": str,
        "thingName": str,
        "roleArn": str,
        "next": NotRequired[str],
    },
)
DeviceShadowEnrichActivityTypeDef = TypedDict(
    "DeviceShadowEnrichActivityTypeDef",
    {
        "name": str,
        "attribute": str,
        "thingName": str,
        "roleArn": str,
        "next": NotRequired[str],
    },
)
FilterActivityTypeDef = TypedDict(
    "FilterActivityTypeDef",
    {
        "name": str,
        "filter": str,
        "next": NotRequired[str],
    },
)
GetDatasetContentRequestRequestTypeDef = TypedDict(
    "GetDatasetContentRequestRequestTypeDef",
    {
        "datasetName": str,
        "versionId": NotRequired[str],
    },
)
GlueConfigurationTypeDef = TypedDict(
    "GlueConfigurationTypeDef",
    {
        "tableName": str,
        "databaseName": str,
    },
)
LambdaActivityTypeDef = TypedDict(
    "LambdaActivityTypeDef",
    {
        "name": str,
        "lambdaName": str,
        "batchSize": int,
        "next": NotRequired[str],
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
ListChannelsRequestRequestTypeDef = TypedDict(
    "ListChannelsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
TimestampTypeDef = Union[datetime, str]
ListDatasetsRequestRequestTypeDef = TypedDict(
    "ListDatasetsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListDatastoresRequestRequestTypeDef = TypedDict(
    "ListDatastoresRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListPipelinesRequestRequestTypeDef = TypedDict(
    "ListPipelinesRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
MathActivityTypeDef = TypedDict(
    "MathActivityTypeDef",
    {
        "name": str,
        "attribute": str,
        "math": str,
        "next": NotRequired[str],
    },
)
OutputFileUriValueTypeDef = TypedDict(
    "OutputFileUriValueTypeDef",
    {
        "fileName": str,
    },
)
RemoveAttributesActivityOutputTypeDef = TypedDict(
    "RemoveAttributesActivityOutputTypeDef",
    {
        "name": str,
        "attributes": List[str],
        "next": NotRequired[str],
    },
)
SelectAttributesActivityOutputTypeDef = TypedDict(
    "SelectAttributesActivityOutputTypeDef",
    {
        "name": str,
        "attributes": List[str],
        "next": NotRequired[str],
    },
)
ReprocessingSummaryTypeDef = TypedDict(
    "ReprocessingSummaryTypeDef",
    {
        "id": NotRequired[str],
        "status": NotRequired[ReprocessingStatusType],
        "creationTime": NotRequired[datetime],
    },
)
RemoveAttributesActivityTypeDef = TypedDict(
    "RemoveAttributesActivityTypeDef",
    {
        "name": str,
        "attributes": Sequence[str],
        "next": NotRequired[str],
    },
)
SelectAttributesActivityTypeDef = TypedDict(
    "SelectAttributesActivityTypeDef",
    {
        "name": str,
        "attributes": Sequence[str],
        "next": NotRequired[str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
AddAttributesActivityUnionTypeDef = Union[
    AddAttributesActivityTypeDef, AddAttributesActivityOutputTypeDef
]
BatchPutMessageResponseTypeDef = TypedDict(
    "BatchPutMessageResponseTypeDef",
    {
        "batchPutMessageErrorEntries": List[BatchPutMessageErrorEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDatasetContentResponseTypeDef = TypedDict(
    "CreateDatasetContentResponseTypeDef",
    {
        "versionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePipelineResponseTypeDef = TypedDict(
    "CreatePipelineResponseTypeDef",
    {
        "pipelineName": str,
        "pipelineArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RunPipelineActivityResponseTypeDef = TypedDict(
    "RunPipelineActivityResponseTypeDef",
    {
        "payloads": List[bytes],
        "logResult": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SampleChannelDataResponseTypeDef = TypedDict(
    "SampleChannelDataResponseTypeDef",
    {
        "payloads": List[bytes],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartPipelineReprocessingResponseTypeDef = TypedDict(
    "StartPipelineReprocessingResponseTypeDef",
    {
        "reprocessingId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "messageId": str,
        "payload": BlobTypeDef,
    },
)
ChannelStatisticsTypeDef = TypedDict(
    "ChannelStatisticsTypeDef",
    {
        "size": NotRequired[EstimatedResourceSizeTypeDef],
    },
)
DatastoreStatisticsTypeDef = TypedDict(
    "DatastoreStatisticsTypeDef",
    {
        "size": NotRequired[EstimatedResourceSizeTypeDef],
    },
)
ChannelStorageOutputTypeDef = TypedDict(
    "ChannelStorageOutputTypeDef",
    {
        "serviceManagedS3": NotRequired[Dict[str, Any]],
        "customerManagedS3": NotRequired[CustomerManagedChannelS3StorageTypeDef],
    },
)
ChannelStorageTypeDef = TypedDict(
    "ChannelStorageTypeDef",
    {
        "serviceManagedS3": NotRequired[Mapping[str, Any]],
        "customerManagedS3": NotRequired[CustomerManagedChannelS3StorageTypeDef],
    },
)
ChannelStorageSummaryTypeDef = TypedDict(
    "ChannelStorageSummaryTypeDef",
    {
        "serviceManagedS3": NotRequired[Dict[str, Any]],
        "customerManagedS3": NotRequired[CustomerManagedChannelS3StorageSummaryTypeDef],
    },
)
CreateChannelResponseTypeDef = TypedDict(
    "CreateChannelResponseTypeDef",
    {
        "channelName": str,
        "channelArn": str,
        "retentionPeriod": RetentionPeriodTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDatasetResponseTypeDef = TypedDict(
    "CreateDatasetResponseTypeDef",
    {
        "datasetName": str,
        "datasetArn": str,
        "retentionPeriod": RetentionPeriodTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDatastoreResponseTypeDef = TypedDict(
    "CreateDatastoreResponseTypeDef",
    {
        "datastoreName": str,
        "datastoreArn": str,
        "retentionPeriod": RetentionPeriodTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SchemaDefinitionOutputTypeDef = TypedDict(
    "SchemaDefinitionOutputTypeDef",
    {
        "columns": NotRequired[List[ColumnTypeDef]],
    },
)
SchemaDefinitionTypeDef = TypedDict(
    "SchemaDefinitionTypeDef",
    {
        "columns": NotRequired[Sequence[ColumnTypeDef]],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[TagTypeDef],
    },
)
DatasetContentSummaryTypeDef = TypedDict(
    "DatasetContentSummaryTypeDef",
    {
        "version": NotRequired[str],
        "status": NotRequired[DatasetContentStatusTypeDef],
        "creationTime": NotRequired[datetime],
        "scheduleTime": NotRequired[datetime],
        "completionTime": NotRequired[datetime],
    },
)
GetDatasetContentResponseTypeDef = TypedDict(
    "GetDatasetContentResponseTypeDef",
    {
        "entries": List[DatasetEntryTypeDef],
        "timestamp": datetime,
        "status": DatasetContentStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DatasetTriggerTypeDef = TypedDict(
    "DatasetTriggerTypeDef",
    {
        "schedule": NotRequired[ScheduleTypeDef],
        "dataset": NotRequired[TriggeringDatasetTypeDef],
    },
)
DatastoreIotSiteWiseMultiLayerStorageSummaryTypeDef = TypedDict(
    "DatastoreIotSiteWiseMultiLayerStorageSummaryTypeDef",
    {
        "customerManagedS3Storage": NotRequired[
            IotSiteWiseCustomerManagedDatastoreS3StorageSummaryTypeDef
        ],
    },
)
DatastoreIotSiteWiseMultiLayerStorageTypeDef = TypedDict(
    "DatastoreIotSiteWiseMultiLayerStorageTypeDef",
    {
        "customerManagedS3Storage": IotSiteWiseCustomerManagedDatastoreS3StorageTypeDef,
    },
)
DatastorePartitionTypeDef = TypedDict(
    "DatastorePartitionTypeDef",
    {
        "attributePartition": NotRequired[PartitionTypeDef],
        "timestampPartition": NotRequired[TimestampPartitionTypeDef],
    },
)
LateDataRuleConfigurationTypeDef = TypedDict(
    "LateDataRuleConfigurationTypeDef",
    {
        "deltaTimeSessionWindowConfiguration": NotRequired[
            DeltaTimeSessionWindowConfigurationTypeDef
        ],
    },
)
QueryFilterTypeDef = TypedDict(
    "QueryFilterTypeDef",
    {
        "deltaTime": NotRequired[DeltaTimeTypeDef],
    },
)
DescribeLoggingOptionsResponseTypeDef = TypedDict(
    "DescribeLoggingOptionsResponseTypeDef",
    {
        "loggingOptions": LoggingOptionsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutLoggingOptionsRequestRequestTypeDef = TypedDict(
    "PutLoggingOptionsRequestRequestTypeDef",
    {
        "loggingOptions": LoggingOptionsTypeDef,
    },
)
S3DestinationConfigurationTypeDef = TypedDict(
    "S3DestinationConfigurationTypeDef",
    {
        "bucket": str,
        "key": str,
        "roleArn": str,
        "glueConfiguration": NotRequired[GlueConfigurationTypeDef],
    },
)
ListChannelsRequestListChannelsPaginateTypeDef = TypedDict(
    "ListChannelsRequestListChannelsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDatasetsRequestListDatasetsPaginateTypeDef = TypedDict(
    "ListDatasetsRequestListDatasetsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDatastoresRequestListDatastoresPaginateTypeDef = TypedDict(
    "ListDatastoresRequestListDatastoresPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPipelinesRequestListPipelinesPaginateTypeDef = TypedDict(
    "ListPipelinesRequestListPipelinesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDatasetContentsRequestListDatasetContentsPaginateTypeDef = TypedDict(
    "ListDatasetContentsRequestListDatasetContentsPaginateTypeDef",
    {
        "datasetName": str,
        "scheduledOnOrAfter": NotRequired[TimestampTypeDef],
        "scheduledBefore": NotRequired[TimestampTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDatasetContentsRequestRequestTypeDef = TypedDict(
    "ListDatasetContentsRequestRequestTypeDef",
    {
        "datasetName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "scheduledOnOrAfter": NotRequired[TimestampTypeDef],
        "scheduledBefore": NotRequired[TimestampTypeDef],
    },
)
SampleChannelDataRequestRequestTypeDef = TypedDict(
    "SampleChannelDataRequestRequestTypeDef",
    {
        "channelName": str,
        "maxMessages": NotRequired[int],
        "startTime": NotRequired[TimestampTypeDef],
        "endTime": NotRequired[TimestampTypeDef],
    },
)
StartPipelineReprocessingRequestRequestTypeDef = TypedDict(
    "StartPipelineReprocessingRequestRequestTypeDef",
    {
        "pipelineName": str,
        "startTime": NotRequired[TimestampTypeDef],
        "endTime": NotRequired[TimestampTypeDef],
        "channelMessages": NotRequired[ChannelMessagesTypeDef],
    },
)
VariableTypeDef = TypedDict(
    "VariableTypeDef",
    {
        "name": str,
        "stringValue": NotRequired[str],
        "doubleValue": NotRequired[float],
        "datasetContentVersionValue": NotRequired[DatasetContentVersionValueTypeDef],
        "outputFileUriValue": NotRequired[OutputFileUriValueTypeDef],
    },
)
PipelineActivityOutputTypeDef = TypedDict(
    "PipelineActivityOutputTypeDef",
    {
        "channel": NotRequired[ChannelActivityTypeDef],
        "lambda": NotRequired[LambdaActivityTypeDef],
        "datastore": NotRequired[DatastoreActivityTypeDef],
        "addAttributes": NotRequired[AddAttributesActivityOutputTypeDef],
        "removeAttributes": NotRequired[RemoveAttributesActivityOutputTypeDef],
        "selectAttributes": NotRequired[SelectAttributesActivityOutputTypeDef],
        "filter": NotRequired[FilterActivityTypeDef],
        "math": NotRequired[MathActivityTypeDef],
        "deviceRegistryEnrich": NotRequired[DeviceRegistryEnrichActivityTypeDef],
        "deviceShadowEnrich": NotRequired[DeviceShadowEnrichActivityTypeDef],
    },
)
PipelineSummaryTypeDef = TypedDict(
    "PipelineSummaryTypeDef",
    {
        "pipelineName": NotRequired[str],
        "reprocessingSummaries": NotRequired[List[ReprocessingSummaryTypeDef]],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
    },
)
RemoveAttributesActivityUnionTypeDef = Union[
    RemoveAttributesActivityTypeDef, RemoveAttributesActivityOutputTypeDef
]
SelectAttributesActivityUnionTypeDef = Union[
    SelectAttributesActivityTypeDef, SelectAttributesActivityOutputTypeDef
]
BatchPutMessageRequestRequestTypeDef = TypedDict(
    "BatchPutMessageRequestRequestTypeDef",
    {
        "channelName": str,
        "messages": Sequence[MessageTypeDef],
    },
)
ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "name": NotRequired[str],
        "storage": NotRequired[ChannelStorageOutputTypeDef],
        "arn": NotRequired[str],
        "status": NotRequired[ChannelStatusType],
        "retentionPeriod": NotRequired[RetentionPeriodTypeDef],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "lastMessageArrivalTime": NotRequired[datetime],
    },
)
CreateChannelRequestRequestTypeDef = TypedDict(
    "CreateChannelRequestRequestTypeDef",
    {
        "channelName": str,
        "channelStorage": NotRequired[ChannelStorageTypeDef],
        "retentionPeriod": NotRequired[RetentionPeriodTypeDef],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
UpdateChannelRequestRequestTypeDef = TypedDict(
    "UpdateChannelRequestRequestTypeDef",
    {
        "channelName": str,
        "channelStorage": NotRequired[ChannelStorageTypeDef],
        "retentionPeriod": NotRequired[RetentionPeriodTypeDef],
    },
)
ChannelSummaryTypeDef = TypedDict(
    "ChannelSummaryTypeDef",
    {
        "channelName": NotRequired[str],
        "channelStorage": NotRequired[ChannelStorageSummaryTypeDef],
        "status": NotRequired[ChannelStatusType],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "lastMessageArrivalTime": NotRequired[datetime],
    },
)
ParquetConfigurationOutputTypeDef = TypedDict(
    "ParquetConfigurationOutputTypeDef",
    {
        "schemaDefinition": NotRequired[SchemaDefinitionOutputTypeDef],
    },
)
SchemaDefinitionUnionTypeDef = Union[SchemaDefinitionTypeDef, SchemaDefinitionOutputTypeDef]
ListDatasetContentsResponseTypeDef = TypedDict(
    "ListDatasetContentsResponseTypeDef",
    {
        "datasetContentSummaries": List[DatasetContentSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DatasetSummaryTypeDef = TypedDict(
    "DatasetSummaryTypeDef",
    {
        "datasetName": NotRequired[str],
        "status": NotRequired[DatasetStatusType],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "triggers": NotRequired[List[DatasetTriggerTypeDef]],
        "actions": NotRequired[List[DatasetActionSummaryTypeDef]],
    },
)
DatastoreStorageSummaryTypeDef = TypedDict(
    "DatastoreStorageSummaryTypeDef",
    {
        "serviceManagedS3": NotRequired[Dict[str, Any]],
        "customerManagedS3": NotRequired[CustomerManagedDatastoreS3StorageSummaryTypeDef],
        "iotSiteWiseMultiLayerStorage": NotRequired[
            DatastoreIotSiteWiseMultiLayerStorageSummaryTypeDef
        ],
    },
)
DatastoreStorageOutputTypeDef = TypedDict(
    "DatastoreStorageOutputTypeDef",
    {
        "serviceManagedS3": NotRequired[Dict[str, Any]],
        "customerManagedS3": NotRequired[CustomerManagedDatastoreS3StorageTypeDef],
        "iotSiteWiseMultiLayerStorage": NotRequired[DatastoreIotSiteWiseMultiLayerStorageTypeDef],
    },
)
DatastoreStorageTypeDef = TypedDict(
    "DatastoreStorageTypeDef",
    {
        "serviceManagedS3": NotRequired[Mapping[str, Any]],
        "customerManagedS3": NotRequired[CustomerManagedDatastoreS3StorageTypeDef],
        "iotSiteWiseMultiLayerStorage": NotRequired[DatastoreIotSiteWiseMultiLayerStorageTypeDef],
    },
)
DatastorePartitionsOutputTypeDef = TypedDict(
    "DatastorePartitionsOutputTypeDef",
    {
        "partitions": NotRequired[List[DatastorePartitionTypeDef]],
    },
)
DatastorePartitionsTypeDef = TypedDict(
    "DatastorePartitionsTypeDef",
    {
        "partitions": NotRequired[Sequence[DatastorePartitionTypeDef]],
    },
)
LateDataRuleTypeDef = TypedDict(
    "LateDataRuleTypeDef",
    {
        "ruleConfiguration": LateDataRuleConfigurationTypeDef,
        "ruleName": NotRequired[str],
    },
)
SqlQueryDatasetActionOutputTypeDef = TypedDict(
    "SqlQueryDatasetActionOutputTypeDef",
    {
        "sqlQuery": str,
        "filters": NotRequired[List[QueryFilterTypeDef]],
    },
)
SqlQueryDatasetActionTypeDef = TypedDict(
    "SqlQueryDatasetActionTypeDef",
    {
        "sqlQuery": str,
        "filters": NotRequired[Sequence[QueryFilterTypeDef]],
    },
)
DatasetContentDeliveryDestinationTypeDef = TypedDict(
    "DatasetContentDeliveryDestinationTypeDef",
    {
        "iotEventsDestinationConfiguration": NotRequired[IotEventsDestinationConfigurationTypeDef],
        "s3DestinationConfiguration": NotRequired[S3DestinationConfigurationTypeDef],
    },
)
ContainerDatasetActionOutputTypeDef = TypedDict(
    "ContainerDatasetActionOutputTypeDef",
    {
        "image": str,
        "executionRoleArn": str,
        "resourceConfiguration": ResourceConfigurationTypeDef,
        "variables": NotRequired[List[VariableTypeDef]],
    },
)
ContainerDatasetActionTypeDef = TypedDict(
    "ContainerDatasetActionTypeDef",
    {
        "image": str,
        "executionRoleArn": str,
        "resourceConfiguration": ResourceConfigurationTypeDef,
        "variables": NotRequired[Sequence[VariableTypeDef]],
    },
)
PipelineTypeDef = TypedDict(
    "PipelineTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "activities": NotRequired[List[PipelineActivityOutputTypeDef]],
        "reprocessingSummaries": NotRequired[List[ReprocessingSummaryTypeDef]],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
    },
)
ListPipelinesResponseTypeDef = TypedDict(
    "ListPipelinesResponseTypeDef",
    {
        "pipelineSummaries": List[PipelineSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PipelineActivityTypeDef = TypedDict(
    "PipelineActivityTypeDef",
    {
        "channel": NotRequired[ChannelActivityTypeDef],
        "lambda": NotRequired[LambdaActivityTypeDef],
        "datastore": NotRequired[DatastoreActivityTypeDef],
        "addAttributes": NotRequired[AddAttributesActivityUnionTypeDef],
        "removeAttributes": NotRequired[RemoveAttributesActivityUnionTypeDef],
        "selectAttributes": NotRequired[SelectAttributesActivityUnionTypeDef],
        "filter": NotRequired[FilterActivityTypeDef],
        "math": NotRequired[MathActivityTypeDef],
        "deviceRegistryEnrich": NotRequired[DeviceRegistryEnrichActivityTypeDef],
        "deviceShadowEnrich": NotRequired[DeviceShadowEnrichActivityTypeDef],
    },
)
DescribeChannelResponseTypeDef = TypedDict(
    "DescribeChannelResponseTypeDef",
    {
        "channel": ChannelTypeDef,
        "statistics": ChannelStatisticsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListChannelsResponseTypeDef = TypedDict(
    "ListChannelsResponseTypeDef",
    {
        "channelSummaries": List[ChannelSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FileFormatConfigurationOutputTypeDef = TypedDict(
    "FileFormatConfigurationOutputTypeDef",
    {
        "jsonConfiguration": NotRequired[Dict[str, Any]],
        "parquetConfiguration": NotRequired[ParquetConfigurationOutputTypeDef],
    },
)
ParquetConfigurationTypeDef = TypedDict(
    "ParquetConfigurationTypeDef",
    {
        "schemaDefinition": NotRequired[SchemaDefinitionUnionTypeDef],
    },
)
ListDatasetsResponseTypeDef = TypedDict(
    "ListDatasetsResponseTypeDef",
    {
        "datasetSummaries": List[DatasetSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DatastoreSummaryTypeDef = TypedDict(
    "DatastoreSummaryTypeDef",
    {
        "datastoreName": NotRequired[str],
        "datastoreStorage": NotRequired[DatastoreStorageSummaryTypeDef],
        "status": NotRequired[DatastoreStatusType],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "lastMessageArrivalTime": NotRequired[datetime],
        "fileFormatType": NotRequired[FileFormatTypeType],
        "datastorePartitions": NotRequired[DatastorePartitionsOutputTypeDef],
    },
)
SqlQueryDatasetActionUnionTypeDef = Union[
    SqlQueryDatasetActionTypeDef, SqlQueryDatasetActionOutputTypeDef
]
DatasetContentDeliveryRuleTypeDef = TypedDict(
    "DatasetContentDeliveryRuleTypeDef",
    {
        "destination": DatasetContentDeliveryDestinationTypeDef,
        "entryName": NotRequired[str],
    },
)
DatasetActionOutputTypeDef = TypedDict(
    "DatasetActionOutputTypeDef",
    {
        "actionName": NotRequired[str],
        "queryAction": NotRequired[SqlQueryDatasetActionOutputTypeDef],
        "containerAction": NotRequired[ContainerDatasetActionOutputTypeDef],
    },
)
ContainerDatasetActionUnionTypeDef = Union[
    ContainerDatasetActionTypeDef, ContainerDatasetActionOutputTypeDef
]
DescribePipelineResponseTypeDef = TypedDict(
    "DescribePipelineResponseTypeDef",
    {
        "pipeline": PipelineTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PipelineActivityUnionTypeDef = Union[PipelineActivityTypeDef, PipelineActivityOutputTypeDef]
RunPipelineActivityRequestRequestTypeDef = TypedDict(
    "RunPipelineActivityRequestRequestTypeDef",
    {
        "pipelineActivity": PipelineActivityTypeDef,
        "payloads": Sequence[BlobTypeDef],
    },
)
UpdatePipelineRequestRequestTypeDef = TypedDict(
    "UpdatePipelineRequestRequestTypeDef",
    {
        "pipelineName": str,
        "pipelineActivities": Sequence[PipelineActivityTypeDef],
    },
)
DatastoreTypeDef = TypedDict(
    "DatastoreTypeDef",
    {
        "name": NotRequired[str],
        "storage": NotRequired[DatastoreStorageOutputTypeDef],
        "arn": NotRequired[str],
        "status": NotRequired[DatastoreStatusType],
        "retentionPeriod": NotRequired[RetentionPeriodTypeDef],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "lastMessageArrivalTime": NotRequired[datetime],
        "fileFormatConfiguration": NotRequired[FileFormatConfigurationOutputTypeDef],
        "datastorePartitions": NotRequired[DatastorePartitionsOutputTypeDef],
    },
)
ParquetConfigurationUnionTypeDef = Union[
    ParquetConfigurationTypeDef, ParquetConfigurationOutputTypeDef
]
ListDatastoresResponseTypeDef = TypedDict(
    "ListDatastoresResponseTypeDef",
    {
        "datastoreSummaries": List[DatastoreSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DatasetTypeDef = TypedDict(
    "DatasetTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "actions": NotRequired[List[DatasetActionOutputTypeDef]],
        "triggers": NotRequired[List[DatasetTriggerTypeDef]],
        "contentDeliveryRules": NotRequired[List[DatasetContentDeliveryRuleTypeDef]],
        "status": NotRequired[DatasetStatusType],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "retentionPeriod": NotRequired[RetentionPeriodTypeDef],
        "versioningConfiguration": NotRequired[VersioningConfigurationTypeDef],
        "lateDataRules": NotRequired[List[LateDataRuleTypeDef]],
    },
)
DatasetActionTypeDef = TypedDict(
    "DatasetActionTypeDef",
    {
        "actionName": NotRequired[str],
        "queryAction": NotRequired[SqlQueryDatasetActionUnionTypeDef],
        "containerAction": NotRequired[ContainerDatasetActionUnionTypeDef],
    },
)
CreatePipelineRequestRequestTypeDef = TypedDict(
    "CreatePipelineRequestRequestTypeDef",
    {
        "pipelineName": str,
        "pipelineActivities": Sequence[PipelineActivityUnionTypeDef],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
DescribeDatastoreResponseTypeDef = TypedDict(
    "DescribeDatastoreResponseTypeDef",
    {
        "datastore": DatastoreTypeDef,
        "statistics": DatastoreStatisticsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FileFormatConfigurationTypeDef = TypedDict(
    "FileFormatConfigurationTypeDef",
    {
        "jsonConfiguration": NotRequired[Mapping[str, Any]],
        "parquetConfiguration": NotRequired[ParquetConfigurationUnionTypeDef],
    },
)
DescribeDatasetResponseTypeDef = TypedDict(
    "DescribeDatasetResponseTypeDef",
    {
        "dataset": DatasetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DatasetActionUnionTypeDef = Union[DatasetActionTypeDef, DatasetActionOutputTypeDef]
UpdateDatasetRequestRequestTypeDef = TypedDict(
    "UpdateDatasetRequestRequestTypeDef",
    {
        "datasetName": str,
        "actions": Sequence[DatasetActionTypeDef],
        "triggers": NotRequired[Sequence[DatasetTriggerTypeDef]],
        "contentDeliveryRules": NotRequired[Sequence[DatasetContentDeliveryRuleTypeDef]],
        "retentionPeriod": NotRequired[RetentionPeriodTypeDef],
        "versioningConfiguration": NotRequired[VersioningConfigurationTypeDef],
        "lateDataRules": NotRequired[Sequence[LateDataRuleTypeDef]],
    },
)
CreateDatastoreRequestRequestTypeDef = TypedDict(
    "CreateDatastoreRequestRequestTypeDef",
    {
        "datastoreName": str,
        "datastoreStorage": NotRequired[DatastoreStorageTypeDef],
        "retentionPeriod": NotRequired[RetentionPeriodTypeDef],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "fileFormatConfiguration": NotRequired[FileFormatConfigurationTypeDef],
        "datastorePartitions": NotRequired[DatastorePartitionsTypeDef],
    },
)
UpdateDatastoreRequestRequestTypeDef = TypedDict(
    "UpdateDatastoreRequestRequestTypeDef",
    {
        "datastoreName": str,
        "retentionPeriod": NotRequired[RetentionPeriodTypeDef],
        "datastoreStorage": NotRequired[DatastoreStorageTypeDef],
        "fileFormatConfiguration": NotRequired[FileFormatConfigurationTypeDef],
    },
)
CreateDatasetRequestRequestTypeDef = TypedDict(
    "CreateDatasetRequestRequestTypeDef",
    {
        "datasetName": str,
        "actions": Sequence[DatasetActionUnionTypeDef],
        "triggers": NotRequired[Sequence[DatasetTriggerTypeDef]],
        "contentDeliveryRules": NotRequired[Sequence[DatasetContentDeliveryRuleTypeDef]],
        "retentionPeriod": NotRequired[RetentionPeriodTypeDef],
        "versioningConfiguration": NotRequired[VersioningConfigurationTypeDef],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "lateDataRules": NotRequired[Sequence[LateDataRuleTypeDef]],
    },
)
