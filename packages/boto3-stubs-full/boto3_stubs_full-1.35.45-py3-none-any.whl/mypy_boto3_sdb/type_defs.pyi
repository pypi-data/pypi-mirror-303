"""
Type annotations for sdb service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/type_defs/)

Usage::

    ```python
    from mypy_boto3_sdb.type_defs import AttributeTypeDef

    data: AttributeTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Sequence

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AttributeTypeDef",
    "CreateDomainRequestRequestTypeDef",
    "UpdateConditionTypeDef",
    "DeleteDomainRequestRequestTypeDef",
    "DomainMetadataRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "GetAttributesRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListDomainsRequestRequestTypeDef",
    "ReplaceableAttributeTypeDef",
    "SelectRequestRequestTypeDef",
    "DeletableItemTypeDef",
    "ItemTypeDef",
    "DeleteAttributesRequestRequestTypeDef",
    "DomainMetadataResultTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetAttributesResultTypeDef",
    "ListDomainsResultTypeDef",
    "ListDomainsRequestListDomainsPaginateTypeDef",
    "SelectRequestSelectPaginateTypeDef",
    "PutAttributesRequestRequestTypeDef",
    "ReplaceableItemTypeDef",
    "BatchDeleteAttributesRequestRequestTypeDef",
    "SelectResultTypeDef",
    "BatchPutAttributesRequestRequestTypeDef",
)

AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "Name": str,
        "Value": str,
        "AlternateNameEncoding": NotRequired[str],
        "AlternateValueEncoding": NotRequired[str],
    },
)
CreateDomainRequestRequestTypeDef = TypedDict(
    "CreateDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
UpdateConditionTypeDef = TypedDict(
    "UpdateConditionTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
        "Exists": NotRequired[bool],
    },
)
DeleteDomainRequestRequestTypeDef = TypedDict(
    "DeleteDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
DomainMetadataRequestRequestTypeDef = TypedDict(
    "DomainMetadataRequestRequestTypeDef",
    {
        "DomainName": str,
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
GetAttributesRequestRequestTypeDef = TypedDict(
    "GetAttributesRequestRequestTypeDef",
    {
        "DomainName": str,
        "ItemName": str,
        "AttributeNames": NotRequired[Sequence[str]],
        "ConsistentRead": NotRequired[bool],
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
ListDomainsRequestRequestTypeDef = TypedDict(
    "ListDomainsRequestRequestTypeDef",
    {
        "MaxNumberOfDomains": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ReplaceableAttributeTypeDef = TypedDict(
    "ReplaceableAttributeTypeDef",
    {
        "Name": str,
        "Value": str,
        "Replace": NotRequired[bool],
    },
)
SelectRequestRequestTypeDef = TypedDict(
    "SelectRequestRequestTypeDef",
    {
        "SelectExpression": str,
        "NextToken": NotRequired[str],
        "ConsistentRead": NotRequired[bool],
    },
)
DeletableItemTypeDef = TypedDict(
    "DeletableItemTypeDef",
    {
        "Name": str,
        "Attributes": NotRequired[Sequence[AttributeTypeDef]],
    },
)
ItemTypeDef = TypedDict(
    "ItemTypeDef",
    {
        "Name": str,
        "Attributes": List[AttributeTypeDef],
        "AlternateNameEncoding": NotRequired[str],
    },
)
DeleteAttributesRequestRequestTypeDef = TypedDict(
    "DeleteAttributesRequestRequestTypeDef",
    {
        "DomainName": str,
        "ItemName": str,
        "Attributes": NotRequired[Sequence[AttributeTypeDef]],
        "Expected": NotRequired[UpdateConditionTypeDef],
    },
)
DomainMetadataResultTypeDef = TypedDict(
    "DomainMetadataResultTypeDef",
    {
        "ItemCount": int,
        "ItemNamesSizeBytes": int,
        "AttributeNameCount": int,
        "AttributeNamesSizeBytes": int,
        "AttributeValueCount": int,
        "AttributeValuesSizeBytes": int,
        "Timestamp": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAttributesResultTypeDef = TypedDict(
    "GetAttributesResultTypeDef",
    {
        "Attributes": List[AttributeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDomainsResultTypeDef = TypedDict(
    "ListDomainsResultTypeDef",
    {
        "DomainNames": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListDomainsRequestListDomainsPaginateTypeDef = TypedDict(
    "ListDomainsRequestListDomainsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SelectRequestSelectPaginateTypeDef = TypedDict(
    "SelectRequestSelectPaginateTypeDef",
    {
        "SelectExpression": str,
        "ConsistentRead": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
PutAttributesRequestRequestTypeDef = TypedDict(
    "PutAttributesRequestRequestTypeDef",
    {
        "DomainName": str,
        "ItemName": str,
        "Attributes": Sequence[ReplaceableAttributeTypeDef],
        "Expected": NotRequired[UpdateConditionTypeDef],
    },
)
ReplaceableItemTypeDef = TypedDict(
    "ReplaceableItemTypeDef",
    {
        "Name": str,
        "Attributes": Sequence[ReplaceableAttributeTypeDef],
    },
)
BatchDeleteAttributesRequestRequestTypeDef = TypedDict(
    "BatchDeleteAttributesRequestRequestTypeDef",
    {
        "DomainName": str,
        "Items": Sequence[DeletableItemTypeDef],
    },
)
SelectResultTypeDef = TypedDict(
    "SelectResultTypeDef",
    {
        "Items": List[ItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
BatchPutAttributesRequestRequestTypeDef = TypedDict(
    "BatchPutAttributesRequestRequestTypeDef",
    {
        "DomainName": str,
        "Items": Sequence[ReplaceableItemTypeDef],
    },
)
