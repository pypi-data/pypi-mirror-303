"""
Type annotations for application-signals service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_signals/type_defs/)

Usage::

    ```python
    from mypy_boto3_application_signals.type_defs import TimestampTypeDef

    data: TimestampTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    DurationUnitType,
    EvaluationTypeType,
    ServiceLevelIndicatorComparisonOperatorType,
    ServiceLevelIndicatorMetricTypeType,
    ServiceLevelObjectiveBudgetStatusType,
    StandardUnitType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "TimestampTypeDef",
    "ResponseMetadataTypeDef",
    "ServiceLevelObjectiveBudgetReportErrorTypeDef",
    "CalendarIntervalOutputTypeDef",
    "TagTypeDef",
    "DeleteServiceLevelObjectiveInputRequestTypeDef",
    "DimensionTypeDef",
    "GetServiceLevelObjectiveInputRequestTypeDef",
    "RollingIntervalTypeDef",
    "PaginatorConfigTypeDef",
    "ListServiceLevelObjectivesInputRequestTypeDef",
    "ServiceLevelObjectiveSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "BatchGetServiceLevelObjectiveBudgetReportInputRequestTypeDef",
    "CalendarIntervalTypeDef",
    "GetServiceInputRequestTypeDef",
    "ListServiceDependenciesInputRequestTypeDef",
    "ListServiceDependentsInputRequestTypeDef",
    "ListServiceOperationsInputRequestTypeDef",
    "ListServicesInputRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "MetricOutputTypeDef",
    "MetricReferenceTypeDef",
    "MetricTypeDef",
    "IntervalOutputTypeDef",
    "ListServiceDependenciesInputListServiceDependenciesPaginateTypeDef",
    "ListServiceDependentsInputListServiceDependentsPaginateTypeDef",
    "ListServiceLevelObjectivesInputListServiceLevelObjectivesPaginateTypeDef",
    "ListServiceOperationsInputListServiceOperationsPaginateTypeDef",
    "ListServicesInputListServicesPaginateTypeDef",
    "ListServiceLevelObjectivesOutputTypeDef",
    "CalendarIntervalUnionTypeDef",
    "MetricStatOutputTypeDef",
    "ServiceDependencyTypeDef",
    "ServiceDependentTypeDef",
    "ServiceOperationTypeDef",
    "ServiceSummaryTypeDef",
    "ServiceTypeDef",
    "MetricUnionTypeDef",
    "GoalOutputTypeDef",
    "IntervalTypeDef",
    "MetricDataQueryOutputTypeDef",
    "ListServiceDependenciesOutputTypeDef",
    "ListServiceDependentsOutputTypeDef",
    "ListServiceOperationsOutputTypeDef",
    "ListServicesOutputTypeDef",
    "GetServiceOutputTypeDef",
    "MetricStatTypeDef",
    "IntervalUnionTypeDef",
    "MonitoredRequestCountMetricDataQueriesOutputTypeDef",
    "ServiceLevelIndicatorMetricTypeDef",
    "MetricStatUnionTypeDef",
    "GoalTypeDef",
    "RequestBasedServiceLevelIndicatorMetricTypeDef",
    "ServiceLevelIndicatorTypeDef",
    "MetricDataQueryTypeDef",
    "RequestBasedServiceLevelIndicatorTypeDef",
    "MetricDataQueryUnionTypeDef",
    "MonitoredRequestCountMetricDataQueriesTypeDef",
    "ServiceLevelObjectiveBudgetReportTypeDef",
    "ServiceLevelObjectiveTypeDef",
    "ServiceLevelIndicatorMetricConfigTypeDef",
    "MonitoredRequestCountMetricDataQueriesUnionTypeDef",
    "BatchGetServiceLevelObjectiveBudgetReportOutputTypeDef",
    "CreateServiceLevelObjectiveOutputTypeDef",
    "GetServiceLevelObjectiveOutputTypeDef",
    "UpdateServiceLevelObjectiveOutputTypeDef",
    "ServiceLevelIndicatorConfigTypeDef",
    "RequestBasedServiceLevelIndicatorMetricConfigTypeDef",
    "RequestBasedServiceLevelIndicatorConfigTypeDef",
    "CreateServiceLevelObjectiveInputRequestTypeDef",
    "UpdateServiceLevelObjectiveInputRequestTypeDef",
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
ServiceLevelObjectiveBudgetReportErrorTypeDef = TypedDict(
    "ServiceLevelObjectiveBudgetReportErrorTypeDef",
    {
        "Name": str,
        "Arn": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
)
CalendarIntervalOutputTypeDef = TypedDict(
    "CalendarIntervalOutputTypeDef",
    {
        "StartTime": datetime,
        "DurationUnit": DurationUnitType,
        "Duration": int,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
DeleteServiceLevelObjectiveInputRequestTypeDef = TypedDict(
    "DeleteServiceLevelObjectiveInputRequestTypeDef",
    {
        "Id": str,
    },
)
DimensionTypeDef = TypedDict(
    "DimensionTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)
GetServiceLevelObjectiveInputRequestTypeDef = TypedDict(
    "GetServiceLevelObjectiveInputRequestTypeDef",
    {
        "Id": str,
    },
)
RollingIntervalTypeDef = TypedDict(
    "RollingIntervalTypeDef",
    {
        "DurationUnit": DurationUnitType,
        "Duration": int,
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
ListServiceLevelObjectivesInputRequestTypeDef = TypedDict(
    "ListServiceLevelObjectivesInputRequestTypeDef",
    {
        "KeyAttributes": NotRequired[Mapping[str, str]],
        "OperationName": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ServiceLevelObjectiveSummaryTypeDef = TypedDict(
    "ServiceLevelObjectiveSummaryTypeDef",
    {
        "Arn": str,
        "Name": str,
        "KeyAttributes": NotRequired[Dict[str, str]],
        "OperationName": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
BatchGetServiceLevelObjectiveBudgetReportInputRequestTypeDef = TypedDict(
    "BatchGetServiceLevelObjectiveBudgetReportInputRequestTypeDef",
    {
        "Timestamp": TimestampTypeDef,
        "SloIds": Sequence[str],
    },
)
CalendarIntervalTypeDef = TypedDict(
    "CalendarIntervalTypeDef",
    {
        "StartTime": TimestampTypeDef,
        "DurationUnit": DurationUnitType,
        "Duration": int,
    },
)
GetServiceInputRequestTypeDef = TypedDict(
    "GetServiceInputRequestTypeDef",
    {
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
        "KeyAttributes": Mapping[str, str],
    },
)
ListServiceDependenciesInputRequestTypeDef = TypedDict(
    "ListServiceDependenciesInputRequestTypeDef",
    {
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
        "KeyAttributes": Mapping[str, str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListServiceDependentsInputRequestTypeDef = TypedDict(
    "ListServiceDependentsInputRequestTypeDef",
    {
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
        "KeyAttributes": Mapping[str, str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListServiceOperationsInputRequestTypeDef = TypedDict(
    "ListServiceOperationsInputRequestTypeDef",
    {
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
        "KeyAttributes": Mapping[str, str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListServicesInputRequestTypeDef = TypedDict(
    "ListServicesInputRequestTypeDef",
    {
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
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
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
MetricOutputTypeDef = TypedDict(
    "MetricOutputTypeDef",
    {
        "Namespace": NotRequired[str],
        "MetricName": NotRequired[str],
        "Dimensions": NotRequired[List[DimensionTypeDef]],
    },
)
MetricReferenceTypeDef = TypedDict(
    "MetricReferenceTypeDef",
    {
        "Namespace": str,
        "MetricType": str,
        "MetricName": str,
        "Dimensions": NotRequired[List[DimensionTypeDef]],
    },
)
MetricTypeDef = TypedDict(
    "MetricTypeDef",
    {
        "Namespace": NotRequired[str],
        "MetricName": NotRequired[str],
        "Dimensions": NotRequired[Sequence[DimensionTypeDef]],
    },
)
IntervalOutputTypeDef = TypedDict(
    "IntervalOutputTypeDef",
    {
        "RollingInterval": NotRequired[RollingIntervalTypeDef],
        "CalendarInterval": NotRequired[CalendarIntervalOutputTypeDef],
    },
)
ListServiceDependenciesInputListServiceDependenciesPaginateTypeDef = TypedDict(
    "ListServiceDependenciesInputListServiceDependenciesPaginateTypeDef",
    {
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
        "KeyAttributes": Mapping[str, str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListServiceDependentsInputListServiceDependentsPaginateTypeDef = TypedDict(
    "ListServiceDependentsInputListServiceDependentsPaginateTypeDef",
    {
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
        "KeyAttributes": Mapping[str, str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListServiceLevelObjectivesInputListServiceLevelObjectivesPaginateTypeDef = TypedDict(
    "ListServiceLevelObjectivesInputListServiceLevelObjectivesPaginateTypeDef",
    {
        "KeyAttributes": NotRequired[Mapping[str, str]],
        "OperationName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListServiceOperationsInputListServiceOperationsPaginateTypeDef = TypedDict(
    "ListServiceOperationsInputListServiceOperationsPaginateTypeDef",
    {
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
        "KeyAttributes": Mapping[str, str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListServicesInputListServicesPaginateTypeDef = TypedDict(
    "ListServicesInputListServicesPaginateTypeDef",
    {
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListServiceLevelObjectivesOutputTypeDef = TypedDict(
    "ListServiceLevelObjectivesOutputTypeDef",
    {
        "SloSummaries": List[ServiceLevelObjectiveSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CalendarIntervalUnionTypeDef = Union[CalendarIntervalTypeDef, CalendarIntervalOutputTypeDef]
MetricStatOutputTypeDef = TypedDict(
    "MetricStatOutputTypeDef",
    {
        "Metric": MetricOutputTypeDef,
        "Period": int,
        "Stat": str,
        "Unit": NotRequired[StandardUnitType],
    },
)
ServiceDependencyTypeDef = TypedDict(
    "ServiceDependencyTypeDef",
    {
        "OperationName": str,
        "DependencyKeyAttributes": Dict[str, str],
        "DependencyOperationName": str,
        "MetricReferences": List[MetricReferenceTypeDef],
    },
)
ServiceDependentTypeDef = TypedDict(
    "ServiceDependentTypeDef",
    {
        "DependentKeyAttributes": Dict[str, str],
        "MetricReferences": List[MetricReferenceTypeDef],
        "OperationName": NotRequired[str],
        "DependentOperationName": NotRequired[str],
    },
)
ServiceOperationTypeDef = TypedDict(
    "ServiceOperationTypeDef",
    {
        "Name": str,
        "MetricReferences": List[MetricReferenceTypeDef],
    },
)
ServiceSummaryTypeDef = TypedDict(
    "ServiceSummaryTypeDef",
    {
        "KeyAttributes": Dict[str, str],
        "MetricReferences": List[MetricReferenceTypeDef],
        "AttributeMaps": NotRequired[List[Dict[str, str]]],
    },
)
ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "KeyAttributes": Dict[str, str],
        "MetricReferences": List[MetricReferenceTypeDef],
        "AttributeMaps": NotRequired[List[Dict[str, str]]],
        "LogGroupReferences": NotRequired[List[Dict[str, str]]],
    },
)
MetricUnionTypeDef = Union[MetricTypeDef, MetricOutputTypeDef]
GoalOutputTypeDef = TypedDict(
    "GoalOutputTypeDef",
    {
        "Interval": NotRequired[IntervalOutputTypeDef],
        "AttainmentGoal": NotRequired[float],
        "WarningThreshold": NotRequired[float],
    },
)
IntervalTypeDef = TypedDict(
    "IntervalTypeDef",
    {
        "RollingInterval": NotRequired[RollingIntervalTypeDef],
        "CalendarInterval": NotRequired[CalendarIntervalUnionTypeDef],
    },
)
MetricDataQueryOutputTypeDef = TypedDict(
    "MetricDataQueryOutputTypeDef",
    {
        "Id": str,
        "MetricStat": NotRequired[MetricStatOutputTypeDef],
        "Expression": NotRequired[str],
        "Label": NotRequired[str],
        "ReturnData": NotRequired[bool],
        "Period": NotRequired[int],
        "AccountId": NotRequired[str],
    },
)
ListServiceDependenciesOutputTypeDef = TypedDict(
    "ListServiceDependenciesOutputTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "ServiceDependencies": List[ServiceDependencyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListServiceDependentsOutputTypeDef = TypedDict(
    "ListServiceDependentsOutputTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "ServiceDependents": List[ServiceDependentTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListServiceOperationsOutputTypeDef = TypedDict(
    "ListServiceOperationsOutputTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "ServiceOperations": List[ServiceOperationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListServicesOutputTypeDef = TypedDict(
    "ListServicesOutputTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "ServiceSummaries": List[ServiceSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetServiceOutputTypeDef = TypedDict(
    "GetServiceOutputTypeDef",
    {
        "Service": ServiceTypeDef,
        "StartTime": datetime,
        "EndTime": datetime,
        "LogGroupReferences": List[Dict[str, str]],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MetricStatTypeDef = TypedDict(
    "MetricStatTypeDef",
    {
        "Metric": MetricUnionTypeDef,
        "Period": int,
        "Stat": str,
        "Unit": NotRequired[StandardUnitType],
    },
)
IntervalUnionTypeDef = Union[IntervalTypeDef, IntervalOutputTypeDef]
MonitoredRequestCountMetricDataQueriesOutputTypeDef = TypedDict(
    "MonitoredRequestCountMetricDataQueriesOutputTypeDef",
    {
        "GoodCountMetric": NotRequired[List[MetricDataQueryOutputTypeDef]],
        "BadCountMetric": NotRequired[List[MetricDataQueryOutputTypeDef]],
    },
)
ServiceLevelIndicatorMetricTypeDef = TypedDict(
    "ServiceLevelIndicatorMetricTypeDef",
    {
        "MetricDataQueries": List[MetricDataQueryOutputTypeDef],
        "KeyAttributes": NotRequired[Dict[str, str]],
        "OperationName": NotRequired[str],
        "MetricType": NotRequired[ServiceLevelIndicatorMetricTypeType],
    },
)
MetricStatUnionTypeDef = Union[MetricStatTypeDef, MetricStatOutputTypeDef]
GoalTypeDef = TypedDict(
    "GoalTypeDef",
    {
        "Interval": NotRequired[IntervalUnionTypeDef],
        "AttainmentGoal": NotRequired[float],
        "WarningThreshold": NotRequired[float],
    },
)
RequestBasedServiceLevelIndicatorMetricTypeDef = TypedDict(
    "RequestBasedServiceLevelIndicatorMetricTypeDef",
    {
        "TotalRequestCountMetric": List[MetricDataQueryOutputTypeDef],
        "MonitoredRequestCountMetric": MonitoredRequestCountMetricDataQueriesOutputTypeDef,
        "KeyAttributes": NotRequired[Dict[str, str]],
        "OperationName": NotRequired[str],
        "MetricType": NotRequired[ServiceLevelIndicatorMetricTypeType],
    },
)
ServiceLevelIndicatorTypeDef = TypedDict(
    "ServiceLevelIndicatorTypeDef",
    {
        "SliMetric": ServiceLevelIndicatorMetricTypeDef,
        "MetricThreshold": float,
        "ComparisonOperator": ServiceLevelIndicatorComparisonOperatorType,
    },
)
MetricDataQueryTypeDef = TypedDict(
    "MetricDataQueryTypeDef",
    {
        "Id": str,
        "MetricStat": NotRequired[MetricStatUnionTypeDef],
        "Expression": NotRequired[str],
        "Label": NotRequired[str],
        "ReturnData": NotRequired[bool],
        "Period": NotRequired[int],
        "AccountId": NotRequired[str],
    },
)
RequestBasedServiceLevelIndicatorTypeDef = TypedDict(
    "RequestBasedServiceLevelIndicatorTypeDef",
    {
        "RequestBasedSliMetric": RequestBasedServiceLevelIndicatorMetricTypeDef,
        "MetricThreshold": NotRequired[float],
        "ComparisonOperator": NotRequired[ServiceLevelIndicatorComparisonOperatorType],
    },
)
MetricDataQueryUnionTypeDef = Union[MetricDataQueryTypeDef, MetricDataQueryOutputTypeDef]
MonitoredRequestCountMetricDataQueriesTypeDef = TypedDict(
    "MonitoredRequestCountMetricDataQueriesTypeDef",
    {
        "GoodCountMetric": NotRequired[Sequence[MetricDataQueryTypeDef]],
        "BadCountMetric": NotRequired[Sequence[MetricDataQueryTypeDef]],
    },
)
ServiceLevelObjectiveBudgetReportTypeDef = TypedDict(
    "ServiceLevelObjectiveBudgetReportTypeDef",
    {
        "Arn": str,
        "Name": str,
        "BudgetStatus": ServiceLevelObjectiveBudgetStatusType,
        "EvaluationType": NotRequired[EvaluationTypeType],
        "Attainment": NotRequired[float],
        "TotalBudgetSeconds": NotRequired[int],
        "BudgetSecondsRemaining": NotRequired[int],
        "TotalBudgetRequests": NotRequired[int],
        "BudgetRequestsRemaining": NotRequired[int],
        "Sli": NotRequired[ServiceLevelIndicatorTypeDef],
        "RequestBasedSli": NotRequired[RequestBasedServiceLevelIndicatorTypeDef],
        "Goal": NotRequired[GoalOutputTypeDef],
    },
)
ServiceLevelObjectiveTypeDef = TypedDict(
    "ServiceLevelObjectiveTypeDef",
    {
        "Arn": str,
        "Name": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "Goal": GoalOutputTypeDef,
        "Description": NotRequired[str],
        "Sli": NotRequired[ServiceLevelIndicatorTypeDef],
        "RequestBasedSli": NotRequired[RequestBasedServiceLevelIndicatorTypeDef],
        "EvaluationType": NotRequired[EvaluationTypeType],
    },
)
ServiceLevelIndicatorMetricConfigTypeDef = TypedDict(
    "ServiceLevelIndicatorMetricConfigTypeDef",
    {
        "KeyAttributes": NotRequired[Mapping[str, str]],
        "OperationName": NotRequired[str],
        "MetricType": NotRequired[ServiceLevelIndicatorMetricTypeType],
        "Statistic": NotRequired[str],
        "PeriodSeconds": NotRequired[int],
        "MetricDataQueries": NotRequired[Sequence[MetricDataQueryUnionTypeDef]],
    },
)
MonitoredRequestCountMetricDataQueriesUnionTypeDef = Union[
    MonitoredRequestCountMetricDataQueriesTypeDef,
    MonitoredRequestCountMetricDataQueriesOutputTypeDef,
]
BatchGetServiceLevelObjectiveBudgetReportOutputTypeDef = TypedDict(
    "BatchGetServiceLevelObjectiveBudgetReportOutputTypeDef",
    {
        "Timestamp": datetime,
        "Reports": List[ServiceLevelObjectiveBudgetReportTypeDef],
        "Errors": List[ServiceLevelObjectiveBudgetReportErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateServiceLevelObjectiveOutputTypeDef = TypedDict(
    "CreateServiceLevelObjectiveOutputTypeDef",
    {
        "Slo": ServiceLevelObjectiveTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServiceLevelObjectiveOutputTypeDef = TypedDict(
    "GetServiceLevelObjectiveOutputTypeDef",
    {
        "Slo": ServiceLevelObjectiveTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateServiceLevelObjectiveOutputTypeDef = TypedDict(
    "UpdateServiceLevelObjectiveOutputTypeDef",
    {
        "Slo": ServiceLevelObjectiveTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ServiceLevelIndicatorConfigTypeDef = TypedDict(
    "ServiceLevelIndicatorConfigTypeDef",
    {
        "SliMetricConfig": ServiceLevelIndicatorMetricConfigTypeDef,
        "MetricThreshold": float,
        "ComparisonOperator": ServiceLevelIndicatorComparisonOperatorType,
    },
)
RequestBasedServiceLevelIndicatorMetricConfigTypeDef = TypedDict(
    "RequestBasedServiceLevelIndicatorMetricConfigTypeDef",
    {
        "KeyAttributes": NotRequired[Mapping[str, str]],
        "OperationName": NotRequired[str],
        "MetricType": NotRequired[ServiceLevelIndicatorMetricTypeType],
        "TotalRequestCountMetric": NotRequired[Sequence[MetricDataQueryUnionTypeDef]],
        "MonitoredRequestCountMetric": NotRequired[
            MonitoredRequestCountMetricDataQueriesUnionTypeDef
        ],
    },
)
RequestBasedServiceLevelIndicatorConfigTypeDef = TypedDict(
    "RequestBasedServiceLevelIndicatorConfigTypeDef",
    {
        "RequestBasedSliMetricConfig": RequestBasedServiceLevelIndicatorMetricConfigTypeDef,
        "MetricThreshold": NotRequired[float],
        "ComparisonOperator": NotRequired[ServiceLevelIndicatorComparisonOperatorType],
    },
)
CreateServiceLevelObjectiveInputRequestTypeDef = TypedDict(
    "CreateServiceLevelObjectiveInputRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "SliConfig": NotRequired[ServiceLevelIndicatorConfigTypeDef],
        "RequestBasedSliConfig": NotRequired[RequestBasedServiceLevelIndicatorConfigTypeDef],
        "Goal": NotRequired[GoalTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
UpdateServiceLevelObjectiveInputRequestTypeDef = TypedDict(
    "UpdateServiceLevelObjectiveInputRequestTypeDef",
    {
        "Id": str,
        "Description": NotRequired[str],
        "SliConfig": NotRequired[ServiceLevelIndicatorConfigTypeDef],
        "RequestBasedSliConfig": NotRequired[RequestBasedServiceLevelIndicatorConfigTypeDef],
        "Goal": NotRequired[GoalTypeDef],
    },
)
