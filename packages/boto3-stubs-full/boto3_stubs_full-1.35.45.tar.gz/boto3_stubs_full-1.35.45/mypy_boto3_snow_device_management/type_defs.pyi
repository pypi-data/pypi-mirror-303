"""
Type annotations for snow-device-management service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_snow_device_management/type_defs/)

Usage::

    ```python
    from mypy_boto3_snow_device_management.type_defs import CancelTaskInputRequestTypeDef

    data: CancelTaskInputRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence

from .literals import (
    AttachmentStatusType,
    ExecutionStateType,
    InstanceStateNameType,
    IpAddressAssignmentType,
    PhysicalConnectorTypeType,
    TaskStateType,
    UnlockStateType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "CancelTaskInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CapacityTypeDef",
    "CommandTypeDef",
    "CpuOptionsTypeDef",
    "DescribeDeviceEc2InputRequestTypeDef",
    "DescribeDeviceInputRequestTypeDef",
    "PhysicalNetworkInterfaceTypeDef",
    "SoftwareInformationTypeDef",
    "DescribeExecutionInputRequestTypeDef",
    "DescribeTaskInputRequestTypeDef",
    "DeviceSummaryTypeDef",
    "EbsInstanceBlockDeviceTypeDef",
    "ExecutionSummaryTypeDef",
    "InstanceStateTypeDef",
    "SecurityGroupIdentifierTypeDef",
    "PaginatorConfigTypeDef",
    "ListDeviceResourcesInputRequestTypeDef",
    "ResourceSummaryTypeDef",
    "ListDevicesInputRequestTypeDef",
    "ListExecutionsInputRequestTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTasksInputRequestTypeDef",
    "TaskSummaryTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "CancelTaskOutputTypeDef",
    "CreateTaskOutputTypeDef",
    "DescribeExecutionOutputTypeDef",
    "DescribeTaskOutputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "CreateTaskInputRequestTypeDef",
    "DescribeDeviceOutputTypeDef",
    "ListDevicesOutputTypeDef",
    "InstanceBlockDeviceMappingTypeDef",
    "ListExecutionsOutputTypeDef",
    "ListDeviceResourcesInputListDeviceResourcesPaginateTypeDef",
    "ListDevicesInputListDevicesPaginateTypeDef",
    "ListExecutionsInputListExecutionsPaginateTypeDef",
    "ListTasksInputListTasksPaginateTypeDef",
    "ListDeviceResourcesOutputTypeDef",
    "ListTasksOutputTypeDef",
    "InstanceTypeDef",
    "InstanceSummaryTypeDef",
    "DescribeDeviceEc2OutputTypeDef",
)

CancelTaskInputRequestTypeDef = TypedDict(
    "CancelTaskInputRequestTypeDef",
    {
        "taskId": str,
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
CapacityTypeDef = TypedDict(
    "CapacityTypeDef",
    {
        "available": NotRequired[int],
        "name": NotRequired[str],
        "total": NotRequired[int],
        "unit": NotRequired[str],
        "used": NotRequired[int],
    },
)
CommandTypeDef = TypedDict(
    "CommandTypeDef",
    {
        "reboot": NotRequired[Mapping[str, Any]],
        "unlock": NotRequired[Mapping[str, Any]],
    },
)
CpuOptionsTypeDef = TypedDict(
    "CpuOptionsTypeDef",
    {
        "coreCount": NotRequired[int],
        "threadsPerCore": NotRequired[int],
    },
)
DescribeDeviceEc2InputRequestTypeDef = TypedDict(
    "DescribeDeviceEc2InputRequestTypeDef",
    {
        "instanceIds": Sequence[str],
        "managedDeviceId": str,
    },
)
DescribeDeviceInputRequestTypeDef = TypedDict(
    "DescribeDeviceInputRequestTypeDef",
    {
        "managedDeviceId": str,
    },
)
PhysicalNetworkInterfaceTypeDef = TypedDict(
    "PhysicalNetworkInterfaceTypeDef",
    {
        "defaultGateway": NotRequired[str],
        "ipAddress": NotRequired[str],
        "ipAddressAssignment": NotRequired[IpAddressAssignmentType],
        "macAddress": NotRequired[str],
        "netmask": NotRequired[str],
        "physicalConnectorType": NotRequired[PhysicalConnectorTypeType],
        "physicalNetworkInterfaceId": NotRequired[str],
    },
)
SoftwareInformationTypeDef = TypedDict(
    "SoftwareInformationTypeDef",
    {
        "installState": NotRequired[str],
        "installedVersion": NotRequired[str],
        "installingVersion": NotRequired[str],
    },
)
DescribeExecutionInputRequestTypeDef = TypedDict(
    "DescribeExecutionInputRequestTypeDef",
    {
        "managedDeviceId": str,
        "taskId": str,
    },
)
DescribeTaskInputRequestTypeDef = TypedDict(
    "DescribeTaskInputRequestTypeDef",
    {
        "taskId": str,
    },
)
DeviceSummaryTypeDef = TypedDict(
    "DeviceSummaryTypeDef",
    {
        "associatedWithJob": NotRequired[str],
        "managedDeviceArn": NotRequired[str],
        "managedDeviceId": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)
EbsInstanceBlockDeviceTypeDef = TypedDict(
    "EbsInstanceBlockDeviceTypeDef",
    {
        "attachTime": NotRequired[datetime],
        "deleteOnTermination": NotRequired[bool],
        "status": NotRequired[AttachmentStatusType],
        "volumeId": NotRequired[str],
    },
)
ExecutionSummaryTypeDef = TypedDict(
    "ExecutionSummaryTypeDef",
    {
        "executionId": NotRequired[str],
        "managedDeviceId": NotRequired[str],
        "state": NotRequired[ExecutionStateType],
        "taskId": NotRequired[str],
    },
)
InstanceStateTypeDef = TypedDict(
    "InstanceStateTypeDef",
    {
        "code": NotRequired[int],
        "name": NotRequired[InstanceStateNameType],
    },
)
SecurityGroupIdentifierTypeDef = TypedDict(
    "SecurityGroupIdentifierTypeDef",
    {
        "groupId": NotRequired[str],
        "groupName": NotRequired[str],
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
ListDeviceResourcesInputRequestTypeDef = TypedDict(
    "ListDeviceResourcesInputRequestTypeDef",
    {
        "managedDeviceId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "type": NotRequired[str],
    },
)
ResourceSummaryTypeDef = TypedDict(
    "ResourceSummaryTypeDef",
    {
        "resourceType": str,
        "arn": NotRequired[str],
        "id": NotRequired[str],
    },
)
ListDevicesInputRequestTypeDef = TypedDict(
    "ListDevicesInputRequestTypeDef",
    {
        "jobId": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListExecutionsInputRequestTypeDef = TypedDict(
    "ListExecutionsInputRequestTypeDef",
    {
        "taskId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "state": NotRequired[ExecutionStateType],
    },
)
ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)
ListTasksInputRequestTypeDef = TypedDict(
    "ListTasksInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "state": NotRequired[TaskStateType],
    },
)
TaskSummaryTypeDef = TypedDict(
    "TaskSummaryTypeDef",
    {
        "taskId": str,
        "state": NotRequired[TaskStateType],
        "tags": NotRequired[Dict[str, str]],
        "taskArn": NotRequired[str],
    },
)
TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
CancelTaskOutputTypeDef = TypedDict(
    "CancelTaskOutputTypeDef",
    {
        "taskId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTaskOutputTypeDef = TypedDict(
    "CreateTaskOutputTypeDef",
    {
        "taskArn": str,
        "taskId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeExecutionOutputTypeDef = TypedDict(
    "DescribeExecutionOutputTypeDef",
    {
        "executionId": str,
        "lastUpdatedAt": datetime,
        "managedDeviceId": str,
        "startedAt": datetime,
        "state": ExecutionStateType,
        "taskId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTaskOutputTypeDef = TypedDict(
    "DescribeTaskOutputTypeDef",
    {
        "completedAt": datetime,
        "createdAt": datetime,
        "description": str,
        "lastUpdatedAt": datetime,
        "state": TaskStateType,
        "tags": Dict[str, str],
        "targets": List[str],
        "taskArn": str,
        "taskId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTaskInputRequestTypeDef = TypedDict(
    "CreateTaskInputRequestTypeDef",
    {
        "command": CommandTypeDef,
        "targets": Sequence[str],
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
DescribeDeviceOutputTypeDef = TypedDict(
    "DescribeDeviceOutputTypeDef",
    {
        "associatedWithJob": str,
        "deviceCapacities": List[CapacityTypeDef],
        "deviceState": UnlockStateType,
        "deviceType": str,
        "lastReachedOutAt": datetime,
        "lastUpdatedAt": datetime,
        "managedDeviceArn": str,
        "managedDeviceId": str,
        "physicalNetworkInterfaces": List[PhysicalNetworkInterfaceTypeDef],
        "software": SoftwareInformationTypeDef,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDevicesOutputTypeDef = TypedDict(
    "ListDevicesOutputTypeDef",
    {
        "devices": List[DeviceSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InstanceBlockDeviceMappingTypeDef = TypedDict(
    "InstanceBlockDeviceMappingTypeDef",
    {
        "deviceName": NotRequired[str],
        "ebs": NotRequired[EbsInstanceBlockDeviceTypeDef],
    },
)
ListExecutionsOutputTypeDef = TypedDict(
    "ListExecutionsOutputTypeDef",
    {
        "executions": List[ExecutionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDeviceResourcesInputListDeviceResourcesPaginateTypeDef = TypedDict(
    "ListDeviceResourcesInputListDeviceResourcesPaginateTypeDef",
    {
        "managedDeviceId": str,
        "type": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDevicesInputListDevicesPaginateTypeDef = TypedDict(
    "ListDevicesInputListDevicesPaginateTypeDef",
    {
        "jobId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListExecutionsInputListExecutionsPaginateTypeDef = TypedDict(
    "ListExecutionsInputListExecutionsPaginateTypeDef",
    {
        "taskId": str,
        "state": NotRequired[ExecutionStateType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTasksInputListTasksPaginateTypeDef = TypedDict(
    "ListTasksInputListTasksPaginateTypeDef",
    {
        "state": NotRequired[TaskStateType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDeviceResourcesOutputTypeDef = TypedDict(
    "ListDeviceResourcesOutputTypeDef",
    {
        "nextToken": str,
        "resources": List[ResourceSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTasksOutputTypeDef = TypedDict(
    "ListTasksOutputTypeDef",
    {
        "nextToken": str,
        "tasks": List[TaskSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "amiLaunchIndex": NotRequired[int],
        "blockDeviceMappings": NotRequired[List[InstanceBlockDeviceMappingTypeDef]],
        "cpuOptions": NotRequired[CpuOptionsTypeDef],
        "createdAt": NotRequired[datetime],
        "imageId": NotRequired[str],
        "instanceId": NotRequired[str],
        "instanceType": NotRequired[str],
        "privateIpAddress": NotRequired[str],
        "publicIpAddress": NotRequired[str],
        "rootDeviceName": NotRequired[str],
        "securityGroups": NotRequired[List[SecurityGroupIdentifierTypeDef]],
        "state": NotRequired[InstanceStateTypeDef],
        "updatedAt": NotRequired[datetime],
    },
)
InstanceSummaryTypeDef = TypedDict(
    "InstanceSummaryTypeDef",
    {
        "instance": NotRequired[InstanceTypeDef],
        "lastUpdatedAt": NotRequired[datetime],
    },
)
DescribeDeviceEc2OutputTypeDef = TypedDict(
    "DescribeDeviceEc2OutputTypeDef",
    {
        "instances": List[InstanceSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
