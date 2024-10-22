"""
Type annotations for controltower service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_controltower.client import ControlTowerClient

    session = Session()
    client: ControlTowerClient = session.client("controltower")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    ListBaselinesPaginator,
    ListControlOperationsPaginator,
    ListEnabledBaselinesPaginator,
    ListEnabledControlsPaginator,
    ListLandingZoneOperationsPaginator,
    ListLandingZonesPaginator,
)
from .type_defs import (
    CreateLandingZoneInputRequestTypeDef,
    CreateLandingZoneOutputTypeDef,
    DeleteLandingZoneInputRequestTypeDef,
    DeleteLandingZoneOutputTypeDef,
    DisableBaselineInputRequestTypeDef,
    DisableBaselineOutputTypeDef,
    DisableControlInputRequestTypeDef,
    DisableControlOutputTypeDef,
    EnableBaselineInputRequestTypeDef,
    EnableBaselineOutputTypeDef,
    EnableControlInputRequestTypeDef,
    EnableControlOutputTypeDef,
    GetBaselineInputRequestTypeDef,
    GetBaselineOperationInputRequestTypeDef,
    GetBaselineOperationOutputTypeDef,
    GetBaselineOutputTypeDef,
    GetControlOperationInputRequestTypeDef,
    GetControlOperationOutputTypeDef,
    GetEnabledBaselineInputRequestTypeDef,
    GetEnabledBaselineOutputTypeDef,
    GetEnabledControlInputRequestTypeDef,
    GetEnabledControlOutputTypeDef,
    GetLandingZoneInputRequestTypeDef,
    GetLandingZoneOperationInputRequestTypeDef,
    GetLandingZoneOperationOutputTypeDef,
    GetLandingZoneOutputTypeDef,
    ListBaselinesInputRequestTypeDef,
    ListBaselinesOutputTypeDef,
    ListControlOperationsInputRequestTypeDef,
    ListControlOperationsOutputTypeDef,
    ListEnabledBaselinesInputRequestTypeDef,
    ListEnabledBaselinesOutputTypeDef,
    ListEnabledControlsInputRequestTypeDef,
    ListEnabledControlsOutputTypeDef,
    ListLandingZoneOperationsInputRequestTypeDef,
    ListLandingZoneOperationsOutputTypeDef,
    ListLandingZonesInputRequestTypeDef,
    ListLandingZonesOutputTypeDef,
    ListTagsForResourceInputRequestTypeDef,
    ListTagsForResourceOutputTypeDef,
    ResetEnabledBaselineInputRequestTypeDef,
    ResetEnabledBaselineOutputTypeDef,
    ResetLandingZoneInputRequestTypeDef,
    ResetLandingZoneOutputTypeDef,
    TagResourceInputRequestTypeDef,
    UntagResourceInputRequestTypeDef,
    UpdateEnabledBaselineInputRequestTypeDef,
    UpdateEnabledBaselineOutputTypeDef,
    UpdateEnabledControlInputRequestTypeDef,
    UpdateEnabledControlOutputTypeDef,
    UpdateLandingZoneInputRequestTypeDef,
    UpdateLandingZoneOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("ControlTowerClient",)

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

class ControlTowerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ControlTowerClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#close)
        """

    def create_landing_zone(
        self, **kwargs: Unpack[CreateLandingZoneInputRequestTypeDef]
    ) -> CreateLandingZoneOutputTypeDef:
        """
        Creates a new landing zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.create_landing_zone)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#create_landing_zone)
        """

    def delete_landing_zone(
        self, **kwargs: Unpack[DeleteLandingZoneInputRequestTypeDef]
    ) -> DeleteLandingZoneOutputTypeDef:
        """
        Decommissions a landing zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.delete_landing_zone)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#delete_landing_zone)
        """

    def disable_baseline(
        self, **kwargs: Unpack[DisableBaselineInputRequestTypeDef]
    ) -> DisableBaselineOutputTypeDef:
        """
        Disable an `EnabledBaseline` resource on the specified Target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.disable_baseline)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#disable_baseline)
        """

    def disable_control(
        self, **kwargs: Unpack[DisableControlInputRequestTypeDef]
    ) -> DisableControlOutputTypeDef:
        """
        This API call turns off a control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.disable_control)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#disable_control)
        """

    def enable_baseline(
        self, **kwargs: Unpack[EnableBaselineInputRequestTypeDef]
    ) -> EnableBaselineOutputTypeDef:
        """
        Enable (apply) a `Baseline` to a Target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.enable_baseline)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#enable_baseline)
        """

    def enable_control(
        self, **kwargs: Unpack[EnableControlInputRequestTypeDef]
    ) -> EnableControlOutputTypeDef:
        """
        This API call activates a control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.enable_control)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#enable_control)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#generate_presigned_url)
        """

    def get_baseline(
        self, **kwargs: Unpack[GetBaselineInputRequestTypeDef]
    ) -> GetBaselineOutputTypeDef:
        """
        Retrieve details about an existing `Baseline` resource by specifying its
        identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.get_baseline)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#get_baseline)
        """

    def get_baseline_operation(
        self, **kwargs: Unpack[GetBaselineOperationInputRequestTypeDef]
    ) -> GetBaselineOperationOutputTypeDef:
        """
        Returns the details of an asynchronous baseline operation, as initiated by any
        of these APIs: `EnableBaseline`, `DisableBaseline`, `UpdateEnabledBaseline`,
        `ResetEnabledBaseline`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.get_baseline_operation)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#get_baseline_operation)
        """

    def get_control_operation(
        self, **kwargs: Unpack[GetControlOperationInputRequestTypeDef]
    ) -> GetControlOperationOutputTypeDef:
        """
        Returns the status of a particular `EnableControl` or `DisableControl`
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.get_control_operation)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#get_control_operation)
        """

    def get_enabled_baseline(
        self, **kwargs: Unpack[GetEnabledBaselineInputRequestTypeDef]
    ) -> GetEnabledBaselineOutputTypeDef:
        """
        Retrieve details of an `EnabledBaseline` resource by specifying its identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.get_enabled_baseline)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#get_enabled_baseline)
        """

    def get_enabled_control(
        self, **kwargs: Unpack[GetEnabledControlInputRequestTypeDef]
    ) -> GetEnabledControlOutputTypeDef:
        """
        Retrieves details about an enabled control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.get_enabled_control)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#get_enabled_control)
        """

    def get_landing_zone(
        self, **kwargs: Unpack[GetLandingZoneInputRequestTypeDef]
    ) -> GetLandingZoneOutputTypeDef:
        """
        Returns details about the landing zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.get_landing_zone)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#get_landing_zone)
        """

    def get_landing_zone_operation(
        self, **kwargs: Unpack[GetLandingZoneOperationInputRequestTypeDef]
    ) -> GetLandingZoneOperationOutputTypeDef:
        """
        Returns the status of the specified landing zone operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.get_landing_zone_operation)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#get_landing_zone_operation)
        """

    def list_baselines(
        self, **kwargs: Unpack[ListBaselinesInputRequestTypeDef]
    ) -> ListBaselinesOutputTypeDef:
        """
        Returns a summary list of all available baselines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.list_baselines)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#list_baselines)
        """

    def list_control_operations(
        self, **kwargs: Unpack[ListControlOperationsInputRequestTypeDef]
    ) -> ListControlOperationsOutputTypeDef:
        """
        Provides a list of operations in progress or queued.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.list_control_operations)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#list_control_operations)
        """

    def list_enabled_baselines(
        self, **kwargs: Unpack[ListEnabledBaselinesInputRequestTypeDef]
    ) -> ListEnabledBaselinesOutputTypeDef:
        """
        Returns a list of summaries describing `EnabledBaseline` resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.list_enabled_baselines)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#list_enabled_baselines)
        """

    def list_enabled_controls(
        self, **kwargs: Unpack[ListEnabledControlsInputRequestTypeDef]
    ) -> ListEnabledControlsOutputTypeDef:
        """
        Lists the controls enabled by Amazon Web Services Control Tower on the
        specified organizational unit and the accounts it
        contains.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.list_enabled_controls)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#list_enabled_controls)
        """

    def list_landing_zone_operations(
        self, **kwargs: Unpack[ListLandingZoneOperationsInputRequestTypeDef]
    ) -> ListLandingZoneOperationsOutputTypeDef:
        """
        Lists all landing zone operations from the past 90 days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.list_landing_zone_operations)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#list_landing_zone_operations)
        """

    def list_landing_zones(
        self, **kwargs: Unpack[ListLandingZonesInputRequestTypeDef]
    ) -> ListLandingZonesOutputTypeDef:
        """
        Returns the landing zone ARN for the landing zone deployed in your managed
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.list_landing_zones)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#list_landing_zones)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputRequestTypeDef]
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Returns a list of tags associated with the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.list_tags_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#list_tags_for_resource)
        """

    def reset_enabled_baseline(
        self, **kwargs: Unpack[ResetEnabledBaselineInputRequestTypeDef]
    ) -> ResetEnabledBaselineOutputTypeDef:
        """
        Re-enables an `EnabledBaseline` resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.reset_enabled_baseline)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#reset_enabled_baseline)
        """

    def reset_landing_zone(
        self, **kwargs: Unpack[ResetLandingZoneInputRequestTypeDef]
    ) -> ResetLandingZoneOutputTypeDef:
        """
        This API call resets a landing zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.reset_landing_zone)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#reset_landing_zone)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceInputRequestTypeDef]) -> Dict[str, Any]:
        """
        Applies tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceInputRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#untag_resource)
        """

    def update_enabled_baseline(
        self, **kwargs: Unpack[UpdateEnabledBaselineInputRequestTypeDef]
    ) -> UpdateEnabledBaselineOutputTypeDef:
        """
        Updates an `EnabledBaseline` resource's applied parameters or version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.update_enabled_baseline)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#update_enabled_baseline)
        """

    def update_enabled_control(
        self, **kwargs: Unpack[UpdateEnabledControlInputRequestTypeDef]
    ) -> UpdateEnabledControlOutputTypeDef:
        """
        Updates the configuration of an already enabled control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.update_enabled_control)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#update_enabled_control)
        """

    def update_landing_zone(
        self, **kwargs: Unpack[UpdateLandingZoneInputRequestTypeDef]
    ) -> UpdateLandingZoneOutputTypeDef:
        """
        This API call updates the landing zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.update_landing_zone)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#update_landing_zone)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_baselines"]) -> ListBaselinesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_control_operations"]
    ) -> ListControlOperationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_enabled_baselines"]
    ) -> ListEnabledBaselinesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_enabled_controls"]
    ) -> ListEnabledControlsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_landing_zone_operations"]
    ) -> ListLandingZoneOperationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_landing_zones"]
    ) -> ListLandingZonesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#get_paginator)
        """
