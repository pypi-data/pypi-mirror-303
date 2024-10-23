"""
Type annotations for mturk service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/type_defs/)

Usage::

    ```python
    from mypy_boto3_mturk.type_defs import AcceptQualificationRequestRequestRequestTypeDef

    data: AcceptQualificationRequestRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    AssignmentStatusType,
    ComparatorType,
    EventTypeType,
    HITAccessActionsType,
    HITReviewStatusType,
    HITStatusType,
    NotificationTransportType,
    NotifyWorkersFailureCodeType,
    QualificationStatusType,
    QualificationTypeStatusType,
    ReviewableHITStatusType,
    ReviewActionStatusType,
    ReviewPolicyLevelType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AcceptQualificationRequestRequestRequestTypeDef",
    "ApproveAssignmentRequestRequestTypeDef",
    "AssignmentTypeDef",
    "AssociateQualificationWithWorkerRequestRequestTypeDef",
    "BonusPaymentTypeDef",
    "CreateAdditionalAssignmentsForHITRequestRequestTypeDef",
    "HITLayoutParameterTypeDef",
    "ResponseMetadataTypeDef",
    "CreateQualificationTypeRequestRequestTypeDef",
    "QualificationTypeTypeDef",
    "CreateWorkerBlockRequestRequestTypeDef",
    "DeleteHITRequestRequestTypeDef",
    "DeleteQualificationTypeRequestRequestTypeDef",
    "DeleteWorkerBlockRequestRequestTypeDef",
    "DisassociateQualificationFromWorkerRequestRequestTypeDef",
    "GetAssignmentRequestRequestTypeDef",
    "GetFileUploadURLRequestRequestTypeDef",
    "GetHITRequestRequestTypeDef",
    "GetQualificationScoreRequestRequestTypeDef",
    "GetQualificationTypeRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListAssignmentsForHITRequestRequestTypeDef",
    "ListBonusPaymentsRequestRequestTypeDef",
    "ListHITsForQualificationTypeRequestRequestTypeDef",
    "ListHITsRequestRequestTypeDef",
    "ListQualificationRequestsRequestRequestTypeDef",
    "QualificationRequestTypeDef",
    "ListQualificationTypesRequestRequestTypeDef",
    "ListReviewPolicyResultsForHITRequestRequestTypeDef",
    "ListReviewableHITsRequestRequestTypeDef",
    "ListWorkerBlocksRequestRequestTypeDef",
    "WorkerBlockTypeDef",
    "ListWorkersWithQualificationTypeRequestRequestTypeDef",
    "LocaleTypeDef",
    "NotificationSpecificationTypeDef",
    "NotifyWorkersFailureStatusTypeDef",
    "NotifyWorkersRequestRequestTypeDef",
    "ParameterMapEntryOutputTypeDef",
    "ParameterMapEntryTypeDef",
    "RejectAssignmentRequestRequestTypeDef",
    "RejectQualificationRequestRequestRequestTypeDef",
    "ReviewActionDetailTypeDef",
    "ReviewResultDetailTypeDef",
    "SendBonusRequestRequestTypeDef",
    "TimestampTypeDef",
    "UpdateHITReviewStatusRequestRequestTypeDef",
    "UpdateHITTypeOfHITRequestRequestTypeDef",
    "UpdateQualificationTypeRequestRequestTypeDef",
    "CreateHITTypeResponseTypeDef",
    "GetAccountBalanceResponseTypeDef",
    "GetFileUploadURLResponseTypeDef",
    "ListAssignmentsForHITResponseTypeDef",
    "ListBonusPaymentsResponseTypeDef",
    "CreateQualificationTypeResponseTypeDef",
    "GetQualificationTypeResponseTypeDef",
    "ListQualificationTypesResponseTypeDef",
    "UpdateQualificationTypeResponseTypeDef",
    "ListAssignmentsForHITRequestListAssignmentsForHITPaginateTypeDef",
    "ListBonusPaymentsRequestListBonusPaymentsPaginateTypeDef",
    "ListHITsForQualificationTypeRequestListHITsForQualificationTypePaginateTypeDef",
    "ListHITsRequestListHITsPaginateTypeDef",
    "ListQualificationRequestsRequestListQualificationRequestsPaginateTypeDef",
    "ListQualificationTypesRequestListQualificationTypesPaginateTypeDef",
    "ListReviewableHITsRequestListReviewableHITsPaginateTypeDef",
    "ListWorkerBlocksRequestListWorkerBlocksPaginateTypeDef",
    "ListWorkersWithQualificationTypeRequestListWorkersWithQualificationTypePaginateTypeDef",
    "ListQualificationRequestsResponseTypeDef",
    "ListWorkerBlocksResponseTypeDef",
    "QualificationRequirementOutputTypeDef",
    "QualificationRequirementTypeDef",
    "QualificationTypeDef",
    "SendTestEventNotificationRequestRequestTypeDef",
    "UpdateNotificationSettingsRequestRequestTypeDef",
    "NotifyWorkersResponseTypeDef",
    "PolicyParameterOutputTypeDef",
    "ParameterMapEntryUnionTypeDef",
    "ReviewReportTypeDef",
    "UpdateExpirationForHITRequestRequestTypeDef",
    "HITTypeDef",
    "CreateHITTypeRequestRequestTypeDef",
    "QualificationRequirementUnionTypeDef",
    "GetQualificationScoreResponseTypeDef",
    "ListWorkersWithQualificationTypeResponseTypeDef",
    "ReviewPolicyOutputTypeDef",
    "PolicyParameterTypeDef",
    "CreateHITResponseTypeDef",
    "CreateHITWithHITTypeResponseTypeDef",
    "GetAssignmentResponseTypeDef",
    "GetHITResponseTypeDef",
    "ListHITsForQualificationTypeResponseTypeDef",
    "ListHITsResponseTypeDef",
    "ListReviewableHITsResponseTypeDef",
    "ListReviewPolicyResultsForHITResponseTypeDef",
    "PolicyParameterUnionTypeDef",
    "ReviewPolicyTypeDef",
    "CreateHITRequestRequestTypeDef",
    "CreateHITWithHITTypeRequestRequestTypeDef",
)

AcceptQualificationRequestRequestRequestTypeDef = TypedDict(
    "AcceptQualificationRequestRequestRequestTypeDef",
    {
        "QualificationRequestId": str,
        "IntegerValue": NotRequired[int],
    },
)
ApproveAssignmentRequestRequestTypeDef = TypedDict(
    "ApproveAssignmentRequestRequestTypeDef",
    {
        "AssignmentId": str,
        "RequesterFeedback": NotRequired[str],
        "OverrideRejection": NotRequired[bool],
    },
)
AssignmentTypeDef = TypedDict(
    "AssignmentTypeDef",
    {
        "AssignmentId": NotRequired[str],
        "WorkerId": NotRequired[str],
        "HITId": NotRequired[str],
        "AssignmentStatus": NotRequired[AssignmentStatusType],
        "AutoApprovalTime": NotRequired[datetime],
        "AcceptTime": NotRequired[datetime],
        "SubmitTime": NotRequired[datetime],
        "ApprovalTime": NotRequired[datetime],
        "RejectionTime": NotRequired[datetime],
        "Deadline": NotRequired[datetime],
        "Answer": NotRequired[str],
        "RequesterFeedback": NotRequired[str],
    },
)
AssociateQualificationWithWorkerRequestRequestTypeDef = TypedDict(
    "AssociateQualificationWithWorkerRequestRequestTypeDef",
    {
        "QualificationTypeId": str,
        "WorkerId": str,
        "IntegerValue": NotRequired[int],
        "SendNotification": NotRequired[bool],
    },
)
BonusPaymentTypeDef = TypedDict(
    "BonusPaymentTypeDef",
    {
        "WorkerId": NotRequired[str],
        "BonusAmount": NotRequired[str],
        "AssignmentId": NotRequired[str],
        "Reason": NotRequired[str],
        "GrantTime": NotRequired[datetime],
    },
)
CreateAdditionalAssignmentsForHITRequestRequestTypeDef = TypedDict(
    "CreateAdditionalAssignmentsForHITRequestRequestTypeDef",
    {
        "HITId": str,
        "NumberOfAdditionalAssignments": int,
        "UniqueRequestToken": NotRequired[str],
    },
)
HITLayoutParameterTypeDef = TypedDict(
    "HITLayoutParameterTypeDef",
    {
        "Name": str,
        "Value": str,
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
CreateQualificationTypeRequestRequestTypeDef = TypedDict(
    "CreateQualificationTypeRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "QualificationTypeStatus": QualificationTypeStatusType,
        "Keywords": NotRequired[str],
        "RetryDelayInSeconds": NotRequired[int],
        "Test": NotRequired[str],
        "AnswerKey": NotRequired[str],
        "TestDurationInSeconds": NotRequired[int],
        "AutoGranted": NotRequired[bool],
        "AutoGrantedValue": NotRequired[int],
    },
)
QualificationTypeTypeDef = TypedDict(
    "QualificationTypeTypeDef",
    {
        "QualificationTypeId": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Keywords": NotRequired[str],
        "QualificationTypeStatus": NotRequired[QualificationTypeStatusType],
        "Test": NotRequired[str],
        "TestDurationInSeconds": NotRequired[int],
        "AnswerKey": NotRequired[str],
        "RetryDelayInSeconds": NotRequired[int],
        "IsRequestable": NotRequired[bool],
        "AutoGranted": NotRequired[bool],
        "AutoGrantedValue": NotRequired[int],
    },
)
CreateWorkerBlockRequestRequestTypeDef = TypedDict(
    "CreateWorkerBlockRequestRequestTypeDef",
    {
        "WorkerId": str,
        "Reason": str,
    },
)
DeleteHITRequestRequestTypeDef = TypedDict(
    "DeleteHITRequestRequestTypeDef",
    {
        "HITId": str,
    },
)
DeleteQualificationTypeRequestRequestTypeDef = TypedDict(
    "DeleteQualificationTypeRequestRequestTypeDef",
    {
        "QualificationTypeId": str,
    },
)
DeleteWorkerBlockRequestRequestTypeDef = TypedDict(
    "DeleteWorkerBlockRequestRequestTypeDef",
    {
        "WorkerId": str,
        "Reason": NotRequired[str],
    },
)
DisassociateQualificationFromWorkerRequestRequestTypeDef = TypedDict(
    "DisassociateQualificationFromWorkerRequestRequestTypeDef",
    {
        "WorkerId": str,
        "QualificationTypeId": str,
        "Reason": NotRequired[str],
    },
)
GetAssignmentRequestRequestTypeDef = TypedDict(
    "GetAssignmentRequestRequestTypeDef",
    {
        "AssignmentId": str,
    },
)
GetFileUploadURLRequestRequestTypeDef = TypedDict(
    "GetFileUploadURLRequestRequestTypeDef",
    {
        "AssignmentId": str,
        "QuestionIdentifier": str,
    },
)
GetHITRequestRequestTypeDef = TypedDict(
    "GetHITRequestRequestTypeDef",
    {
        "HITId": str,
    },
)
GetQualificationScoreRequestRequestTypeDef = TypedDict(
    "GetQualificationScoreRequestRequestTypeDef",
    {
        "QualificationTypeId": str,
        "WorkerId": str,
    },
)
GetQualificationTypeRequestRequestTypeDef = TypedDict(
    "GetQualificationTypeRequestRequestTypeDef",
    {
        "QualificationTypeId": str,
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
ListAssignmentsForHITRequestRequestTypeDef = TypedDict(
    "ListAssignmentsForHITRequestRequestTypeDef",
    {
        "HITId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "AssignmentStatuses": NotRequired[Sequence[AssignmentStatusType]],
    },
)
ListBonusPaymentsRequestRequestTypeDef = TypedDict(
    "ListBonusPaymentsRequestRequestTypeDef",
    {
        "HITId": NotRequired[str],
        "AssignmentId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListHITsForQualificationTypeRequestRequestTypeDef = TypedDict(
    "ListHITsForQualificationTypeRequestRequestTypeDef",
    {
        "QualificationTypeId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListHITsRequestRequestTypeDef = TypedDict(
    "ListHITsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListQualificationRequestsRequestRequestTypeDef = TypedDict(
    "ListQualificationRequestsRequestRequestTypeDef",
    {
        "QualificationTypeId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
QualificationRequestTypeDef = TypedDict(
    "QualificationRequestTypeDef",
    {
        "QualificationRequestId": NotRequired[str],
        "QualificationTypeId": NotRequired[str],
        "WorkerId": NotRequired[str],
        "Test": NotRequired[str],
        "Answer": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
    },
)
ListQualificationTypesRequestRequestTypeDef = TypedDict(
    "ListQualificationTypesRequestRequestTypeDef",
    {
        "MustBeRequestable": bool,
        "Query": NotRequired[str],
        "MustBeOwnedByCaller": NotRequired[bool],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListReviewPolicyResultsForHITRequestRequestTypeDef = TypedDict(
    "ListReviewPolicyResultsForHITRequestRequestTypeDef",
    {
        "HITId": str,
        "PolicyLevels": NotRequired[Sequence[ReviewPolicyLevelType]],
        "RetrieveActions": NotRequired[bool],
        "RetrieveResults": NotRequired[bool],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListReviewableHITsRequestRequestTypeDef = TypedDict(
    "ListReviewableHITsRequestRequestTypeDef",
    {
        "HITTypeId": NotRequired[str],
        "Status": NotRequired[ReviewableHITStatusType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListWorkerBlocksRequestRequestTypeDef = TypedDict(
    "ListWorkerBlocksRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
WorkerBlockTypeDef = TypedDict(
    "WorkerBlockTypeDef",
    {
        "WorkerId": NotRequired[str],
        "Reason": NotRequired[str],
    },
)
ListWorkersWithQualificationTypeRequestRequestTypeDef = TypedDict(
    "ListWorkersWithQualificationTypeRequestRequestTypeDef",
    {
        "QualificationTypeId": str,
        "Status": NotRequired[QualificationStatusType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
LocaleTypeDef = TypedDict(
    "LocaleTypeDef",
    {
        "Country": str,
        "Subdivision": NotRequired[str],
    },
)
NotificationSpecificationTypeDef = TypedDict(
    "NotificationSpecificationTypeDef",
    {
        "Destination": str,
        "Transport": NotificationTransportType,
        "Version": str,
        "EventTypes": Sequence[EventTypeType],
    },
)
NotifyWorkersFailureStatusTypeDef = TypedDict(
    "NotifyWorkersFailureStatusTypeDef",
    {
        "NotifyWorkersFailureCode": NotRequired[NotifyWorkersFailureCodeType],
        "NotifyWorkersFailureMessage": NotRequired[str],
        "WorkerId": NotRequired[str],
    },
)
NotifyWorkersRequestRequestTypeDef = TypedDict(
    "NotifyWorkersRequestRequestTypeDef",
    {
        "Subject": str,
        "MessageText": str,
        "WorkerIds": Sequence[str],
    },
)
ParameterMapEntryOutputTypeDef = TypedDict(
    "ParameterMapEntryOutputTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[List[str]],
    },
)
ParameterMapEntryTypeDef = TypedDict(
    "ParameterMapEntryTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)
RejectAssignmentRequestRequestTypeDef = TypedDict(
    "RejectAssignmentRequestRequestTypeDef",
    {
        "AssignmentId": str,
        "RequesterFeedback": str,
    },
)
RejectQualificationRequestRequestRequestTypeDef = TypedDict(
    "RejectQualificationRequestRequestRequestTypeDef",
    {
        "QualificationRequestId": str,
        "Reason": NotRequired[str],
    },
)
ReviewActionDetailTypeDef = TypedDict(
    "ReviewActionDetailTypeDef",
    {
        "ActionId": NotRequired[str],
        "ActionName": NotRequired[str],
        "TargetId": NotRequired[str],
        "TargetType": NotRequired[str],
        "Status": NotRequired[ReviewActionStatusType],
        "CompleteTime": NotRequired[datetime],
        "Result": NotRequired[str],
        "ErrorCode": NotRequired[str],
    },
)
ReviewResultDetailTypeDef = TypedDict(
    "ReviewResultDetailTypeDef",
    {
        "ActionId": NotRequired[str],
        "SubjectId": NotRequired[str],
        "SubjectType": NotRequired[str],
        "QuestionId": NotRequired[str],
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
SendBonusRequestRequestTypeDef = TypedDict(
    "SendBonusRequestRequestTypeDef",
    {
        "WorkerId": str,
        "BonusAmount": str,
        "AssignmentId": str,
        "Reason": str,
        "UniqueRequestToken": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
UpdateHITReviewStatusRequestRequestTypeDef = TypedDict(
    "UpdateHITReviewStatusRequestRequestTypeDef",
    {
        "HITId": str,
        "Revert": NotRequired[bool],
    },
)
UpdateHITTypeOfHITRequestRequestTypeDef = TypedDict(
    "UpdateHITTypeOfHITRequestRequestTypeDef",
    {
        "HITId": str,
        "HITTypeId": str,
    },
)
UpdateQualificationTypeRequestRequestTypeDef = TypedDict(
    "UpdateQualificationTypeRequestRequestTypeDef",
    {
        "QualificationTypeId": str,
        "Description": NotRequired[str],
        "QualificationTypeStatus": NotRequired[QualificationTypeStatusType],
        "Test": NotRequired[str],
        "AnswerKey": NotRequired[str],
        "TestDurationInSeconds": NotRequired[int],
        "RetryDelayInSeconds": NotRequired[int],
        "AutoGranted": NotRequired[bool],
        "AutoGrantedValue": NotRequired[int],
    },
)
CreateHITTypeResponseTypeDef = TypedDict(
    "CreateHITTypeResponseTypeDef",
    {
        "HITTypeId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAccountBalanceResponseTypeDef = TypedDict(
    "GetAccountBalanceResponseTypeDef",
    {
        "AvailableBalance": str,
        "OnHoldBalance": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFileUploadURLResponseTypeDef = TypedDict(
    "GetFileUploadURLResponseTypeDef",
    {
        "FileUploadURL": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssignmentsForHITResponseTypeDef = TypedDict(
    "ListAssignmentsForHITResponseTypeDef",
    {
        "NumResults": int,
        "Assignments": List[AssignmentTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListBonusPaymentsResponseTypeDef = TypedDict(
    "ListBonusPaymentsResponseTypeDef",
    {
        "NumResults": int,
        "BonusPayments": List[BonusPaymentTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateQualificationTypeResponseTypeDef = TypedDict(
    "CreateQualificationTypeResponseTypeDef",
    {
        "QualificationType": QualificationTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetQualificationTypeResponseTypeDef = TypedDict(
    "GetQualificationTypeResponseTypeDef",
    {
        "QualificationType": QualificationTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListQualificationTypesResponseTypeDef = TypedDict(
    "ListQualificationTypesResponseTypeDef",
    {
        "NumResults": int,
        "QualificationTypes": List[QualificationTypeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateQualificationTypeResponseTypeDef = TypedDict(
    "UpdateQualificationTypeResponseTypeDef",
    {
        "QualificationType": QualificationTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssignmentsForHITRequestListAssignmentsForHITPaginateTypeDef = TypedDict(
    "ListAssignmentsForHITRequestListAssignmentsForHITPaginateTypeDef",
    {
        "HITId": str,
        "AssignmentStatuses": NotRequired[Sequence[AssignmentStatusType]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListBonusPaymentsRequestListBonusPaymentsPaginateTypeDef = TypedDict(
    "ListBonusPaymentsRequestListBonusPaymentsPaginateTypeDef",
    {
        "HITId": NotRequired[str],
        "AssignmentId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListHITsForQualificationTypeRequestListHITsForQualificationTypePaginateTypeDef = TypedDict(
    "ListHITsForQualificationTypeRequestListHITsForQualificationTypePaginateTypeDef",
    {
        "QualificationTypeId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListHITsRequestListHITsPaginateTypeDef = TypedDict(
    "ListHITsRequestListHITsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListQualificationRequestsRequestListQualificationRequestsPaginateTypeDef = TypedDict(
    "ListQualificationRequestsRequestListQualificationRequestsPaginateTypeDef",
    {
        "QualificationTypeId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListQualificationTypesRequestListQualificationTypesPaginateTypeDef = TypedDict(
    "ListQualificationTypesRequestListQualificationTypesPaginateTypeDef",
    {
        "MustBeRequestable": bool,
        "Query": NotRequired[str],
        "MustBeOwnedByCaller": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListReviewableHITsRequestListReviewableHITsPaginateTypeDef = TypedDict(
    "ListReviewableHITsRequestListReviewableHITsPaginateTypeDef",
    {
        "HITTypeId": NotRequired[str],
        "Status": NotRequired[ReviewableHITStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWorkerBlocksRequestListWorkerBlocksPaginateTypeDef = TypedDict(
    "ListWorkerBlocksRequestListWorkerBlocksPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWorkersWithQualificationTypeRequestListWorkersWithQualificationTypePaginateTypeDef = TypedDict(
    "ListWorkersWithQualificationTypeRequestListWorkersWithQualificationTypePaginateTypeDef",
    {
        "QualificationTypeId": str,
        "Status": NotRequired[QualificationStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListQualificationRequestsResponseTypeDef = TypedDict(
    "ListQualificationRequestsResponseTypeDef",
    {
        "NumResults": int,
        "QualificationRequests": List[QualificationRequestTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListWorkerBlocksResponseTypeDef = TypedDict(
    "ListWorkerBlocksResponseTypeDef",
    {
        "NumResults": int,
        "WorkerBlocks": List[WorkerBlockTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
QualificationRequirementOutputTypeDef = TypedDict(
    "QualificationRequirementOutputTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": ComparatorType,
        "IntegerValues": NotRequired[List[int]],
        "LocaleValues": NotRequired[List[LocaleTypeDef]],
        "RequiredToPreview": NotRequired[bool],
        "ActionsGuarded": NotRequired[HITAccessActionsType],
    },
)
QualificationRequirementTypeDef = TypedDict(
    "QualificationRequirementTypeDef",
    {
        "QualificationTypeId": str,
        "Comparator": ComparatorType,
        "IntegerValues": NotRequired[Sequence[int]],
        "LocaleValues": NotRequired[Sequence[LocaleTypeDef]],
        "RequiredToPreview": NotRequired[bool],
        "ActionsGuarded": NotRequired[HITAccessActionsType],
    },
)
QualificationTypeDef = TypedDict(
    "QualificationTypeDef",
    {
        "QualificationTypeId": NotRequired[str],
        "WorkerId": NotRequired[str],
        "GrantTime": NotRequired[datetime],
        "IntegerValue": NotRequired[int],
        "LocaleValue": NotRequired[LocaleTypeDef],
        "Status": NotRequired[QualificationStatusType],
    },
)
SendTestEventNotificationRequestRequestTypeDef = TypedDict(
    "SendTestEventNotificationRequestRequestTypeDef",
    {
        "Notification": NotificationSpecificationTypeDef,
        "TestEventType": EventTypeType,
    },
)
UpdateNotificationSettingsRequestRequestTypeDef = TypedDict(
    "UpdateNotificationSettingsRequestRequestTypeDef",
    {
        "HITTypeId": str,
        "Notification": NotRequired[NotificationSpecificationTypeDef],
        "Active": NotRequired[bool],
    },
)
NotifyWorkersResponseTypeDef = TypedDict(
    "NotifyWorkersResponseTypeDef",
    {
        "NotifyWorkersFailureStatuses": List[NotifyWorkersFailureStatusTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PolicyParameterOutputTypeDef = TypedDict(
    "PolicyParameterOutputTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[List[str]],
        "MapEntries": NotRequired[List[ParameterMapEntryOutputTypeDef]],
    },
)
ParameterMapEntryUnionTypeDef = Union[ParameterMapEntryTypeDef, ParameterMapEntryOutputTypeDef]
ReviewReportTypeDef = TypedDict(
    "ReviewReportTypeDef",
    {
        "ReviewResults": NotRequired[List[ReviewResultDetailTypeDef]],
        "ReviewActions": NotRequired[List[ReviewActionDetailTypeDef]],
    },
)
UpdateExpirationForHITRequestRequestTypeDef = TypedDict(
    "UpdateExpirationForHITRequestRequestTypeDef",
    {
        "HITId": str,
        "ExpireAt": TimestampTypeDef,
    },
)
HITTypeDef = TypedDict(
    "HITTypeDef",
    {
        "HITId": NotRequired[str],
        "HITTypeId": NotRequired[str],
        "HITGroupId": NotRequired[str],
        "HITLayoutId": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "Title": NotRequired[str],
        "Description": NotRequired[str],
        "Question": NotRequired[str],
        "Keywords": NotRequired[str],
        "HITStatus": NotRequired[HITStatusType],
        "MaxAssignments": NotRequired[int],
        "Reward": NotRequired[str],
        "AutoApprovalDelayInSeconds": NotRequired[int],
        "Expiration": NotRequired[datetime],
        "AssignmentDurationInSeconds": NotRequired[int],
        "RequesterAnnotation": NotRequired[str],
        "QualificationRequirements": NotRequired[List[QualificationRequirementOutputTypeDef]],
        "HITReviewStatus": NotRequired[HITReviewStatusType],
        "NumberOfAssignmentsPending": NotRequired[int],
        "NumberOfAssignmentsAvailable": NotRequired[int],
        "NumberOfAssignmentsCompleted": NotRequired[int],
    },
)
CreateHITTypeRequestRequestTypeDef = TypedDict(
    "CreateHITTypeRequestRequestTypeDef",
    {
        "AssignmentDurationInSeconds": int,
        "Reward": str,
        "Title": str,
        "Description": str,
        "AutoApprovalDelayInSeconds": NotRequired[int],
        "Keywords": NotRequired[str],
        "QualificationRequirements": NotRequired[Sequence[QualificationRequirementTypeDef]],
    },
)
QualificationRequirementUnionTypeDef = Union[
    QualificationRequirementTypeDef, QualificationRequirementOutputTypeDef
]
GetQualificationScoreResponseTypeDef = TypedDict(
    "GetQualificationScoreResponseTypeDef",
    {
        "Qualification": QualificationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListWorkersWithQualificationTypeResponseTypeDef = TypedDict(
    "ListWorkersWithQualificationTypeResponseTypeDef",
    {
        "NumResults": int,
        "Qualifications": List[QualificationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ReviewPolicyOutputTypeDef = TypedDict(
    "ReviewPolicyOutputTypeDef",
    {
        "PolicyName": str,
        "Parameters": NotRequired[List[PolicyParameterOutputTypeDef]],
    },
)
PolicyParameterTypeDef = TypedDict(
    "PolicyParameterTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
        "MapEntries": NotRequired[Sequence[ParameterMapEntryUnionTypeDef]],
    },
)
CreateHITResponseTypeDef = TypedDict(
    "CreateHITResponseTypeDef",
    {
        "HIT": HITTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateHITWithHITTypeResponseTypeDef = TypedDict(
    "CreateHITWithHITTypeResponseTypeDef",
    {
        "HIT": HITTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAssignmentResponseTypeDef = TypedDict(
    "GetAssignmentResponseTypeDef",
    {
        "Assignment": AssignmentTypeDef,
        "HIT": HITTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetHITResponseTypeDef = TypedDict(
    "GetHITResponseTypeDef",
    {
        "HIT": HITTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListHITsForQualificationTypeResponseTypeDef = TypedDict(
    "ListHITsForQualificationTypeResponseTypeDef",
    {
        "NumResults": int,
        "HITs": List[HITTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListHITsResponseTypeDef = TypedDict(
    "ListHITsResponseTypeDef",
    {
        "NumResults": int,
        "HITs": List[HITTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListReviewableHITsResponseTypeDef = TypedDict(
    "ListReviewableHITsResponseTypeDef",
    {
        "NumResults": int,
        "HITs": List[HITTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListReviewPolicyResultsForHITResponseTypeDef = TypedDict(
    "ListReviewPolicyResultsForHITResponseTypeDef",
    {
        "HITId": str,
        "AssignmentReviewPolicy": ReviewPolicyOutputTypeDef,
        "HITReviewPolicy": ReviewPolicyOutputTypeDef,
        "AssignmentReviewReport": ReviewReportTypeDef,
        "HITReviewReport": ReviewReportTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PolicyParameterUnionTypeDef = Union[PolicyParameterTypeDef, PolicyParameterOutputTypeDef]
ReviewPolicyTypeDef = TypedDict(
    "ReviewPolicyTypeDef",
    {
        "PolicyName": str,
        "Parameters": NotRequired[Sequence[PolicyParameterUnionTypeDef]],
    },
)
CreateHITRequestRequestTypeDef = TypedDict(
    "CreateHITRequestRequestTypeDef",
    {
        "LifetimeInSeconds": int,
        "AssignmentDurationInSeconds": int,
        "Reward": str,
        "Title": str,
        "Description": str,
        "MaxAssignments": NotRequired[int],
        "AutoApprovalDelayInSeconds": NotRequired[int],
        "Keywords": NotRequired[str],
        "Question": NotRequired[str],
        "RequesterAnnotation": NotRequired[str],
        "QualificationRequirements": NotRequired[Sequence[QualificationRequirementUnionTypeDef]],
        "UniqueRequestToken": NotRequired[str],
        "AssignmentReviewPolicy": NotRequired[ReviewPolicyTypeDef],
        "HITReviewPolicy": NotRequired[ReviewPolicyTypeDef],
        "HITLayoutId": NotRequired[str],
        "HITLayoutParameters": NotRequired[Sequence[HITLayoutParameterTypeDef]],
    },
)
CreateHITWithHITTypeRequestRequestTypeDef = TypedDict(
    "CreateHITWithHITTypeRequestRequestTypeDef",
    {
        "HITTypeId": str,
        "LifetimeInSeconds": int,
        "MaxAssignments": NotRequired[int],
        "Question": NotRequired[str],
        "RequesterAnnotation": NotRequired[str],
        "UniqueRequestToken": NotRequired[str],
        "AssignmentReviewPolicy": NotRequired[ReviewPolicyTypeDef],
        "HITReviewPolicy": NotRequired[ReviewPolicyTypeDef],
        "HITLayoutId": NotRequired[str],
        "HITLayoutParameters": NotRequired[Sequence[HITLayoutParameterTypeDef]],
    },
)
