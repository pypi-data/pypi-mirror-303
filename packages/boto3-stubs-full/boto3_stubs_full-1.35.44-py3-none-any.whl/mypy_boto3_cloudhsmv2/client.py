"""
Type annotations for cloudhsmv2 service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_cloudhsmv2.client import CloudHSMV2Client

    session = Session()
    client: CloudHSMV2Client = session.client("cloudhsmv2")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import DescribeBackupsPaginator, DescribeClustersPaginator, ListTagsPaginator
from .type_defs import (
    CopyBackupToRegionRequestRequestTypeDef,
    CopyBackupToRegionResponseTypeDef,
    CreateClusterRequestRequestTypeDef,
    CreateClusterResponseTypeDef,
    CreateHsmRequestRequestTypeDef,
    CreateHsmResponseTypeDef,
    DeleteBackupRequestRequestTypeDef,
    DeleteBackupResponseTypeDef,
    DeleteClusterRequestRequestTypeDef,
    DeleteClusterResponseTypeDef,
    DeleteHsmRequestRequestTypeDef,
    DeleteHsmResponseTypeDef,
    DeleteResourcePolicyRequestRequestTypeDef,
    DeleteResourcePolicyResponseTypeDef,
    DescribeBackupsRequestRequestTypeDef,
    DescribeBackupsResponseTypeDef,
    DescribeClustersRequestRequestTypeDef,
    DescribeClustersResponseTypeDef,
    GetResourcePolicyRequestRequestTypeDef,
    GetResourcePolicyResponseTypeDef,
    InitializeClusterRequestRequestTypeDef,
    InitializeClusterResponseTypeDef,
    ListTagsRequestRequestTypeDef,
    ListTagsResponseTypeDef,
    ModifyBackupAttributesRequestRequestTypeDef,
    ModifyBackupAttributesResponseTypeDef,
    ModifyClusterRequestRequestTypeDef,
    ModifyClusterResponseTypeDef,
    PutResourcePolicyRequestRequestTypeDef,
    PutResourcePolicyResponseTypeDef,
    RestoreBackupRequestRequestTypeDef,
    RestoreBackupResponseTypeDef,
    TagResourceRequestRequestTypeDef,
    UntagResourceRequestRequestTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack


__all__ = ("CloudHSMV2Client",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    CloudHsmAccessDeniedException: Type[BotocoreClientError]
    CloudHsmInternalFailureException: Type[BotocoreClientError]
    CloudHsmInvalidRequestException: Type[BotocoreClientError]
    CloudHsmResourceNotFoundException: Type[BotocoreClientError]
    CloudHsmServiceException: Type[BotocoreClientError]
    CloudHsmTagException: Type[BotocoreClientError]


class CloudHSMV2Client(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CloudHSMV2Client exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#close)
        """

    def copy_backup_to_region(
        self, **kwargs: Unpack[CopyBackupToRegionRequestRequestTypeDef]
    ) -> CopyBackupToRegionResponseTypeDef:
        """
        Copy an CloudHSM cluster backup to a different region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.copy_backup_to_region)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#copy_backup_to_region)
        """

    def create_cluster(
        self, **kwargs: Unpack[CreateClusterRequestRequestTypeDef]
    ) -> CreateClusterResponseTypeDef:
        """
        Creates a new CloudHSM cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.create_cluster)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#create_cluster)
        """

    def create_hsm(
        self, **kwargs: Unpack[CreateHsmRequestRequestTypeDef]
    ) -> CreateHsmResponseTypeDef:
        """
        Creates a new hardware security module (HSM) in the specified CloudHSM cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.create_hsm)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#create_hsm)
        """

    def delete_backup(
        self, **kwargs: Unpack[DeleteBackupRequestRequestTypeDef]
    ) -> DeleteBackupResponseTypeDef:
        """
        Deletes a specified CloudHSM backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.delete_backup)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#delete_backup)
        """

    def delete_cluster(
        self, **kwargs: Unpack[DeleteClusterRequestRequestTypeDef]
    ) -> DeleteClusterResponseTypeDef:
        """
        Deletes the specified CloudHSM cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.delete_cluster)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#delete_cluster)
        """

    def delete_hsm(
        self, **kwargs: Unpack[DeleteHsmRequestRequestTypeDef]
    ) -> DeleteHsmResponseTypeDef:
        """
        Deletes the specified HSM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.delete_hsm)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#delete_hsm)
        """

    def delete_resource_policy(
        self, **kwargs: Unpack[DeleteResourcePolicyRequestRequestTypeDef]
    ) -> DeleteResourcePolicyResponseTypeDef:
        """
        Deletes an CloudHSM resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.delete_resource_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#delete_resource_policy)
        """

    def describe_backups(
        self, **kwargs: Unpack[DescribeBackupsRequestRequestTypeDef]
    ) -> DescribeBackupsResponseTypeDef:
        """
        Gets information about backups of CloudHSM clusters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.describe_backups)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#describe_backups)
        """

    def describe_clusters(
        self, **kwargs: Unpack[DescribeClustersRequestRequestTypeDef]
    ) -> DescribeClustersResponseTypeDef:
        """
        Gets information about CloudHSM clusters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.describe_clusters)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#describe_clusters)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#generate_presigned_url)
        """

    def get_resource_policy(
        self, **kwargs: Unpack[GetResourcePolicyRequestRequestTypeDef]
    ) -> GetResourcePolicyResponseTypeDef:
        """
        Retrieves the resource policy document attached to a given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.get_resource_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#get_resource_policy)
        """

    def initialize_cluster(
        self, **kwargs: Unpack[InitializeClusterRequestRequestTypeDef]
    ) -> InitializeClusterResponseTypeDef:
        """
        Claims an CloudHSM cluster by submitting the cluster certificate issued by your
        issuing certificate authority (CA) and the CA's root
        certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.initialize_cluster)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#initialize_cluster)
        """

    def list_tags(self, **kwargs: Unpack[ListTagsRequestRequestTypeDef]) -> ListTagsResponseTypeDef:
        """
        Gets a list of tags for the specified CloudHSM cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.list_tags)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#list_tags)
        """

    def modify_backup_attributes(
        self, **kwargs: Unpack[ModifyBackupAttributesRequestRequestTypeDef]
    ) -> ModifyBackupAttributesResponseTypeDef:
        """
        Modifies attributes for CloudHSM backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.modify_backup_attributes)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#modify_backup_attributes)
        """

    def modify_cluster(
        self, **kwargs: Unpack[ModifyClusterRequestRequestTypeDef]
    ) -> ModifyClusterResponseTypeDef:
        """
        Modifies CloudHSM cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.modify_cluster)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#modify_cluster)
        """

    def put_resource_policy(
        self, **kwargs: Unpack[PutResourcePolicyRequestRequestTypeDef]
    ) -> PutResourcePolicyResponseTypeDef:
        """
        Creates or updates an CloudHSM resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.put_resource_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#put_resource_policy)
        """

    def restore_backup(
        self, **kwargs: Unpack[RestoreBackupRequestRequestTypeDef]
    ) -> RestoreBackupResponseTypeDef:
        """
        Restores a specified CloudHSM backup that is in the `PENDING_DELETION` state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.restore_backup)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#restore_backup)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds or overwrites one or more tags for the specified CloudHSM cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes the specified tag or tags from the specified CloudHSM cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#untag_resource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_backups"]
    ) -> DescribeBackupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_clusters"]
    ) -> DescribeClustersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_tags"]) -> ListTagsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2.html#CloudHSMV2.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/client/#get_paginator)
        """
