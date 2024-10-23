"""
Type annotations for backup-gateway service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup_gateway/type_defs/)

Usage::

    ```python
    from mypy_boto3_backup_gateway.type_defs import AssociateGatewayToServerInputRequestTypeDef

    data: AssociateGatewayToServerInputRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import HypervisorStateType, SyncMetadataStatusType

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AssociateGatewayToServerInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "BandwidthRateLimitIntervalOutputTypeDef",
    "BandwidthRateLimitIntervalTypeDef",
    "TagTypeDef",
    "DeleteGatewayInputRequestTypeDef",
    "DeleteHypervisorInputRequestTypeDef",
    "DisassociateGatewayFromServerInputRequestTypeDef",
    "MaintenanceStartTimeTypeDef",
    "GatewayTypeDef",
    "GetBandwidthRateLimitScheduleInputRequestTypeDef",
    "GetGatewayInputRequestTypeDef",
    "GetHypervisorInputRequestTypeDef",
    "HypervisorDetailsTypeDef",
    "GetHypervisorPropertyMappingsInputRequestTypeDef",
    "VmwareToAwsTagMappingTypeDef",
    "GetVirtualMachineInputRequestTypeDef",
    "HypervisorTypeDef",
    "PaginatorConfigTypeDef",
    "ListGatewaysInputRequestTypeDef",
    "ListHypervisorsInputRequestTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListVirtualMachinesInputRequestTypeDef",
    "VirtualMachineTypeDef",
    "PutMaintenanceStartTimeInputRequestTypeDef",
    "StartVirtualMachinesMetadataSyncInputRequestTypeDef",
    "TestHypervisorConfigurationInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateGatewayInformationInputRequestTypeDef",
    "UpdateGatewaySoftwareNowInputRequestTypeDef",
    "UpdateHypervisorInputRequestTypeDef",
    "VmwareTagTypeDef",
    "AssociateGatewayToServerOutputTypeDef",
    "CreateGatewayOutputTypeDef",
    "DeleteGatewayOutputTypeDef",
    "DeleteHypervisorOutputTypeDef",
    "DisassociateGatewayFromServerOutputTypeDef",
    "ImportHypervisorConfigurationOutputTypeDef",
    "PutBandwidthRateLimitScheduleOutputTypeDef",
    "PutHypervisorPropertyMappingsOutputTypeDef",
    "PutMaintenanceStartTimeOutputTypeDef",
    "StartVirtualMachinesMetadataSyncOutputTypeDef",
    "TagResourceOutputTypeDef",
    "UntagResourceOutputTypeDef",
    "UpdateGatewayInformationOutputTypeDef",
    "UpdateGatewaySoftwareNowOutputTypeDef",
    "UpdateHypervisorOutputTypeDef",
    "GetBandwidthRateLimitScheduleOutputTypeDef",
    "BandwidthRateLimitIntervalUnionTypeDef",
    "CreateGatewayInputRequestTypeDef",
    "ImportHypervisorConfigurationInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "TagResourceInputRequestTypeDef",
    "GatewayDetailsTypeDef",
    "ListGatewaysOutputTypeDef",
    "GetHypervisorOutputTypeDef",
    "GetHypervisorPropertyMappingsOutputTypeDef",
    "PutHypervisorPropertyMappingsInputRequestTypeDef",
    "ListHypervisorsOutputTypeDef",
    "ListGatewaysInputListGatewaysPaginateTypeDef",
    "ListHypervisorsInputListHypervisorsPaginateTypeDef",
    "ListVirtualMachinesInputListVirtualMachinesPaginateTypeDef",
    "ListVirtualMachinesOutputTypeDef",
    "VirtualMachineDetailsTypeDef",
    "PutBandwidthRateLimitScheduleInputRequestTypeDef",
    "GetGatewayOutputTypeDef",
    "GetVirtualMachineOutputTypeDef",
)

AssociateGatewayToServerInputRequestTypeDef = TypedDict(
    "AssociateGatewayToServerInputRequestTypeDef",
    {
        "GatewayArn": str,
        "ServerArn": str,
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
BandwidthRateLimitIntervalOutputTypeDef = TypedDict(
    "BandwidthRateLimitIntervalOutputTypeDef",
    {
        "DaysOfWeek": List[int],
        "EndHourOfDay": int,
        "EndMinuteOfHour": int,
        "StartHourOfDay": int,
        "StartMinuteOfHour": int,
        "AverageUploadRateLimitInBitsPerSec": NotRequired[int],
    },
)
BandwidthRateLimitIntervalTypeDef = TypedDict(
    "BandwidthRateLimitIntervalTypeDef",
    {
        "DaysOfWeek": Sequence[int],
        "EndHourOfDay": int,
        "EndMinuteOfHour": int,
        "StartHourOfDay": int,
        "StartMinuteOfHour": int,
        "AverageUploadRateLimitInBitsPerSec": NotRequired[int],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
DeleteGatewayInputRequestTypeDef = TypedDict(
    "DeleteGatewayInputRequestTypeDef",
    {
        "GatewayArn": str,
    },
)
DeleteHypervisorInputRequestTypeDef = TypedDict(
    "DeleteHypervisorInputRequestTypeDef",
    {
        "HypervisorArn": str,
    },
)
DisassociateGatewayFromServerInputRequestTypeDef = TypedDict(
    "DisassociateGatewayFromServerInputRequestTypeDef",
    {
        "GatewayArn": str,
    },
)
MaintenanceStartTimeTypeDef = TypedDict(
    "MaintenanceStartTimeTypeDef",
    {
        "HourOfDay": int,
        "MinuteOfHour": int,
        "DayOfMonth": NotRequired[int],
        "DayOfWeek": NotRequired[int],
    },
)
GatewayTypeDef = TypedDict(
    "GatewayTypeDef",
    {
        "GatewayArn": NotRequired[str],
        "GatewayDisplayName": NotRequired[str],
        "GatewayType": NotRequired[Literal["BACKUP_VM"]],
        "HypervisorId": NotRequired[str],
        "LastSeenTime": NotRequired[datetime],
    },
)
GetBandwidthRateLimitScheduleInputRequestTypeDef = TypedDict(
    "GetBandwidthRateLimitScheduleInputRequestTypeDef",
    {
        "GatewayArn": str,
    },
)
GetGatewayInputRequestTypeDef = TypedDict(
    "GetGatewayInputRequestTypeDef",
    {
        "GatewayArn": str,
    },
)
GetHypervisorInputRequestTypeDef = TypedDict(
    "GetHypervisorInputRequestTypeDef",
    {
        "HypervisorArn": str,
    },
)
HypervisorDetailsTypeDef = TypedDict(
    "HypervisorDetailsTypeDef",
    {
        "Host": NotRequired[str],
        "HypervisorArn": NotRequired[str],
        "KmsKeyArn": NotRequired[str],
        "LastSuccessfulMetadataSyncTime": NotRequired[datetime],
        "LatestMetadataSyncStatus": NotRequired[SyncMetadataStatusType],
        "LatestMetadataSyncStatusMessage": NotRequired[str],
        "LogGroupArn": NotRequired[str],
        "Name": NotRequired[str],
        "State": NotRequired[HypervisorStateType],
    },
)
GetHypervisorPropertyMappingsInputRequestTypeDef = TypedDict(
    "GetHypervisorPropertyMappingsInputRequestTypeDef",
    {
        "HypervisorArn": str,
    },
)
VmwareToAwsTagMappingTypeDef = TypedDict(
    "VmwareToAwsTagMappingTypeDef",
    {
        "AwsTagKey": str,
        "AwsTagValue": str,
        "VmwareCategory": str,
        "VmwareTagName": str,
    },
)
GetVirtualMachineInputRequestTypeDef = TypedDict(
    "GetVirtualMachineInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
HypervisorTypeDef = TypedDict(
    "HypervisorTypeDef",
    {
        "Host": NotRequired[str],
        "HypervisorArn": NotRequired[str],
        "KmsKeyArn": NotRequired[str],
        "Name": NotRequired[str],
        "State": NotRequired[HypervisorStateType],
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
ListGatewaysInputRequestTypeDef = TypedDict(
    "ListGatewaysInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListHypervisorsInputRequestTypeDef = TypedDict(
    "ListHypervisorsInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
ListVirtualMachinesInputRequestTypeDef = TypedDict(
    "ListVirtualMachinesInputRequestTypeDef",
    {
        "HypervisorArn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
VirtualMachineTypeDef = TypedDict(
    "VirtualMachineTypeDef",
    {
        "HostName": NotRequired[str],
        "HypervisorId": NotRequired[str],
        "LastBackupDate": NotRequired[datetime],
        "Name": NotRequired[str],
        "Path": NotRequired[str],
        "ResourceArn": NotRequired[str],
    },
)
PutMaintenanceStartTimeInputRequestTypeDef = TypedDict(
    "PutMaintenanceStartTimeInputRequestTypeDef",
    {
        "GatewayArn": str,
        "HourOfDay": int,
        "MinuteOfHour": int,
        "DayOfMonth": NotRequired[int],
        "DayOfWeek": NotRequired[int],
    },
)
StartVirtualMachinesMetadataSyncInputRequestTypeDef = TypedDict(
    "StartVirtualMachinesMetadataSyncInputRequestTypeDef",
    {
        "HypervisorArn": str,
    },
)
TestHypervisorConfigurationInputRequestTypeDef = TypedDict(
    "TestHypervisorConfigurationInputRequestTypeDef",
    {
        "GatewayArn": str,
        "Host": str,
        "Password": NotRequired[str],
        "Username": NotRequired[str],
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
UpdateGatewayInformationInputRequestTypeDef = TypedDict(
    "UpdateGatewayInformationInputRequestTypeDef",
    {
        "GatewayArn": str,
        "GatewayDisplayName": NotRequired[str],
    },
)
UpdateGatewaySoftwareNowInputRequestTypeDef = TypedDict(
    "UpdateGatewaySoftwareNowInputRequestTypeDef",
    {
        "GatewayArn": str,
    },
)
UpdateHypervisorInputRequestTypeDef = TypedDict(
    "UpdateHypervisorInputRequestTypeDef",
    {
        "HypervisorArn": str,
        "Host": NotRequired[str],
        "LogGroupArn": NotRequired[str],
        "Name": NotRequired[str],
        "Password": NotRequired[str],
        "Username": NotRequired[str],
    },
)
VmwareTagTypeDef = TypedDict(
    "VmwareTagTypeDef",
    {
        "VmwareCategory": NotRequired[str],
        "VmwareTagDescription": NotRequired[str],
        "VmwareTagName": NotRequired[str],
    },
)
AssociateGatewayToServerOutputTypeDef = TypedDict(
    "AssociateGatewayToServerOutputTypeDef",
    {
        "GatewayArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGatewayOutputTypeDef = TypedDict(
    "CreateGatewayOutputTypeDef",
    {
        "GatewayArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteGatewayOutputTypeDef = TypedDict(
    "DeleteGatewayOutputTypeDef",
    {
        "GatewayArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteHypervisorOutputTypeDef = TypedDict(
    "DeleteHypervisorOutputTypeDef",
    {
        "HypervisorArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateGatewayFromServerOutputTypeDef = TypedDict(
    "DisassociateGatewayFromServerOutputTypeDef",
    {
        "GatewayArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportHypervisorConfigurationOutputTypeDef = TypedDict(
    "ImportHypervisorConfigurationOutputTypeDef",
    {
        "HypervisorArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutBandwidthRateLimitScheduleOutputTypeDef = TypedDict(
    "PutBandwidthRateLimitScheduleOutputTypeDef",
    {
        "GatewayArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutHypervisorPropertyMappingsOutputTypeDef = TypedDict(
    "PutHypervisorPropertyMappingsOutputTypeDef",
    {
        "HypervisorArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutMaintenanceStartTimeOutputTypeDef = TypedDict(
    "PutMaintenanceStartTimeOutputTypeDef",
    {
        "GatewayArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartVirtualMachinesMetadataSyncOutputTypeDef = TypedDict(
    "StartVirtualMachinesMetadataSyncOutputTypeDef",
    {
        "HypervisorArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceOutputTypeDef = TypedDict(
    "TagResourceOutputTypeDef",
    {
        "ResourceARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UntagResourceOutputTypeDef = TypedDict(
    "UntagResourceOutputTypeDef",
    {
        "ResourceARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateGatewayInformationOutputTypeDef = TypedDict(
    "UpdateGatewayInformationOutputTypeDef",
    {
        "GatewayArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateGatewaySoftwareNowOutputTypeDef = TypedDict(
    "UpdateGatewaySoftwareNowOutputTypeDef",
    {
        "GatewayArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateHypervisorOutputTypeDef = TypedDict(
    "UpdateHypervisorOutputTypeDef",
    {
        "HypervisorArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBandwidthRateLimitScheduleOutputTypeDef = TypedDict(
    "GetBandwidthRateLimitScheduleOutputTypeDef",
    {
        "BandwidthRateLimitIntervals": List[BandwidthRateLimitIntervalOutputTypeDef],
        "GatewayArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BandwidthRateLimitIntervalUnionTypeDef = Union[
    BandwidthRateLimitIntervalTypeDef, BandwidthRateLimitIntervalOutputTypeDef
]
CreateGatewayInputRequestTypeDef = TypedDict(
    "CreateGatewayInputRequestTypeDef",
    {
        "ActivationKey": str,
        "GatewayDisplayName": str,
        "GatewayType": Literal["BACKUP_VM"],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ImportHypervisorConfigurationInputRequestTypeDef = TypedDict(
    "ImportHypervisorConfigurationInputRequestTypeDef",
    {
        "Host": str,
        "Name": str,
        "KmsKeyArn": NotRequired[str],
        "Password": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "Username": NotRequired[str],
    },
)
ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "ResourceArn": str,
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)
GatewayDetailsTypeDef = TypedDict(
    "GatewayDetailsTypeDef",
    {
        "GatewayArn": NotRequired[str],
        "GatewayDisplayName": NotRequired[str],
        "GatewayType": NotRequired[Literal["BACKUP_VM"]],
        "HypervisorId": NotRequired[str],
        "LastSeenTime": NotRequired[datetime],
        "MaintenanceStartTime": NotRequired[MaintenanceStartTimeTypeDef],
        "NextUpdateAvailabilityTime": NotRequired[datetime],
        "VpcEndpoint": NotRequired[str],
    },
)
ListGatewaysOutputTypeDef = TypedDict(
    "ListGatewaysOutputTypeDef",
    {
        "Gateways": List[GatewayTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetHypervisorOutputTypeDef = TypedDict(
    "GetHypervisorOutputTypeDef",
    {
        "Hypervisor": HypervisorDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetHypervisorPropertyMappingsOutputTypeDef = TypedDict(
    "GetHypervisorPropertyMappingsOutputTypeDef",
    {
        "HypervisorArn": str,
        "IamRoleArn": str,
        "VmwareToAwsTagMappings": List[VmwareToAwsTagMappingTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutHypervisorPropertyMappingsInputRequestTypeDef = TypedDict(
    "PutHypervisorPropertyMappingsInputRequestTypeDef",
    {
        "HypervisorArn": str,
        "IamRoleArn": str,
        "VmwareToAwsTagMappings": Sequence[VmwareToAwsTagMappingTypeDef],
    },
)
ListHypervisorsOutputTypeDef = TypedDict(
    "ListHypervisorsOutputTypeDef",
    {
        "Hypervisors": List[HypervisorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListGatewaysInputListGatewaysPaginateTypeDef = TypedDict(
    "ListGatewaysInputListGatewaysPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListHypervisorsInputListHypervisorsPaginateTypeDef = TypedDict(
    "ListHypervisorsInputListHypervisorsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListVirtualMachinesInputListVirtualMachinesPaginateTypeDef = TypedDict(
    "ListVirtualMachinesInputListVirtualMachinesPaginateTypeDef",
    {
        "HypervisorArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListVirtualMachinesOutputTypeDef = TypedDict(
    "ListVirtualMachinesOutputTypeDef",
    {
        "VirtualMachines": List[VirtualMachineTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
VirtualMachineDetailsTypeDef = TypedDict(
    "VirtualMachineDetailsTypeDef",
    {
        "HostName": NotRequired[str],
        "HypervisorId": NotRequired[str],
        "LastBackupDate": NotRequired[datetime],
        "Name": NotRequired[str],
        "Path": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "VmwareTags": NotRequired[List[VmwareTagTypeDef]],
    },
)
PutBandwidthRateLimitScheduleInputRequestTypeDef = TypedDict(
    "PutBandwidthRateLimitScheduleInputRequestTypeDef",
    {
        "BandwidthRateLimitIntervals": Sequence[BandwidthRateLimitIntervalUnionTypeDef],
        "GatewayArn": str,
    },
)
GetGatewayOutputTypeDef = TypedDict(
    "GetGatewayOutputTypeDef",
    {
        "Gateway": GatewayDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetVirtualMachineOutputTypeDef = TypedDict(
    "GetVirtualMachineOutputTypeDef",
    {
        "VirtualMachine": VirtualMachineDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
