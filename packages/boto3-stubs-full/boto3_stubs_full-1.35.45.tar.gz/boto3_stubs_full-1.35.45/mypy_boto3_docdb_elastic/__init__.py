"""
Main interface for docdb-elastic service.

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_docdb_elastic import (
        Client,
        DocDBElasticClient,
        ListClusterSnapshotsPaginator,
        ListClustersPaginator,
    )

    session = Session()
    client: DocDBElasticClient = session.client("docdb-elastic")

    list_cluster_snapshots_paginator: ListClusterSnapshotsPaginator = client.get_paginator("list_cluster_snapshots")
    list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
    ```
"""

from .client import DocDBElasticClient
from .paginator import ListClusterSnapshotsPaginator, ListClustersPaginator

Client = DocDBElasticClient


__all__ = ("Client", "DocDBElasticClient", "ListClusterSnapshotsPaginator", "ListClustersPaginator")
