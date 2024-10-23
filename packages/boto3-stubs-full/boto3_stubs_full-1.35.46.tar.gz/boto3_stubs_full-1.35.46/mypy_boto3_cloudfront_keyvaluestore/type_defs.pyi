"""
Type annotations for cloudfront-keyvaluestore service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront_keyvaluestore/type_defs/)

Usage::

    ```python
    from mypy_boto3_cloudfront_keyvaluestore.type_defs import DeleteKeyRequestListItemTypeDef

    data: DeleteKeyRequestListItemTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "DeleteKeyRequestListItemTypeDef",
    "DeleteKeyRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "DescribeKeyValueStoreRequestRequestTypeDef",
    "GetKeyRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListKeysRequestRequestTypeDef",
    "ListKeysResponseListItemTypeDef",
    "PutKeyRequestListItemTypeDef",
    "PutKeyRequestRequestTypeDef",
    "DeleteKeyResponseTypeDef",
    "DescribeKeyValueStoreResponseTypeDef",
    "GetKeyResponseTypeDef",
    "PutKeyResponseTypeDef",
    "UpdateKeysResponseTypeDef",
    "ListKeysRequestListKeysPaginateTypeDef",
    "ListKeysResponseTypeDef",
    "UpdateKeysRequestRequestTypeDef",
)

DeleteKeyRequestListItemTypeDef = TypedDict(
    "DeleteKeyRequestListItemTypeDef",
    {
        "Key": str,
    },
)
DeleteKeyRequestRequestTypeDef = TypedDict(
    "DeleteKeyRequestRequestTypeDef",
    {
        "KvsARN": str,
        "Key": str,
        "IfMatch": str,
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
DescribeKeyValueStoreRequestRequestTypeDef = TypedDict(
    "DescribeKeyValueStoreRequestRequestTypeDef",
    {
        "KvsARN": str,
    },
)
GetKeyRequestRequestTypeDef = TypedDict(
    "GetKeyRequestRequestTypeDef",
    {
        "KvsARN": str,
        "Key": str,
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
ListKeysRequestRequestTypeDef = TypedDict(
    "ListKeysRequestRequestTypeDef",
    {
        "KvsARN": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListKeysResponseListItemTypeDef = TypedDict(
    "ListKeysResponseListItemTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
PutKeyRequestListItemTypeDef = TypedDict(
    "PutKeyRequestListItemTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
PutKeyRequestRequestTypeDef = TypedDict(
    "PutKeyRequestRequestTypeDef",
    {
        "Key": str,
        "Value": str,
        "KvsARN": str,
        "IfMatch": str,
    },
)
DeleteKeyResponseTypeDef = TypedDict(
    "DeleteKeyResponseTypeDef",
    {
        "ItemCount": int,
        "TotalSizeInBytes": int,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeKeyValueStoreResponseTypeDef = TypedDict(
    "DescribeKeyValueStoreResponseTypeDef",
    {
        "ItemCount": int,
        "TotalSizeInBytes": int,
        "KvsARN": str,
        "Created": datetime,
        "ETag": str,
        "LastModified": datetime,
        "Status": str,
        "FailureReason": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetKeyResponseTypeDef = TypedDict(
    "GetKeyResponseTypeDef",
    {
        "Key": str,
        "Value": str,
        "ItemCount": int,
        "TotalSizeInBytes": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutKeyResponseTypeDef = TypedDict(
    "PutKeyResponseTypeDef",
    {
        "ItemCount": int,
        "TotalSizeInBytes": int,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateKeysResponseTypeDef = TypedDict(
    "UpdateKeysResponseTypeDef",
    {
        "ItemCount": int,
        "TotalSizeInBytes": int,
        "ETag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListKeysRequestListKeysPaginateTypeDef = TypedDict(
    "ListKeysRequestListKeysPaginateTypeDef",
    {
        "KvsARN": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListKeysResponseTypeDef = TypedDict(
    "ListKeysResponseTypeDef",
    {
        "Items": List[ListKeysResponseListItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateKeysRequestRequestTypeDef = TypedDict(
    "UpdateKeysRequestRequestTypeDef",
    {
        "KvsARN": str,
        "IfMatch": str,
        "Puts": NotRequired[Sequence[PutKeyRequestListItemTypeDef]],
        "Deletes": NotRequired[Sequence[DeleteKeyRequestListItemTypeDef]],
    },
)
