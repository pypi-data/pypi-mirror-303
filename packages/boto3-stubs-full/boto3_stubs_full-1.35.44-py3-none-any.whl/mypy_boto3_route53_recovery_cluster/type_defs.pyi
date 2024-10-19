"""
Type annotations for route53-recovery-cluster service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/type_defs/)

Usage::

    ```python
    from mypy_boto3_route53_recovery_cluster.type_defs import GetRoutingControlStateRequestRequestTypeDef

    data: GetRoutingControlStateRequestRequestTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Sequence

from .literals import RoutingControlStateType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "GetRoutingControlStateRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "PaginatorConfigTypeDef",
    "ListRoutingControlsRequestRequestTypeDef",
    "RoutingControlTypeDef",
    "UpdateRoutingControlStateEntryTypeDef",
    "UpdateRoutingControlStateRequestRequestTypeDef",
    "GetRoutingControlStateResponseTypeDef",
    "ListRoutingControlsRequestListRoutingControlsPaginateTypeDef",
    "ListRoutingControlsResponseTypeDef",
    "UpdateRoutingControlStatesRequestRequestTypeDef",
)

GetRoutingControlStateRequestRequestTypeDef = TypedDict(
    "GetRoutingControlStateRequestRequestTypeDef",
    {
        "RoutingControlArn": str,
    },
)
ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
        "HostId": NotRequired[str],
    },
)
PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
    },
)
ListRoutingControlsRequestRequestTypeDef = TypedDict(
    "ListRoutingControlsRequestRequestTypeDef",
    {
        "ControlPanelArn": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
RoutingControlTypeDef = TypedDict(
    "RoutingControlTypeDef",
    {
        "ControlPanelArn": NotRequired[str],
        "ControlPanelName": NotRequired[str],
        "RoutingControlArn": NotRequired[str],
        "RoutingControlName": NotRequired[str],
        "RoutingControlState": NotRequired[RoutingControlStateType],
        "Owner": NotRequired[str],
    },
)
UpdateRoutingControlStateEntryTypeDef = TypedDict(
    "UpdateRoutingControlStateEntryTypeDef",
    {
        "RoutingControlArn": str,
        "RoutingControlState": RoutingControlStateType,
    },
)
UpdateRoutingControlStateRequestRequestTypeDef = TypedDict(
    "UpdateRoutingControlStateRequestRequestTypeDef",
    {
        "RoutingControlArn": str,
        "RoutingControlState": RoutingControlStateType,
        "SafetyRulesToOverride": NotRequired[Sequence[str]],
    },
)
GetRoutingControlStateResponseTypeDef = TypedDict(
    "GetRoutingControlStateResponseTypeDef",
    {
        "RoutingControlArn": str,
        "RoutingControlState": RoutingControlStateType,
        "RoutingControlName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRoutingControlsRequestListRoutingControlsPaginateTypeDef = TypedDict(
    "ListRoutingControlsRequestListRoutingControlsPaginateTypeDef",
    {
        "ControlPanelArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRoutingControlsResponseTypeDef = TypedDict(
    "ListRoutingControlsResponseTypeDef",
    {
        "RoutingControls": List[RoutingControlTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateRoutingControlStatesRequestRequestTypeDef = TypedDict(
    "UpdateRoutingControlStatesRequestRequestTypeDef",
    {
        "UpdateRoutingControlStateEntries": Sequence[UpdateRoutingControlStateEntryTypeDef],
        "SafetyRulesToOverride": NotRequired[Sequence[str]],
    },
)
