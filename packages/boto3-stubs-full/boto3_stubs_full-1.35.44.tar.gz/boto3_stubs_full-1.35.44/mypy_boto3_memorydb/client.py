"""
Type annotations for memorydb service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_memorydb.client import MemoryDBClient

    session = Session()
    client: MemoryDBClient = session.client("memorydb")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    DescribeACLsPaginator,
    DescribeClustersPaginator,
    DescribeEngineVersionsPaginator,
    DescribeEventsPaginator,
    DescribeParameterGroupsPaginator,
    DescribeParametersPaginator,
    DescribeReservedNodesOfferingsPaginator,
    DescribeReservedNodesPaginator,
    DescribeServiceUpdatesPaginator,
    DescribeSnapshotsPaginator,
    DescribeSubnetGroupsPaginator,
    DescribeUsersPaginator,
)
from .type_defs import (
    BatchUpdateClusterRequestRequestTypeDef,
    BatchUpdateClusterResponseTypeDef,
    CopySnapshotRequestRequestTypeDef,
    CopySnapshotResponseTypeDef,
    CreateACLRequestRequestTypeDef,
    CreateACLResponseTypeDef,
    CreateClusterRequestRequestTypeDef,
    CreateClusterResponseTypeDef,
    CreateParameterGroupRequestRequestTypeDef,
    CreateParameterGroupResponseTypeDef,
    CreateSnapshotRequestRequestTypeDef,
    CreateSnapshotResponseTypeDef,
    CreateSubnetGroupRequestRequestTypeDef,
    CreateSubnetGroupResponseTypeDef,
    CreateUserRequestRequestTypeDef,
    CreateUserResponseTypeDef,
    DeleteACLRequestRequestTypeDef,
    DeleteACLResponseTypeDef,
    DeleteClusterRequestRequestTypeDef,
    DeleteClusterResponseTypeDef,
    DeleteParameterGroupRequestRequestTypeDef,
    DeleteParameterGroupResponseTypeDef,
    DeleteSnapshotRequestRequestTypeDef,
    DeleteSnapshotResponseTypeDef,
    DeleteSubnetGroupRequestRequestTypeDef,
    DeleteSubnetGroupResponseTypeDef,
    DeleteUserRequestRequestTypeDef,
    DeleteUserResponseTypeDef,
    DescribeACLsRequestRequestTypeDef,
    DescribeACLsResponseTypeDef,
    DescribeClustersRequestRequestTypeDef,
    DescribeClustersResponseTypeDef,
    DescribeEngineVersionsRequestRequestTypeDef,
    DescribeEngineVersionsResponseTypeDef,
    DescribeEventsRequestRequestTypeDef,
    DescribeEventsResponseTypeDef,
    DescribeParameterGroupsRequestRequestTypeDef,
    DescribeParameterGroupsResponseTypeDef,
    DescribeParametersRequestRequestTypeDef,
    DescribeParametersResponseTypeDef,
    DescribeReservedNodesOfferingsRequestRequestTypeDef,
    DescribeReservedNodesOfferingsResponseTypeDef,
    DescribeReservedNodesRequestRequestTypeDef,
    DescribeReservedNodesResponseTypeDef,
    DescribeServiceUpdatesRequestRequestTypeDef,
    DescribeServiceUpdatesResponseTypeDef,
    DescribeSnapshotsRequestRequestTypeDef,
    DescribeSnapshotsResponseTypeDef,
    DescribeSubnetGroupsRequestRequestTypeDef,
    DescribeSubnetGroupsResponseTypeDef,
    DescribeUsersRequestRequestTypeDef,
    DescribeUsersResponseTypeDef,
    FailoverShardRequestRequestTypeDef,
    FailoverShardResponseTypeDef,
    ListAllowedNodeTypeUpdatesRequestRequestTypeDef,
    ListAllowedNodeTypeUpdatesResponseTypeDef,
    ListTagsRequestRequestTypeDef,
    ListTagsResponseTypeDef,
    PurchaseReservedNodesOfferingRequestRequestTypeDef,
    PurchaseReservedNodesOfferingResponseTypeDef,
    ResetParameterGroupRequestRequestTypeDef,
    ResetParameterGroupResponseTypeDef,
    TagResourceRequestRequestTypeDef,
    TagResourceResponseTypeDef,
    UntagResourceRequestRequestTypeDef,
    UntagResourceResponseTypeDef,
    UpdateACLRequestRequestTypeDef,
    UpdateACLResponseTypeDef,
    UpdateClusterRequestRequestTypeDef,
    UpdateClusterResponseTypeDef,
    UpdateParameterGroupRequestRequestTypeDef,
    UpdateParameterGroupResponseTypeDef,
    UpdateSubnetGroupRequestRequestTypeDef,
    UpdateSubnetGroupResponseTypeDef,
    UpdateUserRequestRequestTypeDef,
    UpdateUserResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack


__all__ = ("MemoryDBClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ACLAlreadyExistsFault: Type[BotocoreClientError]
    ACLNotFoundFault: Type[BotocoreClientError]
    ACLQuotaExceededFault: Type[BotocoreClientError]
    APICallRateForCustomerExceededFault: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ClusterAlreadyExistsFault: Type[BotocoreClientError]
    ClusterNotFoundFault: Type[BotocoreClientError]
    ClusterQuotaForCustomerExceededFault: Type[BotocoreClientError]
    DefaultUserRequired: Type[BotocoreClientError]
    DuplicateUserNameFault: Type[BotocoreClientError]
    InsufficientClusterCapacityFault: Type[BotocoreClientError]
    InvalidACLStateFault: Type[BotocoreClientError]
    InvalidARNFault: Type[BotocoreClientError]
    InvalidClusterStateFault: Type[BotocoreClientError]
    InvalidCredentialsException: Type[BotocoreClientError]
    InvalidKMSKeyFault: Type[BotocoreClientError]
    InvalidNodeStateFault: Type[BotocoreClientError]
    InvalidParameterCombinationException: Type[BotocoreClientError]
    InvalidParameterGroupStateFault: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    InvalidSnapshotStateFault: Type[BotocoreClientError]
    InvalidSubnet: Type[BotocoreClientError]
    InvalidUserStateFault: Type[BotocoreClientError]
    InvalidVPCNetworkStateFault: Type[BotocoreClientError]
    NoOperationFault: Type[BotocoreClientError]
    NodeQuotaForClusterExceededFault: Type[BotocoreClientError]
    NodeQuotaForCustomerExceededFault: Type[BotocoreClientError]
    ParameterGroupAlreadyExistsFault: Type[BotocoreClientError]
    ParameterGroupNotFoundFault: Type[BotocoreClientError]
    ParameterGroupQuotaExceededFault: Type[BotocoreClientError]
    ReservedNodeAlreadyExistsFault: Type[BotocoreClientError]
    ReservedNodeNotFoundFault: Type[BotocoreClientError]
    ReservedNodeQuotaExceededFault: Type[BotocoreClientError]
    ReservedNodesOfferingNotFoundFault: Type[BotocoreClientError]
    ServiceLinkedRoleNotFoundFault: Type[BotocoreClientError]
    ServiceUpdateNotFoundFault: Type[BotocoreClientError]
    ShardNotFoundFault: Type[BotocoreClientError]
    ShardsPerClusterQuotaExceededFault: Type[BotocoreClientError]
    SnapshotAlreadyExistsFault: Type[BotocoreClientError]
    SnapshotNotFoundFault: Type[BotocoreClientError]
    SnapshotQuotaExceededFault: Type[BotocoreClientError]
    SubnetGroupAlreadyExistsFault: Type[BotocoreClientError]
    SubnetGroupInUseFault: Type[BotocoreClientError]
    SubnetGroupNotFoundFault: Type[BotocoreClientError]
    SubnetGroupQuotaExceededFault: Type[BotocoreClientError]
    SubnetInUse: Type[BotocoreClientError]
    SubnetNotAllowedFault: Type[BotocoreClientError]
    SubnetQuotaExceededFault: Type[BotocoreClientError]
    TagNotFoundFault: Type[BotocoreClientError]
    TagQuotaPerResourceExceeded: Type[BotocoreClientError]
    TestFailoverNotAvailableFault: Type[BotocoreClientError]
    UserAlreadyExistsFault: Type[BotocoreClientError]
    UserNotFoundFault: Type[BotocoreClientError]
    UserQuotaExceededFault: Type[BotocoreClientError]


class MemoryDBClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MemoryDBClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#exceptions)
        """

    def batch_update_cluster(
        self, **kwargs: Unpack[BatchUpdateClusterRequestRequestTypeDef]
    ) -> BatchUpdateClusterResponseTypeDef:
        """
        Apply the service update to a list of clusters supplied.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.batch_update_cluster)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#batch_update_cluster)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#close)
        """

    def copy_snapshot(
        self, **kwargs: Unpack[CopySnapshotRequestRequestTypeDef]
    ) -> CopySnapshotResponseTypeDef:
        """
        Makes a copy of an existing snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.copy_snapshot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#copy_snapshot)
        """

    def create_acl(
        self, **kwargs: Unpack[CreateACLRequestRequestTypeDef]
    ) -> CreateACLResponseTypeDef:
        """
        Creates an Access Control List.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.create_acl)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#create_acl)
        """

    def create_cluster(
        self, **kwargs: Unpack[CreateClusterRequestRequestTypeDef]
    ) -> CreateClusterResponseTypeDef:
        """
        Creates a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.create_cluster)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#create_cluster)
        """

    def create_parameter_group(
        self, **kwargs: Unpack[CreateParameterGroupRequestRequestTypeDef]
    ) -> CreateParameterGroupResponseTypeDef:
        """
        Creates a new MemoryDB parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.create_parameter_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#create_parameter_group)
        """

    def create_snapshot(
        self, **kwargs: Unpack[CreateSnapshotRequestRequestTypeDef]
    ) -> CreateSnapshotResponseTypeDef:
        """
        Creates a copy of an entire cluster at a specific moment in time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.create_snapshot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#create_snapshot)
        """

    def create_subnet_group(
        self, **kwargs: Unpack[CreateSubnetGroupRequestRequestTypeDef]
    ) -> CreateSubnetGroupResponseTypeDef:
        """
        Creates a subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.create_subnet_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#create_subnet_group)
        """

    def create_user(
        self, **kwargs: Unpack[CreateUserRequestRequestTypeDef]
    ) -> CreateUserResponseTypeDef:
        """
        Creates a MemoryDB user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.create_user)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#create_user)
        """

    def delete_acl(
        self, **kwargs: Unpack[DeleteACLRequestRequestTypeDef]
    ) -> DeleteACLResponseTypeDef:
        """
        Deletes an Access Control List.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.delete_acl)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#delete_acl)
        """

    def delete_cluster(
        self, **kwargs: Unpack[DeleteClusterRequestRequestTypeDef]
    ) -> DeleteClusterResponseTypeDef:
        """
        Deletes a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.delete_cluster)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#delete_cluster)
        """

    def delete_parameter_group(
        self, **kwargs: Unpack[DeleteParameterGroupRequestRequestTypeDef]
    ) -> DeleteParameterGroupResponseTypeDef:
        """
        Deletes the specified parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.delete_parameter_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#delete_parameter_group)
        """

    def delete_snapshot(
        self, **kwargs: Unpack[DeleteSnapshotRequestRequestTypeDef]
    ) -> DeleteSnapshotResponseTypeDef:
        """
        Deletes an existing snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.delete_snapshot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#delete_snapshot)
        """

    def delete_subnet_group(
        self, **kwargs: Unpack[DeleteSubnetGroupRequestRequestTypeDef]
    ) -> DeleteSubnetGroupResponseTypeDef:
        """
        Deletes a subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.delete_subnet_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#delete_subnet_group)
        """

    def delete_user(
        self, **kwargs: Unpack[DeleteUserRequestRequestTypeDef]
    ) -> DeleteUserResponseTypeDef:
        """
        Deletes a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.delete_user)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#delete_user)
        """

    def describe_acls(
        self, **kwargs: Unpack[DescribeACLsRequestRequestTypeDef]
    ) -> DescribeACLsResponseTypeDef:
        """
        Returns a list of ACLs See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/memorydb-2021-01-01/DescribeACLs).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.describe_acls)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#describe_acls)
        """

    def describe_clusters(
        self, **kwargs: Unpack[DescribeClustersRequestRequestTypeDef]
    ) -> DescribeClustersResponseTypeDef:
        """
        Returns information about all provisioned clusters if no cluster identifier is
        specified, or about a specific cluster if a cluster name is
        supplied.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.describe_clusters)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#describe_clusters)
        """

    def describe_engine_versions(
        self, **kwargs: Unpack[DescribeEngineVersionsRequestRequestTypeDef]
    ) -> DescribeEngineVersionsResponseTypeDef:
        """
        Returns a list of the available engine versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.describe_engine_versions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#describe_engine_versions)
        """

    def describe_events(
        self, **kwargs: Unpack[DescribeEventsRequestRequestTypeDef]
    ) -> DescribeEventsResponseTypeDef:
        """
        Returns events related to clusters, security groups, and parameter groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.describe_events)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#describe_events)
        """

    def describe_parameter_groups(
        self, **kwargs: Unpack[DescribeParameterGroupsRequestRequestTypeDef]
    ) -> DescribeParameterGroupsResponseTypeDef:
        """
        Returns a list of parameter group descriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.describe_parameter_groups)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#describe_parameter_groups)
        """

    def describe_parameters(
        self, **kwargs: Unpack[DescribeParametersRequestRequestTypeDef]
    ) -> DescribeParametersResponseTypeDef:
        """
        Returns the detailed parameter list for a particular parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.describe_parameters)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#describe_parameters)
        """

    def describe_reserved_nodes(
        self, **kwargs: Unpack[DescribeReservedNodesRequestRequestTypeDef]
    ) -> DescribeReservedNodesResponseTypeDef:
        """
        Returns information about reserved nodes for this account, or about a specified
        reserved
        node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.describe_reserved_nodes)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#describe_reserved_nodes)
        """

    def describe_reserved_nodes_offerings(
        self, **kwargs: Unpack[DescribeReservedNodesOfferingsRequestRequestTypeDef]
    ) -> DescribeReservedNodesOfferingsResponseTypeDef:
        """
        Lists available reserved node offerings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.describe_reserved_nodes_offerings)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#describe_reserved_nodes_offerings)
        """

    def describe_service_updates(
        self, **kwargs: Unpack[DescribeServiceUpdatesRequestRequestTypeDef]
    ) -> DescribeServiceUpdatesResponseTypeDef:
        """
        Returns details of the service updates See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/memorydb-2021-01-01/DescribeServiceUpdates).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.describe_service_updates)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#describe_service_updates)
        """

    def describe_snapshots(
        self, **kwargs: Unpack[DescribeSnapshotsRequestRequestTypeDef]
    ) -> DescribeSnapshotsResponseTypeDef:
        """
        Returns information about cluster snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.describe_snapshots)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#describe_snapshots)
        """

    def describe_subnet_groups(
        self, **kwargs: Unpack[DescribeSubnetGroupsRequestRequestTypeDef]
    ) -> DescribeSubnetGroupsResponseTypeDef:
        """
        Returns a list of subnet group descriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.describe_subnet_groups)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#describe_subnet_groups)
        """

    def describe_users(
        self, **kwargs: Unpack[DescribeUsersRequestRequestTypeDef]
    ) -> DescribeUsersResponseTypeDef:
        """
        Returns a list of users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.describe_users)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#describe_users)
        """

    def failover_shard(
        self, **kwargs: Unpack[FailoverShardRequestRequestTypeDef]
    ) -> FailoverShardResponseTypeDef:
        """
        Used to failover a shard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.failover_shard)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#failover_shard)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#generate_presigned_url)
        """

    def list_allowed_node_type_updates(
        self, **kwargs: Unpack[ListAllowedNodeTypeUpdatesRequestRequestTypeDef]
    ) -> ListAllowedNodeTypeUpdatesResponseTypeDef:
        """
        Lists all available node types that you can scale to from your cluster's
        current node
        type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.list_allowed_node_type_updates)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#list_allowed_node_type_updates)
        """

    def list_tags(self, **kwargs: Unpack[ListTagsRequestRequestTypeDef]) -> ListTagsResponseTypeDef:
        """
        Lists all tags currently on a named resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.list_tags)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#list_tags)
        """

    def purchase_reserved_nodes_offering(
        self, **kwargs: Unpack[PurchaseReservedNodesOfferingRequestRequestTypeDef]
    ) -> PurchaseReservedNodesOfferingResponseTypeDef:
        """
        Allows you to purchase a reserved node offering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.purchase_reserved_nodes_offering)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#purchase_reserved_nodes_offering)
        """

    def reset_parameter_group(
        self, **kwargs: Unpack[ResetParameterGroupRequestRequestTypeDef]
    ) -> ResetParameterGroupResponseTypeDef:
        """
        Modifies the parameters of a parameter group to the engine or system default
        value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.reset_parameter_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#reset_parameter_group)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]
    ) -> TagResourceResponseTypeDef:
        """
        A tag is a key-value pair where the key and value are case-sensitive.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> UntagResourceResponseTypeDef:
        """
        Use this operation to remove tags on a resource See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/memorydb-2021-01-01/UntagResource).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#untag_resource)
        """

    def update_acl(
        self, **kwargs: Unpack[UpdateACLRequestRequestTypeDef]
    ) -> UpdateACLResponseTypeDef:
        """
        Changes the list of users that belong to the Access Control List.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.update_acl)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#update_acl)
        """

    def update_cluster(
        self, **kwargs: Unpack[UpdateClusterRequestRequestTypeDef]
    ) -> UpdateClusterResponseTypeDef:
        """
        Modifies the settings for a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.update_cluster)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#update_cluster)
        """

    def update_parameter_group(
        self, **kwargs: Unpack[UpdateParameterGroupRequestRequestTypeDef]
    ) -> UpdateParameterGroupResponseTypeDef:
        """
        Updates the parameters of a parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.update_parameter_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#update_parameter_group)
        """

    def update_subnet_group(
        self, **kwargs: Unpack[UpdateSubnetGroupRequestRequestTypeDef]
    ) -> UpdateSubnetGroupResponseTypeDef:
        """
        Updates a subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.update_subnet_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#update_subnet_group)
        """

    def update_user(
        self, **kwargs: Unpack[UpdateUserRequestRequestTypeDef]
    ) -> UpdateUserResponseTypeDef:
        """
        Changes user password(s) and/or access string.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.update_user)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#update_user)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_acls"]) -> DescribeACLsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_clusters"]
    ) -> DescribeClustersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_engine_versions"]
    ) -> DescribeEngineVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_events"]) -> DescribeEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_parameter_groups"]
    ) -> DescribeParameterGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_parameters"]
    ) -> DescribeParametersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_nodes"]
    ) -> DescribeReservedNodesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_nodes_offerings"]
    ) -> DescribeReservedNodesOfferingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_service_updates"]
    ) -> DescribeServiceUpdatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_snapshots"]
    ) -> DescribeSnapshotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_subnet_groups"]
    ) -> DescribeSubnetGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_users"]) -> DescribeUsersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#get_paginator)
        """
