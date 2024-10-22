"""
Type annotations for glacier service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_glacier.client import GlacierClient

    session = Session()
    client: GlacierClient = session.client("glacier")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    ListJobsPaginator,
    ListMultipartUploadsPaginator,
    ListPartsPaginator,
    ListVaultsPaginator,
)
from .type_defs import (
    AbortMultipartUploadInputRequestTypeDef,
    AbortVaultLockInputRequestTypeDef,
    AddTagsToVaultInputRequestTypeDef,
    ArchiveCreationOutputTypeDef,
    CompleteMultipartUploadInputRequestTypeDef,
    CompleteVaultLockInputRequestTypeDef,
    CreateVaultInputRequestTypeDef,
    CreateVaultOutputTypeDef,
    DeleteArchiveInputRequestTypeDef,
    DeleteVaultAccessPolicyInputRequestTypeDef,
    DeleteVaultInputRequestTypeDef,
    DeleteVaultNotificationsInputRequestTypeDef,
    DescribeJobInputRequestTypeDef,
    DescribeVaultInputRequestTypeDef,
    DescribeVaultResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    GetDataRetrievalPolicyInputRequestTypeDef,
    GetDataRetrievalPolicyOutputTypeDef,
    GetJobOutputInputRequestTypeDef,
    GetJobOutputOutputTypeDef,
    GetVaultAccessPolicyInputRequestTypeDef,
    GetVaultAccessPolicyOutputTypeDef,
    GetVaultLockInputRequestTypeDef,
    GetVaultLockOutputTypeDef,
    GetVaultNotificationsInputRequestTypeDef,
    GetVaultNotificationsOutputTypeDef,
    GlacierJobDescriptionResponseTypeDef,
    InitiateJobInputRequestTypeDef,
    InitiateJobOutputTypeDef,
    InitiateMultipartUploadInputRequestTypeDef,
    InitiateMultipartUploadOutputTypeDef,
    InitiateVaultLockInputRequestTypeDef,
    InitiateVaultLockOutputTypeDef,
    ListJobsInputRequestTypeDef,
    ListJobsOutputTypeDef,
    ListMultipartUploadsInputRequestTypeDef,
    ListMultipartUploadsOutputTypeDef,
    ListPartsInputRequestTypeDef,
    ListPartsOutputTypeDef,
    ListProvisionedCapacityInputRequestTypeDef,
    ListProvisionedCapacityOutputTypeDef,
    ListTagsForVaultInputRequestTypeDef,
    ListTagsForVaultOutputTypeDef,
    ListVaultsInputRequestTypeDef,
    ListVaultsOutputTypeDef,
    PurchaseProvisionedCapacityInputRequestTypeDef,
    PurchaseProvisionedCapacityOutputTypeDef,
    RemoveTagsFromVaultInputRequestTypeDef,
    SetDataRetrievalPolicyInputRequestTypeDef,
    SetVaultAccessPolicyInputRequestTypeDef,
    SetVaultNotificationsInputRequestTypeDef,
    UploadArchiveInputRequestTypeDef,
    UploadMultipartPartInputRequestTypeDef,
    UploadMultipartPartOutputTypeDef,
)
from .waiter import VaultExistsWaiter, VaultNotExistsWaiter

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("GlacierClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    InsufficientCapacityException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MissingParameterValueException: Type[BotocoreClientError]
    PolicyEnforcedException: Type[BotocoreClientError]
    RequestTimeoutException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]

class GlacierClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        GlacierClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#exceptions)
        """

    def abort_multipart_upload(
        self, **kwargs: Unpack[AbortMultipartUploadInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation aborts a multipart upload identified by the upload ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.abort_multipart_upload)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#abort_multipart_upload)
        """

    def abort_vault_lock(
        self, **kwargs: Unpack[AbortVaultLockInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation aborts the vault locking process if the vault lock is not in the
        `Locked`
        state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.abort_vault_lock)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#abort_vault_lock)
        """

    def add_tags_to_vault(
        self, **kwargs: Unpack[AddTagsToVaultInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation adds the specified tags to a vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.add_tags_to_vault)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#add_tags_to_vault)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#close)
        """

    def complete_multipart_upload(
        self, **kwargs: Unpack[CompleteMultipartUploadInputRequestTypeDef]
    ) -> ArchiveCreationOutputTypeDef:
        """
        You call this operation to inform Amazon S3 Glacier (Glacier) that all the
        archive parts have been uploaded and that Glacier can now assemble the archive
        from the uploaded
        parts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.complete_multipart_upload)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#complete_multipart_upload)
        """

    def complete_vault_lock(
        self, **kwargs: Unpack[CompleteVaultLockInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation completes the vault locking process by transitioning the vault
        lock from the `InProgress` state to the `Locked` state, which causes the vault
        lock policy to become
        unchangeable.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.complete_vault_lock)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#complete_vault_lock)
        """

    def create_vault(
        self, **kwargs: Unpack[CreateVaultInputRequestTypeDef]
    ) -> CreateVaultOutputTypeDef:
        """
        This operation creates a new vault with the specified name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.create_vault)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#create_vault)
        """

    def delete_archive(
        self, **kwargs: Unpack[DeleteArchiveInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation deletes an archive from a vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.delete_archive)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#delete_archive)
        """

    def delete_vault(
        self, **kwargs: Unpack[DeleteVaultInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation deletes a vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.delete_vault)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#delete_vault)
        """

    def delete_vault_access_policy(
        self, **kwargs: Unpack[DeleteVaultAccessPolicyInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation deletes the access policy associated with the specified vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.delete_vault_access_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#delete_vault_access_policy)
        """

    def delete_vault_notifications(
        self, **kwargs: Unpack[DeleteVaultNotificationsInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation deletes the notification configuration set for a vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.delete_vault_notifications)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#delete_vault_notifications)
        """

    def describe_job(
        self, **kwargs: Unpack[DescribeJobInputRequestTypeDef]
    ) -> GlacierJobDescriptionResponseTypeDef:
        """
        This operation returns information about a job you previously initiated,
        including the job initiation date, the user who initiated the job, the job
        status code/message and the Amazon SNS topic to notify after Amazon S3 Glacier
        (Glacier) completes the
        job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.describe_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#describe_job)
        """

    def describe_vault(
        self, **kwargs: Unpack[DescribeVaultInputRequestTypeDef]
    ) -> DescribeVaultResponseTypeDef:
        """
        This operation returns information about a vault, including the vault's Amazon
        Resource Name (ARN), the date the vault was created, the number of archives it
        contains, and the total size of all the archives in the
        vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.describe_vault)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#describe_vault)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#generate_presigned_url)
        """

    def get_data_retrieval_policy(
        self, **kwargs: Unpack[GetDataRetrievalPolicyInputRequestTypeDef]
    ) -> GetDataRetrievalPolicyOutputTypeDef:
        """
        This operation returns the current data retrieval policy for the account and
        region specified in the GET
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.get_data_retrieval_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#get_data_retrieval_policy)
        """

    def get_job_output(
        self, **kwargs: Unpack[GetJobOutputInputRequestTypeDef]
    ) -> GetJobOutputOutputTypeDef:
        """
        This operation downloads the output of the job you initiated using  InitiateJob.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.get_job_output)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#get_job_output)
        """

    def get_vault_access_policy(
        self, **kwargs: Unpack[GetVaultAccessPolicyInputRequestTypeDef]
    ) -> GetVaultAccessPolicyOutputTypeDef:
        """
        This operation retrieves the `access-policy` subresource set on the vault; for
        more information on setting this subresource, see [Set Vault Access Policy (PUT
        access-policy)](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-SetVaultAccessPolicy.html).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.get_vault_access_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#get_vault_access_policy)
        """

    def get_vault_lock(
        self, **kwargs: Unpack[GetVaultLockInputRequestTypeDef]
    ) -> GetVaultLockOutputTypeDef:
        """
        This operation retrieves the following attributes from the `lock-policy`
        subresource set on the specified vault: * The vault lock policy set on the
        vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.get_vault_lock)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#get_vault_lock)
        """

    def get_vault_notifications(
        self, **kwargs: Unpack[GetVaultNotificationsInputRequestTypeDef]
    ) -> GetVaultNotificationsOutputTypeDef:
        """
        This operation retrieves the `notification-configuration` subresource of the
        specified
        vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.get_vault_notifications)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#get_vault_notifications)
        """

    def initiate_job(
        self, **kwargs: Unpack[InitiateJobInputRequestTypeDef]
    ) -> InitiateJobOutputTypeDef:
        """
        This operation initiates a job of the specified type, which can be a select, an
        archival retrieval, or a vault
        retrieval.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.initiate_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#initiate_job)
        """

    def initiate_multipart_upload(
        self, **kwargs: Unpack[InitiateMultipartUploadInputRequestTypeDef]
    ) -> InitiateMultipartUploadOutputTypeDef:
        """
        This operation initiates a multipart upload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.initiate_multipart_upload)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#initiate_multipart_upload)
        """

    def initiate_vault_lock(
        self, **kwargs: Unpack[InitiateVaultLockInputRequestTypeDef]
    ) -> InitiateVaultLockOutputTypeDef:
        """
        This operation initiates the vault locking process by doing the following: *
        Installing a vault lock policy on the specified
        vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.initiate_vault_lock)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#initiate_vault_lock)
        """

    def list_jobs(self, **kwargs: Unpack[ListJobsInputRequestTypeDef]) -> ListJobsOutputTypeDef:
        """
        This operation lists jobs for a vault, including jobs that are in-progress and
        jobs that have recently
        finished.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.list_jobs)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#list_jobs)
        """

    def list_multipart_uploads(
        self, **kwargs: Unpack[ListMultipartUploadsInputRequestTypeDef]
    ) -> ListMultipartUploadsOutputTypeDef:
        """
        This operation lists in-progress multipart uploads for the specified vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.list_multipart_uploads)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#list_multipart_uploads)
        """

    def list_parts(self, **kwargs: Unpack[ListPartsInputRequestTypeDef]) -> ListPartsOutputTypeDef:
        """
        This operation lists the parts of an archive that have been uploaded in a
        specific multipart
        upload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.list_parts)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#list_parts)
        """

    def list_provisioned_capacity(
        self, **kwargs: Unpack[ListProvisionedCapacityInputRequestTypeDef]
    ) -> ListProvisionedCapacityOutputTypeDef:
        """
        This operation lists the provisioned capacity units for the specified AWS
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.list_provisioned_capacity)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#list_provisioned_capacity)
        """

    def list_tags_for_vault(
        self, **kwargs: Unpack[ListTagsForVaultInputRequestTypeDef]
    ) -> ListTagsForVaultOutputTypeDef:
        """
        This operation lists all the tags attached to a vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.list_tags_for_vault)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#list_tags_for_vault)
        """

    def list_vaults(
        self, **kwargs: Unpack[ListVaultsInputRequestTypeDef]
    ) -> ListVaultsOutputTypeDef:
        """
        This operation lists all vaults owned by the calling user's account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.list_vaults)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#list_vaults)
        """

    def purchase_provisioned_capacity(
        self, **kwargs: Unpack[PurchaseProvisionedCapacityInputRequestTypeDef]
    ) -> PurchaseProvisionedCapacityOutputTypeDef:
        """
        This operation purchases a provisioned capacity unit for an AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.purchase_provisioned_capacity)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#purchase_provisioned_capacity)
        """

    def remove_tags_from_vault(
        self, **kwargs: Unpack[RemoveTagsFromVaultInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation removes one or more tags from the set of tags attached to a
        vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.remove_tags_from_vault)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#remove_tags_from_vault)
        """

    def set_data_retrieval_policy(
        self, **kwargs: Unpack[SetDataRetrievalPolicyInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation sets and then enacts a data retrieval policy in the region
        specified in the PUT
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.set_data_retrieval_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#set_data_retrieval_policy)
        """

    def set_vault_access_policy(
        self, **kwargs: Unpack[SetVaultAccessPolicyInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation configures an access policy for a vault and will overwrite an
        existing
        policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.set_vault_access_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#set_vault_access_policy)
        """

    def set_vault_notifications(
        self, **kwargs: Unpack[SetVaultNotificationsInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation configures notifications that will be sent when specific events
        happen to a
        vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.set_vault_notifications)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#set_vault_notifications)
        """

    def upload_archive(
        self, **kwargs: Unpack[UploadArchiveInputRequestTypeDef]
    ) -> ArchiveCreationOutputTypeDef:
        """
        This operation adds an archive to a vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.upload_archive)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#upload_archive)
        """

    def upload_multipart_part(
        self, **kwargs: Unpack[UploadMultipartPartInputRequestTypeDef]
    ) -> UploadMultipartPartOutputTypeDef:
        """
        This operation uploads a part of an archive.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.upload_multipart_part)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#upload_multipart_part)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_jobs"]) -> ListJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_multipart_uploads"]
    ) -> ListMultipartUploadsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_parts"]) -> ListPartsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_vaults"]) -> ListVaultsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#get_paginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["vault_exists"]) -> VaultExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["vault_not_exists"]) -> VaultNotExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glacier.html#Glacier.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/client/#get_waiter)
        """
