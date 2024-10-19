"""
Type annotations for organizations service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_organizations.client import OrganizationsClient

    session = Session()
    client: OrganizationsClient = session.client("organizations")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    ListAccountsForParentPaginator,
    ListAccountsPaginator,
    ListAWSServiceAccessForOrganizationPaginator,
    ListChildrenPaginator,
    ListCreateAccountStatusPaginator,
    ListDelegatedAdministratorsPaginator,
    ListDelegatedServicesForAccountPaginator,
    ListHandshakesForAccountPaginator,
    ListHandshakesForOrganizationPaginator,
    ListOrganizationalUnitsForParentPaginator,
    ListParentsPaginator,
    ListPoliciesForTargetPaginator,
    ListPoliciesPaginator,
    ListRootsPaginator,
    ListTagsForResourcePaginator,
    ListTargetsForPolicyPaginator,
)
from .type_defs import (
    AcceptHandshakeRequestRequestTypeDef,
    AcceptHandshakeResponseTypeDef,
    AttachPolicyRequestRequestTypeDef,
    CancelHandshakeRequestRequestTypeDef,
    CancelHandshakeResponseTypeDef,
    CloseAccountRequestRequestTypeDef,
    CreateAccountRequestRequestTypeDef,
    CreateAccountResponseTypeDef,
    CreateGovCloudAccountRequestRequestTypeDef,
    CreateGovCloudAccountResponseTypeDef,
    CreateOrganizationalUnitRequestRequestTypeDef,
    CreateOrganizationalUnitResponseTypeDef,
    CreateOrganizationRequestRequestTypeDef,
    CreateOrganizationResponseTypeDef,
    CreatePolicyRequestRequestTypeDef,
    CreatePolicyResponseTypeDef,
    DeclineHandshakeRequestRequestTypeDef,
    DeclineHandshakeResponseTypeDef,
    DeleteOrganizationalUnitRequestRequestTypeDef,
    DeletePolicyRequestRequestTypeDef,
    DeregisterDelegatedAdministratorRequestRequestTypeDef,
    DescribeAccountRequestRequestTypeDef,
    DescribeAccountResponseTypeDef,
    DescribeCreateAccountStatusRequestRequestTypeDef,
    DescribeCreateAccountStatusResponseTypeDef,
    DescribeEffectivePolicyRequestRequestTypeDef,
    DescribeEffectivePolicyResponseTypeDef,
    DescribeHandshakeRequestRequestTypeDef,
    DescribeHandshakeResponseTypeDef,
    DescribeOrganizationalUnitRequestRequestTypeDef,
    DescribeOrganizationalUnitResponseTypeDef,
    DescribeOrganizationResponseTypeDef,
    DescribePolicyRequestRequestTypeDef,
    DescribePolicyResponseTypeDef,
    DescribeResourcePolicyResponseTypeDef,
    DetachPolicyRequestRequestTypeDef,
    DisableAWSServiceAccessRequestRequestTypeDef,
    DisablePolicyTypeRequestRequestTypeDef,
    DisablePolicyTypeResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    EnableAllFeaturesResponseTypeDef,
    EnableAWSServiceAccessRequestRequestTypeDef,
    EnablePolicyTypeRequestRequestTypeDef,
    EnablePolicyTypeResponseTypeDef,
    InviteAccountToOrganizationRequestRequestTypeDef,
    InviteAccountToOrganizationResponseTypeDef,
    ListAccountsForParentRequestRequestTypeDef,
    ListAccountsForParentResponseTypeDef,
    ListAccountsRequestRequestTypeDef,
    ListAccountsResponseTypeDef,
    ListAWSServiceAccessForOrganizationRequestRequestTypeDef,
    ListAWSServiceAccessForOrganizationResponseTypeDef,
    ListChildrenRequestRequestTypeDef,
    ListChildrenResponseTypeDef,
    ListCreateAccountStatusRequestRequestTypeDef,
    ListCreateAccountStatusResponseTypeDef,
    ListDelegatedAdministratorsRequestRequestTypeDef,
    ListDelegatedAdministratorsResponseTypeDef,
    ListDelegatedServicesForAccountRequestRequestTypeDef,
    ListDelegatedServicesForAccountResponseTypeDef,
    ListHandshakesForAccountRequestRequestTypeDef,
    ListHandshakesForAccountResponseTypeDef,
    ListHandshakesForOrganizationRequestRequestTypeDef,
    ListHandshakesForOrganizationResponseTypeDef,
    ListOrganizationalUnitsForParentRequestRequestTypeDef,
    ListOrganizationalUnitsForParentResponseTypeDef,
    ListParentsRequestRequestTypeDef,
    ListParentsResponseTypeDef,
    ListPoliciesForTargetRequestRequestTypeDef,
    ListPoliciesForTargetResponseTypeDef,
    ListPoliciesRequestRequestTypeDef,
    ListPoliciesResponseTypeDef,
    ListRootsRequestRequestTypeDef,
    ListRootsResponseTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTargetsForPolicyRequestRequestTypeDef,
    ListTargetsForPolicyResponseTypeDef,
    MoveAccountRequestRequestTypeDef,
    PutResourcePolicyRequestRequestTypeDef,
    PutResourcePolicyResponseTypeDef,
    RegisterDelegatedAdministratorRequestRequestTypeDef,
    RemoveAccountFromOrganizationRequestRequestTypeDef,
    TagResourceRequestRequestTypeDef,
    UntagResourceRequestRequestTypeDef,
    UpdateOrganizationalUnitRequestRequestTypeDef,
    UpdateOrganizationalUnitResponseTypeDef,
    UpdatePolicyRequestRequestTypeDef,
    UpdatePolicyResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack


__all__ = ("OrganizationsClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AWSOrganizationsNotInUseException: Type[BotocoreClientError]
    AccessDeniedException: Type[BotocoreClientError]
    AccessDeniedForDependencyException: Type[BotocoreClientError]
    AccountAlreadyClosedException: Type[BotocoreClientError]
    AccountAlreadyRegisteredException: Type[BotocoreClientError]
    AccountNotFoundException: Type[BotocoreClientError]
    AccountNotRegisteredException: Type[BotocoreClientError]
    AccountOwnerNotVerifiedException: Type[BotocoreClientError]
    AlreadyInOrganizationException: Type[BotocoreClientError]
    ChildNotFoundException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ConstraintViolationException: Type[BotocoreClientError]
    CreateAccountStatusNotFoundException: Type[BotocoreClientError]
    DestinationParentNotFoundException: Type[BotocoreClientError]
    DuplicateAccountException: Type[BotocoreClientError]
    DuplicateHandshakeException: Type[BotocoreClientError]
    DuplicateOrganizationalUnitException: Type[BotocoreClientError]
    DuplicatePolicyAttachmentException: Type[BotocoreClientError]
    DuplicatePolicyException: Type[BotocoreClientError]
    EffectivePolicyNotFoundException: Type[BotocoreClientError]
    FinalizingOrganizationException: Type[BotocoreClientError]
    HandshakeAlreadyInStateException: Type[BotocoreClientError]
    HandshakeConstraintViolationException: Type[BotocoreClientError]
    HandshakeNotFoundException: Type[BotocoreClientError]
    InvalidHandshakeTransitionException: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    MalformedPolicyDocumentException: Type[BotocoreClientError]
    MasterCannotLeaveOrganizationException: Type[BotocoreClientError]
    OrganizationNotEmptyException: Type[BotocoreClientError]
    OrganizationalUnitNotEmptyException: Type[BotocoreClientError]
    OrganizationalUnitNotFoundException: Type[BotocoreClientError]
    ParentNotFoundException: Type[BotocoreClientError]
    PolicyChangesInProgressException: Type[BotocoreClientError]
    PolicyInUseException: Type[BotocoreClientError]
    PolicyNotAttachedException: Type[BotocoreClientError]
    PolicyNotFoundException: Type[BotocoreClientError]
    PolicyTypeAlreadyEnabledException: Type[BotocoreClientError]
    PolicyTypeNotAvailableForOrganizationException: Type[BotocoreClientError]
    PolicyTypeNotEnabledException: Type[BotocoreClientError]
    ResourcePolicyNotFoundException: Type[BotocoreClientError]
    RootNotFoundException: Type[BotocoreClientError]
    ServiceException: Type[BotocoreClientError]
    SourceParentNotFoundException: Type[BotocoreClientError]
    TargetNotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnsupportedAPIEndpointException: Type[BotocoreClientError]


class OrganizationsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        OrganizationsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#exceptions)
        """

    def accept_handshake(
        self, **kwargs: Unpack[AcceptHandshakeRequestRequestTypeDef]
    ) -> AcceptHandshakeResponseTypeDef:
        """
        Sends a response to the originator of a handshake agreeing to the action
        proposed by the handshake
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.accept_handshake)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#accept_handshake)
        """

    def attach_policy(
        self, **kwargs: Unpack[AttachPolicyRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Attaches a policy to a root, an organizational unit (OU), or an individual
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.attach_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#attach_policy)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#can_paginate)
        """

    def cancel_handshake(
        self, **kwargs: Unpack[CancelHandshakeRequestRequestTypeDef]
    ) -> CancelHandshakeResponseTypeDef:
        """
        Cancels a handshake.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.cancel_handshake)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#cancel_handshake)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#close)
        """

    def close_account(
        self, **kwargs: Unpack[CloseAccountRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Closes an Amazon Web Services member account within an organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.close_account)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#close_account)
        """

    def create_account(
        self, **kwargs: Unpack[CreateAccountRequestRequestTypeDef]
    ) -> CreateAccountResponseTypeDef:
        """
        Creates an Amazon Web Services account that is automatically a member of the
        organization whose credentials made the
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.create_account)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#create_account)
        """

    def create_gov_cloud_account(
        self, **kwargs: Unpack[CreateGovCloudAccountRequestRequestTypeDef]
    ) -> CreateGovCloudAccountResponseTypeDef:
        """
        This action is available if all of the following are true: * You're authorized
        to create accounts in the Amazon Web Services GovCloud (US)
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.create_gov_cloud_account)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#create_gov_cloud_account)
        """

    def create_organization(
        self, **kwargs: Unpack[CreateOrganizationRequestRequestTypeDef]
    ) -> CreateOrganizationResponseTypeDef:
        """
        Creates an Amazon Web Services organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.create_organization)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#create_organization)
        """

    def create_organizational_unit(
        self, **kwargs: Unpack[CreateOrganizationalUnitRequestRequestTypeDef]
    ) -> CreateOrganizationalUnitResponseTypeDef:
        """
        Creates an organizational unit (OU) within a root or parent OU.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.create_organizational_unit)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#create_organizational_unit)
        """

    def create_policy(
        self, **kwargs: Unpack[CreatePolicyRequestRequestTypeDef]
    ) -> CreatePolicyResponseTypeDef:
        """
        Creates a policy of a specified type that you can attach to a root, an
        organizational unit (OU), or an individual Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.create_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#create_policy)
        """

    def decline_handshake(
        self, **kwargs: Unpack[DeclineHandshakeRequestRequestTypeDef]
    ) -> DeclineHandshakeResponseTypeDef:
        """
        Declines a handshake request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.decline_handshake)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#decline_handshake)
        """

    def delete_organization(self) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.delete_organization)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#delete_organization)
        """

    def delete_organizational_unit(
        self, **kwargs: Unpack[DeleteOrganizationalUnitRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an organizational unit (OU) from a root or another OU.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.delete_organizational_unit)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#delete_organizational_unit)
        """

    def delete_policy(
        self, **kwargs: Unpack[DeletePolicyRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified policy from your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.delete_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#delete_policy)
        """

    def delete_resource_policy(self) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the resource policy from your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.delete_resource_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#delete_resource_policy)
        """

    def deregister_delegated_administrator(
        self, **kwargs: Unpack[DeregisterDelegatedAdministratorRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the specified member Amazon Web Services account as a delegated
        administrator for the specified Amazon Web Services
        service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.deregister_delegated_administrator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#deregister_delegated_administrator)
        """

    def describe_account(
        self, **kwargs: Unpack[DescribeAccountRequestRequestTypeDef]
    ) -> DescribeAccountResponseTypeDef:
        """
        Retrieves Organizations-related information about the specified account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.describe_account)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#describe_account)
        """

    def describe_create_account_status(
        self, **kwargs: Unpack[DescribeCreateAccountStatusRequestRequestTypeDef]
    ) -> DescribeCreateAccountStatusResponseTypeDef:
        """
        Retrieves the current status of an asynchronous request to create an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.describe_create_account_status)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#describe_create_account_status)
        """

    def describe_effective_policy(
        self, **kwargs: Unpack[DescribeEffectivePolicyRequestRequestTypeDef]
    ) -> DescribeEffectivePolicyResponseTypeDef:
        """
        Returns the contents of the effective policy for specified policy type and
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.describe_effective_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#describe_effective_policy)
        """

    def describe_handshake(
        self, **kwargs: Unpack[DescribeHandshakeRequestRequestTypeDef]
    ) -> DescribeHandshakeResponseTypeDef:
        """
        Retrieves information about a previously requested handshake.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.describe_handshake)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#describe_handshake)
        """

    def describe_organization(self) -> DescribeOrganizationResponseTypeDef:
        """
        Retrieves information about the organization that the user's account belongs to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.describe_organization)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#describe_organization)
        """

    def describe_organizational_unit(
        self, **kwargs: Unpack[DescribeOrganizationalUnitRequestRequestTypeDef]
    ) -> DescribeOrganizationalUnitResponseTypeDef:
        """
        Retrieves information about an organizational unit (OU).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.describe_organizational_unit)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#describe_organizational_unit)
        """

    def describe_policy(
        self, **kwargs: Unpack[DescribePolicyRequestRequestTypeDef]
    ) -> DescribePolicyResponseTypeDef:
        """
        Retrieves information about a policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.describe_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#describe_policy)
        """

    def describe_resource_policy(self) -> DescribeResourcePolicyResponseTypeDef:
        """
        Retrieves information about a resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.describe_resource_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#describe_resource_policy)
        """

    def detach_policy(
        self, **kwargs: Unpack[DetachPolicyRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Detaches a policy from a target root, organizational unit (OU), or account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.detach_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#detach_policy)
        """

    def disable_aws_service_access(
        self, **kwargs: Unpack[DisableAWSServiceAccessRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Disables the integration of an Amazon Web Services service (the service that is
        specified by `ServicePrincipal`) with
        Organizations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.disable_aws_service_access)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#disable_aws_service_access)
        """

    def disable_policy_type(
        self, **kwargs: Unpack[DisablePolicyTypeRequestRequestTypeDef]
    ) -> DisablePolicyTypeResponseTypeDef:
        """
        Disables an organizational policy type in a root.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.disable_policy_type)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#disable_policy_type)
        """

    def enable_all_features(self) -> EnableAllFeaturesResponseTypeDef:
        """
        Enables all features in an organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.enable_all_features)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#enable_all_features)
        """

    def enable_aws_service_access(
        self, **kwargs: Unpack[EnableAWSServiceAccessRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Provides an Amazon Web Services service (the service that is specified by
        `ServicePrincipal`) with permissions to view the structure of an organization,
        create a [service-linked
        role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html)
        in all the accounts in
        the...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.enable_aws_service_access)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#enable_aws_service_access)
        """

    def enable_policy_type(
        self, **kwargs: Unpack[EnablePolicyTypeRequestRequestTypeDef]
    ) -> EnablePolicyTypeResponseTypeDef:
        """
        Enables a policy type in a root.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.enable_policy_type)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#enable_policy_type)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#generate_presigned_url)
        """

    def invite_account_to_organization(
        self, **kwargs: Unpack[InviteAccountToOrganizationRequestRequestTypeDef]
    ) -> InviteAccountToOrganizationResponseTypeDef:
        """
        Sends an invitation to another account to join your organization as a member
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.invite_account_to_organization)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#invite_account_to_organization)
        """

    def leave_organization(self) -> EmptyResponseMetadataTypeDef:
        """
        Removes a member account from its parent organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.leave_organization)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#leave_organization)
        """

    def list_accounts(
        self, **kwargs: Unpack[ListAccountsRequestRequestTypeDef]
    ) -> ListAccountsResponseTypeDef:
        """
        Lists all the accounts in the organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_accounts)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#list_accounts)
        """

    def list_accounts_for_parent(
        self, **kwargs: Unpack[ListAccountsForParentRequestRequestTypeDef]
    ) -> ListAccountsForParentResponseTypeDef:
        """
        Lists the accounts in an organization that are contained by the specified
        target root or organizational unit
        (OU).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_accounts_for_parent)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#list_accounts_for_parent)
        """

    def list_aws_service_access_for_organization(
        self, **kwargs: Unpack[ListAWSServiceAccessForOrganizationRequestRequestTypeDef]
    ) -> ListAWSServiceAccessForOrganizationResponseTypeDef:
        """
        Returns a list of the Amazon Web Services services that you enabled to
        integrate with your
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_aws_service_access_for_organization)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#list_aws_service_access_for_organization)
        """

    def list_children(
        self, **kwargs: Unpack[ListChildrenRequestRequestTypeDef]
    ) -> ListChildrenResponseTypeDef:
        """
        Lists all of the organizational units (OUs) or accounts that are contained in
        the specified parent OU or
        root.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_children)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#list_children)
        """

    def list_create_account_status(
        self, **kwargs: Unpack[ListCreateAccountStatusRequestRequestTypeDef]
    ) -> ListCreateAccountStatusResponseTypeDef:
        """
        Lists the account creation requests that match the specified status that is
        currently being tracked for the
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_create_account_status)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#list_create_account_status)
        """

    def list_delegated_administrators(
        self, **kwargs: Unpack[ListDelegatedAdministratorsRequestRequestTypeDef]
    ) -> ListDelegatedAdministratorsResponseTypeDef:
        """
        Lists the Amazon Web Services accounts that are designated as delegated
        administrators in this
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_delegated_administrators)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#list_delegated_administrators)
        """

    def list_delegated_services_for_account(
        self, **kwargs: Unpack[ListDelegatedServicesForAccountRequestRequestTypeDef]
    ) -> ListDelegatedServicesForAccountResponseTypeDef:
        """
        List the Amazon Web Services services for which the specified account is a
        delegated
        administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_delegated_services_for_account)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#list_delegated_services_for_account)
        """

    def list_handshakes_for_account(
        self, **kwargs: Unpack[ListHandshakesForAccountRequestRequestTypeDef]
    ) -> ListHandshakesForAccountResponseTypeDef:
        """
        Lists the current handshakes that are associated with the account of the
        requesting
        user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_handshakes_for_account)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#list_handshakes_for_account)
        """

    def list_handshakes_for_organization(
        self, **kwargs: Unpack[ListHandshakesForOrganizationRequestRequestTypeDef]
    ) -> ListHandshakesForOrganizationResponseTypeDef:
        """
        Lists the handshakes that are associated with the organization that the
        requesting user is part
        of.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_handshakes_for_organization)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#list_handshakes_for_organization)
        """

    def list_organizational_units_for_parent(
        self, **kwargs: Unpack[ListOrganizationalUnitsForParentRequestRequestTypeDef]
    ) -> ListOrganizationalUnitsForParentResponseTypeDef:
        """
        Lists the organizational units (OUs) in a parent organizational unit or root.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_organizational_units_for_parent)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#list_organizational_units_for_parent)
        """

    def list_parents(
        self, **kwargs: Unpack[ListParentsRequestRequestTypeDef]
    ) -> ListParentsResponseTypeDef:
        """
        Lists the root or organizational units (OUs) that serve as the immediate parent
        of the specified child OU or
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_parents)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#list_parents)
        """

    def list_policies(
        self, **kwargs: Unpack[ListPoliciesRequestRequestTypeDef]
    ) -> ListPoliciesResponseTypeDef:
        """
        Retrieves the list of all policies in an organization of a specified type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_policies)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#list_policies)
        """

    def list_policies_for_target(
        self, **kwargs: Unpack[ListPoliciesForTargetRequestRequestTypeDef]
    ) -> ListPoliciesForTargetResponseTypeDef:
        """
        Lists the policies that are directly attached to the specified target root,
        organizational unit (OU), or
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_policies_for_target)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#list_policies_for_target)
        """

    def list_roots(
        self, **kwargs: Unpack[ListRootsRequestRequestTypeDef]
    ) -> ListRootsResponseTypeDef:
        """
        Lists the roots that are defined in the current organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_roots)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#list_roots)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists tags that are attached to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_tags_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#list_tags_for_resource)
        """

    def list_targets_for_policy(
        self, **kwargs: Unpack[ListTargetsForPolicyRequestRequestTypeDef]
    ) -> ListTargetsForPolicyResponseTypeDef:
        """
        Lists all the roots, organizational units (OUs), and accounts that the
        specified policy is attached
        to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.list_targets_for_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#list_targets_for_policy)
        """

    def move_account(
        self, **kwargs: Unpack[MoveAccountRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Moves an account from its current source parent root or organizational unit
        (OU) to the specified destination parent root or
        OU.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.move_account)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#move_account)
        """

    def put_resource_policy(
        self, **kwargs: Unpack[PutResourcePolicyRequestRequestTypeDef]
    ) -> PutResourcePolicyResponseTypeDef:
        """
        Creates or updates a resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.put_resource_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#put_resource_policy)
        """

    def register_delegated_administrator(
        self, **kwargs: Unpack[RegisterDelegatedAdministratorRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Enables the specified member account to administer the Organizations features
        of the specified Amazon Web Services
        service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.register_delegated_administrator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#register_delegated_administrator)
        """

    def remove_account_from_organization(
        self, **kwargs: Unpack[RemoveAccountFromOrganizationRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the specified account from the organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.remove_account_from_organization)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#remove_account_from_organization)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds one or more tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes any tags with the specified keys from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#untag_resource)
        """

    def update_organizational_unit(
        self, **kwargs: Unpack[UpdateOrganizationalUnitRequestRequestTypeDef]
    ) -> UpdateOrganizationalUnitResponseTypeDef:
        """
        Renames the specified organizational unit (OU).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.update_organizational_unit)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#update_organizational_unit)
        """

    def update_policy(
        self, **kwargs: Unpack[UpdatePolicyRequestRequestTypeDef]
    ) -> UpdatePolicyResponseTypeDef:
        """
        Updates an existing policy with a new name, description, or content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.update_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#update_policy)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_aws_service_access_for_organization"]
    ) -> ListAWSServiceAccessForOrganizationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_accounts"]) -> ListAccountsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_accounts_for_parent"]
    ) -> ListAccountsForParentPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_children"]) -> ListChildrenPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_create_account_status"]
    ) -> ListCreateAccountStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_delegated_administrators"]
    ) -> ListDelegatedAdministratorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_delegated_services_for_account"]
    ) -> ListDelegatedServicesForAccountPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_handshakes_for_account"]
    ) -> ListHandshakesForAccountPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_handshakes_for_organization"]
    ) -> ListHandshakesForOrganizationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_organizational_units_for_parent"]
    ) -> ListOrganizationalUnitsForParentPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_parents"]) -> ListParentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_policies"]) -> ListPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_policies_for_target"]
    ) -> ListPoliciesForTargetPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_roots"]) -> ListRootsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_targets_for_policy"]
    ) -> ListTargetsForPolicyPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_organizations/client/#get_paginator)
        """
