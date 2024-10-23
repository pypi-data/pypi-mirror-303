"""
Type annotations for account service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_account/type_defs/)

Usage::

    ```python
    from mypy_boto3_account.type_defs import AcceptPrimaryEmailUpdateRequestRequestTypeDef

    data: AcceptPrimaryEmailUpdateRequestRequestTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Sequence

from .literals import AlternateContactTypeType, PrimaryEmailUpdateStatusType, RegionOptStatusType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AcceptPrimaryEmailUpdateRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "AlternateContactTypeDef",
    "ContactInformationTypeDef",
    "DeleteAlternateContactRequestRequestTypeDef",
    "DisableRegionRequestRequestTypeDef",
    "EnableRegionRequestRequestTypeDef",
    "GetAlternateContactRequestRequestTypeDef",
    "GetContactInformationRequestRequestTypeDef",
    "GetPrimaryEmailRequestRequestTypeDef",
    "GetRegionOptStatusRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListRegionsRequestRequestTypeDef",
    "RegionTypeDef",
    "PutAlternateContactRequestRequestTypeDef",
    "StartPrimaryEmailUpdateRequestRequestTypeDef",
    "AcceptPrimaryEmailUpdateResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetPrimaryEmailResponseTypeDef",
    "GetRegionOptStatusResponseTypeDef",
    "StartPrimaryEmailUpdateResponseTypeDef",
    "GetAlternateContactResponseTypeDef",
    "GetContactInformationResponseTypeDef",
    "PutContactInformationRequestRequestTypeDef",
    "ListRegionsRequestListRegionsPaginateTypeDef",
    "ListRegionsResponseTypeDef",
)

AcceptPrimaryEmailUpdateRequestRequestTypeDef = TypedDict(
    "AcceptPrimaryEmailUpdateRequestRequestTypeDef",
    {
        "AccountId": str,
        "Otp": str,
        "PrimaryEmail": str,
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
AlternateContactTypeDef = TypedDict(
    "AlternateContactTypeDef",
    {
        "AlternateContactType": NotRequired[AlternateContactTypeType],
        "EmailAddress": NotRequired[str],
        "Name": NotRequired[str],
        "PhoneNumber": NotRequired[str],
        "Title": NotRequired[str],
    },
)
ContactInformationTypeDef = TypedDict(
    "ContactInformationTypeDef",
    {
        "AddressLine1": str,
        "City": str,
        "CountryCode": str,
        "FullName": str,
        "PhoneNumber": str,
        "PostalCode": str,
        "AddressLine2": NotRequired[str],
        "AddressLine3": NotRequired[str],
        "CompanyName": NotRequired[str],
        "DistrictOrCounty": NotRequired[str],
        "StateOrRegion": NotRequired[str],
        "WebsiteUrl": NotRequired[str],
    },
)
DeleteAlternateContactRequestRequestTypeDef = TypedDict(
    "DeleteAlternateContactRequestRequestTypeDef",
    {
        "AlternateContactType": AlternateContactTypeType,
        "AccountId": NotRequired[str],
    },
)
DisableRegionRequestRequestTypeDef = TypedDict(
    "DisableRegionRequestRequestTypeDef",
    {
        "RegionName": str,
        "AccountId": NotRequired[str],
    },
)
EnableRegionRequestRequestTypeDef = TypedDict(
    "EnableRegionRequestRequestTypeDef",
    {
        "RegionName": str,
        "AccountId": NotRequired[str],
    },
)
GetAlternateContactRequestRequestTypeDef = TypedDict(
    "GetAlternateContactRequestRequestTypeDef",
    {
        "AlternateContactType": AlternateContactTypeType,
        "AccountId": NotRequired[str],
    },
)
GetContactInformationRequestRequestTypeDef = TypedDict(
    "GetContactInformationRequestRequestTypeDef",
    {
        "AccountId": NotRequired[str],
    },
)
GetPrimaryEmailRequestRequestTypeDef = TypedDict(
    "GetPrimaryEmailRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
GetRegionOptStatusRequestRequestTypeDef = TypedDict(
    "GetRegionOptStatusRequestRequestTypeDef",
    {
        "RegionName": str,
        "AccountId": NotRequired[str],
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
ListRegionsRequestRequestTypeDef = TypedDict(
    "ListRegionsRequestRequestTypeDef",
    {
        "AccountId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "RegionOptStatusContains": NotRequired[Sequence[RegionOptStatusType]],
    },
)
RegionTypeDef = TypedDict(
    "RegionTypeDef",
    {
        "RegionName": NotRequired[str],
        "RegionOptStatus": NotRequired[RegionOptStatusType],
    },
)
PutAlternateContactRequestRequestTypeDef = TypedDict(
    "PutAlternateContactRequestRequestTypeDef",
    {
        "AlternateContactType": AlternateContactTypeType,
        "EmailAddress": str,
        "Name": str,
        "PhoneNumber": str,
        "Title": str,
        "AccountId": NotRequired[str],
    },
)
StartPrimaryEmailUpdateRequestRequestTypeDef = TypedDict(
    "StartPrimaryEmailUpdateRequestRequestTypeDef",
    {
        "AccountId": str,
        "PrimaryEmail": str,
    },
)
AcceptPrimaryEmailUpdateResponseTypeDef = TypedDict(
    "AcceptPrimaryEmailUpdateResponseTypeDef",
    {
        "Status": PrimaryEmailUpdateStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPrimaryEmailResponseTypeDef = TypedDict(
    "GetPrimaryEmailResponseTypeDef",
    {
        "PrimaryEmail": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRegionOptStatusResponseTypeDef = TypedDict(
    "GetRegionOptStatusResponseTypeDef",
    {
        "RegionName": str,
        "RegionOptStatus": RegionOptStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartPrimaryEmailUpdateResponseTypeDef = TypedDict(
    "StartPrimaryEmailUpdateResponseTypeDef",
    {
        "Status": PrimaryEmailUpdateStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAlternateContactResponseTypeDef = TypedDict(
    "GetAlternateContactResponseTypeDef",
    {
        "AlternateContact": AlternateContactTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetContactInformationResponseTypeDef = TypedDict(
    "GetContactInformationResponseTypeDef",
    {
        "ContactInformation": ContactInformationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutContactInformationRequestRequestTypeDef = TypedDict(
    "PutContactInformationRequestRequestTypeDef",
    {
        "ContactInformation": ContactInformationTypeDef,
        "AccountId": NotRequired[str],
    },
)
ListRegionsRequestListRegionsPaginateTypeDef = TypedDict(
    "ListRegionsRequestListRegionsPaginateTypeDef",
    {
        "AccountId": NotRequired[str],
        "RegionOptStatusContains": NotRequired[Sequence[RegionOptStatusType]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRegionsResponseTypeDef = TypedDict(
    "ListRegionsResponseTypeDef",
    {
        "Regions": List[RegionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
