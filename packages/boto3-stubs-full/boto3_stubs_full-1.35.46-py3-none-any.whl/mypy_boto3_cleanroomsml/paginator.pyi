"""
Type annotations for cleanroomsml service client paginators.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/)

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_cleanroomsml.client import CleanRoomsMLClient
    from mypy_boto3_cleanroomsml.paginator import (
        ListAudienceExportJobsPaginator,
        ListAudienceGenerationJobsPaginator,
        ListAudienceModelsPaginator,
        ListConfiguredAudienceModelsPaginator,
        ListTrainingDatasetsPaginator,
    )

    session = Session()
    client: CleanRoomsMLClient = session.client("cleanroomsml")

    list_audience_export_jobs_paginator: ListAudienceExportJobsPaginator = client.get_paginator("list_audience_export_jobs")
    list_audience_generation_jobs_paginator: ListAudienceGenerationJobsPaginator = client.get_paginator("list_audience_generation_jobs")
    list_audience_models_paginator: ListAudienceModelsPaginator = client.get_paginator("list_audience_models")
    list_configured_audience_models_paginator: ListConfiguredAudienceModelsPaginator = client.get_paginator("list_configured_audience_models")
    list_training_datasets_paginator: ListTrainingDatasetsPaginator = client.get_paginator("list_training_datasets")
    ```
"""

import sys
from typing import Generic, Iterator, TypeVar

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAudienceExportJobsRequestListAudienceExportJobsPaginateTypeDef,
    ListAudienceExportJobsResponseTypeDef,
    ListAudienceGenerationJobsRequestListAudienceGenerationJobsPaginateTypeDef,
    ListAudienceGenerationJobsResponseTypeDef,
    ListAudienceModelsRequestListAudienceModelsPaginateTypeDef,
    ListAudienceModelsResponseTypeDef,
    ListConfiguredAudienceModelsRequestListConfiguredAudienceModelsPaginateTypeDef,
    ListConfiguredAudienceModelsResponseTypeDef,
    ListTrainingDatasetsRequestListTrainingDatasetsPaginateTypeDef,
    ListTrainingDatasetsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListAudienceExportJobsPaginator",
    "ListAudienceGenerationJobsPaginator",
    "ListAudienceModelsPaginator",
    "ListConfiguredAudienceModelsPaginator",
    "ListTrainingDatasetsPaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")

class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """

class ListAudienceExportJobsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Paginator.ListAudienceExportJobs)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listaudienceexportjobspaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListAudienceExportJobsRequestListAudienceExportJobsPaginateTypeDef]
    ) -> _PageIterator[ListAudienceExportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Paginator.ListAudienceExportJobs.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listaudienceexportjobspaginator)
        """

class ListAudienceGenerationJobsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Paginator.ListAudienceGenerationJobs)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listaudiencegenerationjobspaginator)
    """
    def paginate(
        self,
        **kwargs: Unpack[
            ListAudienceGenerationJobsRequestListAudienceGenerationJobsPaginateTypeDef
        ],
    ) -> _PageIterator[ListAudienceGenerationJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Paginator.ListAudienceGenerationJobs.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listaudiencegenerationjobspaginator)
        """

class ListAudienceModelsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Paginator.ListAudienceModels)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listaudiencemodelspaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListAudienceModelsRequestListAudienceModelsPaginateTypeDef]
    ) -> _PageIterator[ListAudienceModelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Paginator.ListAudienceModels.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listaudiencemodelspaginator)
        """

class ListConfiguredAudienceModelsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Paginator.ListConfiguredAudienceModels)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listconfiguredaudiencemodelspaginator)
    """
    def paginate(
        self,
        **kwargs: Unpack[
            ListConfiguredAudienceModelsRequestListConfiguredAudienceModelsPaginateTypeDef
        ],
    ) -> _PageIterator[ListConfiguredAudienceModelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Paginator.ListConfiguredAudienceModels.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listconfiguredaudiencemodelspaginator)
        """

class ListTrainingDatasetsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Paginator.ListTrainingDatasets)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listtrainingdatasetspaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListTrainingDatasetsRequestListTrainingDatasetsPaginateTypeDef]
    ) -> _PageIterator[ListTrainingDatasetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Paginator.ListTrainingDatasets.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/paginators/#listtrainingdatasetspaginator)
        """
