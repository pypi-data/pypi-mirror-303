"""
Type annotations for resource-explorer-2 service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_resource_explorer_2.client import ResourceExplorerClient

    session = Session()
    client: ResourceExplorerClient = session.client("resource-explorer-2")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    ListIndexesForMembersPaginator,
    ListIndexesPaginator,
    ListResourcesPaginator,
    ListSupportedResourceTypesPaginator,
    ListViewsPaginator,
    SearchPaginator,
)
from .type_defs import (
    AssociateDefaultViewInputRequestTypeDef,
    AssociateDefaultViewOutputTypeDef,
    BatchGetViewInputRequestTypeDef,
    BatchGetViewOutputTypeDef,
    CreateIndexInputRequestTypeDef,
    CreateIndexOutputTypeDef,
    CreateViewInputRequestTypeDef,
    CreateViewOutputTypeDef,
    DeleteIndexInputRequestTypeDef,
    DeleteIndexOutputTypeDef,
    DeleteViewInputRequestTypeDef,
    DeleteViewOutputTypeDef,
    EmptyResponseMetadataTypeDef,
    GetAccountLevelServiceConfigurationOutputTypeDef,
    GetDefaultViewOutputTypeDef,
    GetIndexOutputTypeDef,
    GetViewInputRequestTypeDef,
    GetViewOutputTypeDef,
    ListIndexesForMembersInputRequestTypeDef,
    ListIndexesForMembersOutputTypeDef,
    ListIndexesInputRequestTypeDef,
    ListIndexesOutputTypeDef,
    ListResourcesInputRequestTypeDef,
    ListResourcesOutputTypeDef,
    ListSupportedResourceTypesInputRequestTypeDef,
    ListSupportedResourceTypesOutputTypeDef,
    ListTagsForResourceInputRequestTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListViewsInputRequestTypeDef,
    ListViewsOutputTypeDef,
    SearchInputRequestTypeDef,
    SearchOutputTypeDef,
    TagResourceInputRequestTypeDef,
    UntagResourceInputRequestTypeDef,
    UpdateIndexTypeInputRequestTypeDef,
    UpdateIndexTypeOutputTypeDef,
    UpdateViewInputRequestTypeDef,
    UpdateViewOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack


__all__ = ("ResourceExplorerClient",)


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
    UnauthorizedException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class ResourceExplorerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ResourceExplorerClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#exceptions)
        """

    def associate_default_view(
        self, **kwargs: Unpack[AssociateDefaultViewInputRequestTypeDef]
    ) -> AssociateDefaultViewOutputTypeDef:
        """
        Sets the specified view as the default for the Amazon Web Services Region in
        which you call this
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client.associate_default_view)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#associate_default_view)
        """

    def batch_get_view(
        self, **kwargs: Unpack[BatchGetViewInputRequestTypeDef]
    ) -> BatchGetViewOutputTypeDef:
        """
        Retrieves details about a list of views.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client.batch_get_view)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#batch_get_view)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#close)
        """

    def create_index(
        self, **kwargs: Unpack[CreateIndexInputRequestTypeDef]
    ) -> CreateIndexOutputTypeDef:
        """
        Turns on Amazon Web Services Resource Explorer in the Amazon Web Services
        Region in which you called this operation by creating an
        index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client.create_index)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#create_index)
        """

    def create_view(
        self, **kwargs: Unpack[CreateViewInputRequestTypeDef]
    ) -> CreateViewOutputTypeDef:
        """
        Creates a view that users can query by using the  Search operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client.create_view)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#create_view)
        """

    def delete_index(
        self, **kwargs: Unpack[DeleteIndexInputRequestTypeDef]
    ) -> DeleteIndexOutputTypeDef:
        """
        Deletes the specified index and turns off Amazon Web Services Resource Explorer
        in the specified Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client.delete_index)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#delete_index)
        """

    def delete_view(
        self, **kwargs: Unpack[DeleteViewInputRequestTypeDef]
    ) -> DeleteViewOutputTypeDef:
        """
        Deletes the specified view.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client.delete_view)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#delete_view)
        """

    def disassociate_default_view(self) -> EmptyResponseMetadataTypeDef:
        """
        After you call this operation, the affected Amazon Web Services Region no
        longer has a default
        view.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client.disassociate_default_view)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#disassociate_default_view)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#generate_presigned_url)
        """

    def get_account_level_service_configuration(
        self,
    ) -> GetAccountLevelServiceConfigurationOutputTypeDef:
        """
        Retrieves the status of your account's Amazon Web Services service access, and
        validates the service linked role required to access the multi-account search
        feature.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client.get_account_level_service_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#get_account_level_service_configuration)
        """

    def get_default_view(self) -> GetDefaultViewOutputTypeDef:
        """
        Retrieves the Amazon Resource Name (ARN) of the view that is the default for
        the Amazon Web Services Region in which you call this
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client.get_default_view)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#get_default_view)
        """

    def get_index(self) -> GetIndexOutputTypeDef:
        """
        Retrieves details about the Amazon Web Services Resource Explorer index in the
        Amazon Web Services Region in which you invoked the
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client.get_index)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#get_index)
        """

    def get_view(self, **kwargs: Unpack[GetViewInputRequestTypeDef]) -> GetViewOutputTypeDef:
        """
        Retrieves details of the specified view.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client.get_view)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#get_view)
        """

    def list_indexes(
        self, **kwargs: Unpack[ListIndexesInputRequestTypeDef]
    ) -> ListIndexesOutputTypeDef:
        """
        Retrieves a list of all of the indexes in Amazon Web Services Regions that are
        currently collecting resource information for Amazon Web Services Resource
        Explorer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client.list_indexes)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#list_indexes)
        """

    def list_indexes_for_members(
        self, **kwargs: Unpack[ListIndexesForMembersInputRequestTypeDef]
    ) -> ListIndexesForMembersOutputTypeDef:
        """
        Retrieves a list of a member's indexes in all Amazon Web Services Regions that
        are currently collecting resource information for Amazon Web Services Resource
        Explorer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client.list_indexes_for_members)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#list_indexes_for_members)
        """

    def list_resources(
        self, **kwargs: Unpack[ListResourcesInputRequestTypeDef]
    ) -> ListResourcesOutputTypeDef:
        """
        Returns a list of resources and their details that match the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client.list_resources)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#list_resources)
        """

    def list_supported_resource_types(
        self, **kwargs: Unpack[ListSupportedResourceTypesInputRequestTypeDef]
    ) -> ListSupportedResourceTypesOutputTypeDef:
        """
        Retrieves a list of all resource types currently supported by Amazon Web
        Services Resource
        Explorer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client.list_supported_resource_types)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#list_supported_resource_types)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputRequestTypeDef]
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Lists the tags that are attached to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client.list_tags_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#list_tags_for_resource)
        """

    def list_views(self, **kwargs: Unpack[ListViewsInputRequestTypeDef]) -> ListViewsOutputTypeDef:
        """
        Lists the [Amazon resource names
        (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html)
        of the views available in the Amazon Web Services Region in which you call this
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client.list_views)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#list_views)
        """

    def search(self, **kwargs: Unpack[SearchInputRequestTypeDef]) -> SearchOutputTypeDef:
        """
        Searches for resources and displays details about all resources that match the
        specified
        criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client.search)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#search)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceInputRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds one or more tag key and value pairs to an Amazon Web Services Resource
        Explorer view or
        index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceInputRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes one or more tag key and value pairs from an Amazon Web Services
        Resource Explorer view or
        index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#untag_resource)
        """

    def update_index_type(
        self, **kwargs: Unpack[UpdateIndexTypeInputRequestTypeDef]
    ) -> UpdateIndexTypeOutputTypeDef:
        """
        Changes the type of the index from one of the following types to the other.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client.update_index_type)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#update_index_type)
        """

    def update_view(
        self, **kwargs: Unpack[UpdateViewInputRequestTypeDef]
    ) -> UpdateViewOutputTypeDef:
        """
        Modifies some of the details of a view.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client.update_view)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#update_view)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_indexes"]) -> ListIndexesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_indexes_for_members"]
    ) -> ListIndexesForMembersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_resources"]) -> ListResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_supported_resource_types"]
    ) -> ListSupportedResourceTypesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_views"]) -> ListViewsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search"]) -> SearchPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#get_paginator)
        """
