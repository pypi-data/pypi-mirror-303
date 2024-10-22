"""
Type annotations for freetier service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_freetier/type_defs/)

Usage::

    ```python
    from mypy_boto3_freetier.type_defs import DimensionValuesTypeDef

    data: DimensionValuesTypeDef = ...
    ```
"""

import sys
from typing import Any, Dict, List, Mapping, Sequence

from .literals import DimensionType, MatchOptionType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "DimensionValuesTypeDef",
    "FreeTierUsageTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "ExpressionPaginatorTypeDef",
    "ExpressionTypeDef",
    "GetFreeTierUsageResponseTypeDef",
    "GetFreeTierUsageRequestGetFreeTierUsagePaginateTypeDef",
    "GetFreeTierUsageRequestRequestTypeDef",
)

DimensionValuesTypeDef = TypedDict(
    "DimensionValuesTypeDef",
    {
        "Key": DimensionType,
        "MatchOptions": Sequence[MatchOptionType],
        "Values": Sequence[str],
    },
)
FreeTierUsageTypeDef = TypedDict(
    "FreeTierUsageTypeDef",
    {
        "actualUsageAmount": NotRequired[float],
        "description": NotRequired[str],
        "forecastedUsageAmount": NotRequired[float],
        "freeTierType": NotRequired[str],
        "limit": NotRequired[float],
        "operation": NotRequired[str],
        "region": NotRequired[str],
        "service": NotRequired[str],
        "unit": NotRequired[str],
        "usageType": NotRequired[str],
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
ExpressionPaginatorTypeDef = TypedDict(
    "ExpressionPaginatorTypeDef",
    {
        "And": NotRequired[Sequence[Mapping[str, Any]]],
        "Dimensions": NotRequired[DimensionValuesTypeDef],
        "Not": NotRequired[Mapping[str, Any]],
        "Or": NotRequired[Sequence[Mapping[str, Any]]],
    },
)
ExpressionTypeDef = TypedDict(
    "ExpressionTypeDef",
    {
        "And": NotRequired[Sequence[Mapping[str, Any]]],
        "Dimensions": NotRequired[DimensionValuesTypeDef],
        "Not": NotRequired[Mapping[str, Any]],
        "Or": NotRequired[Sequence[Mapping[str, Any]]],
    },
)
GetFreeTierUsageResponseTypeDef = TypedDict(
    "GetFreeTierUsageResponseTypeDef",
    {
        "freeTierUsages": List[FreeTierUsageTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFreeTierUsageRequestGetFreeTierUsagePaginateTypeDef = TypedDict(
    "GetFreeTierUsageRequestGetFreeTierUsagePaginateTypeDef",
    {
        "filter": NotRequired[ExpressionPaginatorTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetFreeTierUsageRequestRequestTypeDef = TypedDict(
    "GetFreeTierUsageRequestRequestTypeDef",
    {
        "filter": NotRequired[ExpressionTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
