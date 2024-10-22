"""
Type annotations for imagebuilder service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/type_defs/)

Usage::

    ```python
    from mypy_boto3_imagebuilder.type_defs import SeverityCountsTypeDef

    data: SeverityCountsTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    BuildTypeType,
    ComponentTypeType,
    DiskImageFormatType,
    EbsVolumeTypeType,
    ImageScanStatusType,
    ImageSourceType,
    ImageStatusType,
    ImageTypeType,
    LifecycleExecutionResourceActionNameType,
    LifecycleExecutionResourceStatusType,
    LifecycleExecutionStatusType,
    LifecyclePolicyDetailActionTypeType,
    LifecyclePolicyDetailFilterTypeType,
    LifecyclePolicyResourceTypeType,
    LifecyclePolicyStatusType,
    LifecyclePolicyTimeUnitType,
    OnWorkflowFailureType,
    OwnershipType,
    PipelineExecutionStartConditionType,
    PipelineStatusType,
    PlatformType,
    ResourceStatusType,
    WorkflowExecutionStatusType,
    WorkflowStepActionTypeType,
    WorkflowStepExecutionRollbackStatusType,
    WorkflowStepExecutionStatusType,
    WorkflowTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "SeverityCountsTypeDef",
    "SystemsManagerAgentTypeDef",
    "LaunchPermissionConfigurationOutputTypeDef",
    "ImageStateTypeDef",
    "CancelImageCreationRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CancelLifecycleExecutionRequestRequestTypeDef",
    "ComponentParameterOutputTypeDef",
    "ComponentParameterDetailTypeDef",
    "ComponentParameterTypeDef",
    "ComponentStateTypeDef",
    "ComponentVersionTypeDef",
    "TargetContainerRepositoryTypeDef",
    "ContainerRecipeSummaryTypeDef",
    "ContainerTypeDef",
    "CreateComponentRequestRequestTypeDef",
    "ImageTestsConfigurationTypeDef",
    "ScheduleTypeDef",
    "InstanceMetadataOptionsTypeDef",
    "CreateWorkflowRequestRequestTypeDef",
    "CvssScoreAdjustmentTypeDef",
    "CvssScoreTypeDef",
    "DeleteComponentRequestRequestTypeDef",
    "DeleteContainerRecipeRequestRequestTypeDef",
    "DeleteDistributionConfigurationRequestRequestTypeDef",
    "DeleteImagePipelineRequestRequestTypeDef",
    "DeleteImageRecipeRequestRequestTypeDef",
    "DeleteImageRequestRequestTypeDef",
    "DeleteInfrastructureConfigurationRequestRequestTypeDef",
    "DeleteLifecyclePolicyRequestRequestTypeDef",
    "DeleteWorkflowRequestRequestTypeDef",
    "DistributionConfigurationSummaryTypeDef",
    "LaunchTemplateConfigurationTypeDef",
    "S3ExportConfigurationTypeDef",
    "EbsInstanceBlockDeviceSpecificationTypeDef",
    "EcrConfigurationOutputTypeDef",
    "EcrConfigurationTypeDef",
    "FastLaunchLaunchTemplateSpecificationTypeDef",
    "FastLaunchSnapshotConfigurationTypeDef",
    "FilterTypeDef",
    "GetComponentPolicyRequestRequestTypeDef",
    "GetComponentRequestRequestTypeDef",
    "GetContainerRecipePolicyRequestRequestTypeDef",
    "GetContainerRecipeRequestRequestTypeDef",
    "GetDistributionConfigurationRequestRequestTypeDef",
    "GetImagePipelineRequestRequestTypeDef",
    "GetImagePolicyRequestRequestTypeDef",
    "GetImageRecipePolicyRequestRequestTypeDef",
    "GetImageRecipeRequestRequestTypeDef",
    "GetImageRequestRequestTypeDef",
    "GetInfrastructureConfigurationRequestRequestTypeDef",
    "GetLifecycleExecutionRequestRequestTypeDef",
    "GetLifecyclePolicyRequestRequestTypeDef",
    "GetWorkflowExecutionRequestRequestTypeDef",
    "GetWorkflowRequestRequestTypeDef",
    "GetWorkflowStepExecutionRequestRequestTypeDef",
    "ImagePackageTypeDef",
    "ImageRecipeSummaryTypeDef",
    "ImageScanFindingsFilterTypeDef",
    "ImageScanStateTypeDef",
    "ImageVersionTypeDef",
    "ImportComponentRequestRequestTypeDef",
    "ImportVmImageRequestRequestTypeDef",
    "InfrastructureConfigurationSummaryTypeDef",
    "LaunchPermissionConfigurationTypeDef",
    "LifecycleExecutionResourceActionTypeDef",
    "LifecycleExecutionResourceStateTypeDef",
    "LifecycleExecutionResourcesImpactedSummaryTypeDef",
    "LifecycleExecutionStateTypeDef",
    "LifecyclePolicyDetailActionIncludeResourcesTypeDef",
    "LifecyclePolicyDetailExclusionRulesAmisLastLaunchedTypeDef",
    "LifecyclePolicyDetailFilterTypeDef",
    "LifecyclePolicyResourceSelectionRecipeTypeDef",
    "LifecyclePolicySummaryTypeDef",
    "ListComponentBuildVersionsRequestRequestTypeDef",
    "ListImagePackagesRequestRequestTypeDef",
    "ListLifecycleExecutionResourcesRequestRequestTypeDef",
    "ListLifecycleExecutionsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListWaitingWorkflowStepsRequestRequestTypeDef",
    "WorkflowStepExecutionTypeDef",
    "ListWorkflowBuildVersionsRequestRequestTypeDef",
    "ListWorkflowExecutionsRequestRequestTypeDef",
    "WorkflowExecutionMetadataTypeDef",
    "ListWorkflowStepExecutionsRequestRequestTypeDef",
    "WorkflowStepMetadataTypeDef",
    "WorkflowVersionTypeDef",
    "S3LogsTypeDef",
    "VulnerablePackageTypeDef",
    "PutComponentPolicyRequestRequestTypeDef",
    "PutContainerRecipePolicyRequestRequestTypeDef",
    "PutImagePolicyRequestRequestTypeDef",
    "PutImageRecipePolicyRequestRequestTypeDef",
    "RemediationRecommendationTypeDef",
    "ResourceStateTypeDef",
    "ResourceStateUpdateIncludeResourcesTypeDef",
    "SendWorkflowStepActionRequestRequestTypeDef",
    "StartImagePipelineExecutionRequestRequestTypeDef",
    "TimestampTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "WorkflowParameterOutputTypeDef",
    "WorkflowParameterDetailTypeDef",
    "WorkflowParameterTypeDef",
    "WorkflowStateTypeDef",
    "AccountAggregationTypeDef",
    "ImageAggregationTypeDef",
    "ImagePipelineAggregationTypeDef",
    "VulnerabilityIdAggregationTypeDef",
    "AdditionalInstanceConfigurationTypeDef",
    "AmiDistributionConfigurationOutputTypeDef",
    "AmiTypeDef",
    "CancelImageCreationResponseTypeDef",
    "CancelLifecycleExecutionResponseTypeDef",
    "CreateComponentResponseTypeDef",
    "CreateContainerRecipeResponseTypeDef",
    "CreateDistributionConfigurationResponseTypeDef",
    "CreateImagePipelineResponseTypeDef",
    "CreateImageRecipeResponseTypeDef",
    "CreateImageResponseTypeDef",
    "CreateInfrastructureConfigurationResponseTypeDef",
    "CreateLifecyclePolicyResponseTypeDef",
    "CreateWorkflowResponseTypeDef",
    "DeleteComponentResponseTypeDef",
    "DeleteContainerRecipeResponseTypeDef",
    "DeleteDistributionConfigurationResponseTypeDef",
    "DeleteImagePipelineResponseTypeDef",
    "DeleteImageRecipeResponseTypeDef",
    "DeleteImageResponseTypeDef",
    "DeleteInfrastructureConfigurationResponseTypeDef",
    "DeleteLifecyclePolicyResponseTypeDef",
    "DeleteWorkflowResponseTypeDef",
    "GetComponentPolicyResponseTypeDef",
    "GetContainerRecipePolicyResponseTypeDef",
    "GetImagePolicyResponseTypeDef",
    "GetImageRecipePolicyResponseTypeDef",
    "GetWorkflowExecutionResponseTypeDef",
    "GetWorkflowStepExecutionResponseTypeDef",
    "ImportComponentResponseTypeDef",
    "ImportVmImageResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PutComponentPolicyResponseTypeDef",
    "PutContainerRecipePolicyResponseTypeDef",
    "PutImagePolicyResponseTypeDef",
    "PutImageRecipePolicyResponseTypeDef",
    "SendWorkflowStepActionResponseTypeDef",
    "StartImagePipelineExecutionResponseTypeDef",
    "StartResourceStateUpdateResponseTypeDef",
    "UpdateDistributionConfigurationResponseTypeDef",
    "UpdateImagePipelineResponseTypeDef",
    "UpdateInfrastructureConfigurationResponseTypeDef",
    "UpdateLifecyclePolicyResponseTypeDef",
    "ComponentConfigurationOutputTypeDef",
    "ComponentParameterUnionTypeDef",
    "ComponentSummaryTypeDef",
    "ComponentTypeDef",
    "ListComponentsResponseTypeDef",
    "ContainerDistributionConfigurationOutputTypeDef",
    "ContainerDistributionConfigurationTypeDef",
    "ListContainerRecipesResponseTypeDef",
    "CvssScoreDetailsTypeDef",
    "ListDistributionConfigurationsResponseTypeDef",
    "InstanceBlockDeviceMappingTypeDef",
    "ImageScanningConfigurationOutputTypeDef",
    "EcrConfigurationUnionTypeDef",
    "FastLaunchConfigurationTypeDef",
    "ListComponentsRequestRequestTypeDef",
    "ListContainerRecipesRequestRequestTypeDef",
    "ListDistributionConfigurationsRequestRequestTypeDef",
    "ListImageBuildVersionsRequestRequestTypeDef",
    "ListImagePipelineImagesRequestRequestTypeDef",
    "ListImagePipelinesRequestRequestTypeDef",
    "ListImageRecipesRequestRequestTypeDef",
    "ListImageScanFindingAggregationsRequestRequestTypeDef",
    "ListImagesRequestRequestTypeDef",
    "ListInfrastructureConfigurationsRequestRequestTypeDef",
    "ListLifecyclePoliciesRequestRequestTypeDef",
    "ListWorkflowsRequestRequestTypeDef",
    "ListImagePackagesResponseTypeDef",
    "ListImageRecipesResponseTypeDef",
    "ListImageScanFindingsRequestRequestTypeDef",
    "ListImagesResponseTypeDef",
    "ListInfrastructureConfigurationsResponseTypeDef",
    "LaunchPermissionConfigurationUnionTypeDef",
    "LifecycleExecutionSnapshotResourceTypeDef",
    "LifecycleExecutionTypeDef",
    "LifecyclePolicyDetailActionTypeDef",
    "LifecyclePolicyDetailExclusionRulesAmisOutputTypeDef",
    "LifecyclePolicyDetailExclusionRulesAmisTypeDef",
    "LifecyclePolicyResourceSelectionOutputTypeDef",
    "LifecyclePolicyResourceSelectionTypeDef",
    "ListLifecyclePoliciesResponseTypeDef",
    "ListWaitingWorkflowStepsResponseTypeDef",
    "ListWorkflowExecutionsResponseTypeDef",
    "ListWorkflowStepExecutionsResponseTypeDef",
    "ListWorkflowsResponseTypeDef",
    "LoggingTypeDef",
    "PackageVulnerabilityDetailsTypeDef",
    "RemediationTypeDef",
    "WorkflowConfigurationOutputTypeDef",
    "WorkflowParameterUnionTypeDef",
    "WorkflowSummaryTypeDef",
    "WorkflowTypeDef",
    "ImageScanFindingAggregationTypeDef",
    "OutputResourcesTypeDef",
    "ComponentConfigurationTypeDef",
    "ListComponentBuildVersionsResponseTypeDef",
    "GetComponentResponseTypeDef",
    "ContainerDistributionConfigurationUnionTypeDef",
    "InspectorScoreDetailsTypeDef",
    "ImageRecipeTypeDef",
    "InstanceConfigurationOutputTypeDef",
    "InstanceConfigurationTypeDef",
    "ImageScanningConfigurationTypeDef",
    "DistributionOutputTypeDef",
    "AmiDistributionConfigurationTypeDef",
    "LifecycleExecutionResourceTypeDef",
    "GetLifecycleExecutionResponseTypeDef",
    "ListLifecycleExecutionsResponseTypeDef",
    "LifecyclePolicyDetailExclusionRulesOutputTypeDef",
    "LifecyclePolicyDetailExclusionRulesAmisUnionTypeDef",
    "CreateInfrastructureConfigurationRequestRequestTypeDef",
    "InfrastructureConfigurationTypeDef",
    "UpdateInfrastructureConfigurationRequestRequestTypeDef",
    "ImagePipelineTypeDef",
    "WorkflowConfigurationTypeDef",
    "ListWorkflowBuildVersionsResponseTypeDef",
    "GetWorkflowResponseTypeDef",
    "ListImageScanFindingAggregationsResponseTypeDef",
    "ImageSummaryTypeDef",
    "ComponentConfigurationUnionTypeDef",
    "CreateImageRecipeRequestRequestTypeDef",
    "ImageScanFindingTypeDef",
    "GetImageRecipeResponseTypeDef",
    "ContainerRecipeTypeDef",
    "DistributionConfigurationTypeDef",
    "AmiDistributionConfigurationUnionTypeDef",
    "ListLifecycleExecutionResourcesResponseTypeDef",
    "LifecyclePolicyDetailOutputTypeDef",
    "LifecyclePolicyDetailExclusionRulesTypeDef",
    "ResourceStateUpdateExclusionRulesTypeDef",
    "GetInfrastructureConfigurationResponseTypeDef",
    "GetImagePipelineResponseTypeDef",
    "ListImagePipelinesResponseTypeDef",
    "CreateImagePipelineRequestRequestTypeDef",
    "UpdateImagePipelineRequestRequestTypeDef",
    "WorkflowConfigurationUnionTypeDef",
    "ListImageBuildVersionsResponseTypeDef",
    "ListImagePipelineImagesResponseTypeDef",
    "CreateContainerRecipeRequestRequestTypeDef",
    "ListImageScanFindingsResponseTypeDef",
    "GetContainerRecipeResponseTypeDef",
    "GetDistributionConfigurationResponseTypeDef",
    "ImageTypeDef",
    "DistributionTypeDef",
    "LifecyclePolicyTypeDef",
    "LifecyclePolicyDetailExclusionRulesUnionTypeDef",
    "StartResourceStateUpdateRequestRequestTypeDef",
    "CreateImageRequestRequestTypeDef",
    "GetImageResponseTypeDef",
    "DistributionUnionTypeDef",
    "UpdateDistributionConfigurationRequestRequestTypeDef",
    "GetLifecyclePolicyResponseTypeDef",
    "LifecyclePolicyDetailTypeDef",
    "CreateDistributionConfigurationRequestRequestTypeDef",
    "LifecyclePolicyDetailUnionTypeDef",
    "UpdateLifecyclePolicyRequestRequestTypeDef",
    "CreateLifecyclePolicyRequestRequestTypeDef",
)

SeverityCountsTypeDef = TypedDict(
    "SeverityCountsTypeDef",
    {
        "all": NotRequired[int],
        "critical": NotRequired[int],
        "high": NotRequired[int],
        "medium": NotRequired[int],
    },
)
SystemsManagerAgentTypeDef = TypedDict(
    "SystemsManagerAgentTypeDef",
    {
        "uninstallAfterBuild": NotRequired[bool],
    },
)
LaunchPermissionConfigurationOutputTypeDef = TypedDict(
    "LaunchPermissionConfigurationOutputTypeDef",
    {
        "userIds": NotRequired[List[str]],
        "userGroups": NotRequired[List[str]],
        "organizationArns": NotRequired[List[str]],
        "organizationalUnitArns": NotRequired[List[str]],
    },
)
ImageStateTypeDef = TypedDict(
    "ImageStateTypeDef",
    {
        "status": NotRequired[ImageStatusType],
        "reason": NotRequired[str],
    },
)
CancelImageCreationRequestRequestTypeDef = TypedDict(
    "CancelImageCreationRequestRequestTypeDef",
    {
        "imageBuildVersionArn": str,
        "clientToken": str,
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
CancelLifecycleExecutionRequestRequestTypeDef = TypedDict(
    "CancelLifecycleExecutionRequestRequestTypeDef",
    {
        "lifecycleExecutionId": str,
        "clientToken": str,
    },
)
ComponentParameterOutputTypeDef = TypedDict(
    "ComponentParameterOutputTypeDef",
    {
        "name": str,
        "value": List[str],
    },
)
ComponentParameterDetailTypeDef = TypedDict(
    "ComponentParameterDetailTypeDef",
    {
        "name": str,
        "type": str,
        "defaultValue": NotRequired[List[str]],
        "description": NotRequired[str],
    },
)
ComponentParameterTypeDef = TypedDict(
    "ComponentParameterTypeDef",
    {
        "name": str,
        "value": Sequence[str],
    },
)
ComponentStateTypeDef = TypedDict(
    "ComponentStateTypeDef",
    {
        "status": NotRequired[Literal["DEPRECATED"]],
        "reason": NotRequired[str],
    },
)
ComponentVersionTypeDef = TypedDict(
    "ComponentVersionTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "version": NotRequired[str],
        "description": NotRequired[str],
        "platform": NotRequired[PlatformType],
        "supportedOsVersions": NotRequired[List[str]],
        "type": NotRequired[ComponentTypeType],
        "owner": NotRequired[str],
        "dateCreated": NotRequired[str],
    },
)
TargetContainerRepositoryTypeDef = TypedDict(
    "TargetContainerRepositoryTypeDef",
    {
        "service": Literal["ECR"],
        "repositoryName": str,
    },
)
ContainerRecipeSummaryTypeDef = TypedDict(
    "ContainerRecipeSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "containerType": NotRequired[Literal["DOCKER"]],
        "name": NotRequired[str],
        "platform": NotRequired[PlatformType],
        "owner": NotRequired[str],
        "parentImage": NotRequired[str],
        "dateCreated": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)
ContainerTypeDef = TypedDict(
    "ContainerTypeDef",
    {
        "region": NotRequired[str],
        "imageUris": NotRequired[List[str]],
    },
)
CreateComponentRequestRequestTypeDef = TypedDict(
    "CreateComponentRequestRequestTypeDef",
    {
        "name": str,
        "semanticVersion": str,
        "platform": PlatformType,
        "clientToken": str,
        "description": NotRequired[str],
        "changeDescription": NotRequired[str],
        "supportedOsVersions": NotRequired[Sequence[str]],
        "data": NotRequired[str],
        "uri": NotRequired[str],
        "kmsKeyId": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
ImageTestsConfigurationTypeDef = TypedDict(
    "ImageTestsConfigurationTypeDef",
    {
        "imageTestsEnabled": NotRequired[bool],
        "timeoutMinutes": NotRequired[int],
    },
)
ScheduleTypeDef = TypedDict(
    "ScheduleTypeDef",
    {
        "scheduleExpression": NotRequired[str],
        "timezone": NotRequired[str],
        "pipelineExecutionStartCondition": NotRequired[PipelineExecutionStartConditionType],
    },
)
InstanceMetadataOptionsTypeDef = TypedDict(
    "InstanceMetadataOptionsTypeDef",
    {
        "httpTokens": NotRequired[str],
        "httpPutResponseHopLimit": NotRequired[int],
    },
)
CreateWorkflowRequestRequestTypeDef = TypedDict(
    "CreateWorkflowRequestRequestTypeDef",
    {
        "name": str,
        "semanticVersion": str,
        "clientToken": str,
        "type": WorkflowTypeType,
        "description": NotRequired[str],
        "changeDescription": NotRequired[str],
        "data": NotRequired[str],
        "uri": NotRequired[str],
        "kmsKeyId": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CvssScoreAdjustmentTypeDef = TypedDict(
    "CvssScoreAdjustmentTypeDef",
    {
        "metric": NotRequired[str],
        "reason": NotRequired[str],
    },
)
CvssScoreTypeDef = TypedDict(
    "CvssScoreTypeDef",
    {
        "baseScore": NotRequired[float],
        "scoringVector": NotRequired[str],
        "version": NotRequired[str],
        "source": NotRequired[str],
    },
)
DeleteComponentRequestRequestTypeDef = TypedDict(
    "DeleteComponentRequestRequestTypeDef",
    {
        "componentBuildVersionArn": str,
    },
)
DeleteContainerRecipeRequestRequestTypeDef = TypedDict(
    "DeleteContainerRecipeRequestRequestTypeDef",
    {
        "containerRecipeArn": str,
    },
)
DeleteDistributionConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteDistributionConfigurationRequestRequestTypeDef",
    {
        "distributionConfigurationArn": str,
    },
)
DeleteImagePipelineRequestRequestTypeDef = TypedDict(
    "DeleteImagePipelineRequestRequestTypeDef",
    {
        "imagePipelineArn": str,
    },
)
DeleteImageRecipeRequestRequestTypeDef = TypedDict(
    "DeleteImageRecipeRequestRequestTypeDef",
    {
        "imageRecipeArn": str,
    },
)
DeleteImageRequestRequestTypeDef = TypedDict(
    "DeleteImageRequestRequestTypeDef",
    {
        "imageBuildVersionArn": str,
    },
)
DeleteInfrastructureConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteInfrastructureConfigurationRequestRequestTypeDef",
    {
        "infrastructureConfigurationArn": str,
    },
)
DeleteLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "DeleteLifecyclePolicyRequestRequestTypeDef",
    {
        "lifecyclePolicyArn": str,
    },
)
DeleteWorkflowRequestRequestTypeDef = TypedDict(
    "DeleteWorkflowRequestRequestTypeDef",
    {
        "workflowBuildVersionArn": str,
    },
)
DistributionConfigurationSummaryTypeDef = TypedDict(
    "DistributionConfigurationSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "dateCreated": NotRequired[str],
        "dateUpdated": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "regions": NotRequired[List[str]],
    },
)
LaunchTemplateConfigurationTypeDef = TypedDict(
    "LaunchTemplateConfigurationTypeDef",
    {
        "launchTemplateId": str,
        "accountId": NotRequired[str],
        "setDefaultVersion": NotRequired[bool],
    },
)
S3ExportConfigurationTypeDef = TypedDict(
    "S3ExportConfigurationTypeDef",
    {
        "roleName": str,
        "diskImageFormat": DiskImageFormatType,
        "s3Bucket": str,
        "s3Prefix": NotRequired[str],
    },
)
EbsInstanceBlockDeviceSpecificationTypeDef = TypedDict(
    "EbsInstanceBlockDeviceSpecificationTypeDef",
    {
        "encrypted": NotRequired[bool],
        "deleteOnTermination": NotRequired[bool],
        "iops": NotRequired[int],
        "kmsKeyId": NotRequired[str],
        "snapshotId": NotRequired[str],
        "volumeSize": NotRequired[int],
        "volumeType": NotRequired[EbsVolumeTypeType],
        "throughput": NotRequired[int],
    },
)
EcrConfigurationOutputTypeDef = TypedDict(
    "EcrConfigurationOutputTypeDef",
    {
        "repositoryName": NotRequired[str],
        "containerTags": NotRequired[List[str]],
    },
)
EcrConfigurationTypeDef = TypedDict(
    "EcrConfigurationTypeDef",
    {
        "repositoryName": NotRequired[str],
        "containerTags": NotRequired[Sequence[str]],
    },
)
FastLaunchLaunchTemplateSpecificationTypeDef = TypedDict(
    "FastLaunchLaunchTemplateSpecificationTypeDef",
    {
        "launchTemplateId": NotRequired[str],
        "launchTemplateName": NotRequired[str],
        "launchTemplateVersion": NotRequired[str],
    },
)
FastLaunchSnapshotConfigurationTypeDef = TypedDict(
    "FastLaunchSnapshotConfigurationTypeDef",
    {
        "targetResourceCount": NotRequired[int],
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "name": NotRequired[str],
        "values": NotRequired[Sequence[str]],
    },
)
GetComponentPolicyRequestRequestTypeDef = TypedDict(
    "GetComponentPolicyRequestRequestTypeDef",
    {
        "componentArn": str,
    },
)
GetComponentRequestRequestTypeDef = TypedDict(
    "GetComponentRequestRequestTypeDef",
    {
        "componentBuildVersionArn": str,
    },
)
GetContainerRecipePolicyRequestRequestTypeDef = TypedDict(
    "GetContainerRecipePolicyRequestRequestTypeDef",
    {
        "containerRecipeArn": str,
    },
)
GetContainerRecipeRequestRequestTypeDef = TypedDict(
    "GetContainerRecipeRequestRequestTypeDef",
    {
        "containerRecipeArn": str,
    },
)
GetDistributionConfigurationRequestRequestTypeDef = TypedDict(
    "GetDistributionConfigurationRequestRequestTypeDef",
    {
        "distributionConfigurationArn": str,
    },
)
GetImagePipelineRequestRequestTypeDef = TypedDict(
    "GetImagePipelineRequestRequestTypeDef",
    {
        "imagePipelineArn": str,
    },
)
GetImagePolicyRequestRequestTypeDef = TypedDict(
    "GetImagePolicyRequestRequestTypeDef",
    {
        "imageArn": str,
    },
)
GetImageRecipePolicyRequestRequestTypeDef = TypedDict(
    "GetImageRecipePolicyRequestRequestTypeDef",
    {
        "imageRecipeArn": str,
    },
)
GetImageRecipeRequestRequestTypeDef = TypedDict(
    "GetImageRecipeRequestRequestTypeDef",
    {
        "imageRecipeArn": str,
    },
)
GetImageRequestRequestTypeDef = TypedDict(
    "GetImageRequestRequestTypeDef",
    {
        "imageBuildVersionArn": str,
    },
)
GetInfrastructureConfigurationRequestRequestTypeDef = TypedDict(
    "GetInfrastructureConfigurationRequestRequestTypeDef",
    {
        "infrastructureConfigurationArn": str,
    },
)
GetLifecycleExecutionRequestRequestTypeDef = TypedDict(
    "GetLifecycleExecutionRequestRequestTypeDef",
    {
        "lifecycleExecutionId": str,
    },
)
GetLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "GetLifecyclePolicyRequestRequestTypeDef",
    {
        "lifecyclePolicyArn": str,
    },
)
GetWorkflowExecutionRequestRequestTypeDef = TypedDict(
    "GetWorkflowExecutionRequestRequestTypeDef",
    {
        "workflowExecutionId": str,
    },
)
GetWorkflowRequestRequestTypeDef = TypedDict(
    "GetWorkflowRequestRequestTypeDef",
    {
        "workflowBuildVersionArn": str,
    },
)
GetWorkflowStepExecutionRequestRequestTypeDef = TypedDict(
    "GetWorkflowStepExecutionRequestRequestTypeDef",
    {
        "stepExecutionId": str,
    },
)
ImagePackageTypeDef = TypedDict(
    "ImagePackageTypeDef",
    {
        "packageName": NotRequired[str],
        "packageVersion": NotRequired[str],
    },
)
ImageRecipeSummaryTypeDef = TypedDict(
    "ImageRecipeSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "platform": NotRequired[PlatformType],
        "owner": NotRequired[str],
        "parentImage": NotRequired[str],
        "dateCreated": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)
ImageScanFindingsFilterTypeDef = TypedDict(
    "ImageScanFindingsFilterTypeDef",
    {
        "name": NotRequired[str],
        "values": NotRequired[Sequence[str]],
    },
)
ImageScanStateTypeDef = TypedDict(
    "ImageScanStateTypeDef",
    {
        "status": NotRequired[ImageScanStatusType],
        "reason": NotRequired[str],
    },
)
ImageVersionTypeDef = TypedDict(
    "ImageVersionTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[ImageTypeType],
        "version": NotRequired[str],
        "platform": NotRequired[PlatformType],
        "osVersion": NotRequired[str],
        "owner": NotRequired[str],
        "dateCreated": NotRequired[str],
        "buildType": NotRequired[BuildTypeType],
        "imageSource": NotRequired[ImageSourceType],
    },
)
ImportComponentRequestRequestTypeDef = TypedDict(
    "ImportComponentRequestRequestTypeDef",
    {
        "name": str,
        "semanticVersion": str,
        "type": ComponentTypeType,
        "format": Literal["SHELL"],
        "platform": PlatformType,
        "clientToken": str,
        "description": NotRequired[str],
        "changeDescription": NotRequired[str],
        "data": NotRequired[str],
        "uri": NotRequired[str],
        "kmsKeyId": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
ImportVmImageRequestRequestTypeDef = TypedDict(
    "ImportVmImageRequestRequestTypeDef",
    {
        "name": str,
        "semanticVersion": str,
        "platform": PlatformType,
        "vmImportTaskId": str,
        "clientToken": str,
        "description": NotRequired[str],
        "osVersion": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
InfrastructureConfigurationSummaryTypeDef = TypedDict(
    "InfrastructureConfigurationSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "dateCreated": NotRequired[str],
        "dateUpdated": NotRequired[str],
        "resourceTags": NotRequired[Dict[str, str]],
        "tags": NotRequired[Dict[str, str]],
        "instanceTypes": NotRequired[List[str]],
        "instanceProfileName": NotRequired[str],
    },
)
LaunchPermissionConfigurationTypeDef = TypedDict(
    "LaunchPermissionConfigurationTypeDef",
    {
        "userIds": NotRequired[Sequence[str]],
        "userGroups": NotRequired[Sequence[str]],
        "organizationArns": NotRequired[Sequence[str]],
        "organizationalUnitArns": NotRequired[Sequence[str]],
    },
)
LifecycleExecutionResourceActionTypeDef = TypedDict(
    "LifecycleExecutionResourceActionTypeDef",
    {
        "name": NotRequired[LifecycleExecutionResourceActionNameType],
        "reason": NotRequired[str],
    },
)
LifecycleExecutionResourceStateTypeDef = TypedDict(
    "LifecycleExecutionResourceStateTypeDef",
    {
        "status": NotRequired[LifecycleExecutionResourceStatusType],
        "reason": NotRequired[str],
    },
)
LifecycleExecutionResourcesImpactedSummaryTypeDef = TypedDict(
    "LifecycleExecutionResourcesImpactedSummaryTypeDef",
    {
        "hasImpactedResources": NotRequired[bool],
    },
)
LifecycleExecutionStateTypeDef = TypedDict(
    "LifecycleExecutionStateTypeDef",
    {
        "status": NotRequired[LifecycleExecutionStatusType],
        "reason": NotRequired[str],
    },
)
LifecyclePolicyDetailActionIncludeResourcesTypeDef = TypedDict(
    "LifecyclePolicyDetailActionIncludeResourcesTypeDef",
    {
        "amis": NotRequired[bool],
        "snapshots": NotRequired[bool],
        "containers": NotRequired[bool],
    },
)
LifecyclePolicyDetailExclusionRulesAmisLastLaunchedTypeDef = TypedDict(
    "LifecyclePolicyDetailExclusionRulesAmisLastLaunchedTypeDef",
    {
        "value": int,
        "unit": LifecyclePolicyTimeUnitType,
    },
)
LifecyclePolicyDetailFilterTypeDef = TypedDict(
    "LifecyclePolicyDetailFilterTypeDef",
    {
        "type": LifecyclePolicyDetailFilterTypeType,
        "value": int,
        "unit": NotRequired[LifecyclePolicyTimeUnitType],
        "retainAtLeast": NotRequired[int],
    },
)
LifecyclePolicyResourceSelectionRecipeTypeDef = TypedDict(
    "LifecyclePolicyResourceSelectionRecipeTypeDef",
    {
        "name": str,
        "semanticVersion": str,
    },
)
LifecyclePolicySummaryTypeDef = TypedDict(
    "LifecyclePolicySummaryTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "status": NotRequired[LifecyclePolicyStatusType],
        "executionRole": NotRequired[str],
        "resourceType": NotRequired[LifecyclePolicyResourceTypeType],
        "dateCreated": NotRequired[datetime],
        "dateUpdated": NotRequired[datetime],
        "dateLastRun": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
    },
)
ListComponentBuildVersionsRequestRequestTypeDef = TypedDict(
    "ListComponentBuildVersionsRequestRequestTypeDef",
    {
        "componentVersionArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListImagePackagesRequestRequestTypeDef = TypedDict(
    "ListImagePackagesRequestRequestTypeDef",
    {
        "imageBuildVersionArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListLifecycleExecutionResourcesRequestRequestTypeDef = TypedDict(
    "ListLifecycleExecutionResourcesRequestRequestTypeDef",
    {
        "lifecycleExecutionId": str,
        "parentResourceId": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListLifecycleExecutionsRequestRequestTypeDef = TypedDict(
    "ListLifecycleExecutionsRequestRequestTypeDef",
    {
        "resourceArn": str,
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
ListWaitingWorkflowStepsRequestRequestTypeDef = TypedDict(
    "ListWaitingWorkflowStepsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
WorkflowStepExecutionTypeDef = TypedDict(
    "WorkflowStepExecutionTypeDef",
    {
        "stepExecutionId": NotRequired[str],
        "imageBuildVersionArn": NotRequired[str],
        "workflowExecutionId": NotRequired[str],
        "workflowBuildVersionArn": NotRequired[str],
        "name": NotRequired[str],
        "action": NotRequired[str],
        "startTime": NotRequired[str],
    },
)
ListWorkflowBuildVersionsRequestRequestTypeDef = TypedDict(
    "ListWorkflowBuildVersionsRequestRequestTypeDef",
    {
        "workflowVersionArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListWorkflowExecutionsRequestRequestTypeDef = TypedDict(
    "ListWorkflowExecutionsRequestRequestTypeDef",
    {
        "imageBuildVersionArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
WorkflowExecutionMetadataTypeDef = TypedDict(
    "WorkflowExecutionMetadataTypeDef",
    {
        "workflowBuildVersionArn": NotRequired[str],
        "workflowExecutionId": NotRequired[str],
        "type": NotRequired[WorkflowTypeType],
        "status": NotRequired[WorkflowExecutionStatusType],
        "message": NotRequired[str],
        "totalStepCount": NotRequired[int],
        "totalStepsSucceeded": NotRequired[int],
        "totalStepsFailed": NotRequired[int],
        "totalStepsSkipped": NotRequired[int],
        "startTime": NotRequired[str],
        "endTime": NotRequired[str],
        "parallelGroup": NotRequired[str],
    },
)
ListWorkflowStepExecutionsRequestRequestTypeDef = TypedDict(
    "ListWorkflowStepExecutionsRequestRequestTypeDef",
    {
        "workflowExecutionId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
WorkflowStepMetadataTypeDef = TypedDict(
    "WorkflowStepMetadataTypeDef",
    {
        "stepExecutionId": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "action": NotRequired[str],
        "status": NotRequired[WorkflowStepExecutionStatusType],
        "rollbackStatus": NotRequired[WorkflowStepExecutionRollbackStatusType],
        "message": NotRequired[str],
        "inputs": NotRequired[str],
        "outputs": NotRequired[str],
        "startTime": NotRequired[str],
        "endTime": NotRequired[str],
    },
)
WorkflowVersionTypeDef = TypedDict(
    "WorkflowVersionTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "version": NotRequired[str],
        "description": NotRequired[str],
        "type": NotRequired[WorkflowTypeType],
        "owner": NotRequired[str],
        "dateCreated": NotRequired[str],
    },
)
S3LogsTypeDef = TypedDict(
    "S3LogsTypeDef",
    {
        "s3BucketName": NotRequired[str],
        "s3KeyPrefix": NotRequired[str],
    },
)
VulnerablePackageTypeDef = TypedDict(
    "VulnerablePackageTypeDef",
    {
        "name": NotRequired[str],
        "version": NotRequired[str],
        "sourceLayerHash": NotRequired[str],
        "epoch": NotRequired[int],
        "release": NotRequired[str],
        "arch": NotRequired[str],
        "packageManager": NotRequired[str],
        "filePath": NotRequired[str],
        "fixedInVersion": NotRequired[str],
        "remediation": NotRequired[str],
    },
)
PutComponentPolicyRequestRequestTypeDef = TypedDict(
    "PutComponentPolicyRequestRequestTypeDef",
    {
        "componentArn": str,
        "policy": str,
    },
)
PutContainerRecipePolicyRequestRequestTypeDef = TypedDict(
    "PutContainerRecipePolicyRequestRequestTypeDef",
    {
        "containerRecipeArn": str,
        "policy": str,
    },
)
PutImagePolicyRequestRequestTypeDef = TypedDict(
    "PutImagePolicyRequestRequestTypeDef",
    {
        "imageArn": str,
        "policy": str,
    },
)
PutImageRecipePolicyRequestRequestTypeDef = TypedDict(
    "PutImageRecipePolicyRequestRequestTypeDef",
    {
        "imageRecipeArn": str,
        "policy": str,
    },
)
RemediationRecommendationTypeDef = TypedDict(
    "RemediationRecommendationTypeDef",
    {
        "text": NotRequired[str],
        "url": NotRequired[str],
    },
)
ResourceStateTypeDef = TypedDict(
    "ResourceStateTypeDef",
    {
        "status": NotRequired[ResourceStatusType],
    },
)
ResourceStateUpdateIncludeResourcesTypeDef = TypedDict(
    "ResourceStateUpdateIncludeResourcesTypeDef",
    {
        "amis": NotRequired[bool],
        "snapshots": NotRequired[bool],
        "containers": NotRequired[bool],
    },
)
SendWorkflowStepActionRequestRequestTypeDef = TypedDict(
    "SendWorkflowStepActionRequestRequestTypeDef",
    {
        "stepExecutionId": str,
        "imageBuildVersionArn": str,
        "action": WorkflowStepActionTypeType,
        "clientToken": str,
        "reason": NotRequired[str],
    },
)
StartImagePipelineExecutionRequestRequestTypeDef = TypedDict(
    "StartImagePipelineExecutionRequestRequestTypeDef",
    {
        "imagePipelineArn": str,
        "clientToken": str,
    },
)
TimestampTypeDef = Union[datetime, str]
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
WorkflowParameterOutputTypeDef = TypedDict(
    "WorkflowParameterOutputTypeDef",
    {
        "name": str,
        "value": List[str],
    },
)
WorkflowParameterDetailTypeDef = TypedDict(
    "WorkflowParameterDetailTypeDef",
    {
        "name": str,
        "type": str,
        "defaultValue": NotRequired[List[str]],
        "description": NotRequired[str],
    },
)
WorkflowParameterTypeDef = TypedDict(
    "WorkflowParameterTypeDef",
    {
        "name": str,
        "value": Sequence[str],
    },
)
WorkflowStateTypeDef = TypedDict(
    "WorkflowStateTypeDef",
    {
        "status": NotRequired[Literal["DEPRECATED"]],
        "reason": NotRequired[str],
    },
)
AccountAggregationTypeDef = TypedDict(
    "AccountAggregationTypeDef",
    {
        "accountId": NotRequired[str],
        "severityCounts": NotRequired[SeverityCountsTypeDef],
    },
)
ImageAggregationTypeDef = TypedDict(
    "ImageAggregationTypeDef",
    {
        "imageBuildVersionArn": NotRequired[str],
        "severityCounts": NotRequired[SeverityCountsTypeDef],
    },
)
ImagePipelineAggregationTypeDef = TypedDict(
    "ImagePipelineAggregationTypeDef",
    {
        "imagePipelineArn": NotRequired[str],
        "severityCounts": NotRequired[SeverityCountsTypeDef],
    },
)
VulnerabilityIdAggregationTypeDef = TypedDict(
    "VulnerabilityIdAggregationTypeDef",
    {
        "vulnerabilityId": NotRequired[str],
        "severityCounts": NotRequired[SeverityCountsTypeDef],
    },
)
AdditionalInstanceConfigurationTypeDef = TypedDict(
    "AdditionalInstanceConfigurationTypeDef",
    {
        "systemsManagerAgent": NotRequired[SystemsManagerAgentTypeDef],
        "userDataOverride": NotRequired[str],
    },
)
AmiDistributionConfigurationOutputTypeDef = TypedDict(
    "AmiDistributionConfigurationOutputTypeDef",
    {
        "name": NotRequired[str],
        "description": NotRequired[str],
        "targetAccountIds": NotRequired[List[str]],
        "amiTags": NotRequired[Dict[str, str]],
        "kmsKeyId": NotRequired[str],
        "launchPermission": NotRequired[LaunchPermissionConfigurationOutputTypeDef],
    },
)
AmiTypeDef = TypedDict(
    "AmiTypeDef",
    {
        "region": NotRequired[str],
        "image": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "state": NotRequired[ImageStateTypeDef],
        "accountId": NotRequired[str],
    },
)
CancelImageCreationResponseTypeDef = TypedDict(
    "CancelImageCreationResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "imageBuildVersionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CancelLifecycleExecutionResponseTypeDef = TypedDict(
    "CancelLifecycleExecutionResponseTypeDef",
    {
        "lifecycleExecutionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateComponentResponseTypeDef = TypedDict(
    "CreateComponentResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "componentBuildVersionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateContainerRecipeResponseTypeDef = TypedDict(
    "CreateContainerRecipeResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "containerRecipeArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDistributionConfigurationResponseTypeDef = TypedDict(
    "CreateDistributionConfigurationResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "distributionConfigurationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateImagePipelineResponseTypeDef = TypedDict(
    "CreateImagePipelineResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "imagePipelineArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateImageRecipeResponseTypeDef = TypedDict(
    "CreateImageRecipeResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "imageRecipeArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateImageResponseTypeDef = TypedDict(
    "CreateImageResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "imageBuildVersionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateInfrastructureConfigurationResponseTypeDef = TypedDict(
    "CreateInfrastructureConfigurationResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "infrastructureConfigurationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateLifecyclePolicyResponseTypeDef = TypedDict(
    "CreateLifecyclePolicyResponseTypeDef",
    {
        "clientToken": str,
        "lifecyclePolicyArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWorkflowResponseTypeDef = TypedDict(
    "CreateWorkflowResponseTypeDef",
    {
        "clientToken": str,
        "workflowBuildVersionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteComponentResponseTypeDef = TypedDict(
    "DeleteComponentResponseTypeDef",
    {
        "requestId": str,
        "componentBuildVersionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteContainerRecipeResponseTypeDef = TypedDict(
    "DeleteContainerRecipeResponseTypeDef",
    {
        "requestId": str,
        "containerRecipeArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDistributionConfigurationResponseTypeDef = TypedDict(
    "DeleteDistributionConfigurationResponseTypeDef",
    {
        "requestId": str,
        "distributionConfigurationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteImagePipelineResponseTypeDef = TypedDict(
    "DeleteImagePipelineResponseTypeDef",
    {
        "requestId": str,
        "imagePipelineArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteImageRecipeResponseTypeDef = TypedDict(
    "DeleteImageRecipeResponseTypeDef",
    {
        "requestId": str,
        "imageRecipeArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteImageResponseTypeDef = TypedDict(
    "DeleteImageResponseTypeDef",
    {
        "requestId": str,
        "imageBuildVersionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteInfrastructureConfigurationResponseTypeDef = TypedDict(
    "DeleteInfrastructureConfigurationResponseTypeDef",
    {
        "requestId": str,
        "infrastructureConfigurationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteLifecyclePolicyResponseTypeDef = TypedDict(
    "DeleteLifecyclePolicyResponseTypeDef",
    {
        "lifecyclePolicyArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteWorkflowResponseTypeDef = TypedDict(
    "DeleteWorkflowResponseTypeDef",
    {
        "workflowBuildVersionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetComponentPolicyResponseTypeDef = TypedDict(
    "GetComponentPolicyResponseTypeDef",
    {
        "requestId": str,
        "policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetContainerRecipePolicyResponseTypeDef = TypedDict(
    "GetContainerRecipePolicyResponseTypeDef",
    {
        "requestId": str,
        "policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetImagePolicyResponseTypeDef = TypedDict(
    "GetImagePolicyResponseTypeDef",
    {
        "requestId": str,
        "policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetImageRecipePolicyResponseTypeDef = TypedDict(
    "GetImageRecipePolicyResponseTypeDef",
    {
        "requestId": str,
        "policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetWorkflowExecutionResponseTypeDef = TypedDict(
    "GetWorkflowExecutionResponseTypeDef",
    {
        "requestId": str,
        "workflowBuildVersionArn": str,
        "workflowExecutionId": str,
        "imageBuildVersionArn": str,
        "type": WorkflowTypeType,
        "status": WorkflowExecutionStatusType,
        "message": str,
        "totalStepCount": int,
        "totalStepsSucceeded": int,
        "totalStepsFailed": int,
        "totalStepsSkipped": int,
        "startTime": str,
        "endTime": str,
        "parallelGroup": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetWorkflowStepExecutionResponseTypeDef = TypedDict(
    "GetWorkflowStepExecutionResponseTypeDef",
    {
        "requestId": str,
        "stepExecutionId": str,
        "workflowBuildVersionArn": str,
        "workflowExecutionId": str,
        "imageBuildVersionArn": str,
        "name": str,
        "description": str,
        "action": str,
        "status": WorkflowStepExecutionStatusType,
        "rollbackStatus": WorkflowStepExecutionRollbackStatusType,
        "message": str,
        "inputs": str,
        "outputs": str,
        "startTime": str,
        "endTime": str,
        "onFailure": str,
        "timeoutSeconds": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportComponentResponseTypeDef = TypedDict(
    "ImportComponentResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "componentBuildVersionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportVmImageResponseTypeDef = TypedDict(
    "ImportVmImageResponseTypeDef",
    {
        "requestId": str,
        "imageArn": str,
        "clientToken": str,
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
PutComponentPolicyResponseTypeDef = TypedDict(
    "PutComponentPolicyResponseTypeDef",
    {
        "requestId": str,
        "componentArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutContainerRecipePolicyResponseTypeDef = TypedDict(
    "PutContainerRecipePolicyResponseTypeDef",
    {
        "requestId": str,
        "containerRecipeArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutImagePolicyResponseTypeDef = TypedDict(
    "PutImagePolicyResponseTypeDef",
    {
        "requestId": str,
        "imageArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutImageRecipePolicyResponseTypeDef = TypedDict(
    "PutImageRecipePolicyResponseTypeDef",
    {
        "requestId": str,
        "imageRecipeArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendWorkflowStepActionResponseTypeDef = TypedDict(
    "SendWorkflowStepActionResponseTypeDef",
    {
        "stepExecutionId": str,
        "imageBuildVersionArn": str,
        "clientToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartImagePipelineExecutionResponseTypeDef = TypedDict(
    "StartImagePipelineExecutionResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "imageBuildVersionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartResourceStateUpdateResponseTypeDef = TypedDict(
    "StartResourceStateUpdateResponseTypeDef",
    {
        "lifecycleExecutionId": str,
        "resourceArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDistributionConfigurationResponseTypeDef = TypedDict(
    "UpdateDistributionConfigurationResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "distributionConfigurationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateImagePipelineResponseTypeDef = TypedDict(
    "UpdateImagePipelineResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "imagePipelineArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateInfrastructureConfigurationResponseTypeDef = TypedDict(
    "UpdateInfrastructureConfigurationResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "infrastructureConfigurationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateLifecyclePolicyResponseTypeDef = TypedDict(
    "UpdateLifecyclePolicyResponseTypeDef",
    {
        "lifecyclePolicyArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ComponentConfigurationOutputTypeDef = TypedDict(
    "ComponentConfigurationOutputTypeDef",
    {
        "componentArn": str,
        "parameters": NotRequired[List[ComponentParameterOutputTypeDef]],
    },
)
ComponentParameterUnionTypeDef = Union[ComponentParameterTypeDef, ComponentParameterOutputTypeDef]
ComponentSummaryTypeDef = TypedDict(
    "ComponentSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "version": NotRequired[str],
        "platform": NotRequired[PlatformType],
        "supportedOsVersions": NotRequired[List[str]],
        "state": NotRequired[ComponentStateTypeDef],
        "type": NotRequired[ComponentTypeType],
        "owner": NotRequired[str],
        "description": NotRequired[str],
        "changeDescription": NotRequired[str],
        "dateCreated": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "publisher": NotRequired[str],
        "obfuscate": NotRequired[bool],
    },
)
ComponentTypeDef = TypedDict(
    "ComponentTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "version": NotRequired[str],
        "description": NotRequired[str],
        "changeDescription": NotRequired[str],
        "type": NotRequired[ComponentTypeType],
        "platform": NotRequired[PlatformType],
        "supportedOsVersions": NotRequired[List[str]],
        "state": NotRequired[ComponentStateTypeDef],
        "parameters": NotRequired[List[ComponentParameterDetailTypeDef]],
        "owner": NotRequired[str],
        "data": NotRequired[str],
        "kmsKeyId": NotRequired[str],
        "encrypted": NotRequired[bool],
        "dateCreated": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "publisher": NotRequired[str],
        "obfuscate": NotRequired[bool],
    },
)
ListComponentsResponseTypeDef = TypedDict(
    "ListComponentsResponseTypeDef",
    {
        "requestId": str,
        "componentVersionList": List[ComponentVersionTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ContainerDistributionConfigurationOutputTypeDef = TypedDict(
    "ContainerDistributionConfigurationOutputTypeDef",
    {
        "targetRepository": TargetContainerRepositoryTypeDef,
        "description": NotRequired[str],
        "containerTags": NotRequired[List[str]],
    },
)
ContainerDistributionConfigurationTypeDef = TypedDict(
    "ContainerDistributionConfigurationTypeDef",
    {
        "targetRepository": TargetContainerRepositoryTypeDef,
        "description": NotRequired[str],
        "containerTags": NotRequired[Sequence[str]],
    },
)
ListContainerRecipesResponseTypeDef = TypedDict(
    "ListContainerRecipesResponseTypeDef",
    {
        "requestId": str,
        "containerRecipeSummaryList": List[ContainerRecipeSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CvssScoreDetailsTypeDef = TypedDict(
    "CvssScoreDetailsTypeDef",
    {
        "scoreSource": NotRequired[str],
        "cvssSource": NotRequired[str],
        "version": NotRequired[str],
        "score": NotRequired[float],
        "scoringVector": NotRequired[str],
        "adjustments": NotRequired[List[CvssScoreAdjustmentTypeDef]],
    },
)
ListDistributionConfigurationsResponseTypeDef = TypedDict(
    "ListDistributionConfigurationsResponseTypeDef",
    {
        "requestId": str,
        "distributionConfigurationSummaryList": List[DistributionConfigurationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InstanceBlockDeviceMappingTypeDef = TypedDict(
    "InstanceBlockDeviceMappingTypeDef",
    {
        "deviceName": NotRequired[str],
        "ebs": NotRequired[EbsInstanceBlockDeviceSpecificationTypeDef],
        "virtualName": NotRequired[str],
        "noDevice": NotRequired[str],
    },
)
ImageScanningConfigurationOutputTypeDef = TypedDict(
    "ImageScanningConfigurationOutputTypeDef",
    {
        "imageScanningEnabled": NotRequired[bool],
        "ecrConfiguration": NotRequired[EcrConfigurationOutputTypeDef],
    },
)
EcrConfigurationUnionTypeDef = Union[EcrConfigurationTypeDef, EcrConfigurationOutputTypeDef]
FastLaunchConfigurationTypeDef = TypedDict(
    "FastLaunchConfigurationTypeDef",
    {
        "enabled": bool,
        "snapshotConfiguration": NotRequired[FastLaunchSnapshotConfigurationTypeDef],
        "maxParallelLaunches": NotRequired[int],
        "launchTemplate": NotRequired[FastLaunchLaunchTemplateSpecificationTypeDef],
        "accountId": NotRequired[str],
    },
)
ListComponentsRequestRequestTypeDef = TypedDict(
    "ListComponentsRequestRequestTypeDef",
    {
        "owner": NotRequired[OwnershipType],
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "byName": NotRequired[bool],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListContainerRecipesRequestRequestTypeDef = TypedDict(
    "ListContainerRecipesRequestRequestTypeDef",
    {
        "owner": NotRequired[OwnershipType],
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListDistributionConfigurationsRequestRequestTypeDef = TypedDict(
    "ListDistributionConfigurationsRequestRequestTypeDef",
    {
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListImageBuildVersionsRequestRequestTypeDef = TypedDict(
    "ListImageBuildVersionsRequestRequestTypeDef",
    {
        "imageVersionArn": str,
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListImagePipelineImagesRequestRequestTypeDef = TypedDict(
    "ListImagePipelineImagesRequestRequestTypeDef",
    {
        "imagePipelineArn": str,
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListImagePipelinesRequestRequestTypeDef = TypedDict(
    "ListImagePipelinesRequestRequestTypeDef",
    {
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListImageRecipesRequestRequestTypeDef = TypedDict(
    "ListImageRecipesRequestRequestTypeDef",
    {
        "owner": NotRequired[OwnershipType],
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListImageScanFindingAggregationsRequestRequestTypeDef = TypedDict(
    "ListImageScanFindingAggregationsRequestRequestTypeDef",
    {
        "filter": NotRequired[FilterTypeDef],
        "nextToken": NotRequired[str],
    },
)
ListImagesRequestRequestTypeDef = TypedDict(
    "ListImagesRequestRequestTypeDef",
    {
        "owner": NotRequired[OwnershipType],
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "byName": NotRequired[bool],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "includeDeprecated": NotRequired[bool],
    },
)
ListInfrastructureConfigurationsRequestRequestTypeDef = TypedDict(
    "ListInfrastructureConfigurationsRequestRequestTypeDef",
    {
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListLifecyclePoliciesRequestRequestTypeDef = TypedDict(
    "ListLifecyclePoliciesRequestRequestTypeDef",
    {
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListWorkflowsRequestRequestTypeDef = TypedDict(
    "ListWorkflowsRequestRequestTypeDef",
    {
        "owner": NotRequired[OwnershipType],
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "byName": NotRequired[bool],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListImagePackagesResponseTypeDef = TypedDict(
    "ListImagePackagesResponseTypeDef",
    {
        "requestId": str,
        "imagePackageList": List[ImagePackageTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListImageRecipesResponseTypeDef = TypedDict(
    "ListImageRecipesResponseTypeDef",
    {
        "requestId": str,
        "imageRecipeSummaryList": List[ImageRecipeSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListImageScanFindingsRequestRequestTypeDef = TypedDict(
    "ListImageScanFindingsRequestRequestTypeDef",
    {
        "filters": NotRequired[Sequence[ImageScanFindingsFilterTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListImagesResponseTypeDef = TypedDict(
    "ListImagesResponseTypeDef",
    {
        "requestId": str,
        "imageVersionList": List[ImageVersionTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListInfrastructureConfigurationsResponseTypeDef = TypedDict(
    "ListInfrastructureConfigurationsResponseTypeDef",
    {
        "requestId": str,
        "infrastructureConfigurationSummaryList": List[InfrastructureConfigurationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LaunchPermissionConfigurationUnionTypeDef = Union[
    LaunchPermissionConfigurationTypeDef, LaunchPermissionConfigurationOutputTypeDef
]
LifecycleExecutionSnapshotResourceTypeDef = TypedDict(
    "LifecycleExecutionSnapshotResourceTypeDef",
    {
        "snapshotId": NotRequired[str],
        "state": NotRequired[LifecycleExecutionResourceStateTypeDef],
    },
)
LifecycleExecutionTypeDef = TypedDict(
    "LifecycleExecutionTypeDef",
    {
        "lifecycleExecutionId": NotRequired[str],
        "lifecyclePolicyArn": NotRequired[str],
        "resourcesImpactedSummary": NotRequired[LifecycleExecutionResourcesImpactedSummaryTypeDef],
        "state": NotRequired[LifecycleExecutionStateTypeDef],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
    },
)
LifecyclePolicyDetailActionTypeDef = TypedDict(
    "LifecyclePolicyDetailActionTypeDef",
    {
        "type": LifecyclePolicyDetailActionTypeType,
        "includeResources": NotRequired[LifecyclePolicyDetailActionIncludeResourcesTypeDef],
    },
)
LifecyclePolicyDetailExclusionRulesAmisOutputTypeDef = TypedDict(
    "LifecyclePolicyDetailExclusionRulesAmisOutputTypeDef",
    {
        "isPublic": NotRequired[bool],
        "regions": NotRequired[List[str]],
        "sharedAccounts": NotRequired[List[str]],
        "lastLaunched": NotRequired[LifecyclePolicyDetailExclusionRulesAmisLastLaunchedTypeDef],
        "tagMap": NotRequired[Dict[str, str]],
    },
)
LifecyclePolicyDetailExclusionRulesAmisTypeDef = TypedDict(
    "LifecyclePolicyDetailExclusionRulesAmisTypeDef",
    {
        "isPublic": NotRequired[bool],
        "regions": NotRequired[Sequence[str]],
        "sharedAccounts": NotRequired[Sequence[str]],
        "lastLaunched": NotRequired[LifecyclePolicyDetailExclusionRulesAmisLastLaunchedTypeDef],
        "tagMap": NotRequired[Mapping[str, str]],
    },
)
LifecyclePolicyResourceSelectionOutputTypeDef = TypedDict(
    "LifecyclePolicyResourceSelectionOutputTypeDef",
    {
        "recipes": NotRequired[List[LifecyclePolicyResourceSelectionRecipeTypeDef]],
        "tagMap": NotRequired[Dict[str, str]],
    },
)
LifecyclePolicyResourceSelectionTypeDef = TypedDict(
    "LifecyclePolicyResourceSelectionTypeDef",
    {
        "recipes": NotRequired[Sequence[LifecyclePolicyResourceSelectionRecipeTypeDef]],
        "tagMap": NotRequired[Mapping[str, str]],
    },
)
ListLifecyclePoliciesResponseTypeDef = TypedDict(
    "ListLifecyclePoliciesResponseTypeDef",
    {
        "lifecyclePolicySummaryList": List[LifecyclePolicySummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListWaitingWorkflowStepsResponseTypeDef = TypedDict(
    "ListWaitingWorkflowStepsResponseTypeDef",
    {
        "steps": List[WorkflowStepExecutionTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListWorkflowExecutionsResponseTypeDef = TypedDict(
    "ListWorkflowExecutionsResponseTypeDef",
    {
        "requestId": str,
        "workflowExecutions": List[WorkflowExecutionMetadataTypeDef],
        "imageBuildVersionArn": str,
        "message": str,
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListWorkflowStepExecutionsResponseTypeDef = TypedDict(
    "ListWorkflowStepExecutionsResponseTypeDef",
    {
        "requestId": str,
        "steps": List[WorkflowStepMetadataTypeDef],
        "workflowBuildVersionArn": str,
        "workflowExecutionId": str,
        "imageBuildVersionArn": str,
        "message": str,
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListWorkflowsResponseTypeDef = TypedDict(
    "ListWorkflowsResponseTypeDef",
    {
        "workflowVersionList": List[WorkflowVersionTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LoggingTypeDef = TypedDict(
    "LoggingTypeDef",
    {
        "s3Logs": NotRequired[S3LogsTypeDef],
    },
)
PackageVulnerabilityDetailsTypeDef = TypedDict(
    "PackageVulnerabilityDetailsTypeDef",
    {
        "vulnerabilityId": str,
        "vulnerablePackages": NotRequired[List[VulnerablePackageTypeDef]],
        "source": NotRequired[str],
        "cvss": NotRequired[List[CvssScoreTypeDef]],
        "relatedVulnerabilities": NotRequired[List[str]],
        "sourceUrl": NotRequired[str],
        "vendorSeverity": NotRequired[str],
        "vendorCreatedAt": NotRequired[datetime],
        "vendorUpdatedAt": NotRequired[datetime],
        "referenceUrls": NotRequired[List[str]],
    },
)
RemediationTypeDef = TypedDict(
    "RemediationTypeDef",
    {
        "recommendation": NotRequired[RemediationRecommendationTypeDef],
    },
)
WorkflowConfigurationOutputTypeDef = TypedDict(
    "WorkflowConfigurationOutputTypeDef",
    {
        "workflowArn": str,
        "parameters": NotRequired[List[WorkflowParameterOutputTypeDef]],
        "parallelGroup": NotRequired[str],
        "onFailure": NotRequired[OnWorkflowFailureType],
    },
)
WorkflowParameterUnionTypeDef = Union[WorkflowParameterTypeDef, WorkflowParameterOutputTypeDef]
WorkflowSummaryTypeDef = TypedDict(
    "WorkflowSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "version": NotRequired[str],
        "description": NotRequired[str],
        "changeDescription": NotRequired[str],
        "type": NotRequired[WorkflowTypeType],
        "owner": NotRequired[str],
        "state": NotRequired[WorkflowStateTypeDef],
        "dateCreated": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)
WorkflowTypeDef = TypedDict(
    "WorkflowTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "version": NotRequired[str],
        "description": NotRequired[str],
        "changeDescription": NotRequired[str],
        "type": NotRequired[WorkflowTypeType],
        "state": NotRequired[WorkflowStateTypeDef],
        "owner": NotRequired[str],
        "data": NotRequired[str],
        "kmsKeyId": NotRequired[str],
        "dateCreated": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "parameters": NotRequired[List[WorkflowParameterDetailTypeDef]],
    },
)
ImageScanFindingAggregationTypeDef = TypedDict(
    "ImageScanFindingAggregationTypeDef",
    {
        "accountAggregation": NotRequired[AccountAggregationTypeDef],
        "imageAggregation": NotRequired[ImageAggregationTypeDef],
        "imagePipelineAggregation": NotRequired[ImagePipelineAggregationTypeDef],
        "vulnerabilityIdAggregation": NotRequired[VulnerabilityIdAggregationTypeDef],
    },
)
OutputResourcesTypeDef = TypedDict(
    "OutputResourcesTypeDef",
    {
        "amis": NotRequired[List[AmiTypeDef]],
        "containers": NotRequired[List[ContainerTypeDef]],
    },
)
ComponentConfigurationTypeDef = TypedDict(
    "ComponentConfigurationTypeDef",
    {
        "componentArn": str,
        "parameters": NotRequired[Sequence[ComponentParameterUnionTypeDef]],
    },
)
ListComponentBuildVersionsResponseTypeDef = TypedDict(
    "ListComponentBuildVersionsResponseTypeDef",
    {
        "requestId": str,
        "componentSummaryList": List[ComponentSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetComponentResponseTypeDef = TypedDict(
    "GetComponentResponseTypeDef",
    {
        "requestId": str,
        "component": ComponentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ContainerDistributionConfigurationUnionTypeDef = Union[
    ContainerDistributionConfigurationTypeDef, ContainerDistributionConfigurationOutputTypeDef
]
InspectorScoreDetailsTypeDef = TypedDict(
    "InspectorScoreDetailsTypeDef",
    {
        "adjustedCvss": NotRequired[CvssScoreDetailsTypeDef],
    },
)
ImageRecipeTypeDef = TypedDict(
    "ImageRecipeTypeDef",
    {
        "arn": NotRequired[str],
        "type": NotRequired[ImageTypeType],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "platform": NotRequired[PlatformType],
        "owner": NotRequired[str],
        "version": NotRequired[str],
        "components": NotRequired[List[ComponentConfigurationOutputTypeDef]],
        "parentImage": NotRequired[str],
        "blockDeviceMappings": NotRequired[List[InstanceBlockDeviceMappingTypeDef]],
        "dateCreated": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "workingDirectory": NotRequired[str],
        "additionalInstanceConfiguration": NotRequired[AdditionalInstanceConfigurationTypeDef],
    },
)
InstanceConfigurationOutputTypeDef = TypedDict(
    "InstanceConfigurationOutputTypeDef",
    {
        "image": NotRequired[str],
        "blockDeviceMappings": NotRequired[List[InstanceBlockDeviceMappingTypeDef]],
    },
)
InstanceConfigurationTypeDef = TypedDict(
    "InstanceConfigurationTypeDef",
    {
        "image": NotRequired[str],
        "blockDeviceMappings": NotRequired[Sequence[InstanceBlockDeviceMappingTypeDef]],
    },
)
ImageScanningConfigurationTypeDef = TypedDict(
    "ImageScanningConfigurationTypeDef",
    {
        "imageScanningEnabled": NotRequired[bool],
        "ecrConfiguration": NotRequired[EcrConfigurationUnionTypeDef],
    },
)
DistributionOutputTypeDef = TypedDict(
    "DistributionOutputTypeDef",
    {
        "region": str,
        "amiDistributionConfiguration": NotRequired[AmiDistributionConfigurationOutputTypeDef],
        "containerDistributionConfiguration": NotRequired[
            ContainerDistributionConfigurationOutputTypeDef
        ],
        "licenseConfigurationArns": NotRequired[List[str]],
        "launchTemplateConfigurations": NotRequired[List[LaunchTemplateConfigurationTypeDef]],
        "s3ExportConfiguration": NotRequired[S3ExportConfigurationTypeDef],
        "fastLaunchConfigurations": NotRequired[List[FastLaunchConfigurationTypeDef]],
    },
)
AmiDistributionConfigurationTypeDef = TypedDict(
    "AmiDistributionConfigurationTypeDef",
    {
        "name": NotRequired[str],
        "description": NotRequired[str],
        "targetAccountIds": NotRequired[Sequence[str]],
        "amiTags": NotRequired[Mapping[str, str]],
        "kmsKeyId": NotRequired[str],
        "launchPermission": NotRequired[LaunchPermissionConfigurationUnionTypeDef],
    },
)
LifecycleExecutionResourceTypeDef = TypedDict(
    "LifecycleExecutionResourceTypeDef",
    {
        "accountId": NotRequired[str],
        "resourceId": NotRequired[str],
        "state": NotRequired[LifecycleExecutionResourceStateTypeDef],
        "action": NotRequired[LifecycleExecutionResourceActionTypeDef],
        "region": NotRequired[str],
        "snapshots": NotRequired[List[LifecycleExecutionSnapshotResourceTypeDef]],
        "imageUris": NotRequired[List[str]],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
    },
)
GetLifecycleExecutionResponseTypeDef = TypedDict(
    "GetLifecycleExecutionResponseTypeDef",
    {
        "lifecycleExecution": LifecycleExecutionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListLifecycleExecutionsResponseTypeDef = TypedDict(
    "ListLifecycleExecutionsResponseTypeDef",
    {
        "lifecycleExecutions": List[LifecycleExecutionTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LifecyclePolicyDetailExclusionRulesOutputTypeDef = TypedDict(
    "LifecyclePolicyDetailExclusionRulesOutputTypeDef",
    {
        "tagMap": NotRequired[Dict[str, str]],
        "amis": NotRequired[LifecyclePolicyDetailExclusionRulesAmisOutputTypeDef],
    },
)
LifecyclePolicyDetailExclusionRulesAmisUnionTypeDef = Union[
    LifecyclePolicyDetailExclusionRulesAmisTypeDef,
    LifecyclePolicyDetailExclusionRulesAmisOutputTypeDef,
]
CreateInfrastructureConfigurationRequestRequestTypeDef = TypedDict(
    "CreateInfrastructureConfigurationRequestRequestTypeDef",
    {
        "name": str,
        "instanceProfileName": str,
        "clientToken": str,
        "description": NotRequired[str],
        "instanceTypes": NotRequired[Sequence[str]],
        "securityGroupIds": NotRequired[Sequence[str]],
        "subnetId": NotRequired[str],
        "logging": NotRequired[LoggingTypeDef],
        "keyPair": NotRequired[str],
        "terminateInstanceOnFailure": NotRequired[bool],
        "snsTopicArn": NotRequired[str],
        "resourceTags": NotRequired[Mapping[str, str]],
        "instanceMetadataOptions": NotRequired[InstanceMetadataOptionsTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
InfrastructureConfigurationTypeDef = TypedDict(
    "InfrastructureConfigurationTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "instanceTypes": NotRequired[List[str]],
        "instanceProfileName": NotRequired[str],
        "securityGroupIds": NotRequired[List[str]],
        "subnetId": NotRequired[str],
        "logging": NotRequired[LoggingTypeDef],
        "keyPair": NotRequired[str],
        "terminateInstanceOnFailure": NotRequired[bool],
        "snsTopicArn": NotRequired[str],
        "dateCreated": NotRequired[str],
        "dateUpdated": NotRequired[str],
        "resourceTags": NotRequired[Dict[str, str]],
        "instanceMetadataOptions": NotRequired[InstanceMetadataOptionsTypeDef],
        "tags": NotRequired[Dict[str, str]],
    },
)
UpdateInfrastructureConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateInfrastructureConfigurationRequestRequestTypeDef",
    {
        "infrastructureConfigurationArn": str,
        "instanceProfileName": str,
        "clientToken": str,
        "description": NotRequired[str],
        "instanceTypes": NotRequired[Sequence[str]],
        "securityGroupIds": NotRequired[Sequence[str]],
        "subnetId": NotRequired[str],
        "logging": NotRequired[LoggingTypeDef],
        "keyPair": NotRequired[str],
        "terminateInstanceOnFailure": NotRequired[bool],
        "snsTopicArn": NotRequired[str],
        "resourceTags": NotRequired[Mapping[str, str]],
        "instanceMetadataOptions": NotRequired[InstanceMetadataOptionsTypeDef],
    },
)
ImagePipelineTypeDef = TypedDict(
    "ImagePipelineTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "platform": NotRequired[PlatformType],
        "enhancedImageMetadataEnabled": NotRequired[bool],
        "imageRecipeArn": NotRequired[str],
        "containerRecipeArn": NotRequired[str],
        "infrastructureConfigurationArn": NotRequired[str],
        "distributionConfigurationArn": NotRequired[str],
        "imageTestsConfiguration": NotRequired[ImageTestsConfigurationTypeDef],
        "schedule": NotRequired[ScheduleTypeDef],
        "status": NotRequired[PipelineStatusType],
        "dateCreated": NotRequired[str],
        "dateUpdated": NotRequired[str],
        "dateLastRun": NotRequired[str],
        "dateNextRun": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "imageScanningConfiguration": NotRequired[ImageScanningConfigurationOutputTypeDef],
        "executionRole": NotRequired[str],
        "workflows": NotRequired[List[WorkflowConfigurationOutputTypeDef]],
    },
)
WorkflowConfigurationTypeDef = TypedDict(
    "WorkflowConfigurationTypeDef",
    {
        "workflowArn": str,
        "parameters": NotRequired[Sequence[WorkflowParameterUnionTypeDef]],
        "parallelGroup": NotRequired[str],
        "onFailure": NotRequired[OnWorkflowFailureType],
    },
)
ListWorkflowBuildVersionsResponseTypeDef = TypedDict(
    "ListWorkflowBuildVersionsResponseTypeDef",
    {
        "workflowSummaryList": List[WorkflowSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetWorkflowResponseTypeDef = TypedDict(
    "GetWorkflowResponseTypeDef",
    {
        "workflow": WorkflowTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListImageScanFindingAggregationsResponseTypeDef = TypedDict(
    "ListImageScanFindingAggregationsResponseTypeDef",
    {
        "requestId": str,
        "aggregationType": str,
        "responses": List[ImageScanFindingAggregationTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImageSummaryTypeDef = TypedDict(
    "ImageSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[ImageTypeType],
        "version": NotRequired[str],
        "platform": NotRequired[PlatformType],
        "osVersion": NotRequired[str],
        "state": NotRequired[ImageStateTypeDef],
        "owner": NotRequired[str],
        "dateCreated": NotRequired[str],
        "outputResources": NotRequired[OutputResourcesTypeDef],
        "tags": NotRequired[Dict[str, str]],
        "buildType": NotRequired[BuildTypeType],
        "imageSource": NotRequired[ImageSourceType],
        "deprecationTime": NotRequired[datetime],
        "lifecycleExecutionId": NotRequired[str],
    },
)
ComponentConfigurationUnionTypeDef = Union[
    ComponentConfigurationTypeDef, ComponentConfigurationOutputTypeDef
]
CreateImageRecipeRequestRequestTypeDef = TypedDict(
    "CreateImageRecipeRequestRequestTypeDef",
    {
        "name": str,
        "semanticVersion": str,
        "components": Sequence[ComponentConfigurationTypeDef],
        "parentImage": str,
        "clientToken": str,
        "description": NotRequired[str],
        "blockDeviceMappings": NotRequired[Sequence[InstanceBlockDeviceMappingTypeDef]],
        "tags": NotRequired[Mapping[str, str]],
        "workingDirectory": NotRequired[str],
        "additionalInstanceConfiguration": NotRequired[AdditionalInstanceConfigurationTypeDef],
    },
)
ImageScanFindingTypeDef = TypedDict(
    "ImageScanFindingTypeDef",
    {
        "awsAccountId": NotRequired[str],
        "imageBuildVersionArn": NotRequired[str],
        "imagePipelineArn": NotRequired[str],
        "type": NotRequired[str],
        "description": NotRequired[str],
        "title": NotRequired[str],
        "remediation": NotRequired[RemediationTypeDef],
        "severity": NotRequired[str],
        "firstObservedAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
        "inspectorScore": NotRequired[float],
        "inspectorScoreDetails": NotRequired[InspectorScoreDetailsTypeDef],
        "packageVulnerabilityDetails": NotRequired[PackageVulnerabilityDetailsTypeDef],
        "fixAvailable": NotRequired[str],
    },
)
GetImageRecipeResponseTypeDef = TypedDict(
    "GetImageRecipeResponseTypeDef",
    {
        "requestId": str,
        "imageRecipe": ImageRecipeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ContainerRecipeTypeDef = TypedDict(
    "ContainerRecipeTypeDef",
    {
        "arn": NotRequired[str],
        "containerType": NotRequired[Literal["DOCKER"]],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "platform": NotRequired[PlatformType],
        "owner": NotRequired[str],
        "version": NotRequired[str],
        "components": NotRequired[List[ComponentConfigurationOutputTypeDef]],
        "instanceConfiguration": NotRequired[InstanceConfigurationOutputTypeDef],
        "dockerfileTemplateData": NotRequired[str],
        "kmsKeyId": NotRequired[str],
        "encrypted": NotRequired[bool],
        "parentImage": NotRequired[str],
        "dateCreated": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "workingDirectory": NotRequired[str],
        "targetRepository": NotRequired[TargetContainerRepositoryTypeDef],
    },
)
DistributionConfigurationTypeDef = TypedDict(
    "DistributionConfigurationTypeDef",
    {
        "timeoutMinutes": int,
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "distributions": NotRequired[List[DistributionOutputTypeDef]],
        "dateCreated": NotRequired[str],
        "dateUpdated": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)
AmiDistributionConfigurationUnionTypeDef = Union[
    AmiDistributionConfigurationTypeDef, AmiDistributionConfigurationOutputTypeDef
]
ListLifecycleExecutionResourcesResponseTypeDef = TypedDict(
    "ListLifecycleExecutionResourcesResponseTypeDef",
    {
        "lifecycleExecutionId": str,
        "lifecycleExecutionState": LifecycleExecutionStateTypeDef,
        "resources": List[LifecycleExecutionResourceTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LifecyclePolicyDetailOutputTypeDef = TypedDict(
    "LifecyclePolicyDetailOutputTypeDef",
    {
        "action": LifecyclePolicyDetailActionTypeDef,
        "filter": LifecyclePolicyDetailFilterTypeDef,
        "exclusionRules": NotRequired[LifecyclePolicyDetailExclusionRulesOutputTypeDef],
    },
)
LifecyclePolicyDetailExclusionRulesTypeDef = TypedDict(
    "LifecyclePolicyDetailExclusionRulesTypeDef",
    {
        "tagMap": NotRequired[Mapping[str, str]],
        "amis": NotRequired[LifecyclePolicyDetailExclusionRulesAmisUnionTypeDef],
    },
)
ResourceStateUpdateExclusionRulesTypeDef = TypedDict(
    "ResourceStateUpdateExclusionRulesTypeDef",
    {
        "amis": NotRequired[LifecyclePolicyDetailExclusionRulesAmisUnionTypeDef],
    },
)
GetInfrastructureConfigurationResponseTypeDef = TypedDict(
    "GetInfrastructureConfigurationResponseTypeDef",
    {
        "requestId": str,
        "infrastructureConfiguration": InfrastructureConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetImagePipelineResponseTypeDef = TypedDict(
    "GetImagePipelineResponseTypeDef",
    {
        "requestId": str,
        "imagePipeline": ImagePipelineTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListImagePipelinesResponseTypeDef = TypedDict(
    "ListImagePipelinesResponseTypeDef",
    {
        "requestId": str,
        "imagePipelineList": List[ImagePipelineTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateImagePipelineRequestRequestTypeDef = TypedDict(
    "CreateImagePipelineRequestRequestTypeDef",
    {
        "name": str,
        "infrastructureConfigurationArn": str,
        "clientToken": str,
        "description": NotRequired[str],
        "imageRecipeArn": NotRequired[str],
        "containerRecipeArn": NotRequired[str],
        "distributionConfigurationArn": NotRequired[str],
        "imageTestsConfiguration": NotRequired[ImageTestsConfigurationTypeDef],
        "enhancedImageMetadataEnabled": NotRequired[bool],
        "schedule": NotRequired[ScheduleTypeDef],
        "status": NotRequired[PipelineStatusType],
        "tags": NotRequired[Mapping[str, str]],
        "imageScanningConfiguration": NotRequired[ImageScanningConfigurationTypeDef],
        "workflows": NotRequired[Sequence[WorkflowConfigurationTypeDef]],
        "executionRole": NotRequired[str],
    },
)
UpdateImagePipelineRequestRequestTypeDef = TypedDict(
    "UpdateImagePipelineRequestRequestTypeDef",
    {
        "imagePipelineArn": str,
        "infrastructureConfigurationArn": str,
        "clientToken": str,
        "description": NotRequired[str],
        "imageRecipeArn": NotRequired[str],
        "containerRecipeArn": NotRequired[str],
        "distributionConfigurationArn": NotRequired[str],
        "imageTestsConfiguration": NotRequired[ImageTestsConfigurationTypeDef],
        "enhancedImageMetadataEnabled": NotRequired[bool],
        "schedule": NotRequired[ScheduleTypeDef],
        "status": NotRequired[PipelineStatusType],
        "imageScanningConfiguration": NotRequired[ImageScanningConfigurationTypeDef],
        "workflows": NotRequired[Sequence[WorkflowConfigurationTypeDef]],
        "executionRole": NotRequired[str],
    },
)
WorkflowConfigurationUnionTypeDef = Union[
    WorkflowConfigurationTypeDef, WorkflowConfigurationOutputTypeDef
]
ListImageBuildVersionsResponseTypeDef = TypedDict(
    "ListImageBuildVersionsResponseTypeDef",
    {
        "requestId": str,
        "imageSummaryList": List[ImageSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListImagePipelineImagesResponseTypeDef = TypedDict(
    "ListImagePipelineImagesResponseTypeDef",
    {
        "requestId": str,
        "imageSummaryList": List[ImageSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateContainerRecipeRequestRequestTypeDef = TypedDict(
    "CreateContainerRecipeRequestRequestTypeDef",
    {
        "containerType": Literal["DOCKER"],
        "name": str,
        "semanticVersion": str,
        "components": Sequence[ComponentConfigurationUnionTypeDef],
        "parentImage": str,
        "targetRepository": TargetContainerRepositoryTypeDef,
        "clientToken": str,
        "description": NotRequired[str],
        "instanceConfiguration": NotRequired[InstanceConfigurationTypeDef],
        "dockerfileTemplateData": NotRequired[str],
        "dockerfileTemplateUri": NotRequired[str],
        "platformOverride": NotRequired[PlatformType],
        "imageOsVersionOverride": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "workingDirectory": NotRequired[str],
        "kmsKeyId": NotRequired[str],
    },
)
ListImageScanFindingsResponseTypeDef = TypedDict(
    "ListImageScanFindingsResponseTypeDef",
    {
        "requestId": str,
        "findings": List[ImageScanFindingTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetContainerRecipeResponseTypeDef = TypedDict(
    "GetContainerRecipeResponseTypeDef",
    {
        "requestId": str,
        "containerRecipe": ContainerRecipeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDistributionConfigurationResponseTypeDef = TypedDict(
    "GetDistributionConfigurationResponseTypeDef",
    {
        "requestId": str,
        "distributionConfiguration": DistributionConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImageTypeDef = TypedDict(
    "ImageTypeDef",
    {
        "arn": NotRequired[str],
        "type": NotRequired[ImageTypeType],
        "name": NotRequired[str],
        "version": NotRequired[str],
        "platform": NotRequired[PlatformType],
        "enhancedImageMetadataEnabled": NotRequired[bool],
        "osVersion": NotRequired[str],
        "state": NotRequired[ImageStateTypeDef],
        "imageRecipe": NotRequired[ImageRecipeTypeDef],
        "containerRecipe": NotRequired[ContainerRecipeTypeDef],
        "sourcePipelineName": NotRequired[str],
        "sourcePipelineArn": NotRequired[str],
        "infrastructureConfiguration": NotRequired[InfrastructureConfigurationTypeDef],
        "distributionConfiguration": NotRequired[DistributionConfigurationTypeDef],
        "imageTestsConfiguration": NotRequired[ImageTestsConfigurationTypeDef],
        "dateCreated": NotRequired[str],
        "outputResources": NotRequired[OutputResourcesTypeDef],
        "tags": NotRequired[Dict[str, str]],
        "buildType": NotRequired[BuildTypeType],
        "imageSource": NotRequired[ImageSourceType],
        "scanState": NotRequired[ImageScanStateTypeDef],
        "imageScanningConfiguration": NotRequired[ImageScanningConfigurationOutputTypeDef],
        "deprecationTime": NotRequired[datetime],
        "lifecycleExecutionId": NotRequired[str],
        "executionRole": NotRequired[str],
        "workflows": NotRequired[List[WorkflowConfigurationOutputTypeDef]],
    },
)
DistributionTypeDef = TypedDict(
    "DistributionTypeDef",
    {
        "region": str,
        "amiDistributionConfiguration": NotRequired[AmiDistributionConfigurationUnionTypeDef],
        "containerDistributionConfiguration": NotRequired[
            ContainerDistributionConfigurationUnionTypeDef
        ],
        "licenseConfigurationArns": NotRequired[Sequence[str]],
        "launchTemplateConfigurations": NotRequired[Sequence[LaunchTemplateConfigurationTypeDef]],
        "s3ExportConfiguration": NotRequired[S3ExportConfigurationTypeDef],
        "fastLaunchConfigurations": NotRequired[Sequence[FastLaunchConfigurationTypeDef]],
    },
)
LifecyclePolicyTypeDef = TypedDict(
    "LifecyclePolicyTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "status": NotRequired[LifecyclePolicyStatusType],
        "executionRole": NotRequired[str],
        "resourceType": NotRequired[LifecyclePolicyResourceTypeType],
        "policyDetails": NotRequired[List[LifecyclePolicyDetailOutputTypeDef]],
        "resourceSelection": NotRequired[LifecyclePolicyResourceSelectionOutputTypeDef],
        "dateCreated": NotRequired[datetime],
        "dateUpdated": NotRequired[datetime],
        "dateLastRun": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
    },
)
LifecyclePolicyDetailExclusionRulesUnionTypeDef = Union[
    LifecyclePolicyDetailExclusionRulesTypeDef, LifecyclePolicyDetailExclusionRulesOutputTypeDef
]
StartResourceStateUpdateRequestRequestTypeDef = TypedDict(
    "StartResourceStateUpdateRequestRequestTypeDef",
    {
        "resourceArn": str,
        "state": ResourceStateTypeDef,
        "clientToken": str,
        "executionRole": NotRequired[str],
        "includeResources": NotRequired[ResourceStateUpdateIncludeResourcesTypeDef],
        "exclusionRules": NotRequired[ResourceStateUpdateExclusionRulesTypeDef],
        "updateAt": NotRequired[TimestampTypeDef],
    },
)
CreateImageRequestRequestTypeDef = TypedDict(
    "CreateImageRequestRequestTypeDef",
    {
        "infrastructureConfigurationArn": str,
        "clientToken": str,
        "imageRecipeArn": NotRequired[str],
        "containerRecipeArn": NotRequired[str],
        "distributionConfigurationArn": NotRequired[str],
        "imageTestsConfiguration": NotRequired[ImageTestsConfigurationTypeDef],
        "enhancedImageMetadataEnabled": NotRequired[bool],
        "tags": NotRequired[Mapping[str, str]],
        "imageScanningConfiguration": NotRequired[ImageScanningConfigurationTypeDef],
        "workflows": NotRequired[Sequence[WorkflowConfigurationUnionTypeDef]],
        "executionRole": NotRequired[str],
    },
)
GetImageResponseTypeDef = TypedDict(
    "GetImageResponseTypeDef",
    {
        "requestId": str,
        "image": ImageTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DistributionUnionTypeDef = Union[DistributionTypeDef, DistributionOutputTypeDef]
UpdateDistributionConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateDistributionConfigurationRequestRequestTypeDef",
    {
        "distributionConfigurationArn": str,
        "distributions": Sequence[DistributionTypeDef],
        "clientToken": str,
        "description": NotRequired[str],
    },
)
GetLifecyclePolicyResponseTypeDef = TypedDict(
    "GetLifecyclePolicyResponseTypeDef",
    {
        "lifecyclePolicy": LifecyclePolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LifecyclePolicyDetailTypeDef = TypedDict(
    "LifecyclePolicyDetailTypeDef",
    {
        "action": LifecyclePolicyDetailActionTypeDef,
        "filter": LifecyclePolicyDetailFilterTypeDef,
        "exclusionRules": NotRequired[LifecyclePolicyDetailExclusionRulesUnionTypeDef],
    },
)
CreateDistributionConfigurationRequestRequestTypeDef = TypedDict(
    "CreateDistributionConfigurationRequestRequestTypeDef",
    {
        "name": str,
        "distributions": Sequence[DistributionUnionTypeDef],
        "clientToken": str,
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
LifecyclePolicyDetailUnionTypeDef = Union[
    LifecyclePolicyDetailTypeDef, LifecyclePolicyDetailOutputTypeDef
]
UpdateLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "UpdateLifecyclePolicyRequestRequestTypeDef",
    {
        "lifecyclePolicyArn": str,
        "executionRole": str,
        "resourceType": LifecyclePolicyResourceTypeType,
        "policyDetails": Sequence[LifecyclePolicyDetailTypeDef],
        "resourceSelection": LifecyclePolicyResourceSelectionTypeDef,
        "clientToken": str,
        "description": NotRequired[str],
        "status": NotRequired[LifecyclePolicyStatusType],
    },
)
CreateLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "CreateLifecyclePolicyRequestRequestTypeDef",
    {
        "name": str,
        "executionRole": str,
        "resourceType": LifecyclePolicyResourceTypeType,
        "policyDetails": Sequence[LifecyclePolicyDetailUnionTypeDef],
        "resourceSelection": LifecyclePolicyResourceSelectionTypeDef,
        "clientToken": str,
        "description": NotRequired[str],
        "status": NotRequired[LifecyclePolicyStatusType],
        "tags": NotRequired[Mapping[str, str]],
    },
)
