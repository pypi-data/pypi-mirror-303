"""
Type annotations for iotsecuretunneling service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/type_defs/)

Usage::

    ```python
    from mypy_boto3_iotsecuretunneling.type_defs import CloseTunnelRequestRequestTypeDef

    data: CloseTunnelRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import ClientModeType, ConnectionStatusType, TunnelStatusType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "CloseTunnelRequestRequestTypeDef",
    "ConnectionStateTypeDef",
    "DescribeTunnelRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "DestinationConfigOutputTypeDef",
    "DestinationConfigTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagTypeDef",
    "ListTunnelsRequestRequestTypeDef",
    "TunnelSummaryTypeDef",
    "TimeoutConfigTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "OpenTunnelResponseTypeDef",
    "RotateTunnelAccessTokenResponseTypeDef",
    "RotateTunnelAccessTokenRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "ListTunnelsResponseTypeDef",
    "OpenTunnelRequestRequestTypeDef",
    "TunnelTypeDef",
    "DescribeTunnelResponseTypeDef",
)

CloseTunnelRequestRequestTypeDef = TypedDict(
    "CloseTunnelRequestRequestTypeDef",
    {
        "tunnelId": str,
        "delete": NotRequired[bool],
    },
)
ConnectionStateTypeDef = TypedDict(
    "ConnectionStateTypeDef",
    {
        "status": NotRequired[ConnectionStatusType],
        "lastUpdatedAt": NotRequired[datetime],
    },
)
DescribeTunnelRequestRequestTypeDef = TypedDict(
    "DescribeTunnelRequestRequestTypeDef",
    {
        "tunnelId": str,
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
DestinationConfigOutputTypeDef = TypedDict(
    "DestinationConfigOutputTypeDef",
    {
        "services": List[str],
        "thingName": NotRequired[str],
    },
)
DestinationConfigTypeDef = TypedDict(
    "DestinationConfigTypeDef",
    {
        "services": Sequence[str],
        "thingName": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)
ListTunnelsRequestRequestTypeDef = TypedDict(
    "ListTunnelsRequestRequestTypeDef",
    {
        "thingName": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
TunnelSummaryTypeDef = TypedDict(
    "TunnelSummaryTypeDef",
    {
        "tunnelId": NotRequired[str],
        "tunnelArn": NotRequired[str],
        "status": NotRequired[TunnelStatusType],
        "description": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
    },
)
TimeoutConfigTypeDef = TypedDict(
    "TimeoutConfigTypeDef",
    {
        "maxLifetimeTimeoutMinutes": NotRequired[int],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
OpenTunnelResponseTypeDef = TypedDict(
    "OpenTunnelResponseTypeDef",
    {
        "tunnelId": str,
        "tunnelArn": str,
        "sourceAccessToken": str,
        "destinationAccessToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RotateTunnelAccessTokenResponseTypeDef = TypedDict(
    "RotateTunnelAccessTokenResponseTypeDef",
    {
        "tunnelArn": str,
        "sourceAccessToken": str,
        "destinationAccessToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RotateTunnelAccessTokenRequestRequestTypeDef = TypedDict(
    "RotateTunnelAccessTokenRequestRequestTypeDef",
    {
        "tunnelId": str,
        "clientMode": ClientModeType,
        "destinationConfig": NotRequired[DestinationConfigTypeDef],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[TagTypeDef],
    },
)
ListTunnelsResponseTypeDef = TypedDict(
    "ListTunnelsResponseTypeDef",
    {
        "tunnelSummaries": List[TunnelSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OpenTunnelRequestRequestTypeDef = TypedDict(
    "OpenTunnelRequestRequestTypeDef",
    {
        "description": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "destinationConfig": NotRequired[DestinationConfigTypeDef],
        "timeoutConfig": NotRequired[TimeoutConfigTypeDef],
    },
)
TunnelTypeDef = TypedDict(
    "TunnelTypeDef",
    {
        "tunnelId": NotRequired[str],
        "tunnelArn": NotRequired[str],
        "status": NotRequired[TunnelStatusType],
        "sourceConnectionState": NotRequired[ConnectionStateTypeDef],
        "destinationConnectionState": NotRequired[ConnectionStateTypeDef],
        "description": NotRequired[str],
        "destinationConfig": NotRequired[DestinationConfigOutputTypeDef],
        "timeoutConfig": NotRequired[TimeoutConfigTypeDef],
        "tags": NotRequired[List[TagTypeDef]],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
    },
)
DescribeTunnelResponseTypeDef = TypedDict(
    "DescribeTunnelResponseTypeDef",
    {
        "tunnel": TunnelTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
