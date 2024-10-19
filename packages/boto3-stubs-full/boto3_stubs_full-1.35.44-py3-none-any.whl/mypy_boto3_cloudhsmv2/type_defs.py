"""
Type annotations for cloudhsmv2 service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/type_defs/)

Usage::

    ```python
    from mypy_boto3_cloudhsmv2.type_defs import BackupRetentionPolicyTypeDef

    data: BackupRetentionPolicyTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import BackupStateType, ClusterModeType, ClusterStateType, HsmStateType

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "BackupRetentionPolicyTypeDef",
    "TagTypeDef",
    "CertificatesTypeDef",
    "HsmTypeDef",
    "DestinationBackupTypeDef",
    "ResponseMetadataTypeDef",
    "CreateHsmRequestRequestTypeDef",
    "DeleteBackupRequestRequestTypeDef",
    "DeleteClusterRequestRequestTypeDef",
    "DeleteHsmRequestRequestTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeBackupsRequestRequestTypeDef",
    "DescribeClustersRequestRequestTypeDef",
    "GetResourcePolicyRequestRequestTypeDef",
    "InitializeClusterRequestRequestTypeDef",
    "ListTagsRequestRequestTypeDef",
    "ModifyBackupAttributesRequestRequestTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "RestoreBackupRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "ModifyClusterRequestRequestTypeDef",
    "BackupTypeDef",
    "CopyBackupToRegionRequestRequestTypeDef",
    "CreateClusterRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "ClusterTypeDef",
    "CopyBackupToRegionResponseTypeDef",
    "CreateHsmResponseTypeDef",
    "DeleteHsmResponseTypeDef",
    "DeleteResourcePolicyResponseTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "InitializeClusterResponseTypeDef",
    "ListTagsResponseTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "DescribeBackupsRequestDescribeBackupsPaginateTypeDef",
    "DescribeClustersRequestDescribeClustersPaginateTypeDef",
    "ListTagsRequestListTagsPaginateTypeDef",
    "DeleteBackupResponseTypeDef",
    "DescribeBackupsResponseTypeDef",
    "ModifyBackupAttributesResponseTypeDef",
    "RestoreBackupResponseTypeDef",
    "CreateClusterResponseTypeDef",
    "DeleteClusterResponseTypeDef",
    "DescribeClustersResponseTypeDef",
    "ModifyClusterResponseTypeDef",
)

BackupRetentionPolicyTypeDef = TypedDict(
    "BackupRetentionPolicyTypeDef",
    {
        "Type": NotRequired[Literal["DAYS"]],
        "Value": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
CertificatesTypeDef = TypedDict(
    "CertificatesTypeDef",
    {
        "ClusterCsr": NotRequired[str],
        "HsmCertificate": NotRequired[str],
        "AwsHardwareCertificate": NotRequired[str],
        "ManufacturerHardwareCertificate": NotRequired[str],
        "ClusterCertificate": NotRequired[str],
    },
)
HsmTypeDef = TypedDict(
    "HsmTypeDef",
    {
        "HsmId": str,
        "AvailabilityZone": NotRequired[str],
        "ClusterId": NotRequired[str],
        "SubnetId": NotRequired[str],
        "EniId": NotRequired[str],
        "EniIp": NotRequired[str],
        "State": NotRequired[HsmStateType],
        "StateMessage": NotRequired[str],
    },
)
DestinationBackupTypeDef = TypedDict(
    "DestinationBackupTypeDef",
    {
        "CreateTimestamp": NotRequired[datetime],
        "SourceRegion": NotRequired[str],
        "SourceBackup": NotRequired[str],
        "SourceCluster": NotRequired[str],
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
CreateHsmRequestRequestTypeDef = TypedDict(
    "CreateHsmRequestRequestTypeDef",
    {
        "ClusterId": str,
        "AvailabilityZone": str,
        "IpAddress": NotRequired[str],
    },
)
DeleteBackupRequestRequestTypeDef = TypedDict(
    "DeleteBackupRequestRequestTypeDef",
    {
        "BackupId": str,
    },
)
DeleteClusterRequestRequestTypeDef = TypedDict(
    "DeleteClusterRequestRequestTypeDef",
    {
        "ClusterId": str,
    },
)
DeleteHsmRequestRequestTypeDef = TypedDict(
    "DeleteHsmRequestRequestTypeDef",
    {
        "ClusterId": str,
        "HsmId": NotRequired[str],
        "EniId": NotRequired[str],
        "EniIp": NotRequired[str],
    },
)
DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": NotRequired[str],
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
DescribeBackupsRequestRequestTypeDef = TypedDict(
    "DescribeBackupsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Mapping[str, Sequence[str]]],
        "Shared": NotRequired[bool],
        "SortAscending": NotRequired[bool],
    },
)
DescribeClustersRequestRequestTypeDef = TypedDict(
    "DescribeClustersRequestRequestTypeDef",
    {
        "Filters": NotRequired[Mapping[str, Sequence[str]]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GetResourcePolicyRequestRequestTypeDef = TypedDict(
    "GetResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": NotRequired[str],
    },
)
InitializeClusterRequestRequestTypeDef = TypedDict(
    "InitializeClusterRequestRequestTypeDef",
    {
        "ClusterId": str,
        "SignedCert": str,
        "TrustAnchor": str,
    },
)
ListTagsRequestRequestTypeDef = TypedDict(
    "ListTagsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ModifyBackupAttributesRequestRequestTypeDef = TypedDict(
    "ModifyBackupAttributesRequestRequestTypeDef",
    {
        "BackupId": str,
        "NeverExpires": bool,
    },
)
PutResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": NotRequired[str],
        "Policy": NotRequired[str],
    },
)
RestoreBackupRequestRequestTypeDef = TypedDict(
    "RestoreBackupRequestRequestTypeDef",
    {
        "BackupId": str,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceId": str,
        "TagKeyList": Sequence[str],
    },
)
ModifyClusterRequestRequestTypeDef = TypedDict(
    "ModifyClusterRequestRequestTypeDef",
    {
        "BackupRetentionPolicy": BackupRetentionPolicyTypeDef,
        "ClusterId": str,
    },
)
BackupTypeDef = TypedDict(
    "BackupTypeDef",
    {
        "BackupId": str,
        "BackupArn": NotRequired[str],
        "BackupState": NotRequired[BackupStateType],
        "ClusterId": NotRequired[str],
        "CreateTimestamp": NotRequired[datetime],
        "CopyTimestamp": NotRequired[datetime],
        "NeverExpires": NotRequired[bool],
        "SourceRegion": NotRequired[str],
        "SourceBackup": NotRequired[str],
        "SourceCluster": NotRequired[str],
        "DeleteTimestamp": NotRequired[datetime],
        "TagList": NotRequired[List[TagTypeDef]],
        "HsmType": NotRequired[str],
        "Mode": NotRequired[ClusterModeType],
    },
)
CopyBackupToRegionRequestRequestTypeDef = TypedDict(
    "CopyBackupToRegionRequestRequestTypeDef",
    {
        "DestinationRegion": str,
        "BackupId": str,
        "TagList": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateClusterRequestRequestTypeDef = TypedDict(
    "CreateClusterRequestRequestTypeDef",
    {
        "HsmType": str,
        "SubnetIds": Sequence[str],
        "BackupRetentionPolicy": NotRequired[BackupRetentionPolicyTypeDef],
        "SourceBackupId": NotRequired[str],
        "TagList": NotRequired[Sequence[TagTypeDef]],
        "Mode": NotRequired[ClusterModeType],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceId": str,
        "TagList": Sequence[TagTypeDef],
    },
)
ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "BackupPolicy": NotRequired[Literal["DEFAULT"]],
        "BackupRetentionPolicy": NotRequired[BackupRetentionPolicyTypeDef],
        "ClusterId": NotRequired[str],
        "CreateTimestamp": NotRequired[datetime],
        "Hsms": NotRequired[List[HsmTypeDef]],
        "HsmType": NotRequired[str],
        "PreCoPassword": NotRequired[str],
        "SecurityGroup": NotRequired[str],
        "SourceBackupId": NotRequired[str],
        "State": NotRequired[ClusterStateType],
        "StateMessage": NotRequired[str],
        "SubnetMapping": NotRequired[Dict[str, str]],
        "VpcId": NotRequired[str],
        "Certificates": NotRequired[CertificatesTypeDef],
        "TagList": NotRequired[List[TagTypeDef]],
        "Mode": NotRequired[ClusterModeType],
    },
)
CopyBackupToRegionResponseTypeDef = TypedDict(
    "CopyBackupToRegionResponseTypeDef",
    {
        "DestinationBackup": DestinationBackupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateHsmResponseTypeDef = TypedDict(
    "CreateHsmResponseTypeDef",
    {
        "Hsm": HsmTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteHsmResponseTypeDef = TypedDict(
    "DeleteHsmResponseTypeDef",
    {
        "HsmId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteResourcePolicyResponseTypeDef = TypedDict(
    "DeleteResourcePolicyResponseTypeDef",
    {
        "ResourceArn": str,
        "Policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResourcePolicyResponseTypeDef = TypedDict(
    "GetResourcePolicyResponseTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InitializeClusterResponseTypeDef = TypedDict(
    "InitializeClusterResponseTypeDef",
    {
        "State": ClusterStateType,
        "StateMessage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef",
    {
        "TagList": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PutResourcePolicyResponseTypeDef = TypedDict(
    "PutResourcePolicyResponseTypeDef",
    {
        "ResourceArn": str,
        "Policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeBackupsRequestDescribeBackupsPaginateTypeDef = TypedDict(
    "DescribeBackupsRequestDescribeBackupsPaginateTypeDef",
    {
        "Filters": NotRequired[Mapping[str, Sequence[str]]],
        "Shared": NotRequired[bool],
        "SortAscending": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeClustersRequestDescribeClustersPaginateTypeDef = TypedDict(
    "DescribeClustersRequestDescribeClustersPaginateTypeDef",
    {
        "Filters": NotRequired[Mapping[str, Sequence[str]]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTagsRequestListTagsPaginateTypeDef = TypedDict(
    "ListTagsRequestListTagsPaginateTypeDef",
    {
        "ResourceId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DeleteBackupResponseTypeDef = TypedDict(
    "DeleteBackupResponseTypeDef",
    {
        "Backup": BackupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeBackupsResponseTypeDef = TypedDict(
    "DescribeBackupsResponseTypeDef",
    {
        "Backups": List[BackupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ModifyBackupAttributesResponseTypeDef = TypedDict(
    "ModifyBackupAttributesResponseTypeDef",
    {
        "Backup": BackupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreBackupResponseTypeDef = TypedDict(
    "RestoreBackupResponseTypeDef",
    {
        "Backup": BackupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateClusterResponseTypeDef = TypedDict(
    "CreateClusterResponseTypeDef",
    {
        "Cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteClusterResponseTypeDef = TypedDict(
    "DeleteClusterResponseTypeDef",
    {
        "Cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeClustersResponseTypeDef = TypedDict(
    "DescribeClustersResponseTypeDef",
    {
        "Clusters": List[ClusterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ModifyClusterResponseTypeDef = TypedDict(
    "ModifyClusterResponseTypeDef",
    {
        "Cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
