"""
Type annotations for ce service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_ce.client import CostExplorerClient

    session = Session()
    client: CostExplorerClient = session.client("ce")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
    CreateAnomalyMonitorRequestRequestTypeDef,
    CreateAnomalyMonitorResponseTypeDef,
    CreateAnomalySubscriptionRequestRequestTypeDef,
    CreateAnomalySubscriptionResponseTypeDef,
    CreateCostCategoryDefinitionRequestRequestTypeDef,
    CreateCostCategoryDefinitionResponseTypeDef,
    DeleteAnomalyMonitorRequestRequestTypeDef,
    DeleteAnomalySubscriptionRequestRequestTypeDef,
    DeleteCostCategoryDefinitionRequestRequestTypeDef,
    DeleteCostCategoryDefinitionResponseTypeDef,
    DescribeCostCategoryDefinitionRequestRequestTypeDef,
    DescribeCostCategoryDefinitionResponseTypeDef,
    GetAnomaliesRequestRequestTypeDef,
    GetAnomaliesResponseTypeDef,
    GetAnomalyMonitorsRequestRequestTypeDef,
    GetAnomalyMonitorsResponseTypeDef,
    GetAnomalySubscriptionsRequestRequestTypeDef,
    GetAnomalySubscriptionsResponseTypeDef,
    GetApproximateUsageRecordsRequestRequestTypeDef,
    GetApproximateUsageRecordsResponseTypeDef,
    GetCostAndUsageRequestRequestTypeDef,
    GetCostAndUsageResponseTypeDef,
    GetCostAndUsageWithResourcesRequestRequestTypeDef,
    GetCostAndUsageWithResourcesResponseTypeDef,
    GetCostCategoriesRequestRequestTypeDef,
    GetCostCategoriesResponseTypeDef,
    GetCostForecastRequestRequestTypeDef,
    GetCostForecastResponseTypeDef,
    GetDimensionValuesRequestRequestTypeDef,
    GetDimensionValuesResponseTypeDef,
    GetReservationCoverageRequestRequestTypeDef,
    GetReservationCoverageResponseTypeDef,
    GetReservationPurchaseRecommendationRequestRequestTypeDef,
    GetReservationPurchaseRecommendationResponseTypeDef,
    GetReservationUtilizationRequestRequestTypeDef,
    GetReservationUtilizationResponseTypeDef,
    GetRightsizingRecommendationRequestRequestTypeDef,
    GetRightsizingRecommendationResponseTypeDef,
    GetSavingsPlanPurchaseRecommendationDetailsRequestRequestTypeDef,
    GetSavingsPlanPurchaseRecommendationDetailsResponseTypeDef,
    GetSavingsPlansCoverageRequestRequestTypeDef,
    GetSavingsPlansCoverageResponseTypeDef,
    GetSavingsPlansPurchaseRecommendationRequestRequestTypeDef,
    GetSavingsPlansPurchaseRecommendationResponseTypeDef,
    GetSavingsPlansUtilizationDetailsRequestRequestTypeDef,
    GetSavingsPlansUtilizationDetailsResponseTypeDef,
    GetSavingsPlansUtilizationRequestRequestTypeDef,
    GetSavingsPlansUtilizationResponseTypeDef,
    GetTagsRequestRequestTypeDef,
    GetTagsResponseTypeDef,
    GetUsageForecastRequestRequestTypeDef,
    GetUsageForecastResponseTypeDef,
    ListCostAllocationTagBackfillHistoryRequestRequestTypeDef,
    ListCostAllocationTagBackfillHistoryResponseTypeDef,
    ListCostAllocationTagsRequestRequestTypeDef,
    ListCostAllocationTagsResponseTypeDef,
    ListCostCategoryDefinitionsRequestRequestTypeDef,
    ListCostCategoryDefinitionsResponseTypeDef,
    ListSavingsPlansPurchaseRecommendationGenerationRequestRequestTypeDef,
    ListSavingsPlansPurchaseRecommendationGenerationResponseTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ProvideAnomalyFeedbackRequestRequestTypeDef,
    ProvideAnomalyFeedbackResponseTypeDef,
    StartCostAllocationTagBackfillRequestRequestTypeDef,
    StartCostAllocationTagBackfillResponseTypeDef,
    StartSavingsPlansPurchaseRecommendationGenerationResponseTypeDef,
    TagResourceRequestRequestTypeDef,
    UntagResourceRequestRequestTypeDef,
    UpdateAnomalyMonitorRequestRequestTypeDef,
    UpdateAnomalyMonitorResponseTypeDef,
    UpdateAnomalySubscriptionRequestRequestTypeDef,
    UpdateAnomalySubscriptionResponseTypeDef,
    UpdateCostAllocationTagsStatusRequestRequestTypeDef,
    UpdateCostAllocationTagsStatusResponseTypeDef,
    UpdateCostCategoryDefinitionRequestRequestTypeDef,
    UpdateCostCategoryDefinitionResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("CostExplorerClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    BackfillLimitExceededException: Type[BotocoreClientError]
    BillExpirationException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DataUnavailableException: Type[BotocoreClientError]
    GenerationExistsException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    RequestChangedException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    UnknownMonitorException: Type[BotocoreClientError]
    UnknownSubscriptionException: Type[BotocoreClientError]
    UnresolvableUsageUnitException: Type[BotocoreClientError]

class CostExplorerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CostExplorerClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#close)
        """

    def create_anomaly_monitor(
        self, **kwargs: Unpack[CreateAnomalyMonitorRequestRequestTypeDef]
    ) -> CreateAnomalyMonitorResponseTypeDef:
        """
        Creates a new cost anomaly detection monitor with the requested type and
        monitor
        specification.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.create_anomaly_monitor)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#create_anomaly_monitor)
        """

    def create_anomaly_subscription(
        self, **kwargs: Unpack[CreateAnomalySubscriptionRequestRequestTypeDef]
    ) -> CreateAnomalySubscriptionResponseTypeDef:
        """
        Adds an alert subscription to a cost anomaly detection monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.create_anomaly_subscription)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#create_anomaly_subscription)
        """

    def create_cost_category_definition(
        self, **kwargs: Unpack[CreateCostCategoryDefinitionRequestRequestTypeDef]
    ) -> CreateCostCategoryDefinitionResponseTypeDef:
        """
        Creates a new Cost Category with the requested name and rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.create_cost_category_definition)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#create_cost_category_definition)
        """

    def delete_anomaly_monitor(
        self, **kwargs: Unpack[DeleteAnomalyMonitorRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a cost anomaly monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.delete_anomaly_monitor)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#delete_anomaly_monitor)
        """

    def delete_anomaly_subscription(
        self, **kwargs: Unpack[DeleteAnomalySubscriptionRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a cost anomaly subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.delete_anomaly_subscription)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#delete_anomaly_subscription)
        """

    def delete_cost_category_definition(
        self, **kwargs: Unpack[DeleteCostCategoryDefinitionRequestRequestTypeDef]
    ) -> DeleteCostCategoryDefinitionResponseTypeDef:
        """
        Deletes a Cost Category.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.delete_cost_category_definition)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#delete_cost_category_definition)
        """

    def describe_cost_category_definition(
        self, **kwargs: Unpack[DescribeCostCategoryDefinitionRequestRequestTypeDef]
    ) -> DescribeCostCategoryDefinitionResponseTypeDef:
        """
        Returns the name, Amazon Resource Name (ARN), rules, definition, and effective
        dates of a Cost Category that's defined in the
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.describe_cost_category_definition)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#describe_cost_category_definition)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#generate_presigned_url)
        """

    def get_anomalies(
        self, **kwargs: Unpack[GetAnomaliesRequestRequestTypeDef]
    ) -> GetAnomaliesResponseTypeDef:
        """
        Retrieves all of the cost anomalies detected on your account during the time
        period that's specified by the `DateInterval`
        object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_anomalies)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_anomalies)
        """

    def get_anomaly_monitors(
        self, **kwargs: Unpack[GetAnomalyMonitorsRequestRequestTypeDef]
    ) -> GetAnomalyMonitorsResponseTypeDef:
        """
        Retrieves the cost anomaly monitor definitions for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_anomaly_monitors)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_anomaly_monitors)
        """

    def get_anomaly_subscriptions(
        self, **kwargs: Unpack[GetAnomalySubscriptionsRequestRequestTypeDef]
    ) -> GetAnomalySubscriptionsResponseTypeDef:
        """
        Retrieves the cost anomaly subscription objects for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_anomaly_subscriptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_anomaly_subscriptions)
        """

    def get_approximate_usage_records(
        self, **kwargs: Unpack[GetApproximateUsageRecordsRequestRequestTypeDef]
    ) -> GetApproximateUsageRecordsResponseTypeDef:
        """
        Retrieves estimated usage records for hourly granularity or resource-level data
        at daily
        granularity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_approximate_usage_records)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_approximate_usage_records)
        """

    def get_cost_and_usage(
        self, **kwargs: Unpack[GetCostAndUsageRequestRequestTypeDef]
    ) -> GetCostAndUsageResponseTypeDef:
        """
        Retrieves cost and usage metrics for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_cost_and_usage)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_cost_and_usage)
        """

    def get_cost_and_usage_with_resources(
        self, **kwargs: Unpack[GetCostAndUsageWithResourcesRequestRequestTypeDef]
    ) -> GetCostAndUsageWithResourcesResponseTypeDef:
        """
        Retrieves cost and usage metrics with resources for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_cost_and_usage_with_resources)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_cost_and_usage_with_resources)
        """

    def get_cost_categories(
        self, **kwargs: Unpack[GetCostCategoriesRequestRequestTypeDef]
    ) -> GetCostCategoriesResponseTypeDef:
        """
        Retrieves an array of Cost Category names and values incurred cost.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_cost_categories)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_cost_categories)
        """

    def get_cost_forecast(
        self, **kwargs: Unpack[GetCostForecastRequestRequestTypeDef]
    ) -> GetCostForecastResponseTypeDef:
        """
        Retrieves a forecast for how much Amazon Web Services predicts that you will
        spend over the forecast time period that you select, based on your past
        costs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_cost_forecast)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_cost_forecast)
        """

    def get_dimension_values(
        self, **kwargs: Unpack[GetDimensionValuesRequestRequestTypeDef]
    ) -> GetDimensionValuesResponseTypeDef:
        """
        Retrieves all available filter values for a specified filter over a period of
        time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_dimension_values)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_dimension_values)
        """

    def get_reservation_coverage(
        self, **kwargs: Unpack[GetReservationCoverageRequestRequestTypeDef]
    ) -> GetReservationCoverageResponseTypeDef:
        """
        Retrieves the reservation coverage for your account, which you can use to see
        how much of your Amazon Elastic Compute Cloud, Amazon ElastiCache, Amazon
        Relational Database Service, or Amazon Redshift usage is covered by a
        reservation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_reservation_coverage)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_reservation_coverage)
        """

    def get_reservation_purchase_recommendation(
        self, **kwargs: Unpack[GetReservationPurchaseRecommendationRequestRequestTypeDef]
    ) -> GetReservationPurchaseRecommendationResponseTypeDef:
        """
        Gets recommendations for reservation purchases.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_reservation_purchase_recommendation)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_reservation_purchase_recommendation)
        """

    def get_reservation_utilization(
        self, **kwargs: Unpack[GetReservationUtilizationRequestRequestTypeDef]
    ) -> GetReservationUtilizationResponseTypeDef:
        """
        Retrieves the reservation utilization for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_reservation_utilization)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_reservation_utilization)
        """

    def get_rightsizing_recommendation(
        self, **kwargs: Unpack[GetRightsizingRecommendationRequestRequestTypeDef]
    ) -> GetRightsizingRecommendationResponseTypeDef:
        """
        Creates recommendations that help you save cost by identifying idle and
        underutilized Amazon EC2
        instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_rightsizing_recommendation)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_rightsizing_recommendation)
        """

    def get_savings_plan_purchase_recommendation_details(
        self, **kwargs: Unpack[GetSavingsPlanPurchaseRecommendationDetailsRequestRequestTypeDef]
    ) -> GetSavingsPlanPurchaseRecommendationDetailsResponseTypeDef:
        """
        Retrieves the details for a Savings Plan recommendation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_savings_plan_purchase_recommendation_details)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_savings_plan_purchase_recommendation_details)
        """

    def get_savings_plans_coverage(
        self, **kwargs: Unpack[GetSavingsPlansCoverageRequestRequestTypeDef]
    ) -> GetSavingsPlansCoverageResponseTypeDef:
        """
        Retrieves the Savings Plans covered for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_savings_plans_coverage)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_savings_plans_coverage)
        """

    def get_savings_plans_purchase_recommendation(
        self, **kwargs: Unpack[GetSavingsPlansPurchaseRecommendationRequestRequestTypeDef]
    ) -> GetSavingsPlansPurchaseRecommendationResponseTypeDef:
        """
        Retrieves the Savings Plans recommendations for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_savings_plans_purchase_recommendation)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_savings_plans_purchase_recommendation)
        """

    def get_savings_plans_utilization(
        self, **kwargs: Unpack[GetSavingsPlansUtilizationRequestRequestTypeDef]
    ) -> GetSavingsPlansUtilizationResponseTypeDef:
        """
        Retrieves the Savings Plans utilization for your account across date ranges
        with daily or monthly
        granularity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_savings_plans_utilization)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_savings_plans_utilization)
        """

    def get_savings_plans_utilization_details(
        self, **kwargs: Unpack[GetSavingsPlansUtilizationDetailsRequestRequestTypeDef]
    ) -> GetSavingsPlansUtilizationDetailsResponseTypeDef:
        """
        Retrieves attribute data along with aggregate utilization and savings data for
        a given time
        period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_savings_plans_utilization_details)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_savings_plans_utilization_details)
        """

    def get_tags(self, **kwargs: Unpack[GetTagsRequestRequestTypeDef]) -> GetTagsResponseTypeDef:
        """
        Queries for available tag keys and tag values for a specified period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_tags)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_tags)
        """

    def get_usage_forecast(
        self, **kwargs: Unpack[GetUsageForecastRequestRequestTypeDef]
    ) -> GetUsageForecastResponseTypeDef:
        """
        Retrieves a forecast for how much Amazon Web Services predicts that you will
        use over the forecast time period that you select, based on your past
        usage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.get_usage_forecast)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#get_usage_forecast)
        """

    def list_cost_allocation_tag_backfill_history(
        self, **kwargs: Unpack[ListCostAllocationTagBackfillHistoryRequestRequestTypeDef]
    ) -> ListCostAllocationTagBackfillHistoryResponseTypeDef:
        """
        Retrieves a list of your historical cost allocation tag backfill requests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.list_cost_allocation_tag_backfill_history)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#list_cost_allocation_tag_backfill_history)
        """

    def list_cost_allocation_tags(
        self, **kwargs: Unpack[ListCostAllocationTagsRequestRequestTypeDef]
    ) -> ListCostAllocationTagsResponseTypeDef:
        """
        Get a list of cost allocation tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.list_cost_allocation_tags)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#list_cost_allocation_tags)
        """

    def list_cost_category_definitions(
        self, **kwargs: Unpack[ListCostCategoryDefinitionsRequestRequestTypeDef]
    ) -> ListCostCategoryDefinitionsResponseTypeDef:
        """
        Returns the name, Amazon Resource Name (ARN), `NumberOfRules` and effective
        dates of all Cost Categories defined in the
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.list_cost_category_definitions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#list_cost_category_definitions)
        """

    def list_savings_plans_purchase_recommendation_generation(
        self,
        **kwargs: Unpack[ListSavingsPlansPurchaseRecommendationGenerationRequestRequestTypeDef],
    ) -> ListSavingsPlansPurchaseRecommendationGenerationResponseTypeDef:
        """
        Retrieves a list of your historical recommendation generations within the past
        30
        days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.list_savings_plans_purchase_recommendation_generation)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#list_savings_plans_purchase_recommendation_generation)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of resource tags associated with the resource specified by the
        Amazon Resource Name
        (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.list_tags_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#list_tags_for_resource)
        """

    def provide_anomaly_feedback(
        self, **kwargs: Unpack[ProvideAnomalyFeedbackRequestRequestTypeDef]
    ) -> ProvideAnomalyFeedbackResponseTypeDef:
        """
        Modifies the feedback property of a given cost anomaly.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.provide_anomaly_feedback)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#provide_anomaly_feedback)
        """

    def start_cost_allocation_tag_backfill(
        self, **kwargs: Unpack[StartCostAllocationTagBackfillRequestRequestTypeDef]
    ) -> StartCostAllocationTagBackfillResponseTypeDef:
        """
        Request a cost allocation tag backfill.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.start_cost_allocation_tag_backfill)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#start_cost_allocation_tag_backfill)
        """

    def start_savings_plans_purchase_recommendation_generation(
        self,
    ) -> StartSavingsPlansPurchaseRecommendationGenerationResponseTypeDef:
        """
        Requests a Savings Plans recommendation generation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.start_savings_plans_purchase_recommendation_generation)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#start_savings_plans_purchase_recommendation_generation)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        An API operation for adding one or more tags (key-value pairs) to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes one or more tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#untag_resource)
        """

    def update_anomaly_monitor(
        self, **kwargs: Unpack[UpdateAnomalyMonitorRequestRequestTypeDef]
    ) -> UpdateAnomalyMonitorResponseTypeDef:
        """
        Updates an existing cost anomaly monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.update_anomaly_monitor)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#update_anomaly_monitor)
        """

    def update_anomaly_subscription(
        self, **kwargs: Unpack[UpdateAnomalySubscriptionRequestRequestTypeDef]
    ) -> UpdateAnomalySubscriptionResponseTypeDef:
        """
        Updates an existing cost anomaly subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.update_anomaly_subscription)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#update_anomaly_subscription)
        """

    def update_cost_allocation_tags_status(
        self, **kwargs: Unpack[UpdateCostAllocationTagsStatusRequestRequestTypeDef]
    ) -> UpdateCostAllocationTagsStatusResponseTypeDef:
        """
        Updates status for cost allocation tags in bulk, with maximum batch size of 20.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.update_cost_allocation_tags_status)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#update_cost_allocation_tags_status)
        """

    def update_cost_category_definition(
        self, **kwargs: Unpack[UpdateCostCategoryDefinitionRequestRequestTypeDef]
    ) -> UpdateCostCategoryDefinitionResponseTypeDef:
        """
        Updates an existing Cost Category.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce.html#CostExplorer.Client.update_cost_category_definition)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/client/#update_cost_category_definition)
        """
