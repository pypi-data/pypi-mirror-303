"""
Type annotations for appflow service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_appflow.client import AppflowClient

    session = Session()
    client: AppflowClient = session.client("appflow")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
    CancelFlowExecutionsRequestRequestTypeDef,
    CancelFlowExecutionsResponseTypeDef,
    CreateConnectorProfileRequestRequestTypeDef,
    CreateConnectorProfileResponseTypeDef,
    CreateFlowRequestRequestTypeDef,
    CreateFlowResponseTypeDef,
    DeleteConnectorProfileRequestRequestTypeDef,
    DeleteFlowRequestRequestTypeDef,
    DescribeConnectorEntityRequestRequestTypeDef,
    DescribeConnectorEntityResponseTypeDef,
    DescribeConnectorProfilesRequestRequestTypeDef,
    DescribeConnectorProfilesResponseTypeDef,
    DescribeConnectorRequestRequestTypeDef,
    DescribeConnectorResponseTypeDef,
    DescribeConnectorsRequestRequestTypeDef,
    DescribeConnectorsResponseTypeDef,
    DescribeFlowExecutionRecordsRequestRequestTypeDef,
    DescribeFlowExecutionRecordsResponseTypeDef,
    DescribeFlowRequestRequestTypeDef,
    DescribeFlowResponseTypeDef,
    ListConnectorEntitiesRequestRequestTypeDef,
    ListConnectorEntitiesResponseTypeDef,
    ListConnectorsRequestRequestTypeDef,
    ListConnectorsResponseTypeDef,
    ListFlowsRequestRequestTypeDef,
    ListFlowsResponseTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    RegisterConnectorRequestRequestTypeDef,
    RegisterConnectorResponseTypeDef,
    ResetConnectorMetadataCacheRequestRequestTypeDef,
    StartFlowRequestRequestTypeDef,
    StartFlowResponseTypeDef,
    StopFlowRequestRequestTypeDef,
    StopFlowResponseTypeDef,
    TagResourceRequestRequestTypeDef,
    UnregisterConnectorRequestRequestTypeDef,
    UntagResourceRequestRequestTypeDef,
    UpdateConnectorProfileRequestRequestTypeDef,
    UpdateConnectorProfileResponseTypeDef,
    UpdateConnectorRegistrationRequestRequestTypeDef,
    UpdateConnectorRegistrationResponseTypeDef,
    UpdateFlowRequestRequestTypeDef,
    UpdateFlowResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack


__all__ = ("AppflowClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ConnectorAuthenticationException: Type[BotocoreClientError]
    ConnectorServerException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class AppflowClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AppflowClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#can_paginate)
        """

    def cancel_flow_executions(
        self, **kwargs: Unpack[CancelFlowExecutionsRequestRequestTypeDef]
    ) -> CancelFlowExecutionsResponseTypeDef:
        """
        Cancels active runs for a flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.cancel_flow_executions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#cancel_flow_executions)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#close)
        """

    def create_connector_profile(
        self, **kwargs: Unpack[CreateConnectorProfileRequestRequestTypeDef]
    ) -> CreateConnectorProfileResponseTypeDef:
        """
        Creates a new connector profile associated with your Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.create_connector_profile)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#create_connector_profile)
        """

    def create_flow(
        self, **kwargs: Unpack[CreateFlowRequestRequestTypeDef]
    ) -> CreateFlowResponseTypeDef:
        """
        Enables your application to create a new flow using Amazon AppFlow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.create_flow)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#create_flow)
        """

    def delete_connector_profile(
        self, **kwargs: Unpack[DeleteConnectorProfileRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Enables you to delete an existing connector profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.delete_connector_profile)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#delete_connector_profile)
        """

    def delete_flow(self, **kwargs: Unpack[DeleteFlowRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Enables your application to delete an existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.delete_flow)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#delete_flow)
        """

    def describe_connector(
        self, **kwargs: Unpack[DescribeConnectorRequestRequestTypeDef]
    ) -> DescribeConnectorResponseTypeDef:
        """
        Describes the given custom connector registered in your Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.describe_connector)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#describe_connector)
        """

    def describe_connector_entity(
        self, **kwargs: Unpack[DescribeConnectorEntityRequestRequestTypeDef]
    ) -> DescribeConnectorEntityResponseTypeDef:
        """
        Provides details regarding the entity used with the connector, with a
        description of the data model for each field in that
        entity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.describe_connector_entity)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#describe_connector_entity)
        """

    def describe_connector_profiles(
        self, **kwargs: Unpack[DescribeConnectorProfilesRequestRequestTypeDef]
    ) -> DescribeConnectorProfilesResponseTypeDef:
        """
        Returns a list of `connector-profile` details matching the provided
        `connector-profile` names and
        `connector-types`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.describe_connector_profiles)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#describe_connector_profiles)
        """

    def describe_connectors(
        self, **kwargs: Unpack[DescribeConnectorsRequestRequestTypeDef]
    ) -> DescribeConnectorsResponseTypeDef:
        """
        Describes the connectors vended by Amazon AppFlow for specified connector types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.describe_connectors)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#describe_connectors)
        """

    def describe_flow(
        self, **kwargs: Unpack[DescribeFlowRequestRequestTypeDef]
    ) -> DescribeFlowResponseTypeDef:
        """
        Provides a description of the specified flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.describe_flow)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#describe_flow)
        """

    def describe_flow_execution_records(
        self, **kwargs: Unpack[DescribeFlowExecutionRecordsRequestRequestTypeDef]
    ) -> DescribeFlowExecutionRecordsResponseTypeDef:
        """
        Fetches the execution history of the flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.describe_flow_execution_records)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#describe_flow_execution_records)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#generate_presigned_url)
        """

    def list_connector_entities(
        self, **kwargs: Unpack[ListConnectorEntitiesRequestRequestTypeDef]
    ) -> ListConnectorEntitiesResponseTypeDef:
        """
        Returns the list of available connector entities supported by Amazon AppFlow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.list_connector_entities)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#list_connector_entities)
        """

    def list_connectors(
        self, **kwargs: Unpack[ListConnectorsRequestRequestTypeDef]
    ) -> ListConnectorsResponseTypeDef:
        """
        Returns the list of all registered custom connectors in your Amazon Web
        Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.list_connectors)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#list_connectors)
        """

    def list_flows(
        self, **kwargs: Unpack[ListFlowsRequestRequestTypeDef]
    ) -> ListFlowsResponseTypeDef:
        """
        Lists all of the flows associated with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.list_flows)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#list_flows)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves the tags that are associated with a specified flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.list_tags_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#list_tags_for_resource)
        """

    def register_connector(
        self, **kwargs: Unpack[RegisterConnectorRequestRequestTypeDef]
    ) -> RegisterConnectorResponseTypeDef:
        """
        Registers a new custom connector with your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.register_connector)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#register_connector)
        """

    def reset_connector_metadata_cache(
        self, **kwargs: Unpack[ResetConnectorMetadataCacheRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Resets metadata about your connector entities that Amazon AppFlow stored in its
        cache.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.reset_connector_metadata_cache)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#reset_connector_metadata_cache)
        """

    def start_flow(
        self, **kwargs: Unpack[StartFlowRequestRequestTypeDef]
    ) -> StartFlowResponseTypeDef:
        """
        Activates an existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.start_flow)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#start_flow)
        """

    def stop_flow(self, **kwargs: Unpack[StopFlowRequestRequestTypeDef]) -> StopFlowResponseTypeDef:
        """
        Deactivates the existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.stop_flow)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#stop_flow)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Applies a tag to the specified flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#tag_resource)
        """

    def unregister_connector(
        self, **kwargs: Unpack[UnregisterConnectorRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Unregisters the custom connector registered in your account that matches the
        connector label provided in the
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.unregister_connector)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#unregister_connector)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes a tag from the specified flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#untag_resource)
        """

    def update_connector_profile(
        self, **kwargs: Unpack[UpdateConnectorProfileRequestRequestTypeDef]
    ) -> UpdateConnectorProfileResponseTypeDef:
        """
        Updates a given connector profile associated with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.update_connector_profile)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#update_connector_profile)
        """

    def update_connector_registration(
        self, **kwargs: Unpack[UpdateConnectorRegistrationRequestRequestTypeDef]
    ) -> UpdateConnectorRegistrationResponseTypeDef:
        """
        Updates a custom connector that you've previously registered.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.update_connector_registration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#update_connector_registration)
        """

    def update_flow(
        self, **kwargs: Unpack[UpdateFlowRequestRequestTypeDef]
    ) -> UpdateFlowResponseTypeDef:
        """
        Updates an existing flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow.Client.update_flow)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appflow/client/#update_flow)
        """
