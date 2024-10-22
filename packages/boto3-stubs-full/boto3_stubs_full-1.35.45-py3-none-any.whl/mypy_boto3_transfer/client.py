"""
Type annotations for transfer service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_transfer.client import TransferClient

    session = Session()
    client: TransferClient = session.client("transfer")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    ListAccessesPaginator,
    ListAgreementsPaginator,
    ListCertificatesPaginator,
    ListConnectorsPaginator,
    ListExecutionsPaginator,
    ListFileTransferResultsPaginator,
    ListProfilesPaginator,
    ListSecurityPoliciesPaginator,
    ListServersPaginator,
    ListTagsForResourcePaginator,
    ListUsersPaginator,
    ListWorkflowsPaginator,
)
from .type_defs import (
    CreateAccessRequestRequestTypeDef,
    CreateAccessResponseTypeDef,
    CreateAgreementRequestRequestTypeDef,
    CreateAgreementResponseTypeDef,
    CreateConnectorRequestRequestTypeDef,
    CreateConnectorResponseTypeDef,
    CreateProfileRequestRequestTypeDef,
    CreateProfileResponseTypeDef,
    CreateServerRequestRequestTypeDef,
    CreateServerResponseTypeDef,
    CreateUserRequestRequestTypeDef,
    CreateUserResponseTypeDef,
    CreateWorkflowRequestRequestTypeDef,
    CreateWorkflowResponseTypeDef,
    DeleteAccessRequestRequestTypeDef,
    DeleteAgreementRequestRequestTypeDef,
    DeleteCertificateRequestRequestTypeDef,
    DeleteConnectorRequestRequestTypeDef,
    DeleteHostKeyRequestRequestTypeDef,
    DeleteProfileRequestRequestTypeDef,
    DeleteServerRequestRequestTypeDef,
    DeleteSshPublicKeyRequestRequestTypeDef,
    DeleteUserRequestRequestTypeDef,
    DeleteWorkflowRequestRequestTypeDef,
    DescribeAccessRequestRequestTypeDef,
    DescribeAccessResponseTypeDef,
    DescribeAgreementRequestRequestTypeDef,
    DescribeAgreementResponseTypeDef,
    DescribeCertificateRequestRequestTypeDef,
    DescribeCertificateResponseTypeDef,
    DescribeConnectorRequestRequestTypeDef,
    DescribeConnectorResponseTypeDef,
    DescribeExecutionRequestRequestTypeDef,
    DescribeExecutionResponseTypeDef,
    DescribeHostKeyRequestRequestTypeDef,
    DescribeHostKeyResponseTypeDef,
    DescribeProfileRequestRequestTypeDef,
    DescribeProfileResponseTypeDef,
    DescribeSecurityPolicyRequestRequestTypeDef,
    DescribeSecurityPolicyResponseTypeDef,
    DescribeServerRequestRequestTypeDef,
    DescribeServerResponseTypeDef,
    DescribeUserRequestRequestTypeDef,
    DescribeUserResponseTypeDef,
    DescribeWorkflowRequestRequestTypeDef,
    DescribeWorkflowResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    ImportCertificateRequestRequestTypeDef,
    ImportCertificateResponseTypeDef,
    ImportHostKeyRequestRequestTypeDef,
    ImportHostKeyResponseTypeDef,
    ImportSshPublicKeyRequestRequestTypeDef,
    ImportSshPublicKeyResponseTypeDef,
    ListAccessesRequestRequestTypeDef,
    ListAccessesResponseTypeDef,
    ListAgreementsRequestRequestTypeDef,
    ListAgreementsResponseTypeDef,
    ListCertificatesRequestRequestTypeDef,
    ListCertificatesResponseTypeDef,
    ListConnectorsRequestRequestTypeDef,
    ListConnectorsResponseTypeDef,
    ListExecutionsRequestRequestTypeDef,
    ListExecutionsResponseTypeDef,
    ListFileTransferResultsRequestRequestTypeDef,
    ListFileTransferResultsResponseTypeDef,
    ListHostKeysRequestRequestTypeDef,
    ListHostKeysResponseTypeDef,
    ListProfilesRequestRequestTypeDef,
    ListProfilesResponseTypeDef,
    ListSecurityPoliciesRequestRequestTypeDef,
    ListSecurityPoliciesResponseTypeDef,
    ListServersRequestRequestTypeDef,
    ListServersResponseTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUsersRequestRequestTypeDef,
    ListUsersResponseTypeDef,
    ListWorkflowsRequestRequestTypeDef,
    ListWorkflowsResponseTypeDef,
    SendWorkflowStepStateRequestRequestTypeDef,
    StartDirectoryListingRequestRequestTypeDef,
    StartDirectoryListingResponseTypeDef,
    StartFileTransferRequestRequestTypeDef,
    StartFileTransferResponseTypeDef,
    StartServerRequestRequestTypeDef,
    StopServerRequestRequestTypeDef,
    TagResourceRequestRequestTypeDef,
    TestConnectionRequestRequestTypeDef,
    TestConnectionResponseTypeDef,
    TestIdentityProviderRequestRequestTypeDef,
    TestIdentityProviderResponseTypeDef,
    UntagResourceRequestRequestTypeDef,
    UpdateAccessRequestRequestTypeDef,
    UpdateAccessResponseTypeDef,
    UpdateAgreementRequestRequestTypeDef,
    UpdateAgreementResponseTypeDef,
    UpdateCertificateRequestRequestTypeDef,
    UpdateCertificateResponseTypeDef,
    UpdateConnectorRequestRequestTypeDef,
    UpdateConnectorResponseTypeDef,
    UpdateHostKeyRequestRequestTypeDef,
    UpdateHostKeyResponseTypeDef,
    UpdateProfileRequestRequestTypeDef,
    UpdateProfileResponseTypeDef,
    UpdateServerRequestRequestTypeDef,
    UpdateServerResponseTypeDef,
    UpdateUserRequestRequestTypeDef,
    UpdateUserResponseTypeDef,
)
from .waiter import ServerOfflineWaiter, ServerOnlineWaiter

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack


__all__ = ("TransferClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServiceError: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    ResourceExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]


class TransferClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        TransferClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#close)
        """

    def create_access(
        self, **kwargs: Unpack[CreateAccessRequestRequestTypeDef]
    ) -> CreateAccessResponseTypeDef:
        """
        Used by administrators to choose which groups in the directory should have
        access to upload and download files over the enabled protocols using Transfer
        Family.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.create_access)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#create_access)
        """

    def create_agreement(
        self, **kwargs: Unpack[CreateAgreementRequestRequestTypeDef]
    ) -> CreateAgreementResponseTypeDef:
        """
        Creates an agreement.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.create_agreement)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#create_agreement)
        """

    def create_connector(
        self, **kwargs: Unpack[CreateConnectorRequestRequestTypeDef]
    ) -> CreateConnectorResponseTypeDef:
        """
        Creates the connector, which captures the parameters for a connection for the
        AS2 or SFTP
        protocol.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.create_connector)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#create_connector)
        """

    def create_profile(
        self, **kwargs: Unpack[CreateProfileRequestRequestTypeDef]
    ) -> CreateProfileResponseTypeDef:
        """
        Creates the local or partner profile to use for AS2 transfers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.create_profile)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#create_profile)
        """

    def create_server(
        self, **kwargs: Unpack[CreateServerRequestRequestTypeDef]
    ) -> CreateServerResponseTypeDef:
        """
        Instantiates an auto-scaling virtual server based on the selected file transfer
        protocol in Amazon Web
        Services.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.create_server)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#create_server)
        """

    def create_user(
        self, **kwargs: Unpack[CreateUserRequestRequestTypeDef]
    ) -> CreateUserResponseTypeDef:
        """
        Creates a user and associates them with an existing file transfer
        protocol-enabled
        server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.create_user)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#create_user)
        """

    def create_workflow(
        self, **kwargs: Unpack[CreateWorkflowRequestRequestTypeDef]
    ) -> CreateWorkflowResponseTypeDef:
        """
        Allows you to create a workflow with specified steps and step details the
        workflow invokes after file transfer
        completes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.create_workflow)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#create_workflow)
        """

    def delete_access(
        self, **kwargs: Unpack[DeleteAccessRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Allows you to delete the access specified in the `ServerID` and `ExternalID`
        parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.delete_access)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#delete_access)
        """

    def delete_agreement(
        self, **kwargs: Unpack[DeleteAgreementRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Delete the agreement that's specified in the provided `AgreementId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.delete_agreement)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#delete_agreement)
        """

    def delete_certificate(
        self, **kwargs: Unpack[DeleteCertificateRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the certificate that's specified in the `CertificateId` parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.delete_certificate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#delete_certificate)
        """

    def delete_connector(
        self, **kwargs: Unpack[DeleteConnectorRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the connector that's specified in the provided `ConnectorId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.delete_connector)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#delete_connector)
        """

    def delete_host_key(
        self, **kwargs: Unpack[DeleteHostKeyRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the host key that's specified in the `HostKeyId` parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.delete_host_key)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#delete_host_key)
        """

    def delete_profile(
        self, **kwargs: Unpack[DeleteProfileRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the profile that's specified in the `ProfileId` parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.delete_profile)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#delete_profile)
        """

    def delete_server(
        self, **kwargs: Unpack[DeleteServerRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the file transfer protocol-enabled server that you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.delete_server)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#delete_server)
        """

    def delete_ssh_public_key(
        self, **kwargs: Unpack[DeleteSshPublicKeyRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a user's Secure Shell (SSH) public key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.delete_ssh_public_key)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#delete_ssh_public_key)
        """

    def delete_user(
        self, **kwargs: Unpack[DeleteUserRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the user belonging to a file transfer protocol-enabled server you
        specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.delete_user)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#delete_user)
        """

    def delete_workflow(
        self, **kwargs: Unpack[DeleteWorkflowRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.delete_workflow)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#delete_workflow)
        """

    def describe_access(
        self, **kwargs: Unpack[DescribeAccessRequestRequestTypeDef]
    ) -> DescribeAccessResponseTypeDef:
        """
        Describes the access that is assigned to the specific file transfer
        protocol-enabled server, as identified by its `ServerId` property and its
        `ExternalId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.describe_access)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#describe_access)
        """

    def describe_agreement(
        self, **kwargs: Unpack[DescribeAgreementRequestRequestTypeDef]
    ) -> DescribeAgreementResponseTypeDef:
        """
        Describes the agreement that's identified by the `AgreementId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.describe_agreement)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#describe_agreement)
        """

    def describe_certificate(
        self, **kwargs: Unpack[DescribeCertificateRequestRequestTypeDef]
    ) -> DescribeCertificateResponseTypeDef:
        """
        Describes the certificate that's identified by the `CertificateId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.describe_certificate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#describe_certificate)
        """

    def describe_connector(
        self, **kwargs: Unpack[DescribeConnectorRequestRequestTypeDef]
    ) -> DescribeConnectorResponseTypeDef:
        """
        Describes the connector that's identified by the `ConnectorId.` See also: [AWS
        API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/transfer-2018-11-05/DescribeConnector).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.describe_connector)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#describe_connector)
        """

    def describe_execution(
        self, **kwargs: Unpack[DescribeExecutionRequestRequestTypeDef]
    ) -> DescribeExecutionResponseTypeDef:
        """
        You can use `DescribeExecution` to check the details of the execution of the
        specified
        workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.describe_execution)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#describe_execution)
        """

    def describe_host_key(
        self, **kwargs: Unpack[DescribeHostKeyRequestRequestTypeDef]
    ) -> DescribeHostKeyResponseTypeDef:
        """
        Returns the details of the host key that's specified by the `HostKeyId` and
        `ServerId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.describe_host_key)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#describe_host_key)
        """

    def describe_profile(
        self, **kwargs: Unpack[DescribeProfileRequestRequestTypeDef]
    ) -> DescribeProfileResponseTypeDef:
        """
        Returns the details of the profile that's specified by the `ProfileId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.describe_profile)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#describe_profile)
        """

    def describe_security_policy(
        self, **kwargs: Unpack[DescribeSecurityPolicyRequestRequestTypeDef]
    ) -> DescribeSecurityPolicyResponseTypeDef:
        """
        Describes the security policy that is attached to your server or SFTP connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.describe_security_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#describe_security_policy)
        """

    def describe_server(
        self, **kwargs: Unpack[DescribeServerRequestRequestTypeDef]
    ) -> DescribeServerResponseTypeDef:
        """
        Describes a file transfer protocol-enabled server that you specify by passing
        the `ServerId`
        parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.describe_server)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#describe_server)
        """

    def describe_user(
        self, **kwargs: Unpack[DescribeUserRequestRequestTypeDef]
    ) -> DescribeUserResponseTypeDef:
        """
        Describes the user assigned to the specific file transfer protocol-enabled
        server, as identified by its `ServerId`
        property.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.describe_user)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#describe_user)
        """

    def describe_workflow(
        self, **kwargs: Unpack[DescribeWorkflowRequestRequestTypeDef]
    ) -> DescribeWorkflowResponseTypeDef:
        """
        Describes the specified workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.describe_workflow)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#describe_workflow)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#generate_presigned_url)
        """

    def import_certificate(
        self, **kwargs: Unpack[ImportCertificateRequestRequestTypeDef]
    ) -> ImportCertificateResponseTypeDef:
        """
        Imports the signing and encryption certificates that you need to create local
        (AS2) profiles and partner
        profiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.import_certificate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#import_certificate)
        """

    def import_host_key(
        self, **kwargs: Unpack[ImportHostKeyRequestRequestTypeDef]
    ) -> ImportHostKeyResponseTypeDef:
        """
        Adds a host key to the server that's specified by the `ServerId` parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.import_host_key)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#import_host_key)
        """

    def import_ssh_public_key(
        self, **kwargs: Unpack[ImportSshPublicKeyRequestRequestTypeDef]
    ) -> ImportSshPublicKeyResponseTypeDef:
        """
        Adds a Secure Shell (SSH) public key to a Transfer Family user identified by a
        `UserName` value assigned to the specific file transfer protocol-enabled
        server, identified by
        `ServerId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.import_ssh_public_key)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#import_ssh_public_key)
        """

    def list_accesses(
        self, **kwargs: Unpack[ListAccessesRequestRequestTypeDef]
    ) -> ListAccessesResponseTypeDef:
        """
        Lists the details for all the accesses you have on your server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.list_accesses)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#list_accesses)
        """

    def list_agreements(
        self, **kwargs: Unpack[ListAgreementsRequestRequestTypeDef]
    ) -> ListAgreementsResponseTypeDef:
        """
        Returns a list of the agreements for the server that's identified by the
        `ServerId` that you
        supply.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.list_agreements)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#list_agreements)
        """

    def list_certificates(
        self, **kwargs: Unpack[ListCertificatesRequestRequestTypeDef]
    ) -> ListCertificatesResponseTypeDef:
        """
        Returns a list of the current certificates that have been imported into
        Transfer
        Family.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.list_certificates)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#list_certificates)
        """

    def list_connectors(
        self, **kwargs: Unpack[ListConnectorsRequestRequestTypeDef]
    ) -> ListConnectorsResponseTypeDef:
        """
        Lists the connectors for the specified Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.list_connectors)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#list_connectors)
        """

    def list_executions(
        self, **kwargs: Unpack[ListExecutionsRequestRequestTypeDef]
    ) -> ListExecutionsResponseTypeDef:
        """
        Lists all in-progress executions for the specified workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.list_executions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#list_executions)
        """

    def list_file_transfer_results(
        self, **kwargs: Unpack[ListFileTransferResultsRequestRequestTypeDef]
    ) -> ListFileTransferResultsResponseTypeDef:
        """
        Returns real-time updates and detailed information on the status of each
        individual file being transferred in a specific file transfer
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.list_file_transfer_results)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#list_file_transfer_results)
        """

    def list_host_keys(
        self, **kwargs: Unpack[ListHostKeysRequestRequestTypeDef]
    ) -> ListHostKeysResponseTypeDef:
        """
        Returns a list of host keys for the server that's specified by the `ServerId`
        parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.list_host_keys)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#list_host_keys)
        """

    def list_profiles(
        self, **kwargs: Unpack[ListProfilesRequestRequestTypeDef]
    ) -> ListProfilesResponseTypeDef:
        """
        Returns a list of the profiles for your system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.list_profiles)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#list_profiles)
        """

    def list_security_policies(
        self, **kwargs: Unpack[ListSecurityPoliciesRequestRequestTypeDef]
    ) -> ListSecurityPoliciesResponseTypeDef:
        """
        Lists the security policies that are attached to your servers and SFTP
        connectors.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.list_security_policies)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#list_security_policies)
        """

    def list_servers(
        self, **kwargs: Unpack[ListServersRequestRequestTypeDef]
    ) -> ListServersResponseTypeDef:
        """
        Lists the file transfer protocol-enabled servers that are associated with your
        Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.list_servers)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#list_servers)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all of the tags associated with the Amazon Resource Name (ARN) that you
        specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.list_tags_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#list_tags_for_resource)
        """

    def list_users(
        self, **kwargs: Unpack[ListUsersRequestRequestTypeDef]
    ) -> ListUsersResponseTypeDef:
        """
        Lists the users for a file transfer protocol-enabled server that you specify by
        passing the `ServerId`
        parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.list_users)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#list_users)
        """

    def list_workflows(
        self, **kwargs: Unpack[ListWorkflowsRequestRequestTypeDef]
    ) -> ListWorkflowsResponseTypeDef:
        """
        Lists all workflows associated with your Amazon Web Services account for your
        current
        region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.list_workflows)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#list_workflows)
        """

    def send_workflow_step_state(
        self, **kwargs: Unpack[SendWorkflowStepStateRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Sends a callback for asynchronous custom steps.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.send_workflow_step_state)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#send_workflow_step_state)
        """

    def start_directory_listing(
        self, **kwargs: Unpack[StartDirectoryListingRequestRequestTypeDef]
    ) -> StartDirectoryListingResponseTypeDef:
        """
        Retrieves a list of the contents of a directory from a remote SFTP server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.start_directory_listing)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#start_directory_listing)
        """

    def start_file_transfer(
        self, **kwargs: Unpack[StartFileTransferRequestRequestTypeDef]
    ) -> StartFileTransferResponseTypeDef:
        """
        Begins a file transfer between local Amazon Web Services storage and a remote
        AS2 or SFTP
        server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.start_file_transfer)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#start_file_transfer)
        """

    def start_server(
        self, **kwargs: Unpack[StartServerRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Changes the state of a file transfer protocol-enabled server from `OFFLINE` to
        `ONLINE`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.start_server)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#start_server)
        """

    def stop_server(
        self, **kwargs: Unpack[StopServerRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Changes the state of a file transfer protocol-enabled server from `ONLINE` to
        `OFFLINE`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.stop_server)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#stop_server)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Attaches a key-value pair to a resource, as identified by its Amazon Resource
        Name
        (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#tag_resource)
        """

    def test_connection(
        self, **kwargs: Unpack[TestConnectionRequestRequestTypeDef]
    ) -> TestConnectionResponseTypeDef:
        """
        Tests whether your SFTP connector is set up successfully.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.test_connection)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#test_connection)
        """

    def test_identity_provider(
        self, **kwargs: Unpack[TestIdentityProviderRequestRequestTypeDef]
    ) -> TestIdentityProviderResponseTypeDef:
        """
        If the `IdentityProviderType` of a file transfer protocol-enabled server is
        `AWS_DIRECTORY_SERVICE` or `API_Gateway`, tests whether your identity provider
        is set up
        successfully.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.test_identity_provider)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#test_identity_provider)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Detaches a key-value pair from a resource, as identified by its Amazon Resource
        Name
        (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#untag_resource)
        """

    def update_access(
        self, **kwargs: Unpack[UpdateAccessRequestRequestTypeDef]
    ) -> UpdateAccessResponseTypeDef:
        """
        Allows you to update parameters for the access specified in the `ServerID` and
        `ExternalID`
        parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.update_access)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#update_access)
        """

    def update_agreement(
        self, **kwargs: Unpack[UpdateAgreementRequestRequestTypeDef]
    ) -> UpdateAgreementResponseTypeDef:
        """
        Updates some of the parameters for an existing agreement.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.update_agreement)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#update_agreement)
        """

    def update_certificate(
        self, **kwargs: Unpack[UpdateCertificateRequestRequestTypeDef]
    ) -> UpdateCertificateResponseTypeDef:
        """
        Updates the active and inactive dates for a certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.update_certificate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#update_certificate)
        """

    def update_connector(
        self, **kwargs: Unpack[UpdateConnectorRequestRequestTypeDef]
    ) -> UpdateConnectorResponseTypeDef:
        """
        Updates some of the parameters for an existing connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.update_connector)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#update_connector)
        """

    def update_host_key(
        self, **kwargs: Unpack[UpdateHostKeyRequestRequestTypeDef]
    ) -> UpdateHostKeyResponseTypeDef:
        """
        Updates the description for the host key that's specified by the `ServerId` and
        `HostKeyId`
        parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.update_host_key)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#update_host_key)
        """

    def update_profile(
        self, **kwargs: Unpack[UpdateProfileRequestRequestTypeDef]
    ) -> UpdateProfileResponseTypeDef:
        """
        Updates some of the parameters for an existing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.update_profile)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#update_profile)
        """

    def update_server(
        self, **kwargs: Unpack[UpdateServerRequestRequestTypeDef]
    ) -> UpdateServerResponseTypeDef:
        """
        Updates the file transfer protocol-enabled server's properties after that
        server has been
        created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.update_server)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#update_server)
        """

    def update_user(
        self, **kwargs: Unpack[UpdateUserRequestRequestTypeDef]
    ) -> UpdateUserResponseTypeDef:
        """
        Assigns new properties to a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.update_user)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#update_user)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_accesses"]) -> ListAccessesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_agreements"]) -> ListAgreementsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_certificates"]
    ) -> ListCertificatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_connectors"]) -> ListConnectorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_executions"]) -> ListExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_file_transfer_results"]
    ) -> ListFileTransferResultsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_profiles"]) -> ListProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_security_policies"]
    ) -> ListSecurityPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_servers"]) -> ListServersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_users"]) -> ListUsersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_workflows"]) -> ListWorkflowsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#get_paginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["server_offline"]) -> ServerOfflineWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["server_online"]) -> ServerOnlineWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transfer.html#Transfer.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/client/#get_waiter)
        """
