"""
Type annotations for dynamodbstreams service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodbstreams/type_defs/)

Usage::

    ```python
    from mypy_boto3_dynamodbstreams.type_defs import AttributeValueTypeDef

    data: AttributeValueTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    KeyTypeType,
    OperationTypeType,
    ShardIteratorTypeType,
    StreamStatusType,
    StreamViewTypeType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AttributeValueTypeDef",
    "DescribeStreamInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "GetRecordsInputRequestTypeDef",
    "GetShardIteratorInputRequestTypeDef",
    "IdentityTypeDef",
    "KeySchemaElementTypeDef",
    "ListStreamsInputRequestTypeDef",
    "StreamTypeDef",
    "SequenceNumberRangeTypeDef",
    "StreamRecordTypeDef",
    "GetShardIteratorOutputTypeDef",
    "ListStreamsOutputTypeDef",
    "ShardTypeDef",
    "RecordTypeDef",
    "StreamDescriptionTypeDef",
    "GetRecordsOutputTypeDef",
    "DescribeStreamOutputTypeDef",
)

AttributeValueTypeDef = TypedDict(
    "AttributeValueTypeDef",
    {
        "S": NotRequired[str],
        "N": NotRequired[str],
        "B": NotRequired[bytes],
        "SS": NotRequired[List[str]],
        "NS": NotRequired[List[str]],
        "BS": NotRequired[List[bytes]],
        "M": NotRequired[Dict[str, Dict[str, Any]]],
        "L": NotRequired[List[Dict[str, Any]]],
        "NULL": NotRequired[bool],
        "BOOL": NotRequired[bool],
    },
)
DescribeStreamInputRequestTypeDef = TypedDict(
    "DescribeStreamInputRequestTypeDef",
    {
        "StreamArn": str,
        "Limit": NotRequired[int],
        "ExclusiveStartShardId": NotRequired[str],
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
GetRecordsInputRequestTypeDef = TypedDict(
    "GetRecordsInputRequestTypeDef",
    {
        "ShardIterator": str,
        "Limit": NotRequired[int],
    },
)
GetShardIteratorInputRequestTypeDef = TypedDict(
    "GetShardIteratorInputRequestTypeDef",
    {
        "StreamArn": str,
        "ShardId": str,
        "ShardIteratorType": ShardIteratorTypeType,
        "SequenceNumber": NotRequired[str],
    },
)
IdentityTypeDef = TypedDict(
    "IdentityTypeDef",
    {
        "PrincipalId": NotRequired[str],
        "Type": NotRequired[str],
    },
)
KeySchemaElementTypeDef = TypedDict(
    "KeySchemaElementTypeDef",
    {
        "AttributeName": str,
        "KeyType": KeyTypeType,
    },
)
ListStreamsInputRequestTypeDef = TypedDict(
    "ListStreamsInputRequestTypeDef",
    {
        "TableName": NotRequired[str],
        "Limit": NotRequired[int],
        "ExclusiveStartStreamArn": NotRequired[str],
    },
)
StreamTypeDef = TypedDict(
    "StreamTypeDef",
    {
        "StreamArn": NotRequired[str],
        "TableName": NotRequired[str],
        "StreamLabel": NotRequired[str],
    },
)
SequenceNumberRangeTypeDef = TypedDict(
    "SequenceNumberRangeTypeDef",
    {
        "StartingSequenceNumber": NotRequired[str],
        "EndingSequenceNumber": NotRequired[str],
    },
)
StreamRecordTypeDef = TypedDict(
    "StreamRecordTypeDef",
    {
        "ApproximateCreationDateTime": NotRequired[datetime],
        "Keys": NotRequired[Dict[str, AttributeValueTypeDef]],
        "NewImage": NotRequired[Dict[str, AttributeValueTypeDef]],
        "OldImage": NotRequired[Dict[str, AttributeValueTypeDef]],
        "SequenceNumber": NotRequired[str],
        "SizeBytes": NotRequired[int],
        "StreamViewType": NotRequired[StreamViewTypeType],
    },
)
GetShardIteratorOutputTypeDef = TypedDict(
    "GetShardIteratorOutputTypeDef",
    {
        "ShardIterator": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListStreamsOutputTypeDef = TypedDict(
    "ListStreamsOutputTypeDef",
    {
        "Streams": List[StreamTypeDef],
        "LastEvaluatedStreamArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ShardTypeDef = TypedDict(
    "ShardTypeDef",
    {
        "ShardId": NotRequired[str],
        "SequenceNumberRange": NotRequired[SequenceNumberRangeTypeDef],
        "ParentShardId": NotRequired[str],
    },
)
RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "eventID": NotRequired[str],
        "eventName": NotRequired[OperationTypeType],
        "eventVersion": NotRequired[str],
        "eventSource": NotRequired[str],
        "awsRegion": NotRequired[str],
        "dynamodb": NotRequired[StreamRecordTypeDef],
        "userIdentity": NotRequired[IdentityTypeDef],
    },
)
StreamDescriptionTypeDef = TypedDict(
    "StreamDescriptionTypeDef",
    {
        "StreamArn": NotRequired[str],
        "StreamLabel": NotRequired[str],
        "StreamStatus": NotRequired[StreamStatusType],
        "StreamViewType": NotRequired[StreamViewTypeType],
        "CreationRequestDateTime": NotRequired[datetime],
        "TableName": NotRequired[str],
        "KeySchema": NotRequired[List[KeySchemaElementTypeDef]],
        "Shards": NotRequired[List[ShardTypeDef]],
        "LastEvaluatedShardId": NotRequired[str],
    },
)
GetRecordsOutputTypeDef = TypedDict(
    "GetRecordsOutputTypeDef",
    {
        "Records": List[RecordTypeDef],
        "NextShardIterator": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeStreamOutputTypeDef = TypedDict(
    "DescribeStreamOutputTypeDef",
    {
        "StreamDescription": StreamDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
