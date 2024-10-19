"""
Type annotations for qldb service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qldb/type_defs/)

Usage::

    ```python
    from mypy_boto3_qldb.type_defs import CancelJournalKinesisStreamRequestRequestTypeDef

    data: CancelJournalKinesisStreamRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    EncryptionStatusType,
    ErrorCauseType,
    ExportStatusType,
    LedgerStateType,
    OutputFormatType,
    PermissionsModeType,
    S3ObjectEncryptionTypeType,
    StreamStatusType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "CancelJournalKinesisStreamRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CreateLedgerRequestRequestTypeDef",
    "DeleteLedgerRequestRequestTypeDef",
    "DescribeJournalKinesisStreamRequestRequestTypeDef",
    "DescribeJournalS3ExportRequestRequestTypeDef",
    "DescribeLedgerRequestRequestTypeDef",
    "LedgerEncryptionDescriptionTypeDef",
    "TimestampTypeDef",
    "ValueHolderTypeDef",
    "GetDigestRequestRequestTypeDef",
    "KinesisConfigurationTypeDef",
    "LedgerSummaryTypeDef",
    "ListJournalKinesisStreamsForLedgerRequestRequestTypeDef",
    "ListJournalS3ExportsForLedgerRequestRequestTypeDef",
    "ListJournalS3ExportsRequestRequestTypeDef",
    "ListLedgersRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "S3EncryptionConfigurationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateLedgerPermissionsModeRequestRequestTypeDef",
    "UpdateLedgerRequestRequestTypeDef",
    "CancelJournalKinesisStreamResponseTypeDef",
    "CreateLedgerResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ExportJournalToS3ResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StreamJournalToKinesisResponseTypeDef",
    "UpdateLedgerPermissionsModeResponseTypeDef",
    "DescribeLedgerResponseTypeDef",
    "UpdateLedgerResponseTypeDef",
    "GetBlockRequestRequestTypeDef",
    "GetBlockResponseTypeDef",
    "GetDigestResponseTypeDef",
    "GetRevisionRequestRequestTypeDef",
    "GetRevisionResponseTypeDef",
    "JournalKinesisStreamDescriptionTypeDef",
    "StreamJournalToKinesisRequestRequestTypeDef",
    "ListLedgersResponseTypeDef",
    "S3ExportConfigurationTypeDef",
    "DescribeJournalKinesisStreamResponseTypeDef",
    "ListJournalKinesisStreamsForLedgerResponseTypeDef",
    "ExportJournalToS3RequestRequestTypeDef",
    "JournalS3ExportDescriptionTypeDef",
    "DescribeJournalS3ExportResponseTypeDef",
    "ListJournalS3ExportsForLedgerResponseTypeDef",
    "ListJournalS3ExportsResponseTypeDef",
)

CancelJournalKinesisStreamRequestRequestTypeDef = TypedDict(
    "CancelJournalKinesisStreamRequestRequestTypeDef",
    {
        "LedgerName": str,
        "StreamId": str,
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
CreateLedgerRequestRequestTypeDef = TypedDict(
    "CreateLedgerRequestRequestTypeDef",
    {
        "Name": str,
        "PermissionsMode": PermissionsModeType,
        "Tags": NotRequired[Mapping[str, str]],
        "DeletionProtection": NotRequired[bool],
        "KmsKey": NotRequired[str],
    },
)
DeleteLedgerRequestRequestTypeDef = TypedDict(
    "DeleteLedgerRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DescribeJournalKinesisStreamRequestRequestTypeDef = TypedDict(
    "DescribeJournalKinesisStreamRequestRequestTypeDef",
    {
        "LedgerName": str,
        "StreamId": str,
    },
)
DescribeJournalS3ExportRequestRequestTypeDef = TypedDict(
    "DescribeJournalS3ExportRequestRequestTypeDef",
    {
        "Name": str,
        "ExportId": str,
    },
)
DescribeLedgerRequestRequestTypeDef = TypedDict(
    "DescribeLedgerRequestRequestTypeDef",
    {
        "Name": str,
    },
)
LedgerEncryptionDescriptionTypeDef = TypedDict(
    "LedgerEncryptionDescriptionTypeDef",
    {
        "KmsKeyArn": str,
        "EncryptionStatus": EncryptionStatusType,
        "InaccessibleKmsKeyDateTime": NotRequired[datetime],
    },
)
TimestampTypeDef = Union[datetime, str]
ValueHolderTypeDef = TypedDict(
    "ValueHolderTypeDef",
    {
        "IonText": NotRequired[str],
    },
)
GetDigestRequestRequestTypeDef = TypedDict(
    "GetDigestRequestRequestTypeDef",
    {
        "Name": str,
    },
)
KinesisConfigurationTypeDef = TypedDict(
    "KinesisConfigurationTypeDef",
    {
        "StreamArn": str,
        "AggregationEnabled": NotRequired[bool],
    },
)
LedgerSummaryTypeDef = TypedDict(
    "LedgerSummaryTypeDef",
    {
        "Name": NotRequired[str],
        "State": NotRequired[LedgerStateType],
        "CreationDateTime": NotRequired[datetime],
    },
)
ListJournalKinesisStreamsForLedgerRequestRequestTypeDef = TypedDict(
    "ListJournalKinesisStreamsForLedgerRequestRequestTypeDef",
    {
        "LedgerName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListJournalS3ExportsForLedgerRequestRequestTypeDef = TypedDict(
    "ListJournalS3ExportsForLedgerRequestRequestTypeDef",
    {
        "Name": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListJournalS3ExportsRequestRequestTypeDef = TypedDict(
    "ListJournalS3ExportsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListLedgersRequestRequestTypeDef = TypedDict(
    "ListLedgersRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
S3EncryptionConfigurationTypeDef = TypedDict(
    "S3EncryptionConfigurationTypeDef",
    {
        "ObjectEncryptionType": S3ObjectEncryptionTypeType,
        "KmsKeyArn": NotRequired[str],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateLedgerPermissionsModeRequestRequestTypeDef = TypedDict(
    "UpdateLedgerPermissionsModeRequestRequestTypeDef",
    {
        "Name": str,
        "PermissionsMode": PermissionsModeType,
    },
)
UpdateLedgerRequestRequestTypeDef = TypedDict(
    "UpdateLedgerRequestRequestTypeDef",
    {
        "Name": str,
        "DeletionProtection": NotRequired[bool],
        "KmsKey": NotRequired[str],
    },
)
CancelJournalKinesisStreamResponseTypeDef = TypedDict(
    "CancelJournalKinesisStreamResponseTypeDef",
    {
        "StreamId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateLedgerResponseTypeDef = TypedDict(
    "CreateLedgerResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "State": LedgerStateType,
        "CreationDateTime": datetime,
        "PermissionsMode": PermissionsModeType,
        "DeletionProtection": bool,
        "KmsKeyArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportJournalToS3ResponseTypeDef = TypedDict(
    "ExportJournalToS3ResponseTypeDef",
    {
        "ExportId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StreamJournalToKinesisResponseTypeDef = TypedDict(
    "StreamJournalToKinesisResponseTypeDef",
    {
        "StreamId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateLedgerPermissionsModeResponseTypeDef = TypedDict(
    "UpdateLedgerPermissionsModeResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "PermissionsMode": PermissionsModeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeLedgerResponseTypeDef = TypedDict(
    "DescribeLedgerResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "State": LedgerStateType,
        "CreationDateTime": datetime,
        "PermissionsMode": PermissionsModeType,
        "DeletionProtection": bool,
        "EncryptionDescription": LedgerEncryptionDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateLedgerResponseTypeDef = TypedDict(
    "UpdateLedgerResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "State": LedgerStateType,
        "CreationDateTime": datetime,
        "DeletionProtection": bool,
        "EncryptionDescription": LedgerEncryptionDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBlockRequestRequestTypeDef = TypedDict(
    "GetBlockRequestRequestTypeDef",
    {
        "Name": str,
        "BlockAddress": ValueHolderTypeDef,
        "DigestTipAddress": NotRequired[ValueHolderTypeDef],
    },
)
GetBlockResponseTypeDef = TypedDict(
    "GetBlockResponseTypeDef",
    {
        "Block": ValueHolderTypeDef,
        "Proof": ValueHolderTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDigestResponseTypeDef = TypedDict(
    "GetDigestResponseTypeDef",
    {
        "Digest": bytes,
        "DigestTipAddress": ValueHolderTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRevisionRequestRequestTypeDef = TypedDict(
    "GetRevisionRequestRequestTypeDef",
    {
        "Name": str,
        "BlockAddress": ValueHolderTypeDef,
        "DocumentId": str,
        "DigestTipAddress": NotRequired[ValueHolderTypeDef],
    },
)
GetRevisionResponseTypeDef = TypedDict(
    "GetRevisionResponseTypeDef",
    {
        "Proof": ValueHolderTypeDef,
        "Revision": ValueHolderTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
JournalKinesisStreamDescriptionTypeDef = TypedDict(
    "JournalKinesisStreamDescriptionTypeDef",
    {
        "LedgerName": str,
        "RoleArn": str,
        "StreamId": str,
        "Status": StreamStatusType,
        "KinesisConfiguration": KinesisConfigurationTypeDef,
        "StreamName": str,
        "CreationTime": NotRequired[datetime],
        "InclusiveStartTime": NotRequired[datetime],
        "ExclusiveEndTime": NotRequired[datetime],
        "Arn": NotRequired[str],
        "ErrorCause": NotRequired[ErrorCauseType],
    },
)
StreamJournalToKinesisRequestRequestTypeDef = TypedDict(
    "StreamJournalToKinesisRequestRequestTypeDef",
    {
        "LedgerName": str,
        "RoleArn": str,
        "InclusiveStartTime": TimestampTypeDef,
        "KinesisConfiguration": KinesisConfigurationTypeDef,
        "StreamName": str,
        "Tags": NotRequired[Mapping[str, str]],
        "ExclusiveEndTime": NotRequired[TimestampTypeDef],
    },
)
ListLedgersResponseTypeDef = TypedDict(
    "ListLedgersResponseTypeDef",
    {
        "Ledgers": List[LedgerSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
S3ExportConfigurationTypeDef = TypedDict(
    "S3ExportConfigurationTypeDef",
    {
        "Bucket": str,
        "Prefix": str,
        "EncryptionConfiguration": S3EncryptionConfigurationTypeDef,
    },
)
DescribeJournalKinesisStreamResponseTypeDef = TypedDict(
    "DescribeJournalKinesisStreamResponseTypeDef",
    {
        "Stream": JournalKinesisStreamDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListJournalKinesisStreamsForLedgerResponseTypeDef = TypedDict(
    "ListJournalKinesisStreamsForLedgerResponseTypeDef",
    {
        "Streams": List[JournalKinesisStreamDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ExportJournalToS3RequestRequestTypeDef = TypedDict(
    "ExportJournalToS3RequestRequestTypeDef",
    {
        "Name": str,
        "InclusiveStartTime": TimestampTypeDef,
        "ExclusiveEndTime": TimestampTypeDef,
        "S3ExportConfiguration": S3ExportConfigurationTypeDef,
        "RoleArn": str,
        "OutputFormat": NotRequired[OutputFormatType],
    },
)
JournalS3ExportDescriptionTypeDef = TypedDict(
    "JournalS3ExportDescriptionTypeDef",
    {
        "LedgerName": str,
        "ExportId": str,
        "ExportCreationTime": datetime,
        "Status": ExportStatusType,
        "InclusiveStartTime": datetime,
        "ExclusiveEndTime": datetime,
        "S3ExportConfiguration": S3ExportConfigurationTypeDef,
        "RoleArn": str,
        "OutputFormat": NotRequired[OutputFormatType],
    },
)
DescribeJournalS3ExportResponseTypeDef = TypedDict(
    "DescribeJournalS3ExportResponseTypeDef",
    {
        "ExportDescription": JournalS3ExportDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListJournalS3ExportsForLedgerResponseTypeDef = TypedDict(
    "ListJournalS3ExportsForLedgerResponseTypeDef",
    {
        "JournalS3Exports": List[JournalS3ExportDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListJournalS3ExportsResponseTypeDef = TypedDict(
    "ListJournalS3ExportsResponseTypeDef",
    {
        "JournalS3Exports": List[JournalS3ExportDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
