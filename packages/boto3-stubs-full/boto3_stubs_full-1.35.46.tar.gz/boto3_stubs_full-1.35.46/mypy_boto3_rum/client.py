"""
Type annotations for rum service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_rum.client import CloudWatchRUMClient

    session = Session()
    client: CloudWatchRUMClient = session.client("rum")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    BatchGetRumMetricDefinitionsPaginator,
    GetAppMonitorDataPaginator,
    ListAppMonitorsPaginator,
    ListRumMetricsDestinationsPaginator,
)
from .type_defs import (
    BatchCreateRumMetricDefinitionsRequestRequestTypeDef,
    BatchCreateRumMetricDefinitionsResponseTypeDef,
    BatchDeleteRumMetricDefinitionsRequestRequestTypeDef,
    BatchDeleteRumMetricDefinitionsResponseTypeDef,
    BatchGetRumMetricDefinitionsRequestRequestTypeDef,
    BatchGetRumMetricDefinitionsResponseTypeDef,
    CreateAppMonitorRequestRequestTypeDef,
    CreateAppMonitorResponseTypeDef,
    DeleteAppMonitorRequestRequestTypeDef,
    DeleteRumMetricsDestinationRequestRequestTypeDef,
    GetAppMonitorDataRequestRequestTypeDef,
    GetAppMonitorDataResponseTypeDef,
    GetAppMonitorRequestRequestTypeDef,
    GetAppMonitorResponseTypeDef,
    ListAppMonitorsRequestRequestTypeDef,
    ListAppMonitorsResponseTypeDef,
    ListRumMetricsDestinationsRequestRequestTypeDef,
    ListRumMetricsDestinationsResponseTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutRumEventsRequestRequestTypeDef,
    PutRumMetricsDestinationRequestRequestTypeDef,
    TagResourceRequestRequestTypeDef,
    UntagResourceRequestRequestTypeDef,
    UpdateAppMonitorRequestRequestTypeDef,
    UpdateRumMetricDefinitionRequestRequestTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack


__all__ = ("CloudWatchRUMClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class CloudWatchRUMClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CloudWatchRUMClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/client/#exceptions)
        """

    def batch_create_rum_metric_definitions(
        self, **kwargs: Unpack[BatchCreateRumMetricDefinitionsRequestRequestTypeDef]
    ) -> BatchCreateRumMetricDefinitionsResponseTypeDef:
        """
        Specifies the extended metrics and custom metrics that you want a CloudWatch
        RUM app monitor to send to a
        destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.batch_create_rum_metric_definitions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/client/#batch_create_rum_metric_definitions)
        """

    def batch_delete_rum_metric_definitions(
        self, **kwargs: Unpack[BatchDeleteRumMetricDefinitionsRequestRequestTypeDef]
    ) -> BatchDeleteRumMetricDefinitionsResponseTypeDef:
        """
        Removes the specified metrics from being sent to an extended metrics
        destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.batch_delete_rum_metric_definitions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/client/#batch_delete_rum_metric_definitions)
        """

    def batch_get_rum_metric_definitions(
        self, **kwargs: Unpack[BatchGetRumMetricDefinitionsRequestRequestTypeDef]
    ) -> BatchGetRumMetricDefinitionsResponseTypeDef:
        """
        Retrieves the list of metrics and dimensions that a RUM app monitor is sending
        to a single
        destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.batch_get_rum_metric_definitions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/client/#batch_get_rum_metric_definitions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/client/#close)
        """

    def create_app_monitor(
        self, **kwargs: Unpack[CreateAppMonitorRequestRequestTypeDef]
    ) -> CreateAppMonitorResponseTypeDef:
        """
        Creates a Amazon CloudWatch RUM app monitor, which collects telemetry data from
        your application and sends that data to
        RUM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.create_app_monitor)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/client/#create_app_monitor)
        """

    def delete_app_monitor(
        self, **kwargs: Unpack[DeleteAppMonitorRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an existing app monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.delete_app_monitor)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/client/#delete_app_monitor)
        """

    def delete_rum_metrics_destination(
        self, **kwargs: Unpack[DeleteRumMetricsDestinationRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a destination for CloudWatch RUM extended metrics, so that the
        specified app monitor stops sending extended metrics to that
        destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.delete_rum_metrics_destination)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/client/#delete_rum_metrics_destination)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/client/#generate_presigned_url)
        """

    def get_app_monitor(
        self, **kwargs: Unpack[GetAppMonitorRequestRequestTypeDef]
    ) -> GetAppMonitorResponseTypeDef:
        """
        Retrieves the complete configuration information for one app monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.get_app_monitor)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/client/#get_app_monitor)
        """

    def get_app_monitor_data(
        self, **kwargs: Unpack[GetAppMonitorDataRequestRequestTypeDef]
    ) -> GetAppMonitorDataResponseTypeDef:
        """
        Retrieves the raw performance events that RUM has collected from your web
        application, so that you can do your own processing or analysis of this
        data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.get_app_monitor_data)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/client/#get_app_monitor_data)
        """

    def list_app_monitors(
        self, **kwargs: Unpack[ListAppMonitorsRequestRequestTypeDef]
    ) -> ListAppMonitorsResponseTypeDef:
        """
        Returns a list of the Amazon CloudWatch RUM app monitors in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.list_app_monitors)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/client/#list_app_monitors)
        """

    def list_rum_metrics_destinations(
        self, **kwargs: Unpack[ListRumMetricsDestinationsRequestRequestTypeDef]
    ) -> ListRumMetricsDestinationsResponseTypeDef:
        """
        Returns a list of destinations that you have created to receive RUM extended
        metrics, for the specified app
        monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.list_rum_metrics_destinations)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/client/#list_rum_metrics_destinations)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Displays the tags associated with a CloudWatch RUM resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.list_tags_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/client/#list_tags_for_resource)
        """

    def put_rum_events(self, **kwargs: Unpack[PutRumEventsRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Sends telemetry events about your application performance and user behavior to
        CloudWatch
        RUM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.put_rum_events)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/client/#put_rum_events)
        """

    def put_rum_metrics_destination(
        self, **kwargs: Unpack[PutRumMetricsDestinationRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates or updates a destination to receive extended metrics from CloudWatch
        RUM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.put_rum_metrics_destination)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/client/#put_rum_metrics_destination)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified CloudWatch RUM
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes one or more tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/client/#untag_resource)
        """

    def update_app_monitor(
        self, **kwargs: Unpack[UpdateAppMonitorRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the configuration of an existing app monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.update_app_monitor)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/client/#update_app_monitor)
        """

    def update_rum_metric_definition(
        self, **kwargs: Unpack[UpdateRumMetricDefinitionRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Modifies one existing metric definition for CloudWatch RUM extended metrics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.update_rum_metric_definition)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/client/#update_rum_metric_definition)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["batch_get_rum_metric_definitions"]
    ) -> BatchGetRumMetricDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_app_monitor_data"]
    ) -> GetAppMonitorDataPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_app_monitors"]
    ) -> ListAppMonitorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_rum_metrics_destinations"]
    ) -> ListRumMetricsDestinationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum.html#CloudWatchRUM.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/client/#get_paginator)
        """
