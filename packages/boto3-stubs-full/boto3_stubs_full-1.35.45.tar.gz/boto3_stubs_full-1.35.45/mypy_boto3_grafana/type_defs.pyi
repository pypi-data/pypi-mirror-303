"""
Type annotations for grafana service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/type_defs/)

Usage::

    ```python
    from mypy_boto3_grafana.type_defs import AssertionAttributesTypeDef

    data: AssertionAttributesTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AccountAccessTypeType,
    AuthenticationProviderTypesType,
    DataSourceTypeType,
    LicenseTypeType,
    PermissionTypeType,
    RoleType,
    SamlConfigurationStatusType,
    UpdateActionType,
    UserTypeType,
    WorkspaceStatusType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AssertionAttributesTypeDef",
    "AssociateLicenseRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "AwsSsoAuthenticationTypeDef",
    "AuthenticationSummaryTypeDef",
    "CreateWorkspaceApiKeyRequestRequestTypeDef",
    "NetworkAccessConfigurationTypeDef",
    "VpcConfigurationTypeDef",
    "CreateWorkspaceServiceAccountRequestRequestTypeDef",
    "CreateWorkspaceServiceAccountTokenRequestRequestTypeDef",
    "ServiceAccountTokenSummaryWithKeyTypeDef",
    "DeleteWorkspaceApiKeyRequestRequestTypeDef",
    "DeleteWorkspaceRequestRequestTypeDef",
    "DeleteWorkspaceServiceAccountRequestRequestTypeDef",
    "DeleteWorkspaceServiceAccountTokenRequestRequestTypeDef",
    "DescribeWorkspaceAuthenticationRequestRequestTypeDef",
    "DescribeWorkspaceConfigurationRequestRequestTypeDef",
    "DescribeWorkspaceRequestRequestTypeDef",
    "DisassociateLicenseRequestRequestTypeDef",
    "IdpMetadataTypeDef",
    "PaginatorConfigTypeDef",
    "ListPermissionsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListVersionsRequestRequestTypeDef",
    "ListWorkspaceServiceAccountTokensRequestRequestTypeDef",
    "ServiceAccountTokenSummaryTypeDef",
    "ListWorkspaceServiceAccountsRequestRequestTypeDef",
    "ServiceAccountSummaryTypeDef",
    "ListWorkspacesRequestRequestTypeDef",
    "NetworkAccessConfigurationOutputTypeDef",
    "UserTypeDef",
    "RoleValuesOutputTypeDef",
    "RoleValuesTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateWorkspaceConfigurationRequestRequestTypeDef",
    "VpcConfigurationOutputTypeDef",
    "CreateWorkspaceApiKeyResponseTypeDef",
    "CreateWorkspaceServiceAccountResponseTypeDef",
    "DeleteWorkspaceApiKeyResponseTypeDef",
    "DeleteWorkspaceServiceAccountResponseTypeDef",
    "DeleteWorkspaceServiceAccountTokenResponseTypeDef",
    "DescribeWorkspaceConfigurationResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListVersionsResponseTypeDef",
    "WorkspaceSummaryTypeDef",
    "CreateWorkspaceRequestRequestTypeDef",
    "UpdateWorkspaceRequestRequestTypeDef",
    "CreateWorkspaceServiceAccountTokenResponseTypeDef",
    "ListPermissionsRequestListPermissionsPaginateTypeDef",
    "ListVersionsRequestListVersionsPaginateTypeDef",
    "ListWorkspaceServiceAccountTokensRequestListWorkspaceServiceAccountTokensPaginateTypeDef",
    "ListWorkspaceServiceAccountsRequestListWorkspaceServiceAccountsPaginateTypeDef",
    "ListWorkspacesRequestListWorkspacesPaginateTypeDef",
    "ListWorkspaceServiceAccountTokensResponseTypeDef",
    "ListWorkspaceServiceAccountsResponseTypeDef",
    "PermissionEntryTypeDef",
    "UpdateInstructionOutputTypeDef",
    "UpdateInstructionTypeDef",
    "SamlConfigurationOutputTypeDef",
    "RoleValuesUnionTypeDef",
    "WorkspaceDescriptionTypeDef",
    "ListWorkspacesResponseTypeDef",
    "ListPermissionsResponseTypeDef",
    "UpdateErrorTypeDef",
    "UpdateInstructionUnionTypeDef",
    "SamlAuthenticationTypeDef",
    "SamlConfigurationTypeDef",
    "AssociateLicenseResponseTypeDef",
    "CreateWorkspaceResponseTypeDef",
    "DeleteWorkspaceResponseTypeDef",
    "DescribeWorkspaceResponseTypeDef",
    "DisassociateLicenseResponseTypeDef",
    "UpdateWorkspaceResponseTypeDef",
    "UpdatePermissionsResponseTypeDef",
    "UpdatePermissionsRequestRequestTypeDef",
    "AuthenticationDescriptionTypeDef",
    "UpdateWorkspaceAuthenticationRequestRequestTypeDef",
    "DescribeWorkspaceAuthenticationResponseTypeDef",
    "UpdateWorkspaceAuthenticationResponseTypeDef",
)

AssertionAttributesTypeDef = TypedDict(
    "AssertionAttributesTypeDef",
    {
        "email": NotRequired[str],
        "groups": NotRequired[str],
        "login": NotRequired[str],
        "name": NotRequired[str],
        "org": NotRequired[str],
        "role": NotRequired[str],
    },
)
AssociateLicenseRequestRequestTypeDef = TypedDict(
    "AssociateLicenseRequestRequestTypeDef",
    {
        "licenseType": LicenseTypeType,
        "workspaceId": str,
        "grafanaToken": NotRequired[str],
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
AwsSsoAuthenticationTypeDef = TypedDict(
    "AwsSsoAuthenticationTypeDef",
    {
        "ssoClientId": NotRequired[str],
    },
)
AuthenticationSummaryTypeDef = TypedDict(
    "AuthenticationSummaryTypeDef",
    {
        "providers": List[AuthenticationProviderTypesType],
        "samlConfigurationStatus": NotRequired[SamlConfigurationStatusType],
    },
)
CreateWorkspaceApiKeyRequestRequestTypeDef = TypedDict(
    "CreateWorkspaceApiKeyRequestRequestTypeDef",
    {
        "keyName": str,
        "keyRole": str,
        "secondsToLive": int,
        "workspaceId": str,
    },
)
NetworkAccessConfigurationTypeDef = TypedDict(
    "NetworkAccessConfigurationTypeDef",
    {
        "prefixListIds": Sequence[str],
        "vpceIds": Sequence[str],
    },
)
VpcConfigurationTypeDef = TypedDict(
    "VpcConfigurationTypeDef",
    {
        "securityGroupIds": Sequence[str],
        "subnetIds": Sequence[str],
    },
)
CreateWorkspaceServiceAccountRequestRequestTypeDef = TypedDict(
    "CreateWorkspaceServiceAccountRequestRequestTypeDef",
    {
        "grafanaRole": RoleType,
        "name": str,
        "workspaceId": str,
    },
)
CreateWorkspaceServiceAccountTokenRequestRequestTypeDef = TypedDict(
    "CreateWorkspaceServiceAccountTokenRequestRequestTypeDef",
    {
        "name": str,
        "secondsToLive": int,
        "serviceAccountId": str,
        "workspaceId": str,
    },
)
ServiceAccountTokenSummaryWithKeyTypeDef = TypedDict(
    "ServiceAccountTokenSummaryWithKeyTypeDef",
    {
        "id": str,
        "key": str,
        "name": str,
    },
)
DeleteWorkspaceApiKeyRequestRequestTypeDef = TypedDict(
    "DeleteWorkspaceApiKeyRequestRequestTypeDef",
    {
        "keyName": str,
        "workspaceId": str,
    },
)
DeleteWorkspaceRequestRequestTypeDef = TypedDict(
    "DeleteWorkspaceRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)
DeleteWorkspaceServiceAccountRequestRequestTypeDef = TypedDict(
    "DeleteWorkspaceServiceAccountRequestRequestTypeDef",
    {
        "serviceAccountId": str,
        "workspaceId": str,
    },
)
DeleteWorkspaceServiceAccountTokenRequestRequestTypeDef = TypedDict(
    "DeleteWorkspaceServiceAccountTokenRequestRequestTypeDef",
    {
        "serviceAccountId": str,
        "tokenId": str,
        "workspaceId": str,
    },
)
DescribeWorkspaceAuthenticationRequestRequestTypeDef = TypedDict(
    "DescribeWorkspaceAuthenticationRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)
DescribeWorkspaceConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeWorkspaceConfigurationRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)
DescribeWorkspaceRequestRequestTypeDef = TypedDict(
    "DescribeWorkspaceRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)
DisassociateLicenseRequestRequestTypeDef = TypedDict(
    "DisassociateLicenseRequestRequestTypeDef",
    {
        "licenseType": LicenseTypeType,
        "workspaceId": str,
    },
)
IdpMetadataTypeDef = TypedDict(
    "IdpMetadataTypeDef",
    {
        "url": NotRequired[str],
        "xml": NotRequired[str],
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
ListPermissionsRequestRequestTypeDef = TypedDict(
    "ListPermissionsRequestRequestTypeDef",
    {
        "workspaceId": str,
        "groupId": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "userId": NotRequired[str],
        "userType": NotRequired[UserTypeType],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
ListVersionsRequestRequestTypeDef = TypedDict(
    "ListVersionsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "workspaceId": NotRequired[str],
    },
)
ListWorkspaceServiceAccountTokensRequestRequestTypeDef = TypedDict(
    "ListWorkspaceServiceAccountTokensRequestRequestTypeDef",
    {
        "serviceAccountId": str,
        "workspaceId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ServiceAccountTokenSummaryTypeDef = TypedDict(
    "ServiceAccountTokenSummaryTypeDef",
    {
        "createdAt": datetime,
        "expiresAt": datetime,
        "id": str,
        "name": str,
        "lastUsedAt": NotRequired[datetime],
    },
)
ListWorkspaceServiceAccountsRequestRequestTypeDef = TypedDict(
    "ListWorkspaceServiceAccountsRequestRequestTypeDef",
    {
        "workspaceId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ServiceAccountSummaryTypeDef = TypedDict(
    "ServiceAccountSummaryTypeDef",
    {
        "grafanaRole": RoleType,
        "id": str,
        "isDisabled": str,
        "name": str,
    },
)
ListWorkspacesRequestRequestTypeDef = TypedDict(
    "ListWorkspacesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
NetworkAccessConfigurationOutputTypeDef = TypedDict(
    "NetworkAccessConfigurationOutputTypeDef",
    {
        "prefixListIds": List[str],
        "vpceIds": List[str],
    },
)
UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "id": str,
        "type": UserTypeType,
    },
)
RoleValuesOutputTypeDef = TypedDict(
    "RoleValuesOutputTypeDef",
    {
        "admin": NotRequired[List[str]],
        "editor": NotRequired[List[str]],
    },
)
RoleValuesTypeDef = TypedDict(
    "RoleValuesTypeDef",
    {
        "admin": NotRequired[Sequence[str]],
        "editor": NotRequired[Sequence[str]],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UpdateWorkspaceConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateWorkspaceConfigurationRequestRequestTypeDef",
    {
        "configuration": str,
        "workspaceId": str,
        "grafanaVersion": NotRequired[str],
    },
)
VpcConfigurationOutputTypeDef = TypedDict(
    "VpcConfigurationOutputTypeDef",
    {
        "securityGroupIds": List[str],
        "subnetIds": List[str],
    },
)
CreateWorkspaceApiKeyResponseTypeDef = TypedDict(
    "CreateWorkspaceApiKeyResponseTypeDef",
    {
        "key": str,
        "keyName": str,
        "workspaceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWorkspaceServiceAccountResponseTypeDef = TypedDict(
    "CreateWorkspaceServiceAccountResponseTypeDef",
    {
        "grafanaRole": RoleType,
        "id": str,
        "name": str,
        "workspaceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteWorkspaceApiKeyResponseTypeDef = TypedDict(
    "DeleteWorkspaceApiKeyResponseTypeDef",
    {
        "keyName": str,
        "workspaceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteWorkspaceServiceAccountResponseTypeDef = TypedDict(
    "DeleteWorkspaceServiceAccountResponseTypeDef",
    {
        "serviceAccountId": str,
        "workspaceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteWorkspaceServiceAccountTokenResponseTypeDef = TypedDict(
    "DeleteWorkspaceServiceAccountTokenResponseTypeDef",
    {
        "serviceAccountId": str,
        "tokenId": str,
        "workspaceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeWorkspaceConfigurationResponseTypeDef = TypedDict(
    "DescribeWorkspaceConfigurationResponseTypeDef",
    {
        "configuration": str,
        "grafanaVersion": str,
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
ListVersionsResponseTypeDef = TypedDict(
    "ListVersionsResponseTypeDef",
    {
        "grafanaVersions": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
WorkspaceSummaryTypeDef = TypedDict(
    "WorkspaceSummaryTypeDef",
    {
        "authentication": AuthenticationSummaryTypeDef,
        "created": datetime,
        "endpoint": str,
        "grafanaVersion": str,
        "id": str,
        "modified": datetime,
        "status": WorkspaceStatusType,
        "description": NotRequired[str],
        "grafanaToken": NotRequired[str],
        "licenseType": NotRequired[LicenseTypeType],
        "name": NotRequired[str],
        "notificationDestinations": NotRequired[List[Literal["SNS"]]],
        "tags": NotRequired[Dict[str, str]],
    },
)
CreateWorkspaceRequestRequestTypeDef = TypedDict(
    "CreateWorkspaceRequestRequestTypeDef",
    {
        "accountAccessType": AccountAccessTypeType,
        "authenticationProviders": Sequence[AuthenticationProviderTypesType],
        "permissionType": PermissionTypeType,
        "clientToken": NotRequired[str],
        "configuration": NotRequired[str],
        "grafanaVersion": NotRequired[str],
        "networkAccessControl": NotRequired[NetworkAccessConfigurationTypeDef],
        "organizationRoleName": NotRequired[str],
        "stackSetName": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "vpcConfiguration": NotRequired[VpcConfigurationTypeDef],
        "workspaceDataSources": NotRequired[Sequence[DataSourceTypeType]],
        "workspaceDescription": NotRequired[str],
        "workspaceName": NotRequired[str],
        "workspaceNotificationDestinations": NotRequired[Sequence[Literal["SNS"]]],
        "workspaceOrganizationalUnits": NotRequired[Sequence[str]],
        "workspaceRoleArn": NotRequired[str],
    },
)
UpdateWorkspaceRequestRequestTypeDef = TypedDict(
    "UpdateWorkspaceRequestRequestTypeDef",
    {
        "workspaceId": str,
        "accountAccessType": NotRequired[AccountAccessTypeType],
        "networkAccessControl": NotRequired[NetworkAccessConfigurationTypeDef],
        "organizationRoleName": NotRequired[str],
        "permissionType": NotRequired[PermissionTypeType],
        "removeNetworkAccessConfiguration": NotRequired[bool],
        "removeVpcConfiguration": NotRequired[bool],
        "stackSetName": NotRequired[str],
        "vpcConfiguration": NotRequired[VpcConfigurationTypeDef],
        "workspaceDataSources": NotRequired[Sequence[DataSourceTypeType]],
        "workspaceDescription": NotRequired[str],
        "workspaceName": NotRequired[str],
        "workspaceNotificationDestinations": NotRequired[Sequence[Literal["SNS"]]],
        "workspaceOrganizationalUnits": NotRequired[Sequence[str]],
        "workspaceRoleArn": NotRequired[str],
    },
)
CreateWorkspaceServiceAccountTokenResponseTypeDef = TypedDict(
    "CreateWorkspaceServiceAccountTokenResponseTypeDef",
    {
        "serviceAccountId": str,
        "serviceAccountToken": ServiceAccountTokenSummaryWithKeyTypeDef,
        "workspaceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPermissionsRequestListPermissionsPaginateTypeDef = TypedDict(
    "ListPermissionsRequestListPermissionsPaginateTypeDef",
    {
        "workspaceId": str,
        "groupId": NotRequired[str],
        "userId": NotRequired[str],
        "userType": NotRequired[UserTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListVersionsRequestListVersionsPaginateTypeDef = TypedDict(
    "ListVersionsRequestListVersionsPaginateTypeDef",
    {
        "workspaceId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWorkspaceServiceAccountTokensRequestListWorkspaceServiceAccountTokensPaginateTypeDef = (
    TypedDict(
        "ListWorkspaceServiceAccountTokensRequestListWorkspaceServiceAccountTokensPaginateTypeDef",
        {
            "serviceAccountId": str,
            "workspaceId": str,
            "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
        },
    )
)
ListWorkspaceServiceAccountsRequestListWorkspaceServiceAccountsPaginateTypeDef = TypedDict(
    "ListWorkspaceServiceAccountsRequestListWorkspaceServiceAccountsPaginateTypeDef",
    {
        "workspaceId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWorkspacesRequestListWorkspacesPaginateTypeDef = TypedDict(
    "ListWorkspacesRequestListWorkspacesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWorkspaceServiceAccountTokensResponseTypeDef = TypedDict(
    "ListWorkspaceServiceAccountTokensResponseTypeDef",
    {
        "nextToken": str,
        "serviceAccountId": str,
        "serviceAccountTokens": List[ServiceAccountTokenSummaryTypeDef],
        "workspaceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListWorkspaceServiceAccountsResponseTypeDef = TypedDict(
    "ListWorkspaceServiceAccountsResponseTypeDef",
    {
        "nextToken": str,
        "serviceAccounts": List[ServiceAccountSummaryTypeDef],
        "workspaceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PermissionEntryTypeDef = TypedDict(
    "PermissionEntryTypeDef",
    {
        "role": RoleType,
        "user": UserTypeDef,
    },
)
UpdateInstructionOutputTypeDef = TypedDict(
    "UpdateInstructionOutputTypeDef",
    {
        "action": UpdateActionType,
        "role": RoleType,
        "users": List[UserTypeDef],
    },
)
UpdateInstructionTypeDef = TypedDict(
    "UpdateInstructionTypeDef",
    {
        "action": UpdateActionType,
        "role": RoleType,
        "users": Sequence[UserTypeDef],
    },
)
SamlConfigurationOutputTypeDef = TypedDict(
    "SamlConfigurationOutputTypeDef",
    {
        "idpMetadata": IdpMetadataTypeDef,
        "allowedOrganizations": NotRequired[List[str]],
        "assertionAttributes": NotRequired[AssertionAttributesTypeDef],
        "loginValidityDuration": NotRequired[int],
        "roleValues": NotRequired[RoleValuesOutputTypeDef],
    },
)
RoleValuesUnionTypeDef = Union[RoleValuesTypeDef, RoleValuesOutputTypeDef]
WorkspaceDescriptionTypeDef = TypedDict(
    "WorkspaceDescriptionTypeDef",
    {
        "authentication": AuthenticationSummaryTypeDef,
        "created": datetime,
        "dataSources": List[DataSourceTypeType],
        "endpoint": str,
        "grafanaVersion": str,
        "id": str,
        "modified": datetime,
        "status": WorkspaceStatusType,
        "accountAccessType": NotRequired[AccountAccessTypeType],
        "description": NotRequired[str],
        "freeTrialConsumed": NotRequired[bool],
        "freeTrialExpiration": NotRequired[datetime],
        "grafanaToken": NotRequired[str],
        "licenseExpiration": NotRequired[datetime],
        "licenseType": NotRequired[LicenseTypeType],
        "name": NotRequired[str],
        "networkAccessControl": NotRequired[NetworkAccessConfigurationOutputTypeDef],
        "notificationDestinations": NotRequired[List[Literal["SNS"]]],
        "organizationRoleName": NotRequired[str],
        "organizationalUnits": NotRequired[List[str]],
        "permissionType": NotRequired[PermissionTypeType],
        "stackSetName": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "vpcConfiguration": NotRequired[VpcConfigurationOutputTypeDef],
        "workspaceRoleArn": NotRequired[str],
    },
)
ListWorkspacesResponseTypeDef = TypedDict(
    "ListWorkspacesResponseTypeDef",
    {
        "nextToken": str,
        "workspaces": List[WorkspaceSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPermissionsResponseTypeDef = TypedDict(
    "ListPermissionsResponseTypeDef",
    {
        "nextToken": str,
        "permissions": List[PermissionEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateErrorTypeDef = TypedDict(
    "UpdateErrorTypeDef",
    {
        "causedBy": UpdateInstructionOutputTypeDef,
        "code": int,
        "message": str,
    },
)
UpdateInstructionUnionTypeDef = Union[UpdateInstructionTypeDef, UpdateInstructionOutputTypeDef]
SamlAuthenticationTypeDef = TypedDict(
    "SamlAuthenticationTypeDef",
    {
        "status": SamlConfigurationStatusType,
        "configuration": NotRequired[SamlConfigurationOutputTypeDef],
    },
)
SamlConfigurationTypeDef = TypedDict(
    "SamlConfigurationTypeDef",
    {
        "idpMetadata": IdpMetadataTypeDef,
        "allowedOrganizations": NotRequired[Sequence[str]],
        "assertionAttributes": NotRequired[AssertionAttributesTypeDef],
        "loginValidityDuration": NotRequired[int],
        "roleValues": NotRequired[RoleValuesUnionTypeDef],
    },
)
AssociateLicenseResponseTypeDef = TypedDict(
    "AssociateLicenseResponseTypeDef",
    {
        "workspace": WorkspaceDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWorkspaceResponseTypeDef = TypedDict(
    "CreateWorkspaceResponseTypeDef",
    {
        "workspace": WorkspaceDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteWorkspaceResponseTypeDef = TypedDict(
    "DeleteWorkspaceResponseTypeDef",
    {
        "workspace": WorkspaceDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeWorkspaceResponseTypeDef = TypedDict(
    "DescribeWorkspaceResponseTypeDef",
    {
        "workspace": WorkspaceDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateLicenseResponseTypeDef = TypedDict(
    "DisassociateLicenseResponseTypeDef",
    {
        "workspace": WorkspaceDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateWorkspaceResponseTypeDef = TypedDict(
    "UpdateWorkspaceResponseTypeDef",
    {
        "workspace": WorkspaceDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePermissionsResponseTypeDef = TypedDict(
    "UpdatePermissionsResponseTypeDef",
    {
        "errors": List[UpdateErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePermissionsRequestRequestTypeDef = TypedDict(
    "UpdatePermissionsRequestRequestTypeDef",
    {
        "updateInstructionBatch": Sequence[UpdateInstructionUnionTypeDef],
        "workspaceId": str,
    },
)
AuthenticationDescriptionTypeDef = TypedDict(
    "AuthenticationDescriptionTypeDef",
    {
        "providers": List[AuthenticationProviderTypesType],
        "awsSso": NotRequired[AwsSsoAuthenticationTypeDef],
        "saml": NotRequired[SamlAuthenticationTypeDef],
    },
)
UpdateWorkspaceAuthenticationRequestRequestTypeDef = TypedDict(
    "UpdateWorkspaceAuthenticationRequestRequestTypeDef",
    {
        "authenticationProviders": Sequence[AuthenticationProviderTypesType],
        "workspaceId": str,
        "samlConfiguration": NotRequired[SamlConfigurationTypeDef],
    },
)
DescribeWorkspaceAuthenticationResponseTypeDef = TypedDict(
    "DescribeWorkspaceAuthenticationResponseTypeDef",
    {
        "authentication": AuthenticationDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateWorkspaceAuthenticationResponseTypeDef = TypedDict(
    "UpdateWorkspaceAuthenticationResponseTypeDef",
    {
        "authentication": AuthenticationDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
