"""
Type annotations for workmailmessageflow service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmailmessageflow/type_defs/)

Usage::

    ```python
    from mypy_boto3_workmailmessageflow.type_defs import GetRawMessageContentRequestRequestTypeDef

    data: GetRawMessageContentRequestRequestTypeDef = ...
    ```
"""

import sys
from typing import Dict

from botocore.response import StreamingBody

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "GetRawMessageContentRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "S3ReferenceTypeDef",
    "GetRawMessageContentResponseTypeDef",
    "RawMessageContentTypeDef",
    "PutRawMessageContentRequestRequestTypeDef",
)

GetRawMessageContentRequestRequestTypeDef = TypedDict(
    "GetRawMessageContentRequestRequestTypeDef",
    {
        "messageId": str,
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
S3ReferenceTypeDef = TypedDict(
    "S3ReferenceTypeDef",
    {
        "bucket": str,
        "key": str,
        "objectVersion": NotRequired[str],
    },
)
GetRawMessageContentResponseTypeDef = TypedDict(
    "GetRawMessageContentResponseTypeDef",
    {
        "messageContent": StreamingBody,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RawMessageContentTypeDef = TypedDict(
    "RawMessageContentTypeDef",
    {
        "s3Reference": S3ReferenceTypeDef,
    },
)
PutRawMessageContentRequestRequestTypeDef = TypedDict(
    "PutRawMessageContentRequestRequestTypeDef",
    {
        "messageId": str,
        "content": RawMessageContentTypeDef,
    },
)
