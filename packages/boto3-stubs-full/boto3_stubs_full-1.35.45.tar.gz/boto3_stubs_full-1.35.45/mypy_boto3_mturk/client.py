"""
Type annotations for mturk service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_mturk.client import MTurkClient

    session = Session()
    client: MTurkClient = session.client("mturk")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    ListAssignmentsForHITPaginator,
    ListBonusPaymentsPaginator,
    ListHITsForQualificationTypePaginator,
    ListHITsPaginator,
    ListQualificationRequestsPaginator,
    ListQualificationTypesPaginator,
    ListReviewableHITsPaginator,
    ListWorkerBlocksPaginator,
    ListWorkersWithQualificationTypePaginator,
)
from .type_defs import (
    AcceptQualificationRequestRequestRequestTypeDef,
    ApproveAssignmentRequestRequestTypeDef,
    AssociateQualificationWithWorkerRequestRequestTypeDef,
    CreateAdditionalAssignmentsForHITRequestRequestTypeDef,
    CreateHITRequestRequestTypeDef,
    CreateHITResponseTypeDef,
    CreateHITTypeRequestRequestTypeDef,
    CreateHITTypeResponseTypeDef,
    CreateHITWithHITTypeRequestRequestTypeDef,
    CreateHITWithHITTypeResponseTypeDef,
    CreateQualificationTypeRequestRequestTypeDef,
    CreateQualificationTypeResponseTypeDef,
    CreateWorkerBlockRequestRequestTypeDef,
    DeleteHITRequestRequestTypeDef,
    DeleteQualificationTypeRequestRequestTypeDef,
    DeleteWorkerBlockRequestRequestTypeDef,
    DisassociateQualificationFromWorkerRequestRequestTypeDef,
    GetAccountBalanceResponseTypeDef,
    GetAssignmentRequestRequestTypeDef,
    GetAssignmentResponseTypeDef,
    GetFileUploadURLRequestRequestTypeDef,
    GetFileUploadURLResponseTypeDef,
    GetHITRequestRequestTypeDef,
    GetHITResponseTypeDef,
    GetQualificationScoreRequestRequestTypeDef,
    GetQualificationScoreResponseTypeDef,
    GetQualificationTypeRequestRequestTypeDef,
    GetQualificationTypeResponseTypeDef,
    ListAssignmentsForHITRequestRequestTypeDef,
    ListAssignmentsForHITResponseTypeDef,
    ListBonusPaymentsRequestRequestTypeDef,
    ListBonusPaymentsResponseTypeDef,
    ListHITsForQualificationTypeRequestRequestTypeDef,
    ListHITsForQualificationTypeResponseTypeDef,
    ListHITsRequestRequestTypeDef,
    ListHITsResponseTypeDef,
    ListQualificationRequestsRequestRequestTypeDef,
    ListQualificationRequestsResponseTypeDef,
    ListQualificationTypesRequestRequestTypeDef,
    ListQualificationTypesResponseTypeDef,
    ListReviewableHITsRequestRequestTypeDef,
    ListReviewableHITsResponseTypeDef,
    ListReviewPolicyResultsForHITRequestRequestTypeDef,
    ListReviewPolicyResultsForHITResponseTypeDef,
    ListWorkerBlocksRequestRequestTypeDef,
    ListWorkerBlocksResponseTypeDef,
    ListWorkersWithQualificationTypeRequestRequestTypeDef,
    ListWorkersWithQualificationTypeResponseTypeDef,
    NotifyWorkersRequestRequestTypeDef,
    NotifyWorkersResponseTypeDef,
    RejectAssignmentRequestRequestTypeDef,
    RejectQualificationRequestRequestRequestTypeDef,
    SendBonusRequestRequestTypeDef,
    SendTestEventNotificationRequestRequestTypeDef,
    UpdateExpirationForHITRequestRequestTypeDef,
    UpdateHITReviewStatusRequestRequestTypeDef,
    UpdateHITTypeOfHITRequestRequestTypeDef,
    UpdateNotificationSettingsRequestRequestTypeDef,
    UpdateQualificationTypeRequestRequestTypeDef,
    UpdateQualificationTypeResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack


__all__ = ("MTurkClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    RequestError: Type[BotocoreClientError]
    ServiceFault: Type[BotocoreClientError]


class MTurkClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MTurkClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#exceptions)
        """

    def accept_qualification_request(
        self, **kwargs: Unpack[AcceptQualificationRequestRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        The `AcceptQualificationRequest` operation approves a Worker's request for a
        Qualification.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.accept_qualification_request)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#accept_qualification_request)
        """

    def approve_assignment(
        self, **kwargs: Unpack[ApproveAssignmentRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        The `ApproveAssignment` operation approves the results of a completed
        assignment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.approve_assignment)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#approve_assignment)
        """

    def associate_qualification_with_worker(
        self, **kwargs: Unpack[AssociateQualificationWithWorkerRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        The `AssociateQualificationWithWorker` operation gives a Worker a Qualification.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.associate_qualification_with_worker)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#associate_qualification_with_worker)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#close)
        """

    def create_additional_assignments_for_hit(
        self, **kwargs: Unpack[CreateAdditionalAssignmentsForHITRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        The `CreateAdditionalAssignmentsForHIT` operation increases the maximum number
        of assignments of an existing
        HIT.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.create_additional_assignments_for_hit)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#create_additional_assignments_for_hit)
        """

    def create_hit(
        self, **kwargs: Unpack[CreateHITRequestRequestTypeDef]
    ) -> CreateHITResponseTypeDef:
        """
        The `CreateHIT` operation creates a new Human Intelligence Task (HIT).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.create_hit)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#create_hit)
        """

    def create_hit_type(
        self, **kwargs: Unpack[CreateHITTypeRequestRequestTypeDef]
    ) -> CreateHITTypeResponseTypeDef:
        """
        The `CreateHITType` operation creates a new HIT type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.create_hit_type)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#create_hit_type)
        """

    def create_hit_with_hit_type(
        self, **kwargs: Unpack[CreateHITWithHITTypeRequestRequestTypeDef]
    ) -> CreateHITWithHITTypeResponseTypeDef:
        """
        The `CreateHITWithHITType` operation creates a new Human Intelligence Task
        (HIT) using an existing HITTypeID generated by the `CreateHITType`
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.create_hit_with_hit_type)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#create_hit_with_hit_type)
        """

    def create_qualification_type(
        self, **kwargs: Unpack[CreateQualificationTypeRequestRequestTypeDef]
    ) -> CreateQualificationTypeResponseTypeDef:
        """
        The `CreateQualificationType` operation creates a new Qualification type, which
        is represented by a `QualificationType` data
        structure.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.create_qualification_type)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#create_qualification_type)
        """

    def create_worker_block(
        self, **kwargs: Unpack[CreateWorkerBlockRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        The `CreateWorkerBlock` operation allows you to prevent a Worker from working
        on your
        HITs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.create_worker_block)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#create_worker_block)
        """

    def delete_hit(self, **kwargs: Unpack[DeleteHITRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        The `DeleteHIT` operation is used to delete HIT that is no longer needed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.delete_hit)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#delete_hit)
        """

    def delete_qualification_type(
        self, **kwargs: Unpack[DeleteQualificationTypeRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        The `DeleteQualificationType` deletes a Qualification type and deletes any HIT
        types that are associated with the Qualification
        type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.delete_qualification_type)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#delete_qualification_type)
        """

    def delete_worker_block(
        self, **kwargs: Unpack[DeleteWorkerBlockRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        The `DeleteWorkerBlock` operation allows you to reinstate a blocked Worker to
        work on your
        HITs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.delete_worker_block)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#delete_worker_block)
        """

    def disassociate_qualification_from_worker(
        self, **kwargs: Unpack[DisassociateQualificationFromWorkerRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        The `DisassociateQualificationFromWorker` revokes a previously granted
        Qualification from a
        user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.disassociate_qualification_from_worker)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#disassociate_qualification_from_worker)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#generate_presigned_url)
        """

    def get_account_balance(self) -> GetAccountBalanceResponseTypeDef:
        """
        The `GetAccountBalance` operation retrieves the Prepaid HITs balance in your
        Amazon Mechanical Turk account if you are a Prepaid
        Requester.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.get_account_balance)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#get_account_balance)
        """

    def get_assignment(
        self, **kwargs: Unpack[GetAssignmentRequestRequestTypeDef]
    ) -> GetAssignmentResponseTypeDef:
        """
        The `GetAssignment` operation retrieves the details of the specified Assignment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.get_assignment)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#get_assignment)
        """

    def get_file_upload_url(
        self, **kwargs: Unpack[GetFileUploadURLRequestRequestTypeDef]
    ) -> GetFileUploadURLResponseTypeDef:
        """
        The `GetFileUploadURL` operation generates and returns a temporary URL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.get_file_upload_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#get_file_upload_url)
        """

    def get_hit(self, **kwargs: Unpack[GetHITRequestRequestTypeDef]) -> GetHITResponseTypeDef:
        """
        The `GetHIT` operation retrieves the details of the specified HIT.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.get_hit)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#get_hit)
        """

    def get_qualification_score(
        self, **kwargs: Unpack[GetQualificationScoreRequestRequestTypeDef]
    ) -> GetQualificationScoreResponseTypeDef:
        """
        The `GetQualificationScore` operation returns the value of a Worker's
        Qualification for a given Qualification
        type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.get_qualification_score)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#get_qualification_score)
        """

    def get_qualification_type(
        self, **kwargs: Unpack[GetQualificationTypeRequestRequestTypeDef]
    ) -> GetQualificationTypeResponseTypeDef:
        """
        The `GetQualificationType`operation retrieves information about a Qualification
        type using its
        ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.get_qualification_type)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#get_qualification_type)
        """

    def list_assignments_for_hit(
        self, **kwargs: Unpack[ListAssignmentsForHITRequestRequestTypeDef]
    ) -> ListAssignmentsForHITResponseTypeDef:
        """
        The `ListAssignmentsForHIT` operation retrieves completed assignments for a HIT.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.list_assignments_for_hit)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#list_assignments_for_hit)
        """

    def list_bonus_payments(
        self, **kwargs: Unpack[ListBonusPaymentsRequestRequestTypeDef]
    ) -> ListBonusPaymentsResponseTypeDef:
        """
        The `ListBonusPayments` operation retrieves the amounts of bonuses you have
        paid to Workers for a given HIT or
        assignment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.list_bonus_payments)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#list_bonus_payments)
        """

    def list_hits(self, **kwargs: Unpack[ListHITsRequestRequestTypeDef]) -> ListHITsResponseTypeDef:
        """
        The `ListHITs` operation returns all of a Requester's HITs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.list_hits)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#list_hits)
        """

    def list_hits_for_qualification_type(
        self, **kwargs: Unpack[ListHITsForQualificationTypeRequestRequestTypeDef]
    ) -> ListHITsForQualificationTypeResponseTypeDef:
        """
        The `ListHITsForQualificationType` operation returns the HITs that use the
        given Qualification type for a Qualification
        requirement.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.list_hits_for_qualification_type)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#list_hits_for_qualification_type)
        """

    def list_qualification_requests(
        self, **kwargs: Unpack[ListQualificationRequestsRequestRequestTypeDef]
    ) -> ListQualificationRequestsResponseTypeDef:
        """
        The `ListQualificationRequests` operation retrieves requests for Qualifications
        of a particular Qualification
        type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.list_qualification_requests)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#list_qualification_requests)
        """

    def list_qualification_types(
        self, **kwargs: Unpack[ListQualificationTypesRequestRequestTypeDef]
    ) -> ListQualificationTypesResponseTypeDef:
        """
        The `ListQualificationTypes` operation returns a list of Qualification types,
        filtered by an optional search
        term.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.list_qualification_types)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#list_qualification_types)
        """

    def list_review_policy_results_for_hit(
        self, **kwargs: Unpack[ListReviewPolicyResultsForHITRequestRequestTypeDef]
    ) -> ListReviewPolicyResultsForHITResponseTypeDef:
        """
        The `ListReviewPolicyResultsForHIT` operation retrieves the computed results
        and the actions taken in the course of executing your Review Policies for a
        given
        HIT.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.list_review_policy_results_for_hit)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#list_review_policy_results_for_hit)
        """

    def list_reviewable_hits(
        self, **kwargs: Unpack[ListReviewableHITsRequestRequestTypeDef]
    ) -> ListReviewableHITsResponseTypeDef:
        """
        The `ListReviewableHITs` operation retrieves the HITs with Status equal to
        Reviewable or Status equal to Reviewing that belong to the Requester calling
        the
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.list_reviewable_hits)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#list_reviewable_hits)
        """

    def list_worker_blocks(
        self, **kwargs: Unpack[ListWorkerBlocksRequestRequestTypeDef]
    ) -> ListWorkerBlocksResponseTypeDef:
        """
        The `ListWorkersBlocks` operation retrieves a list of Workers who are blocked
        from working on your
        HITs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.list_worker_blocks)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#list_worker_blocks)
        """

    def list_workers_with_qualification_type(
        self, **kwargs: Unpack[ListWorkersWithQualificationTypeRequestRequestTypeDef]
    ) -> ListWorkersWithQualificationTypeResponseTypeDef:
        """
        The `ListWorkersWithQualificationType` operation returns all of the Workers
        that have been associated with a given Qualification
        type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.list_workers_with_qualification_type)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#list_workers_with_qualification_type)
        """

    def notify_workers(
        self, **kwargs: Unpack[NotifyWorkersRequestRequestTypeDef]
    ) -> NotifyWorkersResponseTypeDef:
        """
        The `NotifyWorkers` operation sends an email to one or more Workers that you
        specify with the Worker
        ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.notify_workers)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#notify_workers)
        """

    def reject_assignment(
        self, **kwargs: Unpack[RejectAssignmentRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        The `RejectAssignment` operation rejects the results of a completed assignment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.reject_assignment)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#reject_assignment)
        """

    def reject_qualification_request(
        self, **kwargs: Unpack[RejectQualificationRequestRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        The `RejectQualificationRequest` operation rejects a user's request for a
        Qualification.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.reject_qualification_request)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#reject_qualification_request)
        """

    def send_bonus(self, **kwargs: Unpack[SendBonusRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        The `SendBonus` operation issues a payment of money from your account to a
        Worker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.send_bonus)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#send_bonus)
        """

    def send_test_event_notification(
        self, **kwargs: Unpack[SendTestEventNotificationRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        The `SendTestEventNotification` operation causes Amazon Mechanical Turk to send
        a notification message as if a HIT event occurred, according to the provided
        notification
        specification.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.send_test_event_notification)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#send_test_event_notification)
        """

    def update_expiration_for_hit(
        self, **kwargs: Unpack[UpdateExpirationForHITRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        The `UpdateExpirationForHIT` operation allows you update the expiration time of
        a
        HIT.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.update_expiration_for_hit)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#update_expiration_for_hit)
        """

    def update_hit_review_status(
        self, **kwargs: Unpack[UpdateHITReviewStatusRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        The `UpdateHITReviewStatus` operation updates the status of a HIT.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.update_hit_review_status)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#update_hit_review_status)
        """

    def update_hit_type_of_hit(
        self, **kwargs: Unpack[UpdateHITTypeOfHITRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        The `UpdateHITTypeOfHIT` operation allows you to change the HITType properties
        of a
        HIT.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.update_hit_type_of_hit)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#update_hit_type_of_hit)
        """

    def update_notification_settings(
        self, **kwargs: Unpack[UpdateNotificationSettingsRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        The `UpdateNotificationSettings` operation creates, updates, disables or
        re-enables notifications for a HIT
        type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.update_notification_settings)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#update_notification_settings)
        """

    def update_qualification_type(
        self, **kwargs: Unpack[UpdateQualificationTypeRequestRequestTypeDef]
    ) -> UpdateQualificationTypeResponseTypeDef:
        """
        The `UpdateQualificationType` operation modifies the attributes of an existing
        Qualification type, which is represented by a QualificationType data
        structure.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.update_qualification_type)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#update_qualification_type)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_assignments_for_hit"]
    ) -> ListAssignmentsForHITPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_bonus_payments"]
    ) -> ListBonusPaymentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_hits"]) -> ListHITsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_hits_for_qualification_type"]
    ) -> ListHITsForQualificationTypePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_qualification_requests"]
    ) -> ListQualificationRequestsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_qualification_types"]
    ) -> ListQualificationTypesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_reviewable_hits"]
    ) -> ListReviewableHITsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_worker_blocks"]
    ) -> ListWorkerBlocksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_workers_with_qualification_type"]
    ) -> ListWorkersWithQualificationTypePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/client/#get_paginator)
        """
