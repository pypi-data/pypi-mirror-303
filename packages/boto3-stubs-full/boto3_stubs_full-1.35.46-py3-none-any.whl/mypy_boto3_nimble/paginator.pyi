"""
Type annotations for nimble service client paginators.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators/)

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_nimble.client import NimbleStudioClient
    from mypy_boto3_nimble.paginator import (
        ListEulaAcceptancesPaginator,
        ListEulasPaginator,
        ListLaunchProfileMembersPaginator,
        ListLaunchProfilesPaginator,
        ListStreamingImagesPaginator,
        ListStreamingSessionBackupsPaginator,
        ListStreamingSessionsPaginator,
        ListStudioComponentsPaginator,
        ListStudioMembersPaginator,
        ListStudiosPaginator,
    )

    session = Session()
    client: NimbleStudioClient = session.client("nimble")

    list_eula_acceptances_paginator: ListEulaAcceptancesPaginator = client.get_paginator("list_eula_acceptances")
    list_eulas_paginator: ListEulasPaginator = client.get_paginator("list_eulas")
    list_launch_profile_members_paginator: ListLaunchProfileMembersPaginator = client.get_paginator("list_launch_profile_members")
    list_launch_profiles_paginator: ListLaunchProfilesPaginator = client.get_paginator("list_launch_profiles")
    list_streaming_images_paginator: ListStreamingImagesPaginator = client.get_paginator("list_streaming_images")
    list_streaming_session_backups_paginator: ListStreamingSessionBackupsPaginator = client.get_paginator("list_streaming_session_backups")
    list_streaming_sessions_paginator: ListStreamingSessionsPaginator = client.get_paginator("list_streaming_sessions")
    list_studio_components_paginator: ListStudioComponentsPaginator = client.get_paginator("list_studio_components")
    list_studio_members_paginator: ListStudioMembersPaginator = client.get_paginator("list_studio_members")
    list_studios_paginator: ListStudiosPaginator = client.get_paginator("list_studios")
    ```
"""

import sys
from typing import Generic, Iterator, TypeVar

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListEulaAcceptancesRequestListEulaAcceptancesPaginateTypeDef,
    ListEulaAcceptancesResponseTypeDef,
    ListEulasRequestListEulasPaginateTypeDef,
    ListEulasResponseTypeDef,
    ListLaunchProfileMembersRequestListLaunchProfileMembersPaginateTypeDef,
    ListLaunchProfileMembersResponseTypeDef,
    ListLaunchProfilesRequestListLaunchProfilesPaginateTypeDef,
    ListLaunchProfilesResponseTypeDef,
    ListStreamingImagesRequestListStreamingImagesPaginateTypeDef,
    ListStreamingImagesResponseTypeDef,
    ListStreamingSessionBackupsRequestListStreamingSessionBackupsPaginateTypeDef,
    ListStreamingSessionBackupsResponseTypeDef,
    ListStreamingSessionsRequestListStreamingSessionsPaginateTypeDef,
    ListStreamingSessionsResponseTypeDef,
    ListStudioComponentsRequestListStudioComponentsPaginateTypeDef,
    ListStudioComponentsResponseTypeDef,
    ListStudioMembersRequestListStudioMembersPaginateTypeDef,
    ListStudioMembersResponseTypeDef,
    ListStudiosRequestListStudiosPaginateTypeDef,
    ListStudiosResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListEulaAcceptancesPaginator",
    "ListEulasPaginator",
    "ListLaunchProfileMembersPaginator",
    "ListLaunchProfilesPaginator",
    "ListStreamingImagesPaginator",
    "ListStreamingSessionBackupsPaginator",
    "ListStreamingSessionsPaginator",
    "ListStudioComponentsPaginator",
    "ListStudioMembersPaginator",
    "ListStudiosPaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")

class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """

class ListEulaAcceptancesPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Paginator.ListEulaAcceptances)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators/#listeulaacceptancespaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListEulaAcceptancesRequestListEulaAcceptancesPaginateTypeDef]
    ) -> _PageIterator[ListEulaAcceptancesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Paginator.ListEulaAcceptances.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators/#listeulaacceptancespaginator)
        """

class ListEulasPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Paginator.ListEulas)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators/#listeulaspaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListEulasRequestListEulasPaginateTypeDef]
    ) -> _PageIterator[ListEulasResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Paginator.ListEulas.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators/#listeulaspaginator)
        """

class ListLaunchProfileMembersPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Paginator.ListLaunchProfileMembers)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators/#listlaunchprofilememberspaginator)
    """
    def paginate(
        self,
        **kwargs: Unpack[ListLaunchProfileMembersRequestListLaunchProfileMembersPaginateTypeDef],
    ) -> _PageIterator[ListLaunchProfileMembersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Paginator.ListLaunchProfileMembers.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators/#listlaunchprofilememberspaginator)
        """

class ListLaunchProfilesPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Paginator.ListLaunchProfiles)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators/#listlaunchprofilespaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListLaunchProfilesRequestListLaunchProfilesPaginateTypeDef]
    ) -> _PageIterator[ListLaunchProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Paginator.ListLaunchProfiles.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators/#listlaunchprofilespaginator)
        """

class ListStreamingImagesPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Paginator.ListStreamingImages)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators/#liststreamingimagespaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListStreamingImagesRequestListStreamingImagesPaginateTypeDef]
    ) -> _PageIterator[ListStreamingImagesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Paginator.ListStreamingImages.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators/#liststreamingimagespaginator)
        """

class ListStreamingSessionBackupsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Paginator.ListStreamingSessionBackups)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators/#liststreamingsessionbackupspaginator)
    """
    def paginate(
        self,
        **kwargs: Unpack[
            ListStreamingSessionBackupsRequestListStreamingSessionBackupsPaginateTypeDef
        ],
    ) -> _PageIterator[ListStreamingSessionBackupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Paginator.ListStreamingSessionBackups.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators/#liststreamingsessionbackupspaginator)
        """

class ListStreamingSessionsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Paginator.ListStreamingSessions)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators/#liststreamingsessionspaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListStreamingSessionsRequestListStreamingSessionsPaginateTypeDef]
    ) -> _PageIterator[ListStreamingSessionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Paginator.ListStreamingSessions.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators/#liststreamingsessionspaginator)
        """

class ListStudioComponentsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Paginator.ListStudioComponents)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators/#liststudiocomponentspaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListStudioComponentsRequestListStudioComponentsPaginateTypeDef]
    ) -> _PageIterator[ListStudioComponentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Paginator.ListStudioComponents.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators/#liststudiocomponentspaginator)
        """

class ListStudioMembersPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Paginator.ListStudioMembers)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators/#liststudiomemberspaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListStudioMembersRequestListStudioMembersPaginateTypeDef]
    ) -> _PageIterator[ListStudioMembersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Paginator.ListStudioMembers.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators/#liststudiomemberspaginator)
        """

class ListStudiosPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Paginator.ListStudios)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators/#liststudiospaginator)
    """
    def paginate(
        self, **kwargs: Unpack[ListStudiosRequestListStudiosPaginateTypeDef]
    ) -> _PageIterator[ListStudiosResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nimble.html#NimbleStudio.Paginator.ListStudios.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nimble/paginators/#liststudiospaginator)
        """
