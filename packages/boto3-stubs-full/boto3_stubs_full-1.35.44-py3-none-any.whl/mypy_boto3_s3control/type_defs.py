"""
Type annotations for s3control service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3control/type_defs/)

Usage::

    ```python
    from mypy_boto3_s3control.type_defs import AbortIncompleteMultipartUploadTypeDef

    data: AbortIncompleteMultipartUploadTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    AsyncOperationNameType,
    BucketCannedACLType,
    BucketLocationConstraintType,
    BucketVersioningStatusType,
    DeleteMarkerReplicationStatusType,
    ExistingObjectReplicationStatusType,
    ExpirationStatusType,
    FormatType,
    GranteeTypeType,
    JobManifestFieldNameType,
    JobManifestFormatType,
    JobReportScopeType,
    JobStatusType,
    MetricsStatusType,
    MFADeleteStatusType,
    MFADeleteType,
    MultiRegionAccessPointStatusType,
    NetworkOriginType,
    ObjectLambdaAccessPointAliasStatusType,
    ObjectLambdaAllowedFeatureType,
    ObjectLambdaTransformationConfigurationActionType,
    OperationNameType,
    PermissionType,
    PrivilegeType,
    ReplicaModificationsStatusType,
    ReplicationRuleStatusType,
    ReplicationStatusType,
    ReplicationStorageClassType,
    ReplicationTimeStatusType,
    RequestedJobStatusType,
    S3CannedAccessControlListType,
    S3ChecksumAlgorithmType,
    S3GlacierJobTierType,
    S3GranteeTypeIdentifierType,
    S3MetadataDirectiveType,
    S3ObjectLockLegalHoldStatusType,
    S3ObjectLockModeType,
    S3ObjectLockRetentionModeType,
    S3PermissionType,
    S3SSEAlgorithmType,
    S3StorageClassType,
    SseKmsEncryptedObjectsStatusType,
    TransitionStorageClassType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AbortIncompleteMultipartUploadTypeDef",
    "AccessControlTranslationTypeDef",
    "AccessGrantsLocationConfigurationTypeDef",
    "VpcConfigurationTypeDef",
    "ActivityMetricsTypeDef",
    "AdvancedCostOptimizationMetricsTypeDef",
    "AdvancedDataProtectionMetricsTypeDef",
    "DetailedStatusCodesMetricsTypeDef",
    "AssociateAccessGrantsIdentityCenterRequestRequestTypeDef",
    "AsyncErrorDetailsTypeDef",
    "DeleteMultiRegionAccessPointInputTypeDef",
    "PutMultiRegionAccessPointPolicyInputTypeDef",
    "AwsLambdaTransformationTypeDef",
    "CloudWatchMetricsTypeDef",
    "GranteeTypeDef",
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "ObjectLambdaAccessPointAliasTypeDef",
    "PublicAccessBlockConfigurationTypeDef",
    "CreateBucketConfigurationTypeDef",
    "JobReportTypeDef",
    "S3TagTypeDef",
    "RegionTypeDef",
    "CredentialsTypeDef",
    "DeleteAccessGrantRequestRequestTypeDef",
    "DeleteAccessGrantsInstanceRequestRequestTypeDef",
    "DeleteAccessGrantsInstanceResourcePolicyRequestRequestTypeDef",
    "DeleteAccessGrantsLocationRequestRequestTypeDef",
    "DeleteAccessPointForObjectLambdaRequestRequestTypeDef",
    "DeleteAccessPointPolicyForObjectLambdaRequestRequestTypeDef",
    "DeleteAccessPointPolicyRequestRequestTypeDef",
    "DeleteAccessPointRequestRequestTypeDef",
    "DeleteBucketLifecycleConfigurationRequestRequestTypeDef",
    "DeleteBucketPolicyRequestRequestTypeDef",
    "DeleteBucketReplicationRequestRequestTypeDef",
    "DeleteBucketRequestRequestTypeDef",
    "DeleteBucketTaggingRequestRequestTypeDef",
    "DeleteJobTaggingRequestRequestTypeDef",
    "DeleteMarkerReplicationTypeDef",
    "DeletePublicAccessBlockRequestRequestTypeDef",
    "DeleteStorageLensConfigurationRequestRequestTypeDef",
    "DeleteStorageLensConfigurationTaggingRequestRequestTypeDef",
    "DeleteStorageLensGroupRequestRequestTypeDef",
    "DescribeJobRequestRequestTypeDef",
    "DescribeMultiRegionAccessPointOperationRequestRequestTypeDef",
    "EncryptionConfigurationTypeDef",
    "DissociateAccessGrantsIdentityCenterRequestRequestTypeDef",
    "EstablishedMultiRegionAccessPointPolicyTypeDef",
    "ExcludeOutputTypeDef",
    "ExcludeTypeDef",
    "ExistingObjectReplicationTypeDef",
    "SSEKMSEncryptionTypeDef",
    "GetAccessGrantRequestRequestTypeDef",
    "GetAccessGrantsInstanceForPrefixRequestRequestTypeDef",
    "GetAccessGrantsInstanceRequestRequestTypeDef",
    "GetAccessGrantsInstanceResourcePolicyRequestRequestTypeDef",
    "GetAccessGrantsLocationRequestRequestTypeDef",
    "GetAccessPointConfigurationForObjectLambdaRequestRequestTypeDef",
    "GetAccessPointForObjectLambdaRequestRequestTypeDef",
    "GetAccessPointPolicyForObjectLambdaRequestRequestTypeDef",
    "GetAccessPointPolicyRequestRequestTypeDef",
    "GetAccessPointPolicyStatusForObjectLambdaRequestRequestTypeDef",
    "PolicyStatusTypeDef",
    "GetAccessPointPolicyStatusRequestRequestTypeDef",
    "GetAccessPointRequestRequestTypeDef",
    "GetBucketLifecycleConfigurationRequestRequestTypeDef",
    "GetBucketPolicyRequestRequestTypeDef",
    "GetBucketReplicationRequestRequestTypeDef",
    "GetBucketRequestRequestTypeDef",
    "GetBucketTaggingRequestRequestTypeDef",
    "GetBucketVersioningRequestRequestTypeDef",
    "GetDataAccessRequestRequestTypeDef",
    "GetJobTaggingRequestRequestTypeDef",
    "GetMultiRegionAccessPointPolicyRequestRequestTypeDef",
    "GetMultiRegionAccessPointPolicyStatusRequestRequestTypeDef",
    "GetMultiRegionAccessPointRequestRequestTypeDef",
    "GetMultiRegionAccessPointRoutesRequestRequestTypeDef",
    "MultiRegionAccessPointRouteTypeDef",
    "GetPublicAccessBlockRequestRequestTypeDef",
    "GetStorageLensConfigurationRequestRequestTypeDef",
    "GetStorageLensConfigurationTaggingRequestRequestTypeDef",
    "StorageLensTagTypeDef",
    "GetStorageLensGroupRequestRequestTypeDef",
    "IncludeOutputTypeDef",
    "IncludeTypeDef",
    "JobFailureTypeDef",
    "KeyNameConstraintOutputTypeDef",
    "TimestampTypeDef",
    "JobManifestLocationTypeDef",
    "JobManifestSpecOutputTypeDef",
    "JobManifestSpecTypeDef",
    "LambdaInvokeOperationOutputTypeDef",
    "S3InitiateRestoreObjectOperationTypeDef",
    "JobTimersTypeDef",
    "KeyNameConstraintTypeDef",
    "LambdaInvokeOperationTypeDef",
    "LifecycleExpirationOutputTypeDef",
    "NoncurrentVersionExpirationTypeDef",
    "NoncurrentVersionTransitionTypeDef",
    "TransitionOutputTypeDef",
    "ListAccessGrantsInstanceEntryTypeDef",
    "ListAccessGrantsInstancesRequestRequestTypeDef",
    "ListAccessGrantsLocationsEntryTypeDef",
    "ListAccessGrantsLocationsRequestRequestTypeDef",
    "ListAccessGrantsRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListAccessPointsForObjectLambdaRequestRequestTypeDef",
    "ListAccessPointsRequestRequestTypeDef",
    "ListCallerAccessGrantsEntryTypeDef",
    "ListCallerAccessGrantsRequestRequestTypeDef",
    "ListJobsRequestRequestTypeDef",
    "ListMultiRegionAccessPointsRequestRequestTypeDef",
    "ListRegionalBucketsRequestRequestTypeDef",
    "RegionalBucketTypeDef",
    "ListStorageLensConfigurationEntryTypeDef",
    "ListStorageLensConfigurationsRequestRequestTypeDef",
    "ListStorageLensGroupEntryTypeDef",
    "ListStorageLensGroupsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "MatchObjectAgeTypeDef",
    "MatchObjectSizeTypeDef",
    "ReplicationTimeValueTypeDef",
    "ProposedMultiRegionAccessPointPolicyTypeDef",
    "MultiRegionAccessPointRegionalResponseTypeDef",
    "RegionReportTypeDef",
    "SelectionCriteriaTypeDef",
    "PutAccessGrantsInstanceResourcePolicyRequestRequestTypeDef",
    "PutAccessPointPolicyForObjectLambdaRequestRequestTypeDef",
    "PutAccessPointPolicyRequestRequestTypeDef",
    "PutBucketPolicyRequestRequestTypeDef",
    "VersioningConfigurationTypeDef",
    "ReplicaModificationsTypeDef",
    "S3ObjectOwnerTypeDef",
    "S3ObjectMetadataOutputTypeDef",
    "S3GranteeTypeDef",
    "S3ObjectLockLegalHoldTypeDef",
    "S3RetentionOutputTypeDef",
    "SSEKMSTypeDef",
    "SseKmsEncryptedObjectsTypeDef",
    "StorageLensAwsOrgTypeDef",
    "StorageLensGroupLevelSelectionCriteriaOutputTypeDef",
    "StorageLensGroupLevelSelectionCriteriaTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAccessGrantsLocationRequestRequestTypeDef",
    "UpdateJobPriorityRequestRequestTypeDef",
    "UpdateJobStatusRequestRequestTypeDef",
    "AccessPointTypeDef",
    "DeleteMultiRegionAccessPointRequestRequestTypeDef",
    "PutMultiRegionAccessPointPolicyRequestRequestTypeDef",
    "ObjectLambdaContentTransformationTypeDef",
    "ListAccessGrantEntryTypeDef",
    "CreateAccessGrantRequestRequestTypeDef",
    "CreateAccessGrantsInstanceRequestRequestTypeDef",
    "CreateAccessGrantsLocationRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateAccessGrantResultTypeDef",
    "CreateAccessGrantsInstanceResultTypeDef",
    "CreateAccessGrantsLocationResultTypeDef",
    "CreateAccessPointResultTypeDef",
    "CreateBucketResultTypeDef",
    "CreateJobResultTypeDef",
    "CreateMultiRegionAccessPointResultTypeDef",
    "DeleteMultiRegionAccessPointResultTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetAccessGrantResultTypeDef",
    "GetAccessGrantsInstanceForPrefixResultTypeDef",
    "GetAccessGrantsInstanceResourcePolicyResultTypeDef",
    "GetAccessGrantsInstanceResultTypeDef",
    "GetAccessGrantsLocationResultTypeDef",
    "GetAccessPointPolicyForObjectLambdaResultTypeDef",
    "GetAccessPointPolicyResultTypeDef",
    "GetBucketPolicyResultTypeDef",
    "GetBucketResultTypeDef",
    "GetBucketVersioningResultTypeDef",
    "ListTagsForResourceResultTypeDef",
    "PutAccessGrantsInstanceResourcePolicyResultTypeDef",
    "PutMultiRegionAccessPointPolicyResultTypeDef",
    "UpdateAccessGrantsLocationResultTypeDef",
    "UpdateJobPriorityResultTypeDef",
    "UpdateJobStatusResultTypeDef",
    "CreateAccessPointForObjectLambdaResultTypeDef",
    "ObjectLambdaAccessPointTypeDef",
    "CreateAccessPointRequestRequestTypeDef",
    "GetAccessPointForObjectLambdaResultTypeDef",
    "GetAccessPointResultTypeDef",
    "GetPublicAccessBlockOutputTypeDef",
    "PutPublicAccessBlockRequestRequestTypeDef",
    "CreateBucketRequestRequestTypeDef",
    "GetBucketTaggingResultTypeDef",
    "GetJobTaggingResultTypeDef",
    "LifecycleRuleAndOperatorOutputTypeDef",
    "LifecycleRuleAndOperatorTypeDef",
    "PutJobTaggingRequestRequestTypeDef",
    "ReplicationRuleAndOperatorOutputTypeDef",
    "ReplicationRuleAndOperatorTypeDef",
    "S3SetObjectTaggingOperationOutputTypeDef",
    "S3SetObjectTaggingOperationTypeDef",
    "TaggingTypeDef",
    "CreateMultiRegionAccessPointInputOutputTypeDef",
    "CreateMultiRegionAccessPointInputTypeDef",
    "GetDataAccessResultTypeDef",
    "ExcludeUnionTypeDef",
    "GeneratedManifestEncryptionOutputTypeDef",
    "GeneratedManifestEncryptionTypeDef",
    "GetAccessPointPolicyStatusForObjectLambdaResultTypeDef",
    "GetAccessPointPolicyStatusResultTypeDef",
    "GetMultiRegionAccessPointPolicyStatusResultTypeDef",
    "GetMultiRegionAccessPointRoutesResultTypeDef",
    "SubmitMultiRegionAccessPointRoutesRequestRequestTypeDef",
    "GetStorageLensConfigurationTaggingResultTypeDef",
    "PutStorageLensConfigurationTaggingRequestRequestTypeDef",
    "IncludeUnionTypeDef",
    "JobManifestGeneratorFilterOutputTypeDef",
    "LifecycleExpirationTypeDef",
    "S3ObjectMetadataTypeDef",
    "S3RetentionTypeDef",
    "TransitionTypeDef",
    "S3GeneratedManifestDescriptorTypeDef",
    "JobManifestOutputTypeDef",
    "JobManifestSpecUnionTypeDef",
    "JobProgressSummaryTypeDef",
    "KeyNameConstraintUnionTypeDef",
    "LambdaInvokeOperationUnionTypeDef",
    "ListAccessGrantsInstancesResultTypeDef",
    "ListAccessGrantsLocationsResultTypeDef",
    "ListAccessPointsForObjectLambdaRequestListAccessPointsForObjectLambdaPaginateTypeDef",
    "ListCallerAccessGrantsRequestListCallerAccessGrantsPaginateTypeDef",
    "ListCallerAccessGrantsResultTypeDef",
    "ListRegionalBucketsResultTypeDef",
    "ListStorageLensConfigurationsResultTypeDef",
    "ListStorageLensGroupsResultTypeDef",
    "StorageLensGroupAndOperatorOutputTypeDef",
    "StorageLensGroupAndOperatorTypeDef",
    "StorageLensGroupOrOperatorOutputTypeDef",
    "StorageLensGroupOrOperatorTypeDef",
    "MetricsTypeDef",
    "ReplicationTimeTypeDef",
    "MultiRegionAccessPointPolicyDocumentTypeDef",
    "MultiRegionAccessPointsAsyncResponseTypeDef",
    "MultiRegionAccessPointReportTypeDef",
    "PrefixLevelStorageMetricsTypeDef",
    "PutBucketVersioningRequestRequestTypeDef",
    "S3GrantTypeDef",
    "S3SetObjectLegalHoldOperationTypeDef",
    "S3SetObjectRetentionOperationOutputTypeDef",
    "StorageLensDataExportEncryptionOutputTypeDef",
    "StorageLensDataExportEncryptionTypeDef",
    "SourceSelectionCriteriaTypeDef",
    "StorageLensGroupLevelOutputTypeDef",
    "StorageLensGroupLevelSelectionCriteriaUnionTypeDef",
    "ListAccessPointsResultTypeDef",
    "ObjectLambdaTransformationConfigurationOutputTypeDef",
    "ObjectLambdaTransformationConfigurationTypeDef",
    "ListAccessGrantsResultTypeDef",
    "ListAccessPointsForObjectLambdaResultTypeDef",
    "LifecycleRuleFilterOutputTypeDef",
    "LifecycleRuleAndOperatorUnionTypeDef",
    "ReplicationRuleFilterOutputTypeDef",
    "ReplicationRuleAndOperatorUnionTypeDef",
    "S3SetObjectTaggingOperationUnionTypeDef",
    "PutBucketTaggingRequestRequestTypeDef",
    "AsyncRequestParametersTypeDef",
    "CreateMultiRegionAccessPointRequestRequestTypeDef",
    "S3ManifestOutputLocationOutputTypeDef",
    "GeneratedManifestEncryptionUnionTypeDef",
    "LifecycleExpirationUnionTypeDef",
    "S3ObjectMetadataUnionTypeDef",
    "S3RetentionUnionTypeDef",
    "TransitionUnionTypeDef",
    "JobManifestTypeDef",
    "JobListDescriptorTypeDef",
    "JobManifestGeneratorFilterTypeDef",
    "StorageLensGroupAndOperatorUnionTypeDef",
    "StorageLensGroupFilterOutputTypeDef",
    "StorageLensGroupOrOperatorUnionTypeDef",
    "DestinationTypeDef",
    "GetMultiRegionAccessPointPolicyResultTypeDef",
    "AsyncResponseDetailsTypeDef",
    "GetMultiRegionAccessPointResultTypeDef",
    "ListMultiRegionAccessPointsResultTypeDef",
    "PrefixLevelTypeDef",
    "S3AccessControlListOutputTypeDef",
    "S3AccessControlListTypeDef",
    "S3CopyObjectOperationOutputTypeDef",
    "S3BucketDestinationOutputTypeDef",
    "StorageLensDataExportEncryptionUnionTypeDef",
    "StorageLensGroupLevelTypeDef",
    "ObjectLambdaConfigurationOutputTypeDef",
    "ObjectLambdaTransformationConfigurationUnionTypeDef",
    "LifecycleRuleOutputTypeDef",
    "LifecycleRuleFilterTypeDef",
    "ReplicationRuleFilterTypeDef",
    "S3JobManifestGeneratorOutputTypeDef",
    "S3ManifestOutputLocationTypeDef",
    "S3CopyObjectOperationTypeDef",
    "S3SetObjectRetentionOperationTypeDef",
    "ListJobsResultTypeDef",
    "JobManifestGeneratorFilterUnionTypeDef",
    "StorageLensGroupOutputTypeDef",
    "StorageLensGroupFilterTypeDef",
    "ReplicationRuleOutputTypeDef",
    "AsyncOperationTypeDef",
    "BucketLevelTypeDef",
    "S3AccessControlPolicyOutputTypeDef",
    "S3AccessControlListUnionTypeDef",
    "StorageLensDataExportOutputTypeDef",
    "S3BucketDestinationTypeDef",
    "StorageLensGroupLevelUnionTypeDef",
    "GetAccessPointConfigurationForObjectLambdaResultTypeDef",
    "ObjectLambdaConfigurationTypeDef",
    "GetBucketLifecycleConfigurationResultTypeDef",
    "LifecycleRuleFilterUnionTypeDef",
    "ReplicationRuleFilterUnionTypeDef",
    "JobManifestGeneratorOutputTypeDef",
    "S3ManifestOutputLocationUnionTypeDef",
    "S3CopyObjectOperationUnionTypeDef",
    "S3SetObjectRetentionOperationUnionTypeDef",
    "GetStorageLensGroupResultTypeDef",
    "StorageLensGroupFilterUnionTypeDef",
    "ReplicationConfigurationOutputTypeDef",
    "DescribeMultiRegionAccessPointOperationResultTypeDef",
    "AccountLevelOutputTypeDef",
    "S3SetObjectAclOperationOutputTypeDef",
    "S3AccessControlPolicyTypeDef",
    "S3BucketDestinationUnionTypeDef",
    "AccountLevelTypeDef",
    "CreateAccessPointForObjectLambdaRequestRequestTypeDef",
    "PutAccessPointConfigurationForObjectLambdaRequestRequestTypeDef",
    "LifecycleRuleTypeDef",
    "ReplicationRuleTypeDef",
    "S3JobManifestGeneratorTypeDef",
    "StorageLensGroupTypeDef",
    "GetBucketReplicationResultTypeDef",
    "StorageLensConfigurationOutputTypeDef",
    "JobOperationOutputTypeDef",
    "S3AccessControlPolicyUnionTypeDef",
    "StorageLensDataExportTypeDef",
    "AccountLevelUnionTypeDef",
    "LifecycleRuleUnionTypeDef",
    "ReplicationRuleUnionTypeDef",
    "S3JobManifestGeneratorUnionTypeDef",
    "CreateStorageLensGroupRequestRequestTypeDef",
    "UpdateStorageLensGroupRequestRequestTypeDef",
    "GetStorageLensConfigurationResultTypeDef",
    "JobDescriptorTypeDef",
    "S3SetObjectAclOperationTypeDef",
    "StorageLensDataExportUnionTypeDef",
    "LifecycleConfigurationTypeDef",
    "ReplicationConfigurationTypeDef",
    "JobManifestGeneratorTypeDef",
    "DescribeJobResultTypeDef",
    "S3SetObjectAclOperationUnionTypeDef",
    "StorageLensConfigurationTypeDef",
    "PutBucketLifecycleConfigurationRequestRequestTypeDef",
    "PutBucketReplicationRequestRequestTypeDef",
    "JobOperationTypeDef",
    "PutStorageLensConfigurationRequestRequestTypeDef",
    "CreateJobRequestRequestTypeDef",
)

AbortIncompleteMultipartUploadTypeDef = TypedDict(
    "AbortIncompleteMultipartUploadTypeDef",
    {
        "DaysAfterInitiation": NotRequired[int],
    },
)
AccessControlTranslationTypeDef = TypedDict(
    "AccessControlTranslationTypeDef",
    {
        "Owner": Literal["Destination"],
    },
)
AccessGrantsLocationConfigurationTypeDef = TypedDict(
    "AccessGrantsLocationConfigurationTypeDef",
    {
        "S3SubPrefix": NotRequired[str],
    },
)
VpcConfigurationTypeDef = TypedDict(
    "VpcConfigurationTypeDef",
    {
        "VpcId": str,
    },
)
ActivityMetricsTypeDef = TypedDict(
    "ActivityMetricsTypeDef",
    {
        "IsEnabled": NotRequired[bool],
    },
)
AdvancedCostOptimizationMetricsTypeDef = TypedDict(
    "AdvancedCostOptimizationMetricsTypeDef",
    {
        "IsEnabled": NotRequired[bool],
    },
)
AdvancedDataProtectionMetricsTypeDef = TypedDict(
    "AdvancedDataProtectionMetricsTypeDef",
    {
        "IsEnabled": NotRequired[bool],
    },
)
DetailedStatusCodesMetricsTypeDef = TypedDict(
    "DetailedStatusCodesMetricsTypeDef",
    {
        "IsEnabled": NotRequired[bool],
    },
)
AssociateAccessGrantsIdentityCenterRequestRequestTypeDef = TypedDict(
    "AssociateAccessGrantsIdentityCenterRequestRequestTypeDef",
    {
        "AccountId": str,
        "IdentityCenterArn": str,
    },
)
AsyncErrorDetailsTypeDef = TypedDict(
    "AsyncErrorDetailsTypeDef",
    {
        "Code": NotRequired[str],
        "Message": NotRequired[str],
        "Resource": NotRequired[str],
        "RequestId": NotRequired[str],
    },
)
DeleteMultiRegionAccessPointInputTypeDef = TypedDict(
    "DeleteMultiRegionAccessPointInputTypeDef",
    {
        "Name": str,
    },
)
PutMultiRegionAccessPointPolicyInputTypeDef = TypedDict(
    "PutMultiRegionAccessPointPolicyInputTypeDef",
    {
        "Name": str,
        "Policy": str,
    },
)
AwsLambdaTransformationTypeDef = TypedDict(
    "AwsLambdaTransformationTypeDef",
    {
        "FunctionArn": str,
        "FunctionPayload": NotRequired[str],
    },
)
CloudWatchMetricsTypeDef = TypedDict(
    "CloudWatchMetricsTypeDef",
    {
        "IsEnabled": bool,
    },
)
GranteeTypeDef = TypedDict(
    "GranteeTypeDef",
    {
        "GranteeType": NotRequired[GranteeTypeType],
        "GranteeIdentifier": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
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
ObjectLambdaAccessPointAliasTypeDef = TypedDict(
    "ObjectLambdaAccessPointAliasTypeDef",
    {
        "Value": NotRequired[str],
        "Status": NotRequired[ObjectLambdaAccessPointAliasStatusType],
    },
)
PublicAccessBlockConfigurationTypeDef = TypedDict(
    "PublicAccessBlockConfigurationTypeDef",
    {
        "BlockPublicAcls": NotRequired[bool],
        "IgnorePublicAcls": NotRequired[bool],
        "BlockPublicPolicy": NotRequired[bool],
        "RestrictPublicBuckets": NotRequired[bool],
    },
)
CreateBucketConfigurationTypeDef = TypedDict(
    "CreateBucketConfigurationTypeDef",
    {
        "LocationConstraint": NotRequired[BucketLocationConstraintType],
    },
)
JobReportTypeDef = TypedDict(
    "JobReportTypeDef",
    {
        "Enabled": bool,
        "Bucket": NotRequired[str],
        "Format": NotRequired[Literal["Report_CSV_20180820"]],
        "Prefix": NotRequired[str],
        "ReportScope": NotRequired[JobReportScopeType],
    },
)
S3TagTypeDef = TypedDict(
    "S3TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
RegionTypeDef = TypedDict(
    "RegionTypeDef",
    {
        "Bucket": str,
        "BucketAccountId": NotRequired[str],
    },
)
CredentialsTypeDef = TypedDict(
    "CredentialsTypeDef",
    {
        "AccessKeyId": NotRequired[str],
        "SecretAccessKey": NotRequired[str],
        "SessionToken": NotRequired[str],
        "Expiration": NotRequired[datetime],
    },
)
DeleteAccessGrantRequestRequestTypeDef = TypedDict(
    "DeleteAccessGrantRequestRequestTypeDef",
    {
        "AccountId": str,
        "AccessGrantId": str,
    },
)
DeleteAccessGrantsInstanceRequestRequestTypeDef = TypedDict(
    "DeleteAccessGrantsInstanceRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
DeleteAccessGrantsInstanceResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteAccessGrantsInstanceResourcePolicyRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
DeleteAccessGrantsLocationRequestRequestTypeDef = TypedDict(
    "DeleteAccessGrantsLocationRequestRequestTypeDef",
    {
        "AccountId": str,
        "AccessGrantsLocationId": str,
    },
)
DeleteAccessPointForObjectLambdaRequestRequestTypeDef = TypedDict(
    "DeleteAccessPointForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)
DeleteAccessPointPolicyForObjectLambdaRequestRequestTypeDef = TypedDict(
    "DeleteAccessPointPolicyForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)
DeleteAccessPointPolicyRequestRequestTypeDef = TypedDict(
    "DeleteAccessPointPolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)
DeleteAccessPointRequestRequestTypeDef = TypedDict(
    "DeleteAccessPointRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)
DeleteBucketLifecycleConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteBucketLifecycleConfigurationRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)
DeleteBucketPolicyRequestRequestTypeDef = TypedDict(
    "DeleteBucketPolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)
DeleteBucketReplicationRequestRequestTypeDef = TypedDict(
    "DeleteBucketReplicationRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)
DeleteBucketRequestRequestTypeDef = TypedDict(
    "DeleteBucketRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)
DeleteBucketTaggingRequestRequestTypeDef = TypedDict(
    "DeleteBucketTaggingRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)
DeleteJobTaggingRequestRequestTypeDef = TypedDict(
    "DeleteJobTaggingRequestRequestTypeDef",
    {
        "AccountId": str,
        "JobId": str,
    },
)
DeleteMarkerReplicationTypeDef = TypedDict(
    "DeleteMarkerReplicationTypeDef",
    {
        "Status": DeleteMarkerReplicationStatusType,
    },
)
DeletePublicAccessBlockRequestRequestTypeDef = TypedDict(
    "DeletePublicAccessBlockRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
DeleteStorageLensConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteStorageLensConfigurationRequestRequestTypeDef",
    {
        "ConfigId": str,
        "AccountId": str,
    },
)
DeleteStorageLensConfigurationTaggingRequestRequestTypeDef = TypedDict(
    "DeleteStorageLensConfigurationTaggingRequestRequestTypeDef",
    {
        "ConfigId": str,
        "AccountId": str,
    },
)
DeleteStorageLensGroupRequestRequestTypeDef = TypedDict(
    "DeleteStorageLensGroupRequestRequestTypeDef",
    {
        "Name": str,
        "AccountId": str,
    },
)
DescribeJobRequestRequestTypeDef = TypedDict(
    "DescribeJobRequestRequestTypeDef",
    {
        "AccountId": str,
        "JobId": str,
    },
)
DescribeMultiRegionAccessPointOperationRequestRequestTypeDef = TypedDict(
    "DescribeMultiRegionAccessPointOperationRequestRequestTypeDef",
    {
        "AccountId": str,
        "RequestTokenARN": str,
    },
)
EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "ReplicaKmsKeyID": NotRequired[str],
    },
)
DissociateAccessGrantsIdentityCenterRequestRequestTypeDef = TypedDict(
    "DissociateAccessGrantsIdentityCenterRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
EstablishedMultiRegionAccessPointPolicyTypeDef = TypedDict(
    "EstablishedMultiRegionAccessPointPolicyTypeDef",
    {
        "Policy": NotRequired[str],
    },
)
ExcludeOutputTypeDef = TypedDict(
    "ExcludeOutputTypeDef",
    {
        "Buckets": NotRequired[List[str]],
        "Regions": NotRequired[List[str]],
    },
)
ExcludeTypeDef = TypedDict(
    "ExcludeTypeDef",
    {
        "Buckets": NotRequired[Sequence[str]],
        "Regions": NotRequired[Sequence[str]],
    },
)
ExistingObjectReplicationTypeDef = TypedDict(
    "ExistingObjectReplicationTypeDef",
    {
        "Status": ExistingObjectReplicationStatusType,
    },
)
SSEKMSEncryptionTypeDef = TypedDict(
    "SSEKMSEncryptionTypeDef",
    {
        "KeyId": str,
    },
)
GetAccessGrantRequestRequestTypeDef = TypedDict(
    "GetAccessGrantRequestRequestTypeDef",
    {
        "AccountId": str,
        "AccessGrantId": str,
    },
)
GetAccessGrantsInstanceForPrefixRequestRequestTypeDef = TypedDict(
    "GetAccessGrantsInstanceForPrefixRequestRequestTypeDef",
    {
        "AccountId": str,
        "S3Prefix": str,
    },
)
GetAccessGrantsInstanceRequestRequestTypeDef = TypedDict(
    "GetAccessGrantsInstanceRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
GetAccessGrantsInstanceResourcePolicyRequestRequestTypeDef = TypedDict(
    "GetAccessGrantsInstanceResourcePolicyRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
GetAccessGrantsLocationRequestRequestTypeDef = TypedDict(
    "GetAccessGrantsLocationRequestRequestTypeDef",
    {
        "AccountId": str,
        "AccessGrantsLocationId": str,
    },
)
GetAccessPointConfigurationForObjectLambdaRequestRequestTypeDef = TypedDict(
    "GetAccessPointConfigurationForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)
GetAccessPointForObjectLambdaRequestRequestTypeDef = TypedDict(
    "GetAccessPointForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)
GetAccessPointPolicyForObjectLambdaRequestRequestTypeDef = TypedDict(
    "GetAccessPointPolicyForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)
GetAccessPointPolicyRequestRequestTypeDef = TypedDict(
    "GetAccessPointPolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)
GetAccessPointPolicyStatusForObjectLambdaRequestRequestTypeDef = TypedDict(
    "GetAccessPointPolicyStatusForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)
PolicyStatusTypeDef = TypedDict(
    "PolicyStatusTypeDef",
    {
        "IsPublic": NotRequired[bool],
    },
)
GetAccessPointPolicyStatusRequestRequestTypeDef = TypedDict(
    "GetAccessPointPolicyStatusRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)
GetAccessPointRequestRequestTypeDef = TypedDict(
    "GetAccessPointRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)
GetBucketLifecycleConfigurationRequestRequestTypeDef = TypedDict(
    "GetBucketLifecycleConfigurationRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)
GetBucketPolicyRequestRequestTypeDef = TypedDict(
    "GetBucketPolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)
GetBucketReplicationRequestRequestTypeDef = TypedDict(
    "GetBucketReplicationRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)
GetBucketRequestRequestTypeDef = TypedDict(
    "GetBucketRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)
GetBucketTaggingRequestRequestTypeDef = TypedDict(
    "GetBucketTaggingRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)
GetBucketVersioningRequestRequestTypeDef = TypedDict(
    "GetBucketVersioningRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
    },
)
GetDataAccessRequestRequestTypeDef = TypedDict(
    "GetDataAccessRequestRequestTypeDef",
    {
        "AccountId": str,
        "Target": str,
        "Permission": PermissionType,
        "DurationSeconds": NotRequired[int],
        "Privilege": NotRequired[PrivilegeType],
        "TargetType": NotRequired[Literal["Object"]],
    },
)
GetJobTaggingRequestRequestTypeDef = TypedDict(
    "GetJobTaggingRequestRequestTypeDef",
    {
        "AccountId": str,
        "JobId": str,
    },
)
GetMultiRegionAccessPointPolicyRequestRequestTypeDef = TypedDict(
    "GetMultiRegionAccessPointPolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)
GetMultiRegionAccessPointPolicyStatusRequestRequestTypeDef = TypedDict(
    "GetMultiRegionAccessPointPolicyStatusRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)
GetMultiRegionAccessPointRequestRequestTypeDef = TypedDict(
    "GetMultiRegionAccessPointRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
    },
)
GetMultiRegionAccessPointRoutesRequestRequestTypeDef = TypedDict(
    "GetMultiRegionAccessPointRoutesRequestRequestTypeDef",
    {
        "AccountId": str,
        "Mrap": str,
    },
)
MultiRegionAccessPointRouteTypeDef = TypedDict(
    "MultiRegionAccessPointRouteTypeDef",
    {
        "TrafficDialPercentage": int,
        "Bucket": NotRequired[str],
        "Region": NotRequired[str],
    },
)
GetPublicAccessBlockRequestRequestTypeDef = TypedDict(
    "GetPublicAccessBlockRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)
GetStorageLensConfigurationRequestRequestTypeDef = TypedDict(
    "GetStorageLensConfigurationRequestRequestTypeDef",
    {
        "ConfigId": str,
        "AccountId": str,
    },
)
GetStorageLensConfigurationTaggingRequestRequestTypeDef = TypedDict(
    "GetStorageLensConfigurationTaggingRequestRequestTypeDef",
    {
        "ConfigId": str,
        "AccountId": str,
    },
)
StorageLensTagTypeDef = TypedDict(
    "StorageLensTagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
GetStorageLensGroupRequestRequestTypeDef = TypedDict(
    "GetStorageLensGroupRequestRequestTypeDef",
    {
        "Name": str,
        "AccountId": str,
    },
)
IncludeOutputTypeDef = TypedDict(
    "IncludeOutputTypeDef",
    {
        "Buckets": NotRequired[List[str]],
        "Regions": NotRequired[List[str]],
    },
)
IncludeTypeDef = TypedDict(
    "IncludeTypeDef",
    {
        "Buckets": NotRequired[Sequence[str]],
        "Regions": NotRequired[Sequence[str]],
    },
)
JobFailureTypeDef = TypedDict(
    "JobFailureTypeDef",
    {
        "FailureCode": NotRequired[str],
        "FailureReason": NotRequired[str],
    },
)
KeyNameConstraintOutputTypeDef = TypedDict(
    "KeyNameConstraintOutputTypeDef",
    {
        "MatchAnyPrefix": NotRequired[List[str]],
        "MatchAnySuffix": NotRequired[List[str]],
        "MatchAnySubstring": NotRequired[List[str]],
    },
)
TimestampTypeDef = Union[datetime, str]
JobManifestLocationTypeDef = TypedDict(
    "JobManifestLocationTypeDef",
    {
        "ObjectArn": str,
        "ETag": str,
        "ObjectVersionId": NotRequired[str],
    },
)
JobManifestSpecOutputTypeDef = TypedDict(
    "JobManifestSpecOutputTypeDef",
    {
        "Format": JobManifestFormatType,
        "Fields": NotRequired[List[JobManifestFieldNameType]],
    },
)
JobManifestSpecTypeDef = TypedDict(
    "JobManifestSpecTypeDef",
    {
        "Format": JobManifestFormatType,
        "Fields": NotRequired[Sequence[JobManifestFieldNameType]],
    },
)
LambdaInvokeOperationOutputTypeDef = TypedDict(
    "LambdaInvokeOperationOutputTypeDef",
    {
        "FunctionArn": NotRequired[str],
        "InvocationSchemaVersion": NotRequired[str],
        "UserArguments": NotRequired[Dict[str, str]],
    },
)
S3InitiateRestoreObjectOperationTypeDef = TypedDict(
    "S3InitiateRestoreObjectOperationTypeDef",
    {
        "ExpirationInDays": NotRequired[int],
        "GlacierJobTier": NotRequired[S3GlacierJobTierType],
    },
)
JobTimersTypeDef = TypedDict(
    "JobTimersTypeDef",
    {
        "ElapsedTimeInActiveSeconds": NotRequired[int],
    },
)
KeyNameConstraintTypeDef = TypedDict(
    "KeyNameConstraintTypeDef",
    {
        "MatchAnyPrefix": NotRequired[Sequence[str]],
        "MatchAnySuffix": NotRequired[Sequence[str]],
        "MatchAnySubstring": NotRequired[Sequence[str]],
    },
)
LambdaInvokeOperationTypeDef = TypedDict(
    "LambdaInvokeOperationTypeDef",
    {
        "FunctionArn": NotRequired[str],
        "InvocationSchemaVersion": NotRequired[str],
        "UserArguments": NotRequired[Mapping[str, str]],
    },
)
LifecycleExpirationOutputTypeDef = TypedDict(
    "LifecycleExpirationOutputTypeDef",
    {
        "Date": NotRequired[datetime],
        "Days": NotRequired[int],
        "ExpiredObjectDeleteMarker": NotRequired[bool],
    },
)
NoncurrentVersionExpirationTypeDef = TypedDict(
    "NoncurrentVersionExpirationTypeDef",
    {
        "NoncurrentDays": NotRequired[int],
        "NewerNoncurrentVersions": NotRequired[int],
    },
)
NoncurrentVersionTransitionTypeDef = TypedDict(
    "NoncurrentVersionTransitionTypeDef",
    {
        "NoncurrentDays": NotRequired[int],
        "StorageClass": NotRequired[TransitionStorageClassType],
    },
)
TransitionOutputTypeDef = TypedDict(
    "TransitionOutputTypeDef",
    {
        "Date": NotRequired[datetime],
        "Days": NotRequired[int],
        "StorageClass": NotRequired[TransitionStorageClassType],
    },
)
ListAccessGrantsInstanceEntryTypeDef = TypedDict(
    "ListAccessGrantsInstanceEntryTypeDef",
    {
        "AccessGrantsInstanceId": NotRequired[str],
        "AccessGrantsInstanceArn": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "IdentityCenterArn": NotRequired[str],
        "IdentityCenterInstanceArn": NotRequired[str],
        "IdentityCenterApplicationArn": NotRequired[str],
    },
)
ListAccessGrantsInstancesRequestRequestTypeDef = TypedDict(
    "ListAccessGrantsInstancesRequestRequestTypeDef",
    {
        "AccountId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListAccessGrantsLocationsEntryTypeDef = TypedDict(
    "ListAccessGrantsLocationsEntryTypeDef",
    {
        "CreatedAt": NotRequired[datetime],
        "AccessGrantsLocationId": NotRequired[str],
        "AccessGrantsLocationArn": NotRequired[str],
        "LocationScope": NotRequired[str],
        "IAMRoleArn": NotRequired[str],
    },
)
ListAccessGrantsLocationsRequestRequestTypeDef = TypedDict(
    "ListAccessGrantsLocationsRequestRequestTypeDef",
    {
        "AccountId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "LocationScope": NotRequired[str],
    },
)
ListAccessGrantsRequestRequestTypeDef = TypedDict(
    "ListAccessGrantsRequestRequestTypeDef",
    {
        "AccountId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "GranteeType": NotRequired[GranteeTypeType],
        "GranteeIdentifier": NotRequired[str],
        "Permission": NotRequired[PermissionType],
        "GrantScope": NotRequired[str],
        "ApplicationArn": NotRequired[str],
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
ListAccessPointsForObjectLambdaRequestRequestTypeDef = TypedDict(
    "ListAccessPointsForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListAccessPointsRequestRequestTypeDef = TypedDict(
    "ListAccessPointsRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListCallerAccessGrantsEntryTypeDef = TypedDict(
    "ListCallerAccessGrantsEntryTypeDef",
    {
        "Permission": NotRequired[PermissionType],
        "GrantScope": NotRequired[str],
        "ApplicationArn": NotRequired[str],
    },
)
ListCallerAccessGrantsRequestRequestTypeDef = TypedDict(
    "ListCallerAccessGrantsRequestRequestTypeDef",
    {
        "AccountId": str,
        "GrantScope": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "AllowedByApplication": NotRequired[bool],
    },
)
ListJobsRequestRequestTypeDef = TypedDict(
    "ListJobsRequestRequestTypeDef",
    {
        "AccountId": str,
        "JobStatuses": NotRequired[Sequence[JobStatusType]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListMultiRegionAccessPointsRequestRequestTypeDef = TypedDict(
    "ListMultiRegionAccessPointsRequestRequestTypeDef",
    {
        "AccountId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListRegionalBucketsRequestRequestTypeDef = TypedDict(
    "ListRegionalBucketsRequestRequestTypeDef",
    {
        "AccountId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "OutpostId": NotRequired[str],
    },
)
RegionalBucketTypeDef = TypedDict(
    "RegionalBucketTypeDef",
    {
        "Bucket": str,
        "PublicAccessBlockEnabled": bool,
        "CreationDate": datetime,
        "BucketArn": NotRequired[str],
        "OutpostId": NotRequired[str],
    },
)
ListStorageLensConfigurationEntryTypeDef = TypedDict(
    "ListStorageLensConfigurationEntryTypeDef",
    {
        "Id": str,
        "StorageLensArn": str,
        "HomeRegion": str,
        "IsEnabled": NotRequired[bool],
    },
)
ListStorageLensConfigurationsRequestRequestTypeDef = TypedDict(
    "ListStorageLensConfigurationsRequestRequestTypeDef",
    {
        "AccountId": str,
        "NextToken": NotRequired[str],
    },
)
ListStorageLensGroupEntryTypeDef = TypedDict(
    "ListStorageLensGroupEntryTypeDef",
    {
        "Name": str,
        "StorageLensGroupArn": str,
        "HomeRegion": str,
    },
)
ListStorageLensGroupsRequestRequestTypeDef = TypedDict(
    "ListStorageLensGroupsRequestRequestTypeDef",
    {
        "AccountId": str,
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "AccountId": str,
        "ResourceArn": str,
    },
)
MatchObjectAgeTypeDef = TypedDict(
    "MatchObjectAgeTypeDef",
    {
        "DaysGreaterThan": NotRequired[int],
        "DaysLessThan": NotRequired[int],
    },
)
MatchObjectSizeTypeDef = TypedDict(
    "MatchObjectSizeTypeDef",
    {
        "BytesGreaterThan": NotRequired[int],
        "BytesLessThan": NotRequired[int],
    },
)
ReplicationTimeValueTypeDef = TypedDict(
    "ReplicationTimeValueTypeDef",
    {
        "Minutes": NotRequired[int],
    },
)
ProposedMultiRegionAccessPointPolicyTypeDef = TypedDict(
    "ProposedMultiRegionAccessPointPolicyTypeDef",
    {
        "Policy": NotRequired[str],
    },
)
MultiRegionAccessPointRegionalResponseTypeDef = TypedDict(
    "MultiRegionAccessPointRegionalResponseTypeDef",
    {
        "Name": NotRequired[str],
        "RequestStatus": NotRequired[str],
    },
)
RegionReportTypeDef = TypedDict(
    "RegionReportTypeDef",
    {
        "Bucket": NotRequired[str],
        "Region": NotRequired[str],
        "BucketAccountId": NotRequired[str],
    },
)
SelectionCriteriaTypeDef = TypedDict(
    "SelectionCriteriaTypeDef",
    {
        "Delimiter": NotRequired[str],
        "MaxDepth": NotRequired[int],
        "MinStorageBytesPercentage": NotRequired[float],
    },
)
PutAccessGrantsInstanceResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutAccessGrantsInstanceResourcePolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "Policy": str,
        "Organization": NotRequired[str],
    },
)
PutAccessPointPolicyForObjectLambdaRequestRequestTypeDef = TypedDict(
    "PutAccessPointPolicyForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
        "Policy": str,
    },
)
PutAccessPointPolicyRequestRequestTypeDef = TypedDict(
    "PutAccessPointPolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
        "Policy": str,
    },
)
PutBucketPolicyRequestRequestTypeDef = TypedDict(
    "PutBucketPolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
        "Policy": str,
        "ConfirmRemoveSelfBucketAccess": NotRequired[bool],
    },
)
VersioningConfigurationTypeDef = TypedDict(
    "VersioningConfigurationTypeDef",
    {
        "MFADelete": NotRequired[MFADeleteType],
        "Status": NotRequired[BucketVersioningStatusType],
    },
)
ReplicaModificationsTypeDef = TypedDict(
    "ReplicaModificationsTypeDef",
    {
        "Status": ReplicaModificationsStatusType,
    },
)
S3ObjectOwnerTypeDef = TypedDict(
    "S3ObjectOwnerTypeDef",
    {
        "ID": NotRequired[str],
        "DisplayName": NotRequired[str],
    },
)
S3ObjectMetadataOutputTypeDef = TypedDict(
    "S3ObjectMetadataOutputTypeDef",
    {
        "CacheControl": NotRequired[str],
        "ContentDisposition": NotRequired[str],
        "ContentEncoding": NotRequired[str],
        "ContentLanguage": NotRequired[str],
        "UserMetadata": NotRequired[Dict[str, str]],
        "ContentLength": NotRequired[int],
        "ContentMD5": NotRequired[str],
        "ContentType": NotRequired[str],
        "HttpExpiresDate": NotRequired[datetime],
        "RequesterCharged": NotRequired[bool],
        "SSEAlgorithm": NotRequired[S3SSEAlgorithmType],
    },
)
S3GranteeTypeDef = TypedDict(
    "S3GranteeTypeDef",
    {
        "TypeIdentifier": NotRequired[S3GranteeTypeIdentifierType],
        "Identifier": NotRequired[str],
        "DisplayName": NotRequired[str],
    },
)
S3ObjectLockLegalHoldTypeDef = TypedDict(
    "S3ObjectLockLegalHoldTypeDef",
    {
        "Status": S3ObjectLockLegalHoldStatusType,
    },
)
S3RetentionOutputTypeDef = TypedDict(
    "S3RetentionOutputTypeDef",
    {
        "RetainUntilDate": NotRequired[datetime],
        "Mode": NotRequired[S3ObjectLockRetentionModeType],
    },
)
SSEKMSTypeDef = TypedDict(
    "SSEKMSTypeDef",
    {
        "KeyId": str,
    },
)
SseKmsEncryptedObjectsTypeDef = TypedDict(
    "SseKmsEncryptedObjectsTypeDef",
    {
        "Status": SseKmsEncryptedObjectsStatusType,
    },
)
StorageLensAwsOrgTypeDef = TypedDict(
    "StorageLensAwsOrgTypeDef",
    {
        "Arn": str,
    },
)
StorageLensGroupLevelSelectionCriteriaOutputTypeDef = TypedDict(
    "StorageLensGroupLevelSelectionCriteriaOutputTypeDef",
    {
        "Include": NotRequired[List[str]],
        "Exclude": NotRequired[List[str]],
    },
)
StorageLensGroupLevelSelectionCriteriaTypeDef = TypedDict(
    "StorageLensGroupLevelSelectionCriteriaTypeDef",
    {
        "Include": NotRequired[Sequence[str]],
        "Exclude": NotRequired[Sequence[str]],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "AccountId": str,
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateAccessGrantsLocationRequestRequestTypeDef = TypedDict(
    "UpdateAccessGrantsLocationRequestRequestTypeDef",
    {
        "AccountId": str,
        "AccessGrantsLocationId": str,
        "IAMRoleArn": str,
    },
)
UpdateJobPriorityRequestRequestTypeDef = TypedDict(
    "UpdateJobPriorityRequestRequestTypeDef",
    {
        "AccountId": str,
        "JobId": str,
        "Priority": int,
    },
)
UpdateJobStatusRequestRequestTypeDef = TypedDict(
    "UpdateJobStatusRequestRequestTypeDef",
    {
        "AccountId": str,
        "JobId": str,
        "RequestedJobStatus": RequestedJobStatusType,
        "StatusUpdateReason": NotRequired[str],
    },
)
AccessPointTypeDef = TypedDict(
    "AccessPointTypeDef",
    {
        "Name": str,
        "NetworkOrigin": NetworkOriginType,
        "Bucket": str,
        "VpcConfiguration": NotRequired[VpcConfigurationTypeDef],
        "AccessPointArn": NotRequired[str],
        "Alias": NotRequired[str],
        "BucketAccountId": NotRequired[str],
    },
)
DeleteMultiRegionAccessPointRequestRequestTypeDef = TypedDict(
    "DeleteMultiRegionAccessPointRequestRequestTypeDef",
    {
        "AccountId": str,
        "ClientToken": str,
        "Details": DeleteMultiRegionAccessPointInputTypeDef,
    },
)
PutMultiRegionAccessPointPolicyRequestRequestTypeDef = TypedDict(
    "PutMultiRegionAccessPointPolicyRequestRequestTypeDef",
    {
        "AccountId": str,
        "ClientToken": str,
        "Details": PutMultiRegionAccessPointPolicyInputTypeDef,
    },
)
ObjectLambdaContentTransformationTypeDef = TypedDict(
    "ObjectLambdaContentTransformationTypeDef",
    {
        "AwsLambda": NotRequired[AwsLambdaTransformationTypeDef],
    },
)
ListAccessGrantEntryTypeDef = TypedDict(
    "ListAccessGrantEntryTypeDef",
    {
        "CreatedAt": NotRequired[datetime],
        "AccessGrantId": NotRequired[str],
        "AccessGrantArn": NotRequired[str],
        "Grantee": NotRequired[GranteeTypeDef],
        "Permission": NotRequired[PermissionType],
        "AccessGrantsLocationId": NotRequired[str],
        "AccessGrantsLocationConfiguration": NotRequired[AccessGrantsLocationConfigurationTypeDef],
        "GrantScope": NotRequired[str],
        "ApplicationArn": NotRequired[str],
    },
)
CreateAccessGrantRequestRequestTypeDef = TypedDict(
    "CreateAccessGrantRequestRequestTypeDef",
    {
        "AccountId": str,
        "AccessGrantsLocationId": str,
        "Grantee": GranteeTypeDef,
        "Permission": PermissionType,
        "AccessGrantsLocationConfiguration": NotRequired[AccessGrantsLocationConfigurationTypeDef],
        "ApplicationArn": NotRequired[str],
        "S3PrefixType": NotRequired[Literal["Object"]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateAccessGrantsInstanceRequestRequestTypeDef = TypedDict(
    "CreateAccessGrantsInstanceRequestRequestTypeDef",
    {
        "AccountId": str,
        "IdentityCenterArn": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateAccessGrantsLocationRequestRequestTypeDef = TypedDict(
    "CreateAccessGrantsLocationRequestRequestTypeDef",
    {
        "AccountId": str,
        "LocationScope": str,
        "IAMRoleArn": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "AccountId": str,
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CreateAccessGrantResultTypeDef = TypedDict(
    "CreateAccessGrantResultTypeDef",
    {
        "CreatedAt": datetime,
        "AccessGrantId": str,
        "AccessGrantArn": str,
        "Grantee": GranteeTypeDef,
        "AccessGrantsLocationId": str,
        "AccessGrantsLocationConfiguration": AccessGrantsLocationConfigurationTypeDef,
        "Permission": PermissionType,
        "ApplicationArn": str,
        "GrantScope": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAccessGrantsInstanceResultTypeDef = TypedDict(
    "CreateAccessGrantsInstanceResultTypeDef",
    {
        "CreatedAt": datetime,
        "AccessGrantsInstanceId": str,
        "AccessGrantsInstanceArn": str,
        "IdentityCenterArn": str,
        "IdentityCenterInstanceArn": str,
        "IdentityCenterApplicationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAccessGrantsLocationResultTypeDef = TypedDict(
    "CreateAccessGrantsLocationResultTypeDef",
    {
        "CreatedAt": datetime,
        "AccessGrantsLocationId": str,
        "AccessGrantsLocationArn": str,
        "LocationScope": str,
        "IAMRoleArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAccessPointResultTypeDef = TypedDict(
    "CreateAccessPointResultTypeDef",
    {
        "AccessPointArn": str,
        "Alias": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateBucketResultTypeDef = TypedDict(
    "CreateBucketResultTypeDef",
    {
        "Location": str,
        "BucketArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateJobResultTypeDef = TypedDict(
    "CreateJobResultTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMultiRegionAccessPointResultTypeDef = TypedDict(
    "CreateMultiRegionAccessPointResultTypeDef",
    {
        "RequestTokenARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteMultiRegionAccessPointResultTypeDef = TypedDict(
    "DeleteMultiRegionAccessPointResultTypeDef",
    {
        "RequestTokenARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAccessGrantResultTypeDef = TypedDict(
    "GetAccessGrantResultTypeDef",
    {
        "CreatedAt": datetime,
        "AccessGrantId": str,
        "AccessGrantArn": str,
        "Grantee": GranteeTypeDef,
        "Permission": PermissionType,
        "AccessGrantsLocationId": str,
        "AccessGrantsLocationConfiguration": AccessGrantsLocationConfigurationTypeDef,
        "GrantScope": str,
        "ApplicationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAccessGrantsInstanceForPrefixResultTypeDef = TypedDict(
    "GetAccessGrantsInstanceForPrefixResultTypeDef",
    {
        "AccessGrantsInstanceArn": str,
        "AccessGrantsInstanceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAccessGrantsInstanceResourcePolicyResultTypeDef = TypedDict(
    "GetAccessGrantsInstanceResourcePolicyResultTypeDef",
    {
        "Policy": str,
        "Organization": str,
        "CreatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAccessGrantsInstanceResultTypeDef = TypedDict(
    "GetAccessGrantsInstanceResultTypeDef",
    {
        "AccessGrantsInstanceArn": str,
        "AccessGrantsInstanceId": str,
        "IdentityCenterArn": str,
        "IdentityCenterInstanceArn": str,
        "IdentityCenterApplicationArn": str,
        "CreatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAccessGrantsLocationResultTypeDef = TypedDict(
    "GetAccessGrantsLocationResultTypeDef",
    {
        "CreatedAt": datetime,
        "AccessGrantsLocationId": str,
        "AccessGrantsLocationArn": str,
        "LocationScope": str,
        "IAMRoleArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAccessPointPolicyForObjectLambdaResultTypeDef = TypedDict(
    "GetAccessPointPolicyForObjectLambdaResultTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAccessPointPolicyResultTypeDef = TypedDict(
    "GetAccessPointPolicyResultTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBucketPolicyResultTypeDef = TypedDict(
    "GetBucketPolicyResultTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBucketResultTypeDef = TypedDict(
    "GetBucketResultTypeDef",
    {
        "Bucket": str,
        "PublicAccessBlockEnabled": bool,
        "CreationDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBucketVersioningResultTypeDef = TypedDict(
    "GetBucketVersioningResultTypeDef",
    {
        "Status": BucketVersioningStatusType,
        "MFADelete": MFADeleteStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutAccessGrantsInstanceResourcePolicyResultTypeDef = TypedDict(
    "PutAccessGrantsInstanceResourcePolicyResultTypeDef",
    {
        "Policy": str,
        "Organization": str,
        "CreatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutMultiRegionAccessPointPolicyResultTypeDef = TypedDict(
    "PutMultiRegionAccessPointPolicyResultTypeDef",
    {
        "RequestTokenARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAccessGrantsLocationResultTypeDef = TypedDict(
    "UpdateAccessGrantsLocationResultTypeDef",
    {
        "CreatedAt": datetime,
        "AccessGrantsLocationId": str,
        "AccessGrantsLocationArn": str,
        "LocationScope": str,
        "IAMRoleArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateJobPriorityResultTypeDef = TypedDict(
    "UpdateJobPriorityResultTypeDef",
    {
        "JobId": str,
        "Priority": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateJobStatusResultTypeDef = TypedDict(
    "UpdateJobStatusResultTypeDef",
    {
        "JobId": str,
        "Status": JobStatusType,
        "StatusUpdateReason": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAccessPointForObjectLambdaResultTypeDef = TypedDict(
    "CreateAccessPointForObjectLambdaResultTypeDef",
    {
        "ObjectLambdaAccessPointArn": str,
        "Alias": ObjectLambdaAccessPointAliasTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ObjectLambdaAccessPointTypeDef = TypedDict(
    "ObjectLambdaAccessPointTypeDef",
    {
        "Name": str,
        "ObjectLambdaAccessPointArn": NotRequired[str],
        "Alias": NotRequired[ObjectLambdaAccessPointAliasTypeDef],
    },
)
CreateAccessPointRequestRequestTypeDef = TypedDict(
    "CreateAccessPointRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
        "Bucket": str,
        "VpcConfiguration": NotRequired[VpcConfigurationTypeDef],
        "PublicAccessBlockConfiguration": NotRequired[PublicAccessBlockConfigurationTypeDef],
        "BucketAccountId": NotRequired[str],
    },
)
GetAccessPointForObjectLambdaResultTypeDef = TypedDict(
    "GetAccessPointForObjectLambdaResultTypeDef",
    {
        "Name": str,
        "PublicAccessBlockConfiguration": PublicAccessBlockConfigurationTypeDef,
        "CreationDate": datetime,
        "Alias": ObjectLambdaAccessPointAliasTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAccessPointResultTypeDef = TypedDict(
    "GetAccessPointResultTypeDef",
    {
        "Name": str,
        "Bucket": str,
        "NetworkOrigin": NetworkOriginType,
        "VpcConfiguration": VpcConfigurationTypeDef,
        "PublicAccessBlockConfiguration": PublicAccessBlockConfigurationTypeDef,
        "CreationDate": datetime,
        "Alias": str,
        "AccessPointArn": str,
        "Endpoints": Dict[str, str],
        "BucketAccountId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPublicAccessBlockOutputTypeDef = TypedDict(
    "GetPublicAccessBlockOutputTypeDef",
    {
        "PublicAccessBlockConfiguration": PublicAccessBlockConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutPublicAccessBlockRequestRequestTypeDef = TypedDict(
    "PutPublicAccessBlockRequestRequestTypeDef",
    {
        "PublicAccessBlockConfiguration": PublicAccessBlockConfigurationTypeDef,
        "AccountId": str,
    },
)
CreateBucketRequestRequestTypeDef = TypedDict(
    "CreateBucketRequestRequestTypeDef",
    {
        "Bucket": str,
        "ACL": NotRequired[BucketCannedACLType],
        "CreateBucketConfiguration": NotRequired[CreateBucketConfigurationTypeDef],
        "GrantFullControl": NotRequired[str],
        "GrantRead": NotRequired[str],
        "GrantReadACP": NotRequired[str],
        "GrantWrite": NotRequired[str],
        "GrantWriteACP": NotRequired[str],
        "ObjectLockEnabledForBucket": NotRequired[bool],
        "OutpostId": NotRequired[str],
    },
)
GetBucketTaggingResultTypeDef = TypedDict(
    "GetBucketTaggingResultTypeDef",
    {
        "TagSet": List[S3TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetJobTaggingResultTypeDef = TypedDict(
    "GetJobTaggingResultTypeDef",
    {
        "Tags": List[S3TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LifecycleRuleAndOperatorOutputTypeDef = TypedDict(
    "LifecycleRuleAndOperatorOutputTypeDef",
    {
        "Prefix": NotRequired[str],
        "Tags": NotRequired[List[S3TagTypeDef]],
        "ObjectSizeGreaterThan": NotRequired[int],
        "ObjectSizeLessThan": NotRequired[int],
    },
)
LifecycleRuleAndOperatorTypeDef = TypedDict(
    "LifecycleRuleAndOperatorTypeDef",
    {
        "Prefix": NotRequired[str],
        "Tags": NotRequired[Sequence[S3TagTypeDef]],
        "ObjectSizeGreaterThan": NotRequired[int],
        "ObjectSizeLessThan": NotRequired[int],
    },
)
PutJobTaggingRequestRequestTypeDef = TypedDict(
    "PutJobTaggingRequestRequestTypeDef",
    {
        "AccountId": str,
        "JobId": str,
        "Tags": Sequence[S3TagTypeDef],
    },
)
ReplicationRuleAndOperatorOutputTypeDef = TypedDict(
    "ReplicationRuleAndOperatorOutputTypeDef",
    {
        "Prefix": NotRequired[str],
        "Tags": NotRequired[List[S3TagTypeDef]],
    },
)
ReplicationRuleAndOperatorTypeDef = TypedDict(
    "ReplicationRuleAndOperatorTypeDef",
    {
        "Prefix": NotRequired[str],
        "Tags": NotRequired[Sequence[S3TagTypeDef]],
    },
)
S3SetObjectTaggingOperationOutputTypeDef = TypedDict(
    "S3SetObjectTaggingOperationOutputTypeDef",
    {
        "TagSet": NotRequired[List[S3TagTypeDef]],
    },
)
S3SetObjectTaggingOperationTypeDef = TypedDict(
    "S3SetObjectTaggingOperationTypeDef",
    {
        "TagSet": NotRequired[Sequence[S3TagTypeDef]],
    },
)
TaggingTypeDef = TypedDict(
    "TaggingTypeDef",
    {
        "TagSet": Sequence[S3TagTypeDef],
    },
)
CreateMultiRegionAccessPointInputOutputTypeDef = TypedDict(
    "CreateMultiRegionAccessPointInputOutputTypeDef",
    {
        "Name": str,
        "Regions": List[RegionTypeDef],
        "PublicAccessBlock": NotRequired[PublicAccessBlockConfigurationTypeDef],
    },
)
CreateMultiRegionAccessPointInputTypeDef = TypedDict(
    "CreateMultiRegionAccessPointInputTypeDef",
    {
        "Name": str,
        "Regions": Sequence[RegionTypeDef],
        "PublicAccessBlock": NotRequired[PublicAccessBlockConfigurationTypeDef],
    },
)
GetDataAccessResultTypeDef = TypedDict(
    "GetDataAccessResultTypeDef",
    {
        "Credentials": CredentialsTypeDef,
        "MatchedGrantTarget": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExcludeUnionTypeDef = Union[ExcludeTypeDef, ExcludeOutputTypeDef]
GeneratedManifestEncryptionOutputTypeDef = TypedDict(
    "GeneratedManifestEncryptionOutputTypeDef",
    {
        "SSES3": NotRequired[Dict[str, Any]],
        "SSEKMS": NotRequired[SSEKMSEncryptionTypeDef],
    },
)
GeneratedManifestEncryptionTypeDef = TypedDict(
    "GeneratedManifestEncryptionTypeDef",
    {
        "SSES3": NotRequired[Mapping[str, Any]],
        "SSEKMS": NotRequired[SSEKMSEncryptionTypeDef],
    },
)
GetAccessPointPolicyStatusForObjectLambdaResultTypeDef = TypedDict(
    "GetAccessPointPolicyStatusForObjectLambdaResultTypeDef",
    {
        "PolicyStatus": PolicyStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAccessPointPolicyStatusResultTypeDef = TypedDict(
    "GetAccessPointPolicyStatusResultTypeDef",
    {
        "PolicyStatus": PolicyStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMultiRegionAccessPointPolicyStatusResultTypeDef = TypedDict(
    "GetMultiRegionAccessPointPolicyStatusResultTypeDef",
    {
        "Established": PolicyStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMultiRegionAccessPointRoutesResultTypeDef = TypedDict(
    "GetMultiRegionAccessPointRoutesResultTypeDef",
    {
        "Mrap": str,
        "Routes": List[MultiRegionAccessPointRouteTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SubmitMultiRegionAccessPointRoutesRequestRequestTypeDef = TypedDict(
    "SubmitMultiRegionAccessPointRoutesRequestRequestTypeDef",
    {
        "AccountId": str,
        "Mrap": str,
        "RouteUpdates": Sequence[MultiRegionAccessPointRouteTypeDef],
    },
)
GetStorageLensConfigurationTaggingResultTypeDef = TypedDict(
    "GetStorageLensConfigurationTaggingResultTypeDef",
    {
        "Tags": List[StorageLensTagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutStorageLensConfigurationTaggingRequestRequestTypeDef = TypedDict(
    "PutStorageLensConfigurationTaggingRequestRequestTypeDef",
    {
        "ConfigId": str,
        "AccountId": str,
        "Tags": Sequence[StorageLensTagTypeDef],
    },
)
IncludeUnionTypeDef = Union[IncludeTypeDef, IncludeOutputTypeDef]
JobManifestGeneratorFilterOutputTypeDef = TypedDict(
    "JobManifestGeneratorFilterOutputTypeDef",
    {
        "EligibleForReplication": NotRequired[bool],
        "CreatedAfter": NotRequired[datetime],
        "CreatedBefore": NotRequired[datetime],
        "ObjectReplicationStatuses": NotRequired[List[ReplicationStatusType]],
        "KeyNameConstraint": NotRequired[KeyNameConstraintOutputTypeDef],
        "ObjectSizeGreaterThanBytes": NotRequired[int],
        "ObjectSizeLessThanBytes": NotRequired[int],
        "MatchAnyStorageClass": NotRequired[List[S3StorageClassType]],
    },
)
LifecycleExpirationTypeDef = TypedDict(
    "LifecycleExpirationTypeDef",
    {
        "Date": NotRequired[TimestampTypeDef],
        "Days": NotRequired[int],
        "ExpiredObjectDeleteMarker": NotRequired[bool],
    },
)
S3ObjectMetadataTypeDef = TypedDict(
    "S3ObjectMetadataTypeDef",
    {
        "CacheControl": NotRequired[str],
        "ContentDisposition": NotRequired[str],
        "ContentEncoding": NotRequired[str],
        "ContentLanguage": NotRequired[str],
        "UserMetadata": NotRequired[Mapping[str, str]],
        "ContentLength": NotRequired[int],
        "ContentMD5": NotRequired[str],
        "ContentType": NotRequired[str],
        "HttpExpiresDate": NotRequired[TimestampTypeDef],
        "RequesterCharged": NotRequired[bool],
        "SSEAlgorithm": NotRequired[S3SSEAlgorithmType],
    },
)
S3RetentionTypeDef = TypedDict(
    "S3RetentionTypeDef",
    {
        "RetainUntilDate": NotRequired[TimestampTypeDef],
        "Mode": NotRequired[S3ObjectLockRetentionModeType],
    },
)
TransitionTypeDef = TypedDict(
    "TransitionTypeDef",
    {
        "Date": NotRequired[TimestampTypeDef],
        "Days": NotRequired[int],
        "StorageClass": NotRequired[TransitionStorageClassType],
    },
)
S3GeneratedManifestDescriptorTypeDef = TypedDict(
    "S3GeneratedManifestDescriptorTypeDef",
    {
        "Format": NotRequired[Literal["S3InventoryReport_CSV_20211130"]],
        "Location": NotRequired[JobManifestLocationTypeDef],
    },
)
JobManifestOutputTypeDef = TypedDict(
    "JobManifestOutputTypeDef",
    {
        "Spec": JobManifestSpecOutputTypeDef,
        "Location": JobManifestLocationTypeDef,
    },
)
JobManifestSpecUnionTypeDef = Union[JobManifestSpecTypeDef, JobManifestSpecOutputTypeDef]
JobProgressSummaryTypeDef = TypedDict(
    "JobProgressSummaryTypeDef",
    {
        "TotalNumberOfTasks": NotRequired[int],
        "NumberOfTasksSucceeded": NotRequired[int],
        "NumberOfTasksFailed": NotRequired[int],
        "Timers": NotRequired[JobTimersTypeDef],
    },
)
KeyNameConstraintUnionTypeDef = Union[KeyNameConstraintTypeDef, KeyNameConstraintOutputTypeDef]
LambdaInvokeOperationUnionTypeDef = Union[
    LambdaInvokeOperationTypeDef, LambdaInvokeOperationOutputTypeDef
]
ListAccessGrantsInstancesResultTypeDef = TypedDict(
    "ListAccessGrantsInstancesResultTypeDef",
    {
        "AccessGrantsInstancesList": List[ListAccessGrantsInstanceEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListAccessGrantsLocationsResultTypeDef = TypedDict(
    "ListAccessGrantsLocationsResultTypeDef",
    {
        "AccessGrantsLocationsList": List[ListAccessGrantsLocationsEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListAccessPointsForObjectLambdaRequestListAccessPointsForObjectLambdaPaginateTypeDef = TypedDict(
    "ListAccessPointsForObjectLambdaRequestListAccessPointsForObjectLambdaPaginateTypeDef",
    {
        "AccountId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCallerAccessGrantsRequestListCallerAccessGrantsPaginateTypeDef = TypedDict(
    "ListCallerAccessGrantsRequestListCallerAccessGrantsPaginateTypeDef",
    {
        "AccountId": str,
        "GrantScope": NotRequired[str],
        "AllowedByApplication": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCallerAccessGrantsResultTypeDef = TypedDict(
    "ListCallerAccessGrantsResultTypeDef",
    {
        "CallerAccessGrantsList": List[ListCallerAccessGrantsEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListRegionalBucketsResultTypeDef = TypedDict(
    "ListRegionalBucketsResultTypeDef",
    {
        "RegionalBucketList": List[RegionalBucketTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListStorageLensConfigurationsResultTypeDef = TypedDict(
    "ListStorageLensConfigurationsResultTypeDef",
    {
        "StorageLensConfigurationList": List[ListStorageLensConfigurationEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListStorageLensGroupsResultTypeDef = TypedDict(
    "ListStorageLensGroupsResultTypeDef",
    {
        "StorageLensGroupList": List[ListStorageLensGroupEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
StorageLensGroupAndOperatorOutputTypeDef = TypedDict(
    "StorageLensGroupAndOperatorOutputTypeDef",
    {
        "MatchAnyPrefix": NotRequired[List[str]],
        "MatchAnySuffix": NotRequired[List[str]],
        "MatchAnyTag": NotRequired[List[S3TagTypeDef]],
        "MatchObjectAge": NotRequired[MatchObjectAgeTypeDef],
        "MatchObjectSize": NotRequired[MatchObjectSizeTypeDef],
    },
)
StorageLensGroupAndOperatorTypeDef = TypedDict(
    "StorageLensGroupAndOperatorTypeDef",
    {
        "MatchAnyPrefix": NotRequired[Sequence[str]],
        "MatchAnySuffix": NotRequired[Sequence[str]],
        "MatchAnyTag": NotRequired[Sequence[S3TagTypeDef]],
        "MatchObjectAge": NotRequired[MatchObjectAgeTypeDef],
        "MatchObjectSize": NotRequired[MatchObjectSizeTypeDef],
    },
)
StorageLensGroupOrOperatorOutputTypeDef = TypedDict(
    "StorageLensGroupOrOperatorOutputTypeDef",
    {
        "MatchAnyPrefix": NotRequired[List[str]],
        "MatchAnySuffix": NotRequired[List[str]],
        "MatchAnyTag": NotRequired[List[S3TagTypeDef]],
        "MatchObjectAge": NotRequired[MatchObjectAgeTypeDef],
        "MatchObjectSize": NotRequired[MatchObjectSizeTypeDef],
    },
)
StorageLensGroupOrOperatorTypeDef = TypedDict(
    "StorageLensGroupOrOperatorTypeDef",
    {
        "MatchAnyPrefix": NotRequired[Sequence[str]],
        "MatchAnySuffix": NotRequired[Sequence[str]],
        "MatchAnyTag": NotRequired[Sequence[S3TagTypeDef]],
        "MatchObjectAge": NotRequired[MatchObjectAgeTypeDef],
        "MatchObjectSize": NotRequired[MatchObjectSizeTypeDef],
    },
)
MetricsTypeDef = TypedDict(
    "MetricsTypeDef",
    {
        "Status": MetricsStatusType,
        "EventThreshold": NotRequired[ReplicationTimeValueTypeDef],
    },
)
ReplicationTimeTypeDef = TypedDict(
    "ReplicationTimeTypeDef",
    {
        "Status": ReplicationTimeStatusType,
        "Time": ReplicationTimeValueTypeDef,
    },
)
MultiRegionAccessPointPolicyDocumentTypeDef = TypedDict(
    "MultiRegionAccessPointPolicyDocumentTypeDef",
    {
        "Established": NotRequired[EstablishedMultiRegionAccessPointPolicyTypeDef],
        "Proposed": NotRequired[ProposedMultiRegionAccessPointPolicyTypeDef],
    },
)
MultiRegionAccessPointsAsyncResponseTypeDef = TypedDict(
    "MultiRegionAccessPointsAsyncResponseTypeDef",
    {
        "Regions": NotRequired[List[MultiRegionAccessPointRegionalResponseTypeDef]],
    },
)
MultiRegionAccessPointReportTypeDef = TypedDict(
    "MultiRegionAccessPointReportTypeDef",
    {
        "Name": NotRequired[str],
        "Alias": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "PublicAccessBlock": NotRequired[PublicAccessBlockConfigurationTypeDef],
        "Status": NotRequired[MultiRegionAccessPointStatusType],
        "Regions": NotRequired[List[RegionReportTypeDef]],
    },
)
PrefixLevelStorageMetricsTypeDef = TypedDict(
    "PrefixLevelStorageMetricsTypeDef",
    {
        "IsEnabled": NotRequired[bool],
        "SelectionCriteria": NotRequired[SelectionCriteriaTypeDef],
    },
)
PutBucketVersioningRequestRequestTypeDef = TypedDict(
    "PutBucketVersioningRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
        "VersioningConfiguration": VersioningConfigurationTypeDef,
        "MFA": NotRequired[str],
    },
)
S3GrantTypeDef = TypedDict(
    "S3GrantTypeDef",
    {
        "Grantee": NotRequired[S3GranteeTypeDef],
        "Permission": NotRequired[S3PermissionType],
    },
)
S3SetObjectLegalHoldOperationTypeDef = TypedDict(
    "S3SetObjectLegalHoldOperationTypeDef",
    {
        "LegalHold": S3ObjectLockLegalHoldTypeDef,
    },
)
S3SetObjectRetentionOperationOutputTypeDef = TypedDict(
    "S3SetObjectRetentionOperationOutputTypeDef",
    {
        "Retention": S3RetentionOutputTypeDef,
        "BypassGovernanceRetention": NotRequired[bool],
    },
)
StorageLensDataExportEncryptionOutputTypeDef = TypedDict(
    "StorageLensDataExportEncryptionOutputTypeDef",
    {
        "SSES3": NotRequired[Dict[str, Any]],
        "SSEKMS": NotRequired[SSEKMSTypeDef],
    },
)
StorageLensDataExportEncryptionTypeDef = TypedDict(
    "StorageLensDataExportEncryptionTypeDef",
    {
        "SSES3": NotRequired[Mapping[str, Any]],
        "SSEKMS": NotRequired[SSEKMSTypeDef],
    },
)
SourceSelectionCriteriaTypeDef = TypedDict(
    "SourceSelectionCriteriaTypeDef",
    {
        "SseKmsEncryptedObjects": NotRequired[SseKmsEncryptedObjectsTypeDef],
        "ReplicaModifications": NotRequired[ReplicaModificationsTypeDef],
    },
)
StorageLensGroupLevelOutputTypeDef = TypedDict(
    "StorageLensGroupLevelOutputTypeDef",
    {
        "SelectionCriteria": NotRequired[StorageLensGroupLevelSelectionCriteriaOutputTypeDef],
    },
)
StorageLensGroupLevelSelectionCriteriaUnionTypeDef = Union[
    StorageLensGroupLevelSelectionCriteriaTypeDef,
    StorageLensGroupLevelSelectionCriteriaOutputTypeDef,
]
ListAccessPointsResultTypeDef = TypedDict(
    "ListAccessPointsResultTypeDef",
    {
        "AccessPointList": List[AccessPointTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ObjectLambdaTransformationConfigurationOutputTypeDef = TypedDict(
    "ObjectLambdaTransformationConfigurationOutputTypeDef",
    {
        "Actions": List[ObjectLambdaTransformationConfigurationActionType],
        "ContentTransformation": ObjectLambdaContentTransformationTypeDef,
    },
)
ObjectLambdaTransformationConfigurationTypeDef = TypedDict(
    "ObjectLambdaTransformationConfigurationTypeDef",
    {
        "Actions": Sequence[ObjectLambdaTransformationConfigurationActionType],
        "ContentTransformation": ObjectLambdaContentTransformationTypeDef,
    },
)
ListAccessGrantsResultTypeDef = TypedDict(
    "ListAccessGrantsResultTypeDef",
    {
        "AccessGrantsList": List[ListAccessGrantEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListAccessPointsForObjectLambdaResultTypeDef = TypedDict(
    "ListAccessPointsForObjectLambdaResultTypeDef",
    {
        "ObjectLambdaAccessPointList": List[ObjectLambdaAccessPointTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
LifecycleRuleFilterOutputTypeDef = TypedDict(
    "LifecycleRuleFilterOutputTypeDef",
    {
        "Prefix": NotRequired[str],
        "Tag": NotRequired[S3TagTypeDef],
        "And": NotRequired[LifecycleRuleAndOperatorOutputTypeDef],
        "ObjectSizeGreaterThan": NotRequired[int],
        "ObjectSizeLessThan": NotRequired[int],
    },
)
LifecycleRuleAndOperatorUnionTypeDef = Union[
    LifecycleRuleAndOperatorTypeDef, LifecycleRuleAndOperatorOutputTypeDef
]
ReplicationRuleFilterOutputTypeDef = TypedDict(
    "ReplicationRuleFilterOutputTypeDef",
    {
        "Prefix": NotRequired[str],
        "Tag": NotRequired[S3TagTypeDef],
        "And": NotRequired[ReplicationRuleAndOperatorOutputTypeDef],
    },
)
ReplicationRuleAndOperatorUnionTypeDef = Union[
    ReplicationRuleAndOperatorTypeDef, ReplicationRuleAndOperatorOutputTypeDef
]
S3SetObjectTaggingOperationUnionTypeDef = Union[
    S3SetObjectTaggingOperationTypeDef, S3SetObjectTaggingOperationOutputTypeDef
]
PutBucketTaggingRequestRequestTypeDef = TypedDict(
    "PutBucketTaggingRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
        "Tagging": TaggingTypeDef,
    },
)
AsyncRequestParametersTypeDef = TypedDict(
    "AsyncRequestParametersTypeDef",
    {
        "CreateMultiRegionAccessPointRequest": NotRequired[
            CreateMultiRegionAccessPointInputOutputTypeDef
        ],
        "DeleteMultiRegionAccessPointRequest": NotRequired[
            DeleteMultiRegionAccessPointInputTypeDef
        ],
        "PutMultiRegionAccessPointPolicyRequest": NotRequired[
            PutMultiRegionAccessPointPolicyInputTypeDef
        ],
    },
)
CreateMultiRegionAccessPointRequestRequestTypeDef = TypedDict(
    "CreateMultiRegionAccessPointRequestRequestTypeDef",
    {
        "AccountId": str,
        "ClientToken": str,
        "Details": CreateMultiRegionAccessPointInputTypeDef,
    },
)
S3ManifestOutputLocationOutputTypeDef = TypedDict(
    "S3ManifestOutputLocationOutputTypeDef",
    {
        "Bucket": str,
        "ManifestFormat": Literal["S3InventoryReport_CSV_20211130"],
        "ExpectedManifestBucketOwner": NotRequired[str],
        "ManifestPrefix": NotRequired[str],
        "ManifestEncryption": NotRequired[GeneratedManifestEncryptionOutputTypeDef],
    },
)
GeneratedManifestEncryptionUnionTypeDef = Union[
    GeneratedManifestEncryptionTypeDef, GeneratedManifestEncryptionOutputTypeDef
]
LifecycleExpirationUnionTypeDef = Union[
    LifecycleExpirationTypeDef, LifecycleExpirationOutputTypeDef
]
S3ObjectMetadataUnionTypeDef = Union[S3ObjectMetadataTypeDef, S3ObjectMetadataOutputTypeDef]
S3RetentionUnionTypeDef = Union[S3RetentionTypeDef, S3RetentionOutputTypeDef]
TransitionUnionTypeDef = Union[TransitionTypeDef, TransitionOutputTypeDef]
JobManifestTypeDef = TypedDict(
    "JobManifestTypeDef",
    {
        "Spec": JobManifestSpecUnionTypeDef,
        "Location": JobManifestLocationTypeDef,
    },
)
JobListDescriptorTypeDef = TypedDict(
    "JobListDescriptorTypeDef",
    {
        "JobId": NotRequired[str],
        "Description": NotRequired[str],
        "Operation": NotRequired[OperationNameType],
        "Priority": NotRequired[int],
        "Status": NotRequired[JobStatusType],
        "CreationTime": NotRequired[datetime],
        "TerminationDate": NotRequired[datetime],
        "ProgressSummary": NotRequired[JobProgressSummaryTypeDef],
    },
)
JobManifestGeneratorFilterTypeDef = TypedDict(
    "JobManifestGeneratorFilterTypeDef",
    {
        "EligibleForReplication": NotRequired[bool],
        "CreatedAfter": NotRequired[TimestampTypeDef],
        "CreatedBefore": NotRequired[TimestampTypeDef],
        "ObjectReplicationStatuses": NotRequired[Sequence[ReplicationStatusType]],
        "KeyNameConstraint": NotRequired[KeyNameConstraintUnionTypeDef],
        "ObjectSizeGreaterThanBytes": NotRequired[int],
        "ObjectSizeLessThanBytes": NotRequired[int],
        "MatchAnyStorageClass": NotRequired[Sequence[S3StorageClassType]],
    },
)
StorageLensGroupAndOperatorUnionTypeDef = Union[
    StorageLensGroupAndOperatorTypeDef, StorageLensGroupAndOperatorOutputTypeDef
]
StorageLensGroupFilterOutputTypeDef = TypedDict(
    "StorageLensGroupFilterOutputTypeDef",
    {
        "MatchAnyPrefix": NotRequired[List[str]],
        "MatchAnySuffix": NotRequired[List[str]],
        "MatchAnyTag": NotRequired[List[S3TagTypeDef]],
        "MatchObjectAge": NotRequired[MatchObjectAgeTypeDef],
        "MatchObjectSize": NotRequired[MatchObjectSizeTypeDef],
        "And": NotRequired[StorageLensGroupAndOperatorOutputTypeDef],
        "Or": NotRequired[StorageLensGroupOrOperatorOutputTypeDef],
    },
)
StorageLensGroupOrOperatorUnionTypeDef = Union[
    StorageLensGroupOrOperatorTypeDef, StorageLensGroupOrOperatorOutputTypeDef
]
DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "Bucket": str,
        "Account": NotRequired[str],
        "ReplicationTime": NotRequired[ReplicationTimeTypeDef],
        "AccessControlTranslation": NotRequired[AccessControlTranslationTypeDef],
        "EncryptionConfiguration": NotRequired[EncryptionConfigurationTypeDef],
        "Metrics": NotRequired[MetricsTypeDef],
        "StorageClass": NotRequired[ReplicationStorageClassType],
    },
)
GetMultiRegionAccessPointPolicyResultTypeDef = TypedDict(
    "GetMultiRegionAccessPointPolicyResultTypeDef",
    {
        "Policy": MultiRegionAccessPointPolicyDocumentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AsyncResponseDetailsTypeDef = TypedDict(
    "AsyncResponseDetailsTypeDef",
    {
        "MultiRegionAccessPointDetails": NotRequired[MultiRegionAccessPointsAsyncResponseTypeDef],
        "ErrorDetails": NotRequired[AsyncErrorDetailsTypeDef],
    },
)
GetMultiRegionAccessPointResultTypeDef = TypedDict(
    "GetMultiRegionAccessPointResultTypeDef",
    {
        "AccessPoint": MultiRegionAccessPointReportTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListMultiRegionAccessPointsResultTypeDef = TypedDict(
    "ListMultiRegionAccessPointsResultTypeDef",
    {
        "AccessPoints": List[MultiRegionAccessPointReportTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PrefixLevelTypeDef = TypedDict(
    "PrefixLevelTypeDef",
    {
        "StorageMetrics": PrefixLevelStorageMetricsTypeDef,
    },
)
S3AccessControlListOutputTypeDef = TypedDict(
    "S3AccessControlListOutputTypeDef",
    {
        "Owner": S3ObjectOwnerTypeDef,
        "Grants": NotRequired[List[S3GrantTypeDef]],
    },
)
S3AccessControlListTypeDef = TypedDict(
    "S3AccessControlListTypeDef",
    {
        "Owner": S3ObjectOwnerTypeDef,
        "Grants": NotRequired[Sequence[S3GrantTypeDef]],
    },
)
S3CopyObjectOperationOutputTypeDef = TypedDict(
    "S3CopyObjectOperationOutputTypeDef",
    {
        "TargetResource": NotRequired[str],
        "CannedAccessControlList": NotRequired[S3CannedAccessControlListType],
        "AccessControlGrants": NotRequired[List[S3GrantTypeDef]],
        "MetadataDirective": NotRequired[S3MetadataDirectiveType],
        "ModifiedSinceConstraint": NotRequired[datetime],
        "NewObjectMetadata": NotRequired[S3ObjectMetadataOutputTypeDef],
        "NewObjectTagging": NotRequired[List[S3TagTypeDef]],
        "RedirectLocation": NotRequired[str],
        "RequesterPays": NotRequired[bool],
        "StorageClass": NotRequired[S3StorageClassType],
        "UnModifiedSinceConstraint": NotRequired[datetime],
        "SSEAwsKmsKeyId": NotRequired[str],
        "TargetKeyPrefix": NotRequired[str],
        "ObjectLockLegalHoldStatus": NotRequired[S3ObjectLockLegalHoldStatusType],
        "ObjectLockMode": NotRequired[S3ObjectLockModeType],
        "ObjectLockRetainUntilDate": NotRequired[datetime],
        "BucketKeyEnabled": NotRequired[bool],
        "ChecksumAlgorithm": NotRequired[S3ChecksumAlgorithmType],
    },
)
S3BucketDestinationOutputTypeDef = TypedDict(
    "S3BucketDestinationOutputTypeDef",
    {
        "Format": FormatType,
        "OutputSchemaVersion": Literal["V_1"],
        "AccountId": str,
        "Arn": str,
        "Prefix": NotRequired[str],
        "Encryption": NotRequired[StorageLensDataExportEncryptionOutputTypeDef],
    },
)
StorageLensDataExportEncryptionUnionTypeDef = Union[
    StorageLensDataExportEncryptionTypeDef, StorageLensDataExportEncryptionOutputTypeDef
]
StorageLensGroupLevelTypeDef = TypedDict(
    "StorageLensGroupLevelTypeDef",
    {
        "SelectionCriteria": NotRequired[StorageLensGroupLevelSelectionCriteriaUnionTypeDef],
    },
)
ObjectLambdaConfigurationOutputTypeDef = TypedDict(
    "ObjectLambdaConfigurationOutputTypeDef",
    {
        "SupportingAccessPoint": str,
        "TransformationConfigurations": List[ObjectLambdaTransformationConfigurationOutputTypeDef],
        "CloudWatchMetricsEnabled": NotRequired[bool],
        "AllowedFeatures": NotRequired[List[ObjectLambdaAllowedFeatureType]],
    },
)
ObjectLambdaTransformationConfigurationUnionTypeDef = Union[
    ObjectLambdaTransformationConfigurationTypeDef,
    ObjectLambdaTransformationConfigurationOutputTypeDef,
]
LifecycleRuleOutputTypeDef = TypedDict(
    "LifecycleRuleOutputTypeDef",
    {
        "Status": ExpirationStatusType,
        "Expiration": NotRequired[LifecycleExpirationOutputTypeDef],
        "ID": NotRequired[str],
        "Filter": NotRequired[LifecycleRuleFilterOutputTypeDef],
        "Transitions": NotRequired[List[TransitionOutputTypeDef]],
        "NoncurrentVersionTransitions": NotRequired[List[NoncurrentVersionTransitionTypeDef]],
        "NoncurrentVersionExpiration": NotRequired[NoncurrentVersionExpirationTypeDef],
        "AbortIncompleteMultipartUpload": NotRequired[AbortIncompleteMultipartUploadTypeDef],
    },
)
LifecycleRuleFilterTypeDef = TypedDict(
    "LifecycleRuleFilterTypeDef",
    {
        "Prefix": NotRequired[str],
        "Tag": NotRequired[S3TagTypeDef],
        "And": NotRequired[LifecycleRuleAndOperatorUnionTypeDef],
        "ObjectSizeGreaterThan": NotRequired[int],
        "ObjectSizeLessThan": NotRequired[int],
    },
)
ReplicationRuleFilterTypeDef = TypedDict(
    "ReplicationRuleFilterTypeDef",
    {
        "Prefix": NotRequired[str],
        "Tag": NotRequired[S3TagTypeDef],
        "And": NotRequired[ReplicationRuleAndOperatorUnionTypeDef],
    },
)
S3JobManifestGeneratorOutputTypeDef = TypedDict(
    "S3JobManifestGeneratorOutputTypeDef",
    {
        "SourceBucket": str,
        "EnableManifestOutput": bool,
        "ExpectedBucketOwner": NotRequired[str],
        "ManifestOutputLocation": NotRequired[S3ManifestOutputLocationOutputTypeDef],
        "Filter": NotRequired[JobManifestGeneratorFilterOutputTypeDef],
    },
)
S3ManifestOutputLocationTypeDef = TypedDict(
    "S3ManifestOutputLocationTypeDef",
    {
        "Bucket": str,
        "ManifestFormat": Literal["S3InventoryReport_CSV_20211130"],
        "ExpectedManifestBucketOwner": NotRequired[str],
        "ManifestPrefix": NotRequired[str],
        "ManifestEncryption": NotRequired[GeneratedManifestEncryptionUnionTypeDef],
    },
)
S3CopyObjectOperationTypeDef = TypedDict(
    "S3CopyObjectOperationTypeDef",
    {
        "TargetResource": NotRequired[str],
        "CannedAccessControlList": NotRequired[S3CannedAccessControlListType],
        "AccessControlGrants": NotRequired[Sequence[S3GrantTypeDef]],
        "MetadataDirective": NotRequired[S3MetadataDirectiveType],
        "ModifiedSinceConstraint": NotRequired[TimestampTypeDef],
        "NewObjectMetadata": NotRequired[S3ObjectMetadataUnionTypeDef],
        "NewObjectTagging": NotRequired[Sequence[S3TagTypeDef]],
        "RedirectLocation": NotRequired[str],
        "RequesterPays": NotRequired[bool],
        "StorageClass": NotRequired[S3StorageClassType],
        "UnModifiedSinceConstraint": NotRequired[TimestampTypeDef],
        "SSEAwsKmsKeyId": NotRequired[str],
        "TargetKeyPrefix": NotRequired[str],
        "ObjectLockLegalHoldStatus": NotRequired[S3ObjectLockLegalHoldStatusType],
        "ObjectLockMode": NotRequired[S3ObjectLockModeType],
        "ObjectLockRetainUntilDate": NotRequired[TimestampTypeDef],
        "BucketKeyEnabled": NotRequired[bool],
        "ChecksumAlgorithm": NotRequired[S3ChecksumAlgorithmType],
    },
)
S3SetObjectRetentionOperationTypeDef = TypedDict(
    "S3SetObjectRetentionOperationTypeDef",
    {
        "Retention": S3RetentionUnionTypeDef,
        "BypassGovernanceRetention": NotRequired[bool],
    },
)
ListJobsResultTypeDef = TypedDict(
    "ListJobsResultTypeDef",
    {
        "Jobs": List[JobListDescriptorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
JobManifestGeneratorFilterUnionTypeDef = Union[
    JobManifestGeneratorFilterTypeDef, JobManifestGeneratorFilterOutputTypeDef
]
StorageLensGroupOutputTypeDef = TypedDict(
    "StorageLensGroupOutputTypeDef",
    {
        "Name": str,
        "Filter": StorageLensGroupFilterOutputTypeDef,
        "StorageLensGroupArn": NotRequired[str],
    },
)
StorageLensGroupFilterTypeDef = TypedDict(
    "StorageLensGroupFilterTypeDef",
    {
        "MatchAnyPrefix": NotRequired[Sequence[str]],
        "MatchAnySuffix": NotRequired[Sequence[str]],
        "MatchAnyTag": NotRequired[Sequence[S3TagTypeDef]],
        "MatchObjectAge": NotRequired[MatchObjectAgeTypeDef],
        "MatchObjectSize": NotRequired[MatchObjectSizeTypeDef],
        "And": NotRequired[StorageLensGroupAndOperatorUnionTypeDef],
        "Or": NotRequired[StorageLensGroupOrOperatorUnionTypeDef],
    },
)
ReplicationRuleOutputTypeDef = TypedDict(
    "ReplicationRuleOutputTypeDef",
    {
        "Status": ReplicationRuleStatusType,
        "Destination": DestinationTypeDef,
        "Bucket": str,
        "ID": NotRequired[str],
        "Priority": NotRequired[int],
        "Prefix": NotRequired[str],
        "Filter": NotRequired[ReplicationRuleFilterOutputTypeDef],
        "SourceSelectionCriteria": NotRequired[SourceSelectionCriteriaTypeDef],
        "ExistingObjectReplication": NotRequired[ExistingObjectReplicationTypeDef],
        "DeleteMarkerReplication": NotRequired[DeleteMarkerReplicationTypeDef],
    },
)
AsyncOperationTypeDef = TypedDict(
    "AsyncOperationTypeDef",
    {
        "CreationTime": NotRequired[datetime],
        "Operation": NotRequired[AsyncOperationNameType],
        "RequestTokenARN": NotRequired[str],
        "RequestParameters": NotRequired[AsyncRequestParametersTypeDef],
        "RequestStatus": NotRequired[str],
        "ResponseDetails": NotRequired[AsyncResponseDetailsTypeDef],
    },
)
BucketLevelTypeDef = TypedDict(
    "BucketLevelTypeDef",
    {
        "ActivityMetrics": NotRequired[ActivityMetricsTypeDef],
        "PrefixLevel": NotRequired[PrefixLevelTypeDef],
        "AdvancedCostOptimizationMetrics": NotRequired[AdvancedCostOptimizationMetricsTypeDef],
        "AdvancedDataProtectionMetrics": NotRequired[AdvancedDataProtectionMetricsTypeDef],
        "DetailedStatusCodesMetrics": NotRequired[DetailedStatusCodesMetricsTypeDef],
    },
)
S3AccessControlPolicyOutputTypeDef = TypedDict(
    "S3AccessControlPolicyOutputTypeDef",
    {
        "AccessControlList": NotRequired[S3AccessControlListOutputTypeDef],
        "CannedAccessControlList": NotRequired[S3CannedAccessControlListType],
    },
)
S3AccessControlListUnionTypeDef = Union[
    S3AccessControlListTypeDef, S3AccessControlListOutputTypeDef
]
StorageLensDataExportOutputTypeDef = TypedDict(
    "StorageLensDataExportOutputTypeDef",
    {
        "S3BucketDestination": NotRequired[S3BucketDestinationOutputTypeDef],
        "CloudWatchMetrics": NotRequired[CloudWatchMetricsTypeDef],
    },
)
S3BucketDestinationTypeDef = TypedDict(
    "S3BucketDestinationTypeDef",
    {
        "Format": FormatType,
        "OutputSchemaVersion": Literal["V_1"],
        "AccountId": str,
        "Arn": str,
        "Prefix": NotRequired[str],
        "Encryption": NotRequired[StorageLensDataExportEncryptionUnionTypeDef],
    },
)
StorageLensGroupLevelUnionTypeDef = Union[
    StorageLensGroupLevelTypeDef, StorageLensGroupLevelOutputTypeDef
]
GetAccessPointConfigurationForObjectLambdaResultTypeDef = TypedDict(
    "GetAccessPointConfigurationForObjectLambdaResultTypeDef",
    {
        "Configuration": ObjectLambdaConfigurationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ObjectLambdaConfigurationTypeDef = TypedDict(
    "ObjectLambdaConfigurationTypeDef",
    {
        "SupportingAccessPoint": str,
        "TransformationConfigurations": Sequence[
            ObjectLambdaTransformationConfigurationUnionTypeDef
        ],
        "CloudWatchMetricsEnabled": NotRequired[bool],
        "AllowedFeatures": NotRequired[Sequence[ObjectLambdaAllowedFeatureType]],
    },
)
GetBucketLifecycleConfigurationResultTypeDef = TypedDict(
    "GetBucketLifecycleConfigurationResultTypeDef",
    {
        "Rules": List[LifecycleRuleOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LifecycleRuleFilterUnionTypeDef = Union[
    LifecycleRuleFilterTypeDef, LifecycleRuleFilterOutputTypeDef
]
ReplicationRuleFilterUnionTypeDef = Union[
    ReplicationRuleFilterTypeDef, ReplicationRuleFilterOutputTypeDef
]
JobManifestGeneratorOutputTypeDef = TypedDict(
    "JobManifestGeneratorOutputTypeDef",
    {
        "S3JobManifestGenerator": NotRequired[S3JobManifestGeneratorOutputTypeDef],
    },
)
S3ManifestOutputLocationUnionTypeDef = Union[
    S3ManifestOutputLocationTypeDef, S3ManifestOutputLocationOutputTypeDef
]
S3CopyObjectOperationUnionTypeDef = Union[
    S3CopyObjectOperationTypeDef, S3CopyObjectOperationOutputTypeDef
]
S3SetObjectRetentionOperationUnionTypeDef = Union[
    S3SetObjectRetentionOperationTypeDef, S3SetObjectRetentionOperationOutputTypeDef
]
GetStorageLensGroupResultTypeDef = TypedDict(
    "GetStorageLensGroupResultTypeDef",
    {
        "StorageLensGroup": StorageLensGroupOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StorageLensGroupFilterUnionTypeDef = Union[
    StorageLensGroupFilterTypeDef, StorageLensGroupFilterOutputTypeDef
]
ReplicationConfigurationOutputTypeDef = TypedDict(
    "ReplicationConfigurationOutputTypeDef",
    {
        "Role": str,
        "Rules": List[ReplicationRuleOutputTypeDef],
    },
)
DescribeMultiRegionAccessPointOperationResultTypeDef = TypedDict(
    "DescribeMultiRegionAccessPointOperationResultTypeDef",
    {
        "AsyncOperation": AsyncOperationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AccountLevelOutputTypeDef = TypedDict(
    "AccountLevelOutputTypeDef",
    {
        "BucketLevel": BucketLevelTypeDef,
        "ActivityMetrics": NotRequired[ActivityMetricsTypeDef],
        "AdvancedCostOptimizationMetrics": NotRequired[AdvancedCostOptimizationMetricsTypeDef],
        "AdvancedDataProtectionMetrics": NotRequired[AdvancedDataProtectionMetricsTypeDef],
        "DetailedStatusCodesMetrics": NotRequired[DetailedStatusCodesMetricsTypeDef],
        "StorageLensGroupLevel": NotRequired[StorageLensGroupLevelOutputTypeDef],
    },
)
S3SetObjectAclOperationOutputTypeDef = TypedDict(
    "S3SetObjectAclOperationOutputTypeDef",
    {
        "AccessControlPolicy": NotRequired[S3AccessControlPolicyOutputTypeDef],
    },
)
S3AccessControlPolicyTypeDef = TypedDict(
    "S3AccessControlPolicyTypeDef",
    {
        "AccessControlList": NotRequired[S3AccessControlListUnionTypeDef],
        "CannedAccessControlList": NotRequired[S3CannedAccessControlListType],
    },
)
S3BucketDestinationUnionTypeDef = Union[
    S3BucketDestinationTypeDef, S3BucketDestinationOutputTypeDef
]
AccountLevelTypeDef = TypedDict(
    "AccountLevelTypeDef",
    {
        "BucketLevel": BucketLevelTypeDef,
        "ActivityMetrics": NotRequired[ActivityMetricsTypeDef],
        "AdvancedCostOptimizationMetrics": NotRequired[AdvancedCostOptimizationMetricsTypeDef],
        "AdvancedDataProtectionMetrics": NotRequired[AdvancedDataProtectionMetricsTypeDef],
        "DetailedStatusCodesMetrics": NotRequired[DetailedStatusCodesMetricsTypeDef],
        "StorageLensGroupLevel": NotRequired[StorageLensGroupLevelUnionTypeDef],
    },
)
CreateAccessPointForObjectLambdaRequestRequestTypeDef = TypedDict(
    "CreateAccessPointForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
        "Configuration": ObjectLambdaConfigurationTypeDef,
    },
)
PutAccessPointConfigurationForObjectLambdaRequestRequestTypeDef = TypedDict(
    "PutAccessPointConfigurationForObjectLambdaRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
        "Configuration": ObjectLambdaConfigurationTypeDef,
    },
)
LifecycleRuleTypeDef = TypedDict(
    "LifecycleRuleTypeDef",
    {
        "Status": ExpirationStatusType,
        "Expiration": NotRequired[LifecycleExpirationUnionTypeDef],
        "ID": NotRequired[str],
        "Filter": NotRequired[LifecycleRuleFilterUnionTypeDef],
        "Transitions": NotRequired[Sequence[TransitionUnionTypeDef]],
        "NoncurrentVersionTransitions": NotRequired[Sequence[NoncurrentVersionTransitionTypeDef]],
        "NoncurrentVersionExpiration": NotRequired[NoncurrentVersionExpirationTypeDef],
        "AbortIncompleteMultipartUpload": NotRequired[AbortIncompleteMultipartUploadTypeDef],
    },
)
ReplicationRuleTypeDef = TypedDict(
    "ReplicationRuleTypeDef",
    {
        "Status": ReplicationRuleStatusType,
        "Destination": DestinationTypeDef,
        "Bucket": str,
        "ID": NotRequired[str],
        "Priority": NotRequired[int],
        "Prefix": NotRequired[str],
        "Filter": NotRequired[ReplicationRuleFilterUnionTypeDef],
        "SourceSelectionCriteria": NotRequired[SourceSelectionCriteriaTypeDef],
        "ExistingObjectReplication": NotRequired[ExistingObjectReplicationTypeDef],
        "DeleteMarkerReplication": NotRequired[DeleteMarkerReplicationTypeDef],
    },
)
S3JobManifestGeneratorTypeDef = TypedDict(
    "S3JobManifestGeneratorTypeDef",
    {
        "SourceBucket": str,
        "EnableManifestOutput": bool,
        "ExpectedBucketOwner": NotRequired[str],
        "ManifestOutputLocation": NotRequired[S3ManifestOutputLocationUnionTypeDef],
        "Filter": NotRequired[JobManifestGeneratorFilterUnionTypeDef],
    },
)
StorageLensGroupTypeDef = TypedDict(
    "StorageLensGroupTypeDef",
    {
        "Name": str,
        "Filter": StorageLensGroupFilterUnionTypeDef,
        "StorageLensGroupArn": NotRequired[str],
    },
)
GetBucketReplicationResultTypeDef = TypedDict(
    "GetBucketReplicationResultTypeDef",
    {
        "ReplicationConfiguration": ReplicationConfigurationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StorageLensConfigurationOutputTypeDef = TypedDict(
    "StorageLensConfigurationOutputTypeDef",
    {
        "Id": str,
        "AccountLevel": AccountLevelOutputTypeDef,
        "IsEnabled": bool,
        "Include": NotRequired[IncludeOutputTypeDef],
        "Exclude": NotRequired[ExcludeOutputTypeDef],
        "DataExport": NotRequired[StorageLensDataExportOutputTypeDef],
        "AwsOrg": NotRequired[StorageLensAwsOrgTypeDef],
        "StorageLensArn": NotRequired[str],
    },
)
JobOperationOutputTypeDef = TypedDict(
    "JobOperationOutputTypeDef",
    {
        "LambdaInvoke": NotRequired[LambdaInvokeOperationOutputTypeDef],
        "S3PutObjectCopy": NotRequired[S3CopyObjectOperationOutputTypeDef],
        "S3PutObjectAcl": NotRequired[S3SetObjectAclOperationOutputTypeDef],
        "S3PutObjectTagging": NotRequired[S3SetObjectTaggingOperationOutputTypeDef],
        "S3DeleteObjectTagging": NotRequired[Dict[str, Any]],
        "S3InitiateRestoreObject": NotRequired[S3InitiateRestoreObjectOperationTypeDef],
        "S3PutObjectLegalHold": NotRequired[S3SetObjectLegalHoldOperationTypeDef],
        "S3PutObjectRetention": NotRequired[S3SetObjectRetentionOperationOutputTypeDef],
        "S3ReplicateObject": NotRequired[Dict[str, Any]],
    },
)
S3AccessControlPolicyUnionTypeDef = Union[
    S3AccessControlPolicyTypeDef, S3AccessControlPolicyOutputTypeDef
]
StorageLensDataExportTypeDef = TypedDict(
    "StorageLensDataExportTypeDef",
    {
        "S3BucketDestination": NotRequired[S3BucketDestinationUnionTypeDef],
        "CloudWatchMetrics": NotRequired[CloudWatchMetricsTypeDef],
    },
)
AccountLevelUnionTypeDef = Union[AccountLevelTypeDef, AccountLevelOutputTypeDef]
LifecycleRuleUnionTypeDef = Union[LifecycleRuleTypeDef, LifecycleRuleOutputTypeDef]
ReplicationRuleUnionTypeDef = Union[ReplicationRuleTypeDef, ReplicationRuleOutputTypeDef]
S3JobManifestGeneratorUnionTypeDef = Union[
    S3JobManifestGeneratorTypeDef, S3JobManifestGeneratorOutputTypeDef
]
CreateStorageLensGroupRequestRequestTypeDef = TypedDict(
    "CreateStorageLensGroupRequestRequestTypeDef",
    {
        "AccountId": str,
        "StorageLensGroup": StorageLensGroupTypeDef,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
UpdateStorageLensGroupRequestRequestTypeDef = TypedDict(
    "UpdateStorageLensGroupRequestRequestTypeDef",
    {
        "Name": str,
        "AccountId": str,
        "StorageLensGroup": StorageLensGroupTypeDef,
    },
)
GetStorageLensConfigurationResultTypeDef = TypedDict(
    "GetStorageLensConfigurationResultTypeDef",
    {
        "StorageLensConfiguration": StorageLensConfigurationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
JobDescriptorTypeDef = TypedDict(
    "JobDescriptorTypeDef",
    {
        "JobId": NotRequired[str],
        "ConfirmationRequired": NotRequired[bool],
        "Description": NotRequired[str],
        "JobArn": NotRequired[str],
        "Status": NotRequired[JobStatusType],
        "Manifest": NotRequired[JobManifestOutputTypeDef],
        "Operation": NotRequired[JobOperationOutputTypeDef],
        "Priority": NotRequired[int],
        "ProgressSummary": NotRequired[JobProgressSummaryTypeDef],
        "StatusUpdateReason": NotRequired[str],
        "FailureReasons": NotRequired[List[JobFailureTypeDef]],
        "Report": NotRequired[JobReportTypeDef],
        "CreationTime": NotRequired[datetime],
        "TerminationDate": NotRequired[datetime],
        "RoleArn": NotRequired[str],
        "SuspendedDate": NotRequired[datetime],
        "SuspendedCause": NotRequired[str],
        "ManifestGenerator": NotRequired[JobManifestGeneratorOutputTypeDef],
        "GeneratedManifestDescriptor": NotRequired[S3GeneratedManifestDescriptorTypeDef],
    },
)
S3SetObjectAclOperationTypeDef = TypedDict(
    "S3SetObjectAclOperationTypeDef",
    {
        "AccessControlPolicy": NotRequired[S3AccessControlPolicyUnionTypeDef],
    },
)
StorageLensDataExportUnionTypeDef = Union[
    StorageLensDataExportTypeDef, StorageLensDataExportOutputTypeDef
]
LifecycleConfigurationTypeDef = TypedDict(
    "LifecycleConfigurationTypeDef",
    {
        "Rules": NotRequired[Sequence[LifecycleRuleUnionTypeDef]],
    },
)
ReplicationConfigurationTypeDef = TypedDict(
    "ReplicationConfigurationTypeDef",
    {
        "Role": str,
        "Rules": Sequence[ReplicationRuleUnionTypeDef],
    },
)
JobManifestGeneratorTypeDef = TypedDict(
    "JobManifestGeneratorTypeDef",
    {
        "S3JobManifestGenerator": NotRequired[S3JobManifestGeneratorUnionTypeDef],
    },
)
DescribeJobResultTypeDef = TypedDict(
    "DescribeJobResultTypeDef",
    {
        "Job": JobDescriptorTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
S3SetObjectAclOperationUnionTypeDef = Union[
    S3SetObjectAclOperationTypeDef, S3SetObjectAclOperationOutputTypeDef
]
StorageLensConfigurationTypeDef = TypedDict(
    "StorageLensConfigurationTypeDef",
    {
        "Id": str,
        "AccountLevel": AccountLevelUnionTypeDef,
        "IsEnabled": bool,
        "Include": NotRequired[IncludeUnionTypeDef],
        "Exclude": NotRequired[ExcludeUnionTypeDef],
        "DataExport": NotRequired[StorageLensDataExportUnionTypeDef],
        "AwsOrg": NotRequired[StorageLensAwsOrgTypeDef],
        "StorageLensArn": NotRequired[str],
    },
)
PutBucketLifecycleConfigurationRequestRequestTypeDef = TypedDict(
    "PutBucketLifecycleConfigurationRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
        "LifecycleConfiguration": NotRequired[LifecycleConfigurationTypeDef],
    },
)
PutBucketReplicationRequestRequestTypeDef = TypedDict(
    "PutBucketReplicationRequestRequestTypeDef",
    {
        "AccountId": str,
        "Bucket": str,
        "ReplicationConfiguration": ReplicationConfigurationTypeDef,
    },
)
JobOperationTypeDef = TypedDict(
    "JobOperationTypeDef",
    {
        "LambdaInvoke": NotRequired[LambdaInvokeOperationUnionTypeDef],
        "S3PutObjectCopy": NotRequired[S3CopyObjectOperationUnionTypeDef],
        "S3PutObjectAcl": NotRequired[S3SetObjectAclOperationUnionTypeDef],
        "S3PutObjectTagging": NotRequired[S3SetObjectTaggingOperationUnionTypeDef],
        "S3DeleteObjectTagging": NotRequired[Mapping[str, Any]],
        "S3InitiateRestoreObject": NotRequired[S3InitiateRestoreObjectOperationTypeDef],
        "S3PutObjectLegalHold": NotRequired[S3SetObjectLegalHoldOperationTypeDef],
        "S3PutObjectRetention": NotRequired[S3SetObjectRetentionOperationUnionTypeDef],
        "S3ReplicateObject": NotRequired[Mapping[str, Any]],
    },
)
PutStorageLensConfigurationRequestRequestTypeDef = TypedDict(
    "PutStorageLensConfigurationRequestRequestTypeDef",
    {
        "ConfigId": str,
        "AccountId": str,
        "StorageLensConfiguration": StorageLensConfigurationTypeDef,
        "Tags": NotRequired[Sequence[StorageLensTagTypeDef]],
    },
)
CreateJobRequestRequestTypeDef = TypedDict(
    "CreateJobRequestRequestTypeDef",
    {
        "AccountId": str,
        "Operation": JobOperationTypeDef,
        "Report": JobReportTypeDef,
        "ClientRequestToken": str,
        "Priority": int,
        "RoleArn": str,
        "ConfirmationRequired": NotRequired[bool],
        "Manifest": NotRequired[JobManifestTypeDef],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[S3TagTypeDef]],
        "ManifestGenerator": NotRequired[JobManifestGeneratorTypeDef],
    },
)
