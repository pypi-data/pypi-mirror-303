"""
Type annotations for apigatewaymanagementapi service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewaymanagementapi/type_defs/)

Usage::

    ```python
    from mypy_boto3_apigatewaymanagementapi.type_defs import BlobTypeDef

    data: BlobTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, Union

from botocore.response import StreamingBody

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "BlobTypeDef",
    "DeleteConnectionRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "GetConnectionRequestRequestTypeDef",
    "IdentityTypeDef",
    "PostToConnectionRequestRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetConnectionResponseTypeDef",
)

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
DeleteConnectionRequestRequestTypeDef = TypedDict(
    "DeleteConnectionRequestRequestTypeDef",
    {
        "ConnectionId": str,
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
GetConnectionRequestRequestTypeDef = TypedDict(
    "GetConnectionRequestRequestTypeDef",
    {
        "ConnectionId": str,
    },
)
IdentityTypeDef = TypedDict(
    "IdentityTypeDef",
    {
        "SourceIp": str,
        "UserAgent": str,
    },
)
PostToConnectionRequestRequestTypeDef = TypedDict(
    "PostToConnectionRequestRequestTypeDef",
    {
        "Data": BlobTypeDef,
        "ConnectionId": str,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetConnectionResponseTypeDef = TypedDict(
    "GetConnectionResponseTypeDef",
    {
        "ConnectedAt": datetime,
        "Identity": IdentityTypeDef,
        "LastActiveAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
