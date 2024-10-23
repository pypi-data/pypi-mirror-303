"""
Type annotations for networkmanager service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/type_defs/)

Usage::

    ```python
    from mypy_boto3_networkmanager.type_defs import AWSLocationTypeDef

    data: AWSLocationTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AttachmentErrorCodeType,
    AttachmentStateType,
    AttachmentTypeType,
    ChangeActionType,
    ChangeSetStateType,
    ChangeStatusType,
    ChangeTypeType,
    ConnectionStateType,
    ConnectionStatusType,
    ConnectionTypeType,
    ConnectPeerAssociationStateType,
    ConnectPeerErrorCodeType,
    ConnectPeerStateType,
    CoreNetworkPolicyAliasType,
    CoreNetworkStateType,
    CustomerGatewayAssociationStateType,
    DeviceStateType,
    GlobalNetworkStateType,
    LinkAssociationStateType,
    LinkStateType,
    PeeringErrorCodeType,
    PeeringStateType,
    RouteAnalysisCompletionReasonCodeType,
    RouteAnalysisCompletionResultCodeType,
    RouteAnalysisStatusType,
    RouteStateType,
    RouteTableTypeType,
    RouteTypeType,
    SegmentActionServiceInsertionType,
    SendViaModeType,
    SiteStateType,
    TransitGatewayConnectPeerAssociationStateType,
    TransitGatewayRegistrationStateType,
    TunnelProtocolType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AWSLocationTypeDef",
    "AcceptAttachmentRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "AccountStatusTypeDef",
    "AssociateConnectPeerRequestRequestTypeDef",
    "ConnectPeerAssociationTypeDef",
    "AssociateCustomerGatewayRequestRequestTypeDef",
    "CustomerGatewayAssociationTypeDef",
    "AssociateLinkRequestRequestTypeDef",
    "LinkAssociationTypeDef",
    "AssociateTransitGatewayConnectPeerRequestRequestTypeDef",
    "TransitGatewayConnectPeerAssociationTypeDef",
    "AttachmentErrorTypeDef",
    "TagTypeDef",
    "BandwidthTypeDef",
    "BgpOptionsTypeDef",
    "ConnectAttachmentOptionsTypeDef",
    "ConnectPeerBgpConfigurationTypeDef",
    "ConnectPeerErrorTypeDef",
    "ConnectionHealthTypeDef",
    "CoreNetworkChangeEventValuesTypeDef",
    "CoreNetworkEdgeTypeDef",
    "CoreNetworkNetworkFunctionGroupIdentifierTypeDef",
    "ServiceInsertionSegmentsTypeDef",
    "CoreNetworkPolicyErrorTypeDef",
    "CoreNetworkPolicyVersionTypeDef",
    "CoreNetworkSegmentEdgeIdentifierTypeDef",
    "CoreNetworkSegmentTypeDef",
    "LocationTypeDef",
    "VpcOptionsTypeDef",
    "DeleteAttachmentRequestRequestTypeDef",
    "DeleteConnectPeerRequestRequestTypeDef",
    "DeleteConnectionRequestRequestTypeDef",
    "DeleteCoreNetworkPolicyVersionRequestRequestTypeDef",
    "DeleteCoreNetworkRequestRequestTypeDef",
    "DeleteDeviceRequestRequestTypeDef",
    "DeleteGlobalNetworkRequestRequestTypeDef",
    "DeleteLinkRequestRequestTypeDef",
    "DeletePeeringRequestRequestTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DeleteSiteRequestRequestTypeDef",
    "DeregisterTransitGatewayRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeGlobalNetworksRequestRequestTypeDef",
    "DisassociateConnectPeerRequestRequestTypeDef",
    "DisassociateCustomerGatewayRequestRequestTypeDef",
    "DisassociateLinkRequestRequestTypeDef",
    "DisassociateTransitGatewayConnectPeerRequestRequestTypeDef",
    "EdgeOverrideTypeDef",
    "ExecuteCoreNetworkChangeSetRequestRequestTypeDef",
    "GetConnectAttachmentRequestRequestTypeDef",
    "GetConnectPeerAssociationsRequestRequestTypeDef",
    "GetConnectPeerRequestRequestTypeDef",
    "GetConnectionsRequestRequestTypeDef",
    "GetCoreNetworkChangeEventsRequestRequestTypeDef",
    "GetCoreNetworkChangeSetRequestRequestTypeDef",
    "GetCoreNetworkPolicyRequestRequestTypeDef",
    "GetCoreNetworkRequestRequestTypeDef",
    "GetCustomerGatewayAssociationsRequestRequestTypeDef",
    "GetDevicesRequestRequestTypeDef",
    "GetLinkAssociationsRequestRequestTypeDef",
    "GetLinksRequestRequestTypeDef",
    "GetNetworkResourceCountsRequestRequestTypeDef",
    "NetworkResourceCountTypeDef",
    "GetNetworkResourceRelationshipsRequestRequestTypeDef",
    "RelationshipTypeDef",
    "GetNetworkResourcesRequestRequestTypeDef",
    "GetNetworkTelemetryRequestRequestTypeDef",
    "GetResourcePolicyRequestRequestTypeDef",
    "GetRouteAnalysisRequestRequestTypeDef",
    "GetSiteToSiteVpnAttachmentRequestRequestTypeDef",
    "GetSitesRequestRequestTypeDef",
    "GetTransitGatewayConnectPeerAssociationsRequestRequestTypeDef",
    "GetTransitGatewayPeeringRequestRequestTypeDef",
    "GetTransitGatewayRegistrationsRequestRequestTypeDef",
    "GetTransitGatewayRouteTableAttachmentRequestRequestTypeDef",
    "GetVpcAttachmentRequestRequestTypeDef",
    "ListAttachmentsRequestRequestTypeDef",
    "ListConnectPeersRequestRequestTypeDef",
    "ListCoreNetworkPolicyVersionsRequestRequestTypeDef",
    "ListCoreNetworksRequestRequestTypeDef",
    "ListOrganizationServiceAccessStatusRequestRequestTypeDef",
    "ListPeeringsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "NetworkFunctionGroupTypeDef",
    "NetworkResourceSummaryTypeDef",
    "NetworkRouteDestinationTypeDef",
    "PermissionsErrorContextTypeDef",
    "PutCoreNetworkPolicyRequestRequestTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "RegisterTransitGatewayRequestRequestTypeDef",
    "RejectAttachmentRequestRequestTypeDef",
    "RestoreCoreNetworkPolicyVersionRequestRequestTypeDef",
    "RouteAnalysisCompletionTypeDef",
    "RouteAnalysisEndpointOptionsSpecificationTypeDef",
    "RouteAnalysisEndpointOptionsTypeDef",
    "WhenSentToTypeDef",
    "StartOrganizationServiceAccessUpdateRequestRequestTypeDef",
    "TransitGatewayRegistrationStateReasonTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateConnectionRequestRequestTypeDef",
    "UpdateCoreNetworkRequestRequestTypeDef",
    "UpdateGlobalNetworkRequestRequestTypeDef",
    "UpdateNetworkResourceMetadataRequestRequestTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "UpdateNetworkResourceMetadataResponseTypeDef",
    "OrganizationStatusTypeDef",
    "AssociateConnectPeerResponseTypeDef",
    "DisassociateConnectPeerResponseTypeDef",
    "GetConnectPeerAssociationsResponseTypeDef",
    "AssociateCustomerGatewayResponseTypeDef",
    "DisassociateCustomerGatewayResponseTypeDef",
    "GetCustomerGatewayAssociationsResponseTypeDef",
    "AssociateLinkResponseTypeDef",
    "DisassociateLinkResponseTypeDef",
    "GetLinkAssociationsResponseTypeDef",
    "AssociateTransitGatewayConnectPeerResponseTypeDef",
    "DisassociateTransitGatewayConnectPeerResponseTypeDef",
    "GetTransitGatewayConnectPeerAssociationsResponseTypeDef",
    "ConnectPeerSummaryTypeDef",
    "ConnectionTypeDef",
    "CoreNetworkSummaryTypeDef",
    "CreateConnectionRequestRequestTypeDef",
    "CreateCoreNetworkRequestRequestTypeDef",
    "CreateGlobalNetworkRequestRequestTypeDef",
    "CreateSiteToSiteVpnAttachmentRequestRequestTypeDef",
    "CreateTransitGatewayPeeringRequestRequestTypeDef",
    "CreateTransitGatewayRouteTableAttachmentRequestRequestTypeDef",
    "GlobalNetworkTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NetworkResourceTypeDef",
    "ProposedNetworkFunctionGroupChangeTypeDef",
    "ProposedSegmentChangeTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateLinkRequestRequestTypeDef",
    "LinkTypeDef",
    "UpdateLinkRequestRequestTypeDef",
    "CreateConnectPeerRequestRequestTypeDef",
    "CreateConnectAttachmentRequestRequestTypeDef",
    "ConnectPeerConfigurationTypeDef",
    "NetworkTelemetryTypeDef",
    "CoreNetworkChangeEventTypeDef",
    "CoreNetworkNetworkFunctionGroupTypeDef",
    "CoreNetworkPolicyTypeDef",
    "ListCoreNetworkPolicyVersionsResponseTypeDef",
    "RouteTableIdentifierTypeDef",
    "CreateDeviceRequestRequestTypeDef",
    "CreateSiteRequestRequestTypeDef",
    "DeviceTypeDef",
    "SiteTypeDef",
    "UpdateDeviceRequestRequestTypeDef",
    "UpdateSiteRequestRequestTypeDef",
    "CreateVpcAttachmentRequestRequestTypeDef",
    "UpdateVpcAttachmentRequestRequestTypeDef",
    "DescribeGlobalNetworksRequestDescribeGlobalNetworksPaginateTypeDef",
    "GetConnectPeerAssociationsRequestGetConnectPeerAssociationsPaginateTypeDef",
    "GetConnectionsRequestGetConnectionsPaginateTypeDef",
    "GetCoreNetworkChangeEventsRequestGetCoreNetworkChangeEventsPaginateTypeDef",
    "GetCoreNetworkChangeSetRequestGetCoreNetworkChangeSetPaginateTypeDef",
    "GetCustomerGatewayAssociationsRequestGetCustomerGatewayAssociationsPaginateTypeDef",
    "GetDevicesRequestGetDevicesPaginateTypeDef",
    "GetLinkAssociationsRequestGetLinkAssociationsPaginateTypeDef",
    "GetLinksRequestGetLinksPaginateTypeDef",
    "GetNetworkResourceCountsRequestGetNetworkResourceCountsPaginateTypeDef",
    "GetNetworkResourceRelationshipsRequestGetNetworkResourceRelationshipsPaginateTypeDef",
    "GetNetworkResourcesRequestGetNetworkResourcesPaginateTypeDef",
    "GetNetworkTelemetryRequestGetNetworkTelemetryPaginateTypeDef",
    "GetSitesRequestGetSitesPaginateTypeDef",
    "GetTransitGatewayConnectPeerAssociationsRequestGetTransitGatewayConnectPeerAssociationsPaginateTypeDef",
    "GetTransitGatewayRegistrationsRequestGetTransitGatewayRegistrationsPaginateTypeDef",
    "ListAttachmentsRequestListAttachmentsPaginateTypeDef",
    "ListConnectPeersRequestListConnectPeersPaginateTypeDef",
    "ListCoreNetworkPolicyVersionsRequestListCoreNetworkPolicyVersionsPaginateTypeDef",
    "ListCoreNetworksRequestListCoreNetworksPaginateTypeDef",
    "ListPeeringsRequestListPeeringsPaginateTypeDef",
    "GetNetworkResourceCountsResponseTypeDef",
    "GetNetworkResourceRelationshipsResponseTypeDef",
    "ViaTypeDef",
    "PathComponentTypeDef",
    "NetworkRouteTypeDef",
    "PeeringErrorTypeDef",
    "StartRouteAnalysisRequestRequestTypeDef",
    "TransitGatewayRegistrationTypeDef",
    "ListOrganizationServiceAccessStatusResponseTypeDef",
    "StartOrganizationServiceAccessUpdateResponseTypeDef",
    "ListConnectPeersResponseTypeDef",
    "CreateConnectionResponseTypeDef",
    "DeleteConnectionResponseTypeDef",
    "GetConnectionsResponseTypeDef",
    "UpdateConnectionResponseTypeDef",
    "ListCoreNetworksResponseTypeDef",
    "CreateGlobalNetworkResponseTypeDef",
    "DeleteGlobalNetworkResponseTypeDef",
    "DescribeGlobalNetworksResponseTypeDef",
    "UpdateGlobalNetworkResponseTypeDef",
    "GetNetworkResourcesResponseTypeDef",
    "AttachmentTypeDef",
    "CreateLinkResponseTypeDef",
    "DeleteLinkResponseTypeDef",
    "GetLinksResponseTypeDef",
    "UpdateLinkResponseTypeDef",
    "ConnectPeerTypeDef",
    "GetNetworkTelemetryResponseTypeDef",
    "GetCoreNetworkChangeEventsResponseTypeDef",
    "CoreNetworkTypeDef",
    "DeleteCoreNetworkPolicyVersionResponseTypeDef",
    "GetCoreNetworkPolicyResponseTypeDef",
    "PutCoreNetworkPolicyResponseTypeDef",
    "RestoreCoreNetworkPolicyVersionResponseTypeDef",
    "GetNetworkRoutesRequestRequestTypeDef",
    "CreateDeviceResponseTypeDef",
    "DeleteDeviceResponseTypeDef",
    "GetDevicesResponseTypeDef",
    "UpdateDeviceResponseTypeDef",
    "CreateSiteResponseTypeDef",
    "DeleteSiteResponseTypeDef",
    "GetSitesResponseTypeDef",
    "UpdateSiteResponseTypeDef",
    "ServiceInsertionActionTypeDef",
    "RouteAnalysisPathTypeDef",
    "GetNetworkRoutesResponseTypeDef",
    "PeeringTypeDef",
    "DeregisterTransitGatewayResponseTypeDef",
    "GetTransitGatewayRegistrationsResponseTypeDef",
    "RegisterTransitGatewayResponseTypeDef",
    "AcceptAttachmentResponseTypeDef",
    "ConnectAttachmentTypeDef",
    "DeleteAttachmentResponseTypeDef",
    "ListAttachmentsResponseTypeDef",
    "RejectAttachmentResponseTypeDef",
    "SiteToSiteVpnAttachmentTypeDef",
    "TransitGatewayRouteTableAttachmentTypeDef",
    "VpcAttachmentTypeDef",
    "CreateConnectPeerResponseTypeDef",
    "DeleteConnectPeerResponseTypeDef",
    "GetConnectPeerResponseTypeDef",
    "CreateCoreNetworkResponseTypeDef",
    "DeleteCoreNetworkResponseTypeDef",
    "GetCoreNetworkResponseTypeDef",
    "UpdateCoreNetworkResponseTypeDef",
    "CoreNetworkChangeValuesTypeDef",
    "RouteAnalysisTypeDef",
    "DeletePeeringResponseTypeDef",
    "ListPeeringsResponseTypeDef",
    "TransitGatewayPeeringTypeDef",
    "CreateConnectAttachmentResponseTypeDef",
    "GetConnectAttachmentResponseTypeDef",
    "CreateSiteToSiteVpnAttachmentResponseTypeDef",
    "GetSiteToSiteVpnAttachmentResponseTypeDef",
    "CreateTransitGatewayRouteTableAttachmentResponseTypeDef",
    "GetTransitGatewayRouteTableAttachmentResponseTypeDef",
    "CreateVpcAttachmentResponseTypeDef",
    "GetVpcAttachmentResponseTypeDef",
    "UpdateVpcAttachmentResponseTypeDef",
    "CoreNetworkChangeTypeDef",
    "GetRouteAnalysisResponseTypeDef",
    "StartRouteAnalysisResponseTypeDef",
    "CreateTransitGatewayPeeringResponseTypeDef",
    "GetTransitGatewayPeeringResponseTypeDef",
    "GetCoreNetworkChangeSetResponseTypeDef",
)

AWSLocationTypeDef = TypedDict(
    "AWSLocationTypeDef",
    {
        "Zone": NotRequired[str],
        "SubnetArn": NotRequired[str],
    },
)
AcceptAttachmentRequestRequestTypeDef = TypedDict(
    "AcceptAttachmentRequestRequestTypeDef",
    {
        "AttachmentId": str,
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
AccountStatusTypeDef = TypedDict(
    "AccountStatusTypeDef",
    {
        "AccountId": NotRequired[str],
        "SLRDeploymentStatus": NotRequired[str],
    },
)
AssociateConnectPeerRequestRequestTypeDef = TypedDict(
    "AssociateConnectPeerRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "ConnectPeerId": str,
        "DeviceId": str,
        "LinkId": NotRequired[str],
    },
)
ConnectPeerAssociationTypeDef = TypedDict(
    "ConnectPeerAssociationTypeDef",
    {
        "ConnectPeerId": NotRequired[str],
        "GlobalNetworkId": NotRequired[str],
        "DeviceId": NotRequired[str],
        "LinkId": NotRequired[str],
        "State": NotRequired[ConnectPeerAssociationStateType],
    },
)
AssociateCustomerGatewayRequestRequestTypeDef = TypedDict(
    "AssociateCustomerGatewayRequestRequestTypeDef",
    {
        "CustomerGatewayArn": str,
        "GlobalNetworkId": str,
        "DeviceId": str,
        "LinkId": NotRequired[str],
    },
)
CustomerGatewayAssociationTypeDef = TypedDict(
    "CustomerGatewayAssociationTypeDef",
    {
        "CustomerGatewayArn": NotRequired[str],
        "GlobalNetworkId": NotRequired[str],
        "DeviceId": NotRequired[str],
        "LinkId": NotRequired[str],
        "State": NotRequired[CustomerGatewayAssociationStateType],
    },
)
AssociateLinkRequestRequestTypeDef = TypedDict(
    "AssociateLinkRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceId": str,
        "LinkId": str,
    },
)
LinkAssociationTypeDef = TypedDict(
    "LinkAssociationTypeDef",
    {
        "GlobalNetworkId": NotRequired[str],
        "DeviceId": NotRequired[str],
        "LinkId": NotRequired[str],
        "LinkAssociationState": NotRequired[LinkAssociationStateType],
    },
)
AssociateTransitGatewayConnectPeerRequestRequestTypeDef = TypedDict(
    "AssociateTransitGatewayConnectPeerRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "TransitGatewayConnectPeerArn": str,
        "DeviceId": str,
        "LinkId": NotRequired[str],
    },
)
TransitGatewayConnectPeerAssociationTypeDef = TypedDict(
    "TransitGatewayConnectPeerAssociationTypeDef",
    {
        "TransitGatewayConnectPeerArn": NotRequired[str],
        "GlobalNetworkId": NotRequired[str],
        "DeviceId": NotRequired[str],
        "LinkId": NotRequired[str],
        "State": NotRequired[TransitGatewayConnectPeerAssociationStateType],
    },
)
AttachmentErrorTypeDef = TypedDict(
    "AttachmentErrorTypeDef",
    {
        "Code": NotRequired[AttachmentErrorCodeType],
        "Message": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "RequestId": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
BandwidthTypeDef = TypedDict(
    "BandwidthTypeDef",
    {
        "UploadSpeed": NotRequired[int],
        "DownloadSpeed": NotRequired[int],
    },
)
BgpOptionsTypeDef = TypedDict(
    "BgpOptionsTypeDef",
    {
        "PeerAsn": NotRequired[int],
    },
)
ConnectAttachmentOptionsTypeDef = TypedDict(
    "ConnectAttachmentOptionsTypeDef",
    {
        "Protocol": NotRequired[TunnelProtocolType],
    },
)
ConnectPeerBgpConfigurationTypeDef = TypedDict(
    "ConnectPeerBgpConfigurationTypeDef",
    {
        "CoreNetworkAsn": NotRequired[int],
        "PeerAsn": NotRequired[int],
        "CoreNetworkAddress": NotRequired[str],
        "PeerAddress": NotRequired[str],
    },
)
ConnectPeerErrorTypeDef = TypedDict(
    "ConnectPeerErrorTypeDef",
    {
        "Code": NotRequired[ConnectPeerErrorCodeType],
        "Message": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "RequestId": NotRequired[str],
    },
)
ConnectionHealthTypeDef = TypedDict(
    "ConnectionHealthTypeDef",
    {
        "Type": NotRequired[ConnectionTypeType],
        "Status": NotRequired[ConnectionStatusType],
        "Timestamp": NotRequired[datetime],
    },
)
CoreNetworkChangeEventValuesTypeDef = TypedDict(
    "CoreNetworkChangeEventValuesTypeDef",
    {
        "EdgeLocation": NotRequired[str],
        "SegmentName": NotRequired[str],
        "NetworkFunctionGroupName": NotRequired[str],
        "AttachmentId": NotRequired[str],
        "Cidr": NotRequired[str],
    },
)
CoreNetworkEdgeTypeDef = TypedDict(
    "CoreNetworkEdgeTypeDef",
    {
        "EdgeLocation": NotRequired[str],
        "Asn": NotRequired[int],
        "InsideCidrBlocks": NotRequired[List[str]],
    },
)
CoreNetworkNetworkFunctionGroupIdentifierTypeDef = TypedDict(
    "CoreNetworkNetworkFunctionGroupIdentifierTypeDef",
    {
        "CoreNetworkId": NotRequired[str],
        "NetworkFunctionGroupName": NotRequired[str],
        "EdgeLocation": NotRequired[str],
    },
)
ServiceInsertionSegmentsTypeDef = TypedDict(
    "ServiceInsertionSegmentsTypeDef",
    {
        "SendVia": NotRequired[List[str]],
        "SendTo": NotRequired[List[str]],
    },
)
CoreNetworkPolicyErrorTypeDef = TypedDict(
    "CoreNetworkPolicyErrorTypeDef",
    {
        "ErrorCode": str,
        "Message": str,
        "Path": NotRequired[str],
    },
)
CoreNetworkPolicyVersionTypeDef = TypedDict(
    "CoreNetworkPolicyVersionTypeDef",
    {
        "CoreNetworkId": NotRequired[str],
        "PolicyVersionId": NotRequired[int],
        "Alias": NotRequired[CoreNetworkPolicyAliasType],
        "Description": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "ChangeSetState": NotRequired[ChangeSetStateType],
    },
)
CoreNetworkSegmentEdgeIdentifierTypeDef = TypedDict(
    "CoreNetworkSegmentEdgeIdentifierTypeDef",
    {
        "CoreNetworkId": NotRequired[str],
        "SegmentName": NotRequired[str],
        "EdgeLocation": NotRequired[str],
    },
)
CoreNetworkSegmentTypeDef = TypedDict(
    "CoreNetworkSegmentTypeDef",
    {
        "Name": NotRequired[str],
        "EdgeLocations": NotRequired[List[str]],
        "SharedSegments": NotRequired[List[str]],
    },
)
LocationTypeDef = TypedDict(
    "LocationTypeDef",
    {
        "Address": NotRequired[str],
        "Latitude": NotRequired[str],
        "Longitude": NotRequired[str],
    },
)
VpcOptionsTypeDef = TypedDict(
    "VpcOptionsTypeDef",
    {
        "Ipv6Support": NotRequired[bool],
        "ApplianceModeSupport": NotRequired[bool],
    },
)
DeleteAttachmentRequestRequestTypeDef = TypedDict(
    "DeleteAttachmentRequestRequestTypeDef",
    {
        "AttachmentId": str,
    },
)
DeleteConnectPeerRequestRequestTypeDef = TypedDict(
    "DeleteConnectPeerRequestRequestTypeDef",
    {
        "ConnectPeerId": str,
    },
)
DeleteConnectionRequestRequestTypeDef = TypedDict(
    "DeleteConnectionRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "ConnectionId": str,
    },
)
DeleteCoreNetworkPolicyVersionRequestRequestTypeDef = TypedDict(
    "DeleteCoreNetworkPolicyVersionRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "PolicyVersionId": int,
    },
)
DeleteCoreNetworkRequestRequestTypeDef = TypedDict(
    "DeleteCoreNetworkRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
    },
)
DeleteDeviceRequestRequestTypeDef = TypedDict(
    "DeleteDeviceRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceId": str,
    },
)
DeleteGlobalNetworkRequestRequestTypeDef = TypedDict(
    "DeleteGlobalNetworkRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
    },
)
DeleteLinkRequestRequestTypeDef = TypedDict(
    "DeleteLinkRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "LinkId": str,
    },
)
DeletePeeringRequestRequestTypeDef = TypedDict(
    "DeletePeeringRequestRequestTypeDef",
    {
        "PeeringId": str,
    },
)
DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
DeleteSiteRequestRequestTypeDef = TypedDict(
    "DeleteSiteRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "SiteId": str,
    },
)
DeregisterTransitGatewayRequestRequestTypeDef = TypedDict(
    "DeregisterTransitGatewayRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "TransitGatewayArn": str,
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
DescribeGlobalNetworksRequestRequestTypeDef = TypedDict(
    "DescribeGlobalNetworksRequestRequestTypeDef",
    {
        "GlobalNetworkIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DisassociateConnectPeerRequestRequestTypeDef = TypedDict(
    "DisassociateConnectPeerRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "ConnectPeerId": str,
    },
)
DisassociateCustomerGatewayRequestRequestTypeDef = TypedDict(
    "DisassociateCustomerGatewayRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "CustomerGatewayArn": str,
    },
)
DisassociateLinkRequestRequestTypeDef = TypedDict(
    "DisassociateLinkRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceId": str,
        "LinkId": str,
    },
)
DisassociateTransitGatewayConnectPeerRequestRequestTypeDef = TypedDict(
    "DisassociateTransitGatewayConnectPeerRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "TransitGatewayConnectPeerArn": str,
    },
)
EdgeOverrideTypeDef = TypedDict(
    "EdgeOverrideTypeDef",
    {
        "EdgeSets": NotRequired[List[List[str]]],
        "UseEdge": NotRequired[str],
    },
)
ExecuteCoreNetworkChangeSetRequestRequestTypeDef = TypedDict(
    "ExecuteCoreNetworkChangeSetRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "PolicyVersionId": int,
    },
)
GetConnectAttachmentRequestRequestTypeDef = TypedDict(
    "GetConnectAttachmentRequestRequestTypeDef",
    {
        "AttachmentId": str,
    },
)
GetConnectPeerAssociationsRequestRequestTypeDef = TypedDict(
    "GetConnectPeerAssociationsRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "ConnectPeerIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetConnectPeerRequestRequestTypeDef = TypedDict(
    "GetConnectPeerRequestRequestTypeDef",
    {
        "ConnectPeerId": str,
    },
)
GetConnectionsRequestRequestTypeDef = TypedDict(
    "GetConnectionsRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "ConnectionIds": NotRequired[Sequence[str]],
        "DeviceId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetCoreNetworkChangeEventsRequestRequestTypeDef = TypedDict(
    "GetCoreNetworkChangeEventsRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "PolicyVersionId": int,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetCoreNetworkChangeSetRequestRequestTypeDef = TypedDict(
    "GetCoreNetworkChangeSetRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "PolicyVersionId": int,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetCoreNetworkPolicyRequestRequestTypeDef = TypedDict(
    "GetCoreNetworkPolicyRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "PolicyVersionId": NotRequired[int],
        "Alias": NotRequired[CoreNetworkPolicyAliasType],
    },
)
GetCoreNetworkRequestRequestTypeDef = TypedDict(
    "GetCoreNetworkRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
    },
)
GetCustomerGatewayAssociationsRequestRequestTypeDef = TypedDict(
    "GetCustomerGatewayAssociationsRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "CustomerGatewayArns": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetDevicesRequestRequestTypeDef = TypedDict(
    "GetDevicesRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceIds": NotRequired[Sequence[str]],
        "SiteId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetLinkAssociationsRequestRequestTypeDef = TypedDict(
    "GetLinkAssociationsRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceId": NotRequired[str],
        "LinkId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetLinksRequestRequestTypeDef = TypedDict(
    "GetLinksRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "LinkIds": NotRequired[Sequence[str]],
        "SiteId": NotRequired[str],
        "Type": NotRequired[str],
        "Provider": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetNetworkResourceCountsRequestRequestTypeDef = TypedDict(
    "GetNetworkResourceCountsRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "ResourceType": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
NetworkResourceCountTypeDef = TypedDict(
    "NetworkResourceCountTypeDef",
    {
        "ResourceType": NotRequired[str],
        "Count": NotRequired[int],
    },
)
GetNetworkResourceRelationshipsRequestRequestTypeDef = TypedDict(
    "GetNetworkResourceRelationshipsRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "CoreNetworkId": NotRequired[str],
        "RegisteredGatewayArn": NotRequired[str],
        "AwsRegion": NotRequired[str],
        "AccountId": NotRequired[str],
        "ResourceType": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
RelationshipTypeDef = TypedDict(
    "RelationshipTypeDef",
    {
        "From": NotRequired[str],
        "To": NotRequired[str],
    },
)
GetNetworkResourcesRequestRequestTypeDef = TypedDict(
    "GetNetworkResourcesRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "CoreNetworkId": NotRequired[str],
        "RegisteredGatewayArn": NotRequired[str],
        "AwsRegion": NotRequired[str],
        "AccountId": NotRequired[str],
        "ResourceType": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetNetworkTelemetryRequestRequestTypeDef = TypedDict(
    "GetNetworkTelemetryRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "CoreNetworkId": NotRequired[str],
        "RegisteredGatewayArn": NotRequired[str],
        "AwsRegion": NotRequired[str],
        "AccountId": NotRequired[str],
        "ResourceType": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetResourcePolicyRequestRequestTypeDef = TypedDict(
    "GetResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
GetRouteAnalysisRequestRequestTypeDef = TypedDict(
    "GetRouteAnalysisRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "RouteAnalysisId": str,
    },
)
GetSiteToSiteVpnAttachmentRequestRequestTypeDef = TypedDict(
    "GetSiteToSiteVpnAttachmentRequestRequestTypeDef",
    {
        "AttachmentId": str,
    },
)
GetSitesRequestRequestTypeDef = TypedDict(
    "GetSitesRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "SiteIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetTransitGatewayConnectPeerAssociationsRequestRequestTypeDef = TypedDict(
    "GetTransitGatewayConnectPeerAssociationsRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "TransitGatewayConnectPeerArns": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetTransitGatewayPeeringRequestRequestTypeDef = TypedDict(
    "GetTransitGatewayPeeringRequestRequestTypeDef",
    {
        "PeeringId": str,
    },
)
GetTransitGatewayRegistrationsRequestRequestTypeDef = TypedDict(
    "GetTransitGatewayRegistrationsRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "TransitGatewayArns": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetTransitGatewayRouteTableAttachmentRequestRequestTypeDef = TypedDict(
    "GetTransitGatewayRouteTableAttachmentRequestRequestTypeDef",
    {
        "AttachmentId": str,
    },
)
GetVpcAttachmentRequestRequestTypeDef = TypedDict(
    "GetVpcAttachmentRequestRequestTypeDef",
    {
        "AttachmentId": str,
    },
)
ListAttachmentsRequestRequestTypeDef = TypedDict(
    "ListAttachmentsRequestRequestTypeDef",
    {
        "CoreNetworkId": NotRequired[str],
        "AttachmentType": NotRequired[AttachmentTypeType],
        "EdgeLocation": NotRequired[str],
        "State": NotRequired[AttachmentStateType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListConnectPeersRequestRequestTypeDef = TypedDict(
    "ListConnectPeersRequestRequestTypeDef",
    {
        "CoreNetworkId": NotRequired[str],
        "ConnectAttachmentId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListCoreNetworkPolicyVersionsRequestRequestTypeDef = TypedDict(
    "ListCoreNetworkPolicyVersionsRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListCoreNetworksRequestRequestTypeDef = TypedDict(
    "ListCoreNetworksRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListOrganizationServiceAccessStatusRequestRequestTypeDef = TypedDict(
    "ListOrganizationServiceAccessStatusRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListPeeringsRequestRequestTypeDef = TypedDict(
    "ListPeeringsRequestRequestTypeDef",
    {
        "CoreNetworkId": NotRequired[str],
        "PeeringType": NotRequired[Literal["TRANSIT_GATEWAY"]],
        "EdgeLocation": NotRequired[str],
        "State": NotRequired[PeeringStateType],
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
NetworkFunctionGroupTypeDef = TypedDict(
    "NetworkFunctionGroupTypeDef",
    {
        "Name": NotRequired[str],
    },
)
NetworkResourceSummaryTypeDef = TypedDict(
    "NetworkResourceSummaryTypeDef",
    {
        "RegisteredGatewayArn": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "ResourceType": NotRequired[str],
        "Definition": NotRequired[str],
        "NameTag": NotRequired[str],
        "IsMiddlebox": NotRequired[bool],
    },
)
NetworkRouteDestinationTypeDef = TypedDict(
    "NetworkRouteDestinationTypeDef",
    {
        "CoreNetworkAttachmentId": NotRequired[str],
        "TransitGatewayAttachmentId": NotRequired[str],
        "SegmentName": NotRequired[str],
        "NetworkFunctionGroupName": NotRequired[str],
        "EdgeLocation": NotRequired[str],
        "ResourceType": NotRequired[str],
        "ResourceId": NotRequired[str],
    },
)
PermissionsErrorContextTypeDef = TypedDict(
    "PermissionsErrorContextTypeDef",
    {
        "MissingPermission": NotRequired[str],
    },
)
PutCoreNetworkPolicyRequestRequestTypeDef = TypedDict(
    "PutCoreNetworkPolicyRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "PolicyDocument": str,
        "Description": NotRequired[str],
        "LatestVersionId": NotRequired[int],
        "ClientToken": NotRequired[str],
    },
)
PutResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestRequestTypeDef",
    {
        "PolicyDocument": str,
        "ResourceArn": str,
    },
)
RegisterTransitGatewayRequestRequestTypeDef = TypedDict(
    "RegisterTransitGatewayRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "TransitGatewayArn": str,
    },
)
RejectAttachmentRequestRequestTypeDef = TypedDict(
    "RejectAttachmentRequestRequestTypeDef",
    {
        "AttachmentId": str,
    },
)
RestoreCoreNetworkPolicyVersionRequestRequestTypeDef = TypedDict(
    "RestoreCoreNetworkPolicyVersionRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "PolicyVersionId": int,
    },
)
RouteAnalysisCompletionTypeDef = TypedDict(
    "RouteAnalysisCompletionTypeDef",
    {
        "ResultCode": NotRequired[RouteAnalysisCompletionResultCodeType],
        "ReasonCode": NotRequired[RouteAnalysisCompletionReasonCodeType],
        "ReasonContext": NotRequired[Dict[str, str]],
    },
)
RouteAnalysisEndpointOptionsSpecificationTypeDef = TypedDict(
    "RouteAnalysisEndpointOptionsSpecificationTypeDef",
    {
        "TransitGatewayAttachmentArn": NotRequired[str],
        "IpAddress": NotRequired[str],
    },
)
RouteAnalysisEndpointOptionsTypeDef = TypedDict(
    "RouteAnalysisEndpointOptionsTypeDef",
    {
        "TransitGatewayAttachmentArn": NotRequired[str],
        "TransitGatewayArn": NotRequired[str],
        "IpAddress": NotRequired[str],
    },
)
WhenSentToTypeDef = TypedDict(
    "WhenSentToTypeDef",
    {
        "WhenSentToSegmentsList": NotRequired[List[str]],
    },
)
StartOrganizationServiceAccessUpdateRequestRequestTypeDef = TypedDict(
    "StartOrganizationServiceAccessUpdateRequestRequestTypeDef",
    {
        "Action": str,
    },
)
TransitGatewayRegistrationStateReasonTypeDef = TypedDict(
    "TransitGatewayRegistrationStateReasonTypeDef",
    {
        "Code": NotRequired[TransitGatewayRegistrationStateType],
        "Message": NotRequired[str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateConnectionRequestRequestTypeDef = TypedDict(
    "UpdateConnectionRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "ConnectionId": str,
        "LinkId": NotRequired[str],
        "ConnectedLinkId": NotRequired[str],
        "Description": NotRequired[str],
    },
)
UpdateCoreNetworkRequestRequestTypeDef = TypedDict(
    "UpdateCoreNetworkRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "Description": NotRequired[str],
    },
)
UpdateGlobalNetworkRequestRequestTypeDef = TypedDict(
    "UpdateGlobalNetworkRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "Description": NotRequired[str],
    },
)
UpdateNetworkResourceMetadataRequestRequestTypeDef = TypedDict(
    "UpdateNetworkResourceMetadataRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "ResourceArn": str,
        "Metadata": Mapping[str, str],
    },
)
GetResourcePolicyResponseTypeDef = TypedDict(
    "GetResourcePolicyResponseTypeDef",
    {
        "PolicyDocument": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateNetworkResourceMetadataResponseTypeDef = TypedDict(
    "UpdateNetworkResourceMetadataResponseTypeDef",
    {
        "ResourceArn": str,
        "Metadata": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OrganizationStatusTypeDef = TypedDict(
    "OrganizationStatusTypeDef",
    {
        "OrganizationId": NotRequired[str],
        "OrganizationAwsServiceAccessStatus": NotRequired[str],
        "SLRDeploymentStatus": NotRequired[str],
        "AccountStatusList": NotRequired[List[AccountStatusTypeDef]],
    },
)
AssociateConnectPeerResponseTypeDef = TypedDict(
    "AssociateConnectPeerResponseTypeDef",
    {
        "ConnectPeerAssociation": ConnectPeerAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateConnectPeerResponseTypeDef = TypedDict(
    "DisassociateConnectPeerResponseTypeDef",
    {
        "ConnectPeerAssociation": ConnectPeerAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetConnectPeerAssociationsResponseTypeDef = TypedDict(
    "GetConnectPeerAssociationsResponseTypeDef",
    {
        "ConnectPeerAssociations": List[ConnectPeerAssociationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
AssociateCustomerGatewayResponseTypeDef = TypedDict(
    "AssociateCustomerGatewayResponseTypeDef",
    {
        "CustomerGatewayAssociation": CustomerGatewayAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateCustomerGatewayResponseTypeDef = TypedDict(
    "DisassociateCustomerGatewayResponseTypeDef",
    {
        "CustomerGatewayAssociation": CustomerGatewayAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCustomerGatewayAssociationsResponseTypeDef = TypedDict(
    "GetCustomerGatewayAssociationsResponseTypeDef",
    {
        "CustomerGatewayAssociations": List[CustomerGatewayAssociationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
AssociateLinkResponseTypeDef = TypedDict(
    "AssociateLinkResponseTypeDef",
    {
        "LinkAssociation": LinkAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateLinkResponseTypeDef = TypedDict(
    "DisassociateLinkResponseTypeDef",
    {
        "LinkAssociation": LinkAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLinkAssociationsResponseTypeDef = TypedDict(
    "GetLinkAssociationsResponseTypeDef",
    {
        "LinkAssociations": List[LinkAssociationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
AssociateTransitGatewayConnectPeerResponseTypeDef = TypedDict(
    "AssociateTransitGatewayConnectPeerResponseTypeDef",
    {
        "TransitGatewayConnectPeerAssociation": TransitGatewayConnectPeerAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateTransitGatewayConnectPeerResponseTypeDef = TypedDict(
    "DisassociateTransitGatewayConnectPeerResponseTypeDef",
    {
        "TransitGatewayConnectPeerAssociation": TransitGatewayConnectPeerAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTransitGatewayConnectPeerAssociationsResponseTypeDef = TypedDict(
    "GetTransitGatewayConnectPeerAssociationsResponseTypeDef",
    {
        "TransitGatewayConnectPeerAssociations": List[TransitGatewayConnectPeerAssociationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ConnectPeerSummaryTypeDef = TypedDict(
    "ConnectPeerSummaryTypeDef",
    {
        "CoreNetworkId": NotRequired[str],
        "ConnectAttachmentId": NotRequired[str],
        "ConnectPeerId": NotRequired[str],
        "EdgeLocation": NotRequired[str],
        "ConnectPeerState": NotRequired[ConnectPeerStateType],
        "CreatedAt": NotRequired[datetime],
        "Tags": NotRequired[List[TagTypeDef]],
        "SubnetArn": NotRequired[str],
    },
)
ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "ConnectionId": NotRequired[str],
        "ConnectionArn": NotRequired[str],
        "GlobalNetworkId": NotRequired[str],
        "DeviceId": NotRequired[str],
        "ConnectedDeviceId": NotRequired[str],
        "LinkId": NotRequired[str],
        "ConnectedLinkId": NotRequired[str],
        "Description": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "State": NotRequired[ConnectionStateType],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
CoreNetworkSummaryTypeDef = TypedDict(
    "CoreNetworkSummaryTypeDef",
    {
        "CoreNetworkId": NotRequired[str],
        "CoreNetworkArn": NotRequired[str],
        "GlobalNetworkId": NotRequired[str],
        "OwnerAccountId": NotRequired[str],
        "State": NotRequired[CoreNetworkStateType],
        "Description": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
CreateConnectionRequestRequestTypeDef = TypedDict(
    "CreateConnectionRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceId": str,
        "ConnectedDeviceId": str,
        "LinkId": NotRequired[str],
        "ConnectedLinkId": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateCoreNetworkRequestRequestTypeDef = TypedDict(
    "CreateCoreNetworkRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "PolicyDocument": NotRequired[str],
        "ClientToken": NotRequired[str],
    },
)
CreateGlobalNetworkRequestRequestTypeDef = TypedDict(
    "CreateGlobalNetworkRequestRequestTypeDef",
    {
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateSiteToSiteVpnAttachmentRequestRequestTypeDef = TypedDict(
    "CreateSiteToSiteVpnAttachmentRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "VpnConnectionArn": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ClientToken": NotRequired[str],
    },
)
CreateTransitGatewayPeeringRequestRequestTypeDef = TypedDict(
    "CreateTransitGatewayPeeringRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "TransitGatewayArn": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ClientToken": NotRequired[str],
    },
)
CreateTransitGatewayRouteTableAttachmentRequestRequestTypeDef = TypedDict(
    "CreateTransitGatewayRouteTableAttachmentRequestRequestTypeDef",
    {
        "PeeringId": str,
        "TransitGatewayRouteTableArn": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ClientToken": NotRequired[str],
    },
)
GlobalNetworkTypeDef = TypedDict(
    "GlobalNetworkTypeDef",
    {
        "GlobalNetworkId": NotRequired[str],
        "GlobalNetworkArn": NotRequired[str],
        "Description": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "State": NotRequired[GlobalNetworkStateType],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "TagList": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NetworkResourceTypeDef = TypedDict(
    "NetworkResourceTypeDef",
    {
        "RegisteredGatewayArn": NotRequired[str],
        "CoreNetworkId": NotRequired[str],
        "AwsRegion": NotRequired[str],
        "AccountId": NotRequired[str],
        "ResourceType": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "Definition": NotRequired[str],
        "DefinitionTimestamp": NotRequired[datetime],
        "Tags": NotRequired[List[TagTypeDef]],
        "Metadata": NotRequired[Dict[str, str]],
    },
)
ProposedNetworkFunctionGroupChangeTypeDef = TypedDict(
    "ProposedNetworkFunctionGroupChangeTypeDef",
    {
        "Tags": NotRequired[List[TagTypeDef]],
        "AttachmentPolicyRuleNumber": NotRequired[int],
        "NetworkFunctionGroupName": NotRequired[str],
    },
)
ProposedSegmentChangeTypeDef = TypedDict(
    "ProposedSegmentChangeTypeDef",
    {
        "Tags": NotRequired[List[TagTypeDef]],
        "AttachmentPolicyRuleNumber": NotRequired[int],
        "SegmentName": NotRequired[str],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CreateLinkRequestRequestTypeDef = TypedDict(
    "CreateLinkRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "Bandwidth": BandwidthTypeDef,
        "SiteId": str,
        "Description": NotRequired[str],
        "Type": NotRequired[str],
        "Provider": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
LinkTypeDef = TypedDict(
    "LinkTypeDef",
    {
        "LinkId": NotRequired[str],
        "LinkArn": NotRequired[str],
        "GlobalNetworkId": NotRequired[str],
        "SiteId": NotRequired[str],
        "Description": NotRequired[str],
        "Type": NotRequired[str],
        "Bandwidth": NotRequired[BandwidthTypeDef],
        "Provider": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "State": NotRequired[LinkStateType],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
UpdateLinkRequestRequestTypeDef = TypedDict(
    "UpdateLinkRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "LinkId": str,
        "Description": NotRequired[str],
        "Type": NotRequired[str],
        "Bandwidth": NotRequired[BandwidthTypeDef],
        "Provider": NotRequired[str],
    },
)
CreateConnectPeerRequestRequestTypeDef = TypedDict(
    "CreateConnectPeerRequestRequestTypeDef",
    {
        "ConnectAttachmentId": str,
        "PeerAddress": str,
        "CoreNetworkAddress": NotRequired[str],
        "BgpOptions": NotRequired[BgpOptionsTypeDef],
        "InsideCidrBlocks": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ClientToken": NotRequired[str],
        "SubnetArn": NotRequired[str],
    },
)
CreateConnectAttachmentRequestRequestTypeDef = TypedDict(
    "CreateConnectAttachmentRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "EdgeLocation": str,
        "TransportAttachmentId": str,
        "Options": ConnectAttachmentOptionsTypeDef,
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ClientToken": NotRequired[str],
    },
)
ConnectPeerConfigurationTypeDef = TypedDict(
    "ConnectPeerConfigurationTypeDef",
    {
        "CoreNetworkAddress": NotRequired[str],
        "PeerAddress": NotRequired[str],
        "InsideCidrBlocks": NotRequired[List[str]],
        "Protocol": NotRequired[TunnelProtocolType],
        "BgpConfigurations": NotRequired[List[ConnectPeerBgpConfigurationTypeDef]],
    },
)
NetworkTelemetryTypeDef = TypedDict(
    "NetworkTelemetryTypeDef",
    {
        "RegisteredGatewayArn": NotRequired[str],
        "CoreNetworkId": NotRequired[str],
        "AwsRegion": NotRequired[str],
        "AccountId": NotRequired[str],
        "ResourceType": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "Address": NotRequired[str],
        "Health": NotRequired[ConnectionHealthTypeDef],
    },
)
CoreNetworkChangeEventTypeDef = TypedDict(
    "CoreNetworkChangeEventTypeDef",
    {
        "Type": NotRequired[ChangeTypeType],
        "Action": NotRequired[ChangeActionType],
        "IdentifierPath": NotRequired[str],
        "EventTime": NotRequired[datetime],
        "Status": NotRequired[ChangeStatusType],
        "Values": NotRequired[CoreNetworkChangeEventValuesTypeDef],
    },
)
CoreNetworkNetworkFunctionGroupTypeDef = TypedDict(
    "CoreNetworkNetworkFunctionGroupTypeDef",
    {
        "Name": NotRequired[str],
        "EdgeLocations": NotRequired[List[str]],
        "Segments": NotRequired[ServiceInsertionSegmentsTypeDef],
    },
)
CoreNetworkPolicyTypeDef = TypedDict(
    "CoreNetworkPolicyTypeDef",
    {
        "CoreNetworkId": NotRequired[str],
        "PolicyVersionId": NotRequired[int],
        "Alias": NotRequired[CoreNetworkPolicyAliasType],
        "Description": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "ChangeSetState": NotRequired[ChangeSetStateType],
        "PolicyErrors": NotRequired[List[CoreNetworkPolicyErrorTypeDef]],
        "PolicyDocument": NotRequired[str],
    },
)
ListCoreNetworkPolicyVersionsResponseTypeDef = TypedDict(
    "ListCoreNetworkPolicyVersionsResponseTypeDef",
    {
        "CoreNetworkPolicyVersions": List[CoreNetworkPolicyVersionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
RouteTableIdentifierTypeDef = TypedDict(
    "RouteTableIdentifierTypeDef",
    {
        "TransitGatewayRouteTableArn": NotRequired[str],
        "CoreNetworkSegmentEdge": NotRequired[CoreNetworkSegmentEdgeIdentifierTypeDef],
        "CoreNetworkNetworkFunctionGroup": NotRequired[
            CoreNetworkNetworkFunctionGroupIdentifierTypeDef
        ],
    },
)
CreateDeviceRequestRequestTypeDef = TypedDict(
    "CreateDeviceRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "AWSLocation": NotRequired[AWSLocationTypeDef],
        "Description": NotRequired[str],
        "Type": NotRequired[str],
        "Vendor": NotRequired[str],
        "Model": NotRequired[str],
        "SerialNumber": NotRequired[str],
        "Location": NotRequired[LocationTypeDef],
        "SiteId": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateSiteRequestRequestTypeDef = TypedDict(
    "CreateSiteRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "Description": NotRequired[str],
        "Location": NotRequired[LocationTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "DeviceId": NotRequired[str],
        "DeviceArn": NotRequired[str],
        "GlobalNetworkId": NotRequired[str],
        "AWSLocation": NotRequired[AWSLocationTypeDef],
        "Description": NotRequired[str],
        "Type": NotRequired[str],
        "Vendor": NotRequired[str],
        "Model": NotRequired[str],
        "SerialNumber": NotRequired[str],
        "Location": NotRequired[LocationTypeDef],
        "SiteId": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "State": NotRequired[DeviceStateType],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
SiteTypeDef = TypedDict(
    "SiteTypeDef",
    {
        "SiteId": NotRequired[str],
        "SiteArn": NotRequired[str],
        "GlobalNetworkId": NotRequired[str],
        "Description": NotRequired[str],
        "Location": NotRequired[LocationTypeDef],
        "CreatedAt": NotRequired[datetime],
        "State": NotRequired[SiteStateType],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
UpdateDeviceRequestRequestTypeDef = TypedDict(
    "UpdateDeviceRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceId": str,
        "AWSLocation": NotRequired[AWSLocationTypeDef],
        "Description": NotRequired[str],
        "Type": NotRequired[str],
        "Vendor": NotRequired[str],
        "Model": NotRequired[str],
        "SerialNumber": NotRequired[str],
        "Location": NotRequired[LocationTypeDef],
        "SiteId": NotRequired[str],
    },
)
UpdateSiteRequestRequestTypeDef = TypedDict(
    "UpdateSiteRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "SiteId": str,
        "Description": NotRequired[str],
        "Location": NotRequired[LocationTypeDef],
    },
)
CreateVpcAttachmentRequestRequestTypeDef = TypedDict(
    "CreateVpcAttachmentRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "VpcArn": str,
        "SubnetArns": Sequence[str],
        "Options": NotRequired[VpcOptionsTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ClientToken": NotRequired[str],
    },
)
UpdateVpcAttachmentRequestRequestTypeDef = TypedDict(
    "UpdateVpcAttachmentRequestRequestTypeDef",
    {
        "AttachmentId": str,
        "AddSubnetArns": NotRequired[Sequence[str]],
        "RemoveSubnetArns": NotRequired[Sequence[str]],
        "Options": NotRequired[VpcOptionsTypeDef],
    },
)
DescribeGlobalNetworksRequestDescribeGlobalNetworksPaginateTypeDef = TypedDict(
    "DescribeGlobalNetworksRequestDescribeGlobalNetworksPaginateTypeDef",
    {
        "GlobalNetworkIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetConnectPeerAssociationsRequestGetConnectPeerAssociationsPaginateTypeDef = TypedDict(
    "GetConnectPeerAssociationsRequestGetConnectPeerAssociationsPaginateTypeDef",
    {
        "GlobalNetworkId": str,
        "ConnectPeerIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetConnectionsRequestGetConnectionsPaginateTypeDef = TypedDict(
    "GetConnectionsRequestGetConnectionsPaginateTypeDef",
    {
        "GlobalNetworkId": str,
        "ConnectionIds": NotRequired[Sequence[str]],
        "DeviceId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetCoreNetworkChangeEventsRequestGetCoreNetworkChangeEventsPaginateTypeDef = TypedDict(
    "GetCoreNetworkChangeEventsRequestGetCoreNetworkChangeEventsPaginateTypeDef",
    {
        "CoreNetworkId": str,
        "PolicyVersionId": int,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetCoreNetworkChangeSetRequestGetCoreNetworkChangeSetPaginateTypeDef = TypedDict(
    "GetCoreNetworkChangeSetRequestGetCoreNetworkChangeSetPaginateTypeDef",
    {
        "CoreNetworkId": str,
        "PolicyVersionId": int,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetCustomerGatewayAssociationsRequestGetCustomerGatewayAssociationsPaginateTypeDef = TypedDict(
    "GetCustomerGatewayAssociationsRequestGetCustomerGatewayAssociationsPaginateTypeDef",
    {
        "GlobalNetworkId": str,
        "CustomerGatewayArns": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetDevicesRequestGetDevicesPaginateTypeDef = TypedDict(
    "GetDevicesRequestGetDevicesPaginateTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceIds": NotRequired[Sequence[str]],
        "SiteId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetLinkAssociationsRequestGetLinkAssociationsPaginateTypeDef = TypedDict(
    "GetLinkAssociationsRequestGetLinkAssociationsPaginateTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceId": NotRequired[str],
        "LinkId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetLinksRequestGetLinksPaginateTypeDef = TypedDict(
    "GetLinksRequestGetLinksPaginateTypeDef",
    {
        "GlobalNetworkId": str,
        "LinkIds": NotRequired[Sequence[str]],
        "SiteId": NotRequired[str],
        "Type": NotRequired[str],
        "Provider": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetNetworkResourceCountsRequestGetNetworkResourceCountsPaginateTypeDef = TypedDict(
    "GetNetworkResourceCountsRequestGetNetworkResourceCountsPaginateTypeDef",
    {
        "GlobalNetworkId": str,
        "ResourceType": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetNetworkResourceRelationshipsRequestGetNetworkResourceRelationshipsPaginateTypeDef = TypedDict(
    "GetNetworkResourceRelationshipsRequestGetNetworkResourceRelationshipsPaginateTypeDef",
    {
        "GlobalNetworkId": str,
        "CoreNetworkId": NotRequired[str],
        "RegisteredGatewayArn": NotRequired[str],
        "AwsRegion": NotRequired[str],
        "AccountId": NotRequired[str],
        "ResourceType": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetNetworkResourcesRequestGetNetworkResourcesPaginateTypeDef = TypedDict(
    "GetNetworkResourcesRequestGetNetworkResourcesPaginateTypeDef",
    {
        "GlobalNetworkId": str,
        "CoreNetworkId": NotRequired[str],
        "RegisteredGatewayArn": NotRequired[str],
        "AwsRegion": NotRequired[str],
        "AccountId": NotRequired[str],
        "ResourceType": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetNetworkTelemetryRequestGetNetworkTelemetryPaginateTypeDef = TypedDict(
    "GetNetworkTelemetryRequestGetNetworkTelemetryPaginateTypeDef",
    {
        "GlobalNetworkId": str,
        "CoreNetworkId": NotRequired[str],
        "RegisteredGatewayArn": NotRequired[str],
        "AwsRegion": NotRequired[str],
        "AccountId": NotRequired[str],
        "ResourceType": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetSitesRequestGetSitesPaginateTypeDef = TypedDict(
    "GetSitesRequestGetSitesPaginateTypeDef",
    {
        "GlobalNetworkId": str,
        "SiteIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetTransitGatewayConnectPeerAssociationsRequestGetTransitGatewayConnectPeerAssociationsPaginateTypeDef = TypedDict(
    "GetTransitGatewayConnectPeerAssociationsRequestGetTransitGatewayConnectPeerAssociationsPaginateTypeDef",
    {
        "GlobalNetworkId": str,
        "TransitGatewayConnectPeerArns": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetTransitGatewayRegistrationsRequestGetTransitGatewayRegistrationsPaginateTypeDef = TypedDict(
    "GetTransitGatewayRegistrationsRequestGetTransitGatewayRegistrationsPaginateTypeDef",
    {
        "GlobalNetworkId": str,
        "TransitGatewayArns": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAttachmentsRequestListAttachmentsPaginateTypeDef = TypedDict(
    "ListAttachmentsRequestListAttachmentsPaginateTypeDef",
    {
        "CoreNetworkId": NotRequired[str],
        "AttachmentType": NotRequired[AttachmentTypeType],
        "EdgeLocation": NotRequired[str],
        "State": NotRequired[AttachmentStateType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListConnectPeersRequestListConnectPeersPaginateTypeDef = TypedDict(
    "ListConnectPeersRequestListConnectPeersPaginateTypeDef",
    {
        "CoreNetworkId": NotRequired[str],
        "ConnectAttachmentId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCoreNetworkPolicyVersionsRequestListCoreNetworkPolicyVersionsPaginateTypeDef = TypedDict(
    "ListCoreNetworkPolicyVersionsRequestListCoreNetworkPolicyVersionsPaginateTypeDef",
    {
        "CoreNetworkId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCoreNetworksRequestListCoreNetworksPaginateTypeDef = TypedDict(
    "ListCoreNetworksRequestListCoreNetworksPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPeeringsRequestListPeeringsPaginateTypeDef = TypedDict(
    "ListPeeringsRequestListPeeringsPaginateTypeDef",
    {
        "CoreNetworkId": NotRequired[str],
        "PeeringType": NotRequired[Literal["TRANSIT_GATEWAY"]],
        "EdgeLocation": NotRequired[str],
        "State": NotRequired[PeeringStateType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetNetworkResourceCountsResponseTypeDef = TypedDict(
    "GetNetworkResourceCountsResponseTypeDef",
    {
        "NetworkResourceCounts": List[NetworkResourceCountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetNetworkResourceRelationshipsResponseTypeDef = TypedDict(
    "GetNetworkResourceRelationshipsResponseTypeDef",
    {
        "Relationships": List[RelationshipTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ViaTypeDef = TypedDict(
    "ViaTypeDef",
    {
        "NetworkFunctionGroups": NotRequired[List[NetworkFunctionGroupTypeDef]],
        "WithEdgeOverrides": NotRequired[List[EdgeOverrideTypeDef]],
    },
)
PathComponentTypeDef = TypedDict(
    "PathComponentTypeDef",
    {
        "Sequence": NotRequired[int],
        "Resource": NotRequired[NetworkResourceSummaryTypeDef],
        "DestinationCidrBlock": NotRequired[str],
    },
)
NetworkRouteTypeDef = TypedDict(
    "NetworkRouteTypeDef",
    {
        "DestinationCidrBlock": NotRequired[str],
        "Destinations": NotRequired[List[NetworkRouteDestinationTypeDef]],
        "PrefixListId": NotRequired[str],
        "State": NotRequired[RouteStateType],
        "Type": NotRequired[RouteTypeType],
    },
)
PeeringErrorTypeDef = TypedDict(
    "PeeringErrorTypeDef",
    {
        "Code": NotRequired[PeeringErrorCodeType],
        "Message": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "RequestId": NotRequired[str],
        "MissingPermissionsContext": NotRequired[PermissionsErrorContextTypeDef],
    },
)
StartRouteAnalysisRequestRequestTypeDef = TypedDict(
    "StartRouteAnalysisRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "Source": RouteAnalysisEndpointOptionsSpecificationTypeDef,
        "Destination": RouteAnalysisEndpointOptionsSpecificationTypeDef,
        "IncludeReturnPath": NotRequired[bool],
        "UseMiddleboxes": NotRequired[bool],
    },
)
TransitGatewayRegistrationTypeDef = TypedDict(
    "TransitGatewayRegistrationTypeDef",
    {
        "GlobalNetworkId": NotRequired[str],
        "TransitGatewayArn": NotRequired[str],
        "State": NotRequired[TransitGatewayRegistrationStateReasonTypeDef],
    },
)
ListOrganizationServiceAccessStatusResponseTypeDef = TypedDict(
    "ListOrganizationServiceAccessStatusResponseTypeDef",
    {
        "OrganizationStatus": OrganizationStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
StartOrganizationServiceAccessUpdateResponseTypeDef = TypedDict(
    "StartOrganizationServiceAccessUpdateResponseTypeDef",
    {
        "OrganizationStatus": OrganizationStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListConnectPeersResponseTypeDef = TypedDict(
    "ListConnectPeersResponseTypeDef",
    {
        "ConnectPeers": List[ConnectPeerSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateConnectionResponseTypeDef = TypedDict(
    "CreateConnectionResponseTypeDef",
    {
        "Connection": ConnectionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteConnectionResponseTypeDef = TypedDict(
    "DeleteConnectionResponseTypeDef",
    {
        "Connection": ConnectionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetConnectionsResponseTypeDef = TypedDict(
    "GetConnectionsResponseTypeDef",
    {
        "Connections": List[ConnectionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateConnectionResponseTypeDef = TypedDict(
    "UpdateConnectionResponseTypeDef",
    {
        "Connection": ConnectionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCoreNetworksResponseTypeDef = TypedDict(
    "ListCoreNetworksResponseTypeDef",
    {
        "CoreNetworks": List[CoreNetworkSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateGlobalNetworkResponseTypeDef = TypedDict(
    "CreateGlobalNetworkResponseTypeDef",
    {
        "GlobalNetwork": GlobalNetworkTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteGlobalNetworkResponseTypeDef = TypedDict(
    "DeleteGlobalNetworkResponseTypeDef",
    {
        "GlobalNetwork": GlobalNetworkTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeGlobalNetworksResponseTypeDef = TypedDict(
    "DescribeGlobalNetworksResponseTypeDef",
    {
        "GlobalNetworks": List[GlobalNetworkTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateGlobalNetworkResponseTypeDef = TypedDict(
    "UpdateGlobalNetworkResponseTypeDef",
    {
        "GlobalNetwork": GlobalNetworkTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetNetworkResourcesResponseTypeDef = TypedDict(
    "GetNetworkResourcesResponseTypeDef",
    {
        "NetworkResources": List[NetworkResourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
AttachmentTypeDef = TypedDict(
    "AttachmentTypeDef",
    {
        "CoreNetworkId": NotRequired[str],
        "CoreNetworkArn": NotRequired[str],
        "AttachmentId": NotRequired[str],
        "OwnerAccountId": NotRequired[str],
        "AttachmentType": NotRequired[AttachmentTypeType],
        "State": NotRequired[AttachmentStateType],
        "EdgeLocation": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "AttachmentPolicyRuleNumber": NotRequired[int],
        "SegmentName": NotRequired[str],
        "NetworkFunctionGroupName": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "ProposedSegmentChange": NotRequired[ProposedSegmentChangeTypeDef],
        "ProposedNetworkFunctionGroupChange": NotRequired[
            ProposedNetworkFunctionGroupChangeTypeDef
        ],
        "CreatedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
        "LastModificationErrors": NotRequired[List[AttachmentErrorTypeDef]],
    },
)
CreateLinkResponseTypeDef = TypedDict(
    "CreateLinkResponseTypeDef",
    {
        "Link": LinkTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteLinkResponseTypeDef = TypedDict(
    "DeleteLinkResponseTypeDef",
    {
        "Link": LinkTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLinksResponseTypeDef = TypedDict(
    "GetLinksResponseTypeDef",
    {
        "Links": List[LinkTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateLinkResponseTypeDef = TypedDict(
    "UpdateLinkResponseTypeDef",
    {
        "Link": LinkTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConnectPeerTypeDef = TypedDict(
    "ConnectPeerTypeDef",
    {
        "CoreNetworkId": NotRequired[str],
        "ConnectAttachmentId": NotRequired[str],
        "ConnectPeerId": NotRequired[str],
        "EdgeLocation": NotRequired[str],
        "State": NotRequired[ConnectPeerStateType],
        "CreatedAt": NotRequired[datetime],
        "Configuration": NotRequired[ConnectPeerConfigurationTypeDef],
        "Tags": NotRequired[List[TagTypeDef]],
        "SubnetArn": NotRequired[str],
        "LastModificationErrors": NotRequired[List[ConnectPeerErrorTypeDef]],
    },
)
GetNetworkTelemetryResponseTypeDef = TypedDict(
    "GetNetworkTelemetryResponseTypeDef",
    {
        "NetworkTelemetry": List[NetworkTelemetryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetCoreNetworkChangeEventsResponseTypeDef = TypedDict(
    "GetCoreNetworkChangeEventsResponseTypeDef",
    {
        "CoreNetworkChangeEvents": List[CoreNetworkChangeEventTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CoreNetworkTypeDef = TypedDict(
    "CoreNetworkTypeDef",
    {
        "GlobalNetworkId": NotRequired[str],
        "CoreNetworkId": NotRequired[str],
        "CoreNetworkArn": NotRequired[str],
        "Description": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "State": NotRequired[CoreNetworkStateType],
        "Segments": NotRequired[List[CoreNetworkSegmentTypeDef]],
        "NetworkFunctionGroups": NotRequired[List[CoreNetworkNetworkFunctionGroupTypeDef]],
        "Edges": NotRequired[List[CoreNetworkEdgeTypeDef]],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
DeleteCoreNetworkPolicyVersionResponseTypeDef = TypedDict(
    "DeleteCoreNetworkPolicyVersionResponseTypeDef",
    {
        "CoreNetworkPolicy": CoreNetworkPolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCoreNetworkPolicyResponseTypeDef = TypedDict(
    "GetCoreNetworkPolicyResponseTypeDef",
    {
        "CoreNetworkPolicy": CoreNetworkPolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutCoreNetworkPolicyResponseTypeDef = TypedDict(
    "PutCoreNetworkPolicyResponseTypeDef",
    {
        "CoreNetworkPolicy": CoreNetworkPolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreCoreNetworkPolicyVersionResponseTypeDef = TypedDict(
    "RestoreCoreNetworkPolicyVersionResponseTypeDef",
    {
        "CoreNetworkPolicy": CoreNetworkPolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetNetworkRoutesRequestRequestTypeDef = TypedDict(
    "GetNetworkRoutesRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "RouteTableIdentifier": RouteTableIdentifierTypeDef,
        "ExactCidrMatches": NotRequired[Sequence[str]],
        "LongestPrefixMatches": NotRequired[Sequence[str]],
        "SubnetOfMatches": NotRequired[Sequence[str]],
        "SupernetOfMatches": NotRequired[Sequence[str]],
        "PrefixListIds": NotRequired[Sequence[str]],
        "States": NotRequired[Sequence[RouteStateType]],
        "Types": NotRequired[Sequence[RouteTypeType]],
        "DestinationFilters": NotRequired[Mapping[str, Sequence[str]]],
    },
)
CreateDeviceResponseTypeDef = TypedDict(
    "CreateDeviceResponseTypeDef",
    {
        "Device": DeviceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDeviceResponseTypeDef = TypedDict(
    "DeleteDeviceResponseTypeDef",
    {
        "Device": DeviceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDevicesResponseTypeDef = TypedDict(
    "GetDevicesResponseTypeDef",
    {
        "Devices": List[DeviceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateDeviceResponseTypeDef = TypedDict(
    "UpdateDeviceResponseTypeDef",
    {
        "Device": DeviceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSiteResponseTypeDef = TypedDict(
    "CreateSiteResponseTypeDef",
    {
        "Site": SiteTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteSiteResponseTypeDef = TypedDict(
    "DeleteSiteResponseTypeDef",
    {
        "Site": SiteTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSitesResponseTypeDef = TypedDict(
    "GetSitesResponseTypeDef",
    {
        "Sites": List[SiteTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateSiteResponseTypeDef = TypedDict(
    "UpdateSiteResponseTypeDef",
    {
        "Site": SiteTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ServiceInsertionActionTypeDef = TypedDict(
    "ServiceInsertionActionTypeDef",
    {
        "Action": NotRequired[SegmentActionServiceInsertionType],
        "Mode": NotRequired[SendViaModeType],
        "WhenSentTo": NotRequired[WhenSentToTypeDef],
        "Via": NotRequired[ViaTypeDef],
    },
)
RouteAnalysisPathTypeDef = TypedDict(
    "RouteAnalysisPathTypeDef",
    {
        "CompletionStatus": NotRequired[RouteAnalysisCompletionTypeDef],
        "Path": NotRequired[List[PathComponentTypeDef]],
    },
)
GetNetworkRoutesResponseTypeDef = TypedDict(
    "GetNetworkRoutesResponseTypeDef",
    {
        "RouteTableArn": str,
        "CoreNetworkSegmentEdge": CoreNetworkSegmentEdgeIdentifierTypeDef,
        "RouteTableType": RouteTableTypeType,
        "RouteTableTimestamp": datetime,
        "NetworkRoutes": List[NetworkRouteTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PeeringTypeDef = TypedDict(
    "PeeringTypeDef",
    {
        "CoreNetworkId": NotRequired[str],
        "CoreNetworkArn": NotRequired[str],
        "PeeringId": NotRequired[str],
        "OwnerAccountId": NotRequired[str],
        "PeeringType": NotRequired[Literal["TRANSIT_GATEWAY"]],
        "State": NotRequired[PeeringStateType],
        "EdgeLocation": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "CreatedAt": NotRequired[datetime],
        "LastModificationErrors": NotRequired[List[PeeringErrorTypeDef]],
    },
)
DeregisterTransitGatewayResponseTypeDef = TypedDict(
    "DeregisterTransitGatewayResponseTypeDef",
    {
        "TransitGatewayRegistration": TransitGatewayRegistrationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTransitGatewayRegistrationsResponseTypeDef = TypedDict(
    "GetTransitGatewayRegistrationsResponseTypeDef",
    {
        "TransitGatewayRegistrations": List[TransitGatewayRegistrationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
RegisterTransitGatewayResponseTypeDef = TypedDict(
    "RegisterTransitGatewayResponseTypeDef",
    {
        "TransitGatewayRegistration": TransitGatewayRegistrationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AcceptAttachmentResponseTypeDef = TypedDict(
    "AcceptAttachmentResponseTypeDef",
    {
        "Attachment": AttachmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConnectAttachmentTypeDef = TypedDict(
    "ConnectAttachmentTypeDef",
    {
        "Attachment": NotRequired[AttachmentTypeDef],
        "TransportAttachmentId": NotRequired[str],
        "Options": NotRequired[ConnectAttachmentOptionsTypeDef],
    },
)
DeleteAttachmentResponseTypeDef = TypedDict(
    "DeleteAttachmentResponseTypeDef",
    {
        "Attachment": AttachmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAttachmentsResponseTypeDef = TypedDict(
    "ListAttachmentsResponseTypeDef",
    {
        "Attachments": List[AttachmentTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
RejectAttachmentResponseTypeDef = TypedDict(
    "RejectAttachmentResponseTypeDef",
    {
        "Attachment": AttachmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SiteToSiteVpnAttachmentTypeDef = TypedDict(
    "SiteToSiteVpnAttachmentTypeDef",
    {
        "Attachment": NotRequired[AttachmentTypeDef],
        "VpnConnectionArn": NotRequired[str],
    },
)
TransitGatewayRouteTableAttachmentTypeDef = TypedDict(
    "TransitGatewayRouteTableAttachmentTypeDef",
    {
        "Attachment": NotRequired[AttachmentTypeDef],
        "PeeringId": NotRequired[str],
        "TransitGatewayRouteTableArn": NotRequired[str],
    },
)
VpcAttachmentTypeDef = TypedDict(
    "VpcAttachmentTypeDef",
    {
        "Attachment": NotRequired[AttachmentTypeDef],
        "SubnetArns": NotRequired[List[str]],
        "Options": NotRequired[VpcOptionsTypeDef],
    },
)
CreateConnectPeerResponseTypeDef = TypedDict(
    "CreateConnectPeerResponseTypeDef",
    {
        "ConnectPeer": ConnectPeerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteConnectPeerResponseTypeDef = TypedDict(
    "DeleteConnectPeerResponseTypeDef",
    {
        "ConnectPeer": ConnectPeerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetConnectPeerResponseTypeDef = TypedDict(
    "GetConnectPeerResponseTypeDef",
    {
        "ConnectPeer": ConnectPeerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCoreNetworkResponseTypeDef = TypedDict(
    "CreateCoreNetworkResponseTypeDef",
    {
        "CoreNetwork": CoreNetworkTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteCoreNetworkResponseTypeDef = TypedDict(
    "DeleteCoreNetworkResponseTypeDef",
    {
        "CoreNetwork": CoreNetworkTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCoreNetworkResponseTypeDef = TypedDict(
    "GetCoreNetworkResponseTypeDef",
    {
        "CoreNetwork": CoreNetworkTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateCoreNetworkResponseTypeDef = TypedDict(
    "UpdateCoreNetworkResponseTypeDef",
    {
        "CoreNetwork": CoreNetworkTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CoreNetworkChangeValuesTypeDef = TypedDict(
    "CoreNetworkChangeValuesTypeDef",
    {
        "SegmentName": NotRequired[str],
        "NetworkFunctionGroupName": NotRequired[str],
        "EdgeLocations": NotRequired[List[str]],
        "Asn": NotRequired[int],
        "Cidr": NotRequired[str],
        "DestinationIdentifier": NotRequired[str],
        "InsideCidrBlocks": NotRequired[List[str]],
        "SharedSegments": NotRequired[List[str]],
        "ServiceInsertionActions": NotRequired[List[ServiceInsertionActionTypeDef]],
    },
)
RouteAnalysisTypeDef = TypedDict(
    "RouteAnalysisTypeDef",
    {
        "GlobalNetworkId": NotRequired[str],
        "OwnerAccountId": NotRequired[str],
        "RouteAnalysisId": NotRequired[str],
        "StartTimestamp": NotRequired[datetime],
        "Status": NotRequired[RouteAnalysisStatusType],
        "Source": NotRequired[RouteAnalysisEndpointOptionsTypeDef],
        "Destination": NotRequired[RouteAnalysisEndpointOptionsTypeDef],
        "IncludeReturnPath": NotRequired[bool],
        "UseMiddleboxes": NotRequired[bool],
        "ForwardPath": NotRequired[RouteAnalysisPathTypeDef],
        "ReturnPath": NotRequired[RouteAnalysisPathTypeDef],
    },
)
DeletePeeringResponseTypeDef = TypedDict(
    "DeletePeeringResponseTypeDef",
    {
        "Peering": PeeringTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPeeringsResponseTypeDef = TypedDict(
    "ListPeeringsResponseTypeDef",
    {
        "Peerings": List[PeeringTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
TransitGatewayPeeringTypeDef = TypedDict(
    "TransitGatewayPeeringTypeDef",
    {
        "Peering": NotRequired[PeeringTypeDef],
        "TransitGatewayArn": NotRequired[str],
        "TransitGatewayPeeringAttachmentId": NotRequired[str],
    },
)
CreateConnectAttachmentResponseTypeDef = TypedDict(
    "CreateConnectAttachmentResponseTypeDef",
    {
        "ConnectAttachment": ConnectAttachmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetConnectAttachmentResponseTypeDef = TypedDict(
    "GetConnectAttachmentResponseTypeDef",
    {
        "ConnectAttachment": ConnectAttachmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSiteToSiteVpnAttachmentResponseTypeDef = TypedDict(
    "CreateSiteToSiteVpnAttachmentResponseTypeDef",
    {
        "SiteToSiteVpnAttachment": SiteToSiteVpnAttachmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSiteToSiteVpnAttachmentResponseTypeDef = TypedDict(
    "GetSiteToSiteVpnAttachmentResponseTypeDef",
    {
        "SiteToSiteVpnAttachment": SiteToSiteVpnAttachmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTransitGatewayRouteTableAttachmentResponseTypeDef = TypedDict(
    "CreateTransitGatewayRouteTableAttachmentResponseTypeDef",
    {
        "TransitGatewayRouteTableAttachment": TransitGatewayRouteTableAttachmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTransitGatewayRouteTableAttachmentResponseTypeDef = TypedDict(
    "GetTransitGatewayRouteTableAttachmentResponseTypeDef",
    {
        "TransitGatewayRouteTableAttachment": TransitGatewayRouteTableAttachmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateVpcAttachmentResponseTypeDef = TypedDict(
    "CreateVpcAttachmentResponseTypeDef",
    {
        "VpcAttachment": VpcAttachmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetVpcAttachmentResponseTypeDef = TypedDict(
    "GetVpcAttachmentResponseTypeDef",
    {
        "VpcAttachment": VpcAttachmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateVpcAttachmentResponseTypeDef = TypedDict(
    "UpdateVpcAttachmentResponseTypeDef",
    {
        "VpcAttachment": VpcAttachmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CoreNetworkChangeTypeDef = TypedDict(
    "CoreNetworkChangeTypeDef",
    {
        "Type": NotRequired[ChangeTypeType],
        "Action": NotRequired[ChangeActionType],
        "Identifier": NotRequired[str],
        "PreviousValues": NotRequired[CoreNetworkChangeValuesTypeDef],
        "NewValues": NotRequired[CoreNetworkChangeValuesTypeDef],
        "IdentifierPath": NotRequired[str],
    },
)
GetRouteAnalysisResponseTypeDef = TypedDict(
    "GetRouteAnalysisResponseTypeDef",
    {
        "RouteAnalysis": RouteAnalysisTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartRouteAnalysisResponseTypeDef = TypedDict(
    "StartRouteAnalysisResponseTypeDef",
    {
        "RouteAnalysis": RouteAnalysisTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTransitGatewayPeeringResponseTypeDef = TypedDict(
    "CreateTransitGatewayPeeringResponseTypeDef",
    {
        "TransitGatewayPeering": TransitGatewayPeeringTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTransitGatewayPeeringResponseTypeDef = TypedDict(
    "GetTransitGatewayPeeringResponseTypeDef",
    {
        "TransitGatewayPeering": TransitGatewayPeeringTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCoreNetworkChangeSetResponseTypeDef = TypedDict(
    "GetCoreNetworkChangeSetResponseTypeDef",
    {
        "CoreNetworkChanges": List[CoreNetworkChangeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
