"""
Type annotations for ssm-quicksetup service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_quicksetup/type_defs/)

Usage::

    ```python
    from mypy_boto3_ssm_quicksetup.type_defs import ConfigurationDefinitionInputTypeDef

    data: ConfigurationDefinitionInputTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import StatusType, StatusTypeType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "ConfigurationDefinitionInputTypeDef",
    "ConfigurationDefinitionSummaryTypeDef",
    "ConfigurationDefinitionTypeDef",
    "StatusSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "DeleteConfigurationManagerInputRequestTypeDef",
    "FilterTypeDef",
    "GetConfigurationManagerInputRequestTypeDef",
    "ServiceSettingsTypeDef",
    "PaginatorConfigTypeDef",
    "QuickSetupTypeOutputTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagEntryTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateConfigurationDefinitionInputRequestTypeDef",
    "UpdateConfigurationManagerInputRequestTypeDef",
    "UpdateServiceSettingsInputRequestTypeDef",
    "CreateConfigurationManagerInputRequestTypeDef",
    "ConfigurationManagerSummaryTypeDef",
    "CreateConfigurationManagerOutputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetConfigurationManagerOutputTypeDef",
    "ListConfigurationManagersInputRequestTypeDef",
    "GetServiceSettingsOutputTypeDef",
    "ListConfigurationManagersInputListConfigurationManagersPaginateTypeDef",
    "ListQuickSetupTypesOutputTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListConfigurationManagersOutputTypeDef",
)

ConfigurationDefinitionInputTypeDef = TypedDict(
    "ConfigurationDefinitionInputTypeDef",
    {
        "Parameters": Mapping[str, str],
        "Type": str,
        "LocalDeploymentAdministrationRoleArn": NotRequired[str],
        "LocalDeploymentExecutionRoleName": NotRequired[str],
        "TypeVersion": NotRequired[str],
    },
)
ConfigurationDefinitionSummaryTypeDef = TypedDict(
    "ConfigurationDefinitionSummaryTypeDef",
    {
        "FirstClassParameters": NotRequired[Dict[str, str]],
        "Id": NotRequired[str],
        "Type": NotRequired[str],
        "TypeVersion": NotRequired[str],
    },
)
ConfigurationDefinitionTypeDef = TypedDict(
    "ConfigurationDefinitionTypeDef",
    {
        "Parameters": Dict[str, str],
        "Type": str,
        "Id": NotRequired[str],
        "LocalDeploymentAdministrationRoleArn": NotRequired[str],
        "LocalDeploymentExecutionRoleName": NotRequired[str],
        "TypeVersion": NotRequired[str],
    },
)
StatusSummaryTypeDef = TypedDict(
    "StatusSummaryTypeDef",
    {
        "LastUpdatedAt": datetime,
        "StatusType": StatusTypeType,
        "Status": NotRequired[StatusType],
        "StatusDetails": NotRequired[Dict[str, str]],
        "StatusMessage": NotRequired[str],
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
DeleteConfigurationManagerInputRequestTypeDef = TypedDict(
    "DeleteConfigurationManagerInputRequestTypeDef",
    {
        "ManagerArn": str,
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Key": str,
        "Values": Sequence[str],
    },
)
GetConfigurationManagerInputRequestTypeDef = TypedDict(
    "GetConfigurationManagerInputRequestTypeDef",
    {
        "ManagerArn": str,
    },
)
ServiceSettingsTypeDef = TypedDict(
    "ServiceSettingsTypeDef",
    {
        "ExplorerEnablingRoleArn": NotRequired[str],
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
QuickSetupTypeOutputTypeDef = TypedDict(
    "QuickSetupTypeOutputTypeDef",
    {
        "LatestVersion": NotRequired[str],
        "Type": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
TagEntryTypeDef = TypedDict(
    "TagEntryTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateConfigurationDefinitionInputRequestTypeDef = TypedDict(
    "UpdateConfigurationDefinitionInputRequestTypeDef",
    {
        "Id": str,
        "ManagerArn": str,
        "LocalDeploymentAdministrationRoleArn": NotRequired[str],
        "LocalDeploymentExecutionRoleName": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, str]],
        "TypeVersion": NotRequired[str],
    },
)
UpdateConfigurationManagerInputRequestTypeDef = TypedDict(
    "UpdateConfigurationManagerInputRequestTypeDef",
    {
        "ManagerArn": str,
        "Description": NotRequired[str],
        "Name": NotRequired[str],
    },
)
UpdateServiceSettingsInputRequestTypeDef = TypedDict(
    "UpdateServiceSettingsInputRequestTypeDef",
    {
        "ExplorerEnablingRoleArn": NotRequired[str],
    },
)
CreateConfigurationManagerInputRequestTypeDef = TypedDict(
    "CreateConfigurationManagerInputRequestTypeDef",
    {
        "ConfigurationDefinitions": Sequence[ConfigurationDefinitionInputTypeDef],
        "Description": NotRequired[str],
        "Name": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
ConfigurationManagerSummaryTypeDef = TypedDict(
    "ConfigurationManagerSummaryTypeDef",
    {
        "ManagerArn": str,
        "ConfigurationDefinitionSummaries": NotRequired[
            List[ConfigurationDefinitionSummaryTypeDef]
        ],
        "Description": NotRequired[str],
        "Name": NotRequired[str],
        "StatusSummaries": NotRequired[List[StatusSummaryTypeDef]],
    },
)
CreateConfigurationManagerOutputTypeDef = TypedDict(
    "CreateConfigurationManagerOutputTypeDef",
    {
        "ManagerArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetConfigurationManagerOutputTypeDef = TypedDict(
    "GetConfigurationManagerOutputTypeDef",
    {
        "ConfigurationDefinitions": List[ConfigurationDefinitionTypeDef],
        "CreatedAt": datetime,
        "Description": str,
        "LastModifiedAt": datetime,
        "ManagerArn": str,
        "Name": str,
        "StatusSummaries": List[StatusSummaryTypeDef],
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListConfigurationManagersInputRequestTypeDef = TypedDict(
    "ListConfigurationManagersInputRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "MaxItems": NotRequired[int],
        "StartingToken": NotRequired[str],
    },
)
GetServiceSettingsOutputTypeDef = TypedDict(
    "GetServiceSettingsOutputTypeDef",
    {
        "ServiceSettings": ServiceSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListConfigurationManagersInputListConfigurationManagersPaginateTypeDef = TypedDict(
    "ListConfigurationManagersInputListConfigurationManagersPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListQuickSetupTypesOutputTypeDef = TypedDict(
    "ListQuickSetupTypesOutputTypeDef",
    {
        "QuickSetupTypeList": List[QuickSetupTypeOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListConfigurationManagersOutputTypeDef = TypedDict(
    "ListConfigurationManagersOutputTypeDef",
    {
        "ConfigurationManagersList": List[ConfigurationManagerSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
