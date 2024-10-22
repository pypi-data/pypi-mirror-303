"""
Type annotations for networkmonitor service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_networkmonitor.client import CloudWatchNetworkMonitorClient

    session = Session()
    client: CloudWatchNetworkMonitorClient = session.client("networkmonitor")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type

from botocore.client import BaseClient, ClientMeta

from .paginator import ListMonitorsPaginator
from .type_defs import (
    CreateMonitorInputRequestTypeDef,
    CreateMonitorOutputTypeDef,
    CreateProbeInputRequestTypeDef,
    CreateProbeOutputTypeDef,
    DeleteMonitorInputRequestTypeDef,
    DeleteProbeInputRequestTypeDef,
    GetMonitorInputRequestTypeDef,
    GetMonitorOutputTypeDef,
    GetProbeInputRequestTypeDef,
    GetProbeOutputTypeDef,
    ListMonitorsInputRequestTypeDef,
    ListMonitorsOutputTypeDef,
    ListTagsForResourceInputRequestTypeDef,
    ListTagsForResourceOutputTypeDef,
    TagResourceInputRequestTypeDef,
    UntagResourceInputRequestTypeDef,
    UpdateMonitorInputRequestTypeDef,
    UpdateMonitorOutputTypeDef,
    UpdateProbeInputRequestTypeDef,
    UpdateProbeOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("CloudWatchNetworkMonitorClient",)

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

class CloudWatchNetworkMonitorClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CloudWatchNetworkMonitorClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/#close)
        """

    def create_monitor(
        self, **kwargs: Unpack[CreateMonitorInputRequestTypeDef]
    ) -> CreateMonitorOutputTypeDef:
        """
        Creates a monitor between a source subnet and destination IP address.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client.create_monitor)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/#create_monitor)
        """

    def create_probe(
        self, **kwargs: Unpack[CreateProbeInputRequestTypeDef]
    ) -> CreateProbeOutputTypeDef:
        """
        Create a probe within a monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client.create_probe)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/#create_probe)
        """

    def delete_monitor(self, **kwargs: Unpack[DeleteMonitorInputRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a specified monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client.delete_monitor)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/#delete_monitor)
        """

    def delete_probe(self, **kwargs: Unpack[DeleteProbeInputRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified probe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client.delete_probe)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/#delete_probe)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/#generate_presigned_url)
        """

    def get_monitor(
        self, **kwargs: Unpack[GetMonitorInputRequestTypeDef]
    ) -> GetMonitorOutputTypeDef:
        """
        Returns details about a specific monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client.get_monitor)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/#get_monitor)
        """

    def get_probe(self, **kwargs: Unpack[GetProbeInputRequestTypeDef]) -> GetProbeOutputTypeDef:
        """
        Returns the details about a probe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client.get_probe)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/#get_probe)
        """

    def list_monitors(
        self, **kwargs: Unpack[ListMonitorsInputRequestTypeDef]
    ) -> ListMonitorsOutputTypeDef:
        """
        Returns a list of all of your monitors.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client.list_monitors)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/#list_monitors)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputRequestTypeDef]
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Lists the tags assigned to this resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client.list_tags_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/#list_tags_for_resource)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceInputRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds key-value pairs to a monitor or probe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceInputRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes a key-value pair from a monitor or probe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/#untag_resource)
        """

    def update_monitor(
        self, **kwargs: Unpack[UpdateMonitorInputRequestTypeDef]
    ) -> UpdateMonitorOutputTypeDef:
        """
        Updates the `aggregationPeriod` for a monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client.update_monitor)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/#update_monitor)
        """

    def update_probe(
        self, **kwargs: Unpack[UpdateProbeInputRequestTypeDef]
    ) -> UpdateProbeOutputTypeDef:
        """
        Updates a monitor probe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client.update_probe)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/#update_probe)
        """

    def get_paginator(self, operation_name: Literal["list_monitors"]) -> ListMonitorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/client/#get_paginator)
        """
