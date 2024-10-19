"""
Type annotations for grafana service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_grafana.client import ManagedGrafanaClient

    session = Session()
    client: ManagedGrafanaClient = session.client("grafana")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    ListPermissionsPaginator,
    ListVersionsPaginator,
    ListWorkspaceServiceAccountsPaginator,
    ListWorkspaceServiceAccountTokensPaginator,
    ListWorkspacesPaginator,
)
from .type_defs import (
    AssociateLicenseRequestRequestTypeDef,
    AssociateLicenseResponseTypeDef,
    CreateWorkspaceApiKeyRequestRequestTypeDef,
    CreateWorkspaceApiKeyResponseTypeDef,
    CreateWorkspaceRequestRequestTypeDef,
    CreateWorkspaceResponseTypeDef,
    CreateWorkspaceServiceAccountRequestRequestTypeDef,
    CreateWorkspaceServiceAccountResponseTypeDef,
    CreateWorkspaceServiceAccountTokenRequestRequestTypeDef,
    CreateWorkspaceServiceAccountTokenResponseTypeDef,
    DeleteWorkspaceApiKeyRequestRequestTypeDef,
    DeleteWorkspaceApiKeyResponseTypeDef,
    DeleteWorkspaceRequestRequestTypeDef,
    DeleteWorkspaceResponseTypeDef,
    DeleteWorkspaceServiceAccountRequestRequestTypeDef,
    DeleteWorkspaceServiceAccountResponseTypeDef,
    DeleteWorkspaceServiceAccountTokenRequestRequestTypeDef,
    DeleteWorkspaceServiceAccountTokenResponseTypeDef,
    DescribeWorkspaceAuthenticationRequestRequestTypeDef,
    DescribeWorkspaceAuthenticationResponseTypeDef,
    DescribeWorkspaceConfigurationRequestRequestTypeDef,
    DescribeWorkspaceConfigurationResponseTypeDef,
    DescribeWorkspaceRequestRequestTypeDef,
    DescribeWorkspaceResponseTypeDef,
    DisassociateLicenseRequestRequestTypeDef,
    DisassociateLicenseResponseTypeDef,
    ListPermissionsRequestRequestTypeDef,
    ListPermissionsResponseTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListVersionsRequestRequestTypeDef,
    ListVersionsResponseTypeDef,
    ListWorkspaceServiceAccountsRequestRequestTypeDef,
    ListWorkspaceServiceAccountsResponseTypeDef,
    ListWorkspaceServiceAccountTokensRequestRequestTypeDef,
    ListWorkspaceServiceAccountTokensResponseTypeDef,
    ListWorkspacesRequestRequestTypeDef,
    ListWorkspacesResponseTypeDef,
    TagResourceRequestRequestTypeDef,
    UntagResourceRequestRequestTypeDef,
    UpdatePermissionsRequestRequestTypeDef,
    UpdatePermissionsResponseTypeDef,
    UpdateWorkspaceAuthenticationRequestRequestTypeDef,
    UpdateWorkspaceAuthenticationResponseTypeDef,
    UpdateWorkspaceConfigurationRequestRequestTypeDef,
    UpdateWorkspaceRequestRequestTypeDef,
    UpdateWorkspaceResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("ManagedGrafanaClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class ManagedGrafanaClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ManagedGrafanaClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#exceptions)
        """

    def associate_license(
        self, **kwargs: Unpack[AssociateLicenseRequestRequestTypeDef]
    ) -> AssociateLicenseResponseTypeDef:
        """
        Assigns a Grafana Enterprise license to a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.associate_license)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#associate_license)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#close)
        """

    def create_workspace(
        self, **kwargs: Unpack[CreateWorkspaceRequestRequestTypeDef]
    ) -> CreateWorkspaceResponseTypeDef:
        """
        Creates a *workspace*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.create_workspace)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#create_workspace)
        """

    def create_workspace_api_key(
        self, **kwargs: Unpack[CreateWorkspaceApiKeyRequestRequestTypeDef]
    ) -> CreateWorkspaceApiKeyResponseTypeDef:
        """
        Creates a Grafana API key for the workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.create_workspace_api_key)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#create_workspace_api_key)
        """

    def create_workspace_service_account(
        self, **kwargs: Unpack[CreateWorkspaceServiceAccountRequestRequestTypeDef]
    ) -> CreateWorkspaceServiceAccountResponseTypeDef:
        """
        Creates a service account for the workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.create_workspace_service_account)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#create_workspace_service_account)
        """

    def create_workspace_service_account_token(
        self, **kwargs: Unpack[CreateWorkspaceServiceAccountTokenRequestRequestTypeDef]
    ) -> CreateWorkspaceServiceAccountTokenResponseTypeDef:
        """
        Creates a token that can be used to authenticate and authorize Grafana HTTP API
        operations for the given [workspace service
        account](https://docs.aws.amazon.com/grafana/latest/userguide/service-accounts.html).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.create_workspace_service_account_token)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#create_workspace_service_account_token)
        """

    def delete_workspace(
        self, **kwargs: Unpack[DeleteWorkspaceRequestRequestTypeDef]
    ) -> DeleteWorkspaceResponseTypeDef:
        """
        Deletes an Amazon Managed Grafana workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.delete_workspace)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#delete_workspace)
        """

    def delete_workspace_api_key(
        self, **kwargs: Unpack[DeleteWorkspaceApiKeyRequestRequestTypeDef]
    ) -> DeleteWorkspaceApiKeyResponseTypeDef:
        """
        Deletes a Grafana API key for the workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.delete_workspace_api_key)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#delete_workspace_api_key)
        """

    def delete_workspace_service_account(
        self, **kwargs: Unpack[DeleteWorkspaceServiceAccountRequestRequestTypeDef]
    ) -> DeleteWorkspaceServiceAccountResponseTypeDef:
        """
        Deletes a workspace service account from the workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.delete_workspace_service_account)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#delete_workspace_service_account)
        """

    def delete_workspace_service_account_token(
        self, **kwargs: Unpack[DeleteWorkspaceServiceAccountTokenRequestRequestTypeDef]
    ) -> DeleteWorkspaceServiceAccountTokenResponseTypeDef:
        """
        Deletes a token for the workspace service account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.delete_workspace_service_account_token)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#delete_workspace_service_account_token)
        """

    def describe_workspace(
        self, **kwargs: Unpack[DescribeWorkspaceRequestRequestTypeDef]
    ) -> DescribeWorkspaceResponseTypeDef:
        """
        Displays information about one Amazon Managed Grafana workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.describe_workspace)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#describe_workspace)
        """

    def describe_workspace_authentication(
        self, **kwargs: Unpack[DescribeWorkspaceAuthenticationRequestRequestTypeDef]
    ) -> DescribeWorkspaceAuthenticationResponseTypeDef:
        """
        Displays information about the authentication methods used in one Amazon
        Managed Grafana
        workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.describe_workspace_authentication)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#describe_workspace_authentication)
        """

    def describe_workspace_configuration(
        self, **kwargs: Unpack[DescribeWorkspaceConfigurationRequestRequestTypeDef]
    ) -> DescribeWorkspaceConfigurationResponseTypeDef:
        """
        Gets the current configuration string for the given workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.describe_workspace_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#describe_workspace_configuration)
        """

    def disassociate_license(
        self, **kwargs: Unpack[DisassociateLicenseRequestRequestTypeDef]
    ) -> DisassociateLicenseResponseTypeDef:
        """
        Removes the Grafana Enterprise license from a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.disassociate_license)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#disassociate_license)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#generate_presigned_url)
        """

    def list_permissions(
        self, **kwargs: Unpack[ListPermissionsRequestRequestTypeDef]
    ) -> ListPermissionsResponseTypeDef:
        """
        Lists the users and groups who have the Grafana `Admin` and `Editor` roles in
        this
        workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.list_permissions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#list_permissions)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        The `ListTagsForResource` operation returns the tags that are associated with
        the Amazon Managed Service for Grafana resource specified by the
        `resourceArn`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.list_tags_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#list_tags_for_resource)
        """

    def list_versions(
        self, **kwargs: Unpack[ListVersionsRequestRequestTypeDef]
    ) -> ListVersionsResponseTypeDef:
        """
        Lists available versions of Grafana.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.list_versions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#list_versions)
        """

    def list_workspace_service_account_tokens(
        self, **kwargs: Unpack[ListWorkspaceServiceAccountTokensRequestRequestTypeDef]
    ) -> ListWorkspaceServiceAccountTokensResponseTypeDef:
        """
        Returns a list of tokens for a workspace service account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.list_workspace_service_account_tokens)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#list_workspace_service_account_tokens)
        """

    def list_workspace_service_accounts(
        self, **kwargs: Unpack[ListWorkspaceServiceAccountsRequestRequestTypeDef]
    ) -> ListWorkspaceServiceAccountsResponseTypeDef:
        """
        Returns a list of service accounts for a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.list_workspace_service_accounts)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#list_workspace_service_accounts)
        """

    def list_workspaces(
        self, **kwargs: Unpack[ListWorkspacesRequestRequestTypeDef]
    ) -> ListWorkspacesResponseTypeDef:
        """
        Returns a list of Amazon Managed Grafana workspaces in the account, with some
        information about each
        workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.list_workspaces)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#list_workspaces)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        The `TagResource` operation associates tags with an Amazon Managed Grafana
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        The `UntagResource` operation removes the association of the tag with the
        Amazon Managed Grafana
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#untag_resource)
        """

    def update_permissions(
        self, **kwargs: Unpack[UpdatePermissionsRequestRequestTypeDef]
    ) -> UpdatePermissionsResponseTypeDef:
        """
        Updates which users in a workspace have the Grafana `Admin` or `Editor` roles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.update_permissions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#update_permissions)
        """

    def update_workspace(
        self, **kwargs: Unpack[UpdateWorkspaceRequestRequestTypeDef]
    ) -> UpdateWorkspaceResponseTypeDef:
        """
        Modifies an existing Amazon Managed Grafana workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.update_workspace)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#update_workspace)
        """

    def update_workspace_authentication(
        self, **kwargs: Unpack[UpdateWorkspaceAuthenticationRequestRequestTypeDef]
    ) -> UpdateWorkspaceAuthenticationResponseTypeDef:
        """
        Use this operation to define the identity provider (IdP) that this workspace
        authenticates users from, using
        SAML.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.update_workspace_authentication)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#update_workspace_authentication)
        """

    def update_workspace_configuration(
        self, **kwargs: Unpack[UpdateWorkspaceConfigurationRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the configuration string for the given workspace See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/grafana-2020-08-18/UpdateWorkspaceConfiguration).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.update_workspace_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#update_workspace_configuration)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_permissions"]
    ) -> ListPermissionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_versions"]) -> ListVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_workspace_service_account_tokens"]
    ) -> ListWorkspaceServiceAccountTokensPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_workspace_service_accounts"]
    ) -> ListWorkspaceServiceAccountsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_workspaces"]) -> ListWorkspacesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#get_paginator)
        """
