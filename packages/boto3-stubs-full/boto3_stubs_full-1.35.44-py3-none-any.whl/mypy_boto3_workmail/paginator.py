"""
Type annotations for workmail service client paginators.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/)

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_workmail.client import WorkMailClient
    from mypy_boto3_workmail.paginator import (
        ListAliasesPaginator,
        ListAvailabilityConfigurationsPaginator,
        ListGroupMembersPaginator,
        ListGroupsPaginator,
        ListMailboxPermissionsPaginator,
        ListOrganizationsPaginator,
        ListResourceDelegatesPaginator,
        ListResourcesPaginator,
        ListUsersPaginator,
    )

    session = Session()
    client: WorkMailClient = session.client("workmail")

    list_aliases_paginator: ListAliasesPaginator = client.get_paginator("list_aliases")
    list_availability_configurations_paginator: ListAvailabilityConfigurationsPaginator = client.get_paginator("list_availability_configurations")
    list_group_members_paginator: ListGroupMembersPaginator = client.get_paginator("list_group_members")
    list_groups_paginator: ListGroupsPaginator = client.get_paginator("list_groups")
    list_mailbox_permissions_paginator: ListMailboxPermissionsPaginator = client.get_paginator("list_mailbox_permissions")
    list_organizations_paginator: ListOrganizationsPaginator = client.get_paginator("list_organizations")
    list_resource_delegates_paginator: ListResourceDelegatesPaginator = client.get_paginator("list_resource_delegates")
    list_resources_paginator: ListResourcesPaginator = client.get_paginator("list_resources")
    list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
    ```
"""

import sys
from typing import Generic, Iterator, TypeVar

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAliasesRequestListAliasesPaginateTypeDef,
    ListAliasesResponseTypeDef,
    ListAvailabilityConfigurationsRequestListAvailabilityConfigurationsPaginateTypeDef,
    ListAvailabilityConfigurationsResponseTypeDef,
    ListGroupMembersRequestListGroupMembersPaginateTypeDef,
    ListGroupMembersResponseTypeDef,
    ListGroupsRequestListGroupsPaginateTypeDef,
    ListGroupsResponseTypeDef,
    ListMailboxPermissionsRequestListMailboxPermissionsPaginateTypeDef,
    ListMailboxPermissionsResponseTypeDef,
    ListOrganizationsRequestListOrganizationsPaginateTypeDef,
    ListOrganizationsResponseTypeDef,
    ListResourceDelegatesRequestListResourceDelegatesPaginateTypeDef,
    ListResourceDelegatesResponseTypeDef,
    ListResourcesRequestListResourcesPaginateTypeDef,
    ListResourcesResponseTypeDef,
    ListUsersRequestListUsersPaginateTypeDef,
    ListUsersResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack


__all__ = (
    "ListAliasesPaginator",
    "ListAvailabilityConfigurationsPaginator",
    "ListGroupMembersPaginator",
    "ListGroupsPaginator",
    "ListMailboxPermissionsPaginator",
    "ListOrganizationsPaginator",
    "ListResourceDelegatesPaginator",
    "ListResourcesPaginator",
    "ListUsersPaginator",
)


_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class ListAliasesPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListAliases)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listaliasespaginator)
    """

    def paginate(
        self, **kwargs: Unpack[ListAliasesRequestListAliasesPaginateTypeDef]
    ) -> _PageIterator[ListAliasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListAliases.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listaliasespaginator)
        """


class ListAvailabilityConfigurationsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListAvailabilityConfigurations)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listavailabilityconfigurationspaginator)
    """

    def paginate(
        self,
        **kwargs: Unpack[
            ListAvailabilityConfigurationsRequestListAvailabilityConfigurationsPaginateTypeDef
        ],
    ) -> _PageIterator[ListAvailabilityConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListAvailabilityConfigurations.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listavailabilityconfigurationspaginator)
        """


class ListGroupMembersPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListGroupMembers)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listgroupmemberspaginator)
    """

    def paginate(
        self, **kwargs: Unpack[ListGroupMembersRequestListGroupMembersPaginateTypeDef]
    ) -> _PageIterator[ListGroupMembersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListGroupMembers.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listgroupmemberspaginator)
        """


class ListGroupsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListGroups)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listgroupspaginator)
    """

    def paginate(
        self, **kwargs: Unpack[ListGroupsRequestListGroupsPaginateTypeDef]
    ) -> _PageIterator[ListGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListGroups.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listgroupspaginator)
        """


class ListMailboxPermissionsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListMailboxPermissions)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listmailboxpermissionspaginator)
    """

    def paginate(
        self, **kwargs: Unpack[ListMailboxPermissionsRequestListMailboxPermissionsPaginateTypeDef]
    ) -> _PageIterator[ListMailboxPermissionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListMailboxPermissions.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listmailboxpermissionspaginator)
        """


class ListOrganizationsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListOrganizations)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listorganizationspaginator)
    """

    def paginate(
        self, **kwargs: Unpack[ListOrganizationsRequestListOrganizationsPaginateTypeDef]
    ) -> _PageIterator[ListOrganizationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListOrganizations.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listorganizationspaginator)
        """


class ListResourceDelegatesPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListResourceDelegates)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listresourcedelegatespaginator)
    """

    def paginate(
        self, **kwargs: Unpack[ListResourceDelegatesRequestListResourceDelegatesPaginateTypeDef]
    ) -> _PageIterator[ListResourceDelegatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListResourceDelegates.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listresourcedelegatespaginator)
        """


class ListResourcesPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListResources)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listresourcespaginator)
    """

    def paginate(
        self, **kwargs: Unpack[ListResourcesRequestListResourcesPaginateTypeDef]
    ) -> _PageIterator[ListResourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListResources.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listresourcespaginator)
        """


class ListUsersPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListUsers)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listuserspaginator)
    """

    def paginate(
        self, **kwargs: Unpack[ListUsersRequestListUsersPaginateTypeDef]
    ) -> _PageIterator[ListUsersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workmail.html#WorkMail.Paginator.ListUsers.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmail/paginators/#listuserspaginator)
        """
