"""
Type annotations for memorydb service client paginators.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/)

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_memorydb.client import MemoryDBClient
    from mypy_boto3_memorydb.paginator import (
        DescribeACLsPaginator,
        DescribeClustersPaginator,
        DescribeEngineVersionsPaginator,
        DescribeEventsPaginator,
        DescribeParameterGroupsPaginator,
        DescribeParametersPaginator,
        DescribeReservedNodesPaginator,
        DescribeReservedNodesOfferingsPaginator,
        DescribeServiceUpdatesPaginator,
        DescribeSnapshotsPaginator,
        DescribeSubnetGroupsPaginator,
        DescribeUsersPaginator,
    )

    session = Session()
    client: MemoryDBClient = session.client("memorydb")

    describe_acls_paginator: DescribeACLsPaginator = client.get_paginator("describe_acls")
    describe_clusters_paginator: DescribeClustersPaginator = client.get_paginator("describe_clusters")
    describe_engine_versions_paginator: DescribeEngineVersionsPaginator = client.get_paginator("describe_engine_versions")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    describe_parameter_groups_paginator: DescribeParameterGroupsPaginator = client.get_paginator("describe_parameter_groups")
    describe_parameters_paginator: DescribeParametersPaginator = client.get_paginator("describe_parameters")
    describe_reserved_nodes_paginator: DescribeReservedNodesPaginator = client.get_paginator("describe_reserved_nodes")
    describe_reserved_nodes_offerings_paginator: DescribeReservedNodesOfferingsPaginator = client.get_paginator("describe_reserved_nodes_offerings")
    describe_service_updates_paginator: DescribeServiceUpdatesPaginator = client.get_paginator("describe_service_updates")
    describe_snapshots_paginator: DescribeSnapshotsPaginator = client.get_paginator("describe_snapshots")
    describe_subnet_groups_paginator: DescribeSubnetGroupsPaginator = client.get_paginator("describe_subnet_groups")
    describe_users_paginator: DescribeUsersPaginator = client.get_paginator("describe_users")
    ```
"""

import sys
from typing import Generic, Iterator, TypeVar

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeACLsRequestDescribeACLsPaginateTypeDef,
    DescribeACLsResponseTypeDef,
    DescribeClustersRequestDescribeClustersPaginateTypeDef,
    DescribeClustersResponseTypeDef,
    DescribeEngineVersionsRequestDescribeEngineVersionsPaginateTypeDef,
    DescribeEngineVersionsResponseTypeDef,
    DescribeEventsRequestDescribeEventsPaginateTypeDef,
    DescribeEventsResponseTypeDef,
    DescribeParameterGroupsRequestDescribeParameterGroupsPaginateTypeDef,
    DescribeParameterGroupsResponseTypeDef,
    DescribeParametersRequestDescribeParametersPaginateTypeDef,
    DescribeParametersResponseTypeDef,
    DescribeReservedNodesOfferingsRequestDescribeReservedNodesOfferingsPaginateTypeDef,
    DescribeReservedNodesOfferingsResponseTypeDef,
    DescribeReservedNodesRequestDescribeReservedNodesPaginateTypeDef,
    DescribeReservedNodesResponseTypeDef,
    DescribeServiceUpdatesRequestDescribeServiceUpdatesPaginateTypeDef,
    DescribeServiceUpdatesResponseTypeDef,
    DescribeSnapshotsRequestDescribeSnapshotsPaginateTypeDef,
    DescribeSnapshotsResponseTypeDef,
    DescribeSubnetGroupsRequestDescribeSubnetGroupsPaginateTypeDef,
    DescribeSubnetGroupsResponseTypeDef,
    DescribeUsersRequestDescribeUsersPaginateTypeDef,
    DescribeUsersResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack


__all__ = (
    "DescribeACLsPaginator",
    "DescribeClustersPaginator",
    "DescribeEngineVersionsPaginator",
    "DescribeEventsPaginator",
    "DescribeParameterGroupsPaginator",
    "DescribeParametersPaginator",
    "DescribeReservedNodesPaginator",
    "DescribeReservedNodesOfferingsPaginator",
    "DescribeServiceUpdatesPaginator",
    "DescribeSnapshotsPaginator",
    "DescribeSubnetGroupsPaginator",
    "DescribeUsersPaginator",
)


