"""
Type annotations for opsworkscm service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/type_defs/)

Usage::

    ```python
    from mypy_boto3_opsworkscm.type_defs import AccountAttributeTypeDef

    data: AccountAttributeTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import (
    BackupStatusType,
    BackupTypeType,
    MaintenanceStatusType,
    NodeAssociationStatusType,
    ServerStatusType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "AccountAttributeTypeDef",
    "EngineAttributeTypeDef",
    "ResponseMetadataTypeDef",
    "BackupTypeDef",
    "TagTypeDef",
    "DeleteBackupRequestRequestTypeDef",
    "DeleteServerRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeBackupsRequestRequestTypeDef",
    "DescribeEventsRequestRequestTypeDef",
    "ServerEventTypeDef",
    "WaiterConfigTypeDef",
    "DescribeNodeAssociationStatusRequestRequestTypeDef",
    "DescribeServersRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "RestoreServerRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateServerEngineAttributesRequestRequestTypeDef",
    "UpdateServerRequestRequestTypeDef",
    "AssociateNodeRequestRequestTypeDef",
    "DisassociateNodeRequestRequestTypeDef",
    "ExportServerEngineAttributeRequestRequestTypeDef",
    "ServerTypeDef",
    "StartMaintenanceRequestRequestTypeDef",
    "AssociateNodeResponseTypeDef",
    "DescribeAccountAttributesResponseTypeDef",
    "DescribeNodeAssociationStatusResponseTypeDef",
    "DisassociateNodeResponseTypeDef",
    "ExportServerEngineAttributeResponseTypeDef",
    "CreateBackupResponseTypeDef",
    "DescribeBackupsResponseTypeDef",
    "CreateBackupRequestRequestTypeDef",
    "CreateServerRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "DescribeBackupsRequestDescribeBackupsPaginateTypeDef",
    "DescribeEventsRequestDescribeEventsPaginateTypeDef",
    "DescribeServersRequestDescribeServersPaginateTypeDef",
    "ListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    "DescribeEventsResponseTypeDef",
    "DescribeNodeAssociationStatusRequestNodeAssociatedWaitTypeDef",
    "CreateServerResponseTypeDef",
    "DescribeServersResponseTypeDef",
    "RestoreServerResponseTypeDef",
    "StartMaintenanceResponseTypeDef",
    "UpdateServerEngineAttributesResponseTypeDef",
    "UpdateServerResponseTypeDef",
)

AccountAttributeTypeDef = TypedDict(
    "AccountAttributeTypeDef",
    {
        "Name": NotRequired[str],
        "Maximum": NotRequired[int],
        "Used": NotRequired[int],
    },
)
EngineAttributeTypeDef = TypedDict(
    "EngineAttributeTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
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
BackupTypeDef = TypedDict(
    "BackupTypeDef",
    {
        "BackupArn": NotRequired[str],
        "BackupId": NotRequired[str],
        "BackupType": NotRequired[BackupTypeType],
        "CreatedAt": NotRequired[datetime],
        "Description": NotRequired[str],
        "Engine": NotRequired[str],
        "EngineModel": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "InstanceProfileArn": NotRequired[str],
        "InstanceType": NotRequired[str],
        "KeyPair": NotRequired[str],
        "PreferredBackupWindow": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "S3DataSize": NotRequired[int],
        "S3DataUrl": NotRequired[str],
        "S3LogUrl": NotRequired[str],
        "SecurityGroupIds": NotRequired[List[str]],
        "ServerName": NotRequired[str],
        "ServiceRoleArn": NotRequired[str],
        "Status": NotRequired[BackupStatusType],
        "StatusDescription": NotRequired[str],
        "SubnetIds": NotRequired[List[str]],
        "ToolsVersion": NotRequired[str],
        "UserArn": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
DeleteBackupRequestRequestTypeDef = TypedDict(
    "DeleteBackupRequestRequestTypeDef",
    {
        "BackupId": str,
    },
)
DeleteServerRequestRequestTypeDef = TypedDict(
    "DeleteServerRequestRequestTypeDef",
    {
        "ServerName": str,
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
DescribeBackupsRequestRequestTypeDef = TypedDict(
    "DescribeBackupsRequestRequestTypeDef",
    {
        "BackupId": NotRequired[str],
        "ServerName": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeEventsRequestRequestTypeDef = TypedDict(
    "DescribeEventsRequestRequestTypeDef",
    {
        "ServerName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ServerEventTypeDef = TypedDict(
    "ServerEventTypeDef",
    {
        "CreatedAt": NotRequired[datetime],
        "ServerName": NotRequired[str],
        "Message": NotRequired[str],
        "LogUrl": NotRequired[str],
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
DescribeNodeAssociationStatusRequestRequestTypeDef = TypedDict(
    "DescribeNodeAssociationStatusRequestRequestTypeDef",
    {
        "NodeAssociationStatusToken": str,
        "ServerName": str,
    },
)
DescribeServersRequestRequestTypeDef = TypedDict(
    "DescribeServersRequestRequestTypeDef",
    {
        "ServerName": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
RestoreServerRequestRequestTypeDef = TypedDict(
    "RestoreServerRequestRequestTypeDef",
    {
        "BackupId": str,
        "ServerName": str,
        "InstanceType": NotRequired[str],
        "KeyPair": NotRequired[str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateServerEngineAttributesRequestRequestTypeDef = TypedDict(
    "UpdateServerEngineAttributesRequestRequestTypeDef",
    {
        "ServerName": str,
        "AttributeName": str,
        "AttributeValue": NotRequired[str],
    },
)
UpdateServerRequestRequestTypeDef = TypedDict(
    "UpdateServerRequestRequestTypeDef",
    {
        "ServerName": str,
        "DisableAutomatedBackup": NotRequired[bool],
        "BackupRetentionCount": NotRequired[int],
        "PreferredMaintenanceWindow": NotRequired[str],
        "PreferredBackupWindow": NotRequired[str],
    },
)
AssociateNodeRequestRequestTypeDef = TypedDict(
    "AssociateNodeRequestRequestTypeDef",
    {
        "ServerName": str,
        "NodeName": str,
        "EngineAttributes": Sequence[EngineAttributeTypeDef],
    },
)
DisassociateNodeRequestRequestTypeDef = TypedDict(
    "DisassociateNodeRequestRequestTypeDef",
    {
        "ServerName": str,
        "NodeName": str,
        "EngineAttributes": NotRequired[Sequence[EngineAttributeTypeDef]],
    },
)
ExportServerEngineAttributeRequestRequestTypeDef = TypedDict(
    "ExportServerEngineAttributeRequestRequestTypeDef",
    {
        "ExportAttributeName": str,
        "ServerName": str,
        "InputAttributes": NotRequired[Sequence[EngineAttributeTypeDef]],
    },
)
ServerTypeDef = TypedDict(
    "ServerTypeDef",
    {
        "AssociatePublicIpAddress": NotRequired[bool],
        "BackupRetentionCount": NotRequired[int],
        "ServerName": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "CloudFormationStackArn": NotRequired[str],
        "CustomDomain": NotRequired[str],
        "DisableAutomatedBackup": NotRequired[bool],
        "Endpoint": NotRequired[str],
        "Engine": NotRequired[str],
        "EngineModel": NotRequired[str],
        "EngineAttributes": NotRequired[List[EngineAttributeTypeDef]],
        "EngineVersion": NotRequired[str],
        "InstanceProfileArn": NotRequired[str],
        "InstanceType": NotRequired[str],
        "KeyPair": NotRequired[str],
        "MaintenanceStatus": NotRequired[MaintenanceStatusType],
        "PreferredMaintenanceWindow": NotRequired[str],
        "PreferredBackupWindow": NotRequired[str],
        "SecurityGroupIds": NotRequired[List[str]],
        "ServiceRoleArn": NotRequired[str],
        "Status": NotRequired[ServerStatusType],
        "StatusReason": NotRequired[str],
        "SubnetIds": NotRequired[List[str]],
        "ServerArn": NotRequired[str],
    },
)
StartMaintenanceRequestRequestTypeDef = TypedDict(
    "StartMaintenanceRequestRequestTypeDef",
    {
        "ServerName": str,
        "EngineAttributes": NotRequired[Sequence[EngineAttributeTypeDef]],
    },
)
AssociateNodeResponseTypeDef = TypedDict(
    "AssociateNodeResponseTypeDef",
    {
        "NodeAssociationStatusToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAccountAttributesResponseTypeDef = TypedDict(
    "DescribeAccountAttributesResponseTypeDef",
    {
        "Attributes": List[AccountAttributeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeNodeAssociationStatusResponseTypeDef = TypedDict(
    "DescribeNodeAssociationStatusResponseTypeDef",
    {
        "NodeAssociationStatus": NodeAssociationStatusType,
        "EngineAttributes": List[EngineAttributeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateNodeResponseTypeDef = TypedDict(
    "DisassociateNodeResponseTypeDef",
    {
        "NodeAssociationStatusToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportServerEngineAttributeResponseTypeDef = TypedDict(
    "ExportServerEngineAttributeResponseTypeDef",
    {
        "EngineAttribute": EngineAttributeTypeDef,
        "ServerName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateBackupResponseTypeDef = TypedDict(
    "CreateBackupResponseTypeDef",
    {
        "Backup": BackupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeBackupsResponseTypeDef = TypedDict(
    "DescribeBackupsResponseTypeDef",
    {
        "Backups": List[BackupTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateBackupRequestRequestTypeDef = TypedDict(
    "CreateBackupRequestRequestTypeDef",
    {
        "ServerName": str,
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateServerRequestRequestTypeDef = TypedDict(
    "CreateServerRequestRequestTypeDef",
    {
        "Engine": str,
        "ServerName": str,
        "InstanceProfileArn": str,
        "InstanceType": str,
        "ServiceRoleArn": str,
        "AssociatePublicIpAddress": NotRequired[bool],
        "CustomDomain": NotRequired[str],
        "CustomCertificate": NotRequired[str],
        "CustomPrivateKey": NotRequired[str],
        "DisableAutomatedBackup": NotRequired[bool],
        "EngineModel": NotRequired[str],
        "EngineVersion": NotRequired[str],
        "EngineAttributes": NotRequired[Sequence[EngineAttributeTypeDef]],
        "BackupRetentionCount": NotRequired[int],
        "KeyPair": NotRequired[str],
        "PreferredMaintenanceWindow": NotRequired[str],
        "PreferredBackupWindow": NotRequired[str],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "SubnetIds": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "BackupId": NotRequired[str],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
DescribeBackupsRequestDescribeBackupsPaginateTypeDef = TypedDict(
    "DescribeBackupsRequestDescribeBackupsPaginateTypeDef",
    {
        "BackupId": NotRequired[str],
        "ServerName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEventsRequestDescribeEventsPaginateTypeDef = TypedDict(
    "DescribeEventsRequestDescribeEventsPaginateTypeDef",
    {
        "ServerName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeServersRequestDescribeServersPaginateTypeDef = TypedDict(
    "DescribeServersRequestDescribeServersPaginateTypeDef",
    {
        "ServerName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTagsForResourceRequestListTagsForResourcePaginateTypeDef = TypedDict(
    "ListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    {
        "ResourceArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEventsResponseTypeDef = TypedDict(
    "DescribeEventsResponseTypeDef",
    {
        "ServerEvents": List[ServerEventTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeNodeAssociationStatusRequestNodeAssociatedWaitTypeDef = TypedDict(
    "DescribeNodeAssociationStatusRequestNodeAssociatedWaitTypeDef",
    {
        "NodeAssociationStatusToken": str,
        "ServerName": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
CreateServerResponseTypeDef = TypedDict(
    "CreateServerResponseTypeDef",
    {
        "Server": ServerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeServersResponseTypeDef = TypedDict(
    "DescribeServersResponseTypeDef",
    {
        "Servers": List[ServerTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
RestoreServerResponseTypeDef = TypedDict(
    "RestoreServerResponseTypeDef",
    {
        "Server": ServerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartMaintenanceResponseTypeDef = TypedDict(
    "StartMaintenanceResponseTypeDef",
    {
        "Server": ServerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateServerEngineAttributesResponseTypeDef = TypedDict(
    "UpdateServerEngineAttributesResponseTypeDef",
    {
        "Server": ServerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateServerResponseTypeDef = TypedDict(
    "UpdateServerResponseTypeDef",
    {
        "Server": ServerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
