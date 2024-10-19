"""
Type annotations for iotwireless service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/type_defs/)

Usage::

    ```python
    from mypy_boto3_iotwireless.type_defs import SessionKeysAbpV10XTypeDef

    data: SessionKeysAbpV10XTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    AggregationPeriodType,
    BatteryLevelType,
    ConnectionStatusType,
    DeviceProfileTypeType,
    DeviceStateType,
    DimensionNameType,
    DlClassType,
    DownlinkModeType,
    EventNotificationResourceTypeType,
    EventNotificationTopicStatusType,
    EventType,
    ExpressionTypeType,
    FuotaDeviceStatusType,
    FuotaTaskStatusType,
    IdentifierTypeType,
    ImportTaskStatusType,
    LogLevelType,
    MessageTypeType,
    MetricNameType,
    MetricQueryStatusType,
    MulticastFrameInfoType,
    OnboardStatusType,
    PositionConfigurationFecType,
    PositionConfigurationStatusType,
    PositioningConfigStatusType,
    PositionResourceTypeType,
    SigningAlgType,
    SummaryMetricConfigurationStatusType,
    SupportedRfRegionType,
    WirelessDeviceEventType,
    WirelessDeviceFrameInfoType,
    WirelessDeviceIdTypeType,
    WirelessDeviceSidewalkStatusType,
    WirelessDeviceTypeType,
    WirelessGatewayEventType,
    WirelessGatewayIdTypeType,
    WirelessGatewayServiceTypeType,
    WirelessGatewayTaskStatusType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "SessionKeysAbpV10XTypeDef",
    "SessionKeysAbpV11TypeDef",
    "AccuracyTypeDef",
    "ApplicationConfigTypeDef",
    "SidewalkAccountInfoTypeDef",
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "AssociateMulticastGroupWithFuotaTaskRequestRequestTypeDef",
    "AssociateWirelessDeviceWithFuotaTaskRequestRequestTypeDef",
    "AssociateWirelessDeviceWithMulticastGroupRequestRequestTypeDef",
    "AssociateWirelessDeviceWithThingRequestRequestTypeDef",
    "AssociateWirelessGatewayWithCertificateRequestRequestTypeDef",
    "AssociateWirelessGatewayWithThingRequestRequestTypeDef",
    "BeaconingOutputTypeDef",
    "BeaconingTypeDef",
    "BlobTypeDef",
    "CancelMulticastGroupSessionRequestRequestTypeDef",
    "CdmaLocalIdTypeDef",
    "CdmaNmrObjTypeDef",
    "CertificateListTypeDef",
    "LoRaWANConnectionStatusEventNotificationConfigurationsTypeDef",
    "LoRaWANConnectionStatusResourceTypeEventConfigurationTypeDef",
    "LoRaWANDeviceProfileTypeDef",
    "LoRaWANFuotaTaskTypeDef",
    "LoRaWANMulticastTypeDef",
    "TraceContentTypeDef",
    "LoRaWANServiceProfileTypeDef",
    "SidewalkCreateWirelessDeviceTypeDef",
    "CreateWirelessGatewayTaskRequestRequestTypeDef",
    "DakCertificateMetadataTypeDef",
    "DeleteDestinationRequestRequestTypeDef",
    "DeleteDeviceProfileRequestRequestTypeDef",
    "DeleteFuotaTaskRequestRequestTypeDef",
    "DeleteMulticastGroupRequestRequestTypeDef",
    "DeleteNetworkAnalyzerConfigurationRequestRequestTypeDef",
    "DeleteQueuedMessagesRequestRequestTypeDef",
    "DeleteServiceProfileRequestRequestTypeDef",
    "DeleteWirelessDeviceImportTaskRequestRequestTypeDef",
    "DeleteWirelessDeviceRequestRequestTypeDef",
    "DeleteWirelessGatewayRequestRequestTypeDef",
    "DeleteWirelessGatewayTaskDefinitionRequestRequestTypeDef",
    "DeleteWirelessGatewayTaskRequestRequestTypeDef",
    "DeregisterWirelessDeviceRequestRequestTypeDef",
    "DestinationsTypeDef",
    "DeviceProfileTypeDef",
    "SidewalkEventNotificationConfigurationsTypeDef",
    "SidewalkResourceTypeEventConfigurationTypeDef",
    "DimensionTypeDef",
    "DisassociateAwsAccountFromPartnerAccountRequestRequestTypeDef",
    "DisassociateMulticastGroupFromFuotaTaskRequestRequestTypeDef",
    "DisassociateWirelessDeviceFromFuotaTaskRequestRequestTypeDef",
    "DisassociateWirelessDeviceFromMulticastGroupRequestRequestTypeDef",
    "DisassociateWirelessDeviceFromThingRequestRequestTypeDef",
    "DisassociateWirelessGatewayFromCertificateRequestRequestTypeDef",
    "DisassociateWirelessGatewayFromThingRequestRequestTypeDef",
    "PositioningTypeDef",
    "FuotaTaskTypeDef",
    "GatewayListItemTypeDef",
    "GetDestinationRequestRequestTypeDef",
    "GetDeviceProfileRequestRequestTypeDef",
    "LoRaWANDeviceProfileOutputTypeDef",
    "GetFuotaTaskRequestRequestTypeDef",
    "LoRaWANFuotaTaskGetInfoTypeDef",
    "SummaryMetricConfigurationTypeDef",
    "GetMulticastGroupRequestRequestTypeDef",
    "LoRaWANMulticastGetTypeDef",
    "GetMulticastGroupSessionRequestRequestTypeDef",
    "LoRaWANMulticastSessionOutputTypeDef",
    "GetNetworkAnalyzerConfigurationRequestRequestTypeDef",
    "GetPartnerAccountRequestRequestTypeDef",
    "SidewalkAccountInfoWithFingerprintTypeDef",
    "GetPositionConfigurationRequestRequestTypeDef",
    "GnssTypeDef",
    "IpTypeDef",
    "TimestampTypeDef",
    "WiFiAccessPointTypeDef",
    "GetPositionRequestRequestTypeDef",
    "GetResourceEventConfigurationRequestRequestTypeDef",
    "GetResourceLogLevelRequestRequestTypeDef",
    "GetResourcePositionRequestRequestTypeDef",
    "GetServiceEndpointRequestRequestTypeDef",
    "GetServiceProfileRequestRequestTypeDef",
    "LoRaWANGetServiceProfileInfoTypeDef",
    "GetWirelessDeviceImportTaskRequestRequestTypeDef",
    "SidewalkGetStartImportInfoTypeDef",
    "GetWirelessDeviceRequestRequestTypeDef",
    "GetWirelessDeviceStatisticsRequestRequestTypeDef",
    "SidewalkDeviceMetadataTypeDef",
    "GetWirelessGatewayCertificateRequestRequestTypeDef",
    "GetWirelessGatewayFirmwareInformationRequestRequestTypeDef",
    "GetWirelessGatewayRequestRequestTypeDef",
    "GetWirelessGatewayStatisticsRequestRequestTypeDef",
    "GetWirelessGatewayTaskDefinitionRequestRequestTypeDef",
    "GetWirelessGatewayTaskRequestRequestTypeDef",
    "GlobalIdentityTypeDef",
    "GsmLocalIdTypeDef",
    "ImportedSidewalkDeviceTypeDef",
    "LoRaWANJoinEventNotificationConfigurationsTypeDef",
    "LoRaWANJoinResourceTypeEventConfigurationTypeDef",
    "ListDestinationsRequestRequestTypeDef",
    "ListDeviceProfilesRequestRequestTypeDef",
    "ListDevicesForWirelessDeviceImportTaskRequestRequestTypeDef",
    "ListEventConfigurationsRequestRequestTypeDef",
    "ListFuotaTasksRequestRequestTypeDef",
    "ListMulticastGroupsByFuotaTaskRequestRequestTypeDef",
    "MulticastGroupByFuotaTaskTypeDef",
    "ListMulticastGroupsRequestRequestTypeDef",
    "MulticastGroupTypeDef",
    "ListNetworkAnalyzerConfigurationsRequestRequestTypeDef",
    "NetworkAnalyzerConfigurationsTypeDef",
    "ListPartnerAccountsRequestRequestTypeDef",
    "ListPositionConfigurationsRequestRequestTypeDef",
    "ListQueuedMessagesRequestRequestTypeDef",
    "ListServiceProfilesRequestRequestTypeDef",
    "ServiceProfileTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListWirelessDeviceImportTasksRequestRequestTypeDef",
    "ListWirelessDevicesRequestRequestTypeDef",
    "ListWirelessGatewayTaskDefinitionsRequestRequestTypeDef",
    "ListWirelessGatewaysRequestRequestTypeDef",
    "LoRaWANGatewayMetadataTypeDef",
    "LoRaWANPublicGatewayMetadataTypeDef",
    "OtaaV10XTypeDef",
    "OtaaV11TypeDef",
    "LoRaWANGatewayVersionTypeDef",
    "LoRaWANListDeviceTypeDef",
    "LoRaWANMulticastMetadataTypeDef",
    "UpdateAbpV10XTypeDef",
    "UpdateAbpV11TypeDef",
    "LteLocalIdTypeDef",
    "LteNmrObjTypeDef",
    "MetricQueryValueTypeDef",
    "SemtechGnssConfigurationTypeDef",
    "SemtechGnssDetailTypeDef",
    "PutResourceLogLevelRequestRequestTypeDef",
    "ResetResourceLogLevelRequestRequestTypeDef",
    "SidewalkSendDataToDeviceTypeDef",
    "SidewalkSingleStartImportInfoTypeDef",
    "SidewalkStartImportInfoTypeDef",
    "SidewalkUpdateAccountTypeDef",
    "SidewalkUpdateImportInfoTypeDef",
    "TdscdmaLocalIdTypeDef",
    "TdscdmaNmrObjTypeDef",
    "TestWirelessDeviceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDestinationRequestRequestTypeDef",
    "UpdatePositionRequestRequestTypeDef",
    "UpdateWirelessGatewayRequestRequestTypeDef",
    "WcdmaLocalIdTypeDef",
    "WcdmaNmrObjTypeDef",
    "WirelessDeviceEventLogOptionTypeDef",
    "WirelessGatewayEventLogOptionTypeDef",
    "AbpV10XTypeDef",
    "AbpV11TypeDef",
    "AssociateAwsAccountWithPartnerAccountRequestRequestTypeDef",
    "CreateDestinationRequestRequestTypeDef",
    "StartBulkAssociateWirelessDeviceWithMulticastGroupRequestRequestTypeDef",
    "StartBulkDisassociateWirelessDeviceFromMulticastGroupRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "AssociateAwsAccountWithPartnerAccountResponseTypeDef",
    "AssociateWirelessGatewayWithCertificateResponseTypeDef",
    "CreateDestinationResponseTypeDef",
    "CreateDeviceProfileResponseTypeDef",
    "CreateFuotaTaskResponseTypeDef",
    "CreateMulticastGroupResponseTypeDef",
    "CreateNetworkAnalyzerConfigurationResponseTypeDef",
    "CreateServiceProfileResponseTypeDef",
    "CreateWirelessDeviceResponseTypeDef",
    "CreateWirelessGatewayResponseTypeDef",
    "CreateWirelessGatewayTaskDefinitionResponseTypeDef",
    "CreateWirelessGatewayTaskResponseTypeDef",
    "GetDestinationResponseTypeDef",
    "GetPositionEstimateResponseTypeDef",
    "GetPositionResponseTypeDef",
    "GetResourceLogLevelResponseTypeDef",
    "GetResourcePositionResponseTypeDef",
    "GetServiceEndpointResponseTypeDef",
    "GetWirelessGatewayCertificateResponseTypeDef",
    "GetWirelessGatewayStatisticsResponseTypeDef",
    "GetWirelessGatewayTaskResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "SendDataToMulticastGroupResponseTypeDef",
    "SendDataToWirelessDeviceResponseTypeDef",
    "StartSingleWirelessDeviceImportTaskResponseTypeDef",
    "StartWirelessDeviceImportTaskResponseTypeDef",
    "TestWirelessDeviceResponseTypeDef",
    "LoRaWANGatewayOutputTypeDef",
    "BeaconingUnionTypeDef",
    "UpdateResourcePositionRequestRequestTypeDef",
    "CdmaObjTypeDef",
    "SidewalkDeviceTypeDef",
    "SidewalkListDeviceTypeDef",
    "ConnectionStatusEventConfigurationTypeDef",
    "ConnectionStatusResourceTypeEventConfigurationTypeDef",
    "CreateDeviceProfileRequestRequestTypeDef",
    "CreateFuotaTaskRequestRequestTypeDef",
    "UpdateFuotaTaskRequestRequestTypeDef",
    "CreateMulticastGroupRequestRequestTypeDef",
    "UpdateMulticastGroupRequestRequestTypeDef",
    "CreateNetworkAnalyzerConfigurationRequestRequestTypeDef",
    "GetNetworkAnalyzerConfigurationResponseTypeDef",
    "UpdateNetworkAnalyzerConfigurationRequestRequestTypeDef",
    "CreateServiceProfileRequestRequestTypeDef",
    "SidewalkGetDeviceProfileTypeDef",
    "ListDestinationsResponseTypeDef",
    "ListDeviceProfilesResponseTypeDef",
    "DeviceRegistrationStateEventConfigurationTypeDef",
    "MessageDeliveryStatusEventConfigurationTypeDef",
    "ProximityEventConfigurationTypeDef",
    "DeviceRegistrationStateResourceTypeEventConfigurationTypeDef",
    "MessageDeliveryStatusResourceTypeEventConfigurationTypeDef",
    "ProximityResourceTypeEventConfigurationTypeDef",
    "FPortsOutputTypeDef",
    "FPortsTypeDef",
    "UpdateFPortsTypeDef",
    "ListFuotaTasksResponseTypeDef",
    "ParticipatingGatewaysOutputTypeDef",
    "ParticipatingGatewaysTypeDef",
    "GetFuotaTaskResponseTypeDef",
    "GetMetricConfigurationResponseTypeDef",
    "UpdateMetricConfigurationRequestRequestTypeDef",
    "GetMulticastGroupResponseTypeDef",
    "GetMulticastGroupSessionResponseTypeDef",
    "GetPartnerAccountResponseTypeDef",
    "ListPartnerAccountsResponseTypeDef",
    "LoRaWANMulticastSessionTypeDef",
    "LoRaWANStartFuotaTaskTypeDef",
    "SummaryMetricQueryTypeDef",
    "GetServiceProfileResponseTypeDef",
    "GetWirelessDeviceImportTaskResponseTypeDef",
    "WirelessDeviceImportTaskTypeDef",
    "GsmNmrObjTypeDef",
    "ImportedWirelessDeviceTypeDef",
    "JoinEventConfigurationTypeDef",
    "JoinResourceTypeEventConfigurationTypeDef",
    "ListMulticastGroupsByFuotaTaskResponseTypeDef",
    "ListMulticastGroupsResponseTypeDef",
    "ListNetworkAnalyzerConfigurationsResponseTypeDef",
    "ListServiceProfilesResponseTypeDef",
    "LoRaWANDeviceMetadataTypeDef",
    "LoRaWANGatewayCurrentVersionTypeDef",
    "LoRaWANUpdateGatewayTaskCreateTypeDef",
    "LoRaWANUpdateGatewayTaskEntryTypeDef",
    "MulticastWirelessMetadataTypeDef",
    "LteObjTypeDef",
    "SummaryMetricQueryResultTypeDef",
    "PositionSolverConfigurationsTypeDef",
    "PositionSolverDetailsTypeDef",
    "StartSingleWirelessDeviceImportTaskRequestRequestTypeDef",
    "StartWirelessDeviceImportTaskRequestRequestTypeDef",
    "UpdatePartnerAccountRequestRequestTypeDef",
    "UpdateWirelessDeviceImportTaskRequestRequestTypeDef",
    "TdscdmaObjTypeDef",
    "WcdmaObjTypeDef",
    "WirelessDeviceLogOptionOutputTypeDef",
    "WirelessDeviceLogOptionTypeDef",
    "WirelessGatewayLogOptionOutputTypeDef",
    "WirelessGatewayLogOptionTypeDef",
    "GetWirelessGatewayResponseTypeDef",
    "WirelessGatewayStatisticsTypeDef",
    "LoRaWANGatewayTypeDef",
    "WirelessDeviceStatisticsTypeDef",
    "GetDeviceProfileResponseTypeDef",
    "LoRaWANDeviceOutputTypeDef",
    "FPortsUnionTypeDef",
    "LoRaWANUpdateDeviceTypeDef",
    "LoRaWANSendDataToDeviceOutputTypeDef",
    "ParticipatingGatewaysUnionTypeDef",
    "StartMulticastGroupSessionRequestRequestTypeDef",
    "StartFuotaTaskRequestRequestTypeDef",
    "GetMetricsRequestRequestTypeDef",
    "ListWirelessDeviceImportTasksResponseTypeDef",
    "GsmObjTypeDef",
    "ListDevicesForWirelessDeviceImportTaskResponseTypeDef",
    "EventNotificationItemConfigurationsTypeDef",
    "GetResourceEventConfigurationResponseTypeDef",
    "UpdateResourceEventConfigurationRequestRequestTypeDef",
    "GetEventConfigurationByResourceTypesResponseTypeDef",
    "UpdateEventConfigurationByResourceTypesRequestRequestTypeDef",
    "GetWirelessDeviceStatisticsResponseTypeDef",
    "GetWirelessGatewayFirmwareInformationResponseTypeDef",
    "UpdateWirelessGatewayTaskCreateTypeDef",
    "UpdateWirelessGatewayTaskEntryTypeDef",
    "SendDataToMulticastGroupRequestRequestTypeDef",
    "GetMetricsResponseTypeDef",
    "PutPositionConfigurationRequestRequestTypeDef",
    "GetPositionConfigurationResponseTypeDef",
    "PositionConfigurationItemTypeDef",
    "WirelessDeviceLogOptionUnionTypeDef",
    "GetLogLevelsByResourceTypesResponseTypeDef",
    "WirelessGatewayLogOptionUnionTypeDef",
    "ListWirelessGatewaysResponseTypeDef",
    "CreateWirelessGatewayRequestRequestTypeDef",
    "ListWirelessDevicesResponseTypeDef",
    "GetWirelessDeviceResponseTypeDef",
    "LoRaWANDeviceTypeDef",
    "UpdateWirelessDeviceRequestRequestTypeDef",
    "DownlinkQueueMessageTypeDef",
    "LoRaWANSendDataToDeviceTypeDef",
    "CellTowersTypeDef",
    "EventConfigurationItemTypeDef",
    "CreateWirelessGatewayTaskDefinitionRequestRequestTypeDef",
    "GetWirelessGatewayTaskDefinitionResponseTypeDef",
    "ListWirelessGatewayTaskDefinitionsResponseTypeDef",
    "ListPositionConfigurationsResponseTypeDef",
    "UpdateLogLevelsByResourceTypesRequestRequestTypeDef",
    "CreateWirelessDeviceRequestRequestTypeDef",
    "ListQueuedMessagesResponseTypeDef",
    "LoRaWANSendDataToDeviceUnionTypeDef",
    "GetPositionEstimateRequestRequestTypeDef",
    "ListEventConfigurationsResponseTypeDef",
    "WirelessMetadataTypeDef",
    "SendDataToWirelessDeviceRequestRequestTypeDef",
)

SessionKeysAbpV10XTypeDef = TypedDict(
    "SessionKeysAbpV10XTypeDef",
    {
        "NwkSKey": NotRequired[str],
        "AppSKey": NotRequired[str],
    },
)
SessionKeysAbpV11TypeDef = TypedDict(
    "SessionKeysAbpV11TypeDef",
    {
        "FNwkSIntKey": NotRequired[str],
        "SNwkSIntKey": NotRequired[str],
        "NwkSEncKey": NotRequired[str],
        "AppSKey": NotRequired[str],
    },
)
AccuracyTypeDef = TypedDict(
    "AccuracyTypeDef",
    {
        "HorizontalAccuracy": NotRequired[float],
        "VerticalAccuracy": NotRequired[float],
    },
)
ApplicationConfigTypeDef = TypedDict(
    "ApplicationConfigTypeDef",
    {
        "FPort": NotRequired[int],
        "Type": NotRequired[Literal["SemtechGeolocation"]],
        "DestinationName": NotRequired[str],
    },
)
SidewalkAccountInfoTypeDef = TypedDict(
    "SidewalkAccountInfoTypeDef",
    {
        "AmazonId": NotRequired[str],
        "AppServerPrivateKey": NotRequired[str],
    },
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
AssociateMulticastGroupWithFuotaTaskRequestRequestTypeDef = TypedDict(
    "AssociateMulticastGroupWithFuotaTaskRequestRequestTypeDef",
    {
        "Id": str,
        "MulticastGroupId": str,
    },
)
AssociateWirelessDeviceWithFuotaTaskRequestRequestTypeDef = TypedDict(
    "AssociateWirelessDeviceWithFuotaTaskRequestRequestTypeDef",
    {
        "Id": str,
        "WirelessDeviceId": str,
    },
)
AssociateWirelessDeviceWithMulticastGroupRequestRequestTypeDef = TypedDict(
    "AssociateWirelessDeviceWithMulticastGroupRequestRequestTypeDef",
    {
        "Id": str,
        "WirelessDeviceId": str,
    },
)
AssociateWirelessDeviceWithThingRequestRequestTypeDef = TypedDict(
    "AssociateWirelessDeviceWithThingRequestRequestTypeDef",
    {
        "Id": str,
        "ThingArn": str,
    },
)
AssociateWirelessGatewayWithCertificateRequestRequestTypeDef = TypedDict(
    "AssociateWirelessGatewayWithCertificateRequestRequestTypeDef",
    {
        "Id": str,
        "IotCertificateId": str,
    },
)
AssociateWirelessGatewayWithThingRequestRequestTypeDef = TypedDict(
    "AssociateWirelessGatewayWithThingRequestRequestTypeDef",
    {
        "Id": str,
        "ThingArn": str,
    },
)
BeaconingOutputTypeDef = TypedDict(
    "BeaconingOutputTypeDef",
    {
        "DataRate": NotRequired[int],
        "Frequencies": NotRequired[List[int]],
    },
)
BeaconingTypeDef = TypedDict(
    "BeaconingTypeDef",
    {
        "DataRate": NotRequired[int],
        "Frequencies": NotRequired[Sequence[int]],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
CancelMulticastGroupSessionRequestRequestTypeDef = TypedDict(
    "CancelMulticastGroupSessionRequestRequestTypeDef",
    {
        "Id": str,
    },
)
CdmaLocalIdTypeDef = TypedDict(
    "CdmaLocalIdTypeDef",
    {
        "PnOffset": int,
        "CdmaChannel": int,
    },
)
CdmaNmrObjTypeDef = TypedDict(
    "CdmaNmrObjTypeDef",
    {
        "PnOffset": int,
        "CdmaChannel": int,
        "PilotPower": NotRequired[int],
        "BaseStationId": NotRequired[int],
    },
)
CertificateListTypeDef = TypedDict(
    "CertificateListTypeDef",
    {
        "SigningAlg": SigningAlgType,
        "Value": str,
    },
)
LoRaWANConnectionStatusEventNotificationConfigurationsTypeDef = TypedDict(
    "LoRaWANConnectionStatusEventNotificationConfigurationsTypeDef",
    {
        "GatewayEuiEventTopic": NotRequired[EventNotificationTopicStatusType],
    },
)
LoRaWANConnectionStatusResourceTypeEventConfigurationTypeDef = TypedDict(
    "LoRaWANConnectionStatusResourceTypeEventConfigurationTypeDef",
    {
        "WirelessGatewayEventTopic": NotRequired[EventNotificationTopicStatusType],
    },
)
LoRaWANDeviceProfileTypeDef = TypedDict(
    "LoRaWANDeviceProfileTypeDef",
    {
        "SupportsClassB": NotRequired[bool],
        "ClassBTimeout": NotRequired[int],
        "PingSlotPeriod": NotRequired[int],
        "PingSlotDr": NotRequired[int],
        "PingSlotFreq": NotRequired[int],
        "SupportsClassC": NotRequired[bool],
        "ClassCTimeout": NotRequired[int],
        "MacVersion": NotRequired[str],
        "RegParamsRevision": NotRequired[str],
        "RxDelay1": NotRequired[int],
        "RxDrOffset1": NotRequired[int],
        "RxDataRate2": NotRequired[int],
        "RxFreq2": NotRequired[int],
        "FactoryPresetFreqsList": NotRequired[Sequence[int]],
        "MaxEirp": NotRequired[int],
        "MaxDutyCycle": NotRequired[int],
        "RfRegion": NotRequired[str],
        "SupportsJoin": NotRequired[bool],
        "Supports32BitFCnt": NotRequired[bool],
    },
)
LoRaWANFuotaTaskTypeDef = TypedDict(
    "LoRaWANFuotaTaskTypeDef",
    {
        "RfRegion": NotRequired[SupportedRfRegionType],
    },
)
LoRaWANMulticastTypeDef = TypedDict(
    "LoRaWANMulticastTypeDef",
    {
        "RfRegion": NotRequired[SupportedRfRegionType],
        "DlClass": NotRequired[DlClassType],
    },
)
TraceContentTypeDef = TypedDict(
    "TraceContentTypeDef",
    {
        "WirelessDeviceFrameInfo": NotRequired[WirelessDeviceFrameInfoType],
        "LogLevel": NotRequired[LogLevelType],
        "MulticastFrameInfo": NotRequired[MulticastFrameInfoType],
    },
)
LoRaWANServiceProfileTypeDef = TypedDict(
    "LoRaWANServiceProfileTypeDef",
    {
        "AddGwMetadata": NotRequired[bool],
        "DrMin": NotRequired[int],
        "DrMax": NotRequired[int],
        "PrAllowed": NotRequired[bool],
        "RaAllowed": NotRequired[bool],
    },
)
SidewalkCreateWirelessDeviceTypeDef = TypedDict(
    "SidewalkCreateWirelessDeviceTypeDef",
    {
        "DeviceProfileId": NotRequired[str],
    },
)
CreateWirelessGatewayTaskRequestRequestTypeDef = TypedDict(
    "CreateWirelessGatewayTaskRequestRequestTypeDef",
    {
        "Id": str,
        "WirelessGatewayTaskDefinitionId": str,
    },
)
DakCertificateMetadataTypeDef = TypedDict(
    "DakCertificateMetadataTypeDef",
    {
        "CertificateId": str,
        "MaxAllowedSignature": NotRequired[int],
        "FactorySupport": NotRequired[bool],
        "ApId": NotRequired[str],
        "DeviceTypeId": NotRequired[str],
    },
)
DeleteDestinationRequestRequestTypeDef = TypedDict(
    "DeleteDestinationRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteDeviceProfileRequestRequestTypeDef = TypedDict(
    "DeleteDeviceProfileRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DeleteFuotaTaskRequestRequestTypeDef = TypedDict(
    "DeleteFuotaTaskRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DeleteMulticastGroupRequestRequestTypeDef = TypedDict(
    "DeleteMulticastGroupRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DeleteNetworkAnalyzerConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteNetworkAnalyzerConfigurationRequestRequestTypeDef",
    {
        "ConfigurationName": str,
    },
)
DeleteQueuedMessagesRequestRequestTypeDef = TypedDict(
    "DeleteQueuedMessagesRequestRequestTypeDef",
    {
        "Id": str,
        "MessageId": str,
        "WirelessDeviceType": NotRequired[WirelessDeviceTypeType],
    },
)
DeleteServiceProfileRequestRequestTypeDef = TypedDict(
    "DeleteServiceProfileRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DeleteWirelessDeviceImportTaskRequestRequestTypeDef = TypedDict(
    "DeleteWirelessDeviceImportTaskRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DeleteWirelessDeviceRequestRequestTypeDef = TypedDict(
    "DeleteWirelessDeviceRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DeleteWirelessGatewayRequestRequestTypeDef = TypedDict(
    "DeleteWirelessGatewayRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DeleteWirelessGatewayTaskDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteWirelessGatewayTaskDefinitionRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DeleteWirelessGatewayTaskRequestRequestTypeDef = TypedDict(
    "DeleteWirelessGatewayTaskRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DeregisterWirelessDeviceRequestRequestTypeDef = TypedDict(
    "DeregisterWirelessDeviceRequestRequestTypeDef",
    {
        "Identifier": str,
        "WirelessDeviceType": NotRequired[WirelessDeviceTypeType],
    },
)
DestinationsTypeDef = TypedDict(
    "DestinationsTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "ExpressionType": NotRequired[ExpressionTypeType],
        "Expression": NotRequired[str],
        "Description": NotRequired[str],
        "RoleArn": NotRequired[str],
    },
)
DeviceProfileTypeDef = TypedDict(
    "DeviceProfileTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Id": NotRequired[str],
    },
)
SidewalkEventNotificationConfigurationsTypeDef = TypedDict(
    "SidewalkEventNotificationConfigurationsTypeDef",
    {
        "AmazonIdEventTopic": NotRequired[EventNotificationTopicStatusType],
    },
)
SidewalkResourceTypeEventConfigurationTypeDef = TypedDict(
    "SidewalkResourceTypeEventConfigurationTypeDef",
    {
        "WirelessDeviceEventTopic": NotRequired[EventNotificationTopicStatusType],
    },
)
DimensionTypeDef = TypedDict(
    "DimensionTypeDef",
    {
        "name": NotRequired[DimensionNameType],
        "value": NotRequired[str],
    },
)
DisassociateAwsAccountFromPartnerAccountRequestRequestTypeDef = TypedDict(
    "DisassociateAwsAccountFromPartnerAccountRequestRequestTypeDef",
    {
        "PartnerAccountId": str,
        "PartnerType": Literal["Sidewalk"],
    },
)
DisassociateMulticastGroupFromFuotaTaskRequestRequestTypeDef = TypedDict(
    "DisassociateMulticastGroupFromFuotaTaskRequestRequestTypeDef",
    {
        "Id": str,
        "MulticastGroupId": str,
    },
)
DisassociateWirelessDeviceFromFuotaTaskRequestRequestTypeDef = TypedDict(
    "DisassociateWirelessDeviceFromFuotaTaskRequestRequestTypeDef",
    {
        "Id": str,
        "WirelessDeviceId": str,
    },
)
DisassociateWirelessDeviceFromMulticastGroupRequestRequestTypeDef = TypedDict(
    "DisassociateWirelessDeviceFromMulticastGroupRequestRequestTypeDef",
    {
        "Id": str,
        "WirelessDeviceId": str,
    },
)
DisassociateWirelessDeviceFromThingRequestRequestTypeDef = TypedDict(
    "DisassociateWirelessDeviceFromThingRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DisassociateWirelessGatewayFromCertificateRequestRequestTypeDef = TypedDict(
    "DisassociateWirelessGatewayFromCertificateRequestRequestTypeDef",
    {
        "Id": str,
    },
)
DisassociateWirelessGatewayFromThingRequestRequestTypeDef = TypedDict(
    "DisassociateWirelessGatewayFromThingRequestRequestTypeDef",
    {
        "Id": str,
    },
)
PositioningTypeDef = TypedDict(
    "PositioningTypeDef",
    {
        "ClockSync": NotRequired[int],
        "Stream": NotRequired[int],
        "Gnss": NotRequired[int],
    },
)
FuotaTaskTypeDef = TypedDict(
    "FuotaTaskTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)
GatewayListItemTypeDef = TypedDict(
    "GatewayListItemTypeDef",
    {
        "GatewayId": str,
        "DownlinkFrequency": int,
    },
)
GetDestinationRequestRequestTypeDef = TypedDict(
    "GetDestinationRequestRequestTypeDef",
    {
        "Name": str,
    },
)
GetDeviceProfileRequestRequestTypeDef = TypedDict(
    "GetDeviceProfileRequestRequestTypeDef",
    {
        "Id": str,
    },
)
LoRaWANDeviceProfileOutputTypeDef = TypedDict(
    "LoRaWANDeviceProfileOutputTypeDef",
    {
        "SupportsClassB": NotRequired[bool],
        "ClassBTimeout": NotRequired[int],
        "PingSlotPeriod": NotRequired[int],
        "PingSlotDr": NotRequired[int],
        "PingSlotFreq": NotRequired[int],
        "SupportsClassC": NotRequired[bool],
        "ClassCTimeout": NotRequired[int],
        "MacVersion": NotRequired[str],
        "RegParamsRevision": NotRequired[str],
        "RxDelay1": NotRequired[int],
        "RxDrOffset1": NotRequired[int],
        "RxDataRate2": NotRequired[int],
        "RxFreq2": NotRequired[int],
        "FactoryPresetFreqsList": NotRequired[List[int]],
        "MaxEirp": NotRequired[int],
        "MaxDutyCycle": NotRequired[int],
        "RfRegion": NotRequired[str],
        "SupportsJoin": NotRequired[bool],
        "Supports32BitFCnt": NotRequired[bool],
    },
)
GetFuotaTaskRequestRequestTypeDef = TypedDict(
    "GetFuotaTaskRequestRequestTypeDef",
    {
        "Id": str,
    },
)
LoRaWANFuotaTaskGetInfoTypeDef = TypedDict(
    "LoRaWANFuotaTaskGetInfoTypeDef",
    {
        "RfRegion": NotRequired[str],
        "StartTime": NotRequired[datetime],
    },
)
SummaryMetricConfigurationTypeDef = TypedDict(
    "SummaryMetricConfigurationTypeDef",
    {
        "Status": NotRequired[SummaryMetricConfigurationStatusType],
    },
)
GetMulticastGroupRequestRequestTypeDef = TypedDict(
    "GetMulticastGroupRequestRequestTypeDef",
    {
        "Id": str,
    },
)
LoRaWANMulticastGetTypeDef = TypedDict(
    "LoRaWANMulticastGetTypeDef",
    {
        "RfRegion": NotRequired[SupportedRfRegionType],
        "DlClass": NotRequired[DlClassType],
        "NumberOfDevicesRequested": NotRequired[int],
        "NumberOfDevicesInGroup": NotRequired[int],
    },
)
GetMulticastGroupSessionRequestRequestTypeDef = TypedDict(
    "GetMulticastGroupSessionRequestRequestTypeDef",
    {
        "Id": str,
    },
)
LoRaWANMulticastSessionOutputTypeDef = TypedDict(
    "LoRaWANMulticastSessionOutputTypeDef",
    {
        "DlDr": NotRequired[int],
        "DlFreq": NotRequired[int],
        "SessionStartTime": NotRequired[datetime],
        "SessionTimeout": NotRequired[int],
        "PingSlotPeriod": NotRequired[int],
    },
)
GetNetworkAnalyzerConfigurationRequestRequestTypeDef = TypedDict(
    "GetNetworkAnalyzerConfigurationRequestRequestTypeDef",
    {
        "ConfigurationName": str,
    },
)
GetPartnerAccountRequestRequestTypeDef = TypedDict(
    "GetPartnerAccountRequestRequestTypeDef",
    {
        "PartnerAccountId": str,
        "PartnerType": Literal["Sidewalk"],
    },
)
SidewalkAccountInfoWithFingerprintTypeDef = TypedDict(
    "SidewalkAccountInfoWithFingerprintTypeDef",
    {
        "AmazonId": NotRequired[str],
        "Fingerprint": NotRequired[str],
        "Arn": NotRequired[str],
    },
)
GetPositionConfigurationRequestRequestTypeDef = TypedDict(
    "GetPositionConfigurationRequestRequestTypeDef",
    {
        "ResourceIdentifier": str,
        "ResourceType": PositionResourceTypeType,
    },
)
GnssTypeDef = TypedDict(
    "GnssTypeDef",
    {
        "Payload": str,
        "CaptureTime": NotRequired[float],
        "CaptureTimeAccuracy": NotRequired[float],
        "AssistPosition": NotRequired[Sequence[float]],
        "AssistAltitude": NotRequired[float],
        "Use2DSolver": NotRequired[bool],
    },
)
IpTypeDef = TypedDict(
    "IpTypeDef",
    {
        "IpAddress": str,
    },
)
TimestampTypeDef = Union[datetime, str]
WiFiAccessPointTypeDef = TypedDict(
    "WiFiAccessPointTypeDef",
    {
        "MacAddress": str,
        "Rss": int,
    },
)
GetPositionRequestRequestTypeDef = TypedDict(
    "GetPositionRequestRequestTypeDef",
    {
        "ResourceIdentifier": str,
        "ResourceType": PositionResourceTypeType,
    },
)
GetResourceEventConfigurationRequestRequestTypeDef = TypedDict(
    "GetResourceEventConfigurationRequestRequestTypeDef",
    {
        "Identifier": str,
        "IdentifierType": IdentifierTypeType,
        "PartnerType": NotRequired[Literal["Sidewalk"]],
    },
)
GetResourceLogLevelRequestRequestTypeDef = TypedDict(
    "GetResourceLogLevelRequestRequestTypeDef",
    {
        "ResourceIdentifier": str,
        "ResourceType": str,
    },
)
GetResourcePositionRequestRequestTypeDef = TypedDict(
    "GetResourcePositionRequestRequestTypeDef",
    {
        "ResourceIdentifier": str,
        "ResourceType": PositionResourceTypeType,
    },
)
GetServiceEndpointRequestRequestTypeDef = TypedDict(
    "GetServiceEndpointRequestRequestTypeDef",
    {
        "ServiceType": NotRequired[WirelessGatewayServiceTypeType],
    },
)
GetServiceProfileRequestRequestTypeDef = TypedDict(
    "GetServiceProfileRequestRequestTypeDef",
    {
        "Id": str,
    },
)
LoRaWANGetServiceProfileInfoTypeDef = TypedDict(
    "LoRaWANGetServiceProfileInfoTypeDef",
    {
        "UlRate": NotRequired[int],
        "UlBucketSize": NotRequired[int],
        "UlRatePolicy": NotRequired[str],
        "DlRate": NotRequired[int],
        "DlBucketSize": NotRequired[int],
        "DlRatePolicy": NotRequired[str],
        "AddGwMetadata": NotRequired[bool],
        "DevStatusReqFreq": NotRequired[int],
        "ReportDevStatusBattery": NotRequired[bool],
        "ReportDevStatusMargin": NotRequired[bool],
        "DrMin": NotRequired[int],
        "DrMax": NotRequired[int],
        "ChannelMask": NotRequired[str],
        "PrAllowed": NotRequired[bool],
        "HrAllowed": NotRequired[bool],
        "RaAllowed": NotRequired[bool],
        "NwkGeoLoc": NotRequired[bool],
        "TargetPer": NotRequired[int],
        "MinGwDiversity": NotRequired[int],
    },
)
GetWirelessDeviceImportTaskRequestRequestTypeDef = TypedDict(
    "GetWirelessDeviceImportTaskRequestRequestTypeDef",
    {
        "Id": str,
    },
)
SidewalkGetStartImportInfoTypeDef = TypedDict(
    "SidewalkGetStartImportInfoTypeDef",
    {
        "DeviceCreationFileList": NotRequired[List[str]],
        "Role": NotRequired[str],
    },
)
GetWirelessDeviceRequestRequestTypeDef = TypedDict(
    "GetWirelessDeviceRequestRequestTypeDef",
    {
        "Identifier": str,
        "IdentifierType": WirelessDeviceIdTypeType,
    },
)
GetWirelessDeviceStatisticsRequestRequestTypeDef = TypedDict(
    "GetWirelessDeviceStatisticsRequestRequestTypeDef",
    {
        "WirelessDeviceId": str,
    },
)
SidewalkDeviceMetadataTypeDef = TypedDict(
    "SidewalkDeviceMetadataTypeDef",
    {
        "Rssi": NotRequired[int],
        "BatteryLevel": NotRequired[BatteryLevelType],
        "Event": NotRequired[EventType],
        "DeviceState": NotRequired[DeviceStateType],
    },
)
GetWirelessGatewayCertificateRequestRequestTypeDef = TypedDict(
    "GetWirelessGatewayCertificateRequestRequestTypeDef",
    {
        "Id": str,
    },
)
GetWirelessGatewayFirmwareInformationRequestRequestTypeDef = TypedDict(
    "GetWirelessGatewayFirmwareInformationRequestRequestTypeDef",
    {
        "Id": str,
    },
)
GetWirelessGatewayRequestRequestTypeDef = TypedDict(
    "GetWirelessGatewayRequestRequestTypeDef",
    {
        "Identifier": str,
        "IdentifierType": WirelessGatewayIdTypeType,
    },
)
GetWirelessGatewayStatisticsRequestRequestTypeDef = TypedDict(
    "GetWirelessGatewayStatisticsRequestRequestTypeDef",
    {
        "WirelessGatewayId": str,
    },
)
GetWirelessGatewayTaskDefinitionRequestRequestTypeDef = TypedDict(
    "GetWirelessGatewayTaskDefinitionRequestRequestTypeDef",
    {
        "Id": str,
    },
)
GetWirelessGatewayTaskRequestRequestTypeDef = TypedDict(
    "GetWirelessGatewayTaskRequestRequestTypeDef",
    {
        "Id": str,
    },
)
GlobalIdentityTypeDef = TypedDict(
    "GlobalIdentityTypeDef",
    {
        "Lac": int,
        "GeranCid": int,
    },
)
GsmLocalIdTypeDef = TypedDict(
    "GsmLocalIdTypeDef",
    {
        "Bsic": int,
        "Bcch": int,
    },
)
ImportedSidewalkDeviceTypeDef = TypedDict(
    "ImportedSidewalkDeviceTypeDef",
    {
        "SidewalkManufacturingSn": NotRequired[str],
        "OnboardingStatus": NotRequired[OnboardStatusType],
        "OnboardingStatusReason": NotRequired[str],
        "LastUpdateTime": NotRequired[datetime],
    },
)
LoRaWANJoinEventNotificationConfigurationsTypeDef = TypedDict(
    "LoRaWANJoinEventNotificationConfigurationsTypeDef",
    {
        "DevEuiEventTopic": NotRequired[EventNotificationTopicStatusType],
    },
)
LoRaWANJoinResourceTypeEventConfigurationTypeDef = TypedDict(
    "LoRaWANJoinResourceTypeEventConfigurationTypeDef",
    {
        "WirelessDeviceEventTopic": NotRequired[EventNotificationTopicStatusType],
    },
)
ListDestinationsRequestRequestTypeDef = TypedDict(
    "ListDestinationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListDeviceProfilesRequestRequestTypeDef = TypedDict(
    "ListDeviceProfilesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "DeviceProfileType": NotRequired[DeviceProfileTypeType],
    },
)
ListDevicesForWirelessDeviceImportTaskRequestRequestTypeDef = TypedDict(
    "ListDevicesForWirelessDeviceImportTaskRequestRequestTypeDef",
    {
        "Id": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Status": NotRequired[OnboardStatusType],
    },
)
ListEventConfigurationsRequestRequestTypeDef = TypedDict(
    "ListEventConfigurationsRequestRequestTypeDef",
    {
        "ResourceType": EventNotificationResourceTypeType,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListFuotaTasksRequestRequestTypeDef = TypedDict(
    "ListFuotaTasksRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListMulticastGroupsByFuotaTaskRequestRequestTypeDef = TypedDict(
    "ListMulticastGroupsByFuotaTaskRequestRequestTypeDef",
    {
        "Id": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
MulticastGroupByFuotaTaskTypeDef = TypedDict(
    "MulticastGroupByFuotaTaskTypeDef",
    {
        "Id": NotRequired[str],
    },
)
ListMulticastGroupsRequestRequestTypeDef = TypedDict(
    "ListMulticastGroupsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
MulticastGroupTypeDef = TypedDict(
    "MulticastGroupTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)
ListNetworkAnalyzerConfigurationsRequestRequestTypeDef = TypedDict(
    "ListNetworkAnalyzerConfigurationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
NetworkAnalyzerConfigurationsTypeDef = TypedDict(
    "NetworkAnalyzerConfigurationsTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)
ListPartnerAccountsRequestRequestTypeDef = TypedDict(
    "ListPartnerAccountsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListPositionConfigurationsRequestRequestTypeDef = TypedDict(
    "ListPositionConfigurationsRequestRequestTypeDef",
    {
        "ResourceType": NotRequired[PositionResourceTypeType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListQueuedMessagesRequestRequestTypeDef = TypedDict(
    "ListQueuedMessagesRequestRequestTypeDef",
    {
        "Id": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "WirelessDeviceType": NotRequired[WirelessDeviceTypeType],
    },
)
ListServiceProfilesRequestRequestTypeDef = TypedDict(
    "ListServiceProfilesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ServiceProfileTypeDef = TypedDict(
    "ServiceProfileTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Id": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
ListWirelessDeviceImportTasksRequestRequestTypeDef = TypedDict(
    "ListWirelessDeviceImportTasksRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListWirelessDevicesRequestRequestTypeDef = TypedDict(
    "ListWirelessDevicesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DestinationName": NotRequired[str],
        "DeviceProfileId": NotRequired[str],
        "ServiceProfileId": NotRequired[str],
        "WirelessDeviceType": NotRequired[WirelessDeviceTypeType],
        "FuotaTaskId": NotRequired[str],
        "MulticastGroupId": NotRequired[str],
    },
)
ListWirelessGatewayTaskDefinitionsRequestRequestTypeDef = TypedDict(
    "ListWirelessGatewayTaskDefinitionsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "TaskDefinitionType": NotRequired[Literal["UPDATE"]],
    },
)
ListWirelessGatewaysRequestRequestTypeDef = TypedDict(
    "ListWirelessGatewaysRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
LoRaWANGatewayMetadataTypeDef = TypedDict(
    "LoRaWANGatewayMetadataTypeDef",
    {
        "GatewayEui": NotRequired[str],
        "Snr": NotRequired[float],
        "Rssi": NotRequired[float],
    },
)
LoRaWANPublicGatewayMetadataTypeDef = TypedDict(
    "LoRaWANPublicGatewayMetadataTypeDef",
    {
        "ProviderNetId": NotRequired[str],
        "Id": NotRequired[str],
        "Rssi": NotRequired[float],
        "Snr": NotRequired[float],
        "RfRegion": NotRequired[str],
        "DlAllowed": NotRequired[bool],
    },
)
OtaaV10XTypeDef = TypedDict(
    "OtaaV10XTypeDef",
    {
        "AppKey": NotRequired[str],
        "AppEui": NotRequired[str],
        "JoinEui": NotRequired[str],
        "GenAppKey": NotRequired[str],
    },
)
OtaaV11TypeDef = TypedDict(
    "OtaaV11TypeDef",
    {
        "AppKey": NotRequired[str],
        "NwkKey": NotRequired[str],
        "JoinEui": NotRequired[str],
    },
)
LoRaWANGatewayVersionTypeDef = TypedDict(
    "LoRaWANGatewayVersionTypeDef",
    {
        "PackageVersion": NotRequired[str],
        "Model": NotRequired[str],
        "Station": NotRequired[str],
    },
)
LoRaWANListDeviceTypeDef = TypedDict(
    "LoRaWANListDeviceTypeDef",
    {
        "DevEui": NotRequired[str],
    },
)
LoRaWANMulticastMetadataTypeDef = TypedDict(
    "LoRaWANMulticastMetadataTypeDef",
    {
        "FPort": NotRequired[int],
    },
)
UpdateAbpV10XTypeDef = TypedDict(
    "UpdateAbpV10XTypeDef",
    {
        "FCntStart": NotRequired[int],
    },
)
UpdateAbpV11TypeDef = TypedDict(
    "UpdateAbpV11TypeDef",
    {
        "FCntStart": NotRequired[int],
    },
)
LteLocalIdTypeDef = TypedDict(
    "LteLocalIdTypeDef",
    {
        "Pci": int,
        "Earfcn": int,
    },
)
LteNmrObjTypeDef = TypedDict(
    "LteNmrObjTypeDef",
    {
        "Pci": int,
        "Earfcn": int,
        "EutranCid": int,
        "Rsrp": NotRequired[int],
        "Rsrq": NotRequired[float],
    },
)
MetricQueryValueTypeDef = TypedDict(
    "MetricQueryValueTypeDef",
    {
        "Min": NotRequired[float],
        "Max": NotRequired[float],
        "Sum": NotRequired[float],
        "Avg": NotRequired[float],
        "Std": NotRequired[float],
        "P90": NotRequired[float],
    },
)
SemtechGnssConfigurationTypeDef = TypedDict(
    "SemtechGnssConfigurationTypeDef",
    {
        "Status": PositionConfigurationStatusType,
        "Fec": PositionConfigurationFecType,
    },
)
SemtechGnssDetailTypeDef = TypedDict(
    "SemtechGnssDetailTypeDef",
    {
        "Provider": NotRequired[Literal["Semtech"]],
        "Type": NotRequired[Literal["GNSS"]],
        "Status": NotRequired[PositionConfigurationStatusType],
        "Fec": NotRequired[PositionConfigurationFecType],
    },
)
PutResourceLogLevelRequestRequestTypeDef = TypedDict(
    "PutResourceLogLevelRequestRequestTypeDef",
    {
        "ResourceIdentifier": str,
        "ResourceType": str,
        "LogLevel": LogLevelType,
    },
)
ResetResourceLogLevelRequestRequestTypeDef = TypedDict(
    "ResetResourceLogLevelRequestRequestTypeDef",
    {
        "ResourceIdentifier": str,
        "ResourceType": str,
    },
)
SidewalkSendDataToDeviceTypeDef = TypedDict(
    "SidewalkSendDataToDeviceTypeDef",
    {
        "Seq": NotRequired[int],
        "MessageType": NotRequired[MessageTypeType],
        "AckModeRetryDurationSecs": NotRequired[int],
    },
)
SidewalkSingleStartImportInfoTypeDef = TypedDict(
    "SidewalkSingleStartImportInfoTypeDef",
    {
        "SidewalkManufacturingSn": NotRequired[str],
    },
)
SidewalkStartImportInfoTypeDef = TypedDict(
    "SidewalkStartImportInfoTypeDef",
    {
        "DeviceCreationFile": NotRequired[str],
        "Role": NotRequired[str],
    },
)
SidewalkUpdateAccountTypeDef = TypedDict(
    "SidewalkUpdateAccountTypeDef",
    {
        "AppServerPrivateKey": NotRequired[str],
    },
)
SidewalkUpdateImportInfoTypeDef = TypedDict(
    "SidewalkUpdateImportInfoTypeDef",
    {
        "DeviceCreationFile": NotRequired[str],
    },
)
TdscdmaLocalIdTypeDef = TypedDict(
    "TdscdmaLocalIdTypeDef",
    {
        "Uarfcn": int,
        "CellParams": int,
    },
)
TdscdmaNmrObjTypeDef = TypedDict(
    "TdscdmaNmrObjTypeDef",
    {
        "Uarfcn": int,
        "CellParams": int,
        "UtranCid": NotRequired[int],
        "Rscp": NotRequired[int],
        "PathLoss": NotRequired[int],
    },
)
TestWirelessDeviceRequestRequestTypeDef = TypedDict(
    "TestWirelessDeviceRequestRequestTypeDef",
    {
        "Id": str,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateDestinationRequestRequestTypeDef = TypedDict(
    "UpdateDestinationRequestRequestTypeDef",
    {
        "Name": str,
        "ExpressionType": NotRequired[ExpressionTypeType],
        "Expression": NotRequired[str],
        "Description": NotRequired[str],
        "RoleArn": NotRequired[str],
    },
)
UpdatePositionRequestRequestTypeDef = TypedDict(
    "UpdatePositionRequestRequestTypeDef",
    {
        "ResourceIdentifier": str,
        "ResourceType": PositionResourceTypeType,
        "Position": Sequence[float],
    },
)
UpdateWirelessGatewayRequestRequestTypeDef = TypedDict(
    "UpdateWirelessGatewayRequestRequestTypeDef",
    {
        "Id": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "JoinEuiFilters": NotRequired[Sequence[Sequence[str]]],
        "NetIdFilters": NotRequired[Sequence[str]],
        "MaxEirp": NotRequired[float],
    },
)
WcdmaLocalIdTypeDef = TypedDict(
    "WcdmaLocalIdTypeDef",
    {
        "Uarfcndl": int,
        "Psc": int,
    },
)
WcdmaNmrObjTypeDef = TypedDict(
    "WcdmaNmrObjTypeDef",
    {
        "Uarfcndl": int,
        "Psc": int,
        "UtranCid": int,
        "Rscp": NotRequired[int],
        "PathLoss": NotRequired[int],
    },
)
WirelessDeviceEventLogOptionTypeDef = TypedDict(
    "WirelessDeviceEventLogOptionTypeDef",
    {
        "Event": WirelessDeviceEventType,
        "LogLevel": LogLevelType,
    },
)
WirelessGatewayEventLogOptionTypeDef = TypedDict(
    "WirelessGatewayEventLogOptionTypeDef",
    {
        "Event": WirelessGatewayEventType,
        "LogLevel": LogLevelType,
    },
)
AbpV10XTypeDef = TypedDict(
    "AbpV10XTypeDef",
    {
        "DevAddr": NotRequired[str],
        "SessionKeys": NotRequired[SessionKeysAbpV10XTypeDef],
        "FCntStart": NotRequired[int],
    },
)
AbpV11TypeDef = TypedDict(
    "AbpV11TypeDef",
    {
        "DevAddr": NotRequired[str],
        "SessionKeys": NotRequired[SessionKeysAbpV11TypeDef],
        "FCntStart": NotRequired[int],
    },
)
AssociateAwsAccountWithPartnerAccountRequestRequestTypeDef = TypedDict(
    "AssociateAwsAccountWithPartnerAccountRequestRequestTypeDef",
    {
        "Sidewalk": SidewalkAccountInfoTypeDef,
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateDestinationRequestRequestTypeDef = TypedDict(
    "CreateDestinationRequestRequestTypeDef",
    {
        "Name": str,
        "ExpressionType": ExpressionTypeType,
        "Expression": str,
        "RoleArn": str,
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ClientRequestToken": NotRequired[str],
    },
)
StartBulkAssociateWirelessDeviceWithMulticastGroupRequestRequestTypeDef = TypedDict(
    "StartBulkAssociateWirelessDeviceWithMulticastGroupRequestRequestTypeDef",
    {
        "Id": str,
        "QueryString": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
StartBulkDisassociateWirelessDeviceFromMulticastGroupRequestRequestTypeDef = TypedDict(
    "StartBulkDisassociateWirelessDeviceFromMulticastGroupRequestRequestTypeDef",
    {
        "Id": str,
        "QueryString": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
AssociateAwsAccountWithPartnerAccountResponseTypeDef = TypedDict(
    "AssociateAwsAccountWithPartnerAccountResponseTypeDef",
    {
        "Sidewalk": SidewalkAccountInfoTypeDef,
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateWirelessGatewayWithCertificateResponseTypeDef = TypedDict(
    "AssociateWirelessGatewayWithCertificateResponseTypeDef",
    {
        "IotCertificateId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDestinationResponseTypeDef = TypedDict(
    "CreateDestinationResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDeviceProfileResponseTypeDef = TypedDict(
    "CreateDeviceProfileResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFuotaTaskResponseTypeDef = TypedDict(
    "CreateFuotaTaskResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMulticastGroupResponseTypeDef = TypedDict(
    "CreateMulticastGroupResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateNetworkAnalyzerConfigurationResponseTypeDef = TypedDict(
    "CreateNetworkAnalyzerConfigurationResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateServiceProfileResponseTypeDef = TypedDict(
    "CreateServiceProfileResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWirelessDeviceResponseTypeDef = TypedDict(
    "CreateWirelessDeviceResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWirelessGatewayResponseTypeDef = TypedDict(
    "CreateWirelessGatewayResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWirelessGatewayTaskDefinitionResponseTypeDef = TypedDict(
    "CreateWirelessGatewayTaskDefinitionResponseTypeDef",
    {
        "Id": str,
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWirelessGatewayTaskResponseTypeDef = TypedDict(
    "CreateWirelessGatewayTaskResponseTypeDef",
    {
        "WirelessGatewayTaskDefinitionId": str,
        "Status": WirelessGatewayTaskStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDestinationResponseTypeDef = TypedDict(
    "GetDestinationResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Expression": str,
        "ExpressionType": ExpressionTypeType,
        "Description": str,
        "RoleArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPositionEstimateResponseTypeDef = TypedDict(
    "GetPositionEstimateResponseTypeDef",
    {
        "GeoJsonPayload": StreamingBody,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPositionResponseTypeDef = TypedDict(
    "GetPositionResponseTypeDef",
    {
        "Position": List[float],
        "Accuracy": AccuracyTypeDef,
        "SolverType": Literal["GNSS"],
        "SolverProvider": Literal["Semtech"],
        "SolverVersion": str,
        "Timestamp": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResourceLogLevelResponseTypeDef = TypedDict(
    "GetResourceLogLevelResponseTypeDef",
    {
        "LogLevel": LogLevelType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResourcePositionResponseTypeDef = TypedDict(
    "GetResourcePositionResponseTypeDef",
    {
        "GeoJsonPayload": StreamingBody,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServiceEndpointResponseTypeDef = TypedDict(
    "GetServiceEndpointResponseTypeDef",
    {
        "ServiceType": WirelessGatewayServiceTypeType,
        "ServiceEndpoint": str,
        "ServerTrust": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetWirelessGatewayCertificateResponseTypeDef = TypedDict(
    "GetWirelessGatewayCertificateResponseTypeDef",
    {
        "IotCertificateId": str,
        "LoRaWANNetworkServerCertificateId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetWirelessGatewayStatisticsResponseTypeDef = TypedDict(
    "GetWirelessGatewayStatisticsResponseTypeDef",
    {
        "WirelessGatewayId": str,
        "LastUplinkReceivedAt": str,
        "ConnectionStatus": ConnectionStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetWirelessGatewayTaskResponseTypeDef = TypedDict(
    "GetWirelessGatewayTaskResponseTypeDef",
    {
        "WirelessGatewayId": str,
        "WirelessGatewayTaskDefinitionId": str,
        "LastUplinkReceivedAt": str,
        "TaskCreatedAt": str,
        "Status": WirelessGatewayTaskStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendDataToMulticastGroupResponseTypeDef = TypedDict(
    "SendDataToMulticastGroupResponseTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendDataToWirelessDeviceResponseTypeDef = TypedDict(
    "SendDataToWirelessDeviceResponseTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartSingleWirelessDeviceImportTaskResponseTypeDef = TypedDict(
    "StartSingleWirelessDeviceImportTaskResponseTypeDef",
    {
        "Id": str,
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartWirelessDeviceImportTaskResponseTypeDef = TypedDict(
    "StartWirelessDeviceImportTaskResponseTypeDef",
    {
        "Id": str,
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TestWirelessDeviceResponseTypeDef = TypedDict(
    "TestWirelessDeviceResponseTypeDef",
    {
        "Result": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LoRaWANGatewayOutputTypeDef = TypedDict(
    "LoRaWANGatewayOutputTypeDef",
    {
        "GatewayEui": NotRequired[str],
        "RfRegion": NotRequired[str],
        "JoinEuiFilters": NotRequired[List[List[str]]],
        "NetIdFilters": NotRequired[List[str]],
        "SubBands": NotRequired[List[int]],
        "Beaconing": NotRequired[BeaconingOutputTypeDef],
        "MaxEirp": NotRequired[float],
    },
)
BeaconingUnionTypeDef = Union[BeaconingTypeDef, BeaconingOutputTypeDef]
UpdateResourcePositionRequestRequestTypeDef = TypedDict(
    "UpdateResourcePositionRequestRequestTypeDef",
    {
        "ResourceIdentifier": str,
        "ResourceType": PositionResourceTypeType,
        "GeoJsonPayload": NotRequired[BlobTypeDef],
    },
)
CdmaObjTypeDef = TypedDict(
    "CdmaObjTypeDef",
    {
        "SystemId": int,
        "NetworkId": int,
        "BaseStationId": int,
        "RegistrationZone": NotRequired[int],
        "CdmaLocalId": NotRequired[CdmaLocalIdTypeDef],
        "PilotPower": NotRequired[int],
        "BaseLat": NotRequired[float],
        "BaseLng": NotRequired[float],
        "CdmaNmr": NotRequired[Sequence[CdmaNmrObjTypeDef]],
    },
)
SidewalkDeviceTypeDef = TypedDict(
    "SidewalkDeviceTypeDef",
    {
        "AmazonId": NotRequired[str],
        "SidewalkId": NotRequired[str],
        "SidewalkManufacturingSn": NotRequired[str],
        "DeviceCertificates": NotRequired[List[CertificateListTypeDef]],
        "PrivateKeys": NotRequired[List[CertificateListTypeDef]],
        "DeviceProfileId": NotRequired[str],
        "CertificateId": NotRequired[str],
        "Status": NotRequired[WirelessDeviceSidewalkStatusType],
    },
)
SidewalkListDeviceTypeDef = TypedDict(
    "SidewalkListDeviceTypeDef",
    {
        "AmazonId": NotRequired[str],
        "SidewalkId": NotRequired[str],
        "SidewalkManufacturingSn": NotRequired[str],
        "DeviceCertificates": NotRequired[List[CertificateListTypeDef]],
        "DeviceProfileId": NotRequired[str],
        "Status": NotRequired[WirelessDeviceSidewalkStatusType],
    },
)
ConnectionStatusEventConfigurationTypeDef = TypedDict(
    "ConnectionStatusEventConfigurationTypeDef",
    {
        "LoRaWAN": NotRequired[LoRaWANConnectionStatusEventNotificationConfigurationsTypeDef],
        "WirelessGatewayIdEventTopic": NotRequired[EventNotificationTopicStatusType],
    },
)
ConnectionStatusResourceTypeEventConfigurationTypeDef = TypedDict(
    "ConnectionStatusResourceTypeEventConfigurationTypeDef",
    {
        "LoRaWAN": NotRequired[LoRaWANConnectionStatusResourceTypeEventConfigurationTypeDef],
    },
)
CreateDeviceProfileRequestRequestTypeDef = TypedDict(
    "CreateDeviceProfileRequestRequestTypeDef",
    {
        "Name": NotRequired[str],
        "LoRaWAN": NotRequired[LoRaWANDeviceProfileTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ClientRequestToken": NotRequired[str],
        "Sidewalk": NotRequired[Mapping[str, Any]],
    },
)
CreateFuotaTaskRequestRequestTypeDef = TypedDict(
    "CreateFuotaTaskRequestRequestTypeDef",
    {
        "FirmwareUpdateImage": str,
        "FirmwareUpdateRole": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "LoRaWAN": NotRequired[LoRaWANFuotaTaskTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "RedundancyPercent": NotRequired[int],
        "FragmentSizeBytes": NotRequired[int],
        "FragmentIntervalMS": NotRequired[int],
    },
)
UpdateFuotaTaskRequestRequestTypeDef = TypedDict(
    "UpdateFuotaTaskRequestRequestTypeDef",
    {
        "Id": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "LoRaWAN": NotRequired[LoRaWANFuotaTaskTypeDef],
        "FirmwareUpdateImage": NotRequired[str],
        "FirmwareUpdateRole": NotRequired[str],
        "RedundancyPercent": NotRequired[int],
        "FragmentSizeBytes": NotRequired[int],
        "FragmentIntervalMS": NotRequired[int],
    },
)
CreateMulticastGroupRequestRequestTypeDef = TypedDict(
    "CreateMulticastGroupRequestRequestTypeDef",
    {
        "LoRaWAN": LoRaWANMulticastTypeDef,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
UpdateMulticastGroupRequestRequestTypeDef = TypedDict(
    "UpdateMulticastGroupRequestRequestTypeDef",
    {
        "Id": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "LoRaWAN": NotRequired[LoRaWANMulticastTypeDef],
    },
)
CreateNetworkAnalyzerConfigurationRequestRequestTypeDef = TypedDict(
    "CreateNetworkAnalyzerConfigurationRequestRequestTypeDef",
    {
        "Name": str,
        "TraceContent": NotRequired[TraceContentTypeDef],
        "WirelessDevices": NotRequired[Sequence[str]],
        "WirelessGateways": NotRequired[Sequence[str]],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ClientRequestToken": NotRequired[str],
        "MulticastGroups": NotRequired[Sequence[str]],
    },
)
GetNetworkAnalyzerConfigurationResponseTypeDef = TypedDict(
    "GetNetworkAnalyzerConfigurationResponseTypeDef",
    {
        "TraceContent": TraceContentTypeDef,
        "WirelessDevices": List[str],
        "WirelessGateways": List[str],
        "Description": str,
        "Arn": str,
        "Name": str,
        "MulticastGroups": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateNetworkAnalyzerConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateNetworkAnalyzerConfigurationRequestRequestTypeDef",
    {
        "ConfigurationName": str,
        "TraceContent": NotRequired[TraceContentTypeDef],
        "WirelessDevicesToAdd": NotRequired[Sequence[str]],
        "WirelessDevicesToRemove": NotRequired[Sequence[str]],
        "WirelessGatewaysToAdd": NotRequired[Sequence[str]],
        "WirelessGatewaysToRemove": NotRequired[Sequence[str]],
        "Description": NotRequired[str],
        "MulticastGroupsToAdd": NotRequired[Sequence[str]],
        "MulticastGroupsToRemove": NotRequired[Sequence[str]],
    },
)
CreateServiceProfileRequestRequestTypeDef = TypedDict(
    "CreateServiceProfileRequestRequestTypeDef",
    {
        "Name": NotRequired[str],
        "LoRaWAN": NotRequired[LoRaWANServiceProfileTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ClientRequestToken": NotRequired[str],
    },
)
SidewalkGetDeviceProfileTypeDef = TypedDict(
    "SidewalkGetDeviceProfileTypeDef",
    {
        "ApplicationServerPublicKey": NotRequired[str],
        "QualificationStatus": NotRequired[bool],
        "DakCertificateMetadata": NotRequired[List[DakCertificateMetadataTypeDef]],
    },
)
ListDestinationsResponseTypeDef = TypedDict(
    "ListDestinationsResponseTypeDef",
    {
        "DestinationList": List[DestinationsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListDeviceProfilesResponseTypeDef = TypedDict(
    "ListDeviceProfilesResponseTypeDef",
    {
        "DeviceProfileList": List[DeviceProfileTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DeviceRegistrationStateEventConfigurationTypeDef = TypedDict(
    "DeviceRegistrationStateEventConfigurationTypeDef",
    {
        "Sidewalk": NotRequired[SidewalkEventNotificationConfigurationsTypeDef],
        "WirelessDeviceIdEventTopic": NotRequired[EventNotificationTopicStatusType],
    },
)
MessageDeliveryStatusEventConfigurationTypeDef = TypedDict(
    "MessageDeliveryStatusEventConfigurationTypeDef",
    {
        "Sidewalk": NotRequired[SidewalkEventNotificationConfigurationsTypeDef],
        "WirelessDeviceIdEventTopic": NotRequired[EventNotificationTopicStatusType],
    },
)
ProximityEventConfigurationTypeDef = TypedDict(
    "ProximityEventConfigurationTypeDef",
    {
        "Sidewalk": NotRequired[SidewalkEventNotificationConfigurationsTypeDef],
        "WirelessDeviceIdEventTopic": NotRequired[EventNotificationTopicStatusType],
    },
)
DeviceRegistrationStateResourceTypeEventConfigurationTypeDef = TypedDict(
    "DeviceRegistrationStateResourceTypeEventConfigurationTypeDef",
    {
        "Sidewalk": NotRequired[SidewalkResourceTypeEventConfigurationTypeDef],
    },
)
MessageDeliveryStatusResourceTypeEventConfigurationTypeDef = TypedDict(
    "MessageDeliveryStatusResourceTypeEventConfigurationTypeDef",
    {
        "Sidewalk": NotRequired[SidewalkResourceTypeEventConfigurationTypeDef],
    },
)
ProximityResourceTypeEventConfigurationTypeDef = TypedDict(
    "ProximityResourceTypeEventConfigurationTypeDef",
    {
        "Sidewalk": NotRequired[SidewalkResourceTypeEventConfigurationTypeDef],
    },
)
FPortsOutputTypeDef = TypedDict(
    "FPortsOutputTypeDef",
    {
        "Fuota": NotRequired[int],
        "Multicast": NotRequired[int],
        "ClockSync": NotRequired[int],
        "Positioning": NotRequired[PositioningTypeDef],
        "Applications": NotRequired[List[ApplicationConfigTypeDef]],
    },
)
FPortsTypeDef = TypedDict(
    "FPortsTypeDef",
    {
        "Fuota": NotRequired[int],
        "Multicast": NotRequired[int],
        "ClockSync": NotRequired[int],
        "Positioning": NotRequired[PositioningTypeDef],
        "Applications": NotRequired[Sequence[ApplicationConfigTypeDef]],
    },
)
UpdateFPortsTypeDef = TypedDict(
    "UpdateFPortsTypeDef",
    {
        "Positioning": NotRequired[PositioningTypeDef],
        "Applications": NotRequired[Sequence[ApplicationConfigTypeDef]],
    },
)
ListFuotaTasksResponseTypeDef = TypedDict(
    "ListFuotaTasksResponseTypeDef",
    {
        "FuotaTaskList": List[FuotaTaskTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ParticipatingGatewaysOutputTypeDef = TypedDict(
    "ParticipatingGatewaysOutputTypeDef",
    {
        "DownlinkMode": DownlinkModeType,
        "GatewayList": List[GatewayListItemTypeDef],
        "TransmissionInterval": int,
    },
)
ParticipatingGatewaysTypeDef = TypedDict(
    "ParticipatingGatewaysTypeDef",
    {
        "DownlinkMode": DownlinkModeType,
        "GatewayList": Sequence[GatewayListItemTypeDef],
        "TransmissionInterval": int,
    },
)
GetFuotaTaskResponseTypeDef = TypedDict(
    "GetFuotaTaskResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Status": FuotaTaskStatusType,
        "Name": str,
        "Description": str,
        "LoRaWAN": LoRaWANFuotaTaskGetInfoTypeDef,
        "FirmwareUpdateImage": str,
        "FirmwareUpdateRole": str,
        "CreatedAt": datetime,
        "RedundancyPercent": int,
        "FragmentSizeBytes": int,
        "FragmentIntervalMS": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMetricConfigurationResponseTypeDef = TypedDict(
    "GetMetricConfigurationResponseTypeDef",
    {
        "SummaryMetric": SummaryMetricConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateMetricConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateMetricConfigurationRequestRequestTypeDef",
    {
        "SummaryMetric": NotRequired[SummaryMetricConfigurationTypeDef],
    },
)
GetMulticastGroupResponseTypeDef = TypedDict(
    "GetMulticastGroupResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "Status": str,
        "LoRaWAN": LoRaWANMulticastGetTypeDef,
        "CreatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMulticastGroupSessionResponseTypeDef = TypedDict(
    "GetMulticastGroupSessionResponseTypeDef",
    {
        "LoRaWAN": LoRaWANMulticastSessionOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPartnerAccountResponseTypeDef = TypedDict(
    "GetPartnerAccountResponseTypeDef",
    {
        "Sidewalk": SidewalkAccountInfoWithFingerprintTypeDef,
        "AccountLinked": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPartnerAccountsResponseTypeDef = TypedDict(
    "ListPartnerAccountsResponseTypeDef",
    {
        "Sidewalk": List[SidewalkAccountInfoWithFingerprintTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
LoRaWANMulticastSessionTypeDef = TypedDict(
    "LoRaWANMulticastSessionTypeDef",
    {
        "DlDr": NotRequired[int],
        "DlFreq": NotRequired[int],
        "SessionStartTime": NotRequired[TimestampTypeDef],
        "SessionTimeout": NotRequired[int],
        "PingSlotPeriod": NotRequired[int],
    },
)
LoRaWANStartFuotaTaskTypeDef = TypedDict(
    "LoRaWANStartFuotaTaskTypeDef",
    {
        "StartTime": NotRequired[TimestampTypeDef],
    },
)
SummaryMetricQueryTypeDef = TypedDict(
    "SummaryMetricQueryTypeDef",
    {
        "QueryId": NotRequired[str],
        "MetricName": NotRequired[MetricNameType],
        "Dimensions": NotRequired[Sequence[DimensionTypeDef]],
        "AggregationPeriod": NotRequired[AggregationPeriodType],
        "StartTimestamp": NotRequired[TimestampTypeDef],
        "EndTimestamp": NotRequired[TimestampTypeDef],
    },
)
GetServiceProfileResponseTypeDef = TypedDict(
    "GetServiceProfileResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Id": str,
        "LoRaWAN": LoRaWANGetServiceProfileInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetWirelessDeviceImportTaskResponseTypeDef = TypedDict(
    "GetWirelessDeviceImportTaskResponseTypeDef",
    {
        "Id": str,
        "Arn": str,
        "DestinationName": str,
        "Sidewalk": SidewalkGetStartImportInfoTypeDef,
        "CreationTime": datetime,
        "Status": ImportTaskStatusType,
        "StatusReason": str,
        "InitializedImportedDeviceCount": int,
        "PendingImportedDeviceCount": int,
        "OnboardedImportedDeviceCount": int,
        "FailedImportedDeviceCount": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
WirelessDeviceImportTaskTypeDef = TypedDict(
    "WirelessDeviceImportTaskTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "DestinationName": NotRequired[str],
        "Sidewalk": NotRequired[SidewalkGetStartImportInfoTypeDef],
        "CreationTime": NotRequired[datetime],
        "Status": NotRequired[ImportTaskStatusType],
        "StatusReason": NotRequired[str],
        "InitializedImportedDeviceCount": NotRequired[int],
        "PendingImportedDeviceCount": NotRequired[int],
        "OnboardedImportedDeviceCount": NotRequired[int],
        "FailedImportedDeviceCount": NotRequired[int],
    },
)
GsmNmrObjTypeDef = TypedDict(
    "GsmNmrObjTypeDef",
    {
        "Bsic": int,
        "Bcch": int,
        "RxLevel": NotRequired[int],
        "GlobalIdentity": NotRequired[GlobalIdentityTypeDef],
    },
)
ImportedWirelessDeviceTypeDef = TypedDict(
    "ImportedWirelessDeviceTypeDef",
    {
        "Sidewalk": NotRequired[ImportedSidewalkDeviceTypeDef],
    },
)
JoinEventConfigurationTypeDef = TypedDict(
    "JoinEventConfigurationTypeDef",
    {
        "LoRaWAN": NotRequired[LoRaWANJoinEventNotificationConfigurationsTypeDef],
        "WirelessDeviceIdEventTopic": NotRequired[EventNotificationTopicStatusType],
    },
)
JoinResourceTypeEventConfigurationTypeDef = TypedDict(
    "JoinResourceTypeEventConfigurationTypeDef",
    {
        "LoRaWAN": NotRequired[LoRaWANJoinResourceTypeEventConfigurationTypeDef],
    },
)
ListMulticastGroupsByFuotaTaskResponseTypeDef = TypedDict(
    "ListMulticastGroupsByFuotaTaskResponseTypeDef",
    {
        "MulticastGroupList": List[MulticastGroupByFuotaTaskTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListMulticastGroupsResponseTypeDef = TypedDict(
    "ListMulticastGroupsResponseTypeDef",
    {
        "MulticastGroupList": List[MulticastGroupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListNetworkAnalyzerConfigurationsResponseTypeDef = TypedDict(
    "ListNetworkAnalyzerConfigurationsResponseTypeDef",
    {
        "NetworkAnalyzerConfigurationList": List[NetworkAnalyzerConfigurationsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListServiceProfilesResponseTypeDef = TypedDict(
    "ListServiceProfilesResponseTypeDef",
    {
        "ServiceProfileList": List[ServiceProfileTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
LoRaWANDeviceMetadataTypeDef = TypedDict(
    "LoRaWANDeviceMetadataTypeDef",
    {
        "DevEui": NotRequired[str],
        "FPort": NotRequired[int],
        "DataRate": NotRequired[int],
        "Frequency": NotRequired[int],
        "Timestamp": NotRequired[str],
        "Gateways": NotRequired[List[LoRaWANGatewayMetadataTypeDef]],
        "PublicGateways": NotRequired[List[LoRaWANPublicGatewayMetadataTypeDef]],
    },
)
LoRaWANGatewayCurrentVersionTypeDef = TypedDict(
    "LoRaWANGatewayCurrentVersionTypeDef",
    {
        "CurrentVersion": NotRequired[LoRaWANGatewayVersionTypeDef],
    },
)
LoRaWANUpdateGatewayTaskCreateTypeDef = TypedDict(
    "LoRaWANUpdateGatewayTaskCreateTypeDef",
    {
        "UpdateSignature": NotRequired[str],
        "SigKeyCrc": NotRequired[int],
        "CurrentVersion": NotRequired[LoRaWANGatewayVersionTypeDef],
        "UpdateVersion": NotRequired[LoRaWANGatewayVersionTypeDef],
    },
)
LoRaWANUpdateGatewayTaskEntryTypeDef = TypedDict(
    "LoRaWANUpdateGatewayTaskEntryTypeDef",
    {
        "CurrentVersion": NotRequired[LoRaWANGatewayVersionTypeDef],
        "UpdateVersion": NotRequired[LoRaWANGatewayVersionTypeDef],
    },
)
MulticastWirelessMetadataTypeDef = TypedDict(
    "MulticastWirelessMetadataTypeDef",
    {
        "LoRaWAN": NotRequired[LoRaWANMulticastMetadataTypeDef],
    },
)
LteObjTypeDef = TypedDict(
    "LteObjTypeDef",
    {
        "Mcc": int,
        "Mnc": int,
        "EutranCid": int,
        "Tac": NotRequired[int],
        "LteLocalId": NotRequired[LteLocalIdTypeDef],
        "LteTimingAdvance": NotRequired[int],
        "Rsrp": NotRequired[int],
        "Rsrq": NotRequired[float],
        "NrCapable": NotRequired[bool],
        "LteNmr": NotRequired[Sequence[LteNmrObjTypeDef]],
    },
)
SummaryMetricQueryResultTypeDef = TypedDict(
    "SummaryMetricQueryResultTypeDef",
    {
        "QueryId": NotRequired[str],
        "QueryStatus": NotRequired[MetricQueryStatusType],
        "Error": NotRequired[str],
        "MetricName": NotRequired[MetricNameType],
        "Dimensions": NotRequired[List[DimensionTypeDef]],
        "AggregationPeriod": NotRequired[AggregationPeriodType],
        "StartTimestamp": NotRequired[datetime],
        "EndTimestamp": NotRequired[datetime],
        "Timestamps": NotRequired[List[datetime]],
        "Values": NotRequired[List[MetricQueryValueTypeDef]],
        "Unit": NotRequired[str],
    },
)
PositionSolverConfigurationsTypeDef = TypedDict(
    "PositionSolverConfigurationsTypeDef",
    {
        "SemtechGnss": NotRequired[SemtechGnssConfigurationTypeDef],
    },
)
PositionSolverDetailsTypeDef = TypedDict(
    "PositionSolverDetailsTypeDef",
    {
        "SemtechGnss": NotRequired[SemtechGnssDetailTypeDef],
    },
)
StartSingleWirelessDeviceImportTaskRequestRequestTypeDef = TypedDict(
    "StartSingleWirelessDeviceImportTaskRequestRequestTypeDef",
    {
        "DestinationName": str,
        "Sidewalk": SidewalkSingleStartImportInfoTypeDef,
        "ClientRequestToken": NotRequired[str],
        "DeviceName": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
StartWirelessDeviceImportTaskRequestRequestTypeDef = TypedDict(
    "StartWirelessDeviceImportTaskRequestRequestTypeDef",
    {
        "DestinationName": str,
        "Sidewalk": SidewalkStartImportInfoTypeDef,
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
UpdatePartnerAccountRequestRequestTypeDef = TypedDict(
    "UpdatePartnerAccountRequestRequestTypeDef",
    {
        "Sidewalk": SidewalkUpdateAccountTypeDef,
        "PartnerAccountId": str,
        "PartnerType": Literal["Sidewalk"],
    },
)
UpdateWirelessDeviceImportTaskRequestRequestTypeDef = TypedDict(
    "UpdateWirelessDeviceImportTaskRequestRequestTypeDef",
    {
        "Id": str,
        "Sidewalk": SidewalkUpdateImportInfoTypeDef,
    },
)
TdscdmaObjTypeDef = TypedDict(
    "TdscdmaObjTypeDef",
    {
        "Mcc": int,
        "Mnc": int,
        "UtranCid": int,
        "Lac": NotRequired[int],
        "TdscdmaLocalId": NotRequired[TdscdmaLocalIdTypeDef],
        "TdscdmaTimingAdvance": NotRequired[int],
        "Rscp": NotRequired[int],
        "PathLoss": NotRequired[int],
        "TdscdmaNmr": NotRequired[Sequence[TdscdmaNmrObjTypeDef]],
    },
)
WcdmaObjTypeDef = TypedDict(
    "WcdmaObjTypeDef",
    {
        "Mcc": int,
        "Mnc": int,
        "UtranCid": int,
        "Lac": NotRequired[int],
        "WcdmaLocalId": NotRequired[WcdmaLocalIdTypeDef],
        "Rscp": NotRequired[int],
        "PathLoss": NotRequired[int],
        "WcdmaNmr": NotRequired[Sequence[WcdmaNmrObjTypeDef]],
    },
)
WirelessDeviceLogOptionOutputTypeDef = TypedDict(
    "WirelessDeviceLogOptionOutputTypeDef",
    {
        "Type": WirelessDeviceTypeType,
        "LogLevel": LogLevelType,
        "Events": NotRequired[List[WirelessDeviceEventLogOptionTypeDef]],
    },
)
WirelessDeviceLogOptionTypeDef = TypedDict(
    "WirelessDeviceLogOptionTypeDef",
    {
        "Type": WirelessDeviceTypeType,
        "LogLevel": LogLevelType,
        "Events": NotRequired[Sequence[WirelessDeviceEventLogOptionTypeDef]],
    },
)
WirelessGatewayLogOptionOutputTypeDef = TypedDict(
    "WirelessGatewayLogOptionOutputTypeDef",
    {
        "Type": Literal["LoRaWAN"],
        "LogLevel": LogLevelType,
        "Events": NotRequired[List[WirelessGatewayEventLogOptionTypeDef]],
    },
)
WirelessGatewayLogOptionTypeDef = TypedDict(
    "WirelessGatewayLogOptionTypeDef",
    {
        "Type": Literal["LoRaWAN"],
        "LogLevel": LogLevelType,
        "Events": NotRequired[Sequence[WirelessGatewayEventLogOptionTypeDef]],
    },
)
GetWirelessGatewayResponseTypeDef = TypedDict(
    "GetWirelessGatewayResponseTypeDef",
    {
        "Name": str,
        "Id": str,
        "Description": str,
        "LoRaWAN": LoRaWANGatewayOutputTypeDef,
        "Arn": str,
        "ThingName": str,
        "ThingArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
WirelessGatewayStatisticsTypeDef = TypedDict(
    "WirelessGatewayStatisticsTypeDef",
    {
        "Arn": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "LoRaWAN": NotRequired[LoRaWANGatewayOutputTypeDef],
        "LastUplinkReceivedAt": NotRequired[str],
    },
)
LoRaWANGatewayTypeDef = TypedDict(
    "LoRaWANGatewayTypeDef",
    {
        "GatewayEui": NotRequired[str],
        "RfRegion": NotRequired[str],
        "JoinEuiFilters": NotRequired[Sequence[Sequence[str]]],
        "NetIdFilters": NotRequired[Sequence[str]],
        "SubBands": NotRequired[Sequence[int]],
        "Beaconing": NotRequired[BeaconingUnionTypeDef],
        "MaxEirp": NotRequired[float],
    },
)
WirelessDeviceStatisticsTypeDef = TypedDict(
    "WirelessDeviceStatisticsTypeDef",
    {
        "Arn": NotRequired[str],
        "Id": NotRequired[str],
        "Type": NotRequired[WirelessDeviceTypeType],
        "Name": NotRequired[str],
        "DestinationName": NotRequired[str],
        "LastUplinkReceivedAt": NotRequired[str],
        "LoRaWAN": NotRequired[LoRaWANListDeviceTypeDef],
        "Sidewalk": NotRequired[SidewalkListDeviceTypeDef],
        "FuotaDeviceStatus": NotRequired[FuotaDeviceStatusType],
        "MulticastDeviceStatus": NotRequired[str],
        "McGroupId": NotRequired[int],
    },
)
GetDeviceProfileResponseTypeDef = TypedDict(
    "GetDeviceProfileResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Id": str,
        "LoRaWAN": LoRaWANDeviceProfileOutputTypeDef,
        "Sidewalk": SidewalkGetDeviceProfileTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LoRaWANDeviceOutputTypeDef = TypedDict(
    "LoRaWANDeviceOutputTypeDef",
    {
        "DevEui": NotRequired[str],
        "DeviceProfileId": NotRequired[str],
        "ServiceProfileId": NotRequired[str],
        "OtaaV1_1": NotRequired[OtaaV11TypeDef],
        "OtaaV1_0_x": NotRequired[OtaaV10XTypeDef],
        "AbpV1_1": NotRequired[AbpV11TypeDef],
        "AbpV1_0_x": NotRequired[AbpV10XTypeDef],
        "FPorts": NotRequired[FPortsOutputTypeDef],
    },
)
FPortsUnionTypeDef = Union[FPortsTypeDef, FPortsOutputTypeDef]
LoRaWANUpdateDeviceTypeDef = TypedDict(
    "LoRaWANUpdateDeviceTypeDef",
    {
        "DeviceProfileId": NotRequired[str],
        "ServiceProfileId": NotRequired[str],
        "AbpV1_1": NotRequired[UpdateAbpV11TypeDef],
        "AbpV1_0_x": NotRequired[UpdateAbpV10XTypeDef],
        "FPorts": NotRequired[UpdateFPortsTypeDef],
    },
)
LoRaWANSendDataToDeviceOutputTypeDef = TypedDict(
    "LoRaWANSendDataToDeviceOutputTypeDef",
    {
        "FPort": NotRequired[int],
        "ParticipatingGateways": NotRequired[ParticipatingGatewaysOutputTypeDef],
    },
)
ParticipatingGatewaysUnionTypeDef = Union[
    ParticipatingGatewaysTypeDef, ParticipatingGatewaysOutputTypeDef
]
StartMulticastGroupSessionRequestRequestTypeDef = TypedDict(
    "StartMulticastGroupSessionRequestRequestTypeDef",
    {
        "Id": str,
        "LoRaWAN": LoRaWANMulticastSessionTypeDef,
    },
)
StartFuotaTaskRequestRequestTypeDef = TypedDict(
    "StartFuotaTaskRequestRequestTypeDef",
    {
        "Id": str,
        "LoRaWAN": NotRequired[LoRaWANStartFuotaTaskTypeDef],
    },
)
GetMetricsRequestRequestTypeDef = TypedDict(
    "GetMetricsRequestRequestTypeDef",
    {
        "SummaryMetricQueries": NotRequired[Sequence[SummaryMetricQueryTypeDef]],
    },
)
ListWirelessDeviceImportTasksResponseTypeDef = TypedDict(
    "ListWirelessDeviceImportTasksResponseTypeDef",
    {
        "WirelessDeviceImportTaskList": List[WirelessDeviceImportTaskTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GsmObjTypeDef = TypedDict(
    "GsmObjTypeDef",
    {
        "Mcc": int,
        "Mnc": int,
        "Lac": int,
        "GeranCid": int,
        "GsmLocalId": NotRequired[GsmLocalIdTypeDef],
        "GsmTimingAdvance": NotRequired[int],
        "RxLevel": NotRequired[int],
        "GsmNmr": NotRequired[Sequence[GsmNmrObjTypeDef]],
    },
)
ListDevicesForWirelessDeviceImportTaskResponseTypeDef = TypedDict(
    "ListDevicesForWirelessDeviceImportTaskResponseTypeDef",
    {
        "DestinationName": str,
        "ImportedWirelessDeviceList": List[ImportedWirelessDeviceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
EventNotificationItemConfigurationsTypeDef = TypedDict(
    "EventNotificationItemConfigurationsTypeDef",
    {
        "DeviceRegistrationState": NotRequired[DeviceRegistrationStateEventConfigurationTypeDef],
        "Proximity": NotRequired[ProximityEventConfigurationTypeDef],
        "Join": NotRequired[JoinEventConfigurationTypeDef],
        "ConnectionStatus": NotRequired[ConnectionStatusEventConfigurationTypeDef],
        "MessageDeliveryStatus": NotRequired[MessageDeliveryStatusEventConfigurationTypeDef],
    },
)
GetResourceEventConfigurationResponseTypeDef = TypedDict(
    "GetResourceEventConfigurationResponseTypeDef",
    {
        "DeviceRegistrationState": DeviceRegistrationStateEventConfigurationTypeDef,
        "Proximity": ProximityEventConfigurationTypeDef,
        "Join": JoinEventConfigurationTypeDef,
        "ConnectionStatus": ConnectionStatusEventConfigurationTypeDef,
        "MessageDeliveryStatus": MessageDeliveryStatusEventConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateResourceEventConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateResourceEventConfigurationRequestRequestTypeDef",
    {
        "Identifier": str,
        "IdentifierType": IdentifierTypeType,
        "PartnerType": NotRequired[Literal["Sidewalk"]],
        "DeviceRegistrationState": NotRequired[DeviceRegistrationStateEventConfigurationTypeDef],
        "Proximity": NotRequired[ProximityEventConfigurationTypeDef],
        "Join": NotRequired[JoinEventConfigurationTypeDef],
        "ConnectionStatus": NotRequired[ConnectionStatusEventConfigurationTypeDef],
        "MessageDeliveryStatus": NotRequired[MessageDeliveryStatusEventConfigurationTypeDef],
    },
)
GetEventConfigurationByResourceTypesResponseTypeDef = TypedDict(
    "GetEventConfigurationByResourceTypesResponseTypeDef",
    {
        "DeviceRegistrationState": DeviceRegistrationStateResourceTypeEventConfigurationTypeDef,
        "Proximity": ProximityResourceTypeEventConfigurationTypeDef,
        "Join": JoinResourceTypeEventConfigurationTypeDef,
        "ConnectionStatus": ConnectionStatusResourceTypeEventConfigurationTypeDef,
        "MessageDeliveryStatus": MessageDeliveryStatusResourceTypeEventConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEventConfigurationByResourceTypesRequestRequestTypeDef = TypedDict(
    "UpdateEventConfigurationByResourceTypesRequestRequestTypeDef",
    {
        "DeviceRegistrationState": NotRequired[
            DeviceRegistrationStateResourceTypeEventConfigurationTypeDef
        ],
        "Proximity": NotRequired[ProximityResourceTypeEventConfigurationTypeDef],
        "Join": NotRequired[JoinResourceTypeEventConfigurationTypeDef],
        "ConnectionStatus": NotRequired[ConnectionStatusResourceTypeEventConfigurationTypeDef],
        "MessageDeliveryStatus": NotRequired[
            MessageDeliveryStatusResourceTypeEventConfigurationTypeDef
        ],
    },
)
GetWirelessDeviceStatisticsResponseTypeDef = TypedDict(
    "GetWirelessDeviceStatisticsResponseTypeDef",
    {
        "WirelessDeviceId": str,
        "LastUplinkReceivedAt": str,
        "LoRaWAN": LoRaWANDeviceMetadataTypeDef,
        "Sidewalk": SidewalkDeviceMetadataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetWirelessGatewayFirmwareInformationResponseTypeDef = TypedDict(
    "GetWirelessGatewayFirmwareInformationResponseTypeDef",
    {
        "LoRaWAN": LoRaWANGatewayCurrentVersionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateWirelessGatewayTaskCreateTypeDef = TypedDict(
    "UpdateWirelessGatewayTaskCreateTypeDef",
    {
        "UpdateDataSource": NotRequired[str],
        "UpdateDataRole": NotRequired[str],
        "LoRaWAN": NotRequired[LoRaWANUpdateGatewayTaskCreateTypeDef],
    },
)
UpdateWirelessGatewayTaskEntryTypeDef = TypedDict(
    "UpdateWirelessGatewayTaskEntryTypeDef",
    {
        "Id": NotRequired[str],
        "LoRaWAN": NotRequired[LoRaWANUpdateGatewayTaskEntryTypeDef],
        "Arn": NotRequired[str],
    },
)
SendDataToMulticastGroupRequestRequestTypeDef = TypedDict(
    "SendDataToMulticastGroupRequestRequestTypeDef",
    {
        "Id": str,
        "PayloadData": str,
        "WirelessMetadata": MulticastWirelessMetadataTypeDef,
    },
)
GetMetricsResponseTypeDef = TypedDict(
    "GetMetricsResponseTypeDef",
    {
        "SummaryMetricQueryResults": List[SummaryMetricQueryResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutPositionConfigurationRequestRequestTypeDef = TypedDict(
    "PutPositionConfigurationRequestRequestTypeDef",
    {
        "ResourceIdentifier": str,
        "ResourceType": PositionResourceTypeType,
        "Solvers": NotRequired[PositionSolverConfigurationsTypeDef],
        "Destination": NotRequired[str],
    },
)
GetPositionConfigurationResponseTypeDef = TypedDict(
    "GetPositionConfigurationResponseTypeDef",
    {
        "Solvers": PositionSolverDetailsTypeDef,
        "Destination": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PositionConfigurationItemTypeDef = TypedDict(
    "PositionConfigurationItemTypeDef",
    {
        "ResourceIdentifier": NotRequired[str],
        "ResourceType": NotRequired[PositionResourceTypeType],
        "Solvers": NotRequired[PositionSolverDetailsTypeDef],
        "Destination": NotRequired[str],
    },
)
WirelessDeviceLogOptionUnionTypeDef = Union[
    WirelessDeviceLogOptionTypeDef, WirelessDeviceLogOptionOutputTypeDef
]
GetLogLevelsByResourceTypesResponseTypeDef = TypedDict(
    "GetLogLevelsByResourceTypesResponseTypeDef",
    {
        "DefaultLogLevel": LogLevelType,
        "WirelessGatewayLogOptions": List[WirelessGatewayLogOptionOutputTypeDef],
        "WirelessDeviceLogOptions": List[WirelessDeviceLogOptionOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
WirelessGatewayLogOptionUnionTypeDef = Union[
    WirelessGatewayLogOptionTypeDef, WirelessGatewayLogOptionOutputTypeDef
]
ListWirelessGatewaysResponseTypeDef = TypedDict(
    "ListWirelessGatewaysResponseTypeDef",
    {
        "WirelessGatewayList": List[WirelessGatewayStatisticsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateWirelessGatewayRequestRequestTypeDef = TypedDict(
    "CreateWirelessGatewayRequestRequestTypeDef",
    {
        "LoRaWAN": LoRaWANGatewayTypeDef,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ClientRequestToken": NotRequired[str],
    },
)
ListWirelessDevicesResponseTypeDef = TypedDict(
    "ListWirelessDevicesResponseTypeDef",
    {
        "WirelessDeviceList": List[WirelessDeviceStatisticsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetWirelessDeviceResponseTypeDef = TypedDict(
    "GetWirelessDeviceResponseTypeDef",
    {
        "Type": WirelessDeviceTypeType,
        "Name": str,
        "Description": str,
        "DestinationName": str,
        "Id": str,
        "Arn": str,
        "ThingName": str,
        "ThingArn": str,
        "LoRaWAN": LoRaWANDeviceOutputTypeDef,
        "Sidewalk": SidewalkDeviceTypeDef,
        "Positioning": PositioningConfigStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LoRaWANDeviceTypeDef = TypedDict(
    "LoRaWANDeviceTypeDef",
    {
        "DevEui": NotRequired[str],
        "DeviceProfileId": NotRequired[str],
        "ServiceProfileId": NotRequired[str],
        "OtaaV1_1": NotRequired[OtaaV11TypeDef],
        "OtaaV1_0_x": NotRequired[OtaaV10XTypeDef],
        "AbpV1_1": NotRequired[AbpV11TypeDef],
        "AbpV1_0_x": NotRequired[AbpV10XTypeDef],
        "FPorts": NotRequired[FPortsUnionTypeDef],
    },
)
UpdateWirelessDeviceRequestRequestTypeDef = TypedDict(
    "UpdateWirelessDeviceRequestRequestTypeDef",
    {
        "Id": str,
        "DestinationName": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "LoRaWAN": NotRequired[LoRaWANUpdateDeviceTypeDef],
        "Positioning": NotRequired[PositioningConfigStatusType],
    },
)
DownlinkQueueMessageTypeDef = TypedDict(
    "DownlinkQueueMessageTypeDef",
    {
        "MessageId": NotRequired[str],
        "TransmitMode": NotRequired[int],
        "ReceivedAt": NotRequired[str],
        "LoRaWAN": NotRequired[LoRaWANSendDataToDeviceOutputTypeDef],
    },
)
LoRaWANSendDataToDeviceTypeDef = TypedDict(
    "LoRaWANSendDataToDeviceTypeDef",
    {
        "FPort": NotRequired[int],
        "ParticipatingGateways": NotRequired[ParticipatingGatewaysUnionTypeDef],
    },
)
CellTowersTypeDef = TypedDict(
    "CellTowersTypeDef",
    {
        "Gsm": NotRequired[Sequence[GsmObjTypeDef]],
        "Wcdma": NotRequired[Sequence[WcdmaObjTypeDef]],
        "Tdscdma": NotRequired[Sequence[TdscdmaObjTypeDef]],
        "Lte": NotRequired[Sequence[LteObjTypeDef]],
        "Cdma": NotRequired[Sequence[CdmaObjTypeDef]],
    },
)
EventConfigurationItemTypeDef = TypedDict(
    "EventConfigurationItemTypeDef",
    {
        "Identifier": NotRequired[str],
        "IdentifierType": NotRequired[IdentifierTypeType],
        "PartnerType": NotRequired[Literal["Sidewalk"]],
        "Events": NotRequired[EventNotificationItemConfigurationsTypeDef],
    },
)
CreateWirelessGatewayTaskDefinitionRequestRequestTypeDef = TypedDict(
    "CreateWirelessGatewayTaskDefinitionRequestRequestTypeDef",
    {
        "AutoCreateTasks": bool,
        "Name": NotRequired[str],
        "Update": NotRequired[UpdateWirelessGatewayTaskCreateTypeDef],
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
GetWirelessGatewayTaskDefinitionResponseTypeDef = TypedDict(
    "GetWirelessGatewayTaskDefinitionResponseTypeDef",
    {
        "AutoCreateTasks": bool,
        "Name": str,
        "Update": UpdateWirelessGatewayTaskCreateTypeDef,
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListWirelessGatewayTaskDefinitionsResponseTypeDef = TypedDict(
    "ListWirelessGatewayTaskDefinitionsResponseTypeDef",
    {
        "TaskDefinitions": List[UpdateWirelessGatewayTaskEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListPositionConfigurationsResponseTypeDef = TypedDict(
    "ListPositionConfigurationsResponseTypeDef",
    {
        "PositionConfigurationList": List[PositionConfigurationItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateLogLevelsByResourceTypesRequestRequestTypeDef = TypedDict(
    "UpdateLogLevelsByResourceTypesRequestRequestTypeDef",
    {
        "DefaultLogLevel": NotRequired[LogLevelType],
        "WirelessDeviceLogOptions": NotRequired[Sequence[WirelessDeviceLogOptionUnionTypeDef]],
        "WirelessGatewayLogOptions": NotRequired[Sequence[WirelessGatewayLogOptionUnionTypeDef]],
    },
)
CreateWirelessDeviceRequestRequestTypeDef = TypedDict(
    "CreateWirelessDeviceRequestRequestTypeDef",
    {
        "Type": WirelessDeviceTypeType,
        "DestinationName": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "LoRaWAN": NotRequired[LoRaWANDeviceTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "Positioning": NotRequired[PositioningConfigStatusType],
        "Sidewalk": NotRequired[SidewalkCreateWirelessDeviceTypeDef],
    },
)
ListQueuedMessagesResponseTypeDef = TypedDict(
    "ListQueuedMessagesResponseTypeDef",
    {
        "DownlinkQueueMessagesList": List[DownlinkQueueMessageTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
LoRaWANSendDataToDeviceUnionTypeDef = Union[
    LoRaWANSendDataToDeviceTypeDef, LoRaWANSendDataToDeviceOutputTypeDef
]
GetPositionEstimateRequestRequestTypeDef = TypedDict(
    "GetPositionEstimateRequestRequestTypeDef",
    {
        "WiFiAccessPoints": NotRequired[Sequence[WiFiAccessPointTypeDef]],
        "CellTowers": NotRequired[CellTowersTypeDef],
        "Ip": NotRequired[IpTypeDef],
        "Gnss": NotRequired[GnssTypeDef],
        "Timestamp": NotRequired[TimestampTypeDef],
    },
)
ListEventConfigurationsResponseTypeDef = TypedDict(
    "ListEventConfigurationsResponseTypeDef",
    {
        "EventConfigurationsList": List[EventConfigurationItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
WirelessMetadataTypeDef = TypedDict(
    "WirelessMetadataTypeDef",
    {
        "LoRaWAN": NotRequired[LoRaWANSendDataToDeviceUnionTypeDef],
        "Sidewalk": NotRequired[SidewalkSendDataToDeviceTypeDef],
    },
)
SendDataToWirelessDeviceRequestRequestTypeDef = TypedDict(
    "SendDataToWirelessDeviceRequestRequestTypeDef",
    {
        "Id": str,
        "TransmitMode": int,
        "PayloadData": str,
        "WirelessMetadata": NotRequired[WirelessMetadataTypeDef],
    },
)
