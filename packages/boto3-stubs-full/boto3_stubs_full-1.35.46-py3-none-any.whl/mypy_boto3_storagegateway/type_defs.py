"""
Type annotations for storagegateway service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/type_defs/)

Usage::

    ```python
    from mypy_boto3_storagegateway.type_defs import TagTypeDef

    data: TagTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    ActiveDirectoryStatusType,
    AutomaticUpdatePolicyType,
    AvailabilityMonitorTestStatusType,
    CaseSensitivityType,
    EncryptionTypeType,
    FileShareTypeType,
    GatewayCapacityType,
    HostEnvironmentType,
    ObjectACLType,
    PoolStatusType,
    RetentionLockTypeType,
    SMBSecurityStrategyType,
    TapeStorageClassType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "AddCacheInputRequestTypeDef",
    "AddUploadBufferInputRequestTypeDef",
    "AddWorkingStorageInputRequestTypeDef",
    "AssignTapePoolInputRequestTypeDef",
    "CacheAttributesTypeDef",
    "EndpointNetworkConfigurationTypeDef",
    "AttachVolumeInputRequestTypeDef",
    "AutomaticTapeCreationRuleTypeDef",
    "BandwidthRateLimitIntervalOutputTypeDef",
    "BandwidthRateLimitIntervalTypeDef",
    "VolumeiSCSIAttributesTypeDef",
    "CancelArchivalInputRequestTypeDef",
    "CancelRetrievalInputRequestTypeDef",
    "ChapInfoTypeDef",
    "NFSFileShareDefaultsTypeDef",
    "DeleteAutomaticTapeCreationPolicyInputRequestTypeDef",
    "DeleteBandwidthRateLimitInputRequestTypeDef",
    "DeleteChapCredentialsInputRequestTypeDef",
    "DeleteFileShareInputRequestTypeDef",
    "DeleteGatewayInputRequestTypeDef",
    "DeleteSnapshotScheduleInputRequestTypeDef",
    "DeleteTapeArchiveInputRequestTypeDef",
    "DeleteTapeInputRequestTypeDef",
    "DeleteTapePoolInputRequestTypeDef",
    "DeleteVolumeInputRequestTypeDef",
    "DescribeAvailabilityMonitorTestInputRequestTypeDef",
    "DescribeBandwidthRateLimitInputRequestTypeDef",
    "DescribeBandwidthRateLimitScheduleInputRequestTypeDef",
    "DescribeCacheInputRequestTypeDef",
    "DescribeCachediSCSIVolumesInputRequestTypeDef",
    "DescribeChapCredentialsInputRequestTypeDef",
    "DescribeFileSystemAssociationsInputRequestTypeDef",
    "DescribeGatewayInformationInputRequestTypeDef",
    "NetworkInterfaceTypeDef",
    "DescribeMaintenanceStartTimeInputRequestTypeDef",
    "SoftwareUpdatePreferencesTypeDef",
    "DescribeNFSFileSharesInputRequestTypeDef",
    "DescribeSMBFileSharesInputRequestTypeDef",
    "DescribeSMBSettingsInputRequestTypeDef",
    "SMBLocalGroupsOutputTypeDef",
    "DescribeSnapshotScheduleInputRequestTypeDef",
    "DescribeStorediSCSIVolumesInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeTapeArchivesInputRequestTypeDef",
    "TapeArchiveTypeDef",
    "DescribeTapeRecoveryPointsInputRequestTypeDef",
    "TapeRecoveryPointInfoTypeDef",
    "DescribeTapesInputRequestTypeDef",
    "TapeTypeDef",
    "DescribeUploadBufferInputRequestTypeDef",
    "DescribeVTLDevicesInputRequestTypeDef",
    "DescribeWorkingStorageInputRequestTypeDef",
    "DetachVolumeInputRequestTypeDef",
    "DeviceiSCSIAttributesTypeDef",
    "DisableGatewayInputRequestTypeDef",
    "DisassociateFileSystemInputRequestTypeDef",
    "DiskTypeDef",
    "EndpointNetworkConfigurationOutputTypeDef",
    "FileShareInfoTypeDef",
    "FileSystemAssociationStatusDetailTypeDef",
    "FileSystemAssociationSummaryTypeDef",
    "GatewayInfoTypeDef",
    "JoinDomainInputRequestTypeDef",
    "ListAutomaticTapeCreationPoliciesInputRequestTypeDef",
    "ListFileSharesInputRequestTypeDef",
    "ListFileSystemAssociationsInputRequestTypeDef",
    "ListGatewaysInputRequestTypeDef",
    "ListLocalDisksInputRequestTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTapePoolsInputRequestTypeDef",
    "PoolInfoTypeDef",
    "ListTapesInputRequestTypeDef",
    "TapeInfoTypeDef",
    "ListVolumeInitiatorsInputRequestTypeDef",
    "ListVolumeRecoveryPointsInputRequestTypeDef",
    "VolumeRecoveryPointInfoTypeDef",
    "ListVolumesInputRequestTypeDef",
    "VolumeInfoTypeDef",
    "NotifyWhenUploadedInputRequestTypeDef",
    "RefreshCacheInputRequestTypeDef",
    "RemoveTagsFromResourceInputRequestTypeDef",
    "ResetCacheInputRequestTypeDef",
    "RetrieveTapeArchiveInputRequestTypeDef",
    "RetrieveTapeRecoveryPointInputRequestTypeDef",
    "SMBLocalGroupsTypeDef",
    "SetLocalConsolePasswordInputRequestTypeDef",
    "SetSMBGuestPasswordInputRequestTypeDef",
    "ShutdownGatewayInputRequestTypeDef",
    "StartAvailabilityMonitorTestInputRequestTypeDef",
    "StartGatewayInputRequestTypeDef",
    "UpdateBandwidthRateLimitInputRequestTypeDef",
    "UpdateChapCredentialsInputRequestTypeDef",
    "UpdateGatewayInformationInputRequestTypeDef",
    "UpdateGatewaySoftwareNowInputRequestTypeDef",
    "UpdateSMBFileShareVisibilityInputRequestTypeDef",
    "UpdateSMBSecurityStrategyInputRequestTypeDef",
    "UpdateVTLDeviceTypeInputRequestTypeDef",
    "ActivateGatewayInputRequestTypeDef",
    "AddTagsToResourceInputRequestTypeDef",
    "CreateCachediSCSIVolumeInputRequestTypeDef",
    "CreateSnapshotFromVolumeRecoveryPointInputRequestTypeDef",
    "CreateSnapshotInputRequestTypeDef",
    "CreateStorediSCSIVolumeInputRequestTypeDef",
    "CreateTapePoolInputRequestTypeDef",
    "CreateTapeWithBarcodeInputRequestTypeDef",
    "CreateTapesInputRequestTypeDef",
    "UpdateSnapshotScheduleInputRequestTypeDef",
    "ActivateGatewayOutputTypeDef",
    "AddCacheOutputTypeDef",
    "AddTagsToResourceOutputTypeDef",
    "AddUploadBufferOutputTypeDef",
    "AddWorkingStorageOutputTypeDef",
    "AssignTapePoolOutputTypeDef",
    "AssociateFileSystemOutputTypeDef",
    "AttachVolumeOutputTypeDef",
    "CancelArchivalOutputTypeDef",
    "CancelRetrievalOutputTypeDef",
    "CreateCachediSCSIVolumeOutputTypeDef",
    "CreateNFSFileShareOutputTypeDef",
    "CreateSMBFileShareOutputTypeDef",
    "CreateSnapshotFromVolumeRecoveryPointOutputTypeDef",
    "CreateSnapshotOutputTypeDef",
    "CreateStorediSCSIVolumeOutputTypeDef",
    "CreateTapePoolOutputTypeDef",
    "CreateTapeWithBarcodeOutputTypeDef",
    "CreateTapesOutputTypeDef",
    "DeleteAutomaticTapeCreationPolicyOutputTypeDef",
    "DeleteBandwidthRateLimitOutputTypeDef",
    "DeleteChapCredentialsOutputTypeDef",
    "DeleteFileShareOutputTypeDef",
    "DeleteGatewayOutputTypeDef",
    "DeleteSnapshotScheduleOutputTypeDef",
    "DeleteTapeArchiveOutputTypeDef",
    "DeleteTapeOutputTypeDef",
    "DeleteTapePoolOutputTypeDef",
    "DeleteVolumeOutputTypeDef",
    "DescribeAvailabilityMonitorTestOutputTypeDef",
    "DescribeBandwidthRateLimitOutputTypeDef",
    "DescribeCacheOutputTypeDef",
    "DescribeSnapshotScheduleOutputTypeDef",
    "DescribeUploadBufferOutputTypeDef",
    "DescribeWorkingStorageOutputTypeDef",
    "DetachVolumeOutputTypeDef",
    "DisableGatewayOutputTypeDef",
    "DisassociateFileSystemOutputTypeDef",
    "JoinDomainOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListVolumeInitiatorsOutputTypeDef",
    "NotifyWhenUploadedOutputTypeDef",
    "RefreshCacheOutputTypeDef",
    "RemoveTagsFromResourceOutputTypeDef",
    "ResetCacheOutputTypeDef",
    "RetrieveTapeArchiveOutputTypeDef",
    "RetrieveTapeRecoveryPointOutputTypeDef",
    "SetLocalConsolePasswordOutputTypeDef",
    "SetSMBGuestPasswordOutputTypeDef",
    "ShutdownGatewayOutputTypeDef",
    "StartAvailabilityMonitorTestOutputTypeDef",
    "StartGatewayOutputTypeDef",
    "UpdateAutomaticTapeCreationPolicyOutputTypeDef",
    "UpdateBandwidthRateLimitOutputTypeDef",
    "UpdateBandwidthRateLimitScheduleOutputTypeDef",
    "UpdateChapCredentialsOutputTypeDef",
    "UpdateFileSystemAssociationOutputTypeDef",
    "UpdateGatewayInformationOutputTypeDef",
    "UpdateGatewaySoftwareNowOutputTypeDef",
    "UpdateMaintenanceStartTimeOutputTypeDef",
    "UpdateNFSFileShareOutputTypeDef",
    "UpdateSMBFileShareOutputTypeDef",
    "UpdateSMBFileShareVisibilityOutputTypeDef",
    "UpdateSMBLocalGroupsOutputTypeDef",
    "UpdateSMBSecurityStrategyOutputTypeDef",
    "UpdateSnapshotScheduleOutputTypeDef",
    "UpdateVTLDeviceTypeOutputTypeDef",
    "CreateSMBFileShareInputRequestTypeDef",
    "SMBFileShareInfoTypeDef",
    "UpdateFileSystemAssociationInputRequestTypeDef",
    "UpdateSMBFileShareInputRequestTypeDef",
    "AssociateFileSystemInputRequestTypeDef",
    "AutomaticTapeCreationPolicyInfoTypeDef",
    "UpdateAutomaticTapeCreationPolicyInputRequestTypeDef",
    "DescribeBandwidthRateLimitScheduleOutputTypeDef",
    "BandwidthRateLimitIntervalUnionTypeDef",
    "CachediSCSIVolumeTypeDef",
    "StorediSCSIVolumeTypeDef",
    "DescribeChapCredentialsOutputTypeDef",
    "CreateNFSFileShareInputRequestTypeDef",
    "NFSFileShareInfoTypeDef",
    "UpdateNFSFileShareInputRequestTypeDef",
    "DescribeGatewayInformationOutputTypeDef",
    "DescribeMaintenanceStartTimeOutputTypeDef",
    "UpdateMaintenanceStartTimeInputRequestTypeDef",
    "DescribeSMBSettingsOutputTypeDef",
    "DescribeTapeArchivesInputDescribeTapeArchivesPaginateTypeDef",
    "DescribeTapeRecoveryPointsInputDescribeTapeRecoveryPointsPaginateTypeDef",
    "DescribeTapesInputDescribeTapesPaginateTypeDef",
    "DescribeVTLDevicesInputDescribeVTLDevicesPaginateTypeDef",
    "ListFileSharesInputListFileSharesPaginateTypeDef",
    "ListFileSystemAssociationsInputListFileSystemAssociationsPaginateTypeDef",
    "ListGatewaysInputListGatewaysPaginateTypeDef",
    "ListTagsForResourceInputListTagsForResourcePaginateTypeDef",
    "ListTapePoolsInputListTapePoolsPaginateTypeDef",
    "ListTapesInputListTapesPaginateTypeDef",
    "ListVolumesInputListVolumesPaginateTypeDef",
    "DescribeTapeArchivesOutputTypeDef",
    "DescribeTapeRecoveryPointsOutputTypeDef",
    "DescribeTapesOutputTypeDef",
    "VTLDeviceTypeDef",
    "ListLocalDisksOutputTypeDef",
    "ListFileSharesOutputTypeDef",
    "FileSystemAssociationInfoTypeDef",
    "ListFileSystemAssociationsOutputTypeDef",
    "ListGatewaysOutputTypeDef",
    "ListTapePoolsOutputTypeDef",
    "ListTapesOutputTypeDef",
    "ListVolumeRecoveryPointsOutputTypeDef",
    "ListVolumesOutputTypeDef",
    "UpdateSMBLocalGroupsInputRequestTypeDef",
    "DescribeSMBFileSharesOutputTypeDef",
    "ListAutomaticTapeCreationPoliciesOutputTypeDef",
    "UpdateBandwidthRateLimitScheduleInputRequestTypeDef",
    "DescribeCachediSCSIVolumesOutputTypeDef",
    "DescribeStorediSCSIVolumesOutputTypeDef",
    "DescribeNFSFileSharesOutputTypeDef",
    "DescribeVTLDevicesOutputTypeDef",
    "DescribeFileSystemAssociationsOutputTypeDef",
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
AddCacheInputRequestTypeDef = TypedDict(
    "AddCacheInputRequestTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": Sequence[str],
    },
)
AddUploadBufferInputRequestTypeDef = TypedDict(
    "AddUploadBufferInputRequestTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": Sequence[str],
    },
)
AddWorkingStorageInputRequestTypeDef = TypedDict(
    "AddWorkingStorageInputRequestTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": Sequence[str],
    },
)
AssignTapePoolInputRequestTypeDef = TypedDict(
    "AssignTapePoolInputRequestTypeDef",
    {
        "TapeARN": str,
        "PoolId": str,
        "BypassGovernanceRetention": NotRequired[bool],
    },
)
CacheAttributesTypeDef = TypedDict(
    "CacheAttributesTypeDef",
    {
        "CacheStaleTimeoutInSeconds": NotRequired[int],
    },
)
EndpointNetworkConfigurationTypeDef = TypedDict(
    "EndpointNetworkConfigurationTypeDef",
    {
        "IpAddresses": NotRequired[Sequence[str]],
    },
)
AttachVolumeInputRequestTypeDef = TypedDict(
    "AttachVolumeInputRequestTypeDef",
    {
        "GatewayARN": str,
        "VolumeARN": str,
        "NetworkInterfaceId": str,
        "TargetName": NotRequired[str],
        "DiskId": NotRequired[str],
    },
)
AutomaticTapeCreationRuleTypeDef = TypedDict(
    "AutomaticTapeCreationRuleTypeDef",
    {
        "TapeBarcodePrefix": str,
        "PoolId": str,
        "TapeSizeInBytes": int,
        "MinimumNumTapes": int,
        "Worm": NotRequired[bool],
    },
)
BandwidthRateLimitIntervalOutputTypeDef = TypedDict(
    "BandwidthRateLimitIntervalOutputTypeDef",
    {
        "StartHourOfDay": int,
        "StartMinuteOfHour": int,
        "EndHourOfDay": int,
        "EndMinuteOfHour": int,
        "DaysOfWeek": List[int],
        "AverageUploadRateLimitInBitsPerSec": NotRequired[int],
        "AverageDownloadRateLimitInBitsPerSec": NotRequired[int],
    },
)
BandwidthRateLimitIntervalTypeDef = TypedDict(
    "BandwidthRateLimitIntervalTypeDef",
    {
        "StartHourOfDay": int,
        "StartMinuteOfHour": int,
        "EndHourOfDay": int,
        "EndMinuteOfHour": int,
        "DaysOfWeek": Sequence[int],
        "AverageUploadRateLimitInBitsPerSec": NotRequired[int],
        "AverageDownloadRateLimitInBitsPerSec": NotRequired[int],
    },
)
VolumeiSCSIAttributesTypeDef = TypedDict(
    "VolumeiSCSIAttributesTypeDef",
    {
        "TargetARN": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "NetworkInterfacePort": NotRequired[int],
        "LunNumber": NotRequired[int],
        "ChapEnabled": NotRequired[bool],
    },
)
CancelArchivalInputRequestTypeDef = TypedDict(
    "CancelArchivalInputRequestTypeDef",
    {
        "GatewayARN": str,
        "TapeARN": str,
    },
)
CancelRetrievalInputRequestTypeDef = TypedDict(
    "CancelRetrievalInputRequestTypeDef",
    {
        "GatewayARN": str,
        "TapeARN": str,
    },
)
ChapInfoTypeDef = TypedDict(
    "ChapInfoTypeDef",
    {
        "TargetARN": NotRequired[str],
        "SecretToAuthenticateInitiator": NotRequired[str],
        "InitiatorName": NotRequired[str],
        "SecretToAuthenticateTarget": NotRequired[str],
    },
)
NFSFileShareDefaultsTypeDef = TypedDict(
    "NFSFileShareDefaultsTypeDef",
    {
        "FileMode": NotRequired[str],
        "DirectoryMode": NotRequired[str],
        "GroupId": NotRequired[int],
        "OwnerId": NotRequired[int],
    },
)
DeleteAutomaticTapeCreationPolicyInputRequestTypeDef = TypedDict(
    "DeleteAutomaticTapeCreationPolicyInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)
DeleteBandwidthRateLimitInputRequestTypeDef = TypedDict(
    "DeleteBandwidthRateLimitInputRequestTypeDef",
    {
        "GatewayARN": str,
        "BandwidthType": str,
    },
)
DeleteChapCredentialsInputRequestTypeDef = TypedDict(
    "DeleteChapCredentialsInputRequestTypeDef",
    {
        "TargetARN": str,
        "InitiatorName": str,
    },
)
DeleteFileShareInputRequestTypeDef = TypedDict(
    "DeleteFileShareInputRequestTypeDef",
    {
        "FileShareARN": str,
        "ForceDelete": NotRequired[bool],
    },
)
DeleteGatewayInputRequestTypeDef = TypedDict(
    "DeleteGatewayInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)
DeleteSnapshotScheduleInputRequestTypeDef = TypedDict(
    "DeleteSnapshotScheduleInputRequestTypeDef",
    {
        "VolumeARN": str,
    },
)
DeleteTapeArchiveInputRequestTypeDef = TypedDict(
    "DeleteTapeArchiveInputRequestTypeDef",
    {
        "TapeARN": str,
        "BypassGovernanceRetention": NotRequired[bool],
    },
)
DeleteTapeInputRequestTypeDef = TypedDict(
    "DeleteTapeInputRequestTypeDef",
    {
        "GatewayARN": str,
        "TapeARN": str,
        "BypassGovernanceRetention": NotRequired[bool],
    },
)
DeleteTapePoolInputRequestTypeDef = TypedDict(
    "DeleteTapePoolInputRequestTypeDef",
    {
        "PoolARN": str,
    },
)
DeleteVolumeInputRequestTypeDef = TypedDict(
    "DeleteVolumeInputRequestTypeDef",
    {
        "VolumeARN": str,
    },
)
DescribeAvailabilityMonitorTestInputRequestTypeDef = TypedDict(
    "DescribeAvailabilityMonitorTestInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)
DescribeBandwidthRateLimitInputRequestTypeDef = TypedDict(
    "DescribeBandwidthRateLimitInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)
DescribeBandwidthRateLimitScheduleInputRequestTypeDef = TypedDict(
    "DescribeBandwidthRateLimitScheduleInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)
DescribeCacheInputRequestTypeDef = TypedDict(
    "DescribeCacheInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)
DescribeCachediSCSIVolumesInputRequestTypeDef = TypedDict(
    "DescribeCachediSCSIVolumesInputRequestTypeDef",
    {
        "VolumeARNs": Sequence[str],
    },
)
DescribeChapCredentialsInputRequestTypeDef = TypedDict(
    "DescribeChapCredentialsInputRequestTypeDef",
    {
        "TargetARN": str,
    },
)
DescribeFileSystemAssociationsInputRequestTypeDef = TypedDict(
    "DescribeFileSystemAssociationsInputRequestTypeDef",
    {
        "FileSystemAssociationARNList": Sequence[str],
    },
)
DescribeGatewayInformationInputRequestTypeDef = TypedDict(
    "DescribeGatewayInformationInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)
NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "Ipv4Address": NotRequired[str],
        "MacAddress": NotRequired[str],
        "Ipv6Address": NotRequired[str],
    },
)
DescribeMaintenanceStartTimeInputRequestTypeDef = TypedDict(
    "DescribeMaintenanceStartTimeInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)
SoftwareUpdatePreferencesTypeDef = TypedDict(
    "SoftwareUpdatePreferencesTypeDef",
    {
        "AutomaticUpdatePolicy": NotRequired[AutomaticUpdatePolicyType],
    },
)
DescribeNFSFileSharesInputRequestTypeDef = TypedDict(
    "DescribeNFSFileSharesInputRequestTypeDef",
    {
        "FileShareARNList": Sequence[str],
    },
)
DescribeSMBFileSharesInputRequestTypeDef = TypedDict(
    "DescribeSMBFileSharesInputRequestTypeDef",
    {
        "FileShareARNList": Sequence[str],
    },
)
DescribeSMBSettingsInputRequestTypeDef = TypedDict(
    "DescribeSMBSettingsInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)
SMBLocalGroupsOutputTypeDef = TypedDict(
    "SMBLocalGroupsOutputTypeDef",
    {
        "GatewayAdmins": NotRequired[List[str]],
    },
)
DescribeSnapshotScheduleInputRequestTypeDef = TypedDict(
    "DescribeSnapshotScheduleInputRequestTypeDef",
    {
        "VolumeARN": str,
    },
)
DescribeStorediSCSIVolumesInputRequestTypeDef = TypedDict(
    "DescribeStorediSCSIVolumesInputRequestTypeDef",
    {
        "VolumeARNs": Sequence[str],
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
DescribeTapeArchivesInputRequestTypeDef = TypedDict(
    "DescribeTapeArchivesInputRequestTypeDef",
    {
        "TapeARNs": NotRequired[Sequence[str]],
        "Marker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
TapeArchiveTypeDef = TypedDict(
    "TapeArchiveTypeDef",
    {
        "TapeARN": NotRequired[str],
        "TapeBarcode": NotRequired[str],
        "TapeCreatedDate": NotRequired[datetime],
        "TapeSizeInBytes": NotRequired[int],
        "CompletionTime": NotRequired[datetime],
        "RetrievedTo": NotRequired[str],
        "TapeStatus": NotRequired[str],
        "TapeUsedInBytes": NotRequired[int],
        "KMSKey": NotRequired[str],
        "PoolId": NotRequired[str],
        "Worm": NotRequired[bool],
        "RetentionStartDate": NotRequired[datetime],
        "PoolEntryDate": NotRequired[datetime],
    },
)
DescribeTapeRecoveryPointsInputRequestTypeDef = TypedDict(
    "DescribeTapeRecoveryPointsInputRequestTypeDef",
    {
        "GatewayARN": str,
        "Marker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
TapeRecoveryPointInfoTypeDef = TypedDict(
    "TapeRecoveryPointInfoTypeDef",
    {
        "TapeARN": NotRequired[str],
        "TapeRecoveryPointTime": NotRequired[datetime],
        "TapeSizeInBytes": NotRequired[int],
        "TapeStatus": NotRequired[str],
    },
)
DescribeTapesInputRequestTypeDef = TypedDict(
    "DescribeTapesInputRequestTypeDef",
    {
        "GatewayARN": str,
        "TapeARNs": NotRequired[Sequence[str]],
        "Marker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
TapeTypeDef = TypedDict(
    "TapeTypeDef",
    {
        "TapeARN": NotRequired[str],
        "TapeBarcode": NotRequired[str],
        "TapeCreatedDate": NotRequired[datetime],
        "TapeSizeInBytes": NotRequired[int],
        "TapeStatus": NotRequired[str],
        "VTLDevice": NotRequired[str],
        "Progress": NotRequired[float],
        "TapeUsedInBytes": NotRequired[int],
        "KMSKey": NotRequired[str],
        "PoolId": NotRequired[str],
        "Worm": NotRequired[bool],
        "RetentionStartDate": NotRequired[datetime],
        "PoolEntryDate": NotRequired[datetime],
    },
)
DescribeUploadBufferInputRequestTypeDef = TypedDict(
    "DescribeUploadBufferInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)
DescribeVTLDevicesInputRequestTypeDef = TypedDict(
    "DescribeVTLDevicesInputRequestTypeDef",
    {
        "GatewayARN": str,
        "VTLDeviceARNs": NotRequired[Sequence[str]],
        "Marker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
DescribeWorkingStorageInputRequestTypeDef = TypedDict(
    "DescribeWorkingStorageInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)
DetachVolumeInputRequestTypeDef = TypedDict(
    "DetachVolumeInputRequestTypeDef",
    {
        "VolumeARN": str,
        "ForceDetach": NotRequired[bool],
    },
)
DeviceiSCSIAttributesTypeDef = TypedDict(
    "DeviceiSCSIAttributesTypeDef",
    {
        "TargetARN": NotRequired[str],
        "NetworkInterfaceId": NotRequired[str],
        "NetworkInterfacePort": NotRequired[int],
        "ChapEnabled": NotRequired[bool],
    },
)
DisableGatewayInputRequestTypeDef = TypedDict(
    "DisableGatewayInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)
DisassociateFileSystemInputRequestTypeDef = TypedDict(
    "DisassociateFileSystemInputRequestTypeDef",
    {
        "FileSystemAssociationARN": str,
        "ForceDelete": NotRequired[bool],
    },
)
DiskTypeDef = TypedDict(
    "DiskTypeDef",
    {
        "DiskId": NotRequired[str],
        "DiskPath": NotRequired[str],
        "DiskNode": NotRequired[str],
        "DiskStatus": NotRequired[str],
        "DiskSizeInBytes": NotRequired[int],
        "DiskAllocationType": NotRequired[str],
        "DiskAllocationResource": NotRequired[str],
        "DiskAttributeList": NotRequired[List[str]],
    },
)
EndpointNetworkConfigurationOutputTypeDef = TypedDict(
    "EndpointNetworkConfigurationOutputTypeDef",
    {
        "IpAddresses": NotRequired[List[str]],
    },
)
FileShareInfoTypeDef = TypedDict(
    "FileShareInfoTypeDef",
    {
        "FileShareType": NotRequired[FileShareTypeType],
        "FileShareARN": NotRequired[str],
        "FileShareId": NotRequired[str],
        "FileShareStatus": NotRequired[str],
        "GatewayARN": NotRequired[str],
    },
)
FileSystemAssociationStatusDetailTypeDef = TypedDict(
    "FileSystemAssociationStatusDetailTypeDef",
    {
        "ErrorCode": NotRequired[str],
    },
)
FileSystemAssociationSummaryTypeDef = TypedDict(
    "FileSystemAssociationSummaryTypeDef",
    {
        "FileSystemAssociationId": NotRequired[str],
        "FileSystemAssociationARN": NotRequired[str],
        "FileSystemAssociationStatus": NotRequired[str],
        "GatewayARN": NotRequired[str],
    },
)
GatewayInfoTypeDef = TypedDict(
    "GatewayInfoTypeDef",
    {
        "GatewayId": NotRequired[str],
        "GatewayARN": NotRequired[str],
        "GatewayType": NotRequired[str],
        "GatewayOperationalState": NotRequired[str],
        "GatewayName": NotRequired[str],
        "Ec2InstanceId": NotRequired[str],
        "Ec2InstanceRegion": NotRequired[str],
        "HostEnvironment": NotRequired[HostEnvironmentType],
        "HostEnvironmentId": NotRequired[str],
        "DeprecationDate": NotRequired[str],
        "SoftwareVersion": NotRequired[str],
    },
)
JoinDomainInputRequestTypeDef = TypedDict(
    "JoinDomainInputRequestTypeDef",
    {
        "GatewayARN": str,
        "DomainName": str,
        "UserName": str,
        "Password": str,
        "OrganizationalUnit": NotRequired[str],
        "DomainControllers": NotRequired[Sequence[str]],
        "TimeoutInSeconds": NotRequired[int],
    },
)
ListAutomaticTapeCreationPoliciesInputRequestTypeDef = TypedDict(
    "ListAutomaticTapeCreationPoliciesInputRequestTypeDef",
    {
        "GatewayARN": NotRequired[str],
    },
)
ListFileSharesInputRequestTypeDef = TypedDict(
    "ListFileSharesInputRequestTypeDef",
    {
        "GatewayARN": NotRequired[str],
        "Limit": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
ListFileSystemAssociationsInputRequestTypeDef = TypedDict(
    "ListFileSystemAssociationsInputRequestTypeDef",
    {
        "GatewayARN": NotRequired[str],
        "Limit": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
ListGatewaysInputRequestTypeDef = TypedDict(
    "ListGatewaysInputRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
ListLocalDisksInputRequestTypeDef = TypedDict(
    "ListLocalDisksInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)
ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "Marker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
ListTapePoolsInputRequestTypeDef = TypedDict(
    "ListTapePoolsInputRequestTypeDef",
    {
        "PoolARNs": NotRequired[Sequence[str]],
        "Marker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
PoolInfoTypeDef = TypedDict(
    "PoolInfoTypeDef",
    {
        "PoolARN": NotRequired[str],
        "PoolName": NotRequired[str],
        "StorageClass": NotRequired[TapeStorageClassType],
        "RetentionLockType": NotRequired[RetentionLockTypeType],
        "RetentionLockTimeInDays": NotRequired[int],
        "PoolStatus": NotRequired[PoolStatusType],
    },
)
ListTapesInputRequestTypeDef = TypedDict(
    "ListTapesInputRequestTypeDef",
    {
        "TapeARNs": NotRequired[Sequence[str]],
        "Marker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
TapeInfoTypeDef = TypedDict(
    "TapeInfoTypeDef",
    {
        "TapeARN": NotRequired[str],
        "TapeBarcode": NotRequired[str],
        "TapeSizeInBytes": NotRequired[int],
        "TapeStatus": NotRequired[str],
        "GatewayARN": NotRequired[str],
        "PoolId": NotRequired[str],
        "RetentionStartDate": NotRequired[datetime],
        "PoolEntryDate": NotRequired[datetime],
    },
)
ListVolumeInitiatorsInputRequestTypeDef = TypedDict(
    "ListVolumeInitiatorsInputRequestTypeDef",
    {
        "VolumeARN": str,
    },
)
ListVolumeRecoveryPointsInputRequestTypeDef = TypedDict(
    "ListVolumeRecoveryPointsInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)
VolumeRecoveryPointInfoTypeDef = TypedDict(
    "VolumeRecoveryPointInfoTypeDef",
    {
        "VolumeARN": NotRequired[str],
        "VolumeSizeInBytes": NotRequired[int],
        "VolumeUsageInBytes": NotRequired[int],
        "VolumeRecoveryPointTime": NotRequired[str],
    },
)
ListVolumesInputRequestTypeDef = TypedDict(
    "ListVolumesInputRequestTypeDef",
    {
        "GatewayARN": NotRequired[str],
        "Marker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
VolumeInfoTypeDef = TypedDict(
    "VolumeInfoTypeDef",
    {
        "VolumeARN": NotRequired[str],
        "VolumeId": NotRequired[str],
        "GatewayARN": NotRequired[str],
        "GatewayId": NotRequired[str],
        "VolumeType": NotRequired[str],
        "VolumeSizeInBytes": NotRequired[int],
        "VolumeAttachmentStatus": NotRequired[str],
    },
)
NotifyWhenUploadedInputRequestTypeDef = TypedDict(
    "NotifyWhenUploadedInputRequestTypeDef",
    {
        "FileShareARN": str,
    },
)
RefreshCacheInputRequestTypeDef = TypedDict(
    "RefreshCacheInputRequestTypeDef",
    {
        "FileShareARN": str,
        "FolderList": NotRequired[Sequence[str]],
        "Recursive": NotRequired[bool],
    },
)
RemoveTagsFromResourceInputRequestTypeDef = TypedDict(
    "RemoveTagsFromResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
ResetCacheInputRequestTypeDef = TypedDict(
    "ResetCacheInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)
RetrieveTapeArchiveInputRequestTypeDef = TypedDict(
    "RetrieveTapeArchiveInputRequestTypeDef",
    {
        "TapeARN": str,
        "GatewayARN": str,
    },
)
RetrieveTapeRecoveryPointInputRequestTypeDef = TypedDict(
    "RetrieveTapeRecoveryPointInputRequestTypeDef",
    {
        "TapeARN": str,
        "GatewayARN": str,
    },
)
SMBLocalGroupsTypeDef = TypedDict(
    "SMBLocalGroupsTypeDef",
    {
        "GatewayAdmins": NotRequired[Sequence[str]],
    },
)
SetLocalConsolePasswordInputRequestTypeDef = TypedDict(
    "SetLocalConsolePasswordInputRequestTypeDef",
    {
        "GatewayARN": str,
        "LocalConsolePassword": str,
    },
)
SetSMBGuestPasswordInputRequestTypeDef = TypedDict(
    "SetSMBGuestPasswordInputRequestTypeDef",
    {
        "GatewayARN": str,
        "Password": str,
    },
)
ShutdownGatewayInputRequestTypeDef = TypedDict(
    "ShutdownGatewayInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)
StartAvailabilityMonitorTestInputRequestTypeDef = TypedDict(
    "StartAvailabilityMonitorTestInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)
StartGatewayInputRequestTypeDef = TypedDict(
    "StartGatewayInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)
UpdateBandwidthRateLimitInputRequestTypeDef = TypedDict(
    "UpdateBandwidthRateLimitInputRequestTypeDef",
    {
        "GatewayARN": str,
        "AverageUploadRateLimitInBitsPerSec": NotRequired[int],
        "AverageDownloadRateLimitInBitsPerSec": NotRequired[int],
    },
)
UpdateChapCredentialsInputRequestTypeDef = TypedDict(
    "UpdateChapCredentialsInputRequestTypeDef",
    {
        "TargetARN": str,
        "SecretToAuthenticateInitiator": str,
        "InitiatorName": str,
        "SecretToAuthenticateTarget": NotRequired[str],
    },
)
UpdateGatewayInformationInputRequestTypeDef = TypedDict(
    "UpdateGatewayInformationInputRequestTypeDef",
    {
        "GatewayARN": str,
        "GatewayName": NotRequired[str],
        "GatewayTimezone": NotRequired[str],
        "CloudWatchLogGroupARN": NotRequired[str],
        "GatewayCapacity": NotRequired[GatewayCapacityType],
    },
)
UpdateGatewaySoftwareNowInputRequestTypeDef = TypedDict(
    "UpdateGatewaySoftwareNowInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)
UpdateSMBFileShareVisibilityInputRequestTypeDef = TypedDict(
    "UpdateSMBFileShareVisibilityInputRequestTypeDef",
    {
        "GatewayARN": str,
        "FileSharesVisible": bool,
    },
)
UpdateSMBSecurityStrategyInputRequestTypeDef = TypedDict(
    "UpdateSMBSecurityStrategyInputRequestTypeDef",
    {
        "GatewayARN": str,
        "SMBSecurityStrategy": SMBSecurityStrategyType,
    },
)
UpdateVTLDeviceTypeInputRequestTypeDef = TypedDict(
    "UpdateVTLDeviceTypeInputRequestTypeDef",
    {
        "VTLDeviceARN": str,
        "DeviceType": str,
    },
)
ActivateGatewayInputRequestTypeDef = TypedDict(
    "ActivateGatewayInputRequestTypeDef",
    {
        "ActivationKey": str,
        "GatewayName": str,
        "GatewayTimezone": str,
        "GatewayRegion": str,
        "GatewayType": NotRequired[str],
        "TapeDriveType": NotRequired[str],
        "MediumChangerType": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
AddTagsToResourceInputRequestTypeDef = TypedDict(
    "AddTagsToResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CreateCachediSCSIVolumeInputRequestTypeDef = TypedDict(
    "CreateCachediSCSIVolumeInputRequestTypeDef",
    {
        "GatewayARN": str,
        "VolumeSizeInBytes": int,
        "TargetName": str,
        "NetworkInterfaceId": str,
        "ClientToken": str,
        "SnapshotId": NotRequired[str],
        "SourceVolumeARN": NotRequired[str],
        "KMSEncrypted": NotRequired[bool],
        "KMSKey": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateSnapshotFromVolumeRecoveryPointInputRequestTypeDef = TypedDict(
    "CreateSnapshotFromVolumeRecoveryPointInputRequestTypeDef",
    {
        "VolumeARN": str,
        "SnapshotDescription": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateSnapshotInputRequestTypeDef = TypedDict(
    "CreateSnapshotInputRequestTypeDef",
    {
        "VolumeARN": str,
        "SnapshotDescription": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateStorediSCSIVolumeInputRequestTypeDef = TypedDict(
    "CreateStorediSCSIVolumeInputRequestTypeDef",
    {
        "GatewayARN": str,
        "DiskId": str,
        "PreserveExistingData": bool,
        "TargetName": str,
        "NetworkInterfaceId": str,
        "SnapshotId": NotRequired[str],
        "KMSEncrypted": NotRequired[bool],
        "KMSKey": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateTapePoolInputRequestTypeDef = TypedDict(
    "CreateTapePoolInputRequestTypeDef",
    {
        "PoolName": str,
        "StorageClass": TapeStorageClassType,
        "RetentionLockType": NotRequired[RetentionLockTypeType],
        "RetentionLockTimeInDays": NotRequired[int],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateTapeWithBarcodeInputRequestTypeDef = TypedDict(
    "CreateTapeWithBarcodeInputRequestTypeDef",
    {
        "GatewayARN": str,
        "TapeSizeInBytes": int,
        "TapeBarcode": str,
        "KMSEncrypted": NotRequired[bool],
        "KMSKey": NotRequired[str],
        "PoolId": NotRequired[str],
        "Worm": NotRequired[bool],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateTapesInputRequestTypeDef = TypedDict(
    "CreateTapesInputRequestTypeDef",
    {
        "GatewayARN": str,
        "TapeSizeInBytes": int,
        "ClientToken": str,
        "NumTapesToCreate": int,
        "TapeBarcodePrefix": str,
        "KMSEncrypted": NotRequired[bool],
        "KMSKey": NotRequired[str],
        "PoolId": NotRequired[str],
        "Worm": NotRequired[bool],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
UpdateSnapshotScheduleInputRequestTypeDef = TypedDict(
    "UpdateSnapshotScheduleInputRequestTypeDef",
    {
        "VolumeARN": str,
        "StartAt": int,
        "RecurrenceInHours": int,
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ActivateGatewayOutputTypeDef = TypedDict(
    "ActivateGatewayOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AddCacheOutputTypeDef = TypedDict(
    "AddCacheOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AddTagsToResourceOutputTypeDef = TypedDict(
    "AddTagsToResourceOutputTypeDef",
    {
        "ResourceARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AddUploadBufferOutputTypeDef = TypedDict(
    "AddUploadBufferOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AddWorkingStorageOutputTypeDef = TypedDict(
    "AddWorkingStorageOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssignTapePoolOutputTypeDef = TypedDict(
    "AssignTapePoolOutputTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateFileSystemOutputTypeDef = TypedDict(
    "AssociateFileSystemOutputTypeDef",
    {
        "FileSystemAssociationARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AttachVolumeOutputTypeDef = TypedDict(
    "AttachVolumeOutputTypeDef",
    {
        "VolumeARN": str,
        "TargetARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CancelArchivalOutputTypeDef = TypedDict(
    "CancelArchivalOutputTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CancelRetrievalOutputTypeDef = TypedDict(
    "CancelRetrievalOutputTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCachediSCSIVolumeOutputTypeDef = TypedDict(
    "CreateCachediSCSIVolumeOutputTypeDef",
    {
        "VolumeARN": str,
        "TargetARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateNFSFileShareOutputTypeDef = TypedDict(
    "CreateNFSFileShareOutputTypeDef",
    {
        "FileShareARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSMBFileShareOutputTypeDef = TypedDict(
    "CreateSMBFileShareOutputTypeDef",
    {
        "FileShareARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSnapshotFromVolumeRecoveryPointOutputTypeDef = TypedDict(
    "CreateSnapshotFromVolumeRecoveryPointOutputTypeDef",
    {
        "SnapshotId": str,
        "VolumeARN": str,
        "VolumeRecoveryPointTime": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSnapshotOutputTypeDef = TypedDict(
    "CreateSnapshotOutputTypeDef",
    {
        "VolumeARN": str,
        "SnapshotId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateStorediSCSIVolumeOutputTypeDef = TypedDict(
    "CreateStorediSCSIVolumeOutputTypeDef",
    {
        "VolumeARN": str,
        "VolumeSizeInBytes": int,
        "TargetARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTapePoolOutputTypeDef = TypedDict(
    "CreateTapePoolOutputTypeDef",
    {
        "PoolARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTapeWithBarcodeOutputTypeDef = TypedDict(
    "CreateTapeWithBarcodeOutputTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTapesOutputTypeDef = TypedDict(
    "CreateTapesOutputTypeDef",
    {
        "TapeARNs": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteAutomaticTapeCreationPolicyOutputTypeDef = TypedDict(
    "DeleteAutomaticTapeCreationPolicyOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteBandwidthRateLimitOutputTypeDef = TypedDict(
    "DeleteBandwidthRateLimitOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteChapCredentialsOutputTypeDef = TypedDict(
    "DeleteChapCredentialsOutputTypeDef",
    {
        "TargetARN": str,
        "InitiatorName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteFileShareOutputTypeDef = TypedDict(
    "DeleteFileShareOutputTypeDef",
    {
        "FileShareARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteGatewayOutputTypeDef = TypedDict(
    "DeleteGatewayOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteSnapshotScheduleOutputTypeDef = TypedDict(
    "DeleteSnapshotScheduleOutputTypeDef",
    {
        "VolumeARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTapeArchiveOutputTypeDef = TypedDict(
    "DeleteTapeArchiveOutputTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTapeOutputTypeDef = TypedDict(
    "DeleteTapeOutputTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTapePoolOutputTypeDef = TypedDict(
    "DeleteTapePoolOutputTypeDef",
    {
        "PoolARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteVolumeOutputTypeDef = TypedDict(
    "DeleteVolumeOutputTypeDef",
    {
        "VolumeARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAvailabilityMonitorTestOutputTypeDef = TypedDict(
    "DescribeAvailabilityMonitorTestOutputTypeDef",
    {
        "GatewayARN": str,
        "Status": AvailabilityMonitorTestStatusType,
        "StartTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeBandwidthRateLimitOutputTypeDef = TypedDict(
    "DescribeBandwidthRateLimitOutputTypeDef",
    {
        "GatewayARN": str,
        "AverageUploadRateLimitInBitsPerSec": int,
        "AverageDownloadRateLimitInBitsPerSec": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeCacheOutputTypeDef = TypedDict(
    "DescribeCacheOutputTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
        "CacheAllocatedInBytes": int,
        "CacheUsedPercentage": float,
        "CacheDirtyPercentage": float,
        "CacheHitPercentage": float,
        "CacheMissPercentage": float,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSnapshotScheduleOutputTypeDef = TypedDict(
    "DescribeSnapshotScheduleOutputTypeDef",
    {
        "VolumeARN": str,
        "StartAt": int,
        "RecurrenceInHours": int,
        "Description": str,
        "Timezone": str,
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeUploadBufferOutputTypeDef = TypedDict(
    "DescribeUploadBufferOutputTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
        "UploadBufferUsedInBytes": int,
        "UploadBufferAllocatedInBytes": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeWorkingStorageOutputTypeDef = TypedDict(
    "DescribeWorkingStorageOutputTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
        "WorkingStorageUsedInBytes": int,
        "WorkingStorageAllocatedInBytes": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DetachVolumeOutputTypeDef = TypedDict(
    "DetachVolumeOutputTypeDef",
    {
        "VolumeARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisableGatewayOutputTypeDef = TypedDict(
    "DisableGatewayOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateFileSystemOutputTypeDef = TypedDict(
    "DisassociateFileSystemOutputTypeDef",
    {
        "FileSystemAssociationARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
JoinDomainOutputTypeDef = TypedDict(
    "JoinDomainOutputTypeDef",
    {
        "GatewayARN": str,
        "ActiveDirectoryStatus": ActiveDirectoryStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "ResourceARN": str,
        "Marker": str,
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListVolumeInitiatorsOutputTypeDef = TypedDict(
    "ListVolumeInitiatorsOutputTypeDef",
    {
        "Initiators": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NotifyWhenUploadedOutputTypeDef = TypedDict(
    "NotifyWhenUploadedOutputTypeDef",
    {
        "FileShareARN": str,
        "NotificationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RefreshCacheOutputTypeDef = TypedDict(
    "RefreshCacheOutputTypeDef",
    {
        "FileShareARN": str,
        "NotificationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RemoveTagsFromResourceOutputTypeDef = TypedDict(
    "RemoveTagsFromResourceOutputTypeDef",
    {
        "ResourceARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResetCacheOutputTypeDef = TypedDict(
    "ResetCacheOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RetrieveTapeArchiveOutputTypeDef = TypedDict(
    "RetrieveTapeArchiveOutputTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RetrieveTapeRecoveryPointOutputTypeDef = TypedDict(
    "RetrieveTapeRecoveryPointOutputTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SetLocalConsolePasswordOutputTypeDef = TypedDict(
    "SetLocalConsolePasswordOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SetSMBGuestPasswordOutputTypeDef = TypedDict(
    "SetSMBGuestPasswordOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ShutdownGatewayOutputTypeDef = TypedDict(
    "ShutdownGatewayOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartAvailabilityMonitorTestOutputTypeDef = TypedDict(
    "StartAvailabilityMonitorTestOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartGatewayOutputTypeDef = TypedDict(
    "StartGatewayOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAutomaticTapeCreationPolicyOutputTypeDef = TypedDict(
    "UpdateAutomaticTapeCreationPolicyOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateBandwidthRateLimitOutputTypeDef = TypedDict(
    "UpdateBandwidthRateLimitOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateBandwidthRateLimitScheduleOutputTypeDef = TypedDict(
    "UpdateBandwidthRateLimitScheduleOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateChapCredentialsOutputTypeDef = TypedDict(
    "UpdateChapCredentialsOutputTypeDef",
    {
        "TargetARN": str,
        "InitiatorName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFileSystemAssociationOutputTypeDef = TypedDict(
    "UpdateFileSystemAssociationOutputTypeDef",
    {
        "FileSystemAssociationARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateGatewayInformationOutputTypeDef = TypedDict(
    "UpdateGatewayInformationOutputTypeDef",
    {
        "GatewayARN": str,
        "GatewayName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateGatewaySoftwareNowOutputTypeDef = TypedDict(
    "UpdateGatewaySoftwareNowOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateMaintenanceStartTimeOutputTypeDef = TypedDict(
    "UpdateMaintenanceStartTimeOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateNFSFileShareOutputTypeDef = TypedDict(
    "UpdateNFSFileShareOutputTypeDef",
    {
        "FileShareARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSMBFileShareOutputTypeDef = TypedDict(
    "UpdateSMBFileShareOutputTypeDef",
    {
        "FileShareARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSMBFileShareVisibilityOutputTypeDef = TypedDict(
    "UpdateSMBFileShareVisibilityOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSMBLocalGroupsOutputTypeDef = TypedDict(
    "UpdateSMBLocalGroupsOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSMBSecurityStrategyOutputTypeDef = TypedDict(
    "UpdateSMBSecurityStrategyOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSnapshotScheduleOutputTypeDef = TypedDict(
    "UpdateSnapshotScheduleOutputTypeDef",
    {
        "VolumeARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateVTLDeviceTypeOutputTypeDef = TypedDict(
    "UpdateVTLDeviceTypeOutputTypeDef",
    {
        "VTLDeviceARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSMBFileShareInputRequestTypeDef = TypedDict(
    "CreateSMBFileShareInputRequestTypeDef",
    {
        "ClientToken": str,
        "GatewayARN": str,
        "Role": str,
        "LocationARN": str,
        "EncryptionType": NotRequired[EncryptionTypeType],
        "KMSEncrypted": NotRequired[bool],
        "KMSKey": NotRequired[str],
        "DefaultStorageClass": NotRequired[str],
        "ObjectACL": NotRequired[ObjectACLType],
        "ReadOnly": NotRequired[bool],
        "GuessMIMETypeEnabled": NotRequired[bool],
        "RequesterPays": NotRequired[bool],
        "SMBACLEnabled": NotRequired[bool],
        "AccessBasedEnumeration": NotRequired[bool],
        "AdminUserList": NotRequired[Sequence[str]],
        "ValidUserList": NotRequired[Sequence[str]],
        "InvalidUserList": NotRequired[Sequence[str]],
        "AuditDestinationARN": NotRequired[str],
        "Authentication": NotRequired[str],
        "CaseSensitivity": NotRequired[CaseSensitivityType],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "FileShareName": NotRequired[str],
        "CacheAttributes": NotRequired[CacheAttributesTypeDef],
        "NotificationPolicy": NotRequired[str],
        "VPCEndpointDNSName": NotRequired[str],
        "BucketRegion": NotRequired[str],
        "OplocksEnabled": NotRequired[bool],
    },
)
SMBFileShareInfoTypeDef = TypedDict(
    "SMBFileShareInfoTypeDef",
    {
        "FileShareARN": NotRequired[str],
        "FileShareId": NotRequired[str],
        "FileShareStatus": NotRequired[str],
        "GatewayARN": NotRequired[str],
        "EncryptionType": NotRequired[EncryptionTypeType],
        "KMSEncrypted": NotRequired[bool],
        "KMSKey": NotRequired[str],
        "Path": NotRequired[str],
        "Role": NotRequired[str],
        "LocationARN": NotRequired[str],
        "DefaultStorageClass": NotRequired[str],
        "ObjectACL": NotRequired[ObjectACLType],
        "ReadOnly": NotRequired[bool],
        "GuessMIMETypeEnabled": NotRequired[bool],
        "RequesterPays": NotRequired[bool],
        "SMBACLEnabled": NotRequired[bool],
        "AccessBasedEnumeration": NotRequired[bool],
        "AdminUserList": NotRequired[List[str]],
        "ValidUserList": NotRequired[List[str]],
        "InvalidUserList": NotRequired[List[str]],
        "AuditDestinationARN": NotRequired[str],
        "Authentication": NotRequired[str],
        "CaseSensitivity": NotRequired[CaseSensitivityType],
        "Tags": NotRequired[List[TagTypeDef]],
        "FileShareName": NotRequired[str],
        "CacheAttributes": NotRequired[CacheAttributesTypeDef],
        "NotificationPolicy": NotRequired[str],
        "VPCEndpointDNSName": NotRequired[str],
        "BucketRegion": NotRequired[str],
        "OplocksEnabled": NotRequired[bool],
    },
)
UpdateFileSystemAssociationInputRequestTypeDef = TypedDict(
    "UpdateFileSystemAssociationInputRequestTypeDef",
    {
        "FileSystemAssociationARN": str,
        "UserName": NotRequired[str],
        "Password": NotRequired[str],
        "AuditDestinationARN": NotRequired[str],
        "CacheAttributes": NotRequired[CacheAttributesTypeDef],
    },
)
UpdateSMBFileShareInputRequestTypeDef = TypedDict(
    "UpdateSMBFileShareInputRequestTypeDef",
    {
        "FileShareARN": str,
        "EncryptionType": NotRequired[EncryptionTypeType],
        "KMSEncrypted": NotRequired[bool],
        "KMSKey": NotRequired[str],
        "DefaultStorageClass": NotRequired[str],
        "ObjectACL": NotRequired[ObjectACLType],
        "ReadOnly": NotRequired[bool],
        "GuessMIMETypeEnabled": NotRequired[bool],
        "RequesterPays": NotRequired[bool],
        "SMBACLEnabled": NotRequired[bool],
        "AccessBasedEnumeration": NotRequired[bool],
        "AdminUserList": NotRequired[Sequence[str]],
        "ValidUserList": NotRequired[Sequence[str]],
        "InvalidUserList": NotRequired[Sequence[str]],
        "AuditDestinationARN": NotRequired[str],
        "CaseSensitivity": NotRequired[CaseSensitivityType],
        "FileShareName": NotRequired[str],
        "CacheAttributes": NotRequired[CacheAttributesTypeDef],
        "NotificationPolicy": NotRequired[str],
        "OplocksEnabled": NotRequired[bool],
    },
)
AssociateFileSystemInputRequestTypeDef = TypedDict(
    "AssociateFileSystemInputRequestTypeDef",
    {
        "UserName": str,
        "Password": str,
        "ClientToken": str,
        "GatewayARN": str,
        "LocationARN": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "AuditDestinationARN": NotRequired[str],
        "CacheAttributes": NotRequired[CacheAttributesTypeDef],
        "EndpointNetworkConfiguration": NotRequired[EndpointNetworkConfigurationTypeDef],
    },
)
AutomaticTapeCreationPolicyInfoTypeDef = TypedDict(
    "AutomaticTapeCreationPolicyInfoTypeDef",
    {
        "AutomaticTapeCreationRules": NotRequired[List[AutomaticTapeCreationRuleTypeDef]],
        "GatewayARN": NotRequired[str],
    },
)
UpdateAutomaticTapeCreationPolicyInputRequestTypeDef = TypedDict(
    "UpdateAutomaticTapeCreationPolicyInputRequestTypeDef",
    {
        "AutomaticTapeCreationRules": Sequence[AutomaticTapeCreationRuleTypeDef],
        "GatewayARN": str,
    },
)
DescribeBandwidthRateLimitScheduleOutputTypeDef = TypedDict(
    "DescribeBandwidthRateLimitScheduleOutputTypeDef",
    {
        "GatewayARN": str,
        "BandwidthRateLimitIntervals": List[BandwidthRateLimitIntervalOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BandwidthRateLimitIntervalUnionTypeDef = Union[
    BandwidthRateLimitIntervalTypeDef, BandwidthRateLimitIntervalOutputTypeDef
]
CachediSCSIVolumeTypeDef = TypedDict(
    "CachediSCSIVolumeTypeDef",
    {
        "VolumeARN": NotRequired[str],
        "VolumeId": NotRequired[str],
        "VolumeType": NotRequired[str],
        "VolumeStatus": NotRequired[str],
        "VolumeAttachmentStatus": NotRequired[str],
        "VolumeSizeInBytes": NotRequired[int],
        "VolumeProgress": NotRequired[float],
        "SourceSnapshotId": NotRequired[str],
        "VolumeiSCSIAttributes": NotRequired[VolumeiSCSIAttributesTypeDef],
        "CreatedDate": NotRequired[datetime],
        "VolumeUsedInBytes": NotRequired[int],
        "KMSKey": NotRequired[str],
        "TargetName": NotRequired[str],
    },
)
StorediSCSIVolumeTypeDef = TypedDict(
    "StorediSCSIVolumeTypeDef",
    {
        "VolumeARN": NotRequired[str],
        "VolumeId": NotRequired[str],
        "VolumeType": NotRequired[str],
        "VolumeStatus": NotRequired[str],
        "VolumeAttachmentStatus": NotRequired[str],
        "VolumeSizeInBytes": NotRequired[int],
        "VolumeProgress": NotRequired[float],
        "VolumeDiskId": NotRequired[str],
        "SourceSnapshotId": NotRequired[str],
        "PreservedExistingData": NotRequired[bool],
        "VolumeiSCSIAttributes": NotRequired[VolumeiSCSIAttributesTypeDef],
        "CreatedDate": NotRequired[datetime],
        "VolumeUsedInBytes": NotRequired[int],
        "KMSKey": NotRequired[str],
        "TargetName": NotRequired[str],
    },
)
DescribeChapCredentialsOutputTypeDef = TypedDict(
    "DescribeChapCredentialsOutputTypeDef",
    {
        "ChapCredentials": List[ChapInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateNFSFileShareInputRequestTypeDef = TypedDict(
    "CreateNFSFileShareInputRequestTypeDef",
    {
        "ClientToken": str,
        "GatewayARN": str,
        "Role": str,
        "LocationARN": str,
        "NFSFileShareDefaults": NotRequired[NFSFileShareDefaultsTypeDef],
        "EncryptionType": NotRequired[EncryptionTypeType],
        "KMSEncrypted": NotRequired[bool],
        "KMSKey": NotRequired[str],
        "DefaultStorageClass": NotRequired[str],
        "ObjectACL": NotRequired[ObjectACLType],
        "ClientList": NotRequired[Sequence[str]],
        "Squash": NotRequired[str],
        "ReadOnly": NotRequired[bool],
        "GuessMIMETypeEnabled": NotRequired[bool],
        "RequesterPays": NotRequired[bool],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "FileShareName": NotRequired[str],
        "CacheAttributes": NotRequired[CacheAttributesTypeDef],
        "NotificationPolicy": NotRequired[str],
        "VPCEndpointDNSName": NotRequired[str],
        "BucketRegion": NotRequired[str],
        "AuditDestinationARN": NotRequired[str],
    },
)
NFSFileShareInfoTypeDef = TypedDict(
    "NFSFileShareInfoTypeDef",
    {
        "NFSFileShareDefaults": NotRequired[NFSFileShareDefaultsTypeDef],
        "FileShareARN": NotRequired[str],
        "FileShareId": NotRequired[str],
        "FileShareStatus": NotRequired[str],
        "GatewayARN": NotRequired[str],
        "EncryptionType": NotRequired[EncryptionTypeType],
        "KMSEncrypted": NotRequired[bool],
        "KMSKey": NotRequired[str],
        "Path": NotRequired[str],
        "Role": NotRequired[str],
        "LocationARN": NotRequired[str],
        "DefaultStorageClass": NotRequired[str],
        "ObjectACL": NotRequired[ObjectACLType],
        "ClientList": NotRequired[List[str]],
        "Squash": NotRequired[str],
        "ReadOnly": NotRequired[bool],
        "GuessMIMETypeEnabled": NotRequired[bool],
        "RequesterPays": NotRequired[bool],
        "Tags": NotRequired[List[TagTypeDef]],
        "FileShareName": NotRequired[str],
        "CacheAttributes": NotRequired[CacheAttributesTypeDef],
        "NotificationPolicy": NotRequired[str],
        "VPCEndpointDNSName": NotRequired[str],
        "BucketRegion": NotRequired[str],
        "AuditDestinationARN": NotRequired[str],
    },
)
UpdateNFSFileShareInputRequestTypeDef = TypedDict(
    "UpdateNFSFileShareInputRequestTypeDef",
    {
        "FileShareARN": str,
        "EncryptionType": NotRequired[EncryptionTypeType],
        "KMSEncrypted": NotRequired[bool],
        "KMSKey": NotRequired[str],
        "NFSFileShareDefaults": NotRequired[NFSFileShareDefaultsTypeDef],
        "DefaultStorageClass": NotRequired[str],
        "ObjectACL": NotRequired[ObjectACLType],
        "ClientList": NotRequired[Sequence[str]],
        "Squash": NotRequired[str],
        "ReadOnly": NotRequired[bool],
        "GuessMIMETypeEnabled": NotRequired[bool],
        "RequesterPays": NotRequired[bool],
        "FileShareName": NotRequired[str],
        "CacheAttributes": NotRequired[CacheAttributesTypeDef],
        "NotificationPolicy": NotRequired[str],
        "AuditDestinationARN": NotRequired[str],
    },
)
DescribeGatewayInformationOutputTypeDef = TypedDict(
    "DescribeGatewayInformationOutputTypeDef",
    {
        "GatewayARN": str,
        "GatewayId": str,
        "GatewayName": str,
        "GatewayTimezone": str,
        "GatewayState": str,
        "GatewayNetworkInterfaces": List[NetworkInterfaceTypeDef],
        "GatewayType": str,
        "NextUpdateAvailabilityDate": str,
        "LastSoftwareUpdate": str,
        "Ec2InstanceId": str,
        "Ec2InstanceRegion": str,
        "Tags": List[TagTypeDef],
        "VPCEndpoint": str,
        "CloudWatchLogGroupARN": str,
        "HostEnvironment": HostEnvironmentType,
        "EndpointType": str,
        "SoftwareUpdatesEndDate": str,
        "DeprecationDate": str,
        "GatewayCapacity": GatewayCapacityType,
        "SupportedGatewayCapacities": List[GatewayCapacityType],
        "HostEnvironmentId": str,
        "SoftwareVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeMaintenanceStartTimeOutputTypeDef = TypedDict(
    "DescribeMaintenanceStartTimeOutputTypeDef",
    {
        "GatewayARN": str,
        "HourOfDay": int,
        "MinuteOfHour": int,
        "DayOfWeek": int,
        "DayOfMonth": int,
        "Timezone": str,
        "SoftwareUpdatePreferences": SoftwareUpdatePreferencesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateMaintenanceStartTimeInputRequestTypeDef = TypedDict(
    "UpdateMaintenanceStartTimeInputRequestTypeDef",
    {
        "GatewayARN": str,
        "HourOfDay": NotRequired[int],
        "MinuteOfHour": NotRequired[int],
        "DayOfWeek": NotRequired[int],
        "DayOfMonth": NotRequired[int],
        "SoftwareUpdatePreferences": NotRequired[SoftwareUpdatePreferencesTypeDef],
    },
)
DescribeSMBSettingsOutputTypeDef = TypedDict(
    "DescribeSMBSettingsOutputTypeDef",
    {
        "GatewayARN": str,
        "DomainName": str,
        "ActiveDirectoryStatus": ActiveDirectoryStatusType,
        "SMBGuestPasswordSet": bool,
        "SMBSecurityStrategy": SMBSecurityStrategyType,
        "FileSharesVisible": bool,
        "SMBLocalGroups": SMBLocalGroupsOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTapeArchivesInputDescribeTapeArchivesPaginateTypeDef = TypedDict(
    "DescribeTapeArchivesInputDescribeTapeArchivesPaginateTypeDef",
    {
        "TapeARNs": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeTapeRecoveryPointsInputDescribeTapeRecoveryPointsPaginateTypeDef = TypedDict(
    "DescribeTapeRecoveryPointsInputDescribeTapeRecoveryPointsPaginateTypeDef",
    {
        "GatewayARN": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeTapesInputDescribeTapesPaginateTypeDef = TypedDict(
    "DescribeTapesInputDescribeTapesPaginateTypeDef",
    {
        "GatewayARN": str,
        "TapeARNs": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeVTLDevicesInputDescribeVTLDevicesPaginateTypeDef = TypedDict(
    "DescribeVTLDevicesInputDescribeVTLDevicesPaginateTypeDef",
    {
        "GatewayARN": str,
        "VTLDeviceARNs": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFileSharesInputListFileSharesPaginateTypeDef = TypedDict(
    "ListFileSharesInputListFileSharesPaginateTypeDef",
    {
        "GatewayARN": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFileSystemAssociationsInputListFileSystemAssociationsPaginateTypeDef = TypedDict(
    "ListFileSystemAssociationsInputListFileSystemAssociationsPaginateTypeDef",
    {
        "GatewayARN": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGatewaysInputListGatewaysPaginateTypeDef = TypedDict(
    "ListGatewaysInputListGatewaysPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTagsForResourceInputListTagsForResourcePaginateTypeDef = TypedDict(
    "ListTagsForResourceInputListTagsForResourcePaginateTypeDef",
    {
        "ResourceARN": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTapePoolsInputListTapePoolsPaginateTypeDef = TypedDict(
    "ListTapePoolsInputListTapePoolsPaginateTypeDef",
    {
        "PoolARNs": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTapesInputListTapesPaginateTypeDef = TypedDict(
    "ListTapesInputListTapesPaginateTypeDef",
    {
        "TapeARNs": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListVolumesInputListVolumesPaginateTypeDef = TypedDict(
    "ListVolumesInputListVolumesPaginateTypeDef",
    {
        "GatewayARN": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeTapeArchivesOutputTypeDef = TypedDict(
    "DescribeTapeArchivesOutputTypeDef",
    {
        "TapeArchives": List[TapeArchiveTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTapeRecoveryPointsOutputTypeDef = TypedDict(
    "DescribeTapeRecoveryPointsOutputTypeDef",
    {
        "GatewayARN": str,
        "TapeRecoveryPointInfos": List[TapeRecoveryPointInfoTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTapesOutputTypeDef = TypedDict(
    "DescribeTapesOutputTypeDef",
    {
        "Tapes": List[TapeTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VTLDeviceTypeDef = TypedDict(
    "VTLDeviceTypeDef",
    {
        "VTLDeviceARN": NotRequired[str],
        "VTLDeviceType": NotRequired[str],
        "VTLDeviceVendor": NotRequired[str],
        "VTLDeviceProductIdentifier": NotRequired[str],
        "DeviceiSCSIAttributes": NotRequired[DeviceiSCSIAttributesTypeDef],
    },
)
ListLocalDisksOutputTypeDef = TypedDict(
    "ListLocalDisksOutputTypeDef",
    {
        "GatewayARN": str,
        "Disks": List[DiskTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListFileSharesOutputTypeDef = TypedDict(
    "ListFileSharesOutputTypeDef",
    {
        "Marker": str,
        "NextMarker": str,
        "FileShareInfoList": List[FileShareInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FileSystemAssociationInfoTypeDef = TypedDict(
    "FileSystemAssociationInfoTypeDef",
    {
        "FileSystemAssociationARN": NotRequired[str],
        "LocationARN": NotRequired[str],
        "FileSystemAssociationStatus": NotRequired[str],
        "AuditDestinationARN": NotRequired[str],
        "GatewayARN": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "CacheAttributes": NotRequired[CacheAttributesTypeDef],
        "EndpointNetworkConfiguration": NotRequired[EndpointNetworkConfigurationOutputTypeDef],
        "FileSystemAssociationStatusDetails": NotRequired[
            List[FileSystemAssociationStatusDetailTypeDef]
        ],
    },
)
ListFileSystemAssociationsOutputTypeDef = TypedDict(
    "ListFileSystemAssociationsOutputTypeDef",
    {
        "Marker": str,
        "NextMarker": str,
        "FileSystemAssociationSummaryList": List[FileSystemAssociationSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListGatewaysOutputTypeDef = TypedDict(
    "ListGatewaysOutputTypeDef",
    {
        "Gateways": List[GatewayInfoTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTapePoolsOutputTypeDef = TypedDict(
    "ListTapePoolsOutputTypeDef",
    {
        "PoolInfos": List[PoolInfoTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTapesOutputTypeDef = TypedDict(
    "ListTapesOutputTypeDef",
    {
        "TapeInfos": List[TapeInfoTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListVolumeRecoveryPointsOutputTypeDef = TypedDict(
    "ListVolumeRecoveryPointsOutputTypeDef",
    {
        "GatewayARN": str,
        "VolumeRecoveryPointInfos": List[VolumeRecoveryPointInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListVolumesOutputTypeDef = TypedDict(
    "ListVolumesOutputTypeDef",
    {
        "GatewayARN": str,
        "Marker": str,
        "VolumeInfos": List[VolumeInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSMBLocalGroupsInputRequestTypeDef = TypedDict(
    "UpdateSMBLocalGroupsInputRequestTypeDef",
    {
        "GatewayARN": str,
        "SMBLocalGroups": SMBLocalGroupsTypeDef,
    },
)
DescribeSMBFileSharesOutputTypeDef = TypedDict(
    "DescribeSMBFileSharesOutputTypeDef",
    {
        "SMBFileShareInfoList": List[SMBFileShareInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAutomaticTapeCreationPoliciesOutputTypeDef = TypedDict(
    "ListAutomaticTapeCreationPoliciesOutputTypeDef",
    {
        "AutomaticTapeCreationPolicyInfos": List[AutomaticTapeCreationPolicyInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateBandwidthRateLimitScheduleInputRequestTypeDef = TypedDict(
    "UpdateBandwidthRateLimitScheduleInputRequestTypeDef",
    {
        "GatewayARN": str,
        "BandwidthRateLimitIntervals": Sequence[BandwidthRateLimitIntervalUnionTypeDef],
    },
)
DescribeCachediSCSIVolumesOutputTypeDef = TypedDict(
    "DescribeCachediSCSIVolumesOutputTypeDef",
    {
        "CachediSCSIVolumes": List[CachediSCSIVolumeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeStorediSCSIVolumesOutputTypeDef = TypedDict(
    "DescribeStorediSCSIVolumesOutputTypeDef",
    {
        "StorediSCSIVolumes": List[StorediSCSIVolumeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeNFSFileSharesOutputTypeDef = TypedDict(
    "DescribeNFSFileSharesOutputTypeDef",
    {
        "NFSFileShareInfoList": List[NFSFileShareInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeVTLDevicesOutputTypeDef = TypedDict(
    "DescribeVTLDevicesOutputTypeDef",
    {
        "GatewayARN": str,
        "VTLDevices": List[VTLDeviceTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeFileSystemAssociationsOutputTypeDef = TypedDict(
    "DescribeFileSystemAssociationsOutputTypeDef",
    {
        "FileSystemAssociationInfoList": List[FileSystemAssociationInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
