"""
Type annotations for mediaconnect service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/type_defs/)

Usage::

    ```python
    from mypy_boto3_mediaconnect.type_defs import VpcInterfaceAttachmentTypeDef

    data: VpcInterfaceAttachmentTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AlgorithmType,
    BridgePlacementType,
    BridgeStateType,
    ColorimetryType,
    ConnectionStatusType,
    DesiredStateType,
    EncoderProfileType,
    EncodingNameType,
    EntitlementStatusType,
    FailoverModeType,
    GatewayStateType,
    InstanceStateType,
    KeyTypeType,
    MaintenanceDayType,
    MediaStreamTypeType,
    NetworkInterfaceTypeType,
    OutputStatusType,
    ProtocolType,
    RangeType,
    ReservationStateType,
    ScanModeType,
    SourceTypeType,
    StateType,
    StatusType,
    TcsType,
    ThumbnailStateType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "VpcInterfaceAttachmentTypeDef",
    "AddBridgeNetworkOutputRequestTypeDef",
    "AddBridgeNetworkSourceRequestTypeDef",
    "ResponseMetadataTypeDef",
    "AddEgressGatewayBridgeRequestTypeDef",
    "VpcInterfaceRequestTypeDef",
    "VpcInterfaceTypeDef",
    "AddIngressGatewayBridgeRequestTypeDef",
    "AddMaintenanceTypeDef",
    "EncryptionTypeDef",
    "BridgeFlowOutputTypeDef",
    "BridgeNetworkOutputTypeDef",
    "BridgeNetworkSourceTypeDef",
    "EgressGatewayBridgeTypeDef",
    "IngressGatewayBridgeTypeDef",
    "MessageDetailTypeDef",
    "MonitoringConfigTypeDef",
    "GatewayNetworkTypeDef",
    "DeleteBridgeRequestRequestTypeDef",
    "DeleteFlowRequestRequestTypeDef",
    "DeleteGatewayRequestRequestTypeDef",
    "DeregisterGatewayInstanceRequestRequestTypeDef",
    "DescribeBridgeRequestRequestTypeDef",
    "WaiterConfigTypeDef",
    "DescribeFlowRequestRequestTypeDef",
    "MessagesTypeDef",
    "DescribeFlowSourceMetadataRequestRequestTypeDef",
    "DescribeFlowSourceThumbnailRequestRequestTypeDef",
    "DescribeGatewayInstanceRequestRequestTypeDef",
    "DescribeGatewayRequestRequestTypeDef",
    "DescribeOfferingRequestRequestTypeDef",
    "DescribeReservationRequestRequestTypeDef",
    "InterfaceRequestTypeDef",
    "InterfaceTypeDef",
    "EncodingParametersRequestTypeDef",
    "EncodingParametersTypeDef",
    "SourcePriorityTypeDef",
    "MaintenanceTypeDef",
    "FmtpRequestTypeDef",
    "FmtpTypeDef",
    "FrameResolutionTypeDef",
    "PaginatorConfigTypeDef",
    "ListBridgesRequestRequestTypeDef",
    "ListedBridgeTypeDef",
    "ListEntitlementsRequestRequestTypeDef",
    "ListedEntitlementTypeDef",
    "ListFlowsRequestRequestTypeDef",
    "ListGatewayInstancesRequestRequestTypeDef",
    "ListedGatewayInstanceTypeDef",
    "ListGatewaysRequestRequestTypeDef",
    "ListedGatewayTypeDef",
    "ListOfferingsRequestRequestTypeDef",
    "ListReservationsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ResourceSpecificationTypeDef",
    "TransportTypeDef",
    "PurchaseOfferingRequestRequestTypeDef",
    "RemoveBridgeOutputRequestRequestTypeDef",
    "RemoveBridgeSourceRequestRequestTypeDef",
    "RemoveFlowMediaStreamRequestRequestTypeDef",
    "RemoveFlowOutputRequestRequestTypeDef",
    "RemoveFlowSourceRequestRequestTypeDef",
    "RemoveFlowVpcInterfaceRequestRequestTypeDef",
    "RevokeFlowEntitlementRequestRequestTypeDef",
    "StartFlowRequestRequestTypeDef",
    "StopFlowRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateBridgeNetworkOutputRequestTypeDef",
    "UpdateBridgeNetworkSourceRequestTypeDef",
    "UpdateEgressGatewayBridgeRequestTypeDef",
    "UpdateIngressGatewayBridgeRequestTypeDef",
    "UpdateBridgeStateRequestRequestTypeDef",
    "UpdateEncryptionTypeDef",
    "UpdateMaintenanceTypeDef",
    "UpdateGatewayInstanceRequestRequestTypeDef",
    "AddBridgeFlowSourceRequestTypeDef",
    "BridgeFlowSourceTypeDef",
    "GatewayBridgeSourceTypeDef",
    "SetGatewayBridgeSourceRequestTypeDef",
    "UpdateBridgeFlowSourceRequestTypeDef",
    "UpdateGatewayBridgeSourceRequestTypeDef",
    "AddBridgeOutputRequestTypeDef",
    "DeleteBridgeResponseTypeDef",
    "DeleteFlowResponseTypeDef",
    "DeleteGatewayResponseTypeDef",
    "DeregisterGatewayInstanceResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "RemoveBridgeOutputResponseTypeDef",
    "RemoveBridgeSourceResponseTypeDef",
    "RemoveFlowMediaStreamResponseTypeDef",
    "RemoveFlowOutputResponseTypeDef",
    "RemoveFlowSourceResponseTypeDef",
    "RemoveFlowVpcInterfaceResponseTypeDef",
    "RevokeFlowEntitlementResponseTypeDef",
    "StartFlowResponseTypeDef",
    "StopFlowResponseTypeDef",
    "UpdateBridgeStateResponseTypeDef",
    "UpdateGatewayInstanceResponseTypeDef",
    "AddFlowVpcInterfacesRequestRequestTypeDef",
    "AddFlowVpcInterfacesResponseTypeDef",
    "EntitlementTypeDef",
    "GrantEntitlementRequestTypeDef",
    "BridgeOutputTypeDef",
    "GatewayInstanceTypeDef",
    "ThumbnailDetailsTypeDef",
    "CreateGatewayRequestRequestTypeDef",
    "GatewayTypeDef",
    "DescribeFlowRequestFlowActiveWaitTypeDef",
    "DescribeFlowRequestFlowDeletedWaitTypeDef",
    "DescribeFlowRequestFlowStandbyWaitTypeDef",
    "DestinationConfigurationRequestTypeDef",
    "InputConfigurationRequestTypeDef",
    "DestinationConfigurationTypeDef",
    "InputConfigurationTypeDef",
    "FailoverConfigTypeDef",
    "UpdateFailoverConfigTypeDef",
    "ListedFlowTypeDef",
    "MediaStreamAttributesRequestTypeDef",
    "MediaStreamAttributesTypeDef",
    "TransportStreamTypeDef",
    "ListBridgesRequestListBridgesPaginateTypeDef",
    "ListEntitlementsRequestListEntitlementsPaginateTypeDef",
    "ListFlowsRequestListFlowsPaginateTypeDef",
    "ListGatewayInstancesRequestListGatewayInstancesPaginateTypeDef",
    "ListGatewaysRequestListGatewaysPaginateTypeDef",
    "ListOfferingsRequestListOfferingsPaginateTypeDef",
    "ListReservationsRequestListReservationsPaginateTypeDef",
    "ListBridgesResponseTypeDef",
    "ListEntitlementsResponseTypeDef",
    "ListGatewayInstancesResponseTypeDef",
    "ListGatewaysResponseTypeDef",
    "OfferingTypeDef",
    "ReservationTypeDef",
    "UpdateBridgeOutputRequestRequestTypeDef",
    "UpdateFlowEntitlementRequestRequestTypeDef",
    "AddBridgeSourceRequestTypeDef",
    "BridgeSourceTypeDef",
    "UpdateBridgeSourceRequestRequestTypeDef",
    "AddBridgeOutputsRequestRequestTypeDef",
    "GrantFlowEntitlementsResponseTypeDef",
    "UpdateFlowEntitlementResponseTypeDef",
    "GrantFlowEntitlementsRequestRequestTypeDef",
    "AddBridgeOutputsResponseTypeDef",
    "UpdateBridgeOutputResponseTypeDef",
    "DescribeGatewayInstanceResponseTypeDef",
    "DescribeFlowSourceThumbnailResponseTypeDef",
    "CreateGatewayResponseTypeDef",
    "DescribeGatewayResponseTypeDef",
    "MediaStreamOutputConfigurationRequestTypeDef",
    "MediaStreamSourceConfigurationRequestTypeDef",
    "MediaStreamOutputConfigurationTypeDef",
    "MediaStreamSourceConfigurationTypeDef",
    "UpdateBridgeRequestRequestTypeDef",
    "UpdateFlowRequestRequestTypeDef",
    "ListFlowsResponseTypeDef",
    "AddMediaStreamRequestTypeDef",
    "UpdateFlowMediaStreamRequestRequestTypeDef",
    "MediaStreamTypeDef",
    "TransportStreamProgramTypeDef",
    "DescribeOfferingResponseTypeDef",
    "ListOfferingsResponseTypeDef",
    "DescribeReservationResponseTypeDef",
    "ListReservationsResponseTypeDef",
    "PurchaseOfferingResponseTypeDef",
    "AddBridgeSourcesRequestRequestTypeDef",
    "CreateBridgeRequestRequestTypeDef",
    "AddBridgeSourcesResponseTypeDef",
    "BridgeTypeDef",
    "UpdateBridgeSourceResponseTypeDef",
    "AddOutputRequestTypeDef",
    "UpdateFlowOutputRequestRequestTypeDef",
    "SetSourceRequestTypeDef",
    "UpdateFlowSourceRequestRequestTypeDef",
    "OutputTypeDef",
    "SourceTypeDef",
    "AddFlowMediaStreamsRequestRequestTypeDef",
    "AddFlowMediaStreamsResponseTypeDef",
    "UpdateFlowMediaStreamResponseTypeDef",
    "TransportMediaInfoTypeDef",
    "CreateBridgeResponseTypeDef",
    "DescribeBridgeResponseTypeDef",
    "UpdateBridgeResponseTypeDef",
    "AddFlowOutputsRequestRequestTypeDef",
    "AddFlowSourcesRequestRequestTypeDef",
    "CreateFlowRequestRequestTypeDef",
    "AddFlowOutputsResponseTypeDef",
    "UpdateFlowOutputResponseTypeDef",
    "AddFlowSourcesResponseTypeDef",
    "FlowTypeDef",
    "UpdateFlowSourceResponseTypeDef",
    "DescribeFlowSourceMetadataResponseTypeDef",
    "CreateFlowResponseTypeDef",
    "DescribeFlowResponseTypeDef",
    "UpdateFlowResponseTypeDef",
)

VpcInterfaceAttachmentTypeDef = TypedDict(
    "VpcInterfaceAttachmentTypeDef",
    {
        "VpcInterfaceName": NotRequired[str],
    },
)
AddBridgeNetworkOutputRequestTypeDef = TypedDict(
    "AddBridgeNetworkOutputRequestTypeDef",
    {
        "IpAddress": str,
        "Name": str,
        "NetworkName": str,
        "Port": int,
        "Protocol": ProtocolType,
        "Ttl": int,
    },
)
AddBridgeNetworkSourceRequestTypeDef = TypedDict(
    "AddBridgeNetworkSourceRequestTypeDef",
    {
        "MulticastIp": str,
        "Name": str,
        "NetworkName": str,
        "Port": int,
        "Protocol": ProtocolType,
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
AddEgressGatewayBridgeRequestTypeDef = TypedDict(
    "AddEgressGatewayBridgeRequestTypeDef",
    {
        "MaxBitrate": int,
    },
)
VpcInterfaceRequestTypeDef = TypedDict(
    "VpcInterfaceRequestTypeDef",
    {
        "Name": str,
        "RoleArn": str,
        "SecurityGroupIds": Sequence[str],
        "SubnetId": str,
        "NetworkInterfaceType": NotRequired[NetworkInterfaceTypeType],
    },
)
VpcInterfaceTypeDef = TypedDict(
    "VpcInterfaceTypeDef",
    {
        "Name": str,
        "NetworkInterfaceIds": List[str],
        "NetworkInterfaceType": NetworkInterfaceTypeType,
        "RoleArn": str,
        "SecurityGroupIds": List[str],
        "SubnetId": str,
    },
)
AddIngressGatewayBridgeRequestTypeDef = TypedDict(
    "AddIngressGatewayBridgeRequestTypeDef",
    {
        "MaxBitrate": int,
        "MaxOutputs": int,
    },
)
AddMaintenanceTypeDef = TypedDict(
    "AddMaintenanceTypeDef",
    {
        "MaintenanceDay": MaintenanceDayType,
        "MaintenanceStartHour": str,
    },
)
EncryptionTypeDef = TypedDict(
    "EncryptionTypeDef",
    {
        "RoleArn": str,
        "Algorithm": NotRequired[AlgorithmType],
        "ConstantInitializationVector": NotRequired[str],
        "DeviceId": NotRequired[str],
        "KeyType": NotRequired[KeyTypeType],
        "Region": NotRequired[str],
        "ResourceId": NotRequired[str],
        "SecretArn": NotRequired[str],
        "Url": NotRequired[str],
    },
)
BridgeFlowOutputTypeDef = TypedDict(
    "BridgeFlowOutputTypeDef",
    {
        "FlowArn": str,
        "FlowSourceArn": str,
        "Name": str,
    },
)
BridgeNetworkOutputTypeDef = TypedDict(
    "BridgeNetworkOutputTypeDef",
    {
        "IpAddress": str,
        "Name": str,
        "NetworkName": str,
        "Port": int,
        "Protocol": ProtocolType,
        "Ttl": int,
    },
)
BridgeNetworkSourceTypeDef = TypedDict(
    "BridgeNetworkSourceTypeDef",
    {
        "MulticastIp": str,
        "Name": str,
        "NetworkName": str,
        "Port": int,
        "Protocol": ProtocolType,
    },
)
EgressGatewayBridgeTypeDef = TypedDict(
    "EgressGatewayBridgeTypeDef",
    {
        "MaxBitrate": int,
        "InstanceId": NotRequired[str],
    },
)
IngressGatewayBridgeTypeDef = TypedDict(
    "IngressGatewayBridgeTypeDef",
    {
        "MaxBitrate": int,
        "MaxOutputs": int,
        "InstanceId": NotRequired[str],
    },
)
MessageDetailTypeDef = TypedDict(
    "MessageDetailTypeDef",
    {
        "Code": str,
        "Message": str,
        "ResourceName": NotRequired[str],
    },
)
MonitoringConfigTypeDef = TypedDict(
    "MonitoringConfigTypeDef",
    {
        "ThumbnailState": NotRequired[ThumbnailStateType],
    },
)
GatewayNetworkTypeDef = TypedDict(
    "GatewayNetworkTypeDef",
    {
        "CidrBlock": str,
        "Name": str,
    },
)
DeleteBridgeRequestRequestTypeDef = TypedDict(
    "DeleteBridgeRequestRequestTypeDef",
    {
        "BridgeArn": str,
    },
)
DeleteFlowRequestRequestTypeDef = TypedDict(
    "DeleteFlowRequestRequestTypeDef",
    {
        "FlowArn": str,
    },
)
DeleteGatewayRequestRequestTypeDef = TypedDict(
    "DeleteGatewayRequestRequestTypeDef",
    {
        "GatewayArn": str,
    },
)
DeregisterGatewayInstanceRequestRequestTypeDef = TypedDict(
    "DeregisterGatewayInstanceRequestRequestTypeDef",
    {
        "GatewayInstanceArn": str,
        "Force": NotRequired[bool],
    },
)
DescribeBridgeRequestRequestTypeDef = TypedDict(
    "DescribeBridgeRequestRequestTypeDef",
    {
        "BridgeArn": str,
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
DescribeFlowRequestRequestTypeDef = TypedDict(
    "DescribeFlowRequestRequestTypeDef",
    {
        "FlowArn": str,
    },
)
MessagesTypeDef = TypedDict(
    "MessagesTypeDef",
    {
        "Errors": List[str],
    },
)
DescribeFlowSourceMetadataRequestRequestTypeDef = TypedDict(
    "DescribeFlowSourceMetadataRequestRequestTypeDef",
    {
        "FlowArn": str,
    },
)
DescribeFlowSourceThumbnailRequestRequestTypeDef = TypedDict(
    "DescribeFlowSourceThumbnailRequestRequestTypeDef",
    {
        "FlowArn": str,
    },
)
DescribeGatewayInstanceRequestRequestTypeDef = TypedDict(
    "DescribeGatewayInstanceRequestRequestTypeDef",
    {
        "GatewayInstanceArn": str,
    },
)
DescribeGatewayRequestRequestTypeDef = TypedDict(
    "DescribeGatewayRequestRequestTypeDef",
    {
        "GatewayArn": str,
    },
)
DescribeOfferingRequestRequestTypeDef = TypedDict(
    "DescribeOfferingRequestRequestTypeDef",
    {
        "OfferingArn": str,
    },
)
DescribeReservationRequestRequestTypeDef = TypedDict(
    "DescribeReservationRequestRequestTypeDef",
    {
        "ReservationArn": str,
    },
)
InterfaceRequestTypeDef = TypedDict(
    "InterfaceRequestTypeDef",
    {
        "Name": str,
    },
)
InterfaceTypeDef = TypedDict(
    "InterfaceTypeDef",
    {
        "Name": str,
    },
)
EncodingParametersRequestTypeDef = TypedDict(
    "EncodingParametersRequestTypeDef",
    {
        "CompressionFactor": float,
        "EncoderProfile": EncoderProfileType,
    },
)
EncodingParametersTypeDef = TypedDict(
    "EncodingParametersTypeDef",
    {
        "CompressionFactor": float,
        "EncoderProfile": EncoderProfileType,
    },
)
SourcePriorityTypeDef = TypedDict(
    "SourcePriorityTypeDef",
    {
        "PrimarySource": NotRequired[str],
    },
)
MaintenanceTypeDef = TypedDict(
    "MaintenanceTypeDef",
    {
        "MaintenanceDay": NotRequired[MaintenanceDayType],
        "MaintenanceDeadline": NotRequired[str],
        "MaintenanceScheduledDate": NotRequired[str],
        "MaintenanceStartHour": NotRequired[str],
    },
)
FmtpRequestTypeDef = TypedDict(
    "FmtpRequestTypeDef",
    {
        "ChannelOrder": NotRequired[str],
        "Colorimetry": NotRequired[ColorimetryType],
        "ExactFramerate": NotRequired[str],
        "Par": NotRequired[str],
        "Range": NotRequired[RangeType],
        "ScanMode": NotRequired[ScanModeType],
        "Tcs": NotRequired[TcsType],
    },
)
FmtpTypeDef = TypedDict(
    "FmtpTypeDef",
    {
        "ChannelOrder": NotRequired[str],
        "Colorimetry": NotRequired[ColorimetryType],
        "ExactFramerate": NotRequired[str],
        "Par": NotRequired[str],
        "Range": NotRequired[RangeType],
        "ScanMode": NotRequired[ScanModeType],
        "Tcs": NotRequired[TcsType],
    },
)
FrameResolutionTypeDef = TypedDict(
    "FrameResolutionTypeDef",
    {
        "FrameHeight": int,
        "FrameWidth": int,
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
ListBridgesRequestRequestTypeDef = TypedDict(
    "ListBridgesRequestRequestTypeDef",
    {
        "FilterArn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListedBridgeTypeDef = TypedDict(
    "ListedBridgeTypeDef",
    {
        "BridgeArn": str,
        "BridgeState": BridgeStateType,
        "BridgeType": str,
        "Name": str,
        "PlacementArn": str,
    },
)
ListEntitlementsRequestRequestTypeDef = TypedDict(
    "ListEntitlementsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListedEntitlementTypeDef = TypedDict(
    "ListedEntitlementTypeDef",
    {
        "EntitlementArn": str,
        "EntitlementName": str,
        "DataTransferSubscriberFeePercent": NotRequired[int],
    },
)
ListFlowsRequestRequestTypeDef = TypedDict(
    "ListFlowsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListGatewayInstancesRequestRequestTypeDef = TypedDict(
    "ListGatewayInstancesRequestRequestTypeDef",
    {
        "FilterArn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListedGatewayInstanceTypeDef = TypedDict(
    "ListedGatewayInstanceTypeDef",
    {
        "GatewayArn": str,
        "GatewayInstanceArn": str,
        "InstanceId": str,
        "InstanceState": NotRequired[InstanceStateType],
    },
)
ListGatewaysRequestRequestTypeDef = TypedDict(
    "ListGatewaysRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListedGatewayTypeDef = TypedDict(
    "ListedGatewayTypeDef",
    {
        "GatewayArn": str,
        "GatewayState": GatewayStateType,
        "Name": str,
    },
)
ListOfferingsRequestRequestTypeDef = TypedDict(
    "ListOfferingsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListReservationsRequestRequestTypeDef = TypedDict(
    "ListReservationsRequestRequestTypeDef",
    {
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
ResourceSpecificationTypeDef = TypedDict(
    "ResourceSpecificationTypeDef",
    {
        "ResourceType": Literal["Mbps_Outbound_Bandwidth"],
        "ReservedBitrate": NotRequired[int],
    },
)
TransportTypeDef = TypedDict(
    "TransportTypeDef",
    {
        "Protocol": ProtocolType,
        "CidrAllowList": NotRequired[List[str]],
        "MaxBitrate": NotRequired[int],
        "MaxLatency": NotRequired[int],
        "MaxSyncBuffer": NotRequired[int],
        "MinLatency": NotRequired[int],
        "RemoteId": NotRequired[str],
        "SenderControlPort": NotRequired[int],
        "SenderIpAddress": NotRequired[str],
        "SmoothingLatency": NotRequired[int],
        "SourceListenerAddress": NotRequired[str],
        "SourceListenerPort": NotRequired[int],
        "StreamId": NotRequired[str],
    },
)
PurchaseOfferingRequestRequestTypeDef = TypedDict(
    "PurchaseOfferingRequestRequestTypeDef",
    {
        "OfferingArn": str,
        "ReservationName": str,
        "Start": str,
    },
)
RemoveBridgeOutputRequestRequestTypeDef = TypedDict(
    "RemoveBridgeOutputRequestRequestTypeDef",
    {
        "BridgeArn": str,
        "OutputName": str,
    },
)
RemoveBridgeSourceRequestRequestTypeDef = TypedDict(
    "RemoveBridgeSourceRequestRequestTypeDef",
    {
        "BridgeArn": str,
        "SourceName": str,
    },
)
RemoveFlowMediaStreamRequestRequestTypeDef = TypedDict(
    "RemoveFlowMediaStreamRequestRequestTypeDef",
    {
        "FlowArn": str,
        "MediaStreamName": str,
    },
)
RemoveFlowOutputRequestRequestTypeDef = TypedDict(
    "RemoveFlowOutputRequestRequestTypeDef",
    {
        "FlowArn": str,
        "OutputArn": str,
    },
)
RemoveFlowSourceRequestRequestTypeDef = TypedDict(
    "RemoveFlowSourceRequestRequestTypeDef",
    {
        "FlowArn": str,
        "SourceArn": str,
    },
)
RemoveFlowVpcInterfaceRequestRequestTypeDef = TypedDict(
    "RemoveFlowVpcInterfaceRequestRequestTypeDef",
    {
        "FlowArn": str,
        "VpcInterfaceName": str,
    },
)
RevokeFlowEntitlementRequestRequestTypeDef = TypedDict(
    "RevokeFlowEntitlementRequestRequestTypeDef",
    {
        "EntitlementArn": str,
        "FlowArn": str,
    },
)
StartFlowRequestRequestTypeDef = TypedDict(
    "StartFlowRequestRequestTypeDef",
    {
        "FlowArn": str,
    },
)
StopFlowRequestRequestTypeDef = TypedDict(
    "StopFlowRequestRequestTypeDef",
    {
        "FlowArn": str,
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
UpdateBridgeNetworkOutputRequestTypeDef = TypedDict(
    "UpdateBridgeNetworkOutputRequestTypeDef",
    {
        "IpAddress": NotRequired[str],
        "NetworkName": NotRequired[str],
        "Port": NotRequired[int],
        "Protocol": NotRequired[ProtocolType],
        "Ttl": NotRequired[int],
    },
)
UpdateBridgeNetworkSourceRequestTypeDef = TypedDict(
    "UpdateBridgeNetworkSourceRequestTypeDef",
    {
        "MulticastIp": NotRequired[str],
        "NetworkName": NotRequired[str],
        "Port": NotRequired[int],
        "Protocol": NotRequired[ProtocolType],
    },
)
UpdateEgressGatewayBridgeRequestTypeDef = TypedDict(
    "UpdateEgressGatewayBridgeRequestTypeDef",
    {
        "MaxBitrate": NotRequired[int],
    },
)
UpdateIngressGatewayBridgeRequestTypeDef = TypedDict(
    "UpdateIngressGatewayBridgeRequestTypeDef",
    {
        "MaxBitrate": NotRequired[int],
        "MaxOutputs": NotRequired[int],
    },
)
UpdateBridgeStateRequestRequestTypeDef = TypedDict(
    "UpdateBridgeStateRequestRequestTypeDef",
    {
        "BridgeArn": str,
        "DesiredState": DesiredStateType,
    },
)
UpdateEncryptionTypeDef = TypedDict(
    "UpdateEncryptionTypeDef",
    {
        "Algorithm": NotRequired[AlgorithmType],
        "ConstantInitializationVector": NotRequired[str],
        "DeviceId": NotRequired[str],
        "KeyType": NotRequired[KeyTypeType],
        "Region": NotRequired[str],
        "ResourceId": NotRequired[str],
        "RoleArn": NotRequired[str],
        "SecretArn": NotRequired[str],
        "Url": NotRequired[str],
    },
)
UpdateMaintenanceTypeDef = TypedDict(
    "UpdateMaintenanceTypeDef",
    {
        "MaintenanceDay": NotRequired[MaintenanceDayType],
        "MaintenanceScheduledDate": NotRequired[str],
        "MaintenanceStartHour": NotRequired[str],
    },
)
UpdateGatewayInstanceRequestRequestTypeDef = TypedDict(
    "UpdateGatewayInstanceRequestRequestTypeDef",
    {
        "GatewayInstanceArn": str,
        "BridgePlacement": NotRequired[BridgePlacementType],
    },
)
AddBridgeFlowSourceRequestTypeDef = TypedDict(
    "AddBridgeFlowSourceRequestTypeDef",
    {
        "FlowArn": str,
        "Name": str,
        "FlowVpcInterfaceAttachment": NotRequired[VpcInterfaceAttachmentTypeDef],
    },
)
BridgeFlowSourceTypeDef = TypedDict(
    "BridgeFlowSourceTypeDef",
    {
        "FlowArn": str,
        "Name": str,
        "FlowVpcInterfaceAttachment": NotRequired[VpcInterfaceAttachmentTypeDef],
        "OutputArn": NotRequired[str],
    },
)
GatewayBridgeSourceTypeDef = TypedDict(
    "GatewayBridgeSourceTypeDef",
    {
        "BridgeArn": str,
        "VpcInterfaceAttachment": NotRequired[VpcInterfaceAttachmentTypeDef],
    },
)
SetGatewayBridgeSourceRequestTypeDef = TypedDict(
    "SetGatewayBridgeSourceRequestTypeDef",
    {
        "BridgeArn": str,
        "VpcInterfaceAttachment": NotRequired[VpcInterfaceAttachmentTypeDef],
    },
)
UpdateBridgeFlowSourceRequestTypeDef = TypedDict(
    "UpdateBridgeFlowSourceRequestTypeDef",
    {
        "FlowArn": NotRequired[str],
        "FlowVpcInterfaceAttachment": NotRequired[VpcInterfaceAttachmentTypeDef],
    },
)
UpdateGatewayBridgeSourceRequestTypeDef = TypedDict(
    "UpdateGatewayBridgeSourceRequestTypeDef",
    {
        "BridgeArn": NotRequired[str],
        "VpcInterfaceAttachment": NotRequired[VpcInterfaceAttachmentTypeDef],
    },
)
AddBridgeOutputRequestTypeDef = TypedDict(
    "AddBridgeOutputRequestTypeDef",
    {
        "NetworkOutput": NotRequired[AddBridgeNetworkOutputRequestTypeDef],
    },
)
DeleteBridgeResponseTypeDef = TypedDict(
    "DeleteBridgeResponseTypeDef",
    {
        "BridgeArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteFlowResponseTypeDef = TypedDict(
    "DeleteFlowResponseTypeDef",
    {
        "FlowArn": str,
        "Status": StatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteGatewayResponseTypeDef = TypedDict(
    "DeleteGatewayResponseTypeDef",
    {
        "GatewayArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeregisterGatewayInstanceResponseTypeDef = TypedDict(
    "DeregisterGatewayInstanceResponseTypeDef",
    {
        "GatewayInstanceArn": str,
        "InstanceState": InstanceStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
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
RemoveBridgeOutputResponseTypeDef = TypedDict(
    "RemoveBridgeOutputResponseTypeDef",
    {
        "BridgeArn": str,
        "OutputName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RemoveBridgeSourceResponseTypeDef = TypedDict(
    "RemoveBridgeSourceResponseTypeDef",
    {
        "BridgeArn": str,
        "SourceName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RemoveFlowMediaStreamResponseTypeDef = TypedDict(
    "RemoveFlowMediaStreamResponseTypeDef",
    {
        "FlowArn": str,
        "MediaStreamName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RemoveFlowOutputResponseTypeDef = TypedDict(
    "RemoveFlowOutputResponseTypeDef",
    {
        "FlowArn": str,
        "OutputArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RemoveFlowSourceResponseTypeDef = TypedDict(
    "RemoveFlowSourceResponseTypeDef",
    {
        "FlowArn": str,
        "SourceArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RemoveFlowVpcInterfaceResponseTypeDef = TypedDict(
    "RemoveFlowVpcInterfaceResponseTypeDef",
    {
        "FlowArn": str,
        "NonDeletedNetworkInterfaceIds": List[str],
        "VpcInterfaceName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RevokeFlowEntitlementResponseTypeDef = TypedDict(
    "RevokeFlowEntitlementResponseTypeDef",
    {
        "EntitlementArn": str,
        "FlowArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartFlowResponseTypeDef = TypedDict(
    "StartFlowResponseTypeDef",
    {
        "FlowArn": str,
        "Status": StatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopFlowResponseTypeDef = TypedDict(
    "StopFlowResponseTypeDef",
    {
        "FlowArn": str,
        "Status": StatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateBridgeStateResponseTypeDef = TypedDict(
    "UpdateBridgeStateResponseTypeDef",
    {
        "BridgeArn": str,
        "DesiredState": DesiredStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateGatewayInstanceResponseTypeDef = TypedDict(
    "UpdateGatewayInstanceResponseTypeDef",
    {
        "BridgePlacement": BridgePlacementType,
        "GatewayInstanceArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AddFlowVpcInterfacesRequestRequestTypeDef = TypedDict(
    "AddFlowVpcInterfacesRequestRequestTypeDef",
    {
        "FlowArn": str,
        "VpcInterfaces": Sequence[VpcInterfaceRequestTypeDef],
    },
)
AddFlowVpcInterfacesResponseTypeDef = TypedDict(
    "AddFlowVpcInterfacesResponseTypeDef",
    {
        "FlowArn": str,
        "VpcInterfaces": List[VpcInterfaceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EntitlementTypeDef = TypedDict(
    "EntitlementTypeDef",
    {
        "EntitlementArn": str,
        "Name": str,
        "Subscribers": List[str],
        "DataTransferSubscriberFeePercent": NotRequired[int],
        "Description": NotRequired[str],
        "Encryption": NotRequired[EncryptionTypeDef],
        "EntitlementStatus": NotRequired[EntitlementStatusType],
    },
)
GrantEntitlementRequestTypeDef = TypedDict(
    "GrantEntitlementRequestTypeDef",
    {
        "Subscribers": Sequence[str],
        "DataTransferSubscriberFeePercent": NotRequired[int],
        "Description": NotRequired[str],
        "Encryption": NotRequired[EncryptionTypeDef],
        "EntitlementStatus": NotRequired[EntitlementStatusType],
        "Name": NotRequired[str],
    },
)
BridgeOutputTypeDef = TypedDict(
    "BridgeOutputTypeDef",
    {
        "FlowOutput": NotRequired[BridgeFlowOutputTypeDef],
        "NetworkOutput": NotRequired[BridgeNetworkOutputTypeDef],
    },
)
GatewayInstanceTypeDef = TypedDict(
    "GatewayInstanceTypeDef",
    {
        "BridgePlacement": BridgePlacementType,
        "ConnectionStatus": ConnectionStatusType,
        "GatewayArn": str,
        "GatewayInstanceArn": str,
        "InstanceId": str,
        "InstanceState": InstanceStateType,
        "RunningBridgeCount": int,
        "InstanceMessages": NotRequired[List[MessageDetailTypeDef]],
    },
)
ThumbnailDetailsTypeDef = TypedDict(
    "ThumbnailDetailsTypeDef",
    {
        "FlowArn": str,
        "ThumbnailMessages": List[MessageDetailTypeDef],
        "Thumbnail": NotRequired[str],
        "Timecode": NotRequired[str],
        "Timestamp": NotRequired[datetime],
    },
)
CreateGatewayRequestRequestTypeDef = TypedDict(
    "CreateGatewayRequestRequestTypeDef",
    {
        "EgressCidrBlocks": Sequence[str],
        "Name": str,
        "Networks": Sequence[GatewayNetworkTypeDef],
    },
)
GatewayTypeDef = TypedDict(
    "GatewayTypeDef",
    {
        "EgressCidrBlocks": List[str],
        "GatewayArn": str,
        "Name": str,
        "Networks": List[GatewayNetworkTypeDef],
        "GatewayMessages": NotRequired[List[MessageDetailTypeDef]],
        "GatewayState": NotRequired[GatewayStateType],
    },
)
DescribeFlowRequestFlowActiveWaitTypeDef = TypedDict(
    "DescribeFlowRequestFlowActiveWaitTypeDef",
    {
        "FlowArn": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeFlowRequestFlowDeletedWaitTypeDef = TypedDict(
    "DescribeFlowRequestFlowDeletedWaitTypeDef",
    {
        "FlowArn": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeFlowRequestFlowStandbyWaitTypeDef = TypedDict(
    "DescribeFlowRequestFlowStandbyWaitTypeDef",
    {
        "FlowArn": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DestinationConfigurationRequestTypeDef = TypedDict(
    "DestinationConfigurationRequestTypeDef",
    {
        "DestinationIp": str,
        "DestinationPort": int,
        "Interface": InterfaceRequestTypeDef,
    },
)
InputConfigurationRequestTypeDef = TypedDict(
    "InputConfigurationRequestTypeDef",
    {
        "InputPort": int,
        "Interface": InterfaceRequestTypeDef,
    },
)
DestinationConfigurationTypeDef = TypedDict(
    "DestinationConfigurationTypeDef",
    {
        "DestinationIp": str,
        "DestinationPort": int,
        "Interface": InterfaceTypeDef,
        "OutboundIp": str,
    },
)
InputConfigurationTypeDef = TypedDict(
    "InputConfigurationTypeDef",
    {
        "InputIp": str,
        "InputPort": int,
        "Interface": InterfaceTypeDef,
    },
)
FailoverConfigTypeDef = TypedDict(
    "FailoverConfigTypeDef",
    {
        "FailoverMode": NotRequired[FailoverModeType],
        "RecoveryWindow": NotRequired[int],
        "SourcePriority": NotRequired[SourcePriorityTypeDef],
        "State": NotRequired[StateType],
    },
)
UpdateFailoverConfigTypeDef = TypedDict(
    "UpdateFailoverConfigTypeDef",
    {
        "FailoverMode": NotRequired[FailoverModeType],
        "RecoveryWindow": NotRequired[int],
        "SourcePriority": NotRequired[SourcePriorityTypeDef],
        "State": NotRequired[StateType],
    },
)
ListedFlowTypeDef = TypedDict(
    "ListedFlowTypeDef",
    {
        "AvailabilityZone": str,
        "Description": str,
        "FlowArn": str,
        "Name": str,
        "SourceType": SourceTypeType,
        "Status": StatusType,
        "Maintenance": NotRequired[MaintenanceTypeDef],
    },
)
MediaStreamAttributesRequestTypeDef = TypedDict(
    "MediaStreamAttributesRequestTypeDef",
    {
        "Fmtp": NotRequired[FmtpRequestTypeDef],
        "Lang": NotRequired[str],
    },
)
MediaStreamAttributesTypeDef = TypedDict(
    "MediaStreamAttributesTypeDef",
    {
        "Fmtp": FmtpTypeDef,
        "Lang": NotRequired[str],
    },
)
TransportStreamTypeDef = TypedDict(
    "TransportStreamTypeDef",
    {
        "Pid": int,
        "StreamType": str,
        "Channels": NotRequired[int],
        "Codec": NotRequired[str],
        "FrameRate": NotRequired[str],
        "FrameResolution": NotRequired[FrameResolutionTypeDef],
        "SampleRate": NotRequired[int],
        "SampleSize": NotRequired[int],
    },
)
ListBridgesRequestListBridgesPaginateTypeDef = TypedDict(
    "ListBridgesRequestListBridgesPaginateTypeDef",
    {
        "FilterArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEntitlementsRequestListEntitlementsPaginateTypeDef = TypedDict(
    "ListEntitlementsRequestListEntitlementsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFlowsRequestListFlowsPaginateTypeDef = TypedDict(
    "ListFlowsRequestListFlowsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGatewayInstancesRequestListGatewayInstancesPaginateTypeDef = TypedDict(
    "ListGatewayInstancesRequestListGatewayInstancesPaginateTypeDef",
    {
        "FilterArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGatewaysRequestListGatewaysPaginateTypeDef = TypedDict(
    "ListGatewaysRequestListGatewaysPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOfferingsRequestListOfferingsPaginateTypeDef = TypedDict(
    "ListOfferingsRequestListOfferingsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListReservationsRequestListReservationsPaginateTypeDef = TypedDict(
    "ListReservationsRequestListReservationsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListBridgesResponseTypeDef = TypedDict(
    "ListBridgesResponseTypeDef",
    {
        "Bridges": List[ListedBridgeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListEntitlementsResponseTypeDef = TypedDict(
    "ListEntitlementsResponseTypeDef",
    {
        "Entitlements": List[ListedEntitlementTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListGatewayInstancesResponseTypeDef = TypedDict(
    "ListGatewayInstancesResponseTypeDef",
    {
        "Instances": List[ListedGatewayInstanceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListGatewaysResponseTypeDef = TypedDict(
    "ListGatewaysResponseTypeDef",
    {
        "Gateways": List[ListedGatewayTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
OfferingTypeDef = TypedDict(
    "OfferingTypeDef",
    {
        "CurrencyCode": str,
        "Duration": int,
        "DurationUnits": Literal["MONTHS"],
        "OfferingArn": str,
        "OfferingDescription": str,
        "PricePerUnit": str,
        "PriceUnits": Literal["HOURLY"],
        "ResourceSpecification": ResourceSpecificationTypeDef,
    },
)
ReservationTypeDef = TypedDict(
    "ReservationTypeDef",
    {
        "CurrencyCode": str,
        "Duration": int,
        "DurationUnits": Literal["MONTHS"],
        "End": str,
        "OfferingArn": str,
        "OfferingDescription": str,
        "PricePerUnit": str,
        "PriceUnits": Literal["HOURLY"],
        "ReservationArn": str,
        "ReservationName": str,
        "ReservationState": ReservationStateType,
        "ResourceSpecification": ResourceSpecificationTypeDef,
        "Start": str,
    },
)
UpdateBridgeOutputRequestRequestTypeDef = TypedDict(
    "UpdateBridgeOutputRequestRequestTypeDef",
    {
        "BridgeArn": str,
        "OutputName": str,
        "NetworkOutput": NotRequired[UpdateBridgeNetworkOutputRequestTypeDef],
    },
)
UpdateFlowEntitlementRequestRequestTypeDef = TypedDict(
    "UpdateFlowEntitlementRequestRequestTypeDef",
    {
        "EntitlementArn": str,
        "FlowArn": str,
        "Description": NotRequired[str],
        "Encryption": NotRequired[UpdateEncryptionTypeDef],
        "EntitlementStatus": NotRequired[EntitlementStatusType],
        "Subscribers": NotRequired[Sequence[str]],
    },
)
AddBridgeSourceRequestTypeDef = TypedDict(
    "AddBridgeSourceRequestTypeDef",
    {
        "FlowSource": NotRequired[AddBridgeFlowSourceRequestTypeDef],
        "NetworkSource": NotRequired[AddBridgeNetworkSourceRequestTypeDef],
    },
)
BridgeSourceTypeDef = TypedDict(
    "BridgeSourceTypeDef",
    {
        "FlowSource": NotRequired[BridgeFlowSourceTypeDef],
        "NetworkSource": NotRequired[BridgeNetworkSourceTypeDef],
    },
)
UpdateBridgeSourceRequestRequestTypeDef = TypedDict(
    "UpdateBridgeSourceRequestRequestTypeDef",
    {
        "BridgeArn": str,
        "SourceName": str,
        "FlowSource": NotRequired[UpdateBridgeFlowSourceRequestTypeDef],
        "NetworkSource": NotRequired[UpdateBridgeNetworkSourceRequestTypeDef],
    },
)
AddBridgeOutputsRequestRequestTypeDef = TypedDict(
    "AddBridgeOutputsRequestRequestTypeDef",
    {
        "BridgeArn": str,
        "Outputs": Sequence[AddBridgeOutputRequestTypeDef],
    },
)
GrantFlowEntitlementsResponseTypeDef = TypedDict(
    "GrantFlowEntitlementsResponseTypeDef",
    {
        "Entitlements": List[EntitlementTypeDef],
        "FlowArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFlowEntitlementResponseTypeDef = TypedDict(
    "UpdateFlowEntitlementResponseTypeDef",
    {
        "Entitlement": EntitlementTypeDef,
        "FlowArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GrantFlowEntitlementsRequestRequestTypeDef = TypedDict(
    "GrantFlowEntitlementsRequestRequestTypeDef",
    {
        "Entitlements": Sequence[GrantEntitlementRequestTypeDef],
        "FlowArn": str,
    },
)
AddBridgeOutputsResponseTypeDef = TypedDict(
    "AddBridgeOutputsResponseTypeDef",
    {
        "BridgeArn": str,
        "Outputs": List[BridgeOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateBridgeOutputResponseTypeDef = TypedDict(
    "UpdateBridgeOutputResponseTypeDef",
    {
        "BridgeArn": str,
        "Output": BridgeOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeGatewayInstanceResponseTypeDef = TypedDict(
    "DescribeGatewayInstanceResponseTypeDef",
    {
        "GatewayInstance": GatewayInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeFlowSourceThumbnailResponseTypeDef = TypedDict(
    "DescribeFlowSourceThumbnailResponseTypeDef",
    {
        "ThumbnailDetails": ThumbnailDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGatewayResponseTypeDef = TypedDict(
    "CreateGatewayResponseTypeDef",
    {
        "Gateway": GatewayTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeGatewayResponseTypeDef = TypedDict(
    "DescribeGatewayResponseTypeDef",
    {
        "Gateway": GatewayTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MediaStreamOutputConfigurationRequestTypeDef = TypedDict(
    "MediaStreamOutputConfigurationRequestTypeDef",
    {
        "EncodingName": EncodingNameType,
        "MediaStreamName": str,
        "DestinationConfigurations": NotRequired[Sequence[DestinationConfigurationRequestTypeDef]],
        "EncodingParameters": NotRequired[EncodingParametersRequestTypeDef],
    },
)
MediaStreamSourceConfigurationRequestTypeDef = TypedDict(
    "MediaStreamSourceConfigurationRequestTypeDef",
    {
        "EncodingName": EncodingNameType,
        "MediaStreamName": str,
        "InputConfigurations": NotRequired[Sequence[InputConfigurationRequestTypeDef]],
    },
)
MediaStreamOutputConfigurationTypeDef = TypedDict(
    "MediaStreamOutputConfigurationTypeDef",
    {
        "EncodingName": EncodingNameType,
        "MediaStreamName": str,
        "DestinationConfigurations": NotRequired[List[DestinationConfigurationTypeDef]],
        "EncodingParameters": NotRequired[EncodingParametersTypeDef],
    },
)
MediaStreamSourceConfigurationTypeDef = TypedDict(
    "MediaStreamSourceConfigurationTypeDef",
    {
        "EncodingName": EncodingNameType,
        "MediaStreamName": str,
        "InputConfigurations": NotRequired[List[InputConfigurationTypeDef]],
    },
)
UpdateBridgeRequestRequestTypeDef = TypedDict(
    "UpdateBridgeRequestRequestTypeDef",
    {
        "BridgeArn": str,
        "EgressGatewayBridge": NotRequired[UpdateEgressGatewayBridgeRequestTypeDef],
        "IngressGatewayBridge": NotRequired[UpdateIngressGatewayBridgeRequestTypeDef],
        "SourceFailoverConfig": NotRequired[UpdateFailoverConfigTypeDef],
    },
)
UpdateFlowRequestRequestTypeDef = TypedDict(
    "UpdateFlowRequestRequestTypeDef",
    {
        "FlowArn": str,
        "SourceFailoverConfig": NotRequired[UpdateFailoverConfigTypeDef],
        "Maintenance": NotRequired[UpdateMaintenanceTypeDef],
        "SourceMonitoringConfig": NotRequired[MonitoringConfigTypeDef],
    },
)
ListFlowsResponseTypeDef = TypedDict(
    "ListFlowsResponseTypeDef",
    {
        "Flows": List[ListedFlowTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
AddMediaStreamRequestTypeDef = TypedDict(
    "AddMediaStreamRequestTypeDef",
    {
        "MediaStreamId": int,
        "MediaStreamName": str,
        "MediaStreamType": MediaStreamTypeType,
        "Attributes": NotRequired[MediaStreamAttributesRequestTypeDef],
        "ClockRate": NotRequired[int],
        "Description": NotRequired[str],
        "VideoFormat": NotRequired[str],
    },
)
UpdateFlowMediaStreamRequestRequestTypeDef = TypedDict(
    "UpdateFlowMediaStreamRequestRequestTypeDef",
    {
        "FlowArn": str,
        "MediaStreamName": str,
        "Attributes": NotRequired[MediaStreamAttributesRequestTypeDef],
        "ClockRate": NotRequired[int],
        "Description": NotRequired[str],
        "MediaStreamType": NotRequired[MediaStreamTypeType],
        "VideoFormat": NotRequired[str],
    },
)
MediaStreamTypeDef = TypedDict(
    "MediaStreamTypeDef",
    {
        "Fmt": int,
        "MediaStreamId": int,
        "MediaStreamName": str,
        "MediaStreamType": MediaStreamTypeType,
        "Attributes": NotRequired[MediaStreamAttributesTypeDef],
        "ClockRate": NotRequired[int],
        "Description": NotRequired[str],
        "VideoFormat": NotRequired[str],
    },
)
TransportStreamProgramTypeDef = TypedDict(
    "TransportStreamProgramTypeDef",
    {
        "PcrPid": int,
        "ProgramNumber": int,
        "ProgramPid": int,
        "Streams": List[TransportStreamTypeDef],
        "ProgramName": NotRequired[str],
    },
)
DescribeOfferingResponseTypeDef = TypedDict(
    "DescribeOfferingResponseTypeDef",
    {
        "Offering": OfferingTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListOfferingsResponseTypeDef = TypedDict(
    "ListOfferingsResponseTypeDef",
    {
        "Offerings": List[OfferingTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeReservationResponseTypeDef = TypedDict(
    "DescribeReservationResponseTypeDef",
    {
        "Reservation": ReservationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListReservationsResponseTypeDef = TypedDict(
    "ListReservationsResponseTypeDef",
    {
        "Reservations": List[ReservationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PurchaseOfferingResponseTypeDef = TypedDict(
    "PurchaseOfferingResponseTypeDef",
    {
        "Reservation": ReservationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AddBridgeSourcesRequestRequestTypeDef = TypedDict(
    "AddBridgeSourcesRequestRequestTypeDef",
    {
        "BridgeArn": str,
        "Sources": Sequence[AddBridgeSourceRequestTypeDef],
    },
)
CreateBridgeRequestRequestTypeDef = TypedDict(
    "CreateBridgeRequestRequestTypeDef",
    {
        "Name": str,
        "PlacementArn": str,
        "Sources": Sequence[AddBridgeSourceRequestTypeDef],
        "EgressGatewayBridge": NotRequired[AddEgressGatewayBridgeRequestTypeDef],
        "IngressGatewayBridge": NotRequired[AddIngressGatewayBridgeRequestTypeDef],
        "Outputs": NotRequired[Sequence[AddBridgeOutputRequestTypeDef]],
        "SourceFailoverConfig": NotRequired[FailoverConfigTypeDef],
    },
)
AddBridgeSourcesResponseTypeDef = TypedDict(
    "AddBridgeSourcesResponseTypeDef",
    {
        "BridgeArn": str,
        "Sources": List[BridgeSourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BridgeTypeDef = TypedDict(
    "BridgeTypeDef",
    {
        "BridgeArn": str,
        "BridgeState": BridgeStateType,
        "Name": str,
        "PlacementArn": str,
        "BridgeMessages": NotRequired[List[MessageDetailTypeDef]],
        "EgressGatewayBridge": NotRequired[EgressGatewayBridgeTypeDef],
        "IngressGatewayBridge": NotRequired[IngressGatewayBridgeTypeDef],
        "Outputs": NotRequired[List[BridgeOutputTypeDef]],
        "SourceFailoverConfig": NotRequired[FailoverConfigTypeDef],
        "Sources": NotRequired[List[BridgeSourceTypeDef]],
    },
)
UpdateBridgeSourceResponseTypeDef = TypedDict(
    "UpdateBridgeSourceResponseTypeDef",
    {
        "BridgeArn": str,
        "Source": BridgeSourceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AddOutputRequestTypeDef = TypedDict(
    "AddOutputRequestTypeDef",
    {
        "Protocol": ProtocolType,
        "CidrAllowList": NotRequired[Sequence[str]],
        "Description": NotRequired[str],
        "Destination": NotRequired[str],
        "Encryption": NotRequired[EncryptionTypeDef],
        "MaxLatency": NotRequired[int],
        "MediaStreamOutputConfigurations": NotRequired[
            Sequence[MediaStreamOutputConfigurationRequestTypeDef]
        ],
        "MinLatency": NotRequired[int],
        "Name": NotRequired[str],
        "Port": NotRequired[int],
        "RemoteId": NotRequired[str],
        "SenderControlPort": NotRequired[int],
        "SmoothingLatency": NotRequired[int],
        "StreamId": NotRequired[str],
        "VpcInterfaceAttachment": NotRequired[VpcInterfaceAttachmentTypeDef],
        "OutputStatus": NotRequired[OutputStatusType],
    },
)
UpdateFlowOutputRequestRequestTypeDef = TypedDict(
    "UpdateFlowOutputRequestRequestTypeDef",
    {
        "FlowArn": str,
        "OutputArn": str,
        "CidrAllowList": NotRequired[Sequence[str]],
        "Description": NotRequired[str],
        "Destination": NotRequired[str],
        "Encryption": NotRequired[UpdateEncryptionTypeDef],
        "MaxLatency": NotRequired[int],
        "MediaStreamOutputConfigurations": NotRequired[
            Sequence[MediaStreamOutputConfigurationRequestTypeDef]
        ],
        "MinLatency": NotRequired[int],
        "Port": NotRequired[int],
        "Protocol": NotRequired[ProtocolType],
        "RemoteId": NotRequired[str],
        "SenderControlPort": NotRequired[int],
        "SenderIpAddress": NotRequired[str],
        "SmoothingLatency": NotRequired[int],
        "StreamId": NotRequired[str],
        "VpcInterfaceAttachment": NotRequired[VpcInterfaceAttachmentTypeDef],
        "OutputStatus": NotRequired[OutputStatusType],
    },
)
SetSourceRequestTypeDef = TypedDict(
    "SetSourceRequestTypeDef",
    {
        "Decryption": NotRequired[EncryptionTypeDef],
        "Description": NotRequired[str],
        "EntitlementArn": NotRequired[str],
        "IngestPort": NotRequired[int],
        "MaxBitrate": NotRequired[int],
        "MaxLatency": NotRequired[int],
        "MaxSyncBuffer": NotRequired[int],
        "MediaStreamSourceConfigurations": NotRequired[
            Sequence[MediaStreamSourceConfigurationRequestTypeDef]
        ],
        "MinLatency": NotRequired[int],
        "Name": NotRequired[str],
        "Protocol": NotRequired[ProtocolType],
        "SenderControlPort": NotRequired[int],
        "SenderIpAddress": NotRequired[str],
        "SourceListenerAddress": NotRequired[str],
        "SourceListenerPort": NotRequired[int],
        "StreamId": NotRequired[str],
        "VpcInterfaceName": NotRequired[str],
        "WhitelistCidr": NotRequired[str],
        "GatewayBridgeSource": NotRequired[SetGatewayBridgeSourceRequestTypeDef],
    },
)
UpdateFlowSourceRequestRequestTypeDef = TypedDict(
    "UpdateFlowSourceRequestRequestTypeDef",
    {
        "FlowArn": str,
        "SourceArn": str,
        "Decryption": NotRequired[UpdateEncryptionTypeDef],
        "Description": NotRequired[str],
        "EntitlementArn": NotRequired[str],
        "IngestPort": NotRequired[int],
        "MaxBitrate": NotRequired[int],
        "MaxLatency": NotRequired[int],
        "MaxSyncBuffer": NotRequired[int],
        "MediaStreamSourceConfigurations": NotRequired[
            Sequence[MediaStreamSourceConfigurationRequestTypeDef]
        ],
        "MinLatency": NotRequired[int],
        "Protocol": NotRequired[ProtocolType],
        "SenderControlPort": NotRequired[int],
        "SenderIpAddress": NotRequired[str],
        "SourceListenerAddress": NotRequired[str],
        "SourceListenerPort": NotRequired[int],
        "StreamId": NotRequired[str],
        "VpcInterfaceName": NotRequired[str],
        "WhitelistCidr": NotRequired[str],
        "GatewayBridgeSource": NotRequired[UpdateGatewayBridgeSourceRequestTypeDef],
    },
)
OutputTypeDef = TypedDict(
    "OutputTypeDef",
    {
        "Name": str,
        "OutputArn": str,
        "DataTransferSubscriberFeePercent": NotRequired[int],
        "Description": NotRequired[str],
        "Destination": NotRequired[str],
        "Encryption": NotRequired[EncryptionTypeDef],
        "EntitlementArn": NotRequired[str],
        "ListenerAddress": NotRequired[str],
        "MediaLiveInputArn": NotRequired[str],
        "MediaStreamOutputConfigurations": NotRequired[List[MediaStreamOutputConfigurationTypeDef]],
        "Port": NotRequired[int],
        "Transport": NotRequired[TransportTypeDef],
        "VpcInterfaceAttachment": NotRequired[VpcInterfaceAttachmentTypeDef],
        "BridgeArn": NotRequired[str],
        "BridgePorts": NotRequired[List[int]],
        "OutputStatus": NotRequired[OutputStatusType],
    },
)
SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "Name": str,
        "SourceArn": str,
        "DataTransferSubscriberFeePercent": NotRequired[int],
        "Decryption": NotRequired[EncryptionTypeDef],
        "Description": NotRequired[str],
        "EntitlementArn": NotRequired[str],
        "IngestIp": NotRequired[str],
        "IngestPort": NotRequired[int],
        "MediaStreamSourceConfigurations": NotRequired[List[MediaStreamSourceConfigurationTypeDef]],
        "SenderControlPort": NotRequired[int],
        "SenderIpAddress": NotRequired[str],
        "Transport": NotRequired[TransportTypeDef],
        "VpcInterfaceName": NotRequired[str],
        "WhitelistCidr": NotRequired[str],
        "GatewayBridgeSource": NotRequired[GatewayBridgeSourceTypeDef],
    },
)
AddFlowMediaStreamsRequestRequestTypeDef = TypedDict(
    "AddFlowMediaStreamsRequestRequestTypeDef",
    {
        "FlowArn": str,
        "MediaStreams": Sequence[AddMediaStreamRequestTypeDef],
    },
)
AddFlowMediaStreamsResponseTypeDef = TypedDict(
    "AddFlowMediaStreamsResponseTypeDef",
    {
        "FlowArn": str,
        "MediaStreams": List[MediaStreamTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFlowMediaStreamResponseTypeDef = TypedDict(
    "UpdateFlowMediaStreamResponseTypeDef",
    {
        "FlowArn": str,
        "MediaStream": MediaStreamTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TransportMediaInfoTypeDef = TypedDict(
    "TransportMediaInfoTypeDef",
    {
        "Programs": List[TransportStreamProgramTypeDef],
    },
)
CreateBridgeResponseTypeDef = TypedDict(
    "CreateBridgeResponseTypeDef",
    {
        "Bridge": BridgeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeBridgeResponseTypeDef = TypedDict(
    "DescribeBridgeResponseTypeDef",
    {
        "Bridge": BridgeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateBridgeResponseTypeDef = TypedDict(
    "UpdateBridgeResponseTypeDef",
    {
        "Bridge": BridgeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AddFlowOutputsRequestRequestTypeDef = TypedDict(
    "AddFlowOutputsRequestRequestTypeDef",
    {
        "FlowArn": str,
        "Outputs": Sequence[AddOutputRequestTypeDef],
    },
)
AddFlowSourcesRequestRequestTypeDef = TypedDict(
    "AddFlowSourcesRequestRequestTypeDef",
    {
        "FlowArn": str,
        "Sources": Sequence[SetSourceRequestTypeDef],
    },
)
CreateFlowRequestRequestTypeDef = TypedDict(
    "CreateFlowRequestRequestTypeDef",
    {
        "Name": str,
        "AvailabilityZone": NotRequired[str],
        "Entitlements": NotRequired[Sequence[GrantEntitlementRequestTypeDef]],
        "MediaStreams": NotRequired[Sequence[AddMediaStreamRequestTypeDef]],
        "Outputs": NotRequired[Sequence[AddOutputRequestTypeDef]],
        "Source": NotRequired[SetSourceRequestTypeDef],
        "SourceFailoverConfig": NotRequired[FailoverConfigTypeDef],
        "Sources": NotRequired[Sequence[SetSourceRequestTypeDef]],
        "VpcInterfaces": NotRequired[Sequence[VpcInterfaceRequestTypeDef]],
        "Maintenance": NotRequired[AddMaintenanceTypeDef],
        "SourceMonitoringConfig": NotRequired[MonitoringConfigTypeDef],
    },
)
AddFlowOutputsResponseTypeDef = TypedDict(
    "AddFlowOutputsResponseTypeDef",
    {
        "FlowArn": str,
        "Outputs": List[OutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFlowOutputResponseTypeDef = TypedDict(
    "UpdateFlowOutputResponseTypeDef",
    {
        "FlowArn": str,
        "Output": OutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AddFlowSourcesResponseTypeDef = TypedDict(
    "AddFlowSourcesResponseTypeDef",
    {
        "FlowArn": str,
        "Sources": List[SourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FlowTypeDef = TypedDict(
    "FlowTypeDef",
    {
        "AvailabilityZone": str,
        "Entitlements": List[EntitlementTypeDef],
        "FlowArn": str,
        "Name": str,
        "Outputs": List[OutputTypeDef],
        "Source": SourceTypeDef,
        "Status": StatusType,
        "Description": NotRequired[str],
        "EgressIp": NotRequired[str],
        "MediaStreams": NotRequired[List[MediaStreamTypeDef]],
        "SourceFailoverConfig": NotRequired[FailoverConfigTypeDef],
        "Sources": NotRequired[List[SourceTypeDef]],
        "VpcInterfaces": NotRequired[List[VpcInterfaceTypeDef]],
        "Maintenance": NotRequired[MaintenanceTypeDef],
        "SourceMonitoringConfig": NotRequired[MonitoringConfigTypeDef],
    },
)
UpdateFlowSourceResponseTypeDef = TypedDict(
    "UpdateFlowSourceResponseTypeDef",
    {
        "FlowArn": str,
        "Source": SourceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeFlowSourceMetadataResponseTypeDef = TypedDict(
    "DescribeFlowSourceMetadataResponseTypeDef",
    {
        "FlowArn": str,
        "Messages": List[MessageDetailTypeDef],
        "Timestamp": datetime,
        "TransportMediaInfo": TransportMediaInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFlowResponseTypeDef = TypedDict(
    "CreateFlowResponseTypeDef",
    {
        "Flow": FlowTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeFlowResponseTypeDef = TypedDict(
    "DescribeFlowResponseTypeDef",
    {
        "Flow": FlowTypeDef,
        "Messages": MessagesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFlowResponseTypeDef = TypedDict(
    "UpdateFlowResponseTypeDef",
    {
        "Flow": FlowTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
