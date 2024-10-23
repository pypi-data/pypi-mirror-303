"""
Type annotations for macie2 service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_macie2/type_defs/)

Usage::

    ```python
    from mypy_boto3_macie2.type_defs import AcceptInvitationRequestRequestTypeDef

    data: AcceptInvitationRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    AdminStatusType,
    AllowListStatusCodeType,
    AllowsUnencryptedObjectUploadsType,
    AutoEnableModeType,
    AutomatedDiscoveryAccountStatusType,
    AutomatedDiscoveryAccountUpdateErrorCodeType,
    AutomatedDiscoveryMonitoringStatusType,
    AutomatedDiscoveryStatusType,
    AvailabilityCodeType,
    ClassificationScopeUpdateOperationType,
    DataIdentifierSeverityType,
    DataIdentifierTypeType,
    DayOfWeekType,
    EffectivePermissionType,
    EncryptionTypeType,
    ErrorCodeType,
    FindingCategoryType,
    FindingPublishingFrequencyType,
    FindingsFilterActionType,
    FindingStatisticsSortAttributeNameType,
    FindingTypeType,
    GroupByType,
    IsDefinedInJobType,
    IsMonitoredByJobType,
    JobComparatorType,
    JobStatusType,
    JobTypeType,
    LastRunErrorStatusCodeType,
    ListJobsFilterKeyType,
    ListJobsSortAttributeNameType,
    MacieStatusType,
    ManagedDataIdentifierSelectorType,
    OrderByType,
    OriginTypeType,
    RelationshipStatusType,
    RetrievalModeType,
    RevealRequestStatusType,
    RevealStatusType,
    ScopeFilterKeyType,
    SearchResourcesComparatorType,
    SearchResourcesSimpleCriterionKeyType,
    SearchResourcesSortAttributeNameType,
    SensitiveDataItemCategoryType,
    SeverityDescriptionType,
    SharedAccessType,
    SimpleCriterionKeyForJobType,
    StorageClassType,
    TimeRangeType,
    TypeType,
    UnavailabilityReasonCodeType,
    UsageStatisticsFilterComparatorType,
    UsageStatisticsFilterKeyType,
    UsageStatisticsSortKeyType,
    UsageTypeType,
    UserIdentityTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AcceptInvitationRequestRequestTypeDef",
    "AccessControlListTypeDef",
    "AccountDetailTypeDef",
    "BlockPublicAccessTypeDef",
    "AdminAccountTypeDef",
    "S3WordsListTypeDef",
    "AllowListStatusTypeDef",
    "AllowListSummaryTypeDef",
    "ApiCallDetailsTypeDef",
    "AutomatedDiscoveryAccountTypeDef",
    "AutomatedDiscoveryAccountUpdateErrorTypeDef",
    "AutomatedDiscoveryAccountUpdateTypeDef",
    "AwsAccountTypeDef",
    "AwsServiceTypeDef",
    "BatchGetCustomDataIdentifierSummaryTypeDef",
    "BatchGetCustomDataIdentifiersRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "BucketCountByEffectivePermissionTypeDef",
    "BucketCountByEncryptionTypeTypeDef",
    "BucketCountBySharedAccessTypeTypeDef",
    "BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef",
    "BucketCriteriaAdditionalPropertiesTypeDef",
    "BucketPolicyTypeDef",
    "BucketServerSideEncryptionTypeDef",
    "JobDetailsTypeDef",
    "KeyValuePairTypeDef",
    "ObjectCountByEncryptionTypeTypeDef",
    "ObjectLevelStatisticsTypeDef",
    "ReplicationDetailsTypeDef",
    "BucketSortCriteriaTypeDef",
    "SensitivityAggregationsTypeDef",
    "CellTypeDef",
    "S3DestinationTypeDef",
    "ClassificationResultStatusTypeDef",
    "ClassificationScopeSummaryTypeDef",
    "SeverityLevelTypeDef",
    "CreateInvitationsRequestRequestTypeDef",
    "UnprocessedAccountTypeDef",
    "CreateSampleFindingsRequestRequestTypeDef",
    "SimpleCriterionForJobOutputTypeDef",
    "CriterionAdditionalPropertiesOutputTypeDef",
    "CriterionAdditionalPropertiesTypeDef",
    "CustomDataIdentifierSummaryTypeDef",
    "DeclineInvitationsRequestRequestTypeDef",
    "DeleteAllowListRequestRequestTypeDef",
    "DeleteCustomDataIdentifierRequestRequestTypeDef",
    "DeleteFindingsFilterRequestRequestTypeDef",
    "DeleteInvitationsRequestRequestTypeDef",
    "DeleteMemberRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeClassificationJobRequestRequestTypeDef",
    "LastRunErrorStatusTypeDef",
    "StatisticsTypeDef",
    "UserPausedDetailsTypeDef",
    "DetectedDataDetailsTypeDef",
    "DetectionTypeDef",
    "DisableOrganizationAdminAccountRequestRequestTypeDef",
    "DisassociateMemberRequestRequestTypeDef",
    "DomainDetailsTypeDef",
    "EnableMacieRequestRequestTypeDef",
    "EnableOrganizationAdminAccountRequestRequestTypeDef",
    "FindingStatisticsSortCriteriaTypeDef",
    "SeverityTypeDef",
    "FindingsFilterListItemTypeDef",
    "InvitationTypeDef",
    "GetAllowListRequestRequestTypeDef",
    "GetBucketStatisticsRequestRequestTypeDef",
    "GetClassificationScopeRequestRequestTypeDef",
    "GetCustomDataIdentifierRequestRequestTypeDef",
    "GroupCountTypeDef",
    "GetFindingsFilterRequestRequestTypeDef",
    "SecurityHubConfigurationTypeDef",
    "SortCriteriaTypeDef",
    "GetMemberRequestRequestTypeDef",
    "GetResourceProfileRequestRequestTypeDef",
    "ResourceStatisticsTypeDef",
    "RetrievalConfigurationTypeDef",
    "RevealConfigurationTypeDef",
    "GetSensitiveDataOccurrencesAvailabilityRequestRequestTypeDef",
    "WaiterConfigTypeDef",
    "GetSensitiveDataOccurrencesRequestRequestTypeDef",
    "GetSensitivityInspectionTemplateRequestRequestTypeDef",
    "SensitivityInspectionTemplateExcludesOutputTypeDef",
    "SensitivityInspectionTemplateIncludesOutputTypeDef",
    "UsageStatisticsFilterTypeDef",
    "UsageStatisticsSortByTypeDef",
    "GetUsageTotalsRequestRequestTypeDef",
    "UsageTotalTypeDef",
    "IamUserTypeDef",
    "IpCityTypeDef",
    "IpCountryTypeDef",
    "IpGeoLocationTypeDef",
    "IpOwnerTypeDef",
    "MonthlyScheduleTypeDef",
    "WeeklyScheduleTypeDef",
    "SimpleScopeTermOutputTypeDef",
    "S3BucketDefinitionForJobOutputTypeDef",
    "ListAllowListsRequestRequestTypeDef",
    "ListAutomatedDiscoveryAccountsRequestRequestTypeDef",
    "ListJobsSortCriteriaTypeDef",
    "ListClassificationScopesRequestRequestTypeDef",
    "ListCustomDataIdentifiersRequestRequestTypeDef",
    "ListFindingsFiltersRequestRequestTypeDef",
    "ListInvitationsRequestRequestTypeDef",
    "ListJobsFilterTermTypeDef",
    "ListManagedDataIdentifiersRequestRequestTypeDef",
    "ManagedDataIdentifierSummaryTypeDef",
    "ListMembersRequestRequestTypeDef",
    "MemberTypeDef",
    "ListOrganizationAdminAccountsRequestRequestTypeDef",
    "ListResourceProfileArtifactsRequestRequestTypeDef",
    "ResourceProfileArtifactTypeDef",
    "ListResourceProfileDetectionsRequestRequestTypeDef",
    "ListSensitivityInspectionTemplatesRequestRequestTypeDef",
    "SensitivityInspectionTemplatesEntryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "RangeTypeDef",
    "RecordTypeDef",
    "S3BucketDefinitionForJobTypeDef",
    "S3BucketOwnerTypeDef",
    "ServerSideEncryptionTypeDef",
    "S3ClassificationScopeExclusionTypeDef",
    "S3ClassificationScopeExclusionUpdateTypeDef",
    "SearchResourcesSimpleCriterionTypeDef",
    "SearchResourcesSortCriteriaTypeDef",
    "SearchResourcesTagCriterionPairTypeDef",
    "SensitivityInspectionTemplateExcludesTypeDef",
    "SensitivityInspectionTemplateIncludesTypeDef",
    "ServiceLimitTypeDef",
    "SessionContextAttributesTypeDef",
    "SessionIssuerTypeDef",
    "SimpleCriterionForJobTypeDef",
    "SimpleScopeTermTypeDef",
    "SuppressDataIdentifierTypeDef",
    "TagCriterionPairForJobTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagValuePairTypeDef",
    "TestCustomDataIdentifierRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAutomatedDiscoveryConfigurationRequestRequestTypeDef",
    "UpdateClassificationJobRequestRequestTypeDef",
    "UpdateMacieSessionRequestRequestTypeDef",
    "UpdateMemberSessionRequestRequestTypeDef",
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
    "UpdateResourceProfileRequestRequestTypeDef",
    "UpdateRetrievalConfigurationTypeDef",
    "UserIdentityRootTypeDef",
    "CreateMemberRequestRequestTypeDef",
    "AccountLevelPermissionsTypeDef",
    "AllowListCriteriaTypeDef",
    "FindingActionTypeDef",
    "BatchUpdateAutomatedDiscoveryAccountsRequestRequestTypeDef",
    "BatchGetCustomDataIdentifiersResponseTypeDef",
    "BatchUpdateAutomatedDiscoveryAccountsResponseTypeDef",
    "CreateAllowListResponseTypeDef",
    "CreateClassificationJobResponseTypeDef",
    "CreateCustomDataIdentifierResponseTypeDef",
    "CreateFindingsFilterResponseTypeDef",
    "CreateMemberResponseTypeDef",
    "DescribeOrganizationConfigurationResponseTypeDef",
    "GetAutomatedDiscoveryConfigurationResponseTypeDef",
    "GetInvitationsCountResponseTypeDef",
    "GetMacieSessionResponseTypeDef",
    "GetMemberResponseTypeDef",
    "GetSensitiveDataOccurrencesAvailabilityResponseTypeDef",
    "ListAllowListsResponseTypeDef",
    "ListAutomatedDiscoveryAccountsResponseTypeDef",
    "ListFindingsResponseTypeDef",
    "ListOrganizationAdminAccountsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TestCustomDataIdentifierResponseTypeDef",
    "UpdateAllowListResponseTypeDef",
    "UpdateFindingsFilterResponseTypeDef",
    "BucketLevelPermissionsTypeDef",
    "MatchingBucketTypeDef",
    "DescribeBucketsRequestRequestTypeDef",
    "BucketStatisticsBySensitivityTypeDef",
    "ClassificationExportConfigurationTypeDef",
    "ListClassificationScopesResponseTypeDef",
    "CreateCustomDataIdentifierRequestRequestTypeDef",
    "GetCustomDataIdentifierResponseTypeDef",
    "CreateInvitationsResponseTypeDef",
    "DeclineInvitationsResponseTypeDef",
    "DeleteInvitationsResponseTypeDef",
    "FindingCriteriaOutputTypeDef",
    "CriterionAdditionalPropertiesUnionTypeDef",
    "ListCustomDataIdentifiersResponseTypeDef",
    "DescribeBucketsRequestDescribeBucketsPaginateTypeDef",
    "ListAllowListsRequestListAllowListsPaginateTypeDef",
    "ListAutomatedDiscoveryAccountsRequestListAutomatedDiscoveryAccountsPaginateTypeDef",
    "ListClassificationScopesRequestListClassificationScopesPaginateTypeDef",
    "ListCustomDataIdentifiersRequestListCustomDataIdentifiersPaginateTypeDef",
    "ListFindingsFiltersRequestListFindingsFiltersPaginateTypeDef",
    "ListInvitationsRequestListInvitationsPaginateTypeDef",
    "ListManagedDataIdentifiersRequestListManagedDataIdentifiersPaginateTypeDef",
    "ListMembersRequestListMembersPaginateTypeDef",
    "ListOrganizationAdminAccountsRequestListOrganizationAdminAccountsPaginateTypeDef",
    "ListResourceProfileArtifactsRequestListResourceProfileArtifactsPaginateTypeDef",
    "ListResourceProfileDetectionsRequestListResourceProfileDetectionsPaginateTypeDef",
    "ListSensitivityInspectionTemplatesRequestListSensitivityInspectionTemplatesPaginateTypeDef",
    "GetSensitiveDataOccurrencesResponseTypeDef",
    "ListResourceProfileDetectionsResponseTypeDef",
    "ListFindingsFiltersResponseTypeDef",
    "GetAdministratorAccountResponseTypeDef",
    "GetMasterAccountResponseTypeDef",
    "ListInvitationsResponseTypeDef",
    "GetFindingStatisticsResponseTypeDef",
    "GetFindingsPublicationConfigurationResponseTypeDef",
    "PutFindingsPublicationConfigurationRequestRequestTypeDef",
    "GetFindingsRequestRequestTypeDef",
    "GetResourceProfileResponseTypeDef",
    "GetRevealConfigurationResponseTypeDef",
    "UpdateRevealConfigurationResponseTypeDef",
    "GetSensitiveDataOccurrencesRequestFindingRevealedWaitTypeDef",
    "GetSensitivityInspectionTemplateResponseTypeDef",
    "GetUsageStatisticsRequestGetUsageStatisticsPaginateTypeDef",
    "GetUsageStatisticsRequestRequestTypeDef",
    "GetUsageTotalsResponseTypeDef",
    "IpAddressDetailsTypeDef",
    "JobScheduleFrequencyOutputTypeDef",
    "JobScheduleFrequencyTypeDef",
    "ListJobsFilterCriteriaTypeDef",
    "ListManagedDataIdentifiersResponseTypeDef",
    "ListMembersResponseTypeDef",
    "ListResourceProfileArtifactsResponseTypeDef",
    "ListSensitivityInspectionTemplatesResponseTypeDef",
    "PageTypeDef",
    "S3BucketDefinitionForJobUnionTypeDef",
    "S3ObjectTypeDef",
    "S3ClassificationScopeTypeDef",
    "S3ClassificationScopeUpdateTypeDef",
    "SearchResourcesTagCriterionTypeDef",
    "UpdateSensitivityInspectionTemplateRequestRequestTypeDef",
    "UsageByAccountTypeDef",
    "SessionContextTypeDef",
    "SimpleCriterionForJobUnionTypeDef",
    "SimpleScopeTermUnionTypeDef",
    "UpdateResourceProfileDetectionsRequestRequestTypeDef",
    "TagCriterionForJobOutputTypeDef",
    "TagCriterionForJobTypeDef",
    "TagScopeTermOutputTypeDef",
    "TagScopeTermTypeDef",
    "UpdateRevealConfigurationRequestRequestTypeDef",
    "CreateAllowListRequestRequestTypeDef",
    "GetAllowListResponseTypeDef",
    "UpdateAllowListRequestRequestTypeDef",
    "BucketPermissionConfigurationTypeDef",
    "MatchingResourceTypeDef",
    "GetBucketStatisticsResponseTypeDef",
    "GetClassificationExportConfigurationResponseTypeDef",
    "PutClassificationExportConfigurationRequestRequestTypeDef",
    "PutClassificationExportConfigurationResponseTypeDef",
    "GetFindingsFilterResponseTypeDef",
    "FindingCriteriaTypeDef",
    "ListClassificationJobsRequestListClassificationJobsPaginateTypeDef",
    "ListClassificationJobsRequestRequestTypeDef",
    "OccurrencesTypeDef",
    "GetClassificationScopeResponseTypeDef",
    "UpdateClassificationScopeRequestRequestTypeDef",
    "SearchResourcesCriteriaTypeDef",
    "UsageRecordTypeDef",
    "AssumedRoleTypeDef",
    "FederatedUserTypeDef",
    "CriteriaForJobOutputTypeDef",
    "TagCriterionForJobUnionTypeDef",
    "JobScopeTermOutputTypeDef",
    "TagScopeTermUnionTypeDef",
    "BucketPublicAccessTypeDef",
    "SearchResourcesResponseTypeDef",
    "CreateFindingsFilterRequestRequestTypeDef",
    "GetFindingStatisticsRequestRequestTypeDef",
    "ListFindingsRequestListFindingsPaginateTypeDef",
    "ListFindingsRequestRequestTypeDef",
    "UpdateFindingsFilterRequestRequestTypeDef",
    "CustomDetectionTypeDef",
    "DefaultDetectionTypeDef",
    "SearchResourcesCriteriaBlockTypeDef",
    "GetUsageStatisticsResponseTypeDef",
    "UserIdentityTypeDef",
    "CriteriaBlockForJobOutputTypeDef",
    "CriteriaForJobTypeDef",
    "JobScopingBlockOutputTypeDef",
    "JobScopeTermTypeDef",
    "BucketMetadataTypeDef",
    "S3BucketTypeDef",
    "CustomDataIdentifiersTypeDef",
    "SensitiveDataItemTypeDef",
    "SearchResourcesBucketCriteriaTypeDef",
    "FindingActorTypeDef",
    "S3BucketCriteriaForJobOutputTypeDef",
    "CriteriaForJobUnionTypeDef",
    "ScopingOutputTypeDef",
    "JobScopeTermUnionTypeDef",
    "DescribeBucketsResponseTypeDef",
    "ResourcesAffectedTypeDef",
    "ClassificationResultTypeDef",
    "SearchResourcesRequestRequestTypeDef",
    "SearchResourcesRequestSearchResourcesPaginateTypeDef",
    "PolicyDetailsTypeDef",
    "JobSummaryTypeDef",
    "CriteriaBlockForJobTypeDef",
    "S3JobDefinitionOutputTypeDef",
    "JobScopingBlockTypeDef",
    "ClassificationDetailsTypeDef",
    "ListClassificationJobsResponseTypeDef",
    "CriteriaBlockForJobUnionTypeDef",
    "DescribeClassificationJobResponseTypeDef",
    "JobScopingBlockUnionTypeDef",
    "FindingTypeDef",
    "S3BucketCriteriaForJobTypeDef",
    "ScopingTypeDef",
    "GetFindingsResponseTypeDef",
    "S3BucketCriteriaForJobUnionTypeDef",
    "ScopingUnionTypeDef",
    "S3JobDefinitionTypeDef",
    "CreateClassificationJobRequestRequestTypeDef",
)

AcceptInvitationRequestRequestTypeDef = TypedDict(
    "AcceptInvitationRequestRequestTypeDef",
    {
        "invitationId": str,
        "administratorAccountId": NotRequired[str],
        "masterAccount": NotRequired[str],
    },
)
AccessControlListTypeDef = TypedDict(
    "AccessControlListTypeDef",
    {
        "allowsPublicReadAccess": NotRequired[bool],
        "allowsPublicWriteAccess": NotRequired[bool],
    },
)
AccountDetailTypeDef = TypedDict(
    "AccountDetailTypeDef",
    {
        "accountId": str,
        "email": str,
    },
)
BlockPublicAccessTypeDef = TypedDict(
    "BlockPublicAccessTypeDef",
    {
        "blockPublicAcls": NotRequired[bool],
        "blockPublicPolicy": NotRequired[bool],
        "ignorePublicAcls": NotRequired[bool],
        "restrictPublicBuckets": NotRequired[bool],
    },
)
AdminAccountTypeDef = TypedDict(
    "AdminAccountTypeDef",
    {
        "accountId": NotRequired[str],
        "status": NotRequired[AdminStatusType],
    },
)
S3WordsListTypeDef = TypedDict(
    "S3WordsListTypeDef",
    {
        "bucketName": str,
        "objectKey": str,
    },
)
AllowListStatusTypeDef = TypedDict(
    "AllowListStatusTypeDef",
    {
        "code": AllowListStatusCodeType,
        "description": NotRequired[str],
    },
)
AllowListSummaryTypeDef = TypedDict(
    "AllowListSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "description": NotRequired[str],
        "id": NotRequired[str],
        "name": NotRequired[str],
        "updatedAt": NotRequired[datetime],
    },
)
ApiCallDetailsTypeDef = TypedDict(
    "ApiCallDetailsTypeDef",
    {
        "api": NotRequired[str],
        "apiServiceName": NotRequired[str],
        "firstSeen": NotRequired[datetime],
        "lastSeen": NotRequired[datetime],
    },
)
AutomatedDiscoveryAccountTypeDef = TypedDict(
    "AutomatedDiscoveryAccountTypeDef",
    {
        "accountId": NotRequired[str],
        "status": NotRequired[AutomatedDiscoveryAccountStatusType],
    },
)
AutomatedDiscoveryAccountUpdateErrorTypeDef = TypedDict(
    "AutomatedDiscoveryAccountUpdateErrorTypeDef",
    {
        "accountId": NotRequired[str],
        "errorCode": NotRequired[AutomatedDiscoveryAccountUpdateErrorCodeType],
    },
)
AutomatedDiscoveryAccountUpdateTypeDef = TypedDict(
    "AutomatedDiscoveryAccountUpdateTypeDef",
    {
        "accountId": NotRequired[str],
        "status": NotRequired[AutomatedDiscoveryAccountStatusType],
    },
)
AwsAccountTypeDef = TypedDict(
    "AwsAccountTypeDef",
    {
        "accountId": NotRequired[str],
        "principalId": NotRequired[str],
    },
)
AwsServiceTypeDef = TypedDict(
    "AwsServiceTypeDef",
    {
        "invokedBy": NotRequired[str],
    },
)
BatchGetCustomDataIdentifierSummaryTypeDef = TypedDict(
    "BatchGetCustomDataIdentifierSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "deleted": NotRequired[bool],
        "description": NotRequired[str],
        "id": NotRequired[str],
        "name": NotRequired[str],
    },
)
BatchGetCustomDataIdentifiersRequestRequestTypeDef = TypedDict(
    "BatchGetCustomDataIdentifiersRequestRequestTypeDef",
    {
        "ids": NotRequired[Sequence[str]],
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
BucketCountByEffectivePermissionTypeDef = TypedDict(
    "BucketCountByEffectivePermissionTypeDef",
    {
        "publiclyAccessible": NotRequired[int],
        "publiclyReadable": NotRequired[int],
        "publiclyWritable": NotRequired[int],
        "unknown": NotRequired[int],
    },
)
BucketCountByEncryptionTypeTypeDef = TypedDict(
    "BucketCountByEncryptionTypeTypeDef",
    {
        "kmsManaged": NotRequired[int],
        "s3Managed": NotRequired[int],
        "unencrypted": NotRequired[int],
        "unknown": NotRequired[int],
    },
)
BucketCountBySharedAccessTypeTypeDef = TypedDict(
    "BucketCountBySharedAccessTypeTypeDef",
    {
        "external": NotRequired[int],
        "internal": NotRequired[int],
        "notShared": NotRequired[int],
        "unknown": NotRequired[int],
    },
)
BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef = TypedDict(
    "BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef",
    {
        "allowsUnencryptedObjectUploads": NotRequired[int],
        "deniesUnencryptedObjectUploads": NotRequired[int],
        "unknown": NotRequired[int],
    },
)
BucketCriteriaAdditionalPropertiesTypeDef = TypedDict(
    "BucketCriteriaAdditionalPropertiesTypeDef",
    {
        "eq": NotRequired[Sequence[str]],
        "gt": NotRequired[int],
        "gte": NotRequired[int],
        "lt": NotRequired[int],
        "lte": NotRequired[int],
        "neq": NotRequired[Sequence[str]],
        "prefix": NotRequired[str],
    },
)
BucketPolicyTypeDef = TypedDict(
    "BucketPolicyTypeDef",
    {
        "allowsPublicReadAccess": NotRequired[bool],
        "allowsPublicWriteAccess": NotRequired[bool],
    },
)
BucketServerSideEncryptionTypeDef = TypedDict(
    "BucketServerSideEncryptionTypeDef",
    {
        "kmsMasterKeyId": NotRequired[str],
        "type": NotRequired[TypeType],
    },
)
JobDetailsTypeDef = TypedDict(
    "JobDetailsTypeDef",
    {
        "isDefinedInJob": NotRequired[IsDefinedInJobType],
        "isMonitoredByJob": NotRequired[IsMonitoredByJobType],
        "lastJobId": NotRequired[str],
        "lastJobRunTime": NotRequired[datetime],
    },
)
KeyValuePairTypeDef = TypedDict(
    "KeyValuePairTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[str],
    },
)
ObjectCountByEncryptionTypeTypeDef = TypedDict(
    "ObjectCountByEncryptionTypeTypeDef",
    {
        "customerManaged": NotRequired[int],
        "kmsManaged": NotRequired[int],
        "s3Managed": NotRequired[int],
        "unencrypted": NotRequired[int],
        "unknown": NotRequired[int],
    },
)
ObjectLevelStatisticsTypeDef = TypedDict(
    "ObjectLevelStatisticsTypeDef",
    {
        "fileType": NotRequired[int],
        "storageClass": NotRequired[int],
        "total": NotRequired[int],
    },
)
ReplicationDetailsTypeDef = TypedDict(
    "ReplicationDetailsTypeDef",
    {
        "replicated": NotRequired[bool],
        "replicatedExternally": NotRequired[bool],
        "replicationAccounts": NotRequired[List[str]],
    },
)
BucketSortCriteriaTypeDef = TypedDict(
    "BucketSortCriteriaTypeDef",
    {
        "attributeName": NotRequired[str],
        "orderBy": NotRequired[OrderByType],
    },
)
SensitivityAggregationsTypeDef = TypedDict(
    "SensitivityAggregationsTypeDef",
    {
        "classifiableSizeInBytes": NotRequired[int],
        "publiclyAccessibleCount": NotRequired[int],
        "totalCount": NotRequired[int],
        "totalSizeInBytes": NotRequired[int],
    },
)
CellTypeDef = TypedDict(
    "CellTypeDef",
    {
        "cellReference": NotRequired[str],
        "column": NotRequired[int],
        "columnName": NotRequired[str],
        "row": NotRequired[int],
    },
)
S3DestinationTypeDef = TypedDict(
    "S3DestinationTypeDef",
    {
        "bucketName": str,
        "kmsKeyArn": str,
        "keyPrefix": NotRequired[str],
    },
)
ClassificationResultStatusTypeDef = TypedDict(
    "ClassificationResultStatusTypeDef",
    {
        "code": NotRequired[str],
        "reason": NotRequired[str],
    },
)
ClassificationScopeSummaryTypeDef = TypedDict(
    "ClassificationScopeSummaryTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
    },
)
SeverityLevelTypeDef = TypedDict(
    "SeverityLevelTypeDef",
    {
        "occurrencesThreshold": int,
        "severity": DataIdentifierSeverityType,
    },
)
CreateInvitationsRequestRequestTypeDef = TypedDict(
    "CreateInvitationsRequestRequestTypeDef",
    {
        "accountIds": Sequence[str],
        "disableEmailNotification": NotRequired[bool],
        "message": NotRequired[str],
    },
)
UnprocessedAccountTypeDef = TypedDict(
    "UnprocessedAccountTypeDef",
    {
        "accountId": NotRequired[str],
        "errorCode": NotRequired[ErrorCodeType],
        "errorMessage": NotRequired[str],
    },
)
CreateSampleFindingsRequestRequestTypeDef = TypedDict(
    "CreateSampleFindingsRequestRequestTypeDef",
    {
        "findingTypes": NotRequired[Sequence[FindingTypeType]],
    },
)
SimpleCriterionForJobOutputTypeDef = TypedDict(
    "SimpleCriterionForJobOutputTypeDef",
    {
        "comparator": NotRequired[JobComparatorType],
        "key": NotRequired[SimpleCriterionKeyForJobType],
        "values": NotRequired[List[str]],
    },
)
CriterionAdditionalPropertiesOutputTypeDef = TypedDict(
    "CriterionAdditionalPropertiesOutputTypeDef",
    {
        "eq": NotRequired[List[str]],
        "eqExactMatch": NotRequired[List[str]],
        "gt": NotRequired[int],
        "gte": NotRequired[int],
        "lt": NotRequired[int],
        "lte": NotRequired[int],
        "neq": NotRequired[List[str]],
    },
)
CriterionAdditionalPropertiesTypeDef = TypedDict(
    "CriterionAdditionalPropertiesTypeDef",
    {
        "eq": NotRequired[Sequence[str]],
        "eqExactMatch": NotRequired[Sequence[str]],
        "gt": NotRequired[int],
        "gte": NotRequired[int],
        "lt": NotRequired[int],
        "lte": NotRequired[int],
        "neq": NotRequired[Sequence[str]],
    },
)
CustomDataIdentifierSummaryTypeDef = TypedDict(
    "CustomDataIdentifierSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "description": NotRequired[str],
        "id": NotRequired[str],
        "name": NotRequired[str],
    },
)
DeclineInvitationsRequestRequestTypeDef = TypedDict(
    "DeclineInvitationsRequestRequestTypeDef",
    {
        "accountIds": Sequence[str],
    },
)
DeleteAllowListRequestRequestTypeDef = TypedDict(
    "DeleteAllowListRequestRequestTypeDef",
    {
        "id": str,
        "ignoreJobChecks": NotRequired[str],
    },
)
DeleteCustomDataIdentifierRequestRequestTypeDef = TypedDict(
    "DeleteCustomDataIdentifierRequestRequestTypeDef",
    {
        "id": str,
    },
)
DeleteFindingsFilterRequestRequestTypeDef = TypedDict(
    "DeleteFindingsFilterRequestRequestTypeDef",
    {
        "id": str,
    },
)
DeleteInvitationsRequestRequestTypeDef = TypedDict(
    "DeleteInvitationsRequestRequestTypeDef",
    {
        "accountIds": Sequence[str],
    },
)
DeleteMemberRequestRequestTypeDef = TypedDict(
    "DeleteMemberRequestRequestTypeDef",
    {
        "id": str,
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
DescribeClassificationJobRequestRequestTypeDef = TypedDict(
    "DescribeClassificationJobRequestRequestTypeDef",
    {
        "jobId": str,
    },
)
LastRunErrorStatusTypeDef = TypedDict(
    "LastRunErrorStatusTypeDef",
    {
        "code": NotRequired[LastRunErrorStatusCodeType],
    },
)
StatisticsTypeDef = TypedDict(
    "StatisticsTypeDef",
    {
        "approximateNumberOfObjectsToProcess": NotRequired[float],
        "numberOfRuns": NotRequired[float],
    },
)
UserPausedDetailsTypeDef = TypedDict(
    "UserPausedDetailsTypeDef",
    {
        "jobExpiresAt": NotRequired[datetime],
        "jobImminentExpirationHealthEventArn": NotRequired[str],
        "jobPausedAt": NotRequired[datetime],
    },
)
DetectedDataDetailsTypeDef = TypedDict(
    "DetectedDataDetailsTypeDef",
    {
        "value": str,
    },
)
DetectionTypeDef = TypedDict(
    "DetectionTypeDef",
    {
        "arn": NotRequired[str],
        "count": NotRequired[int],
        "id": NotRequired[str],
        "name": NotRequired[str],
        "suppressed": NotRequired[bool],
        "type": NotRequired[DataIdentifierTypeType],
    },
)
DisableOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "DisableOrganizationAdminAccountRequestRequestTypeDef",
    {
        "adminAccountId": str,
    },
)
DisassociateMemberRequestRequestTypeDef = TypedDict(
    "DisassociateMemberRequestRequestTypeDef",
    {
        "id": str,
    },
)
DomainDetailsTypeDef = TypedDict(
    "DomainDetailsTypeDef",
    {
        "domainName": NotRequired[str],
    },
)
EnableMacieRequestRequestTypeDef = TypedDict(
    "EnableMacieRequestRequestTypeDef",
    {
        "clientToken": NotRequired[str],
        "findingPublishingFrequency": NotRequired[FindingPublishingFrequencyType],
        "status": NotRequired[MacieStatusType],
    },
)
EnableOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "EnableOrganizationAdminAccountRequestRequestTypeDef",
    {
        "adminAccountId": str,
        "clientToken": NotRequired[str],
    },
)
FindingStatisticsSortCriteriaTypeDef = TypedDict(
    "FindingStatisticsSortCriteriaTypeDef",
    {
        "attributeName": NotRequired[FindingStatisticsSortAttributeNameType],
        "orderBy": NotRequired[OrderByType],
    },
)
SeverityTypeDef = TypedDict(
    "SeverityTypeDef",
    {
        "description": NotRequired[SeverityDescriptionType],
        "score": NotRequired[int],
    },
)
FindingsFilterListItemTypeDef = TypedDict(
    "FindingsFilterListItemTypeDef",
    {
        "action": NotRequired[FindingsFilterActionType],
        "arn": NotRequired[str],
        "id": NotRequired[str],
        "name": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)
InvitationTypeDef = TypedDict(
    "InvitationTypeDef",
    {
        "accountId": NotRequired[str],
        "invitationId": NotRequired[str],
        "invitedAt": NotRequired[datetime],
        "relationshipStatus": NotRequired[RelationshipStatusType],
    },
)
GetAllowListRequestRequestTypeDef = TypedDict(
    "GetAllowListRequestRequestTypeDef",
    {
        "id": str,
    },
)
GetBucketStatisticsRequestRequestTypeDef = TypedDict(
    "GetBucketStatisticsRequestRequestTypeDef",
    {
        "accountId": NotRequired[str],
    },
)
GetClassificationScopeRequestRequestTypeDef = TypedDict(
    "GetClassificationScopeRequestRequestTypeDef",
    {
        "id": str,
    },
)
GetCustomDataIdentifierRequestRequestTypeDef = TypedDict(
    "GetCustomDataIdentifierRequestRequestTypeDef",
    {
        "id": str,
    },
)
GroupCountTypeDef = TypedDict(
    "GroupCountTypeDef",
    {
        "count": NotRequired[int],
        "groupKey": NotRequired[str],
    },
)
GetFindingsFilterRequestRequestTypeDef = TypedDict(
    "GetFindingsFilterRequestRequestTypeDef",
    {
        "id": str,
    },
)
SecurityHubConfigurationTypeDef = TypedDict(
    "SecurityHubConfigurationTypeDef",
    {
        "publishClassificationFindings": bool,
        "publishPolicyFindings": bool,
    },
)
SortCriteriaTypeDef = TypedDict(
    "SortCriteriaTypeDef",
    {
        "attributeName": NotRequired[str],
        "orderBy": NotRequired[OrderByType],
    },
)
GetMemberRequestRequestTypeDef = TypedDict(
    "GetMemberRequestRequestTypeDef",
    {
        "id": str,
    },
)
GetResourceProfileRequestRequestTypeDef = TypedDict(
    "GetResourceProfileRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
ResourceStatisticsTypeDef = TypedDict(
    "ResourceStatisticsTypeDef",
    {
        "totalBytesClassified": NotRequired[int],
        "totalDetections": NotRequired[int],
        "totalDetectionsSuppressed": NotRequired[int],
        "totalItemsClassified": NotRequired[int],
        "totalItemsSensitive": NotRequired[int],
        "totalItemsSkipped": NotRequired[int],
        "totalItemsSkippedInvalidEncryption": NotRequired[int],
        "totalItemsSkippedInvalidKms": NotRequired[int],
        "totalItemsSkippedPermissionDenied": NotRequired[int],
    },
)
RetrievalConfigurationTypeDef = TypedDict(
    "RetrievalConfigurationTypeDef",
    {
        "retrievalMode": RetrievalModeType,
        "externalId": NotRequired[str],
        "roleName": NotRequired[str],
    },
)
RevealConfigurationTypeDef = TypedDict(
    "RevealConfigurationTypeDef",
    {
        "status": RevealStatusType,
        "kmsKeyId": NotRequired[str],
    },
)
GetSensitiveDataOccurrencesAvailabilityRequestRequestTypeDef = TypedDict(
    "GetSensitiveDataOccurrencesAvailabilityRequestRequestTypeDef",
    {
        "findingId": str,
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
GetSensitiveDataOccurrencesRequestRequestTypeDef = TypedDict(
    "GetSensitiveDataOccurrencesRequestRequestTypeDef",
    {
        "findingId": str,
    },
)
GetSensitivityInspectionTemplateRequestRequestTypeDef = TypedDict(
    "GetSensitivityInspectionTemplateRequestRequestTypeDef",
    {
        "id": str,
    },
)
SensitivityInspectionTemplateExcludesOutputTypeDef = TypedDict(
    "SensitivityInspectionTemplateExcludesOutputTypeDef",
    {
        "managedDataIdentifierIds": NotRequired[List[str]],
    },
)
SensitivityInspectionTemplateIncludesOutputTypeDef = TypedDict(
    "SensitivityInspectionTemplateIncludesOutputTypeDef",
    {
        "allowListIds": NotRequired[List[str]],
        "customDataIdentifierIds": NotRequired[List[str]],
        "managedDataIdentifierIds": NotRequired[List[str]],
    },
)
UsageStatisticsFilterTypeDef = TypedDict(
    "UsageStatisticsFilterTypeDef",
    {
        "comparator": NotRequired[UsageStatisticsFilterComparatorType],
        "key": NotRequired[UsageStatisticsFilterKeyType],
        "values": NotRequired[Sequence[str]],
    },
)
UsageStatisticsSortByTypeDef = TypedDict(
    "UsageStatisticsSortByTypeDef",
    {
        "key": NotRequired[UsageStatisticsSortKeyType],
        "orderBy": NotRequired[OrderByType],
    },
)
GetUsageTotalsRequestRequestTypeDef = TypedDict(
    "GetUsageTotalsRequestRequestTypeDef",
    {
        "timeRange": NotRequired[str],
    },
)
UsageTotalTypeDef = TypedDict(
    "UsageTotalTypeDef",
    {
        "currency": NotRequired[Literal["USD"]],
        "estimatedCost": NotRequired[str],
        "type": NotRequired[UsageTypeType],
    },
)
IamUserTypeDef = TypedDict(
    "IamUserTypeDef",
    {
        "accountId": NotRequired[str],
        "arn": NotRequired[str],
        "principalId": NotRequired[str],
        "userName": NotRequired[str],
    },
)
IpCityTypeDef = TypedDict(
    "IpCityTypeDef",
    {
        "name": NotRequired[str],
    },
)
IpCountryTypeDef = TypedDict(
    "IpCountryTypeDef",
    {
        "code": NotRequired[str],
        "name": NotRequired[str],
    },
)
IpGeoLocationTypeDef = TypedDict(
    "IpGeoLocationTypeDef",
    {
        "lat": NotRequired[float],
        "lon": NotRequired[float],
    },
)
IpOwnerTypeDef = TypedDict(
    "IpOwnerTypeDef",
    {
        "asn": NotRequired[str],
        "asnOrg": NotRequired[str],
        "isp": NotRequired[str],
        "org": NotRequired[str],
    },
)
MonthlyScheduleTypeDef = TypedDict(
    "MonthlyScheduleTypeDef",
    {
        "dayOfMonth": NotRequired[int],
    },
)
WeeklyScheduleTypeDef = TypedDict(
    "WeeklyScheduleTypeDef",
    {
        "dayOfWeek": NotRequired[DayOfWeekType],
    },
)
SimpleScopeTermOutputTypeDef = TypedDict(
    "SimpleScopeTermOutputTypeDef",
    {
        "comparator": NotRequired[JobComparatorType],
        "key": NotRequired[ScopeFilterKeyType],
        "values": NotRequired[List[str]],
    },
)
S3BucketDefinitionForJobOutputTypeDef = TypedDict(
    "S3BucketDefinitionForJobOutputTypeDef",
    {
        "accountId": str,
        "buckets": List[str],
    },
)
ListAllowListsRequestRequestTypeDef = TypedDict(
    "ListAllowListsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListAutomatedDiscoveryAccountsRequestRequestTypeDef = TypedDict(
    "ListAutomatedDiscoveryAccountsRequestRequestTypeDef",
    {
        "accountIds": NotRequired[Sequence[str]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListJobsSortCriteriaTypeDef = TypedDict(
    "ListJobsSortCriteriaTypeDef",
    {
        "attributeName": NotRequired[ListJobsSortAttributeNameType],
        "orderBy": NotRequired[OrderByType],
    },
)
ListClassificationScopesRequestRequestTypeDef = TypedDict(
    "ListClassificationScopesRequestRequestTypeDef",
    {
        "name": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)
ListCustomDataIdentifiersRequestRequestTypeDef = TypedDict(
    "ListCustomDataIdentifiersRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListFindingsFiltersRequestRequestTypeDef = TypedDict(
    "ListFindingsFiltersRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListInvitationsRequestRequestTypeDef = TypedDict(
    "ListInvitationsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListJobsFilterTermTypeDef = TypedDict(
    "ListJobsFilterTermTypeDef",
    {
        "comparator": NotRequired[JobComparatorType],
        "key": NotRequired[ListJobsFilterKeyType],
        "values": NotRequired[Sequence[str]],
    },
)
ListManagedDataIdentifiersRequestRequestTypeDef = TypedDict(
    "ListManagedDataIdentifiersRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
    },
)
ManagedDataIdentifierSummaryTypeDef = TypedDict(
    "ManagedDataIdentifierSummaryTypeDef",
    {
        "category": NotRequired[SensitiveDataItemCategoryType],
        "id": NotRequired[str],
    },
)
ListMembersRequestRequestTypeDef = TypedDict(
    "ListMembersRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "onlyAssociated": NotRequired[str],
    },
)
MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "accountId": NotRequired[str],
        "administratorAccountId": NotRequired[str],
        "arn": NotRequired[str],
        "email": NotRequired[str],
        "invitedAt": NotRequired[datetime],
        "masterAccountId": NotRequired[str],
        "relationshipStatus": NotRequired[RelationshipStatusType],
        "tags": NotRequired[Dict[str, str]],
        "updatedAt": NotRequired[datetime],
    },
)
ListOrganizationAdminAccountsRequestRequestTypeDef = TypedDict(
    "ListOrganizationAdminAccountsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListResourceProfileArtifactsRequestRequestTypeDef = TypedDict(
    "ListResourceProfileArtifactsRequestRequestTypeDef",
    {
        "resourceArn": str,
        "nextToken": NotRequired[str],
    },
)
ResourceProfileArtifactTypeDef = TypedDict(
    "ResourceProfileArtifactTypeDef",
    {
        "arn": str,
        "classificationResultStatus": str,
        "sensitive": NotRequired[bool],
    },
)
ListResourceProfileDetectionsRequestRequestTypeDef = TypedDict(
    "ListResourceProfileDetectionsRequestRequestTypeDef",
    {
        "resourceArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListSensitivityInspectionTemplatesRequestRequestTypeDef = TypedDict(
    "ListSensitivityInspectionTemplatesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
SensitivityInspectionTemplatesEntryTypeDef = TypedDict(
    "SensitivityInspectionTemplatesEntryTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
RangeTypeDef = TypedDict(
    "RangeTypeDef",
    {
        "end": NotRequired[int],
        "start": NotRequired[int],
        "startColumn": NotRequired[int],
    },
)
RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "jsonPath": NotRequired[str],
        "recordIndex": NotRequired[int],
    },
)
S3BucketDefinitionForJobTypeDef = TypedDict(
    "S3BucketDefinitionForJobTypeDef",
    {
        "accountId": str,
        "buckets": Sequence[str],
    },
)
S3BucketOwnerTypeDef = TypedDict(
    "S3BucketOwnerTypeDef",
    {
        "displayName": NotRequired[str],
        "id": NotRequired[str],
    },
)
ServerSideEncryptionTypeDef = TypedDict(
    "ServerSideEncryptionTypeDef",
    {
        "encryptionType": NotRequired[EncryptionTypeType],
        "kmsMasterKeyId": NotRequired[str],
    },
)
S3ClassificationScopeExclusionTypeDef = TypedDict(
    "S3ClassificationScopeExclusionTypeDef",
    {
        "bucketNames": List[str],
    },
)
S3ClassificationScopeExclusionUpdateTypeDef = TypedDict(
    "S3ClassificationScopeExclusionUpdateTypeDef",
    {
        "bucketNames": Sequence[str],
        "operation": ClassificationScopeUpdateOperationType,
    },
)
SearchResourcesSimpleCriterionTypeDef = TypedDict(
    "SearchResourcesSimpleCriterionTypeDef",
    {
        "comparator": NotRequired[SearchResourcesComparatorType],
        "key": NotRequired[SearchResourcesSimpleCriterionKeyType],
        "values": NotRequired[Sequence[str]],
    },
)
SearchResourcesSortCriteriaTypeDef = TypedDict(
    "SearchResourcesSortCriteriaTypeDef",
    {
        "attributeName": NotRequired[SearchResourcesSortAttributeNameType],
        "orderBy": NotRequired[OrderByType],
    },
)
SearchResourcesTagCriterionPairTypeDef = TypedDict(
    "SearchResourcesTagCriterionPairTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[str],
    },
)
SensitivityInspectionTemplateExcludesTypeDef = TypedDict(
    "SensitivityInspectionTemplateExcludesTypeDef",
    {
        "managedDataIdentifierIds": NotRequired[Sequence[str]],
    },
)
SensitivityInspectionTemplateIncludesTypeDef = TypedDict(
    "SensitivityInspectionTemplateIncludesTypeDef",
    {
        "allowListIds": NotRequired[Sequence[str]],
        "customDataIdentifierIds": NotRequired[Sequence[str]],
        "managedDataIdentifierIds": NotRequired[Sequence[str]],
    },
)
ServiceLimitTypeDef = TypedDict(
    "ServiceLimitTypeDef",
    {
        "isServiceLimited": NotRequired[bool],
        "unit": NotRequired[Literal["TERABYTES"]],
        "value": NotRequired[int],
    },
)
SessionContextAttributesTypeDef = TypedDict(
    "SessionContextAttributesTypeDef",
    {
        "creationDate": NotRequired[datetime],
        "mfaAuthenticated": NotRequired[bool],
    },
)
SessionIssuerTypeDef = TypedDict(
    "SessionIssuerTypeDef",
    {
        "accountId": NotRequired[str],
        "arn": NotRequired[str],
        "principalId": NotRequired[str],
        "type": NotRequired[str],
        "userName": NotRequired[str],
    },
)
SimpleCriterionForJobTypeDef = TypedDict(
    "SimpleCriterionForJobTypeDef",
    {
        "comparator": NotRequired[JobComparatorType],
        "key": NotRequired[SimpleCriterionKeyForJobType],
        "values": NotRequired[Sequence[str]],
    },
)
SimpleScopeTermTypeDef = TypedDict(
    "SimpleScopeTermTypeDef",
    {
        "comparator": NotRequired[JobComparatorType],
        "key": NotRequired[ScopeFilterKeyType],
        "values": NotRequired[Sequence[str]],
    },
)
SuppressDataIdentifierTypeDef = TypedDict(
    "SuppressDataIdentifierTypeDef",
    {
        "id": NotRequired[str],
        "type": NotRequired[DataIdentifierTypeType],
    },
)
TagCriterionPairForJobTypeDef = TypedDict(
    "TagCriterionPairForJobTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[str],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)
TagValuePairTypeDef = TypedDict(
    "TagValuePairTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[str],
    },
)
TestCustomDataIdentifierRequestRequestTypeDef = TypedDict(
    "TestCustomDataIdentifierRequestRequestTypeDef",
    {
        "regex": str,
        "sampleText": str,
        "ignoreWords": NotRequired[Sequence[str]],
        "keywords": NotRequired[Sequence[str]],
        "maximumMatchDistance": NotRequired[int],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UpdateAutomatedDiscoveryConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateAutomatedDiscoveryConfigurationRequestRequestTypeDef",
    {
        "status": AutomatedDiscoveryStatusType,
        "autoEnableOrganizationMembers": NotRequired[AutoEnableModeType],
    },
)
UpdateClassificationJobRequestRequestTypeDef = TypedDict(
    "UpdateClassificationJobRequestRequestTypeDef",
    {
        "jobId": str,
        "jobStatus": JobStatusType,
    },
)
UpdateMacieSessionRequestRequestTypeDef = TypedDict(
    "UpdateMacieSessionRequestRequestTypeDef",
    {
        "findingPublishingFrequency": NotRequired[FindingPublishingFrequencyType],
        "status": NotRequired[MacieStatusType],
    },
)
UpdateMemberSessionRequestRequestTypeDef = TypedDict(
    "UpdateMemberSessionRequestRequestTypeDef",
    {
        "id": str,
        "status": MacieStatusType,
    },
)
UpdateOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
    {
        "autoEnable": bool,
    },
)
UpdateResourceProfileRequestRequestTypeDef = TypedDict(
    "UpdateResourceProfileRequestRequestTypeDef",
    {
        "resourceArn": str,
        "sensitivityScoreOverride": NotRequired[int],
    },
)
UpdateRetrievalConfigurationTypeDef = TypedDict(
    "UpdateRetrievalConfigurationTypeDef",
    {
        "retrievalMode": RetrievalModeType,
        "roleName": NotRequired[str],
    },
)
UserIdentityRootTypeDef = TypedDict(
    "UserIdentityRootTypeDef",
    {
        "accountId": NotRequired[str],
        "arn": NotRequired[str],
        "principalId": NotRequired[str],
    },
)
CreateMemberRequestRequestTypeDef = TypedDict(
    "CreateMemberRequestRequestTypeDef",
    {
        "account": AccountDetailTypeDef,
        "tags": NotRequired[Mapping[str, str]],
    },
)
AccountLevelPermissionsTypeDef = TypedDict(
    "AccountLevelPermissionsTypeDef",
    {
        "blockPublicAccess": NotRequired[BlockPublicAccessTypeDef],
    },
)
AllowListCriteriaTypeDef = TypedDict(
    "AllowListCriteriaTypeDef",
    {
        "regex": NotRequired[str],
        "s3WordsList": NotRequired[S3WordsListTypeDef],
    },
)
FindingActionTypeDef = TypedDict(
    "FindingActionTypeDef",
    {
        "actionType": NotRequired[Literal["AWS_API_CALL"]],
        "apiCallDetails": NotRequired[ApiCallDetailsTypeDef],
    },
)
BatchUpdateAutomatedDiscoveryAccountsRequestRequestTypeDef = TypedDict(
    "BatchUpdateAutomatedDiscoveryAccountsRequestRequestTypeDef",
    {
        "accounts": NotRequired[Sequence[AutomatedDiscoveryAccountUpdateTypeDef]],
    },
)
BatchGetCustomDataIdentifiersResponseTypeDef = TypedDict(
    "BatchGetCustomDataIdentifiersResponseTypeDef",
    {
        "customDataIdentifiers": List[BatchGetCustomDataIdentifierSummaryTypeDef],
        "notFoundIdentifierIds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchUpdateAutomatedDiscoveryAccountsResponseTypeDef = TypedDict(
    "BatchUpdateAutomatedDiscoveryAccountsResponseTypeDef",
    {
        "errors": List[AutomatedDiscoveryAccountUpdateErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAllowListResponseTypeDef = TypedDict(
    "CreateAllowListResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateClassificationJobResponseTypeDef = TypedDict(
    "CreateClassificationJobResponseTypeDef",
    {
        "jobArn": str,
        "jobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCustomDataIdentifierResponseTypeDef = TypedDict(
    "CreateCustomDataIdentifierResponseTypeDef",
    {
        "customDataIdentifierId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFindingsFilterResponseTypeDef = TypedDict(
    "CreateFindingsFilterResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMemberResponseTypeDef = TypedDict(
    "CreateMemberResponseTypeDef",
    {
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeOrganizationConfigurationResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigurationResponseTypeDef",
    {
        "autoEnable": bool,
        "maxAccountLimitReached": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAutomatedDiscoveryConfigurationResponseTypeDef = TypedDict(
    "GetAutomatedDiscoveryConfigurationResponseTypeDef",
    {
        "autoEnableOrganizationMembers": AutoEnableModeType,
        "classificationScopeId": str,
        "disabledAt": datetime,
        "firstEnabledAt": datetime,
        "lastUpdatedAt": datetime,
        "sensitivityInspectionTemplateId": str,
        "status": AutomatedDiscoveryStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetInvitationsCountResponseTypeDef = TypedDict(
    "GetInvitationsCountResponseTypeDef",
    {
        "invitationsCount": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMacieSessionResponseTypeDef = TypedDict(
    "GetMacieSessionResponseTypeDef",
    {
        "createdAt": datetime,
        "findingPublishingFrequency": FindingPublishingFrequencyType,
        "serviceRole": str,
        "status": MacieStatusType,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMemberResponseTypeDef = TypedDict(
    "GetMemberResponseTypeDef",
    {
        "accountId": str,
        "administratorAccountId": str,
        "arn": str,
        "email": str,
        "invitedAt": datetime,
        "masterAccountId": str,
        "relationshipStatus": RelationshipStatusType,
        "tags": Dict[str, str],
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSensitiveDataOccurrencesAvailabilityResponseTypeDef = TypedDict(
    "GetSensitiveDataOccurrencesAvailabilityResponseTypeDef",
    {
        "code": AvailabilityCodeType,
        "reasons": List[UnavailabilityReasonCodeType],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAllowListsResponseTypeDef = TypedDict(
    "ListAllowListsResponseTypeDef",
    {
        "allowLists": List[AllowListSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAutomatedDiscoveryAccountsResponseTypeDef = TypedDict(
    "ListAutomatedDiscoveryAccountsResponseTypeDef",
    {
        "items": List[AutomatedDiscoveryAccountTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListFindingsResponseTypeDef = TypedDict(
    "ListFindingsResponseTypeDef",
    {
        "findingIds": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListOrganizationAdminAccountsResponseTypeDef = TypedDict(
    "ListOrganizationAdminAccountsResponseTypeDef",
    {
        "adminAccounts": List[AdminAccountTypeDef],
        "nextToken": str,
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
TestCustomDataIdentifierResponseTypeDef = TypedDict(
    "TestCustomDataIdentifierResponseTypeDef",
    {
        "matchCount": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAllowListResponseTypeDef = TypedDict(
    "UpdateAllowListResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFindingsFilterResponseTypeDef = TypedDict(
    "UpdateFindingsFilterResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BucketLevelPermissionsTypeDef = TypedDict(
    "BucketLevelPermissionsTypeDef",
    {
        "accessControlList": NotRequired[AccessControlListTypeDef],
        "blockPublicAccess": NotRequired[BlockPublicAccessTypeDef],
        "bucketPolicy": NotRequired[BucketPolicyTypeDef],
    },
)
MatchingBucketTypeDef = TypedDict(
    "MatchingBucketTypeDef",
    {
        "accountId": NotRequired[str],
        "automatedDiscoveryMonitoringStatus": NotRequired[AutomatedDiscoveryMonitoringStatusType],
        "bucketName": NotRequired[str],
        "classifiableObjectCount": NotRequired[int],
        "classifiableSizeInBytes": NotRequired[int],
        "errorCode": NotRequired[Literal["ACCESS_DENIED"]],
        "errorMessage": NotRequired[str],
        "jobDetails": NotRequired[JobDetailsTypeDef],
        "lastAutomatedDiscoveryTime": NotRequired[datetime],
        "objectCount": NotRequired[int],
        "objectCountByEncryptionType": NotRequired[ObjectCountByEncryptionTypeTypeDef],
        "sensitivityScore": NotRequired[int],
        "sizeInBytes": NotRequired[int],
        "sizeInBytesCompressed": NotRequired[int],
        "unclassifiableObjectCount": NotRequired[ObjectLevelStatisticsTypeDef],
        "unclassifiableObjectSizeInBytes": NotRequired[ObjectLevelStatisticsTypeDef],
    },
)
DescribeBucketsRequestRequestTypeDef = TypedDict(
    "DescribeBucketsRequestRequestTypeDef",
    {
        "criteria": NotRequired[Mapping[str, BucketCriteriaAdditionalPropertiesTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortCriteria": NotRequired[BucketSortCriteriaTypeDef],
    },
)
BucketStatisticsBySensitivityTypeDef = TypedDict(
    "BucketStatisticsBySensitivityTypeDef",
    {
        "classificationError": NotRequired[SensitivityAggregationsTypeDef],
        "notClassified": NotRequired[SensitivityAggregationsTypeDef],
        "notSensitive": NotRequired[SensitivityAggregationsTypeDef],
        "sensitive": NotRequired[SensitivityAggregationsTypeDef],
    },
)
ClassificationExportConfigurationTypeDef = TypedDict(
    "ClassificationExportConfigurationTypeDef",
    {
        "s3Destination": NotRequired[S3DestinationTypeDef],
    },
)
ListClassificationScopesResponseTypeDef = TypedDict(
    "ListClassificationScopesResponseTypeDef",
    {
        "classificationScopes": List[ClassificationScopeSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCustomDataIdentifierRequestRequestTypeDef = TypedDict(
    "CreateCustomDataIdentifierRequestRequestTypeDef",
    {
        "name": str,
        "regex": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "ignoreWords": NotRequired[Sequence[str]],
        "keywords": NotRequired[Sequence[str]],
        "maximumMatchDistance": NotRequired[int],
        "severityLevels": NotRequired[Sequence[SeverityLevelTypeDef]],
        "tags": NotRequired[Mapping[str, str]],
    },
)
GetCustomDataIdentifierResponseTypeDef = TypedDict(
    "GetCustomDataIdentifierResponseTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deleted": bool,
        "description": str,
        "id": str,
        "ignoreWords": List[str],
        "keywords": List[str],
        "maximumMatchDistance": int,
        "name": str,
        "regex": str,
        "severityLevels": List[SeverityLevelTypeDef],
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateInvitationsResponseTypeDef = TypedDict(
    "CreateInvitationsResponseTypeDef",
    {
        "unprocessedAccounts": List[UnprocessedAccountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeclineInvitationsResponseTypeDef = TypedDict(
    "DeclineInvitationsResponseTypeDef",
    {
        "unprocessedAccounts": List[UnprocessedAccountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteInvitationsResponseTypeDef = TypedDict(
    "DeleteInvitationsResponseTypeDef",
    {
        "unprocessedAccounts": List[UnprocessedAccountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FindingCriteriaOutputTypeDef = TypedDict(
    "FindingCriteriaOutputTypeDef",
    {
        "criterion": NotRequired[Dict[str, CriterionAdditionalPropertiesOutputTypeDef]],
    },
)
CriterionAdditionalPropertiesUnionTypeDef = Union[
    CriterionAdditionalPropertiesTypeDef, CriterionAdditionalPropertiesOutputTypeDef
]
ListCustomDataIdentifiersResponseTypeDef = TypedDict(
    "ListCustomDataIdentifiersResponseTypeDef",
    {
        "items": List[CustomDataIdentifierSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeBucketsRequestDescribeBucketsPaginateTypeDef = TypedDict(
    "DescribeBucketsRequestDescribeBucketsPaginateTypeDef",
    {
        "criteria": NotRequired[Mapping[str, BucketCriteriaAdditionalPropertiesTypeDef]],
        "sortCriteria": NotRequired[BucketSortCriteriaTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAllowListsRequestListAllowListsPaginateTypeDef = TypedDict(
    "ListAllowListsRequestListAllowListsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAutomatedDiscoveryAccountsRequestListAutomatedDiscoveryAccountsPaginateTypeDef = TypedDict(
    "ListAutomatedDiscoveryAccountsRequestListAutomatedDiscoveryAccountsPaginateTypeDef",
    {
        "accountIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListClassificationScopesRequestListClassificationScopesPaginateTypeDef = TypedDict(
    "ListClassificationScopesRequestListClassificationScopesPaginateTypeDef",
    {
        "name": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCustomDataIdentifiersRequestListCustomDataIdentifiersPaginateTypeDef = TypedDict(
    "ListCustomDataIdentifiersRequestListCustomDataIdentifiersPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFindingsFiltersRequestListFindingsFiltersPaginateTypeDef = TypedDict(
    "ListFindingsFiltersRequestListFindingsFiltersPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListInvitationsRequestListInvitationsPaginateTypeDef = TypedDict(
    "ListInvitationsRequestListInvitationsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListManagedDataIdentifiersRequestListManagedDataIdentifiersPaginateTypeDef = TypedDict(
    "ListManagedDataIdentifiersRequestListManagedDataIdentifiersPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMembersRequestListMembersPaginateTypeDef = TypedDict(
    "ListMembersRequestListMembersPaginateTypeDef",
    {
        "onlyAssociated": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOrganizationAdminAccountsRequestListOrganizationAdminAccountsPaginateTypeDef = TypedDict(
    "ListOrganizationAdminAccountsRequestListOrganizationAdminAccountsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResourceProfileArtifactsRequestListResourceProfileArtifactsPaginateTypeDef = TypedDict(
    "ListResourceProfileArtifactsRequestListResourceProfileArtifactsPaginateTypeDef",
    {
        "resourceArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResourceProfileDetectionsRequestListResourceProfileDetectionsPaginateTypeDef = TypedDict(
    "ListResourceProfileDetectionsRequestListResourceProfileDetectionsPaginateTypeDef",
    {
        "resourceArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSensitivityInspectionTemplatesRequestListSensitivityInspectionTemplatesPaginateTypeDef = TypedDict(
    "ListSensitivityInspectionTemplatesRequestListSensitivityInspectionTemplatesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetSensitiveDataOccurrencesResponseTypeDef = TypedDict(
    "GetSensitiveDataOccurrencesResponseTypeDef",
    {
        "error": str,
        "sensitiveDataOccurrences": Dict[str, List[DetectedDataDetailsTypeDef]],
        "status": RevealRequestStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListResourceProfileDetectionsResponseTypeDef = TypedDict(
    "ListResourceProfileDetectionsResponseTypeDef",
    {
        "detections": List[DetectionTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListFindingsFiltersResponseTypeDef = TypedDict(
    "ListFindingsFiltersResponseTypeDef",
    {
        "findingsFilterListItems": List[FindingsFilterListItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAdministratorAccountResponseTypeDef = TypedDict(
    "GetAdministratorAccountResponseTypeDef",
    {
        "administrator": InvitationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMasterAccountResponseTypeDef = TypedDict(
    "GetMasterAccountResponseTypeDef",
    {
        "master": InvitationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListInvitationsResponseTypeDef = TypedDict(
    "ListInvitationsResponseTypeDef",
    {
        "invitations": List[InvitationTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFindingStatisticsResponseTypeDef = TypedDict(
    "GetFindingStatisticsResponseTypeDef",
    {
        "countsByGroup": List[GroupCountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFindingsPublicationConfigurationResponseTypeDef = TypedDict(
    "GetFindingsPublicationConfigurationResponseTypeDef",
    {
        "securityHubConfiguration": SecurityHubConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutFindingsPublicationConfigurationRequestRequestTypeDef = TypedDict(
    "PutFindingsPublicationConfigurationRequestRequestTypeDef",
    {
        "clientToken": NotRequired[str],
        "securityHubConfiguration": NotRequired[SecurityHubConfigurationTypeDef],
    },
)
GetFindingsRequestRequestTypeDef = TypedDict(
    "GetFindingsRequestRequestTypeDef",
    {
        "findingIds": Sequence[str],
        "sortCriteria": NotRequired[SortCriteriaTypeDef],
    },
)
GetResourceProfileResponseTypeDef = TypedDict(
    "GetResourceProfileResponseTypeDef",
    {
        "profileUpdatedAt": datetime,
        "sensitivityScore": int,
        "sensitivityScoreOverridden": bool,
        "statistics": ResourceStatisticsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRevealConfigurationResponseTypeDef = TypedDict(
    "GetRevealConfigurationResponseTypeDef",
    {
        "configuration": RevealConfigurationTypeDef,
        "retrievalConfiguration": RetrievalConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRevealConfigurationResponseTypeDef = TypedDict(
    "UpdateRevealConfigurationResponseTypeDef",
    {
        "configuration": RevealConfigurationTypeDef,
        "retrievalConfiguration": RetrievalConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSensitiveDataOccurrencesRequestFindingRevealedWaitTypeDef = TypedDict(
    "GetSensitiveDataOccurrencesRequestFindingRevealedWaitTypeDef",
    {
        "findingId": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetSensitivityInspectionTemplateResponseTypeDef = TypedDict(
    "GetSensitivityInspectionTemplateResponseTypeDef",
    {
        "description": str,
        "excludes": SensitivityInspectionTemplateExcludesOutputTypeDef,
        "includes": SensitivityInspectionTemplateIncludesOutputTypeDef,
        "name": str,
        "sensitivityInspectionTemplateId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetUsageStatisticsRequestGetUsageStatisticsPaginateTypeDef = TypedDict(
    "GetUsageStatisticsRequestGetUsageStatisticsPaginateTypeDef",
    {
        "filterBy": NotRequired[Sequence[UsageStatisticsFilterTypeDef]],
        "sortBy": NotRequired[UsageStatisticsSortByTypeDef],
        "timeRange": NotRequired[TimeRangeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetUsageStatisticsRequestRequestTypeDef = TypedDict(
    "GetUsageStatisticsRequestRequestTypeDef",
    {
        "filterBy": NotRequired[Sequence[UsageStatisticsFilterTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortBy": NotRequired[UsageStatisticsSortByTypeDef],
        "timeRange": NotRequired[TimeRangeType],
    },
)
GetUsageTotalsResponseTypeDef = TypedDict(
    "GetUsageTotalsResponseTypeDef",
    {
        "timeRange": TimeRangeType,
        "usageTotals": List[UsageTotalTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IpAddressDetailsTypeDef = TypedDict(
    "IpAddressDetailsTypeDef",
    {
        "ipAddressV4": NotRequired[str],
        "ipCity": NotRequired[IpCityTypeDef],
        "ipCountry": NotRequired[IpCountryTypeDef],
        "ipGeoLocation": NotRequired[IpGeoLocationTypeDef],
        "ipOwner": NotRequired[IpOwnerTypeDef],
    },
)
JobScheduleFrequencyOutputTypeDef = TypedDict(
    "JobScheduleFrequencyOutputTypeDef",
    {
        "dailySchedule": NotRequired[Dict[str, Any]],
        "monthlySchedule": NotRequired[MonthlyScheduleTypeDef],
        "weeklySchedule": NotRequired[WeeklyScheduleTypeDef],
    },
)
JobScheduleFrequencyTypeDef = TypedDict(
    "JobScheduleFrequencyTypeDef",
    {
        "dailySchedule": NotRequired[Mapping[str, Any]],
        "monthlySchedule": NotRequired[MonthlyScheduleTypeDef],
        "weeklySchedule": NotRequired[WeeklyScheduleTypeDef],
    },
)
ListJobsFilterCriteriaTypeDef = TypedDict(
    "ListJobsFilterCriteriaTypeDef",
    {
        "excludes": NotRequired[Sequence[ListJobsFilterTermTypeDef]],
        "includes": NotRequired[Sequence[ListJobsFilterTermTypeDef]],
    },
)
ListManagedDataIdentifiersResponseTypeDef = TypedDict(
    "ListManagedDataIdentifiersResponseTypeDef",
    {
        "items": List[ManagedDataIdentifierSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListMembersResponseTypeDef = TypedDict(
    "ListMembersResponseTypeDef",
    {
        "members": List[MemberTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListResourceProfileArtifactsResponseTypeDef = TypedDict(
    "ListResourceProfileArtifactsResponseTypeDef",
    {
        "artifacts": List[ResourceProfileArtifactTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSensitivityInspectionTemplatesResponseTypeDef = TypedDict(
    "ListSensitivityInspectionTemplatesResponseTypeDef",
    {
        "nextToken": str,
        "sensitivityInspectionTemplates": List[SensitivityInspectionTemplatesEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PageTypeDef = TypedDict(
    "PageTypeDef",
    {
        "lineRange": NotRequired[RangeTypeDef],
        "offsetRange": NotRequired[RangeTypeDef],
        "pageNumber": NotRequired[int],
    },
)
S3BucketDefinitionForJobUnionTypeDef = Union[
    S3BucketDefinitionForJobTypeDef, S3BucketDefinitionForJobOutputTypeDef
]
S3ObjectTypeDef = TypedDict(
    "S3ObjectTypeDef",
    {
        "bucketArn": NotRequired[str],
        "eTag": NotRequired[str],
        "extension": NotRequired[str],
        "key": NotRequired[str],
        "lastModified": NotRequired[datetime],
        "path": NotRequired[str],
        "publicAccess": NotRequired[bool],
        "serverSideEncryption": NotRequired[ServerSideEncryptionTypeDef],
        "size": NotRequired[int],
        "storageClass": NotRequired[StorageClassType],
        "tags": NotRequired[List[KeyValuePairTypeDef]],
        "versionId": NotRequired[str],
    },
)
S3ClassificationScopeTypeDef = TypedDict(
    "S3ClassificationScopeTypeDef",
    {
        "excludes": S3ClassificationScopeExclusionTypeDef,
    },
)
S3ClassificationScopeUpdateTypeDef = TypedDict(
    "S3ClassificationScopeUpdateTypeDef",
    {
        "excludes": S3ClassificationScopeExclusionUpdateTypeDef,
    },
)
SearchResourcesTagCriterionTypeDef = TypedDict(
    "SearchResourcesTagCriterionTypeDef",
    {
        "comparator": NotRequired[SearchResourcesComparatorType],
        "tagValues": NotRequired[Sequence[SearchResourcesTagCriterionPairTypeDef]],
    },
)
UpdateSensitivityInspectionTemplateRequestRequestTypeDef = TypedDict(
    "UpdateSensitivityInspectionTemplateRequestRequestTypeDef",
    {
        "id": str,
        "description": NotRequired[str],
        "excludes": NotRequired[SensitivityInspectionTemplateExcludesTypeDef],
        "includes": NotRequired[SensitivityInspectionTemplateIncludesTypeDef],
    },
)
UsageByAccountTypeDef = TypedDict(
    "UsageByAccountTypeDef",
    {
        "currency": NotRequired[Literal["USD"]],
        "estimatedCost": NotRequired[str],
        "serviceLimit": NotRequired[ServiceLimitTypeDef],
        "type": NotRequired[UsageTypeType],
    },
)
SessionContextTypeDef = TypedDict(
    "SessionContextTypeDef",
    {
        "attributes": NotRequired[SessionContextAttributesTypeDef],
        "sessionIssuer": NotRequired[SessionIssuerTypeDef],
    },
)
SimpleCriterionForJobUnionTypeDef = Union[
    SimpleCriterionForJobTypeDef, SimpleCriterionForJobOutputTypeDef
]
SimpleScopeTermUnionTypeDef = Union[SimpleScopeTermTypeDef, SimpleScopeTermOutputTypeDef]
UpdateResourceProfileDetectionsRequestRequestTypeDef = TypedDict(
    "UpdateResourceProfileDetectionsRequestRequestTypeDef",
    {
        "resourceArn": str,
        "suppressDataIdentifiers": NotRequired[Sequence[SuppressDataIdentifierTypeDef]],
    },
)
TagCriterionForJobOutputTypeDef = TypedDict(
    "TagCriterionForJobOutputTypeDef",
    {
        "comparator": NotRequired[JobComparatorType],
        "tagValues": NotRequired[List[TagCriterionPairForJobTypeDef]],
    },
)
TagCriterionForJobTypeDef = TypedDict(
    "TagCriterionForJobTypeDef",
    {
        "comparator": NotRequired[JobComparatorType],
        "tagValues": NotRequired[Sequence[TagCriterionPairForJobTypeDef]],
    },
)
TagScopeTermOutputTypeDef = TypedDict(
    "TagScopeTermOutputTypeDef",
    {
        "comparator": NotRequired[JobComparatorType],
        "key": NotRequired[str],
        "tagValues": NotRequired[List[TagValuePairTypeDef]],
        "target": NotRequired[Literal["S3_OBJECT"]],
    },
)
TagScopeTermTypeDef = TypedDict(
    "TagScopeTermTypeDef",
    {
        "comparator": NotRequired[JobComparatorType],
        "key": NotRequired[str],
        "tagValues": NotRequired[Sequence[TagValuePairTypeDef]],
        "target": NotRequired[Literal["S3_OBJECT"]],
    },
)
UpdateRevealConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateRevealConfigurationRequestRequestTypeDef",
    {
        "configuration": RevealConfigurationTypeDef,
        "retrievalConfiguration": NotRequired[UpdateRetrievalConfigurationTypeDef],
    },
)
CreateAllowListRequestRequestTypeDef = TypedDict(
    "CreateAllowListRequestRequestTypeDef",
    {
        "clientToken": str,
        "criteria": AllowListCriteriaTypeDef,
        "name": str,
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
GetAllowListResponseTypeDef = TypedDict(
    "GetAllowListResponseTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "criteria": AllowListCriteriaTypeDef,
        "description": str,
        "id": str,
        "name": str,
        "status": AllowListStatusTypeDef,
        "tags": Dict[str, str],
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAllowListRequestRequestTypeDef = TypedDict(
    "UpdateAllowListRequestRequestTypeDef",
    {
        "criteria": AllowListCriteriaTypeDef,
        "id": str,
        "name": str,
        "description": NotRequired[str],
    },
)
BucketPermissionConfigurationTypeDef = TypedDict(
    "BucketPermissionConfigurationTypeDef",
    {
        "accountLevelPermissions": NotRequired[AccountLevelPermissionsTypeDef],
        "bucketLevelPermissions": NotRequired[BucketLevelPermissionsTypeDef],
    },
)
MatchingResourceTypeDef = TypedDict(
    "MatchingResourceTypeDef",
    {
        "matchingBucket": NotRequired[MatchingBucketTypeDef],
    },
)
GetBucketStatisticsResponseTypeDef = TypedDict(
    "GetBucketStatisticsResponseTypeDef",
    {
        "bucketCount": int,
        "bucketCountByEffectivePermission": BucketCountByEffectivePermissionTypeDef,
        "bucketCountByEncryptionType": BucketCountByEncryptionTypeTypeDef,
        "bucketCountByObjectEncryptionRequirement": BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef,
        "bucketCountBySharedAccessType": BucketCountBySharedAccessTypeTypeDef,
        "bucketStatisticsBySensitivity": BucketStatisticsBySensitivityTypeDef,
        "classifiableObjectCount": int,
        "classifiableSizeInBytes": int,
        "lastUpdated": datetime,
        "objectCount": int,
        "sizeInBytes": int,
        "sizeInBytesCompressed": int,
        "unclassifiableObjectCount": ObjectLevelStatisticsTypeDef,
        "unclassifiableObjectSizeInBytes": ObjectLevelStatisticsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetClassificationExportConfigurationResponseTypeDef = TypedDict(
    "GetClassificationExportConfigurationResponseTypeDef",
    {
        "configuration": ClassificationExportConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutClassificationExportConfigurationRequestRequestTypeDef = TypedDict(
    "PutClassificationExportConfigurationRequestRequestTypeDef",
    {
        "configuration": ClassificationExportConfigurationTypeDef,
    },
)
PutClassificationExportConfigurationResponseTypeDef = TypedDict(
    "PutClassificationExportConfigurationResponseTypeDef",
    {
        "configuration": ClassificationExportConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFindingsFilterResponseTypeDef = TypedDict(
    "GetFindingsFilterResponseTypeDef",
    {
        "action": FindingsFilterActionType,
        "arn": str,
        "description": str,
        "findingCriteria": FindingCriteriaOutputTypeDef,
        "id": str,
        "name": str,
        "position": int,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FindingCriteriaTypeDef = TypedDict(
    "FindingCriteriaTypeDef",
    {
        "criterion": NotRequired[Mapping[str, CriterionAdditionalPropertiesUnionTypeDef]],
    },
)
ListClassificationJobsRequestListClassificationJobsPaginateTypeDef = TypedDict(
    "ListClassificationJobsRequestListClassificationJobsPaginateTypeDef",
    {
        "filterCriteria": NotRequired[ListJobsFilterCriteriaTypeDef],
        "sortCriteria": NotRequired[ListJobsSortCriteriaTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListClassificationJobsRequestRequestTypeDef = TypedDict(
    "ListClassificationJobsRequestRequestTypeDef",
    {
        "filterCriteria": NotRequired[ListJobsFilterCriteriaTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortCriteria": NotRequired[ListJobsSortCriteriaTypeDef],
    },
)
OccurrencesTypeDef = TypedDict(
    "OccurrencesTypeDef",
    {
        "cells": NotRequired[List[CellTypeDef]],
        "lineRanges": NotRequired[List[RangeTypeDef]],
        "offsetRanges": NotRequired[List[RangeTypeDef]],
        "pages": NotRequired[List[PageTypeDef]],
        "records": NotRequired[List[RecordTypeDef]],
    },
)
GetClassificationScopeResponseTypeDef = TypedDict(
    "GetClassificationScopeResponseTypeDef",
    {
        "id": str,
        "name": str,
        "s3": S3ClassificationScopeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateClassificationScopeRequestRequestTypeDef = TypedDict(
    "UpdateClassificationScopeRequestRequestTypeDef",
    {
        "id": str,
        "s3": NotRequired[S3ClassificationScopeUpdateTypeDef],
    },
)
SearchResourcesCriteriaTypeDef = TypedDict(
    "SearchResourcesCriteriaTypeDef",
    {
        "simpleCriterion": NotRequired[SearchResourcesSimpleCriterionTypeDef],
        "tagCriterion": NotRequired[SearchResourcesTagCriterionTypeDef],
    },
)
UsageRecordTypeDef = TypedDict(
    "UsageRecordTypeDef",
    {
        "accountId": NotRequired[str],
        "automatedDiscoveryFreeTrialStartDate": NotRequired[datetime],
        "freeTrialStartDate": NotRequired[datetime],
        "usage": NotRequired[List[UsageByAccountTypeDef]],
    },
)
AssumedRoleTypeDef = TypedDict(
    "AssumedRoleTypeDef",
    {
        "accessKeyId": NotRequired[str],
        "accountId": NotRequired[str],
        "arn": NotRequired[str],
        "principalId": NotRequired[str],
        "sessionContext": NotRequired[SessionContextTypeDef],
    },
)
FederatedUserTypeDef = TypedDict(
    "FederatedUserTypeDef",
    {
        "accessKeyId": NotRequired[str],
        "accountId": NotRequired[str],
        "arn": NotRequired[str],
        "principalId": NotRequired[str],
        "sessionContext": NotRequired[SessionContextTypeDef],
    },
)
CriteriaForJobOutputTypeDef = TypedDict(
    "CriteriaForJobOutputTypeDef",
    {
        "simpleCriterion": NotRequired[SimpleCriterionForJobOutputTypeDef],
        "tagCriterion": NotRequired[TagCriterionForJobOutputTypeDef],
    },
)
TagCriterionForJobUnionTypeDef = Union[TagCriterionForJobTypeDef, TagCriterionForJobOutputTypeDef]
JobScopeTermOutputTypeDef = TypedDict(
    "JobScopeTermOutputTypeDef",
    {
        "simpleScopeTerm": NotRequired[SimpleScopeTermOutputTypeDef],
        "tagScopeTerm": NotRequired[TagScopeTermOutputTypeDef],
    },
)
TagScopeTermUnionTypeDef = Union[TagScopeTermTypeDef, TagScopeTermOutputTypeDef]
BucketPublicAccessTypeDef = TypedDict(
    "BucketPublicAccessTypeDef",
    {
        "effectivePermission": NotRequired[EffectivePermissionType],
        "permissionConfiguration": NotRequired[BucketPermissionConfigurationTypeDef],
    },
)
SearchResourcesResponseTypeDef = TypedDict(
    "SearchResourcesResponseTypeDef",
    {
        "matchingResources": List[MatchingResourceTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFindingsFilterRequestRequestTypeDef = TypedDict(
    "CreateFindingsFilterRequestRequestTypeDef",
    {
        "action": FindingsFilterActionType,
        "findingCriteria": FindingCriteriaTypeDef,
        "name": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "position": NotRequired[int],
        "tags": NotRequired[Mapping[str, str]],
    },
)
GetFindingStatisticsRequestRequestTypeDef = TypedDict(
    "GetFindingStatisticsRequestRequestTypeDef",
    {
        "groupBy": GroupByType,
        "findingCriteria": NotRequired[FindingCriteriaTypeDef],
        "size": NotRequired[int],
        "sortCriteria": NotRequired[FindingStatisticsSortCriteriaTypeDef],
    },
)
ListFindingsRequestListFindingsPaginateTypeDef = TypedDict(
    "ListFindingsRequestListFindingsPaginateTypeDef",
    {
        "findingCriteria": NotRequired[FindingCriteriaTypeDef],
        "sortCriteria": NotRequired[SortCriteriaTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFindingsRequestRequestTypeDef = TypedDict(
    "ListFindingsRequestRequestTypeDef",
    {
        "findingCriteria": NotRequired[FindingCriteriaTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortCriteria": NotRequired[SortCriteriaTypeDef],
    },
)
UpdateFindingsFilterRequestRequestTypeDef = TypedDict(
    "UpdateFindingsFilterRequestRequestTypeDef",
    {
        "id": str,
        "action": NotRequired[FindingsFilterActionType],
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "findingCriteria": NotRequired[FindingCriteriaTypeDef],
        "name": NotRequired[str],
        "position": NotRequired[int],
    },
)
CustomDetectionTypeDef = TypedDict(
    "CustomDetectionTypeDef",
    {
        "arn": NotRequired[str],
        "count": NotRequired[int],
        "name": NotRequired[str],
        "occurrences": NotRequired[OccurrencesTypeDef],
    },
)
DefaultDetectionTypeDef = TypedDict(
    "DefaultDetectionTypeDef",
    {
        "count": NotRequired[int],
        "occurrences": NotRequired[OccurrencesTypeDef],
        "type": NotRequired[str],
    },
)
SearchResourcesCriteriaBlockTypeDef = TypedDict(
    "SearchResourcesCriteriaBlockTypeDef",
    {
        "and": NotRequired[Sequence[SearchResourcesCriteriaTypeDef]],
    },
)
GetUsageStatisticsResponseTypeDef = TypedDict(
    "GetUsageStatisticsResponseTypeDef",
    {
        "nextToken": str,
        "records": List[UsageRecordTypeDef],
        "timeRange": TimeRangeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UserIdentityTypeDef = TypedDict(
    "UserIdentityTypeDef",
    {
        "assumedRole": NotRequired[AssumedRoleTypeDef],
        "awsAccount": NotRequired[AwsAccountTypeDef],
        "awsService": NotRequired[AwsServiceTypeDef],
        "federatedUser": NotRequired[FederatedUserTypeDef],
        "iamUser": NotRequired[IamUserTypeDef],
        "root": NotRequired[UserIdentityRootTypeDef],
        "type": NotRequired[UserIdentityTypeType],
    },
)
CriteriaBlockForJobOutputTypeDef = TypedDict(
    "CriteriaBlockForJobOutputTypeDef",
    {
        "and": NotRequired[List[CriteriaForJobOutputTypeDef]],
    },
)
CriteriaForJobTypeDef = TypedDict(
    "CriteriaForJobTypeDef",
    {
        "simpleCriterion": NotRequired[SimpleCriterionForJobUnionTypeDef],
        "tagCriterion": NotRequired[TagCriterionForJobUnionTypeDef],
    },
)
JobScopingBlockOutputTypeDef = TypedDict(
    "JobScopingBlockOutputTypeDef",
    {
        "and": NotRequired[List[JobScopeTermOutputTypeDef]],
    },
)
JobScopeTermTypeDef = TypedDict(
    "JobScopeTermTypeDef",
    {
        "simpleScopeTerm": NotRequired[SimpleScopeTermUnionTypeDef],
        "tagScopeTerm": NotRequired[TagScopeTermUnionTypeDef],
    },
)
BucketMetadataTypeDef = TypedDict(
    "BucketMetadataTypeDef",
    {
        "accountId": NotRequired[str],
        "allowsUnencryptedObjectUploads": NotRequired[AllowsUnencryptedObjectUploadsType],
        "automatedDiscoveryMonitoringStatus": NotRequired[AutomatedDiscoveryMonitoringStatusType],
        "bucketArn": NotRequired[str],
        "bucketCreatedAt": NotRequired[datetime],
        "bucketName": NotRequired[str],
        "classifiableObjectCount": NotRequired[int],
        "classifiableSizeInBytes": NotRequired[int],
        "errorCode": NotRequired[Literal["ACCESS_DENIED"]],
        "errorMessage": NotRequired[str],
        "jobDetails": NotRequired[JobDetailsTypeDef],
        "lastAutomatedDiscoveryTime": NotRequired[datetime],
        "lastUpdated": NotRequired[datetime],
        "objectCount": NotRequired[int],
        "objectCountByEncryptionType": NotRequired[ObjectCountByEncryptionTypeTypeDef],
        "publicAccess": NotRequired[BucketPublicAccessTypeDef],
        "region": NotRequired[str],
        "replicationDetails": NotRequired[ReplicationDetailsTypeDef],
        "sensitivityScore": NotRequired[int],
        "serverSideEncryption": NotRequired[BucketServerSideEncryptionTypeDef],
        "sharedAccess": NotRequired[SharedAccessType],
        "sizeInBytes": NotRequired[int],
        "sizeInBytesCompressed": NotRequired[int],
        "tags": NotRequired[List[KeyValuePairTypeDef]],
        "unclassifiableObjectCount": NotRequired[ObjectLevelStatisticsTypeDef],
        "unclassifiableObjectSizeInBytes": NotRequired[ObjectLevelStatisticsTypeDef],
        "versioning": NotRequired[bool],
    },
)
S3BucketTypeDef = TypedDict(
    "S3BucketTypeDef",
    {
        "allowsUnencryptedObjectUploads": NotRequired[AllowsUnencryptedObjectUploadsType],
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "defaultServerSideEncryption": NotRequired[ServerSideEncryptionTypeDef],
        "name": NotRequired[str],
        "owner": NotRequired[S3BucketOwnerTypeDef],
        "publicAccess": NotRequired[BucketPublicAccessTypeDef],
        "tags": NotRequired[List[KeyValuePairTypeDef]],
    },
)
CustomDataIdentifiersTypeDef = TypedDict(
    "CustomDataIdentifiersTypeDef",
    {
        "detections": NotRequired[List[CustomDetectionTypeDef]],
        "totalCount": NotRequired[int],
    },
)
SensitiveDataItemTypeDef = TypedDict(
    "SensitiveDataItemTypeDef",
    {
        "category": NotRequired[SensitiveDataItemCategoryType],
        "detections": NotRequired[List[DefaultDetectionTypeDef]],
        "totalCount": NotRequired[int],
    },
)
SearchResourcesBucketCriteriaTypeDef = TypedDict(
    "SearchResourcesBucketCriteriaTypeDef",
    {
        "excludes": NotRequired[SearchResourcesCriteriaBlockTypeDef],
        "includes": NotRequired[SearchResourcesCriteriaBlockTypeDef],
    },
)
FindingActorTypeDef = TypedDict(
    "FindingActorTypeDef",
    {
        "domainDetails": NotRequired[DomainDetailsTypeDef],
        "ipAddressDetails": NotRequired[IpAddressDetailsTypeDef],
        "userIdentity": NotRequired[UserIdentityTypeDef],
    },
)
S3BucketCriteriaForJobOutputTypeDef = TypedDict(
    "S3BucketCriteriaForJobOutputTypeDef",
    {
        "excludes": NotRequired[CriteriaBlockForJobOutputTypeDef],
        "includes": NotRequired[CriteriaBlockForJobOutputTypeDef],
    },
)
CriteriaForJobUnionTypeDef = Union[CriteriaForJobTypeDef, CriteriaForJobOutputTypeDef]
ScopingOutputTypeDef = TypedDict(
    "ScopingOutputTypeDef",
    {
        "excludes": NotRequired[JobScopingBlockOutputTypeDef],
        "includes": NotRequired[JobScopingBlockOutputTypeDef],
    },
)
JobScopeTermUnionTypeDef = Union[JobScopeTermTypeDef, JobScopeTermOutputTypeDef]
DescribeBucketsResponseTypeDef = TypedDict(
    "DescribeBucketsResponseTypeDef",
    {
        "buckets": List[BucketMetadataTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResourcesAffectedTypeDef = TypedDict(
    "ResourcesAffectedTypeDef",
    {
        "s3Bucket": NotRequired[S3BucketTypeDef],
        "s3Object": NotRequired[S3ObjectTypeDef],
    },
)
ClassificationResultTypeDef = TypedDict(
    "ClassificationResultTypeDef",
    {
        "additionalOccurrences": NotRequired[bool],
        "customDataIdentifiers": NotRequired[CustomDataIdentifiersTypeDef],
        "mimeType": NotRequired[str],
        "sensitiveData": NotRequired[List[SensitiveDataItemTypeDef]],
        "sizeClassified": NotRequired[int],
        "status": NotRequired[ClassificationResultStatusTypeDef],
    },
)
SearchResourcesRequestRequestTypeDef = TypedDict(
    "SearchResourcesRequestRequestTypeDef",
    {
        "bucketCriteria": NotRequired[SearchResourcesBucketCriteriaTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortCriteria": NotRequired[SearchResourcesSortCriteriaTypeDef],
    },
)
SearchResourcesRequestSearchResourcesPaginateTypeDef = TypedDict(
    "SearchResourcesRequestSearchResourcesPaginateTypeDef",
    {
        "bucketCriteria": NotRequired[SearchResourcesBucketCriteriaTypeDef],
        "sortCriteria": NotRequired[SearchResourcesSortCriteriaTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
PolicyDetailsTypeDef = TypedDict(
    "PolicyDetailsTypeDef",
    {
        "action": NotRequired[FindingActionTypeDef],
        "actor": NotRequired[FindingActorTypeDef],
    },
)
JobSummaryTypeDef = TypedDict(
    "JobSummaryTypeDef",
    {
        "bucketCriteria": NotRequired[S3BucketCriteriaForJobOutputTypeDef],
        "bucketDefinitions": NotRequired[List[S3BucketDefinitionForJobOutputTypeDef]],
        "createdAt": NotRequired[datetime],
        "jobId": NotRequired[str],
        "jobStatus": NotRequired[JobStatusType],
        "jobType": NotRequired[JobTypeType],
        "lastRunErrorStatus": NotRequired[LastRunErrorStatusTypeDef],
        "name": NotRequired[str],
        "userPausedDetails": NotRequired[UserPausedDetailsTypeDef],
    },
)
CriteriaBlockForJobTypeDef = TypedDict(
    "CriteriaBlockForJobTypeDef",
    {
        "and": NotRequired[Sequence[CriteriaForJobUnionTypeDef]],
    },
)
S3JobDefinitionOutputTypeDef = TypedDict(
    "S3JobDefinitionOutputTypeDef",
    {
        "bucketCriteria": NotRequired[S3BucketCriteriaForJobOutputTypeDef],
        "bucketDefinitions": NotRequired[List[S3BucketDefinitionForJobOutputTypeDef]],
        "scoping": NotRequired[ScopingOutputTypeDef],
    },
)
JobScopingBlockTypeDef = TypedDict(
    "JobScopingBlockTypeDef",
    {
        "and": NotRequired[Sequence[JobScopeTermUnionTypeDef]],
    },
)
ClassificationDetailsTypeDef = TypedDict(
    "ClassificationDetailsTypeDef",
    {
        "detailedResultsLocation": NotRequired[str],
        "jobArn": NotRequired[str],
        "jobId": NotRequired[str],
        "originType": NotRequired[OriginTypeType],
        "result": NotRequired[ClassificationResultTypeDef],
    },
)
ListClassificationJobsResponseTypeDef = TypedDict(
    "ListClassificationJobsResponseTypeDef",
    {
        "items": List[JobSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CriteriaBlockForJobUnionTypeDef = Union[
    CriteriaBlockForJobTypeDef, CriteriaBlockForJobOutputTypeDef
]
DescribeClassificationJobResponseTypeDef = TypedDict(
    "DescribeClassificationJobResponseTypeDef",
    {
        "allowListIds": List[str],
        "clientToken": str,
        "createdAt": datetime,
        "customDataIdentifierIds": List[str],
        "description": str,
        "initialRun": bool,
        "jobArn": str,
        "jobId": str,
        "jobStatus": JobStatusType,
        "jobType": JobTypeType,
        "lastRunErrorStatus": LastRunErrorStatusTypeDef,
        "lastRunTime": datetime,
        "managedDataIdentifierIds": List[str],
        "managedDataIdentifierSelector": ManagedDataIdentifierSelectorType,
        "name": str,
        "s3JobDefinition": S3JobDefinitionOutputTypeDef,
        "samplingPercentage": int,
        "scheduleFrequency": JobScheduleFrequencyOutputTypeDef,
        "statistics": StatisticsTypeDef,
        "tags": Dict[str, str],
        "userPausedDetails": UserPausedDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
JobScopingBlockUnionTypeDef = Union[JobScopingBlockTypeDef, JobScopingBlockOutputTypeDef]
FindingTypeDef = TypedDict(
    "FindingTypeDef",
    {
        "accountId": NotRequired[str],
        "archived": NotRequired[bool],
        "category": NotRequired[FindingCategoryType],
        "classificationDetails": NotRequired[ClassificationDetailsTypeDef],
        "count": NotRequired[int],
        "createdAt": NotRequired[datetime],
        "description": NotRequired[str],
        "id": NotRequired[str],
        "partition": NotRequired[str],
        "policyDetails": NotRequired[PolicyDetailsTypeDef],
        "region": NotRequired[str],
        "resourcesAffected": NotRequired[ResourcesAffectedTypeDef],
        "sample": NotRequired[bool],
        "schemaVersion": NotRequired[str],
        "severity": NotRequired[SeverityTypeDef],
        "title": NotRequired[str],
        "type": NotRequired[FindingTypeType],
        "updatedAt": NotRequired[datetime],
    },
)
S3BucketCriteriaForJobTypeDef = TypedDict(
    "S3BucketCriteriaForJobTypeDef",
    {
        "excludes": NotRequired[CriteriaBlockForJobUnionTypeDef],
        "includes": NotRequired[CriteriaBlockForJobUnionTypeDef],
    },
)
ScopingTypeDef = TypedDict(
    "ScopingTypeDef",
    {
        "excludes": NotRequired[JobScopingBlockUnionTypeDef],
        "includes": NotRequired[JobScopingBlockUnionTypeDef],
    },
)
GetFindingsResponseTypeDef = TypedDict(
    "GetFindingsResponseTypeDef",
    {
        "findings": List[FindingTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
S3BucketCriteriaForJobUnionTypeDef = Union[
    S3BucketCriteriaForJobTypeDef, S3BucketCriteriaForJobOutputTypeDef
]
ScopingUnionTypeDef = Union[ScopingTypeDef, ScopingOutputTypeDef]
S3JobDefinitionTypeDef = TypedDict(
    "S3JobDefinitionTypeDef",
    {
        "bucketCriteria": NotRequired[S3BucketCriteriaForJobUnionTypeDef],
        "bucketDefinitions": NotRequired[Sequence[S3BucketDefinitionForJobUnionTypeDef]],
        "scoping": NotRequired[ScopingUnionTypeDef],
    },
)
CreateClassificationJobRequestRequestTypeDef = TypedDict(
    "CreateClassificationJobRequestRequestTypeDef",
    {
        "clientToken": str,
        "jobType": JobTypeType,
        "name": str,
        "s3JobDefinition": S3JobDefinitionTypeDef,
        "allowListIds": NotRequired[Sequence[str]],
        "customDataIdentifierIds": NotRequired[Sequence[str]],
        "description": NotRequired[str],
        "initialRun": NotRequired[bool],
        "managedDataIdentifierIds": NotRequired[Sequence[str]],
        "managedDataIdentifierSelector": NotRequired[ManagedDataIdentifierSelectorType],
        "samplingPercentage": NotRequired[int],
        "scheduleFrequency": NotRequired[JobScheduleFrequencyTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
