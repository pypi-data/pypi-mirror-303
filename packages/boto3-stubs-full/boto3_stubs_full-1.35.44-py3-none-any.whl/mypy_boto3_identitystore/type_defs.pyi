"""
Type annotations for identitystore service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_identitystore/type_defs/)

Usage::

    ```python
    from mypy_boto3_identitystore.type_defs import AddressTypeDef

    data: AddressTypeDef = ...
    ```
"""

import sys
from typing import Any, Dict, List, Mapping, Sequence

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AddressTypeDef",
    "ExternalIdTypeDef",
    "UniqueAttributeTypeDef",
    "AttributeOperationTypeDef",
    "MemberIdTypeDef",
    "ResponseMetadataTypeDef",
    "CreateGroupRequestRequestTypeDef",
    "EmailTypeDef",
    "NameTypeDef",
    "PhoneNumberTypeDef",
    "DeleteGroupMembershipRequestRequestTypeDef",
    "DeleteGroupRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DescribeGroupMembershipRequestRequestTypeDef",
    "DescribeGroupRequestRequestTypeDef",
    "DescribeUserRequestRequestTypeDef",
    "FilterTypeDef",
    "PaginatorConfigTypeDef",
    "ListGroupMembershipsRequestRequestTypeDef",
    "GroupTypeDef",
    "AlternateIdentifierTypeDef",
    "UpdateGroupRequestRequestTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "CreateGroupMembershipRequestRequestTypeDef",
    "GetGroupMembershipIdRequestRequestTypeDef",
    "GroupMembershipExistenceResultTypeDef",
    "GroupMembershipTypeDef",
    "IsMemberInGroupsRequestRequestTypeDef",
    "ListGroupMembershipsForMemberRequestRequestTypeDef",
    "CreateGroupMembershipResponseTypeDef",
    "CreateGroupResponseTypeDef",
    "CreateUserResponseTypeDef",
    "DescribeGroupMembershipResponseTypeDef",
    "DescribeGroupResponseTypeDef",
    "GetGroupIdResponseTypeDef",
    "GetGroupMembershipIdResponseTypeDef",
    "GetUserIdResponseTypeDef",
    "CreateUserRequestRequestTypeDef",
    "DescribeUserResponseTypeDef",
    "UserTypeDef",
    "ListGroupsRequestRequestTypeDef",
    "ListUsersRequestRequestTypeDef",
    "ListGroupMembershipsForMemberRequestListGroupMembershipsForMemberPaginateTypeDef",
    "ListGroupMembershipsRequestListGroupMembershipsPaginateTypeDef",
    "ListGroupsRequestListGroupsPaginateTypeDef",
    "ListUsersRequestListUsersPaginateTypeDef",
    "ListGroupsResponseTypeDef",
    "GetGroupIdRequestRequestTypeDef",
    "GetUserIdRequestRequestTypeDef",
    "IsMemberInGroupsResponseTypeDef",
    "ListGroupMembershipsForMemberResponseTypeDef",
    "ListGroupMembershipsResponseTypeDef",
    "ListUsersResponseTypeDef",
)

