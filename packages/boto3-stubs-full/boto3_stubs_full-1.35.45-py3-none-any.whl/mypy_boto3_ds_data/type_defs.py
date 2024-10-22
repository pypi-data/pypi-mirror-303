"""
Type annotations for ds-data service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/type_defs/)

Usage::

    ```python
    from mypy_boto3_ds_data.type_defs import AddGroupMemberRequestRequestTypeDef

    data: AddGroupMemberRequestRequestTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Mapping, Sequence, Union

from .literals import GroupScopeType, GroupTypeType, MemberTypeType, UpdateTypeType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "AddGroupMemberRequestRequestTypeDef",
    "AttributeValueOutputTypeDef",
    "AttributeValueTypeDef",
    "ResponseMetadataTypeDef",
    "DeleteGroupRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DescribeGroupRequestRequestTypeDef",
    "DescribeUserRequestRequestTypeDef",
    "DisableUserRequestRequestTypeDef",
    "GroupSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "ListGroupMembersRequestRequestTypeDef",
    "MemberTypeDef",
    "ListGroupsForMemberRequestRequestTypeDef",
    "ListGroupsRequestRequestTypeDef",
    "ListUsersRequestRequestTypeDef",
    "UserSummaryTypeDef",
    "RemoveGroupMemberRequestRequestTypeDef",
    "SearchGroupsRequestRequestTypeDef",
    "SearchUsersRequestRequestTypeDef",
    "GroupTypeDef",
    "UserTypeDef",
    "AttributeValueUnionTypeDef",
    "CreateUserRequestRequestTypeDef",
    "UpdateGroupRequestRequestTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "CreateGroupResultTypeDef",
    "CreateUserResultTypeDef",
    "DescribeGroupResultTypeDef",
    "DescribeUserResultTypeDef",
    "ListGroupsForMemberResultTypeDef",
    "ListGroupsResultTypeDef",
    "ListGroupMembersRequestListGroupMembersPaginateTypeDef",
    "ListGroupsForMemberRequestListGroupsForMemberPaginateTypeDef",
    "ListGroupsRequestListGroupsPaginateTypeDef",
    "ListUsersRequestListUsersPaginateTypeDef",
    "SearchGroupsRequestSearchGroupsPaginateTypeDef",
    "SearchUsersRequestSearchUsersPaginateTypeDef",
    "ListGroupMembersResultTypeDef",
    "ListUsersResultTypeDef",
    "SearchGroupsResultTypeDef",
    "SearchUsersResultTypeDef",
    "CreateGroupRequestRequestTypeDef",
)

AddGroupMemberRequestRequestTypeDef = TypedDict(
    "AddGroupMemberRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "GroupName": str,
        "MemberName": str,
        "ClientToken": NotRequired[str],
        "MemberRealm": NotRequired[str],
    },
)
AttributeValueOutputTypeDef = TypedDict(
    "AttributeValueOutputTypeDef",
    {
        "BOOL": NotRequired[bool],
        "N": NotRequired[int],
        "S": NotRequired[str],
        "SS": NotRequired[List[str]],
    },
)
AttributeValueTypeDef = TypedDict(
    "AttributeValueTypeDef",
    {
        "BOOL": NotRequired[bool],
        "N": NotRequired[int],
        "S": NotRequired[str],
        "SS": NotRequired[Sequence[str]],
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
DeleteGroupRequestRequestTypeDef = TypedDict(
    "DeleteGroupRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "SAMAccountName": str,
        "ClientToken": NotRequired[str],
    },
)
DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "SAMAccountName": str,
        "ClientToken": NotRequired[str],
    },
)
DescribeGroupRequestRequestTypeDef = TypedDict(
    "DescribeGroupRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "SAMAccountName": str,
        "OtherAttributes": NotRequired[Sequence[str]],
        "Realm": NotRequired[str],
    },
)
DescribeUserRequestRequestTypeDef = TypedDict(
    "DescribeUserRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "SAMAccountName": str,
        "OtherAttributes": NotRequired[Sequence[str]],
        "Realm": NotRequired[str],
    },
)
DisableUserRequestRequestTypeDef = TypedDict(
    "DisableUserRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "SAMAccountName": str,
        "ClientToken": NotRequired[str],
    },
)
GroupSummaryTypeDef = TypedDict(
    "GroupSummaryTypeDef",
    {
        "GroupScope": GroupScopeType,
        "GroupType": GroupTypeType,
        "SAMAccountName": str,
        "SID": str,
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
ListGroupMembersRequestRequestTypeDef = TypedDict(
    "ListGroupMembersRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "SAMAccountName": str,
        "MaxResults": NotRequired[int],
        "MemberRealm": NotRequired[str],
        "NextToken": NotRequired[str],
        "Realm": NotRequired[str],
    },
)
MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "MemberType": MemberTypeType,
        "SAMAccountName": str,
        "SID": str,
    },
)
ListGroupsForMemberRequestRequestTypeDef = TypedDict(
    "ListGroupsForMemberRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "SAMAccountName": str,
        "MaxResults": NotRequired[int],
        "MemberRealm": NotRequired[str],
        "NextToken": NotRequired[str],
        "Realm": NotRequired[str],
    },
)
ListGroupsRequestRequestTypeDef = TypedDict(
    "ListGroupsRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Realm": NotRequired[str],
    },
)
ListUsersRequestRequestTypeDef = TypedDict(
    "ListUsersRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Realm": NotRequired[str],
    },
)
UserSummaryTypeDef = TypedDict(
    "UserSummaryTypeDef",
    {
        "Enabled": bool,
        "SAMAccountName": str,
        "SID": str,
        "GivenName": NotRequired[str],
        "Surname": NotRequired[str],
    },
)
RemoveGroupMemberRequestRequestTypeDef = TypedDict(
    "RemoveGroupMemberRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "GroupName": str,
        "MemberName": str,
        "ClientToken": NotRequired[str],
        "MemberRealm": NotRequired[str],
    },
)
SearchGroupsRequestRequestTypeDef = TypedDict(
    "SearchGroupsRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "SearchAttributes": Sequence[str],
        "SearchString": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Realm": NotRequired[str],
    },
)
SearchUsersRequestRequestTypeDef = TypedDict(
    "SearchUsersRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "SearchAttributes": Sequence[str],
        "SearchString": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Realm": NotRequired[str],
    },
)
GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "SAMAccountName": str,
        "DistinguishedName": NotRequired[str],
        "GroupScope": NotRequired[GroupScopeType],
        "GroupType": NotRequired[GroupTypeType],
        "OtherAttributes": NotRequired[Dict[str, AttributeValueOutputTypeDef]],
        "SID": NotRequired[str],
    },
)
UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "SAMAccountName": str,
        "DistinguishedName": NotRequired[str],
        "EmailAddress": NotRequired[str],
        "Enabled": NotRequired[bool],
        "GivenName": NotRequired[str],
        "OtherAttributes": NotRequired[Dict[str, AttributeValueOutputTypeDef]],
        "SID": NotRequired[str],
        "Surname": NotRequired[str],
        "UserPrincipalName": NotRequired[str],
    },
)
AttributeValueUnionTypeDef = Union[AttributeValueTypeDef, AttributeValueOutputTypeDef]
CreateUserRequestRequestTypeDef = TypedDict(
    "CreateUserRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "SAMAccountName": str,
        "ClientToken": NotRequired[str],
        "EmailAddress": NotRequired[str],
        "GivenName": NotRequired[str],
        "OtherAttributes": NotRequired[Mapping[str, AttributeValueTypeDef]],
        "Surname": NotRequired[str],
    },
)
UpdateGroupRequestRequestTypeDef = TypedDict(
    "UpdateGroupRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "SAMAccountName": str,
        "ClientToken": NotRequired[str],
        "GroupScope": NotRequired[GroupScopeType],
        "GroupType": NotRequired[GroupTypeType],
        "OtherAttributes": NotRequired[Mapping[str, AttributeValueTypeDef]],
        "UpdateType": NotRequired[UpdateTypeType],
    },
)
UpdateUserRequestRequestTypeDef = TypedDict(
    "UpdateUserRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "SAMAccountName": str,
        "ClientToken": NotRequired[str],
        "EmailAddress": NotRequired[str],
        "GivenName": NotRequired[str],
        "OtherAttributes": NotRequired[Mapping[str, AttributeValueTypeDef]],
        "Surname": NotRequired[str],
        "UpdateType": NotRequired[UpdateTypeType],
    },
)
CreateGroupResultTypeDef = TypedDict(
    "CreateGroupResultTypeDef",
    {
        "DirectoryId": str,
        "SAMAccountName": str,
        "SID": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateUserResultTypeDef = TypedDict(
    "CreateUserResultTypeDef",
    {
        "DirectoryId": str,
        "SAMAccountName": str,
        "SID": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeGroupResultTypeDef = TypedDict(
    "DescribeGroupResultTypeDef",
    {
        "DirectoryId": str,
        "DistinguishedName": str,
        "GroupScope": GroupScopeType,
        "GroupType": GroupTypeType,
        "OtherAttributes": Dict[str, AttributeValueOutputTypeDef],
        "Realm": str,
        "SAMAccountName": str,
        "SID": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeUserResultTypeDef = TypedDict(
    "DescribeUserResultTypeDef",
    {
        "DirectoryId": str,
        "DistinguishedName": str,
        "EmailAddress": str,
        "Enabled": bool,
        "GivenName": str,
        "OtherAttributes": Dict[str, AttributeValueOutputTypeDef],
        "Realm": str,
        "SAMAccountName": str,
        "SID": str,
        "Surname": str,
        "UserPrincipalName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListGroupsForMemberResultTypeDef = TypedDict(
    "ListGroupsForMemberResultTypeDef",
    {
        "DirectoryId": str,
        "Groups": List[GroupSummaryTypeDef],
        "MemberRealm": str,
        "Realm": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListGroupsResultTypeDef = TypedDict(
    "ListGroupsResultTypeDef",
    {
        "DirectoryId": str,
        "Groups": List[GroupSummaryTypeDef],
        "Realm": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListGroupMembersRequestListGroupMembersPaginateTypeDef = TypedDict(
    "ListGroupMembersRequestListGroupMembersPaginateTypeDef",
    {
        "DirectoryId": str,
        "SAMAccountName": str,
        "MemberRealm": NotRequired[str],
        "Realm": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGroupsForMemberRequestListGroupsForMemberPaginateTypeDef = TypedDict(
    "ListGroupsForMemberRequestListGroupsForMemberPaginateTypeDef",
    {
        "DirectoryId": str,
        "SAMAccountName": str,
        "MemberRealm": NotRequired[str],
        "Realm": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGroupsRequestListGroupsPaginateTypeDef = TypedDict(
    "ListGroupsRequestListGroupsPaginateTypeDef",
    {
        "DirectoryId": str,
        "Realm": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListUsersRequestListUsersPaginateTypeDef = TypedDict(
    "ListUsersRequestListUsersPaginateTypeDef",
    {
        "DirectoryId": str,
        "Realm": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchGroupsRequestSearchGroupsPaginateTypeDef = TypedDict(
    "SearchGroupsRequestSearchGroupsPaginateTypeDef",
    {
        "DirectoryId": str,
        "SearchAttributes": Sequence[str],
        "SearchString": str,
        "Realm": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchUsersRequestSearchUsersPaginateTypeDef = TypedDict(
    "SearchUsersRequestSearchUsersPaginateTypeDef",
    {
        "DirectoryId": str,
        "SearchAttributes": Sequence[str],
        "SearchString": str,
        "Realm": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGroupMembersResultTypeDef = TypedDict(
    "ListGroupMembersResultTypeDef",
    {
        "DirectoryId": str,
        "MemberRealm": str,
        "Members": List[MemberTypeDef],
        "Realm": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListUsersResultTypeDef = TypedDict(
    "ListUsersResultTypeDef",
    {
        "DirectoryId": str,
        "Realm": str,
        "Users": List[UserSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
SearchGroupsResultTypeDef = TypedDict(
    "SearchGroupsResultTypeDef",
    {
        "DirectoryId": str,
        "Groups": List[GroupTypeDef],
        "Realm": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
SearchUsersResultTypeDef = TypedDict(
    "SearchUsersResultTypeDef",
    {
        "DirectoryId": str,
        "Realm": str,
        "Users": List[UserTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateGroupRequestRequestTypeDef = TypedDict(
    "CreateGroupRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "SAMAccountName": str,
        "ClientToken": NotRequired[str],
        "GroupScope": NotRequired[GroupScopeType],
        "GroupType": NotRequired[GroupTypeType],
        "OtherAttributes": NotRequired[Mapping[str, AttributeValueUnionTypeDef]],
    },
)
