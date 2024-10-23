"""
Type annotations for proton service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/type_defs/)

Usage::

    ```python
    from mypy_boto3_proton.type_defs import AcceptEnvironmentAccountConnectionInputRequestTypeDef

    data: AcceptEnvironmentAccountConnectionInputRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import (
    BlockerStatusType,
    ComponentDeploymentUpdateTypeType,
    DeploymentStatusType,
    DeploymentTargetResourceTypeType,
    DeploymentUpdateTypeType,
    EnvironmentAccountConnectionRequesterAccountTypeType,
    EnvironmentAccountConnectionStatusType,
    ListServiceInstancesFilterByType,
    ListServiceInstancesSortByType,
    ProvisionedResourceEngineType,
    RepositoryProviderType,
    RepositorySyncStatusType,
    ResourceDeploymentStatusType,
    ResourceSyncStatusType,
    ServiceStatusType,
    SortOrderType,
    SyncTypeType,
    TemplateTypeType,
    TemplateVersionStatusType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AcceptEnvironmentAccountConnectionInputRequestTypeDef",
    "EnvironmentAccountConnectionTypeDef",
    "ResponseMetadataTypeDef",
    "RepositoryBranchTypeDef",
    "CancelComponentDeploymentInputRequestTypeDef",
    "ComponentTypeDef",
    "CancelEnvironmentDeploymentInputRequestTypeDef",
    "CancelServiceInstanceDeploymentInputRequestTypeDef",
    "ServiceInstanceTypeDef",
    "CancelServicePipelineDeploymentInputRequestTypeDef",
    "ServicePipelineTypeDef",
    "CompatibleEnvironmentTemplateInputTypeDef",
    "CompatibleEnvironmentTemplateTypeDef",
    "ComponentStateTypeDef",
    "ComponentSummaryTypeDef",
    "ResourceCountsSummaryTypeDef",
    "TagTypeDef",
    "RepositoryBranchInputTypeDef",
    "EnvironmentTemplateTypeDef",
    "EnvironmentTemplateVersionTypeDef",
    "RepositoryTypeDef",
    "CreateServiceSyncConfigInputRequestTypeDef",
    "ServiceSyncConfigTypeDef",
    "ServiceTemplateTypeDef",
    "CreateTemplateSyncConfigInputRequestTypeDef",
    "TemplateSyncConfigTypeDef",
    "DeleteComponentInputRequestTypeDef",
    "DeleteDeploymentInputRequestTypeDef",
    "DeleteEnvironmentAccountConnectionInputRequestTypeDef",
    "DeleteEnvironmentInputRequestTypeDef",
    "DeleteEnvironmentTemplateInputRequestTypeDef",
    "DeleteEnvironmentTemplateVersionInputRequestTypeDef",
    "DeleteRepositoryInputRequestTypeDef",
    "DeleteServiceInputRequestTypeDef",
    "DeleteServiceSyncConfigInputRequestTypeDef",
    "DeleteServiceTemplateInputRequestTypeDef",
    "DeleteServiceTemplateVersionInputRequestTypeDef",
    "DeleteTemplateSyncConfigInputRequestTypeDef",
    "EnvironmentStateTypeDef",
    "ServiceInstanceStateTypeDef",
    "ServicePipelineStateTypeDef",
    "DeploymentSummaryTypeDef",
    "EnvironmentAccountConnectionSummaryTypeDef",
    "EnvironmentSummaryTypeDef",
    "EnvironmentTemplateFilterTypeDef",
    "EnvironmentTemplateSummaryTypeDef",
    "EnvironmentTemplateVersionSummaryTypeDef",
    "WaiterConfigTypeDef",
    "GetComponentInputRequestTypeDef",
    "GetDeploymentInputRequestTypeDef",
    "GetEnvironmentAccountConnectionInputRequestTypeDef",
    "GetEnvironmentInputRequestTypeDef",
    "GetEnvironmentTemplateInputRequestTypeDef",
    "GetEnvironmentTemplateVersionInputRequestTypeDef",
    "GetRepositoryInputRequestTypeDef",
    "GetRepositorySyncStatusInputRequestTypeDef",
    "GetServiceInputRequestTypeDef",
    "GetServiceInstanceInputRequestTypeDef",
    "GetServiceInstanceSyncStatusInputRequestTypeDef",
    "RevisionTypeDef",
    "GetServiceSyncBlockerSummaryInputRequestTypeDef",
    "GetServiceSyncConfigInputRequestTypeDef",
    "GetServiceTemplateInputRequestTypeDef",
    "GetServiceTemplateVersionInputRequestTypeDef",
    "GetTemplateSyncConfigInputRequestTypeDef",
    "GetTemplateSyncStatusInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListComponentOutputsInputRequestTypeDef",
    "OutputTypeDef",
    "ListComponentProvisionedResourcesInputRequestTypeDef",
    "ProvisionedResourceTypeDef",
    "ListComponentsInputRequestTypeDef",
    "ListDeploymentsInputRequestTypeDef",
    "ListEnvironmentAccountConnectionsInputRequestTypeDef",
    "ListEnvironmentOutputsInputRequestTypeDef",
    "ListEnvironmentProvisionedResourcesInputRequestTypeDef",
    "ListEnvironmentTemplateVersionsInputRequestTypeDef",
    "ListEnvironmentTemplatesInputRequestTypeDef",
    "ListRepositoriesInputRequestTypeDef",
    "RepositorySummaryTypeDef",
    "ListRepositorySyncDefinitionsInputRequestTypeDef",
    "RepositorySyncDefinitionTypeDef",
    "ListServiceInstanceOutputsInputRequestTypeDef",
    "ListServiceInstanceProvisionedResourcesInputRequestTypeDef",
    "ListServiceInstancesFilterTypeDef",
    "ServiceInstanceSummaryTypeDef",
    "ListServicePipelineOutputsInputRequestTypeDef",
    "ListServicePipelineProvisionedResourcesInputRequestTypeDef",
    "ListServiceTemplateVersionsInputRequestTypeDef",
    "ServiceTemplateVersionSummaryTypeDef",
    "ListServiceTemplatesInputRequestTypeDef",
    "ServiceTemplateSummaryTypeDef",
    "ListServicesInputRequestTypeDef",
    "ServiceSummaryTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "RejectEnvironmentAccountConnectionInputRequestTypeDef",
    "RepositorySyncEventTypeDef",
    "ResourceSyncEventTypeDef",
    "S3ObjectSourceTypeDef",
    "SyncBlockerContextTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateComponentInputRequestTypeDef",
    "UpdateEnvironmentAccountConnectionInputRequestTypeDef",
    "UpdateEnvironmentTemplateInputRequestTypeDef",
    "UpdateEnvironmentTemplateVersionInputRequestTypeDef",
    "UpdateServiceInputRequestTypeDef",
    "UpdateServiceInstanceInputRequestTypeDef",
    "UpdateServicePipelineInputRequestTypeDef",
    "UpdateServiceSyncBlockerInputRequestTypeDef",
    "UpdateServiceSyncConfigInputRequestTypeDef",
    "UpdateServiceTemplateInputRequestTypeDef",
    "UpdateTemplateSyncConfigInputRequestTypeDef",
    "AcceptEnvironmentAccountConnectionOutputTypeDef",
    "CreateEnvironmentAccountConnectionOutputTypeDef",
    "DeleteEnvironmentAccountConnectionOutputTypeDef",
    "GetEnvironmentAccountConnectionOutputTypeDef",
    "RejectEnvironmentAccountConnectionOutputTypeDef",
    "UpdateEnvironmentAccountConnectionOutputTypeDef",
    "AccountSettingsTypeDef",
    "EnvironmentTypeDef",
    "CancelComponentDeploymentOutputTypeDef",
    "CreateComponentOutputTypeDef",
    "DeleteComponentOutputTypeDef",
    "GetComponentOutputTypeDef",
    "UpdateComponentOutputTypeDef",
    "CancelServiceInstanceDeploymentOutputTypeDef",
    "CreateServiceInstanceOutputTypeDef",
    "GetServiceInstanceOutputTypeDef",
    "UpdateServiceInstanceOutputTypeDef",
    "CancelServicePipelineDeploymentOutputTypeDef",
    "ServiceTypeDef",
    "UpdateServicePipelineOutputTypeDef",
    "UpdateServiceTemplateVersionInputRequestTypeDef",
    "ServiceTemplateVersionTypeDef",
    "ListComponentsOutputTypeDef",
    "CountsSummaryTypeDef",
    "CreateComponentInputRequestTypeDef",
    "CreateEnvironmentAccountConnectionInputRequestTypeDef",
    "CreateEnvironmentTemplateInputRequestTypeDef",
    "CreateRepositoryInputRequestTypeDef",
    "CreateServiceInputRequestTypeDef",
    "CreateServiceInstanceInputRequestTypeDef",
    "CreateServiceTemplateInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "TagResourceInputRequestTypeDef",
    "CreateEnvironmentInputRequestTypeDef",
    "UpdateAccountSettingsInputRequestTypeDef",
    "UpdateEnvironmentInputRequestTypeDef",
    "CreateEnvironmentTemplateOutputTypeDef",
    "DeleteEnvironmentTemplateOutputTypeDef",
    "GetEnvironmentTemplateOutputTypeDef",
    "UpdateEnvironmentTemplateOutputTypeDef",
    "CreateEnvironmentTemplateVersionOutputTypeDef",
    "DeleteEnvironmentTemplateVersionOutputTypeDef",
    "GetEnvironmentTemplateVersionOutputTypeDef",
    "UpdateEnvironmentTemplateVersionOutputTypeDef",
    "CreateRepositoryOutputTypeDef",
    "DeleteRepositoryOutputTypeDef",
    "GetRepositoryOutputTypeDef",
    "CreateServiceSyncConfigOutputTypeDef",
    "DeleteServiceSyncConfigOutputTypeDef",
    "GetServiceSyncConfigOutputTypeDef",
    "UpdateServiceSyncConfigOutputTypeDef",
    "CreateServiceTemplateOutputTypeDef",
    "DeleteServiceTemplateOutputTypeDef",
    "GetServiceTemplateOutputTypeDef",
    "UpdateServiceTemplateOutputTypeDef",
    "CreateTemplateSyncConfigOutputTypeDef",
    "DeleteTemplateSyncConfigOutputTypeDef",
    "GetTemplateSyncConfigOutputTypeDef",
    "UpdateTemplateSyncConfigOutputTypeDef",
    "DeploymentStateTypeDef",
    "ListDeploymentsOutputTypeDef",
    "ListEnvironmentAccountConnectionsOutputTypeDef",
    "ListEnvironmentsOutputTypeDef",
    "ListEnvironmentsInputRequestTypeDef",
    "ListEnvironmentTemplatesOutputTypeDef",
    "ListEnvironmentTemplateVersionsOutputTypeDef",
    "GetComponentInputComponentDeletedWaitTypeDef",
    "GetComponentInputComponentDeployedWaitTypeDef",
    "GetEnvironmentInputEnvironmentDeployedWaitTypeDef",
    "GetEnvironmentTemplateVersionInputEnvironmentTemplateVersionRegisteredWaitTypeDef",
    "GetServiceInputServiceCreatedWaitTypeDef",
    "GetServiceInputServiceDeletedWaitTypeDef",
    "GetServiceInputServicePipelineDeployedWaitTypeDef",
    "GetServiceInputServiceUpdatedWaitTypeDef",
    "GetServiceInstanceInputServiceInstanceDeployedWaitTypeDef",
    "GetServiceTemplateVersionInputServiceTemplateVersionRegisteredWaitTypeDef",
    "ListComponentOutputsInputListComponentOutputsPaginateTypeDef",
    "ListComponentProvisionedResourcesInputListComponentProvisionedResourcesPaginateTypeDef",
    "ListComponentsInputListComponentsPaginateTypeDef",
    "ListDeploymentsInputListDeploymentsPaginateTypeDef",
    "ListEnvironmentAccountConnectionsInputListEnvironmentAccountConnectionsPaginateTypeDef",
    "ListEnvironmentOutputsInputListEnvironmentOutputsPaginateTypeDef",
    "ListEnvironmentProvisionedResourcesInputListEnvironmentProvisionedResourcesPaginateTypeDef",
    "ListEnvironmentTemplateVersionsInputListEnvironmentTemplateVersionsPaginateTypeDef",
    "ListEnvironmentTemplatesInputListEnvironmentTemplatesPaginateTypeDef",
    "ListEnvironmentsInputListEnvironmentsPaginateTypeDef",
    "ListRepositoriesInputListRepositoriesPaginateTypeDef",
    "ListRepositorySyncDefinitionsInputListRepositorySyncDefinitionsPaginateTypeDef",
    "ListServiceInstanceOutputsInputListServiceInstanceOutputsPaginateTypeDef",
    "ListServiceInstanceProvisionedResourcesInputListServiceInstanceProvisionedResourcesPaginateTypeDef",
    "ListServicePipelineOutputsInputListServicePipelineOutputsPaginateTypeDef",
    "ListServicePipelineProvisionedResourcesInputListServicePipelineProvisionedResourcesPaginateTypeDef",
    "ListServiceTemplateVersionsInputListServiceTemplateVersionsPaginateTypeDef",
    "ListServiceTemplatesInputListServiceTemplatesPaginateTypeDef",
    "ListServicesInputListServicesPaginateTypeDef",
    "ListTagsForResourceInputListTagsForResourcePaginateTypeDef",
    "ListComponentOutputsOutputTypeDef",
    "ListEnvironmentOutputsOutputTypeDef",
    "ListServiceInstanceOutputsOutputTypeDef",
    "ListServicePipelineOutputsOutputTypeDef",
    "NotifyResourceDeploymentStatusChangeInputRequestTypeDef",
    "ListComponentProvisionedResourcesOutputTypeDef",
    "ListEnvironmentProvisionedResourcesOutputTypeDef",
    "ListServiceInstanceProvisionedResourcesOutputTypeDef",
    "ListServicePipelineProvisionedResourcesOutputTypeDef",
    "ListRepositoriesOutputTypeDef",
    "ListRepositorySyncDefinitionsOutputTypeDef",
    "ListServiceInstancesInputListServiceInstancesPaginateTypeDef",
    "ListServiceInstancesInputRequestTypeDef",
    "ListServiceInstancesOutputTypeDef",
    "ListServiceTemplateVersionsOutputTypeDef",
    "ListServiceTemplatesOutputTypeDef",
    "ListServicesOutputTypeDef",
    "RepositorySyncAttemptTypeDef",
    "ResourceSyncAttemptTypeDef",
    "TemplateVersionSourceInputTypeDef",
    "SyncBlockerTypeDef",
    "GetAccountSettingsOutputTypeDef",
    "UpdateAccountSettingsOutputTypeDef",
    "CancelEnvironmentDeploymentOutputTypeDef",
    "CreateEnvironmentOutputTypeDef",
    "DeleteEnvironmentOutputTypeDef",
    "GetEnvironmentOutputTypeDef",
    "UpdateEnvironmentOutputTypeDef",
    "CreateServiceOutputTypeDef",
    "DeleteServiceOutputTypeDef",
    "GetServiceOutputTypeDef",
    "UpdateServiceOutputTypeDef",
    "CreateServiceTemplateVersionOutputTypeDef",
    "DeleteServiceTemplateVersionOutputTypeDef",
    "GetServiceTemplateVersionOutputTypeDef",
    "UpdateServiceTemplateVersionOutputTypeDef",
    "GetResourcesSummaryOutputTypeDef",
    "DeploymentTypeDef",
    "GetRepositorySyncStatusOutputTypeDef",
    "GetServiceInstanceSyncStatusOutputTypeDef",
    "GetTemplateSyncStatusOutputTypeDef",
    "CreateEnvironmentTemplateVersionInputRequestTypeDef",
    "CreateServiceTemplateVersionInputRequestTypeDef",
    "ServiceSyncBlockerSummaryTypeDef",
    "UpdateServiceSyncBlockerOutputTypeDef",
    "DeleteDeploymentOutputTypeDef",
    "GetDeploymentOutputTypeDef",
    "GetServiceSyncBlockerSummaryOutputTypeDef",
)

AcceptEnvironmentAccountConnectionInputRequestTypeDef = TypedDict(
    "AcceptEnvironmentAccountConnectionInputRequestTypeDef",
    {
        "id": str,
    },
)
EnvironmentAccountConnectionTypeDef = TypedDict(
    "EnvironmentAccountConnectionTypeDef",
    {
        "arn": str,
        "environmentAccountId": str,
        "environmentName": str,
        "id": str,
        "lastModifiedAt": datetime,
        "managementAccountId": str,
        "requestedAt": datetime,
        "roleArn": str,
        "status": EnvironmentAccountConnectionStatusType,
        "codebuildRoleArn": NotRequired[str],
        "componentRoleArn": NotRequired[str],
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
RepositoryBranchTypeDef = TypedDict(
    "RepositoryBranchTypeDef",
    {
        "arn": str,
        "branch": str,
        "name": str,
        "provider": RepositoryProviderType,
    },
)
CancelComponentDeploymentInputRequestTypeDef = TypedDict(
    "CancelComponentDeploymentInputRequestTypeDef",
    {
        "componentName": str,
    },
)
ComponentTypeDef = TypedDict(
    "ComponentTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deploymentStatus": DeploymentStatusType,
        "environmentName": str,
        "lastModifiedAt": datetime,
        "name": str,
        "deploymentStatusMessage": NotRequired[str],
        "description": NotRequired[str],
        "lastAttemptedDeploymentId": NotRequired[str],
        "lastClientRequestToken": NotRequired[str],
        "lastDeploymentAttemptedAt": NotRequired[datetime],
        "lastDeploymentSucceededAt": NotRequired[datetime],
        "lastSucceededDeploymentId": NotRequired[str],
        "serviceInstanceName": NotRequired[str],
        "serviceName": NotRequired[str],
        "serviceSpec": NotRequired[str],
    },
)
CancelEnvironmentDeploymentInputRequestTypeDef = TypedDict(
    "CancelEnvironmentDeploymentInputRequestTypeDef",
    {
        "environmentName": str,
    },
)
CancelServiceInstanceDeploymentInputRequestTypeDef = TypedDict(
    "CancelServiceInstanceDeploymentInputRequestTypeDef",
    {
        "serviceInstanceName": str,
        "serviceName": str,
    },
)
ServiceInstanceTypeDef = TypedDict(
    "ServiceInstanceTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deploymentStatus": DeploymentStatusType,
        "environmentName": str,
        "lastDeploymentAttemptedAt": datetime,
        "lastDeploymentSucceededAt": datetime,
        "name": str,
        "serviceName": str,
        "templateMajorVersion": str,
        "templateMinorVersion": str,
        "templateName": str,
        "deploymentStatusMessage": NotRequired[str],
        "lastAttemptedDeploymentId": NotRequired[str],
        "lastClientRequestToken": NotRequired[str],
        "lastSucceededDeploymentId": NotRequired[str],
        "spec": NotRequired[str],
    },
)
CancelServicePipelineDeploymentInputRequestTypeDef = TypedDict(
    "CancelServicePipelineDeploymentInputRequestTypeDef",
    {
        "serviceName": str,
    },
)
ServicePipelineTypeDef = TypedDict(
    "ServicePipelineTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deploymentStatus": DeploymentStatusType,
        "lastDeploymentAttemptedAt": datetime,
        "lastDeploymentSucceededAt": datetime,
        "templateMajorVersion": str,
        "templateMinorVersion": str,
        "templateName": str,
        "deploymentStatusMessage": NotRequired[str],
        "lastAttemptedDeploymentId": NotRequired[str],
        "lastSucceededDeploymentId": NotRequired[str],
        "spec": NotRequired[str],
    },
)
CompatibleEnvironmentTemplateInputTypeDef = TypedDict(
    "CompatibleEnvironmentTemplateInputTypeDef",
    {
        "majorVersion": str,
        "templateName": str,
    },
)
CompatibleEnvironmentTemplateTypeDef = TypedDict(
    "CompatibleEnvironmentTemplateTypeDef",
    {
        "majorVersion": str,
        "templateName": str,
    },
)
ComponentStateTypeDef = TypedDict(
    "ComponentStateTypeDef",
    {
        "serviceInstanceName": NotRequired[str],
        "serviceName": NotRequired[str],
        "serviceSpec": NotRequired[str],
        "templateFile": NotRequired[str],
    },
)
ComponentSummaryTypeDef = TypedDict(
    "ComponentSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deploymentStatus": DeploymentStatusType,
        "environmentName": str,
        "lastModifiedAt": datetime,
        "name": str,
        "deploymentStatusMessage": NotRequired[str],
        "lastAttemptedDeploymentId": NotRequired[str],
        "lastDeploymentAttemptedAt": NotRequired[datetime],
        "lastDeploymentSucceededAt": NotRequired[datetime],
        "lastSucceededDeploymentId": NotRequired[str],
        "serviceInstanceName": NotRequired[str],
        "serviceName": NotRequired[str],
    },
)
ResourceCountsSummaryTypeDef = TypedDict(
    "ResourceCountsSummaryTypeDef",
    {
        "total": int,
        "behindMajor": NotRequired[int],
        "behindMinor": NotRequired[int],
        "failed": NotRequired[int],
        "upToDate": NotRequired[int],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)
RepositoryBranchInputTypeDef = TypedDict(
    "RepositoryBranchInputTypeDef",
    {
        "branch": str,
        "name": str,
        "provider": RepositoryProviderType,
    },
)
EnvironmentTemplateTypeDef = TypedDict(
    "EnvironmentTemplateTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "name": str,
        "description": NotRequired[str],
        "displayName": NotRequired[str],
        "encryptionKey": NotRequired[str],
        "provisioning": NotRequired[Literal["CUSTOMER_MANAGED"]],
        "recommendedVersion": NotRequired[str],
    },
)
EnvironmentTemplateVersionTypeDef = TypedDict(
    "EnvironmentTemplateVersionTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "majorVersion": str,
        "minorVersion": str,
        "status": TemplateVersionStatusType,
        "templateName": str,
        "description": NotRequired[str],
        "recommendedMinorVersion": NotRequired[str],
        "schema": NotRequired[str],
        "statusMessage": NotRequired[str],
    },
)
RepositoryTypeDef = TypedDict(
    "RepositoryTypeDef",
    {
        "arn": str,
        "connectionArn": str,
        "name": str,
        "provider": RepositoryProviderType,
        "encryptionKey": NotRequired[str],
    },
)
CreateServiceSyncConfigInputRequestTypeDef = TypedDict(
    "CreateServiceSyncConfigInputRequestTypeDef",
    {
        "branch": str,
        "filePath": str,
        "repositoryName": str,
        "repositoryProvider": RepositoryProviderType,
        "serviceName": str,
    },
)
ServiceSyncConfigTypeDef = TypedDict(
    "ServiceSyncConfigTypeDef",
    {
        "branch": str,
        "filePath": str,
        "repositoryName": str,
        "repositoryProvider": RepositoryProviderType,
        "serviceName": str,
    },
)
ServiceTemplateTypeDef = TypedDict(
    "ServiceTemplateTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "name": str,
        "description": NotRequired[str],
        "displayName": NotRequired[str],
        "encryptionKey": NotRequired[str],
        "pipelineProvisioning": NotRequired[Literal["CUSTOMER_MANAGED"]],
        "recommendedVersion": NotRequired[str],
    },
)
CreateTemplateSyncConfigInputRequestTypeDef = TypedDict(
    "CreateTemplateSyncConfigInputRequestTypeDef",
    {
        "branch": str,
        "repositoryName": str,
        "repositoryProvider": RepositoryProviderType,
        "templateName": str,
        "templateType": TemplateTypeType,
        "subdirectory": NotRequired[str],
    },
)
TemplateSyncConfigTypeDef = TypedDict(
    "TemplateSyncConfigTypeDef",
    {
        "branch": str,
        "repositoryName": str,
        "repositoryProvider": RepositoryProviderType,
        "templateName": str,
        "templateType": TemplateTypeType,
        "subdirectory": NotRequired[str],
    },
)
DeleteComponentInputRequestTypeDef = TypedDict(
    "DeleteComponentInputRequestTypeDef",
    {
        "name": str,
    },
)
DeleteDeploymentInputRequestTypeDef = TypedDict(
    "DeleteDeploymentInputRequestTypeDef",
    {
        "id": str,
    },
)
DeleteEnvironmentAccountConnectionInputRequestTypeDef = TypedDict(
    "DeleteEnvironmentAccountConnectionInputRequestTypeDef",
    {
        "id": str,
    },
)
DeleteEnvironmentInputRequestTypeDef = TypedDict(
    "DeleteEnvironmentInputRequestTypeDef",
    {
        "name": str,
    },
)
DeleteEnvironmentTemplateInputRequestTypeDef = TypedDict(
    "DeleteEnvironmentTemplateInputRequestTypeDef",
    {
        "name": str,
    },
)
DeleteEnvironmentTemplateVersionInputRequestTypeDef = TypedDict(
    "DeleteEnvironmentTemplateVersionInputRequestTypeDef",
    {
        "majorVersion": str,
        "minorVersion": str,
        "templateName": str,
    },
)
DeleteRepositoryInputRequestTypeDef = TypedDict(
    "DeleteRepositoryInputRequestTypeDef",
    {
        "name": str,
        "provider": RepositoryProviderType,
    },
)
DeleteServiceInputRequestTypeDef = TypedDict(
    "DeleteServiceInputRequestTypeDef",
    {
        "name": str,
    },
)
DeleteServiceSyncConfigInputRequestTypeDef = TypedDict(
    "DeleteServiceSyncConfigInputRequestTypeDef",
    {
        "serviceName": str,
    },
)
DeleteServiceTemplateInputRequestTypeDef = TypedDict(
    "DeleteServiceTemplateInputRequestTypeDef",
    {
        "name": str,
    },
)
DeleteServiceTemplateVersionInputRequestTypeDef = TypedDict(
    "DeleteServiceTemplateVersionInputRequestTypeDef",
    {
        "majorVersion": str,
        "minorVersion": str,
        "templateName": str,
    },
)
DeleteTemplateSyncConfigInputRequestTypeDef = TypedDict(
    "DeleteTemplateSyncConfigInputRequestTypeDef",
    {
        "templateName": str,
        "templateType": TemplateTypeType,
    },
)
EnvironmentStateTypeDef = TypedDict(
    "EnvironmentStateTypeDef",
    {
        "templateMajorVersion": str,
        "templateMinorVersion": str,
        "templateName": str,
        "spec": NotRequired[str],
    },
)
ServiceInstanceStateTypeDef = TypedDict(
    "ServiceInstanceStateTypeDef",
    {
        "spec": str,
        "templateMajorVersion": str,
        "templateMinorVersion": str,
        "templateName": str,
        "lastSuccessfulComponentDeploymentIds": NotRequired[List[str]],
        "lastSuccessfulEnvironmentDeploymentId": NotRequired[str],
        "lastSuccessfulServicePipelineDeploymentId": NotRequired[str],
    },
)
ServicePipelineStateTypeDef = TypedDict(
    "ServicePipelineStateTypeDef",
    {
        "templateMajorVersion": str,
        "templateMinorVersion": str,
        "templateName": str,
        "spec": NotRequired[str],
    },
)
DeploymentSummaryTypeDef = TypedDict(
    "DeploymentSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deploymentStatus": DeploymentStatusType,
        "environmentName": str,
        "id": str,
        "lastModifiedAt": datetime,
        "targetArn": str,
        "targetResourceCreatedAt": datetime,
        "targetResourceType": DeploymentTargetResourceTypeType,
        "completedAt": NotRequired[datetime],
        "componentName": NotRequired[str],
        "lastAttemptedDeploymentId": NotRequired[str],
        "lastSucceededDeploymentId": NotRequired[str],
        "serviceInstanceName": NotRequired[str],
        "serviceName": NotRequired[str],
    },
)
EnvironmentAccountConnectionSummaryTypeDef = TypedDict(
    "EnvironmentAccountConnectionSummaryTypeDef",
    {
        "arn": str,
        "environmentAccountId": str,
        "environmentName": str,
        "id": str,
        "lastModifiedAt": datetime,
        "managementAccountId": str,
        "requestedAt": datetime,
        "roleArn": str,
        "status": EnvironmentAccountConnectionStatusType,
        "componentRoleArn": NotRequired[str],
    },
)
EnvironmentSummaryTypeDef = TypedDict(
    "EnvironmentSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deploymentStatus": DeploymentStatusType,
        "lastDeploymentAttemptedAt": datetime,
        "lastDeploymentSucceededAt": datetime,
        "name": str,
        "templateMajorVersion": str,
        "templateMinorVersion": str,
        "templateName": str,
        "componentRoleArn": NotRequired[str],
        "deploymentStatusMessage": NotRequired[str],
        "description": NotRequired[str],
        "environmentAccountConnectionId": NotRequired[str],
        "environmentAccountId": NotRequired[str],
        "lastAttemptedDeploymentId": NotRequired[str],
        "lastSucceededDeploymentId": NotRequired[str],
        "protonServiceRoleArn": NotRequired[str],
        "provisioning": NotRequired[Literal["CUSTOMER_MANAGED"]],
    },
)
EnvironmentTemplateFilterTypeDef = TypedDict(
    "EnvironmentTemplateFilterTypeDef",
    {
        "majorVersion": str,
        "templateName": str,
    },
)
EnvironmentTemplateSummaryTypeDef = TypedDict(
    "EnvironmentTemplateSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "name": str,
        "description": NotRequired[str],
        "displayName": NotRequired[str],
        "provisioning": NotRequired[Literal["CUSTOMER_MANAGED"]],
        "recommendedVersion": NotRequired[str],
    },
)
EnvironmentTemplateVersionSummaryTypeDef = TypedDict(
    "EnvironmentTemplateVersionSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "majorVersion": str,
        "minorVersion": str,
        "status": TemplateVersionStatusType,
        "templateName": str,
        "description": NotRequired[str],
        "recommendedMinorVersion": NotRequired[str],
        "statusMessage": NotRequired[str],
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
GetComponentInputRequestTypeDef = TypedDict(
    "GetComponentInputRequestTypeDef",
    {
        "name": str,
    },
)
GetDeploymentInputRequestTypeDef = TypedDict(
    "GetDeploymentInputRequestTypeDef",
    {
        "id": str,
        "componentName": NotRequired[str],
        "environmentName": NotRequired[str],
        "serviceInstanceName": NotRequired[str],
        "serviceName": NotRequired[str],
    },
)
GetEnvironmentAccountConnectionInputRequestTypeDef = TypedDict(
    "GetEnvironmentAccountConnectionInputRequestTypeDef",
    {
        "id": str,
    },
)
GetEnvironmentInputRequestTypeDef = TypedDict(
    "GetEnvironmentInputRequestTypeDef",
    {
        "name": str,
    },
)
GetEnvironmentTemplateInputRequestTypeDef = TypedDict(
    "GetEnvironmentTemplateInputRequestTypeDef",
    {
        "name": str,
    },
)
GetEnvironmentTemplateVersionInputRequestTypeDef = TypedDict(
    "GetEnvironmentTemplateVersionInputRequestTypeDef",
    {
        "majorVersion": str,
        "minorVersion": str,
        "templateName": str,
    },
)
GetRepositoryInputRequestTypeDef = TypedDict(
    "GetRepositoryInputRequestTypeDef",
    {
        "name": str,
        "provider": RepositoryProviderType,
    },
)
GetRepositorySyncStatusInputRequestTypeDef = TypedDict(
    "GetRepositorySyncStatusInputRequestTypeDef",
    {
        "branch": str,
        "repositoryName": str,
        "repositoryProvider": RepositoryProviderType,
        "syncType": SyncTypeType,
    },
)
GetServiceInputRequestTypeDef = TypedDict(
    "GetServiceInputRequestTypeDef",
    {
        "name": str,
    },
)
GetServiceInstanceInputRequestTypeDef = TypedDict(
    "GetServiceInstanceInputRequestTypeDef",
    {
        "name": str,
        "serviceName": str,
    },
)
GetServiceInstanceSyncStatusInputRequestTypeDef = TypedDict(
    "GetServiceInstanceSyncStatusInputRequestTypeDef",
    {
        "serviceInstanceName": str,
        "serviceName": str,
    },
)
RevisionTypeDef = TypedDict(
    "RevisionTypeDef",
    {
        "branch": str,
        "directory": str,
        "repositoryName": str,
        "repositoryProvider": RepositoryProviderType,
        "sha": str,
    },
)
GetServiceSyncBlockerSummaryInputRequestTypeDef = TypedDict(
    "GetServiceSyncBlockerSummaryInputRequestTypeDef",
    {
        "serviceName": str,
        "serviceInstanceName": NotRequired[str],
    },
)
GetServiceSyncConfigInputRequestTypeDef = TypedDict(
    "GetServiceSyncConfigInputRequestTypeDef",
    {
        "serviceName": str,
    },
)
GetServiceTemplateInputRequestTypeDef = TypedDict(
    "GetServiceTemplateInputRequestTypeDef",
    {
        "name": str,
    },
)
GetServiceTemplateVersionInputRequestTypeDef = TypedDict(
    "GetServiceTemplateVersionInputRequestTypeDef",
    {
        "majorVersion": str,
        "minorVersion": str,
        "templateName": str,
    },
)
GetTemplateSyncConfigInputRequestTypeDef = TypedDict(
    "GetTemplateSyncConfigInputRequestTypeDef",
    {
        "templateName": str,
        "templateType": TemplateTypeType,
    },
)
GetTemplateSyncStatusInputRequestTypeDef = TypedDict(
    "GetTemplateSyncStatusInputRequestTypeDef",
    {
        "templateName": str,
        "templateType": TemplateTypeType,
        "templateVersion": str,
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
ListComponentOutputsInputRequestTypeDef = TypedDict(
    "ListComponentOutputsInputRequestTypeDef",
    {
        "componentName": str,
        "deploymentId": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)
OutputTypeDef = TypedDict(
    "OutputTypeDef",
    {
        "key": NotRequired[str],
        "valueString": NotRequired[str],
    },
)
ListComponentProvisionedResourcesInputRequestTypeDef = TypedDict(
    "ListComponentProvisionedResourcesInputRequestTypeDef",
    {
        "componentName": str,
        "nextToken": NotRequired[str],
    },
)
ProvisionedResourceTypeDef = TypedDict(
    "ProvisionedResourceTypeDef",
    {
        "identifier": NotRequired[str],
        "name": NotRequired[str],
        "provisioningEngine": NotRequired[ProvisionedResourceEngineType],
    },
)
ListComponentsInputRequestTypeDef = TypedDict(
    "ListComponentsInputRequestTypeDef",
    {
        "environmentName": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "serviceInstanceName": NotRequired[str],
        "serviceName": NotRequired[str],
    },
)
ListDeploymentsInputRequestTypeDef = TypedDict(
    "ListDeploymentsInputRequestTypeDef",
    {
        "componentName": NotRequired[str],
        "environmentName": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "serviceInstanceName": NotRequired[str],
        "serviceName": NotRequired[str],
    },
)
ListEnvironmentAccountConnectionsInputRequestTypeDef = TypedDict(
    "ListEnvironmentAccountConnectionsInputRequestTypeDef",
    {
        "requestedBy": EnvironmentAccountConnectionRequesterAccountTypeType,
        "environmentName": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "statuses": NotRequired[Sequence[EnvironmentAccountConnectionStatusType]],
    },
)
ListEnvironmentOutputsInputRequestTypeDef = TypedDict(
    "ListEnvironmentOutputsInputRequestTypeDef",
    {
        "environmentName": str,
        "deploymentId": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)
ListEnvironmentProvisionedResourcesInputRequestTypeDef = TypedDict(
    "ListEnvironmentProvisionedResourcesInputRequestTypeDef",
    {
        "environmentName": str,
        "nextToken": NotRequired[str],
    },
)
ListEnvironmentTemplateVersionsInputRequestTypeDef = TypedDict(
    "ListEnvironmentTemplateVersionsInputRequestTypeDef",
    {
        "templateName": str,
        "majorVersion": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListEnvironmentTemplatesInputRequestTypeDef = TypedDict(
    "ListEnvironmentTemplatesInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListRepositoriesInputRequestTypeDef = TypedDict(
    "ListRepositoriesInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
RepositorySummaryTypeDef = TypedDict(
    "RepositorySummaryTypeDef",
    {
        "arn": str,
        "connectionArn": str,
        "name": str,
        "provider": RepositoryProviderType,
    },
)
ListRepositorySyncDefinitionsInputRequestTypeDef = TypedDict(
    "ListRepositorySyncDefinitionsInputRequestTypeDef",
    {
        "repositoryName": str,
        "repositoryProvider": RepositoryProviderType,
        "syncType": SyncTypeType,
        "nextToken": NotRequired[str],
    },
)
RepositorySyncDefinitionTypeDef = TypedDict(
    "RepositorySyncDefinitionTypeDef",
    {
        "branch": str,
        "directory": str,
        "parent": str,
        "target": str,
    },
)
ListServiceInstanceOutputsInputRequestTypeDef = TypedDict(
    "ListServiceInstanceOutputsInputRequestTypeDef",
    {
        "serviceInstanceName": str,
        "serviceName": str,
        "deploymentId": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)
ListServiceInstanceProvisionedResourcesInputRequestTypeDef = TypedDict(
    "ListServiceInstanceProvisionedResourcesInputRequestTypeDef",
    {
        "serviceInstanceName": str,
        "serviceName": str,
        "nextToken": NotRequired[str],
    },
)
ListServiceInstancesFilterTypeDef = TypedDict(
    "ListServiceInstancesFilterTypeDef",
    {
        "key": NotRequired[ListServiceInstancesFilterByType],
        "value": NotRequired[str],
    },
)
ServiceInstanceSummaryTypeDef = TypedDict(
    "ServiceInstanceSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deploymentStatus": DeploymentStatusType,
        "environmentName": str,
        "lastDeploymentAttemptedAt": datetime,
        "lastDeploymentSucceededAt": datetime,
        "name": str,
        "serviceName": str,
        "templateMajorVersion": str,
        "templateMinorVersion": str,
        "templateName": str,
        "deploymentStatusMessage": NotRequired[str],
        "lastAttemptedDeploymentId": NotRequired[str],
        "lastSucceededDeploymentId": NotRequired[str],
    },
)
ListServicePipelineOutputsInputRequestTypeDef = TypedDict(
    "ListServicePipelineOutputsInputRequestTypeDef",
    {
        "serviceName": str,
        "deploymentId": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)
ListServicePipelineProvisionedResourcesInputRequestTypeDef = TypedDict(
    "ListServicePipelineProvisionedResourcesInputRequestTypeDef",
    {
        "serviceName": str,
        "nextToken": NotRequired[str],
    },
)
ListServiceTemplateVersionsInputRequestTypeDef = TypedDict(
    "ListServiceTemplateVersionsInputRequestTypeDef",
    {
        "templateName": str,
        "majorVersion": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ServiceTemplateVersionSummaryTypeDef = TypedDict(
    "ServiceTemplateVersionSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "majorVersion": str,
        "minorVersion": str,
        "status": TemplateVersionStatusType,
        "templateName": str,
        "description": NotRequired[str],
        "recommendedMinorVersion": NotRequired[str],
        "statusMessage": NotRequired[str],
    },
)
ListServiceTemplatesInputRequestTypeDef = TypedDict(
    "ListServiceTemplatesInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ServiceTemplateSummaryTypeDef = TypedDict(
    "ServiceTemplateSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "name": str,
        "description": NotRequired[str],
        "displayName": NotRequired[str],
        "pipelineProvisioning": NotRequired[Literal["CUSTOMER_MANAGED"]],
        "recommendedVersion": NotRequired[str],
    },
)
ListServicesInputRequestTypeDef = TypedDict(
    "ListServicesInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ServiceSummaryTypeDef = TypedDict(
    "ServiceSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "name": str,
        "status": ServiceStatusType,
        "templateName": str,
        "description": NotRequired[str],
        "statusMessage": NotRequired[str],
    },
)
ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
RejectEnvironmentAccountConnectionInputRequestTypeDef = TypedDict(
    "RejectEnvironmentAccountConnectionInputRequestTypeDef",
    {
        "id": str,
    },
)
RepositorySyncEventTypeDef = TypedDict(
    "RepositorySyncEventTypeDef",
    {
        "event": str,
        "time": datetime,
        "type": str,
        "externalId": NotRequired[str],
    },
)
ResourceSyncEventTypeDef = TypedDict(
    "ResourceSyncEventTypeDef",
    {
        "event": str,
        "time": datetime,
        "type": str,
        "externalId": NotRequired[str],
    },
)
S3ObjectSourceTypeDef = TypedDict(
    "S3ObjectSourceTypeDef",
    {
        "bucket": str,
        "key": str,
    },
)
SyncBlockerContextTypeDef = TypedDict(
    "SyncBlockerContextTypeDef",
    {
        "key": str,
        "value": str,
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UpdateComponentInputRequestTypeDef = TypedDict(
    "UpdateComponentInputRequestTypeDef",
    {
        "deploymentType": ComponentDeploymentUpdateTypeType,
        "name": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "serviceInstanceName": NotRequired[str],
        "serviceName": NotRequired[str],
        "serviceSpec": NotRequired[str],
        "templateFile": NotRequired[str],
    },
)
UpdateEnvironmentAccountConnectionInputRequestTypeDef = TypedDict(
    "UpdateEnvironmentAccountConnectionInputRequestTypeDef",
    {
        "id": str,
        "codebuildRoleArn": NotRequired[str],
        "componentRoleArn": NotRequired[str],
        "roleArn": NotRequired[str],
    },
)
UpdateEnvironmentTemplateInputRequestTypeDef = TypedDict(
    "UpdateEnvironmentTemplateInputRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "displayName": NotRequired[str],
    },
)
UpdateEnvironmentTemplateVersionInputRequestTypeDef = TypedDict(
    "UpdateEnvironmentTemplateVersionInputRequestTypeDef",
    {
        "majorVersion": str,
        "minorVersion": str,
        "templateName": str,
        "description": NotRequired[str],
        "status": NotRequired[TemplateVersionStatusType],
    },
)
UpdateServiceInputRequestTypeDef = TypedDict(
    "UpdateServiceInputRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "spec": NotRequired[str],
    },
)
UpdateServiceInstanceInputRequestTypeDef = TypedDict(
    "UpdateServiceInstanceInputRequestTypeDef",
    {
        "deploymentType": DeploymentUpdateTypeType,
        "name": str,
        "serviceName": str,
        "clientToken": NotRequired[str],
        "spec": NotRequired[str],
        "templateMajorVersion": NotRequired[str],
        "templateMinorVersion": NotRequired[str],
    },
)
UpdateServicePipelineInputRequestTypeDef = TypedDict(
    "UpdateServicePipelineInputRequestTypeDef",
    {
        "deploymentType": DeploymentUpdateTypeType,
        "serviceName": str,
        "spec": str,
        "templateMajorVersion": NotRequired[str],
        "templateMinorVersion": NotRequired[str],
    },
)
UpdateServiceSyncBlockerInputRequestTypeDef = TypedDict(
    "UpdateServiceSyncBlockerInputRequestTypeDef",
    {
        "id": str,
        "resolvedReason": str,
    },
)
UpdateServiceSyncConfigInputRequestTypeDef = TypedDict(
    "UpdateServiceSyncConfigInputRequestTypeDef",
    {
        "branch": str,
        "filePath": str,
        "repositoryName": str,
        "repositoryProvider": RepositoryProviderType,
        "serviceName": str,
    },
)
UpdateServiceTemplateInputRequestTypeDef = TypedDict(
    "UpdateServiceTemplateInputRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "displayName": NotRequired[str],
    },
)
UpdateTemplateSyncConfigInputRequestTypeDef = TypedDict(
    "UpdateTemplateSyncConfigInputRequestTypeDef",
    {
        "branch": str,
        "repositoryName": str,
        "repositoryProvider": RepositoryProviderType,
        "templateName": str,
        "templateType": TemplateTypeType,
        "subdirectory": NotRequired[str],
    },
)
AcceptEnvironmentAccountConnectionOutputTypeDef = TypedDict(
    "AcceptEnvironmentAccountConnectionOutputTypeDef",
    {
        "environmentAccountConnection": EnvironmentAccountConnectionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEnvironmentAccountConnectionOutputTypeDef = TypedDict(
    "CreateEnvironmentAccountConnectionOutputTypeDef",
    {
        "environmentAccountConnection": EnvironmentAccountConnectionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteEnvironmentAccountConnectionOutputTypeDef = TypedDict(
    "DeleteEnvironmentAccountConnectionOutputTypeDef",
    {
        "environmentAccountConnection": EnvironmentAccountConnectionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEnvironmentAccountConnectionOutputTypeDef = TypedDict(
    "GetEnvironmentAccountConnectionOutputTypeDef",
    {
        "environmentAccountConnection": EnvironmentAccountConnectionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RejectEnvironmentAccountConnectionOutputTypeDef = TypedDict(
    "RejectEnvironmentAccountConnectionOutputTypeDef",
    {
        "environmentAccountConnection": EnvironmentAccountConnectionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEnvironmentAccountConnectionOutputTypeDef = TypedDict(
    "UpdateEnvironmentAccountConnectionOutputTypeDef",
    {
        "environmentAccountConnection": EnvironmentAccountConnectionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AccountSettingsTypeDef = TypedDict(
    "AccountSettingsTypeDef",
    {
        "pipelineCodebuildRoleArn": NotRequired[str],
        "pipelineProvisioningRepository": NotRequired[RepositoryBranchTypeDef],
        "pipelineServiceRoleArn": NotRequired[str],
    },
)
EnvironmentTypeDef = TypedDict(
    "EnvironmentTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deploymentStatus": DeploymentStatusType,
        "lastDeploymentAttemptedAt": datetime,
        "lastDeploymentSucceededAt": datetime,
        "name": str,
        "templateMajorVersion": str,
        "templateMinorVersion": str,
        "templateName": str,
        "codebuildRoleArn": NotRequired[str],
        "componentRoleArn": NotRequired[str],
        "deploymentStatusMessage": NotRequired[str],
        "description": NotRequired[str],
        "environmentAccountConnectionId": NotRequired[str],
        "environmentAccountId": NotRequired[str],
        "lastAttemptedDeploymentId": NotRequired[str],
        "lastSucceededDeploymentId": NotRequired[str],
        "protonServiceRoleArn": NotRequired[str],
        "provisioning": NotRequired[Literal["CUSTOMER_MANAGED"]],
        "provisioningRepository": NotRequired[RepositoryBranchTypeDef],
        "spec": NotRequired[str],
    },
)
CancelComponentDeploymentOutputTypeDef = TypedDict(
    "CancelComponentDeploymentOutputTypeDef",
    {
        "component": ComponentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateComponentOutputTypeDef = TypedDict(
    "CreateComponentOutputTypeDef",
    {
        "component": ComponentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteComponentOutputTypeDef = TypedDict(
    "DeleteComponentOutputTypeDef",
    {
        "component": ComponentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetComponentOutputTypeDef = TypedDict(
    "GetComponentOutputTypeDef",
    {
        "component": ComponentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateComponentOutputTypeDef = TypedDict(
    "UpdateComponentOutputTypeDef",
    {
        "component": ComponentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CancelServiceInstanceDeploymentOutputTypeDef = TypedDict(
    "CancelServiceInstanceDeploymentOutputTypeDef",
    {
        "serviceInstance": ServiceInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateServiceInstanceOutputTypeDef = TypedDict(
    "CreateServiceInstanceOutputTypeDef",
    {
        "serviceInstance": ServiceInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServiceInstanceOutputTypeDef = TypedDict(
    "GetServiceInstanceOutputTypeDef",
    {
        "serviceInstance": ServiceInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateServiceInstanceOutputTypeDef = TypedDict(
    "UpdateServiceInstanceOutputTypeDef",
    {
        "serviceInstance": ServiceInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CancelServicePipelineDeploymentOutputTypeDef = TypedDict(
    "CancelServicePipelineDeploymentOutputTypeDef",
    {
        "pipeline": ServicePipelineTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "name": str,
        "spec": str,
        "status": ServiceStatusType,
        "templateName": str,
        "branchName": NotRequired[str],
        "description": NotRequired[str],
        "pipeline": NotRequired[ServicePipelineTypeDef],
        "repositoryConnectionArn": NotRequired[str],
        "repositoryId": NotRequired[str],
        "statusMessage": NotRequired[str],
    },
)
UpdateServicePipelineOutputTypeDef = TypedDict(
    "UpdateServicePipelineOutputTypeDef",
    {
        "pipeline": ServicePipelineTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateServiceTemplateVersionInputRequestTypeDef = TypedDict(
    "UpdateServiceTemplateVersionInputRequestTypeDef",
    {
        "majorVersion": str,
        "minorVersion": str,
        "templateName": str,
        "compatibleEnvironmentTemplates": NotRequired[
            Sequence[CompatibleEnvironmentTemplateInputTypeDef]
        ],
        "description": NotRequired[str],
        "status": NotRequired[TemplateVersionStatusType],
        "supportedComponentSources": NotRequired[Sequence[Literal["DIRECTLY_DEFINED"]]],
    },
)
ServiceTemplateVersionTypeDef = TypedDict(
    "ServiceTemplateVersionTypeDef",
    {
        "arn": str,
        "compatibleEnvironmentTemplates": List[CompatibleEnvironmentTemplateTypeDef],
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "majorVersion": str,
        "minorVersion": str,
        "status": TemplateVersionStatusType,
        "templateName": str,
        "description": NotRequired[str],
        "recommendedMinorVersion": NotRequired[str],
        "schema": NotRequired[str],
        "statusMessage": NotRequired[str],
        "supportedComponentSources": NotRequired[List[Literal["DIRECTLY_DEFINED"]]],
    },
)
ListComponentsOutputTypeDef = TypedDict(
    "ListComponentsOutputTypeDef",
    {
        "components": List[ComponentSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CountsSummaryTypeDef = TypedDict(
    "CountsSummaryTypeDef",
    {
        "components": NotRequired[ResourceCountsSummaryTypeDef],
        "environmentTemplates": NotRequired[ResourceCountsSummaryTypeDef],
        "environments": NotRequired[ResourceCountsSummaryTypeDef],
        "pipelines": NotRequired[ResourceCountsSummaryTypeDef],
        "serviceInstances": NotRequired[ResourceCountsSummaryTypeDef],
        "serviceTemplates": NotRequired[ResourceCountsSummaryTypeDef],
        "services": NotRequired[ResourceCountsSummaryTypeDef],
    },
)
CreateComponentInputRequestTypeDef = TypedDict(
    "CreateComponentInputRequestTypeDef",
    {
        "manifest": str,
        "name": str,
        "templateFile": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "environmentName": NotRequired[str],
        "serviceInstanceName": NotRequired[str],
        "serviceName": NotRequired[str],
        "serviceSpec": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateEnvironmentAccountConnectionInputRequestTypeDef = TypedDict(
    "CreateEnvironmentAccountConnectionInputRequestTypeDef",
    {
        "environmentName": str,
        "managementAccountId": str,
        "clientToken": NotRequired[str],
        "codebuildRoleArn": NotRequired[str],
        "componentRoleArn": NotRequired[str],
        "roleArn": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateEnvironmentTemplateInputRequestTypeDef = TypedDict(
    "CreateEnvironmentTemplateInputRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "displayName": NotRequired[str],
        "encryptionKey": NotRequired[str],
        "provisioning": NotRequired[Literal["CUSTOMER_MANAGED"]],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateRepositoryInputRequestTypeDef = TypedDict(
    "CreateRepositoryInputRequestTypeDef",
    {
        "connectionArn": str,
        "name": str,
        "provider": RepositoryProviderType,
        "encryptionKey": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateServiceInputRequestTypeDef = TypedDict(
    "CreateServiceInputRequestTypeDef",
    {
        "name": str,
        "spec": str,
        "templateMajorVersion": str,
        "templateName": str,
        "branchName": NotRequired[str],
        "description": NotRequired[str],
        "repositoryConnectionArn": NotRequired[str],
        "repositoryId": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "templateMinorVersion": NotRequired[str],
    },
)
CreateServiceInstanceInputRequestTypeDef = TypedDict(
    "CreateServiceInstanceInputRequestTypeDef",
    {
        "name": str,
        "serviceName": str,
        "spec": str,
        "clientToken": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "templateMajorVersion": NotRequired[str],
        "templateMinorVersion": NotRequired[str],
    },
)
CreateServiceTemplateInputRequestTypeDef = TypedDict(
    "CreateServiceTemplateInputRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "displayName": NotRequired[str],
        "encryptionKey": NotRequired[str],
        "pipelineProvisioning": NotRequired[Literal["CUSTOMER_MANAGED"]],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "nextToken": str,
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[TagTypeDef],
    },
)
CreateEnvironmentInputRequestTypeDef = TypedDict(
    "CreateEnvironmentInputRequestTypeDef",
    {
        "name": str,
        "spec": str,
        "templateMajorVersion": str,
        "templateName": str,
        "codebuildRoleArn": NotRequired[str],
        "componentRoleArn": NotRequired[str],
        "description": NotRequired[str],
        "environmentAccountConnectionId": NotRequired[str],
        "protonServiceRoleArn": NotRequired[str],
        "provisioningRepository": NotRequired[RepositoryBranchInputTypeDef],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "templateMinorVersion": NotRequired[str],
    },
)
UpdateAccountSettingsInputRequestTypeDef = TypedDict(
    "UpdateAccountSettingsInputRequestTypeDef",
    {
        "deletePipelineProvisioningRepository": NotRequired[bool],
        "pipelineCodebuildRoleArn": NotRequired[str],
        "pipelineProvisioningRepository": NotRequired[RepositoryBranchInputTypeDef],
        "pipelineServiceRoleArn": NotRequired[str],
    },
)
UpdateEnvironmentInputRequestTypeDef = TypedDict(
    "UpdateEnvironmentInputRequestTypeDef",
    {
        "deploymentType": DeploymentUpdateTypeType,
        "name": str,
        "codebuildRoleArn": NotRequired[str],
        "componentRoleArn": NotRequired[str],
        "description": NotRequired[str],
        "environmentAccountConnectionId": NotRequired[str],
        "protonServiceRoleArn": NotRequired[str],
        "provisioningRepository": NotRequired[RepositoryBranchInputTypeDef],
        "spec": NotRequired[str],
        "templateMajorVersion": NotRequired[str],
        "templateMinorVersion": NotRequired[str],
    },
)
CreateEnvironmentTemplateOutputTypeDef = TypedDict(
    "CreateEnvironmentTemplateOutputTypeDef",
    {
        "environmentTemplate": EnvironmentTemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteEnvironmentTemplateOutputTypeDef = TypedDict(
    "DeleteEnvironmentTemplateOutputTypeDef",
    {
        "environmentTemplate": EnvironmentTemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEnvironmentTemplateOutputTypeDef = TypedDict(
    "GetEnvironmentTemplateOutputTypeDef",
    {
        "environmentTemplate": EnvironmentTemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEnvironmentTemplateOutputTypeDef = TypedDict(
    "UpdateEnvironmentTemplateOutputTypeDef",
    {
        "environmentTemplate": EnvironmentTemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEnvironmentTemplateVersionOutputTypeDef = TypedDict(
    "CreateEnvironmentTemplateVersionOutputTypeDef",
    {
        "environmentTemplateVersion": EnvironmentTemplateVersionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteEnvironmentTemplateVersionOutputTypeDef = TypedDict(
    "DeleteEnvironmentTemplateVersionOutputTypeDef",
    {
        "environmentTemplateVersion": EnvironmentTemplateVersionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEnvironmentTemplateVersionOutputTypeDef = TypedDict(
    "GetEnvironmentTemplateVersionOutputTypeDef",
    {
        "environmentTemplateVersion": EnvironmentTemplateVersionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEnvironmentTemplateVersionOutputTypeDef = TypedDict(
    "UpdateEnvironmentTemplateVersionOutputTypeDef",
    {
        "environmentTemplateVersion": EnvironmentTemplateVersionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRepositoryOutputTypeDef = TypedDict(
    "CreateRepositoryOutputTypeDef",
    {
        "repository": RepositoryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteRepositoryOutputTypeDef = TypedDict(
    "DeleteRepositoryOutputTypeDef",
    {
        "repository": RepositoryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRepositoryOutputTypeDef = TypedDict(
    "GetRepositoryOutputTypeDef",
    {
        "repository": RepositoryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateServiceSyncConfigOutputTypeDef = TypedDict(
    "CreateServiceSyncConfigOutputTypeDef",
    {
        "serviceSyncConfig": ServiceSyncConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteServiceSyncConfigOutputTypeDef = TypedDict(
    "DeleteServiceSyncConfigOutputTypeDef",
    {
        "serviceSyncConfig": ServiceSyncConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServiceSyncConfigOutputTypeDef = TypedDict(
    "GetServiceSyncConfigOutputTypeDef",
    {
        "serviceSyncConfig": ServiceSyncConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateServiceSyncConfigOutputTypeDef = TypedDict(
    "UpdateServiceSyncConfigOutputTypeDef",
    {
        "serviceSyncConfig": ServiceSyncConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateServiceTemplateOutputTypeDef = TypedDict(
    "CreateServiceTemplateOutputTypeDef",
    {
        "serviceTemplate": ServiceTemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteServiceTemplateOutputTypeDef = TypedDict(
    "DeleteServiceTemplateOutputTypeDef",
    {
        "serviceTemplate": ServiceTemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServiceTemplateOutputTypeDef = TypedDict(
    "GetServiceTemplateOutputTypeDef",
    {
        "serviceTemplate": ServiceTemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateServiceTemplateOutputTypeDef = TypedDict(
    "UpdateServiceTemplateOutputTypeDef",
    {
        "serviceTemplate": ServiceTemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTemplateSyncConfigOutputTypeDef = TypedDict(
    "CreateTemplateSyncConfigOutputTypeDef",
    {
        "templateSyncConfig": TemplateSyncConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTemplateSyncConfigOutputTypeDef = TypedDict(
    "DeleteTemplateSyncConfigOutputTypeDef",
    {
        "templateSyncConfig": TemplateSyncConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTemplateSyncConfigOutputTypeDef = TypedDict(
    "GetTemplateSyncConfigOutputTypeDef",
    {
        "templateSyncConfig": TemplateSyncConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTemplateSyncConfigOutputTypeDef = TypedDict(
    "UpdateTemplateSyncConfigOutputTypeDef",
    {
        "templateSyncConfig": TemplateSyncConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeploymentStateTypeDef = TypedDict(
    "DeploymentStateTypeDef",
    {
        "component": NotRequired[ComponentStateTypeDef],
        "environment": NotRequired[EnvironmentStateTypeDef],
        "serviceInstance": NotRequired[ServiceInstanceStateTypeDef],
        "servicePipeline": NotRequired[ServicePipelineStateTypeDef],
    },
)
ListDeploymentsOutputTypeDef = TypedDict(
    "ListDeploymentsOutputTypeDef",
    {
        "deployments": List[DeploymentSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEnvironmentAccountConnectionsOutputTypeDef = TypedDict(
    "ListEnvironmentAccountConnectionsOutputTypeDef",
    {
        "environmentAccountConnections": List[EnvironmentAccountConnectionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEnvironmentsOutputTypeDef = TypedDict(
    "ListEnvironmentsOutputTypeDef",
    {
        "environments": List[EnvironmentSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEnvironmentsInputRequestTypeDef = TypedDict(
    "ListEnvironmentsInputRequestTypeDef",
    {
        "environmentTemplates": NotRequired[Sequence[EnvironmentTemplateFilterTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListEnvironmentTemplatesOutputTypeDef = TypedDict(
    "ListEnvironmentTemplatesOutputTypeDef",
    {
        "nextToken": str,
        "templates": List[EnvironmentTemplateSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEnvironmentTemplateVersionsOutputTypeDef = TypedDict(
    "ListEnvironmentTemplateVersionsOutputTypeDef",
    {
        "nextToken": str,
        "templateVersions": List[EnvironmentTemplateVersionSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetComponentInputComponentDeletedWaitTypeDef = TypedDict(
    "GetComponentInputComponentDeletedWaitTypeDef",
    {
        "name": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetComponentInputComponentDeployedWaitTypeDef = TypedDict(
    "GetComponentInputComponentDeployedWaitTypeDef",
    {
        "name": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetEnvironmentInputEnvironmentDeployedWaitTypeDef = TypedDict(
    "GetEnvironmentInputEnvironmentDeployedWaitTypeDef",
    {
        "name": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetEnvironmentTemplateVersionInputEnvironmentTemplateVersionRegisteredWaitTypeDef = TypedDict(
    "GetEnvironmentTemplateVersionInputEnvironmentTemplateVersionRegisteredWaitTypeDef",
    {
        "majorVersion": str,
        "minorVersion": str,
        "templateName": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetServiceInputServiceCreatedWaitTypeDef = TypedDict(
    "GetServiceInputServiceCreatedWaitTypeDef",
    {
        "name": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetServiceInputServiceDeletedWaitTypeDef = TypedDict(
    "GetServiceInputServiceDeletedWaitTypeDef",
    {
        "name": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetServiceInputServicePipelineDeployedWaitTypeDef = TypedDict(
    "GetServiceInputServicePipelineDeployedWaitTypeDef",
    {
        "name": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetServiceInputServiceUpdatedWaitTypeDef = TypedDict(
    "GetServiceInputServiceUpdatedWaitTypeDef",
    {
        "name": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetServiceInstanceInputServiceInstanceDeployedWaitTypeDef = TypedDict(
    "GetServiceInstanceInputServiceInstanceDeployedWaitTypeDef",
    {
        "name": str,
        "serviceName": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetServiceTemplateVersionInputServiceTemplateVersionRegisteredWaitTypeDef = TypedDict(
    "GetServiceTemplateVersionInputServiceTemplateVersionRegisteredWaitTypeDef",
    {
        "majorVersion": str,
        "minorVersion": str,
        "templateName": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
ListComponentOutputsInputListComponentOutputsPaginateTypeDef = TypedDict(
    "ListComponentOutputsInputListComponentOutputsPaginateTypeDef",
    {
        "componentName": str,
        "deploymentId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListComponentProvisionedResourcesInputListComponentProvisionedResourcesPaginateTypeDef = TypedDict(
    "ListComponentProvisionedResourcesInputListComponentProvisionedResourcesPaginateTypeDef",
    {
        "componentName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListComponentsInputListComponentsPaginateTypeDef = TypedDict(
    "ListComponentsInputListComponentsPaginateTypeDef",
    {
        "environmentName": NotRequired[str],
        "serviceInstanceName": NotRequired[str],
        "serviceName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDeploymentsInputListDeploymentsPaginateTypeDef = TypedDict(
    "ListDeploymentsInputListDeploymentsPaginateTypeDef",
    {
        "componentName": NotRequired[str],
        "environmentName": NotRequired[str],
        "serviceInstanceName": NotRequired[str],
        "serviceName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEnvironmentAccountConnectionsInputListEnvironmentAccountConnectionsPaginateTypeDef = TypedDict(
    "ListEnvironmentAccountConnectionsInputListEnvironmentAccountConnectionsPaginateTypeDef",
    {
        "requestedBy": EnvironmentAccountConnectionRequesterAccountTypeType,
        "environmentName": NotRequired[str],
        "statuses": NotRequired[Sequence[EnvironmentAccountConnectionStatusType]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEnvironmentOutputsInputListEnvironmentOutputsPaginateTypeDef = TypedDict(
    "ListEnvironmentOutputsInputListEnvironmentOutputsPaginateTypeDef",
    {
        "environmentName": str,
        "deploymentId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEnvironmentProvisionedResourcesInputListEnvironmentProvisionedResourcesPaginateTypeDef = TypedDict(
    "ListEnvironmentProvisionedResourcesInputListEnvironmentProvisionedResourcesPaginateTypeDef",
    {
        "environmentName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEnvironmentTemplateVersionsInputListEnvironmentTemplateVersionsPaginateTypeDef = TypedDict(
    "ListEnvironmentTemplateVersionsInputListEnvironmentTemplateVersionsPaginateTypeDef",
    {
        "templateName": str,
        "majorVersion": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEnvironmentTemplatesInputListEnvironmentTemplatesPaginateTypeDef = TypedDict(
    "ListEnvironmentTemplatesInputListEnvironmentTemplatesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEnvironmentsInputListEnvironmentsPaginateTypeDef = TypedDict(
    "ListEnvironmentsInputListEnvironmentsPaginateTypeDef",
    {
        "environmentTemplates": NotRequired[Sequence[EnvironmentTemplateFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRepositoriesInputListRepositoriesPaginateTypeDef = TypedDict(
    "ListRepositoriesInputListRepositoriesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRepositorySyncDefinitionsInputListRepositorySyncDefinitionsPaginateTypeDef = TypedDict(
    "ListRepositorySyncDefinitionsInputListRepositorySyncDefinitionsPaginateTypeDef",
    {
        "repositoryName": str,
        "repositoryProvider": RepositoryProviderType,
        "syncType": SyncTypeType,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListServiceInstanceOutputsInputListServiceInstanceOutputsPaginateTypeDef = TypedDict(
    "ListServiceInstanceOutputsInputListServiceInstanceOutputsPaginateTypeDef",
    {
        "serviceInstanceName": str,
        "serviceName": str,
        "deploymentId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListServiceInstanceProvisionedResourcesInputListServiceInstanceProvisionedResourcesPaginateTypeDef = TypedDict(
    "ListServiceInstanceProvisionedResourcesInputListServiceInstanceProvisionedResourcesPaginateTypeDef",
    {
        "serviceInstanceName": str,
        "serviceName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListServicePipelineOutputsInputListServicePipelineOutputsPaginateTypeDef = TypedDict(
    "ListServicePipelineOutputsInputListServicePipelineOutputsPaginateTypeDef",
    {
        "serviceName": str,
        "deploymentId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListServicePipelineProvisionedResourcesInputListServicePipelineProvisionedResourcesPaginateTypeDef = TypedDict(
    "ListServicePipelineProvisionedResourcesInputListServicePipelineProvisionedResourcesPaginateTypeDef",
    {
        "serviceName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListServiceTemplateVersionsInputListServiceTemplateVersionsPaginateTypeDef = TypedDict(
    "ListServiceTemplateVersionsInputListServiceTemplateVersionsPaginateTypeDef",
    {
        "templateName": str,
        "majorVersion": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListServiceTemplatesInputListServiceTemplatesPaginateTypeDef = TypedDict(
    "ListServiceTemplatesInputListServiceTemplatesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListServicesInputListServicesPaginateTypeDef = TypedDict(
    "ListServicesInputListServicesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTagsForResourceInputListTagsForResourcePaginateTypeDef = TypedDict(
    "ListTagsForResourceInputListTagsForResourcePaginateTypeDef",
    {
        "resourceArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListComponentOutputsOutputTypeDef = TypedDict(
    "ListComponentOutputsOutputTypeDef",
    {
        "nextToken": str,
        "outputs": List[OutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEnvironmentOutputsOutputTypeDef = TypedDict(
    "ListEnvironmentOutputsOutputTypeDef",
    {
        "nextToken": str,
        "outputs": List[OutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListServiceInstanceOutputsOutputTypeDef = TypedDict(
    "ListServiceInstanceOutputsOutputTypeDef",
    {
        "nextToken": str,
        "outputs": List[OutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListServicePipelineOutputsOutputTypeDef = TypedDict(
    "ListServicePipelineOutputsOutputTypeDef",
    {
        "nextToken": str,
        "outputs": List[OutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NotifyResourceDeploymentStatusChangeInputRequestTypeDef = TypedDict(
    "NotifyResourceDeploymentStatusChangeInputRequestTypeDef",
    {
        "resourceArn": str,
        "deploymentId": NotRequired[str],
        "outputs": NotRequired[Sequence[OutputTypeDef]],
        "status": NotRequired[ResourceDeploymentStatusType],
        "statusMessage": NotRequired[str],
    },
)
ListComponentProvisionedResourcesOutputTypeDef = TypedDict(
    "ListComponentProvisionedResourcesOutputTypeDef",
    {
        "nextToken": str,
        "provisionedResources": List[ProvisionedResourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEnvironmentProvisionedResourcesOutputTypeDef = TypedDict(
    "ListEnvironmentProvisionedResourcesOutputTypeDef",
    {
        "nextToken": str,
        "provisionedResources": List[ProvisionedResourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListServiceInstanceProvisionedResourcesOutputTypeDef = TypedDict(
    "ListServiceInstanceProvisionedResourcesOutputTypeDef",
    {
        "nextToken": str,
        "provisionedResources": List[ProvisionedResourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListServicePipelineProvisionedResourcesOutputTypeDef = TypedDict(
    "ListServicePipelineProvisionedResourcesOutputTypeDef",
    {
        "nextToken": str,
        "provisionedResources": List[ProvisionedResourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRepositoriesOutputTypeDef = TypedDict(
    "ListRepositoriesOutputTypeDef",
    {
        "nextToken": str,
        "repositories": List[RepositorySummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRepositorySyncDefinitionsOutputTypeDef = TypedDict(
    "ListRepositorySyncDefinitionsOutputTypeDef",
    {
        "nextToken": str,
        "syncDefinitions": List[RepositorySyncDefinitionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListServiceInstancesInputListServiceInstancesPaginateTypeDef = TypedDict(
    "ListServiceInstancesInputListServiceInstancesPaginateTypeDef",
    {
        "filters": NotRequired[Sequence[ListServiceInstancesFilterTypeDef]],
        "serviceName": NotRequired[str],
        "sortBy": NotRequired[ListServiceInstancesSortByType],
        "sortOrder": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListServiceInstancesInputRequestTypeDef = TypedDict(
    "ListServiceInstancesInputRequestTypeDef",
    {
        "filters": NotRequired[Sequence[ListServiceInstancesFilterTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "serviceName": NotRequired[str],
        "sortBy": NotRequired[ListServiceInstancesSortByType],
        "sortOrder": NotRequired[SortOrderType],
    },
)
ListServiceInstancesOutputTypeDef = TypedDict(
    "ListServiceInstancesOutputTypeDef",
    {
        "nextToken": str,
        "serviceInstances": List[ServiceInstanceSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListServiceTemplateVersionsOutputTypeDef = TypedDict(
    "ListServiceTemplateVersionsOutputTypeDef",
    {
        "nextToken": str,
        "templateVersions": List[ServiceTemplateVersionSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListServiceTemplatesOutputTypeDef = TypedDict(
    "ListServiceTemplatesOutputTypeDef",
    {
        "nextToken": str,
        "templates": List[ServiceTemplateSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListServicesOutputTypeDef = TypedDict(
    "ListServicesOutputTypeDef",
    {
        "nextToken": str,
        "services": List[ServiceSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RepositorySyncAttemptTypeDef = TypedDict(
    "RepositorySyncAttemptTypeDef",
    {
        "events": List[RepositorySyncEventTypeDef],
        "startedAt": datetime,
        "status": RepositorySyncStatusType,
    },
)
ResourceSyncAttemptTypeDef = TypedDict(
    "ResourceSyncAttemptTypeDef",
    {
        "events": List[ResourceSyncEventTypeDef],
        "initialRevision": RevisionTypeDef,
        "startedAt": datetime,
        "status": ResourceSyncStatusType,
        "target": str,
        "targetRevision": RevisionTypeDef,
    },
)
TemplateVersionSourceInputTypeDef = TypedDict(
    "TemplateVersionSourceInputTypeDef",
    {
        "s3": NotRequired[S3ObjectSourceTypeDef],
    },
)
SyncBlockerTypeDef = TypedDict(
    "SyncBlockerTypeDef",
    {
        "createdAt": datetime,
        "createdReason": str,
        "id": str,
        "status": BlockerStatusType,
        "type": Literal["AUTOMATED"],
        "contexts": NotRequired[List[SyncBlockerContextTypeDef]],
        "resolvedAt": NotRequired[datetime],
        "resolvedReason": NotRequired[str],
    },
)
GetAccountSettingsOutputTypeDef = TypedDict(
    "GetAccountSettingsOutputTypeDef",
    {
        "accountSettings": AccountSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAccountSettingsOutputTypeDef = TypedDict(
    "UpdateAccountSettingsOutputTypeDef",
    {
        "accountSettings": AccountSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CancelEnvironmentDeploymentOutputTypeDef = TypedDict(
    "CancelEnvironmentDeploymentOutputTypeDef",
    {
        "environment": EnvironmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEnvironmentOutputTypeDef = TypedDict(
    "CreateEnvironmentOutputTypeDef",
    {
        "environment": EnvironmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteEnvironmentOutputTypeDef = TypedDict(
    "DeleteEnvironmentOutputTypeDef",
    {
        "environment": EnvironmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEnvironmentOutputTypeDef = TypedDict(
    "GetEnvironmentOutputTypeDef",
    {
        "environment": EnvironmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEnvironmentOutputTypeDef = TypedDict(
    "UpdateEnvironmentOutputTypeDef",
    {
        "environment": EnvironmentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateServiceOutputTypeDef = TypedDict(
    "CreateServiceOutputTypeDef",
    {
        "service": ServiceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteServiceOutputTypeDef = TypedDict(
    "DeleteServiceOutputTypeDef",
    {
        "service": ServiceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServiceOutputTypeDef = TypedDict(
    "GetServiceOutputTypeDef",
    {
        "service": ServiceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateServiceOutputTypeDef = TypedDict(
    "UpdateServiceOutputTypeDef",
    {
        "service": ServiceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateServiceTemplateVersionOutputTypeDef = TypedDict(
    "CreateServiceTemplateVersionOutputTypeDef",
    {
        "serviceTemplateVersion": ServiceTemplateVersionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteServiceTemplateVersionOutputTypeDef = TypedDict(
    "DeleteServiceTemplateVersionOutputTypeDef",
    {
        "serviceTemplateVersion": ServiceTemplateVersionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServiceTemplateVersionOutputTypeDef = TypedDict(
    "GetServiceTemplateVersionOutputTypeDef",
    {
        "serviceTemplateVersion": ServiceTemplateVersionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateServiceTemplateVersionOutputTypeDef = TypedDict(
    "UpdateServiceTemplateVersionOutputTypeDef",
    {
        "serviceTemplateVersion": ServiceTemplateVersionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResourcesSummaryOutputTypeDef = TypedDict(
    "GetResourcesSummaryOutputTypeDef",
    {
        "counts": CountsSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deploymentStatus": DeploymentStatusType,
        "environmentName": str,
        "id": str,
        "lastModifiedAt": datetime,
        "targetArn": str,
        "targetResourceCreatedAt": datetime,
        "targetResourceType": DeploymentTargetResourceTypeType,
        "completedAt": NotRequired[datetime],
        "componentName": NotRequired[str],
        "deploymentStatusMessage": NotRequired[str],
        "initialState": NotRequired[DeploymentStateTypeDef],
        "lastAttemptedDeploymentId": NotRequired[str],
        "lastSucceededDeploymentId": NotRequired[str],
        "serviceInstanceName": NotRequired[str],
        "serviceName": NotRequired[str],
        "targetState": NotRequired[DeploymentStateTypeDef],
    },
)
GetRepositorySyncStatusOutputTypeDef = TypedDict(
    "GetRepositorySyncStatusOutputTypeDef",
    {
        "latestSync": RepositorySyncAttemptTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServiceInstanceSyncStatusOutputTypeDef = TypedDict(
    "GetServiceInstanceSyncStatusOutputTypeDef",
    {
        "desiredState": RevisionTypeDef,
        "latestSuccessfulSync": ResourceSyncAttemptTypeDef,
        "latestSync": ResourceSyncAttemptTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTemplateSyncStatusOutputTypeDef = TypedDict(
    "GetTemplateSyncStatusOutputTypeDef",
    {
        "desiredState": RevisionTypeDef,
        "latestSuccessfulSync": ResourceSyncAttemptTypeDef,
        "latestSync": ResourceSyncAttemptTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEnvironmentTemplateVersionInputRequestTypeDef = TypedDict(
    "CreateEnvironmentTemplateVersionInputRequestTypeDef",
    {
        "source": TemplateVersionSourceInputTypeDef,
        "templateName": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "majorVersion": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateServiceTemplateVersionInputRequestTypeDef = TypedDict(
    "CreateServiceTemplateVersionInputRequestTypeDef",
    {
        "compatibleEnvironmentTemplates": Sequence[CompatibleEnvironmentTemplateInputTypeDef],
        "source": TemplateVersionSourceInputTypeDef,
        "templateName": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "majorVersion": NotRequired[str],
        "supportedComponentSources": NotRequired[Sequence[Literal["DIRECTLY_DEFINED"]]],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ServiceSyncBlockerSummaryTypeDef = TypedDict(
    "ServiceSyncBlockerSummaryTypeDef",
    {
        "serviceName": str,
        "latestBlockers": NotRequired[List[SyncBlockerTypeDef]],
        "serviceInstanceName": NotRequired[str],
    },
)
UpdateServiceSyncBlockerOutputTypeDef = TypedDict(
    "UpdateServiceSyncBlockerOutputTypeDef",
    {
        "serviceInstanceName": str,
        "serviceName": str,
        "serviceSyncBlocker": SyncBlockerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDeploymentOutputTypeDef = TypedDict(
    "DeleteDeploymentOutputTypeDef",
    {
        "deployment": DeploymentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDeploymentOutputTypeDef = TypedDict(
    "GetDeploymentOutputTypeDef",
    {
        "deployment": DeploymentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServiceSyncBlockerSummaryOutputTypeDef = TypedDict(
    "GetServiceSyncBlockerSummaryOutputTypeDef",
    {
        "serviceSyncBlockerSummary": ServiceSyncBlockerSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
