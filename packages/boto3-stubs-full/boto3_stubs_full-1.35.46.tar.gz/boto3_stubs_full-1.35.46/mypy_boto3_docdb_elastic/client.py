"""
Type annotations for docdb-elastic service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_docdb_elastic.client import DocDBElasticClient

    session = Session()
    client: DocDBElasticClient = session.client("docdb-elastic")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import ListClusterSnapshotsPaginator, ListClustersPaginator
from .type_defs import (
    CopyClusterSnapshotInputRequestTypeDef,
    CopyClusterSnapshotOutputTypeDef,
    CreateClusterInputRequestTypeDef,
    CreateClusterOutputTypeDef,
    CreateClusterSnapshotInputRequestTypeDef,
    CreateClusterSnapshotOutputTypeDef,
    DeleteClusterInputRequestTypeDef,
    DeleteClusterOutputTypeDef,
    DeleteClusterSnapshotInputRequestTypeDef,
    DeleteClusterSnapshotOutputTypeDef,
    GetClusterInputRequestTypeDef,
    GetClusterOutputTypeDef,
    GetClusterSnapshotInputRequestTypeDef,
    GetClusterSnapshotOutputTypeDef,
    ListClustersInputRequestTypeDef,
    ListClusterSnapshotsInputRequestTypeDef,
    ListClusterSnapshotsOutputTypeDef,
    ListClustersOutputTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    RestoreClusterFromSnapshotInputRequestTypeDef,
    RestoreClusterFromSnapshotOutputTypeDef,
    StartClusterInputRequestTypeDef,
    StartClusterOutputTypeDef,
    StopClusterInputRequestTypeDef,
    StopClusterOutputTypeDef,
    TagResourceRequestRequestTypeDef,
    UntagResourceRequestRequestTypeDef,
    UpdateClusterInputRequestTypeDef,
    UpdateClusterOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack


__all__ = ("DocDBElasticClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class DocDBElasticClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic.html#DocDBElastic.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DocDBElasticClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic.html#DocDBElastic.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic.html#DocDBElastic.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic.html#DocDBElastic.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client/#close)
        """

    def copy_cluster_snapshot(
        self, **kwargs: Unpack[CopyClusterSnapshotInputRequestTypeDef]
    ) -> CopyClusterSnapshotOutputTypeDef:
        """
        Copies a snapshot of an elastic cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic.html#DocDBElastic.Client.copy_cluster_snapshot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client/#copy_cluster_snapshot)
        """

    def create_cluster(
        self, **kwargs: Unpack[CreateClusterInputRequestTypeDef]
    ) -> CreateClusterOutputTypeDef:
        """
        Creates a new Amazon DocumentDB elastic cluster and returns its cluster
        structure.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic.html#DocDBElastic.Client.create_cluster)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client/#create_cluster)
        """

    def create_cluster_snapshot(
        self, **kwargs: Unpack[CreateClusterSnapshotInputRequestTypeDef]
    ) -> CreateClusterSnapshotOutputTypeDef:
        """
        Creates a snapshot of an elastic cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic.html#DocDBElastic.Client.create_cluster_snapshot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client/#create_cluster_snapshot)
        """

    def delete_cluster(
        self, **kwargs: Unpack[DeleteClusterInputRequestTypeDef]
    ) -> DeleteClusterOutputTypeDef:
        """
        Delete an elastic cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic.html#DocDBElastic.Client.delete_cluster)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client/#delete_cluster)
        """

    def delete_cluster_snapshot(
        self, **kwargs: Unpack[DeleteClusterSnapshotInputRequestTypeDef]
    ) -> DeleteClusterSnapshotOutputTypeDef:
        """
        Delete an elastic cluster snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic.html#DocDBElastic.Client.delete_cluster_snapshot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client/#delete_cluster_snapshot)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic.html#DocDBElastic.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client/#generate_presigned_url)
        """

    def get_cluster(
        self, **kwargs: Unpack[GetClusterInputRequestTypeDef]
    ) -> GetClusterOutputTypeDef:
        """
        Returns information about a specific elastic cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic.html#DocDBElastic.Client.get_cluster)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client/#get_cluster)
        """

    def get_cluster_snapshot(
        self, **kwargs: Unpack[GetClusterSnapshotInputRequestTypeDef]
    ) -> GetClusterSnapshotOutputTypeDef:
        """
        Returns information about a specific elastic cluster snapshot See also: [AWS
        API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/docdb-elastic-2022-11-28/GetClusterSnapshot).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic.html#DocDBElastic.Client.get_cluster_snapshot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client/#get_cluster_snapshot)
        """

    def list_cluster_snapshots(
        self, **kwargs: Unpack[ListClusterSnapshotsInputRequestTypeDef]
    ) -> ListClusterSnapshotsOutputTypeDef:
        """
        Returns information about snapshots for a specified elastic cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic.html#DocDBElastic.Client.list_cluster_snapshots)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client/#list_cluster_snapshots)
        """

    def list_clusters(
        self, **kwargs: Unpack[ListClustersInputRequestTypeDef]
    ) -> ListClustersOutputTypeDef:
        """
        Returns information about provisioned Amazon DocumentDB elastic clusters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic.html#DocDBElastic.Client.list_clusters)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client/#list_clusters)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all tags on a elastic cluster resource See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/docdb-elastic-2022-11-28/ListTagsForResource).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic.html#DocDBElastic.Client.list_tags_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client/#list_tags_for_resource)
        """

    def restore_cluster_from_snapshot(
        self, **kwargs: Unpack[RestoreClusterFromSnapshotInputRequestTypeDef]
    ) -> RestoreClusterFromSnapshotOutputTypeDef:
        """
        Restores an elastic cluster from a snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic.html#DocDBElastic.Client.restore_cluster_from_snapshot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client/#restore_cluster_from_snapshot)
        """

    def start_cluster(
        self, **kwargs: Unpack[StartClusterInputRequestTypeDef]
    ) -> StartClusterOutputTypeDef:
        """
        Restarts the stopped elastic cluster that is specified by `clusterARN`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic.html#DocDBElastic.Client.start_cluster)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client/#start_cluster)
        """

    def stop_cluster(
        self, **kwargs: Unpack[StopClusterInputRequestTypeDef]
    ) -> StopClusterOutputTypeDef:
        """
        Stops the running elastic cluster that is specified by `clusterArn`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic.html#DocDBElastic.Client.stop_cluster)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client/#stop_cluster)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds metadata tags to an elastic cluster resource See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/docdb-elastic-2022-11-28/TagResource).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic.html#DocDBElastic.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes metadata tags from an elastic cluster resource See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/docdb-elastic-2022-11-28/UntagResource).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic.html#DocDBElastic.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client/#untag_resource)
        """

    def update_cluster(
        self, **kwargs: Unpack[UpdateClusterInputRequestTypeDef]
    ) -> UpdateClusterOutputTypeDef:
        """
        Modifies an elastic cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic.html#DocDBElastic.Client.update_cluster)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client/#update_cluster)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_cluster_snapshots"]
    ) -> ListClusterSnapshotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic.html#DocDBElastic.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_clusters"]) -> ListClustersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic.html#DocDBElastic.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client/#get_paginator)
        """
