"""
Type annotations for iot1click-devices service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot1click_devices/type_defs/)

Usage::

    ```python
    from mypy_boto3_iot1click_devices.type_defs import ClaimDevicesByClaimCodeRequestRequestTypeDef

    data: ClaimDevicesByClaimCodeRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "ClaimDevicesByClaimCodeRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "DescribeDeviceRequestRequestTypeDef",
    "DeviceDescriptionTypeDef",
    "DeviceTypeDef",
    "DeviceMethodTypeDef",
    "FinalizeDeviceClaimRequestRequestTypeDef",
    "GetDeviceMethodsRequestRequestTypeDef",
    "InitiateDeviceClaimRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "TimestampTypeDef",
    "ListDevicesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UnclaimDeviceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDeviceStateRequestRequestTypeDef",
    "ClaimDevicesByClaimCodeResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "FinalizeDeviceClaimResponseTypeDef",
    "InitiateDeviceClaimResponseTypeDef",
    "InvokeDeviceMethodResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "UnclaimDeviceResponseTypeDef",
    "DescribeDeviceResponseTypeDef",
    "ListDevicesResponseTypeDef",
    "DeviceEventTypeDef",
    "GetDeviceMethodsResponseTypeDef",
    "InvokeDeviceMethodRequestRequestTypeDef",
    "ListDevicesRequestListDevicesPaginateTypeDef",
    "ListDeviceEventsRequestListDeviceEventsPaginateTypeDef",
    "ListDeviceEventsRequestRequestTypeDef",
    "ListDeviceEventsResponseTypeDef",
)

ClaimDevicesByClaimCodeRequestRequestTypeDef = TypedDict(
    "ClaimDevicesByClaimCodeRequestRequestTypeDef",
    {
        "ClaimCode": str,
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
DescribeDeviceRequestRequestTypeDef = TypedDict(
    "DescribeDeviceRequestRequestTypeDef",
    {
        "DeviceId": str,
    },
)
DeviceDescriptionTypeDef = TypedDict(
    "DeviceDescriptionTypeDef",
    {
        "Arn": NotRequired[str],
        "Attributes": NotRequired[Dict[str, str]],
        "DeviceId": NotRequired[str],
        "Enabled": NotRequired[bool],
        "RemainingLife": NotRequired[float],
        "Type": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)
DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "Attributes": NotRequired[Dict[str, Any]],
        "DeviceId": NotRequired[str],
        "Type": NotRequired[str],
    },
)
DeviceMethodTypeDef = TypedDict(
    "DeviceMethodTypeDef",
    {
        "DeviceType": NotRequired[str],
        "MethodName": NotRequired[str],
    },
)
FinalizeDeviceClaimRequestRequestTypeDef = TypedDict(
    "FinalizeDeviceClaimRequestRequestTypeDef",
    {
        "DeviceId": str,
        "Tags": NotRequired[Mapping[str, str]],
    },
)
GetDeviceMethodsRequestRequestTypeDef = TypedDict(
    "GetDeviceMethodsRequestRequestTypeDef",
    {
        "DeviceId": str,
    },
)
InitiateDeviceClaimRequestRequestTypeDef = TypedDict(
    "InitiateDeviceClaimRequestRequestTypeDef",
    {
        "DeviceId": str,
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
TimestampTypeDef = Union[datetime, str]
ListDevicesRequestRequestTypeDef = TypedDict(
    "ListDevicesRequestRequestTypeDef",
    {
        "DeviceType": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)
UnclaimDeviceRequestRequestTypeDef = TypedDict(
    "UnclaimDeviceRequestRequestTypeDef",
    {
        "DeviceId": str,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateDeviceStateRequestRequestTypeDef = TypedDict(
    "UpdateDeviceStateRequestRequestTypeDef",
    {
        "DeviceId": str,
        "Enabled": NotRequired[bool],
    },
)
ClaimDevicesByClaimCodeResponseTypeDef = TypedDict(
    "ClaimDevicesByClaimCodeResponseTypeDef",
    {
        "ClaimCode": str,
        "Total": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FinalizeDeviceClaimResponseTypeDef = TypedDict(
    "FinalizeDeviceClaimResponseTypeDef",
    {
        "State": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InitiateDeviceClaimResponseTypeDef = TypedDict(
    "InitiateDeviceClaimResponseTypeDef",
    {
        "State": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InvokeDeviceMethodResponseTypeDef = TypedDict(
    "InvokeDeviceMethodResponseTypeDef",
    {
        "DeviceMethodResponse": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UnclaimDeviceResponseTypeDef = TypedDict(
    "UnclaimDeviceResponseTypeDef",
    {
        "State": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDeviceResponseTypeDef = TypedDict(
    "DescribeDeviceResponseTypeDef",
    {
        "DeviceDescription": DeviceDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDevicesResponseTypeDef = TypedDict(
    "ListDevicesResponseTypeDef",
    {
        "Devices": List[DeviceDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DeviceEventTypeDef = TypedDict(
    "DeviceEventTypeDef",
    {
        "Device": NotRequired[DeviceTypeDef],
        "StdEvent": NotRequired[str],
    },
)
GetDeviceMethodsResponseTypeDef = TypedDict(
    "GetDeviceMethodsResponseTypeDef",
    {
        "DeviceMethods": List[DeviceMethodTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InvokeDeviceMethodRequestRequestTypeDef = TypedDict(
    "InvokeDeviceMethodRequestRequestTypeDef",
    {
        "DeviceId": str,
        "DeviceMethod": NotRequired[DeviceMethodTypeDef],
        "DeviceMethodParameters": NotRequired[str],
    },
)
ListDevicesRequestListDevicesPaginateTypeDef = TypedDict(
    "ListDevicesRequestListDevicesPaginateTypeDef",
    {
        "DeviceType": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDeviceEventsRequestListDeviceEventsPaginateTypeDef = TypedDict(
    "ListDeviceEventsRequestListDeviceEventsPaginateTypeDef",
    {
        "DeviceId": str,
        "FromTimeStamp": TimestampTypeDef,
        "ToTimeStamp": TimestampTypeDef,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDeviceEventsRequestRequestTypeDef = TypedDict(
    "ListDeviceEventsRequestRequestTypeDef",
    {
        "DeviceId": str,
        "FromTimeStamp": TimestampTypeDef,
        "ToTimeStamp": TimestampTypeDef,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListDeviceEventsResponseTypeDef = TypedDict(
    "ListDeviceEventsResponseTypeDef",
    {
        "Events": List[DeviceEventTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
