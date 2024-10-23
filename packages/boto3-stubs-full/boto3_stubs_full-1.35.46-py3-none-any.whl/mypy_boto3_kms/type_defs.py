"""
Type annotations for kms service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/type_defs/)

Usage::

    ```python
    from mypy_boto3_kms.type_defs import AliasListEntryTypeDef

    data: AliasListEntryTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    AlgorithmSpecType,
    ConnectionErrorCodeTypeType,
    ConnectionStateTypeType,
    CustomerMasterKeySpecType,
    CustomKeyStoreTypeType,
    DataKeyPairSpecType,
    DataKeySpecType,
    EncryptionAlgorithmSpecType,
    ExpirationModelTypeType,
    GrantOperationType,
    KeyManagerTypeType,
    KeySpecType,
    KeyStateType,
    KeyUsageTypeType,
    MacAlgorithmSpecType,
    MessageTypeType,
    MultiRegionKeyTypeType,
    OriginTypeType,
    RotationTypeType,
    SigningAlgorithmSpecType,
    WrappingKeySpecType,
    XksProxyConnectivityTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AliasListEntryTypeDef",
    "BlobTypeDef",
    "CancelKeyDeletionRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "ConnectCustomKeyStoreRequestRequestTypeDef",
    "CreateAliasRequestRequestTypeDef",
    "XksProxyAuthenticationCredentialTypeTypeDef",
    "GrantConstraintsTypeDef",
    "TagTypeDef",
    "XksProxyConfigurationTypeTypeDef",
    "DeleteAliasRequestRequestTypeDef",
    "DeleteCustomKeyStoreRequestRequestTypeDef",
    "DeleteImportedKeyMaterialRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeCustomKeyStoresRequestRequestTypeDef",
    "DescribeKeyRequestRequestTypeDef",
    "DisableKeyRequestRequestTypeDef",
    "DisableKeyRotationRequestRequestTypeDef",
    "DisconnectCustomKeyStoreRequestRequestTypeDef",
    "EnableKeyRequestRequestTypeDef",
    "EnableKeyRotationRequestRequestTypeDef",
    "GenerateDataKeyPairWithoutPlaintextRequestRequestTypeDef",
    "GenerateDataKeyWithoutPlaintextRequestRequestTypeDef",
    "GetKeyPolicyRequestRequestTypeDef",
    "GetKeyRotationStatusRequestRequestTypeDef",
    "GetParametersForImportRequestRequestTypeDef",
    "GetPublicKeyRequestRequestTypeDef",
    "GrantConstraintsOutputTypeDef",
    "TimestampTypeDef",
    "KeyListEntryTypeDef",
    "XksKeyConfigurationTypeTypeDef",
    "ListAliasesRequestRequestTypeDef",
    "ListGrantsRequestRequestTypeDef",
    "ListKeyPoliciesRequestRequestTypeDef",
    "ListKeyRotationsRequestRequestTypeDef",
    "RotationsListEntryTypeDef",
    "ListKeysRequestRequestTypeDef",
    "ListResourceTagsRequestRequestTypeDef",
    "ListRetirableGrantsRequestRequestTypeDef",
    "MultiRegionKeyTypeDef",
    "PutKeyPolicyRequestRequestTypeDef",
    "RetireGrantRequestRequestTypeDef",
    "RevokeGrantRequestRequestTypeDef",
    "RotateKeyOnDemandRequestRequestTypeDef",
    "ScheduleKeyDeletionRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAliasRequestRequestTypeDef",
    "UpdateKeyDescriptionRequestRequestTypeDef",
    "UpdatePrimaryRegionRequestRequestTypeDef",
    "EncryptRequestRequestTypeDef",
    "GenerateMacRequestRequestTypeDef",
    "ReEncryptRequestRequestTypeDef",
    "RecipientInfoTypeDef",
    "SignRequestRequestTypeDef",
    "VerifyMacRequestRequestTypeDef",
    "VerifyRequestRequestTypeDef",
    "CancelKeyDeletionResponseTypeDef",
    "CreateCustomKeyStoreResponseTypeDef",
    "CreateGrantResponseTypeDef",
    "DecryptResponseTypeDef",
    "DeriveSharedSecretResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EncryptResponseTypeDef",
    "GenerateDataKeyPairResponseTypeDef",
    "GenerateDataKeyPairWithoutPlaintextResponseTypeDef",
    "GenerateDataKeyResponseTypeDef",
    "GenerateDataKeyWithoutPlaintextResponseTypeDef",
    "GenerateMacResponseTypeDef",
    "GenerateRandomResponseTypeDef",
    "GetKeyPolicyResponseTypeDef",
    "GetKeyRotationStatusResponseTypeDef",
    "GetParametersForImportResponseTypeDef",
    "GetPublicKeyResponseTypeDef",
    "ListAliasesResponseTypeDef",
    "ListKeyPoliciesResponseTypeDef",
    "ReEncryptResponseTypeDef",
    "RotateKeyOnDemandResponseTypeDef",
    "ScheduleKeyDeletionResponseTypeDef",
    "SignResponseTypeDef",
    "VerifyMacResponseTypeDef",
    "VerifyResponseTypeDef",
    "CreateCustomKeyStoreRequestRequestTypeDef",
    "UpdateCustomKeyStoreRequestRequestTypeDef",
    "CreateGrantRequestRequestTypeDef",
    "CreateKeyRequestRequestTypeDef",
    "ListResourceTagsResponseTypeDef",
    "ReplicateKeyRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CustomKeyStoresListEntryTypeDef",
    "DescribeCustomKeyStoresRequestDescribeCustomKeyStoresPaginateTypeDef",
    "ListAliasesRequestListAliasesPaginateTypeDef",
    "ListGrantsRequestListGrantsPaginateTypeDef",
    "ListKeyPoliciesRequestListKeyPoliciesPaginateTypeDef",
    "ListKeyRotationsRequestListKeyRotationsPaginateTypeDef",
    "ListKeysRequestListKeysPaginateTypeDef",
    "ListResourceTagsRequestListResourceTagsPaginateTypeDef",
    "ListRetirableGrantsRequestListRetirableGrantsPaginateTypeDef",
    "GrantListEntryTypeDef",
    "ImportKeyMaterialRequestRequestTypeDef",
    "ListKeysResponseTypeDef",
    "ListKeyRotationsResponseTypeDef",
    "MultiRegionConfigurationTypeDef",
    "DecryptRequestRequestTypeDef",
    "DeriveSharedSecretRequestRequestTypeDef",
    "GenerateDataKeyPairRequestRequestTypeDef",
    "GenerateDataKeyRequestRequestTypeDef",
    "GenerateRandomRequestRequestTypeDef",
    "DescribeCustomKeyStoresResponseTypeDef",
    "ListGrantsResponseTypeDef",
    "KeyMetadataTypeDef",
    "CreateKeyResponseTypeDef",
    "DescribeKeyResponseTypeDef",
    "ReplicateKeyResponseTypeDef",
)

AliasListEntryTypeDef = TypedDict(
    "AliasListEntryTypeDef",
    {
        "AliasName": NotRequired[str],
        "AliasArn": NotRequired[str],
        "TargetKeyId": NotRequired[str],
        "CreationDate": NotRequired[datetime],
        "LastUpdatedDate": NotRequired[datetime],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
CancelKeyDeletionRequestRequestTypeDef = TypedDict(
    "CancelKeyDeletionRequestRequestTypeDef",
    {
        "KeyId": str,
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
ConnectCustomKeyStoreRequestRequestTypeDef = TypedDict(
    "ConnectCustomKeyStoreRequestRequestTypeDef",
    {
        "CustomKeyStoreId": str,
    },
)
CreateAliasRequestRequestTypeDef = TypedDict(
    "CreateAliasRequestRequestTypeDef",
    {
        "AliasName": str,
        "TargetKeyId": str,
    },
)
XksProxyAuthenticationCredentialTypeTypeDef = TypedDict(
    "XksProxyAuthenticationCredentialTypeTypeDef",
    {
        "AccessKeyId": str,
        "RawSecretAccessKey": str,
    },
)
GrantConstraintsTypeDef = TypedDict(
    "GrantConstraintsTypeDef",
    {
        "EncryptionContextSubset": NotRequired[Mapping[str, str]],
        "EncryptionContextEquals": NotRequired[Mapping[str, str]],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "TagKey": str,
        "TagValue": str,
    },
)
XksProxyConfigurationTypeTypeDef = TypedDict(
    "XksProxyConfigurationTypeTypeDef",
    {
        "Connectivity": NotRequired[XksProxyConnectivityTypeType],
        "AccessKeyId": NotRequired[str],
        "UriEndpoint": NotRequired[str],
        "UriPath": NotRequired[str],
        "VpcEndpointServiceName": NotRequired[str],
    },
)
DeleteAliasRequestRequestTypeDef = TypedDict(
    "DeleteAliasRequestRequestTypeDef",
    {
        "AliasName": str,
    },
)
DeleteCustomKeyStoreRequestRequestTypeDef = TypedDict(
    "DeleteCustomKeyStoreRequestRequestTypeDef",
    {
        "CustomKeyStoreId": str,
    },
)
DeleteImportedKeyMaterialRequestRequestTypeDef = TypedDict(
    "DeleteImportedKeyMaterialRequestRequestTypeDef",
    {
        "KeyId": str,
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
DescribeCustomKeyStoresRequestRequestTypeDef = TypedDict(
    "DescribeCustomKeyStoresRequestRequestTypeDef",
    {
        "CustomKeyStoreId": NotRequired[str],
        "CustomKeyStoreName": NotRequired[str],
        "Limit": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeKeyRequestRequestTypeDef = TypedDict(
    "DescribeKeyRequestRequestTypeDef",
    {
        "KeyId": str,
        "GrantTokens": NotRequired[Sequence[str]],
    },
)
DisableKeyRequestRequestTypeDef = TypedDict(
    "DisableKeyRequestRequestTypeDef",
    {
        "KeyId": str,
    },
)
DisableKeyRotationRequestRequestTypeDef = TypedDict(
    "DisableKeyRotationRequestRequestTypeDef",
    {
        "KeyId": str,
    },
)
DisconnectCustomKeyStoreRequestRequestTypeDef = TypedDict(
    "DisconnectCustomKeyStoreRequestRequestTypeDef",
    {
        "CustomKeyStoreId": str,
    },
)
EnableKeyRequestRequestTypeDef = TypedDict(
    "EnableKeyRequestRequestTypeDef",
    {
        "KeyId": str,
    },
)
EnableKeyRotationRequestRequestTypeDef = TypedDict(
    "EnableKeyRotationRequestRequestTypeDef",
    {
        "KeyId": str,
        "RotationPeriodInDays": NotRequired[int],
    },
)
GenerateDataKeyPairWithoutPlaintextRequestRequestTypeDef = TypedDict(
    "GenerateDataKeyPairWithoutPlaintextRequestRequestTypeDef",
    {
        "KeyId": str,
        "KeyPairSpec": DataKeyPairSpecType,
        "EncryptionContext": NotRequired[Mapping[str, str]],
        "GrantTokens": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)
GenerateDataKeyWithoutPlaintextRequestRequestTypeDef = TypedDict(
    "GenerateDataKeyWithoutPlaintextRequestRequestTypeDef",
    {
        "KeyId": str,
        "EncryptionContext": NotRequired[Mapping[str, str]],
        "KeySpec": NotRequired[DataKeySpecType],
        "NumberOfBytes": NotRequired[int],
        "GrantTokens": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)
GetKeyPolicyRequestRequestTypeDef = TypedDict(
    "GetKeyPolicyRequestRequestTypeDef",
    {
        "KeyId": str,
        "PolicyName": NotRequired[str],
    },
)
GetKeyRotationStatusRequestRequestTypeDef = TypedDict(
    "GetKeyRotationStatusRequestRequestTypeDef",
    {
        "KeyId": str,
    },
)
GetParametersForImportRequestRequestTypeDef = TypedDict(
    "GetParametersForImportRequestRequestTypeDef",
    {
        "KeyId": str,
        "WrappingAlgorithm": AlgorithmSpecType,
        "WrappingKeySpec": WrappingKeySpecType,
    },
)
GetPublicKeyRequestRequestTypeDef = TypedDict(
    "GetPublicKeyRequestRequestTypeDef",
    {
        "KeyId": str,
        "GrantTokens": NotRequired[Sequence[str]],
    },
)
GrantConstraintsOutputTypeDef = TypedDict(
    "GrantConstraintsOutputTypeDef",
    {
        "EncryptionContextSubset": NotRequired[Dict[str, str]],
        "EncryptionContextEquals": NotRequired[Dict[str, str]],
    },
)
TimestampTypeDef = Union[datetime, str]
KeyListEntryTypeDef = TypedDict(
    "KeyListEntryTypeDef",
    {
        "KeyId": NotRequired[str],
        "KeyArn": NotRequired[str],
    },
)
XksKeyConfigurationTypeTypeDef = TypedDict(
    "XksKeyConfigurationTypeTypeDef",
    {
        "Id": NotRequired[str],
    },
)
ListAliasesRequestRequestTypeDef = TypedDict(
    "ListAliasesRequestRequestTypeDef",
    {
        "KeyId": NotRequired[str],
        "Limit": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
ListGrantsRequestRequestTypeDef = TypedDict(
    "ListGrantsRequestRequestTypeDef",
    {
        "KeyId": str,
        "Limit": NotRequired[int],
        "Marker": NotRequired[str],
        "GrantId": NotRequired[str],
        "GranteePrincipal": NotRequired[str],
    },
)
ListKeyPoliciesRequestRequestTypeDef = TypedDict(
    "ListKeyPoliciesRequestRequestTypeDef",
    {
        "KeyId": str,
        "Limit": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
ListKeyRotationsRequestRequestTypeDef = TypedDict(
    "ListKeyRotationsRequestRequestTypeDef",
    {
        "KeyId": str,
        "Limit": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
RotationsListEntryTypeDef = TypedDict(
    "RotationsListEntryTypeDef",
    {
        "KeyId": NotRequired[str],
        "RotationDate": NotRequired[datetime],
        "RotationType": NotRequired[RotationTypeType],
    },
)
ListKeysRequestRequestTypeDef = TypedDict(
    "ListKeysRequestRequestTypeDef",
    {
        "Limit": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
ListResourceTagsRequestRequestTypeDef = TypedDict(
    "ListResourceTagsRequestRequestTypeDef",
    {
        "KeyId": str,
        "Limit": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
ListRetirableGrantsRequestRequestTypeDef = TypedDict(
    "ListRetirableGrantsRequestRequestTypeDef",
    {
        "RetiringPrincipal": str,
        "Limit": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
MultiRegionKeyTypeDef = TypedDict(
    "MultiRegionKeyTypeDef",
    {
        "Arn": NotRequired[str],
        "Region": NotRequired[str],
    },
)
PutKeyPolicyRequestRequestTypeDef = TypedDict(
    "PutKeyPolicyRequestRequestTypeDef",
    {
        "KeyId": str,
        "Policy": str,
        "PolicyName": NotRequired[str],
        "BypassPolicyLockoutSafetyCheck": NotRequired[bool],
    },
)
RetireGrantRequestRequestTypeDef = TypedDict(
    "RetireGrantRequestRequestTypeDef",
    {
        "GrantToken": NotRequired[str],
        "KeyId": NotRequired[str],
        "GrantId": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
RevokeGrantRequestRequestTypeDef = TypedDict(
    "RevokeGrantRequestRequestTypeDef",
    {
        "KeyId": str,
        "GrantId": str,
        "DryRun": NotRequired[bool],
    },
)
RotateKeyOnDemandRequestRequestTypeDef = TypedDict(
    "RotateKeyOnDemandRequestRequestTypeDef",
    {
        "KeyId": str,
    },
)
ScheduleKeyDeletionRequestRequestTypeDef = TypedDict(
    "ScheduleKeyDeletionRequestRequestTypeDef",
    {
        "KeyId": str,
        "PendingWindowInDays": NotRequired[int],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "KeyId": str,
        "TagKeys": Sequence[str],
    },
)
UpdateAliasRequestRequestTypeDef = TypedDict(
    "UpdateAliasRequestRequestTypeDef",
    {
        "AliasName": str,
        "TargetKeyId": str,
    },
)
UpdateKeyDescriptionRequestRequestTypeDef = TypedDict(
    "UpdateKeyDescriptionRequestRequestTypeDef",
    {
        "KeyId": str,
        "Description": str,
    },
)
UpdatePrimaryRegionRequestRequestTypeDef = TypedDict(
    "UpdatePrimaryRegionRequestRequestTypeDef",
    {
        "KeyId": str,
        "PrimaryRegion": str,
    },
)
EncryptRequestRequestTypeDef = TypedDict(
    "EncryptRequestRequestTypeDef",
    {
        "KeyId": str,
        "Plaintext": BlobTypeDef,
        "EncryptionContext": NotRequired[Mapping[str, str]],
        "GrantTokens": NotRequired[Sequence[str]],
        "EncryptionAlgorithm": NotRequired[EncryptionAlgorithmSpecType],
        "DryRun": NotRequired[bool],
    },
)
GenerateMacRequestRequestTypeDef = TypedDict(
    "GenerateMacRequestRequestTypeDef",
    {
        "Message": BlobTypeDef,
        "KeyId": str,
        "MacAlgorithm": MacAlgorithmSpecType,
        "GrantTokens": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)
ReEncryptRequestRequestTypeDef = TypedDict(
    "ReEncryptRequestRequestTypeDef",
    {
        "CiphertextBlob": BlobTypeDef,
        "DestinationKeyId": str,
        "SourceEncryptionContext": NotRequired[Mapping[str, str]],
        "SourceKeyId": NotRequired[str],
        "DestinationEncryptionContext": NotRequired[Mapping[str, str]],
        "SourceEncryptionAlgorithm": NotRequired[EncryptionAlgorithmSpecType],
        "DestinationEncryptionAlgorithm": NotRequired[EncryptionAlgorithmSpecType],
        "GrantTokens": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)
RecipientInfoTypeDef = TypedDict(
    "RecipientInfoTypeDef",
    {
        "KeyEncryptionAlgorithm": NotRequired[Literal["RSAES_OAEP_SHA_256"]],
        "AttestationDocument": NotRequired[BlobTypeDef],
    },
)
SignRequestRequestTypeDef = TypedDict(
    "SignRequestRequestTypeDef",
    {
        "KeyId": str,
        "Message": BlobTypeDef,
        "SigningAlgorithm": SigningAlgorithmSpecType,
        "MessageType": NotRequired[MessageTypeType],
        "GrantTokens": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)
VerifyMacRequestRequestTypeDef = TypedDict(
    "VerifyMacRequestRequestTypeDef",
    {
        "Message": BlobTypeDef,
        "KeyId": str,
        "MacAlgorithm": MacAlgorithmSpecType,
        "Mac": BlobTypeDef,
        "GrantTokens": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)
VerifyRequestRequestTypeDef = TypedDict(
    "VerifyRequestRequestTypeDef",
    {
        "KeyId": str,
        "Message": BlobTypeDef,
        "Signature": BlobTypeDef,
        "SigningAlgorithm": SigningAlgorithmSpecType,
        "MessageType": NotRequired[MessageTypeType],
        "GrantTokens": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
    },
)
CancelKeyDeletionResponseTypeDef = TypedDict(
    "CancelKeyDeletionResponseTypeDef",
    {
        "KeyId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCustomKeyStoreResponseTypeDef = TypedDict(
    "CreateCustomKeyStoreResponseTypeDef",
    {
        "CustomKeyStoreId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGrantResponseTypeDef = TypedDict(
    "CreateGrantResponseTypeDef",
    {
        "GrantToken": str,
        "GrantId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DecryptResponseTypeDef = TypedDict(
    "DecryptResponseTypeDef",
    {
        "KeyId": str,
        "Plaintext": bytes,
        "EncryptionAlgorithm": EncryptionAlgorithmSpecType,
        "CiphertextForRecipient": bytes,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeriveSharedSecretResponseTypeDef = TypedDict(
    "DeriveSharedSecretResponseTypeDef",
    {
        "KeyId": str,
        "SharedSecret": bytes,
        "CiphertextForRecipient": bytes,
        "KeyAgreementAlgorithm": Literal["ECDH"],
        "KeyOrigin": OriginTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EncryptResponseTypeDef = TypedDict(
    "EncryptResponseTypeDef",
    {
        "CiphertextBlob": bytes,
        "KeyId": str,
        "EncryptionAlgorithm": EncryptionAlgorithmSpecType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GenerateDataKeyPairResponseTypeDef = TypedDict(
    "GenerateDataKeyPairResponseTypeDef",
    {
        "PrivateKeyCiphertextBlob": bytes,
        "PrivateKeyPlaintext": bytes,
        "PublicKey": bytes,
        "KeyId": str,
        "KeyPairSpec": DataKeyPairSpecType,
        "CiphertextForRecipient": bytes,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GenerateDataKeyPairWithoutPlaintextResponseTypeDef = TypedDict(
    "GenerateDataKeyPairWithoutPlaintextResponseTypeDef",
    {
        "PrivateKeyCiphertextBlob": bytes,
        "PublicKey": bytes,
        "KeyId": str,
        "KeyPairSpec": DataKeyPairSpecType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GenerateDataKeyResponseTypeDef = TypedDict(
    "GenerateDataKeyResponseTypeDef",
    {
        "CiphertextBlob": bytes,
        "Plaintext": bytes,
        "KeyId": str,
        "CiphertextForRecipient": bytes,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GenerateDataKeyWithoutPlaintextResponseTypeDef = TypedDict(
    "GenerateDataKeyWithoutPlaintextResponseTypeDef",
    {
        "CiphertextBlob": bytes,
        "KeyId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GenerateMacResponseTypeDef = TypedDict(
    "GenerateMacResponseTypeDef",
    {
        "Mac": bytes,
        "MacAlgorithm": MacAlgorithmSpecType,
        "KeyId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GenerateRandomResponseTypeDef = TypedDict(
    "GenerateRandomResponseTypeDef",
    {
        "Plaintext": bytes,
        "CiphertextForRecipient": bytes,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetKeyPolicyResponseTypeDef = TypedDict(
    "GetKeyPolicyResponseTypeDef",
    {
        "Policy": str,
        "PolicyName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetKeyRotationStatusResponseTypeDef = TypedDict(
    "GetKeyRotationStatusResponseTypeDef",
    {
        "KeyRotationEnabled": bool,
        "KeyId": str,
        "RotationPeriodInDays": int,
        "NextRotationDate": datetime,
        "OnDemandRotationStartDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetParametersForImportResponseTypeDef = TypedDict(
    "GetParametersForImportResponseTypeDef",
    {
        "KeyId": str,
        "ImportToken": bytes,
        "PublicKey": bytes,
        "ParametersValidTo": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPublicKeyResponseTypeDef = TypedDict(
    "GetPublicKeyResponseTypeDef",
    {
        "KeyId": str,
        "PublicKey": bytes,
        "CustomerMasterKeySpec": CustomerMasterKeySpecType,
        "KeySpec": KeySpecType,
        "KeyUsage": KeyUsageTypeType,
        "EncryptionAlgorithms": List[EncryptionAlgorithmSpecType],
        "SigningAlgorithms": List[SigningAlgorithmSpecType],
        "KeyAgreementAlgorithms": List[Literal["ECDH"]],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAliasesResponseTypeDef = TypedDict(
    "ListAliasesResponseTypeDef",
    {
        "Aliases": List[AliasListEntryTypeDef],
        "NextMarker": str,
        "Truncated": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListKeyPoliciesResponseTypeDef = TypedDict(
    "ListKeyPoliciesResponseTypeDef",
    {
        "PolicyNames": List[str],
        "NextMarker": str,
        "Truncated": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReEncryptResponseTypeDef = TypedDict(
    "ReEncryptResponseTypeDef",
    {
        "CiphertextBlob": bytes,
        "SourceKeyId": str,
        "KeyId": str,
        "SourceEncryptionAlgorithm": EncryptionAlgorithmSpecType,
        "DestinationEncryptionAlgorithm": EncryptionAlgorithmSpecType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RotateKeyOnDemandResponseTypeDef = TypedDict(
    "RotateKeyOnDemandResponseTypeDef",
    {
        "KeyId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ScheduleKeyDeletionResponseTypeDef = TypedDict(
    "ScheduleKeyDeletionResponseTypeDef",
    {
        "KeyId": str,
        "DeletionDate": datetime,
        "KeyState": KeyStateType,
        "PendingWindowInDays": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SignResponseTypeDef = TypedDict(
    "SignResponseTypeDef",
    {
        "KeyId": str,
        "Signature": bytes,
        "SigningAlgorithm": SigningAlgorithmSpecType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VerifyMacResponseTypeDef = TypedDict(
    "VerifyMacResponseTypeDef",
    {
        "KeyId": str,
        "MacValid": bool,
        "MacAlgorithm": MacAlgorithmSpecType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VerifyResponseTypeDef = TypedDict(
    "VerifyResponseTypeDef",
    {
        "KeyId": str,
        "SignatureValid": bool,
        "SigningAlgorithm": SigningAlgorithmSpecType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCustomKeyStoreRequestRequestTypeDef = TypedDict(
    "CreateCustomKeyStoreRequestRequestTypeDef",
    {
        "CustomKeyStoreName": str,
        "CloudHsmClusterId": NotRequired[str],
        "TrustAnchorCertificate": NotRequired[str],
        "KeyStorePassword": NotRequired[str],
        "CustomKeyStoreType": NotRequired[CustomKeyStoreTypeType],
        "XksProxyUriEndpoint": NotRequired[str],
        "XksProxyUriPath": NotRequired[str],
        "XksProxyVpcEndpointServiceName": NotRequired[str],
        "XksProxyAuthenticationCredential": NotRequired[
            XksProxyAuthenticationCredentialTypeTypeDef
        ],
        "XksProxyConnectivity": NotRequired[XksProxyConnectivityTypeType],
    },
)
UpdateCustomKeyStoreRequestRequestTypeDef = TypedDict(
    "UpdateCustomKeyStoreRequestRequestTypeDef",
    {
        "CustomKeyStoreId": str,
        "NewCustomKeyStoreName": NotRequired[str],
        "KeyStorePassword": NotRequired[str],
        "CloudHsmClusterId": NotRequired[str],
        "XksProxyUriEndpoint": NotRequired[str],
        "XksProxyUriPath": NotRequired[str],
        "XksProxyVpcEndpointServiceName": NotRequired[str],
        "XksProxyAuthenticationCredential": NotRequired[
            XksProxyAuthenticationCredentialTypeTypeDef
        ],
        "XksProxyConnectivity": NotRequired[XksProxyConnectivityTypeType],
    },
)
CreateGrantRequestRequestTypeDef = TypedDict(
    "CreateGrantRequestRequestTypeDef",
    {
        "KeyId": str,
        "GranteePrincipal": str,
        "Operations": Sequence[GrantOperationType],
        "RetiringPrincipal": NotRequired[str],
        "Constraints": NotRequired[GrantConstraintsTypeDef],
        "GrantTokens": NotRequired[Sequence[str]],
        "Name": NotRequired[str],
        "DryRun": NotRequired[bool],
    },
)
CreateKeyRequestRequestTypeDef = TypedDict(
    "CreateKeyRequestRequestTypeDef",
    {
        "Policy": NotRequired[str],
        "Description": NotRequired[str],
        "KeyUsage": NotRequired[KeyUsageTypeType],
        "CustomerMasterKeySpec": NotRequired[CustomerMasterKeySpecType],
        "KeySpec": NotRequired[KeySpecType],
        "Origin": NotRequired[OriginTypeType],
        "CustomKeyStoreId": NotRequired[str],
        "BypassPolicyLockoutSafetyCheck": NotRequired[bool],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "MultiRegion": NotRequired[bool],
        "XksKeyId": NotRequired[str],
    },
)
ListResourceTagsResponseTypeDef = TypedDict(
    "ListResourceTagsResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "NextMarker": str,
        "Truncated": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReplicateKeyRequestRequestTypeDef = TypedDict(
    "ReplicateKeyRequestRequestTypeDef",
    {
        "KeyId": str,
        "ReplicaRegion": str,
        "Policy": NotRequired[str],
        "BypassPolicyLockoutSafetyCheck": NotRequired[bool],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "KeyId": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CustomKeyStoresListEntryTypeDef = TypedDict(
    "CustomKeyStoresListEntryTypeDef",
    {
        "CustomKeyStoreId": NotRequired[str],
        "CustomKeyStoreName": NotRequired[str],
        "CloudHsmClusterId": NotRequired[str],
        "TrustAnchorCertificate": NotRequired[str],
        "ConnectionState": NotRequired[ConnectionStateTypeType],
        "ConnectionErrorCode": NotRequired[ConnectionErrorCodeTypeType],
        "CreationDate": NotRequired[datetime],
        "CustomKeyStoreType": NotRequired[CustomKeyStoreTypeType],
        "XksProxyConfiguration": NotRequired[XksProxyConfigurationTypeTypeDef],
    },
)
DescribeCustomKeyStoresRequestDescribeCustomKeyStoresPaginateTypeDef = TypedDict(
    "DescribeCustomKeyStoresRequestDescribeCustomKeyStoresPaginateTypeDef",
    {
        "CustomKeyStoreId": NotRequired[str],
        "CustomKeyStoreName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAliasesRequestListAliasesPaginateTypeDef = TypedDict(
    "ListAliasesRequestListAliasesPaginateTypeDef",
    {
        "KeyId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGrantsRequestListGrantsPaginateTypeDef = TypedDict(
    "ListGrantsRequestListGrantsPaginateTypeDef",
    {
        "KeyId": str,
        "GrantId": NotRequired[str],
        "GranteePrincipal": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListKeyPoliciesRequestListKeyPoliciesPaginateTypeDef = TypedDict(
    "ListKeyPoliciesRequestListKeyPoliciesPaginateTypeDef",
    {
        "KeyId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListKeyRotationsRequestListKeyRotationsPaginateTypeDef = TypedDict(
    "ListKeyRotationsRequestListKeyRotationsPaginateTypeDef",
    {
        "KeyId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListKeysRequestListKeysPaginateTypeDef = TypedDict(
    "ListKeysRequestListKeysPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResourceTagsRequestListResourceTagsPaginateTypeDef = TypedDict(
    "ListResourceTagsRequestListResourceTagsPaginateTypeDef",
    {
        "KeyId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRetirableGrantsRequestListRetirableGrantsPaginateTypeDef = TypedDict(
    "ListRetirableGrantsRequestListRetirableGrantsPaginateTypeDef",
    {
        "RetiringPrincipal": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GrantListEntryTypeDef = TypedDict(
    "GrantListEntryTypeDef",
    {
        "KeyId": NotRequired[str],
        "GrantId": NotRequired[str],
        "Name": NotRequired[str],
        "CreationDate": NotRequired[datetime],
        "GranteePrincipal": NotRequired[str],
        "RetiringPrincipal": NotRequired[str],
        "IssuingAccount": NotRequired[str],
        "Operations": NotRequired[List[GrantOperationType]],
        "Constraints": NotRequired[GrantConstraintsOutputTypeDef],
    },
)
ImportKeyMaterialRequestRequestTypeDef = TypedDict(
    "ImportKeyMaterialRequestRequestTypeDef",
    {
        "KeyId": str,
        "ImportToken": BlobTypeDef,
        "EncryptedKeyMaterial": BlobTypeDef,
        "ValidTo": NotRequired[TimestampTypeDef],
        "ExpirationModel": NotRequired[ExpirationModelTypeType],
    },
)
ListKeysResponseTypeDef = TypedDict(
    "ListKeysResponseTypeDef",
    {
        "Keys": List[KeyListEntryTypeDef],
        "NextMarker": str,
        "Truncated": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListKeyRotationsResponseTypeDef = TypedDict(
    "ListKeyRotationsResponseTypeDef",
    {
        "Rotations": List[RotationsListEntryTypeDef],
        "NextMarker": str,
        "Truncated": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MultiRegionConfigurationTypeDef = TypedDict(
    "MultiRegionConfigurationTypeDef",
    {
        "MultiRegionKeyType": NotRequired[MultiRegionKeyTypeType],
        "PrimaryKey": NotRequired[MultiRegionKeyTypeDef],
        "ReplicaKeys": NotRequired[List[MultiRegionKeyTypeDef]],
    },
)
DecryptRequestRequestTypeDef = TypedDict(
    "DecryptRequestRequestTypeDef",
    {
        "CiphertextBlob": BlobTypeDef,
        "EncryptionContext": NotRequired[Mapping[str, str]],
        "GrantTokens": NotRequired[Sequence[str]],
        "KeyId": NotRequired[str],
        "EncryptionAlgorithm": NotRequired[EncryptionAlgorithmSpecType],
        "Recipient": NotRequired[RecipientInfoTypeDef],
        "DryRun": NotRequired[bool],
    },
)
DeriveSharedSecretRequestRequestTypeDef = TypedDict(
    "DeriveSharedSecretRequestRequestTypeDef",
    {
        "KeyId": str,
        "KeyAgreementAlgorithm": Literal["ECDH"],
        "PublicKey": BlobTypeDef,
        "GrantTokens": NotRequired[Sequence[str]],
        "DryRun": NotRequired[bool],
        "Recipient": NotRequired[RecipientInfoTypeDef],
    },
)
GenerateDataKeyPairRequestRequestTypeDef = TypedDict(
    "GenerateDataKeyPairRequestRequestTypeDef",
    {
        "KeyId": str,
        "KeyPairSpec": DataKeyPairSpecType,
        "EncryptionContext": NotRequired[Mapping[str, str]],
        "GrantTokens": NotRequired[Sequence[str]],
        "Recipient": NotRequired[RecipientInfoTypeDef],
        "DryRun": NotRequired[bool],
    },
)
GenerateDataKeyRequestRequestTypeDef = TypedDict(
    "GenerateDataKeyRequestRequestTypeDef",
    {
        "KeyId": str,
        "EncryptionContext": NotRequired[Mapping[str, str]],
        "NumberOfBytes": NotRequired[int],
        "KeySpec": NotRequired[DataKeySpecType],
        "GrantTokens": NotRequired[Sequence[str]],
        "Recipient": NotRequired[RecipientInfoTypeDef],
        "DryRun": NotRequired[bool],
    },
)
GenerateRandomRequestRequestTypeDef = TypedDict(
    "GenerateRandomRequestRequestTypeDef",
    {
        "NumberOfBytes": NotRequired[int],
        "CustomKeyStoreId": NotRequired[str],
        "Recipient": NotRequired[RecipientInfoTypeDef],
    },
)
DescribeCustomKeyStoresResponseTypeDef = TypedDict(
    "DescribeCustomKeyStoresResponseTypeDef",
    {
        "CustomKeyStores": List[CustomKeyStoresListEntryTypeDef],
        "NextMarker": str,
        "Truncated": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListGrantsResponseTypeDef = TypedDict(
    "ListGrantsResponseTypeDef",
    {
        "Grants": List[GrantListEntryTypeDef],
        "NextMarker": str,
        "Truncated": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
KeyMetadataTypeDef = TypedDict(
    "KeyMetadataTypeDef",
    {
        "KeyId": str,
        "AWSAccountId": NotRequired[str],
        "Arn": NotRequired[str],
        "CreationDate": NotRequired[datetime],
        "Enabled": NotRequired[bool],
        "Description": NotRequired[str],
        "KeyUsage": NotRequired[KeyUsageTypeType],
        "KeyState": NotRequired[KeyStateType],
        "DeletionDate": NotRequired[datetime],
        "ValidTo": NotRequired[datetime],
        "Origin": NotRequired[OriginTypeType],
        "CustomKeyStoreId": NotRequired[str],
        "CloudHsmClusterId": NotRequired[str],
        "ExpirationModel": NotRequired[ExpirationModelTypeType],
        "KeyManager": NotRequired[KeyManagerTypeType],
        "CustomerMasterKeySpec": NotRequired[CustomerMasterKeySpecType],
        "KeySpec": NotRequired[KeySpecType],
        "EncryptionAlgorithms": NotRequired[List[EncryptionAlgorithmSpecType]],
        "SigningAlgorithms": NotRequired[List[SigningAlgorithmSpecType]],
        "KeyAgreementAlgorithms": NotRequired[List[Literal["ECDH"]]],
        "MultiRegion": NotRequired[bool],
        "MultiRegionConfiguration": NotRequired[MultiRegionConfigurationTypeDef],
        "PendingDeletionWindowInDays": NotRequired[int],
        "MacAlgorithms": NotRequired[List[MacAlgorithmSpecType]],
        "XksKeyConfiguration": NotRequired[XksKeyConfigurationTypeTypeDef],
    },
)
CreateKeyResponseTypeDef = TypedDict(
    "CreateKeyResponseTypeDef",
    {
        "KeyMetadata": KeyMetadataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeKeyResponseTypeDef = TypedDict(
    "DescribeKeyResponseTypeDef",
    {
        "KeyMetadata": KeyMetadataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReplicateKeyResponseTypeDef = TypedDict(
    "ReplicateKeyResponseTypeDef",
    {
        "ReplicaKeyMetadata": KeyMetadataTypeDef,
        "ReplicaPolicy": str,
        "ReplicaTags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
