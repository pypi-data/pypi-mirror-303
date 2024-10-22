"""
Type annotations for kinesisanalytics service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/type_defs/)

Usage::

    ```python
    from mypy_boto3_kinesisanalytics.type_defs import CloudWatchLoggingOptionTypeDef

    data: CloudWatchLoggingOptionTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import ApplicationStatusType, InputStartingPositionType, RecordFormatTypeType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "CloudWatchLoggingOptionTypeDef",
    "CloudWatchLoggingOptionDescriptionTypeDef",
    "ApplicationSummaryTypeDef",
    "CloudWatchLoggingOptionUpdateTypeDef",
    "CSVMappingParametersTypeDef",
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "DeleteApplicationCloudWatchLoggingOptionRequestRequestTypeDef",
    "DeleteApplicationInputProcessingConfigurationRequestRequestTypeDef",
    "DeleteApplicationOutputRequestRequestTypeDef",
    "DeleteApplicationReferenceDataSourceRequestRequestTypeDef",
    "TimestampTypeDef",
    "DescribeApplicationRequestRequestTypeDef",
    "DestinationSchemaTypeDef",
    "InputStartingPositionConfigurationTypeDef",
    "S3ConfigurationTypeDef",
    "InputParallelismTypeDef",
    "KinesisFirehoseInputDescriptionTypeDef",
    "KinesisStreamsInputDescriptionTypeDef",
    "InputLambdaProcessorDescriptionTypeDef",
    "InputLambdaProcessorTypeDef",
    "InputLambdaProcessorUpdateTypeDef",
    "InputParallelismUpdateTypeDef",
    "RecordColumnTypeDef",
    "KinesisFirehoseInputTypeDef",
    "KinesisStreamsInputTypeDef",
    "KinesisFirehoseInputUpdateTypeDef",
    "KinesisStreamsInputUpdateTypeDef",
    "JSONMappingParametersTypeDef",
    "KinesisFirehoseOutputDescriptionTypeDef",
    "KinesisFirehoseOutputTypeDef",
    "KinesisFirehoseOutputUpdateTypeDef",
    "KinesisStreamsOutputDescriptionTypeDef",
    "KinesisStreamsOutputTypeDef",
    "KinesisStreamsOutputUpdateTypeDef",
    "LambdaOutputDescriptionTypeDef",
    "LambdaOutputTypeDef",
    "LambdaOutputUpdateTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "S3ReferenceDataSourceDescriptionTypeDef",
    "S3ReferenceDataSourceTypeDef",
    "S3ReferenceDataSourceUpdateTypeDef",
    "StopApplicationRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "AddApplicationCloudWatchLoggingOptionRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateApplicationResponseTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "InputConfigurationTypeDef",
    "InputProcessingConfigurationDescriptionTypeDef",
    "InputProcessingConfigurationTypeDef",
    "InputProcessingConfigurationUpdateTypeDef",
    "MappingParametersTypeDef",
    "OutputDescriptionTypeDef",
    "OutputTypeDef",
    "OutputUpdateTypeDef",
    "StartApplicationRequestRequestTypeDef",
    "AddApplicationInputProcessingConfigurationRequestRequestTypeDef",
    "DiscoverInputSchemaRequestRequestTypeDef",
    "RecordFormatTypeDef",
    "AddApplicationOutputRequestRequestTypeDef",
    "InputSchemaUpdateTypeDef",
    "SourceSchemaOutputTypeDef",
    "SourceSchemaTypeDef",
    "InputUpdateTypeDef",
    "DiscoverInputSchemaResponseTypeDef",
    "InputDescriptionTypeDef",
    "ReferenceDataSourceDescriptionTypeDef",
    "SourceSchemaUnionTypeDef",
    "ApplicationDetailTypeDef",
    "InputTypeDef",
    "ReferenceDataSourceTypeDef",
    "ReferenceDataSourceUpdateTypeDef",
    "DescribeApplicationResponseTypeDef",
    "AddApplicationInputRequestRequestTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "AddApplicationReferenceDataSourceRequestRequestTypeDef",
    "ApplicationUpdateTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
)

CloudWatchLoggingOptionTypeDef = TypedDict(
    "CloudWatchLoggingOptionTypeDef",
    {
        "LogStreamARN": str,
        "RoleARN": str,
    },
)
CloudWatchLoggingOptionDescriptionTypeDef = TypedDict(
    "CloudWatchLoggingOptionDescriptionTypeDef",
    {
        "LogStreamARN": str,
        "RoleARN": str,
        "CloudWatchLoggingOptionId": NotRequired[str],
    },
)
ApplicationSummaryTypeDef = TypedDict(
    "ApplicationSummaryTypeDef",
    {
        "ApplicationName": str,
        "ApplicationARN": str,
        "ApplicationStatus": ApplicationStatusType,
    },
)
CloudWatchLoggingOptionUpdateTypeDef = TypedDict(
    "CloudWatchLoggingOptionUpdateTypeDef",
    {
        "CloudWatchLoggingOptionId": str,
        "LogStreamARNUpdate": NotRequired[str],
        "RoleARNUpdate": NotRequired[str],
    },
)
CSVMappingParametersTypeDef = TypedDict(
    "CSVMappingParametersTypeDef",
    {
        "RecordRowDelimiter": str,
        "RecordColumnDelimiter": str,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": NotRequired[str],
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
DeleteApplicationCloudWatchLoggingOptionRequestRequestTypeDef = TypedDict(
    "DeleteApplicationCloudWatchLoggingOptionRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "CloudWatchLoggingOptionId": str,
    },
)
DeleteApplicationInputProcessingConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationInputProcessingConfigurationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "InputId": str,
    },
)
DeleteApplicationOutputRequestRequestTypeDef = TypedDict(
    "DeleteApplicationOutputRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "OutputId": str,
    },
)
DeleteApplicationReferenceDataSourceRequestRequestTypeDef = TypedDict(
    "DeleteApplicationReferenceDataSourceRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "ReferenceId": str,
    },
)
TimestampTypeDef = Union[datetime, str]
DescribeApplicationRequestRequestTypeDef = TypedDict(
    "DescribeApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
    },
)
DestinationSchemaTypeDef = TypedDict(
    "DestinationSchemaTypeDef",
    {
        "RecordFormatType": RecordFormatTypeType,
    },
)
InputStartingPositionConfigurationTypeDef = TypedDict(
    "InputStartingPositionConfigurationTypeDef",
    {
        "InputStartingPosition": NotRequired[InputStartingPositionType],
    },
)
S3ConfigurationTypeDef = TypedDict(
    "S3ConfigurationTypeDef",
    {
        "RoleARN": str,
        "BucketARN": str,
        "FileKey": str,
    },
)
InputParallelismTypeDef = TypedDict(
    "InputParallelismTypeDef",
    {
        "Count": NotRequired[int],
    },
)
KinesisFirehoseInputDescriptionTypeDef = TypedDict(
    "KinesisFirehoseInputDescriptionTypeDef",
    {
        "ResourceARN": NotRequired[str],
        "RoleARN": NotRequired[str],
    },
)
KinesisStreamsInputDescriptionTypeDef = TypedDict(
    "KinesisStreamsInputDescriptionTypeDef",
    {
        "ResourceARN": NotRequired[str],
        "RoleARN": NotRequired[str],
    },
)
InputLambdaProcessorDescriptionTypeDef = TypedDict(
    "InputLambdaProcessorDescriptionTypeDef",
    {
        "ResourceARN": NotRequired[str],
        "RoleARN": NotRequired[str],
    },
)
InputLambdaProcessorTypeDef = TypedDict(
    "InputLambdaProcessorTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
)
InputLambdaProcessorUpdateTypeDef = TypedDict(
    "InputLambdaProcessorUpdateTypeDef",
    {
        "ResourceARNUpdate": NotRequired[str],
        "RoleARNUpdate": NotRequired[str],
    },
)
InputParallelismUpdateTypeDef = TypedDict(
    "InputParallelismUpdateTypeDef",
    {
        "CountUpdate": NotRequired[int],
    },
)
RecordColumnTypeDef = TypedDict(
    "RecordColumnTypeDef",
    {
        "Name": str,
        "SqlType": str,
        "Mapping": NotRequired[str],
    },
)
KinesisFirehoseInputTypeDef = TypedDict(
    "KinesisFirehoseInputTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
)
KinesisStreamsInputTypeDef = TypedDict(
    "KinesisStreamsInputTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
)
KinesisFirehoseInputUpdateTypeDef = TypedDict(
    "KinesisFirehoseInputUpdateTypeDef",
    {
        "ResourceARNUpdate": NotRequired[str],
        "RoleARNUpdate": NotRequired[str],
    },
)
KinesisStreamsInputUpdateTypeDef = TypedDict(
    "KinesisStreamsInputUpdateTypeDef",
    {
        "ResourceARNUpdate": NotRequired[str],
        "RoleARNUpdate": NotRequired[str],
    },
)
JSONMappingParametersTypeDef = TypedDict(
    "JSONMappingParametersTypeDef",
    {
        "RecordRowPath": str,
    },
)
KinesisFirehoseOutputDescriptionTypeDef = TypedDict(
    "KinesisFirehoseOutputDescriptionTypeDef",
    {
        "ResourceARN": NotRequired[str],
        "RoleARN": NotRequired[str],
    },
)
KinesisFirehoseOutputTypeDef = TypedDict(
    "KinesisFirehoseOutputTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
)
KinesisFirehoseOutputUpdateTypeDef = TypedDict(
    "KinesisFirehoseOutputUpdateTypeDef",
    {
        "ResourceARNUpdate": NotRequired[str],
        "RoleARNUpdate": NotRequired[str],
    },
)
KinesisStreamsOutputDescriptionTypeDef = TypedDict(
    "KinesisStreamsOutputDescriptionTypeDef",
    {
        "ResourceARN": NotRequired[str],
        "RoleARN": NotRequired[str],
    },
)
KinesisStreamsOutputTypeDef = TypedDict(
    "KinesisStreamsOutputTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
)
KinesisStreamsOutputUpdateTypeDef = TypedDict(
    "KinesisStreamsOutputUpdateTypeDef",
    {
        "ResourceARNUpdate": NotRequired[str],
        "RoleARNUpdate": NotRequired[str],
    },
)
LambdaOutputDescriptionTypeDef = TypedDict(
    "LambdaOutputDescriptionTypeDef",
    {
        "ResourceARN": NotRequired[str],
        "RoleARN": NotRequired[str],
    },
)
LambdaOutputTypeDef = TypedDict(
    "LambdaOutputTypeDef",
    {
        "ResourceARN": str,
        "RoleARN": str,
    },
)
LambdaOutputUpdateTypeDef = TypedDict(
    "LambdaOutputUpdateTypeDef",
    {
        "ResourceARNUpdate": NotRequired[str],
        "RoleARNUpdate": NotRequired[str],
    },
)
ListApplicationsRequestRequestTypeDef = TypedDict(
    "ListApplicationsRequestRequestTypeDef",
    {
        "Limit": NotRequired[int],
        "ExclusiveStartApplicationName": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
S3ReferenceDataSourceDescriptionTypeDef = TypedDict(
    "S3ReferenceDataSourceDescriptionTypeDef",
    {
        "BucketARN": str,
        "FileKey": str,
        "ReferenceRoleARN": str,
    },
)
S3ReferenceDataSourceTypeDef = TypedDict(
    "S3ReferenceDataSourceTypeDef",
    {
        "BucketARN": str,
        "FileKey": str,
        "ReferenceRoleARN": str,
    },
)
S3ReferenceDataSourceUpdateTypeDef = TypedDict(
    "S3ReferenceDataSourceUpdateTypeDef",
    {
        "BucketARNUpdate": NotRequired[str],
        "FileKeyUpdate": NotRequired[str],
        "ReferenceRoleARNUpdate": NotRequired[str],
    },
)
StopApplicationRequestRequestTypeDef = TypedDict(
    "StopApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
AddApplicationCloudWatchLoggingOptionRequestRequestTypeDef = TypedDict(
    "AddApplicationCloudWatchLoggingOptionRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "CloudWatchLoggingOption": CloudWatchLoggingOptionTypeDef,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "ApplicationSummary": ApplicationSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {
        "ApplicationSummaries": List[ApplicationSummaryTypeDef],
        "HasMoreApplications": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CreateTimestamp": TimestampTypeDef,
    },
)
InputConfigurationTypeDef = TypedDict(
    "InputConfigurationTypeDef",
    {
        "Id": str,
        "InputStartingPositionConfiguration": InputStartingPositionConfigurationTypeDef,
    },
)
InputProcessingConfigurationDescriptionTypeDef = TypedDict(
    "InputProcessingConfigurationDescriptionTypeDef",
    {
        "InputLambdaProcessorDescription": NotRequired[InputLambdaProcessorDescriptionTypeDef],
    },
)
InputProcessingConfigurationTypeDef = TypedDict(
    "InputProcessingConfigurationTypeDef",
    {
        "InputLambdaProcessor": InputLambdaProcessorTypeDef,
    },
)
InputProcessingConfigurationUpdateTypeDef = TypedDict(
    "InputProcessingConfigurationUpdateTypeDef",
    {
        "InputLambdaProcessorUpdate": InputLambdaProcessorUpdateTypeDef,
    },
)
MappingParametersTypeDef = TypedDict(
    "MappingParametersTypeDef",
    {
        "JSONMappingParameters": NotRequired[JSONMappingParametersTypeDef],
        "CSVMappingParameters": NotRequired[CSVMappingParametersTypeDef],
    },
)
OutputDescriptionTypeDef = TypedDict(
    "OutputDescriptionTypeDef",
    {
        "OutputId": NotRequired[str],
        "Name": NotRequired[str],
        "KinesisStreamsOutputDescription": NotRequired[KinesisStreamsOutputDescriptionTypeDef],
        "KinesisFirehoseOutputDescription": NotRequired[KinesisFirehoseOutputDescriptionTypeDef],
        "LambdaOutputDescription": NotRequired[LambdaOutputDescriptionTypeDef],
        "DestinationSchema": NotRequired[DestinationSchemaTypeDef],
    },
)
OutputTypeDef = TypedDict(
    "OutputTypeDef",
    {
        "Name": str,
        "DestinationSchema": DestinationSchemaTypeDef,
        "KinesisStreamsOutput": NotRequired[KinesisStreamsOutputTypeDef],
        "KinesisFirehoseOutput": NotRequired[KinesisFirehoseOutputTypeDef],
        "LambdaOutput": NotRequired[LambdaOutputTypeDef],
    },
)
OutputUpdateTypeDef = TypedDict(
    "OutputUpdateTypeDef",
    {
        "OutputId": str,
        "NameUpdate": NotRequired[str],
        "KinesisStreamsOutputUpdate": NotRequired[KinesisStreamsOutputUpdateTypeDef],
        "KinesisFirehoseOutputUpdate": NotRequired[KinesisFirehoseOutputUpdateTypeDef],
        "LambdaOutputUpdate": NotRequired[LambdaOutputUpdateTypeDef],
        "DestinationSchemaUpdate": NotRequired[DestinationSchemaTypeDef],
    },
)
StartApplicationRequestRequestTypeDef = TypedDict(
    "StartApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "InputConfigurations": Sequence[InputConfigurationTypeDef],
    },
)
AddApplicationInputProcessingConfigurationRequestRequestTypeDef = TypedDict(
    "AddApplicationInputProcessingConfigurationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "InputId": str,
        "InputProcessingConfiguration": InputProcessingConfigurationTypeDef,
    },
)
DiscoverInputSchemaRequestRequestTypeDef = TypedDict(
    "DiscoverInputSchemaRequestRequestTypeDef",
    {
        "ResourceARN": NotRequired[str],
        "RoleARN": NotRequired[str],
        "InputStartingPositionConfiguration": NotRequired[
            InputStartingPositionConfigurationTypeDef
        ],
        "S3Configuration": NotRequired[S3ConfigurationTypeDef],
        "InputProcessingConfiguration": NotRequired[InputProcessingConfigurationTypeDef],
    },
)
RecordFormatTypeDef = TypedDict(
    "RecordFormatTypeDef",
    {
        "RecordFormatType": RecordFormatTypeType,
        "MappingParameters": NotRequired[MappingParametersTypeDef],
    },
)
AddApplicationOutputRequestRequestTypeDef = TypedDict(
    "AddApplicationOutputRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "Output": OutputTypeDef,
    },
)
InputSchemaUpdateTypeDef = TypedDict(
    "InputSchemaUpdateTypeDef",
    {
        "RecordFormatUpdate": NotRequired[RecordFormatTypeDef],
        "RecordEncodingUpdate": NotRequired[str],
        "RecordColumnUpdates": NotRequired[Sequence[RecordColumnTypeDef]],
    },
)
SourceSchemaOutputTypeDef = TypedDict(
    "SourceSchemaOutputTypeDef",
    {
        "RecordFormat": RecordFormatTypeDef,
        "RecordColumns": List[RecordColumnTypeDef],
        "RecordEncoding": NotRequired[str],
    },
)
SourceSchemaTypeDef = TypedDict(
    "SourceSchemaTypeDef",
    {
        "RecordFormat": RecordFormatTypeDef,
        "RecordColumns": Sequence[RecordColumnTypeDef],
        "RecordEncoding": NotRequired[str],
    },
)
InputUpdateTypeDef = TypedDict(
    "InputUpdateTypeDef",
    {
        "InputId": str,
        "NamePrefixUpdate": NotRequired[str],
        "InputProcessingConfigurationUpdate": NotRequired[
            InputProcessingConfigurationUpdateTypeDef
        ],
        "KinesisStreamsInputUpdate": NotRequired[KinesisStreamsInputUpdateTypeDef],
        "KinesisFirehoseInputUpdate": NotRequired[KinesisFirehoseInputUpdateTypeDef],
        "InputSchemaUpdate": NotRequired[InputSchemaUpdateTypeDef],
        "InputParallelismUpdate": NotRequired[InputParallelismUpdateTypeDef],
    },
)
DiscoverInputSchemaResponseTypeDef = TypedDict(
    "DiscoverInputSchemaResponseTypeDef",
    {
        "InputSchema": SourceSchemaOutputTypeDef,
        "ParsedInputRecords": List[List[str]],
        "ProcessedInputRecords": List[str],
        "RawInputRecords": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InputDescriptionTypeDef = TypedDict(
    "InputDescriptionTypeDef",
    {
        "InputId": NotRequired[str],
        "NamePrefix": NotRequired[str],
        "InAppStreamNames": NotRequired[List[str]],
        "InputProcessingConfigurationDescription": NotRequired[
            InputProcessingConfigurationDescriptionTypeDef
        ],
        "KinesisStreamsInputDescription": NotRequired[KinesisStreamsInputDescriptionTypeDef],
        "KinesisFirehoseInputDescription": NotRequired[KinesisFirehoseInputDescriptionTypeDef],
        "InputSchema": NotRequired[SourceSchemaOutputTypeDef],
        "InputParallelism": NotRequired[InputParallelismTypeDef],
        "InputStartingPositionConfiguration": NotRequired[
            InputStartingPositionConfigurationTypeDef
        ],
    },
)
ReferenceDataSourceDescriptionTypeDef = TypedDict(
    "ReferenceDataSourceDescriptionTypeDef",
    {
        "ReferenceId": str,
        "TableName": str,
        "S3ReferenceDataSourceDescription": S3ReferenceDataSourceDescriptionTypeDef,
        "ReferenceSchema": NotRequired[SourceSchemaOutputTypeDef],
    },
)
SourceSchemaUnionTypeDef = Union[SourceSchemaTypeDef, SourceSchemaOutputTypeDef]
ApplicationDetailTypeDef = TypedDict(
    "ApplicationDetailTypeDef",
    {
        "ApplicationName": str,
        "ApplicationARN": str,
        "ApplicationStatus": ApplicationStatusType,
        "ApplicationVersionId": int,
        "ApplicationDescription": NotRequired[str],
        "CreateTimestamp": NotRequired[datetime],
        "LastUpdateTimestamp": NotRequired[datetime],
        "InputDescriptions": NotRequired[List[InputDescriptionTypeDef]],
        "OutputDescriptions": NotRequired[List[OutputDescriptionTypeDef]],
        "ReferenceDataSourceDescriptions": NotRequired[List[ReferenceDataSourceDescriptionTypeDef]],
        "CloudWatchLoggingOptionDescriptions": NotRequired[
            List[CloudWatchLoggingOptionDescriptionTypeDef]
        ],
        "ApplicationCode": NotRequired[str],
    },
)
InputTypeDef = TypedDict(
    "InputTypeDef",
    {
        "NamePrefix": str,
        "InputSchema": SourceSchemaUnionTypeDef,
        "InputProcessingConfiguration": NotRequired[InputProcessingConfigurationTypeDef],
        "KinesisStreamsInput": NotRequired[KinesisStreamsInputTypeDef],
        "KinesisFirehoseInput": NotRequired[KinesisFirehoseInputTypeDef],
        "InputParallelism": NotRequired[InputParallelismTypeDef],
    },
)
ReferenceDataSourceTypeDef = TypedDict(
    "ReferenceDataSourceTypeDef",
    {
        "TableName": str,
        "ReferenceSchema": SourceSchemaUnionTypeDef,
        "S3ReferenceDataSource": NotRequired[S3ReferenceDataSourceTypeDef],
    },
)
ReferenceDataSourceUpdateTypeDef = TypedDict(
    "ReferenceDataSourceUpdateTypeDef",
    {
        "ReferenceId": str,
        "TableNameUpdate": NotRequired[str],
        "S3ReferenceDataSourceUpdate": NotRequired[S3ReferenceDataSourceUpdateTypeDef],
        "ReferenceSchemaUpdate": NotRequired[SourceSchemaUnionTypeDef],
    },
)
DescribeApplicationResponseTypeDef = TypedDict(
    "DescribeApplicationResponseTypeDef",
    {
        "ApplicationDetail": ApplicationDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AddApplicationInputRequestRequestTypeDef = TypedDict(
    "AddApplicationInputRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "Input": InputTypeDef,
    },
)
CreateApplicationRequestRequestTypeDef = TypedDict(
    "CreateApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "ApplicationDescription": NotRequired[str],
        "Inputs": NotRequired[Sequence[InputTypeDef]],
        "Outputs": NotRequired[Sequence[OutputTypeDef]],
        "CloudWatchLoggingOptions": NotRequired[Sequence[CloudWatchLoggingOptionTypeDef]],
        "ApplicationCode": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
AddApplicationReferenceDataSourceRequestRequestTypeDef = TypedDict(
    "AddApplicationReferenceDataSourceRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "ReferenceDataSource": ReferenceDataSourceTypeDef,
    },
)
ApplicationUpdateTypeDef = TypedDict(
    "ApplicationUpdateTypeDef",
    {
        "InputUpdates": NotRequired[Sequence[InputUpdateTypeDef]],
        "ApplicationCodeUpdate": NotRequired[str],
        "OutputUpdates": NotRequired[Sequence[OutputUpdateTypeDef]],
        "ReferenceDataSourceUpdates": NotRequired[Sequence[ReferenceDataSourceUpdateTypeDef]],
        "CloudWatchLoggingOptionUpdates": NotRequired[
            Sequence[CloudWatchLoggingOptionUpdateTypeDef]
        ],
    },
)
UpdateApplicationRequestRequestTypeDef = TypedDict(
    "UpdateApplicationRequestRequestTypeDef",
    {
        "ApplicationName": str,
        "CurrentApplicationVersionId": int,
        "ApplicationUpdate": ApplicationUpdateTypeDef,
    },
)
