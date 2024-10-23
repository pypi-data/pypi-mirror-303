"""
Type annotations for machinelearning service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_machinelearning.client import MachineLearningClient

    session = Session()
    client: MachineLearningClient = session.client("machinelearning")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    DescribeBatchPredictionsPaginator,
    DescribeDataSourcesPaginator,
    DescribeEvaluationsPaginator,
    DescribeMLModelsPaginator,
)
from .type_defs import (
    AddTagsInputRequestTypeDef,
    AddTagsOutputTypeDef,
    CreateBatchPredictionInputRequestTypeDef,
    CreateBatchPredictionOutputTypeDef,
    CreateDataSourceFromRDSInputRequestTypeDef,
    CreateDataSourceFromRDSOutputTypeDef,
    CreateDataSourceFromRedshiftInputRequestTypeDef,
    CreateDataSourceFromRedshiftOutputTypeDef,
    CreateDataSourceFromS3InputRequestTypeDef,
    CreateDataSourceFromS3OutputTypeDef,
    CreateEvaluationInputRequestTypeDef,
    CreateEvaluationOutputTypeDef,
    CreateMLModelInputRequestTypeDef,
    CreateMLModelOutputTypeDef,
    CreateRealtimeEndpointInputRequestTypeDef,
    CreateRealtimeEndpointOutputTypeDef,
    DeleteBatchPredictionInputRequestTypeDef,
    DeleteBatchPredictionOutputTypeDef,
    DeleteDataSourceInputRequestTypeDef,
    DeleteDataSourceOutputTypeDef,
    DeleteEvaluationInputRequestTypeDef,
    DeleteEvaluationOutputTypeDef,
    DeleteMLModelInputRequestTypeDef,
    DeleteMLModelOutputTypeDef,
    DeleteRealtimeEndpointInputRequestTypeDef,
    DeleteRealtimeEndpointOutputTypeDef,
    DeleteTagsInputRequestTypeDef,
    DeleteTagsOutputTypeDef,
    DescribeBatchPredictionsInputRequestTypeDef,
    DescribeBatchPredictionsOutputTypeDef,
    DescribeDataSourcesInputRequestTypeDef,
    DescribeDataSourcesOutputTypeDef,
    DescribeEvaluationsInputRequestTypeDef,
    DescribeEvaluationsOutputTypeDef,
    DescribeMLModelsInputRequestTypeDef,
    DescribeMLModelsOutputTypeDef,
    DescribeTagsInputRequestTypeDef,
    DescribeTagsOutputTypeDef,
    GetBatchPredictionInputRequestTypeDef,
    GetBatchPredictionOutputTypeDef,
    GetDataSourceInputRequestTypeDef,
    GetDataSourceOutputTypeDef,
    GetEvaluationInputRequestTypeDef,
    GetEvaluationOutputTypeDef,
    GetMLModelInputRequestTypeDef,
    GetMLModelOutputTypeDef,
    PredictInputRequestTypeDef,
    PredictOutputTypeDef,
    UpdateBatchPredictionInputRequestTypeDef,
    UpdateBatchPredictionOutputTypeDef,
    UpdateDataSourceInputRequestTypeDef,
    UpdateDataSourceOutputTypeDef,
    UpdateEvaluationInputRequestTypeDef,
    UpdateEvaluationOutputTypeDef,
    UpdateMLModelInputRequestTypeDef,
    UpdateMLModelOutputTypeDef,
)
from .waiter import (
    BatchPredictionAvailableWaiter,
    DataSourceAvailableWaiter,
    EvaluationAvailableWaiter,
    MLModelAvailableWaiter,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack


__all__ = ("MachineLearningClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    IdempotentParameterMismatchException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    InvalidTagException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    PredictorNotMountedException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TagLimitExceededException: Type[BotocoreClientError]


class MachineLearningClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MachineLearningClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#exceptions)
        """

    def add_tags(self, **kwargs: Unpack[AddTagsInputRequestTypeDef]) -> AddTagsOutputTypeDef:
        """
        Adds one or more tags to an object, up to a limit of 10.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.add_tags)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#add_tags)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#close)
        """

    def create_batch_prediction(
        self, **kwargs: Unpack[CreateBatchPredictionInputRequestTypeDef]
    ) -> CreateBatchPredictionOutputTypeDef:
        """
        Generates predictions for a group of observations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.create_batch_prediction)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#create_batch_prediction)
        """

    def create_data_source_from_rds(
        self, **kwargs: Unpack[CreateDataSourceFromRDSInputRequestTypeDef]
    ) -> CreateDataSourceFromRDSOutputTypeDef:
        """
        Creates a `DataSource` object from an `Amazon Relational Database Service
        <http://aws.amazon.com/rds/>`__ (Amazon
        RDS).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.create_data_source_from_rds)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#create_data_source_from_rds)
        """

    def create_data_source_from_redshift(
        self, **kwargs: Unpack[CreateDataSourceFromRedshiftInputRequestTypeDef]
    ) -> CreateDataSourceFromRedshiftOutputTypeDef:
        """
        Creates a `DataSource` from a database hosted on an Amazon Redshift cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.create_data_source_from_redshift)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#create_data_source_from_redshift)
        """

    def create_data_source_from_s3(
        self, **kwargs: Unpack[CreateDataSourceFromS3InputRequestTypeDef]
    ) -> CreateDataSourceFromS3OutputTypeDef:
        """
        Creates a `DataSource` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.create_data_source_from_s3)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#create_data_source_from_s3)
        """

    def create_evaluation(
        self, **kwargs: Unpack[CreateEvaluationInputRequestTypeDef]
    ) -> CreateEvaluationOutputTypeDef:
        """
        Creates a new `Evaluation` of an `MLModel`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.create_evaluation)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#create_evaluation)
        """

    def create_ml_model(
        self, **kwargs: Unpack[CreateMLModelInputRequestTypeDef]
    ) -> CreateMLModelOutputTypeDef:
        """
        Creates a new `MLModel` using the `DataSource` and the recipe as information
        sources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.create_ml_model)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#create_ml_model)
        """

    def create_realtime_endpoint(
        self, **kwargs: Unpack[CreateRealtimeEndpointInputRequestTypeDef]
    ) -> CreateRealtimeEndpointOutputTypeDef:
        """
        Creates a real-time endpoint for the `MLModel`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.create_realtime_endpoint)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#create_realtime_endpoint)
        """

    def delete_batch_prediction(
        self, **kwargs: Unpack[DeleteBatchPredictionInputRequestTypeDef]
    ) -> DeleteBatchPredictionOutputTypeDef:
        """
        Assigns the DELETED status to a `BatchPrediction`, rendering it unusable.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.delete_batch_prediction)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#delete_batch_prediction)
        """

    def delete_data_source(
        self, **kwargs: Unpack[DeleteDataSourceInputRequestTypeDef]
    ) -> DeleteDataSourceOutputTypeDef:
        """
        Assigns the DELETED status to a `DataSource`, rendering it unusable.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.delete_data_source)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#delete_data_source)
        """

    def delete_evaluation(
        self, **kwargs: Unpack[DeleteEvaluationInputRequestTypeDef]
    ) -> DeleteEvaluationOutputTypeDef:
        """
        Assigns the `DELETED` status to an `Evaluation`, rendering it unusable.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.delete_evaluation)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#delete_evaluation)
        """

    def delete_ml_model(
        self, **kwargs: Unpack[DeleteMLModelInputRequestTypeDef]
    ) -> DeleteMLModelOutputTypeDef:
        """
        Assigns the `DELETED` status to an `MLModel`, rendering it unusable.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.delete_ml_model)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#delete_ml_model)
        """

    def delete_realtime_endpoint(
        self, **kwargs: Unpack[DeleteRealtimeEndpointInputRequestTypeDef]
    ) -> DeleteRealtimeEndpointOutputTypeDef:
        """
        Deletes a real time endpoint of an `MLModel`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.delete_realtime_endpoint)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#delete_realtime_endpoint)
        """

    def delete_tags(
        self, **kwargs: Unpack[DeleteTagsInputRequestTypeDef]
    ) -> DeleteTagsOutputTypeDef:
        """
        Deletes the specified tags associated with an ML object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.delete_tags)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#delete_tags)
        """

    def describe_batch_predictions(
        self, **kwargs: Unpack[DescribeBatchPredictionsInputRequestTypeDef]
    ) -> DescribeBatchPredictionsOutputTypeDef:
        """
        Returns a list of `BatchPrediction` operations that match the search criteria
        in the
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.describe_batch_predictions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#describe_batch_predictions)
        """

    def describe_data_sources(
        self, **kwargs: Unpack[DescribeDataSourcesInputRequestTypeDef]
    ) -> DescribeDataSourcesOutputTypeDef:
        """
        Returns a list of `DataSource` that match the search criteria in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.describe_data_sources)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#describe_data_sources)
        """

    def describe_evaluations(
        self, **kwargs: Unpack[DescribeEvaluationsInputRequestTypeDef]
    ) -> DescribeEvaluationsOutputTypeDef:
        """
        Returns a list of `DescribeEvaluations` that match the search criteria in the
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.describe_evaluations)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#describe_evaluations)
        """

    def describe_ml_models(
        self, **kwargs: Unpack[DescribeMLModelsInputRequestTypeDef]
    ) -> DescribeMLModelsOutputTypeDef:
        """
        Returns a list of `MLModel` that match the search criteria in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.describe_ml_models)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#describe_ml_models)
        """

    def describe_tags(
        self, **kwargs: Unpack[DescribeTagsInputRequestTypeDef]
    ) -> DescribeTagsOutputTypeDef:
        """
        Describes one or more of the tags for your Amazon ML object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.describe_tags)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#describe_tags)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#generate_presigned_url)
        """

    def get_batch_prediction(
        self, **kwargs: Unpack[GetBatchPredictionInputRequestTypeDef]
    ) -> GetBatchPredictionOutputTypeDef:
        """
        Returns a `BatchPrediction` that includes detailed metadata, status, and data
        file information for a `Batch Prediction`
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.get_batch_prediction)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#get_batch_prediction)
        """

    def get_data_source(
        self, **kwargs: Unpack[GetDataSourceInputRequestTypeDef]
    ) -> GetDataSourceOutputTypeDef:
        """
        Returns a `DataSource` that includes metadata and data file information, as
        well as the current status of the
        `DataSource`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.get_data_source)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#get_data_source)
        """

    def get_evaluation(
        self, **kwargs: Unpack[GetEvaluationInputRequestTypeDef]
    ) -> GetEvaluationOutputTypeDef:
        """
        Returns an `Evaluation` that includes metadata as well as the current status of
        the
        `Evaluation`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.get_evaluation)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#get_evaluation)
        """

    def get_ml_model(
        self, **kwargs: Unpack[GetMLModelInputRequestTypeDef]
    ) -> GetMLModelOutputTypeDef:
        """
        Returns an `MLModel` that includes detailed metadata, data source information,
        and the current status of the
        `MLModel`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.get_ml_model)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#get_ml_model)
        """

    def predict(self, **kwargs: Unpack[PredictInputRequestTypeDef]) -> PredictOutputTypeDef:
        """
        Generates a prediction for the observation using the specified `ML Model`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.predict)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#predict)
        """

    def update_batch_prediction(
        self, **kwargs: Unpack[UpdateBatchPredictionInputRequestTypeDef]
    ) -> UpdateBatchPredictionOutputTypeDef:
        """
        Updates the `BatchPredictionName` of a `BatchPrediction`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.update_batch_prediction)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#update_batch_prediction)
        """

    def update_data_source(
        self, **kwargs: Unpack[UpdateDataSourceInputRequestTypeDef]
    ) -> UpdateDataSourceOutputTypeDef:
        """
        Updates the `DataSourceName` of a `DataSource`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.update_data_source)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#update_data_source)
        """

    def update_evaluation(
        self, **kwargs: Unpack[UpdateEvaluationInputRequestTypeDef]
    ) -> UpdateEvaluationOutputTypeDef:
        """
        Updates the `EvaluationName` of an `Evaluation`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.update_evaluation)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#update_evaluation)
        """

    def update_ml_model(
        self, **kwargs: Unpack[UpdateMLModelInputRequestTypeDef]
    ) -> UpdateMLModelOutputTypeDef:
        """
        Updates the `MLModelName` and the `ScoreThreshold` of an `MLModel`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.update_ml_model)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#update_ml_model)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_batch_predictions"]
    ) -> DescribeBatchPredictionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_data_sources"]
    ) -> DescribeDataSourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_evaluations"]
    ) -> DescribeEvaluationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_ml_models"]
    ) -> DescribeMLModelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#get_paginator)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["batch_prediction_available"]
    ) -> BatchPredictionAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["data_source_available"]
    ) -> DataSourceAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["evaluation_available"]) -> EvaluationAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["ml_model_available"]) -> MLModelAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#get_waiter)
        """
