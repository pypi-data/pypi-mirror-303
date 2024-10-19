"""
Type annotations for greengrassv2 service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/type_defs/)

Usage::

    ```python
    from mypy_boto3_greengrassv2.type_defs import AssociateClientDeviceWithCoreDeviceEntryTypeDef

    data: AssociateClientDeviceWithCoreDeviceEntryTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    CloudComponentStateType,
    ComponentDependencyTypeType,
    ComponentVisibilityScopeType,
    CoreDeviceStatusType,
    DeploymentComponentUpdatePolicyActionType,
    DeploymentFailureHandlingPolicyType,
    DeploymentHistoryFilterType,
    DeploymentStatusType,
    EffectiveDeploymentExecutionStatusType,
    InstalledComponentLifecycleStateType,
    InstalledComponentTopologyFilterType,
    IotEndpointTypeType,
    IoTJobExecutionFailureTypeType,
    LambdaEventSourceTypeType,
    LambdaFilesystemPermissionType,
    LambdaInputPayloadEncodingTypeType,
    LambdaIsolationModeType,
    RecipeOutputFormatType,
    S3EndpointTypeType,
    VendorGuidanceType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AssociateClientDeviceWithCoreDeviceEntryTypeDef",
    "AssociateClientDeviceWithCoreDeviceErrorEntryTypeDef",
    "AssociateServiceRoleToAccountRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "AssociatedClientDeviceTypeDef",
    "DisassociateClientDeviceFromCoreDeviceEntryTypeDef",
    "DisassociateClientDeviceFromCoreDeviceErrorEntryTypeDef",
    "BlobTypeDef",
    "CancelDeploymentRequestRequestTypeDef",
    "CloudComponentStatusTypeDef",
    "ComponentCandidateTypeDef",
    "ComponentConfigurationUpdateOutputTypeDef",
    "ComponentConfigurationUpdateTypeDef",
    "ComponentDependencyRequirementTypeDef",
    "ComponentPlatformOutputTypeDef",
    "ComponentPlatformTypeDef",
    "SystemResourceLimitsTypeDef",
    "ComponentVersionListItemTypeDef",
    "ConnectivityInfoTypeDef",
    "CoreDeviceTypeDef",
    "DeleteComponentRequestRequestTypeDef",
    "DeleteCoreDeviceRequestRequestTypeDef",
    "DeleteDeploymentRequestRequestTypeDef",
    "DeploymentComponentUpdatePolicyTypeDef",
    "DeploymentConfigurationValidationPolicyTypeDef",
    "IoTJobTimeoutConfigTypeDef",
    "DeploymentTypeDef",
    "DescribeComponentRequestRequestTypeDef",
    "EffectiveDeploymentStatusDetailsTypeDef",
    "GetComponentRequestRequestTypeDef",
    "GetComponentVersionArtifactRequestRequestTypeDef",
    "GetConnectivityInfoRequestRequestTypeDef",
    "GetCoreDeviceRequestRequestTypeDef",
    "GetDeploymentRequestRequestTypeDef",
    "InstalledComponentTypeDef",
    "IoTJobAbortCriteriaTypeDef",
    "IoTJobRateIncreaseCriteriaTypeDef",
    "LambdaDeviceMountTypeDef",
    "LambdaVolumeMountTypeDef",
    "LambdaEventSourceTypeDef",
    "PaginatorConfigTypeDef",
    "ListClientDevicesAssociatedWithCoreDeviceRequestRequestTypeDef",
    "ListComponentVersionsRequestRequestTypeDef",
    "ListComponentsRequestRequestTypeDef",
    "ListCoreDevicesRequestRequestTypeDef",
    "ListDeploymentsRequestRequestTypeDef",
    "ListEffectiveDeploymentsRequestRequestTypeDef",
    "ListInstalledComponentsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ResolvedComponentVersionTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "BatchAssociateClientDeviceWithCoreDeviceRequestRequestTypeDef",
    "AssociateServiceRoleToAccountResponseTypeDef",
    "BatchAssociateClientDeviceWithCoreDeviceResponseTypeDef",
    "CancelDeploymentResponseTypeDef",
    "CreateDeploymentResponseTypeDef",
    "DisassociateServiceRoleFromAccountResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetComponentResponseTypeDef",
    "GetComponentVersionArtifactResponseTypeDef",
    "GetCoreDeviceResponseTypeDef",
    "GetServiceRoleForAccountResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "UpdateConnectivityInfoResponseTypeDef",
    "ListClientDevicesAssociatedWithCoreDeviceResponseTypeDef",
    "BatchDisassociateClientDeviceFromCoreDeviceRequestRequestTypeDef",
    "BatchDisassociateClientDeviceFromCoreDeviceResponseTypeDef",
    "CreateComponentVersionResponseTypeDef",
    "ComponentConfigurationUpdateUnionTypeDef",
    "ComponentLatestVersionTypeDef",
    "DescribeComponentResponseTypeDef",
    "ComponentPlatformUnionTypeDef",
    "ResolveComponentCandidatesRequestRequestTypeDef",
    "ComponentRunWithTypeDef",
    "ListComponentVersionsResponseTypeDef",
    "GetConnectivityInfoResponseTypeDef",
    "UpdateConnectivityInfoRequestRequestTypeDef",
    "ListCoreDevicesResponseTypeDef",
    "DeploymentPoliciesTypeDef",
    "ListDeploymentsResponseTypeDef",
    "EffectiveDeploymentTypeDef",
    "ListInstalledComponentsResponseTypeDef",
    "IoTJobAbortConfigOutputTypeDef",
    "IoTJobAbortConfigTypeDef",
    "IoTJobExponentialRolloutRateTypeDef",
    "LambdaContainerParamsTypeDef",
    "ListClientDevicesAssociatedWithCoreDeviceRequestListClientDevicesAssociatedWithCoreDevicePaginateTypeDef",
    "ListComponentVersionsRequestListComponentVersionsPaginateTypeDef",
    "ListComponentsRequestListComponentsPaginateTypeDef",
    "ListCoreDevicesRequestListCoreDevicesPaginateTypeDef",
    "ListDeploymentsRequestListDeploymentsPaginateTypeDef",
    "ListEffectiveDeploymentsRequestListEffectiveDeploymentsPaginateTypeDef",
    "ListInstalledComponentsRequestListInstalledComponentsPaginateTypeDef",
    "ResolveComponentCandidatesResponseTypeDef",
    "ComponentTypeDef",
    "ComponentDeploymentSpecificationOutputTypeDef",
    "ComponentDeploymentSpecificationTypeDef",
    "ListEffectiveDeploymentsResponseTypeDef",
    "IoTJobAbortConfigUnionTypeDef",
    "IoTJobExecutionsRolloutConfigTypeDef",
    "LambdaLinuxProcessParamsTypeDef",
    "ListComponentsResponseTypeDef",
    "ComponentDeploymentSpecificationUnionTypeDef",
    "DeploymentIoTJobConfigurationOutputTypeDef",
    "DeploymentIoTJobConfigurationTypeDef",
    "LambdaExecutionParametersTypeDef",
    "GetDeploymentResponseTypeDef",
    "CreateDeploymentRequestRequestTypeDef",
    "LambdaFunctionRecipeSourceTypeDef",
    "CreateComponentVersionRequestRequestTypeDef",
)

AssociateClientDeviceWithCoreDeviceEntryTypeDef = TypedDict(
    "AssociateClientDeviceWithCoreDeviceEntryTypeDef",
    {
        "thingName": str,
    },
)
AssociateClientDeviceWithCoreDeviceErrorEntryTypeDef = TypedDict(
    "AssociateClientDeviceWithCoreDeviceErrorEntryTypeDef",
    {
        "thingName": NotRequired[str],
        "code": NotRequired[str],
        "message": NotRequired[str],
    },
)
AssociateServiceRoleToAccountRequestRequestTypeDef = TypedDict(
    "AssociateServiceRoleToAccountRequestRequestTypeDef",
    {
        "roleArn": str,
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
AssociatedClientDeviceTypeDef = TypedDict(
    "AssociatedClientDeviceTypeDef",
    {
        "thingName": NotRequired[str],
        "associationTimestamp": NotRequired[datetime],
    },
)
DisassociateClientDeviceFromCoreDeviceEntryTypeDef = TypedDict(
    "DisassociateClientDeviceFromCoreDeviceEntryTypeDef",
    {
        "thingName": str,
    },
)
DisassociateClientDeviceFromCoreDeviceErrorEntryTypeDef = TypedDict(
    "DisassociateClientDeviceFromCoreDeviceErrorEntryTypeDef",
    {
        "thingName": NotRequired[str],
        "code": NotRequired[str],
        "message": NotRequired[str],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
CancelDeploymentRequestRequestTypeDef = TypedDict(
    "CancelDeploymentRequestRequestTypeDef",
    {
        "deploymentId": str,
    },
)
CloudComponentStatusTypeDef = TypedDict(
    "CloudComponentStatusTypeDef",
    {
        "componentState": NotRequired[CloudComponentStateType],
        "message": NotRequired[str],
        "errors": NotRequired[Dict[str, str]],
        "vendorGuidance": NotRequired[VendorGuidanceType],
        "vendorGuidanceMessage": NotRequired[str],
    },
)
ComponentCandidateTypeDef = TypedDict(
    "ComponentCandidateTypeDef",
    {
        "componentName": NotRequired[str],
        "componentVersion": NotRequired[str],
        "versionRequirements": NotRequired[Mapping[str, str]],
    },
)
ComponentConfigurationUpdateOutputTypeDef = TypedDict(
    "ComponentConfigurationUpdateOutputTypeDef",
    {
        "merge": NotRequired[str],
        "reset": NotRequired[List[str]],
    },
)
ComponentConfigurationUpdateTypeDef = TypedDict(
    "ComponentConfigurationUpdateTypeDef",
    {
        "merge": NotRequired[str],
        "reset": NotRequired[Sequence[str]],
    },
)
ComponentDependencyRequirementTypeDef = TypedDict(
    "ComponentDependencyRequirementTypeDef",
    {
        "versionRequirement": NotRequired[str],
        "dependencyType": NotRequired[ComponentDependencyTypeType],
    },
)
ComponentPlatformOutputTypeDef = TypedDict(
    "ComponentPlatformOutputTypeDef",
    {
        "name": NotRequired[str],
        "attributes": NotRequired[Dict[str, str]],
    },
)
ComponentPlatformTypeDef = TypedDict(
    "ComponentPlatformTypeDef",
    {
        "name": NotRequired[str],
        "attributes": NotRequired[Mapping[str, str]],
    },
)
SystemResourceLimitsTypeDef = TypedDict(
    "SystemResourceLimitsTypeDef",
    {
        "memory": NotRequired[int],
        "cpus": NotRequired[float],
    },
)
ComponentVersionListItemTypeDef = TypedDict(
    "ComponentVersionListItemTypeDef",
    {
        "componentName": NotRequired[str],
        "componentVersion": NotRequired[str],
        "arn": NotRequired[str],
    },
)
ConnectivityInfoTypeDef = TypedDict(
    "ConnectivityInfoTypeDef",
    {
        "id": NotRequired[str],
        "hostAddress": NotRequired[str],
        "portNumber": NotRequired[int],
        "metadata": NotRequired[str],
    },
)
CoreDeviceTypeDef = TypedDict(
    "CoreDeviceTypeDef",
    {
        "coreDeviceThingName": NotRequired[str],
        "status": NotRequired[CoreDeviceStatusType],
        "lastStatusUpdateTimestamp": NotRequired[datetime],
    },
)
DeleteComponentRequestRequestTypeDef = TypedDict(
    "DeleteComponentRequestRequestTypeDef",
    {
        "arn": str,
    },
)
DeleteCoreDeviceRequestRequestTypeDef = TypedDict(
    "DeleteCoreDeviceRequestRequestTypeDef",
    {
        "coreDeviceThingName": str,
    },
)
DeleteDeploymentRequestRequestTypeDef = TypedDict(
    "DeleteDeploymentRequestRequestTypeDef",
    {
        "deploymentId": str,
    },
)
DeploymentComponentUpdatePolicyTypeDef = TypedDict(
    "DeploymentComponentUpdatePolicyTypeDef",
    {
        "timeoutInSeconds": NotRequired[int],
        "action": NotRequired[DeploymentComponentUpdatePolicyActionType],
    },
)
DeploymentConfigurationValidationPolicyTypeDef = TypedDict(
    "DeploymentConfigurationValidationPolicyTypeDef",
    {
        "timeoutInSeconds": NotRequired[int],
    },
)
IoTJobTimeoutConfigTypeDef = TypedDict(
    "IoTJobTimeoutConfigTypeDef",
    {
        "inProgressTimeoutInMinutes": NotRequired[int],
    },
)
DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "targetArn": NotRequired[str],
        "revisionId": NotRequired[str],
        "deploymentId": NotRequired[str],
        "deploymentName": NotRequired[str],
        "creationTimestamp": NotRequired[datetime],
        "deploymentStatus": NotRequired[DeploymentStatusType],
        "isLatestForTarget": NotRequired[bool],
        "parentTargetArn": NotRequired[str],
    },
)
DescribeComponentRequestRequestTypeDef = TypedDict(
    "DescribeComponentRequestRequestTypeDef",
    {
        "arn": str,
    },
)
EffectiveDeploymentStatusDetailsTypeDef = TypedDict(
    "EffectiveDeploymentStatusDetailsTypeDef",
    {
        "errorStack": NotRequired[List[str]],
        "errorTypes": NotRequired[List[str]],
    },
)
GetComponentRequestRequestTypeDef = TypedDict(
    "GetComponentRequestRequestTypeDef",
    {
        "arn": str,
        "recipeOutputFormat": NotRequired[RecipeOutputFormatType],
    },
)
GetComponentVersionArtifactRequestRequestTypeDef = TypedDict(
    "GetComponentVersionArtifactRequestRequestTypeDef",
    {
        "arn": str,
        "artifactName": str,
        "s3EndpointType": NotRequired[S3EndpointTypeType],
        "iotEndpointType": NotRequired[IotEndpointTypeType],
    },
)
GetConnectivityInfoRequestRequestTypeDef = TypedDict(
    "GetConnectivityInfoRequestRequestTypeDef",
    {
        "thingName": str,
    },
)
GetCoreDeviceRequestRequestTypeDef = TypedDict(
    "GetCoreDeviceRequestRequestTypeDef",
    {
        "coreDeviceThingName": str,
    },
)
GetDeploymentRequestRequestTypeDef = TypedDict(
    "GetDeploymentRequestRequestTypeDef",
    {
        "deploymentId": str,
    },
)
InstalledComponentTypeDef = TypedDict(
    "InstalledComponentTypeDef",
    {
        "componentName": NotRequired[str],
        "componentVersion": NotRequired[str],
        "lifecycleState": NotRequired[InstalledComponentLifecycleStateType],
        "lifecycleStateDetails": NotRequired[str],
        "isRoot": NotRequired[bool],
        "lastStatusChangeTimestamp": NotRequired[datetime],
        "lastReportedTimestamp": NotRequired[datetime],
        "lastInstallationSource": NotRequired[str],
        "lifecycleStatusCodes": NotRequired[List[str]],
    },
)
IoTJobAbortCriteriaTypeDef = TypedDict(
    "IoTJobAbortCriteriaTypeDef",
    {
        "failureType": IoTJobExecutionFailureTypeType,
        "action": Literal["CANCEL"],
        "thresholdPercentage": float,
        "minNumberOfExecutedThings": int,
    },
)
IoTJobRateIncreaseCriteriaTypeDef = TypedDict(
    "IoTJobRateIncreaseCriteriaTypeDef",
    {
        "numberOfNotifiedThings": NotRequired[int],
        "numberOfSucceededThings": NotRequired[int],
    },
)
LambdaDeviceMountTypeDef = TypedDict(
    "LambdaDeviceMountTypeDef",
    {
        "path": str,
        "permission": NotRequired[LambdaFilesystemPermissionType],
        "addGroupOwner": NotRequired[bool],
    },
)
LambdaVolumeMountTypeDef = TypedDict(
    "LambdaVolumeMountTypeDef",
    {
        "sourcePath": str,
        "destinationPath": str,
        "permission": NotRequired[LambdaFilesystemPermissionType],
        "addGroupOwner": NotRequired[bool],
    },
)
LambdaEventSourceTypeDef = TypedDict(
    "LambdaEventSourceTypeDef",
    {
        "topic": str,
        "type": LambdaEventSourceTypeType,
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
ListClientDevicesAssociatedWithCoreDeviceRequestRequestTypeDef = TypedDict(
    "ListClientDevicesAssociatedWithCoreDeviceRequestRequestTypeDef",
    {
        "coreDeviceThingName": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListComponentVersionsRequestRequestTypeDef = TypedDict(
    "ListComponentVersionsRequestRequestTypeDef",
    {
        "arn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListComponentsRequestRequestTypeDef = TypedDict(
    "ListComponentsRequestRequestTypeDef",
    {
        "scope": NotRequired[ComponentVisibilityScopeType],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListCoreDevicesRequestRequestTypeDef = TypedDict(
    "ListCoreDevicesRequestRequestTypeDef",
    {
        "thingGroupArn": NotRequired[str],
        "status": NotRequired[CoreDeviceStatusType],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListDeploymentsRequestRequestTypeDef = TypedDict(
    "ListDeploymentsRequestRequestTypeDef",
    {
        "targetArn": NotRequired[str],
        "historyFilter": NotRequired[DeploymentHistoryFilterType],
        "parentTargetArn": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListEffectiveDeploymentsRequestRequestTypeDef = TypedDict(
    "ListEffectiveDeploymentsRequestRequestTypeDef",
    {
        "coreDeviceThingName": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListInstalledComponentsRequestRequestTypeDef = TypedDict(
    "ListInstalledComponentsRequestRequestTypeDef",
    {
        "coreDeviceThingName": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "topologyFilter": NotRequired[InstalledComponentTopologyFilterType],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
ResolvedComponentVersionTypeDef = TypedDict(
    "ResolvedComponentVersionTypeDef",
    {
        "arn": NotRequired[str],
        "componentName": NotRequired[str],
        "componentVersion": NotRequired[str],
        "recipe": NotRequired[bytes],
        "vendorGuidance": NotRequired[VendorGuidanceType],
        "message": NotRequired[str],
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
BatchAssociateClientDeviceWithCoreDeviceRequestRequestTypeDef = TypedDict(
    "BatchAssociateClientDeviceWithCoreDeviceRequestRequestTypeDef",
    {
        "coreDeviceThingName": str,
        "entries": NotRequired[Sequence[AssociateClientDeviceWithCoreDeviceEntryTypeDef]],
    },
)
AssociateServiceRoleToAccountResponseTypeDef = TypedDict(
    "AssociateServiceRoleToAccountResponseTypeDef",
    {
        "associatedAt": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchAssociateClientDeviceWithCoreDeviceResponseTypeDef = TypedDict(
    "BatchAssociateClientDeviceWithCoreDeviceResponseTypeDef",
    {
        "errorEntries": List[AssociateClientDeviceWithCoreDeviceErrorEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CancelDeploymentResponseTypeDef = TypedDict(
    "CancelDeploymentResponseTypeDef",
    {
        "message": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDeploymentResponseTypeDef = TypedDict(
    "CreateDeploymentResponseTypeDef",
    {
        "deploymentId": str,
        "iotJobId": str,
        "iotJobArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateServiceRoleFromAccountResponseTypeDef = TypedDict(
    "DisassociateServiceRoleFromAccountResponseTypeDef",
    {
        "disassociatedAt": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetComponentResponseTypeDef = TypedDict(
    "GetComponentResponseTypeDef",
    {
        "recipeOutputFormat": RecipeOutputFormatType,
        "recipe": bytes,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetComponentVersionArtifactResponseTypeDef = TypedDict(
    "GetComponentVersionArtifactResponseTypeDef",
    {
        "preSignedUrl": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCoreDeviceResponseTypeDef = TypedDict(
    "GetCoreDeviceResponseTypeDef",
    {
        "coreDeviceThingName": str,
        "coreVersion": str,
        "platform": str,
        "architecture": str,
        "status": CoreDeviceStatusType,
        "lastStatusUpdateTimestamp": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServiceRoleForAccountResponseTypeDef = TypedDict(
    "GetServiceRoleForAccountResponseTypeDef",
    {
        "associatedAt": str,
        "roleArn": str,
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
UpdateConnectivityInfoResponseTypeDef = TypedDict(
    "UpdateConnectivityInfoResponseTypeDef",
    {
        "version": str,
        "message": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListClientDevicesAssociatedWithCoreDeviceResponseTypeDef = TypedDict(
    "ListClientDevicesAssociatedWithCoreDeviceResponseTypeDef",
    {
        "associatedClientDevices": List[AssociatedClientDeviceTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDisassociateClientDeviceFromCoreDeviceRequestRequestTypeDef = TypedDict(
    "BatchDisassociateClientDeviceFromCoreDeviceRequestRequestTypeDef",
    {
        "coreDeviceThingName": str,
        "entries": NotRequired[Sequence[DisassociateClientDeviceFromCoreDeviceEntryTypeDef]],
    },
)
BatchDisassociateClientDeviceFromCoreDeviceResponseTypeDef = TypedDict(
    "BatchDisassociateClientDeviceFromCoreDeviceResponseTypeDef",
    {
        "errorEntries": List[DisassociateClientDeviceFromCoreDeviceErrorEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateComponentVersionResponseTypeDef = TypedDict(
    "CreateComponentVersionResponseTypeDef",
    {
        "arn": str,
        "componentName": str,
        "componentVersion": str,
        "creationTimestamp": datetime,
        "status": CloudComponentStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ComponentConfigurationUpdateUnionTypeDef = Union[
    ComponentConfigurationUpdateTypeDef, ComponentConfigurationUpdateOutputTypeDef
]
ComponentLatestVersionTypeDef = TypedDict(
    "ComponentLatestVersionTypeDef",
    {
        "arn": NotRequired[str],
        "componentVersion": NotRequired[str],
        "creationTimestamp": NotRequired[datetime],
        "description": NotRequired[str],
        "publisher": NotRequired[str],
        "platforms": NotRequired[List[ComponentPlatformOutputTypeDef]],
    },
)
DescribeComponentResponseTypeDef = TypedDict(
    "DescribeComponentResponseTypeDef",
    {
        "arn": str,
        "componentName": str,
        "componentVersion": str,
        "creationTimestamp": datetime,
        "publisher": str,
        "description": str,
        "status": CloudComponentStatusTypeDef,
        "platforms": List[ComponentPlatformOutputTypeDef],
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ComponentPlatformUnionTypeDef = Union[ComponentPlatformTypeDef, ComponentPlatformOutputTypeDef]
ResolveComponentCandidatesRequestRequestTypeDef = TypedDict(
    "ResolveComponentCandidatesRequestRequestTypeDef",
    {
        "platform": NotRequired[ComponentPlatformTypeDef],
        "componentCandidates": NotRequired[Sequence[ComponentCandidateTypeDef]],
    },
)
ComponentRunWithTypeDef = TypedDict(
    "ComponentRunWithTypeDef",
    {
        "posixUser": NotRequired[str],
        "systemResourceLimits": NotRequired[SystemResourceLimitsTypeDef],
        "windowsUser": NotRequired[str],
    },
)
ListComponentVersionsResponseTypeDef = TypedDict(
    "ListComponentVersionsResponseTypeDef",
    {
        "componentVersions": List[ComponentVersionListItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetConnectivityInfoResponseTypeDef = TypedDict(
    "GetConnectivityInfoResponseTypeDef",
    {
        "connectivityInfo": List[ConnectivityInfoTypeDef],
        "message": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateConnectivityInfoRequestRequestTypeDef = TypedDict(
    "UpdateConnectivityInfoRequestRequestTypeDef",
    {
        "thingName": str,
        "connectivityInfo": Sequence[ConnectivityInfoTypeDef],
    },
)
ListCoreDevicesResponseTypeDef = TypedDict(
    "ListCoreDevicesResponseTypeDef",
    {
        "coreDevices": List[CoreDeviceTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeploymentPoliciesTypeDef = TypedDict(
    "DeploymentPoliciesTypeDef",
    {
        "failureHandlingPolicy": NotRequired[DeploymentFailureHandlingPolicyType],
        "componentUpdatePolicy": NotRequired[DeploymentComponentUpdatePolicyTypeDef],
        "configurationValidationPolicy": NotRequired[
            DeploymentConfigurationValidationPolicyTypeDef
        ],
    },
)
ListDeploymentsResponseTypeDef = TypedDict(
    "ListDeploymentsResponseTypeDef",
    {
        "deployments": List[DeploymentTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EffectiveDeploymentTypeDef = TypedDict(
    "EffectiveDeploymentTypeDef",
    {
        "deploymentId": str,
        "deploymentName": str,
        "targetArn": str,
        "coreDeviceExecutionStatus": EffectiveDeploymentExecutionStatusType,
        "creationTimestamp": datetime,
        "modifiedTimestamp": datetime,
        "iotJobId": NotRequired[str],
        "iotJobArn": NotRequired[str],
        "description": NotRequired[str],
        "reason": NotRequired[str],
        "statusDetails": NotRequired[EffectiveDeploymentStatusDetailsTypeDef],
    },
)
ListInstalledComponentsResponseTypeDef = TypedDict(
    "ListInstalledComponentsResponseTypeDef",
    {
        "installedComponents": List[InstalledComponentTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IoTJobAbortConfigOutputTypeDef = TypedDict(
    "IoTJobAbortConfigOutputTypeDef",
    {
        "criteriaList": List[IoTJobAbortCriteriaTypeDef],
    },
)
IoTJobAbortConfigTypeDef = TypedDict(
    "IoTJobAbortConfigTypeDef",
    {
        "criteriaList": Sequence[IoTJobAbortCriteriaTypeDef],
    },
)
IoTJobExponentialRolloutRateTypeDef = TypedDict(
    "IoTJobExponentialRolloutRateTypeDef",
    {
        "baseRatePerMinute": int,
        "incrementFactor": float,
        "rateIncreaseCriteria": IoTJobRateIncreaseCriteriaTypeDef,
    },
)
LambdaContainerParamsTypeDef = TypedDict(
    "LambdaContainerParamsTypeDef",
    {
        "memorySizeInKB": NotRequired[int],
        "mountROSysfs": NotRequired[bool],
        "volumes": NotRequired[Sequence[LambdaVolumeMountTypeDef]],
        "devices": NotRequired[Sequence[LambdaDeviceMountTypeDef]],
    },
)
ListClientDevicesAssociatedWithCoreDeviceRequestListClientDevicesAssociatedWithCoreDevicePaginateTypeDef = TypedDict(
    "ListClientDevicesAssociatedWithCoreDeviceRequestListClientDevicesAssociatedWithCoreDevicePaginateTypeDef",
    {
        "coreDeviceThingName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListComponentVersionsRequestListComponentVersionsPaginateTypeDef = TypedDict(
    "ListComponentVersionsRequestListComponentVersionsPaginateTypeDef",
    {
        "arn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListComponentsRequestListComponentsPaginateTypeDef = TypedDict(
    "ListComponentsRequestListComponentsPaginateTypeDef",
    {
        "scope": NotRequired[ComponentVisibilityScopeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCoreDevicesRequestListCoreDevicesPaginateTypeDef = TypedDict(
    "ListCoreDevicesRequestListCoreDevicesPaginateTypeDef",
    {
        "thingGroupArn": NotRequired[str],
        "status": NotRequired[CoreDeviceStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDeploymentsRequestListDeploymentsPaginateTypeDef = TypedDict(
    "ListDeploymentsRequestListDeploymentsPaginateTypeDef",
    {
        "targetArn": NotRequired[str],
        "historyFilter": NotRequired[DeploymentHistoryFilterType],
        "parentTargetArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEffectiveDeploymentsRequestListEffectiveDeploymentsPaginateTypeDef = TypedDict(
    "ListEffectiveDeploymentsRequestListEffectiveDeploymentsPaginateTypeDef",
    {
        "coreDeviceThingName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListInstalledComponentsRequestListInstalledComponentsPaginateTypeDef = TypedDict(
    "ListInstalledComponentsRequestListInstalledComponentsPaginateTypeDef",
    {
        "coreDeviceThingName": str,
        "topologyFilter": NotRequired[InstalledComponentTopologyFilterType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ResolveComponentCandidatesResponseTypeDef = TypedDict(
    "ResolveComponentCandidatesResponseTypeDef",
    {
        "resolvedComponentVersions": List[ResolvedComponentVersionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ComponentTypeDef = TypedDict(
    "ComponentTypeDef",
    {
        "arn": NotRequired[str],
        "componentName": NotRequired[str],
        "latestVersion": NotRequired[ComponentLatestVersionTypeDef],
    },
)
ComponentDeploymentSpecificationOutputTypeDef = TypedDict(
    "ComponentDeploymentSpecificationOutputTypeDef",
    {
        "componentVersion": str,
        "configurationUpdate": NotRequired[ComponentConfigurationUpdateOutputTypeDef],
        "runWith": NotRequired[ComponentRunWithTypeDef],
    },
)
ComponentDeploymentSpecificationTypeDef = TypedDict(
    "ComponentDeploymentSpecificationTypeDef",
    {
        "componentVersion": str,
        "configurationUpdate": NotRequired[ComponentConfigurationUpdateUnionTypeDef],
        "runWith": NotRequired[ComponentRunWithTypeDef],
    },
)
ListEffectiveDeploymentsResponseTypeDef = TypedDict(
    "ListEffectiveDeploymentsResponseTypeDef",
    {
        "effectiveDeployments": List[EffectiveDeploymentTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IoTJobAbortConfigUnionTypeDef = Union[IoTJobAbortConfigTypeDef, IoTJobAbortConfigOutputTypeDef]
IoTJobExecutionsRolloutConfigTypeDef = TypedDict(
    "IoTJobExecutionsRolloutConfigTypeDef",
    {
        "exponentialRate": NotRequired[IoTJobExponentialRolloutRateTypeDef],
        "maximumPerMinute": NotRequired[int],
    },
)
LambdaLinuxProcessParamsTypeDef = TypedDict(
    "LambdaLinuxProcessParamsTypeDef",
    {
        "isolationMode": NotRequired[LambdaIsolationModeType],
        "containerParams": NotRequired[LambdaContainerParamsTypeDef],
    },
)
ListComponentsResponseTypeDef = TypedDict(
    "ListComponentsResponseTypeDef",
    {
        "components": List[ComponentTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ComponentDeploymentSpecificationUnionTypeDef = Union[
    ComponentDeploymentSpecificationTypeDef, ComponentDeploymentSpecificationOutputTypeDef
]
DeploymentIoTJobConfigurationOutputTypeDef = TypedDict(
    "DeploymentIoTJobConfigurationOutputTypeDef",
    {
        "jobExecutionsRolloutConfig": NotRequired[IoTJobExecutionsRolloutConfigTypeDef],
        "abortConfig": NotRequired[IoTJobAbortConfigOutputTypeDef],
        "timeoutConfig": NotRequired[IoTJobTimeoutConfigTypeDef],
    },
)
DeploymentIoTJobConfigurationTypeDef = TypedDict(
    "DeploymentIoTJobConfigurationTypeDef",
    {
        "jobExecutionsRolloutConfig": NotRequired[IoTJobExecutionsRolloutConfigTypeDef],
        "abortConfig": NotRequired[IoTJobAbortConfigUnionTypeDef],
        "timeoutConfig": NotRequired[IoTJobTimeoutConfigTypeDef],
    },
)
LambdaExecutionParametersTypeDef = TypedDict(
    "LambdaExecutionParametersTypeDef",
    {
        "eventSources": NotRequired[Sequence[LambdaEventSourceTypeDef]],
        "maxQueueSize": NotRequired[int],
        "maxInstancesCount": NotRequired[int],
        "maxIdleTimeInSeconds": NotRequired[int],
        "timeoutInSeconds": NotRequired[int],
        "statusTimeoutInSeconds": NotRequired[int],
        "pinned": NotRequired[bool],
        "inputPayloadEncodingType": NotRequired[LambdaInputPayloadEncodingTypeType],
        "execArgs": NotRequired[Sequence[str]],
        "environmentVariables": NotRequired[Mapping[str, str]],
        "linuxProcessParams": NotRequired[LambdaLinuxProcessParamsTypeDef],
    },
)
GetDeploymentResponseTypeDef = TypedDict(
    "GetDeploymentResponseTypeDef",
    {
        "targetArn": str,
        "revisionId": str,
        "deploymentId": str,
        "deploymentName": str,
        "deploymentStatus": DeploymentStatusType,
        "iotJobId": str,
        "iotJobArn": str,
        "components": Dict[str, ComponentDeploymentSpecificationOutputTypeDef],
        "deploymentPolicies": DeploymentPoliciesTypeDef,
        "iotJobConfiguration": DeploymentIoTJobConfigurationOutputTypeDef,
        "creationTimestamp": datetime,
        "isLatestForTarget": bool,
        "parentTargetArn": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDeploymentRequestRequestTypeDef = TypedDict(
    "CreateDeploymentRequestRequestTypeDef",
    {
        "targetArn": str,
        "deploymentName": NotRequired[str],
        "components": NotRequired[Mapping[str, ComponentDeploymentSpecificationUnionTypeDef]],
        "iotJobConfiguration": NotRequired[DeploymentIoTJobConfigurationTypeDef],
        "deploymentPolicies": NotRequired[DeploymentPoliciesTypeDef],
        "parentTargetArn": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "clientToken": NotRequired[str],
    },
)
LambdaFunctionRecipeSourceTypeDef = TypedDict(
    "LambdaFunctionRecipeSourceTypeDef",
    {
        "lambdaArn": str,
        "componentName": NotRequired[str],
        "componentVersion": NotRequired[str],
        "componentPlatforms": NotRequired[Sequence[ComponentPlatformUnionTypeDef]],
        "componentDependencies": NotRequired[Mapping[str, ComponentDependencyRequirementTypeDef]],
        "componentLambdaParameters": NotRequired[LambdaExecutionParametersTypeDef],
    },
)
CreateComponentVersionRequestRequestTypeDef = TypedDict(
    "CreateComponentVersionRequestRequestTypeDef",
    {
        "inlineRecipe": NotRequired[BlobTypeDef],
        "lambdaFunction": NotRequired[LambdaFunctionRecipeSourceTypeDef],
        "tags": NotRequired[Mapping[str, str]],
        "clientToken": NotRequired[str],
    },
)
