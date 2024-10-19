"""
Main interface for workspaces-web service.

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_workspaces_web import (
        Client,
        ListSessionsPaginator,
        WorkSpacesWebClient,
    )

    session = Session()
    client: WorkSpacesWebClient = session.client("workspaces-web")

    list_sessions_paginator: ListSessionsPaginator = client.get_paginator("list_sessions")
    ```
"""

from .client import WorkSpacesWebClient
from .paginator import ListSessionsPaginator

Client = WorkSpacesWebClient


__all__ = ("Client", "ListSessionsPaginator", "WorkSpacesWebClient")
