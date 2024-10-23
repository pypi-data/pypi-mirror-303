"""
Type annotations for privatenetworks service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/type_defs/)

Usage::

    ```python
    from mypy_boto3_privatenetworks.type_defs import AcknowledgeOrderReceiptRequestRequestTypeDef

    data: AcknowledgeOrderReceiptRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AcknowledgmentStatusType,
    CommitmentLengthType,
    DeviceIdentifierFilterKeysType,
    DeviceIdentifierStatusType,
    ElevationReferenceType,
    HealthStatusType,
    NetworkResourceDefinitionTypeType,
    NetworkResourceFilterKeysType,
    NetworkResourceStatusType,
    NetworkSiteStatusType,
    NetworkStatusType,
    OrderFilterKeysType,
    UpdateTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AcknowledgeOrderReceiptRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "ActivateDeviceIdentifierRequestRequestTypeDef",
    "DeviceIdentifierTypeDef",
    "AddressTypeDef",
    "CommitmentConfigurationTypeDef",
    "PositionTypeDef",
    "CreateNetworkRequestRequestTypeDef",
    "NetworkTypeDef",
    "DeactivateDeviceIdentifierRequestRequestTypeDef",
    "DeleteNetworkRequestRequestTypeDef",
    "DeleteNetworkSiteRequestRequestTypeDef",
    "GetDeviceIdentifierRequestRequestTypeDef",
    "GetNetworkRequestRequestTypeDef",
    "GetNetworkResourceRequestRequestTypeDef",
    "GetNetworkSiteRequestRequestTypeDef",
    "GetOrderRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListDeviceIdentifiersRequestRequestTypeDef",
    "ListNetworkResourcesRequestRequestTypeDef",
    "ListNetworkSitesRequestRequestTypeDef",
    "ListNetworksRequestRequestTypeDef",
    "ListOrdersRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "NameValuePairTypeDef",
    "TrackingInformationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateNetworkSiteRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PingResponseTypeDef",
    "ActivateDeviceIdentifierResponseTypeDef",
    "DeactivateDeviceIdentifierResponseTypeDef",
    "GetDeviceIdentifierResponseTypeDef",
    "ListDeviceIdentifiersResponseTypeDef",
    "ReturnInformationTypeDef",
    "ActivateNetworkSiteRequestRequestTypeDef",
    "CommitmentInformationTypeDef",
    "OrderedResourceDefinitionTypeDef",
    "StartNetworkResourceUpdateRequestRequestTypeDef",
    "ConfigureAccessPointRequestRequestTypeDef",
    "CreateNetworkResponseTypeDef",
    "DeleteNetworkResponseTypeDef",
    "GetNetworkResponseTypeDef",
    "ListNetworksResponseTypeDef",
    "ListDeviceIdentifiersRequestListDeviceIdentifiersPaginateTypeDef",
    "ListNetworkResourcesRequestListNetworkResourcesPaginateTypeDef",
    "ListNetworkSitesRequestListNetworkSitesPaginateTypeDef",
    "ListNetworksRequestListNetworksPaginateTypeDef",
    "ListOrdersRequestListOrdersPaginateTypeDef",
    "NetworkResourceDefinitionOutputTypeDef",
    "NetworkResourceDefinitionTypeDef",
    "NetworkResourceTypeDef",
    "OrderTypeDef",
    "SitePlanOutputTypeDef",
    "NetworkResourceDefinitionUnionTypeDef",
    "ConfigureAccessPointResponseTypeDef",
    "GetNetworkResourceResponseTypeDef",
    "ListNetworkResourcesResponseTypeDef",
    "StartNetworkResourceUpdateResponseTypeDef",
    "AcknowledgeOrderReceiptResponseTypeDef",
    "GetOrderResponseTypeDef",
    "ListOrdersResponseTypeDef",
    "NetworkSiteTypeDef",
    "SitePlanTypeDef",
    "ActivateNetworkSiteResponseTypeDef",
    "CreateNetworkSiteResponseTypeDef",
    "DeleteNetworkSiteResponseTypeDef",
    "GetNetworkSiteResponseTypeDef",
    "ListNetworkSitesResponseTypeDef",
    "UpdateNetworkSiteResponseTypeDef",
    "CreateNetworkSiteRequestRequestTypeDef",
    "UpdateNetworkSitePlanRequestRequestTypeDef",
)

AcknowledgeOrderReceiptRequestRequestTypeDef = TypedDict(
    "AcknowledgeOrderReceiptRequestRequestTypeDef",
    {
        "orderArn": str,
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
ActivateDeviceIdentifierRequestRequestTypeDef = TypedDict(
    "ActivateDeviceIdentifierRequestRequestTypeDef",
    {
        "deviceIdentifierArn": str,
        "clientToken": NotRequired[str],
    },
)
DeviceIdentifierTypeDef = TypedDict(
    "DeviceIdentifierTypeDef",
    {
        "createdAt": NotRequired[datetime],
        "deviceIdentifierArn": NotRequired[str],
        "iccid": NotRequired[str],
        "imsi": NotRequired[str],
        "networkArn": NotRequired[str],
        "orderArn": NotRequired[str],
        "status": NotRequired[DeviceIdentifierStatusType],
        "trafficGroupArn": NotRequired[str],
        "vendor": NotRequired[str],
    },
)
AddressTypeDef = TypedDict(
    "AddressTypeDef",
    {
        "city": str,
        "country": str,
        "name": str,
        "postalCode": str,
        "stateOrProvince": str,
        "street1": str,
        "company": NotRequired[str],
        "emailAddress": NotRequired[str],
        "phoneNumber": NotRequired[str],
        "street2": NotRequired[str],
        "street3": NotRequired[str],
    },
)
CommitmentConfigurationTypeDef = TypedDict(
    "CommitmentConfigurationTypeDef",
    {
        "automaticRenewal": bool,
        "commitmentLength": CommitmentLengthType,
    },
)
PositionTypeDef = TypedDict(
    "PositionTypeDef",
    {
        "elevation": NotRequired[float],
        "elevationReference": NotRequired[ElevationReferenceType],
        "elevationUnit": NotRequired[Literal["FEET"]],
        "latitude": NotRequired[float],
        "longitude": NotRequired[float],
    },
)
CreateNetworkRequestRequestTypeDef = TypedDict(
    "CreateNetworkRequestRequestTypeDef",
    {
        "networkName": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
NetworkTypeDef = TypedDict(
    "NetworkTypeDef",
    {
        "networkArn": str,
        "networkName": str,
        "status": NetworkStatusType,
        "createdAt": NotRequired[datetime],
        "description": NotRequired[str],
        "statusReason": NotRequired[str],
    },
)
DeactivateDeviceIdentifierRequestRequestTypeDef = TypedDict(
    "DeactivateDeviceIdentifierRequestRequestTypeDef",
    {
        "deviceIdentifierArn": str,
        "clientToken": NotRequired[str],
    },
)
DeleteNetworkRequestRequestTypeDef = TypedDict(
    "DeleteNetworkRequestRequestTypeDef",
    {
        "networkArn": str,
        "clientToken": NotRequired[str],
    },
)
DeleteNetworkSiteRequestRequestTypeDef = TypedDict(
    "DeleteNetworkSiteRequestRequestTypeDef",
    {
        "networkSiteArn": str,
        "clientToken": NotRequired[str],
    },
)
GetDeviceIdentifierRequestRequestTypeDef = TypedDict(
    "GetDeviceIdentifierRequestRequestTypeDef",
    {
        "deviceIdentifierArn": str,
    },
)
GetNetworkRequestRequestTypeDef = TypedDict(
    "GetNetworkRequestRequestTypeDef",
    {
        "networkArn": str,
    },
)
GetNetworkResourceRequestRequestTypeDef = TypedDict(
    "GetNetworkResourceRequestRequestTypeDef",
    {
        "networkResourceArn": str,
    },
)
GetNetworkSiteRequestRequestTypeDef = TypedDict(
    "GetNetworkSiteRequestRequestTypeDef",
    {
        "networkSiteArn": str,
    },
)
GetOrderRequestRequestTypeDef = TypedDict(
    "GetOrderRequestRequestTypeDef",
    {
        "orderArn": str,
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
ListDeviceIdentifiersRequestRequestTypeDef = TypedDict(
    "ListDeviceIdentifiersRequestRequestTypeDef",
    {
        "networkArn": str,
        "filters": NotRequired[Mapping[DeviceIdentifierFilterKeysType, Sequence[str]]],
        "maxResults": NotRequired[int],
        "startToken": NotRequired[str],
    },
)
ListNetworkResourcesRequestRequestTypeDef = TypedDict(
    "ListNetworkResourcesRequestRequestTypeDef",
    {
        "networkArn": str,
        "filters": NotRequired[Mapping[NetworkResourceFilterKeysType, Sequence[str]]],
        "maxResults": NotRequired[int],
        "startToken": NotRequired[str],
    },
)
ListNetworkSitesRequestRequestTypeDef = TypedDict(
    "ListNetworkSitesRequestRequestTypeDef",
    {
        "networkArn": str,
        "filters": NotRequired[Mapping[Literal["STATUS"], Sequence[str]]],
        "maxResults": NotRequired[int],
        "startToken": NotRequired[str],
    },
)
ListNetworksRequestRequestTypeDef = TypedDict(
    "ListNetworksRequestRequestTypeDef",
    {
        "filters": NotRequired[Mapping[Literal["STATUS"], Sequence[str]]],
        "maxResults": NotRequired[int],
        "startToken": NotRequired[str],
    },
)
ListOrdersRequestRequestTypeDef = TypedDict(
    "ListOrdersRequestRequestTypeDef",
    {
        "networkArn": str,
        "filters": NotRequired[Mapping[OrderFilterKeysType, Sequence[str]]],
        "maxResults": NotRequired[int],
        "startToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
NameValuePairTypeDef = TypedDict(
    "NameValuePairTypeDef",
    {
        "name": str,
        "value": NotRequired[str],
    },
)
TrackingInformationTypeDef = TypedDict(
    "TrackingInformationTypeDef",
    {
        "trackingNumber": NotRequired[str],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UpdateNetworkSiteRequestRequestTypeDef = TypedDict(
    "UpdateNetworkSiteRequestRequestTypeDef",
    {
        "networkSiteArn": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PingResponseTypeDef = TypedDict(
    "PingResponseTypeDef",
    {
        "status": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ActivateDeviceIdentifierResponseTypeDef = TypedDict(
    "ActivateDeviceIdentifierResponseTypeDef",
    {
        "deviceIdentifier": DeviceIdentifierTypeDef,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeactivateDeviceIdentifierResponseTypeDef = TypedDict(
    "DeactivateDeviceIdentifierResponseTypeDef",
    {
        "deviceIdentifier": DeviceIdentifierTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDeviceIdentifierResponseTypeDef = TypedDict(
    "GetDeviceIdentifierResponseTypeDef",
    {
        "deviceIdentifier": DeviceIdentifierTypeDef,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDeviceIdentifiersResponseTypeDef = TypedDict(
    "ListDeviceIdentifiersResponseTypeDef",
    {
        "deviceIdentifiers": List[DeviceIdentifierTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReturnInformationTypeDef = TypedDict(
    "ReturnInformationTypeDef",
    {
        "replacementOrderArn": NotRequired[str],
        "returnReason": NotRequired[str],
        "shippingAddress": NotRequired[AddressTypeDef],
        "shippingLabel": NotRequired[str],
    },
)
ActivateNetworkSiteRequestRequestTypeDef = TypedDict(
    "ActivateNetworkSiteRequestRequestTypeDef",
    {
        "networkSiteArn": str,
        "shippingAddress": AddressTypeDef,
        "clientToken": NotRequired[str],
        "commitmentConfiguration": NotRequired[CommitmentConfigurationTypeDef],
    },
)
CommitmentInformationTypeDef = TypedDict(
    "CommitmentInformationTypeDef",
    {
        "commitmentConfiguration": CommitmentConfigurationTypeDef,
        "expiresOn": NotRequired[datetime],
        "startAt": NotRequired[datetime],
    },
)
OrderedResourceDefinitionTypeDef = TypedDict(
    "OrderedResourceDefinitionTypeDef",
    {
        "count": int,
        "type": NetworkResourceDefinitionTypeType,
        "commitmentConfiguration": NotRequired[CommitmentConfigurationTypeDef],
    },
)
StartNetworkResourceUpdateRequestRequestTypeDef = TypedDict(
    "StartNetworkResourceUpdateRequestRequestTypeDef",
    {
        "networkResourceArn": str,
        "updateType": UpdateTypeType,
        "commitmentConfiguration": NotRequired[CommitmentConfigurationTypeDef],
        "returnReason": NotRequired[str],
        "shippingAddress": NotRequired[AddressTypeDef],
    },
)
ConfigureAccessPointRequestRequestTypeDef = TypedDict(
    "ConfigureAccessPointRequestRequestTypeDef",
    {
        "accessPointArn": str,
        "cpiSecretKey": NotRequired[str],
        "cpiUserId": NotRequired[str],
        "cpiUserPassword": NotRequired[str],
        "cpiUsername": NotRequired[str],
        "position": NotRequired[PositionTypeDef],
    },
)
CreateNetworkResponseTypeDef = TypedDict(
    "CreateNetworkResponseTypeDef",
    {
        "network": NetworkTypeDef,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteNetworkResponseTypeDef = TypedDict(
    "DeleteNetworkResponseTypeDef",
    {
        "network": NetworkTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetNetworkResponseTypeDef = TypedDict(
    "GetNetworkResponseTypeDef",
    {
        "network": NetworkTypeDef,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListNetworksResponseTypeDef = TypedDict(
    "ListNetworksResponseTypeDef",
    {
        "networks": List[NetworkTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDeviceIdentifiersRequestListDeviceIdentifiersPaginateTypeDef = TypedDict(
    "ListDeviceIdentifiersRequestListDeviceIdentifiersPaginateTypeDef",
    {
        "networkArn": str,
        "filters": NotRequired[Mapping[DeviceIdentifierFilterKeysType, Sequence[str]]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListNetworkResourcesRequestListNetworkResourcesPaginateTypeDef = TypedDict(
    "ListNetworkResourcesRequestListNetworkResourcesPaginateTypeDef",
    {
        "networkArn": str,
        "filters": NotRequired[Mapping[NetworkResourceFilterKeysType, Sequence[str]]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListNetworkSitesRequestListNetworkSitesPaginateTypeDef = TypedDict(
    "ListNetworkSitesRequestListNetworkSitesPaginateTypeDef",
    {
        "networkArn": str,
        "filters": NotRequired[Mapping[Literal["STATUS"], Sequence[str]]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListNetworksRequestListNetworksPaginateTypeDef = TypedDict(
    "ListNetworksRequestListNetworksPaginateTypeDef",
    {
        "filters": NotRequired[Mapping[Literal["STATUS"], Sequence[str]]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOrdersRequestListOrdersPaginateTypeDef = TypedDict(
    "ListOrdersRequestListOrdersPaginateTypeDef",
    {
        "networkArn": str,
        "filters": NotRequired[Mapping[OrderFilterKeysType, Sequence[str]]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
NetworkResourceDefinitionOutputTypeDef = TypedDict(
    "NetworkResourceDefinitionOutputTypeDef",
    {
        "count": int,
        "type": NetworkResourceDefinitionTypeType,
        "options": NotRequired[List[NameValuePairTypeDef]],
    },
)
NetworkResourceDefinitionTypeDef = TypedDict(
    "NetworkResourceDefinitionTypeDef",
    {
        "count": int,
        "type": NetworkResourceDefinitionTypeType,
        "options": NotRequired[Sequence[NameValuePairTypeDef]],
    },
)
NetworkResourceTypeDef = TypedDict(
    "NetworkResourceTypeDef",
    {
        "attributes": NotRequired[List[NameValuePairTypeDef]],
        "commitmentInformation": NotRequired[CommitmentInformationTypeDef],
        "createdAt": NotRequired[datetime],
        "description": NotRequired[str],
        "health": NotRequired[HealthStatusType],
        "model": NotRequired[str],
        "networkArn": NotRequired[str],
        "networkResourceArn": NotRequired[str],
        "networkSiteArn": NotRequired[str],
        "orderArn": NotRequired[str],
        "position": NotRequired[PositionTypeDef],
        "returnInformation": NotRequired[ReturnInformationTypeDef],
        "serialNumber": NotRequired[str],
        "status": NotRequired[NetworkResourceStatusType],
        "statusReason": NotRequired[str],
        "type": NotRequired[Literal["RADIO_UNIT"]],
        "vendor": NotRequired[str],
    },
)
OrderTypeDef = TypedDict(
    "OrderTypeDef",
    {
        "acknowledgmentStatus": NotRequired[AcknowledgmentStatusType],
        "createdAt": NotRequired[datetime],
        "networkArn": NotRequired[str],
        "networkSiteArn": NotRequired[str],
        "orderArn": NotRequired[str],
        "orderedResources": NotRequired[List[OrderedResourceDefinitionTypeDef]],
        "shippingAddress": NotRequired[AddressTypeDef],
        "trackingInformation": NotRequired[List[TrackingInformationTypeDef]],
    },
)
SitePlanOutputTypeDef = TypedDict(
    "SitePlanOutputTypeDef",
    {
        "options": NotRequired[List[NameValuePairTypeDef]],
        "resourceDefinitions": NotRequired[List[NetworkResourceDefinitionOutputTypeDef]],
    },
)
NetworkResourceDefinitionUnionTypeDef = Union[
    NetworkResourceDefinitionTypeDef, NetworkResourceDefinitionOutputTypeDef
]
ConfigureAccessPointResponseTypeDef = TypedDict(
    "ConfigureAccessPointResponseTypeDef",
    {
        "accessPoint": NetworkResourceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetNetworkResourceResponseTypeDef = TypedDict(
    "GetNetworkResourceResponseTypeDef",
    {
        "networkResource": NetworkResourceTypeDef,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListNetworkResourcesResponseTypeDef = TypedDict(
    "ListNetworkResourcesResponseTypeDef",
    {
        "networkResources": List[NetworkResourceTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartNetworkResourceUpdateResponseTypeDef = TypedDict(
    "StartNetworkResourceUpdateResponseTypeDef",
    {
        "networkResource": NetworkResourceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AcknowledgeOrderReceiptResponseTypeDef = TypedDict(
    "AcknowledgeOrderReceiptResponseTypeDef",
    {
        "order": OrderTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetOrderResponseTypeDef = TypedDict(
    "GetOrderResponseTypeDef",
    {
        "order": OrderTypeDef,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListOrdersResponseTypeDef = TypedDict(
    "ListOrdersResponseTypeDef",
    {
        "nextToken": str,
        "orders": List[OrderTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NetworkSiteTypeDef = TypedDict(
    "NetworkSiteTypeDef",
    {
        "networkArn": str,
        "networkSiteArn": str,
        "networkSiteName": str,
        "status": NetworkSiteStatusType,
        "availabilityZone": NotRequired[str],
        "availabilityZoneId": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "currentPlan": NotRequired[SitePlanOutputTypeDef],
        "description": NotRequired[str],
        "pendingPlan": NotRequired[SitePlanOutputTypeDef],
        "statusReason": NotRequired[str],
    },
)
SitePlanTypeDef = TypedDict(
    "SitePlanTypeDef",
    {
        "options": NotRequired[Sequence[NameValuePairTypeDef]],
        "resourceDefinitions": NotRequired[Sequence[NetworkResourceDefinitionUnionTypeDef]],
    },
)
ActivateNetworkSiteResponseTypeDef = TypedDict(
    "ActivateNetworkSiteResponseTypeDef",
    {
        "networkSite": NetworkSiteTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateNetworkSiteResponseTypeDef = TypedDict(
    "CreateNetworkSiteResponseTypeDef",
    {
        "networkSite": NetworkSiteTypeDef,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteNetworkSiteResponseTypeDef = TypedDict(
    "DeleteNetworkSiteResponseTypeDef",
    {
        "networkSite": NetworkSiteTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetNetworkSiteResponseTypeDef = TypedDict(
    "GetNetworkSiteResponseTypeDef",
    {
        "networkSite": NetworkSiteTypeDef,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListNetworkSitesResponseTypeDef = TypedDict(
    "ListNetworkSitesResponseTypeDef",
    {
        "networkSites": List[NetworkSiteTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateNetworkSiteResponseTypeDef = TypedDict(
    "UpdateNetworkSiteResponseTypeDef",
    {
        "networkSite": NetworkSiteTypeDef,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateNetworkSiteRequestRequestTypeDef = TypedDict(
    "CreateNetworkSiteRequestRequestTypeDef",
    {
        "networkArn": str,
        "networkSiteName": str,
        "availabilityZone": NotRequired[str],
        "availabilityZoneId": NotRequired[str],
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "pendingPlan": NotRequired[SitePlanTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
UpdateNetworkSitePlanRequestRequestTypeDef = TypedDict(
    "UpdateNetworkSitePlanRequestRequestTypeDef",
    {
        "networkSiteArn": str,
        "pendingPlan": SitePlanTypeDef,
        "clientToken": NotRequired[str],
    },
)
