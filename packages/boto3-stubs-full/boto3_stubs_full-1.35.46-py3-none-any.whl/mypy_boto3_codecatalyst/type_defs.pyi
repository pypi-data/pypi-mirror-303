"""
Type annotations for codecatalyst service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/type_defs/)

Usage::

    ```python
    from mypy_boto3_codecatalyst.type_defs import AccessTokenSummaryTypeDef

    data: AccessTokenSummaryTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    ComparisonOperatorType,
    DevEnvironmentSessionTypeType,
    DevEnvironmentStatusType,
    FilterKeyType,
    InstanceTypeType,
    OperationTypeType,
    UserTypeType,
    WorkflowRunModeType,
    WorkflowRunStatusType,
    WorkflowStatusType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AccessTokenSummaryTypeDef",
    "TimestampTypeDef",
    "ResponseMetadataTypeDef",
    "IdeConfigurationTypeDef",
    "PersistentStorageConfigurationTypeDef",
    "RepositoryInputTypeDef",
    "CreateProjectRequestRequestTypeDef",
    "CreateSourceRepositoryBranchRequestRequestTypeDef",
    "CreateSourceRepositoryRequestRequestTypeDef",
    "DeleteAccessTokenRequestRequestTypeDef",
    "DeleteDevEnvironmentRequestRequestTypeDef",
    "DeleteProjectRequestRequestTypeDef",
    "DeleteSourceRepositoryRequestRequestTypeDef",
    "DeleteSpaceRequestRequestTypeDef",
    "DevEnvironmentAccessDetailsTypeDef",
    "DevEnvironmentRepositorySummaryTypeDef",
    "ExecuteCommandSessionConfigurationTypeDef",
    "DevEnvironmentSessionSummaryTypeDef",
    "IdeTypeDef",
    "PersistentStorageTypeDef",
    "EmailAddressTypeDef",
    "EventPayloadTypeDef",
    "ProjectInformationTypeDef",
    "UserIdentityTypeDef",
    "FilterTypeDef",
    "GetDevEnvironmentRequestRequestTypeDef",
    "GetProjectRequestRequestTypeDef",
    "GetSourceRepositoryCloneUrlsRequestRequestTypeDef",
    "GetSourceRepositoryRequestRequestTypeDef",
    "GetSpaceRequestRequestTypeDef",
    "GetSubscriptionRequestRequestTypeDef",
    "GetUserDetailsRequestRequestTypeDef",
    "GetWorkflowRequestRequestTypeDef",
    "WorkflowDefinitionTypeDef",
    "GetWorkflowRunRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListAccessTokensRequestRequestTypeDef",
    "ListDevEnvironmentSessionsRequestRequestTypeDef",
    "ProjectListFilterTypeDef",
    "ProjectSummaryTypeDef",
    "ListSourceRepositoriesItemTypeDef",
    "ListSourceRepositoriesRequestRequestTypeDef",
    "ListSourceRepositoryBranchesItemTypeDef",
    "ListSourceRepositoryBranchesRequestRequestTypeDef",
    "ListSpacesRequestRequestTypeDef",
    "SpaceSummaryTypeDef",
    "ListWorkflowRunsRequestRequestTypeDef",
    "WorkflowRunSummaryTypeDef",
    "ListWorkflowsRequestRequestTypeDef",
    "StartWorkflowRunRequestRequestTypeDef",
    "StopDevEnvironmentRequestRequestTypeDef",
    "StopDevEnvironmentSessionRequestRequestTypeDef",
    "UpdateProjectRequestRequestTypeDef",
    "UpdateSpaceRequestRequestTypeDef",
    "WorkflowDefinitionSummaryTypeDef",
    "CreateAccessTokenRequestRequestTypeDef",
    "ListEventLogsRequestRequestTypeDef",
    "CreateAccessTokenResponseTypeDef",
    "CreateDevEnvironmentResponseTypeDef",
    "CreateProjectResponseTypeDef",
    "CreateSourceRepositoryBranchResponseTypeDef",
    "CreateSourceRepositoryResponseTypeDef",
    "DeleteDevEnvironmentResponseTypeDef",
    "DeleteProjectResponseTypeDef",
    "DeleteSourceRepositoryResponseTypeDef",
    "DeleteSpaceResponseTypeDef",
    "GetProjectResponseTypeDef",
    "GetSourceRepositoryCloneUrlsResponseTypeDef",
    "GetSourceRepositoryResponseTypeDef",
    "GetSpaceResponseTypeDef",
    "GetSubscriptionResponseTypeDef",
    "GetWorkflowRunResponseTypeDef",
    "ListAccessTokensResponseTypeDef",
    "StartDevEnvironmentResponseTypeDef",
    "StartWorkflowRunResponseTypeDef",
    "StopDevEnvironmentResponseTypeDef",
    "StopDevEnvironmentSessionResponseTypeDef",
    "UpdateProjectResponseTypeDef",
    "UpdateSpaceResponseTypeDef",
    "VerifySessionResponseTypeDef",
    "StartDevEnvironmentRequestRequestTypeDef",
    "UpdateDevEnvironmentRequestRequestTypeDef",
    "UpdateDevEnvironmentResponseTypeDef",
    "CreateDevEnvironmentRequestRequestTypeDef",
    "StartDevEnvironmentSessionResponseTypeDef",
    "DevEnvironmentSessionConfigurationTypeDef",
    "ListDevEnvironmentSessionsResponseTypeDef",
    "DevEnvironmentSummaryTypeDef",
    "GetDevEnvironmentResponseTypeDef",
    "GetUserDetailsResponseTypeDef",
    "EventLogEntryTypeDef",
    "ListDevEnvironmentsRequestRequestTypeDef",
    "GetWorkflowResponseTypeDef",
    "ListAccessTokensRequestListAccessTokensPaginateTypeDef",
    "ListDevEnvironmentSessionsRequestListDevEnvironmentSessionsPaginateTypeDef",
    "ListDevEnvironmentsRequestListDevEnvironmentsPaginateTypeDef",
    "ListEventLogsRequestListEventLogsPaginateTypeDef",
    "ListSourceRepositoriesRequestListSourceRepositoriesPaginateTypeDef",
    "ListSourceRepositoryBranchesRequestListSourceRepositoryBranchesPaginateTypeDef",
    "ListSpacesRequestListSpacesPaginateTypeDef",
    "ListWorkflowRunsRequestListWorkflowRunsPaginateTypeDef",
    "ListWorkflowsRequestListWorkflowsPaginateTypeDef",
    "ListProjectsRequestListProjectsPaginateTypeDef",
    "ListProjectsRequestRequestTypeDef",
    "ListProjectsResponseTypeDef",
    "ListSourceRepositoriesResponseTypeDef",
    "ListSourceRepositoryBranchesResponseTypeDef",
    "ListSpacesResponseTypeDef",
    "ListWorkflowRunsResponseTypeDef",
    "WorkflowSummaryTypeDef",
    "StartDevEnvironmentSessionRequestRequestTypeDef",
    "ListDevEnvironmentsResponseTypeDef",
    "ListEventLogsResponseTypeDef",
    "ListWorkflowsResponseTypeDef",
)

AccessTokenSummaryTypeDef = TypedDict(
    "AccessTokenSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "expiresTime": NotRequired[datetime],
    },
)
TimestampTypeDef = Union[datetime, str]
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
IdeConfigurationTypeDef = TypedDict(
    "IdeConfigurationTypeDef",
    {
        "runtime": NotRequired[str],
        "name": NotRequired[str],
    },
)
PersistentStorageConfigurationTypeDef = TypedDict(
    "PersistentStorageConfigurationTypeDef",
    {
        "sizeInGiB": int,
    },
)
RepositoryInputTypeDef = TypedDict(
    "RepositoryInputTypeDef",
    {
        "repositoryName": str,
        "branchName": NotRequired[str],
    },
)
CreateProjectRequestRequestTypeDef = TypedDict(
    "CreateProjectRequestRequestTypeDef",
    {
        "spaceName": str,
        "displayName": str,
        "description": NotRequired[str],
    },
)
CreateSourceRepositoryBranchRequestRequestTypeDef = TypedDict(
    "CreateSourceRepositoryBranchRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "sourceRepositoryName": str,
        "name": str,
        "headCommitId": NotRequired[str],
    },
)
CreateSourceRepositoryRequestRequestTypeDef = TypedDict(
    "CreateSourceRepositoryRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "name": str,
        "description": NotRequired[str],
    },
)
DeleteAccessTokenRequestRequestTypeDef = TypedDict(
    "DeleteAccessTokenRequestRequestTypeDef",
    {
        "id": str,
    },
)
DeleteDevEnvironmentRequestRequestTypeDef = TypedDict(
    "DeleteDevEnvironmentRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
    },
)
DeleteProjectRequestRequestTypeDef = TypedDict(
    "DeleteProjectRequestRequestTypeDef",
    {
        "spaceName": str,
        "name": str,
    },
)
DeleteSourceRepositoryRequestRequestTypeDef = TypedDict(
    "DeleteSourceRepositoryRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "name": str,
    },
)
DeleteSpaceRequestRequestTypeDef = TypedDict(
    "DeleteSpaceRequestRequestTypeDef",
    {
        "name": str,
    },
)
DevEnvironmentAccessDetailsTypeDef = TypedDict(
    "DevEnvironmentAccessDetailsTypeDef",
    {
        "streamUrl": str,
        "tokenValue": str,
    },
)
DevEnvironmentRepositorySummaryTypeDef = TypedDict(
    "DevEnvironmentRepositorySummaryTypeDef",
    {
        "repositoryName": str,
        "branchName": NotRequired[str],
    },
)
ExecuteCommandSessionConfigurationTypeDef = TypedDict(
    "ExecuteCommandSessionConfigurationTypeDef",
    {
        "command": str,
        "arguments": NotRequired[Sequence[str]],
    },
)
DevEnvironmentSessionSummaryTypeDef = TypedDict(
    "DevEnvironmentSessionSummaryTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "devEnvironmentId": str,
        "startedTime": datetime,
        "id": str,
    },
)
IdeTypeDef = TypedDict(
    "IdeTypeDef",
    {
        "runtime": NotRequired[str],
        "name": NotRequired[str],
    },
)
PersistentStorageTypeDef = TypedDict(
    "PersistentStorageTypeDef",
    {
        "sizeInGiB": int,
    },
)
EmailAddressTypeDef = TypedDict(
    "EmailAddressTypeDef",
    {
        "email": NotRequired[str],
        "verified": NotRequired[bool],
    },
)
EventPayloadTypeDef = TypedDict(
    "EventPayloadTypeDef",
    {
        "contentType": NotRequired[str],
        "data": NotRequired[str],
    },
)
ProjectInformationTypeDef = TypedDict(
    "ProjectInformationTypeDef",
    {
        "name": NotRequired[str],
        "projectId": NotRequired[str],
    },
)
UserIdentityTypeDef = TypedDict(
    "UserIdentityTypeDef",
    {
        "userType": UserTypeType,
        "principalId": str,
        "userName": NotRequired[str],
        "awsAccountId": NotRequired[str],
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "key": str,
        "values": Sequence[str],
        "comparisonOperator": NotRequired[str],
    },
)
GetDevEnvironmentRequestRequestTypeDef = TypedDict(
    "GetDevEnvironmentRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
    },
)
GetProjectRequestRequestTypeDef = TypedDict(
    "GetProjectRequestRequestTypeDef",
    {
        "spaceName": str,
        "name": str,
    },
)
GetSourceRepositoryCloneUrlsRequestRequestTypeDef = TypedDict(
    "GetSourceRepositoryCloneUrlsRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "sourceRepositoryName": str,
    },
)
GetSourceRepositoryRequestRequestTypeDef = TypedDict(
    "GetSourceRepositoryRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "name": str,
    },
)
GetSpaceRequestRequestTypeDef = TypedDict(
    "GetSpaceRequestRequestTypeDef",
    {
        "name": str,
    },
)
GetSubscriptionRequestRequestTypeDef = TypedDict(
    "GetSubscriptionRequestRequestTypeDef",
    {
        "spaceName": str,
    },
)
GetUserDetailsRequestRequestTypeDef = TypedDict(
    "GetUserDetailsRequestRequestTypeDef",
    {
        "id": NotRequired[str],
        "userName": NotRequired[str],
    },
)
GetWorkflowRequestRequestTypeDef = TypedDict(
    "GetWorkflowRequestRequestTypeDef",
    {
        "spaceName": str,
        "id": str,
        "projectName": str,
    },
)
WorkflowDefinitionTypeDef = TypedDict(
    "WorkflowDefinitionTypeDef",
    {
        "path": str,
    },
)
GetWorkflowRunRequestRequestTypeDef = TypedDict(
    "GetWorkflowRunRequestRequestTypeDef",
    {
        "spaceName": str,
        "id": str,
        "projectName": str,
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
ListAccessTokensRequestRequestTypeDef = TypedDict(
    "ListAccessTokensRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListDevEnvironmentSessionsRequestRequestTypeDef = TypedDict(
    "ListDevEnvironmentSessionsRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "devEnvironmentId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ProjectListFilterTypeDef = TypedDict(
    "ProjectListFilterTypeDef",
    {
        "key": FilterKeyType,
        "values": Sequence[str],
        "comparisonOperator": NotRequired[ComparisonOperatorType],
    },
)
ProjectSummaryTypeDef = TypedDict(
    "ProjectSummaryTypeDef",
    {
        "name": str,
        "displayName": NotRequired[str],
        "description": NotRequired[str],
    },
)
ListSourceRepositoriesItemTypeDef = TypedDict(
    "ListSourceRepositoriesItemTypeDef",
    {
        "id": str,
        "name": str,
        "lastUpdatedTime": datetime,
        "createdTime": datetime,
        "description": NotRequired[str],
    },
)
ListSourceRepositoriesRequestRequestTypeDef = TypedDict(
    "ListSourceRepositoriesRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListSourceRepositoryBranchesItemTypeDef = TypedDict(
    "ListSourceRepositoryBranchesItemTypeDef",
    {
        "ref": NotRequired[str],
        "name": NotRequired[str],
        "lastUpdatedTime": NotRequired[datetime],
        "headCommitId": NotRequired[str],
    },
)
ListSourceRepositoryBranchesRequestRequestTypeDef = TypedDict(
    "ListSourceRepositoryBranchesRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "sourceRepositoryName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListSpacesRequestRequestTypeDef = TypedDict(
    "ListSpacesRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
    },
)
SpaceSummaryTypeDef = TypedDict(
    "SpaceSummaryTypeDef",
    {
        "name": str,
        "regionName": str,
        "displayName": NotRequired[str],
        "description": NotRequired[str],
    },
)
ListWorkflowRunsRequestRequestTypeDef = TypedDict(
    "ListWorkflowRunsRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "workflowId": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "sortBy": NotRequired[Sequence[Mapping[str, Any]]],
    },
)
WorkflowRunSummaryTypeDef = TypedDict(
    "WorkflowRunSummaryTypeDef",
    {
        "id": str,
        "workflowId": str,
        "workflowName": str,
        "status": WorkflowRunStatusType,
        "startTime": datetime,
        "lastUpdatedTime": datetime,
        "statusReasons": NotRequired[List[Dict[str, Any]]],
        "endTime": NotRequired[datetime],
    },
)
ListWorkflowsRequestRequestTypeDef = TypedDict(
    "ListWorkflowsRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "sortBy": NotRequired[Sequence[Mapping[str, Any]]],
    },
)
StartWorkflowRunRequestRequestTypeDef = TypedDict(
    "StartWorkflowRunRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "workflowId": str,
        "clientToken": NotRequired[str],
    },
)
StopDevEnvironmentRequestRequestTypeDef = TypedDict(
    "StopDevEnvironmentRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
    },
)
StopDevEnvironmentSessionRequestRequestTypeDef = TypedDict(
    "StopDevEnvironmentSessionRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "sessionId": str,
    },
)
UpdateProjectRequestRequestTypeDef = TypedDict(
    "UpdateProjectRequestRequestTypeDef",
    {
        "spaceName": str,
        "name": str,
        "description": NotRequired[str],
    },
)
UpdateSpaceRequestRequestTypeDef = TypedDict(
    "UpdateSpaceRequestRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
    },
)
WorkflowDefinitionSummaryTypeDef = TypedDict(
    "WorkflowDefinitionSummaryTypeDef",
    {
        "path": str,
    },
)
CreateAccessTokenRequestRequestTypeDef = TypedDict(
    "CreateAccessTokenRequestRequestTypeDef",
    {
        "name": str,
        "expiresTime": NotRequired[TimestampTypeDef],
    },
)
ListEventLogsRequestRequestTypeDef = TypedDict(
    "ListEventLogsRequestRequestTypeDef",
    {
        "spaceName": str,
        "startTime": TimestampTypeDef,
        "endTime": TimestampTypeDef,
        "eventName": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
CreateAccessTokenResponseTypeDef = TypedDict(
    "CreateAccessTokenResponseTypeDef",
    {
        "secret": str,
        "name": str,
        "expiresTime": datetime,
        "accessTokenId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDevEnvironmentResponseTypeDef = TypedDict(
    "CreateDevEnvironmentResponseTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "vpcConnectionName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProjectResponseTypeDef = TypedDict(
    "CreateProjectResponseTypeDef",
    {
        "spaceName": str,
        "name": str,
        "displayName": str,
        "description": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSourceRepositoryBranchResponseTypeDef = TypedDict(
    "CreateSourceRepositoryBranchResponseTypeDef",
    {
        "ref": str,
        "name": str,
        "lastUpdatedTime": datetime,
        "headCommitId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSourceRepositoryResponseTypeDef = TypedDict(
    "CreateSourceRepositoryResponseTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "name": str,
        "description": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDevEnvironmentResponseTypeDef = TypedDict(
    "DeleteDevEnvironmentResponseTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteProjectResponseTypeDef = TypedDict(
    "DeleteProjectResponseTypeDef",
    {
        "spaceName": str,
        "name": str,
        "displayName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteSourceRepositoryResponseTypeDef = TypedDict(
    "DeleteSourceRepositoryResponseTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteSpaceResponseTypeDef = TypedDict(
    "DeleteSpaceResponseTypeDef",
    {
        "name": str,
        "displayName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetProjectResponseTypeDef = TypedDict(
    "GetProjectResponseTypeDef",
    {
        "spaceName": str,
        "name": str,
        "displayName": str,
        "description": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSourceRepositoryCloneUrlsResponseTypeDef = TypedDict(
    "GetSourceRepositoryCloneUrlsResponseTypeDef",
    {
        "https": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSourceRepositoryResponseTypeDef = TypedDict(
    "GetSourceRepositoryResponseTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "name": str,
        "description": str,
        "lastUpdatedTime": datetime,
        "createdTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSpaceResponseTypeDef = TypedDict(
    "GetSpaceResponseTypeDef",
    {
        "name": str,
        "regionName": str,
        "displayName": str,
        "description": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSubscriptionResponseTypeDef = TypedDict(
    "GetSubscriptionResponseTypeDef",
    {
        "subscriptionType": str,
        "awsAccountName": str,
        "pendingSubscriptionType": str,
        "pendingSubscriptionStartTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetWorkflowRunResponseTypeDef = TypedDict(
    "GetWorkflowRunResponseTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "workflowId": str,
        "status": WorkflowRunStatusType,
        "statusReasons": List[Dict[str, Any]],
        "startTime": datetime,
        "endTime": datetime,
        "lastUpdatedTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAccessTokensResponseTypeDef = TypedDict(
    "ListAccessTokensResponseTypeDef",
    {
        "items": List[AccessTokenSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartDevEnvironmentResponseTypeDef = TypedDict(
    "StartDevEnvironmentResponseTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "status": DevEnvironmentStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartWorkflowRunResponseTypeDef = TypedDict(
    "StartWorkflowRunResponseTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "workflowId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopDevEnvironmentResponseTypeDef = TypedDict(
    "StopDevEnvironmentResponseTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "status": DevEnvironmentStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopDevEnvironmentSessionResponseTypeDef = TypedDict(
    "StopDevEnvironmentSessionResponseTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "sessionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateProjectResponseTypeDef = TypedDict(
    "UpdateProjectResponseTypeDef",
    {
        "spaceName": str,
        "name": str,
        "displayName": str,
        "description": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSpaceResponseTypeDef = TypedDict(
    "UpdateSpaceResponseTypeDef",
    {
        "name": str,
        "displayName": str,
        "description": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VerifySessionResponseTypeDef = TypedDict(
    "VerifySessionResponseTypeDef",
    {
        "identity": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartDevEnvironmentRequestRequestTypeDef = TypedDict(
    "StartDevEnvironmentRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "ides": NotRequired[Sequence[IdeConfigurationTypeDef]],
        "instanceType": NotRequired[InstanceTypeType],
        "inactivityTimeoutMinutes": NotRequired[int],
    },
)
UpdateDevEnvironmentRequestRequestTypeDef = TypedDict(
    "UpdateDevEnvironmentRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "alias": NotRequired[str],
        "ides": NotRequired[Sequence[IdeConfigurationTypeDef]],
        "instanceType": NotRequired[InstanceTypeType],
        "inactivityTimeoutMinutes": NotRequired[int],
        "clientToken": NotRequired[str],
    },
)
UpdateDevEnvironmentResponseTypeDef = TypedDict(
    "UpdateDevEnvironmentResponseTypeDef",
    {
        "id": str,
        "spaceName": str,
        "projectName": str,
        "alias": str,
        "ides": List[IdeConfigurationTypeDef],
        "instanceType": InstanceTypeType,
        "inactivityTimeoutMinutes": int,
        "clientToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDevEnvironmentRequestRequestTypeDef = TypedDict(
    "CreateDevEnvironmentRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "instanceType": InstanceTypeType,
        "persistentStorage": PersistentStorageConfigurationTypeDef,
        "repositories": NotRequired[Sequence[RepositoryInputTypeDef]],
        "clientToken": NotRequired[str],
        "alias": NotRequired[str],
        "ides": NotRequired[Sequence[IdeConfigurationTypeDef]],
        "inactivityTimeoutMinutes": NotRequired[int],
        "vpcConnectionName": NotRequired[str],
    },
)
StartDevEnvironmentSessionResponseTypeDef = TypedDict(
    "StartDevEnvironmentSessionResponseTypeDef",
    {
        "accessDetails": DevEnvironmentAccessDetailsTypeDef,
        "sessionId": str,
        "spaceName": str,
        "projectName": str,
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DevEnvironmentSessionConfigurationTypeDef = TypedDict(
    "DevEnvironmentSessionConfigurationTypeDef",
    {
        "sessionType": DevEnvironmentSessionTypeType,
        "executeCommandSessionConfiguration": NotRequired[
            ExecuteCommandSessionConfigurationTypeDef
        ],
    },
)
ListDevEnvironmentSessionsResponseTypeDef = TypedDict(
    "ListDevEnvironmentSessionsResponseTypeDef",
    {
        "items": List[DevEnvironmentSessionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DevEnvironmentSummaryTypeDef = TypedDict(
    "DevEnvironmentSummaryTypeDef",
    {
        "id": str,
        "lastUpdatedTime": datetime,
        "creatorId": str,
        "status": DevEnvironmentStatusType,
        "repositories": List[DevEnvironmentRepositorySummaryTypeDef],
        "instanceType": InstanceTypeType,
        "inactivityTimeoutMinutes": int,
        "persistentStorage": PersistentStorageTypeDef,
        "spaceName": NotRequired[str],
        "projectName": NotRequired[str],
        "statusReason": NotRequired[str],
        "alias": NotRequired[str],
        "ides": NotRequired[List[IdeTypeDef]],
        "vpcConnectionName": NotRequired[str],
    },
)
GetDevEnvironmentResponseTypeDef = TypedDict(
    "GetDevEnvironmentResponseTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "lastUpdatedTime": datetime,
        "creatorId": str,
        "status": DevEnvironmentStatusType,
        "statusReason": str,
        "repositories": List[DevEnvironmentRepositorySummaryTypeDef],
        "alias": str,
        "ides": List[IdeTypeDef],
        "instanceType": InstanceTypeType,
        "inactivityTimeoutMinutes": int,
        "persistentStorage": PersistentStorageTypeDef,
        "vpcConnectionName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetUserDetailsResponseTypeDef = TypedDict(
    "GetUserDetailsResponseTypeDef",
    {
        "userId": str,
        "userName": str,
        "displayName": str,
        "primaryEmail": EmailAddressTypeDef,
        "version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EventLogEntryTypeDef = TypedDict(
    "EventLogEntryTypeDef",
    {
        "id": str,
        "eventName": str,
        "eventType": str,
        "eventCategory": str,
        "eventSource": str,
        "eventTime": datetime,
        "operationType": OperationTypeType,
        "userIdentity": UserIdentityTypeDef,
        "projectInformation": NotRequired[ProjectInformationTypeDef],
        "requestId": NotRequired[str],
        "requestPayload": NotRequired[EventPayloadTypeDef],
        "responsePayload": NotRequired[EventPayloadTypeDef],
        "errorCode": NotRequired[str],
        "sourceIpAddress": NotRequired[str],
        "userAgent": NotRequired[str],
    },
)
ListDevEnvironmentsRequestRequestTypeDef = TypedDict(
    "ListDevEnvironmentsRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": NotRequired[str],
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
GetWorkflowResponseTypeDef = TypedDict(
    "GetWorkflowResponseTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "name": str,
        "sourceRepositoryName": str,
        "sourceBranchName": str,
        "definition": WorkflowDefinitionTypeDef,
        "createdTime": datetime,
        "lastUpdatedTime": datetime,
        "runMode": WorkflowRunModeType,
        "status": WorkflowStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAccessTokensRequestListAccessTokensPaginateTypeDef = TypedDict(
    "ListAccessTokensRequestListAccessTokensPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDevEnvironmentSessionsRequestListDevEnvironmentSessionsPaginateTypeDef = TypedDict(
    "ListDevEnvironmentSessionsRequestListDevEnvironmentSessionsPaginateTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "devEnvironmentId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDevEnvironmentsRequestListDevEnvironmentsPaginateTypeDef = TypedDict(
    "ListDevEnvironmentsRequestListDevEnvironmentsPaginateTypeDef",
    {
        "spaceName": str,
        "projectName": NotRequired[str],
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEventLogsRequestListEventLogsPaginateTypeDef = TypedDict(
    "ListEventLogsRequestListEventLogsPaginateTypeDef",
    {
        "spaceName": str,
        "startTime": TimestampTypeDef,
        "endTime": TimestampTypeDef,
        "eventName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSourceRepositoriesRequestListSourceRepositoriesPaginateTypeDef = TypedDict(
    "ListSourceRepositoriesRequestListSourceRepositoriesPaginateTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSourceRepositoryBranchesRequestListSourceRepositoryBranchesPaginateTypeDef = TypedDict(
    "ListSourceRepositoryBranchesRequestListSourceRepositoryBranchesPaginateTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "sourceRepositoryName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSpacesRequestListSpacesPaginateTypeDef = TypedDict(
    "ListSpacesRequestListSpacesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWorkflowRunsRequestListWorkflowRunsPaginateTypeDef = TypedDict(
    "ListWorkflowRunsRequestListWorkflowRunsPaginateTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "workflowId": NotRequired[str],
        "sortBy": NotRequired[Sequence[Mapping[str, Any]]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWorkflowsRequestListWorkflowsPaginateTypeDef = TypedDict(
    "ListWorkflowsRequestListWorkflowsPaginateTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "sortBy": NotRequired[Sequence[Mapping[str, Any]]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProjectsRequestListProjectsPaginateTypeDef = TypedDict(
    "ListProjectsRequestListProjectsPaginateTypeDef",
    {
        "spaceName": str,
        "filters": NotRequired[Sequence[ProjectListFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProjectsRequestRequestTypeDef = TypedDict(
    "ListProjectsRequestRequestTypeDef",
    {
        "spaceName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "filters": NotRequired[Sequence[ProjectListFilterTypeDef]],
    },
)
ListProjectsResponseTypeDef = TypedDict(
    "ListProjectsResponseTypeDef",
    {
        "nextToken": str,
        "items": List[ProjectSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSourceRepositoriesResponseTypeDef = TypedDict(
    "ListSourceRepositoriesResponseTypeDef",
    {
        "items": List[ListSourceRepositoriesItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSourceRepositoryBranchesResponseTypeDef = TypedDict(
    "ListSourceRepositoryBranchesResponseTypeDef",
    {
        "nextToken": str,
        "items": List[ListSourceRepositoryBranchesItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSpacesResponseTypeDef = TypedDict(
    "ListSpacesResponseTypeDef",
    {
        "nextToken": str,
        "items": List[SpaceSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListWorkflowRunsResponseTypeDef = TypedDict(
    "ListWorkflowRunsResponseTypeDef",
    {
        "nextToken": str,
        "items": List[WorkflowRunSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
WorkflowSummaryTypeDef = TypedDict(
    "WorkflowSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "sourceRepositoryName": str,
        "sourceBranchName": str,
        "definition": WorkflowDefinitionSummaryTypeDef,
        "createdTime": datetime,
        "lastUpdatedTime": datetime,
        "runMode": WorkflowRunModeType,
        "status": WorkflowStatusType,
    },
)
StartDevEnvironmentSessionRequestRequestTypeDef = TypedDict(
    "StartDevEnvironmentSessionRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "sessionConfiguration": DevEnvironmentSessionConfigurationTypeDef,
    },
)
ListDevEnvironmentsResponseTypeDef = TypedDict(
    "ListDevEnvironmentsResponseTypeDef",
    {
        "items": List[DevEnvironmentSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEventLogsResponseTypeDef = TypedDict(
    "ListEventLogsResponseTypeDef",
    {
        "nextToken": str,
        "items": List[EventLogEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListWorkflowsResponseTypeDef = TypedDict(
    "ListWorkflowsResponseTypeDef",
    {
        "nextToken": str,
        "items": List[WorkflowSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
