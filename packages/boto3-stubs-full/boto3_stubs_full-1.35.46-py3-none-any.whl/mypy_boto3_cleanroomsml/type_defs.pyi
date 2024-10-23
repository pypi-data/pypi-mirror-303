"""
Type annotations for cleanroomsml service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/type_defs/)

Usage::

    ```python
    from mypy_boto3_cleanroomsml.type_defs import S3ConfigMapTypeDef

    data: S3ConfigMapTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AudienceExportJobStatusType,
    AudienceGenerationJobStatusType,
    AudienceModelStatusType,
    AudienceSizeTypeType,
    ColumnTypeType,
    PolicyExistenceConditionType,
    SharedAudienceMetricsType,
    TagOnCreatePolicyType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "S3ConfigMapTypeDef",
    "AudienceSizeTypeDef",
    "StatusDetailsTypeDef",
    "ProtectedQuerySQLParametersOutputTypeDef",
    "AudienceGenerationJobSummaryTypeDef",
    "AudienceModelSummaryTypeDef",
    "AudienceSizeConfigOutputTypeDef",
    "AudienceSizeConfigTypeDef",
    "ColumnSchemaOutputTypeDef",
    "ColumnSchemaTypeDef",
    "TimestampTypeDef",
    "ResponseMetadataTypeDef",
    "GlueDataSourceTypeDef",
    "DeleteAudienceGenerationJobRequestRequestTypeDef",
    "DeleteAudienceModelRequestRequestTypeDef",
    "DeleteConfiguredAudienceModelPolicyRequestRequestTypeDef",
    "DeleteConfiguredAudienceModelRequestRequestTypeDef",
    "DeleteTrainingDatasetRequestRequestTypeDef",
    "GetAudienceGenerationJobRequestRequestTypeDef",
    "GetAudienceModelRequestRequestTypeDef",
    "GetConfiguredAudienceModelPolicyRequestRequestTypeDef",
    "GetConfiguredAudienceModelRequestRequestTypeDef",
    "GetTrainingDatasetRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListAudienceExportJobsRequestRequestTypeDef",
    "ListAudienceGenerationJobsRequestRequestTypeDef",
    "ListAudienceModelsRequestRequestTypeDef",
    "ListConfiguredAudienceModelsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTrainingDatasetsRequestRequestTypeDef",
    "TrainingDatasetSummaryTypeDef",
    "ProtectedQuerySQLParametersTypeDef",
    "PutConfiguredAudienceModelPolicyRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "AudienceDestinationTypeDef",
    "RelevanceMetricTypeDef",
    "StartAudienceExportJobRequestRequestTypeDef",
    "AudienceExportJobSummaryTypeDef",
    "AudienceGenerationJobDataSourceOutputTypeDef",
    "ColumnSchemaUnionTypeDef",
    "CreateAudienceModelRequestRequestTypeDef",
    "CreateAudienceModelResponseTypeDef",
    "CreateConfiguredAudienceModelResponseTypeDef",
    "CreateTrainingDatasetResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetAudienceModelResponseTypeDef",
    "GetConfiguredAudienceModelPolicyResponseTypeDef",
    "ListAudienceGenerationJobsResponseTypeDef",
    "ListAudienceModelsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PutConfiguredAudienceModelPolicyResponseTypeDef",
    "StartAudienceGenerationJobResponseTypeDef",
    "UpdateConfiguredAudienceModelResponseTypeDef",
    "DataSourceTypeDef",
    "ListAudienceExportJobsRequestListAudienceExportJobsPaginateTypeDef",
    "ListAudienceGenerationJobsRequestListAudienceGenerationJobsPaginateTypeDef",
    "ListAudienceModelsRequestListAudienceModelsPaginateTypeDef",
    "ListConfiguredAudienceModelsRequestListConfiguredAudienceModelsPaginateTypeDef",
    "ListTrainingDatasetsRequestListTrainingDatasetsPaginateTypeDef",
    "ListTrainingDatasetsResponseTypeDef",
    "ProtectedQuerySQLParametersUnionTypeDef",
    "ConfiguredAudienceModelOutputConfigTypeDef",
    "AudienceQualityMetricsTypeDef",
    "ListAudienceExportJobsResponseTypeDef",
    "DatasetInputConfigOutputTypeDef",
    "DatasetInputConfigTypeDef",
    "AudienceGenerationJobDataSourceTypeDef",
    "ConfiguredAudienceModelSummaryTypeDef",
    "CreateConfiguredAudienceModelRequestRequestTypeDef",
    "GetConfiguredAudienceModelResponseTypeDef",
    "UpdateConfiguredAudienceModelRequestRequestTypeDef",
    "GetAudienceGenerationJobResponseTypeDef",
    "DatasetOutputTypeDef",
    "DatasetInputConfigUnionTypeDef",
    "StartAudienceGenerationJobRequestRequestTypeDef",
    "ListConfiguredAudienceModelsResponseTypeDef",
    "GetTrainingDatasetResponseTypeDef",
    "DatasetTypeDef",
    "DatasetUnionTypeDef",
    "CreateTrainingDatasetRequestRequestTypeDef",
)

S3ConfigMapTypeDef = TypedDict(
    "S3ConfigMapTypeDef",
    {
        "s3Uri": str,
    },
)
AudienceSizeTypeDef = TypedDict(
    "AudienceSizeTypeDef",
    {
        "type": AudienceSizeTypeType,
        "value": int,
    },
)
StatusDetailsTypeDef = TypedDict(
    "StatusDetailsTypeDef",
    {
        "statusCode": NotRequired[str],
        "message": NotRequired[str],
    },
)
ProtectedQuerySQLParametersOutputTypeDef = TypedDict(
    "ProtectedQuerySQLParametersOutputTypeDef",
    {
        "queryString": NotRequired[str],
        "analysisTemplateArn": NotRequired[str],
        "parameters": NotRequired[Dict[str, str]],
    },
)
AudienceGenerationJobSummaryTypeDef = TypedDict(
    "AudienceGenerationJobSummaryTypeDef",
    {
        "createTime": datetime,
        "updateTime": datetime,
        "audienceGenerationJobArn": str,
        "name": str,
        "status": AudienceGenerationJobStatusType,
        "configuredAudienceModelArn": str,
        "description": NotRequired[str],
        "collaborationId": NotRequired[str],
        "startedBy": NotRequired[str],
    },
)
AudienceModelSummaryTypeDef = TypedDict(
    "AudienceModelSummaryTypeDef",
    {
        "createTime": datetime,
        "updateTime": datetime,
        "audienceModelArn": str,
        "name": str,
        "trainingDatasetArn": str,
        "status": AudienceModelStatusType,
        "description": NotRequired[str],
    },
)
AudienceSizeConfigOutputTypeDef = TypedDict(
    "AudienceSizeConfigOutputTypeDef",
    {
        "audienceSizeType": AudienceSizeTypeType,
        "audienceSizeBins": List[int],
    },
)
AudienceSizeConfigTypeDef = TypedDict(
    "AudienceSizeConfigTypeDef",
    {
        "audienceSizeType": AudienceSizeTypeType,
        "audienceSizeBins": Sequence[int],
    },
)
ColumnSchemaOutputTypeDef = TypedDict(
    "ColumnSchemaOutputTypeDef",
    {
        "columnName": str,
        "columnTypes": List[ColumnTypeType],
    },
)
ColumnSchemaTypeDef = TypedDict(
    "ColumnSchemaTypeDef",
    {
        "columnName": str,
        "columnTypes": Sequence[ColumnTypeType],
    },
)
TimestampTypeDef = Union[datetime, str]
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
GlueDataSourceTypeDef = TypedDict(
    "GlueDataSourceTypeDef",
    {
        "tableName": str,
        "databaseName": str,
        "catalogId": NotRequired[str],
    },
)
DeleteAudienceGenerationJobRequestRequestTypeDef = TypedDict(
    "DeleteAudienceGenerationJobRequestRequestTypeDef",
    {
        "audienceGenerationJobArn": str,
    },
)
DeleteAudienceModelRequestRequestTypeDef = TypedDict(
    "DeleteAudienceModelRequestRequestTypeDef",
    {
        "audienceModelArn": str,
    },
)
DeleteConfiguredAudienceModelPolicyRequestRequestTypeDef = TypedDict(
    "DeleteConfiguredAudienceModelPolicyRequestRequestTypeDef",
    {
        "configuredAudienceModelArn": str,
    },
)
DeleteConfiguredAudienceModelRequestRequestTypeDef = TypedDict(
    "DeleteConfiguredAudienceModelRequestRequestTypeDef",
    {
        "configuredAudienceModelArn": str,
    },
)
DeleteTrainingDatasetRequestRequestTypeDef = TypedDict(
    "DeleteTrainingDatasetRequestRequestTypeDef",
    {
        "trainingDatasetArn": str,
    },
)
GetAudienceGenerationJobRequestRequestTypeDef = TypedDict(
    "GetAudienceGenerationJobRequestRequestTypeDef",
    {
        "audienceGenerationJobArn": str,
    },
)
GetAudienceModelRequestRequestTypeDef = TypedDict(
    "GetAudienceModelRequestRequestTypeDef",
    {
        "audienceModelArn": str,
    },
)
GetConfiguredAudienceModelPolicyRequestRequestTypeDef = TypedDict(
    "GetConfiguredAudienceModelPolicyRequestRequestTypeDef",
    {
        "configuredAudienceModelArn": str,
    },
)
GetConfiguredAudienceModelRequestRequestTypeDef = TypedDict(
    "GetConfiguredAudienceModelRequestRequestTypeDef",
    {
        "configuredAudienceModelArn": str,
    },
)
GetTrainingDatasetRequestRequestTypeDef = TypedDict(
    "GetTrainingDatasetRequestRequestTypeDef",
    {
        "trainingDatasetArn": str,
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
ListAudienceExportJobsRequestRequestTypeDef = TypedDict(
    "ListAudienceExportJobsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "audienceGenerationJobArn": NotRequired[str],
    },
)
ListAudienceGenerationJobsRequestRequestTypeDef = TypedDict(
    "ListAudienceGenerationJobsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "configuredAudienceModelArn": NotRequired[str],
        "collaborationId": NotRequired[str],
    },
)
ListAudienceModelsRequestRequestTypeDef = TypedDict(
    "ListAudienceModelsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListConfiguredAudienceModelsRequestRequestTypeDef = TypedDict(
    "ListConfiguredAudienceModelsRequestRequestTypeDef",
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
ListTrainingDatasetsRequestRequestTypeDef = TypedDict(
    "ListTrainingDatasetsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
TrainingDatasetSummaryTypeDef = TypedDict(
    "TrainingDatasetSummaryTypeDef",
    {
        "createTime": datetime,
        "updateTime": datetime,
        "trainingDatasetArn": str,
        "name": str,
        "status": Literal["ACTIVE"],
        "description": NotRequired[str],
    },
)
ProtectedQuerySQLParametersTypeDef = TypedDict(
    "ProtectedQuerySQLParametersTypeDef",
    {
        "queryString": NotRequired[str],
        "analysisTemplateArn": NotRequired[str],
        "parameters": NotRequired[Mapping[str, str]],
    },
)
PutConfiguredAudienceModelPolicyRequestRequestTypeDef = TypedDict(
    "PutConfiguredAudienceModelPolicyRequestRequestTypeDef",
    {
        "configuredAudienceModelArn": str,
        "configuredAudienceModelPolicy": str,
        "previousPolicyHash": NotRequired[str],
        "policyExistenceCondition": NotRequired[PolicyExistenceConditionType],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
AudienceDestinationTypeDef = TypedDict(
    "AudienceDestinationTypeDef",
    {
        "s3Destination": S3ConfigMapTypeDef,
    },
)
RelevanceMetricTypeDef = TypedDict(
    "RelevanceMetricTypeDef",
    {
        "audienceSize": AudienceSizeTypeDef,
        "score": NotRequired[float],
    },
)
StartAudienceExportJobRequestRequestTypeDef = TypedDict(
    "StartAudienceExportJobRequestRequestTypeDef",
    {
        "name": str,
        "audienceGenerationJobArn": str,
        "audienceSize": AudienceSizeTypeDef,
        "description": NotRequired[str],
    },
)
AudienceExportJobSummaryTypeDef = TypedDict(
    "AudienceExportJobSummaryTypeDef",
    {
        "createTime": datetime,
        "updateTime": datetime,
        "name": str,
        "audienceGenerationJobArn": str,
        "audienceSize": AudienceSizeTypeDef,
        "status": AudienceExportJobStatusType,
        "description": NotRequired[str],
        "statusDetails": NotRequired[StatusDetailsTypeDef],
        "outputLocation": NotRequired[str],
    },
)
AudienceGenerationJobDataSourceOutputTypeDef = TypedDict(
    "AudienceGenerationJobDataSourceOutputTypeDef",
    {
        "roleArn": str,
        "dataSource": NotRequired[S3ConfigMapTypeDef],
        "sqlParameters": NotRequired[ProtectedQuerySQLParametersOutputTypeDef],
    },
)
ColumnSchemaUnionTypeDef = Union[ColumnSchemaTypeDef, ColumnSchemaOutputTypeDef]
CreateAudienceModelRequestRequestTypeDef = TypedDict(
    "CreateAudienceModelRequestRequestTypeDef",
    {
        "name": str,
        "trainingDatasetArn": str,
        "trainingDataStartTime": NotRequired[TimestampTypeDef],
        "trainingDataEndTime": NotRequired[TimestampTypeDef],
        "kmsKeyArn": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "description": NotRequired[str],
    },
)
CreateAudienceModelResponseTypeDef = TypedDict(
    "CreateAudienceModelResponseTypeDef",
    {
        "audienceModelArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateConfiguredAudienceModelResponseTypeDef = TypedDict(
    "CreateConfiguredAudienceModelResponseTypeDef",
    {
        "configuredAudienceModelArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTrainingDatasetResponseTypeDef = TypedDict(
    "CreateTrainingDatasetResponseTypeDef",
    {
        "trainingDatasetArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAudienceModelResponseTypeDef = TypedDict(
    "GetAudienceModelResponseTypeDef",
    {
        "createTime": datetime,
        "updateTime": datetime,
        "trainingDataStartTime": datetime,
        "trainingDataEndTime": datetime,
        "audienceModelArn": str,
        "name": str,
        "trainingDatasetArn": str,
        "status": AudienceModelStatusType,
        "statusDetails": StatusDetailsTypeDef,
        "kmsKeyArn": str,
        "tags": Dict[str, str],
        "description": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetConfiguredAudienceModelPolicyResponseTypeDef = TypedDict(
    "GetConfiguredAudienceModelPolicyResponseTypeDef",
    {
        "configuredAudienceModelArn": str,
        "configuredAudienceModelPolicy": str,
        "policyHash": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAudienceGenerationJobsResponseTypeDef = TypedDict(
    "ListAudienceGenerationJobsResponseTypeDef",
    {
        "nextToken": str,
        "audienceGenerationJobs": List[AudienceGenerationJobSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAudienceModelsResponseTypeDef = TypedDict(
    "ListAudienceModelsResponseTypeDef",
    {
        "nextToken": str,
        "audienceModels": List[AudienceModelSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutConfiguredAudienceModelPolicyResponseTypeDef = TypedDict(
    "PutConfiguredAudienceModelPolicyResponseTypeDef",
    {
        "configuredAudienceModelPolicy": str,
        "policyHash": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartAudienceGenerationJobResponseTypeDef = TypedDict(
    "StartAudienceGenerationJobResponseTypeDef",
    {
        "audienceGenerationJobArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateConfiguredAudienceModelResponseTypeDef = TypedDict(
    "UpdateConfiguredAudienceModelResponseTypeDef",
    {
        "configuredAudienceModelArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "glueDataSource": GlueDataSourceTypeDef,
    },
)
ListAudienceExportJobsRequestListAudienceExportJobsPaginateTypeDef = TypedDict(
    "ListAudienceExportJobsRequestListAudienceExportJobsPaginateTypeDef",
    {
        "audienceGenerationJobArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAudienceGenerationJobsRequestListAudienceGenerationJobsPaginateTypeDef = TypedDict(
    "ListAudienceGenerationJobsRequestListAudienceGenerationJobsPaginateTypeDef",
    {
        "configuredAudienceModelArn": NotRequired[str],
        "collaborationId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAudienceModelsRequestListAudienceModelsPaginateTypeDef = TypedDict(
    "ListAudienceModelsRequestListAudienceModelsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListConfiguredAudienceModelsRequestListConfiguredAudienceModelsPaginateTypeDef = TypedDict(
    "ListConfiguredAudienceModelsRequestListConfiguredAudienceModelsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTrainingDatasetsRequestListTrainingDatasetsPaginateTypeDef = TypedDict(
    "ListTrainingDatasetsRequestListTrainingDatasetsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTrainingDatasetsResponseTypeDef = TypedDict(
    "ListTrainingDatasetsResponseTypeDef",
    {
        "nextToken": str,
        "trainingDatasets": List[TrainingDatasetSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProtectedQuerySQLParametersUnionTypeDef = Union[
    ProtectedQuerySQLParametersTypeDef, ProtectedQuerySQLParametersOutputTypeDef
]
ConfiguredAudienceModelOutputConfigTypeDef = TypedDict(
    "ConfiguredAudienceModelOutputConfigTypeDef",
    {
        "destination": AudienceDestinationTypeDef,
        "roleArn": str,
    },
)
AudienceQualityMetricsTypeDef = TypedDict(
    "AudienceQualityMetricsTypeDef",
    {
        "relevanceMetrics": List[RelevanceMetricTypeDef],
        "recallMetric": NotRequired[float],
    },
)
ListAudienceExportJobsResponseTypeDef = TypedDict(
    "ListAudienceExportJobsResponseTypeDef",
    {
        "nextToken": str,
        "audienceExportJobs": List[AudienceExportJobSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DatasetInputConfigOutputTypeDef = TypedDict(
    "DatasetInputConfigOutputTypeDef",
    {
        "schema": List[ColumnSchemaOutputTypeDef],
        "dataSource": DataSourceTypeDef,
    },
)
DatasetInputConfigTypeDef = TypedDict(
    "DatasetInputConfigTypeDef",
    {
        "schema": Sequence[ColumnSchemaUnionTypeDef],
        "dataSource": DataSourceTypeDef,
    },
)
AudienceGenerationJobDataSourceTypeDef = TypedDict(
    "AudienceGenerationJobDataSourceTypeDef",
    {
        "roleArn": str,
        "dataSource": NotRequired[S3ConfigMapTypeDef],
        "sqlParameters": NotRequired[ProtectedQuerySQLParametersUnionTypeDef],
    },
)
ConfiguredAudienceModelSummaryTypeDef = TypedDict(
    "ConfiguredAudienceModelSummaryTypeDef",
    {
        "createTime": datetime,
        "updateTime": datetime,
        "name": str,
        "audienceModelArn": str,
        "outputConfig": ConfiguredAudienceModelOutputConfigTypeDef,
        "configuredAudienceModelArn": str,
        "status": Literal["ACTIVE"],
        "description": NotRequired[str],
    },
)
CreateConfiguredAudienceModelRequestRequestTypeDef = TypedDict(
    "CreateConfiguredAudienceModelRequestRequestTypeDef",
    {
        "name": str,
        "audienceModelArn": str,
        "outputConfig": ConfiguredAudienceModelOutputConfigTypeDef,
        "sharedAudienceMetrics": Sequence[SharedAudienceMetricsType],
        "description": NotRequired[str],
        "minMatchingSeedSize": NotRequired[int],
        "audienceSizeConfig": NotRequired[AudienceSizeConfigTypeDef],
        "tags": NotRequired[Mapping[str, str]],
        "childResourceTagOnCreatePolicy": NotRequired[TagOnCreatePolicyType],
    },
)
GetConfiguredAudienceModelResponseTypeDef = TypedDict(
    "GetConfiguredAudienceModelResponseTypeDef",
    {
        "createTime": datetime,
        "updateTime": datetime,
        "configuredAudienceModelArn": str,
        "name": str,
        "audienceModelArn": str,
        "outputConfig": ConfiguredAudienceModelOutputConfigTypeDef,
        "description": str,
        "status": Literal["ACTIVE"],
        "sharedAudienceMetrics": List[SharedAudienceMetricsType],
        "minMatchingSeedSize": int,
        "audienceSizeConfig": AudienceSizeConfigOutputTypeDef,
        "tags": Dict[str, str],
        "childResourceTagOnCreatePolicy": TagOnCreatePolicyType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateConfiguredAudienceModelRequestRequestTypeDef = TypedDict(
    "UpdateConfiguredAudienceModelRequestRequestTypeDef",
    {
        "configuredAudienceModelArn": str,
        "outputConfig": NotRequired[ConfiguredAudienceModelOutputConfigTypeDef],
        "audienceModelArn": NotRequired[str],
        "sharedAudienceMetrics": NotRequired[Sequence[SharedAudienceMetricsType]],
        "minMatchingSeedSize": NotRequired[int],
        "audienceSizeConfig": NotRequired[AudienceSizeConfigTypeDef],
        "description": NotRequired[str],
    },
)
GetAudienceGenerationJobResponseTypeDef = TypedDict(
    "GetAudienceGenerationJobResponseTypeDef",
    {
        "createTime": datetime,
        "updateTime": datetime,
        "audienceGenerationJobArn": str,
        "name": str,
        "description": str,
        "status": AudienceGenerationJobStatusType,
        "statusDetails": StatusDetailsTypeDef,
        "configuredAudienceModelArn": str,
        "seedAudience": AudienceGenerationJobDataSourceOutputTypeDef,
        "includeSeedInOutput": bool,
        "collaborationId": str,
        "metrics": AudienceQualityMetricsTypeDef,
        "startedBy": str,
        "tags": Dict[str, str],
        "protectedQueryIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DatasetOutputTypeDef = TypedDict(
    "DatasetOutputTypeDef",
    {
        "type": Literal["INTERACTIONS"],
        "inputConfig": DatasetInputConfigOutputTypeDef,
    },
)
DatasetInputConfigUnionTypeDef = Union[DatasetInputConfigTypeDef, DatasetInputConfigOutputTypeDef]
StartAudienceGenerationJobRequestRequestTypeDef = TypedDict(
    "StartAudienceGenerationJobRequestRequestTypeDef",
    {
        "name": str,
        "configuredAudienceModelArn": str,
        "seedAudience": AudienceGenerationJobDataSourceTypeDef,
        "includeSeedInOutput": NotRequired[bool],
        "collaborationId": NotRequired[str],
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
ListConfiguredAudienceModelsResponseTypeDef = TypedDict(
    "ListConfiguredAudienceModelsResponseTypeDef",
    {
        "nextToken": str,
        "configuredAudienceModels": List[ConfiguredAudienceModelSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTrainingDatasetResponseTypeDef = TypedDict(
    "GetTrainingDatasetResponseTypeDef",
    {
        "createTime": datetime,
        "updateTime": datetime,
        "trainingDatasetArn": str,
        "name": str,
        "trainingData": List[DatasetOutputTypeDef],
        "status": Literal["ACTIVE"],
        "roleArn": str,
        "tags": Dict[str, str],
        "description": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DatasetTypeDef = TypedDict(
    "DatasetTypeDef",
    {
        "type": Literal["INTERACTIONS"],
        "inputConfig": DatasetInputConfigUnionTypeDef,
    },
)
DatasetUnionTypeDef = Union[DatasetTypeDef, DatasetOutputTypeDef]
CreateTrainingDatasetRequestRequestTypeDef = TypedDict(
    "CreateTrainingDatasetRequestRequestTypeDef",
    {
        "name": str,
        "roleArn": str,
        "trainingData": Sequence[DatasetUnionTypeDef],
        "tags": NotRequired[Mapping[str, str]],
        "description": NotRequired[str],
    },
)
