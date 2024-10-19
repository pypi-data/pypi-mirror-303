"""
Type annotations for glacier service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glacier/type_defs/)

Usage::

    ```python
    from mypy_boto3_glacier.type_defs import AbortMultipartUploadInputRequestTypeDef

    data: AbortMultipartUploadInputRequestTypeDef = ...
    ```
"""

import sys
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    ActionCodeType,
    CannedACLType,
    EncryptionTypeType,
    FileHeaderInfoType,
    PermissionType,
    QuoteFieldsType,
    StatusCodeType,
    StorageClassType,
    TypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AbortMultipartUploadInputRequestTypeDef",
    "AbortVaultLockInputRequestTypeDef",
    "AddTagsToVaultInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "BlobTypeDef",
    "CSVInputTypeDef",
    "CSVOutputTypeDef",
    "CompleteMultipartUploadInputMultipartUploadCompleteTypeDef",
    "CompleteMultipartUploadInputRequestTypeDef",
    "CompleteVaultLockInputRequestTypeDef",
    "CreateVaultInputAccountCreateVaultTypeDef",
    "CreateVaultInputRequestTypeDef",
    "CreateVaultInputServiceResourceCreateVaultTypeDef",
    "DataRetrievalRuleTypeDef",
    "DeleteArchiveInputRequestTypeDef",
    "DeleteVaultAccessPolicyInputRequestTypeDef",
    "DeleteVaultInputRequestTypeDef",
    "DeleteVaultNotificationsInputRequestTypeDef",
    "DescribeJobInputRequestTypeDef",
    "DescribeVaultInputRequestTypeDef",
    "WaiterConfigTypeDef",
    "DescribeVaultOutputTypeDef",
    "EncryptionTypeDef",
    "GetDataRetrievalPolicyInputRequestTypeDef",
    "GetJobOutputInputJobGetOutputTypeDef",
    "GetJobOutputInputRequestTypeDef",
    "GetVaultAccessPolicyInputRequestTypeDef",
    "VaultAccessPolicyTypeDef",
    "GetVaultLockInputRequestTypeDef",
    "GetVaultNotificationsInputRequestTypeDef",
    "VaultNotificationConfigOutputTypeDef",
    "InventoryRetrievalJobDescriptionTypeDef",
    "GranteeTypeDef",
    "InitiateMultipartUploadInputRequestTypeDef",
    "InitiateMultipartUploadInputVaultInitiateMultipartUploadTypeDef",
    "VaultLockPolicyTypeDef",
    "InventoryRetrievalJobInputTypeDef",
    "PaginatorConfigTypeDef",
    "ListJobsInputRequestTypeDef",
    "ListMultipartUploadsInputRequestTypeDef",
    "UploadListElementTypeDef",
    "ListPartsInputMultipartUploadPartsTypeDef",
    "ListPartsInputRequestTypeDef",
    "PartListElementTypeDef",
    "ListProvisionedCapacityInputRequestTypeDef",
    "ProvisionedCapacityDescriptionTypeDef",
    "ListTagsForVaultInputRequestTypeDef",
    "ListVaultsInputRequestTypeDef",
    "PurchaseProvisionedCapacityInputRequestTypeDef",
    "RemoveTagsFromVaultInputRequestTypeDef",
    "VaultNotificationConfigTypeDef",
    "ArchiveCreationOutputTypeDef",
    "CreateVaultOutputTypeDef",
    "DescribeVaultResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetJobOutputOutputTypeDef",
    "GetVaultLockOutputTypeDef",
    "InitiateJobOutputTypeDef",
    "InitiateMultipartUploadOutputTypeDef",
    "InitiateVaultLockOutputTypeDef",
    "ListTagsForVaultOutputTypeDef",
    "PurchaseProvisionedCapacityOutputTypeDef",
    "UploadMultipartPartOutputTypeDef",
    "UploadArchiveInputRequestTypeDef",
    "UploadArchiveInputVaultUploadArchiveTypeDef",
    "UploadMultipartPartInputMultipartUploadUploadPartTypeDef",
    "UploadMultipartPartInputRequestTypeDef",
    "InputSerializationTypeDef",
    "OutputSerializationTypeDef",
    "DataRetrievalPolicyOutputTypeDef",
    "DataRetrievalPolicyTypeDef",
    "DescribeVaultInputVaultExistsWaitTypeDef",
    "DescribeVaultInputVaultNotExistsWaitTypeDef",
    "ListVaultsOutputTypeDef",
    "GetVaultAccessPolicyOutputTypeDef",
    "SetVaultAccessPolicyInputRequestTypeDef",
    "GetVaultNotificationsOutputTypeDef",
    "GrantTypeDef",
    "InitiateVaultLockInputRequestTypeDef",
    "ListJobsInputListJobsPaginateTypeDef",
    "ListMultipartUploadsInputListMultipartUploadsPaginateTypeDef",
    "ListPartsInputListPartsPaginateTypeDef",
    "ListVaultsInputListVaultsPaginateTypeDef",
    "ListMultipartUploadsOutputTypeDef",
    "ListPartsOutputTypeDef",
    "ListProvisionedCapacityOutputTypeDef",
    "SetVaultNotificationsInputNotificationSetTypeDef",
    "SetVaultNotificationsInputRequestTypeDef",
    "SelectParametersTypeDef",
    "GetDataRetrievalPolicyOutputTypeDef",
    "SetDataRetrievalPolicyInputRequestTypeDef",
    "S3LocationOutputTypeDef",
    "S3LocationTypeDef",
    "OutputLocationOutputTypeDef",
    "S3LocationUnionTypeDef",
    "GlacierJobDescriptionResponseTypeDef",
    "GlacierJobDescriptionTypeDef",
    "OutputLocationTypeDef",
    "ListJobsOutputTypeDef",
    "OutputLocationUnionTypeDef",
    "JobParametersTypeDef",
    "InitiateJobInputRequestTypeDef",
)

