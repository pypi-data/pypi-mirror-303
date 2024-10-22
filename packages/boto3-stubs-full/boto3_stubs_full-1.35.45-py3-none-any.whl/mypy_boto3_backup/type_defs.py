"""
Type annotations for backup service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backup/type_defs/)

Usage::

    ```python
    from mypy_boto3_backup.type_defs import AdvancedBackupSettingOutputTypeDef

    data: AdvancedBackupSettingOutputTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AggregationPeriodType,
    BackupJobStateType,
    BackupJobStatusType,
    BackupVaultEventType,
    CopyJobStateType,
    CopyJobStatusType,
    LegalHoldStatusType,
    RecoveryPointStatusType,
    RestoreDeletionStatusType,
    RestoreJobStateType,
    RestoreJobStatusType,
    RestoreTestingRecoveryPointSelectionAlgorithmType,
    RestoreTestingRecoveryPointTypeType,
    RestoreValidationStatusType,
    StorageClassType,
    VaultStateType,
    VaultTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AdvancedBackupSettingOutputTypeDef",
    "AdvancedBackupSettingTypeDef",
    "BackupJobSummaryTypeDef",
    "RecoveryPointCreatorTypeDef",
    "BackupPlanTemplatesListMemberTypeDef",
    "LifecycleTypeDef",
    "ConditionTypeDef",
    "BackupSelectionsListMemberTypeDef",
    "BackupVaultListMemberTypeDef",
    "CalculatedLifecycleTypeDef",
    "CancelLegalHoldInputRequestTypeDef",
    "ConditionParameterTypeDef",
    "ControlInputParameterTypeDef",
    "ControlScopeOutputTypeDef",
    "ControlScopeTypeDef",
    "CopyJobSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "CreateBackupVaultInputRequestTypeDef",
    "CreateLogicallyAirGappedBackupVaultInputRequestTypeDef",
    "ReportDeliveryChannelTypeDef",
    "ReportSettingTypeDef",
    "DateRangeOutputTypeDef",
    "TimestampTypeDef",
    "DeleteBackupPlanInputRequestTypeDef",
    "DeleteBackupSelectionInputRequestTypeDef",
    "DeleteBackupVaultAccessPolicyInputRequestTypeDef",
    "DeleteBackupVaultInputRequestTypeDef",
    "DeleteBackupVaultLockConfigurationInputRequestTypeDef",
    "DeleteBackupVaultNotificationsInputRequestTypeDef",
    "DeleteFrameworkInputRequestTypeDef",
    "DeleteRecoveryPointInputRequestTypeDef",
    "DeleteReportPlanInputRequestTypeDef",
    "DeleteRestoreTestingPlanInputRequestTypeDef",
    "DeleteRestoreTestingSelectionInputRequestTypeDef",
    "DescribeBackupJobInputRequestTypeDef",
    "DescribeBackupVaultInputRequestTypeDef",
    "DescribeCopyJobInputRequestTypeDef",
    "DescribeFrameworkInputRequestTypeDef",
    "DescribeProtectedResourceInputRequestTypeDef",
    "DescribeRecoveryPointInputRequestTypeDef",
    "DescribeReportJobInputRequestTypeDef",
    "DescribeReportPlanInputRequestTypeDef",
    "DescribeRestoreJobInputRequestTypeDef",
    "RestoreJobCreatorTypeDef",
    "DisassociateRecoveryPointFromParentInputRequestTypeDef",
    "DisassociateRecoveryPointInputRequestTypeDef",
    "ExportBackupPlanTemplateInputRequestTypeDef",
    "FrameworkTypeDef",
    "GetBackupPlanFromJSONInputRequestTypeDef",
    "GetBackupPlanFromTemplateInputRequestTypeDef",
    "GetBackupPlanInputRequestTypeDef",
    "GetBackupSelectionInputRequestTypeDef",
    "GetBackupVaultAccessPolicyInputRequestTypeDef",
    "GetBackupVaultNotificationsInputRequestTypeDef",
    "GetLegalHoldInputRequestTypeDef",
    "GetRecoveryPointRestoreMetadataInputRequestTypeDef",
    "GetRestoreJobMetadataInputRequestTypeDef",
    "GetRestoreTestingInferredMetadataInputRequestTypeDef",
    "GetRestoreTestingPlanInputRequestTypeDef",
    "GetRestoreTestingSelectionInputRequestTypeDef",
    "KeyValueTypeDef",
    "LegalHoldTypeDef",
    "ListBackupJobSummariesInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListBackupPlanTemplatesInputRequestTypeDef",
    "ListBackupPlanVersionsInputRequestTypeDef",
    "ListBackupPlansInputRequestTypeDef",
    "ListBackupSelectionsInputRequestTypeDef",
    "ListBackupVaultsInputRequestTypeDef",
    "ListCopyJobSummariesInputRequestTypeDef",
    "ListFrameworksInputRequestTypeDef",
    "ListLegalHoldsInputRequestTypeDef",
    "ListProtectedResourcesByBackupVaultInputRequestTypeDef",
    "ProtectedResourceTypeDef",
    "ListProtectedResourcesInputRequestTypeDef",
    "ListRecoveryPointsByLegalHoldInputRequestTypeDef",
    "RecoveryPointMemberTypeDef",
    "ListRecoveryPointsByResourceInputRequestTypeDef",
    "RecoveryPointByResourceTypeDef",
    "ListReportPlansInputRequestTypeDef",
    "ListRestoreJobSummariesInputRequestTypeDef",
    "RestoreJobSummaryTypeDef",
    "ListRestoreTestingPlansInputRequestTypeDef",
    "RestoreTestingPlanForListTypeDef",
    "ListRestoreTestingSelectionsInputRequestTypeDef",
    "RestoreTestingSelectionForListTypeDef",
    "ListTagsInputRequestTypeDef",
    "PutBackupVaultAccessPolicyInputRequestTypeDef",
    "PutBackupVaultLockConfigurationInputRequestTypeDef",
    "PutBackupVaultNotificationsInputRequestTypeDef",
    "PutRestoreValidationResultInputRequestTypeDef",
    "ReportDeliveryChannelOutputTypeDef",
    "ReportDestinationTypeDef",
    "ReportSettingOutputTypeDef",
    "RestoreTestingRecoveryPointSelectionOutputTypeDef",
    "RestoreTestingRecoveryPointSelectionTypeDef",
    "StartReportJobInputRequestTypeDef",
    "StartRestoreJobInputRequestTypeDef",
    "StopBackupJobInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateGlobalSettingsInputRequestTypeDef",
    "UpdateRegionSettingsInputRequestTypeDef",
    "BackupPlansListMemberTypeDef",
    "AdvancedBackupSettingUnionTypeDef",
    "BackupJobTypeDef",
    "CopyJobTypeDef",
    "CopyActionTypeDef",
    "StartBackupJobInputRequestTypeDef",
    "StartCopyJobInputRequestTypeDef",
    "UpdateRecoveryPointLifecycleInputRequestTypeDef",
    "RecoveryPointByBackupVaultTypeDef",
    "ConditionsOutputTypeDef",
    "ConditionsTypeDef",
    "FrameworkControlOutputTypeDef",
    "ControlScopeUnionTypeDef",
    "CreateBackupPlanOutputTypeDef",
    "CreateBackupSelectionOutputTypeDef",
    "CreateBackupVaultOutputTypeDef",
    "CreateFrameworkOutputTypeDef",
    "CreateLogicallyAirGappedBackupVaultOutputTypeDef",
    "CreateReportPlanOutputTypeDef",
    "CreateRestoreTestingPlanOutputTypeDef",
    "CreateRestoreTestingSelectionOutputTypeDef",
    "DeleteBackupPlanOutputTypeDef",
    "DescribeBackupJobOutputTypeDef",
    "DescribeBackupVaultOutputTypeDef",
    "DescribeGlobalSettingsOutputTypeDef",
    "DescribeProtectedResourceOutputTypeDef",
    "DescribeRecoveryPointOutputTypeDef",
    "DescribeRegionSettingsOutputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ExportBackupPlanTemplateOutputTypeDef",
    "GetBackupVaultAccessPolicyOutputTypeDef",
    "GetBackupVaultNotificationsOutputTypeDef",
    "GetRecoveryPointRestoreMetadataOutputTypeDef",
    "GetRestoreJobMetadataOutputTypeDef",
    "GetRestoreTestingInferredMetadataOutputTypeDef",
    "GetSupportedResourceTypesOutputTypeDef",
    "ListBackupJobSummariesOutputTypeDef",
    "ListBackupPlanTemplatesOutputTypeDef",
    "ListBackupSelectionsOutputTypeDef",
    "ListBackupVaultsOutputTypeDef",
    "ListCopyJobSummariesOutputTypeDef",
    "ListTagsOutputTypeDef",
    "StartBackupJobOutputTypeDef",
    "StartCopyJobOutputTypeDef",
    "StartReportJobOutputTypeDef",
    "StartRestoreJobOutputTypeDef",
    "UpdateBackupPlanOutputTypeDef",
    "UpdateFrameworkOutputTypeDef",
    "UpdateRecoveryPointLifecycleOutputTypeDef",
    "UpdateReportPlanOutputTypeDef",
    "UpdateRestoreTestingPlanOutputTypeDef",
    "UpdateRestoreTestingSelectionOutputTypeDef",
    "CreateReportPlanInputRequestTypeDef",
    "UpdateReportPlanInputRequestTypeDef",
    "RecoveryPointSelectionOutputTypeDef",
    "DateRangeTypeDef",
    "ListBackupJobsInputRequestTypeDef",
    "ListCopyJobsInputRequestTypeDef",
    "ListRecoveryPointsByBackupVaultInputRequestTypeDef",
    "ListReportJobsInputRequestTypeDef",
    "ListRestoreJobsByProtectedResourceInputRequestTypeDef",
    "ListRestoreJobsInputRequestTypeDef",
    "DescribeRestoreJobOutputTypeDef",
    "RestoreJobsListMemberTypeDef",
    "ListFrameworksOutputTypeDef",
    "ProtectedResourceConditionsOutputTypeDef",
    "ProtectedResourceConditionsTypeDef",
    "ListLegalHoldsOutputTypeDef",
    "ListBackupJobsInputListBackupJobsPaginateTypeDef",
    "ListBackupPlanTemplatesInputListBackupPlanTemplatesPaginateTypeDef",
    "ListBackupPlanVersionsInputListBackupPlanVersionsPaginateTypeDef",
    "ListBackupPlansInputListBackupPlansPaginateTypeDef",
    "ListBackupSelectionsInputListBackupSelectionsPaginateTypeDef",
    "ListBackupVaultsInputListBackupVaultsPaginateTypeDef",
    "ListCopyJobsInputListCopyJobsPaginateTypeDef",
    "ListLegalHoldsInputListLegalHoldsPaginateTypeDef",
    "ListProtectedResourcesByBackupVaultInputListProtectedResourcesByBackupVaultPaginateTypeDef",
    "ListProtectedResourcesInputListProtectedResourcesPaginateTypeDef",
    "ListRecoveryPointsByBackupVaultInputListRecoveryPointsByBackupVaultPaginateTypeDef",
    "ListRecoveryPointsByLegalHoldInputListRecoveryPointsByLegalHoldPaginateTypeDef",
    "ListRecoveryPointsByResourceInputListRecoveryPointsByResourcePaginateTypeDef",
    "ListRestoreJobsByProtectedResourceInputListRestoreJobsByProtectedResourcePaginateTypeDef",
    "ListRestoreJobsInputListRestoreJobsPaginateTypeDef",
    "ListRestoreTestingPlansInputListRestoreTestingPlansPaginateTypeDef",
    "ListRestoreTestingSelectionsInputListRestoreTestingSelectionsPaginateTypeDef",
    "ListProtectedResourcesByBackupVaultOutputTypeDef",
    "ListProtectedResourcesOutputTypeDef",
    "ListRecoveryPointsByLegalHoldOutputTypeDef",
    "ListRecoveryPointsByResourceOutputTypeDef",
    "ListRestoreJobSummariesOutputTypeDef",
    "ListRestoreTestingPlansOutputTypeDef",
    "ListRestoreTestingSelectionsOutputTypeDef",
    "ReportJobTypeDef",
    "ReportPlanTypeDef",
    "RestoreTestingPlanForGetTypeDef",
    "RestoreTestingRecoveryPointSelectionUnionTypeDef",
    "ListBackupPlanVersionsOutputTypeDef",
    "ListBackupPlansOutputTypeDef",
    "ListBackupJobsOutputTypeDef",
    "DescribeCopyJobOutputTypeDef",
    "ListCopyJobsOutputTypeDef",
    "BackupRuleInputTypeDef",
    "BackupRuleTypeDef",
    "ListRecoveryPointsByBackupVaultOutputTypeDef",
    "BackupSelectionOutputTypeDef",
    "ConditionsUnionTypeDef",
    "DescribeFrameworkOutputTypeDef",
    "FrameworkControlTypeDef",
    "CreateLegalHoldOutputTypeDef",
    "GetLegalHoldOutputTypeDef",
    "DateRangeUnionTypeDef",
    "ListRestoreJobsByProtectedResourceOutputTypeDef",
    "ListRestoreJobsOutputTypeDef",
    "RestoreTestingSelectionForGetTypeDef",
    "ProtectedResourceConditionsUnionTypeDef",
    "DescribeReportJobOutputTypeDef",
    "ListReportJobsOutputTypeDef",
    "DescribeReportPlanOutputTypeDef",
    "ListReportPlansOutputTypeDef",
    "GetRestoreTestingPlanOutputTypeDef",
    "RestoreTestingPlanForCreateTypeDef",
    "RestoreTestingPlanForUpdateTypeDef",
    "BackupPlanInputTypeDef",
    "BackupPlanTypeDef",
    "GetBackupSelectionOutputTypeDef",
    "BackupSelectionTypeDef",
    "FrameworkControlUnionTypeDef",
    "UpdateFrameworkInputRequestTypeDef",
    "RecoveryPointSelectionTypeDef",
    "GetRestoreTestingSelectionOutputTypeDef",
    "RestoreTestingSelectionForCreateTypeDef",
    "RestoreTestingSelectionForUpdateTypeDef",
    "CreateRestoreTestingPlanInputRequestTypeDef",
    "UpdateRestoreTestingPlanInputRequestTypeDef",
    "CreateBackupPlanInputRequestTypeDef",
    "UpdateBackupPlanInputRequestTypeDef",
    "GetBackupPlanFromJSONOutputTypeDef",
    "GetBackupPlanFromTemplateOutputTypeDef",
    "GetBackupPlanOutputTypeDef",
    "CreateBackupSelectionInputRequestTypeDef",
    "CreateFrameworkInputRequestTypeDef",
    "CreateLegalHoldInputRequestTypeDef",
    "CreateRestoreTestingSelectionInputRequestTypeDef",
    "UpdateRestoreTestingSelectionInputRequestTypeDef",
)

AdvancedBackupSettingOutputTypeDef = TypedDict(
    "AdvancedBackupSettingOutputTypeDef",
    {
        "ResourceType": NotRequired[str],
        "BackupOptions": NotRequired[Dict[str, str]],
    },
)
AdvancedBackupSettingTypeDef = TypedDict(
    "AdvancedBackupSettingTypeDef",
    {
        "ResourceType": NotRequired[str],
        "BackupOptions": NotRequired[Mapping[str, str]],
    },
)
BackupJobSummaryTypeDef = TypedDict(
    "BackupJobSummaryTypeDef",
    {
        "Region": NotRequired[str],
        "AccountId": NotRequired[str],
        "State": NotRequired[BackupJobStatusType],
        "ResourceType": NotRequired[str],
        "MessageCategory": NotRequired[str],
        "Count": NotRequired[int],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
    },
)
RecoveryPointCreatorTypeDef = TypedDict(
    "RecoveryPointCreatorTypeDef",
    {
        "BackupPlanId": NotRequired[str],
        "BackupPlanArn": NotRequired[str],
        "BackupPlanVersion": NotRequired[str],
        "BackupRuleId": NotRequired[str],
    },
)
BackupPlanTemplatesListMemberTypeDef = TypedDict(
    "BackupPlanTemplatesListMemberTypeDef",
    {
        "BackupPlanTemplateId": NotRequired[str],
        "BackupPlanTemplateName": NotRequired[str],
    },
)
LifecycleTypeDef = TypedDict(
    "LifecycleTypeDef",
    {
        "MoveToColdStorageAfterDays": NotRequired[int],
        "DeleteAfterDays": NotRequired[int],
        "OptInToArchiveForSupportedResources": NotRequired[bool],
    },
)
ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "ConditionType": Literal["STRINGEQUALS"],
        "ConditionKey": str,
        "ConditionValue": str,
    },
)
BackupSelectionsListMemberTypeDef = TypedDict(
    "BackupSelectionsListMemberTypeDef",
    {
        "SelectionId": NotRequired[str],
        "SelectionName": NotRequired[str],
        "BackupPlanId": NotRequired[str],
        "CreationDate": NotRequired[datetime],
        "CreatorRequestId": NotRequired[str],
        "IamRoleArn": NotRequired[str],
    },
)
BackupVaultListMemberTypeDef = TypedDict(
    "BackupVaultListMemberTypeDef",
    {
        "BackupVaultName": NotRequired[str],
        "BackupVaultArn": NotRequired[str],
        "VaultType": NotRequired[VaultTypeType],
        "VaultState": NotRequired[VaultStateType],
        "CreationDate": NotRequired[datetime],
        "EncryptionKeyArn": NotRequired[str],
        "CreatorRequestId": NotRequired[str],
        "NumberOfRecoveryPoints": NotRequired[int],
        "Locked": NotRequired[bool],
        "MinRetentionDays": NotRequired[int],
        "MaxRetentionDays": NotRequired[int],
        "LockDate": NotRequired[datetime],
    },
)
CalculatedLifecycleTypeDef = TypedDict(
    "CalculatedLifecycleTypeDef",
    {
        "MoveToColdStorageAt": NotRequired[datetime],
        "DeleteAt": NotRequired[datetime],
    },
)
CancelLegalHoldInputRequestTypeDef = TypedDict(
    "CancelLegalHoldInputRequestTypeDef",
    {
        "LegalHoldId": str,
        "CancelDescription": str,
        "RetainRecordInDays": NotRequired[int],
    },
)
ConditionParameterTypeDef = TypedDict(
    "ConditionParameterTypeDef",
    {
        "ConditionKey": NotRequired[str],
        "ConditionValue": NotRequired[str],
    },
)
ControlInputParameterTypeDef = TypedDict(
    "ControlInputParameterTypeDef",
    {
        "ParameterName": NotRequired[str],
        "ParameterValue": NotRequired[str],
    },
)
ControlScopeOutputTypeDef = TypedDict(
    "ControlScopeOutputTypeDef",
    {
        "ComplianceResourceIds": NotRequired[List[str]],
        "ComplianceResourceTypes": NotRequired[List[str]],
        "Tags": NotRequired[Dict[str, str]],
    },
)
ControlScopeTypeDef = TypedDict(
    "ControlScopeTypeDef",
    {
        "ComplianceResourceIds": NotRequired[Sequence[str]],
        "ComplianceResourceTypes": NotRequired[Sequence[str]],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CopyJobSummaryTypeDef = TypedDict(
    "CopyJobSummaryTypeDef",
    {
        "Region": NotRequired[str],
        "AccountId": NotRequired[str],
        "State": NotRequired[CopyJobStatusType],
        "ResourceType": NotRequired[str],
        "MessageCategory": NotRequired[str],
        "Count": NotRequired[int],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
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
CreateBackupVaultInputRequestTypeDef = TypedDict(
    "CreateBackupVaultInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultTags": NotRequired[Mapping[str, str]],
        "EncryptionKeyArn": NotRequired[str],
        "CreatorRequestId": NotRequired[str],
    },
)
CreateLogicallyAirGappedBackupVaultInputRequestTypeDef = TypedDict(
    "CreateLogicallyAirGappedBackupVaultInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "MinRetentionDays": int,
        "MaxRetentionDays": int,
        "BackupVaultTags": NotRequired[Mapping[str, str]],
        "CreatorRequestId": NotRequired[str],
    },
)
ReportDeliveryChannelTypeDef = TypedDict(
    "ReportDeliveryChannelTypeDef",
    {
        "S3BucketName": str,
        "S3KeyPrefix": NotRequired[str],
        "Formats": NotRequired[Sequence[str]],
    },
)
ReportSettingTypeDef = TypedDict(
    "ReportSettingTypeDef",
    {
        "ReportTemplate": str,
        "FrameworkArns": NotRequired[Sequence[str]],
        "NumberOfFrameworks": NotRequired[int],
        "Accounts": NotRequired[Sequence[str]],
        "OrganizationUnits": NotRequired[Sequence[str]],
        "Regions": NotRequired[Sequence[str]],
    },
)
DateRangeOutputTypeDef = TypedDict(
    "DateRangeOutputTypeDef",
    {
        "FromDate": datetime,
        "ToDate": datetime,
    },
)
TimestampTypeDef = Union[datetime, str]
DeleteBackupPlanInputRequestTypeDef = TypedDict(
    "DeleteBackupPlanInputRequestTypeDef",
    {
        "BackupPlanId": str,
    },
)
DeleteBackupSelectionInputRequestTypeDef = TypedDict(
    "DeleteBackupSelectionInputRequestTypeDef",
    {
        "BackupPlanId": str,
        "SelectionId": str,
    },
)
DeleteBackupVaultAccessPolicyInputRequestTypeDef = TypedDict(
    "DeleteBackupVaultAccessPolicyInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)
DeleteBackupVaultInputRequestTypeDef = TypedDict(
    "DeleteBackupVaultInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)
DeleteBackupVaultLockConfigurationInputRequestTypeDef = TypedDict(
    "DeleteBackupVaultLockConfigurationInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)
DeleteBackupVaultNotificationsInputRequestTypeDef = TypedDict(
    "DeleteBackupVaultNotificationsInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)
DeleteFrameworkInputRequestTypeDef = TypedDict(
    "DeleteFrameworkInputRequestTypeDef",
    {
        "FrameworkName": str,
    },
)
DeleteRecoveryPointInputRequestTypeDef = TypedDict(
    "DeleteRecoveryPointInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "RecoveryPointArn": str,
    },
)
DeleteReportPlanInputRequestTypeDef = TypedDict(
    "DeleteReportPlanInputRequestTypeDef",
    {
        "ReportPlanName": str,
    },
)
DeleteRestoreTestingPlanInputRequestTypeDef = TypedDict(
    "DeleteRestoreTestingPlanInputRequestTypeDef",
    {
        "RestoreTestingPlanName": str,
    },
)
DeleteRestoreTestingSelectionInputRequestTypeDef = TypedDict(
    "DeleteRestoreTestingSelectionInputRequestTypeDef",
    {
        "RestoreTestingPlanName": str,
        "RestoreTestingSelectionName": str,
    },
)
DescribeBackupJobInputRequestTypeDef = TypedDict(
    "DescribeBackupJobInputRequestTypeDef",
    {
        "BackupJobId": str,
    },
)
DescribeBackupVaultInputRequestTypeDef = TypedDict(
    "DescribeBackupVaultInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultAccountId": NotRequired[str],
    },
)
DescribeCopyJobInputRequestTypeDef = TypedDict(
    "DescribeCopyJobInputRequestTypeDef",
    {
        "CopyJobId": str,
    },
)
DescribeFrameworkInputRequestTypeDef = TypedDict(
    "DescribeFrameworkInputRequestTypeDef",
    {
        "FrameworkName": str,
    },
)
DescribeProtectedResourceInputRequestTypeDef = TypedDict(
    "DescribeProtectedResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
DescribeRecoveryPointInputRequestTypeDef = TypedDict(
    "DescribeRecoveryPointInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "RecoveryPointArn": str,
        "BackupVaultAccountId": NotRequired[str],
    },
)
DescribeReportJobInputRequestTypeDef = TypedDict(
    "DescribeReportJobInputRequestTypeDef",
    {
        "ReportJobId": str,
    },
)
DescribeReportPlanInputRequestTypeDef = TypedDict(
    "DescribeReportPlanInputRequestTypeDef",
    {
        "ReportPlanName": str,
    },
)
DescribeRestoreJobInputRequestTypeDef = TypedDict(
    "DescribeRestoreJobInputRequestTypeDef",
    {
        "RestoreJobId": str,
    },
)
RestoreJobCreatorTypeDef = TypedDict(
    "RestoreJobCreatorTypeDef",
    {
        "RestoreTestingPlanArn": NotRequired[str],
    },
)
DisassociateRecoveryPointFromParentInputRequestTypeDef = TypedDict(
    "DisassociateRecoveryPointFromParentInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "RecoveryPointArn": str,
    },
)
DisassociateRecoveryPointInputRequestTypeDef = TypedDict(
    "DisassociateRecoveryPointInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "RecoveryPointArn": str,
    },
)
ExportBackupPlanTemplateInputRequestTypeDef = TypedDict(
    "ExportBackupPlanTemplateInputRequestTypeDef",
    {
        "BackupPlanId": str,
    },
)
FrameworkTypeDef = TypedDict(
    "FrameworkTypeDef",
    {
        "FrameworkName": NotRequired[str],
        "FrameworkArn": NotRequired[str],
        "FrameworkDescription": NotRequired[str],
        "NumberOfControls": NotRequired[int],
        "CreationTime": NotRequired[datetime],
        "DeploymentStatus": NotRequired[str],
    },
)
GetBackupPlanFromJSONInputRequestTypeDef = TypedDict(
    "GetBackupPlanFromJSONInputRequestTypeDef",
    {
        "BackupPlanTemplateJson": str,
    },
)
GetBackupPlanFromTemplateInputRequestTypeDef = TypedDict(
    "GetBackupPlanFromTemplateInputRequestTypeDef",
    {
        "BackupPlanTemplateId": str,
    },
)
GetBackupPlanInputRequestTypeDef = TypedDict(
    "GetBackupPlanInputRequestTypeDef",
    {
        "BackupPlanId": str,
        "VersionId": NotRequired[str],
    },
)
GetBackupSelectionInputRequestTypeDef = TypedDict(
    "GetBackupSelectionInputRequestTypeDef",
    {
        "BackupPlanId": str,
        "SelectionId": str,
    },
)
GetBackupVaultAccessPolicyInputRequestTypeDef = TypedDict(
    "GetBackupVaultAccessPolicyInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)
GetBackupVaultNotificationsInputRequestTypeDef = TypedDict(
    "GetBackupVaultNotificationsInputRequestTypeDef",
    {
        "BackupVaultName": str,
    },
)
GetLegalHoldInputRequestTypeDef = TypedDict(
    "GetLegalHoldInputRequestTypeDef",
    {
        "LegalHoldId": str,
    },
)
GetRecoveryPointRestoreMetadataInputRequestTypeDef = TypedDict(
    "GetRecoveryPointRestoreMetadataInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "RecoveryPointArn": str,
        "BackupVaultAccountId": NotRequired[str],
    },
)
GetRestoreJobMetadataInputRequestTypeDef = TypedDict(
    "GetRestoreJobMetadataInputRequestTypeDef",
    {
        "RestoreJobId": str,
    },
)
GetRestoreTestingInferredMetadataInputRequestTypeDef = TypedDict(
    "GetRestoreTestingInferredMetadataInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "RecoveryPointArn": str,
        "BackupVaultAccountId": NotRequired[str],
    },
)
GetRestoreTestingPlanInputRequestTypeDef = TypedDict(
    "GetRestoreTestingPlanInputRequestTypeDef",
    {
        "RestoreTestingPlanName": str,
    },
)
GetRestoreTestingSelectionInputRequestTypeDef = TypedDict(
    "GetRestoreTestingSelectionInputRequestTypeDef",
    {
        "RestoreTestingPlanName": str,
        "RestoreTestingSelectionName": str,
    },
)
KeyValueTypeDef = TypedDict(
    "KeyValueTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
LegalHoldTypeDef = TypedDict(
    "LegalHoldTypeDef",
    {
        "Title": NotRequired[str],
        "Status": NotRequired[LegalHoldStatusType],
        "Description": NotRequired[str],
        "LegalHoldId": NotRequired[str],
        "LegalHoldArn": NotRequired[str],
        "CreationDate": NotRequired[datetime],
        "CancellationDate": NotRequired[datetime],
    },
)
ListBackupJobSummariesInputRequestTypeDef = TypedDict(
    "ListBackupJobSummariesInputRequestTypeDef",
    {
        "AccountId": NotRequired[str],
        "State": NotRequired[BackupJobStatusType],
        "ResourceType": NotRequired[str],
        "MessageCategory": NotRequired[str],
        "AggregationPeriod": NotRequired[AggregationPeriodType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
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
ListBackupPlanTemplatesInputRequestTypeDef = TypedDict(
    "ListBackupPlanTemplatesInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListBackupPlanVersionsInputRequestTypeDef = TypedDict(
    "ListBackupPlanVersionsInputRequestTypeDef",
    {
        "BackupPlanId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListBackupPlansInputRequestTypeDef = TypedDict(
    "ListBackupPlansInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "IncludeDeleted": NotRequired[bool],
    },
)
ListBackupSelectionsInputRequestTypeDef = TypedDict(
    "ListBackupSelectionsInputRequestTypeDef",
    {
        "BackupPlanId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListBackupVaultsInputRequestTypeDef = TypedDict(
    "ListBackupVaultsInputRequestTypeDef",
    {
        "ByVaultType": NotRequired[VaultTypeType],
        "ByShared": NotRequired[bool],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListCopyJobSummariesInputRequestTypeDef = TypedDict(
    "ListCopyJobSummariesInputRequestTypeDef",
    {
        "AccountId": NotRequired[str],
        "State": NotRequired[CopyJobStatusType],
        "ResourceType": NotRequired[str],
        "MessageCategory": NotRequired[str],
        "AggregationPeriod": NotRequired[AggregationPeriodType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListFrameworksInputRequestTypeDef = TypedDict(
    "ListFrameworksInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListLegalHoldsInputRequestTypeDef = TypedDict(
    "ListLegalHoldsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListProtectedResourcesByBackupVaultInputRequestTypeDef = TypedDict(
    "ListProtectedResourcesByBackupVaultInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultAccountId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ProtectedResourceTypeDef = TypedDict(
    "ProtectedResourceTypeDef",
    {
        "ResourceArn": NotRequired[str],
        "ResourceType": NotRequired[str],
        "LastBackupTime": NotRequired[datetime],
        "ResourceName": NotRequired[str],
        "LastBackupVaultArn": NotRequired[str],
        "LastRecoveryPointArn": NotRequired[str],
    },
)
ListProtectedResourcesInputRequestTypeDef = TypedDict(
    "ListProtectedResourcesInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListRecoveryPointsByLegalHoldInputRequestTypeDef = TypedDict(
    "ListRecoveryPointsByLegalHoldInputRequestTypeDef",
    {
        "LegalHoldId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
RecoveryPointMemberTypeDef = TypedDict(
    "RecoveryPointMemberTypeDef",
    {
        "RecoveryPointArn": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "ResourceType": NotRequired[str],
        "BackupVaultName": NotRequired[str],
    },
)
ListRecoveryPointsByResourceInputRequestTypeDef = TypedDict(
    "ListRecoveryPointsByResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ManagedByAWSBackupOnly": NotRequired[bool],
    },
)
RecoveryPointByResourceTypeDef = TypedDict(
    "RecoveryPointByResourceTypeDef",
    {
        "RecoveryPointArn": NotRequired[str],
        "CreationDate": NotRequired[datetime],
        "Status": NotRequired[RecoveryPointStatusType],
        "StatusMessage": NotRequired[str],
        "EncryptionKeyArn": NotRequired[str],
        "BackupSizeBytes": NotRequired[int],
        "BackupVaultName": NotRequired[str],
        "IsParent": NotRequired[bool],
        "ParentRecoveryPointArn": NotRequired[str],
        "ResourceName": NotRequired[str],
        "VaultType": NotRequired[VaultTypeType],
    },
)
ListReportPlansInputRequestTypeDef = TypedDict(
    "ListReportPlansInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListRestoreJobSummariesInputRequestTypeDef = TypedDict(
    "ListRestoreJobSummariesInputRequestTypeDef",
    {
        "AccountId": NotRequired[str],
        "State": NotRequired[RestoreJobStateType],
        "ResourceType": NotRequired[str],
        "AggregationPeriod": NotRequired[AggregationPeriodType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
RestoreJobSummaryTypeDef = TypedDict(
    "RestoreJobSummaryTypeDef",
    {
        "Region": NotRequired[str],
        "AccountId": NotRequired[str],
        "State": NotRequired[RestoreJobStateType],
        "ResourceType": NotRequired[str],
        "Count": NotRequired[int],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
    },
)
ListRestoreTestingPlansInputRequestTypeDef = TypedDict(
    "ListRestoreTestingPlansInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
RestoreTestingPlanForListTypeDef = TypedDict(
    "RestoreTestingPlanForListTypeDef",
    {
        "CreationTime": datetime,
        "RestoreTestingPlanArn": str,
        "RestoreTestingPlanName": str,
        "ScheduleExpression": str,
        "LastExecutionTime": NotRequired[datetime],
        "LastUpdateTime": NotRequired[datetime],
        "ScheduleExpressionTimezone": NotRequired[str],
        "StartWindowHours": NotRequired[int],
    },
)
ListRestoreTestingSelectionsInputRequestTypeDef = TypedDict(
    "ListRestoreTestingSelectionsInputRequestTypeDef",
    {
        "RestoreTestingPlanName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
RestoreTestingSelectionForListTypeDef = TypedDict(
    "RestoreTestingSelectionForListTypeDef",
    {
        "CreationTime": datetime,
        "IamRoleArn": str,
        "ProtectedResourceType": str,
        "RestoreTestingPlanName": str,
        "RestoreTestingSelectionName": str,
        "ValidationWindowHours": NotRequired[int],
    },
)
ListTagsInputRequestTypeDef = TypedDict(
    "ListTagsInputRequestTypeDef",
    {
        "ResourceArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
PutBackupVaultAccessPolicyInputRequestTypeDef = TypedDict(
    "PutBackupVaultAccessPolicyInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "Policy": NotRequired[str],
    },
)
PutBackupVaultLockConfigurationInputRequestTypeDef = TypedDict(
    "PutBackupVaultLockConfigurationInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "MinRetentionDays": NotRequired[int],
        "MaxRetentionDays": NotRequired[int],
        "ChangeableForDays": NotRequired[int],
    },
)
PutBackupVaultNotificationsInputRequestTypeDef = TypedDict(
    "PutBackupVaultNotificationsInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "SNSTopicArn": str,
        "BackupVaultEvents": Sequence[BackupVaultEventType],
    },
)
PutRestoreValidationResultInputRequestTypeDef = TypedDict(
    "PutRestoreValidationResultInputRequestTypeDef",
    {
        "RestoreJobId": str,
        "ValidationStatus": RestoreValidationStatusType,
        "ValidationStatusMessage": NotRequired[str],
    },
)
ReportDeliveryChannelOutputTypeDef = TypedDict(
    "ReportDeliveryChannelOutputTypeDef",
    {
        "S3BucketName": str,
        "S3KeyPrefix": NotRequired[str],
        "Formats": NotRequired[List[str]],
    },
)
ReportDestinationTypeDef = TypedDict(
    "ReportDestinationTypeDef",
    {
        "S3BucketName": NotRequired[str],
        "S3Keys": NotRequired[List[str]],
    },
)
ReportSettingOutputTypeDef = TypedDict(
    "ReportSettingOutputTypeDef",
    {
        "ReportTemplate": str,
        "FrameworkArns": NotRequired[List[str]],
        "NumberOfFrameworks": NotRequired[int],
        "Accounts": NotRequired[List[str]],
        "OrganizationUnits": NotRequired[List[str]],
        "Regions": NotRequired[List[str]],
    },
)
RestoreTestingRecoveryPointSelectionOutputTypeDef = TypedDict(
    "RestoreTestingRecoveryPointSelectionOutputTypeDef",
    {
        "Algorithm": NotRequired[RestoreTestingRecoveryPointSelectionAlgorithmType],
        "ExcludeVaults": NotRequired[List[str]],
        "IncludeVaults": NotRequired[List[str]],
        "RecoveryPointTypes": NotRequired[List[RestoreTestingRecoveryPointTypeType]],
        "SelectionWindowDays": NotRequired[int],
    },
)
RestoreTestingRecoveryPointSelectionTypeDef = TypedDict(
    "RestoreTestingRecoveryPointSelectionTypeDef",
    {
        "Algorithm": NotRequired[RestoreTestingRecoveryPointSelectionAlgorithmType],
        "ExcludeVaults": NotRequired[Sequence[str]],
        "IncludeVaults": NotRequired[Sequence[str]],
        "RecoveryPointTypes": NotRequired[Sequence[RestoreTestingRecoveryPointTypeType]],
        "SelectionWindowDays": NotRequired[int],
    },
)
StartReportJobInputRequestTypeDef = TypedDict(
    "StartReportJobInputRequestTypeDef",
    {
        "ReportPlanName": str,
        "IdempotencyToken": NotRequired[str],
    },
)
StartRestoreJobInputRequestTypeDef = TypedDict(
    "StartRestoreJobInputRequestTypeDef",
    {
        "RecoveryPointArn": str,
        "Metadata": Mapping[str, str],
        "IamRoleArn": NotRequired[str],
        "IdempotencyToken": NotRequired[str],
        "ResourceType": NotRequired[str],
        "CopySourceTagsToRestoredResource": NotRequired[bool],
    },
)
StopBackupJobInputRequestTypeDef = TypedDict(
    "StopBackupJobInputRequestTypeDef",
    {
        "BackupJobId": str,
    },
)
TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeyList": Sequence[str],
    },
)
UpdateGlobalSettingsInputRequestTypeDef = TypedDict(
    "UpdateGlobalSettingsInputRequestTypeDef",
    {
        "GlobalSettings": NotRequired[Mapping[str, str]],
    },
)
UpdateRegionSettingsInputRequestTypeDef = TypedDict(
    "UpdateRegionSettingsInputRequestTypeDef",
    {
        "ResourceTypeOptInPreference": NotRequired[Mapping[str, bool]],
        "ResourceTypeManagementPreference": NotRequired[Mapping[str, bool]],
    },
)
BackupPlansListMemberTypeDef = TypedDict(
    "BackupPlansListMemberTypeDef",
    {
        "BackupPlanArn": NotRequired[str],
        "BackupPlanId": NotRequired[str],
        "CreationDate": NotRequired[datetime],
        "DeletionDate": NotRequired[datetime],
        "VersionId": NotRequired[str],
        "BackupPlanName": NotRequired[str],
        "CreatorRequestId": NotRequired[str],
        "LastExecutionDate": NotRequired[datetime],
        "AdvancedBackupSettings": NotRequired[List[AdvancedBackupSettingOutputTypeDef]],
    },
)
AdvancedBackupSettingUnionTypeDef = Union[
    AdvancedBackupSettingTypeDef, AdvancedBackupSettingOutputTypeDef
]
BackupJobTypeDef = TypedDict(
    "BackupJobTypeDef",
    {
        "AccountId": NotRequired[str],
        "BackupJobId": NotRequired[str],
        "BackupVaultName": NotRequired[str],
        "BackupVaultArn": NotRequired[str],
        "RecoveryPointArn": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "CreationDate": NotRequired[datetime],
        "CompletionDate": NotRequired[datetime],
        "State": NotRequired[BackupJobStateType],
        "StatusMessage": NotRequired[str],
        "PercentDone": NotRequired[str],
        "BackupSizeInBytes": NotRequired[int],
        "IamRoleArn": NotRequired[str],
        "CreatedBy": NotRequired[RecoveryPointCreatorTypeDef],
        "ExpectedCompletionDate": NotRequired[datetime],
        "StartBy": NotRequired[datetime],
        "ResourceType": NotRequired[str],
        "BytesTransferred": NotRequired[int],
        "BackupOptions": NotRequired[Dict[str, str]],
        "BackupType": NotRequired[str],
        "ParentJobId": NotRequired[str],
        "IsParent": NotRequired[bool],
        "ResourceName": NotRequired[str],
        "InitiationDate": NotRequired[datetime],
        "MessageCategory": NotRequired[str],
    },
)
CopyJobTypeDef = TypedDict(
    "CopyJobTypeDef",
    {
        "AccountId": NotRequired[str],
        "CopyJobId": NotRequired[str],
        "SourceBackupVaultArn": NotRequired[str],
        "SourceRecoveryPointArn": NotRequired[str],
        "DestinationBackupVaultArn": NotRequired[str],
        "DestinationRecoveryPointArn": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "CreationDate": NotRequired[datetime],
        "CompletionDate": NotRequired[datetime],
        "State": NotRequired[CopyJobStateType],
        "StatusMessage": NotRequired[str],
        "BackupSizeInBytes": NotRequired[int],
        "IamRoleArn": NotRequired[str],
        "CreatedBy": NotRequired[RecoveryPointCreatorTypeDef],
        "ResourceType": NotRequired[str],
        "ParentJobId": NotRequired[str],
        "IsParent": NotRequired[bool],
        "CompositeMemberIdentifier": NotRequired[str],
        "NumberOfChildJobs": NotRequired[int],
        "ChildJobsInState": NotRequired[Dict[CopyJobStateType, int]],
        "ResourceName": NotRequired[str],
        "MessageCategory": NotRequired[str],
    },
)
CopyActionTypeDef = TypedDict(
    "CopyActionTypeDef",
    {
        "DestinationBackupVaultArn": str,
        "Lifecycle": NotRequired[LifecycleTypeDef],
    },
)
StartBackupJobInputRequestTypeDef = TypedDict(
    "StartBackupJobInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "ResourceArn": str,
        "IamRoleArn": str,
        "IdempotencyToken": NotRequired[str],
        "StartWindowMinutes": NotRequired[int],
        "CompleteWindowMinutes": NotRequired[int],
        "Lifecycle": NotRequired[LifecycleTypeDef],
        "RecoveryPointTags": NotRequired[Mapping[str, str]],
        "BackupOptions": NotRequired[Mapping[str, str]],
    },
)
StartCopyJobInputRequestTypeDef = TypedDict(
    "StartCopyJobInputRequestTypeDef",
    {
        "RecoveryPointArn": str,
        "SourceBackupVaultName": str,
        "DestinationBackupVaultArn": str,
        "IamRoleArn": str,
        "IdempotencyToken": NotRequired[str],
        "Lifecycle": NotRequired[LifecycleTypeDef],
    },
)
UpdateRecoveryPointLifecycleInputRequestTypeDef = TypedDict(
    "UpdateRecoveryPointLifecycleInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "RecoveryPointArn": str,
        "Lifecycle": NotRequired[LifecycleTypeDef],
    },
)
RecoveryPointByBackupVaultTypeDef = TypedDict(
    "RecoveryPointByBackupVaultTypeDef",
    {
        "RecoveryPointArn": NotRequired[str],
        "BackupVaultName": NotRequired[str],
        "BackupVaultArn": NotRequired[str],
        "SourceBackupVaultArn": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "ResourceType": NotRequired[str],
        "CreatedBy": NotRequired[RecoveryPointCreatorTypeDef],
        "IamRoleArn": NotRequired[str],
        "Status": NotRequired[RecoveryPointStatusType],
        "StatusMessage": NotRequired[str],
        "CreationDate": NotRequired[datetime],
        "CompletionDate": NotRequired[datetime],
        "BackupSizeInBytes": NotRequired[int],
        "CalculatedLifecycle": NotRequired[CalculatedLifecycleTypeDef],
        "Lifecycle": NotRequired[LifecycleTypeDef],
        "EncryptionKeyArn": NotRequired[str],
        "IsEncrypted": NotRequired[bool],
        "LastRestoreTime": NotRequired[datetime],
        "ParentRecoveryPointArn": NotRequired[str],
        "CompositeMemberIdentifier": NotRequired[str],
        "IsParent": NotRequired[bool],
        "ResourceName": NotRequired[str],
        "VaultType": NotRequired[VaultTypeType],
    },
)
ConditionsOutputTypeDef = TypedDict(
    "ConditionsOutputTypeDef",
    {
        "StringEquals": NotRequired[List[ConditionParameterTypeDef]],
        "StringNotEquals": NotRequired[List[ConditionParameterTypeDef]],
        "StringLike": NotRequired[List[ConditionParameterTypeDef]],
        "StringNotLike": NotRequired[List[ConditionParameterTypeDef]],
    },
)
ConditionsTypeDef = TypedDict(
    "ConditionsTypeDef",
    {
        "StringEquals": NotRequired[Sequence[ConditionParameterTypeDef]],
        "StringNotEquals": NotRequired[Sequence[ConditionParameterTypeDef]],
        "StringLike": NotRequired[Sequence[ConditionParameterTypeDef]],
        "StringNotLike": NotRequired[Sequence[ConditionParameterTypeDef]],
    },
)
FrameworkControlOutputTypeDef = TypedDict(
    "FrameworkControlOutputTypeDef",
    {
        "ControlName": str,
        "ControlInputParameters": NotRequired[List[ControlInputParameterTypeDef]],
        "ControlScope": NotRequired[ControlScopeOutputTypeDef],
    },
)
ControlScopeUnionTypeDef = Union[ControlScopeTypeDef, ControlScopeOutputTypeDef]
CreateBackupPlanOutputTypeDef = TypedDict(
    "CreateBackupPlanOutputTypeDef",
    {
        "BackupPlanId": str,
        "BackupPlanArn": str,
        "CreationDate": datetime,
        "VersionId": str,
        "AdvancedBackupSettings": List[AdvancedBackupSettingOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateBackupSelectionOutputTypeDef = TypedDict(
    "CreateBackupSelectionOutputTypeDef",
    {
        "SelectionId": str,
        "BackupPlanId": str,
        "CreationDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateBackupVaultOutputTypeDef = TypedDict(
    "CreateBackupVaultOutputTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "CreationDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFrameworkOutputTypeDef = TypedDict(
    "CreateFrameworkOutputTypeDef",
    {
        "FrameworkName": str,
        "FrameworkArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateLogicallyAirGappedBackupVaultOutputTypeDef = TypedDict(
    "CreateLogicallyAirGappedBackupVaultOutputTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "CreationDate": datetime,
        "VaultState": VaultStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateReportPlanOutputTypeDef = TypedDict(
    "CreateReportPlanOutputTypeDef",
    {
        "ReportPlanName": str,
        "ReportPlanArn": str,
        "CreationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRestoreTestingPlanOutputTypeDef = TypedDict(
    "CreateRestoreTestingPlanOutputTypeDef",
    {
        "CreationTime": datetime,
        "RestoreTestingPlanArn": str,
        "RestoreTestingPlanName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRestoreTestingSelectionOutputTypeDef = TypedDict(
    "CreateRestoreTestingSelectionOutputTypeDef",
    {
        "CreationTime": datetime,
        "RestoreTestingPlanArn": str,
        "RestoreTestingPlanName": str,
        "RestoreTestingSelectionName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteBackupPlanOutputTypeDef = TypedDict(
    "DeleteBackupPlanOutputTypeDef",
    {
        "BackupPlanId": str,
        "BackupPlanArn": str,
        "DeletionDate": datetime,
        "VersionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeBackupJobOutputTypeDef = TypedDict(
    "DescribeBackupJobOutputTypeDef",
    {
        "AccountId": str,
        "BackupJobId": str,
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "RecoveryPointArn": str,
        "ResourceArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "State": BackupJobStateType,
        "StatusMessage": str,
        "PercentDone": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "CreatedBy": RecoveryPointCreatorTypeDef,
        "ResourceType": str,
        "BytesTransferred": int,
        "ExpectedCompletionDate": datetime,
        "StartBy": datetime,
        "BackupOptions": Dict[str, str],
        "BackupType": str,
        "ParentJobId": str,
        "IsParent": bool,
        "NumberOfChildJobs": int,
        "ChildJobsInState": Dict[BackupJobStateType, int],
        "ResourceName": str,
        "InitiationDate": datetime,
        "MessageCategory": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeBackupVaultOutputTypeDef = TypedDict(
    "DescribeBackupVaultOutputTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "VaultType": VaultTypeType,
        "VaultState": VaultStateType,
        "EncryptionKeyArn": str,
        "CreationDate": datetime,
        "CreatorRequestId": str,
        "NumberOfRecoveryPoints": int,
        "Locked": bool,
        "MinRetentionDays": int,
        "MaxRetentionDays": int,
        "LockDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeGlobalSettingsOutputTypeDef = TypedDict(
    "DescribeGlobalSettingsOutputTypeDef",
    {
        "GlobalSettings": Dict[str, str],
        "LastUpdateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeProtectedResourceOutputTypeDef = TypedDict(
    "DescribeProtectedResourceOutputTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": str,
        "LastBackupTime": datetime,
        "ResourceName": str,
        "LastBackupVaultArn": str,
        "LastRecoveryPointArn": str,
        "LatestRestoreExecutionTimeMinutes": int,
        "LatestRestoreJobCreationDate": datetime,
        "LatestRestoreRecoveryPointCreationDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRecoveryPointOutputTypeDef = TypedDict(
    "DescribeRecoveryPointOutputTypeDef",
    {
        "RecoveryPointArn": str,
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "SourceBackupVaultArn": str,
        "ResourceArn": str,
        "ResourceType": str,
        "CreatedBy": RecoveryPointCreatorTypeDef,
        "IamRoleArn": str,
        "Status": RecoveryPointStatusType,
        "StatusMessage": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "BackupSizeInBytes": int,
        "CalculatedLifecycle": CalculatedLifecycleTypeDef,
        "Lifecycle": LifecycleTypeDef,
        "EncryptionKeyArn": str,
        "IsEncrypted": bool,
        "StorageClass": StorageClassType,
        "LastRestoreTime": datetime,
        "ParentRecoveryPointArn": str,
        "CompositeMemberIdentifier": str,
        "IsParent": bool,
        "ResourceName": str,
        "VaultType": VaultTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRegionSettingsOutputTypeDef = TypedDict(
    "DescribeRegionSettingsOutputTypeDef",
    {
        "ResourceTypeOptInPreference": Dict[str, bool],
        "ResourceTypeManagementPreference": Dict[str, bool],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportBackupPlanTemplateOutputTypeDef = TypedDict(
    "ExportBackupPlanTemplateOutputTypeDef",
    {
        "BackupPlanTemplateJson": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBackupVaultAccessPolicyOutputTypeDef = TypedDict(
    "GetBackupVaultAccessPolicyOutputTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "Policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBackupVaultNotificationsOutputTypeDef = TypedDict(
    "GetBackupVaultNotificationsOutputTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultArn": str,
        "SNSTopicArn": str,
        "BackupVaultEvents": List[BackupVaultEventType],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRecoveryPointRestoreMetadataOutputTypeDef = TypedDict(
    "GetRecoveryPointRestoreMetadataOutputTypeDef",
    {
        "BackupVaultArn": str,
        "RecoveryPointArn": str,
        "RestoreMetadata": Dict[str, str],
        "ResourceType": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRestoreJobMetadataOutputTypeDef = TypedDict(
    "GetRestoreJobMetadataOutputTypeDef",
    {
        "RestoreJobId": str,
        "Metadata": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRestoreTestingInferredMetadataOutputTypeDef = TypedDict(
    "GetRestoreTestingInferredMetadataOutputTypeDef",
    {
        "InferredMetadata": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSupportedResourceTypesOutputTypeDef = TypedDict(
    "GetSupportedResourceTypesOutputTypeDef",
    {
        "ResourceTypes": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListBackupJobSummariesOutputTypeDef = TypedDict(
    "ListBackupJobSummariesOutputTypeDef",
    {
        "BackupJobSummaries": List[BackupJobSummaryTypeDef],
        "AggregationPeriod": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListBackupPlanTemplatesOutputTypeDef = TypedDict(
    "ListBackupPlanTemplatesOutputTypeDef",
    {
        "BackupPlanTemplatesList": List[BackupPlanTemplatesListMemberTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListBackupSelectionsOutputTypeDef = TypedDict(
    "ListBackupSelectionsOutputTypeDef",
    {
        "BackupSelectionsList": List[BackupSelectionsListMemberTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListBackupVaultsOutputTypeDef = TypedDict(
    "ListBackupVaultsOutputTypeDef",
    {
        "BackupVaultList": List[BackupVaultListMemberTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListCopyJobSummariesOutputTypeDef = TypedDict(
    "ListCopyJobSummariesOutputTypeDef",
    {
        "CopyJobSummaries": List[CopyJobSummaryTypeDef],
        "AggregationPeriod": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTagsOutputTypeDef = TypedDict(
    "ListTagsOutputTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
StartBackupJobOutputTypeDef = TypedDict(
    "StartBackupJobOutputTypeDef",
    {
        "BackupJobId": str,
        "RecoveryPointArn": str,
        "CreationDate": datetime,
        "IsParent": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartCopyJobOutputTypeDef = TypedDict(
    "StartCopyJobOutputTypeDef",
    {
        "CopyJobId": str,
        "CreationDate": datetime,
        "IsParent": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartReportJobOutputTypeDef = TypedDict(
    "StartReportJobOutputTypeDef",
    {
        "ReportJobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartRestoreJobOutputTypeDef = TypedDict(
    "StartRestoreJobOutputTypeDef",
    {
        "RestoreJobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateBackupPlanOutputTypeDef = TypedDict(
    "UpdateBackupPlanOutputTypeDef",
    {
        "BackupPlanId": str,
        "BackupPlanArn": str,
        "CreationDate": datetime,
        "VersionId": str,
        "AdvancedBackupSettings": List[AdvancedBackupSettingOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFrameworkOutputTypeDef = TypedDict(
    "UpdateFrameworkOutputTypeDef",
    {
        "FrameworkName": str,
        "FrameworkArn": str,
        "CreationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRecoveryPointLifecycleOutputTypeDef = TypedDict(
    "UpdateRecoveryPointLifecycleOutputTypeDef",
    {
        "BackupVaultArn": str,
        "RecoveryPointArn": str,
        "Lifecycle": LifecycleTypeDef,
        "CalculatedLifecycle": CalculatedLifecycleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateReportPlanOutputTypeDef = TypedDict(
    "UpdateReportPlanOutputTypeDef",
    {
        "ReportPlanName": str,
        "ReportPlanArn": str,
        "CreationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRestoreTestingPlanOutputTypeDef = TypedDict(
    "UpdateRestoreTestingPlanOutputTypeDef",
    {
        "CreationTime": datetime,
        "RestoreTestingPlanArn": str,
        "RestoreTestingPlanName": str,
        "UpdateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRestoreTestingSelectionOutputTypeDef = TypedDict(
    "UpdateRestoreTestingSelectionOutputTypeDef",
    {
        "CreationTime": datetime,
        "RestoreTestingPlanArn": str,
        "RestoreTestingPlanName": str,
        "RestoreTestingSelectionName": str,
        "UpdateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateReportPlanInputRequestTypeDef = TypedDict(
    "CreateReportPlanInputRequestTypeDef",
    {
        "ReportPlanName": str,
        "ReportDeliveryChannel": ReportDeliveryChannelTypeDef,
        "ReportSetting": ReportSettingTypeDef,
        "ReportPlanDescription": NotRequired[str],
        "ReportPlanTags": NotRequired[Mapping[str, str]],
        "IdempotencyToken": NotRequired[str],
    },
)
UpdateReportPlanInputRequestTypeDef = TypedDict(
    "UpdateReportPlanInputRequestTypeDef",
    {
        "ReportPlanName": str,
        "ReportPlanDescription": NotRequired[str],
        "ReportDeliveryChannel": NotRequired[ReportDeliveryChannelTypeDef],
        "ReportSetting": NotRequired[ReportSettingTypeDef],
        "IdempotencyToken": NotRequired[str],
    },
)
RecoveryPointSelectionOutputTypeDef = TypedDict(
    "RecoveryPointSelectionOutputTypeDef",
    {
        "VaultNames": NotRequired[List[str]],
        "ResourceIdentifiers": NotRequired[List[str]],
        "DateRange": NotRequired[DateRangeOutputTypeDef],
    },
)
DateRangeTypeDef = TypedDict(
    "DateRangeTypeDef",
    {
        "FromDate": TimestampTypeDef,
        "ToDate": TimestampTypeDef,
    },
)
ListBackupJobsInputRequestTypeDef = TypedDict(
    "ListBackupJobsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ByResourceArn": NotRequired[str],
        "ByState": NotRequired[BackupJobStateType],
        "ByBackupVaultName": NotRequired[str],
        "ByCreatedBefore": NotRequired[TimestampTypeDef],
        "ByCreatedAfter": NotRequired[TimestampTypeDef],
        "ByResourceType": NotRequired[str],
        "ByAccountId": NotRequired[str],
        "ByCompleteAfter": NotRequired[TimestampTypeDef],
        "ByCompleteBefore": NotRequired[TimestampTypeDef],
        "ByParentJobId": NotRequired[str],
        "ByMessageCategory": NotRequired[str],
    },
)
ListCopyJobsInputRequestTypeDef = TypedDict(
    "ListCopyJobsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ByResourceArn": NotRequired[str],
        "ByState": NotRequired[CopyJobStateType],
        "ByCreatedBefore": NotRequired[TimestampTypeDef],
        "ByCreatedAfter": NotRequired[TimestampTypeDef],
        "ByResourceType": NotRequired[str],
        "ByDestinationVaultArn": NotRequired[str],
        "ByAccountId": NotRequired[str],
        "ByCompleteBefore": NotRequired[TimestampTypeDef],
        "ByCompleteAfter": NotRequired[TimestampTypeDef],
        "ByParentJobId": NotRequired[str],
        "ByMessageCategory": NotRequired[str],
    },
)
ListRecoveryPointsByBackupVaultInputRequestTypeDef = TypedDict(
    "ListRecoveryPointsByBackupVaultInputRequestTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultAccountId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ByResourceArn": NotRequired[str],
        "ByResourceType": NotRequired[str],
        "ByBackupPlanId": NotRequired[str],
        "ByCreatedBefore": NotRequired[TimestampTypeDef],
        "ByCreatedAfter": NotRequired[TimestampTypeDef],
        "ByParentRecoveryPointArn": NotRequired[str],
    },
)
ListReportJobsInputRequestTypeDef = TypedDict(
    "ListReportJobsInputRequestTypeDef",
    {
        "ByReportPlanName": NotRequired[str],
        "ByCreationBefore": NotRequired[TimestampTypeDef],
        "ByCreationAfter": NotRequired[TimestampTypeDef],
        "ByStatus": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListRestoreJobsByProtectedResourceInputRequestTypeDef = TypedDict(
    "ListRestoreJobsByProtectedResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "ByStatus": NotRequired[RestoreJobStatusType],
        "ByRecoveryPointCreationDateAfter": NotRequired[TimestampTypeDef],
        "ByRecoveryPointCreationDateBefore": NotRequired[TimestampTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListRestoreJobsInputRequestTypeDef = TypedDict(
    "ListRestoreJobsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ByAccountId": NotRequired[str],
        "ByResourceType": NotRequired[str],
        "ByCreatedBefore": NotRequired[TimestampTypeDef],
        "ByCreatedAfter": NotRequired[TimestampTypeDef],
        "ByStatus": NotRequired[RestoreJobStatusType],
        "ByCompleteBefore": NotRequired[TimestampTypeDef],
        "ByCompleteAfter": NotRequired[TimestampTypeDef],
        "ByRestoreTestingPlanArn": NotRequired[str],
    },
)
DescribeRestoreJobOutputTypeDef = TypedDict(
    "DescribeRestoreJobOutputTypeDef",
    {
        "AccountId": str,
        "RestoreJobId": str,
        "RecoveryPointArn": str,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "Status": RestoreJobStatusType,
        "StatusMessage": str,
        "PercentDone": str,
        "BackupSizeInBytes": int,
        "IamRoleArn": str,
        "ExpectedCompletionTimeMinutes": int,
        "CreatedResourceArn": str,
        "ResourceType": str,
        "RecoveryPointCreationDate": datetime,
        "CreatedBy": RestoreJobCreatorTypeDef,
        "ValidationStatus": RestoreValidationStatusType,
        "ValidationStatusMessage": str,
        "DeletionStatus": RestoreDeletionStatusType,
        "DeletionStatusMessage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreJobsListMemberTypeDef = TypedDict(
    "RestoreJobsListMemberTypeDef",
    {
        "AccountId": NotRequired[str],
        "RestoreJobId": NotRequired[str],
        "RecoveryPointArn": NotRequired[str],
        "CreationDate": NotRequired[datetime],
        "CompletionDate": NotRequired[datetime],
        "Status": NotRequired[RestoreJobStatusType],
        "StatusMessage": NotRequired[str],
        "PercentDone": NotRequired[str],
        "BackupSizeInBytes": NotRequired[int],
        "IamRoleArn": NotRequired[str],
        "ExpectedCompletionTimeMinutes": NotRequired[int],
        "CreatedResourceArn": NotRequired[str],
        "ResourceType": NotRequired[str],
        "RecoveryPointCreationDate": NotRequired[datetime],
        "CreatedBy": NotRequired[RestoreJobCreatorTypeDef],
        "ValidationStatus": NotRequired[RestoreValidationStatusType],
        "ValidationStatusMessage": NotRequired[str],
        "DeletionStatus": NotRequired[RestoreDeletionStatusType],
        "DeletionStatusMessage": NotRequired[str],
    },
)
ListFrameworksOutputTypeDef = TypedDict(
    "ListFrameworksOutputTypeDef",
    {
        "Frameworks": List[FrameworkTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ProtectedResourceConditionsOutputTypeDef = TypedDict(
    "ProtectedResourceConditionsOutputTypeDef",
    {
        "StringEquals": NotRequired[List[KeyValueTypeDef]],
        "StringNotEquals": NotRequired[List[KeyValueTypeDef]],
    },
)
ProtectedResourceConditionsTypeDef = TypedDict(
    "ProtectedResourceConditionsTypeDef",
    {
        "StringEquals": NotRequired[Sequence[KeyValueTypeDef]],
        "StringNotEquals": NotRequired[Sequence[KeyValueTypeDef]],
    },
)
ListLegalHoldsOutputTypeDef = TypedDict(
    "ListLegalHoldsOutputTypeDef",
    {
        "LegalHolds": List[LegalHoldTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListBackupJobsInputListBackupJobsPaginateTypeDef = TypedDict(
    "ListBackupJobsInputListBackupJobsPaginateTypeDef",
    {
        "ByResourceArn": NotRequired[str],
        "ByState": NotRequired[BackupJobStateType],
        "ByBackupVaultName": NotRequired[str],
        "ByCreatedBefore": NotRequired[TimestampTypeDef],
        "ByCreatedAfter": NotRequired[TimestampTypeDef],
        "ByResourceType": NotRequired[str],
        "ByAccountId": NotRequired[str],
        "ByCompleteAfter": NotRequired[TimestampTypeDef],
        "ByCompleteBefore": NotRequired[TimestampTypeDef],
        "ByParentJobId": NotRequired[str],
        "ByMessageCategory": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListBackupPlanTemplatesInputListBackupPlanTemplatesPaginateTypeDef = TypedDict(
    "ListBackupPlanTemplatesInputListBackupPlanTemplatesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListBackupPlanVersionsInputListBackupPlanVersionsPaginateTypeDef = TypedDict(
    "ListBackupPlanVersionsInputListBackupPlanVersionsPaginateTypeDef",
    {
        "BackupPlanId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListBackupPlansInputListBackupPlansPaginateTypeDef = TypedDict(
    "ListBackupPlansInputListBackupPlansPaginateTypeDef",
    {
        "IncludeDeleted": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListBackupSelectionsInputListBackupSelectionsPaginateTypeDef = TypedDict(
    "ListBackupSelectionsInputListBackupSelectionsPaginateTypeDef",
    {
        "BackupPlanId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListBackupVaultsInputListBackupVaultsPaginateTypeDef = TypedDict(
    "ListBackupVaultsInputListBackupVaultsPaginateTypeDef",
    {
        "ByVaultType": NotRequired[VaultTypeType],
        "ByShared": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCopyJobsInputListCopyJobsPaginateTypeDef = TypedDict(
    "ListCopyJobsInputListCopyJobsPaginateTypeDef",
    {
        "ByResourceArn": NotRequired[str],
        "ByState": NotRequired[CopyJobStateType],
        "ByCreatedBefore": NotRequired[TimestampTypeDef],
        "ByCreatedAfter": NotRequired[TimestampTypeDef],
        "ByResourceType": NotRequired[str],
        "ByDestinationVaultArn": NotRequired[str],
        "ByAccountId": NotRequired[str],
        "ByCompleteBefore": NotRequired[TimestampTypeDef],
        "ByCompleteAfter": NotRequired[TimestampTypeDef],
        "ByParentJobId": NotRequired[str],
        "ByMessageCategory": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListLegalHoldsInputListLegalHoldsPaginateTypeDef = TypedDict(
    "ListLegalHoldsInputListLegalHoldsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProtectedResourcesByBackupVaultInputListProtectedResourcesByBackupVaultPaginateTypeDef = TypedDict(
    "ListProtectedResourcesByBackupVaultInputListProtectedResourcesByBackupVaultPaginateTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultAccountId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProtectedResourcesInputListProtectedResourcesPaginateTypeDef = TypedDict(
    "ListProtectedResourcesInputListProtectedResourcesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRecoveryPointsByBackupVaultInputListRecoveryPointsByBackupVaultPaginateTypeDef = TypedDict(
    "ListRecoveryPointsByBackupVaultInputListRecoveryPointsByBackupVaultPaginateTypeDef",
    {
        "BackupVaultName": str,
        "BackupVaultAccountId": NotRequired[str],
        "ByResourceArn": NotRequired[str],
        "ByResourceType": NotRequired[str],
        "ByBackupPlanId": NotRequired[str],
        "ByCreatedBefore": NotRequired[TimestampTypeDef],
        "ByCreatedAfter": NotRequired[TimestampTypeDef],
        "ByParentRecoveryPointArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRecoveryPointsByLegalHoldInputListRecoveryPointsByLegalHoldPaginateTypeDef = TypedDict(
    "ListRecoveryPointsByLegalHoldInputListRecoveryPointsByLegalHoldPaginateTypeDef",
    {
        "LegalHoldId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRecoveryPointsByResourceInputListRecoveryPointsByResourcePaginateTypeDef = TypedDict(
    "ListRecoveryPointsByResourceInputListRecoveryPointsByResourcePaginateTypeDef",
    {
        "ResourceArn": str,
        "ManagedByAWSBackupOnly": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRestoreJobsByProtectedResourceInputListRestoreJobsByProtectedResourcePaginateTypeDef = (
    TypedDict(
        "ListRestoreJobsByProtectedResourceInputListRestoreJobsByProtectedResourcePaginateTypeDef",
        {
            "ResourceArn": str,
            "ByStatus": NotRequired[RestoreJobStatusType],
            "ByRecoveryPointCreationDateAfter": NotRequired[TimestampTypeDef],
            "ByRecoveryPointCreationDateBefore": NotRequired[TimestampTypeDef],
            "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
        },
    )
)
ListRestoreJobsInputListRestoreJobsPaginateTypeDef = TypedDict(
    "ListRestoreJobsInputListRestoreJobsPaginateTypeDef",
    {
        "ByAccountId": NotRequired[str],
        "ByResourceType": NotRequired[str],
        "ByCreatedBefore": NotRequired[TimestampTypeDef],
        "ByCreatedAfter": NotRequired[TimestampTypeDef],
        "ByStatus": NotRequired[RestoreJobStatusType],
        "ByCompleteBefore": NotRequired[TimestampTypeDef],
        "ByCompleteAfter": NotRequired[TimestampTypeDef],
        "ByRestoreTestingPlanArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRestoreTestingPlansInputListRestoreTestingPlansPaginateTypeDef = TypedDict(
    "ListRestoreTestingPlansInputListRestoreTestingPlansPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRestoreTestingSelectionsInputListRestoreTestingSelectionsPaginateTypeDef = TypedDict(
    "ListRestoreTestingSelectionsInputListRestoreTestingSelectionsPaginateTypeDef",
    {
        "RestoreTestingPlanName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProtectedResourcesByBackupVaultOutputTypeDef = TypedDict(
    "ListProtectedResourcesByBackupVaultOutputTypeDef",
    {
        "Results": List[ProtectedResourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListProtectedResourcesOutputTypeDef = TypedDict(
    "ListProtectedResourcesOutputTypeDef",
    {
        "Results": List[ProtectedResourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListRecoveryPointsByLegalHoldOutputTypeDef = TypedDict(
    "ListRecoveryPointsByLegalHoldOutputTypeDef",
    {
        "RecoveryPoints": List[RecoveryPointMemberTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListRecoveryPointsByResourceOutputTypeDef = TypedDict(
    "ListRecoveryPointsByResourceOutputTypeDef",
    {
        "RecoveryPoints": List[RecoveryPointByResourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListRestoreJobSummariesOutputTypeDef = TypedDict(
    "ListRestoreJobSummariesOutputTypeDef",
    {
        "RestoreJobSummaries": List[RestoreJobSummaryTypeDef],
        "AggregationPeriod": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListRestoreTestingPlansOutputTypeDef = TypedDict(
    "ListRestoreTestingPlansOutputTypeDef",
    {
        "RestoreTestingPlans": List[RestoreTestingPlanForListTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListRestoreTestingSelectionsOutputTypeDef = TypedDict(
    "ListRestoreTestingSelectionsOutputTypeDef",
    {
        "RestoreTestingSelections": List[RestoreTestingSelectionForListTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ReportJobTypeDef = TypedDict(
    "ReportJobTypeDef",
    {
        "ReportJobId": NotRequired[str],
        "ReportPlanArn": NotRequired[str],
        "ReportTemplate": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "CompletionTime": NotRequired[datetime],
        "Status": NotRequired[str],
        "StatusMessage": NotRequired[str],
        "ReportDestination": NotRequired[ReportDestinationTypeDef],
    },
)
ReportPlanTypeDef = TypedDict(
    "ReportPlanTypeDef",
    {
        "ReportPlanArn": NotRequired[str],
        "ReportPlanName": NotRequired[str],
        "ReportPlanDescription": NotRequired[str],
        "ReportSetting": NotRequired[ReportSettingOutputTypeDef],
        "ReportDeliveryChannel": NotRequired[ReportDeliveryChannelOutputTypeDef],
        "DeploymentStatus": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastAttemptedExecutionTime": NotRequired[datetime],
        "LastSuccessfulExecutionTime": NotRequired[datetime],
    },
)
RestoreTestingPlanForGetTypeDef = TypedDict(
    "RestoreTestingPlanForGetTypeDef",
    {
        "CreationTime": datetime,
        "RecoveryPointSelection": RestoreTestingRecoveryPointSelectionOutputTypeDef,
        "RestoreTestingPlanArn": str,
        "RestoreTestingPlanName": str,
        "ScheduleExpression": str,
        "CreatorRequestId": NotRequired[str],
        "LastExecutionTime": NotRequired[datetime],
        "LastUpdateTime": NotRequired[datetime],
        "ScheduleExpressionTimezone": NotRequired[str],
        "StartWindowHours": NotRequired[int],
    },
)
RestoreTestingRecoveryPointSelectionUnionTypeDef = Union[
    RestoreTestingRecoveryPointSelectionTypeDef, RestoreTestingRecoveryPointSelectionOutputTypeDef
]
ListBackupPlanVersionsOutputTypeDef = TypedDict(
    "ListBackupPlanVersionsOutputTypeDef",
    {
        "BackupPlanVersionsList": List[BackupPlansListMemberTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListBackupPlansOutputTypeDef = TypedDict(
    "ListBackupPlansOutputTypeDef",
    {
        "BackupPlansList": List[BackupPlansListMemberTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListBackupJobsOutputTypeDef = TypedDict(
    "ListBackupJobsOutputTypeDef",
    {
        "BackupJobs": List[BackupJobTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeCopyJobOutputTypeDef = TypedDict(
    "DescribeCopyJobOutputTypeDef",
    {
        "CopyJob": CopyJobTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCopyJobsOutputTypeDef = TypedDict(
    "ListCopyJobsOutputTypeDef",
    {
        "CopyJobs": List[CopyJobTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
BackupRuleInputTypeDef = TypedDict(
    "BackupRuleInputTypeDef",
    {
        "RuleName": str,
        "TargetBackupVaultName": str,
        "ScheduleExpression": NotRequired[str],
        "StartWindowMinutes": NotRequired[int],
        "CompletionWindowMinutes": NotRequired[int],
        "Lifecycle": NotRequired[LifecycleTypeDef],
        "RecoveryPointTags": NotRequired[Mapping[str, str]],
        "CopyActions": NotRequired[Sequence[CopyActionTypeDef]],
        "EnableContinuousBackup": NotRequired[bool],
        "ScheduleExpressionTimezone": NotRequired[str],
    },
)
BackupRuleTypeDef = TypedDict(
    "BackupRuleTypeDef",
    {
        "RuleName": str,
        "TargetBackupVaultName": str,
        "ScheduleExpression": NotRequired[str],
        "StartWindowMinutes": NotRequired[int],
        "CompletionWindowMinutes": NotRequired[int],
        "Lifecycle": NotRequired[LifecycleTypeDef],
        "RecoveryPointTags": NotRequired[Dict[str, str]],
        "RuleId": NotRequired[str],
        "CopyActions": NotRequired[List[CopyActionTypeDef]],
        "EnableContinuousBackup": NotRequired[bool],
        "ScheduleExpressionTimezone": NotRequired[str],
    },
)
ListRecoveryPointsByBackupVaultOutputTypeDef = TypedDict(
    "ListRecoveryPointsByBackupVaultOutputTypeDef",
    {
        "RecoveryPoints": List[RecoveryPointByBackupVaultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
BackupSelectionOutputTypeDef = TypedDict(
    "BackupSelectionOutputTypeDef",
    {
        "SelectionName": str,
        "IamRoleArn": str,
        "Resources": NotRequired[List[str]],
        "ListOfTags": NotRequired[List[ConditionTypeDef]],
        "NotResources": NotRequired[List[str]],
        "Conditions": NotRequired[ConditionsOutputTypeDef],
    },
)
ConditionsUnionTypeDef = Union[ConditionsTypeDef, ConditionsOutputTypeDef]
DescribeFrameworkOutputTypeDef = TypedDict(
    "DescribeFrameworkOutputTypeDef",
    {
        "FrameworkName": str,
        "FrameworkArn": str,
        "FrameworkDescription": str,
        "FrameworkControls": List[FrameworkControlOutputTypeDef],
        "CreationTime": datetime,
        "DeploymentStatus": str,
        "FrameworkStatus": str,
        "IdempotencyToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FrameworkControlTypeDef = TypedDict(
    "FrameworkControlTypeDef",
    {
        "ControlName": str,
        "ControlInputParameters": NotRequired[Sequence[ControlInputParameterTypeDef]],
        "ControlScope": NotRequired[ControlScopeUnionTypeDef],
    },
)
CreateLegalHoldOutputTypeDef = TypedDict(
    "CreateLegalHoldOutputTypeDef",
    {
        "Title": str,
        "Status": LegalHoldStatusType,
        "Description": str,
        "LegalHoldId": str,
        "LegalHoldArn": str,
        "CreationDate": datetime,
        "RecoveryPointSelection": RecoveryPointSelectionOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLegalHoldOutputTypeDef = TypedDict(
    "GetLegalHoldOutputTypeDef",
    {
        "Title": str,
        "Status": LegalHoldStatusType,
        "Description": str,
        "CancelDescription": str,
        "LegalHoldId": str,
        "LegalHoldArn": str,
        "CreationDate": datetime,
        "CancellationDate": datetime,
        "RetainRecordUntil": datetime,
        "RecoveryPointSelection": RecoveryPointSelectionOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DateRangeUnionTypeDef = Union[DateRangeTypeDef, DateRangeOutputTypeDef]
ListRestoreJobsByProtectedResourceOutputTypeDef = TypedDict(
    "ListRestoreJobsByProtectedResourceOutputTypeDef",
    {
        "RestoreJobs": List[RestoreJobsListMemberTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListRestoreJobsOutputTypeDef = TypedDict(
    "ListRestoreJobsOutputTypeDef",
    {
        "RestoreJobs": List[RestoreJobsListMemberTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
RestoreTestingSelectionForGetTypeDef = TypedDict(
    "RestoreTestingSelectionForGetTypeDef",
    {
        "CreationTime": datetime,
        "IamRoleArn": str,
        "ProtectedResourceType": str,
        "RestoreTestingPlanName": str,
        "RestoreTestingSelectionName": str,
        "CreatorRequestId": NotRequired[str],
        "ProtectedResourceArns": NotRequired[List[str]],
        "ProtectedResourceConditions": NotRequired[ProtectedResourceConditionsOutputTypeDef],
        "RestoreMetadataOverrides": NotRequired[Dict[str, str]],
        "ValidationWindowHours": NotRequired[int],
    },
)
ProtectedResourceConditionsUnionTypeDef = Union[
    ProtectedResourceConditionsTypeDef, ProtectedResourceConditionsOutputTypeDef
]
DescribeReportJobOutputTypeDef = TypedDict(
    "DescribeReportJobOutputTypeDef",
    {
        "ReportJob": ReportJobTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListReportJobsOutputTypeDef = TypedDict(
    "ListReportJobsOutputTypeDef",
    {
        "ReportJobs": List[ReportJobTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeReportPlanOutputTypeDef = TypedDict(
    "DescribeReportPlanOutputTypeDef",
    {
        "ReportPlan": ReportPlanTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListReportPlansOutputTypeDef = TypedDict(
    "ListReportPlansOutputTypeDef",
    {
        "ReportPlans": List[ReportPlanTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetRestoreTestingPlanOutputTypeDef = TypedDict(
    "GetRestoreTestingPlanOutputTypeDef",
    {
        "RestoreTestingPlan": RestoreTestingPlanForGetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreTestingPlanForCreateTypeDef = TypedDict(
    "RestoreTestingPlanForCreateTypeDef",
    {
        "RecoveryPointSelection": RestoreTestingRecoveryPointSelectionUnionTypeDef,
        "RestoreTestingPlanName": str,
        "ScheduleExpression": str,
        "ScheduleExpressionTimezone": NotRequired[str],
        "StartWindowHours": NotRequired[int],
    },
)
RestoreTestingPlanForUpdateTypeDef = TypedDict(
    "RestoreTestingPlanForUpdateTypeDef",
    {
        "RecoveryPointSelection": NotRequired[RestoreTestingRecoveryPointSelectionUnionTypeDef],
        "ScheduleExpression": NotRequired[str],
        "ScheduleExpressionTimezone": NotRequired[str],
        "StartWindowHours": NotRequired[int],
    },
)
BackupPlanInputTypeDef = TypedDict(
    "BackupPlanInputTypeDef",
    {
        "BackupPlanName": str,
        "Rules": Sequence[BackupRuleInputTypeDef],
        "AdvancedBackupSettings": NotRequired[Sequence[AdvancedBackupSettingUnionTypeDef]],
    },
)
BackupPlanTypeDef = TypedDict(
    "BackupPlanTypeDef",
    {
        "BackupPlanName": str,
        "Rules": List[BackupRuleTypeDef],
        "AdvancedBackupSettings": NotRequired[List[AdvancedBackupSettingOutputTypeDef]],
    },
)
GetBackupSelectionOutputTypeDef = TypedDict(
    "GetBackupSelectionOutputTypeDef",
    {
        "BackupSelection": BackupSelectionOutputTypeDef,
        "SelectionId": str,
        "BackupPlanId": str,
        "CreationDate": datetime,
        "CreatorRequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BackupSelectionTypeDef = TypedDict(
    "BackupSelectionTypeDef",
    {
        "SelectionName": str,
        "IamRoleArn": str,
        "Resources": NotRequired[Sequence[str]],
        "ListOfTags": NotRequired[Sequence[ConditionTypeDef]],
        "NotResources": NotRequired[Sequence[str]],
        "Conditions": NotRequired[ConditionsUnionTypeDef],
    },
)
FrameworkControlUnionTypeDef = Union[FrameworkControlTypeDef, FrameworkControlOutputTypeDef]
UpdateFrameworkInputRequestTypeDef = TypedDict(
    "UpdateFrameworkInputRequestTypeDef",
    {
        "FrameworkName": str,
        "FrameworkDescription": NotRequired[str],
        "FrameworkControls": NotRequired[Sequence[FrameworkControlTypeDef]],
        "IdempotencyToken": NotRequired[str],
    },
)
RecoveryPointSelectionTypeDef = TypedDict(
    "RecoveryPointSelectionTypeDef",
    {
        "VaultNames": NotRequired[Sequence[str]],
        "ResourceIdentifiers": NotRequired[Sequence[str]],
        "DateRange": NotRequired[DateRangeUnionTypeDef],
    },
)
GetRestoreTestingSelectionOutputTypeDef = TypedDict(
    "GetRestoreTestingSelectionOutputTypeDef",
    {
        "RestoreTestingSelection": RestoreTestingSelectionForGetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreTestingSelectionForCreateTypeDef = TypedDict(
    "RestoreTestingSelectionForCreateTypeDef",
    {
        "IamRoleArn": str,
        "ProtectedResourceType": str,
        "RestoreTestingSelectionName": str,
        "ProtectedResourceArns": NotRequired[Sequence[str]],
        "ProtectedResourceConditions": NotRequired[ProtectedResourceConditionsUnionTypeDef],
        "RestoreMetadataOverrides": NotRequired[Mapping[str, str]],
        "ValidationWindowHours": NotRequired[int],
    },
)
RestoreTestingSelectionForUpdateTypeDef = TypedDict(
    "RestoreTestingSelectionForUpdateTypeDef",
    {
        "IamRoleArn": NotRequired[str],
        "ProtectedResourceArns": NotRequired[Sequence[str]],
        "ProtectedResourceConditions": NotRequired[ProtectedResourceConditionsUnionTypeDef],
        "RestoreMetadataOverrides": NotRequired[Mapping[str, str]],
        "ValidationWindowHours": NotRequired[int],
    },
)
CreateRestoreTestingPlanInputRequestTypeDef = TypedDict(
    "CreateRestoreTestingPlanInputRequestTypeDef",
    {
        "RestoreTestingPlan": RestoreTestingPlanForCreateTypeDef,
        "CreatorRequestId": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
UpdateRestoreTestingPlanInputRequestTypeDef = TypedDict(
    "UpdateRestoreTestingPlanInputRequestTypeDef",
    {
        "RestoreTestingPlan": RestoreTestingPlanForUpdateTypeDef,
        "RestoreTestingPlanName": str,
    },
)
CreateBackupPlanInputRequestTypeDef = TypedDict(
    "CreateBackupPlanInputRequestTypeDef",
    {
        "BackupPlan": BackupPlanInputTypeDef,
        "BackupPlanTags": NotRequired[Mapping[str, str]],
        "CreatorRequestId": NotRequired[str],
    },
)
UpdateBackupPlanInputRequestTypeDef = TypedDict(
    "UpdateBackupPlanInputRequestTypeDef",
    {
        "BackupPlanId": str,
        "BackupPlan": BackupPlanInputTypeDef,
    },
)
GetBackupPlanFromJSONOutputTypeDef = TypedDict(
    "GetBackupPlanFromJSONOutputTypeDef",
    {
        "BackupPlan": BackupPlanTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBackupPlanFromTemplateOutputTypeDef = TypedDict(
    "GetBackupPlanFromTemplateOutputTypeDef",
    {
        "BackupPlanDocument": BackupPlanTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBackupPlanOutputTypeDef = TypedDict(
    "GetBackupPlanOutputTypeDef",
    {
        "BackupPlan": BackupPlanTypeDef,
        "BackupPlanId": str,
        "BackupPlanArn": str,
        "VersionId": str,
        "CreatorRequestId": str,
        "CreationDate": datetime,
        "DeletionDate": datetime,
        "LastExecutionDate": datetime,
        "AdvancedBackupSettings": List[AdvancedBackupSettingOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateBackupSelectionInputRequestTypeDef = TypedDict(
    "CreateBackupSelectionInputRequestTypeDef",
    {
        "BackupPlanId": str,
        "BackupSelection": BackupSelectionTypeDef,
        "CreatorRequestId": NotRequired[str],
    },
)
CreateFrameworkInputRequestTypeDef = TypedDict(
    "CreateFrameworkInputRequestTypeDef",
    {
        "FrameworkName": str,
        "FrameworkControls": Sequence[FrameworkControlUnionTypeDef],
        "FrameworkDescription": NotRequired[str],
        "IdempotencyToken": NotRequired[str],
        "FrameworkTags": NotRequired[Mapping[str, str]],
    },
)
CreateLegalHoldInputRequestTypeDef = TypedDict(
    "CreateLegalHoldInputRequestTypeDef",
    {
        "Title": str,
        "Description": str,
        "IdempotencyToken": NotRequired[str],
        "RecoveryPointSelection": NotRequired[RecoveryPointSelectionTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CreateRestoreTestingSelectionInputRequestTypeDef = TypedDict(
    "CreateRestoreTestingSelectionInputRequestTypeDef",
    {
        "RestoreTestingPlanName": str,
        "RestoreTestingSelection": RestoreTestingSelectionForCreateTypeDef,
        "CreatorRequestId": NotRequired[str],
    },
)
UpdateRestoreTestingSelectionInputRequestTypeDef = TypedDict(
    "UpdateRestoreTestingSelectionInputRequestTypeDef",
    {
        "RestoreTestingPlanName": str,
        "RestoreTestingSelection": RestoreTestingSelectionForUpdateTypeDef,
        "RestoreTestingSelectionName": str,
    },
)
