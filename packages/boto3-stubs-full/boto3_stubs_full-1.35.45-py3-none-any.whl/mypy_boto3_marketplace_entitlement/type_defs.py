"""
Type annotations for marketplace-entitlement service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_entitlement/type_defs/)

Usage::

    ```python
    from mypy_boto3_marketplace_entitlement.type_defs import EntitlementValueTypeDef

    data: EntitlementValueTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import GetEntitlementFilterNameType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "EntitlementValueTypeDef",
    "PaginatorConfigTypeDef",
    "GetEntitlementsRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "EntitlementTypeDef",
    "GetEntitlementsRequestGetEntitlementsPaginateTypeDef",
    "GetEntitlementsResultTypeDef",
)

EntitlementValueTypeDef = TypedDict(
    "EntitlementValueTypeDef",
    {
        "IntegerValue": NotRequired[int],
        "DoubleValue": NotRequired[float],
        "BooleanValue": NotRequired[bool],
        "StringValue": NotRequired[str],
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
GetEntitlementsRequestRequestTypeDef = TypedDict(
    "GetEntitlementsRequestRequestTypeDef",
    {
        "ProductCode": str,
        "Filter": NotRequired[Mapping[GetEntitlementFilterNameType, Sequence[str]]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
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
EntitlementTypeDef = TypedDict(
    "EntitlementTypeDef",
    {
        "ProductCode": NotRequired[str],
        "Dimension": NotRequired[str],
        "CustomerIdentifier": NotRequired[str],
        "Value": NotRequired[EntitlementValueTypeDef],
        "ExpirationDate": NotRequired[datetime],
    },
)
GetEntitlementsRequestGetEntitlementsPaginateTypeDef = TypedDict(
    "GetEntitlementsRequestGetEntitlementsPaginateTypeDef",
    {
        "ProductCode": str,
        "Filter": NotRequired[Mapping[GetEntitlementFilterNameType, Sequence[str]]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetEntitlementsResultTypeDef = TypedDict(
    "GetEntitlementsResultTypeDef",
    {
        "Entitlements": List[EntitlementTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
