"""
Type annotations for iot-data service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_data/type_defs/)

Usage::

    ```python
    from mypy_boto3_iot_data.type_defs import BlobTypeDef

    data: BlobTypeDef = ...
    ```
"""

import sys
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import PayloadFormatIndicatorType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "BlobTypeDef",
    "DeleteThingShadowRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "GetRetainedMessageRequestRequestTypeDef",
    "GetThingShadowRequestRequestTypeDef",
    "ListNamedShadowsForThingRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListRetainedMessagesRequestRequestTypeDef",
    "RetainedMessageSummaryTypeDef",
    "PublishRequestRequestTypeDef",
    "UpdateThingShadowRequestRequestTypeDef",
    "DeleteThingShadowResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetRetainedMessageResponseTypeDef",
    "GetThingShadowResponseTypeDef",
    "ListNamedShadowsForThingResponseTypeDef",
    "UpdateThingShadowResponseTypeDef",
    "ListRetainedMessagesRequestListRetainedMessagesPaginateTypeDef",
    "ListRetainedMessagesResponseTypeDef",
)

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
DeleteThingShadowRequestRequestTypeDef = TypedDict(
    "DeleteThingShadowRequestRequestTypeDef",
    {
        "thingName": str,
        "shadowName": NotRequired[str],
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
GetRetainedMessageRequestRequestTypeDef = TypedDict(
    "GetRetainedMessageRequestRequestTypeDef",
    {
        "topic": str,
    },
)
GetThingShadowRequestRequestTypeDef = TypedDict(
    "GetThingShadowRequestRequestTypeDef",
    {
        "thingName": str,
        "shadowName": NotRequired[str],
    },
)
ListNamedShadowsForThingRequestRequestTypeDef = TypedDict(
    "ListNamedShadowsForThingRequestRequestTypeDef",
    {
        "thingName": str,
        "nextToken": NotRequired[str],
        "pageSize": NotRequired[int],
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
ListRetainedMessagesRequestRequestTypeDef = TypedDict(
    "ListRetainedMessagesRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
RetainedMessageSummaryTypeDef = TypedDict(
    "RetainedMessageSummaryTypeDef",
    {
        "topic": NotRequired[str],
        "payloadSize": NotRequired[int],
        "qos": NotRequired[int],
        "lastModifiedTime": NotRequired[int],
    },
)
PublishRequestRequestTypeDef = TypedDict(
    "PublishRequestRequestTypeDef",
    {
        "topic": str,
        "qos": NotRequired[int],
        "retain": NotRequired[bool],
        "payload": NotRequired[BlobTypeDef],
        "userProperties": NotRequired[str],
        "payloadFormatIndicator": NotRequired[PayloadFormatIndicatorType],
        "contentType": NotRequired[str],
        "responseTopic": NotRequired[str],
        "correlationData": NotRequired[str],
        "messageExpiry": NotRequired[int],
    },
)
UpdateThingShadowRequestRequestTypeDef = TypedDict(
    "UpdateThingShadowRequestRequestTypeDef",
    {
        "thingName": str,
        "payload": BlobTypeDef,
        "shadowName": NotRequired[str],
    },
)
DeleteThingShadowResponseTypeDef = TypedDict(
    "DeleteThingShadowResponseTypeDef",
    {
        "payload": StreamingBody,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRetainedMessageResponseTypeDef = TypedDict(
    "GetRetainedMessageResponseTypeDef",
    {
        "topic": str,
        "payload": bytes,
        "qos": int,
        "lastModifiedTime": int,
        "userProperties": bytes,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetThingShadowResponseTypeDef = TypedDict(
    "GetThingShadowResponseTypeDef",
    {
        "payload": StreamingBody,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListNamedShadowsForThingResponseTypeDef = TypedDict(
    "ListNamedShadowsForThingResponseTypeDef",
    {
        "results": List[str],
        "nextToken": str,
        "timestamp": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateThingShadowResponseTypeDef = TypedDict(
    "UpdateThingShadowResponseTypeDef",
    {
        "payload": StreamingBody,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRetainedMessagesRequestListRetainedMessagesPaginateTypeDef = TypedDict(
    "ListRetainedMessagesRequestListRetainedMessagesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRetainedMessagesResponseTypeDef = TypedDict(
    "ListRetainedMessagesResponseTypeDef",
    {
        "retainedTopics": List[RetainedMessageSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
