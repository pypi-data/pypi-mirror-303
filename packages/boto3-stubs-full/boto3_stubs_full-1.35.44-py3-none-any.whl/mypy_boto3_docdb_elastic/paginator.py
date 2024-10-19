"""
Type annotations for docdb-elastic service client paginators.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/paginators/)

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_docdb_elastic.client import DocDBElasticClient
    from mypy_boto3_docdb_elastic.paginator import (
        ListClusterSnapshotsPaginator,
        ListClustersPaginator,
    )

    session = Session()
    client: DocDBElasticClient = session.client("docdb-elastic")

    list_cluster_snapshots_paginator: ListClusterSnapshotsPaginator = client.get_paginator("list_cluster_snapshots")
    list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
    ```
"""

import sys
from typing import Generic, Iterator, TypeVar

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListClustersInputListClustersPaginateTypeDef,
    ListClusterSnapshotsInputListClusterSnapshotsPaginateTypeDef,
    ListClusterSnapshotsOutputTypeDef,
    ListClustersOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack


__all__ = ("ListClusterSnapshotsPaginator", "ListClustersPaginator")


_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class ListClusterSnapshotsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic.html#DocDBElastic.Paginator.ListClusterSnapshots)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/paginators/#listclustersnapshotspaginator)
    """

    def paginate(
        self, **kwargs: Unpack[ListClusterSnapshotsInputListClusterSnapshotsPaginateTypeDef]
    ) -> _PageIterator[ListClusterSnapshotsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic.html#DocDBElastic.Paginator.ListClusterSnapshots.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/paginators/#listclustersnapshotspaginator)
        """


class ListClustersPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic.html#DocDBElastic.Paginator.ListClusters)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/paginators/#listclusterspaginator)
    """

    def paginate(
        self, **kwargs: Unpack[ListClustersInputListClustersPaginateTypeDef]
    ) -> _PageIterator[ListClustersOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic.html#DocDBElastic.Paginator.ListClusters.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/paginators/#listclusterspaginator)
        """
