"""
Type annotations for braket service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_braket.client import BraketClient

    session = Session()
    client: BraketClient = session.client("braket")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import SearchDevicesPaginator, SearchJobsPaginator, SearchQuantumTasksPaginator
from .type_defs import (
    CancelJobRequestRequestTypeDef,
    CancelJobResponseTypeDef,
    CancelQuantumTaskRequestRequestTypeDef,
    CancelQuantumTaskResponseTypeDef,
    CreateJobRequestRequestTypeDef,
    CreateJobResponseTypeDef,
    CreateQuantumTaskRequestRequestTypeDef,
    CreateQuantumTaskResponseTypeDef,
    GetDeviceRequestRequestTypeDef,
    GetDeviceResponseTypeDef,
    GetJobRequestRequestTypeDef,
    GetJobResponseTypeDef,
    GetQuantumTaskRequestRequestTypeDef,
    GetQuantumTaskResponseTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    SearchDevicesRequestRequestTypeDef,
    SearchDevicesResponseTypeDef,
    SearchJobsRequestRequestTypeDef,
    SearchJobsResponseTypeDef,
    SearchQuantumTasksRequestRequestTypeDef,
    SearchQuantumTasksResponseTypeDef,
    TagResourceRequestRequestTypeDef,
    UntagResourceRequestRequestTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("BraketClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    DeviceOfflineException: Type[BotocoreClientError]
    DeviceRetiredException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class BraketClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        BraketClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#can_paginate)
        """

    def cancel_job(
        self, **kwargs: Unpack[CancelJobRequestRequestTypeDef]
    ) -> CancelJobResponseTypeDef:
        """
        Cancels an Amazon Braket job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client.cancel_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#cancel_job)
        """

    def cancel_quantum_task(
        self, **kwargs: Unpack[CancelQuantumTaskRequestRequestTypeDef]
    ) -> CancelQuantumTaskResponseTypeDef:
        """
        Cancels the specified task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client.cancel_quantum_task)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#cancel_quantum_task)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#close)
        """

    def create_job(
        self, **kwargs: Unpack[CreateJobRequestRequestTypeDef]
    ) -> CreateJobResponseTypeDef:
        """
        Creates an Amazon Braket job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client.create_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#create_job)
        """

    def create_quantum_task(
        self, **kwargs: Unpack[CreateQuantumTaskRequestRequestTypeDef]
    ) -> CreateQuantumTaskResponseTypeDef:
        """
        Creates a quantum task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client.create_quantum_task)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#create_quantum_task)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#generate_presigned_url)
        """

    def get_device(
        self, **kwargs: Unpack[GetDeviceRequestRequestTypeDef]
    ) -> GetDeviceResponseTypeDef:
        """
        Retrieves the devices available in Amazon Braket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client.get_device)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#get_device)
        """

    def get_job(self, **kwargs: Unpack[GetJobRequestRequestTypeDef]) -> GetJobResponseTypeDef:
        """
        Retrieves the specified Amazon Braket job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client.get_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#get_job)
        """

    def get_quantum_task(
        self, **kwargs: Unpack[GetQuantumTaskRequestRequestTypeDef]
    ) -> GetQuantumTaskResponseTypeDef:
        """
        Retrieves the specified quantum task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client.get_quantum_task)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#get_quantum_task)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Shows the tags associated with this resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client.list_tags_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#list_tags_for_resource)
        """

    def search_devices(
        self, **kwargs: Unpack[SearchDevicesRequestRequestTypeDef]
    ) -> SearchDevicesResponseTypeDef:
        """
        Searches for devices using the specified filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client.search_devices)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#search_devices)
        """

    def search_jobs(
        self, **kwargs: Unpack[SearchJobsRequestRequestTypeDef]
    ) -> SearchJobsResponseTypeDef:
        """
        Searches for Amazon Braket jobs that match the specified filter values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client.search_jobs)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#search_jobs)
        """

    def search_quantum_tasks(
        self, **kwargs: Unpack[SearchQuantumTasksRequestRequestTypeDef]
    ) -> SearchQuantumTasksResponseTypeDef:
        """
        Searches for tasks that match the specified filter values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client.search_quantum_tasks)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#search_quantum_tasks)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Add a tag to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Remove tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#untag_resource)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_devices"]) -> SearchDevicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_jobs"]) -> SearchJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_quantum_tasks"]
    ) -> SearchQuantumTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html#Braket.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_braket/client/#get_paginator)
        """
