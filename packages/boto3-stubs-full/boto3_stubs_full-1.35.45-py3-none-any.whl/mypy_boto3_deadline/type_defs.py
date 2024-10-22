"""
Type annotations for deadline service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_deadline/type_defs/)

Usage::

    ```python
    from mypy_boto3_deadline.type_defs import AcceleratorCountRangeTypeDef

    data: AcceleratorCountRangeTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    AutoScalingModeType,
    AutoScalingStatusType,
    BudgetActionTypeType,
    BudgetStatusType,
    ComparisonOperatorType,
    CompletedStatusType,
    CpuArchitectureTypeType,
    CreateJobTargetTaskRunStatusType,
    CustomerManagedFleetOperatingSystemFamilyType,
    DefaultQueueBudgetActionType,
    DependencyConsumerResolutionStatusType,
    Ec2MarketTypeType,
    EnvironmentTemplateTypeType,
    FileSystemLocationTypeType,
    FleetStatusType,
    JobAttachmentsFileSystemType,
    JobEntityErrorCodeType,
    JobLifecycleStatusType,
    JobTargetTaskRunStatusType,
    JobTemplateTypeType,
    LicenseEndpointStatusType,
    LogicalOperatorType,
    MembershipLevelType,
    PathFormatType,
    PeriodType,
    PrincipalTypeType,
    QueueBlockedReasonType,
    QueueFleetAssociationStatusType,
    QueueStatusType,
    RunAsType,
    ServiceManagedFleetOperatingSystemFamilyType,
    SessionActionStatusType,
    SessionLifecycleStatusType,
    SessionsStatisticsAggregationStatusType,
    SortOrderType,
    StepLifecycleStatusType,
    StepParameterTypeType,
    StepTargetTaskRunStatusType,
    StorageProfileOperatingSystemFamilyType,
    TaskRunStatusType,
    TaskTargetRunStatusType,
    UpdatedWorkerStatusType,
    UpdateQueueFleetAssociationStatusType,
    UsageGroupByFieldType,
    UsageStatisticType,
    UsageTypeType,
    WorkerStatusType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AcceleratorCountRangeTypeDef",
    "AcceleratorTotalMemoryMiBRangeTypeDef",
    "AssignedEnvironmentEnterSessionActionDefinitionTypeDef",
    "AssignedEnvironmentExitSessionActionDefinitionTypeDef",
    "AssignedSyncInputJobAttachmentsSessionActionDefinitionTypeDef",
    "LogConfigurationTypeDef",
    "TaskParameterValueTypeDef",
    "AssociateMemberToFarmRequestRequestTypeDef",
    "AssociateMemberToFleetRequestRequestTypeDef",
    "AssociateMemberToJobRequestRequestTypeDef",
    "AssociateMemberToQueueRequestRequestTypeDef",
    "AssumeFleetRoleForReadRequestRequestTypeDef",
    "AwsCredentialsTypeDef",
    "ResponseMetadataTypeDef",
    "AssumeFleetRoleForWorkerRequestRequestTypeDef",
    "AssumeQueueRoleForReadRequestRequestTypeDef",
    "AssumeQueueRoleForUserRequestRequestTypeDef",
    "AssumeQueueRoleForWorkerRequestRequestTypeDef",
    "ManifestPropertiesOutputTypeDef",
    "BudgetActionToAddTypeDef",
    "BudgetActionToRemoveTypeDef",
    "FixedBudgetScheduleOutputTypeDef",
    "ConsumedUsagesTypeDef",
    "UsageTrackingResourceTypeDef",
    "S3LocationTypeDef",
    "CreateFarmRequestRequestTypeDef",
    "JobParameterTypeDef",
    "CreateLicenseEndpointRequestRequestTypeDef",
    "CreateMonitorRequestRequestTypeDef",
    "CreateQueueEnvironmentRequestRequestTypeDef",
    "CreateQueueFleetAssociationRequestRequestTypeDef",
    "JobAttachmentSettingsTypeDef",
    "FileSystemLocationTypeDef",
    "FleetAmountCapabilityTypeDef",
    "FleetAttributeCapabilityOutputTypeDef",
    "MemoryMiBRangeTypeDef",
    "VCpuCountRangeTypeDef",
    "TimestampTypeDef",
    "DeleteBudgetRequestRequestTypeDef",
    "DeleteFarmRequestRequestTypeDef",
    "DeleteFleetRequestRequestTypeDef",
    "DeleteLicenseEndpointRequestRequestTypeDef",
    "DeleteMeteredProductRequestRequestTypeDef",
    "DeleteMonitorRequestRequestTypeDef",
    "DeleteQueueEnvironmentRequestRequestTypeDef",
    "DeleteQueueFleetAssociationRequestRequestTypeDef",
    "DeleteQueueRequestRequestTypeDef",
    "DeleteStorageProfileRequestRequestTypeDef",
    "DeleteWorkerRequestRequestTypeDef",
    "DependencyCountsTypeDef",
    "DisassociateMemberFromFarmRequestRequestTypeDef",
    "DisassociateMemberFromFleetRequestRequestTypeDef",
    "DisassociateMemberFromJobRequestRequestTypeDef",
    "DisassociateMemberFromQueueRequestRequestTypeDef",
    "Ec2EbsVolumeTypeDef",
    "EnvironmentDetailsEntityTypeDef",
    "EnvironmentDetailsErrorTypeDef",
    "EnvironmentDetailsIdentifiersTypeDef",
    "EnvironmentEnterSessionActionDefinitionSummaryTypeDef",
    "EnvironmentEnterSessionActionDefinitionTypeDef",
    "EnvironmentExitSessionActionDefinitionSummaryTypeDef",
    "EnvironmentExitSessionActionDefinitionTypeDef",
    "FarmMemberTypeDef",
    "FarmSummaryTypeDef",
    "FieldSortExpressionTypeDef",
    "FleetAttributeCapabilityTypeDef",
    "FleetMemberTypeDef",
    "GetBudgetRequestRequestTypeDef",
    "ResponseBudgetActionTypeDef",
    "GetFarmRequestRequestTypeDef",
    "WaiterConfigTypeDef",
    "GetFleetRequestRequestTypeDef",
    "JobAttachmentDetailsErrorTypeDef",
    "JobDetailsErrorTypeDef",
    "StepDetailsErrorTypeDef",
    "GetJobRequestRequestTypeDef",
    "GetLicenseEndpointRequestRequestTypeDef",
    "GetMonitorRequestRequestTypeDef",
    "GetQueueEnvironmentRequestRequestTypeDef",
    "GetQueueFleetAssociationRequestRequestTypeDef",
    "GetQueueRequestRequestTypeDef",
    "GetSessionActionRequestRequestTypeDef",
    "GetSessionRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "GetSessionsStatisticsAggregationRequestRequestTypeDef",
    "GetStepRequestRequestTypeDef",
    "GetStorageProfileForQueueRequestRequestTypeDef",
    "GetStorageProfileRequestRequestTypeDef",
    "GetTaskRequestRequestTypeDef",
    "GetWorkerRequestRequestTypeDef",
    "IpAddressesOutputTypeDef",
    "IpAddressesTypeDef",
    "JobAttachmentDetailsIdentifiersTypeDef",
    "PathMappingRuleTypeDef",
    "JobDetailsIdentifiersTypeDef",
    "StepDetailsIdentifiersTypeDef",
    "StepDetailsEntityTypeDef",
    "JobMemberTypeDef",
    "PosixUserTypeDef",
    "WindowsUserTypeDef",
    "JobSummaryTypeDef",
    "LicenseEndpointSummaryTypeDef",
    "ListAvailableMeteredProductsRequestRequestTypeDef",
    "MeteredProductSummaryTypeDef",
    "ListBudgetsRequestRequestTypeDef",
    "ListFarmMembersRequestRequestTypeDef",
    "ListFarmsRequestRequestTypeDef",
    "ListFleetMembersRequestRequestTypeDef",
    "ListFleetsRequestRequestTypeDef",
    "ListJobMembersRequestRequestTypeDef",
    "ListJobParameterDefinitionsRequestRequestTypeDef",
    "ListJobsRequestRequestTypeDef",
    "ListLicenseEndpointsRequestRequestTypeDef",
    "ListMeteredProductsRequestRequestTypeDef",
    "ListMonitorsRequestRequestTypeDef",
    "MonitorSummaryTypeDef",
    "ListQueueEnvironmentsRequestRequestTypeDef",
    "QueueEnvironmentSummaryTypeDef",
    "ListQueueFleetAssociationsRequestRequestTypeDef",
    "QueueFleetAssociationSummaryTypeDef",
    "ListQueueMembersRequestRequestTypeDef",
    "QueueMemberTypeDef",
    "ListQueuesRequestRequestTypeDef",
    "QueueSummaryTypeDef",
    "ListSessionActionsRequestRequestTypeDef",
    "ListSessionsForWorkerRequestRequestTypeDef",
    "WorkerSessionSummaryTypeDef",
    "ListSessionsRequestRequestTypeDef",
    "SessionSummaryTypeDef",
    "ListStepConsumersRequestRequestTypeDef",
    "StepConsumerTypeDef",
    "ListStepDependenciesRequestRequestTypeDef",
    "StepDependencyTypeDef",
    "ListStepsRequestRequestTypeDef",
    "ListStorageProfilesForQueueRequestRequestTypeDef",
    "StorageProfileSummaryTypeDef",
    "ListStorageProfilesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTasksRequestRequestTypeDef",
    "ListWorkersRequestRequestTypeDef",
    "ManifestPropertiesTypeDef",
    "ParameterFilterExpressionTypeDef",
    "ParameterSortExpressionTypeDef",
    "StepParameterTypeDef",
    "PutMeteredProductRequestRequestTypeDef",
    "SearchTermFilterExpressionTypeDef",
    "StringFilterExpressionTypeDef",
    "UserJobsFirstTypeDef",
    "ServiceManagedEc2InstanceMarketOptionsTypeDef",
    "SyncInputJobAttachmentsSessionActionDefinitionSummaryTypeDef",
    "TaskRunSessionActionDefinitionSummaryTypeDef",
    "SyncInputJobAttachmentsSessionActionDefinitionTypeDef",
    "SessionsStatisticsResourcesTypeDef",
    "StatsTypeDef",
    "StepAmountCapabilityTypeDef",
    "StepAttributeCapabilityTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateFarmRequestRequestTypeDef",
    "UpdateJobRequestRequestTypeDef",
    "UpdateMonitorRequestRequestTypeDef",
    "UpdateQueueEnvironmentRequestRequestTypeDef",
    "UpdateQueueFleetAssociationRequestRequestTypeDef",
    "UpdateSessionRequestRequestTypeDef",
    "UpdateStepRequestRequestTypeDef",
    "UpdateTaskRequestRequestTypeDef",
    "WorkerAmountCapabilityTypeDef",
    "WorkerAttributeCapabilityTypeDef",
    "AssignedTaskRunSessionActionDefinitionTypeDef",
    "TaskRunSessionActionDefinitionTypeDef",
    "TaskSearchSummaryTypeDef",
    "TaskSummaryTypeDef",
    "AssumeFleetRoleForReadResponseTypeDef",
    "AssumeFleetRoleForWorkerResponseTypeDef",
    "AssumeQueueRoleForReadResponseTypeDef",
    "AssumeQueueRoleForUserResponseTypeDef",
    "AssumeQueueRoleForWorkerResponseTypeDef",
    "CopyJobTemplateResponseTypeDef",
    "CreateBudgetResponseTypeDef",
    "CreateFarmResponseTypeDef",
    "CreateFleetResponseTypeDef",
    "CreateJobResponseTypeDef",
    "CreateLicenseEndpointResponseTypeDef",
    "CreateMonitorResponseTypeDef",
    "CreateQueueEnvironmentResponseTypeDef",
    "CreateQueueResponseTypeDef",
    "CreateStorageProfileResponseTypeDef",
    "CreateWorkerResponseTypeDef",
    "GetFarmResponseTypeDef",
    "GetLicenseEndpointResponseTypeDef",
    "GetMonitorResponseTypeDef",
    "GetQueueEnvironmentResponseTypeDef",
    "GetQueueFleetAssociationResponseTypeDef",
    "GetTaskResponseTypeDef",
    "ListJobParameterDefinitionsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartSessionsStatisticsAggregationResponseTypeDef",
    "UpdateWorkerResponseTypeDef",
    "AttachmentsOutputTypeDef",
    "BudgetScheduleOutputTypeDef",
    "BudgetSummaryTypeDef",
    "CopyJobTemplateRequestRequestTypeDef",
    "JobSearchSummaryTypeDef",
    "CreateStorageProfileRequestRequestTypeDef",
    "GetStorageProfileForQueueResponseTypeDef",
    "GetStorageProfileResponseTypeDef",
    "UpdateStorageProfileRequestRequestTypeDef",
    "FleetCapabilitiesTypeDef",
    "CustomerManagedWorkerCapabilitiesOutputTypeDef",
    "DateTimeFilterExpressionTypeDef",
    "FixedBudgetScheduleTypeDef",
    "UpdatedSessionActionInfoTypeDef",
    "StepSummaryTypeDef",
    "ServiceManagedEc2InstanceCapabilitiesOutputTypeDef",
    "ListFarmMembersResponseTypeDef",
    "ListFarmsResponseTypeDef",
    "FleetAttributeCapabilityUnionTypeDef",
    "ServiceManagedEc2InstanceCapabilitiesTypeDef",
    "ListFleetMembersResponseTypeDef",
    "GetFleetRequestFleetActiveWaitTypeDef",
    "GetJobRequestJobCreateCompleteWaitTypeDef",
    "GetLicenseEndpointRequestLicenseEndpointDeletedWaitTypeDef",
    "GetLicenseEndpointRequestLicenseEndpointValidWaitTypeDef",
    "GetQueueFleetAssociationRequestQueueFleetAssociationStoppedWaitTypeDef",
    "GetQueueRequestQueueSchedulingBlockedWaitTypeDef",
    "GetQueueRequestQueueSchedulingWaitTypeDef",
    "GetJobEntityErrorTypeDef",
    "GetSessionsStatisticsAggregationRequestGetSessionsStatisticsAggregationPaginateTypeDef",
    "ListAvailableMeteredProductsRequestListAvailableMeteredProductsPaginateTypeDef",
    "ListBudgetsRequestListBudgetsPaginateTypeDef",
    "ListFarmMembersRequestListFarmMembersPaginateTypeDef",
    "ListFarmsRequestListFarmsPaginateTypeDef",
    "ListFleetMembersRequestListFleetMembersPaginateTypeDef",
    "ListFleetsRequestListFleetsPaginateTypeDef",
    "ListJobMembersRequestListJobMembersPaginateTypeDef",
    "ListJobParameterDefinitionsRequestListJobParameterDefinitionsPaginateTypeDef",
    "ListJobsRequestListJobsPaginateTypeDef",
    "ListLicenseEndpointsRequestListLicenseEndpointsPaginateTypeDef",
    "ListMeteredProductsRequestListMeteredProductsPaginateTypeDef",
    "ListMonitorsRequestListMonitorsPaginateTypeDef",
    "ListQueueEnvironmentsRequestListQueueEnvironmentsPaginateTypeDef",
    "ListQueueFleetAssociationsRequestListQueueFleetAssociationsPaginateTypeDef",
    "ListQueueMembersRequestListQueueMembersPaginateTypeDef",
    "ListQueuesRequestListQueuesPaginateTypeDef",
    "ListSessionActionsRequestListSessionActionsPaginateTypeDef",
    "ListSessionsForWorkerRequestListSessionsForWorkerPaginateTypeDef",
    "ListSessionsRequestListSessionsPaginateTypeDef",
    "ListStepConsumersRequestListStepConsumersPaginateTypeDef",
    "ListStepDependenciesRequestListStepDependenciesPaginateTypeDef",
    "ListStepsRequestListStepsPaginateTypeDef",
    "ListStorageProfilesForQueueRequestListStorageProfilesForQueuePaginateTypeDef",
    "ListStorageProfilesRequestListStorageProfilesPaginateTypeDef",
    "ListTasksRequestListTasksPaginateTypeDef",
    "ListWorkersRequestListWorkersPaginateTypeDef",
    "HostPropertiesResponseTypeDef",
    "IpAddressesUnionTypeDef",
    "JobEntityIdentifiersUnionTypeDef",
    "ListJobMembersResponseTypeDef",
    "JobRunAsUserTypeDef",
    "ListJobsResponseTypeDef",
    "ListLicenseEndpointsResponseTypeDef",
    "ListAvailableMeteredProductsResponseTypeDef",
    "ListMeteredProductsResponseTypeDef",
    "ListMonitorsResponseTypeDef",
    "ListQueueEnvironmentsResponseTypeDef",
    "ListQueueFleetAssociationsResponseTypeDef",
    "ListQueueMembersResponseTypeDef",
    "ListQueuesResponseTypeDef",
    "ListSessionsForWorkerResponseTypeDef",
    "ListSessionsResponseTypeDef",
    "ListStepConsumersResponseTypeDef",
    "ListStepDependenciesResponseTypeDef",
    "ListStorageProfilesForQueueResponseTypeDef",
    "ListStorageProfilesResponseTypeDef",
    "ManifestPropertiesUnionTypeDef",
    "ParameterSpaceTypeDef",
    "SearchSortExpressionTypeDef",
    "SessionActionDefinitionSummaryTypeDef",
    "StartSessionsStatisticsAggregationRequestRequestTypeDef",
    "StatisticsTypeDef",
    "StepRequiredCapabilitiesTypeDef",
    "WorkerCapabilitiesTypeDef",
    "AssignedSessionActionDefinitionTypeDef",
    "SessionActionDefinitionTypeDef",
    "SearchTasksResponseTypeDef",
    "ListTasksResponseTypeDef",
    "GetJobResponseTypeDef",
    "JobAttachmentDetailsEntityTypeDef",
    "GetBudgetResponseTypeDef",
    "ListBudgetsResponseTypeDef",
    "SearchJobsResponseTypeDef",
    "CustomerManagedFleetConfigurationOutputTypeDef",
    "SearchFilterExpressionTypeDef",
    "FixedBudgetScheduleUnionTypeDef",
    "UpdateWorkerScheduleRequestRequestTypeDef",
    "ListStepsResponseTypeDef",
    "ServiceManagedEc2FleetConfigurationOutputTypeDef",
    "CustomerManagedWorkerCapabilitiesTypeDef",
    "ServiceManagedEc2InstanceCapabilitiesUnionTypeDef",
    "GetSessionResponseTypeDef",
    "GetWorkerResponseTypeDef",
    "WorkerSearchSummaryTypeDef",
    "WorkerSummaryTypeDef",
    "HostPropertiesRequestTypeDef",
    "BatchGetJobEntityRequestRequestTypeDef",
    "CreateQueueRequestRequestTypeDef",
    "GetQueueResponseTypeDef",
    "JobDetailsEntityTypeDef",
    "UpdateQueueRequestRequestTypeDef",
    "AttachmentsTypeDef",
    "StepSearchSummaryTypeDef",
    "SessionActionSummaryTypeDef",
    "GetSessionsStatisticsAggregationResponseTypeDef",
    "GetStepResponseTypeDef",
    "AssignedSessionActionTypeDef",
    "GetSessionActionResponseTypeDef",
    "SearchGroupedFilterExpressionsTypeDef",
    "BudgetScheduleTypeDef",
    "FleetConfigurationOutputTypeDef",
    "CustomerManagedWorkerCapabilitiesUnionTypeDef",
    "ServiceManagedEc2FleetConfigurationTypeDef",
    "SearchWorkersResponseTypeDef",
    "ListWorkersResponseTypeDef",
    "CreateWorkerRequestRequestTypeDef",
    "UpdateWorkerRequestRequestTypeDef",
    "JobEntityTypeDef",
    "CreateJobRequestRequestTypeDef",
    "SearchStepsResponseTypeDef",
    "ListSessionActionsResponseTypeDef",
    "AssignedSessionTypeDef",
    "SearchJobsRequestRequestTypeDef",
    "SearchStepsRequestRequestTypeDef",
    "SearchTasksRequestRequestTypeDef",
    "SearchWorkersRequestRequestTypeDef",
    "CreateBudgetRequestRequestTypeDef",
    "UpdateBudgetRequestRequestTypeDef",
    "FleetSummaryTypeDef",
    "GetFleetResponseTypeDef",
    "CustomerManagedFleetConfigurationTypeDef",
    "ServiceManagedEc2FleetConfigurationUnionTypeDef",
    "BatchGetJobEntityResponseTypeDef",
    "UpdateWorkerScheduleResponseTypeDef",
    "ListFleetsResponseTypeDef",
    "CustomerManagedFleetConfigurationUnionTypeDef",
    "FleetConfigurationTypeDef",
    "CreateFleetRequestRequestTypeDef",
    "UpdateFleetRequestRequestTypeDef",
)

AcceleratorCountRangeTypeDef = TypedDict(
    "AcceleratorCountRangeTypeDef",
    {
        "min": int,
        "max": NotRequired[int],
    },
)
AcceleratorTotalMemoryMiBRangeTypeDef = TypedDict(
    "AcceleratorTotalMemoryMiBRangeTypeDef",
    {
        "min": int,
        "max": NotRequired[int],
    },
)
AssignedEnvironmentEnterSessionActionDefinitionTypeDef = TypedDict(
    "AssignedEnvironmentEnterSessionActionDefinitionTypeDef",
    {
        "environmentId": str,
    },
)
AssignedEnvironmentExitSessionActionDefinitionTypeDef = TypedDict(
    "AssignedEnvironmentExitSessionActionDefinitionTypeDef",
    {
        "environmentId": str,
    },
)
AssignedSyncInputJobAttachmentsSessionActionDefinitionTypeDef = TypedDict(
    "AssignedSyncInputJobAttachmentsSessionActionDefinitionTypeDef",
    {
        "stepId": NotRequired[str],
    },
)
LogConfigurationTypeDef = TypedDict(
    "LogConfigurationTypeDef",
    {
        "logDriver": str,
        "options": NotRequired[Dict[str, str]],
        "parameters": NotRequired[Dict[str, str]],
        "error": NotRequired[str],
    },
)
TaskParameterValueTypeDef = TypedDict(
    "TaskParameterValueTypeDef",
    {
        "int": NotRequired[str],
        "float": NotRequired[str],
        "string": NotRequired[str],
        "path": NotRequired[str],
    },
)
AssociateMemberToFarmRequestRequestTypeDef = TypedDict(
    "AssociateMemberToFarmRequestRequestTypeDef",
    {
        "farmId": str,
        "principalId": str,
        "principalType": PrincipalTypeType,
        "identityStoreId": str,
        "membershipLevel": MembershipLevelType,
    },
)
AssociateMemberToFleetRequestRequestTypeDef = TypedDict(
    "AssociateMemberToFleetRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "principalId": str,
        "principalType": PrincipalTypeType,
        "identityStoreId": str,
        "membershipLevel": MembershipLevelType,
    },
)
AssociateMemberToJobRequestRequestTypeDef = TypedDict(
    "AssociateMemberToJobRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "jobId": str,
        "principalId": str,
        "principalType": PrincipalTypeType,
        "identityStoreId": str,
        "membershipLevel": MembershipLevelType,
    },
)
AssociateMemberToQueueRequestRequestTypeDef = TypedDict(
    "AssociateMemberToQueueRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "principalId": str,
        "principalType": PrincipalTypeType,
        "identityStoreId": str,
        "membershipLevel": MembershipLevelType,
    },
)
AssumeFleetRoleForReadRequestRequestTypeDef = TypedDict(
    "AssumeFleetRoleForReadRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
    },
)
AwsCredentialsTypeDef = TypedDict(
    "AwsCredentialsTypeDef",
    {
        "accessKeyId": str,
        "secretAccessKey": str,
        "sessionToken": str,
        "expiration": datetime,
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
AssumeFleetRoleForWorkerRequestRequestTypeDef = TypedDict(
    "AssumeFleetRoleForWorkerRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "workerId": str,
    },
)
AssumeQueueRoleForReadRequestRequestTypeDef = TypedDict(
    "AssumeQueueRoleForReadRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
    },
)
AssumeQueueRoleForUserRequestRequestTypeDef = TypedDict(
    "AssumeQueueRoleForUserRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
    },
)
AssumeQueueRoleForWorkerRequestRequestTypeDef = TypedDict(
    "AssumeQueueRoleForWorkerRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "workerId": str,
        "queueId": str,
    },
)
ManifestPropertiesOutputTypeDef = TypedDict(
    "ManifestPropertiesOutputTypeDef",
    {
        "rootPath": str,
        "rootPathFormat": PathFormatType,
        "fileSystemLocationName": NotRequired[str],
        "outputRelativeDirectories": NotRequired[List[str]],
        "inputManifestPath": NotRequired[str],
        "inputManifestHash": NotRequired[str],
    },
)
BudgetActionToAddTypeDef = TypedDict(
    "BudgetActionToAddTypeDef",
    {
        "type": BudgetActionTypeType,
        "thresholdPercentage": float,
        "description": NotRequired[str],
    },
)
BudgetActionToRemoveTypeDef = TypedDict(
    "BudgetActionToRemoveTypeDef",
    {
        "type": BudgetActionTypeType,
        "thresholdPercentage": float,
    },
)
FixedBudgetScheduleOutputTypeDef = TypedDict(
    "FixedBudgetScheduleOutputTypeDef",
    {
        "startTime": datetime,
        "endTime": datetime,
    },
)
ConsumedUsagesTypeDef = TypedDict(
    "ConsumedUsagesTypeDef",
    {
        "approximateDollarUsage": float,
    },
)
UsageTrackingResourceTypeDef = TypedDict(
    "UsageTrackingResourceTypeDef",
    {
        "queueId": NotRequired[str],
    },
)
S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucketName": str,
        "key": str,
    },
)
CreateFarmRequestRequestTypeDef = TypedDict(
    "CreateFarmRequestRequestTypeDef",
    {
        "displayName": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "kmsKeyArn": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
JobParameterTypeDef = TypedDict(
    "JobParameterTypeDef",
    {
        "int": NotRequired[str],
        "float": NotRequired[str],
        "string": NotRequired[str],
        "path": NotRequired[str],
    },
)
CreateLicenseEndpointRequestRequestTypeDef = TypedDict(
    "CreateLicenseEndpointRequestRequestTypeDef",
    {
        "vpcId": str,
        "subnetIds": Sequence[str],
        "securityGroupIds": Sequence[str],
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateMonitorRequestRequestTypeDef = TypedDict(
    "CreateMonitorRequestRequestTypeDef",
    {
        "displayName": str,
        "identityCenterInstanceArn": str,
        "subdomain": str,
        "roleArn": str,
        "clientToken": NotRequired[str],
    },
)
CreateQueueEnvironmentRequestRequestTypeDef = TypedDict(
    "CreateQueueEnvironmentRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "priority": int,
        "templateType": EnvironmentTemplateTypeType,
        "template": str,
        "clientToken": NotRequired[str],
    },
)
CreateQueueFleetAssociationRequestRequestTypeDef = TypedDict(
    "CreateQueueFleetAssociationRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "fleetId": str,
    },
)
JobAttachmentSettingsTypeDef = TypedDict(
    "JobAttachmentSettingsTypeDef",
    {
        "s3BucketName": str,
        "rootPrefix": str,
    },
)
FileSystemLocationTypeDef = TypedDict(
    "FileSystemLocationTypeDef",
    {
        "name": str,
        "path": str,
        "type": FileSystemLocationTypeType,
    },
)
FleetAmountCapabilityTypeDef = TypedDict(
    "FleetAmountCapabilityTypeDef",
    {
        "name": str,
        "min": float,
        "max": NotRequired[float],
    },
)
FleetAttributeCapabilityOutputTypeDef = TypedDict(
    "FleetAttributeCapabilityOutputTypeDef",
    {
        "name": str,
        "values": List[str],
    },
)
MemoryMiBRangeTypeDef = TypedDict(
    "MemoryMiBRangeTypeDef",
    {
        "min": int,
        "max": NotRequired[int],
    },
)
VCpuCountRangeTypeDef = TypedDict(
    "VCpuCountRangeTypeDef",
    {
        "min": int,
        "max": NotRequired[int],
    },
)
TimestampTypeDef = Union[datetime, str]
DeleteBudgetRequestRequestTypeDef = TypedDict(
    "DeleteBudgetRequestRequestTypeDef",
    {
        "farmId": str,
        "budgetId": str,
    },
)
DeleteFarmRequestRequestTypeDef = TypedDict(
    "DeleteFarmRequestRequestTypeDef",
    {
        "farmId": str,
    },
)
DeleteFleetRequestRequestTypeDef = TypedDict(
    "DeleteFleetRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "clientToken": NotRequired[str],
    },
)
DeleteLicenseEndpointRequestRequestTypeDef = TypedDict(
    "DeleteLicenseEndpointRequestRequestTypeDef",
    {
        "licenseEndpointId": str,
    },
)
DeleteMeteredProductRequestRequestTypeDef = TypedDict(
    "DeleteMeteredProductRequestRequestTypeDef",
    {
        "licenseEndpointId": str,
        "productId": str,
    },
)
DeleteMonitorRequestRequestTypeDef = TypedDict(
    "DeleteMonitorRequestRequestTypeDef",
    {
        "monitorId": str,
    },
)
DeleteQueueEnvironmentRequestRequestTypeDef = TypedDict(
    "DeleteQueueEnvironmentRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "queueEnvironmentId": str,
    },
)
DeleteQueueFleetAssociationRequestRequestTypeDef = TypedDict(
    "DeleteQueueFleetAssociationRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "fleetId": str,
    },
)
DeleteQueueRequestRequestTypeDef = TypedDict(
    "DeleteQueueRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
    },
)
DeleteStorageProfileRequestRequestTypeDef = TypedDict(
    "DeleteStorageProfileRequestRequestTypeDef",
    {
        "farmId": str,
        "storageProfileId": str,
    },
)
DeleteWorkerRequestRequestTypeDef = TypedDict(
    "DeleteWorkerRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "workerId": str,
    },
)
DependencyCountsTypeDef = TypedDict(
    "DependencyCountsTypeDef",
    {
        "dependenciesResolved": int,
        "dependenciesUnresolved": int,
        "consumersResolved": int,
        "consumersUnresolved": int,
    },
)
DisassociateMemberFromFarmRequestRequestTypeDef = TypedDict(
    "DisassociateMemberFromFarmRequestRequestTypeDef",
    {
        "farmId": str,
        "principalId": str,
    },
)
DisassociateMemberFromFleetRequestRequestTypeDef = TypedDict(
    "DisassociateMemberFromFleetRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "principalId": str,
    },
)
DisassociateMemberFromJobRequestRequestTypeDef = TypedDict(
    "DisassociateMemberFromJobRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "jobId": str,
        "principalId": str,
    },
)
DisassociateMemberFromQueueRequestRequestTypeDef = TypedDict(
    "DisassociateMemberFromQueueRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "principalId": str,
    },
)
Ec2EbsVolumeTypeDef = TypedDict(
    "Ec2EbsVolumeTypeDef",
    {
        "sizeGiB": NotRequired[int],
        "iops": NotRequired[int],
        "throughputMiB": NotRequired[int],
    },
)
EnvironmentDetailsEntityTypeDef = TypedDict(
    "EnvironmentDetailsEntityTypeDef",
    {
        "jobId": str,
        "environmentId": str,
        "schemaVersion": str,
        "template": Dict[str, Any],
    },
)
EnvironmentDetailsErrorTypeDef = TypedDict(
    "EnvironmentDetailsErrorTypeDef",
    {
        "jobId": str,
        "environmentId": str,
        "code": JobEntityErrorCodeType,
        "message": str,
    },
)
EnvironmentDetailsIdentifiersTypeDef = TypedDict(
    "EnvironmentDetailsIdentifiersTypeDef",
    {
        "jobId": str,
        "environmentId": str,
    },
)
EnvironmentEnterSessionActionDefinitionSummaryTypeDef = TypedDict(
    "EnvironmentEnterSessionActionDefinitionSummaryTypeDef",
    {
        "environmentId": str,
    },
)
EnvironmentEnterSessionActionDefinitionTypeDef = TypedDict(
    "EnvironmentEnterSessionActionDefinitionTypeDef",
    {
        "environmentId": str,
    },
)
EnvironmentExitSessionActionDefinitionSummaryTypeDef = TypedDict(
    "EnvironmentExitSessionActionDefinitionSummaryTypeDef",
    {
        "environmentId": str,
    },
)
EnvironmentExitSessionActionDefinitionTypeDef = TypedDict(
    "EnvironmentExitSessionActionDefinitionTypeDef",
    {
        "environmentId": str,
    },
)
FarmMemberTypeDef = TypedDict(
    "FarmMemberTypeDef",
    {
        "farmId": str,
        "principalId": str,
        "principalType": PrincipalTypeType,
        "identityStoreId": str,
        "membershipLevel": MembershipLevelType,
    },
)
FarmSummaryTypeDef = TypedDict(
    "FarmSummaryTypeDef",
    {
        "farmId": str,
        "displayName": str,
        "createdAt": datetime,
        "createdBy": str,
        "kmsKeyArn": NotRequired[str],
        "updatedAt": NotRequired[datetime],
        "updatedBy": NotRequired[str],
    },
)
FieldSortExpressionTypeDef = TypedDict(
    "FieldSortExpressionTypeDef",
    {
        "sortOrder": SortOrderType,
        "name": str,
    },
)
FleetAttributeCapabilityTypeDef = TypedDict(
    "FleetAttributeCapabilityTypeDef",
    {
        "name": str,
        "values": Sequence[str],
    },
)
FleetMemberTypeDef = TypedDict(
    "FleetMemberTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "principalId": str,
        "principalType": PrincipalTypeType,
        "identityStoreId": str,
        "membershipLevel": MembershipLevelType,
    },
)
GetBudgetRequestRequestTypeDef = TypedDict(
    "GetBudgetRequestRequestTypeDef",
    {
        "farmId": str,
        "budgetId": str,
    },
)
ResponseBudgetActionTypeDef = TypedDict(
    "ResponseBudgetActionTypeDef",
    {
        "type": BudgetActionTypeType,
        "thresholdPercentage": float,
        "description": NotRequired[str],
    },
)
GetFarmRequestRequestTypeDef = TypedDict(
    "GetFarmRequestRequestTypeDef",
    {
        "farmId": str,
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
GetFleetRequestRequestTypeDef = TypedDict(
    "GetFleetRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
    },
)
JobAttachmentDetailsErrorTypeDef = TypedDict(
    "JobAttachmentDetailsErrorTypeDef",
    {
        "jobId": str,
        "code": JobEntityErrorCodeType,
        "message": str,
    },
)
JobDetailsErrorTypeDef = TypedDict(
    "JobDetailsErrorTypeDef",
    {
        "jobId": str,
        "code": JobEntityErrorCodeType,
        "message": str,
    },
)
StepDetailsErrorTypeDef = TypedDict(
    "StepDetailsErrorTypeDef",
    {
        "jobId": str,
        "stepId": str,
        "code": JobEntityErrorCodeType,
        "message": str,
    },
)
GetJobRequestRequestTypeDef = TypedDict(
    "GetJobRequestRequestTypeDef",
    {
        "farmId": str,
        "jobId": str,
        "queueId": str,
    },
)
GetLicenseEndpointRequestRequestTypeDef = TypedDict(
    "GetLicenseEndpointRequestRequestTypeDef",
    {
        "licenseEndpointId": str,
    },
)
GetMonitorRequestRequestTypeDef = TypedDict(
    "GetMonitorRequestRequestTypeDef",
    {
        "monitorId": str,
    },
)
GetQueueEnvironmentRequestRequestTypeDef = TypedDict(
    "GetQueueEnvironmentRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "queueEnvironmentId": str,
    },
)
GetQueueFleetAssociationRequestRequestTypeDef = TypedDict(
    "GetQueueFleetAssociationRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "fleetId": str,
    },
)
GetQueueRequestRequestTypeDef = TypedDict(
    "GetQueueRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
    },
)
GetSessionActionRequestRequestTypeDef = TypedDict(
    "GetSessionActionRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "jobId": str,
        "sessionActionId": str,
    },
)
GetSessionRequestRequestTypeDef = TypedDict(
    "GetSessionRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "jobId": str,
        "sessionId": str,
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
GetSessionsStatisticsAggregationRequestRequestTypeDef = TypedDict(
    "GetSessionsStatisticsAggregationRequestRequestTypeDef",
    {
        "farmId": str,
        "aggregationId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
GetStepRequestRequestTypeDef = TypedDict(
    "GetStepRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "jobId": str,
        "stepId": str,
    },
)
GetStorageProfileForQueueRequestRequestTypeDef = TypedDict(
    "GetStorageProfileForQueueRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "storageProfileId": str,
    },
)
GetStorageProfileRequestRequestTypeDef = TypedDict(
    "GetStorageProfileRequestRequestTypeDef",
    {
        "farmId": str,
        "storageProfileId": str,
    },
)
GetTaskRequestRequestTypeDef = TypedDict(
    "GetTaskRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "jobId": str,
        "stepId": str,
        "taskId": str,
    },
)
GetWorkerRequestRequestTypeDef = TypedDict(
    "GetWorkerRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "workerId": str,
    },
)
IpAddressesOutputTypeDef = TypedDict(
    "IpAddressesOutputTypeDef",
    {
        "ipV4Addresses": NotRequired[List[str]],
        "ipV6Addresses": NotRequired[List[str]],
    },
)
IpAddressesTypeDef = TypedDict(
    "IpAddressesTypeDef",
    {
        "ipV4Addresses": NotRequired[Sequence[str]],
        "ipV6Addresses": NotRequired[Sequence[str]],
    },
)
JobAttachmentDetailsIdentifiersTypeDef = TypedDict(
    "JobAttachmentDetailsIdentifiersTypeDef",
    {
        "jobId": str,
    },
)
PathMappingRuleTypeDef = TypedDict(
    "PathMappingRuleTypeDef",
    {
        "sourcePathFormat": PathFormatType,
        "sourcePath": str,
        "destinationPath": str,
    },
)
JobDetailsIdentifiersTypeDef = TypedDict(
    "JobDetailsIdentifiersTypeDef",
    {
        "jobId": str,
    },
)
StepDetailsIdentifiersTypeDef = TypedDict(
    "StepDetailsIdentifiersTypeDef",
    {
        "jobId": str,
        "stepId": str,
    },
)
StepDetailsEntityTypeDef = TypedDict(
    "StepDetailsEntityTypeDef",
    {
        "jobId": str,
        "stepId": str,
        "schemaVersion": str,
        "template": Dict[str, Any],
        "dependencies": List[str],
    },
)
JobMemberTypeDef = TypedDict(
    "JobMemberTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "jobId": str,
        "principalId": str,
        "principalType": PrincipalTypeType,
        "identityStoreId": str,
        "membershipLevel": MembershipLevelType,
    },
)
PosixUserTypeDef = TypedDict(
    "PosixUserTypeDef",
    {
        "user": str,
        "group": str,
    },
)
WindowsUserTypeDef = TypedDict(
    "WindowsUserTypeDef",
    {
        "user": str,
        "passwordArn": str,
    },
)
JobSummaryTypeDef = TypedDict(
    "JobSummaryTypeDef",
    {
        "jobId": str,
        "name": str,
        "lifecycleStatus": JobLifecycleStatusType,
        "lifecycleStatusMessage": str,
        "priority": int,
        "createdAt": datetime,
        "createdBy": str,
        "updatedAt": NotRequired[datetime],
        "updatedBy": NotRequired[str],
        "startedAt": NotRequired[datetime],
        "endedAt": NotRequired[datetime],
        "taskRunStatus": NotRequired[TaskRunStatusType],
        "targetTaskRunStatus": NotRequired[JobTargetTaskRunStatusType],
        "taskRunStatusCounts": NotRequired[Dict[TaskRunStatusType, int]],
        "maxFailedTasksCount": NotRequired[int],
        "maxRetriesPerTask": NotRequired[int],
        "sourceJobId": NotRequired[str],
    },
)
LicenseEndpointSummaryTypeDef = TypedDict(
    "LicenseEndpointSummaryTypeDef",
    {
        "licenseEndpointId": NotRequired[str],
        "status": NotRequired[LicenseEndpointStatusType],
        "statusMessage": NotRequired[str],
        "vpcId": NotRequired[str],
    },
)
ListAvailableMeteredProductsRequestRequestTypeDef = TypedDict(
    "ListAvailableMeteredProductsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
MeteredProductSummaryTypeDef = TypedDict(
    "MeteredProductSummaryTypeDef",
    {
        "productId": str,
        "family": str,
        "vendor": str,
        "port": int,
    },
)
ListBudgetsRequestRequestTypeDef = TypedDict(
    "ListBudgetsRequestRequestTypeDef",
    {
        "farmId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "status": NotRequired[BudgetStatusType],
    },
)
ListFarmMembersRequestRequestTypeDef = TypedDict(
    "ListFarmMembersRequestRequestTypeDef",
    {
        "farmId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListFarmsRequestRequestTypeDef = TypedDict(
    "ListFarmsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "principalId": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListFleetMembersRequestRequestTypeDef = TypedDict(
    "ListFleetMembersRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListFleetsRequestRequestTypeDef = TypedDict(
    "ListFleetsRequestRequestTypeDef",
    {
        "farmId": str,
        "principalId": NotRequired[str],
        "displayName": NotRequired[str],
        "status": NotRequired[FleetStatusType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListJobMembersRequestRequestTypeDef = TypedDict(
    "ListJobMembersRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "jobId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListJobParameterDefinitionsRequestRequestTypeDef = TypedDict(
    "ListJobParameterDefinitionsRequestRequestTypeDef",
    {
        "farmId": str,
        "jobId": str,
        "queueId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListJobsRequestRequestTypeDef = TypedDict(
    "ListJobsRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "principalId": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListLicenseEndpointsRequestRequestTypeDef = TypedDict(
    "ListLicenseEndpointsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListMeteredProductsRequestRequestTypeDef = TypedDict(
    "ListMeteredProductsRequestRequestTypeDef",
    {
        "licenseEndpointId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListMonitorsRequestRequestTypeDef = TypedDict(
    "ListMonitorsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
MonitorSummaryTypeDef = TypedDict(
    "MonitorSummaryTypeDef",
    {
        "monitorId": str,
        "displayName": str,
        "subdomain": str,
        "url": str,
        "roleArn": str,
        "identityCenterInstanceArn": str,
        "identityCenterApplicationArn": str,
        "createdAt": datetime,
        "createdBy": str,
        "updatedAt": NotRequired[datetime],
        "updatedBy": NotRequired[str],
    },
)
ListQueueEnvironmentsRequestRequestTypeDef = TypedDict(
    "ListQueueEnvironmentsRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
QueueEnvironmentSummaryTypeDef = TypedDict(
    "QueueEnvironmentSummaryTypeDef",
    {
        "queueEnvironmentId": str,
        "name": str,
        "priority": int,
    },
)
ListQueueFleetAssociationsRequestRequestTypeDef = TypedDict(
    "ListQueueFleetAssociationsRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": NotRequired[str],
        "fleetId": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
QueueFleetAssociationSummaryTypeDef = TypedDict(
    "QueueFleetAssociationSummaryTypeDef",
    {
        "queueId": str,
        "fleetId": str,
        "status": QueueFleetAssociationStatusType,
        "createdAt": datetime,
        "createdBy": str,
        "updatedAt": NotRequired[datetime],
        "updatedBy": NotRequired[str],
    },
)
ListQueueMembersRequestRequestTypeDef = TypedDict(
    "ListQueueMembersRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
QueueMemberTypeDef = TypedDict(
    "QueueMemberTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "principalId": str,
        "principalType": PrincipalTypeType,
        "identityStoreId": str,
        "membershipLevel": MembershipLevelType,
    },
)
ListQueuesRequestRequestTypeDef = TypedDict(
    "ListQueuesRequestRequestTypeDef",
    {
        "farmId": str,
        "principalId": NotRequired[str],
        "status": NotRequired[QueueStatusType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
QueueSummaryTypeDef = TypedDict(
    "QueueSummaryTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "displayName": str,
        "status": QueueStatusType,
        "defaultBudgetAction": DefaultQueueBudgetActionType,
        "createdAt": datetime,
        "createdBy": str,
        "blockedReason": NotRequired[QueueBlockedReasonType],
        "updatedAt": NotRequired[datetime],
        "updatedBy": NotRequired[str],
    },
)
ListSessionActionsRequestRequestTypeDef = TypedDict(
    "ListSessionActionsRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "jobId": str,
        "sessionId": NotRequired[str],
        "taskId": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListSessionsForWorkerRequestRequestTypeDef = TypedDict(
    "ListSessionsForWorkerRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "workerId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
WorkerSessionSummaryTypeDef = TypedDict(
    "WorkerSessionSummaryTypeDef",
    {
        "sessionId": str,
        "queueId": str,
        "jobId": str,
        "startedAt": datetime,
        "lifecycleStatus": SessionLifecycleStatusType,
        "endedAt": NotRequired[datetime],
        "targetLifecycleStatus": NotRequired[Literal["ENDED"]],
    },
)
ListSessionsRequestRequestTypeDef = TypedDict(
    "ListSessionsRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "jobId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
SessionSummaryTypeDef = TypedDict(
    "SessionSummaryTypeDef",
    {
        "sessionId": str,
        "fleetId": str,
        "workerId": str,
        "startedAt": datetime,
        "lifecycleStatus": SessionLifecycleStatusType,
        "endedAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
        "updatedBy": NotRequired[str],
        "targetLifecycleStatus": NotRequired[Literal["ENDED"]],
    },
)
ListStepConsumersRequestRequestTypeDef = TypedDict(
    "ListStepConsumersRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "jobId": str,
        "stepId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
StepConsumerTypeDef = TypedDict(
    "StepConsumerTypeDef",
    {
        "stepId": str,
        "status": DependencyConsumerResolutionStatusType,
    },
)
ListStepDependenciesRequestRequestTypeDef = TypedDict(
    "ListStepDependenciesRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "jobId": str,
        "stepId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
StepDependencyTypeDef = TypedDict(
    "StepDependencyTypeDef",
    {
        "stepId": str,
        "status": DependencyConsumerResolutionStatusType,
    },
)
ListStepsRequestRequestTypeDef = TypedDict(
    "ListStepsRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "jobId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListStorageProfilesForQueueRequestRequestTypeDef = TypedDict(
    "ListStorageProfilesForQueueRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
StorageProfileSummaryTypeDef = TypedDict(
    "StorageProfileSummaryTypeDef",
    {
        "storageProfileId": str,
        "displayName": str,
        "osFamily": StorageProfileOperatingSystemFamilyType,
    },
)
ListStorageProfilesRequestRequestTypeDef = TypedDict(
    "ListStorageProfilesRequestRequestTypeDef",
    {
        "farmId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
ListTasksRequestRequestTypeDef = TypedDict(
    "ListTasksRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "jobId": str,
        "stepId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListWorkersRequestRequestTypeDef = TypedDict(
    "ListWorkersRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ManifestPropertiesTypeDef = TypedDict(
    "ManifestPropertiesTypeDef",
    {
        "rootPath": str,
        "rootPathFormat": PathFormatType,
        "fileSystemLocationName": NotRequired[str],
        "outputRelativeDirectories": NotRequired[Sequence[str]],
        "inputManifestPath": NotRequired[str],
        "inputManifestHash": NotRequired[str],
    },
)
ParameterFilterExpressionTypeDef = TypedDict(
    "ParameterFilterExpressionTypeDef",
    {
        "name": str,
        "operator": ComparisonOperatorType,
        "value": str,
    },
)
ParameterSortExpressionTypeDef = TypedDict(
    "ParameterSortExpressionTypeDef",
    {
        "sortOrder": SortOrderType,
        "name": str,
    },
)
StepParameterTypeDef = TypedDict(
    "StepParameterTypeDef",
    {
        "name": str,
        "type": StepParameterTypeType,
    },
)
PutMeteredProductRequestRequestTypeDef = TypedDict(
    "PutMeteredProductRequestRequestTypeDef",
    {
        "licenseEndpointId": str,
        "productId": str,
    },
)
SearchTermFilterExpressionTypeDef = TypedDict(
    "SearchTermFilterExpressionTypeDef",
    {
        "searchTerm": str,
    },
)
StringFilterExpressionTypeDef = TypedDict(
    "StringFilterExpressionTypeDef",
    {
        "name": str,
        "operator": ComparisonOperatorType,
        "value": str,
    },
)
UserJobsFirstTypeDef = TypedDict(
    "UserJobsFirstTypeDef",
    {
        "userIdentityId": str,
    },
)
ServiceManagedEc2InstanceMarketOptionsTypeDef = TypedDict(
    "ServiceManagedEc2InstanceMarketOptionsTypeDef",
    {
        "type": Ec2MarketTypeType,
    },
)
SyncInputJobAttachmentsSessionActionDefinitionSummaryTypeDef = TypedDict(
    "SyncInputJobAttachmentsSessionActionDefinitionSummaryTypeDef",
    {
        "stepId": NotRequired[str],
    },
)
TaskRunSessionActionDefinitionSummaryTypeDef = TypedDict(
    "TaskRunSessionActionDefinitionSummaryTypeDef",
    {
        "taskId": str,
        "stepId": str,
    },
)
SyncInputJobAttachmentsSessionActionDefinitionTypeDef = TypedDict(
    "SyncInputJobAttachmentsSessionActionDefinitionTypeDef",
    {
        "stepId": NotRequired[str],
    },
)
SessionsStatisticsResourcesTypeDef = TypedDict(
    "SessionsStatisticsResourcesTypeDef",
    {
        "queueIds": NotRequired[Sequence[str]],
        "fleetIds": NotRequired[Sequence[str]],
    },
)
StatsTypeDef = TypedDict(
    "StatsTypeDef",
    {
        "min": NotRequired[float],
        "max": NotRequired[float],
        "avg": NotRequired[float],
        "sum": NotRequired[float],
    },
)
StepAmountCapabilityTypeDef = TypedDict(
    "StepAmountCapabilityTypeDef",
    {
        "name": str,
        "min": NotRequired[float],
        "max": NotRequired[float],
        "value": NotRequired[float],
    },
)
StepAttributeCapabilityTypeDef = TypedDict(
    "StepAttributeCapabilityTypeDef",
    {
        "name": str,
        "anyOf": NotRequired[List[str]],
        "allOf": NotRequired[List[str]],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": NotRequired[Mapping[str, str]],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UpdateFarmRequestRequestTypeDef = TypedDict(
    "UpdateFarmRequestRequestTypeDef",
    {
        "farmId": str,
        "displayName": NotRequired[str],
        "description": NotRequired[str],
    },
)
UpdateJobRequestRequestTypeDef = TypedDict(
    "UpdateJobRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "jobId": str,
        "clientToken": NotRequired[str],
        "targetTaskRunStatus": NotRequired[JobTargetTaskRunStatusType],
        "priority": NotRequired[int],
        "maxFailedTasksCount": NotRequired[int],
        "maxRetriesPerTask": NotRequired[int],
        "lifecycleStatus": NotRequired[Literal["ARCHIVED"]],
    },
)
UpdateMonitorRequestRequestTypeDef = TypedDict(
    "UpdateMonitorRequestRequestTypeDef",
    {
        "monitorId": str,
        "subdomain": NotRequired[str],
        "displayName": NotRequired[str],
        "roleArn": NotRequired[str],
    },
)
UpdateQueueEnvironmentRequestRequestTypeDef = TypedDict(
    "UpdateQueueEnvironmentRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "queueEnvironmentId": str,
        "clientToken": NotRequired[str],
        "priority": NotRequired[int],
        "templateType": NotRequired[EnvironmentTemplateTypeType],
        "template": NotRequired[str],
    },
)
UpdateQueueFleetAssociationRequestRequestTypeDef = TypedDict(
    "UpdateQueueFleetAssociationRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "fleetId": str,
        "status": UpdateQueueFleetAssociationStatusType,
    },
)
UpdateSessionRequestRequestTypeDef = TypedDict(
    "UpdateSessionRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "jobId": str,
        "sessionId": str,
        "targetLifecycleStatus": Literal["ENDED"],
        "clientToken": NotRequired[str],
    },
)
UpdateStepRequestRequestTypeDef = TypedDict(
    "UpdateStepRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "jobId": str,
        "stepId": str,
        "targetTaskRunStatus": StepTargetTaskRunStatusType,
        "clientToken": NotRequired[str],
    },
)
UpdateTaskRequestRequestTypeDef = TypedDict(
    "UpdateTaskRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "jobId": str,
        "stepId": str,
        "taskId": str,
        "targetRunStatus": TaskTargetRunStatusType,
        "clientToken": NotRequired[str],
    },
)
WorkerAmountCapabilityTypeDef = TypedDict(
    "WorkerAmountCapabilityTypeDef",
    {
        "name": str,
        "value": float,
    },
)
WorkerAttributeCapabilityTypeDef = TypedDict(
    "WorkerAttributeCapabilityTypeDef",
    {
        "name": str,
        "values": Sequence[str],
    },
)
AssignedTaskRunSessionActionDefinitionTypeDef = TypedDict(
    "AssignedTaskRunSessionActionDefinitionTypeDef",
    {
        "taskId": str,
        "stepId": str,
        "parameters": Dict[str, TaskParameterValueTypeDef],
    },
)
TaskRunSessionActionDefinitionTypeDef = TypedDict(
    "TaskRunSessionActionDefinitionTypeDef",
    {
        "taskId": str,
        "stepId": str,
        "parameters": Dict[str, TaskParameterValueTypeDef],
    },
)
TaskSearchSummaryTypeDef = TypedDict(
    "TaskSearchSummaryTypeDef",
    {
        "taskId": NotRequired[str],
        "stepId": NotRequired[str],
        "jobId": NotRequired[str],
        "queueId": NotRequired[str],
        "runStatus": NotRequired[TaskRunStatusType],
        "targetRunStatus": NotRequired[TaskTargetRunStatusType],
        "parameters": NotRequired[Dict[str, TaskParameterValueTypeDef]],
        "failureRetryCount": NotRequired[int],
        "startedAt": NotRequired[datetime],
        "endedAt": NotRequired[datetime],
    },
)
TaskSummaryTypeDef = TypedDict(
    "TaskSummaryTypeDef",
    {
        "taskId": str,
        "createdAt": datetime,
        "createdBy": str,
        "runStatus": TaskRunStatusType,
        "targetRunStatus": NotRequired[TaskTargetRunStatusType],
        "failureRetryCount": NotRequired[int],
        "parameters": NotRequired[Dict[str, TaskParameterValueTypeDef]],
        "startedAt": NotRequired[datetime],
        "endedAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
        "updatedBy": NotRequired[str],
        "latestSessionActionId": NotRequired[str],
    },
)
AssumeFleetRoleForReadResponseTypeDef = TypedDict(
    "AssumeFleetRoleForReadResponseTypeDef",
    {
        "credentials": AwsCredentialsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssumeFleetRoleForWorkerResponseTypeDef = TypedDict(
    "AssumeFleetRoleForWorkerResponseTypeDef",
    {
        "credentials": AwsCredentialsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssumeQueueRoleForReadResponseTypeDef = TypedDict(
    "AssumeQueueRoleForReadResponseTypeDef",
    {
        "credentials": AwsCredentialsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssumeQueueRoleForUserResponseTypeDef = TypedDict(
    "AssumeQueueRoleForUserResponseTypeDef",
    {
        "credentials": AwsCredentialsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssumeQueueRoleForWorkerResponseTypeDef = TypedDict(
    "AssumeQueueRoleForWorkerResponseTypeDef",
    {
        "credentials": AwsCredentialsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CopyJobTemplateResponseTypeDef = TypedDict(
    "CopyJobTemplateResponseTypeDef",
    {
        "templateType": JobTemplateTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateBudgetResponseTypeDef = TypedDict(
    "CreateBudgetResponseTypeDef",
    {
        "budgetId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFarmResponseTypeDef = TypedDict(
    "CreateFarmResponseTypeDef",
    {
        "farmId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFleetResponseTypeDef = TypedDict(
    "CreateFleetResponseTypeDef",
    {
        "fleetId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateJobResponseTypeDef = TypedDict(
    "CreateJobResponseTypeDef",
    {
        "jobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateLicenseEndpointResponseTypeDef = TypedDict(
    "CreateLicenseEndpointResponseTypeDef",
    {
        "licenseEndpointId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMonitorResponseTypeDef = TypedDict(
    "CreateMonitorResponseTypeDef",
    {
        "monitorId": str,
        "identityCenterApplicationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateQueueEnvironmentResponseTypeDef = TypedDict(
    "CreateQueueEnvironmentResponseTypeDef",
    {
        "queueEnvironmentId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateQueueResponseTypeDef = TypedDict(
    "CreateQueueResponseTypeDef",
    {
        "queueId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateStorageProfileResponseTypeDef = TypedDict(
    "CreateStorageProfileResponseTypeDef",
    {
        "storageProfileId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWorkerResponseTypeDef = TypedDict(
    "CreateWorkerResponseTypeDef",
    {
        "workerId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFarmResponseTypeDef = TypedDict(
    "GetFarmResponseTypeDef",
    {
        "farmId": str,
        "displayName": str,
        "description": str,
        "kmsKeyArn": str,
        "createdAt": datetime,
        "createdBy": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLicenseEndpointResponseTypeDef = TypedDict(
    "GetLicenseEndpointResponseTypeDef",
    {
        "licenseEndpointId": str,
        "status": LicenseEndpointStatusType,
        "statusMessage": str,
        "vpcId": str,
        "dnsName": str,
        "subnetIds": List[str],
        "securityGroupIds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMonitorResponseTypeDef = TypedDict(
    "GetMonitorResponseTypeDef",
    {
        "monitorId": str,
        "displayName": str,
        "subdomain": str,
        "url": str,
        "roleArn": str,
        "identityCenterInstanceArn": str,
        "identityCenterApplicationArn": str,
        "createdAt": datetime,
        "createdBy": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetQueueEnvironmentResponseTypeDef = TypedDict(
    "GetQueueEnvironmentResponseTypeDef",
    {
        "queueEnvironmentId": str,
        "name": str,
        "priority": int,
        "templateType": EnvironmentTemplateTypeType,
        "template": str,
        "createdAt": datetime,
        "createdBy": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetQueueFleetAssociationResponseTypeDef = TypedDict(
    "GetQueueFleetAssociationResponseTypeDef",
    {
        "queueId": str,
        "fleetId": str,
        "status": QueueFleetAssociationStatusType,
        "createdAt": datetime,
        "createdBy": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTaskResponseTypeDef = TypedDict(
    "GetTaskResponseTypeDef",
    {
        "taskId": str,
        "createdAt": datetime,
        "createdBy": str,
        "runStatus": TaskRunStatusType,
        "targetRunStatus": TaskTargetRunStatusType,
        "failureRetryCount": int,
        "parameters": Dict[str, TaskParameterValueTypeDef],
        "startedAt": datetime,
        "endedAt": datetime,
        "updatedAt": datetime,
        "updatedBy": str,
        "latestSessionActionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListJobParameterDefinitionsResponseTypeDef = TypedDict(
    "ListJobParameterDefinitionsResponseTypeDef",
    {
        "jobParameterDefinitions": List[Dict[str, Any]],
        "nextToken": str,
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
StartSessionsStatisticsAggregationResponseTypeDef = TypedDict(
    "StartSessionsStatisticsAggregationResponseTypeDef",
    {
        "aggregationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateWorkerResponseTypeDef = TypedDict(
    "UpdateWorkerResponseTypeDef",
    {
        "log": LogConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AttachmentsOutputTypeDef = TypedDict(
    "AttachmentsOutputTypeDef",
    {
        "manifests": List[ManifestPropertiesOutputTypeDef],
        "fileSystem": NotRequired[JobAttachmentsFileSystemType],
    },
)
BudgetScheduleOutputTypeDef = TypedDict(
    "BudgetScheduleOutputTypeDef",
    {
        "fixed": NotRequired[FixedBudgetScheduleOutputTypeDef],
    },
)
BudgetSummaryTypeDef = TypedDict(
    "BudgetSummaryTypeDef",
    {
        "budgetId": str,
        "usageTrackingResource": UsageTrackingResourceTypeDef,
        "status": BudgetStatusType,
        "displayName": str,
        "approximateDollarLimit": float,
        "usages": ConsumedUsagesTypeDef,
        "createdBy": str,
        "createdAt": datetime,
        "description": NotRequired[str],
        "updatedBy": NotRequired[str],
        "updatedAt": NotRequired[datetime],
    },
)
CopyJobTemplateRequestRequestTypeDef = TypedDict(
    "CopyJobTemplateRequestRequestTypeDef",
    {
        "farmId": str,
        "jobId": str,
        "queueId": str,
        "targetS3Location": S3LocationTypeDef,
    },
)
JobSearchSummaryTypeDef = TypedDict(
    "JobSearchSummaryTypeDef",
    {
        "jobId": NotRequired[str],
        "queueId": NotRequired[str],
        "name": NotRequired[str],
        "lifecycleStatus": NotRequired[JobLifecycleStatusType],
        "lifecycleStatusMessage": NotRequired[str],
        "taskRunStatus": NotRequired[TaskRunStatusType],
        "targetTaskRunStatus": NotRequired[JobTargetTaskRunStatusType],
        "taskRunStatusCounts": NotRequired[Dict[TaskRunStatusType, int]],
        "priority": NotRequired[int],
        "maxFailedTasksCount": NotRequired[int],
        "maxRetriesPerTask": NotRequired[int],
        "createdBy": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "endedAt": NotRequired[datetime],
        "startedAt": NotRequired[datetime],
        "jobParameters": NotRequired[Dict[str, JobParameterTypeDef]],
        "sourceJobId": NotRequired[str],
    },
)
CreateStorageProfileRequestRequestTypeDef = TypedDict(
    "CreateStorageProfileRequestRequestTypeDef",
    {
        "farmId": str,
        "displayName": str,
        "osFamily": StorageProfileOperatingSystemFamilyType,
        "clientToken": NotRequired[str],
        "fileSystemLocations": NotRequired[Sequence[FileSystemLocationTypeDef]],
    },
)
GetStorageProfileForQueueResponseTypeDef = TypedDict(
    "GetStorageProfileForQueueResponseTypeDef",
    {
        "storageProfileId": str,
        "displayName": str,
        "osFamily": StorageProfileOperatingSystemFamilyType,
        "fileSystemLocations": List[FileSystemLocationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetStorageProfileResponseTypeDef = TypedDict(
    "GetStorageProfileResponseTypeDef",
    {
        "storageProfileId": str,
        "displayName": str,
        "osFamily": StorageProfileOperatingSystemFamilyType,
        "createdAt": datetime,
        "createdBy": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "fileSystemLocations": List[FileSystemLocationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateStorageProfileRequestRequestTypeDef = TypedDict(
    "UpdateStorageProfileRequestRequestTypeDef",
    {
        "farmId": str,
        "storageProfileId": str,
        "clientToken": NotRequired[str],
        "displayName": NotRequired[str],
        "osFamily": NotRequired[StorageProfileOperatingSystemFamilyType],
        "fileSystemLocationsToAdd": NotRequired[Sequence[FileSystemLocationTypeDef]],
        "fileSystemLocationsToRemove": NotRequired[Sequence[FileSystemLocationTypeDef]],
    },
)
FleetCapabilitiesTypeDef = TypedDict(
    "FleetCapabilitiesTypeDef",
    {
        "amounts": NotRequired[List[FleetAmountCapabilityTypeDef]],
        "attributes": NotRequired[List[FleetAttributeCapabilityOutputTypeDef]],
    },
)
CustomerManagedWorkerCapabilitiesOutputTypeDef = TypedDict(
    "CustomerManagedWorkerCapabilitiesOutputTypeDef",
    {
        "vCpuCount": VCpuCountRangeTypeDef,
        "memoryMiB": MemoryMiBRangeTypeDef,
        "osFamily": CustomerManagedFleetOperatingSystemFamilyType,
        "cpuArchitectureType": CpuArchitectureTypeType,
        "acceleratorTypes": NotRequired[List[Literal["gpu"]]],
        "acceleratorCount": NotRequired[AcceleratorCountRangeTypeDef],
        "acceleratorTotalMemoryMiB": NotRequired[AcceleratorTotalMemoryMiBRangeTypeDef],
        "customAmounts": NotRequired[List[FleetAmountCapabilityTypeDef]],
        "customAttributes": NotRequired[List[FleetAttributeCapabilityOutputTypeDef]],
    },
)
DateTimeFilterExpressionTypeDef = TypedDict(
    "DateTimeFilterExpressionTypeDef",
    {
        "name": str,
        "operator": ComparisonOperatorType,
        "dateTime": TimestampTypeDef,
    },
)
FixedBudgetScheduleTypeDef = TypedDict(
    "FixedBudgetScheduleTypeDef",
    {
        "startTime": TimestampTypeDef,
        "endTime": TimestampTypeDef,
    },
)
UpdatedSessionActionInfoTypeDef = TypedDict(
    "UpdatedSessionActionInfoTypeDef",
    {
        "completedStatus": NotRequired[CompletedStatusType],
        "processExitCode": NotRequired[int],
        "progressMessage": NotRequired[str],
        "startedAt": NotRequired[TimestampTypeDef],
        "endedAt": NotRequired[TimestampTypeDef],
        "updatedAt": NotRequired[TimestampTypeDef],
        "progressPercent": NotRequired[float],
    },
)
StepSummaryTypeDef = TypedDict(
    "StepSummaryTypeDef",
    {
        "stepId": str,
        "name": str,
        "lifecycleStatus": StepLifecycleStatusType,
        "taskRunStatus": TaskRunStatusType,
        "taskRunStatusCounts": Dict[TaskRunStatusType, int],
        "createdAt": datetime,
        "createdBy": str,
        "lifecycleStatusMessage": NotRequired[str],
        "targetTaskRunStatus": NotRequired[StepTargetTaskRunStatusType],
        "updatedAt": NotRequired[datetime],
        "updatedBy": NotRequired[str],
        "startedAt": NotRequired[datetime],
        "endedAt": NotRequired[datetime],
        "dependencyCounts": NotRequired[DependencyCountsTypeDef],
    },
)
ServiceManagedEc2InstanceCapabilitiesOutputTypeDef = TypedDict(
    "ServiceManagedEc2InstanceCapabilitiesOutputTypeDef",
    {
        "vCpuCount": VCpuCountRangeTypeDef,
        "memoryMiB": MemoryMiBRangeTypeDef,
        "osFamily": ServiceManagedFleetOperatingSystemFamilyType,
        "cpuArchitectureType": CpuArchitectureTypeType,
        "rootEbsVolume": NotRequired[Ec2EbsVolumeTypeDef],
        "allowedInstanceTypes": NotRequired[List[str]],
        "excludedInstanceTypes": NotRequired[List[str]],
        "customAmounts": NotRequired[List[FleetAmountCapabilityTypeDef]],
        "customAttributes": NotRequired[List[FleetAttributeCapabilityOutputTypeDef]],
    },
)
ListFarmMembersResponseTypeDef = TypedDict(
    "ListFarmMembersResponseTypeDef",
    {
        "members": List[FarmMemberTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListFarmsResponseTypeDef = TypedDict(
    "ListFarmsResponseTypeDef",
    {
        "nextToken": str,
        "farms": List[FarmSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FleetAttributeCapabilityUnionTypeDef = Union[
    FleetAttributeCapabilityTypeDef, FleetAttributeCapabilityOutputTypeDef
]
ServiceManagedEc2InstanceCapabilitiesTypeDef = TypedDict(
    "ServiceManagedEc2InstanceCapabilitiesTypeDef",
    {
        "vCpuCount": VCpuCountRangeTypeDef,
        "memoryMiB": MemoryMiBRangeTypeDef,
        "osFamily": ServiceManagedFleetOperatingSystemFamilyType,
        "cpuArchitectureType": CpuArchitectureTypeType,
        "rootEbsVolume": NotRequired[Ec2EbsVolumeTypeDef],
        "allowedInstanceTypes": NotRequired[Sequence[str]],
        "excludedInstanceTypes": NotRequired[Sequence[str]],
        "customAmounts": NotRequired[Sequence[FleetAmountCapabilityTypeDef]],
        "customAttributes": NotRequired[Sequence[FleetAttributeCapabilityTypeDef]],
    },
)
ListFleetMembersResponseTypeDef = TypedDict(
    "ListFleetMembersResponseTypeDef",
    {
        "members": List[FleetMemberTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFleetRequestFleetActiveWaitTypeDef = TypedDict(
    "GetFleetRequestFleetActiveWaitTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetJobRequestJobCreateCompleteWaitTypeDef = TypedDict(
    "GetJobRequestJobCreateCompleteWaitTypeDef",
    {
        "farmId": str,
        "jobId": str,
        "queueId": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetLicenseEndpointRequestLicenseEndpointDeletedWaitTypeDef = TypedDict(
    "GetLicenseEndpointRequestLicenseEndpointDeletedWaitTypeDef",
    {
        "licenseEndpointId": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetLicenseEndpointRequestLicenseEndpointValidWaitTypeDef = TypedDict(
    "GetLicenseEndpointRequestLicenseEndpointValidWaitTypeDef",
    {
        "licenseEndpointId": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetQueueFleetAssociationRequestQueueFleetAssociationStoppedWaitTypeDef = TypedDict(
    "GetQueueFleetAssociationRequestQueueFleetAssociationStoppedWaitTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "fleetId": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetQueueRequestQueueSchedulingBlockedWaitTypeDef = TypedDict(
    "GetQueueRequestQueueSchedulingBlockedWaitTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetQueueRequestQueueSchedulingWaitTypeDef = TypedDict(
    "GetQueueRequestQueueSchedulingWaitTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetJobEntityErrorTypeDef = TypedDict(
    "GetJobEntityErrorTypeDef",
    {
        "jobDetails": NotRequired[JobDetailsErrorTypeDef],
        "jobAttachmentDetails": NotRequired[JobAttachmentDetailsErrorTypeDef],
        "stepDetails": NotRequired[StepDetailsErrorTypeDef],
        "environmentDetails": NotRequired[EnvironmentDetailsErrorTypeDef],
    },
)
GetSessionsStatisticsAggregationRequestGetSessionsStatisticsAggregationPaginateTypeDef = TypedDict(
    "GetSessionsStatisticsAggregationRequestGetSessionsStatisticsAggregationPaginateTypeDef",
    {
        "farmId": str,
        "aggregationId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAvailableMeteredProductsRequestListAvailableMeteredProductsPaginateTypeDef = TypedDict(
    "ListAvailableMeteredProductsRequestListAvailableMeteredProductsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListBudgetsRequestListBudgetsPaginateTypeDef = TypedDict(
    "ListBudgetsRequestListBudgetsPaginateTypeDef",
    {
        "farmId": str,
        "status": NotRequired[BudgetStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFarmMembersRequestListFarmMembersPaginateTypeDef = TypedDict(
    "ListFarmMembersRequestListFarmMembersPaginateTypeDef",
    {
        "farmId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFarmsRequestListFarmsPaginateTypeDef = TypedDict(
    "ListFarmsRequestListFarmsPaginateTypeDef",
    {
        "principalId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFleetMembersRequestListFleetMembersPaginateTypeDef = TypedDict(
    "ListFleetMembersRequestListFleetMembersPaginateTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFleetsRequestListFleetsPaginateTypeDef = TypedDict(
    "ListFleetsRequestListFleetsPaginateTypeDef",
    {
        "farmId": str,
        "principalId": NotRequired[str],
        "displayName": NotRequired[str],
        "status": NotRequired[FleetStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListJobMembersRequestListJobMembersPaginateTypeDef = TypedDict(
    "ListJobMembersRequestListJobMembersPaginateTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "jobId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListJobParameterDefinitionsRequestListJobParameterDefinitionsPaginateTypeDef = TypedDict(
    "ListJobParameterDefinitionsRequestListJobParameterDefinitionsPaginateTypeDef",
    {
        "farmId": str,
        "jobId": str,
        "queueId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListJobsRequestListJobsPaginateTypeDef = TypedDict(
    "ListJobsRequestListJobsPaginateTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "principalId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListLicenseEndpointsRequestListLicenseEndpointsPaginateTypeDef = TypedDict(
    "ListLicenseEndpointsRequestListLicenseEndpointsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMeteredProductsRequestListMeteredProductsPaginateTypeDef = TypedDict(
    "ListMeteredProductsRequestListMeteredProductsPaginateTypeDef",
    {
        "licenseEndpointId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMonitorsRequestListMonitorsPaginateTypeDef = TypedDict(
    "ListMonitorsRequestListMonitorsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListQueueEnvironmentsRequestListQueueEnvironmentsPaginateTypeDef = TypedDict(
    "ListQueueEnvironmentsRequestListQueueEnvironmentsPaginateTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListQueueFleetAssociationsRequestListQueueFleetAssociationsPaginateTypeDef = TypedDict(
    "ListQueueFleetAssociationsRequestListQueueFleetAssociationsPaginateTypeDef",
    {
        "farmId": str,
        "queueId": NotRequired[str],
        "fleetId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListQueueMembersRequestListQueueMembersPaginateTypeDef = TypedDict(
    "ListQueueMembersRequestListQueueMembersPaginateTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListQueuesRequestListQueuesPaginateTypeDef = TypedDict(
    "ListQueuesRequestListQueuesPaginateTypeDef",
    {
        "farmId": str,
        "principalId": NotRequired[str],
        "status": NotRequired[QueueStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSessionActionsRequestListSessionActionsPaginateTypeDef = TypedDict(
    "ListSessionActionsRequestListSessionActionsPaginateTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "jobId": str,
        "sessionId": NotRequired[str],
        "taskId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSessionsForWorkerRequestListSessionsForWorkerPaginateTypeDef = TypedDict(
    "ListSessionsForWorkerRequestListSessionsForWorkerPaginateTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "workerId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSessionsRequestListSessionsPaginateTypeDef = TypedDict(
    "ListSessionsRequestListSessionsPaginateTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "jobId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListStepConsumersRequestListStepConsumersPaginateTypeDef = TypedDict(
    "ListStepConsumersRequestListStepConsumersPaginateTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "jobId": str,
        "stepId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListStepDependenciesRequestListStepDependenciesPaginateTypeDef = TypedDict(
    "ListStepDependenciesRequestListStepDependenciesPaginateTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "jobId": str,
        "stepId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListStepsRequestListStepsPaginateTypeDef = TypedDict(
    "ListStepsRequestListStepsPaginateTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "jobId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListStorageProfilesForQueueRequestListStorageProfilesForQueuePaginateTypeDef = TypedDict(
    "ListStorageProfilesForQueueRequestListStorageProfilesForQueuePaginateTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListStorageProfilesRequestListStorageProfilesPaginateTypeDef = TypedDict(
    "ListStorageProfilesRequestListStorageProfilesPaginateTypeDef",
    {
        "farmId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTasksRequestListTasksPaginateTypeDef = TypedDict(
    "ListTasksRequestListTasksPaginateTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "jobId": str,
        "stepId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWorkersRequestListWorkersPaginateTypeDef = TypedDict(
    "ListWorkersRequestListWorkersPaginateTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
HostPropertiesResponseTypeDef = TypedDict(
    "HostPropertiesResponseTypeDef",
    {
        "ipAddresses": NotRequired[IpAddressesOutputTypeDef],
        "hostName": NotRequired[str],
        "ec2InstanceArn": NotRequired[str],
        "ec2InstanceType": NotRequired[str],
    },
)
IpAddressesUnionTypeDef = Union[IpAddressesTypeDef, IpAddressesOutputTypeDef]
JobEntityIdentifiersUnionTypeDef = TypedDict(
    "JobEntityIdentifiersUnionTypeDef",
    {
        "jobDetails": NotRequired[JobDetailsIdentifiersTypeDef],
        "jobAttachmentDetails": NotRequired[JobAttachmentDetailsIdentifiersTypeDef],
        "stepDetails": NotRequired[StepDetailsIdentifiersTypeDef],
        "environmentDetails": NotRequired[EnvironmentDetailsIdentifiersTypeDef],
    },
)
ListJobMembersResponseTypeDef = TypedDict(
    "ListJobMembersResponseTypeDef",
    {
        "members": List[JobMemberTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
JobRunAsUserTypeDef = TypedDict(
    "JobRunAsUserTypeDef",
    {
        "runAs": RunAsType,
        "posix": NotRequired[PosixUserTypeDef],
        "windows": NotRequired[WindowsUserTypeDef],
    },
)
ListJobsResponseTypeDef = TypedDict(
    "ListJobsResponseTypeDef",
    {
        "jobs": List[JobSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListLicenseEndpointsResponseTypeDef = TypedDict(
    "ListLicenseEndpointsResponseTypeDef",
    {
        "licenseEndpoints": List[LicenseEndpointSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAvailableMeteredProductsResponseTypeDef = TypedDict(
    "ListAvailableMeteredProductsResponseTypeDef",
    {
        "meteredProducts": List[MeteredProductSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListMeteredProductsResponseTypeDef = TypedDict(
    "ListMeteredProductsResponseTypeDef",
    {
        "meteredProducts": List[MeteredProductSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListMonitorsResponseTypeDef = TypedDict(
    "ListMonitorsResponseTypeDef",
    {
        "nextToken": str,
        "monitors": List[MonitorSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListQueueEnvironmentsResponseTypeDef = TypedDict(
    "ListQueueEnvironmentsResponseTypeDef",
    {
        "environments": List[QueueEnvironmentSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListQueueFleetAssociationsResponseTypeDef = TypedDict(
    "ListQueueFleetAssociationsResponseTypeDef",
    {
        "queueFleetAssociations": List[QueueFleetAssociationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListQueueMembersResponseTypeDef = TypedDict(
    "ListQueueMembersResponseTypeDef",
    {
        "members": List[QueueMemberTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListQueuesResponseTypeDef = TypedDict(
    "ListQueuesResponseTypeDef",
    {
        "queues": List[QueueSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSessionsForWorkerResponseTypeDef = TypedDict(
    "ListSessionsForWorkerResponseTypeDef",
    {
        "sessions": List[WorkerSessionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSessionsResponseTypeDef = TypedDict(
    "ListSessionsResponseTypeDef",
    {
        "sessions": List[SessionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListStepConsumersResponseTypeDef = TypedDict(
    "ListStepConsumersResponseTypeDef",
    {
        "consumers": List[StepConsumerTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListStepDependenciesResponseTypeDef = TypedDict(
    "ListStepDependenciesResponseTypeDef",
    {
        "dependencies": List[StepDependencyTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListStorageProfilesForQueueResponseTypeDef = TypedDict(
    "ListStorageProfilesForQueueResponseTypeDef",
    {
        "storageProfiles": List[StorageProfileSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListStorageProfilesResponseTypeDef = TypedDict(
    "ListStorageProfilesResponseTypeDef",
    {
        "storageProfiles": List[StorageProfileSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ManifestPropertiesUnionTypeDef = Union[ManifestPropertiesTypeDef, ManifestPropertiesOutputTypeDef]
ParameterSpaceTypeDef = TypedDict(
    "ParameterSpaceTypeDef",
    {
        "parameters": List[StepParameterTypeDef],
        "combination": NotRequired[str],
    },
)
SearchSortExpressionTypeDef = TypedDict(
    "SearchSortExpressionTypeDef",
    {
        "userJobsFirst": NotRequired[UserJobsFirstTypeDef],
        "fieldSort": NotRequired[FieldSortExpressionTypeDef],
        "parameterSort": NotRequired[ParameterSortExpressionTypeDef],
    },
)
SessionActionDefinitionSummaryTypeDef = TypedDict(
    "SessionActionDefinitionSummaryTypeDef",
    {
        "envEnter": NotRequired[EnvironmentEnterSessionActionDefinitionSummaryTypeDef],
        "envExit": NotRequired[EnvironmentExitSessionActionDefinitionSummaryTypeDef],
        "taskRun": NotRequired[TaskRunSessionActionDefinitionSummaryTypeDef],
        "syncInputJobAttachments": NotRequired[
            SyncInputJobAttachmentsSessionActionDefinitionSummaryTypeDef
        ],
    },
)
StartSessionsStatisticsAggregationRequestRequestTypeDef = TypedDict(
    "StartSessionsStatisticsAggregationRequestRequestTypeDef",
    {
        "farmId": str,
        "resourceIds": SessionsStatisticsResourcesTypeDef,
        "startTime": TimestampTypeDef,
        "endTime": TimestampTypeDef,
        "groupBy": Sequence[UsageGroupByFieldType],
        "statistics": Sequence[UsageStatisticType],
        "timezone": NotRequired[str],
        "period": NotRequired[PeriodType],
    },
)
StatisticsTypeDef = TypedDict(
    "StatisticsTypeDef",
    {
        "count": int,
        "costInUsd": StatsTypeDef,
        "runtimeInSeconds": StatsTypeDef,
        "queueId": NotRequired[str],
        "fleetId": NotRequired[str],
        "jobId": NotRequired[str],
        "jobName": NotRequired[str],
        "userId": NotRequired[str],
        "usageType": NotRequired[UsageTypeType],
        "licenseProduct": NotRequired[str],
        "instanceType": NotRequired[str],
        "aggregationStartTime": NotRequired[datetime],
        "aggregationEndTime": NotRequired[datetime],
    },
)
StepRequiredCapabilitiesTypeDef = TypedDict(
    "StepRequiredCapabilitiesTypeDef",
    {
        "attributes": List[StepAttributeCapabilityTypeDef],
        "amounts": List[StepAmountCapabilityTypeDef],
    },
)
WorkerCapabilitiesTypeDef = TypedDict(
    "WorkerCapabilitiesTypeDef",
    {
        "amounts": Sequence[WorkerAmountCapabilityTypeDef],
        "attributes": Sequence[WorkerAttributeCapabilityTypeDef],
    },
)
AssignedSessionActionDefinitionTypeDef = TypedDict(
    "AssignedSessionActionDefinitionTypeDef",
    {
        "envEnter": NotRequired[AssignedEnvironmentEnterSessionActionDefinitionTypeDef],
        "envExit": NotRequired[AssignedEnvironmentExitSessionActionDefinitionTypeDef],
        "taskRun": NotRequired[AssignedTaskRunSessionActionDefinitionTypeDef],
        "syncInputJobAttachments": NotRequired[
            AssignedSyncInputJobAttachmentsSessionActionDefinitionTypeDef
        ],
    },
)
SessionActionDefinitionTypeDef = TypedDict(
    "SessionActionDefinitionTypeDef",
    {
        "envEnter": NotRequired[EnvironmentEnterSessionActionDefinitionTypeDef],
        "envExit": NotRequired[EnvironmentExitSessionActionDefinitionTypeDef],
        "taskRun": NotRequired[TaskRunSessionActionDefinitionTypeDef],
        "syncInputJobAttachments": NotRequired[
            SyncInputJobAttachmentsSessionActionDefinitionTypeDef
        ],
    },
)
SearchTasksResponseTypeDef = TypedDict(
    "SearchTasksResponseTypeDef",
    {
        "tasks": List[TaskSearchSummaryTypeDef],
        "nextItemOffset": int,
        "totalResults": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTasksResponseTypeDef = TypedDict(
    "ListTasksResponseTypeDef",
    {
        "tasks": List[TaskSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetJobResponseTypeDef = TypedDict(
    "GetJobResponseTypeDef",
    {
        "jobId": str,
        "name": str,
        "lifecycleStatus": JobLifecycleStatusType,
        "lifecycleStatusMessage": str,
        "priority": int,
        "createdAt": datetime,
        "createdBy": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "startedAt": datetime,
        "endedAt": datetime,
        "taskRunStatus": TaskRunStatusType,
        "targetTaskRunStatus": JobTargetTaskRunStatusType,
        "taskRunStatusCounts": Dict[TaskRunStatusType, int],
        "storageProfileId": str,
        "maxFailedTasksCount": int,
        "maxRetriesPerTask": int,
        "parameters": Dict[str, JobParameterTypeDef],
        "attachments": AttachmentsOutputTypeDef,
        "description": str,
        "sourceJobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
JobAttachmentDetailsEntityTypeDef = TypedDict(
    "JobAttachmentDetailsEntityTypeDef",
    {
        "jobId": str,
        "attachments": AttachmentsOutputTypeDef,
    },
)
GetBudgetResponseTypeDef = TypedDict(
    "GetBudgetResponseTypeDef",
    {
        "budgetId": str,
        "usageTrackingResource": UsageTrackingResourceTypeDef,
        "status": BudgetStatusType,
        "displayName": str,
        "description": str,
        "approximateDollarLimit": float,
        "usages": ConsumedUsagesTypeDef,
        "actions": List[ResponseBudgetActionTypeDef],
        "schedule": BudgetScheduleOutputTypeDef,
        "createdBy": str,
        "createdAt": datetime,
        "updatedBy": str,
        "updatedAt": datetime,
        "queueStoppedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListBudgetsResponseTypeDef = TypedDict(
    "ListBudgetsResponseTypeDef",
    {
        "nextToken": str,
        "budgets": List[BudgetSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchJobsResponseTypeDef = TypedDict(
    "SearchJobsResponseTypeDef",
    {
        "jobs": List[JobSearchSummaryTypeDef],
        "nextItemOffset": int,
        "totalResults": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CustomerManagedFleetConfigurationOutputTypeDef = TypedDict(
    "CustomerManagedFleetConfigurationOutputTypeDef",
    {
        "mode": AutoScalingModeType,
        "workerCapabilities": CustomerManagedWorkerCapabilitiesOutputTypeDef,
        "storageProfileId": NotRequired[str],
    },
)
SearchFilterExpressionTypeDef = TypedDict(
    "SearchFilterExpressionTypeDef",
    {
        "dateTimeFilter": NotRequired[DateTimeFilterExpressionTypeDef],
        "parameterFilter": NotRequired[ParameterFilterExpressionTypeDef],
        "searchTermFilter": NotRequired[SearchTermFilterExpressionTypeDef],
        "stringFilter": NotRequired[StringFilterExpressionTypeDef],
        "groupFilter": NotRequired[Mapping[str, Any]],
    },
)
FixedBudgetScheduleUnionTypeDef = Union[
    FixedBudgetScheduleTypeDef, FixedBudgetScheduleOutputTypeDef
]
UpdateWorkerScheduleRequestRequestTypeDef = TypedDict(
    "UpdateWorkerScheduleRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "workerId": str,
        "updatedSessionActions": NotRequired[Mapping[str, UpdatedSessionActionInfoTypeDef]],
    },
)
ListStepsResponseTypeDef = TypedDict(
    "ListStepsResponseTypeDef",
    {
        "steps": List[StepSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ServiceManagedEc2FleetConfigurationOutputTypeDef = TypedDict(
    "ServiceManagedEc2FleetConfigurationOutputTypeDef",
    {
        "instanceCapabilities": ServiceManagedEc2InstanceCapabilitiesOutputTypeDef,
        "instanceMarketOptions": ServiceManagedEc2InstanceMarketOptionsTypeDef,
    },
)
CustomerManagedWorkerCapabilitiesTypeDef = TypedDict(
    "CustomerManagedWorkerCapabilitiesTypeDef",
    {
        "vCpuCount": VCpuCountRangeTypeDef,
        "memoryMiB": MemoryMiBRangeTypeDef,
        "osFamily": CustomerManagedFleetOperatingSystemFamilyType,
        "cpuArchitectureType": CpuArchitectureTypeType,
        "acceleratorTypes": NotRequired[Sequence[Literal["gpu"]]],
        "acceleratorCount": NotRequired[AcceleratorCountRangeTypeDef],
        "acceleratorTotalMemoryMiB": NotRequired[AcceleratorTotalMemoryMiBRangeTypeDef],
        "customAmounts": NotRequired[Sequence[FleetAmountCapabilityTypeDef]],
        "customAttributes": NotRequired[Sequence[FleetAttributeCapabilityUnionTypeDef]],
    },
)
ServiceManagedEc2InstanceCapabilitiesUnionTypeDef = Union[
    ServiceManagedEc2InstanceCapabilitiesTypeDef, ServiceManagedEc2InstanceCapabilitiesOutputTypeDef
]
GetSessionResponseTypeDef = TypedDict(
    "GetSessionResponseTypeDef",
    {
        "sessionId": str,
        "fleetId": str,
        "workerId": str,
        "startedAt": datetime,
        "log": LogConfigurationTypeDef,
        "lifecycleStatus": SessionLifecycleStatusType,
        "endedAt": datetime,
        "updatedAt": datetime,
        "updatedBy": str,
        "targetLifecycleStatus": Literal["ENDED"],
        "hostProperties": HostPropertiesResponseTypeDef,
        "workerLog": LogConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetWorkerResponseTypeDef = TypedDict(
    "GetWorkerResponseTypeDef",
    {
        "workerId": str,
        "farmId": str,
        "fleetId": str,
        "hostProperties": HostPropertiesResponseTypeDef,
        "status": WorkerStatusType,
        "log": LogConfigurationTypeDef,
        "createdAt": datetime,
        "createdBy": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
WorkerSearchSummaryTypeDef = TypedDict(
    "WorkerSearchSummaryTypeDef",
    {
        "fleetId": NotRequired[str],
        "workerId": NotRequired[str],
        "status": NotRequired[WorkerStatusType],
        "hostProperties": NotRequired[HostPropertiesResponseTypeDef],
        "createdBy": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "updatedBy": NotRequired[str],
        "updatedAt": NotRequired[datetime],
    },
)
WorkerSummaryTypeDef = TypedDict(
    "WorkerSummaryTypeDef",
    {
        "workerId": str,
        "farmId": str,
        "fleetId": str,
        "status": WorkerStatusType,
        "createdAt": datetime,
        "createdBy": str,
        "hostProperties": NotRequired[HostPropertiesResponseTypeDef],
        "log": NotRequired[LogConfigurationTypeDef],
        "updatedAt": NotRequired[datetime],
        "updatedBy": NotRequired[str],
    },
)
HostPropertiesRequestTypeDef = TypedDict(
    "HostPropertiesRequestTypeDef",
    {
        "ipAddresses": NotRequired[IpAddressesUnionTypeDef],
        "hostName": NotRequired[str],
    },
)
BatchGetJobEntityRequestRequestTypeDef = TypedDict(
    "BatchGetJobEntityRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "workerId": str,
        "identifiers": Sequence[JobEntityIdentifiersUnionTypeDef],
    },
)
CreateQueueRequestRequestTypeDef = TypedDict(
    "CreateQueueRequestRequestTypeDef",
    {
        "farmId": str,
        "displayName": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "defaultBudgetAction": NotRequired[DefaultQueueBudgetActionType],
        "jobAttachmentSettings": NotRequired[JobAttachmentSettingsTypeDef],
        "roleArn": NotRequired[str],
        "jobRunAsUser": NotRequired[JobRunAsUserTypeDef],
        "requiredFileSystemLocationNames": NotRequired[Sequence[str]],
        "allowedStorageProfileIds": NotRequired[Sequence[str]],
        "tags": NotRequired[Mapping[str, str]],
    },
)
GetQueueResponseTypeDef = TypedDict(
    "GetQueueResponseTypeDef",
    {
        "queueId": str,
        "displayName": str,
        "description": str,
        "farmId": str,
        "status": QueueStatusType,
        "defaultBudgetAction": DefaultQueueBudgetActionType,
        "blockedReason": QueueBlockedReasonType,
        "jobAttachmentSettings": JobAttachmentSettingsTypeDef,
        "roleArn": str,
        "requiredFileSystemLocationNames": List[str],
        "allowedStorageProfileIds": List[str],
        "jobRunAsUser": JobRunAsUserTypeDef,
        "createdAt": datetime,
        "createdBy": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
JobDetailsEntityTypeDef = TypedDict(
    "JobDetailsEntityTypeDef",
    {
        "jobId": str,
        "logGroupName": str,
        "schemaVersion": str,
        "jobAttachmentSettings": NotRequired[JobAttachmentSettingsTypeDef],
        "jobRunAsUser": NotRequired[JobRunAsUserTypeDef],
        "queueRoleArn": NotRequired[str],
        "parameters": NotRequired[Dict[str, JobParameterTypeDef]],
        "pathMappingRules": NotRequired[List[PathMappingRuleTypeDef]],
    },
)
UpdateQueueRequestRequestTypeDef = TypedDict(
    "UpdateQueueRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "clientToken": NotRequired[str],
        "displayName": NotRequired[str],
        "description": NotRequired[str],
        "defaultBudgetAction": NotRequired[DefaultQueueBudgetActionType],
        "jobAttachmentSettings": NotRequired[JobAttachmentSettingsTypeDef],
        "roleArn": NotRequired[str],
        "jobRunAsUser": NotRequired[JobRunAsUserTypeDef],
        "requiredFileSystemLocationNamesToAdd": NotRequired[Sequence[str]],
        "requiredFileSystemLocationNamesToRemove": NotRequired[Sequence[str]],
        "allowedStorageProfileIdsToAdd": NotRequired[Sequence[str]],
        "allowedStorageProfileIdsToRemove": NotRequired[Sequence[str]],
    },
)
AttachmentsTypeDef = TypedDict(
    "AttachmentsTypeDef",
    {
        "manifests": Sequence[ManifestPropertiesUnionTypeDef],
        "fileSystem": NotRequired[JobAttachmentsFileSystemType],
    },
)
StepSearchSummaryTypeDef = TypedDict(
    "StepSearchSummaryTypeDef",
    {
        "stepId": NotRequired[str],
        "jobId": NotRequired[str],
        "queueId": NotRequired[str],
        "name": NotRequired[str],
        "lifecycleStatus": NotRequired[StepLifecycleStatusType],
        "lifecycleStatusMessage": NotRequired[str],
        "taskRunStatus": NotRequired[TaskRunStatusType],
        "targetTaskRunStatus": NotRequired[StepTargetTaskRunStatusType],
        "taskRunStatusCounts": NotRequired[Dict[TaskRunStatusType, int]],
        "createdAt": NotRequired[datetime],
        "startedAt": NotRequired[datetime],
        "endedAt": NotRequired[datetime],
        "parameterSpace": NotRequired[ParameterSpaceTypeDef],
    },
)
SessionActionSummaryTypeDef = TypedDict(
    "SessionActionSummaryTypeDef",
    {
        "sessionActionId": str,
        "status": SessionActionStatusType,
        "definition": SessionActionDefinitionSummaryTypeDef,
        "startedAt": NotRequired[datetime],
        "endedAt": NotRequired[datetime],
        "workerUpdatedAt": NotRequired[datetime],
        "progressPercent": NotRequired[float],
    },
)
GetSessionsStatisticsAggregationResponseTypeDef = TypedDict(
    "GetSessionsStatisticsAggregationResponseTypeDef",
    {
        "statistics": List[StatisticsTypeDef],
        "nextToken": str,
        "status": SessionsStatisticsAggregationStatusType,
        "statusMessage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetStepResponseTypeDef = TypedDict(
    "GetStepResponseTypeDef",
    {
        "stepId": str,
        "name": str,
        "lifecycleStatus": StepLifecycleStatusType,
        "lifecycleStatusMessage": str,
        "taskRunStatus": TaskRunStatusType,
        "taskRunStatusCounts": Dict[TaskRunStatusType, int],
        "targetTaskRunStatus": StepTargetTaskRunStatusType,
        "createdAt": datetime,
        "createdBy": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "startedAt": datetime,
        "endedAt": datetime,
        "dependencyCounts": DependencyCountsTypeDef,
        "requiredCapabilities": StepRequiredCapabilitiesTypeDef,
        "parameterSpace": ParameterSpaceTypeDef,
        "description": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssignedSessionActionTypeDef = TypedDict(
    "AssignedSessionActionTypeDef",
    {
        "sessionActionId": str,
        "definition": AssignedSessionActionDefinitionTypeDef,
    },
)
GetSessionActionResponseTypeDef = TypedDict(
    "GetSessionActionResponseTypeDef",
    {
        "sessionActionId": str,
        "status": SessionActionStatusType,
        "startedAt": datetime,
        "endedAt": datetime,
        "workerUpdatedAt": datetime,
        "progressPercent": float,
        "sessionId": str,
        "processExitCode": int,
        "progressMessage": str,
        "definition": SessionActionDefinitionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchGroupedFilterExpressionsTypeDef = TypedDict(
    "SearchGroupedFilterExpressionsTypeDef",
    {
        "filters": Sequence[SearchFilterExpressionTypeDef],
        "operator": LogicalOperatorType,
    },
)
BudgetScheduleTypeDef = TypedDict(
    "BudgetScheduleTypeDef",
    {
        "fixed": NotRequired[FixedBudgetScheduleUnionTypeDef],
    },
)
FleetConfigurationOutputTypeDef = TypedDict(
    "FleetConfigurationOutputTypeDef",
    {
        "customerManaged": NotRequired[CustomerManagedFleetConfigurationOutputTypeDef],
        "serviceManagedEc2": NotRequired[ServiceManagedEc2FleetConfigurationOutputTypeDef],
    },
)
CustomerManagedWorkerCapabilitiesUnionTypeDef = Union[
    CustomerManagedWorkerCapabilitiesTypeDef, CustomerManagedWorkerCapabilitiesOutputTypeDef
]
ServiceManagedEc2FleetConfigurationTypeDef = TypedDict(
    "ServiceManagedEc2FleetConfigurationTypeDef",
    {
        "instanceCapabilities": ServiceManagedEc2InstanceCapabilitiesUnionTypeDef,
        "instanceMarketOptions": ServiceManagedEc2InstanceMarketOptionsTypeDef,
    },
)
SearchWorkersResponseTypeDef = TypedDict(
    "SearchWorkersResponseTypeDef",
    {
        "workers": List[WorkerSearchSummaryTypeDef],
        "nextItemOffset": int,
        "totalResults": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListWorkersResponseTypeDef = TypedDict(
    "ListWorkersResponseTypeDef",
    {
        "nextToken": str,
        "workers": List[WorkerSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWorkerRequestRequestTypeDef = TypedDict(
    "CreateWorkerRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "hostProperties": NotRequired[HostPropertiesRequestTypeDef],
        "clientToken": NotRequired[str],
    },
)
UpdateWorkerRequestRequestTypeDef = TypedDict(
    "UpdateWorkerRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "workerId": str,
        "status": NotRequired[UpdatedWorkerStatusType],
        "capabilities": NotRequired[WorkerCapabilitiesTypeDef],
        "hostProperties": NotRequired[HostPropertiesRequestTypeDef],
    },
)
JobEntityTypeDef = TypedDict(
    "JobEntityTypeDef",
    {
        "jobDetails": NotRequired[JobDetailsEntityTypeDef],
        "jobAttachmentDetails": NotRequired[JobAttachmentDetailsEntityTypeDef],
        "stepDetails": NotRequired[StepDetailsEntityTypeDef],
        "environmentDetails": NotRequired[EnvironmentDetailsEntityTypeDef],
    },
)
CreateJobRequestRequestTypeDef = TypedDict(
    "CreateJobRequestRequestTypeDef",
    {
        "farmId": str,
        "queueId": str,
        "priority": int,
        "clientToken": NotRequired[str],
        "template": NotRequired[str],
        "templateType": NotRequired[JobTemplateTypeType],
        "parameters": NotRequired[Mapping[str, JobParameterTypeDef]],
        "attachments": NotRequired[AttachmentsTypeDef],
        "storageProfileId": NotRequired[str],
        "targetTaskRunStatus": NotRequired[CreateJobTargetTaskRunStatusType],
        "maxFailedTasksCount": NotRequired[int],
        "maxRetriesPerTask": NotRequired[int],
        "sourceJobId": NotRequired[str],
    },
)
SearchStepsResponseTypeDef = TypedDict(
    "SearchStepsResponseTypeDef",
    {
        "steps": List[StepSearchSummaryTypeDef],
        "nextItemOffset": int,
        "totalResults": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSessionActionsResponseTypeDef = TypedDict(
    "ListSessionActionsResponseTypeDef",
    {
        "sessionActions": List[SessionActionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssignedSessionTypeDef = TypedDict(
    "AssignedSessionTypeDef",
    {
        "queueId": str,
        "jobId": str,
        "sessionActions": List[AssignedSessionActionTypeDef],
        "logConfiguration": LogConfigurationTypeDef,
    },
)
SearchJobsRequestRequestTypeDef = TypedDict(
    "SearchJobsRequestRequestTypeDef",
    {
        "farmId": str,
        "queueIds": Sequence[str],
        "itemOffset": int,
        "filterExpressions": NotRequired[SearchGroupedFilterExpressionsTypeDef],
        "sortExpressions": NotRequired[Sequence[SearchSortExpressionTypeDef]],
        "pageSize": NotRequired[int],
    },
)
SearchStepsRequestRequestTypeDef = TypedDict(
    "SearchStepsRequestRequestTypeDef",
    {
        "farmId": str,
        "queueIds": Sequence[str],
        "itemOffset": int,
        "jobId": NotRequired[str],
        "filterExpressions": NotRequired[SearchGroupedFilterExpressionsTypeDef],
        "sortExpressions": NotRequired[Sequence[SearchSortExpressionTypeDef]],
        "pageSize": NotRequired[int],
    },
)
SearchTasksRequestRequestTypeDef = TypedDict(
    "SearchTasksRequestRequestTypeDef",
    {
        "farmId": str,
        "queueIds": Sequence[str],
        "itemOffset": int,
        "jobId": NotRequired[str],
        "filterExpressions": NotRequired[SearchGroupedFilterExpressionsTypeDef],
        "sortExpressions": NotRequired[Sequence[SearchSortExpressionTypeDef]],
        "pageSize": NotRequired[int],
    },
)
SearchWorkersRequestRequestTypeDef = TypedDict(
    "SearchWorkersRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetIds": Sequence[str],
        "itemOffset": int,
        "filterExpressions": NotRequired[SearchGroupedFilterExpressionsTypeDef],
        "sortExpressions": NotRequired[Sequence[SearchSortExpressionTypeDef]],
        "pageSize": NotRequired[int],
    },
)
CreateBudgetRequestRequestTypeDef = TypedDict(
    "CreateBudgetRequestRequestTypeDef",
    {
        "farmId": str,
        "usageTrackingResource": UsageTrackingResourceTypeDef,
        "displayName": str,
        "approximateDollarLimit": float,
        "actions": Sequence[BudgetActionToAddTypeDef],
        "schedule": BudgetScheduleTypeDef,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
    },
)
UpdateBudgetRequestRequestTypeDef = TypedDict(
    "UpdateBudgetRequestRequestTypeDef",
    {
        "farmId": str,
        "budgetId": str,
        "clientToken": NotRequired[str],
        "displayName": NotRequired[str],
        "description": NotRequired[str],
        "status": NotRequired[BudgetStatusType],
        "approximateDollarLimit": NotRequired[float],
        "actionsToAdd": NotRequired[Sequence[BudgetActionToAddTypeDef]],
        "actionsToRemove": NotRequired[Sequence[BudgetActionToRemoveTypeDef]],
        "schedule": NotRequired[BudgetScheduleTypeDef],
    },
)
FleetSummaryTypeDef = TypedDict(
    "FleetSummaryTypeDef",
    {
        "fleetId": str,
        "farmId": str,
        "displayName": str,
        "status": FleetStatusType,
        "workerCount": int,
        "minWorkerCount": int,
        "maxWorkerCount": int,
        "configuration": FleetConfigurationOutputTypeDef,
        "createdAt": datetime,
        "createdBy": str,
        "autoScalingStatus": NotRequired[AutoScalingStatusType],
        "targetWorkerCount": NotRequired[int],
        "updatedAt": NotRequired[datetime],
        "updatedBy": NotRequired[str],
    },
)
GetFleetResponseTypeDef = TypedDict(
    "GetFleetResponseTypeDef",
    {
        "fleetId": str,
        "farmId": str,
        "displayName": str,
        "description": str,
        "status": FleetStatusType,
        "autoScalingStatus": AutoScalingStatusType,
        "targetWorkerCount": int,
        "workerCount": int,
        "minWorkerCount": int,
        "maxWorkerCount": int,
        "configuration": FleetConfigurationOutputTypeDef,
        "capabilities": FleetCapabilitiesTypeDef,
        "roleArn": str,
        "createdAt": datetime,
        "createdBy": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CustomerManagedFleetConfigurationTypeDef = TypedDict(
    "CustomerManagedFleetConfigurationTypeDef",
    {
        "mode": AutoScalingModeType,
        "workerCapabilities": CustomerManagedWorkerCapabilitiesUnionTypeDef,
        "storageProfileId": NotRequired[str],
    },
)
ServiceManagedEc2FleetConfigurationUnionTypeDef = Union[
    ServiceManagedEc2FleetConfigurationTypeDef, ServiceManagedEc2FleetConfigurationOutputTypeDef
]
BatchGetJobEntityResponseTypeDef = TypedDict(
    "BatchGetJobEntityResponseTypeDef",
    {
        "entities": List[JobEntityTypeDef],
        "errors": List[GetJobEntityErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateWorkerScheduleResponseTypeDef = TypedDict(
    "UpdateWorkerScheduleResponseTypeDef",
    {
        "assignedSessions": Dict[str, AssignedSessionTypeDef],
        "cancelSessionActions": Dict[str, List[str]],
        "desiredWorkerStatus": Literal["STOPPED"],
        "updateIntervalSeconds": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListFleetsResponseTypeDef = TypedDict(
    "ListFleetsResponseTypeDef",
    {
        "fleets": List[FleetSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CustomerManagedFleetConfigurationUnionTypeDef = Union[
    CustomerManagedFleetConfigurationTypeDef, CustomerManagedFleetConfigurationOutputTypeDef
]
FleetConfigurationTypeDef = TypedDict(
    "FleetConfigurationTypeDef",
    {
        "customerManaged": NotRequired[CustomerManagedFleetConfigurationUnionTypeDef],
        "serviceManagedEc2": NotRequired[ServiceManagedEc2FleetConfigurationUnionTypeDef],
    },
)
CreateFleetRequestRequestTypeDef = TypedDict(
    "CreateFleetRequestRequestTypeDef",
    {
        "farmId": str,
        "displayName": str,
        "roleArn": str,
        "maxWorkerCount": int,
        "configuration": FleetConfigurationTypeDef,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "minWorkerCount": NotRequired[int],
        "tags": NotRequired[Mapping[str, str]],
    },
)
UpdateFleetRequestRequestTypeDef = TypedDict(
    "UpdateFleetRequestRequestTypeDef",
    {
        "farmId": str,
        "fleetId": str,
        "clientToken": NotRequired[str],
        "displayName": NotRequired[str],
        "description": NotRequired[str],
        "roleArn": NotRequired[str],
        "minWorkerCount": NotRequired[int],
        "maxWorkerCount": NotRequired[int],
        "configuration": NotRequired[FleetConfigurationTypeDef],
    },
)
