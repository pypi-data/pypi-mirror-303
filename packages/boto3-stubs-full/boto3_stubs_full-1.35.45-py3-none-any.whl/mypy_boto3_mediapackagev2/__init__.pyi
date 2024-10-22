"""
Main interface for mediapackagev2 service.

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_mediapackagev2 import (
        Client,
        ListChannelGroupsPaginator,
        ListChannelsPaginator,
        ListOriginEndpointsPaginator,
        Mediapackagev2Client,
    )

    session = Session()
    client: Mediapackagev2Client = session.client("mediapackagev2")

    list_channel_groups_paginator: ListChannelGroupsPaginator = client.get_paginator("list_channel_groups")
    list_channels_paginator: ListChannelsPaginator = client.get_paginator("list_channels")
    list_origin_endpoints_paginator: ListOriginEndpointsPaginator = client.get_paginator("list_origin_endpoints")
    ```
"""

from .client import Mediapackagev2Client
from .paginator import (
    ListChannelGroupsPaginator,
    ListChannelsPaginator,
    ListOriginEndpointsPaginator,
)

Client = Mediapackagev2Client

__all__ = (
    "Client",
    "ListChannelGroupsPaginator",
    "ListChannelsPaginator",
    "ListOriginEndpointsPaginator",
    "Mediapackagev2Client",
)
