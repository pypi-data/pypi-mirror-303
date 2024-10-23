"""
Type annotations for efs service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_efs/type_defs/)

Usage::

    ```python
    from mypy_boto3_efs.type_defs import PosixUserOutputTypeDef

    data: PosixUserOutputTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import (
    LifeCycleStateType,
    PerformanceModeType,
    ReplicationOverwriteProtectionType,
    ReplicationStatusType,
    ResourceIdTypeType,
    ResourceType,
    StatusType,
    ThroughputModeType,
    TransitionToArchiveRulesType,
    TransitionToIARulesType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "PosixUserOutputTypeDef",
    "ResponseMetadataTypeDef",
    "TagTypeDef",
    "BackupPolicyTypeDef",
    "PosixUserTypeDef",
    "CreateMountTargetRequestRequestTypeDef",
    "DestinationToCreateTypeDef",
    "CreationInfoTypeDef",
    "DeleteAccessPointRequestRequestTypeDef",
    "DeleteFileSystemPolicyRequestRequestTypeDef",
    "DeleteFileSystemRequestRequestTypeDef",
    "DeleteMountTargetRequestRequestTypeDef",
    "DeleteReplicationConfigurationRequestRequestTypeDef",
    "DeleteTagsRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeAccessPointsRequestRequestTypeDef",
    "DescribeAccountPreferencesRequestRequestTypeDef",
    "ResourceIdPreferenceTypeDef",
    "DescribeBackupPolicyRequestRequestTypeDef",
    "DescribeFileSystemPolicyRequestRequestTypeDef",
    "DescribeFileSystemsRequestRequestTypeDef",
    "DescribeLifecycleConfigurationRequestRequestTypeDef",
    "DescribeMountTargetSecurityGroupsRequestRequestTypeDef",
    "DescribeMountTargetsRequestRequestTypeDef",
    "MountTargetDescriptionTypeDef",
    "DescribeReplicationConfigurationsRequestRequestTypeDef",
    "DescribeTagsRequestRequestTypeDef",
    "DestinationTypeDef",
    "FileSystemProtectionDescriptionTypeDef",
    "FileSystemSizeTypeDef",
    "LifecyclePolicyTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ModifyMountTargetSecurityGroupsRequestRequestTypeDef",
    "PutAccountPreferencesRequestRequestTypeDef",
    "PutFileSystemPolicyRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateFileSystemProtectionRequestRequestTypeDef",
    "UpdateFileSystemRequestRequestTypeDef",
    "DescribeMountTargetSecurityGroupsResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "FileSystemPolicyDescriptionTypeDef",
    "FileSystemProtectionDescriptionResponseTypeDef",
    "MountTargetDescriptionResponseTypeDef",
    "CreateFileSystemRequestRequestTypeDef",
    "CreateTagsRequestRequestTypeDef",
    "DescribeTagsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "BackupPolicyDescriptionTypeDef",
    "PutBackupPolicyRequestRequestTypeDef",
    "CreateReplicationConfigurationRequestRequestTypeDef",
    "RootDirectoryTypeDef",
    "DescribeAccessPointsRequestDescribeAccessPointsPaginateTypeDef",
    "DescribeFileSystemsRequestDescribeFileSystemsPaginateTypeDef",
    "DescribeMountTargetsRequestDescribeMountTargetsPaginateTypeDef",
    "DescribeReplicationConfigurationsRequestDescribeReplicationConfigurationsPaginateTypeDef",
    "DescribeTagsRequestDescribeTagsPaginateTypeDef",
    "DescribeAccountPreferencesResponseTypeDef",
    "PutAccountPreferencesResponseTypeDef",
    "DescribeMountTargetsResponseTypeDef",
    "ReplicationConfigurationDescriptionResponseTypeDef",
    "ReplicationConfigurationDescriptionTypeDef",
    "FileSystemDescriptionResponseTypeDef",
    "FileSystemDescriptionTypeDef",
    "LifecycleConfigurationDescriptionTypeDef",
    "PutLifecycleConfigurationRequestRequestTypeDef",
    "AccessPointDescriptionResponseTypeDef",
    "AccessPointDescriptionTypeDef",
    "CreateAccessPointRequestRequestTypeDef",
    "DescribeReplicationConfigurationsResponseTypeDef",
    "DescribeFileSystemsResponseTypeDef",
    "DescribeAccessPointsResponseTypeDef",
)

PosixUserOutputTypeDef = TypedDict(
    "PosixUserOutputTypeDef",
    {
        "Uid": int,
        "Gid": int,
        "SecondaryGids": NotRequired[List[int]],
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
        "Value": str,
    },
)
BackupPolicyTypeDef = TypedDict(
    "BackupPolicyTypeDef",
    {
        "Status": StatusType,
    },
)
PosixUserTypeDef = TypedDict(
    "PosixUserTypeDef",
    {
        "Uid": int,
        "Gid": int,
        "SecondaryGids": NotRequired[Sequence[int]],
    },
)
CreateMountTargetRequestRequestTypeDef = TypedDict(
    "CreateMountTargetRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "SubnetId": str,
        "IpAddress": NotRequired[str],
        "SecurityGroups": NotRequired[Sequence[str]],
    },
)
DestinationToCreateTypeDef = TypedDict(
    "DestinationToCreateTypeDef",
    {
        "Region": NotRequired[str],
        "AvailabilityZoneName": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "FileSystemId": NotRequired[str],
    },
)
CreationInfoTypeDef = TypedDict(
    "CreationInfoTypeDef",
    {
        "OwnerUid": int,
        "OwnerGid": int,
        "Permissions": str,
    },
)
DeleteAccessPointRequestRequestTypeDef = TypedDict(
    "DeleteAccessPointRequestRequestTypeDef",
    {
        "AccessPointId": str,
    },
)
DeleteFileSystemPolicyRequestRequestTypeDef = TypedDict(
    "DeleteFileSystemPolicyRequestRequestTypeDef",
    {
        "FileSystemId": str,
    },
)
DeleteFileSystemRequestRequestTypeDef = TypedDict(
    "DeleteFileSystemRequestRequestTypeDef",
    {
        "FileSystemId": str,
    },
)
DeleteMountTargetRequestRequestTypeDef = TypedDict(
    "DeleteMountTargetRequestRequestTypeDef",
    {
        "MountTargetId": str,
    },
)
DeleteReplicationConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteReplicationConfigurationRequestRequestTypeDef",
    {
        "SourceFileSystemId": str,
    },
)
DeleteTagsRequestRequestTypeDef = TypedDict(
    "DeleteTagsRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "TagKeys": Sequence[str],
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
DescribeAccessPointsRequestRequestTypeDef = TypedDict(
    "DescribeAccessPointsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "AccessPointId": NotRequired[str],
        "FileSystemId": NotRequired[str],
    },
)
DescribeAccountPreferencesRequestRequestTypeDef = TypedDict(
    "DescribeAccountPreferencesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ResourceIdPreferenceTypeDef = TypedDict(
    "ResourceIdPreferenceTypeDef",
    {
        "ResourceIdType": NotRequired[ResourceIdTypeType],
        "Resources": NotRequired[List[ResourceType]],
    },
)
DescribeBackupPolicyRequestRequestTypeDef = TypedDict(
    "DescribeBackupPolicyRequestRequestTypeDef",
    {
        "FileSystemId": str,
    },
)
DescribeFileSystemPolicyRequestRequestTypeDef = TypedDict(
    "DescribeFileSystemPolicyRequestRequestTypeDef",
    {
        "FileSystemId": str,
    },
)
DescribeFileSystemsRequestRequestTypeDef = TypedDict(
    "DescribeFileSystemsRequestRequestTypeDef",
    {
        "MaxItems": NotRequired[int],
        "Marker": NotRequired[str],
        "CreationToken": NotRequired[str],
        "FileSystemId": NotRequired[str],
    },
)
DescribeLifecycleConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeLifecycleConfigurationRequestRequestTypeDef",
    {
        "FileSystemId": str,
    },
)
DescribeMountTargetSecurityGroupsRequestRequestTypeDef = TypedDict(
    "DescribeMountTargetSecurityGroupsRequestRequestTypeDef",
    {
        "MountTargetId": str,
    },
)
DescribeMountTargetsRequestRequestTypeDef = TypedDict(
    "DescribeMountTargetsRequestRequestTypeDef",
    {
        "MaxItems": NotRequired[int],
        "Marker": NotRequired[str],
        "FileSystemId": NotRequired[str],
        "MountTargetId": NotRequired[str],
        "AccessPointId": NotRequired[str],
    },
)
MountTargetDescriptionTypeDef = TypedDict(
    "MountTargetDescriptionTypeDef",
    {
        "MountTargetId": str,
        "FileSystemId": str,
        "SubnetId": str,
        "LifeCycleState": LifeCycleStateType,
        "OwnerId": NotRequired[str],
        "IpAddress": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "AvailabilityZoneId": NotRequired[str],
        "AvailabilityZoneName": NotRequired[str],
        "VpcId": NotRequired[str],
    },
)
DescribeReplicationConfigurationsRequestRequestTypeDef = TypedDict(
    "DescribeReplicationConfigurationsRequestRequestTypeDef",
    {
        "FileSystemId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeTagsRequestRequestTypeDef = TypedDict(
    "DescribeTagsRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "MaxItems": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "Status": ReplicationStatusType,
        "FileSystemId": str,
        "Region": str,
        "LastReplicatedTimestamp": NotRequired[datetime],
    },
)
FileSystemProtectionDescriptionTypeDef = TypedDict(
    "FileSystemProtectionDescriptionTypeDef",
    {
        "ReplicationOverwriteProtection": NotRequired[ReplicationOverwriteProtectionType],
    },
)
FileSystemSizeTypeDef = TypedDict(
    "FileSystemSizeTypeDef",
    {
        "Value": int,
        "Timestamp": NotRequired[datetime],
        "ValueInIA": NotRequired[int],
        "ValueInStandard": NotRequired[int],
        "ValueInArchive": NotRequired[int],
    },
)
LifecyclePolicyTypeDef = TypedDict(
    "LifecyclePolicyTypeDef",
    {
        "TransitionToIA": NotRequired[TransitionToIARulesType],
        "TransitionToPrimaryStorageClass": NotRequired[Literal["AFTER_1_ACCESS"]],
        "TransitionToArchive": NotRequired[TransitionToArchiveRulesType],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ModifyMountTargetSecurityGroupsRequestRequestTypeDef = TypedDict(
    "ModifyMountTargetSecurityGroupsRequestRequestTypeDef",
    {
        "MountTargetId": str,
        "SecurityGroups": NotRequired[Sequence[str]],
    },
)
PutAccountPreferencesRequestRequestTypeDef = TypedDict(
    "PutAccountPreferencesRequestRequestTypeDef",
    {
        "ResourceIdType": ResourceIdTypeType,
    },
)
PutFileSystemPolicyRequestRequestTypeDef = TypedDict(
    "PutFileSystemPolicyRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "Policy": str,
        "BypassPolicyLockoutSafetyCheck": NotRequired[bool],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceId": str,
        "TagKeys": Sequence[str],
    },
)
UpdateFileSystemProtectionRequestRequestTypeDef = TypedDict(
    "UpdateFileSystemProtectionRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "ReplicationOverwriteProtection": NotRequired[ReplicationOverwriteProtectionType],
    },
)
UpdateFileSystemRequestRequestTypeDef = TypedDict(
    "UpdateFileSystemRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "ThroughputMode": NotRequired[ThroughputModeType],
        "ProvisionedThroughputInMibps": NotRequired[float],
    },
)
DescribeMountTargetSecurityGroupsResponseTypeDef = TypedDict(
    "DescribeMountTargetSecurityGroupsResponseTypeDef",
    {
        "SecurityGroups": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FileSystemPolicyDescriptionTypeDef = TypedDict(
    "FileSystemPolicyDescriptionTypeDef",
    {
        "FileSystemId": str,
        "Policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FileSystemProtectionDescriptionResponseTypeDef = TypedDict(
    "FileSystemProtectionDescriptionResponseTypeDef",
    {
        "ReplicationOverwriteProtection": ReplicationOverwriteProtectionType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MountTargetDescriptionResponseTypeDef = TypedDict(
    "MountTargetDescriptionResponseTypeDef",
    {
        "OwnerId": str,
        "MountTargetId": str,
        "FileSystemId": str,
        "SubnetId": str,
        "LifeCycleState": LifeCycleStateType,
        "IpAddress": str,
        "NetworkInterfaceId": str,
        "AvailabilityZoneId": str,
        "AvailabilityZoneName": str,
        "VpcId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFileSystemRequestRequestTypeDef = TypedDict(
    "CreateFileSystemRequestRequestTypeDef",
    {
        "CreationToken": str,
        "PerformanceMode": NotRequired[PerformanceModeType],
        "Encrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "ThroughputMode": NotRequired[ThroughputModeType],
        "ProvisionedThroughputInMibps": NotRequired[float],
        "AvailabilityZoneName": NotRequired[str],
        "Backup": NotRequired[bool],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateTagsRequestRequestTypeDef = TypedDict(
    "CreateTagsRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "Tags": Sequence[TagTypeDef],
    },
)
DescribeTagsResponseTypeDef = TypedDict(
    "DescribeTagsResponseTypeDef",
    {
        "Marker": str,
        "Tags": List[TagTypeDef],
        "NextMarker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceId": str,
        "Tags": Sequence[TagTypeDef],
    },
)
BackupPolicyDescriptionTypeDef = TypedDict(
    "BackupPolicyDescriptionTypeDef",
    {
        "BackupPolicy": BackupPolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutBackupPolicyRequestRequestTypeDef = TypedDict(
    "PutBackupPolicyRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "BackupPolicy": BackupPolicyTypeDef,
    },
)
CreateReplicationConfigurationRequestRequestTypeDef = TypedDict(
    "CreateReplicationConfigurationRequestRequestTypeDef",
    {
        "SourceFileSystemId": str,
        "Destinations": Sequence[DestinationToCreateTypeDef],
    },
)
RootDirectoryTypeDef = TypedDict(
    "RootDirectoryTypeDef",
    {
        "Path": NotRequired[str],
        "CreationInfo": NotRequired[CreationInfoTypeDef],
    },
)
DescribeAccessPointsRequestDescribeAccessPointsPaginateTypeDef = TypedDict(
    "DescribeAccessPointsRequestDescribeAccessPointsPaginateTypeDef",
    {
        "AccessPointId": NotRequired[str],
        "FileSystemId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeFileSystemsRequestDescribeFileSystemsPaginateTypeDef = TypedDict(
    "DescribeFileSystemsRequestDescribeFileSystemsPaginateTypeDef",
    {
        "CreationToken": NotRequired[str],
        "FileSystemId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeMountTargetsRequestDescribeMountTargetsPaginateTypeDef = TypedDict(
    "DescribeMountTargetsRequestDescribeMountTargetsPaginateTypeDef",
    {
        "FileSystemId": NotRequired[str],
        "MountTargetId": NotRequired[str],
        "AccessPointId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeReplicationConfigurationsRequestDescribeReplicationConfigurationsPaginateTypeDef = (
    TypedDict(
        "DescribeReplicationConfigurationsRequestDescribeReplicationConfigurationsPaginateTypeDef",
        {
            "FileSystemId": NotRequired[str],
            "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
        },
    )
)
DescribeTagsRequestDescribeTagsPaginateTypeDef = TypedDict(
    "DescribeTagsRequestDescribeTagsPaginateTypeDef",
    {
        "FileSystemId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeAccountPreferencesResponseTypeDef = TypedDict(
    "DescribeAccountPreferencesResponseTypeDef",
    {
        "ResourceIdPreference": ResourceIdPreferenceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PutAccountPreferencesResponseTypeDef = TypedDict(
    "PutAccountPreferencesResponseTypeDef",
    {
        "ResourceIdPreference": ResourceIdPreferenceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeMountTargetsResponseTypeDef = TypedDict(
    "DescribeMountTargetsResponseTypeDef",
    {
        "Marker": str,
        "MountTargets": List[MountTargetDescriptionTypeDef],
        "NextMarker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReplicationConfigurationDescriptionResponseTypeDef = TypedDict(
    "ReplicationConfigurationDescriptionResponseTypeDef",
    {
        "SourceFileSystemId": str,
        "SourceFileSystemRegion": str,
        "SourceFileSystemArn": str,
        "OriginalSourceFileSystemArn": str,
        "CreationTime": datetime,
        "Destinations": List[DestinationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReplicationConfigurationDescriptionTypeDef = TypedDict(
    "ReplicationConfigurationDescriptionTypeDef",
    {
        "SourceFileSystemId": str,
        "SourceFileSystemRegion": str,
        "SourceFileSystemArn": str,
        "OriginalSourceFileSystemArn": str,
        "CreationTime": datetime,
        "Destinations": List[DestinationTypeDef],
    },
)
FileSystemDescriptionResponseTypeDef = TypedDict(
    "FileSystemDescriptionResponseTypeDef",
    {
        "OwnerId": str,
        "CreationToken": str,
        "FileSystemId": str,
        "FileSystemArn": str,
        "CreationTime": datetime,
        "LifeCycleState": LifeCycleStateType,
        "Name": str,
        "NumberOfMountTargets": int,
        "SizeInBytes": FileSystemSizeTypeDef,
        "PerformanceMode": PerformanceModeType,
        "Encrypted": bool,
        "KmsKeyId": str,
        "ThroughputMode": ThroughputModeType,
        "ProvisionedThroughputInMibps": float,
        "AvailabilityZoneName": str,
        "AvailabilityZoneId": str,
        "Tags": List[TagTypeDef],
        "FileSystemProtection": FileSystemProtectionDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FileSystemDescriptionTypeDef = TypedDict(
    "FileSystemDescriptionTypeDef",
    {
        "OwnerId": str,
        "CreationToken": str,
        "FileSystemId": str,
        "CreationTime": datetime,
        "LifeCycleState": LifeCycleStateType,
        "NumberOfMountTargets": int,
        "SizeInBytes": FileSystemSizeTypeDef,
        "PerformanceMode": PerformanceModeType,
        "Tags": List[TagTypeDef],
        "FileSystemArn": NotRequired[str],
        "Name": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "KmsKeyId": NotRequired[str],
        "ThroughputMode": NotRequired[ThroughputModeType],
        "ProvisionedThroughputInMibps": NotRequired[float],
        "AvailabilityZoneName": NotRequired[str],
        "AvailabilityZoneId": NotRequired[str],
        "FileSystemProtection": NotRequired[FileSystemProtectionDescriptionTypeDef],
    },
)
LifecycleConfigurationDescriptionTypeDef = TypedDict(
    "LifecycleConfigurationDescriptionTypeDef",
    {
        "LifecyclePolicies": List[LifecyclePolicyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutLifecycleConfigurationRequestRequestTypeDef = TypedDict(
    "PutLifecycleConfigurationRequestRequestTypeDef",
    {
        "FileSystemId": str,
        "LifecyclePolicies": Sequence[LifecyclePolicyTypeDef],
    },
)
AccessPointDescriptionResponseTypeDef = TypedDict(
    "AccessPointDescriptionResponseTypeDef",
    {
        "ClientToken": str,
        "Name": str,
        "Tags": List[TagTypeDef],
        "AccessPointId": str,
        "AccessPointArn": str,
        "FileSystemId": str,
        "PosixUser": PosixUserOutputTypeDef,
        "RootDirectory": RootDirectoryTypeDef,
        "OwnerId": str,
        "LifeCycleState": LifeCycleStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AccessPointDescriptionTypeDef = TypedDict(
    "AccessPointDescriptionTypeDef",
    {
        "ClientToken": NotRequired[str],
        "Name": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "AccessPointId": NotRequired[str],
        "AccessPointArn": NotRequired[str],
        "FileSystemId": NotRequired[str],
        "PosixUser": NotRequired[PosixUserOutputTypeDef],
        "RootDirectory": NotRequired[RootDirectoryTypeDef],
        "OwnerId": NotRequired[str],
        "LifeCycleState": NotRequired[LifeCycleStateType],
    },
)
CreateAccessPointRequestRequestTypeDef = TypedDict(
    "CreateAccessPointRequestRequestTypeDef",
    {
        "ClientToken": str,
        "FileSystemId": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "PosixUser": NotRequired[PosixUserTypeDef],
        "RootDirectory": NotRequired[RootDirectoryTypeDef],
    },
)
DescribeReplicationConfigurationsResponseTypeDef = TypedDict(
    "DescribeReplicationConfigurationsResponseTypeDef",
    {
        "Replications": List[ReplicationConfigurationDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeFileSystemsResponseTypeDef = TypedDict(
    "DescribeFileSystemsResponseTypeDef",
    {
        "Marker": str,
        "FileSystems": List[FileSystemDescriptionTypeDef],
        "NextMarker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAccessPointsResponseTypeDef = TypedDict(
    "DescribeAccessPointsResponseTypeDef",
    {
        "AccessPoints": List[AccessPointDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
