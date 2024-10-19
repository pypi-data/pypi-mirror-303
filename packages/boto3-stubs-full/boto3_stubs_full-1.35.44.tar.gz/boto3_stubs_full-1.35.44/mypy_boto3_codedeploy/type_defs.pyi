"""
Type annotations for codedeploy service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/type_defs/)

Usage::

    ```python
    from mypy_boto3_codedeploy.type_defs import TagTypeDef

    data: TagTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    ApplicationRevisionSortByType,
    AutoRollbackEventType,
    BundleTypeType,
    ComputePlatformType,
    DeploymentCreatorType,
    DeploymentOptionType,
    DeploymentReadyActionType,
    DeploymentStatusType,
    DeploymentTargetTypeType,
    DeploymentTypeType,
    DeploymentWaitTypeType,
    EC2TagFilterTypeType,
    ErrorCodeType,
    FileExistsBehaviorType,
    GreenFleetProvisioningActionType,
    InstanceActionType,
    InstanceStatusType,
    InstanceTypeType,
    LifecycleErrorCodeType,
    LifecycleEventStatusType,
    ListStateFilterActionType,
    MinimumHealthyHostsPerZoneTypeType,
    MinimumHealthyHostsTypeType,
    OutdatedInstancesStrategyType,
    RegistrationStatusType,
    RevisionLocationTypeType,
    SortOrderType,
    StopStatusType,
    TagFilterTypeType,
    TargetFilterNameType,
    TargetLabelType,
    TargetStatusType,
    TrafficRoutingTypeType,
    TriggerEventTypeType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "TagTypeDef",
    "AlarmTypeDef",
    "AppSpecContentTypeDef",
    "ApplicationInfoTypeDef",
    "AutoRollbackConfigurationOutputTypeDef",
    "AutoRollbackConfigurationTypeDef",
    "AutoScalingGroupTypeDef",
    "ResponseMetadataTypeDef",
    "BatchGetApplicationsInputRequestTypeDef",
    "BatchGetDeploymentGroupsInputRequestTypeDef",
    "BatchGetDeploymentInstancesInputRequestTypeDef",
    "BatchGetDeploymentTargetsInputRequestTypeDef",
    "BatchGetDeploymentsInputRequestTypeDef",
    "BatchGetOnPremisesInstancesInputRequestTypeDef",
    "BlueInstanceTerminationOptionTypeDef",
    "DeploymentReadyOptionTypeDef",
    "GreenFleetProvisioningOptionTypeDef",
    "ContinueDeploymentInputRequestTypeDef",
    "MinimumHealthyHostsTypeDef",
    "DeploymentStyleTypeDef",
    "EC2TagFilterTypeDef",
    "ECSServiceTypeDef",
    "TagFilterTypeDef",
    "DeleteApplicationInputRequestTypeDef",
    "DeleteDeploymentConfigInputRequestTypeDef",
    "DeleteDeploymentGroupInputRequestTypeDef",
    "DeleteGitHubAccountTokenInputRequestTypeDef",
    "DeleteResourcesByExternalIdInputRequestTypeDef",
    "LastDeploymentInfoTypeDef",
    "TriggerConfigOutputTypeDef",
    "DeploymentOverviewTypeDef",
    "ErrorInformationTypeDef",
    "RelatedDeploymentsTypeDef",
    "RollbackInfoTypeDef",
    "DeregisterOnPremisesInstanceInputRequestTypeDef",
    "DiagnosticsTypeDef",
    "TargetGroupInfoTypeDef",
    "ELBInfoTypeDef",
    "GenericRevisionInfoTypeDef",
    "GetApplicationInputRequestTypeDef",
    "GetDeploymentConfigInputRequestTypeDef",
    "GetDeploymentGroupInputRequestTypeDef",
    "WaiterConfigTypeDef",
    "GetDeploymentInputRequestTypeDef",
    "GetDeploymentInstanceInputRequestTypeDef",
    "GetDeploymentTargetInputRequestTypeDef",
    "GetOnPremisesInstanceInputRequestTypeDef",
    "GitHubLocationTypeDef",
    "LambdaFunctionInfoTypeDef",
    "PaginatorConfigTypeDef",
    "ListApplicationRevisionsInputRequestTypeDef",
    "ListApplicationsInputRequestTypeDef",
    "ListDeploymentConfigsInputRequestTypeDef",
    "ListDeploymentGroupsInputRequestTypeDef",
    "ListDeploymentInstancesInputRequestTypeDef",
    "ListDeploymentTargetsInputRequestTypeDef",
    "ListGitHubAccountTokenNamesInputRequestTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "MinimumHealthyHostsPerZoneTypeDef",
    "PutLifecycleEventHookExecutionStatusInputRequestTypeDef",
    "RawStringTypeDef",
    "RegisterOnPremisesInstanceInputRequestTypeDef",
    "S3LocationTypeDef",
    "SkipWaitTimeForInstanceTerminationInputRequestTypeDef",
    "StopDeploymentInputRequestTypeDef",
    "TrafficRouteOutputTypeDef",
    "TimeBasedCanaryTypeDef",
    "TimeBasedLinearTypeDef",
    "TimestampTypeDef",
    "TrafficRouteTypeDef",
    "TriggerConfigTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateApplicationInputRequestTypeDef",
    "AddTagsToOnPremisesInstancesInputRequestTypeDef",
    "CreateApplicationInputRequestTypeDef",
    "InstanceInfoTypeDef",
    "RemoveTagsFromOnPremisesInstancesInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "AlarmConfigurationOutputTypeDef",
    "AlarmConfigurationTypeDef",
    "BatchGetApplicationsOutputTypeDef",
    "CreateApplicationOutputTypeDef",
    "CreateDeploymentConfigOutputTypeDef",
    "CreateDeploymentGroupOutputTypeDef",
    "CreateDeploymentOutputTypeDef",
    "DeleteDeploymentGroupOutputTypeDef",
    "DeleteGitHubAccountTokenOutputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetApplicationOutputTypeDef",
    "ListApplicationsOutputTypeDef",
    "ListDeploymentConfigsOutputTypeDef",
    "ListDeploymentGroupsOutputTypeDef",
    "ListDeploymentInstancesOutputTypeDef",
    "ListDeploymentTargetsOutputTypeDef",
    "ListDeploymentsOutputTypeDef",
    "ListGitHubAccountTokenNamesOutputTypeDef",
    "ListOnPremisesInstancesOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "PutLifecycleEventHookExecutionStatusOutputTypeDef",
    "StopDeploymentOutputTypeDef",
    "UpdateDeploymentGroupOutputTypeDef",
    "BlueGreenDeploymentConfigurationTypeDef",
    "EC2TagSetOutputTypeDef",
    "EC2TagSetTypeDef",
    "ListOnPremisesInstancesInputRequestTypeDef",
    "OnPremisesTagSetOutputTypeDef",
    "OnPremisesTagSetTypeDef",
    "LifecycleEventTypeDef",
    "ECSTaskSetTypeDef",
    "GetDeploymentInputDeploymentSuccessfulWaitTypeDef",
    "ListApplicationRevisionsInputListApplicationRevisionsPaginateTypeDef",
    "ListApplicationsInputListApplicationsPaginateTypeDef",
    "ListDeploymentConfigsInputListDeploymentConfigsPaginateTypeDef",
    "ListDeploymentGroupsInputListDeploymentGroupsPaginateTypeDef",
    "ListDeploymentInstancesInputListDeploymentInstancesPaginateTypeDef",
    "ListDeploymentTargetsInputListDeploymentTargetsPaginateTypeDef",
    "ListGitHubAccountTokenNamesInputListGitHubAccountTokenNamesPaginateTypeDef",
    "ListOnPremisesInstancesInputListOnPremisesInstancesPaginateTypeDef",
    "ZonalConfigTypeDef",
    "RevisionLocationTypeDef",
    "TargetGroupPairInfoOutputTypeDef",
    "TrafficRoutingConfigTypeDef",
    "TimeRangeTypeDef",
    "TrafficRouteUnionTypeDef",
    "TriggerConfigUnionTypeDef",
    "BatchGetOnPremisesInstancesOutputTypeDef",
    "GetOnPremisesInstanceOutputTypeDef",
    "TargetInstancesOutputTypeDef",
    "EC2TagSetUnionTypeDef",
    "CloudFormationTargetTypeDef",
    "InstanceSummaryTypeDef",
    "InstanceTargetTypeDef",
    "LambdaTargetTypeDef",
    "ECSTargetTypeDef",
    "BatchGetApplicationRevisionsInputRequestTypeDef",
    "GetApplicationRevisionInputRequestTypeDef",
    "GetApplicationRevisionOutputTypeDef",
    "ListApplicationRevisionsOutputTypeDef",
    "RegisterApplicationRevisionInputRequestTypeDef",
    "RevisionInfoTypeDef",
    "LoadBalancerInfoOutputTypeDef",
    "CreateDeploymentConfigInputRequestTypeDef",
    "DeploymentConfigInfoTypeDef",
    "ListDeploymentsInputListDeploymentsPaginateTypeDef",
    "ListDeploymentsInputRequestTypeDef",
    "TargetGroupPairInfoTypeDef",
    "TargetInstancesTypeDef",
    "BatchGetDeploymentInstancesOutputTypeDef",
    "GetDeploymentInstanceOutputTypeDef",
    "DeploymentTargetTypeDef",
    "BatchGetApplicationRevisionsOutputTypeDef",
    "DeploymentGroupInfoTypeDef",
    "DeploymentInfoTypeDef",
    "GetDeploymentConfigOutputTypeDef",
    "TargetGroupPairInfoUnionTypeDef",
    "CreateDeploymentInputRequestTypeDef",
    "BatchGetDeploymentTargetsOutputTypeDef",
    "GetDeploymentTargetOutputTypeDef",
    "BatchGetDeploymentGroupsOutputTypeDef",
    "GetDeploymentGroupOutputTypeDef",
    "BatchGetDeploymentsOutputTypeDef",
    "GetDeploymentOutputTypeDef",
    "LoadBalancerInfoTypeDef",
    "CreateDeploymentGroupInputRequestTypeDef",
    "UpdateDeploymentGroupInputRequestTypeDef",
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
AlarmTypeDef = TypedDict(
    "AlarmTypeDef",
    {
        "name": NotRequired[str],
    },
)
AppSpecContentTypeDef = TypedDict(
    "AppSpecContentTypeDef",
    {
        "content": NotRequired[str],
        "sha256": NotRequired[str],
    },
)
ApplicationInfoTypeDef = TypedDict(
    "ApplicationInfoTypeDef",
    {
        "applicationId": NotRequired[str],
        "applicationName": NotRequired[str],
        "createTime": NotRequired[datetime],
        "linkedToGitHub": NotRequired[bool],
        "gitHubAccountName": NotRequired[str],
        "computePlatform": NotRequired[ComputePlatformType],
    },
)
AutoRollbackConfigurationOutputTypeDef = TypedDict(
    "AutoRollbackConfigurationOutputTypeDef",
    {
        "enabled": NotRequired[bool],
        "events": NotRequired[List[AutoRollbackEventType]],
    },
)
AutoRollbackConfigurationTypeDef = TypedDict(
    "AutoRollbackConfigurationTypeDef",
    {
        "enabled": NotRequired[bool],
        "events": NotRequired[Sequence[AutoRollbackEventType]],
    },
)
AutoScalingGroupTypeDef = TypedDict(
    "AutoScalingGroupTypeDef",
    {
        "name": NotRequired[str],
        "hook": NotRequired[str],
        "terminationHook": NotRequired[str],
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
BatchGetApplicationsInputRequestTypeDef = TypedDict(
    "BatchGetApplicationsInputRequestTypeDef",
    {
        "applicationNames": Sequence[str],
    },
)
BatchGetDeploymentGroupsInputRequestTypeDef = TypedDict(
    "BatchGetDeploymentGroupsInputRequestTypeDef",
    {
        "applicationName": str,
        "deploymentGroupNames": Sequence[str],
    },
)
BatchGetDeploymentInstancesInputRequestTypeDef = TypedDict(
    "BatchGetDeploymentInstancesInputRequestTypeDef",
    {
        "deploymentId": str,
        "instanceIds": Sequence[str],
    },
)
BatchGetDeploymentTargetsInputRequestTypeDef = TypedDict(
    "BatchGetDeploymentTargetsInputRequestTypeDef",
    {
        "deploymentId": str,
        "targetIds": Sequence[str],
    },
)
BatchGetDeploymentsInputRequestTypeDef = TypedDict(
    "BatchGetDeploymentsInputRequestTypeDef",
    {
        "deploymentIds": Sequence[str],
    },
)
BatchGetOnPremisesInstancesInputRequestTypeDef = TypedDict(
    "BatchGetOnPremisesInstancesInputRequestTypeDef",
    {
        "instanceNames": Sequence[str],
    },
)
BlueInstanceTerminationOptionTypeDef = TypedDict(
    "BlueInstanceTerminationOptionTypeDef",
    {
        "action": NotRequired[InstanceActionType],
        "terminationWaitTimeInMinutes": NotRequired[int],
    },
)
DeploymentReadyOptionTypeDef = TypedDict(
    "DeploymentReadyOptionTypeDef",
    {
        "actionOnTimeout": NotRequired[DeploymentReadyActionType],
        "waitTimeInMinutes": NotRequired[int],
    },
)
GreenFleetProvisioningOptionTypeDef = TypedDict(
    "GreenFleetProvisioningOptionTypeDef",
    {
        "action": NotRequired[GreenFleetProvisioningActionType],
    },
)
ContinueDeploymentInputRequestTypeDef = TypedDict(
    "ContinueDeploymentInputRequestTypeDef",
    {
        "deploymentId": NotRequired[str],
        "deploymentWaitType": NotRequired[DeploymentWaitTypeType],
    },
)
MinimumHealthyHostsTypeDef = TypedDict(
    "MinimumHealthyHostsTypeDef",
    {
        "type": NotRequired[MinimumHealthyHostsTypeType],
        "value": NotRequired[int],
    },
)
DeploymentStyleTypeDef = TypedDict(
    "DeploymentStyleTypeDef",
    {
        "deploymentType": NotRequired[DeploymentTypeType],
        "deploymentOption": NotRequired[DeploymentOptionType],
    },
)
EC2TagFilterTypeDef = TypedDict(
    "EC2TagFilterTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
        "Type": NotRequired[EC2TagFilterTypeType],
    },
)
ECSServiceTypeDef = TypedDict(
    "ECSServiceTypeDef",
    {
        "serviceName": NotRequired[str],
        "clusterName": NotRequired[str],
    },
)
TagFilterTypeDef = TypedDict(
    "TagFilterTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
        "Type": NotRequired[TagFilterTypeType],
    },
)
DeleteApplicationInputRequestTypeDef = TypedDict(
    "DeleteApplicationInputRequestTypeDef",
    {
        "applicationName": str,
    },
)
DeleteDeploymentConfigInputRequestTypeDef = TypedDict(
    "DeleteDeploymentConfigInputRequestTypeDef",
    {
        "deploymentConfigName": str,
    },
)
DeleteDeploymentGroupInputRequestTypeDef = TypedDict(
    "DeleteDeploymentGroupInputRequestTypeDef",
    {
        "applicationName": str,
        "deploymentGroupName": str,
    },
)
DeleteGitHubAccountTokenInputRequestTypeDef = TypedDict(
    "DeleteGitHubAccountTokenInputRequestTypeDef",
    {
        "tokenName": NotRequired[str],
    },
)
DeleteResourcesByExternalIdInputRequestTypeDef = TypedDict(
    "DeleteResourcesByExternalIdInputRequestTypeDef",
    {
        "externalId": NotRequired[str],
    },
)
LastDeploymentInfoTypeDef = TypedDict(
    "LastDeploymentInfoTypeDef",
    {
        "deploymentId": NotRequired[str],
        "status": NotRequired[DeploymentStatusType],
        "endTime": NotRequired[datetime],
        "createTime": NotRequired[datetime],
    },
)
TriggerConfigOutputTypeDef = TypedDict(
    "TriggerConfigOutputTypeDef",
    {
        "triggerName": NotRequired[str],
        "triggerTargetArn": NotRequired[str],
        "triggerEvents": NotRequired[List[TriggerEventTypeType]],
    },
)
DeploymentOverviewTypeDef = TypedDict(
    "DeploymentOverviewTypeDef",
    {
        "Pending": NotRequired[int],
        "InProgress": NotRequired[int],
        "Succeeded": NotRequired[int],
        "Failed": NotRequired[int],
        "Skipped": NotRequired[int],
        "Ready": NotRequired[int],
    },
)
ErrorInformationTypeDef = TypedDict(
    "ErrorInformationTypeDef",
    {
        "code": NotRequired[ErrorCodeType],
        "message": NotRequired[str],
    },
)
RelatedDeploymentsTypeDef = TypedDict(
    "RelatedDeploymentsTypeDef",
    {
        "autoUpdateOutdatedInstancesRootDeploymentId": NotRequired[str],
        "autoUpdateOutdatedInstancesDeploymentIds": NotRequired[List[str]],
    },
)
RollbackInfoTypeDef = TypedDict(
    "RollbackInfoTypeDef",
    {
        "rollbackDeploymentId": NotRequired[str],
        "rollbackTriggeringDeploymentId": NotRequired[str],
        "rollbackMessage": NotRequired[str],
    },
)
DeregisterOnPremisesInstanceInputRequestTypeDef = TypedDict(
    "DeregisterOnPremisesInstanceInputRequestTypeDef",
    {
        "instanceName": str,
    },
)
DiagnosticsTypeDef = TypedDict(
    "DiagnosticsTypeDef",
    {
        "errorCode": NotRequired[LifecycleErrorCodeType],
        "scriptName": NotRequired[str],
        "message": NotRequired[str],
        "logTail": NotRequired[str],
    },
)
TargetGroupInfoTypeDef = TypedDict(
    "TargetGroupInfoTypeDef",
    {
        "name": NotRequired[str],
    },
)
ELBInfoTypeDef = TypedDict(
    "ELBInfoTypeDef",
    {
        "name": NotRequired[str],
    },
)
GenericRevisionInfoTypeDef = TypedDict(
    "GenericRevisionInfoTypeDef",
    {
        "description": NotRequired[str],
        "deploymentGroups": NotRequired[List[str]],
        "firstUsedTime": NotRequired[datetime],
        "lastUsedTime": NotRequired[datetime],
        "registerTime": NotRequired[datetime],
    },
)
GetApplicationInputRequestTypeDef = TypedDict(
    "GetApplicationInputRequestTypeDef",
    {
        "applicationName": str,
    },
)
GetDeploymentConfigInputRequestTypeDef = TypedDict(
    "GetDeploymentConfigInputRequestTypeDef",
    {
        "deploymentConfigName": str,
    },
)
GetDeploymentGroupInputRequestTypeDef = TypedDict(
    "GetDeploymentGroupInputRequestTypeDef",
    {
        "applicationName": str,
        "deploymentGroupName": str,
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
GetDeploymentInputRequestTypeDef = TypedDict(
    "GetDeploymentInputRequestTypeDef",
    {
        "deploymentId": str,
    },
)
GetDeploymentInstanceInputRequestTypeDef = TypedDict(
    "GetDeploymentInstanceInputRequestTypeDef",
    {
        "deploymentId": str,
        "instanceId": str,
    },
)
GetDeploymentTargetInputRequestTypeDef = TypedDict(
    "GetDeploymentTargetInputRequestTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
    },
)
GetOnPremisesInstanceInputRequestTypeDef = TypedDict(
    "GetOnPremisesInstanceInputRequestTypeDef",
    {
        "instanceName": str,
    },
)
GitHubLocationTypeDef = TypedDict(
    "GitHubLocationTypeDef",
    {
        "repository": NotRequired[str],
        "commitId": NotRequired[str],
    },
)
LambdaFunctionInfoTypeDef = TypedDict(
    "LambdaFunctionInfoTypeDef",
    {
        "functionName": NotRequired[str],
        "functionAlias": NotRequired[str],
        "currentVersion": NotRequired[str],
        "targetVersion": NotRequired[str],
        "targetVersionWeight": NotRequired[float],
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
ListApplicationRevisionsInputRequestTypeDef = TypedDict(
    "ListApplicationRevisionsInputRequestTypeDef",
    {
        "applicationName": str,
        "sortBy": NotRequired[ApplicationRevisionSortByType],
        "sortOrder": NotRequired[SortOrderType],
        "s3Bucket": NotRequired[str],
        "s3KeyPrefix": NotRequired[str],
        "deployed": NotRequired[ListStateFilterActionType],
        "nextToken": NotRequired[str],
    },
)
ListApplicationsInputRequestTypeDef = TypedDict(
    "ListApplicationsInputRequestTypeDef",
    {
        "nextToken": NotRequired[str],
    },
)
ListDeploymentConfigsInputRequestTypeDef = TypedDict(
    "ListDeploymentConfigsInputRequestTypeDef",
    {
        "nextToken": NotRequired[str],
    },
)
ListDeploymentGroupsInputRequestTypeDef = TypedDict(
    "ListDeploymentGroupsInputRequestTypeDef",
    {
        "applicationName": str,
        "nextToken": NotRequired[str],
    },
)
ListDeploymentInstancesInputRequestTypeDef = TypedDict(
    "ListDeploymentInstancesInputRequestTypeDef",
    {
        "deploymentId": str,
        "nextToken": NotRequired[str],
        "instanceStatusFilter": NotRequired[Sequence[InstanceStatusType]],
        "instanceTypeFilter": NotRequired[Sequence[InstanceTypeType]],
    },
)
ListDeploymentTargetsInputRequestTypeDef = TypedDict(
    "ListDeploymentTargetsInputRequestTypeDef",
    {
        "deploymentId": str,
        "nextToken": NotRequired[str],
        "targetFilters": NotRequired[Mapping[TargetFilterNameType, Sequence[str]]],
    },
)
ListGitHubAccountTokenNamesInputRequestTypeDef = TypedDict(
    "ListGitHubAccountTokenNamesInputRequestTypeDef",
    {
        "nextToken": NotRequired[str],
    },
)
ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "NextToken": NotRequired[str],
    },
)
MinimumHealthyHostsPerZoneTypeDef = TypedDict(
    "MinimumHealthyHostsPerZoneTypeDef",
    {
        "type": NotRequired[MinimumHealthyHostsPerZoneTypeType],
        "value": NotRequired[int],
    },
)
PutLifecycleEventHookExecutionStatusInputRequestTypeDef = TypedDict(
    "PutLifecycleEventHookExecutionStatusInputRequestTypeDef",
    {
        "deploymentId": NotRequired[str],
        "lifecycleEventHookExecutionId": NotRequired[str],
        "status": NotRequired[LifecycleEventStatusType],
    },
)
RawStringTypeDef = TypedDict(
    "RawStringTypeDef",
    {
        "content": NotRequired[str],
        "sha256": NotRequired[str],
    },
)
RegisterOnPremisesInstanceInputRequestTypeDef = TypedDict(
    "RegisterOnPremisesInstanceInputRequestTypeDef",
    {
        "instanceName": str,
        "iamSessionArn": NotRequired[str],
        "iamUserArn": NotRequired[str],
    },
)
S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucket": NotRequired[str],
        "key": NotRequired[str],
        "bundleType": NotRequired[BundleTypeType],
        "version": NotRequired[str],
        "eTag": NotRequired[str],
    },
)
SkipWaitTimeForInstanceTerminationInputRequestTypeDef = TypedDict(
    "SkipWaitTimeForInstanceTerminationInputRequestTypeDef",
    {
        "deploymentId": NotRequired[str],
    },
)
StopDeploymentInputRequestTypeDef = TypedDict(
    "StopDeploymentInputRequestTypeDef",
    {
        "deploymentId": str,
        "autoRollbackEnabled": NotRequired[bool],
    },
)
TrafficRouteOutputTypeDef = TypedDict(
    "TrafficRouteOutputTypeDef",
    {
        "listenerArns": NotRequired[List[str]],
    },
)
TimeBasedCanaryTypeDef = TypedDict(
    "TimeBasedCanaryTypeDef",
    {
        "canaryPercentage": NotRequired[int],
        "canaryInterval": NotRequired[int],
    },
)
TimeBasedLinearTypeDef = TypedDict(
    "TimeBasedLinearTypeDef",
    {
        "linearPercentage": NotRequired[int],
        "linearInterval": NotRequired[int],
    },
)
TimestampTypeDef = Union[datetime, str]
TrafficRouteTypeDef = TypedDict(
    "TrafficRouteTypeDef",
    {
        "listenerArns": NotRequired[Sequence[str]],
    },
)
TriggerConfigTypeDef = TypedDict(
    "TriggerConfigTypeDef",
    {
        "triggerName": NotRequired[str],
        "triggerTargetArn": NotRequired[str],
        "triggerEvents": NotRequired[Sequence[TriggerEventTypeType]],
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateApplicationInputRequestTypeDef = TypedDict(
    "UpdateApplicationInputRequestTypeDef",
    {
        "applicationName": NotRequired[str],
        "newApplicationName": NotRequired[str],
    },
)
AddTagsToOnPremisesInstancesInputRequestTypeDef = TypedDict(
    "AddTagsToOnPremisesInstancesInputRequestTypeDef",
    {
        "tags": Sequence[TagTypeDef],
        "instanceNames": Sequence[str],
    },
)
CreateApplicationInputRequestTypeDef = TypedDict(
    "CreateApplicationInputRequestTypeDef",
    {
        "applicationName": str,
        "computePlatform": NotRequired[ComputePlatformType],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
InstanceInfoTypeDef = TypedDict(
    "InstanceInfoTypeDef",
    {
        "instanceName": NotRequired[str],
        "iamSessionArn": NotRequired[str],
        "iamUserArn": NotRequired[str],
        "instanceArn": NotRequired[str],
        "registerTime": NotRequired[datetime],
        "deregisterTime": NotRequired[datetime],
        "tags": NotRequired[List[TagTypeDef]],
    },
)
RemoveTagsFromOnPremisesInstancesInputRequestTypeDef = TypedDict(
    "RemoveTagsFromOnPremisesInstancesInputRequestTypeDef",
    {
        "tags": Sequence[TagTypeDef],
        "instanceNames": Sequence[str],
    },
)
TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
AlarmConfigurationOutputTypeDef = TypedDict(
    "AlarmConfigurationOutputTypeDef",
    {
        "enabled": NotRequired[bool],
        "ignorePollAlarmFailure": NotRequired[bool],
        "alarms": NotRequired[List[AlarmTypeDef]],
    },
)
AlarmConfigurationTypeDef = TypedDict(
    "AlarmConfigurationTypeDef",
    {
        "enabled": NotRequired[bool],
        "ignorePollAlarmFailure": NotRequired[bool],
        "alarms": NotRequired[Sequence[AlarmTypeDef]],
    },
)
BatchGetApplicationsOutputTypeDef = TypedDict(
    "BatchGetApplicationsOutputTypeDef",
    {
        "applicationsInfo": List[ApplicationInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateApplicationOutputTypeDef = TypedDict(
    "CreateApplicationOutputTypeDef",
    {
        "applicationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDeploymentConfigOutputTypeDef = TypedDict(
    "CreateDeploymentConfigOutputTypeDef",
    {
        "deploymentConfigId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDeploymentGroupOutputTypeDef = TypedDict(
    "CreateDeploymentGroupOutputTypeDef",
    {
        "deploymentGroupId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDeploymentOutputTypeDef = TypedDict(
    "CreateDeploymentOutputTypeDef",
    {
        "deploymentId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDeploymentGroupOutputTypeDef = TypedDict(
    "DeleteDeploymentGroupOutputTypeDef",
    {
        "hooksNotCleanedUp": List[AutoScalingGroupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteGitHubAccountTokenOutputTypeDef = TypedDict(
    "DeleteGitHubAccountTokenOutputTypeDef",
    {
        "tokenName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetApplicationOutputTypeDef = TypedDict(
    "GetApplicationOutputTypeDef",
    {
        "application": ApplicationInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListApplicationsOutputTypeDef = TypedDict(
    "ListApplicationsOutputTypeDef",
    {
        "applications": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDeploymentConfigsOutputTypeDef = TypedDict(
    "ListDeploymentConfigsOutputTypeDef",
    {
        "deploymentConfigsList": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDeploymentGroupsOutputTypeDef = TypedDict(
    "ListDeploymentGroupsOutputTypeDef",
    {
        "applicationName": str,
        "deploymentGroups": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDeploymentInstancesOutputTypeDef = TypedDict(
    "ListDeploymentInstancesOutputTypeDef",
    {
        "instancesList": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDeploymentTargetsOutputTypeDef = TypedDict(
    "ListDeploymentTargetsOutputTypeDef",
    {
        "targetIds": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDeploymentsOutputTypeDef = TypedDict(
    "ListDeploymentsOutputTypeDef",
    {
        "deployments": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListGitHubAccountTokenNamesOutputTypeDef = TypedDict(
    "ListGitHubAccountTokenNamesOutputTypeDef",
    {
        "tokenNameList": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListOnPremisesInstancesOutputTypeDef = TypedDict(
    "ListOnPremisesInstancesOutputTypeDef",
    {
        "instanceNames": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PutLifecycleEventHookExecutionStatusOutputTypeDef = TypedDict(
    "PutLifecycleEventHookExecutionStatusOutputTypeDef",
    {
        "lifecycleEventHookExecutionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopDeploymentOutputTypeDef = TypedDict(
    "StopDeploymentOutputTypeDef",
    {
        "status": StopStatusType,
        "statusMessage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDeploymentGroupOutputTypeDef = TypedDict(
    "UpdateDeploymentGroupOutputTypeDef",
    {
        "hooksNotCleanedUp": List[AutoScalingGroupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BlueGreenDeploymentConfigurationTypeDef = TypedDict(
    "BlueGreenDeploymentConfigurationTypeDef",
    {
        "terminateBlueInstancesOnDeploymentSuccess": NotRequired[
            BlueInstanceTerminationOptionTypeDef
        ],
        "deploymentReadyOption": NotRequired[DeploymentReadyOptionTypeDef],
        "greenFleetProvisioningOption": NotRequired[GreenFleetProvisioningOptionTypeDef],
    },
)
EC2TagSetOutputTypeDef = TypedDict(
    "EC2TagSetOutputTypeDef",
    {
        "ec2TagSetList": NotRequired[List[List[EC2TagFilterTypeDef]]],
    },
)
EC2TagSetTypeDef = TypedDict(
    "EC2TagSetTypeDef",
    {
        "ec2TagSetList": NotRequired[Sequence[Sequence[EC2TagFilterTypeDef]]],
    },
)
ListOnPremisesInstancesInputRequestTypeDef = TypedDict(
    "ListOnPremisesInstancesInputRequestTypeDef",
    {
        "registrationStatus": NotRequired[RegistrationStatusType],
        "tagFilters": NotRequired[Sequence[TagFilterTypeDef]],
        "nextToken": NotRequired[str],
    },
)
OnPremisesTagSetOutputTypeDef = TypedDict(
    "OnPremisesTagSetOutputTypeDef",
    {
        "onPremisesTagSetList": NotRequired[List[List[TagFilterTypeDef]]],
    },
)
OnPremisesTagSetTypeDef = TypedDict(
    "OnPremisesTagSetTypeDef",
    {
        "onPremisesTagSetList": NotRequired[Sequence[Sequence[TagFilterTypeDef]]],
    },
)
LifecycleEventTypeDef = TypedDict(
    "LifecycleEventTypeDef",
    {
        "lifecycleEventName": NotRequired[str],
        "diagnostics": NotRequired[DiagnosticsTypeDef],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
        "status": NotRequired[LifecycleEventStatusType],
    },
)
ECSTaskSetTypeDef = TypedDict(
    "ECSTaskSetTypeDef",
    {
        "identifer": NotRequired[str],
        "desiredCount": NotRequired[int],
        "pendingCount": NotRequired[int],
        "runningCount": NotRequired[int],
        "status": NotRequired[str],
        "trafficWeight": NotRequired[float],
        "targetGroup": NotRequired[TargetGroupInfoTypeDef],
        "taskSetLabel": NotRequired[TargetLabelType],
    },
)
GetDeploymentInputDeploymentSuccessfulWaitTypeDef = TypedDict(
    "GetDeploymentInputDeploymentSuccessfulWaitTypeDef",
    {
        "deploymentId": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
ListApplicationRevisionsInputListApplicationRevisionsPaginateTypeDef = TypedDict(
    "ListApplicationRevisionsInputListApplicationRevisionsPaginateTypeDef",
    {
        "applicationName": str,
        "sortBy": NotRequired[ApplicationRevisionSortByType],
        "sortOrder": NotRequired[SortOrderType],
        "s3Bucket": NotRequired[str],
        "s3KeyPrefix": NotRequired[str],
        "deployed": NotRequired[ListStateFilterActionType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListApplicationsInputListApplicationsPaginateTypeDef = TypedDict(
    "ListApplicationsInputListApplicationsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDeploymentConfigsInputListDeploymentConfigsPaginateTypeDef = TypedDict(
    "ListDeploymentConfigsInputListDeploymentConfigsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDeploymentGroupsInputListDeploymentGroupsPaginateTypeDef = TypedDict(
    "ListDeploymentGroupsInputListDeploymentGroupsPaginateTypeDef",
    {
        "applicationName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDeploymentInstancesInputListDeploymentInstancesPaginateTypeDef = TypedDict(
    "ListDeploymentInstancesInputListDeploymentInstancesPaginateTypeDef",
    {
        "deploymentId": str,
        "instanceStatusFilter": NotRequired[Sequence[InstanceStatusType]],
        "instanceTypeFilter": NotRequired[Sequence[InstanceTypeType]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDeploymentTargetsInputListDeploymentTargetsPaginateTypeDef = TypedDict(
    "ListDeploymentTargetsInputListDeploymentTargetsPaginateTypeDef",
    {
        "deploymentId": str,
        "targetFilters": NotRequired[Mapping[TargetFilterNameType, Sequence[str]]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGitHubAccountTokenNamesInputListGitHubAccountTokenNamesPaginateTypeDef = TypedDict(
    "ListGitHubAccountTokenNamesInputListGitHubAccountTokenNamesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOnPremisesInstancesInputListOnPremisesInstancesPaginateTypeDef = TypedDict(
    "ListOnPremisesInstancesInputListOnPremisesInstancesPaginateTypeDef",
    {
        "registrationStatus": NotRequired[RegistrationStatusType],
        "tagFilters": NotRequired[Sequence[TagFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ZonalConfigTypeDef = TypedDict(
    "ZonalConfigTypeDef",
    {
        "firstZoneMonitorDurationInSeconds": NotRequired[int],
        "monitorDurationInSeconds": NotRequired[int],
        "minimumHealthyHostsPerZone": NotRequired[MinimumHealthyHostsPerZoneTypeDef],
    },
)
RevisionLocationTypeDef = TypedDict(
    "RevisionLocationTypeDef",
    {
        "revisionType": NotRequired[RevisionLocationTypeType],
        "s3Location": NotRequired[S3LocationTypeDef],
        "gitHubLocation": NotRequired[GitHubLocationTypeDef],
        "string": NotRequired[RawStringTypeDef],
        "appSpecContent": NotRequired[AppSpecContentTypeDef],
    },
)
TargetGroupPairInfoOutputTypeDef = TypedDict(
    "TargetGroupPairInfoOutputTypeDef",
    {
        "targetGroups": NotRequired[List[TargetGroupInfoTypeDef]],
        "prodTrafficRoute": NotRequired[TrafficRouteOutputTypeDef],
        "testTrafficRoute": NotRequired[TrafficRouteOutputTypeDef],
    },
)
TrafficRoutingConfigTypeDef = TypedDict(
    "TrafficRoutingConfigTypeDef",
    {
        "type": NotRequired[TrafficRoutingTypeType],
        "timeBasedCanary": NotRequired[TimeBasedCanaryTypeDef],
        "timeBasedLinear": NotRequired[TimeBasedLinearTypeDef],
    },
)
TimeRangeTypeDef = TypedDict(
    "TimeRangeTypeDef",
    {
        "start": NotRequired[TimestampTypeDef],
        "end": NotRequired[TimestampTypeDef],
    },
)
TrafficRouteUnionTypeDef = Union[TrafficRouteTypeDef, TrafficRouteOutputTypeDef]
TriggerConfigUnionTypeDef = Union[TriggerConfigTypeDef, TriggerConfigOutputTypeDef]
BatchGetOnPremisesInstancesOutputTypeDef = TypedDict(
    "BatchGetOnPremisesInstancesOutputTypeDef",
    {
        "instanceInfos": List[InstanceInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetOnPremisesInstanceOutputTypeDef = TypedDict(
    "GetOnPremisesInstanceOutputTypeDef",
    {
        "instanceInfo": InstanceInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TargetInstancesOutputTypeDef = TypedDict(
    "TargetInstancesOutputTypeDef",
    {
        "tagFilters": NotRequired[List[EC2TagFilterTypeDef]],
        "autoScalingGroups": NotRequired[List[str]],
        "ec2TagSet": NotRequired[EC2TagSetOutputTypeDef],
    },
)
EC2TagSetUnionTypeDef = Union[EC2TagSetTypeDef, EC2TagSetOutputTypeDef]
CloudFormationTargetTypeDef = TypedDict(
    "CloudFormationTargetTypeDef",
    {
        "deploymentId": NotRequired[str],
        "targetId": NotRequired[str],
        "lastUpdatedAt": NotRequired[datetime],
        "lifecycleEvents": NotRequired[List[LifecycleEventTypeDef]],
        "status": NotRequired[TargetStatusType],
        "resourceType": NotRequired[str],
        "targetVersionWeight": NotRequired[float],
    },
)
InstanceSummaryTypeDef = TypedDict(
    "InstanceSummaryTypeDef",
    {
        "deploymentId": NotRequired[str],
        "instanceId": NotRequired[str],
        "status": NotRequired[InstanceStatusType],
        "lastUpdatedAt": NotRequired[datetime],
        "lifecycleEvents": NotRequired[List[LifecycleEventTypeDef]],
        "instanceType": NotRequired[InstanceTypeType],
    },
)
InstanceTargetTypeDef = TypedDict(
    "InstanceTargetTypeDef",
    {
        "deploymentId": NotRequired[str],
        "targetId": NotRequired[str],
        "targetArn": NotRequired[str],
        "status": NotRequired[TargetStatusType],
        "lastUpdatedAt": NotRequired[datetime],
        "lifecycleEvents": NotRequired[List[LifecycleEventTypeDef]],
        "instanceLabel": NotRequired[TargetLabelType],
    },
)
LambdaTargetTypeDef = TypedDict(
    "LambdaTargetTypeDef",
    {
        "deploymentId": NotRequired[str],
        "targetId": NotRequired[str],
        "targetArn": NotRequired[str],
        "status": NotRequired[TargetStatusType],
        "lastUpdatedAt": NotRequired[datetime],
        "lifecycleEvents": NotRequired[List[LifecycleEventTypeDef]],
        "lambdaFunctionInfo": NotRequired[LambdaFunctionInfoTypeDef],
    },
)
ECSTargetTypeDef = TypedDict(
    "ECSTargetTypeDef",
    {
        "deploymentId": NotRequired[str],
        "targetId": NotRequired[str],
        "targetArn": NotRequired[str],
        "lastUpdatedAt": NotRequired[datetime],
        "lifecycleEvents": NotRequired[List[LifecycleEventTypeDef]],
        "status": NotRequired[TargetStatusType],
        "taskSetsInfo": NotRequired[List[ECSTaskSetTypeDef]],
    },
)
BatchGetApplicationRevisionsInputRequestTypeDef = TypedDict(
    "BatchGetApplicationRevisionsInputRequestTypeDef",
    {
        "applicationName": str,
        "revisions": Sequence[RevisionLocationTypeDef],
    },
)
GetApplicationRevisionInputRequestTypeDef = TypedDict(
    "GetApplicationRevisionInputRequestTypeDef",
    {
        "applicationName": str,
        "revision": RevisionLocationTypeDef,
    },
)
GetApplicationRevisionOutputTypeDef = TypedDict(
    "GetApplicationRevisionOutputTypeDef",
    {
        "applicationName": str,
        "revision": RevisionLocationTypeDef,
        "revisionInfo": GenericRevisionInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListApplicationRevisionsOutputTypeDef = TypedDict(
    "ListApplicationRevisionsOutputTypeDef",
    {
        "revisions": List[RevisionLocationTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterApplicationRevisionInputRequestTypeDef = TypedDict(
    "RegisterApplicationRevisionInputRequestTypeDef",
    {
        "applicationName": str,
        "revision": RevisionLocationTypeDef,
        "description": NotRequired[str],
    },
)
RevisionInfoTypeDef = TypedDict(
    "RevisionInfoTypeDef",
    {
        "revisionLocation": NotRequired[RevisionLocationTypeDef],
        "genericRevisionInfo": NotRequired[GenericRevisionInfoTypeDef],
    },
)
LoadBalancerInfoOutputTypeDef = TypedDict(
    "LoadBalancerInfoOutputTypeDef",
    {
        "elbInfoList": NotRequired[List[ELBInfoTypeDef]],
        "targetGroupInfoList": NotRequired[List[TargetGroupInfoTypeDef]],
        "targetGroupPairInfoList": NotRequired[List[TargetGroupPairInfoOutputTypeDef]],
    },
)
CreateDeploymentConfigInputRequestTypeDef = TypedDict(
    "CreateDeploymentConfigInputRequestTypeDef",
    {
        "deploymentConfigName": str,
        "minimumHealthyHosts": NotRequired[MinimumHealthyHostsTypeDef],
        "trafficRoutingConfig": NotRequired[TrafficRoutingConfigTypeDef],
        "computePlatform": NotRequired[ComputePlatformType],
        "zonalConfig": NotRequired[ZonalConfigTypeDef],
    },
)
DeploymentConfigInfoTypeDef = TypedDict(
    "DeploymentConfigInfoTypeDef",
    {
        "deploymentConfigId": NotRequired[str],
        "deploymentConfigName": NotRequired[str],
        "minimumHealthyHosts": NotRequired[MinimumHealthyHostsTypeDef],
        "createTime": NotRequired[datetime],
        "computePlatform": NotRequired[ComputePlatformType],
        "trafficRoutingConfig": NotRequired[TrafficRoutingConfigTypeDef],
        "zonalConfig": NotRequired[ZonalConfigTypeDef],
    },
)
ListDeploymentsInputListDeploymentsPaginateTypeDef = TypedDict(
    "ListDeploymentsInputListDeploymentsPaginateTypeDef",
    {
        "applicationName": NotRequired[str],
        "deploymentGroupName": NotRequired[str],
        "externalId": NotRequired[str],
        "includeOnlyStatuses": NotRequired[Sequence[DeploymentStatusType]],
        "createTimeRange": NotRequired[TimeRangeTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDeploymentsInputRequestTypeDef = TypedDict(
    "ListDeploymentsInputRequestTypeDef",
    {
        "applicationName": NotRequired[str],
        "deploymentGroupName": NotRequired[str],
        "externalId": NotRequired[str],
        "includeOnlyStatuses": NotRequired[Sequence[DeploymentStatusType]],
        "createTimeRange": NotRequired[TimeRangeTypeDef],
        "nextToken": NotRequired[str],
    },
)
TargetGroupPairInfoTypeDef = TypedDict(
    "TargetGroupPairInfoTypeDef",
    {
        "targetGroups": NotRequired[Sequence[TargetGroupInfoTypeDef]],
        "prodTrafficRoute": NotRequired[TrafficRouteUnionTypeDef],
        "testTrafficRoute": NotRequired[TrafficRouteUnionTypeDef],
    },
)
TargetInstancesTypeDef = TypedDict(
    "TargetInstancesTypeDef",
    {
        "tagFilters": NotRequired[Sequence[EC2TagFilterTypeDef]],
        "autoScalingGroups": NotRequired[Sequence[str]],
        "ec2TagSet": NotRequired[EC2TagSetUnionTypeDef],
    },
)
BatchGetDeploymentInstancesOutputTypeDef = TypedDict(
    "BatchGetDeploymentInstancesOutputTypeDef",
    {
        "instancesSummary": List[InstanceSummaryTypeDef],
        "errorMessage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDeploymentInstanceOutputTypeDef = TypedDict(
    "GetDeploymentInstanceOutputTypeDef",
    {
        "instanceSummary": InstanceSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeploymentTargetTypeDef = TypedDict(
    "DeploymentTargetTypeDef",
    {
        "deploymentTargetType": NotRequired[DeploymentTargetTypeType],
        "instanceTarget": NotRequired[InstanceTargetTypeDef],
        "lambdaTarget": NotRequired[LambdaTargetTypeDef],
        "ecsTarget": NotRequired[ECSTargetTypeDef],
        "cloudFormationTarget": NotRequired[CloudFormationTargetTypeDef],
    },
)
BatchGetApplicationRevisionsOutputTypeDef = TypedDict(
    "BatchGetApplicationRevisionsOutputTypeDef",
    {
        "applicationName": str,
        "errorMessage": str,
        "revisions": List[RevisionInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeploymentGroupInfoTypeDef = TypedDict(
    "DeploymentGroupInfoTypeDef",
    {
        "applicationName": NotRequired[str],
        "deploymentGroupId": NotRequired[str],
        "deploymentGroupName": NotRequired[str],
        "deploymentConfigName": NotRequired[str],
        "ec2TagFilters": NotRequired[List[EC2TagFilterTypeDef]],
        "onPremisesInstanceTagFilters": NotRequired[List[TagFilterTypeDef]],
        "autoScalingGroups": NotRequired[List[AutoScalingGroupTypeDef]],
        "serviceRoleArn": NotRequired[str],
        "targetRevision": NotRequired[RevisionLocationTypeDef],
        "triggerConfigurations": NotRequired[List[TriggerConfigOutputTypeDef]],
        "alarmConfiguration": NotRequired[AlarmConfigurationOutputTypeDef],
        "autoRollbackConfiguration": NotRequired[AutoRollbackConfigurationOutputTypeDef],
        "deploymentStyle": NotRequired[DeploymentStyleTypeDef],
        "outdatedInstancesStrategy": NotRequired[OutdatedInstancesStrategyType],
        "blueGreenDeploymentConfiguration": NotRequired[BlueGreenDeploymentConfigurationTypeDef],
        "loadBalancerInfo": NotRequired[LoadBalancerInfoOutputTypeDef],
        "lastSuccessfulDeployment": NotRequired[LastDeploymentInfoTypeDef],
        "lastAttemptedDeployment": NotRequired[LastDeploymentInfoTypeDef],
        "ec2TagSet": NotRequired[EC2TagSetOutputTypeDef],
        "onPremisesTagSet": NotRequired[OnPremisesTagSetOutputTypeDef],
        "computePlatform": NotRequired[ComputePlatformType],
        "ecsServices": NotRequired[List[ECSServiceTypeDef]],
        "terminationHookEnabled": NotRequired[bool],
    },
)
DeploymentInfoTypeDef = TypedDict(
    "DeploymentInfoTypeDef",
    {
        "applicationName": NotRequired[str],
        "deploymentGroupName": NotRequired[str],
        "deploymentConfigName": NotRequired[str],
        "deploymentId": NotRequired[str],
        "previousRevision": NotRequired[RevisionLocationTypeDef],
        "revision": NotRequired[RevisionLocationTypeDef],
        "status": NotRequired[DeploymentStatusType],
        "errorInformation": NotRequired[ErrorInformationTypeDef],
        "createTime": NotRequired[datetime],
        "startTime": NotRequired[datetime],
        "completeTime": NotRequired[datetime],
        "deploymentOverview": NotRequired[DeploymentOverviewTypeDef],
        "description": NotRequired[str],
        "creator": NotRequired[DeploymentCreatorType],
        "ignoreApplicationStopFailures": NotRequired[bool],
        "autoRollbackConfiguration": NotRequired[AutoRollbackConfigurationOutputTypeDef],
        "updateOutdatedInstancesOnly": NotRequired[bool],
        "rollbackInfo": NotRequired[RollbackInfoTypeDef],
        "deploymentStyle": NotRequired[DeploymentStyleTypeDef],
        "targetInstances": NotRequired[TargetInstancesOutputTypeDef],
        "instanceTerminationWaitTimeStarted": NotRequired[bool],
        "blueGreenDeploymentConfiguration": NotRequired[BlueGreenDeploymentConfigurationTypeDef],
        "loadBalancerInfo": NotRequired[LoadBalancerInfoOutputTypeDef],
        "additionalDeploymentStatusInfo": NotRequired[str],
        "fileExistsBehavior": NotRequired[FileExistsBehaviorType],
        "deploymentStatusMessages": NotRequired[List[str]],
        "computePlatform": NotRequired[ComputePlatformType],
        "externalId": NotRequired[str],
        "relatedDeployments": NotRequired[RelatedDeploymentsTypeDef],
        "overrideAlarmConfiguration": NotRequired[AlarmConfigurationOutputTypeDef],
    },
)
GetDeploymentConfigOutputTypeDef = TypedDict(
    "GetDeploymentConfigOutputTypeDef",
    {
        "deploymentConfigInfo": DeploymentConfigInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TargetGroupPairInfoUnionTypeDef = Union[
    TargetGroupPairInfoTypeDef, TargetGroupPairInfoOutputTypeDef
]
CreateDeploymentInputRequestTypeDef = TypedDict(
    "CreateDeploymentInputRequestTypeDef",
    {
        "applicationName": str,
        "deploymentGroupName": NotRequired[str],
        "revision": NotRequired[RevisionLocationTypeDef],
        "deploymentConfigName": NotRequired[str],
        "description": NotRequired[str],
        "ignoreApplicationStopFailures": NotRequired[bool],
        "targetInstances": NotRequired[TargetInstancesTypeDef],
        "autoRollbackConfiguration": NotRequired[AutoRollbackConfigurationTypeDef],
        "updateOutdatedInstancesOnly": NotRequired[bool],
        "fileExistsBehavior": NotRequired[FileExistsBehaviorType],
        "overrideAlarmConfiguration": NotRequired[AlarmConfigurationTypeDef],
    },
)
BatchGetDeploymentTargetsOutputTypeDef = TypedDict(
    "BatchGetDeploymentTargetsOutputTypeDef",
    {
        "deploymentTargets": List[DeploymentTargetTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDeploymentTargetOutputTypeDef = TypedDict(
    "GetDeploymentTargetOutputTypeDef",
    {
        "deploymentTarget": DeploymentTargetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetDeploymentGroupsOutputTypeDef = TypedDict(
    "BatchGetDeploymentGroupsOutputTypeDef",
    {
        "deploymentGroupsInfo": List[DeploymentGroupInfoTypeDef],
        "errorMessage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDeploymentGroupOutputTypeDef = TypedDict(
    "GetDeploymentGroupOutputTypeDef",
    {
        "deploymentGroupInfo": DeploymentGroupInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetDeploymentsOutputTypeDef = TypedDict(
    "BatchGetDeploymentsOutputTypeDef",
    {
        "deploymentsInfo": List[DeploymentInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDeploymentOutputTypeDef = TypedDict(
    "GetDeploymentOutputTypeDef",
    {
        "deploymentInfo": DeploymentInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LoadBalancerInfoTypeDef = TypedDict(
    "LoadBalancerInfoTypeDef",
    {
        "elbInfoList": NotRequired[Sequence[ELBInfoTypeDef]],
        "targetGroupInfoList": NotRequired[Sequence[TargetGroupInfoTypeDef]],
        "targetGroupPairInfoList": NotRequired[Sequence[TargetGroupPairInfoUnionTypeDef]],
    },
)
CreateDeploymentGroupInputRequestTypeDef = TypedDict(
    "CreateDeploymentGroupInputRequestTypeDef",
    {
        "applicationName": str,
        "deploymentGroupName": str,
        "serviceRoleArn": str,
        "deploymentConfigName": NotRequired[str],
        "ec2TagFilters": NotRequired[Sequence[EC2TagFilterTypeDef]],
        "onPremisesInstanceTagFilters": NotRequired[Sequence[TagFilterTypeDef]],
        "autoScalingGroups": NotRequired[Sequence[str]],
        "triggerConfigurations": NotRequired[Sequence[TriggerConfigUnionTypeDef]],
        "alarmConfiguration": NotRequired[AlarmConfigurationTypeDef],
        "autoRollbackConfiguration": NotRequired[AutoRollbackConfigurationTypeDef],
        "outdatedInstancesStrategy": NotRequired[OutdatedInstancesStrategyType],
        "deploymentStyle": NotRequired[DeploymentStyleTypeDef],
        "blueGreenDeploymentConfiguration": NotRequired[BlueGreenDeploymentConfigurationTypeDef],
        "loadBalancerInfo": NotRequired[LoadBalancerInfoTypeDef],
        "ec2TagSet": NotRequired[EC2TagSetTypeDef],
        "ecsServices": NotRequired[Sequence[ECSServiceTypeDef]],
        "onPremisesTagSet": NotRequired[OnPremisesTagSetTypeDef],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "terminationHookEnabled": NotRequired[bool],
    },
)
UpdateDeploymentGroupInputRequestTypeDef = TypedDict(
    "UpdateDeploymentGroupInputRequestTypeDef",
    {
        "applicationName": str,
        "currentDeploymentGroupName": str,
        "newDeploymentGroupName": NotRequired[str],
        "deploymentConfigName": NotRequired[str],
        "ec2TagFilters": NotRequired[Sequence[EC2TagFilterTypeDef]],
        "onPremisesInstanceTagFilters": NotRequired[Sequence[TagFilterTypeDef]],
        "autoScalingGroups": NotRequired[Sequence[str]],
        "serviceRoleArn": NotRequired[str],
        "triggerConfigurations": NotRequired[Sequence[TriggerConfigTypeDef]],
        "alarmConfiguration": NotRequired[AlarmConfigurationTypeDef],
        "autoRollbackConfiguration": NotRequired[AutoRollbackConfigurationTypeDef],
        "outdatedInstancesStrategy": NotRequired[OutdatedInstancesStrategyType],
        "deploymentStyle": NotRequired[DeploymentStyleTypeDef],
        "blueGreenDeploymentConfiguration": NotRequired[BlueGreenDeploymentConfigurationTypeDef],
        "loadBalancerInfo": NotRequired[LoadBalancerInfoTypeDef],
        "ec2TagSet": NotRequired[EC2TagSetTypeDef],
        "ecsServices": NotRequired[Sequence[ECSServiceTypeDef]],
        "onPremisesTagSet": NotRequired[OnPremisesTagSetTypeDef],
        "terminationHookEnabled": NotRequired[bool],
    },
)
