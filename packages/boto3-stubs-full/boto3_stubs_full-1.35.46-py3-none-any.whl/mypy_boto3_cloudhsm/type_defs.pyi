"""
Type annotations for cloudhsm service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/type_defs/)

Usage::

    ```python
    from mypy_boto3_cloudhsm.type_defs import TagTypeDef

    data: TagTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Sequence

from .literals import ClientVersionType, CloudHsmObjectStateType, HsmStatusType

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "CreateHapgRequestRequestTypeDef",
    "CreateHsmRequestRequestTypeDef",
    "CreateLunaClientRequestRequestTypeDef",
    "DeleteHapgRequestRequestTypeDef",
    "DeleteHsmRequestRequestTypeDef",
    "DeleteLunaClientRequestRequestTypeDef",
    "DescribeHapgRequestRequestTypeDef",
    "DescribeHsmRequestRequestTypeDef",
    "DescribeLunaClientRequestRequestTypeDef",
    "GetConfigRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListHapgsRequestRequestTypeDef",
    "ListHsmsRequestRequestTypeDef",
    "ListLunaClientsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ModifyHapgRequestRequestTypeDef",
    "ModifyHsmRequestRequestTypeDef",
    "ModifyLunaClientRequestRequestTypeDef",
    "RemoveTagsFromResourceRequestRequestTypeDef",
    "AddTagsToResourceRequestRequestTypeDef",
    "AddTagsToResourceResponseTypeDef",
    "CreateHapgResponseTypeDef",
    "CreateHsmResponseTypeDef",
    "CreateLunaClientResponseTypeDef",
    "DeleteHapgResponseTypeDef",
    "DeleteHsmResponseTypeDef",
    "DeleteLunaClientResponseTypeDef",
    "DescribeHapgResponseTypeDef",
    "DescribeHsmResponseTypeDef",
    "DescribeLunaClientResponseTypeDef",
    "GetConfigResponseTypeDef",
    "ListAvailableZonesResponseTypeDef",
    "ListHapgsResponseTypeDef",
    "ListHsmsResponseTypeDef",
    "ListLunaClientsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ModifyHapgResponseTypeDef",
    "ModifyHsmResponseTypeDef",
    "ModifyLunaClientResponseTypeDef",
    "RemoveTagsFromResourceResponseTypeDef",
    "ListHapgsRequestListHapgsPaginateTypeDef",
    "ListHsmsRequestListHsmsPaginateTypeDef",
    "ListLunaClientsRequestListLunaClientsPaginateTypeDef",
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
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
CreateHapgRequestRequestTypeDef = TypedDict(
    "CreateHapgRequestRequestTypeDef",
    {
        "Label": str,
    },
)
CreateHsmRequestRequestTypeDef = TypedDict(
    "CreateHsmRequestRequestTypeDef",
    {
        "SubnetId": str,
        "SshKey": str,
        "IamRoleArn": str,
        "SubscriptionType": Literal["PRODUCTION"],
        "EniIp": NotRequired[str],
        "ExternalId": NotRequired[str],
        "ClientToken": NotRequired[str],
        "SyslogIp": NotRequired[str],
    },
)
CreateLunaClientRequestRequestTypeDef = TypedDict(
    "CreateLunaClientRequestRequestTypeDef",
    {
        "Certificate": str,
        "Label": NotRequired[str],
    },
)
DeleteHapgRequestRequestTypeDef = TypedDict(
    "DeleteHapgRequestRequestTypeDef",
    {
        "HapgArn": str,
    },
)
DeleteHsmRequestRequestTypeDef = TypedDict(
    "DeleteHsmRequestRequestTypeDef",
    {
        "HsmArn": str,
    },
)
DeleteLunaClientRequestRequestTypeDef = TypedDict(
    "DeleteLunaClientRequestRequestTypeDef",
    {
        "ClientArn": str,
    },
)
DescribeHapgRequestRequestTypeDef = TypedDict(
    "DescribeHapgRequestRequestTypeDef",
    {
        "HapgArn": str,
    },
)
DescribeHsmRequestRequestTypeDef = TypedDict(
    "DescribeHsmRequestRequestTypeDef",
    {
        "HsmArn": NotRequired[str],
        "HsmSerialNumber": NotRequired[str],
    },
)
DescribeLunaClientRequestRequestTypeDef = TypedDict(
    "DescribeLunaClientRequestRequestTypeDef",
    {
        "ClientArn": NotRequired[str],
        "CertificateFingerprint": NotRequired[str],
    },
)
GetConfigRequestRequestTypeDef = TypedDict(
    "GetConfigRequestRequestTypeDef",
    {
        "ClientArn": str,
        "ClientVersion": ClientVersionType,
        "HapgList": Sequence[str],
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
ListHapgsRequestRequestTypeDef = TypedDict(
    "ListHapgsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)
ListHsmsRequestRequestTypeDef = TypedDict(
    "ListHsmsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)
ListLunaClientsRequestRequestTypeDef = TypedDict(
    "ListLunaClientsRequestRequestTypeDef",
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
ModifyHapgRequestRequestTypeDef = TypedDict(
    "ModifyHapgRequestRequestTypeDef",
    {
        "HapgArn": str,
        "Label": NotRequired[str],
        "PartitionSerialList": NotRequired[Sequence[str]],
    },
)
ModifyHsmRequestRequestTypeDef = TypedDict(
    "ModifyHsmRequestRequestTypeDef",
    {
        "HsmArn": str,
        "SubnetId": NotRequired[str],
        "EniIp": NotRequired[str],
        "IamRoleArn": NotRequired[str],
        "ExternalId": NotRequired[str],
        "SyslogIp": NotRequired[str],
    },
)
ModifyLunaClientRequestRequestTypeDef = TypedDict(
    "ModifyLunaClientRequestRequestTypeDef",
    {
        "ClientArn": str,
        "Certificate": str,
    },
)
RemoveTagsFromResourceRequestRequestTypeDef = TypedDict(
    "RemoveTagsFromResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeyList": Sequence[str],
    },
)
AddTagsToResourceRequestRequestTypeDef = TypedDict(
    "AddTagsToResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagList": Sequence[TagTypeDef],
    },
)
AddTagsToResourceResponseTypeDef = TypedDict(
    "AddTagsToResourceResponseTypeDef",
    {
        "Status": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateHapgResponseTypeDef = TypedDict(
    "CreateHapgResponseTypeDef",
    {
        "HapgArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateHsmResponseTypeDef = TypedDict(
    "CreateHsmResponseTypeDef",
    {
        "HsmArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateLunaClientResponseTypeDef = TypedDict(
    "CreateLunaClientResponseTypeDef",
    {
        "ClientArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteHapgResponseTypeDef = TypedDict(
    "DeleteHapgResponseTypeDef",
    {
        "Status": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteHsmResponseTypeDef = TypedDict(
    "DeleteHsmResponseTypeDef",
    {
        "Status": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteLunaClientResponseTypeDef = TypedDict(
    "DeleteLunaClientResponseTypeDef",
    {
        "Status": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeHapgResponseTypeDef = TypedDict(
    "DescribeHapgResponseTypeDef",
    {
        "HapgArn": str,
        "HapgSerial": str,
        "HsmsLastActionFailed": List[str],
        "HsmsPendingDeletion": List[str],
        "HsmsPendingRegistration": List[str],
        "Label": str,
        "LastModifiedTimestamp": str,
        "PartitionSerialList": List[str],
        "State": CloudHsmObjectStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeHsmResponseTypeDef = TypedDict(
    "DescribeHsmResponseTypeDef",
    {
        "HsmArn": str,
        "Status": HsmStatusType,
        "StatusDetails": str,
        "AvailabilityZone": str,
        "EniId": str,
        "EniIp": str,
        "SubscriptionType": Literal["PRODUCTION"],
        "SubscriptionStartDate": str,
        "SubscriptionEndDate": str,
        "VpcId": str,
        "SubnetId": str,
        "IamRoleArn": str,
        "SerialNumber": str,
        "VendorName": str,
        "HsmType": str,
        "SoftwareVersion": str,
        "SshPublicKey": str,
        "SshKeyLastUpdated": str,
        "ServerCertUri": str,
        "ServerCertLastUpdated": str,
        "Partitions": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeLunaClientResponseTypeDef = TypedDict(
    "DescribeLunaClientResponseTypeDef",
    {
        "ClientArn": str,
        "Certificate": str,
        "CertificateFingerprint": str,
        "LastModifiedTimestamp": str,
        "Label": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetConfigResponseTypeDef = TypedDict(
    "GetConfigResponseTypeDef",
    {
        "ConfigType": str,
        "ConfigFile": str,
        "ConfigCred": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAvailableZonesResponseTypeDef = TypedDict(
    "ListAvailableZonesResponseTypeDef",
    {
        "AZList": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListHapgsResponseTypeDef = TypedDict(
    "ListHapgsResponseTypeDef",
    {
        "HapgList": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListHsmsResponseTypeDef = TypedDict(
    "ListHsmsResponseTypeDef",
    {
        "HsmList": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListLunaClientsResponseTypeDef = TypedDict(
    "ListLunaClientsResponseTypeDef",
    {
        "ClientList": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "TagList": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyHapgResponseTypeDef = TypedDict(
    "ModifyHapgResponseTypeDef",
    {
        "HapgArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyHsmResponseTypeDef = TypedDict(
    "ModifyHsmResponseTypeDef",
    {
        "HsmArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModifyLunaClientResponseTypeDef = TypedDict(
    "ModifyLunaClientResponseTypeDef",
    {
        "ClientArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RemoveTagsFromResourceResponseTypeDef = TypedDict(
    "RemoveTagsFromResourceResponseTypeDef",
    {
        "Status": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListHapgsRequestListHapgsPaginateTypeDef = TypedDict(
    "ListHapgsRequestListHapgsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListHsmsRequestListHsmsPaginateTypeDef = TypedDict(
    "ListHsmsRequestListHsmsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListLunaClientsRequestListLunaClientsPaginateTypeDef = TypedDict(
    "ListLunaClientsRequestListLunaClientsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