AddressTypeDef = TypedDict(
    "AddressTypeDef",
    {
        "StreetAddress": NotRequired[str],
        "Locality": NotRequired[str],
        "Region": NotRequired[str],
        "PostalCode": NotRequired[str],
        "Country": NotRequired[str],
        "Formatted": NotRequired[str],
        "Type": NotRequired[str],
        "Primary": NotRequired[bool],
    },
)
ExternalIdTypeDef = TypedDict(
    "ExternalIdTypeDef",
    {
        "Issuer": str,
        "Id": str,
    },
)
UniqueAttributeTypeDef = TypedDict(
    "UniqueAttributeTypeDef",
    {
        "AttributePath": str,
        "AttributeValue": Mapping[str, Any],
    },
)
AttributeOperationTypeDef = TypedDict(
    "AttributeOperationTypeDef",
    {
        "AttributePath": str,
        "AttributeValue": NotRequired[Mapping[str, Any]],
    },
)
MemberIdTypeDef = TypedDict(
    "MemberIdTypeDef",
    {
        "UserId": NotRequired[str],
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
CreateGroupRequestRequestTypeDef = TypedDict(
    "CreateGroupRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "DisplayName": NotRequired[str],
        "Description": NotRequired[str],
    },
)
EmailTypeDef = TypedDict(
    "EmailTypeDef",
    {
        "Value": NotRequired[str],
        "Type": NotRequired[str],
        "Primary": NotRequired[bool],
    },
)
NameTypeDef = TypedDict(
    "NameTypeDef",
    {
        "Formatted": NotRequired[str],
        "FamilyName": NotRequired[str],
        "GivenName": NotRequired[str],
        "MiddleName": NotRequired[str],
        "HonorificPrefix": NotRequired[str],
        "HonorificSuffix": NotRequired[str],
    },
)
PhoneNumberTypeDef = TypedDict(
    "PhoneNumberTypeDef",
    {
        "Value": NotRequired[str],
        "Type": NotRequired[str],
        "Primary": NotRequired[bool],
    },
)
DeleteGroupMembershipRequestRequestTypeDef = TypedDict(
    "DeleteGroupMembershipRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "MembershipId": str,
    },
)
DeleteGroupRequestRequestTypeDef = TypedDict(
    "DeleteGroupRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "GroupId": str,
    },
)
DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "UserId": str,
    },
)
DescribeGroupMembershipRequestRequestTypeDef = TypedDict(
    "DescribeGroupMembershipRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "MembershipId": str,
    },
)
DescribeGroupRequestRequestTypeDef = TypedDict(
    "DescribeGroupRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "GroupId": str,
    },
)
DescribeUserRequestRequestTypeDef = TypedDict(
    "DescribeUserRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "UserId": str,
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "AttributePath": str,
        "AttributeValue": str,
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
ListGroupMembershipsRequestRequestTypeDef = TypedDict(
    "ListGroupMembershipsRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "GroupId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "GroupId": str,
        "IdentityStoreId": str,
        "DisplayName": NotRequired[str],
        "ExternalIds": NotRequired[List[ExternalIdTypeDef]],
        "Description": NotRequired[str],
    },
)
AlternateIdentifierTypeDef = TypedDict(
    "AlternateIdentifierTypeDef",
    {
        "ExternalId": NotRequired[ExternalIdTypeDef],
        "UniqueAttribute": NotRequired[UniqueAttributeTypeDef],
    },
)
UpdateGroupRequestRequestTypeDef = TypedDict(
    "UpdateGroupRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "GroupId": str,
        "Operations": Sequence[AttributeOperationTypeDef],
    },
)
UpdateUserRequestRequestTypeDef = TypedDict(
    "UpdateUserRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "UserId": str,
        "Operations": Sequence[AttributeOperationTypeDef],
    },
)
CreateGroupMembershipRequestRequestTypeDef = TypedDict(
    "CreateGroupMembershipRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "GroupId": str,
        "MemberId": MemberIdTypeDef,
    },
)
GetGroupMembershipIdRequestRequestTypeDef = TypedDict(
    "GetGroupMembershipIdRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "GroupId": str,
        "MemberId": MemberIdTypeDef,
    },
)
GroupMembershipExistenceResultTypeDef = TypedDict(
    "GroupMembershipExistenceResultTypeDef",
    {
        "GroupId": NotRequired[str],
        "MemberId": NotRequired[MemberIdTypeDef],
        "MembershipExists": NotRequired[bool],
    },
)
GroupMembershipTypeDef = TypedDict(
    "GroupMembershipTypeDef",
    {
        "IdentityStoreId": str,
        "MembershipId": NotRequired[str],
        "GroupId": NotRequired[str],
        "MemberId": NotRequired[MemberIdTypeDef],
    },
)
IsMemberInGroupsRequestRequestTypeDef = TypedDict(
    "IsMemberInGroupsRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "MemberId": MemberIdTypeDef,
        "GroupIds": Sequence[str],
    },
)
ListGroupMembershipsForMemberRequestRequestTypeDef = TypedDict(
    "ListGroupMembershipsForMemberRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "MemberId": MemberIdTypeDef,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
CreateGroupMembershipResponseTypeDef = TypedDict(
    "CreateGroupMembershipResponseTypeDef",
    {
        "MembershipId": str,
        "IdentityStoreId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGroupResponseTypeDef = TypedDict(
    "CreateGroupResponseTypeDef",
    {
        "GroupId": str,
        "IdentityStoreId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef",
    {
        "UserId": str,
        "IdentityStoreId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeGroupMembershipResponseTypeDef = TypedDict(
    "DescribeGroupMembershipResponseTypeDef",
    {
        "IdentityStoreId": str,
        "MembershipId": str,
        "GroupId": str,
        "MemberId": MemberIdTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeGroupResponseTypeDef = TypedDict(
    "DescribeGroupResponseTypeDef",
    {
        "GroupId": str,
        "DisplayName": str,
        "ExternalIds": List[ExternalIdTypeDef],
        "Description": str,
        "IdentityStoreId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetGroupIdResponseTypeDef = TypedDict(
    "GetGroupIdResponseTypeDef",
    {
        "GroupId": str,
        "IdentityStoreId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetGroupMembershipIdResponseTypeDef = TypedDict(
    "GetGroupMembershipIdResponseTypeDef",
    {
        "MembershipId": str,
        "IdentityStoreId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetUserIdResponseTypeDef = TypedDict(
    "GetUserIdResponseTypeDef",
    {
        "UserId": str,
        "IdentityStoreId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateUserRequestRequestTypeDef = TypedDict(
    "CreateUserRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "UserName": NotRequired[str],
        "Name": NotRequired[NameTypeDef],
        "DisplayName": NotRequired[str],
        "NickName": NotRequired[str],
        "ProfileUrl": NotRequired[str],
        "Emails": NotRequired[Sequence[EmailTypeDef]],
        "Addresses": NotRequired[Sequence[AddressTypeDef]],
        "PhoneNumbers": NotRequired[Sequence[PhoneNumberTypeDef]],
        "UserType": NotRequired[str],
        "Title": NotRequired[str],
        "PreferredLanguage": NotRequired[str],
        "Locale": NotRequired[str],
        "Timezone": NotRequired[str],
    },
)
DescribeUserResponseTypeDef = TypedDict(
    "DescribeUserResponseTypeDef",
    {
        "UserName": str,
        "UserId": str,
        "ExternalIds": List[ExternalIdTypeDef],
        "Name": NameTypeDef,
        "DisplayName": str,
        "NickName": str,
        "ProfileUrl": str,
        "Emails": List[EmailTypeDef],
        "Addresses": List[AddressTypeDef],
        "PhoneNumbers": List[PhoneNumberTypeDef],
        "UserType": str,
        "Title": str,
        "PreferredLanguage": str,
        "Locale": str,
        "Timezone": str,
        "IdentityStoreId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "UserId": str,
        "IdentityStoreId": str,
        "UserName": NotRequired[str],
        "ExternalIds": NotRequired[List[ExternalIdTypeDef]],
        "Name": NotRequired[NameTypeDef],
        "DisplayName": NotRequired[str],
        "NickName": NotRequired[str],
        "ProfileUrl": NotRequired[str],
        "Emails": NotRequired[List[EmailTypeDef]],
        "Addresses": NotRequired[List[AddressTypeDef]],
        "PhoneNumbers": NotRequired[List[PhoneNumberTypeDef]],
        "UserType": NotRequired[str],
        "Title": NotRequired[str],
        "PreferredLanguage": NotRequired[str],
        "Locale": NotRequired[str],
        "Timezone": NotRequired[str],
    },
)
ListGroupsRequestRequestTypeDef = TypedDict(
    "ListGroupsRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
ListUsersRequestRequestTypeDef = TypedDict(
    "ListUsersRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence[FilterTypeDef]],
    },
)
ListGroupMembershipsForMemberRequestListGroupMembershipsForMemberPaginateTypeDef = TypedDict(
    "ListGroupMembershipsForMemberRequestListGroupMembershipsForMemberPaginateTypeDef",
    {
        "IdentityStoreId": str,
        "MemberId": MemberIdTypeDef,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGroupMembershipsRequestListGroupMembershipsPaginateTypeDef = TypedDict(
    "ListGroupMembershipsRequestListGroupMembershipsPaginateTypeDef",
    {
        "IdentityStoreId": str,
        "GroupId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGroupsRequestListGroupsPaginateTypeDef = TypedDict(
    "ListGroupsRequestListGroupsPaginateTypeDef",
    {
        "IdentityStoreId": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListUsersRequestListUsersPaginateTypeDef = TypedDict(
    "ListUsersRequestListUsersPaginateTypeDef",
    {
        "IdentityStoreId": str,
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGroupsResponseTypeDef = TypedDict(
    "ListGroupsResponseTypeDef",
    {
        "Groups": List[GroupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetGroupIdRequestRequestTypeDef = TypedDict(
    "GetGroupIdRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "AlternateIdentifier": AlternateIdentifierTypeDef,
    },
)
GetUserIdRequestRequestTypeDef = TypedDict(
    "GetUserIdRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "AlternateIdentifier": AlternateIdentifierTypeDef,
    },
)
IsMemberInGroupsResponseTypeDef = TypedDict(
    "IsMemberInGroupsResponseTypeDef",
    {
        "Results": List[GroupMembershipExistenceResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListGroupMembershipsForMemberResponseTypeDef = TypedDict(
    "ListGroupMembershipsForMemberResponseTypeDef",
    {
        "GroupMemberships": List[GroupMembershipTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListGroupMembershipsResponseTypeDef = TypedDict(
    "ListGroupMembershipsResponseTypeDef",
    {
        "GroupMemberships": List[GroupMembershipTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "Users": List[UserTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
