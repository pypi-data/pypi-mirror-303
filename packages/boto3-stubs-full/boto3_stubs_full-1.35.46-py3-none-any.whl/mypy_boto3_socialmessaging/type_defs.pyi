"""
Type annotations for socialmessaging service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_socialmessaging/type_defs/)

Usage::

    ```python
    from mypy_boto3_socialmessaging.type_defs import WhatsAppSignupCallbackTypeDef

    data: WhatsAppSignupCallbackTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import RegistrationStatusType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "WhatsAppSignupCallbackTypeDef",
    "ResponseMetadataTypeDef",
    "BlobTypeDef",
    "DeleteWhatsAppMessageMediaInputRequestTypeDef",
    "DisassociateWhatsAppBusinessAccountInputRequestTypeDef",
    "GetLinkedWhatsAppBusinessAccountInputRequestTypeDef",
    "GetLinkedWhatsAppBusinessAccountPhoneNumberInputRequestTypeDef",
    "WhatsAppPhoneNumberDetailTypeDef",
    "S3FileTypeDef",
    "S3PresignedUrlTypeDef",
    "WhatsAppBusinessAccountEventDestinationTypeDef",
    "WhatsAppPhoneNumberSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "ListLinkedWhatsAppBusinessAccountsInputRequestTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "TagTypeDef",
    "UntagResourceInputRequestTypeDef",
    "DeleteWhatsAppMessageMediaOutputTypeDef",
    "GetWhatsAppMessageMediaOutputTypeDef",
    "PostWhatsAppMessageMediaOutputTypeDef",
    "SendWhatsAppMessageOutputTypeDef",
    "TagResourceOutputTypeDef",
    "UntagResourceOutputTypeDef",
    "SendWhatsAppMessageInputRequestTypeDef",
    "GetLinkedWhatsAppBusinessAccountPhoneNumberOutputTypeDef",
    "LinkedWhatsAppBusinessAccountIdMetaDataTypeDef",
    "GetWhatsAppMessageMediaInputRequestTypeDef",
    "PostWhatsAppMessageMediaInputRequestTypeDef",
    "LinkedWhatsAppBusinessAccountSummaryTypeDef",
    "PutWhatsAppBusinessAccountEventDestinationsInputRequestTypeDef",
    "LinkedWhatsAppBusinessAccountTypeDef",
    "ListLinkedWhatsAppBusinessAccountsInputListLinkedWhatsAppBusinessAccountsPaginateTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "TagResourceInputRequestTypeDef",
    "WabaPhoneNumberSetupFinalizationTypeDef",
    "WabaSetupFinalizationTypeDef",
    "WhatsAppSignupCallbackResultTypeDef",
    "ListLinkedWhatsAppBusinessAccountsOutputTypeDef",
    "GetLinkedWhatsAppBusinessAccountOutputTypeDef",
    "WhatsAppSetupFinalizationTypeDef",
    "AssociateWhatsAppBusinessAccountOutputTypeDef",
    "AssociateWhatsAppBusinessAccountInputRequestTypeDef",
)

WhatsAppSignupCallbackTypeDef = TypedDict(
    "WhatsAppSignupCallbackTypeDef",
    {
        "accessToken": str,
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
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
DeleteWhatsAppMessageMediaInputRequestTypeDef = TypedDict(
    "DeleteWhatsAppMessageMediaInputRequestTypeDef",
    {
        "mediaId": str,
        "originationPhoneNumberId": str,
    },
)
DisassociateWhatsAppBusinessAccountInputRequestTypeDef = TypedDict(
    "DisassociateWhatsAppBusinessAccountInputRequestTypeDef",
    {
        "id": str,
    },
)
GetLinkedWhatsAppBusinessAccountInputRequestTypeDef = TypedDict(
    "GetLinkedWhatsAppBusinessAccountInputRequestTypeDef",
    {
        "id": str,
    },
)
GetLinkedWhatsAppBusinessAccountPhoneNumberInputRequestTypeDef = TypedDict(
    "GetLinkedWhatsAppBusinessAccountPhoneNumberInputRequestTypeDef",
    {
        "id": str,
    },
)
WhatsAppPhoneNumberDetailTypeDef = TypedDict(
    "WhatsAppPhoneNumberDetailTypeDef",
    {
        "arn": str,
        "phoneNumber": str,
        "phoneNumberId": str,
        "metaPhoneNumberId": str,
        "displayPhoneNumberName": str,
        "displayPhoneNumber": str,
        "qualityRating": str,
    },
)
S3FileTypeDef = TypedDict(
    "S3FileTypeDef",
    {
        "bucketName": str,
        "key": str,
    },
)
S3PresignedUrlTypeDef = TypedDict(
    "S3PresignedUrlTypeDef",
    {
        "url": str,
        "headers": Mapping[str, str],
    },
)
WhatsAppBusinessAccountEventDestinationTypeDef = TypedDict(
    "WhatsAppBusinessAccountEventDestinationTypeDef",
    {
        "eventDestinationArn": str,
    },
)
WhatsAppPhoneNumberSummaryTypeDef = TypedDict(
    "WhatsAppPhoneNumberSummaryTypeDef",
    {
        "arn": str,
        "phoneNumber": str,
        "phoneNumberId": str,
        "metaPhoneNumberId": str,
        "displayPhoneNumberName": str,
        "displayPhoneNumber": str,
        "qualityRating": str,
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
ListLinkedWhatsAppBusinessAccountsInputRequestTypeDef = TypedDict(
    "ListLinkedWhatsAppBusinessAccountsInputRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": NotRequired[str],
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
DeleteWhatsAppMessageMediaOutputTypeDef = TypedDict(
    "DeleteWhatsAppMessageMediaOutputTypeDef",
    {
        "success": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetWhatsAppMessageMediaOutputTypeDef = TypedDict(
    "GetWhatsAppMessageMediaOutputTypeDef",
    {
        "mimeType": str,
        "fileSize": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PostWhatsAppMessageMediaOutputTypeDef = TypedDict(
    "PostWhatsAppMessageMediaOutputTypeDef",
    {
        "mediaId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendWhatsAppMessageOutputTypeDef = TypedDict(
    "SendWhatsAppMessageOutputTypeDef",
    {
        "messageId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceOutputTypeDef = TypedDict(
    "TagResourceOutputTypeDef",
    {
        "statusCode": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UntagResourceOutputTypeDef = TypedDict(
    "UntagResourceOutputTypeDef",
    {
        "statusCode": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendWhatsAppMessageInputRequestTypeDef = TypedDict(
    "SendWhatsAppMessageInputRequestTypeDef",
    {
        "originationPhoneNumberId": str,
        "message": BlobTypeDef,
        "metaApiVersion": str,
    },
)
GetLinkedWhatsAppBusinessAccountPhoneNumberOutputTypeDef = TypedDict(
    "GetLinkedWhatsAppBusinessAccountPhoneNumberOutputTypeDef",
    {
        "phoneNumber": WhatsAppPhoneNumberDetailTypeDef,
        "linkedWhatsAppBusinessAccountId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LinkedWhatsAppBusinessAccountIdMetaDataTypeDef = TypedDict(
    "LinkedWhatsAppBusinessAccountIdMetaDataTypeDef",
    {
        "accountName": NotRequired[str],
        "registrationStatus": NotRequired[RegistrationStatusType],
        "unregisteredWhatsAppPhoneNumbers": NotRequired[List[WhatsAppPhoneNumberDetailTypeDef]],
    },
)
GetWhatsAppMessageMediaInputRequestTypeDef = TypedDict(
    "GetWhatsAppMessageMediaInputRequestTypeDef",
    {
        "mediaId": str,
        "originationPhoneNumberId": str,
        "metadataOnly": NotRequired[bool],
        "destinationS3PresignedUrl": NotRequired[S3PresignedUrlTypeDef],
        "destinationS3File": NotRequired[S3FileTypeDef],
    },
)
PostWhatsAppMessageMediaInputRequestTypeDef = TypedDict(
    "PostWhatsAppMessageMediaInputRequestTypeDef",
    {
        "originationPhoneNumberId": str,
        "sourceS3PresignedUrl": NotRequired[S3PresignedUrlTypeDef],
        "sourceS3File": NotRequired[S3FileTypeDef],
    },
)
LinkedWhatsAppBusinessAccountSummaryTypeDef = TypedDict(
    "LinkedWhatsAppBusinessAccountSummaryTypeDef",
    {
        "arn": str,
        "id": str,
        "wabaId": str,
        "registrationStatus": RegistrationStatusType,
        "linkDate": datetime,
        "wabaName": str,
        "eventDestinations": List[WhatsAppBusinessAccountEventDestinationTypeDef],
    },
)
PutWhatsAppBusinessAccountEventDestinationsInputRequestTypeDef = TypedDict(
    "PutWhatsAppBusinessAccountEventDestinationsInputRequestTypeDef",
    {
        "id": str,
        "eventDestinations": Sequence[WhatsAppBusinessAccountEventDestinationTypeDef],
    },
)
LinkedWhatsAppBusinessAccountTypeDef = TypedDict(
    "LinkedWhatsAppBusinessAccountTypeDef",
    {
        "arn": str,
        "id": str,
        "wabaId": str,
        "registrationStatus": RegistrationStatusType,
        "linkDate": datetime,
        "wabaName": str,
        "eventDestinations": List[WhatsAppBusinessAccountEventDestinationTypeDef],
        "phoneNumbers": List[WhatsAppPhoneNumberSummaryTypeDef],
    },
)
ListLinkedWhatsAppBusinessAccountsInputListLinkedWhatsAppBusinessAccountsPaginateTypeDef = (
    TypedDict(
        "ListLinkedWhatsAppBusinessAccountsInputListLinkedWhatsAppBusinessAccountsPaginateTypeDef",
        {
            "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
        },
    )
)
ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "statusCode": int,
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[TagTypeDef],
    },
)
WabaPhoneNumberSetupFinalizationTypeDef = TypedDict(
    "WabaPhoneNumberSetupFinalizationTypeDef",
    {
        "id": str,
        "twoFactorPin": str,
        "dataLocalizationRegion": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
WabaSetupFinalizationTypeDef = TypedDict(
    "WabaSetupFinalizationTypeDef",
    {
        "id": NotRequired[str],
        "eventDestinations": NotRequired[Sequence[WhatsAppBusinessAccountEventDestinationTypeDef]],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
WhatsAppSignupCallbackResultTypeDef = TypedDict(
    "WhatsAppSignupCallbackResultTypeDef",
    {
        "associateInProgressToken": NotRequired[str],
        "linkedAccountsWithIncompleteSetup": NotRequired[
            Dict[str, LinkedWhatsAppBusinessAccountIdMetaDataTypeDef]
        ],
    },
)
ListLinkedWhatsAppBusinessAccountsOutputTypeDef = TypedDict(
    "ListLinkedWhatsAppBusinessAccountsOutputTypeDef",
    {
        "linkedAccounts": List[LinkedWhatsAppBusinessAccountSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLinkedWhatsAppBusinessAccountOutputTypeDef = TypedDict(
    "GetLinkedWhatsAppBusinessAccountOutputTypeDef",
    {
        "account": LinkedWhatsAppBusinessAccountTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
WhatsAppSetupFinalizationTypeDef = TypedDict(
    "WhatsAppSetupFinalizationTypeDef",
    {
        "associateInProgressToken": str,
        "phoneNumbers": Sequence[WabaPhoneNumberSetupFinalizationTypeDef],
        "phoneNumberParent": NotRequired[str],
        "waba": NotRequired[WabaSetupFinalizationTypeDef],
    },
)
AssociateWhatsAppBusinessAccountOutputTypeDef = TypedDict(
    "AssociateWhatsAppBusinessAccountOutputTypeDef",
    {
        "signupCallbackResult": WhatsAppSignupCallbackResultTypeDef,
        "statusCode": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateWhatsAppBusinessAccountInputRequestTypeDef = TypedDict(
    "AssociateWhatsAppBusinessAccountInputRequestTypeDef",
    {
        "signupCallback": NotRequired[WhatsAppSignupCallbackTypeDef],
        "setupFinalization": NotRequired[WhatsAppSetupFinalizationTypeDef],
    },
)
