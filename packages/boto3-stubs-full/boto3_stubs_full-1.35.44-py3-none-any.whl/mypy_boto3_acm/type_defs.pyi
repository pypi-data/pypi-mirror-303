"""
Type annotations for acm service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm/type_defs/)

Usage::

    ```python
    from mypy_boto3_acm.type_defs import TagTypeDef

    data: TagTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    CertificateStatusType,
    CertificateTransparencyLoggingPreferenceType,
    CertificateTypeType,
    DomainStatusType,
    ExtendedKeyUsageNameType,
    FailureReasonType,
    KeyAlgorithmType,
    KeyUsageNameType,
    RenewalEligibilityType,
    RenewalStatusType,
    RevocationReasonType,
    SortOrderType,
    ValidationMethodType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "TagTypeDef",
    "BlobTypeDef",
    "CertificateOptionsTypeDef",
    "ExtendedKeyUsageTypeDef",
    "KeyUsageTypeDef",
    "CertificateSummaryTypeDef",
    "DeleteCertificateRequestRequestTypeDef",
    "WaiterConfigTypeDef",
    "DescribeCertificateRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "DomainValidationOptionTypeDef",
    "ResourceRecordTypeDef",
    "ExpiryEventsConfigurationTypeDef",
    "FiltersTypeDef",
    "GetCertificateRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListTagsForCertificateRequestRequestTypeDef",
    "RenewCertificateRequestRequestTypeDef",
    "ResendValidationEmailRequestRequestTypeDef",
    "AddTagsToCertificateRequestRequestTypeDef",
    "RemoveTagsFromCertificateRequestRequestTypeDef",
    "ExportCertificateRequestRequestTypeDef",
    "ImportCertificateRequestRequestTypeDef",
    "UpdateCertificateOptionsRequestRequestTypeDef",
    "DescribeCertificateRequestCertificateValidatedWaitTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ExportCertificateResponseTypeDef",
    "GetCertificateResponseTypeDef",
    "ImportCertificateResponseTypeDef",
    "ListCertificatesResponseTypeDef",
    "ListTagsForCertificateResponseTypeDef",
    "RequestCertificateResponseTypeDef",
    "RequestCertificateRequestRequestTypeDef",
    "DomainValidationTypeDef",
    "GetAccountConfigurationResponseTypeDef",
    "PutAccountConfigurationRequestRequestTypeDef",
    "ListCertificatesRequestRequestTypeDef",
    "ListCertificatesRequestListCertificatesPaginateTypeDef",
    "RenewalSummaryTypeDef",
    "CertificateDetailTypeDef",
    "DescribeCertificateResponseTypeDef",
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": NotRequired[str],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
CertificateOptionsTypeDef = TypedDict(
    "CertificateOptionsTypeDef",
    {
        "CertificateTransparencyLoggingPreference": NotRequired[
            CertificateTransparencyLoggingPreferenceType
        ],
    },
)
ExtendedKeyUsageTypeDef = TypedDict(
    "ExtendedKeyUsageTypeDef",
    {
        "Name": NotRequired[ExtendedKeyUsageNameType],
        "OID": NotRequired[str],
    },
)
KeyUsageTypeDef = TypedDict(
    "KeyUsageTypeDef",
    {
        "Name": NotRequired[KeyUsageNameType],
    },
)
CertificateSummaryTypeDef = TypedDict(
    "CertificateSummaryTypeDef",
    {
        "CertificateArn": NotRequired[str],
        "DomainName": NotRequired[str],
        "SubjectAlternativeNameSummaries": NotRequired[List[str]],
        "HasAdditionalSubjectAlternativeNames": NotRequired[bool],
        "Status": NotRequired[CertificateStatusType],
        "Type": NotRequired[CertificateTypeType],
        "KeyAlgorithm": NotRequired[KeyAlgorithmType],
        "KeyUsages": NotRequired[List[KeyUsageNameType]],
        "ExtendedKeyUsages": NotRequired[List[ExtendedKeyUsageNameType]],
        "InUse": NotRequired[bool],
        "Exported": NotRequired[bool],
        "RenewalEligibility": NotRequired[RenewalEligibilityType],
        "NotBefore": NotRequired[datetime],
        "NotAfter": NotRequired[datetime],
        "CreatedAt": NotRequired[datetime],
        "IssuedAt": NotRequired[datetime],
        "ImportedAt": NotRequired[datetime],
        "RevokedAt": NotRequired[datetime],
    },
)
DeleteCertificateRequestRequestTypeDef = TypedDict(
    "DeleteCertificateRequestRequestTypeDef",
    {
        "CertificateArn": str,
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
DescribeCertificateRequestRequestTypeDef = TypedDict(
    "DescribeCertificateRequestRequestTypeDef",
    {
        "CertificateArn": str,
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
DomainValidationOptionTypeDef = TypedDict(
    "DomainValidationOptionTypeDef",
    {
        "DomainName": str,
        "ValidationDomain": str,
    },
)
ResourceRecordTypeDef = TypedDict(
    "ResourceRecordTypeDef",
    {
        "Name": str,
        "Type": Literal["CNAME"],
        "Value": str,
    },
)
ExpiryEventsConfigurationTypeDef = TypedDict(
    "ExpiryEventsConfigurationTypeDef",
    {
        "DaysBeforeExpiry": NotRequired[int],
    },
)
FiltersTypeDef = TypedDict(
    "FiltersTypeDef",
    {
        "extendedKeyUsage": NotRequired[Sequence[ExtendedKeyUsageNameType]],
        "keyUsage": NotRequired[Sequence[KeyUsageNameType]],
        "keyTypes": NotRequired[Sequence[KeyAlgorithmType]],
    },
)
GetCertificateRequestRequestTypeDef = TypedDict(
    "GetCertificateRequestRequestTypeDef",
    {
        "CertificateArn": str,
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
ListTagsForCertificateRequestRequestTypeDef = TypedDict(
    "ListTagsForCertificateRequestRequestTypeDef",
    {
        "CertificateArn": str,
    },
)
RenewCertificateRequestRequestTypeDef = TypedDict(
    "RenewCertificateRequestRequestTypeDef",
    {
        "CertificateArn": str,
    },
)
ResendValidationEmailRequestRequestTypeDef = TypedDict(
    "ResendValidationEmailRequestRequestTypeDef",
    {
        "CertificateArn": str,
        "Domain": str,
        "ValidationDomain": str,
    },
)
AddTagsToCertificateRequestRequestTypeDef = TypedDict(
    "AddTagsToCertificateRequestRequestTypeDef",
    {
        "CertificateArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
RemoveTagsFromCertificateRequestRequestTypeDef = TypedDict(
    "RemoveTagsFromCertificateRequestRequestTypeDef",
    {
        "CertificateArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
ExportCertificateRequestRequestTypeDef = TypedDict(
    "ExportCertificateRequestRequestTypeDef",
    {
        "CertificateArn": str,
        "Passphrase": BlobTypeDef,
    },
)
ImportCertificateRequestRequestTypeDef = TypedDict(
    "ImportCertificateRequestRequestTypeDef",
    {
        "Certificate": BlobTypeDef,
        "PrivateKey": BlobTypeDef,
        "CertificateArn": NotRequired[str],
        "CertificateChain": NotRequired[BlobTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
UpdateCertificateOptionsRequestRequestTypeDef = TypedDict(
    "UpdateCertificateOptionsRequestRequestTypeDef",
    {
        "CertificateArn": str,
        "Options": CertificateOptionsTypeDef,
    },
)
DescribeCertificateRequestCertificateValidatedWaitTypeDef = TypedDict(
    "DescribeCertificateRequestCertificateValidatedWaitTypeDef",
    {
        "CertificateArn": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportCertificateResponseTypeDef = TypedDict(
    "ExportCertificateResponseTypeDef",
    {
        "Certificate": str,
        "CertificateChain": str,
        "PrivateKey": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCertificateResponseTypeDef = TypedDict(
    "GetCertificateResponseTypeDef",
    {
        "Certificate": str,
        "CertificateChain": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportCertificateResponseTypeDef = TypedDict(
    "ImportCertificateResponseTypeDef",
    {
        "CertificateArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCertificatesResponseTypeDef = TypedDict(
    "ListCertificatesResponseTypeDef",
    {
        "CertificateSummaryList": List[CertificateSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTagsForCertificateResponseTypeDef = TypedDict(
    "ListTagsForCertificateResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RequestCertificateResponseTypeDef = TypedDict(
    "RequestCertificateResponseTypeDef",
    {
        "CertificateArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RequestCertificateRequestRequestTypeDef = TypedDict(
    "RequestCertificateRequestRequestTypeDef",
    {
        "DomainName": str,
        "ValidationMethod": NotRequired[ValidationMethodType],
        "SubjectAlternativeNames": NotRequired[Sequence[str]],
        "IdempotencyToken": NotRequired[str],
        "DomainValidationOptions": NotRequired[Sequence[DomainValidationOptionTypeDef]],
        "Options": NotRequired[CertificateOptionsTypeDef],
        "CertificateAuthorityArn": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "KeyAlgorithm": NotRequired[KeyAlgorithmType],
    },
)
DomainValidationTypeDef = TypedDict(
    "DomainValidationTypeDef",
    {
        "DomainName": str,
        "ValidationEmails": NotRequired[List[str]],
        "ValidationDomain": NotRequired[str],
        "ValidationStatus": NotRequired[DomainStatusType],
        "ResourceRecord": NotRequired[ResourceRecordTypeDef],
        "ValidationMethod": NotRequired[ValidationMethodType],
    },
)
GetAccountConfigurationResponseTypeDef = TypedDict(
    "GetAccountConfigurationResponseTypeDef",
    {
        "ExpiryEvents": ExpiryEventsConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutAccountConfigurationRequestRequestTypeDef = TypedDict(
    "PutAccountConfigurationRequestRequestTypeDef",
    {
        "IdempotencyToken": str,
        "ExpiryEvents": NotRequired[ExpiryEventsConfigurationTypeDef],
    },
)
ListCertificatesRequestRequestTypeDef = TypedDict(
    "ListCertificatesRequestRequestTypeDef",
    {
        "CertificateStatuses": NotRequired[Sequence[CertificateStatusType]],
        "Includes": NotRequired[FiltersTypeDef],
        "NextToken": NotRequired[str],
        "MaxItems": NotRequired[int],
        "SortBy": NotRequired[Literal["CREATED_AT"]],
        "SortOrder": NotRequired[SortOrderType],
    },
)
ListCertificatesRequestListCertificatesPaginateTypeDef = TypedDict(
    "ListCertificatesRequestListCertificatesPaginateTypeDef",
    {
        "CertificateStatuses": NotRequired[Sequence[CertificateStatusType]],
        "Includes": NotRequired[FiltersTypeDef],
        "SortBy": NotRequired[Literal["CREATED_AT"]],
        "SortOrder": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
RenewalSummaryTypeDef = TypedDict(
    "RenewalSummaryTypeDef",
    {
        "RenewalStatus": RenewalStatusType,
        "DomainValidationOptions": List[DomainValidationTypeDef],
        "UpdatedAt": datetime,
        "RenewalStatusReason": NotRequired[FailureReasonType],
    },
)
CertificateDetailTypeDef = TypedDict(
    "CertificateDetailTypeDef",
    {
        "CertificateArn": NotRequired[str],
        "DomainName": NotRequired[str],
        "SubjectAlternativeNames": NotRequired[List[str]],
        "DomainValidationOptions": NotRequired[List[DomainValidationTypeDef]],
        "Serial": NotRequired[str],
        "Subject": NotRequired[str],
        "Issuer": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "IssuedAt": NotRequired[datetime],
        "ImportedAt": NotRequired[datetime],
        "Status": NotRequired[CertificateStatusType],
        "RevokedAt": NotRequired[datetime],
        "RevocationReason": NotRequired[RevocationReasonType],
        "NotBefore": NotRequired[datetime],
        "NotAfter": NotRequired[datetime],
        "KeyAlgorithm": NotRequired[KeyAlgorithmType],
        "SignatureAlgorithm": NotRequired[str],
        "InUseBy": NotRequired[List[str]],
        "FailureReason": NotRequired[FailureReasonType],
        "Type": NotRequired[CertificateTypeType],
        "RenewalSummary": NotRequired[RenewalSummaryTypeDef],
        "KeyUsages": NotRequired[List[KeyUsageTypeDef]],
        "ExtendedKeyUsages": NotRequired[List[ExtendedKeyUsageTypeDef]],
        "CertificateAuthorityArn": NotRequired[str],
        "RenewalEligibility": NotRequired[RenewalEligibilityType],
        "Options": NotRequired[CertificateOptionsTypeDef],
    },
)
DescribeCertificateResponseTypeDef = TypedDict(
    "DescribeCertificateResponseTypeDef",
    {
        "Certificate": CertificateDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
