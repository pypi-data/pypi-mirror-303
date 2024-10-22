"""
Type annotations for iot-jobs-data service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_jobs_data/type_defs/)

Usage::

    ```python
    from mypy_boto3_iot_jobs_data.type_defs import DescribeJobExecutionRequestRequestTypeDef

    data: DescribeJobExecutionRequestRequestTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Mapping

from .literals import JobExecutionStatusType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "DescribeJobExecutionRequestRequestTypeDef",
    "JobExecutionTypeDef",
    "ResponseMetadataTypeDef",
    "GetPendingJobExecutionsRequestRequestTypeDef",
    "JobExecutionSummaryTypeDef",
    "JobExecutionStateTypeDef",
    "StartNextPendingJobExecutionRequestRequestTypeDef",
    "UpdateJobExecutionRequestRequestTypeDef",
    "DescribeJobExecutionResponseTypeDef",
    "StartNextPendingJobExecutionResponseTypeDef",
    "GetPendingJobExecutionsResponseTypeDef",
    "UpdateJobExecutionResponseTypeDef",
)

DescribeJobExecutionRequestRequestTypeDef = TypedDict(
    "DescribeJobExecutionRequestRequestTypeDef",
    {
        "jobId": str,
        "thingName": str,
        "includeJobDocument": NotRequired[bool],
        "executionNumber": NotRequired[int],
    },
)
JobExecutionTypeDef = TypedDict(
    "JobExecutionTypeDef",
    {
        "jobId": NotRequired[str],
        "thingName": NotRequired[str],
        "status": NotRequired[JobExecutionStatusType],
        "statusDetails": NotRequired[Dict[str, str]],
        "queuedAt": NotRequired[int],
        "startedAt": NotRequired[int],
        "lastUpdatedAt": NotRequired[int],
        "approximateSecondsBeforeTimedOut": NotRequired[int],
        "versionNumber": NotRequired[int],
        "executionNumber": NotRequired[int],
        "jobDocument": NotRequired[str],
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
GetPendingJobExecutionsRequestRequestTypeDef = TypedDict(
    "GetPendingJobExecutionsRequestRequestTypeDef",
    {
        "thingName": str,
    },
)
JobExecutionSummaryTypeDef = TypedDict(
    "JobExecutionSummaryTypeDef",
    {
        "jobId": NotRequired[str],
        "queuedAt": NotRequired[int],
        "startedAt": NotRequired[int],
        "lastUpdatedAt": NotRequired[int],
        "versionNumber": NotRequired[int],
        "executionNumber": NotRequired[int],
    },
)
JobExecutionStateTypeDef = TypedDict(
    "JobExecutionStateTypeDef",
    {
        "status": NotRequired[JobExecutionStatusType],
        "statusDetails": NotRequired[Dict[str, str]],
        "versionNumber": NotRequired[int],
    },
)
StartNextPendingJobExecutionRequestRequestTypeDef = TypedDict(
    "StartNextPendingJobExecutionRequestRequestTypeDef",
    {
        "thingName": str,
        "statusDetails": NotRequired[Mapping[str, str]],
        "stepTimeoutInMinutes": NotRequired[int],
    },
)
UpdateJobExecutionRequestRequestTypeDef = TypedDict(
    "UpdateJobExecutionRequestRequestTypeDef",
    {
        "jobId": str,
        "thingName": str,
        "status": JobExecutionStatusType,
        "statusDetails": NotRequired[Mapping[str, str]],
        "stepTimeoutInMinutes": NotRequired[int],
        "expectedVersion": NotRequired[int],
        "includeJobExecutionState": NotRequired[bool],
        "includeJobDocument": NotRequired[bool],
        "executionNumber": NotRequired[int],
    },
)
DescribeJobExecutionResponseTypeDef = TypedDict(
    "DescribeJobExecutionResponseTypeDef",
    {
        "execution": JobExecutionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartNextPendingJobExecutionResponseTypeDef = TypedDict(
    "StartNextPendingJobExecutionResponseTypeDef",
    {
        "execution": JobExecutionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPendingJobExecutionsResponseTypeDef = TypedDict(
    "GetPendingJobExecutionsResponseTypeDef",
    {
        "inProgressJobs": List[JobExecutionSummaryTypeDef],
        "queuedJobs": List[JobExecutionSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateJobExecutionResponseTypeDef = TypedDict(
    "UpdateJobExecutionResponseTypeDef",
    {
        "executionState": JobExecutionStateTypeDef,
        "jobDocument": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
