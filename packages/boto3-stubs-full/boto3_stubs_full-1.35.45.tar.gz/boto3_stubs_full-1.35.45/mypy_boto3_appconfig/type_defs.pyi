"""
Type annotations for appconfig service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfig/type_defs/)

Usage::

    ```python
    from mypy_boto3_appconfig.type_defs import DeletionProtectionSettingsTypeDef

    data: DeletionProtectionSettingsTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    ActionPointType,
    DeletionProtectionCheckType,
    DeploymentEventTypeType,
    DeploymentStateType,
    EnvironmentStateType,
    GrowthTypeType,
    ReplicateToType,
    TriggeredByType,
    ValidatorTypeType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "DeletionProtectionSettingsTypeDef",
    "ResponseMetadataTypeDef",
    "ActionInvocationTypeDef",
    "ActionTypeDef",
    "ApplicationTypeDef",
    "AppliedExtensionTypeDef",
    "BlobTypeDef",
    "ConfigurationProfileSummaryTypeDef",
    "ValidatorTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "CreateDeploymentStrategyRequestRequestTypeDef",
    "MonitorTypeDef",
    "CreateExtensionAssociationRequestRequestTypeDef",
    "ParameterTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "DeleteConfigurationProfileRequestRequestTypeDef",
    "DeleteDeploymentStrategyRequestRequestTypeDef",
    "DeleteEnvironmentRequestRequestTypeDef",
    "DeleteExtensionAssociationRequestRequestTypeDef",
    "DeleteExtensionRequestRequestTypeDef",
    "DeleteHostedConfigurationVersionRequestRequestTypeDef",
    "DeploymentStrategyTypeDef",
    "DeploymentSummaryTypeDef",
    "ExtensionAssociationSummaryTypeDef",
    "ExtensionSummaryTypeDef",
    "GetApplicationRequestRequestTypeDef",
    "GetConfigurationProfileRequestRequestTypeDef",
    "GetConfigurationRequestRequestTypeDef",
    "GetDeploymentRequestRequestTypeDef",
    "GetDeploymentStrategyRequestRequestTypeDef",
    "GetEnvironmentRequestRequestTypeDef",
    "GetExtensionAssociationRequestRequestTypeDef",
    "GetExtensionRequestRequestTypeDef",
    "GetHostedConfigurationVersionRequestRequestTypeDef",
    "HostedConfigurationVersionSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "ListConfigurationProfilesRequestRequestTypeDef",
    "ListDeploymentStrategiesRequestRequestTypeDef",
    "ListDeploymentsRequestRequestTypeDef",
    "ListEnvironmentsRequestRequestTypeDef",
    "ListExtensionAssociationsRequestRequestTypeDef",
    "ListExtensionsRequestRequestTypeDef",
    "ListHostedConfigurationVersionsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "StartDeploymentRequestRequestTypeDef",
    "StopDeploymentRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
    "UpdateDeploymentStrategyRequestRequestTypeDef",
    "UpdateExtensionAssociationRequestRequestTypeDef",
    "ValidateConfigurationRequestRequestTypeDef",
    "UpdateAccountSettingsRequestRequestTypeDef",
    "AccountSettingsTypeDef",
    "ApplicationResponseTypeDef",
    "ConfigurationTypeDef",
    "DeploymentStrategyResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ExtensionAssociationTypeDef",
    "HostedConfigurationVersionTypeDef",
    "ResourceTagsTypeDef",
    "DeploymentEventTypeDef",
    "ApplicationsTypeDef",
    "CreateHostedConfigurationVersionRequestRequestTypeDef",
    "ConfigurationProfilesTypeDef",
    "ConfigurationProfileTypeDef",
    "CreateConfigurationProfileRequestRequestTypeDef",
    "UpdateConfigurationProfileRequestRequestTypeDef",
    "CreateEnvironmentRequestRequestTypeDef",
    "EnvironmentResponseTypeDef",
    "EnvironmentTypeDef",
    "UpdateEnvironmentRequestRequestTypeDef",
    "CreateExtensionRequestRequestTypeDef",
    "ExtensionTypeDef",
    "UpdateExtensionRequestRequestTypeDef",
    "DeploymentStrategiesTypeDef",
    "DeploymentsTypeDef",
    "ExtensionAssociationsTypeDef",
    "ExtensionsTypeDef",
    "HostedConfigurationVersionsTypeDef",
    "ListApplicationsRequestListApplicationsPaginateTypeDef",
    "ListConfigurationProfilesRequestListConfigurationProfilesPaginateTypeDef",
    "ListDeploymentStrategiesRequestListDeploymentStrategiesPaginateTypeDef",
    "ListDeploymentsRequestListDeploymentsPaginateTypeDef",
    "ListEnvironmentsRequestListEnvironmentsPaginateTypeDef",
    "ListExtensionAssociationsRequestListExtensionAssociationsPaginateTypeDef",
    "ListExtensionsRequestListExtensionsPaginateTypeDef",
    "ListHostedConfigurationVersionsRequestListHostedConfigurationVersionsPaginateTypeDef",
    "DeploymentTypeDef",
    "EnvironmentsTypeDef",
)

DeletionProtectionSettingsTypeDef = TypedDict(
    "DeletionProtectionSettingsTypeDef",
    {
        "Enabled": NotRequired[bool],
        "ProtectionPeriodInMinutes": NotRequired[int],
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
ActionInvocationTypeDef = TypedDict(
    "ActionInvocationTypeDef",
    {
        "ExtensionIdentifier": NotRequired[str],
        "ActionName": NotRequired[str],
        "Uri": NotRequired[str],
        "RoleArn": NotRequired[str],
        "ErrorMessage": NotRequired[str],
        "ErrorCode": NotRequired[str],
        "InvocationId": NotRequired[str],
    },
)
ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Uri": NotRequired[str],
        "RoleArn": NotRequired[str],
    },
)
ApplicationTypeDef = TypedDict(
    "ApplicationTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
    },
)
AppliedExtensionTypeDef = TypedDict(
    "AppliedExtensionTypeDef",
    {
        "ExtensionId": NotRequired[str],
        "ExtensionAssociationId": NotRequired[str],
        "VersionNumber": NotRequired[int],
        "Parameters": NotRequired[Dict[str, str]],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
ConfigurationProfileSummaryTypeDef = TypedDict(
    "ConfigurationProfileSummaryTypeDef",
    {
        "ApplicationId": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "LocationUri": NotRequired[str],
        "ValidatorTypes": NotRequired[List[ValidatorTypeType]],
        "Type": NotRequired[str],
    },
)
ValidatorTypeDef = TypedDict(
    "ValidatorTypeDef",
    {
        "Type": ValidatorTypeType,
        "Content": str,
    },
)
CreateApplicationRequestRequestTypeDef = TypedDict(
    "CreateApplicationRequestRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CreateDeploymentStrategyRequestRequestTypeDef = TypedDict(
    "CreateDeploymentStrategyRequestRequestTypeDef",
    {
        "Name": str,
        "DeploymentDurationInMinutes": int,
        "GrowthFactor": float,
        "Description": NotRequired[str],
        "FinalBakeTimeInMinutes": NotRequired[int],
        "GrowthType": NotRequired[GrowthTypeType],
        "ReplicateTo": NotRequired[ReplicateToType],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
MonitorTypeDef = TypedDict(
    "MonitorTypeDef",
    {
        "AlarmArn": str,
        "AlarmRoleArn": NotRequired[str],
    },
)
CreateExtensionAssociationRequestRequestTypeDef = TypedDict(
    "CreateExtensionAssociationRequestRequestTypeDef",
    {
        "ExtensionIdentifier": str,
        "ResourceIdentifier": str,
        "ExtensionVersionNumber": NotRequired[int],
        "Parameters": NotRequired[Mapping[str, str]],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "Description": NotRequired[str],
        "Required": NotRequired[bool],
        "Dynamic": NotRequired[bool],
    },
)
DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
DeleteConfigurationProfileRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationProfileRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
        "DeletionProtectionCheck": NotRequired[DeletionProtectionCheckType],
    },
)
DeleteDeploymentStrategyRequestRequestTypeDef = TypedDict(
    "DeleteDeploymentStrategyRequestRequestTypeDef",
    {
        "DeploymentStrategyId": str,
    },
)
DeleteEnvironmentRequestRequestTypeDef = TypedDict(
    "DeleteEnvironmentRequestRequestTypeDef",
    {
        "EnvironmentId": str,
        "ApplicationId": str,
        "DeletionProtectionCheck": NotRequired[DeletionProtectionCheckType],
    },
)
DeleteExtensionAssociationRequestRequestTypeDef = TypedDict(
    "DeleteExtensionAssociationRequestRequestTypeDef",
    {
        "ExtensionAssociationId": str,
    },
)
DeleteExtensionRequestRequestTypeDef = TypedDict(
    "DeleteExtensionRequestRequestTypeDef",
    {
        "ExtensionIdentifier": str,
        "VersionNumber": NotRequired[int],
    },
)
DeleteHostedConfigurationVersionRequestRequestTypeDef = TypedDict(
    "DeleteHostedConfigurationVersionRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
        "VersionNumber": int,
    },
)
DeploymentStrategyTypeDef = TypedDict(
    "DeploymentStrategyTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "DeploymentDurationInMinutes": NotRequired[int],
        "GrowthType": NotRequired[GrowthTypeType],
        "GrowthFactor": NotRequired[float],
        "FinalBakeTimeInMinutes": NotRequired[int],
        "ReplicateTo": NotRequired[ReplicateToType],
    },
)
DeploymentSummaryTypeDef = TypedDict(
    "DeploymentSummaryTypeDef",
    {
        "DeploymentNumber": NotRequired[int],
        "ConfigurationName": NotRequired[str],
        "ConfigurationVersion": NotRequired[str],
        "DeploymentDurationInMinutes": NotRequired[int],
        "GrowthType": NotRequired[GrowthTypeType],
        "GrowthFactor": NotRequired[float],
        "FinalBakeTimeInMinutes": NotRequired[int],
        "State": NotRequired[DeploymentStateType],
        "PercentageComplete": NotRequired[float],
        "StartedAt": NotRequired[datetime],
        "CompletedAt": NotRequired[datetime],
        "VersionLabel": NotRequired[str],
    },
)
ExtensionAssociationSummaryTypeDef = TypedDict(
    "ExtensionAssociationSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "ExtensionArn": NotRequired[str],
        "ResourceArn": NotRequired[str],
    },
)
ExtensionSummaryTypeDef = TypedDict(
    "ExtensionSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "VersionNumber": NotRequired[int],
        "Arn": NotRequired[str],
        "Description": NotRequired[str],
    },
)
GetApplicationRequestRequestTypeDef = TypedDict(
    "GetApplicationRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
GetConfigurationProfileRequestRequestTypeDef = TypedDict(
    "GetConfigurationProfileRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
    },
)
GetConfigurationRequestRequestTypeDef = TypedDict(
    "GetConfigurationRequestRequestTypeDef",
    {
        "Application": str,
        "Environment": str,
        "Configuration": str,
        "ClientId": str,
        "ClientConfigurationVersion": NotRequired[str],
    },
)
GetDeploymentRequestRequestTypeDef = TypedDict(
    "GetDeploymentRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
        "DeploymentNumber": int,
    },
)
GetDeploymentStrategyRequestRequestTypeDef = TypedDict(
    "GetDeploymentStrategyRequestRequestTypeDef",
    {
        "DeploymentStrategyId": str,
    },
)
GetEnvironmentRequestRequestTypeDef = TypedDict(
    "GetEnvironmentRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
    },
)
GetExtensionAssociationRequestRequestTypeDef = TypedDict(
    "GetExtensionAssociationRequestRequestTypeDef",
    {
        "ExtensionAssociationId": str,
    },
)
GetExtensionRequestRequestTypeDef = TypedDict(
    "GetExtensionRequestRequestTypeDef",
    {
        "ExtensionIdentifier": str,
        "VersionNumber": NotRequired[int],
    },
)
GetHostedConfigurationVersionRequestRequestTypeDef = TypedDict(
    "GetHostedConfigurationVersionRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
        "VersionNumber": int,
    },
)
HostedConfigurationVersionSummaryTypeDef = TypedDict(
    "HostedConfigurationVersionSummaryTypeDef",
    {
        "ApplicationId": NotRequired[str],
        "ConfigurationProfileId": NotRequired[str],
        "VersionNumber": NotRequired[int],
        "Description": NotRequired[str],
        "ContentType": NotRequired[str],
        "VersionLabel": NotRequired[str],
        "KmsKeyArn": NotRequired[str],
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
ListApplicationsRequestRequestTypeDef = TypedDict(
    "ListApplicationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListConfigurationProfilesRequestRequestTypeDef = TypedDict(
    "ListConfigurationProfilesRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Type": NotRequired[str],
    },
)
ListDeploymentStrategiesRequestRequestTypeDef = TypedDict(
    "ListDeploymentStrategiesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListDeploymentsRequestRequestTypeDef = TypedDict(
    "ListDeploymentsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListEnvironmentsRequestRequestTypeDef = TypedDict(
    "ListEnvironmentsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListExtensionAssociationsRequestRequestTypeDef = TypedDict(
    "ListExtensionAssociationsRequestRequestTypeDef",
    {
        "ResourceIdentifier": NotRequired[str],
        "ExtensionIdentifier": NotRequired[str],
        "ExtensionVersionNumber": NotRequired[int],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListExtensionsRequestRequestTypeDef = TypedDict(
    "ListExtensionsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Name": NotRequired[str],
    },
)
ListHostedConfigurationVersionsRequestRequestTypeDef = TypedDict(
    "ListHostedConfigurationVersionsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "VersionLabel": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
StartDeploymentRequestRequestTypeDef = TypedDict(
    "StartDeploymentRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
        "DeploymentStrategyId": str,
        "ConfigurationProfileId": str,
        "ConfigurationVersion": str,
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "KmsKeyIdentifier": NotRequired[str],
        "DynamicExtensionParameters": NotRequired[Mapping[str, str]],
    },
)
StopDeploymentRequestRequestTypeDef = TypedDict(
    "StopDeploymentRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
        "DeploymentNumber": int,
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
UpdateApplicationRequestRequestTypeDef = TypedDict(
    "UpdateApplicationRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
    },
)
UpdateDeploymentStrategyRequestRequestTypeDef = TypedDict(
    "UpdateDeploymentStrategyRequestRequestTypeDef",
    {
        "DeploymentStrategyId": str,
        "Description": NotRequired[str],
        "DeploymentDurationInMinutes": NotRequired[int],
        "FinalBakeTimeInMinutes": NotRequired[int],
        "GrowthFactor": NotRequired[float],
        "GrowthType": NotRequired[GrowthTypeType],
    },
)
UpdateExtensionAssociationRequestRequestTypeDef = TypedDict(
    "UpdateExtensionAssociationRequestRequestTypeDef",
    {
        "ExtensionAssociationId": str,
        "Parameters": NotRequired[Mapping[str, str]],
    },
)
ValidateConfigurationRequestRequestTypeDef = TypedDict(
    "ValidateConfigurationRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
        "ConfigurationVersion": str,
    },
)
UpdateAccountSettingsRequestRequestTypeDef = TypedDict(
    "UpdateAccountSettingsRequestRequestTypeDef",
    {
        "DeletionProtection": NotRequired[DeletionProtectionSettingsTypeDef],
    },
)
AccountSettingsTypeDef = TypedDict(
    "AccountSettingsTypeDef",
    {
        "DeletionProtection": DeletionProtectionSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ApplicationResponseTypeDef = TypedDict(
    "ApplicationResponseTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "Content": StreamingBody,
        "ConfigurationVersion": str,
        "ContentType": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeploymentStrategyResponseTypeDef = TypedDict(
    "DeploymentStrategyResponseTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "DeploymentDurationInMinutes": int,
        "GrowthType": GrowthTypeType,
        "GrowthFactor": float,
        "FinalBakeTimeInMinutes": int,
        "ReplicateTo": ReplicateToType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExtensionAssociationTypeDef = TypedDict(
    "ExtensionAssociationTypeDef",
    {
        "Id": str,
        "ExtensionArn": str,
        "ResourceArn": str,
        "Arn": str,
        "Parameters": Dict[str, str],
        "ExtensionVersionNumber": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
HostedConfigurationVersionTypeDef = TypedDict(
    "HostedConfigurationVersionTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
        "VersionNumber": int,
        "Description": str,
        "Content": StreamingBody,
        "ContentType": str,
        "VersionLabel": str,
        "KmsKeyArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResourceTagsTypeDef = TypedDict(
    "ResourceTagsTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeploymentEventTypeDef = TypedDict(
    "DeploymentEventTypeDef",
    {
        "EventType": NotRequired[DeploymentEventTypeType],
        "TriggeredBy": NotRequired[TriggeredByType],
        "Description": NotRequired[str],
        "ActionInvocations": NotRequired[List[ActionInvocationTypeDef]],
        "OccurredAt": NotRequired[datetime],
    },
)
ApplicationsTypeDef = TypedDict(
    "ApplicationsTypeDef",
    {
        "Items": List[ApplicationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateHostedConfigurationVersionRequestRequestTypeDef = TypedDict(
    "CreateHostedConfigurationVersionRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
        "Content": BlobTypeDef,
        "ContentType": str,
        "Description": NotRequired[str],
        "LatestVersionNumber": NotRequired[int],
        "VersionLabel": NotRequired[str],
    },
)
ConfigurationProfilesTypeDef = TypedDict(
    "ConfigurationProfilesTypeDef",
    {
        "Items": List[ConfigurationProfileSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ConfigurationProfileTypeDef = TypedDict(
    "ConfigurationProfileTypeDef",
    {
        "ApplicationId": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "LocationUri": str,
        "RetrievalRoleArn": str,
        "Validators": List[ValidatorTypeDef],
        "Type": str,
        "KmsKeyArn": str,
        "KmsKeyIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateConfigurationProfileRequestRequestTypeDef = TypedDict(
    "CreateConfigurationProfileRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "Name": str,
        "LocationUri": str,
        "Description": NotRequired[str],
        "RetrievalRoleArn": NotRequired[str],
        "Validators": NotRequired[Sequence[ValidatorTypeDef]],
        "Tags": NotRequired[Mapping[str, str]],
        "Type": NotRequired[str],
        "KmsKeyIdentifier": NotRequired[str],
    },
)
UpdateConfigurationProfileRequestRequestTypeDef = TypedDict(
    "UpdateConfigurationProfileRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "RetrievalRoleArn": NotRequired[str],
        "Validators": NotRequired[Sequence[ValidatorTypeDef]],
        "KmsKeyIdentifier": NotRequired[str],
    },
)
CreateEnvironmentRequestRequestTypeDef = TypedDict(
    "CreateEnvironmentRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "Name": str,
        "Description": NotRequired[str],
        "Monitors": NotRequired[Sequence[MonitorTypeDef]],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
EnvironmentResponseTypeDef = TypedDict(
    "EnvironmentResponseTypeDef",
    {
        "ApplicationId": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "State": EnvironmentStateType,
        "Monitors": List[MonitorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnvironmentTypeDef = TypedDict(
    "EnvironmentTypeDef",
    {
        "ApplicationId": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "State": NotRequired[EnvironmentStateType],
        "Monitors": NotRequired[List[MonitorTypeDef]],
    },
)
UpdateEnvironmentRequestRequestTypeDef = TypedDict(
    "UpdateEnvironmentRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Monitors": NotRequired[Sequence[MonitorTypeDef]],
    },
)
CreateExtensionRequestRequestTypeDef = TypedDict(
    "CreateExtensionRequestRequestTypeDef",
    {
        "Name": str,
        "Actions": Mapping[ActionPointType, Sequence[ActionTypeDef]],
        "Description": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, ParameterTypeDef]],
        "Tags": NotRequired[Mapping[str, str]],
        "LatestVersionNumber": NotRequired[int],
    },
)
ExtensionTypeDef = TypedDict(
    "ExtensionTypeDef",
    {
        "Id": str,
        "Name": str,
        "VersionNumber": int,
        "Arn": str,
        "Description": str,
        "Actions": Dict[ActionPointType, List[ActionTypeDef]],
        "Parameters": Dict[str, ParameterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateExtensionRequestRequestTypeDef = TypedDict(
    "UpdateExtensionRequestRequestTypeDef",
    {
        "ExtensionIdentifier": str,
        "Description": NotRequired[str],
        "Actions": NotRequired[Mapping[ActionPointType, Sequence[ActionTypeDef]]],
        "Parameters": NotRequired[Mapping[str, ParameterTypeDef]],
        "VersionNumber": NotRequired[int],
    },
)
DeploymentStrategiesTypeDef = TypedDict(
    "DeploymentStrategiesTypeDef",
    {
        "Items": List[DeploymentStrategyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DeploymentsTypeDef = TypedDict(
    "DeploymentsTypeDef",
    {
        "Items": List[DeploymentSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ExtensionAssociationsTypeDef = TypedDict(
    "ExtensionAssociationsTypeDef",
    {
        "Items": List[ExtensionAssociationSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ExtensionsTypeDef = TypedDict(
    "ExtensionsTypeDef",
    {
        "Items": List[ExtensionSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
HostedConfigurationVersionsTypeDef = TypedDict(
    "HostedConfigurationVersionsTypeDef",
    {
        "Items": List[HostedConfigurationVersionSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListApplicationsRequestListApplicationsPaginateTypeDef = TypedDict(
    "ListApplicationsRequestListApplicationsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListConfigurationProfilesRequestListConfigurationProfilesPaginateTypeDef = TypedDict(
    "ListConfigurationProfilesRequestListConfigurationProfilesPaginateTypeDef",
    {
        "ApplicationId": str,
        "Type": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDeploymentStrategiesRequestListDeploymentStrategiesPaginateTypeDef = TypedDict(
    "ListDeploymentStrategiesRequestListDeploymentStrategiesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDeploymentsRequestListDeploymentsPaginateTypeDef = TypedDict(
    "ListDeploymentsRequestListDeploymentsPaginateTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEnvironmentsRequestListEnvironmentsPaginateTypeDef = TypedDict(
    "ListEnvironmentsRequestListEnvironmentsPaginateTypeDef",
    {
        "ApplicationId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListExtensionAssociationsRequestListExtensionAssociationsPaginateTypeDef = TypedDict(
    "ListExtensionAssociationsRequestListExtensionAssociationsPaginateTypeDef",
    {
        "ResourceIdentifier": NotRequired[str],
        "ExtensionIdentifier": NotRequired[str],
        "ExtensionVersionNumber": NotRequired[int],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListExtensionsRequestListExtensionsPaginateTypeDef = TypedDict(
    "ListExtensionsRequestListExtensionsPaginateTypeDef",
    {
        "Name": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListHostedConfigurationVersionsRequestListHostedConfigurationVersionsPaginateTypeDef = TypedDict(
    "ListHostedConfigurationVersionsRequestListHostedConfigurationVersionsPaginateTypeDef",
    {
        "ApplicationId": str,
        "ConfigurationProfileId": str,
        "VersionLabel": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "ApplicationId": str,
        "EnvironmentId": str,
        "DeploymentStrategyId": str,
        "ConfigurationProfileId": str,
        "DeploymentNumber": int,
        "ConfigurationName": str,
        "ConfigurationLocationUri": str,
        "ConfigurationVersion": str,
        "Description": str,
        "DeploymentDurationInMinutes": int,
        "GrowthType": GrowthTypeType,
        "GrowthFactor": float,
        "FinalBakeTimeInMinutes": int,
        "State": DeploymentStateType,
        "EventLog": List[DeploymentEventTypeDef],
        "PercentageComplete": float,
        "StartedAt": datetime,
        "CompletedAt": datetime,
        "AppliedExtensions": List[AppliedExtensionTypeDef],
        "KmsKeyArn": str,
        "KmsKeyIdentifier": str,
        "VersionLabel": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnvironmentsTypeDef = TypedDict(
    "EnvironmentsTypeDef",
    {
        "Items": List[EnvironmentTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
