"""
Type annotations for codeconnections service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/type_defs/)

Usage::

    ```python
    from mypy_boto3_codeconnections.type_defs import ConnectionTypeDef

    data: ConnectionTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import (
    BlockerStatusType,
    ConnectionStatusType,
    ProviderTypeType,
    PublishDeploymentStatusType,
    PullRequestCommentType,
    RepositorySyncStatusType,
    ResourceSyncStatusType,
    TriggerResourceUpdateOnType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "ConnectionTypeDef",
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "VpcConfigurationTypeDef",
    "RepositoryLinkInfoTypeDef",
    "CreateSyncConfigurationInputRequestTypeDef",
    "SyncConfigurationTypeDef",
    "DeleteConnectionInputRequestTypeDef",
    "DeleteHostInputRequestTypeDef",
    "DeleteRepositoryLinkInputRequestTypeDef",
    "DeleteSyncConfigurationInputRequestTypeDef",
    "GetConnectionInputRequestTypeDef",
    "GetHostInputRequestTypeDef",
    "VpcConfigurationOutputTypeDef",
    "GetRepositoryLinkInputRequestTypeDef",
    "GetRepositorySyncStatusInputRequestTypeDef",
    "GetResourceSyncStatusInputRequestTypeDef",
    "RevisionTypeDef",
    "GetSyncBlockerSummaryInputRequestTypeDef",
    "GetSyncConfigurationInputRequestTypeDef",
    "ListConnectionsInputRequestTypeDef",
    "ListHostsInputRequestTypeDef",
    "ListRepositoryLinksInputRequestTypeDef",
    "ListRepositorySyncDefinitionsInputRequestTypeDef",
    "RepositorySyncDefinitionTypeDef",
    "ListSyncConfigurationsInputRequestTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "RepositorySyncEventTypeDef",
    "ResourceSyncEventTypeDef",
    "SyncBlockerContextTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateRepositoryLinkInputRequestTypeDef",
    "UpdateSyncBlockerInputRequestTypeDef",
    "UpdateSyncConfigurationInputRequestTypeDef",
    "CreateConnectionInputRequestTypeDef",
    "CreateRepositoryLinkInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "CreateConnectionOutputTypeDef",
    "CreateHostOutputTypeDef",
    "GetConnectionOutputTypeDef",
    "ListConnectionsOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "CreateHostInputRequestTypeDef",
    "UpdateHostInputRequestTypeDef",
    "CreateRepositoryLinkOutputTypeDef",
    "GetRepositoryLinkOutputTypeDef",
    "ListRepositoryLinksOutputTypeDef",
    "UpdateRepositoryLinkOutputTypeDef",
    "CreateSyncConfigurationOutputTypeDef",
    "GetSyncConfigurationOutputTypeDef",
    "ListSyncConfigurationsOutputTypeDef",
    "UpdateSyncConfigurationOutputTypeDef",
    "GetHostOutputTypeDef",
    "HostTypeDef",
    "ListRepositorySyncDefinitionsOutputTypeDef",
    "RepositorySyncAttemptTypeDef",
    "ResourceSyncAttemptTypeDef",
    "SyncBlockerTypeDef",
    "ListHostsOutputTypeDef",
    "GetRepositorySyncStatusOutputTypeDef",
    "GetResourceSyncStatusOutputTypeDef",
    "SyncBlockerSummaryTypeDef",
    "UpdateSyncBlockerOutputTypeDef",
    "GetSyncBlockerSummaryOutputTypeDef",
)

ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "ConnectionName": NotRequired[str],
        "ConnectionArn": NotRequired[str],
        "ProviderType": NotRequired[ProviderTypeType],
        "OwnerAccountId": NotRequired[str],
        "ConnectionStatus": NotRequired[ConnectionStatusType],
        "HostArn": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
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
VpcConfigurationTypeDef = TypedDict(
    "VpcConfigurationTypeDef",
    {
        "VpcId": str,
        "SubnetIds": Sequence[str],
        "SecurityGroupIds": Sequence[str],
        "TlsCertificate": NotRequired[str],
    },
)
RepositoryLinkInfoTypeDef = TypedDict(
    "RepositoryLinkInfoTypeDef",
    {
        "ConnectionArn": str,
        "OwnerId": str,
        "ProviderType": ProviderTypeType,
        "RepositoryLinkArn": str,
        "RepositoryLinkId": str,
        "RepositoryName": str,
        "EncryptionKeyArn": NotRequired[str],
    },
)
CreateSyncConfigurationInputRequestTypeDef = TypedDict(
    "CreateSyncConfigurationInputRequestTypeDef",
    {
        "Branch": str,
        "ConfigFile": str,
        "RepositoryLinkId": str,
        "ResourceName": str,
        "RoleArn": str,
        "SyncType": Literal["CFN_STACK_SYNC"],
        "PublishDeploymentStatus": NotRequired[PublishDeploymentStatusType],
        "TriggerResourceUpdateOn": NotRequired[TriggerResourceUpdateOnType],
        "PullRequestComment": NotRequired[PullRequestCommentType],
    },
)
SyncConfigurationTypeDef = TypedDict(
    "SyncConfigurationTypeDef",
    {
        "Branch": str,
        "OwnerId": str,
        "ProviderType": ProviderTypeType,
        "RepositoryLinkId": str,
        "RepositoryName": str,
        "ResourceName": str,
        "RoleArn": str,
        "SyncType": Literal["CFN_STACK_SYNC"],
        "ConfigFile": NotRequired[str],
        "PublishDeploymentStatus": NotRequired[PublishDeploymentStatusType],
        "TriggerResourceUpdateOn": NotRequired[TriggerResourceUpdateOnType],
        "PullRequestComment": NotRequired[PullRequestCommentType],
    },
)
DeleteConnectionInputRequestTypeDef = TypedDict(
    "DeleteConnectionInputRequestTypeDef",
    {
        "ConnectionArn": str,
    },
)
DeleteHostInputRequestTypeDef = TypedDict(
    "DeleteHostInputRequestTypeDef",
    {
        "HostArn": str,
    },
)
DeleteRepositoryLinkInputRequestTypeDef = TypedDict(
    "DeleteRepositoryLinkInputRequestTypeDef",
    {
        "RepositoryLinkId": str,
    },
)
DeleteSyncConfigurationInputRequestTypeDef = TypedDict(
    "DeleteSyncConfigurationInputRequestTypeDef",
    {
        "SyncType": Literal["CFN_STACK_SYNC"],
        "ResourceName": str,
    },
)
GetConnectionInputRequestTypeDef = TypedDict(
    "GetConnectionInputRequestTypeDef",
    {
        "ConnectionArn": str,
    },
)
GetHostInputRequestTypeDef = TypedDict(
    "GetHostInputRequestTypeDef",
    {
        "HostArn": str,
    },
)
VpcConfigurationOutputTypeDef = TypedDict(
    "VpcConfigurationOutputTypeDef",
    {
        "VpcId": str,
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
        "TlsCertificate": NotRequired[str],
    },
)
GetRepositoryLinkInputRequestTypeDef = TypedDict(
    "GetRepositoryLinkInputRequestTypeDef",
    {
        "RepositoryLinkId": str,
    },
)
GetRepositorySyncStatusInputRequestTypeDef = TypedDict(
    "GetRepositorySyncStatusInputRequestTypeDef",
    {
        "Branch": str,
        "RepositoryLinkId": str,
        "SyncType": Literal["CFN_STACK_SYNC"],
    },
)
GetResourceSyncStatusInputRequestTypeDef = TypedDict(
    "GetResourceSyncStatusInputRequestTypeDef",
    {
        "ResourceName": str,
        "SyncType": Literal["CFN_STACK_SYNC"],
    },
)
RevisionTypeDef = TypedDict(
    "RevisionTypeDef",
    {
        "Branch": str,
        "Directory": str,
        "OwnerId": str,
        "RepositoryName": str,
        "ProviderType": ProviderTypeType,
        "Sha": str,
    },
)
GetSyncBlockerSummaryInputRequestTypeDef = TypedDict(
    "GetSyncBlockerSummaryInputRequestTypeDef",
    {
        "SyncType": Literal["CFN_STACK_SYNC"],
        "ResourceName": str,
    },
)
GetSyncConfigurationInputRequestTypeDef = TypedDict(
    "GetSyncConfigurationInputRequestTypeDef",
    {
        "SyncType": Literal["CFN_STACK_SYNC"],
        "ResourceName": str,
    },
)
ListConnectionsInputRequestTypeDef = TypedDict(
    "ListConnectionsInputRequestTypeDef",
    {
        "ProviderTypeFilter": NotRequired[ProviderTypeType],
        "HostArnFilter": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListHostsInputRequestTypeDef = TypedDict(
    "ListHostsInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListRepositoryLinksInputRequestTypeDef = TypedDict(
    "ListRepositoryLinksInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListRepositorySyncDefinitionsInputRequestTypeDef = TypedDict(
    "ListRepositorySyncDefinitionsInputRequestTypeDef",
    {
        "RepositoryLinkId": str,
        "SyncType": Literal["CFN_STACK_SYNC"],
    },
)
RepositorySyncDefinitionTypeDef = TypedDict(
    "RepositorySyncDefinitionTypeDef",
    {
        "Branch": str,
        "Directory": str,
        "Parent": str,
        "Target": str,
    },
)
ListSyncConfigurationsInputRequestTypeDef = TypedDict(
    "ListSyncConfigurationsInputRequestTypeDef",
    {
        "RepositoryLinkId": str,
        "SyncType": Literal["CFN_STACK_SYNC"],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
RepositorySyncEventTypeDef = TypedDict(
    "RepositorySyncEventTypeDef",
    {
        "Event": str,
        "Time": datetime,
        "Type": str,
        "ExternalId": NotRequired[str],
    },
)
ResourceSyncEventTypeDef = TypedDict(
    "ResourceSyncEventTypeDef",
    {
        "Event": str,
        "Time": datetime,
        "Type": str,
        "ExternalId": NotRequired[str],
    },
)
SyncBlockerContextTypeDef = TypedDict(
    "SyncBlockerContextTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateRepositoryLinkInputRequestTypeDef = TypedDict(
    "UpdateRepositoryLinkInputRequestTypeDef",
    {
        "RepositoryLinkId": str,
        "ConnectionArn": NotRequired[str],
        "EncryptionKeyArn": NotRequired[str],
    },
)
UpdateSyncBlockerInputRequestTypeDef = TypedDict(
    "UpdateSyncBlockerInputRequestTypeDef",
    {
        "Id": str,
        "SyncType": Literal["CFN_STACK_SYNC"],
        "ResourceName": str,
        "ResolvedReason": str,
    },
)
UpdateSyncConfigurationInputRequestTypeDef = TypedDict(
    "UpdateSyncConfigurationInputRequestTypeDef",
    {
        "ResourceName": str,
        "SyncType": Literal["CFN_STACK_SYNC"],
        "Branch": NotRequired[str],
        "ConfigFile": NotRequired[str],
        "RepositoryLinkId": NotRequired[str],
        "RoleArn": NotRequired[str],
        "PublishDeploymentStatus": NotRequired[PublishDeploymentStatusType],
        "TriggerResourceUpdateOn": NotRequired[TriggerResourceUpdateOnType],
        "PullRequestComment": NotRequired[PullRequestCommentType],
    },
)
CreateConnectionInputRequestTypeDef = TypedDict(
    "CreateConnectionInputRequestTypeDef",
    {
        "ConnectionName": str,
        "ProviderType": NotRequired[ProviderTypeType],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "HostArn": NotRequired[str],
    },
)
CreateRepositoryLinkInputRequestTypeDef = TypedDict(
    "CreateRepositoryLinkInputRequestTypeDef",
    {
        "ConnectionArn": str,
        "OwnerId": str,
        "RepositoryName": str,
        "EncryptionKeyArn": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CreateConnectionOutputTypeDef = TypedDict(
    "CreateConnectionOutputTypeDef",
    {
        "ConnectionArn": str,
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateHostOutputTypeDef = TypedDict(
    "CreateHostOutputTypeDef",
    {
        "HostArn": str,
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetConnectionOutputTypeDef = TypedDict(
    "GetConnectionOutputTypeDef",
    {
        "Connection": ConnectionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListConnectionsOutputTypeDef = TypedDict(
    "ListConnectionsOutputTypeDef",
    {
        "Connections": List[ConnectionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateHostInputRequestTypeDef = TypedDict(
    "CreateHostInputRequestTypeDef",
    {
        "Name": str,
        "ProviderType": ProviderTypeType,
        "ProviderEndpoint": str,
        "VpcConfiguration": NotRequired[VpcConfigurationTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
UpdateHostInputRequestTypeDef = TypedDict(
    "UpdateHostInputRequestTypeDef",
    {
        "HostArn": str,
        "ProviderEndpoint": NotRequired[str],
        "VpcConfiguration": NotRequired[VpcConfigurationTypeDef],
    },
)
CreateRepositoryLinkOutputTypeDef = TypedDict(
    "CreateRepositoryLinkOutputTypeDef",
    {
        "RepositoryLinkInfo": RepositoryLinkInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRepositoryLinkOutputTypeDef = TypedDict(
    "GetRepositoryLinkOutputTypeDef",
    {
        "RepositoryLinkInfo": RepositoryLinkInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRepositoryLinksOutputTypeDef = TypedDict(
    "ListRepositoryLinksOutputTypeDef",
    {
        "RepositoryLinks": List[RepositoryLinkInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateRepositoryLinkOutputTypeDef = TypedDict(
    "UpdateRepositoryLinkOutputTypeDef",
    {
        "RepositoryLinkInfo": RepositoryLinkInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSyncConfigurationOutputTypeDef = TypedDict(
    "CreateSyncConfigurationOutputTypeDef",
    {
        "SyncConfiguration": SyncConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSyncConfigurationOutputTypeDef = TypedDict(
    "GetSyncConfigurationOutputTypeDef",
    {
        "SyncConfiguration": SyncConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSyncConfigurationsOutputTypeDef = TypedDict(
    "ListSyncConfigurationsOutputTypeDef",
    {
        "SyncConfigurations": List[SyncConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateSyncConfigurationOutputTypeDef = TypedDict(
    "UpdateSyncConfigurationOutputTypeDef",
    {
        "SyncConfiguration": SyncConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetHostOutputTypeDef = TypedDict(
    "GetHostOutputTypeDef",
    {
        "Name": str,
        "Status": str,
        "ProviderType": ProviderTypeType,
        "ProviderEndpoint": str,
        "VpcConfiguration": VpcConfigurationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
HostTypeDef = TypedDict(
    "HostTypeDef",
    {
        "Name": NotRequired[str],
        "HostArn": NotRequired[str],
        "ProviderType": NotRequired[ProviderTypeType],
        "ProviderEndpoint": NotRequired[str],
        "VpcConfiguration": NotRequired[VpcConfigurationOutputTypeDef],
        "Status": NotRequired[str],
        "StatusMessage": NotRequired[str],
    },
)
ListRepositorySyncDefinitionsOutputTypeDef = TypedDict(
    "ListRepositorySyncDefinitionsOutputTypeDef",
    {
        "RepositorySyncDefinitions": List[RepositorySyncDefinitionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
RepositorySyncAttemptTypeDef = TypedDict(
    "RepositorySyncAttemptTypeDef",
    {
        "StartedAt": datetime,
        "Status": RepositorySyncStatusType,
        "Events": List[RepositorySyncEventTypeDef],
    },
)
ResourceSyncAttemptTypeDef = TypedDict(
    "ResourceSyncAttemptTypeDef",
    {
        "Events": List[ResourceSyncEventTypeDef],
        "InitialRevision": RevisionTypeDef,
        "StartedAt": datetime,
        "Status": ResourceSyncStatusType,
        "TargetRevision": RevisionTypeDef,
        "Target": str,
    },
)
SyncBlockerTypeDef = TypedDict(
    "SyncBlockerTypeDef",
    {
        "Id": str,
        "Type": Literal["AUTOMATED"],
        "Status": BlockerStatusType,
        "CreatedReason": str,
        "CreatedAt": datetime,
        "Contexts": NotRequired[List[SyncBlockerContextTypeDef]],
        "ResolvedReason": NotRequired[str],
        "ResolvedAt": NotRequired[datetime],
    },
)
ListHostsOutputTypeDef = TypedDict(
    "ListHostsOutputTypeDef",
    {
        "Hosts": List[HostTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetRepositorySyncStatusOutputTypeDef = TypedDict(
    "GetRepositorySyncStatusOutputTypeDef",
    {
        "LatestSync": RepositorySyncAttemptTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResourceSyncStatusOutputTypeDef = TypedDict(
    "GetResourceSyncStatusOutputTypeDef",
    {
        "DesiredState": RevisionTypeDef,
        "LatestSuccessfulSync": ResourceSyncAttemptTypeDef,
        "LatestSync": ResourceSyncAttemptTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SyncBlockerSummaryTypeDef = TypedDict(
    "SyncBlockerSummaryTypeDef",
    {
        "ResourceName": str,
        "ParentResourceName": NotRequired[str],
        "LatestBlockers": NotRequired[List[SyncBlockerTypeDef]],
    },
)
UpdateSyncBlockerOutputTypeDef = TypedDict(
    "UpdateSyncBlockerOutputTypeDef",
    {
        "ResourceName": str,
        "ParentResourceName": str,
        "SyncBlocker": SyncBlockerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSyncBlockerSummaryOutputTypeDef = TypedDict(
    "GetSyncBlockerSummaryOutputTypeDef",
    {
        "SyncBlockerSummary": SyncBlockerSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
