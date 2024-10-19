"""
Type annotations for qldb-session service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qldb_session/type_defs/)

Usage::

    ```python
    from mypy_boto3_qldb_session.type_defs import TimingInformationTypeDef

    data: TimingInformationTypeDef = ...
    ```
"""

import sys
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "TimingInformationTypeDef",
    "BlobTypeDef",
    "IOUsageTypeDef",
    "FetchPageRequestTypeDef",
    "ValueHolderOutputTypeDef",
    "ResponseMetadataTypeDef",
    "StartSessionRequestTypeDef",
    "AbortTransactionResultTypeDef",
    "EndSessionResultTypeDef",
    "StartSessionResultTypeDef",
    "StartTransactionResultTypeDef",
    "CommitTransactionRequestTypeDef",
    "ValueHolderTypeDef",
    "CommitTransactionResultTypeDef",
    "PageTypeDef",
    "ValueHolderUnionTypeDef",
    "ExecuteStatementResultTypeDef",
    "FetchPageResultTypeDef",
    "ExecuteStatementRequestTypeDef",
    "SendCommandResultTypeDef",
    "SendCommandRequestRequestTypeDef",
)

TimingInformationTypeDef = TypedDict(
    "TimingInformationTypeDef",
    {
        "ProcessingTimeMilliseconds": NotRequired[int],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
IOUsageTypeDef = TypedDict(
    "IOUsageTypeDef",
    {
        "ReadIOs": NotRequired[int],
        "WriteIOs": NotRequired[int],
    },
)
FetchPageRequestTypeDef = TypedDict(
    "FetchPageRequestTypeDef",
    {
        "TransactionId": str,
        "NextPageToken": str,
    },
)
ValueHolderOutputTypeDef = TypedDict(
    "ValueHolderOutputTypeDef",
    {
        "IonBinary": NotRequired[bytes],
        "IonText": NotRequired[str],
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
StartSessionRequestTypeDef = TypedDict(
    "StartSessionRequestTypeDef",
    {
        "LedgerName": str,
    },
)
AbortTransactionResultTypeDef = TypedDict(
    "AbortTransactionResultTypeDef",
    {
        "TimingInformation": NotRequired[TimingInformationTypeDef],
    },
)
EndSessionResultTypeDef = TypedDict(
    "EndSessionResultTypeDef",
    {
        "TimingInformation": NotRequired[TimingInformationTypeDef],
    },
)
StartSessionResultTypeDef = TypedDict(
    "StartSessionResultTypeDef",
    {
        "SessionToken": NotRequired[str],
        "TimingInformation": NotRequired[TimingInformationTypeDef],
    },
)
StartTransactionResultTypeDef = TypedDict(
    "StartTransactionResultTypeDef",
    {
        "TransactionId": NotRequired[str],
        "TimingInformation": NotRequired[TimingInformationTypeDef],
    },
)
CommitTransactionRequestTypeDef = TypedDict(
    "CommitTransactionRequestTypeDef",
    {
        "TransactionId": str,
        "CommitDigest": BlobTypeDef,
    },
)
ValueHolderTypeDef = TypedDict(
    "ValueHolderTypeDef",
    {
        "IonBinary": NotRequired[BlobTypeDef],
        "IonText": NotRequired[str],
    },
)
CommitTransactionResultTypeDef = TypedDict(
    "CommitTransactionResultTypeDef",
    {
        "TransactionId": NotRequired[str],
        "CommitDigest": NotRequired[bytes],
        "TimingInformation": NotRequired[TimingInformationTypeDef],
        "ConsumedIOs": NotRequired[IOUsageTypeDef],
    },
)
PageTypeDef = TypedDict(
    "PageTypeDef",
    {
        "Values": NotRequired[List[ValueHolderOutputTypeDef]],
        "NextPageToken": NotRequired[str],
    },
)
ValueHolderUnionTypeDef = Union[ValueHolderTypeDef, ValueHolderOutputTypeDef]
ExecuteStatementResultTypeDef = TypedDict(
    "ExecuteStatementResultTypeDef",
    {
        "FirstPage": NotRequired[PageTypeDef],
        "TimingInformation": NotRequired[TimingInformationTypeDef],
        "ConsumedIOs": NotRequired[IOUsageTypeDef],
    },
)
FetchPageResultTypeDef = TypedDict(
    "FetchPageResultTypeDef",
    {
        "Page": NotRequired[PageTypeDef],
        "TimingInformation": NotRequired[TimingInformationTypeDef],
        "ConsumedIOs": NotRequired[IOUsageTypeDef],
    },
)
ExecuteStatementRequestTypeDef = TypedDict(
    "ExecuteStatementRequestTypeDef",
    {
        "TransactionId": str,
        "Statement": str,
        "Parameters": NotRequired[Sequence[ValueHolderUnionTypeDef]],
    },
)
SendCommandResultTypeDef = TypedDict(
    "SendCommandResultTypeDef",
    {
        "StartSession": StartSessionResultTypeDef,
        "StartTransaction": StartTransactionResultTypeDef,
        "EndSession": EndSessionResultTypeDef,
        "CommitTransaction": CommitTransactionResultTypeDef,
        "AbortTransaction": AbortTransactionResultTypeDef,
        "ExecuteStatement": ExecuteStatementResultTypeDef,
        "FetchPage": FetchPageResultTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendCommandRequestRequestTypeDef = TypedDict(
    "SendCommandRequestRequestTypeDef",
    {
        "SessionToken": NotRequired[str],
        "StartSession": NotRequired[StartSessionRequestTypeDef],
        "StartTransaction": NotRequired[Mapping[str, Any]],
        "EndSession": NotRequired[Mapping[str, Any]],
        "CommitTransaction": NotRequired[CommitTransactionRequestTypeDef],
        "AbortTransaction": NotRequired[Mapping[str, Any]],
        "ExecuteStatement": NotRequired[ExecuteStatementRequestTypeDef],
        "FetchPage": NotRequired[FetchPageRequestTypeDef],
    },
)
