"""
Type annotations for outposts service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/type_defs/)

Usage::

    ```python
    from mypy_boto3_outposts.type_defs import AddressTypeDef

    data: AddressTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AddressTypeType,
    AssetStateType,
    CapacityTaskStatusType,
    CatalogItemClassType,
    CatalogItemStatusType,
    ComputeAssetStateType,
    FiberOpticCableTypeType,
    LineItemStatusType,
    MaximumSupportedWeightLbsType,
    OpticalStandardType,
    OrderStatusType,
    OrderTypeType,
    PaymentOptionType,
    PaymentTermType,
    PowerConnectorType,
    PowerDrawKvaType,
    PowerFeedDropType,
    PowerPhaseType,
    ShipmentCarrierType,
    SupportedHardwareTypeType,
    SupportedStorageEnumType,
    UplinkCountType,
    UplinkGbpsType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AddressTypeDef",
    "AssetLocationTypeDef",
    "ComputeAttributesTypeDef",
    "CancelCapacityTaskInputRequestTypeDef",
    "CancelOrderInputRequestTypeDef",
    "CapacityTaskFailureTypeDef",
    "CapacityTaskSummaryTypeDef",
    "EC2CapacityTypeDef",
    "ConnectionDetailsTypeDef",
    "LineItemRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CreateOutpostInputRequestTypeDef",
    "OutpostTypeDef",
    "RackPhysicalPropertiesTypeDef",
    "DeleteOutpostInputRequestTypeDef",
    "DeleteSiteInputRequestTypeDef",
    "GetCapacityTaskInputRequestTypeDef",
    "InstanceTypeCapacityTypeDef",
    "GetCatalogItemInputRequestTypeDef",
    "GetConnectionRequestRequestTypeDef",
    "GetOrderInputRequestTypeDef",
    "GetOutpostInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "GetOutpostInstanceTypesInputRequestTypeDef",
    "InstanceTypeItemTypeDef",
    "GetOutpostSupportedInstanceTypesInputRequestTypeDef",
    "GetSiteAddressInputRequestTypeDef",
    "GetSiteInputRequestTypeDef",
    "LineItemAssetInformationTypeDef",
    "ShipmentInformationTypeDef",
    "ListAssetsInputRequestTypeDef",
    "ListCapacityTasksInputRequestTypeDef",
    "ListCatalogItemsInputRequestTypeDef",
    "ListOrdersInputRequestTypeDef",
    "OrderSummaryTypeDef",
    "ListOutpostsInputRequestTypeDef",
    "ListSitesInputRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "StartConnectionRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateOutpostInputRequestTypeDef",
    "UpdateSiteInputRequestTypeDef",
    "UpdateSiteRackPhysicalPropertiesInputRequestTypeDef",
    "UpdateSiteAddressInputRequestTypeDef",
    "AssetInfoTypeDef",
    "CatalogItemTypeDef",
    "CreateOrderInputRequestTypeDef",
    "GetConnectionResponseTypeDef",
    "GetSiteAddressOutputTypeDef",
    "ListCapacityTasksOutputTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartConnectionResponseTypeDef",
    "UpdateSiteAddressOutputTypeDef",
    "CreateOutpostOutputTypeDef",
    "GetOutpostOutputTypeDef",
    "ListOutpostsOutputTypeDef",
    "UpdateOutpostOutputTypeDef",
    "CreateSiteInputRequestTypeDef",
    "SiteTypeDef",
    "GetCapacityTaskOutputTypeDef",
    "StartCapacityTaskInputRequestTypeDef",
    "StartCapacityTaskOutputTypeDef",
    "GetOutpostInstanceTypesInputGetOutpostInstanceTypesPaginateTypeDef",
    "GetOutpostSupportedInstanceTypesInputGetOutpostSupportedInstanceTypesPaginateTypeDef",
    "ListAssetsInputListAssetsPaginateTypeDef",
    "ListCapacityTasksInputListCapacityTasksPaginateTypeDef",
    "ListCatalogItemsInputListCatalogItemsPaginateTypeDef",
    "ListOrdersInputListOrdersPaginateTypeDef",
    "ListOutpostsInputListOutpostsPaginateTypeDef",
    "ListSitesInputListSitesPaginateTypeDef",
    "GetOutpostInstanceTypesOutputTypeDef",
    "GetOutpostSupportedInstanceTypesOutputTypeDef",
    "LineItemTypeDef",
    "ListOrdersOutputTypeDef",
    "ListAssetsOutputTypeDef",
    "GetCatalogItemOutputTypeDef",
    "ListCatalogItemsOutputTypeDef",
    "CreateSiteOutputTypeDef",
    "GetSiteOutputTypeDef",
    "ListSitesOutputTypeDef",
    "UpdateSiteOutputTypeDef",
    "UpdateSiteRackPhysicalPropertiesOutputTypeDef",
    "OrderTypeDef",
    "CreateOrderOutputTypeDef",
    "GetOrderOutputTypeDef",
)

AddressTypeDef = TypedDict(
    "AddressTypeDef",
    {
        "AddressLine1": str,
        "City": str,
        "StateOrRegion": str,
        "PostalCode": str,
        "CountryCode": str,
        "ContactName": NotRequired[str],
        "ContactPhoneNumber": NotRequired[str],
        "AddressLine2": NotRequired[str],
        "AddressLine3": NotRequired[str],
        "DistrictOrCounty": NotRequired[str],
        "Municipality": NotRequired[str],
    },
)
AssetLocationTypeDef = TypedDict(
    "AssetLocationTypeDef",
    {
        "RackElevation": NotRequired[float],
    },
)
ComputeAttributesTypeDef = TypedDict(
    "ComputeAttributesTypeDef",
    {
        "HostId": NotRequired[str],
        "State": NotRequired[ComputeAssetStateType],
        "InstanceFamilies": NotRequired[List[str]],
    },
)
CancelCapacityTaskInputRequestTypeDef = TypedDict(
    "CancelCapacityTaskInputRequestTypeDef",
    {
        "CapacityTaskId": str,
        "OutpostIdentifier": str,
    },
)
CancelOrderInputRequestTypeDef = TypedDict(
    "CancelOrderInputRequestTypeDef",
    {
        "OrderId": str,
    },
)
CapacityTaskFailureTypeDef = TypedDict(
    "CapacityTaskFailureTypeDef",
    {
        "Reason": str,
        "Type": NotRequired[Literal["UNSUPPORTED_CAPACITY_CONFIGURATION"]],
    },
)
CapacityTaskSummaryTypeDef = TypedDict(
    "CapacityTaskSummaryTypeDef",
    {
        "CapacityTaskId": NotRequired[str],
        "OutpostId": NotRequired[str],
        "OrderId": NotRequired[str],
        "CapacityTaskStatus": NotRequired[CapacityTaskStatusType],
        "CreationDate": NotRequired[datetime],
        "CompletionDate": NotRequired[datetime],
        "LastModifiedDate": NotRequired[datetime],
    },
)
EC2CapacityTypeDef = TypedDict(
    "EC2CapacityTypeDef",
    {
        "Family": NotRequired[str],
        "MaxSize": NotRequired[str],
        "Quantity": NotRequired[str],
    },
)
ConnectionDetailsTypeDef = TypedDict(
    "ConnectionDetailsTypeDef",
    {
        "ClientPublicKey": NotRequired[str],
        "ServerPublicKey": NotRequired[str],
        "ServerEndpoint": NotRequired[str],
        "ClientTunnelAddress": NotRequired[str],
        "ServerTunnelAddress": NotRequired[str],
        "AllowedIps": NotRequired[List[str]],
    },
)
LineItemRequestTypeDef = TypedDict(
    "LineItemRequestTypeDef",
    {
        "CatalogItemId": NotRequired[str],
        "Quantity": NotRequired[int],
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
CreateOutpostInputRequestTypeDef = TypedDict(
    "CreateOutpostInputRequestTypeDef",
    {
        "Name": str,
        "SiteId": str,
        "Description": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "AvailabilityZoneId": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "SupportedHardwareType": NotRequired[SupportedHardwareTypeType],
    },
)
OutpostTypeDef = TypedDict(
    "OutpostTypeDef",
    {
        "OutpostId": NotRequired[str],
        "OwnerId": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "SiteId": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "LifeCycleStatus": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "AvailabilityZoneId": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
        "SiteArn": NotRequired[str],
        "SupportedHardwareType": NotRequired[SupportedHardwareTypeType],
    },
)
RackPhysicalPropertiesTypeDef = TypedDict(
    "RackPhysicalPropertiesTypeDef",
    {
        "PowerDrawKva": NotRequired[PowerDrawKvaType],
        "PowerPhase": NotRequired[PowerPhaseType],
        "PowerConnector": NotRequired[PowerConnectorType],
        "PowerFeedDrop": NotRequired[PowerFeedDropType],
        "UplinkGbps": NotRequired[UplinkGbpsType],
        "UplinkCount": NotRequired[UplinkCountType],
        "FiberOpticCableType": NotRequired[FiberOpticCableTypeType],
        "OpticalStandard": NotRequired[OpticalStandardType],
        "MaximumSupportedWeightLbs": NotRequired[MaximumSupportedWeightLbsType],
    },
)
DeleteOutpostInputRequestTypeDef = TypedDict(
    "DeleteOutpostInputRequestTypeDef",
    {
        "OutpostId": str,
    },
)
DeleteSiteInputRequestTypeDef = TypedDict(
    "DeleteSiteInputRequestTypeDef",
    {
        "SiteId": str,
    },
)
GetCapacityTaskInputRequestTypeDef = TypedDict(
    "GetCapacityTaskInputRequestTypeDef",
    {
        "CapacityTaskId": str,
        "OutpostIdentifier": str,
    },
)
InstanceTypeCapacityTypeDef = TypedDict(
    "InstanceTypeCapacityTypeDef",
    {
        "InstanceType": str,
        "Count": int,
    },
)
GetCatalogItemInputRequestTypeDef = TypedDict(
    "GetCatalogItemInputRequestTypeDef",
    {
        "CatalogItemId": str,
    },
)
GetConnectionRequestRequestTypeDef = TypedDict(
    "GetConnectionRequestRequestTypeDef",
    {
        "ConnectionId": str,
    },
)
GetOrderInputRequestTypeDef = TypedDict(
    "GetOrderInputRequestTypeDef",
    {
        "OrderId": str,
    },
)
GetOutpostInputRequestTypeDef = TypedDict(
    "GetOutpostInputRequestTypeDef",
    {
        "OutpostId": str,
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
GetOutpostInstanceTypesInputRequestTypeDef = TypedDict(
    "GetOutpostInstanceTypesInputRequestTypeDef",
    {
        "OutpostId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
InstanceTypeItemTypeDef = TypedDict(
    "InstanceTypeItemTypeDef",
    {
        "InstanceType": NotRequired[str],
        "VCPUs": NotRequired[int],
    },
)
GetOutpostSupportedInstanceTypesInputRequestTypeDef = TypedDict(
    "GetOutpostSupportedInstanceTypesInputRequestTypeDef",
    {
        "OutpostIdentifier": str,
        "OrderId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetSiteAddressInputRequestTypeDef = TypedDict(
    "GetSiteAddressInputRequestTypeDef",
    {
        "SiteId": str,
        "AddressType": AddressTypeType,
    },
)
GetSiteInputRequestTypeDef = TypedDict(
    "GetSiteInputRequestTypeDef",
    {
        "SiteId": str,
    },
)
LineItemAssetInformationTypeDef = TypedDict(
    "LineItemAssetInformationTypeDef",
    {
        "AssetId": NotRequired[str],
        "MacAddressList": NotRequired[List[str]],
    },
)
ShipmentInformationTypeDef = TypedDict(
    "ShipmentInformationTypeDef",
    {
        "ShipmentTrackingNumber": NotRequired[str],
        "ShipmentCarrier": NotRequired[ShipmentCarrierType],
    },
)
ListAssetsInputRequestTypeDef = TypedDict(
    "ListAssetsInputRequestTypeDef",
    {
        "OutpostIdentifier": str,
        "HostIdFilter": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "StatusFilter": NotRequired[Sequence[AssetStateType]],
    },
)
ListCapacityTasksInputRequestTypeDef = TypedDict(
    "ListCapacityTasksInputRequestTypeDef",
    {
        "OutpostIdentifierFilter": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "CapacityTaskStatusFilter": NotRequired[Sequence[CapacityTaskStatusType]],
    },
)
ListCatalogItemsInputRequestTypeDef = TypedDict(
    "ListCatalogItemsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ItemClassFilter": NotRequired[Sequence[CatalogItemClassType]],
        "SupportedStorageFilter": NotRequired[Sequence[SupportedStorageEnumType]],
        "EC2FamilyFilter": NotRequired[Sequence[str]],
    },
)
ListOrdersInputRequestTypeDef = TypedDict(
    "ListOrdersInputRequestTypeDef",
    {
        "OutpostIdentifierFilter": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
OrderSummaryTypeDef = TypedDict(
    "OrderSummaryTypeDef",
    {
        "OutpostId": NotRequired[str],
        "OrderId": NotRequired[str],
        "OrderType": NotRequired[OrderTypeType],
        "Status": NotRequired[OrderStatusType],
        "LineItemCountsByStatus": NotRequired[Dict[LineItemStatusType, int]],
        "OrderSubmissionDate": NotRequired[datetime],
        "OrderFulfilledDate": NotRequired[datetime],
    },
)
ListOutpostsInputRequestTypeDef = TypedDict(
    "ListOutpostsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "LifeCycleStatusFilter": NotRequired[Sequence[str]],
        "AvailabilityZoneFilter": NotRequired[Sequence[str]],
        "AvailabilityZoneIdFilter": NotRequired[Sequence[str]],
    },
)
ListSitesInputRequestTypeDef = TypedDict(
    "ListSitesInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "OperatingAddressCountryCodeFilter": NotRequired[Sequence[str]],
        "OperatingAddressStateOrRegionFilter": NotRequired[Sequence[str]],
        "OperatingAddressCityFilter": NotRequired[Sequence[str]],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
StartConnectionRequestRequestTypeDef = TypedDict(
    "StartConnectionRequestRequestTypeDef",
    {
        "AssetId": str,
        "ClientPublicKey": str,
        "NetworkInterfaceDeviceIndex": int,
        "DeviceSerialNumber": NotRequired[str],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateOutpostInputRequestTypeDef = TypedDict(
    "UpdateOutpostInputRequestTypeDef",
    {
        "OutpostId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "SupportedHardwareType": NotRequired[SupportedHardwareTypeType],
    },
)
UpdateSiteInputRequestTypeDef = TypedDict(
    "UpdateSiteInputRequestTypeDef",
    {
        "SiteId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Notes": NotRequired[str],
    },
)
UpdateSiteRackPhysicalPropertiesInputRequestTypeDef = TypedDict(
    "UpdateSiteRackPhysicalPropertiesInputRequestTypeDef",
    {
        "SiteId": str,
        "PowerDrawKva": NotRequired[PowerDrawKvaType],
        "PowerPhase": NotRequired[PowerPhaseType],
        "PowerConnector": NotRequired[PowerConnectorType],
        "PowerFeedDrop": NotRequired[PowerFeedDropType],
        "UplinkGbps": NotRequired[UplinkGbpsType],
        "UplinkCount": NotRequired[UplinkCountType],
        "FiberOpticCableType": NotRequired[FiberOpticCableTypeType],
        "OpticalStandard": NotRequired[OpticalStandardType],
        "MaximumSupportedWeightLbs": NotRequired[MaximumSupportedWeightLbsType],
    },
)
UpdateSiteAddressInputRequestTypeDef = TypedDict(
    "UpdateSiteAddressInputRequestTypeDef",
    {
        "SiteId": str,
        "AddressType": AddressTypeType,
        "Address": AddressTypeDef,
    },
)
AssetInfoTypeDef = TypedDict(
    "AssetInfoTypeDef",
    {
        "AssetId": NotRequired[str],
        "RackId": NotRequired[str],
        "AssetType": NotRequired[Literal["COMPUTE"]],
        "ComputeAttributes": NotRequired[ComputeAttributesTypeDef],
        "AssetLocation": NotRequired[AssetLocationTypeDef],
    },
)
CatalogItemTypeDef = TypedDict(
    "CatalogItemTypeDef",
    {
        "CatalogItemId": NotRequired[str],
        "ItemStatus": NotRequired[CatalogItemStatusType],
        "EC2Capacities": NotRequired[List[EC2CapacityTypeDef]],
        "PowerKva": NotRequired[float],
        "WeightLbs": NotRequired[int],
        "SupportedUplinkGbps": NotRequired[List[int]],
        "SupportedStorage": NotRequired[List[SupportedStorageEnumType]],
    },
)
CreateOrderInputRequestTypeDef = TypedDict(
    "CreateOrderInputRequestTypeDef",
    {
        "OutpostIdentifier": str,
        "LineItems": Sequence[LineItemRequestTypeDef],
        "PaymentOption": PaymentOptionType,
        "PaymentTerm": NotRequired[PaymentTermType],
    },
)
GetConnectionResponseTypeDef = TypedDict(
    "GetConnectionResponseTypeDef",
    {
        "ConnectionId": str,
        "ConnectionDetails": ConnectionDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSiteAddressOutputTypeDef = TypedDict(
    "GetSiteAddressOutputTypeDef",
    {
        "SiteId": str,
        "AddressType": AddressTypeType,
        "Address": AddressTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCapacityTasksOutputTypeDef = TypedDict(
    "ListCapacityTasksOutputTypeDef",
    {
        "CapacityTasks": List[CapacityTaskSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartConnectionResponseTypeDef = TypedDict(
    "StartConnectionResponseTypeDef",
    {
        "ConnectionId": str,
        "UnderlayIpAddress": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSiteAddressOutputTypeDef = TypedDict(
    "UpdateSiteAddressOutputTypeDef",
    {
        "AddressType": AddressTypeType,
        "Address": AddressTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateOutpostOutputTypeDef = TypedDict(
    "CreateOutpostOutputTypeDef",
    {
        "Outpost": OutpostTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetOutpostOutputTypeDef = TypedDict(
    "GetOutpostOutputTypeDef",
    {
        "Outpost": OutpostTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListOutpostsOutputTypeDef = TypedDict(
    "ListOutpostsOutputTypeDef",
    {
        "Outposts": List[OutpostTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateOutpostOutputTypeDef = TypedDict(
    "UpdateOutpostOutputTypeDef",
    {
        "Outpost": OutpostTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSiteInputRequestTypeDef = TypedDict(
    "CreateSiteInputRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "Notes": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "OperatingAddress": NotRequired[AddressTypeDef],
        "ShippingAddress": NotRequired[AddressTypeDef],
        "RackPhysicalProperties": NotRequired[RackPhysicalPropertiesTypeDef],
    },
)
SiteTypeDef = TypedDict(
    "SiteTypeDef",
    {
        "SiteId": NotRequired[str],
        "AccountId": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
        "SiteArn": NotRequired[str],
        "Notes": NotRequired[str],
        "OperatingAddressCountryCode": NotRequired[str],
        "OperatingAddressStateOrRegion": NotRequired[str],
        "OperatingAddressCity": NotRequired[str],
        "RackPhysicalProperties": NotRequired[RackPhysicalPropertiesTypeDef],
    },
)
GetCapacityTaskOutputTypeDef = TypedDict(
    "GetCapacityTaskOutputTypeDef",
    {
        "CapacityTaskId": str,
        "OutpostId": str,
        "OrderId": str,
        "RequestedInstancePools": List[InstanceTypeCapacityTypeDef],
        "DryRun": bool,
        "CapacityTaskStatus": CapacityTaskStatusType,
        "Failed": CapacityTaskFailureTypeDef,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "LastModifiedDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartCapacityTaskInputRequestTypeDef = TypedDict(
    "StartCapacityTaskInputRequestTypeDef",
    {
        "OutpostIdentifier": str,
        "OrderId": str,
        "InstancePools": Sequence[InstanceTypeCapacityTypeDef],
        "DryRun": NotRequired[bool],
    },
)
StartCapacityTaskOutputTypeDef = TypedDict(
    "StartCapacityTaskOutputTypeDef",
    {
        "CapacityTaskId": str,
        "OutpostId": str,
        "OrderId": str,
        "RequestedInstancePools": List[InstanceTypeCapacityTypeDef],
        "DryRun": bool,
        "CapacityTaskStatus": CapacityTaskStatusType,
        "Failed": CapacityTaskFailureTypeDef,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "LastModifiedDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetOutpostInstanceTypesInputGetOutpostInstanceTypesPaginateTypeDef = TypedDict(
    "GetOutpostInstanceTypesInputGetOutpostInstanceTypesPaginateTypeDef",
    {
        "OutpostId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetOutpostSupportedInstanceTypesInputGetOutpostSupportedInstanceTypesPaginateTypeDef = TypedDict(
    "GetOutpostSupportedInstanceTypesInputGetOutpostSupportedInstanceTypesPaginateTypeDef",
    {
        "OutpostIdentifier": str,
        "OrderId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAssetsInputListAssetsPaginateTypeDef = TypedDict(
    "ListAssetsInputListAssetsPaginateTypeDef",
    {
        "OutpostIdentifier": str,
        "HostIdFilter": NotRequired[Sequence[str]],
        "StatusFilter": NotRequired[Sequence[AssetStateType]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCapacityTasksInputListCapacityTasksPaginateTypeDef = TypedDict(
    "ListCapacityTasksInputListCapacityTasksPaginateTypeDef",
    {
        "OutpostIdentifierFilter": NotRequired[str],
        "CapacityTaskStatusFilter": NotRequired[Sequence[CapacityTaskStatusType]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCatalogItemsInputListCatalogItemsPaginateTypeDef = TypedDict(
    "ListCatalogItemsInputListCatalogItemsPaginateTypeDef",
    {
        "ItemClassFilter": NotRequired[Sequence[CatalogItemClassType]],
        "SupportedStorageFilter": NotRequired[Sequence[SupportedStorageEnumType]],
        "EC2FamilyFilter": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOrdersInputListOrdersPaginateTypeDef = TypedDict(
    "ListOrdersInputListOrdersPaginateTypeDef",
    {
        "OutpostIdentifierFilter": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOutpostsInputListOutpostsPaginateTypeDef = TypedDict(
    "ListOutpostsInputListOutpostsPaginateTypeDef",
    {
        "LifeCycleStatusFilter": NotRequired[Sequence[str]],
        "AvailabilityZoneFilter": NotRequired[Sequence[str]],
        "AvailabilityZoneIdFilter": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSitesInputListSitesPaginateTypeDef = TypedDict(
    "ListSitesInputListSitesPaginateTypeDef",
    {
        "OperatingAddressCountryCodeFilter": NotRequired[Sequence[str]],
        "OperatingAddressStateOrRegionFilter": NotRequired[Sequence[str]],
        "OperatingAddressCityFilter": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetOutpostInstanceTypesOutputTypeDef = TypedDict(
    "GetOutpostInstanceTypesOutputTypeDef",
    {
        "InstanceTypes": List[InstanceTypeItemTypeDef],
        "OutpostId": str,
        "OutpostArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetOutpostSupportedInstanceTypesOutputTypeDef = TypedDict(
    "GetOutpostSupportedInstanceTypesOutputTypeDef",
    {
        "InstanceTypes": List[InstanceTypeItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
LineItemTypeDef = TypedDict(
    "LineItemTypeDef",
    {
        "CatalogItemId": NotRequired[str],
        "LineItemId": NotRequired[str],
        "Quantity": NotRequired[int],
        "Status": NotRequired[LineItemStatusType],
        "ShipmentInformation": NotRequired[ShipmentInformationTypeDef],
        "AssetInformationList": NotRequired[List[LineItemAssetInformationTypeDef]],
        "PreviousLineItemId": NotRequired[str],
        "PreviousOrderId": NotRequired[str],
    },
)
ListOrdersOutputTypeDef = TypedDict(
    "ListOrdersOutputTypeDef",
    {
        "Orders": List[OrderSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListAssetsOutputTypeDef = TypedDict(
    "ListAssetsOutputTypeDef",
    {
        "Assets": List[AssetInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetCatalogItemOutputTypeDef = TypedDict(
    "GetCatalogItemOutputTypeDef",
    {
        "CatalogItem": CatalogItemTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCatalogItemsOutputTypeDef = TypedDict(
    "ListCatalogItemsOutputTypeDef",
    {
        "CatalogItems": List[CatalogItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateSiteOutputTypeDef = TypedDict(
    "CreateSiteOutputTypeDef",
    {
        "Site": SiteTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSiteOutputTypeDef = TypedDict(
    "GetSiteOutputTypeDef",
    {
        "Site": SiteTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSitesOutputTypeDef = TypedDict(
    "ListSitesOutputTypeDef",
    {
        "Sites": List[SiteTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateSiteOutputTypeDef = TypedDict(
    "UpdateSiteOutputTypeDef",
    {
        "Site": SiteTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSiteRackPhysicalPropertiesOutputTypeDef = TypedDict(
    "UpdateSiteRackPhysicalPropertiesOutputTypeDef",
    {
        "Site": SiteTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OrderTypeDef = TypedDict(
    "OrderTypeDef",
    {
        "OutpostId": NotRequired[str],
        "OrderId": NotRequired[str],
        "Status": NotRequired[OrderStatusType],
        "LineItems": NotRequired[List[LineItemTypeDef]],
        "PaymentOption": NotRequired[PaymentOptionType],
        "OrderSubmissionDate": NotRequired[datetime],
        "OrderFulfilledDate": NotRequired[datetime],
        "PaymentTerm": NotRequired[PaymentTermType],
        "OrderType": NotRequired[OrderTypeType],
    },
)
CreateOrderOutputTypeDef = TypedDict(
    "CreateOrderOutputTypeDef",
    {
        "Order": OrderTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetOrderOutputTypeDef = TypedDict(
    "GetOrderOutputTypeDef",
    {
        "Order": OrderTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