AbortMultipartUploadInputRequestTypeDef = TypedDict(
    "AbortMultipartUploadInputRequestTypeDef",
    {
        "vaultName": str,
        "uploadId": str,
        "accountId": NotRequired[str],
    },
)
AbortVaultLockInputRequestTypeDef = TypedDict(
    "AbortVaultLockInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
    },
)
AddTagsToVaultInputRequestTypeDef = TypedDict(
    "AddTagsToVaultInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
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
CSVInputTypeDef = TypedDict(
    "CSVInputTypeDef",
    {
        "FileHeaderInfo": NotRequired[FileHeaderInfoType],
        "Comments": NotRequired[str],
        "QuoteEscapeCharacter": NotRequired[str],
        "RecordDelimiter": NotRequired[str],
        "FieldDelimiter": NotRequired[str],
        "QuoteCharacter": NotRequired[str],
    },
)
CSVOutputTypeDef = TypedDict(
    "CSVOutputTypeDef",
    {
        "QuoteFields": NotRequired[QuoteFieldsType],
        "QuoteEscapeCharacter": NotRequired[str],
        "RecordDelimiter": NotRequired[str],
        "FieldDelimiter": NotRequired[str],
        "QuoteCharacter": NotRequired[str],
    },
)
CompleteMultipartUploadInputMultipartUploadCompleteTypeDef = TypedDict(
    "CompleteMultipartUploadInputMultipartUploadCompleteTypeDef",
    {
        "archiveSize": NotRequired[str],
        "checksum": NotRequired[str],
    },
)
CompleteMultipartUploadInputRequestTypeDef = TypedDict(
    "CompleteMultipartUploadInputRequestTypeDef",
    {
        "vaultName": str,
        "uploadId": str,
        "accountId": NotRequired[str],
        "archiveSize": NotRequired[str],
        "checksum": NotRequired[str],
    },
)
CompleteVaultLockInputRequestTypeDef = TypedDict(
    "CompleteVaultLockInputRequestTypeDef",
    {
        "vaultName": str,
        "lockId": str,
        "accountId": NotRequired[str],
    },
)
CreateVaultInputAccountCreateVaultTypeDef = TypedDict(
    "CreateVaultInputAccountCreateVaultTypeDef",
    {
        "vaultName": str,
    },
)
CreateVaultInputRequestTypeDef = TypedDict(
    "CreateVaultInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
    },
)
CreateVaultInputServiceResourceCreateVaultTypeDef = TypedDict(
    "CreateVaultInputServiceResourceCreateVaultTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
    },
)
DataRetrievalRuleTypeDef = TypedDict(
    "DataRetrievalRuleTypeDef",
    {
        "Strategy": NotRequired[str],
        "BytesPerHour": NotRequired[int],
    },
)
DeleteArchiveInputRequestTypeDef = TypedDict(
    "DeleteArchiveInputRequestTypeDef",
    {
        "vaultName": str,
        "archiveId": str,
        "accountId": NotRequired[str],
    },
)
DeleteVaultAccessPolicyInputRequestTypeDef = TypedDict(
    "DeleteVaultAccessPolicyInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
    },
)
DeleteVaultInputRequestTypeDef = TypedDict(
    "DeleteVaultInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
    },
)
DeleteVaultNotificationsInputRequestTypeDef = TypedDict(
    "DeleteVaultNotificationsInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
    },
)
DescribeJobInputRequestTypeDef = TypedDict(
    "DescribeJobInputRequestTypeDef",
    {
        "vaultName": str,
        "jobId": str,
        "accountId": NotRequired[str],
    },
)
DescribeVaultInputRequestTypeDef = TypedDict(
    "DescribeVaultInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
DescribeVaultOutputTypeDef = TypedDict(
    "DescribeVaultOutputTypeDef",
    {
        "VaultARN": NotRequired[str],
        "VaultName": NotRequired[str],
        "CreationDate": NotRequired[str],
        "LastInventoryDate": NotRequired[str],
        "NumberOfArchives": NotRequired[int],
        "SizeInBytes": NotRequired[int],
    },
)
EncryptionTypeDef = TypedDict(
    "EncryptionTypeDef",
    {
        "EncryptionType": NotRequired[EncryptionTypeType],
        "KMSKeyId": NotRequired[str],
        "KMSContext": NotRequired[str],
    },
)
GetDataRetrievalPolicyInputRequestTypeDef = TypedDict(
    "GetDataRetrievalPolicyInputRequestTypeDef",
    {
        "accountId": NotRequired[str],
    },
)
GetJobOutputInputJobGetOutputTypeDef = TypedDict(
    "GetJobOutputInputJobGetOutputTypeDef",
    {
        "range": NotRequired[str],
    },
)
GetJobOutputInputRequestTypeDef = TypedDict(
    "GetJobOutputInputRequestTypeDef",
    {
        "vaultName": str,
        "jobId": str,
        "accountId": NotRequired[str],
        "range": NotRequired[str],
    },
)
GetVaultAccessPolicyInputRequestTypeDef = TypedDict(
    "GetVaultAccessPolicyInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
    },
)
VaultAccessPolicyTypeDef = TypedDict(
    "VaultAccessPolicyTypeDef",
    {
        "Policy": NotRequired[str],
    },
)
GetVaultLockInputRequestTypeDef = TypedDict(
    "GetVaultLockInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
    },
)
GetVaultNotificationsInputRequestTypeDef = TypedDict(
    "GetVaultNotificationsInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
    },
)
VaultNotificationConfigOutputTypeDef = TypedDict(
    "VaultNotificationConfigOutputTypeDef",
    {
        "SNSTopic": NotRequired[str],
        "Events": NotRequired[List[str]],
    },
)
InventoryRetrievalJobDescriptionTypeDef = TypedDict(
    "InventoryRetrievalJobDescriptionTypeDef",
    {
        "Format": NotRequired[str],
        "StartDate": NotRequired[str],
        "EndDate": NotRequired[str],
        "Limit": NotRequired[str],
        "Marker": NotRequired[str],
    },
)
GranteeTypeDef = TypedDict(
    "GranteeTypeDef",
    {
        "Type": TypeType,
        "DisplayName": NotRequired[str],
        "URI": NotRequired[str],
        "ID": NotRequired[str],
        "EmailAddress": NotRequired[str],
    },
)
InitiateMultipartUploadInputRequestTypeDef = TypedDict(
    "InitiateMultipartUploadInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
        "archiveDescription": NotRequired[str],
        "partSize": NotRequired[str],
    },
)
InitiateMultipartUploadInputVaultInitiateMultipartUploadTypeDef = TypedDict(
    "InitiateMultipartUploadInputVaultInitiateMultipartUploadTypeDef",
    {
        "archiveDescription": NotRequired[str],
        "partSize": NotRequired[str],
    },
)
VaultLockPolicyTypeDef = TypedDict(
    "VaultLockPolicyTypeDef",
    {
        "Policy": NotRequired[str],
    },
)
InventoryRetrievalJobInputTypeDef = TypedDict(
    "InventoryRetrievalJobInputTypeDef",
    {
        "StartDate": NotRequired[str],
        "EndDate": NotRequired[str],
        "Limit": NotRequired[str],
        "Marker": NotRequired[str],
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
ListJobsInputRequestTypeDef = TypedDict(
    "ListJobsInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
        "limit": NotRequired[str],
        "marker": NotRequired[str],
        "statuscode": NotRequired[str],
        "completed": NotRequired[str],
    },
)
ListMultipartUploadsInputRequestTypeDef = TypedDict(
    "ListMultipartUploadsInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
        "marker": NotRequired[str],
        "limit": NotRequired[str],
    },
)
UploadListElementTypeDef = TypedDict(
    "UploadListElementTypeDef",
    {
        "MultipartUploadId": NotRequired[str],
        "VaultARN": NotRequired[str],
        "ArchiveDescription": NotRequired[str],
        "PartSizeInBytes": NotRequired[int],
        "CreationDate": NotRequired[str],
    },
)
ListPartsInputMultipartUploadPartsTypeDef = TypedDict(
    "ListPartsInputMultipartUploadPartsTypeDef",
    {
        "marker": NotRequired[str],
        "limit": NotRequired[str],
    },
)
ListPartsInputRequestTypeDef = TypedDict(
    "ListPartsInputRequestTypeDef",
    {
        "vaultName": str,
        "uploadId": str,
        "accountId": NotRequired[str],
        "marker": NotRequired[str],
        "limit": NotRequired[str],
    },
)
PartListElementTypeDef = TypedDict(
    "PartListElementTypeDef",
    {
        "RangeInBytes": NotRequired[str],
        "SHA256TreeHash": NotRequired[str],
    },
)
ListProvisionedCapacityInputRequestTypeDef = TypedDict(
    "ListProvisionedCapacityInputRequestTypeDef",
    {
        "accountId": NotRequired[str],
    },
)
ProvisionedCapacityDescriptionTypeDef = TypedDict(
    "ProvisionedCapacityDescriptionTypeDef",
    {
        "CapacityId": NotRequired[str],
        "StartDate": NotRequired[str],
        "ExpirationDate": NotRequired[str],
    },
)
ListTagsForVaultInputRequestTypeDef = TypedDict(
    "ListTagsForVaultInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
    },
)
ListVaultsInputRequestTypeDef = TypedDict(
    "ListVaultsInputRequestTypeDef",
    {
        "accountId": NotRequired[str],
        "marker": NotRequired[str],
        "limit": NotRequired[str],
    },
)
PurchaseProvisionedCapacityInputRequestTypeDef = TypedDict(
    "PurchaseProvisionedCapacityInputRequestTypeDef",
    {
        "accountId": NotRequired[str],
    },
)
RemoveTagsFromVaultInputRequestTypeDef = TypedDict(
    "RemoveTagsFromVaultInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
        "TagKeys": NotRequired[Sequence[str]],
    },
)
VaultNotificationConfigTypeDef = TypedDict(
    "VaultNotificationConfigTypeDef",
    {
        "SNSTopic": NotRequired[str],
        "Events": NotRequired[Sequence[str]],
    },
)
ArchiveCreationOutputTypeDef = TypedDict(
    "ArchiveCreationOutputTypeDef",
    {
        "location": str,
        "checksum": str,
        "archiveId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateVaultOutputTypeDef = TypedDict(
    "CreateVaultOutputTypeDef",
    {
        "location": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeVaultResponseTypeDef = TypedDict(
    "DescribeVaultResponseTypeDef",
    {
        "VaultARN": str,
        "VaultName": str,
        "CreationDate": str,
        "LastInventoryDate": str,
        "NumberOfArchives": int,
        "SizeInBytes": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetJobOutputOutputTypeDef = TypedDict(
    "GetJobOutputOutputTypeDef",
    {
        "body": StreamingBody,
        "checksum": str,
        "status": int,
        "contentRange": str,
        "acceptRanges": str,
        "contentType": str,
        "archiveDescription": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetVaultLockOutputTypeDef = TypedDict(
    "GetVaultLockOutputTypeDef",
    {
        "Policy": str,
        "State": str,
        "ExpirationDate": str,
        "CreationDate": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InitiateJobOutputTypeDef = TypedDict(
    "InitiateJobOutputTypeDef",
    {
        "location": str,
        "jobId": str,
        "jobOutputPath": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InitiateMultipartUploadOutputTypeDef = TypedDict(
    "InitiateMultipartUploadOutputTypeDef",
    {
        "location": str,
        "uploadId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InitiateVaultLockOutputTypeDef = TypedDict(
    "InitiateVaultLockOutputTypeDef",
    {
        "lockId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForVaultOutputTypeDef = TypedDict(
    "ListTagsForVaultOutputTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PurchaseProvisionedCapacityOutputTypeDef = TypedDict(
    "PurchaseProvisionedCapacityOutputTypeDef",
    {
        "capacityId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UploadMultipartPartOutputTypeDef = TypedDict(
    "UploadMultipartPartOutputTypeDef",
    {
        "checksum": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UploadArchiveInputRequestTypeDef = TypedDict(
    "UploadArchiveInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
        "archiveDescription": NotRequired[str],
        "checksum": NotRequired[str],
        "body": NotRequired[BlobTypeDef],
    },
)
UploadArchiveInputVaultUploadArchiveTypeDef = TypedDict(
    "UploadArchiveInputVaultUploadArchiveTypeDef",
    {
        "archiveDescription": NotRequired[str],
        "checksum": NotRequired[str],
        "body": NotRequired[BlobTypeDef],
    },
)
UploadMultipartPartInputMultipartUploadUploadPartTypeDef = TypedDict(
    "UploadMultipartPartInputMultipartUploadUploadPartTypeDef",
    {
        "checksum": NotRequired[str],
        "range": NotRequired[str],
        "body": NotRequired[BlobTypeDef],
    },
)
UploadMultipartPartInputRequestTypeDef = TypedDict(
    "UploadMultipartPartInputRequestTypeDef",
    {
        "vaultName": str,
        "uploadId": str,
        "accountId": NotRequired[str],
        "checksum": NotRequired[str],
        "range": NotRequired[str],
        "body": NotRequired[BlobTypeDef],
    },
)
InputSerializationTypeDef = TypedDict(
    "InputSerializationTypeDef",
    {
        "csv": NotRequired[CSVInputTypeDef],
    },
)
OutputSerializationTypeDef = TypedDict(
    "OutputSerializationTypeDef",
    {
        "csv": NotRequired[CSVOutputTypeDef],
    },
)
DataRetrievalPolicyOutputTypeDef = TypedDict(
    "DataRetrievalPolicyOutputTypeDef",
    {
        "Rules": NotRequired[List[DataRetrievalRuleTypeDef]],
    },
)
DataRetrievalPolicyTypeDef = TypedDict(
    "DataRetrievalPolicyTypeDef",
    {
        "Rules": NotRequired[Sequence[DataRetrievalRuleTypeDef]],
    },
)
DescribeVaultInputVaultExistsWaitTypeDef = TypedDict(
    "DescribeVaultInputVaultExistsWaitTypeDef",
    {
        "accountId": str,
        "vaultName": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeVaultInputVaultNotExistsWaitTypeDef = TypedDict(
    "DescribeVaultInputVaultNotExistsWaitTypeDef",
    {
        "accountId": str,
        "vaultName": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
ListVaultsOutputTypeDef = TypedDict(
    "ListVaultsOutputTypeDef",
    {
        "VaultList": List[DescribeVaultOutputTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetVaultAccessPolicyOutputTypeDef = TypedDict(
    "GetVaultAccessPolicyOutputTypeDef",
    {
        "policy": VaultAccessPolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SetVaultAccessPolicyInputRequestTypeDef = TypedDict(
    "SetVaultAccessPolicyInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
        "policy": NotRequired[VaultAccessPolicyTypeDef],
    },
)
GetVaultNotificationsOutputTypeDef = TypedDict(
    "GetVaultNotificationsOutputTypeDef",
    {
        "vaultNotificationConfig": VaultNotificationConfigOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GrantTypeDef = TypedDict(
    "GrantTypeDef",
    {
        "Grantee": NotRequired[GranteeTypeDef],
        "Permission": NotRequired[PermissionType],
    },
)
InitiateVaultLockInputRequestTypeDef = TypedDict(
    "InitiateVaultLockInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
        "policy": NotRequired[VaultLockPolicyTypeDef],
    },
)
ListJobsInputListJobsPaginateTypeDef = TypedDict(
    "ListJobsInputListJobsPaginateTypeDef",
    {
        "accountId": str,
        "vaultName": str,
        "statuscode": NotRequired[str],
        "completed": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMultipartUploadsInputListMultipartUploadsPaginateTypeDef = TypedDict(
    "ListMultipartUploadsInputListMultipartUploadsPaginateTypeDef",
    {
        "accountId": str,
        "vaultName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPartsInputListPartsPaginateTypeDef = TypedDict(
    "ListPartsInputListPartsPaginateTypeDef",
    {
        "accountId": str,
        "vaultName": str,
        "uploadId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListVaultsInputListVaultsPaginateTypeDef = TypedDict(
    "ListVaultsInputListVaultsPaginateTypeDef",
    {
        "accountId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMultipartUploadsOutputTypeDef = TypedDict(
    "ListMultipartUploadsOutputTypeDef",
    {
        "UploadsList": List[UploadListElementTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPartsOutputTypeDef = TypedDict(
    "ListPartsOutputTypeDef",
    {
        "MultipartUploadId": str,
        "VaultARN": str,
        "ArchiveDescription": str,
        "PartSizeInBytes": int,
        "CreationDate": str,
        "Parts": List[PartListElementTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListProvisionedCapacityOutputTypeDef = TypedDict(
    "ListProvisionedCapacityOutputTypeDef",
    {
        "ProvisionedCapacityList": List[ProvisionedCapacityDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SetVaultNotificationsInputNotificationSetTypeDef = TypedDict(
    "SetVaultNotificationsInputNotificationSetTypeDef",
    {
        "vaultNotificationConfig": NotRequired[VaultNotificationConfigTypeDef],
    },
)
SetVaultNotificationsInputRequestTypeDef = TypedDict(
    "SetVaultNotificationsInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
        "vaultNotificationConfig": NotRequired[VaultNotificationConfigTypeDef],
    },
)
SelectParametersTypeDef = TypedDict(
    "SelectParametersTypeDef",
    {
        "InputSerialization": NotRequired[InputSerializationTypeDef],
        "ExpressionType": NotRequired[Literal["SQL"]],
        "Expression": NotRequired[str],
        "OutputSerialization": NotRequired[OutputSerializationTypeDef],
    },
)
GetDataRetrievalPolicyOutputTypeDef = TypedDict(
    "GetDataRetrievalPolicyOutputTypeDef",
    {
        "Policy": DataRetrievalPolicyOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SetDataRetrievalPolicyInputRequestTypeDef = TypedDict(
    "SetDataRetrievalPolicyInputRequestTypeDef",
    {
        "accountId": NotRequired[str],
        "Policy": NotRequired[DataRetrievalPolicyTypeDef],
    },
)
S3LocationOutputTypeDef = TypedDict(
    "S3LocationOutputTypeDef",
    {
        "BucketName": NotRequired[str],
        "Prefix": NotRequired[str],
        "Encryption": NotRequired[EncryptionTypeDef],
        "CannedACL": NotRequired[CannedACLType],
        "AccessControlList": NotRequired[List[GrantTypeDef]],
        "Tagging": NotRequired[Dict[str, str]],
        "UserMetadata": NotRequired[Dict[str, str]],
        "StorageClass": NotRequired[StorageClassType],
    },
)
S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "BucketName": NotRequired[str],
        "Prefix": NotRequired[str],
        "Encryption": NotRequired[EncryptionTypeDef],
        "CannedACL": NotRequired[CannedACLType],
        "AccessControlList": NotRequired[Sequence[GrantTypeDef]],
        "Tagging": NotRequired[Mapping[str, str]],
        "UserMetadata": NotRequired[Mapping[str, str]],
        "StorageClass": NotRequired[StorageClassType],
    },
)
OutputLocationOutputTypeDef = TypedDict(
    "OutputLocationOutputTypeDef",
    {
        "S3": NotRequired[S3LocationOutputTypeDef],
    },
)
S3LocationUnionTypeDef = Union[S3LocationTypeDef, S3LocationOutputTypeDef]
GlacierJobDescriptionResponseTypeDef = TypedDict(
    "GlacierJobDescriptionResponseTypeDef",
    {
        "JobId": str,
        "JobDescription": str,
        "Action": ActionCodeType,
        "ArchiveId": str,
        "VaultARN": str,
        "CreationDate": str,
        "Completed": bool,
        "StatusCode": StatusCodeType,
        "StatusMessage": str,
        "ArchiveSizeInBytes": int,
        "InventorySizeInBytes": int,
        "SNSTopic": str,
        "CompletionDate": str,
        "SHA256TreeHash": str,
        "ArchiveSHA256TreeHash": str,
        "RetrievalByteRange": str,
        "Tier": str,
        "InventoryRetrievalParameters": InventoryRetrievalJobDescriptionTypeDef,
        "JobOutputPath": str,
        "SelectParameters": SelectParametersTypeDef,
        "OutputLocation": OutputLocationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GlacierJobDescriptionTypeDef = TypedDict(
    "GlacierJobDescriptionTypeDef",
    {
        "JobId": NotRequired[str],
        "JobDescription": NotRequired[str],
        "Action": NotRequired[ActionCodeType],
        "ArchiveId": NotRequired[str],
        "VaultARN": NotRequired[str],
        "CreationDate": NotRequired[str],
        "Completed": NotRequired[bool],
        "StatusCode": NotRequired[StatusCodeType],
        "StatusMessage": NotRequired[str],
        "ArchiveSizeInBytes": NotRequired[int],
        "InventorySizeInBytes": NotRequired[int],
        "SNSTopic": NotRequired[str],
        "CompletionDate": NotRequired[str],
        "SHA256TreeHash": NotRequired[str],
        "ArchiveSHA256TreeHash": NotRequired[str],
        "RetrievalByteRange": NotRequired[str],
        "Tier": NotRequired[str],
        "InventoryRetrievalParameters": NotRequired[InventoryRetrievalJobDescriptionTypeDef],
        "JobOutputPath": NotRequired[str],
        "SelectParameters": NotRequired[SelectParametersTypeDef],
        "OutputLocation": NotRequired[OutputLocationOutputTypeDef],
    },
)
OutputLocationTypeDef = TypedDict(
    "OutputLocationTypeDef",
    {
        "S3": NotRequired[S3LocationUnionTypeDef],
    },
)
ListJobsOutputTypeDef = TypedDict(
    "ListJobsOutputTypeDef",
    {
        "JobList": List[GlacierJobDescriptionTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OutputLocationUnionTypeDef = Union[OutputLocationTypeDef, OutputLocationOutputTypeDef]
JobParametersTypeDef = TypedDict(
    "JobParametersTypeDef",
    {
        "Format": NotRequired[str],
        "Type": NotRequired[str],
        "ArchiveId": NotRequired[str],
        "Description": NotRequired[str],
        "SNSTopic": NotRequired[str],
        "RetrievalByteRange": NotRequired[str],
        "Tier": NotRequired[str],
        "InventoryRetrievalParameters": NotRequired[InventoryRetrievalJobInputTypeDef],
        "SelectParameters": NotRequired[SelectParametersTypeDef],
        "OutputLocation": NotRequired[OutputLocationUnionTypeDef],
    },
)
InitiateJobInputRequestTypeDef = TypedDict(
    "InitiateJobInputRequestTypeDef",
    {
        "vaultName": str,
        "accountId": NotRequired[str],
        "jobParameters": NotRequired[JobParametersTypeDef],
    },
)
