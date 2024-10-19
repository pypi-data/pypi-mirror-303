"""
Type annotations for personalize-events service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/type_defs/)

Usage::

    ```python
    from mypy_boto3_personalize_events.type_defs import TimestampTypeDef

    data: TimestampTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, Sequence, Union

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "TimestampTypeDef",
    "ActionTypeDef",
    "ResponseMetadataTypeDef",
    "MetricAttributionTypeDef",
    "ItemTypeDef",
    "UserTypeDef",
    "ActionInteractionTypeDef",
    "PutActionsRequestRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EventTypeDef",
    "PutItemsRequestRequestTypeDef",
    "PutUsersRequestRequestTypeDef",
    "PutActionInteractionsRequestRequestTypeDef",
    "PutEventsRequestRequestTypeDef",
)

TimestampTypeDef = Union[datetime, str]
ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "actionId": str,
        "properties": NotRequired[str],
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
MetricAttributionTypeDef = TypedDict(
    "MetricAttributionTypeDef",
    {
        "eventAttributionSource": str,
    },
)
ItemTypeDef = TypedDict(
    "ItemTypeDef",
    {
        "itemId": str,
        "properties": NotRequired[str],
    },
)
UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "userId": str,
        "properties": NotRequired[str],
    },
)
ActionInteractionTypeDef = TypedDict(
    "ActionInteractionTypeDef",
    {
        "actionId": str,
        "sessionId": str,
        "timestamp": TimestampTypeDef,
        "eventType": str,
        "userId": NotRequired[str],
        "eventId": NotRequired[str],
        "recommendationId": NotRequired[str],
        "impression": NotRequired[Sequence[str]],
        "properties": NotRequired[str],
    },
)
PutActionsRequestRequestTypeDef = TypedDict(
    "PutActionsRequestRequestTypeDef",
    {
        "datasetArn": str,
        "actions": Sequence[ActionTypeDef],
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "eventType": str,
        "sentAt": TimestampTypeDef,
        "eventId": NotRequired[str],
        "eventValue": NotRequired[float],
        "itemId": NotRequired[str],
        "properties": NotRequired[str],
        "recommendationId": NotRequired[str],
        "impression": NotRequired[Sequence[str]],
        "metricAttribution": NotRequired[MetricAttributionTypeDef],
    },
)
PutItemsRequestRequestTypeDef = TypedDict(
    "PutItemsRequestRequestTypeDef",
    {
        "datasetArn": str,
        "items": Sequence[ItemTypeDef],
    },
)
PutUsersRequestRequestTypeDef = TypedDict(
    "PutUsersRequestRequestTypeDef",
    {
        "datasetArn": str,
        "users": Sequence[UserTypeDef],
    },
)
PutActionInteractionsRequestRequestTypeDef = TypedDict(
    "PutActionInteractionsRequestRequestTypeDef",
    {
        "trackingId": str,
        "actionInteractions": Sequence[ActionInteractionTypeDef],
    },
)
PutEventsRequestRequestTypeDef = TypedDict(
    "PutEventsRequestRequestTypeDef",
    {
        "trackingId": str,
        "sessionId": str,
        "eventList": Sequence[EventTypeDef],
        "userId": NotRequired[str],
    },
)
