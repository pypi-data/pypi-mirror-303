"""
Type annotations for codestar-notifications service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codestar_notifications/type_defs/)

Usage::

    ```python
    from mypy_boto3_codestar_notifications.type_defs import TargetTypeDef

    data: TargetTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    DetailTypeType,
    ListEventTypesFilterNameType,
    ListNotificationRulesFilterNameType,
    ListTargetsFilterNameType,
    NotificationRuleStatusType,
    TargetStatusType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "TargetTypeDef",
    "ResponseMetadataTypeDef",
    "DeleteNotificationRuleRequestRequestTypeDef",
    "DeleteTargetRequestRequestTypeDef",
    "DescribeNotificationRuleRequestRequestTypeDef",
    "EventTypeSummaryTypeDef",
    "TargetSummaryTypeDef",
    "ListEventTypesFilterTypeDef",
    "PaginatorConfigTypeDef",
    "ListNotificationRulesFilterTypeDef",
    "NotificationRuleSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTargetsFilterTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UnsubscribeRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "CreateNotificationRuleRequestRequestTypeDef",
    "SubscribeRequestRequestTypeDef",
    "UpdateNotificationRuleRequestRequestTypeDef",
    "CreateNotificationRuleResultTypeDef",
    "DeleteNotificationRuleResultTypeDef",
    "ListTagsForResourceResultTypeDef",
    "SubscribeResultTypeDef",
    "TagResourceResultTypeDef",
    "UnsubscribeResultTypeDef",
    "ListEventTypesResultTypeDef",
    "DescribeNotificationRuleResultTypeDef",
    "ListTargetsResultTypeDef",
    "ListEventTypesRequestRequestTypeDef",
    "ListEventTypesRequestListEventTypesPaginateTypeDef",
    "ListNotificationRulesRequestListNotificationRulesPaginateTypeDef",
    "ListNotificationRulesRequestRequestTypeDef",
    "ListNotificationRulesResultTypeDef",
    "ListTargetsRequestListTargetsPaginateTypeDef",
    "ListTargetsRequestRequestTypeDef",
)

TargetTypeDef = TypedDict(
    "TargetTypeDef",
    {
        "TargetType": NotRequired[str],
        "TargetAddress": NotRequired[str],
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
DeleteNotificationRuleRequestRequestTypeDef = TypedDict(
    "DeleteNotificationRuleRequestRequestTypeDef",
    {
        "Arn": str,
    },
)
DeleteTargetRequestRequestTypeDef = TypedDict(
    "DeleteTargetRequestRequestTypeDef",
    {
        "TargetAddress": str,
        "ForceUnsubscribeAll": NotRequired[bool],
    },
)
DescribeNotificationRuleRequestRequestTypeDef = TypedDict(
    "DescribeNotificationRuleRequestRequestTypeDef",
    {
        "Arn": str,
    },
)
EventTypeSummaryTypeDef = TypedDict(
    "EventTypeSummaryTypeDef",
    {
        "EventTypeId": NotRequired[str],
        "ServiceName": NotRequired[str],
        "EventTypeName": NotRequired[str],
        "ResourceType": NotRequired[str],
    },
)
TargetSummaryTypeDef = TypedDict(
    "TargetSummaryTypeDef",
    {
        "TargetAddress": NotRequired[str],
        "TargetType": NotRequired[str],
        "TargetStatus": NotRequired[TargetStatusType],
    },
)
ListEventTypesFilterTypeDef = TypedDict(
    "ListEventTypesFilterTypeDef",
    {
        "Name": ListEventTypesFilterNameType,
        "Value": str,
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
ListNotificationRulesFilterTypeDef = TypedDict(
    "ListNotificationRulesFilterTypeDef",
    {
        "Name": ListNotificationRulesFilterNameType,
        "Value": str,
    },
)
NotificationRuleSummaryTypeDef = TypedDict(
    "NotificationRuleSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "Arn": str,
    },
)
ListTargetsFilterTypeDef = TypedDict(
    "ListTargetsFilterTypeDef",
    {
        "Name": ListTargetsFilterNameType,
        "Value": str,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "Arn": str,
        "Tags": Mapping[str, str],
    },
)
UnsubscribeRequestRequestTypeDef = TypedDict(
    "UnsubscribeRequestRequestTypeDef",
    {
        "Arn": str,
        "TargetAddress": str,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "Arn": str,
        "TagKeys": Sequence[str],
    },
)
CreateNotificationRuleRequestRequestTypeDef = TypedDict(
    "CreateNotificationRuleRequestRequestTypeDef",
    {
        "Name": str,
        "EventTypeIds": Sequence[str],
        "Resource": str,
        "Targets": Sequence[TargetTypeDef],
        "DetailType": DetailTypeType,
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "Status": NotRequired[NotificationRuleStatusType],
    },
)
SubscribeRequestRequestTypeDef = TypedDict(
    "SubscribeRequestRequestTypeDef",
    {
        "Arn": str,
        "Target": TargetTypeDef,
        "ClientRequestToken": NotRequired[str],
    },
)
UpdateNotificationRuleRequestRequestTypeDef = TypedDict(
    "UpdateNotificationRuleRequestRequestTypeDef",
    {
        "Arn": str,
        "Name": NotRequired[str],
        "Status": NotRequired[NotificationRuleStatusType],
        "EventTypeIds": NotRequired[Sequence[str]],
        "Targets": NotRequired[Sequence[TargetTypeDef]],
        "DetailType": NotRequired[DetailTypeType],
    },
)
CreateNotificationRuleResultTypeDef = TypedDict(
    "CreateNotificationRuleResultTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteNotificationRuleResultTypeDef = TypedDict(
    "DeleteNotificationRuleResultTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SubscribeResultTypeDef = TypedDict(
    "SubscribeResultTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceResultTypeDef = TypedDict(
    "TagResourceResultTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UnsubscribeResultTypeDef = TypedDict(
    "UnsubscribeResultTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEventTypesResultTypeDef = TypedDict(
    "ListEventTypesResultTypeDef",
    {
        "EventTypes": List[EventTypeSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeNotificationRuleResultTypeDef = TypedDict(
    "DescribeNotificationRuleResultTypeDef",
    {
        "Arn": str,
        "Name": str,
        "EventTypes": List[EventTypeSummaryTypeDef],
        "Resource": str,
        "Targets": List[TargetSummaryTypeDef],
        "DetailType": DetailTypeType,
        "CreatedBy": str,
        "Status": NotificationRuleStatusType,
        "CreatedTimestamp": datetime,
        "LastModifiedTimestamp": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTargetsResultTypeDef = TypedDict(
    "ListTargetsResultTypeDef",
    {
        "Targets": List[TargetSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListEventTypesRequestRequestTypeDef = TypedDict(
    "ListEventTypesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[ListEventTypesFilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListEventTypesRequestListEventTypesPaginateTypeDef = TypedDict(
    "ListEventTypesRequestListEventTypesPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[ListEventTypesFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListNotificationRulesRequestListNotificationRulesPaginateTypeDef = TypedDict(
    "ListNotificationRulesRequestListNotificationRulesPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[ListNotificationRulesFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListNotificationRulesRequestRequestTypeDef = TypedDict(
    "ListNotificationRulesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[ListNotificationRulesFilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListNotificationRulesResultTypeDef = TypedDict(
    "ListNotificationRulesResultTypeDef",
    {
        "NotificationRules": List[NotificationRuleSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTargetsRequestListTargetsPaginateTypeDef = TypedDict(
    "ListTargetsRequestListTargetsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[ListTargetsFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTargetsRequestRequestTypeDef = TypedDict(
    "ListTargetsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[ListTargetsFilterTypeDef]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
