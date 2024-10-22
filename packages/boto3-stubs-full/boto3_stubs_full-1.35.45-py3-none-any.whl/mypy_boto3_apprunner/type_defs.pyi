"""
Type annotations for apprunner service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/type_defs/)

Usage::

    ```python
    from mypy_boto3_apprunner.type_defs import AssociateCustomDomainRequestRequestTypeDef

    data: AssociateCustomDomainRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AutoScalingConfigurationStatusType,
    CertificateValidationRecordStatusType,
    ConfigurationSourceType,
    ConnectionStatusType,
    CustomDomainAssociationStatusType,
    EgressTypeType,
    HealthCheckProtocolType,
    ImageRepositoryTypeType,
    IpAddressTypeType,
    ObservabilityConfigurationStatusType,
    OperationStatusType,
    OperationTypeType,
    ProviderTypeType,
    RuntimeType,
    ServiceStatusType,
    VpcConnectorStatusType,
    VpcIngressConnectionStatusType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AssociateCustomDomainRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "VpcDNSTargetTypeDef",
    "AuthenticationConfigurationTypeDef",
    "AutoScalingConfigurationSummaryTypeDef",
    "AutoScalingConfigurationTypeDef",
    "CertificateValidationRecordTypeDef",
    "CodeConfigurationValuesOutputTypeDef",
    "CodeConfigurationValuesTypeDef",
    "SourceCodeVersionTypeDef",
    "ConnectionSummaryTypeDef",
    "ConnectionTypeDef",
    "TagTypeDef",
    "TraceConfigurationTypeDef",
    "EncryptionConfigurationTypeDef",
    "HealthCheckConfigurationTypeDef",
    "InstanceConfigurationTypeDef",
    "ServiceObservabilityConfigurationTypeDef",
    "VpcConnectorTypeDef",
    "IngressVpcConfigurationTypeDef",
    "DeleteAutoScalingConfigurationRequestRequestTypeDef",
    "DeleteConnectionRequestRequestTypeDef",
    "DeleteObservabilityConfigurationRequestRequestTypeDef",
    "DeleteServiceRequestRequestTypeDef",
    "DeleteVpcConnectorRequestRequestTypeDef",
    "DeleteVpcIngressConnectionRequestRequestTypeDef",
    "DescribeAutoScalingConfigurationRequestRequestTypeDef",
    "DescribeCustomDomainsRequestRequestTypeDef",
    "DescribeObservabilityConfigurationRequestRequestTypeDef",
    "DescribeServiceRequestRequestTypeDef",
    "DescribeVpcConnectorRequestRequestTypeDef",
    "DescribeVpcIngressConnectionRequestRequestTypeDef",
    "DisassociateCustomDomainRequestRequestTypeDef",
    "EgressConfigurationTypeDef",
    "ImageConfigurationOutputTypeDef",
    "ImageConfigurationTypeDef",
    "IngressConfigurationTypeDef",
    "ListAutoScalingConfigurationsRequestRequestTypeDef",
    "ListConnectionsRequestRequestTypeDef",
    "ListObservabilityConfigurationsRequestRequestTypeDef",
    "ObservabilityConfigurationSummaryTypeDef",
    "ListOperationsRequestRequestTypeDef",
    "OperationSummaryTypeDef",
    "ListServicesForAutoScalingConfigurationRequestRequestTypeDef",
    "ListServicesRequestRequestTypeDef",
    "ServiceSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListVpcConnectorsRequestRequestTypeDef",
    "ListVpcIngressConnectionsFilterTypeDef",
    "VpcIngressConnectionSummaryTypeDef",
    "PauseServiceRequestRequestTypeDef",
    "ResumeServiceRequestRequestTypeDef",
    "StartDeploymentRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDefaultAutoScalingConfigurationRequestRequestTypeDef",
    "ListServicesForAutoScalingConfigurationResponseTypeDef",
    "StartDeploymentResponseTypeDef",
    "ListAutoScalingConfigurationsResponseTypeDef",
    "CreateAutoScalingConfigurationResponseTypeDef",
    "DeleteAutoScalingConfigurationResponseTypeDef",
    "DescribeAutoScalingConfigurationResponseTypeDef",
    "UpdateDefaultAutoScalingConfigurationResponseTypeDef",
    "CustomDomainTypeDef",
    "CodeConfigurationOutputTypeDef",
    "CodeConfigurationValuesUnionTypeDef",
    "ListConnectionsResponseTypeDef",
    "CreateConnectionResponseTypeDef",
    "DeleteConnectionResponseTypeDef",
    "CreateAutoScalingConfigurationRequestRequestTypeDef",
    "CreateConnectionRequestRequestTypeDef",
    "CreateVpcConnectorRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateObservabilityConfigurationRequestRequestTypeDef",
    "ObservabilityConfigurationTypeDef",
    "CreateVpcConnectorResponseTypeDef",
    "DeleteVpcConnectorResponseTypeDef",
    "DescribeVpcConnectorResponseTypeDef",
    "ListVpcConnectorsResponseTypeDef",
    "CreateVpcIngressConnectionRequestRequestTypeDef",
    "UpdateVpcIngressConnectionRequestRequestTypeDef",
    "VpcIngressConnectionTypeDef",
    "ImageRepositoryOutputTypeDef",
    "ImageConfigurationUnionTypeDef",
    "NetworkConfigurationTypeDef",
    "ListObservabilityConfigurationsResponseTypeDef",
    "ListOperationsResponseTypeDef",
    "ListServicesResponseTypeDef",
    "ListVpcIngressConnectionsRequestRequestTypeDef",
    "ListVpcIngressConnectionsResponseTypeDef",
    "AssociateCustomDomainResponseTypeDef",
    "DescribeCustomDomainsResponseTypeDef",
    "DisassociateCustomDomainResponseTypeDef",
    "CodeRepositoryOutputTypeDef",
    "CodeConfigurationTypeDef",
    "CreateObservabilityConfigurationResponseTypeDef",
    "DeleteObservabilityConfigurationResponseTypeDef",
    "DescribeObservabilityConfigurationResponseTypeDef",
    "CreateVpcIngressConnectionResponseTypeDef",
    "DeleteVpcIngressConnectionResponseTypeDef",
    "DescribeVpcIngressConnectionResponseTypeDef",
    "UpdateVpcIngressConnectionResponseTypeDef",
    "ImageRepositoryTypeDef",
    "SourceConfigurationOutputTypeDef",
    "CodeConfigurationUnionTypeDef",
    "ImageRepositoryUnionTypeDef",
    "ServiceTypeDef",
    "CodeRepositoryTypeDef",
    "CreateServiceResponseTypeDef",
    "DeleteServiceResponseTypeDef",
    "DescribeServiceResponseTypeDef",
    "PauseServiceResponseTypeDef",
    "ResumeServiceResponseTypeDef",
    "UpdateServiceResponseTypeDef",
    "CodeRepositoryUnionTypeDef",
    "SourceConfigurationTypeDef",
    "CreateServiceRequestRequestTypeDef",
    "UpdateServiceRequestRequestTypeDef",
)

AssociateCustomDomainRequestRequestTypeDef = TypedDict(
    "AssociateCustomDomainRequestRequestTypeDef",
    {
        "ServiceArn": str,
        "DomainName": str,
        "EnableWWWSubdomain": NotRequired[bool],
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
VpcDNSTargetTypeDef = TypedDict(
    "VpcDNSTargetTypeDef",
    {
        "VpcIngressConnectionArn": NotRequired[str],
        "VpcId": NotRequired[str],
        "DomainName": NotRequired[str],
    },
)
AuthenticationConfigurationTypeDef = TypedDict(
    "AuthenticationConfigurationTypeDef",
    {
        "ConnectionArn": NotRequired[str],
        "AccessRoleArn": NotRequired[str],
    },
)
AutoScalingConfigurationSummaryTypeDef = TypedDict(
    "AutoScalingConfigurationSummaryTypeDef",
    {
        "AutoScalingConfigurationArn": NotRequired[str],
        "AutoScalingConfigurationName": NotRequired[str],
        "AutoScalingConfigurationRevision": NotRequired[int],
        "Status": NotRequired[AutoScalingConfigurationStatusType],
        "CreatedAt": NotRequired[datetime],
        "HasAssociatedService": NotRequired[bool],
        "IsDefault": NotRequired[bool],
    },
)
AutoScalingConfigurationTypeDef = TypedDict(
    "AutoScalingConfigurationTypeDef",
    {
        "AutoScalingConfigurationArn": NotRequired[str],
        "AutoScalingConfigurationName": NotRequired[str],
        "AutoScalingConfigurationRevision": NotRequired[int],
        "Latest": NotRequired[bool],
        "Status": NotRequired[AutoScalingConfigurationStatusType],
        "MaxConcurrency": NotRequired[int],
        "MinSize": NotRequired[int],
        "MaxSize": NotRequired[int],
        "CreatedAt": NotRequired[datetime],
        "DeletedAt": NotRequired[datetime],
        "HasAssociatedService": NotRequired[bool],
        "IsDefault": NotRequired[bool],
    },
)
CertificateValidationRecordTypeDef = TypedDict(
    "CertificateValidationRecordTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
        "Value": NotRequired[str],
        "Status": NotRequired[CertificateValidationRecordStatusType],
    },
)
CodeConfigurationValuesOutputTypeDef = TypedDict(
    "CodeConfigurationValuesOutputTypeDef",
    {
        "Runtime": RuntimeType,
        "BuildCommand": NotRequired[str],
        "StartCommand": NotRequired[str],
        "Port": NotRequired[str],
        "RuntimeEnvironmentVariables": NotRequired[Dict[str, str]],
        "RuntimeEnvironmentSecrets": NotRequired[Dict[str, str]],
    },
)
CodeConfigurationValuesTypeDef = TypedDict(
    "CodeConfigurationValuesTypeDef",
    {
        "Runtime": RuntimeType,
        "BuildCommand": NotRequired[str],
        "StartCommand": NotRequired[str],
        "Port": NotRequired[str],
        "RuntimeEnvironmentVariables": NotRequired[Mapping[str, str]],
        "RuntimeEnvironmentSecrets": NotRequired[Mapping[str, str]],
    },
)
SourceCodeVersionTypeDef = TypedDict(
    "SourceCodeVersionTypeDef",
    {
        "Type": Literal["BRANCH"],
        "Value": str,
    },
)
ConnectionSummaryTypeDef = TypedDict(
    "ConnectionSummaryTypeDef",
    {
        "ConnectionName": NotRequired[str],
        "ConnectionArn": NotRequired[str],
        "ProviderType": NotRequired[ProviderTypeType],
        "Status": NotRequired[ConnectionStatusType],
        "CreatedAt": NotRequired[datetime],
    },
)
ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "ConnectionName": NotRequired[str],
        "ConnectionArn": NotRequired[str],
        "ProviderType": NotRequired[ProviderTypeType],
        "Status": NotRequired[ConnectionStatusType],
        "CreatedAt": NotRequired[datetime],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
TraceConfigurationTypeDef = TypedDict(
    "TraceConfigurationTypeDef",
    {
        "Vendor": Literal["AWSXRAY"],
    },
)
EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "KmsKey": str,
    },
)
HealthCheckConfigurationTypeDef = TypedDict(
    "HealthCheckConfigurationTypeDef",
    {
        "Protocol": NotRequired[HealthCheckProtocolType],
        "Path": NotRequired[str],
        "Interval": NotRequired[int],
        "Timeout": NotRequired[int],
        "HealthyThreshold": NotRequired[int],
        "UnhealthyThreshold": NotRequired[int],
    },
)
InstanceConfigurationTypeDef = TypedDict(
    "InstanceConfigurationTypeDef",
    {
        "Cpu": NotRequired[str],
        "Memory": NotRequired[str],
        "InstanceRoleArn": NotRequired[str],
    },
)
ServiceObservabilityConfigurationTypeDef = TypedDict(
    "ServiceObservabilityConfigurationTypeDef",
    {
        "ObservabilityEnabled": bool,
        "ObservabilityConfigurationArn": NotRequired[str],
    },
)
VpcConnectorTypeDef = TypedDict(
    "VpcConnectorTypeDef",
    {
        "VpcConnectorName": NotRequired[str],
        "VpcConnectorArn": NotRequired[str],
        "VpcConnectorRevision": NotRequired[int],
        "Subnets": NotRequired[List[str]],
        "SecurityGroups": NotRequired[List[str]],
        "Status": NotRequired[VpcConnectorStatusType],
        "CreatedAt": NotRequired[datetime],
        "DeletedAt": NotRequired[datetime],
    },
)
IngressVpcConfigurationTypeDef = TypedDict(
    "IngressVpcConfigurationTypeDef",
    {
        "VpcId": NotRequired[str],
        "VpcEndpointId": NotRequired[str],
    },
)
DeleteAutoScalingConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteAutoScalingConfigurationRequestRequestTypeDef",
    {
        "AutoScalingConfigurationArn": str,
        "DeleteAllRevisions": NotRequired[bool],
    },
)
DeleteConnectionRequestRequestTypeDef = TypedDict(
    "DeleteConnectionRequestRequestTypeDef",
    {
        "ConnectionArn": str,
    },
)
DeleteObservabilityConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteObservabilityConfigurationRequestRequestTypeDef",
    {
        "ObservabilityConfigurationArn": str,
    },
)
DeleteServiceRequestRequestTypeDef = TypedDict(
    "DeleteServiceRequestRequestTypeDef",
    {
        "ServiceArn": str,
    },
)
DeleteVpcConnectorRequestRequestTypeDef = TypedDict(
    "DeleteVpcConnectorRequestRequestTypeDef",
    {
        "VpcConnectorArn": str,
    },
)
DeleteVpcIngressConnectionRequestRequestTypeDef = TypedDict(
    "DeleteVpcIngressConnectionRequestRequestTypeDef",
    {
        "VpcIngressConnectionArn": str,
    },
)
DescribeAutoScalingConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeAutoScalingConfigurationRequestRequestTypeDef",
    {
        "AutoScalingConfigurationArn": str,
    },
)
DescribeCustomDomainsRequestRequestTypeDef = TypedDict(
    "DescribeCustomDomainsRequestRequestTypeDef",
    {
        "ServiceArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeObservabilityConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeObservabilityConfigurationRequestRequestTypeDef",
    {
        "ObservabilityConfigurationArn": str,
    },
)
DescribeServiceRequestRequestTypeDef = TypedDict(
    "DescribeServiceRequestRequestTypeDef",
    {
        "ServiceArn": str,
    },
)
DescribeVpcConnectorRequestRequestTypeDef = TypedDict(
    "DescribeVpcConnectorRequestRequestTypeDef",
    {
        "VpcConnectorArn": str,
    },
)
DescribeVpcIngressConnectionRequestRequestTypeDef = TypedDict(
    "DescribeVpcIngressConnectionRequestRequestTypeDef",
    {
        "VpcIngressConnectionArn": str,
    },
)
DisassociateCustomDomainRequestRequestTypeDef = TypedDict(
    "DisassociateCustomDomainRequestRequestTypeDef",
    {
        "ServiceArn": str,
        "DomainName": str,
    },
)
EgressConfigurationTypeDef = TypedDict(
    "EgressConfigurationTypeDef",
    {
        "EgressType": NotRequired[EgressTypeType],
        "VpcConnectorArn": NotRequired[str],
    },
)
ImageConfigurationOutputTypeDef = TypedDict(
    "ImageConfigurationOutputTypeDef",
    {
        "RuntimeEnvironmentVariables": NotRequired[Dict[str, str]],
        "StartCommand": NotRequired[str],
        "Port": NotRequired[str],
        "RuntimeEnvironmentSecrets": NotRequired[Dict[str, str]],
    },
)
ImageConfigurationTypeDef = TypedDict(
    "ImageConfigurationTypeDef",
    {
        "RuntimeEnvironmentVariables": NotRequired[Mapping[str, str]],
        "StartCommand": NotRequired[str],
        "Port": NotRequired[str],
        "RuntimeEnvironmentSecrets": NotRequired[Mapping[str, str]],
    },
)
IngressConfigurationTypeDef = TypedDict(
    "IngressConfigurationTypeDef",
    {
        "IsPubliclyAccessible": NotRequired[bool],
    },
)
ListAutoScalingConfigurationsRequestRequestTypeDef = TypedDict(
    "ListAutoScalingConfigurationsRequestRequestTypeDef",
    {
        "AutoScalingConfigurationName": NotRequired[str],
        "LatestOnly": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListConnectionsRequestRequestTypeDef = TypedDict(
    "ListConnectionsRequestRequestTypeDef",
    {
        "ConnectionName": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListObservabilityConfigurationsRequestRequestTypeDef = TypedDict(
    "ListObservabilityConfigurationsRequestRequestTypeDef",
    {
        "ObservabilityConfigurationName": NotRequired[str],
        "LatestOnly": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ObservabilityConfigurationSummaryTypeDef = TypedDict(
    "ObservabilityConfigurationSummaryTypeDef",
    {
        "ObservabilityConfigurationArn": NotRequired[str],
        "ObservabilityConfigurationName": NotRequired[str],
        "ObservabilityConfigurationRevision": NotRequired[int],
    },
)
ListOperationsRequestRequestTypeDef = TypedDict(
    "ListOperationsRequestRequestTypeDef",
    {
        "ServiceArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
OperationSummaryTypeDef = TypedDict(
    "OperationSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Type": NotRequired[OperationTypeType],
        "Status": NotRequired[OperationStatusType],
        "TargetArn": NotRequired[str],
        "StartedAt": NotRequired[datetime],
        "EndedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
    },
)
ListServicesForAutoScalingConfigurationRequestRequestTypeDef = TypedDict(
    "ListServicesForAutoScalingConfigurationRequestRequestTypeDef",
    {
        "AutoScalingConfigurationArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListServicesRequestRequestTypeDef = TypedDict(
    "ListServicesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ServiceSummaryTypeDef = TypedDict(
    "ServiceSummaryTypeDef",
    {
        "ServiceName": NotRequired[str],
        "ServiceId": NotRequired[str],
        "ServiceArn": NotRequired[str],
        "ServiceUrl": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
        "Status": NotRequired[ServiceStatusType],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
ListVpcConnectorsRequestRequestTypeDef = TypedDict(
    "ListVpcConnectorsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListVpcIngressConnectionsFilterTypeDef = TypedDict(
    "ListVpcIngressConnectionsFilterTypeDef",
    {
        "ServiceArn": NotRequired[str],
        "VpcEndpointId": NotRequired[str],
    },
)
VpcIngressConnectionSummaryTypeDef = TypedDict(
    "VpcIngressConnectionSummaryTypeDef",
    {
        "VpcIngressConnectionArn": NotRequired[str],
        "ServiceArn": NotRequired[str],
    },
)
PauseServiceRequestRequestTypeDef = TypedDict(
    "PauseServiceRequestRequestTypeDef",
    {
        "ServiceArn": str,
    },
)
ResumeServiceRequestRequestTypeDef = TypedDict(
    "ResumeServiceRequestRequestTypeDef",
    {
        "ServiceArn": str,
    },
)
StartDeploymentRequestRequestTypeDef = TypedDict(
    "StartDeploymentRequestRequestTypeDef",
    {
        "ServiceArn": str,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateDefaultAutoScalingConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateDefaultAutoScalingConfigurationRequestRequestTypeDef",
    {
        "AutoScalingConfigurationArn": str,
    },
)
ListServicesForAutoScalingConfigurationResponseTypeDef = TypedDict(
    "ListServicesForAutoScalingConfigurationResponseTypeDef",
    {
        "ServiceArnList": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
StartDeploymentResponseTypeDef = TypedDict(
    "StartDeploymentResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAutoScalingConfigurationsResponseTypeDef = TypedDict(
    "ListAutoScalingConfigurationsResponseTypeDef",
    {
        "AutoScalingConfigurationSummaryList": List[AutoScalingConfigurationSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateAutoScalingConfigurationResponseTypeDef = TypedDict(
    "CreateAutoScalingConfigurationResponseTypeDef",
    {
        "AutoScalingConfiguration": AutoScalingConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteAutoScalingConfigurationResponseTypeDef = TypedDict(
    "DeleteAutoScalingConfigurationResponseTypeDef",
    {
        "AutoScalingConfiguration": AutoScalingConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAutoScalingConfigurationResponseTypeDef = TypedDict(
    "DescribeAutoScalingConfigurationResponseTypeDef",
    {
        "AutoScalingConfiguration": AutoScalingConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDefaultAutoScalingConfigurationResponseTypeDef = TypedDict(
    "UpdateDefaultAutoScalingConfigurationResponseTypeDef",
    {
        "AutoScalingConfiguration": AutoScalingConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CustomDomainTypeDef = TypedDict(
    "CustomDomainTypeDef",
    {
        "DomainName": str,
        "EnableWWWSubdomain": bool,
        "Status": CustomDomainAssociationStatusType,
        "CertificateValidationRecords": NotRequired[List[CertificateValidationRecordTypeDef]],
    },
)
CodeConfigurationOutputTypeDef = TypedDict(
    "CodeConfigurationOutputTypeDef",
    {
        "ConfigurationSource": ConfigurationSourceType,
        "CodeConfigurationValues": NotRequired[CodeConfigurationValuesOutputTypeDef],
    },
)
CodeConfigurationValuesUnionTypeDef = Union[
    CodeConfigurationValuesTypeDef, CodeConfigurationValuesOutputTypeDef
]
ListConnectionsResponseTypeDef = TypedDict(
    "ListConnectionsResponseTypeDef",
    {
        "ConnectionSummaryList": List[ConnectionSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateConnectionResponseTypeDef = TypedDict(
    "CreateConnectionResponseTypeDef",
    {
        "Connection": ConnectionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteConnectionResponseTypeDef = TypedDict(
    "DeleteConnectionResponseTypeDef",
    {
        "Connection": ConnectionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAutoScalingConfigurationRequestRequestTypeDef = TypedDict(
    "CreateAutoScalingConfigurationRequestRequestTypeDef",
    {
        "AutoScalingConfigurationName": str,
        "MaxConcurrency": NotRequired[int],
        "MinSize": NotRequired[int],
        "MaxSize": NotRequired[int],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateConnectionRequestRequestTypeDef = TypedDict(
    "CreateConnectionRequestRequestTypeDef",
    {
        "ConnectionName": str,
        "ProviderType": ProviderTypeType,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateVpcConnectorRequestRequestTypeDef = TypedDict(
    "CreateVpcConnectorRequestRequestTypeDef",
    {
        "VpcConnectorName": str,
        "Subnets": Sequence[str],
        "SecurityGroups": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CreateObservabilityConfigurationRequestRequestTypeDef = TypedDict(
    "CreateObservabilityConfigurationRequestRequestTypeDef",
    {
        "ObservabilityConfigurationName": str,
        "TraceConfiguration": NotRequired[TraceConfigurationTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ObservabilityConfigurationTypeDef = TypedDict(
    "ObservabilityConfigurationTypeDef",
    {
        "ObservabilityConfigurationArn": NotRequired[str],
        "ObservabilityConfigurationName": NotRequired[str],
        "TraceConfiguration": NotRequired[TraceConfigurationTypeDef],
        "ObservabilityConfigurationRevision": NotRequired[int],
        "Latest": NotRequired[bool],
        "Status": NotRequired[ObservabilityConfigurationStatusType],
        "CreatedAt": NotRequired[datetime],
        "DeletedAt": NotRequired[datetime],
    },
)
CreateVpcConnectorResponseTypeDef = TypedDict(
    "CreateVpcConnectorResponseTypeDef",
    {
        "VpcConnector": VpcConnectorTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteVpcConnectorResponseTypeDef = TypedDict(
    "DeleteVpcConnectorResponseTypeDef",
    {
        "VpcConnector": VpcConnectorTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeVpcConnectorResponseTypeDef = TypedDict(
    "DescribeVpcConnectorResponseTypeDef",
    {
        "VpcConnector": VpcConnectorTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListVpcConnectorsResponseTypeDef = TypedDict(
    "ListVpcConnectorsResponseTypeDef",
    {
        "VpcConnectors": List[VpcConnectorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateVpcIngressConnectionRequestRequestTypeDef = TypedDict(
    "CreateVpcIngressConnectionRequestRequestTypeDef",
    {
        "ServiceArn": str,
        "VpcIngressConnectionName": str,
        "IngressVpcConfiguration": IngressVpcConfigurationTypeDef,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
UpdateVpcIngressConnectionRequestRequestTypeDef = TypedDict(
    "UpdateVpcIngressConnectionRequestRequestTypeDef",
    {
        "VpcIngressConnectionArn": str,
        "IngressVpcConfiguration": IngressVpcConfigurationTypeDef,
    },
)
VpcIngressConnectionTypeDef = TypedDict(
    "VpcIngressConnectionTypeDef",
    {
        "VpcIngressConnectionArn": NotRequired[str],
        "VpcIngressConnectionName": NotRequired[str],
        "ServiceArn": NotRequired[str],
        "Status": NotRequired[VpcIngressConnectionStatusType],
        "AccountId": NotRequired[str],
        "DomainName": NotRequired[str],
        "IngressVpcConfiguration": NotRequired[IngressVpcConfigurationTypeDef],
        "CreatedAt": NotRequired[datetime],
        "DeletedAt": NotRequired[datetime],
    },
)
ImageRepositoryOutputTypeDef = TypedDict(
    "ImageRepositoryOutputTypeDef",
    {
        "ImageIdentifier": str,
        "ImageRepositoryType": ImageRepositoryTypeType,
        "ImageConfiguration": NotRequired[ImageConfigurationOutputTypeDef],
    },
)
ImageConfigurationUnionTypeDef = Union[ImageConfigurationTypeDef, ImageConfigurationOutputTypeDef]
NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {
        "EgressConfiguration": NotRequired[EgressConfigurationTypeDef],
        "IngressConfiguration": NotRequired[IngressConfigurationTypeDef],
        "IpAddressType": NotRequired[IpAddressTypeType],
    },
)
ListObservabilityConfigurationsResponseTypeDef = TypedDict(
    "ListObservabilityConfigurationsResponseTypeDef",
    {
        "ObservabilityConfigurationSummaryList": List[ObservabilityConfigurationSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListOperationsResponseTypeDef = TypedDict(
    "ListOperationsResponseTypeDef",
    {
        "OperationSummaryList": List[OperationSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListServicesResponseTypeDef = TypedDict(
    "ListServicesResponseTypeDef",
    {
        "ServiceSummaryList": List[ServiceSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListVpcIngressConnectionsRequestRequestTypeDef = TypedDict(
    "ListVpcIngressConnectionsRequestRequestTypeDef",
    {
        "Filter": NotRequired[ListVpcIngressConnectionsFilterTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListVpcIngressConnectionsResponseTypeDef = TypedDict(
    "ListVpcIngressConnectionsResponseTypeDef",
    {
        "VpcIngressConnectionSummaryList": List[VpcIngressConnectionSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
AssociateCustomDomainResponseTypeDef = TypedDict(
    "AssociateCustomDomainResponseTypeDef",
    {
        "DNSTarget": str,
        "ServiceArn": str,
        "CustomDomain": CustomDomainTypeDef,
        "VpcDNSTargets": List[VpcDNSTargetTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeCustomDomainsResponseTypeDef = TypedDict(
    "DescribeCustomDomainsResponseTypeDef",
    {
        "DNSTarget": str,
        "ServiceArn": str,
        "CustomDomains": List[CustomDomainTypeDef],
        "VpcDNSTargets": List[VpcDNSTargetTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DisassociateCustomDomainResponseTypeDef = TypedDict(
    "DisassociateCustomDomainResponseTypeDef",
    {
        "DNSTarget": str,
        "ServiceArn": str,
        "CustomDomain": CustomDomainTypeDef,
        "VpcDNSTargets": List[VpcDNSTargetTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CodeRepositoryOutputTypeDef = TypedDict(
    "CodeRepositoryOutputTypeDef",
    {
        "RepositoryUrl": str,
        "SourceCodeVersion": SourceCodeVersionTypeDef,
        "CodeConfiguration": NotRequired[CodeConfigurationOutputTypeDef],
        "SourceDirectory": NotRequired[str],
    },
)
CodeConfigurationTypeDef = TypedDict(
    "CodeConfigurationTypeDef",
    {
        "ConfigurationSource": ConfigurationSourceType,
        "CodeConfigurationValues": NotRequired[CodeConfigurationValuesUnionTypeDef],
    },
)
CreateObservabilityConfigurationResponseTypeDef = TypedDict(
    "CreateObservabilityConfigurationResponseTypeDef",
    {
        "ObservabilityConfiguration": ObservabilityConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteObservabilityConfigurationResponseTypeDef = TypedDict(
    "DeleteObservabilityConfigurationResponseTypeDef",
    {
        "ObservabilityConfiguration": ObservabilityConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeObservabilityConfigurationResponseTypeDef = TypedDict(
    "DescribeObservabilityConfigurationResponseTypeDef",
    {
        "ObservabilityConfiguration": ObservabilityConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateVpcIngressConnectionResponseTypeDef = TypedDict(
    "CreateVpcIngressConnectionResponseTypeDef",
    {
        "VpcIngressConnection": VpcIngressConnectionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteVpcIngressConnectionResponseTypeDef = TypedDict(
    "DeleteVpcIngressConnectionResponseTypeDef",
    {
        "VpcIngressConnection": VpcIngressConnectionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeVpcIngressConnectionResponseTypeDef = TypedDict(
    "DescribeVpcIngressConnectionResponseTypeDef",
    {
        "VpcIngressConnection": VpcIngressConnectionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateVpcIngressConnectionResponseTypeDef = TypedDict(
    "UpdateVpcIngressConnectionResponseTypeDef",
    {
        "VpcIngressConnection": VpcIngressConnectionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImageRepositoryTypeDef = TypedDict(
    "ImageRepositoryTypeDef",
    {
        "ImageIdentifier": str,
        "ImageRepositoryType": ImageRepositoryTypeType,
        "ImageConfiguration": NotRequired[ImageConfigurationUnionTypeDef],
    },
)
SourceConfigurationOutputTypeDef = TypedDict(
    "SourceConfigurationOutputTypeDef",
    {
        "CodeRepository": NotRequired[CodeRepositoryOutputTypeDef],
        "ImageRepository": NotRequired[ImageRepositoryOutputTypeDef],
        "AutoDeploymentsEnabled": NotRequired[bool],
        "AuthenticationConfiguration": NotRequired[AuthenticationConfigurationTypeDef],
    },
)
CodeConfigurationUnionTypeDef = Union[CodeConfigurationTypeDef, CodeConfigurationOutputTypeDef]
ImageRepositoryUnionTypeDef = Union[ImageRepositoryTypeDef, ImageRepositoryOutputTypeDef]
ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "ServiceName": str,
        "ServiceId": str,
        "ServiceArn": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Status": ServiceStatusType,
        "SourceConfiguration": SourceConfigurationOutputTypeDef,
        "InstanceConfiguration": InstanceConfigurationTypeDef,
        "AutoScalingConfigurationSummary": AutoScalingConfigurationSummaryTypeDef,
        "NetworkConfiguration": NetworkConfigurationTypeDef,
        "ServiceUrl": NotRequired[str],
        "DeletedAt": NotRequired[datetime],
        "EncryptionConfiguration": NotRequired[EncryptionConfigurationTypeDef],
        "HealthCheckConfiguration": NotRequired[HealthCheckConfigurationTypeDef],
        "ObservabilityConfiguration": NotRequired[ServiceObservabilityConfigurationTypeDef],
    },
)
CodeRepositoryTypeDef = TypedDict(
    "CodeRepositoryTypeDef",
    {
        "RepositoryUrl": str,
        "SourceCodeVersion": SourceCodeVersionTypeDef,
        "CodeConfiguration": NotRequired[CodeConfigurationUnionTypeDef],
        "SourceDirectory": NotRequired[str],
    },
)
CreateServiceResponseTypeDef = TypedDict(
    "CreateServiceResponseTypeDef",
    {
        "Service": ServiceTypeDef,
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteServiceResponseTypeDef = TypedDict(
    "DeleteServiceResponseTypeDef",
    {
        "Service": ServiceTypeDef,
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeServiceResponseTypeDef = TypedDict(
    "DescribeServiceResponseTypeDef",
    {
        "Service": ServiceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PauseServiceResponseTypeDef = TypedDict(
    "PauseServiceResponseTypeDef",
    {
        "Service": ServiceTypeDef,
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResumeServiceResponseTypeDef = TypedDict(
    "ResumeServiceResponseTypeDef",
    {
        "Service": ServiceTypeDef,
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateServiceResponseTypeDef = TypedDict(
    "UpdateServiceResponseTypeDef",
    {
        "Service": ServiceTypeDef,
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CodeRepositoryUnionTypeDef = Union[CodeRepositoryTypeDef, CodeRepositoryOutputTypeDef]
SourceConfigurationTypeDef = TypedDict(
    "SourceConfigurationTypeDef",
    {
        "CodeRepository": NotRequired[CodeRepositoryUnionTypeDef],
        "ImageRepository": NotRequired[ImageRepositoryUnionTypeDef],
        "AutoDeploymentsEnabled": NotRequired[bool],
        "AuthenticationConfiguration": NotRequired[AuthenticationConfigurationTypeDef],
    },
)
CreateServiceRequestRequestTypeDef = TypedDict(
    "CreateServiceRequestRequestTypeDef",
    {
        "ServiceName": str,
        "SourceConfiguration": SourceConfigurationTypeDef,
        "InstanceConfiguration": NotRequired[InstanceConfigurationTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "EncryptionConfiguration": NotRequired[EncryptionConfigurationTypeDef],
        "HealthCheckConfiguration": NotRequired[HealthCheckConfigurationTypeDef],
        "AutoScalingConfigurationArn": NotRequired[str],
        "NetworkConfiguration": NotRequired[NetworkConfigurationTypeDef],
        "ObservabilityConfiguration": NotRequired[ServiceObservabilityConfigurationTypeDef],
    },
)
UpdateServiceRequestRequestTypeDef = TypedDict(
    "UpdateServiceRequestRequestTypeDef",
    {
        "ServiceArn": str,
        "SourceConfiguration": NotRequired[SourceConfigurationTypeDef],
        "InstanceConfiguration": NotRequired[InstanceConfigurationTypeDef],
        "AutoScalingConfigurationArn": NotRequired[str],
        "HealthCheckConfiguration": NotRequired[HealthCheckConfigurationTypeDef],
        "NetworkConfiguration": NotRequired[NetworkConfigurationTypeDef],
        "ObservabilityConfiguration": NotRequired[ServiceObservabilityConfigurationTypeDef],
    },
)
