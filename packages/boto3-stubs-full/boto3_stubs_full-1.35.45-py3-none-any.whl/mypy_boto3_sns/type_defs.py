"""
Type annotations for sns service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sns/type_defs/)

Usage::

    ```python
    from mypy_boto3_sns.type_defs import AddPermissionInputRequestTypeDef

    data: AddPermissionInputRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    LanguageCodeStringType,
    NumberCapabilityType,
    RouteTypeType,
    SMSSandboxPhoneNumberVerificationStatusType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "AddPermissionInputRequestTypeDef",
    "AddPermissionInputTopicAddPermissionTypeDef",
    "BatchResultErrorEntryTypeDef",
    "BlobTypeDef",
    "CheckIfPhoneNumberIsOptedOutInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "ConfirmSubscriptionInputRequestTypeDef",
    "ConfirmSubscriptionInputTopicConfirmSubscriptionTypeDef",
    "CreatePlatformApplicationInputRequestTypeDef",
    "CreatePlatformApplicationInputServiceResourceCreatePlatformApplicationTypeDef",
    "CreatePlatformEndpointInputPlatformApplicationCreatePlatformEndpointTypeDef",
    "CreatePlatformEndpointInputRequestTypeDef",
    "CreateSMSSandboxPhoneNumberInputRequestTypeDef",
    "TagTypeDef",
    "DeleteEndpointInputRequestTypeDef",
    "DeletePlatformApplicationInputRequestTypeDef",
    "DeleteSMSSandboxPhoneNumberInputRequestTypeDef",
    "DeleteTopicInputRequestTypeDef",
    "EndpointTypeDef",
    "GetDataProtectionPolicyInputRequestTypeDef",
    "GetEndpointAttributesInputRequestTypeDef",
    "GetPlatformApplicationAttributesInputRequestTypeDef",
    "GetSMSAttributesInputRequestTypeDef",
    "GetSubscriptionAttributesInputRequestTypeDef",
    "GetTopicAttributesInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListEndpointsByPlatformApplicationInputRequestTypeDef",
    "ListOriginationNumbersRequestRequestTypeDef",
    "PhoneNumberInformationTypeDef",
    "ListPhoneNumbersOptedOutInputRequestTypeDef",
    "ListPlatformApplicationsInputRequestTypeDef",
    "PlatformApplicationTypeDef",
    "ListSMSSandboxPhoneNumbersInputRequestTypeDef",
    "SMSSandboxPhoneNumberTypeDef",
    "ListSubscriptionsByTopicInputRequestTypeDef",
    "SubscriptionTypeDef",
    "ListSubscriptionsInputRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTopicsInputRequestTypeDef",
    "TopicTypeDef",
    "OptInPhoneNumberInputRequestTypeDef",
    "PublishBatchResultEntryTypeDef",
    "PutDataProtectionPolicyInputRequestTypeDef",
    "RemovePermissionInputRequestTypeDef",
    "RemovePermissionInputTopicRemovePermissionTypeDef",
    "SetEndpointAttributesInputPlatformEndpointSetAttributesTypeDef",
    "SetEndpointAttributesInputRequestTypeDef",
    "SetPlatformApplicationAttributesInputPlatformApplicationSetAttributesTypeDef",
    "SetPlatformApplicationAttributesInputRequestTypeDef",
    "SetSMSAttributesInputRequestTypeDef",
    "SetSubscriptionAttributesInputRequestTypeDef",
    "SetSubscriptionAttributesInputSubscriptionSetAttributesTypeDef",
    "SetTopicAttributesInputRequestTypeDef",
    "SetTopicAttributesInputTopicSetAttributesTypeDef",
    "SubscribeInputRequestTypeDef",
    "SubscribeInputTopicSubscribeTypeDef",
    "UnsubscribeInputRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "VerifySMSSandboxPhoneNumberInputRequestTypeDef",
    "MessageAttributeValueTypeDef",
    "CheckIfPhoneNumberIsOptedOutResponseTypeDef",
    "ConfirmSubscriptionResponseTypeDef",
    "CreateEndpointResponseTypeDef",
    "CreatePlatformApplicationResponseTypeDef",
    "CreateTopicResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetDataProtectionPolicyResponseTypeDef",
    "GetEndpointAttributesResponseTypeDef",
    "GetPlatformApplicationAttributesResponseTypeDef",
    "GetSMSAttributesResponseTypeDef",
    "GetSMSSandboxAccountStatusResultTypeDef",
    "GetSubscriptionAttributesResponseTypeDef",
    "GetTopicAttributesResponseTypeDef",
    "ListPhoneNumbersOptedOutResponseTypeDef",
    "PublishResponseTypeDef",
    "SubscribeResponseTypeDef",
    "CreateTopicInputRequestTypeDef",
    "CreateTopicInputServiceResourceCreateTopicTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "ListEndpointsByPlatformApplicationResponseTypeDef",
    "ListEndpointsByPlatformApplicationInputListEndpointsByPlatformApplicationPaginateTypeDef",
    "ListOriginationNumbersRequestListOriginationNumbersPaginateTypeDef",
    "ListPhoneNumbersOptedOutInputListPhoneNumbersOptedOutPaginateTypeDef",
    "ListPlatformApplicationsInputListPlatformApplicationsPaginateTypeDef",
    "ListSMSSandboxPhoneNumbersInputListSMSSandboxPhoneNumbersPaginateTypeDef",
    "ListSubscriptionsByTopicInputListSubscriptionsByTopicPaginateTypeDef",
    "ListSubscriptionsInputListSubscriptionsPaginateTypeDef",
    "ListTopicsInputListTopicsPaginateTypeDef",
    "ListOriginationNumbersResultTypeDef",
    "ListPlatformApplicationsResponseTypeDef",
    "ListSMSSandboxPhoneNumbersResultTypeDef",
    "ListSubscriptionsByTopicResponseTypeDef",
    "ListSubscriptionsResponseTypeDef",
    "ListTopicsResponseTypeDef",
    "PublishBatchResponseTypeDef",
    "PublishBatchRequestEntryTypeDef",
    "PublishInputPlatformEndpointPublishTypeDef",
    "PublishInputRequestTypeDef",
    "PublishInputTopicPublishTypeDef",
    "PublishBatchInputRequestTypeDef",
)

AddPermissionInputRequestTypeDef = TypedDict(
    "AddPermissionInputRequestTypeDef",
    {
        "TopicArn": str,
        "Label": str,
        "AWSAccountId": Sequence[str],
        "ActionName": Sequence[str],
    },
)
AddPermissionInputTopicAddPermissionTypeDef = TypedDict(
    "AddPermissionInputTopicAddPermissionTypeDef",
    {
        "Label": str,
        "AWSAccountId": Sequence[str],
        "ActionName": Sequence[str],
    },
)
BatchResultErrorEntryTypeDef = TypedDict(
    "BatchResultErrorEntryTypeDef",
    {
        "Id": str,
        "Code": str,
        "SenderFault": bool,
        "Message": NotRequired[str],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
CheckIfPhoneNumberIsOptedOutInputRequestTypeDef = TypedDict(
    "CheckIfPhoneNumberIsOptedOutInputRequestTypeDef",
    {
        "phoneNumber": str,
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
ConfirmSubscriptionInputRequestTypeDef = TypedDict(
    "ConfirmSubscriptionInputRequestTypeDef",
    {
        "TopicArn": str,
        "Token": str,
        "AuthenticateOnUnsubscribe": NotRequired[str],
    },
)
ConfirmSubscriptionInputTopicConfirmSubscriptionTypeDef = TypedDict(
    "ConfirmSubscriptionInputTopicConfirmSubscriptionTypeDef",
    {
        "Token": str,
        "AuthenticateOnUnsubscribe": NotRequired[str],
    },
)
CreatePlatformApplicationInputRequestTypeDef = TypedDict(
    "CreatePlatformApplicationInputRequestTypeDef",
    {
        "Name": str,
        "Platform": str,
        "Attributes": Mapping[str, str],
    },
)
CreatePlatformApplicationInputServiceResourceCreatePlatformApplicationTypeDef = TypedDict(
    "CreatePlatformApplicationInputServiceResourceCreatePlatformApplicationTypeDef",
    {
        "Name": str,
        "Platform": str,
        "Attributes": Mapping[str, str],
    },
)
CreatePlatformEndpointInputPlatformApplicationCreatePlatformEndpointTypeDef = TypedDict(
    "CreatePlatformEndpointInputPlatformApplicationCreatePlatformEndpointTypeDef",
    {
        "Token": str,
        "CustomUserData": NotRequired[str],
        "Attributes": NotRequired[Mapping[str, str]],
    },
)
CreatePlatformEndpointInputRequestTypeDef = TypedDict(
    "CreatePlatformEndpointInputRequestTypeDef",
    {
        "PlatformApplicationArn": str,
        "Token": str,
        "CustomUserData": NotRequired[str],
        "Attributes": NotRequired[Mapping[str, str]],
    },
)
CreateSMSSandboxPhoneNumberInputRequestTypeDef = TypedDict(
    "CreateSMSSandboxPhoneNumberInputRequestTypeDef",
    {
        "PhoneNumber": str,
        "LanguageCode": NotRequired[LanguageCodeStringType],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
DeleteEndpointInputRequestTypeDef = TypedDict(
    "DeleteEndpointInputRequestTypeDef",
    {
        "EndpointArn": str,
    },
)
DeletePlatformApplicationInputRequestTypeDef = TypedDict(
    "DeletePlatformApplicationInputRequestTypeDef",
    {
        "PlatformApplicationArn": str,
    },
)
DeleteSMSSandboxPhoneNumberInputRequestTypeDef = TypedDict(
    "DeleteSMSSandboxPhoneNumberInputRequestTypeDef",
    {
        "PhoneNumber": str,
    },
)
DeleteTopicInputRequestTypeDef = TypedDict(
    "DeleteTopicInputRequestTypeDef",
    {
        "TopicArn": str,
    },
)
EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "EndpointArn": NotRequired[str],
        "Attributes": NotRequired[Dict[str, str]],
    },
)
GetDataProtectionPolicyInputRequestTypeDef = TypedDict(
    "GetDataProtectionPolicyInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
GetEndpointAttributesInputRequestTypeDef = TypedDict(
    "GetEndpointAttributesInputRequestTypeDef",
    {
        "EndpointArn": str,
    },
)
GetPlatformApplicationAttributesInputRequestTypeDef = TypedDict(
    "GetPlatformApplicationAttributesInputRequestTypeDef",
    {
        "PlatformApplicationArn": str,
    },
)
GetSMSAttributesInputRequestTypeDef = TypedDict(
    "GetSMSAttributesInputRequestTypeDef",
    {
        "attributes": NotRequired[Sequence[str]],
    },
)
GetSubscriptionAttributesInputRequestTypeDef = TypedDict(
    "GetSubscriptionAttributesInputRequestTypeDef",
    {
        "SubscriptionArn": str,
    },
)
GetTopicAttributesInputRequestTypeDef = TypedDict(
    "GetTopicAttributesInputRequestTypeDef",
    {
        "TopicArn": str,
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
ListEndpointsByPlatformApplicationInputRequestTypeDef = TypedDict(
    "ListEndpointsByPlatformApplicationInputRequestTypeDef",
    {
        "PlatformApplicationArn": str,
        "NextToken": NotRequired[str],
    },
)
ListOriginationNumbersRequestRequestTypeDef = TypedDict(
    "ListOriginationNumbersRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
PhoneNumberInformationTypeDef = TypedDict(
    "PhoneNumberInformationTypeDef",
    {
        "CreatedAt": NotRequired[datetime],
        "PhoneNumber": NotRequired[str],
        "Status": NotRequired[str],
        "Iso2CountryCode": NotRequired[str],
        "RouteType": NotRequired[RouteTypeType],
        "NumberCapabilities": NotRequired[List[NumberCapabilityType]],
    },
)
ListPhoneNumbersOptedOutInputRequestTypeDef = TypedDict(
    "ListPhoneNumbersOptedOutInputRequestTypeDef",
    {
        "nextToken": NotRequired[str],
    },
)
ListPlatformApplicationsInputRequestTypeDef = TypedDict(
    "ListPlatformApplicationsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)
PlatformApplicationTypeDef = TypedDict(
    "PlatformApplicationTypeDef",
    {
        "PlatformApplicationArn": NotRequired[str],
        "Attributes": NotRequired[Dict[str, str]],
    },
)
ListSMSSandboxPhoneNumbersInputRequestTypeDef = TypedDict(
    "ListSMSSandboxPhoneNumbersInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
SMSSandboxPhoneNumberTypeDef = TypedDict(
    "SMSSandboxPhoneNumberTypeDef",
    {
        "PhoneNumber": NotRequired[str],
        "Status": NotRequired[SMSSandboxPhoneNumberVerificationStatusType],
    },
)
ListSubscriptionsByTopicInputRequestTypeDef = TypedDict(
    "ListSubscriptionsByTopicInputRequestTypeDef",
    {
        "TopicArn": str,
        "NextToken": NotRequired[str],
    },
)
SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
    {
        "SubscriptionArn": NotRequired[str],
        "Owner": NotRequired[str],
        "Protocol": NotRequired[str],
        "Endpoint": NotRequired[str],
        "TopicArn": NotRequired[str],
    },
)
ListSubscriptionsInputRequestTypeDef = TypedDict(
    "ListSubscriptionsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
ListTopicsInputRequestTypeDef = TypedDict(
    "ListTopicsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)
TopicTypeDef = TypedDict(
    "TopicTypeDef",
    {
        "TopicArn": NotRequired[str],
    },
)
OptInPhoneNumberInputRequestTypeDef = TypedDict(
    "OptInPhoneNumberInputRequestTypeDef",
    {
        "phoneNumber": str,
    },
)
PublishBatchResultEntryTypeDef = TypedDict(
    "PublishBatchResultEntryTypeDef",
    {
        "Id": NotRequired[str],
        "MessageId": NotRequired[str],
        "SequenceNumber": NotRequired[str],
    },
)
PutDataProtectionPolicyInputRequestTypeDef = TypedDict(
    "PutDataProtectionPolicyInputRequestTypeDef",
    {
        "ResourceArn": str,
        "DataProtectionPolicy": str,
    },
)
RemovePermissionInputRequestTypeDef = TypedDict(
    "RemovePermissionInputRequestTypeDef",
    {
        "TopicArn": str,
        "Label": str,
    },
)
RemovePermissionInputTopicRemovePermissionTypeDef = TypedDict(
    "RemovePermissionInputTopicRemovePermissionTypeDef",
    {
        "Label": str,
    },
)
SetEndpointAttributesInputPlatformEndpointSetAttributesTypeDef = TypedDict(
    "SetEndpointAttributesInputPlatformEndpointSetAttributesTypeDef",
    {
        "Attributes": Mapping[str, str],
    },
)
SetEndpointAttributesInputRequestTypeDef = TypedDict(
    "SetEndpointAttributesInputRequestTypeDef",
    {
        "EndpointArn": str,
        "Attributes": Mapping[str, str],
    },
)
SetPlatformApplicationAttributesInputPlatformApplicationSetAttributesTypeDef = TypedDict(
    "SetPlatformApplicationAttributesInputPlatformApplicationSetAttributesTypeDef",
    {
        "Attributes": Mapping[str, str],
    },
)
SetPlatformApplicationAttributesInputRequestTypeDef = TypedDict(
    "SetPlatformApplicationAttributesInputRequestTypeDef",
    {
        "PlatformApplicationArn": str,
        "Attributes": Mapping[str, str],
    },
)
SetSMSAttributesInputRequestTypeDef = TypedDict(
    "SetSMSAttributesInputRequestTypeDef",
    {
        "attributes": Mapping[str, str],
    },
)
SetSubscriptionAttributesInputRequestTypeDef = TypedDict(
    "SetSubscriptionAttributesInputRequestTypeDef",
    {
        "SubscriptionArn": str,
        "AttributeName": str,
        "AttributeValue": NotRequired[str],
    },
)
SetSubscriptionAttributesInputSubscriptionSetAttributesTypeDef = TypedDict(
    "SetSubscriptionAttributesInputSubscriptionSetAttributesTypeDef",
    {
        "AttributeName": str,
        "AttributeValue": NotRequired[str],
    },
)
SetTopicAttributesInputRequestTypeDef = TypedDict(
    "SetTopicAttributesInputRequestTypeDef",
    {
        "TopicArn": str,
        "AttributeName": str,
        "AttributeValue": NotRequired[str],
    },
)
SetTopicAttributesInputTopicSetAttributesTypeDef = TypedDict(
    "SetTopicAttributesInputTopicSetAttributesTypeDef",
    {
        "AttributeName": str,
        "AttributeValue": NotRequired[str],
    },
)
SubscribeInputRequestTypeDef = TypedDict(
    "SubscribeInputRequestTypeDef",
    {
        "TopicArn": str,
        "Protocol": str,
        "Endpoint": NotRequired[str],
        "Attributes": NotRequired[Mapping[str, str]],
        "ReturnSubscriptionArn": NotRequired[bool],
    },
)
SubscribeInputTopicSubscribeTypeDef = TypedDict(
    "SubscribeInputTopicSubscribeTypeDef",
    {
        "Protocol": str,
        "Endpoint": NotRequired[str],
        "Attributes": NotRequired[Mapping[str, str]],
        "ReturnSubscriptionArn": NotRequired[bool],
    },
)
UnsubscribeInputRequestTypeDef = TypedDict(
    "UnsubscribeInputRequestTypeDef",
    {
        "SubscriptionArn": str,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
VerifySMSSandboxPhoneNumberInputRequestTypeDef = TypedDict(
    "VerifySMSSandboxPhoneNumberInputRequestTypeDef",
    {
        "PhoneNumber": str,
        "OneTimePassword": str,
    },
)
MessageAttributeValueTypeDef = TypedDict(
    "MessageAttributeValueTypeDef",
    {
        "DataType": str,
        "StringValue": NotRequired[str],
        "BinaryValue": NotRequired[BlobTypeDef],
    },
)
CheckIfPhoneNumberIsOptedOutResponseTypeDef = TypedDict(
    "CheckIfPhoneNumberIsOptedOutResponseTypeDef",
    {
        "isOptedOut": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConfirmSubscriptionResponseTypeDef = TypedDict(
    "ConfirmSubscriptionResponseTypeDef",
    {
        "SubscriptionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEndpointResponseTypeDef = TypedDict(
    "CreateEndpointResponseTypeDef",
    {
        "EndpointArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePlatformApplicationResponseTypeDef = TypedDict(
    "CreatePlatformApplicationResponseTypeDef",
    {
        "PlatformApplicationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTopicResponseTypeDef = TypedDict(
    "CreateTopicResponseTypeDef",
    {
        "TopicArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDataProtectionPolicyResponseTypeDef = TypedDict(
    "GetDataProtectionPolicyResponseTypeDef",
    {
        "DataProtectionPolicy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEndpointAttributesResponseTypeDef = TypedDict(
    "GetEndpointAttributesResponseTypeDef",
    {
        "Attributes": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPlatformApplicationAttributesResponseTypeDef = TypedDict(
    "GetPlatformApplicationAttributesResponseTypeDef",
    {
        "Attributes": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSMSAttributesResponseTypeDef = TypedDict(
    "GetSMSAttributesResponseTypeDef",
    {
        "attributes": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSMSSandboxAccountStatusResultTypeDef = TypedDict(
    "GetSMSSandboxAccountStatusResultTypeDef",
    {
        "IsInSandbox": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSubscriptionAttributesResponseTypeDef = TypedDict(
    "GetSubscriptionAttributesResponseTypeDef",
    {
        "Attributes": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTopicAttributesResponseTypeDef = TypedDict(
    "GetTopicAttributesResponseTypeDef",
    {
        "Attributes": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPhoneNumbersOptedOutResponseTypeDef = TypedDict(
    "ListPhoneNumbersOptedOutResponseTypeDef",
    {
        "phoneNumbers": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PublishResponseTypeDef = TypedDict(
    "PublishResponseTypeDef",
    {
        "MessageId": str,
        "SequenceNumber": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SubscribeResponseTypeDef = TypedDict(
    "SubscribeResponseTypeDef",
    {
        "SubscriptionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTopicInputRequestTypeDef = TypedDict(
    "CreateTopicInputRequestTypeDef",
    {
        "Name": str,
        "Attributes": NotRequired[Mapping[str, str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "DataProtectionPolicy": NotRequired[str],
    },
)
CreateTopicInputServiceResourceCreateTopicTypeDef = TypedDict(
    "CreateTopicInputServiceResourceCreateTopicTypeDef",
    {
        "Name": str,
        "Attributes": NotRequired[Mapping[str, str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "DataProtectionPolicy": NotRequired[str],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
ListEndpointsByPlatformApplicationResponseTypeDef = TypedDict(
    "ListEndpointsByPlatformApplicationResponseTypeDef",
    {
        "Endpoints": List[EndpointTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListEndpointsByPlatformApplicationInputListEndpointsByPlatformApplicationPaginateTypeDef = (
    TypedDict(
        "ListEndpointsByPlatformApplicationInputListEndpointsByPlatformApplicationPaginateTypeDef",
        {
            "PlatformApplicationArn": str,
            "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
        },
    )
)
ListOriginationNumbersRequestListOriginationNumbersPaginateTypeDef = TypedDict(
    "ListOriginationNumbersRequestListOriginationNumbersPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPhoneNumbersOptedOutInputListPhoneNumbersOptedOutPaginateTypeDef = TypedDict(
    "ListPhoneNumbersOptedOutInputListPhoneNumbersOptedOutPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPlatformApplicationsInputListPlatformApplicationsPaginateTypeDef = TypedDict(
    "ListPlatformApplicationsInputListPlatformApplicationsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSMSSandboxPhoneNumbersInputListSMSSandboxPhoneNumbersPaginateTypeDef = TypedDict(
    "ListSMSSandboxPhoneNumbersInputListSMSSandboxPhoneNumbersPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSubscriptionsByTopicInputListSubscriptionsByTopicPaginateTypeDef = TypedDict(
    "ListSubscriptionsByTopicInputListSubscriptionsByTopicPaginateTypeDef",
    {
        "TopicArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSubscriptionsInputListSubscriptionsPaginateTypeDef = TypedDict(
    "ListSubscriptionsInputListSubscriptionsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTopicsInputListTopicsPaginateTypeDef = TypedDict(
    "ListTopicsInputListTopicsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOriginationNumbersResultTypeDef = TypedDict(
    "ListOriginationNumbersResultTypeDef",
    {
        "PhoneNumbers": List[PhoneNumberInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListPlatformApplicationsResponseTypeDef = TypedDict(
    "ListPlatformApplicationsResponseTypeDef",
    {
        "PlatformApplications": List[PlatformApplicationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListSMSSandboxPhoneNumbersResultTypeDef = TypedDict(
    "ListSMSSandboxPhoneNumbersResultTypeDef",
    {
        "PhoneNumbers": List[SMSSandboxPhoneNumberTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListSubscriptionsByTopicResponseTypeDef = TypedDict(
    "ListSubscriptionsByTopicResponseTypeDef",
    {
        "Subscriptions": List[SubscriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListSubscriptionsResponseTypeDef = TypedDict(
    "ListSubscriptionsResponseTypeDef",
    {
        "Subscriptions": List[SubscriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTopicsResponseTypeDef = TypedDict(
    "ListTopicsResponseTypeDef",
    {
        "Topics": List[TopicTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PublishBatchResponseTypeDef = TypedDict(
    "PublishBatchResponseTypeDef",
    {
        "Successful": List[PublishBatchResultEntryTypeDef],
        "Failed": List[BatchResultErrorEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PublishBatchRequestEntryTypeDef = TypedDict(
    "PublishBatchRequestEntryTypeDef",
    {
        "Id": str,
        "Message": str,
        "Subject": NotRequired[str],
        "MessageStructure": NotRequired[str],
        "MessageAttributes": NotRequired[Mapping[str, MessageAttributeValueTypeDef]],
        "MessageDeduplicationId": NotRequired[str],
        "MessageGroupId": NotRequired[str],
    },
)
PublishInputPlatformEndpointPublishTypeDef = TypedDict(
    "PublishInputPlatformEndpointPublishTypeDef",
    {
        "Message": str,
        "TopicArn": NotRequired[str],
        "PhoneNumber": NotRequired[str],
        "Subject": NotRequired[str],
        "MessageStructure": NotRequired[str],
        "MessageAttributes": NotRequired[Mapping[str, MessageAttributeValueTypeDef]],
        "MessageDeduplicationId": NotRequired[str],
        "MessageGroupId": NotRequired[str],
    },
)
PublishInputRequestTypeDef = TypedDict(
    "PublishInputRequestTypeDef",
    {
        "Message": str,
        "TopicArn": NotRequired[str],
        "TargetArn": NotRequired[str],
        "PhoneNumber": NotRequired[str],
        "Subject": NotRequired[str],
        "MessageStructure": NotRequired[str],
        "MessageAttributes": NotRequired[Mapping[str, MessageAttributeValueTypeDef]],
        "MessageDeduplicationId": NotRequired[str],
        "MessageGroupId": NotRequired[str],
    },
)
PublishInputTopicPublishTypeDef = TypedDict(
    "PublishInputTopicPublishTypeDef",
    {
        "Message": str,
        "TargetArn": NotRequired[str],
        "PhoneNumber": NotRequired[str],
        "Subject": NotRequired[str],
        "MessageStructure": NotRequired[str],
        "MessageAttributes": NotRequired[Mapping[str, MessageAttributeValueTypeDef]],
        "MessageDeduplicationId": NotRequired[str],
        "MessageGroupId": NotRequired[str],
    },
)
PublishBatchInputRequestTypeDef = TypedDict(
    "PublishBatchInputRequestTypeDef",
    {
        "TopicArn": str,
        "PublishBatchRequestEntries": Sequence[PublishBatchRequestEntryTypeDef],
    },
)
