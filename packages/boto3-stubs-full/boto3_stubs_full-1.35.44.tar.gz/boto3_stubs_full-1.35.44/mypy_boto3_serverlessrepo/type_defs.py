"""
Type annotations for serverlessrepo service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/type_defs/)

Usage::

    ```python
    from mypy_boto3_serverlessrepo.type_defs import ApplicationDependencySummaryTypeDef

    data: ApplicationDependencySummaryTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Sequence, Union

from .literals import CapabilityType, StatusType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "ApplicationDependencySummaryTypeDef",
    "ApplicationPolicyStatementOutputTypeDef",
    "ApplicationPolicyStatementTypeDef",
    "ApplicationSummaryTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CreateApplicationVersionRequestRequestTypeDef",
    "ParameterDefinitionTypeDef",
    "ParameterValueTypeDef",
    "TagTypeDef",
    "CreateCloudFormationTemplateRequestRequestTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "GetApplicationPolicyRequestRequestTypeDef",
    "GetApplicationRequestRequestTypeDef",
    "GetCloudFormationTemplateRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListApplicationDependenciesRequestRequestTypeDef",
    "ListApplicationVersionsRequestRequestTypeDef",
    "VersionSummaryTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "RollbackTriggerTypeDef",
    "UnshareApplicationRequestRequestTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
    "ApplicationPolicyStatementUnionTypeDef",
    "CreateCloudFormationChangeSetResponseTypeDef",
    "CreateCloudFormationTemplateResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetApplicationPolicyResponseTypeDef",
    "GetCloudFormationTemplateResponseTypeDef",
    "ListApplicationDependenciesResponseTypeDef",
    "ListApplicationsResponseTypeDef",
    "PutApplicationPolicyResponseTypeDef",
    "CreateApplicationVersionResponseTypeDef",
    "VersionTypeDef",
    "ListApplicationDependenciesRequestListApplicationDependenciesPaginateTypeDef",
    "ListApplicationVersionsRequestListApplicationVersionsPaginateTypeDef",
    "ListApplicationsRequestListApplicationsPaginateTypeDef",
    "ListApplicationVersionsResponseTypeDef",
    "RollbackConfigurationTypeDef",
    "PutApplicationPolicyRequestRequestTypeDef",
    "CreateApplicationResponseTypeDef",
    "GetApplicationResponseTypeDef",
    "UpdateApplicationResponseTypeDef",
    "CreateCloudFormationChangeSetRequestRequestTypeDef",
)

ApplicationDependencySummaryTypeDef = TypedDict(
    "ApplicationDependencySummaryTypeDef",
    {
        "ApplicationId": str,
        "SemanticVersion": str,
    },
)
ApplicationPolicyStatementOutputTypeDef = TypedDict(
    "ApplicationPolicyStatementOutputTypeDef",
    {
        "Actions": List[str],
        "Principals": List[str],
        "PrincipalOrgIDs": NotRequired[List[str]],
        "StatementId": NotRequired[str],
    },
)
ApplicationPolicyStatementTypeDef = TypedDict(
    "ApplicationPolicyStatementTypeDef",
    {
        "Actions": Sequence[str],
        "Principals": Sequence[str],
        "PrincipalOrgIDs": NotRequired[Sequence[str]],
        "StatementId": NotRequired[str],
    },
)
ApplicationSummaryTypeDef = TypedDict(
    "ApplicationSummaryTypeDef",
    {
        "ApplicationId": str,
        "Author": str,
        "Description": str,
        "Name": str,
        "CreationTime": NotRequired[str],
        "HomePageUrl": NotRequired[str],
        "Labels": NotRequired[List[str]],
        "SpdxLicenseId": NotRequired[str],
    },
)
CreateApplicationRequestRequestTypeDef = TypedDict(
    "CreateApplicationRequestRequestTypeDef",
    {
        "Author": str,
        "Description": str,
        "Name": str,
        "HomePageUrl": NotRequired[str],
        "Labels": NotRequired[Sequence[str]],
        "LicenseBody": NotRequired[str],
        "LicenseUrl": NotRequired[str],
        "ReadmeBody": NotRequired[str],
        "ReadmeUrl": NotRequired[str],
        "SemanticVersion": NotRequired[str],
        "SourceCodeArchiveUrl": NotRequired[str],
        "SourceCodeUrl": NotRequired[str],
        "SpdxLicenseId": NotRequired[str],
        "TemplateBody": NotRequired[str],
        "TemplateUrl": NotRequired[str],
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
CreateApplicationVersionRequestRequestTypeDef = TypedDict(
    "CreateApplicationVersionRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "SemanticVersion": str,
        "SourceCodeArchiveUrl": NotRequired[str],
        "SourceCodeUrl": NotRequired[str],
        "TemplateBody": NotRequired[str],
        "TemplateUrl": NotRequired[str],
    },
)
ParameterDefinitionTypeDef = TypedDict(
    "ParameterDefinitionTypeDef",
    {
        "Name": str,
        "ReferencedByResources": List[str],
        "AllowedPattern": NotRequired[str],
        "AllowedValues": NotRequired[List[str]],
        "ConstraintDescription": NotRequired[str],
        "DefaultValue": NotRequired[str],
        "Description": NotRequired[str],
        "MaxLength": NotRequired[int],
        "MaxValue": NotRequired[int],
        "MinLength": NotRequired[int],
        "MinValue": NotRequired[int],
        "NoEcho": NotRequired[bool],
        "Type": NotRequired[str],
    },
)
ParameterValueTypeDef = TypedDict(
    "ParameterValueTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
CreateCloudFormationTemplateRequestRequestTypeDef = TypedDict(
    "CreateCloudFormationTemplateRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "SemanticVersion": NotRequired[str],
    },
)
DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
GetApplicationPolicyRequestRequestTypeDef = TypedDict(
    "GetApplicationPolicyRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
GetApplicationRequestRequestTypeDef = TypedDict(
    "GetApplicationRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "SemanticVersion": NotRequired[str],
    },
)
GetCloudFormationTemplateRequestRequestTypeDef = TypedDict(
    "GetCloudFormationTemplateRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "TemplateId": str,
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
ListApplicationDependenciesRequestRequestTypeDef = TypedDict(
    "ListApplicationDependenciesRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "MaxItems": NotRequired[int],
        "NextToken": NotRequired[str],
        "SemanticVersion": NotRequired[str],
    },
)
ListApplicationVersionsRequestRequestTypeDef = TypedDict(
    "ListApplicationVersionsRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "MaxItems": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
VersionSummaryTypeDef = TypedDict(
    "VersionSummaryTypeDef",
    {
        "ApplicationId": str,
        "CreationTime": str,
        "SemanticVersion": str,
        "SourceCodeUrl": NotRequired[str],
    },
)
ListApplicationsRequestRequestTypeDef = TypedDict(
    "ListApplicationsRequestRequestTypeDef",
    {
        "MaxItems": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
RollbackTriggerTypeDef = TypedDict(
    "RollbackTriggerTypeDef",
    {
        "Arn": str,
        "Type": str,
    },
)
UnshareApplicationRequestRequestTypeDef = TypedDict(
    "UnshareApplicationRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "OrganizationId": str,
    },
)
UpdateApplicationRequestRequestTypeDef = TypedDict(
    "UpdateApplicationRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "Author": NotRequired[str],
        "Description": NotRequired[str],
        "HomePageUrl": NotRequired[str],
        "Labels": NotRequired[Sequence[str]],
        "ReadmeBody": NotRequired[str],
        "ReadmeUrl": NotRequired[str],
    },
)
ApplicationPolicyStatementUnionTypeDef = Union[
    ApplicationPolicyStatementTypeDef, ApplicationPolicyStatementOutputTypeDef
]
CreateCloudFormationChangeSetResponseTypeDef = TypedDict(
    "CreateCloudFormationChangeSetResponseTypeDef",
    {
        "ApplicationId": str,
        "ChangeSetId": str,
        "SemanticVersion": str,
        "StackId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCloudFormationTemplateResponseTypeDef = TypedDict(
    "CreateCloudFormationTemplateResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationTime": str,
        "ExpirationTime": str,
        "SemanticVersion": str,
        "Status": StatusType,
        "TemplateId": str,
        "TemplateUrl": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetApplicationPolicyResponseTypeDef = TypedDict(
    "GetApplicationPolicyResponseTypeDef",
    {
        "Statements": List[ApplicationPolicyStatementOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCloudFormationTemplateResponseTypeDef = TypedDict(
    "GetCloudFormationTemplateResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationTime": str,
        "ExpirationTime": str,
        "SemanticVersion": str,
        "Status": StatusType,
        "TemplateId": str,
        "TemplateUrl": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListApplicationDependenciesResponseTypeDef = TypedDict(
    "ListApplicationDependenciesResponseTypeDef",
    {
        "Dependencies": List[ApplicationDependencySummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {
        "Applications": List[ApplicationSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PutApplicationPolicyResponseTypeDef = TypedDict(
    "PutApplicationPolicyResponseTypeDef",
    {
        "Statements": List[ApplicationPolicyStatementOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateApplicationVersionResponseTypeDef = TypedDict(
    "CreateApplicationVersionResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationTime": str,
        "ParameterDefinitions": List[ParameterDefinitionTypeDef],
        "RequiredCapabilities": List[CapabilityType],
        "ResourcesSupported": bool,
        "SemanticVersion": str,
        "SourceCodeArchiveUrl": str,
        "SourceCodeUrl": str,
        "TemplateUrl": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VersionTypeDef = TypedDict(
    "VersionTypeDef",
    {
        "ApplicationId": str,
        "CreationTime": str,
        "ParameterDefinitions": List[ParameterDefinitionTypeDef],
        "RequiredCapabilities": List[CapabilityType],
        "ResourcesSupported": bool,
        "SemanticVersion": str,
        "TemplateUrl": str,
        "SourceCodeArchiveUrl": NotRequired[str],
        "SourceCodeUrl": NotRequired[str],
    },
)
ListApplicationDependenciesRequestListApplicationDependenciesPaginateTypeDef = TypedDict(
    "ListApplicationDependenciesRequestListApplicationDependenciesPaginateTypeDef",
    {
        "ApplicationId": str,
        "SemanticVersion": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListApplicationVersionsRequestListApplicationVersionsPaginateTypeDef = TypedDict(
    "ListApplicationVersionsRequestListApplicationVersionsPaginateTypeDef",
    {
        "ApplicationId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListApplicationsRequestListApplicationsPaginateTypeDef = TypedDict(
    "ListApplicationsRequestListApplicationsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListApplicationVersionsResponseTypeDef = TypedDict(
    "ListApplicationVersionsResponseTypeDef",
    {
        "Versions": List[VersionSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
RollbackConfigurationTypeDef = TypedDict(
    "RollbackConfigurationTypeDef",
    {
        "MonitoringTimeInMinutes": NotRequired[int],
        "RollbackTriggers": NotRequired[Sequence[RollbackTriggerTypeDef]],
    },
)
PutApplicationPolicyRequestRequestTypeDef = TypedDict(
    "PutApplicationPolicyRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "Statements": Sequence[ApplicationPolicyStatementUnionTypeDef],
    },
)
CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "ApplicationId": str,
        "Author": str,
        "CreationTime": str,
        "Description": str,
        "HomePageUrl": str,
        "IsVerifiedAuthor": bool,
        "Labels": List[str],
        "LicenseUrl": str,
        "Name": str,
        "ReadmeUrl": str,
        "SpdxLicenseId": str,
        "VerifiedAuthorUrl": str,
        "Version": VersionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetApplicationResponseTypeDef = TypedDict(
    "GetApplicationResponseTypeDef",
    {
        "ApplicationId": str,
        "Author": str,
        "CreationTime": str,
        "Description": str,
        "HomePageUrl": str,
        "IsVerifiedAuthor": bool,
        "Labels": List[str],
        "LicenseUrl": str,
        "Name": str,
        "ReadmeUrl": str,
        "SpdxLicenseId": str,
        "VerifiedAuthorUrl": str,
        "Version": VersionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateApplicationResponseTypeDef = TypedDict(
    "UpdateApplicationResponseTypeDef",
    {
        "ApplicationId": str,
        "Author": str,
        "CreationTime": str,
        "Description": str,
        "HomePageUrl": str,
        "IsVerifiedAuthor": bool,
        "Labels": List[str],
        "LicenseUrl": str,
        "Name": str,
        "ReadmeUrl": str,
        "SpdxLicenseId": str,
        "VerifiedAuthorUrl": str,
        "Version": VersionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCloudFormationChangeSetRequestRequestTypeDef = TypedDict(
    "CreateCloudFormationChangeSetRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "StackName": str,
        "Capabilities": NotRequired[Sequence[str]],
        "ChangeSetName": NotRequired[str],
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
        "NotificationArns": NotRequired[Sequence[str]],
        "ParameterOverrides": NotRequired[Sequence[ParameterValueTypeDef]],
        "ResourceTypes": NotRequired[Sequence[str]],
        "RollbackConfiguration": NotRequired[RollbackConfigurationTypeDef],
        "SemanticVersion": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "TemplateId": NotRequired[str],
    },
)
