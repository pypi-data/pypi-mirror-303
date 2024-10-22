"""
Type annotations for fis service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_fis/type_defs/)

Usage::

    ```python
    from mypy_boto3_fis.type_defs import ActionParameterTypeDef

    data: ActionParameterTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AccountTargetingType,
    ActionsModeType,
    EmptyTargetResolutionModeType,
    ExperimentActionStatusType,
    ExperimentStatusType,
    SafetyLeverStatusInputType,
    SafetyLeverStatusType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "ActionParameterTypeDef",
    "ActionTargetTypeDef",
    "CreateExperimentTemplateActionInputTypeDef",
    "CreateExperimentTemplateExperimentOptionsInputTypeDef",
    "ExperimentTemplateCloudWatchLogsLogConfigurationInputTypeDef",
    "ExperimentTemplateS3LogConfigurationInputTypeDef",
    "CreateExperimentTemplateStopConditionInputTypeDef",
    "ResponseMetadataTypeDef",
    "ExperimentTemplateTargetInputFilterTypeDef",
    "CreateTargetAccountConfigurationRequestRequestTypeDef",
    "TargetAccountConfigurationTypeDef",
    "DeleteExperimentTemplateRequestRequestTypeDef",
    "DeleteTargetAccountConfigurationRequestRequestTypeDef",
    "ExperimentActionStateTypeDef",
    "ExperimentCloudWatchLogsLogConfigurationTypeDef",
    "ExperimentErrorTypeDef",
    "ExperimentS3LogConfigurationTypeDef",
    "ExperimentOptionsTypeDef",
    "ExperimentStopConditionTypeDef",
    "ExperimentTargetAccountConfigurationSummaryTypeDef",
    "ExperimentTargetAccountConfigurationTypeDef",
    "ExperimentTargetFilterTypeDef",
    "ExperimentTemplateActionTypeDef",
    "ExperimentTemplateCloudWatchLogsLogConfigurationTypeDef",
    "ExperimentTemplateExperimentOptionsTypeDef",
    "ExperimentTemplateS3LogConfigurationTypeDef",
    "ExperimentTemplateStopConditionTypeDef",
    "ExperimentTemplateSummaryTypeDef",
    "ExperimentTemplateTargetFilterTypeDef",
    "GetActionRequestRequestTypeDef",
    "GetExperimentRequestRequestTypeDef",
    "GetExperimentTargetAccountConfigurationRequestRequestTypeDef",
    "GetExperimentTemplateRequestRequestTypeDef",
    "GetSafetyLeverRequestRequestTypeDef",
    "GetTargetAccountConfigurationRequestRequestTypeDef",
    "GetTargetResourceTypeRequestRequestTypeDef",
    "ListActionsRequestRequestTypeDef",
    "ListExperimentResolvedTargetsRequestRequestTypeDef",
    "ResolvedTargetTypeDef",
    "ListExperimentTargetAccountConfigurationsRequestRequestTypeDef",
    "ListExperimentTemplatesRequestRequestTypeDef",
    "ListExperimentsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTargetAccountConfigurationsRequestRequestTypeDef",
    "TargetAccountConfigurationSummaryTypeDef",
    "ListTargetResourceTypesRequestRequestTypeDef",
    "TargetResourceTypeSummaryTypeDef",
    "SafetyLeverStateTypeDef",
    "StartExperimentExperimentOptionsInputTypeDef",
    "StopExperimentRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TargetResourceTypeParameterTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateExperimentTemplateActionInputItemTypeDef",
    "UpdateExperimentTemplateExperimentOptionsInputTypeDef",
    "UpdateExperimentTemplateStopConditionInputTypeDef",
    "UpdateSafetyLeverStateInputTypeDef",
    "UpdateTargetAccountConfigurationRequestRequestTypeDef",
    "ActionSummaryTypeDef",
    "ActionTypeDef",
    "CreateExperimentTemplateLogConfigurationInputTypeDef",
    "UpdateExperimentTemplateLogConfigurationInputTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "CreateExperimentTemplateTargetInputTypeDef",
    "UpdateExperimentTemplateTargetInputTypeDef",
    "CreateTargetAccountConfigurationResponseTypeDef",
    "DeleteTargetAccountConfigurationResponseTypeDef",
    "GetTargetAccountConfigurationResponseTypeDef",
    "UpdateTargetAccountConfigurationResponseTypeDef",
    "ExperimentActionTypeDef",
    "ExperimentStateTypeDef",
    "ExperimentLogConfigurationTypeDef",
    "ListExperimentTargetAccountConfigurationsResponseTypeDef",
    "GetExperimentTargetAccountConfigurationResponseTypeDef",
    "ExperimentTargetTypeDef",
    "ExperimentTemplateLogConfigurationTypeDef",
    "ListExperimentTemplatesResponseTypeDef",
    "ExperimentTemplateTargetTypeDef",
    "ListExperimentResolvedTargetsResponseTypeDef",
    "ListTargetAccountConfigurationsResponseTypeDef",
    "ListTargetResourceTypesResponseTypeDef",
    "SafetyLeverTypeDef",
    "StartExperimentRequestRequestTypeDef",
    "TargetResourceTypeTypeDef",
    "UpdateSafetyLeverStateRequestRequestTypeDef",
    "ListActionsResponseTypeDef",
    "GetActionResponseTypeDef",
    "CreateExperimentTemplateRequestRequestTypeDef",
    "UpdateExperimentTemplateRequestRequestTypeDef",
    "ExperimentSummaryTypeDef",
    "ExperimentTypeDef",
    "ExperimentTemplateTypeDef",
    "GetSafetyLeverResponseTypeDef",
    "UpdateSafetyLeverStateResponseTypeDef",
    "GetTargetResourceTypeResponseTypeDef",
    "ListExperimentsResponseTypeDef",
    "GetExperimentResponseTypeDef",
    "StartExperimentResponseTypeDef",
    "StopExperimentResponseTypeDef",
    "CreateExperimentTemplateResponseTypeDef",
    "DeleteExperimentTemplateResponseTypeDef",
    "GetExperimentTemplateResponseTypeDef",
    "UpdateExperimentTemplateResponseTypeDef",
)

ActionParameterTypeDef = TypedDict(
    "ActionParameterTypeDef",
    {
        "description": NotRequired[str],
        "required": NotRequired[bool],
    },
)
ActionTargetTypeDef = TypedDict(
    "ActionTargetTypeDef",
    {
        "resourceType": NotRequired[str],
    },
)
CreateExperimentTemplateActionInputTypeDef = TypedDict(
    "CreateExperimentTemplateActionInputTypeDef",
    {
        "actionId": str,
        "description": NotRequired[str],
        "parameters": NotRequired[Mapping[str, str]],
        "targets": NotRequired[Mapping[str, str]],
        "startAfter": NotRequired[Sequence[str]],
    },
)
CreateExperimentTemplateExperimentOptionsInputTypeDef = TypedDict(
    "CreateExperimentTemplateExperimentOptionsInputTypeDef",
    {
        "accountTargeting": NotRequired[AccountTargetingType],
        "emptyTargetResolutionMode": NotRequired[EmptyTargetResolutionModeType],
    },
)
ExperimentTemplateCloudWatchLogsLogConfigurationInputTypeDef = TypedDict(
    "ExperimentTemplateCloudWatchLogsLogConfigurationInputTypeDef",
    {
        "logGroupArn": str,
    },
)
ExperimentTemplateS3LogConfigurationInputTypeDef = TypedDict(
    "ExperimentTemplateS3LogConfigurationInputTypeDef",
    {
        "bucketName": str,
        "prefix": NotRequired[str],
    },
)
CreateExperimentTemplateStopConditionInputTypeDef = TypedDict(
    "CreateExperimentTemplateStopConditionInputTypeDef",
    {
        "source": str,
        "value": NotRequired[str],
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
ExperimentTemplateTargetInputFilterTypeDef = TypedDict(
    "ExperimentTemplateTargetInputFilterTypeDef",
    {
        "path": str,
        "values": Sequence[str],
    },
)
CreateTargetAccountConfigurationRequestRequestTypeDef = TypedDict(
    "CreateTargetAccountConfigurationRequestRequestTypeDef",
    {
        "experimentTemplateId": str,
        "accountId": str,
        "roleArn": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
    },
)
TargetAccountConfigurationTypeDef = TypedDict(
    "TargetAccountConfigurationTypeDef",
    {
        "roleArn": NotRequired[str],
        "accountId": NotRequired[str],
        "description": NotRequired[str],
    },
)
DeleteExperimentTemplateRequestRequestTypeDef = TypedDict(
    "DeleteExperimentTemplateRequestRequestTypeDef",
    {
        "id": str,
    },
)
DeleteTargetAccountConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteTargetAccountConfigurationRequestRequestTypeDef",
    {
        "experimentTemplateId": str,
        "accountId": str,
    },
)
ExperimentActionStateTypeDef = TypedDict(
    "ExperimentActionStateTypeDef",
    {
        "status": NotRequired[ExperimentActionStatusType],
        "reason": NotRequired[str],
    },
)
ExperimentCloudWatchLogsLogConfigurationTypeDef = TypedDict(
    "ExperimentCloudWatchLogsLogConfigurationTypeDef",
    {
        "logGroupArn": NotRequired[str],
    },
)
ExperimentErrorTypeDef = TypedDict(
    "ExperimentErrorTypeDef",
    {
        "accountId": NotRequired[str],
        "code": NotRequired[str],
        "location": NotRequired[str],
    },
)
ExperimentS3LogConfigurationTypeDef = TypedDict(
    "ExperimentS3LogConfigurationTypeDef",
    {
        "bucketName": NotRequired[str],
        "prefix": NotRequired[str],
    },
)
ExperimentOptionsTypeDef = TypedDict(
    "ExperimentOptionsTypeDef",
    {
        "accountTargeting": NotRequired[AccountTargetingType],
        "emptyTargetResolutionMode": NotRequired[EmptyTargetResolutionModeType],
        "actionsMode": NotRequired[ActionsModeType],
    },
)
ExperimentStopConditionTypeDef = TypedDict(
    "ExperimentStopConditionTypeDef",
    {
        "source": NotRequired[str],
        "value": NotRequired[str],
    },
)
ExperimentTargetAccountConfigurationSummaryTypeDef = TypedDict(
    "ExperimentTargetAccountConfigurationSummaryTypeDef",
    {
        "roleArn": NotRequired[str],
        "accountId": NotRequired[str],
        "description": NotRequired[str],
    },
)
ExperimentTargetAccountConfigurationTypeDef = TypedDict(
    "ExperimentTargetAccountConfigurationTypeDef",
    {
        "roleArn": NotRequired[str],
        "accountId": NotRequired[str],
        "description": NotRequired[str],
    },
)
ExperimentTargetFilterTypeDef = TypedDict(
    "ExperimentTargetFilterTypeDef",
    {
        "path": NotRequired[str],
        "values": NotRequired[List[str]],
    },
)
ExperimentTemplateActionTypeDef = TypedDict(
    "ExperimentTemplateActionTypeDef",
    {
        "actionId": NotRequired[str],
        "description": NotRequired[str],
        "parameters": NotRequired[Dict[str, str]],
        "targets": NotRequired[Dict[str, str]],
        "startAfter": NotRequired[List[str]],
    },
)
ExperimentTemplateCloudWatchLogsLogConfigurationTypeDef = TypedDict(
    "ExperimentTemplateCloudWatchLogsLogConfigurationTypeDef",
    {
        "logGroupArn": NotRequired[str],
    },
)
ExperimentTemplateExperimentOptionsTypeDef = TypedDict(
    "ExperimentTemplateExperimentOptionsTypeDef",
    {
        "accountTargeting": NotRequired[AccountTargetingType],
        "emptyTargetResolutionMode": NotRequired[EmptyTargetResolutionModeType],
    },
)
ExperimentTemplateS3LogConfigurationTypeDef = TypedDict(
    "ExperimentTemplateS3LogConfigurationTypeDef",
    {
        "bucketName": NotRequired[str],
        "prefix": NotRequired[str],
    },
)
ExperimentTemplateStopConditionTypeDef = TypedDict(
    "ExperimentTemplateStopConditionTypeDef",
    {
        "source": NotRequired[str],
        "value": NotRequired[str],
    },
)
ExperimentTemplateSummaryTypeDef = TypedDict(
    "ExperimentTemplateSummaryTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "description": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
    },
)
ExperimentTemplateTargetFilterTypeDef = TypedDict(
    "ExperimentTemplateTargetFilterTypeDef",
    {
        "path": NotRequired[str],
        "values": NotRequired[List[str]],
    },
)
GetActionRequestRequestTypeDef = TypedDict(
    "GetActionRequestRequestTypeDef",
    {
        "id": str,
    },
)
GetExperimentRequestRequestTypeDef = TypedDict(
    "GetExperimentRequestRequestTypeDef",
    {
        "id": str,
    },
)
GetExperimentTargetAccountConfigurationRequestRequestTypeDef = TypedDict(
    "GetExperimentTargetAccountConfigurationRequestRequestTypeDef",
    {
        "experimentId": str,
        "accountId": str,
    },
)
GetExperimentTemplateRequestRequestTypeDef = TypedDict(
    "GetExperimentTemplateRequestRequestTypeDef",
    {
        "id": str,
    },
)
GetSafetyLeverRequestRequestTypeDef = TypedDict(
    "GetSafetyLeverRequestRequestTypeDef",
    {
        "id": str,
    },
)
GetTargetAccountConfigurationRequestRequestTypeDef = TypedDict(
    "GetTargetAccountConfigurationRequestRequestTypeDef",
    {
        "experimentTemplateId": str,
        "accountId": str,
    },
)
GetTargetResourceTypeRequestRequestTypeDef = TypedDict(
    "GetTargetResourceTypeRequestRequestTypeDef",
    {
        "resourceType": str,
    },
)
ListActionsRequestRequestTypeDef = TypedDict(
    "ListActionsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListExperimentResolvedTargetsRequestRequestTypeDef = TypedDict(
    "ListExperimentResolvedTargetsRequestRequestTypeDef",
    {
        "experimentId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "targetName": NotRequired[str],
    },
)
ResolvedTargetTypeDef = TypedDict(
    "ResolvedTargetTypeDef",
    {
        "resourceType": NotRequired[str],
        "targetName": NotRequired[str],
        "targetInformation": NotRequired[Dict[str, str]],
    },
)
ListExperimentTargetAccountConfigurationsRequestRequestTypeDef = TypedDict(
    "ListExperimentTargetAccountConfigurationsRequestRequestTypeDef",
    {
        "experimentId": str,
        "nextToken": NotRequired[str],
    },
)
ListExperimentTemplatesRequestRequestTypeDef = TypedDict(
    "ListExperimentTemplatesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListExperimentsRequestRequestTypeDef = TypedDict(
    "ListExperimentsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "experimentTemplateId": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
ListTargetAccountConfigurationsRequestRequestTypeDef = TypedDict(
    "ListTargetAccountConfigurationsRequestRequestTypeDef",
    {
        "experimentTemplateId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
TargetAccountConfigurationSummaryTypeDef = TypedDict(
    "TargetAccountConfigurationSummaryTypeDef",
    {
        "roleArn": NotRequired[str],
        "accountId": NotRequired[str],
        "description": NotRequired[str],
    },
)
ListTargetResourceTypesRequestRequestTypeDef = TypedDict(
    "ListTargetResourceTypesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
TargetResourceTypeSummaryTypeDef = TypedDict(
    "TargetResourceTypeSummaryTypeDef",
    {
        "resourceType": NotRequired[str],
        "description": NotRequired[str],
    },
)
SafetyLeverStateTypeDef = TypedDict(
    "SafetyLeverStateTypeDef",
    {
        "status": NotRequired[SafetyLeverStatusType],
        "reason": NotRequired[str],
    },
)
StartExperimentExperimentOptionsInputTypeDef = TypedDict(
    "StartExperimentExperimentOptionsInputTypeDef",
    {
        "actionsMode": NotRequired[ActionsModeType],
    },
)
StopExperimentRequestRequestTypeDef = TypedDict(
    "StopExperimentRequestRequestTypeDef",
    {
        "id": str,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)
TargetResourceTypeParameterTypeDef = TypedDict(
    "TargetResourceTypeParameterTypeDef",
    {
        "description": NotRequired[str],
        "required": NotRequired[bool],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": NotRequired[Sequence[str]],
    },
)
UpdateExperimentTemplateActionInputItemTypeDef = TypedDict(
    "UpdateExperimentTemplateActionInputItemTypeDef",
    {
        "actionId": NotRequired[str],
        "description": NotRequired[str],
        "parameters": NotRequired[Mapping[str, str]],
        "targets": NotRequired[Mapping[str, str]],
        "startAfter": NotRequired[Sequence[str]],
    },
)
UpdateExperimentTemplateExperimentOptionsInputTypeDef = TypedDict(
    "UpdateExperimentTemplateExperimentOptionsInputTypeDef",
    {
        "emptyTargetResolutionMode": NotRequired[EmptyTargetResolutionModeType],
    },
)
UpdateExperimentTemplateStopConditionInputTypeDef = TypedDict(
    "UpdateExperimentTemplateStopConditionInputTypeDef",
    {
        "source": str,
        "value": NotRequired[str],
    },
)
UpdateSafetyLeverStateInputTypeDef = TypedDict(
    "UpdateSafetyLeverStateInputTypeDef",
    {
        "status": SafetyLeverStatusInputType,
        "reason": str,
    },
)
UpdateTargetAccountConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateTargetAccountConfigurationRequestRequestTypeDef",
    {
        "experimentTemplateId": str,
        "accountId": str,
        "roleArn": NotRequired[str],
        "description": NotRequired[str],
    },
)
ActionSummaryTypeDef = TypedDict(
    "ActionSummaryTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "description": NotRequired[str],
        "targets": NotRequired[Dict[str, ActionTargetTypeDef]],
        "tags": NotRequired[Dict[str, str]],
    },
)
ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "description": NotRequired[str],
        "parameters": NotRequired[Dict[str, ActionParameterTypeDef]],
        "targets": NotRequired[Dict[str, ActionTargetTypeDef]],
        "tags": NotRequired[Dict[str, str]],
    },
)
CreateExperimentTemplateLogConfigurationInputTypeDef = TypedDict(
    "CreateExperimentTemplateLogConfigurationInputTypeDef",
    {
        "logSchemaVersion": int,
        "cloudWatchLogsConfiguration": NotRequired[
            ExperimentTemplateCloudWatchLogsLogConfigurationInputTypeDef
        ],
        "s3Configuration": NotRequired[ExperimentTemplateS3LogConfigurationInputTypeDef],
    },
)
UpdateExperimentTemplateLogConfigurationInputTypeDef = TypedDict(
    "UpdateExperimentTemplateLogConfigurationInputTypeDef",
    {
        "cloudWatchLogsConfiguration": NotRequired[
            ExperimentTemplateCloudWatchLogsLogConfigurationInputTypeDef
        ],
        "s3Configuration": NotRequired[ExperimentTemplateS3LogConfigurationInputTypeDef],
        "logSchemaVersion": NotRequired[int],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateExperimentTemplateTargetInputTypeDef = TypedDict(
    "CreateExperimentTemplateTargetInputTypeDef",
    {
        "resourceType": str,
        "selectionMode": str,
        "resourceArns": NotRequired[Sequence[str]],
        "resourceTags": NotRequired[Mapping[str, str]],
        "filters": NotRequired[Sequence[ExperimentTemplateTargetInputFilterTypeDef]],
        "parameters": NotRequired[Mapping[str, str]],
    },
)
UpdateExperimentTemplateTargetInputTypeDef = TypedDict(
    "UpdateExperimentTemplateTargetInputTypeDef",
    {
        "resourceType": str,
        "selectionMode": str,
        "resourceArns": NotRequired[Sequence[str]],
        "resourceTags": NotRequired[Mapping[str, str]],
        "filters": NotRequired[Sequence[ExperimentTemplateTargetInputFilterTypeDef]],
        "parameters": NotRequired[Mapping[str, str]],
    },
)
CreateTargetAccountConfigurationResponseTypeDef = TypedDict(
    "CreateTargetAccountConfigurationResponseTypeDef",
    {
        "targetAccountConfiguration": TargetAccountConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTargetAccountConfigurationResponseTypeDef = TypedDict(
    "DeleteTargetAccountConfigurationResponseTypeDef",
    {
        "targetAccountConfiguration": TargetAccountConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTargetAccountConfigurationResponseTypeDef = TypedDict(
    "GetTargetAccountConfigurationResponseTypeDef",
    {
        "targetAccountConfiguration": TargetAccountConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTargetAccountConfigurationResponseTypeDef = TypedDict(
    "UpdateTargetAccountConfigurationResponseTypeDef",
    {
        "targetAccountConfiguration": TargetAccountConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExperimentActionTypeDef = TypedDict(
    "ExperimentActionTypeDef",
    {
        "actionId": NotRequired[str],
        "description": NotRequired[str],
        "parameters": NotRequired[Dict[str, str]],
        "targets": NotRequired[Dict[str, str]],
        "startAfter": NotRequired[List[str]],
        "state": NotRequired[ExperimentActionStateTypeDef],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
    },
)
ExperimentStateTypeDef = TypedDict(
    "ExperimentStateTypeDef",
    {
        "status": NotRequired[ExperimentStatusType],
        "reason": NotRequired[str],
        "error": NotRequired[ExperimentErrorTypeDef],
    },
)
ExperimentLogConfigurationTypeDef = TypedDict(
    "ExperimentLogConfigurationTypeDef",
    {
        "cloudWatchLogsConfiguration": NotRequired[ExperimentCloudWatchLogsLogConfigurationTypeDef],
        "s3Configuration": NotRequired[ExperimentS3LogConfigurationTypeDef],
        "logSchemaVersion": NotRequired[int],
    },
)
ListExperimentTargetAccountConfigurationsResponseTypeDef = TypedDict(
    "ListExperimentTargetAccountConfigurationsResponseTypeDef",
    {
        "targetAccountConfigurations": List[ExperimentTargetAccountConfigurationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetExperimentTargetAccountConfigurationResponseTypeDef = TypedDict(
    "GetExperimentTargetAccountConfigurationResponseTypeDef",
    {
        "targetAccountConfiguration": ExperimentTargetAccountConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExperimentTargetTypeDef = TypedDict(
    "ExperimentTargetTypeDef",
    {
        "resourceType": NotRequired[str],
        "resourceArns": NotRequired[List[str]],
        "resourceTags": NotRequired[Dict[str, str]],
        "filters": NotRequired[List[ExperimentTargetFilterTypeDef]],
        "selectionMode": NotRequired[str],
        "parameters": NotRequired[Dict[str, str]],
    },
)
ExperimentTemplateLogConfigurationTypeDef = TypedDict(
    "ExperimentTemplateLogConfigurationTypeDef",
    {
        "cloudWatchLogsConfiguration": NotRequired[
            ExperimentTemplateCloudWatchLogsLogConfigurationTypeDef
        ],
        "s3Configuration": NotRequired[ExperimentTemplateS3LogConfigurationTypeDef],
        "logSchemaVersion": NotRequired[int],
    },
)
ListExperimentTemplatesResponseTypeDef = TypedDict(
    "ListExperimentTemplatesResponseTypeDef",
    {
        "experimentTemplates": List[ExperimentTemplateSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExperimentTemplateTargetTypeDef = TypedDict(
    "ExperimentTemplateTargetTypeDef",
    {
        "resourceType": NotRequired[str],
        "resourceArns": NotRequired[List[str]],
        "resourceTags": NotRequired[Dict[str, str]],
        "filters": NotRequired[List[ExperimentTemplateTargetFilterTypeDef]],
        "selectionMode": NotRequired[str],
        "parameters": NotRequired[Dict[str, str]],
    },
)
ListExperimentResolvedTargetsResponseTypeDef = TypedDict(
    "ListExperimentResolvedTargetsResponseTypeDef",
    {
        "resolvedTargets": List[ResolvedTargetTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTargetAccountConfigurationsResponseTypeDef = TypedDict(
    "ListTargetAccountConfigurationsResponseTypeDef",
    {
        "targetAccountConfigurations": List[TargetAccountConfigurationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTargetResourceTypesResponseTypeDef = TypedDict(
    "ListTargetResourceTypesResponseTypeDef",
    {
        "targetResourceTypes": List[TargetResourceTypeSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SafetyLeverTypeDef = TypedDict(
    "SafetyLeverTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "state": NotRequired[SafetyLeverStateTypeDef],
    },
)
StartExperimentRequestRequestTypeDef = TypedDict(
    "StartExperimentRequestRequestTypeDef",
    {
        "clientToken": str,
        "experimentTemplateId": str,
        "experimentOptions": NotRequired[StartExperimentExperimentOptionsInputTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
TargetResourceTypeTypeDef = TypedDict(
    "TargetResourceTypeTypeDef",
    {
        "resourceType": NotRequired[str],
        "description": NotRequired[str],
        "parameters": NotRequired[Dict[str, TargetResourceTypeParameterTypeDef]],
    },
)
UpdateSafetyLeverStateRequestRequestTypeDef = TypedDict(
    "UpdateSafetyLeverStateRequestRequestTypeDef",
    {
        "id": str,
        "state": UpdateSafetyLeverStateInputTypeDef,
    },
)
ListActionsResponseTypeDef = TypedDict(
    "ListActionsResponseTypeDef",
    {
        "actions": List[ActionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetActionResponseTypeDef = TypedDict(
    "GetActionResponseTypeDef",
    {
        "action": ActionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateExperimentTemplateRequestRequestTypeDef = TypedDict(
    "CreateExperimentTemplateRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "stopConditions": Sequence[CreateExperimentTemplateStopConditionInputTypeDef],
        "actions": Mapping[str, CreateExperimentTemplateActionInputTypeDef],
        "roleArn": str,
        "targets": NotRequired[Mapping[str, CreateExperimentTemplateTargetInputTypeDef]],
        "tags": NotRequired[Mapping[str, str]],
        "logConfiguration": NotRequired[CreateExperimentTemplateLogConfigurationInputTypeDef],
        "experimentOptions": NotRequired[CreateExperimentTemplateExperimentOptionsInputTypeDef],
    },
)
UpdateExperimentTemplateRequestRequestTypeDef = TypedDict(
    "UpdateExperimentTemplateRequestRequestTypeDef",
    {
        "id": str,
        "description": NotRequired[str],
        "stopConditions": NotRequired[Sequence[UpdateExperimentTemplateStopConditionInputTypeDef]],
        "targets": NotRequired[Mapping[str, UpdateExperimentTemplateTargetInputTypeDef]],
        "actions": NotRequired[Mapping[str, UpdateExperimentTemplateActionInputItemTypeDef]],
        "roleArn": NotRequired[str],
        "logConfiguration": NotRequired[UpdateExperimentTemplateLogConfigurationInputTypeDef],
        "experimentOptions": NotRequired[UpdateExperimentTemplateExperimentOptionsInputTypeDef],
    },
)
ExperimentSummaryTypeDef = TypedDict(
    "ExperimentSummaryTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "experimentTemplateId": NotRequired[str],
        "state": NotRequired[ExperimentStateTypeDef],
        "creationTime": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
        "experimentOptions": NotRequired[ExperimentOptionsTypeDef],
    },
)
ExperimentTypeDef = TypedDict(
    "ExperimentTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "experimentTemplateId": NotRequired[str],
        "roleArn": NotRequired[str],
        "state": NotRequired[ExperimentStateTypeDef],
        "targets": NotRequired[Dict[str, ExperimentTargetTypeDef]],
        "actions": NotRequired[Dict[str, ExperimentActionTypeDef]],
        "stopConditions": NotRequired[List[ExperimentStopConditionTypeDef]],
        "creationTime": NotRequired[datetime],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
        "logConfiguration": NotRequired[ExperimentLogConfigurationTypeDef],
        "experimentOptions": NotRequired[ExperimentOptionsTypeDef],
        "targetAccountConfigurationsCount": NotRequired[int],
    },
)
ExperimentTemplateTypeDef = TypedDict(
    "ExperimentTemplateTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "description": NotRequired[str],
        "targets": NotRequired[Dict[str, ExperimentTemplateTargetTypeDef]],
        "actions": NotRequired[Dict[str, ExperimentTemplateActionTypeDef]],
        "stopConditions": NotRequired[List[ExperimentTemplateStopConditionTypeDef]],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "roleArn": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "logConfiguration": NotRequired[ExperimentTemplateLogConfigurationTypeDef],
        "experimentOptions": NotRequired[ExperimentTemplateExperimentOptionsTypeDef],
        "targetAccountConfigurationsCount": NotRequired[int],
    },
)
GetSafetyLeverResponseTypeDef = TypedDict(
    "GetSafetyLeverResponseTypeDef",
    {
        "safetyLever": SafetyLeverTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSafetyLeverStateResponseTypeDef = TypedDict(
    "UpdateSafetyLeverStateResponseTypeDef",
    {
        "safetyLever": SafetyLeverTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTargetResourceTypeResponseTypeDef = TypedDict(
    "GetTargetResourceTypeResponseTypeDef",
    {
        "targetResourceType": TargetResourceTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListExperimentsResponseTypeDef = TypedDict(
    "ListExperimentsResponseTypeDef",
    {
        "experiments": List[ExperimentSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetExperimentResponseTypeDef = TypedDict(
    "GetExperimentResponseTypeDef",
    {
        "experiment": ExperimentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartExperimentResponseTypeDef = TypedDict(
    "StartExperimentResponseTypeDef",
    {
        "experiment": ExperimentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopExperimentResponseTypeDef = TypedDict(
    "StopExperimentResponseTypeDef",
    {
        "experiment": ExperimentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateExperimentTemplateResponseTypeDef = TypedDict(
    "CreateExperimentTemplateResponseTypeDef",
    {
        "experimentTemplate": ExperimentTemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteExperimentTemplateResponseTypeDef = TypedDict(
    "DeleteExperimentTemplateResponseTypeDef",
    {
        "experimentTemplate": ExperimentTemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetExperimentTemplateResponseTypeDef = TypedDict(
    "GetExperimentTemplateResponseTypeDef",
    {
        "experimentTemplate": ExperimentTemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateExperimentTemplateResponseTypeDef = TypedDict(
    "UpdateExperimentTemplateResponseTypeDef",
    {
        "experimentTemplate": ExperimentTemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
