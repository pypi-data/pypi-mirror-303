"""
Type annotations for codepipeline service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/type_defs/)

Usage::

    ```python
    from mypy_boto3_codepipeline.type_defs import AWSSessionCredentialsTypeDef

    data: AWSSessionCredentialsTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    ActionCategoryType,
    ActionConfigurationPropertyTypeType,
    ActionExecutionStatusType,
    ActionOwnerType,
    ApprovalStatusType,
    ConditionExecutionStatusType,
    ConditionTypeType,
    ExecutionModeType,
    ExecutionTypeType,
    ExecutorTypeType,
    FailureTypeType,
    GitPullRequestEventTypeType,
    JobStatusType,
    PipelineExecutionStatusType,
    PipelineTypeType,
    ResultType,
    RetryTriggerType,
    RuleConfigurationPropertyTypeType,
    RuleExecutionStatusType,
    SourceRevisionTypeType,
    StageExecutionStatusType,
    StageRetryModeType,
    StageTransitionTypeType,
    StartTimeRangeType,
    TriggerTypeType,
    WebhookAuthenticationTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AWSSessionCredentialsTypeDef",
    "AcknowledgeJobInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "AcknowledgeThirdPartyJobInputRequestTypeDef",
    "ActionConfigurationPropertyTypeDef",
    "ActionConfigurationTypeDef",
    "ActionContextTypeDef",
    "ActionTypeIdTypeDef",
    "InputArtifactTypeDef",
    "OutputArtifactOutputTypeDef",
    "LatestInPipelineExecutionFilterTypeDef",
    "ErrorDetailsTypeDef",
    "ActionRevisionOutputTypeDef",
    "TimestampTypeDef",
    "ActionTypeArtifactDetailsTypeDef",
    "ActionTypeIdentifierTypeDef",
    "ActionTypePermissionsOutputTypeDef",
    "ActionTypePropertyTypeDef",
    "ActionTypeUrlsTypeDef",
    "ActionTypePermissionsTypeDef",
    "ActionTypeSettingsTypeDef",
    "ArtifactDetailsTypeDef",
    "ApprovalResultTypeDef",
    "S3LocationTypeDef",
    "S3ArtifactLocationTypeDef",
    "ArtifactRevisionTypeDef",
    "EncryptionKeyTypeDef",
    "BlockerDeclarationTypeDef",
    "ConditionExecutionTypeDef",
    "TagTypeDef",
    "DeleteCustomActionTypeInputRequestTypeDef",
    "DeletePipelineInputRequestTypeDef",
    "DeleteWebhookInputRequestTypeDef",
    "DeregisterWebhookWithThirdPartyInputRequestTypeDef",
    "DisableStageTransitionInputRequestTypeDef",
    "EnableStageTransitionInputRequestTypeDef",
    "ExecutionDetailsTypeDef",
    "ExecutionTriggerTypeDef",
    "JobWorkerExecutorConfigurationOutputTypeDef",
    "LambdaExecutorConfigurationTypeDef",
    "RetryConfigurationTypeDef",
    "FailureDetailsTypeDef",
    "GetActionTypeInputRequestTypeDef",
    "GetJobDetailsInputRequestTypeDef",
    "GetPipelineExecutionInputRequestTypeDef",
    "GetPipelineInputRequestTypeDef",
    "PipelineMetadataTypeDef",
    "GetPipelineStateInputRequestTypeDef",
    "GetThirdPartyJobDetailsInputRequestTypeDef",
    "GitBranchFilterCriteriaOutputTypeDef",
    "GitBranchFilterCriteriaTypeDef",
    "GitFilePathFilterCriteriaOutputTypeDef",
    "GitFilePathFilterCriteriaTypeDef",
    "GitTagFilterCriteriaOutputTypeDef",
    "GitTagFilterCriteriaTypeDef",
    "JobWorkerExecutorConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ListActionTypesInputRequestTypeDef",
    "ListPipelinesInputRequestTypeDef",
    "PipelineSummaryTypeDef",
    "ListRuleTypesInputRequestTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListWebhooksInputRequestTypeDef",
    "OutputArtifactTypeDef",
    "OverrideStageConditionInputRequestTypeDef",
    "StageContextTypeDef",
    "PipelineVariableDeclarationTypeDef",
    "SucceededInStageFilterTypeDef",
    "PipelineRollbackMetadataTypeDef",
    "SourceRevisionTypeDef",
    "StopExecutionTriggerTypeDef",
    "ResolvedPipelineVariableTypeDef",
    "PipelineVariableTypeDef",
    "ThirdPartyJobTypeDef",
    "RegisterWebhookWithThirdPartyInputRequestTypeDef",
    "RetryStageExecutionInputRequestTypeDef",
    "RetryStageMetadataTypeDef",
    "RollbackStageInputRequestTypeDef",
    "RuleConfigurationPropertyTypeDef",
    "RuleTypeIdTypeDef",
    "RuleRevisionTypeDef",
    "RuleTypeSettingsTypeDef",
    "SourceRevisionOverrideTypeDef",
    "StageConditionsExecutionTypeDef",
    "StageExecutionTypeDef",
    "TransitionStateTypeDef",
    "StopPipelineExecutionInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "WebhookAuthConfigurationTypeDef",
    "WebhookFilterRuleTypeDef",
    "AcknowledgeJobOutputTypeDef",
    "AcknowledgeThirdPartyJobOutputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "PutActionRevisionOutputTypeDef",
    "PutApprovalResultOutputTypeDef",
    "RetryStageExecutionOutputTypeDef",
    "RollbackStageOutputTypeDef",
    "StartPipelineExecutionOutputTypeDef",
    "StopPipelineExecutionOutputTypeDef",
    "PollForJobsInputRequestTypeDef",
    "PollForThirdPartyJobsInputRequestTypeDef",
    "ActionDeclarationOutputTypeDef",
    "ActionExecutionFilterTypeDef",
    "RuleExecutionFilterTypeDef",
    "ActionExecutionResultTypeDef",
    "ActionExecutionTypeDef",
    "RuleExecutionResultTypeDef",
    "RuleExecutionTypeDef",
    "ActionRevisionTypeDef",
    "CurrentRevisionTypeDef",
    "ActionTypePermissionsUnionTypeDef",
    "ActionTypeTypeDef",
    "PutApprovalResultInputRequestTypeDef",
    "ArtifactDetailTypeDef",
    "ArtifactLocationTypeDef",
    "ArtifactStoreTypeDef",
    "CreateCustomActionTypeInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "TagResourceInputRequestTypeDef",
    "ExecutorConfigurationOutputTypeDef",
    "PutJobFailureResultInputRequestTypeDef",
    "PutThirdPartyJobFailureResultInputRequestTypeDef",
    "GitBranchFilterCriteriaUnionTypeDef",
    "GitPullRequestFilterOutputTypeDef",
    "GitFilePathFilterCriteriaUnionTypeDef",
    "GitPushFilterOutputTypeDef",
    "GitTagFilterCriteriaUnionTypeDef",
    "JobWorkerExecutorConfigurationUnionTypeDef",
    "ListActionTypesInputListActionTypesPaginateTypeDef",
    "ListPipelinesInputListPipelinesPaginateTypeDef",
    "ListTagsForResourceInputListTagsForResourcePaginateTypeDef",
    "ListWebhooksInputListWebhooksPaginateTypeDef",
    "ListPipelinesOutputTypeDef",
    "OutputArtifactUnionTypeDef",
    "PipelineContextTypeDef",
    "PipelineExecutionFilterTypeDef",
    "PipelineExecutionSummaryTypeDef",
    "PipelineExecutionTypeDef",
    "PollForThirdPartyJobsOutputTypeDef",
    "RuleDeclarationOutputTypeDef",
    "RuleDeclarationTypeDef",
    "RuleTypeTypeDef",
    "StartPipelineExecutionInputRequestTypeDef",
    "WebhookDefinitionOutputTypeDef",
    "WebhookDefinitionTypeDef",
    "ListActionExecutionsInputListActionExecutionsPaginateTypeDef",
    "ListActionExecutionsInputRequestTypeDef",
    "ListRuleExecutionsInputListRuleExecutionsPaginateTypeDef",
    "ListRuleExecutionsInputRequestTypeDef",
    "ActionStateTypeDef",
    "RuleExecutionOutputTypeDef",
    "RuleStateTypeDef",
    "PutActionRevisionInputRequestTypeDef",
    "PutJobSuccessResultInputRequestTypeDef",
    "PutThirdPartyJobSuccessResultInputRequestTypeDef",
    "CreateCustomActionTypeOutputTypeDef",
    "ListActionTypesOutputTypeDef",
    "ActionExecutionInputTypeDef",
    "ActionExecutionOutputTypeDef",
    "RuleExecutionInputTypeDef",
    "ArtifactTypeDef",
    "ActionTypeExecutorOutputTypeDef",
    "GitPullRequestFilterTypeDef",
    "GitConfigurationOutputTypeDef",
    "GitPushFilterTypeDef",
    "ExecutorConfigurationTypeDef",
    "ActionDeclarationTypeDef",
    "ListPipelineExecutionsInputListPipelineExecutionsPaginateTypeDef",
    "ListPipelineExecutionsInputRequestTypeDef",
    "ListPipelineExecutionsOutputTypeDef",
    "GetPipelineExecutionOutputTypeDef",
    "ConditionOutputTypeDef",
    "RuleDeclarationUnionTypeDef",
    "ListRuleTypesOutputTypeDef",
    "ListWebhookItemTypeDef",
    "PutWebhookInputRequestTypeDef",
    "ConditionStateTypeDef",
    "ActionExecutionDetailTypeDef",
    "RuleExecutionDetailTypeDef",
    "JobDataTypeDef",
    "ThirdPartyJobDataTypeDef",
    "ActionTypeDeclarationOutputTypeDef",
    "GitPullRequestFilterUnionTypeDef",
    "PipelineTriggerDeclarationOutputTypeDef",
    "GitPushFilterUnionTypeDef",
    "ExecutorConfigurationUnionTypeDef",
    "ActionDeclarationUnionTypeDef",
    "BeforeEntryConditionsOutputTypeDef",
    "FailureConditionsOutputTypeDef",
    "SuccessConditionsOutputTypeDef",
    "ConditionTypeDef",
    "ListWebhooksOutputTypeDef",
    "PutWebhookOutputTypeDef",
    "StageConditionStateTypeDef",
    "ListActionExecutionsOutputTypeDef",
    "ListRuleExecutionsOutputTypeDef",
    "JobDetailsTypeDef",
    "JobTypeDef",
    "ThirdPartyJobDetailsTypeDef",
    "GetActionTypeOutputTypeDef",
    "GitConfigurationTypeDef",
    "ActionTypeExecutorTypeDef",
    "StageDeclarationOutputTypeDef",
    "BeforeEntryConditionsTypeDef",
    "ConditionUnionTypeDef",
    "SuccessConditionsTypeDef",
    "StageStateTypeDef",
    "GetJobDetailsOutputTypeDef",
    "PollForJobsOutputTypeDef",
    "GetThirdPartyJobDetailsOutputTypeDef",
    "GitConfigurationUnionTypeDef",
    "ActionTypeExecutorUnionTypeDef",
    "PipelineDeclarationOutputTypeDef",
    "BeforeEntryConditionsUnionTypeDef",
    "FailureConditionsTypeDef",
    "SuccessConditionsUnionTypeDef",
    "GetPipelineStateOutputTypeDef",
    "PipelineTriggerDeclarationTypeDef",
    "ActionTypeDeclarationTypeDef",
    "CreatePipelineOutputTypeDef",
    "GetPipelineOutputTypeDef",
    "UpdatePipelineOutputTypeDef",
    "FailureConditionsUnionTypeDef",
    "PipelineTriggerDeclarationUnionTypeDef",
    "UpdateActionTypeInputRequestTypeDef",
    "StageDeclarationTypeDef",
    "StageDeclarationUnionTypeDef",
    "PipelineDeclarationTypeDef",
    "CreatePipelineInputRequestTypeDef",
    "UpdatePipelineInputRequestTypeDef",
)

AWSSessionCredentialsTypeDef = TypedDict(
    "AWSSessionCredentialsTypeDef",
    {
        "accessKeyId": str,
        "secretAccessKey": str,
        "sessionToken": str,
    },
)
AcknowledgeJobInputRequestTypeDef = TypedDict(
    "AcknowledgeJobInputRequestTypeDef",
    {
        "jobId": str,
        "nonce": str,
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
AcknowledgeThirdPartyJobInputRequestTypeDef = TypedDict(
    "AcknowledgeThirdPartyJobInputRequestTypeDef",
    {
        "jobId": str,
        "nonce": str,
        "clientToken": str,
    },
)
ActionConfigurationPropertyTypeDef = TypedDict(
    "ActionConfigurationPropertyTypeDef",
    {
        "name": str,
        "required": bool,
        "key": bool,
        "secret": bool,
        "queryable": NotRequired[bool],
        "description": NotRequired[str],
        "type": NotRequired[ActionConfigurationPropertyTypeType],
    },
)
ActionConfigurationTypeDef = TypedDict(
    "ActionConfigurationTypeDef",
    {
        "configuration": NotRequired[Dict[str, str]],
    },
)
ActionContextTypeDef = TypedDict(
    "ActionContextTypeDef",
    {
        "name": NotRequired[str],
        "actionExecutionId": NotRequired[str],
    },
)
ActionTypeIdTypeDef = TypedDict(
    "ActionTypeIdTypeDef",
    {
        "category": ActionCategoryType,
        "owner": ActionOwnerType,
        "provider": str,
        "version": str,
    },
)
InputArtifactTypeDef = TypedDict(
    "InputArtifactTypeDef",
    {
        "name": str,
    },
)
OutputArtifactOutputTypeDef = TypedDict(
    "OutputArtifactOutputTypeDef",
    {
        "name": str,
        "files": NotRequired[List[str]],
    },
)
LatestInPipelineExecutionFilterTypeDef = TypedDict(
    "LatestInPipelineExecutionFilterTypeDef",
    {
        "pipelineExecutionId": str,
        "startTimeRange": StartTimeRangeType,
    },
)
ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef",
    {
        "code": NotRequired[str],
        "message": NotRequired[str],
    },
)
ActionRevisionOutputTypeDef = TypedDict(
    "ActionRevisionOutputTypeDef",
    {
        "revisionId": str,
        "revisionChangeId": str,
        "created": datetime,
    },
)
TimestampTypeDef = Union[datetime, str]
ActionTypeArtifactDetailsTypeDef = TypedDict(
    "ActionTypeArtifactDetailsTypeDef",
    {
        "minimumCount": int,
        "maximumCount": int,
    },
)
ActionTypeIdentifierTypeDef = TypedDict(
    "ActionTypeIdentifierTypeDef",
    {
        "category": ActionCategoryType,
        "owner": str,
        "provider": str,
        "version": str,
    },
)
ActionTypePermissionsOutputTypeDef = TypedDict(
    "ActionTypePermissionsOutputTypeDef",
    {
        "allowedAccounts": List[str],
    },
)
ActionTypePropertyTypeDef = TypedDict(
    "ActionTypePropertyTypeDef",
    {
        "name": str,
        "optional": bool,
        "key": bool,
        "noEcho": bool,
        "queryable": NotRequired[bool],
        "description": NotRequired[str],
    },
)
ActionTypeUrlsTypeDef = TypedDict(
    "ActionTypeUrlsTypeDef",
    {
        "configurationUrl": NotRequired[str],
        "entityUrlTemplate": NotRequired[str],
        "executionUrlTemplate": NotRequired[str],
        "revisionUrlTemplate": NotRequired[str],
    },
)
ActionTypePermissionsTypeDef = TypedDict(
    "ActionTypePermissionsTypeDef",
    {
        "allowedAccounts": Sequence[str],
    },
)
ActionTypeSettingsTypeDef = TypedDict(
    "ActionTypeSettingsTypeDef",
    {
        "thirdPartyConfigurationUrl": NotRequired[str],
        "entityUrlTemplate": NotRequired[str],
        "executionUrlTemplate": NotRequired[str],
        "revisionUrlTemplate": NotRequired[str],
    },
)
ArtifactDetailsTypeDef = TypedDict(
    "ArtifactDetailsTypeDef",
    {
        "minimumCount": int,
        "maximumCount": int,
    },
)
ApprovalResultTypeDef = TypedDict(
    "ApprovalResultTypeDef",
    {
        "summary": str,
        "status": ApprovalStatusType,
    },
)
S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucket": NotRequired[str],
        "key": NotRequired[str],
    },
)
S3ArtifactLocationTypeDef = TypedDict(
    "S3ArtifactLocationTypeDef",
    {
        "bucketName": str,
        "objectKey": str,
    },
)
ArtifactRevisionTypeDef = TypedDict(
    "ArtifactRevisionTypeDef",
    {
        "name": NotRequired[str],
        "revisionId": NotRequired[str],
        "revisionChangeIdentifier": NotRequired[str],
        "revisionSummary": NotRequired[str],
        "created": NotRequired[datetime],
        "revisionUrl": NotRequired[str],
    },
)
EncryptionKeyTypeDef = TypedDict(
    "EncryptionKeyTypeDef",
    {
        "id": str,
        "type": Literal["KMS"],
    },
)
BlockerDeclarationTypeDef = TypedDict(
    "BlockerDeclarationTypeDef",
    {
        "name": str,
        "type": Literal["Schedule"],
    },
)
ConditionExecutionTypeDef = TypedDict(
    "ConditionExecutionTypeDef",
    {
        "status": NotRequired[ConditionExecutionStatusType],
        "summary": NotRequired[str],
        "lastStatusChange": NotRequired[datetime],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)
DeleteCustomActionTypeInputRequestTypeDef = TypedDict(
    "DeleteCustomActionTypeInputRequestTypeDef",
    {
        "category": ActionCategoryType,
        "provider": str,
        "version": str,
    },
)
DeletePipelineInputRequestTypeDef = TypedDict(
    "DeletePipelineInputRequestTypeDef",
    {
        "name": str,
    },
)
DeleteWebhookInputRequestTypeDef = TypedDict(
    "DeleteWebhookInputRequestTypeDef",
    {
        "name": str,
    },
)
DeregisterWebhookWithThirdPartyInputRequestTypeDef = TypedDict(
    "DeregisterWebhookWithThirdPartyInputRequestTypeDef",
    {
        "webhookName": NotRequired[str],
    },
)
DisableStageTransitionInputRequestTypeDef = TypedDict(
    "DisableStageTransitionInputRequestTypeDef",
    {
        "pipelineName": str,
        "stageName": str,
        "transitionType": StageTransitionTypeType,
        "reason": str,
    },
)
EnableStageTransitionInputRequestTypeDef = TypedDict(
    "EnableStageTransitionInputRequestTypeDef",
    {
        "pipelineName": str,
        "stageName": str,
        "transitionType": StageTransitionTypeType,
    },
)
ExecutionDetailsTypeDef = TypedDict(
    "ExecutionDetailsTypeDef",
    {
        "summary": NotRequired[str],
        "externalExecutionId": NotRequired[str],
        "percentComplete": NotRequired[int],
    },
)
ExecutionTriggerTypeDef = TypedDict(
    "ExecutionTriggerTypeDef",
    {
        "triggerType": NotRequired[TriggerTypeType],
        "triggerDetail": NotRequired[str],
    },
)
JobWorkerExecutorConfigurationOutputTypeDef = TypedDict(
    "JobWorkerExecutorConfigurationOutputTypeDef",
    {
        "pollingAccounts": NotRequired[List[str]],
        "pollingServicePrincipals": NotRequired[List[str]],
    },
)
LambdaExecutorConfigurationTypeDef = TypedDict(
    "LambdaExecutorConfigurationTypeDef",
    {
        "lambdaFunctionArn": str,
    },
)
RetryConfigurationTypeDef = TypedDict(
    "RetryConfigurationTypeDef",
    {
        "retryMode": NotRequired[StageRetryModeType],
    },
)
FailureDetailsTypeDef = TypedDict(
    "FailureDetailsTypeDef",
    {
        "type": FailureTypeType,
        "message": str,
        "externalExecutionId": NotRequired[str],
    },
)
GetActionTypeInputRequestTypeDef = TypedDict(
    "GetActionTypeInputRequestTypeDef",
    {
        "category": ActionCategoryType,
        "owner": str,
        "provider": str,
        "version": str,
    },
)
GetJobDetailsInputRequestTypeDef = TypedDict(
    "GetJobDetailsInputRequestTypeDef",
    {
        "jobId": str,
    },
)
GetPipelineExecutionInputRequestTypeDef = TypedDict(
    "GetPipelineExecutionInputRequestTypeDef",
    {
        "pipelineName": str,
        "pipelineExecutionId": str,
    },
)
GetPipelineInputRequestTypeDef = TypedDict(
    "GetPipelineInputRequestTypeDef",
    {
        "name": str,
        "version": NotRequired[int],
    },
)
PipelineMetadataTypeDef = TypedDict(
    "PipelineMetadataTypeDef",
    {
        "pipelineArn": NotRequired[str],
        "created": NotRequired[datetime],
        "updated": NotRequired[datetime],
        "pollingDisabledAt": NotRequired[datetime],
    },
)
GetPipelineStateInputRequestTypeDef = TypedDict(
    "GetPipelineStateInputRequestTypeDef",
    {
        "name": str,
    },
)
GetThirdPartyJobDetailsInputRequestTypeDef = TypedDict(
    "GetThirdPartyJobDetailsInputRequestTypeDef",
    {
        "jobId": str,
        "clientToken": str,
    },
)
GitBranchFilterCriteriaOutputTypeDef = TypedDict(
    "GitBranchFilterCriteriaOutputTypeDef",
    {
        "includes": NotRequired[List[str]],
        "excludes": NotRequired[List[str]],
    },
)
GitBranchFilterCriteriaTypeDef = TypedDict(
    "GitBranchFilterCriteriaTypeDef",
    {
        "includes": NotRequired[Sequence[str]],
        "excludes": NotRequired[Sequence[str]],
    },
)
GitFilePathFilterCriteriaOutputTypeDef = TypedDict(
    "GitFilePathFilterCriteriaOutputTypeDef",
    {
        "includes": NotRequired[List[str]],
        "excludes": NotRequired[List[str]],
    },
)
GitFilePathFilterCriteriaTypeDef = TypedDict(
    "GitFilePathFilterCriteriaTypeDef",
    {
        "includes": NotRequired[Sequence[str]],
        "excludes": NotRequired[Sequence[str]],
    },
)
GitTagFilterCriteriaOutputTypeDef = TypedDict(
    "GitTagFilterCriteriaOutputTypeDef",
    {
        "includes": NotRequired[List[str]],
        "excludes": NotRequired[List[str]],
    },
)
GitTagFilterCriteriaTypeDef = TypedDict(
    "GitTagFilterCriteriaTypeDef",
    {
        "includes": NotRequired[Sequence[str]],
        "excludes": NotRequired[Sequence[str]],
    },
)
JobWorkerExecutorConfigurationTypeDef = TypedDict(
    "JobWorkerExecutorConfigurationTypeDef",
    {
        "pollingAccounts": NotRequired[Sequence[str]],
        "pollingServicePrincipals": NotRequired[Sequence[str]],
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
ListActionTypesInputRequestTypeDef = TypedDict(
    "ListActionTypesInputRequestTypeDef",
    {
        "actionOwnerFilter": NotRequired[ActionOwnerType],
        "nextToken": NotRequired[str],
        "regionFilter": NotRequired[str],
    },
)
ListPipelinesInputRequestTypeDef = TypedDict(
    "ListPipelinesInputRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
PipelineSummaryTypeDef = TypedDict(
    "PipelineSummaryTypeDef",
    {
        "name": NotRequired[str],
        "version": NotRequired[int],
        "pipelineType": NotRequired[PipelineTypeType],
        "executionMode": NotRequired[ExecutionModeType],
        "created": NotRequired[datetime],
        "updated": NotRequired[datetime],
    },
)
ListRuleTypesInputRequestTypeDef = TypedDict(
    "ListRuleTypesInputRequestTypeDef",
    {
        "ruleOwnerFilter": NotRequired[Literal["AWS"]],
        "regionFilter": NotRequired[str],
    },
)
ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListWebhooksInputRequestTypeDef = TypedDict(
    "ListWebhooksInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
OutputArtifactTypeDef = TypedDict(
    "OutputArtifactTypeDef",
    {
        "name": str,
        "files": NotRequired[Sequence[str]],
    },
)
OverrideStageConditionInputRequestTypeDef = TypedDict(
    "OverrideStageConditionInputRequestTypeDef",
    {
        "pipelineName": str,
        "stageName": str,
        "pipelineExecutionId": str,
        "conditionType": ConditionTypeType,
    },
)
StageContextTypeDef = TypedDict(
    "StageContextTypeDef",
    {
        "name": NotRequired[str],
    },
)
PipelineVariableDeclarationTypeDef = TypedDict(
    "PipelineVariableDeclarationTypeDef",
    {
        "name": str,
        "defaultValue": NotRequired[str],
        "description": NotRequired[str],
    },
)
SucceededInStageFilterTypeDef = TypedDict(
    "SucceededInStageFilterTypeDef",
    {
        "stageName": NotRequired[str],
    },
)
PipelineRollbackMetadataTypeDef = TypedDict(
    "PipelineRollbackMetadataTypeDef",
    {
        "rollbackTargetPipelineExecutionId": NotRequired[str],
    },
)
SourceRevisionTypeDef = TypedDict(
    "SourceRevisionTypeDef",
    {
        "actionName": str,
        "revisionId": NotRequired[str],
        "revisionSummary": NotRequired[str],
        "revisionUrl": NotRequired[str],
    },
)
StopExecutionTriggerTypeDef = TypedDict(
    "StopExecutionTriggerTypeDef",
    {
        "reason": NotRequired[str],
    },
)
ResolvedPipelineVariableTypeDef = TypedDict(
    "ResolvedPipelineVariableTypeDef",
    {
        "name": NotRequired[str],
        "resolvedValue": NotRequired[str],
    },
)
PipelineVariableTypeDef = TypedDict(
    "PipelineVariableTypeDef",
    {
        "name": str,
        "value": str,
    },
)
ThirdPartyJobTypeDef = TypedDict(
    "ThirdPartyJobTypeDef",
    {
        "clientId": NotRequired[str],
        "jobId": NotRequired[str],
    },
)
RegisterWebhookWithThirdPartyInputRequestTypeDef = TypedDict(
    "RegisterWebhookWithThirdPartyInputRequestTypeDef",
    {
        "webhookName": NotRequired[str],
    },
)
RetryStageExecutionInputRequestTypeDef = TypedDict(
    "RetryStageExecutionInputRequestTypeDef",
    {
        "pipelineName": str,
        "stageName": str,
        "pipelineExecutionId": str,
        "retryMode": StageRetryModeType,
    },
)
RetryStageMetadataTypeDef = TypedDict(
    "RetryStageMetadataTypeDef",
    {
        "autoStageRetryAttempt": NotRequired[int],
        "manualStageRetryAttempt": NotRequired[int],
        "latestRetryTrigger": NotRequired[RetryTriggerType],
    },
)
RollbackStageInputRequestTypeDef = TypedDict(
    "RollbackStageInputRequestTypeDef",
    {
        "pipelineName": str,
        "stageName": str,
        "targetPipelineExecutionId": str,
    },
)
RuleConfigurationPropertyTypeDef = TypedDict(
    "RuleConfigurationPropertyTypeDef",
    {
        "name": str,
        "required": bool,
        "key": bool,
        "secret": bool,
        "queryable": NotRequired[bool],
        "description": NotRequired[str],
        "type": NotRequired[RuleConfigurationPropertyTypeType],
    },
)
RuleTypeIdTypeDef = TypedDict(
    "RuleTypeIdTypeDef",
    {
        "category": Literal["Rule"],
        "provider": str,
        "owner": NotRequired[Literal["AWS"]],
        "version": NotRequired[str],
    },
)
RuleRevisionTypeDef = TypedDict(
    "RuleRevisionTypeDef",
    {
        "revisionId": str,
        "revisionChangeId": str,
        "created": datetime,
    },
)
RuleTypeSettingsTypeDef = TypedDict(
    "RuleTypeSettingsTypeDef",
    {
        "thirdPartyConfigurationUrl": NotRequired[str],
        "entityUrlTemplate": NotRequired[str],
        "executionUrlTemplate": NotRequired[str],
        "revisionUrlTemplate": NotRequired[str],
    },
)
SourceRevisionOverrideTypeDef = TypedDict(
    "SourceRevisionOverrideTypeDef",
    {
        "actionName": str,
        "revisionType": SourceRevisionTypeType,
        "revisionValue": str,
    },
)
StageConditionsExecutionTypeDef = TypedDict(
    "StageConditionsExecutionTypeDef",
    {
        "status": NotRequired[ConditionExecutionStatusType],
        "summary": NotRequired[str],
    },
)
StageExecutionTypeDef = TypedDict(
    "StageExecutionTypeDef",
    {
        "pipelineExecutionId": str,
        "status": StageExecutionStatusType,
        "type": NotRequired[ExecutionTypeType],
    },
)
TransitionStateTypeDef = TypedDict(
    "TransitionStateTypeDef",
    {
        "enabled": NotRequired[bool],
        "lastChangedBy": NotRequired[str],
        "lastChangedAt": NotRequired[datetime],
        "disabledReason": NotRequired[str],
    },
)
StopPipelineExecutionInputRequestTypeDef = TypedDict(
    "StopPipelineExecutionInputRequestTypeDef",
    {
        "pipelineName": str,
        "pipelineExecutionId": str,
        "abandon": NotRequired[bool],
        "reason": NotRequired[str],
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
WebhookAuthConfigurationTypeDef = TypedDict(
    "WebhookAuthConfigurationTypeDef",
    {
        "AllowedIPRange": NotRequired[str],
        "SecretToken": NotRequired[str],
    },
)
WebhookFilterRuleTypeDef = TypedDict(
    "WebhookFilterRuleTypeDef",
    {
        "jsonPath": str,
        "matchEquals": NotRequired[str],
    },
)
AcknowledgeJobOutputTypeDef = TypedDict(
    "AcknowledgeJobOutputTypeDef",
    {
        "status": JobStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AcknowledgeThirdPartyJobOutputTypeDef = TypedDict(
    "AcknowledgeThirdPartyJobOutputTypeDef",
    {
        "status": JobStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutActionRevisionOutputTypeDef = TypedDict(
    "PutActionRevisionOutputTypeDef",
    {
        "newRevision": bool,
        "pipelineExecutionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutApprovalResultOutputTypeDef = TypedDict(
    "PutApprovalResultOutputTypeDef",
    {
        "approvedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RetryStageExecutionOutputTypeDef = TypedDict(
    "RetryStageExecutionOutputTypeDef",
    {
        "pipelineExecutionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RollbackStageOutputTypeDef = TypedDict(
    "RollbackStageOutputTypeDef",
    {
        "pipelineExecutionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartPipelineExecutionOutputTypeDef = TypedDict(
    "StartPipelineExecutionOutputTypeDef",
    {
        "pipelineExecutionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopPipelineExecutionOutputTypeDef = TypedDict(
    "StopPipelineExecutionOutputTypeDef",
    {
        "pipelineExecutionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PollForJobsInputRequestTypeDef = TypedDict(
    "PollForJobsInputRequestTypeDef",
    {
        "actionTypeId": ActionTypeIdTypeDef,
        "maxBatchSize": NotRequired[int],
        "queryParam": NotRequired[Mapping[str, str]],
    },
)
PollForThirdPartyJobsInputRequestTypeDef = TypedDict(
    "PollForThirdPartyJobsInputRequestTypeDef",
    {
        "actionTypeId": ActionTypeIdTypeDef,
        "maxBatchSize": NotRequired[int],
    },
)
ActionDeclarationOutputTypeDef = TypedDict(
    "ActionDeclarationOutputTypeDef",
    {
        "name": str,
        "actionTypeId": ActionTypeIdTypeDef,
        "runOrder": NotRequired[int],
        "configuration": NotRequired[Dict[str, str]],
        "commands": NotRequired[List[str]],
        "outputArtifacts": NotRequired[List[OutputArtifactOutputTypeDef]],
        "inputArtifacts": NotRequired[List[InputArtifactTypeDef]],
        "outputVariables": NotRequired[List[str]],
        "roleArn": NotRequired[str],
        "region": NotRequired[str],
        "namespace": NotRequired[str],
        "timeoutInMinutes": NotRequired[int],
    },
)
ActionExecutionFilterTypeDef = TypedDict(
    "ActionExecutionFilterTypeDef",
    {
        "pipelineExecutionId": NotRequired[str],
        "latestInPipelineExecution": NotRequired[LatestInPipelineExecutionFilterTypeDef],
    },
)
RuleExecutionFilterTypeDef = TypedDict(
    "RuleExecutionFilterTypeDef",
    {
        "pipelineExecutionId": NotRequired[str],
        "latestInPipelineExecution": NotRequired[LatestInPipelineExecutionFilterTypeDef],
    },
)
ActionExecutionResultTypeDef = TypedDict(
    "ActionExecutionResultTypeDef",
    {
        "externalExecutionId": NotRequired[str],
        "externalExecutionSummary": NotRequired[str],
        "externalExecutionUrl": NotRequired[str],
        "errorDetails": NotRequired[ErrorDetailsTypeDef],
    },
)
ActionExecutionTypeDef = TypedDict(
    "ActionExecutionTypeDef",
    {
        "actionExecutionId": NotRequired[str],
        "status": NotRequired[ActionExecutionStatusType],
        "summary": NotRequired[str],
        "lastStatusChange": NotRequired[datetime],
        "token": NotRequired[str],
        "lastUpdatedBy": NotRequired[str],
        "externalExecutionId": NotRequired[str],
        "externalExecutionUrl": NotRequired[str],
        "percentComplete": NotRequired[int],
        "errorDetails": NotRequired[ErrorDetailsTypeDef],
    },
)
RuleExecutionResultTypeDef = TypedDict(
    "RuleExecutionResultTypeDef",
    {
        "externalExecutionId": NotRequired[str],
        "externalExecutionSummary": NotRequired[str],
        "externalExecutionUrl": NotRequired[str],
        "errorDetails": NotRequired[ErrorDetailsTypeDef],
    },
)
RuleExecutionTypeDef = TypedDict(
    "RuleExecutionTypeDef",
    {
        "ruleExecutionId": NotRequired[str],
        "status": NotRequired[RuleExecutionStatusType],
        "summary": NotRequired[str],
        "lastStatusChange": NotRequired[datetime],
        "token": NotRequired[str],
        "lastUpdatedBy": NotRequired[str],
        "externalExecutionId": NotRequired[str],
        "externalExecutionUrl": NotRequired[str],
        "errorDetails": NotRequired[ErrorDetailsTypeDef],
    },
)
ActionRevisionTypeDef = TypedDict(
    "ActionRevisionTypeDef",
    {
        "revisionId": str,
        "revisionChangeId": str,
        "created": TimestampTypeDef,
    },
)
CurrentRevisionTypeDef = TypedDict(
    "CurrentRevisionTypeDef",
    {
        "revision": str,
        "changeIdentifier": str,
        "created": NotRequired[TimestampTypeDef],
        "revisionSummary": NotRequired[str],
    },
)
ActionTypePermissionsUnionTypeDef = Union[
    ActionTypePermissionsTypeDef, ActionTypePermissionsOutputTypeDef
]
ActionTypeTypeDef = TypedDict(
    "ActionTypeTypeDef",
    {
        "id": ActionTypeIdTypeDef,
        "inputArtifactDetails": ArtifactDetailsTypeDef,
        "outputArtifactDetails": ArtifactDetailsTypeDef,
        "settings": NotRequired[ActionTypeSettingsTypeDef],
        "actionConfigurationProperties": NotRequired[List[ActionConfigurationPropertyTypeDef]],
    },
)
PutApprovalResultInputRequestTypeDef = TypedDict(
    "PutApprovalResultInputRequestTypeDef",
    {
        "pipelineName": str,
        "stageName": str,
        "actionName": str,
        "result": ApprovalResultTypeDef,
        "token": str,
    },
)
ArtifactDetailTypeDef = TypedDict(
    "ArtifactDetailTypeDef",
    {
        "name": NotRequired[str],
        "s3location": NotRequired[S3LocationTypeDef],
    },
)
ArtifactLocationTypeDef = TypedDict(
    "ArtifactLocationTypeDef",
    {
        "type": NotRequired[Literal["S3"]],
        "s3Location": NotRequired[S3ArtifactLocationTypeDef],
    },
)
ArtifactStoreTypeDef = TypedDict(
    "ArtifactStoreTypeDef",
    {
        "type": Literal["S3"],
        "location": str,
        "encryptionKey": NotRequired[EncryptionKeyTypeDef],
    },
)
CreateCustomActionTypeInputRequestTypeDef = TypedDict(
    "CreateCustomActionTypeInputRequestTypeDef",
    {
        "category": ActionCategoryType,
        "provider": str,
        "version": str,
        "inputArtifactDetails": ArtifactDetailsTypeDef,
        "outputArtifactDetails": ArtifactDetailsTypeDef,
        "settings": NotRequired[ActionTypeSettingsTypeDef],
        "configurationProperties": NotRequired[Sequence[ActionConfigurationPropertyTypeDef]],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "tags": List[TagTypeDef],
        "nextToken": str,
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
ExecutorConfigurationOutputTypeDef = TypedDict(
    "ExecutorConfigurationOutputTypeDef",
    {
        "lambdaExecutorConfiguration": NotRequired[LambdaExecutorConfigurationTypeDef],
        "jobWorkerExecutorConfiguration": NotRequired[JobWorkerExecutorConfigurationOutputTypeDef],
    },
)
PutJobFailureResultInputRequestTypeDef = TypedDict(
    "PutJobFailureResultInputRequestTypeDef",
    {
        "jobId": str,
        "failureDetails": FailureDetailsTypeDef,
    },
)
PutThirdPartyJobFailureResultInputRequestTypeDef = TypedDict(
    "PutThirdPartyJobFailureResultInputRequestTypeDef",
    {
        "jobId": str,
        "clientToken": str,
        "failureDetails": FailureDetailsTypeDef,
    },
)
GitBranchFilterCriteriaUnionTypeDef = Union[
    GitBranchFilterCriteriaTypeDef, GitBranchFilterCriteriaOutputTypeDef
]
GitPullRequestFilterOutputTypeDef = TypedDict(
    "GitPullRequestFilterOutputTypeDef",
    {
        "events": NotRequired[List[GitPullRequestEventTypeType]],
        "branches": NotRequired[GitBranchFilterCriteriaOutputTypeDef],
        "filePaths": NotRequired[GitFilePathFilterCriteriaOutputTypeDef],
    },
)
GitFilePathFilterCriteriaUnionTypeDef = Union[
    GitFilePathFilterCriteriaTypeDef, GitFilePathFilterCriteriaOutputTypeDef
]
GitPushFilterOutputTypeDef = TypedDict(
    "GitPushFilterOutputTypeDef",
    {
        "tags": NotRequired[GitTagFilterCriteriaOutputTypeDef],
        "branches": NotRequired[GitBranchFilterCriteriaOutputTypeDef],
        "filePaths": NotRequired[GitFilePathFilterCriteriaOutputTypeDef],
    },
)
GitTagFilterCriteriaUnionTypeDef = Union[
    GitTagFilterCriteriaTypeDef, GitTagFilterCriteriaOutputTypeDef
]
JobWorkerExecutorConfigurationUnionTypeDef = Union[
    JobWorkerExecutorConfigurationTypeDef, JobWorkerExecutorConfigurationOutputTypeDef
]
ListActionTypesInputListActionTypesPaginateTypeDef = TypedDict(
    "ListActionTypesInputListActionTypesPaginateTypeDef",
    {
        "actionOwnerFilter": NotRequired[ActionOwnerType],
        "regionFilter": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPipelinesInputListPipelinesPaginateTypeDef = TypedDict(
    "ListPipelinesInputListPipelinesPaginateTypeDef",
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
ListWebhooksInputListWebhooksPaginateTypeDef = TypedDict(
    "ListWebhooksInputListWebhooksPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPipelinesOutputTypeDef = TypedDict(
    "ListPipelinesOutputTypeDef",
    {
        "pipelines": List[PipelineSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OutputArtifactUnionTypeDef = Union[OutputArtifactTypeDef, OutputArtifactOutputTypeDef]
PipelineContextTypeDef = TypedDict(
    "PipelineContextTypeDef",
    {
        "pipelineName": NotRequired[str],
        "stage": NotRequired[StageContextTypeDef],
        "action": NotRequired[ActionContextTypeDef],
        "pipelineArn": NotRequired[str],
        "pipelineExecutionId": NotRequired[str],
    },
)
PipelineExecutionFilterTypeDef = TypedDict(
    "PipelineExecutionFilterTypeDef",
    {
        "succeededInStage": NotRequired[SucceededInStageFilterTypeDef],
    },
)
PipelineExecutionSummaryTypeDef = TypedDict(
    "PipelineExecutionSummaryTypeDef",
    {
        "pipelineExecutionId": NotRequired[str],
        "status": NotRequired[PipelineExecutionStatusType],
        "statusSummary": NotRequired[str],
        "startTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "sourceRevisions": NotRequired[List[SourceRevisionTypeDef]],
        "trigger": NotRequired[ExecutionTriggerTypeDef],
        "stopTrigger": NotRequired[StopExecutionTriggerTypeDef],
        "executionMode": NotRequired[ExecutionModeType],
        "executionType": NotRequired[ExecutionTypeType],
        "rollbackMetadata": NotRequired[PipelineRollbackMetadataTypeDef],
    },
)
PipelineExecutionTypeDef = TypedDict(
    "PipelineExecutionTypeDef",
    {
        "pipelineName": NotRequired[str],
        "pipelineVersion": NotRequired[int],
        "pipelineExecutionId": NotRequired[str],
        "status": NotRequired[PipelineExecutionStatusType],
        "statusSummary": NotRequired[str],
        "artifactRevisions": NotRequired[List[ArtifactRevisionTypeDef]],
        "variables": NotRequired[List[ResolvedPipelineVariableTypeDef]],
        "trigger": NotRequired[ExecutionTriggerTypeDef],
        "executionMode": NotRequired[ExecutionModeType],
        "executionType": NotRequired[ExecutionTypeType],
        "rollbackMetadata": NotRequired[PipelineRollbackMetadataTypeDef],
    },
)
PollForThirdPartyJobsOutputTypeDef = TypedDict(
    "PollForThirdPartyJobsOutputTypeDef",
    {
        "jobs": List[ThirdPartyJobTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RuleDeclarationOutputTypeDef = TypedDict(
    "RuleDeclarationOutputTypeDef",
    {
        "name": str,
        "ruleTypeId": RuleTypeIdTypeDef,
        "configuration": NotRequired[Dict[str, str]],
        "inputArtifacts": NotRequired[List[InputArtifactTypeDef]],
        "roleArn": NotRequired[str],
        "region": NotRequired[str],
        "timeoutInMinutes": NotRequired[int],
    },
)
RuleDeclarationTypeDef = TypedDict(
    "RuleDeclarationTypeDef",
    {
        "name": str,
        "ruleTypeId": RuleTypeIdTypeDef,
        "configuration": NotRequired[Mapping[str, str]],
        "inputArtifacts": NotRequired[Sequence[InputArtifactTypeDef]],
        "roleArn": NotRequired[str],
        "region": NotRequired[str],
        "timeoutInMinutes": NotRequired[int],
    },
)
RuleTypeTypeDef = TypedDict(
    "RuleTypeTypeDef",
    {
        "id": RuleTypeIdTypeDef,
        "inputArtifactDetails": ArtifactDetailsTypeDef,
        "settings": NotRequired[RuleTypeSettingsTypeDef],
        "ruleConfigurationProperties": NotRequired[List[RuleConfigurationPropertyTypeDef]],
    },
)
StartPipelineExecutionInputRequestTypeDef = TypedDict(
    "StartPipelineExecutionInputRequestTypeDef",
    {
        "name": str,
        "variables": NotRequired[Sequence[PipelineVariableTypeDef]],
        "clientRequestToken": NotRequired[str],
        "sourceRevisions": NotRequired[Sequence[SourceRevisionOverrideTypeDef]],
    },
)
WebhookDefinitionOutputTypeDef = TypedDict(
    "WebhookDefinitionOutputTypeDef",
    {
        "name": str,
        "targetPipeline": str,
        "targetAction": str,
        "filters": List[WebhookFilterRuleTypeDef],
        "authentication": WebhookAuthenticationTypeType,
        "authenticationConfiguration": WebhookAuthConfigurationTypeDef,
    },
)
WebhookDefinitionTypeDef = TypedDict(
    "WebhookDefinitionTypeDef",
    {
        "name": str,
        "targetPipeline": str,
        "targetAction": str,
        "filters": Sequence[WebhookFilterRuleTypeDef],
        "authentication": WebhookAuthenticationTypeType,
        "authenticationConfiguration": WebhookAuthConfigurationTypeDef,
    },
)
ListActionExecutionsInputListActionExecutionsPaginateTypeDef = TypedDict(
    "ListActionExecutionsInputListActionExecutionsPaginateTypeDef",
    {
        "pipelineName": str,
        "filter": NotRequired[ActionExecutionFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListActionExecutionsInputRequestTypeDef = TypedDict(
    "ListActionExecutionsInputRequestTypeDef",
    {
        "pipelineName": str,
        "filter": NotRequired[ActionExecutionFilterTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListRuleExecutionsInputListRuleExecutionsPaginateTypeDef = TypedDict(
    "ListRuleExecutionsInputListRuleExecutionsPaginateTypeDef",
    {
        "pipelineName": str,
        "filter": NotRequired[RuleExecutionFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRuleExecutionsInputRequestTypeDef = TypedDict(
    "ListRuleExecutionsInputRequestTypeDef",
    {
        "pipelineName": str,
        "filter": NotRequired[RuleExecutionFilterTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ActionStateTypeDef = TypedDict(
    "ActionStateTypeDef",
    {
        "actionName": NotRequired[str],
        "currentRevision": NotRequired[ActionRevisionOutputTypeDef],
        "latestExecution": NotRequired[ActionExecutionTypeDef],
        "entityUrl": NotRequired[str],
        "revisionUrl": NotRequired[str],
    },
)
RuleExecutionOutputTypeDef = TypedDict(
    "RuleExecutionOutputTypeDef",
    {
        "executionResult": NotRequired[RuleExecutionResultTypeDef],
    },
)
RuleStateTypeDef = TypedDict(
    "RuleStateTypeDef",
    {
        "ruleName": NotRequired[str],
        "currentRevision": NotRequired[RuleRevisionTypeDef],
        "latestExecution": NotRequired[RuleExecutionTypeDef],
        "entityUrl": NotRequired[str],
        "revisionUrl": NotRequired[str],
    },
)
PutActionRevisionInputRequestTypeDef = TypedDict(
    "PutActionRevisionInputRequestTypeDef",
    {
        "pipelineName": str,
        "stageName": str,
        "actionName": str,
        "actionRevision": ActionRevisionTypeDef,
    },
)
PutJobSuccessResultInputRequestTypeDef = TypedDict(
    "PutJobSuccessResultInputRequestTypeDef",
    {
        "jobId": str,
        "currentRevision": NotRequired[CurrentRevisionTypeDef],
        "continuationToken": NotRequired[str],
        "executionDetails": NotRequired[ExecutionDetailsTypeDef],
        "outputVariables": NotRequired[Mapping[str, str]],
    },
)
PutThirdPartyJobSuccessResultInputRequestTypeDef = TypedDict(
    "PutThirdPartyJobSuccessResultInputRequestTypeDef",
    {
        "jobId": str,
        "clientToken": str,
        "currentRevision": NotRequired[CurrentRevisionTypeDef],
        "continuationToken": NotRequired[str],
        "executionDetails": NotRequired[ExecutionDetailsTypeDef],
    },
)
CreateCustomActionTypeOutputTypeDef = TypedDict(
    "CreateCustomActionTypeOutputTypeDef",
    {
        "actionType": ActionTypeTypeDef,
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListActionTypesOutputTypeDef = TypedDict(
    "ListActionTypesOutputTypeDef",
    {
        "actionTypes": List[ActionTypeTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ActionExecutionInputTypeDef = TypedDict(
    "ActionExecutionInputTypeDef",
    {
        "actionTypeId": NotRequired[ActionTypeIdTypeDef],
        "configuration": NotRequired[Dict[str, str]],
        "resolvedConfiguration": NotRequired[Dict[str, str]],
        "roleArn": NotRequired[str],
        "region": NotRequired[str],
        "inputArtifacts": NotRequired[List[ArtifactDetailTypeDef]],
        "namespace": NotRequired[str],
    },
)
ActionExecutionOutputTypeDef = TypedDict(
    "ActionExecutionOutputTypeDef",
    {
        "outputArtifacts": NotRequired[List[ArtifactDetailTypeDef]],
        "executionResult": NotRequired[ActionExecutionResultTypeDef],
        "outputVariables": NotRequired[Dict[str, str]],
    },
)
RuleExecutionInputTypeDef = TypedDict(
    "RuleExecutionInputTypeDef",
    {
        "ruleTypeId": NotRequired[RuleTypeIdTypeDef],
        "configuration": NotRequired[Dict[str, str]],
        "resolvedConfiguration": NotRequired[Dict[str, str]],
        "roleArn": NotRequired[str],
        "region": NotRequired[str],
        "inputArtifacts": NotRequired[List[ArtifactDetailTypeDef]],
    },
)
ArtifactTypeDef = TypedDict(
    "ArtifactTypeDef",
    {
        "name": NotRequired[str],
        "revision": NotRequired[str],
        "location": NotRequired[ArtifactLocationTypeDef],
    },
)
ActionTypeExecutorOutputTypeDef = TypedDict(
    "ActionTypeExecutorOutputTypeDef",
    {
        "configuration": ExecutorConfigurationOutputTypeDef,
        "type": ExecutorTypeType,
        "policyStatementsTemplate": NotRequired[str],
        "jobTimeout": NotRequired[int],
    },
)
GitPullRequestFilterTypeDef = TypedDict(
    "GitPullRequestFilterTypeDef",
    {
        "events": NotRequired[Sequence[GitPullRequestEventTypeType]],
        "branches": NotRequired[GitBranchFilterCriteriaUnionTypeDef],
        "filePaths": NotRequired[GitFilePathFilterCriteriaUnionTypeDef],
    },
)
GitConfigurationOutputTypeDef = TypedDict(
    "GitConfigurationOutputTypeDef",
    {
        "sourceActionName": str,
        "push": NotRequired[List[GitPushFilterOutputTypeDef]],
        "pullRequest": NotRequired[List[GitPullRequestFilterOutputTypeDef]],
    },
)
GitPushFilterTypeDef = TypedDict(
    "GitPushFilterTypeDef",
    {
        "tags": NotRequired[GitTagFilterCriteriaUnionTypeDef],
        "branches": NotRequired[GitBranchFilterCriteriaUnionTypeDef],
        "filePaths": NotRequired[GitFilePathFilterCriteriaUnionTypeDef],
    },
)
ExecutorConfigurationTypeDef = TypedDict(
    "ExecutorConfigurationTypeDef",
    {
        "lambdaExecutorConfiguration": NotRequired[LambdaExecutorConfigurationTypeDef],
        "jobWorkerExecutorConfiguration": NotRequired[JobWorkerExecutorConfigurationUnionTypeDef],
    },
)
ActionDeclarationTypeDef = TypedDict(
    "ActionDeclarationTypeDef",
    {
        "name": str,
        "actionTypeId": ActionTypeIdTypeDef,
        "runOrder": NotRequired[int],
        "configuration": NotRequired[Mapping[str, str]],
        "commands": NotRequired[Sequence[str]],
        "outputArtifacts": NotRequired[Sequence[OutputArtifactUnionTypeDef]],
        "inputArtifacts": NotRequired[Sequence[InputArtifactTypeDef]],
        "outputVariables": NotRequired[Sequence[str]],
        "roleArn": NotRequired[str],
        "region": NotRequired[str],
        "namespace": NotRequired[str],
        "timeoutInMinutes": NotRequired[int],
    },
)
ListPipelineExecutionsInputListPipelineExecutionsPaginateTypeDef = TypedDict(
    "ListPipelineExecutionsInputListPipelineExecutionsPaginateTypeDef",
    {
        "pipelineName": str,
        "filter": NotRequired[PipelineExecutionFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPipelineExecutionsInputRequestTypeDef = TypedDict(
    "ListPipelineExecutionsInputRequestTypeDef",
    {
        "pipelineName": str,
        "maxResults": NotRequired[int],
        "filter": NotRequired[PipelineExecutionFilterTypeDef],
        "nextToken": NotRequired[str],
    },
)
ListPipelineExecutionsOutputTypeDef = TypedDict(
    "ListPipelineExecutionsOutputTypeDef",
    {
        "pipelineExecutionSummaries": List[PipelineExecutionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPipelineExecutionOutputTypeDef = TypedDict(
    "GetPipelineExecutionOutputTypeDef",
    {
        "pipelineExecution": PipelineExecutionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConditionOutputTypeDef = TypedDict(
    "ConditionOutputTypeDef",
    {
        "result": NotRequired[ResultType],
        "rules": NotRequired[List[RuleDeclarationOutputTypeDef]],
    },
)
RuleDeclarationUnionTypeDef = Union[RuleDeclarationTypeDef, RuleDeclarationOutputTypeDef]
ListRuleTypesOutputTypeDef = TypedDict(
    "ListRuleTypesOutputTypeDef",
    {
        "ruleTypes": List[RuleTypeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListWebhookItemTypeDef = TypedDict(
    "ListWebhookItemTypeDef",
    {
        "definition": WebhookDefinitionOutputTypeDef,
        "url": str,
        "errorMessage": NotRequired[str],
        "errorCode": NotRequired[str],
        "lastTriggered": NotRequired[datetime],
        "arn": NotRequired[str],
        "tags": NotRequired[List[TagTypeDef]],
    },
)
PutWebhookInputRequestTypeDef = TypedDict(
    "PutWebhookInputRequestTypeDef",
    {
        "webhook": WebhookDefinitionTypeDef,
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ConditionStateTypeDef = TypedDict(
    "ConditionStateTypeDef",
    {
        "latestExecution": NotRequired[ConditionExecutionTypeDef],
        "ruleStates": NotRequired[List[RuleStateTypeDef]],
    },
)
ActionExecutionDetailTypeDef = TypedDict(
    "ActionExecutionDetailTypeDef",
    {
        "pipelineExecutionId": NotRequired[str],
        "actionExecutionId": NotRequired[str],
        "pipelineVersion": NotRequired[int],
        "stageName": NotRequired[str],
        "actionName": NotRequired[str],
        "startTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "updatedBy": NotRequired[str],
        "status": NotRequired[ActionExecutionStatusType],
        "input": NotRequired[ActionExecutionInputTypeDef],
        "output": NotRequired[ActionExecutionOutputTypeDef],
    },
)
RuleExecutionDetailTypeDef = TypedDict(
    "RuleExecutionDetailTypeDef",
    {
        "pipelineExecutionId": NotRequired[str],
        "ruleExecutionId": NotRequired[str],
        "pipelineVersion": NotRequired[int],
        "stageName": NotRequired[str],
        "ruleName": NotRequired[str],
        "startTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "updatedBy": NotRequired[str],
        "status": NotRequired[RuleExecutionStatusType],
        "input": NotRequired[RuleExecutionInputTypeDef],
        "output": NotRequired[RuleExecutionOutputTypeDef],
    },
)
JobDataTypeDef = TypedDict(
    "JobDataTypeDef",
    {
        "actionTypeId": NotRequired[ActionTypeIdTypeDef],
        "actionConfiguration": NotRequired[ActionConfigurationTypeDef],
        "pipelineContext": NotRequired[PipelineContextTypeDef],
        "inputArtifacts": NotRequired[List[ArtifactTypeDef]],
        "outputArtifacts": NotRequired[List[ArtifactTypeDef]],
        "artifactCredentials": NotRequired[AWSSessionCredentialsTypeDef],
        "continuationToken": NotRequired[str],
        "encryptionKey": NotRequired[EncryptionKeyTypeDef],
    },
)
ThirdPartyJobDataTypeDef = TypedDict(
    "ThirdPartyJobDataTypeDef",
    {
        "actionTypeId": NotRequired[ActionTypeIdTypeDef],
        "actionConfiguration": NotRequired[ActionConfigurationTypeDef],
        "pipelineContext": NotRequired[PipelineContextTypeDef],
        "inputArtifacts": NotRequired[List[ArtifactTypeDef]],
        "outputArtifacts": NotRequired[List[ArtifactTypeDef]],
        "artifactCredentials": NotRequired[AWSSessionCredentialsTypeDef],
        "continuationToken": NotRequired[str],
        "encryptionKey": NotRequired[EncryptionKeyTypeDef],
    },
)
ActionTypeDeclarationOutputTypeDef = TypedDict(
    "ActionTypeDeclarationOutputTypeDef",
    {
        "executor": ActionTypeExecutorOutputTypeDef,
        "id": ActionTypeIdentifierTypeDef,
        "inputArtifactDetails": ActionTypeArtifactDetailsTypeDef,
        "outputArtifactDetails": ActionTypeArtifactDetailsTypeDef,
        "description": NotRequired[str],
        "permissions": NotRequired[ActionTypePermissionsOutputTypeDef],
        "properties": NotRequired[List[ActionTypePropertyTypeDef]],
        "urls": NotRequired[ActionTypeUrlsTypeDef],
    },
)
GitPullRequestFilterUnionTypeDef = Union[
    GitPullRequestFilterTypeDef, GitPullRequestFilterOutputTypeDef
]
PipelineTriggerDeclarationOutputTypeDef = TypedDict(
    "PipelineTriggerDeclarationOutputTypeDef",
    {
        "providerType": Literal["CodeStarSourceConnection"],
        "gitConfiguration": GitConfigurationOutputTypeDef,
    },
)
GitPushFilterUnionTypeDef = Union[GitPushFilterTypeDef, GitPushFilterOutputTypeDef]
ExecutorConfigurationUnionTypeDef = Union[
    ExecutorConfigurationTypeDef, ExecutorConfigurationOutputTypeDef
]
ActionDeclarationUnionTypeDef = Union[ActionDeclarationTypeDef, ActionDeclarationOutputTypeDef]
BeforeEntryConditionsOutputTypeDef = TypedDict(
    "BeforeEntryConditionsOutputTypeDef",
    {
        "conditions": List[ConditionOutputTypeDef],
    },
)
FailureConditionsOutputTypeDef = TypedDict(
    "FailureConditionsOutputTypeDef",
    {
        "result": NotRequired[ResultType],
        "retryConfiguration": NotRequired[RetryConfigurationTypeDef],
        "conditions": NotRequired[List[ConditionOutputTypeDef]],
    },
)
SuccessConditionsOutputTypeDef = TypedDict(
    "SuccessConditionsOutputTypeDef",
    {
        "conditions": List[ConditionOutputTypeDef],
    },
)
ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "result": NotRequired[ResultType],
        "rules": NotRequired[Sequence[RuleDeclarationUnionTypeDef]],
    },
)
ListWebhooksOutputTypeDef = TypedDict(
    "ListWebhooksOutputTypeDef",
    {
        "webhooks": List[ListWebhookItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PutWebhookOutputTypeDef = TypedDict(
    "PutWebhookOutputTypeDef",
    {
        "webhook": ListWebhookItemTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StageConditionStateTypeDef = TypedDict(
    "StageConditionStateTypeDef",
    {
        "latestExecution": NotRequired[StageConditionsExecutionTypeDef],
        "conditionStates": NotRequired[List[ConditionStateTypeDef]],
    },
)
ListActionExecutionsOutputTypeDef = TypedDict(
    "ListActionExecutionsOutputTypeDef",
    {
        "actionExecutionDetails": List[ActionExecutionDetailTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRuleExecutionsOutputTypeDef = TypedDict(
    "ListRuleExecutionsOutputTypeDef",
    {
        "ruleExecutionDetails": List[RuleExecutionDetailTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
JobDetailsTypeDef = TypedDict(
    "JobDetailsTypeDef",
    {
        "id": NotRequired[str],
        "data": NotRequired[JobDataTypeDef],
        "accountId": NotRequired[str],
    },
)
JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "id": NotRequired[str],
        "data": NotRequired[JobDataTypeDef],
        "nonce": NotRequired[str],
        "accountId": NotRequired[str],
    },
)
ThirdPartyJobDetailsTypeDef = TypedDict(
    "ThirdPartyJobDetailsTypeDef",
    {
        "id": NotRequired[str],
        "data": NotRequired[ThirdPartyJobDataTypeDef],
        "nonce": NotRequired[str],
    },
)
GetActionTypeOutputTypeDef = TypedDict(
    "GetActionTypeOutputTypeDef",
    {
        "actionType": ActionTypeDeclarationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GitConfigurationTypeDef = TypedDict(
    "GitConfigurationTypeDef",
    {
        "sourceActionName": str,
        "push": NotRequired[Sequence[GitPushFilterUnionTypeDef]],
        "pullRequest": NotRequired[Sequence[GitPullRequestFilterUnionTypeDef]],
    },
)
ActionTypeExecutorTypeDef = TypedDict(
    "ActionTypeExecutorTypeDef",
    {
        "configuration": ExecutorConfigurationUnionTypeDef,
        "type": ExecutorTypeType,
        "policyStatementsTemplate": NotRequired[str],
        "jobTimeout": NotRequired[int],
    },
)
StageDeclarationOutputTypeDef = TypedDict(
    "StageDeclarationOutputTypeDef",
    {
        "name": str,
        "actions": List[ActionDeclarationOutputTypeDef],
        "blockers": NotRequired[List[BlockerDeclarationTypeDef]],
        "onFailure": NotRequired[FailureConditionsOutputTypeDef],
        "onSuccess": NotRequired[SuccessConditionsOutputTypeDef],
        "beforeEntry": NotRequired[BeforeEntryConditionsOutputTypeDef],
    },
)
BeforeEntryConditionsTypeDef = TypedDict(
    "BeforeEntryConditionsTypeDef",
    {
        "conditions": Sequence[ConditionTypeDef],
    },
)
ConditionUnionTypeDef = Union[ConditionTypeDef, ConditionOutputTypeDef]
SuccessConditionsTypeDef = TypedDict(
    "SuccessConditionsTypeDef",
    {
        "conditions": Sequence[ConditionTypeDef],
    },
)
StageStateTypeDef = TypedDict(
    "StageStateTypeDef",
    {
        "stageName": NotRequired[str],
        "inboundExecution": NotRequired[StageExecutionTypeDef],
        "inboundExecutions": NotRequired[List[StageExecutionTypeDef]],
        "inboundTransitionState": NotRequired[TransitionStateTypeDef],
        "actionStates": NotRequired[List[ActionStateTypeDef]],
        "latestExecution": NotRequired[StageExecutionTypeDef],
        "beforeEntryConditionState": NotRequired[StageConditionStateTypeDef],
        "onSuccessConditionState": NotRequired[StageConditionStateTypeDef],
        "onFailureConditionState": NotRequired[StageConditionStateTypeDef],
        "retryStageMetadata": NotRequired[RetryStageMetadataTypeDef],
    },
)
GetJobDetailsOutputTypeDef = TypedDict(
    "GetJobDetailsOutputTypeDef",
    {
        "jobDetails": JobDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PollForJobsOutputTypeDef = TypedDict(
    "PollForJobsOutputTypeDef",
    {
        "jobs": List[JobTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetThirdPartyJobDetailsOutputTypeDef = TypedDict(
    "GetThirdPartyJobDetailsOutputTypeDef",
    {
        "jobDetails": ThirdPartyJobDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GitConfigurationUnionTypeDef = Union[GitConfigurationTypeDef, GitConfigurationOutputTypeDef]
ActionTypeExecutorUnionTypeDef = Union[ActionTypeExecutorTypeDef, ActionTypeExecutorOutputTypeDef]
PipelineDeclarationOutputTypeDef = TypedDict(
    "PipelineDeclarationOutputTypeDef",
    {
        "name": str,
        "roleArn": str,
        "stages": List[StageDeclarationOutputTypeDef],
        "artifactStore": NotRequired[ArtifactStoreTypeDef],
        "artifactStores": NotRequired[Dict[str, ArtifactStoreTypeDef]],
        "version": NotRequired[int],
        "executionMode": NotRequired[ExecutionModeType],
        "pipelineType": NotRequired[PipelineTypeType],
        "variables": NotRequired[List[PipelineVariableDeclarationTypeDef]],
        "triggers": NotRequired[List[PipelineTriggerDeclarationOutputTypeDef]],
    },
)
BeforeEntryConditionsUnionTypeDef = Union[
    BeforeEntryConditionsTypeDef, BeforeEntryConditionsOutputTypeDef
]
FailureConditionsTypeDef = TypedDict(
    "FailureConditionsTypeDef",
    {
        "result": NotRequired[ResultType],
        "retryConfiguration": NotRequired[RetryConfigurationTypeDef],
        "conditions": NotRequired[Sequence[ConditionUnionTypeDef]],
    },
)
SuccessConditionsUnionTypeDef = Union[SuccessConditionsTypeDef, SuccessConditionsOutputTypeDef]
GetPipelineStateOutputTypeDef = TypedDict(
    "GetPipelineStateOutputTypeDef",
    {
        "pipelineName": str,
        "pipelineVersion": int,
        "stageStates": List[StageStateTypeDef],
        "created": datetime,
        "updated": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PipelineTriggerDeclarationTypeDef = TypedDict(
    "PipelineTriggerDeclarationTypeDef",
    {
        "providerType": Literal["CodeStarSourceConnection"],
        "gitConfiguration": GitConfigurationUnionTypeDef,
    },
)
ActionTypeDeclarationTypeDef = TypedDict(
    "ActionTypeDeclarationTypeDef",
    {
        "executor": ActionTypeExecutorUnionTypeDef,
        "id": ActionTypeIdentifierTypeDef,
        "inputArtifactDetails": ActionTypeArtifactDetailsTypeDef,
        "outputArtifactDetails": ActionTypeArtifactDetailsTypeDef,
        "description": NotRequired[str],
        "permissions": NotRequired[ActionTypePermissionsUnionTypeDef],
        "properties": NotRequired[Sequence[ActionTypePropertyTypeDef]],
        "urls": NotRequired[ActionTypeUrlsTypeDef],
    },
)
CreatePipelineOutputTypeDef = TypedDict(
    "CreatePipelineOutputTypeDef",
    {
        "pipeline": PipelineDeclarationOutputTypeDef,
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPipelineOutputTypeDef = TypedDict(
    "GetPipelineOutputTypeDef",
    {
        "pipeline": PipelineDeclarationOutputTypeDef,
        "metadata": PipelineMetadataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePipelineOutputTypeDef = TypedDict(
    "UpdatePipelineOutputTypeDef",
    {
        "pipeline": PipelineDeclarationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FailureConditionsUnionTypeDef = Union[FailureConditionsTypeDef, FailureConditionsOutputTypeDef]
PipelineTriggerDeclarationUnionTypeDef = Union[
    PipelineTriggerDeclarationTypeDef, PipelineTriggerDeclarationOutputTypeDef
]
UpdateActionTypeInputRequestTypeDef = TypedDict(
    "UpdateActionTypeInputRequestTypeDef",
    {
        "actionType": ActionTypeDeclarationTypeDef,
    },
)
StageDeclarationTypeDef = TypedDict(
    "StageDeclarationTypeDef",
    {
        "name": str,
        "actions": Sequence[ActionDeclarationUnionTypeDef],
        "blockers": NotRequired[Sequence[BlockerDeclarationTypeDef]],
        "onFailure": NotRequired[FailureConditionsUnionTypeDef],
        "onSuccess": NotRequired[SuccessConditionsUnionTypeDef],
        "beforeEntry": NotRequired[BeforeEntryConditionsUnionTypeDef],
    },
)
StageDeclarationUnionTypeDef = Union[StageDeclarationTypeDef, StageDeclarationOutputTypeDef]
PipelineDeclarationTypeDef = TypedDict(
    "PipelineDeclarationTypeDef",
    {
        "name": str,
        "roleArn": str,
        "stages": Sequence[StageDeclarationUnionTypeDef],
        "artifactStore": NotRequired[ArtifactStoreTypeDef],
        "artifactStores": NotRequired[Mapping[str, ArtifactStoreTypeDef]],
        "version": NotRequired[int],
        "executionMode": NotRequired[ExecutionModeType],
        "pipelineType": NotRequired[PipelineTypeType],
        "variables": NotRequired[Sequence[PipelineVariableDeclarationTypeDef]],
        "triggers": NotRequired[Sequence[PipelineTriggerDeclarationUnionTypeDef]],
    },
)
CreatePipelineInputRequestTypeDef = TypedDict(
    "CreatePipelineInputRequestTypeDef",
    {
        "pipeline": PipelineDeclarationTypeDef,
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
UpdatePipelineInputRequestTypeDef = TypedDict(
    "UpdatePipelineInputRequestTypeDef",
    {
        "pipeline": PipelineDeclarationTypeDef,
    },
)
