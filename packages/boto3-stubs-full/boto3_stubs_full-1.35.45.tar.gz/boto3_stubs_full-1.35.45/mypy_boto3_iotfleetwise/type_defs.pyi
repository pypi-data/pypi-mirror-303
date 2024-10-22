"""
Type annotations for iotfleetwise service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/type_defs/)

Usage::

    ```python
    from mypy_boto3_iotfleetwise.type_defs import ActuatorOutputTypeDef

    data: ActuatorOutputTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    CampaignStatusType,
    CompressionType,
    DataFormatType,
    DiagnosticsModeType,
    EncryptionStatusType,
    EncryptionTypeType,
    LogTypeType,
    ManifestStatusType,
    NetworkInterfaceTypeType,
    NodeDataEncodingType,
    NodeDataTypeType,
    RegistrationStatusType,
    ROS2PrimitiveTypeType,
    SignalDecoderTypeType,
    SignalNodeTypeType,
    SpoolingModeType,
    StorageCompressionFormatType,
    StructuredMessageListTypeType,
    TriggerModeType,
    UpdateCampaignActionType,
    UpdateModeType,
    VehicleAssociationBehaviorType,
    VehicleStateType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "ActuatorOutputTypeDef",
    "ActuatorTypeDef",
    "AssociateVehicleFleetRequestRequestTypeDef",
    "AttributeOutputTypeDef",
    "AttributeTypeDef",
    "CreateVehicleErrorTypeDef",
    "CreateVehicleResponseItemTypeDef",
    "ResponseMetadataTypeDef",
    "UpdateVehicleRequestItemTypeDef",
    "UpdateVehicleErrorTypeDef",
    "UpdateVehicleResponseItemTypeDef",
    "BlobTypeDef",
    "BranchTypeDef",
    "CampaignSummaryTypeDef",
    "CanInterfaceTypeDef",
    "CanSignalTypeDef",
    "CloudWatchLogDeliveryOptionsTypeDef",
    "ConditionBasedCollectionSchemeTypeDef",
    "TimeBasedCollectionSchemeTypeDef",
    "SignalInformationTypeDef",
    "TagTypeDef",
    "TimestampTypeDef",
    "CustomPropertyTypeDef",
    "CustomStructTypeDef",
    "S3ConfigTypeDef",
    "TimestreamConfigTypeDef",
    "DecoderManifestSummaryTypeDef",
    "DeleteCampaignRequestRequestTypeDef",
    "DeleteDecoderManifestRequestRequestTypeDef",
    "DeleteFleetRequestRequestTypeDef",
    "DeleteModelManifestRequestRequestTypeDef",
    "DeleteSignalCatalogRequestRequestTypeDef",
    "DeleteVehicleRequestRequestTypeDef",
    "DisassociateVehicleFleetRequestRequestTypeDef",
    "FleetSummaryTypeDef",
    "FormattedVssTypeDef",
    "GetCampaignRequestRequestTypeDef",
    "GetDecoderManifestRequestRequestTypeDef",
    "GetFleetRequestRequestTypeDef",
    "GetModelManifestRequestRequestTypeDef",
    "IamRegistrationResponseTypeDef",
    "TimestreamRegistrationResponseTypeDef",
    "GetSignalCatalogRequestRequestTypeDef",
    "NodeCountsTypeDef",
    "GetVehicleRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "GetVehicleStatusRequestRequestTypeDef",
    "VehicleStatusTypeDef",
    "IamResourcesTypeDef",
    "ListCampaignsRequestRequestTypeDef",
    "ListDecoderManifestNetworkInterfacesRequestRequestTypeDef",
    "ListDecoderManifestSignalsRequestRequestTypeDef",
    "ListDecoderManifestsRequestRequestTypeDef",
    "ListFleetsForVehicleRequestRequestTypeDef",
    "ListFleetsRequestRequestTypeDef",
    "ListModelManifestNodesRequestRequestTypeDef",
    "ListModelManifestsRequestRequestTypeDef",
    "ModelManifestSummaryTypeDef",
    "ListSignalCatalogNodesRequestRequestTypeDef",
    "ListSignalCatalogsRequestRequestTypeDef",
    "SignalCatalogSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListVehiclesInFleetRequestRequestTypeDef",
    "ListVehiclesRequestRequestTypeDef",
    "VehicleSummaryTypeDef",
    "ObdInterfaceTypeDef",
    "VehicleMiddlewareTypeDef",
    "SensorOutputTypeDef",
    "ObdSignalTypeDef",
    "ROS2PrimitiveMessageDefinitionTypeDef",
    "PutEncryptionConfigurationRequestRequestTypeDef",
    "TimestreamResourcesTypeDef",
    "SensorTypeDef",
    "StructuredMessageFieldNameAndDataTypePairOutputTypeDef",
    "StructuredMessageFieldNameAndDataTypePairPaginatorTypeDef",
    "StructuredMessageFieldNameAndDataTypePairTypeDef",
    "StructuredMessageListDefinitionOutputTypeDef",
    "StructuredMessageListDefinitionPaginatorTypeDef",
    "StructuredMessageListDefinitionTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateCampaignRequestRequestTypeDef",
    "UpdateFleetRequestRequestTypeDef",
    "UpdateModelManifestRequestRequestTypeDef",
    "UpdateVehicleRequestRequestTypeDef",
    "ActuatorUnionTypeDef",
    "AttributeUnionTypeDef",
    "BatchCreateVehicleResponseTypeDef",
    "CreateCampaignResponseTypeDef",
    "CreateDecoderManifestResponseTypeDef",
    "CreateFleetResponseTypeDef",
    "CreateModelManifestResponseTypeDef",
    "CreateSignalCatalogResponseTypeDef",
    "CreateVehicleResponseTypeDef",
    "DeleteCampaignResponseTypeDef",
    "DeleteDecoderManifestResponseTypeDef",
    "DeleteFleetResponseTypeDef",
    "DeleteModelManifestResponseTypeDef",
    "DeleteSignalCatalogResponseTypeDef",
    "DeleteVehicleResponseTypeDef",
    "GetDecoderManifestResponseTypeDef",
    "GetEncryptionConfigurationResponseTypeDef",
    "GetFleetResponseTypeDef",
    "GetModelManifestResponseTypeDef",
    "GetVehicleResponseTypeDef",
    "ImportDecoderManifestResponseTypeDef",
    "ImportSignalCatalogResponseTypeDef",
    "ListFleetsForVehicleResponseTypeDef",
    "ListVehiclesInFleetResponseTypeDef",
    "PutEncryptionConfigurationResponseTypeDef",
    "UpdateCampaignResponseTypeDef",
    "UpdateDecoderManifestResponseTypeDef",
    "UpdateFleetResponseTypeDef",
    "UpdateModelManifestResponseTypeDef",
    "UpdateSignalCatalogResponseTypeDef",
    "UpdateVehicleResponseTypeDef",
    "BatchUpdateVehicleRequestRequestTypeDef",
    "BatchUpdateVehicleResponseTypeDef",
    "CanDbcDefinitionTypeDef",
    "ListCampaignsResponseTypeDef",
    "GetLoggingOptionsResponseTypeDef",
    "PutLoggingOptionsRequestRequestTypeDef",
    "CollectionSchemeTypeDef",
    "CreateFleetRequestRequestTypeDef",
    "CreateModelManifestRequestRequestTypeDef",
    "CreateVehicleRequestItemTypeDef",
    "CreateVehicleRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "DataDestinationConfigTypeDef",
    "ListDecoderManifestsResponseTypeDef",
    "ListFleetsResponseTypeDef",
    "ImportSignalCatalogRequestRequestTypeDef",
    "GetRegisterAccountStatusResponseTypeDef",
    "GetSignalCatalogResponseTypeDef",
    "GetVehicleStatusRequestGetVehicleStatusPaginateTypeDef",
    "ListCampaignsRequestListCampaignsPaginateTypeDef",
    "ListDecoderManifestNetworkInterfacesRequestListDecoderManifestNetworkInterfacesPaginateTypeDef",
    "ListDecoderManifestSignalsRequestListDecoderManifestSignalsPaginateTypeDef",
    "ListDecoderManifestsRequestListDecoderManifestsPaginateTypeDef",
    "ListFleetsForVehicleRequestListFleetsForVehiclePaginateTypeDef",
    "ListFleetsRequestListFleetsPaginateTypeDef",
    "ListModelManifestNodesRequestListModelManifestNodesPaginateTypeDef",
    "ListModelManifestsRequestListModelManifestsPaginateTypeDef",
    "ListSignalCatalogNodesRequestListSignalCatalogNodesPaginateTypeDef",
    "ListSignalCatalogsRequestListSignalCatalogsPaginateTypeDef",
    "ListVehiclesInFleetRequestListVehiclesInFleetPaginateTypeDef",
    "ListVehiclesRequestListVehiclesPaginateTypeDef",
    "GetVehicleStatusResponseTypeDef",
    "ListModelManifestsResponseTypeDef",
    "ListSignalCatalogsResponseTypeDef",
    "ListVehiclesResponseTypeDef",
    "NetworkInterfaceTypeDef",
    "NodeOutputTypeDef",
    "PrimitiveMessageDefinitionTypeDef",
    "RegisterAccountRequestRequestTypeDef",
    "RegisterAccountResponseTypeDef",
    "SensorUnionTypeDef",
    "StructuredMessageFieldNameAndDataTypePairUnionTypeDef",
    "StructuredMessageListDefinitionUnionTypeDef",
    "NetworkFileDefinitionTypeDef",
    "BatchCreateVehicleRequestRequestTypeDef",
    "CreateCampaignRequestRequestTypeDef",
    "GetCampaignResponseTypeDef",
    "ListDecoderManifestNetworkInterfacesResponseTypeDef",
    "ListModelManifestNodesResponseTypeDef",
    "ListSignalCatalogNodesResponseTypeDef",
    "StructuredMessageOutputTypeDef",
    "StructuredMessagePaginatorTypeDef",
    "NodeTypeDef",
    "StructuredMessageTypeDef",
    "ImportDecoderManifestRequestRequestTypeDef",
    "MessageSignalOutputTypeDef",
    "MessageSignalPaginatorTypeDef",
    "NodeUnionTypeDef",
    "UpdateSignalCatalogRequestRequestTypeDef",
    "StructuredMessageUnionTypeDef",
    "SignalDecoderOutputTypeDef",
    "SignalDecoderPaginatorTypeDef",
    "CreateSignalCatalogRequestRequestTypeDef",
    "MessageSignalTypeDef",
    "ListDecoderManifestSignalsResponseTypeDef",
    "ListDecoderManifestSignalsResponsePaginatorTypeDef",
    "MessageSignalUnionTypeDef",
    "SignalDecoderTypeDef",
    "SignalDecoderUnionTypeDef",
    "UpdateDecoderManifestRequestRequestTypeDef",
    "CreateDecoderManifestRequestRequestTypeDef",
)

ActuatorOutputTypeDef = TypedDict(
    "ActuatorOutputTypeDef",
    {
        "fullyQualifiedName": str,
        "dataType": NodeDataTypeType,
        "description": NotRequired[str],
        "unit": NotRequired[str],
        "allowedValues": NotRequired[List[str]],
        "min": NotRequired[float],
        "max": NotRequired[float],
        "assignedValue": NotRequired[str],
        "deprecationMessage": NotRequired[str],
        "comment": NotRequired[str],
        "structFullyQualifiedName": NotRequired[str],
    },
)
ActuatorTypeDef = TypedDict(
    "ActuatorTypeDef",
    {
        "fullyQualifiedName": str,
        "dataType": NodeDataTypeType,
        "description": NotRequired[str],
        "unit": NotRequired[str],
        "allowedValues": NotRequired[Sequence[str]],
        "min": NotRequired[float],
        "max": NotRequired[float],
        "assignedValue": NotRequired[str],
        "deprecationMessage": NotRequired[str],
        "comment": NotRequired[str],
        "structFullyQualifiedName": NotRequired[str],
    },
)
AssociateVehicleFleetRequestRequestTypeDef = TypedDict(
    "AssociateVehicleFleetRequestRequestTypeDef",
    {
        "vehicleName": str,
        "fleetId": str,
    },
)
AttributeOutputTypeDef = TypedDict(
    "AttributeOutputTypeDef",
    {
        "fullyQualifiedName": str,
        "dataType": NodeDataTypeType,
        "description": NotRequired[str],
        "unit": NotRequired[str],
        "allowedValues": NotRequired[List[str]],
        "min": NotRequired[float],
        "max": NotRequired[float],
        "assignedValue": NotRequired[str],
        "defaultValue": NotRequired[str],
        "deprecationMessage": NotRequired[str],
        "comment": NotRequired[str],
    },
)
AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "fullyQualifiedName": str,
        "dataType": NodeDataTypeType,
        "description": NotRequired[str],
        "unit": NotRequired[str],
        "allowedValues": NotRequired[Sequence[str]],
        "min": NotRequired[float],
        "max": NotRequired[float],
        "assignedValue": NotRequired[str],
        "defaultValue": NotRequired[str],
        "deprecationMessage": NotRequired[str],
        "comment": NotRequired[str],
    },
)
CreateVehicleErrorTypeDef = TypedDict(
    "CreateVehicleErrorTypeDef",
    {
        "vehicleName": NotRequired[str],
        "code": NotRequired[str],
        "message": NotRequired[str],
    },
)
CreateVehicleResponseItemTypeDef = TypedDict(
    "CreateVehicleResponseItemTypeDef",
    {
        "vehicleName": NotRequired[str],
        "arn": NotRequired[str],
        "thingArn": NotRequired[str],
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
UpdateVehicleRequestItemTypeDef = TypedDict(
    "UpdateVehicleRequestItemTypeDef",
    {
        "vehicleName": str,
        "modelManifestArn": NotRequired[str],
        "decoderManifestArn": NotRequired[str],
        "attributes": NotRequired[Mapping[str, str]],
        "attributeUpdateMode": NotRequired[UpdateModeType],
    },
)
UpdateVehicleErrorTypeDef = TypedDict(
    "UpdateVehicleErrorTypeDef",
    {
        "vehicleName": NotRequired[str],
        "code": NotRequired[int],
        "message": NotRequired[str],
    },
)
UpdateVehicleResponseItemTypeDef = TypedDict(
    "UpdateVehicleResponseItemTypeDef",
    {
        "vehicleName": NotRequired[str],
        "arn": NotRequired[str],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
BranchTypeDef = TypedDict(
    "BranchTypeDef",
    {
        "fullyQualifiedName": str,
        "description": NotRequired[str],
        "deprecationMessage": NotRequired[str],
        "comment": NotRequired[str],
    },
)
CampaignSummaryTypeDef = TypedDict(
    "CampaignSummaryTypeDef",
    {
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "signalCatalogArn": NotRequired[str],
        "targetArn": NotRequired[str],
        "status": NotRequired[CampaignStatusType],
    },
)
CanInterfaceTypeDef = TypedDict(
    "CanInterfaceTypeDef",
    {
        "name": str,
        "protocolName": NotRequired[str],
        "protocolVersion": NotRequired[str],
    },
)
CanSignalTypeDef = TypedDict(
    "CanSignalTypeDef",
    {
        "messageId": int,
        "isBigEndian": bool,
        "isSigned": bool,
        "startBit": int,
        "offset": float,
        "factor": float,
        "length": int,
        "name": NotRequired[str],
    },
)
CloudWatchLogDeliveryOptionsTypeDef = TypedDict(
    "CloudWatchLogDeliveryOptionsTypeDef",
    {
        "logType": LogTypeType,
        "logGroupName": NotRequired[str],
    },
)
ConditionBasedCollectionSchemeTypeDef = TypedDict(
    "ConditionBasedCollectionSchemeTypeDef",
    {
        "expression": str,
        "minimumTriggerIntervalMs": NotRequired[int],
        "triggerMode": NotRequired[TriggerModeType],
        "conditionLanguageVersion": NotRequired[int],
    },
)
TimeBasedCollectionSchemeTypeDef = TypedDict(
    "TimeBasedCollectionSchemeTypeDef",
    {
        "periodMs": int,
    },
)
SignalInformationTypeDef = TypedDict(
    "SignalInformationTypeDef",
    {
        "name": str,
        "maxSampleCount": NotRequired[int],
        "minimumSamplingIntervalMs": NotRequired[int],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
TimestampTypeDef = Union[datetime, str]
CustomPropertyTypeDef = TypedDict(
    "CustomPropertyTypeDef",
    {
        "fullyQualifiedName": str,
        "dataType": NodeDataTypeType,
        "dataEncoding": NotRequired[NodeDataEncodingType],
        "description": NotRequired[str],
        "deprecationMessage": NotRequired[str],
        "comment": NotRequired[str],
        "structFullyQualifiedName": NotRequired[str],
    },
)
CustomStructTypeDef = TypedDict(
    "CustomStructTypeDef",
    {
        "fullyQualifiedName": str,
        "description": NotRequired[str],
        "deprecationMessage": NotRequired[str],
        "comment": NotRequired[str],
    },
)
S3ConfigTypeDef = TypedDict(
    "S3ConfigTypeDef",
    {
        "bucketArn": str,
        "dataFormat": NotRequired[DataFormatType],
        "storageCompressionFormat": NotRequired[StorageCompressionFormatType],
        "prefix": NotRequired[str],
    },
)
TimestreamConfigTypeDef = TypedDict(
    "TimestreamConfigTypeDef",
    {
        "timestreamTableArn": str,
        "executionRoleArn": str,
    },
)
DecoderManifestSummaryTypeDef = TypedDict(
    "DecoderManifestSummaryTypeDef",
    {
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "modelManifestArn": NotRequired[str],
        "description": NotRequired[str],
        "status": NotRequired[ManifestStatusType],
        "message": NotRequired[str],
    },
)
DeleteCampaignRequestRequestTypeDef = TypedDict(
    "DeleteCampaignRequestRequestTypeDef",
    {
        "name": str,
    },
)
DeleteDecoderManifestRequestRequestTypeDef = TypedDict(
    "DeleteDecoderManifestRequestRequestTypeDef",
    {
        "name": str,
    },
)
DeleteFleetRequestRequestTypeDef = TypedDict(
    "DeleteFleetRequestRequestTypeDef",
    {
        "fleetId": str,
    },
)
DeleteModelManifestRequestRequestTypeDef = TypedDict(
    "DeleteModelManifestRequestRequestTypeDef",
    {
        "name": str,
    },
)
DeleteSignalCatalogRequestRequestTypeDef = TypedDict(
    "DeleteSignalCatalogRequestRequestTypeDef",
    {
        "name": str,
    },
)
DeleteVehicleRequestRequestTypeDef = TypedDict(
    "DeleteVehicleRequestRequestTypeDef",
    {
        "vehicleName": str,
    },
)
DisassociateVehicleFleetRequestRequestTypeDef = TypedDict(
    "DisassociateVehicleFleetRequestRequestTypeDef",
    {
        "vehicleName": str,
        "fleetId": str,
    },
)
FleetSummaryTypeDef = TypedDict(
    "FleetSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "signalCatalogArn": str,
        "creationTime": datetime,
        "description": NotRequired[str],
        "lastModificationTime": NotRequired[datetime],
    },
)
FormattedVssTypeDef = TypedDict(
    "FormattedVssTypeDef",
    {
        "vssJson": NotRequired[str],
    },
)
GetCampaignRequestRequestTypeDef = TypedDict(
    "GetCampaignRequestRequestTypeDef",
    {
        "name": str,
    },
)
GetDecoderManifestRequestRequestTypeDef = TypedDict(
    "GetDecoderManifestRequestRequestTypeDef",
    {
        "name": str,
    },
)
GetFleetRequestRequestTypeDef = TypedDict(
    "GetFleetRequestRequestTypeDef",
    {
        "fleetId": str,
    },
)
GetModelManifestRequestRequestTypeDef = TypedDict(
    "GetModelManifestRequestRequestTypeDef",
    {
        "name": str,
    },
)
IamRegistrationResponseTypeDef = TypedDict(
    "IamRegistrationResponseTypeDef",
    {
        "roleArn": str,
        "registrationStatus": RegistrationStatusType,
        "errorMessage": NotRequired[str],
    },
)
TimestreamRegistrationResponseTypeDef = TypedDict(
    "TimestreamRegistrationResponseTypeDef",
    {
        "timestreamDatabaseName": str,
        "timestreamTableName": str,
        "registrationStatus": RegistrationStatusType,
        "timestreamDatabaseArn": NotRequired[str],
        "timestreamTableArn": NotRequired[str],
        "errorMessage": NotRequired[str],
    },
)
GetSignalCatalogRequestRequestTypeDef = TypedDict(
    "GetSignalCatalogRequestRequestTypeDef",
    {
        "name": str,
    },
)
NodeCountsTypeDef = TypedDict(
    "NodeCountsTypeDef",
    {
        "totalNodes": NotRequired[int],
        "totalBranches": NotRequired[int],
        "totalSensors": NotRequired[int],
        "totalAttributes": NotRequired[int],
        "totalActuators": NotRequired[int],
        "totalStructs": NotRequired[int],
        "totalProperties": NotRequired[int],
    },
)
GetVehicleRequestRequestTypeDef = TypedDict(
    "GetVehicleRequestRequestTypeDef",
    {
        "vehicleName": str,
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
GetVehicleStatusRequestRequestTypeDef = TypedDict(
    "GetVehicleStatusRequestRequestTypeDef",
    {
        "vehicleName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
VehicleStatusTypeDef = TypedDict(
    "VehicleStatusTypeDef",
    {
        "campaignName": NotRequired[str],
        "vehicleName": NotRequired[str],
        "status": NotRequired[VehicleStateType],
    },
)
IamResourcesTypeDef = TypedDict(
    "IamResourcesTypeDef",
    {
        "roleArn": str,
    },
)
ListCampaignsRequestRequestTypeDef = TypedDict(
    "ListCampaignsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "status": NotRequired[str],
    },
)
ListDecoderManifestNetworkInterfacesRequestRequestTypeDef = TypedDict(
    "ListDecoderManifestNetworkInterfacesRequestRequestTypeDef",
    {
        "name": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListDecoderManifestSignalsRequestRequestTypeDef = TypedDict(
    "ListDecoderManifestSignalsRequestRequestTypeDef",
    {
        "name": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListDecoderManifestsRequestRequestTypeDef = TypedDict(
    "ListDecoderManifestsRequestRequestTypeDef",
    {
        "modelManifestArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListFleetsForVehicleRequestRequestTypeDef = TypedDict(
    "ListFleetsForVehicleRequestRequestTypeDef",
    {
        "vehicleName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListFleetsRequestRequestTypeDef = TypedDict(
    "ListFleetsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListModelManifestNodesRequestRequestTypeDef = TypedDict(
    "ListModelManifestNodesRequestRequestTypeDef",
    {
        "name": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListModelManifestsRequestRequestTypeDef = TypedDict(
    "ListModelManifestsRequestRequestTypeDef",
    {
        "signalCatalogArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ModelManifestSummaryTypeDef = TypedDict(
    "ModelManifestSummaryTypeDef",
    {
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "signalCatalogArn": NotRequired[str],
        "description": NotRequired[str],
        "status": NotRequired[ManifestStatusType],
    },
)
ListSignalCatalogNodesRequestRequestTypeDef = TypedDict(
    "ListSignalCatalogNodesRequestRequestTypeDef",
    {
        "name": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "signalNodeType": NotRequired[SignalNodeTypeType],
    },
)
ListSignalCatalogsRequestRequestTypeDef = TypedDict(
    "ListSignalCatalogsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
SignalCatalogSummaryTypeDef = TypedDict(
    "SignalCatalogSummaryTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastModificationTime": NotRequired[datetime],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
ListVehiclesInFleetRequestRequestTypeDef = TypedDict(
    "ListVehiclesInFleetRequestRequestTypeDef",
    {
        "fleetId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListVehiclesRequestRequestTypeDef = TypedDict(
    "ListVehiclesRequestRequestTypeDef",
    {
        "modelManifestArn": NotRequired[str],
        "attributeNames": NotRequired[Sequence[str]],
        "attributeValues": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
VehicleSummaryTypeDef = TypedDict(
    "VehicleSummaryTypeDef",
    {
        "vehicleName": str,
        "arn": str,
        "modelManifestArn": str,
        "decoderManifestArn": str,
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "attributes": NotRequired[Dict[str, str]],
    },
)
ObdInterfaceTypeDef = TypedDict(
    "ObdInterfaceTypeDef",
    {
        "name": str,
        "requestMessageId": int,
        "obdStandard": NotRequired[str],
        "pidRequestIntervalSeconds": NotRequired[int],
        "dtcRequestIntervalSeconds": NotRequired[int],
        "useExtendedIds": NotRequired[bool],
        "hasTransmissionEcu": NotRequired[bool],
    },
)
VehicleMiddlewareTypeDef = TypedDict(
    "VehicleMiddlewareTypeDef",
    {
        "name": str,
        "protocolName": Literal["ROS_2"],
    },
)
SensorOutputTypeDef = TypedDict(
    "SensorOutputTypeDef",
    {
        "fullyQualifiedName": str,
        "dataType": NodeDataTypeType,
        "description": NotRequired[str],
        "unit": NotRequired[str],
        "allowedValues": NotRequired[List[str]],
        "min": NotRequired[float],
        "max": NotRequired[float],
        "deprecationMessage": NotRequired[str],
        "comment": NotRequired[str],
        "structFullyQualifiedName": NotRequired[str],
    },
)
ObdSignalTypeDef = TypedDict(
    "ObdSignalTypeDef",
    {
        "pidResponseLength": int,
        "serviceMode": int,
        "pid": int,
        "scaling": float,
        "offset": float,
        "startByte": int,
        "byteLength": int,
        "bitRightShift": NotRequired[int],
        "bitMaskLength": NotRequired[int],
    },
)
ROS2PrimitiveMessageDefinitionTypeDef = TypedDict(
    "ROS2PrimitiveMessageDefinitionTypeDef",
    {
        "primitiveType": ROS2PrimitiveTypeType,
        "offset": NotRequired[float],
        "scaling": NotRequired[float],
        "upperBound": NotRequired[int],
    },
)
PutEncryptionConfigurationRequestRequestTypeDef = TypedDict(
    "PutEncryptionConfigurationRequestRequestTypeDef",
    {
        "encryptionType": EncryptionTypeType,
        "kmsKeyId": NotRequired[str],
    },
)
TimestreamResourcesTypeDef = TypedDict(
    "TimestreamResourcesTypeDef",
    {
        "timestreamDatabaseName": str,
        "timestreamTableName": str,
    },
)
SensorTypeDef = TypedDict(
    "SensorTypeDef",
    {
        "fullyQualifiedName": str,
        "dataType": NodeDataTypeType,
        "description": NotRequired[str],
        "unit": NotRequired[str],
        "allowedValues": NotRequired[Sequence[str]],
        "min": NotRequired[float],
        "max": NotRequired[float],
        "deprecationMessage": NotRequired[str],
        "comment": NotRequired[str],
        "structFullyQualifiedName": NotRequired[str],
    },
)
StructuredMessageFieldNameAndDataTypePairOutputTypeDef = TypedDict(
    "StructuredMessageFieldNameAndDataTypePairOutputTypeDef",
    {
        "fieldName": str,
        "dataType": Dict[str, Any],
    },
)
StructuredMessageFieldNameAndDataTypePairPaginatorTypeDef = TypedDict(
    "StructuredMessageFieldNameAndDataTypePairPaginatorTypeDef",
    {
        "fieldName": str,
        "dataType": Dict[str, Any],
    },
)
StructuredMessageFieldNameAndDataTypePairTypeDef = TypedDict(
    "StructuredMessageFieldNameAndDataTypePairTypeDef",
    {
        "fieldName": str,
        "dataType": Mapping[str, Any],
    },
)
StructuredMessageListDefinitionOutputTypeDef = TypedDict(
    "StructuredMessageListDefinitionOutputTypeDef",
    {
        "name": str,
        "memberType": Dict[str, Any],
        "listType": StructuredMessageListTypeType,
        "capacity": NotRequired[int],
    },
)
StructuredMessageListDefinitionPaginatorTypeDef = TypedDict(
    "StructuredMessageListDefinitionPaginatorTypeDef",
    {
        "name": str,
        "memberType": Dict[str, Any],
        "listType": StructuredMessageListTypeType,
        "capacity": NotRequired[int],
    },
)
StructuredMessageListDefinitionTypeDef = TypedDict(
    "StructuredMessageListDefinitionTypeDef",
    {
        "name": str,
        "memberType": Mapping[str, Any],
        "listType": StructuredMessageListTypeType,
        "capacity": NotRequired[int],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
UpdateCampaignRequestRequestTypeDef = TypedDict(
    "UpdateCampaignRequestRequestTypeDef",
    {
        "name": str,
        "action": UpdateCampaignActionType,
        "description": NotRequired[str],
        "dataExtraDimensions": NotRequired[Sequence[str]],
    },
)
UpdateFleetRequestRequestTypeDef = TypedDict(
    "UpdateFleetRequestRequestTypeDef",
    {
        "fleetId": str,
        "description": NotRequired[str],
    },
)
UpdateModelManifestRequestRequestTypeDef = TypedDict(
    "UpdateModelManifestRequestRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "nodesToAdd": NotRequired[Sequence[str]],
        "nodesToRemove": NotRequired[Sequence[str]],
        "status": NotRequired[ManifestStatusType],
    },
)
UpdateVehicleRequestRequestTypeDef = TypedDict(
    "UpdateVehicleRequestRequestTypeDef",
    {
        "vehicleName": str,
        "modelManifestArn": NotRequired[str],
        "decoderManifestArn": NotRequired[str],
        "attributes": NotRequired[Mapping[str, str]],
        "attributeUpdateMode": NotRequired[UpdateModeType],
    },
)
ActuatorUnionTypeDef = Union[ActuatorTypeDef, ActuatorOutputTypeDef]
AttributeUnionTypeDef = Union[AttributeTypeDef, AttributeOutputTypeDef]
BatchCreateVehicleResponseTypeDef = TypedDict(
    "BatchCreateVehicleResponseTypeDef",
    {
        "vehicles": List[CreateVehicleResponseItemTypeDef],
        "errors": List[CreateVehicleErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCampaignResponseTypeDef = TypedDict(
    "CreateCampaignResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDecoderManifestResponseTypeDef = TypedDict(
    "CreateDecoderManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFleetResponseTypeDef = TypedDict(
    "CreateFleetResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateModelManifestResponseTypeDef = TypedDict(
    "CreateModelManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSignalCatalogResponseTypeDef = TypedDict(
    "CreateSignalCatalogResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateVehicleResponseTypeDef = TypedDict(
    "CreateVehicleResponseTypeDef",
    {
        "vehicleName": str,
        "arn": str,
        "thingArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteCampaignResponseTypeDef = TypedDict(
    "DeleteCampaignResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDecoderManifestResponseTypeDef = TypedDict(
    "DeleteDecoderManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteFleetResponseTypeDef = TypedDict(
    "DeleteFleetResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteModelManifestResponseTypeDef = TypedDict(
    "DeleteModelManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteSignalCatalogResponseTypeDef = TypedDict(
    "DeleteSignalCatalogResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteVehicleResponseTypeDef = TypedDict(
    "DeleteVehicleResponseTypeDef",
    {
        "vehicleName": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDecoderManifestResponseTypeDef = TypedDict(
    "GetDecoderManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "description": str,
        "modelManifestArn": str,
        "status": ManifestStatusType,
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "message": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEncryptionConfigurationResponseTypeDef = TypedDict(
    "GetEncryptionConfigurationResponseTypeDef",
    {
        "kmsKeyId": str,
        "encryptionStatus": EncryptionStatusType,
        "encryptionType": EncryptionTypeType,
        "errorMessage": str,
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFleetResponseTypeDef = TypedDict(
    "GetFleetResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "description": str,
        "signalCatalogArn": str,
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetModelManifestResponseTypeDef = TypedDict(
    "GetModelManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "description": str,
        "signalCatalogArn": str,
        "status": ManifestStatusType,
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetVehicleResponseTypeDef = TypedDict(
    "GetVehicleResponseTypeDef",
    {
        "vehicleName": str,
        "arn": str,
        "modelManifestArn": str,
        "decoderManifestArn": str,
        "attributes": Dict[str, str],
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportDecoderManifestResponseTypeDef = TypedDict(
    "ImportDecoderManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportSignalCatalogResponseTypeDef = TypedDict(
    "ImportSignalCatalogResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListFleetsForVehicleResponseTypeDef = TypedDict(
    "ListFleetsForVehicleResponseTypeDef",
    {
        "fleets": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListVehiclesInFleetResponseTypeDef = TypedDict(
    "ListVehiclesInFleetResponseTypeDef",
    {
        "vehicles": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutEncryptionConfigurationResponseTypeDef = TypedDict(
    "PutEncryptionConfigurationResponseTypeDef",
    {
        "kmsKeyId": str,
        "encryptionStatus": EncryptionStatusType,
        "encryptionType": EncryptionTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateCampaignResponseTypeDef = TypedDict(
    "UpdateCampaignResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "status": CampaignStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDecoderManifestResponseTypeDef = TypedDict(
    "UpdateDecoderManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFleetResponseTypeDef = TypedDict(
    "UpdateFleetResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateModelManifestResponseTypeDef = TypedDict(
    "UpdateModelManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSignalCatalogResponseTypeDef = TypedDict(
    "UpdateSignalCatalogResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateVehicleResponseTypeDef = TypedDict(
    "UpdateVehicleResponseTypeDef",
    {
        "vehicleName": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchUpdateVehicleRequestRequestTypeDef = TypedDict(
    "BatchUpdateVehicleRequestRequestTypeDef",
    {
        "vehicles": Sequence[UpdateVehicleRequestItemTypeDef],
    },
)
BatchUpdateVehicleResponseTypeDef = TypedDict(
    "BatchUpdateVehicleResponseTypeDef",
    {
        "vehicles": List[UpdateVehicleResponseItemTypeDef],
        "errors": List[UpdateVehicleErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CanDbcDefinitionTypeDef = TypedDict(
    "CanDbcDefinitionTypeDef",
    {
        "networkInterface": str,
        "canDbcFiles": Sequence[BlobTypeDef],
        "signalsMap": NotRequired[Mapping[str, str]],
    },
)
ListCampaignsResponseTypeDef = TypedDict(
    "ListCampaignsResponseTypeDef",
    {
        "campaignSummaries": List[CampaignSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLoggingOptionsResponseTypeDef = TypedDict(
    "GetLoggingOptionsResponseTypeDef",
    {
        "cloudWatchLogDelivery": CloudWatchLogDeliveryOptionsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutLoggingOptionsRequestRequestTypeDef = TypedDict(
    "PutLoggingOptionsRequestRequestTypeDef",
    {
        "cloudWatchLogDelivery": CloudWatchLogDeliveryOptionsTypeDef,
    },
)
CollectionSchemeTypeDef = TypedDict(
    "CollectionSchemeTypeDef",
    {
        "timeBasedCollectionScheme": NotRequired[TimeBasedCollectionSchemeTypeDef],
        "conditionBasedCollectionScheme": NotRequired[ConditionBasedCollectionSchemeTypeDef],
    },
)
CreateFleetRequestRequestTypeDef = TypedDict(
    "CreateFleetRequestRequestTypeDef",
    {
        "fleetId": str,
        "signalCatalogArn": str,
        "description": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateModelManifestRequestRequestTypeDef = TypedDict(
    "CreateModelManifestRequestRequestTypeDef",
    {
        "name": str,
        "nodes": Sequence[str],
        "signalCatalogArn": str,
        "description": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateVehicleRequestItemTypeDef = TypedDict(
    "CreateVehicleRequestItemTypeDef",
    {
        "vehicleName": str,
        "modelManifestArn": str,
        "decoderManifestArn": str,
        "attributes": NotRequired[Mapping[str, str]],
        "associationBehavior": NotRequired[VehicleAssociationBehaviorType],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateVehicleRequestRequestTypeDef = TypedDict(
    "CreateVehicleRequestRequestTypeDef",
    {
        "vehicleName": str,
        "modelManifestArn": str,
        "decoderManifestArn": str,
        "attributes": NotRequired[Mapping[str, str]],
        "associationBehavior": NotRequired[VehicleAssociationBehaviorType],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)
DataDestinationConfigTypeDef = TypedDict(
    "DataDestinationConfigTypeDef",
    {
        "s3Config": NotRequired[S3ConfigTypeDef],
        "timestreamConfig": NotRequired[TimestreamConfigTypeDef],
    },
)
ListDecoderManifestsResponseTypeDef = TypedDict(
    "ListDecoderManifestsResponseTypeDef",
    {
        "summaries": List[DecoderManifestSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListFleetsResponseTypeDef = TypedDict(
    "ListFleetsResponseTypeDef",
    {
        "fleetSummaries": List[FleetSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportSignalCatalogRequestRequestTypeDef = TypedDict(
    "ImportSignalCatalogRequestRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "vss": NotRequired[FormattedVssTypeDef],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
GetRegisterAccountStatusResponseTypeDef = TypedDict(
    "GetRegisterAccountStatusResponseTypeDef",
    {
        "customerAccountId": str,
        "accountStatus": RegistrationStatusType,
        "timestreamRegistrationResponse": TimestreamRegistrationResponseTypeDef,
        "iamRegistrationResponse": IamRegistrationResponseTypeDef,
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSignalCatalogResponseTypeDef = TypedDict(
    "GetSignalCatalogResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "description": str,
        "nodeCounts": NodeCountsTypeDef,
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetVehicleStatusRequestGetVehicleStatusPaginateTypeDef = TypedDict(
    "GetVehicleStatusRequestGetVehicleStatusPaginateTypeDef",
    {
        "vehicleName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCampaignsRequestListCampaignsPaginateTypeDef = TypedDict(
    "ListCampaignsRequestListCampaignsPaginateTypeDef",
    {
        "status": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDecoderManifestNetworkInterfacesRequestListDecoderManifestNetworkInterfacesPaginateTypeDef = TypedDict(
    "ListDecoderManifestNetworkInterfacesRequestListDecoderManifestNetworkInterfacesPaginateTypeDef",
    {
        "name": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDecoderManifestSignalsRequestListDecoderManifestSignalsPaginateTypeDef = TypedDict(
    "ListDecoderManifestSignalsRequestListDecoderManifestSignalsPaginateTypeDef",
    {
        "name": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDecoderManifestsRequestListDecoderManifestsPaginateTypeDef = TypedDict(
    "ListDecoderManifestsRequestListDecoderManifestsPaginateTypeDef",
    {
        "modelManifestArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFleetsForVehicleRequestListFleetsForVehiclePaginateTypeDef = TypedDict(
    "ListFleetsForVehicleRequestListFleetsForVehiclePaginateTypeDef",
    {
        "vehicleName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFleetsRequestListFleetsPaginateTypeDef = TypedDict(
    "ListFleetsRequestListFleetsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListModelManifestNodesRequestListModelManifestNodesPaginateTypeDef = TypedDict(
    "ListModelManifestNodesRequestListModelManifestNodesPaginateTypeDef",
    {
        "name": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListModelManifestsRequestListModelManifestsPaginateTypeDef = TypedDict(
    "ListModelManifestsRequestListModelManifestsPaginateTypeDef",
    {
        "signalCatalogArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSignalCatalogNodesRequestListSignalCatalogNodesPaginateTypeDef = TypedDict(
    "ListSignalCatalogNodesRequestListSignalCatalogNodesPaginateTypeDef",
    {
        "name": str,
        "signalNodeType": NotRequired[SignalNodeTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSignalCatalogsRequestListSignalCatalogsPaginateTypeDef = TypedDict(
    "ListSignalCatalogsRequestListSignalCatalogsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListVehiclesInFleetRequestListVehiclesInFleetPaginateTypeDef = TypedDict(
    "ListVehiclesInFleetRequestListVehiclesInFleetPaginateTypeDef",
    {
        "fleetId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListVehiclesRequestListVehiclesPaginateTypeDef = TypedDict(
    "ListVehiclesRequestListVehiclesPaginateTypeDef",
    {
        "modelManifestArn": NotRequired[str],
        "attributeNames": NotRequired[Sequence[str]],
        "attributeValues": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetVehicleStatusResponseTypeDef = TypedDict(
    "GetVehicleStatusResponseTypeDef",
    {
        "campaigns": List[VehicleStatusTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListModelManifestsResponseTypeDef = TypedDict(
    "ListModelManifestsResponseTypeDef",
    {
        "summaries": List[ModelManifestSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSignalCatalogsResponseTypeDef = TypedDict(
    "ListSignalCatalogsResponseTypeDef",
    {
        "summaries": List[SignalCatalogSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListVehiclesResponseTypeDef = TypedDict(
    "ListVehiclesResponseTypeDef",
    {
        "vehicleSummaries": List[VehicleSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "interfaceId": str,
        "type": NetworkInterfaceTypeType,
        "canInterface": NotRequired[CanInterfaceTypeDef],
        "obdInterface": NotRequired[ObdInterfaceTypeDef],
        "vehicleMiddleware": NotRequired[VehicleMiddlewareTypeDef],
    },
)
NodeOutputTypeDef = TypedDict(
    "NodeOutputTypeDef",
    {
        "branch": NotRequired[BranchTypeDef],
        "sensor": NotRequired[SensorOutputTypeDef],
        "actuator": NotRequired[ActuatorOutputTypeDef],
        "attribute": NotRequired[AttributeOutputTypeDef],
        "struct": NotRequired[CustomStructTypeDef],
        "property": NotRequired[CustomPropertyTypeDef],
    },
)
PrimitiveMessageDefinitionTypeDef = TypedDict(
    "PrimitiveMessageDefinitionTypeDef",
    {
        "ros2PrimitiveMessageDefinition": NotRequired[ROS2PrimitiveMessageDefinitionTypeDef],
    },
)
RegisterAccountRequestRequestTypeDef = TypedDict(
    "RegisterAccountRequestRequestTypeDef",
    {
        "timestreamResources": NotRequired[TimestreamResourcesTypeDef],
        "iamResources": NotRequired[IamResourcesTypeDef],
    },
)
RegisterAccountResponseTypeDef = TypedDict(
    "RegisterAccountResponseTypeDef",
    {
        "registerAccountStatus": RegistrationStatusType,
        "timestreamResources": TimestreamResourcesTypeDef,
        "iamResources": IamResourcesTypeDef,
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SensorUnionTypeDef = Union[SensorTypeDef, SensorOutputTypeDef]
StructuredMessageFieldNameAndDataTypePairUnionTypeDef = Union[
    StructuredMessageFieldNameAndDataTypePairTypeDef,
    StructuredMessageFieldNameAndDataTypePairOutputTypeDef,
]
StructuredMessageListDefinitionUnionTypeDef = Union[
    StructuredMessageListDefinitionTypeDef, StructuredMessageListDefinitionOutputTypeDef
]
NetworkFileDefinitionTypeDef = TypedDict(
    "NetworkFileDefinitionTypeDef",
    {
        "canDbc": NotRequired[CanDbcDefinitionTypeDef],
    },
)
BatchCreateVehicleRequestRequestTypeDef = TypedDict(
    "BatchCreateVehicleRequestRequestTypeDef",
    {
        "vehicles": Sequence[CreateVehicleRequestItemTypeDef],
    },
)
CreateCampaignRequestRequestTypeDef = TypedDict(
    "CreateCampaignRequestRequestTypeDef",
    {
        "name": str,
        "signalCatalogArn": str,
        "targetArn": str,
        "collectionScheme": CollectionSchemeTypeDef,
        "description": NotRequired[str],
        "startTime": NotRequired[TimestampTypeDef],
        "expiryTime": NotRequired[TimestampTypeDef],
        "postTriggerCollectionDuration": NotRequired[int],
        "diagnosticsMode": NotRequired[DiagnosticsModeType],
        "spoolingMode": NotRequired[SpoolingModeType],
        "compression": NotRequired[CompressionType],
        "priority": NotRequired[int],
        "signalsToCollect": NotRequired[Sequence[SignalInformationTypeDef]],
        "dataExtraDimensions": NotRequired[Sequence[str]],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "dataDestinationConfigs": NotRequired[Sequence[DataDestinationConfigTypeDef]],
    },
)
GetCampaignResponseTypeDef = TypedDict(
    "GetCampaignResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "description": str,
        "signalCatalogArn": str,
        "targetArn": str,
        "status": CampaignStatusType,
        "startTime": datetime,
        "expiryTime": datetime,
        "postTriggerCollectionDuration": int,
        "diagnosticsMode": DiagnosticsModeType,
        "spoolingMode": SpoolingModeType,
        "compression": CompressionType,
        "priority": int,
        "signalsToCollect": List[SignalInformationTypeDef],
        "collectionScheme": CollectionSchemeTypeDef,
        "dataExtraDimensions": List[str],
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "dataDestinationConfigs": List[DataDestinationConfigTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDecoderManifestNetworkInterfacesResponseTypeDef = TypedDict(
    "ListDecoderManifestNetworkInterfacesResponseTypeDef",
    {
        "networkInterfaces": List[NetworkInterfaceTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListModelManifestNodesResponseTypeDef = TypedDict(
    "ListModelManifestNodesResponseTypeDef",
    {
        "nodes": List[NodeOutputTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSignalCatalogNodesResponseTypeDef = TypedDict(
    "ListSignalCatalogNodesResponseTypeDef",
    {
        "nodes": List[NodeOutputTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StructuredMessageOutputTypeDef = TypedDict(
    "StructuredMessageOutputTypeDef",
    {
        "primitiveMessageDefinition": NotRequired[PrimitiveMessageDefinitionTypeDef],
        "structuredMessageListDefinition": NotRequired[
            StructuredMessageListDefinitionOutputTypeDef
        ],
        "structuredMessageDefinition": NotRequired[
            List[StructuredMessageFieldNameAndDataTypePairOutputTypeDef]
        ],
    },
)
StructuredMessagePaginatorTypeDef = TypedDict(
    "StructuredMessagePaginatorTypeDef",
    {
        "primitiveMessageDefinition": NotRequired[PrimitiveMessageDefinitionTypeDef],
        "structuredMessageListDefinition": NotRequired[
            StructuredMessageListDefinitionPaginatorTypeDef
        ],
        "structuredMessageDefinition": NotRequired[
            List[StructuredMessageFieldNameAndDataTypePairPaginatorTypeDef]
        ],
    },
)
NodeTypeDef = TypedDict(
    "NodeTypeDef",
    {
        "branch": NotRequired[BranchTypeDef],
        "sensor": NotRequired[SensorUnionTypeDef],
        "actuator": NotRequired[ActuatorUnionTypeDef],
        "attribute": NotRequired[AttributeUnionTypeDef],
        "struct": NotRequired[CustomStructTypeDef],
        "property": NotRequired[CustomPropertyTypeDef],
    },
)
StructuredMessageTypeDef = TypedDict(
    "StructuredMessageTypeDef",
    {
        "primitiveMessageDefinition": NotRequired[PrimitiveMessageDefinitionTypeDef],
        "structuredMessageListDefinition": NotRequired[StructuredMessageListDefinitionUnionTypeDef],
        "structuredMessageDefinition": NotRequired[
            Sequence[StructuredMessageFieldNameAndDataTypePairUnionTypeDef]
        ],
    },
)
ImportDecoderManifestRequestRequestTypeDef = TypedDict(
    "ImportDecoderManifestRequestRequestTypeDef",
    {
        "name": str,
        "networkFileDefinitions": Sequence[NetworkFileDefinitionTypeDef],
    },
)
MessageSignalOutputTypeDef = TypedDict(
    "MessageSignalOutputTypeDef",
    {
        "topicName": str,
        "structuredMessage": StructuredMessageOutputTypeDef,
    },
)
MessageSignalPaginatorTypeDef = TypedDict(
    "MessageSignalPaginatorTypeDef",
    {
        "topicName": str,
        "structuredMessage": StructuredMessagePaginatorTypeDef,
    },
)
NodeUnionTypeDef = Union[NodeTypeDef, NodeOutputTypeDef]
UpdateSignalCatalogRequestRequestTypeDef = TypedDict(
    "UpdateSignalCatalogRequestRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "nodesToAdd": NotRequired[Sequence[NodeTypeDef]],
        "nodesToUpdate": NotRequired[Sequence[NodeTypeDef]],
        "nodesToRemove": NotRequired[Sequence[str]],
    },
)
StructuredMessageUnionTypeDef = Union[StructuredMessageTypeDef, StructuredMessageOutputTypeDef]
SignalDecoderOutputTypeDef = TypedDict(
    "SignalDecoderOutputTypeDef",
    {
        "fullyQualifiedName": str,
        "type": SignalDecoderTypeType,
        "interfaceId": str,
        "canSignal": NotRequired[CanSignalTypeDef],
        "obdSignal": NotRequired[ObdSignalTypeDef],
        "messageSignal": NotRequired[MessageSignalOutputTypeDef],
    },
)
SignalDecoderPaginatorTypeDef = TypedDict(
    "SignalDecoderPaginatorTypeDef",
    {
        "fullyQualifiedName": str,
        "type": SignalDecoderTypeType,
        "interfaceId": str,
        "canSignal": NotRequired[CanSignalTypeDef],
        "obdSignal": NotRequired[ObdSignalTypeDef],
        "messageSignal": NotRequired[MessageSignalPaginatorTypeDef],
    },
)
CreateSignalCatalogRequestRequestTypeDef = TypedDict(
    "CreateSignalCatalogRequestRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "nodes": NotRequired[Sequence[NodeUnionTypeDef]],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
MessageSignalTypeDef = TypedDict(
    "MessageSignalTypeDef",
    {
        "topicName": str,
        "structuredMessage": StructuredMessageUnionTypeDef,
    },
)
ListDecoderManifestSignalsResponseTypeDef = TypedDict(
    "ListDecoderManifestSignalsResponseTypeDef",
    {
        "signalDecoders": List[SignalDecoderOutputTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDecoderManifestSignalsResponsePaginatorTypeDef = TypedDict(
    "ListDecoderManifestSignalsResponsePaginatorTypeDef",
    {
        "signalDecoders": List[SignalDecoderPaginatorTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MessageSignalUnionTypeDef = Union[MessageSignalTypeDef, MessageSignalOutputTypeDef]
SignalDecoderTypeDef = TypedDict(
    "SignalDecoderTypeDef",
    {
        "fullyQualifiedName": str,
        "type": SignalDecoderTypeType,
        "interfaceId": str,
        "canSignal": NotRequired[CanSignalTypeDef],
        "obdSignal": NotRequired[ObdSignalTypeDef],
        "messageSignal": NotRequired[MessageSignalUnionTypeDef],
    },
)
SignalDecoderUnionTypeDef = Union[SignalDecoderTypeDef, SignalDecoderOutputTypeDef]
UpdateDecoderManifestRequestRequestTypeDef = TypedDict(
    "UpdateDecoderManifestRequestRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "signalDecodersToAdd": NotRequired[Sequence[SignalDecoderTypeDef]],
        "signalDecodersToUpdate": NotRequired[Sequence[SignalDecoderTypeDef]],
        "signalDecodersToRemove": NotRequired[Sequence[str]],
        "networkInterfacesToAdd": NotRequired[Sequence[NetworkInterfaceTypeDef]],
        "networkInterfacesToUpdate": NotRequired[Sequence[NetworkInterfaceTypeDef]],
        "networkInterfacesToRemove": NotRequired[Sequence[str]],
        "status": NotRequired[ManifestStatusType],
    },
)
CreateDecoderManifestRequestRequestTypeDef = TypedDict(
    "CreateDecoderManifestRequestRequestTypeDef",
    {
        "name": str,
        "modelManifestArn": str,
        "description": NotRequired[str],
        "signalDecoders": NotRequired[Sequence[SignalDecoderUnionTypeDef]],
        "networkInterfaces": NotRequired[Sequence[NetworkInterfaceTypeDef]],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
