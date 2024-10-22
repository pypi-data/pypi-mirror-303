"""
Type annotations for payment-cryptography service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/type_defs/)

Usage::

    ```python
    from mypy_boto3_payment_cryptography.type_defs import AliasTypeDef

    data: AliasTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    KeyAlgorithmType,
    KeyCheckValueAlgorithmType,
    KeyClassType,
    KeyExportabilityType,
    KeyMaterialTypeType,
    KeyOriginType,
    KeyStateType,
    KeyUsageType,
    WrappedKeyMaterialFormatType,
    WrappingKeySpecType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AliasTypeDef",
    "CreateAliasInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "TagTypeDef",
    "DeleteAliasInputRequestTypeDef",
    "DeleteKeyInputRequestTypeDef",
    "ExportDukptInitialKeyTypeDef",
    "ExportKeyCryptogramTypeDef",
    "WrappedKeyTypeDef",
    "GetAliasInputRequestTypeDef",
    "GetKeyInputRequestTypeDef",
    "GetParametersForExportInputRequestTypeDef",
    "GetParametersForImportInputRequestTypeDef",
    "GetPublicKeyCertificateInputRequestTypeDef",
    "ImportTr31KeyBlockTypeDef",
    "ImportTr34KeyBlockTypeDef",
    "KeyModesOfUseTypeDef",
    "PaginatorConfigTypeDef",
    "ListAliasesInputRequestTypeDef",
    "ListKeysInputRequestTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "RestoreKeyInputRequestTypeDef",
    "StartKeyUsageInputRequestTypeDef",
    "StopKeyUsageInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateAliasInputRequestTypeDef",
    "CreateAliasOutputTypeDef",
    "GetAliasOutputTypeDef",
    "GetParametersForExportOutputTypeDef",
    "GetParametersForImportOutputTypeDef",
    "GetPublicKeyCertificateOutputTypeDef",
    "ListAliasesOutputTypeDef",
    "UpdateAliasOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "TagResourceInputRequestTypeDef",
    "ExportAttributesTypeDef",
    "ExportKeyOutputTypeDef",
    "KeyAttributesTypeDef",
    "KeyBlockHeadersTypeDef",
    "ListAliasesInputListAliasesPaginateTypeDef",
    "ListKeysInputListKeysPaginateTypeDef",
    "ListTagsForResourceInputListTagsForResourcePaginateTypeDef",
    "CreateKeyInputRequestTypeDef",
    "ImportKeyCryptogramTypeDef",
    "KeySummaryTypeDef",
    "KeyTypeDef",
    "RootCertificatePublicKeyTypeDef",
    "TrustedCertificatePublicKeyTypeDef",
    "ExportTr31KeyBlockTypeDef",
    "ExportTr34KeyBlockTypeDef",
    "ListKeysOutputTypeDef",
    "CreateKeyOutputTypeDef",
    "DeleteKeyOutputTypeDef",
    "GetKeyOutputTypeDef",
    "ImportKeyOutputTypeDef",
    "RestoreKeyOutputTypeDef",
    "StartKeyUsageOutputTypeDef",
    "StopKeyUsageOutputTypeDef",
    "ImportKeyMaterialTypeDef",
    "ExportKeyMaterialTypeDef",
    "ImportKeyInputRequestTypeDef",
    "ExportKeyInputRequestTypeDef",
)

AliasTypeDef = TypedDict(
    "AliasTypeDef",
    {
        "AliasName": str,
        "KeyArn": NotRequired[str],
    },
)
CreateAliasInputRequestTypeDef = TypedDict(
    "CreateAliasInputRequestTypeDef",
    {
        "AliasName": str,
        "KeyArn": NotRequired[str],
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
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": NotRequired[str],
    },
)
DeleteAliasInputRequestTypeDef = TypedDict(
    "DeleteAliasInputRequestTypeDef",
    {
        "AliasName": str,
    },
)
DeleteKeyInputRequestTypeDef = TypedDict(
    "DeleteKeyInputRequestTypeDef",
    {
        "KeyIdentifier": str,
        "DeleteKeyInDays": NotRequired[int],
    },
)
ExportDukptInitialKeyTypeDef = TypedDict(
    "ExportDukptInitialKeyTypeDef",
    {
        "KeySerialNumber": str,
    },
)
ExportKeyCryptogramTypeDef = TypedDict(
    "ExportKeyCryptogramTypeDef",
    {
        "CertificateAuthorityPublicKeyIdentifier": str,
        "WrappingKeyCertificate": str,
        "WrappingSpec": NotRequired[WrappingKeySpecType],
    },
)
WrappedKeyTypeDef = TypedDict(
    "WrappedKeyTypeDef",
    {
        "WrappingKeyArn": str,
        "WrappedKeyMaterialFormat": WrappedKeyMaterialFormatType,
        "KeyMaterial": str,
        "KeyCheckValue": NotRequired[str],
        "KeyCheckValueAlgorithm": NotRequired[KeyCheckValueAlgorithmType],
    },
)
GetAliasInputRequestTypeDef = TypedDict(
    "GetAliasInputRequestTypeDef",
    {
        "AliasName": str,
    },
)
GetKeyInputRequestTypeDef = TypedDict(
    "GetKeyInputRequestTypeDef",
    {
        "KeyIdentifier": str,
    },
)
GetParametersForExportInputRequestTypeDef = TypedDict(
    "GetParametersForExportInputRequestTypeDef",
    {
        "KeyMaterialType": KeyMaterialTypeType,
        "SigningKeyAlgorithm": KeyAlgorithmType,
    },
)
GetParametersForImportInputRequestTypeDef = TypedDict(
    "GetParametersForImportInputRequestTypeDef",
    {
        "KeyMaterialType": KeyMaterialTypeType,
        "WrappingKeyAlgorithm": KeyAlgorithmType,
    },
)
GetPublicKeyCertificateInputRequestTypeDef = TypedDict(
    "GetPublicKeyCertificateInputRequestTypeDef",
    {
        "KeyIdentifier": str,
    },
)
ImportTr31KeyBlockTypeDef = TypedDict(
    "ImportTr31KeyBlockTypeDef",
    {
        "WrappingKeyIdentifier": str,
        "WrappedKeyBlock": str,
    },
)
ImportTr34KeyBlockTypeDef = TypedDict(
    "ImportTr34KeyBlockTypeDef",
    {
        "CertificateAuthorityPublicKeyIdentifier": str,
        "SigningKeyCertificate": str,
        "ImportToken": str,
        "WrappedKeyBlock": str,
        "KeyBlockFormat": Literal["X9_TR34_2012"],
        "RandomNonce": NotRequired[str],
    },
)
KeyModesOfUseTypeDef = TypedDict(
    "KeyModesOfUseTypeDef",
    {
        "Encrypt": NotRequired[bool],
        "Decrypt": NotRequired[bool],
        "Wrap": NotRequired[bool],
        "Unwrap": NotRequired[bool],
        "Generate": NotRequired[bool],
        "Sign": NotRequired[bool],
        "Verify": NotRequired[bool],
        "DeriveKey": NotRequired[bool],
        "NoRestrictions": NotRequired[bool],
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
ListAliasesInputRequestTypeDef = TypedDict(
    "ListAliasesInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListKeysInputRequestTypeDef = TypedDict(
    "ListKeysInputRequestTypeDef",
    {
        "KeyState": NotRequired[KeyStateType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
RestoreKeyInputRequestTypeDef = TypedDict(
    "RestoreKeyInputRequestTypeDef",
    {
        "KeyIdentifier": str,
    },
)
StartKeyUsageInputRequestTypeDef = TypedDict(
    "StartKeyUsageInputRequestTypeDef",
    {
        "KeyIdentifier": str,
    },
)
StopKeyUsageInputRequestTypeDef = TypedDict(
    "StopKeyUsageInputRequestTypeDef",
    {
        "KeyIdentifier": str,
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateAliasInputRequestTypeDef = TypedDict(
    "UpdateAliasInputRequestTypeDef",
    {
        "AliasName": str,
        "KeyArn": NotRequired[str],
    },
)
CreateAliasOutputTypeDef = TypedDict(
    "CreateAliasOutputTypeDef",
    {
        "Alias": AliasTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAliasOutputTypeDef = TypedDict(
    "GetAliasOutputTypeDef",
    {
        "Alias": AliasTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetParametersForExportOutputTypeDef = TypedDict(
    "GetParametersForExportOutputTypeDef",
    {
        "SigningKeyCertificate": str,
        "SigningKeyCertificateChain": str,
        "SigningKeyAlgorithm": KeyAlgorithmType,
        "ExportToken": str,
        "ParametersValidUntilTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetParametersForImportOutputTypeDef = TypedDict(
    "GetParametersForImportOutputTypeDef",
    {
        "WrappingKeyCertificate": str,
        "WrappingKeyCertificateChain": str,
        "WrappingKeyAlgorithm": KeyAlgorithmType,
        "ImportToken": str,
        "ParametersValidUntilTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPublicKeyCertificateOutputTypeDef = TypedDict(
    "GetPublicKeyCertificateOutputTypeDef",
    {
        "KeyCertificate": str,
        "KeyCertificateChain": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAliasesOutputTypeDef = TypedDict(
    "ListAliasesOutputTypeDef",
    {
        "Aliases": List[AliasTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateAliasOutputTypeDef = TypedDict(
    "UpdateAliasOutputTypeDef",
    {
        "Alias": AliasTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
ExportAttributesTypeDef = TypedDict(
    "ExportAttributesTypeDef",
    {
        "ExportDukptInitialKey": NotRequired[ExportDukptInitialKeyTypeDef],
        "KeyCheckValueAlgorithm": NotRequired[KeyCheckValueAlgorithmType],
    },
)
ExportKeyOutputTypeDef = TypedDict(
    "ExportKeyOutputTypeDef",
    {
        "WrappedKey": WrappedKeyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
KeyAttributesTypeDef = TypedDict(
    "KeyAttributesTypeDef",
    {
        "KeyUsage": KeyUsageType,
        "KeyClass": KeyClassType,
        "KeyAlgorithm": KeyAlgorithmType,
        "KeyModesOfUse": KeyModesOfUseTypeDef,
    },
)
KeyBlockHeadersTypeDef = TypedDict(
    "KeyBlockHeadersTypeDef",
    {
        "KeyModesOfUse": NotRequired[KeyModesOfUseTypeDef],
        "KeyExportability": NotRequired[KeyExportabilityType],
        "KeyVersion": NotRequired[str],
        "OptionalBlocks": NotRequired[Mapping[str, str]],
    },
)
ListAliasesInputListAliasesPaginateTypeDef = TypedDict(
    "ListAliasesInputListAliasesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListKeysInputListKeysPaginateTypeDef = TypedDict(
    "ListKeysInputListKeysPaginateTypeDef",
    {
        "KeyState": NotRequired[KeyStateType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTagsForResourceInputListTagsForResourcePaginateTypeDef = TypedDict(
    "ListTagsForResourceInputListTagsForResourcePaginateTypeDef",
    {
        "ResourceArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
CreateKeyInputRequestTypeDef = TypedDict(
    "CreateKeyInputRequestTypeDef",
    {
        "KeyAttributes": KeyAttributesTypeDef,
        "Exportable": bool,
        "KeyCheckValueAlgorithm": NotRequired[KeyCheckValueAlgorithmType],
        "Enabled": NotRequired[bool],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ImportKeyCryptogramTypeDef = TypedDict(
    "ImportKeyCryptogramTypeDef",
    {
        "KeyAttributes": KeyAttributesTypeDef,
        "Exportable": bool,
        "WrappedKeyCryptogram": str,
        "ImportToken": str,
        "WrappingSpec": NotRequired[WrappingKeySpecType],
    },
)
KeySummaryTypeDef = TypedDict(
    "KeySummaryTypeDef",
    {
        "KeyArn": str,
        "KeyState": KeyStateType,
        "KeyAttributes": KeyAttributesTypeDef,
        "KeyCheckValue": str,
        "Exportable": bool,
        "Enabled": bool,
    },
)
KeyTypeDef = TypedDict(
    "KeyTypeDef",
    {
        "KeyArn": str,
        "KeyAttributes": KeyAttributesTypeDef,
        "KeyCheckValue": str,
        "KeyCheckValueAlgorithm": KeyCheckValueAlgorithmType,
        "Enabled": bool,
        "Exportable": bool,
        "KeyState": KeyStateType,
        "KeyOrigin": KeyOriginType,
        "CreateTimestamp": datetime,
        "UsageStartTimestamp": NotRequired[datetime],
        "UsageStopTimestamp": NotRequired[datetime],
        "DeletePendingTimestamp": NotRequired[datetime],
        "DeleteTimestamp": NotRequired[datetime],
    },
)
RootCertificatePublicKeyTypeDef = TypedDict(
    "RootCertificatePublicKeyTypeDef",
    {
        "KeyAttributes": KeyAttributesTypeDef,
        "PublicKeyCertificate": str,
    },
)
TrustedCertificatePublicKeyTypeDef = TypedDict(
    "TrustedCertificatePublicKeyTypeDef",
    {
        "KeyAttributes": KeyAttributesTypeDef,
        "PublicKeyCertificate": str,
        "CertificateAuthorityPublicKeyIdentifier": str,
    },
)
ExportTr31KeyBlockTypeDef = TypedDict(
    "ExportTr31KeyBlockTypeDef",
    {
        "WrappingKeyIdentifier": str,
        "KeyBlockHeaders": NotRequired[KeyBlockHeadersTypeDef],
    },
)
ExportTr34KeyBlockTypeDef = TypedDict(
    "ExportTr34KeyBlockTypeDef",
    {
        "CertificateAuthorityPublicKeyIdentifier": str,
        "WrappingKeyCertificate": str,
        "ExportToken": str,
        "KeyBlockFormat": Literal["X9_TR34_2012"],
        "RandomNonce": NotRequired[str],
        "KeyBlockHeaders": NotRequired[KeyBlockHeadersTypeDef],
    },
)
ListKeysOutputTypeDef = TypedDict(
    "ListKeysOutputTypeDef",
    {
        "Keys": List[KeySummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateKeyOutputTypeDef = TypedDict(
    "CreateKeyOutputTypeDef",
    {
        "Key": KeyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteKeyOutputTypeDef = TypedDict(
    "DeleteKeyOutputTypeDef",
    {
        "Key": KeyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetKeyOutputTypeDef = TypedDict(
    "GetKeyOutputTypeDef",
    {
        "Key": KeyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportKeyOutputTypeDef = TypedDict(
    "ImportKeyOutputTypeDef",
    {
        "Key": KeyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreKeyOutputTypeDef = TypedDict(
    "RestoreKeyOutputTypeDef",
    {
        "Key": KeyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartKeyUsageOutputTypeDef = TypedDict(
    "StartKeyUsageOutputTypeDef",
    {
        "Key": KeyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopKeyUsageOutputTypeDef = TypedDict(
    "StopKeyUsageOutputTypeDef",
    {
        "Key": KeyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportKeyMaterialTypeDef = TypedDict(
    "ImportKeyMaterialTypeDef",
    {
        "RootCertificatePublicKey": NotRequired[RootCertificatePublicKeyTypeDef],
        "TrustedCertificatePublicKey": NotRequired[TrustedCertificatePublicKeyTypeDef],
        "Tr31KeyBlock": NotRequired[ImportTr31KeyBlockTypeDef],
        "Tr34KeyBlock": NotRequired[ImportTr34KeyBlockTypeDef],
        "KeyCryptogram": NotRequired[ImportKeyCryptogramTypeDef],
    },
)
ExportKeyMaterialTypeDef = TypedDict(
    "ExportKeyMaterialTypeDef",
    {
        "Tr31KeyBlock": NotRequired[ExportTr31KeyBlockTypeDef],
        "Tr34KeyBlock": NotRequired[ExportTr34KeyBlockTypeDef],
        "KeyCryptogram": NotRequired[ExportKeyCryptogramTypeDef],
    },
)
ImportKeyInputRequestTypeDef = TypedDict(
    "ImportKeyInputRequestTypeDef",
    {
        "KeyMaterial": ImportKeyMaterialTypeDef,
        "KeyCheckValueAlgorithm": NotRequired[KeyCheckValueAlgorithmType],
        "Enabled": NotRequired[bool],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ExportKeyInputRequestTypeDef = TypedDict(
    "ExportKeyInputRequestTypeDef",
    {
        "KeyMaterial": ExportKeyMaterialTypeDef,
        "ExportKeyIdentifier": str,
        "ExportAttributes": NotRequired[ExportAttributesTypeDef],
    },
)
