"""
Type annotations for emr service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr/type_defs/)

Usage::

    ```python
    from mypy_boto3_emr.type_defs import ResponseMetadataTypeDef

    data: ResponseMetadataTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    ActionOnFailureType,
    AdjustmentTypeType,
    AuthModeType,
    AutoScalingPolicyStateChangeReasonCodeType,
    AutoScalingPolicyStateType,
    CancelStepsRequestStatusType,
    ClusterStateChangeReasonCodeType,
    ClusterStateType,
    ComparisonOperatorType,
    ComputeLimitsUnitTypeType,
    IdcUserAssignmentType,
    IdentityTypeType,
    InstanceCollectionTypeType,
    InstanceFleetStateChangeReasonCodeType,
    InstanceFleetStateType,
    InstanceFleetTypeType,
    InstanceGroupStateChangeReasonCodeType,
    InstanceGroupStateType,
    InstanceGroupTypeType,
    InstanceRoleTypeType,
    InstanceStateChangeReasonCodeType,
    InstanceStateType,
    JobFlowExecutionStateType,
    MarketTypeType,
    NotebookExecutionStatusType,
    OnDemandCapacityReservationPreferenceType,
    OnDemandProvisioningAllocationStrategyType,
    PlacementGroupStrategyType,
    ReconfigurationTypeType,
    RepoUpgradeOnBootType,
    ScaleDownBehaviorType,
    SpotProvisioningAllocationStrategyType,
    SpotProvisioningTimeoutActionType,
    StatisticType,
    StepCancellationOptionType,
    StepExecutionStateType,
    StepStateType,
    UnitType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "ResponseMetadataTypeDef",
    "TagTypeDef",
    "ApplicationOutputTypeDef",
    "ApplicationTypeDef",
    "ScalingConstraintsTypeDef",
    "AutoScalingPolicyStateChangeReasonTypeDef",
    "AutoTerminationPolicyTypeDef",
    "BlockPublicAccessConfigurationMetadataTypeDef",
    "PortRangeTypeDef",
    "ScriptBootstrapActionConfigOutputTypeDef",
    "CancelStepsInfoTypeDef",
    "CancelStepsInputRequestTypeDef",
    "MetricDimensionTypeDef",
    "ClusterStateChangeReasonTypeDef",
    "ClusterTimelineTypeDef",
    "ErrorDetailTypeDef",
    "ConfigurationOutputTypeDef",
    "Ec2InstanceAttributesTypeDef",
    "KerberosAttributesTypeDef",
    "PlacementGroupConfigTypeDef",
    "CommandTypeDef",
    "ComputeLimitsTypeDef",
    "ConfigurationPaginatorTypeDef",
    "ConfigurationTypeDef",
    "CreateSecurityConfigurationInputRequestTypeDef",
    "CreateStudioSessionMappingInputRequestTypeDef",
    "UsernamePasswordTypeDef",
    "DeleteSecurityConfigurationInputRequestTypeDef",
    "DeleteStudioInputRequestTypeDef",
    "DeleteStudioSessionMappingInputRequestTypeDef",
    "WaiterConfigTypeDef",
    "DescribeClusterInputRequestTypeDef",
    "TimestampTypeDef",
    "DescribeNotebookExecutionInputRequestTypeDef",
    "DescribeReleaseLabelInputRequestTypeDef",
    "OSReleaseTypeDef",
    "SimplifiedApplicationTypeDef",
    "DescribeSecurityConfigurationInputRequestTypeDef",
    "DescribeStepInputRequestTypeDef",
    "DescribeStudioInputRequestTypeDef",
    "VolumeSpecificationTypeDef",
    "EbsVolumeTypeDef",
    "ExecutionEngineConfigTypeDef",
    "FailureDetailsTypeDef",
    "GetAutoTerminationPolicyInputRequestTypeDef",
    "GetClusterSessionCredentialsInputRequestTypeDef",
    "GetManagedScalingPolicyInputRequestTypeDef",
    "GetStudioSessionMappingInputRequestTypeDef",
    "SessionMappingDetailTypeDef",
    "KeyValueTypeDef",
    "HadoopStepConfigTypeDef",
    "SpotProvisioningSpecificationTypeDef",
    "SpotResizingSpecificationTypeDef",
    "InstanceFleetStateChangeReasonTypeDef",
    "InstanceFleetTimelineTypeDef",
    "InstanceGroupDetailTypeDef",
    "InstanceGroupStateChangeReasonTypeDef",
    "InstanceGroupTimelineTypeDef",
    "InstanceResizePolicyOutputTypeDef",
    "InstanceResizePolicyTypeDef",
    "InstanceStateChangeReasonTypeDef",
    "InstanceTimelineTypeDef",
    "JobFlowExecutionStatusDetailTypeDef",
    "PlacementTypeOutputTypeDef",
    "PaginatorConfigTypeDef",
    "ListBootstrapActionsInputRequestTypeDef",
    "ListInstanceFleetsInputRequestTypeDef",
    "ListInstanceGroupsInputRequestTypeDef",
    "ListInstancesInputRequestTypeDef",
    "ReleaseLabelFilterTypeDef",
    "ListSecurityConfigurationsInputRequestTypeDef",
    "SecurityConfigurationSummaryTypeDef",
    "ListStepsInputRequestTypeDef",
    "ListStudioSessionMappingsInputRequestTypeDef",
    "SessionMappingSummaryTypeDef",
    "ListStudiosInputRequestTypeDef",
    "StudioSummaryTypeDef",
    "ListSupportedInstanceTypesInputRequestTypeDef",
    "SupportedInstanceTypeTypeDef",
    "ModifyClusterInputRequestTypeDef",
    "NotebookS3LocationForOutputTypeDef",
    "OutputNotebookS3LocationForOutputTypeDef",
    "NotebookS3LocationFromInputTypeDef",
    "OnDemandCapacityReservationOptionsTypeDef",
    "OutputNotebookS3LocationFromInputTypeDef",
    "PlacementTypeTypeDef",
    "RemoveAutoScalingPolicyInputRequestTypeDef",
    "RemoveAutoTerminationPolicyInputRequestTypeDef",
    "RemoveManagedScalingPolicyInputRequestTypeDef",
    "RemoveTagsInputRequestTypeDef",
    "SupportedProductConfigTypeDef",
    "SimpleScalingPolicyConfigurationTypeDef",
    "ScriptBootstrapActionConfigTypeDef",
    "SetKeepJobFlowAliveWhenNoStepsInputRequestTypeDef",
    "SetTerminationProtectionInputRequestTypeDef",
    "SetUnhealthyNodeReplacementInputRequestTypeDef",
    "SetVisibleToAllUsersInputRequestTypeDef",
    "StepExecutionStatusDetailTypeDef",
    "StepStateChangeReasonTypeDef",
    "StepTimelineTypeDef",
    "StopNotebookExecutionInputRequestTypeDef",
    "TerminateJobFlowsInputRequestTypeDef",
    "UpdateStudioInputRequestTypeDef",
    "UpdateStudioSessionMappingInputRequestTypeDef",
    "AddInstanceFleetOutputTypeDef",
    "AddInstanceGroupsOutputTypeDef",
    "AddJobFlowStepsOutputTypeDef",
    "CreateSecurityConfigurationOutputTypeDef",
    "CreateStudioOutputTypeDef",
    "DescribeSecurityConfigurationOutputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ListReleaseLabelsOutputTypeDef",
    "ModifyClusterOutputTypeDef",
    "RunJobFlowOutputTypeDef",
    "StartNotebookExecutionOutputTypeDef",
    "AddTagsInputRequestTypeDef",
    "CreateStudioInputRequestTypeDef",
    "StudioTypeDef",
    "ApplicationUnionTypeDef",
    "AutoScalingPolicyStatusTypeDef",
    "GetAutoTerminationPolicyOutputTypeDef",
    "PutAutoTerminationPolicyInputRequestTypeDef",
    "BlockPublicAccessConfigurationOutputTypeDef",
    "BlockPublicAccessConfigurationTypeDef",
    "BootstrapActionConfigOutputTypeDef",
    "CancelStepsOutputTypeDef",
    "CloudWatchAlarmDefinitionOutputTypeDef",
    "CloudWatchAlarmDefinitionTypeDef",
    "ClusterStatusTypeDef",
    "ListBootstrapActionsOutputTypeDef",
    "ManagedScalingPolicyTypeDef",
    "ConfigurationUnionTypeDef",
    "CredentialsTypeDef",
    "DescribeClusterInputClusterRunningWaitTypeDef",
    "DescribeClusterInputClusterTerminatedWaitTypeDef",
    "DescribeStepInputStepCompleteWaitTypeDef",
    "DescribeJobFlowsInputRequestTypeDef",
    "ListClustersInputRequestTypeDef",
    "ListNotebookExecutionsInputRequestTypeDef",
    "DescribeReleaseLabelOutputTypeDef",
    "EbsBlockDeviceConfigTypeDef",
    "EbsBlockDeviceTypeDef",
    "GetStudioSessionMappingOutputTypeDef",
    "HadoopJarStepConfigOutputTypeDef",
    "HadoopJarStepConfigTypeDef",
    "InstanceFleetStatusTypeDef",
    "InstanceGroupStatusTypeDef",
    "ShrinkPolicyOutputTypeDef",
    "InstanceResizePolicyUnionTypeDef",
    "InstanceStatusTypeDef",
    "JobFlowInstancesDetailTypeDef",
    "ListBootstrapActionsInputListBootstrapActionsPaginateTypeDef",
    "ListClustersInputListClustersPaginateTypeDef",
    "ListInstanceFleetsInputListInstanceFleetsPaginateTypeDef",
    "ListInstanceGroupsInputListInstanceGroupsPaginateTypeDef",
    "ListInstancesInputListInstancesPaginateTypeDef",
    "ListNotebookExecutionsInputListNotebookExecutionsPaginateTypeDef",
    "ListSecurityConfigurationsInputListSecurityConfigurationsPaginateTypeDef",
    "ListStepsInputListStepsPaginateTypeDef",
    "ListStudioSessionMappingsInputListStudioSessionMappingsPaginateTypeDef",
    "ListStudiosInputListStudiosPaginateTypeDef",
    "ListReleaseLabelsInputRequestTypeDef",
    "ListSecurityConfigurationsOutputTypeDef",
    "ListStudioSessionMappingsOutputTypeDef",
    "ListStudiosOutputTypeDef",
    "ListSupportedInstanceTypesOutputTypeDef",
    "NotebookExecutionSummaryTypeDef",
    "NotebookExecutionTypeDef",
    "OnDemandProvisioningSpecificationTypeDef",
    "OnDemandResizingSpecificationTypeDef",
    "StartNotebookExecutionInputRequestTypeDef",
    "PlacementTypeUnionTypeDef",
    "ScalingActionTypeDef",
    "ScriptBootstrapActionConfigUnionTypeDef",
    "StepStatusTypeDef",
    "DescribeStudioOutputTypeDef",
    "GetBlockPublicAccessConfigurationOutputTypeDef",
    "PutBlockPublicAccessConfigurationInputRequestTypeDef",
    "BootstrapActionDetailTypeDef",
    "ScalingTriggerOutputTypeDef",
    "CloudWatchAlarmDefinitionUnionTypeDef",
    "ClusterSummaryTypeDef",
    "ClusterTypeDef",
    "GetManagedScalingPolicyOutputTypeDef",
    "PutManagedScalingPolicyInputRequestTypeDef",
    "GetClusterSessionCredentialsOutputTypeDef",
    "EbsConfigurationTypeDef",
    "InstanceTypeSpecificationPaginatorTypeDef",
    "InstanceTypeSpecificationTypeDef",
    "StepConfigOutputTypeDef",
    "HadoopJarStepConfigUnionTypeDef",
    "ShrinkPolicyTypeDef",
    "InstanceTypeDef",
    "ListNotebookExecutionsOutputTypeDef",
    "DescribeNotebookExecutionOutputTypeDef",
    "InstanceFleetProvisioningSpecificationsTypeDef",
    "InstanceFleetResizingSpecificationsTypeDef",
    "BootstrapActionConfigTypeDef",
    "StepSummaryTypeDef",
    "StepTypeDef",
    "ScalingRuleOutputTypeDef",
    "ScalingTriggerTypeDef",
    "ListClustersOutputTypeDef",
    "DescribeClusterOutputTypeDef",
    "InstanceTypeConfigTypeDef",
    "StepDetailTypeDef",
    "StepConfigTypeDef",
    "ShrinkPolicyUnionTypeDef",
    "ListInstancesOutputTypeDef",
    "InstanceFleetPaginatorTypeDef",
    "InstanceFleetTypeDef",
    "BootstrapActionConfigUnionTypeDef",
    "ListStepsOutputTypeDef",
    "DescribeStepOutputTypeDef",
    "AutoScalingPolicyDescriptionTypeDef",
    "ScalingTriggerUnionTypeDef",
    "InstanceFleetConfigTypeDef",
    "InstanceFleetModifyConfigTypeDef",
    "JobFlowDetailTypeDef",
    "StepConfigUnionTypeDef",
    "InstanceGroupModifyConfigTypeDef",
    "ListInstanceFleetsOutputPaginatorTypeDef",
    "ListInstanceFleetsOutputTypeDef",
    "InstanceGroupPaginatorTypeDef",
    "InstanceGroupTypeDef",
    "PutAutoScalingPolicyOutputTypeDef",
    "ScalingRuleTypeDef",
    "AddInstanceFleetInputRequestTypeDef",
    "ModifyInstanceFleetInputRequestTypeDef",
    "DescribeJobFlowsOutputTypeDef",
    "AddJobFlowStepsInputRequestTypeDef",
    "ModifyInstanceGroupsInputRequestTypeDef",
    "ListInstanceGroupsOutputPaginatorTypeDef",
    "ListInstanceGroupsOutputTypeDef",
    "ScalingRuleUnionTypeDef",
    "AutoScalingPolicyTypeDef",
    "InstanceGroupConfigTypeDef",
    "PutAutoScalingPolicyInputRequestTypeDef",
    "AddInstanceGroupsInputRequestTypeDef",
    "JobFlowInstancesConfigTypeDef",
    "RunJobFlowInputRequestTypeDef",
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
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
ApplicationOutputTypeDef = TypedDict(
    "ApplicationOutputTypeDef",
    {
        "Name": NotRequired[str],
        "Version": NotRequired[str],
        "Args": NotRequired[List[str]],
        "AdditionalInfo": NotRequired[Dict[str, str]],
    },
)
ApplicationTypeDef = TypedDict(
    "ApplicationTypeDef",
    {
        "Name": NotRequired[str],
        "Version": NotRequired[str],
        "Args": NotRequired[Sequence[str]],
        "AdditionalInfo": NotRequired[Mapping[str, str]],
    },
)
ScalingConstraintsTypeDef = TypedDict(
    "ScalingConstraintsTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
    },
)
AutoScalingPolicyStateChangeReasonTypeDef = TypedDict(
    "AutoScalingPolicyStateChangeReasonTypeDef",
    {
        "Code": NotRequired[AutoScalingPolicyStateChangeReasonCodeType],
        "Message": NotRequired[str],
    },
)
AutoTerminationPolicyTypeDef = TypedDict(
    "AutoTerminationPolicyTypeDef",
    {
        "IdleTimeout": NotRequired[int],
    },
)
BlockPublicAccessConfigurationMetadataTypeDef = TypedDict(
    "BlockPublicAccessConfigurationMetadataTypeDef",
    {
        "CreationDateTime": datetime,
        "CreatedByArn": str,
    },
)
PortRangeTypeDef = TypedDict(
    "PortRangeTypeDef",
    {
        "MinRange": int,
        "MaxRange": NotRequired[int],
    },
)
ScriptBootstrapActionConfigOutputTypeDef = TypedDict(
    "ScriptBootstrapActionConfigOutputTypeDef",
    {
        "Path": str,
        "Args": NotRequired[List[str]],
    },
)
CancelStepsInfoTypeDef = TypedDict(
    "CancelStepsInfoTypeDef",
    {
        "StepId": NotRequired[str],
        "Status": NotRequired[CancelStepsRequestStatusType],
        "Reason": NotRequired[str],
    },
)
CancelStepsInputRequestTypeDef = TypedDict(
    "CancelStepsInputRequestTypeDef",
    {
        "ClusterId": str,
        "StepIds": Sequence[str],
        "StepCancellationOption": NotRequired[StepCancellationOptionType],
    },
)
MetricDimensionTypeDef = TypedDict(
    "MetricDimensionTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
ClusterStateChangeReasonTypeDef = TypedDict(
    "ClusterStateChangeReasonTypeDef",
    {
        "Code": NotRequired[ClusterStateChangeReasonCodeType],
        "Message": NotRequired[str],
    },
)
ClusterTimelineTypeDef = TypedDict(
    "ClusterTimelineTypeDef",
    {
        "CreationDateTime": NotRequired[datetime],
        "ReadyDateTime": NotRequired[datetime],
        "EndDateTime": NotRequired[datetime],
    },
)
ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef",
    {
        "ErrorCode": NotRequired[str],
        "ErrorData": NotRequired[List[Dict[str, str]]],
        "ErrorMessage": NotRequired[str],
    },
)
ConfigurationOutputTypeDef = TypedDict(
    "ConfigurationOutputTypeDef",
    {
        "Classification": NotRequired[str],
        "Configurations": NotRequired[List[Dict[str, Any]]],
        "Properties": NotRequired[Dict[str, str]],
    },
)
Ec2InstanceAttributesTypeDef = TypedDict(
    "Ec2InstanceAttributesTypeDef",
    {
        "Ec2KeyName": NotRequired[str],
        "Ec2SubnetId": NotRequired[str],
        "RequestedEc2SubnetIds": NotRequired[List[str]],
        "Ec2AvailabilityZone": NotRequired[str],
        "RequestedEc2AvailabilityZones": NotRequired[List[str]],
        "IamInstanceProfile": NotRequired[str],
        "EmrManagedMasterSecurityGroup": NotRequired[str],
        "EmrManagedSlaveSecurityGroup": NotRequired[str],
        "ServiceAccessSecurityGroup": NotRequired[str],
        "AdditionalMasterSecurityGroups": NotRequired[List[str]],
        "AdditionalSlaveSecurityGroups": NotRequired[List[str]],
    },
)
KerberosAttributesTypeDef = TypedDict(
    "KerberosAttributesTypeDef",
    {
        "Realm": str,
        "KdcAdminPassword": str,
        "CrossRealmTrustPrincipalPassword": NotRequired[str],
        "ADDomainJoinUser": NotRequired[str],
        "ADDomainJoinPassword": NotRequired[str],
    },
)
PlacementGroupConfigTypeDef = TypedDict(
    "PlacementGroupConfigTypeDef",
    {
        "InstanceRole": InstanceRoleTypeType,
        "PlacementStrategy": NotRequired[PlacementGroupStrategyType],
    },
)
CommandTypeDef = TypedDict(
    "CommandTypeDef",
    {
        "Name": NotRequired[str],
        "ScriptPath": NotRequired[str],
        "Args": NotRequired[List[str]],
    },
)
ComputeLimitsTypeDef = TypedDict(
    "ComputeLimitsTypeDef",
    {
        "UnitType": ComputeLimitsUnitTypeType,
        "MinimumCapacityUnits": int,
        "MaximumCapacityUnits": int,
        "MaximumOnDemandCapacityUnits": NotRequired[int],
        "MaximumCoreCapacityUnits": NotRequired[int],
    },
)
ConfigurationPaginatorTypeDef = TypedDict(
    "ConfigurationPaginatorTypeDef",
    {
        "Classification": NotRequired[str],
        "Configurations": NotRequired[List[Dict[str, Any]]],
        "Properties": NotRequired[Dict[str, str]],
    },
)
ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "Classification": NotRequired[str],
        "Configurations": NotRequired[Sequence[Mapping[str, Any]]],
        "Properties": NotRequired[Mapping[str, str]],
    },
)
CreateSecurityConfigurationInputRequestTypeDef = TypedDict(
    "CreateSecurityConfigurationInputRequestTypeDef",
    {
        "Name": str,
        "SecurityConfiguration": str,
    },
)
CreateStudioSessionMappingInputRequestTypeDef = TypedDict(
    "CreateStudioSessionMappingInputRequestTypeDef",
    {
        "StudioId": str,
        "IdentityType": IdentityTypeType,
        "SessionPolicyArn": str,
        "IdentityId": NotRequired[str],
        "IdentityName": NotRequired[str],
    },
)
UsernamePasswordTypeDef = TypedDict(
    "UsernamePasswordTypeDef",
    {
        "Username": NotRequired[str],
        "Password": NotRequired[str],
    },
)
DeleteSecurityConfigurationInputRequestTypeDef = TypedDict(
    "DeleteSecurityConfigurationInputRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteStudioInputRequestTypeDef = TypedDict(
    "DeleteStudioInputRequestTypeDef",
    {
        "StudioId": str,
    },
)
DeleteStudioSessionMappingInputRequestTypeDef = TypedDict(
    "DeleteStudioSessionMappingInputRequestTypeDef",
    {
        "StudioId": str,
        "IdentityType": IdentityTypeType,
        "IdentityId": NotRequired[str],
        "IdentityName": NotRequired[str],
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
DescribeClusterInputRequestTypeDef = TypedDict(
    "DescribeClusterInputRequestTypeDef",
    {
        "ClusterId": str,
    },
)
TimestampTypeDef = Union[datetime, str]
DescribeNotebookExecutionInputRequestTypeDef = TypedDict(
    "DescribeNotebookExecutionInputRequestTypeDef",
    {
        "NotebookExecutionId": str,
    },
)
DescribeReleaseLabelInputRequestTypeDef = TypedDict(
    "DescribeReleaseLabelInputRequestTypeDef",
    {
        "ReleaseLabel": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
OSReleaseTypeDef = TypedDict(
    "OSReleaseTypeDef",
    {
        "Label": NotRequired[str],
    },
)
SimplifiedApplicationTypeDef = TypedDict(
    "SimplifiedApplicationTypeDef",
    {
        "Name": NotRequired[str],
        "Version": NotRequired[str],
    },
)
DescribeSecurityConfigurationInputRequestTypeDef = TypedDict(
    "DescribeSecurityConfigurationInputRequestTypeDef",
    {
        "Name": str,
    },
)
DescribeStepInputRequestTypeDef = TypedDict(
    "DescribeStepInputRequestTypeDef",
    {
        "ClusterId": str,
        "StepId": str,
    },
)
DescribeStudioInputRequestTypeDef = TypedDict(
    "DescribeStudioInputRequestTypeDef",
    {
        "StudioId": str,
    },
)
VolumeSpecificationTypeDef = TypedDict(
    "VolumeSpecificationTypeDef",
    {
        "VolumeType": str,
        "SizeInGB": int,
        "Iops": NotRequired[int],
        "Throughput": NotRequired[int],
    },
)
EbsVolumeTypeDef = TypedDict(
    "EbsVolumeTypeDef",
    {
        "Device": NotRequired[str],
        "VolumeId": NotRequired[str],
    },
)
ExecutionEngineConfigTypeDef = TypedDict(
    "ExecutionEngineConfigTypeDef",
    {
        "Id": str,
        "Type": NotRequired[Literal["EMR"]],
        "MasterInstanceSecurityGroupId": NotRequired[str],
        "ExecutionRoleArn": NotRequired[str],
    },
)
FailureDetailsTypeDef = TypedDict(
    "FailureDetailsTypeDef",
    {
        "Reason": NotRequired[str],
        "Message": NotRequired[str],
        "LogFile": NotRequired[str],
    },
)
GetAutoTerminationPolicyInputRequestTypeDef = TypedDict(
    "GetAutoTerminationPolicyInputRequestTypeDef",
    {
        "ClusterId": str,
    },
)
GetClusterSessionCredentialsInputRequestTypeDef = TypedDict(
    "GetClusterSessionCredentialsInputRequestTypeDef",
    {
        "ClusterId": str,
        "ExecutionRoleArn": NotRequired[str],
    },
)
GetManagedScalingPolicyInputRequestTypeDef = TypedDict(
    "GetManagedScalingPolicyInputRequestTypeDef",
    {
        "ClusterId": str,
    },
)
GetStudioSessionMappingInputRequestTypeDef = TypedDict(
    "GetStudioSessionMappingInputRequestTypeDef",
    {
        "StudioId": str,
        "IdentityType": IdentityTypeType,
        "IdentityId": NotRequired[str],
        "IdentityName": NotRequired[str],
    },
)
SessionMappingDetailTypeDef = TypedDict(
    "SessionMappingDetailTypeDef",
    {
        "StudioId": NotRequired[str],
        "IdentityId": NotRequired[str],
        "IdentityName": NotRequired[str],
        "IdentityType": NotRequired[IdentityTypeType],
        "SessionPolicyArn": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
    },
)
KeyValueTypeDef = TypedDict(
    "KeyValueTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
HadoopStepConfigTypeDef = TypedDict(
    "HadoopStepConfigTypeDef",
    {
        "Jar": NotRequired[str],
        "Properties": NotRequired[Dict[str, str]],
        "MainClass": NotRequired[str],
        "Args": NotRequired[List[str]],
    },
)
SpotProvisioningSpecificationTypeDef = TypedDict(
    "SpotProvisioningSpecificationTypeDef",
    {
        "TimeoutDurationMinutes": int,
        "TimeoutAction": SpotProvisioningTimeoutActionType,
        "BlockDurationMinutes": NotRequired[int],
        "AllocationStrategy": NotRequired[SpotProvisioningAllocationStrategyType],
    },
)
SpotResizingSpecificationTypeDef = TypedDict(
    "SpotResizingSpecificationTypeDef",
    {
        "TimeoutDurationMinutes": NotRequired[int],
        "AllocationStrategy": NotRequired[SpotProvisioningAllocationStrategyType],
    },
)
InstanceFleetStateChangeReasonTypeDef = TypedDict(
    "InstanceFleetStateChangeReasonTypeDef",
    {
        "Code": NotRequired[InstanceFleetStateChangeReasonCodeType],
        "Message": NotRequired[str],
    },
)
InstanceFleetTimelineTypeDef = TypedDict(
    "InstanceFleetTimelineTypeDef",
    {
        "CreationDateTime": NotRequired[datetime],
        "ReadyDateTime": NotRequired[datetime],
        "EndDateTime": NotRequired[datetime],
    },
)
InstanceGroupDetailTypeDef = TypedDict(
    "InstanceGroupDetailTypeDef",
    {
        "Market": MarketTypeType,
        "InstanceRole": InstanceRoleTypeType,
        "InstanceType": str,
        "InstanceRequestCount": int,
        "InstanceRunningCount": int,
        "State": InstanceGroupStateType,
        "CreationDateTime": datetime,
        "InstanceGroupId": NotRequired[str],
        "Name": NotRequired[str],
        "BidPrice": NotRequired[str],
        "LastStateChangeReason": NotRequired[str],
        "StartDateTime": NotRequired[datetime],
        "ReadyDateTime": NotRequired[datetime],
        "EndDateTime": NotRequired[datetime],
        "CustomAmiId": NotRequired[str],
    },
)
InstanceGroupStateChangeReasonTypeDef = TypedDict(
    "InstanceGroupStateChangeReasonTypeDef",
    {
        "Code": NotRequired[InstanceGroupStateChangeReasonCodeType],
        "Message": NotRequired[str],
    },
)
InstanceGroupTimelineTypeDef = TypedDict(
    "InstanceGroupTimelineTypeDef",
    {
        "CreationDateTime": NotRequired[datetime],
        "ReadyDateTime": NotRequired[datetime],
        "EndDateTime": NotRequired[datetime],
    },
)
InstanceResizePolicyOutputTypeDef = TypedDict(
    "InstanceResizePolicyOutputTypeDef",
    {
        "InstancesToTerminate": NotRequired[List[str]],
        "InstancesToProtect": NotRequired[List[str]],
        "InstanceTerminationTimeout": NotRequired[int],
    },
)
InstanceResizePolicyTypeDef = TypedDict(
    "InstanceResizePolicyTypeDef",
    {
        "InstancesToTerminate": NotRequired[Sequence[str]],
        "InstancesToProtect": NotRequired[Sequence[str]],
        "InstanceTerminationTimeout": NotRequired[int],
    },
)
InstanceStateChangeReasonTypeDef = TypedDict(
    "InstanceStateChangeReasonTypeDef",
    {
        "Code": NotRequired[InstanceStateChangeReasonCodeType],
        "Message": NotRequired[str],
    },
)
InstanceTimelineTypeDef = TypedDict(
    "InstanceTimelineTypeDef",
    {
        "CreationDateTime": NotRequired[datetime],
        "ReadyDateTime": NotRequired[datetime],
        "EndDateTime": NotRequired[datetime],
    },
)
JobFlowExecutionStatusDetailTypeDef = TypedDict(
    "JobFlowExecutionStatusDetailTypeDef",
    {
        "State": JobFlowExecutionStateType,
        "CreationDateTime": datetime,
        "StartDateTime": NotRequired[datetime],
        "ReadyDateTime": NotRequired[datetime],
        "EndDateTime": NotRequired[datetime],
        "LastStateChangeReason": NotRequired[str],
    },
)
PlacementTypeOutputTypeDef = TypedDict(
    "PlacementTypeOutputTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "AvailabilityZones": NotRequired[List[str]],
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
ListBootstrapActionsInputRequestTypeDef = TypedDict(
    "ListBootstrapActionsInputRequestTypeDef",
    {
        "ClusterId": str,
        "Marker": NotRequired[str],
    },
)
ListInstanceFleetsInputRequestTypeDef = TypedDict(
    "ListInstanceFleetsInputRequestTypeDef",
    {
        "ClusterId": str,
        "Marker": NotRequired[str],
    },
)
ListInstanceGroupsInputRequestTypeDef = TypedDict(
    "ListInstanceGroupsInputRequestTypeDef",
    {
        "ClusterId": str,
        "Marker": NotRequired[str],
    },
)
ListInstancesInputRequestTypeDef = TypedDict(
    "ListInstancesInputRequestTypeDef",
    {
        "ClusterId": str,
        "InstanceGroupId": NotRequired[str],
        "InstanceGroupTypes": NotRequired[Sequence[InstanceGroupTypeType]],
        "InstanceFleetId": NotRequired[str],
        "InstanceFleetType": NotRequired[InstanceFleetTypeType],
        "InstanceStates": NotRequired[Sequence[InstanceStateType]],
        "Marker": NotRequired[str],
    },
)
ReleaseLabelFilterTypeDef = TypedDict(
    "ReleaseLabelFilterTypeDef",
    {
        "Prefix": NotRequired[str],
        "Application": NotRequired[str],
    },
)
ListSecurityConfigurationsInputRequestTypeDef = TypedDict(
    "ListSecurityConfigurationsInputRequestTypeDef",
    {
        "Marker": NotRequired[str],
    },
)
SecurityConfigurationSummaryTypeDef = TypedDict(
    "SecurityConfigurationSummaryTypeDef",
    {
        "Name": NotRequired[str],
        "CreationDateTime": NotRequired[datetime],
    },
)
ListStepsInputRequestTypeDef = TypedDict(
    "ListStepsInputRequestTypeDef",
    {
        "ClusterId": str,
        "StepStates": NotRequired[Sequence[StepStateType]],
        "StepIds": NotRequired[Sequence[str]],
        "Marker": NotRequired[str],
    },
)
ListStudioSessionMappingsInputRequestTypeDef = TypedDict(
    "ListStudioSessionMappingsInputRequestTypeDef",
    {
        "StudioId": NotRequired[str],
        "IdentityType": NotRequired[IdentityTypeType],
        "Marker": NotRequired[str],
    },
)
SessionMappingSummaryTypeDef = TypedDict(
    "SessionMappingSummaryTypeDef",
    {
        "StudioId": NotRequired[str],
        "IdentityId": NotRequired[str],
        "IdentityName": NotRequired[str],
        "IdentityType": NotRequired[IdentityTypeType],
        "SessionPolicyArn": NotRequired[str],
        "CreationTime": NotRequired[datetime],
    },
)
ListStudiosInputRequestTypeDef = TypedDict(
    "ListStudiosInputRequestTypeDef",
    {
        "Marker": NotRequired[str],
    },
)
StudioSummaryTypeDef = TypedDict(
    "StudioSummaryTypeDef",
    {
        "StudioId": NotRequired[str],
        "Name": NotRequired[str],
        "VpcId": NotRequired[str],
        "Description": NotRequired[str],
        "Url": NotRequired[str],
        "AuthMode": NotRequired[AuthModeType],
        "CreationTime": NotRequired[datetime],
    },
)
ListSupportedInstanceTypesInputRequestTypeDef = TypedDict(
    "ListSupportedInstanceTypesInputRequestTypeDef",
    {
        "ReleaseLabel": str,
        "Marker": NotRequired[str],
    },
)
SupportedInstanceTypeTypeDef = TypedDict(
    "SupportedInstanceTypeTypeDef",
    {
        "Type": NotRequired[str],
        "MemoryGB": NotRequired[float],
        "StorageGB": NotRequired[int],
        "VCPU": NotRequired[int],
        "Is64BitsOnly": NotRequired[bool],
        "InstanceFamilyId": NotRequired[str],
        "EbsOptimizedAvailable": NotRequired[bool],
        "EbsOptimizedByDefault": NotRequired[bool],
        "NumberOfDisks": NotRequired[int],
        "EbsStorageOnly": NotRequired[bool],
        "Architecture": NotRequired[str],
    },
)
ModifyClusterInputRequestTypeDef = TypedDict(
    "ModifyClusterInputRequestTypeDef",
    {
        "ClusterId": str,
        "StepConcurrencyLevel": NotRequired[int],
    },
)
NotebookS3LocationForOutputTypeDef = TypedDict(
    "NotebookS3LocationForOutputTypeDef",
    {
        "Bucket": NotRequired[str],
        "Key": NotRequired[str],
    },
)
OutputNotebookS3LocationForOutputTypeDef = TypedDict(
    "OutputNotebookS3LocationForOutputTypeDef",
    {
        "Bucket": NotRequired[str],
        "Key": NotRequired[str],
    },
)
NotebookS3LocationFromInputTypeDef = TypedDict(
    "NotebookS3LocationFromInputTypeDef",
    {
        "Bucket": NotRequired[str],
        "Key": NotRequired[str],
    },
)
OnDemandCapacityReservationOptionsTypeDef = TypedDict(
    "OnDemandCapacityReservationOptionsTypeDef",
    {
        "UsageStrategy": NotRequired[Literal["use-capacity-reservations-first"]],
        "CapacityReservationPreference": NotRequired[OnDemandCapacityReservationPreferenceType],
        "CapacityReservationResourceGroupArn": NotRequired[str],
    },
)
OutputNotebookS3LocationFromInputTypeDef = TypedDict(
    "OutputNotebookS3LocationFromInputTypeDef",
    {
        "Bucket": NotRequired[str],
        "Key": NotRequired[str],
    },
)
PlacementTypeTypeDef = TypedDict(
    "PlacementTypeTypeDef",
    {
        "AvailabilityZone": NotRequired[str],
        "AvailabilityZones": NotRequired[Sequence[str]],
    },
)
RemoveAutoScalingPolicyInputRequestTypeDef = TypedDict(
    "RemoveAutoScalingPolicyInputRequestTypeDef",
    {
        "ClusterId": str,
        "InstanceGroupId": str,
    },
)
RemoveAutoTerminationPolicyInputRequestTypeDef = TypedDict(
    "RemoveAutoTerminationPolicyInputRequestTypeDef",
    {
        "ClusterId": str,
    },
)
RemoveManagedScalingPolicyInputRequestTypeDef = TypedDict(
    "RemoveManagedScalingPolicyInputRequestTypeDef",
    {
        "ClusterId": str,
    },
)
RemoveTagsInputRequestTypeDef = TypedDict(
    "RemoveTagsInputRequestTypeDef",
    {
        "ResourceId": str,
        "TagKeys": Sequence[str],
    },
)
SupportedProductConfigTypeDef = TypedDict(
    "SupportedProductConfigTypeDef",
    {
        "Name": NotRequired[str],
        "Args": NotRequired[Sequence[str]],
    },
)
SimpleScalingPolicyConfigurationTypeDef = TypedDict(
    "SimpleScalingPolicyConfigurationTypeDef",
    {
        "ScalingAdjustment": int,
        "AdjustmentType": NotRequired[AdjustmentTypeType],
        "CoolDown": NotRequired[int],
    },
)
ScriptBootstrapActionConfigTypeDef = TypedDict(
    "ScriptBootstrapActionConfigTypeDef",
    {
        "Path": str,
        "Args": NotRequired[Sequence[str]],
    },
)
SetKeepJobFlowAliveWhenNoStepsInputRequestTypeDef = TypedDict(
    "SetKeepJobFlowAliveWhenNoStepsInputRequestTypeDef",
    {
        "JobFlowIds": Sequence[str],
        "KeepJobFlowAliveWhenNoSteps": bool,
    },
)
SetTerminationProtectionInputRequestTypeDef = TypedDict(
    "SetTerminationProtectionInputRequestTypeDef",
    {
        "JobFlowIds": Sequence[str],
        "TerminationProtected": bool,
    },
)
SetUnhealthyNodeReplacementInputRequestTypeDef = TypedDict(
    "SetUnhealthyNodeReplacementInputRequestTypeDef",
    {
        "JobFlowIds": Sequence[str],
        "UnhealthyNodeReplacement": bool,
    },
)
SetVisibleToAllUsersInputRequestTypeDef = TypedDict(
    "SetVisibleToAllUsersInputRequestTypeDef",
    {
        "JobFlowIds": Sequence[str],
        "VisibleToAllUsers": bool,
    },
)
StepExecutionStatusDetailTypeDef = TypedDict(
    "StepExecutionStatusDetailTypeDef",
    {
        "State": StepExecutionStateType,
        "CreationDateTime": datetime,
        "StartDateTime": NotRequired[datetime],
        "EndDateTime": NotRequired[datetime],
        "LastStateChangeReason": NotRequired[str],
    },
)
StepStateChangeReasonTypeDef = TypedDict(
    "StepStateChangeReasonTypeDef",
    {
        "Code": NotRequired[Literal["NONE"]],
        "Message": NotRequired[str],
    },
)
StepTimelineTypeDef = TypedDict(
    "StepTimelineTypeDef",
    {
        "CreationDateTime": NotRequired[datetime],
        "StartDateTime": NotRequired[datetime],
        "EndDateTime": NotRequired[datetime],
    },
)
StopNotebookExecutionInputRequestTypeDef = TypedDict(
    "StopNotebookExecutionInputRequestTypeDef",
    {
        "NotebookExecutionId": str,
    },
)
TerminateJobFlowsInputRequestTypeDef = TypedDict(
    "TerminateJobFlowsInputRequestTypeDef",
    {
        "JobFlowIds": Sequence[str],
    },
)
UpdateStudioInputRequestTypeDef = TypedDict(
    "UpdateStudioInputRequestTypeDef",
    {
        "StudioId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "SubnetIds": NotRequired[Sequence[str]],
        "DefaultS3Location": NotRequired[str],
        "EncryptionKeyArn": NotRequired[str],
    },
)
UpdateStudioSessionMappingInputRequestTypeDef = TypedDict(
    "UpdateStudioSessionMappingInputRequestTypeDef",
    {
        "StudioId": str,
        "IdentityType": IdentityTypeType,
        "SessionPolicyArn": str,
        "IdentityId": NotRequired[str],
        "IdentityName": NotRequired[str],
    },
)
AddInstanceFleetOutputTypeDef = TypedDict(
    "AddInstanceFleetOutputTypeDef",
    {
        "ClusterId": str,
        "InstanceFleetId": str,
        "ClusterArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AddInstanceGroupsOutputTypeDef = TypedDict(
    "AddInstanceGroupsOutputTypeDef",
    {
        "JobFlowId": str,
        "InstanceGroupIds": List[str],
        "ClusterArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AddJobFlowStepsOutputTypeDef = TypedDict(
    "AddJobFlowStepsOutputTypeDef",
    {
        "StepIds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSecurityConfigurationOutputTypeDef = TypedDict(
    "CreateSecurityConfigurationOutputTypeDef",
    {
        "Name": str,
        "CreationDateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateStudioOutputTypeDef = TypedDict(
    "CreateStudioOutputTypeDef",
    {
        "StudioId": str,
        "Url": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSecurityConfigurationOutputTypeDef = TypedDict(
    "DescribeSecurityConfigurationOutputTypeDef",
    {
        "Name": str,
        "SecurityConfiguration": str,
        "CreationDateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListReleaseLabelsOutputTypeDef = TypedDict(
    "ListReleaseLabelsOutputTypeDef",
    {
        "ReleaseLabels": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ModifyClusterOutputTypeDef = TypedDict(
    "ModifyClusterOutputTypeDef",
    {
        "StepConcurrencyLevel": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RunJobFlowOutputTypeDef = TypedDict(
    "RunJobFlowOutputTypeDef",
    {
        "JobFlowId": str,
        "ClusterArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartNotebookExecutionOutputTypeDef = TypedDict(
    "StartNotebookExecutionOutputTypeDef",
    {
        "NotebookExecutionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AddTagsInputRequestTypeDef = TypedDict(
    "AddTagsInputRequestTypeDef",
    {
        "ResourceId": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CreateStudioInputRequestTypeDef = TypedDict(
    "CreateStudioInputRequestTypeDef",
    {
        "Name": str,
        "AuthMode": AuthModeType,
        "VpcId": str,
        "SubnetIds": Sequence[str],
        "ServiceRole": str,
        "WorkspaceSecurityGroupId": str,
        "EngineSecurityGroupId": str,
        "DefaultS3Location": str,
        "Description": NotRequired[str],
        "UserRole": NotRequired[str],
        "IdpAuthUrl": NotRequired[str],
        "IdpRelayStateParameterName": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "TrustedIdentityPropagationEnabled": NotRequired[bool],
        "IdcUserAssignment": NotRequired[IdcUserAssignmentType],
        "IdcInstanceArn": NotRequired[str],
        "EncryptionKeyArn": NotRequired[str],
    },
)
StudioTypeDef = TypedDict(
    "StudioTypeDef",
    {
        "StudioId": NotRequired[str],
        "StudioArn": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "AuthMode": NotRequired[AuthModeType],
        "VpcId": NotRequired[str],
        "SubnetIds": NotRequired[List[str]],
        "ServiceRole": NotRequired[str],
        "UserRole": NotRequired[str],
        "WorkspaceSecurityGroupId": NotRequired[str],
        "EngineSecurityGroupId": NotRequired[str],
        "Url": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "DefaultS3Location": NotRequired[str],
        "IdpAuthUrl": NotRequired[str],
        "IdpRelayStateParameterName": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "IdcInstanceArn": NotRequired[str],
        "TrustedIdentityPropagationEnabled": NotRequired[bool],
        "IdcUserAssignment": NotRequired[IdcUserAssignmentType],
        "EncryptionKeyArn": NotRequired[str],
    },
)
ApplicationUnionTypeDef = Union[ApplicationTypeDef, ApplicationOutputTypeDef]
AutoScalingPolicyStatusTypeDef = TypedDict(
    "AutoScalingPolicyStatusTypeDef",
    {
        "State": NotRequired[AutoScalingPolicyStateType],
        "StateChangeReason": NotRequired[AutoScalingPolicyStateChangeReasonTypeDef],
    },
)
GetAutoTerminationPolicyOutputTypeDef = TypedDict(
    "GetAutoTerminationPolicyOutputTypeDef",
    {
        "AutoTerminationPolicy": AutoTerminationPolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutAutoTerminationPolicyInputRequestTypeDef = TypedDict(
    "PutAutoTerminationPolicyInputRequestTypeDef",
    {
        "ClusterId": str,
        "AutoTerminationPolicy": NotRequired[AutoTerminationPolicyTypeDef],
    },
)
BlockPublicAccessConfigurationOutputTypeDef = TypedDict(
    "BlockPublicAccessConfigurationOutputTypeDef",
    {
        "BlockPublicSecurityGroupRules": bool,
        "PermittedPublicSecurityGroupRuleRanges": NotRequired[List[PortRangeTypeDef]],
    },
)
BlockPublicAccessConfigurationTypeDef = TypedDict(
    "BlockPublicAccessConfigurationTypeDef",
    {
        "BlockPublicSecurityGroupRules": bool,
        "PermittedPublicSecurityGroupRuleRanges": NotRequired[Sequence[PortRangeTypeDef]],
    },
)
BootstrapActionConfigOutputTypeDef = TypedDict(
    "BootstrapActionConfigOutputTypeDef",
    {
        "Name": str,
        "ScriptBootstrapAction": ScriptBootstrapActionConfigOutputTypeDef,
    },
)
CancelStepsOutputTypeDef = TypedDict(
    "CancelStepsOutputTypeDef",
    {
        "CancelStepsInfoList": List[CancelStepsInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CloudWatchAlarmDefinitionOutputTypeDef = TypedDict(
    "CloudWatchAlarmDefinitionOutputTypeDef",
    {
        "ComparisonOperator": ComparisonOperatorType,
        "MetricName": str,
        "Period": int,
        "Threshold": float,
        "EvaluationPeriods": NotRequired[int],
        "Namespace": NotRequired[str],
        "Statistic": NotRequired[StatisticType],
        "Unit": NotRequired[UnitType],
        "Dimensions": NotRequired[List[MetricDimensionTypeDef]],
    },
)
CloudWatchAlarmDefinitionTypeDef = TypedDict(
    "CloudWatchAlarmDefinitionTypeDef",
    {
        "ComparisonOperator": ComparisonOperatorType,
        "MetricName": str,
        "Period": int,
        "Threshold": float,
        "EvaluationPeriods": NotRequired[int],
        "Namespace": NotRequired[str],
        "Statistic": NotRequired[StatisticType],
        "Unit": NotRequired[UnitType],
        "Dimensions": NotRequired[Sequence[MetricDimensionTypeDef]],
    },
)
ClusterStatusTypeDef = TypedDict(
    "ClusterStatusTypeDef",
    {
        "State": NotRequired[ClusterStateType],
        "StateChangeReason": NotRequired[ClusterStateChangeReasonTypeDef],
        "Timeline": NotRequired[ClusterTimelineTypeDef],
        "ErrorDetails": NotRequired[List[ErrorDetailTypeDef]],
    },
)
ListBootstrapActionsOutputTypeDef = TypedDict(
    "ListBootstrapActionsOutputTypeDef",
    {
        "BootstrapActions": List[CommandTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ManagedScalingPolicyTypeDef = TypedDict(
    "ManagedScalingPolicyTypeDef",
    {
        "ComputeLimits": NotRequired[ComputeLimitsTypeDef],
    },
)
ConfigurationUnionTypeDef = Union[ConfigurationTypeDef, ConfigurationOutputTypeDef]
CredentialsTypeDef = TypedDict(
    "CredentialsTypeDef",
    {
        "UsernamePassword": NotRequired[UsernamePasswordTypeDef],
    },
)
DescribeClusterInputClusterRunningWaitTypeDef = TypedDict(
    "DescribeClusterInputClusterRunningWaitTypeDef",
    {
        "ClusterId": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeClusterInputClusterTerminatedWaitTypeDef = TypedDict(
    "DescribeClusterInputClusterTerminatedWaitTypeDef",
    {
        "ClusterId": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeStepInputStepCompleteWaitTypeDef = TypedDict(
    "DescribeStepInputStepCompleteWaitTypeDef",
    {
        "ClusterId": str,
        "StepId": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeJobFlowsInputRequestTypeDef = TypedDict(
    "DescribeJobFlowsInputRequestTypeDef",
    {
        "CreatedAfter": NotRequired[TimestampTypeDef],
        "CreatedBefore": NotRequired[TimestampTypeDef],
        "JobFlowIds": NotRequired[Sequence[str]],
        "JobFlowStates": NotRequired[Sequence[JobFlowExecutionStateType]],
    },
)
ListClustersInputRequestTypeDef = TypedDict(
    "ListClustersInputRequestTypeDef",
    {
        "CreatedAfter": NotRequired[TimestampTypeDef],
        "CreatedBefore": NotRequired[TimestampTypeDef],
        "ClusterStates": NotRequired[Sequence[ClusterStateType]],
        "Marker": NotRequired[str],
    },
)
ListNotebookExecutionsInputRequestTypeDef = TypedDict(
    "ListNotebookExecutionsInputRequestTypeDef",
    {
        "EditorId": NotRequired[str],
        "Status": NotRequired[NotebookExecutionStatusType],
        "From": NotRequired[TimestampTypeDef],
        "To": NotRequired[TimestampTypeDef],
        "Marker": NotRequired[str],
        "ExecutionEngineId": NotRequired[str],
    },
)
DescribeReleaseLabelOutputTypeDef = TypedDict(
    "DescribeReleaseLabelOutputTypeDef",
    {
        "ReleaseLabel": str,
        "Applications": List[SimplifiedApplicationTypeDef],
        "AvailableOSReleases": List[OSReleaseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
EbsBlockDeviceConfigTypeDef = TypedDict(
    "EbsBlockDeviceConfigTypeDef",
    {
        "VolumeSpecification": VolumeSpecificationTypeDef,
        "VolumesPerInstance": NotRequired[int],
    },
)
EbsBlockDeviceTypeDef = TypedDict(
    "EbsBlockDeviceTypeDef",
    {
        "VolumeSpecification": NotRequired[VolumeSpecificationTypeDef],
        "Device": NotRequired[str],
    },
)
GetStudioSessionMappingOutputTypeDef = TypedDict(
    "GetStudioSessionMappingOutputTypeDef",
    {
        "SessionMapping": SessionMappingDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
HadoopJarStepConfigOutputTypeDef = TypedDict(
    "HadoopJarStepConfigOutputTypeDef",
    {
        "Jar": str,
        "Properties": NotRequired[List[KeyValueTypeDef]],
        "MainClass": NotRequired[str],
        "Args": NotRequired[List[str]],
    },
)
HadoopJarStepConfigTypeDef = TypedDict(
    "HadoopJarStepConfigTypeDef",
    {
        "Jar": str,
        "Properties": NotRequired[Sequence[KeyValueTypeDef]],
        "MainClass": NotRequired[str],
        "Args": NotRequired[Sequence[str]],
    },
)
InstanceFleetStatusTypeDef = TypedDict(
    "InstanceFleetStatusTypeDef",
    {
        "State": NotRequired[InstanceFleetStateType],
        "StateChangeReason": NotRequired[InstanceFleetStateChangeReasonTypeDef],
        "Timeline": NotRequired[InstanceFleetTimelineTypeDef],
    },
)
InstanceGroupStatusTypeDef = TypedDict(
    "InstanceGroupStatusTypeDef",
    {
        "State": NotRequired[InstanceGroupStateType],
        "StateChangeReason": NotRequired[InstanceGroupStateChangeReasonTypeDef],
        "Timeline": NotRequired[InstanceGroupTimelineTypeDef],
    },
)
ShrinkPolicyOutputTypeDef = TypedDict(
    "ShrinkPolicyOutputTypeDef",
    {
        "DecommissionTimeout": NotRequired[int],
        "InstanceResizePolicy": NotRequired[InstanceResizePolicyOutputTypeDef],
    },
)
InstanceResizePolicyUnionTypeDef = Union[
    InstanceResizePolicyTypeDef, InstanceResizePolicyOutputTypeDef
]
InstanceStatusTypeDef = TypedDict(
    "InstanceStatusTypeDef",
    {
        "State": NotRequired[InstanceStateType],
        "StateChangeReason": NotRequired[InstanceStateChangeReasonTypeDef],
        "Timeline": NotRequired[InstanceTimelineTypeDef],
    },
)
JobFlowInstancesDetailTypeDef = TypedDict(
    "JobFlowInstancesDetailTypeDef",
    {
        "MasterInstanceType": str,
        "SlaveInstanceType": str,
        "InstanceCount": int,
        "MasterPublicDnsName": NotRequired[str],
        "MasterInstanceId": NotRequired[str],
        "InstanceGroups": NotRequired[List[InstanceGroupDetailTypeDef]],
        "NormalizedInstanceHours": NotRequired[int],
        "Ec2KeyName": NotRequired[str],
        "Ec2SubnetId": NotRequired[str],
        "Placement": NotRequired[PlacementTypeOutputTypeDef],
        "KeepJobFlowAliveWhenNoSteps": NotRequired[bool],
        "TerminationProtected": NotRequired[bool],
        "UnhealthyNodeReplacement": NotRequired[bool],
        "HadoopVersion": NotRequired[str],
    },
)
ListBootstrapActionsInputListBootstrapActionsPaginateTypeDef = TypedDict(
    "ListBootstrapActionsInputListBootstrapActionsPaginateTypeDef",
    {
        "ClusterId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListClustersInputListClustersPaginateTypeDef = TypedDict(
    "ListClustersInputListClustersPaginateTypeDef",
    {
        "CreatedAfter": NotRequired[TimestampTypeDef],
        "CreatedBefore": NotRequired[TimestampTypeDef],
        "ClusterStates": NotRequired[Sequence[ClusterStateType]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListInstanceFleetsInputListInstanceFleetsPaginateTypeDef = TypedDict(
    "ListInstanceFleetsInputListInstanceFleetsPaginateTypeDef",
    {
        "ClusterId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListInstanceGroupsInputListInstanceGroupsPaginateTypeDef = TypedDict(
    "ListInstanceGroupsInputListInstanceGroupsPaginateTypeDef",
    {
        "ClusterId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListInstancesInputListInstancesPaginateTypeDef = TypedDict(
    "ListInstancesInputListInstancesPaginateTypeDef",
    {
        "ClusterId": str,
        "InstanceGroupId": NotRequired[str],
        "InstanceGroupTypes": NotRequired[Sequence[InstanceGroupTypeType]],
        "InstanceFleetId": NotRequired[str],
        "InstanceFleetType": NotRequired[InstanceFleetTypeType],
        "InstanceStates": NotRequired[Sequence[InstanceStateType]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListNotebookExecutionsInputListNotebookExecutionsPaginateTypeDef = TypedDict(
    "ListNotebookExecutionsInputListNotebookExecutionsPaginateTypeDef",
    {
        "EditorId": NotRequired[str],
        "Status": NotRequired[NotebookExecutionStatusType],
        "From": NotRequired[TimestampTypeDef],
        "To": NotRequired[TimestampTypeDef],
        "ExecutionEngineId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSecurityConfigurationsInputListSecurityConfigurationsPaginateTypeDef = TypedDict(
    "ListSecurityConfigurationsInputListSecurityConfigurationsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListStepsInputListStepsPaginateTypeDef = TypedDict(
    "ListStepsInputListStepsPaginateTypeDef",
    {
        "ClusterId": str,
        "StepStates": NotRequired[Sequence[StepStateType]],
        "StepIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListStudioSessionMappingsInputListStudioSessionMappingsPaginateTypeDef = TypedDict(
    "ListStudioSessionMappingsInputListStudioSessionMappingsPaginateTypeDef",
    {
        "StudioId": NotRequired[str],
        "IdentityType": NotRequired[IdentityTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListStudiosInputListStudiosPaginateTypeDef = TypedDict(
    "ListStudiosInputListStudiosPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListReleaseLabelsInputRequestTypeDef = TypedDict(
    "ListReleaseLabelsInputRequestTypeDef",
    {
        "Filters": NotRequired[ReleaseLabelFilterTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListSecurityConfigurationsOutputTypeDef = TypedDict(
    "ListSecurityConfigurationsOutputTypeDef",
    {
        "SecurityConfigurations": List[SecurityConfigurationSummaryTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListStudioSessionMappingsOutputTypeDef = TypedDict(
    "ListStudioSessionMappingsOutputTypeDef",
    {
        "SessionMappings": List[SessionMappingSummaryTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListStudiosOutputTypeDef = TypedDict(
    "ListStudiosOutputTypeDef",
    {
        "Studios": List[StudioSummaryTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSupportedInstanceTypesOutputTypeDef = TypedDict(
    "ListSupportedInstanceTypesOutputTypeDef",
    {
        "SupportedInstanceTypes": List[SupportedInstanceTypeTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NotebookExecutionSummaryTypeDef = TypedDict(
    "NotebookExecutionSummaryTypeDef",
    {
        "NotebookExecutionId": NotRequired[str],
        "EditorId": NotRequired[str],
        "NotebookExecutionName": NotRequired[str],
        "Status": NotRequired[NotebookExecutionStatusType],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "NotebookS3Location": NotRequired[NotebookS3LocationForOutputTypeDef],
        "ExecutionEngineId": NotRequired[str],
    },
)
NotebookExecutionTypeDef = TypedDict(
    "NotebookExecutionTypeDef",
    {
        "NotebookExecutionId": NotRequired[str],
        "EditorId": NotRequired[str],
        "ExecutionEngine": NotRequired[ExecutionEngineConfigTypeDef],
        "NotebookExecutionName": NotRequired[str],
        "NotebookParams": NotRequired[str],
        "Status": NotRequired[NotebookExecutionStatusType],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "Arn": NotRequired[str],
        "OutputNotebookURI": NotRequired[str],
        "LastStateChangeReason": NotRequired[str],
        "NotebookInstanceSecurityGroupId": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "NotebookS3Location": NotRequired[NotebookS3LocationForOutputTypeDef],
        "OutputNotebookS3Location": NotRequired[OutputNotebookS3LocationForOutputTypeDef],
        "OutputNotebookFormat": NotRequired[Literal["HTML"]],
        "EnvironmentVariables": NotRequired[Dict[str, str]],
    },
)
OnDemandProvisioningSpecificationTypeDef = TypedDict(
    "OnDemandProvisioningSpecificationTypeDef",
    {
        "AllocationStrategy": OnDemandProvisioningAllocationStrategyType,
        "CapacityReservationOptions": NotRequired[OnDemandCapacityReservationOptionsTypeDef],
    },
)
OnDemandResizingSpecificationTypeDef = TypedDict(
    "OnDemandResizingSpecificationTypeDef",
    {
        "TimeoutDurationMinutes": NotRequired[int],
        "AllocationStrategy": NotRequired[OnDemandProvisioningAllocationStrategyType],
        "CapacityReservationOptions": NotRequired[OnDemandCapacityReservationOptionsTypeDef],
    },
)
StartNotebookExecutionInputRequestTypeDef = TypedDict(
    "StartNotebookExecutionInputRequestTypeDef",
    {
        "ExecutionEngine": ExecutionEngineConfigTypeDef,
        "ServiceRole": str,
        "EditorId": NotRequired[str],
        "RelativePath": NotRequired[str],
        "NotebookExecutionName": NotRequired[str],
        "NotebookParams": NotRequired[str],
        "NotebookInstanceSecurityGroupId": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "NotebookS3Location": NotRequired[NotebookS3LocationFromInputTypeDef],
        "OutputNotebookS3Location": NotRequired[OutputNotebookS3LocationFromInputTypeDef],
        "OutputNotebookFormat": NotRequired[Literal["HTML"]],
        "EnvironmentVariables": NotRequired[Mapping[str, str]],
    },
)
PlacementTypeUnionTypeDef = Union[PlacementTypeTypeDef, PlacementTypeOutputTypeDef]
ScalingActionTypeDef = TypedDict(
    "ScalingActionTypeDef",
    {
        "SimpleScalingPolicyConfiguration": SimpleScalingPolicyConfigurationTypeDef,
        "Market": NotRequired[MarketTypeType],
    },
)
ScriptBootstrapActionConfigUnionTypeDef = Union[
    ScriptBootstrapActionConfigTypeDef, ScriptBootstrapActionConfigOutputTypeDef
]
StepStatusTypeDef = TypedDict(
    "StepStatusTypeDef",
    {
        "State": NotRequired[StepStateType],
        "StateChangeReason": NotRequired[StepStateChangeReasonTypeDef],
        "FailureDetails": NotRequired[FailureDetailsTypeDef],
        "Timeline": NotRequired[StepTimelineTypeDef],
    },
)
DescribeStudioOutputTypeDef = TypedDict(
    "DescribeStudioOutputTypeDef",
    {
        "Studio": StudioTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBlockPublicAccessConfigurationOutputTypeDef = TypedDict(
    "GetBlockPublicAccessConfigurationOutputTypeDef",
    {
        "BlockPublicAccessConfiguration": BlockPublicAccessConfigurationOutputTypeDef,
        "BlockPublicAccessConfigurationMetadata": BlockPublicAccessConfigurationMetadataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutBlockPublicAccessConfigurationInputRequestTypeDef = TypedDict(
    "PutBlockPublicAccessConfigurationInputRequestTypeDef",
    {
        "BlockPublicAccessConfiguration": BlockPublicAccessConfigurationTypeDef,
    },
)
BootstrapActionDetailTypeDef = TypedDict(
    "BootstrapActionDetailTypeDef",
    {
        "BootstrapActionConfig": NotRequired[BootstrapActionConfigOutputTypeDef],
    },
)
ScalingTriggerOutputTypeDef = TypedDict(
    "ScalingTriggerOutputTypeDef",
    {
        "CloudWatchAlarmDefinition": CloudWatchAlarmDefinitionOutputTypeDef,
    },
)
CloudWatchAlarmDefinitionUnionTypeDef = Union[
    CloudWatchAlarmDefinitionTypeDef, CloudWatchAlarmDefinitionOutputTypeDef
]
ClusterSummaryTypeDef = TypedDict(
    "ClusterSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired[ClusterStatusTypeDef],
        "NormalizedInstanceHours": NotRequired[int],
        "ClusterArn": NotRequired[str],
        "OutpostArn": NotRequired[str],
    },
)
ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired[ClusterStatusTypeDef],
        "Ec2InstanceAttributes": NotRequired[Ec2InstanceAttributesTypeDef],
        "InstanceCollectionType": NotRequired[InstanceCollectionTypeType],
        "LogUri": NotRequired[str],
        "LogEncryptionKmsKeyId": NotRequired[str],
        "RequestedAmiVersion": NotRequired[str],
        "RunningAmiVersion": NotRequired[str],
        "ReleaseLabel": NotRequired[str],
        "AutoTerminate": NotRequired[bool],
        "TerminationProtected": NotRequired[bool],
        "UnhealthyNodeReplacement": NotRequired[bool],
        "VisibleToAllUsers": NotRequired[bool],
        "Applications": NotRequired[List[ApplicationOutputTypeDef]],
        "Tags": NotRequired[List[TagTypeDef]],
        "ServiceRole": NotRequired[str],
        "NormalizedInstanceHours": NotRequired[int],
        "MasterPublicDnsName": NotRequired[str],
        "Configurations": NotRequired[List[ConfigurationOutputTypeDef]],
        "SecurityConfiguration": NotRequired[str],
        "AutoScalingRole": NotRequired[str],
        "ScaleDownBehavior": NotRequired[ScaleDownBehaviorType],
        "CustomAmiId": NotRequired[str],
        "EbsRootVolumeSize": NotRequired[int],
        "RepoUpgradeOnBoot": NotRequired[RepoUpgradeOnBootType],
        "KerberosAttributes": NotRequired[KerberosAttributesTypeDef],
        "ClusterArn": NotRequired[str],
        "OutpostArn": NotRequired[str],
        "StepConcurrencyLevel": NotRequired[int],
        "PlacementGroups": NotRequired[List[PlacementGroupConfigTypeDef]],
        "OSReleaseLabel": NotRequired[str],
        "EbsRootVolumeIops": NotRequired[int],
        "EbsRootVolumeThroughput": NotRequired[int],
    },
)
GetManagedScalingPolicyOutputTypeDef = TypedDict(
    "GetManagedScalingPolicyOutputTypeDef",
    {
        "ManagedScalingPolicy": ManagedScalingPolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutManagedScalingPolicyInputRequestTypeDef = TypedDict(
    "PutManagedScalingPolicyInputRequestTypeDef",
    {
        "ClusterId": str,
        "ManagedScalingPolicy": ManagedScalingPolicyTypeDef,
    },
)
GetClusterSessionCredentialsOutputTypeDef = TypedDict(
    "GetClusterSessionCredentialsOutputTypeDef",
    {
        "Credentials": CredentialsTypeDef,
        "ExpiresAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EbsConfigurationTypeDef = TypedDict(
    "EbsConfigurationTypeDef",
    {
        "EbsBlockDeviceConfigs": NotRequired[Sequence[EbsBlockDeviceConfigTypeDef]],
        "EbsOptimized": NotRequired[bool],
    },
)
InstanceTypeSpecificationPaginatorTypeDef = TypedDict(
    "InstanceTypeSpecificationPaginatorTypeDef",
    {
        "InstanceType": NotRequired[str],
        "WeightedCapacity": NotRequired[int],
        "BidPrice": NotRequired[str],
        "BidPriceAsPercentageOfOnDemandPrice": NotRequired[float],
        "Configurations": NotRequired[List[ConfigurationPaginatorTypeDef]],
        "EbsBlockDevices": NotRequired[List[EbsBlockDeviceTypeDef]],
        "EbsOptimized": NotRequired[bool],
        "CustomAmiId": NotRequired[str],
        "Priority": NotRequired[float],
    },
)
InstanceTypeSpecificationTypeDef = TypedDict(
    "InstanceTypeSpecificationTypeDef",
    {
        "InstanceType": NotRequired[str],
        "WeightedCapacity": NotRequired[int],
        "BidPrice": NotRequired[str],
        "BidPriceAsPercentageOfOnDemandPrice": NotRequired[float],
        "Configurations": NotRequired[List[ConfigurationOutputTypeDef]],
        "EbsBlockDevices": NotRequired[List[EbsBlockDeviceTypeDef]],
        "EbsOptimized": NotRequired[bool],
        "CustomAmiId": NotRequired[str],
        "Priority": NotRequired[float],
    },
)
StepConfigOutputTypeDef = TypedDict(
    "StepConfigOutputTypeDef",
    {
        "Name": str,
        "HadoopJarStep": HadoopJarStepConfigOutputTypeDef,
        "ActionOnFailure": NotRequired[ActionOnFailureType],
    },
)
HadoopJarStepConfigUnionTypeDef = Union[
    HadoopJarStepConfigTypeDef, HadoopJarStepConfigOutputTypeDef
]
ShrinkPolicyTypeDef = TypedDict(
    "ShrinkPolicyTypeDef",
    {
        "DecommissionTimeout": NotRequired[int],
        "InstanceResizePolicy": NotRequired[InstanceResizePolicyUnionTypeDef],
    },
)
InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "Id": NotRequired[str],
        "Ec2InstanceId": NotRequired[str],
        "PublicDnsName": NotRequired[str],
        "PublicIpAddress": NotRequired[str],
        "PrivateDnsName": NotRequired[str],
        "PrivateIpAddress": NotRequired[str],
        "Status": NotRequired[InstanceStatusTypeDef],
        "InstanceGroupId": NotRequired[str],
        "InstanceFleetId": NotRequired[str],
        "Market": NotRequired[MarketTypeType],
        "InstanceType": NotRequired[str],
        "EbsVolumes": NotRequired[List[EbsVolumeTypeDef]],
    },
)
ListNotebookExecutionsOutputTypeDef = TypedDict(
    "ListNotebookExecutionsOutputTypeDef",
    {
        "NotebookExecutions": List[NotebookExecutionSummaryTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeNotebookExecutionOutputTypeDef = TypedDict(
    "DescribeNotebookExecutionOutputTypeDef",
    {
        "NotebookExecution": NotebookExecutionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InstanceFleetProvisioningSpecificationsTypeDef = TypedDict(
    "InstanceFleetProvisioningSpecificationsTypeDef",
    {
        "SpotSpecification": NotRequired[SpotProvisioningSpecificationTypeDef],
        "OnDemandSpecification": NotRequired[OnDemandProvisioningSpecificationTypeDef],
    },
)
InstanceFleetResizingSpecificationsTypeDef = TypedDict(
    "InstanceFleetResizingSpecificationsTypeDef",
    {
        "SpotResizeSpecification": NotRequired[SpotResizingSpecificationTypeDef],
        "OnDemandResizeSpecification": NotRequired[OnDemandResizingSpecificationTypeDef],
    },
)
BootstrapActionConfigTypeDef = TypedDict(
    "BootstrapActionConfigTypeDef",
    {
        "Name": str,
        "ScriptBootstrapAction": ScriptBootstrapActionConfigUnionTypeDef,
    },
)
StepSummaryTypeDef = TypedDict(
    "StepSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Config": NotRequired[HadoopStepConfigTypeDef],
        "ActionOnFailure": NotRequired[ActionOnFailureType],
        "Status": NotRequired[StepStatusTypeDef],
    },
)
StepTypeDef = TypedDict(
    "StepTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Config": NotRequired[HadoopStepConfigTypeDef],
        "ActionOnFailure": NotRequired[ActionOnFailureType],
        "Status": NotRequired[StepStatusTypeDef],
        "ExecutionRoleArn": NotRequired[str],
    },
)
ScalingRuleOutputTypeDef = TypedDict(
    "ScalingRuleOutputTypeDef",
    {
        "Name": str,
        "Action": ScalingActionTypeDef,
        "Trigger": ScalingTriggerOutputTypeDef,
        "Description": NotRequired[str],
    },
)
ScalingTriggerTypeDef = TypedDict(
    "ScalingTriggerTypeDef",
    {
        "CloudWatchAlarmDefinition": CloudWatchAlarmDefinitionUnionTypeDef,
    },
)
ListClustersOutputTypeDef = TypedDict(
    "ListClustersOutputTypeDef",
    {
        "Clusters": List[ClusterSummaryTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeClusterOutputTypeDef = TypedDict(
    "DescribeClusterOutputTypeDef",
    {
        "Cluster": ClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InstanceTypeConfigTypeDef = TypedDict(
    "InstanceTypeConfigTypeDef",
    {
        "InstanceType": str,
        "WeightedCapacity": NotRequired[int],
        "BidPrice": NotRequired[str],
        "BidPriceAsPercentageOfOnDemandPrice": NotRequired[float],
        "EbsConfiguration": NotRequired[EbsConfigurationTypeDef],
        "Configurations": NotRequired[Sequence[ConfigurationUnionTypeDef]],
        "CustomAmiId": NotRequired[str],
        "Priority": NotRequired[float],
    },
)
StepDetailTypeDef = TypedDict(
    "StepDetailTypeDef",
    {
        "StepConfig": StepConfigOutputTypeDef,
        "ExecutionStatusDetail": StepExecutionStatusDetailTypeDef,
    },
)
StepConfigTypeDef = TypedDict(
    "StepConfigTypeDef",
    {
        "Name": str,
        "HadoopJarStep": HadoopJarStepConfigUnionTypeDef,
        "ActionOnFailure": NotRequired[ActionOnFailureType],
    },
)
ShrinkPolicyUnionTypeDef = Union[ShrinkPolicyTypeDef, ShrinkPolicyOutputTypeDef]
ListInstancesOutputTypeDef = TypedDict(
    "ListInstancesOutputTypeDef",
    {
        "Instances": List[InstanceTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InstanceFleetPaginatorTypeDef = TypedDict(
    "InstanceFleetPaginatorTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired[InstanceFleetStatusTypeDef],
        "InstanceFleetType": NotRequired[InstanceFleetTypeType],
        "TargetOnDemandCapacity": NotRequired[int],
        "TargetSpotCapacity": NotRequired[int],
        "ProvisionedOnDemandCapacity": NotRequired[int],
        "ProvisionedSpotCapacity": NotRequired[int],
        "InstanceTypeSpecifications": NotRequired[List[InstanceTypeSpecificationPaginatorTypeDef]],
        "LaunchSpecifications": NotRequired[InstanceFleetProvisioningSpecificationsTypeDef],
        "ResizeSpecifications": NotRequired[InstanceFleetResizingSpecificationsTypeDef],
        "Context": NotRequired[str],
    },
)
InstanceFleetTypeDef = TypedDict(
    "InstanceFleetTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired[InstanceFleetStatusTypeDef],
        "InstanceFleetType": NotRequired[InstanceFleetTypeType],
        "TargetOnDemandCapacity": NotRequired[int],
        "TargetSpotCapacity": NotRequired[int],
        "ProvisionedOnDemandCapacity": NotRequired[int],
        "ProvisionedSpotCapacity": NotRequired[int],
        "InstanceTypeSpecifications": NotRequired[List[InstanceTypeSpecificationTypeDef]],
        "LaunchSpecifications": NotRequired[InstanceFleetProvisioningSpecificationsTypeDef],
        "ResizeSpecifications": NotRequired[InstanceFleetResizingSpecificationsTypeDef],
        "Context": NotRequired[str],
    },
)
BootstrapActionConfigUnionTypeDef = Union[
    BootstrapActionConfigTypeDef, BootstrapActionConfigOutputTypeDef
]
ListStepsOutputTypeDef = TypedDict(
    "ListStepsOutputTypeDef",
    {
        "Steps": List[StepSummaryTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeStepOutputTypeDef = TypedDict(
    "DescribeStepOutputTypeDef",
    {
        "Step": StepTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AutoScalingPolicyDescriptionTypeDef = TypedDict(
    "AutoScalingPolicyDescriptionTypeDef",
    {
        "Status": NotRequired[AutoScalingPolicyStatusTypeDef],
        "Constraints": NotRequired[ScalingConstraintsTypeDef],
        "Rules": NotRequired[List[ScalingRuleOutputTypeDef]],
    },
)
ScalingTriggerUnionTypeDef = Union[ScalingTriggerTypeDef, ScalingTriggerOutputTypeDef]
InstanceFleetConfigTypeDef = TypedDict(
    "InstanceFleetConfigTypeDef",
    {
        "InstanceFleetType": InstanceFleetTypeType,
        "Name": NotRequired[str],
        "TargetOnDemandCapacity": NotRequired[int],
        "TargetSpotCapacity": NotRequired[int],
        "InstanceTypeConfigs": NotRequired[Sequence[InstanceTypeConfigTypeDef]],
        "LaunchSpecifications": NotRequired[InstanceFleetProvisioningSpecificationsTypeDef],
        "ResizeSpecifications": NotRequired[InstanceFleetResizingSpecificationsTypeDef],
        "Context": NotRequired[str],
    },
)
InstanceFleetModifyConfigTypeDef = TypedDict(
    "InstanceFleetModifyConfigTypeDef",
    {
        "InstanceFleetId": str,
        "TargetOnDemandCapacity": NotRequired[int],
        "TargetSpotCapacity": NotRequired[int],
        "ResizeSpecifications": NotRequired[InstanceFleetResizingSpecificationsTypeDef],
        "InstanceTypeConfigs": NotRequired[Sequence[InstanceTypeConfigTypeDef]],
        "Context": NotRequired[str],
    },
)
JobFlowDetailTypeDef = TypedDict(
    "JobFlowDetailTypeDef",
    {
        "JobFlowId": str,
        "Name": str,
        "ExecutionStatusDetail": JobFlowExecutionStatusDetailTypeDef,
        "Instances": JobFlowInstancesDetailTypeDef,
        "LogUri": NotRequired[str],
        "LogEncryptionKmsKeyId": NotRequired[str],
        "AmiVersion": NotRequired[str],
        "Steps": NotRequired[List[StepDetailTypeDef]],
        "BootstrapActions": NotRequired[List[BootstrapActionDetailTypeDef]],
        "SupportedProducts": NotRequired[List[str]],
        "VisibleToAllUsers": NotRequired[bool],
        "JobFlowRole": NotRequired[str],
        "ServiceRole": NotRequired[str],
        "AutoScalingRole": NotRequired[str],
        "ScaleDownBehavior": NotRequired[ScaleDownBehaviorType],
    },
)
StepConfigUnionTypeDef = Union[StepConfigTypeDef, StepConfigOutputTypeDef]
InstanceGroupModifyConfigTypeDef = TypedDict(
    "InstanceGroupModifyConfigTypeDef",
    {
        "InstanceGroupId": str,
        "InstanceCount": NotRequired[int],
        "EC2InstanceIdsToTerminate": NotRequired[Sequence[str]],
        "ShrinkPolicy": NotRequired[ShrinkPolicyUnionTypeDef],
        "ReconfigurationType": NotRequired[ReconfigurationTypeType],
        "Configurations": NotRequired[Sequence[ConfigurationUnionTypeDef]],
    },
)
ListInstanceFleetsOutputPaginatorTypeDef = TypedDict(
    "ListInstanceFleetsOutputPaginatorTypeDef",
    {
        "InstanceFleets": List[InstanceFleetPaginatorTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListInstanceFleetsOutputTypeDef = TypedDict(
    "ListInstanceFleetsOutputTypeDef",
    {
        "InstanceFleets": List[InstanceFleetTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InstanceGroupPaginatorTypeDef = TypedDict(
    "InstanceGroupPaginatorTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Market": NotRequired[MarketTypeType],
        "InstanceGroupType": NotRequired[InstanceGroupTypeType],
        "BidPrice": NotRequired[str],
        "InstanceType": NotRequired[str],
        "RequestedInstanceCount": NotRequired[int],
        "RunningInstanceCount": NotRequired[int],
        "Status": NotRequired[InstanceGroupStatusTypeDef],
        "Configurations": NotRequired[List[ConfigurationPaginatorTypeDef]],
        "ConfigurationsVersion": NotRequired[int],
        "LastSuccessfullyAppliedConfigurations": NotRequired[List[ConfigurationPaginatorTypeDef]],
        "LastSuccessfullyAppliedConfigurationsVersion": NotRequired[int],
        "EbsBlockDevices": NotRequired[List[EbsBlockDeviceTypeDef]],
        "EbsOptimized": NotRequired[bool],
        "ShrinkPolicy": NotRequired[ShrinkPolicyOutputTypeDef],
        "AutoScalingPolicy": NotRequired[AutoScalingPolicyDescriptionTypeDef],
        "CustomAmiId": NotRequired[str],
    },
)
InstanceGroupTypeDef = TypedDict(
    "InstanceGroupTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Market": NotRequired[MarketTypeType],
        "InstanceGroupType": NotRequired[InstanceGroupTypeType],
        "BidPrice": NotRequired[str],
        "InstanceType": NotRequired[str],
        "RequestedInstanceCount": NotRequired[int],
        "RunningInstanceCount": NotRequired[int],
        "Status": NotRequired[InstanceGroupStatusTypeDef],
        "Configurations": NotRequired[List[ConfigurationOutputTypeDef]],
        "ConfigurationsVersion": NotRequired[int],
        "LastSuccessfullyAppliedConfigurations": NotRequired[List[ConfigurationOutputTypeDef]],
        "LastSuccessfullyAppliedConfigurationsVersion": NotRequired[int],
        "EbsBlockDevices": NotRequired[List[EbsBlockDeviceTypeDef]],
        "EbsOptimized": NotRequired[bool],
        "ShrinkPolicy": NotRequired[ShrinkPolicyOutputTypeDef],
        "AutoScalingPolicy": NotRequired[AutoScalingPolicyDescriptionTypeDef],
        "CustomAmiId": NotRequired[str],
    },
)
PutAutoScalingPolicyOutputTypeDef = TypedDict(
    "PutAutoScalingPolicyOutputTypeDef",
    {
        "ClusterId": str,
        "InstanceGroupId": str,
        "AutoScalingPolicy": AutoScalingPolicyDescriptionTypeDef,
        "ClusterArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ScalingRuleTypeDef = TypedDict(
    "ScalingRuleTypeDef",
    {
        "Name": str,
        "Action": ScalingActionTypeDef,
        "Trigger": ScalingTriggerUnionTypeDef,
        "Description": NotRequired[str],
    },
)
AddInstanceFleetInputRequestTypeDef = TypedDict(
    "AddInstanceFleetInputRequestTypeDef",
    {
        "ClusterId": str,
        "InstanceFleet": InstanceFleetConfigTypeDef,
    },
)
ModifyInstanceFleetInputRequestTypeDef = TypedDict(
    "ModifyInstanceFleetInputRequestTypeDef",
    {
        "ClusterId": str,
        "InstanceFleet": InstanceFleetModifyConfigTypeDef,
    },
)
DescribeJobFlowsOutputTypeDef = TypedDict(
    "DescribeJobFlowsOutputTypeDef",
    {
        "JobFlows": List[JobFlowDetailTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AddJobFlowStepsInputRequestTypeDef = TypedDict(
    "AddJobFlowStepsInputRequestTypeDef",
    {
        "JobFlowId": str,
        "Steps": Sequence[StepConfigUnionTypeDef],
        "ExecutionRoleArn": NotRequired[str],
    },
)
ModifyInstanceGroupsInputRequestTypeDef = TypedDict(
    "ModifyInstanceGroupsInputRequestTypeDef",
    {
        "ClusterId": NotRequired[str],
        "InstanceGroups": NotRequired[Sequence[InstanceGroupModifyConfigTypeDef]],
    },
)
ListInstanceGroupsOutputPaginatorTypeDef = TypedDict(
    "ListInstanceGroupsOutputPaginatorTypeDef",
    {
        "InstanceGroups": List[InstanceGroupPaginatorTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListInstanceGroupsOutputTypeDef = TypedDict(
    "ListInstanceGroupsOutputTypeDef",
    {
        "InstanceGroups": List[InstanceGroupTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ScalingRuleUnionTypeDef = Union[ScalingRuleTypeDef, ScalingRuleOutputTypeDef]
AutoScalingPolicyTypeDef = TypedDict(
    "AutoScalingPolicyTypeDef",
    {
        "Constraints": ScalingConstraintsTypeDef,
        "Rules": Sequence[ScalingRuleUnionTypeDef],
    },
)
InstanceGroupConfigTypeDef = TypedDict(
    "InstanceGroupConfigTypeDef",
    {
        "InstanceRole": InstanceRoleTypeType,
        "InstanceType": str,
        "InstanceCount": int,
        "Name": NotRequired[str],
        "Market": NotRequired[MarketTypeType],
        "BidPrice": NotRequired[str],
        "Configurations": NotRequired[Sequence[ConfigurationUnionTypeDef]],
        "EbsConfiguration": NotRequired[EbsConfigurationTypeDef],
        "AutoScalingPolicy": NotRequired[AutoScalingPolicyTypeDef],
        "CustomAmiId": NotRequired[str],
    },
)
PutAutoScalingPolicyInputRequestTypeDef = TypedDict(
    "PutAutoScalingPolicyInputRequestTypeDef",
    {
        "ClusterId": str,
        "InstanceGroupId": str,
        "AutoScalingPolicy": AutoScalingPolicyTypeDef,
    },
)
AddInstanceGroupsInputRequestTypeDef = TypedDict(
    "AddInstanceGroupsInputRequestTypeDef",
    {
        "InstanceGroups": Sequence[InstanceGroupConfigTypeDef],
        "JobFlowId": str,
    },
)
JobFlowInstancesConfigTypeDef = TypedDict(
    "JobFlowInstancesConfigTypeDef",
    {
        "MasterInstanceType": NotRequired[str],
        "SlaveInstanceType": NotRequired[str],
        "InstanceCount": NotRequired[int],
        "InstanceGroups": NotRequired[Sequence[InstanceGroupConfigTypeDef]],
        "InstanceFleets": NotRequired[Sequence[InstanceFleetConfigTypeDef]],
        "Ec2KeyName": NotRequired[str],
        "Placement": NotRequired[PlacementTypeUnionTypeDef],
        "KeepJobFlowAliveWhenNoSteps": NotRequired[bool],
        "TerminationProtected": NotRequired[bool],
        "UnhealthyNodeReplacement": NotRequired[bool],
        "HadoopVersion": NotRequired[str],
        "Ec2SubnetId": NotRequired[str],
        "Ec2SubnetIds": NotRequired[Sequence[str]],
        "EmrManagedMasterSecurityGroup": NotRequired[str],
        "EmrManagedSlaveSecurityGroup": NotRequired[str],
        "ServiceAccessSecurityGroup": NotRequired[str],
        "AdditionalMasterSecurityGroups": NotRequired[Sequence[str]],
        "AdditionalSlaveSecurityGroups": NotRequired[Sequence[str]],
    },
)
RunJobFlowInputRequestTypeDef = TypedDict(
    "RunJobFlowInputRequestTypeDef",
    {
        "Name": str,
        "Instances": JobFlowInstancesConfigTypeDef,
        "LogUri": NotRequired[str],
        "LogEncryptionKmsKeyId": NotRequired[str],
        "AdditionalInfo": NotRequired[str],
        "AmiVersion": NotRequired[str],
        "ReleaseLabel": NotRequired[str],
        "Steps": NotRequired[Sequence[StepConfigTypeDef]],
        "BootstrapActions": NotRequired[Sequence[BootstrapActionConfigUnionTypeDef]],
        "SupportedProducts": NotRequired[Sequence[str]],
        "NewSupportedProducts": NotRequired[Sequence[SupportedProductConfigTypeDef]],
        "Applications": NotRequired[Sequence[ApplicationUnionTypeDef]],
        "Configurations": NotRequired[Sequence[ConfigurationUnionTypeDef]],
        "VisibleToAllUsers": NotRequired[bool],
        "JobFlowRole": NotRequired[str],
        "ServiceRole": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "SecurityConfiguration": NotRequired[str],
        "AutoScalingRole": NotRequired[str],
        "ScaleDownBehavior": NotRequired[ScaleDownBehaviorType],
        "CustomAmiId": NotRequired[str],
        "EbsRootVolumeSize": NotRequired[int],
        "RepoUpgradeOnBoot": NotRequired[RepoUpgradeOnBootType],
        "KerberosAttributes": NotRequired[KerberosAttributesTypeDef],
        "StepConcurrencyLevel": NotRequired[int],
        "ManagedScalingPolicy": NotRequired[ManagedScalingPolicyTypeDef],
        "PlacementGroupConfigs": NotRequired[Sequence[PlacementGroupConfigTypeDef]],
        "AutoTerminationPolicy": NotRequired[AutoTerminationPolicyTypeDef],
        "OSReleaseLabel": NotRequired[str],
        "EbsRootVolumeIops": NotRequired[int],
        "EbsRootVolumeThroughput": NotRequired[int],
    },
)
