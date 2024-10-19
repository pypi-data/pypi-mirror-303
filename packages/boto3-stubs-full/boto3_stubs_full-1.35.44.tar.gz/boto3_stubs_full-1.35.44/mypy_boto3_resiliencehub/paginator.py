"""
Type annotations for resiliencehub service client paginators.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/paginators/)

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_resiliencehub.client import ResilienceHubClient
    from mypy_boto3_resiliencehub.paginator import (
        ListAppAssessmentResourceDriftsPaginator,
        ListResourceGroupingRecommendationsPaginator,
    )

    session = Session()
    client: ResilienceHubClient = session.client("resiliencehub")

    list_app_assessment_resource_drifts_paginator: ListAppAssessmentResourceDriftsPaginator = client.get_paginator("list_app_assessment_resource_drifts")
    list_resource_grouping_recommendations_paginator: ListResourceGroupingRecommendationsPaginator = client.get_paginator("list_resource_grouping_recommendations")
    ```
"""

import sys
from typing import Generic, Iterator, TypeVar

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAppAssessmentResourceDriftsRequestListAppAssessmentResourceDriftsPaginateTypeDef,
    ListAppAssessmentResourceDriftsResponseTypeDef,
    ListResourceGroupingRecommendationsRequestListResourceGroupingRecommendationsPaginateTypeDef,
    ListResourceGroupingRecommendationsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack


__all__ = (
    "ListAppAssessmentResourceDriftsPaginator",
    "ListResourceGroupingRecommendationsPaginator",
)


_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class ListAppAssessmentResourceDriftsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub.html#ResilienceHub.Paginator.ListAppAssessmentResourceDrifts)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/paginators/#listappassessmentresourcedriftspaginator)
    """

    def paginate(
        self,
        **kwargs: Unpack[
            ListAppAssessmentResourceDriftsRequestListAppAssessmentResourceDriftsPaginateTypeDef
        ],
    ) -> _PageIterator[ListAppAssessmentResourceDriftsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub.html#ResilienceHub.Paginator.ListAppAssessmentResourceDrifts.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/paginators/#listappassessmentresourcedriftspaginator)
        """


class ListResourceGroupingRecommendationsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub.html#ResilienceHub.Paginator.ListResourceGroupingRecommendations)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/paginators/#listresourcegroupingrecommendationspaginator)
    """

    def paginate(
        self,
        **kwargs: Unpack[
            ListResourceGroupingRecommendationsRequestListResourceGroupingRecommendationsPaginateTypeDef
        ],
    ) -> _PageIterator[ListResourceGroupingRecommendationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resiliencehub.html#ResilienceHub.Paginator.ListResourceGroupingRecommendations.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/paginators/#listresourcegroupingrecommendationspaginator)
        """
