"""
Type annotations for frauddetector service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/type_defs/)

Usage::

    ```python
    from mypy_boto3_frauddetector.type_defs import ATIMetricDataPointTypeDef

    data: ATIMetricDataPointTypeDef = ...
    ```
"""

import sys
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    AsyncJobStatusType,
    DataSourceType,
    DataTypeType,
    DetectorVersionStatusType,
    EventIngestionType,
    ListUpdateModeType,
    ModelEndpointStatusType,
    ModelInputDataFormatType,
    ModelOutputDataFormatType,
    ModelTypeEnumType,
    ModelVersionStatusType,
    RuleExecutionModeType,
    TrainingDataSourceEnumType,
    UnlabeledEventsTreatmentType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "ATIMetricDataPointTypeDef",
    "ATIModelPerformanceTypeDef",
    "AggregatedLogOddsMetricTypeDef",
    "AggregatedVariablesImpactExplanationTypeDef",
    "AllowDenyListTypeDef",
    "BatchCreateVariableErrorTypeDef",
    "TagTypeDef",
    "VariableEntryTypeDef",
    "ResponseMetadataTypeDef",
    "BatchGetVariableErrorTypeDef",
    "BatchGetVariableRequestRequestTypeDef",
    "VariableTypeDef",
    "BatchImportTypeDef",
    "BatchPredictionTypeDef",
    "BlobTypeDef",
    "CancelBatchImportJobRequestRequestTypeDef",
    "CancelBatchPredictionJobRequestRequestTypeDef",
    "ModelVersionTypeDef",
    "RuleTypeDef",
    "ExternalEventsDetailTypeDef",
    "FieldValidationMessageTypeDef",
    "FileValidationMessageTypeDef",
    "DeleteBatchImportJobRequestRequestTypeDef",
    "DeleteBatchPredictionJobRequestRequestTypeDef",
    "DeleteDetectorRequestRequestTypeDef",
    "DeleteDetectorVersionRequestRequestTypeDef",
    "DeleteEntityTypeRequestRequestTypeDef",
    "DeleteEventRequestRequestTypeDef",
    "DeleteEventTypeRequestRequestTypeDef",
    "DeleteEventsByEventTypeRequestRequestTypeDef",
    "DeleteExternalModelRequestRequestTypeDef",
    "DeleteLabelRequestRequestTypeDef",
    "DeleteListRequestRequestTypeDef",
    "DeleteModelRequestRequestTypeDef",
    "DeleteModelVersionRequestRequestTypeDef",
    "DeleteOutcomeRequestRequestTypeDef",
    "DeleteVariableRequestRequestTypeDef",
    "DescribeDetectorRequestRequestTypeDef",
    "DetectorVersionSummaryTypeDef",
    "DescribeModelVersionsRequestRequestTypeDef",
    "DetectorTypeDef",
    "EntityTypeDef",
    "EntityTypeTypeDef",
    "EvaluatedExternalModelTypeDef",
    "EvaluatedRuleTypeDef",
    "EventOrchestrationTypeDef",
    "EventPredictionSummaryTypeDef",
    "IngestedEventStatisticsTypeDef",
    "EventVariableSummaryTypeDef",
    "ExternalModelSummaryTypeDef",
    "ModelInputConfigurationTypeDef",
    "ModelOutputConfigurationOutputTypeDef",
    "FilterConditionTypeDef",
    "GetBatchImportJobsRequestRequestTypeDef",
    "GetBatchPredictionJobsRequestRequestTypeDef",
    "GetDeleteEventsByEventTypeStatusRequestRequestTypeDef",
    "GetDetectorVersionRequestRequestTypeDef",
    "GetDetectorsRequestRequestTypeDef",
    "GetEntityTypesRequestRequestTypeDef",
    "GetEventPredictionMetadataRequestRequestTypeDef",
    "RuleResultTypeDef",
    "GetEventRequestRequestTypeDef",
    "GetEventTypesRequestRequestTypeDef",
    "GetExternalModelsRequestRequestTypeDef",
    "KMSKeyTypeDef",
    "GetLabelsRequestRequestTypeDef",
    "LabelTypeDef",
    "GetListElementsRequestRequestTypeDef",
    "GetListsMetadataRequestRequestTypeDef",
    "GetModelVersionRequestRequestTypeDef",
    "GetModelsRequestRequestTypeDef",
    "ModelTypeDef",
    "GetOutcomesRequestRequestTypeDef",
    "OutcomeTypeDef",
    "GetRulesRequestRequestTypeDef",
    "RuleDetailTypeDef",
    "GetVariablesRequestRequestTypeDef",
    "IngestedEventsTimeWindowTypeDef",
    "LabelSchemaOutputTypeDef",
    "LabelSchemaTypeDef",
    "PredictionTimeRangeTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "LogOddsMetricTypeDef",
    "MetricDataPointTypeDef",
    "ModelOutputConfigurationTypeDef",
    "OFIMetricDataPointTypeDef",
    "UncertaintyRangeTypeDef",
    "VariableImpactExplanationTypeDef",
    "PutKMSEncryptionKeyRequestRequestTypeDef",
    "TFIMetricDataPointTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDetectorVersionMetadataRequestRequestTypeDef",
    "UpdateDetectorVersionStatusRequestRequestTypeDef",
    "UpdateEventLabelRequestRequestTypeDef",
    "UpdateListRequestRequestTypeDef",
    "UpdateModelRequestRequestTypeDef",
    "UpdateModelVersionStatusRequestRequestTypeDef",
    "UpdateVariableRequestRequestTypeDef",
    "ATITrainingMetricsValueTypeDef",
    "AggregatedVariablesImportanceMetricsTypeDef",
    "CreateBatchImportJobRequestRequestTypeDef",
    "CreateBatchPredictionJobRequestRequestTypeDef",
    "CreateListRequestRequestTypeDef",
    "CreateModelRequestRequestTypeDef",
    "CreateRuleRequestRequestTypeDef",
    "CreateVariableRequestRequestTypeDef",
    "PutDetectorRequestRequestTypeDef",
    "PutEntityTypeRequestRequestTypeDef",
    "PutLabelRequestRequestTypeDef",
    "PutOutcomeRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "BatchCreateVariableRequestRequestTypeDef",
    "BatchCreateVariableResultTypeDef",
    "CreateDetectorVersionResultTypeDef",
    "CreateModelVersionResultTypeDef",
    "DeleteEventsByEventTypeResultTypeDef",
    "GetDeleteEventsByEventTypeStatusResultTypeDef",
    "GetListElementsResultTypeDef",
    "GetListsMetadataResultTypeDef",
    "ListTagsForResourceResultTypeDef",
    "UpdateModelVersionResultTypeDef",
    "BatchGetVariableResultTypeDef",
    "GetVariablesResultTypeDef",
    "GetBatchImportJobsResultTypeDef",
    "GetBatchPredictionJobsResultTypeDef",
    "ModelEndpointDataBlobTypeDef",
    "ModelScoresTypeDef",
    "CreateDetectorVersionRequestRequestTypeDef",
    "CreateRuleResultTypeDef",
    "DeleteRuleRequestRequestTypeDef",
    "GetDetectorVersionResultTypeDef",
    "UpdateDetectorVersionRequestRequestTypeDef",
    "UpdateRuleMetadataRequestRequestTypeDef",
    "UpdateRuleVersionRequestRequestTypeDef",
    "UpdateRuleVersionResultTypeDef",
    "DataValidationMetricsTypeDef",
    "DescribeDetectorResultTypeDef",
    "GetDetectorsResultTypeDef",
    "EventTypeDef",
    "SendEventRequestRequestTypeDef",
    "GetEntityTypesResultTypeDef",
    "PutEventTypeRequestRequestTypeDef",
    "ListEventPredictionsResultTypeDef",
    "EventTypeTypeDef",
    "ExternalModelOutputsTypeDef",
    "ExternalModelTypeDef",
    "GetKMSEncryptionKeyResultTypeDef",
    "GetLabelsResultTypeDef",
    "GetModelsResultTypeDef",
    "GetOutcomesResultTypeDef",
    "GetRulesResultTypeDef",
    "IngestedEventsDetailTypeDef",
    "TrainingDataSchemaOutputTypeDef",
    "LabelSchemaUnionTypeDef",
    "ListEventPredictionsRequestRequestTypeDef",
    "VariableImportanceMetricsTypeDef",
    "TrainingMetricsTypeDef",
    "PutExternalModelRequestRequestTypeDef",
    "OFIModelPerformanceTypeDef",
    "TFIModelPerformanceTypeDef",
    "PredictionExplanationsTypeDef",
    "GetEventPredictionRequestRequestTypeDef",
    "GetEventResultTypeDef",
    "GetEventTypesResultTypeDef",
    "GetEventPredictionResultTypeDef",
    "GetExternalModelsResultTypeDef",
    "UpdateModelVersionRequestRequestTypeDef",
    "GetModelVersionResultTypeDef",
    "TrainingDataSchemaTypeDef",
    "TrainingResultTypeDef",
    "OFITrainingMetricsValueTypeDef",
    "TFITrainingMetricsValueTypeDef",
    "ModelVersionEvaluationTypeDef",
    "CreateModelVersionRequestRequestTypeDef",
    "TrainingMetricsV2TypeDef",
    "EvaluatedModelVersionTypeDef",
    "TrainingResultV2TypeDef",
    "GetEventPredictionMetadataResultTypeDef",
    "ModelVersionDetailTypeDef",
    "DescribeModelVersionsResultTypeDef",
)

