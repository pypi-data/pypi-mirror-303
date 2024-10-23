"""
Type annotations for outposts service client paginators.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/)

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_outposts.client import OutpostsClient
    from mypy_boto3_outposts.paginator import (
        GetOutpostInstanceTypesPaginator,
        GetOutpostSupportedInstanceTypesPaginator,
        ListAssetsPaginator,
        ListCapacityTasksPaginator,
        ListCatalogItemsPaginator,
        ListOrdersPaginator,
        ListOutpostsPaginator,
        ListSitesPaginator,
    )

    session = Session()
    client: OutpostsClient = session.client("outposts")

    get_outpost_instance_types_paginator: GetOutpostInstanceTypesPaginator = client.get_paginator("get_outpost_instance_types")
    get_outpost_supported_instance_types_paginator: GetOutpostSupportedInstanceTypesPaginator = client.get_paginator("get_outpost_supported_instance_types")
    list_assets_paginator: ListAssetsPaginator = client.get_paginator("list_assets")
    list_capacity_tasks_paginator: ListCapacityTasksPaginator = client.get_paginator("list_capacity_tasks")
    list_catalog_items_paginator: ListCatalogItemsPaginator = client.get_paginator("list_catalog_items")
    list_orders_paginator: ListOrdersPaginator = client.get_paginator("list_orders")
    list_outposts_paginator: ListOutpostsPaginator = client.get_paginator("list_outposts")
    list_sites_paginator: ListSitesPaginator = client.get_paginator("list_sites")
    ```
"""

import sys
from typing import Generic, Iterator, TypeVar

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetOutpostInstanceTypesInputGetOutpostInstanceTypesPaginateTypeDef,
    GetOutpostInstanceTypesOutputTypeDef,
    GetOutpostSupportedInstanceTypesInputGetOutpostSupportedInstanceTypesPaginateTypeDef,
    GetOutpostSupportedInstanceTypesOutputTypeDef,
    ListAssetsInputListAssetsPaginateTypeDef,
    ListAssetsOutputTypeDef,
    ListCapacityTasksInputListCapacityTasksPaginateTypeDef,
    ListCapacityTasksOutputTypeDef,
    ListCatalogItemsInputListCatalogItemsPaginateTypeDef,
    ListCatalogItemsOutputTypeDef,
    ListOrdersInputListOrdersPaginateTypeDef,
    ListOrdersOutputTypeDef,
    ListOutpostsInputListOutpostsPaginateTypeDef,
    ListOutpostsOutputTypeDef,
    ListSitesInputListSitesPaginateTypeDef,
    ListSitesOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack


__all__ = (
    "GetOutpostInstanceTypesPaginator",
    "GetOutpostSupportedInstanceTypesPaginator",
    "ListAssetsPaginator",
    "ListCapacityTasksPaginator",
    "ListCatalogItemsPaginator",
    "ListOrdersPaginator",
    "ListOutpostsPaginator",
    "ListSitesPaginator",
)


_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class GetOutpostInstanceTypesPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Paginator.GetOutpostInstanceTypes)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#getoutpostinstancetypespaginator)
    """

    def paginate(
        self, **kwargs: Unpack[GetOutpostInstanceTypesInputGetOutpostInstanceTypesPaginateTypeDef]
    ) -> _PageIterator[GetOutpostInstanceTypesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Paginator.GetOutpostInstanceTypes.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#getoutpostinstancetypespaginator)
        """


class GetOutpostSupportedInstanceTypesPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Paginator.GetOutpostSupportedInstanceTypes)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#getoutpostsupportedinstancetypespaginator)
    """

    def paginate(
        self,
        **kwargs: Unpack[
            GetOutpostSupportedInstanceTypesInputGetOutpostSupportedInstanceTypesPaginateTypeDef
        ],
    ) -> _PageIterator[GetOutpostSupportedInstanceTypesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Paginator.GetOutpostSupportedInstanceTypes.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#getoutpostsupportedinstancetypespaginator)
        """


class ListAssetsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Paginator.ListAssets)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#listassetspaginator)
    """

    def paginate(
        self, **kwargs: Unpack[ListAssetsInputListAssetsPaginateTypeDef]
    ) -> _PageIterator[ListAssetsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Paginator.ListAssets.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#listassetspaginator)
        """


class ListCapacityTasksPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Paginator.ListCapacityTasks)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#listcapacitytaskspaginator)
    """

    def paginate(
        self, **kwargs: Unpack[ListCapacityTasksInputListCapacityTasksPaginateTypeDef]
    ) -> _PageIterator[ListCapacityTasksOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Paginator.ListCapacityTasks.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#listcapacitytaskspaginator)
        """


class ListCatalogItemsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Paginator.ListCatalogItems)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#listcatalogitemspaginator)
    """

    def paginate(
        self, **kwargs: Unpack[ListCatalogItemsInputListCatalogItemsPaginateTypeDef]
    ) -> _PageIterator[ListCatalogItemsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Paginator.ListCatalogItems.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#listcatalogitemspaginator)
        """


class ListOrdersPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Paginator.ListOrders)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#listorderspaginator)
    """

    def paginate(
        self, **kwargs: Unpack[ListOrdersInputListOrdersPaginateTypeDef]
    ) -> _PageIterator[ListOrdersOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Paginator.ListOrders.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#listorderspaginator)
        """


class ListOutpostsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Paginator.ListOutposts)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#listoutpostspaginator)
    """

    def paginate(
        self, **kwargs: Unpack[ListOutpostsInputListOutpostsPaginateTypeDef]
    ) -> _PageIterator[ListOutpostsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Paginator.ListOutposts.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#listoutpostspaginator)
        """


class ListSitesPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Paginator.ListSites)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#listsitespaginator)
    """

    def paginate(
        self, **kwargs: Unpack[ListSitesInputListSitesPaginateTypeDef]
    ) -> _PageIterator[ListSitesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts.html#Outposts.Paginator.ListSites.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#listsitespaginator)
        """