_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class DescribeACLsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Paginator.DescribeACLs)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describeaclspaginator)
    """

    def paginate(
        self, **kwargs: Unpack[DescribeACLsRequestDescribeACLsPaginateTypeDef]
    ) -> _PageIterator[DescribeACLsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Paginator.DescribeACLs.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describeaclspaginator)
        """


class DescribeClustersPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Paginator.DescribeClusters)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describeclusterspaginator)
    """

    def paginate(
        self, **kwargs: Unpack[DescribeClustersRequestDescribeClustersPaginateTypeDef]
    ) -> _PageIterator[DescribeClustersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Paginator.DescribeClusters.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describeclusterspaginator)
        """


class DescribeEngineVersionsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Paginator.DescribeEngineVersions)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describeengineversionspaginator)
    """

    def paginate(
        self, **kwargs: Unpack[DescribeEngineVersionsRequestDescribeEngineVersionsPaginateTypeDef]
    ) -> _PageIterator[DescribeEngineVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Paginator.DescribeEngineVersions.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describeengineversionspaginator)
        """


class DescribeEventsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Paginator.DescribeEvents)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describeeventspaginator)
    """

    def paginate(
        self, **kwargs: Unpack[DescribeEventsRequestDescribeEventsPaginateTypeDef]
    ) -> _PageIterator[DescribeEventsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Paginator.DescribeEvents.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describeeventspaginator)
        """


class DescribeParameterGroupsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Paginator.DescribeParameterGroups)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describeparametergroupspaginator)
    """

    def paginate(
        self, **kwargs: Unpack[DescribeParameterGroupsRequestDescribeParameterGroupsPaginateTypeDef]
    ) -> _PageIterator[DescribeParameterGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Paginator.DescribeParameterGroups.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describeparametergroupspaginator)
        """


class DescribeParametersPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Paginator.DescribeParameters)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describeparameterspaginator)
    """

    def paginate(
        self, **kwargs: Unpack[DescribeParametersRequestDescribeParametersPaginateTypeDef]
    ) -> _PageIterator[DescribeParametersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Paginator.DescribeParameters.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describeparameterspaginator)
        """


class DescribeReservedNodesPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Paginator.DescribeReservedNodes)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describereservednodespaginator)
    """

    def paginate(
        self, **kwargs: Unpack[DescribeReservedNodesRequestDescribeReservedNodesPaginateTypeDef]
    ) -> _PageIterator[DescribeReservedNodesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Paginator.DescribeReservedNodes.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describereservednodespaginator)
        """


class DescribeReservedNodesOfferingsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Paginator.DescribeReservedNodesOfferings)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describereservednodesofferingspaginator)
    """

    def paginate(
        self,
        **kwargs: Unpack[
            DescribeReservedNodesOfferingsRequestDescribeReservedNodesOfferingsPaginateTypeDef
        ],
    ) -> _PageIterator[DescribeReservedNodesOfferingsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Paginator.DescribeReservedNodesOfferings.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describereservednodesofferingspaginator)
        """


class DescribeServiceUpdatesPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Paginator.DescribeServiceUpdates)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describeserviceupdatespaginator)
    """

    def paginate(
        self, **kwargs: Unpack[DescribeServiceUpdatesRequestDescribeServiceUpdatesPaginateTypeDef]
    ) -> _PageIterator[DescribeServiceUpdatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Paginator.DescribeServiceUpdates.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describeserviceupdatespaginator)
        """


class DescribeSnapshotsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Paginator.DescribeSnapshots)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describesnapshotspaginator)
    """

    def paginate(
        self, **kwargs: Unpack[DescribeSnapshotsRequestDescribeSnapshotsPaginateTypeDef]
    ) -> _PageIterator[DescribeSnapshotsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Paginator.DescribeSnapshots.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describesnapshotspaginator)
        """


class DescribeSubnetGroupsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Paginator.DescribeSubnetGroups)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describesubnetgroupspaginator)
    """

    def paginate(
        self, **kwargs: Unpack[DescribeSubnetGroupsRequestDescribeSubnetGroupsPaginateTypeDef]
    ) -> _PageIterator[DescribeSubnetGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Paginator.DescribeSubnetGroups.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describesubnetgroupspaginator)
        """


class DescribeUsersPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Paginator.DescribeUsers)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describeuserspaginator)
    """

    def paginate(
        self, **kwargs: Unpack[DescribeUsersRequestDescribeUsersPaginateTypeDef]
    ) -> _PageIterator[DescribeUsersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Paginator.DescribeUsers.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/paginators/#describeuserspaginator)
        """
