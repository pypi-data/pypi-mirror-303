"""
Type annotations for transfer service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transfer/type_defs/)

Usage::

    ```python
    from mypy_boto3_transfer.type_defs import As2ConnectorConfigTypeDef

    data: As2ConnectorConfigTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    AgreementStatusTypeType,
    CertificateStatusTypeType,
    CertificateTypeType,
    CertificateUsageTypeType,
    CompressionEnumType,
    CustomStepStatusType,
    DirectoryListingOptimizationType,
    DomainType,
    EncryptionAlgType,
    EndpointTypeType,
    ExecutionErrorTypeType,
    ExecutionStatusType,
    HomeDirectoryTypeType,
    IdentityProviderTypeType,
    MapTypeType,
    MdnResponseType,
    MdnSigningAlgType,
    OverwriteExistingType,
    ProfileTypeType,
    ProtocolType,
    SecurityPolicyProtocolType,
    SecurityPolicyResourceTypeType,
    SetStatOptionType,
    SftpAuthenticationMethodsType,
    SigningAlgType,
    StateType,
    TlsSessionResumptionModeType,
    TransferTableStatusType,
    WorkflowStepTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "As2ConnectorConfigTypeDef",
    "ConnectorFileTransferResultTypeDef",
    "HomeDirectoryMapEntryTypeDef",
    "PosixProfileTypeDef",
    "ResponseMetadataTypeDef",
    "TagTypeDef",
    "SftpConnectorConfigTypeDef",
    "EndpointDetailsTypeDef",
    "IdentityProviderDetailsTypeDef",
    "ProtocolDetailsTypeDef",
    "S3StorageOptionsTypeDef",
    "CustomStepDetailsTypeDef",
    "DeleteAccessRequestRequestTypeDef",
    "DeleteAgreementRequestRequestTypeDef",
    "DeleteCertificateRequestRequestTypeDef",
    "DeleteConnectorRequestRequestTypeDef",
    "DeleteHostKeyRequestRequestTypeDef",
    "DeleteProfileRequestRequestTypeDef",
    "DeleteServerRequestRequestTypeDef",
    "DeleteSshPublicKeyRequestRequestTypeDef",
    "DeleteStepDetailsTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DeleteWorkflowRequestRequestTypeDef",
    "DescribeAccessRequestRequestTypeDef",
    "DescribeAgreementRequestRequestTypeDef",
    "DescribeCertificateRequestRequestTypeDef",
    "DescribeConnectorRequestRequestTypeDef",
    "DescribeExecutionRequestRequestTypeDef",
    "DescribeHostKeyRequestRequestTypeDef",
    "DescribeProfileRequestRequestTypeDef",
    "DescribeSecurityPolicyRequestRequestTypeDef",
    "DescribedSecurityPolicyTypeDef",
    "DescribeServerRequestRequestTypeDef",
    "WaiterConfigTypeDef",
    "DescribeUserRequestRequestTypeDef",
    "DescribeWorkflowRequestRequestTypeDef",
    "PosixProfileOutputTypeDef",
    "SftpConnectorConfigOutputTypeDef",
    "LoggingConfigurationTypeDef",
    "EndpointDetailsOutputTypeDef",
    "ProtocolDetailsOutputTypeDef",
    "SshPublicKeyTypeDef",
    "EfsFileLocationTypeDef",
    "ExecutionErrorTypeDef",
    "S3FileLocationTypeDef",
    "TimestampTypeDef",
    "ImportSshPublicKeyRequestRequestTypeDef",
    "S3InputFileLocationTypeDef",
    "PaginatorConfigTypeDef",
    "ListAccessesRequestRequestTypeDef",
    "ListedAccessTypeDef",
    "ListAgreementsRequestRequestTypeDef",
    "ListedAgreementTypeDef",
    "ListCertificatesRequestRequestTypeDef",
    "ListedCertificateTypeDef",
    "ListConnectorsRequestRequestTypeDef",
    "ListedConnectorTypeDef",
    "ListExecutionsRequestRequestTypeDef",
    "ListFileTransferResultsRequestRequestTypeDef",
    "ListHostKeysRequestRequestTypeDef",
    "ListedHostKeyTypeDef",
    "ListProfilesRequestRequestTypeDef",
    "ListedProfileTypeDef",
    "ListSecurityPoliciesRequestRequestTypeDef",
    "ListServersRequestRequestTypeDef",
    "ListedServerTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListUsersRequestRequestTypeDef",
    "ListedUserTypeDef",
    "ListWorkflowsRequestRequestTypeDef",
    "ListedWorkflowTypeDef",
    "S3TagTypeDef",
    "SendWorkflowStepStateRequestRequestTypeDef",
    "UserDetailsTypeDef",
    "StartDirectoryListingRequestRequestTypeDef",
    "StartFileTransferRequestRequestTypeDef",
    "StartServerRequestRequestTypeDef",
    "StopServerRequestRequestTypeDef",
    "TestConnectionRequestRequestTypeDef",
    "TestIdentityProviderRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAgreementRequestRequestTypeDef",
    "UpdateHostKeyRequestRequestTypeDef",
    "UpdateProfileRequestRequestTypeDef",
    "WorkflowDetailTypeDef",
    "CreateAccessRequestRequestTypeDef",
    "UpdateAccessRequestRequestTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "CreateAccessResponseTypeDef",
    "CreateAgreementResponseTypeDef",
    "CreateConnectorResponseTypeDef",
    "CreateProfileResponseTypeDef",
    "CreateServerResponseTypeDef",
    "CreateUserResponseTypeDef",
    "CreateWorkflowResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ImportCertificateResponseTypeDef",
    "ImportHostKeyResponseTypeDef",
    "ImportSshPublicKeyResponseTypeDef",
    "ListFileTransferResultsResponseTypeDef",
    "ListSecurityPoliciesResponseTypeDef",
    "StartDirectoryListingResponseTypeDef",
    "StartFileTransferResponseTypeDef",
    "TestConnectionResponseTypeDef",
    "TestIdentityProviderResponseTypeDef",
    "UpdateAccessResponseTypeDef",
    "UpdateAgreementResponseTypeDef",
    "UpdateCertificateResponseTypeDef",
    "UpdateConnectorResponseTypeDef",
    "UpdateHostKeyResponseTypeDef",
    "UpdateProfileResponseTypeDef",
    "UpdateServerResponseTypeDef",
    "UpdateUserResponseTypeDef",
    "CreateAgreementRequestRequestTypeDef",
    "CreateProfileRequestRequestTypeDef",
    "CreateUserRequestRequestTypeDef",
    "DescribedAgreementTypeDef",
    "DescribedCertificateTypeDef",
    "DescribedHostKeyTypeDef",
    "DescribedProfileTypeDef",
    "ImportHostKeyRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateConnectorRequestRequestTypeDef",
    "UpdateConnectorRequestRequestTypeDef",
    "DescribeSecurityPolicyResponseTypeDef",
    "DescribeServerRequestServerOfflineWaitTypeDef",
    "DescribeServerRequestServerOnlineWaitTypeDef",
    "DescribedAccessTypeDef",
    "DescribedConnectorTypeDef",
    "DescribedUserTypeDef",
    "ExecutionStepResultTypeDef",
    "FileLocationTypeDef",
    "ImportCertificateRequestRequestTypeDef",
    "UpdateCertificateRequestRequestTypeDef",
    "InputFileLocationTypeDef",
    "ListAccessesRequestListAccessesPaginateTypeDef",
    "ListAgreementsRequestListAgreementsPaginateTypeDef",
    "ListCertificatesRequestListCertificatesPaginateTypeDef",
    "ListConnectorsRequestListConnectorsPaginateTypeDef",
    "ListExecutionsRequestListExecutionsPaginateTypeDef",
    "ListFileTransferResultsRequestListFileTransferResultsPaginateTypeDef",
    "ListProfilesRequestListProfilesPaginateTypeDef",
    "ListSecurityPoliciesRequestListSecurityPoliciesPaginateTypeDef",
    "ListServersRequestListServersPaginateTypeDef",
    "ListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    "ListUsersRequestListUsersPaginateTypeDef",
    "ListWorkflowsRequestListWorkflowsPaginateTypeDef",
    "ListAccessesResponseTypeDef",
    "ListAgreementsResponseTypeDef",
    "ListCertificatesResponseTypeDef",
    "ListConnectorsResponseTypeDef",
    "ListHostKeysResponseTypeDef",
    "ListProfilesResponseTypeDef",
    "ListServersResponseTypeDef",
    "ListUsersResponseTypeDef",
    "ListWorkflowsResponseTypeDef",
    "TagStepDetailsOutputTypeDef",
    "TagStepDetailsTypeDef",
    "ServiceMetadataTypeDef",
    "WorkflowDetailsOutputTypeDef",
    "WorkflowDetailsTypeDef",
    "DescribeAgreementResponseTypeDef",
    "DescribeCertificateResponseTypeDef",
    "DescribeHostKeyResponseTypeDef",
    "DescribeProfileResponseTypeDef",
    "DescribeAccessResponseTypeDef",
    "DescribeConnectorResponseTypeDef",
    "DescribeUserResponseTypeDef",
    "ExecutionResultsTypeDef",
    "CopyStepDetailsTypeDef",
    "DecryptStepDetailsTypeDef",
    "TagStepDetailsUnionTypeDef",
    "ListedExecutionTypeDef",
    "DescribedServerTypeDef",
    "CreateServerRequestRequestTypeDef",
    "UpdateServerRequestRequestTypeDef",
    "DescribedExecutionTypeDef",
    "WorkflowStepOutputTypeDef",
    "WorkflowStepTypeDef",
    "ListExecutionsResponseTypeDef",
    "DescribeServerResponseTypeDef",
    "DescribeExecutionResponseTypeDef",
    "DescribedWorkflowTypeDef",
    "WorkflowStepUnionTypeDef",
    "DescribeWorkflowResponseTypeDef",
    "CreateWorkflowRequestRequestTypeDef",
)

As2ConnectorConfigTypeDef = TypedDict(
    "As2ConnectorConfigTypeDef",
    {
        "LocalProfileId": NotRequired[str],
        "PartnerProfileId": NotRequired[str],
        "MessageSubject": NotRequired[str],
        "Compression": NotRequired[CompressionEnumType],
        "EncryptionAlgorithm": NotRequired[EncryptionAlgType],
        "SigningAlgorithm": NotRequired[SigningAlgType],
        "MdnSigningAlgorithm": NotRequired[MdnSigningAlgType],
        "MdnResponse": NotRequired[MdnResponseType],
        "BasicAuthSecretId": NotRequired[str],
    },
)
ConnectorFileTransferResultTypeDef = TypedDict(
    "ConnectorFileTransferResultTypeDef",
    {
        "FilePath": str,
        "StatusCode": TransferTableStatusType,
        "FailureCode": NotRequired[str],
        "FailureMessage": NotRequired[str],
    },
)
HomeDirectoryMapEntryTypeDef = TypedDict(
    "HomeDirectoryMapEntryTypeDef",
    {
        "Entry": str,
        "Target": str,
        "Type": NotRequired[MapTypeType],
    },
)
PosixProfileTypeDef = TypedDict(
    "PosixProfileTypeDef",
    {
        "Uid": int,
        "Gid": int,
        "SecondaryGids": NotRequired[Sequence[int]],
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
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
SftpConnectorConfigTypeDef = TypedDict(
    "SftpConnectorConfigTypeDef",
    {
        "UserSecretId": NotRequired[str],
        "TrustedHostKeys": NotRequired[Sequence[str]],
    },
)
EndpointDetailsTypeDef = TypedDict(
    "EndpointDetailsTypeDef",
    {
        "AddressAllocationIds": NotRequired[Sequence[str]],
        "SubnetIds": NotRequired[Sequence[str]],
        "VpcEndpointId": NotRequired[str],
        "VpcId": NotRequired[str],
        "SecurityGroupIds": NotRequired[Sequence[str]],
    },
)
IdentityProviderDetailsTypeDef = TypedDict(
    "IdentityProviderDetailsTypeDef",
    {
        "Url": NotRequired[str],
        "InvocationRole": NotRequired[str],
        "DirectoryId": NotRequired[str],
        "Function": NotRequired[str],
        "SftpAuthenticationMethods": NotRequired[SftpAuthenticationMethodsType],
    },
)
ProtocolDetailsTypeDef = TypedDict(
    "ProtocolDetailsTypeDef",
    {
        "PassiveIp": NotRequired[str],
        "TlsSessionResumptionMode": NotRequired[TlsSessionResumptionModeType],
        "SetStatOption": NotRequired[SetStatOptionType],
        "As2Transports": NotRequired[Sequence[Literal["HTTP"]]],
    },
)
S3StorageOptionsTypeDef = TypedDict(
    "S3StorageOptionsTypeDef",
    {
        "DirectoryListingOptimization": NotRequired[DirectoryListingOptimizationType],
    },
)
CustomStepDetailsTypeDef = TypedDict(
    "CustomStepDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Target": NotRequired[str],
        "TimeoutSeconds": NotRequired[int],
        "SourceFileLocation": NotRequired[str],
    },
)
DeleteAccessRequestRequestTypeDef = TypedDict(
    "DeleteAccessRequestRequestTypeDef",
    {
        "ServerId": str,
        "ExternalId": str,
    },
)
DeleteAgreementRequestRequestTypeDef = TypedDict(
    "DeleteAgreementRequestRequestTypeDef",
    {
        "AgreementId": str,
        "ServerId": str,
    },
)
DeleteCertificateRequestRequestTypeDef = TypedDict(
    "DeleteCertificateRequestRequestTypeDef",
    {
        "CertificateId": str,
    },
)
DeleteConnectorRequestRequestTypeDef = TypedDict(
    "DeleteConnectorRequestRequestTypeDef",
    {
        "ConnectorId": str,
    },
)
DeleteHostKeyRequestRequestTypeDef = TypedDict(
    "DeleteHostKeyRequestRequestTypeDef",
    {
        "ServerId": str,
        "HostKeyId": str,
    },
)
DeleteProfileRequestRequestTypeDef = TypedDict(
    "DeleteProfileRequestRequestTypeDef",
    {
        "ProfileId": str,
    },
)
DeleteServerRequestRequestTypeDef = TypedDict(
    "DeleteServerRequestRequestTypeDef",
    {
        "ServerId": str,
    },
)
DeleteSshPublicKeyRequestRequestTypeDef = TypedDict(
    "DeleteSshPublicKeyRequestRequestTypeDef",
    {
        "ServerId": str,
        "SshPublicKeyId": str,
        "UserName": str,
    },
)
DeleteStepDetailsTypeDef = TypedDict(
    "DeleteStepDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "SourceFileLocation": NotRequired[str],
    },
)
DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "ServerId": str,
        "UserName": str,
    },
)
DeleteWorkflowRequestRequestTypeDef = TypedDict(
    "DeleteWorkflowRequestRequestTypeDef",
    {
        "WorkflowId": str,
    },
)
DescribeAccessRequestRequestTypeDef = TypedDict(
    "DescribeAccessRequestRequestTypeDef",
    {
        "ServerId": str,
        "ExternalId": str,
    },
)
DescribeAgreementRequestRequestTypeDef = TypedDict(
    "DescribeAgreementRequestRequestTypeDef",
    {
        "AgreementId": str,
        "ServerId": str,
    },
)
DescribeCertificateRequestRequestTypeDef = TypedDict(
    "DescribeCertificateRequestRequestTypeDef",
    {
        "CertificateId": str,
    },
)
DescribeConnectorRequestRequestTypeDef = TypedDict(
    "DescribeConnectorRequestRequestTypeDef",
    {
        "ConnectorId": str,
    },
)
DescribeExecutionRequestRequestTypeDef = TypedDict(
    "DescribeExecutionRequestRequestTypeDef",
    {
        "ExecutionId": str,
        "WorkflowId": str,
    },
)
DescribeHostKeyRequestRequestTypeDef = TypedDict(
    "DescribeHostKeyRequestRequestTypeDef",
    {
        "ServerId": str,
        "HostKeyId": str,
    },
)
DescribeProfileRequestRequestTypeDef = TypedDict(
    "DescribeProfileRequestRequestTypeDef",
    {
        "ProfileId": str,
    },
)
DescribeSecurityPolicyRequestRequestTypeDef = TypedDict(
    "DescribeSecurityPolicyRequestRequestTypeDef",
    {
        "SecurityPolicyName": str,
    },
)
DescribedSecurityPolicyTypeDef = TypedDict(
    "DescribedSecurityPolicyTypeDef",
    {
        "SecurityPolicyName": str,
        "Fips": NotRequired[bool],
        "SshCiphers": NotRequired[List[str]],
        "SshKexs": NotRequired[List[str]],
        "SshMacs": NotRequired[List[str]],
        "TlsCiphers": NotRequired[List[str]],
        "SshHostKeyAlgorithms": NotRequired[List[str]],
        "Type": NotRequired[SecurityPolicyResourceTypeType],
        "Protocols": NotRequired[List[SecurityPolicyProtocolType]],
    },
)
DescribeServerRequestRequestTypeDef = TypedDict(
    "DescribeServerRequestRequestTypeDef",
    {
        "ServerId": str,
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
DescribeUserRequestRequestTypeDef = TypedDict(
    "DescribeUserRequestRequestTypeDef",
    {
        "ServerId": str,
        "UserName": str,
    },
)
DescribeWorkflowRequestRequestTypeDef = TypedDict(
    "DescribeWorkflowRequestRequestTypeDef",
    {
        "WorkflowId": str,
    },
)
PosixProfileOutputTypeDef = TypedDict(
    "PosixProfileOutputTypeDef",
    {
        "Uid": int,
        "Gid": int,
        "SecondaryGids": NotRequired[List[int]],
    },
)
SftpConnectorConfigOutputTypeDef = TypedDict(
    "SftpConnectorConfigOutputTypeDef",
    {
        "UserSecretId": NotRequired[str],
        "TrustedHostKeys": NotRequired[List[str]],
    },
)
LoggingConfigurationTypeDef = TypedDict(
    "LoggingConfigurationTypeDef",
    {
        "LoggingRole": NotRequired[str],
        "LogGroupName": NotRequired[str],
    },
)
EndpointDetailsOutputTypeDef = TypedDict(
    "EndpointDetailsOutputTypeDef",
    {
        "AddressAllocationIds": NotRequired[List[str]],
        "SubnetIds": NotRequired[List[str]],
        "VpcEndpointId": NotRequired[str],
        "VpcId": NotRequired[str],
        "SecurityGroupIds": NotRequired[List[str]],
    },
)
ProtocolDetailsOutputTypeDef = TypedDict(
    "ProtocolDetailsOutputTypeDef",
    {
        "PassiveIp": NotRequired[str],
        "TlsSessionResumptionMode": NotRequired[TlsSessionResumptionModeType],
        "SetStatOption": NotRequired[SetStatOptionType],
        "As2Transports": NotRequired[List[Literal["HTTP"]]],
    },
)
SshPublicKeyTypeDef = TypedDict(
    "SshPublicKeyTypeDef",
    {
        "DateImported": datetime,
        "SshPublicKeyBody": str,
        "SshPublicKeyId": str,
    },
)
EfsFileLocationTypeDef = TypedDict(
    "EfsFileLocationTypeDef",
    {
        "FileSystemId": NotRequired[str],
        "Path": NotRequired[str],
    },
)
ExecutionErrorTypeDef = TypedDict(
    "ExecutionErrorTypeDef",
    {
        "Type": ExecutionErrorTypeType,
        "Message": str,
    },
)
S3FileLocationTypeDef = TypedDict(
    "S3FileLocationTypeDef",
    {
        "Bucket": NotRequired[str],
        "Key": NotRequired[str],
        "VersionId": NotRequired[str],
        "Etag": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
ImportSshPublicKeyRequestRequestTypeDef = TypedDict(
    "ImportSshPublicKeyRequestRequestTypeDef",
    {
        "ServerId": str,
        "SshPublicKeyBody": str,
        "UserName": str,
    },
)
S3InputFileLocationTypeDef = TypedDict(
    "S3InputFileLocationTypeDef",
    {
        "Bucket": NotRequired[str],
        "Key": NotRequired[str],
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
ListAccessesRequestRequestTypeDef = TypedDict(
    "ListAccessesRequestRequestTypeDef",
    {
        "ServerId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListedAccessTypeDef = TypedDict(
    "ListedAccessTypeDef",
    {
        "HomeDirectory": NotRequired[str],
        "HomeDirectoryType": NotRequired[HomeDirectoryTypeType],
        "Role": NotRequired[str],
        "ExternalId": NotRequired[str],
    },
)
ListAgreementsRequestRequestTypeDef = TypedDict(
    "ListAgreementsRequestRequestTypeDef",
    {
        "ServerId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListedAgreementTypeDef = TypedDict(
    "ListedAgreementTypeDef",
    {
        "Arn": NotRequired[str],
        "AgreementId": NotRequired[str],
        "Description": NotRequired[str],
        "Status": NotRequired[AgreementStatusTypeType],
        "ServerId": NotRequired[str],
        "LocalProfileId": NotRequired[str],
        "PartnerProfileId": NotRequired[str],
    },
)
ListCertificatesRequestRequestTypeDef = TypedDict(
    "ListCertificatesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListedCertificateTypeDef = TypedDict(
    "ListedCertificateTypeDef",
    {
        "Arn": NotRequired[str],
        "CertificateId": NotRequired[str],
        "Usage": NotRequired[CertificateUsageTypeType],
        "Status": NotRequired[CertificateStatusTypeType],
        "ActiveDate": NotRequired[datetime],
        "InactiveDate": NotRequired[datetime],
        "Type": NotRequired[CertificateTypeType],
        "Description": NotRequired[str],
    },
)
ListConnectorsRequestRequestTypeDef = TypedDict(
    "ListConnectorsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListedConnectorTypeDef = TypedDict(
    "ListedConnectorTypeDef",
    {
        "Arn": NotRequired[str],
        "ConnectorId": NotRequired[str],
        "Url": NotRequired[str],
    },
)
ListExecutionsRequestRequestTypeDef = TypedDict(
    "ListExecutionsRequestRequestTypeDef",
    {
        "WorkflowId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListFileTransferResultsRequestRequestTypeDef = TypedDict(
    "ListFileTransferResultsRequestRequestTypeDef",
    {
        "ConnectorId": str,
        "TransferId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListHostKeysRequestRequestTypeDef = TypedDict(
    "ListHostKeysRequestRequestTypeDef",
    {
        "ServerId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListedHostKeyTypeDef = TypedDict(
    "ListedHostKeyTypeDef",
    {
        "Arn": str,
        "HostKeyId": NotRequired[str],
        "Fingerprint": NotRequired[str],
        "Description": NotRequired[str],
        "Type": NotRequired[str],
        "DateImported": NotRequired[datetime],
    },
)
ListProfilesRequestRequestTypeDef = TypedDict(
    "ListProfilesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ProfileType": NotRequired[ProfileTypeType],
    },
)
ListedProfileTypeDef = TypedDict(
    "ListedProfileTypeDef",
    {
        "Arn": NotRequired[str],
        "ProfileId": NotRequired[str],
        "As2Id": NotRequired[str],
        "ProfileType": NotRequired[ProfileTypeType],
    },
)
ListSecurityPoliciesRequestRequestTypeDef = TypedDict(
    "ListSecurityPoliciesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListServersRequestRequestTypeDef = TypedDict(
    "ListServersRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListedServerTypeDef = TypedDict(
    "ListedServerTypeDef",
    {
        "Arn": str,
        "Domain": NotRequired[DomainType],
        "IdentityProviderType": NotRequired[IdentityProviderTypeType],
        "EndpointType": NotRequired[EndpointTypeType],
        "LoggingRole": NotRequired[str],
        "ServerId": NotRequired[str],
        "State": NotRequired[StateType],
        "UserCount": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "Arn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListUsersRequestRequestTypeDef = TypedDict(
    "ListUsersRequestRequestTypeDef",
    {
        "ServerId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListedUserTypeDef = TypedDict(
    "ListedUserTypeDef",
    {
        "Arn": str,
        "HomeDirectory": NotRequired[str],
        "HomeDirectoryType": NotRequired[HomeDirectoryTypeType],
        "Role": NotRequired[str],
        "SshPublicKeyCount": NotRequired[int],
        "UserName": NotRequired[str],
    },
)
ListWorkflowsRequestRequestTypeDef = TypedDict(
    "ListWorkflowsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListedWorkflowTypeDef = TypedDict(
    "ListedWorkflowTypeDef",
    {
        "WorkflowId": NotRequired[str],
        "Description": NotRequired[str],
        "Arn": NotRequired[str],
    },
)
S3TagTypeDef = TypedDict(
    "S3TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
SendWorkflowStepStateRequestRequestTypeDef = TypedDict(
    "SendWorkflowStepStateRequestRequestTypeDef",
    {
        "WorkflowId": str,
        "ExecutionId": str,
        "Token": str,
        "Status": CustomStepStatusType,
    },
)
UserDetailsTypeDef = TypedDict(
    "UserDetailsTypeDef",
    {
        "UserName": str,
        "ServerId": str,
        "SessionId": NotRequired[str],
    },
)
StartDirectoryListingRequestRequestTypeDef = TypedDict(
    "StartDirectoryListingRequestRequestTypeDef",
    {
        "ConnectorId": str,
        "RemoteDirectoryPath": str,
        "OutputDirectoryPath": str,
        "MaxItems": NotRequired[int],
    },
)
StartFileTransferRequestRequestTypeDef = TypedDict(
    "StartFileTransferRequestRequestTypeDef",
    {
        "ConnectorId": str,
        "SendFilePaths": NotRequired[Sequence[str]],
        "RetrieveFilePaths": NotRequired[Sequence[str]],
        "LocalDirectoryPath": NotRequired[str],
        "RemoteDirectoryPath": NotRequired[str],
    },
)
StartServerRequestRequestTypeDef = TypedDict(
    "StartServerRequestRequestTypeDef",
    {
        "ServerId": str,
    },
)
StopServerRequestRequestTypeDef = TypedDict(
    "StopServerRequestRequestTypeDef",
    {
        "ServerId": str,
    },
)
TestConnectionRequestRequestTypeDef = TypedDict(
    "TestConnectionRequestRequestTypeDef",
    {
        "ConnectorId": str,
    },
)
TestIdentityProviderRequestRequestTypeDef = TypedDict(
    "TestIdentityProviderRequestRequestTypeDef",
    {
        "ServerId": str,
        "UserName": str,
        "ServerProtocol": NotRequired[ProtocolType],
        "SourceIp": NotRequired[str],
        "UserPassword": NotRequired[str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "Arn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateAgreementRequestRequestTypeDef = TypedDict(
    "UpdateAgreementRequestRequestTypeDef",
    {
        "AgreementId": str,
        "ServerId": str,
        "Description": NotRequired[str],
        "Status": NotRequired[AgreementStatusTypeType],
        "LocalProfileId": NotRequired[str],
        "PartnerProfileId": NotRequired[str],
        "BaseDirectory": NotRequired[str],
        "AccessRole": NotRequired[str],
    },
)
UpdateHostKeyRequestRequestTypeDef = TypedDict(
    "UpdateHostKeyRequestRequestTypeDef",
    {
        "ServerId": str,
        "HostKeyId": str,
        "Description": str,
    },
)
UpdateProfileRequestRequestTypeDef = TypedDict(
    "UpdateProfileRequestRequestTypeDef",
    {
        "ProfileId": str,
        "CertificateIds": NotRequired[Sequence[str]],
    },
)
WorkflowDetailTypeDef = TypedDict(
    "WorkflowDetailTypeDef",
    {
        "WorkflowId": str,
        "ExecutionRole": str,
    },
)
CreateAccessRequestRequestTypeDef = TypedDict(
    "CreateAccessRequestRequestTypeDef",
    {
        "Role": str,
        "ServerId": str,
        "ExternalId": str,
        "HomeDirectory": NotRequired[str],
        "HomeDirectoryType": NotRequired[HomeDirectoryTypeType],
        "HomeDirectoryMappings": NotRequired[Sequence[HomeDirectoryMapEntryTypeDef]],
        "Policy": NotRequired[str],
        "PosixProfile": NotRequired[PosixProfileTypeDef],
    },
)
UpdateAccessRequestRequestTypeDef = TypedDict(
    "UpdateAccessRequestRequestTypeDef",
    {
        "ServerId": str,
        "ExternalId": str,
        "HomeDirectory": NotRequired[str],
        "HomeDirectoryType": NotRequired[HomeDirectoryTypeType],
        "HomeDirectoryMappings": NotRequired[Sequence[HomeDirectoryMapEntryTypeDef]],
        "Policy": NotRequired[str],
        "PosixProfile": NotRequired[PosixProfileTypeDef],
        "Role": NotRequired[str],
    },
)
UpdateUserRequestRequestTypeDef = TypedDict(
    "UpdateUserRequestRequestTypeDef",
    {
        "ServerId": str,
        "UserName": str,
        "HomeDirectory": NotRequired[str],
        "HomeDirectoryType": NotRequired[HomeDirectoryTypeType],
        "HomeDirectoryMappings": NotRequired[Sequence[HomeDirectoryMapEntryTypeDef]],
        "Policy": NotRequired[str],
        "PosixProfile": NotRequired[PosixProfileTypeDef],
        "Role": NotRequired[str],
    },
)
CreateAccessResponseTypeDef = TypedDict(
    "CreateAccessResponseTypeDef",
    {
        "ServerId": str,
        "ExternalId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAgreementResponseTypeDef = TypedDict(
    "CreateAgreementResponseTypeDef",
    {
        "AgreementId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateConnectorResponseTypeDef = TypedDict(
    "CreateConnectorResponseTypeDef",
    {
        "ConnectorId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProfileResponseTypeDef = TypedDict(
    "CreateProfileResponseTypeDef",
    {
        "ProfileId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateServerResponseTypeDef = TypedDict(
    "CreateServerResponseTypeDef",
    {
        "ServerId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef",
    {
        "ServerId": str,
        "UserName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWorkflowResponseTypeDef = TypedDict(
    "CreateWorkflowResponseTypeDef",
    {
        "WorkflowId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportCertificateResponseTypeDef = TypedDict(
    "ImportCertificateResponseTypeDef",
    {
        "CertificateId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportHostKeyResponseTypeDef = TypedDict(
    "ImportHostKeyResponseTypeDef",
    {
        "ServerId": str,
        "HostKeyId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportSshPublicKeyResponseTypeDef = TypedDict(
    "ImportSshPublicKeyResponseTypeDef",
    {
        "ServerId": str,
        "SshPublicKeyId": str,
        "UserName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListFileTransferResultsResponseTypeDef = TypedDict(
    "ListFileTransferResultsResponseTypeDef",
    {
        "FileTransferResults": List[ConnectorFileTransferResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListSecurityPoliciesResponseTypeDef = TypedDict(
    "ListSecurityPoliciesResponseTypeDef",
    {
        "SecurityPolicyNames": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
StartDirectoryListingResponseTypeDef = TypedDict(
    "StartDirectoryListingResponseTypeDef",
    {
        "ListingId": str,
        "OutputFileName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartFileTransferResponseTypeDef = TypedDict(
    "StartFileTransferResponseTypeDef",
    {
        "TransferId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TestConnectionResponseTypeDef = TypedDict(
    "TestConnectionResponseTypeDef",
    {
        "ConnectorId": str,
        "Status": str,
        "StatusMessage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TestIdentityProviderResponseTypeDef = TypedDict(
    "TestIdentityProviderResponseTypeDef",
    {
        "Response": str,
        "StatusCode": int,
        "Message": str,
        "Url": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAccessResponseTypeDef = TypedDict(
    "UpdateAccessResponseTypeDef",
    {
        "ServerId": str,
        "ExternalId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAgreementResponseTypeDef = TypedDict(
    "UpdateAgreementResponseTypeDef",
    {
        "AgreementId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateCertificateResponseTypeDef = TypedDict(
    "UpdateCertificateResponseTypeDef",
    {
        "CertificateId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateConnectorResponseTypeDef = TypedDict(
    "UpdateConnectorResponseTypeDef",
    {
        "ConnectorId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateHostKeyResponseTypeDef = TypedDict(
    "UpdateHostKeyResponseTypeDef",
    {
        "ServerId": str,
        "HostKeyId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateProfileResponseTypeDef = TypedDict(
    "UpdateProfileResponseTypeDef",
    {
        "ProfileId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateServerResponseTypeDef = TypedDict(
    "UpdateServerResponseTypeDef",
    {
        "ServerId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateUserResponseTypeDef = TypedDict(
    "UpdateUserResponseTypeDef",
    {
        "ServerId": str,
        "UserName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAgreementRequestRequestTypeDef = TypedDict(
    "CreateAgreementRequestRequestTypeDef",
    {
        "ServerId": str,
        "LocalProfileId": str,
        "PartnerProfileId": str,
        "BaseDirectory": str,
        "AccessRole": str,
        "Description": NotRequired[str],
        "Status": NotRequired[AgreementStatusTypeType],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateProfileRequestRequestTypeDef = TypedDict(
    "CreateProfileRequestRequestTypeDef",
    {
        "As2Id": str,
        "ProfileType": ProfileTypeType,
        "CertificateIds": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateUserRequestRequestTypeDef = TypedDict(
    "CreateUserRequestRequestTypeDef",
    {
        "Role": str,
        "ServerId": str,
        "UserName": str,
        "HomeDirectory": NotRequired[str],
        "HomeDirectoryType": NotRequired[HomeDirectoryTypeType],
        "HomeDirectoryMappings": NotRequired[Sequence[HomeDirectoryMapEntryTypeDef]],
        "Policy": NotRequired[str],
        "PosixProfile": NotRequired[PosixProfileTypeDef],
        "SshPublicKeyBody": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
DescribedAgreementTypeDef = TypedDict(
    "DescribedAgreementTypeDef",
    {
        "Arn": str,
        "AgreementId": NotRequired[str],
        "Description": NotRequired[str],
        "Status": NotRequired[AgreementStatusTypeType],
        "ServerId": NotRequired[str],
        "LocalProfileId": NotRequired[str],
        "PartnerProfileId": NotRequired[str],
        "BaseDirectory": NotRequired[str],
        "AccessRole": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
DescribedCertificateTypeDef = TypedDict(
    "DescribedCertificateTypeDef",
    {
        "Arn": str,
        "CertificateId": NotRequired[str],
        "Usage": NotRequired[CertificateUsageTypeType],
        "Status": NotRequired[CertificateStatusTypeType],
        "Certificate": NotRequired[str],
        "CertificateChain": NotRequired[str],
        "ActiveDate": NotRequired[datetime],
        "InactiveDate": NotRequired[datetime],
        "Serial": NotRequired[str],
        "NotBeforeDate": NotRequired[datetime],
        "NotAfterDate": NotRequired[datetime],
        "Type": NotRequired[CertificateTypeType],
        "Description": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
DescribedHostKeyTypeDef = TypedDict(
    "DescribedHostKeyTypeDef",
    {
        "Arn": str,
        "HostKeyId": NotRequired[str],
        "HostKeyFingerprint": NotRequired[str],
        "Description": NotRequired[str],
        "Type": NotRequired[str],
        "DateImported": NotRequired[datetime],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
DescribedProfileTypeDef = TypedDict(
    "DescribedProfileTypeDef",
    {
        "Arn": str,
        "ProfileId": NotRequired[str],
        "ProfileType": NotRequired[ProfileTypeType],
        "As2Id": NotRequired[str],
        "CertificateIds": NotRequired[List[str]],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
ImportHostKeyRequestRequestTypeDef = TypedDict(
    "ImportHostKeyRequestRequestTypeDef",
    {
        "ServerId": str,
        "HostKeyBody": str,
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Arn": str,
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "Arn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CreateConnectorRequestRequestTypeDef = TypedDict(
    "CreateConnectorRequestRequestTypeDef",
    {
        "Url": str,
        "AccessRole": str,
        "As2Config": NotRequired[As2ConnectorConfigTypeDef],
        "LoggingRole": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "SftpConfig": NotRequired[SftpConnectorConfigTypeDef],
        "SecurityPolicyName": NotRequired[str],
    },
)
UpdateConnectorRequestRequestTypeDef = TypedDict(
    "UpdateConnectorRequestRequestTypeDef",
    {
        "ConnectorId": str,
        "Url": NotRequired[str],
        "As2Config": NotRequired[As2ConnectorConfigTypeDef],
        "AccessRole": NotRequired[str],
        "LoggingRole": NotRequired[str],
        "SftpConfig": NotRequired[SftpConnectorConfigTypeDef],
        "SecurityPolicyName": NotRequired[str],
    },
)
DescribeSecurityPolicyResponseTypeDef = TypedDict(
    "DescribeSecurityPolicyResponseTypeDef",
    {
        "SecurityPolicy": DescribedSecurityPolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeServerRequestServerOfflineWaitTypeDef = TypedDict(
    "DescribeServerRequestServerOfflineWaitTypeDef",
    {
        "ServerId": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeServerRequestServerOnlineWaitTypeDef = TypedDict(
    "DescribeServerRequestServerOnlineWaitTypeDef",
    {
        "ServerId": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribedAccessTypeDef = TypedDict(
    "DescribedAccessTypeDef",
    {
        "HomeDirectory": NotRequired[str],
        "HomeDirectoryMappings": NotRequired[List[HomeDirectoryMapEntryTypeDef]],
        "HomeDirectoryType": NotRequired[HomeDirectoryTypeType],
        "Policy": NotRequired[str],
        "PosixProfile": NotRequired[PosixProfileOutputTypeDef],
        "Role": NotRequired[str],
        "ExternalId": NotRequired[str],
    },
)
DescribedConnectorTypeDef = TypedDict(
    "DescribedConnectorTypeDef",
    {
        "Arn": str,
        "ConnectorId": NotRequired[str],
        "Url": NotRequired[str],
        "As2Config": NotRequired[As2ConnectorConfigTypeDef],
        "AccessRole": NotRequired[str],
        "LoggingRole": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "SftpConfig": NotRequired[SftpConnectorConfigOutputTypeDef],
        "ServiceManagedEgressIpAddresses": NotRequired[List[str]],
        "SecurityPolicyName": NotRequired[str],
    },
)
DescribedUserTypeDef = TypedDict(
    "DescribedUserTypeDef",
    {
        "Arn": str,
        "HomeDirectory": NotRequired[str],
        "HomeDirectoryMappings": NotRequired[List[HomeDirectoryMapEntryTypeDef]],
        "HomeDirectoryType": NotRequired[HomeDirectoryTypeType],
        "Policy": NotRequired[str],
        "PosixProfile": NotRequired[PosixProfileOutputTypeDef],
        "Role": NotRequired[str],
        "SshPublicKeys": NotRequired[List[SshPublicKeyTypeDef]],
        "Tags": NotRequired[List[TagTypeDef]],
        "UserName": NotRequired[str],
    },
)
ExecutionStepResultTypeDef = TypedDict(
    "ExecutionStepResultTypeDef",
    {
        "StepType": NotRequired[WorkflowStepTypeType],
        "Outputs": NotRequired[str],
        "Error": NotRequired[ExecutionErrorTypeDef],
    },
)
FileLocationTypeDef = TypedDict(
    "FileLocationTypeDef",
    {
        "S3FileLocation": NotRequired[S3FileLocationTypeDef],
        "EfsFileLocation": NotRequired[EfsFileLocationTypeDef],
    },
)
ImportCertificateRequestRequestTypeDef = TypedDict(
    "ImportCertificateRequestRequestTypeDef",
    {
        "Usage": CertificateUsageTypeType,
        "Certificate": str,
        "CertificateChain": NotRequired[str],
        "PrivateKey": NotRequired[str],
        "ActiveDate": NotRequired[TimestampTypeDef],
        "InactiveDate": NotRequired[TimestampTypeDef],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
UpdateCertificateRequestRequestTypeDef = TypedDict(
    "UpdateCertificateRequestRequestTypeDef",
    {
        "CertificateId": str,
        "ActiveDate": NotRequired[TimestampTypeDef],
        "InactiveDate": NotRequired[TimestampTypeDef],
        "Description": NotRequired[str],
    },
)
InputFileLocationTypeDef = TypedDict(
    "InputFileLocationTypeDef",
    {
        "S3FileLocation": NotRequired[S3InputFileLocationTypeDef],
        "EfsFileLocation": NotRequired[EfsFileLocationTypeDef],
    },
)
ListAccessesRequestListAccessesPaginateTypeDef = TypedDict(
    "ListAccessesRequestListAccessesPaginateTypeDef",
    {
        "ServerId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAgreementsRequestListAgreementsPaginateTypeDef = TypedDict(
    "ListAgreementsRequestListAgreementsPaginateTypeDef",
    {
        "ServerId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCertificatesRequestListCertificatesPaginateTypeDef = TypedDict(
    "ListCertificatesRequestListCertificatesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListConnectorsRequestListConnectorsPaginateTypeDef = TypedDict(
    "ListConnectorsRequestListConnectorsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListExecutionsRequestListExecutionsPaginateTypeDef = TypedDict(
    "ListExecutionsRequestListExecutionsPaginateTypeDef",
    {
        "WorkflowId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFileTransferResultsRequestListFileTransferResultsPaginateTypeDef = TypedDict(
    "ListFileTransferResultsRequestListFileTransferResultsPaginateTypeDef",
    {
        "ConnectorId": str,
        "TransferId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProfilesRequestListProfilesPaginateTypeDef = TypedDict(
    "ListProfilesRequestListProfilesPaginateTypeDef",
    {
        "ProfileType": NotRequired[ProfileTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSecurityPoliciesRequestListSecurityPoliciesPaginateTypeDef = TypedDict(
    "ListSecurityPoliciesRequestListSecurityPoliciesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListServersRequestListServersPaginateTypeDef = TypedDict(
    "ListServersRequestListServersPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTagsForResourceRequestListTagsForResourcePaginateTypeDef = TypedDict(
    "ListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    {
        "Arn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListUsersRequestListUsersPaginateTypeDef = TypedDict(
    "ListUsersRequestListUsersPaginateTypeDef",
    {
        "ServerId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWorkflowsRequestListWorkflowsPaginateTypeDef = TypedDict(
    "ListWorkflowsRequestListWorkflowsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAccessesResponseTypeDef = TypedDict(
    "ListAccessesResponseTypeDef",
    {
        "ServerId": str,
        "Accesses": List[ListedAccessTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListAgreementsResponseTypeDef = TypedDict(
    "ListAgreementsResponseTypeDef",
    {
        "Agreements": List[ListedAgreementTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListCertificatesResponseTypeDef = TypedDict(
    "ListCertificatesResponseTypeDef",
    {
        "Certificates": List[ListedCertificateTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListConnectorsResponseTypeDef = TypedDict(
    "ListConnectorsResponseTypeDef",
    {
        "Connectors": List[ListedConnectorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListHostKeysResponseTypeDef = TypedDict(
    "ListHostKeysResponseTypeDef",
    {
        "ServerId": str,
        "HostKeys": List[ListedHostKeyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListProfilesResponseTypeDef = TypedDict(
    "ListProfilesResponseTypeDef",
    {
        "Profiles": List[ListedProfileTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListServersResponseTypeDef = TypedDict(
    "ListServersResponseTypeDef",
    {
        "Servers": List[ListedServerTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "ServerId": str,
        "Users": List[ListedUserTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListWorkflowsResponseTypeDef = TypedDict(
    "ListWorkflowsResponseTypeDef",
    {
        "Workflows": List[ListedWorkflowTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
TagStepDetailsOutputTypeDef = TypedDict(
    "TagStepDetailsOutputTypeDef",
    {
        "Name": NotRequired[str],
        "Tags": NotRequired[List[S3TagTypeDef]],
        "SourceFileLocation": NotRequired[str],
    },
)
TagStepDetailsTypeDef = TypedDict(
    "TagStepDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Tags": NotRequired[Sequence[S3TagTypeDef]],
        "SourceFileLocation": NotRequired[str],
    },
)
ServiceMetadataTypeDef = TypedDict(
    "ServiceMetadataTypeDef",
    {
        "UserDetails": UserDetailsTypeDef,
    },
)
WorkflowDetailsOutputTypeDef = TypedDict(
    "WorkflowDetailsOutputTypeDef",
    {
        "OnUpload": NotRequired[List[WorkflowDetailTypeDef]],
        "OnPartialUpload": NotRequired[List[WorkflowDetailTypeDef]],
    },
)
WorkflowDetailsTypeDef = TypedDict(
    "WorkflowDetailsTypeDef",
    {
        "OnUpload": NotRequired[Sequence[WorkflowDetailTypeDef]],
        "OnPartialUpload": NotRequired[Sequence[WorkflowDetailTypeDef]],
    },
)
DescribeAgreementResponseTypeDef = TypedDict(
    "DescribeAgreementResponseTypeDef",
    {
        "Agreement": DescribedAgreementTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeCertificateResponseTypeDef = TypedDict(
    "DescribeCertificateResponseTypeDef",
    {
        "Certificate": DescribedCertificateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeHostKeyResponseTypeDef = TypedDict(
    "DescribeHostKeyResponseTypeDef",
    {
        "HostKey": DescribedHostKeyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeProfileResponseTypeDef = TypedDict(
    "DescribeProfileResponseTypeDef",
    {
        "Profile": DescribedProfileTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAccessResponseTypeDef = TypedDict(
    "DescribeAccessResponseTypeDef",
    {
        "ServerId": str,
        "Access": DescribedAccessTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeConnectorResponseTypeDef = TypedDict(
    "DescribeConnectorResponseTypeDef",
    {
        "Connector": DescribedConnectorTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeUserResponseTypeDef = TypedDict(
    "DescribeUserResponseTypeDef",
    {
        "ServerId": str,
        "User": DescribedUserTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExecutionResultsTypeDef = TypedDict(
    "ExecutionResultsTypeDef",
    {
        "Steps": NotRequired[List[ExecutionStepResultTypeDef]],
        "OnExceptionSteps": NotRequired[List[ExecutionStepResultTypeDef]],
    },
)
CopyStepDetailsTypeDef = TypedDict(
    "CopyStepDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "DestinationFileLocation": NotRequired[InputFileLocationTypeDef],
        "OverwriteExisting": NotRequired[OverwriteExistingType],
        "SourceFileLocation": NotRequired[str],
    },
)
DecryptStepDetailsTypeDef = TypedDict(
    "DecryptStepDetailsTypeDef",
    {
        "Type": Literal["PGP"],
        "DestinationFileLocation": InputFileLocationTypeDef,
        "Name": NotRequired[str],
        "SourceFileLocation": NotRequired[str],
        "OverwriteExisting": NotRequired[OverwriteExistingType],
    },
)
TagStepDetailsUnionTypeDef = Union[TagStepDetailsTypeDef, TagStepDetailsOutputTypeDef]
ListedExecutionTypeDef = TypedDict(
    "ListedExecutionTypeDef",
    {
        "ExecutionId": NotRequired[str],
        "InitialFileLocation": NotRequired[FileLocationTypeDef],
        "ServiceMetadata": NotRequired[ServiceMetadataTypeDef],
        "Status": NotRequired[ExecutionStatusType],
    },
)
DescribedServerTypeDef = TypedDict(
    "DescribedServerTypeDef",
    {
        "Arn": str,
        "Certificate": NotRequired[str],
        "ProtocolDetails": NotRequired[ProtocolDetailsOutputTypeDef],
        "Domain": NotRequired[DomainType],
        "EndpointDetails": NotRequired[EndpointDetailsOutputTypeDef],
        "EndpointType": NotRequired[EndpointTypeType],
        "HostKeyFingerprint": NotRequired[str],
        "IdentityProviderDetails": NotRequired[IdentityProviderDetailsTypeDef],
        "IdentityProviderType": NotRequired[IdentityProviderTypeType],
        "LoggingRole": NotRequired[str],
        "PostAuthenticationLoginBanner": NotRequired[str],
        "PreAuthenticationLoginBanner": NotRequired[str],
        "Protocols": NotRequired[List[ProtocolType]],
        "SecurityPolicyName": NotRequired[str],
        "ServerId": NotRequired[str],
        "State": NotRequired[StateType],
        "Tags": NotRequired[List[TagTypeDef]],
        "UserCount": NotRequired[int],
        "WorkflowDetails": NotRequired[WorkflowDetailsOutputTypeDef],
        "StructuredLogDestinations": NotRequired[List[str]],
        "S3StorageOptions": NotRequired[S3StorageOptionsTypeDef],
        "As2ServiceManagedEgressIpAddresses": NotRequired[List[str]],
    },
)
CreateServerRequestRequestTypeDef = TypedDict(
    "CreateServerRequestRequestTypeDef",
    {
        "Certificate": NotRequired[str],
        "Domain": NotRequired[DomainType],
        "EndpointDetails": NotRequired[EndpointDetailsTypeDef],
        "EndpointType": NotRequired[EndpointTypeType],
        "HostKey": NotRequired[str],
        "IdentityProviderDetails": NotRequired[IdentityProviderDetailsTypeDef],
        "IdentityProviderType": NotRequired[IdentityProviderTypeType],
        "LoggingRole": NotRequired[str],
        "PostAuthenticationLoginBanner": NotRequired[str],
        "PreAuthenticationLoginBanner": NotRequired[str],
        "Protocols": NotRequired[Sequence[ProtocolType]],
        "ProtocolDetails": NotRequired[ProtocolDetailsTypeDef],
        "SecurityPolicyName": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "WorkflowDetails": NotRequired[WorkflowDetailsTypeDef],
        "StructuredLogDestinations": NotRequired[Sequence[str]],
        "S3StorageOptions": NotRequired[S3StorageOptionsTypeDef],
    },
)
UpdateServerRequestRequestTypeDef = TypedDict(
    "UpdateServerRequestRequestTypeDef",
    {
        "ServerId": str,
        "Certificate": NotRequired[str],
        "ProtocolDetails": NotRequired[ProtocolDetailsTypeDef],
        "EndpointDetails": NotRequired[EndpointDetailsTypeDef],
        "EndpointType": NotRequired[EndpointTypeType],
        "HostKey": NotRequired[str],
        "IdentityProviderDetails": NotRequired[IdentityProviderDetailsTypeDef],
        "LoggingRole": NotRequired[str],
        "PostAuthenticationLoginBanner": NotRequired[str],
        "PreAuthenticationLoginBanner": NotRequired[str],
        "Protocols": NotRequired[Sequence[ProtocolType]],
        "SecurityPolicyName": NotRequired[str],
        "WorkflowDetails": NotRequired[WorkflowDetailsTypeDef],
        "StructuredLogDestinations": NotRequired[Sequence[str]],
        "S3StorageOptions": NotRequired[S3StorageOptionsTypeDef],
    },
)
DescribedExecutionTypeDef = TypedDict(
    "DescribedExecutionTypeDef",
    {
        "ExecutionId": NotRequired[str],
        "InitialFileLocation": NotRequired[FileLocationTypeDef],
        "ServiceMetadata": NotRequired[ServiceMetadataTypeDef],
        "ExecutionRole": NotRequired[str],
        "LoggingConfiguration": NotRequired[LoggingConfigurationTypeDef],
        "PosixProfile": NotRequired[PosixProfileOutputTypeDef],
        "Status": NotRequired[ExecutionStatusType],
        "Results": NotRequired[ExecutionResultsTypeDef],
    },
)
WorkflowStepOutputTypeDef = TypedDict(
    "WorkflowStepOutputTypeDef",
    {
        "Type": NotRequired[WorkflowStepTypeType],
        "CopyStepDetails": NotRequired[CopyStepDetailsTypeDef],
        "CustomStepDetails": NotRequired[CustomStepDetailsTypeDef],
        "DeleteStepDetails": NotRequired[DeleteStepDetailsTypeDef],
        "TagStepDetails": NotRequired[TagStepDetailsOutputTypeDef],
        "DecryptStepDetails": NotRequired[DecryptStepDetailsTypeDef],
    },
)
WorkflowStepTypeDef = TypedDict(
    "WorkflowStepTypeDef",
    {
        "Type": NotRequired[WorkflowStepTypeType],
        "CopyStepDetails": NotRequired[CopyStepDetailsTypeDef],
        "CustomStepDetails": NotRequired[CustomStepDetailsTypeDef],
        "DeleteStepDetails": NotRequired[DeleteStepDetailsTypeDef],
        "TagStepDetails": NotRequired[TagStepDetailsUnionTypeDef],
        "DecryptStepDetails": NotRequired[DecryptStepDetailsTypeDef],
    },
)
ListExecutionsResponseTypeDef = TypedDict(
    "ListExecutionsResponseTypeDef",
    {
        "WorkflowId": str,
        "Executions": List[ListedExecutionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeServerResponseTypeDef = TypedDict(
    "DescribeServerResponseTypeDef",
    {
        "Server": DescribedServerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeExecutionResponseTypeDef = TypedDict(
    "DescribeExecutionResponseTypeDef",
    {
        "WorkflowId": str,
        "Execution": DescribedExecutionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribedWorkflowTypeDef = TypedDict(
    "DescribedWorkflowTypeDef",
    {
        "Arn": str,
        "Description": NotRequired[str],
        "Steps": NotRequired[List[WorkflowStepOutputTypeDef]],
        "OnExceptionSteps": NotRequired[List[WorkflowStepOutputTypeDef]],
        "WorkflowId": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
WorkflowStepUnionTypeDef = Union[WorkflowStepTypeDef, WorkflowStepOutputTypeDef]
DescribeWorkflowResponseTypeDef = TypedDict(
    "DescribeWorkflowResponseTypeDef",
    {
        "Workflow": DescribedWorkflowTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWorkflowRequestRequestTypeDef = TypedDict(
    "CreateWorkflowRequestRequestTypeDef",
    {
        "Steps": Sequence[WorkflowStepUnionTypeDef],
        "Description": NotRequired[str],
        "OnExceptionSteps": NotRequired[Sequence[WorkflowStepTypeDef]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
