"""
Type annotations for auditmanager service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/type_defs/)

Usage::

    ```python
    from mypy_boto3_auditmanager.type_defs import AWSAccountTypeDef

    data: AWSAccountTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AccountStatusType,
    ActionEnumType,
    AssessmentReportStatusType,
    AssessmentStatusType,
    ControlResponseType,
    ControlSetStatusType,
    ControlStateType,
    ControlStatusType,
    ControlTypeType,
    DataSourceTypeType,
    DelegationStatusType,
    DeleteResourcesType,
    EvidenceFinderBackfillStatusType,
    EvidenceFinderEnablementStatusType,
    FrameworkTypeType,
    KeywordInputTypeType,
    ObjectTypeEnumType,
    RoleTypeType,
    SettingAttributeType,
    ShareRequestActionType,
    ShareRequestStatusType,
    ShareRequestTypeType,
    SourceFrequencyType,
    SourceSetUpOptionType,
    SourceTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AWSAccountTypeDef",
    "AWSServiceTypeDef",
    "DelegationTypeDef",
    "RoleTypeDef",
    "ControlCommentTypeDef",
    "AssessmentEvidenceFolderTypeDef",
    "AssessmentFrameworkMetadataTypeDef",
    "AssessmentFrameworkShareRequestTypeDef",
    "FrameworkMetadataTypeDef",
    "AssessmentReportsDestinationTypeDef",
    "AssessmentReportEvidenceErrorTypeDef",
    "AssessmentReportMetadataTypeDef",
    "AssessmentReportTypeDef",
    "AssociateAssessmentReportEvidenceFolderRequestRequestTypeDef",
    "BatchAssociateAssessmentReportEvidenceRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CreateDelegationRequestTypeDef",
    "BatchDeleteDelegationByAssessmentErrorTypeDef",
    "BatchDeleteDelegationByAssessmentRequestRequestTypeDef",
    "BatchDisassociateAssessmentReportEvidenceRequestRequestTypeDef",
    "ManualEvidenceTypeDef",
    "ChangeLogTypeDef",
    "EvidenceInsightsTypeDef",
    "SourceKeywordTypeDef",
    "ControlMetadataTypeDef",
    "CreateAssessmentFrameworkControlTypeDef",
    "CreateAssessmentReportRequestRequestTypeDef",
    "DefaultExportDestinationTypeDef",
    "DelegationMetadataTypeDef",
    "DeleteAssessmentFrameworkRequestRequestTypeDef",
    "DeleteAssessmentFrameworkShareRequestRequestTypeDef",
    "DeleteAssessmentReportRequestRequestTypeDef",
    "DeleteAssessmentRequestRequestTypeDef",
    "DeleteControlRequestRequestTypeDef",
    "DeregisterOrganizationAdminAccountRequestRequestTypeDef",
    "DeregistrationPolicyTypeDef",
    "DisassociateAssessmentReportEvidenceFolderRequestRequestTypeDef",
    "EvidenceFinderEnablementTypeDef",
    "ResourceTypeDef",
    "GetAssessmentFrameworkRequestRequestTypeDef",
    "GetAssessmentReportUrlRequestRequestTypeDef",
    "URLTypeDef",
    "GetAssessmentRequestRequestTypeDef",
    "GetChangeLogsRequestRequestTypeDef",
    "GetControlRequestRequestTypeDef",
    "GetDelegationsRequestRequestTypeDef",
    "GetEvidenceByEvidenceFolderRequestRequestTypeDef",
    "GetEvidenceFileUploadUrlRequestRequestTypeDef",
    "GetEvidenceFolderRequestRequestTypeDef",
    "GetEvidenceFoldersByAssessmentControlRequestRequestTypeDef",
    "GetEvidenceFoldersByAssessmentRequestRequestTypeDef",
    "GetEvidenceRequestRequestTypeDef",
    "GetInsightsByAssessmentRequestRequestTypeDef",
    "InsightsByAssessmentTypeDef",
    "InsightsTypeDef",
    "ServiceMetadataTypeDef",
    "GetSettingsRequestRequestTypeDef",
    "ListAssessmentControlInsightsByControlDomainRequestRequestTypeDef",
    "ListAssessmentFrameworkShareRequestsRequestRequestTypeDef",
    "ListAssessmentFrameworksRequestRequestTypeDef",
    "ListAssessmentReportsRequestRequestTypeDef",
    "ListAssessmentsRequestRequestTypeDef",
    "ListControlDomainInsightsByAssessmentRequestRequestTypeDef",
    "ListControlDomainInsightsRequestRequestTypeDef",
    "ListControlInsightsByControlDomainRequestRequestTypeDef",
    "ListControlsRequestRequestTypeDef",
    "ListKeywordsForDataSourceRequestRequestTypeDef",
    "ListNotificationsRequestRequestTypeDef",
    "NotificationTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "RegisterAccountRequestRequestTypeDef",
    "RegisterOrganizationAdminAccountRequestRequestTypeDef",
    "StartAssessmentFrameworkShareRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAssessmentControlRequestRequestTypeDef",
    "UpdateAssessmentControlSetStatusRequestRequestTypeDef",
    "UpdateAssessmentFrameworkShareRequestRequestTypeDef",
    "UpdateAssessmentStatusRequestRequestTypeDef",
    "ValidateAssessmentReportIntegrityRequestRequestTypeDef",
    "ScopeOutputTypeDef",
    "ScopeTypeDef",
    "AssessmentMetadataItemTypeDef",
    "AssessmentControlTypeDef",
    "BatchAssociateAssessmentReportEvidenceResponseTypeDef",
    "BatchDisassociateAssessmentReportEvidenceResponseTypeDef",
    "CreateAssessmentReportResponseTypeDef",
    "DeregisterAccountResponseTypeDef",
    "GetAccountStatusResponseTypeDef",
    "GetEvidenceFileUploadUrlResponseTypeDef",
    "GetEvidenceFolderResponseTypeDef",
    "GetEvidenceFoldersByAssessmentControlResponseTypeDef",
    "GetEvidenceFoldersByAssessmentResponseTypeDef",
    "GetOrganizationAdminAccountResponseTypeDef",
    "ListAssessmentFrameworkShareRequestsResponseTypeDef",
    "ListAssessmentFrameworksResponseTypeDef",
    "ListAssessmentReportsResponseTypeDef",
    "ListKeywordsForDataSourceResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "RegisterAccountResponseTypeDef",
    "RegisterOrganizationAdminAccountResponseTypeDef",
    "StartAssessmentFrameworkShareResponseTypeDef",
    "UpdateAssessmentFrameworkShareResponseTypeDef",
    "ValidateAssessmentReportIntegrityResponseTypeDef",
    "BatchCreateDelegationByAssessmentErrorTypeDef",
    "BatchCreateDelegationByAssessmentRequestRequestTypeDef",
    "BatchDeleteDelegationByAssessmentResponseTypeDef",
    "BatchImportEvidenceToAssessmentControlErrorTypeDef",
    "BatchImportEvidenceToAssessmentControlRequestRequestTypeDef",
    "GetChangeLogsResponseTypeDef",
    "ControlDomainInsightsTypeDef",
    "ControlInsightsMetadataByAssessmentItemTypeDef",
    "ControlInsightsMetadataItemTypeDef",
    "ControlMappingSourceTypeDef",
    "CreateControlMappingSourceTypeDef",
    "ListControlsResponseTypeDef",
    "CreateAssessmentFrameworkControlSetTypeDef",
    "UpdateAssessmentFrameworkControlSetTypeDef",
    "GetDelegationsResponseTypeDef",
    "UpdateSettingsRequestRequestTypeDef",
    "SettingsTypeDef",
    "EvidenceTypeDef",
    "GetAssessmentReportUrlResponseTypeDef",
    "GetInsightsByAssessmentResponseTypeDef",
    "GetInsightsResponseTypeDef",
    "GetServicesInScopeResponseTypeDef",
    "ListNotificationsResponseTypeDef",
    "AssessmentMetadataTypeDef",
    "CreateAssessmentRequestRequestTypeDef",
    "UpdateAssessmentRequestRequestTypeDef",
    "ListAssessmentsResponseTypeDef",
    "AssessmentControlSetTypeDef",
    "UpdateAssessmentControlResponseTypeDef",
    "BatchCreateDelegationByAssessmentResponseTypeDef",
    "BatchImportEvidenceToAssessmentControlResponseTypeDef",
    "ListControlDomainInsightsByAssessmentResponseTypeDef",
    "ListControlDomainInsightsResponseTypeDef",
    "ListAssessmentControlInsightsByControlDomainResponseTypeDef",
    "ListControlInsightsByControlDomainResponseTypeDef",
    "ControlTypeDef",
    "UpdateControlRequestRequestTypeDef",
    "CreateControlRequestRequestTypeDef",
    "CreateAssessmentFrameworkRequestRequestTypeDef",
    "UpdateAssessmentFrameworkRequestRequestTypeDef",
    "GetSettingsResponseTypeDef",
    "UpdateSettingsResponseTypeDef",
    "GetEvidenceByEvidenceFolderResponseTypeDef",
    "GetEvidenceResponseTypeDef",
    "AssessmentFrameworkTypeDef",
    "UpdateAssessmentControlSetStatusResponseTypeDef",
    "ControlSetTypeDef",
    "CreateControlResponseTypeDef",
    "GetControlResponseTypeDef",
    "UpdateControlResponseTypeDef",
    "AssessmentTypeDef",
    "FrameworkTypeDef",
    "CreateAssessmentResponseTypeDef",
    "GetAssessmentResponseTypeDef",
    "UpdateAssessmentResponseTypeDef",
    "UpdateAssessmentStatusResponseTypeDef",
    "CreateAssessmentFrameworkResponseTypeDef",
    "GetAssessmentFrameworkResponseTypeDef",
    "UpdateAssessmentFrameworkResponseTypeDef",
)

AWSAccountTypeDef = TypedDict(
    "AWSAccountTypeDef",
    {
        "id": NotRequired[str],
        "emailAddress": NotRequired[str],
        "name": NotRequired[str],
    },
)
AWSServiceTypeDef = TypedDict(
    "AWSServiceTypeDef",
    {
        "serviceName": NotRequired[str],
    },
)
DelegationTypeDef = TypedDict(
    "DelegationTypeDef",
    {
        "id": NotRequired[str],
        "assessmentName": NotRequired[str],
        "assessmentId": NotRequired[str],
        "status": NotRequired[DelegationStatusType],
        "roleArn": NotRequired[str],
        "roleType": NotRequired[RoleTypeType],
        "creationTime": NotRequired[datetime],
        "lastUpdated": NotRequired[datetime],
        "controlSetId": NotRequired[str],
        "comment": NotRequired[str],
        "createdBy": NotRequired[str],
    },
)
RoleTypeDef = TypedDict(
    "RoleTypeDef",
    {
        "roleType": RoleTypeType,
        "roleArn": str,
    },
)
ControlCommentTypeDef = TypedDict(
    "ControlCommentTypeDef",
    {
        "authorName": NotRequired[str],
        "commentBody": NotRequired[str],
        "postedDate": NotRequired[datetime],
    },
)
AssessmentEvidenceFolderTypeDef = TypedDict(
    "AssessmentEvidenceFolderTypeDef",
    {
        "name": NotRequired[str],
        "date": NotRequired[datetime],
        "assessmentId": NotRequired[str],
        "controlSetId": NotRequired[str],
        "controlId": NotRequired[str],
        "id": NotRequired[str],
        "dataSource": NotRequired[str],
        "author": NotRequired[str],
        "totalEvidence": NotRequired[int],
        "assessmentReportSelectionCount": NotRequired[int],
        "controlName": NotRequired[str],
        "evidenceResourcesIncludedCount": NotRequired[int],
        "evidenceByTypeConfigurationDataCount": NotRequired[int],
        "evidenceByTypeManualCount": NotRequired[int],
        "evidenceByTypeComplianceCheckCount": NotRequired[int],
        "evidenceByTypeComplianceCheckIssuesCount": NotRequired[int],
        "evidenceByTypeUserActivityCount": NotRequired[int],
        "evidenceAwsServiceSourceCount": NotRequired[int],
    },
)
AssessmentFrameworkMetadataTypeDef = TypedDict(
    "AssessmentFrameworkMetadataTypeDef",
    {
        "arn": NotRequired[str],
        "id": NotRequired[str],
        "type": NotRequired[FrameworkTypeType],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "logo": NotRequired[str],
        "complianceType": NotRequired[str],
        "controlsCount": NotRequired[int],
        "controlSetsCount": NotRequired[int],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
    },
)
AssessmentFrameworkShareRequestTypeDef = TypedDict(
    "AssessmentFrameworkShareRequestTypeDef",
    {
        "id": NotRequired[str],
        "frameworkId": NotRequired[str],
        "frameworkName": NotRequired[str],
        "frameworkDescription": NotRequired[str],
        "status": NotRequired[ShareRequestStatusType],
        "sourceAccount": NotRequired[str],
        "destinationAccount": NotRequired[str],
        "destinationRegion": NotRequired[str],
        "expirationTime": NotRequired[datetime],
        "creationTime": NotRequired[datetime],
        "lastUpdated": NotRequired[datetime],
        "comment": NotRequired[str],
        "standardControlsCount": NotRequired[int],
        "customControlsCount": NotRequired[int],
        "complianceType": NotRequired[str],
    },
)
FrameworkMetadataTypeDef = TypedDict(
    "FrameworkMetadataTypeDef",
    {
        "name": NotRequired[str],
        "description": NotRequired[str],
        "logo": NotRequired[str],
        "complianceType": NotRequired[str],
    },
)
AssessmentReportsDestinationTypeDef = TypedDict(
    "AssessmentReportsDestinationTypeDef",
    {
        "destinationType": NotRequired[Literal["S3"]],
        "destination": NotRequired[str],
    },
)
AssessmentReportEvidenceErrorTypeDef = TypedDict(
    "AssessmentReportEvidenceErrorTypeDef",
    {
        "evidenceId": NotRequired[str],
        "errorCode": NotRequired[str],
        "errorMessage": NotRequired[str],
    },
)
AssessmentReportMetadataTypeDef = TypedDict(
    "AssessmentReportMetadataTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "assessmentId": NotRequired[str],
        "assessmentName": NotRequired[str],
        "author": NotRequired[str],
        "status": NotRequired[AssessmentReportStatusType],
        "creationTime": NotRequired[datetime],
    },
)
AssessmentReportTypeDef = TypedDict(
    "AssessmentReportTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "awsAccountId": NotRequired[str],
        "assessmentId": NotRequired[str],
        "assessmentName": NotRequired[str],
        "author": NotRequired[str],
        "status": NotRequired[AssessmentReportStatusType],
        "creationTime": NotRequired[datetime],
    },
)
AssociateAssessmentReportEvidenceFolderRequestRequestTypeDef = TypedDict(
    "AssociateAssessmentReportEvidenceFolderRequestRequestTypeDef",
    {
        "assessmentId": str,
        "evidenceFolderId": str,
    },
)
BatchAssociateAssessmentReportEvidenceRequestRequestTypeDef = TypedDict(
    "BatchAssociateAssessmentReportEvidenceRequestRequestTypeDef",
    {
        "assessmentId": str,
        "evidenceFolderId": str,
        "evidenceIds": Sequence[str],
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
CreateDelegationRequestTypeDef = TypedDict(
    "CreateDelegationRequestTypeDef",
    {
        "comment": NotRequired[str],
        "controlSetId": NotRequired[str],
        "roleArn": NotRequired[str],
        "roleType": NotRequired[RoleTypeType],
    },
)
BatchDeleteDelegationByAssessmentErrorTypeDef = TypedDict(
    "BatchDeleteDelegationByAssessmentErrorTypeDef",
    {
        "delegationId": NotRequired[str],
        "errorCode": NotRequired[str],
        "errorMessage": NotRequired[str],
    },
)
BatchDeleteDelegationByAssessmentRequestRequestTypeDef = TypedDict(
    "BatchDeleteDelegationByAssessmentRequestRequestTypeDef",
    {
        "delegationIds": Sequence[str],
        "assessmentId": str,
    },
)
BatchDisassociateAssessmentReportEvidenceRequestRequestTypeDef = TypedDict(
    "BatchDisassociateAssessmentReportEvidenceRequestRequestTypeDef",
    {
        "assessmentId": str,
        "evidenceFolderId": str,
        "evidenceIds": Sequence[str],
    },
)
ManualEvidenceTypeDef = TypedDict(
    "ManualEvidenceTypeDef",
    {
        "s3ResourcePath": NotRequired[str],
        "textResponse": NotRequired[str],
        "evidenceFileName": NotRequired[str],
    },
)
ChangeLogTypeDef = TypedDict(
    "ChangeLogTypeDef",
    {
        "objectType": NotRequired[ObjectTypeEnumType],
        "objectName": NotRequired[str],
        "action": NotRequired[ActionEnumType],
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
    },
)
EvidenceInsightsTypeDef = TypedDict(
    "EvidenceInsightsTypeDef",
    {
        "noncompliantEvidenceCount": NotRequired[int],
        "compliantEvidenceCount": NotRequired[int],
        "inconclusiveEvidenceCount": NotRequired[int],
    },
)
SourceKeywordTypeDef = TypedDict(
    "SourceKeywordTypeDef",
    {
        "keywordInputType": NotRequired[KeywordInputTypeType],
        "keywordValue": NotRequired[str],
    },
)
ControlMetadataTypeDef = TypedDict(
    "ControlMetadataTypeDef",
    {
        "arn": NotRequired[str],
        "id": NotRequired[str],
        "name": NotRequired[str],
        "controlSources": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
    },
)
CreateAssessmentFrameworkControlTypeDef = TypedDict(
    "CreateAssessmentFrameworkControlTypeDef",
    {
        "id": str,
    },
)
CreateAssessmentReportRequestRequestTypeDef = TypedDict(
    "CreateAssessmentReportRequestRequestTypeDef",
    {
        "name": str,
        "assessmentId": str,
        "description": NotRequired[str],
        "queryStatement": NotRequired[str],
    },
)
DefaultExportDestinationTypeDef = TypedDict(
    "DefaultExportDestinationTypeDef",
    {
        "destinationType": NotRequired[Literal["S3"]],
        "destination": NotRequired[str],
    },
)
DelegationMetadataTypeDef = TypedDict(
    "DelegationMetadataTypeDef",
    {
        "id": NotRequired[str],
        "assessmentName": NotRequired[str],
        "assessmentId": NotRequired[str],
        "status": NotRequired[DelegationStatusType],
        "roleArn": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "controlSetName": NotRequired[str],
    },
)
DeleteAssessmentFrameworkRequestRequestTypeDef = TypedDict(
    "DeleteAssessmentFrameworkRequestRequestTypeDef",
    {
        "frameworkId": str,
    },
)
DeleteAssessmentFrameworkShareRequestRequestTypeDef = TypedDict(
    "DeleteAssessmentFrameworkShareRequestRequestTypeDef",
    {
        "requestId": str,
        "requestType": ShareRequestTypeType,
    },
)
DeleteAssessmentReportRequestRequestTypeDef = TypedDict(
    "DeleteAssessmentReportRequestRequestTypeDef",
    {
        "assessmentId": str,
        "assessmentReportId": str,
    },
)
DeleteAssessmentRequestRequestTypeDef = TypedDict(
    "DeleteAssessmentRequestRequestTypeDef",
    {
        "assessmentId": str,
    },
)
DeleteControlRequestRequestTypeDef = TypedDict(
    "DeleteControlRequestRequestTypeDef",
    {
        "controlId": str,
    },
)
DeregisterOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "DeregisterOrganizationAdminAccountRequestRequestTypeDef",
    {
        "adminAccountId": NotRequired[str],
    },
)
DeregistrationPolicyTypeDef = TypedDict(
    "DeregistrationPolicyTypeDef",
    {
        "deleteResources": NotRequired[DeleteResourcesType],
    },
)
DisassociateAssessmentReportEvidenceFolderRequestRequestTypeDef = TypedDict(
    "DisassociateAssessmentReportEvidenceFolderRequestRequestTypeDef",
    {
        "assessmentId": str,
        "evidenceFolderId": str,
    },
)
EvidenceFinderEnablementTypeDef = TypedDict(
    "EvidenceFinderEnablementTypeDef",
    {
        "eventDataStoreArn": NotRequired[str],
        "enablementStatus": NotRequired[EvidenceFinderEnablementStatusType],
        "backfillStatus": NotRequired[EvidenceFinderBackfillStatusType],
        "error": NotRequired[str],
    },
)
ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "arn": NotRequired[str],
        "value": NotRequired[str],
        "complianceCheck": NotRequired[str],
    },
)
GetAssessmentFrameworkRequestRequestTypeDef = TypedDict(
    "GetAssessmentFrameworkRequestRequestTypeDef",
    {
        "frameworkId": str,
    },
)
GetAssessmentReportUrlRequestRequestTypeDef = TypedDict(
    "GetAssessmentReportUrlRequestRequestTypeDef",
    {
        "assessmentReportId": str,
        "assessmentId": str,
    },
)
URLTypeDef = TypedDict(
    "URLTypeDef",
    {
        "hyperlinkName": NotRequired[str],
        "link": NotRequired[str],
    },
)
GetAssessmentRequestRequestTypeDef = TypedDict(
    "GetAssessmentRequestRequestTypeDef",
    {
        "assessmentId": str,
    },
)
GetChangeLogsRequestRequestTypeDef = TypedDict(
    "GetChangeLogsRequestRequestTypeDef",
    {
        "assessmentId": str,
        "controlSetId": NotRequired[str],
        "controlId": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
GetControlRequestRequestTypeDef = TypedDict(
    "GetControlRequestRequestTypeDef",
    {
        "controlId": str,
    },
)
GetDelegationsRequestRequestTypeDef = TypedDict(
    "GetDelegationsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
GetEvidenceByEvidenceFolderRequestRequestTypeDef = TypedDict(
    "GetEvidenceByEvidenceFolderRequestRequestTypeDef",
    {
        "assessmentId": str,
        "controlSetId": str,
        "evidenceFolderId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
GetEvidenceFileUploadUrlRequestRequestTypeDef = TypedDict(
    "GetEvidenceFileUploadUrlRequestRequestTypeDef",
    {
        "fileName": str,
    },
)
GetEvidenceFolderRequestRequestTypeDef = TypedDict(
    "GetEvidenceFolderRequestRequestTypeDef",
    {
        "assessmentId": str,
        "controlSetId": str,
        "evidenceFolderId": str,
    },
)
GetEvidenceFoldersByAssessmentControlRequestRequestTypeDef = TypedDict(
    "GetEvidenceFoldersByAssessmentControlRequestRequestTypeDef",
    {
        "assessmentId": str,
        "controlSetId": str,
        "controlId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
GetEvidenceFoldersByAssessmentRequestRequestTypeDef = TypedDict(
    "GetEvidenceFoldersByAssessmentRequestRequestTypeDef",
    {
        "assessmentId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
GetEvidenceRequestRequestTypeDef = TypedDict(
    "GetEvidenceRequestRequestTypeDef",
    {
        "assessmentId": str,
        "controlSetId": str,
        "evidenceFolderId": str,
        "evidenceId": str,
    },
)
GetInsightsByAssessmentRequestRequestTypeDef = TypedDict(
    "GetInsightsByAssessmentRequestRequestTypeDef",
    {
        "assessmentId": str,
    },
)
InsightsByAssessmentTypeDef = TypedDict(
    "InsightsByAssessmentTypeDef",
    {
        "noncompliantEvidenceCount": NotRequired[int],
        "compliantEvidenceCount": NotRequired[int],
        "inconclusiveEvidenceCount": NotRequired[int],
        "assessmentControlsCountByNoncompliantEvidence": NotRequired[int],
        "totalAssessmentControlsCount": NotRequired[int],
        "lastUpdated": NotRequired[datetime],
    },
)
InsightsTypeDef = TypedDict(
    "InsightsTypeDef",
    {
        "activeAssessmentsCount": NotRequired[int],
        "noncompliantEvidenceCount": NotRequired[int],
        "compliantEvidenceCount": NotRequired[int],
        "inconclusiveEvidenceCount": NotRequired[int],
        "assessmentControlsCountByNoncompliantEvidence": NotRequired[int],
        "totalAssessmentControlsCount": NotRequired[int],
        "lastUpdated": NotRequired[datetime],
    },
)
ServiceMetadataTypeDef = TypedDict(
    "ServiceMetadataTypeDef",
    {
        "name": NotRequired[str],
        "displayName": NotRequired[str],
        "description": NotRequired[str],
        "category": NotRequired[str],
    },
)
GetSettingsRequestRequestTypeDef = TypedDict(
    "GetSettingsRequestRequestTypeDef",
    {
        "attribute": SettingAttributeType,
    },
)
ListAssessmentControlInsightsByControlDomainRequestRequestTypeDef = TypedDict(
    "ListAssessmentControlInsightsByControlDomainRequestRequestTypeDef",
    {
        "controlDomainId": str,
        "assessmentId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListAssessmentFrameworkShareRequestsRequestRequestTypeDef = TypedDict(
    "ListAssessmentFrameworkShareRequestsRequestRequestTypeDef",
    {
        "requestType": ShareRequestTypeType,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListAssessmentFrameworksRequestRequestTypeDef = TypedDict(
    "ListAssessmentFrameworksRequestRequestTypeDef",
    {
        "frameworkType": FrameworkTypeType,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListAssessmentReportsRequestRequestTypeDef = TypedDict(
    "ListAssessmentReportsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListAssessmentsRequestRequestTypeDef = TypedDict(
    "ListAssessmentsRequestRequestTypeDef",
    {
        "status": NotRequired[AssessmentStatusType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListControlDomainInsightsByAssessmentRequestRequestTypeDef = TypedDict(
    "ListControlDomainInsightsByAssessmentRequestRequestTypeDef",
    {
        "assessmentId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListControlDomainInsightsRequestRequestTypeDef = TypedDict(
    "ListControlDomainInsightsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListControlInsightsByControlDomainRequestRequestTypeDef = TypedDict(
    "ListControlInsightsByControlDomainRequestRequestTypeDef",
    {
        "controlDomainId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListControlsRequestRequestTypeDef = TypedDict(
    "ListControlsRequestRequestTypeDef",
    {
        "controlType": ControlTypeType,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "controlCatalogId": NotRequired[str],
    },
)
ListKeywordsForDataSourceRequestRequestTypeDef = TypedDict(
    "ListKeywordsForDataSourceRequestRequestTypeDef",
    {
        "source": DataSourceTypeType,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListNotificationsRequestRequestTypeDef = TypedDict(
    "ListNotificationsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
NotificationTypeDef = TypedDict(
    "NotificationTypeDef",
    {
        "id": NotRequired[str],
        "assessmentId": NotRequired[str],
        "assessmentName": NotRequired[str],
        "controlSetId": NotRequired[str],
        "controlSetName": NotRequired[str],
        "description": NotRequired[str],
        "eventTime": NotRequired[datetime],
        "source": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
RegisterAccountRequestRequestTypeDef = TypedDict(
    "RegisterAccountRequestRequestTypeDef",
    {
        "kmsKey": NotRequired[str],
        "delegatedAdminAccount": NotRequired[str],
    },
)
RegisterOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "RegisterOrganizationAdminAccountRequestRequestTypeDef",
    {
        "adminAccountId": str,
    },
)
StartAssessmentFrameworkShareRequestRequestTypeDef = TypedDict(
    "StartAssessmentFrameworkShareRequestRequestTypeDef",
    {
        "frameworkId": str,
        "destinationAccount": str,
        "destinationRegion": str,
        "comment": NotRequired[str],
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
UpdateAssessmentControlRequestRequestTypeDef = TypedDict(
    "UpdateAssessmentControlRequestRequestTypeDef",
    {
        "assessmentId": str,
        "controlSetId": str,
        "controlId": str,
        "controlStatus": NotRequired[ControlStatusType],
        "commentBody": NotRequired[str],
    },
)
UpdateAssessmentControlSetStatusRequestRequestTypeDef = TypedDict(
    "UpdateAssessmentControlSetStatusRequestRequestTypeDef",
    {
        "assessmentId": str,
        "controlSetId": str,
        "status": ControlSetStatusType,
        "comment": str,
    },
)
UpdateAssessmentFrameworkShareRequestRequestTypeDef = TypedDict(
    "UpdateAssessmentFrameworkShareRequestRequestTypeDef",
    {
        "requestId": str,
        "requestType": ShareRequestTypeType,
        "action": ShareRequestActionType,
    },
)
UpdateAssessmentStatusRequestRequestTypeDef = TypedDict(
    "UpdateAssessmentStatusRequestRequestTypeDef",
    {
        "assessmentId": str,
        "status": AssessmentStatusType,
    },
)
ValidateAssessmentReportIntegrityRequestRequestTypeDef = TypedDict(
    "ValidateAssessmentReportIntegrityRequestRequestTypeDef",
    {
        "s3RelativePath": str,
    },
)
ScopeOutputTypeDef = TypedDict(
    "ScopeOutputTypeDef",
    {
        "awsAccounts": NotRequired[List[AWSAccountTypeDef]],
        "awsServices": NotRequired[List[AWSServiceTypeDef]],
    },
)
ScopeTypeDef = TypedDict(
    "ScopeTypeDef",
    {
        "awsAccounts": NotRequired[Sequence[AWSAccountTypeDef]],
        "awsServices": NotRequired[Sequence[AWSServiceTypeDef]],
    },
)
AssessmentMetadataItemTypeDef = TypedDict(
    "AssessmentMetadataItemTypeDef",
    {
        "name": NotRequired[str],
        "id": NotRequired[str],
        "complianceType": NotRequired[str],
        "status": NotRequired[AssessmentStatusType],
        "roles": NotRequired[List[RoleTypeDef]],
        "delegations": NotRequired[List[DelegationTypeDef]],
        "creationTime": NotRequired[datetime],
        "lastUpdated": NotRequired[datetime],
    },
)
AssessmentControlTypeDef = TypedDict(
    "AssessmentControlTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "status": NotRequired[ControlStatusType],
        "response": NotRequired[ControlResponseType],
        "comments": NotRequired[List[ControlCommentTypeDef]],
        "evidenceSources": NotRequired[List[str]],
        "evidenceCount": NotRequired[int],
        "assessmentReportEvidenceCount": NotRequired[int],
    },
)
BatchAssociateAssessmentReportEvidenceResponseTypeDef = TypedDict(
    "BatchAssociateAssessmentReportEvidenceResponseTypeDef",
    {
        "evidenceIds": List[str],
        "errors": List[AssessmentReportEvidenceErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDisassociateAssessmentReportEvidenceResponseTypeDef = TypedDict(
    "BatchDisassociateAssessmentReportEvidenceResponseTypeDef",
    {
        "evidenceIds": List[str],
        "errors": List[AssessmentReportEvidenceErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAssessmentReportResponseTypeDef = TypedDict(
    "CreateAssessmentReportResponseTypeDef",
    {
        "assessmentReport": AssessmentReportTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeregisterAccountResponseTypeDef = TypedDict(
    "DeregisterAccountResponseTypeDef",
    {
        "status": AccountStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAccountStatusResponseTypeDef = TypedDict(
    "GetAccountStatusResponseTypeDef",
    {
        "status": AccountStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEvidenceFileUploadUrlResponseTypeDef = TypedDict(
    "GetEvidenceFileUploadUrlResponseTypeDef",
    {
        "evidenceFileName": str,
        "uploadUrl": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEvidenceFolderResponseTypeDef = TypedDict(
    "GetEvidenceFolderResponseTypeDef",
    {
        "evidenceFolder": AssessmentEvidenceFolderTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEvidenceFoldersByAssessmentControlResponseTypeDef = TypedDict(
    "GetEvidenceFoldersByAssessmentControlResponseTypeDef",
    {
        "evidenceFolders": List[AssessmentEvidenceFolderTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEvidenceFoldersByAssessmentResponseTypeDef = TypedDict(
    "GetEvidenceFoldersByAssessmentResponseTypeDef",
    {
        "evidenceFolders": List[AssessmentEvidenceFolderTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetOrganizationAdminAccountResponseTypeDef = TypedDict(
    "GetOrganizationAdminAccountResponseTypeDef",
    {
        "adminAccountId": str,
        "organizationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssessmentFrameworkShareRequestsResponseTypeDef = TypedDict(
    "ListAssessmentFrameworkShareRequestsResponseTypeDef",
    {
        "assessmentFrameworkShareRequests": List[AssessmentFrameworkShareRequestTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssessmentFrameworksResponseTypeDef = TypedDict(
    "ListAssessmentFrameworksResponseTypeDef",
    {
        "frameworkMetadataList": List[AssessmentFrameworkMetadataTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssessmentReportsResponseTypeDef = TypedDict(
    "ListAssessmentReportsResponseTypeDef",
    {
        "assessmentReports": List[AssessmentReportMetadataTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListKeywordsForDataSourceResponseTypeDef = TypedDict(
    "ListKeywordsForDataSourceResponseTypeDef",
    {
        "keywords": List[str],
        "nextToken": str,
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
RegisterAccountResponseTypeDef = TypedDict(
    "RegisterAccountResponseTypeDef",
    {
        "status": AccountStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterOrganizationAdminAccountResponseTypeDef = TypedDict(
    "RegisterOrganizationAdminAccountResponseTypeDef",
    {
        "adminAccountId": str,
        "organizationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartAssessmentFrameworkShareResponseTypeDef = TypedDict(
    "StartAssessmentFrameworkShareResponseTypeDef",
    {
        "assessmentFrameworkShareRequest": AssessmentFrameworkShareRequestTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAssessmentFrameworkShareResponseTypeDef = TypedDict(
    "UpdateAssessmentFrameworkShareResponseTypeDef",
    {
        "assessmentFrameworkShareRequest": AssessmentFrameworkShareRequestTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ValidateAssessmentReportIntegrityResponseTypeDef = TypedDict(
    "ValidateAssessmentReportIntegrityResponseTypeDef",
    {
        "signatureValid": bool,
        "signatureAlgorithm": str,
        "signatureDateTime": str,
        "signatureKeyId": str,
        "validationErrors": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchCreateDelegationByAssessmentErrorTypeDef = TypedDict(
    "BatchCreateDelegationByAssessmentErrorTypeDef",
    {
        "createDelegationRequest": NotRequired[CreateDelegationRequestTypeDef],
        "errorCode": NotRequired[str],
        "errorMessage": NotRequired[str],
    },
)
BatchCreateDelegationByAssessmentRequestRequestTypeDef = TypedDict(
    "BatchCreateDelegationByAssessmentRequestRequestTypeDef",
    {
        "createDelegationRequests": Sequence[CreateDelegationRequestTypeDef],
        "assessmentId": str,
    },
)
BatchDeleteDelegationByAssessmentResponseTypeDef = TypedDict(
    "BatchDeleteDelegationByAssessmentResponseTypeDef",
    {
        "errors": List[BatchDeleteDelegationByAssessmentErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchImportEvidenceToAssessmentControlErrorTypeDef = TypedDict(
    "BatchImportEvidenceToAssessmentControlErrorTypeDef",
    {
        "manualEvidence": NotRequired[ManualEvidenceTypeDef],
        "errorCode": NotRequired[str],
        "errorMessage": NotRequired[str],
    },
)
BatchImportEvidenceToAssessmentControlRequestRequestTypeDef = TypedDict(
    "BatchImportEvidenceToAssessmentControlRequestRequestTypeDef",
    {
        "assessmentId": str,
        "controlSetId": str,
        "controlId": str,
        "manualEvidence": Sequence[ManualEvidenceTypeDef],
    },
)
GetChangeLogsResponseTypeDef = TypedDict(
    "GetChangeLogsResponseTypeDef",
    {
        "changeLogs": List[ChangeLogTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ControlDomainInsightsTypeDef = TypedDict(
    "ControlDomainInsightsTypeDef",
    {
        "name": NotRequired[str],
        "id": NotRequired[str],
        "controlsCountByNoncompliantEvidence": NotRequired[int],
        "totalControlsCount": NotRequired[int],
        "evidenceInsights": NotRequired[EvidenceInsightsTypeDef],
        "lastUpdated": NotRequired[datetime],
    },
)
ControlInsightsMetadataByAssessmentItemTypeDef = TypedDict(
    "ControlInsightsMetadataByAssessmentItemTypeDef",
    {
        "name": NotRequired[str],
        "id": NotRequired[str],
        "evidenceInsights": NotRequired[EvidenceInsightsTypeDef],
        "controlSetName": NotRequired[str],
        "lastUpdated": NotRequired[datetime],
    },
)
ControlInsightsMetadataItemTypeDef = TypedDict(
    "ControlInsightsMetadataItemTypeDef",
    {
        "name": NotRequired[str],
        "id": NotRequired[str],
        "evidenceInsights": NotRequired[EvidenceInsightsTypeDef],
        "lastUpdated": NotRequired[datetime],
    },
)
ControlMappingSourceTypeDef = TypedDict(
    "ControlMappingSourceTypeDef",
    {
        "sourceId": NotRequired[str],
        "sourceName": NotRequired[str],
        "sourceDescription": NotRequired[str],
        "sourceSetUpOption": NotRequired[SourceSetUpOptionType],
        "sourceType": NotRequired[SourceTypeType],
        "sourceKeyword": NotRequired[SourceKeywordTypeDef],
        "sourceFrequency": NotRequired[SourceFrequencyType],
        "troubleshootingText": NotRequired[str],
    },
)
CreateControlMappingSourceTypeDef = TypedDict(
    "CreateControlMappingSourceTypeDef",
    {
        "sourceName": NotRequired[str],
        "sourceDescription": NotRequired[str],
        "sourceSetUpOption": NotRequired[SourceSetUpOptionType],
        "sourceType": NotRequired[SourceTypeType],
        "sourceKeyword": NotRequired[SourceKeywordTypeDef],
        "sourceFrequency": NotRequired[SourceFrequencyType],
        "troubleshootingText": NotRequired[str],
    },
)
ListControlsResponseTypeDef = TypedDict(
    "ListControlsResponseTypeDef",
    {
        "controlMetadataList": List[ControlMetadataTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAssessmentFrameworkControlSetTypeDef = TypedDict(
    "CreateAssessmentFrameworkControlSetTypeDef",
    {
        "name": str,
        "controls": NotRequired[Sequence[CreateAssessmentFrameworkControlTypeDef]],
    },
)
UpdateAssessmentFrameworkControlSetTypeDef = TypedDict(
    "UpdateAssessmentFrameworkControlSetTypeDef",
    {
        "name": str,
        "controls": Sequence[CreateAssessmentFrameworkControlTypeDef],
        "id": NotRequired[str],
    },
)
GetDelegationsResponseTypeDef = TypedDict(
    "GetDelegationsResponseTypeDef",
    {
        "delegations": List[DelegationMetadataTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSettingsRequestRequestTypeDef = TypedDict(
    "UpdateSettingsRequestRequestTypeDef",
    {
        "snsTopic": NotRequired[str],
        "defaultAssessmentReportsDestination": NotRequired[AssessmentReportsDestinationTypeDef],
        "defaultProcessOwners": NotRequired[Sequence[RoleTypeDef]],
        "kmsKey": NotRequired[str],
        "evidenceFinderEnabled": NotRequired[bool],
        "deregistrationPolicy": NotRequired[DeregistrationPolicyTypeDef],
        "defaultExportDestination": NotRequired[DefaultExportDestinationTypeDef],
    },
)
SettingsTypeDef = TypedDict(
    "SettingsTypeDef",
    {
        "isAwsOrgEnabled": NotRequired[bool],
        "snsTopic": NotRequired[str],
        "defaultAssessmentReportsDestination": NotRequired[AssessmentReportsDestinationTypeDef],
        "defaultProcessOwners": NotRequired[List[RoleTypeDef]],
        "kmsKey": NotRequired[str],
        "evidenceFinderEnablement": NotRequired[EvidenceFinderEnablementTypeDef],
        "deregistrationPolicy": NotRequired[DeregistrationPolicyTypeDef],
        "defaultExportDestination": NotRequired[DefaultExportDestinationTypeDef],
    },
)
EvidenceTypeDef = TypedDict(
    "EvidenceTypeDef",
    {
        "dataSource": NotRequired[str],
        "evidenceAwsAccountId": NotRequired[str],
        "time": NotRequired[datetime],
        "eventSource": NotRequired[str],
        "eventName": NotRequired[str],
        "evidenceByType": NotRequired[str],
        "resourcesIncluded": NotRequired[List[ResourceTypeDef]],
        "attributes": NotRequired[Dict[str, str]],
        "iamId": NotRequired[str],
        "complianceCheck": NotRequired[str],
        "awsOrganization": NotRequired[str],
        "awsAccountId": NotRequired[str],
        "evidenceFolderId": NotRequired[str],
        "id": NotRequired[str],
        "assessmentReportSelection": NotRequired[str],
    },
)
GetAssessmentReportUrlResponseTypeDef = TypedDict(
    "GetAssessmentReportUrlResponseTypeDef",
    {
        "preSignedUrl": URLTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetInsightsByAssessmentResponseTypeDef = TypedDict(
    "GetInsightsByAssessmentResponseTypeDef",
    {
        "insights": InsightsByAssessmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetInsightsResponseTypeDef = TypedDict(
    "GetInsightsResponseTypeDef",
    {
        "insights": InsightsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServicesInScopeResponseTypeDef = TypedDict(
    "GetServicesInScopeResponseTypeDef",
    {
        "serviceMetadata": List[ServiceMetadataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListNotificationsResponseTypeDef = TypedDict(
    "ListNotificationsResponseTypeDef",
    {
        "notifications": List[NotificationTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssessmentMetadataTypeDef = TypedDict(
    "AssessmentMetadataTypeDef",
    {
        "name": NotRequired[str],
        "id": NotRequired[str],
        "description": NotRequired[str],
        "complianceType": NotRequired[str],
        "status": NotRequired[AssessmentStatusType],
        "assessmentReportsDestination": NotRequired[AssessmentReportsDestinationTypeDef],
        "scope": NotRequired[ScopeOutputTypeDef],
        "roles": NotRequired[List[RoleTypeDef]],
        "delegations": NotRequired[List[DelegationTypeDef]],
        "creationTime": NotRequired[datetime],
        "lastUpdated": NotRequired[datetime],
    },
)
CreateAssessmentRequestRequestTypeDef = TypedDict(
    "CreateAssessmentRequestRequestTypeDef",
    {
        "name": str,
        "assessmentReportsDestination": AssessmentReportsDestinationTypeDef,
        "scope": ScopeTypeDef,
        "roles": Sequence[RoleTypeDef],
        "frameworkId": str,
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
UpdateAssessmentRequestRequestTypeDef = TypedDict(
    "UpdateAssessmentRequestRequestTypeDef",
    {
        "assessmentId": str,
        "scope": ScopeTypeDef,
        "assessmentName": NotRequired[str],
        "assessmentDescription": NotRequired[str],
        "assessmentReportsDestination": NotRequired[AssessmentReportsDestinationTypeDef],
        "roles": NotRequired[Sequence[RoleTypeDef]],
    },
)
ListAssessmentsResponseTypeDef = TypedDict(
    "ListAssessmentsResponseTypeDef",
    {
        "assessmentMetadata": List[AssessmentMetadataItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssessmentControlSetTypeDef = TypedDict(
    "AssessmentControlSetTypeDef",
    {
        "id": NotRequired[str],
        "description": NotRequired[str],
        "status": NotRequired[ControlSetStatusType],
        "roles": NotRequired[List[RoleTypeDef]],
        "controls": NotRequired[List[AssessmentControlTypeDef]],
        "delegations": NotRequired[List[DelegationTypeDef]],
        "systemEvidenceCount": NotRequired[int],
        "manualEvidenceCount": NotRequired[int],
    },
)
UpdateAssessmentControlResponseTypeDef = TypedDict(
    "UpdateAssessmentControlResponseTypeDef",
    {
        "control": AssessmentControlTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchCreateDelegationByAssessmentResponseTypeDef = TypedDict(
    "BatchCreateDelegationByAssessmentResponseTypeDef",
    {
        "delegations": List[DelegationTypeDef],
        "errors": List[BatchCreateDelegationByAssessmentErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchImportEvidenceToAssessmentControlResponseTypeDef = TypedDict(
    "BatchImportEvidenceToAssessmentControlResponseTypeDef",
    {
        "errors": List[BatchImportEvidenceToAssessmentControlErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListControlDomainInsightsByAssessmentResponseTypeDef = TypedDict(
    "ListControlDomainInsightsByAssessmentResponseTypeDef",
    {
        "controlDomainInsights": List[ControlDomainInsightsTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListControlDomainInsightsResponseTypeDef = TypedDict(
    "ListControlDomainInsightsResponseTypeDef",
    {
        "controlDomainInsights": List[ControlDomainInsightsTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssessmentControlInsightsByControlDomainResponseTypeDef = TypedDict(
    "ListAssessmentControlInsightsByControlDomainResponseTypeDef",
    {
        "controlInsightsByAssessment": List[ControlInsightsMetadataByAssessmentItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListControlInsightsByControlDomainResponseTypeDef = TypedDict(
    "ListControlInsightsByControlDomainResponseTypeDef",
    {
        "controlInsightsMetadata": List[ControlInsightsMetadataItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ControlTypeDef = TypedDict(
    "ControlTypeDef",
    {
        "arn": NotRequired[str],
        "id": NotRequired[str],
        "type": NotRequired[ControlTypeType],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "testingInformation": NotRequired[str],
        "actionPlanTitle": NotRequired[str],
        "actionPlanInstructions": NotRequired[str],
        "controlSources": NotRequired[str],
        "controlMappingSources": NotRequired[List[ControlMappingSourceTypeDef]],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "lastUpdatedBy": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "state": NotRequired[ControlStateType],
    },
)
UpdateControlRequestRequestTypeDef = TypedDict(
    "UpdateControlRequestRequestTypeDef",
    {
        "controlId": str,
        "name": str,
        "controlMappingSources": Sequence[ControlMappingSourceTypeDef],
        "description": NotRequired[str],
        "testingInformation": NotRequired[str],
        "actionPlanTitle": NotRequired[str],
        "actionPlanInstructions": NotRequired[str],
    },
)
CreateControlRequestRequestTypeDef = TypedDict(
    "CreateControlRequestRequestTypeDef",
    {
        "name": str,
        "controlMappingSources": Sequence[CreateControlMappingSourceTypeDef],
        "description": NotRequired[str],
        "testingInformation": NotRequired[str],
        "actionPlanTitle": NotRequired[str],
        "actionPlanInstructions": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateAssessmentFrameworkRequestRequestTypeDef = TypedDict(
    "CreateAssessmentFrameworkRequestRequestTypeDef",
    {
        "name": str,
        "controlSets": Sequence[CreateAssessmentFrameworkControlSetTypeDef],
        "description": NotRequired[str],
        "complianceType": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
UpdateAssessmentFrameworkRequestRequestTypeDef = TypedDict(
    "UpdateAssessmentFrameworkRequestRequestTypeDef",
    {
        "frameworkId": str,
        "name": str,
        "controlSets": Sequence[UpdateAssessmentFrameworkControlSetTypeDef],
        "description": NotRequired[str],
        "complianceType": NotRequired[str],
    },
)
GetSettingsResponseTypeDef = TypedDict(
    "GetSettingsResponseTypeDef",
    {
        "settings": SettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSettingsResponseTypeDef = TypedDict(
    "UpdateSettingsResponseTypeDef",
    {
        "settings": SettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEvidenceByEvidenceFolderResponseTypeDef = TypedDict(
    "GetEvidenceByEvidenceFolderResponseTypeDef",
    {
        "evidence": List[EvidenceTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEvidenceResponseTypeDef = TypedDict(
    "GetEvidenceResponseTypeDef",
    {
        "evidence": EvidenceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssessmentFrameworkTypeDef = TypedDict(
    "AssessmentFrameworkTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "metadata": NotRequired[FrameworkMetadataTypeDef],
        "controlSets": NotRequired[List[AssessmentControlSetTypeDef]],
    },
)
UpdateAssessmentControlSetStatusResponseTypeDef = TypedDict(
    "UpdateAssessmentControlSetStatusResponseTypeDef",
    {
        "controlSet": AssessmentControlSetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ControlSetTypeDef = TypedDict(
    "ControlSetTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "controls": NotRequired[List[ControlTypeDef]],
    },
)
CreateControlResponseTypeDef = TypedDict(
    "CreateControlResponseTypeDef",
    {
        "control": ControlTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetControlResponseTypeDef = TypedDict(
    "GetControlResponseTypeDef",
    {
        "control": ControlTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateControlResponseTypeDef = TypedDict(
    "UpdateControlResponseTypeDef",
    {
        "control": ControlTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssessmentTypeDef = TypedDict(
    "AssessmentTypeDef",
    {
        "arn": NotRequired[str],
        "awsAccount": NotRequired[AWSAccountTypeDef],
        "metadata": NotRequired[AssessmentMetadataTypeDef],
        "framework": NotRequired[AssessmentFrameworkTypeDef],
        "tags": NotRequired[Dict[str, str]],
    },
)
FrameworkTypeDef = TypedDict(
    "FrameworkTypeDef",
    {
        "arn": NotRequired[str],
        "id": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[FrameworkTypeType],
        "complianceType": NotRequired[str],
        "description": NotRequired[str],
        "logo": NotRequired[str],
        "controlSources": NotRequired[str],
        "controlSets": NotRequired[List[ControlSetTypeDef]],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "lastUpdatedBy": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)
CreateAssessmentResponseTypeDef = TypedDict(
    "CreateAssessmentResponseTypeDef",
    {
        "assessment": AssessmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAssessmentResponseTypeDef = TypedDict(
    "GetAssessmentResponseTypeDef",
    {
        "assessment": AssessmentTypeDef,
        "userRole": RoleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAssessmentResponseTypeDef = TypedDict(
    "UpdateAssessmentResponseTypeDef",
    {
        "assessment": AssessmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAssessmentStatusResponseTypeDef = TypedDict(
    "UpdateAssessmentStatusResponseTypeDef",
    {
        "assessment": AssessmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAssessmentFrameworkResponseTypeDef = TypedDict(
    "CreateAssessmentFrameworkResponseTypeDef",
    {
        "framework": FrameworkTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAssessmentFrameworkResponseTypeDef = TypedDict(
    "GetAssessmentFrameworkResponseTypeDef",
    {
        "framework": FrameworkTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAssessmentFrameworkResponseTypeDef = TypedDict(
    "UpdateAssessmentFrameworkResponseTypeDef",
    {
        "framework": FrameworkTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
