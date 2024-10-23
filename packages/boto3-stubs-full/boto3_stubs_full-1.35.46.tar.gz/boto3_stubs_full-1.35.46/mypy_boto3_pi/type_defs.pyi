"""
Type annotations for pi service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pi/type_defs/)

Usage::

    ```python
    from mypy_boto3_pi.type_defs import TagTypeDef

    data: TagTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    AnalysisStatusType,
    ContextTypeType,
    DetailStatusType,
    FeatureStatusType,
    FineGrainedActionType,
    PeriodAlignmentType,
    ServiceTypeType,
    SeverityType,
    TextFormatType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "TagTypeDef",
    "TimestampTypeDef",
    "ResponseMetadataTypeDef",
    "DataPointTypeDef",
    "PerformanceInsightsMetricTypeDef",
    "DeletePerformanceAnalysisReportRequestRequestTypeDef",
    "DimensionGroupTypeDef",
    "DimensionKeyDescriptionTypeDef",
    "ResponsePartitionKeyTypeDef",
    "DimensionDetailTypeDef",
    "DimensionKeyDetailTypeDef",
    "FeatureMetadataTypeDef",
    "GetDimensionKeyDetailsRequestRequestTypeDef",
    "GetPerformanceAnalysisReportRequestRequestTypeDef",
    "GetResourceMetadataRequestRequestTypeDef",
    "RecommendationTypeDef",
    "ListAvailableResourceDimensionsRequestRequestTypeDef",
    "ListAvailableResourceMetricsRequestRequestTypeDef",
    "ResponseResourceMetricTypeDef",
    "ListPerformanceAnalysisReportsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ResponseResourceMetricKeyTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "AnalysisReportSummaryTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreatePerformanceAnalysisReportRequestRequestTypeDef",
    "CreatePerformanceAnalysisReportResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "DataTypeDef",
    "DescribeDimensionKeysRequestRequestTypeDef",
    "MetricQueryTypeDef",
    "DescribeDimensionKeysResponseTypeDef",
    "DimensionGroupDetailTypeDef",
    "GetDimensionKeyDetailsResponseTypeDef",
    "GetResourceMetadataResponseTypeDef",
    "ListAvailableResourceMetricsResponseTypeDef",
    "MetricKeyDataPointsTypeDef",
    "ListPerformanceAnalysisReportsResponseTypeDef",
    "InsightTypeDef",
    "GetResourceMetricsRequestRequestTypeDef",
    "MetricDimensionGroupsTypeDef",
    "GetResourceMetricsResponseTypeDef",
    "AnalysisReportTypeDef",
    "ListAvailableResourceDimensionsResponseTypeDef",
    "GetPerformanceAnalysisReportResponseTypeDef",
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
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
DataPointTypeDef = TypedDict(
    "DataPointTypeDef",
    {
        "Timestamp": datetime,
        "Value": float,
    },
)
PerformanceInsightsMetricTypeDef = TypedDict(
    "PerformanceInsightsMetricTypeDef",
    {
        "Metric": NotRequired[str],
        "DisplayName": NotRequired[str],
        "Dimensions": NotRequired[Dict[str, str]],
        "Value": NotRequired[float],
    },
)
DeletePerformanceAnalysisReportRequestRequestTypeDef = TypedDict(
    "DeletePerformanceAnalysisReportRequestRequestTypeDef",
    {
        "ServiceType": ServiceTypeType,
        "Identifier": str,
        "AnalysisReportId": str,
    },
)
DimensionGroupTypeDef = TypedDict(
    "DimensionGroupTypeDef",
    {
        "Group": str,
        "Dimensions": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
    },
)
DimensionKeyDescriptionTypeDef = TypedDict(
    "DimensionKeyDescriptionTypeDef",
    {
        "Dimensions": NotRequired[Dict[str, str]],
        "Total": NotRequired[float],
        "AdditionalMetrics": NotRequired[Dict[str, float]],
        "Partitions": NotRequired[List[float]],
    },
)
ResponsePartitionKeyTypeDef = TypedDict(
    "ResponsePartitionKeyTypeDef",
    {
        "Dimensions": Dict[str, str],
    },
)
DimensionDetailTypeDef = TypedDict(
    "DimensionDetailTypeDef",
    {
        "Identifier": NotRequired[str],
    },
)
DimensionKeyDetailTypeDef = TypedDict(
    "DimensionKeyDetailTypeDef",
    {
        "Value": NotRequired[str],
        "Dimension": NotRequired[str],
        "Status": NotRequired[DetailStatusType],
    },
)
FeatureMetadataTypeDef = TypedDict(
    "FeatureMetadataTypeDef",
    {
        "Status": NotRequired[FeatureStatusType],
    },
)
GetDimensionKeyDetailsRequestRequestTypeDef = TypedDict(
    "GetDimensionKeyDetailsRequestRequestTypeDef",
    {
        "ServiceType": ServiceTypeType,
        "Identifier": str,
        "Group": str,
        "GroupIdentifier": str,
        "RequestedDimensions": NotRequired[Sequence[str]],
    },
)
GetPerformanceAnalysisReportRequestRequestTypeDef = TypedDict(
    "GetPerformanceAnalysisReportRequestRequestTypeDef",
    {
        "ServiceType": ServiceTypeType,
        "Identifier": str,
        "AnalysisReportId": str,
        "TextFormat": NotRequired[TextFormatType],
        "AcceptLanguage": NotRequired[Literal["EN_US"]],
    },
)
GetResourceMetadataRequestRequestTypeDef = TypedDict(
    "GetResourceMetadataRequestRequestTypeDef",
    {
        "ServiceType": ServiceTypeType,
        "Identifier": str,
    },
)
RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "RecommendationId": NotRequired[str],
        "RecommendationDescription": NotRequired[str],
    },
)
ListAvailableResourceDimensionsRequestRequestTypeDef = TypedDict(
    "ListAvailableResourceDimensionsRequestRequestTypeDef",
    {
        "ServiceType": ServiceTypeType,
        "Identifier": str,
        "Metrics": Sequence[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "AuthorizedActions": NotRequired[Sequence[FineGrainedActionType]],
    },
)
ListAvailableResourceMetricsRequestRequestTypeDef = TypedDict(
    "ListAvailableResourceMetricsRequestRequestTypeDef",
    {
        "ServiceType": ServiceTypeType,
        "Identifier": str,
        "MetricTypes": Sequence[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ResponseResourceMetricTypeDef = TypedDict(
    "ResponseResourceMetricTypeDef",
    {
        "Metric": NotRequired[str],
        "Description": NotRequired[str],
        "Unit": NotRequired[str],
    },
)
ListPerformanceAnalysisReportsRequestRequestTypeDef = TypedDict(
    "ListPerformanceAnalysisReportsRequestRequestTypeDef",
    {
        "ServiceType": ServiceTypeType,
        "Identifier": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ListTags": NotRequired[bool],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ServiceType": ServiceTypeType,
        "ResourceARN": str,
    },
)
ResponseResourceMetricKeyTypeDef = TypedDict(
    "ResponseResourceMetricKeyTypeDef",
    {
        "Metric": str,
        "Dimensions": NotRequired[Dict[str, str]],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ServiceType": ServiceTypeType,
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
AnalysisReportSummaryTypeDef = TypedDict(
    "AnalysisReportSummaryTypeDef",
    {
        "AnalysisReportId": NotRequired[str],
        "CreateTime": NotRequired[datetime],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "Status": NotRequired[AnalysisStatusType],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ServiceType": ServiceTypeType,
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CreatePerformanceAnalysisReportRequestRequestTypeDef = TypedDict(
    "CreatePerformanceAnalysisReportRequestRequestTypeDef",
    {
        "ServiceType": ServiceTypeType,
        "Identifier": str,
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreatePerformanceAnalysisReportResponseTypeDef = TypedDict(
    "CreatePerformanceAnalysisReportResponseTypeDef",
    {
        "AnalysisReportId": str,
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
DataTypeDef = TypedDict(
    "DataTypeDef",
    {
        "PerformanceInsightsMetric": NotRequired[PerformanceInsightsMetricTypeDef],
    },
)
DescribeDimensionKeysRequestRequestTypeDef = TypedDict(
    "DescribeDimensionKeysRequestRequestTypeDef",
    {
        "ServiceType": ServiceTypeType,
        "Identifier": str,
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
        "Metric": str,
        "GroupBy": DimensionGroupTypeDef,
        "PeriodInSeconds": NotRequired[int],
        "AdditionalMetrics": NotRequired[Sequence[str]],
        "PartitionBy": NotRequired[DimensionGroupTypeDef],
        "Filter": NotRequired[Mapping[str, str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
MetricQueryTypeDef = TypedDict(
    "MetricQueryTypeDef",
    {
        "Metric": str,
        "GroupBy": NotRequired[DimensionGroupTypeDef],
        "Filter": NotRequired[Mapping[str, str]],
    },
)
DescribeDimensionKeysResponseTypeDef = TypedDict(
    "DescribeDimensionKeysResponseTypeDef",
    {
        "AlignedStartTime": datetime,
        "AlignedEndTime": datetime,
        "PartitionKeys": List[ResponsePartitionKeyTypeDef],
        "Keys": List[DimensionKeyDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DimensionGroupDetailTypeDef = TypedDict(
    "DimensionGroupDetailTypeDef",
    {
        "Group": NotRequired[str],
        "Dimensions": NotRequired[List[DimensionDetailTypeDef]],
    },
)
GetDimensionKeyDetailsResponseTypeDef = TypedDict(
    "GetDimensionKeyDetailsResponseTypeDef",
    {
        "Dimensions": List[DimensionKeyDetailTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResourceMetadataResponseTypeDef = TypedDict(
    "GetResourceMetadataResponseTypeDef",
    {
        "Identifier": str,
        "Features": Dict[str, FeatureMetadataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAvailableResourceMetricsResponseTypeDef = TypedDict(
    "ListAvailableResourceMetricsResponseTypeDef",
    {
        "Metrics": List[ResponseResourceMetricTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
MetricKeyDataPointsTypeDef = TypedDict(
    "MetricKeyDataPointsTypeDef",
    {
        "Key": NotRequired[ResponseResourceMetricKeyTypeDef],
        "DataPoints": NotRequired[List[DataPointTypeDef]],
    },
)
ListPerformanceAnalysisReportsResponseTypeDef = TypedDict(
    "ListPerformanceAnalysisReportsResponseTypeDef",
    {
        "AnalysisReports": List[AnalysisReportSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
InsightTypeDef = TypedDict(
    "InsightTypeDef",
    {
        "InsightId": str,
        "InsightType": NotRequired[str],
        "Context": NotRequired[ContextTypeType],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "Severity": NotRequired[SeverityType],
        "SupportingInsights": NotRequired[List[Dict[str, Any]]],
        "Description": NotRequired[str],
        "Recommendations": NotRequired[List[RecommendationTypeDef]],
        "InsightData": NotRequired[List[DataTypeDef]],
        "BaselineData": NotRequired[List[DataTypeDef]],
    },
)
GetResourceMetricsRequestRequestTypeDef = TypedDict(
    "GetResourceMetricsRequestRequestTypeDef",
    {
        "ServiceType": ServiceTypeType,
        "Identifier": str,
        "MetricQueries": Sequence[MetricQueryTypeDef],
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
        "PeriodInSeconds": NotRequired[int],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "PeriodAlignment": NotRequired[PeriodAlignmentType],
    },
)
MetricDimensionGroupsTypeDef = TypedDict(
    "MetricDimensionGroupsTypeDef",
    {
        "Metric": NotRequired[str],
        "Groups": NotRequired[List[DimensionGroupDetailTypeDef]],
    },
)
GetResourceMetricsResponseTypeDef = TypedDict(
    "GetResourceMetricsResponseTypeDef",
    {
        "AlignedStartTime": datetime,
        "AlignedEndTime": datetime,
        "Identifier": str,
        "MetricList": List[MetricKeyDataPointsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
AnalysisReportTypeDef = TypedDict(
    "AnalysisReportTypeDef",
    {
        "AnalysisReportId": str,
        "Identifier": NotRequired[str],
        "ServiceType": NotRequired[ServiceTypeType],
        "CreateTime": NotRequired[datetime],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "Status": NotRequired[AnalysisStatusType],
        "Insights": NotRequired[List[InsightTypeDef]],
    },
)
ListAvailableResourceDimensionsResponseTypeDef = TypedDict(
    "ListAvailableResourceDimensionsResponseTypeDef",
    {
        "MetricDimensions": List[MetricDimensionGroupsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetPerformanceAnalysisReportResponseTypeDef = TypedDict(
    "GetPerformanceAnalysisReportResponseTypeDef",
    {
        "AnalysisReport": AnalysisReportTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
