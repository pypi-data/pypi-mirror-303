"""
Type annotations for workspaces-web service client paginators.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/paginators/)

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_workspaces_web.client import WorkSpacesWebClient
    from mypy_boto3_workspaces_web.paginator import (
        ListSessionsPaginator,
    )

    session = Session()
    client: WorkSpacesWebClient = session.client("workspaces-web")

    list_sessions_paginator: ListSessionsPaginator = client.get_paginator("list_sessions")
    ```
"""

import sys
from typing import Generic, Iterator, TypeVar

from botocore.paginate import PageIterator, Paginator

from .type_defs import ListSessionsRequestListSessionsPaginateTypeDef, ListSessionsResponseTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack


__all__ = ("ListSessionsPaginator",)


_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class ListSessionsPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Paginator.ListSessions)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/paginators/#listsessionspaginator)
    """

    def paginate(
        self, **kwargs: Unpack[ListSessionsRequestListSessionsPaginateTypeDef]
    ) -> _PageIterator[ListSessionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Paginator.ListSessions.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/paginators/#listsessionspaginator)
        """
