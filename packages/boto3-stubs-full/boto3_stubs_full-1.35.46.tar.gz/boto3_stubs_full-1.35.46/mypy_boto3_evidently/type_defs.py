"""
Type annotations for evidently service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/type_defs/)

Usage::

    ```python
    from mypy_boto3_evidently.type_defs import EvaluationRequestTypeDef

    data: EvaluationRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    ChangeDirectionEnumType,
    EventTypeType,
    ExperimentResultRequestTypeType,
    ExperimentResultResponseTypeType,
    ExperimentStatusType,
    ExperimentStopDesiredStateType,
    FeatureEvaluationStrategyType,
    FeatureStatusType,
    LaunchStatusType,
    LaunchStopDesiredStateType,
    ProjectStatusType,
    SegmentReferenceResourceTypeType,
    VariationValueTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "EvaluationRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CloudWatchLogsDestinationConfigTypeDef",
    "CloudWatchLogsDestinationTypeDef",
    "OnlineAbConfigTypeDef",
    "TreatmentConfigTypeDef",
    "LaunchGroupConfigTypeDef",
    "ProjectAppConfigResourceConfigTypeDef",
    "CreateSegmentRequestRequestTypeDef",
    "SegmentTypeDef",
    "DeleteExperimentRequestRequestTypeDef",
    "DeleteFeatureRequestRequestTypeDef",
    "DeleteLaunchRequestRequestTypeDef",
    "DeleteProjectRequestRequestTypeDef",
    "DeleteSegmentRequestRequestTypeDef",
    "EvaluateFeatureRequestRequestTypeDef",
    "VariableValueTypeDef",
    "EvaluationRuleTypeDef",
    "TimestampTypeDef",
    "ExperimentExecutionTypeDef",
    "ExperimentReportTypeDef",
    "ExperimentResultsDataTypeDef",
    "ExperimentScheduleTypeDef",
    "OnlineAbDefinitionTypeDef",
    "TreatmentTypeDef",
    "GetExperimentRequestRequestTypeDef",
    "GetFeatureRequestRequestTypeDef",
    "GetLaunchRequestRequestTypeDef",
    "GetProjectRequestRequestTypeDef",
    "GetSegmentRequestRequestTypeDef",
    "LaunchExecutionTypeDef",
    "LaunchGroupTypeDef",
    "PaginatorConfigTypeDef",
    "ListExperimentsRequestRequestTypeDef",
    "ListFeaturesRequestRequestTypeDef",
    "ListLaunchesRequestRequestTypeDef",
    "ListProjectsRequestRequestTypeDef",
    "ProjectSummaryTypeDef",
    "ListSegmentReferencesRequestRequestTypeDef",
    "RefResourceTypeDef",
    "ListSegmentsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "MetricDefinitionConfigTypeDef",
    "MetricDefinitionTypeDef",
    "ProjectAppConfigResourceTypeDef",
    "S3DestinationConfigTypeDef",
    "S3DestinationTypeDef",
    "PutProjectEventsResultEntryTypeDef",
    "SegmentOverrideOutputTypeDef",
    "SegmentOverrideTypeDef",
    "StartLaunchRequestRequestTypeDef",
    "StopExperimentRequestRequestTypeDef",
    "StopLaunchRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TestSegmentPatternRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "BatchEvaluateFeatureRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartExperimentResponseTypeDef",
    "StopExperimentResponseTypeDef",
    "StopLaunchResponseTypeDef",
    "TestSegmentPatternResponseTypeDef",
    "UpdateProjectRequestRequestTypeDef",
    "CreateSegmentResponseTypeDef",
    "GetSegmentResponseTypeDef",
    "ListSegmentsResponseTypeDef",
    "EvaluateFeatureResponseTypeDef",
    "EvaluationResultTypeDef",
    "VariationConfigTypeDef",
    "VariationTypeDef",
    "FeatureSummaryTypeDef",
    "EventTypeDef",
    "GetExperimentResultsRequestRequestTypeDef",
    "StartExperimentRequestRequestTypeDef",
    "GetExperimentResultsResponseTypeDef",
    "ListExperimentsRequestListExperimentsPaginateTypeDef",
    "ListFeaturesRequestListFeaturesPaginateTypeDef",
    "ListLaunchesRequestListLaunchesPaginateTypeDef",
    "ListProjectsRequestListProjectsPaginateTypeDef",
    "ListSegmentReferencesRequestListSegmentReferencesPaginateTypeDef",
    "ListSegmentsRequestListSegmentsPaginateTypeDef",
    "ListProjectsResponseTypeDef",
    "ListSegmentReferencesResponseTypeDef",
    "MetricGoalConfigTypeDef",
    "MetricMonitorConfigTypeDef",
    "MetricGoalTypeDef",
    "MetricMonitorTypeDef",
    "ProjectDataDeliveryConfigTypeDef",
    "UpdateProjectDataDeliveryRequestRequestTypeDef",
    "ProjectDataDeliveryTypeDef",
    "PutProjectEventsResponseTypeDef",
    "ScheduledSplitTypeDef",
    "SegmentOverrideUnionTypeDef",
    "BatchEvaluateFeatureResponseTypeDef",
    "CreateFeatureRequestRequestTypeDef",
    "UpdateFeatureRequestRequestTypeDef",
    "FeatureTypeDef",
    "ListFeaturesResponseTypeDef",
    "PutProjectEventsRequestRequestTypeDef",
    "CreateExperimentRequestRequestTypeDef",
    "UpdateExperimentRequestRequestTypeDef",
    "ExperimentTypeDef",
    "CreateProjectRequestRequestTypeDef",
    "ProjectTypeDef",
    "ScheduledSplitsLaunchDefinitionTypeDef",
    "ScheduledSplitConfigTypeDef",
    "CreateFeatureResponseTypeDef",
    "GetFeatureResponseTypeDef",
    "UpdateFeatureResponseTypeDef",
    "CreateExperimentResponseTypeDef",
    "GetExperimentResponseTypeDef",
    "ListExperimentsResponseTypeDef",
    "UpdateExperimentResponseTypeDef",
    "CreateProjectResponseTypeDef",
    "GetProjectResponseTypeDef",
    "UpdateProjectDataDeliveryResponseTypeDef",
    "UpdateProjectResponseTypeDef",
    "LaunchTypeDef",
    "ScheduledSplitsLaunchConfigTypeDef",
    "CreateLaunchResponseTypeDef",
    "GetLaunchResponseTypeDef",
    "ListLaunchesResponseTypeDef",
    "StartLaunchResponseTypeDef",
    "UpdateLaunchResponseTypeDef",
    "CreateLaunchRequestRequestTypeDef",
    "UpdateLaunchRequestRequestTypeDef",
)

EvaluationRequestTypeDef = TypedDict(
    "EvaluationRequestTypeDef",
    {
        "entityId": str,
        "feature": str,
        "evaluationContext": NotRequired[str],
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
CloudWatchLogsDestinationConfigTypeDef = TypedDict(
    "CloudWatchLogsDestinationConfigTypeDef",
    {
        "logGroup": NotRequired[str],
    },
)
CloudWatchLogsDestinationTypeDef = TypedDict(
    "CloudWatchLogsDestinationTypeDef",
    {
        "logGroup": NotRequired[str],
    },
)
OnlineAbConfigTypeDef = TypedDict(
    "OnlineAbConfigTypeDef",
    {
        "controlTreatmentName": NotRequired[str],
        "treatmentWeights": NotRequired[Mapping[str, int]],
    },
)
TreatmentConfigTypeDef = TypedDict(
    "TreatmentConfigTypeDef",
    {
        "feature": str,
        "name": str,
        "variation": str,
        "description": NotRequired[str],
    },
)
LaunchGroupConfigTypeDef = TypedDict(
    "LaunchGroupConfigTypeDef",
    {
        "feature": str,
        "name": str,
        "variation": str,
        "description": NotRequired[str],
    },
)
ProjectAppConfigResourceConfigTypeDef = TypedDict(
    "ProjectAppConfigResourceConfigTypeDef",
    {
        "applicationId": NotRequired[str],
        "environmentId": NotRequired[str],
    },
)
CreateSegmentRequestRequestTypeDef = TypedDict(
    "CreateSegmentRequestRequestTypeDef",
    {
        "name": str,
        "pattern": str,
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
SegmentTypeDef = TypedDict(
    "SegmentTypeDef",
    {
        "arn": str,
        "createdTime": datetime,
        "lastUpdatedTime": datetime,
        "name": str,
        "pattern": str,
        "description": NotRequired[str],
        "experimentCount": NotRequired[int],
        "launchCount": NotRequired[int],
        "tags": NotRequired[Dict[str, str]],
    },
)
DeleteExperimentRequestRequestTypeDef = TypedDict(
    "DeleteExperimentRequestRequestTypeDef",
    {
        "experiment": str,
        "project": str,
    },
)
DeleteFeatureRequestRequestTypeDef = TypedDict(
    "DeleteFeatureRequestRequestTypeDef",
    {
        "feature": str,
        "project": str,
    },
)
DeleteLaunchRequestRequestTypeDef = TypedDict(
    "DeleteLaunchRequestRequestTypeDef",
    {
        "launch": str,
        "project": str,
    },
)
DeleteProjectRequestRequestTypeDef = TypedDict(
    "DeleteProjectRequestRequestTypeDef",
    {
        "project": str,
    },
)
DeleteSegmentRequestRequestTypeDef = TypedDict(
    "DeleteSegmentRequestRequestTypeDef",
    {
        "segment": str,
    },
)
EvaluateFeatureRequestRequestTypeDef = TypedDict(
    "EvaluateFeatureRequestRequestTypeDef",
    {
        "entityId": str,
        "feature": str,
        "project": str,
        "evaluationContext": NotRequired[str],
    },
)
VariableValueTypeDef = TypedDict(
    "VariableValueTypeDef",
    {
        "boolValue": NotRequired[bool],
        "doubleValue": NotRequired[float],
        "longValue": NotRequired[int],
        "stringValue": NotRequired[str],
    },
)
EvaluationRuleTypeDef = TypedDict(
    "EvaluationRuleTypeDef",
    {
        "type": str,
        "name": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
ExperimentExecutionTypeDef = TypedDict(
    "ExperimentExecutionTypeDef",
    {
        "endedTime": NotRequired[datetime],
        "startedTime": NotRequired[datetime],
    },
)
ExperimentReportTypeDef = TypedDict(
    "ExperimentReportTypeDef",
    {
        "content": NotRequired[str],
        "metricName": NotRequired[str],
        "reportName": NotRequired[Literal["BayesianInference"]],
        "treatmentName": NotRequired[str],
    },
)
ExperimentResultsDataTypeDef = TypedDict(
    "ExperimentResultsDataTypeDef",
    {
        "metricName": NotRequired[str],
        "resultStat": NotRequired[ExperimentResultResponseTypeType],
        "treatmentName": NotRequired[str],
        "values": NotRequired[List[float]],
    },
)
ExperimentScheduleTypeDef = TypedDict(
    "ExperimentScheduleTypeDef",
    {
        "analysisCompleteTime": NotRequired[datetime],
    },
)
OnlineAbDefinitionTypeDef = TypedDict(
    "OnlineAbDefinitionTypeDef",
    {
        "controlTreatmentName": NotRequired[str],
        "treatmentWeights": NotRequired[Dict[str, int]],
    },
)
TreatmentTypeDef = TypedDict(
    "TreatmentTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "featureVariations": NotRequired[Dict[str, str]],
    },
)
GetExperimentRequestRequestTypeDef = TypedDict(
    "GetExperimentRequestRequestTypeDef",
    {
        "experiment": str,
        "project": str,
    },
)
GetFeatureRequestRequestTypeDef = TypedDict(
    "GetFeatureRequestRequestTypeDef",
    {
        "feature": str,
        "project": str,
    },
)
GetLaunchRequestRequestTypeDef = TypedDict(
    "GetLaunchRequestRequestTypeDef",
    {
        "launch": str,
        "project": str,
    },
)
GetProjectRequestRequestTypeDef = TypedDict(
    "GetProjectRequestRequestTypeDef",
    {
        "project": str,
    },
)
GetSegmentRequestRequestTypeDef = TypedDict(
    "GetSegmentRequestRequestTypeDef",
    {
        "segment": str,
    },
)
LaunchExecutionTypeDef = TypedDict(
    "LaunchExecutionTypeDef",
    {
        "endedTime": NotRequired[datetime],
        "startedTime": NotRequired[datetime],
    },
)
LaunchGroupTypeDef = TypedDict(
    "LaunchGroupTypeDef",
    {
        "featureVariations": Dict[str, str],
        "name": str,
        "description": NotRequired[str],
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
ListExperimentsRequestRequestTypeDef = TypedDict(
    "ListExperimentsRequestRequestTypeDef",
    {
        "project": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "status": NotRequired[ExperimentStatusType],
    },
)
ListFeaturesRequestRequestTypeDef = TypedDict(
    "ListFeaturesRequestRequestTypeDef",
    {
        "project": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListLaunchesRequestRequestTypeDef = TypedDict(
    "ListLaunchesRequestRequestTypeDef",
    {
        "project": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "status": NotRequired[LaunchStatusType],
    },
)
ListProjectsRequestRequestTypeDef = TypedDict(
    "ListProjectsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ProjectSummaryTypeDef = TypedDict(
    "ProjectSummaryTypeDef",
    {
        "arn": str,
        "createdTime": datetime,
        "lastUpdatedTime": datetime,
        "name": str,
        "status": ProjectStatusType,
        "activeExperimentCount": NotRequired[int],
        "activeLaunchCount": NotRequired[int],
        "description": NotRequired[str],
        "experimentCount": NotRequired[int],
        "featureCount": NotRequired[int],
        "launchCount": NotRequired[int],
        "tags": NotRequired[Dict[str, str]],
    },
)
ListSegmentReferencesRequestRequestTypeDef = TypedDict(
    "ListSegmentReferencesRequestRequestTypeDef",
    {
        "segment": str,
        "type": SegmentReferenceResourceTypeType,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
RefResourceTypeDef = TypedDict(
    "RefResourceTypeDef",
    {
        "name": str,
        "type": str,
        "arn": NotRequired[str],
        "endTime": NotRequired[str],
        "lastUpdatedOn": NotRequired[str],
        "startTime": NotRequired[str],
        "status": NotRequired[str],
    },
)
ListSegmentsRequestRequestTypeDef = TypedDict(
    "ListSegmentsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
MetricDefinitionConfigTypeDef = TypedDict(
    "MetricDefinitionConfigTypeDef",
    {
        "entityIdKey": str,
        "name": str,
        "valueKey": str,
        "eventPattern": NotRequired[str],
        "unitLabel": NotRequired[str],
    },
)
MetricDefinitionTypeDef = TypedDict(
    "MetricDefinitionTypeDef",
    {
        "entityIdKey": NotRequired[str],
        "eventPattern": NotRequired[str],
        "name": NotRequired[str],
        "unitLabel": NotRequired[str],
        "valueKey": NotRequired[str],
    },
)
ProjectAppConfigResourceTypeDef = TypedDict(
    "ProjectAppConfigResourceTypeDef",
    {
        "applicationId": str,
        "configurationProfileId": str,
        "environmentId": str,
    },
)
S3DestinationConfigTypeDef = TypedDict(
    "S3DestinationConfigTypeDef",
    {
        "bucket": NotRequired[str],
        "prefix": NotRequired[str],
    },
)
S3DestinationTypeDef = TypedDict(
    "S3DestinationTypeDef",
    {
        "bucket": NotRequired[str],
        "prefix": NotRequired[str],
    },
)
PutProjectEventsResultEntryTypeDef = TypedDict(
    "PutProjectEventsResultEntryTypeDef",
    {
        "errorCode": NotRequired[str],
        "errorMessage": NotRequired[str],
        "eventId": NotRequired[str],
    },
)
SegmentOverrideOutputTypeDef = TypedDict(
    "SegmentOverrideOutputTypeDef",
    {
        "evaluationOrder": int,
        "segment": str,
        "weights": Dict[str, int],
    },
)
SegmentOverrideTypeDef = TypedDict(
    "SegmentOverrideTypeDef",
    {
        "evaluationOrder": int,
        "segment": str,
        "weights": Mapping[str, int],
    },
)
StartLaunchRequestRequestTypeDef = TypedDict(
    "StartLaunchRequestRequestTypeDef",
    {
        "launch": str,
        "project": str,
    },
)
StopExperimentRequestRequestTypeDef = TypedDict(
    "StopExperimentRequestRequestTypeDef",
    {
        "experiment": str,
        "project": str,
        "desiredState": NotRequired[ExperimentStopDesiredStateType],
        "reason": NotRequired[str],
    },
)
StopLaunchRequestRequestTypeDef = TypedDict(
    "StopLaunchRequestRequestTypeDef",
    {
        "launch": str,
        "project": str,
        "desiredState": NotRequired[LaunchStopDesiredStateType],
        "reason": NotRequired[str],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)
TestSegmentPatternRequestRequestTypeDef = TypedDict(
    "TestSegmentPatternRequestRequestTypeDef",
    {
        "pattern": str,
        "payload": str,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
BatchEvaluateFeatureRequestRequestTypeDef = TypedDict(
    "BatchEvaluateFeatureRequestRequestTypeDef",
    {
        "project": str,
        "requests": Sequence[EvaluationRequestTypeDef],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartExperimentResponseTypeDef = TypedDict(
    "StartExperimentResponseTypeDef",
    {
        "startedTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopExperimentResponseTypeDef = TypedDict(
    "StopExperimentResponseTypeDef",
    {
        "endedTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopLaunchResponseTypeDef = TypedDict(
    "StopLaunchResponseTypeDef",
    {
        "endedTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TestSegmentPatternResponseTypeDef = TypedDict(
    "TestSegmentPatternResponseTypeDef",
    {
        "match": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateProjectRequestRequestTypeDef = TypedDict(
    "UpdateProjectRequestRequestTypeDef",
    {
        "project": str,
        "appConfigResource": NotRequired[ProjectAppConfigResourceConfigTypeDef],
        "description": NotRequired[str],
    },
)
CreateSegmentResponseTypeDef = TypedDict(
    "CreateSegmentResponseTypeDef",
    {
        "segment": SegmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSegmentResponseTypeDef = TypedDict(
    "GetSegmentResponseTypeDef",
    {
        "segment": SegmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSegmentsResponseTypeDef = TypedDict(
    "ListSegmentsResponseTypeDef",
    {
        "nextToken": str,
        "segments": List[SegmentTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EvaluateFeatureResponseTypeDef = TypedDict(
    "EvaluateFeatureResponseTypeDef",
    {
        "details": str,
        "reason": str,
        "value": VariableValueTypeDef,
        "variation": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EvaluationResultTypeDef = TypedDict(
    "EvaluationResultTypeDef",
    {
        "entityId": str,
        "feature": str,
        "details": NotRequired[str],
        "project": NotRequired[str],
        "reason": NotRequired[str],
        "value": NotRequired[VariableValueTypeDef],
        "variation": NotRequired[str],
    },
)
VariationConfigTypeDef = TypedDict(
    "VariationConfigTypeDef",
    {
        "name": str,
        "value": VariableValueTypeDef,
    },
)
VariationTypeDef = TypedDict(
    "VariationTypeDef",
    {
        "name": NotRequired[str],
        "value": NotRequired[VariableValueTypeDef],
    },
)
FeatureSummaryTypeDef = TypedDict(
    "FeatureSummaryTypeDef",
    {
        "arn": str,
        "createdTime": datetime,
        "evaluationStrategy": FeatureEvaluationStrategyType,
        "lastUpdatedTime": datetime,
        "name": str,
        "status": FeatureStatusType,
        "defaultVariation": NotRequired[str],
        "evaluationRules": NotRequired[List[EvaluationRuleTypeDef]],
        "project": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)
EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "data": str,
        "timestamp": TimestampTypeDef,
        "type": EventTypeType,
    },
)
GetExperimentResultsRequestRequestTypeDef = TypedDict(
    "GetExperimentResultsRequestRequestTypeDef",
    {
        "experiment": str,
        "metricNames": Sequence[str],
        "project": str,
        "treatmentNames": Sequence[str],
        "baseStat": NotRequired[Literal["Mean"]],
        "endTime": NotRequired[TimestampTypeDef],
        "period": NotRequired[int],
        "reportNames": NotRequired[Sequence[Literal["BayesianInference"]]],
        "resultStats": NotRequired[Sequence[ExperimentResultRequestTypeType]],
        "startTime": NotRequired[TimestampTypeDef],
    },
)
StartExperimentRequestRequestTypeDef = TypedDict(
    "StartExperimentRequestRequestTypeDef",
    {
        "analysisCompleteTime": TimestampTypeDef,
        "experiment": str,
        "project": str,
    },
)
GetExperimentResultsResponseTypeDef = TypedDict(
    "GetExperimentResultsResponseTypeDef",
    {
        "details": str,
        "reports": List[ExperimentReportTypeDef],
        "resultsData": List[ExperimentResultsDataTypeDef],
        "timestamps": List[datetime],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListExperimentsRequestListExperimentsPaginateTypeDef = TypedDict(
    "ListExperimentsRequestListExperimentsPaginateTypeDef",
    {
        "project": str,
        "status": NotRequired[ExperimentStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFeaturesRequestListFeaturesPaginateTypeDef = TypedDict(
    "ListFeaturesRequestListFeaturesPaginateTypeDef",
    {
        "project": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListLaunchesRequestListLaunchesPaginateTypeDef = TypedDict(
    "ListLaunchesRequestListLaunchesPaginateTypeDef",
    {
        "project": str,
        "status": NotRequired[LaunchStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProjectsRequestListProjectsPaginateTypeDef = TypedDict(
    "ListProjectsRequestListProjectsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSegmentReferencesRequestListSegmentReferencesPaginateTypeDef = TypedDict(
    "ListSegmentReferencesRequestListSegmentReferencesPaginateTypeDef",
    {
        "segment": str,
        "type": SegmentReferenceResourceTypeType,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSegmentsRequestListSegmentsPaginateTypeDef = TypedDict(
    "ListSegmentsRequestListSegmentsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProjectsResponseTypeDef = TypedDict(
    "ListProjectsResponseTypeDef",
    {
        "nextToken": str,
        "projects": List[ProjectSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSegmentReferencesResponseTypeDef = TypedDict(
    "ListSegmentReferencesResponseTypeDef",
    {
        "nextToken": str,
        "referencedBy": List[RefResourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MetricGoalConfigTypeDef = TypedDict(
    "MetricGoalConfigTypeDef",
    {
        "metricDefinition": MetricDefinitionConfigTypeDef,
        "desiredChange": NotRequired[ChangeDirectionEnumType],
    },
)
MetricMonitorConfigTypeDef = TypedDict(
    "MetricMonitorConfigTypeDef",
    {
        "metricDefinition": MetricDefinitionConfigTypeDef,
    },
)
MetricGoalTypeDef = TypedDict(
    "MetricGoalTypeDef",
    {
        "metricDefinition": MetricDefinitionTypeDef,
        "desiredChange": NotRequired[ChangeDirectionEnumType],
    },
)
MetricMonitorTypeDef = TypedDict(
    "MetricMonitorTypeDef",
    {
        "metricDefinition": MetricDefinitionTypeDef,
    },
)
ProjectDataDeliveryConfigTypeDef = TypedDict(
    "ProjectDataDeliveryConfigTypeDef",
    {
        "cloudWatchLogs": NotRequired[CloudWatchLogsDestinationConfigTypeDef],
        "s3Destination": NotRequired[S3DestinationConfigTypeDef],
    },
)
UpdateProjectDataDeliveryRequestRequestTypeDef = TypedDict(
    "UpdateProjectDataDeliveryRequestRequestTypeDef",
    {
        "project": str,
        "cloudWatchLogs": NotRequired[CloudWatchLogsDestinationConfigTypeDef],
        "s3Destination": NotRequired[S3DestinationConfigTypeDef],
    },
)
ProjectDataDeliveryTypeDef = TypedDict(
    "ProjectDataDeliveryTypeDef",
    {
        "cloudWatchLogs": NotRequired[CloudWatchLogsDestinationTypeDef],
        "s3Destination": NotRequired[S3DestinationTypeDef],
    },
)
PutProjectEventsResponseTypeDef = TypedDict(
    "PutProjectEventsResponseTypeDef",
    {
        "eventResults": List[PutProjectEventsResultEntryTypeDef],
        "failedEventCount": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ScheduledSplitTypeDef = TypedDict(
    "ScheduledSplitTypeDef",
    {
        "startTime": datetime,
        "groupWeights": NotRequired[Dict[str, int]],
        "segmentOverrides": NotRequired[List[SegmentOverrideOutputTypeDef]],
    },
)
SegmentOverrideUnionTypeDef = Union[SegmentOverrideTypeDef, SegmentOverrideOutputTypeDef]
BatchEvaluateFeatureResponseTypeDef = TypedDict(
    "BatchEvaluateFeatureResponseTypeDef",
    {
        "results": List[EvaluationResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFeatureRequestRequestTypeDef = TypedDict(
    "CreateFeatureRequestRequestTypeDef",
    {
        "name": str,
        "project": str,
        "variations": Sequence[VariationConfigTypeDef],
        "defaultVariation": NotRequired[str],
        "description": NotRequired[str],
        "entityOverrides": NotRequired[Mapping[str, str]],
        "evaluationStrategy": NotRequired[FeatureEvaluationStrategyType],
        "tags": NotRequired[Mapping[str, str]],
    },
)
UpdateFeatureRequestRequestTypeDef = TypedDict(
    "UpdateFeatureRequestRequestTypeDef",
    {
        "feature": str,
        "project": str,
        "addOrUpdateVariations": NotRequired[Sequence[VariationConfigTypeDef]],
        "defaultVariation": NotRequired[str],
        "description": NotRequired[str],
        "entityOverrides": NotRequired[Mapping[str, str]],
        "evaluationStrategy": NotRequired[FeatureEvaluationStrategyType],
        "removeVariations": NotRequired[Sequence[str]],
    },
)
FeatureTypeDef = TypedDict(
    "FeatureTypeDef",
    {
        "arn": str,
        "createdTime": datetime,
        "evaluationStrategy": FeatureEvaluationStrategyType,
        "lastUpdatedTime": datetime,
        "name": str,
        "status": FeatureStatusType,
        "valueType": VariationValueTypeType,
        "variations": List[VariationTypeDef],
        "defaultVariation": NotRequired[str],
        "description": NotRequired[str],
        "entityOverrides": NotRequired[Dict[str, str]],
        "evaluationRules": NotRequired[List[EvaluationRuleTypeDef]],
        "project": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)
ListFeaturesResponseTypeDef = TypedDict(
    "ListFeaturesResponseTypeDef",
    {
        "features": List[FeatureSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutProjectEventsRequestRequestTypeDef = TypedDict(
    "PutProjectEventsRequestRequestTypeDef",
    {
        "events": Sequence[EventTypeDef],
        "project": str,
    },
)
CreateExperimentRequestRequestTypeDef = TypedDict(
    "CreateExperimentRequestRequestTypeDef",
    {
        "metricGoals": Sequence[MetricGoalConfigTypeDef],
        "name": str,
        "project": str,
        "treatments": Sequence[TreatmentConfigTypeDef],
        "description": NotRequired[str],
        "onlineAbConfig": NotRequired[OnlineAbConfigTypeDef],
        "randomizationSalt": NotRequired[str],
        "samplingRate": NotRequired[int],
        "segment": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
UpdateExperimentRequestRequestTypeDef = TypedDict(
    "UpdateExperimentRequestRequestTypeDef",
    {
        "experiment": str,
        "project": str,
        "description": NotRequired[str],
        "metricGoals": NotRequired[Sequence[MetricGoalConfigTypeDef]],
        "onlineAbConfig": NotRequired[OnlineAbConfigTypeDef],
        "randomizationSalt": NotRequired[str],
        "removeSegment": NotRequired[bool],
        "samplingRate": NotRequired[int],
        "segment": NotRequired[str],
        "treatments": NotRequired[Sequence[TreatmentConfigTypeDef]],
    },
)
ExperimentTypeDef = TypedDict(
    "ExperimentTypeDef",
    {
        "arn": str,
        "createdTime": datetime,
        "lastUpdatedTime": datetime,
        "name": str,
        "status": ExperimentStatusType,
        "type": Literal["aws.evidently.onlineab"],
        "description": NotRequired[str],
        "execution": NotRequired[ExperimentExecutionTypeDef],
        "metricGoals": NotRequired[List[MetricGoalTypeDef]],
        "onlineAbDefinition": NotRequired[OnlineAbDefinitionTypeDef],
        "project": NotRequired[str],
        "randomizationSalt": NotRequired[str],
        "samplingRate": NotRequired[int],
        "schedule": NotRequired[ExperimentScheduleTypeDef],
        "segment": NotRequired[str],
        "statusReason": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "treatments": NotRequired[List[TreatmentTypeDef]],
    },
)
CreateProjectRequestRequestTypeDef = TypedDict(
    "CreateProjectRequestRequestTypeDef",
    {
        "name": str,
        "appConfigResource": NotRequired[ProjectAppConfigResourceConfigTypeDef],
        "dataDelivery": NotRequired[ProjectDataDeliveryConfigTypeDef],
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
ProjectTypeDef = TypedDict(
    "ProjectTypeDef",
    {
        "arn": str,
        "createdTime": datetime,
        "lastUpdatedTime": datetime,
        "name": str,
        "status": ProjectStatusType,
        "activeExperimentCount": NotRequired[int],
        "activeLaunchCount": NotRequired[int],
        "appConfigResource": NotRequired[ProjectAppConfigResourceTypeDef],
        "dataDelivery": NotRequired[ProjectDataDeliveryTypeDef],
        "description": NotRequired[str],
        "experimentCount": NotRequired[int],
        "featureCount": NotRequired[int],
        "launchCount": NotRequired[int],
        "tags": NotRequired[Dict[str, str]],
    },
)
ScheduledSplitsLaunchDefinitionTypeDef = TypedDict(
    "ScheduledSplitsLaunchDefinitionTypeDef",
    {
        "steps": NotRequired[List[ScheduledSplitTypeDef]],
    },
)
ScheduledSplitConfigTypeDef = TypedDict(
    "ScheduledSplitConfigTypeDef",
    {
        "groupWeights": Mapping[str, int],
        "startTime": TimestampTypeDef,
        "segmentOverrides": NotRequired[Sequence[SegmentOverrideUnionTypeDef]],
    },
)
CreateFeatureResponseTypeDef = TypedDict(
    "CreateFeatureResponseTypeDef",
    {
        "feature": FeatureTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFeatureResponseTypeDef = TypedDict(
    "GetFeatureResponseTypeDef",
    {
        "feature": FeatureTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFeatureResponseTypeDef = TypedDict(
    "UpdateFeatureResponseTypeDef",
    {
        "feature": FeatureTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateExperimentResponseTypeDef = TypedDict(
    "CreateExperimentResponseTypeDef",
    {
        "experiment": ExperimentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetExperimentResponseTypeDef = TypedDict(
    "GetExperimentResponseTypeDef",
    {
        "experiment": ExperimentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListExperimentsResponseTypeDef = TypedDict(
    "ListExperimentsResponseTypeDef",
    {
        "experiments": List[ExperimentTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateExperimentResponseTypeDef = TypedDict(
    "UpdateExperimentResponseTypeDef",
    {
        "experiment": ExperimentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProjectResponseTypeDef = TypedDict(
    "CreateProjectResponseTypeDef",
    {
        "project": ProjectTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetProjectResponseTypeDef = TypedDict(
    "GetProjectResponseTypeDef",
    {
        "project": ProjectTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateProjectDataDeliveryResponseTypeDef = TypedDict(
    "UpdateProjectDataDeliveryResponseTypeDef",
    {
        "project": ProjectTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateProjectResponseTypeDef = TypedDict(
    "UpdateProjectResponseTypeDef",
    {
        "project": ProjectTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LaunchTypeDef = TypedDict(
    "LaunchTypeDef",
    {
        "arn": str,
        "createdTime": datetime,
        "lastUpdatedTime": datetime,
        "name": str,
        "status": LaunchStatusType,
        "type": Literal["aws.evidently.splits"],
        "description": NotRequired[str],
        "execution": NotRequired[LaunchExecutionTypeDef],
        "groups": NotRequired[List[LaunchGroupTypeDef]],
        "metricMonitors": NotRequired[List[MetricMonitorTypeDef]],
        "project": NotRequired[str],
        "randomizationSalt": NotRequired[str],
        "scheduledSplitsDefinition": NotRequired[ScheduledSplitsLaunchDefinitionTypeDef],
        "statusReason": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)
ScheduledSplitsLaunchConfigTypeDef = TypedDict(
    "ScheduledSplitsLaunchConfigTypeDef",
    {
        "steps": Sequence[ScheduledSplitConfigTypeDef],
    },
)
CreateLaunchResponseTypeDef = TypedDict(
    "CreateLaunchResponseTypeDef",
    {
        "launch": LaunchTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLaunchResponseTypeDef = TypedDict(
    "GetLaunchResponseTypeDef",
    {
        "launch": LaunchTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListLaunchesResponseTypeDef = TypedDict(
    "ListLaunchesResponseTypeDef",
    {
        "launches": List[LaunchTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartLaunchResponseTypeDef = TypedDict(
    "StartLaunchResponseTypeDef",
    {
        "launch": LaunchTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateLaunchResponseTypeDef = TypedDict(
    "UpdateLaunchResponseTypeDef",
    {
        "launch": LaunchTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateLaunchRequestRequestTypeDef = TypedDict(
    "CreateLaunchRequestRequestTypeDef",
    {
        "groups": Sequence[LaunchGroupConfigTypeDef],
        "name": str,
        "project": str,
        "description": NotRequired[str],
        "metricMonitors": NotRequired[Sequence[MetricMonitorConfigTypeDef]],
        "randomizationSalt": NotRequired[str],
        "scheduledSplitsConfig": NotRequired[ScheduledSplitsLaunchConfigTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
UpdateLaunchRequestRequestTypeDef = TypedDict(
    "UpdateLaunchRequestRequestTypeDef",
    {
        "launch": str,
        "project": str,
        "description": NotRequired[str],
        "groups": NotRequired[Sequence[LaunchGroupConfigTypeDef]],
        "metricMonitors": NotRequired[Sequence[MetricMonitorConfigTypeDef]],
        "randomizationSalt": NotRequired[str],
        "scheduledSplitsConfig": NotRequired[ScheduledSplitsLaunchConfigTypeDef],
    },
)
