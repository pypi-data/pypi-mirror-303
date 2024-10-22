"""
Type annotations for redshift-serverless service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/type_defs/)

Usage::

    ```python
    from mypy_boto3_redshift_serverless.type_defs import AssociationTypeDef

    data: AssociationTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    LogExportType,
    NamespaceStatusType,
    SnapshotStatusType,
    StateType,
    UsageLimitBreachActionType,
    UsageLimitPeriodType,
    UsageLimitUsageTypeType,
    WorkgroupStatusType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AssociationTypeDef",
    "ConfigParameterTypeDef",
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "SnapshotTypeDef",
    "CreateCustomDomainAssociationRequestRequestTypeDef",
    "CreateEndpointAccessRequestRequestTypeDef",
    "NamespaceTypeDef",
    "TimestampTypeDef",
    "CreateSnapshotCopyConfigurationRequestRequestTypeDef",
    "SnapshotCopyConfigurationTypeDef",
    "CreateUsageLimitRequestRequestTypeDef",
    "UsageLimitTypeDef",
    "DeleteCustomDomainAssociationRequestRequestTypeDef",
    "DeleteEndpointAccessRequestRequestTypeDef",
    "DeleteNamespaceRequestRequestTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DeleteScheduledActionRequestRequestTypeDef",
    "DeleteSnapshotCopyConfigurationRequestRequestTypeDef",
    "DeleteSnapshotRequestRequestTypeDef",
    "DeleteUsageLimitRequestRequestTypeDef",
    "DeleteWorkgroupRequestRequestTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "GetCredentialsRequestRequestTypeDef",
    "GetCustomDomainAssociationRequestRequestTypeDef",
    "GetEndpointAccessRequestRequestTypeDef",
    "GetNamespaceRequestRequestTypeDef",
    "GetRecoveryPointRequestRequestTypeDef",
    "RecoveryPointTypeDef",
    "GetResourcePolicyRequestRequestTypeDef",
    "ResourcePolicyTypeDef",
    "GetScheduledActionRequestRequestTypeDef",
    "GetSnapshotRequestRequestTypeDef",
    "GetTableRestoreStatusRequestRequestTypeDef",
    "TableRestoreStatusTypeDef",
    "GetUsageLimitRequestRequestTypeDef",
    "GetWorkgroupRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListCustomDomainAssociationsRequestRequestTypeDef",
    "ListEndpointAccessRequestRequestTypeDef",
    "ListNamespacesRequestRequestTypeDef",
    "ListScheduledActionsRequestRequestTypeDef",
    "ScheduledActionAssociationTypeDef",
    "ListSnapshotCopyConfigurationsRequestRequestTypeDef",
    "ListTableRestoreStatusRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListUsageLimitsRequestRequestTypeDef",
    "ListWorkgroupsRequestRequestTypeDef",
    "NetworkInterfaceTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "RestoreFromRecoveryPointRequestRequestTypeDef",
    "RestoreFromSnapshotRequestRequestTypeDef",
    "RestoreTableFromRecoveryPointRequestRequestTypeDef",
    "RestoreTableFromSnapshotRequestRequestTypeDef",
    "ScheduleOutputTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateCustomDomainAssociationRequestRequestTypeDef",
    "UpdateEndpointAccessRequestRequestTypeDef",
    "UpdateNamespaceRequestRequestTypeDef",
    "UpdateSnapshotCopyConfigurationRequestRequestTypeDef",
    "UpdateSnapshotRequestRequestTypeDef",
    "UpdateUsageLimitRequestRequestTypeDef",
    "UpdateWorkgroupRequestRequestTypeDef",
    "ConvertRecoveryPointToSnapshotRequestRequestTypeDef",
    "CreateNamespaceRequestRequestTypeDef",
    "CreateSnapshotRequestRequestTypeDef",
    "CreateSnapshotScheduleActionParametersOutputTypeDef",
    "CreateSnapshotScheduleActionParametersTypeDef",
    "CreateWorkgroupRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateCustomDomainAssociationResponseTypeDef",
    "GetCredentialsResponseTypeDef",
    "GetCustomDomainAssociationResponseTypeDef",
    "ListCustomDomainAssociationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "UpdateCustomDomainAssociationResponseTypeDef",
    "ConvertRecoveryPointToSnapshotResponseTypeDef",
    "CreateSnapshotResponseTypeDef",
    "DeleteSnapshotResponseTypeDef",
    "GetSnapshotResponseTypeDef",
    "ListSnapshotsResponseTypeDef",
    "UpdateSnapshotResponseTypeDef",
    "CreateNamespaceResponseTypeDef",
    "DeleteNamespaceResponseTypeDef",
    "GetNamespaceResponseTypeDef",
    "ListNamespacesResponseTypeDef",
    "RestoreFromRecoveryPointResponseTypeDef",
    "RestoreFromSnapshotResponseTypeDef",
    "UpdateNamespaceResponseTypeDef",
    "ListRecoveryPointsRequestRequestTypeDef",
    "ListSnapshotsRequestRequestTypeDef",
    "ScheduleTypeDef",
    "CreateSnapshotCopyConfigurationResponseTypeDef",
    "DeleteSnapshotCopyConfigurationResponseTypeDef",
    "ListSnapshotCopyConfigurationsResponseTypeDef",
    "UpdateSnapshotCopyConfigurationResponseTypeDef",
    "CreateUsageLimitResponseTypeDef",
    "DeleteUsageLimitResponseTypeDef",
    "GetUsageLimitResponseTypeDef",
    "ListUsageLimitsResponseTypeDef",
    "UpdateUsageLimitResponseTypeDef",
    "GetRecoveryPointResponseTypeDef",
    "ListRecoveryPointsResponseTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "GetTableRestoreStatusResponseTypeDef",
    "ListTableRestoreStatusResponseTypeDef",
    "RestoreTableFromRecoveryPointResponseTypeDef",
    "RestoreTableFromSnapshotResponseTypeDef",
    "ListCustomDomainAssociationsRequestListCustomDomainAssociationsPaginateTypeDef",
    "ListEndpointAccessRequestListEndpointAccessPaginateTypeDef",
    "ListNamespacesRequestListNamespacesPaginateTypeDef",
    "ListRecoveryPointsRequestListRecoveryPointsPaginateTypeDef",
    "ListScheduledActionsRequestListScheduledActionsPaginateTypeDef",
    "ListSnapshotCopyConfigurationsRequestListSnapshotCopyConfigurationsPaginateTypeDef",
    "ListSnapshotsRequestListSnapshotsPaginateTypeDef",
    "ListTableRestoreStatusRequestListTableRestoreStatusPaginateTypeDef",
    "ListUsageLimitsRequestListUsageLimitsPaginateTypeDef",
    "ListWorkgroupsRequestListWorkgroupsPaginateTypeDef",
    "ListScheduledActionsResponseTypeDef",
    "VpcEndpointTypeDef",
    "TargetActionOutputTypeDef",
    "CreateSnapshotScheduleActionParametersUnionTypeDef",
    "EndpointAccessTypeDef",
    "EndpointTypeDef",
    "ScheduledActionResponseTypeDef",
    "TargetActionTypeDef",
    "CreateEndpointAccessResponseTypeDef",
    "DeleteEndpointAccessResponseTypeDef",
    "GetEndpointAccessResponseTypeDef",
    "ListEndpointAccessResponseTypeDef",
    "UpdateEndpointAccessResponseTypeDef",
    "WorkgroupTypeDef",
    "CreateScheduledActionResponseTypeDef",
    "DeleteScheduledActionResponseTypeDef",
    "GetScheduledActionResponseTypeDef",
    "UpdateScheduledActionResponseTypeDef",
    "CreateScheduledActionRequestRequestTypeDef",
    "UpdateScheduledActionRequestRequestTypeDef",
    "CreateWorkgroupResponseTypeDef",
    "DeleteWorkgroupResponseTypeDef",
    "GetWorkgroupResponseTypeDef",
    "ListWorkgroupsResponseTypeDef",
    "UpdateWorkgroupResponseTypeDef",
)

AssociationTypeDef = TypedDict(
    "AssociationTypeDef",
    {
        "customDomainCertificateArn": NotRequired[str],
        "customDomainCertificateExpiryTime": NotRequired[datetime],
        "customDomainName": NotRequired[str],
        "workgroupName": NotRequired[str],
    },
)
ConfigParameterTypeDef = TypedDict(
    "ConfigParameterTypeDef",
    {
        "parameterKey": NotRequired[str],
        "parameterValue": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
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
SnapshotTypeDef = TypedDict(
    "SnapshotTypeDef",
    {
        "accountsWithProvisionedRestoreAccess": NotRequired[List[str]],
        "accountsWithRestoreAccess": NotRequired[List[str]],
        "actualIncrementalBackupSizeInMegaBytes": NotRequired[float],
        "adminPasswordSecretArn": NotRequired[str],
        "adminPasswordSecretKmsKeyId": NotRequired[str],
        "adminUsername": NotRequired[str],
        "backupProgressInMegaBytes": NotRequired[float],
        "currentBackupRateInMegaBytesPerSecond": NotRequired[float],
        "elapsedTimeInSeconds": NotRequired[int],
        "estimatedSecondsToCompletion": NotRequired[int],
        "kmsKeyId": NotRequired[str],
        "namespaceArn": NotRequired[str],
        "namespaceName": NotRequired[str],
        "ownerAccount": NotRequired[str],
        "snapshotArn": NotRequired[str],
        "snapshotCreateTime": NotRequired[datetime],
        "snapshotName": NotRequired[str],
        "snapshotRemainingDays": NotRequired[int],
        "snapshotRetentionPeriod": NotRequired[int],
        "snapshotRetentionStartTime": NotRequired[datetime],
        "status": NotRequired[SnapshotStatusType],
        "totalBackupSizeInMegaBytes": NotRequired[float],
    },
)
CreateCustomDomainAssociationRequestRequestTypeDef = TypedDict(
    "CreateCustomDomainAssociationRequestRequestTypeDef",
    {
        "customDomainCertificateArn": str,
        "customDomainName": str,
        "workgroupName": str,
    },
)
CreateEndpointAccessRequestRequestTypeDef = TypedDict(
    "CreateEndpointAccessRequestRequestTypeDef",
    {
        "endpointName": str,
        "subnetIds": Sequence[str],
        "workgroupName": str,
        "ownerAccount": NotRequired[str],
        "vpcSecurityGroupIds": NotRequired[Sequence[str]],
    },
)
NamespaceTypeDef = TypedDict(
    "NamespaceTypeDef",
    {
        "adminPasswordSecretArn": NotRequired[str],
        "adminPasswordSecretKmsKeyId": NotRequired[str],
        "adminUsername": NotRequired[str],
        "creationDate": NotRequired[datetime],
        "dbName": NotRequired[str],
        "defaultIamRoleArn": NotRequired[str],
        "iamRoles": NotRequired[List[str]],
        "kmsKeyId": NotRequired[str],
        "logExports": NotRequired[List[LogExportType]],
        "namespaceArn": NotRequired[str],
        "namespaceId": NotRequired[str],
        "namespaceName": NotRequired[str],
        "status": NotRequired[NamespaceStatusType],
    },
)
TimestampTypeDef = Union[datetime, str]
CreateSnapshotCopyConfigurationRequestRequestTypeDef = TypedDict(
    "CreateSnapshotCopyConfigurationRequestRequestTypeDef",
    {
        "destinationRegion": str,
        "namespaceName": str,
        "destinationKmsKeyId": NotRequired[str],
        "snapshotRetentionPeriod": NotRequired[int],
    },
)
SnapshotCopyConfigurationTypeDef = TypedDict(
    "SnapshotCopyConfigurationTypeDef",
    {
        "destinationKmsKeyId": NotRequired[str],
        "destinationRegion": NotRequired[str],
        "namespaceName": NotRequired[str],
        "snapshotCopyConfigurationArn": NotRequired[str],
        "snapshotCopyConfigurationId": NotRequired[str],
        "snapshotRetentionPeriod": NotRequired[int],
    },
)
CreateUsageLimitRequestRequestTypeDef = TypedDict(
    "CreateUsageLimitRequestRequestTypeDef",
    {
        "amount": int,
        "resourceArn": str,
        "usageType": UsageLimitUsageTypeType,
        "breachAction": NotRequired[UsageLimitBreachActionType],
        "period": NotRequired[UsageLimitPeriodType],
    },
)
UsageLimitTypeDef = TypedDict(
    "UsageLimitTypeDef",
    {
        "amount": NotRequired[int],
        "breachAction": NotRequired[UsageLimitBreachActionType],
        "period": NotRequired[UsageLimitPeriodType],
        "resourceArn": NotRequired[str],
        "usageLimitArn": NotRequired[str],
        "usageLimitId": NotRequired[str],
        "usageType": NotRequired[UsageLimitUsageTypeType],
    },
)
DeleteCustomDomainAssociationRequestRequestTypeDef = TypedDict(
    "DeleteCustomDomainAssociationRequestRequestTypeDef",
    {
        "customDomainName": str,
        "workgroupName": str,
    },
)
DeleteEndpointAccessRequestRequestTypeDef = TypedDict(
    "DeleteEndpointAccessRequestRequestTypeDef",
    {
        "endpointName": str,
    },
)
DeleteNamespaceRequestRequestTypeDef = TypedDict(
    "DeleteNamespaceRequestRequestTypeDef",
    {
        "namespaceName": str,
        "finalSnapshotName": NotRequired[str],
        "finalSnapshotRetentionPeriod": NotRequired[int],
    },
)
DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
DeleteScheduledActionRequestRequestTypeDef = TypedDict(
    "DeleteScheduledActionRequestRequestTypeDef",
    {
        "scheduledActionName": str,
    },
)
DeleteSnapshotCopyConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteSnapshotCopyConfigurationRequestRequestTypeDef",
    {
        "snapshotCopyConfigurationId": str,
    },
)
DeleteSnapshotRequestRequestTypeDef = TypedDict(
    "DeleteSnapshotRequestRequestTypeDef",
    {
        "snapshotName": str,
    },
)
DeleteUsageLimitRequestRequestTypeDef = TypedDict(
    "DeleteUsageLimitRequestRequestTypeDef",
    {
        "usageLimitId": str,
    },
)
DeleteWorkgroupRequestRequestTypeDef = TypedDict(
    "DeleteWorkgroupRequestRequestTypeDef",
    {
        "workgroupName": str,
    },
)
VpcSecurityGroupMembershipTypeDef = TypedDict(
    "VpcSecurityGroupMembershipTypeDef",
    {
        "status": NotRequired[str],
        "vpcSecurityGroupId": NotRequired[str],
    },
)
GetCredentialsRequestRequestTypeDef = TypedDict(
    "GetCredentialsRequestRequestTypeDef",
    {
        "customDomainName": NotRequired[str],
        "dbName": NotRequired[str],
        "durationSeconds": NotRequired[int],
        "workgroupName": NotRequired[str],
    },
)
GetCustomDomainAssociationRequestRequestTypeDef = TypedDict(
    "GetCustomDomainAssociationRequestRequestTypeDef",
    {
        "customDomainName": str,
        "workgroupName": str,
    },
)
GetEndpointAccessRequestRequestTypeDef = TypedDict(
    "GetEndpointAccessRequestRequestTypeDef",
    {
        "endpointName": str,
    },
)
GetNamespaceRequestRequestTypeDef = TypedDict(
    "GetNamespaceRequestRequestTypeDef",
    {
        "namespaceName": str,
    },
)
GetRecoveryPointRequestRequestTypeDef = TypedDict(
    "GetRecoveryPointRequestRequestTypeDef",
    {
        "recoveryPointId": str,
    },
)
RecoveryPointTypeDef = TypedDict(
    "RecoveryPointTypeDef",
    {
        "namespaceArn": NotRequired[str],
        "namespaceName": NotRequired[str],
        "recoveryPointCreateTime": NotRequired[datetime],
        "recoveryPointId": NotRequired[str],
        "totalSizeInMegaBytes": NotRequired[float],
        "workgroupName": NotRequired[str],
    },
)
GetResourcePolicyRequestRequestTypeDef = TypedDict(
    "GetResourcePolicyRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
ResourcePolicyTypeDef = TypedDict(
    "ResourcePolicyTypeDef",
    {
        "policy": NotRequired[str],
        "resourceArn": NotRequired[str],
    },
)
GetScheduledActionRequestRequestTypeDef = TypedDict(
    "GetScheduledActionRequestRequestTypeDef",
    {
        "scheduledActionName": str,
    },
)
GetSnapshotRequestRequestTypeDef = TypedDict(
    "GetSnapshotRequestRequestTypeDef",
    {
        "ownerAccount": NotRequired[str],
        "snapshotArn": NotRequired[str],
        "snapshotName": NotRequired[str],
    },
)
GetTableRestoreStatusRequestRequestTypeDef = TypedDict(
    "GetTableRestoreStatusRequestRequestTypeDef",
    {
        "tableRestoreRequestId": str,
    },
)
TableRestoreStatusTypeDef = TypedDict(
    "TableRestoreStatusTypeDef",
    {
        "message": NotRequired[str],
        "namespaceName": NotRequired[str],
        "newTableName": NotRequired[str],
        "progressInMegaBytes": NotRequired[int],
        "recoveryPointId": NotRequired[str],
        "requestTime": NotRequired[datetime],
        "snapshotName": NotRequired[str],
        "sourceDatabaseName": NotRequired[str],
        "sourceSchemaName": NotRequired[str],
        "sourceTableName": NotRequired[str],
        "status": NotRequired[str],
        "tableRestoreRequestId": NotRequired[str],
        "targetDatabaseName": NotRequired[str],
        "targetSchemaName": NotRequired[str],
        "totalDataInMegaBytes": NotRequired[int],
        "workgroupName": NotRequired[str],
    },
)
GetUsageLimitRequestRequestTypeDef = TypedDict(
    "GetUsageLimitRequestRequestTypeDef",
    {
        "usageLimitId": str,
    },
)
GetWorkgroupRequestRequestTypeDef = TypedDict(
    "GetWorkgroupRequestRequestTypeDef",
    {
        "workgroupName": str,
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
ListCustomDomainAssociationsRequestRequestTypeDef = TypedDict(
    "ListCustomDomainAssociationsRequestRequestTypeDef",
    {
        "customDomainCertificateArn": NotRequired[str],
        "customDomainName": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListEndpointAccessRequestRequestTypeDef = TypedDict(
    "ListEndpointAccessRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "ownerAccount": NotRequired[str],
        "vpcId": NotRequired[str],
        "workgroupName": NotRequired[str],
    },
)
ListNamespacesRequestRequestTypeDef = TypedDict(
    "ListNamespacesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListScheduledActionsRequestRequestTypeDef = TypedDict(
    "ListScheduledActionsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "namespaceName": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)
ScheduledActionAssociationTypeDef = TypedDict(
    "ScheduledActionAssociationTypeDef",
    {
        "namespaceName": NotRequired[str],
        "scheduledActionName": NotRequired[str],
    },
)
ListSnapshotCopyConfigurationsRequestRequestTypeDef = TypedDict(
    "ListSnapshotCopyConfigurationsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "namespaceName": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)
ListTableRestoreStatusRequestRequestTypeDef = TypedDict(
    "ListTableRestoreStatusRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "namespaceName": NotRequired[str],
        "nextToken": NotRequired[str],
        "workgroupName": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
ListUsageLimitsRequestRequestTypeDef = TypedDict(
    "ListUsageLimitsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "resourceArn": NotRequired[str],
        "usageType": NotRequired[UsageLimitUsageTypeType],
    },
)
ListWorkgroupsRequestRequestTypeDef = TypedDict(
    "ListWorkgroupsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "ownerAccount": NotRequired[str],
    },
)
NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "availabilityZone": NotRequired[str],
        "ipv6Address": NotRequired[str],
        "networkInterfaceId": NotRequired[str],
        "privateIpAddress": NotRequired[str],
        "subnetId": NotRequired[str],
    },
)
PutResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestRequestTypeDef",
    {
        "policy": str,
        "resourceArn": str,
    },
)
RestoreFromRecoveryPointRequestRequestTypeDef = TypedDict(
    "RestoreFromRecoveryPointRequestRequestTypeDef",
    {
        "namespaceName": str,
        "recoveryPointId": str,
        "workgroupName": str,
    },
)
RestoreFromSnapshotRequestRequestTypeDef = TypedDict(
    "RestoreFromSnapshotRequestRequestTypeDef",
    {
        "namespaceName": str,
        "workgroupName": str,
        "adminPasswordSecretKmsKeyId": NotRequired[str],
        "manageAdminPassword": NotRequired[bool],
        "ownerAccount": NotRequired[str],
        "snapshotArn": NotRequired[str],
        "snapshotName": NotRequired[str],
    },
)
RestoreTableFromRecoveryPointRequestRequestTypeDef = TypedDict(
    "RestoreTableFromRecoveryPointRequestRequestTypeDef",
    {
        "namespaceName": str,
        "newTableName": str,
        "recoveryPointId": str,
        "sourceDatabaseName": str,
        "sourceTableName": str,
        "workgroupName": str,
        "activateCaseSensitiveIdentifier": NotRequired[bool],
        "sourceSchemaName": NotRequired[str],
        "targetDatabaseName": NotRequired[str],
        "targetSchemaName": NotRequired[str],
    },
)
RestoreTableFromSnapshotRequestRequestTypeDef = TypedDict(
    "RestoreTableFromSnapshotRequestRequestTypeDef",
    {
        "namespaceName": str,
        "newTableName": str,
        "snapshotName": str,
        "sourceDatabaseName": str,
        "sourceTableName": str,
        "workgroupName": str,
        "activateCaseSensitiveIdentifier": NotRequired[bool],
        "sourceSchemaName": NotRequired[str],
        "targetDatabaseName": NotRequired[str],
        "targetSchemaName": NotRequired[str],
    },
)
ScheduleOutputTypeDef = TypedDict(
    "ScheduleOutputTypeDef",
    {
        "at": NotRequired[datetime],
        "cron": NotRequired[str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UpdateCustomDomainAssociationRequestRequestTypeDef = TypedDict(
    "UpdateCustomDomainAssociationRequestRequestTypeDef",
    {
        "customDomainCertificateArn": str,
        "customDomainName": str,
        "workgroupName": str,
    },
)
UpdateEndpointAccessRequestRequestTypeDef = TypedDict(
    "UpdateEndpointAccessRequestRequestTypeDef",
    {
        "endpointName": str,
        "vpcSecurityGroupIds": NotRequired[Sequence[str]],
    },
)
UpdateNamespaceRequestRequestTypeDef = TypedDict(
    "UpdateNamespaceRequestRequestTypeDef",
    {
        "namespaceName": str,
        "adminPasswordSecretKmsKeyId": NotRequired[str],
        "adminUserPassword": NotRequired[str],
        "adminUsername": NotRequired[str],
        "defaultIamRoleArn": NotRequired[str],
        "iamRoles": NotRequired[Sequence[str]],
        "kmsKeyId": NotRequired[str],
        "logExports": NotRequired[Sequence[LogExportType]],
        "manageAdminPassword": NotRequired[bool],
    },
)
UpdateSnapshotCopyConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateSnapshotCopyConfigurationRequestRequestTypeDef",
    {
        "snapshotCopyConfigurationId": str,
        "snapshotRetentionPeriod": NotRequired[int],
    },
)
UpdateSnapshotRequestRequestTypeDef = TypedDict(
    "UpdateSnapshotRequestRequestTypeDef",
    {
        "snapshotName": str,
        "retentionPeriod": NotRequired[int],
    },
)
UpdateUsageLimitRequestRequestTypeDef = TypedDict(
    "UpdateUsageLimitRequestRequestTypeDef",
    {
        "usageLimitId": str,
        "amount": NotRequired[int],
        "breachAction": NotRequired[UsageLimitBreachActionType],
    },
)
UpdateWorkgroupRequestRequestTypeDef = TypedDict(
    "UpdateWorkgroupRequestRequestTypeDef",
    {
        "workgroupName": str,
        "baseCapacity": NotRequired[int],
        "configParameters": NotRequired[Sequence[ConfigParameterTypeDef]],
        "enhancedVpcRouting": NotRequired[bool],
        "ipAddressType": NotRequired[str],
        "maxCapacity": NotRequired[int],
        "port": NotRequired[int],
        "publiclyAccessible": NotRequired[bool],
        "securityGroupIds": NotRequired[Sequence[str]],
        "subnetIds": NotRequired[Sequence[str]],
    },
)
ConvertRecoveryPointToSnapshotRequestRequestTypeDef = TypedDict(
    "ConvertRecoveryPointToSnapshotRequestRequestTypeDef",
    {
        "recoveryPointId": str,
        "snapshotName": str,
        "retentionPeriod": NotRequired[int],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateNamespaceRequestRequestTypeDef = TypedDict(
    "CreateNamespaceRequestRequestTypeDef",
    {
        "namespaceName": str,
        "adminPasswordSecretKmsKeyId": NotRequired[str],
        "adminUserPassword": NotRequired[str],
        "adminUsername": NotRequired[str],
        "dbName": NotRequired[str],
        "defaultIamRoleArn": NotRequired[str],
        "iamRoles": NotRequired[Sequence[str]],
        "kmsKeyId": NotRequired[str],
        "logExports": NotRequired[Sequence[LogExportType]],
        "manageAdminPassword": NotRequired[bool],
        "redshiftIdcApplicationArn": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateSnapshotRequestRequestTypeDef = TypedDict(
    "CreateSnapshotRequestRequestTypeDef",
    {
        "namespaceName": str,
        "snapshotName": str,
        "retentionPeriod": NotRequired[int],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateSnapshotScheduleActionParametersOutputTypeDef = TypedDict(
    "CreateSnapshotScheduleActionParametersOutputTypeDef",
    {
        "namespaceName": str,
        "snapshotNamePrefix": str,
        "retentionPeriod": NotRequired[int],
        "tags": NotRequired[List[TagTypeDef]],
    },
)
CreateSnapshotScheduleActionParametersTypeDef = TypedDict(
    "CreateSnapshotScheduleActionParametersTypeDef",
    {
        "namespaceName": str,
        "snapshotNamePrefix": str,
        "retentionPeriod": NotRequired[int],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateWorkgroupRequestRequestTypeDef = TypedDict(
    "CreateWorkgroupRequestRequestTypeDef",
    {
        "namespaceName": str,
        "workgroupName": str,
        "baseCapacity": NotRequired[int],
        "configParameters": NotRequired[Sequence[ConfigParameterTypeDef]],
        "enhancedVpcRouting": NotRequired[bool],
        "ipAddressType": NotRequired[str],
        "maxCapacity": NotRequired[int],
        "port": NotRequired[int],
        "publiclyAccessible": NotRequired[bool],
        "securityGroupIds": NotRequired[Sequence[str]],
        "subnetIds": NotRequired[Sequence[str]],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[TagTypeDef],
    },
)
CreateCustomDomainAssociationResponseTypeDef = TypedDict(
    "CreateCustomDomainAssociationResponseTypeDef",
    {
        "customDomainCertificateArn": str,
        "customDomainCertificateExpiryTime": datetime,
        "customDomainName": str,
        "workgroupName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCredentialsResponseTypeDef = TypedDict(
    "GetCredentialsResponseTypeDef",
    {
        "dbPassword": str,
        "dbUser": str,
        "expiration": datetime,
        "nextRefreshTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCustomDomainAssociationResponseTypeDef = TypedDict(
    "GetCustomDomainAssociationResponseTypeDef",
    {
        "customDomainCertificateArn": str,
        "customDomainCertificateExpiryTime": datetime,
        "customDomainName": str,
        "workgroupName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCustomDomainAssociationsResponseTypeDef = TypedDict(
    "ListCustomDomainAssociationsResponseTypeDef",
    {
        "associations": List[AssociationTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateCustomDomainAssociationResponseTypeDef = TypedDict(
    "UpdateCustomDomainAssociationResponseTypeDef",
    {
        "customDomainCertificateArn": str,
        "customDomainCertificateExpiryTime": datetime,
        "customDomainName": str,
        "workgroupName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConvertRecoveryPointToSnapshotResponseTypeDef = TypedDict(
    "ConvertRecoveryPointToSnapshotResponseTypeDef",
    {
        "snapshot": SnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSnapshotResponseTypeDef = TypedDict(
    "CreateSnapshotResponseTypeDef",
    {
        "snapshot": SnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteSnapshotResponseTypeDef = TypedDict(
    "DeleteSnapshotResponseTypeDef",
    {
        "snapshot": SnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSnapshotResponseTypeDef = TypedDict(
    "GetSnapshotResponseTypeDef",
    {
        "snapshot": SnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSnapshotsResponseTypeDef = TypedDict(
    "ListSnapshotsResponseTypeDef",
    {
        "nextToken": str,
        "snapshots": List[SnapshotTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSnapshotResponseTypeDef = TypedDict(
    "UpdateSnapshotResponseTypeDef",
    {
        "snapshot": SnapshotTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateNamespaceResponseTypeDef = TypedDict(
    "CreateNamespaceResponseTypeDef",
    {
        "namespace": NamespaceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteNamespaceResponseTypeDef = TypedDict(
    "DeleteNamespaceResponseTypeDef",
    {
        "namespace": NamespaceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetNamespaceResponseTypeDef = TypedDict(
    "GetNamespaceResponseTypeDef",
    {
        "namespace": NamespaceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListNamespacesResponseTypeDef = TypedDict(
    "ListNamespacesResponseTypeDef",
    {
        "namespaces": List[NamespaceTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreFromRecoveryPointResponseTypeDef = TypedDict(
    "RestoreFromRecoveryPointResponseTypeDef",
    {
        "namespace": NamespaceTypeDef,
        "recoveryPointId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreFromSnapshotResponseTypeDef = TypedDict(
    "RestoreFromSnapshotResponseTypeDef",
    {
        "namespace": NamespaceTypeDef,
        "ownerAccount": str,
        "snapshotName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateNamespaceResponseTypeDef = TypedDict(
    "UpdateNamespaceResponseTypeDef",
    {
        "namespace": NamespaceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRecoveryPointsRequestRequestTypeDef = TypedDict(
    "ListRecoveryPointsRequestRequestTypeDef",
    {
        "endTime": NotRequired[TimestampTypeDef],
        "maxResults": NotRequired[int],
        "namespaceArn": NotRequired[str],
        "namespaceName": NotRequired[str],
        "nextToken": NotRequired[str],
        "startTime": NotRequired[TimestampTypeDef],
    },
)
ListSnapshotsRequestRequestTypeDef = TypedDict(
    "ListSnapshotsRequestRequestTypeDef",
    {
        "endTime": NotRequired[TimestampTypeDef],
        "maxResults": NotRequired[int],
        "namespaceArn": NotRequired[str],
        "namespaceName": NotRequired[str],
        "nextToken": NotRequired[str],
        "ownerAccount": NotRequired[str],
        "startTime": NotRequired[TimestampTypeDef],
    },
)
ScheduleTypeDef = TypedDict(
    "ScheduleTypeDef",
    {
        "at": NotRequired[TimestampTypeDef],
        "cron": NotRequired[str],
    },
)
CreateSnapshotCopyConfigurationResponseTypeDef = TypedDict(
    "CreateSnapshotCopyConfigurationResponseTypeDef",
    {
        "snapshotCopyConfiguration": SnapshotCopyConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteSnapshotCopyConfigurationResponseTypeDef = TypedDict(
    "DeleteSnapshotCopyConfigurationResponseTypeDef",
    {
        "snapshotCopyConfiguration": SnapshotCopyConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSnapshotCopyConfigurationsResponseTypeDef = TypedDict(
    "ListSnapshotCopyConfigurationsResponseTypeDef",
    {
        "nextToken": str,
        "snapshotCopyConfigurations": List[SnapshotCopyConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSnapshotCopyConfigurationResponseTypeDef = TypedDict(
    "UpdateSnapshotCopyConfigurationResponseTypeDef",
    {
        "snapshotCopyConfiguration": SnapshotCopyConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateUsageLimitResponseTypeDef = TypedDict(
    "CreateUsageLimitResponseTypeDef",
    {
        "usageLimit": UsageLimitTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteUsageLimitResponseTypeDef = TypedDict(
    "DeleteUsageLimitResponseTypeDef",
    {
        "usageLimit": UsageLimitTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetUsageLimitResponseTypeDef = TypedDict(
    "GetUsageLimitResponseTypeDef",
    {
        "usageLimit": UsageLimitTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListUsageLimitsResponseTypeDef = TypedDict(
    "ListUsageLimitsResponseTypeDef",
    {
        "nextToken": str,
        "usageLimits": List[UsageLimitTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateUsageLimitResponseTypeDef = TypedDict(
    "UpdateUsageLimitResponseTypeDef",
    {
        "usageLimit": UsageLimitTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRecoveryPointResponseTypeDef = TypedDict(
    "GetRecoveryPointResponseTypeDef",
    {
        "recoveryPoint": RecoveryPointTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRecoveryPointsResponseTypeDef = TypedDict(
    "ListRecoveryPointsResponseTypeDef",
    {
        "nextToken": str,
        "recoveryPoints": List[RecoveryPointTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResourcePolicyResponseTypeDef = TypedDict(
    "GetResourcePolicyResponseTypeDef",
    {
        "resourcePolicy": ResourcePolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutResourcePolicyResponseTypeDef = TypedDict(
    "PutResourcePolicyResponseTypeDef",
    {
        "resourcePolicy": ResourcePolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTableRestoreStatusResponseTypeDef = TypedDict(
    "GetTableRestoreStatusResponseTypeDef",
    {
        "tableRestoreStatus": TableRestoreStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTableRestoreStatusResponseTypeDef = TypedDict(
    "ListTableRestoreStatusResponseTypeDef",
    {
        "nextToken": str,
        "tableRestoreStatuses": List[TableRestoreStatusTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreTableFromRecoveryPointResponseTypeDef = TypedDict(
    "RestoreTableFromRecoveryPointResponseTypeDef",
    {
        "tableRestoreStatus": TableRestoreStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreTableFromSnapshotResponseTypeDef = TypedDict(
    "RestoreTableFromSnapshotResponseTypeDef",
    {
        "tableRestoreStatus": TableRestoreStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCustomDomainAssociationsRequestListCustomDomainAssociationsPaginateTypeDef = TypedDict(
    "ListCustomDomainAssociationsRequestListCustomDomainAssociationsPaginateTypeDef",
    {
        "customDomainCertificateArn": NotRequired[str],
        "customDomainName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEndpointAccessRequestListEndpointAccessPaginateTypeDef = TypedDict(
    "ListEndpointAccessRequestListEndpointAccessPaginateTypeDef",
    {
        "ownerAccount": NotRequired[str],
        "vpcId": NotRequired[str],
        "workgroupName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListNamespacesRequestListNamespacesPaginateTypeDef = TypedDict(
    "ListNamespacesRequestListNamespacesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRecoveryPointsRequestListRecoveryPointsPaginateTypeDef = TypedDict(
    "ListRecoveryPointsRequestListRecoveryPointsPaginateTypeDef",
    {
        "endTime": NotRequired[TimestampTypeDef],
        "namespaceArn": NotRequired[str],
        "namespaceName": NotRequired[str],
        "startTime": NotRequired[TimestampTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListScheduledActionsRequestListScheduledActionsPaginateTypeDef = TypedDict(
    "ListScheduledActionsRequestListScheduledActionsPaginateTypeDef",
    {
        "namespaceName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSnapshotCopyConfigurationsRequestListSnapshotCopyConfigurationsPaginateTypeDef = TypedDict(
    "ListSnapshotCopyConfigurationsRequestListSnapshotCopyConfigurationsPaginateTypeDef",
    {
        "namespaceName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSnapshotsRequestListSnapshotsPaginateTypeDef = TypedDict(
    "ListSnapshotsRequestListSnapshotsPaginateTypeDef",
    {
        "endTime": NotRequired[TimestampTypeDef],
        "namespaceArn": NotRequired[str],
        "namespaceName": NotRequired[str],
        "ownerAccount": NotRequired[str],
        "startTime": NotRequired[TimestampTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTableRestoreStatusRequestListTableRestoreStatusPaginateTypeDef = TypedDict(
    "ListTableRestoreStatusRequestListTableRestoreStatusPaginateTypeDef",
    {
        "namespaceName": NotRequired[str],
        "workgroupName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListUsageLimitsRequestListUsageLimitsPaginateTypeDef = TypedDict(
    "ListUsageLimitsRequestListUsageLimitsPaginateTypeDef",
    {
        "resourceArn": NotRequired[str],
        "usageType": NotRequired[UsageLimitUsageTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWorkgroupsRequestListWorkgroupsPaginateTypeDef = TypedDict(
    "ListWorkgroupsRequestListWorkgroupsPaginateTypeDef",
    {
        "ownerAccount": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListScheduledActionsResponseTypeDef = TypedDict(
    "ListScheduledActionsResponseTypeDef",
    {
        "nextToken": str,
        "scheduledActions": List[ScheduledActionAssociationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VpcEndpointTypeDef = TypedDict(
    "VpcEndpointTypeDef",
    {
        "networkInterfaces": NotRequired[List[NetworkInterfaceTypeDef]],
        "vpcEndpointId": NotRequired[str],
        "vpcId": NotRequired[str],
    },
)
TargetActionOutputTypeDef = TypedDict(
    "TargetActionOutputTypeDef",
    {
        "createSnapshot": NotRequired[CreateSnapshotScheduleActionParametersOutputTypeDef],
    },
)
CreateSnapshotScheduleActionParametersUnionTypeDef = Union[
    CreateSnapshotScheduleActionParametersTypeDef,
    CreateSnapshotScheduleActionParametersOutputTypeDef,
]
EndpointAccessTypeDef = TypedDict(
    "EndpointAccessTypeDef",
    {
        "address": NotRequired[str],
        "endpointArn": NotRequired[str],
        "endpointCreateTime": NotRequired[datetime],
        "endpointName": NotRequired[str],
        "endpointStatus": NotRequired[str],
        "port": NotRequired[int],
        "subnetIds": NotRequired[List[str]],
        "vpcEndpoint": NotRequired[VpcEndpointTypeDef],
        "vpcSecurityGroups": NotRequired[List[VpcSecurityGroupMembershipTypeDef]],
        "workgroupName": NotRequired[str],
    },
)
EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "address": NotRequired[str],
        "port": NotRequired[int],
        "vpcEndpoints": NotRequired[List[VpcEndpointTypeDef]],
    },
)
ScheduledActionResponseTypeDef = TypedDict(
    "ScheduledActionResponseTypeDef",
    {
        "endTime": NotRequired[datetime],
        "namespaceName": NotRequired[str],
        "nextInvocations": NotRequired[List[datetime]],
        "roleArn": NotRequired[str],
        "schedule": NotRequired[ScheduleOutputTypeDef],
        "scheduledActionDescription": NotRequired[str],
        "scheduledActionName": NotRequired[str],
        "scheduledActionUuid": NotRequired[str],
        "startTime": NotRequired[datetime],
        "state": NotRequired[StateType],
        "targetAction": NotRequired[TargetActionOutputTypeDef],
    },
)
TargetActionTypeDef = TypedDict(
    "TargetActionTypeDef",
    {
        "createSnapshot": NotRequired[CreateSnapshotScheduleActionParametersUnionTypeDef],
    },
)
CreateEndpointAccessResponseTypeDef = TypedDict(
    "CreateEndpointAccessResponseTypeDef",
    {
        "endpoint": EndpointAccessTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteEndpointAccessResponseTypeDef = TypedDict(
    "DeleteEndpointAccessResponseTypeDef",
    {
        "endpoint": EndpointAccessTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEndpointAccessResponseTypeDef = TypedDict(
    "GetEndpointAccessResponseTypeDef",
    {
        "endpoint": EndpointAccessTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEndpointAccessResponseTypeDef = TypedDict(
    "ListEndpointAccessResponseTypeDef",
    {
        "endpoints": List[EndpointAccessTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEndpointAccessResponseTypeDef = TypedDict(
    "UpdateEndpointAccessResponseTypeDef",
    {
        "endpoint": EndpointAccessTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
WorkgroupTypeDef = TypedDict(
    "WorkgroupTypeDef",
    {
        "baseCapacity": NotRequired[int],
        "configParameters": NotRequired[List[ConfigParameterTypeDef]],
        "creationDate": NotRequired[datetime],
        "crossAccountVpcs": NotRequired[List[str]],
        "customDomainCertificateArn": NotRequired[str],
        "customDomainCertificateExpiryTime": NotRequired[datetime],
        "customDomainName": NotRequired[str],
        "endpoint": NotRequired[EndpointTypeDef],
        "enhancedVpcRouting": NotRequired[bool],
        "ipAddressType": NotRequired[str],
        "maxCapacity": NotRequired[int],
        "namespaceName": NotRequired[str],
        "patchVersion": NotRequired[str],
        "port": NotRequired[int],
        "publiclyAccessible": NotRequired[bool],
        "securityGroupIds": NotRequired[List[str]],
        "status": NotRequired[WorkgroupStatusType],
        "subnetIds": NotRequired[List[str]],
        "workgroupArn": NotRequired[str],
        "workgroupId": NotRequired[str],
        "workgroupName": NotRequired[str],
        "workgroupVersion": NotRequired[str],
    },
)
CreateScheduledActionResponseTypeDef = TypedDict(
    "CreateScheduledActionResponseTypeDef",
    {
        "scheduledAction": ScheduledActionResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteScheduledActionResponseTypeDef = TypedDict(
    "DeleteScheduledActionResponseTypeDef",
    {
        "scheduledAction": ScheduledActionResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetScheduledActionResponseTypeDef = TypedDict(
    "GetScheduledActionResponseTypeDef",
    {
        "scheduledAction": ScheduledActionResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateScheduledActionResponseTypeDef = TypedDict(
    "UpdateScheduledActionResponseTypeDef",
    {
        "scheduledAction": ScheduledActionResponseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateScheduledActionRequestRequestTypeDef = TypedDict(
    "CreateScheduledActionRequestRequestTypeDef",
    {
        "namespaceName": str,
        "roleArn": str,
        "schedule": ScheduleTypeDef,
        "scheduledActionName": str,
        "targetAction": TargetActionTypeDef,
        "enabled": NotRequired[bool],
        "endTime": NotRequired[TimestampTypeDef],
        "scheduledActionDescription": NotRequired[str],
        "startTime": NotRequired[TimestampTypeDef],
    },
)
UpdateScheduledActionRequestRequestTypeDef = TypedDict(
    "UpdateScheduledActionRequestRequestTypeDef",
    {
        "scheduledActionName": str,
        "enabled": NotRequired[bool],
        "endTime": NotRequired[TimestampTypeDef],
        "roleArn": NotRequired[str],
        "schedule": NotRequired[ScheduleTypeDef],
        "scheduledActionDescription": NotRequired[str],
        "startTime": NotRequired[TimestampTypeDef],
        "targetAction": NotRequired[TargetActionTypeDef],
    },
)
CreateWorkgroupResponseTypeDef = TypedDict(
    "CreateWorkgroupResponseTypeDef",
    {
        "workgroup": WorkgroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteWorkgroupResponseTypeDef = TypedDict(
    "DeleteWorkgroupResponseTypeDef",
    {
        "workgroup": WorkgroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetWorkgroupResponseTypeDef = TypedDict(
    "GetWorkgroupResponseTypeDef",
    {
        "workgroup": WorkgroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListWorkgroupsResponseTypeDef = TypedDict(
    "ListWorkgroupsResponseTypeDef",
    {
        "nextToken": str,
        "workgroups": List[WorkgroupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateWorkgroupResponseTypeDef = TypedDict(
    "UpdateWorkgroupResponseTypeDef",
    {
        "workgroup": WorkgroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
