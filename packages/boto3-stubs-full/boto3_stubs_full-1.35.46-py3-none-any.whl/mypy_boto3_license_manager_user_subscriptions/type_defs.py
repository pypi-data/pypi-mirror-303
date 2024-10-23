"""
Type annotations for license-manager-user-subscriptions service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_license_manager_user_subscriptions/type_defs/)

Usage::

    ```python
    from mypy_boto3_license_manager_user_subscriptions.type_defs import ActiveDirectoryIdentityProviderTypeDef

    data: ActiveDirectoryIdentityProviderTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Sequence

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "ActiveDirectoryIdentityProviderTypeDef",
    "ResponseMetadataTypeDef",
    "FilterTypeDef",
    "SettingsOutputTypeDef",
    "InstanceSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "ListIdentityProvidersRequestRequestTypeDef",
    "SettingsTypeDef",
    "UpdateSettingsTypeDef",
    "IdentityProviderTypeDef",
    "ListInstancesRequestRequestTypeDef",
    "ListInstancesResponseTypeDef",
    "ListIdentityProvidersRequestListIdentityProvidersPaginateTypeDef",
    "ListInstancesRequestListInstancesPaginateTypeDef",
    "AssociateUserRequestRequestTypeDef",
    "DeregisterIdentityProviderRequestRequestTypeDef",
    "DisassociateUserRequestRequestTypeDef",
    "IdentityProviderSummaryTypeDef",
    "InstanceUserSummaryTypeDef",
    "ListProductSubscriptionsRequestListProductSubscriptionsPaginateTypeDef",
    "ListProductSubscriptionsRequestRequestTypeDef",
    "ListUserAssociationsRequestListUserAssociationsPaginateTypeDef",
    "ListUserAssociationsRequestRequestTypeDef",
    "ProductUserSummaryTypeDef",
    "RegisterIdentityProviderRequestRequestTypeDef",
    "StartProductSubscriptionRequestRequestTypeDef",
    "StopProductSubscriptionRequestRequestTypeDef",
    "UpdateIdentityProviderSettingsRequestRequestTypeDef",
    "DeregisterIdentityProviderResponseTypeDef",
    "ListIdentityProvidersResponseTypeDef",
    "RegisterIdentityProviderResponseTypeDef",
    "UpdateIdentityProviderSettingsResponseTypeDef",
    "AssociateUserResponseTypeDef",
    "DisassociateUserResponseTypeDef",
    "ListUserAssociationsResponseTypeDef",
    "ListProductSubscriptionsResponseTypeDef",
    "StartProductSubscriptionResponseTypeDef",
    "StopProductSubscriptionResponseTypeDef",
)

ActiveDirectoryIdentityProviderTypeDef = TypedDict(
    "ActiveDirectoryIdentityProviderTypeDef",
    {
        "DirectoryId": NotRequired[str],
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
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Attribute": NotRequired[str],
        "Operation": NotRequired[str],
        "Value": NotRequired[str],
    },
)
SettingsOutputTypeDef = TypedDict(
    "SettingsOutputTypeDef",
    {
        "SecurityGroupId": str,
        "Subnets": List[str],
    },
)
InstanceSummaryTypeDef = TypedDict(
    "InstanceSummaryTypeDef",
    {
        "InstanceId": str,
        "Products": List[str],
        "Status": str,
        "LastStatusCheckDate": NotRequired[str],
        "StatusMessage": NotRequired[str],
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
ListIdentityProvidersRequestRequestTypeDef = TypedDict(
    "ListIdentityProvidersRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
SettingsTypeDef = TypedDict(
    "SettingsTypeDef",
    {
        "SecurityGroupId": str,
        "Subnets": Sequence[str],
    },
)
UpdateSettingsTypeDef = TypedDict(
    "UpdateSettingsTypeDef",
    {
        "AddSubnets": Sequence[str],
        "RemoveSubnets": Sequence[str],
        "SecurityGroupId": NotRequired[str],
    },
)
IdentityProviderTypeDef = TypedDict(
    "IdentityProviderTypeDef",
    {
        "ActiveDirectoryIdentityProvider": NotRequired[ActiveDirectoryIdentityProviderTypeDef],
    },
)
ListInstancesRequestRequestTypeDef = TypedDict(
    "ListInstancesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListInstancesResponseTypeDef = TypedDict(
    "ListInstancesResponseTypeDef",
    {
        "InstanceSummaries": List[InstanceSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListIdentityProvidersRequestListIdentityProvidersPaginateTypeDef = TypedDict(
    "ListIdentityProvidersRequestListIdentityProvidersPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListInstancesRequestListInstancesPaginateTypeDef = TypedDict(
    "ListInstancesRequestListInstancesPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
AssociateUserRequestRequestTypeDef = TypedDict(
    "AssociateUserRequestRequestTypeDef",
    {
        "IdentityProvider": IdentityProviderTypeDef,
        "InstanceId": str,
        "Username": str,
        "Domain": NotRequired[str],
    },
)
DeregisterIdentityProviderRequestRequestTypeDef = TypedDict(
    "DeregisterIdentityProviderRequestRequestTypeDef",
    {
        "IdentityProvider": IdentityProviderTypeDef,
        "Product": str,
    },
)
DisassociateUserRequestRequestTypeDef = TypedDict(
    "DisassociateUserRequestRequestTypeDef",
    {
        "IdentityProvider": IdentityProviderTypeDef,
        "InstanceId": str,
        "Username": str,
        "Domain": NotRequired[str],
    },
)
IdentityProviderSummaryTypeDef = TypedDict(
    "IdentityProviderSummaryTypeDef",
    {
        "IdentityProvider": IdentityProviderTypeDef,
        "Product": str,
        "Settings": SettingsOutputTypeDef,
        "Status": str,
        "FailureMessage": NotRequired[str],
    },
)
InstanceUserSummaryTypeDef = TypedDict(
    "InstanceUserSummaryTypeDef",
    {
        "IdentityProvider": IdentityProviderTypeDef,
        "InstanceId": str,
        "Status": str,
        "Username": str,
        "AssociationDate": NotRequired[str],
        "DisassociationDate": NotRequired[str],
        "Domain": NotRequired[str],
        "StatusMessage": NotRequired[str],
    },
)
ListProductSubscriptionsRequestListProductSubscriptionsPaginateTypeDef = TypedDict(
    "ListProductSubscriptionsRequestListProductSubscriptionsPaginateTypeDef",
    {
        "IdentityProvider": IdentityProviderTypeDef,
        "Product": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProductSubscriptionsRequestRequestTypeDef = TypedDict(
    "ListProductSubscriptionsRequestRequestTypeDef",
    {
        "IdentityProvider": IdentityProviderTypeDef,
        "Product": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListUserAssociationsRequestListUserAssociationsPaginateTypeDef = TypedDict(
    "ListUserAssociationsRequestListUserAssociationsPaginateTypeDef",
    {
        "IdentityProvider": IdentityProviderTypeDef,
        "InstanceId": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListUserAssociationsRequestRequestTypeDef = TypedDict(
    "ListUserAssociationsRequestRequestTypeDef",
    {
        "IdentityProvider": IdentityProviderTypeDef,
        "InstanceId": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ProductUserSummaryTypeDef = TypedDict(
    "ProductUserSummaryTypeDef",
    {
        "IdentityProvider": IdentityProviderTypeDef,
        "Product": str,
        "Status": str,
        "Username": str,
        "Domain": NotRequired[str],
        "StatusMessage": NotRequired[str],
        "SubscriptionEndDate": NotRequired[str],
        "SubscriptionStartDate": NotRequired[str],
    },
)
RegisterIdentityProviderRequestRequestTypeDef = TypedDict(
    "RegisterIdentityProviderRequestRequestTypeDef",
    {
        "IdentityProvider": IdentityProviderTypeDef,
        "Product": str,
        "Settings": NotRequired[SettingsTypeDef],
    },
)
StartProductSubscriptionRequestRequestTypeDef = TypedDict(
    "StartProductSubscriptionRequestRequestTypeDef",
    {
        "IdentityProvider": IdentityProviderTypeDef,
        "Product": str,
        "Username": str,
        "Domain": NotRequired[str],
    },
)
StopProductSubscriptionRequestRequestTypeDef = TypedDict(
    "StopProductSubscriptionRequestRequestTypeDef",
    {
        "IdentityProvider": IdentityProviderTypeDef,
        "Product": str,
        "Username": str,
        "Domain": NotRequired[str],
    },
)
UpdateIdentityProviderSettingsRequestRequestTypeDef = TypedDict(
    "UpdateIdentityProviderSettingsRequestRequestTypeDef",
    {
        "IdentityProvider": IdentityProviderTypeDef,
        "Product": str,
        "UpdateSettings": UpdateSettingsTypeDef,
    },
)
DeregisterIdentityProviderResponseTypeDef = TypedDict(
    "DeregisterIdentityProviderResponseTypeDef",
    {
        "IdentityProviderSummary": IdentityProviderSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListIdentityProvidersResponseTypeDef = TypedDict(
    "ListIdentityProvidersResponseTypeDef",
    {
        "IdentityProviderSummaries": List[IdentityProviderSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
RegisterIdentityProviderResponseTypeDef = TypedDict(
    "RegisterIdentityProviderResponseTypeDef",
    {
        "IdentityProviderSummary": IdentityProviderSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateIdentityProviderSettingsResponseTypeDef = TypedDict(
    "UpdateIdentityProviderSettingsResponseTypeDef",
    {
        "IdentityProviderSummary": IdentityProviderSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateUserResponseTypeDef = TypedDict(
    "AssociateUserResponseTypeDef",
    {
        "InstanceUserSummary": InstanceUserSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateUserResponseTypeDef = TypedDict(
    "DisassociateUserResponseTypeDef",
    {
        "InstanceUserSummary": InstanceUserSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListUserAssociationsResponseTypeDef = TypedDict(
    "ListUserAssociationsResponseTypeDef",
    {
        "InstanceUserSummaries": List[InstanceUserSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListProductSubscriptionsResponseTypeDef = TypedDict(
    "ListProductSubscriptionsResponseTypeDef",
    {
        "ProductUserSummaries": List[ProductUserSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
StartProductSubscriptionResponseTypeDef = TypedDict(
    "StartProductSubscriptionResponseTypeDef",
    {
        "ProductUserSummary": ProductUserSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopProductSubscriptionResponseTypeDef = TypedDict(
    "StopProductSubscriptionResponseTypeDef",
    {
        "ProductUserSummary": ProductUserSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
