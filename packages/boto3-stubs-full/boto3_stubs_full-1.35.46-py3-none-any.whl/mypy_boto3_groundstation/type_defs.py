"""
Type annotations for groundstation service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/type_defs/)

Usage::

    ```python
    from mypy_boto3_groundstation.type_defs import ComponentVersionTypeDef

    data: ComponentVersionTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AgentStatusType,
    AngleUnitsType,
    AuditResultsType,
    BandwidthUnitsType,
    CapabilityHealthReasonType,
    CapabilityHealthType,
    ConfigCapabilityTypeType,
    ContactStatusType,
    CriticalityType,
    EndpointStatusType,
    EphemerisInvalidReasonType,
    EphemerisSourceType,
    EphemerisStatusType,
    FrequencyUnitsType,
    PolarizationType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "ComponentVersionTypeDef",
    "AggregateStatusTypeDef",
    "AntennaDemodDecodeDetailsTypeDef",
    "DecodeConfigTypeDef",
    "DemodulationConfigTypeDef",
    "EirpTypeDef",
    "CancelContactRequestRequestTypeDef",
    "ComponentStatusDataTypeDef",
    "S3RecordingDetailsTypeDef",
    "ResponseMetadataTypeDef",
    "ConfigListItemTypeDef",
    "DataflowEndpointConfigTypeDef",
    "S3RecordingConfigTypeDef",
    "TrackingConfigTypeDef",
    "UplinkEchoConfigTypeDef",
    "SocketAddressTypeDef",
    "ElevationTypeDef",
    "TimestampTypeDef",
    "KmsKeyTypeDef",
    "DataflowEndpointListItemTypeDef",
    "DeleteConfigRequestRequestTypeDef",
    "DeleteDataflowEndpointGroupRequestRequestTypeDef",
    "DeleteEphemerisRequestRequestTypeDef",
    "DeleteMissionProfileRequestRequestTypeDef",
    "WaiterConfigTypeDef",
    "DescribeContactRequestRequestTypeDef",
    "DescribeEphemerisRequestRequestTypeDef",
    "DiscoveryDataTypeDef",
    "SecurityDetailsOutputTypeDef",
    "S3ObjectTypeDef",
    "EphemerisMetaDataTypeDef",
    "FrequencyBandwidthTypeDef",
    "FrequencyTypeDef",
    "GetAgentConfigurationRequestRequestTypeDef",
    "GetConfigRequestRequestTypeDef",
    "GetDataflowEndpointGroupRequestRequestTypeDef",
    "GetMinuteUsageRequestRequestTypeDef",
    "GetMissionProfileRequestRequestTypeDef",
    "GetSatelliteRequestRequestTypeDef",
    "GroundStationDataTypeDef",
    "IntegerRangeTypeDef",
    "PaginatorConfigTypeDef",
    "ListConfigsRequestRequestTypeDef",
    "ListDataflowEndpointGroupsRequestRequestTypeDef",
    "ListGroundStationsRequestRequestTypeDef",
    "ListMissionProfilesRequestRequestTypeDef",
    "MissionProfileListItemTypeDef",
    "ListSatellitesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "SecurityDetailsTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateEphemerisRequestRequestTypeDef",
    "AgentDetailsTypeDef",
    "UpdateAgentStatusRequestRequestTypeDef",
    "ConfigIdResponseTypeDef",
    "ContactIdResponseTypeDef",
    "DataflowEndpointGroupIdResponseTypeDef",
    "EphemerisIdResponseTypeDef",
    "GetAgentConfigurationResponseTypeDef",
    "GetMinuteUsageResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MissionProfileIdResponseTypeDef",
    "RegisterAgentResponseTypeDef",
    "UpdateAgentStatusResponseTypeDef",
    "ListConfigsResponseTypeDef",
    "ConnectionDetailsTypeDef",
    "DataflowEndpointTypeDef",
    "ContactDataTypeDef",
    "ListContactsRequestRequestTypeDef",
    "ListEphemeridesRequestRequestTypeDef",
    "ReserveContactRequestRequestTypeDef",
    "TimeRangeTypeDef",
    "CreateMissionProfileRequestRequestTypeDef",
    "GetMissionProfileResponseTypeDef",
    "UpdateMissionProfileRequestRequestTypeDef",
    "ListDataflowEndpointGroupsResponseTypeDef",
    "DescribeContactRequestContactScheduledWaitTypeDef",
    "EphemerisDescriptionTypeDef",
    "EphemerisItemTypeDef",
    "OEMEphemerisTypeDef",
    "GetSatelliteResponseTypeDef",
    "SatelliteListItemTypeDef",
    "SpectrumConfigTypeDef",
    "UplinkSpectrumConfigTypeDef",
    "ListGroundStationsResponseTypeDef",
    "RangedSocketAddressTypeDef",
    "ListConfigsRequestListConfigsPaginateTypeDef",
    "ListContactsRequestListContactsPaginateTypeDef",
    "ListDataflowEndpointGroupsRequestListDataflowEndpointGroupsPaginateTypeDef",
    "ListEphemeridesRequestListEphemeridesPaginateTypeDef",
    "ListGroundStationsRequestListGroundStationsPaginateTypeDef",
    "ListMissionProfilesRequestListMissionProfilesPaginateTypeDef",
    "ListSatellitesRequestListSatellitesPaginateTypeDef",
    "ListMissionProfilesResponseTypeDef",
    "SecurityDetailsUnionTypeDef",
    "RegisterAgentRequestRequestTypeDef",
    "ListContactsResponseTypeDef",
    "TLEDataTypeDef",
    "EphemerisTypeDescriptionTypeDef",
    "ListEphemeridesResponseTypeDef",
    "ListSatellitesResponseTypeDef",
    "AntennaDownlinkConfigTypeDef",
    "AntennaDownlinkDemodDecodeConfigTypeDef",
    "AntennaUplinkConfigTypeDef",
    "RangedConnectionDetailsTypeDef",
    "TLEEphemerisTypeDef",
    "DescribeEphemerisResponseTypeDef",
    "ConfigTypeDataTypeDef",
    "AwsGroundStationAgentEndpointTypeDef",
    "EphemerisDataTypeDef",
    "CreateConfigRequestRequestTypeDef",
    "GetConfigResponseTypeDef",
    "UpdateConfigRequestRequestTypeDef",
    "EndpointDetailsOutputTypeDef",
    "EndpointDetailsTypeDef",
    "CreateEphemerisRequestRequestTypeDef",
    "ConfigDetailsTypeDef",
    "GetDataflowEndpointGroupResponseTypeDef",
    "EndpointDetailsUnionTypeDef",
    "DestinationTypeDef",
    "SourceTypeDef",
    "CreateDataflowEndpointGroupRequestRequestTypeDef",
    "DataflowDetailTypeDef",
    "DescribeContactResponseTypeDef",
)

ComponentVersionTypeDef = TypedDict(
    "ComponentVersionTypeDef",
    {
        "componentType": str,
        "versions": Sequence[str],
    },
)
AggregateStatusTypeDef = TypedDict(
    "AggregateStatusTypeDef",
    {
        "status": AgentStatusType,
        "signatureMap": NotRequired[Mapping[str, bool]],
    },
)
AntennaDemodDecodeDetailsTypeDef = TypedDict(
    "AntennaDemodDecodeDetailsTypeDef",
    {
        "outputNode": NotRequired[str],
    },
)
DecodeConfigTypeDef = TypedDict(
    "DecodeConfigTypeDef",
    {
        "unvalidatedJSON": str,
    },
)
DemodulationConfigTypeDef = TypedDict(
    "DemodulationConfigTypeDef",
    {
        "unvalidatedJSON": str,
    },
)
EirpTypeDef = TypedDict(
    "EirpTypeDef",
    {
        "units": Literal["dBW"],
        "value": float,
    },
)
CancelContactRequestRequestTypeDef = TypedDict(
    "CancelContactRequestRequestTypeDef",
    {
        "contactId": str,
    },
)
ComponentStatusDataTypeDef = TypedDict(
    "ComponentStatusDataTypeDef",
    {
        "capabilityArn": str,
        "componentType": str,
        "dataflowId": str,
        "status": AgentStatusType,
        "bytesReceived": NotRequired[int],
        "bytesSent": NotRequired[int],
        "packetsDropped": NotRequired[int],
    },
)
S3RecordingDetailsTypeDef = TypedDict(
    "S3RecordingDetailsTypeDef",
    {
        "bucketArn": NotRequired[str],
        "keyTemplate": NotRequired[str],
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
ConfigListItemTypeDef = TypedDict(
    "ConfigListItemTypeDef",
    {
        "configArn": NotRequired[str],
        "configId": NotRequired[str],
        "configType": NotRequired[ConfigCapabilityTypeType],
        "name": NotRequired[str],
    },
)
DataflowEndpointConfigTypeDef = TypedDict(
    "DataflowEndpointConfigTypeDef",
    {
        "dataflowEndpointName": str,
        "dataflowEndpointRegion": NotRequired[str],
    },
)
S3RecordingConfigTypeDef = TypedDict(
    "S3RecordingConfigTypeDef",
    {
        "bucketArn": str,
        "roleArn": str,
        "prefix": NotRequired[str],
    },
)
TrackingConfigTypeDef = TypedDict(
    "TrackingConfigTypeDef",
    {
        "autotrack": CriticalityType,
    },
)
UplinkEchoConfigTypeDef = TypedDict(
    "UplinkEchoConfigTypeDef",
    {
        "antennaUplinkConfigArn": str,
        "enabled": bool,
    },
)
SocketAddressTypeDef = TypedDict(
    "SocketAddressTypeDef",
    {
        "name": str,
        "port": int,
    },
)
ElevationTypeDef = TypedDict(
    "ElevationTypeDef",
    {
        "unit": AngleUnitsType,
        "value": float,
    },
)
TimestampTypeDef = Union[datetime, str]
KmsKeyTypeDef = TypedDict(
    "KmsKeyTypeDef",
    {
        "kmsAliasArn": NotRequired[str],
        "kmsAliasName": NotRequired[str],
        "kmsKeyArn": NotRequired[str],
    },
)
DataflowEndpointListItemTypeDef = TypedDict(
    "DataflowEndpointListItemTypeDef",
    {
        "dataflowEndpointGroupArn": NotRequired[str],
        "dataflowEndpointGroupId": NotRequired[str],
    },
)
DeleteConfigRequestRequestTypeDef = TypedDict(
    "DeleteConfigRequestRequestTypeDef",
    {
        "configId": str,
        "configType": ConfigCapabilityTypeType,
    },
)
DeleteDataflowEndpointGroupRequestRequestTypeDef = TypedDict(
    "DeleteDataflowEndpointGroupRequestRequestTypeDef",
    {
        "dataflowEndpointGroupId": str,
    },
)
DeleteEphemerisRequestRequestTypeDef = TypedDict(
    "DeleteEphemerisRequestRequestTypeDef",
    {
        "ephemerisId": str,
    },
)
DeleteMissionProfileRequestRequestTypeDef = TypedDict(
    "DeleteMissionProfileRequestRequestTypeDef",
    {
        "missionProfileId": str,
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
DescribeContactRequestRequestTypeDef = TypedDict(
    "DescribeContactRequestRequestTypeDef",
    {
        "contactId": str,
    },
)
DescribeEphemerisRequestRequestTypeDef = TypedDict(
    "DescribeEphemerisRequestRequestTypeDef",
    {
        "ephemerisId": str,
    },
)
DiscoveryDataTypeDef = TypedDict(
    "DiscoveryDataTypeDef",
    {
        "capabilityArns": Sequence[str],
        "privateIpAddresses": Sequence[str],
        "publicIpAddresses": Sequence[str],
    },
)
SecurityDetailsOutputTypeDef = TypedDict(
    "SecurityDetailsOutputTypeDef",
    {
        "roleArn": str,
        "securityGroupIds": List[str],
        "subnetIds": List[str],
    },
)
S3ObjectTypeDef = TypedDict(
    "S3ObjectTypeDef",
    {
        "bucket": NotRequired[str],
        "key": NotRequired[str],
        "version": NotRequired[str],
    },
)
EphemerisMetaDataTypeDef = TypedDict(
    "EphemerisMetaDataTypeDef",
    {
        "source": EphemerisSourceType,
        "ephemerisId": NotRequired[str],
        "epoch": NotRequired[datetime],
        "name": NotRequired[str],
    },
)
FrequencyBandwidthTypeDef = TypedDict(
    "FrequencyBandwidthTypeDef",
    {
        "units": BandwidthUnitsType,
        "value": float,
    },
)
FrequencyTypeDef = TypedDict(
    "FrequencyTypeDef",
    {
        "units": FrequencyUnitsType,
        "value": float,
    },
)
GetAgentConfigurationRequestRequestTypeDef = TypedDict(
    "GetAgentConfigurationRequestRequestTypeDef",
    {
        "agentId": str,
    },
)
GetConfigRequestRequestTypeDef = TypedDict(
    "GetConfigRequestRequestTypeDef",
    {
        "configId": str,
        "configType": ConfigCapabilityTypeType,
    },
)
GetDataflowEndpointGroupRequestRequestTypeDef = TypedDict(
    "GetDataflowEndpointGroupRequestRequestTypeDef",
    {
        "dataflowEndpointGroupId": str,
    },
)
GetMinuteUsageRequestRequestTypeDef = TypedDict(
    "GetMinuteUsageRequestRequestTypeDef",
    {
        "month": int,
        "year": int,
    },
)
GetMissionProfileRequestRequestTypeDef = TypedDict(
    "GetMissionProfileRequestRequestTypeDef",
    {
        "missionProfileId": str,
    },
)
GetSatelliteRequestRequestTypeDef = TypedDict(
    "GetSatelliteRequestRequestTypeDef",
    {
        "satelliteId": str,
    },
)
GroundStationDataTypeDef = TypedDict(
    "GroundStationDataTypeDef",
    {
        "groundStationId": NotRequired[str],
        "groundStationName": NotRequired[str],
        "region": NotRequired[str],
    },
)
IntegerRangeTypeDef = TypedDict(
    "IntegerRangeTypeDef",
    {
        "maximum": int,
        "minimum": int,
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
ListConfigsRequestRequestTypeDef = TypedDict(
    "ListConfigsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListDataflowEndpointGroupsRequestRequestTypeDef = TypedDict(
    "ListDataflowEndpointGroupsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListGroundStationsRequestRequestTypeDef = TypedDict(
    "ListGroundStationsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "satelliteId": NotRequired[str],
    },
)
ListMissionProfilesRequestRequestTypeDef = TypedDict(
    "ListMissionProfilesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
MissionProfileListItemTypeDef = TypedDict(
    "MissionProfileListItemTypeDef",
    {
        "missionProfileArn": NotRequired[str],
        "missionProfileId": NotRequired[str],
        "name": NotRequired[str],
        "region": NotRequired[str],
    },
)
ListSatellitesRequestRequestTypeDef = TypedDict(
    "ListSatellitesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
SecurityDetailsTypeDef = TypedDict(
    "SecurityDetailsTypeDef",
    {
        "roleArn": str,
        "securityGroupIds": Sequence[str],
        "subnetIds": Sequence[str],
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
UpdateEphemerisRequestRequestTypeDef = TypedDict(
    "UpdateEphemerisRequestRequestTypeDef",
    {
        "enabled": bool,
        "ephemerisId": str,
        "name": NotRequired[str],
        "priority": NotRequired[int],
    },
)
AgentDetailsTypeDef = TypedDict(
    "AgentDetailsTypeDef",
    {
        "agentVersion": str,
        "componentVersions": Sequence[ComponentVersionTypeDef],
        "instanceId": str,
        "instanceType": str,
        "agentCpuCores": NotRequired[Sequence[int]],
        "reservedCpuCores": NotRequired[Sequence[int]],
    },
)
UpdateAgentStatusRequestRequestTypeDef = TypedDict(
    "UpdateAgentStatusRequestRequestTypeDef",
    {
        "agentId": str,
        "aggregateStatus": AggregateStatusTypeDef,
        "componentStatuses": Sequence[ComponentStatusDataTypeDef],
        "taskId": str,
    },
)
ConfigIdResponseTypeDef = TypedDict(
    "ConfigIdResponseTypeDef",
    {
        "configArn": str,
        "configId": str,
        "configType": ConfigCapabilityTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ContactIdResponseTypeDef = TypedDict(
    "ContactIdResponseTypeDef",
    {
        "contactId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DataflowEndpointGroupIdResponseTypeDef = TypedDict(
    "DataflowEndpointGroupIdResponseTypeDef",
    {
        "dataflowEndpointGroupId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EphemerisIdResponseTypeDef = TypedDict(
    "EphemerisIdResponseTypeDef",
    {
        "ephemerisId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAgentConfigurationResponseTypeDef = TypedDict(
    "GetAgentConfigurationResponseTypeDef",
    {
        "agentId": str,
        "taskingDocument": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMinuteUsageResponseTypeDef = TypedDict(
    "GetMinuteUsageResponseTypeDef",
    {
        "estimatedMinutesRemaining": int,
        "isReservedMinutesCustomer": bool,
        "totalReservedMinuteAllocation": int,
        "totalScheduledMinutes": int,
        "upcomingMinutesScheduled": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MissionProfileIdResponseTypeDef = TypedDict(
    "MissionProfileIdResponseTypeDef",
    {
        "missionProfileId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterAgentResponseTypeDef = TypedDict(
    "RegisterAgentResponseTypeDef",
    {
        "agentId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAgentStatusResponseTypeDef = TypedDict(
    "UpdateAgentStatusResponseTypeDef",
    {
        "agentId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListConfigsResponseTypeDef = TypedDict(
    "ListConfigsResponseTypeDef",
    {
        "configList": List[ConfigListItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConnectionDetailsTypeDef = TypedDict(
    "ConnectionDetailsTypeDef",
    {
        "socketAddress": SocketAddressTypeDef,
        "mtu": NotRequired[int],
    },
)
DataflowEndpointTypeDef = TypedDict(
    "DataflowEndpointTypeDef",
    {
        "address": NotRequired[SocketAddressTypeDef],
        "mtu": NotRequired[int],
        "name": NotRequired[str],
        "status": NotRequired[EndpointStatusType],
    },
)
ContactDataTypeDef = TypedDict(
    "ContactDataTypeDef",
    {
        "contactId": NotRequired[str],
        "contactStatus": NotRequired[ContactStatusType],
        "endTime": NotRequired[datetime],
        "errorMessage": NotRequired[str],
        "groundStation": NotRequired[str],
        "maximumElevation": NotRequired[ElevationTypeDef],
        "missionProfileArn": NotRequired[str],
        "postPassEndTime": NotRequired[datetime],
        "prePassStartTime": NotRequired[datetime],
        "region": NotRequired[str],
        "satelliteArn": NotRequired[str],
        "startTime": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
        "visibilityEndTime": NotRequired[datetime],
        "visibilityStartTime": NotRequired[datetime],
    },
)
ListContactsRequestRequestTypeDef = TypedDict(
    "ListContactsRequestRequestTypeDef",
    {
        "endTime": TimestampTypeDef,
        "startTime": TimestampTypeDef,
        "statusList": Sequence[ContactStatusType],
        "groundStation": NotRequired[str],
        "maxResults": NotRequired[int],
        "missionProfileArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "satelliteArn": NotRequired[str],
    },
)
ListEphemeridesRequestRequestTypeDef = TypedDict(
    "ListEphemeridesRequestRequestTypeDef",
    {
        "endTime": TimestampTypeDef,
        "satelliteId": str,
        "startTime": TimestampTypeDef,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "statusList": NotRequired[Sequence[EphemerisStatusType]],
    },
)
ReserveContactRequestRequestTypeDef = TypedDict(
    "ReserveContactRequestRequestTypeDef",
    {
        "endTime": TimestampTypeDef,
        "groundStation": str,
        "missionProfileArn": str,
        "satelliteArn": str,
        "startTime": TimestampTypeDef,
        "tags": NotRequired[Mapping[str, str]],
    },
)
TimeRangeTypeDef = TypedDict(
    "TimeRangeTypeDef",
    {
        "endTime": TimestampTypeDef,
        "startTime": TimestampTypeDef,
    },
)
CreateMissionProfileRequestRequestTypeDef = TypedDict(
    "CreateMissionProfileRequestRequestTypeDef",
    {
        "dataflowEdges": Sequence[Sequence[str]],
        "minimumViableContactDurationSeconds": int,
        "name": str,
        "trackingConfigArn": str,
        "contactPostPassDurationSeconds": NotRequired[int],
        "contactPrePassDurationSeconds": NotRequired[int],
        "streamsKmsKey": NotRequired[KmsKeyTypeDef],
        "streamsKmsRole": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
GetMissionProfileResponseTypeDef = TypedDict(
    "GetMissionProfileResponseTypeDef",
    {
        "contactPostPassDurationSeconds": int,
        "contactPrePassDurationSeconds": int,
        "dataflowEdges": List[List[str]],
        "minimumViableContactDurationSeconds": int,
        "missionProfileArn": str,
        "missionProfileId": str,
        "name": str,
        "region": str,
        "streamsKmsKey": KmsKeyTypeDef,
        "streamsKmsRole": str,
        "tags": Dict[str, str],
        "trackingConfigArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateMissionProfileRequestRequestTypeDef = TypedDict(
    "UpdateMissionProfileRequestRequestTypeDef",
    {
        "missionProfileId": str,
        "contactPostPassDurationSeconds": NotRequired[int],
        "contactPrePassDurationSeconds": NotRequired[int],
        "dataflowEdges": NotRequired[Sequence[Sequence[str]]],
        "minimumViableContactDurationSeconds": NotRequired[int],
        "name": NotRequired[str],
        "streamsKmsKey": NotRequired[KmsKeyTypeDef],
        "streamsKmsRole": NotRequired[str],
        "trackingConfigArn": NotRequired[str],
    },
)
ListDataflowEndpointGroupsResponseTypeDef = TypedDict(
    "ListDataflowEndpointGroupsResponseTypeDef",
    {
        "dataflowEndpointGroupList": List[DataflowEndpointListItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeContactRequestContactScheduledWaitTypeDef = TypedDict(
    "DescribeContactRequestContactScheduledWaitTypeDef",
    {
        "contactId": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
EphemerisDescriptionTypeDef = TypedDict(
    "EphemerisDescriptionTypeDef",
    {
        "ephemerisData": NotRequired[str],
        "sourceS3Object": NotRequired[S3ObjectTypeDef],
    },
)
EphemerisItemTypeDef = TypedDict(
    "EphemerisItemTypeDef",
    {
        "creationTime": NotRequired[datetime],
        "enabled": NotRequired[bool],
        "ephemerisId": NotRequired[str],
        "name": NotRequired[str],
        "priority": NotRequired[int],
        "sourceS3Object": NotRequired[S3ObjectTypeDef],
        "status": NotRequired[EphemerisStatusType],
    },
)
OEMEphemerisTypeDef = TypedDict(
    "OEMEphemerisTypeDef",
    {
        "oemData": NotRequired[str],
        "s3Object": NotRequired[S3ObjectTypeDef],
    },
)
GetSatelliteResponseTypeDef = TypedDict(
    "GetSatelliteResponseTypeDef",
    {
        "currentEphemeris": EphemerisMetaDataTypeDef,
        "groundStations": List[str],
        "noradSatelliteID": int,
        "satelliteArn": str,
        "satelliteId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SatelliteListItemTypeDef = TypedDict(
    "SatelliteListItemTypeDef",
    {
        "currentEphemeris": NotRequired[EphemerisMetaDataTypeDef],
        "groundStations": NotRequired[List[str]],
        "noradSatelliteID": NotRequired[int],
        "satelliteArn": NotRequired[str],
        "satelliteId": NotRequired[str],
    },
)
SpectrumConfigTypeDef = TypedDict(
    "SpectrumConfigTypeDef",
    {
        "bandwidth": FrequencyBandwidthTypeDef,
        "centerFrequency": FrequencyTypeDef,
        "polarization": NotRequired[PolarizationType],
    },
)
UplinkSpectrumConfigTypeDef = TypedDict(
    "UplinkSpectrumConfigTypeDef",
    {
        "centerFrequency": FrequencyTypeDef,
        "polarization": NotRequired[PolarizationType],
    },
)
ListGroundStationsResponseTypeDef = TypedDict(
    "ListGroundStationsResponseTypeDef",
    {
        "groundStationList": List[GroundStationDataTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RangedSocketAddressTypeDef = TypedDict(
    "RangedSocketAddressTypeDef",
    {
        "name": str,
        "portRange": IntegerRangeTypeDef,
    },
)
ListConfigsRequestListConfigsPaginateTypeDef = TypedDict(
    "ListConfigsRequestListConfigsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListContactsRequestListContactsPaginateTypeDef = TypedDict(
    "ListContactsRequestListContactsPaginateTypeDef",
    {
        "endTime": TimestampTypeDef,
        "startTime": TimestampTypeDef,
        "statusList": Sequence[ContactStatusType],
        "groundStation": NotRequired[str],
        "missionProfileArn": NotRequired[str],
        "satelliteArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDataflowEndpointGroupsRequestListDataflowEndpointGroupsPaginateTypeDef = TypedDict(
    "ListDataflowEndpointGroupsRequestListDataflowEndpointGroupsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEphemeridesRequestListEphemeridesPaginateTypeDef = TypedDict(
    "ListEphemeridesRequestListEphemeridesPaginateTypeDef",
    {
        "endTime": TimestampTypeDef,
        "satelliteId": str,
        "startTime": TimestampTypeDef,
        "statusList": NotRequired[Sequence[EphemerisStatusType]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGroundStationsRequestListGroundStationsPaginateTypeDef = TypedDict(
    "ListGroundStationsRequestListGroundStationsPaginateTypeDef",
    {
        "satelliteId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMissionProfilesRequestListMissionProfilesPaginateTypeDef = TypedDict(
    "ListMissionProfilesRequestListMissionProfilesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSatellitesRequestListSatellitesPaginateTypeDef = TypedDict(
    "ListSatellitesRequestListSatellitesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMissionProfilesResponseTypeDef = TypedDict(
    "ListMissionProfilesResponseTypeDef",
    {
        "missionProfileList": List[MissionProfileListItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SecurityDetailsUnionTypeDef = Union[SecurityDetailsTypeDef, SecurityDetailsOutputTypeDef]
RegisterAgentRequestRequestTypeDef = TypedDict(
    "RegisterAgentRequestRequestTypeDef",
    {
        "agentDetails": AgentDetailsTypeDef,
        "discoveryData": DiscoveryDataTypeDef,
    },
)
ListContactsResponseTypeDef = TypedDict(
    "ListContactsResponseTypeDef",
    {
        "contactList": List[ContactDataTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TLEDataTypeDef = TypedDict(
    "TLEDataTypeDef",
    {
        "tleLine1": str,
        "tleLine2": str,
        "validTimeRange": TimeRangeTypeDef,
    },
)
EphemerisTypeDescriptionTypeDef = TypedDict(
    "EphemerisTypeDescriptionTypeDef",
    {
        "oem": NotRequired[EphemerisDescriptionTypeDef],
        "tle": NotRequired[EphemerisDescriptionTypeDef],
    },
)
ListEphemeridesResponseTypeDef = TypedDict(
    "ListEphemeridesResponseTypeDef",
    {
        "ephemerides": List[EphemerisItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSatellitesResponseTypeDef = TypedDict(
    "ListSatellitesResponseTypeDef",
    {
        "nextToken": str,
        "satellites": List[SatelliteListItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AntennaDownlinkConfigTypeDef = TypedDict(
    "AntennaDownlinkConfigTypeDef",
    {
        "spectrumConfig": SpectrumConfigTypeDef,
    },
)
AntennaDownlinkDemodDecodeConfigTypeDef = TypedDict(
    "AntennaDownlinkDemodDecodeConfigTypeDef",
    {
        "decodeConfig": DecodeConfigTypeDef,
        "demodulationConfig": DemodulationConfigTypeDef,
        "spectrumConfig": SpectrumConfigTypeDef,
    },
)
AntennaUplinkConfigTypeDef = TypedDict(
    "AntennaUplinkConfigTypeDef",
    {
        "spectrumConfig": UplinkSpectrumConfigTypeDef,
        "targetEirp": EirpTypeDef,
        "transmitDisabled": NotRequired[bool],
    },
)
RangedConnectionDetailsTypeDef = TypedDict(
    "RangedConnectionDetailsTypeDef",
    {
        "socketAddress": RangedSocketAddressTypeDef,
        "mtu": NotRequired[int],
    },
)
TLEEphemerisTypeDef = TypedDict(
    "TLEEphemerisTypeDef",
    {
        "s3Object": NotRequired[S3ObjectTypeDef],
        "tleData": NotRequired[Sequence[TLEDataTypeDef]],
    },
)
DescribeEphemerisResponseTypeDef = TypedDict(
    "DescribeEphemerisResponseTypeDef",
    {
        "creationTime": datetime,
        "enabled": bool,
        "ephemerisId": str,
        "invalidReason": EphemerisInvalidReasonType,
        "name": str,
        "priority": int,
        "satelliteId": str,
        "status": EphemerisStatusType,
        "suppliedData": EphemerisTypeDescriptionTypeDef,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConfigTypeDataTypeDef = TypedDict(
    "ConfigTypeDataTypeDef",
    {
        "antennaDownlinkConfig": NotRequired[AntennaDownlinkConfigTypeDef],
        "antennaDownlinkDemodDecodeConfig": NotRequired[AntennaDownlinkDemodDecodeConfigTypeDef],
        "antennaUplinkConfig": NotRequired[AntennaUplinkConfigTypeDef],
        "dataflowEndpointConfig": NotRequired[DataflowEndpointConfigTypeDef],
        "s3RecordingConfig": NotRequired[S3RecordingConfigTypeDef],
        "trackingConfig": NotRequired[TrackingConfigTypeDef],
        "uplinkEchoConfig": NotRequired[UplinkEchoConfigTypeDef],
    },
)
AwsGroundStationAgentEndpointTypeDef = TypedDict(
    "AwsGroundStationAgentEndpointTypeDef",
    {
        "egressAddress": ConnectionDetailsTypeDef,
        "ingressAddress": RangedConnectionDetailsTypeDef,
        "name": str,
        "agentStatus": NotRequired[AgentStatusType],
        "auditResults": NotRequired[AuditResultsType],
    },
)
EphemerisDataTypeDef = TypedDict(
    "EphemerisDataTypeDef",
    {
        "oem": NotRequired[OEMEphemerisTypeDef],
        "tle": NotRequired[TLEEphemerisTypeDef],
    },
)
CreateConfigRequestRequestTypeDef = TypedDict(
    "CreateConfigRequestRequestTypeDef",
    {
        "configData": ConfigTypeDataTypeDef,
        "name": str,
        "tags": NotRequired[Mapping[str, str]],
    },
)
GetConfigResponseTypeDef = TypedDict(
    "GetConfigResponseTypeDef",
    {
        "configArn": str,
        "configData": ConfigTypeDataTypeDef,
        "configId": str,
        "configType": ConfigCapabilityTypeType,
        "name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateConfigRequestRequestTypeDef = TypedDict(
    "UpdateConfigRequestRequestTypeDef",
    {
        "configData": ConfigTypeDataTypeDef,
        "configId": str,
        "configType": ConfigCapabilityTypeType,
        "name": str,
    },
)
EndpointDetailsOutputTypeDef = TypedDict(
    "EndpointDetailsOutputTypeDef",
    {
        "awsGroundStationAgentEndpoint": NotRequired[AwsGroundStationAgentEndpointTypeDef],
        "endpoint": NotRequired[DataflowEndpointTypeDef],
        "healthReasons": NotRequired[List[CapabilityHealthReasonType]],
        "healthStatus": NotRequired[CapabilityHealthType],
        "securityDetails": NotRequired[SecurityDetailsOutputTypeDef],
    },
)
EndpointDetailsTypeDef = TypedDict(
    "EndpointDetailsTypeDef",
    {
        "awsGroundStationAgentEndpoint": NotRequired[AwsGroundStationAgentEndpointTypeDef],
        "endpoint": NotRequired[DataflowEndpointTypeDef],
        "healthReasons": NotRequired[Sequence[CapabilityHealthReasonType]],
        "healthStatus": NotRequired[CapabilityHealthType],
        "securityDetails": NotRequired[SecurityDetailsUnionTypeDef],
    },
)
CreateEphemerisRequestRequestTypeDef = TypedDict(
    "CreateEphemerisRequestRequestTypeDef",
    {
        "name": str,
        "satelliteId": str,
        "enabled": NotRequired[bool],
        "ephemeris": NotRequired[EphemerisDataTypeDef],
        "expirationTime": NotRequired[TimestampTypeDef],
        "kmsKeyArn": NotRequired[str],
        "priority": NotRequired[int],
        "tags": NotRequired[Mapping[str, str]],
    },
)
ConfigDetailsTypeDef = TypedDict(
    "ConfigDetailsTypeDef",
    {
        "antennaDemodDecodeDetails": NotRequired[AntennaDemodDecodeDetailsTypeDef],
        "endpointDetails": NotRequired[EndpointDetailsOutputTypeDef],
        "s3RecordingDetails": NotRequired[S3RecordingDetailsTypeDef],
    },
)
GetDataflowEndpointGroupResponseTypeDef = TypedDict(
    "GetDataflowEndpointGroupResponseTypeDef",
    {
        "contactPostPassDurationSeconds": int,
        "contactPrePassDurationSeconds": int,
        "dataflowEndpointGroupArn": str,
        "dataflowEndpointGroupId": str,
        "endpointsDetails": List[EndpointDetailsOutputTypeDef],
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EndpointDetailsUnionTypeDef = Union[EndpointDetailsTypeDef, EndpointDetailsOutputTypeDef]
DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "configDetails": NotRequired[ConfigDetailsTypeDef],
        "configId": NotRequired[str],
        "configType": NotRequired[ConfigCapabilityTypeType],
        "dataflowDestinationRegion": NotRequired[str],
    },
)
SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "configDetails": NotRequired[ConfigDetailsTypeDef],
        "configId": NotRequired[str],
        "configType": NotRequired[ConfigCapabilityTypeType],
        "dataflowSourceRegion": NotRequired[str],
    },
)
CreateDataflowEndpointGroupRequestRequestTypeDef = TypedDict(
    "CreateDataflowEndpointGroupRequestRequestTypeDef",
    {
        "endpointDetails": Sequence[EndpointDetailsUnionTypeDef],
        "contactPostPassDurationSeconds": NotRequired[int],
        "contactPrePassDurationSeconds": NotRequired[int],
        "tags": NotRequired[Mapping[str, str]],
    },
)
DataflowDetailTypeDef = TypedDict(
    "DataflowDetailTypeDef",
    {
        "destination": NotRequired[DestinationTypeDef],
        "errorMessage": NotRequired[str],
        "source": NotRequired[SourceTypeDef],
    },
)
DescribeContactResponseTypeDef = TypedDict(
    "DescribeContactResponseTypeDef",
    {
        "contactId": str,
        "contactStatus": ContactStatusType,
        "dataflowList": List[DataflowDetailTypeDef],
        "endTime": datetime,
        "errorMessage": str,
        "groundStation": str,
        "maximumElevation": ElevationTypeDef,
        "missionProfileArn": str,
        "postPassEndTime": datetime,
        "prePassStartTime": datetime,
        "region": str,
        "satelliteArn": str,
        "startTime": datetime,
        "tags": Dict[str, str],
        "visibilityEndTime": datetime,
        "visibilityStartTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
