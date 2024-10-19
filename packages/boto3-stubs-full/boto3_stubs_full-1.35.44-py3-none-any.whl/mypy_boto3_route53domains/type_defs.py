"""
Type annotations for route53domains service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53domains/type_defs/)

Usage::

    ```python
    from mypy_boto3_route53domains.type_defs import AcceptDomainTransferFromAnotherAwsAccountRequestRequestTypeDef

    data: AcceptDomainTransferFromAnotherAwsAccountRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    ContactTypeType,
    CountryCodeType,
    DomainAvailabilityType,
    ExtraParamNameType,
    ListDomainsAttributeNameType,
    OperationStatusType,
    OperationTypeType,
    OperatorType,
    ReachabilityStatusType,
    SortOrderType,
    StatusFlagType,
    TransferableType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AcceptDomainTransferFromAnotherAwsAccountRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "DnssecSigningAttributesTypeDef",
    "BillingRecordTypeDef",
    "CancelDomainTransferToAnotherAwsAccountRequestRequestTypeDef",
    "CheckDomainAvailabilityRequestRequestTypeDef",
    "CheckDomainTransferabilityRequestRequestTypeDef",
    "DomainTransferabilityTypeDef",
    "ConsentTypeDef",
    "ExtraParamTypeDef",
    "DeleteDomainRequestRequestTypeDef",
    "DeleteTagsForDomainRequestRequestTypeDef",
    "DisableDomainAutoRenewRequestRequestTypeDef",
    "DisableDomainTransferLockRequestRequestTypeDef",
    "DisassociateDelegationSignerFromDomainRequestRequestTypeDef",
    "DnssecKeyTypeDef",
    "PriceWithCurrencyTypeDef",
    "DomainSuggestionTypeDef",
    "DomainSummaryTypeDef",
    "EnableDomainAutoRenewRequestRequestTypeDef",
    "EnableDomainTransferLockRequestRequestTypeDef",
    "FilterConditionTypeDef",
    "GetContactReachabilityStatusRequestRequestTypeDef",
    "GetDomainDetailRequestRequestTypeDef",
    "NameserverOutputTypeDef",
    "GetDomainSuggestionsRequestRequestTypeDef",
    "GetOperationDetailRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "SortConditionTypeDef",
    "TimestampTypeDef",
    "OperationSummaryTypeDef",
    "ListPricesRequestRequestTypeDef",
    "ListTagsForDomainRequestRequestTypeDef",
    "TagTypeDef",
    "NameserverTypeDef",
    "PushDomainRequestRequestTypeDef",
    "RejectDomainTransferFromAnotherAwsAccountRequestRequestTypeDef",
    "RenewDomainRequestRequestTypeDef",
    "ResendContactReachabilityEmailRequestRequestTypeDef",
    "ResendOperationAuthorizationRequestRequestTypeDef",
    "RetrieveDomainAuthCodeRequestRequestTypeDef",
    "TransferDomainToAnotherAwsAccountRequestRequestTypeDef",
    "UpdateDomainContactPrivacyRequestRequestTypeDef",
    "AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef",
    "AssociateDelegationSignerToDomainResponseTypeDef",
    "CancelDomainTransferToAnotherAwsAccountResponseTypeDef",
    "CheckDomainAvailabilityResponseTypeDef",
    "DeleteDomainResponseTypeDef",
    "DisableDomainTransferLockResponseTypeDef",
    "DisassociateDelegationSignerFromDomainResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EnableDomainTransferLockResponseTypeDef",
    "GetContactReachabilityStatusResponseTypeDef",
    "GetOperationDetailResponseTypeDef",
    "RegisterDomainResponseTypeDef",
    "RejectDomainTransferFromAnotherAwsAccountResponseTypeDef",
    "RenewDomainResponseTypeDef",
    "ResendContactReachabilityEmailResponseTypeDef",
    "RetrieveDomainAuthCodeResponseTypeDef",
    "TransferDomainResponseTypeDef",
    "TransferDomainToAnotherAwsAccountResponseTypeDef",
    "UpdateDomainContactPrivacyResponseTypeDef",
    "UpdateDomainContactResponseTypeDef",
    "UpdateDomainNameserversResponseTypeDef",
    "AssociateDelegationSignerToDomainRequestRequestTypeDef",
    "ViewBillingResponseTypeDef",
    "CheckDomainTransferabilityResponseTypeDef",
    "ContactDetailOutputTypeDef",
    "ContactDetailTypeDef",
    "DomainPriceTypeDef",
    "GetDomainSuggestionsResponseTypeDef",
    "ListDomainsResponseTypeDef",
    "ListPricesRequestListPricesPaginateTypeDef",
    "ListDomainsRequestListDomainsPaginateTypeDef",
    "ListDomainsRequestRequestTypeDef",
    "ListOperationsRequestListOperationsPaginateTypeDef",
    "ListOperationsRequestRequestTypeDef",
    "ViewBillingRequestRequestTypeDef",
    "ViewBillingRequestViewBillingPaginateTypeDef",
    "ListOperationsResponseTypeDef",
    "ListTagsForDomainResponseTypeDef",
    "UpdateTagsForDomainRequestRequestTypeDef",
    "NameserverUnionTypeDef",
    "UpdateDomainNameserversRequestRequestTypeDef",
    "GetDomainDetailResponseTypeDef",
    "RegisterDomainRequestRequestTypeDef",
    "UpdateDomainContactRequestRequestTypeDef",
    "ListPricesResponseTypeDef",
    "TransferDomainRequestRequestTypeDef",
)

AcceptDomainTransferFromAnotherAwsAccountRequestRequestTypeDef = TypedDict(
    "AcceptDomainTransferFromAnotherAwsAccountRequestRequestTypeDef",
    {
        "DomainName": str,
        "Password": str,
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
DnssecSigningAttributesTypeDef = TypedDict(
    "DnssecSigningAttributesTypeDef",
    {
        "Algorithm": NotRequired[int],
        "Flags": NotRequired[int],
        "PublicKey": NotRequired[str],
    },
)
BillingRecordTypeDef = TypedDict(
    "BillingRecordTypeDef",
    {
        "DomainName": NotRequired[str],
        "Operation": NotRequired[OperationTypeType],
        "InvoiceId": NotRequired[str],
        "BillDate": NotRequired[datetime],
        "Price": NotRequired[float],
    },
)
CancelDomainTransferToAnotherAwsAccountRequestRequestTypeDef = TypedDict(
    "CancelDomainTransferToAnotherAwsAccountRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
CheckDomainAvailabilityRequestRequestTypeDef = TypedDict(
    "CheckDomainAvailabilityRequestRequestTypeDef",
    {
        "DomainName": str,
        "IdnLangCode": NotRequired[str],
    },
)
CheckDomainTransferabilityRequestRequestTypeDef = TypedDict(
    "CheckDomainTransferabilityRequestRequestTypeDef",
    {
        "DomainName": str,
        "AuthCode": NotRequired[str],
    },
)
DomainTransferabilityTypeDef = TypedDict(
    "DomainTransferabilityTypeDef",
    {
        "Transferable": NotRequired[TransferableType],
    },
)
ConsentTypeDef = TypedDict(
    "ConsentTypeDef",
    {
        "MaxPrice": float,
        "Currency": str,
    },
)
ExtraParamTypeDef = TypedDict(
    "ExtraParamTypeDef",
    {
        "Name": ExtraParamNameType,
        "Value": str,
    },
)
DeleteDomainRequestRequestTypeDef = TypedDict(
    "DeleteDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
DeleteTagsForDomainRequestRequestTypeDef = TypedDict(
    "DeleteTagsForDomainRequestRequestTypeDef",
    {
        "DomainName": str,
        "TagsToDelete": Sequence[str],
    },
)
DisableDomainAutoRenewRequestRequestTypeDef = TypedDict(
    "DisableDomainAutoRenewRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
DisableDomainTransferLockRequestRequestTypeDef = TypedDict(
    "DisableDomainTransferLockRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
DisassociateDelegationSignerFromDomainRequestRequestTypeDef = TypedDict(
    "DisassociateDelegationSignerFromDomainRequestRequestTypeDef",
    {
        "DomainName": str,
        "Id": str,
    },
)
DnssecKeyTypeDef = TypedDict(
    "DnssecKeyTypeDef",
    {
        "Algorithm": NotRequired[int],
        "Flags": NotRequired[int],
        "PublicKey": NotRequired[str],
        "DigestType": NotRequired[int],
        "Digest": NotRequired[str],
        "KeyTag": NotRequired[int],
        "Id": NotRequired[str],
    },
)
PriceWithCurrencyTypeDef = TypedDict(
    "PriceWithCurrencyTypeDef",
    {
        "Price": float,
        "Currency": str,
    },
)
DomainSuggestionTypeDef = TypedDict(
    "DomainSuggestionTypeDef",
    {
        "DomainName": NotRequired[str],
        "Availability": NotRequired[str],
    },
)
DomainSummaryTypeDef = TypedDict(
    "DomainSummaryTypeDef",
    {
        "DomainName": NotRequired[str],
        "AutoRenew": NotRequired[bool],
        "TransferLock": NotRequired[bool],
        "Expiry": NotRequired[datetime],
    },
)
EnableDomainAutoRenewRequestRequestTypeDef = TypedDict(
    "EnableDomainAutoRenewRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
EnableDomainTransferLockRequestRequestTypeDef = TypedDict(
    "EnableDomainTransferLockRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
FilterConditionTypeDef = TypedDict(
    "FilterConditionTypeDef",
    {
        "Name": ListDomainsAttributeNameType,
        "Operator": OperatorType,
        "Values": Sequence[str],
    },
)
GetContactReachabilityStatusRequestRequestTypeDef = TypedDict(
    "GetContactReachabilityStatusRequestRequestTypeDef",
    {
        "domainName": NotRequired[str],
    },
)
GetDomainDetailRequestRequestTypeDef = TypedDict(
    "GetDomainDetailRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
NameserverOutputTypeDef = TypedDict(
    "NameserverOutputTypeDef",
    {
        "Name": str,
        "GlueIps": NotRequired[List[str]],
    },
)
GetDomainSuggestionsRequestRequestTypeDef = TypedDict(
    "GetDomainSuggestionsRequestRequestTypeDef",
    {
        "DomainName": str,
        "SuggestionCount": int,
        "OnlyAvailable": bool,
    },
)
GetOperationDetailRequestRequestTypeDef = TypedDict(
    "GetOperationDetailRequestRequestTypeDef",
    {
        "OperationId": str,
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
SortConditionTypeDef = TypedDict(
    "SortConditionTypeDef",
    {
        "Name": ListDomainsAttributeNameType,
        "SortOrder": SortOrderType,
    },
)
TimestampTypeDef = Union[datetime, str]
OperationSummaryTypeDef = TypedDict(
    "OperationSummaryTypeDef",
    {
        "OperationId": NotRequired[str],
        "Status": NotRequired[OperationStatusType],
        "Type": NotRequired[OperationTypeType],
        "SubmittedDate": NotRequired[datetime],
        "DomainName": NotRequired[str],
        "Message": NotRequired[str],
        "StatusFlag": NotRequired[StatusFlagType],
        "LastUpdatedDate": NotRequired[datetime],
    },
)
ListPricesRequestRequestTypeDef = TypedDict(
    "ListPricesRequestRequestTypeDef",
    {
        "Tld": NotRequired[str],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
ListTagsForDomainRequestRequestTypeDef = TypedDict(
    "ListTagsForDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
NameserverTypeDef = TypedDict(
    "NameserverTypeDef",
    {
        "Name": str,
        "GlueIps": NotRequired[Sequence[str]],
    },
)
PushDomainRequestRequestTypeDef = TypedDict(
    "PushDomainRequestRequestTypeDef",
    {
        "DomainName": str,
        "Target": str,
    },
)
RejectDomainTransferFromAnotherAwsAccountRequestRequestTypeDef = TypedDict(
    "RejectDomainTransferFromAnotherAwsAccountRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
RenewDomainRequestRequestTypeDef = TypedDict(
    "RenewDomainRequestRequestTypeDef",
    {
        "DomainName": str,
        "CurrentExpiryYear": int,
        "DurationInYears": NotRequired[int],
    },
)
ResendContactReachabilityEmailRequestRequestTypeDef = TypedDict(
    "ResendContactReachabilityEmailRequestRequestTypeDef",
    {
        "domainName": NotRequired[str],
    },
)
ResendOperationAuthorizationRequestRequestTypeDef = TypedDict(
    "ResendOperationAuthorizationRequestRequestTypeDef",
    {
        "OperationId": str,
    },
)
RetrieveDomainAuthCodeRequestRequestTypeDef = TypedDict(
    "RetrieveDomainAuthCodeRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
TransferDomainToAnotherAwsAccountRequestRequestTypeDef = TypedDict(
    "TransferDomainToAnotherAwsAccountRequestRequestTypeDef",
    {
        "DomainName": str,
        "AccountId": str,
    },
)
UpdateDomainContactPrivacyRequestRequestTypeDef = TypedDict(
    "UpdateDomainContactPrivacyRequestRequestTypeDef",
    {
        "DomainName": str,
        "AdminPrivacy": NotRequired[bool],
        "RegistrantPrivacy": NotRequired[bool],
        "TechPrivacy": NotRequired[bool],
        "BillingPrivacy": NotRequired[bool],
    },
)
AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef = TypedDict(
    "AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateDelegationSignerToDomainResponseTypeDef = TypedDict(
    "AssociateDelegationSignerToDomainResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CancelDomainTransferToAnotherAwsAccountResponseTypeDef = TypedDict(
    "CancelDomainTransferToAnotherAwsAccountResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CheckDomainAvailabilityResponseTypeDef = TypedDict(
    "CheckDomainAvailabilityResponseTypeDef",
    {
        "Availability": DomainAvailabilityType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDomainResponseTypeDef = TypedDict(
    "DeleteDomainResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisableDomainTransferLockResponseTypeDef = TypedDict(
    "DisableDomainTransferLockResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateDelegationSignerFromDomainResponseTypeDef = TypedDict(
    "DisassociateDelegationSignerFromDomainResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableDomainTransferLockResponseTypeDef = TypedDict(
    "EnableDomainTransferLockResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetContactReachabilityStatusResponseTypeDef = TypedDict(
    "GetContactReachabilityStatusResponseTypeDef",
    {
        "domainName": str,
        "status": ReachabilityStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetOperationDetailResponseTypeDef = TypedDict(
    "GetOperationDetailResponseTypeDef",
    {
        "OperationId": str,
        "Status": OperationStatusType,
        "Message": str,
        "DomainName": str,
        "Type": OperationTypeType,
        "SubmittedDate": datetime,
        "LastUpdatedDate": datetime,
        "StatusFlag": StatusFlagType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterDomainResponseTypeDef = TypedDict(
    "RegisterDomainResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RejectDomainTransferFromAnotherAwsAccountResponseTypeDef = TypedDict(
    "RejectDomainTransferFromAnotherAwsAccountResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RenewDomainResponseTypeDef = TypedDict(
    "RenewDomainResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResendContactReachabilityEmailResponseTypeDef = TypedDict(
    "ResendContactReachabilityEmailResponseTypeDef",
    {
        "domainName": str,
        "emailAddress": str,
        "isAlreadyVerified": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RetrieveDomainAuthCodeResponseTypeDef = TypedDict(
    "RetrieveDomainAuthCodeResponseTypeDef",
    {
        "AuthCode": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TransferDomainResponseTypeDef = TypedDict(
    "TransferDomainResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TransferDomainToAnotherAwsAccountResponseTypeDef = TypedDict(
    "TransferDomainToAnotherAwsAccountResponseTypeDef",
    {
        "OperationId": str,
        "Password": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDomainContactPrivacyResponseTypeDef = TypedDict(
    "UpdateDomainContactPrivacyResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDomainContactResponseTypeDef = TypedDict(
    "UpdateDomainContactResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDomainNameserversResponseTypeDef = TypedDict(
    "UpdateDomainNameserversResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateDelegationSignerToDomainRequestRequestTypeDef = TypedDict(
    "AssociateDelegationSignerToDomainRequestRequestTypeDef",
    {
        "DomainName": str,
        "SigningAttributes": DnssecSigningAttributesTypeDef,
    },
)
ViewBillingResponseTypeDef = TypedDict(
    "ViewBillingResponseTypeDef",
    {
        "NextPageMarker": str,
        "BillingRecords": List[BillingRecordTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CheckDomainTransferabilityResponseTypeDef = TypedDict(
    "CheckDomainTransferabilityResponseTypeDef",
    {
        "Transferability": DomainTransferabilityTypeDef,
        "Message": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ContactDetailOutputTypeDef = TypedDict(
    "ContactDetailOutputTypeDef",
    {
        "FirstName": NotRequired[str],
        "LastName": NotRequired[str],
        "ContactType": NotRequired[ContactTypeType],
        "OrganizationName": NotRequired[str],
        "AddressLine1": NotRequired[str],
        "AddressLine2": NotRequired[str],
        "City": NotRequired[str],
        "State": NotRequired[str],
        "CountryCode": NotRequired[CountryCodeType],
        "ZipCode": NotRequired[str],
        "PhoneNumber": NotRequired[str],
        "Email": NotRequired[str],
        "Fax": NotRequired[str],
        "ExtraParams": NotRequired[List[ExtraParamTypeDef]],
    },
)
ContactDetailTypeDef = TypedDict(
    "ContactDetailTypeDef",
    {
        "FirstName": NotRequired[str],
        "LastName": NotRequired[str],
        "ContactType": NotRequired[ContactTypeType],
        "OrganizationName": NotRequired[str],
        "AddressLine1": NotRequired[str],
        "AddressLine2": NotRequired[str],
        "City": NotRequired[str],
        "State": NotRequired[str],
        "CountryCode": NotRequired[CountryCodeType],
        "ZipCode": NotRequired[str],
        "PhoneNumber": NotRequired[str],
        "Email": NotRequired[str],
        "Fax": NotRequired[str],
        "ExtraParams": NotRequired[Sequence[ExtraParamTypeDef]],
    },
)
DomainPriceTypeDef = TypedDict(
    "DomainPriceTypeDef",
    {
        "Name": NotRequired[str],
        "RegistrationPrice": NotRequired[PriceWithCurrencyTypeDef],
        "TransferPrice": NotRequired[PriceWithCurrencyTypeDef],
        "RenewalPrice": NotRequired[PriceWithCurrencyTypeDef],
        "ChangeOwnershipPrice": NotRequired[PriceWithCurrencyTypeDef],
        "RestorationPrice": NotRequired[PriceWithCurrencyTypeDef],
    },
)
GetDomainSuggestionsResponseTypeDef = TypedDict(
    "GetDomainSuggestionsResponseTypeDef",
    {
        "SuggestionsList": List[DomainSuggestionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDomainsResponseTypeDef = TypedDict(
    "ListDomainsResponseTypeDef",
    {
        "Domains": List[DomainSummaryTypeDef],
        "NextPageMarker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPricesRequestListPricesPaginateTypeDef = TypedDict(
    "ListPricesRequestListPricesPaginateTypeDef",
    {
        "Tld": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDomainsRequestListDomainsPaginateTypeDef = TypedDict(
    "ListDomainsRequestListDomainsPaginateTypeDef",
    {
        "FilterConditions": NotRequired[Sequence[FilterConditionTypeDef]],
        "SortCondition": NotRequired[SortConditionTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDomainsRequestRequestTypeDef = TypedDict(
    "ListDomainsRequestRequestTypeDef",
    {
        "FilterConditions": NotRequired[Sequence[FilterConditionTypeDef]],
        "SortCondition": NotRequired[SortConditionTypeDef],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
ListOperationsRequestListOperationsPaginateTypeDef = TypedDict(
    "ListOperationsRequestListOperationsPaginateTypeDef",
    {
        "SubmittedSince": NotRequired[TimestampTypeDef],
        "Status": NotRequired[Sequence[OperationStatusType]],
        "Type": NotRequired[Sequence[OperationTypeType]],
        "SortBy": NotRequired[Literal["SubmittedDate"]],
        "SortOrder": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOperationsRequestRequestTypeDef = TypedDict(
    "ListOperationsRequestRequestTypeDef",
    {
        "SubmittedSince": NotRequired[TimestampTypeDef],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
        "Status": NotRequired[Sequence[OperationStatusType]],
        "Type": NotRequired[Sequence[OperationTypeType]],
        "SortBy": NotRequired[Literal["SubmittedDate"]],
        "SortOrder": NotRequired[SortOrderType],
    },
)
ViewBillingRequestRequestTypeDef = TypedDict(
    "ViewBillingRequestRequestTypeDef",
    {
        "Start": NotRequired[TimestampTypeDef],
        "End": NotRequired[TimestampTypeDef],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
ViewBillingRequestViewBillingPaginateTypeDef = TypedDict(
    "ViewBillingRequestViewBillingPaginateTypeDef",
    {
        "Start": NotRequired[TimestampTypeDef],
        "End": NotRequired[TimestampTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOperationsResponseTypeDef = TypedDict(
    "ListOperationsResponseTypeDef",
    {
        "Operations": List[OperationSummaryTypeDef],
        "NextPageMarker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForDomainResponseTypeDef = TypedDict(
    "ListTagsForDomainResponseTypeDef",
    {
        "TagList": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTagsForDomainRequestRequestTypeDef = TypedDict(
    "UpdateTagsForDomainRequestRequestTypeDef",
    {
        "DomainName": str,
        "TagsToUpdate": NotRequired[Sequence[TagTypeDef]],
    },
)
NameserverUnionTypeDef = Union[NameserverTypeDef, NameserverOutputTypeDef]
UpdateDomainNameserversRequestRequestTypeDef = TypedDict(
    "UpdateDomainNameserversRequestRequestTypeDef",
    {
        "DomainName": str,
        "Nameservers": Sequence[NameserverTypeDef],
        "FIAuthKey": NotRequired[str],
    },
)
GetDomainDetailResponseTypeDef = TypedDict(
    "GetDomainDetailResponseTypeDef",
    {
        "DomainName": str,
        "Nameservers": List[NameserverOutputTypeDef],
        "AutoRenew": bool,
        "AdminContact": ContactDetailOutputTypeDef,
        "RegistrantContact": ContactDetailOutputTypeDef,
        "TechContact": ContactDetailOutputTypeDef,
        "AdminPrivacy": bool,
        "RegistrantPrivacy": bool,
        "TechPrivacy": bool,
        "RegistrarName": str,
        "WhoIsServer": str,
        "RegistrarUrl": str,
        "AbuseContactEmail": str,
        "AbuseContactPhone": str,
        "RegistryDomainId": str,
        "CreationDate": datetime,
        "UpdatedDate": datetime,
        "ExpirationDate": datetime,
        "Reseller": str,
        "DnsSec": str,
        "StatusList": List[str],
        "DnssecKeys": List[DnssecKeyTypeDef],
        "BillingContact": ContactDetailOutputTypeDef,
        "BillingPrivacy": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterDomainRequestRequestTypeDef = TypedDict(
    "RegisterDomainRequestRequestTypeDef",
    {
        "DomainName": str,
        "DurationInYears": int,
        "AdminContact": ContactDetailTypeDef,
        "RegistrantContact": ContactDetailTypeDef,
        "TechContact": ContactDetailTypeDef,
        "IdnLangCode": NotRequired[str],
        "AutoRenew": NotRequired[bool],
        "PrivacyProtectAdminContact": NotRequired[bool],
        "PrivacyProtectRegistrantContact": NotRequired[bool],
        "PrivacyProtectTechContact": NotRequired[bool],
        "BillingContact": NotRequired[ContactDetailTypeDef],
        "PrivacyProtectBillingContact": NotRequired[bool],
    },
)
UpdateDomainContactRequestRequestTypeDef = TypedDict(
    "UpdateDomainContactRequestRequestTypeDef",
    {
        "DomainName": str,
        "AdminContact": NotRequired[ContactDetailTypeDef],
        "RegistrantContact": NotRequired[ContactDetailTypeDef],
        "TechContact": NotRequired[ContactDetailTypeDef],
        "Consent": NotRequired[ConsentTypeDef],
        "BillingContact": NotRequired[ContactDetailTypeDef],
    },
)
ListPricesResponseTypeDef = TypedDict(
    "ListPricesResponseTypeDef",
    {
        "Prices": List[DomainPriceTypeDef],
        "NextPageMarker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TransferDomainRequestRequestTypeDef = TypedDict(
    "TransferDomainRequestRequestTypeDef",
    {
        "DomainName": str,
        "DurationInYears": int,
        "AdminContact": ContactDetailTypeDef,
        "RegistrantContact": ContactDetailTypeDef,
        "TechContact": ContactDetailTypeDef,
        "IdnLangCode": NotRequired[str],
        "Nameservers": NotRequired[Sequence[NameserverUnionTypeDef]],
        "AuthCode": NotRequired[str],
        "AutoRenew": NotRequired[bool],
        "PrivacyProtectAdminContact": NotRequired[bool],
        "PrivacyProtectRegistrantContact": NotRequired[bool],
        "PrivacyProtectTechContact": NotRequired[bool],
        "BillingContact": NotRequired[ContactDetailTypeDef],
        "PrivacyProtectBillingContact": NotRequired[bool],
    },
)
