"""
Type annotations for sagemaker-metrics service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_metrics/type_defs/)

Usage::

    ```python
    from mypy_boto3_sagemaker_metrics.type_defs import MetricQueryTypeDef

    data: MetricQueryTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    MetricQueryResultStatusType,
    MetricStatisticType,
    PeriodType,
    PutMetricsErrorCodeType,
    XAxisTypeType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "MetricQueryTypeDef",
    "MetricQueryResultTypeDef",
    "ResponseMetadataTypeDef",
    "BatchPutMetricsErrorTypeDef",
    "TimestampTypeDef",
    "BatchGetMetricsRequestRequestTypeDef",
    "BatchGetMetricsResponseTypeDef",
    "BatchPutMetricsResponseTypeDef",
    "RawMetricDataTypeDef",
    "BatchPutMetricsRequestRequestTypeDef",
)

MetricQueryTypeDef = TypedDict(
    "MetricQueryTypeDef",
    {
        "MetricName": str,
        "ResourceArn": str,
        "MetricStat": MetricStatisticType,
        "Period": PeriodType,
        "XAxisType": XAxisTypeType,
        "Start": NotRequired[int],
        "End": NotRequired[int],
    },
)
MetricQueryResultTypeDef = TypedDict(
    "MetricQueryResultTypeDef",
    {
        "Status": MetricQueryResultStatusType,
        "XAxisValues": List[int],
        "MetricValues": List[float],
        "Message": NotRequired[str],
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
BatchPutMetricsErrorTypeDef = TypedDict(
    "BatchPutMetricsErrorTypeDef",
    {
        "Code": NotRequired[PutMetricsErrorCodeType],
        "MetricIndex": NotRequired[int],
    },
)
TimestampTypeDef = Union[datetime, str]
BatchGetMetricsRequestRequestTypeDef = TypedDict(
    "BatchGetMetricsRequestRequestTypeDef",
    {
        "MetricQueries": Sequence[MetricQueryTypeDef],
    },
)
BatchGetMetricsResponseTypeDef = TypedDict(
    "BatchGetMetricsResponseTypeDef",
    {
        "MetricQueryResults": List[MetricQueryResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchPutMetricsResponseTypeDef = TypedDict(
    "BatchPutMetricsResponseTypeDef",
    {
        "Errors": List[BatchPutMetricsErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RawMetricDataTypeDef = TypedDict(
    "RawMetricDataTypeDef",
    {
        "MetricName": str,
        "Timestamp": TimestampTypeDef,
        "Value": float,
        "Step": NotRequired[int],
    },
)
BatchPutMetricsRequestRequestTypeDef = TypedDict(
    "BatchPutMetricsRequestRequestTypeDef",
    {
        "TrialComponentName": str,
        "MetricData": Sequence[RawMetricDataTypeDef],
    },
)
