"""
Type annotations for ebs service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ebs/type_defs/)

Usage::

    ```python
    from mypy_boto3_ebs.type_defs import BlobTypeDef

    data: BlobTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Sequence, Union

from botocore.response import StreamingBody

from .literals import SSETypeType, StatusType

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "BlobTypeDef",
    "BlockTypeDef",
    "ChangedBlockTypeDef",
    "CompleteSnapshotRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "GetSnapshotBlockRequestRequestTypeDef",
    "ListChangedBlocksRequestRequestTypeDef",
    "ListSnapshotBlocksRequestRequestTypeDef",
    "TagTypeDef",
    "PutSnapshotBlockRequestRequestTypeDef",
    "CompleteSnapshotResponseTypeDef",
    "GetSnapshotBlockResponseTypeDef",
    "ListChangedBlocksResponseTypeDef",
    "ListSnapshotBlocksResponseTypeDef",
    "PutSnapshotBlockResponseTypeDef",
    "StartSnapshotRequestRequestTypeDef",
    "StartSnapshotResponseTypeDef",
)

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
BlockTypeDef = TypedDict(
    "BlockTypeDef",
    {
        "BlockIndex": NotRequired[int],
        "BlockToken": NotRequired[str],
    },
)
ChangedBlockTypeDef = TypedDict(
    "ChangedBlockTypeDef",
    {
        "BlockIndex": NotRequired[int],
        "FirstBlockToken": NotRequired[str],
        "SecondBlockToken": NotRequired[str],
    },
)
CompleteSnapshotRequestRequestTypeDef = TypedDict(
    "CompleteSnapshotRequestRequestTypeDef",
    {
        "SnapshotId": str,
        "ChangedBlocksCount": int,
        "Checksum": NotRequired[str],
        "ChecksumAlgorithm": NotRequired[Literal["SHA256"]],
        "ChecksumAggregationMethod": NotRequired[Literal["LINEAR"]],
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
GetSnapshotBlockRequestRequestTypeDef = TypedDict(
    "GetSnapshotBlockRequestRequestTypeDef",
    {
        "SnapshotId": str,
        "BlockIndex": int,
        "BlockToken": str,
    },
)
ListChangedBlocksRequestRequestTypeDef = TypedDict(
    "ListChangedBlocksRequestRequestTypeDef",
    {
        "SecondSnapshotId": str,
        "FirstSnapshotId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "StartingBlockIndex": NotRequired[int],
    },
)
ListSnapshotBlocksRequestRequestTypeDef = TypedDict(
    "ListSnapshotBlocksRequestRequestTypeDef",
    {
        "SnapshotId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "StartingBlockIndex": NotRequired[int],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
PutSnapshotBlockRequestRequestTypeDef = TypedDict(
    "PutSnapshotBlockRequestRequestTypeDef",
    {
        "SnapshotId": str,
        "BlockIndex": int,
        "BlockData": BlobTypeDef,
        "DataLength": int,
        "Checksum": str,
        "ChecksumAlgorithm": Literal["SHA256"],
        "Progress": NotRequired[int],
    },
)
CompleteSnapshotResponseTypeDef = TypedDict(
    "CompleteSnapshotResponseTypeDef",
    {
        "Status": StatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSnapshotBlockResponseTypeDef = TypedDict(
    "GetSnapshotBlockResponseTypeDef",
    {
        "DataLength": int,
        "BlockData": StreamingBody,
        "Checksum": str,
        "ChecksumAlgorithm": Literal["SHA256"],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListChangedBlocksResponseTypeDef = TypedDict(
    "ListChangedBlocksResponseTypeDef",
    {
        "ChangedBlocks": List[ChangedBlockTypeDef],
        "ExpiryTime": datetime,
        "VolumeSize": int,
        "BlockSize": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListSnapshotBlocksResponseTypeDef = TypedDict(
    "ListSnapshotBlocksResponseTypeDef",
    {
        "Blocks": List[BlockTypeDef],
        "ExpiryTime": datetime,
        "VolumeSize": int,
        "BlockSize": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PutSnapshotBlockResponseTypeDef = TypedDict(
    "PutSnapshotBlockResponseTypeDef",
    {
        "Checksum": str,
        "ChecksumAlgorithm": Literal["SHA256"],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartSnapshotRequestRequestTypeDef = TypedDict(
    "StartSnapshotRequestRequestTypeDef",
    {
        "VolumeSize": int,
        "ParentSnapshotId": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "Description": NotRequired[str],
        "ClientToken": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "KmsKeyArn": NotRequired[str],
        "Timeout": NotRequired[int],
    },
)
StartSnapshotResponseTypeDef = TypedDict(
    "StartSnapshotResponseTypeDef",
    {
        "Description": str,
        "SnapshotId": str,
        "OwnerId": str,
        "Status": StatusType,
        "StartTime": datetime,
        "VolumeSize": int,
        "BlockSize": int,
        "Tags": List[TagTypeDef],
        "ParentSnapshotId": str,
        "KmsKeyArn": str,
        "SseType": SSETypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
