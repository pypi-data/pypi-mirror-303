"""
Type annotations for ram service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ram/type_defs/)

Usage::

    ```python
    from mypy_boto3_ram.type_defs import AcceptResourceShareInvitationRequestRequestTypeDef

    data: AcceptResourceShareInvitationRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import (
    PermissionFeatureSetType,
    PermissionStatusType,
    PermissionTypeFilterType,
    PermissionTypeType,
    ReplacePermissionAssociationsWorkStatusType,
    ResourceOwnerType,
    ResourceRegionScopeFilterType,
    ResourceRegionScopeType,
    ResourceShareAssociationStatusType,
    ResourceShareAssociationTypeType,
    ResourceShareFeatureSetType,
    ResourceShareInvitationStatusType,
    ResourceShareStatusType,
    ResourceStatusType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AcceptResourceShareInvitationRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "AssociateResourceSharePermissionRequestRequestTypeDef",
    "AssociateResourceShareRequestRequestTypeDef",
    "ResourceShareAssociationTypeDef",
    "AssociatedPermissionTypeDef",
    "TagTypeDef",
    "CreatePermissionVersionRequestRequestTypeDef",
    "DeletePermissionRequestRequestTypeDef",
    "DeletePermissionVersionRequestRequestTypeDef",
    "DeleteResourceShareRequestRequestTypeDef",
    "DisassociateResourceSharePermissionRequestRequestTypeDef",
    "DisassociateResourceShareRequestRequestTypeDef",
    "GetPermissionRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "GetResourcePoliciesRequestRequestTypeDef",
    "GetResourceShareAssociationsRequestRequestTypeDef",
    "GetResourceShareInvitationsRequestRequestTypeDef",
    "TagFilterTypeDef",
    "ListPendingInvitationResourcesRequestRequestTypeDef",
    "ResourceTypeDef",
    "ListPermissionAssociationsRequestRequestTypeDef",
    "ListPermissionVersionsRequestRequestTypeDef",
    "ListPermissionsRequestRequestTypeDef",
    "ListPrincipalsRequestRequestTypeDef",
    "PrincipalTypeDef",
    "ListReplacePermissionAssociationsWorkRequestRequestTypeDef",
    "ReplacePermissionAssociationsWorkTypeDef",
    "ListResourceSharePermissionsRequestRequestTypeDef",
    "ListResourceTypesRequestRequestTypeDef",
    "ServiceNameAndResourceTypeTypeDef",
    "ListResourcesRequestRequestTypeDef",
    "PromotePermissionCreatedFromPolicyRequestRequestTypeDef",
    "PromoteResourceShareCreatedFromPolicyRequestRequestTypeDef",
    "RejectResourceShareInvitationRequestRequestTypeDef",
    "ReplacePermissionAssociationsRequestRequestTypeDef",
    "SetDefaultPermissionVersionRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateResourceShareRequestRequestTypeDef",
    "AssociateResourceSharePermissionResponseTypeDef",
    "DeletePermissionResponseTypeDef",
    "DeletePermissionVersionResponseTypeDef",
    "DeleteResourceShareResponseTypeDef",
    "DisassociateResourceSharePermissionResponseTypeDef",
    "EnableSharingWithAwsOrganizationResponseTypeDef",
    "GetResourcePoliciesResponseTypeDef",
    "PromoteResourceShareCreatedFromPolicyResponseTypeDef",
    "SetDefaultPermissionVersionResponseTypeDef",
    "AssociateResourceShareResponseTypeDef",
    "DisassociateResourceShareResponseTypeDef",
    "GetResourceShareAssociationsResponseTypeDef",
    "ResourceShareInvitationTypeDef",
    "ListPermissionAssociationsResponseTypeDef",
    "CreatePermissionRequestRequestTypeDef",
    "CreateResourceShareRequestRequestTypeDef",
    "ResourceSharePermissionDetailTypeDef",
    "ResourceSharePermissionSummaryTypeDef",
    "ResourceShareTypeDef",
    "TagResourceRequestRequestTypeDef",
    "GetResourcePoliciesRequestGetResourcePoliciesPaginateTypeDef",
    "GetResourceShareAssociationsRequestGetResourceShareAssociationsPaginateTypeDef",
    "GetResourceShareInvitationsRequestGetResourceShareInvitationsPaginateTypeDef",
    "ListPrincipalsRequestListPrincipalsPaginateTypeDef",
    "ListResourcesRequestListResourcesPaginateTypeDef",
    "GetResourceSharesRequestGetResourceSharesPaginateTypeDef",
    "GetResourceSharesRequestRequestTypeDef",
    "ListPendingInvitationResourcesResponseTypeDef",
    "ListResourcesResponseTypeDef",
    "ListPrincipalsResponseTypeDef",
    "ListReplacePermissionAssociationsWorkResponseTypeDef",
    "ReplacePermissionAssociationsResponseTypeDef",
    "ListResourceTypesResponseTypeDef",
    "AcceptResourceShareInvitationResponseTypeDef",
    "GetResourceShareInvitationsResponseTypeDef",
    "RejectResourceShareInvitationResponseTypeDef",
    "CreatePermissionVersionResponseTypeDef",
    "GetPermissionResponseTypeDef",
    "CreatePermissionResponseTypeDef",
    "ListPermissionVersionsResponseTypeDef",
    "ListPermissionsResponseTypeDef",
    "ListResourceSharePermissionsResponseTypeDef",
    "PromotePermissionCreatedFromPolicyResponseTypeDef",
    "CreateResourceShareResponseTypeDef",
    "GetResourceSharesResponseTypeDef",
    "UpdateResourceShareResponseTypeDef",
)

AcceptResourceShareInvitationRequestRequestTypeDef = TypedDict(
    "AcceptResourceShareInvitationRequestRequestTypeDef",
    {
        "resourceShareInvitationArn": str,
        "clientToken": NotRequired[str],
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
AssociateResourceSharePermissionRequestRequestTypeDef = TypedDict(
    "AssociateResourceSharePermissionRequestRequestTypeDef",
    {
        "resourceShareArn": str,
        "permissionArn": str,
        "replace": NotRequired[bool],
        "clientToken": NotRequired[str],
        "permissionVersion": NotRequired[int],
    },
)
AssociateResourceShareRequestRequestTypeDef = TypedDict(
    "AssociateResourceShareRequestRequestTypeDef",
    {
        "resourceShareArn": str,
        "resourceArns": NotRequired[Sequence[str]],
        "principals": NotRequired[Sequence[str]],
        "clientToken": NotRequired[str],
        "sources": NotRequired[Sequence[str]],
    },
)
ResourceShareAssociationTypeDef = TypedDict(
    "ResourceShareAssociationTypeDef",
    {
        "resourceShareArn": NotRequired[str],
        "resourceShareName": NotRequired[str],
        "associatedEntity": NotRequired[str],
        "associationType": NotRequired[ResourceShareAssociationTypeType],
        "status": NotRequired[ResourceShareAssociationStatusType],
        "statusMessage": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdatedTime": NotRequired[datetime],
        "external": NotRequired[bool],
    },
)
AssociatedPermissionTypeDef = TypedDict(
    "AssociatedPermissionTypeDef",
    {
        "arn": NotRequired[str],
        "permissionVersion": NotRequired[str],
        "defaultVersion": NotRequired[bool],
        "resourceType": NotRequired[str],
        "status": NotRequired[str],
        "featureSet": NotRequired[PermissionFeatureSetType],
        "lastUpdatedTime": NotRequired[datetime],
        "resourceShareArn": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[str],
    },
)
CreatePermissionVersionRequestRequestTypeDef = TypedDict(
    "CreatePermissionVersionRequestRequestTypeDef",
    {
        "permissionArn": str,
        "policyTemplate": str,
        "clientToken": NotRequired[str],
    },
)
DeletePermissionRequestRequestTypeDef = TypedDict(
    "DeletePermissionRequestRequestTypeDef",
    {
        "permissionArn": str,
        "clientToken": NotRequired[str],
    },
)
DeletePermissionVersionRequestRequestTypeDef = TypedDict(
    "DeletePermissionVersionRequestRequestTypeDef",
    {
        "permissionArn": str,
        "permissionVersion": int,
        "clientToken": NotRequired[str],
    },
)
DeleteResourceShareRequestRequestTypeDef = TypedDict(
    "DeleteResourceShareRequestRequestTypeDef",
    {
        "resourceShareArn": str,
        "clientToken": NotRequired[str],
    },
)
DisassociateResourceSharePermissionRequestRequestTypeDef = TypedDict(
    "DisassociateResourceSharePermissionRequestRequestTypeDef",
    {
        "resourceShareArn": str,
        "permissionArn": str,
        "clientToken": NotRequired[str],
    },
)
DisassociateResourceShareRequestRequestTypeDef = TypedDict(
    "DisassociateResourceShareRequestRequestTypeDef",
    {
        "resourceShareArn": str,
        "resourceArns": NotRequired[Sequence[str]],
        "principals": NotRequired[Sequence[str]],
        "clientToken": NotRequired[str],
        "sources": NotRequired[Sequence[str]],
    },
)
GetPermissionRequestRequestTypeDef = TypedDict(
    "GetPermissionRequestRequestTypeDef",
    {
        "permissionArn": str,
        "permissionVersion": NotRequired[int],
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
GetResourcePoliciesRequestRequestTypeDef = TypedDict(
    "GetResourcePoliciesRequestRequestTypeDef",
    {
        "resourceArns": Sequence[str],
        "principal": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
GetResourceShareAssociationsRequestRequestTypeDef = TypedDict(
    "GetResourceShareAssociationsRequestRequestTypeDef",
    {
        "associationType": ResourceShareAssociationTypeType,
        "resourceShareArns": NotRequired[Sequence[str]],
        "resourceArn": NotRequired[str],
        "principal": NotRequired[str],
        "associationStatus": NotRequired[ResourceShareAssociationStatusType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
GetResourceShareInvitationsRequestRequestTypeDef = TypedDict(
    "GetResourceShareInvitationsRequestRequestTypeDef",
    {
        "resourceShareInvitationArns": NotRequired[Sequence[str]],
        "resourceShareArns": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
TagFilterTypeDef = TypedDict(
    "TagFilterTypeDef",
    {
        "tagKey": NotRequired[str],
        "tagValues": NotRequired[Sequence[str]],
    },
)
ListPendingInvitationResourcesRequestRequestTypeDef = TypedDict(
    "ListPendingInvitationResourcesRequestRequestTypeDef",
    {
        "resourceShareInvitationArn": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "resourceRegionScope": NotRequired[ResourceRegionScopeFilterType],
    },
)
ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "arn": NotRequired[str],
        "type": NotRequired[str],
        "resourceShareArn": NotRequired[str],
        "resourceGroupArn": NotRequired[str],
        "status": NotRequired[ResourceStatusType],
        "statusMessage": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdatedTime": NotRequired[datetime],
        "resourceRegionScope": NotRequired[ResourceRegionScopeType],
    },
)
ListPermissionAssociationsRequestRequestTypeDef = TypedDict(
    "ListPermissionAssociationsRequestRequestTypeDef",
    {
        "permissionArn": NotRequired[str],
        "permissionVersion": NotRequired[int],
        "associationStatus": NotRequired[ResourceShareAssociationStatusType],
        "resourceType": NotRequired[str],
        "featureSet": NotRequired[PermissionFeatureSetType],
        "defaultVersion": NotRequired[bool],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListPermissionVersionsRequestRequestTypeDef = TypedDict(
    "ListPermissionVersionsRequestRequestTypeDef",
    {
        "permissionArn": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListPermissionsRequestRequestTypeDef = TypedDict(
    "ListPermissionsRequestRequestTypeDef",
    {
        "resourceType": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "permissionType": NotRequired[PermissionTypeFilterType],
    },
)
ListPrincipalsRequestRequestTypeDef = TypedDict(
    "ListPrincipalsRequestRequestTypeDef",
    {
        "resourceOwner": ResourceOwnerType,
        "resourceArn": NotRequired[str],
        "principals": NotRequired[Sequence[str]],
        "resourceType": NotRequired[str],
        "resourceShareArns": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
PrincipalTypeDef = TypedDict(
    "PrincipalTypeDef",
    {
        "id": NotRequired[str],
        "resourceShareArn": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdatedTime": NotRequired[datetime],
        "external": NotRequired[bool],
    },
)
ListReplacePermissionAssociationsWorkRequestRequestTypeDef = TypedDict(
    "ListReplacePermissionAssociationsWorkRequestRequestTypeDef",
    {
        "workIds": NotRequired[Sequence[str]],
        "status": NotRequired[ReplacePermissionAssociationsWorkStatusType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ReplacePermissionAssociationsWorkTypeDef = TypedDict(
    "ReplacePermissionAssociationsWorkTypeDef",
    {
        "id": NotRequired[str],
        "fromPermissionArn": NotRequired[str],
        "fromPermissionVersion": NotRequired[str],
        "toPermissionArn": NotRequired[str],
        "toPermissionVersion": NotRequired[str],
        "status": NotRequired[ReplacePermissionAssociationsWorkStatusType],
        "statusMessage": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdatedTime": NotRequired[datetime],
    },
)
ListResourceSharePermissionsRequestRequestTypeDef = TypedDict(
    "ListResourceSharePermissionsRequestRequestTypeDef",
    {
        "resourceShareArn": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListResourceTypesRequestRequestTypeDef = TypedDict(
    "ListResourceTypesRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "resourceRegionScope": NotRequired[ResourceRegionScopeFilterType],
    },
)
ServiceNameAndResourceTypeTypeDef = TypedDict(
    "ServiceNameAndResourceTypeTypeDef",
    {
        "resourceType": NotRequired[str],
        "serviceName": NotRequired[str],
        "resourceRegionScope": NotRequired[ResourceRegionScopeType],
    },
)
ListResourcesRequestRequestTypeDef = TypedDict(
    "ListResourcesRequestRequestTypeDef",
    {
        "resourceOwner": ResourceOwnerType,
        "principal": NotRequired[str],
        "resourceType": NotRequired[str],
        "resourceArns": NotRequired[Sequence[str]],
        "resourceShareArns": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "resourceRegionScope": NotRequired[ResourceRegionScopeFilterType],
    },
)
PromotePermissionCreatedFromPolicyRequestRequestTypeDef = TypedDict(
    "PromotePermissionCreatedFromPolicyRequestRequestTypeDef",
    {
        "permissionArn": str,
        "name": str,
        "clientToken": NotRequired[str],
    },
)
PromoteResourceShareCreatedFromPolicyRequestRequestTypeDef = TypedDict(
    "PromoteResourceShareCreatedFromPolicyRequestRequestTypeDef",
    {
        "resourceShareArn": str,
    },
)
RejectResourceShareInvitationRequestRequestTypeDef = TypedDict(
    "RejectResourceShareInvitationRequestRequestTypeDef",
    {
        "resourceShareInvitationArn": str,
        "clientToken": NotRequired[str],
    },
)
ReplacePermissionAssociationsRequestRequestTypeDef = TypedDict(
    "ReplacePermissionAssociationsRequestRequestTypeDef",
    {
        "fromPermissionArn": str,
        "toPermissionArn": str,
        "fromPermissionVersion": NotRequired[int],
        "clientToken": NotRequired[str],
    },
)
SetDefaultPermissionVersionRequestRequestTypeDef = TypedDict(
    "SetDefaultPermissionVersionRequestRequestTypeDef",
    {
        "permissionArn": str,
        "permissionVersion": int,
        "clientToken": NotRequired[str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "tagKeys": Sequence[str],
        "resourceShareArn": NotRequired[str],
        "resourceArn": NotRequired[str],
    },
)
UpdateResourceShareRequestRequestTypeDef = TypedDict(
    "UpdateResourceShareRequestRequestTypeDef",
    {
        "resourceShareArn": str,
        "name": NotRequired[str],
        "allowExternalPrincipals": NotRequired[bool],
        "clientToken": NotRequired[str],
    },
)
AssociateResourceSharePermissionResponseTypeDef = TypedDict(
    "AssociateResourceSharePermissionResponseTypeDef",
    {
        "returnValue": bool,
        "clientToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeletePermissionResponseTypeDef = TypedDict(
    "DeletePermissionResponseTypeDef",
    {
        "returnValue": bool,
        "clientToken": str,
        "permissionStatus": PermissionStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeletePermissionVersionResponseTypeDef = TypedDict(
    "DeletePermissionVersionResponseTypeDef",
    {
        "returnValue": bool,
        "clientToken": str,
        "permissionStatus": PermissionStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteResourceShareResponseTypeDef = TypedDict(
    "DeleteResourceShareResponseTypeDef",
    {
        "returnValue": bool,
        "clientToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateResourceSharePermissionResponseTypeDef = TypedDict(
    "DisassociateResourceSharePermissionResponseTypeDef",
    {
        "returnValue": bool,
        "clientToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableSharingWithAwsOrganizationResponseTypeDef = TypedDict(
    "EnableSharingWithAwsOrganizationResponseTypeDef",
    {
        "returnValue": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResourcePoliciesResponseTypeDef = TypedDict(
    "GetResourcePoliciesResponseTypeDef",
    {
        "policies": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PromoteResourceShareCreatedFromPolicyResponseTypeDef = TypedDict(
    "PromoteResourceShareCreatedFromPolicyResponseTypeDef",
    {
        "returnValue": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SetDefaultPermissionVersionResponseTypeDef = TypedDict(
    "SetDefaultPermissionVersionResponseTypeDef",
    {
        "returnValue": bool,
        "clientToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateResourceShareResponseTypeDef = TypedDict(
    "AssociateResourceShareResponseTypeDef",
    {
        "resourceShareAssociations": List[ResourceShareAssociationTypeDef],
        "clientToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateResourceShareResponseTypeDef = TypedDict(
    "DisassociateResourceShareResponseTypeDef",
    {
        "resourceShareAssociations": List[ResourceShareAssociationTypeDef],
        "clientToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResourceShareAssociationsResponseTypeDef = TypedDict(
    "GetResourceShareAssociationsResponseTypeDef",
    {
        "resourceShareAssociations": List[ResourceShareAssociationTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResourceShareInvitationTypeDef = TypedDict(
    "ResourceShareInvitationTypeDef",
    {
        "resourceShareInvitationArn": NotRequired[str],
        "resourceShareName": NotRequired[str],
        "resourceShareArn": NotRequired[str],
        "senderAccountId": NotRequired[str],
        "receiverAccountId": NotRequired[str],
        "invitationTimestamp": NotRequired[datetime],
        "status": NotRequired[ResourceShareInvitationStatusType],
        "resourceShareAssociations": NotRequired[List[ResourceShareAssociationTypeDef]],
        "receiverArn": NotRequired[str],
    },
)
ListPermissionAssociationsResponseTypeDef = TypedDict(
    "ListPermissionAssociationsResponseTypeDef",
    {
        "permissions": List[AssociatedPermissionTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePermissionRequestRequestTypeDef = TypedDict(
    "CreatePermissionRequestRequestTypeDef",
    {
        "name": str,
        "resourceType": str,
        "policyTemplate": str,
        "clientToken": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateResourceShareRequestRequestTypeDef = TypedDict(
    "CreateResourceShareRequestRequestTypeDef",
    {
        "name": str,
        "resourceArns": NotRequired[Sequence[str]],
        "principals": NotRequired[Sequence[str]],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "allowExternalPrincipals": NotRequired[bool],
        "clientToken": NotRequired[str],
        "permissionArns": NotRequired[Sequence[str]],
        "sources": NotRequired[Sequence[str]],
    },
)
ResourceSharePermissionDetailTypeDef = TypedDict(
    "ResourceSharePermissionDetailTypeDef",
    {
        "arn": NotRequired[str],
        "version": NotRequired[str],
        "defaultVersion": NotRequired[bool],
        "name": NotRequired[str],
        "resourceType": NotRequired[str],
        "permission": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdatedTime": NotRequired[datetime],
        "isResourceTypeDefault": NotRequired[bool],
        "permissionType": NotRequired[PermissionTypeType],
        "featureSet": NotRequired[PermissionFeatureSetType],
        "status": NotRequired[PermissionStatusType],
        "tags": NotRequired[List[TagTypeDef]],
    },
)
ResourceSharePermissionSummaryTypeDef = TypedDict(
    "ResourceSharePermissionSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "version": NotRequired[str],
        "defaultVersion": NotRequired[bool],
        "name": NotRequired[str],
        "resourceType": NotRequired[str],
        "status": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdatedTime": NotRequired[datetime],
        "isResourceTypeDefault": NotRequired[bool],
        "permissionType": NotRequired[PermissionTypeType],
        "featureSet": NotRequired[PermissionFeatureSetType],
        "tags": NotRequired[List[TagTypeDef]],
    },
)
ResourceShareTypeDef = TypedDict(
    "ResourceShareTypeDef",
    {
        "resourceShareArn": NotRequired[str],
        "name": NotRequired[str],
        "owningAccountId": NotRequired[str],
        "allowExternalPrincipals": NotRequired[bool],
        "status": NotRequired[ResourceShareStatusType],
        "statusMessage": NotRequired[str],
        "tags": NotRequired[List[TagTypeDef]],
        "creationTime": NotRequired[datetime],
        "lastUpdatedTime": NotRequired[datetime],
        "featureSet": NotRequired[ResourceShareFeatureSetType],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "tags": Sequence[TagTypeDef],
        "resourceShareArn": NotRequired[str],
        "resourceArn": NotRequired[str],
    },
)
GetResourcePoliciesRequestGetResourcePoliciesPaginateTypeDef = TypedDict(
    "GetResourcePoliciesRequestGetResourcePoliciesPaginateTypeDef",
    {
        "resourceArns": Sequence[str],
        "principal": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetResourceShareAssociationsRequestGetResourceShareAssociationsPaginateTypeDef = TypedDict(
    "GetResourceShareAssociationsRequestGetResourceShareAssociationsPaginateTypeDef",
    {
        "associationType": ResourceShareAssociationTypeType,
        "resourceShareArns": NotRequired[Sequence[str]],
        "resourceArn": NotRequired[str],
        "principal": NotRequired[str],
        "associationStatus": NotRequired[ResourceShareAssociationStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetResourceShareInvitationsRequestGetResourceShareInvitationsPaginateTypeDef = TypedDict(
    "GetResourceShareInvitationsRequestGetResourceShareInvitationsPaginateTypeDef",
    {
        "resourceShareInvitationArns": NotRequired[Sequence[str]],
        "resourceShareArns": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPrincipalsRequestListPrincipalsPaginateTypeDef = TypedDict(
    "ListPrincipalsRequestListPrincipalsPaginateTypeDef",
    {
        "resourceOwner": ResourceOwnerType,
        "resourceArn": NotRequired[str],
        "principals": NotRequired[Sequence[str]],
        "resourceType": NotRequired[str],
        "resourceShareArns": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResourcesRequestListResourcesPaginateTypeDef = TypedDict(
    "ListResourcesRequestListResourcesPaginateTypeDef",
    {
        "resourceOwner": ResourceOwnerType,
        "principal": NotRequired[str],
        "resourceType": NotRequired[str],
        "resourceArns": NotRequired[Sequence[str]],
        "resourceShareArns": NotRequired[Sequence[str]],
        "resourceRegionScope": NotRequired[ResourceRegionScopeFilterType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetResourceSharesRequestGetResourceSharesPaginateTypeDef = TypedDict(
    "GetResourceSharesRequestGetResourceSharesPaginateTypeDef",
    {
        "resourceOwner": ResourceOwnerType,
        "resourceShareArns": NotRequired[Sequence[str]],
        "resourceShareStatus": NotRequired[ResourceShareStatusType],
        "name": NotRequired[str],
        "tagFilters": NotRequired[Sequence[TagFilterTypeDef]],
        "permissionArn": NotRequired[str],
        "permissionVersion": NotRequired[int],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetResourceSharesRequestRequestTypeDef = TypedDict(
    "GetResourceSharesRequestRequestTypeDef",
    {
        "resourceOwner": ResourceOwnerType,
        "resourceShareArns": NotRequired[Sequence[str]],
        "resourceShareStatus": NotRequired[ResourceShareStatusType],
        "name": NotRequired[str],
        "tagFilters": NotRequired[Sequence[TagFilterTypeDef]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "permissionArn": NotRequired[str],
        "permissionVersion": NotRequired[int],
    },
)
ListPendingInvitationResourcesResponseTypeDef = TypedDict(
    "ListPendingInvitationResourcesResponseTypeDef",
    {
        "resources": List[ResourceTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListResourcesResponseTypeDef = TypedDict(
    "ListResourcesResponseTypeDef",
    {
        "resources": List[ResourceTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPrincipalsResponseTypeDef = TypedDict(
    "ListPrincipalsResponseTypeDef",
    {
        "principals": List[PrincipalTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListReplacePermissionAssociationsWorkResponseTypeDef = TypedDict(
    "ListReplacePermissionAssociationsWorkResponseTypeDef",
    {
        "replacePermissionAssociationsWorks": List[ReplacePermissionAssociationsWorkTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReplacePermissionAssociationsResponseTypeDef = TypedDict(
    "ReplacePermissionAssociationsResponseTypeDef",
    {
        "replacePermissionAssociationsWork": ReplacePermissionAssociationsWorkTypeDef,
        "clientToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListResourceTypesResponseTypeDef = TypedDict(
    "ListResourceTypesResponseTypeDef",
    {
        "resourceTypes": List[ServiceNameAndResourceTypeTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AcceptResourceShareInvitationResponseTypeDef = TypedDict(
    "AcceptResourceShareInvitationResponseTypeDef",
    {
        "resourceShareInvitation": ResourceShareInvitationTypeDef,
        "clientToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResourceShareInvitationsResponseTypeDef = TypedDict(
    "GetResourceShareInvitationsResponseTypeDef",
    {
        "resourceShareInvitations": List[ResourceShareInvitationTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RejectResourceShareInvitationResponseTypeDef = TypedDict(
    "RejectResourceShareInvitationResponseTypeDef",
    {
        "resourceShareInvitation": ResourceShareInvitationTypeDef,
        "clientToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePermissionVersionResponseTypeDef = TypedDict(
    "CreatePermissionVersionResponseTypeDef",
    {
        "permission": ResourceSharePermissionDetailTypeDef,
        "clientToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPermissionResponseTypeDef = TypedDict(
    "GetPermissionResponseTypeDef",
    {
        "permission": ResourceSharePermissionDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePermissionResponseTypeDef = TypedDict(
    "CreatePermissionResponseTypeDef",
    {
        "permission": ResourceSharePermissionSummaryTypeDef,
        "clientToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPermissionVersionsResponseTypeDef = TypedDict(
    "ListPermissionVersionsResponseTypeDef",
    {
        "permissions": List[ResourceSharePermissionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPermissionsResponseTypeDef = TypedDict(
    "ListPermissionsResponseTypeDef",
    {
        "permissions": List[ResourceSharePermissionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListResourceSharePermissionsResponseTypeDef = TypedDict(
    "ListResourceSharePermissionsResponseTypeDef",
    {
        "permissions": List[ResourceSharePermissionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PromotePermissionCreatedFromPolicyResponseTypeDef = TypedDict(
    "PromotePermissionCreatedFromPolicyResponseTypeDef",
    {
        "permission": ResourceSharePermissionSummaryTypeDef,
        "clientToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateResourceShareResponseTypeDef = TypedDict(
    "CreateResourceShareResponseTypeDef",
    {
        "resourceShare": ResourceShareTypeDef,
        "clientToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResourceSharesResponseTypeDef = TypedDict(
    "GetResourceSharesResponseTypeDef",
    {
        "resourceShares": List[ResourceShareTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateResourceShareResponseTypeDef = TypedDict(
    "UpdateResourceShareResponseTypeDef",
    {
        "resourceShare": ResourceShareTypeDef,
        "clientToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
