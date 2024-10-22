"""
Type annotations for lakeformation service client paginators.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators/)

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_lakeformation.client import LakeFormationClient
    from mypy_boto3_lakeformation.paginator import (
        GetWorkUnitsPaginator,
        ListDataCellsFilterPaginator,
        ListLFTagsPaginator,
        SearchDatabasesByLFTagsPaginator,
        SearchTablesByLFTagsPaginator,
    )

    session = Session()
    client: LakeFormationClient = session.client("lakeformation")

    get_work_units_paginator: GetWorkUnitsPaginator = client.get_paginator("get_work_units")
    list_data_cells_filter_paginator: ListDataCellsFilterPaginator = client.get_paginator("list_data_cells_filter")
    list_lf_tags_paginator: ListLFTagsPaginator = client.get_paginator("list_lf_tags")
    search_databases_by_lf_tags_paginator: SearchDatabasesByLFTagsPaginator = client.get_paginator("search_databases_by_lf_tags")
    search_tables_by_lf_tags_paginator: SearchTablesByLFTagsPaginator = client.get_paginator("search_tables_by_lf_tags")
    ```
"""

import sys
from typing import Generic, Iterator, TypeVar

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetWorkUnitsRequestGetWorkUnitsPaginateTypeDef,
    GetWorkUnitsResponseTypeDef,
    ListDataCellsFilterRequestListDataCellsFilterPaginateTypeDef,
    ListDataCellsFilterResponseTypeDef,
    ListLFTagsRequestListLFTagsPaginateTypeDef,
    ListLFTagsResponseTypeDef,
    SearchDatabasesByLFTagsRequestSearchDatabasesByLFTagsPaginateTypeDef,
    SearchDatabasesByLFTagsResponseTypeDef,
    SearchTablesByLFTagsRequestSearchTablesByLFTagsPaginateTypeDef,
    SearchTablesByLFTagsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack


__all__ = (
    "GetWorkUnitsPaginator",
    "ListDataCellsFilterPaginator",
    "ListLFTagsPaginator",
    "SearchDatabasesByLFTagsPaginator",
    "SearchTablesByLFTagsPaginator",
)


_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class GetWorkUnitsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html#LakeFormation.Paginator.GetWorkUnits)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators/#getworkunitspaginator)
    """

    def paginate(
        self, **kwargs: Unpack[GetWorkUnitsRequestGetWorkUnitsPaginateTypeDef]
    ) -> _PageIterator[GetWorkUnitsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html#LakeFormation.Paginator.GetWorkUnits.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators/#getworkunitspaginator)
        """


class ListDataCellsFilterPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html#LakeFormation.Paginator.ListDataCellsFilter)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators/#listdatacellsfilterpaginator)
    """

    def paginate(
        self, **kwargs: Unpack[ListDataCellsFilterRequestListDataCellsFilterPaginateTypeDef]
    ) -> _PageIterator[ListDataCellsFilterResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html#LakeFormation.Paginator.ListDataCellsFilter.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators/#listdatacellsfilterpaginator)
        """


class ListLFTagsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html#LakeFormation.Paginator.ListLFTags)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators/#listlftagspaginator)
    """

    def paginate(
        self, **kwargs: Unpack[ListLFTagsRequestListLFTagsPaginateTypeDef]
    ) -> _PageIterator[ListLFTagsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html#LakeFormation.Paginator.ListLFTags.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators/#listlftagspaginator)
        """


class SearchDatabasesByLFTagsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html#LakeFormation.Paginator.SearchDatabasesByLFTags)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators/#searchdatabasesbylftagspaginator)
    """

    def paginate(
        self, **kwargs: Unpack[SearchDatabasesByLFTagsRequestSearchDatabasesByLFTagsPaginateTypeDef]
    ) -> _PageIterator[SearchDatabasesByLFTagsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html#LakeFormation.Paginator.SearchDatabasesByLFTags.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators/#searchdatabasesbylftagspaginator)
        """


class SearchTablesByLFTagsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html#LakeFormation.Paginator.SearchTablesByLFTags)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators/#searchtablesbylftagspaginator)
    """

    def paginate(
        self, **kwargs: Unpack[SearchTablesByLFTagsRequestSearchTablesByLFTagsPaginateTypeDef]
    ) -> _PageIterator[SearchTablesByLFTagsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lakeformation.html#LakeFormation.Paginator.SearchTablesByLFTags.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/paginators/#searchtablesbylftagspaginator)
        """
