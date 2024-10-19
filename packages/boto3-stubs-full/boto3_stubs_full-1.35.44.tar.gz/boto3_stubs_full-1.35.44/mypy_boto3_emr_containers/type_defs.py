"""
Type annotations for emr-containers service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/type_defs/)

Usage::

    ```python
    from mypy_boto3_emr_containers.type_defs import CancelJobRunRequestRequestTypeDef

    data: CancelJobRunRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    EndpointStateType,
    FailureReasonType,
    JobRunStateType,
    PersistentAppUIType,
    TemplateParameterDataTypeType,
    VirtualClusterStateType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "CancelJobRunRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CertificateTypeDef",
    "CloudWatchMonitoringConfigurationTypeDef",
    "ConfigurationOutputTypeDef",
    "ConfigurationPaginatorTypeDef",
    "ConfigurationTypeDef",
    "EksInfoTypeDef",
    "ContainerLogRotationConfigurationTypeDef",
    "CredentialsTypeDef",
    "DeleteJobTemplateRequestRequestTypeDef",
    "DeleteManagedEndpointRequestRequestTypeDef",
    "DeleteVirtualClusterRequestRequestTypeDef",
    "DescribeJobRunRequestRequestTypeDef",
    "DescribeJobTemplateRequestRequestTypeDef",
    "DescribeManagedEndpointRequestRequestTypeDef",
    "DescribeSecurityConfigurationRequestRequestTypeDef",
    "DescribeVirtualClusterRequestRequestTypeDef",
    "GetManagedEndpointSessionCredentialsRequestRequestTypeDef",
    "TLSCertificateConfigurationTypeDef",
    "SparkSqlJobDriverTypeDef",
    "SparkSubmitJobDriverOutputTypeDef",
    "RetryPolicyConfigurationTypeDef",
    "RetryPolicyExecutionTypeDef",
    "TemplateParameterConfigurationTypeDef",
    "SecureNamespaceInfoTypeDef",
    "PaginatorConfigTypeDef",
    "TimestampTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "S3MonitoringConfigurationTypeDef",
    "ParametricCloudWatchMonitoringConfigurationTypeDef",
    "ParametricS3MonitoringConfigurationTypeDef",
    "SparkSubmitJobDriverTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "CancelJobRunResponseTypeDef",
    "CreateJobTemplateResponseTypeDef",
    "CreateManagedEndpointResponseTypeDef",
    "CreateSecurityConfigurationResponseTypeDef",
    "CreateVirtualClusterResponseTypeDef",
    "DeleteJobTemplateResponseTypeDef",
    "DeleteManagedEndpointResponseTypeDef",
    "DeleteVirtualClusterResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartJobRunResponseTypeDef",
    "ConfigurationUnionTypeDef",
    "ContainerInfoTypeDef",
    "GetManagedEndpointSessionCredentialsResponseTypeDef",
    "InTransitEncryptionConfigurationTypeDef",
    "JobDriverOutputTypeDef",
    "LakeFormationConfigurationTypeDef",
    "ListJobRunsRequestListJobRunsPaginateTypeDef",
    "ListJobRunsRequestRequestTypeDef",
    "ListJobTemplatesRequestListJobTemplatesPaginateTypeDef",
    "ListJobTemplatesRequestRequestTypeDef",
    "ListManagedEndpointsRequestListManagedEndpointsPaginateTypeDef",
    "ListManagedEndpointsRequestRequestTypeDef",
    "ListSecurityConfigurationsRequestListSecurityConfigurationsPaginateTypeDef",
    "ListSecurityConfigurationsRequestRequestTypeDef",
    "ListVirtualClustersRequestListVirtualClustersPaginateTypeDef",
    "ListVirtualClustersRequestRequestTypeDef",
    "MonitoringConfigurationTypeDef",
    "ParametricMonitoringConfigurationTypeDef",
    "SparkSubmitJobDriverUnionTypeDef",
    "ContainerProviderTypeDef",
    "EncryptionConfigurationTypeDef",
    "ConfigurationOverridesOutputTypeDef",
    "ConfigurationOverridesPaginatorTypeDef",
    "ConfigurationOverridesTypeDef",
    "ParametricConfigurationOverridesOutputTypeDef",
    "ParametricConfigurationOverridesPaginatorTypeDef",
    "ParametricConfigurationOverridesTypeDef",
    "JobDriverTypeDef",
    "CreateVirtualClusterRequestRequestTypeDef",
    "VirtualClusterTypeDef",
    "AuthorizationConfigurationTypeDef",
    "EndpointTypeDef",
    "JobRunTypeDef",
    "EndpointPaginatorTypeDef",
    "JobRunPaginatorTypeDef",
    "CreateManagedEndpointRequestRequestTypeDef",
    "JobTemplateDataOutputTypeDef",
    "JobTemplateDataPaginatorTypeDef",
    "ParametricConfigurationOverridesUnionTypeDef",
    "JobDriverUnionTypeDef",
    "StartJobRunRequestRequestTypeDef",
    "DescribeVirtualClusterResponseTypeDef",
    "ListVirtualClustersResponseTypeDef",
    "SecurityConfigurationDataTypeDef",
    "DescribeManagedEndpointResponseTypeDef",
    "ListManagedEndpointsResponseTypeDef",
    "DescribeJobRunResponseTypeDef",
    "ListJobRunsResponseTypeDef",
    "ListManagedEndpointsResponsePaginatorTypeDef",
    "ListJobRunsResponsePaginatorTypeDef",
    "JobTemplateTypeDef",
    "JobTemplatePaginatorTypeDef",
    "JobTemplateDataTypeDef",
    "CreateSecurityConfigurationRequestRequestTypeDef",
    "SecurityConfigurationTypeDef",
    "DescribeJobTemplateResponseTypeDef",
    "ListJobTemplatesResponseTypeDef",
    "ListJobTemplatesResponsePaginatorTypeDef",
    "CreateJobTemplateRequestRequestTypeDef",
    "DescribeSecurityConfigurationResponseTypeDef",
    "ListSecurityConfigurationsResponseTypeDef",
)

CancelJobRunRequestRequestTypeDef = TypedDict(
    "CancelJobRunRequestRequestTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
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
CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "certificateArn": NotRequired[str],
        "certificateData": NotRequired[str],
    },
)
CloudWatchMonitoringConfigurationTypeDef = TypedDict(
    "CloudWatchMonitoringConfigurationTypeDef",
    {
        "logGroupName": str,
        "logStreamNamePrefix": NotRequired[str],
    },
)
ConfigurationOutputTypeDef = TypedDict(
    "ConfigurationOutputTypeDef",
    {
        "classification": str,
        "properties": NotRequired[Dict[str, str]],
        "configurations": NotRequired[List[Dict[str, Any]]],
    },
)
ConfigurationPaginatorTypeDef = TypedDict(
    "ConfigurationPaginatorTypeDef",
    {
        "classification": str,
        "properties": NotRequired[Dict[str, str]],
        "configurations": NotRequired[List[Dict[str, Any]]],
    },
)
ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "classification": str,
        "properties": NotRequired[Mapping[str, str]],
        "configurations": NotRequired[Sequence[Mapping[str, Any]]],
    },
)
EksInfoTypeDef = TypedDict(
    "EksInfoTypeDef",
    {
        "namespace": NotRequired[str],
    },
)
ContainerLogRotationConfigurationTypeDef = TypedDict(
    "ContainerLogRotationConfigurationTypeDef",
    {
        "rotationSize": str,
        "maxFilesToKeep": int,
    },
)
CredentialsTypeDef = TypedDict(
    "CredentialsTypeDef",
    {
        "token": NotRequired[str],
    },
)
DeleteJobTemplateRequestRequestTypeDef = TypedDict(
    "DeleteJobTemplateRequestRequestTypeDef",
    {
        "id": str,
    },
)
DeleteManagedEndpointRequestRequestTypeDef = TypedDict(
    "DeleteManagedEndpointRequestRequestTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
    },
)
DeleteVirtualClusterRequestRequestTypeDef = TypedDict(
    "DeleteVirtualClusterRequestRequestTypeDef",
    {
        "id": str,
    },
)
DescribeJobRunRequestRequestTypeDef = TypedDict(
    "DescribeJobRunRequestRequestTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
    },
)
DescribeJobTemplateRequestRequestTypeDef = TypedDict(
    "DescribeJobTemplateRequestRequestTypeDef",
    {
        "id": str,
    },
)
DescribeManagedEndpointRequestRequestTypeDef = TypedDict(
    "DescribeManagedEndpointRequestRequestTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
    },
)
DescribeSecurityConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeSecurityConfigurationRequestRequestTypeDef",
    {
        "id": str,
    },
)
DescribeVirtualClusterRequestRequestTypeDef = TypedDict(
    "DescribeVirtualClusterRequestRequestTypeDef",
    {
        "id": str,
    },
)
GetManagedEndpointSessionCredentialsRequestRequestTypeDef = TypedDict(
    "GetManagedEndpointSessionCredentialsRequestRequestTypeDef",
    {
        "endpointIdentifier": str,
        "virtualClusterIdentifier": str,
        "executionRoleArn": str,
        "credentialType": str,
        "durationInSeconds": NotRequired[int],
        "logContext": NotRequired[str],
        "clientToken": NotRequired[str],
    },
)
TLSCertificateConfigurationTypeDef = TypedDict(
    "TLSCertificateConfigurationTypeDef",
    {
        "certificateProviderType": NotRequired[Literal["PEM"]],
        "publicCertificateSecretArn": NotRequired[str],
        "privateCertificateSecretArn": NotRequired[str],
    },
)
SparkSqlJobDriverTypeDef = TypedDict(
    "SparkSqlJobDriverTypeDef",
    {
        "entryPoint": NotRequired[str],
        "sparkSqlParameters": NotRequired[str],
    },
)
SparkSubmitJobDriverOutputTypeDef = TypedDict(
    "SparkSubmitJobDriverOutputTypeDef",
    {
        "entryPoint": str,
        "entryPointArguments": NotRequired[List[str]],
        "sparkSubmitParameters": NotRequired[str],
    },
)
RetryPolicyConfigurationTypeDef = TypedDict(
    "RetryPolicyConfigurationTypeDef",
    {
        "maxAttempts": int,
    },
)
RetryPolicyExecutionTypeDef = TypedDict(
    "RetryPolicyExecutionTypeDef",
    {
        "currentAttemptCount": int,
    },
)
TemplateParameterConfigurationTypeDef = TypedDict(
    "TemplateParameterConfigurationTypeDef",
    {
        "type": NotRequired[TemplateParameterDataTypeType],
        "defaultValue": NotRequired[str],
    },
)
SecureNamespaceInfoTypeDef = TypedDict(
    "SecureNamespaceInfoTypeDef",
    {
        "clusterId": NotRequired[str],
        "namespace": NotRequired[str],
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
TimestampTypeDef = Union[datetime, str]
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
S3MonitoringConfigurationTypeDef = TypedDict(
    "S3MonitoringConfigurationTypeDef",
    {
        "logUri": str,
    },
)
ParametricCloudWatchMonitoringConfigurationTypeDef = TypedDict(
    "ParametricCloudWatchMonitoringConfigurationTypeDef",
    {
        "logGroupName": NotRequired[str],
        "logStreamNamePrefix": NotRequired[str],
    },
)
ParametricS3MonitoringConfigurationTypeDef = TypedDict(
    "ParametricS3MonitoringConfigurationTypeDef",
    {
        "logUri": NotRequired[str],
    },
)
SparkSubmitJobDriverTypeDef = TypedDict(
    "SparkSubmitJobDriverTypeDef",
    {
        "entryPoint": str,
        "entryPointArguments": NotRequired[Sequence[str]],
        "sparkSubmitParameters": NotRequired[str],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
CancelJobRunResponseTypeDef = TypedDict(
    "CancelJobRunResponseTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateJobTemplateResponseTypeDef = TypedDict(
    "CreateJobTemplateResponseTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateManagedEndpointResponseTypeDef = TypedDict(
    "CreateManagedEndpointResponseTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "virtualClusterId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSecurityConfigurationResponseTypeDef = TypedDict(
    "CreateSecurityConfigurationResponseTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateVirtualClusterResponseTypeDef = TypedDict(
    "CreateVirtualClusterResponseTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteJobTemplateResponseTypeDef = TypedDict(
    "DeleteJobTemplateResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteManagedEndpointResponseTypeDef = TypedDict(
    "DeleteManagedEndpointResponseTypeDef",
    {
        "id": str,
        "virtualClusterId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteVirtualClusterResponseTypeDef = TypedDict(
    "DeleteVirtualClusterResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartJobRunResponseTypeDef = TypedDict(
    "StartJobRunResponseTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "virtualClusterId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConfigurationUnionTypeDef = Union[ConfigurationTypeDef, ConfigurationOutputTypeDef]
ContainerInfoTypeDef = TypedDict(
    "ContainerInfoTypeDef",
    {
        "eksInfo": NotRequired[EksInfoTypeDef],
    },
)
GetManagedEndpointSessionCredentialsResponseTypeDef = TypedDict(
    "GetManagedEndpointSessionCredentialsResponseTypeDef",
    {
        "id": str,
        "credentials": CredentialsTypeDef,
        "expiresAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InTransitEncryptionConfigurationTypeDef = TypedDict(
    "InTransitEncryptionConfigurationTypeDef",
    {
        "tlsCertificateConfiguration": NotRequired[TLSCertificateConfigurationTypeDef],
    },
)
JobDriverOutputTypeDef = TypedDict(
    "JobDriverOutputTypeDef",
    {
        "sparkSubmitJobDriver": NotRequired[SparkSubmitJobDriverOutputTypeDef],
        "sparkSqlJobDriver": NotRequired[SparkSqlJobDriverTypeDef],
    },
)
LakeFormationConfigurationTypeDef = TypedDict(
    "LakeFormationConfigurationTypeDef",
    {
        "authorizedSessionTagValue": NotRequired[str],
        "secureNamespaceInfo": NotRequired[SecureNamespaceInfoTypeDef],
        "queryEngineRoleArn": NotRequired[str],
    },
)
ListJobRunsRequestListJobRunsPaginateTypeDef = TypedDict(
    "ListJobRunsRequestListJobRunsPaginateTypeDef",
    {
        "virtualClusterId": str,
        "createdBefore": NotRequired[TimestampTypeDef],
        "createdAfter": NotRequired[TimestampTypeDef],
        "name": NotRequired[str],
        "states": NotRequired[Sequence[JobRunStateType]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListJobRunsRequestRequestTypeDef = TypedDict(
    "ListJobRunsRequestRequestTypeDef",
    {
        "virtualClusterId": str,
        "createdBefore": NotRequired[TimestampTypeDef],
        "createdAfter": NotRequired[TimestampTypeDef],
        "name": NotRequired[str],
        "states": NotRequired[Sequence[JobRunStateType]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListJobTemplatesRequestListJobTemplatesPaginateTypeDef = TypedDict(
    "ListJobTemplatesRequestListJobTemplatesPaginateTypeDef",
    {
        "createdAfter": NotRequired[TimestampTypeDef],
        "createdBefore": NotRequired[TimestampTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListJobTemplatesRequestRequestTypeDef = TypedDict(
    "ListJobTemplatesRequestRequestTypeDef",
    {
        "createdAfter": NotRequired[TimestampTypeDef],
        "createdBefore": NotRequired[TimestampTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListManagedEndpointsRequestListManagedEndpointsPaginateTypeDef = TypedDict(
    "ListManagedEndpointsRequestListManagedEndpointsPaginateTypeDef",
    {
        "virtualClusterId": str,
        "createdBefore": NotRequired[TimestampTypeDef],
        "createdAfter": NotRequired[TimestampTypeDef],
        "types": NotRequired[Sequence[str]],
        "states": NotRequired[Sequence[EndpointStateType]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListManagedEndpointsRequestRequestTypeDef = TypedDict(
    "ListManagedEndpointsRequestRequestTypeDef",
    {
        "virtualClusterId": str,
        "createdBefore": NotRequired[TimestampTypeDef],
        "createdAfter": NotRequired[TimestampTypeDef],
        "types": NotRequired[Sequence[str]],
        "states": NotRequired[Sequence[EndpointStateType]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListSecurityConfigurationsRequestListSecurityConfigurationsPaginateTypeDef = TypedDict(
    "ListSecurityConfigurationsRequestListSecurityConfigurationsPaginateTypeDef",
    {
        "createdAfter": NotRequired[TimestampTypeDef],
        "createdBefore": NotRequired[TimestampTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSecurityConfigurationsRequestRequestTypeDef = TypedDict(
    "ListSecurityConfigurationsRequestRequestTypeDef",
    {
        "createdAfter": NotRequired[TimestampTypeDef],
        "createdBefore": NotRequired[TimestampTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListVirtualClustersRequestListVirtualClustersPaginateTypeDef = TypedDict(
    "ListVirtualClustersRequestListVirtualClustersPaginateTypeDef",
    {
        "containerProviderId": NotRequired[str],
        "containerProviderType": NotRequired[Literal["EKS"]],
        "createdAfter": NotRequired[TimestampTypeDef],
        "createdBefore": NotRequired[TimestampTypeDef],
        "states": NotRequired[Sequence[VirtualClusterStateType]],
        "eksAccessEntryIntegrated": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListVirtualClustersRequestRequestTypeDef = TypedDict(
    "ListVirtualClustersRequestRequestTypeDef",
    {
        "containerProviderId": NotRequired[str],
        "containerProviderType": NotRequired[Literal["EKS"]],
        "createdAfter": NotRequired[TimestampTypeDef],
        "createdBefore": NotRequired[TimestampTypeDef],
        "states": NotRequired[Sequence[VirtualClusterStateType]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "eksAccessEntryIntegrated": NotRequired[bool],
    },
)
MonitoringConfigurationTypeDef = TypedDict(
    "MonitoringConfigurationTypeDef",
    {
        "persistentAppUI": NotRequired[PersistentAppUIType],
        "cloudWatchMonitoringConfiguration": NotRequired[CloudWatchMonitoringConfigurationTypeDef],
        "s3MonitoringConfiguration": NotRequired[S3MonitoringConfigurationTypeDef],
        "containerLogRotationConfiguration": NotRequired[ContainerLogRotationConfigurationTypeDef],
    },
)
ParametricMonitoringConfigurationTypeDef = TypedDict(
    "ParametricMonitoringConfigurationTypeDef",
    {
        "persistentAppUI": NotRequired[str],
        "cloudWatchMonitoringConfiguration": NotRequired[
            ParametricCloudWatchMonitoringConfigurationTypeDef
        ],
        "s3MonitoringConfiguration": NotRequired[ParametricS3MonitoringConfigurationTypeDef],
    },
)
SparkSubmitJobDriverUnionTypeDef = Union[
    SparkSubmitJobDriverTypeDef, SparkSubmitJobDriverOutputTypeDef
]
ContainerProviderTypeDef = TypedDict(
    "ContainerProviderTypeDef",
    {
        "type": Literal["EKS"],
        "id": str,
        "info": NotRequired[ContainerInfoTypeDef],
    },
)
EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "inTransitEncryptionConfiguration": NotRequired[InTransitEncryptionConfigurationTypeDef],
    },
)
ConfigurationOverridesOutputTypeDef = TypedDict(
    "ConfigurationOverridesOutputTypeDef",
    {
        "applicationConfiguration": NotRequired[List[ConfigurationOutputTypeDef]],
        "monitoringConfiguration": NotRequired[MonitoringConfigurationTypeDef],
    },
)
ConfigurationOverridesPaginatorTypeDef = TypedDict(
    "ConfigurationOverridesPaginatorTypeDef",
    {
        "applicationConfiguration": NotRequired[List[ConfigurationPaginatorTypeDef]],
        "monitoringConfiguration": NotRequired[MonitoringConfigurationTypeDef],
    },
)
ConfigurationOverridesTypeDef = TypedDict(
    "ConfigurationOverridesTypeDef",
    {
        "applicationConfiguration": NotRequired[Sequence[ConfigurationUnionTypeDef]],
        "monitoringConfiguration": NotRequired[MonitoringConfigurationTypeDef],
    },
)
ParametricConfigurationOverridesOutputTypeDef = TypedDict(
    "ParametricConfigurationOverridesOutputTypeDef",
    {
        "applicationConfiguration": NotRequired[List[ConfigurationOutputTypeDef]],
        "monitoringConfiguration": NotRequired[ParametricMonitoringConfigurationTypeDef],
    },
)
ParametricConfigurationOverridesPaginatorTypeDef = TypedDict(
    "ParametricConfigurationOverridesPaginatorTypeDef",
    {
        "applicationConfiguration": NotRequired[List[ConfigurationPaginatorTypeDef]],
        "monitoringConfiguration": NotRequired[ParametricMonitoringConfigurationTypeDef],
    },
)
ParametricConfigurationOverridesTypeDef = TypedDict(
    "ParametricConfigurationOverridesTypeDef",
    {
        "applicationConfiguration": NotRequired[Sequence[ConfigurationUnionTypeDef]],
        "monitoringConfiguration": NotRequired[ParametricMonitoringConfigurationTypeDef],
    },
)
JobDriverTypeDef = TypedDict(
    "JobDriverTypeDef",
    {
        "sparkSubmitJobDriver": NotRequired[SparkSubmitJobDriverUnionTypeDef],
        "sparkSqlJobDriver": NotRequired[SparkSqlJobDriverTypeDef],
    },
)
CreateVirtualClusterRequestRequestTypeDef = TypedDict(
    "CreateVirtualClusterRequestRequestTypeDef",
    {
        "name": str,
        "containerProvider": ContainerProviderTypeDef,
        "clientToken": str,
        "tags": NotRequired[Mapping[str, str]],
        "securityConfigurationId": NotRequired[str],
    },
)
VirtualClusterTypeDef = TypedDict(
    "VirtualClusterTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "state": NotRequired[VirtualClusterStateType],
        "containerProvider": NotRequired[ContainerProviderTypeDef],
        "createdAt": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
        "securityConfigurationId": NotRequired[str],
    },
)
AuthorizationConfigurationTypeDef = TypedDict(
    "AuthorizationConfigurationTypeDef",
    {
        "lakeFormationConfiguration": NotRequired[LakeFormationConfigurationTypeDef],
        "encryptionConfiguration": NotRequired[EncryptionConfigurationTypeDef],
    },
)
EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "virtualClusterId": NotRequired[str],
        "type": NotRequired[str],
        "state": NotRequired[EndpointStateType],
        "releaseLabel": NotRequired[str],
        "executionRoleArn": NotRequired[str],
        "certificateArn": NotRequired[str],
        "certificateAuthority": NotRequired[CertificateTypeDef],
        "configurationOverrides": NotRequired[ConfigurationOverridesOutputTypeDef],
        "serverUrl": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "securityGroup": NotRequired[str],
        "subnetIds": NotRequired[List[str]],
        "stateDetails": NotRequired[str],
        "failureReason": NotRequired[FailureReasonType],
        "tags": NotRequired[Dict[str, str]],
    },
)
JobRunTypeDef = TypedDict(
    "JobRunTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "virtualClusterId": NotRequired[str],
        "arn": NotRequired[str],
        "state": NotRequired[JobRunStateType],
        "clientToken": NotRequired[str],
        "executionRoleArn": NotRequired[str],
        "releaseLabel": NotRequired[str],
        "configurationOverrides": NotRequired[ConfigurationOverridesOutputTypeDef],
        "jobDriver": NotRequired[JobDriverOutputTypeDef],
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "finishedAt": NotRequired[datetime],
        "stateDetails": NotRequired[str],
        "failureReason": NotRequired[FailureReasonType],
        "tags": NotRequired[Dict[str, str]],
        "retryPolicyConfiguration": NotRequired[RetryPolicyConfigurationTypeDef],
        "retryPolicyExecution": NotRequired[RetryPolicyExecutionTypeDef],
    },
)
EndpointPaginatorTypeDef = TypedDict(
    "EndpointPaginatorTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "virtualClusterId": NotRequired[str],
        "type": NotRequired[str],
        "state": NotRequired[EndpointStateType],
        "releaseLabel": NotRequired[str],
        "executionRoleArn": NotRequired[str],
        "certificateArn": NotRequired[str],
        "certificateAuthority": NotRequired[CertificateTypeDef],
        "configurationOverrides": NotRequired[ConfigurationOverridesPaginatorTypeDef],
        "serverUrl": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "securityGroup": NotRequired[str],
        "subnetIds": NotRequired[List[str]],
        "stateDetails": NotRequired[str],
        "failureReason": NotRequired[FailureReasonType],
        "tags": NotRequired[Dict[str, str]],
    },
)
JobRunPaginatorTypeDef = TypedDict(
    "JobRunPaginatorTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "virtualClusterId": NotRequired[str],
        "arn": NotRequired[str],
        "state": NotRequired[JobRunStateType],
        "clientToken": NotRequired[str],
        "executionRoleArn": NotRequired[str],
        "releaseLabel": NotRequired[str],
        "configurationOverrides": NotRequired[ConfigurationOverridesPaginatorTypeDef],
        "jobDriver": NotRequired[JobDriverOutputTypeDef],
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "finishedAt": NotRequired[datetime],
        "stateDetails": NotRequired[str],
        "failureReason": NotRequired[FailureReasonType],
        "tags": NotRequired[Dict[str, str]],
        "retryPolicyConfiguration": NotRequired[RetryPolicyConfigurationTypeDef],
        "retryPolicyExecution": NotRequired[RetryPolicyExecutionTypeDef],
    },
)
CreateManagedEndpointRequestRequestTypeDef = TypedDict(
    "CreateManagedEndpointRequestRequestTypeDef",
    {
        "name": str,
        "virtualClusterId": str,
        "type": str,
        "releaseLabel": str,
        "executionRoleArn": str,
        "clientToken": str,
        "certificateArn": NotRequired[str],
        "configurationOverrides": NotRequired[ConfigurationOverridesTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
JobTemplateDataOutputTypeDef = TypedDict(
    "JobTemplateDataOutputTypeDef",
    {
        "executionRoleArn": str,
        "releaseLabel": str,
        "jobDriver": JobDriverOutputTypeDef,
        "configurationOverrides": NotRequired[ParametricConfigurationOverridesOutputTypeDef],
        "parameterConfiguration": NotRequired[Dict[str, TemplateParameterConfigurationTypeDef]],
        "jobTags": NotRequired[Dict[str, str]],
    },
)
JobTemplateDataPaginatorTypeDef = TypedDict(
    "JobTemplateDataPaginatorTypeDef",
    {
        "executionRoleArn": str,
        "releaseLabel": str,
        "jobDriver": JobDriverOutputTypeDef,
        "configurationOverrides": NotRequired[ParametricConfigurationOverridesPaginatorTypeDef],
        "parameterConfiguration": NotRequired[Dict[str, TemplateParameterConfigurationTypeDef]],
        "jobTags": NotRequired[Dict[str, str]],
    },
)
ParametricConfigurationOverridesUnionTypeDef = Union[
    ParametricConfigurationOverridesTypeDef, ParametricConfigurationOverridesOutputTypeDef
]
JobDriverUnionTypeDef = Union[JobDriverTypeDef, JobDriverOutputTypeDef]
StartJobRunRequestRequestTypeDef = TypedDict(
    "StartJobRunRequestRequestTypeDef",
    {
        "virtualClusterId": str,
        "clientToken": str,
        "name": NotRequired[str],
        "executionRoleArn": NotRequired[str],
        "releaseLabel": NotRequired[str],
        "jobDriver": NotRequired[JobDriverTypeDef],
        "configurationOverrides": NotRequired[ConfigurationOverridesTypeDef],
        "tags": NotRequired[Mapping[str, str]],
        "jobTemplateId": NotRequired[str],
        "jobTemplateParameters": NotRequired[Mapping[str, str]],
        "retryPolicyConfiguration": NotRequired[RetryPolicyConfigurationTypeDef],
    },
)
DescribeVirtualClusterResponseTypeDef = TypedDict(
    "DescribeVirtualClusterResponseTypeDef",
    {
        "virtualCluster": VirtualClusterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListVirtualClustersResponseTypeDef = TypedDict(
    "ListVirtualClustersResponseTypeDef",
    {
        "virtualClusters": List[VirtualClusterTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SecurityConfigurationDataTypeDef = TypedDict(
    "SecurityConfigurationDataTypeDef",
    {
        "authorizationConfiguration": NotRequired[AuthorizationConfigurationTypeDef],
    },
)
DescribeManagedEndpointResponseTypeDef = TypedDict(
    "DescribeManagedEndpointResponseTypeDef",
    {
        "endpoint": EndpointTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListManagedEndpointsResponseTypeDef = TypedDict(
    "ListManagedEndpointsResponseTypeDef",
    {
        "endpoints": List[EndpointTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeJobRunResponseTypeDef = TypedDict(
    "DescribeJobRunResponseTypeDef",
    {
        "jobRun": JobRunTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListJobRunsResponseTypeDef = TypedDict(
    "ListJobRunsResponseTypeDef",
    {
        "jobRuns": List[JobRunTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListManagedEndpointsResponsePaginatorTypeDef = TypedDict(
    "ListManagedEndpointsResponsePaginatorTypeDef",
    {
        "endpoints": List[EndpointPaginatorTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListJobRunsResponsePaginatorTypeDef = TypedDict(
    "ListJobRunsResponsePaginatorTypeDef",
    {
        "jobRuns": List[JobRunPaginatorTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
JobTemplateTypeDef = TypedDict(
    "JobTemplateTypeDef",
    {
        "jobTemplateData": JobTemplateDataOutputTypeDef,
        "name": NotRequired[str],
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "kmsKeyArn": NotRequired[str],
        "decryptionError": NotRequired[str],
    },
)
JobTemplatePaginatorTypeDef = TypedDict(
    "JobTemplatePaginatorTypeDef",
    {
        "jobTemplateData": JobTemplateDataPaginatorTypeDef,
        "name": NotRequired[str],
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "kmsKeyArn": NotRequired[str],
        "decryptionError": NotRequired[str],
    },
)
JobTemplateDataTypeDef = TypedDict(
    "JobTemplateDataTypeDef",
    {
        "executionRoleArn": str,
        "releaseLabel": str,
        "jobDriver": JobDriverUnionTypeDef,
        "configurationOverrides": NotRequired[ParametricConfigurationOverridesUnionTypeDef],
        "parameterConfiguration": NotRequired[Mapping[str, TemplateParameterConfigurationTypeDef]],
        "jobTags": NotRequired[Mapping[str, str]],
    },
)
CreateSecurityConfigurationRequestRequestTypeDef = TypedDict(
    "CreateSecurityConfigurationRequestRequestTypeDef",
    {
        "clientToken": str,
        "name": str,
        "securityConfigurationData": SecurityConfigurationDataTypeDef,
        "tags": NotRequired[Mapping[str, str]],
    },
)
SecurityConfigurationTypeDef = TypedDict(
    "SecurityConfigurationTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "securityConfigurationData": NotRequired[SecurityConfigurationDataTypeDef],
        "tags": NotRequired[Dict[str, str]],
    },
)
DescribeJobTemplateResponseTypeDef = TypedDict(
    "DescribeJobTemplateResponseTypeDef",
    {
        "jobTemplate": JobTemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListJobTemplatesResponseTypeDef = TypedDict(
    "ListJobTemplatesResponseTypeDef",
    {
        "templates": List[JobTemplateTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListJobTemplatesResponsePaginatorTypeDef = TypedDict(
    "ListJobTemplatesResponsePaginatorTypeDef",
    {
        "templates": List[JobTemplatePaginatorTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateJobTemplateRequestRequestTypeDef = TypedDict(
    "CreateJobTemplateRequestRequestTypeDef",
    {
        "name": str,
        "clientToken": str,
        "jobTemplateData": JobTemplateDataTypeDef,
        "tags": NotRequired[Mapping[str, str]],
        "kmsKeyArn": NotRequired[str],
    },
)
DescribeSecurityConfigurationResponseTypeDef = TypedDict(
    "DescribeSecurityConfigurationResponseTypeDef",
    {
        "securityConfiguration": SecurityConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSecurityConfigurationsResponseTypeDef = TypedDict(
    "ListSecurityConfigurationsResponseTypeDef",
    {
        "securityConfigurations": List[SecurityConfigurationTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
