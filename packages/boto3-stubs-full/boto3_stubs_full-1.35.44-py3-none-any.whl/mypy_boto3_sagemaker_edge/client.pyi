"""
Type annotations for sagemaker-edge service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_edge/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_sagemaker_edge.client import SagemakerEdgeManagerClient

    session = Session()
    client: SagemakerEdgeManagerClient = session.client("sagemaker-edge")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
    EmptyResponseMetadataTypeDef,
    GetDeploymentsRequestRequestTypeDef,
    GetDeploymentsResultTypeDef,
    GetDeviceRegistrationRequestRequestTypeDef,
    GetDeviceRegistrationResultTypeDef,
    SendHeartbeatRequestRequestTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("SagemakerEdgeManagerClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]

class SagemakerEdgeManagerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-edge.html#SagemakerEdgeManager.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_edge/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SagemakerEdgeManagerClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-edge.html#SagemakerEdgeManager.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_edge/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-edge.html#SagemakerEdgeManager.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_edge/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-edge.html#SagemakerEdgeManager.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_edge/client/#close)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-edge.html#SagemakerEdgeManager.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_edge/client/#generate_presigned_url)
        """

    def get_deployments(
        self, **kwargs: Unpack[GetDeploymentsRequestRequestTypeDef]
    ) -> GetDeploymentsResultTypeDef:
        """
        Use to get the active deployments from a device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-edge.html#SagemakerEdgeManager.Client.get_deployments)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_edge/client/#get_deployments)
        """

    def get_device_registration(
        self, **kwargs: Unpack[GetDeviceRegistrationRequestRequestTypeDef]
    ) -> GetDeviceRegistrationResultTypeDef:
        """
        Use to check if a device is registered with SageMaker Edge Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-edge.html#SagemakerEdgeManager.Client.get_device_registration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_edge/client/#get_device_registration)
        """

    def send_heartbeat(
        self, **kwargs: Unpack[SendHeartbeatRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Use to get the current status of devices registered on SageMaker Edge Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-edge.html#SagemakerEdgeManager.Client.send_heartbeat)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_edge/client/#send_heartbeat)
        """
