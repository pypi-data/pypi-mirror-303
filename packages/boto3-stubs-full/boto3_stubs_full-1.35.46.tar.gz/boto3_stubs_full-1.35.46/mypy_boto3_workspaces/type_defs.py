"""
Type annotations for workspaces service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces/type_defs/)

Usage::

    ```python
    from mypy_boto3_workspaces.type_defs import AcceptAccountLinkInvitationRequestRequestTypeDef

    data: AcceptAccountLinkInvitationRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    AccessPropertyValueType,
    AccountLinkStatusEnumType,
    ApplicationAssociatedResourceTypeType,
    ApplicationSettingsStatusEnumType,
    ApplicationType,
    AssociationErrorCodeType,
    AssociationStateType,
    AssociationStatusType,
    BundleTypeType,
    CertificateBasedAuthStatusEnumType,
    ClientDeviceTypeType,
    ComputeType,
    ConnectionAliasStateType,
    ConnectionStateType,
    DataReplicationType,
    DedicatedTenancyAccountTypeType,
    DedicatedTenancyModificationStateEnumType,
    DedicatedTenancySupportResultEnumType,
    DeletableSamlPropertyType,
    DescribeWorkspaceDirectoriesFilterNameType,
    DescribeWorkspacesPoolsFilterOperatorType,
    ImageTypeType,
    LogUploadEnumType,
    ModificationResourceEnumType,
    ModificationStateEnumType,
    OperatingSystemNameType,
    OperatingSystemTypeType,
    ProtocolType,
    ReconnectEnumType,
    RunningModeType,
    SamlStatusEnumType,
    SessionConnectionStateType,
    StandbyWorkspaceRelationshipTypeType,
    StorageConnectorStatusEnumType,
    StreamingExperiencePreferredProtocolEnumType,
    TargetWorkspaceStateType,
    TenancyType,
    UserIdentityTypeType,
    UserSettingActionEnumType,
    UserSettingPermissionEnumType,
    WorkSpaceApplicationLicenseTypeType,
    WorkSpaceApplicationStateType,
    WorkspaceBundleStateType,
    WorkspaceDirectoryStateType,
    WorkspaceDirectoryTypeType,
    WorkspaceImageErrorDetailCodeType,
    WorkspaceImageIngestionProcessType,
    WorkspaceImageRequiredTenancyType,
    WorkspaceImageStateType,
    WorkspacesPoolErrorCodeType,
    WorkspacesPoolStateType,
    WorkspaceStateType,
    WorkspaceTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AcceptAccountLinkInvitationRequestRequestTypeDef",
    "AccountLinkTypeDef",
    "ResponseMetadataTypeDef",
    "AccountModificationTypeDef",
    "ActiveDirectoryConfigTypeDef",
    "AssociationStateReasonTypeDef",
    "ApplicationSettingsRequestTypeDef",
    "ApplicationSettingsResponseTypeDef",
    "AssociateConnectionAliasRequestRequestTypeDef",
    "AssociateIpGroupsRequestRequestTypeDef",
    "AssociateWorkspaceApplicationRequestRequestTypeDef",
    "IpRuleItemTypeDef",
    "BlobTypeDef",
    "CapacityStatusTypeDef",
    "CapacityTypeDef",
    "CertificateBasedAuthPropertiesTypeDef",
    "ClientPropertiesTypeDef",
    "ComputeTypeTypeDef",
    "ConnectClientAddInTypeDef",
    "ConnectionAliasAssociationTypeDef",
    "ConnectionAliasPermissionTypeDef",
    "TagTypeDef",
    "CreateAccountLinkInvitationRequestRequestTypeDef",
    "CreateConnectClientAddInRequestRequestTypeDef",
    "PendingCreateStandbyWorkspacesRequestTypeDef",
    "RootStorageTypeDef",
    "UserStorageTypeDef",
    "OperatingSystemTypeDef",
    "TimeoutSettingsTypeDef",
    "DataReplicationSettingsTypeDef",
    "DefaultClientBrandingAttributesTypeDef",
    "DefaultWorkspaceCreationPropertiesTypeDef",
    "DeleteAccountLinkInvitationRequestRequestTypeDef",
    "DeleteClientBrandingRequestRequestTypeDef",
    "DeleteConnectClientAddInRequestRequestTypeDef",
    "DeleteConnectionAliasRequestRequestTypeDef",
    "DeleteIpGroupRequestRequestTypeDef",
    "DeleteTagsRequestRequestTypeDef",
    "DeleteWorkspaceBundleRequestRequestTypeDef",
    "DeleteWorkspaceImageRequestRequestTypeDef",
    "DeployWorkspaceApplicationsRequestRequestTypeDef",
    "DeregisterWorkspaceDirectoryRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeAccountModificationsRequestRequestTypeDef",
    "DescribeApplicationAssociationsRequestRequestTypeDef",
    "DescribeApplicationsRequestRequestTypeDef",
    "WorkSpaceApplicationTypeDef",
    "DescribeBundleAssociationsRequestRequestTypeDef",
    "DescribeClientBrandingRequestRequestTypeDef",
    "IosClientBrandingAttributesTypeDef",
    "DescribeClientPropertiesRequestRequestTypeDef",
    "DescribeConnectClientAddInsRequestRequestTypeDef",
    "DescribeConnectionAliasPermissionsRequestRequestTypeDef",
    "DescribeConnectionAliasesRequestRequestTypeDef",
    "DescribeImageAssociationsRequestRequestTypeDef",
    "DescribeIpGroupsRequestRequestTypeDef",
    "DescribeTagsRequestRequestTypeDef",
    "DescribeWorkspaceAssociationsRequestRequestTypeDef",
    "DescribeWorkspaceBundlesRequestRequestTypeDef",
    "DescribeWorkspaceDirectoriesFilterTypeDef",
    "DescribeWorkspaceImagePermissionsRequestRequestTypeDef",
    "ImagePermissionTypeDef",
    "DescribeWorkspaceImagesRequestRequestTypeDef",
    "DescribeWorkspaceSnapshotsRequestRequestTypeDef",
    "SnapshotTypeDef",
    "DescribeWorkspacesConnectionStatusRequestRequestTypeDef",
    "WorkspaceConnectionStatusTypeDef",
    "DescribeWorkspacesPoolSessionsRequestRequestTypeDef",
    "DescribeWorkspacesPoolsFilterTypeDef",
    "DescribeWorkspacesRequestRequestTypeDef",
    "DisassociateConnectionAliasRequestRequestTypeDef",
    "DisassociateIpGroupsRequestRequestTypeDef",
    "DisassociateWorkspaceApplicationRequestRequestTypeDef",
    "ErrorDetailsTypeDef",
    "FailedWorkspaceChangeRequestTypeDef",
    "GetAccountLinkRequestRequestTypeDef",
    "IDCConfigTypeDef",
    "ListAccountLinksRequestRequestTypeDef",
    "ListAvailableManagementCidrRangesRequestRequestTypeDef",
    "MicrosoftEntraConfigTypeDef",
    "MigrateWorkspaceRequestRequestTypeDef",
    "ModificationStateTypeDef",
    "ModifyAccountRequestRequestTypeDef",
    "SamlPropertiesTypeDef",
    "SelfservicePermissionsTypeDef",
    "WorkspaceAccessPropertiesTypeDef",
    "WorkspaceCreationPropertiesTypeDef",
    "WorkspacePropertiesTypeDef",
    "ModifyWorkspaceStateRequestRequestTypeDef",
    "NetworkAccessConfigurationTypeDef",
    "RebootRequestTypeDef",
    "RebuildRequestTypeDef",
    "RejectAccountLinkInvitationRequestRequestTypeDef",
    "RelatedWorkspacePropertiesTypeDef",
    "RestoreWorkspaceRequestRequestTypeDef",
    "RevokeIpRulesRequestRequestTypeDef",
    "StandbyWorkspacesPropertiesTypeDef",
    "StartRequestTypeDef",
    "StartWorkspacesPoolRequestRequestTypeDef",
    "StopRequestTypeDef",
    "StopWorkspacesPoolRequestRequestTypeDef",
    "StorageConnectorTypeDef",
    "UserSettingTypeDef",
    "TerminateRequestTypeDef",
    "TerminateWorkspacesPoolRequestRequestTypeDef",
    "TerminateWorkspacesPoolSessionRequestRequestTypeDef",
    "UpdateConnectClientAddInRequestRequestTypeDef",
    "UpdateResultTypeDef",
    "UpdateWorkspaceBundleRequestRequestTypeDef",
    "UpdateWorkspaceImagePermissionRequestRequestTypeDef",
    "WorkspacePropertiesOutputTypeDef",
    "WorkspacesPoolErrorTypeDef",
    "AcceptAccountLinkInvitationResultTypeDef",
    "AssociateConnectionAliasResultTypeDef",
    "CopyWorkspaceImageResultTypeDef",
    "CreateAccountLinkInvitationResultTypeDef",
    "CreateConnectClientAddInResultTypeDef",
    "CreateConnectionAliasResultTypeDef",
    "CreateIpGroupResultTypeDef",
    "CreateUpdatedWorkspaceImageResultTypeDef",
    "DeleteAccountLinkInvitationResultTypeDef",
    "DescribeAccountResultTypeDef",
    "GetAccountLinkResultTypeDef",
    "ImportWorkspaceImageResultTypeDef",
    "ListAccountLinksResultTypeDef",
    "ListAvailableManagementCidrRangesResultTypeDef",
    "MigrateWorkspaceResultTypeDef",
    "RegisterWorkspaceDirectoryResultTypeDef",
    "RejectAccountLinkInvitationResultTypeDef",
    "DescribeAccountModificationsResultTypeDef",
    "ApplicationResourceAssociationTypeDef",
    "BundleResourceAssociationTypeDef",
    "ImageResourceAssociationTypeDef",
    "WorkspaceResourceAssociationTypeDef",
    "AuthorizeIpRulesRequestRequestTypeDef",
    "UpdateRulesOfIpGroupRequestRequestTypeDef",
    "WorkspacesIpGroupTypeDef",
    "DefaultImportClientBrandingAttributesTypeDef",
    "IosImportClientBrandingAttributesTypeDef",
    "ModifyCertificateBasedAuthPropertiesRequestRequestTypeDef",
    "ClientPropertiesResultTypeDef",
    "ModifyClientPropertiesRequestRequestTypeDef",
    "DescribeConnectClientAddInsResultTypeDef",
    "ConnectionAliasTypeDef",
    "DescribeConnectionAliasPermissionsResultTypeDef",
    "UpdateConnectionAliasPermissionRequestRequestTypeDef",
    "CopyWorkspaceImageRequestRequestTypeDef",
    "CreateConnectionAliasRequestRequestTypeDef",
    "CreateIpGroupRequestRequestTypeDef",
    "CreateTagsRequestRequestTypeDef",
    "CreateUpdatedWorkspaceImageRequestRequestTypeDef",
    "CreateWorkspaceImageRequestRequestTypeDef",
    "DescribeTagsResultTypeDef",
    "ImportWorkspaceImageRequestRequestTypeDef",
    "StandbyWorkspaceOutputTypeDef",
    "StandbyWorkspaceTypeDef",
    "CreateWorkspaceBundleRequestRequestTypeDef",
    "WorkspaceBundleTypeDef",
    "CreateWorkspaceImageResultTypeDef",
    "CreateWorkspacesPoolRequestRequestTypeDef",
    "UpdateWorkspacesPoolRequestRequestTypeDef",
    "DescribeAccountModificationsRequestDescribeAccountModificationsPaginateTypeDef",
    "DescribeIpGroupsRequestDescribeIpGroupsPaginateTypeDef",
    "DescribeWorkspaceBundlesRequestDescribeWorkspaceBundlesPaginateTypeDef",
    "DescribeWorkspaceImagesRequestDescribeWorkspaceImagesPaginateTypeDef",
    "DescribeWorkspacesConnectionStatusRequestDescribeWorkspacesConnectionStatusPaginateTypeDef",
    "DescribeWorkspacesRequestDescribeWorkspacesPaginateTypeDef",
    "ListAccountLinksRequestListAccountLinksPaginateTypeDef",
    "ListAvailableManagementCidrRangesRequestListAvailableManagementCidrRangesPaginateTypeDef",
    "DescribeApplicationsResultTypeDef",
    "DescribeClientBrandingResultTypeDef",
    "ImportClientBrandingResultTypeDef",
    "DescribeWorkspaceDirectoriesRequestDescribeWorkspaceDirectoriesPaginateTypeDef",
    "DescribeWorkspaceDirectoriesRequestRequestTypeDef",
    "DescribeWorkspaceImagePermissionsResultTypeDef",
    "DescribeWorkspaceSnapshotsResultTypeDef",
    "DescribeWorkspacesConnectionStatusResultTypeDef",
    "DescribeWorkspacesPoolsRequestRequestTypeDef",
    "RebootWorkspacesResultTypeDef",
    "RebuildWorkspacesResultTypeDef",
    "StartWorkspacesResultTypeDef",
    "StopWorkspacesResultTypeDef",
    "TerminateWorkspacesResultTypeDef",
    "RegisterWorkspaceDirectoryRequestRequestTypeDef",
    "ModifySamlPropertiesRequestRequestTypeDef",
    "ModifySelfservicePermissionsRequestRequestTypeDef",
    "ModifyWorkspaceAccessPropertiesRequestRequestTypeDef",
    "ModifyWorkspaceCreationPropertiesRequestRequestTypeDef",
    "ModifyWorkspacePropertiesRequestRequestTypeDef",
    "WorkspacesPoolSessionTypeDef",
    "RebootWorkspacesRequestRequestTypeDef",
    "RebuildWorkspacesRequestRequestTypeDef",
    "StartWorkspacesRequestRequestTypeDef",
    "StopWorkspacesRequestRequestTypeDef",
    "StreamingPropertiesOutputTypeDef",
    "StreamingPropertiesTypeDef",
    "TerminateWorkspacesRequestRequestTypeDef",
    "WorkspaceImageTypeDef",
    "WorkspacePropertiesUnionTypeDef",
    "WorkspaceRequestOutputTypeDef",
    "WorkspaceTypeDef",
    "WorkspacesPoolTypeDef",
    "DescribeApplicationAssociationsResultTypeDef",
    "DescribeBundleAssociationsResultTypeDef",
    "DescribeImageAssociationsResultTypeDef",
    "AssociateWorkspaceApplicationResultTypeDef",
    "DescribeWorkspaceAssociationsResultTypeDef",
    "DisassociateWorkspaceApplicationResultTypeDef",
    "WorkSpaceApplicationDeploymentTypeDef",
    "DescribeIpGroupsResultTypeDef",
    "ImportClientBrandingRequestRequestTypeDef",
    "DescribeClientPropertiesResultTypeDef",
    "DescribeConnectionAliasesResultTypeDef",
    "FailedCreateStandbyWorkspacesRequestTypeDef",
    "StandbyWorkspaceUnionTypeDef",
    "CreateWorkspaceBundleResultTypeDef",
    "DescribeWorkspaceBundlesResultTypeDef",
    "DescribeWorkspacesPoolSessionsResultTypeDef",
    "WorkspaceDirectoryTypeDef",
    "ModifyStreamingPropertiesRequestRequestTypeDef",
    "DescribeWorkspaceImagesResultTypeDef",
    "WorkspaceRequestTypeDef",
    "FailedCreateWorkspaceRequestTypeDef",
    "DescribeWorkspacesResultTypeDef",
    "CreateWorkspacesPoolResultTypeDef",
    "DescribeWorkspacesPoolsResultTypeDef",
    "UpdateWorkspacesPoolResultTypeDef",
    "DeployWorkspaceApplicationsResultTypeDef",
    "CreateStandbyWorkspacesResultTypeDef",
    "CreateStandbyWorkspacesRequestRequestTypeDef",
    "DescribeWorkspaceDirectoriesResultTypeDef",
    "WorkspaceRequestUnionTypeDef",
    "CreateWorkspacesResultTypeDef",
    "CreateWorkspacesRequestRequestTypeDef",
)

AcceptAccountLinkInvitationRequestRequestTypeDef = TypedDict(
    "AcceptAccountLinkInvitationRequestRequestTypeDef",
    {
        "LinkId": str,
        "ClientToken": NotRequired[str],
    },
)
AccountLinkTypeDef = TypedDict(
    "AccountLinkTypeDef",
    {
        "AccountLinkId": NotRequired[str],
        "AccountLinkStatus": NotRequired[AccountLinkStatusEnumType],
        "SourceAccountId": NotRequired[str],
        "TargetAccountId": NotRequired[str],
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
AccountModificationTypeDef = TypedDict(
    "AccountModificationTypeDef",
    {
        "ModificationState": NotRequired[DedicatedTenancyModificationStateEnumType],
        "DedicatedTenancySupport": NotRequired[DedicatedTenancySupportResultEnumType],
        "DedicatedTenancyManagementCidrRange": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)
ActiveDirectoryConfigTypeDef = TypedDict(
    "ActiveDirectoryConfigTypeDef",
    {
        "DomainName": str,
        "ServiceAccountSecretArn": str,
    },
)
AssociationStateReasonTypeDef = TypedDict(
    "AssociationStateReasonTypeDef",
    {
        "ErrorCode": NotRequired[AssociationErrorCodeType],
        "ErrorMessage": NotRequired[str],
    },
)
ApplicationSettingsRequestTypeDef = TypedDict(
    "ApplicationSettingsRequestTypeDef",
    {
        "Status": ApplicationSettingsStatusEnumType,
        "SettingsGroup": NotRequired[str],
    },
)
ApplicationSettingsResponseTypeDef = TypedDict(
    "ApplicationSettingsResponseTypeDef",
    {
        "Status": ApplicationSettingsStatusEnumType,
        "SettingsGroup": NotRequired[str],
        "S3BucketName": NotRequired[str],
    },
)
AssociateConnectionAliasRequestRequestTypeDef = TypedDict(
    "AssociateConnectionAliasRequestRequestTypeDef",
    {
        "AliasId": str,
        "ResourceId": str,
    },
)
AssociateIpGroupsRequestRequestTypeDef = TypedDict(
    "AssociateIpGroupsRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "GroupIds": Sequence[str],
    },
)
AssociateWorkspaceApplicationRequestRequestTypeDef = TypedDict(
    "AssociateWorkspaceApplicationRequestRequestTypeDef",
    {
        "WorkspaceId": str,
        "ApplicationId": str,
    },
)
IpRuleItemTypeDef = TypedDict(
    "IpRuleItemTypeDef",
    {
        "ipRule": NotRequired[str],
        "ruleDesc": NotRequired[str],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
CapacityStatusTypeDef = TypedDict(
    "CapacityStatusTypeDef",
    {
        "AvailableUserSessions": int,
        "DesiredUserSessions": int,
        "ActualUserSessions": int,
        "ActiveUserSessions": int,
    },
)
CapacityTypeDef = TypedDict(
    "CapacityTypeDef",
    {
        "DesiredUserSessions": int,
    },
)
CertificateBasedAuthPropertiesTypeDef = TypedDict(
    "CertificateBasedAuthPropertiesTypeDef",
    {
        "Status": NotRequired[CertificateBasedAuthStatusEnumType],
        "CertificateAuthorityArn": NotRequired[str],
    },
)
ClientPropertiesTypeDef = TypedDict(
    "ClientPropertiesTypeDef",
    {
        "ReconnectEnabled": NotRequired[ReconnectEnumType],
        "LogUploadEnabled": NotRequired[LogUploadEnumType],
    },
)
ComputeTypeTypeDef = TypedDict(
    "ComputeTypeTypeDef",
    {
        "Name": NotRequired[ComputeType],
    },
)
ConnectClientAddInTypeDef = TypedDict(
    "ConnectClientAddInTypeDef",
    {
        "AddInId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "Name": NotRequired[str],
        "URL": NotRequired[str],
    },
)
ConnectionAliasAssociationTypeDef = TypedDict(
    "ConnectionAliasAssociationTypeDef",
    {
        "AssociationStatus": NotRequired[AssociationStatusType],
        "AssociatedAccountId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ConnectionIdentifier": NotRequired[str],
    },
)
ConnectionAliasPermissionTypeDef = TypedDict(
    "ConnectionAliasPermissionTypeDef",
    {
        "SharedAccountId": str,
        "AllowAssociation": bool,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": NotRequired[str],
    },
)
CreateAccountLinkInvitationRequestRequestTypeDef = TypedDict(
    "CreateAccountLinkInvitationRequestRequestTypeDef",
    {
        "TargetAccountId": str,
        "ClientToken": NotRequired[str],
    },
)
CreateConnectClientAddInRequestRequestTypeDef = TypedDict(
    "CreateConnectClientAddInRequestRequestTypeDef",
    {
        "ResourceId": str,
        "Name": str,
        "URL": str,
    },
)
PendingCreateStandbyWorkspacesRequestTypeDef = TypedDict(
    "PendingCreateStandbyWorkspacesRequestTypeDef",
    {
        "UserName": NotRequired[str],
        "DirectoryId": NotRequired[str],
        "State": NotRequired[WorkspaceStateType],
        "WorkspaceId": NotRequired[str],
    },
)
RootStorageTypeDef = TypedDict(
    "RootStorageTypeDef",
    {
        "Capacity": str,
    },
)
UserStorageTypeDef = TypedDict(
    "UserStorageTypeDef",
    {
        "Capacity": str,
    },
)
OperatingSystemTypeDef = TypedDict(
    "OperatingSystemTypeDef",
    {
        "Type": NotRequired[OperatingSystemTypeType],
    },
)
TimeoutSettingsTypeDef = TypedDict(
    "TimeoutSettingsTypeDef",
    {
        "DisconnectTimeoutInSeconds": NotRequired[int],
        "IdleDisconnectTimeoutInSeconds": NotRequired[int],
        "MaxUserDurationInSeconds": NotRequired[int],
    },
)
DataReplicationSettingsTypeDef = TypedDict(
    "DataReplicationSettingsTypeDef",
    {
        "DataReplication": NotRequired[DataReplicationType],
        "RecoverySnapshotTime": NotRequired[datetime],
    },
)
DefaultClientBrandingAttributesTypeDef = TypedDict(
    "DefaultClientBrandingAttributesTypeDef",
    {
        "LogoUrl": NotRequired[str],
        "SupportEmail": NotRequired[str],
        "SupportLink": NotRequired[str],
        "ForgotPasswordLink": NotRequired[str],
        "LoginMessage": NotRequired[Dict[str, str]],
    },
)
DefaultWorkspaceCreationPropertiesTypeDef = TypedDict(
    "DefaultWorkspaceCreationPropertiesTypeDef",
    {
        "EnableWorkDocs": NotRequired[bool],
        "EnableInternetAccess": NotRequired[bool],
        "DefaultOu": NotRequired[str],
        "CustomSecurityGroupId": NotRequired[str],
        "UserEnabledAsLocalAdministrator": NotRequired[bool],
        "EnableMaintenanceMode": NotRequired[bool],
        "InstanceIamRoleArn": NotRequired[str],
    },
)
DeleteAccountLinkInvitationRequestRequestTypeDef = TypedDict(
    "DeleteAccountLinkInvitationRequestRequestTypeDef",
    {
        "LinkId": str,
        "ClientToken": NotRequired[str],
    },
)
DeleteClientBrandingRequestRequestTypeDef = TypedDict(
    "DeleteClientBrandingRequestRequestTypeDef",
    {
        "ResourceId": str,
        "Platforms": Sequence[ClientDeviceTypeType],
    },
)
DeleteConnectClientAddInRequestRequestTypeDef = TypedDict(
    "DeleteConnectClientAddInRequestRequestTypeDef",
    {
        "AddInId": str,
        "ResourceId": str,
    },
)
DeleteConnectionAliasRequestRequestTypeDef = TypedDict(
    "DeleteConnectionAliasRequestRequestTypeDef",
    {
        "AliasId": str,
    },
)
DeleteIpGroupRequestRequestTypeDef = TypedDict(
    "DeleteIpGroupRequestRequestTypeDef",
    {
        "GroupId": str,
    },
)
DeleteTagsRequestRequestTypeDef = TypedDict(
    "DeleteTagsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "TagKeys": Sequence[str],
    },
)
DeleteWorkspaceBundleRequestRequestTypeDef = TypedDict(
    "DeleteWorkspaceBundleRequestRequestTypeDef",
    {
        "BundleId": NotRequired[str],
    },
)
DeleteWorkspaceImageRequestRequestTypeDef = TypedDict(
    "DeleteWorkspaceImageRequestRequestTypeDef",
    {
        "ImageId": str,
    },
)
DeployWorkspaceApplicationsRequestRequestTypeDef = TypedDict(
    "DeployWorkspaceApplicationsRequestRequestTypeDef",
    {
        "WorkspaceId": str,
        "Force": NotRequired[bool],
    },
)
DeregisterWorkspaceDirectoryRequestRequestTypeDef = TypedDict(
    "DeregisterWorkspaceDirectoryRequestRequestTypeDef",
    {
        "DirectoryId": str,
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
DescribeAccountModificationsRequestRequestTypeDef = TypedDict(
    "DescribeAccountModificationsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)
DescribeApplicationAssociationsRequestRequestTypeDef = TypedDict(
    "DescribeApplicationAssociationsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "AssociatedResourceTypes": Sequence[ApplicationAssociatedResourceTypeType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeApplicationsRequestRequestTypeDef = TypedDict(
    "DescribeApplicationsRequestRequestTypeDef",
    {
        "ApplicationIds": NotRequired[Sequence[str]],
        "ComputeTypeNames": NotRequired[Sequence[ComputeType]],
        "LicenseType": NotRequired[WorkSpaceApplicationLicenseTypeType],
        "OperatingSystemNames": NotRequired[Sequence[OperatingSystemNameType]],
        "Owner": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
WorkSpaceApplicationTypeDef = TypedDict(
    "WorkSpaceApplicationTypeDef",
    {
        "ApplicationId": NotRequired[str],
        "Created": NotRequired[datetime],
        "Description": NotRequired[str],
        "LicenseType": NotRequired[WorkSpaceApplicationLicenseTypeType],
        "Name": NotRequired[str],
        "Owner": NotRequired[str],
        "State": NotRequired[WorkSpaceApplicationStateType],
        "SupportedComputeTypeNames": NotRequired[List[ComputeType]],
        "SupportedOperatingSystemNames": NotRequired[List[OperatingSystemNameType]],
    },
)
DescribeBundleAssociationsRequestRequestTypeDef = TypedDict(
    "DescribeBundleAssociationsRequestRequestTypeDef",
    {
        "BundleId": str,
        "AssociatedResourceTypes": Sequence[Literal["APPLICATION"]],
    },
)
DescribeClientBrandingRequestRequestTypeDef = TypedDict(
    "DescribeClientBrandingRequestRequestTypeDef",
    {
        "ResourceId": str,
    },
)
IosClientBrandingAttributesTypeDef = TypedDict(
    "IosClientBrandingAttributesTypeDef",
    {
        "LogoUrl": NotRequired[str],
        "Logo2xUrl": NotRequired[str],
        "Logo3xUrl": NotRequired[str],
        "SupportEmail": NotRequired[str],
        "SupportLink": NotRequired[str],
        "ForgotPasswordLink": NotRequired[str],
        "LoginMessage": NotRequired[Dict[str, str]],
    },
)
DescribeClientPropertiesRequestRequestTypeDef = TypedDict(
    "DescribeClientPropertiesRequestRequestTypeDef",
    {
        "ResourceIds": Sequence[str],
    },
)
DescribeConnectClientAddInsRequestRequestTypeDef = TypedDict(
    "DescribeConnectClientAddInsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeConnectionAliasPermissionsRequestRequestTypeDef = TypedDict(
    "DescribeConnectionAliasPermissionsRequestRequestTypeDef",
    {
        "AliasId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeConnectionAliasesRequestRequestTypeDef = TypedDict(
    "DescribeConnectionAliasesRequestRequestTypeDef",
    {
        "AliasIds": NotRequired[Sequence[str]],
        "ResourceId": NotRequired[str],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeImageAssociationsRequestRequestTypeDef = TypedDict(
    "DescribeImageAssociationsRequestRequestTypeDef",
    {
        "ImageId": str,
        "AssociatedResourceTypes": Sequence[Literal["APPLICATION"]],
    },
)
DescribeIpGroupsRequestRequestTypeDef = TypedDict(
    "DescribeIpGroupsRequestRequestTypeDef",
    {
        "GroupIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeTagsRequestRequestTypeDef = TypedDict(
    "DescribeTagsRequestRequestTypeDef",
    {
        "ResourceId": str,
    },
)
DescribeWorkspaceAssociationsRequestRequestTypeDef = TypedDict(
    "DescribeWorkspaceAssociationsRequestRequestTypeDef",
    {
        "WorkspaceId": str,
        "AssociatedResourceTypes": Sequence[Literal["APPLICATION"]],
    },
)
DescribeWorkspaceBundlesRequestRequestTypeDef = TypedDict(
    "DescribeWorkspaceBundlesRequestRequestTypeDef",
    {
        "BundleIds": NotRequired[Sequence[str]],
        "Owner": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
DescribeWorkspaceDirectoriesFilterTypeDef = TypedDict(
    "DescribeWorkspaceDirectoriesFilterTypeDef",
    {
        "Name": DescribeWorkspaceDirectoriesFilterNameType,
        "Values": Sequence[str],
    },
)
DescribeWorkspaceImagePermissionsRequestRequestTypeDef = TypedDict(
    "DescribeWorkspaceImagePermissionsRequestRequestTypeDef",
    {
        "ImageId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ImagePermissionTypeDef = TypedDict(
    "ImagePermissionTypeDef",
    {
        "SharedAccountId": NotRequired[str],
    },
)
DescribeWorkspaceImagesRequestRequestTypeDef = TypedDict(
    "DescribeWorkspaceImagesRequestRequestTypeDef",
    {
        "ImageIds": NotRequired[Sequence[str]],
        "ImageType": NotRequired[ImageTypeType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeWorkspaceSnapshotsRequestRequestTypeDef = TypedDict(
    "DescribeWorkspaceSnapshotsRequestRequestTypeDef",
    {
        "WorkspaceId": str,
    },
)
SnapshotTypeDef = TypedDict(
    "SnapshotTypeDef",
    {
        "SnapshotTime": NotRequired[datetime],
    },
)
DescribeWorkspacesConnectionStatusRequestRequestTypeDef = TypedDict(
    "DescribeWorkspacesConnectionStatusRequestRequestTypeDef",
    {
        "WorkspaceIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
    },
)
WorkspaceConnectionStatusTypeDef = TypedDict(
    "WorkspaceConnectionStatusTypeDef",
    {
        "WorkspaceId": NotRequired[str],
        "ConnectionState": NotRequired[ConnectionStateType],
        "ConnectionStateCheckTimestamp": NotRequired[datetime],
        "LastKnownUserConnectionTimestamp": NotRequired[datetime],
    },
)
DescribeWorkspacesPoolSessionsRequestRequestTypeDef = TypedDict(
    "DescribeWorkspacesPoolSessionsRequestRequestTypeDef",
    {
        "PoolId": str,
        "UserId": NotRequired[str],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeWorkspacesPoolsFilterTypeDef = TypedDict(
    "DescribeWorkspacesPoolsFilterTypeDef",
    {
        "Name": Literal["PoolName"],
        "Values": Sequence[str],
        "Operator": DescribeWorkspacesPoolsFilterOperatorType,
    },
)
DescribeWorkspacesRequestRequestTypeDef = TypedDict(
    "DescribeWorkspacesRequestRequestTypeDef",
    {
        "WorkspaceIds": NotRequired[Sequence[str]],
        "DirectoryId": NotRequired[str],
        "UserName": NotRequired[str],
        "BundleId": NotRequired[str],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
        "WorkspaceName": NotRequired[str],
    },
)
DisassociateConnectionAliasRequestRequestTypeDef = TypedDict(
    "DisassociateConnectionAliasRequestRequestTypeDef",
    {
        "AliasId": str,
    },
)
DisassociateIpGroupsRequestRequestTypeDef = TypedDict(
    "DisassociateIpGroupsRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "GroupIds": Sequence[str],
    },
)
DisassociateWorkspaceApplicationRequestRequestTypeDef = TypedDict(
    "DisassociateWorkspaceApplicationRequestRequestTypeDef",
    {
        "WorkspaceId": str,
        "ApplicationId": str,
    },
)
ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef",
    {
        "ErrorCode": NotRequired[WorkspaceImageErrorDetailCodeType],
        "ErrorMessage": NotRequired[str],
    },
)
FailedWorkspaceChangeRequestTypeDef = TypedDict(
    "FailedWorkspaceChangeRequestTypeDef",
    {
        "WorkspaceId": NotRequired[str],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)
GetAccountLinkRequestRequestTypeDef = TypedDict(
    "GetAccountLinkRequestRequestTypeDef",
    {
        "LinkId": NotRequired[str],
        "LinkedAccountId": NotRequired[str],
    },
)
IDCConfigTypeDef = TypedDict(
    "IDCConfigTypeDef",
    {
        "InstanceArn": NotRequired[str],
        "ApplicationArn": NotRequired[str],
    },
)
ListAccountLinksRequestRequestTypeDef = TypedDict(
    "ListAccountLinksRequestRequestTypeDef",
    {
        "LinkStatusFilter": NotRequired[Sequence[AccountLinkStatusEnumType]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListAvailableManagementCidrRangesRequestRequestTypeDef = TypedDict(
    "ListAvailableManagementCidrRangesRequestRequestTypeDef",
    {
        "ManagementCidrRangeConstraint": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
MicrosoftEntraConfigTypeDef = TypedDict(
    "MicrosoftEntraConfigTypeDef",
    {
        "TenantId": NotRequired[str],
        "ApplicationConfigSecretArn": NotRequired[str],
    },
)
MigrateWorkspaceRequestRequestTypeDef = TypedDict(
    "MigrateWorkspaceRequestRequestTypeDef",
    {
        "SourceWorkspaceId": str,
        "BundleId": str,
    },
)
ModificationStateTypeDef = TypedDict(
    "ModificationStateTypeDef",
    {
        "Resource": NotRequired[ModificationResourceEnumType],
        "State": NotRequired[ModificationStateEnumType],
    },
)
ModifyAccountRequestRequestTypeDef = TypedDict(
    "ModifyAccountRequestRequestTypeDef",
    {
        "DedicatedTenancySupport": NotRequired[Literal["ENABLED"]],
        "DedicatedTenancyManagementCidrRange": NotRequired[str],
    },
)
SamlPropertiesTypeDef = TypedDict(
    "SamlPropertiesTypeDef",
    {
        "Status": NotRequired[SamlStatusEnumType],
        "UserAccessUrl": NotRequired[str],
        "RelayStateParameterName": NotRequired[str],
    },
)
SelfservicePermissionsTypeDef = TypedDict(
    "SelfservicePermissionsTypeDef",
    {
        "RestartWorkspace": NotRequired[ReconnectEnumType],
        "IncreaseVolumeSize": NotRequired[ReconnectEnumType],
        "ChangeComputeType": NotRequired[ReconnectEnumType],
        "SwitchRunningMode": NotRequired[ReconnectEnumType],
        "RebuildWorkspace": NotRequired[ReconnectEnumType],
    },
)
WorkspaceAccessPropertiesTypeDef = TypedDict(
    "WorkspaceAccessPropertiesTypeDef",
    {
        "DeviceTypeWindows": NotRequired[AccessPropertyValueType],
        "DeviceTypeOsx": NotRequired[AccessPropertyValueType],
        "DeviceTypeWeb": NotRequired[AccessPropertyValueType],
        "DeviceTypeIos": NotRequired[AccessPropertyValueType],
        "DeviceTypeAndroid": NotRequired[AccessPropertyValueType],
        "DeviceTypeChromeOs": NotRequired[AccessPropertyValueType],
        "DeviceTypeZeroClient": NotRequired[AccessPropertyValueType],
        "DeviceTypeLinux": NotRequired[AccessPropertyValueType],
    },
)
WorkspaceCreationPropertiesTypeDef = TypedDict(
    "WorkspaceCreationPropertiesTypeDef",
    {
        "EnableWorkDocs": NotRequired[bool],
        "EnableInternetAccess": NotRequired[bool],
        "DefaultOu": NotRequired[str],
        "CustomSecurityGroupId": NotRequired[str],
        "UserEnabledAsLocalAdministrator": NotRequired[bool],
        "EnableMaintenanceMode": NotRequired[bool],
        "InstanceIamRoleArn": NotRequired[str],
    },
)
WorkspacePropertiesTypeDef = TypedDict(
    "WorkspacePropertiesTypeDef",
    {
        "RunningMode": NotRequired[RunningModeType],
        "RunningModeAutoStopTimeoutInMinutes": NotRequired[int],
        "RootVolumeSizeGib": NotRequired[int],
        "UserVolumeSizeGib": NotRequired[int],
        "ComputeTypeName": NotRequired[ComputeType],
        "Protocols": NotRequired[Sequence[ProtocolType]],
        "OperatingSystemName": NotRequired[OperatingSystemNameType],
    },
)
ModifyWorkspaceStateRequestRequestTypeDef = TypedDict(
    "ModifyWorkspaceStateRequestRequestTypeDef",
    {
        "WorkspaceId": str,
        "WorkspaceState": TargetWorkspaceStateType,
    },
)
NetworkAccessConfigurationTypeDef = TypedDict(
    "NetworkAccessConfigurationTypeDef",
    {
        "EniPrivateIpAddress": NotRequired[str],
        "EniId": NotRequired[str],
    },
)
RebootRequestTypeDef = TypedDict(
    "RebootRequestTypeDef",
    {
        "WorkspaceId": str,
    },
)
RebuildRequestTypeDef = TypedDict(
    "RebuildRequestTypeDef",
    {
        "WorkspaceId": str,
    },
)
RejectAccountLinkInvitationRequestRequestTypeDef = TypedDict(
    "RejectAccountLinkInvitationRequestRequestTypeDef",
    {
        "LinkId": str,
        "ClientToken": NotRequired[str],
    },
)
RelatedWorkspacePropertiesTypeDef = TypedDict(
    "RelatedWorkspacePropertiesTypeDef",
    {
        "WorkspaceId": NotRequired[str],
        "Region": NotRequired[str],
        "State": NotRequired[WorkspaceStateType],
        "Type": NotRequired[StandbyWorkspaceRelationshipTypeType],
    },
)
RestoreWorkspaceRequestRequestTypeDef = TypedDict(
    "RestoreWorkspaceRequestRequestTypeDef",
    {
        "WorkspaceId": str,
    },
)
RevokeIpRulesRequestRequestTypeDef = TypedDict(
    "RevokeIpRulesRequestRequestTypeDef",
    {
        "GroupId": str,
        "UserRules": Sequence[str],
    },
)
StandbyWorkspacesPropertiesTypeDef = TypedDict(
    "StandbyWorkspacesPropertiesTypeDef",
    {
        "StandbyWorkspaceId": NotRequired[str],
        "DataReplication": NotRequired[DataReplicationType],
        "RecoverySnapshotTime": NotRequired[datetime],
    },
)
StartRequestTypeDef = TypedDict(
    "StartRequestTypeDef",
    {
        "WorkspaceId": NotRequired[str],
    },
)
StartWorkspacesPoolRequestRequestTypeDef = TypedDict(
    "StartWorkspacesPoolRequestRequestTypeDef",
    {
        "PoolId": str,
    },
)
StopRequestTypeDef = TypedDict(
    "StopRequestTypeDef",
    {
        "WorkspaceId": NotRequired[str],
    },
)
StopWorkspacesPoolRequestRequestTypeDef = TypedDict(
    "StopWorkspacesPoolRequestRequestTypeDef",
    {
        "PoolId": str,
    },
)
StorageConnectorTypeDef = TypedDict(
    "StorageConnectorTypeDef",
    {
        "ConnectorType": Literal["HOME_FOLDER"],
        "Status": StorageConnectorStatusEnumType,
    },
)
UserSettingTypeDef = TypedDict(
    "UserSettingTypeDef",
    {
        "Action": UserSettingActionEnumType,
        "Permission": UserSettingPermissionEnumType,
        "MaximumLength": NotRequired[int],
    },
)
TerminateRequestTypeDef = TypedDict(
    "TerminateRequestTypeDef",
    {
        "WorkspaceId": str,
    },
)
TerminateWorkspacesPoolRequestRequestTypeDef = TypedDict(
    "TerminateWorkspacesPoolRequestRequestTypeDef",
    {
        "PoolId": str,
    },
)
TerminateWorkspacesPoolSessionRequestRequestTypeDef = TypedDict(
    "TerminateWorkspacesPoolSessionRequestRequestTypeDef",
    {
        "SessionId": str,
    },
)
UpdateConnectClientAddInRequestRequestTypeDef = TypedDict(
    "UpdateConnectClientAddInRequestRequestTypeDef",
    {
        "AddInId": str,
        "ResourceId": str,
        "Name": NotRequired[str],
        "URL": NotRequired[str],
    },
)
UpdateResultTypeDef = TypedDict(
    "UpdateResultTypeDef",
    {
        "UpdateAvailable": NotRequired[bool],
        "Description": NotRequired[str],
    },
)
UpdateWorkspaceBundleRequestRequestTypeDef = TypedDict(
    "UpdateWorkspaceBundleRequestRequestTypeDef",
    {
        "BundleId": NotRequired[str],
        "ImageId": NotRequired[str],
    },
)
UpdateWorkspaceImagePermissionRequestRequestTypeDef = TypedDict(
    "UpdateWorkspaceImagePermissionRequestRequestTypeDef",
    {
        "ImageId": str,
        "AllowCopyImage": bool,
        "SharedAccountId": str,
    },
)
WorkspacePropertiesOutputTypeDef = TypedDict(
    "WorkspacePropertiesOutputTypeDef",
    {
        "RunningMode": NotRequired[RunningModeType],
        "RunningModeAutoStopTimeoutInMinutes": NotRequired[int],
        "RootVolumeSizeGib": NotRequired[int],
        "UserVolumeSizeGib": NotRequired[int],
        "ComputeTypeName": NotRequired[ComputeType],
        "Protocols": NotRequired[List[ProtocolType]],
        "OperatingSystemName": NotRequired[OperatingSystemNameType],
    },
)
WorkspacesPoolErrorTypeDef = TypedDict(
    "WorkspacesPoolErrorTypeDef",
    {
        "ErrorCode": NotRequired[WorkspacesPoolErrorCodeType],
        "ErrorMessage": NotRequired[str],
    },
)
AcceptAccountLinkInvitationResultTypeDef = TypedDict(
    "AcceptAccountLinkInvitationResultTypeDef",
    {
        "AccountLink": AccountLinkTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateConnectionAliasResultTypeDef = TypedDict(
    "AssociateConnectionAliasResultTypeDef",
    {
        "ConnectionIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CopyWorkspaceImageResultTypeDef = TypedDict(
    "CopyWorkspaceImageResultTypeDef",
    {
        "ImageId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAccountLinkInvitationResultTypeDef = TypedDict(
    "CreateAccountLinkInvitationResultTypeDef",
    {
        "AccountLink": AccountLinkTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateConnectClientAddInResultTypeDef = TypedDict(
    "CreateConnectClientAddInResultTypeDef",
    {
        "AddInId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateConnectionAliasResultTypeDef = TypedDict(
    "CreateConnectionAliasResultTypeDef",
    {
        "AliasId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateIpGroupResultTypeDef = TypedDict(
    "CreateIpGroupResultTypeDef",
    {
        "GroupId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateUpdatedWorkspaceImageResultTypeDef = TypedDict(
    "CreateUpdatedWorkspaceImageResultTypeDef",
    {
        "ImageId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteAccountLinkInvitationResultTypeDef = TypedDict(
    "DeleteAccountLinkInvitationResultTypeDef",
    {
        "AccountLink": AccountLinkTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAccountResultTypeDef = TypedDict(
    "DescribeAccountResultTypeDef",
    {
        "DedicatedTenancySupport": DedicatedTenancySupportResultEnumType,
        "DedicatedTenancyManagementCidrRange": str,
        "DedicatedTenancyAccountType": DedicatedTenancyAccountTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAccountLinkResultTypeDef = TypedDict(
    "GetAccountLinkResultTypeDef",
    {
        "AccountLink": AccountLinkTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportWorkspaceImageResultTypeDef = TypedDict(
    "ImportWorkspaceImageResultTypeDef",
    {
        "ImageId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAccountLinksResultTypeDef = TypedDict(
    "ListAccountLinksResultTypeDef",
    {
        "AccountLinks": List[AccountLinkTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListAvailableManagementCidrRangesResultTypeDef = TypedDict(
    "ListAvailableManagementCidrRangesResultTypeDef",
    {
        "ManagementCidrRanges": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
MigrateWorkspaceResultTypeDef = TypedDict(
    "MigrateWorkspaceResultTypeDef",
    {
        "SourceWorkspaceId": str,
        "TargetWorkspaceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterWorkspaceDirectoryResultTypeDef = TypedDict(
    "RegisterWorkspaceDirectoryResultTypeDef",
    {
        "DirectoryId": str,
        "State": WorkspaceDirectoryStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RejectAccountLinkInvitationResultTypeDef = TypedDict(
    "RejectAccountLinkInvitationResultTypeDef",
    {
        "AccountLink": AccountLinkTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAccountModificationsResultTypeDef = TypedDict(
    "DescribeAccountModificationsResultTypeDef",
    {
        "AccountModifications": List[AccountModificationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ApplicationResourceAssociationTypeDef = TypedDict(
    "ApplicationResourceAssociationTypeDef",
    {
        "ApplicationId": NotRequired[str],
        "AssociatedResourceId": NotRequired[str],
        "AssociatedResourceType": NotRequired[ApplicationAssociatedResourceTypeType],
        "Created": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "State": NotRequired[AssociationStateType],
        "StateReason": NotRequired[AssociationStateReasonTypeDef],
    },
)
BundleResourceAssociationTypeDef = TypedDict(
    "BundleResourceAssociationTypeDef",
    {
        "AssociatedResourceId": NotRequired[str],
        "AssociatedResourceType": NotRequired[Literal["APPLICATION"]],
        "BundleId": NotRequired[str],
        "Created": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "State": NotRequired[AssociationStateType],
        "StateReason": NotRequired[AssociationStateReasonTypeDef],
    },
)
ImageResourceAssociationTypeDef = TypedDict(
    "ImageResourceAssociationTypeDef",
    {
        "AssociatedResourceId": NotRequired[str],
        "AssociatedResourceType": NotRequired[Literal["APPLICATION"]],
        "Created": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "ImageId": NotRequired[str],
        "State": NotRequired[AssociationStateType],
        "StateReason": NotRequired[AssociationStateReasonTypeDef],
    },
)
WorkspaceResourceAssociationTypeDef = TypedDict(
    "WorkspaceResourceAssociationTypeDef",
    {
        "AssociatedResourceId": NotRequired[str],
        "AssociatedResourceType": NotRequired[Literal["APPLICATION"]],
        "Created": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "State": NotRequired[AssociationStateType],
        "StateReason": NotRequired[AssociationStateReasonTypeDef],
        "WorkspaceId": NotRequired[str],
    },
)
AuthorizeIpRulesRequestRequestTypeDef = TypedDict(
    "AuthorizeIpRulesRequestRequestTypeDef",
    {
        "GroupId": str,
        "UserRules": Sequence[IpRuleItemTypeDef],
    },
)
UpdateRulesOfIpGroupRequestRequestTypeDef = TypedDict(
    "UpdateRulesOfIpGroupRequestRequestTypeDef",
    {
        "GroupId": str,
        "UserRules": Sequence[IpRuleItemTypeDef],
    },
)
WorkspacesIpGroupTypeDef = TypedDict(
    "WorkspacesIpGroupTypeDef",
    {
        "groupId": NotRequired[str],
        "groupName": NotRequired[str],
        "groupDesc": NotRequired[str],
        "userRules": NotRequired[List[IpRuleItemTypeDef]],
    },
)
DefaultImportClientBrandingAttributesTypeDef = TypedDict(
    "DefaultImportClientBrandingAttributesTypeDef",
    {
        "Logo": NotRequired[BlobTypeDef],
        "SupportEmail": NotRequired[str],
        "SupportLink": NotRequired[str],
        "ForgotPasswordLink": NotRequired[str],
        "LoginMessage": NotRequired[Mapping[str, str]],
    },
)
IosImportClientBrandingAttributesTypeDef = TypedDict(
    "IosImportClientBrandingAttributesTypeDef",
    {
        "Logo": NotRequired[BlobTypeDef],
        "Logo2x": NotRequired[BlobTypeDef],
        "Logo3x": NotRequired[BlobTypeDef],
        "SupportEmail": NotRequired[str],
        "SupportLink": NotRequired[str],
        "ForgotPasswordLink": NotRequired[str],
        "LoginMessage": NotRequired[Mapping[str, str]],
    },
)
ModifyCertificateBasedAuthPropertiesRequestRequestTypeDef = TypedDict(
    "ModifyCertificateBasedAuthPropertiesRequestRequestTypeDef",
    {
        "ResourceId": str,
        "CertificateBasedAuthProperties": NotRequired[CertificateBasedAuthPropertiesTypeDef],
        "PropertiesToDelete": NotRequired[
            Sequence[Literal["CERTIFICATE_BASED_AUTH_PROPERTIES_CERTIFICATE_AUTHORITY_ARN"]]
        ],
    },
)
ClientPropertiesResultTypeDef = TypedDict(
    "ClientPropertiesResultTypeDef",
    {
        "ResourceId": NotRequired[str],
        "ClientProperties": NotRequired[ClientPropertiesTypeDef],
    },
)
ModifyClientPropertiesRequestRequestTypeDef = TypedDict(
    "ModifyClientPropertiesRequestRequestTypeDef",
    {
        "ResourceId": str,
        "ClientProperties": ClientPropertiesTypeDef,
    },
)
DescribeConnectClientAddInsResultTypeDef = TypedDict(
    "DescribeConnectClientAddInsResultTypeDef",
    {
        "AddIns": List[ConnectClientAddInTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ConnectionAliasTypeDef = TypedDict(
    "ConnectionAliasTypeDef",
    {
        "ConnectionString": NotRequired[str],
        "AliasId": NotRequired[str],
        "State": NotRequired[ConnectionAliasStateType],
        "OwnerAccountId": NotRequired[str],
        "Associations": NotRequired[List[ConnectionAliasAssociationTypeDef]],
    },
)
DescribeConnectionAliasPermissionsResultTypeDef = TypedDict(
    "DescribeConnectionAliasPermissionsResultTypeDef",
    {
        "AliasId": str,
        "ConnectionAliasPermissions": List[ConnectionAliasPermissionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateConnectionAliasPermissionRequestRequestTypeDef = TypedDict(
    "UpdateConnectionAliasPermissionRequestRequestTypeDef",
    {
        "AliasId": str,
        "ConnectionAliasPermission": ConnectionAliasPermissionTypeDef,
    },
)
CopyWorkspaceImageRequestRequestTypeDef = TypedDict(
    "CopyWorkspaceImageRequestRequestTypeDef",
    {
        "Name": str,
        "SourceImageId": str,
        "SourceRegion": str,
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateConnectionAliasRequestRequestTypeDef = TypedDict(
    "CreateConnectionAliasRequestRequestTypeDef",
    {
        "ConnectionString": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateIpGroupRequestRequestTypeDef = TypedDict(
    "CreateIpGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "GroupDesc": NotRequired[str],
        "UserRules": NotRequired[Sequence[IpRuleItemTypeDef]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateTagsRequestRequestTypeDef = TypedDict(
    "CreateTagsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CreateUpdatedWorkspaceImageRequestRequestTypeDef = TypedDict(
    "CreateUpdatedWorkspaceImageRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "SourceImageId": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateWorkspaceImageRequestRequestTypeDef = TypedDict(
    "CreateWorkspaceImageRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "WorkspaceId": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
DescribeTagsResultTypeDef = TypedDict(
    "DescribeTagsResultTypeDef",
    {
        "TagList": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportWorkspaceImageRequestRequestTypeDef = TypedDict(
    "ImportWorkspaceImageRequestRequestTypeDef",
    {
        "Ec2ImageId": str,
        "IngestionProcess": WorkspaceImageIngestionProcessType,
        "ImageName": str,
        "ImageDescription": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "Applications": NotRequired[Sequence[ApplicationType]],
    },
)
StandbyWorkspaceOutputTypeDef = TypedDict(
    "StandbyWorkspaceOutputTypeDef",
    {
        "PrimaryWorkspaceId": str,
        "DirectoryId": str,
        "VolumeEncryptionKey": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "DataReplication": NotRequired[DataReplicationType],
    },
)
StandbyWorkspaceTypeDef = TypedDict(
    "StandbyWorkspaceTypeDef",
    {
        "PrimaryWorkspaceId": str,
        "DirectoryId": str,
        "VolumeEncryptionKey": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "DataReplication": NotRequired[DataReplicationType],
    },
)
CreateWorkspaceBundleRequestRequestTypeDef = TypedDict(
    "CreateWorkspaceBundleRequestRequestTypeDef",
    {
        "BundleName": str,
        "BundleDescription": str,
        "ImageId": str,
        "ComputeType": ComputeTypeTypeDef,
        "UserStorage": UserStorageTypeDef,
        "RootStorage": NotRequired[RootStorageTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
WorkspaceBundleTypeDef = TypedDict(
    "WorkspaceBundleTypeDef",
    {
        "BundleId": NotRequired[str],
        "Name": NotRequired[str],
        "Owner": NotRequired[str],
        "Description": NotRequired[str],
        "ImageId": NotRequired[str],
        "RootStorage": NotRequired[RootStorageTypeDef],
        "UserStorage": NotRequired[UserStorageTypeDef],
        "ComputeType": NotRequired[ComputeTypeTypeDef],
        "LastUpdatedTime": NotRequired[datetime],
        "CreationTime": NotRequired[datetime],
        "State": NotRequired[WorkspaceBundleStateType],
        "BundleType": NotRequired[BundleTypeType],
    },
)
CreateWorkspaceImageResultTypeDef = TypedDict(
    "CreateWorkspaceImageResultTypeDef",
    {
        "ImageId": str,
        "Name": str,
        "Description": str,
        "OperatingSystem": OperatingSystemTypeDef,
        "State": WorkspaceImageStateType,
        "RequiredTenancy": WorkspaceImageRequiredTenancyType,
        "Created": datetime,
        "OwnerAccountId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWorkspacesPoolRequestRequestTypeDef = TypedDict(
    "CreateWorkspacesPoolRequestRequestTypeDef",
    {
        "PoolName": str,
        "Description": str,
        "BundleId": str,
        "DirectoryId": str,
        "Capacity": CapacityTypeDef,
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ApplicationSettings": NotRequired[ApplicationSettingsRequestTypeDef],
        "TimeoutSettings": NotRequired[TimeoutSettingsTypeDef],
    },
)
UpdateWorkspacesPoolRequestRequestTypeDef = TypedDict(
    "UpdateWorkspacesPoolRequestRequestTypeDef",
    {
        "PoolId": str,
        "Description": NotRequired[str],
        "BundleId": NotRequired[str],
        "DirectoryId": NotRequired[str],
        "Capacity": NotRequired[CapacityTypeDef],
        "ApplicationSettings": NotRequired[ApplicationSettingsRequestTypeDef],
        "TimeoutSettings": NotRequired[TimeoutSettingsTypeDef],
    },
)
DescribeAccountModificationsRequestDescribeAccountModificationsPaginateTypeDef = TypedDict(
    "DescribeAccountModificationsRequestDescribeAccountModificationsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeIpGroupsRequestDescribeIpGroupsPaginateTypeDef = TypedDict(
    "DescribeIpGroupsRequestDescribeIpGroupsPaginateTypeDef",
    {
        "GroupIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeWorkspaceBundlesRequestDescribeWorkspaceBundlesPaginateTypeDef = TypedDict(
    "DescribeWorkspaceBundlesRequestDescribeWorkspaceBundlesPaginateTypeDef",
    {
        "BundleIds": NotRequired[Sequence[str]],
        "Owner": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeWorkspaceImagesRequestDescribeWorkspaceImagesPaginateTypeDef = TypedDict(
    "DescribeWorkspaceImagesRequestDescribeWorkspaceImagesPaginateTypeDef",
    {
        "ImageIds": NotRequired[Sequence[str]],
        "ImageType": NotRequired[ImageTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeWorkspacesConnectionStatusRequestDescribeWorkspacesConnectionStatusPaginateTypeDef = TypedDict(
    "DescribeWorkspacesConnectionStatusRequestDescribeWorkspacesConnectionStatusPaginateTypeDef",
    {
        "WorkspaceIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeWorkspacesRequestDescribeWorkspacesPaginateTypeDef = TypedDict(
    "DescribeWorkspacesRequestDescribeWorkspacesPaginateTypeDef",
    {
        "WorkspaceIds": NotRequired[Sequence[str]],
        "DirectoryId": NotRequired[str],
        "UserName": NotRequired[str],
        "BundleId": NotRequired[str],
        "WorkspaceName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAccountLinksRequestListAccountLinksPaginateTypeDef = TypedDict(
    "ListAccountLinksRequestListAccountLinksPaginateTypeDef",
    {
        "LinkStatusFilter": NotRequired[Sequence[AccountLinkStatusEnumType]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAvailableManagementCidrRangesRequestListAvailableManagementCidrRangesPaginateTypeDef = (
    TypedDict(
        "ListAvailableManagementCidrRangesRequestListAvailableManagementCidrRangesPaginateTypeDef",
        {
            "ManagementCidrRangeConstraint": str,
            "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
        },
    )
)
DescribeApplicationsResultTypeDef = TypedDict(
    "DescribeApplicationsResultTypeDef",
    {
        "Applications": List[WorkSpaceApplicationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeClientBrandingResultTypeDef = TypedDict(
    "DescribeClientBrandingResultTypeDef",
    {
        "DeviceTypeWindows": DefaultClientBrandingAttributesTypeDef,
        "DeviceTypeOsx": DefaultClientBrandingAttributesTypeDef,
        "DeviceTypeAndroid": DefaultClientBrandingAttributesTypeDef,
        "DeviceTypeIos": IosClientBrandingAttributesTypeDef,
        "DeviceTypeLinux": DefaultClientBrandingAttributesTypeDef,
        "DeviceTypeWeb": DefaultClientBrandingAttributesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportClientBrandingResultTypeDef = TypedDict(
    "ImportClientBrandingResultTypeDef",
    {
        "DeviceTypeWindows": DefaultClientBrandingAttributesTypeDef,
        "DeviceTypeOsx": DefaultClientBrandingAttributesTypeDef,
        "DeviceTypeAndroid": DefaultClientBrandingAttributesTypeDef,
        "DeviceTypeIos": IosClientBrandingAttributesTypeDef,
        "DeviceTypeLinux": DefaultClientBrandingAttributesTypeDef,
        "DeviceTypeWeb": DefaultClientBrandingAttributesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeWorkspaceDirectoriesRequestDescribeWorkspaceDirectoriesPaginateTypeDef = TypedDict(
    "DescribeWorkspaceDirectoriesRequestDescribeWorkspaceDirectoriesPaginateTypeDef",
    {
        "DirectoryIds": NotRequired[Sequence[str]],
        "WorkspaceDirectoryNames": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "Filters": NotRequired[Sequence[DescribeWorkspaceDirectoriesFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeWorkspaceDirectoriesRequestRequestTypeDef = TypedDict(
    "DescribeWorkspaceDirectoriesRequestRequestTypeDef",
    {
        "DirectoryIds": NotRequired[Sequence[str]],
        "WorkspaceDirectoryNames": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence[DescribeWorkspaceDirectoriesFilterTypeDef]],
    },
)
DescribeWorkspaceImagePermissionsResultTypeDef = TypedDict(
    "DescribeWorkspaceImagePermissionsResultTypeDef",
    {
        "ImageId": str,
        "ImagePermissions": List[ImagePermissionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeWorkspaceSnapshotsResultTypeDef = TypedDict(
    "DescribeWorkspaceSnapshotsResultTypeDef",
    {
        "RebuildSnapshots": List[SnapshotTypeDef],
        "RestoreSnapshots": List[SnapshotTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeWorkspacesConnectionStatusResultTypeDef = TypedDict(
    "DescribeWorkspacesConnectionStatusResultTypeDef",
    {
        "WorkspacesConnectionStatus": List[WorkspaceConnectionStatusTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeWorkspacesPoolsRequestRequestTypeDef = TypedDict(
    "DescribeWorkspacesPoolsRequestRequestTypeDef",
    {
        "PoolIds": NotRequired[Sequence[str]],
        "Filters": NotRequired[Sequence[DescribeWorkspacesPoolsFilterTypeDef]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
RebootWorkspacesResultTypeDef = TypedDict(
    "RebootWorkspacesResultTypeDef",
    {
        "FailedRequests": List[FailedWorkspaceChangeRequestTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RebuildWorkspacesResultTypeDef = TypedDict(
    "RebuildWorkspacesResultTypeDef",
    {
        "FailedRequests": List[FailedWorkspaceChangeRequestTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartWorkspacesResultTypeDef = TypedDict(
    "StartWorkspacesResultTypeDef",
    {
        "FailedRequests": List[FailedWorkspaceChangeRequestTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopWorkspacesResultTypeDef = TypedDict(
    "StopWorkspacesResultTypeDef",
    {
        "FailedRequests": List[FailedWorkspaceChangeRequestTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TerminateWorkspacesResultTypeDef = TypedDict(
    "TerminateWorkspacesResultTypeDef",
    {
        "FailedRequests": List[FailedWorkspaceChangeRequestTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterWorkspaceDirectoryRequestRequestTypeDef = TypedDict(
    "RegisterWorkspaceDirectoryRequestRequestTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "SubnetIds": NotRequired[Sequence[str]],
        "EnableWorkDocs": NotRequired[bool],
        "EnableSelfService": NotRequired[bool],
        "Tenancy": NotRequired[TenancyType],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "WorkspaceDirectoryName": NotRequired[str],
        "WorkspaceDirectoryDescription": NotRequired[str],
        "UserIdentityType": NotRequired[UserIdentityTypeType],
        "IdcInstanceArn": NotRequired[str],
        "MicrosoftEntraConfig": NotRequired[MicrosoftEntraConfigTypeDef],
        "WorkspaceType": NotRequired[WorkspaceTypeType],
        "ActiveDirectoryConfig": NotRequired[ActiveDirectoryConfigTypeDef],
    },
)
ModifySamlPropertiesRequestRequestTypeDef = TypedDict(
    "ModifySamlPropertiesRequestRequestTypeDef",
    {
        "ResourceId": str,
        "SamlProperties": NotRequired[SamlPropertiesTypeDef],
        "PropertiesToDelete": NotRequired[Sequence[DeletableSamlPropertyType]],
    },
)
ModifySelfservicePermissionsRequestRequestTypeDef = TypedDict(
    "ModifySelfservicePermissionsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "SelfservicePermissions": SelfservicePermissionsTypeDef,
    },
)
ModifyWorkspaceAccessPropertiesRequestRequestTypeDef = TypedDict(
    "ModifyWorkspaceAccessPropertiesRequestRequestTypeDef",
    {
        "ResourceId": str,
        "WorkspaceAccessProperties": WorkspaceAccessPropertiesTypeDef,
    },
)
ModifyWorkspaceCreationPropertiesRequestRequestTypeDef = TypedDict(
    "ModifyWorkspaceCreationPropertiesRequestRequestTypeDef",
    {
        "ResourceId": str,
        "WorkspaceCreationProperties": WorkspaceCreationPropertiesTypeDef,
    },
)
ModifyWorkspacePropertiesRequestRequestTypeDef = TypedDict(
    "ModifyWorkspacePropertiesRequestRequestTypeDef",
    {
        "WorkspaceId": str,
        "WorkspaceProperties": NotRequired[WorkspacePropertiesTypeDef],
        "DataReplication": NotRequired[DataReplicationType],
    },
)
WorkspacesPoolSessionTypeDef = TypedDict(
    "WorkspacesPoolSessionTypeDef",
    {
        "SessionId": str,
        "PoolId": str,
        "UserId": str,
        "AuthenticationType": NotRequired[Literal["SAML"]],
        "ConnectionState": NotRequired[SessionConnectionStateType],
        "InstanceId": NotRequired[str],
        "ExpirationTime": NotRequired[datetime],
        "NetworkAccessConfiguration": NotRequired[NetworkAccessConfigurationTypeDef],
        "StartTime": NotRequired[datetime],
    },
)
RebootWorkspacesRequestRequestTypeDef = TypedDict(
    "RebootWorkspacesRequestRequestTypeDef",
    {
        "RebootWorkspaceRequests": Sequence[RebootRequestTypeDef],
    },
)
RebuildWorkspacesRequestRequestTypeDef = TypedDict(
    "RebuildWorkspacesRequestRequestTypeDef",
    {
        "RebuildWorkspaceRequests": Sequence[RebuildRequestTypeDef],
    },
)
StartWorkspacesRequestRequestTypeDef = TypedDict(
    "StartWorkspacesRequestRequestTypeDef",
    {
        "StartWorkspaceRequests": Sequence[StartRequestTypeDef],
    },
)
StopWorkspacesRequestRequestTypeDef = TypedDict(
    "StopWorkspacesRequestRequestTypeDef",
    {
        "StopWorkspaceRequests": Sequence[StopRequestTypeDef],
    },
)
StreamingPropertiesOutputTypeDef = TypedDict(
    "StreamingPropertiesOutputTypeDef",
    {
        "StreamingExperiencePreferredProtocol": NotRequired[
            StreamingExperiencePreferredProtocolEnumType
        ],
        "UserSettings": NotRequired[List[UserSettingTypeDef]],
        "StorageConnectors": NotRequired[List[StorageConnectorTypeDef]],
    },
)
StreamingPropertiesTypeDef = TypedDict(
    "StreamingPropertiesTypeDef",
    {
        "StreamingExperiencePreferredProtocol": NotRequired[
            StreamingExperiencePreferredProtocolEnumType
        ],
        "UserSettings": NotRequired[Sequence[UserSettingTypeDef]],
        "StorageConnectors": NotRequired[Sequence[StorageConnectorTypeDef]],
    },
)
TerminateWorkspacesRequestRequestTypeDef = TypedDict(
    "TerminateWorkspacesRequestRequestTypeDef",
    {
        "TerminateWorkspaceRequests": Sequence[TerminateRequestTypeDef],
    },
)
WorkspaceImageTypeDef = TypedDict(
    "WorkspaceImageTypeDef",
    {
        "ImageId": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "OperatingSystem": NotRequired[OperatingSystemTypeDef],
        "State": NotRequired[WorkspaceImageStateType],
        "RequiredTenancy": NotRequired[WorkspaceImageRequiredTenancyType],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
        "Created": NotRequired[datetime],
        "OwnerAccountId": NotRequired[str],
        "Updates": NotRequired[UpdateResultTypeDef],
        "ErrorDetails": NotRequired[List[ErrorDetailsTypeDef]],
    },
)
WorkspacePropertiesUnionTypeDef = Union[
    WorkspacePropertiesTypeDef, WorkspacePropertiesOutputTypeDef
]
WorkspaceRequestOutputTypeDef = TypedDict(
    "WorkspaceRequestOutputTypeDef",
    {
        "DirectoryId": str,
        "UserName": str,
        "BundleId": str,
        "VolumeEncryptionKey": NotRequired[str],
        "UserVolumeEncryptionEnabled": NotRequired[bool],
        "RootVolumeEncryptionEnabled": NotRequired[bool],
        "WorkspaceProperties": NotRequired[WorkspacePropertiesOutputTypeDef],
        "Tags": NotRequired[List[TagTypeDef]],
        "WorkspaceName": NotRequired[str],
    },
)
WorkspaceTypeDef = TypedDict(
    "WorkspaceTypeDef",
    {
        "WorkspaceId": NotRequired[str],
        "DirectoryId": NotRequired[str],
        "UserName": NotRequired[str],
        "IpAddress": NotRequired[str],
        "State": NotRequired[WorkspaceStateType],
        "BundleId": NotRequired[str],
        "SubnetId": NotRequired[str],
        "ErrorMessage": NotRequired[str],
        "ErrorCode": NotRequired[str],
        "ComputerName": NotRequired[str],
        "VolumeEncryptionKey": NotRequired[str],
        "UserVolumeEncryptionEnabled": NotRequired[bool],
        "RootVolumeEncryptionEnabled": NotRequired[bool],
        "WorkspaceName": NotRequired[str],
        "WorkspaceProperties": NotRequired[WorkspacePropertiesOutputTypeDef],
        "ModificationStates": NotRequired[List[ModificationStateTypeDef]],
        "RelatedWorkspaces": NotRequired[List[RelatedWorkspacePropertiesTypeDef]],
        "DataReplicationSettings": NotRequired[DataReplicationSettingsTypeDef],
        "StandbyWorkspacesProperties": NotRequired[List[StandbyWorkspacesPropertiesTypeDef]],
    },
)
WorkspacesPoolTypeDef = TypedDict(
    "WorkspacesPoolTypeDef",
    {
        "PoolId": str,
        "PoolArn": str,
        "CapacityStatus": CapacityStatusTypeDef,
        "PoolName": str,
        "State": WorkspacesPoolStateType,
        "CreatedAt": datetime,
        "BundleId": str,
        "DirectoryId": str,
        "Description": NotRequired[str],
        "Errors": NotRequired[List[WorkspacesPoolErrorTypeDef]],
        "ApplicationSettings": NotRequired[ApplicationSettingsResponseTypeDef],
        "TimeoutSettings": NotRequired[TimeoutSettingsTypeDef],
    },
)
DescribeApplicationAssociationsResultTypeDef = TypedDict(
    "DescribeApplicationAssociationsResultTypeDef",
    {
        "Associations": List[ApplicationResourceAssociationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeBundleAssociationsResultTypeDef = TypedDict(
    "DescribeBundleAssociationsResultTypeDef",
    {
        "Associations": List[BundleResourceAssociationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeImageAssociationsResultTypeDef = TypedDict(
    "DescribeImageAssociationsResultTypeDef",
    {
        "Associations": List[ImageResourceAssociationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateWorkspaceApplicationResultTypeDef = TypedDict(
    "AssociateWorkspaceApplicationResultTypeDef",
    {
        "Association": WorkspaceResourceAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeWorkspaceAssociationsResultTypeDef = TypedDict(
    "DescribeWorkspaceAssociationsResultTypeDef",
    {
        "Associations": List[WorkspaceResourceAssociationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateWorkspaceApplicationResultTypeDef = TypedDict(
    "DisassociateWorkspaceApplicationResultTypeDef",
    {
        "Association": WorkspaceResourceAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
WorkSpaceApplicationDeploymentTypeDef = TypedDict(
    "WorkSpaceApplicationDeploymentTypeDef",
    {
        "Associations": NotRequired[List[WorkspaceResourceAssociationTypeDef]],
    },
)
DescribeIpGroupsResultTypeDef = TypedDict(
    "DescribeIpGroupsResultTypeDef",
    {
        "Result": List[WorkspacesIpGroupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ImportClientBrandingRequestRequestTypeDef = TypedDict(
    "ImportClientBrandingRequestRequestTypeDef",
    {
        "ResourceId": str,
        "DeviceTypeWindows": NotRequired[DefaultImportClientBrandingAttributesTypeDef],
        "DeviceTypeOsx": NotRequired[DefaultImportClientBrandingAttributesTypeDef],
        "DeviceTypeAndroid": NotRequired[DefaultImportClientBrandingAttributesTypeDef],
        "DeviceTypeIos": NotRequired[IosImportClientBrandingAttributesTypeDef],
        "DeviceTypeLinux": NotRequired[DefaultImportClientBrandingAttributesTypeDef],
        "DeviceTypeWeb": NotRequired[DefaultImportClientBrandingAttributesTypeDef],
    },
)
DescribeClientPropertiesResultTypeDef = TypedDict(
    "DescribeClientPropertiesResultTypeDef",
    {
        "ClientPropertiesList": List[ClientPropertiesResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeConnectionAliasesResultTypeDef = TypedDict(
    "DescribeConnectionAliasesResultTypeDef",
    {
        "ConnectionAliases": List[ConnectionAliasTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
FailedCreateStandbyWorkspacesRequestTypeDef = TypedDict(
    "FailedCreateStandbyWorkspacesRequestTypeDef",
    {
        "StandbyWorkspaceRequest": NotRequired[StandbyWorkspaceOutputTypeDef],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)
StandbyWorkspaceUnionTypeDef = Union[StandbyWorkspaceTypeDef, StandbyWorkspaceOutputTypeDef]
CreateWorkspaceBundleResultTypeDef = TypedDict(
    "CreateWorkspaceBundleResultTypeDef",
    {
        "WorkspaceBundle": WorkspaceBundleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeWorkspaceBundlesResultTypeDef = TypedDict(
    "DescribeWorkspaceBundlesResultTypeDef",
    {
        "Bundles": List[WorkspaceBundleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeWorkspacesPoolSessionsResultTypeDef = TypedDict(
    "DescribeWorkspacesPoolSessionsResultTypeDef",
    {
        "Sessions": List[WorkspacesPoolSessionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
WorkspaceDirectoryTypeDef = TypedDict(
    "WorkspaceDirectoryTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "Alias": NotRequired[str],
        "DirectoryName": NotRequired[str],
        "RegistrationCode": NotRequired[str],
        "SubnetIds": NotRequired[List[str]],
        "DnsIpAddresses": NotRequired[List[str]],
        "CustomerUserName": NotRequired[str],
        "IamRoleId": NotRequired[str],
        "DirectoryType": NotRequired[WorkspaceDirectoryTypeType],
        "WorkspaceSecurityGroupId": NotRequired[str],
        "State": NotRequired[WorkspaceDirectoryStateType],
        "WorkspaceCreationProperties": NotRequired[DefaultWorkspaceCreationPropertiesTypeDef],
        "ipGroupIds": NotRequired[List[str]],
        "WorkspaceAccessProperties": NotRequired[WorkspaceAccessPropertiesTypeDef],
        "Tenancy": NotRequired[TenancyType],
        "SelfservicePermissions": NotRequired[SelfservicePermissionsTypeDef],
        "SamlProperties": NotRequired[SamlPropertiesTypeDef],
        "CertificateBasedAuthProperties": NotRequired[CertificateBasedAuthPropertiesTypeDef],
        "MicrosoftEntraConfig": NotRequired[MicrosoftEntraConfigTypeDef],
        "WorkspaceDirectoryName": NotRequired[str],
        "WorkspaceDirectoryDescription": NotRequired[str],
        "UserIdentityType": NotRequired[UserIdentityTypeType],
        "WorkspaceType": NotRequired[WorkspaceTypeType],
        "IDCConfig": NotRequired[IDCConfigTypeDef],
        "ActiveDirectoryConfig": NotRequired[ActiveDirectoryConfigTypeDef],
        "StreamingProperties": NotRequired[StreamingPropertiesOutputTypeDef],
        "ErrorMessage": NotRequired[str],
    },
)
ModifyStreamingPropertiesRequestRequestTypeDef = TypedDict(
    "ModifyStreamingPropertiesRequestRequestTypeDef",
    {
        "ResourceId": str,
        "StreamingProperties": NotRequired[StreamingPropertiesTypeDef],
    },
)
DescribeWorkspaceImagesResultTypeDef = TypedDict(
    "DescribeWorkspaceImagesResultTypeDef",
    {
        "Images": List[WorkspaceImageTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
WorkspaceRequestTypeDef = TypedDict(
    "WorkspaceRequestTypeDef",
    {
        "DirectoryId": str,
        "UserName": str,
        "BundleId": str,
        "VolumeEncryptionKey": NotRequired[str],
        "UserVolumeEncryptionEnabled": NotRequired[bool],
        "RootVolumeEncryptionEnabled": NotRequired[bool],
        "WorkspaceProperties": NotRequired[WorkspacePropertiesUnionTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "WorkspaceName": NotRequired[str],
    },
)
FailedCreateWorkspaceRequestTypeDef = TypedDict(
    "FailedCreateWorkspaceRequestTypeDef",
    {
        "WorkspaceRequest": NotRequired[WorkspaceRequestOutputTypeDef],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)
DescribeWorkspacesResultTypeDef = TypedDict(
    "DescribeWorkspacesResultTypeDef",
    {
        "Workspaces": List[WorkspaceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateWorkspacesPoolResultTypeDef = TypedDict(
    "CreateWorkspacesPoolResultTypeDef",
    {
        "WorkspacesPool": WorkspacesPoolTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeWorkspacesPoolsResultTypeDef = TypedDict(
    "DescribeWorkspacesPoolsResultTypeDef",
    {
        "WorkspacesPools": List[WorkspacesPoolTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateWorkspacesPoolResultTypeDef = TypedDict(
    "UpdateWorkspacesPoolResultTypeDef",
    {
        "WorkspacesPool": WorkspacesPoolTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeployWorkspaceApplicationsResultTypeDef = TypedDict(
    "DeployWorkspaceApplicationsResultTypeDef",
    {
        "Deployment": WorkSpaceApplicationDeploymentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateStandbyWorkspacesResultTypeDef = TypedDict(
    "CreateStandbyWorkspacesResultTypeDef",
    {
        "FailedStandbyRequests": List[FailedCreateStandbyWorkspacesRequestTypeDef],
        "PendingStandbyRequests": List[PendingCreateStandbyWorkspacesRequestTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateStandbyWorkspacesRequestRequestTypeDef = TypedDict(
    "CreateStandbyWorkspacesRequestRequestTypeDef",
    {
        "PrimaryRegion": str,
        "StandbyWorkspaces": Sequence[StandbyWorkspaceUnionTypeDef],
    },
)
DescribeWorkspaceDirectoriesResultTypeDef = TypedDict(
    "DescribeWorkspaceDirectoriesResultTypeDef",
    {
        "Directories": List[WorkspaceDirectoryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
WorkspaceRequestUnionTypeDef = Union[WorkspaceRequestTypeDef, WorkspaceRequestOutputTypeDef]
CreateWorkspacesResultTypeDef = TypedDict(
    "CreateWorkspacesResultTypeDef",
    {
        "FailedRequests": List[FailedCreateWorkspaceRequestTypeDef],
        "PendingRequests": List[WorkspaceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWorkspacesRequestRequestTypeDef = TypedDict(
    "CreateWorkspacesRequestRequestTypeDef",
    {
        "Workspaces": Sequence[WorkspaceRequestUnionTypeDef],
    },
)
