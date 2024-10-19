"""
Type annotations for cleanroomsml service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_cleanroomsml.client import CleanRoomsMLClient

    session = Session()
    client: CleanRoomsMLClient = session.client("cleanroomsml")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    ListAudienceExportJobsPaginator,
    ListAudienceGenerationJobsPaginator,
    ListAudienceModelsPaginator,
    ListConfiguredAudienceModelsPaginator,
    ListTrainingDatasetsPaginator,
)
from .type_defs import (
    CreateAudienceModelRequestRequestTypeDef,
    CreateAudienceModelResponseTypeDef,
    CreateConfiguredAudienceModelRequestRequestTypeDef,
    CreateConfiguredAudienceModelResponseTypeDef,
    CreateTrainingDatasetRequestRequestTypeDef,
    CreateTrainingDatasetResponseTypeDef,
    DeleteAudienceGenerationJobRequestRequestTypeDef,
    DeleteAudienceModelRequestRequestTypeDef,
    DeleteConfiguredAudienceModelPolicyRequestRequestTypeDef,
    DeleteConfiguredAudienceModelRequestRequestTypeDef,
    DeleteTrainingDatasetRequestRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    GetAudienceGenerationJobRequestRequestTypeDef,
    GetAudienceGenerationJobResponseTypeDef,
    GetAudienceModelRequestRequestTypeDef,
    GetAudienceModelResponseTypeDef,
    GetConfiguredAudienceModelPolicyRequestRequestTypeDef,
    GetConfiguredAudienceModelPolicyResponseTypeDef,
    GetConfiguredAudienceModelRequestRequestTypeDef,
    GetConfiguredAudienceModelResponseTypeDef,
    GetTrainingDatasetRequestRequestTypeDef,
    GetTrainingDatasetResponseTypeDef,
    ListAudienceExportJobsRequestRequestTypeDef,
    ListAudienceExportJobsResponseTypeDef,
    ListAudienceGenerationJobsRequestRequestTypeDef,
    ListAudienceGenerationJobsResponseTypeDef,
    ListAudienceModelsRequestRequestTypeDef,
    ListAudienceModelsResponseTypeDef,
    ListConfiguredAudienceModelsRequestRequestTypeDef,
    ListConfiguredAudienceModelsResponseTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTrainingDatasetsRequestRequestTypeDef,
    ListTrainingDatasetsResponseTypeDef,
    PutConfiguredAudienceModelPolicyRequestRequestTypeDef,
    PutConfiguredAudienceModelPolicyResponseTypeDef,
    StartAudienceExportJobRequestRequestTypeDef,
    StartAudienceGenerationJobRequestRequestTypeDef,
    StartAudienceGenerationJobResponseTypeDef,
    TagResourceRequestRequestTypeDef,
    UntagResourceRequestRequestTypeDef,
    UpdateConfiguredAudienceModelRequestRequestTypeDef,
    UpdateConfiguredAudienceModelResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack


__all__ = ("CleanRoomsMLClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class CleanRoomsMLClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CleanRoomsMLClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#close)
        """

    def create_audience_model(
        self, **kwargs: Unpack[CreateAudienceModelRequestRequestTypeDef]
    ) -> CreateAudienceModelResponseTypeDef:
        """
        Defines the information necessary to create an audience model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.create_audience_model)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#create_audience_model)
        """

    def create_configured_audience_model(
        self, **kwargs: Unpack[CreateConfiguredAudienceModelRequestRequestTypeDef]
    ) -> CreateConfiguredAudienceModelResponseTypeDef:
        """
        Defines the information necessary to create a configured audience model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.create_configured_audience_model)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#create_configured_audience_model)
        """

    def create_training_dataset(
        self, **kwargs: Unpack[CreateTrainingDatasetRequestRequestTypeDef]
    ) -> CreateTrainingDatasetResponseTypeDef:
        """
        Defines the information necessary to create a training dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.create_training_dataset)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#create_training_dataset)
        """

    def delete_audience_generation_job(
        self, **kwargs: Unpack[DeleteAudienceGenerationJobRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified audience generation job, and removes all data associated
        with the
        job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.delete_audience_generation_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#delete_audience_generation_job)
        """

    def delete_audience_model(
        self, **kwargs: Unpack[DeleteAudienceModelRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Specifies an audience model that you want to delete.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.delete_audience_model)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#delete_audience_model)
        """

    def delete_configured_audience_model(
        self, **kwargs: Unpack[DeleteConfiguredAudienceModelRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified configured audience model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.delete_configured_audience_model)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#delete_configured_audience_model)
        """

    def delete_configured_audience_model_policy(
        self, **kwargs: Unpack[DeleteConfiguredAudienceModelPolicyRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified configured audience model policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.delete_configured_audience_model_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#delete_configured_audience_model_policy)
        """

    def delete_training_dataset(
        self, **kwargs: Unpack[DeleteTrainingDatasetRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Specifies a training dataset that you want to delete.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.delete_training_dataset)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#delete_training_dataset)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#generate_presigned_url)
        """

    def get_audience_generation_job(
        self, **kwargs: Unpack[GetAudienceGenerationJobRequestRequestTypeDef]
    ) -> GetAudienceGenerationJobResponseTypeDef:
        """
        Returns information about an audience generation job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.get_audience_generation_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_audience_generation_job)
        """

    def get_audience_model(
        self, **kwargs: Unpack[GetAudienceModelRequestRequestTypeDef]
    ) -> GetAudienceModelResponseTypeDef:
        """
        Returns information about an audience model See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/cleanroomsml-2023-09-06/GetAudienceModel).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.get_audience_model)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_audience_model)
        """

    def get_configured_audience_model(
        self, **kwargs: Unpack[GetConfiguredAudienceModelRequestRequestTypeDef]
    ) -> GetConfiguredAudienceModelResponseTypeDef:
        """
        Returns information about a specified configured audience model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.get_configured_audience_model)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_configured_audience_model)
        """

    def get_configured_audience_model_policy(
        self, **kwargs: Unpack[GetConfiguredAudienceModelPolicyRequestRequestTypeDef]
    ) -> GetConfiguredAudienceModelPolicyResponseTypeDef:
        """
        Returns information about a configured audience model policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.get_configured_audience_model_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_configured_audience_model_policy)
        """

    def get_training_dataset(
        self, **kwargs: Unpack[GetTrainingDatasetRequestRequestTypeDef]
    ) -> GetTrainingDatasetResponseTypeDef:
        """
        Returns information about a training dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.get_training_dataset)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_training_dataset)
        """

    def list_audience_export_jobs(
        self, **kwargs: Unpack[ListAudienceExportJobsRequestRequestTypeDef]
    ) -> ListAudienceExportJobsResponseTypeDef:
        """
        Returns a list of the audience export jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.list_audience_export_jobs)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#list_audience_export_jobs)
        """

    def list_audience_generation_jobs(
        self, **kwargs: Unpack[ListAudienceGenerationJobsRequestRequestTypeDef]
    ) -> ListAudienceGenerationJobsResponseTypeDef:
        """
        Returns a list of audience generation jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.list_audience_generation_jobs)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#list_audience_generation_jobs)
        """

    def list_audience_models(
        self, **kwargs: Unpack[ListAudienceModelsRequestRequestTypeDef]
    ) -> ListAudienceModelsResponseTypeDef:
        """
        Returns a list of audience models.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.list_audience_models)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#list_audience_models)
        """

    def list_configured_audience_models(
        self, **kwargs: Unpack[ListConfiguredAudienceModelsRequestRequestTypeDef]
    ) -> ListConfiguredAudienceModelsResponseTypeDef:
        """
        Returns a list of the configured audience models.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.list_configured_audience_models)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#list_configured_audience_models)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags for a provided resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.list_tags_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#list_tags_for_resource)
        """

    def list_training_datasets(
        self, **kwargs: Unpack[ListTrainingDatasetsRequestRequestTypeDef]
    ) -> ListTrainingDatasetsResponseTypeDef:
        """
        Returns a list of training datasets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.list_training_datasets)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#list_training_datasets)
        """

    def put_configured_audience_model_policy(
        self, **kwargs: Unpack[PutConfiguredAudienceModelPolicyRequestRequestTypeDef]
    ) -> PutConfiguredAudienceModelPolicyResponseTypeDef:
        """
        Create or update the resource policy for a configured audience model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.put_configured_audience_model_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#put_configured_audience_model_policy)
        """

    def start_audience_export_job(
        self, **kwargs: Unpack[StartAudienceExportJobRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Export an audience of a specified size after you have generated an audience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.start_audience_export_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#start_audience_export_job)
        """

    def start_audience_generation_job(
        self, **kwargs: Unpack[StartAudienceGenerationJobRequestRequestTypeDef]
    ) -> StartAudienceGenerationJobResponseTypeDef:
        """
        Information necessary to start the audience generation job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.start_audience_generation_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#start_audience_generation_job)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds metadata tags to a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes metadata tags from a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#untag_resource)
        """

    def update_configured_audience_model(
        self, **kwargs: Unpack[UpdateConfiguredAudienceModelRequestRequestTypeDef]
    ) -> UpdateConfiguredAudienceModelResponseTypeDef:
        """
        Provides the information necessary to update a configured audience model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.update_configured_audience_model)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#update_configured_audience_model)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_audience_export_jobs"]
    ) -> ListAudienceExportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_audience_generation_jobs"]
    ) -> ListAudienceGenerationJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_audience_models"]
    ) -> ListAudienceModelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_configured_audience_models"]
    ) -> ListConfiguredAudienceModelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_training_datasets"]
    ) -> ListTrainingDatasetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cleanroomsml.html#CleanRoomsML.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanroomsml/client/#get_paginator)
        """
