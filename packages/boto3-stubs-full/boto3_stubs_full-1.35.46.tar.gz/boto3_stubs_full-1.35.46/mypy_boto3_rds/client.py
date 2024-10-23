"""
Type annotations for rds service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_rds.client import RDSClient

    session = Session()
    client: RDSClient = session.client("rds")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Optional, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    DescribeBlueGreenDeploymentsPaginator,
    DescribeCertificatesPaginator,
    DescribeDBClusterAutomatedBackupsPaginator,
    DescribeDBClusterBacktracksPaginator,
    DescribeDBClusterEndpointsPaginator,
    DescribeDBClusterParameterGroupsPaginator,
    DescribeDBClusterParametersPaginator,
    DescribeDBClusterSnapshotsPaginator,
    DescribeDBClustersPaginator,
    DescribeDBEngineVersionsPaginator,
    DescribeDBInstanceAutomatedBackupsPaginator,
    DescribeDBInstancesPaginator,
    DescribeDBLogFilesPaginator,
    DescribeDBParameterGroupsPaginator,
    DescribeDBParametersPaginator,
    DescribeDBProxiesPaginator,
    DescribeDBProxyEndpointsPaginator,
    DescribeDBProxyTargetGroupsPaginator,
    DescribeDBProxyTargetsPaginator,
    DescribeDBRecommendationsPaginator,
    DescribeDBSecurityGroupsPaginator,
    DescribeDBSnapshotsPaginator,
    DescribeDBSnapshotTenantDatabasesPaginator,
    DescribeDBSubnetGroupsPaginator,
    DescribeEngineDefaultClusterParametersPaginator,
    DescribeEngineDefaultParametersPaginator,
    DescribeEventsPaginator,
    DescribeEventSubscriptionsPaginator,
    DescribeExportTasksPaginator,
    DescribeGlobalClustersPaginator,
    DescribeIntegrationsPaginator,
    DescribeOptionGroupOptionsPaginator,
    DescribeOptionGroupsPaginator,
    DescribeOrderableDBInstanceOptionsPaginator,
    DescribePendingMaintenanceActionsPaginator,
    DescribeReservedDBInstancesOfferingsPaginator,
    DescribeReservedDBInstancesPaginator,
    DescribeSourceRegionsPaginator,
    DescribeTenantDatabasesPaginator,
    DownloadDBLogFilePortionPaginator,
)
from .type_defs import (
    AccountAttributesMessageTypeDef,
    AddRoleToDBClusterMessageRequestTypeDef,
    AddRoleToDBInstanceMessageRequestTypeDef,
    AddSourceIdentifierToSubscriptionMessageRequestTypeDef,
    AddSourceIdentifierToSubscriptionResultTypeDef,
    AddTagsToResourceMessageRequestTypeDef,
    ApplyPendingMaintenanceActionMessageRequestTypeDef,
    ApplyPendingMaintenanceActionResultTypeDef,
    AuthorizeDBSecurityGroupIngressMessageRequestTypeDef,
    AuthorizeDBSecurityGroupIngressResultTypeDef,
    BacktrackDBClusterMessageRequestTypeDef,
    CancelExportTaskMessageRequestTypeDef,
    CertificateMessageTypeDef,
    CopyDBClusterParameterGroupMessageRequestTypeDef,
    CopyDBClusterParameterGroupResultTypeDef,
    CopyDBClusterSnapshotMessageRequestTypeDef,
    CopyDBClusterSnapshotResultTypeDef,
    CopyDBParameterGroupMessageRequestTypeDef,
    CopyDBParameterGroupResultTypeDef,
    CopyDBSnapshotMessageRequestTypeDef,
    CopyDBSnapshotResultTypeDef,
    CopyOptionGroupMessageRequestTypeDef,
    CopyOptionGroupResultTypeDef,
    CreateBlueGreenDeploymentRequestRequestTypeDef,
    CreateBlueGreenDeploymentResponseTypeDef,
    CreateCustomDBEngineVersionMessageRequestTypeDef,
    CreateDBClusterEndpointMessageRequestTypeDef,
    CreateDBClusterMessageRequestTypeDef,
    CreateDBClusterParameterGroupMessageRequestTypeDef,
    CreateDBClusterParameterGroupResultTypeDef,
    CreateDBClusterResultTypeDef,
    CreateDBClusterSnapshotMessageRequestTypeDef,
    CreateDBClusterSnapshotResultTypeDef,
    CreateDBInstanceMessageRequestTypeDef,
    CreateDBInstanceReadReplicaMessageRequestTypeDef,
    CreateDBInstanceReadReplicaResultTypeDef,
    CreateDBInstanceResultTypeDef,
    CreateDBParameterGroupMessageRequestTypeDef,
    CreateDBParameterGroupResultTypeDef,
    CreateDBProxyEndpointRequestRequestTypeDef,
    CreateDBProxyEndpointResponseTypeDef,
    CreateDBProxyRequestRequestTypeDef,
    CreateDBProxyResponseTypeDef,
    CreateDBSecurityGroupMessageRequestTypeDef,
    CreateDBSecurityGroupResultTypeDef,
    CreateDBShardGroupMessageRequestTypeDef,
    CreateDBSnapshotMessageRequestTypeDef,
    CreateDBSnapshotResultTypeDef,
    CreateDBSubnetGroupMessageRequestTypeDef,
    CreateDBSubnetGroupResultTypeDef,
    CreateEventSubscriptionMessageRequestTypeDef,
    CreateEventSubscriptionResultTypeDef,
    CreateGlobalClusterMessageRequestTypeDef,
    CreateGlobalClusterResultTypeDef,
    CreateIntegrationMessageRequestTypeDef,
    CreateOptionGroupMessageRequestTypeDef,
    CreateOptionGroupResultTypeDef,
    CreateTenantDatabaseMessageRequestTypeDef,
    CreateTenantDatabaseResultTypeDef,
    DBClusterAutomatedBackupMessageTypeDef,
    DBClusterBacktrackMessageTypeDef,
    DBClusterBacktrackResponseTypeDef,
    DBClusterCapacityInfoTypeDef,
    DBClusterEndpointMessageTypeDef,
    DBClusterEndpointResponseTypeDef,
    DBClusterMessageTypeDef,
    DBClusterParameterGroupDetailsTypeDef,
    DBClusterParameterGroupNameMessageTypeDef,
    DBClusterParameterGroupsMessageTypeDef,
    DBClusterSnapshotMessageTypeDef,
    DBEngineVersionMessageTypeDef,
    DBEngineVersionResponseTypeDef,
    DBInstanceAutomatedBackupMessageTypeDef,
    DBInstanceMessageTypeDef,
    DBParameterGroupDetailsTypeDef,
    DBParameterGroupNameMessageTypeDef,
    DBParameterGroupsMessageTypeDef,
    DBRecommendationMessageTypeDef,
    DBRecommendationsMessageTypeDef,
    DBSecurityGroupMessageTypeDef,
    DBShardGroupResponseTypeDef,
    DBSnapshotMessageTypeDef,
    DBSnapshotTenantDatabasesMessageTypeDef,
    DBSubnetGroupMessageTypeDef,
    DeleteBlueGreenDeploymentRequestRequestTypeDef,
    DeleteBlueGreenDeploymentResponseTypeDef,
    DeleteCustomDBEngineVersionMessageRequestTypeDef,
    DeleteDBClusterAutomatedBackupMessageRequestTypeDef,
    DeleteDBClusterAutomatedBackupResultTypeDef,
    DeleteDBClusterEndpointMessageRequestTypeDef,
    DeleteDBClusterMessageRequestTypeDef,
    DeleteDBClusterParameterGroupMessageRequestTypeDef,
    DeleteDBClusterResultTypeDef,
    DeleteDBClusterSnapshotMessageRequestTypeDef,
    DeleteDBClusterSnapshotResultTypeDef,
    DeleteDBInstanceAutomatedBackupMessageRequestTypeDef,
    DeleteDBInstanceAutomatedBackupResultTypeDef,
    DeleteDBInstanceMessageRequestTypeDef,
    DeleteDBInstanceResultTypeDef,
    DeleteDBParameterGroupMessageRequestTypeDef,
    DeleteDBProxyEndpointRequestRequestTypeDef,
    DeleteDBProxyEndpointResponseTypeDef,
    DeleteDBProxyRequestRequestTypeDef,
    DeleteDBProxyResponseTypeDef,
    DeleteDBSecurityGroupMessageRequestTypeDef,
    DeleteDBShardGroupMessageRequestTypeDef,
    DeleteDBSnapshotMessageRequestTypeDef,
    DeleteDBSnapshotResultTypeDef,
    DeleteDBSubnetGroupMessageRequestTypeDef,
    DeleteEventSubscriptionMessageRequestTypeDef,
    DeleteEventSubscriptionResultTypeDef,
    DeleteGlobalClusterMessageRequestTypeDef,
    DeleteGlobalClusterResultTypeDef,
    DeleteIntegrationMessageRequestTypeDef,
    DeleteOptionGroupMessageRequestTypeDef,
    DeleteTenantDatabaseMessageRequestTypeDef,
    DeleteTenantDatabaseResultTypeDef,
    DeregisterDBProxyTargetsRequestRequestTypeDef,
    DescribeBlueGreenDeploymentsRequestRequestTypeDef,
    DescribeBlueGreenDeploymentsResponseTypeDef,
    DescribeCertificatesMessageRequestTypeDef,
    DescribeDBClusterAutomatedBackupsMessageRequestTypeDef,
    DescribeDBClusterBacktracksMessageRequestTypeDef,
    DescribeDBClusterEndpointsMessageRequestTypeDef,
    DescribeDBClusterParameterGroupsMessageRequestTypeDef,
    DescribeDBClusterParametersMessageRequestTypeDef,
    DescribeDBClustersMessageRequestTypeDef,
    DescribeDBClusterSnapshotAttributesMessageRequestTypeDef,
    DescribeDBClusterSnapshotAttributesResultTypeDef,
    DescribeDBClusterSnapshotsMessageRequestTypeDef,
    DescribeDBEngineVersionsMessageRequestTypeDef,
    DescribeDBInstanceAutomatedBackupsMessageRequestTypeDef,
    DescribeDBInstancesMessageRequestTypeDef,
    DescribeDBLogFilesMessageRequestTypeDef,
    DescribeDBLogFilesResponseTypeDef,
    DescribeDBParameterGroupsMessageRequestTypeDef,
    DescribeDBParametersMessageRequestTypeDef,
    DescribeDBProxiesRequestRequestTypeDef,
    DescribeDBProxiesResponseTypeDef,
    DescribeDBProxyEndpointsRequestRequestTypeDef,
    DescribeDBProxyEndpointsResponseTypeDef,
    DescribeDBProxyTargetGroupsRequestRequestTypeDef,
    DescribeDBProxyTargetGroupsResponseTypeDef,
    DescribeDBProxyTargetsRequestRequestTypeDef,
    DescribeDBProxyTargetsResponseTypeDef,
    DescribeDBRecommendationsMessageRequestTypeDef,
    DescribeDBSecurityGroupsMessageRequestTypeDef,
    DescribeDBShardGroupsMessageRequestTypeDef,
    DescribeDBShardGroupsResponseTypeDef,
    DescribeDBSnapshotAttributesMessageRequestTypeDef,
    DescribeDBSnapshotAttributesResultTypeDef,
    DescribeDBSnapshotsMessageRequestTypeDef,
    DescribeDBSnapshotTenantDatabasesMessageRequestTypeDef,
    DescribeDBSubnetGroupsMessageRequestTypeDef,
    DescribeEngineDefaultClusterParametersMessageRequestTypeDef,
    DescribeEngineDefaultClusterParametersResultTypeDef,
    DescribeEngineDefaultParametersMessageRequestTypeDef,
    DescribeEngineDefaultParametersResultTypeDef,
    DescribeEventCategoriesMessageRequestTypeDef,
    DescribeEventsMessageRequestTypeDef,
    DescribeEventSubscriptionsMessageRequestTypeDef,
    DescribeExportTasksMessageRequestTypeDef,
    DescribeGlobalClustersMessageRequestTypeDef,
    DescribeIntegrationsMessageRequestTypeDef,
    DescribeIntegrationsResponseTypeDef,
    DescribeOptionGroupOptionsMessageRequestTypeDef,
    DescribeOptionGroupsMessageRequestTypeDef,
    DescribeOrderableDBInstanceOptionsMessageRequestTypeDef,
    DescribePendingMaintenanceActionsMessageRequestTypeDef,
    DescribeReservedDBInstancesMessageRequestTypeDef,
    DescribeReservedDBInstancesOfferingsMessageRequestTypeDef,
    DescribeSourceRegionsMessageRequestTypeDef,
    DescribeTenantDatabasesMessageRequestTypeDef,
    DescribeValidDBInstanceModificationsMessageRequestTypeDef,
    DescribeValidDBInstanceModificationsResultTypeDef,
    DisableHttpEndpointRequestRequestTypeDef,
    DisableHttpEndpointResponseTypeDef,
    DownloadDBLogFilePortionDetailsTypeDef,
    DownloadDBLogFilePortionMessageRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    EnableHttpEndpointRequestRequestTypeDef,
    EnableHttpEndpointResponseTypeDef,
    EventCategoriesMessageTypeDef,
    EventsMessageTypeDef,
    EventSubscriptionsMessageTypeDef,
    ExportTaskResponseTypeDef,
    ExportTasksMessageTypeDef,
    FailoverDBClusterMessageRequestTypeDef,
    FailoverDBClusterResultTypeDef,
    FailoverGlobalClusterMessageRequestTypeDef,
    FailoverGlobalClusterResultTypeDef,
    GlobalClustersMessageTypeDef,
    IntegrationResponseTypeDef,
    ListTagsForResourceMessageRequestTypeDef,
    ModifyActivityStreamRequestRequestTypeDef,
    ModifyActivityStreamResponseTypeDef,
    ModifyCertificatesMessageRequestTypeDef,
    ModifyCertificatesResultTypeDef,
    ModifyCurrentDBClusterCapacityMessageRequestTypeDef,
    ModifyCustomDBEngineVersionMessageRequestTypeDef,
    ModifyDBClusterEndpointMessageRequestTypeDef,
    ModifyDBClusterMessageRequestTypeDef,
    ModifyDBClusterParameterGroupMessageRequestTypeDef,
    ModifyDBClusterResultTypeDef,
    ModifyDBClusterSnapshotAttributeMessageRequestTypeDef,
    ModifyDBClusterSnapshotAttributeResultTypeDef,
    ModifyDBInstanceMessageRequestTypeDef,
    ModifyDBInstanceResultTypeDef,
    ModifyDBParameterGroupMessageRequestTypeDef,
    ModifyDBProxyEndpointRequestRequestTypeDef,
    ModifyDBProxyEndpointResponseTypeDef,
    ModifyDBProxyRequestRequestTypeDef,
    ModifyDBProxyResponseTypeDef,
    ModifyDBProxyTargetGroupRequestRequestTypeDef,
    ModifyDBProxyTargetGroupResponseTypeDef,
    ModifyDBRecommendationMessageRequestTypeDef,
    ModifyDBShardGroupMessageRequestTypeDef,
    ModifyDBSnapshotAttributeMessageRequestTypeDef,
    ModifyDBSnapshotAttributeResultTypeDef,
    ModifyDBSnapshotMessageRequestTypeDef,
    ModifyDBSnapshotResultTypeDef,
    ModifyDBSubnetGroupMessageRequestTypeDef,
    ModifyDBSubnetGroupResultTypeDef,
    ModifyEventSubscriptionMessageRequestTypeDef,
    ModifyEventSubscriptionResultTypeDef,
    ModifyGlobalClusterMessageRequestTypeDef,
    ModifyGlobalClusterResultTypeDef,
    ModifyIntegrationMessageRequestTypeDef,
    ModifyOptionGroupMessageRequestTypeDef,
    ModifyOptionGroupResultTypeDef,
    ModifyTenantDatabaseMessageRequestTypeDef,
    ModifyTenantDatabaseResultTypeDef,
    OptionGroupOptionsMessageTypeDef,
    OptionGroupsTypeDef,
    OrderableDBInstanceOptionsMessageTypeDef,
    PendingMaintenanceActionsMessageTypeDef,
    PromoteReadReplicaDBClusterMessageRequestTypeDef,
    PromoteReadReplicaDBClusterResultTypeDef,
    PromoteReadReplicaMessageRequestTypeDef,
    PromoteReadReplicaResultTypeDef,
    PurchaseReservedDBInstancesOfferingMessageRequestTypeDef,
    PurchaseReservedDBInstancesOfferingResultTypeDef,
    RebootDBClusterMessageRequestTypeDef,
    RebootDBClusterResultTypeDef,
    RebootDBInstanceMessageRequestTypeDef,
    RebootDBInstanceResultTypeDef,
    RebootDBShardGroupMessageRequestTypeDef,
    RegisterDBProxyTargetsRequestRequestTypeDef,
    RegisterDBProxyTargetsResponseTypeDef,
    RemoveFromGlobalClusterMessageRequestTypeDef,
    RemoveFromGlobalClusterResultTypeDef,
    RemoveRoleFromDBClusterMessageRequestTypeDef,
    RemoveRoleFromDBInstanceMessageRequestTypeDef,
    RemoveSourceIdentifierFromSubscriptionMessageRequestTypeDef,
    RemoveSourceIdentifierFromSubscriptionResultTypeDef,
    RemoveTagsFromResourceMessageRequestTypeDef,
    ReservedDBInstanceMessageTypeDef,
    ReservedDBInstancesOfferingMessageTypeDef,
    ResetDBClusterParameterGroupMessageRequestTypeDef,
    ResetDBParameterGroupMessageRequestTypeDef,
    RestoreDBClusterFromS3MessageRequestTypeDef,
    RestoreDBClusterFromS3ResultTypeDef,
    RestoreDBClusterFromSnapshotMessageRequestTypeDef,
    RestoreDBClusterFromSnapshotResultTypeDef,
    RestoreDBClusterToPointInTimeMessageRequestTypeDef,
    RestoreDBClusterToPointInTimeResultTypeDef,
    RestoreDBInstanceFromDBSnapshotMessageRequestTypeDef,
    RestoreDBInstanceFromDBSnapshotResultTypeDef,
    RestoreDBInstanceFromS3MessageRequestTypeDef,
    RestoreDBInstanceFromS3ResultTypeDef,
    RestoreDBInstanceToPointInTimeMessageRequestTypeDef,
    RestoreDBInstanceToPointInTimeResultTypeDef,
    RevokeDBSecurityGroupIngressMessageRequestTypeDef,
    RevokeDBSecurityGroupIngressResultTypeDef,
    SourceRegionMessageTypeDef,
    StartActivityStreamRequestRequestTypeDef,
    StartActivityStreamResponseTypeDef,
    StartDBClusterMessageRequestTypeDef,
    StartDBClusterResultTypeDef,
    StartDBInstanceAutomatedBackupsReplicationMessageRequestTypeDef,
    StartDBInstanceAutomatedBackupsReplicationResultTypeDef,
    StartDBInstanceMessageRequestTypeDef,
    StartDBInstanceResultTypeDef,
    StartExportTaskMessageRequestTypeDef,
    StopActivityStreamRequestRequestTypeDef,
    StopActivityStreamResponseTypeDef,
    StopDBClusterMessageRequestTypeDef,
    StopDBClusterResultTypeDef,
    StopDBInstanceAutomatedBackupsReplicationMessageRequestTypeDef,
    StopDBInstanceAutomatedBackupsReplicationResultTypeDef,
    StopDBInstanceMessageRequestTypeDef,
    StopDBInstanceResultTypeDef,
    SwitchoverBlueGreenDeploymentRequestRequestTypeDef,
    SwitchoverBlueGreenDeploymentResponseTypeDef,
    SwitchoverGlobalClusterMessageRequestTypeDef,
    SwitchoverGlobalClusterResultTypeDef,
    SwitchoverReadReplicaMessageRequestTypeDef,
    SwitchoverReadReplicaResultTypeDef,
    TagListMessageTypeDef,
    TenantDatabasesMessageTypeDef,
)
from .waiter import (
    DBClusterAvailableWaiter,
    DBClusterDeletedWaiter,
    DBClusterSnapshotAvailableWaiter,
    DBClusterSnapshotDeletedWaiter,
    DBInstanceAvailableWaiter,
    DBInstanceDeletedWaiter,
    DBSnapshotAvailableWaiter,
    DBSnapshotCompletedWaiter,
    DBSnapshotDeletedWaiter,
    TenantDatabaseAvailableWaiter,
    TenantDatabaseDeletedWaiter,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack


__all__ = ("RDSClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AuthorizationAlreadyExistsFault: Type[BotocoreClientError]
    AuthorizationNotFoundFault: Type[BotocoreClientError]
    AuthorizationQuotaExceededFault: Type[BotocoreClientError]
    BackupPolicyNotFoundFault: Type[BotocoreClientError]
    BlueGreenDeploymentAlreadyExistsFault: Type[BotocoreClientError]
    BlueGreenDeploymentNotFoundFault: Type[BotocoreClientError]
    CertificateNotFoundFault: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    CreateCustomDBEngineVersionFault: Type[BotocoreClientError]
    CustomAvailabilityZoneNotFoundFault: Type[BotocoreClientError]
    CustomDBEngineVersionAlreadyExistsFault: Type[BotocoreClientError]
    CustomDBEngineVersionNotFoundFault: Type[BotocoreClientError]
    CustomDBEngineVersionQuotaExceededFault: Type[BotocoreClientError]
    DBClusterAlreadyExistsFault: Type[BotocoreClientError]
    DBClusterAutomatedBackupNotFoundFault: Type[BotocoreClientError]
    DBClusterAutomatedBackupQuotaExceededFault: Type[BotocoreClientError]
    DBClusterBacktrackNotFoundFault: Type[BotocoreClientError]
    DBClusterEndpointAlreadyExistsFault: Type[BotocoreClientError]
    DBClusterEndpointNotFoundFault: Type[BotocoreClientError]
    DBClusterEndpointQuotaExceededFault: Type[BotocoreClientError]
    DBClusterNotFoundFault: Type[BotocoreClientError]
    DBClusterParameterGroupNotFoundFault: Type[BotocoreClientError]
    DBClusterQuotaExceededFault: Type[BotocoreClientError]
    DBClusterRoleAlreadyExistsFault: Type[BotocoreClientError]
    DBClusterRoleNotFoundFault: Type[BotocoreClientError]
    DBClusterRoleQuotaExceededFault: Type[BotocoreClientError]
    DBClusterSnapshotAlreadyExistsFault: Type[BotocoreClientError]
    DBClusterSnapshotNotFoundFault: Type[BotocoreClientError]
    DBInstanceAlreadyExistsFault: Type[BotocoreClientError]
    DBInstanceAutomatedBackupNotFoundFault: Type[BotocoreClientError]
    DBInstanceAutomatedBackupQuotaExceededFault: Type[BotocoreClientError]
    DBInstanceNotFoundFault: Type[BotocoreClientError]
    DBInstanceRoleAlreadyExistsFault: Type[BotocoreClientError]
    DBInstanceRoleNotFoundFault: Type[BotocoreClientError]
    DBInstanceRoleQuotaExceededFault: Type[BotocoreClientError]
    DBLogFileNotFoundFault: Type[BotocoreClientError]
    DBParameterGroupAlreadyExistsFault: Type[BotocoreClientError]
    DBParameterGroupNotFoundFault: Type[BotocoreClientError]
    DBParameterGroupQuotaExceededFault: Type[BotocoreClientError]
    DBProxyAlreadyExistsFault: Type[BotocoreClientError]
    DBProxyEndpointAlreadyExistsFault: Type[BotocoreClientError]
    DBProxyEndpointNotFoundFault: Type[BotocoreClientError]
    DBProxyEndpointQuotaExceededFault: Type[BotocoreClientError]
    DBProxyNotFoundFault: Type[BotocoreClientError]
    DBProxyQuotaExceededFault: Type[BotocoreClientError]
    DBProxyTargetAlreadyRegisteredFault: Type[BotocoreClientError]
    DBProxyTargetGroupNotFoundFault: Type[BotocoreClientError]
    DBProxyTargetNotFoundFault: Type[BotocoreClientError]
    DBSecurityGroupAlreadyExistsFault: Type[BotocoreClientError]
    DBSecurityGroupNotFoundFault: Type[BotocoreClientError]
    DBSecurityGroupNotSupportedFault: Type[BotocoreClientError]
    DBSecurityGroupQuotaExceededFault: Type[BotocoreClientError]
    DBShardGroupAlreadyExistsFault: Type[BotocoreClientError]
    DBShardGroupNotFoundFault: Type[BotocoreClientError]
    DBSnapshotAlreadyExistsFault: Type[BotocoreClientError]
    DBSnapshotNotFoundFault: Type[BotocoreClientError]
    DBSnapshotTenantDatabaseNotFoundFault: Type[BotocoreClientError]
    DBSubnetGroupAlreadyExistsFault: Type[BotocoreClientError]
    DBSubnetGroupDoesNotCoverEnoughAZs: Type[BotocoreClientError]
    DBSubnetGroupNotAllowedFault: Type[BotocoreClientError]
    DBSubnetGroupNotFoundFault: Type[BotocoreClientError]
    DBSubnetGroupQuotaExceededFault: Type[BotocoreClientError]
    DBSubnetQuotaExceededFault: Type[BotocoreClientError]
    DBUpgradeDependencyFailureFault: Type[BotocoreClientError]
    DomainNotFoundFault: Type[BotocoreClientError]
    Ec2ImagePropertiesNotSupportedFault: Type[BotocoreClientError]
    EventSubscriptionQuotaExceededFault: Type[BotocoreClientError]
    ExportTaskAlreadyExistsFault: Type[BotocoreClientError]
    ExportTaskNotFoundFault: Type[BotocoreClientError]
    GlobalClusterAlreadyExistsFault: Type[BotocoreClientError]
    GlobalClusterNotFoundFault: Type[BotocoreClientError]
    GlobalClusterQuotaExceededFault: Type[BotocoreClientError]
    IamRoleMissingPermissionsFault: Type[BotocoreClientError]
    IamRoleNotFoundFault: Type[BotocoreClientError]
    InstanceQuotaExceededFault: Type[BotocoreClientError]
    InsufficientAvailableIPsInSubnetFault: Type[BotocoreClientError]
    InsufficientDBClusterCapacityFault: Type[BotocoreClientError]
    InsufficientDBInstanceCapacityFault: Type[BotocoreClientError]
    InsufficientStorageClusterCapacityFault: Type[BotocoreClientError]
    IntegrationAlreadyExistsFault: Type[BotocoreClientError]
    IntegrationConflictOperationFault: Type[BotocoreClientError]
    IntegrationNotFoundFault: Type[BotocoreClientError]
    IntegrationQuotaExceededFault: Type[BotocoreClientError]
    InvalidBlueGreenDeploymentStateFault: Type[BotocoreClientError]
    InvalidCustomDBEngineVersionStateFault: Type[BotocoreClientError]
    InvalidDBClusterAutomatedBackupStateFault: Type[BotocoreClientError]
    InvalidDBClusterCapacityFault: Type[BotocoreClientError]
    InvalidDBClusterEndpointStateFault: Type[BotocoreClientError]
    InvalidDBClusterSnapshotStateFault: Type[BotocoreClientError]
    InvalidDBClusterStateFault: Type[BotocoreClientError]
    InvalidDBInstanceAutomatedBackupStateFault: Type[BotocoreClientError]
    InvalidDBInstanceStateFault: Type[BotocoreClientError]
    InvalidDBParameterGroupStateFault: Type[BotocoreClientError]
    InvalidDBProxyEndpointStateFault: Type[BotocoreClientError]
    InvalidDBProxyStateFault: Type[BotocoreClientError]
    InvalidDBSecurityGroupStateFault: Type[BotocoreClientError]
    InvalidDBShardGroupStateFault: Type[BotocoreClientError]
    InvalidDBSnapshotStateFault: Type[BotocoreClientError]
    InvalidDBSubnetGroupFault: Type[BotocoreClientError]
    InvalidDBSubnetGroupStateFault: Type[BotocoreClientError]
    InvalidDBSubnetStateFault: Type[BotocoreClientError]
    InvalidEventSubscriptionStateFault: Type[BotocoreClientError]
    InvalidExportOnlyFault: Type[BotocoreClientError]
    InvalidExportSourceStateFault: Type[BotocoreClientError]
    InvalidExportTaskStateFault: Type[BotocoreClientError]
    InvalidGlobalClusterStateFault: Type[BotocoreClientError]
    InvalidIntegrationStateFault: Type[BotocoreClientError]
    InvalidOptionGroupStateFault: Type[BotocoreClientError]
    InvalidResourceStateFault: Type[BotocoreClientError]
    InvalidRestoreFault: Type[BotocoreClientError]
    InvalidS3BucketFault: Type[BotocoreClientError]
    InvalidSubnet: Type[BotocoreClientError]
    InvalidVPCNetworkStateFault: Type[BotocoreClientError]
    KMSKeyNotAccessibleFault: Type[BotocoreClientError]
    MaxDBShardGroupLimitReached: Type[BotocoreClientError]
    NetworkTypeNotSupported: Type[BotocoreClientError]
    OptionGroupAlreadyExistsFault: Type[BotocoreClientError]
    OptionGroupNotFoundFault: Type[BotocoreClientError]
    OptionGroupQuotaExceededFault: Type[BotocoreClientError]
    PointInTimeRestoreNotEnabledFault: Type[BotocoreClientError]
    ProvisionedIopsNotAvailableInAZFault: Type[BotocoreClientError]
    ReservedDBInstanceAlreadyExistsFault: Type[BotocoreClientError]
    ReservedDBInstanceNotFoundFault: Type[BotocoreClientError]
    ReservedDBInstanceQuotaExceededFault: Type[BotocoreClientError]
    ReservedDBInstancesOfferingNotFoundFault: Type[BotocoreClientError]
    ResourceNotFoundFault: Type[BotocoreClientError]
    SNSInvalidTopicFault: Type[BotocoreClientError]
    SNSNoAuthorizationFault: Type[BotocoreClientError]
    SNSTopicArnNotFoundFault: Type[BotocoreClientError]
    SharedSnapshotQuotaExceededFault: Type[BotocoreClientError]
    SnapshotQuotaExceededFault: Type[BotocoreClientError]
    SourceClusterNotSupportedFault: Type[BotocoreClientError]
    SourceDatabaseNotSupportedFault: Type[BotocoreClientError]
    SourceNotFoundFault: Type[BotocoreClientError]
    StorageQuotaExceededFault: Type[BotocoreClientError]
    StorageTypeNotAvailableFault: Type[BotocoreClientError]
    StorageTypeNotSupportedFault: Type[BotocoreClientError]
    SubnetAlreadyInUse: Type[BotocoreClientError]
    SubscriptionAlreadyExistFault: Type[BotocoreClientError]
    SubscriptionCategoryNotFoundFault: Type[BotocoreClientError]
    SubscriptionNotFoundFault: Type[BotocoreClientError]
    TenantDatabaseAlreadyExistsFault: Type[BotocoreClientError]
    TenantDatabaseNotFoundFault: Type[BotocoreClientError]
    TenantDatabaseQuotaExceededFault: Type[BotocoreClientError]
    UnsupportedDBEngineVersionFault: Type[BotocoreClientError]


class RDSClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        RDSClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#exceptions)
        """

    def add_role_to_db_cluster(
        self, **kwargs: Unpack[AddRoleToDBClusterMessageRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Associates an Identity and Access Management (IAM) role with a DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.add_role_to_db_cluster)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#add_role_to_db_cluster)
        """

    def add_role_to_db_instance(
        self, **kwargs: Unpack[AddRoleToDBInstanceMessageRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Associates an Amazon Web Services Identity and Access Management (IAM) role
        with a DB
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.add_role_to_db_instance)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#add_role_to_db_instance)
        """

    def add_source_identifier_to_subscription(
        self, **kwargs: Unpack[AddSourceIdentifierToSubscriptionMessageRequestTypeDef]
    ) -> AddSourceIdentifierToSubscriptionResultTypeDef:
        """
        Adds a source identifier to an existing RDS event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.add_source_identifier_to_subscription)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#add_source_identifier_to_subscription)
        """

    def add_tags_to_resource(
        self, **kwargs: Unpack[AddTagsToResourceMessageRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds metadata tags to an Amazon RDS resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.add_tags_to_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#add_tags_to_resource)
        """

    def apply_pending_maintenance_action(
        self, **kwargs: Unpack[ApplyPendingMaintenanceActionMessageRequestTypeDef]
    ) -> ApplyPendingMaintenanceActionResultTypeDef:
        """
        Applies a pending maintenance action to a resource (for example, to a DB
        instance).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.apply_pending_maintenance_action)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#apply_pending_maintenance_action)
        """

    def authorize_db_security_group_ingress(
        self, **kwargs: Unpack[AuthorizeDBSecurityGroupIngressMessageRequestTypeDef]
    ) -> AuthorizeDBSecurityGroupIngressResultTypeDef:
        """
        Enables ingress to a DBSecurityGroup using one of two forms of authorization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.authorize_db_security_group_ingress)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#authorize_db_security_group_ingress)
        """

    def backtrack_db_cluster(
        self, **kwargs: Unpack[BacktrackDBClusterMessageRequestTypeDef]
    ) -> DBClusterBacktrackResponseTypeDef:
        """
        Backtracks a DB cluster to a specific time, without creating a new DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.backtrack_db_cluster)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#backtrack_db_cluster)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#can_paginate)
        """

    def cancel_export_task(
        self, **kwargs: Unpack[CancelExportTaskMessageRequestTypeDef]
    ) -> ExportTaskResponseTypeDef:
        """
        Cancels an export task in progress that is exporting a snapshot or cluster to
        Amazon
        S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.cancel_export_task)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#cancel_export_task)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#close)
        """

    def copy_db_cluster_parameter_group(
        self, **kwargs: Unpack[CopyDBClusterParameterGroupMessageRequestTypeDef]
    ) -> CopyDBClusterParameterGroupResultTypeDef:
        """
        Copies the specified DB cluster parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.copy_db_cluster_parameter_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#copy_db_cluster_parameter_group)
        """

    def copy_db_cluster_snapshot(
        self, **kwargs: Unpack[CopyDBClusterSnapshotMessageRequestTypeDef]
    ) -> CopyDBClusterSnapshotResultTypeDef:
        """
        Copies a snapshot of a DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.copy_db_cluster_snapshot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#copy_db_cluster_snapshot)
        """

    def copy_db_parameter_group(
        self, **kwargs: Unpack[CopyDBParameterGroupMessageRequestTypeDef]
    ) -> CopyDBParameterGroupResultTypeDef:
        """
        Copies the specified DB parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.copy_db_parameter_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#copy_db_parameter_group)
        """

    def copy_db_snapshot(
        self, **kwargs: Unpack[CopyDBSnapshotMessageRequestTypeDef]
    ) -> CopyDBSnapshotResultTypeDef:
        """
        Copies the specified DB snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.copy_db_snapshot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#copy_db_snapshot)
        """

    def copy_option_group(
        self, **kwargs: Unpack[CopyOptionGroupMessageRequestTypeDef]
    ) -> CopyOptionGroupResultTypeDef:
        """
        Copies the specified option group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.copy_option_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#copy_option_group)
        """

    def create_blue_green_deployment(
        self, **kwargs: Unpack[CreateBlueGreenDeploymentRequestRequestTypeDef]
    ) -> CreateBlueGreenDeploymentResponseTypeDef:
        """
        Creates a blue/green deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_blue_green_deployment)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_blue_green_deployment)
        """

    def create_custom_db_engine_version(
        self, **kwargs: Unpack[CreateCustomDBEngineVersionMessageRequestTypeDef]
    ) -> DBEngineVersionResponseTypeDef:
        """
        Creates a custom DB engine version (CEV).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_custom_db_engine_version)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_custom_db_engine_version)
        """

    def create_db_cluster(
        self, **kwargs: Unpack[CreateDBClusterMessageRequestTypeDef]
    ) -> CreateDBClusterResultTypeDef:
        """
        Creates a new Amazon Aurora DB cluster or Multi-AZ DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_cluster)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_cluster)
        """

    def create_db_cluster_endpoint(
        self, **kwargs: Unpack[CreateDBClusterEndpointMessageRequestTypeDef]
    ) -> DBClusterEndpointResponseTypeDef:
        """
        Creates a new custom endpoint and associates it with an Amazon Aurora DB
        cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_cluster_endpoint)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_cluster_endpoint)
        """

    def create_db_cluster_parameter_group(
        self, **kwargs: Unpack[CreateDBClusterParameterGroupMessageRequestTypeDef]
    ) -> CreateDBClusterParameterGroupResultTypeDef:
        """
        Creates a new DB cluster parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_cluster_parameter_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_cluster_parameter_group)
        """

    def create_db_cluster_snapshot(
        self, **kwargs: Unpack[CreateDBClusterSnapshotMessageRequestTypeDef]
    ) -> CreateDBClusterSnapshotResultTypeDef:
        """
        Creates a snapshot of a DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_cluster_snapshot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_cluster_snapshot)
        """

    def create_db_instance(
        self, **kwargs: Unpack[CreateDBInstanceMessageRequestTypeDef]
    ) -> CreateDBInstanceResultTypeDef:
        """
        Creates a new DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_instance)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_instance)
        """

    def create_db_instance_read_replica(
        self, **kwargs: Unpack[CreateDBInstanceReadReplicaMessageRequestTypeDef]
    ) -> CreateDBInstanceReadReplicaResultTypeDef:
        """
        Creates a new DB instance that acts as a read replica for an existing source DB
        instance or Multi-AZ DB
        cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_instance_read_replica)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_instance_read_replica)
        """

    def create_db_parameter_group(
        self, **kwargs: Unpack[CreateDBParameterGroupMessageRequestTypeDef]
    ) -> CreateDBParameterGroupResultTypeDef:
        """
        Creates a new DB parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_parameter_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_parameter_group)
        """

    def create_db_proxy(
        self, **kwargs: Unpack[CreateDBProxyRequestRequestTypeDef]
    ) -> CreateDBProxyResponseTypeDef:
        """
        Creates a new DB proxy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_proxy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_proxy)
        """

    def create_db_proxy_endpoint(
        self, **kwargs: Unpack[CreateDBProxyEndpointRequestRequestTypeDef]
    ) -> CreateDBProxyEndpointResponseTypeDef:
        """
        Creates a `DBProxyEndpoint`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_proxy_endpoint)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_proxy_endpoint)
        """

    def create_db_security_group(
        self, **kwargs: Unpack[CreateDBSecurityGroupMessageRequestTypeDef]
    ) -> CreateDBSecurityGroupResultTypeDef:
        """
        Creates a new DB security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_security_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_security_group)
        """

    def create_db_shard_group(
        self, **kwargs: Unpack[CreateDBShardGroupMessageRequestTypeDef]
    ) -> DBShardGroupResponseTypeDef:
        """
        Creates a new DB shard group for Aurora Limitless Database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_shard_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_shard_group)
        """

    def create_db_snapshot(
        self, **kwargs: Unpack[CreateDBSnapshotMessageRequestTypeDef]
    ) -> CreateDBSnapshotResultTypeDef:
        """
        Creates a snapshot of a DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_snapshot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_snapshot)
        """

    def create_db_subnet_group(
        self, **kwargs: Unpack[CreateDBSubnetGroupMessageRequestTypeDef]
    ) -> CreateDBSubnetGroupResultTypeDef:
        """
        Creates a new DB subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_db_subnet_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_db_subnet_group)
        """

    def create_event_subscription(
        self, **kwargs: Unpack[CreateEventSubscriptionMessageRequestTypeDef]
    ) -> CreateEventSubscriptionResultTypeDef:
        """
        Creates an RDS event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_event_subscription)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_event_subscription)
        """

    def create_global_cluster(
        self, **kwargs: Unpack[CreateGlobalClusterMessageRequestTypeDef]
    ) -> CreateGlobalClusterResultTypeDef:
        """
        Creates an Aurora global database spread across multiple Amazon Web Services
        Regions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_global_cluster)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_global_cluster)
        """

    def create_integration(
        self, **kwargs: Unpack[CreateIntegrationMessageRequestTypeDef]
    ) -> IntegrationResponseTypeDef:
        """
        Creates a zero-ETL integration with Amazon Redshift.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_integration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_integration)
        """

    def create_option_group(
        self, **kwargs: Unpack[CreateOptionGroupMessageRequestTypeDef]
    ) -> CreateOptionGroupResultTypeDef:
        """
        Creates a new option group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_option_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_option_group)
        """

    def create_tenant_database(
        self, **kwargs: Unpack[CreateTenantDatabaseMessageRequestTypeDef]
    ) -> CreateTenantDatabaseResultTypeDef:
        """
        Creates a tenant database in a DB instance that uses the multi-tenant
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.create_tenant_database)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#create_tenant_database)
        """

    def delete_blue_green_deployment(
        self, **kwargs: Unpack[DeleteBlueGreenDeploymentRequestRequestTypeDef]
    ) -> DeleteBlueGreenDeploymentResponseTypeDef:
        """
        Deletes a blue/green deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_blue_green_deployment)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_blue_green_deployment)
        """

    def delete_custom_db_engine_version(
        self, **kwargs: Unpack[DeleteCustomDBEngineVersionMessageRequestTypeDef]
    ) -> DBEngineVersionResponseTypeDef:
        """
        Deletes a custom engine version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_custom_db_engine_version)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_custom_db_engine_version)
        """

    def delete_db_cluster(
        self, **kwargs: Unpack[DeleteDBClusterMessageRequestTypeDef]
    ) -> DeleteDBClusterResultTypeDef:
        """
        The DeleteDBCluster action deletes a previously provisioned DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_cluster)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_cluster)
        """

    def delete_db_cluster_automated_backup(
        self, **kwargs: Unpack[DeleteDBClusterAutomatedBackupMessageRequestTypeDef]
    ) -> DeleteDBClusterAutomatedBackupResultTypeDef:
        """
        Deletes automated backups using the `DbClusterResourceId` value of the source
        DB cluster or the Amazon Resource Name (ARN) of the automated
        backups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_cluster_automated_backup)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_cluster_automated_backup)
        """

    def delete_db_cluster_endpoint(
        self, **kwargs: Unpack[DeleteDBClusterEndpointMessageRequestTypeDef]
    ) -> DBClusterEndpointResponseTypeDef:
        """
        Deletes a custom endpoint and removes it from an Amazon Aurora DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_cluster_endpoint)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_cluster_endpoint)
        """

    def delete_db_cluster_parameter_group(
        self, **kwargs: Unpack[DeleteDBClusterParameterGroupMessageRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a specified DB cluster parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_cluster_parameter_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_cluster_parameter_group)
        """

    def delete_db_cluster_snapshot(
        self, **kwargs: Unpack[DeleteDBClusterSnapshotMessageRequestTypeDef]
    ) -> DeleteDBClusterSnapshotResultTypeDef:
        """
        Deletes a DB cluster snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_cluster_snapshot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_cluster_snapshot)
        """

    def delete_db_instance(
        self, **kwargs: Unpack[DeleteDBInstanceMessageRequestTypeDef]
    ) -> DeleteDBInstanceResultTypeDef:
        """
        Deletes a previously provisioned DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_instance)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_instance)
        """

    def delete_db_instance_automated_backup(
        self, **kwargs: Unpack[DeleteDBInstanceAutomatedBackupMessageRequestTypeDef]
    ) -> DeleteDBInstanceAutomatedBackupResultTypeDef:
        """
        Deletes automated backups using the `DbiResourceId` value of the source DB
        instance or the Amazon Resource Name (ARN) of the automated
        backups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_instance_automated_backup)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_instance_automated_backup)
        """

    def delete_db_parameter_group(
        self, **kwargs: Unpack[DeleteDBParameterGroupMessageRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a specified DB parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_parameter_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_parameter_group)
        """

    def delete_db_proxy(
        self, **kwargs: Unpack[DeleteDBProxyRequestRequestTypeDef]
    ) -> DeleteDBProxyResponseTypeDef:
        """
        Deletes an existing DB proxy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_proxy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_proxy)
        """

    def delete_db_proxy_endpoint(
        self, **kwargs: Unpack[DeleteDBProxyEndpointRequestRequestTypeDef]
    ) -> DeleteDBProxyEndpointResponseTypeDef:
        """
        Deletes a `DBProxyEndpoint`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_proxy_endpoint)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_proxy_endpoint)
        """

    def delete_db_security_group(
        self, **kwargs: Unpack[DeleteDBSecurityGroupMessageRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a DB security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_security_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_security_group)
        """

    def delete_db_shard_group(
        self, **kwargs: Unpack[DeleteDBShardGroupMessageRequestTypeDef]
    ) -> DBShardGroupResponseTypeDef:
        """
        Deletes an Aurora Limitless Database DB shard group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_shard_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_shard_group)
        """

    def delete_db_snapshot(
        self, **kwargs: Unpack[DeleteDBSnapshotMessageRequestTypeDef]
    ) -> DeleteDBSnapshotResultTypeDef:
        """
        Deletes a DB snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_snapshot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_snapshot)
        """

    def delete_db_subnet_group(
        self, **kwargs: Unpack[DeleteDBSubnetGroupMessageRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a DB subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_db_subnet_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_db_subnet_group)
        """

    def delete_event_subscription(
        self, **kwargs: Unpack[DeleteEventSubscriptionMessageRequestTypeDef]
    ) -> DeleteEventSubscriptionResultTypeDef:
        """
        Deletes an RDS event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_event_subscription)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_event_subscription)
        """

    def delete_global_cluster(
        self, **kwargs: Unpack[DeleteGlobalClusterMessageRequestTypeDef]
    ) -> DeleteGlobalClusterResultTypeDef:
        """
        Deletes a global database cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_global_cluster)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_global_cluster)
        """

    def delete_integration(
        self, **kwargs: Unpack[DeleteIntegrationMessageRequestTypeDef]
    ) -> IntegrationResponseTypeDef:
        """
        Deletes a zero-ETL integration with Amazon Redshift.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_integration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_integration)
        """

    def delete_option_group(
        self, **kwargs: Unpack[DeleteOptionGroupMessageRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an existing option group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_option_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_option_group)
        """

    def delete_tenant_database(
        self, **kwargs: Unpack[DeleteTenantDatabaseMessageRequestTypeDef]
    ) -> DeleteTenantDatabaseResultTypeDef:
        """
        Deletes a tenant database from your DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.delete_tenant_database)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#delete_tenant_database)
        """

    def deregister_db_proxy_targets(
        self, **kwargs: Unpack[DeregisterDBProxyTargetsRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Remove the association between one or more `DBProxyTarget` data structures and
        a
        `DBProxyTargetGroup`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.deregister_db_proxy_targets)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#deregister_db_proxy_targets)
        """

    def describe_account_attributes(self) -> AccountAttributesMessageTypeDef:
        """
        Lists all of the attributes for a customer account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_account_attributes)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_account_attributes)
        """

    def describe_blue_green_deployments(
        self, **kwargs: Unpack[DescribeBlueGreenDeploymentsRequestRequestTypeDef]
    ) -> DescribeBlueGreenDeploymentsResponseTypeDef:
        """
        Describes one or more blue/green deployments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_blue_green_deployments)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_blue_green_deployments)
        """

    def describe_certificates(
        self, **kwargs: Unpack[DescribeCertificatesMessageRequestTypeDef]
    ) -> CertificateMessageTypeDef:
        """
        Lists the set of certificate authority (CA) certificates provided by Amazon RDS
        for this Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_certificates)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_certificates)
        """

    def describe_db_cluster_automated_backups(
        self, **kwargs: Unpack[DescribeDBClusterAutomatedBackupsMessageRequestTypeDef]
    ) -> DBClusterAutomatedBackupMessageTypeDef:
        """
        Displays backups for both current and deleted DB clusters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_cluster_automated_backups)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_cluster_automated_backups)
        """

    def describe_db_cluster_backtracks(
        self, **kwargs: Unpack[DescribeDBClusterBacktracksMessageRequestTypeDef]
    ) -> DBClusterBacktrackMessageTypeDef:
        """
        Returns information about backtracks for a DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_cluster_backtracks)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_cluster_backtracks)
        """

    def describe_db_cluster_endpoints(
        self, **kwargs: Unpack[DescribeDBClusterEndpointsMessageRequestTypeDef]
    ) -> DBClusterEndpointMessageTypeDef:
        """
        Returns information about endpoints for an Amazon Aurora DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_cluster_endpoints)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_cluster_endpoints)
        """

    def describe_db_cluster_parameter_groups(
        self, **kwargs: Unpack[DescribeDBClusterParameterGroupsMessageRequestTypeDef]
    ) -> DBClusterParameterGroupsMessageTypeDef:
        """
        Returns a list of `DBClusterParameterGroup` descriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_cluster_parameter_groups)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_cluster_parameter_groups)
        """

    def describe_db_cluster_parameters(
        self, **kwargs: Unpack[DescribeDBClusterParametersMessageRequestTypeDef]
    ) -> DBClusterParameterGroupDetailsTypeDef:
        """
        Returns the detailed parameter list for a particular DB cluster parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_cluster_parameters)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_cluster_parameters)
        """

    def describe_db_cluster_snapshot_attributes(
        self, **kwargs: Unpack[DescribeDBClusterSnapshotAttributesMessageRequestTypeDef]
    ) -> DescribeDBClusterSnapshotAttributesResultTypeDef:
        """
        Returns a list of DB cluster snapshot attribute names and values for a manual
        DB cluster
        snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_cluster_snapshot_attributes)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_cluster_snapshot_attributes)
        """

    def describe_db_cluster_snapshots(
        self, **kwargs: Unpack[DescribeDBClusterSnapshotsMessageRequestTypeDef]
    ) -> DBClusterSnapshotMessageTypeDef:
        """
        Returns information about DB cluster snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_cluster_snapshots)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_cluster_snapshots)
        """

    def describe_db_clusters(
        self, **kwargs: Unpack[DescribeDBClustersMessageRequestTypeDef]
    ) -> DBClusterMessageTypeDef:
        """
        Describes existing Amazon Aurora DB clusters and Multi-AZ DB clusters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_clusters)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_clusters)
        """

    def describe_db_engine_versions(
        self, **kwargs: Unpack[DescribeDBEngineVersionsMessageRequestTypeDef]
    ) -> DBEngineVersionMessageTypeDef:
        """
        Describes the properties of specific versions of DB engines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_engine_versions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_engine_versions)
        """

    def describe_db_instance_automated_backups(
        self, **kwargs: Unpack[DescribeDBInstanceAutomatedBackupsMessageRequestTypeDef]
    ) -> DBInstanceAutomatedBackupMessageTypeDef:
        """
        Displays backups for both current and deleted instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_instance_automated_backups)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_instance_automated_backups)
        """

    def describe_db_instances(
        self, **kwargs: Unpack[DescribeDBInstancesMessageRequestTypeDef]
    ) -> DBInstanceMessageTypeDef:
        """
        Describes provisioned RDS instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_instances)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_instances)
        """

    def describe_db_log_files(
        self, **kwargs: Unpack[DescribeDBLogFilesMessageRequestTypeDef]
    ) -> DescribeDBLogFilesResponseTypeDef:
        """
        Returns a list of DB log files for the DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_log_files)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_log_files)
        """

    def describe_db_parameter_groups(
        self, **kwargs: Unpack[DescribeDBParameterGroupsMessageRequestTypeDef]
    ) -> DBParameterGroupsMessageTypeDef:
        """
        Returns a list of `DBParameterGroup` descriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_parameter_groups)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_parameter_groups)
        """

    def describe_db_parameters(
        self, **kwargs: Unpack[DescribeDBParametersMessageRequestTypeDef]
    ) -> DBParameterGroupDetailsTypeDef:
        """
        Returns the detailed parameter list for a particular DB parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_parameters)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_parameters)
        """

    def describe_db_proxies(
        self, **kwargs: Unpack[DescribeDBProxiesRequestRequestTypeDef]
    ) -> DescribeDBProxiesResponseTypeDef:
        """
        Returns information about DB proxies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_proxies)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_proxies)
        """

    def describe_db_proxy_endpoints(
        self, **kwargs: Unpack[DescribeDBProxyEndpointsRequestRequestTypeDef]
    ) -> DescribeDBProxyEndpointsResponseTypeDef:
        """
        Returns information about DB proxy endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_proxy_endpoints)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_proxy_endpoints)
        """

    def describe_db_proxy_target_groups(
        self, **kwargs: Unpack[DescribeDBProxyTargetGroupsRequestRequestTypeDef]
    ) -> DescribeDBProxyTargetGroupsResponseTypeDef:
        """
        Returns information about DB proxy target groups, represented by
        `DBProxyTargetGroup` data
        structures.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_proxy_target_groups)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_proxy_target_groups)
        """

    def describe_db_proxy_targets(
        self, **kwargs: Unpack[DescribeDBProxyTargetsRequestRequestTypeDef]
    ) -> DescribeDBProxyTargetsResponseTypeDef:
        """
        Returns information about `DBProxyTarget` objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_proxy_targets)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_proxy_targets)
        """

    def describe_db_recommendations(
        self, **kwargs: Unpack[DescribeDBRecommendationsMessageRequestTypeDef]
    ) -> DBRecommendationsMessageTypeDef:
        """
        Describes the recommendations to resolve the issues for your DB instances, DB
        clusters, and DB parameter
        groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_recommendations)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_recommendations)
        """

    def describe_db_security_groups(
        self, **kwargs: Unpack[DescribeDBSecurityGroupsMessageRequestTypeDef]
    ) -> DBSecurityGroupMessageTypeDef:
        """
        Returns a list of `DBSecurityGroup` descriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_security_groups)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_security_groups)
        """

    def describe_db_shard_groups(
        self, **kwargs: Unpack[DescribeDBShardGroupsMessageRequestTypeDef]
    ) -> DescribeDBShardGroupsResponseTypeDef:
        """
        Describes existing Aurora Limitless Database DB shard groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_shard_groups)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_shard_groups)
        """

    def describe_db_snapshot_attributes(
        self, **kwargs: Unpack[DescribeDBSnapshotAttributesMessageRequestTypeDef]
    ) -> DescribeDBSnapshotAttributesResultTypeDef:
        """
        Returns a list of DB snapshot attribute names and values for a manual DB
        snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_snapshot_attributes)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_snapshot_attributes)
        """

    def describe_db_snapshot_tenant_databases(
        self, **kwargs: Unpack[DescribeDBSnapshotTenantDatabasesMessageRequestTypeDef]
    ) -> DBSnapshotTenantDatabasesMessageTypeDef:
        """
        Describes the tenant databases that exist in a DB snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_snapshot_tenant_databases)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_snapshot_tenant_databases)
        """

    def describe_db_snapshots(
        self, **kwargs: Unpack[DescribeDBSnapshotsMessageRequestTypeDef]
    ) -> DBSnapshotMessageTypeDef:
        """
        Returns information about DB snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_snapshots)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_snapshots)
        """

    def describe_db_subnet_groups(
        self, **kwargs: Unpack[DescribeDBSubnetGroupsMessageRequestTypeDef]
    ) -> DBSubnetGroupMessageTypeDef:
        """
        Returns a list of DBSubnetGroup descriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_subnet_groups)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_db_subnet_groups)
        """

    def describe_engine_default_cluster_parameters(
        self, **kwargs: Unpack[DescribeEngineDefaultClusterParametersMessageRequestTypeDef]
    ) -> DescribeEngineDefaultClusterParametersResultTypeDef:
        """
        Returns the default engine and system parameter information for the cluster
        database
        engine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_engine_default_cluster_parameters)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_engine_default_cluster_parameters)
        """

    def describe_engine_default_parameters(
        self, **kwargs: Unpack[DescribeEngineDefaultParametersMessageRequestTypeDef]
    ) -> DescribeEngineDefaultParametersResultTypeDef:
        """
        Returns the default engine and system parameter information for the specified
        database
        engine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_engine_default_parameters)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_engine_default_parameters)
        """

    def describe_event_categories(
        self, **kwargs: Unpack[DescribeEventCategoriesMessageRequestTypeDef]
    ) -> EventCategoriesMessageTypeDef:
        """
        Displays a list of categories for all event source types, or, if specified, for
        a specified source
        type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_event_categories)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_event_categories)
        """

    def describe_event_subscriptions(
        self, **kwargs: Unpack[DescribeEventSubscriptionsMessageRequestTypeDef]
    ) -> EventSubscriptionsMessageTypeDef:
        """
        Lists all the subscription descriptions for a customer account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_event_subscriptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_event_subscriptions)
        """

    def describe_events(
        self, **kwargs: Unpack[DescribeEventsMessageRequestTypeDef]
    ) -> EventsMessageTypeDef:
        """
        Returns events related to DB instances, DB clusters, DB parameter groups, DB
        security groups, DB snapshots, DB cluster snapshots, and RDS Proxies for the
        past 14
        days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_events)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_events)
        """

    def describe_export_tasks(
        self, **kwargs: Unpack[DescribeExportTasksMessageRequestTypeDef]
    ) -> ExportTasksMessageTypeDef:
        """
        Returns information about a snapshot or cluster export to Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_export_tasks)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_export_tasks)
        """

    def describe_global_clusters(
        self, **kwargs: Unpack[DescribeGlobalClustersMessageRequestTypeDef]
    ) -> GlobalClustersMessageTypeDef:
        """
        Returns information about Aurora global database clusters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_global_clusters)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_global_clusters)
        """

    def describe_integrations(
        self, **kwargs: Unpack[DescribeIntegrationsMessageRequestTypeDef]
    ) -> DescribeIntegrationsResponseTypeDef:
        """
        Describe one or more zero-ETL integrations with Amazon Redshift.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_integrations)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_integrations)
        """

    def describe_option_group_options(
        self, **kwargs: Unpack[DescribeOptionGroupOptionsMessageRequestTypeDef]
    ) -> OptionGroupOptionsMessageTypeDef:
        """
        Describes all available options for the specified engine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_option_group_options)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_option_group_options)
        """

    def describe_option_groups(
        self, **kwargs: Unpack[DescribeOptionGroupsMessageRequestTypeDef]
    ) -> OptionGroupsTypeDef:
        """
        Describes the available option groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_option_groups)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_option_groups)
        """

    def describe_orderable_db_instance_options(
        self, **kwargs: Unpack[DescribeOrderableDBInstanceOptionsMessageRequestTypeDef]
    ) -> OrderableDBInstanceOptionsMessageTypeDef:
        """
        Describes the orderable DB instance options for a specified DB engine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_orderable_db_instance_options)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_orderable_db_instance_options)
        """

    def describe_pending_maintenance_actions(
        self, **kwargs: Unpack[DescribePendingMaintenanceActionsMessageRequestTypeDef]
    ) -> PendingMaintenanceActionsMessageTypeDef:
        """
        Returns a list of resources (for example, DB instances) that have at least one
        pending maintenance
        action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_pending_maintenance_actions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_pending_maintenance_actions)
        """

    def describe_reserved_db_instances(
        self, **kwargs: Unpack[DescribeReservedDBInstancesMessageRequestTypeDef]
    ) -> ReservedDBInstanceMessageTypeDef:
        """
        Returns information about reserved DB instances for this account, or about a
        specified reserved DB
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_reserved_db_instances)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_reserved_db_instances)
        """

    def describe_reserved_db_instances_offerings(
        self, **kwargs: Unpack[DescribeReservedDBInstancesOfferingsMessageRequestTypeDef]
    ) -> ReservedDBInstancesOfferingMessageTypeDef:
        """
        Lists available reserved DB instance offerings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_reserved_db_instances_offerings)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_reserved_db_instances_offerings)
        """

    def describe_source_regions(
        self, **kwargs: Unpack[DescribeSourceRegionsMessageRequestTypeDef]
    ) -> SourceRegionMessageTypeDef:
        """
        Returns a list of the source Amazon Web Services Regions where the current
        Amazon Web Services Region can create a read replica, copy a DB snapshot from,
        or replicate automated backups
        from.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_source_regions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_source_regions)
        """

    def describe_tenant_databases(
        self, **kwargs: Unpack[DescribeTenantDatabasesMessageRequestTypeDef]
    ) -> TenantDatabasesMessageTypeDef:
        """
        Describes the tenant databases in a DB instance that uses the multi-tenant
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_tenant_databases)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_tenant_databases)
        """

    def describe_valid_db_instance_modifications(
        self, **kwargs: Unpack[DescribeValidDBInstanceModificationsMessageRequestTypeDef]
    ) -> DescribeValidDBInstanceModificationsResultTypeDef:
        """
        You can call `DescribeValidDBInstanceModifications` to learn what modifications
        you can make to your DB
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_valid_db_instance_modifications)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#describe_valid_db_instance_modifications)
        """

    def disable_http_endpoint(
        self, **kwargs: Unpack[DisableHttpEndpointRequestRequestTypeDef]
    ) -> DisableHttpEndpointResponseTypeDef:
        """
        Disables the HTTP endpoint for the specified DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.disable_http_endpoint)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#disable_http_endpoint)
        """

    def download_db_log_file_portion(
        self, **kwargs: Unpack[DownloadDBLogFilePortionMessageRequestTypeDef]
    ) -> DownloadDBLogFilePortionDetailsTypeDef:
        """
        Downloads all or a portion of the specified log file, up to 1 MB in size.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.download_db_log_file_portion)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#download_db_log_file_portion)
        """

    def enable_http_endpoint(
        self, **kwargs: Unpack[EnableHttpEndpointRequestRequestTypeDef]
    ) -> EnableHttpEndpointResponseTypeDef:
        """
        Enables the HTTP endpoint for the DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.enable_http_endpoint)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#enable_http_endpoint)
        """

    def failover_db_cluster(
        self, **kwargs: Unpack[FailoverDBClusterMessageRequestTypeDef]
    ) -> FailoverDBClusterResultTypeDef:
        """
        Forces a failover for a DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.failover_db_cluster)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#failover_db_cluster)
        """

    def failover_global_cluster(
        self, **kwargs: Unpack[FailoverGlobalClusterMessageRequestTypeDef]
    ) -> FailoverGlobalClusterResultTypeDef:
        """
        Promotes the specified secondary DB cluster to be the primary DB cluster in the
        global database cluster to fail over or switch over a global
        database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.failover_global_cluster)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#failover_global_cluster)
        """

    def generate_db_auth_token(
        self, DBHostname: str, Port: int, DBUsername: str, Region: Optional[str] = ...
    ) -> str:
        """
        Generates an auth token used to connect to a db with IAM credentials.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.generate_db_auth_token)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#generate_db_auth_token)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#generate_presigned_url)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceMessageRequestTypeDef]
    ) -> TagListMessageTypeDef:
        """
        Lists all tags on an Amazon RDS resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.list_tags_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#list_tags_for_resource)
        """

    def modify_activity_stream(
        self, **kwargs: Unpack[ModifyActivityStreamRequestRequestTypeDef]
    ) -> ModifyActivityStreamResponseTypeDef:
        """
        Changes the audit policy state of a database activity stream to either locked
        (default) or
        unlocked.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_activity_stream)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_activity_stream)
        """

    def modify_certificates(
        self, **kwargs: Unpack[ModifyCertificatesMessageRequestTypeDef]
    ) -> ModifyCertificatesResultTypeDef:
        """
        Override the system-default Secure Sockets Layer/Transport Layer Security
        (SSL/TLS) certificate for Amazon RDS for new DB instances, or remove the
        override.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_certificates)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_certificates)
        """

    def modify_current_db_cluster_capacity(
        self, **kwargs: Unpack[ModifyCurrentDBClusterCapacityMessageRequestTypeDef]
    ) -> DBClusterCapacityInfoTypeDef:
        """
        Set the capacity of an Aurora Serverless v1 DB cluster to a specific value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_current_db_cluster_capacity)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_current_db_cluster_capacity)
        """

    def modify_custom_db_engine_version(
        self, **kwargs: Unpack[ModifyCustomDBEngineVersionMessageRequestTypeDef]
    ) -> DBEngineVersionResponseTypeDef:
        """
        Modifies the status of a custom engine version (CEV).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_custom_db_engine_version)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_custom_db_engine_version)
        """

    def modify_db_cluster(
        self, **kwargs: Unpack[ModifyDBClusterMessageRequestTypeDef]
    ) -> ModifyDBClusterResultTypeDef:
        """
        Modifies the settings of an Amazon Aurora DB cluster or a Multi-AZ DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_cluster)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_cluster)
        """

    def modify_db_cluster_endpoint(
        self, **kwargs: Unpack[ModifyDBClusterEndpointMessageRequestTypeDef]
    ) -> DBClusterEndpointResponseTypeDef:
        """
        Modifies the properties of an endpoint in an Amazon Aurora DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_cluster_endpoint)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_cluster_endpoint)
        """

    def modify_db_cluster_parameter_group(
        self, **kwargs: Unpack[ModifyDBClusterParameterGroupMessageRequestTypeDef]
    ) -> DBClusterParameterGroupNameMessageTypeDef:
        """
        Modifies the parameters of a DB cluster parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_cluster_parameter_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_cluster_parameter_group)
        """

    def modify_db_cluster_snapshot_attribute(
        self, **kwargs: Unpack[ModifyDBClusterSnapshotAttributeMessageRequestTypeDef]
    ) -> ModifyDBClusterSnapshotAttributeResultTypeDef:
        """
        Adds an attribute and values to, or removes an attribute and values from, a
        manual DB cluster
        snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_cluster_snapshot_attribute)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_cluster_snapshot_attribute)
        """

    def modify_db_instance(
        self, **kwargs: Unpack[ModifyDBInstanceMessageRequestTypeDef]
    ) -> ModifyDBInstanceResultTypeDef:
        """
        Modifies settings for a DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_instance)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_instance)
        """

    def modify_db_parameter_group(
        self, **kwargs: Unpack[ModifyDBParameterGroupMessageRequestTypeDef]
    ) -> DBParameterGroupNameMessageTypeDef:
        """
        Modifies the parameters of a DB parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_parameter_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_parameter_group)
        """

    def modify_db_proxy(
        self, **kwargs: Unpack[ModifyDBProxyRequestRequestTypeDef]
    ) -> ModifyDBProxyResponseTypeDef:
        """
        Changes the settings for an existing DB proxy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_proxy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_proxy)
        """

    def modify_db_proxy_endpoint(
        self, **kwargs: Unpack[ModifyDBProxyEndpointRequestRequestTypeDef]
    ) -> ModifyDBProxyEndpointResponseTypeDef:
        """
        Changes the settings for an existing DB proxy endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_proxy_endpoint)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_proxy_endpoint)
        """

    def modify_db_proxy_target_group(
        self, **kwargs: Unpack[ModifyDBProxyTargetGroupRequestRequestTypeDef]
    ) -> ModifyDBProxyTargetGroupResponseTypeDef:
        """
        Modifies the properties of a `DBProxyTargetGroup`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_proxy_target_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_proxy_target_group)
        """

    def modify_db_recommendation(
        self, **kwargs: Unpack[ModifyDBRecommendationMessageRequestTypeDef]
    ) -> DBRecommendationMessageTypeDef:
        """
        Updates the recommendation status and recommended action status for the
        specified
        recommendation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_recommendation)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_recommendation)
        """

    def modify_db_shard_group(
        self, **kwargs: Unpack[ModifyDBShardGroupMessageRequestTypeDef]
    ) -> DBShardGroupResponseTypeDef:
        """
        Modifies the settings of an Aurora Limitless Database DB shard group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_shard_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_shard_group)
        """

    def modify_db_snapshot(
        self, **kwargs: Unpack[ModifyDBSnapshotMessageRequestTypeDef]
    ) -> ModifyDBSnapshotResultTypeDef:
        """
        Updates a manual DB snapshot with a new engine version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_snapshot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_snapshot)
        """

    def modify_db_snapshot_attribute(
        self, **kwargs: Unpack[ModifyDBSnapshotAttributeMessageRequestTypeDef]
    ) -> ModifyDBSnapshotAttributeResultTypeDef:
        """
        Adds an attribute and values to, or removes an attribute and values from, a
        manual DB
        snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_snapshot_attribute)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_snapshot_attribute)
        """

    def modify_db_subnet_group(
        self, **kwargs: Unpack[ModifyDBSubnetGroupMessageRequestTypeDef]
    ) -> ModifyDBSubnetGroupResultTypeDef:
        """
        Modifies an existing DB subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_db_subnet_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_db_subnet_group)
        """

    def modify_event_subscription(
        self, **kwargs: Unpack[ModifyEventSubscriptionMessageRequestTypeDef]
    ) -> ModifyEventSubscriptionResultTypeDef:
        """
        Modifies an existing RDS event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_event_subscription)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_event_subscription)
        """

    def modify_global_cluster(
        self, **kwargs: Unpack[ModifyGlobalClusterMessageRequestTypeDef]
    ) -> ModifyGlobalClusterResultTypeDef:
        """
        Modifies a setting for an Amazon Aurora global database cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_global_cluster)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_global_cluster)
        """

    def modify_integration(
        self, **kwargs: Unpack[ModifyIntegrationMessageRequestTypeDef]
    ) -> IntegrationResponseTypeDef:
        """
        Modifies a zero-ETL integration with Amazon Redshift.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_integration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_integration)
        """

    def modify_option_group(
        self, **kwargs: Unpack[ModifyOptionGroupMessageRequestTypeDef]
    ) -> ModifyOptionGroupResultTypeDef:
        """
        Modifies an existing option group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_option_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_option_group)
        """

    def modify_tenant_database(
        self, **kwargs: Unpack[ModifyTenantDatabaseMessageRequestTypeDef]
    ) -> ModifyTenantDatabaseResultTypeDef:
        """
        Modifies an existing tenant database in a DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.modify_tenant_database)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#modify_tenant_database)
        """

    def promote_read_replica(
        self, **kwargs: Unpack[PromoteReadReplicaMessageRequestTypeDef]
    ) -> PromoteReadReplicaResultTypeDef:
        """
        Promotes a read replica DB instance to a standalone DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.promote_read_replica)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#promote_read_replica)
        """

    def promote_read_replica_db_cluster(
        self, **kwargs: Unpack[PromoteReadReplicaDBClusterMessageRequestTypeDef]
    ) -> PromoteReadReplicaDBClusterResultTypeDef:
        """
        Promotes a read replica DB cluster to a standalone DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.promote_read_replica_db_cluster)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#promote_read_replica_db_cluster)
        """

    def purchase_reserved_db_instances_offering(
        self, **kwargs: Unpack[PurchaseReservedDBInstancesOfferingMessageRequestTypeDef]
    ) -> PurchaseReservedDBInstancesOfferingResultTypeDef:
        """
        Purchases a reserved DB instance offering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.purchase_reserved_db_instances_offering)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#purchase_reserved_db_instances_offering)
        """

    def reboot_db_cluster(
        self, **kwargs: Unpack[RebootDBClusterMessageRequestTypeDef]
    ) -> RebootDBClusterResultTypeDef:
        """
        You might need to reboot your DB cluster, usually for maintenance reasons.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.reboot_db_cluster)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#reboot_db_cluster)
        """

    def reboot_db_instance(
        self, **kwargs: Unpack[RebootDBInstanceMessageRequestTypeDef]
    ) -> RebootDBInstanceResultTypeDef:
        """
        You might need to reboot your DB instance, usually for maintenance reasons.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.reboot_db_instance)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#reboot_db_instance)
        """

    def reboot_db_shard_group(
        self, **kwargs: Unpack[RebootDBShardGroupMessageRequestTypeDef]
    ) -> DBShardGroupResponseTypeDef:
        """
        You might need to reboot your DB shard group, usually for maintenance reasons.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.reboot_db_shard_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#reboot_db_shard_group)
        """

    def register_db_proxy_targets(
        self, **kwargs: Unpack[RegisterDBProxyTargetsRequestRequestTypeDef]
    ) -> RegisterDBProxyTargetsResponseTypeDef:
        """
        Associate one or more `DBProxyTarget` data structures with a
        `DBProxyTargetGroup`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.register_db_proxy_targets)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#register_db_proxy_targets)
        """

    def remove_from_global_cluster(
        self, **kwargs: Unpack[RemoveFromGlobalClusterMessageRequestTypeDef]
    ) -> RemoveFromGlobalClusterResultTypeDef:
        """
        Detaches an Aurora secondary cluster from an Aurora global database cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.remove_from_global_cluster)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#remove_from_global_cluster)
        """

    def remove_role_from_db_cluster(
        self, **kwargs: Unpack[RemoveRoleFromDBClusterMessageRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the asssociation of an Amazon Web Services Identity and Access
        Management (IAM) role from a DB
        cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.remove_role_from_db_cluster)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#remove_role_from_db_cluster)
        """

    def remove_role_from_db_instance(
        self, **kwargs: Unpack[RemoveRoleFromDBInstanceMessageRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Disassociates an Amazon Web Services Identity and Access Management (IAM) role
        from a DB
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.remove_role_from_db_instance)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#remove_role_from_db_instance)
        """

    def remove_source_identifier_from_subscription(
        self, **kwargs: Unpack[RemoveSourceIdentifierFromSubscriptionMessageRequestTypeDef]
    ) -> RemoveSourceIdentifierFromSubscriptionResultTypeDef:
        """
        Removes a source identifier from an existing RDS event notification
        subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.remove_source_identifier_from_subscription)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#remove_source_identifier_from_subscription)
        """

    def remove_tags_from_resource(
        self, **kwargs: Unpack[RemoveTagsFromResourceMessageRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes metadata tags from an Amazon RDS resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.remove_tags_from_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#remove_tags_from_resource)
        """

    def reset_db_cluster_parameter_group(
        self, **kwargs: Unpack[ResetDBClusterParameterGroupMessageRequestTypeDef]
    ) -> DBClusterParameterGroupNameMessageTypeDef:
        """
        Modifies the parameters of a DB cluster parameter group to the default value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.reset_db_cluster_parameter_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#reset_db_cluster_parameter_group)
        """

    def reset_db_parameter_group(
        self, **kwargs: Unpack[ResetDBParameterGroupMessageRequestTypeDef]
    ) -> DBParameterGroupNameMessageTypeDef:
        """
        Modifies the parameters of a DB parameter group to the engine/system default
        value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.reset_db_parameter_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#reset_db_parameter_group)
        """

    def restore_db_cluster_from_s3(
        self, **kwargs: Unpack[RestoreDBClusterFromS3MessageRequestTypeDef]
    ) -> RestoreDBClusterFromS3ResultTypeDef:
        """
        Creates an Amazon Aurora DB cluster from MySQL data stored in an Amazon S3
        bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.restore_db_cluster_from_s3)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#restore_db_cluster_from_s3)
        """

    def restore_db_cluster_from_snapshot(
        self, **kwargs: Unpack[RestoreDBClusterFromSnapshotMessageRequestTypeDef]
    ) -> RestoreDBClusterFromSnapshotResultTypeDef:
        """
        Creates a new DB cluster from a DB snapshot or DB cluster snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.restore_db_cluster_from_snapshot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#restore_db_cluster_from_snapshot)
        """

    def restore_db_cluster_to_point_in_time(
        self, **kwargs: Unpack[RestoreDBClusterToPointInTimeMessageRequestTypeDef]
    ) -> RestoreDBClusterToPointInTimeResultTypeDef:
        """
        Restores a DB cluster to an arbitrary point in time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.restore_db_cluster_to_point_in_time)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#restore_db_cluster_to_point_in_time)
        """

    def restore_db_instance_from_db_snapshot(
        self, **kwargs: Unpack[RestoreDBInstanceFromDBSnapshotMessageRequestTypeDef]
    ) -> RestoreDBInstanceFromDBSnapshotResultTypeDef:
        """
        Creates a new DB instance from a DB snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.restore_db_instance_from_db_snapshot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#restore_db_instance_from_db_snapshot)
        """

    def restore_db_instance_from_s3(
        self, **kwargs: Unpack[RestoreDBInstanceFromS3MessageRequestTypeDef]
    ) -> RestoreDBInstanceFromS3ResultTypeDef:
        """
        Amazon Relational Database Service (Amazon RDS) supports importing MySQL
        databases by using backup
        files.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.restore_db_instance_from_s3)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#restore_db_instance_from_s3)
        """

    def restore_db_instance_to_point_in_time(
        self, **kwargs: Unpack[RestoreDBInstanceToPointInTimeMessageRequestTypeDef]
    ) -> RestoreDBInstanceToPointInTimeResultTypeDef:
        """
        Restores a DB instance to an arbitrary point in time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.restore_db_instance_to_point_in_time)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#restore_db_instance_to_point_in_time)
        """

    def revoke_db_security_group_ingress(
        self, **kwargs: Unpack[RevokeDBSecurityGroupIngressMessageRequestTypeDef]
    ) -> RevokeDBSecurityGroupIngressResultTypeDef:
        """
        Revokes ingress from a DBSecurityGroup for previously authorized IP ranges or
        EC2 or VPC security
        groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.revoke_db_security_group_ingress)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#revoke_db_security_group_ingress)
        """

    def start_activity_stream(
        self, **kwargs: Unpack[StartActivityStreamRequestRequestTypeDef]
    ) -> StartActivityStreamResponseTypeDef:
        """
        Starts a database activity stream to monitor activity on the database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.start_activity_stream)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#start_activity_stream)
        """

    def start_db_cluster(
        self, **kwargs: Unpack[StartDBClusterMessageRequestTypeDef]
    ) -> StartDBClusterResultTypeDef:
        """
        Starts an Amazon Aurora DB cluster that was stopped using the Amazon Web
        Services console, the stop-db-cluster CLI command, or the `StopDBCluster`
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.start_db_cluster)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#start_db_cluster)
        """

    def start_db_instance(
        self, **kwargs: Unpack[StartDBInstanceMessageRequestTypeDef]
    ) -> StartDBInstanceResultTypeDef:
        """
        Starts an Amazon RDS DB instance that was stopped using the Amazon Web Services
        console, the stop-db-instance CLI command, or the `StopDBInstance`
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.start_db_instance)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#start_db_instance)
        """

    def start_db_instance_automated_backups_replication(
        self, **kwargs: Unpack[StartDBInstanceAutomatedBackupsReplicationMessageRequestTypeDef]
    ) -> StartDBInstanceAutomatedBackupsReplicationResultTypeDef:
        """
        Enables replication of automated backups to a different Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.start_db_instance_automated_backups_replication)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#start_db_instance_automated_backups_replication)
        """

    def start_export_task(
        self, **kwargs: Unpack[StartExportTaskMessageRequestTypeDef]
    ) -> ExportTaskResponseTypeDef:
        """
        Starts an export of DB snapshot or DB cluster data to Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.start_export_task)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#start_export_task)
        """

    def stop_activity_stream(
        self, **kwargs: Unpack[StopActivityStreamRequestRequestTypeDef]
    ) -> StopActivityStreamResponseTypeDef:
        """
        Stops a database activity stream that was started using the Amazon Web Services
        console, the `start-activity-stream` CLI command, or the `StartActivityStream`
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.stop_activity_stream)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#stop_activity_stream)
        """

    def stop_db_cluster(
        self, **kwargs: Unpack[StopDBClusterMessageRequestTypeDef]
    ) -> StopDBClusterResultTypeDef:
        """
        Stops an Amazon Aurora DB cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.stop_db_cluster)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#stop_db_cluster)
        """

    def stop_db_instance(
        self, **kwargs: Unpack[StopDBInstanceMessageRequestTypeDef]
    ) -> StopDBInstanceResultTypeDef:
        """
        Stops an Amazon RDS DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.stop_db_instance)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#stop_db_instance)
        """

    def stop_db_instance_automated_backups_replication(
        self, **kwargs: Unpack[StopDBInstanceAutomatedBackupsReplicationMessageRequestTypeDef]
    ) -> StopDBInstanceAutomatedBackupsReplicationResultTypeDef:
        """
        Stops automated backup replication for a DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.stop_db_instance_automated_backups_replication)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#stop_db_instance_automated_backups_replication)
        """

    def switchover_blue_green_deployment(
        self, **kwargs: Unpack[SwitchoverBlueGreenDeploymentRequestRequestTypeDef]
    ) -> SwitchoverBlueGreenDeploymentResponseTypeDef:
        """
        Switches over a blue/green deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.switchover_blue_green_deployment)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#switchover_blue_green_deployment)
        """

    def switchover_global_cluster(
        self, **kwargs: Unpack[SwitchoverGlobalClusterMessageRequestTypeDef]
    ) -> SwitchoverGlobalClusterResultTypeDef:
        """
        Switches over the specified secondary DB cluster to be the new primary DB
        cluster in the global database
        cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.switchover_global_cluster)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#switchover_global_cluster)
        """

    def switchover_read_replica(
        self, **kwargs: Unpack[SwitchoverReadReplicaMessageRequestTypeDef]
    ) -> SwitchoverReadReplicaResultTypeDef:
        """
        Switches over an Oracle standby database in an Oracle Data Guard environment,
        making it the new primary
        database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.switchover_read_replica)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#switchover_read_replica)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_blue_green_deployments"]
    ) -> DescribeBlueGreenDeploymentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_certificates"]
    ) -> DescribeCertificatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_automated_backups"]
    ) -> DescribeDBClusterAutomatedBackupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_backtracks"]
    ) -> DescribeDBClusterBacktracksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_endpoints"]
    ) -> DescribeDBClusterEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_parameter_groups"]
    ) -> DescribeDBClusterParameterGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_parameters"]
    ) -> DescribeDBClusterParametersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_cluster_snapshots"]
    ) -> DescribeDBClusterSnapshotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_clusters"]
    ) -> DescribeDBClustersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_engine_versions"]
    ) -> DescribeDBEngineVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_instance_automated_backups"]
    ) -> DescribeDBInstanceAutomatedBackupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_instances"]
    ) -> DescribeDBInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_log_files"]
    ) -> DescribeDBLogFilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_parameter_groups"]
    ) -> DescribeDBParameterGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_parameters"]
    ) -> DescribeDBParametersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_proxies"]
    ) -> DescribeDBProxiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_proxy_endpoints"]
    ) -> DescribeDBProxyEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_proxy_target_groups"]
    ) -> DescribeDBProxyTargetGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_proxy_targets"]
    ) -> DescribeDBProxyTargetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_recommendations"]
    ) -> DescribeDBRecommendationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_security_groups"]
    ) -> DescribeDBSecurityGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_snapshot_tenant_databases"]
    ) -> DescribeDBSnapshotTenantDatabasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_snapshots"]
    ) -> DescribeDBSnapshotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_subnet_groups"]
    ) -> DescribeDBSubnetGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_engine_default_cluster_parameters"]
    ) -> DescribeEngineDefaultClusterParametersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_engine_default_parameters"]
    ) -> DescribeEngineDefaultParametersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_event_subscriptions"]
    ) -> DescribeEventSubscriptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_events"]) -> DescribeEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_export_tasks"]
    ) -> DescribeExportTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_global_clusters"]
    ) -> DescribeGlobalClustersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_integrations"]
    ) -> DescribeIntegrationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_option_group_options"]
    ) -> DescribeOptionGroupOptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_option_groups"]
    ) -> DescribeOptionGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_orderable_db_instance_options"]
    ) -> DescribeOrderableDBInstanceOptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_pending_maintenance_actions"]
    ) -> DescribePendingMaintenanceActionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_db_instances"]
    ) -> DescribeReservedDBInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_db_instances_offerings"]
    ) -> DescribeReservedDBInstancesOfferingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_source_regions"]
    ) -> DescribeSourceRegionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_tenant_databases"]
    ) -> DescribeTenantDatabasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["download_db_log_file_portion"]
    ) -> DownloadDBLogFilePortionPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_paginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["db_cluster_available"]) -> DBClusterAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["db_cluster_deleted"]) -> DBClusterDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["db_cluster_snapshot_available"]
    ) -> DBClusterSnapshotAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["db_cluster_snapshot_deleted"]
    ) -> DBClusterSnapshotDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["db_instance_available"]
    ) -> DBInstanceAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["db_instance_deleted"]) -> DBInstanceDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["db_snapshot_available"]
    ) -> DBSnapshotAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["db_snapshot_completed"]
    ) -> DBSnapshotCompletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["db_snapshot_deleted"]) -> DBSnapshotDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["tenant_database_available"]
    ) -> TenantDatabaseAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["tenant_database_deleted"]
    ) -> TenantDatabaseDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds/client/#get_waiter)
        """
