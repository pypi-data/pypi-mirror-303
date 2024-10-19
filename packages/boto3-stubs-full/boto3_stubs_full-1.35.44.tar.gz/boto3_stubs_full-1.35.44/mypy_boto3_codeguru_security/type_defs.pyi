"""
Type annotations for codeguru-security service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_security/type_defs/)

Usage::

    ```python
    from mypy_boto3_codeguru_security.type_defs import FindingMetricsValuePerSeverityTypeDef

    data: FindingMetricsValuePerSeverityTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AnalysisTypeType,
    ErrorCodeType,
    ScanStateType,
    ScanTypeType,
    SeverityType,
    StatusType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "FindingMetricsValuePerSeverityTypeDef",
    "BatchGetFindingsErrorTypeDef",
    "FindingIdentifierTypeDef",
    "ResponseMetadataTypeDef",
    "CategoryWithFindingNumTypeDef",
    "CodeLineTypeDef",
    "ResourceIdTypeDef",
    "CreateUploadUrlRequestRequestTypeDef",
    "EncryptionConfigTypeDef",
    "ResourceTypeDef",
    "PaginatorConfigTypeDef",
    "GetFindingsRequestRequestTypeDef",
    "TimestampTypeDef",
    "GetScanRequestRequestTypeDef",
    "ListScansRequestRequestTypeDef",
    "ScanSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ScanNameWithFindingNumTypeDef",
    "RecommendationTypeDef",
    "SuggestedFixTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "AccountFindingsMetricTypeDef",
    "BatchGetFindingsRequestRequestTypeDef",
    "CreateUploadUrlResponseTypeDef",
    "GetScanResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "FilePathTypeDef",
    "CreateScanRequestRequestTypeDef",
    "CreateScanResponseTypeDef",
    "GetAccountConfigurationResponseTypeDef",
    "UpdateAccountConfigurationRequestRequestTypeDef",
    "UpdateAccountConfigurationResponseTypeDef",
    "GetFindingsRequestGetFindingsPaginateTypeDef",
    "ListScansRequestListScansPaginateTypeDef",
    "GetMetricsSummaryRequestRequestTypeDef",
    "ListFindingsMetricsRequestListFindingsMetricsPaginateTypeDef",
    "ListFindingsMetricsRequestRequestTypeDef",
    "ListScansResponseTypeDef",
    "MetricsSummaryTypeDef",
    "RemediationTypeDef",
    "ListFindingsMetricsResponseTypeDef",
    "VulnerabilityTypeDef",
    "GetMetricsSummaryResponseTypeDef",
    "FindingTypeDef",
    "BatchGetFindingsResponseTypeDef",
    "GetFindingsResponseTypeDef",
)

FindingMetricsValuePerSeverityTypeDef = TypedDict(
    "FindingMetricsValuePerSeverityTypeDef",
    {
        "critical": NotRequired[float],
        "high": NotRequired[float],
        "info": NotRequired[float],
        "low": NotRequired[float],
        "medium": NotRequired[float],
    },
)
BatchGetFindingsErrorTypeDef = TypedDict(
    "BatchGetFindingsErrorTypeDef",
    {
        "errorCode": ErrorCodeType,
        "findingId": str,
        "message": str,
        "scanName": str,
    },
)
FindingIdentifierTypeDef = TypedDict(
    "FindingIdentifierTypeDef",
    {
        "findingId": str,
        "scanName": str,
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
CategoryWithFindingNumTypeDef = TypedDict(
    "CategoryWithFindingNumTypeDef",
    {
        "categoryName": NotRequired[str],
        "findingNumber": NotRequired[int],
    },
)
CodeLineTypeDef = TypedDict(
    "CodeLineTypeDef",
    {
        "content": NotRequired[str],
        "number": NotRequired[int],
    },
)
ResourceIdTypeDef = TypedDict(
    "ResourceIdTypeDef",
    {
        "codeArtifactId": NotRequired[str],
    },
)
CreateUploadUrlRequestRequestTypeDef = TypedDict(
    "CreateUploadUrlRequestRequestTypeDef",
    {
        "scanName": str,
    },
)
EncryptionConfigTypeDef = TypedDict(
    "EncryptionConfigTypeDef",
    {
        "kmsKeyArn": NotRequired[str],
    },
)
ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "id": NotRequired[str],
        "subResourceId": NotRequired[str],
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
GetFindingsRequestRequestTypeDef = TypedDict(
    "GetFindingsRequestRequestTypeDef",
    {
        "scanName": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "status": NotRequired[StatusType],
    },
)
TimestampTypeDef = Union[datetime, str]
GetScanRequestRequestTypeDef = TypedDict(
    "GetScanRequestRequestTypeDef",
    {
        "scanName": str,
        "runId": NotRequired[str],
    },
)
ListScansRequestRequestTypeDef = TypedDict(
    "ListScansRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ScanSummaryTypeDef = TypedDict(
    "ScanSummaryTypeDef",
    {
        "createdAt": datetime,
        "runId": str,
        "scanName": str,
        "scanState": ScanStateType,
        "scanNameArn": NotRequired[str],
        "updatedAt": NotRequired[datetime],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
ScanNameWithFindingNumTypeDef = TypedDict(
    "ScanNameWithFindingNumTypeDef",
    {
        "findingNumber": NotRequired[int],
        "scanName": NotRequired[str],
    },
)
RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "text": NotRequired[str],
        "url": NotRequired[str],
    },
)
SuggestedFixTypeDef = TypedDict(
    "SuggestedFixTypeDef",
    {
        "code": NotRequired[str],
        "description": NotRequired[str],
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
AccountFindingsMetricTypeDef = TypedDict(
    "AccountFindingsMetricTypeDef",
    {
        "closedFindings": NotRequired[FindingMetricsValuePerSeverityTypeDef],
        "date": NotRequired[datetime],
        "meanTimeToClose": NotRequired[FindingMetricsValuePerSeverityTypeDef],
        "newFindings": NotRequired[FindingMetricsValuePerSeverityTypeDef],
        "openFindings": NotRequired[FindingMetricsValuePerSeverityTypeDef],
    },
)
BatchGetFindingsRequestRequestTypeDef = TypedDict(
    "BatchGetFindingsRequestRequestTypeDef",
    {
        "findingIdentifiers": Sequence[FindingIdentifierTypeDef],
    },
)
CreateUploadUrlResponseTypeDef = TypedDict(
    "CreateUploadUrlResponseTypeDef",
    {
        "codeArtifactId": str,
        "requestHeaders": Dict[str, str],
        "s3Url": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetScanResponseTypeDef = TypedDict(
    "GetScanResponseTypeDef",
    {
        "analysisType": AnalysisTypeType,
        "createdAt": datetime,
        "errorMessage": str,
        "numberOfRevisions": int,
        "runId": str,
        "scanName": str,
        "scanNameArn": str,
        "scanState": ScanStateType,
        "updatedAt": datetime,
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
FilePathTypeDef = TypedDict(
    "FilePathTypeDef",
    {
        "codeSnippet": NotRequired[List[CodeLineTypeDef]],
        "endLine": NotRequired[int],
        "name": NotRequired[str],
        "path": NotRequired[str],
        "startLine": NotRequired[int],
    },
)
CreateScanRequestRequestTypeDef = TypedDict(
    "CreateScanRequestRequestTypeDef",
    {
        "resourceId": ResourceIdTypeDef,
        "scanName": str,
        "analysisType": NotRequired[AnalysisTypeType],
        "clientToken": NotRequired[str],
        "scanType": NotRequired[ScanTypeType],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateScanResponseTypeDef = TypedDict(
    "CreateScanResponseTypeDef",
    {
        "resourceId": ResourceIdTypeDef,
        "runId": str,
        "scanName": str,
        "scanNameArn": str,
        "scanState": ScanStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAccountConfigurationResponseTypeDef = TypedDict(
    "GetAccountConfigurationResponseTypeDef",
    {
        "encryptionConfig": EncryptionConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAccountConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateAccountConfigurationRequestRequestTypeDef",
    {
        "encryptionConfig": EncryptionConfigTypeDef,
    },
)
UpdateAccountConfigurationResponseTypeDef = TypedDict(
    "UpdateAccountConfigurationResponseTypeDef",
    {
        "encryptionConfig": EncryptionConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFindingsRequestGetFindingsPaginateTypeDef = TypedDict(
    "GetFindingsRequestGetFindingsPaginateTypeDef",
    {
        "scanName": str,
        "status": NotRequired[StatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListScansRequestListScansPaginateTypeDef = TypedDict(
    "ListScansRequestListScansPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetMetricsSummaryRequestRequestTypeDef = TypedDict(
    "GetMetricsSummaryRequestRequestTypeDef",
    {
        "date": TimestampTypeDef,
    },
)
ListFindingsMetricsRequestListFindingsMetricsPaginateTypeDef = TypedDict(
    "ListFindingsMetricsRequestListFindingsMetricsPaginateTypeDef",
    {
        "endDate": TimestampTypeDef,
        "startDate": TimestampTypeDef,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFindingsMetricsRequestRequestTypeDef = TypedDict(
    "ListFindingsMetricsRequestRequestTypeDef",
    {
        "endDate": TimestampTypeDef,
        "startDate": TimestampTypeDef,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListScansResponseTypeDef = TypedDict(
    "ListScansResponseTypeDef",
    {
        "nextToken": str,
        "summaries": List[ScanSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MetricsSummaryTypeDef = TypedDict(
    "MetricsSummaryTypeDef",
    {
        "categoriesWithMostFindings": NotRequired[List[CategoryWithFindingNumTypeDef]],
        "date": NotRequired[datetime],
        "openFindings": NotRequired[FindingMetricsValuePerSeverityTypeDef],
        "scansWithMostOpenCriticalFindings": NotRequired[List[ScanNameWithFindingNumTypeDef]],
        "scansWithMostOpenFindings": NotRequired[List[ScanNameWithFindingNumTypeDef]],
    },
)
RemediationTypeDef = TypedDict(
    "RemediationTypeDef",
    {
        "recommendation": NotRequired[RecommendationTypeDef],
        "suggestedFixes": NotRequired[List[SuggestedFixTypeDef]],
    },
)
ListFindingsMetricsResponseTypeDef = TypedDict(
    "ListFindingsMetricsResponseTypeDef",
    {
        "findingsMetrics": List[AccountFindingsMetricTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VulnerabilityTypeDef = TypedDict(
    "VulnerabilityTypeDef",
    {
        "filePath": NotRequired[FilePathTypeDef],
        "id": NotRequired[str],
        "itemCount": NotRequired[int],
        "referenceUrls": NotRequired[List[str]],
        "relatedVulnerabilities": NotRequired[List[str]],
    },
)
GetMetricsSummaryResponseTypeDef = TypedDict(
    "GetMetricsSummaryResponseTypeDef",
    {
        "metricsSummary": MetricsSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FindingTypeDef = TypedDict(
    "FindingTypeDef",
    {
        "createdAt": NotRequired[datetime],
        "description": NotRequired[str],
        "detectorId": NotRequired[str],
        "detectorName": NotRequired[str],
        "detectorTags": NotRequired[List[str]],
        "generatorId": NotRequired[str],
        "id": NotRequired[str],
        "remediation": NotRequired[RemediationTypeDef],
        "resource": NotRequired[ResourceTypeDef],
        "ruleId": NotRequired[str],
        "severity": NotRequired[SeverityType],
        "status": NotRequired[StatusType],
        "title": NotRequired[str],
        "type": NotRequired[str],
        "updatedAt": NotRequired[datetime],
        "vulnerability": NotRequired[VulnerabilityTypeDef],
    },
)
BatchGetFindingsResponseTypeDef = TypedDict(
    "BatchGetFindingsResponseTypeDef",
    {
        "failedFindings": List[BatchGetFindingsErrorTypeDef],
        "findings": List[FindingTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFindingsResponseTypeDef = TypedDict(
    "GetFindingsResponseTypeDef",
    {
        "findings": List[FindingTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
