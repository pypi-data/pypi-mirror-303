"""
Type annotations for devops-guru service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/type_defs/)

Usage::

    ```python
    from mypy_boto3_devops_guru.type_defs import AccountInsightHealthTypeDef

    data: AccountInsightHealthTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    AnomalySeverityType,
    AnomalyStatusType,
    AnomalyTypeType,
    CloudWatchMetricDataStatusCodeType,
    CloudWatchMetricsStatType,
    CostEstimationServiceResourceStateType,
    CostEstimationStatusType,
    EventClassType,
    EventDataSourceType,
    EventSourceOptInStatusType,
    InsightFeedbackOptionType,
    InsightSeverityType,
    InsightStatusType,
    InsightTypeType,
    LocaleType,
    LogAnomalyTypeType,
    NotificationMessageTypeType,
    OptInStatusType,
    OrganizationResourceCollectionTypeType,
    ResourceCollectionTypeType,
    ResourcePermissionType,
    ResourceTypeFilterType,
    ServerSideEncryptionTypeType,
    ServiceNameType,
    UpdateResourceCollectionActionType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AccountInsightHealthTypeDef",
    "ResponseMetadataTypeDef",
    "AmazonCodeGuruProfilerIntegrationTypeDef",
    "AnomalyReportedTimeRangeTypeDef",
    "AnomalyResourceTypeDef",
    "AnomalySourceMetadataTypeDef",
    "AnomalyTimeRangeTypeDef",
    "CloudFormationCollectionFilterTypeDef",
    "CloudFormationCollectionOutputTypeDef",
    "CloudFormationCollectionTypeDef",
    "CloudFormationCostEstimationResourceCollectionFilterOutputTypeDef",
    "CloudFormationCostEstimationResourceCollectionFilterTypeDef",
    "InsightHealthTypeDef",
    "TimestampMetricValuePairTypeDef",
    "CloudWatchMetricsDimensionTypeDef",
    "TagCostEstimationResourceCollectionFilterOutputTypeDef",
    "CostEstimationTimeRangeTypeDef",
    "DeleteInsightRequestRequestTypeDef",
    "TimestampTypeDef",
    "DescribeAnomalyRequestRequestTypeDef",
    "DescribeFeedbackRequestRequestTypeDef",
    "InsightFeedbackTypeDef",
    "DescribeInsightRequestRequestTypeDef",
    "DescribeOrganizationHealthRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeOrganizationResourceCollectionHealthRequestRequestTypeDef",
    "DescribeResourceCollectionHealthRequestRequestTypeDef",
    "EventResourceTypeDef",
    "GetCostEstimationRequestRequestTypeDef",
    "ServiceResourceCostTypeDef",
    "GetResourceCollectionRequestRequestTypeDef",
    "InsightTimeRangeTypeDef",
    "KMSServerSideEncryptionIntegrationConfigTypeDef",
    "KMSServerSideEncryptionIntegrationTypeDef",
    "ServiceCollectionTypeDef",
    "ListAnomalousLogGroupsRequestRequestTypeDef",
    "ListInsightsOngoingStatusFilterTypeDef",
    "ListMonitoredResourcesFiltersTypeDef",
    "ListNotificationChannelsRequestRequestTypeDef",
    "ListRecommendationsRequestRequestTypeDef",
    "LogAnomalyClassTypeDef",
    "LogsAnomalyDetectionIntegrationConfigTypeDef",
    "LogsAnomalyDetectionIntegrationTypeDef",
    "NotificationFilterConfigOutputTypeDef",
    "SnsChannelConfigTypeDef",
    "NotificationFilterConfigTypeDef",
    "OpsCenterIntegrationConfigTypeDef",
    "OpsCenterIntegrationTypeDef",
    "PerformanceInsightsMetricDimensionGroupTypeDef",
    "PerformanceInsightsStatTypeDef",
    "PerformanceInsightsReferenceScalarTypeDef",
    "PredictionTimeRangeTypeDef",
    "ServiceCollectionOutputTypeDef",
    "RecommendationRelatedAnomalyResourceTypeDef",
    "RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef",
    "RecommendationRelatedEventResourceTypeDef",
    "RemoveNotificationChannelRequestRequestTypeDef",
    "TagCollectionFilterTypeDef",
    "TagCollectionOutputTypeDef",
    "TagCollectionTypeDef",
    "ServiceInsightHealthTypeDef",
    "TagCostEstimationResourceCollectionFilterTypeDef",
    "UpdateCloudFormationCollectionFilterTypeDef",
    "UpdateTagCollectionFilterTypeDef",
    "AccountHealthTypeDef",
    "AddNotificationChannelResponseTypeDef",
    "DescribeAccountHealthResponseTypeDef",
    "DescribeAccountOverviewResponseTypeDef",
    "DescribeOrganizationHealthResponseTypeDef",
    "DescribeOrganizationOverviewResponseTypeDef",
    "EventSourcesConfigTypeDef",
    "CloudFormationCostEstimationResourceCollectionFilterUnionTypeDef",
    "CloudFormationHealthTypeDef",
    "TagHealthTypeDef",
    "CloudWatchMetricsDataSummaryTypeDef",
    "CostEstimationResourceCollectionFilterOutputTypeDef",
    "DescribeAccountOverviewRequestRequestTypeDef",
    "DescribeOrganizationOverviewRequestRequestTypeDef",
    "EndTimeRangeTypeDef",
    "EventTimeRangeTypeDef",
    "StartTimeRangeTypeDef",
    "DescribeFeedbackResponseTypeDef",
    "PutFeedbackRequestRequestTypeDef",
    "DescribeOrganizationResourceCollectionHealthRequestDescribeOrganizationResourceCollectionHealthPaginateTypeDef",
    "DescribeResourceCollectionHealthRequestDescribeResourceCollectionHealthPaginateTypeDef",
    "GetCostEstimationRequestGetCostEstimationPaginateTypeDef",
    "GetResourceCollectionRequestGetResourceCollectionPaginateTypeDef",
    "ListAnomalousLogGroupsRequestListAnomalousLogGroupsPaginateTypeDef",
    "ListNotificationChannelsRequestListNotificationChannelsPaginateTypeDef",
    "ListRecommendationsRequestListRecommendationsPaginateTypeDef",
    "ListAnomaliesForInsightFiltersTypeDef",
    "ListMonitoredResourcesRequestListMonitoredResourcesPaginateTypeDef",
    "ListMonitoredResourcesRequestRequestTypeDef",
    "LogAnomalyShowcaseTypeDef",
    "NotificationChannelConfigOutputTypeDef",
    "NotificationFilterConfigUnionTypeDef",
    "UpdateServiceIntegrationConfigTypeDef",
    "ServiceIntegrationConfigTypeDef",
    "PerformanceInsightsMetricQueryTypeDef",
    "ServiceCollectionUnionTypeDef",
    "RecommendationRelatedAnomalySourceDetailTypeDef",
    "RecommendationRelatedEventTypeDef",
    "ResourceCollectionFilterTypeDef",
    "ResourceCollectionOutputTypeDef",
    "ResourceCollectionTypeDef",
    "ServiceHealthTypeDef",
    "TagCostEstimationResourceCollectionFilterUnionTypeDef",
    "UpdateResourceCollectionFilterTypeDef",
    "DescribeEventSourcesConfigResponseTypeDef",
    "UpdateEventSourcesConfigRequestRequestTypeDef",
    "CloudWatchMetricsDetailTypeDef",
    "GetCostEstimationResponseTypeDef",
    "ListInsightsClosedStatusFilterTypeDef",
    "ListInsightsAnyStatusFilterTypeDef",
    "ListAnomaliesForInsightRequestListAnomaliesForInsightPaginateTypeDef",
    "ListAnomaliesForInsightRequestRequestTypeDef",
    "AnomalousLogGroupTypeDef",
    "NotificationChannelTypeDef",
    "NotificationChannelConfigTypeDef",
    "UpdateServiceIntegrationRequestRequestTypeDef",
    "DescribeServiceIntegrationResponseTypeDef",
    "PerformanceInsightsReferenceMetricTypeDef",
    "RecommendationRelatedAnomalyTypeDef",
    "GetResourceCollectionResponseTypeDef",
    "EventTypeDef",
    "MonitoredResourceIdentifierTypeDef",
    "ProactiveInsightSummaryTypeDef",
    "ProactiveInsightTypeDef",
    "ProactiveOrganizationInsightSummaryTypeDef",
    "ReactiveInsightSummaryTypeDef",
    "ReactiveInsightTypeDef",
    "ReactiveOrganizationInsightSummaryTypeDef",
    "ListEventsFiltersTypeDef",
    "ResourceCollectionUnionTypeDef",
    "DescribeOrganizationResourceCollectionHealthResponseTypeDef",
    "DescribeResourceCollectionHealthResponseTypeDef",
    "CostEstimationResourceCollectionFilterTypeDef",
    "UpdateResourceCollectionRequestRequestTypeDef",
    "ListInsightsStatusFilterTypeDef",
    "ListAnomalousLogGroupsResponseTypeDef",
    "ListNotificationChannelsResponseTypeDef",
    "AddNotificationChannelRequestRequestTypeDef",
    "PerformanceInsightsReferenceComparisonValuesTypeDef",
    "RecommendationTypeDef",
    "ListEventsResponseTypeDef",
    "ListMonitoredResourcesResponseTypeDef",
    "ListInsightsResponseTypeDef",
    "SearchInsightsResponseTypeDef",
    "SearchOrganizationInsightsResponseTypeDef",
    "DescribeInsightResponseTypeDef",
    "ListOrganizationInsightsResponseTypeDef",
    "ListEventsRequestListEventsPaginateTypeDef",
    "ListEventsRequestRequestTypeDef",
    "SearchInsightsFiltersTypeDef",
    "SearchOrganizationInsightsFiltersTypeDef",
    "StartCostEstimationRequestRequestTypeDef",
    "ListInsightsRequestListInsightsPaginateTypeDef",
    "ListInsightsRequestRequestTypeDef",
    "ListOrganizationInsightsRequestListOrganizationInsightsPaginateTypeDef",
    "ListOrganizationInsightsRequestRequestTypeDef",
    "PerformanceInsightsReferenceDataTypeDef",
    "ListRecommendationsResponseTypeDef",
    "SearchInsightsRequestRequestTypeDef",
    "SearchInsightsRequestSearchInsightsPaginateTypeDef",
    "SearchOrganizationInsightsRequestRequestTypeDef",
    "SearchOrganizationInsightsRequestSearchOrganizationInsightsPaginateTypeDef",
    "PerformanceInsightsMetricsDetailTypeDef",
    "AnomalySourceDetailsTypeDef",
    "ProactiveAnomalySummaryTypeDef",
    "ProactiveAnomalyTypeDef",
    "ReactiveAnomalySummaryTypeDef",
    "ReactiveAnomalyTypeDef",
    "ListAnomaliesForInsightResponseTypeDef",
    "DescribeAnomalyResponseTypeDef",
)

AccountInsightHealthTypeDef = TypedDict(
    "AccountInsightHealthTypeDef",
    {
        "OpenProactiveInsights": NotRequired[int],
        "OpenReactiveInsights": NotRequired[int],
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
AmazonCodeGuruProfilerIntegrationTypeDef = TypedDict(
    "AmazonCodeGuruProfilerIntegrationTypeDef",
    {
        "Status": NotRequired[EventSourceOptInStatusType],
    },
)
AnomalyReportedTimeRangeTypeDef = TypedDict(
    "AnomalyReportedTimeRangeTypeDef",
    {
        "OpenTime": datetime,
        "CloseTime": NotRequired[datetime],
    },
)
AnomalyResourceTypeDef = TypedDict(
    "AnomalyResourceTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AnomalySourceMetadataTypeDef = TypedDict(
    "AnomalySourceMetadataTypeDef",
    {
        "Source": NotRequired[str],
        "SourceResourceName": NotRequired[str],
        "SourceResourceType": NotRequired[str],
    },
)
AnomalyTimeRangeTypeDef = TypedDict(
    "AnomalyTimeRangeTypeDef",
    {
        "StartTime": datetime,
        "EndTime": NotRequired[datetime],
    },
)
CloudFormationCollectionFilterTypeDef = TypedDict(
    "CloudFormationCollectionFilterTypeDef",
    {
        "StackNames": NotRequired[List[str]],
    },
)
CloudFormationCollectionOutputTypeDef = TypedDict(
    "CloudFormationCollectionOutputTypeDef",
    {
        "StackNames": NotRequired[List[str]],
    },
)
CloudFormationCollectionTypeDef = TypedDict(
    "CloudFormationCollectionTypeDef",
    {
        "StackNames": NotRequired[Sequence[str]],
    },
)
CloudFormationCostEstimationResourceCollectionFilterOutputTypeDef = TypedDict(
    "CloudFormationCostEstimationResourceCollectionFilterOutputTypeDef",
    {
        "StackNames": NotRequired[List[str]],
    },
)
CloudFormationCostEstimationResourceCollectionFilterTypeDef = TypedDict(
    "CloudFormationCostEstimationResourceCollectionFilterTypeDef",
    {
        "StackNames": NotRequired[Sequence[str]],
    },
)
InsightHealthTypeDef = TypedDict(
    "InsightHealthTypeDef",
    {
        "OpenProactiveInsights": NotRequired[int],
        "OpenReactiveInsights": NotRequired[int],
        "MeanTimeToRecoverInMilliseconds": NotRequired[int],
    },
)
TimestampMetricValuePairTypeDef = TypedDict(
    "TimestampMetricValuePairTypeDef",
    {
        "Timestamp": NotRequired[datetime],
        "MetricValue": NotRequired[float],
    },
)
CloudWatchMetricsDimensionTypeDef = TypedDict(
    "CloudWatchMetricsDimensionTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)
TagCostEstimationResourceCollectionFilterOutputTypeDef = TypedDict(
    "TagCostEstimationResourceCollectionFilterOutputTypeDef",
    {
        "AppBoundaryKey": str,
        "TagValues": List[str],
    },
)
CostEstimationTimeRangeTypeDef = TypedDict(
    "CostEstimationTimeRangeTypeDef",
    {
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
    },
)
DeleteInsightRequestRequestTypeDef = TypedDict(
    "DeleteInsightRequestRequestTypeDef",
    {
        "Id": str,
    },
)
TimestampTypeDef = Union[datetime, str]
DescribeAnomalyRequestRequestTypeDef = TypedDict(
    "DescribeAnomalyRequestRequestTypeDef",
    {
        "Id": str,
        "AccountId": NotRequired[str],
    },
)
DescribeFeedbackRequestRequestTypeDef = TypedDict(
    "DescribeFeedbackRequestRequestTypeDef",
    {
        "InsightId": NotRequired[str],
    },
)
InsightFeedbackTypeDef = TypedDict(
    "InsightFeedbackTypeDef",
    {
        "Id": NotRequired[str],
        "Feedback": NotRequired[InsightFeedbackOptionType],
    },
)
DescribeInsightRequestRequestTypeDef = TypedDict(
    "DescribeInsightRequestRequestTypeDef",
    {
        "Id": str,
        "AccountId": NotRequired[str],
    },
)
DescribeOrganizationHealthRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationHealthRequestRequestTypeDef",
    {
        "AccountIds": NotRequired[Sequence[str]],
        "OrganizationalUnitIds": NotRequired[Sequence[str]],
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
DescribeOrganizationResourceCollectionHealthRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationResourceCollectionHealthRequestRequestTypeDef",
    {
        "OrganizationResourceCollectionType": OrganizationResourceCollectionTypeType,
        "AccountIds": NotRequired[Sequence[str]],
        "OrganizationalUnitIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeResourceCollectionHealthRequestRequestTypeDef = TypedDict(
    "DescribeResourceCollectionHealthRequestRequestTypeDef",
    {
        "ResourceCollectionType": ResourceCollectionTypeType,
        "NextToken": NotRequired[str],
    },
)
EventResourceTypeDef = TypedDict(
    "EventResourceTypeDef",
    {
        "Type": NotRequired[str],
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
    },
)
GetCostEstimationRequestRequestTypeDef = TypedDict(
    "GetCostEstimationRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)
ServiceResourceCostTypeDef = TypedDict(
    "ServiceResourceCostTypeDef",
    {
        "Type": NotRequired[str],
        "State": NotRequired[CostEstimationServiceResourceStateType],
        "Count": NotRequired[int],
        "UnitCost": NotRequired[float],
        "Cost": NotRequired[float],
    },
)
GetResourceCollectionRequestRequestTypeDef = TypedDict(
    "GetResourceCollectionRequestRequestTypeDef",
    {
        "ResourceCollectionType": ResourceCollectionTypeType,
        "NextToken": NotRequired[str],
    },
)
InsightTimeRangeTypeDef = TypedDict(
    "InsightTimeRangeTypeDef",
    {
        "StartTime": datetime,
        "EndTime": NotRequired[datetime],
    },
)
KMSServerSideEncryptionIntegrationConfigTypeDef = TypedDict(
    "KMSServerSideEncryptionIntegrationConfigTypeDef",
    {
        "KMSKeyId": NotRequired[str],
        "OptInStatus": NotRequired[OptInStatusType],
        "Type": NotRequired[ServerSideEncryptionTypeType],
    },
)
KMSServerSideEncryptionIntegrationTypeDef = TypedDict(
    "KMSServerSideEncryptionIntegrationTypeDef",
    {
        "KMSKeyId": NotRequired[str],
        "OptInStatus": NotRequired[OptInStatusType],
        "Type": NotRequired[ServerSideEncryptionTypeType],
    },
)
ServiceCollectionTypeDef = TypedDict(
    "ServiceCollectionTypeDef",
    {
        "ServiceNames": NotRequired[Sequence[ServiceNameType]],
    },
)
ListAnomalousLogGroupsRequestRequestTypeDef = TypedDict(
    "ListAnomalousLogGroupsRequestRequestTypeDef",
    {
        "InsightId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListInsightsOngoingStatusFilterTypeDef = TypedDict(
    "ListInsightsOngoingStatusFilterTypeDef",
    {
        "Type": InsightTypeType,
    },
)
ListMonitoredResourcesFiltersTypeDef = TypedDict(
    "ListMonitoredResourcesFiltersTypeDef",
    {
        "ResourcePermission": ResourcePermissionType,
        "ResourceTypeFilters": Sequence[ResourceTypeFilterType],
    },
)
ListNotificationChannelsRequestRequestTypeDef = TypedDict(
    "ListNotificationChannelsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)
ListRecommendationsRequestRequestTypeDef = TypedDict(
    "ListRecommendationsRequestRequestTypeDef",
    {
        "InsightId": str,
        "NextToken": NotRequired[str],
        "Locale": NotRequired[LocaleType],
        "AccountId": NotRequired[str],
    },
)
LogAnomalyClassTypeDef = TypedDict(
    "LogAnomalyClassTypeDef",
    {
        "LogStreamName": NotRequired[str],
        "LogAnomalyType": NotRequired[LogAnomalyTypeType],
        "LogAnomalyToken": NotRequired[str],
        "LogEventId": NotRequired[str],
        "Explanation": NotRequired[str],
        "NumberOfLogLinesOccurrences": NotRequired[int],
        "LogEventTimestamp": NotRequired[datetime],
    },
)
LogsAnomalyDetectionIntegrationConfigTypeDef = TypedDict(
    "LogsAnomalyDetectionIntegrationConfigTypeDef",
    {
        "OptInStatus": NotRequired[OptInStatusType],
    },
)
LogsAnomalyDetectionIntegrationTypeDef = TypedDict(
    "LogsAnomalyDetectionIntegrationTypeDef",
    {
        "OptInStatus": NotRequired[OptInStatusType],
    },
)
NotificationFilterConfigOutputTypeDef = TypedDict(
    "NotificationFilterConfigOutputTypeDef",
    {
        "Severities": NotRequired[List[InsightSeverityType]],
        "MessageTypes": NotRequired[List[NotificationMessageTypeType]],
    },
)
SnsChannelConfigTypeDef = TypedDict(
    "SnsChannelConfigTypeDef",
    {
        "TopicArn": NotRequired[str],
    },
)
NotificationFilterConfigTypeDef = TypedDict(
    "NotificationFilterConfigTypeDef",
    {
        "Severities": NotRequired[Sequence[InsightSeverityType]],
        "MessageTypes": NotRequired[Sequence[NotificationMessageTypeType]],
    },
)
OpsCenterIntegrationConfigTypeDef = TypedDict(
    "OpsCenterIntegrationConfigTypeDef",
    {
        "OptInStatus": NotRequired[OptInStatusType],
    },
)
OpsCenterIntegrationTypeDef = TypedDict(
    "OpsCenterIntegrationTypeDef",
    {
        "OptInStatus": NotRequired[OptInStatusType],
    },
)
PerformanceInsightsMetricDimensionGroupTypeDef = TypedDict(
    "PerformanceInsightsMetricDimensionGroupTypeDef",
    {
        "Group": NotRequired[str],
        "Dimensions": NotRequired[List[str]],
        "Limit": NotRequired[int],
    },
)
PerformanceInsightsStatTypeDef = TypedDict(
    "PerformanceInsightsStatTypeDef",
    {
        "Type": NotRequired[str],
        "Value": NotRequired[float],
    },
)
PerformanceInsightsReferenceScalarTypeDef = TypedDict(
    "PerformanceInsightsReferenceScalarTypeDef",
    {
        "Value": NotRequired[float],
    },
)
PredictionTimeRangeTypeDef = TypedDict(
    "PredictionTimeRangeTypeDef",
    {
        "StartTime": datetime,
        "EndTime": NotRequired[datetime],
    },
)
ServiceCollectionOutputTypeDef = TypedDict(
    "ServiceCollectionOutputTypeDef",
    {
        "ServiceNames": NotRequired[List[ServiceNameType]],
    },
)
RecommendationRelatedAnomalyResourceTypeDef = TypedDict(
    "RecommendationRelatedAnomalyResourceTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
    },
)
RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef = TypedDict(
    "RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef",
    {
        "MetricName": NotRequired[str],
        "Namespace": NotRequired[str],
    },
)
RecommendationRelatedEventResourceTypeDef = TypedDict(
    "RecommendationRelatedEventResourceTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
    },
)
RemoveNotificationChannelRequestRequestTypeDef = TypedDict(
    "RemoveNotificationChannelRequestRequestTypeDef",
    {
        "Id": str,
    },
)
TagCollectionFilterTypeDef = TypedDict(
    "TagCollectionFilterTypeDef",
    {
        "AppBoundaryKey": str,
        "TagValues": List[str],
    },
)
TagCollectionOutputTypeDef = TypedDict(
    "TagCollectionOutputTypeDef",
    {
        "AppBoundaryKey": str,
        "TagValues": List[str],
    },
)
TagCollectionTypeDef = TypedDict(
    "TagCollectionTypeDef",
    {
        "AppBoundaryKey": str,
        "TagValues": Sequence[str],
    },
)
ServiceInsightHealthTypeDef = TypedDict(
    "ServiceInsightHealthTypeDef",
    {
        "OpenProactiveInsights": NotRequired[int],
        "OpenReactiveInsights": NotRequired[int],
    },
)
TagCostEstimationResourceCollectionFilterTypeDef = TypedDict(
    "TagCostEstimationResourceCollectionFilterTypeDef",
    {
        "AppBoundaryKey": str,
        "TagValues": Sequence[str],
    },
)
UpdateCloudFormationCollectionFilterTypeDef = TypedDict(
    "UpdateCloudFormationCollectionFilterTypeDef",
    {
        "StackNames": NotRequired[Sequence[str]],
    },
)
UpdateTagCollectionFilterTypeDef = TypedDict(
    "UpdateTagCollectionFilterTypeDef",
    {
        "AppBoundaryKey": str,
        "TagValues": Sequence[str],
    },
)
AccountHealthTypeDef = TypedDict(
    "AccountHealthTypeDef",
    {
        "AccountId": NotRequired[str],
        "Insight": NotRequired[AccountInsightHealthTypeDef],
    },
)
AddNotificationChannelResponseTypeDef = TypedDict(
    "AddNotificationChannelResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAccountHealthResponseTypeDef = TypedDict(
    "DescribeAccountHealthResponseTypeDef",
    {
        "OpenReactiveInsights": int,
        "OpenProactiveInsights": int,
        "MetricsAnalyzed": int,
        "ResourceHours": int,
        "AnalyzedResourceCount": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAccountOverviewResponseTypeDef = TypedDict(
    "DescribeAccountOverviewResponseTypeDef",
    {
        "ReactiveInsights": int,
        "ProactiveInsights": int,
        "MeanTimeToRecoverInMilliseconds": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeOrganizationHealthResponseTypeDef = TypedDict(
    "DescribeOrganizationHealthResponseTypeDef",
    {
        "OpenReactiveInsights": int,
        "OpenProactiveInsights": int,
        "MetricsAnalyzed": int,
        "ResourceHours": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeOrganizationOverviewResponseTypeDef = TypedDict(
    "DescribeOrganizationOverviewResponseTypeDef",
    {
        "ReactiveInsights": int,
        "ProactiveInsights": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EventSourcesConfigTypeDef = TypedDict(
    "EventSourcesConfigTypeDef",
    {
        "AmazonCodeGuruProfiler": NotRequired[AmazonCodeGuruProfilerIntegrationTypeDef],
    },
)
CloudFormationCostEstimationResourceCollectionFilterUnionTypeDef = Union[
    CloudFormationCostEstimationResourceCollectionFilterTypeDef,
    CloudFormationCostEstimationResourceCollectionFilterOutputTypeDef,
]
CloudFormationHealthTypeDef = TypedDict(
    "CloudFormationHealthTypeDef",
    {
        "StackName": NotRequired[str],
        "Insight": NotRequired[InsightHealthTypeDef],
        "AnalyzedResourceCount": NotRequired[int],
    },
)
TagHealthTypeDef = TypedDict(
    "TagHealthTypeDef",
    {
        "AppBoundaryKey": NotRequired[str],
        "TagValue": NotRequired[str],
        "Insight": NotRequired[InsightHealthTypeDef],
        "AnalyzedResourceCount": NotRequired[int],
    },
)
CloudWatchMetricsDataSummaryTypeDef = TypedDict(
    "CloudWatchMetricsDataSummaryTypeDef",
    {
        "TimestampMetricValuePairList": NotRequired[List[TimestampMetricValuePairTypeDef]],
        "StatusCode": NotRequired[CloudWatchMetricDataStatusCodeType],
    },
)
CostEstimationResourceCollectionFilterOutputTypeDef = TypedDict(
    "CostEstimationResourceCollectionFilterOutputTypeDef",
    {
        "CloudFormation": NotRequired[
            CloudFormationCostEstimationResourceCollectionFilterOutputTypeDef
        ],
        "Tags": NotRequired[List[TagCostEstimationResourceCollectionFilterOutputTypeDef]],
    },
)
DescribeAccountOverviewRequestRequestTypeDef = TypedDict(
    "DescribeAccountOverviewRequestRequestTypeDef",
    {
        "FromTime": TimestampTypeDef,
        "ToTime": NotRequired[TimestampTypeDef],
    },
)
DescribeOrganizationOverviewRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationOverviewRequestRequestTypeDef",
    {
        "FromTime": TimestampTypeDef,
        "ToTime": NotRequired[TimestampTypeDef],
        "AccountIds": NotRequired[Sequence[str]],
        "OrganizationalUnitIds": NotRequired[Sequence[str]],
    },
)
EndTimeRangeTypeDef = TypedDict(
    "EndTimeRangeTypeDef",
    {
        "FromTime": NotRequired[TimestampTypeDef],
        "ToTime": NotRequired[TimestampTypeDef],
    },
)
EventTimeRangeTypeDef = TypedDict(
    "EventTimeRangeTypeDef",
    {
        "FromTime": TimestampTypeDef,
        "ToTime": TimestampTypeDef,
    },
)
StartTimeRangeTypeDef = TypedDict(
    "StartTimeRangeTypeDef",
    {
        "FromTime": NotRequired[TimestampTypeDef],
        "ToTime": NotRequired[TimestampTypeDef],
    },
)
DescribeFeedbackResponseTypeDef = TypedDict(
    "DescribeFeedbackResponseTypeDef",
    {
        "InsightFeedback": InsightFeedbackTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutFeedbackRequestRequestTypeDef = TypedDict(
    "PutFeedbackRequestRequestTypeDef",
    {
        "InsightFeedback": NotRequired[InsightFeedbackTypeDef],
    },
)
DescribeOrganizationResourceCollectionHealthRequestDescribeOrganizationResourceCollectionHealthPaginateTypeDef = TypedDict(
    "DescribeOrganizationResourceCollectionHealthRequestDescribeOrganizationResourceCollectionHealthPaginateTypeDef",
    {
        "OrganizationResourceCollectionType": OrganizationResourceCollectionTypeType,
        "AccountIds": NotRequired[Sequence[str]],
        "OrganizationalUnitIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeResourceCollectionHealthRequestDescribeResourceCollectionHealthPaginateTypeDef = TypedDict(
    "DescribeResourceCollectionHealthRequestDescribeResourceCollectionHealthPaginateTypeDef",
    {
        "ResourceCollectionType": ResourceCollectionTypeType,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetCostEstimationRequestGetCostEstimationPaginateTypeDef = TypedDict(
    "GetCostEstimationRequestGetCostEstimationPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetResourceCollectionRequestGetResourceCollectionPaginateTypeDef = TypedDict(
    "GetResourceCollectionRequestGetResourceCollectionPaginateTypeDef",
    {
        "ResourceCollectionType": ResourceCollectionTypeType,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAnomalousLogGroupsRequestListAnomalousLogGroupsPaginateTypeDef = TypedDict(
    "ListAnomalousLogGroupsRequestListAnomalousLogGroupsPaginateTypeDef",
    {
        "InsightId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListNotificationChannelsRequestListNotificationChannelsPaginateTypeDef = TypedDict(
    "ListNotificationChannelsRequestListNotificationChannelsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRecommendationsRequestListRecommendationsPaginateTypeDef = TypedDict(
    "ListRecommendationsRequestListRecommendationsPaginateTypeDef",
    {
        "InsightId": str,
        "Locale": NotRequired[LocaleType],
        "AccountId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAnomaliesForInsightFiltersTypeDef = TypedDict(
    "ListAnomaliesForInsightFiltersTypeDef",
    {
        "ServiceCollection": NotRequired[ServiceCollectionTypeDef],
    },
)
ListMonitoredResourcesRequestListMonitoredResourcesPaginateTypeDef = TypedDict(
    "ListMonitoredResourcesRequestListMonitoredResourcesPaginateTypeDef",
    {
        "Filters": NotRequired[ListMonitoredResourcesFiltersTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMonitoredResourcesRequestRequestTypeDef = TypedDict(
    "ListMonitoredResourcesRequestRequestTypeDef",
    {
        "Filters": NotRequired[ListMonitoredResourcesFiltersTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
LogAnomalyShowcaseTypeDef = TypedDict(
    "LogAnomalyShowcaseTypeDef",
    {
        "LogAnomalyClasses": NotRequired[List[LogAnomalyClassTypeDef]],
    },
)
NotificationChannelConfigOutputTypeDef = TypedDict(
    "NotificationChannelConfigOutputTypeDef",
    {
        "Sns": SnsChannelConfigTypeDef,
        "Filters": NotRequired[NotificationFilterConfigOutputTypeDef],
    },
)
NotificationFilterConfigUnionTypeDef = Union[
    NotificationFilterConfigTypeDef, NotificationFilterConfigOutputTypeDef
]
UpdateServiceIntegrationConfigTypeDef = TypedDict(
    "UpdateServiceIntegrationConfigTypeDef",
    {
        "OpsCenter": NotRequired[OpsCenterIntegrationConfigTypeDef],
        "LogsAnomalyDetection": NotRequired[LogsAnomalyDetectionIntegrationConfigTypeDef],
        "KMSServerSideEncryption": NotRequired[KMSServerSideEncryptionIntegrationConfigTypeDef],
    },
)
ServiceIntegrationConfigTypeDef = TypedDict(
    "ServiceIntegrationConfigTypeDef",
    {
        "OpsCenter": NotRequired[OpsCenterIntegrationTypeDef],
        "LogsAnomalyDetection": NotRequired[LogsAnomalyDetectionIntegrationTypeDef],
        "KMSServerSideEncryption": NotRequired[KMSServerSideEncryptionIntegrationTypeDef],
    },
)
PerformanceInsightsMetricQueryTypeDef = TypedDict(
    "PerformanceInsightsMetricQueryTypeDef",
    {
        "Metric": NotRequired[str],
        "GroupBy": NotRequired[PerformanceInsightsMetricDimensionGroupTypeDef],
        "Filter": NotRequired[Dict[str, str]],
    },
)
ServiceCollectionUnionTypeDef = Union[ServiceCollectionTypeDef, ServiceCollectionOutputTypeDef]
RecommendationRelatedAnomalySourceDetailTypeDef = TypedDict(
    "RecommendationRelatedAnomalySourceDetailTypeDef",
    {
        "CloudWatchMetrics": NotRequired[
            List[RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef]
        ],
    },
)
RecommendationRelatedEventTypeDef = TypedDict(
    "RecommendationRelatedEventTypeDef",
    {
        "Name": NotRequired[str],
        "Resources": NotRequired[List[RecommendationRelatedEventResourceTypeDef]],
    },
)
ResourceCollectionFilterTypeDef = TypedDict(
    "ResourceCollectionFilterTypeDef",
    {
        "CloudFormation": NotRequired[CloudFormationCollectionFilterTypeDef],
        "Tags": NotRequired[List[TagCollectionFilterTypeDef]],
    },
)
ResourceCollectionOutputTypeDef = TypedDict(
    "ResourceCollectionOutputTypeDef",
    {
        "CloudFormation": NotRequired[CloudFormationCollectionOutputTypeDef],
        "Tags": NotRequired[List[TagCollectionOutputTypeDef]],
    },
)
ResourceCollectionTypeDef = TypedDict(
    "ResourceCollectionTypeDef",
    {
        "CloudFormation": NotRequired[CloudFormationCollectionTypeDef],
        "Tags": NotRequired[Sequence[TagCollectionTypeDef]],
    },
)
ServiceHealthTypeDef = TypedDict(
    "ServiceHealthTypeDef",
    {
        "ServiceName": NotRequired[ServiceNameType],
        "Insight": NotRequired[ServiceInsightHealthTypeDef],
        "AnalyzedResourceCount": NotRequired[int],
    },
)
TagCostEstimationResourceCollectionFilterUnionTypeDef = Union[
    TagCostEstimationResourceCollectionFilterTypeDef,
    TagCostEstimationResourceCollectionFilterOutputTypeDef,
]
UpdateResourceCollectionFilterTypeDef = TypedDict(
    "UpdateResourceCollectionFilterTypeDef",
    {
        "CloudFormation": NotRequired[UpdateCloudFormationCollectionFilterTypeDef],
        "Tags": NotRequired[Sequence[UpdateTagCollectionFilterTypeDef]],
    },
)
DescribeEventSourcesConfigResponseTypeDef = TypedDict(
    "DescribeEventSourcesConfigResponseTypeDef",
    {
        "EventSources": EventSourcesConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEventSourcesConfigRequestRequestTypeDef = TypedDict(
    "UpdateEventSourcesConfigRequestRequestTypeDef",
    {
        "EventSources": NotRequired[EventSourcesConfigTypeDef],
    },
)
CloudWatchMetricsDetailTypeDef = TypedDict(
    "CloudWatchMetricsDetailTypeDef",
    {
        "MetricName": NotRequired[str],
        "Namespace": NotRequired[str],
        "Dimensions": NotRequired[List[CloudWatchMetricsDimensionTypeDef]],
        "Stat": NotRequired[CloudWatchMetricsStatType],
        "Unit": NotRequired[str],
        "Period": NotRequired[int],
        "MetricDataSummary": NotRequired[CloudWatchMetricsDataSummaryTypeDef],
    },
)
GetCostEstimationResponseTypeDef = TypedDict(
    "GetCostEstimationResponseTypeDef",
    {
        "ResourceCollection": CostEstimationResourceCollectionFilterOutputTypeDef,
        "Status": CostEstimationStatusType,
        "Costs": List[ServiceResourceCostTypeDef],
        "TimeRange": CostEstimationTimeRangeTypeDef,
        "TotalCost": float,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListInsightsClosedStatusFilterTypeDef = TypedDict(
    "ListInsightsClosedStatusFilterTypeDef",
    {
        "Type": InsightTypeType,
        "EndTimeRange": EndTimeRangeTypeDef,
    },
)
ListInsightsAnyStatusFilterTypeDef = TypedDict(
    "ListInsightsAnyStatusFilterTypeDef",
    {
        "Type": InsightTypeType,
        "StartTimeRange": StartTimeRangeTypeDef,
    },
)
ListAnomaliesForInsightRequestListAnomaliesForInsightPaginateTypeDef = TypedDict(
    "ListAnomaliesForInsightRequestListAnomaliesForInsightPaginateTypeDef",
    {
        "InsightId": str,
        "StartTimeRange": NotRequired[StartTimeRangeTypeDef],
        "AccountId": NotRequired[str],
        "Filters": NotRequired[ListAnomaliesForInsightFiltersTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAnomaliesForInsightRequestRequestTypeDef = TypedDict(
    "ListAnomaliesForInsightRequestRequestTypeDef",
    {
        "InsightId": str,
        "StartTimeRange": NotRequired[StartTimeRangeTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "AccountId": NotRequired[str],
        "Filters": NotRequired[ListAnomaliesForInsightFiltersTypeDef],
    },
)
AnomalousLogGroupTypeDef = TypedDict(
    "AnomalousLogGroupTypeDef",
    {
        "LogGroupName": NotRequired[str],
        "ImpactStartTime": NotRequired[datetime],
        "ImpactEndTime": NotRequired[datetime],
        "NumberOfLogLinesScanned": NotRequired[int],
        "LogAnomalyShowcases": NotRequired[List[LogAnomalyShowcaseTypeDef]],
    },
)
NotificationChannelTypeDef = TypedDict(
    "NotificationChannelTypeDef",
    {
        "Id": NotRequired[str],
        "Config": NotRequired[NotificationChannelConfigOutputTypeDef],
    },
)
NotificationChannelConfigTypeDef = TypedDict(
    "NotificationChannelConfigTypeDef",
    {
        "Sns": SnsChannelConfigTypeDef,
        "Filters": NotRequired[NotificationFilterConfigUnionTypeDef],
    },
)
UpdateServiceIntegrationRequestRequestTypeDef = TypedDict(
    "UpdateServiceIntegrationRequestRequestTypeDef",
    {
        "ServiceIntegration": UpdateServiceIntegrationConfigTypeDef,
    },
)
DescribeServiceIntegrationResponseTypeDef = TypedDict(
    "DescribeServiceIntegrationResponseTypeDef",
    {
        "ServiceIntegration": ServiceIntegrationConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PerformanceInsightsReferenceMetricTypeDef = TypedDict(
    "PerformanceInsightsReferenceMetricTypeDef",
    {
        "MetricQuery": NotRequired[PerformanceInsightsMetricQueryTypeDef],
    },
)
RecommendationRelatedAnomalyTypeDef = TypedDict(
    "RecommendationRelatedAnomalyTypeDef",
    {
        "Resources": NotRequired[List[RecommendationRelatedAnomalyResourceTypeDef]],
        "SourceDetails": NotRequired[List[RecommendationRelatedAnomalySourceDetailTypeDef]],
        "AnomalyId": NotRequired[str],
    },
)
GetResourceCollectionResponseTypeDef = TypedDict(
    "GetResourceCollectionResponseTypeDef",
    {
        "ResourceCollection": ResourceCollectionFilterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "ResourceCollection": NotRequired[ResourceCollectionOutputTypeDef],
        "Id": NotRequired[str],
        "Time": NotRequired[datetime],
        "EventSource": NotRequired[str],
        "Name": NotRequired[str],
        "DataSource": NotRequired[EventDataSourceType],
        "EventClass": NotRequired[EventClassType],
        "Resources": NotRequired[List[EventResourceTypeDef]],
    },
)
MonitoredResourceIdentifierTypeDef = TypedDict(
    "MonitoredResourceIdentifierTypeDef",
    {
        "MonitoredResourceName": NotRequired[str],
        "Type": NotRequired[str],
        "ResourcePermission": NotRequired[ResourcePermissionType],
        "LastUpdated": NotRequired[datetime],
        "ResourceCollection": NotRequired[ResourceCollectionOutputTypeDef],
    },
)
ProactiveInsightSummaryTypeDef = TypedDict(
    "ProactiveInsightSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Severity": NotRequired[InsightSeverityType],
        "Status": NotRequired[InsightStatusType],
        "InsightTimeRange": NotRequired[InsightTimeRangeTypeDef],
        "PredictionTimeRange": NotRequired[PredictionTimeRangeTypeDef],
        "ResourceCollection": NotRequired[ResourceCollectionOutputTypeDef],
        "ServiceCollection": NotRequired[ServiceCollectionOutputTypeDef],
        "AssociatedResourceArns": NotRequired[List[str]],
    },
)
ProactiveInsightTypeDef = TypedDict(
    "ProactiveInsightTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Severity": NotRequired[InsightSeverityType],
        "Status": NotRequired[InsightStatusType],
        "InsightTimeRange": NotRequired[InsightTimeRangeTypeDef],
        "PredictionTimeRange": NotRequired[PredictionTimeRangeTypeDef],
        "ResourceCollection": NotRequired[ResourceCollectionOutputTypeDef],
        "SsmOpsItemId": NotRequired[str],
        "Description": NotRequired[str],
    },
)
ProactiveOrganizationInsightSummaryTypeDef = TypedDict(
    "ProactiveOrganizationInsightSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "AccountId": NotRequired[str],
        "OrganizationalUnitId": NotRequired[str],
        "Name": NotRequired[str],
        "Severity": NotRequired[InsightSeverityType],
        "Status": NotRequired[InsightStatusType],
        "InsightTimeRange": NotRequired[InsightTimeRangeTypeDef],
        "PredictionTimeRange": NotRequired[PredictionTimeRangeTypeDef],
        "ResourceCollection": NotRequired[ResourceCollectionOutputTypeDef],
        "ServiceCollection": NotRequired[ServiceCollectionOutputTypeDef],
    },
)
ReactiveInsightSummaryTypeDef = TypedDict(
    "ReactiveInsightSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Severity": NotRequired[InsightSeverityType],
        "Status": NotRequired[InsightStatusType],
        "InsightTimeRange": NotRequired[InsightTimeRangeTypeDef],
        "ResourceCollection": NotRequired[ResourceCollectionOutputTypeDef],
        "ServiceCollection": NotRequired[ServiceCollectionOutputTypeDef],
        "AssociatedResourceArns": NotRequired[List[str]],
    },
)
ReactiveInsightTypeDef = TypedDict(
    "ReactiveInsightTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Severity": NotRequired[InsightSeverityType],
        "Status": NotRequired[InsightStatusType],
        "InsightTimeRange": NotRequired[InsightTimeRangeTypeDef],
        "ResourceCollection": NotRequired[ResourceCollectionOutputTypeDef],
        "SsmOpsItemId": NotRequired[str],
        "Description": NotRequired[str],
    },
)
ReactiveOrganizationInsightSummaryTypeDef = TypedDict(
    "ReactiveOrganizationInsightSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "AccountId": NotRequired[str],
        "OrganizationalUnitId": NotRequired[str],
        "Name": NotRequired[str],
        "Severity": NotRequired[InsightSeverityType],
        "Status": NotRequired[InsightStatusType],
        "InsightTimeRange": NotRequired[InsightTimeRangeTypeDef],
        "ResourceCollection": NotRequired[ResourceCollectionOutputTypeDef],
        "ServiceCollection": NotRequired[ServiceCollectionOutputTypeDef],
    },
)
ListEventsFiltersTypeDef = TypedDict(
    "ListEventsFiltersTypeDef",
    {
        "InsightId": NotRequired[str],
        "EventTimeRange": NotRequired[EventTimeRangeTypeDef],
        "EventClass": NotRequired[EventClassType],
        "EventSource": NotRequired[str],
        "DataSource": NotRequired[EventDataSourceType],
        "ResourceCollection": NotRequired[ResourceCollectionTypeDef],
    },
)
ResourceCollectionUnionTypeDef = Union[ResourceCollectionTypeDef, ResourceCollectionOutputTypeDef]
DescribeOrganizationResourceCollectionHealthResponseTypeDef = TypedDict(
    "DescribeOrganizationResourceCollectionHealthResponseTypeDef",
    {
        "CloudFormation": List[CloudFormationHealthTypeDef],
        "Service": List[ServiceHealthTypeDef],
        "Account": List[AccountHealthTypeDef],
        "Tags": List[TagHealthTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeResourceCollectionHealthResponseTypeDef = TypedDict(
    "DescribeResourceCollectionHealthResponseTypeDef",
    {
        "CloudFormation": List[CloudFormationHealthTypeDef],
        "Service": List[ServiceHealthTypeDef],
        "Tags": List[TagHealthTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CostEstimationResourceCollectionFilterTypeDef = TypedDict(
    "CostEstimationResourceCollectionFilterTypeDef",
    {
        "CloudFormation": NotRequired[
            CloudFormationCostEstimationResourceCollectionFilterUnionTypeDef
        ],
        "Tags": NotRequired[Sequence[TagCostEstimationResourceCollectionFilterUnionTypeDef]],
    },
)
UpdateResourceCollectionRequestRequestTypeDef = TypedDict(
    "UpdateResourceCollectionRequestRequestTypeDef",
    {
        "Action": UpdateResourceCollectionActionType,
        "ResourceCollection": UpdateResourceCollectionFilterTypeDef,
    },
)
ListInsightsStatusFilterTypeDef = TypedDict(
    "ListInsightsStatusFilterTypeDef",
    {
        "Ongoing": NotRequired[ListInsightsOngoingStatusFilterTypeDef],
        "Closed": NotRequired[ListInsightsClosedStatusFilterTypeDef],
        "Any": NotRequired[ListInsightsAnyStatusFilterTypeDef],
    },
)
ListAnomalousLogGroupsResponseTypeDef = TypedDict(
    "ListAnomalousLogGroupsResponseTypeDef",
    {
        "InsightId": str,
        "AnomalousLogGroups": List[AnomalousLogGroupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListNotificationChannelsResponseTypeDef = TypedDict(
    "ListNotificationChannelsResponseTypeDef",
    {
        "Channels": List[NotificationChannelTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
AddNotificationChannelRequestRequestTypeDef = TypedDict(
    "AddNotificationChannelRequestRequestTypeDef",
    {
        "Config": NotificationChannelConfigTypeDef,
    },
)
PerformanceInsightsReferenceComparisonValuesTypeDef = TypedDict(
    "PerformanceInsightsReferenceComparisonValuesTypeDef",
    {
        "ReferenceScalar": NotRequired[PerformanceInsightsReferenceScalarTypeDef],
        "ReferenceMetric": NotRequired[PerformanceInsightsReferenceMetricTypeDef],
    },
)
RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "Description": NotRequired[str],
        "Link": NotRequired[str],
        "Name": NotRequired[str],
        "Reason": NotRequired[str],
        "RelatedEvents": NotRequired[List[RecommendationRelatedEventTypeDef]],
        "RelatedAnomalies": NotRequired[List[RecommendationRelatedAnomalyTypeDef]],
        "Category": NotRequired[str],
    },
)
ListEventsResponseTypeDef = TypedDict(
    "ListEventsResponseTypeDef",
    {
        "Events": List[EventTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListMonitoredResourcesResponseTypeDef = TypedDict(
    "ListMonitoredResourcesResponseTypeDef",
    {
        "MonitoredResourceIdentifiers": List[MonitoredResourceIdentifierTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListInsightsResponseTypeDef = TypedDict(
    "ListInsightsResponseTypeDef",
    {
        "ProactiveInsights": List[ProactiveInsightSummaryTypeDef],
        "ReactiveInsights": List[ReactiveInsightSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
SearchInsightsResponseTypeDef = TypedDict(
    "SearchInsightsResponseTypeDef",
    {
        "ProactiveInsights": List[ProactiveInsightSummaryTypeDef],
        "ReactiveInsights": List[ReactiveInsightSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
SearchOrganizationInsightsResponseTypeDef = TypedDict(
    "SearchOrganizationInsightsResponseTypeDef",
    {
        "ProactiveInsights": List[ProactiveInsightSummaryTypeDef],
        "ReactiveInsights": List[ReactiveInsightSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeInsightResponseTypeDef = TypedDict(
    "DescribeInsightResponseTypeDef",
    {
        "ProactiveInsight": ProactiveInsightTypeDef,
        "ReactiveInsight": ReactiveInsightTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListOrganizationInsightsResponseTypeDef = TypedDict(
    "ListOrganizationInsightsResponseTypeDef",
    {
        "ProactiveInsights": List[ProactiveOrganizationInsightSummaryTypeDef],
        "ReactiveInsights": List[ReactiveOrganizationInsightSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListEventsRequestListEventsPaginateTypeDef = TypedDict(
    "ListEventsRequestListEventsPaginateTypeDef",
    {
        "Filters": ListEventsFiltersTypeDef,
        "AccountId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEventsRequestRequestTypeDef = TypedDict(
    "ListEventsRequestRequestTypeDef",
    {
        "Filters": ListEventsFiltersTypeDef,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "AccountId": NotRequired[str],
    },
)
SearchInsightsFiltersTypeDef = TypedDict(
    "SearchInsightsFiltersTypeDef",
    {
        "Severities": NotRequired[Sequence[InsightSeverityType]],
        "Statuses": NotRequired[Sequence[InsightStatusType]],
        "ResourceCollection": NotRequired[ResourceCollectionUnionTypeDef],
        "ServiceCollection": NotRequired[ServiceCollectionUnionTypeDef],
    },
)
SearchOrganizationInsightsFiltersTypeDef = TypedDict(
    "SearchOrganizationInsightsFiltersTypeDef",
    {
        "Severities": NotRequired[Sequence[InsightSeverityType]],
        "Statuses": NotRequired[Sequence[InsightStatusType]],
        "ResourceCollection": NotRequired[ResourceCollectionUnionTypeDef],
        "ServiceCollection": NotRequired[ServiceCollectionUnionTypeDef],
    },
)
StartCostEstimationRequestRequestTypeDef = TypedDict(
    "StartCostEstimationRequestRequestTypeDef",
    {
        "ResourceCollection": CostEstimationResourceCollectionFilterTypeDef,
        "ClientToken": NotRequired[str],
    },
)
ListInsightsRequestListInsightsPaginateTypeDef = TypedDict(
    "ListInsightsRequestListInsightsPaginateTypeDef",
    {
        "StatusFilter": ListInsightsStatusFilterTypeDef,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListInsightsRequestRequestTypeDef = TypedDict(
    "ListInsightsRequestRequestTypeDef",
    {
        "StatusFilter": ListInsightsStatusFilterTypeDef,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListOrganizationInsightsRequestListOrganizationInsightsPaginateTypeDef = TypedDict(
    "ListOrganizationInsightsRequestListOrganizationInsightsPaginateTypeDef",
    {
        "StatusFilter": ListInsightsStatusFilterTypeDef,
        "AccountIds": NotRequired[Sequence[str]],
        "OrganizationalUnitIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOrganizationInsightsRequestRequestTypeDef = TypedDict(
    "ListOrganizationInsightsRequestRequestTypeDef",
    {
        "StatusFilter": ListInsightsStatusFilterTypeDef,
        "MaxResults": NotRequired[int],
        "AccountIds": NotRequired[Sequence[str]],
        "OrganizationalUnitIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
    },
)
PerformanceInsightsReferenceDataTypeDef = TypedDict(
    "PerformanceInsightsReferenceDataTypeDef",
    {
        "Name": NotRequired[str],
        "ComparisonValues": NotRequired[PerformanceInsightsReferenceComparisonValuesTypeDef],
    },
)
ListRecommendationsResponseTypeDef = TypedDict(
    "ListRecommendationsResponseTypeDef",
    {
        "Recommendations": List[RecommendationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
SearchInsightsRequestRequestTypeDef = TypedDict(
    "SearchInsightsRequestRequestTypeDef",
    {
        "StartTimeRange": StartTimeRangeTypeDef,
        "Type": InsightTypeType,
        "Filters": NotRequired[SearchInsightsFiltersTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
SearchInsightsRequestSearchInsightsPaginateTypeDef = TypedDict(
    "SearchInsightsRequestSearchInsightsPaginateTypeDef",
    {
        "StartTimeRange": StartTimeRangeTypeDef,
        "Type": InsightTypeType,
        "Filters": NotRequired[SearchInsightsFiltersTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchOrganizationInsightsRequestRequestTypeDef = TypedDict(
    "SearchOrganizationInsightsRequestRequestTypeDef",
    {
        "AccountIds": Sequence[str],
        "StartTimeRange": StartTimeRangeTypeDef,
        "Type": InsightTypeType,
        "Filters": NotRequired[SearchOrganizationInsightsFiltersTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
SearchOrganizationInsightsRequestSearchOrganizationInsightsPaginateTypeDef = TypedDict(
    "SearchOrganizationInsightsRequestSearchOrganizationInsightsPaginateTypeDef",
    {
        "AccountIds": Sequence[str],
        "StartTimeRange": StartTimeRangeTypeDef,
        "Type": InsightTypeType,
        "Filters": NotRequired[SearchOrganizationInsightsFiltersTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
PerformanceInsightsMetricsDetailTypeDef = TypedDict(
    "PerformanceInsightsMetricsDetailTypeDef",
    {
        "MetricDisplayName": NotRequired[str],
        "Unit": NotRequired[str],
        "MetricQuery": NotRequired[PerformanceInsightsMetricQueryTypeDef],
        "ReferenceData": NotRequired[List[PerformanceInsightsReferenceDataTypeDef]],
        "StatsAtAnomaly": NotRequired[List[PerformanceInsightsStatTypeDef]],
        "StatsAtBaseline": NotRequired[List[PerformanceInsightsStatTypeDef]],
    },
)
AnomalySourceDetailsTypeDef = TypedDict(
    "AnomalySourceDetailsTypeDef",
    {
        "CloudWatchMetrics": NotRequired[List[CloudWatchMetricsDetailTypeDef]],
        "PerformanceInsightsMetrics": NotRequired[List[PerformanceInsightsMetricsDetailTypeDef]],
    },
)
ProactiveAnomalySummaryTypeDef = TypedDict(
    "ProactiveAnomalySummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Severity": NotRequired[AnomalySeverityType],
        "Status": NotRequired[AnomalyStatusType],
        "UpdateTime": NotRequired[datetime],
        "AnomalyTimeRange": NotRequired[AnomalyTimeRangeTypeDef],
        "AnomalyReportedTimeRange": NotRequired[AnomalyReportedTimeRangeTypeDef],
        "PredictionTimeRange": NotRequired[PredictionTimeRangeTypeDef],
        "SourceDetails": NotRequired[AnomalySourceDetailsTypeDef],
        "AssociatedInsightId": NotRequired[str],
        "ResourceCollection": NotRequired[ResourceCollectionOutputTypeDef],
        "Limit": NotRequired[float],
        "SourceMetadata": NotRequired[AnomalySourceMetadataTypeDef],
        "AnomalyResources": NotRequired[List[AnomalyResourceTypeDef]],
        "Description": NotRequired[str],
    },
)
ProactiveAnomalyTypeDef = TypedDict(
    "ProactiveAnomalyTypeDef",
    {
        "Id": NotRequired[str],
        "Severity": NotRequired[AnomalySeverityType],
        "Status": NotRequired[AnomalyStatusType],
        "UpdateTime": NotRequired[datetime],
        "AnomalyTimeRange": NotRequired[AnomalyTimeRangeTypeDef],
        "AnomalyReportedTimeRange": NotRequired[AnomalyReportedTimeRangeTypeDef],
        "PredictionTimeRange": NotRequired[PredictionTimeRangeTypeDef],
        "SourceDetails": NotRequired[AnomalySourceDetailsTypeDef],
        "AssociatedInsightId": NotRequired[str],
        "ResourceCollection": NotRequired[ResourceCollectionOutputTypeDef],
        "Limit": NotRequired[float],
        "SourceMetadata": NotRequired[AnomalySourceMetadataTypeDef],
        "AnomalyResources": NotRequired[List[AnomalyResourceTypeDef]],
        "Description": NotRequired[str],
    },
)
ReactiveAnomalySummaryTypeDef = TypedDict(
    "ReactiveAnomalySummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Severity": NotRequired[AnomalySeverityType],
        "Status": NotRequired[AnomalyStatusType],
        "AnomalyTimeRange": NotRequired[AnomalyTimeRangeTypeDef],
        "AnomalyReportedTimeRange": NotRequired[AnomalyReportedTimeRangeTypeDef],
        "SourceDetails": NotRequired[AnomalySourceDetailsTypeDef],
        "AssociatedInsightId": NotRequired[str],
        "ResourceCollection": NotRequired[ResourceCollectionOutputTypeDef],
        "Type": NotRequired[AnomalyTypeType],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "CausalAnomalyId": NotRequired[str],
        "AnomalyResources": NotRequired[List[AnomalyResourceTypeDef]],
    },
)
ReactiveAnomalyTypeDef = TypedDict(
    "ReactiveAnomalyTypeDef",
    {
        "Id": NotRequired[str],
        "Severity": NotRequired[AnomalySeverityType],
        "Status": NotRequired[AnomalyStatusType],
        "AnomalyTimeRange": NotRequired[AnomalyTimeRangeTypeDef],
        "AnomalyReportedTimeRange": NotRequired[AnomalyReportedTimeRangeTypeDef],
        "SourceDetails": NotRequired[AnomalySourceDetailsTypeDef],
        "AssociatedInsightId": NotRequired[str],
        "ResourceCollection": NotRequired[ResourceCollectionOutputTypeDef],
        "Type": NotRequired[AnomalyTypeType],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "CausalAnomalyId": NotRequired[str],
        "AnomalyResources": NotRequired[List[AnomalyResourceTypeDef]],
    },
)
ListAnomaliesForInsightResponseTypeDef = TypedDict(
    "ListAnomaliesForInsightResponseTypeDef",
    {
        "ProactiveAnomalies": List[ProactiveAnomalySummaryTypeDef],
        "ReactiveAnomalies": List[ReactiveAnomalySummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeAnomalyResponseTypeDef = TypedDict(
    "DescribeAnomalyResponseTypeDef",
    {
        "ProactiveAnomaly": ProactiveAnomalyTypeDef,
        "ReactiveAnomaly": ReactiveAnomalyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
