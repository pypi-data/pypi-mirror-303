"""
Type annotations for elasticbeanstalk service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/type_defs/)

Usage::

    ```python
    from mypy_boto3_elasticbeanstalk.type_defs import AbortEnvironmentUpdateMessageRequestTypeDef

    data: AbortEnvironmentUpdateMessageRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    ActionHistoryStatusType,
    ActionStatusType,
    ActionTypeType,
    ApplicationVersionStatusType,
    ComputeTypeType,
    ConfigurationDeploymentStatusType,
    ConfigurationOptionValueTypeType,
    EnvironmentHealthAttributeType,
    EnvironmentHealthStatusType,
    EnvironmentHealthType,
    EnvironmentInfoTypeType,
    EnvironmentStatusType,
    EventSeverityType,
    FailureTypeType,
    InstancesHealthAttributeType,
    PlatformStatusType,
    SourceRepositoryType,
    SourceTypeType,
    ValidationSeverityType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AbortEnvironmentUpdateMessageRequestTypeDef",
    "ResponseMetadataTypeDef",
    "LatencyTypeDef",
    "StatusCodesTypeDef",
    "S3LocationTypeDef",
    "SourceBuildInformationTypeDef",
    "MaxAgeRuleTypeDef",
    "MaxCountRuleTypeDef",
    "ApplyEnvironmentManagedActionRequestRequestTypeDef",
    "AssociateEnvironmentOperationsRoleMessageRequestTypeDef",
    "AutoScalingGroupTypeDef",
    "BuildConfigurationTypeDef",
    "BuilderTypeDef",
    "CPUUtilizationTypeDef",
    "CheckDNSAvailabilityMessageRequestTypeDef",
    "ComposeEnvironmentsMessageRequestTypeDef",
    "OptionRestrictionRegexTypeDef",
    "ConfigurationOptionSettingTypeDef",
    "ValidationMessageTypeDef",
    "TagTypeDef",
    "SourceConfigurationTypeDef",
    "EnvironmentTierTypeDef",
    "OptionSpecificationTypeDef",
    "PlatformSummaryTypeDef",
    "CustomAmiTypeDef",
    "DeleteApplicationMessageRequestTypeDef",
    "DeleteApplicationVersionMessageRequestTypeDef",
    "DeleteConfigurationTemplateMessageRequestTypeDef",
    "DeleteEnvironmentConfigurationMessageRequestTypeDef",
    "DeletePlatformVersionRequestRequestTypeDef",
    "DeploymentTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeApplicationVersionsMessageRequestTypeDef",
    "DescribeApplicationsMessageRequestTypeDef",
    "DescribeConfigurationSettingsMessageRequestTypeDef",
    "DescribeEnvironmentHealthRequestRequestTypeDef",
    "InstanceHealthSummaryTypeDef",
    "DescribeEnvironmentManagedActionHistoryRequestRequestTypeDef",
    "ManagedActionHistoryItemTypeDef",
    "DescribeEnvironmentManagedActionsRequestRequestTypeDef",
    "ManagedActionTypeDef",
    "DescribeEnvironmentResourcesMessageRequestTypeDef",
    "TimestampTypeDef",
    "WaiterConfigTypeDef",
    "DescribeInstancesHealthRequestRequestTypeDef",
    "DescribePlatformVersionRequestRequestTypeDef",
    "DisassociateEnvironmentOperationsRoleMessageRequestTypeDef",
    "EnvironmentLinkTypeDef",
    "EnvironmentInfoDescriptionTypeDef",
    "InstanceTypeDef",
    "LaunchConfigurationTypeDef",
    "LaunchTemplateTypeDef",
    "LoadBalancerTypeDef",
    "QueueTypeDef",
    "TriggerTypeDef",
    "EventDescriptionTypeDef",
    "SolutionStackDescriptionTypeDef",
    "SearchFilterTypeDef",
    "PlatformBranchSummaryTypeDef",
    "PlatformFilterTypeDef",
    "ListTagsForResourceMessageRequestTypeDef",
    "ListenerTypeDef",
    "PlatformFrameworkTypeDef",
    "PlatformProgrammingLanguageTypeDef",
    "RebuildEnvironmentMessageRequestTypeDef",
    "RequestEnvironmentInfoMessageRequestTypeDef",
    "ResourceQuotaTypeDef",
    "RestartAppServerMessageRequestTypeDef",
    "RetrieveEnvironmentInfoMessageRequestTypeDef",
    "SwapEnvironmentCNAMEsMessageRequestTypeDef",
    "TerminateEnvironmentMessageRequestTypeDef",
    "UpdateApplicationMessageRequestTypeDef",
    "UpdateApplicationVersionMessageRequestTypeDef",
    "ApplyEnvironmentManagedActionResultTypeDef",
    "CheckDNSAvailabilityResultMessageTypeDef",
    "CreateStorageLocationResultMessageTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ApplicationMetricsTypeDef",
    "ApplicationVersionDescriptionTypeDef",
    "ApplicationVersionLifecycleConfigTypeDef",
    "SystemStatusTypeDef",
    "ConfigurationOptionDescriptionTypeDef",
    "ConfigurationSettingsDescriptionResponseTypeDef",
    "ConfigurationSettingsDescriptionTypeDef",
    "ValidateConfigurationSettingsMessageRequestTypeDef",
    "ConfigurationSettingsValidationMessagesTypeDef",
    "CreateApplicationVersionMessageRequestTypeDef",
    "CreatePlatformVersionRequestRequestTypeDef",
    "ResourceTagsDescriptionMessageTypeDef",
    "UpdateTagsForResourceMessageRequestTypeDef",
    "CreateConfigurationTemplateMessageRequestTypeDef",
    "CreateEnvironmentMessageRequestTypeDef",
    "DescribeConfigurationOptionsMessageRequestTypeDef",
    "UpdateConfigurationTemplateMessageRequestTypeDef",
    "UpdateEnvironmentMessageRequestTypeDef",
    "CreatePlatformVersionResultTypeDef",
    "DeletePlatformVersionResultTypeDef",
    "ListPlatformVersionsResultTypeDef",
    "DescribeApplicationVersionsMessageDescribeApplicationVersionsPaginateTypeDef",
    "DescribeEnvironmentManagedActionHistoryRequestDescribeEnvironmentManagedActionHistoryPaginateTypeDef",
    "DescribeEnvironmentManagedActionHistoryResultTypeDef",
    "DescribeEnvironmentManagedActionsResultTypeDef",
    "DescribeEnvironmentsMessageDescribeEnvironmentsPaginateTypeDef",
    "DescribeEnvironmentsMessageRequestTypeDef",
    "DescribeEventsMessageDescribeEventsPaginateTypeDef",
    "DescribeEventsMessageRequestTypeDef",
    "DescribeEnvironmentsMessageEnvironmentExistsWaitTypeDef",
    "DescribeEnvironmentsMessageEnvironmentTerminatedWaitTypeDef",
    "DescribeEnvironmentsMessageEnvironmentUpdatedWaitTypeDef",
    "RetrieveEnvironmentInfoResultMessageTypeDef",
    "EnvironmentResourceDescriptionTypeDef",
    "EventDescriptionsMessageTypeDef",
    "ListAvailableSolutionStacksResultMessageTypeDef",
    "ListPlatformBranchesRequestRequestTypeDef",
    "ListPlatformBranchesResultTypeDef",
    "ListPlatformVersionsRequestListPlatformVersionsPaginateTypeDef",
    "ListPlatformVersionsRequestRequestTypeDef",
    "LoadBalancerDescriptionTypeDef",
    "PlatformDescriptionTypeDef",
    "ResourceQuotasTypeDef",
    "DescribeEnvironmentHealthResultTypeDef",
    "ApplicationVersionDescriptionMessageTypeDef",
    "ApplicationVersionDescriptionsMessageTypeDef",
    "ApplicationResourceLifecycleConfigTypeDef",
    "SingleInstanceHealthTypeDef",
    "ConfigurationOptionsDescriptionTypeDef",
    "ConfigurationSettingsDescriptionsTypeDef",
    "EnvironmentResourceDescriptionsMessageTypeDef",
    "EnvironmentResourcesDescriptionTypeDef",
    "DescribePlatformVersionResultTypeDef",
    "DescribeAccountAttributesResultTypeDef",
    "ApplicationDescriptionTypeDef",
    "ApplicationResourceLifecycleDescriptionMessageTypeDef",
    "CreateApplicationMessageRequestTypeDef",
    "UpdateApplicationResourceLifecycleMessageRequestTypeDef",
    "DescribeInstancesHealthResultTypeDef",
    "EnvironmentDescriptionResponseTypeDef",
    "EnvironmentDescriptionTypeDef",
    "ApplicationDescriptionMessageTypeDef",
    "ApplicationDescriptionsMessageTypeDef",
    "EnvironmentDescriptionsMessageTypeDef",
)

AbortEnvironmentUpdateMessageRequestTypeDef = TypedDict(
    "AbortEnvironmentUpdateMessageRequestTypeDef",
    {
        "EnvironmentId": NotRequired[str],
        "EnvironmentName": NotRequired[str],
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
LatencyTypeDef = TypedDict(
    "LatencyTypeDef",
    {
        "P999": NotRequired[float],
        "P99": NotRequired[float],
        "P95": NotRequired[float],
        "P90": NotRequired[float],
        "P85": NotRequired[float],
        "P75": NotRequired[float],
        "P50": NotRequired[float],
        "P10": NotRequired[float],
    },
)
StatusCodesTypeDef = TypedDict(
    "StatusCodesTypeDef",
    {
        "Status2xx": NotRequired[int],
        "Status3xx": NotRequired[int],
        "Status4xx": NotRequired[int],
        "Status5xx": NotRequired[int],
    },
)
S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "S3Bucket": NotRequired[str],
        "S3Key": NotRequired[str],
    },
)
SourceBuildInformationTypeDef = TypedDict(
    "SourceBuildInformationTypeDef",
    {
        "SourceType": SourceTypeType,
        "SourceRepository": SourceRepositoryType,
        "SourceLocation": str,
    },
)
MaxAgeRuleTypeDef = TypedDict(
    "MaxAgeRuleTypeDef",
    {
        "Enabled": bool,
        "MaxAgeInDays": NotRequired[int],
        "DeleteSourceFromS3": NotRequired[bool],
    },
)
MaxCountRuleTypeDef = TypedDict(
    "MaxCountRuleTypeDef",
    {
        "Enabled": bool,
        "MaxCount": NotRequired[int],
        "DeleteSourceFromS3": NotRequired[bool],
    },
)
ApplyEnvironmentManagedActionRequestRequestTypeDef = TypedDict(
    "ApplyEnvironmentManagedActionRequestRequestTypeDef",
    {
        "ActionId": str,
        "EnvironmentName": NotRequired[str],
        "EnvironmentId": NotRequired[str],
    },
)
AssociateEnvironmentOperationsRoleMessageRequestTypeDef = TypedDict(
    "AssociateEnvironmentOperationsRoleMessageRequestTypeDef",
    {
        "EnvironmentName": str,
        "OperationsRole": str,
    },
)
AutoScalingGroupTypeDef = TypedDict(
    "AutoScalingGroupTypeDef",
    {
        "Name": NotRequired[str],
    },
)
BuildConfigurationTypeDef = TypedDict(
    "BuildConfigurationTypeDef",
    {
        "CodeBuildServiceRole": str,
        "Image": str,
        "ArtifactName": NotRequired[str],
        "ComputeType": NotRequired[ComputeTypeType],
        "TimeoutInMinutes": NotRequired[int],
    },
)
BuilderTypeDef = TypedDict(
    "BuilderTypeDef",
    {
        "ARN": NotRequired[str],
    },
)
CPUUtilizationTypeDef = TypedDict(
    "CPUUtilizationTypeDef",
    {
        "User": NotRequired[float],
        "Nice": NotRequired[float],
        "System": NotRequired[float],
        "Idle": NotRequired[float],
        "IOWait": NotRequired[float],
        "IRQ": NotRequired[float],
        "SoftIRQ": NotRequired[float],
        "Privileged": NotRequired[float],
    },
)
CheckDNSAvailabilityMessageRequestTypeDef = TypedDict(
    "CheckDNSAvailabilityMessageRequestTypeDef",
    {
        "CNAMEPrefix": str,
    },
)
ComposeEnvironmentsMessageRequestTypeDef = TypedDict(
    "ComposeEnvironmentsMessageRequestTypeDef",
    {
        "ApplicationName": NotRequired[str],
        "GroupName": NotRequired[str],
        "VersionLabels": NotRequired[Sequence[str]],
    },
)
OptionRestrictionRegexTypeDef = TypedDict(
    "OptionRestrictionRegexTypeDef",
    {
        "Pattern": NotRequired[str],
        "Label": NotRequired[str],
    },
)
ConfigurationOptionSettingTypeDef = TypedDict(
    "ConfigurationOptionSettingTypeDef",
    {
        "ResourceName": NotRequired[str],
        "Namespace": NotRequired[str],
        "OptionName": NotRequired[str],
        "Value": NotRequired[str],
    },
)
ValidationMessageTypeDef = TypedDict(
    "ValidationMessageTypeDef",
    {
        "Message": NotRequired[str],
        "Severity": NotRequired[ValidationSeverityType],
        "Namespace": NotRequired[str],
        "OptionName": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
SourceConfigurationTypeDef = TypedDict(
    "SourceConfigurationTypeDef",
    {
        "ApplicationName": NotRequired[str],
        "TemplateName": NotRequired[str],
    },
)
EnvironmentTierTypeDef = TypedDict(
    "EnvironmentTierTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
        "Version": NotRequired[str],
    },
)
OptionSpecificationTypeDef = TypedDict(
    "OptionSpecificationTypeDef",
    {
        "ResourceName": NotRequired[str],
        "Namespace": NotRequired[str],
        "OptionName": NotRequired[str],
    },
)
PlatformSummaryTypeDef = TypedDict(
    "PlatformSummaryTypeDef",
    {
        "PlatformArn": NotRequired[str],
        "PlatformOwner": NotRequired[str],
        "PlatformStatus": NotRequired[PlatformStatusType],
        "PlatformCategory": NotRequired[str],
        "OperatingSystemName": NotRequired[str],
        "OperatingSystemVersion": NotRequired[str],
        "SupportedTierList": NotRequired[List[str]],
        "SupportedAddonList": NotRequired[List[str]],
        "PlatformLifecycleState": NotRequired[str],
        "PlatformVersion": NotRequired[str],
        "PlatformBranchName": NotRequired[str],
        "PlatformBranchLifecycleState": NotRequired[str],
    },
)
CustomAmiTypeDef = TypedDict(
    "CustomAmiTypeDef",
    {
        "VirtualizationType": NotRequired[str],
        "ImageId": NotRequired[str],
    },
)
DeleteApplicationMessageRequestTypeDef = TypedDict(
    "DeleteApplicationMessageRequestTypeDef",
    {
        "ApplicationName": str,
        "TerminateEnvByForce": NotRequired[bool],
    },
)
DeleteApplicationVersionMessageRequestTypeDef = TypedDict(
    "DeleteApplicationVersionMessageRequestTypeDef",
    {
        "ApplicationName": str,
        "VersionLabel": str,
        "DeleteSourceBundle": NotRequired[bool],
    },
)
DeleteConfigurationTemplateMessageRequestTypeDef = TypedDict(
    "DeleteConfigurationTemplateMessageRequestTypeDef",
    {
        "ApplicationName": str,
        "TemplateName": str,
    },
)
DeleteEnvironmentConfigurationMessageRequestTypeDef = TypedDict(
    "DeleteEnvironmentConfigurationMessageRequestTypeDef",
    {
        "ApplicationName": str,
        "EnvironmentName": str,
    },
)
DeletePlatformVersionRequestRequestTypeDef = TypedDict(
    "DeletePlatformVersionRequestRequestTypeDef",
    {
        "PlatformArn": NotRequired[str],
    },
)
DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "VersionLabel": NotRequired[str],
        "DeploymentId": NotRequired[int],
        "Status": NotRequired[str],
        "DeploymentTime": NotRequired[datetime],
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
DescribeApplicationVersionsMessageRequestTypeDef = TypedDict(
    "DescribeApplicationVersionsMessageRequestTypeDef",
    {
        "ApplicationName": NotRequired[str],
        "VersionLabels": NotRequired[Sequence[str]],
        "MaxRecords": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeApplicationsMessageRequestTypeDef = TypedDict(
    "DescribeApplicationsMessageRequestTypeDef",
    {
        "ApplicationNames": NotRequired[Sequence[str]],
    },
)
DescribeConfigurationSettingsMessageRequestTypeDef = TypedDict(
    "DescribeConfigurationSettingsMessageRequestTypeDef",
    {
        "ApplicationName": str,
        "TemplateName": NotRequired[str],
        "EnvironmentName": NotRequired[str],
    },
)
DescribeEnvironmentHealthRequestRequestTypeDef = TypedDict(
    "DescribeEnvironmentHealthRequestRequestTypeDef",
    {
        "EnvironmentName": NotRequired[str],
        "EnvironmentId": NotRequired[str],
        "AttributeNames": NotRequired[Sequence[EnvironmentHealthAttributeType]],
    },
)
InstanceHealthSummaryTypeDef = TypedDict(
    "InstanceHealthSummaryTypeDef",
    {
        "NoData": NotRequired[int],
        "Unknown": NotRequired[int],
        "Pending": NotRequired[int],
        "Ok": NotRequired[int],
        "Info": NotRequired[int],
        "Warning": NotRequired[int],
        "Degraded": NotRequired[int],
        "Severe": NotRequired[int],
    },
)
DescribeEnvironmentManagedActionHistoryRequestRequestTypeDef = TypedDict(
    "DescribeEnvironmentManagedActionHistoryRequestRequestTypeDef",
    {
        "EnvironmentId": NotRequired[str],
        "EnvironmentName": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
ManagedActionHistoryItemTypeDef = TypedDict(
    "ManagedActionHistoryItemTypeDef",
    {
        "ActionId": NotRequired[str],
        "ActionType": NotRequired[ActionTypeType],
        "ActionDescription": NotRequired[str],
        "FailureType": NotRequired[FailureTypeType],
        "Status": NotRequired[ActionHistoryStatusType],
        "FailureDescription": NotRequired[str],
        "ExecutedTime": NotRequired[datetime],
        "FinishedTime": NotRequired[datetime],
    },
)
DescribeEnvironmentManagedActionsRequestRequestTypeDef = TypedDict(
    "DescribeEnvironmentManagedActionsRequestRequestTypeDef",
    {
        "EnvironmentName": NotRequired[str],
        "EnvironmentId": NotRequired[str],
        "Status": NotRequired[ActionStatusType],
    },
)
ManagedActionTypeDef = TypedDict(
    "ManagedActionTypeDef",
    {
        "ActionId": NotRequired[str],
        "ActionDescription": NotRequired[str],
        "ActionType": NotRequired[ActionTypeType],
        "Status": NotRequired[ActionStatusType],
        "WindowStartTime": NotRequired[datetime],
    },
)
DescribeEnvironmentResourcesMessageRequestTypeDef = TypedDict(
    "DescribeEnvironmentResourcesMessageRequestTypeDef",
    {
        "EnvironmentId": NotRequired[str],
        "EnvironmentName": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
DescribeInstancesHealthRequestRequestTypeDef = TypedDict(
    "DescribeInstancesHealthRequestRequestTypeDef",
    {
        "EnvironmentName": NotRequired[str],
        "EnvironmentId": NotRequired[str],
        "AttributeNames": NotRequired[Sequence[InstancesHealthAttributeType]],
        "NextToken": NotRequired[str],
    },
)
DescribePlatformVersionRequestRequestTypeDef = TypedDict(
    "DescribePlatformVersionRequestRequestTypeDef",
    {
        "PlatformArn": NotRequired[str],
    },
)
DisassociateEnvironmentOperationsRoleMessageRequestTypeDef = TypedDict(
    "DisassociateEnvironmentOperationsRoleMessageRequestTypeDef",
    {
        "EnvironmentName": str,
    },
)
EnvironmentLinkTypeDef = TypedDict(
    "EnvironmentLinkTypeDef",
    {
        "LinkName": NotRequired[str],
        "EnvironmentName": NotRequired[str],
    },
)
EnvironmentInfoDescriptionTypeDef = TypedDict(
    "EnvironmentInfoDescriptionTypeDef",
    {
        "InfoType": NotRequired[EnvironmentInfoTypeType],
        "Ec2InstanceId": NotRequired[str],
        "SampleTimestamp": NotRequired[datetime],
        "Message": NotRequired[str],
    },
)
InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "Id": NotRequired[str],
    },
)
LaunchConfigurationTypeDef = TypedDict(
    "LaunchConfigurationTypeDef",
    {
        "Name": NotRequired[str],
    },
)
LaunchTemplateTypeDef = TypedDict(
    "LaunchTemplateTypeDef",
    {
        "Id": NotRequired[str],
    },
)
LoadBalancerTypeDef = TypedDict(
    "LoadBalancerTypeDef",
    {
        "Name": NotRequired[str],
    },
)
QueueTypeDef = TypedDict(
    "QueueTypeDef",
    {
        "Name": NotRequired[str],
        "URL": NotRequired[str],
    },
)
TriggerTypeDef = TypedDict(
    "TriggerTypeDef",
    {
        "Name": NotRequired[str],
    },
)
EventDescriptionTypeDef = TypedDict(
    "EventDescriptionTypeDef",
    {
        "EventDate": NotRequired[datetime],
        "Message": NotRequired[str],
        "ApplicationName": NotRequired[str],
        "VersionLabel": NotRequired[str],
        "TemplateName": NotRequired[str],
        "EnvironmentName": NotRequired[str],
        "PlatformArn": NotRequired[str],
        "RequestId": NotRequired[str],
        "Severity": NotRequired[EventSeverityType],
    },
)
SolutionStackDescriptionTypeDef = TypedDict(
    "SolutionStackDescriptionTypeDef",
    {
        "SolutionStackName": NotRequired[str],
        "PermittedFileTypes": NotRequired[List[str]],
    },
)
SearchFilterTypeDef = TypedDict(
    "SearchFilterTypeDef",
    {
        "Attribute": NotRequired[str],
        "Operator": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)
PlatformBranchSummaryTypeDef = TypedDict(
    "PlatformBranchSummaryTypeDef",
    {
        "PlatformName": NotRequired[str],
        "BranchName": NotRequired[str],
        "LifecycleState": NotRequired[str],
        "BranchOrder": NotRequired[int],
        "SupportedTierList": NotRequired[List[str]],
    },
)
PlatformFilterTypeDef = TypedDict(
    "PlatformFilterTypeDef",
    {
        "Type": NotRequired[str],
        "Operator": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)
ListTagsForResourceMessageRequestTypeDef = TypedDict(
    "ListTagsForResourceMessageRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
ListenerTypeDef = TypedDict(
    "ListenerTypeDef",
    {
        "Protocol": NotRequired[str],
        "Port": NotRequired[int],
    },
)
PlatformFrameworkTypeDef = TypedDict(
    "PlatformFrameworkTypeDef",
    {
        "Name": NotRequired[str],
        "Version": NotRequired[str],
    },
)
PlatformProgrammingLanguageTypeDef = TypedDict(
    "PlatformProgrammingLanguageTypeDef",
    {
        "Name": NotRequired[str],
        "Version": NotRequired[str],
    },
)
RebuildEnvironmentMessageRequestTypeDef = TypedDict(
    "RebuildEnvironmentMessageRequestTypeDef",
    {
        "EnvironmentId": NotRequired[str],
        "EnvironmentName": NotRequired[str],
    },
)
RequestEnvironmentInfoMessageRequestTypeDef = TypedDict(
    "RequestEnvironmentInfoMessageRequestTypeDef",
    {
        "InfoType": EnvironmentInfoTypeType,
        "EnvironmentId": NotRequired[str],
        "EnvironmentName": NotRequired[str],
    },
)
ResourceQuotaTypeDef = TypedDict(
    "ResourceQuotaTypeDef",
    {
        "Maximum": NotRequired[int],
    },
)
RestartAppServerMessageRequestTypeDef = TypedDict(
    "RestartAppServerMessageRequestTypeDef",
    {
        "EnvironmentId": NotRequired[str],
        "EnvironmentName": NotRequired[str],
    },
)
RetrieveEnvironmentInfoMessageRequestTypeDef = TypedDict(
    "RetrieveEnvironmentInfoMessageRequestTypeDef",
    {
        "InfoType": EnvironmentInfoTypeType,
        "EnvironmentId": NotRequired[str],
        "EnvironmentName": NotRequired[str],
    },
)
SwapEnvironmentCNAMEsMessageRequestTypeDef = TypedDict(
    "SwapEnvironmentCNAMEsMessageRequestTypeDef",
    {
        "SourceEnvironmentId": NotRequired[str],
        "SourceEnvironmentName": NotRequired[str],
        "DestinationEnvironmentId": NotRequired[str],
        "DestinationEnvironmentName": NotRequired[str],
    },
)
TerminateEnvironmentMessageRequestTypeDef = TypedDict(
    "TerminateEnvironmentMessageRequestTypeDef",
    {
        "EnvironmentId": NotRequired[str],
        "EnvironmentName": NotRequired[str],
        "TerminateResources": NotRequired[bool],
        "ForceTerminate": NotRequired[bool],
    },
)
UpdateApplicationMessageRequestTypeDef = TypedDict(
    "UpdateApplicationMessageRequestTypeDef",
    {
        "ApplicationName": str,
        "Description": NotRequired[str],
    },
)
UpdateApplicationVersionMessageRequestTypeDef = TypedDict(
    "UpdateApplicationVersionMessageRequestTypeDef",
    {
        "ApplicationName": str,
        "VersionLabel": str,
        "Description": NotRequired[str],
    },
)
ApplyEnvironmentManagedActionResultTypeDef = TypedDict(
    "ApplyEnvironmentManagedActionResultTypeDef",
    {
        "ActionId": str,
        "ActionDescription": str,
        "ActionType": ActionTypeType,
        "Status": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CheckDNSAvailabilityResultMessageTypeDef = TypedDict(
    "CheckDNSAvailabilityResultMessageTypeDef",
    {
        "Available": bool,
        "FullyQualifiedCNAME": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateStorageLocationResultMessageTypeDef = TypedDict(
    "CreateStorageLocationResultMessageTypeDef",
    {
        "S3Bucket": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ApplicationMetricsTypeDef = TypedDict(
    "ApplicationMetricsTypeDef",
    {
        "Duration": NotRequired[int],
        "RequestCount": NotRequired[int],
        "StatusCodes": NotRequired[StatusCodesTypeDef],
        "Latency": NotRequired[LatencyTypeDef],
    },
)
ApplicationVersionDescriptionTypeDef = TypedDict(
    "ApplicationVersionDescriptionTypeDef",
    {
        "ApplicationVersionArn": NotRequired[str],
        "ApplicationName": NotRequired[str],
        "Description": NotRequired[str],
        "VersionLabel": NotRequired[str],
        "SourceBuildInformation": NotRequired[SourceBuildInformationTypeDef],
        "BuildArn": NotRequired[str],
        "SourceBundle": NotRequired[S3LocationTypeDef],
        "DateCreated": NotRequired[datetime],
        "DateUpdated": NotRequired[datetime],
        "Status": NotRequired[ApplicationVersionStatusType],
    },
)
ApplicationVersionLifecycleConfigTypeDef = TypedDict(
    "ApplicationVersionLifecycleConfigTypeDef",
    {
        "MaxCountRule": NotRequired[MaxCountRuleTypeDef],
        "MaxAgeRule": NotRequired[MaxAgeRuleTypeDef],
    },
)
SystemStatusTypeDef = TypedDict(
    "SystemStatusTypeDef",
    {
        "CPUUtilization": NotRequired[CPUUtilizationTypeDef],
        "LoadAverage": NotRequired[List[float]],
    },
)
ConfigurationOptionDescriptionTypeDef = TypedDict(
    "ConfigurationOptionDescriptionTypeDef",
    {
        "Namespace": NotRequired[str],
        "Name": NotRequired[str],
        "DefaultValue": NotRequired[str],
        "ChangeSeverity": NotRequired[str],
        "UserDefined": NotRequired[bool],
        "ValueType": NotRequired[ConfigurationOptionValueTypeType],
        "ValueOptions": NotRequired[List[str]],
        "MinValue": NotRequired[int],
        "MaxValue": NotRequired[int],
        "MaxLength": NotRequired[int],
        "Regex": NotRequired[OptionRestrictionRegexTypeDef],
    },
)
ConfigurationSettingsDescriptionResponseTypeDef = TypedDict(
    "ConfigurationSettingsDescriptionResponseTypeDef",
    {
        "SolutionStackName": str,
        "PlatformArn": str,
        "ApplicationName": str,
        "TemplateName": str,
        "Description": str,
        "EnvironmentName": str,
        "DeploymentStatus": ConfigurationDeploymentStatusType,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "OptionSettings": List[ConfigurationOptionSettingTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConfigurationSettingsDescriptionTypeDef = TypedDict(
    "ConfigurationSettingsDescriptionTypeDef",
    {
        "SolutionStackName": NotRequired[str],
        "PlatformArn": NotRequired[str],
        "ApplicationName": NotRequired[str],
        "TemplateName": NotRequired[str],
        "Description": NotRequired[str],
        "EnvironmentName": NotRequired[str],
        "DeploymentStatus": NotRequired[ConfigurationDeploymentStatusType],
        "DateCreated": NotRequired[datetime],
        "DateUpdated": NotRequired[datetime],
        "OptionSettings": NotRequired[List[ConfigurationOptionSettingTypeDef]],
    },
)
ValidateConfigurationSettingsMessageRequestTypeDef = TypedDict(
    "ValidateConfigurationSettingsMessageRequestTypeDef",
    {
        "ApplicationName": str,
        "OptionSettings": Sequence[ConfigurationOptionSettingTypeDef],
        "TemplateName": NotRequired[str],
        "EnvironmentName": NotRequired[str],
    },
)
ConfigurationSettingsValidationMessagesTypeDef = TypedDict(
    "ConfigurationSettingsValidationMessagesTypeDef",
    {
        "Messages": List[ValidationMessageTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateApplicationVersionMessageRequestTypeDef = TypedDict(
    "CreateApplicationVersionMessageRequestTypeDef",
    {
        "ApplicationName": str,
        "VersionLabel": str,
        "Description": NotRequired[str],
        "SourceBuildInformation": NotRequired[SourceBuildInformationTypeDef],
        "SourceBundle": NotRequired[S3LocationTypeDef],
        "BuildConfiguration": NotRequired[BuildConfigurationTypeDef],
        "AutoCreateApplication": NotRequired[bool],
        "Process": NotRequired[bool],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreatePlatformVersionRequestRequestTypeDef = TypedDict(
    "CreatePlatformVersionRequestRequestTypeDef",
    {
        "PlatformName": str,
        "PlatformVersion": str,
        "PlatformDefinitionBundle": S3LocationTypeDef,
        "EnvironmentName": NotRequired[str],
        "OptionSettings": NotRequired[Sequence[ConfigurationOptionSettingTypeDef]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ResourceTagsDescriptionMessageTypeDef = TypedDict(
    "ResourceTagsDescriptionMessageTypeDef",
    {
        "ResourceArn": str,
        "ResourceTags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTagsForResourceMessageRequestTypeDef = TypedDict(
    "UpdateTagsForResourceMessageRequestTypeDef",
    {
        "ResourceArn": str,
        "TagsToAdd": NotRequired[Sequence[TagTypeDef]],
        "TagsToRemove": NotRequired[Sequence[str]],
    },
)
CreateConfigurationTemplateMessageRequestTypeDef = TypedDict(
    "CreateConfigurationTemplateMessageRequestTypeDef",
    {
        "ApplicationName": str,
        "TemplateName": str,
        "SolutionStackName": NotRequired[str],
        "PlatformArn": NotRequired[str],
        "SourceConfiguration": NotRequired[SourceConfigurationTypeDef],
        "EnvironmentId": NotRequired[str],
        "Description": NotRequired[str],
        "OptionSettings": NotRequired[Sequence[ConfigurationOptionSettingTypeDef]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateEnvironmentMessageRequestTypeDef = TypedDict(
    "CreateEnvironmentMessageRequestTypeDef",
    {
        "ApplicationName": str,
        "EnvironmentName": NotRequired[str],
        "GroupName": NotRequired[str],
        "Description": NotRequired[str],
        "CNAMEPrefix": NotRequired[str],
        "Tier": NotRequired[EnvironmentTierTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "VersionLabel": NotRequired[str],
        "TemplateName": NotRequired[str],
        "SolutionStackName": NotRequired[str],
        "PlatformArn": NotRequired[str],
        "OptionSettings": NotRequired[Sequence[ConfigurationOptionSettingTypeDef]],
        "OptionsToRemove": NotRequired[Sequence[OptionSpecificationTypeDef]],
        "OperationsRole": NotRequired[str],
    },
)
DescribeConfigurationOptionsMessageRequestTypeDef = TypedDict(
    "DescribeConfigurationOptionsMessageRequestTypeDef",
    {
        "ApplicationName": NotRequired[str],
        "TemplateName": NotRequired[str],
        "EnvironmentName": NotRequired[str],
        "SolutionStackName": NotRequired[str],
        "PlatformArn": NotRequired[str],
        "Options": NotRequired[Sequence[OptionSpecificationTypeDef]],
    },
)
UpdateConfigurationTemplateMessageRequestTypeDef = TypedDict(
    "UpdateConfigurationTemplateMessageRequestTypeDef",
    {
        "ApplicationName": str,
        "TemplateName": str,
        "Description": NotRequired[str],
        "OptionSettings": NotRequired[Sequence[ConfigurationOptionSettingTypeDef]],
        "OptionsToRemove": NotRequired[Sequence[OptionSpecificationTypeDef]],
    },
)
UpdateEnvironmentMessageRequestTypeDef = TypedDict(
    "UpdateEnvironmentMessageRequestTypeDef",
    {
        "ApplicationName": NotRequired[str],
        "EnvironmentId": NotRequired[str],
        "EnvironmentName": NotRequired[str],
        "GroupName": NotRequired[str],
        "Description": NotRequired[str],
        "Tier": NotRequired[EnvironmentTierTypeDef],
        "VersionLabel": NotRequired[str],
        "TemplateName": NotRequired[str],
        "SolutionStackName": NotRequired[str],
        "PlatformArn": NotRequired[str],
        "OptionSettings": NotRequired[Sequence[ConfigurationOptionSettingTypeDef]],
        "OptionsToRemove": NotRequired[Sequence[OptionSpecificationTypeDef]],
    },
)
CreatePlatformVersionResultTypeDef = TypedDict(
    "CreatePlatformVersionResultTypeDef",
    {
        "PlatformSummary": PlatformSummaryTypeDef,
        "Builder": BuilderTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeletePlatformVersionResultTypeDef = TypedDict(
    "DeletePlatformVersionResultTypeDef",
    {
        "PlatformSummary": PlatformSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPlatformVersionsResultTypeDef = TypedDict(
    "ListPlatformVersionsResultTypeDef",
    {
        "PlatformSummaryList": List[PlatformSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeApplicationVersionsMessageDescribeApplicationVersionsPaginateTypeDef = TypedDict(
    "DescribeApplicationVersionsMessageDescribeApplicationVersionsPaginateTypeDef",
    {
        "ApplicationName": NotRequired[str],
        "VersionLabels": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEnvironmentManagedActionHistoryRequestDescribeEnvironmentManagedActionHistoryPaginateTypeDef = TypedDict(
    "DescribeEnvironmentManagedActionHistoryRequestDescribeEnvironmentManagedActionHistoryPaginateTypeDef",
    {
        "EnvironmentId": NotRequired[str],
        "EnvironmentName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEnvironmentManagedActionHistoryResultTypeDef = TypedDict(
    "DescribeEnvironmentManagedActionHistoryResultTypeDef",
    {
        "ManagedActionHistoryItems": List[ManagedActionHistoryItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeEnvironmentManagedActionsResultTypeDef = TypedDict(
    "DescribeEnvironmentManagedActionsResultTypeDef",
    {
        "ManagedActions": List[ManagedActionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEnvironmentsMessageDescribeEnvironmentsPaginateTypeDef = TypedDict(
    "DescribeEnvironmentsMessageDescribeEnvironmentsPaginateTypeDef",
    {
        "ApplicationName": NotRequired[str],
        "VersionLabel": NotRequired[str],
        "EnvironmentIds": NotRequired[Sequence[str]],
        "EnvironmentNames": NotRequired[Sequence[str]],
        "IncludeDeleted": NotRequired[bool],
        "IncludedDeletedBackTo": NotRequired[TimestampTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEnvironmentsMessageRequestTypeDef = TypedDict(
    "DescribeEnvironmentsMessageRequestTypeDef",
    {
        "ApplicationName": NotRequired[str],
        "VersionLabel": NotRequired[str],
        "EnvironmentIds": NotRequired[Sequence[str]],
        "EnvironmentNames": NotRequired[Sequence[str]],
        "IncludeDeleted": NotRequired[bool],
        "IncludedDeletedBackTo": NotRequired[TimestampTypeDef],
        "MaxRecords": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeEventsMessageDescribeEventsPaginateTypeDef = TypedDict(
    "DescribeEventsMessageDescribeEventsPaginateTypeDef",
    {
        "ApplicationName": NotRequired[str],
        "VersionLabel": NotRequired[str],
        "TemplateName": NotRequired[str],
        "EnvironmentId": NotRequired[str],
        "EnvironmentName": NotRequired[str],
        "PlatformArn": NotRequired[str],
        "RequestId": NotRequired[str],
        "Severity": NotRequired[EventSeverityType],
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeEventsMessageRequestTypeDef = TypedDict(
    "DescribeEventsMessageRequestTypeDef",
    {
        "ApplicationName": NotRequired[str],
        "VersionLabel": NotRequired[str],
        "TemplateName": NotRequired[str],
        "EnvironmentId": NotRequired[str],
        "EnvironmentName": NotRequired[str],
        "PlatformArn": NotRequired[str],
        "RequestId": NotRequired[str],
        "Severity": NotRequired[EventSeverityType],
        "StartTime": NotRequired[TimestampTypeDef],
        "EndTime": NotRequired[TimestampTypeDef],
        "MaxRecords": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeEnvironmentsMessageEnvironmentExistsWaitTypeDef = TypedDict(
    "DescribeEnvironmentsMessageEnvironmentExistsWaitTypeDef",
    {
        "ApplicationName": NotRequired[str],
        "VersionLabel": NotRequired[str],
        "EnvironmentIds": NotRequired[Sequence[str]],
        "EnvironmentNames": NotRequired[Sequence[str]],
        "IncludeDeleted": NotRequired[bool],
        "IncludedDeletedBackTo": NotRequired[TimestampTypeDef],
        "MaxRecords": NotRequired[int],
        "NextToken": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeEnvironmentsMessageEnvironmentTerminatedWaitTypeDef = TypedDict(
    "DescribeEnvironmentsMessageEnvironmentTerminatedWaitTypeDef",
    {
        "ApplicationName": NotRequired[str],
        "VersionLabel": NotRequired[str],
        "EnvironmentIds": NotRequired[Sequence[str]],
        "EnvironmentNames": NotRequired[Sequence[str]],
        "IncludeDeleted": NotRequired[bool],
        "IncludedDeletedBackTo": NotRequired[TimestampTypeDef],
        "MaxRecords": NotRequired[int],
        "NextToken": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeEnvironmentsMessageEnvironmentUpdatedWaitTypeDef = TypedDict(
    "DescribeEnvironmentsMessageEnvironmentUpdatedWaitTypeDef",
    {
        "ApplicationName": NotRequired[str],
        "VersionLabel": NotRequired[str],
        "EnvironmentIds": NotRequired[Sequence[str]],
        "EnvironmentNames": NotRequired[Sequence[str]],
        "IncludeDeleted": NotRequired[bool],
        "IncludedDeletedBackTo": NotRequired[TimestampTypeDef],
        "MaxRecords": NotRequired[int],
        "NextToken": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
RetrieveEnvironmentInfoResultMessageTypeDef = TypedDict(
    "RetrieveEnvironmentInfoResultMessageTypeDef",
    {
        "EnvironmentInfo": List[EnvironmentInfoDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnvironmentResourceDescriptionTypeDef = TypedDict(
    "EnvironmentResourceDescriptionTypeDef",
    {
        "EnvironmentName": NotRequired[str],
        "AutoScalingGroups": NotRequired[List[AutoScalingGroupTypeDef]],
        "Instances": NotRequired[List[InstanceTypeDef]],
        "LaunchConfigurations": NotRequired[List[LaunchConfigurationTypeDef]],
        "LaunchTemplates": NotRequired[List[LaunchTemplateTypeDef]],
        "LoadBalancers": NotRequired[List[LoadBalancerTypeDef]],
        "Triggers": NotRequired[List[TriggerTypeDef]],
        "Queues": NotRequired[List[QueueTypeDef]],
    },
)
EventDescriptionsMessageTypeDef = TypedDict(
    "EventDescriptionsMessageTypeDef",
    {
        "Events": List[EventDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListAvailableSolutionStacksResultMessageTypeDef = TypedDict(
    "ListAvailableSolutionStacksResultMessageTypeDef",
    {
        "SolutionStacks": List[str],
        "SolutionStackDetails": List[SolutionStackDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPlatformBranchesRequestRequestTypeDef = TypedDict(
    "ListPlatformBranchesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[SearchFilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListPlatformBranchesResultTypeDef = TypedDict(
    "ListPlatformBranchesResultTypeDef",
    {
        "PlatformBranchSummaryList": List[PlatformBranchSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListPlatformVersionsRequestListPlatformVersionsPaginateTypeDef = TypedDict(
    "ListPlatformVersionsRequestListPlatformVersionsPaginateTypeDef",
    {
        "Filters": NotRequired[Sequence[PlatformFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPlatformVersionsRequestRequestTypeDef = TypedDict(
    "ListPlatformVersionsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence[PlatformFilterTypeDef]],
        "MaxRecords": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
LoadBalancerDescriptionTypeDef = TypedDict(
    "LoadBalancerDescriptionTypeDef",
    {
        "LoadBalancerName": NotRequired[str],
        "Domain": NotRequired[str],
        "Listeners": NotRequired[List[ListenerTypeDef]],
    },
)
PlatformDescriptionTypeDef = TypedDict(
    "PlatformDescriptionTypeDef",
    {
        "PlatformArn": NotRequired[str],
        "PlatformOwner": NotRequired[str],
        "PlatformName": NotRequired[str],
        "PlatformVersion": NotRequired[str],
        "SolutionStackName": NotRequired[str],
        "PlatformStatus": NotRequired[PlatformStatusType],
        "DateCreated": NotRequired[datetime],
        "DateUpdated": NotRequired[datetime],
        "PlatformCategory": NotRequired[str],
        "Description": NotRequired[str],
        "Maintainer": NotRequired[str],
        "OperatingSystemName": NotRequired[str],
        "OperatingSystemVersion": NotRequired[str],
        "ProgrammingLanguages": NotRequired[List[PlatformProgrammingLanguageTypeDef]],
        "Frameworks": NotRequired[List[PlatformFrameworkTypeDef]],
        "CustomAmiList": NotRequired[List[CustomAmiTypeDef]],
        "SupportedTierList": NotRequired[List[str]],
        "SupportedAddonList": NotRequired[List[str]],
        "PlatformLifecycleState": NotRequired[str],
        "PlatformBranchName": NotRequired[str],
        "PlatformBranchLifecycleState": NotRequired[str],
    },
)
ResourceQuotasTypeDef = TypedDict(
    "ResourceQuotasTypeDef",
    {
        "ApplicationQuota": NotRequired[ResourceQuotaTypeDef],
        "ApplicationVersionQuota": NotRequired[ResourceQuotaTypeDef],
        "EnvironmentQuota": NotRequired[ResourceQuotaTypeDef],
        "ConfigurationTemplateQuota": NotRequired[ResourceQuotaTypeDef],
        "CustomPlatformQuota": NotRequired[ResourceQuotaTypeDef],
    },
)
DescribeEnvironmentHealthResultTypeDef = TypedDict(
    "DescribeEnvironmentHealthResultTypeDef",
    {
        "EnvironmentName": str,
        "HealthStatus": str,
        "Status": EnvironmentHealthType,
        "Color": str,
        "Causes": List[str],
        "ApplicationMetrics": ApplicationMetricsTypeDef,
        "InstancesHealth": InstanceHealthSummaryTypeDef,
        "RefreshedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ApplicationVersionDescriptionMessageTypeDef = TypedDict(
    "ApplicationVersionDescriptionMessageTypeDef",
    {
        "ApplicationVersion": ApplicationVersionDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ApplicationVersionDescriptionsMessageTypeDef = TypedDict(
    "ApplicationVersionDescriptionsMessageTypeDef",
    {
        "ApplicationVersions": List[ApplicationVersionDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ApplicationResourceLifecycleConfigTypeDef = TypedDict(
    "ApplicationResourceLifecycleConfigTypeDef",
    {
        "ServiceRole": NotRequired[str],
        "VersionLifecycleConfig": NotRequired[ApplicationVersionLifecycleConfigTypeDef],
    },
)
SingleInstanceHealthTypeDef = TypedDict(
    "SingleInstanceHealthTypeDef",
    {
        "InstanceId": NotRequired[str],
        "HealthStatus": NotRequired[str],
        "Color": NotRequired[str],
        "Causes": NotRequired[List[str]],
        "LaunchedAt": NotRequired[datetime],
        "ApplicationMetrics": NotRequired[ApplicationMetricsTypeDef],
        "System": NotRequired[SystemStatusTypeDef],
        "Deployment": NotRequired[DeploymentTypeDef],
        "AvailabilityZone": NotRequired[str],
        "InstanceType": NotRequired[str],
    },
)
ConfigurationOptionsDescriptionTypeDef = TypedDict(
    "ConfigurationOptionsDescriptionTypeDef",
    {
        "SolutionStackName": str,
        "PlatformArn": str,
        "Options": List[ConfigurationOptionDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConfigurationSettingsDescriptionsTypeDef = TypedDict(
    "ConfigurationSettingsDescriptionsTypeDef",
    {
        "ConfigurationSettings": List[ConfigurationSettingsDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnvironmentResourceDescriptionsMessageTypeDef = TypedDict(
    "EnvironmentResourceDescriptionsMessageTypeDef",
    {
        "EnvironmentResources": EnvironmentResourceDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnvironmentResourcesDescriptionTypeDef = TypedDict(
    "EnvironmentResourcesDescriptionTypeDef",
    {
        "LoadBalancer": NotRequired[LoadBalancerDescriptionTypeDef],
    },
)
DescribePlatformVersionResultTypeDef = TypedDict(
    "DescribePlatformVersionResultTypeDef",
    {
        "PlatformDescription": PlatformDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAccountAttributesResultTypeDef = TypedDict(
    "DescribeAccountAttributesResultTypeDef",
    {
        "ResourceQuotas": ResourceQuotasTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ApplicationDescriptionTypeDef = TypedDict(
    "ApplicationDescriptionTypeDef",
    {
        "ApplicationArn": NotRequired[str],
        "ApplicationName": NotRequired[str],
        "Description": NotRequired[str],
        "DateCreated": NotRequired[datetime],
        "DateUpdated": NotRequired[datetime],
        "Versions": NotRequired[List[str]],
        "ConfigurationTemplates": NotRequired[List[str]],
        "ResourceLifecycleConfig": NotRequired[ApplicationResourceLifecycleConfigTypeDef],
    },
)
ApplicationResourceLifecycleDescriptionMessageTypeDef = TypedDict(
    "ApplicationResourceLifecycleDescriptionMessageTypeDef",
    {
        "ApplicationName": str,
        "ResourceLifecycleConfig": ApplicationResourceLifecycleConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateApplicationMessageRequestTypeDef = TypedDict(
    "CreateApplicationMessageRequestTypeDef",
    {
        "ApplicationName": str,
        "Description": NotRequired[str],
        "ResourceLifecycleConfig": NotRequired[ApplicationResourceLifecycleConfigTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
UpdateApplicationResourceLifecycleMessageRequestTypeDef = TypedDict(
    "UpdateApplicationResourceLifecycleMessageRequestTypeDef",
    {
        "ApplicationName": str,
        "ResourceLifecycleConfig": ApplicationResourceLifecycleConfigTypeDef,
    },
)
DescribeInstancesHealthResultTypeDef = TypedDict(
    "DescribeInstancesHealthResultTypeDef",
    {
        "InstanceHealthList": List[SingleInstanceHealthTypeDef],
        "RefreshedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
EnvironmentDescriptionResponseTypeDef = TypedDict(
    "EnvironmentDescriptionResponseTypeDef",
    {
        "EnvironmentName": str,
        "EnvironmentId": str,
        "ApplicationName": str,
        "VersionLabel": str,
        "SolutionStackName": str,
        "PlatformArn": str,
        "TemplateName": str,
        "Description": str,
        "EndpointURL": str,
        "CNAME": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": EnvironmentStatusType,
        "AbortableOperationInProgress": bool,
        "Health": EnvironmentHealthType,
        "HealthStatus": EnvironmentHealthStatusType,
        "Resources": EnvironmentResourcesDescriptionTypeDef,
        "Tier": EnvironmentTierTypeDef,
        "EnvironmentLinks": List[EnvironmentLinkTypeDef],
        "EnvironmentArn": str,
        "OperationsRole": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnvironmentDescriptionTypeDef = TypedDict(
    "EnvironmentDescriptionTypeDef",
    {
        "EnvironmentName": NotRequired[str],
        "EnvironmentId": NotRequired[str],
        "ApplicationName": NotRequired[str],
        "VersionLabel": NotRequired[str],
        "SolutionStackName": NotRequired[str],
        "PlatformArn": NotRequired[str],
        "TemplateName": NotRequired[str],
        "Description": NotRequired[str],
        "EndpointURL": NotRequired[str],
        "CNAME": NotRequired[str],
        "DateCreated": NotRequired[datetime],
        "DateUpdated": NotRequired[datetime],
        "Status": NotRequired[EnvironmentStatusType],
        "AbortableOperationInProgress": NotRequired[bool],
        "Health": NotRequired[EnvironmentHealthType],
        "HealthStatus": NotRequired[EnvironmentHealthStatusType],
        "Resources": NotRequired[EnvironmentResourcesDescriptionTypeDef],
        "Tier": NotRequired[EnvironmentTierTypeDef],
        "EnvironmentLinks": NotRequired[List[EnvironmentLinkTypeDef]],
        "EnvironmentArn": NotRequired[str],
        "OperationsRole": NotRequired[str],
    },
)
ApplicationDescriptionMessageTypeDef = TypedDict(
    "ApplicationDescriptionMessageTypeDef",
    {
        "Application": ApplicationDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ApplicationDescriptionsMessageTypeDef = TypedDict(
    "ApplicationDescriptionsMessageTypeDef",
    {
        "Applications": List[ApplicationDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnvironmentDescriptionsMessageTypeDef = TypedDict(
    "EnvironmentDescriptionsMessageTypeDef",
    {
        "Environments": List[EnvironmentDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