ATIMetricDataPointTypeDef = TypedDict(
    "ATIMetricDataPointTypeDef",
    {
        "cr": NotRequired[float],
        "adr": NotRequired[float],
        "threshold": NotRequired[float],
        "atodr": NotRequired[float],
    },
)
ATIModelPerformanceTypeDef = TypedDict(
    "ATIModelPerformanceTypeDef",
    {
        "asi": NotRequired[float],
    },
)
AggregatedLogOddsMetricTypeDef = TypedDict(
    "AggregatedLogOddsMetricTypeDef",
    {
        "variableNames": List[str],
        "aggregatedVariablesImportance": float,
    },
)
AggregatedVariablesImpactExplanationTypeDef = TypedDict(
    "AggregatedVariablesImpactExplanationTypeDef",
    {
        "eventVariableNames": NotRequired[List[str]],
        "relativeImpact": NotRequired[str],
        "logOddsImpact": NotRequired[float],
    },
)
AllowDenyListTypeDef = TypedDict(
    "AllowDenyListTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "variableType": NotRequired[str],
        "createdTime": NotRequired[str],
        "updatedTime": NotRequired[str],
        "arn": NotRequired[str],
    },
)
BatchCreateVariableErrorTypeDef = TypedDict(
    "BatchCreateVariableErrorTypeDef",
    {
        "name": NotRequired[str],
        "code": NotRequired[int],
        "message": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)
VariableEntryTypeDef = TypedDict(
    "VariableEntryTypeDef",
    {
        "name": NotRequired[str],
        "dataType": NotRequired[str],
        "dataSource": NotRequired[str],
        "defaultValue": NotRequired[str],
        "description": NotRequired[str],
        "variableType": NotRequired[str],
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
BatchGetVariableErrorTypeDef = TypedDict(
    "BatchGetVariableErrorTypeDef",
    {
        "name": NotRequired[str],
        "code": NotRequired[int],
        "message": NotRequired[str],
    },
)
BatchGetVariableRequestRequestTypeDef = TypedDict(
    "BatchGetVariableRequestRequestTypeDef",
    {
        "names": Sequence[str],
    },
)
VariableTypeDef = TypedDict(
    "VariableTypeDef",
    {
        "name": NotRequired[str],
        "dataType": NotRequired[DataTypeType],
        "dataSource": NotRequired[DataSourceType],
        "defaultValue": NotRequired[str],
        "description": NotRequired[str],
        "variableType": NotRequired[str],
        "lastUpdatedTime": NotRequired[str],
        "createdTime": NotRequired[str],
        "arn": NotRequired[str],
    },
)
BatchImportTypeDef = TypedDict(
    "BatchImportTypeDef",
    {
        "jobId": NotRequired[str],
        "status": NotRequired[AsyncJobStatusType],
        "failureReason": NotRequired[str],
        "startTime": NotRequired[str],
        "completionTime": NotRequired[str],
        "inputPath": NotRequired[str],
        "outputPath": NotRequired[str],
        "eventTypeName": NotRequired[str],
        "iamRoleArn": NotRequired[str],
        "arn": NotRequired[str],
        "processedRecordsCount": NotRequired[int],
        "failedRecordsCount": NotRequired[int],
        "totalRecordsCount": NotRequired[int],
    },
)
BatchPredictionTypeDef = TypedDict(
    "BatchPredictionTypeDef",
    {
        "jobId": NotRequired[str],
        "status": NotRequired[AsyncJobStatusType],
        "failureReason": NotRequired[str],
        "startTime": NotRequired[str],
        "completionTime": NotRequired[str],
        "lastHeartbeatTime": NotRequired[str],
        "inputPath": NotRequired[str],
        "outputPath": NotRequired[str],
        "eventTypeName": NotRequired[str],
        "detectorName": NotRequired[str],
        "detectorVersion": NotRequired[str],
        "iamRoleArn": NotRequired[str],
        "arn": NotRequired[str],
        "processedRecordsCount": NotRequired[int],
        "totalRecordsCount": NotRequired[int],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
CancelBatchImportJobRequestRequestTypeDef = TypedDict(
    "CancelBatchImportJobRequestRequestTypeDef",
    {
        "jobId": str,
    },
)
CancelBatchPredictionJobRequestRequestTypeDef = TypedDict(
    "CancelBatchPredictionJobRequestRequestTypeDef",
    {
        "jobId": str,
    },
)
ModelVersionTypeDef = TypedDict(
    "ModelVersionTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "modelVersionNumber": str,
        "arn": NotRequired[str],
    },
)
RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "detectorId": str,
        "ruleId": str,
        "ruleVersion": str,
    },
)
ExternalEventsDetailTypeDef = TypedDict(
    "ExternalEventsDetailTypeDef",
    {
        "dataLocation": str,
        "dataAccessRoleArn": str,
    },
)
FieldValidationMessageTypeDef = TypedDict(
    "FieldValidationMessageTypeDef",
    {
        "fieldName": NotRequired[str],
        "identifier": NotRequired[str],
        "title": NotRequired[str],
        "content": NotRequired[str],
        "type": NotRequired[str],
    },
)
FileValidationMessageTypeDef = TypedDict(
    "FileValidationMessageTypeDef",
    {
        "title": NotRequired[str],
        "content": NotRequired[str],
        "type": NotRequired[str],
    },
)
DeleteBatchImportJobRequestRequestTypeDef = TypedDict(
    "DeleteBatchImportJobRequestRequestTypeDef",
    {
        "jobId": str,
    },
)
DeleteBatchPredictionJobRequestRequestTypeDef = TypedDict(
    "DeleteBatchPredictionJobRequestRequestTypeDef",
    {
        "jobId": str,
    },
)
DeleteDetectorRequestRequestTypeDef = TypedDict(
    "DeleteDetectorRequestRequestTypeDef",
    {
        "detectorId": str,
    },
)
DeleteDetectorVersionRequestRequestTypeDef = TypedDict(
    "DeleteDetectorVersionRequestRequestTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
    },
)
DeleteEntityTypeRequestRequestTypeDef = TypedDict(
    "DeleteEntityTypeRequestRequestTypeDef",
    {
        "name": str,
    },
)
DeleteEventRequestRequestTypeDef = TypedDict(
    "DeleteEventRequestRequestTypeDef",
    {
        "eventId": str,
        "eventTypeName": str,
        "deleteAuditHistory": NotRequired[bool],
    },
)
DeleteEventTypeRequestRequestTypeDef = TypedDict(
    "DeleteEventTypeRequestRequestTypeDef",
    {
        "name": str,
    },
)
DeleteEventsByEventTypeRequestRequestTypeDef = TypedDict(
    "DeleteEventsByEventTypeRequestRequestTypeDef",
    {
        "eventTypeName": str,
    },
)
DeleteExternalModelRequestRequestTypeDef = TypedDict(
    "DeleteExternalModelRequestRequestTypeDef",
    {
        "modelEndpoint": str,
    },
)
DeleteLabelRequestRequestTypeDef = TypedDict(
    "DeleteLabelRequestRequestTypeDef",
    {
        "name": str,
    },
)
DeleteListRequestRequestTypeDef = TypedDict(
    "DeleteListRequestRequestTypeDef",
    {
        "name": str,
    },
)
DeleteModelRequestRequestTypeDef = TypedDict(
    "DeleteModelRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
    },
)
DeleteModelVersionRequestRequestTypeDef = TypedDict(
    "DeleteModelVersionRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "modelVersionNumber": str,
    },
)
DeleteOutcomeRequestRequestTypeDef = TypedDict(
    "DeleteOutcomeRequestRequestTypeDef",
    {
        "name": str,
    },
)
DeleteVariableRequestRequestTypeDef = TypedDict(
    "DeleteVariableRequestRequestTypeDef",
    {
        "name": str,
    },
)
DescribeDetectorRequestRequestTypeDef = TypedDict(
    "DescribeDetectorRequestRequestTypeDef",
    {
        "detectorId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
DetectorVersionSummaryTypeDef = TypedDict(
    "DetectorVersionSummaryTypeDef",
    {
        "detectorVersionId": NotRequired[str],
        "status": NotRequired[DetectorVersionStatusType],
        "description": NotRequired[str],
        "lastUpdatedTime": NotRequired[str],
    },
)
DescribeModelVersionsRequestRequestTypeDef = TypedDict(
    "DescribeModelVersionsRequestRequestTypeDef",
    {
        "modelId": NotRequired[str],
        "modelVersionNumber": NotRequired[str],
        "modelType": NotRequired[ModelTypeEnumType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
DetectorTypeDef = TypedDict(
    "DetectorTypeDef",
    {
        "detectorId": NotRequired[str],
        "description": NotRequired[str],
        "eventTypeName": NotRequired[str],
        "lastUpdatedTime": NotRequired[str],
        "createdTime": NotRequired[str],
        "arn": NotRequired[str],
    },
)
EntityTypeDef = TypedDict(
    "EntityTypeDef",
    {
        "entityType": str,
        "entityId": str,
    },
)
EntityTypeTypeDef = TypedDict(
    "EntityTypeTypeDef",
    {
        "name": NotRequired[str],
        "description": NotRequired[str],
        "lastUpdatedTime": NotRequired[str],
        "createdTime": NotRequired[str],
        "arn": NotRequired[str],
    },
)
EvaluatedExternalModelTypeDef = TypedDict(
    "EvaluatedExternalModelTypeDef",
    {
        "modelEndpoint": NotRequired[str],
        "useEventVariables": NotRequired[bool],
        "inputVariables": NotRequired[Dict[str, str]],
        "outputVariables": NotRequired[Dict[str, str]],
    },
)
EvaluatedRuleTypeDef = TypedDict(
    "EvaluatedRuleTypeDef",
    {
        "ruleId": NotRequired[str],
        "ruleVersion": NotRequired[str],
        "expression": NotRequired[str],
        "expressionWithValues": NotRequired[str],
        "outcomes": NotRequired[List[str]],
        "evaluated": NotRequired[bool],
        "matched": NotRequired[bool],
    },
)
EventOrchestrationTypeDef = TypedDict(
    "EventOrchestrationTypeDef",
    {
        "eventBridgeEnabled": bool,
    },
)
EventPredictionSummaryTypeDef = TypedDict(
    "EventPredictionSummaryTypeDef",
    {
        "eventId": NotRequired[str],
        "eventTypeName": NotRequired[str],
        "eventTimestamp": NotRequired[str],
        "predictionTimestamp": NotRequired[str],
        "detectorId": NotRequired[str],
        "detectorVersionId": NotRequired[str],
    },
)
IngestedEventStatisticsTypeDef = TypedDict(
    "IngestedEventStatisticsTypeDef",
    {
        "numberOfEvents": NotRequired[int],
        "eventDataSizeInBytes": NotRequired[int],
        "leastRecentEvent": NotRequired[str],
        "mostRecentEvent": NotRequired[str],
        "lastUpdatedTime": NotRequired[str],
    },
)
EventVariableSummaryTypeDef = TypedDict(
    "EventVariableSummaryTypeDef",
    {
        "name": NotRequired[str],
        "value": NotRequired[str],
        "source": NotRequired[str],
    },
)
ExternalModelSummaryTypeDef = TypedDict(
    "ExternalModelSummaryTypeDef",
    {
        "modelEndpoint": NotRequired[str],
        "modelSource": NotRequired[Literal["SAGEMAKER"]],
    },
)
ModelInputConfigurationTypeDef = TypedDict(
    "ModelInputConfigurationTypeDef",
    {
        "useEventVariables": bool,
        "eventTypeName": NotRequired[str],
        "format": NotRequired[ModelInputDataFormatType],
        "jsonInputTemplate": NotRequired[str],
        "csvInputTemplate": NotRequired[str],
    },
)
ModelOutputConfigurationOutputTypeDef = TypedDict(
    "ModelOutputConfigurationOutputTypeDef",
    {
        "format": ModelOutputDataFormatType,
        "jsonKeyToVariableMap": NotRequired[Dict[str, str]],
        "csvIndexToVariableMap": NotRequired[Dict[str, str]],
    },
)
FilterConditionTypeDef = TypedDict(
    "FilterConditionTypeDef",
    {
        "value": NotRequired[str],
    },
)
GetBatchImportJobsRequestRequestTypeDef = TypedDict(
    "GetBatchImportJobsRequestRequestTypeDef",
    {
        "jobId": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
GetBatchPredictionJobsRequestRequestTypeDef = TypedDict(
    "GetBatchPredictionJobsRequestRequestTypeDef",
    {
        "jobId": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
GetDeleteEventsByEventTypeStatusRequestRequestTypeDef = TypedDict(
    "GetDeleteEventsByEventTypeStatusRequestRequestTypeDef",
    {
        "eventTypeName": str,
    },
)
GetDetectorVersionRequestRequestTypeDef = TypedDict(
    "GetDetectorVersionRequestRequestTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
    },
)
GetDetectorsRequestRequestTypeDef = TypedDict(
    "GetDetectorsRequestRequestTypeDef",
    {
        "detectorId": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
GetEntityTypesRequestRequestTypeDef = TypedDict(
    "GetEntityTypesRequestRequestTypeDef",
    {
        "name": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
GetEventPredictionMetadataRequestRequestTypeDef = TypedDict(
    "GetEventPredictionMetadataRequestRequestTypeDef",
    {
        "eventId": str,
        "eventTypeName": str,
        "detectorId": str,
        "detectorVersionId": str,
        "predictionTimestamp": str,
    },
)
RuleResultTypeDef = TypedDict(
    "RuleResultTypeDef",
    {
        "ruleId": NotRequired[str],
        "outcomes": NotRequired[List[str]],
    },
)
GetEventRequestRequestTypeDef = TypedDict(
    "GetEventRequestRequestTypeDef",
    {
        "eventId": str,
        "eventTypeName": str,
    },
)
GetEventTypesRequestRequestTypeDef = TypedDict(
    "GetEventTypesRequestRequestTypeDef",
    {
        "name": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
GetExternalModelsRequestRequestTypeDef = TypedDict(
    "GetExternalModelsRequestRequestTypeDef",
    {
        "modelEndpoint": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
KMSKeyTypeDef = TypedDict(
    "KMSKeyTypeDef",
    {
        "kmsEncryptionKeyArn": NotRequired[str],
    },
)
GetLabelsRequestRequestTypeDef = TypedDict(
    "GetLabelsRequestRequestTypeDef",
    {
        "name": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
LabelTypeDef = TypedDict(
    "LabelTypeDef",
    {
        "name": NotRequired[str],
        "description": NotRequired[str],
        "lastUpdatedTime": NotRequired[str],
        "createdTime": NotRequired[str],
        "arn": NotRequired[str],
    },
)
GetListElementsRequestRequestTypeDef = TypedDict(
    "GetListElementsRequestRequestTypeDef",
    {
        "name": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
GetListsMetadataRequestRequestTypeDef = TypedDict(
    "GetListsMetadataRequestRequestTypeDef",
    {
        "name": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
GetModelVersionRequestRequestTypeDef = TypedDict(
    "GetModelVersionRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "modelVersionNumber": str,
    },
)
GetModelsRequestRequestTypeDef = TypedDict(
    "GetModelsRequestRequestTypeDef",
    {
        "modelId": NotRequired[str],
        "modelType": NotRequired[ModelTypeEnumType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ModelTypeDef = TypedDict(
    "ModelTypeDef",
    {
        "modelId": NotRequired[str],
        "modelType": NotRequired[ModelTypeEnumType],
        "description": NotRequired[str],
        "eventTypeName": NotRequired[str],
        "createdTime": NotRequired[str],
        "lastUpdatedTime": NotRequired[str],
        "arn": NotRequired[str],
    },
)
GetOutcomesRequestRequestTypeDef = TypedDict(
    "GetOutcomesRequestRequestTypeDef",
    {
        "name": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
OutcomeTypeDef = TypedDict(
    "OutcomeTypeDef",
    {
        "name": NotRequired[str],
        "description": NotRequired[str],
        "lastUpdatedTime": NotRequired[str],
        "createdTime": NotRequired[str],
        "arn": NotRequired[str],
    },
)
GetRulesRequestRequestTypeDef = TypedDict(
    "GetRulesRequestRequestTypeDef",
    {
        "detectorId": str,
        "ruleId": NotRequired[str],
        "ruleVersion": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
RuleDetailTypeDef = TypedDict(
    "RuleDetailTypeDef",
    {
        "ruleId": NotRequired[str],
        "description": NotRequired[str],
        "detectorId": NotRequired[str],
        "ruleVersion": NotRequired[str],
        "expression": NotRequired[str],
        "language": NotRequired[Literal["DETECTORPL"]],
        "outcomes": NotRequired[List[str]],
        "lastUpdatedTime": NotRequired[str],
        "createdTime": NotRequired[str],
        "arn": NotRequired[str],
    },
)
GetVariablesRequestRequestTypeDef = TypedDict(
    "GetVariablesRequestRequestTypeDef",
    {
        "name": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
IngestedEventsTimeWindowTypeDef = TypedDict(
    "IngestedEventsTimeWindowTypeDef",
    {
        "startTime": str,
        "endTime": str,
    },
)
LabelSchemaOutputTypeDef = TypedDict(
    "LabelSchemaOutputTypeDef",
    {
        "labelMapper": NotRequired[Dict[str, List[str]]],
        "unlabeledEventsTreatment": NotRequired[UnlabeledEventsTreatmentType],
    },
)
LabelSchemaTypeDef = TypedDict(
    "LabelSchemaTypeDef",
    {
        "labelMapper": NotRequired[Mapping[str, Sequence[str]]],
        "unlabeledEventsTreatment": NotRequired[UnlabeledEventsTreatmentType],
    },
)
PredictionTimeRangeTypeDef = TypedDict(
    "PredictionTimeRangeTypeDef",
    {
        "startTime": str,
        "endTime": str,
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
LogOddsMetricTypeDef = TypedDict(
    "LogOddsMetricTypeDef",
    {
        "variableName": str,
        "variableType": str,
        "variableImportance": float,
    },
)
MetricDataPointTypeDef = TypedDict(
    "MetricDataPointTypeDef",
    {
        "fpr": NotRequired[float],
        "precision": NotRequired[float],
        "tpr": NotRequired[float],
        "threshold": NotRequired[float],
    },
)
ModelOutputConfigurationTypeDef = TypedDict(
    "ModelOutputConfigurationTypeDef",
    {
        "format": ModelOutputDataFormatType,
        "jsonKeyToVariableMap": NotRequired[Mapping[str, str]],
        "csvIndexToVariableMap": NotRequired[Mapping[str, str]],
    },
)
OFIMetricDataPointTypeDef = TypedDict(
    "OFIMetricDataPointTypeDef",
    {
        "fpr": NotRequired[float],
        "precision": NotRequired[float],
        "tpr": NotRequired[float],
        "threshold": NotRequired[float],
    },
)
UncertaintyRangeTypeDef = TypedDict(
    "UncertaintyRangeTypeDef",
    {
        "lowerBoundValue": float,
        "upperBoundValue": float,
    },
)
VariableImpactExplanationTypeDef = TypedDict(
    "VariableImpactExplanationTypeDef",
    {
        "eventVariableName": NotRequired[str],
        "relativeImpact": NotRequired[str],
        "logOddsImpact": NotRequired[float],
    },
)
PutKMSEncryptionKeyRequestRequestTypeDef = TypedDict(
    "PutKMSEncryptionKeyRequestRequestTypeDef",
    {
        "kmsEncryptionKeyArn": str,
    },
)
TFIMetricDataPointTypeDef = TypedDict(
    "TFIMetricDataPointTypeDef",
    {
        "fpr": NotRequired[float],
        "precision": NotRequired[float],
        "tpr": NotRequired[float],
        "threshold": NotRequired[float],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
        "tagKeys": Sequence[str],
    },
)
UpdateDetectorVersionMetadataRequestRequestTypeDef = TypedDict(
    "UpdateDetectorVersionMetadataRequestRequestTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
        "description": str,
    },
)
UpdateDetectorVersionStatusRequestRequestTypeDef = TypedDict(
    "UpdateDetectorVersionStatusRequestRequestTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
        "status": DetectorVersionStatusType,
    },
)
UpdateEventLabelRequestRequestTypeDef = TypedDict(
    "UpdateEventLabelRequestRequestTypeDef",
    {
        "eventId": str,
        "eventTypeName": str,
        "assignedLabel": str,
        "labelTimestamp": str,
    },
)
UpdateListRequestRequestTypeDef = TypedDict(
    "UpdateListRequestRequestTypeDef",
    {
        "name": str,
        "elements": NotRequired[Sequence[str]],
        "description": NotRequired[str],
        "updateMode": NotRequired[ListUpdateModeType],
        "variableType": NotRequired[str],
    },
)
UpdateModelRequestRequestTypeDef = TypedDict(
    "UpdateModelRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "description": NotRequired[str],
    },
)
UpdateModelVersionStatusRequestRequestTypeDef = TypedDict(
    "UpdateModelVersionStatusRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "modelVersionNumber": str,
        "status": ModelVersionStatusType,
    },
)
UpdateVariableRequestRequestTypeDef = TypedDict(
    "UpdateVariableRequestRequestTypeDef",
    {
        "name": str,
        "defaultValue": NotRequired[str],
        "description": NotRequired[str],
        "variableType": NotRequired[str],
    },
)
ATITrainingMetricsValueTypeDef = TypedDict(
    "ATITrainingMetricsValueTypeDef",
    {
        "metricDataPoints": NotRequired[List[ATIMetricDataPointTypeDef]],
        "modelPerformance": NotRequired[ATIModelPerformanceTypeDef],
    },
)
AggregatedVariablesImportanceMetricsTypeDef = TypedDict(
    "AggregatedVariablesImportanceMetricsTypeDef",
    {
        "logOddsMetrics": NotRequired[List[AggregatedLogOddsMetricTypeDef]],
    },
)
CreateBatchImportJobRequestRequestTypeDef = TypedDict(
    "CreateBatchImportJobRequestRequestTypeDef",
    {
        "jobId": str,
        "inputPath": str,
        "outputPath": str,
        "eventTypeName": str,
        "iamRoleArn": str,
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateBatchPredictionJobRequestRequestTypeDef = TypedDict(
    "CreateBatchPredictionJobRequestRequestTypeDef",
    {
        "jobId": str,
        "inputPath": str,
        "outputPath": str,
        "eventTypeName": str,
        "detectorName": str,
        "iamRoleArn": str,
        "detectorVersion": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateListRequestRequestTypeDef = TypedDict(
    "CreateListRequestRequestTypeDef",
    {
        "name": str,
        "elements": NotRequired[Sequence[str]],
        "variableType": NotRequired[str],
        "description": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateModelRequestRequestTypeDef = TypedDict(
    "CreateModelRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "eventTypeName": str,
        "description": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateRuleRequestRequestTypeDef = TypedDict(
    "CreateRuleRequestRequestTypeDef",
    {
        "ruleId": str,
        "detectorId": str,
        "expression": str,
        "language": Literal["DETECTORPL"],
        "outcomes": Sequence[str],
        "description": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateVariableRequestRequestTypeDef = TypedDict(
    "CreateVariableRequestRequestTypeDef",
    {
        "name": str,
        "dataType": DataTypeType,
        "dataSource": DataSourceType,
        "defaultValue": str,
        "description": NotRequired[str],
        "variableType": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
PutDetectorRequestRequestTypeDef = TypedDict(
    "PutDetectorRequestRequestTypeDef",
    {
        "detectorId": str,
        "eventTypeName": str,
        "description": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
PutEntityTypeRequestRequestTypeDef = TypedDict(
    "PutEntityTypeRequestRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
PutLabelRequestRequestTypeDef = TypedDict(
    "PutLabelRequestRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
PutOutcomeRequestRequestTypeDef = TypedDict(
    "PutOutcomeRequestRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
        "tags": Sequence[TagTypeDef],
    },
)
BatchCreateVariableRequestRequestTypeDef = TypedDict(
    "BatchCreateVariableRequestRequestTypeDef",
    {
        "variableEntries": Sequence[VariableEntryTypeDef],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
BatchCreateVariableResultTypeDef = TypedDict(
    "BatchCreateVariableResultTypeDef",
    {
        "errors": List[BatchCreateVariableErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDetectorVersionResultTypeDef = TypedDict(
    "CreateDetectorVersionResultTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
        "status": DetectorVersionStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateModelVersionResultTypeDef = TypedDict(
    "CreateModelVersionResultTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "modelVersionNumber": str,
        "status": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteEventsByEventTypeResultTypeDef = TypedDict(
    "DeleteEventsByEventTypeResultTypeDef",
    {
        "eventTypeName": str,
        "eventsDeletionStatus": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDeleteEventsByEventTypeStatusResultTypeDef = TypedDict(
    "GetDeleteEventsByEventTypeStatusResultTypeDef",
    {
        "eventTypeName": str,
        "eventsDeletionStatus": AsyncJobStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetListElementsResultTypeDef = TypedDict(
    "GetListElementsResultTypeDef",
    {
        "elements": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetListsMetadataResultTypeDef = TypedDict(
    "GetListsMetadataResultTypeDef",
    {
        "lists": List[AllowDenyListTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "tags": List[TagTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateModelVersionResultTypeDef = TypedDict(
    "UpdateModelVersionResultTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "modelVersionNumber": str,
        "status": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetVariableResultTypeDef = TypedDict(
    "BatchGetVariableResultTypeDef",
    {
        "variables": List[VariableTypeDef],
        "errors": List[BatchGetVariableErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetVariablesResultTypeDef = TypedDict(
    "GetVariablesResultTypeDef",
    {
        "variables": List[VariableTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBatchImportJobsResultTypeDef = TypedDict(
    "GetBatchImportJobsResultTypeDef",
    {
        "batchImports": List[BatchImportTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBatchPredictionJobsResultTypeDef = TypedDict(
    "GetBatchPredictionJobsResultTypeDef",
    {
        "batchPredictions": List[BatchPredictionTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModelEndpointDataBlobTypeDef = TypedDict(
    "ModelEndpointDataBlobTypeDef",
    {
        "byteBuffer": NotRequired[BlobTypeDef],
        "contentType": NotRequired[str],
    },
)
ModelScoresTypeDef = TypedDict(
    "ModelScoresTypeDef",
    {
        "modelVersion": NotRequired[ModelVersionTypeDef],
        "scores": NotRequired[Dict[str, float]],
    },
)
CreateDetectorVersionRequestRequestTypeDef = TypedDict(
    "CreateDetectorVersionRequestRequestTypeDef",
    {
        "detectorId": str,
        "rules": Sequence[RuleTypeDef],
        "description": NotRequired[str],
        "externalModelEndpoints": NotRequired[Sequence[str]],
        "modelVersions": NotRequired[Sequence[ModelVersionTypeDef]],
        "ruleExecutionMode": NotRequired[RuleExecutionModeType],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateRuleResultTypeDef = TypedDict(
    "CreateRuleResultTypeDef",
    {
        "rule": RuleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteRuleRequestRequestTypeDef = TypedDict(
    "DeleteRuleRequestRequestTypeDef",
    {
        "rule": RuleTypeDef,
    },
)
GetDetectorVersionResultTypeDef = TypedDict(
    "GetDetectorVersionResultTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
        "description": str,
        "externalModelEndpoints": List[str],
        "modelVersions": List[ModelVersionTypeDef],
        "rules": List[RuleTypeDef],
        "status": DetectorVersionStatusType,
        "lastUpdatedTime": str,
        "createdTime": str,
        "ruleExecutionMode": RuleExecutionModeType,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDetectorVersionRequestRequestTypeDef = TypedDict(
    "UpdateDetectorVersionRequestRequestTypeDef",
    {
        "detectorId": str,
        "detectorVersionId": str,
        "externalModelEndpoints": Sequence[str],
        "rules": Sequence[RuleTypeDef],
        "description": NotRequired[str],
        "modelVersions": NotRequired[Sequence[ModelVersionTypeDef]],
        "ruleExecutionMode": NotRequired[RuleExecutionModeType],
    },
)
UpdateRuleMetadataRequestRequestTypeDef = TypedDict(
    "UpdateRuleMetadataRequestRequestTypeDef",
    {
        "rule": RuleTypeDef,
        "description": str,
    },
)
UpdateRuleVersionRequestRequestTypeDef = TypedDict(
    "UpdateRuleVersionRequestRequestTypeDef",
    {
        "rule": RuleTypeDef,
        "expression": str,
        "language": Literal["DETECTORPL"],
        "outcomes": Sequence[str],
        "description": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
UpdateRuleVersionResultTypeDef = TypedDict(
    "UpdateRuleVersionResultTypeDef",
    {
        "rule": RuleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DataValidationMetricsTypeDef = TypedDict(
    "DataValidationMetricsTypeDef",
    {
        "fileLevelMessages": NotRequired[List[FileValidationMessageTypeDef]],
        "fieldLevelMessages": NotRequired[List[FieldValidationMessageTypeDef]],
    },
)
DescribeDetectorResultTypeDef = TypedDict(
    "DescribeDetectorResultTypeDef",
    {
        "detectorId": str,
        "detectorVersionSummaries": List[DetectorVersionSummaryTypeDef],
        "nextToken": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDetectorsResultTypeDef = TypedDict(
    "GetDetectorsResultTypeDef",
    {
        "detectors": List[DetectorTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "eventId": NotRequired[str],
        "eventTypeName": NotRequired[str],
        "eventTimestamp": NotRequired[str],
        "eventVariables": NotRequired[Dict[str, str]],
        "currentLabel": NotRequired[str],
        "labelTimestamp": NotRequired[str],
        "entities": NotRequired[List[EntityTypeDef]],
    },
)
SendEventRequestRequestTypeDef = TypedDict(
    "SendEventRequestRequestTypeDef",
    {
        "eventId": str,
        "eventTypeName": str,
        "eventTimestamp": str,
        "eventVariables": Mapping[str, str],
        "entities": Sequence[EntityTypeDef],
        "assignedLabel": NotRequired[str],
        "labelTimestamp": NotRequired[str],
    },
)
GetEntityTypesResultTypeDef = TypedDict(
    "GetEntityTypesResultTypeDef",
    {
        "entityTypes": List[EntityTypeTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutEventTypeRequestRequestTypeDef = TypedDict(
    "PutEventTypeRequestRequestTypeDef",
    {
        "name": str,
        "eventVariables": Sequence[str],
        "entityTypes": Sequence[str],
        "description": NotRequired[str],
        "labels": NotRequired[Sequence[str]],
        "eventIngestion": NotRequired[EventIngestionType],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "eventOrchestration": NotRequired[EventOrchestrationTypeDef],
    },
)
ListEventPredictionsResultTypeDef = TypedDict(
    "ListEventPredictionsResultTypeDef",
    {
        "eventPredictionSummaries": List[EventPredictionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EventTypeTypeDef = TypedDict(
    "EventTypeTypeDef",
    {
        "name": NotRequired[str],
        "description": NotRequired[str],
        "eventVariables": NotRequired[List[str]],
        "labels": NotRequired[List[str]],
        "entityTypes": NotRequired[List[str]],
        "eventIngestion": NotRequired[EventIngestionType],
        "ingestedEventStatistics": NotRequired[IngestedEventStatisticsTypeDef],
        "lastUpdatedTime": NotRequired[str],
        "createdTime": NotRequired[str],
        "arn": NotRequired[str],
        "eventOrchestration": NotRequired[EventOrchestrationTypeDef],
    },
)
ExternalModelOutputsTypeDef = TypedDict(
    "ExternalModelOutputsTypeDef",
    {
        "externalModel": NotRequired[ExternalModelSummaryTypeDef],
        "outputs": NotRequired[Dict[str, str]],
    },
)
ExternalModelTypeDef = TypedDict(
    "ExternalModelTypeDef",
    {
        "modelEndpoint": NotRequired[str],
        "modelSource": NotRequired[Literal["SAGEMAKER"]],
        "invokeModelEndpointRoleArn": NotRequired[str],
        "inputConfiguration": NotRequired[ModelInputConfigurationTypeDef],
        "outputConfiguration": NotRequired[ModelOutputConfigurationOutputTypeDef],
        "modelEndpointStatus": NotRequired[ModelEndpointStatusType],
        "lastUpdatedTime": NotRequired[str],
        "createdTime": NotRequired[str],
        "arn": NotRequired[str],
    },
)
GetKMSEncryptionKeyResultTypeDef = TypedDict(
    "GetKMSEncryptionKeyResultTypeDef",
    {
        "kmsKey": KMSKeyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLabelsResultTypeDef = TypedDict(
    "GetLabelsResultTypeDef",
    {
        "labels": List[LabelTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetModelsResultTypeDef = TypedDict(
    "GetModelsResultTypeDef",
    {
        "nextToken": str,
        "models": List[ModelTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetOutcomesResultTypeDef = TypedDict(
    "GetOutcomesResultTypeDef",
    {
        "outcomes": List[OutcomeTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRulesResultTypeDef = TypedDict(
    "GetRulesResultTypeDef",
    {
        "ruleDetails": List[RuleDetailTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IngestedEventsDetailTypeDef = TypedDict(
    "IngestedEventsDetailTypeDef",
    {
        "ingestedEventsTimeWindow": IngestedEventsTimeWindowTypeDef,
    },
)
TrainingDataSchemaOutputTypeDef = TypedDict(
    "TrainingDataSchemaOutputTypeDef",
    {
        "modelVariables": List[str],
        "labelSchema": NotRequired[LabelSchemaOutputTypeDef],
    },
)
LabelSchemaUnionTypeDef = Union[LabelSchemaTypeDef, LabelSchemaOutputTypeDef]
ListEventPredictionsRequestRequestTypeDef = TypedDict(
    "ListEventPredictionsRequestRequestTypeDef",
    {
        "eventId": NotRequired[FilterConditionTypeDef],
        "eventType": NotRequired[FilterConditionTypeDef],
        "detectorId": NotRequired[FilterConditionTypeDef],
        "detectorVersionId": NotRequired[FilterConditionTypeDef],
        "predictionTimeRange": NotRequired[PredictionTimeRangeTypeDef],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
VariableImportanceMetricsTypeDef = TypedDict(
    "VariableImportanceMetricsTypeDef",
    {
        "logOddsMetrics": NotRequired[List[LogOddsMetricTypeDef]],
    },
)
TrainingMetricsTypeDef = TypedDict(
    "TrainingMetricsTypeDef",
    {
        "auc": NotRequired[float],
        "metricDataPoints": NotRequired[List[MetricDataPointTypeDef]],
    },
)
PutExternalModelRequestRequestTypeDef = TypedDict(
    "PutExternalModelRequestRequestTypeDef",
    {
        "modelEndpoint": str,
        "modelSource": Literal["SAGEMAKER"],
        "invokeModelEndpointRoleArn": str,
        "inputConfiguration": ModelInputConfigurationTypeDef,
        "outputConfiguration": ModelOutputConfigurationTypeDef,
        "modelEndpointStatus": ModelEndpointStatusType,
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
OFIModelPerformanceTypeDef = TypedDict(
    "OFIModelPerformanceTypeDef",
    {
        "auc": NotRequired[float],
        "uncertaintyRange": NotRequired[UncertaintyRangeTypeDef],
    },
)
TFIModelPerformanceTypeDef = TypedDict(
    "TFIModelPerformanceTypeDef",
    {
        "auc": NotRequired[float],
        "uncertaintyRange": NotRequired[UncertaintyRangeTypeDef],
    },
)
PredictionExplanationsTypeDef = TypedDict(
    "PredictionExplanationsTypeDef",
    {
        "variableImpactExplanations": NotRequired[List[VariableImpactExplanationTypeDef]],
        "aggregatedVariablesImpactExplanations": NotRequired[
            List[AggregatedVariablesImpactExplanationTypeDef]
        ],
    },
)
GetEventPredictionRequestRequestTypeDef = TypedDict(
    "GetEventPredictionRequestRequestTypeDef",
    {
        "detectorId": str,
        "eventId": str,
        "eventTypeName": str,
        "entities": Sequence[EntityTypeDef],
        "eventTimestamp": str,
        "eventVariables": Mapping[str, str],
        "detectorVersionId": NotRequired[str],
        "externalModelEndpointDataBlobs": NotRequired[Mapping[str, ModelEndpointDataBlobTypeDef]],
    },
)
GetEventResultTypeDef = TypedDict(
    "GetEventResultTypeDef",
    {
        "event": EventTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEventTypesResultTypeDef = TypedDict(
    "GetEventTypesResultTypeDef",
    {
        "eventTypes": List[EventTypeTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEventPredictionResultTypeDef = TypedDict(
    "GetEventPredictionResultTypeDef",
    {
        "modelScores": List[ModelScoresTypeDef],
        "ruleResults": List[RuleResultTypeDef],
        "externalModelOutputs": List[ExternalModelOutputsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetExternalModelsResultTypeDef = TypedDict(
    "GetExternalModelsResultTypeDef",
    {
        "externalModels": List[ExternalModelTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateModelVersionRequestRequestTypeDef = TypedDict(
    "UpdateModelVersionRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "majorVersionNumber": str,
        "externalEventsDetail": NotRequired[ExternalEventsDetailTypeDef],
        "ingestedEventsDetail": NotRequired[IngestedEventsDetailTypeDef],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
GetModelVersionResultTypeDef = TypedDict(
    "GetModelVersionResultTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "modelVersionNumber": str,
        "trainingDataSource": TrainingDataSourceEnumType,
        "trainingDataSchema": TrainingDataSchemaOutputTypeDef,
        "externalEventsDetail": ExternalEventsDetailTypeDef,
        "ingestedEventsDetail": IngestedEventsDetailTypeDef,
        "status": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TrainingDataSchemaTypeDef = TypedDict(
    "TrainingDataSchemaTypeDef",
    {
        "modelVariables": Sequence[str],
        "labelSchema": NotRequired[LabelSchemaUnionTypeDef],
    },
)
TrainingResultTypeDef = TypedDict(
    "TrainingResultTypeDef",
    {
        "dataValidationMetrics": NotRequired[DataValidationMetricsTypeDef],
        "trainingMetrics": NotRequired[TrainingMetricsTypeDef],
        "variableImportanceMetrics": NotRequired[VariableImportanceMetricsTypeDef],
    },
)
OFITrainingMetricsValueTypeDef = TypedDict(
    "OFITrainingMetricsValueTypeDef",
    {
        "metricDataPoints": NotRequired[List[OFIMetricDataPointTypeDef]],
        "modelPerformance": NotRequired[OFIModelPerformanceTypeDef],
    },
)
TFITrainingMetricsValueTypeDef = TypedDict(
    "TFITrainingMetricsValueTypeDef",
    {
        "metricDataPoints": NotRequired[List[TFIMetricDataPointTypeDef]],
        "modelPerformance": NotRequired[TFIModelPerformanceTypeDef],
    },
)
ModelVersionEvaluationTypeDef = TypedDict(
    "ModelVersionEvaluationTypeDef",
    {
        "outputVariableName": NotRequired[str],
        "evaluationScore": NotRequired[str],
        "predictionExplanations": NotRequired[PredictionExplanationsTypeDef],
    },
)
CreateModelVersionRequestRequestTypeDef = TypedDict(
    "CreateModelVersionRequestRequestTypeDef",
    {
        "modelId": str,
        "modelType": ModelTypeEnumType,
        "trainingDataSource": TrainingDataSourceEnumType,
        "trainingDataSchema": TrainingDataSchemaTypeDef,
        "externalEventsDetail": NotRequired[ExternalEventsDetailTypeDef],
        "ingestedEventsDetail": NotRequired[IngestedEventsDetailTypeDef],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
TrainingMetricsV2TypeDef = TypedDict(
    "TrainingMetricsV2TypeDef",
    {
        "ofi": NotRequired[OFITrainingMetricsValueTypeDef],
        "tfi": NotRequired[TFITrainingMetricsValueTypeDef],
        "ati": NotRequired[ATITrainingMetricsValueTypeDef],
    },
)
EvaluatedModelVersionTypeDef = TypedDict(
    "EvaluatedModelVersionTypeDef",
    {
        "modelId": NotRequired[str],
        "modelVersion": NotRequired[str],
        "modelType": NotRequired[str],
        "evaluations": NotRequired[List[ModelVersionEvaluationTypeDef]],
    },
)
TrainingResultV2TypeDef = TypedDict(
    "TrainingResultV2TypeDef",
    {
        "dataValidationMetrics": NotRequired[DataValidationMetricsTypeDef],
        "trainingMetricsV2": NotRequired[TrainingMetricsV2TypeDef],
        "variableImportanceMetrics": NotRequired[VariableImportanceMetricsTypeDef],
        "aggregatedVariablesImportanceMetrics": NotRequired[
            AggregatedVariablesImportanceMetricsTypeDef
        ],
    },
)
GetEventPredictionMetadataResultTypeDef = TypedDict(
    "GetEventPredictionMetadataResultTypeDef",
    {
        "eventId": str,
        "eventTypeName": str,
        "entityId": str,
        "entityType": str,
        "eventTimestamp": str,
        "detectorId": str,
        "detectorVersionId": str,
        "detectorVersionStatus": str,
        "eventVariables": List[EventVariableSummaryTypeDef],
        "rules": List[EvaluatedRuleTypeDef],
        "ruleExecutionMode": RuleExecutionModeType,
        "outcomes": List[str],
        "evaluatedModelVersions": List[EvaluatedModelVersionTypeDef],
        "evaluatedExternalModels": List[EvaluatedExternalModelTypeDef],
        "predictionTimestamp": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModelVersionDetailTypeDef = TypedDict(
    "ModelVersionDetailTypeDef",
    {
        "modelId": NotRequired[str],
        "modelType": NotRequired[ModelTypeEnumType],
        "modelVersionNumber": NotRequired[str],
        "status": NotRequired[str],
        "trainingDataSource": NotRequired[TrainingDataSourceEnumType],
        "trainingDataSchema": NotRequired[TrainingDataSchemaOutputTypeDef],
        "externalEventsDetail": NotRequired[ExternalEventsDetailTypeDef],
        "ingestedEventsDetail": NotRequired[IngestedEventsDetailTypeDef],
        "trainingResult": NotRequired[TrainingResultTypeDef],
        "lastUpdatedTime": NotRequired[str],
        "createdTime": NotRequired[str],
        "arn": NotRequired[str],
        "trainingResultV2": NotRequired[TrainingResultV2TypeDef],
    },
)
DescribeModelVersionsResultTypeDef = TypedDict(
    "DescribeModelVersionsResultTypeDef",
    {
        "modelVersionDetails": List[ModelVersionDetailTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
