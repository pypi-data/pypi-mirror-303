"""
Type annotations for connectparticipant service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectparticipant/type_defs/)

Usage::

    ```python
    from mypy_boto3_connectparticipant.type_defs import AttachmentItemTypeDef

    data: AttachmentItemTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Sequence

from .literals import (
    ArtifactStatusType,
    ChatItemTypeType,
    ConnectionTypeType,
    ParticipantRoleType,
    ScanDirectionType,
    SortKeyType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "AttachmentItemTypeDef",
    "CompleteAttachmentUploadRequestRequestTypeDef",
    "ConnectionCredentialsTypeDef",
    "CreateParticipantConnectionRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "WebsocketTypeDef",
    "DescribeViewRequestRequestTypeDef",
    "DisconnectParticipantRequestRequestTypeDef",
    "GetAttachmentRequestRequestTypeDef",
    "StartPositionTypeDef",
    "ReceiptTypeDef",
    "SendEventRequestRequestTypeDef",
    "SendMessageRequestRequestTypeDef",
    "StartAttachmentUploadRequestRequestTypeDef",
    "UploadMetadataTypeDef",
    "ViewContentTypeDef",
    "GetAttachmentResponseTypeDef",
    "SendEventResponseTypeDef",
    "SendMessageResponseTypeDef",
    "CreateParticipantConnectionResponseTypeDef",
    "GetTranscriptRequestRequestTypeDef",
    "MessageMetadataTypeDef",
    "StartAttachmentUploadResponseTypeDef",
    "ViewTypeDef",
    "ItemTypeDef",
    "DescribeViewResponseTypeDef",
    "GetTranscriptResponseTypeDef",
)

AttachmentItemTypeDef = TypedDict(
    "AttachmentItemTypeDef",
    {
        "ContentType": NotRequired[str],
        "AttachmentId": NotRequired[str],
        "AttachmentName": NotRequired[str],
        "Status": NotRequired[ArtifactStatusType],
    },
)
CompleteAttachmentUploadRequestRequestTypeDef = TypedDict(
    "CompleteAttachmentUploadRequestRequestTypeDef",
    {
        "AttachmentIds": Sequence[str],
        "ClientToken": str,
        "ConnectionToken": str,
    },
)
ConnectionCredentialsTypeDef = TypedDict(
    "ConnectionCredentialsTypeDef",
    {
        "ConnectionToken": NotRequired[str],
        "Expiry": NotRequired[str],
    },
)
CreateParticipantConnectionRequestRequestTypeDef = TypedDict(
    "CreateParticipantConnectionRequestRequestTypeDef",
    {
        "ParticipantToken": str,
        "Type": NotRequired[Sequence[ConnectionTypeType]],
        "ConnectParticipant": NotRequired[bool],
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
WebsocketTypeDef = TypedDict(
    "WebsocketTypeDef",
    {
        "Url": NotRequired[str],
        "ConnectionExpiry": NotRequired[str],
    },
)
DescribeViewRequestRequestTypeDef = TypedDict(
    "DescribeViewRequestRequestTypeDef",
    {
        "ViewToken": str,
        "ConnectionToken": str,
    },
)
DisconnectParticipantRequestRequestTypeDef = TypedDict(
    "DisconnectParticipantRequestRequestTypeDef",
    {
        "ConnectionToken": str,
        "ClientToken": NotRequired[str],
    },
)
GetAttachmentRequestRequestTypeDef = TypedDict(
    "GetAttachmentRequestRequestTypeDef",
    {
        "AttachmentId": str,
        "ConnectionToken": str,
    },
)
StartPositionTypeDef = TypedDict(
    "StartPositionTypeDef",
    {
        "Id": NotRequired[str],
        "AbsoluteTime": NotRequired[str],
        "MostRecent": NotRequired[int],
    },
)
ReceiptTypeDef = TypedDict(
    "ReceiptTypeDef",
    {
        "DeliveredTimestamp": NotRequired[str],
        "ReadTimestamp": NotRequired[str],
        "RecipientParticipantId": NotRequired[str],
    },
)
SendEventRequestRequestTypeDef = TypedDict(
    "SendEventRequestRequestTypeDef",
    {
        "ContentType": str,
        "ConnectionToken": str,
        "Content": NotRequired[str],
        "ClientToken": NotRequired[str],
    },
)
SendMessageRequestRequestTypeDef = TypedDict(
    "SendMessageRequestRequestTypeDef",
    {
        "ContentType": str,
        "Content": str,
        "ConnectionToken": str,
        "ClientToken": NotRequired[str],
    },
)
StartAttachmentUploadRequestRequestTypeDef = TypedDict(
    "StartAttachmentUploadRequestRequestTypeDef",
    {
        "ContentType": str,
        "AttachmentSizeInBytes": int,
        "AttachmentName": str,
        "ClientToken": str,
        "ConnectionToken": str,
    },
)
UploadMetadataTypeDef = TypedDict(
    "UploadMetadataTypeDef",
    {
        "Url": NotRequired[str],
        "UrlExpiry": NotRequired[str],
        "HeadersToInclude": NotRequired[Dict[str, str]],
    },
)
ViewContentTypeDef = TypedDict(
    "ViewContentTypeDef",
    {
        "InputSchema": NotRequired[str],
        "Template": NotRequired[str],
        "Actions": NotRequired[List[str]],
    },
)
GetAttachmentResponseTypeDef = TypedDict(
    "GetAttachmentResponseTypeDef",
    {
        "Url": str,
        "UrlExpiry": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendEventResponseTypeDef = TypedDict(
    "SendEventResponseTypeDef",
    {
        "Id": str,
        "AbsoluteTime": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendMessageResponseTypeDef = TypedDict(
    "SendMessageResponseTypeDef",
    {
        "Id": str,
        "AbsoluteTime": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateParticipantConnectionResponseTypeDef = TypedDict(
    "CreateParticipantConnectionResponseTypeDef",
    {
        "Websocket": WebsocketTypeDef,
        "ConnectionCredentials": ConnectionCredentialsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTranscriptRequestRequestTypeDef = TypedDict(
    "GetTranscriptRequestRequestTypeDef",
    {
        "ConnectionToken": str,
        "ContactId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ScanDirection": NotRequired[ScanDirectionType],
        "SortOrder": NotRequired[SortKeyType],
        "StartPosition": NotRequired[StartPositionTypeDef],
    },
)
MessageMetadataTypeDef = TypedDict(
    "MessageMetadataTypeDef",
    {
        "MessageId": NotRequired[str],
        "Receipts": NotRequired[List[ReceiptTypeDef]],
    },
)
StartAttachmentUploadResponseTypeDef = TypedDict(
    "StartAttachmentUploadResponseTypeDef",
    {
        "AttachmentId": str,
        "UploadMetadata": UploadMetadataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ViewTypeDef = TypedDict(
    "ViewTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Version": NotRequired[int],
        "Content": NotRequired[ViewContentTypeDef],
    },
)
ItemTypeDef = TypedDict(
    "ItemTypeDef",
    {
        "AbsoluteTime": NotRequired[str],
        "Content": NotRequired[str],
        "ContentType": NotRequired[str],
        "Id": NotRequired[str],
        "Type": NotRequired[ChatItemTypeType],
        "ParticipantId": NotRequired[str],
        "DisplayName": NotRequired[str],
        "ParticipantRole": NotRequired[ParticipantRoleType],
        "Attachments": NotRequired[List[AttachmentItemTypeDef]],
        "MessageMetadata": NotRequired[MessageMetadataTypeDef],
        "RelatedContactId": NotRequired[str],
        "ContactId": NotRequired[str],
    },
)
DescribeViewResponseTypeDef = TypedDict(
    "DescribeViewResponseTypeDef",
    {
        "View": ViewTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTranscriptResponseTypeDef = TypedDict(
    "GetTranscriptResponseTypeDef",
    {
        "InitialContactId": str,
        "Transcript": List[ItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
