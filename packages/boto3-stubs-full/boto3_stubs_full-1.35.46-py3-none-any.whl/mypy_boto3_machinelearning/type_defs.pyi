"""
Type annotations for machinelearning service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/type_defs/)

Usage::

    ```python
    from mypy_boto3_machinelearning.type_defs import TagTypeDef

    data: TagTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    BatchPredictionFilterVariableType,
    DataSourceFilterVariableType,
    DetailsAttributesType,
    EntityStatusType,
    EvaluationFilterVariableType,
    MLModelFilterVariableType,
    MLModelTypeType,
    RealtimeEndpointStatusType,
    SortOrderType,
    TaggableResourceTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "BatchPredictionTypeDef",
    "CreateBatchPredictionInputRequestTypeDef",
    "S3DataSpecTypeDef",
    "CreateEvaluationInputRequestTypeDef",
    "CreateMLModelInputRequestTypeDef",
    "CreateRealtimeEndpointInputRequestTypeDef",
    "RealtimeEndpointInfoTypeDef",
    "DeleteBatchPredictionInputRequestTypeDef",
    "DeleteDataSourceInputRequestTypeDef",
    "DeleteEvaluationInputRequestTypeDef",
    "DeleteMLModelInputRequestTypeDef",
    "DeleteRealtimeEndpointInputRequestTypeDef",
    "DeleteTagsInputRequestTypeDef",
    "WaiterConfigTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeBatchPredictionsInputRequestTypeDef",
    "DescribeDataSourcesInputRequestTypeDef",
    "DescribeEvaluationsInputRequestTypeDef",
    "DescribeMLModelsInputRequestTypeDef",
    "DescribeTagsInputRequestTypeDef",
    "PerformanceMetricsTypeDef",
    "GetBatchPredictionInputRequestTypeDef",
    "GetDataSourceInputRequestTypeDef",
    "GetEvaluationInputRequestTypeDef",
    "GetMLModelInputRequestTypeDef",
    "PredictInputRequestTypeDef",
    "PredictionTypeDef",
    "RDSDatabaseCredentialsTypeDef",
    "RDSDatabaseTypeDef",
    "RedshiftDatabaseCredentialsTypeDef",
    "RedshiftDatabaseTypeDef",
    "UpdateBatchPredictionInputRequestTypeDef",
    "UpdateDataSourceInputRequestTypeDef",
    "UpdateEvaluationInputRequestTypeDef",
    "UpdateMLModelInputRequestTypeDef",
    "AddTagsInputRequestTypeDef",
    "AddTagsOutputTypeDef",
    "CreateBatchPredictionOutputTypeDef",
    "CreateDataSourceFromRDSOutputTypeDef",
    "CreateDataSourceFromRedshiftOutputTypeDef",
    "CreateDataSourceFromS3OutputTypeDef",
    "CreateEvaluationOutputTypeDef",
    "CreateMLModelOutputTypeDef",
    "DeleteBatchPredictionOutputTypeDef",
    "DeleteDataSourceOutputTypeDef",
    "DeleteEvaluationOutputTypeDef",
    "DeleteMLModelOutputTypeDef",
    "DeleteTagsOutputTypeDef",
    "DescribeTagsOutputTypeDef",
    "GetBatchPredictionOutputTypeDef",
    "UpdateBatchPredictionOutputTypeDef",
    "UpdateDataSourceOutputTypeDef",
    "UpdateEvaluationOutputTypeDef",
    "UpdateMLModelOutputTypeDef",
    "DescribeBatchPredictionsOutputTypeDef",
    "CreateDataSourceFromS3InputRequestTypeDef",
    "CreateRealtimeEndpointOutputTypeDef",
    "DeleteRealtimeEndpointOutputTypeDef",
    "GetMLModelOutputTypeDef",
    "MLModelTypeDef",
    "DescribeBatchPredictionsInputBatchPredictionAvailableWaitTypeDef",
    "DescribeDataSourcesInputDataSourceAvailableWaitTypeDef",
    "DescribeEvaluationsInputEvaluationAvailableWaitTypeDef",
    "DescribeMLModelsInputMLModelAvailableWaitTypeDef",
    "DescribeBatchPredictionsInputDescribeBatchPredictionsPaginateTypeDef",
    "DescribeDataSourcesInputDescribeDataSourcesPaginateTypeDef",
    "DescribeEvaluationsInputDescribeEvaluationsPaginateTypeDef",
    "DescribeMLModelsInputDescribeMLModelsPaginateTypeDef",
    "EvaluationTypeDef",
    "GetEvaluationOutputTypeDef",
    "PredictOutputTypeDef",
    "RDSDataSpecTypeDef",
    "RDSMetadataTypeDef",
    "RedshiftDataSpecTypeDef",
    "RedshiftMetadataTypeDef",
    "DescribeMLModelsOutputTypeDef",
    "DescribeEvaluationsOutputTypeDef",
    "CreateDataSourceFromRDSInputRequestTypeDef",
    "CreateDataSourceFromRedshiftInputRequestTypeDef",
    "DataSourceTypeDef",
    "GetDataSourceOutputTypeDef",
    "DescribeDataSourcesOutputTypeDef",
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
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
BatchPredictionTypeDef = TypedDict(
    "BatchPredictionTypeDef",
    {
        "BatchPredictionId": NotRequired[str],
        "MLModelId": NotRequired[str],
        "BatchPredictionDataSourceId": NotRequired[str],
        "InputDataLocationS3": NotRequired[str],
        "CreatedByIamUser": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "LastUpdatedAt": NotRequired[datetime],
        "Name": NotRequired[str],
        "Status": NotRequired[EntityStatusType],
        "OutputUri": NotRequired[str],
        "Message": NotRequired[str],
        "ComputeTime": NotRequired[int],
        "FinishedAt": NotRequired[datetime],
        "StartedAt": NotRequired[datetime],
        "TotalRecordCount": NotRequired[int],
        "InvalidRecordCount": NotRequired[int],
    },
)
CreateBatchPredictionInputRequestTypeDef = TypedDict(
    "CreateBatchPredictionInputRequestTypeDef",
    {
        "BatchPredictionId": str,
        "MLModelId": str,
        "BatchPredictionDataSourceId": str,
        "OutputUri": str,
        "BatchPredictionName": NotRequired[str],
    },
)
S3DataSpecTypeDef = TypedDict(
    "S3DataSpecTypeDef",
    {
        "DataLocationS3": str,
        "DataRearrangement": NotRequired[str],
        "DataSchema": NotRequired[str],
        "DataSchemaLocationS3": NotRequired[str],
    },
)
CreateEvaluationInputRequestTypeDef = TypedDict(
    "CreateEvaluationInputRequestTypeDef",
    {
        "EvaluationId": str,
        "MLModelId": str,
        "EvaluationDataSourceId": str,
        "EvaluationName": NotRequired[str],
    },
)
CreateMLModelInputRequestTypeDef = TypedDict(
    "CreateMLModelInputRequestTypeDef",
    {
        "MLModelId": str,
        "MLModelType": MLModelTypeType,
        "TrainingDataSourceId": str,
        "MLModelName": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, str]],
        "Recipe": NotRequired[str],
        "RecipeUri": NotRequired[str],
    },
)
CreateRealtimeEndpointInputRequestTypeDef = TypedDict(
    "CreateRealtimeEndpointInputRequestTypeDef",
    {
        "MLModelId": str,
    },
)
RealtimeEndpointInfoTypeDef = TypedDict(
    "RealtimeEndpointInfoTypeDef",
    {
        "PeakRequestsPerSecond": NotRequired[int],
        "CreatedAt": NotRequired[datetime],
        "EndpointUrl": NotRequired[str],
        "EndpointStatus": NotRequired[RealtimeEndpointStatusType],
    },
)
DeleteBatchPredictionInputRequestTypeDef = TypedDict(
    "DeleteBatchPredictionInputRequestTypeDef",
    {
        "BatchPredictionId": str,
    },
)
DeleteDataSourceInputRequestTypeDef = TypedDict(
    "DeleteDataSourceInputRequestTypeDef",
    {
        "DataSourceId": str,
    },
)
DeleteEvaluationInputRequestTypeDef = TypedDict(
    "DeleteEvaluationInputRequestTypeDef",
    {
        "EvaluationId": str,
    },
)
DeleteMLModelInputRequestTypeDef = TypedDict(
    "DeleteMLModelInputRequestTypeDef",
    {
        "MLModelId": str,
    },
)
DeleteRealtimeEndpointInputRequestTypeDef = TypedDict(
    "DeleteRealtimeEndpointInputRequestTypeDef",
    {
        "MLModelId": str,
    },
)
DeleteTagsInputRequestTypeDef = TypedDict(
    "DeleteTagsInputRequestTypeDef",
    {
        "TagKeys": Sequence[str],
        "ResourceId": str,
        "ResourceType": TaggableResourceTypeType,
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
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
DescribeBatchPredictionsInputRequestTypeDef = TypedDict(
    "DescribeBatchPredictionsInputRequestTypeDef",
    {
        "FilterVariable": NotRequired[BatchPredictionFilterVariableType],
        "EQ": NotRequired[str],
        "GT": NotRequired[str],
        "LT": NotRequired[str],
        "GE": NotRequired[str],
        "LE": NotRequired[str],
        "NE": NotRequired[str],
        "Prefix": NotRequired[str],
        "SortOrder": NotRequired[SortOrderType],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
DescribeDataSourcesInputRequestTypeDef = TypedDict(
    "DescribeDataSourcesInputRequestTypeDef",
    {
        "FilterVariable": NotRequired[DataSourceFilterVariableType],
        "EQ": NotRequired[str],
        "GT": NotRequired[str],
        "LT": NotRequired[str],
        "GE": NotRequired[str],
        "LE": NotRequired[str],
        "NE": NotRequired[str],
        "Prefix": NotRequired[str],
        "SortOrder": NotRequired[SortOrderType],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
DescribeEvaluationsInputRequestTypeDef = TypedDict(
    "DescribeEvaluationsInputRequestTypeDef",
    {
        "FilterVariable": NotRequired[EvaluationFilterVariableType],
        "EQ": NotRequired[str],
        "GT": NotRequired[str],
        "LT": NotRequired[str],
        "GE": NotRequired[str],
        "LE": NotRequired[str],
        "NE": NotRequired[str],
        "Prefix": NotRequired[str],
        "SortOrder": NotRequired[SortOrderType],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
DescribeMLModelsInputRequestTypeDef = TypedDict(
    "DescribeMLModelsInputRequestTypeDef",
    {
        "FilterVariable": NotRequired[MLModelFilterVariableType],
        "EQ": NotRequired[str],
        "GT": NotRequired[str],
        "LT": NotRequired[str],
        "GE": NotRequired[str],
        "LE": NotRequired[str],
        "NE": NotRequired[str],
        "Prefix": NotRequired[str],
        "SortOrder": NotRequired[SortOrderType],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
DescribeTagsInputRequestTypeDef = TypedDict(
    "DescribeTagsInputRequestTypeDef",
    {
        "ResourceId": str,
        "ResourceType": TaggableResourceTypeType,
    },
)
PerformanceMetricsTypeDef = TypedDict(
    "PerformanceMetricsTypeDef",
    {
        "Properties": NotRequired[Dict[str, str]],
    },
)
GetBatchPredictionInputRequestTypeDef = TypedDict(
    "GetBatchPredictionInputRequestTypeDef",
    {
        "BatchPredictionId": str,
    },
)
GetDataSourceInputRequestTypeDef = TypedDict(
    "GetDataSourceInputRequestTypeDef",
    {
        "DataSourceId": str,
        "Verbose": NotRequired[bool],
    },
)
GetEvaluationInputRequestTypeDef = TypedDict(
    "GetEvaluationInputRequestTypeDef",
    {
        "EvaluationId": str,
    },
)
GetMLModelInputRequestTypeDef = TypedDict(
    "GetMLModelInputRequestTypeDef",
    {
        "MLModelId": str,
        "Verbose": NotRequired[bool],
    },
)
PredictInputRequestTypeDef = TypedDict(
    "PredictInputRequestTypeDef",
    {
        "MLModelId": str,
        "Record": Mapping[str, str],
        "PredictEndpoint": str,
    },
)
PredictionTypeDef = TypedDict(
    "PredictionTypeDef",
    {
        "predictedLabel": NotRequired[str],
        "predictedValue": NotRequired[float],
        "predictedScores": NotRequired[Dict[str, float]],
        "details": NotRequired[Dict[DetailsAttributesType, str]],
    },
)
RDSDatabaseCredentialsTypeDef = TypedDict(
    "RDSDatabaseCredentialsTypeDef",
    {
        "Username": str,
        "Password": str,
    },
)
RDSDatabaseTypeDef = TypedDict(
    "RDSDatabaseTypeDef",
    {
        "InstanceIdentifier": str,
        "DatabaseName": str,
    },
)
RedshiftDatabaseCredentialsTypeDef = TypedDict(
    "RedshiftDatabaseCredentialsTypeDef",
    {
        "Username": str,
        "Password": str,
    },
)
RedshiftDatabaseTypeDef = TypedDict(
    "RedshiftDatabaseTypeDef",
    {
        "DatabaseName": str,
        "ClusterIdentifier": str,
    },
)
UpdateBatchPredictionInputRequestTypeDef = TypedDict(
    "UpdateBatchPredictionInputRequestTypeDef",
    {
        "BatchPredictionId": str,
        "BatchPredictionName": str,
    },
)
UpdateDataSourceInputRequestTypeDef = TypedDict(
    "UpdateDataSourceInputRequestTypeDef",
    {
        "DataSourceId": str,
        "DataSourceName": str,
    },
)
UpdateEvaluationInputRequestTypeDef = TypedDict(
    "UpdateEvaluationInputRequestTypeDef",
    {
        "EvaluationId": str,
        "EvaluationName": str,
    },
)
UpdateMLModelInputRequestTypeDef = TypedDict(
    "UpdateMLModelInputRequestTypeDef",
    {
        "MLModelId": str,
        "MLModelName": NotRequired[str],
        "ScoreThreshold": NotRequired[float],
    },
)
AddTagsInputRequestTypeDef = TypedDict(
    "AddTagsInputRequestTypeDef",
    {
        "Tags": Sequence[TagTypeDef],
        "ResourceId": str,
        "ResourceType": TaggableResourceTypeType,
    },
)
AddTagsOutputTypeDef = TypedDict(
    "AddTagsOutputTypeDef",
    {
        "ResourceId": str,
        "ResourceType": TaggableResourceTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateBatchPredictionOutputTypeDef = TypedDict(
    "CreateBatchPredictionOutputTypeDef",
    {
        "BatchPredictionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDataSourceFromRDSOutputTypeDef = TypedDict(
    "CreateDataSourceFromRDSOutputTypeDef",
    {
        "DataSourceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDataSourceFromRedshiftOutputTypeDef = TypedDict(
    "CreateDataSourceFromRedshiftOutputTypeDef",
    {
        "DataSourceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDataSourceFromS3OutputTypeDef = TypedDict(
    "CreateDataSourceFromS3OutputTypeDef",
    {
        "DataSourceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEvaluationOutputTypeDef = TypedDict(
    "CreateEvaluationOutputTypeDef",
    {
        "EvaluationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMLModelOutputTypeDef = TypedDict(
    "CreateMLModelOutputTypeDef",
    {
        "MLModelId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteBatchPredictionOutputTypeDef = TypedDict(
    "DeleteBatchPredictionOutputTypeDef",
    {
        "BatchPredictionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDataSourceOutputTypeDef = TypedDict(
    "DeleteDataSourceOutputTypeDef",
    {
        "DataSourceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteEvaluationOutputTypeDef = TypedDict(
    "DeleteEvaluationOutputTypeDef",
    {
        "EvaluationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteMLModelOutputTypeDef = TypedDict(
    "DeleteMLModelOutputTypeDef",
    {
        "MLModelId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTagsOutputTypeDef = TypedDict(
    "DeleteTagsOutputTypeDef",
    {
        "ResourceId": str,
        "ResourceType": TaggableResourceTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTagsOutputTypeDef = TypedDict(
    "DescribeTagsOutputTypeDef",
    {
        "ResourceId": str,
        "ResourceType": TaggableResourceTypeType,
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBatchPredictionOutputTypeDef = TypedDict(
    "GetBatchPredictionOutputTypeDef",
    {
        "BatchPredictionId": str,
        "MLModelId": str,
        "BatchPredictionDataSourceId": str,
        "InputDataLocationS3": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": EntityStatusType,
        "OutputUri": str,
        "LogUri": str,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
        "TotalRecordCount": int,
        "InvalidRecordCount": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateBatchPredictionOutputTypeDef = TypedDict(
    "UpdateBatchPredictionOutputTypeDef",
    {
        "BatchPredictionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDataSourceOutputTypeDef = TypedDict(
    "UpdateDataSourceOutputTypeDef",
    {
        "DataSourceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEvaluationOutputTypeDef = TypedDict(
    "UpdateEvaluationOutputTypeDef",
    {
        "EvaluationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateMLModelOutputTypeDef = TypedDict(
    "UpdateMLModelOutputTypeDef",
    {
        "MLModelId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeBatchPredictionsOutputTypeDef = TypedDict(
    "DescribeBatchPredictionsOutputTypeDef",
    {
        "Results": List[BatchPredictionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateDataSourceFromS3InputRequestTypeDef = TypedDict(
    "CreateDataSourceFromS3InputRequestTypeDef",
    {
        "DataSourceId": str,
        "DataSpec": S3DataSpecTypeDef,
        "DataSourceName": NotRequired[str],
        "ComputeStatistics": NotRequired[bool],
    },
)
CreateRealtimeEndpointOutputTypeDef = TypedDict(
    "CreateRealtimeEndpointOutputTypeDef",
    {
        "MLModelId": str,
        "RealtimeEndpointInfo": RealtimeEndpointInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteRealtimeEndpointOutputTypeDef = TypedDict(
    "DeleteRealtimeEndpointOutputTypeDef",
    {
        "MLModelId": str,
        "RealtimeEndpointInfo": RealtimeEndpointInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMLModelOutputTypeDef = TypedDict(
    "GetMLModelOutputTypeDef",
    {
        "MLModelId": str,
        "TrainingDataSourceId": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": EntityStatusType,
        "SizeInBytes": int,
        "EndpointInfo": RealtimeEndpointInfoTypeDef,
        "TrainingParameters": Dict[str, str],
        "InputDataLocationS3": str,
        "MLModelType": MLModelTypeType,
        "ScoreThreshold": float,
        "ScoreThresholdLastUpdatedAt": datetime,
        "LogUri": str,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
        "Recipe": str,
        "Schema": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MLModelTypeDef = TypedDict(
    "MLModelTypeDef",
    {
        "MLModelId": NotRequired[str],
        "TrainingDataSourceId": NotRequired[str],
        "CreatedByIamUser": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "LastUpdatedAt": NotRequired[datetime],
        "Name": NotRequired[str],
        "Status": NotRequired[EntityStatusType],
        "SizeInBytes": NotRequired[int],
        "EndpointInfo": NotRequired[RealtimeEndpointInfoTypeDef],
        "TrainingParameters": NotRequired[Dict[str, str]],
        "InputDataLocationS3": NotRequired[str],
        "Algorithm": NotRequired[Literal["sgd"]],
        "MLModelType": NotRequired[MLModelTypeType],
        "ScoreThreshold": NotRequired[float],
        "ScoreThresholdLastUpdatedAt": NotRequired[datetime],
        "Message": NotRequired[str],
        "ComputeTime": NotRequired[int],
        "FinishedAt": NotRequired[datetime],
        "StartedAt": NotRequired[datetime],
    },
)
DescribeBatchPredictionsInputBatchPredictionAvailableWaitTypeDef = TypedDict(
    "DescribeBatchPredictionsInputBatchPredictionAvailableWaitTypeDef",
    {
        "FilterVariable": NotRequired[BatchPredictionFilterVariableType],
        "EQ": NotRequired[str],
        "GT": NotRequired[str],
        "LT": NotRequired[str],
        "GE": NotRequired[str],
        "LE": NotRequired[str],
        "NE": NotRequired[str],
        "Prefix": NotRequired[str],
        "SortOrder": NotRequired[SortOrderType],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeDataSourcesInputDataSourceAvailableWaitTypeDef = TypedDict(
    "DescribeDataSourcesInputDataSourceAvailableWaitTypeDef",
    {
        "FilterVariable": NotRequired[DataSourceFilterVariableType],
        "EQ": NotRequired[str],
        "GT": NotRequired[str],
        "LT": NotRequired[str],
        "GE": NotRequired[str],
        "LE": NotRequired[str],
        "NE": NotRequired[str],
        "Prefix": NotRequired[str],
        "SortOrder": NotRequired[SortOrderType],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeEvaluationsInputEvaluationAvailableWaitTypeDef = TypedDict(
    "DescribeEvaluationsInputEvaluationAvailableWaitTypeDef",
    {
        "FilterVariable": NotRequired[EvaluationFilterVariableType],
        "EQ": NotRequired[str],
        "GT": NotRequired[str],
        "LT": NotRequired[str],
        "GE": NotRequired[str],
        "LE": NotRequired[str],
        "NE": NotRequired[str],
        "Prefix": NotRequired[str],
        "SortOrder": NotRequired[SortOrderType],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeMLModelsInputMLModelAvailableWaitTypeDef = TypedDict(
    "DescribeMLModelsInputMLModelAvailableWaitTypeDef",
    {
        "FilterVariable": NotRequired[MLModelFilterVariableType],
        "EQ": NotRequired[str],
        "GT": NotRequired[str],
        "LT": NotRequired[str],
        "GE": NotRequired[str],
        "LE": NotRequired[str],
        "NE": NotRequired[str],
        "Prefix": NotRequired[str],
        "SortOrder": NotRequired[SortOrderType],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeBatchPredictionsInputDescribeBatchPredictionsPaginateTypeDef = TypedDict(
    "DescribeBatchPredictionsInputDescribeBatchPredictionsPaginateTypeDef",
    {
        "FilterVariable": NotRequired[BatchPredictionFilterVariableType],
        "EQ": NotRequired[str],
        "GT": NotRequired[str],
        "LT": NotRequired[str],
        "GE": NotRequired[str],
        "LE": NotRequired[str],
        "NE": NotRequired[str],
        "Prefix": NotRequired[str],
        "SortOrder": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDataSourcesInputDescribeDataSourcesPaginateTypeDef = TypedDict(
    "DescribeDataSourcesInputDescribeDataSourcesPaginateTypeDef",
    {
        "FilterVariable": NotRequired[DataSourceFilterVariableType],
        "EQ": NotRequired[str],
        "GT": NotRequired[str],
        "LT": NotRequired[str],
        "GE": NotRequired[str],
        "LE": NotRequired[str],
        "NE": NotRequired[str],
        "Prefix": NotRequired[str],
        "SortOrder": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEvaluationsInputDescribeEvaluationsPaginateTypeDef = TypedDict(
    "DescribeEvaluationsInputDescribeEvaluationsPaginateTypeDef",
    {
        "FilterVariable": NotRequired[EvaluationFilterVariableType],
        "EQ": NotRequired[str],
        "GT": NotRequired[str],
        "LT": NotRequired[str],
        "GE": NotRequired[str],
        "LE": NotRequired[str],
        "NE": NotRequired[str],
        "Prefix": NotRequired[str],
        "SortOrder": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeMLModelsInputDescribeMLModelsPaginateTypeDef = TypedDict(
    "DescribeMLModelsInputDescribeMLModelsPaginateTypeDef",
    {
        "FilterVariable": NotRequired[MLModelFilterVariableType],
        "EQ": NotRequired[str],
        "GT": NotRequired[str],
        "LT": NotRequired[str],
        "GE": NotRequired[str],
        "LE": NotRequired[str],
        "NE": NotRequired[str],
        "Prefix": NotRequired[str],
        "SortOrder": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
EvaluationTypeDef = TypedDict(
    "EvaluationTypeDef",
    {
        "EvaluationId": NotRequired[str],
        "MLModelId": NotRequired[str],
        "EvaluationDataSourceId": NotRequired[str],
        "InputDataLocationS3": NotRequired[str],
        "CreatedByIamUser": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "LastUpdatedAt": NotRequired[datetime],
        "Name": NotRequired[str],
        "Status": NotRequired[EntityStatusType],
        "PerformanceMetrics": NotRequired[PerformanceMetricsTypeDef],
        "Message": NotRequired[str],
        "ComputeTime": NotRequired[int],
        "FinishedAt": NotRequired[datetime],
        "StartedAt": NotRequired[datetime],
    },
)
GetEvaluationOutputTypeDef = TypedDict(
    "GetEvaluationOutputTypeDef",
    {
        "EvaluationId": str,
        "MLModelId": str,
        "EvaluationDataSourceId": str,
        "InputDataLocationS3": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": EntityStatusType,
        "PerformanceMetrics": PerformanceMetricsTypeDef,
        "LogUri": str,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PredictOutputTypeDef = TypedDict(
    "PredictOutputTypeDef",
    {
        "Prediction": PredictionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RDSDataSpecTypeDef = TypedDict(
    "RDSDataSpecTypeDef",
    {
        "DatabaseInformation": RDSDatabaseTypeDef,
        "SelectSqlQuery": str,
        "DatabaseCredentials": RDSDatabaseCredentialsTypeDef,
        "S3StagingLocation": str,
        "ResourceRole": str,
        "ServiceRole": str,
        "SubnetId": str,
        "SecurityGroupIds": Sequence[str],
        "DataRearrangement": NotRequired[str],
        "DataSchema": NotRequired[str],
        "DataSchemaUri": NotRequired[str],
    },
)
RDSMetadataTypeDef = TypedDict(
    "RDSMetadataTypeDef",
    {
        "Database": NotRequired[RDSDatabaseTypeDef],
        "DatabaseUserName": NotRequired[str],
        "SelectSqlQuery": NotRequired[str],
        "ResourceRole": NotRequired[str],
        "ServiceRole": NotRequired[str],
        "DataPipelineId": NotRequired[str],
    },
)
RedshiftDataSpecTypeDef = TypedDict(
    "RedshiftDataSpecTypeDef",
    {
        "DatabaseInformation": RedshiftDatabaseTypeDef,
        "SelectSqlQuery": str,
        "DatabaseCredentials": RedshiftDatabaseCredentialsTypeDef,
        "S3StagingLocation": str,
        "DataRearrangement": NotRequired[str],
        "DataSchema": NotRequired[str],
        "DataSchemaUri": NotRequired[str],
    },
)
RedshiftMetadataTypeDef = TypedDict(
    "RedshiftMetadataTypeDef",
    {
        "RedshiftDatabase": NotRequired[RedshiftDatabaseTypeDef],
        "DatabaseUserName": NotRequired[str],
        "SelectSqlQuery": NotRequired[str],
    },
)
DescribeMLModelsOutputTypeDef = TypedDict(
    "DescribeMLModelsOutputTypeDef",
    {
        "Results": List[MLModelTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeEvaluationsOutputTypeDef = TypedDict(
    "DescribeEvaluationsOutputTypeDef",
    {
        "Results": List[EvaluationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateDataSourceFromRDSInputRequestTypeDef = TypedDict(
    "CreateDataSourceFromRDSInputRequestTypeDef",
    {
        "DataSourceId": str,
        "RDSData": RDSDataSpecTypeDef,
        "RoleARN": str,
        "DataSourceName": NotRequired[str],
        "ComputeStatistics": NotRequired[bool],
    },
)
CreateDataSourceFromRedshiftInputRequestTypeDef = TypedDict(
    "CreateDataSourceFromRedshiftInputRequestTypeDef",
    {
        "DataSourceId": str,
        "DataSpec": RedshiftDataSpecTypeDef,
        "RoleARN": str,
        "DataSourceName": NotRequired[str],
        "ComputeStatistics": NotRequired[bool],
    },
)
DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "DataSourceId": NotRequired[str],
        "DataLocationS3": NotRequired[str],
        "DataRearrangement": NotRequired[str],
        "CreatedByIamUser": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "LastUpdatedAt": NotRequired[datetime],
        "DataSizeInBytes": NotRequired[int],
        "NumberOfFiles": NotRequired[int],
        "Name": NotRequired[str],
        "Status": NotRequired[EntityStatusType],
        "Message": NotRequired[str],
        "RedshiftMetadata": NotRequired[RedshiftMetadataTypeDef],
        "RDSMetadata": NotRequired[RDSMetadataTypeDef],
        "RoleARN": NotRequired[str],
        "ComputeStatistics": NotRequired[bool],
        "ComputeTime": NotRequired[int],
        "FinishedAt": NotRequired[datetime],
        "StartedAt": NotRequired[datetime],
    },
)
GetDataSourceOutputTypeDef = TypedDict(
    "GetDataSourceOutputTypeDef",
    {
        "DataSourceId": str,
        "DataLocationS3": str,
        "DataRearrangement": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "DataSizeInBytes": int,
        "NumberOfFiles": int,
        "Name": str,
        "Status": EntityStatusType,
        "LogUri": str,
        "Message": str,
        "RedshiftMetadata": RedshiftMetadataTypeDef,
        "RDSMetadata": RDSMetadataTypeDef,
        "RoleARN": str,
        "ComputeStatistics": bool,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
        "DataSourceSchema": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDataSourcesOutputTypeDef = TypedDict(
    "DescribeDataSourcesOutputTypeDef",
    {
        "Results": List[DataSourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
