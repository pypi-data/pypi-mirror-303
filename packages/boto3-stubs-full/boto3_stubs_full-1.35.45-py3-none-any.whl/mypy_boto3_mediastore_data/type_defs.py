"""
Type annotations for mediastore-data service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore_data/type_defs/)

Usage::

    ```python
    from mypy_boto3_mediastore_data.type_defs import BlobTypeDef

    data: BlobTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import ItemTypeType, UploadAvailabilityType

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "BlobTypeDef",
    "DeleteObjectRequestRequestTypeDef",
    "DescribeObjectRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "GetObjectRequestRequestTypeDef",
    "ItemTypeDef",
    "PaginatorConfigTypeDef",
    "ListItemsRequestRequestTypeDef",
    "PutObjectRequestRequestTypeDef",
    "DescribeObjectResponseTypeDef",
    "GetObjectResponseTypeDef",
    "PutObjectResponseTypeDef",
    "ListItemsResponseTypeDef",
    "ListItemsRequestListItemsPaginateTypeDef",
)

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
DeleteObjectRequestRequestTypeDef = TypedDict(
    "DeleteObjectRequestRequestTypeDef",
    {
        "Path": str,
    },
)
DescribeObjectRequestRequestTypeDef = TypedDict(
    "DescribeObjectRequestRequestTypeDef",
    {
        "Path": str,
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
GetObjectRequestRequestTypeDef = TypedDict(
    "GetObjectRequestRequestTypeDef",
    {
        "Path": str,
        "Range": NotRequired[str],
    },
)
ItemTypeDef = TypedDict(
    "ItemTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[ItemTypeType],
        "ETag": NotRequired[str],
        "LastModified": NotRequired[datetime],
        "ContentType": NotRequired[str],
        "ContentLength": NotRequired[int],
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
ListItemsRequestRequestTypeDef = TypedDict(
    "ListItemsRequestRequestTypeDef",
    {
        "Path": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
PutObjectRequestRequestTypeDef = TypedDict(
    "PutObjectRequestRequestTypeDef",
    {
        "Body": BlobTypeDef,
        "Path": str,
        "ContentType": NotRequired[str],
        "CacheControl": NotRequired[str],
        "StorageClass": NotRequired[Literal["TEMPORAL"]],
        "UploadAvailability": NotRequired[UploadAvailabilityType],
    },
)
DescribeObjectResponseTypeDef = TypedDict(
    "DescribeObjectResponseTypeDef",
    {
        "ETag": str,
        "ContentType": str,
        "ContentLength": int,
        "CacheControl": str,
        "LastModified": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetObjectResponseTypeDef = TypedDict(
    "GetObjectResponseTypeDef",
    {
        "Body": StreamingBody,
        "CacheControl": str,
        "ContentRange": str,
        "ContentLength": int,
        "ContentType": str,
        "ETag": str,
        "LastModified": datetime,
        "StatusCode": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutObjectResponseTypeDef = TypedDict(
    "PutObjectResponseTypeDef",
    {
        "ContentSHA256": str,
        "ETag": str,
        "StorageClass": Literal["TEMPORAL"],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListItemsResponseTypeDef = TypedDict(
    "ListItemsResponseTypeDef",
    {
        "Items": List[ItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListItemsRequestListItemsPaginateTypeDef = TypedDict(
    "ListItemsRequestListItemsPaginateTypeDef",
    {
        "Path": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
