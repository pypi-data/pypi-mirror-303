"""
Type annotations for workspaces-web service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/type_defs/)

Usage::

    ```python
    from mypy_boto3_workspaces_web.type_defs import AssociateBrowserSettingsRequestRequestTypeDef

    data: AssociateBrowserSettingsRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    AuthenticationTypeType,
    EnabledTypeType,
    IdentityProviderTypeType,
    InstanceTypeType,
    PortalStatusType,
    SessionSortByType,
    SessionStatusType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AssociateBrowserSettingsRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "AssociateIpAccessSettingsRequestRequestTypeDef",
    "AssociateNetworkSettingsRequestRequestTypeDef",
    "AssociateTrustStoreRequestRequestTypeDef",
    "AssociateUserAccessLoggingSettingsRequestRequestTypeDef",
    "AssociateUserSettingsRequestRequestTypeDef",
    "BlobTypeDef",
    "BrowserSettingsSummaryTypeDef",
    "BrowserSettingsTypeDef",
    "CertificateSummaryTypeDef",
    "CertificateTypeDef",
    "CookieSpecificationTypeDef",
    "TagTypeDef",
    "IpRuleTypeDef",
    "DeleteBrowserSettingsRequestRequestTypeDef",
    "DeleteIdentityProviderRequestRequestTypeDef",
    "DeleteIpAccessSettingsRequestRequestTypeDef",
    "DeleteNetworkSettingsRequestRequestTypeDef",
    "DeletePortalRequestRequestTypeDef",
    "DeleteTrustStoreRequestRequestTypeDef",
    "DeleteUserAccessLoggingSettingsRequestRequestTypeDef",
    "DeleteUserSettingsRequestRequestTypeDef",
    "DisassociateBrowserSettingsRequestRequestTypeDef",
    "DisassociateIpAccessSettingsRequestRequestTypeDef",
    "DisassociateNetworkSettingsRequestRequestTypeDef",
    "DisassociateTrustStoreRequestRequestTypeDef",
    "DisassociateUserAccessLoggingSettingsRequestRequestTypeDef",
    "DisassociateUserSettingsRequestRequestTypeDef",
    "ExpireSessionRequestRequestTypeDef",
    "GetBrowserSettingsRequestRequestTypeDef",
    "GetIdentityProviderRequestRequestTypeDef",
    "IdentityProviderTypeDef",
    "GetIpAccessSettingsRequestRequestTypeDef",
    "GetNetworkSettingsRequestRequestTypeDef",
    "NetworkSettingsTypeDef",
    "GetPortalRequestRequestTypeDef",
    "PortalTypeDef",
    "GetPortalServiceProviderMetadataRequestRequestTypeDef",
    "GetSessionRequestRequestTypeDef",
    "SessionTypeDef",
    "GetTrustStoreCertificateRequestRequestTypeDef",
    "GetTrustStoreRequestRequestTypeDef",
    "TrustStoreTypeDef",
    "GetUserAccessLoggingSettingsRequestRequestTypeDef",
    "UserAccessLoggingSettingsTypeDef",
    "GetUserSettingsRequestRequestTypeDef",
    "IdentityProviderSummaryTypeDef",
    "IpAccessSettingsSummaryTypeDef",
    "ListBrowserSettingsRequestRequestTypeDef",
    "ListIdentityProvidersRequestRequestTypeDef",
    "ListIpAccessSettingsRequestRequestTypeDef",
    "ListNetworkSettingsRequestRequestTypeDef",
    "NetworkSettingsSummaryTypeDef",
    "ListPortalsRequestRequestTypeDef",
    "PortalSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "ListSessionsRequestRequestTypeDef",
    "SessionSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTrustStoreCertificatesRequestRequestTypeDef",
    "ListTrustStoresRequestRequestTypeDef",
    "TrustStoreSummaryTypeDef",
    "ListUserAccessLoggingSettingsRequestRequestTypeDef",
    "UserAccessLoggingSettingsSummaryTypeDef",
    "ListUserSettingsRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateBrowserSettingsRequestRequestTypeDef",
    "UpdateIdentityProviderRequestRequestTypeDef",
    "UpdateNetworkSettingsRequestRequestTypeDef",
    "UpdatePortalRequestRequestTypeDef",
    "UpdateUserAccessLoggingSettingsRequestRequestTypeDef",
    "AssociateBrowserSettingsResponseTypeDef",
    "AssociateIpAccessSettingsResponseTypeDef",
    "AssociateNetworkSettingsResponseTypeDef",
    "AssociateTrustStoreResponseTypeDef",
    "AssociateUserAccessLoggingSettingsResponseTypeDef",
    "AssociateUserSettingsResponseTypeDef",
    "CreateBrowserSettingsResponseTypeDef",
    "CreateIdentityProviderResponseTypeDef",
    "CreateIpAccessSettingsResponseTypeDef",
    "CreateNetworkSettingsResponseTypeDef",
    "CreatePortalResponseTypeDef",
    "CreateTrustStoreResponseTypeDef",
    "CreateUserAccessLoggingSettingsResponseTypeDef",
    "CreateUserSettingsResponseTypeDef",
    "GetPortalServiceProviderMetadataResponseTypeDef",
    "UpdateTrustStoreResponseTypeDef",
    "UpdateTrustStoreRequestRequestTypeDef",
    "ListBrowserSettingsResponseTypeDef",
    "GetBrowserSettingsResponseTypeDef",
    "UpdateBrowserSettingsResponseTypeDef",
    "ListTrustStoreCertificatesResponseTypeDef",
    "GetTrustStoreCertificateResponseTypeDef",
    "CookieSynchronizationConfigurationOutputTypeDef",
    "CookieSynchronizationConfigurationTypeDef",
    "CreateBrowserSettingsRequestRequestTypeDef",
    "CreateIdentityProviderRequestRequestTypeDef",
    "CreateNetworkSettingsRequestRequestTypeDef",
    "CreatePortalRequestRequestTypeDef",
    "CreateTrustStoreRequestRequestTypeDef",
    "CreateUserAccessLoggingSettingsRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateIpAccessSettingsRequestRequestTypeDef",
    "IpAccessSettingsTypeDef",
    "UpdateIpAccessSettingsRequestRequestTypeDef",
    "GetIdentityProviderResponseTypeDef",
    "UpdateIdentityProviderResponseTypeDef",
    "GetNetworkSettingsResponseTypeDef",
    "UpdateNetworkSettingsResponseTypeDef",
    "GetPortalResponseTypeDef",
    "UpdatePortalResponseTypeDef",
    "GetSessionResponseTypeDef",
    "GetTrustStoreResponseTypeDef",
    "GetUserAccessLoggingSettingsResponseTypeDef",
    "UpdateUserAccessLoggingSettingsResponseTypeDef",
    "ListIdentityProvidersResponseTypeDef",
    "ListIpAccessSettingsResponseTypeDef",
    "ListNetworkSettingsResponseTypeDef",
    "ListPortalsResponseTypeDef",
    "ListSessionsRequestListSessionsPaginateTypeDef",
    "ListSessionsResponseTypeDef",
    "ListTrustStoresResponseTypeDef",
    "ListUserAccessLoggingSettingsResponseTypeDef",
    "UserSettingsSummaryTypeDef",
    "UserSettingsTypeDef",
    "CreateUserSettingsRequestRequestTypeDef",
    "UpdateUserSettingsRequestRequestTypeDef",
    "GetIpAccessSettingsResponseTypeDef",
    "UpdateIpAccessSettingsResponseTypeDef",
    "ListUserSettingsResponseTypeDef",
    "GetUserSettingsResponseTypeDef",
    "UpdateUserSettingsResponseTypeDef",
)

AssociateBrowserSettingsRequestRequestTypeDef = TypedDict(
    "AssociateBrowserSettingsRequestRequestTypeDef",
    {
        "browserSettingsArn": str,
        "portalArn": str,
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
AssociateIpAccessSettingsRequestRequestTypeDef = TypedDict(
    "AssociateIpAccessSettingsRequestRequestTypeDef",
    {
        "ipAccessSettingsArn": str,
        "portalArn": str,
    },
)
AssociateNetworkSettingsRequestRequestTypeDef = TypedDict(
    "AssociateNetworkSettingsRequestRequestTypeDef",
    {
        "networkSettingsArn": str,
        "portalArn": str,
    },
)
AssociateTrustStoreRequestRequestTypeDef = TypedDict(
    "AssociateTrustStoreRequestRequestTypeDef",
    {
        "portalArn": str,
        "trustStoreArn": str,
    },
)
AssociateUserAccessLoggingSettingsRequestRequestTypeDef = TypedDict(
    "AssociateUserAccessLoggingSettingsRequestRequestTypeDef",
    {
        "portalArn": str,
        "userAccessLoggingSettingsArn": str,
    },
)
AssociateUserSettingsRequestRequestTypeDef = TypedDict(
    "AssociateUserSettingsRequestRequestTypeDef",
    {
        "portalArn": str,
        "userSettingsArn": str,
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
BrowserSettingsSummaryTypeDef = TypedDict(
    "BrowserSettingsSummaryTypeDef",
    {
        "browserSettingsArn": str,
    },
)
BrowserSettingsTypeDef = TypedDict(
    "BrowserSettingsTypeDef",
    {
        "browserSettingsArn": str,
        "additionalEncryptionContext": NotRequired[Dict[str, str]],
        "associatedPortalArns": NotRequired[List[str]],
        "browserPolicy": NotRequired[str],
        "customerManagedKey": NotRequired[str],
    },
)
CertificateSummaryTypeDef = TypedDict(
    "CertificateSummaryTypeDef",
    {
        "issuer": NotRequired[str],
        "notValidAfter": NotRequired[datetime],
        "notValidBefore": NotRequired[datetime],
        "subject": NotRequired[str],
        "thumbprint": NotRequired[str],
    },
)
CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "body": NotRequired[bytes],
        "issuer": NotRequired[str],
        "notValidAfter": NotRequired[datetime],
        "notValidBefore": NotRequired[datetime],
        "subject": NotRequired[str],
        "thumbprint": NotRequired[str],
    },
)
CookieSpecificationTypeDef = TypedDict(
    "CookieSpecificationTypeDef",
    {
        "domain": str,
        "name": NotRequired[str],
        "path": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
IpRuleTypeDef = TypedDict(
    "IpRuleTypeDef",
    {
        "ipRange": str,
        "description": NotRequired[str],
    },
)
DeleteBrowserSettingsRequestRequestTypeDef = TypedDict(
    "DeleteBrowserSettingsRequestRequestTypeDef",
    {
        "browserSettingsArn": str,
    },
)
DeleteIdentityProviderRequestRequestTypeDef = TypedDict(
    "DeleteIdentityProviderRequestRequestTypeDef",
    {
        "identityProviderArn": str,
    },
)
DeleteIpAccessSettingsRequestRequestTypeDef = TypedDict(
    "DeleteIpAccessSettingsRequestRequestTypeDef",
    {
        "ipAccessSettingsArn": str,
    },
)
DeleteNetworkSettingsRequestRequestTypeDef = TypedDict(
    "DeleteNetworkSettingsRequestRequestTypeDef",
    {
        "networkSettingsArn": str,
    },
)
DeletePortalRequestRequestTypeDef = TypedDict(
    "DeletePortalRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)
DeleteTrustStoreRequestRequestTypeDef = TypedDict(
    "DeleteTrustStoreRequestRequestTypeDef",
    {
        "trustStoreArn": str,
    },
)
DeleteUserAccessLoggingSettingsRequestRequestTypeDef = TypedDict(
    "DeleteUserAccessLoggingSettingsRequestRequestTypeDef",
    {
        "userAccessLoggingSettingsArn": str,
    },
)
DeleteUserSettingsRequestRequestTypeDef = TypedDict(
    "DeleteUserSettingsRequestRequestTypeDef",
    {
        "userSettingsArn": str,
    },
)
DisassociateBrowserSettingsRequestRequestTypeDef = TypedDict(
    "DisassociateBrowserSettingsRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)
DisassociateIpAccessSettingsRequestRequestTypeDef = TypedDict(
    "DisassociateIpAccessSettingsRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)
DisassociateNetworkSettingsRequestRequestTypeDef = TypedDict(
    "DisassociateNetworkSettingsRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)
DisassociateTrustStoreRequestRequestTypeDef = TypedDict(
    "DisassociateTrustStoreRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)
DisassociateUserAccessLoggingSettingsRequestRequestTypeDef = TypedDict(
    "DisassociateUserAccessLoggingSettingsRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)
DisassociateUserSettingsRequestRequestTypeDef = TypedDict(
    "DisassociateUserSettingsRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)
ExpireSessionRequestRequestTypeDef = TypedDict(
    "ExpireSessionRequestRequestTypeDef",
    {
        "portalId": str,
        "sessionId": str,
    },
)
GetBrowserSettingsRequestRequestTypeDef = TypedDict(
    "GetBrowserSettingsRequestRequestTypeDef",
    {
        "browserSettingsArn": str,
    },
)
GetIdentityProviderRequestRequestTypeDef = TypedDict(
    "GetIdentityProviderRequestRequestTypeDef",
    {
        "identityProviderArn": str,
    },
)
IdentityProviderTypeDef = TypedDict(
    "IdentityProviderTypeDef",
    {
        "identityProviderArn": str,
        "identityProviderDetails": NotRequired[Dict[str, str]],
        "identityProviderName": NotRequired[str],
        "identityProviderType": NotRequired[IdentityProviderTypeType],
    },
)
GetIpAccessSettingsRequestRequestTypeDef = TypedDict(
    "GetIpAccessSettingsRequestRequestTypeDef",
    {
        "ipAccessSettingsArn": str,
    },
)
GetNetworkSettingsRequestRequestTypeDef = TypedDict(
    "GetNetworkSettingsRequestRequestTypeDef",
    {
        "networkSettingsArn": str,
    },
)
NetworkSettingsTypeDef = TypedDict(
    "NetworkSettingsTypeDef",
    {
        "networkSettingsArn": str,
        "associatedPortalArns": NotRequired[List[str]],
        "securityGroupIds": NotRequired[List[str]],
        "subnetIds": NotRequired[List[str]],
        "vpcId": NotRequired[str],
    },
)
GetPortalRequestRequestTypeDef = TypedDict(
    "GetPortalRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)
PortalTypeDef = TypedDict(
    "PortalTypeDef",
    {
        "portalArn": str,
        "additionalEncryptionContext": NotRequired[Dict[str, str]],
        "authenticationType": NotRequired[AuthenticationTypeType],
        "browserSettingsArn": NotRequired[str],
        "browserType": NotRequired[Literal["Chrome"]],
        "creationDate": NotRequired[datetime],
        "customerManagedKey": NotRequired[str],
        "displayName": NotRequired[str],
        "instanceType": NotRequired[InstanceTypeType],
        "ipAccessSettingsArn": NotRequired[str],
        "maxConcurrentSessions": NotRequired[int],
        "networkSettingsArn": NotRequired[str],
        "portalEndpoint": NotRequired[str],
        "portalStatus": NotRequired[PortalStatusType],
        "rendererType": NotRequired[Literal["AppStream"]],
        "statusReason": NotRequired[str],
        "trustStoreArn": NotRequired[str],
        "userAccessLoggingSettingsArn": NotRequired[str],
        "userSettingsArn": NotRequired[str],
    },
)
GetPortalServiceProviderMetadataRequestRequestTypeDef = TypedDict(
    "GetPortalServiceProviderMetadataRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)
GetSessionRequestRequestTypeDef = TypedDict(
    "GetSessionRequestRequestTypeDef",
    {
        "portalId": str,
        "sessionId": str,
    },
)
SessionTypeDef = TypedDict(
    "SessionTypeDef",
    {
        "clientIpAddresses": NotRequired[List[str]],
        "endTime": NotRequired[datetime],
        "portalArn": NotRequired[str],
        "sessionId": NotRequired[str],
        "startTime": NotRequired[datetime],
        "status": NotRequired[SessionStatusType],
        "username": NotRequired[str],
    },
)
GetTrustStoreCertificateRequestRequestTypeDef = TypedDict(
    "GetTrustStoreCertificateRequestRequestTypeDef",
    {
        "thumbprint": str,
        "trustStoreArn": str,
    },
)
GetTrustStoreRequestRequestTypeDef = TypedDict(
    "GetTrustStoreRequestRequestTypeDef",
    {
        "trustStoreArn": str,
    },
)
TrustStoreTypeDef = TypedDict(
    "TrustStoreTypeDef",
    {
        "trustStoreArn": str,
        "associatedPortalArns": NotRequired[List[str]],
    },
)
GetUserAccessLoggingSettingsRequestRequestTypeDef = TypedDict(
    "GetUserAccessLoggingSettingsRequestRequestTypeDef",
    {
        "userAccessLoggingSettingsArn": str,
    },
)
UserAccessLoggingSettingsTypeDef = TypedDict(
    "UserAccessLoggingSettingsTypeDef",
    {
        "userAccessLoggingSettingsArn": str,
        "associatedPortalArns": NotRequired[List[str]],
        "kinesisStreamArn": NotRequired[str],
    },
)
GetUserSettingsRequestRequestTypeDef = TypedDict(
    "GetUserSettingsRequestRequestTypeDef",
    {
        "userSettingsArn": str,
    },
)
IdentityProviderSummaryTypeDef = TypedDict(
    "IdentityProviderSummaryTypeDef",
    {
        "identityProviderArn": str,
        "identityProviderName": NotRequired[str],
        "identityProviderType": NotRequired[IdentityProviderTypeType],
    },
)
IpAccessSettingsSummaryTypeDef = TypedDict(
    "IpAccessSettingsSummaryTypeDef",
    {
        "ipAccessSettingsArn": str,
        "creationDate": NotRequired[datetime],
        "description": NotRequired[str],
        "displayName": NotRequired[str],
    },
)
ListBrowserSettingsRequestRequestTypeDef = TypedDict(
    "ListBrowserSettingsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListIdentityProvidersRequestRequestTypeDef = TypedDict(
    "ListIdentityProvidersRequestRequestTypeDef",
    {
        "portalArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListIpAccessSettingsRequestRequestTypeDef = TypedDict(
    "ListIpAccessSettingsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListNetworkSettingsRequestRequestTypeDef = TypedDict(
    "ListNetworkSettingsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
NetworkSettingsSummaryTypeDef = TypedDict(
    "NetworkSettingsSummaryTypeDef",
    {
        "networkSettingsArn": str,
        "vpcId": NotRequired[str],
    },
)
ListPortalsRequestRequestTypeDef = TypedDict(
    "ListPortalsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
PortalSummaryTypeDef = TypedDict(
    "PortalSummaryTypeDef",
    {
        "portalArn": str,
        "authenticationType": NotRequired[AuthenticationTypeType],
        "browserSettingsArn": NotRequired[str],
        "browserType": NotRequired[Literal["Chrome"]],
        "creationDate": NotRequired[datetime],
        "displayName": NotRequired[str],
        "instanceType": NotRequired[InstanceTypeType],
        "ipAccessSettingsArn": NotRequired[str],
        "maxConcurrentSessions": NotRequired[int],
        "networkSettingsArn": NotRequired[str],
        "portalEndpoint": NotRequired[str],
        "portalStatus": NotRequired[PortalStatusType],
        "rendererType": NotRequired[Literal["AppStream"]],
        "trustStoreArn": NotRequired[str],
        "userAccessLoggingSettingsArn": NotRequired[str],
        "userSettingsArn": NotRequired[str],
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
ListSessionsRequestRequestTypeDef = TypedDict(
    "ListSessionsRequestRequestTypeDef",
    {
        "portalId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sessionId": NotRequired[str],
        "sortBy": NotRequired[SessionSortByType],
        "status": NotRequired[SessionStatusType],
        "username": NotRequired[str],
    },
)
SessionSummaryTypeDef = TypedDict(
    "SessionSummaryTypeDef",
    {
        "endTime": NotRequired[datetime],
        "portalArn": NotRequired[str],
        "sessionId": NotRequired[str],
        "startTime": NotRequired[datetime],
        "status": NotRequired[SessionStatusType],
        "username": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
ListTrustStoreCertificatesRequestRequestTypeDef = TypedDict(
    "ListTrustStoreCertificatesRequestRequestTypeDef",
    {
        "trustStoreArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListTrustStoresRequestRequestTypeDef = TypedDict(
    "ListTrustStoresRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
TrustStoreSummaryTypeDef = TypedDict(
    "TrustStoreSummaryTypeDef",
    {
        "trustStoreArn": NotRequired[str],
    },
)
ListUserAccessLoggingSettingsRequestRequestTypeDef = TypedDict(
    "ListUserAccessLoggingSettingsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
UserAccessLoggingSettingsSummaryTypeDef = TypedDict(
    "UserAccessLoggingSettingsSummaryTypeDef",
    {
        "userAccessLoggingSettingsArn": str,
        "kinesisStreamArn": NotRequired[str],
    },
)
ListUserSettingsRequestRequestTypeDef = TypedDict(
    "ListUserSettingsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UpdateBrowserSettingsRequestRequestTypeDef = TypedDict(
    "UpdateBrowserSettingsRequestRequestTypeDef",
    {
        "browserSettingsArn": str,
        "browserPolicy": NotRequired[str],
        "clientToken": NotRequired[str],
    },
)
UpdateIdentityProviderRequestRequestTypeDef = TypedDict(
    "UpdateIdentityProviderRequestRequestTypeDef",
    {
        "identityProviderArn": str,
        "clientToken": NotRequired[str],
        "identityProviderDetails": NotRequired[Mapping[str, str]],
        "identityProviderName": NotRequired[str],
        "identityProviderType": NotRequired[IdentityProviderTypeType],
    },
)
UpdateNetworkSettingsRequestRequestTypeDef = TypedDict(
    "UpdateNetworkSettingsRequestRequestTypeDef",
    {
        "networkSettingsArn": str,
        "clientToken": NotRequired[str],
        "securityGroupIds": NotRequired[Sequence[str]],
        "subnetIds": NotRequired[Sequence[str]],
        "vpcId": NotRequired[str],
    },
)
UpdatePortalRequestRequestTypeDef = TypedDict(
    "UpdatePortalRequestRequestTypeDef",
    {
        "portalArn": str,
        "authenticationType": NotRequired[AuthenticationTypeType],
        "displayName": NotRequired[str],
        "instanceType": NotRequired[InstanceTypeType],
        "maxConcurrentSessions": NotRequired[int],
    },
)
UpdateUserAccessLoggingSettingsRequestRequestTypeDef = TypedDict(
    "UpdateUserAccessLoggingSettingsRequestRequestTypeDef",
    {
        "userAccessLoggingSettingsArn": str,
        "clientToken": NotRequired[str],
        "kinesisStreamArn": NotRequired[str],
    },
)
AssociateBrowserSettingsResponseTypeDef = TypedDict(
    "AssociateBrowserSettingsResponseTypeDef",
    {
        "browserSettingsArn": str,
        "portalArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateIpAccessSettingsResponseTypeDef = TypedDict(
    "AssociateIpAccessSettingsResponseTypeDef",
    {
        "ipAccessSettingsArn": str,
        "portalArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateNetworkSettingsResponseTypeDef = TypedDict(
    "AssociateNetworkSettingsResponseTypeDef",
    {
        "networkSettingsArn": str,
        "portalArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateTrustStoreResponseTypeDef = TypedDict(
    "AssociateTrustStoreResponseTypeDef",
    {
        "portalArn": str,
        "trustStoreArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateUserAccessLoggingSettingsResponseTypeDef = TypedDict(
    "AssociateUserAccessLoggingSettingsResponseTypeDef",
    {
        "portalArn": str,
        "userAccessLoggingSettingsArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateUserSettingsResponseTypeDef = TypedDict(
    "AssociateUserSettingsResponseTypeDef",
    {
        "portalArn": str,
        "userSettingsArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateBrowserSettingsResponseTypeDef = TypedDict(
    "CreateBrowserSettingsResponseTypeDef",
    {
        "browserSettingsArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateIdentityProviderResponseTypeDef = TypedDict(
    "CreateIdentityProviderResponseTypeDef",
    {
        "identityProviderArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateIpAccessSettingsResponseTypeDef = TypedDict(
    "CreateIpAccessSettingsResponseTypeDef",
    {
        "ipAccessSettingsArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateNetworkSettingsResponseTypeDef = TypedDict(
    "CreateNetworkSettingsResponseTypeDef",
    {
        "networkSettingsArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePortalResponseTypeDef = TypedDict(
    "CreatePortalResponseTypeDef",
    {
        "portalArn": str,
        "portalEndpoint": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTrustStoreResponseTypeDef = TypedDict(
    "CreateTrustStoreResponseTypeDef",
    {
        "trustStoreArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateUserAccessLoggingSettingsResponseTypeDef = TypedDict(
    "CreateUserAccessLoggingSettingsResponseTypeDef",
    {
        "userAccessLoggingSettingsArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateUserSettingsResponseTypeDef = TypedDict(
    "CreateUserSettingsResponseTypeDef",
    {
        "userSettingsArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPortalServiceProviderMetadataResponseTypeDef = TypedDict(
    "GetPortalServiceProviderMetadataResponseTypeDef",
    {
        "portalArn": str,
        "serviceProviderSamlMetadata": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTrustStoreResponseTypeDef = TypedDict(
    "UpdateTrustStoreResponseTypeDef",
    {
        "trustStoreArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTrustStoreRequestRequestTypeDef = TypedDict(
    "UpdateTrustStoreRequestRequestTypeDef",
    {
        "trustStoreArn": str,
        "certificatesToAdd": NotRequired[Sequence[BlobTypeDef]],
        "certificatesToDelete": NotRequired[Sequence[str]],
        "clientToken": NotRequired[str],
    },
)
ListBrowserSettingsResponseTypeDef = TypedDict(
    "ListBrowserSettingsResponseTypeDef",
    {
        "browserSettings": List[BrowserSettingsSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBrowserSettingsResponseTypeDef = TypedDict(
    "GetBrowserSettingsResponseTypeDef",
    {
        "browserSettings": BrowserSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateBrowserSettingsResponseTypeDef = TypedDict(
    "UpdateBrowserSettingsResponseTypeDef",
    {
        "browserSettings": BrowserSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTrustStoreCertificatesResponseTypeDef = TypedDict(
    "ListTrustStoreCertificatesResponseTypeDef",
    {
        "certificateList": List[CertificateSummaryTypeDef],
        "nextToken": str,
        "trustStoreArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTrustStoreCertificateResponseTypeDef = TypedDict(
    "GetTrustStoreCertificateResponseTypeDef",
    {
        "certificate": CertificateTypeDef,
        "trustStoreArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CookieSynchronizationConfigurationOutputTypeDef = TypedDict(
    "CookieSynchronizationConfigurationOutputTypeDef",
    {
        "allowlist": List[CookieSpecificationTypeDef],
        "blocklist": NotRequired[List[CookieSpecificationTypeDef]],
    },
)
CookieSynchronizationConfigurationTypeDef = TypedDict(
    "CookieSynchronizationConfigurationTypeDef",
    {
        "allowlist": Sequence[CookieSpecificationTypeDef],
        "blocklist": NotRequired[Sequence[CookieSpecificationTypeDef]],
    },
)
CreateBrowserSettingsRequestRequestTypeDef = TypedDict(
    "CreateBrowserSettingsRequestRequestTypeDef",
    {
        "browserPolicy": str,
        "additionalEncryptionContext": NotRequired[Mapping[str, str]],
        "clientToken": NotRequired[str],
        "customerManagedKey": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateIdentityProviderRequestRequestTypeDef = TypedDict(
    "CreateIdentityProviderRequestRequestTypeDef",
    {
        "identityProviderDetails": Mapping[str, str],
        "identityProviderName": str,
        "identityProviderType": IdentityProviderTypeType,
        "portalArn": str,
        "clientToken": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateNetworkSettingsRequestRequestTypeDef = TypedDict(
    "CreateNetworkSettingsRequestRequestTypeDef",
    {
        "securityGroupIds": Sequence[str],
        "subnetIds": Sequence[str],
        "vpcId": str,
        "clientToken": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreatePortalRequestRequestTypeDef = TypedDict(
    "CreatePortalRequestRequestTypeDef",
    {
        "additionalEncryptionContext": NotRequired[Mapping[str, str]],
        "authenticationType": NotRequired[AuthenticationTypeType],
        "clientToken": NotRequired[str],
        "customerManagedKey": NotRequired[str],
        "displayName": NotRequired[str],
        "instanceType": NotRequired[InstanceTypeType],
        "maxConcurrentSessions": NotRequired[int],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateTrustStoreRequestRequestTypeDef = TypedDict(
    "CreateTrustStoreRequestRequestTypeDef",
    {
        "certificateList": Sequence[BlobTypeDef],
        "clientToken": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateUserAccessLoggingSettingsRequestRequestTypeDef = TypedDict(
    "CreateUserAccessLoggingSettingsRequestRequestTypeDef",
    {
        "kinesisStreamArn": str,
        "clientToken": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[TagTypeDef],
        "clientToken": NotRequired[str],
    },
)
CreateIpAccessSettingsRequestRequestTypeDef = TypedDict(
    "CreateIpAccessSettingsRequestRequestTypeDef",
    {
        "ipRules": Sequence[IpRuleTypeDef],
        "additionalEncryptionContext": NotRequired[Mapping[str, str]],
        "clientToken": NotRequired[str],
        "customerManagedKey": NotRequired[str],
        "description": NotRequired[str],
        "displayName": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
IpAccessSettingsTypeDef = TypedDict(
    "IpAccessSettingsTypeDef",
    {
        "ipAccessSettingsArn": str,
        "additionalEncryptionContext": NotRequired[Dict[str, str]],
        "associatedPortalArns": NotRequired[List[str]],
        "creationDate": NotRequired[datetime],
        "customerManagedKey": NotRequired[str],
        "description": NotRequired[str],
        "displayName": NotRequired[str],
        "ipRules": NotRequired[List[IpRuleTypeDef]],
    },
)
UpdateIpAccessSettingsRequestRequestTypeDef = TypedDict(
    "UpdateIpAccessSettingsRequestRequestTypeDef",
    {
        "ipAccessSettingsArn": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "displayName": NotRequired[str],
        "ipRules": NotRequired[Sequence[IpRuleTypeDef]],
    },
)
GetIdentityProviderResponseTypeDef = TypedDict(
    "GetIdentityProviderResponseTypeDef",
    {
        "identityProvider": IdentityProviderTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateIdentityProviderResponseTypeDef = TypedDict(
    "UpdateIdentityProviderResponseTypeDef",
    {
        "identityProvider": IdentityProviderTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetNetworkSettingsResponseTypeDef = TypedDict(
    "GetNetworkSettingsResponseTypeDef",
    {
        "networkSettings": NetworkSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateNetworkSettingsResponseTypeDef = TypedDict(
    "UpdateNetworkSettingsResponseTypeDef",
    {
        "networkSettings": NetworkSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPortalResponseTypeDef = TypedDict(
    "GetPortalResponseTypeDef",
    {
        "portal": PortalTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePortalResponseTypeDef = TypedDict(
    "UpdatePortalResponseTypeDef",
    {
        "portal": PortalTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSessionResponseTypeDef = TypedDict(
    "GetSessionResponseTypeDef",
    {
        "session": SessionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTrustStoreResponseTypeDef = TypedDict(
    "GetTrustStoreResponseTypeDef",
    {
        "trustStore": TrustStoreTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetUserAccessLoggingSettingsResponseTypeDef = TypedDict(
    "GetUserAccessLoggingSettingsResponseTypeDef",
    {
        "userAccessLoggingSettings": UserAccessLoggingSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateUserAccessLoggingSettingsResponseTypeDef = TypedDict(
    "UpdateUserAccessLoggingSettingsResponseTypeDef",
    {
        "userAccessLoggingSettings": UserAccessLoggingSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListIdentityProvidersResponseTypeDef = TypedDict(
    "ListIdentityProvidersResponseTypeDef",
    {
        "identityProviders": List[IdentityProviderSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListIpAccessSettingsResponseTypeDef = TypedDict(
    "ListIpAccessSettingsResponseTypeDef",
    {
        "ipAccessSettings": List[IpAccessSettingsSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListNetworkSettingsResponseTypeDef = TypedDict(
    "ListNetworkSettingsResponseTypeDef",
    {
        "networkSettings": List[NetworkSettingsSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPortalsResponseTypeDef = TypedDict(
    "ListPortalsResponseTypeDef",
    {
        "nextToken": str,
        "portals": List[PortalSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSessionsRequestListSessionsPaginateTypeDef = TypedDict(
    "ListSessionsRequestListSessionsPaginateTypeDef",
    {
        "portalId": str,
        "sessionId": NotRequired[str],
        "sortBy": NotRequired[SessionSortByType],
        "status": NotRequired[SessionStatusType],
        "username": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSessionsResponseTypeDef = TypedDict(
    "ListSessionsResponseTypeDef",
    {
        "nextToken": str,
        "sessions": List[SessionSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTrustStoresResponseTypeDef = TypedDict(
    "ListTrustStoresResponseTypeDef",
    {
        "nextToken": str,
        "trustStores": List[TrustStoreSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListUserAccessLoggingSettingsResponseTypeDef = TypedDict(
    "ListUserAccessLoggingSettingsResponseTypeDef",
    {
        "nextToken": str,
        "userAccessLoggingSettings": List[UserAccessLoggingSettingsSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UserSettingsSummaryTypeDef = TypedDict(
    "UserSettingsSummaryTypeDef",
    {
        "userSettingsArn": str,
        "cookieSynchronizationConfiguration": NotRequired[
            CookieSynchronizationConfigurationOutputTypeDef
        ],
        "copyAllowed": NotRequired[EnabledTypeType],
        "deepLinkAllowed": NotRequired[EnabledTypeType],
        "disconnectTimeoutInMinutes": NotRequired[int],
        "downloadAllowed": NotRequired[EnabledTypeType],
        "idleDisconnectTimeoutInMinutes": NotRequired[int],
        "pasteAllowed": NotRequired[EnabledTypeType],
        "printAllowed": NotRequired[EnabledTypeType],
        "uploadAllowed": NotRequired[EnabledTypeType],
    },
)
UserSettingsTypeDef = TypedDict(
    "UserSettingsTypeDef",
    {
        "userSettingsArn": str,
        "additionalEncryptionContext": NotRequired[Dict[str, str]],
        "associatedPortalArns": NotRequired[List[str]],
        "cookieSynchronizationConfiguration": NotRequired[
            CookieSynchronizationConfigurationOutputTypeDef
        ],
        "copyAllowed": NotRequired[EnabledTypeType],
        "customerManagedKey": NotRequired[str],
        "deepLinkAllowed": NotRequired[EnabledTypeType],
        "disconnectTimeoutInMinutes": NotRequired[int],
        "downloadAllowed": NotRequired[EnabledTypeType],
        "idleDisconnectTimeoutInMinutes": NotRequired[int],
        "pasteAllowed": NotRequired[EnabledTypeType],
        "printAllowed": NotRequired[EnabledTypeType],
        "uploadAllowed": NotRequired[EnabledTypeType],
    },
)
CreateUserSettingsRequestRequestTypeDef = TypedDict(
    "CreateUserSettingsRequestRequestTypeDef",
    {
        "copyAllowed": EnabledTypeType,
        "downloadAllowed": EnabledTypeType,
        "pasteAllowed": EnabledTypeType,
        "printAllowed": EnabledTypeType,
        "uploadAllowed": EnabledTypeType,
        "additionalEncryptionContext": NotRequired[Mapping[str, str]],
        "clientToken": NotRequired[str],
        "cookieSynchronizationConfiguration": NotRequired[
            CookieSynchronizationConfigurationTypeDef
        ],
        "customerManagedKey": NotRequired[str],
        "deepLinkAllowed": NotRequired[EnabledTypeType],
        "disconnectTimeoutInMinutes": NotRequired[int],
        "idleDisconnectTimeoutInMinutes": NotRequired[int],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
UpdateUserSettingsRequestRequestTypeDef = TypedDict(
    "UpdateUserSettingsRequestRequestTypeDef",
    {
        "userSettingsArn": str,
        "clientToken": NotRequired[str],
        "cookieSynchronizationConfiguration": NotRequired[
            CookieSynchronizationConfigurationTypeDef
        ],
        "copyAllowed": NotRequired[EnabledTypeType],
        "deepLinkAllowed": NotRequired[EnabledTypeType],
        "disconnectTimeoutInMinutes": NotRequired[int],
        "downloadAllowed": NotRequired[EnabledTypeType],
        "idleDisconnectTimeoutInMinutes": NotRequired[int],
        "pasteAllowed": NotRequired[EnabledTypeType],
        "printAllowed": NotRequired[EnabledTypeType],
        "uploadAllowed": NotRequired[EnabledTypeType],
    },
)
GetIpAccessSettingsResponseTypeDef = TypedDict(
    "GetIpAccessSettingsResponseTypeDef",
    {
        "ipAccessSettings": IpAccessSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateIpAccessSettingsResponseTypeDef = TypedDict(
    "UpdateIpAccessSettingsResponseTypeDef",
    {
        "ipAccessSettings": IpAccessSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListUserSettingsResponseTypeDef = TypedDict(
    "ListUserSettingsResponseTypeDef",
    {
        "nextToken": str,
        "userSettings": List[UserSettingsSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetUserSettingsResponseTypeDef = TypedDict(
    "GetUserSettingsResponseTypeDef",
    {
        "userSettings": UserSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateUserSettingsResponseTypeDef = TypedDict(
    "UpdateUserSettingsResponseTypeDef",
    {
        "userSettings": UserSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
