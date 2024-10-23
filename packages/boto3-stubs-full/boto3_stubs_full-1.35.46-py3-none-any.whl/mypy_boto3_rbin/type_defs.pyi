"""
Type annotations for rbin service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rbin/type_defs/)

Usage::

    ```python
    from mypy_boto3_rbin.type_defs import ResourceTagTypeDef

    data: ResourceTagTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import LockStateType, ResourceTypeType, RuleStatusType

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "ResourceTagTypeDef",
    "RetentionPeriodTypeDef",
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "DeleteRuleRequestRequestTypeDef",
    "GetRuleRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "UnlockDelayTypeDef",
    "UnlockRuleRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "ListRulesRequestRequestTypeDef",
    "RuleSummaryTypeDef",
    "UpdateRuleRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "UpdateRuleResponseTypeDef",
    "ListRulesRequestListRulesPaginateTypeDef",
    "LockConfigurationTypeDef",
    "ListRulesResponseTypeDef",
    "CreateRuleRequestRequestTypeDef",
    "CreateRuleResponseTypeDef",
    "GetRuleResponseTypeDef",
    "LockRuleRequestRequestTypeDef",
    "LockRuleResponseTypeDef",
    "UnlockRuleResponseTypeDef",
)

ResourceTagTypeDef = TypedDict(
    "ResourceTagTypeDef",
    {
        "ResourceTagKey": str,
        "ResourceTagValue": NotRequired[str],
    },
)
RetentionPeriodTypeDef = TypedDict(
    "RetentionPeriodTypeDef",
    {
        "RetentionPeriodValue": int,
        "RetentionPeriodUnit": Literal["DAYS"],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
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
DeleteRuleRequestRequestTypeDef = TypedDict(
    "DeleteRuleRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)
GetRuleRequestRequestTypeDef = TypedDict(
    "GetRuleRequestRequestTypeDef",
    {
        "Identifier": str,
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
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
UnlockDelayTypeDef = TypedDict(
    "UnlockDelayTypeDef",
    {
        "UnlockDelayValue": int,
        "UnlockDelayUnit": Literal["DAYS"],
    },
)
UnlockRuleRequestRequestTypeDef = TypedDict(
    "UnlockRuleRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
ListRulesRequestRequestTypeDef = TypedDict(
    "ListRulesRequestRequestTypeDef",
    {
        "ResourceType": ResourceTypeType,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ResourceTags": NotRequired[Sequence[ResourceTagTypeDef]],
        "LockState": NotRequired[LockStateType],
    },
)
RuleSummaryTypeDef = TypedDict(
    "RuleSummaryTypeDef",
    {
        "Identifier": NotRequired[str],
        "Description": NotRequired[str],
        "RetentionPeriod": NotRequired[RetentionPeriodTypeDef],
        "LockState": NotRequired[LockStateType],
        "RuleArn": NotRequired[str],
    },
)
UpdateRuleRequestRequestTypeDef = TypedDict(
    "UpdateRuleRequestRequestTypeDef",
    {
        "Identifier": str,
        "RetentionPeriod": NotRequired[RetentionPeriodTypeDef],
        "Description": NotRequired[str],
        "ResourceType": NotRequired[ResourceTypeType],
        "ResourceTags": NotRequired[Sequence[ResourceTagTypeDef]],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRuleResponseTypeDef = TypedDict(
    "UpdateRuleResponseTypeDef",
    {
        "Identifier": str,
        "RetentionPeriod": RetentionPeriodTypeDef,
        "Description": str,
        "ResourceType": ResourceTypeType,
        "ResourceTags": List[ResourceTagTypeDef],
        "Status": RuleStatusType,
        "LockState": LockStateType,
        "LockEndTime": datetime,
        "RuleArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRulesRequestListRulesPaginateTypeDef = TypedDict(
    "ListRulesRequestListRulesPaginateTypeDef",
    {
        "ResourceType": ResourceTypeType,
        "ResourceTags": NotRequired[Sequence[ResourceTagTypeDef]],
        "LockState": NotRequired[LockStateType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
LockConfigurationTypeDef = TypedDict(
    "LockConfigurationTypeDef",
    {
        "UnlockDelay": UnlockDelayTypeDef,
    },
)
ListRulesResponseTypeDef = TypedDict(
    "ListRulesResponseTypeDef",
    {
        "Rules": List[RuleSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateRuleRequestRequestTypeDef = TypedDict(
    "CreateRuleRequestRequestTypeDef",
    {
        "RetentionPeriod": RetentionPeriodTypeDef,
        "ResourceType": ResourceTypeType,
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ResourceTags": NotRequired[Sequence[ResourceTagTypeDef]],
        "LockConfiguration": NotRequired[LockConfigurationTypeDef],
    },
)
CreateRuleResponseTypeDef = TypedDict(
    "CreateRuleResponseTypeDef",
    {
        "Identifier": str,
        "RetentionPeriod": RetentionPeriodTypeDef,
        "Description": str,
        "Tags": List[TagTypeDef],
        "ResourceType": ResourceTypeType,
        "ResourceTags": List[ResourceTagTypeDef],
        "Status": RuleStatusType,
        "LockConfiguration": LockConfigurationTypeDef,
        "LockState": LockStateType,
        "RuleArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRuleResponseTypeDef = TypedDict(
    "GetRuleResponseTypeDef",
    {
        "Identifier": str,
        "Description": str,
        "ResourceType": ResourceTypeType,
        "RetentionPeriod": RetentionPeriodTypeDef,
        "ResourceTags": List[ResourceTagTypeDef],
        "Status": RuleStatusType,
        "LockConfiguration": LockConfigurationTypeDef,
        "LockState": LockStateType,
        "LockEndTime": datetime,
        "RuleArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LockRuleRequestRequestTypeDef = TypedDict(
    "LockRuleRequestRequestTypeDef",
    {
        "Identifier": str,
        "LockConfiguration": LockConfigurationTypeDef,
    },
)
LockRuleResponseTypeDef = TypedDict(
    "LockRuleResponseTypeDef",
    {
        "Identifier": str,
        "Description": str,
        "ResourceType": ResourceTypeType,
        "RetentionPeriod": RetentionPeriodTypeDef,
        "ResourceTags": List[ResourceTagTypeDef],
        "Status": RuleStatusType,
        "LockConfiguration": LockConfigurationTypeDef,
        "LockState": LockStateType,
        "RuleArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UnlockRuleResponseTypeDef = TypedDict(
    "UnlockRuleResponseTypeDef",
    {
        "Identifier": str,
        "Description": str,
        "ResourceType": ResourceTypeType,
        "RetentionPeriod": RetentionPeriodTypeDef,
        "ResourceTags": List[ResourceTagTypeDef],
        "Status": RuleStatusType,
        "LockConfiguration": LockConfigurationTypeDef,
        "LockState": LockStateType,
        "LockEndTime": datetime,
        "RuleArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
