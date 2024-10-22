"""
Type annotations for kendra-ranking service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra_ranking/type_defs/)

Usage::

    ```python
    from mypy_boto3_kendra_ranking.type_defs import CapacityUnitsConfigurationTypeDef

    data: CapacityUnitsConfigurationTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import RescoreExecutionPlanStatusType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "CapacityUnitsConfigurationTypeDef",
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "DeleteRescoreExecutionPlanRequestRequestTypeDef",
    "DescribeRescoreExecutionPlanRequestRequestTypeDef",
    "DocumentTypeDef",
    "ListRescoreExecutionPlansRequestRequestTypeDef",
    "RescoreExecutionPlanSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "RescoreResultItemTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateRescoreExecutionPlanRequestRequestTypeDef",
    "CreateRescoreExecutionPlanRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateRescoreExecutionPlanResponseTypeDef",
    "DescribeRescoreExecutionPlanResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "RescoreRequestRequestTypeDef",
    "ListRescoreExecutionPlansResponseTypeDef",
    "RescoreResultTypeDef",
)

CapacityUnitsConfigurationTypeDef = TypedDict(
    "CapacityUnitsConfigurationTypeDef",
    {
        "RescoreCapacityUnits": int,
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
DeleteRescoreExecutionPlanRequestRequestTypeDef = TypedDict(
    "DeleteRescoreExecutionPlanRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DescribeRescoreExecutionPlanRequestRequestTypeDef = TypedDict(
    "DescribeRescoreExecutionPlanRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DocumentTypeDef = TypedDict(
    "DocumentTypeDef",
    {
        "Id": str,
        "OriginalScore": float,
        "GroupId": NotRequired[str],
        "Title": NotRequired[str],
        "Body": NotRequired[str],
        "TokenizedTitle": NotRequired[Sequence[str]],
        "TokenizedBody": NotRequired[Sequence[str]],
    },
)
ListRescoreExecutionPlansRequestRequestTypeDef = TypedDict(
    "ListRescoreExecutionPlansRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
RescoreExecutionPlanSummaryTypeDef = TypedDict(
    "RescoreExecutionPlanSummaryTypeDef",
    {
        "Name": NotRequired[str],
        "Id": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
        "Status": NotRequired[RescoreExecutionPlanStatusType],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
RescoreResultItemTypeDef = TypedDict(
    "RescoreResultItemTypeDef",
    {
        "DocumentId": NotRequired[str],
        "Score": NotRequired[float],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
UpdateRescoreExecutionPlanRequestRequestTypeDef = TypedDict(
    "UpdateRescoreExecutionPlanRequestRequestTypeDef",
    {
        "Id": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "CapacityUnits": NotRequired[CapacityUnitsConfigurationTypeDef],
    },
)
CreateRescoreExecutionPlanRequestRequestTypeDef = TypedDict(
    "CreateRescoreExecutionPlanRequestRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "CapacityUnits": NotRequired[CapacityUnitsConfigurationTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ClientToken": NotRequired[str],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CreateRescoreExecutionPlanResponseTypeDef = TypedDict(
    "CreateRescoreExecutionPlanResponseTypeDef",
    {
        "Id": str,
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRescoreExecutionPlanResponseTypeDef = TypedDict(
    "DescribeRescoreExecutionPlanResponseTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "CapacityUnits": CapacityUnitsConfigurationTypeDef,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Status": RescoreExecutionPlanStatusType,
        "ErrorMessage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RescoreRequestRequestTypeDef = TypedDict(
    "RescoreRequestRequestTypeDef",
    {
        "RescoreExecutionPlanId": str,
        "SearchQuery": str,
        "Documents": Sequence[DocumentTypeDef],
    },
)
ListRescoreExecutionPlansResponseTypeDef = TypedDict(
    "ListRescoreExecutionPlansResponseTypeDef",
    {
        "SummaryItems": List[RescoreExecutionPlanSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
RescoreResultTypeDef = TypedDict(
    "RescoreResultTypeDef",
    {
        "RescoreId": str,
        "ResultItems": List[RescoreResultItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
