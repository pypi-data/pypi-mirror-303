"""
Type annotations for mturk service client paginators.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/)

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_mturk.client import MTurkClient
    from mypy_boto3_mturk.paginator import (
        ListAssignmentsForHITPaginator,
        ListBonusPaymentsPaginator,
        ListHITsPaginator,
        ListHITsForQualificationTypePaginator,
        ListQualificationRequestsPaginator,
        ListQualificationTypesPaginator,
        ListReviewableHITsPaginator,
        ListWorkerBlocksPaginator,
        ListWorkersWithQualificationTypePaginator,
    )

    session = Session()
    client: MTurkClient = session.client("mturk")

    list_assignments_for_hit_paginator: ListAssignmentsForHITPaginator = client.get_paginator("list_assignments_for_hit")
    list_bonus_payments_paginator: ListBonusPaymentsPaginator = client.get_paginator("list_bonus_payments")
    list_hits_paginator: ListHITsPaginator = client.get_paginator("list_hits")
    list_hits_for_qualification_type_paginator: ListHITsForQualificationTypePaginator = client.get_paginator("list_hits_for_qualification_type")
    list_qualification_requests_paginator: ListQualificationRequestsPaginator = client.get_paginator("list_qualification_requests")
    list_qualification_types_paginator: ListQualificationTypesPaginator = client.get_paginator("list_qualification_types")
    list_reviewable_hits_paginator: ListReviewableHITsPaginator = client.get_paginator("list_reviewable_hits")
    list_worker_blocks_paginator: ListWorkerBlocksPaginator = client.get_paginator("list_worker_blocks")
    list_workers_with_qualification_type_paginator: ListWorkersWithQualificationTypePaginator = client.get_paginator("list_workers_with_qualification_type")
    ```
"""

import sys
from typing import Generic, Iterator, TypeVar

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAssignmentsForHITRequestListAssignmentsForHITPaginateTypeDef,
    ListAssignmentsForHITResponseTypeDef,
    ListBonusPaymentsRequestListBonusPaymentsPaginateTypeDef,
    ListBonusPaymentsResponseTypeDef,
    ListHITsForQualificationTypeRequestListHITsForQualificationTypePaginateTypeDef,
    ListHITsForQualificationTypeResponseTypeDef,
    ListHITsRequestListHITsPaginateTypeDef,
    ListHITsResponseTypeDef,
    ListQualificationRequestsRequestListQualificationRequestsPaginateTypeDef,
    ListQualificationRequestsResponseTypeDef,
    ListQualificationTypesRequestListQualificationTypesPaginateTypeDef,
    ListQualificationTypesResponseTypeDef,
    ListReviewableHITsRequestListReviewableHITsPaginateTypeDef,
    ListReviewableHITsResponseTypeDef,
    ListWorkerBlocksRequestListWorkerBlocksPaginateTypeDef,
    ListWorkerBlocksResponseTypeDef,
    ListWorkersWithQualificationTypeRequestListWorkersWithQualificationTypePaginateTypeDef,
    ListWorkersWithQualificationTypeResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack


__all__ = (
    "ListAssignmentsForHITPaginator",
    "ListBonusPaymentsPaginator",
    "ListHITsPaginator",
    "ListHITsForQualificationTypePaginator",
    "ListQualificationRequestsPaginator",
    "ListQualificationTypesPaginator",
    "ListReviewableHITsPaginator",
    "ListWorkerBlocksPaginator",
    "ListWorkersWithQualificationTypePaginator",
)


_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class ListAssignmentsForHITPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Paginator.ListAssignmentsForHIT)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listassignmentsforhitpaginator)
    """

    def paginate(
        self, **kwargs: Unpack[ListAssignmentsForHITRequestListAssignmentsForHITPaginateTypeDef]
    ) -> _PageIterator[ListAssignmentsForHITResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Paginator.ListAssignmentsForHIT.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listassignmentsforhitpaginator)
        """


class ListBonusPaymentsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Paginator.ListBonusPayments)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listbonuspaymentspaginator)
    """

    def paginate(
        self, **kwargs: Unpack[ListBonusPaymentsRequestListBonusPaymentsPaginateTypeDef]
    ) -> _PageIterator[ListBonusPaymentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Paginator.ListBonusPayments.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listbonuspaymentspaginator)
        """


class ListHITsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Paginator.ListHITs)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listhitspaginator)
    """

    def paginate(
        self, **kwargs: Unpack[ListHITsRequestListHITsPaginateTypeDef]
    ) -> _PageIterator[ListHITsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Paginator.ListHITs.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listhitspaginator)
        """


class ListHITsForQualificationTypePaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Paginator.ListHITsForQualificationType)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listhitsforqualificationtypepaginator)
    """

    def paginate(
        self,
        **kwargs: Unpack[
            ListHITsForQualificationTypeRequestListHITsForQualificationTypePaginateTypeDef
        ],
    ) -> _PageIterator[ListHITsForQualificationTypeResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Paginator.ListHITsForQualificationType.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listhitsforqualificationtypepaginator)
        """


class ListQualificationRequestsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Paginator.ListQualificationRequests)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listqualificationrequestspaginator)
    """

    def paginate(
        self,
        **kwargs: Unpack[ListQualificationRequestsRequestListQualificationRequestsPaginateTypeDef],
    ) -> _PageIterator[ListQualificationRequestsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Paginator.ListQualificationRequests.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listqualificationrequestspaginator)
        """


class ListQualificationTypesPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Paginator.ListQualificationTypes)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listqualificationtypespaginator)
    """

    def paginate(
        self, **kwargs: Unpack[ListQualificationTypesRequestListQualificationTypesPaginateTypeDef]
    ) -> _PageIterator[ListQualificationTypesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Paginator.ListQualificationTypes.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listqualificationtypespaginator)
        """


class ListReviewableHITsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Paginator.ListReviewableHITs)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listreviewablehitspaginator)
    """

    def paginate(
        self, **kwargs: Unpack[ListReviewableHITsRequestListReviewableHITsPaginateTypeDef]
    ) -> _PageIterator[ListReviewableHITsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Paginator.ListReviewableHITs.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listreviewablehitspaginator)
        """


class ListWorkerBlocksPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Paginator.ListWorkerBlocks)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listworkerblockspaginator)
    """

    def paginate(
        self, **kwargs: Unpack[ListWorkerBlocksRequestListWorkerBlocksPaginateTypeDef]
    ) -> _PageIterator[ListWorkerBlocksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Paginator.ListWorkerBlocks.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listworkerblockspaginator)
        """


class ListWorkersWithQualificationTypePaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Paginator.ListWorkersWithQualificationType)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listworkerswithqualificationtypepaginator)
    """

    def paginate(
        self,
        **kwargs: Unpack[
            ListWorkersWithQualificationTypeRequestListWorkersWithQualificationTypePaginateTypeDef
        ],
    ) -> _PageIterator[ListWorkersWithQualificationTypeResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mturk.html#MTurk.Paginator.ListWorkersWithQualificationType.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mturk/paginators/#listworkerswithqualificationtypepaginator)
        """
