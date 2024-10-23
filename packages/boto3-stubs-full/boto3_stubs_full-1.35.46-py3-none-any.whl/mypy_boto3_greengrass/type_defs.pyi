"""
Type annotations for greengrass service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrass/type_defs/)

Usage::

    ```python
    from mypy_boto3_greengrass.type_defs import AssociateRoleToGroupRequestRequestTypeDef

    data: AssociateRoleToGroupRequestRequestTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    BulkDeploymentStatusType,
    ConfigurationSyncStatusType,
    DeploymentTypeType,
    EncodingTypeType,
    FunctionIsolationModeType,
    LoggerComponentType,
    LoggerLevelType,
    LoggerTypeType,
    PermissionType,
    SoftwareToUpdateType,
    TelemetryType,
    UpdateAgentLogLevelType,
    UpdateTargetsArchitectureType,
    UpdateTargetsOperatingSystemType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AssociateRoleToGroupRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "AssociateServiceRoleToAccountRequestRequestTypeDef",
    "BulkDeploymentMetricsTypeDef",
    "ErrorDetailTypeDef",
    "BulkDeploymentTypeDef",
    "ConnectivityInfoTypeDef",
    "ConnectorOutputTypeDef",
    "ConnectorTypeDef",
    "CoreTypeDef",
    "CreateDeploymentRequestRequestTypeDef",
    "DeviceTypeDef",
    "CreateGroupCertificateAuthorityRequestRequestTypeDef",
    "GroupVersionTypeDef",
    "CreateGroupVersionRequestRequestTypeDef",
    "LoggerTypeDef",
    "CreateSoftwareUpdateJobRequestRequestTypeDef",
    "SubscriptionTypeDef",
    "DefinitionInformationTypeDef",
    "DeleteConnectorDefinitionRequestRequestTypeDef",
    "DeleteCoreDefinitionRequestRequestTypeDef",
    "DeleteDeviceDefinitionRequestRequestTypeDef",
    "DeleteFunctionDefinitionRequestRequestTypeDef",
    "DeleteGroupRequestRequestTypeDef",
    "DeleteLoggerDefinitionRequestRequestTypeDef",
    "DeleteResourceDefinitionRequestRequestTypeDef",
    "DeleteSubscriptionDefinitionRequestRequestTypeDef",
    "DeploymentTypeDef",
    "DisassociateRoleFromGroupRequestRequestTypeDef",
    "ResourceAccessPolicyTypeDef",
    "FunctionRunAsConfigTypeDef",
    "GetAssociatedRoleRequestRequestTypeDef",
    "GetBulkDeploymentStatusRequestRequestTypeDef",
    "GetConnectivityInfoRequestRequestTypeDef",
    "GetConnectorDefinitionRequestRequestTypeDef",
    "GetConnectorDefinitionVersionRequestRequestTypeDef",
    "GetCoreDefinitionRequestRequestTypeDef",
    "GetCoreDefinitionVersionRequestRequestTypeDef",
    "GetDeploymentStatusRequestRequestTypeDef",
    "GetDeviceDefinitionRequestRequestTypeDef",
    "GetDeviceDefinitionVersionRequestRequestTypeDef",
    "GetFunctionDefinitionRequestRequestTypeDef",
    "GetFunctionDefinitionVersionRequestRequestTypeDef",
    "GetGroupCertificateAuthorityRequestRequestTypeDef",
    "GetGroupCertificateConfigurationRequestRequestTypeDef",
    "GetGroupRequestRequestTypeDef",
    "GetGroupVersionRequestRequestTypeDef",
    "GetLoggerDefinitionRequestRequestTypeDef",
    "GetLoggerDefinitionVersionRequestRequestTypeDef",
    "GetResourceDefinitionRequestRequestTypeDef",
    "GetResourceDefinitionVersionRequestRequestTypeDef",
    "GetSubscriptionDefinitionRequestRequestTypeDef",
    "GetSubscriptionDefinitionVersionRequestRequestTypeDef",
    "GetThingRuntimeConfigurationRequestRequestTypeDef",
    "GroupCertificateAuthorityPropertiesTypeDef",
    "GroupInformationTypeDef",
    "GroupOwnerSettingTypeDef",
    "PaginatorConfigTypeDef",
    "ListBulkDeploymentDetailedReportsRequestRequestTypeDef",
    "ListBulkDeploymentsRequestRequestTypeDef",
    "ListConnectorDefinitionVersionsRequestRequestTypeDef",
    "VersionInformationTypeDef",
    "ListConnectorDefinitionsRequestRequestTypeDef",
    "ListCoreDefinitionVersionsRequestRequestTypeDef",
    "ListCoreDefinitionsRequestRequestTypeDef",
    "ListDeploymentsRequestRequestTypeDef",
    "ListDeviceDefinitionVersionsRequestRequestTypeDef",
    "ListDeviceDefinitionsRequestRequestTypeDef",
    "ListFunctionDefinitionVersionsRequestRequestTypeDef",
    "ListFunctionDefinitionsRequestRequestTypeDef",
    "ListGroupCertificateAuthoritiesRequestRequestTypeDef",
    "ListGroupVersionsRequestRequestTypeDef",
    "ListGroupsRequestRequestTypeDef",
    "ListLoggerDefinitionVersionsRequestRequestTypeDef",
    "ListLoggerDefinitionsRequestRequestTypeDef",
    "ListResourceDefinitionVersionsRequestRequestTypeDef",
    "ListResourceDefinitionsRequestRequestTypeDef",
    "ListSubscriptionDefinitionVersionsRequestRequestTypeDef",
    "ListSubscriptionDefinitionsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ResetDeploymentsRequestRequestTypeDef",
    "SecretsManagerSecretResourceDataOutputTypeDef",
    "ResourceDownloadOwnerSettingTypeDef",
    "TelemetryConfigurationTypeDef",
    "SecretsManagerSecretResourceDataTypeDef",
    "StartBulkDeploymentRequestRequestTypeDef",
    "StopBulkDeploymentRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TelemetryConfigurationUpdateTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateConnectorDefinitionRequestRequestTypeDef",
    "UpdateCoreDefinitionRequestRequestTypeDef",
    "UpdateDeviceDefinitionRequestRequestTypeDef",
    "UpdateFunctionDefinitionRequestRequestTypeDef",
    "UpdateGroupCertificateConfigurationRequestRequestTypeDef",
    "UpdateGroupRequestRequestTypeDef",
    "UpdateLoggerDefinitionRequestRequestTypeDef",
    "UpdateResourceDefinitionRequestRequestTypeDef",
    "UpdateSubscriptionDefinitionRequestRequestTypeDef",
    "AssociateRoleToGroupResponseTypeDef",
    "AssociateServiceRoleToAccountResponseTypeDef",
    "CreateConnectorDefinitionResponseTypeDef",
    "CreateConnectorDefinitionVersionResponseTypeDef",
    "CreateCoreDefinitionResponseTypeDef",
    "CreateCoreDefinitionVersionResponseTypeDef",
    "CreateDeploymentResponseTypeDef",
    "CreateDeviceDefinitionResponseTypeDef",
    "CreateDeviceDefinitionVersionResponseTypeDef",
    "CreateFunctionDefinitionResponseTypeDef",
    "CreateFunctionDefinitionVersionResponseTypeDef",
    "CreateGroupCertificateAuthorityResponseTypeDef",
    "CreateGroupResponseTypeDef",
    "CreateGroupVersionResponseTypeDef",
    "CreateLoggerDefinitionResponseTypeDef",
    "CreateLoggerDefinitionVersionResponseTypeDef",
    "CreateResourceDefinitionResponseTypeDef",
    "CreateResourceDefinitionVersionResponseTypeDef",
    "CreateSoftwareUpdateJobResponseTypeDef",
    "CreateSubscriptionDefinitionResponseTypeDef",
    "CreateSubscriptionDefinitionVersionResponseTypeDef",
    "DisassociateRoleFromGroupResponseTypeDef",
    "DisassociateServiceRoleFromAccountResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetAssociatedRoleResponseTypeDef",
    "GetConnectorDefinitionResponseTypeDef",
    "GetCoreDefinitionResponseTypeDef",
    "GetDeviceDefinitionResponseTypeDef",
    "GetFunctionDefinitionResponseTypeDef",
    "GetGroupCertificateAuthorityResponseTypeDef",
    "GetGroupCertificateConfigurationResponseTypeDef",
    "GetGroupResponseTypeDef",
    "GetLoggerDefinitionResponseTypeDef",
    "GetResourceDefinitionResponseTypeDef",
    "GetServiceRoleForAccountResponseTypeDef",
    "GetSubscriptionDefinitionResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ResetDeploymentsResponseTypeDef",
    "StartBulkDeploymentResponseTypeDef",
    "UpdateConnectivityInfoResponseTypeDef",
    "UpdateGroupCertificateConfigurationResponseTypeDef",
    "BulkDeploymentResultTypeDef",
    "GetBulkDeploymentStatusResponseTypeDef",
    "GetDeploymentStatusResponseTypeDef",
    "ListBulkDeploymentsResponseTypeDef",
    "GetConnectivityInfoResponseTypeDef",
    "UpdateConnectivityInfoRequestRequestTypeDef",
    "ConnectorDefinitionVersionOutputTypeDef",
    "ConnectorUnionTypeDef",
    "CoreDefinitionVersionOutputTypeDef",
    "CoreDefinitionVersionTypeDef",
    "CreateCoreDefinitionVersionRequestRequestTypeDef",
    "CreateDeviceDefinitionVersionRequestRequestTypeDef",
    "DeviceDefinitionVersionOutputTypeDef",
    "DeviceDefinitionVersionTypeDef",
    "CreateGroupRequestRequestTypeDef",
    "GetGroupVersionResponseTypeDef",
    "CreateLoggerDefinitionVersionRequestRequestTypeDef",
    "LoggerDefinitionVersionOutputTypeDef",
    "LoggerDefinitionVersionTypeDef",
    "CreateSubscriptionDefinitionVersionRequestRequestTypeDef",
    "SubscriptionDefinitionVersionOutputTypeDef",
    "SubscriptionDefinitionVersionTypeDef",
    "ListConnectorDefinitionsResponseTypeDef",
    "ListCoreDefinitionsResponseTypeDef",
    "ListDeviceDefinitionsResponseTypeDef",
    "ListFunctionDefinitionsResponseTypeDef",
    "ListLoggerDefinitionsResponseTypeDef",
    "ListResourceDefinitionsResponseTypeDef",
    "ListSubscriptionDefinitionsResponseTypeDef",
    "ListDeploymentsResponseTypeDef",
    "FunctionDefaultExecutionConfigTypeDef",
    "FunctionExecutionConfigTypeDef",
    "ListGroupCertificateAuthoritiesResponseTypeDef",
    "ListGroupsResponseTypeDef",
    "LocalDeviceResourceDataTypeDef",
    "LocalVolumeResourceDataTypeDef",
    "ListBulkDeploymentDetailedReportsRequestListBulkDeploymentDetailedReportsPaginateTypeDef",
    "ListBulkDeploymentsRequestListBulkDeploymentsPaginateTypeDef",
    "ListConnectorDefinitionVersionsRequestListConnectorDefinitionVersionsPaginateTypeDef",
    "ListConnectorDefinitionsRequestListConnectorDefinitionsPaginateTypeDef",
    "ListCoreDefinitionVersionsRequestListCoreDefinitionVersionsPaginateTypeDef",
    "ListCoreDefinitionsRequestListCoreDefinitionsPaginateTypeDef",
    "ListDeploymentsRequestListDeploymentsPaginateTypeDef",
    "ListDeviceDefinitionVersionsRequestListDeviceDefinitionVersionsPaginateTypeDef",
    "ListDeviceDefinitionsRequestListDeviceDefinitionsPaginateTypeDef",
    "ListFunctionDefinitionVersionsRequestListFunctionDefinitionVersionsPaginateTypeDef",
    "ListFunctionDefinitionsRequestListFunctionDefinitionsPaginateTypeDef",
    "ListGroupVersionsRequestListGroupVersionsPaginateTypeDef",
    "ListGroupsRequestListGroupsPaginateTypeDef",
    "ListLoggerDefinitionVersionsRequestListLoggerDefinitionVersionsPaginateTypeDef",
    "ListLoggerDefinitionsRequestListLoggerDefinitionsPaginateTypeDef",
    "ListResourceDefinitionVersionsRequestListResourceDefinitionVersionsPaginateTypeDef",
    "ListResourceDefinitionsRequestListResourceDefinitionsPaginateTypeDef",
    "ListSubscriptionDefinitionVersionsRequestListSubscriptionDefinitionVersionsPaginateTypeDef",
    "ListSubscriptionDefinitionsRequestListSubscriptionDefinitionsPaginateTypeDef",
    "ListConnectorDefinitionVersionsResponseTypeDef",
    "ListCoreDefinitionVersionsResponseTypeDef",
    "ListDeviceDefinitionVersionsResponseTypeDef",
    "ListFunctionDefinitionVersionsResponseTypeDef",
    "ListGroupVersionsResponseTypeDef",
    "ListLoggerDefinitionVersionsResponseTypeDef",
    "ListResourceDefinitionVersionsResponseTypeDef",
    "ListSubscriptionDefinitionVersionsResponseTypeDef",
    "S3MachineLearningModelResourceDataTypeDef",
    "SageMakerMachineLearningModelResourceDataTypeDef",
    "RuntimeConfigurationTypeDef",
    "SecretsManagerSecretResourceDataUnionTypeDef",
    "UpdateThingRuntimeConfigurationRequestRequestTypeDef",
    "ListBulkDeploymentDetailedReportsResponseTypeDef",
    "GetConnectorDefinitionVersionResponseTypeDef",
    "ConnectorDefinitionVersionTypeDef",
    "CreateConnectorDefinitionVersionRequestRequestTypeDef",
    "GetCoreDefinitionVersionResponseTypeDef",
    "CreateCoreDefinitionRequestRequestTypeDef",
    "GetDeviceDefinitionVersionResponseTypeDef",
    "CreateDeviceDefinitionRequestRequestTypeDef",
    "GetLoggerDefinitionVersionResponseTypeDef",
    "CreateLoggerDefinitionRequestRequestTypeDef",
    "GetSubscriptionDefinitionVersionResponseTypeDef",
    "CreateSubscriptionDefinitionRequestRequestTypeDef",
    "FunctionDefaultConfigTypeDef",
    "FunctionConfigurationEnvironmentOutputTypeDef",
    "FunctionConfigurationEnvironmentTypeDef",
    "ResourceDataContainerOutputTypeDef",
    "GetThingRuntimeConfigurationResponseTypeDef",
    "ResourceDataContainerTypeDef",
    "CreateConnectorDefinitionRequestRequestTypeDef",
    "FunctionConfigurationOutputTypeDef",
    "FunctionConfigurationEnvironmentUnionTypeDef",
    "ResourceOutputTypeDef",
    "ResourceDataContainerUnionTypeDef",
    "FunctionOutputTypeDef",
    "FunctionConfigurationTypeDef",
    "ResourceDefinitionVersionOutputTypeDef",
    "ResourceTypeDef",
    "FunctionDefinitionVersionOutputTypeDef",
    "FunctionConfigurationUnionTypeDef",
    "GetResourceDefinitionVersionResponseTypeDef",
    "ResourceUnionTypeDef",
    "GetFunctionDefinitionVersionResponseTypeDef",
    "FunctionTypeDef",
    "CreateResourceDefinitionVersionRequestRequestTypeDef",
    "ResourceDefinitionVersionTypeDef",
    "FunctionUnionTypeDef",
    "CreateResourceDefinitionRequestRequestTypeDef",
    "CreateFunctionDefinitionVersionRequestRequestTypeDef",
    "FunctionDefinitionVersionTypeDef",
    "CreateFunctionDefinitionRequestRequestTypeDef",
)

AssociateRoleToGroupRequestRequestTypeDef = TypedDict(
    "AssociateRoleToGroupRequestRequestTypeDef",
    {
        "GroupId": str,
        "RoleArn": str,
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
AssociateServiceRoleToAccountRequestRequestTypeDef = TypedDict(
    "AssociateServiceRoleToAccountRequestRequestTypeDef",
    {
        "RoleArn": str,
    },
)
BulkDeploymentMetricsTypeDef = TypedDict(
    "BulkDeploymentMetricsTypeDef",
    {
        "InvalidInputRecords": NotRequired[int],
        "RecordsProcessed": NotRequired[int],
        "RetryAttempts": NotRequired[int],
    },
)
ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef",
    {
        "DetailedErrorCode": NotRequired[str],
        "DetailedErrorMessage": NotRequired[str],
    },
)
BulkDeploymentTypeDef = TypedDict(
    "BulkDeploymentTypeDef",
    {
        "BulkDeploymentArn": NotRequired[str],
        "BulkDeploymentId": NotRequired[str],
        "CreatedAt": NotRequired[str],
    },
)
ConnectivityInfoTypeDef = TypedDict(
    "ConnectivityInfoTypeDef",
    {
        "HostAddress": NotRequired[str],
        "Id": NotRequired[str],
        "Metadata": NotRequired[str],
        "PortNumber": NotRequired[int],
    },
)
ConnectorOutputTypeDef = TypedDict(
    "ConnectorOutputTypeDef",
    {
        "ConnectorArn": str,
        "Id": str,
        "Parameters": NotRequired[Dict[str, str]],
    },
)
ConnectorTypeDef = TypedDict(
    "ConnectorTypeDef",
    {
        "ConnectorArn": str,
        "Id": str,
        "Parameters": NotRequired[Mapping[str, str]],
    },
)
CoreTypeDef = TypedDict(
    "CoreTypeDef",
    {
        "CertificateArn": str,
        "Id": str,
        "ThingArn": str,
        "SyncShadow": NotRequired[bool],
    },
)
CreateDeploymentRequestRequestTypeDef = TypedDict(
    "CreateDeploymentRequestRequestTypeDef",
    {
        "DeploymentType": DeploymentTypeType,
        "GroupId": str,
        "AmznClientToken": NotRequired[str],
        "DeploymentId": NotRequired[str],
        "GroupVersionId": NotRequired[str],
    },
)
DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "CertificateArn": str,
        "Id": str,
        "ThingArn": str,
        "SyncShadow": NotRequired[bool],
    },
)
CreateGroupCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "CreateGroupCertificateAuthorityRequestRequestTypeDef",
    {
        "GroupId": str,
        "AmznClientToken": NotRequired[str],
    },
)
GroupVersionTypeDef = TypedDict(
    "GroupVersionTypeDef",
    {
        "ConnectorDefinitionVersionArn": NotRequired[str],
        "CoreDefinitionVersionArn": NotRequired[str],
        "DeviceDefinitionVersionArn": NotRequired[str],
        "FunctionDefinitionVersionArn": NotRequired[str],
        "LoggerDefinitionVersionArn": NotRequired[str],
        "ResourceDefinitionVersionArn": NotRequired[str],
        "SubscriptionDefinitionVersionArn": NotRequired[str],
    },
)
CreateGroupVersionRequestRequestTypeDef = TypedDict(
    "CreateGroupVersionRequestRequestTypeDef",
    {
        "GroupId": str,
        "AmznClientToken": NotRequired[str],
        "ConnectorDefinitionVersionArn": NotRequired[str],
        "CoreDefinitionVersionArn": NotRequired[str],
        "DeviceDefinitionVersionArn": NotRequired[str],
        "FunctionDefinitionVersionArn": NotRequired[str],
        "LoggerDefinitionVersionArn": NotRequired[str],
        "ResourceDefinitionVersionArn": NotRequired[str],
        "SubscriptionDefinitionVersionArn": NotRequired[str],
    },
)
LoggerTypeDef = TypedDict(
    "LoggerTypeDef",
    {
        "Component": LoggerComponentType,
        "Id": str,
        "Level": LoggerLevelType,
        "Type": LoggerTypeType,
        "Space": NotRequired[int],
    },
)
CreateSoftwareUpdateJobRequestRequestTypeDef = TypedDict(
    "CreateSoftwareUpdateJobRequestRequestTypeDef",
    {
        "S3UrlSignerRole": str,
        "SoftwareToUpdate": SoftwareToUpdateType,
        "UpdateTargets": Sequence[str],
        "UpdateTargetsArchitecture": UpdateTargetsArchitectureType,
        "UpdateTargetsOperatingSystem": UpdateTargetsOperatingSystemType,
        "AmznClientToken": NotRequired[str],
        "UpdateAgentLogLevel": NotRequired[UpdateAgentLogLevelType],
    },
)
SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
    {
        "Id": str,
        "Source": str,
        "Subject": str,
        "Target": str,
    },
)
DefinitionInformationTypeDef = TypedDict(
    "DefinitionInformationTypeDef",
    {
        "Arn": NotRequired[str],
        "CreationTimestamp": NotRequired[str],
        "Id": NotRequired[str],
        "LastUpdatedTimestamp": NotRequired[str],
        "LatestVersion": NotRequired[str],
        "LatestVersionArn": NotRequired[str],
        "Name": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)
DeleteConnectorDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteConnectorDefinitionRequestRequestTypeDef",
    {
        "ConnectorDefinitionId": str,
    },
)
DeleteCoreDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteCoreDefinitionRequestRequestTypeDef",
    {
        "CoreDefinitionId": str,
    },
)
DeleteDeviceDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteDeviceDefinitionRequestRequestTypeDef",
    {
        "DeviceDefinitionId": str,
    },
)
DeleteFunctionDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteFunctionDefinitionRequestRequestTypeDef",
    {
        "FunctionDefinitionId": str,
    },
)
DeleteGroupRequestRequestTypeDef = TypedDict(
    "DeleteGroupRequestRequestTypeDef",
    {
        "GroupId": str,
    },
)
DeleteLoggerDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteLoggerDefinitionRequestRequestTypeDef",
    {
        "LoggerDefinitionId": str,
    },
)
DeleteResourceDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteResourceDefinitionRequestRequestTypeDef",
    {
        "ResourceDefinitionId": str,
    },
)
DeleteSubscriptionDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteSubscriptionDefinitionRequestRequestTypeDef",
    {
        "SubscriptionDefinitionId": str,
    },
)
DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "CreatedAt": NotRequired[str],
        "DeploymentArn": NotRequired[str],
        "DeploymentId": NotRequired[str],
        "DeploymentType": NotRequired[DeploymentTypeType],
        "GroupArn": NotRequired[str],
    },
)
DisassociateRoleFromGroupRequestRequestTypeDef = TypedDict(
    "DisassociateRoleFromGroupRequestRequestTypeDef",
    {
        "GroupId": str,
    },
)
ResourceAccessPolicyTypeDef = TypedDict(
    "ResourceAccessPolicyTypeDef",
    {
        "ResourceId": str,
        "Permission": NotRequired[PermissionType],
    },
)
FunctionRunAsConfigTypeDef = TypedDict(
    "FunctionRunAsConfigTypeDef",
    {
        "Gid": NotRequired[int],
        "Uid": NotRequired[int],
    },
)
GetAssociatedRoleRequestRequestTypeDef = TypedDict(
    "GetAssociatedRoleRequestRequestTypeDef",
    {
        "GroupId": str,
    },
)
GetBulkDeploymentStatusRequestRequestTypeDef = TypedDict(
    "GetBulkDeploymentStatusRequestRequestTypeDef",
    {
        "BulkDeploymentId": str,
    },
)
GetConnectivityInfoRequestRequestTypeDef = TypedDict(
    "GetConnectivityInfoRequestRequestTypeDef",
    {
        "ThingName": str,
    },
)
GetConnectorDefinitionRequestRequestTypeDef = TypedDict(
    "GetConnectorDefinitionRequestRequestTypeDef",
    {
        "ConnectorDefinitionId": str,
    },
)
GetConnectorDefinitionVersionRequestRequestTypeDef = TypedDict(
    "GetConnectorDefinitionVersionRequestRequestTypeDef",
    {
        "ConnectorDefinitionId": str,
        "ConnectorDefinitionVersionId": str,
        "NextToken": NotRequired[str],
    },
)
GetCoreDefinitionRequestRequestTypeDef = TypedDict(
    "GetCoreDefinitionRequestRequestTypeDef",
    {
        "CoreDefinitionId": str,
    },
)
GetCoreDefinitionVersionRequestRequestTypeDef = TypedDict(
    "GetCoreDefinitionVersionRequestRequestTypeDef",
    {
        "CoreDefinitionId": str,
        "CoreDefinitionVersionId": str,
    },
)
GetDeploymentStatusRequestRequestTypeDef = TypedDict(
    "GetDeploymentStatusRequestRequestTypeDef",
    {
        "DeploymentId": str,
        "GroupId": str,
    },
)
GetDeviceDefinitionRequestRequestTypeDef = TypedDict(
    "GetDeviceDefinitionRequestRequestTypeDef",
    {
        "DeviceDefinitionId": str,
    },
)
GetDeviceDefinitionVersionRequestRequestTypeDef = TypedDict(
    "GetDeviceDefinitionVersionRequestRequestTypeDef",
    {
        "DeviceDefinitionId": str,
        "DeviceDefinitionVersionId": str,
        "NextToken": NotRequired[str],
    },
)
GetFunctionDefinitionRequestRequestTypeDef = TypedDict(
    "GetFunctionDefinitionRequestRequestTypeDef",
    {
        "FunctionDefinitionId": str,
    },
)
GetFunctionDefinitionVersionRequestRequestTypeDef = TypedDict(
    "GetFunctionDefinitionVersionRequestRequestTypeDef",
    {
        "FunctionDefinitionId": str,
        "FunctionDefinitionVersionId": str,
        "NextToken": NotRequired[str],
    },
)
GetGroupCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "GetGroupCertificateAuthorityRequestRequestTypeDef",
    {
        "CertificateAuthorityId": str,
        "GroupId": str,
    },
)
GetGroupCertificateConfigurationRequestRequestTypeDef = TypedDict(
    "GetGroupCertificateConfigurationRequestRequestTypeDef",
    {
        "GroupId": str,
    },
)
GetGroupRequestRequestTypeDef = TypedDict(
    "GetGroupRequestRequestTypeDef",
    {
        "GroupId": str,
    },
)
GetGroupVersionRequestRequestTypeDef = TypedDict(
    "GetGroupVersionRequestRequestTypeDef",
    {
        "GroupId": str,
        "GroupVersionId": str,
    },
)
GetLoggerDefinitionRequestRequestTypeDef = TypedDict(
    "GetLoggerDefinitionRequestRequestTypeDef",
    {
        "LoggerDefinitionId": str,
    },
)
GetLoggerDefinitionVersionRequestRequestTypeDef = TypedDict(
    "GetLoggerDefinitionVersionRequestRequestTypeDef",
    {
        "LoggerDefinitionId": str,
        "LoggerDefinitionVersionId": str,
        "NextToken": NotRequired[str],
    },
)
GetResourceDefinitionRequestRequestTypeDef = TypedDict(
    "GetResourceDefinitionRequestRequestTypeDef",
    {
        "ResourceDefinitionId": str,
    },
)
GetResourceDefinitionVersionRequestRequestTypeDef = TypedDict(
    "GetResourceDefinitionVersionRequestRequestTypeDef",
    {
        "ResourceDefinitionId": str,
        "ResourceDefinitionVersionId": str,
    },
)
GetSubscriptionDefinitionRequestRequestTypeDef = TypedDict(
    "GetSubscriptionDefinitionRequestRequestTypeDef",
    {
        "SubscriptionDefinitionId": str,
    },
)
GetSubscriptionDefinitionVersionRequestRequestTypeDef = TypedDict(
    "GetSubscriptionDefinitionVersionRequestRequestTypeDef",
    {
        "SubscriptionDefinitionId": str,
        "SubscriptionDefinitionVersionId": str,
        "NextToken": NotRequired[str],
    },
)
GetThingRuntimeConfigurationRequestRequestTypeDef = TypedDict(
    "GetThingRuntimeConfigurationRequestRequestTypeDef",
    {
        "ThingName": str,
    },
)
GroupCertificateAuthorityPropertiesTypeDef = TypedDict(
    "GroupCertificateAuthorityPropertiesTypeDef",
    {
        "GroupCertificateAuthorityArn": NotRequired[str],
        "GroupCertificateAuthorityId": NotRequired[str],
    },
)
GroupInformationTypeDef = TypedDict(
    "GroupInformationTypeDef",
    {
        "Arn": NotRequired[str],
        "CreationTimestamp": NotRequired[str],
        "Id": NotRequired[str],
        "LastUpdatedTimestamp": NotRequired[str],
        "LatestVersion": NotRequired[str],
        "LatestVersionArn": NotRequired[str],
        "Name": NotRequired[str],
    },
)
GroupOwnerSettingTypeDef = TypedDict(
    "GroupOwnerSettingTypeDef",
    {
        "AutoAddGroupOwner": NotRequired[bool],
        "GroupOwner": NotRequired[str],
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
ListBulkDeploymentDetailedReportsRequestRequestTypeDef = TypedDict(
    "ListBulkDeploymentDetailedReportsRequestRequestTypeDef",
    {
        "BulkDeploymentId": str,
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
ListBulkDeploymentsRequestRequestTypeDef = TypedDict(
    "ListBulkDeploymentsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
ListConnectorDefinitionVersionsRequestRequestTypeDef = TypedDict(
    "ListConnectorDefinitionVersionsRequestRequestTypeDef",
    {
        "ConnectorDefinitionId": str,
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
VersionInformationTypeDef = TypedDict(
    "VersionInformationTypeDef",
    {
        "Arn": NotRequired[str],
        "CreationTimestamp": NotRequired[str],
        "Id": NotRequired[str],
        "Version": NotRequired[str],
    },
)
ListConnectorDefinitionsRequestRequestTypeDef = TypedDict(
    "ListConnectorDefinitionsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
ListCoreDefinitionVersionsRequestRequestTypeDef = TypedDict(
    "ListCoreDefinitionVersionsRequestRequestTypeDef",
    {
        "CoreDefinitionId": str,
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
ListCoreDefinitionsRequestRequestTypeDef = TypedDict(
    "ListCoreDefinitionsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
ListDeploymentsRequestRequestTypeDef = TypedDict(
    "ListDeploymentsRequestRequestTypeDef",
    {
        "GroupId": str,
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
ListDeviceDefinitionVersionsRequestRequestTypeDef = TypedDict(
    "ListDeviceDefinitionVersionsRequestRequestTypeDef",
    {
        "DeviceDefinitionId": str,
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
ListDeviceDefinitionsRequestRequestTypeDef = TypedDict(
    "ListDeviceDefinitionsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
ListFunctionDefinitionVersionsRequestRequestTypeDef = TypedDict(
    "ListFunctionDefinitionVersionsRequestRequestTypeDef",
    {
        "FunctionDefinitionId": str,
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
ListFunctionDefinitionsRequestRequestTypeDef = TypedDict(
    "ListFunctionDefinitionsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
ListGroupCertificateAuthoritiesRequestRequestTypeDef = TypedDict(
    "ListGroupCertificateAuthoritiesRequestRequestTypeDef",
    {
        "GroupId": str,
    },
)
ListGroupVersionsRequestRequestTypeDef = TypedDict(
    "ListGroupVersionsRequestRequestTypeDef",
    {
        "GroupId": str,
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
ListGroupsRequestRequestTypeDef = TypedDict(
    "ListGroupsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
ListLoggerDefinitionVersionsRequestRequestTypeDef = TypedDict(
    "ListLoggerDefinitionVersionsRequestRequestTypeDef",
    {
        "LoggerDefinitionId": str,
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
ListLoggerDefinitionsRequestRequestTypeDef = TypedDict(
    "ListLoggerDefinitionsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
ListResourceDefinitionVersionsRequestRequestTypeDef = TypedDict(
    "ListResourceDefinitionVersionsRequestRequestTypeDef",
    {
        "ResourceDefinitionId": str,
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
ListResourceDefinitionsRequestRequestTypeDef = TypedDict(
    "ListResourceDefinitionsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
ListSubscriptionDefinitionVersionsRequestRequestTypeDef = TypedDict(
    "ListSubscriptionDefinitionVersionsRequestRequestTypeDef",
    {
        "SubscriptionDefinitionId": str,
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
ListSubscriptionDefinitionsRequestRequestTypeDef = TypedDict(
    "ListSubscriptionDefinitionsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
ResetDeploymentsRequestRequestTypeDef = TypedDict(
    "ResetDeploymentsRequestRequestTypeDef",
    {
        "GroupId": str,
        "AmznClientToken": NotRequired[str],
        "Force": NotRequired[bool],
    },
)
SecretsManagerSecretResourceDataOutputTypeDef = TypedDict(
    "SecretsManagerSecretResourceDataOutputTypeDef",
    {
        "ARN": NotRequired[str],
        "AdditionalStagingLabelsToDownload": NotRequired[List[str]],
    },
)
ResourceDownloadOwnerSettingTypeDef = TypedDict(
    "ResourceDownloadOwnerSettingTypeDef",
    {
        "GroupOwner": str,
        "GroupPermission": PermissionType,
    },
)
TelemetryConfigurationTypeDef = TypedDict(
    "TelemetryConfigurationTypeDef",
    {
        "Telemetry": TelemetryType,
        "ConfigurationSyncStatus": NotRequired[ConfigurationSyncStatusType],
    },
)
SecretsManagerSecretResourceDataTypeDef = TypedDict(
    "SecretsManagerSecretResourceDataTypeDef",
    {
        "ARN": NotRequired[str],
        "AdditionalStagingLabelsToDownload": NotRequired[Sequence[str]],
    },
)
StartBulkDeploymentRequestRequestTypeDef = TypedDict(
    "StartBulkDeploymentRequestRequestTypeDef",
    {
        "ExecutionRoleArn": str,
        "InputFileUri": str,
        "AmznClientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
StopBulkDeploymentRequestRequestTypeDef = TypedDict(
    "StopBulkDeploymentRequestRequestTypeDef",
    {
        "BulkDeploymentId": str,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "tags": NotRequired[Mapping[str, str]],
    },
)
TelemetryConfigurationUpdateTypeDef = TypedDict(
    "TelemetryConfigurationUpdateTypeDef",
    {
        "Telemetry": TelemetryType,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateConnectorDefinitionRequestRequestTypeDef = TypedDict(
    "UpdateConnectorDefinitionRequestRequestTypeDef",
    {
        "ConnectorDefinitionId": str,
        "Name": NotRequired[str],
    },
)
UpdateCoreDefinitionRequestRequestTypeDef = TypedDict(
    "UpdateCoreDefinitionRequestRequestTypeDef",
    {
        "CoreDefinitionId": str,
        "Name": NotRequired[str],
    },
)
UpdateDeviceDefinitionRequestRequestTypeDef = TypedDict(
    "UpdateDeviceDefinitionRequestRequestTypeDef",
    {
        "DeviceDefinitionId": str,
        "Name": NotRequired[str],
    },
)
UpdateFunctionDefinitionRequestRequestTypeDef = TypedDict(
    "UpdateFunctionDefinitionRequestRequestTypeDef",
    {
        "FunctionDefinitionId": str,
        "Name": NotRequired[str],
    },
)
UpdateGroupCertificateConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateGroupCertificateConfigurationRequestRequestTypeDef",
    {
        "GroupId": str,
        "CertificateExpiryInMilliseconds": NotRequired[str],
    },
)
UpdateGroupRequestRequestTypeDef = TypedDict(
    "UpdateGroupRequestRequestTypeDef",
    {
        "GroupId": str,
        "Name": NotRequired[str],
    },
)
UpdateLoggerDefinitionRequestRequestTypeDef = TypedDict(
    "UpdateLoggerDefinitionRequestRequestTypeDef",
    {
        "LoggerDefinitionId": str,
        "Name": NotRequired[str],
    },
)
UpdateResourceDefinitionRequestRequestTypeDef = TypedDict(
    "UpdateResourceDefinitionRequestRequestTypeDef",
    {
        "ResourceDefinitionId": str,
        "Name": NotRequired[str],
    },
)
UpdateSubscriptionDefinitionRequestRequestTypeDef = TypedDict(
    "UpdateSubscriptionDefinitionRequestRequestTypeDef",
    {
        "SubscriptionDefinitionId": str,
        "Name": NotRequired[str],
    },
)
AssociateRoleToGroupResponseTypeDef = TypedDict(
    "AssociateRoleToGroupResponseTypeDef",
    {
        "AssociatedAt": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateServiceRoleToAccountResponseTypeDef = TypedDict(
    "AssociateServiceRoleToAccountResponseTypeDef",
    {
        "AssociatedAt": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateConnectorDefinitionResponseTypeDef = TypedDict(
    "CreateConnectorDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateConnectorDefinitionVersionResponseTypeDef = TypedDict(
    "CreateConnectorDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCoreDefinitionResponseTypeDef = TypedDict(
    "CreateCoreDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCoreDefinitionVersionResponseTypeDef = TypedDict(
    "CreateCoreDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDeploymentResponseTypeDef = TypedDict(
    "CreateDeploymentResponseTypeDef",
    {
        "DeploymentArn": str,
        "DeploymentId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDeviceDefinitionResponseTypeDef = TypedDict(
    "CreateDeviceDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDeviceDefinitionVersionResponseTypeDef = TypedDict(
    "CreateDeviceDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFunctionDefinitionResponseTypeDef = TypedDict(
    "CreateFunctionDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFunctionDefinitionVersionResponseTypeDef = TypedDict(
    "CreateFunctionDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGroupCertificateAuthorityResponseTypeDef = TypedDict(
    "CreateGroupCertificateAuthorityResponseTypeDef",
    {
        "GroupCertificateAuthorityArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGroupResponseTypeDef = TypedDict(
    "CreateGroupResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGroupVersionResponseTypeDef = TypedDict(
    "CreateGroupVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateLoggerDefinitionResponseTypeDef = TypedDict(
    "CreateLoggerDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateLoggerDefinitionVersionResponseTypeDef = TypedDict(
    "CreateLoggerDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateResourceDefinitionResponseTypeDef = TypedDict(
    "CreateResourceDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateResourceDefinitionVersionResponseTypeDef = TypedDict(
    "CreateResourceDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSoftwareUpdateJobResponseTypeDef = TypedDict(
    "CreateSoftwareUpdateJobResponseTypeDef",
    {
        "IotJobArn": str,
        "IotJobId": str,
        "PlatformSoftwareVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSubscriptionDefinitionResponseTypeDef = TypedDict(
    "CreateSubscriptionDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSubscriptionDefinitionVersionResponseTypeDef = TypedDict(
    "CreateSubscriptionDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateRoleFromGroupResponseTypeDef = TypedDict(
    "DisassociateRoleFromGroupResponseTypeDef",
    {
        "DisassociatedAt": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateServiceRoleFromAccountResponseTypeDef = TypedDict(
    "DisassociateServiceRoleFromAccountResponseTypeDef",
    {
        "DisassociatedAt": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAssociatedRoleResponseTypeDef = TypedDict(
    "GetAssociatedRoleResponseTypeDef",
    {
        "AssociatedAt": str,
        "RoleArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetConnectorDefinitionResponseTypeDef = TypedDict(
    "GetConnectorDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCoreDefinitionResponseTypeDef = TypedDict(
    "GetCoreDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDeviceDefinitionResponseTypeDef = TypedDict(
    "GetDeviceDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFunctionDefinitionResponseTypeDef = TypedDict(
    "GetFunctionDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetGroupCertificateAuthorityResponseTypeDef = TypedDict(
    "GetGroupCertificateAuthorityResponseTypeDef",
    {
        "GroupCertificateAuthorityArn": str,
        "GroupCertificateAuthorityId": str,
        "PemEncodedCertificate": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetGroupCertificateConfigurationResponseTypeDef = TypedDict(
    "GetGroupCertificateConfigurationResponseTypeDef",
    {
        "CertificateAuthorityExpiryInMilliseconds": str,
        "CertificateExpiryInMilliseconds": str,
        "GroupId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetGroupResponseTypeDef = TypedDict(
    "GetGroupResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLoggerDefinitionResponseTypeDef = TypedDict(
    "GetLoggerDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResourceDefinitionResponseTypeDef = TypedDict(
    "GetResourceDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServiceRoleForAccountResponseTypeDef = TypedDict(
    "GetServiceRoleForAccountResponseTypeDef",
    {
        "AssociatedAt": str,
        "RoleArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSubscriptionDefinitionResponseTypeDef = TypedDict(
    "GetSubscriptionDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
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
ResetDeploymentsResponseTypeDef = TypedDict(
    "ResetDeploymentsResponseTypeDef",
    {
        "DeploymentArn": str,
        "DeploymentId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartBulkDeploymentResponseTypeDef = TypedDict(
    "StartBulkDeploymentResponseTypeDef",
    {
        "BulkDeploymentArn": str,
        "BulkDeploymentId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateConnectivityInfoResponseTypeDef = TypedDict(
    "UpdateConnectivityInfoResponseTypeDef",
    {
        "Message": str,
        "Version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateGroupCertificateConfigurationResponseTypeDef = TypedDict(
    "UpdateGroupCertificateConfigurationResponseTypeDef",
    {
        "CertificateAuthorityExpiryInMilliseconds": str,
        "CertificateExpiryInMilliseconds": str,
        "GroupId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BulkDeploymentResultTypeDef = TypedDict(
    "BulkDeploymentResultTypeDef",
    {
        "CreatedAt": NotRequired[str],
        "DeploymentArn": NotRequired[str],
        "DeploymentId": NotRequired[str],
        "DeploymentStatus": NotRequired[str],
        "DeploymentType": NotRequired[DeploymentTypeType],
        "ErrorDetails": NotRequired[List[ErrorDetailTypeDef]],
        "ErrorMessage": NotRequired[str],
        "GroupArn": NotRequired[str],
    },
)
GetBulkDeploymentStatusResponseTypeDef = TypedDict(
    "GetBulkDeploymentStatusResponseTypeDef",
    {
        "BulkDeploymentMetrics": BulkDeploymentMetricsTypeDef,
        "BulkDeploymentStatus": BulkDeploymentStatusType,
        "CreatedAt": str,
        "ErrorDetails": List[ErrorDetailTypeDef],
        "ErrorMessage": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDeploymentStatusResponseTypeDef = TypedDict(
    "GetDeploymentStatusResponseTypeDef",
    {
        "DeploymentStatus": str,
        "DeploymentType": DeploymentTypeType,
        "ErrorDetails": List[ErrorDetailTypeDef],
        "ErrorMessage": str,
        "UpdatedAt": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListBulkDeploymentsResponseTypeDef = TypedDict(
    "ListBulkDeploymentsResponseTypeDef",
    {
        "BulkDeployments": List[BulkDeploymentTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetConnectivityInfoResponseTypeDef = TypedDict(
    "GetConnectivityInfoResponseTypeDef",
    {
        "ConnectivityInfo": List[ConnectivityInfoTypeDef],
        "Message": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateConnectivityInfoRequestRequestTypeDef = TypedDict(
    "UpdateConnectivityInfoRequestRequestTypeDef",
    {
        "ThingName": str,
        "ConnectivityInfo": NotRequired[Sequence[ConnectivityInfoTypeDef]],
    },
)
ConnectorDefinitionVersionOutputTypeDef = TypedDict(
    "ConnectorDefinitionVersionOutputTypeDef",
    {
        "Connectors": NotRequired[List[ConnectorOutputTypeDef]],
    },
)
ConnectorUnionTypeDef = Union[ConnectorTypeDef, ConnectorOutputTypeDef]
CoreDefinitionVersionOutputTypeDef = TypedDict(
    "CoreDefinitionVersionOutputTypeDef",
    {
        "Cores": NotRequired[List[CoreTypeDef]],
    },
)
CoreDefinitionVersionTypeDef = TypedDict(
    "CoreDefinitionVersionTypeDef",
    {
        "Cores": NotRequired[Sequence[CoreTypeDef]],
    },
)
CreateCoreDefinitionVersionRequestRequestTypeDef = TypedDict(
    "CreateCoreDefinitionVersionRequestRequestTypeDef",
    {
        "CoreDefinitionId": str,
        "AmznClientToken": NotRequired[str],
        "Cores": NotRequired[Sequence[CoreTypeDef]],
    },
)
CreateDeviceDefinitionVersionRequestRequestTypeDef = TypedDict(
    "CreateDeviceDefinitionVersionRequestRequestTypeDef",
    {
        "DeviceDefinitionId": str,
        "AmznClientToken": NotRequired[str],
        "Devices": NotRequired[Sequence[DeviceTypeDef]],
    },
)
DeviceDefinitionVersionOutputTypeDef = TypedDict(
    "DeviceDefinitionVersionOutputTypeDef",
    {
        "Devices": NotRequired[List[DeviceTypeDef]],
    },
)
DeviceDefinitionVersionTypeDef = TypedDict(
    "DeviceDefinitionVersionTypeDef",
    {
        "Devices": NotRequired[Sequence[DeviceTypeDef]],
    },
)
CreateGroupRequestRequestTypeDef = TypedDict(
    "CreateGroupRequestRequestTypeDef",
    {
        "Name": str,
        "AmznClientToken": NotRequired[str],
        "InitialVersion": NotRequired[GroupVersionTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
GetGroupVersionResponseTypeDef = TypedDict(
    "GetGroupVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": GroupVersionTypeDef,
        "Id": str,
        "Version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateLoggerDefinitionVersionRequestRequestTypeDef = TypedDict(
    "CreateLoggerDefinitionVersionRequestRequestTypeDef",
    {
        "LoggerDefinitionId": str,
        "AmznClientToken": NotRequired[str],
        "Loggers": NotRequired[Sequence[LoggerTypeDef]],
    },
)
LoggerDefinitionVersionOutputTypeDef = TypedDict(
    "LoggerDefinitionVersionOutputTypeDef",
    {
        "Loggers": NotRequired[List[LoggerTypeDef]],
    },
)
LoggerDefinitionVersionTypeDef = TypedDict(
    "LoggerDefinitionVersionTypeDef",
    {
        "Loggers": NotRequired[Sequence[LoggerTypeDef]],
    },
)
CreateSubscriptionDefinitionVersionRequestRequestTypeDef = TypedDict(
    "CreateSubscriptionDefinitionVersionRequestRequestTypeDef",
    {
        "SubscriptionDefinitionId": str,
        "AmznClientToken": NotRequired[str],
        "Subscriptions": NotRequired[Sequence[SubscriptionTypeDef]],
    },
)
SubscriptionDefinitionVersionOutputTypeDef = TypedDict(
    "SubscriptionDefinitionVersionOutputTypeDef",
    {
        "Subscriptions": NotRequired[List[SubscriptionTypeDef]],
    },
)
SubscriptionDefinitionVersionTypeDef = TypedDict(
    "SubscriptionDefinitionVersionTypeDef",
    {
        "Subscriptions": NotRequired[Sequence[SubscriptionTypeDef]],
    },
)
ListConnectorDefinitionsResponseTypeDef = TypedDict(
    "ListConnectorDefinitionsResponseTypeDef",
    {
        "Definitions": List[DefinitionInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListCoreDefinitionsResponseTypeDef = TypedDict(
    "ListCoreDefinitionsResponseTypeDef",
    {
        "Definitions": List[DefinitionInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListDeviceDefinitionsResponseTypeDef = TypedDict(
    "ListDeviceDefinitionsResponseTypeDef",
    {
        "Definitions": List[DefinitionInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListFunctionDefinitionsResponseTypeDef = TypedDict(
    "ListFunctionDefinitionsResponseTypeDef",
    {
        "Definitions": List[DefinitionInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListLoggerDefinitionsResponseTypeDef = TypedDict(
    "ListLoggerDefinitionsResponseTypeDef",
    {
        "Definitions": List[DefinitionInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListResourceDefinitionsResponseTypeDef = TypedDict(
    "ListResourceDefinitionsResponseTypeDef",
    {
        "Definitions": List[DefinitionInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListSubscriptionDefinitionsResponseTypeDef = TypedDict(
    "ListSubscriptionDefinitionsResponseTypeDef",
    {
        "Definitions": List[DefinitionInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListDeploymentsResponseTypeDef = TypedDict(
    "ListDeploymentsResponseTypeDef",
    {
        "Deployments": List[DeploymentTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
FunctionDefaultExecutionConfigTypeDef = TypedDict(
    "FunctionDefaultExecutionConfigTypeDef",
    {
        "IsolationMode": NotRequired[FunctionIsolationModeType],
        "RunAs": NotRequired[FunctionRunAsConfigTypeDef],
    },
)
FunctionExecutionConfigTypeDef = TypedDict(
    "FunctionExecutionConfigTypeDef",
    {
        "IsolationMode": NotRequired[FunctionIsolationModeType],
        "RunAs": NotRequired[FunctionRunAsConfigTypeDef],
    },
)
ListGroupCertificateAuthoritiesResponseTypeDef = TypedDict(
    "ListGroupCertificateAuthoritiesResponseTypeDef",
    {
        "GroupCertificateAuthorities": List[GroupCertificateAuthorityPropertiesTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListGroupsResponseTypeDef = TypedDict(
    "ListGroupsResponseTypeDef",
    {
        "Groups": List[GroupInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
LocalDeviceResourceDataTypeDef = TypedDict(
    "LocalDeviceResourceDataTypeDef",
    {
        "GroupOwnerSetting": NotRequired[GroupOwnerSettingTypeDef],
        "SourcePath": NotRequired[str],
    },
)
LocalVolumeResourceDataTypeDef = TypedDict(
    "LocalVolumeResourceDataTypeDef",
    {
        "DestinationPath": NotRequired[str],
        "GroupOwnerSetting": NotRequired[GroupOwnerSettingTypeDef],
        "SourcePath": NotRequired[str],
    },
)
ListBulkDeploymentDetailedReportsRequestListBulkDeploymentDetailedReportsPaginateTypeDef = (
    TypedDict(
        "ListBulkDeploymentDetailedReportsRequestListBulkDeploymentDetailedReportsPaginateTypeDef",
        {
            "BulkDeploymentId": str,
            "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
        },
    )
)
ListBulkDeploymentsRequestListBulkDeploymentsPaginateTypeDef = TypedDict(
    "ListBulkDeploymentsRequestListBulkDeploymentsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListConnectorDefinitionVersionsRequestListConnectorDefinitionVersionsPaginateTypeDef = TypedDict(
    "ListConnectorDefinitionVersionsRequestListConnectorDefinitionVersionsPaginateTypeDef",
    {
        "ConnectorDefinitionId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListConnectorDefinitionsRequestListConnectorDefinitionsPaginateTypeDef = TypedDict(
    "ListConnectorDefinitionsRequestListConnectorDefinitionsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCoreDefinitionVersionsRequestListCoreDefinitionVersionsPaginateTypeDef = TypedDict(
    "ListCoreDefinitionVersionsRequestListCoreDefinitionVersionsPaginateTypeDef",
    {
        "CoreDefinitionId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCoreDefinitionsRequestListCoreDefinitionsPaginateTypeDef = TypedDict(
    "ListCoreDefinitionsRequestListCoreDefinitionsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDeploymentsRequestListDeploymentsPaginateTypeDef = TypedDict(
    "ListDeploymentsRequestListDeploymentsPaginateTypeDef",
    {
        "GroupId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDeviceDefinitionVersionsRequestListDeviceDefinitionVersionsPaginateTypeDef = TypedDict(
    "ListDeviceDefinitionVersionsRequestListDeviceDefinitionVersionsPaginateTypeDef",
    {
        "DeviceDefinitionId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDeviceDefinitionsRequestListDeviceDefinitionsPaginateTypeDef = TypedDict(
    "ListDeviceDefinitionsRequestListDeviceDefinitionsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFunctionDefinitionVersionsRequestListFunctionDefinitionVersionsPaginateTypeDef = TypedDict(
    "ListFunctionDefinitionVersionsRequestListFunctionDefinitionVersionsPaginateTypeDef",
    {
        "FunctionDefinitionId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFunctionDefinitionsRequestListFunctionDefinitionsPaginateTypeDef = TypedDict(
    "ListFunctionDefinitionsRequestListFunctionDefinitionsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGroupVersionsRequestListGroupVersionsPaginateTypeDef = TypedDict(
    "ListGroupVersionsRequestListGroupVersionsPaginateTypeDef",
    {
        "GroupId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGroupsRequestListGroupsPaginateTypeDef = TypedDict(
    "ListGroupsRequestListGroupsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListLoggerDefinitionVersionsRequestListLoggerDefinitionVersionsPaginateTypeDef = TypedDict(
    "ListLoggerDefinitionVersionsRequestListLoggerDefinitionVersionsPaginateTypeDef",
    {
        "LoggerDefinitionId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListLoggerDefinitionsRequestListLoggerDefinitionsPaginateTypeDef = TypedDict(
    "ListLoggerDefinitionsRequestListLoggerDefinitionsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResourceDefinitionVersionsRequestListResourceDefinitionVersionsPaginateTypeDef = TypedDict(
    "ListResourceDefinitionVersionsRequestListResourceDefinitionVersionsPaginateTypeDef",
    {
        "ResourceDefinitionId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResourceDefinitionsRequestListResourceDefinitionsPaginateTypeDef = TypedDict(
    "ListResourceDefinitionsRequestListResourceDefinitionsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSubscriptionDefinitionVersionsRequestListSubscriptionDefinitionVersionsPaginateTypeDef = TypedDict(
    "ListSubscriptionDefinitionVersionsRequestListSubscriptionDefinitionVersionsPaginateTypeDef",
    {
        "SubscriptionDefinitionId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSubscriptionDefinitionsRequestListSubscriptionDefinitionsPaginateTypeDef = TypedDict(
    "ListSubscriptionDefinitionsRequestListSubscriptionDefinitionsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListConnectorDefinitionVersionsResponseTypeDef = TypedDict(
    "ListConnectorDefinitionVersionsResponseTypeDef",
    {
        "Versions": List[VersionInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListCoreDefinitionVersionsResponseTypeDef = TypedDict(
    "ListCoreDefinitionVersionsResponseTypeDef",
    {
        "Versions": List[VersionInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListDeviceDefinitionVersionsResponseTypeDef = TypedDict(
    "ListDeviceDefinitionVersionsResponseTypeDef",
    {
        "Versions": List[VersionInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListFunctionDefinitionVersionsResponseTypeDef = TypedDict(
    "ListFunctionDefinitionVersionsResponseTypeDef",
    {
        "Versions": List[VersionInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListGroupVersionsResponseTypeDef = TypedDict(
    "ListGroupVersionsResponseTypeDef",
    {
        "Versions": List[VersionInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListLoggerDefinitionVersionsResponseTypeDef = TypedDict(
    "ListLoggerDefinitionVersionsResponseTypeDef",
    {
        "Versions": List[VersionInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListResourceDefinitionVersionsResponseTypeDef = TypedDict(
    "ListResourceDefinitionVersionsResponseTypeDef",
    {
        "Versions": List[VersionInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListSubscriptionDefinitionVersionsResponseTypeDef = TypedDict(
    "ListSubscriptionDefinitionVersionsResponseTypeDef",
    {
        "Versions": List[VersionInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
S3MachineLearningModelResourceDataTypeDef = TypedDict(
    "S3MachineLearningModelResourceDataTypeDef",
    {
        "DestinationPath": NotRequired[str],
        "OwnerSetting": NotRequired[ResourceDownloadOwnerSettingTypeDef],
        "S3Uri": NotRequired[str],
    },
)
SageMakerMachineLearningModelResourceDataTypeDef = TypedDict(
    "SageMakerMachineLearningModelResourceDataTypeDef",
    {
        "DestinationPath": NotRequired[str],
        "OwnerSetting": NotRequired[ResourceDownloadOwnerSettingTypeDef],
        "SageMakerJobArn": NotRequired[str],
    },
)
RuntimeConfigurationTypeDef = TypedDict(
    "RuntimeConfigurationTypeDef",
    {
        "TelemetryConfiguration": NotRequired[TelemetryConfigurationTypeDef],
    },
)
SecretsManagerSecretResourceDataUnionTypeDef = Union[
    SecretsManagerSecretResourceDataTypeDef, SecretsManagerSecretResourceDataOutputTypeDef
]
UpdateThingRuntimeConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateThingRuntimeConfigurationRequestRequestTypeDef",
    {
        "ThingName": str,
        "TelemetryConfiguration": NotRequired[TelemetryConfigurationUpdateTypeDef],
    },
)
ListBulkDeploymentDetailedReportsResponseTypeDef = TypedDict(
    "ListBulkDeploymentDetailedReportsResponseTypeDef",
    {
        "Deployments": List[BulkDeploymentResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetConnectorDefinitionVersionResponseTypeDef = TypedDict(
    "GetConnectorDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": ConnectorDefinitionVersionOutputTypeDef,
        "Id": str,
        "Version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ConnectorDefinitionVersionTypeDef = TypedDict(
    "ConnectorDefinitionVersionTypeDef",
    {
        "Connectors": NotRequired[Sequence[ConnectorUnionTypeDef]],
    },
)
CreateConnectorDefinitionVersionRequestRequestTypeDef = TypedDict(
    "CreateConnectorDefinitionVersionRequestRequestTypeDef",
    {
        "ConnectorDefinitionId": str,
        "AmznClientToken": NotRequired[str],
        "Connectors": NotRequired[Sequence[ConnectorUnionTypeDef]],
    },
)
GetCoreDefinitionVersionResponseTypeDef = TypedDict(
    "GetCoreDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": CoreDefinitionVersionOutputTypeDef,
        "Id": str,
        "Version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateCoreDefinitionRequestRequestTypeDef = TypedDict(
    "CreateCoreDefinitionRequestRequestTypeDef",
    {
        "AmznClientToken": NotRequired[str],
        "InitialVersion": NotRequired[CoreDefinitionVersionTypeDef],
        "Name": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
GetDeviceDefinitionVersionResponseTypeDef = TypedDict(
    "GetDeviceDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": DeviceDefinitionVersionOutputTypeDef,
        "Id": str,
        "Version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateDeviceDefinitionRequestRequestTypeDef = TypedDict(
    "CreateDeviceDefinitionRequestRequestTypeDef",
    {
        "AmznClientToken": NotRequired[str],
        "InitialVersion": NotRequired[DeviceDefinitionVersionTypeDef],
        "Name": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
GetLoggerDefinitionVersionResponseTypeDef = TypedDict(
    "GetLoggerDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": LoggerDefinitionVersionOutputTypeDef,
        "Id": str,
        "Version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateLoggerDefinitionRequestRequestTypeDef = TypedDict(
    "CreateLoggerDefinitionRequestRequestTypeDef",
    {
        "AmznClientToken": NotRequired[str],
        "InitialVersion": NotRequired[LoggerDefinitionVersionTypeDef],
        "Name": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
GetSubscriptionDefinitionVersionResponseTypeDef = TypedDict(
    "GetSubscriptionDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": SubscriptionDefinitionVersionOutputTypeDef,
        "Id": str,
        "Version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateSubscriptionDefinitionRequestRequestTypeDef = TypedDict(
    "CreateSubscriptionDefinitionRequestRequestTypeDef",
    {
        "AmznClientToken": NotRequired[str],
        "InitialVersion": NotRequired[SubscriptionDefinitionVersionTypeDef],
        "Name": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
FunctionDefaultConfigTypeDef = TypedDict(
    "FunctionDefaultConfigTypeDef",
    {
        "Execution": NotRequired[FunctionDefaultExecutionConfigTypeDef],
    },
)
FunctionConfigurationEnvironmentOutputTypeDef = TypedDict(
    "FunctionConfigurationEnvironmentOutputTypeDef",
    {
        "AccessSysfs": NotRequired[bool],
        "Execution": NotRequired[FunctionExecutionConfigTypeDef],
        "ResourceAccessPolicies": NotRequired[List[ResourceAccessPolicyTypeDef]],
        "Variables": NotRequired[Dict[str, str]],
    },
)
FunctionConfigurationEnvironmentTypeDef = TypedDict(
    "FunctionConfigurationEnvironmentTypeDef",
    {
        "AccessSysfs": NotRequired[bool],
        "Execution": NotRequired[FunctionExecutionConfigTypeDef],
        "ResourceAccessPolicies": NotRequired[Sequence[ResourceAccessPolicyTypeDef]],
        "Variables": NotRequired[Mapping[str, str]],
    },
)
ResourceDataContainerOutputTypeDef = TypedDict(
    "ResourceDataContainerOutputTypeDef",
    {
        "LocalDeviceResourceData": NotRequired[LocalDeviceResourceDataTypeDef],
        "LocalVolumeResourceData": NotRequired[LocalVolumeResourceDataTypeDef],
        "S3MachineLearningModelResourceData": NotRequired[
            S3MachineLearningModelResourceDataTypeDef
        ],
        "SageMakerMachineLearningModelResourceData": NotRequired[
            SageMakerMachineLearningModelResourceDataTypeDef
        ],
        "SecretsManagerSecretResourceData": NotRequired[
            SecretsManagerSecretResourceDataOutputTypeDef
        ],
    },
)
GetThingRuntimeConfigurationResponseTypeDef = TypedDict(
    "GetThingRuntimeConfigurationResponseTypeDef",
    {
        "RuntimeConfiguration": RuntimeConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResourceDataContainerTypeDef = TypedDict(
    "ResourceDataContainerTypeDef",
    {
        "LocalDeviceResourceData": NotRequired[LocalDeviceResourceDataTypeDef],
        "LocalVolumeResourceData": NotRequired[LocalVolumeResourceDataTypeDef],
        "S3MachineLearningModelResourceData": NotRequired[
            S3MachineLearningModelResourceDataTypeDef
        ],
        "SageMakerMachineLearningModelResourceData": NotRequired[
            SageMakerMachineLearningModelResourceDataTypeDef
        ],
        "SecretsManagerSecretResourceData": NotRequired[
            SecretsManagerSecretResourceDataUnionTypeDef
        ],
    },
)
CreateConnectorDefinitionRequestRequestTypeDef = TypedDict(
    "CreateConnectorDefinitionRequestRequestTypeDef",
    {
        "AmznClientToken": NotRequired[str],
        "InitialVersion": NotRequired[ConnectorDefinitionVersionTypeDef],
        "Name": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
FunctionConfigurationOutputTypeDef = TypedDict(
    "FunctionConfigurationOutputTypeDef",
    {
        "EncodingType": NotRequired[EncodingTypeType],
        "Environment": NotRequired[FunctionConfigurationEnvironmentOutputTypeDef],
        "ExecArgs": NotRequired[str],
        "Executable": NotRequired[str],
        "MemorySize": NotRequired[int],
        "Pinned": NotRequired[bool],
        "Timeout": NotRequired[int],
        "FunctionRuntimeOverride": NotRequired[str],
    },
)
FunctionConfigurationEnvironmentUnionTypeDef = Union[
    FunctionConfigurationEnvironmentTypeDef, FunctionConfigurationEnvironmentOutputTypeDef
]
ResourceOutputTypeDef = TypedDict(
    "ResourceOutputTypeDef",
    {
        "Id": str,
        "Name": str,
        "ResourceDataContainer": ResourceDataContainerOutputTypeDef,
    },
)
ResourceDataContainerUnionTypeDef = Union[
    ResourceDataContainerTypeDef, ResourceDataContainerOutputTypeDef
]
FunctionOutputTypeDef = TypedDict(
    "FunctionOutputTypeDef",
    {
        "Id": str,
        "FunctionArn": NotRequired[str],
        "FunctionConfiguration": NotRequired[FunctionConfigurationOutputTypeDef],
    },
)
FunctionConfigurationTypeDef = TypedDict(
    "FunctionConfigurationTypeDef",
    {
        "EncodingType": NotRequired[EncodingTypeType],
        "Environment": NotRequired[FunctionConfigurationEnvironmentUnionTypeDef],
        "ExecArgs": NotRequired[str],
        "Executable": NotRequired[str],
        "MemorySize": NotRequired[int],
        "Pinned": NotRequired[bool],
        "Timeout": NotRequired[int],
        "FunctionRuntimeOverride": NotRequired[str],
    },
)
ResourceDefinitionVersionOutputTypeDef = TypedDict(
    "ResourceDefinitionVersionOutputTypeDef",
    {
        "Resources": NotRequired[List[ResourceOutputTypeDef]],
    },
)
ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "Id": str,
        "Name": str,
        "ResourceDataContainer": ResourceDataContainerUnionTypeDef,
    },
)
FunctionDefinitionVersionOutputTypeDef = TypedDict(
    "FunctionDefinitionVersionOutputTypeDef",
    {
        "DefaultConfig": NotRequired[FunctionDefaultConfigTypeDef],
        "Functions": NotRequired[List[FunctionOutputTypeDef]],
    },
)
FunctionConfigurationUnionTypeDef = Union[
    FunctionConfigurationTypeDef, FunctionConfigurationOutputTypeDef
]
GetResourceDefinitionVersionResponseTypeDef = TypedDict(
    "GetResourceDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": ResourceDefinitionVersionOutputTypeDef,
        "Id": str,
        "Version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResourceUnionTypeDef = Union[ResourceTypeDef, ResourceOutputTypeDef]
GetFunctionDefinitionVersionResponseTypeDef = TypedDict(
    "GetFunctionDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": FunctionDefinitionVersionOutputTypeDef,
        "Id": str,
        "Version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
FunctionTypeDef = TypedDict(
    "FunctionTypeDef",
    {
        "Id": str,
        "FunctionArn": NotRequired[str],
        "FunctionConfiguration": NotRequired[FunctionConfigurationUnionTypeDef],
    },
)
CreateResourceDefinitionVersionRequestRequestTypeDef = TypedDict(
    "CreateResourceDefinitionVersionRequestRequestTypeDef",
    {
        "ResourceDefinitionId": str,
        "AmznClientToken": NotRequired[str],
        "Resources": NotRequired[Sequence[ResourceUnionTypeDef]],
    },
)
ResourceDefinitionVersionTypeDef = TypedDict(
    "ResourceDefinitionVersionTypeDef",
    {
        "Resources": NotRequired[Sequence[ResourceUnionTypeDef]],
    },
)
FunctionUnionTypeDef = Union[FunctionTypeDef, FunctionOutputTypeDef]
CreateResourceDefinitionRequestRequestTypeDef = TypedDict(
    "CreateResourceDefinitionRequestRequestTypeDef",
    {
        "AmznClientToken": NotRequired[str],
        "InitialVersion": NotRequired[ResourceDefinitionVersionTypeDef],
        "Name": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateFunctionDefinitionVersionRequestRequestTypeDef = TypedDict(
    "CreateFunctionDefinitionVersionRequestRequestTypeDef",
    {
        "FunctionDefinitionId": str,
        "AmznClientToken": NotRequired[str],
        "DefaultConfig": NotRequired[FunctionDefaultConfigTypeDef],
        "Functions": NotRequired[Sequence[FunctionUnionTypeDef]],
    },
)
FunctionDefinitionVersionTypeDef = TypedDict(
    "FunctionDefinitionVersionTypeDef",
    {
        "DefaultConfig": NotRequired[FunctionDefaultConfigTypeDef],
        "Functions": NotRequired[Sequence[FunctionUnionTypeDef]],
    },
)
CreateFunctionDefinitionRequestRequestTypeDef = TypedDict(
    "CreateFunctionDefinitionRequestRequestTypeDef",
    {
        "AmznClientToken": NotRequired[str],
        "InitialVersion": NotRequired[FunctionDefinitionVersionTypeDef],
        "Name": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
