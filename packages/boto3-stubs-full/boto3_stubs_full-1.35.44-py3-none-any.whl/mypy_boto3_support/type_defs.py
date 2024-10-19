"""
Type annotations for support service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support/type_defs/)

Usage::

    ```python
    from mypy_boto3_support.type_defs import ResponseMetadataTypeDef

    data: ResponseMetadataTypeDef = ...
    ```
"""

import sys
from typing import IO, Any, Dict, List, Sequence, Union

from botocore.response import StreamingBody

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "ResponseMetadataTypeDef",
    "AddCommunicationToCaseRequestRequestTypeDef",
    "AttachmentDetailsTypeDef",
    "AttachmentOutputTypeDef",
    "BlobTypeDef",
    "CategoryTypeDef",
    "DateIntervalTypeDef",
    "SupportedHourTypeDef",
    "CreateCaseRequestRequestTypeDef",
    "DescribeAttachmentRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeCasesRequestRequestTypeDef",
    "DescribeCommunicationsRequestRequestTypeDef",
    "DescribeCreateCaseOptionsRequestRequestTypeDef",
    "DescribeServicesRequestRequestTypeDef",
    "DescribeSeverityLevelsRequestRequestTypeDef",
    "SeverityLevelTypeDef",
    "DescribeSupportedLanguagesRequestRequestTypeDef",
    "SupportedLanguageTypeDef",
    "DescribeTrustedAdvisorCheckRefreshStatusesRequestRequestTypeDef",
    "TrustedAdvisorCheckRefreshStatusTypeDef",
    "DescribeTrustedAdvisorCheckResultRequestRequestTypeDef",
    "DescribeTrustedAdvisorCheckSummariesRequestRequestTypeDef",
    "DescribeTrustedAdvisorChecksRequestRequestTypeDef",
    "TrustedAdvisorCheckDescriptionTypeDef",
    "RefreshTrustedAdvisorCheckRequestRequestTypeDef",
    "ResolveCaseRequestRequestTypeDef",
    "TrustedAdvisorCostOptimizingSummaryTypeDef",
    "TrustedAdvisorResourceDetailTypeDef",
    "TrustedAdvisorResourcesSummaryTypeDef",
    "AddAttachmentsToSetResponseTypeDef",
    "AddCommunicationToCaseResponseTypeDef",
    "CreateCaseResponseTypeDef",
    "ResolveCaseResponseTypeDef",
    "CommunicationTypeDef",
    "DescribeAttachmentResponseTypeDef",
    "AttachmentTypeDef",
    "ServiceTypeDef",
    "CommunicationTypeOptionsTypeDef",
    "DescribeCasesRequestDescribeCasesPaginateTypeDef",
    "DescribeCommunicationsRequestDescribeCommunicationsPaginateTypeDef",
    "DescribeSeverityLevelsResponseTypeDef",
    "DescribeSupportedLanguagesResponseTypeDef",
    "DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef",
    "RefreshTrustedAdvisorCheckResponseTypeDef",
    "DescribeTrustedAdvisorChecksResponseTypeDef",
    "TrustedAdvisorCategorySpecificSummaryTypeDef",
    "DescribeCommunicationsResponseTypeDef",
    "RecentCaseCommunicationsTypeDef",
    "AttachmentUnionTypeDef",
    "DescribeServicesResponseTypeDef",
    "DescribeCreateCaseOptionsResponseTypeDef",
    "TrustedAdvisorCheckResultTypeDef",
    "TrustedAdvisorCheckSummaryTypeDef",
    "CaseDetailsTypeDef",
    "AddAttachmentsToSetRequestRequestTypeDef",
    "DescribeTrustedAdvisorCheckResultResponseTypeDef",
    "DescribeTrustedAdvisorCheckSummariesResponseTypeDef",
    "DescribeCasesResponseTypeDef",
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
AddCommunicationToCaseRequestRequestTypeDef = TypedDict(
    "AddCommunicationToCaseRequestRequestTypeDef",
    {
        "communicationBody": str,
        "caseId": NotRequired[str],
        "ccEmailAddresses": NotRequired[Sequence[str]],
        "attachmentSetId": NotRequired[str],
    },
)
AttachmentDetailsTypeDef = TypedDict(
    "AttachmentDetailsTypeDef",
    {
        "attachmentId": NotRequired[str],
        "fileName": NotRequired[str],
    },
)
AttachmentOutputTypeDef = TypedDict(
    "AttachmentOutputTypeDef",
    {
        "fileName": NotRequired[str],
        "data": NotRequired[bytes],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
CategoryTypeDef = TypedDict(
    "CategoryTypeDef",
    {
        "code": NotRequired[str],
        "name": NotRequired[str],
    },
)
DateIntervalTypeDef = TypedDict(
    "DateIntervalTypeDef",
    {
        "startDateTime": NotRequired[str],
        "endDateTime": NotRequired[str],
    },
)
SupportedHourTypeDef = TypedDict(
    "SupportedHourTypeDef",
    {
        "startTime": NotRequired[str],
        "endTime": NotRequired[str],
    },
)
CreateCaseRequestRequestTypeDef = TypedDict(
    "CreateCaseRequestRequestTypeDef",
    {
        "subject": str,
        "communicationBody": str,
        "serviceCode": NotRequired[str],
        "severityCode": NotRequired[str],
        "categoryCode": NotRequired[str],
        "ccEmailAddresses": NotRequired[Sequence[str]],
        "language": NotRequired[str],
        "issueType": NotRequired[str],
        "attachmentSetId": NotRequired[str],
    },
)
DescribeAttachmentRequestRequestTypeDef = TypedDict(
    "DescribeAttachmentRequestRequestTypeDef",
    {
        "attachmentId": str,
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
DescribeCasesRequestRequestTypeDef = TypedDict(
    "DescribeCasesRequestRequestTypeDef",
    {
        "caseIdList": NotRequired[Sequence[str]],
        "displayId": NotRequired[str],
        "afterTime": NotRequired[str],
        "beforeTime": NotRequired[str],
        "includeResolvedCases": NotRequired[bool],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "language": NotRequired[str],
        "includeCommunications": NotRequired[bool],
    },
)
DescribeCommunicationsRequestRequestTypeDef = TypedDict(
    "DescribeCommunicationsRequestRequestTypeDef",
    {
        "caseId": str,
        "beforeTime": NotRequired[str],
        "afterTime": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
DescribeCreateCaseOptionsRequestRequestTypeDef = TypedDict(
    "DescribeCreateCaseOptionsRequestRequestTypeDef",
    {
        "issueType": str,
        "serviceCode": str,
        "language": str,
        "categoryCode": str,
    },
)
DescribeServicesRequestRequestTypeDef = TypedDict(
    "DescribeServicesRequestRequestTypeDef",
    {
        "serviceCodeList": NotRequired[Sequence[str]],
        "language": NotRequired[str],
    },
)
DescribeSeverityLevelsRequestRequestTypeDef = TypedDict(
    "DescribeSeverityLevelsRequestRequestTypeDef",
    {
        "language": NotRequired[str],
    },
)
SeverityLevelTypeDef = TypedDict(
    "SeverityLevelTypeDef",
    {
        "code": NotRequired[str],
        "name": NotRequired[str],
    },
)
DescribeSupportedLanguagesRequestRequestTypeDef = TypedDict(
    "DescribeSupportedLanguagesRequestRequestTypeDef",
    {
        "issueType": str,
        "serviceCode": str,
        "categoryCode": str,
    },
)
SupportedLanguageTypeDef = TypedDict(
    "SupportedLanguageTypeDef",
    {
        "code": NotRequired[str],
        "language": NotRequired[str],
        "display": NotRequired[str],
    },
)
DescribeTrustedAdvisorCheckRefreshStatusesRequestRequestTypeDef = TypedDict(
    "DescribeTrustedAdvisorCheckRefreshStatusesRequestRequestTypeDef",
    {
        "checkIds": Sequence[str],
    },
)
TrustedAdvisorCheckRefreshStatusTypeDef = TypedDict(
    "TrustedAdvisorCheckRefreshStatusTypeDef",
    {
        "checkId": str,
        "status": str,
        "millisUntilNextRefreshable": int,
    },
)
DescribeTrustedAdvisorCheckResultRequestRequestTypeDef = TypedDict(
    "DescribeTrustedAdvisorCheckResultRequestRequestTypeDef",
    {
        "checkId": str,
        "language": NotRequired[str],
    },
)
DescribeTrustedAdvisorCheckSummariesRequestRequestTypeDef = TypedDict(
    "DescribeTrustedAdvisorCheckSummariesRequestRequestTypeDef",
    {
        "checkIds": Sequence[str],
    },
)
DescribeTrustedAdvisorChecksRequestRequestTypeDef = TypedDict(
    "DescribeTrustedAdvisorChecksRequestRequestTypeDef",
    {
        "language": str,
    },
)
TrustedAdvisorCheckDescriptionTypeDef = TypedDict(
    "TrustedAdvisorCheckDescriptionTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "category": str,
        "metadata": List[str],
    },
)
RefreshTrustedAdvisorCheckRequestRequestTypeDef = TypedDict(
    "RefreshTrustedAdvisorCheckRequestRequestTypeDef",
    {
        "checkId": str,
    },
)
ResolveCaseRequestRequestTypeDef = TypedDict(
    "ResolveCaseRequestRequestTypeDef",
    {
        "caseId": NotRequired[str],
    },
)
TrustedAdvisorCostOptimizingSummaryTypeDef = TypedDict(
    "TrustedAdvisorCostOptimizingSummaryTypeDef",
    {
        "estimatedMonthlySavings": float,
        "estimatedPercentMonthlySavings": float,
    },
)
TrustedAdvisorResourceDetailTypeDef = TypedDict(
    "TrustedAdvisorResourceDetailTypeDef",
    {
        "status": str,
        "resourceId": str,
        "metadata": List[str],
        "region": NotRequired[str],
        "isSuppressed": NotRequired[bool],
    },
)
TrustedAdvisorResourcesSummaryTypeDef = TypedDict(
    "TrustedAdvisorResourcesSummaryTypeDef",
    {
        "resourcesProcessed": int,
        "resourcesFlagged": int,
        "resourcesIgnored": int,
        "resourcesSuppressed": int,
    },
)
AddAttachmentsToSetResponseTypeDef = TypedDict(
    "AddAttachmentsToSetResponseTypeDef",
    {
        "attachmentSetId": str,
        "expiryTime": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AddCommunicationToCaseResponseTypeDef = TypedDict(
    "AddCommunicationToCaseResponseTypeDef",
    {
        "result": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCaseResponseTypeDef = TypedDict(
    "CreateCaseResponseTypeDef",
    {
        "caseId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResolveCaseResponseTypeDef = TypedDict(
    "ResolveCaseResponseTypeDef",
    {
        "initialCaseStatus": str,
        "finalCaseStatus": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CommunicationTypeDef = TypedDict(
    "CommunicationTypeDef",
    {
        "caseId": NotRequired[str],
        "body": NotRequired[str],
        "submittedBy": NotRequired[str],
        "timeCreated": NotRequired[str],
        "attachmentSet": NotRequired[List[AttachmentDetailsTypeDef]],
    },
)
DescribeAttachmentResponseTypeDef = TypedDict(
    "DescribeAttachmentResponseTypeDef",
    {
        "attachment": AttachmentOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AttachmentTypeDef = TypedDict(
    "AttachmentTypeDef",
    {
        "fileName": NotRequired[str],
        "data": NotRequired[BlobTypeDef],
    },
)
ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "code": NotRequired[str],
        "name": NotRequired[str],
        "categories": NotRequired[List[CategoryTypeDef]],
    },
)
CommunicationTypeOptionsTypeDef = TypedDict(
    "CommunicationTypeOptionsTypeDef",
    {
        "type": NotRequired[str],
        "supportedHours": NotRequired[List[SupportedHourTypeDef]],
        "datesWithoutSupport": NotRequired[List[DateIntervalTypeDef]],
    },
)
DescribeCasesRequestDescribeCasesPaginateTypeDef = TypedDict(
    "DescribeCasesRequestDescribeCasesPaginateTypeDef",
    {
        "caseIdList": NotRequired[Sequence[str]],
        "displayId": NotRequired[str],
        "afterTime": NotRequired[str],
        "beforeTime": NotRequired[str],
        "includeResolvedCases": NotRequired[bool],
        "language": NotRequired[str],
        "includeCommunications": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeCommunicationsRequestDescribeCommunicationsPaginateTypeDef = TypedDict(
    "DescribeCommunicationsRequestDescribeCommunicationsPaginateTypeDef",
    {
        "caseId": str,
        "beforeTime": NotRequired[str],
        "afterTime": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeSeverityLevelsResponseTypeDef = TypedDict(
    "DescribeSeverityLevelsResponseTypeDef",
    {
        "severityLevels": List[SeverityLevelTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSupportedLanguagesResponseTypeDef = TypedDict(
    "DescribeSupportedLanguagesResponseTypeDef",
    {
        "supportedLanguages": List[SupportedLanguageTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef = TypedDict(
    "DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef",
    {
        "statuses": List[TrustedAdvisorCheckRefreshStatusTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RefreshTrustedAdvisorCheckResponseTypeDef = TypedDict(
    "RefreshTrustedAdvisorCheckResponseTypeDef",
    {
        "status": TrustedAdvisorCheckRefreshStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTrustedAdvisorChecksResponseTypeDef = TypedDict(
    "DescribeTrustedAdvisorChecksResponseTypeDef",
    {
        "checks": List[TrustedAdvisorCheckDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TrustedAdvisorCategorySpecificSummaryTypeDef = TypedDict(
    "TrustedAdvisorCategorySpecificSummaryTypeDef",
    {
        "costOptimizing": NotRequired[TrustedAdvisorCostOptimizingSummaryTypeDef],
    },
)
DescribeCommunicationsResponseTypeDef = TypedDict(
    "DescribeCommunicationsResponseTypeDef",
    {
        "communications": List[CommunicationTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RecentCaseCommunicationsTypeDef = TypedDict(
    "RecentCaseCommunicationsTypeDef",
    {
        "communications": NotRequired[List[CommunicationTypeDef]],
        "nextToken": NotRequired[str],
    },
)
AttachmentUnionTypeDef = Union[AttachmentTypeDef, AttachmentOutputTypeDef]
DescribeServicesResponseTypeDef = TypedDict(
    "DescribeServicesResponseTypeDef",
    {
        "services": List[ServiceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeCreateCaseOptionsResponseTypeDef = TypedDict(
    "DescribeCreateCaseOptionsResponseTypeDef",
    {
        "languageAvailability": str,
        "communicationTypes": List[CommunicationTypeOptionsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TrustedAdvisorCheckResultTypeDef = TypedDict(
    "TrustedAdvisorCheckResultTypeDef",
    {
        "checkId": str,
        "timestamp": str,
        "status": str,
        "resourcesSummary": TrustedAdvisorResourcesSummaryTypeDef,
        "categorySpecificSummary": TrustedAdvisorCategorySpecificSummaryTypeDef,
        "flaggedResources": List[TrustedAdvisorResourceDetailTypeDef],
    },
)
TrustedAdvisorCheckSummaryTypeDef = TypedDict(
    "TrustedAdvisorCheckSummaryTypeDef",
    {
        "checkId": str,
        "timestamp": str,
        "status": str,
        "resourcesSummary": TrustedAdvisorResourcesSummaryTypeDef,
        "categorySpecificSummary": TrustedAdvisorCategorySpecificSummaryTypeDef,
        "hasFlaggedResources": NotRequired[bool],
    },
)
CaseDetailsTypeDef = TypedDict(
    "CaseDetailsTypeDef",
    {
        "caseId": NotRequired[str],
        "displayId": NotRequired[str],
        "subject": NotRequired[str],
        "status": NotRequired[str],
        "serviceCode": NotRequired[str],
        "categoryCode": NotRequired[str],
        "severityCode": NotRequired[str],
        "submittedBy": NotRequired[str],
        "timeCreated": NotRequired[str],
        "recentCommunications": NotRequired[RecentCaseCommunicationsTypeDef],
        "ccEmailAddresses": NotRequired[List[str]],
        "language": NotRequired[str],
    },
)
AddAttachmentsToSetRequestRequestTypeDef = TypedDict(
    "AddAttachmentsToSetRequestRequestTypeDef",
    {
        "attachments": Sequence[AttachmentUnionTypeDef],
        "attachmentSetId": NotRequired[str],
    },
)
DescribeTrustedAdvisorCheckResultResponseTypeDef = TypedDict(
    "DescribeTrustedAdvisorCheckResultResponseTypeDef",
    {
        "result": TrustedAdvisorCheckResultTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTrustedAdvisorCheckSummariesResponseTypeDef = TypedDict(
    "DescribeTrustedAdvisorCheckSummariesResponseTypeDef",
    {
        "summaries": List[TrustedAdvisorCheckSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeCasesResponseTypeDef = TypedDict(
    "DescribeCasesResponseTypeDef",
    {
        "cases": List[CaseDetailsTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
