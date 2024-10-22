"""
Type annotations for directconnect service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_directconnect/type_defs/)

Usage::

    ```python
    from mypy_boto3_directconnect.type_defs import RouteFilterPrefixTypeDef

    data: RouteFilterPrefixTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import (
    AddressFamilyType,
    BGPPeerStateType,
    BGPStatusType,
    ConnectionStateType,
    DirectConnectGatewayAssociationProposalStateType,
    DirectConnectGatewayAssociationStateType,
    DirectConnectGatewayAttachmentStateType,
    DirectConnectGatewayAttachmentTypeType,
    DirectConnectGatewayStateType,
    GatewayTypeType,
    HasLogicalRedundancyType,
    InterconnectStateType,
    LagStateType,
    NniPartnerTypeType,
    VirtualInterfaceStateType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "RouteFilterPrefixTypeDef",
    "ResponseMetadataTypeDef",
    "AllocateConnectionOnInterconnectRequestRequestTypeDef",
    "TagTypeDef",
    "AssociateConnectionWithLagRequestRequestTypeDef",
    "AssociateHostedConnectionRequestRequestTypeDef",
    "AssociateMacSecKeyRequestRequestTypeDef",
    "MacSecKeyTypeDef",
    "AssociateVirtualInterfaceRequestRequestTypeDef",
    "AssociatedGatewayTypeDef",
    "BGPPeerTypeDef",
    "ConfirmConnectionRequestRequestTypeDef",
    "ConfirmCustomerAgreementRequestRequestTypeDef",
    "ConfirmPrivateVirtualInterfaceRequestRequestTypeDef",
    "ConfirmPublicVirtualInterfaceRequestRequestTypeDef",
    "ConfirmTransitVirtualInterfaceRequestRequestTypeDef",
    "NewBGPPeerTypeDef",
    "CreateDirectConnectGatewayRequestRequestTypeDef",
    "DirectConnectGatewayTypeDef",
    "CustomerAgreementTypeDef",
    "DeleteBGPPeerRequestRequestTypeDef",
    "DeleteConnectionRequestRequestTypeDef",
    "DeleteDirectConnectGatewayAssociationProposalRequestRequestTypeDef",
    "DeleteDirectConnectGatewayAssociationRequestRequestTypeDef",
    "DeleteDirectConnectGatewayRequestRequestTypeDef",
    "DeleteInterconnectRequestRequestTypeDef",
    "DeleteLagRequestRequestTypeDef",
    "DeleteVirtualInterfaceRequestRequestTypeDef",
    "DescribeConnectionLoaRequestRequestTypeDef",
    "LoaTypeDef",
    "DescribeConnectionsOnInterconnectRequestRequestTypeDef",
    "DescribeConnectionsRequestRequestTypeDef",
    "DescribeDirectConnectGatewayAssociationProposalsRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeDirectConnectGatewayAssociationsRequestRequestTypeDef",
    "DescribeDirectConnectGatewayAttachmentsRequestRequestTypeDef",
    "DirectConnectGatewayAttachmentTypeDef",
    "DescribeDirectConnectGatewaysRequestRequestTypeDef",
    "DescribeHostedConnectionsRequestRequestTypeDef",
    "DescribeInterconnectLoaRequestRequestTypeDef",
    "DescribeInterconnectsRequestRequestTypeDef",
    "DescribeLagsRequestRequestTypeDef",
    "DescribeLoaRequestRequestTypeDef",
    "DescribeRouterConfigurationRequestRequestTypeDef",
    "RouterTypeTypeDef",
    "DescribeTagsRequestRequestTypeDef",
    "DescribeVirtualInterfacesRequestRequestTypeDef",
    "DisassociateConnectionFromLagRequestRequestTypeDef",
    "DisassociateMacSecKeyRequestRequestTypeDef",
    "ListVirtualInterfaceTestHistoryRequestRequestTypeDef",
    "VirtualInterfaceTestHistoryTypeDef",
    "LocationTypeDef",
    "StartBgpFailoverTestRequestRequestTypeDef",
    "StopBgpFailoverTestRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateConnectionRequestRequestTypeDef",
    "UpdateDirectConnectGatewayRequestRequestTypeDef",
    "UpdateLagRequestRequestTypeDef",
    "UpdateVirtualInterfaceAttributesRequestRequestTypeDef",
    "VirtualGatewayTypeDef",
    "AcceptDirectConnectGatewayAssociationProposalRequestRequestTypeDef",
    "CreateDirectConnectGatewayAssociationProposalRequestRequestTypeDef",
    "CreateDirectConnectGatewayAssociationRequestRequestTypeDef",
    "UpdateDirectConnectGatewayAssociationRequestRequestTypeDef",
    "ConfirmConnectionResponseTypeDef",
    "ConfirmCustomerAgreementResponseTypeDef",
    "ConfirmPrivateVirtualInterfaceResponseTypeDef",
    "ConfirmPublicVirtualInterfaceResponseTypeDef",
    "ConfirmTransitVirtualInterfaceResponseTypeDef",
    "DeleteInterconnectResponseTypeDef",
    "DeleteVirtualInterfaceResponseTypeDef",
    "LoaResponseTypeDef",
    "AllocateHostedConnectionRequestRequestTypeDef",
    "CreateConnectionRequestRequestTypeDef",
    "CreateInterconnectRequestRequestTypeDef",
    "CreateLagRequestRequestTypeDef",
    "InterconnectResponseTypeDef",
    "InterconnectTypeDef",
    "NewPrivateVirtualInterfaceAllocationTypeDef",
    "NewPrivateVirtualInterfaceTypeDef",
    "NewPublicVirtualInterfaceAllocationTypeDef",
    "NewPublicVirtualInterfaceTypeDef",
    "NewTransitVirtualInterfaceAllocationTypeDef",
    "NewTransitVirtualInterfaceTypeDef",
    "ResourceTagTypeDef",
    "TagResourceRequestRequestTypeDef",
    "AssociateMacSecKeyResponseTypeDef",
    "ConnectionResponseTypeDef",
    "ConnectionTypeDef",
    "DisassociateMacSecKeyResponseTypeDef",
    "DirectConnectGatewayAssociationProposalTypeDef",
    "DirectConnectGatewayAssociationTypeDef",
    "VirtualInterfaceResponseTypeDef",
    "VirtualInterfaceTypeDef",
    "CreateBGPPeerRequestRequestTypeDef",
    "CreateDirectConnectGatewayResultTypeDef",
    "DeleteDirectConnectGatewayResultTypeDef",
    "DescribeDirectConnectGatewaysResultTypeDef",
    "UpdateDirectConnectGatewayResponseTypeDef",
    "DescribeCustomerMetadataResponseTypeDef",
    "DescribeConnectionLoaResponseTypeDef",
    "DescribeInterconnectLoaResponseTypeDef",
    "DescribeDirectConnectGatewayAssociationsRequestDescribeDirectConnectGatewayAssociationsPaginateTypeDef",
    "DescribeDirectConnectGatewayAttachmentsRequestDescribeDirectConnectGatewayAttachmentsPaginateTypeDef",
    "DescribeDirectConnectGatewaysRequestDescribeDirectConnectGatewaysPaginateTypeDef",
    "DescribeDirectConnectGatewayAttachmentsResultTypeDef",
    "DescribeRouterConfigurationResponseTypeDef",
    "ListVirtualInterfaceTestHistoryResponseTypeDef",
    "StartBgpFailoverTestResponseTypeDef",
    "StopBgpFailoverTestResponseTypeDef",
    "LocationsTypeDef",
    "VirtualGatewaysTypeDef",
    "InterconnectsTypeDef",
    "AllocatePrivateVirtualInterfaceRequestRequestTypeDef",
    "CreatePrivateVirtualInterfaceRequestRequestTypeDef",
    "AllocatePublicVirtualInterfaceRequestRequestTypeDef",
    "CreatePublicVirtualInterfaceRequestRequestTypeDef",
    "AllocateTransitVirtualInterfaceRequestRequestTypeDef",
    "CreateTransitVirtualInterfaceRequestRequestTypeDef",
    "DescribeTagsResponseTypeDef",
    "ConnectionsTypeDef",
    "LagResponseTypeDef",
    "LagTypeDef",
    "CreateDirectConnectGatewayAssociationProposalResultTypeDef",
    "DeleteDirectConnectGatewayAssociationProposalResultTypeDef",
    "DescribeDirectConnectGatewayAssociationProposalsResultTypeDef",
    "AcceptDirectConnectGatewayAssociationProposalResultTypeDef",
    "CreateDirectConnectGatewayAssociationResultTypeDef",
    "DeleteDirectConnectGatewayAssociationResultTypeDef",
    "DescribeDirectConnectGatewayAssociationsResultTypeDef",
    "UpdateDirectConnectGatewayAssociationResultTypeDef",
    "AllocateTransitVirtualInterfaceResultTypeDef",
    "CreateBGPPeerResponseTypeDef",
    "CreateTransitVirtualInterfaceResultTypeDef",
    "DeleteBGPPeerResponseTypeDef",
    "VirtualInterfacesTypeDef",
    "LagsTypeDef",
)

RouteFilterPrefixTypeDef = TypedDict(
    "RouteFilterPrefixTypeDef",
    {
        "cidr": NotRequired[str],
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
AllocateConnectionOnInterconnectRequestRequestTypeDef = TypedDict(
    "AllocateConnectionOnInterconnectRequestRequestTypeDef",
    {
        "bandwidth": str,
        "connectionName": str,
        "ownerAccount": str,
        "interconnectId": str,
        "vlan": int,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": NotRequired[str],
    },
)
AssociateConnectionWithLagRequestRequestTypeDef = TypedDict(
    "AssociateConnectionWithLagRequestRequestTypeDef",
    {
        "connectionId": str,
        "lagId": str,
    },
)
AssociateHostedConnectionRequestRequestTypeDef = TypedDict(
    "AssociateHostedConnectionRequestRequestTypeDef",
    {
        "connectionId": str,
        "parentConnectionId": str,
    },
)
AssociateMacSecKeyRequestRequestTypeDef = TypedDict(
    "AssociateMacSecKeyRequestRequestTypeDef",
    {
        "connectionId": str,
        "secretARN": NotRequired[str],
        "ckn": NotRequired[str],
        "cak": NotRequired[str],
    },
)
MacSecKeyTypeDef = TypedDict(
    "MacSecKeyTypeDef",
    {
        "secretARN": NotRequired[str],
        "ckn": NotRequired[str],
        "state": NotRequired[str],
        "startOn": NotRequired[str],
    },
)
AssociateVirtualInterfaceRequestRequestTypeDef = TypedDict(
    "AssociateVirtualInterfaceRequestRequestTypeDef",
    {
        "virtualInterfaceId": str,
        "connectionId": str,
    },
)
AssociatedGatewayTypeDef = TypedDict(
    "AssociatedGatewayTypeDef",
    {
        "id": NotRequired[str],
        "type": NotRequired[GatewayTypeType],
        "ownerAccount": NotRequired[str],
        "region": NotRequired[str],
    },
)
BGPPeerTypeDef = TypedDict(
    "BGPPeerTypeDef",
    {
        "bgpPeerId": NotRequired[str],
        "asn": NotRequired[int],
        "authKey": NotRequired[str],
        "addressFamily": NotRequired[AddressFamilyType],
        "amazonAddress": NotRequired[str],
        "customerAddress": NotRequired[str],
        "bgpPeerState": NotRequired[BGPPeerStateType],
        "bgpStatus": NotRequired[BGPStatusType],
        "awsDeviceV2": NotRequired[str],
        "awsLogicalDeviceId": NotRequired[str],
    },
)
ConfirmConnectionRequestRequestTypeDef = TypedDict(
    "ConfirmConnectionRequestRequestTypeDef",
    {
        "connectionId": str,
    },
)
ConfirmCustomerAgreementRequestRequestTypeDef = TypedDict(
    "ConfirmCustomerAgreementRequestRequestTypeDef",
    {
        "agreementName": NotRequired[str],
    },
)
ConfirmPrivateVirtualInterfaceRequestRequestTypeDef = TypedDict(
    "ConfirmPrivateVirtualInterfaceRequestRequestTypeDef",
    {
        "virtualInterfaceId": str,
        "virtualGatewayId": NotRequired[str],
        "directConnectGatewayId": NotRequired[str],
    },
)
ConfirmPublicVirtualInterfaceRequestRequestTypeDef = TypedDict(
    "ConfirmPublicVirtualInterfaceRequestRequestTypeDef",
    {
        "virtualInterfaceId": str,
    },
)
ConfirmTransitVirtualInterfaceRequestRequestTypeDef = TypedDict(
    "ConfirmTransitVirtualInterfaceRequestRequestTypeDef",
    {
        "virtualInterfaceId": str,
        "directConnectGatewayId": str,
    },
)
NewBGPPeerTypeDef = TypedDict(
    "NewBGPPeerTypeDef",
    {
        "asn": NotRequired[int],
        "authKey": NotRequired[str],
        "addressFamily": NotRequired[AddressFamilyType],
        "amazonAddress": NotRequired[str],
        "customerAddress": NotRequired[str],
    },
)
CreateDirectConnectGatewayRequestRequestTypeDef = TypedDict(
    "CreateDirectConnectGatewayRequestRequestTypeDef",
    {
        "directConnectGatewayName": str,
        "amazonSideAsn": NotRequired[int],
    },
)
DirectConnectGatewayTypeDef = TypedDict(
    "DirectConnectGatewayTypeDef",
    {
        "directConnectGatewayId": NotRequired[str],
        "directConnectGatewayName": NotRequired[str],
        "amazonSideAsn": NotRequired[int],
        "ownerAccount": NotRequired[str],
        "directConnectGatewayState": NotRequired[DirectConnectGatewayStateType],
        "stateChangeError": NotRequired[str],
    },
)
CustomerAgreementTypeDef = TypedDict(
    "CustomerAgreementTypeDef",
    {
        "agreementName": NotRequired[str],
        "status": NotRequired[str],
    },
)
DeleteBGPPeerRequestRequestTypeDef = TypedDict(
    "DeleteBGPPeerRequestRequestTypeDef",
    {
        "virtualInterfaceId": NotRequired[str],
        "asn": NotRequired[int],
        "customerAddress": NotRequired[str],
        "bgpPeerId": NotRequired[str],
    },
)
DeleteConnectionRequestRequestTypeDef = TypedDict(
    "DeleteConnectionRequestRequestTypeDef",
    {
        "connectionId": str,
    },
)
DeleteDirectConnectGatewayAssociationProposalRequestRequestTypeDef = TypedDict(
    "DeleteDirectConnectGatewayAssociationProposalRequestRequestTypeDef",
    {
        "proposalId": str,
    },
)
DeleteDirectConnectGatewayAssociationRequestRequestTypeDef = TypedDict(
    "DeleteDirectConnectGatewayAssociationRequestRequestTypeDef",
    {
        "associationId": NotRequired[str],
        "directConnectGatewayId": NotRequired[str],
        "virtualGatewayId": NotRequired[str],
    },
)
DeleteDirectConnectGatewayRequestRequestTypeDef = TypedDict(
    "DeleteDirectConnectGatewayRequestRequestTypeDef",
    {
        "directConnectGatewayId": str,
    },
)
DeleteInterconnectRequestRequestTypeDef = TypedDict(
    "DeleteInterconnectRequestRequestTypeDef",
    {
        "interconnectId": str,
    },
)
DeleteLagRequestRequestTypeDef = TypedDict(
    "DeleteLagRequestRequestTypeDef",
    {
        "lagId": str,
    },
)
DeleteVirtualInterfaceRequestRequestTypeDef = TypedDict(
    "DeleteVirtualInterfaceRequestRequestTypeDef",
    {
        "virtualInterfaceId": str,
    },
)
DescribeConnectionLoaRequestRequestTypeDef = TypedDict(
    "DescribeConnectionLoaRequestRequestTypeDef",
    {
        "connectionId": str,
        "providerName": NotRequired[str],
        "loaContentType": NotRequired[Literal["application/pdf"]],
    },
)
LoaTypeDef = TypedDict(
    "LoaTypeDef",
    {
        "loaContent": NotRequired[bytes],
        "loaContentType": NotRequired[Literal["application/pdf"]],
    },
)
DescribeConnectionsOnInterconnectRequestRequestTypeDef = TypedDict(
    "DescribeConnectionsOnInterconnectRequestRequestTypeDef",
    {
        "interconnectId": str,
    },
)
DescribeConnectionsRequestRequestTypeDef = TypedDict(
    "DescribeConnectionsRequestRequestTypeDef",
    {
        "connectionId": NotRequired[str],
    },
)
DescribeDirectConnectGatewayAssociationProposalsRequestRequestTypeDef = TypedDict(
    "DescribeDirectConnectGatewayAssociationProposalsRequestRequestTypeDef",
    {
        "directConnectGatewayId": NotRequired[str],
        "proposalId": NotRequired[str],
        "associatedGatewayId": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
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
DescribeDirectConnectGatewayAssociationsRequestRequestTypeDef = TypedDict(
    "DescribeDirectConnectGatewayAssociationsRequestRequestTypeDef",
    {
        "associationId": NotRequired[str],
        "associatedGatewayId": NotRequired[str],
        "directConnectGatewayId": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "virtualGatewayId": NotRequired[str],
    },
)
DescribeDirectConnectGatewayAttachmentsRequestRequestTypeDef = TypedDict(
    "DescribeDirectConnectGatewayAttachmentsRequestRequestTypeDef",
    {
        "directConnectGatewayId": NotRequired[str],
        "virtualInterfaceId": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
DirectConnectGatewayAttachmentTypeDef = TypedDict(
    "DirectConnectGatewayAttachmentTypeDef",
    {
        "directConnectGatewayId": NotRequired[str],
        "virtualInterfaceId": NotRequired[str],
        "virtualInterfaceRegion": NotRequired[str],
        "virtualInterfaceOwnerAccount": NotRequired[str],
        "attachmentState": NotRequired[DirectConnectGatewayAttachmentStateType],
        "attachmentType": NotRequired[DirectConnectGatewayAttachmentTypeType],
        "stateChangeError": NotRequired[str],
    },
)
DescribeDirectConnectGatewaysRequestRequestTypeDef = TypedDict(
    "DescribeDirectConnectGatewaysRequestRequestTypeDef",
    {
        "directConnectGatewayId": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
DescribeHostedConnectionsRequestRequestTypeDef = TypedDict(
    "DescribeHostedConnectionsRequestRequestTypeDef",
    {
        "connectionId": str,
    },
)
DescribeInterconnectLoaRequestRequestTypeDef = TypedDict(
    "DescribeInterconnectLoaRequestRequestTypeDef",
    {
        "interconnectId": str,
        "providerName": NotRequired[str],
        "loaContentType": NotRequired[Literal["application/pdf"]],
    },
)
DescribeInterconnectsRequestRequestTypeDef = TypedDict(
    "DescribeInterconnectsRequestRequestTypeDef",
    {
        "interconnectId": NotRequired[str],
    },
)
DescribeLagsRequestRequestTypeDef = TypedDict(
    "DescribeLagsRequestRequestTypeDef",
    {
        "lagId": NotRequired[str],
    },
)
DescribeLoaRequestRequestTypeDef = TypedDict(
    "DescribeLoaRequestRequestTypeDef",
    {
        "connectionId": str,
        "providerName": NotRequired[str],
        "loaContentType": NotRequired[Literal["application/pdf"]],
    },
)
DescribeRouterConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeRouterConfigurationRequestRequestTypeDef",
    {
        "virtualInterfaceId": str,
        "routerTypeIdentifier": NotRequired[str],
    },
)
RouterTypeTypeDef = TypedDict(
    "RouterTypeTypeDef",
    {
        "vendor": NotRequired[str],
        "platform": NotRequired[str],
        "software": NotRequired[str],
        "xsltTemplateName": NotRequired[str],
        "xsltTemplateNameForMacSec": NotRequired[str],
        "routerTypeIdentifier": NotRequired[str],
    },
)
DescribeTagsRequestRequestTypeDef = TypedDict(
    "DescribeTagsRequestRequestTypeDef",
    {
        "resourceArns": Sequence[str],
    },
)
DescribeVirtualInterfacesRequestRequestTypeDef = TypedDict(
    "DescribeVirtualInterfacesRequestRequestTypeDef",
    {
        "connectionId": NotRequired[str],
        "virtualInterfaceId": NotRequired[str],
    },
)
DisassociateConnectionFromLagRequestRequestTypeDef = TypedDict(
    "DisassociateConnectionFromLagRequestRequestTypeDef",
    {
        "connectionId": str,
        "lagId": str,
    },
)
DisassociateMacSecKeyRequestRequestTypeDef = TypedDict(
    "DisassociateMacSecKeyRequestRequestTypeDef",
    {
        "connectionId": str,
        "secretARN": str,
    },
)
ListVirtualInterfaceTestHistoryRequestRequestTypeDef = TypedDict(
    "ListVirtualInterfaceTestHistoryRequestRequestTypeDef",
    {
        "testId": NotRequired[str],
        "virtualInterfaceId": NotRequired[str],
        "bgpPeers": NotRequired[Sequence[str]],
        "status": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
VirtualInterfaceTestHistoryTypeDef = TypedDict(
    "VirtualInterfaceTestHistoryTypeDef",
    {
        "testId": NotRequired[str],
        "virtualInterfaceId": NotRequired[str],
        "bgpPeers": NotRequired[List[str]],
        "status": NotRequired[str],
        "ownerAccount": NotRequired[str],
        "testDurationInMinutes": NotRequired[int],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
    },
)
LocationTypeDef = TypedDict(
    "LocationTypeDef",
    {
        "locationCode": NotRequired[str],
        "locationName": NotRequired[str],
        "region": NotRequired[str],
        "availablePortSpeeds": NotRequired[List[str]],
        "availableProviders": NotRequired[List[str]],
        "availableMacSecPortSpeeds": NotRequired[List[str]],
    },
)
StartBgpFailoverTestRequestRequestTypeDef = TypedDict(
    "StartBgpFailoverTestRequestRequestTypeDef",
    {
        "virtualInterfaceId": str,
        "bgpPeers": NotRequired[Sequence[str]],
        "testDurationInMinutes": NotRequired[int],
    },
)
StopBgpFailoverTestRequestRequestTypeDef = TypedDict(
    "StopBgpFailoverTestRequestRequestTypeDef",
    {
        "virtualInterfaceId": str,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UpdateConnectionRequestRequestTypeDef = TypedDict(
    "UpdateConnectionRequestRequestTypeDef",
    {
        "connectionId": str,
        "connectionName": NotRequired[str],
        "encryptionMode": NotRequired[str],
    },
)
UpdateDirectConnectGatewayRequestRequestTypeDef = TypedDict(
    "UpdateDirectConnectGatewayRequestRequestTypeDef",
    {
        "directConnectGatewayId": str,
        "newDirectConnectGatewayName": str,
    },
)
UpdateLagRequestRequestTypeDef = TypedDict(
    "UpdateLagRequestRequestTypeDef",
    {
        "lagId": str,
        "lagName": NotRequired[str],
        "minimumLinks": NotRequired[int],
        "encryptionMode": NotRequired[str],
    },
)
UpdateVirtualInterfaceAttributesRequestRequestTypeDef = TypedDict(
    "UpdateVirtualInterfaceAttributesRequestRequestTypeDef",
    {
        "virtualInterfaceId": str,
        "mtu": NotRequired[int],
        "enableSiteLink": NotRequired[bool],
        "virtualInterfaceName": NotRequired[str],
    },
)
VirtualGatewayTypeDef = TypedDict(
    "VirtualGatewayTypeDef",
    {
        "virtualGatewayId": NotRequired[str],
        "virtualGatewayState": NotRequired[str],
    },
)
AcceptDirectConnectGatewayAssociationProposalRequestRequestTypeDef = TypedDict(
    "AcceptDirectConnectGatewayAssociationProposalRequestRequestTypeDef",
    {
        "directConnectGatewayId": str,
        "proposalId": str,
        "associatedGatewayOwnerAccount": str,
        "overrideAllowedPrefixesToDirectConnectGateway": NotRequired[
            Sequence[RouteFilterPrefixTypeDef]
        ],
    },
)
CreateDirectConnectGatewayAssociationProposalRequestRequestTypeDef = TypedDict(
    "CreateDirectConnectGatewayAssociationProposalRequestRequestTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "gatewayId": str,
        "addAllowedPrefixesToDirectConnectGateway": NotRequired[Sequence[RouteFilterPrefixTypeDef]],
        "removeAllowedPrefixesToDirectConnectGateway": NotRequired[
            Sequence[RouteFilterPrefixTypeDef]
        ],
    },
)
CreateDirectConnectGatewayAssociationRequestRequestTypeDef = TypedDict(
    "CreateDirectConnectGatewayAssociationRequestRequestTypeDef",
    {
        "directConnectGatewayId": str,
        "gatewayId": NotRequired[str],
        "addAllowedPrefixesToDirectConnectGateway": NotRequired[Sequence[RouteFilterPrefixTypeDef]],
        "virtualGatewayId": NotRequired[str],
    },
)
UpdateDirectConnectGatewayAssociationRequestRequestTypeDef = TypedDict(
    "UpdateDirectConnectGatewayAssociationRequestRequestTypeDef",
    {
        "associationId": NotRequired[str],
        "addAllowedPrefixesToDirectConnectGateway": NotRequired[Sequence[RouteFilterPrefixTypeDef]],
        "removeAllowedPrefixesToDirectConnectGateway": NotRequired[
            Sequence[RouteFilterPrefixTypeDef]
        ],
    },
)
ConfirmConnectionResponseTypeDef = TypedDict(
    "ConfirmConnectionResponseTypeDef",
    {
        "connectionState": ConnectionStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConfirmCustomerAgreementResponseTypeDef = TypedDict(
    "ConfirmCustomerAgreementResponseTypeDef",
    {
        "status": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConfirmPrivateVirtualInterfaceResponseTypeDef = TypedDict(
    "ConfirmPrivateVirtualInterfaceResponseTypeDef",
    {
        "virtualInterfaceState": VirtualInterfaceStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConfirmPublicVirtualInterfaceResponseTypeDef = TypedDict(
    "ConfirmPublicVirtualInterfaceResponseTypeDef",
    {
        "virtualInterfaceState": VirtualInterfaceStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConfirmTransitVirtualInterfaceResponseTypeDef = TypedDict(
    "ConfirmTransitVirtualInterfaceResponseTypeDef",
    {
        "virtualInterfaceState": VirtualInterfaceStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteInterconnectResponseTypeDef = TypedDict(
    "DeleteInterconnectResponseTypeDef",
    {
        "interconnectState": InterconnectStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteVirtualInterfaceResponseTypeDef = TypedDict(
    "DeleteVirtualInterfaceResponseTypeDef",
    {
        "virtualInterfaceState": VirtualInterfaceStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LoaResponseTypeDef = TypedDict(
    "LoaResponseTypeDef",
    {
        "loaContent": bytes,
        "loaContentType": Literal["application/pdf"],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AllocateHostedConnectionRequestRequestTypeDef = TypedDict(
    "AllocateHostedConnectionRequestRequestTypeDef",
    {
        "connectionId": str,
        "ownerAccount": str,
        "bandwidth": str,
        "connectionName": str,
        "vlan": int,
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateConnectionRequestRequestTypeDef = TypedDict(
    "CreateConnectionRequestRequestTypeDef",
    {
        "location": str,
        "bandwidth": str,
        "connectionName": str,
        "lagId": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "providerName": NotRequired[str],
        "requestMACSec": NotRequired[bool],
    },
)
CreateInterconnectRequestRequestTypeDef = TypedDict(
    "CreateInterconnectRequestRequestTypeDef",
    {
        "interconnectName": str,
        "bandwidth": str,
        "location": str,
        "lagId": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "providerName": NotRequired[str],
    },
)
CreateLagRequestRequestTypeDef = TypedDict(
    "CreateLagRequestRequestTypeDef",
    {
        "numberOfConnections": int,
        "location": str,
        "connectionsBandwidth": str,
        "lagName": str,
        "connectionId": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "childConnectionTags": NotRequired[Sequence[TagTypeDef]],
        "providerName": NotRequired[str],
        "requestMACSec": NotRequired[bool],
    },
)
InterconnectResponseTypeDef = TypedDict(
    "InterconnectResponseTypeDef",
    {
        "interconnectId": str,
        "interconnectName": str,
        "interconnectState": InterconnectStateType,
        "region": str,
        "location": str,
        "bandwidth": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "awsLogicalDeviceId": str,
        "hasLogicalRedundancy": HasLogicalRedundancyType,
        "tags": List[TagTypeDef],
        "providerName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InterconnectTypeDef = TypedDict(
    "InterconnectTypeDef",
    {
        "interconnectId": NotRequired[str],
        "interconnectName": NotRequired[str],
        "interconnectState": NotRequired[InterconnectStateType],
        "region": NotRequired[str],
        "location": NotRequired[str],
        "bandwidth": NotRequired[str],
        "loaIssueTime": NotRequired[datetime],
        "lagId": NotRequired[str],
        "awsDevice": NotRequired[str],
        "jumboFrameCapable": NotRequired[bool],
        "awsDeviceV2": NotRequired[str],
        "awsLogicalDeviceId": NotRequired[str],
        "hasLogicalRedundancy": NotRequired[HasLogicalRedundancyType],
        "tags": NotRequired[List[TagTypeDef]],
        "providerName": NotRequired[str],
    },
)
NewPrivateVirtualInterfaceAllocationTypeDef = TypedDict(
    "NewPrivateVirtualInterfaceAllocationTypeDef",
    {
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "mtu": NotRequired[int],
        "authKey": NotRequired[str],
        "amazonAddress": NotRequired[str],
        "addressFamily": NotRequired[AddressFamilyType],
        "customerAddress": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
NewPrivateVirtualInterfaceTypeDef = TypedDict(
    "NewPrivateVirtualInterfaceTypeDef",
    {
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "mtu": NotRequired[int],
        "authKey": NotRequired[str],
        "amazonAddress": NotRequired[str],
        "customerAddress": NotRequired[str],
        "addressFamily": NotRequired[AddressFamilyType],
        "virtualGatewayId": NotRequired[str],
        "directConnectGatewayId": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "enableSiteLink": NotRequired[bool],
    },
)
NewPublicVirtualInterfaceAllocationTypeDef = TypedDict(
    "NewPublicVirtualInterfaceAllocationTypeDef",
    {
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "authKey": NotRequired[str],
        "amazonAddress": NotRequired[str],
        "customerAddress": NotRequired[str],
        "addressFamily": NotRequired[AddressFamilyType],
        "routeFilterPrefixes": NotRequired[Sequence[RouteFilterPrefixTypeDef]],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
NewPublicVirtualInterfaceTypeDef = TypedDict(
    "NewPublicVirtualInterfaceTypeDef",
    {
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "authKey": NotRequired[str],
        "amazonAddress": NotRequired[str],
        "customerAddress": NotRequired[str],
        "addressFamily": NotRequired[AddressFamilyType],
        "routeFilterPrefixes": NotRequired[Sequence[RouteFilterPrefixTypeDef]],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
NewTransitVirtualInterfaceAllocationTypeDef = TypedDict(
    "NewTransitVirtualInterfaceAllocationTypeDef",
    {
        "virtualInterfaceName": NotRequired[str],
        "vlan": NotRequired[int],
        "asn": NotRequired[int],
        "mtu": NotRequired[int],
        "authKey": NotRequired[str],
        "amazonAddress": NotRequired[str],
        "customerAddress": NotRequired[str],
        "addressFamily": NotRequired[AddressFamilyType],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
NewTransitVirtualInterfaceTypeDef = TypedDict(
    "NewTransitVirtualInterfaceTypeDef",
    {
        "virtualInterfaceName": NotRequired[str],
        "vlan": NotRequired[int],
        "asn": NotRequired[int],
        "mtu": NotRequired[int],
        "authKey": NotRequired[str],
        "amazonAddress": NotRequired[str],
        "customerAddress": NotRequired[str],
        "addressFamily": NotRequired[AddressFamilyType],
        "directConnectGatewayId": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "enableSiteLink": NotRequired[bool],
    },
)
ResourceTagTypeDef = TypedDict(
    "ResourceTagTypeDef",
    {
        "resourceArn": NotRequired[str],
        "tags": NotRequired[List[TagTypeDef]],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[TagTypeDef],
    },
)
AssociateMacSecKeyResponseTypeDef = TypedDict(
    "AssociateMacSecKeyResponseTypeDef",
    {
        "connectionId": str,
        "macSecKeys": List[MacSecKeyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConnectionResponseTypeDef = TypedDict(
    "ConnectionResponseTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": ConnectionStateType,
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "awsLogicalDeviceId": str,
        "hasLogicalRedundancy": HasLogicalRedundancyType,
        "tags": List[TagTypeDef],
        "providerName": str,
        "macSecCapable": bool,
        "portEncryptionStatus": str,
        "encryptionMode": str,
        "macSecKeys": List[MacSecKeyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "ownerAccount": NotRequired[str],
        "connectionId": NotRequired[str],
        "connectionName": NotRequired[str],
        "connectionState": NotRequired[ConnectionStateType],
        "region": NotRequired[str],
        "location": NotRequired[str],
        "bandwidth": NotRequired[str],
        "vlan": NotRequired[int],
        "partnerName": NotRequired[str],
        "loaIssueTime": NotRequired[datetime],
        "lagId": NotRequired[str],
        "awsDevice": NotRequired[str],
        "jumboFrameCapable": NotRequired[bool],
        "awsDeviceV2": NotRequired[str],
        "awsLogicalDeviceId": NotRequired[str],
        "hasLogicalRedundancy": NotRequired[HasLogicalRedundancyType],
        "tags": NotRequired[List[TagTypeDef]],
        "providerName": NotRequired[str],
        "macSecCapable": NotRequired[bool],
        "portEncryptionStatus": NotRequired[str],
        "encryptionMode": NotRequired[str],
        "macSecKeys": NotRequired[List[MacSecKeyTypeDef]],
    },
)
DisassociateMacSecKeyResponseTypeDef = TypedDict(
    "DisassociateMacSecKeyResponseTypeDef",
    {
        "connectionId": str,
        "macSecKeys": List[MacSecKeyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DirectConnectGatewayAssociationProposalTypeDef = TypedDict(
    "DirectConnectGatewayAssociationProposalTypeDef",
    {
        "proposalId": NotRequired[str],
        "directConnectGatewayId": NotRequired[str],
        "directConnectGatewayOwnerAccount": NotRequired[str],
        "proposalState": NotRequired[DirectConnectGatewayAssociationProposalStateType],
        "associatedGateway": NotRequired[AssociatedGatewayTypeDef],
        "existingAllowedPrefixesToDirectConnectGateway": NotRequired[
            List[RouteFilterPrefixTypeDef]
        ],
        "requestedAllowedPrefixesToDirectConnectGateway": NotRequired[
            List[RouteFilterPrefixTypeDef]
        ],
    },
)
DirectConnectGatewayAssociationTypeDef = TypedDict(
    "DirectConnectGatewayAssociationTypeDef",
    {
        "directConnectGatewayId": NotRequired[str],
        "directConnectGatewayOwnerAccount": NotRequired[str],
        "associationState": NotRequired[DirectConnectGatewayAssociationStateType],
        "stateChangeError": NotRequired[str],
        "associatedGateway": NotRequired[AssociatedGatewayTypeDef],
        "associationId": NotRequired[str],
        "allowedPrefixesToDirectConnectGateway": NotRequired[List[RouteFilterPrefixTypeDef]],
        "virtualGatewayId": NotRequired[str],
        "virtualGatewayRegion": NotRequired[str],
        "virtualGatewayOwnerAccount": NotRequired[str],
    },
)
VirtualInterfaceResponseTypeDef = TypedDict(
    "VirtualInterfaceResponseTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": AddressFamilyType,
        "virtualInterfaceState": VirtualInterfaceStateType,
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List[RouteFilterPrefixTypeDef],
        "bgpPeers": List[BGPPeerTypeDef],
        "region": str,
        "awsDeviceV2": str,
        "awsLogicalDeviceId": str,
        "tags": List[TagTypeDef],
        "siteLinkEnabled": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VirtualInterfaceTypeDef = TypedDict(
    "VirtualInterfaceTypeDef",
    {
        "ownerAccount": NotRequired[str],
        "virtualInterfaceId": NotRequired[str],
        "location": NotRequired[str],
        "connectionId": NotRequired[str],
        "virtualInterfaceType": NotRequired[str],
        "virtualInterfaceName": NotRequired[str],
        "vlan": NotRequired[int],
        "asn": NotRequired[int],
        "amazonSideAsn": NotRequired[int],
        "authKey": NotRequired[str],
        "amazonAddress": NotRequired[str],
        "customerAddress": NotRequired[str],
        "addressFamily": NotRequired[AddressFamilyType],
        "virtualInterfaceState": NotRequired[VirtualInterfaceStateType],
        "customerRouterConfig": NotRequired[str],
        "mtu": NotRequired[int],
        "jumboFrameCapable": NotRequired[bool],
        "virtualGatewayId": NotRequired[str],
        "directConnectGatewayId": NotRequired[str],
        "routeFilterPrefixes": NotRequired[List[RouteFilterPrefixTypeDef]],
        "bgpPeers": NotRequired[List[BGPPeerTypeDef]],
        "region": NotRequired[str],
        "awsDeviceV2": NotRequired[str],
        "awsLogicalDeviceId": NotRequired[str],
        "tags": NotRequired[List[TagTypeDef]],
        "siteLinkEnabled": NotRequired[bool],
    },
)
CreateBGPPeerRequestRequestTypeDef = TypedDict(
    "CreateBGPPeerRequestRequestTypeDef",
    {
        "virtualInterfaceId": NotRequired[str],
        "newBGPPeer": NotRequired[NewBGPPeerTypeDef],
    },
)
CreateDirectConnectGatewayResultTypeDef = TypedDict(
    "CreateDirectConnectGatewayResultTypeDef",
    {
        "directConnectGateway": DirectConnectGatewayTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDirectConnectGatewayResultTypeDef = TypedDict(
    "DeleteDirectConnectGatewayResultTypeDef",
    {
        "directConnectGateway": DirectConnectGatewayTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDirectConnectGatewaysResultTypeDef = TypedDict(
    "DescribeDirectConnectGatewaysResultTypeDef",
    {
        "directConnectGateways": List[DirectConnectGatewayTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDirectConnectGatewayResponseTypeDef = TypedDict(
    "UpdateDirectConnectGatewayResponseTypeDef",
    {
        "directConnectGateway": DirectConnectGatewayTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeCustomerMetadataResponseTypeDef = TypedDict(
    "DescribeCustomerMetadataResponseTypeDef",
    {
        "agreements": List[CustomerAgreementTypeDef],
        "nniPartnerType": NniPartnerTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeConnectionLoaResponseTypeDef = TypedDict(
    "DescribeConnectionLoaResponseTypeDef",
    {
        "loa": LoaTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeInterconnectLoaResponseTypeDef = TypedDict(
    "DescribeInterconnectLoaResponseTypeDef",
    {
        "loa": LoaTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDirectConnectGatewayAssociationsRequestDescribeDirectConnectGatewayAssociationsPaginateTypeDef = TypedDict(
    "DescribeDirectConnectGatewayAssociationsRequestDescribeDirectConnectGatewayAssociationsPaginateTypeDef",
    {
        "associationId": NotRequired[str],
        "associatedGatewayId": NotRequired[str],
        "directConnectGatewayId": NotRequired[str],
        "virtualGatewayId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDirectConnectGatewayAttachmentsRequestDescribeDirectConnectGatewayAttachmentsPaginateTypeDef = TypedDict(
    "DescribeDirectConnectGatewayAttachmentsRequestDescribeDirectConnectGatewayAttachmentsPaginateTypeDef",
    {
        "directConnectGatewayId": NotRequired[str],
        "virtualInterfaceId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDirectConnectGatewaysRequestDescribeDirectConnectGatewaysPaginateTypeDef = TypedDict(
    "DescribeDirectConnectGatewaysRequestDescribeDirectConnectGatewaysPaginateTypeDef",
    {
        "directConnectGatewayId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDirectConnectGatewayAttachmentsResultTypeDef = TypedDict(
    "DescribeDirectConnectGatewayAttachmentsResultTypeDef",
    {
        "directConnectGatewayAttachments": List[DirectConnectGatewayAttachmentTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRouterConfigurationResponseTypeDef = TypedDict(
    "DescribeRouterConfigurationResponseTypeDef",
    {
        "customerRouterConfig": str,
        "router": RouterTypeTypeDef,
        "virtualInterfaceId": str,
        "virtualInterfaceName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListVirtualInterfaceTestHistoryResponseTypeDef = TypedDict(
    "ListVirtualInterfaceTestHistoryResponseTypeDef",
    {
        "virtualInterfaceTestHistory": List[VirtualInterfaceTestHistoryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartBgpFailoverTestResponseTypeDef = TypedDict(
    "StartBgpFailoverTestResponseTypeDef",
    {
        "virtualInterfaceTest": VirtualInterfaceTestHistoryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopBgpFailoverTestResponseTypeDef = TypedDict(
    "StopBgpFailoverTestResponseTypeDef",
    {
        "virtualInterfaceTest": VirtualInterfaceTestHistoryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LocationsTypeDef = TypedDict(
    "LocationsTypeDef",
    {
        "locations": List[LocationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VirtualGatewaysTypeDef = TypedDict(
    "VirtualGatewaysTypeDef",
    {
        "virtualGateways": List[VirtualGatewayTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InterconnectsTypeDef = TypedDict(
    "InterconnectsTypeDef",
    {
        "interconnects": List[InterconnectTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AllocatePrivateVirtualInterfaceRequestRequestTypeDef = TypedDict(
    "AllocatePrivateVirtualInterfaceRequestRequestTypeDef",
    {
        "connectionId": str,
        "ownerAccount": str,
        "newPrivateVirtualInterfaceAllocation": NewPrivateVirtualInterfaceAllocationTypeDef,
    },
)
CreatePrivateVirtualInterfaceRequestRequestTypeDef = TypedDict(
    "CreatePrivateVirtualInterfaceRequestRequestTypeDef",
    {
        "connectionId": str,
        "newPrivateVirtualInterface": NewPrivateVirtualInterfaceTypeDef,
    },
)
AllocatePublicVirtualInterfaceRequestRequestTypeDef = TypedDict(
    "AllocatePublicVirtualInterfaceRequestRequestTypeDef",
    {
        "connectionId": str,
        "ownerAccount": str,
        "newPublicVirtualInterfaceAllocation": NewPublicVirtualInterfaceAllocationTypeDef,
    },
)
CreatePublicVirtualInterfaceRequestRequestTypeDef = TypedDict(
    "CreatePublicVirtualInterfaceRequestRequestTypeDef",
    {
        "connectionId": str,
        "newPublicVirtualInterface": NewPublicVirtualInterfaceTypeDef,
    },
)
AllocateTransitVirtualInterfaceRequestRequestTypeDef = TypedDict(
    "AllocateTransitVirtualInterfaceRequestRequestTypeDef",
    {
        "connectionId": str,
        "ownerAccount": str,
        "newTransitVirtualInterfaceAllocation": NewTransitVirtualInterfaceAllocationTypeDef,
    },
)
CreateTransitVirtualInterfaceRequestRequestTypeDef = TypedDict(
    "CreateTransitVirtualInterfaceRequestRequestTypeDef",
    {
        "connectionId": str,
        "newTransitVirtualInterface": NewTransitVirtualInterfaceTypeDef,
    },
)
DescribeTagsResponseTypeDef = TypedDict(
    "DescribeTagsResponseTypeDef",
    {
        "resourceTags": List[ResourceTagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConnectionsTypeDef = TypedDict(
    "ConnectionsTypeDef",
    {
        "connections": List[ConnectionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LagResponseTypeDef = TypedDict(
    "LagResponseTypeDef",
    {
        "connectionsBandwidth": str,
        "numberOfConnections": int,
        "lagId": str,
        "ownerAccount": str,
        "lagName": str,
        "lagState": LagStateType,
        "location": str,
        "region": str,
        "minimumLinks": int,
        "awsDevice": str,
        "awsDeviceV2": str,
        "awsLogicalDeviceId": str,
        "connections": List[ConnectionTypeDef],
        "allowsHostedConnections": bool,
        "jumboFrameCapable": bool,
        "hasLogicalRedundancy": HasLogicalRedundancyType,
        "tags": List[TagTypeDef],
        "providerName": str,
        "macSecCapable": bool,
        "encryptionMode": str,
        "macSecKeys": List[MacSecKeyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LagTypeDef = TypedDict(
    "LagTypeDef",
    {
        "connectionsBandwidth": NotRequired[str],
        "numberOfConnections": NotRequired[int],
        "lagId": NotRequired[str],
        "ownerAccount": NotRequired[str],
        "lagName": NotRequired[str],
        "lagState": NotRequired[LagStateType],
        "location": NotRequired[str],
        "region": NotRequired[str],
        "minimumLinks": NotRequired[int],
        "awsDevice": NotRequired[str],
        "awsDeviceV2": NotRequired[str],
        "awsLogicalDeviceId": NotRequired[str],
        "connections": NotRequired[List[ConnectionTypeDef]],
        "allowsHostedConnections": NotRequired[bool],
        "jumboFrameCapable": NotRequired[bool],
        "hasLogicalRedundancy": NotRequired[HasLogicalRedundancyType],
        "tags": NotRequired[List[TagTypeDef]],
        "providerName": NotRequired[str],
        "macSecCapable": NotRequired[bool],
        "encryptionMode": NotRequired[str],
        "macSecKeys": NotRequired[List[MacSecKeyTypeDef]],
    },
)
CreateDirectConnectGatewayAssociationProposalResultTypeDef = TypedDict(
    "CreateDirectConnectGatewayAssociationProposalResultTypeDef",
    {
        "directConnectGatewayAssociationProposal": DirectConnectGatewayAssociationProposalTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDirectConnectGatewayAssociationProposalResultTypeDef = TypedDict(
    "DeleteDirectConnectGatewayAssociationProposalResultTypeDef",
    {
        "directConnectGatewayAssociationProposal": DirectConnectGatewayAssociationProposalTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDirectConnectGatewayAssociationProposalsResultTypeDef = TypedDict(
    "DescribeDirectConnectGatewayAssociationProposalsResultTypeDef",
    {
        "directConnectGatewayAssociationProposals": List[
            DirectConnectGatewayAssociationProposalTypeDef
        ],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AcceptDirectConnectGatewayAssociationProposalResultTypeDef = TypedDict(
    "AcceptDirectConnectGatewayAssociationProposalResultTypeDef",
    {
        "directConnectGatewayAssociation": DirectConnectGatewayAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDirectConnectGatewayAssociationResultTypeDef = TypedDict(
    "CreateDirectConnectGatewayAssociationResultTypeDef",
    {
        "directConnectGatewayAssociation": DirectConnectGatewayAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDirectConnectGatewayAssociationResultTypeDef = TypedDict(
    "DeleteDirectConnectGatewayAssociationResultTypeDef",
    {
        "directConnectGatewayAssociation": DirectConnectGatewayAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDirectConnectGatewayAssociationsResultTypeDef = TypedDict(
    "DescribeDirectConnectGatewayAssociationsResultTypeDef",
    {
        "directConnectGatewayAssociations": List[DirectConnectGatewayAssociationTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDirectConnectGatewayAssociationResultTypeDef = TypedDict(
    "UpdateDirectConnectGatewayAssociationResultTypeDef",
    {
        "directConnectGatewayAssociation": DirectConnectGatewayAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AllocateTransitVirtualInterfaceResultTypeDef = TypedDict(
    "AllocateTransitVirtualInterfaceResultTypeDef",
    {
        "virtualInterface": VirtualInterfaceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateBGPPeerResponseTypeDef = TypedDict(
    "CreateBGPPeerResponseTypeDef",
    {
        "virtualInterface": VirtualInterfaceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTransitVirtualInterfaceResultTypeDef = TypedDict(
    "CreateTransitVirtualInterfaceResultTypeDef",
    {
        "virtualInterface": VirtualInterfaceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteBGPPeerResponseTypeDef = TypedDict(
    "DeleteBGPPeerResponseTypeDef",
    {
        "virtualInterface": VirtualInterfaceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VirtualInterfacesTypeDef = TypedDict(
    "VirtualInterfacesTypeDef",
    {
        "virtualInterfaces": List[VirtualInterfaceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LagsTypeDef = TypedDict(
    "LagsTypeDef",
    {
        "lags": List[LagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
