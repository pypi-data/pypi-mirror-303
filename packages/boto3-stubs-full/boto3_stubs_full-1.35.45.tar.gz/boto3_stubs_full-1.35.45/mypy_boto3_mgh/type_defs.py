"""
Type annotations for mgh service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mgh/type_defs/)

Usage::

    ```python
    from mypy_boto3_mgh.type_defs import ApplicationStateTypeDef

    data: ApplicationStateTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import ApplicationStatusType, ResourceAttributeTypeType, StatusType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "ApplicationStateTypeDef",
    "CreatedArtifactTypeDef",
    "DiscoveredResourceTypeDef",
    "CreateProgressUpdateStreamRequestRequestTypeDef",
    "DeleteProgressUpdateStreamRequestRequestTypeDef",
    "DescribeApplicationStateRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "DescribeMigrationTaskRequestRequestTypeDef",
    "DisassociateCreatedArtifactRequestRequestTypeDef",
    "DisassociateDiscoveredResourceRequestRequestTypeDef",
    "ImportMigrationTaskRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListApplicationStatesRequestRequestTypeDef",
    "ListCreatedArtifactsRequestRequestTypeDef",
    "ListDiscoveredResourcesRequestRequestTypeDef",
    "ListMigrationTasksRequestRequestTypeDef",
    "MigrationTaskSummaryTypeDef",
    "ListProgressUpdateStreamsRequestRequestTypeDef",
    "ProgressUpdateStreamSummaryTypeDef",
    "ResourceAttributeTypeDef",
    "TaskTypeDef",
    "TimestampTypeDef",
    "AssociateCreatedArtifactRequestRequestTypeDef",
    "AssociateDiscoveredResourceRequestRequestTypeDef",
    "DescribeApplicationStateResultTypeDef",
    "ListApplicationStatesResultTypeDef",
    "ListCreatedArtifactsResultTypeDef",
    "ListDiscoveredResourcesResultTypeDef",
    "ListApplicationStatesRequestListApplicationStatesPaginateTypeDef",
    "ListCreatedArtifactsRequestListCreatedArtifactsPaginateTypeDef",
    "ListDiscoveredResourcesRequestListDiscoveredResourcesPaginateTypeDef",
    "ListMigrationTasksRequestListMigrationTasksPaginateTypeDef",
    "ListProgressUpdateStreamsRequestListProgressUpdateStreamsPaginateTypeDef",
    "ListMigrationTasksResultTypeDef",
    "ListProgressUpdateStreamsResultTypeDef",
    "PutResourceAttributesRequestRequestTypeDef",
    "MigrationTaskTypeDef",
    "NotifyApplicationStateRequestRequestTypeDef",
    "NotifyMigrationTaskStateRequestRequestTypeDef",
    "DescribeMigrationTaskResultTypeDef",
)

ApplicationStateTypeDef = TypedDict(
    "ApplicationStateTypeDef",
    {
        "ApplicationId": NotRequired[str],
        "ApplicationStatus": NotRequired[ApplicationStatusType],
        "LastUpdatedTime": NotRequired[datetime],
    },
)
CreatedArtifactTypeDef = TypedDict(
    "CreatedArtifactTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
    },
)
DiscoveredResourceTypeDef = TypedDict(
    "DiscoveredResourceTypeDef",
    {
        "ConfigurationId": str,
        "Description": NotRequired[str],
    },
)
CreateProgressUpdateStreamRequestRequestTypeDef = TypedDict(
    "CreateProgressUpdateStreamRequestRequestTypeDef",
    {
        "ProgressUpdateStreamName": str,
        "DryRun": NotRequired[bool],
    },
)
DeleteProgressUpdateStreamRequestRequestTypeDef = TypedDict(
    "DeleteProgressUpdateStreamRequestRequestTypeDef",
    {
        "ProgressUpdateStreamName": str,
        "DryRun": NotRequired[bool],
    },
)
DescribeApplicationStateRequestRequestTypeDef = TypedDict(
    "DescribeApplicationStateRequestRequestTypeDef",
    {
        "ApplicationId": str,
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
DescribeMigrationTaskRequestRequestTypeDef = TypedDict(
    "DescribeMigrationTaskRequestRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
    },
)
DisassociateCreatedArtifactRequestRequestTypeDef = TypedDict(
    "DisassociateCreatedArtifactRequestRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "CreatedArtifactName": str,
        "DryRun": NotRequired[bool],
    },
)
DisassociateDiscoveredResourceRequestRequestTypeDef = TypedDict(
    "DisassociateDiscoveredResourceRequestRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "ConfigurationId": str,
        "DryRun": NotRequired[bool],
    },
)
ImportMigrationTaskRequestRequestTypeDef = TypedDict(
    "ImportMigrationTaskRequestRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "DryRun": NotRequired[bool],
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
ListApplicationStatesRequestRequestTypeDef = TypedDict(
    "ListApplicationStatesRequestRequestTypeDef",
    {
        "ApplicationIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListCreatedArtifactsRequestRequestTypeDef = TypedDict(
    "ListCreatedArtifactsRequestRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListDiscoveredResourcesRequestRequestTypeDef = TypedDict(
    "ListDiscoveredResourcesRequestRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListMigrationTasksRequestRequestTypeDef = TypedDict(
    "ListMigrationTasksRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ResourceName": NotRequired[str],
    },
)
MigrationTaskSummaryTypeDef = TypedDict(
    "MigrationTaskSummaryTypeDef",
    {
        "ProgressUpdateStream": NotRequired[str],
        "MigrationTaskName": NotRequired[str],
        "Status": NotRequired[StatusType],
        "ProgressPercent": NotRequired[int],
        "StatusDetail": NotRequired[str],
        "UpdateDateTime": NotRequired[datetime],
    },
)
ListProgressUpdateStreamsRequestRequestTypeDef = TypedDict(
    "ListProgressUpdateStreamsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ProgressUpdateStreamSummaryTypeDef = TypedDict(
    "ProgressUpdateStreamSummaryTypeDef",
    {
        "ProgressUpdateStreamName": NotRequired[str],
    },
)
ResourceAttributeTypeDef = TypedDict(
    "ResourceAttributeTypeDef",
    {
        "Type": ResourceAttributeTypeType,
        "Value": str,
    },
)
TaskTypeDef = TypedDict(
    "TaskTypeDef",
    {
        "Status": StatusType,
        "StatusDetail": NotRequired[str],
        "ProgressPercent": NotRequired[int],
    },
)
TimestampTypeDef = Union[datetime, str]
AssociateCreatedArtifactRequestRequestTypeDef = TypedDict(
    "AssociateCreatedArtifactRequestRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "CreatedArtifact": CreatedArtifactTypeDef,
        "DryRun": NotRequired[bool],
    },
)
AssociateDiscoveredResourceRequestRequestTypeDef = TypedDict(
    "AssociateDiscoveredResourceRequestRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "DiscoveredResource": DiscoveredResourceTypeDef,
        "DryRun": NotRequired[bool],
    },
)
DescribeApplicationStateResultTypeDef = TypedDict(
    "DescribeApplicationStateResultTypeDef",
    {
        "ApplicationStatus": ApplicationStatusType,
        "LastUpdatedTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListApplicationStatesResultTypeDef = TypedDict(
    "ListApplicationStatesResultTypeDef",
    {
        "ApplicationStateList": List[ApplicationStateTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListCreatedArtifactsResultTypeDef = TypedDict(
    "ListCreatedArtifactsResultTypeDef",
    {
        "CreatedArtifactList": List[CreatedArtifactTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListDiscoveredResourcesResultTypeDef = TypedDict(
    "ListDiscoveredResourcesResultTypeDef",
    {
        "DiscoveredResourceList": List[DiscoveredResourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListApplicationStatesRequestListApplicationStatesPaginateTypeDef = TypedDict(
    "ListApplicationStatesRequestListApplicationStatesPaginateTypeDef",
    {
        "ApplicationIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCreatedArtifactsRequestListCreatedArtifactsPaginateTypeDef = TypedDict(
    "ListCreatedArtifactsRequestListCreatedArtifactsPaginateTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDiscoveredResourcesRequestListDiscoveredResourcesPaginateTypeDef = TypedDict(
    "ListDiscoveredResourcesRequestListDiscoveredResourcesPaginateTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMigrationTasksRequestListMigrationTasksPaginateTypeDef = TypedDict(
    "ListMigrationTasksRequestListMigrationTasksPaginateTypeDef",
    {
        "ResourceName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProgressUpdateStreamsRequestListProgressUpdateStreamsPaginateTypeDef = TypedDict(
    "ListProgressUpdateStreamsRequestListProgressUpdateStreamsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMigrationTasksResultTypeDef = TypedDict(
    "ListMigrationTasksResultTypeDef",
    {
        "MigrationTaskSummaryList": List[MigrationTaskSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListProgressUpdateStreamsResultTypeDef = TypedDict(
    "ListProgressUpdateStreamsResultTypeDef",
    {
        "ProgressUpdateStreamSummaryList": List[ProgressUpdateStreamSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PutResourceAttributesRequestRequestTypeDef = TypedDict(
    "PutResourceAttributesRequestRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "ResourceAttributeList": Sequence[ResourceAttributeTypeDef],
        "DryRun": NotRequired[bool],
    },
)
MigrationTaskTypeDef = TypedDict(
    "MigrationTaskTypeDef",
    {
        "ProgressUpdateStream": NotRequired[str],
        "MigrationTaskName": NotRequired[str],
        "Task": NotRequired[TaskTypeDef],
        "UpdateDateTime": NotRequired[datetime],
        "ResourceAttributeList": NotRequired[List[ResourceAttributeTypeDef]],
    },
)
NotifyApplicationStateRequestRequestTypeDef = TypedDict(
    "NotifyApplicationStateRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "Status": ApplicationStatusType,
        "UpdateDateTime": NotRequired[TimestampTypeDef],
        "DryRun": NotRequired[bool],
    },
)
NotifyMigrationTaskStateRequestRequestTypeDef = TypedDict(
    "NotifyMigrationTaskStateRequestRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "Task": TaskTypeDef,
        "UpdateDateTime": TimestampTypeDef,
        "NextUpdateSeconds": int,
        "DryRun": NotRequired[bool],
    },
)
DescribeMigrationTaskResultTypeDef = TypedDict(
    "DescribeMigrationTaskResultTypeDef",
    {
        "MigrationTask": MigrationTaskTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
