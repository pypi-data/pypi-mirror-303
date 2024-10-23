"""
Type annotations for workdocs service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/type_defs/)

Usage::

    ```python
    from mypy_boto3_workdocs.type_defs import AbortDocumentVersionUploadRequestRequestTypeDef

    data: AbortDocumentVersionUploadRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    ActivityTypeType,
    BooleanEnumTypeType,
    CommentStatusTypeType,
    CommentVisibilityTypeType,
    ContentCategoryTypeType,
    DocumentSourceTypeType,
    DocumentStatusTypeType,
    DocumentThumbnailTypeType,
    FolderContentTypeType,
    LanguageCodeTypeType,
    LocaleTypeType,
    OrderByFieldTypeType,
    OrderTypeType,
    PrincipalRoleTypeType,
    PrincipalTypeType,
    ResourceSortTypeType,
    ResourceStateTypeType,
    ResourceTypeType,
    ResponseItemTypeType,
    RolePermissionTypeType,
    RoleTypeType,
    SearchCollectionTypeType,
    SearchQueryScopeTypeType,
    SearchResourceTypeType,
    ShareStatusTypeType,
    SortOrderType,
    StorageTypeType,
    SubscriptionProtocolTypeType,
    UserFilterTypeType,
    UserSortTypeType,
    UserStatusTypeType,
    UserTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AbortDocumentVersionUploadRequestRequestTypeDef",
    "ActivateUserRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "UserMetadataTypeDef",
    "NotificationOptionsTypeDef",
    "SharePrincipalTypeDef",
    "ShareResultTypeDef",
    "CreateCommentRequestRequestTypeDef",
    "CreateCustomMetadataRequestRequestTypeDef",
    "CreateFolderRequestRequestTypeDef",
    "FolderMetadataTypeDef",
    "CreateLabelsRequestRequestTypeDef",
    "CreateNotificationSubscriptionRequestRequestTypeDef",
    "SubscriptionTypeDef",
    "StorageRuleTypeTypeDef",
    "TimestampTypeDef",
    "DeactivateUserRequestRequestTypeDef",
    "DeleteCommentRequestRequestTypeDef",
    "DeleteCustomMetadataRequestRequestTypeDef",
    "DeleteDocumentRequestRequestTypeDef",
    "DeleteDocumentVersionRequestRequestTypeDef",
    "DeleteFolderContentsRequestRequestTypeDef",
    "DeleteFolderRequestRequestTypeDef",
    "DeleteLabelsRequestRequestTypeDef",
    "DeleteNotificationSubscriptionRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeCommentsRequestRequestTypeDef",
    "DescribeDocumentVersionsRequestRequestTypeDef",
    "DocumentVersionMetadataTypeDef",
    "DescribeFolderContentsRequestRequestTypeDef",
    "DescribeGroupsRequestRequestTypeDef",
    "GroupMetadataTypeDef",
    "DescribeNotificationSubscriptionsRequestRequestTypeDef",
    "DescribeResourcePermissionsRequestRequestTypeDef",
    "DescribeRootFoldersRequestRequestTypeDef",
    "DescribeUsersRequestRequestTypeDef",
    "LongRangeTypeTypeDef",
    "SearchPrincipalTypeTypeDef",
    "GetCurrentUserRequestRequestTypeDef",
    "GetDocumentPathRequestRequestTypeDef",
    "GetDocumentRequestRequestTypeDef",
    "GetDocumentVersionRequestRequestTypeDef",
    "GetFolderPathRequestRequestTypeDef",
    "GetFolderRequestRequestTypeDef",
    "GetResourcesRequestRequestTypeDef",
    "UploadMetadataTypeDef",
    "PermissionInfoTypeDef",
    "RemoveAllResourcePermissionsRequestRequestTypeDef",
    "RemoveResourcePermissionRequestRequestTypeDef",
    "ResourcePathComponentTypeDef",
    "RestoreDocumentVersionsRequestRequestTypeDef",
    "SearchSortResultTypeDef",
    "UpdateDocumentRequestRequestTypeDef",
    "UpdateDocumentVersionRequestRequestTypeDef",
    "UpdateFolderRequestRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ResourceMetadataTypeDef",
    "AddResourcePermissionsRequestRequestTypeDef",
    "AddResourcePermissionsResponseTypeDef",
    "CreateFolderResponseTypeDef",
    "DescribeRootFoldersResponseTypeDef",
    "GetFolderResponseTypeDef",
    "CreateNotificationSubscriptionResponseTypeDef",
    "DescribeNotificationSubscriptionsResponseTypeDef",
    "CreateUserRequestRequestTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "UserStorageMetadataTypeDef",
    "DateRangeTypeTypeDef",
    "DescribeActivitiesRequestRequestTypeDef",
    "InitiateDocumentVersionUploadRequestRequestTypeDef",
    "DescribeActivitiesRequestDescribeActivitiesPaginateTypeDef",
    "DescribeCommentsRequestDescribeCommentsPaginateTypeDef",
    "DescribeDocumentVersionsRequestDescribeDocumentVersionsPaginateTypeDef",
    "DescribeFolderContentsRequestDescribeFolderContentsPaginateTypeDef",
    "DescribeGroupsRequestDescribeGroupsPaginateTypeDef",
    "DescribeNotificationSubscriptionsRequestDescribeNotificationSubscriptionsPaginateTypeDef",
    "DescribeResourcePermissionsRequestDescribeResourcePermissionsPaginateTypeDef",
    "DescribeRootFoldersRequestDescribeRootFoldersPaginateTypeDef",
    "DescribeUsersRequestDescribeUsersPaginateTypeDef",
    "DescribeDocumentVersionsResponseTypeDef",
    "DocumentMetadataTypeDef",
    "GetDocumentVersionResponseTypeDef",
    "DescribeGroupsResponseTypeDef",
    "ParticipantsTypeDef",
    "PrincipalTypeDef",
    "ResourcePathTypeDef",
    "UserTypeDef",
    "FiltersTypeDef",
    "DescribeFolderContentsResponseTypeDef",
    "GetDocumentResponseTypeDef",
    "GetResourcesResponseTypeDef",
    "InitiateDocumentVersionUploadResponseTypeDef",
    "DescribeResourcePermissionsResponseTypeDef",
    "GetDocumentPathResponseTypeDef",
    "GetFolderPathResponseTypeDef",
    "ActivateUserResponseTypeDef",
    "CommentMetadataTypeDef",
    "CommentTypeDef",
    "CreateUserResponseTypeDef",
    "DescribeUsersResponseTypeDef",
    "GetCurrentUserResponseTypeDef",
    "UpdateUserResponseTypeDef",
    "SearchResourcesRequestRequestTypeDef",
    "SearchResourcesRequestSearchResourcesPaginateTypeDef",
    "ActivityTypeDef",
    "ResponseItemTypeDef",
    "CreateCommentResponseTypeDef",
    "DescribeCommentsResponseTypeDef",
    "DescribeActivitiesResponseTypeDef",
    "SearchResourcesResponseTypeDef",
)

AbortDocumentVersionUploadRequestRequestTypeDef = TypedDict(
    "AbortDocumentVersionUploadRequestRequestTypeDef",
    {
        "DocumentId": str,
        "VersionId": str,
        "AuthenticationToken": NotRequired[str],
    },
)
ActivateUserRequestRequestTypeDef = TypedDict(
    "ActivateUserRequestRequestTypeDef",
    {
        "UserId": str,
        "AuthenticationToken": NotRequired[str],
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
UserMetadataTypeDef = TypedDict(
    "UserMetadataTypeDef",
    {
        "Id": NotRequired[str],
        "Username": NotRequired[str],
        "GivenName": NotRequired[str],
        "Surname": NotRequired[str],
        "EmailAddress": NotRequired[str],
    },
)
NotificationOptionsTypeDef = TypedDict(
    "NotificationOptionsTypeDef",
    {
        "SendEmail": NotRequired[bool],
        "EmailMessage": NotRequired[str],
    },
)
SharePrincipalTypeDef = TypedDict(
    "SharePrincipalTypeDef",
    {
        "Id": str,
        "Type": PrincipalTypeType,
        "Role": RoleTypeType,
    },
)
ShareResultTypeDef = TypedDict(
    "ShareResultTypeDef",
    {
        "PrincipalId": NotRequired[str],
        "InviteePrincipalId": NotRequired[str],
        "Role": NotRequired[RoleTypeType],
        "Status": NotRequired[ShareStatusTypeType],
        "ShareId": NotRequired[str],
        "StatusMessage": NotRequired[str],
    },
)
CreateCommentRequestRequestTypeDef = TypedDict(
    "CreateCommentRequestRequestTypeDef",
    {
        "DocumentId": str,
        "VersionId": str,
        "Text": str,
        "AuthenticationToken": NotRequired[str],
        "ParentId": NotRequired[str],
        "ThreadId": NotRequired[str],
        "Visibility": NotRequired[CommentVisibilityTypeType],
        "NotifyCollaborators": NotRequired[bool],
    },
)
CreateCustomMetadataRequestRequestTypeDef = TypedDict(
    "CreateCustomMetadataRequestRequestTypeDef",
    {
        "ResourceId": str,
        "CustomMetadata": Mapping[str, str],
        "AuthenticationToken": NotRequired[str],
        "VersionId": NotRequired[str],
    },
)
CreateFolderRequestRequestTypeDef = TypedDict(
    "CreateFolderRequestRequestTypeDef",
    {
        "ParentFolderId": str,
        "AuthenticationToken": NotRequired[str],
        "Name": NotRequired[str],
    },
)
FolderMetadataTypeDef = TypedDict(
    "FolderMetadataTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "CreatorId": NotRequired[str],
        "ParentFolderId": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "ModifiedTimestamp": NotRequired[datetime],
        "ResourceState": NotRequired[ResourceStateTypeType],
        "Signature": NotRequired[str],
        "Labels": NotRequired[List[str]],
        "Size": NotRequired[int],
        "LatestVersionSize": NotRequired[int],
    },
)
CreateLabelsRequestRequestTypeDef = TypedDict(
    "CreateLabelsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "Labels": Sequence[str],
        "AuthenticationToken": NotRequired[str],
    },
)
CreateNotificationSubscriptionRequestRequestTypeDef = TypedDict(
    "CreateNotificationSubscriptionRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "Endpoint": str,
        "Protocol": SubscriptionProtocolTypeType,
        "SubscriptionType": Literal["ALL"],
    },
)
SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
    {
        "SubscriptionId": NotRequired[str],
        "EndPoint": NotRequired[str],
        "Protocol": NotRequired[SubscriptionProtocolTypeType],
    },
)
StorageRuleTypeTypeDef = TypedDict(
    "StorageRuleTypeTypeDef",
    {
        "StorageAllocatedInBytes": NotRequired[int],
        "StorageType": NotRequired[StorageTypeType],
    },
)
TimestampTypeDef = Union[datetime, str]
DeactivateUserRequestRequestTypeDef = TypedDict(
    "DeactivateUserRequestRequestTypeDef",
    {
        "UserId": str,
        "AuthenticationToken": NotRequired[str],
    },
)
DeleteCommentRequestRequestTypeDef = TypedDict(
    "DeleteCommentRequestRequestTypeDef",
    {
        "DocumentId": str,
        "VersionId": str,
        "CommentId": str,
        "AuthenticationToken": NotRequired[str],
    },
)
DeleteCustomMetadataRequestRequestTypeDef = TypedDict(
    "DeleteCustomMetadataRequestRequestTypeDef",
    {
        "ResourceId": str,
        "AuthenticationToken": NotRequired[str],
        "VersionId": NotRequired[str],
        "Keys": NotRequired[Sequence[str]],
        "DeleteAll": NotRequired[bool],
    },
)
DeleteDocumentRequestRequestTypeDef = TypedDict(
    "DeleteDocumentRequestRequestTypeDef",
    {
        "DocumentId": str,
        "AuthenticationToken": NotRequired[str],
    },
)
DeleteDocumentVersionRequestRequestTypeDef = TypedDict(
    "DeleteDocumentVersionRequestRequestTypeDef",
    {
        "DocumentId": str,
        "VersionId": str,
        "DeletePriorVersions": bool,
        "AuthenticationToken": NotRequired[str],
    },
)
DeleteFolderContentsRequestRequestTypeDef = TypedDict(
    "DeleteFolderContentsRequestRequestTypeDef",
    {
        "FolderId": str,
        "AuthenticationToken": NotRequired[str],
    },
)
DeleteFolderRequestRequestTypeDef = TypedDict(
    "DeleteFolderRequestRequestTypeDef",
    {
        "FolderId": str,
        "AuthenticationToken": NotRequired[str],
    },
)
DeleteLabelsRequestRequestTypeDef = TypedDict(
    "DeleteLabelsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "AuthenticationToken": NotRequired[str],
        "Labels": NotRequired[Sequence[str]],
        "DeleteAll": NotRequired[bool],
    },
)
DeleteNotificationSubscriptionRequestRequestTypeDef = TypedDict(
    "DeleteNotificationSubscriptionRequestRequestTypeDef",
    {
        "SubscriptionId": str,
        "OrganizationId": str,
    },
)
DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "UserId": str,
        "AuthenticationToken": NotRequired[str],
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
DescribeCommentsRequestRequestTypeDef = TypedDict(
    "DescribeCommentsRequestRequestTypeDef",
    {
        "DocumentId": str,
        "VersionId": str,
        "AuthenticationToken": NotRequired[str],
        "Limit": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeDocumentVersionsRequestRequestTypeDef = TypedDict(
    "DescribeDocumentVersionsRequestRequestTypeDef",
    {
        "DocumentId": str,
        "AuthenticationToken": NotRequired[str],
        "Marker": NotRequired[str],
        "Limit": NotRequired[int],
        "Include": NotRequired[str],
        "Fields": NotRequired[str],
    },
)
DocumentVersionMetadataTypeDef = TypedDict(
    "DocumentVersionMetadataTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "ContentType": NotRequired[str],
        "Size": NotRequired[int],
        "Signature": NotRequired[str],
        "Status": NotRequired[DocumentStatusTypeType],
        "CreatedTimestamp": NotRequired[datetime],
        "ModifiedTimestamp": NotRequired[datetime],
        "ContentCreatedTimestamp": NotRequired[datetime],
        "ContentModifiedTimestamp": NotRequired[datetime],
        "CreatorId": NotRequired[str],
        "Thumbnail": NotRequired[Dict[DocumentThumbnailTypeType, str]],
        "Source": NotRequired[Dict[DocumentSourceTypeType, str]],
    },
)
DescribeFolderContentsRequestRequestTypeDef = TypedDict(
    "DescribeFolderContentsRequestRequestTypeDef",
    {
        "FolderId": str,
        "AuthenticationToken": NotRequired[str],
        "Sort": NotRequired[ResourceSortTypeType],
        "Order": NotRequired[OrderTypeType],
        "Limit": NotRequired[int],
        "Marker": NotRequired[str],
        "Type": NotRequired[FolderContentTypeType],
        "Include": NotRequired[str],
    },
)
DescribeGroupsRequestRequestTypeDef = TypedDict(
    "DescribeGroupsRequestRequestTypeDef",
    {
        "SearchQuery": str,
        "AuthenticationToken": NotRequired[str],
        "OrganizationId": NotRequired[str],
        "Marker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
GroupMetadataTypeDef = TypedDict(
    "GroupMetadataTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
    },
)
DescribeNotificationSubscriptionsRequestRequestTypeDef = TypedDict(
    "DescribeNotificationSubscriptionsRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "Marker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)
DescribeResourcePermissionsRequestRequestTypeDef = TypedDict(
    "DescribeResourcePermissionsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "AuthenticationToken": NotRequired[str],
        "PrincipalId": NotRequired[str],
        "Limit": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeRootFoldersRequestRequestTypeDef = TypedDict(
    "DescribeRootFoldersRequestRequestTypeDef",
    {
        "AuthenticationToken": str,
        "Limit": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
DescribeUsersRequestRequestTypeDef = TypedDict(
    "DescribeUsersRequestRequestTypeDef",
    {
        "AuthenticationToken": NotRequired[str],
        "OrganizationId": NotRequired[str],
        "UserIds": NotRequired[str],
        "Query": NotRequired[str],
        "Include": NotRequired[UserFilterTypeType],
        "Order": NotRequired[OrderTypeType],
        "Sort": NotRequired[UserSortTypeType],
        "Marker": NotRequired[str],
        "Limit": NotRequired[int],
        "Fields": NotRequired[str],
    },
)
LongRangeTypeTypeDef = TypedDict(
    "LongRangeTypeTypeDef",
    {
        "StartValue": NotRequired[int],
        "EndValue": NotRequired[int],
    },
)
SearchPrincipalTypeTypeDef = TypedDict(
    "SearchPrincipalTypeTypeDef",
    {
        "Id": str,
        "Roles": NotRequired[Sequence[PrincipalRoleTypeType]],
    },
)
GetCurrentUserRequestRequestTypeDef = TypedDict(
    "GetCurrentUserRequestRequestTypeDef",
    {
        "AuthenticationToken": str,
    },
)
GetDocumentPathRequestRequestTypeDef = TypedDict(
    "GetDocumentPathRequestRequestTypeDef",
    {
        "DocumentId": str,
        "AuthenticationToken": NotRequired[str],
        "Limit": NotRequired[int],
        "Fields": NotRequired[str],
        "Marker": NotRequired[str],
    },
)
GetDocumentRequestRequestTypeDef = TypedDict(
    "GetDocumentRequestRequestTypeDef",
    {
        "DocumentId": str,
        "AuthenticationToken": NotRequired[str],
        "IncludeCustomMetadata": NotRequired[bool],
    },
)
GetDocumentVersionRequestRequestTypeDef = TypedDict(
    "GetDocumentVersionRequestRequestTypeDef",
    {
        "DocumentId": str,
        "VersionId": str,
        "AuthenticationToken": NotRequired[str],
        "Fields": NotRequired[str],
        "IncludeCustomMetadata": NotRequired[bool],
    },
)
GetFolderPathRequestRequestTypeDef = TypedDict(
    "GetFolderPathRequestRequestTypeDef",
    {
        "FolderId": str,
        "AuthenticationToken": NotRequired[str],
        "Limit": NotRequired[int],
        "Fields": NotRequired[str],
        "Marker": NotRequired[str],
    },
)
GetFolderRequestRequestTypeDef = TypedDict(
    "GetFolderRequestRequestTypeDef",
    {
        "FolderId": str,
        "AuthenticationToken": NotRequired[str],
        "IncludeCustomMetadata": NotRequired[bool],
    },
)
GetResourcesRequestRequestTypeDef = TypedDict(
    "GetResourcesRequestRequestTypeDef",
    {
        "AuthenticationToken": NotRequired[str],
        "UserId": NotRequired[str],
        "CollectionType": NotRequired[Literal["SHARED_WITH_ME"]],
        "Limit": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
UploadMetadataTypeDef = TypedDict(
    "UploadMetadataTypeDef",
    {
        "UploadUrl": NotRequired[str],
        "SignedHeaders": NotRequired[Dict[str, str]],
    },
)
PermissionInfoTypeDef = TypedDict(
    "PermissionInfoTypeDef",
    {
        "Role": NotRequired[RoleTypeType],
        "Type": NotRequired[RolePermissionTypeType],
    },
)
RemoveAllResourcePermissionsRequestRequestTypeDef = TypedDict(
    "RemoveAllResourcePermissionsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "AuthenticationToken": NotRequired[str],
    },
)
RemoveResourcePermissionRequestRequestTypeDef = TypedDict(
    "RemoveResourcePermissionRequestRequestTypeDef",
    {
        "ResourceId": str,
        "PrincipalId": str,
        "AuthenticationToken": NotRequired[str],
        "PrincipalType": NotRequired[PrincipalTypeType],
    },
)
ResourcePathComponentTypeDef = TypedDict(
    "ResourcePathComponentTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
    },
)
RestoreDocumentVersionsRequestRequestTypeDef = TypedDict(
    "RestoreDocumentVersionsRequestRequestTypeDef",
    {
        "DocumentId": str,
        "AuthenticationToken": NotRequired[str],
    },
)
SearchSortResultTypeDef = TypedDict(
    "SearchSortResultTypeDef",
    {
        "Field": NotRequired[OrderByFieldTypeType],
        "Order": NotRequired[SortOrderType],
    },
)
UpdateDocumentRequestRequestTypeDef = TypedDict(
    "UpdateDocumentRequestRequestTypeDef",
    {
        "DocumentId": str,
        "AuthenticationToken": NotRequired[str],
        "Name": NotRequired[str],
        "ParentFolderId": NotRequired[str],
        "ResourceState": NotRequired[ResourceStateTypeType],
    },
)
UpdateDocumentVersionRequestRequestTypeDef = TypedDict(
    "UpdateDocumentVersionRequestRequestTypeDef",
    {
        "DocumentId": str,
        "VersionId": str,
        "AuthenticationToken": NotRequired[str],
        "VersionStatus": NotRequired[Literal["ACTIVE"]],
    },
)
UpdateFolderRequestRequestTypeDef = TypedDict(
    "UpdateFolderRequestRequestTypeDef",
    {
        "FolderId": str,
        "AuthenticationToken": NotRequired[str],
        "Name": NotRequired[str],
        "ParentFolderId": NotRequired[str],
        "ResourceState": NotRequired[ResourceStateTypeType],
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResourceMetadataTypeDef = TypedDict(
    "ResourceMetadataTypeDef",
    {
        "Type": NotRequired[ResourceTypeType],
        "Name": NotRequired[str],
        "OriginalName": NotRequired[str],
        "Id": NotRequired[str],
        "VersionId": NotRequired[str],
        "Owner": NotRequired[UserMetadataTypeDef],
        "ParentId": NotRequired[str],
    },
)
AddResourcePermissionsRequestRequestTypeDef = TypedDict(
    "AddResourcePermissionsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "Principals": Sequence[SharePrincipalTypeDef],
        "AuthenticationToken": NotRequired[str],
        "NotificationOptions": NotRequired[NotificationOptionsTypeDef],
    },
)
AddResourcePermissionsResponseTypeDef = TypedDict(
    "AddResourcePermissionsResponseTypeDef",
    {
        "ShareResults": List[ShareResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFolderResponseTypeDef = TypedDict(
    "CreateFolderResponseTypeDef",
    {
        "Metadata": FolderMetadataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRootFoldersResponseTypeDef = TypedDict(
    "DescribeRootFoldersResponseTypeDef",
    {
        "Folders": List[FolderMetadataTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFolderResponseTypeDef = TypedDict(
    "GetFolderResponseTypeDef",
    {
        "Metadata": FolderMetadataTypeDef,
        "CustomMetadata": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateNotificationSubscriptionResponseTypeDef = TypedDict(
    "CreateNotificationSubscriptionResponseTypeDef",
    {
        "Subscription": SubscriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeNotificationSubscriptionsResponseTypeDef = TypedDict(
    "DescribeNotificationSubscriptionsResponseTypeDef",
    {
        "Subscriptions": List[SubscriptionTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateUserRequestRequestTypeDef = TypedDict(
    "CreateUserRequestRequestTypeDef",
    {
        "Username": str,
        "GivenName": str,
        "Surname": str,
        "Password": str,
        "OrganizationId": NotRequired[str],
        "EmailAddress": NotRequired[str],
        "TimeZoneId": NotRequired[str],
        "StorageRule": NotRequired[StorageRuleTypeTypeDef],
        "AuthenticationToken": NotRequired[str],
    },
)
UpdateUserRequestRequestTypeDef = TypedDict(
    "UpdateUserRequestRequestTypeDef",
    {
        "UserId": str,
        "AuthenticationToken": NotRequired[str],
        "GivenName": NotRequired[str],
        "Surname": NotRequired[str],
        "Type": NotRequired[UserTypeType],
        "StorageRule": NotRequired[StorageRuleTypeTypeDef],
        "TimeZoneId": NotRequired[str],
        "Locale": NotRequired[LocaleTypeType],
        "GrantPoweruserPrivileges": NotRequired[BooleanEnumTypeType],
    },
)
UserStorageMetadataTypeDef = TypedDict(
    "UserStorageMetadataTypeDef",
    {
        "StorageUtilizedInBytes": NotRequired[int],
        "StorageRule": NotRequired[StorageRuleTypeTypeDef],
    },
)
DateRangeTypeTypeDef = TypedDict(
    "DateRangeTypeTypeDef",
    {
        "StartValue": NotRequired[TimestampTypeDef],
        "EndValue": NotRequired[TimestampTypeDef],
    },
)
DescribeActivitiesRequestRequestTypeDef = TypedDict(
    "DescribeActivitiesRequestRequestTypeDef",
    {
        "AuthenticationToken": NotRequired[str],
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "OrganizationId": NotRequired[str],
        "ActivityTypes": NotRequired[str],
        "ResourceId": NotRequired[str],
        "UserId": NotRequired[str],
        "IncludeIndirectActivities": NotRequired[bool],
        "Limit": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
InitiateDocumentVersionUploadRequestRequestTypeDef = TypedDict(
    "InitiateDocumentVersionUploadRequestRequestTypeDef",
    {
        "AuthenticationToken": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "ContentCreatedTimestamp": NotRequired[TimestampTypeDef],
        "ContentModifiedTimestamp": NotRequired[TimestampTypeDef],
        "ContentType": NotRequired[str],
        "DocumentSizeInBytes": NotRequired[int],
        "ParentFolderId": NotRequired[str],
    },
)
DescribeActivitiesRequestDescribeActivitiesPaginateTypeDef = TypedDict(
    "DescribeActivitiesRequestDescribeActivitiesPaginateTypeDef",
    {
        "AuthenticationToken": NotRequired[str],
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "OrganizationId": NotRequired[str],
        "ActivityTypes": NotRequired[str],
        "ResourceId": NotRequired[str],
        "UserId": NotRequired[str],
        "IncludeIndirectActivities": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeCommentsRequestDescribeCommentsPaginateTypeDef = TypedDict(
    "DescribeCommentsRequestDescribeCommentsPaginateTypeDef",
    {
        "DocumentId": str,
        "VersionId": str,
        "AuthenticationToken": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDocumentVersionsRequestDescribeDocumentVersionsPaginateTypeDef = TypedDict(
    "DescribeDocumentVersionsRequestDescribeDocumentVersionsPaginateTypeDef",
    {
        "DocumentId": str,
        "AuthenticationToken": NotRequired[str],
        "Include": NotRequired[str],
        "Fields": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeFolderContentsRequestDescribeFolderContentsPaginateTypeDef = TypedDict(
    "DescribeFolderContentsRequestDescribeFolderContentsPaginateTypeDef",
    {
        "FolderId": str,
        "AuthenticationToken": NotRequired[str],
        "Sort": NotRequired[ResourceSortTypeType],
        "Order": NotRequired[OrderTypeType],
        "Type": NotRequired[FolderContentTypeType],
        "Include": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeGroupsRequestDescribeGroupsPaginateTypeDef = TypedDict(
    "DescribeGroupsRequestDescribeGroupsPaginateTypeDef",
    {
        "SearchQuery": str,
        "AuthenticationToken": NotRequired[str],
        "OrganizationId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeNotificationSubscriptionsRequestDescribeNotificationSubscriptionsPaginateTypeDef = (
    TypedDict(
        "DescribeNotificationSubscriptionsRequestDescribeNotificationSubscriptionsPaginateTypeDef",
        {
            "OrganizationId": str,
            "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
        },
    )
)
DescribeResourcePermissionsRequestDescribeResourcePermissionsPaginateTypeDef = TypedDict(
    "DescribeResourcePermissionsRequestDescribeResourcePermissionsPaginateTypeDef",
    {
        "ResourceId": str,
        "AuthenticationToken": NotRequired[str],
        "PrincipalId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeRootFoldersRequestDescribeRootFoldersPaginateTypeDef = TypedDict(
    "DescribeRootFoldersRequestDescribeRootFoldersPaginateTypeDef",
    {
        "AuthenticationToken": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeUsersRequestDescribeUsersPaginateTypeDef = TypedDict(
    "DescribeUsersRequestDescribeUsersPaginateTypeDef",
    {
        "AuthenticationToken": NotRequired[str],
        "OrganizationId": NotRequired[str],
        "UserIds": NotRequired[str],
        "Query": NotRequired[str],
        "Include": NotRequired[UserFilterTypeType],
        "Order": NotRequired[OrderTypeType],
        "Sort": NotRequired[UserSortTypeType],
        "Fields": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeDocumentVersionsResponseTypeDef = TypedDict(
    "DescribeDocumentVersionsResponseTypeDef",
    {
        "DocumentVersions": List[DocumentVersionMetadataTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DocumentMetadataTypeDef = TypedDict(
    "DocumentMetadataTypeDef",
    {
        "Id": NotRequired[str],
        "CreatorId": NotRequired[str],
        "ParentFolderId": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "ModifiedTimestamp": NotRequired[datetime],
        "LatestVersionMetadata": NotRequired[DocumentVersionMetadataTypeDef],
        "ResourceState": NotRequired[ResourceStateTypeType],
        "Labels": NotRequired[List[str]],
    },
)
GetDocumentVersionResponseTypeDef = TypedDict(
    "GetDocumentVersionResponseTypeDef",
    {
        "Metadata": DocumentVersionMetadataTypeDef,
        "CustomMetadata": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeGroupsResponseTypeDef = TypedDict(
    "DescribeGroupsResponseTypeDef",
    {
        "Groups": List[GroupMetadataTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ParticipantsTypeDef = TypedDict(
    "ParticipantsTypeDef",
    {
        "Users": NotRequired[List[UserMetadataTypeDef]],
        "Groups": NotRequired[List[GroupMetadataTypeDef]],
    },
)
PrincipalTypeDef = TypedDict(
    "PrincipalTypeDef",
    {
        "Id": NotRequired[str],
        "Type": NotRequired[PrincipalTypeType],
        "Roles": NotRequired[List[PermissionInfoTypeDef]],
    },
)
ResourcePathTypeDef = TypedDict(
    "ResourcePathTypeDef",
    {
        "Components": NotRequired[List[ResourcePathComponentTypeDef]],
    },
)
UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "Id": NotRequired[str],
        "Username": NotRequired[str],
        "EmailAddress": NotRequired[str],
        "GivenName": NotRequired[str],
        "Surname": NotRequired[str],
        "OrganizationId": NotRequired[str],
        "RootFolderId": NotRequired[str],
        "RecycleBinFolderId": NotRequired[str],
        "Status": NotRequired[UserStatusTypeType],
        "Type": NotRequired[UserTypeType],
        "CreatedTimestamp": NotRequired[datetime],
        "ModifiedTimestamp": NotRequired[datetime],
        "TimeZoneId": NotRequired[str],
        "Locale": NotRequired[LocaleTypeType],
        "Storage": NotRequired[UserStorageMetadataTypeDef],
    },
)
FiltersTypeDef = TypedDict(
    "FiltersTypeDef",
    {
        "TextLocales": NotRequired[Sequence[LanguageCodeTypeType]],
        "ContentCategories": NotRequired[Sequence[ContentCategoryTypeType]],
        "ResourceTypes": NotRequired[Sequence[SearchResourceTypeType]],
        "Labels": NotRequired[Sequence[str]],
        "Principals": NotRequired[Sequence[SearchPrincipalTypeTypeDef]],
        "AncestorIds": NotRequired[Sequence[str]],
        "SearchCollectionTypes": NotRequired[Sequence[SearchCollectionTypeType]],
        "SizeRange": NotRequired[LongRangeTypeTypeDef],
        "CreatedRange": NotRequired[DateRangeTypeTypeDef],
        "ModifiedRange": NotRequired[DateRangeTypeTypeDef],
    },
)
DescribeFolderContentsResponseTypeDef = TypedDict(
    "DescribeFolderContentsResponseTypeDef",
    {
        "Folders": List[FolderMetadataTypeDef],
        "Documents": List[DocumentMetadataTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDocumentResponseTypeDef = TypedDict(
    "GetDocumentResponseTypeDef",
    {
        "Metadata": DocumentMetadataTypeDef,
        "CustomMetadata": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResourcesResponseTypeDef = TypedDict(
    "GetResourcesResponseTypeDef",
    {
        "Folders": List[FolderMetadataTypeDef],
        "Documents": List[DocumentMetadataTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InitiateDocumentVersionUploadResponseTypeDef = TypedDict(
    "InitiateDocumentVersionUploadResponseTypeDef",
    {
        "Metadata": DocumentMetadataTypeDef,
        "UploadMetadata": UploadMetadataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeResourcePermissionsResponseTypeDef = TypedDict(
    "DescribeResourcePermissionsResponseTypeDef",
    {
        "Principals": List[PrincipalTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDocumentPathResponseTypeDef = TypedDict(
    "GetDocumentPathResponseTypeDef",
    {
        "Path": ResourcePathTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFolderPathResponseTypeDef = TypedDict(
    "GetFolderPathResponseTypeDef",
    {
        "Path": ResourcePathTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ActivateUserResponseTypeDef = TypedDict(
    "ActivateUserResponseTypeDef",
    {
        "User": UserTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CommentMetadataTypeDef = TypedDict(
    "CommentMetadataTypeDef",
    {
        "CommentId": NotRequired[str],
        "Contributor": NotRequired[UserTypeDef],
        "CreatedTimestamp": NotRequired[datetime],
        "CommentStatus": NotRequired[CommentStatusTypeType],
        "RecipientId": NotRequired[str],
        "ContributorId": NotRequired[str],
    },
)
CommentTypeDef = TypedDict(
    "CommentTypeDef",
    {
        "CommentId": str,
        "ParentId": NotRequired[str],
        "ThreadId": NotRequired[str],
        "Text": NotRequired[str],
        "Contributor": NotRequired[UserTypeDef],
        "CreatedTimestamp": NotRequired[datetime],
        "Status": NotRequired[CommentStatusTypeType],
        "Visibility": NotRequired[CommentVisibilityTypeType],
        "RecipientId": NotRequired[str],
    },
)
CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef",
    {
        "User": UserTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeUsersResponseTypeDef = TypedDict(
    "DescribeUsersResponseTypeDef",
    {
        "Users": List[UserTypeDef],
        "TotalNumberOfUsers": int,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCurrentUserResponseTypeDef = TypedDict(
    "GetCurrentUserResponseTypeDef",
    {
        "User": UserTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateUserResponseTypeDef = TypedDict(
    "UpdateUserResponseTypeDef",
    {
        "User": UserTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchResourcesRequestRequestTypeDef = TypedDict(
    "SearchResourcesRequestRequestTypeDef",
    {
        "AuthenticationToken": NotRequired[str],
        "QueryText": NotRequired[str],
        "QueryScopes": NotRequired[Sequence[SearchQueryScopeTypeType]],
        "OrganizationId": NotRequired[str],
        "AdditionalResponseFields": NotRequired[Sequence[Literal["WEBURL"]]],
        "Filters": NotRequired[FiltersTypeDef],
        "OrderBy": NotRequired[Sequence[SearchSortResultTypeDef]],
        "Limit": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
SearchResourcesRequestSearchResourcesPaginateTypeDef = TypedDict(
    "SearchResourcesRequestSearchResourcesPaginateTypeDef",
    {
        "AuthenticationToken": NotRequired[str],
        "QueryText": NotRequired[str],
        "QueryScopes": NotRequired[Sequence[SearchQueryScopeTypeType]],
        "OrganizationId": NotRequired[str],
        "AdditionalResponseFields": NotRequired[Sequence[Literal["WEBURL"]]],
        "Filters": NotRequired[FiltersTypeDef],
        "OrderBy": NotRequired[Sequence[SearchSortResultTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ActivityTypeDef = TypedDict(
    "ActivityTypeDef",
    {
        "Type": NotRequired[ActivityTypeType],
        "TimeStamp": NotRequired[datetime],
        "IsIndirectActivity": NotRequired[bool],
        "OrganizationId": NotRequired[str],
        "Initiator": NotRequired[UserMetadataTypeDef],
        "Participants": NotRequired[ParticipantsTypeDef],
        "ResourceMetadata": NotRequired[ResourceMetadataTypeDef],
        "OriginalParent": NotRequired[ResourceMetadataTypeDef],
        "CommentMetadata": NotRequired[CommentMetadataTypeDef],
    },
)
ResponseItemTypeDef = TypedDict(
    "ResponseItemTypeDef",
    {
        "ResourceType": NotRequired[ResponseItemTypeType],
        "WebUrl": NotRequired[str],
        "DocumentMetadata": NotRequired[DocumentMetadataTypeDef],
        "FolderMetadata": NotRequired[FolderMetadataTypeDef],
        "CommentMetadata": NotRequired[CommentMetadataTypeDef],
        "DocumentVersionMetadata": NotRequired[DocumentVersionMetadataTypeDef],
    },
)
CreateCommentResponseTypeDef = TypedDict(
    "CreateCommentResponseTypeDef",
    {
        "Comment": CommentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeCommentsResponseTypeDef = TypedDict(
    "DescribeCommentsResponseTypeDef",
    {
        "Comments": List[CommentTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeActivitiesResponseTypeDef = TypedDict(
    "DescribeActivitiesResponseTypeDef",
    {
        "UserActivities": List[ActivityTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchResourcesResponseTypeDef = TypedDict(
    "SearchResourcesResponseTypeDef",
    {
        "Items": List[ResponseItemTypeDef],
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
