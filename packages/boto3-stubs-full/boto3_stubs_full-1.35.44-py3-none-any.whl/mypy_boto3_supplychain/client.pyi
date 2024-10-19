"""
Type annotations for supplychain service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_supplychain.client import SupplyChainClient

    session = Session()
    client: SupplyChainClient = session.client("supplychain")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    ListDataIntegrationFlowsPaginator,
    ListDataLakeDatasetsPaginator,
    ListInstancesPaginator,
)
from .type_defs import (
    CreateBillOfMaterialsImportJobRequestRequestTypeDef,
    CreateBillOfMaterialsImportJobResponseTypeDef,
    CreateDataIntegrationFlowRequestRequestTypeDef,
    CreateDataIntegrationFlowResponseTypeDef,
    CreateDataLakeDatasetRequestRequestTypeDef,
    CreateDataLakeDatasetResponseTypeDef,
    CreateInstanceRequestRequestTypeDef,
    CreateInstanceResponseTypeDef,
    DeleteDataIntegrationFlowRequestRequestTypeDef,
    DeleteDataIntegrationFlowResponseTypeDef,
    DeleteDataLakeDatasetRequestRequestTypeDef,
    DeleteDataLakeDatasetResponseTypeDef,
    DeleteInstanceRequestRequestTypeDef,
    DeleteInstanceResponseTypeDef,
    GetBillOfMaterialsImportJobRequestRequestTypeDef,
    GetBillOfMaterialsImportJobResponseTypeDef,
    GetDataIntegrationFlowRequestRequestTypeDef,
    GetDataIntegrationFlowResponseTypeDef,
    GetDataLakeDatasetRequestRequestTypeDef,
    GetDataLakeDatasetResponseTypeDef,
    GetInstanceRequestRequestTypeDef,
    GetInstanceResponseTypeDef,
    ListDataIntegrationFlowsRequestRequestTypeDef,
    ListDataIntegrationFlowsResponseTypeDef,
    ListDataLakeDatasetsRequestRequestTypeDef,
    ListDataLakeDatasetsResponseTypeDef,
    ListInstancesRequestRequestTypeDef,
    ListInstancesResponseTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    SendDataIntegrationEventRequestRequestTypeDef,
    SendDataIntegrationEventResponseTypeDef,
    TagResourceRequestRequestTypeDef,
    UntagResourceRequestRequestTypeDef,
    UpdateDataIntegrationFlowRequestRequestTypeDef,
    UpdateDataIntegrationFlowResponseTypeDef,
    UpdateDataLakeDatasetRequestRequestTypeDef,
    UpdateDataLakeDatasetResponseTypeDef,
    UpdateInstanceRequestRequestTypeDef,
    UpdateInstanceResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("SupplyChainClient",)

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

class SupplyChainClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/supplychain.html#SupplyChain.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SupplyChainClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/supplychain.html#SupplyChain.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/supplychain.html#SupplyChain.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/supplychain.html#SupplyChain.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client/#close)
        """

    def create_bill_of_materials_import_job(
        self, **kwargs: Unpack[CreateBillOfMaterialsImportJobRequestRequestTypeDef]
    ) -> CreateBillOfMaterialsImportJobResponseTypeDef:
        """
        CreateBillOfMaterialsImportJob creates an import job for the Product Bill Of
        Materials (BOM)
        entity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/supplychain.html#SupplyChain.Client.create_bill_of_materials_import_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client/#create_bill_of_materials_import_job)
        """

    def create_data_integration_flow(
        self, **kwargs: Unpack[CreateDataIntegrationFlowRequestRequestTypeDef]
    ) -> CreateDataIntegrationFlowResponseTypeDef:
        """
        Create DataIntegrationFlow to map one or more different sources to one target
        using the SQL transformation
        query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/supplychain.html#SupplyChain.Client.create_data_integration_flow)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client/#create_data_integration_flow)
        """

    def create_data_lake_dataset(
        self, **kwargs: Unpack[CreateDataLakeDatasetRequestRequestTypeDef]
    ) -> CreateDataLakeDatasetResponseTypeDef:
        """
        Create a data lake dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/supplychain.html#SupplyChain.Client.create_data_lake_dataset)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client/#create_data_lake_dataset)
        """

    def create_instance(
        self, **kwargs: Unpack[CreateInstanceRequestRequestTypeDef]
    ) -> CreateInstanceResponseTypeDef:
        """
        Create a new instance for AWS Supply Chain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/supplychain.html#SupplyChain.Client.create_instance)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client/#create_instance)
        """

    def delete_data_integration_flow(
        self, **kwargs: Unpack[DeleteDataIntegrationFlowRequestRequestTypeDef]
    ) -> DeleteDataIntegrationFlowResponseTypeDef:
        """
        Delete the DataIntegrationFlow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/supplychain.html#SupplyChain.Client.delete_data_integration_flow)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client/#delete_data_integration_flow)
        """

    def delete_data_lake_dataset(
        self, **kwargs: Unpack[DeleteDataLakeDatasetRequestRequestTypeDef]
    ) -> DeleteDataLakeDatasetResponseTypeDef:
        """
        Delete a data lake dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/supplychain.html#SupplyChain.Client.delete_data_lake_dataset)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client/#delete_data_lake_dataset)
        """

    def delete_instance(
        self, **kwargs: Unpack[DeleteInstanceRequestRequestTypeDef]
    ) -> DeleteInstanceResponseTypeDef:
        """
        Delete the instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/supplychain.html#SupplyChain.Client.delete_instance)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client/#delete_instance)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/supplychain.html#SupplyChain.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client/#generate_presigned_url)
        """

    def get_bill_of_materials_import_job(
        self, **kwargs: Unpack[GetBillOfMaterialsImportJobRequestRequestTypeDef]
    ) -> GetBillOfMaterialsImportJobResponseTypeDef:
        """
        Get status and details of a BillOfMaterialsImportJob.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/supplychain.html#SupplyChain.Client.get_bill_of_materials_import_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client/#get_bill_of_materials_import_job)
        """

    def get_data_integration_flow(
        self, **kwargs: Unpack[GetDataIntegrationFlowRequestRequestTypeDef]
    ) -> GetDataIntegrationFlowResponseTypeDef:
        """
        View the DataIntegrationFlow details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/supplychain.html#SupplyChain.Client.get_data_integration_flow)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client/#get_data_integration_flow)
        """

    def get_data_lake_dataset(
        self, **kwargs: Unpack[GetDataLakeDatasetRequestRequestTypeDef]
    ) -> GetDataLakeDatasetResponseTypeDef:
        """
        Get a data lake dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/supplychain.html#SupplyChain.Client.get_data_lake_dataset)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client/#get_data_lake_dataset)
        """

    def get_instance(
        self, **kwargs: Unpack[GetInstanceRequestRequestTypeDef]
    ) -> GetInstanceResponseTypeDef:
        """
        Get the AWS Supply Chain instance details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/supplychain.html#SupplyChain.Client.get_instance)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client/#get_instance)
        """

    def list_data_integration_flows(
        self, **kwargs: Unpack[ListDataIntegrationFlowsRequestRequestTypeDef]
    ) -> ListDataIntegrationFlowsResponseTypeDef:
        """
        Lists all the DataIntegrationFlows in a paginated way.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/supplychain.html#SupplyChain.Client.list_data_integration_flows)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client/#list_data_integration_flows)
        """

    def list_data_lake_datasets(
        self, **kwargs: Unpack[ListDataLakeDatasetsRequestRequestTypeDef]
    ) -> ListDataLakeDatasetsResponseTypeDef:
        """
        List the data lake datasets for a specific instance and name space.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/supplychain.html#SupplyChain.Client.list_data_lake_datasets)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client/#list_data_lake_datasets)
        """

    def list_instances(
        self, **kwargs: Unpack[ListInstancesRequestRequestTypeDef]
    ) -> ListInstancesResponseTypeDef:
        """
        List all the AWS Supply Chain instances in a paginated way.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/supplychain.html#SupplyChain.Client.list_instances)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client/#list_instances)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        List all the tags for an Amazon Web ServicesSupply Chain resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/supplychain.html#SupplyChain.Client.list_tags_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client/#list_tags_for_resource)
        """

    def send_data_integration_event(
        self, **kwargs: Unpack[SendDataIntegrationEventRequestRequestTypeDef]
    ) -> SendDataIntegrationEventResponseTypeDef:
        """
        Send the transactional data payload for the event with real-time data for
        analysis or
        monitoring.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/supplychain.html#SupplyChain.Client.send_data_integration_event)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client/#send_data_integration_event)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Create tags for an Amazon Web Services Supply chain resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/supplychain.html#SupplyChain.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Delete tags for an Amazon Web Services Supply chain resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/supplychain.html#SupplyChain.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client/#untag_resource)
        """

    def update_data_integration_flow(
        self, **kwargs: Unpack[UpdateDataIntegrationFlowRequestRequestTypeDef]
    ) -> UpdateDataIntegrationFlowResponseTypeDef:
        """
        Update the DataIntegrationFlow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/supplychain.html#SupplyChain.Client.update_data_integration_flow)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client/#update_data_integration_flow)
        """

    def update_data_lake_dataset(
        self, **kwargs: Unpack[UpdateDataLakeDatasetRequestRequestTypeDef]
    ) -> UpdateDataLakeDatasetResponseTypeDef:
        """
        Update a data lake dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/supplychain.html#SupplyChain.Client.update_data_lake_dataset)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client/#update_data_lake_dataset)
        """

    def update_instance(
        self, **kwargs: Unpack[UpdateInstanceRequestRequestTypeDef]
    ) -> UpdateInstanceResponseTypeDef:
        """
        Update the instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/supplychain.html#SupplyChain.Client.update_instance)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client/#update_instance)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_integration_flows"]
    ) -> ListDataIntegrationFlowsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/supplychain.html#SupplyChain.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_lake_datasets"]
    ) -> ListDataLakeDatasetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/supplychain.html#SupplyChain.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_instances"]) -> ListInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/supplychain.html#SupplyChain.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_supplychain/client/#get_paginator)
        """
