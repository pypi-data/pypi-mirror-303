"""
Type annotations for inspector2 service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/type_defs/)

Usage::

    ```python
    from mypy_boto3_inspector2.type_defs import SeverityCountsTypeDef

    data: SeverityCountsTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    AccountSortByType,
    AggregationFindingTypeType,
    AggregationResourceTypeType,
    AggregationTypeType,
    AmiSortByType,
    ArchitectureType,
    AwsEcrContainerSortByType,
    CisFindingStatusType,
    CisReportFormatType,
    CisReportStatusType,
    CisResultStatusType,
    CisRuleStatusType,
    CisScanConfigurationsSortByType,
    CisScanResultDetailsSortByType,
    CisScanResultsAggregatedByChecksSortByType,
    CisScanResultsAggregatedByTargetResourceSortByType,
    CisScanStatusType,
    CisSecurityLevelType,
    CisSortOrderType,
    CisStringComparisonType,
    CisTargetStatusReasonType,
    CisTargetStatusType,
    CodeSnippetErrorCodeType,
    CoverageResourceTypeType,
    CoverageStringComparisonType,
    DayType,
    DelegatedAdminStatusType,
    Ec2DeepInspectionStatusType,
    Ec2InstanceSortByType,
    Ec2PlatformType,
    Ec2ScanModeStatusType,
    Ec2ScanModeType,
    EcrPullDateRescanDurationType,
    EcrRescanDurationStatusType,
    EcrRescanDurationType,
    EcrScanFrequencyType,
    ErrorCodeType,
    ExploitAvailableType,
    ExternalReportStatusType,
    FilterActionType,
    FindingDetailsErrorCodeType,
    FindingStatusType,
    FindingTypeSortByType,
    FindingTypeType,
    FixAvailableType,
    FreeTrialInfoErrorCodeType,
    FreeTrialStatusType,
    FreeTrialTypeType,
    GroupKeyType,
    ImageLayerSortByType,
    LambdaFunctionSortByType,
    LambdaLayerSortByType,
    ListCisScansDetailLevelType,
    ListCisScansSortByType,
    NetworkProtocolType,
    OperationType,
    PackageManagerType,
    PackageSortByType,
    PackageTypeType,
    RelationshipStatusType,
    ReportFormatType,
    ReportingErrorCodeType,
    RepositorySortByType,
    ResourceScanTypeType,
    ResourceStringComparisonType,
    ResourceTypeType,
    RuntimeType,
    SbomReportFormatType,
    ScanModeType,
    ScanStatusCodeType,
    ScanStatusReasonType,
    ScanTypeType,
    ServiceType,
    SeverityType,
    SortFieldType,
    SortOrderType,
    StatusType,
    StopCisSessionStatusType,
    StringComparisonType,
    TitleSortByType,
    UsageTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "SeverityCountsTypeDef",
    "AccountAggregationTypeDef",
    "StateTypeDef",
    "ResourceStatusTypeDef",
    "FindingTypeAggregationTypeDef",
    "StringFilterTypeDef",
    "AssociateMemberRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "AtigDataTypeDef",
    "AutoEnableTypeDef",
    "AwsEc2InstanceDetailsTypeDef",
    "AwsEcrContainerImageDetailsTypeDef",
    "LambdaVpcConfigTypeDef",
    "BatchGetAccountStatusRequestRequestTypeDef",
    "BatchGetCodeSnippetRequestRequestTypeDef",
    "CodeSnippetErrorTypeDef",
    "BatchGetFindingDetailsRequestRequestTypeDef",
    "FindingDetailsErrorTypeDef",
    "BatchGetFreeTrialInfoRequestRequestTypeDef",
    "FreeTrialInfoErrorTypeDef",
    "BatchGetMemberEc2DeepInspectionStatusRequestRequestTypeDef",
    "FailedMemberAccountEc2DeepInspectionStatusStateTypeDef",
    "MemberAccountEc2DeepInspectionStatusStateTypeDef",
    "MemberAccountEc2DeepInspectionStatusTypeDef",
    "BlobTypeDef",
    "CancelFindingsReportRequestRequestTypeDef",
    "CancelSbomExportRequestRequestTypeDef",
    "StatusCountsTypeDef",
    "TimestampTypeDef",
    "CisFindingStatusFilterTypeDef",
    "CisNumberFilterTypeDef",
    "CisResultStatusFilterTypeDef",
    "CisTargetsTypeDef",
    "CisSecurityLevelFilterTypeDef",
    "CisStringFilterTypeDef",
    "CisScanResultDetailsTypeDef",
    "CisTargetStatusFilterTypeDef",
    "CisTargetStatusReasonFilterTypeDef",
    "TagFilterTypeDef",
    "CisScanStatusFilterTypeDef",
    "CisaDataTypeDef",
    "CodeFilePathTypeDef",
    "CodeLineTypeDef",
    "SuggestedFixTypeDef",
    "ComputePlatformTypeDef",
    "CountsTypeDef",
    "CoverageMapFilterTypeDef",
    "CoverageStringFilterTypeDef",
    "ScanStatusTypeDef",
    "CreateCisTargetsTypeDef",
    "DestinationTypeDef",
    "Cvss2TypeDef",
    "Cvss3TypeDef",
    "CvssScoreAdjustmentTypeDef",
    "CvssScoreTypeDef",
    "TimeTypeDef",
    "DateFilterOutputTypeDef",
    "DelegatedAdminAccountTypeDef",
    "DelegatedAdminTypeDef",
    "DeleteCisScanConfigurationRequestRequestTypeDef",
    "DeleteFilterRequestRequestTypeDef",
    "DisableDelegatedAdminAccountRequestRequestTypeDef",
    "DisableRequestRequestTypeDef",
    "DisassociateMemberRequestRequestTypeDef",
    "Ec2ScanModeStateTypeDef",
    "Ec2ConfigurationTypeDef",
    "MapFilterTypeDef",
    "Ec2MetadataTypeDef",
    "EcrRescanDurationStateTypeDef",
    "EcrConfigurationTypeDef",
    "EcrContainerImageMetadataTypeDef",
    "EcrRepositoryMetadataTypeDef",
    "EnableDelegatedAdminAccountRequestRequestTypeDef",
    "EnableRequestRequestTypeDef",
    "EpssDetailsTypeDef",
    "EpssTypeDef",
    "EvidenceTypeDef",
    "ExploitObservedTypeDef",
    "ExploitabilityDetailsTypeDef",
    "NumberFilterTypeDef",
    "PortRangeFilterTypeDef",
    "FreeTrialInfoTypeDef",
    "GetCisScanReportRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "GetEncryptionKeyRequestRequestTypeDef",
    "GetFindingsReportStatusRequestRequestTypeDef",
    "GetMemberRequestRequestTypeDef",
    "MemberTypeDef",
    "GetSbomExportRequestRequestTypeDef",
    "LambdaFunctionMetadataTypeDef",
    "ListAccountPermissionsRequestRequestTypeDef",
    "PermissionTypeDef",
    "ListDelegatedAdminAccountsRequestRequestTypeDef",
    "ListFiltersRequestRequestTypeDef",
    "SortCriteriaTypeDef",
    "ListMembersRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListUsageTotalsRequestRequestTypeDef",
    "StepTypeDef",
    "PortRangeTypeDef",
    "VulnerablePackageTypeDef",
    "RecommendationTypeDef",
    "ResetEncryptionKeyRequestRequestTypeDef",
    "ResourceMapFilterTypeDef",
    "ResourceStringFilterTypeDef",
    "SearchVulnerabilitiesFilterCriteriaTypeDef",
    "SendCisSessionHealthRequestRequestTypeDef",
    "StartCisSessionMessageTypeDef",
    "StopCisMessageProgressTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateCisTargetsTypeDef",
    "UpdateEc2DeepInspectionConfigurationRequestRequestTypeDef",
    "UpdateEncryptionKeyRequestRequestTypeDef",
    "UpdateOrgEc2DeepInspectionConfigurationRequestRequestTypeDef",
    "UsageTypeDef",
    "AccountAggregationResponseTypeDef",
    "AmiAggregationResponseTypeDef",
    "AwsEcrContainerAggregationResponseTypeDef",
    "Ec2InstanceAggregationResponseTypeDef",
    "FindingTypeAggregationResponseTypeDef",
    "ImageLayerAggregationResponseTypeDef",
    "LambdaFunctionAggregationResponseTypeDef",
    "LambdaLayerAggregationResponseTypeDef",
    "PackageAggregationResponseTypeDef",
    "RepositoryAggregationResponseTypeDef",
    "TitleAggregationResponseTypeDef",
    "ResourceStateTypeDef",
    "AccountTypeDef",
    "FailedAccountTypeDef",
    "AmiAggregationTypeDef",
    "AwsEcrContainerAggregationTypeDef",
    "ImageLayerAggregationTypeDef",
    "LambdaLayerAggregationTypeDef",
    "PackageAggregationTypeDef",
    "RepositoryAggregationTypeDef",
    "TitleAggregationTypeDef",
    "AssociateMemberResponseTypeDef",
    "CancelFindingsReportResponseTypeDef",
    "CancelSbomExportResponseTypeDef",
    "CreateCisScanConfigurationResponseTypeDef",
    "CreateFilterResponseTypeDef",
    "CreateFindingsReportResponseTypeDef",
    "CreateSbomExportResponseTypeDef",
    "DeleteCisScanConfigurationResponseTypeDef",
    "DeleteFilterResponseTypeDef",
    "DisableDelegatedAdminAccountResponseTypeDef",
    "DisassociateMemberResponseTypeDef",
    "EnableDelegatedAdminAccountResponseTypeDef",
    "GetCisScanReportResponseTypeDef",
    "GetEc2DeepInspectionConfigurationResponseTypeDef",
    "GetEncryptionKeyResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "UpdateCisScanConfigurationResponseTypeDef",
    "UpdateEc2DeepInspectionConfigurationResponseTypeDef",
    "UpdateFilterResponseTypeDef",
    "DescribeOrganizationConfigurationResponseTypeDef",
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
    "UpdateOrganizationConfigurationResponseTypeDef",
    "AwsLambdaFunctionDetailsTypeDef",
    "BatchGetMemberEc2DeepInspectionStatusResponseTypeDef",
    "BatchUpdateMemberEc2DeepInspectionStatusResponseTypeDef",
    "BatchUpdateMemberEc2DeepInspectionStatusRequestRequestTypeDef",
    "CisSessionMessageTypeDef",
    "CisCheckAggregationTypeDef",
    "CisTargetResourceAggregationTypeDef",
    "CisDateFilterTypeDef",
    "CoverageDateFilterTypeDef",
    "DateFilterTypeDef",
    "CisScanTypeDef",
    "CisScanResultDetailsFilterCriteriaTypeDef",
    "CisScanResultsAggregatedByChecksFilterCriteriaTypeDef",
    "GetCisScanResultDetailsResponseTypeDef",
    "CisScanResultsAggregatedByTargetResourceFilterCriteriaTypeDef",
    "ListCisScanConfigurationsFilterCriteriaTypeDef",
    "CodeVulnerabilityDetailsTypeDef",
    "CodeSnippetResultTypeDef",
    "ListCoverageStatisticsResponseTypeDef",
    "CvssScoreDetailsTypeDef",
    "DailyScheduleTypeDef",
    "MonthlyScheduleTypeDef",
    "WeeklyScheduleOutputTypeDef",
    "WeeklyScheduleTypeDef",
    "ListDelegatedAdminAccountsResponseTypeDef",
    "GetDelegatedAdminAccountResponseTypeDef",
    "Ec2ConfigurationStateTypeDef",
    "Ec2InstanceAggregationTypeDef",
    "LambdaFunctionAggregationTypeDef",
    "EcrConfigurationStateTypeDef",
    "UpdateConfigurationRequestRequestTypeDef",
    "FindingDetailTypeDef",
    "VulnerabilityTypeDef",
    "PackageFilterTypeDef",
    "FreeTrialAccountInfoTypeDef",
    "ListAccountPermissionsRequestListAccountPermissionsPaginateTypeDef",
    "ListDelegatedAdminAccountsRequestListDelegatedAdminAccountsPaginateTypeDef",
    "ListFiltersRequestListFiltersPaginateTypeDef",
    "ListMembersRequestListMembersPaginateTypeDef",
    "ListUsageTotalsRequestListUsageTotalsPaginateTypeDef",
    "GetMemberResponseTypeDef",
    "ListMembersResponseTypeDef",
    "ResourceScanMetadataTypeDef",
    "ListAccountPermissionsResponseTypeDef",
    "NetworkPathTypeDef",
    "PackageVulnerabilityDetailsTypeDef",
    "RemediationTypeDef",
    "ResourceFilterCriteriaOutputTypeDef",
    "ResourceFilterCriteriaTypeDef",
    "SearchVulnerabilitiesRequestRequestTypeDef",
    "SearchVulnerabilitiesRequestSearchVulnerabilitiesPaginateTypeDef",
    "StartCisSessionRequestRequestTypeDef",
    "StopCisSessionMessageTypeDef",
    "UsageTotalTypeDef",
    "AggregationResponseTypeDef",
    "AccountStateTypeDef",
    "DisableResponseTypeDef",
    "EnableResponseTypeDef",
    "ResourceDetailsTypeDef",
    "SendCisSessionTelemetryRequestRequestTypeDef",
    "ListCisScanResultsAggregatedByChecksResponseTypeDef",
    "ListCisScanResultsAggregatedByTargetResourceResponseTypeDef",
    "ListCisScansFilterCriteriaTypeDef",
    "CoverageFilterCriteriaTypeDef",
    "DateFilterUnionTypeDef",
    "ListCisScansResponseTypeDef",
    "GetCisScanResultDetailsRequestGetCisScanResultDetailsPaginateTypeDef",
    "GetCisScanResultDetailsRequestRequestTypeDef",
    "ListCisScanResultsAggregatedByChecksRequestListCisScanResultsAggregatedByChecksPaginateTypeDef",
    "ListCisScanResultsAggregatedByChecksRequestRequestTypeDef",
    "ListCisScanResultsAggregatedByTargetResourceRequestListCisScanResultsAggregatedByTargetResourcePaginateTypeDef",
    "ListCisScanResultsAggregatedByTargetResourceRequestRequestTypeDef",
    "ListCisScanConfigurationsRequestListCisScanConfigurationsPaginateTypeDef",
    "ListCisScanConfigurationsRequestRequestTypeDef",
    "BatchGetCodeSnippetResponseTypeDef",
    "InspectorScoreDetailsTypeDef",
    "ScheduleOutputTypeDef",
    "WeeklyScheduleUnionTypeDef",
    "AggregationRequestTypeDef",
    "GetConfigurationResponseTypeDef",
    "BatchGetFindingDetailsResponseTypeDef",
    "SearchVulnerabilitiesResponseTypeDef",
    "FilterCriteriaOutputTypeDef",
    "BatchGetFreeTrialInfoResponseTypeDef",
    "CoveredResourceTypeDef",
    "NetworkReachabilityDetailsTypeDef",
    "GetSbomExportResponseTypeDef",
    "CreateSbomExportRequestRequestTypeDef",
    "StopCisSessionRequestRequestTypeDef",
    "ListUsageTotalsResponseTypeDef",
    "ListFindingAggregationsResponseTypeDef",
    "BatchGetAccountStatusResponseTypeDef",
    "ResourceTypeDef",
    "ListCisScansRequestListCisScansPaginateTypeDef",
    "ListCisScansRequestRequestTypeDef",
    "ListCoverageRequestListCoveragePaginateTypeDef",
    "ListCoverageRequestRequestTypeDef",
    "ListCoverageStatisticsRequestListCoverageStatisticsPaginateTypeDef",
    "ListCoverageStatisticsRequestRequestTypeDef",
    "FilterCriteriaTypeDef",
    "CisScanConfigurationTypeDef",
    "ScheduleTypeDef",
    "ListFindingAggregationsRequestListFindingAggregationsPaginateTypeDef",
    "ListFindingAggregationsRequestRequestTypeDef",
    "FilterTypeDef",
    "GetFindingsReportStatusResponseTypeDef",
    "ListCoverageResponseTypeDef",
    "FindingTypeDef",
    "CreateFilterRequestRequestTypeDef",
    "CreateFindingsReportRequestRequestTypeDef",
    "ListFindingsRequestListFindingsPaginateTypeDef",
    "ListFindingsRequestRequestTypeDef",
    "UpdateFilterRequestRequestTypeDef",
    "ListCisScanConfigurationsResponseTypeDef",
    "CreateCisScanConfigurationRequestRequestTypeDef",
    "UpdateCisScanConfigurationRequestRequestTypeDef",
    "ListFiltersResponseTypeDef",
    "ListFindingsResponseTypeDef",
)

SeverityCountsTypeDef = TypedDict(
    "SeverityCountsTypeDef",
    {
        "all": NotRequired[int],
        "critical": NotRequired[int],
        "high": NotRequired[int],
        "medium": NotRequired[int],
    },
)
AccountAggregationTypeDef = TypedDict(
    "AccountAggregationTypeDef",
    {
        "findingType": NotRequired[AggregationFindingTypeType],
        "resourceType": NotRequired[AggregationResourceTypeType],
        "sortBy": NotRequired[AccountSortByType],
        "sortOrder": NotRequired[SortOrderType],
    },
)
StateTypeDef = TypedDict(
    "StateTypeDef",
    {
        "errorCode": ErrorCodeType,
        "errorMessage": str,
        "status": StatusType,
    },
)
ResourceStatusTypeDef = TypedDict(
    "ResourceStatusTypeDef",
    {
        "ec2": StatusType,
        "ecr": StatusType,
        "lambda": NotRequired[StatusType],
        "lambdaCode": NotRequired[StatusType],
    },
)
FindingTypeAggregationTypeDef = TypedDict(
    "FindingTypeAggregationTypeDef",
    {
        "findingType": NotRequired[AggregationFindingTypeType],
        "resourceType": NotRequired[AggregationResourceTypeType],
        "sortBy": NotRequired[FindingTypeSortByType],
        "sortOrder": NotRequired[SortOrderType],
    },
)
StringFilterTypeDef = TypedDict(
    "StringFilterTypeDef",
    {
        "comparison": StringComparisonType,
        "value": str,
    },
)
AssociateMemberRequestRequestTypeDef = TypedDict(
    "AssociateMemberRequestRequestTypeDef",
    {
        "accountId": str,
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
AtigDataTypeDef = TypedDict(
    "AtigDataTypeDef",
    {
        "firstSeen": NotRequired[datetime],
        "lastSeen": NotRequired[datetime],
        "targets": NotRequired[List[str]],
        "ttps": NotRequired[List[str]],
    },
)
AutoEnableTypeDef = TypedDict(
    "AutoEnableTypeDef",
    {
        "ec2": bool,
        "ecr": bool,
        "lambda": NotRequired[bool],
        "lambdaCode": NotRequired[bool],
    },
)
AwsEc2InstanceDetailsTypeDef = TypedDict(
    "AwsEc2InstanceDetailsTypeDef",
    {
        "iamInstanceProfileArn": NotRequired[str],
        "imageId": NotRequired[str],
        "ipV4Addresses": NotRequired[List[str]],
        "ipV6Addresses": NotRequired[List[str]],
        "keyName": NotRequired[str],
        "launchedAt": NotRequired[datetime],
        "platform": NotRequired[str],
        "subnetId": NotRequired[str],
        "type": NotRequired[str],
        "vpcId": NotRequired[str],
    },
)
AwsEcrContainerImageDetailsTypeDef = TypedDict(
    "AwsEcrContainerImageDetailsTypeDef",
    {
        "imageHash": str,
        "registry": str,
        "repositoryName": str,
        "architecture": NotRequired[str],
        "author": NotRequired[str],
        "imageTags": NotRequired[List[str]],
        "platform": NotRequired[str],
        "pushedAt": NotRequired[datetime],
    },
)
LambdaVpcConfigTypeDef = TypedDict(
    "LambdaVpcConfigTypeDef",
    {
        "securityGroupIds": NotRequired[List[str]],
        "subnetIds": NotRequired[List[str]],
        "vpcId": NotRequired[str],
    },
)
BatchGetAccountStatusRequestRequestTypeDef = TypedDict(
    "BatchGetAccountStatusRequestRequestTypeDef",
    {
        "accountIds": NotRequired[Sequence[str]],
    },
)
BatchGetCodeSnippetRequestRequestTypeDef = TypedDict(
    "BatchGetCodeSnippetRequestRequestTypeDef",
    {
        "findingArns": Sequence[str],
    },
)
CodeSnippetErrorTypeDef = TypedDict(
    "CodeSnippetErrorTypeDef",
    {
        "errorCode": CodeSnippetErrorCodeType,
        "errorMessage": str,
        "findingArn": str,
    },
)
BatchGetFindingDetailsRequestRequestTypeDef = TypedDict(
    "BatchGetFindingDetailsRequestRequestTypeDef",
    {
        "findingArns": Sequence[str],
    },
)
FindingDetailsErrorTypeDef = TypedDict(
    "FindingDetailsErrorTypeDef",
    {
        "errorCode": FindingDetailsErrorCodeType,
        "errorMessage": str,
        "findingArn": str,
    },
)
BatchGetFreeTrialInfoRequestRequestTypeDef = TypedDict(
    "BatchGetFreeTrialInfoRequestRequestTypeDef",
    {
        "accountIds": Sequence[str],
    },
)
FreeTrialInfoErrorTypeDef = TypedDict(
    "FreeTrialInfoErrorTypeDef",
    {
        "accountId": str,
        "code": FreeTrialInfoErrorCodeType,
        "message": str,
    },
)
BatchGetMemberEc2DeepInspectionStatusRequestRequestTypeDef = TypedDict(
    "BatchGetMemberEc2DeepInspectionStatusRequestRequestTypeDef",
    {
        "accountIds": NotRequired[Sequence[str]],
    },
)
FailedMemberAccountEc2DeepInspectionStatusStateTypeDef = TypedDict(
    "FailedMemberAccountEc2DeepInspectionStatusStateTypeDef",
    {
        "accountId": str,
        "ec2ScanStatus": NotRequired[StatusType],
        "errorMessage": NotRequired[str],
    },
)
MemberAccountEc2DeepInspectionStatusStateTypeDef = TypedDict(
    "MemberAccountEc2DeepInspectionStatusStateTypeDef",
    {
        "accountId": str,
        "errorMessage": NotRequired[str],
        "status": NotRequired[Ec2DeepInspectionStatusType],
    },
)
MemberAccountEc2DeepInspectionStatusTypeDef = TypedDict(
    "MemberAccountEc2DeepInspectionStatusTypeDef",
    {
        "accountId": str,
        "activateDeepInspection": bool,
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
CancelFindingsReportRequestRequestTypeDef = TypedDict(
    "CancelFindingsReportRequestRequestTypeDef",
    {
        "reportId": str,
    },
)
CancelSbomExportRequestRequestTypeDef = TypedDict(
    "CancelSbomExportRequestRequestTypeDef",
    {
        "reportId": str,
    },
)
StatusCountsTypeDef = TypedDict(
    "StatusCountsTypeDef",
    {
        "failed": NotRequired[int],
        "passed": NotRequired[int],
        "skipped": NotRequired[int],
    },
)
TimestampTypeDef = Union[datetime, str]
CisFindingStatusFilterTypeDef = TypedDict(
    "CisFindingStatusFilterTypeDef",
    {
        "comparison": Literal["EQUALS"],
        "value": CisFindingStatusType,
    },
)
CisNumberFilterTypeDef = TypedDict(
    "CisNumberFilterTypeDef",
    {
        "lowerInclusive": NotRequired[int],
        "upperInclusive": NotRequired[int],
    },
)
CisResultStatusFilterTypeDef = TypedDict(
    "CisResultStatusFilterTypeDef",
    {
        "comparison": Literal["EQUALS"],
        "value": CisResultStatusType,
    },
)
CisTargetsTypeDef = TypedDict(
    "CisTargetsTypeDef",
    {
        "accountIds": NotRequired[List[str]],
        "targetResourceTags": NotRequired[Dict[str, List[str]]],
    },
)
CisSecurityLevelFilterTypeDef = TypedDict(
    "CisSecurityLevelFilterTypeDef",
    {
        "comparison": Literal["EQUALS"],
        "value": CisSecurityLevelType,
    },
)
CisStringFilterTypeDef = TypedDict(
    "CisStringFilterTypeDef",
    {
        "comparison": CisStringComparisonType,
        "value": str,
    },
)
CisScanResultDetailsTypeDef = TypedDict(
    "CisScanResultDetailsTypeDef",
    {
        "scanArn": str,
        "accountId": NotRequired[str],
        "checkDescription": NotRequired[str],
        "checkId": NotRequired[str],
        "findingArn": NotRequired[str],
        "level": NotRequired[CisSecurityLevelType],
        "platform": NotRequired[str],
        "remediation": NotRequired[str],
        "status": NotRequired[CisFindingStatusType],
        "statusReason": NotRequired[str],
        "targetResourceId": NotRequired[str],
        "title": NotRequired[str],
    },
)
CisTargetStatusFilterTypeDef = TypedDict(
    "CisTargetStatusFilterTypeDef",
    {
        "comparison": Literal["EQUALS"],
        "value": CisTargetStatusType,
    },
)
CisTargetStatusReasonFilterTypeDef = TypedDict(
    "CisTargetStatusReasonFilterTypeDef",
    {
        "comparison": Literal["EQUALS"],
        "value": CisTargetStatusReasonType,
    },
)
TagFilterTypeDef = TypedDict(
    "TagFilterTypeDef",
    {
        "comparison": Literal["EQUALS"],
        "key": str,
        "value": str,
    },
)
CisScanStatusFilterTypeDef = TypedDict(
    "CisScanStatusFilterTypeDef",
    {
        "comparison": Literal["EQUALS"],
        "value": CisScanStatusType,
    },
)
CisaDataTypeDef = TypedDict(
    "CisaDataTypeDef",
    {
        "action": NotRequired[str],
        "dateAdded": NotRequired[datetime],
        "dateDue": NotRequired[datetime],
    },
)
CodeFilePathTypeDef = TypedDict(
    "CodeFilePathTypeDef",
    {
        "endLine": int,
        "fileName": str,
        "filePath": str,
        "startLine": int,
    },
)
CodeLineTypeDef = TypedDict(
    "CodeLineTypeDef",
    {
        "content": str,
        "lineNumber": int,
    },
)
SuggestedFixTypeDef = TypedDict(
    "SuggestedFixTypeDef",
    {
        "code": NotRequired[str],
        "description": NotRequired[str],
    },
)
ComputePlatformTypeDef = TypedDict(
    "ComputePlatformTypeDef",
    {
        "product": NotRequired[str],
        "vendor": NotRequired[str],
        "version": NotRequired[str],
    },
)
CountsTypeDef = TypedDict(
    "CountsTypeDef",
    {
        "count": NotRequired[int],
        "groupKey": NotRequired[GroupKeyType],
    },
)
CoverageMapFilterTypeDef = TypedDict(
    "CoverageMapFilterTypeDef",
    {
        "comparison": Literal["EQUALS"],
        "key": str,
        "value": NotRequired[str],
    },
)
CoverageStringFilterTypeDef = TypedDict(
    "CoverageStringFilterTypeDef",
    {
        "comparison": CoverageStringComparisonType,
        "value": str,
    },
)
ScanStatusTypeDef = TypedDict(
    "ScanStatusTypeDef",
    {
        "reason": ScanStatusReasonType,
        "statusCode": ScanStatusCodeType,
    },
)
CreateCisTargetsTypeDef = TypedDict(
    "CreateCisTargetsTypeDef",
    {
        "accountIds": Sequence[str],
        "targetResourceTags": Mapping[str, Sequence[str]],
    },
)
DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "bucketName": str,
        "kmsKeyArn": str,
        "keyPrefix": NotRequired[str],
    },
)
Cvss2TypeDef = TypedDict(
    "Cvss2TypeDef",
    {
        "baseScore": NotRequired[float],
        "scoringVector": NotRequired[str],
    },
)
Cvss3TypeDef = TypedDict(
    "Cvss3TypeDef",
    {
        "baseScore": NotRequired[float],
        "scoringVector": NotRequired[str],
    },
)
CvssScoreAdjustmentTypeDef = TypedDict(
    "CvssScoreAdjustmentTypeDef",
    {
        "metric": str,
        "reason": str,
    },
)
CvssScoreTypeDef = TypedDict(
    "CvssScoreTypeDef",
    {
        "baseScore": float,
        "scoringVector": str,
        "source": str,
        "version": str,
    },
)
TimeTypeDef = TypedDict(
    "TimeTypeDef",
    {
        "timeOfDay": str,
        "timezone": str,
    },
)
DateFilterOutputTypeDef = TypedDict(
    "DateFilterOutputTypeDef",
    {
        "endInclusive": NotRequired[datetime],
        "startInclusive": NotRequired[datetime],
    },
)
DelegatedAdminAccountTypeDef = TypedDict(
    "DelegatedAdminAccountTypeDef",
    {
        "accountId": NotRequired[str],
        "status": NotRequired[DelegatedAdminStatusType],
    },
)
DelegatedAdminTypeDef = TypedDict(
    "DelegatedAdminTypeDef",
    {
        "accountId": NotRequired[str],
        "relationshipStatus": NotRequired[RelationshipStatusType],
    },
)
DeleteCisScanConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteCisScanConfigurationRequestRequestTypeDef",
    {
        "scanConfigurationArn": str,
    },
)
DeleteFilterRequestRequestTypeDef = TypedDict(
    "DeleteFilterRequestRequestTypeDef",
    {
        "arn": str,
    },
)
DisableDelegatedAdminAccountRequestRequestTypeDef = TypedDict(
    "DisableDelegatedAdminAccountRequestRequestTypeDef",
    {
        "delegatedAdminAccountId": str,
    },
)
DisableRequestRequestTypeDef = TypedDict(
    "DisableRequestRequestTypeDef",
    {
        "accountIds": NotRequired[Sequence[str]],
        "resourceTypes": NotRequired[Sequence[ResourceScanTypeType]],
    },
)
DisassociateMemberRequestRequestTypeDef = TypedDict(
    "DisassociateMemberRequestRequestTypeDef",
    {
        "accountId": str,
    },
)
Ec2ScanModeStateTypeDef = TypedDict(
    "Ec2ScanModeStateTypeDef",
    {
        "scanMode": NotRequired[Ec2ScanModeType],
        "scanModeStatus": NotRequired[Ec2ScanModeStatusType],
    },
)
Ec2ConfigurationTypeDef = TypedDict(
    "Ec2ConfigurationTypeDef",
    {
        "scanMode": Ec2ScanModeType,
    },
)
MapFilterTypeDef = TypedDict(
    "MapFilterTypeDef",
    {
        "comparison": Literal["EQUALS"],
        "key": str,
        "value": NotRequired[str],
    },
)
Ec2MetadataTypeDef = TypedDict(
    "Ec2MetadataTypeDef",
    {
        "amiId": NotRequired[str],
        "platform": NotRequired[Ec2PlatformType],
        "tags": NotRequired[Dict[str, str]],
    },
)
EcrRescanDurationStateTypeDef = TypedDict(
    "EcrRescanDurationStateTypeDef",
    {
        "pullDateRescanDuration": NotRequired[EcrPullDateRescanDurationType],
        "rescanDuration": NotRequired[EcrRescanDurationType],
        "status": NotRequired[EcrRescanDurationStatusType],
        "updatedAt": NotRequired[datetime],
    },
)
EcrConfigurationTypeDef = TypedDict(
    "EcrConfigurationTypeDef",
    {
        "rescanDuration": EcrRescanDurationType,
        "pullDateRescanDuration": NotRequired[EcrPullDateRescanDurationType],
    },
)
EcrContainerImageMetadataTypeDef = TypedDict(
    "EcrContainerImageMetadataTypeDef",
    {
        "imagePulledAt": NotRequired[datetime],
        "tags": NotRequired[List[str]],
    },
)
EcrRepositoryMetadataTypeDef = TypedDict(
    "EcrRepositoryMetadataTypeDef",
    {
        "name": NotRequired[str],
        "scanFrequency": NotRequired[EcrScanFrequencyType],
    },
)
EnableDelegatedAdminAccountRequestRequestTypeDef = TypedDict(
    "EnableDelegatedAdminAccountRequestRequestTypeDef",
    {
        "delegatedAdminAccountId": str,
        "clientToken": NotRequired[str],
    },
)
EnableRequestRequestTypeDef = TypedDict(
    "EnableRequestRequestTypeDef",
    {
        "resourceTypes": Sequence[ResourceScanTypeType],
        "accountIds": NotRequired[Sequence[str]],
        "clientToken": NotRequired[str],
    },
)
EpssDetailsTypeDef = TypedDict(
    "EpssDetailsTypeDef",
    {
        "score": NotRequired[float],
    },
)
EpssTypeDef = TypedDict(
    "EpssTypeDef",
    {
        "score": NotRequired[float],
    },
)
EvidenceTypeDef = TypedDict(
    "EvidenceTypeDef",
    {
        "evidenceDetail": NotRequired[str],
        "evidenceRule": NotRequired[str],
        "severity": NotRequired[str],
    },
)
ExploitObservedTypeDef = TypedDict(
    "ExploitObservedTypeDef",
    {
        "firstSeen": NotRequired[datetime],
        "lastSeen": NotRequired[datetime],
    },
)
ExploitabilityDetailsTypeDef = TypedDict(
    "ExploitabilityDetailsTypeDef",
    {
        "lastKnownExploitAt": NotRequired[datetime],
    },
)
NumberFilterTypeDef = TypedDict(
    "NumberFilterTypeDef",
    {
        "lowerInclusive": NotRequired[float],
        "upperInclusive": NotRequired[float],
    },
)
PortRangeFilterTypeDef = TypedDict(
    "PortRangeFilterTypeDef",
    {
        "beginInclusive": NotRequired[int],
        "endInclusive": NotRequired[int],
    },
)
FreeTrialInfoTypeDef = TypedDict(
    "FreeTrialInfoTypeDef",
    {
        "end": datetime,
        "start": datetime,
        "status": FreeTrialStatusType,
        "type": FreeTrialTypeType,
    },
)
GetCisScanReportRequestRequestTypeDef = TypedDict(
    "GetCisScanReportRequestRequestTypeDef",
    {
        "scanArn": str,
        "reportFormat": NotRequired[CisReportFormatType],
        "targetAccounts": NotRequired[Sequence[str]],
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
GetEncryptionKeyRequestRequestTypeDef = TypedDict(
    "GetEncryptionKeyRequestRequestTypeDef",
    {
        "resourceType": ResourceTypeType,
        "scanType": ScanTypeType,
    },
)
GetFindingsReportStatusRequestRequestTypeDef = TypedDict(
    "GetFindingsReportStatusRequestRequestTypeDef",
    {
        "reportId": NotRequired[str],
    },
)
GetMemberRequestRequestTypeDef = TypedDict(
    "GetMemberRequestRequestTypeDef",
    {
        "accountId": str,
    },
)
MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "accountId": NotRequired[str],
        "delegatedAdminAccountId": NotRequired[str],
        "relationshipStatus": NotRequired[RelationshipStatusType],
        "updatedAt": NotRequired[datetime],
    },
)
GetSbomExportRequestRequestTypeDef = TypedDict(
    "GetSbomExportRequestRequestTypeDef",
    {
        "reportId": str,
    },
)
LambdaFunctionMetadataTypeDef = TypedDict(
    "LambdaFunctionMetadataTypeDef",
    {
        "functionName": NotRequired[str],
        "functionTags": NotRequired[Dict[str, str]],
        "layers": NotRequired[List[str]],
        "runtime": NotRequired[RuntimeType],
    },
)
ListAccountPermissionsRequestRequestTypeDef = TypedDict(
    "ListAccountPermissionsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "service": NotRequired[ServiceType],
    },
)
PermissionTypeDef = TypedDict(
    "PermissionTypeDef",
    {
        "operation": OperationType,
        "service": ServiceType,
    },
)
ListDelegatedAdminAccountsRequestRequestTypeDef = TypedDict(
    "ListDelegatedAdminAccountsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListFiltersRequestRequestTypeDef = TypedDict(
    "ListFiltersRequestRequestTypeDef",
    {
        "action": NotRequired[FilterActionType],
        "arns": NotRequired[Sequence[str]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
SortCriteriaTypeDef = TypedDict(
    "SortCriteriaTypeDef",
    {
        "field": SortFieldType,
        "sortOrder": SortOrderType,
    },
)
ListMembersRequestRequestTypeDef = TypedDict(
    "ListMembersRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "onlyAssociated": NotRequired[bool],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
ListUsageTotalsRequestRequestTypeDef = TypedDict(
    "ListUsageTotalsRequestRequestTypeDef",
    {
        "accountIds": NotRequired[Sequence[str]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
StepTypeDef = TypedDict(
    "StepTypeDef",
    {
        "componentId": str,
        "componentType": str,
    },
)
PortRangeTypeDef = TypedDict(
    "PortRangeTypeDef",
    {
        "begin": int,
        "end": int,
    },
)
VulnerablePackageTypeDef = TypedDict(
    "VulnerablePackageTypeDef",
    {
        "name": str,
        "version": str,
        "arch": NotRequired[str],
        "epoch": NotRequired[int],
        "filePath": NotRequired[str],
        "fixedInVersion": NotRequired[str],
        "packageManager": NotRequired[PackageManagerType],
        "release": NotRequired[str],
        "remediation": NotRequired[str],
        "sourceLambdaLayerArn": NotRequired[str],
        "sourceLayerHash": NotRequired[str],
    },
)
RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "Url": NotRequired[str],
        "text": NotRequired[str],
    },
)
ResetEncryptionKeyRequestRequestTypeDef = TypedDict(
    "ResetEncryptionKeyRequestRequestTypeDef",
    {
        "resourceType": ResourceTypeType,
        "scanType": ScanTypeType,
    },
)
ResourceMapFilterTypeDef = TypedDict(
    "ResourceMapFilterTypeDef",
    {
        "comparison": Literal["EQUALS"],
        "key": str,
        "value": NotRequired[str],
    },
)
ResourceStringFilterTypeDef = TypedDict(
    "ResourceStringFilterTypeDef",
    {
        "comparison": ResourceStringComparisonType,
        "value": str,
    },
)
SearchVulnerabilitiesFilterCriteriaTypeDef = TypedDict(
    "SearchVulnerabilitiesFilterCriteriaTypeDef",
    {
        "vulnerabilityIds": Sequence[str],
    },
)
SendCisSessionHealthRequestRequestTypeDef = TypedDict(
    "SendCisSessionHealthRequestRequestTypeDef",
    {
        "scanJobId": str,
        "sessionToken": str,
    },
)
StartCisSessionMessageTypeDef = TypedDict(
    "StartCisSessionMessageTypeDef",
    {
        "sessionToken": str,
    },
)
StopCisMessageProgressTypeDef = TypedDict(
    "StopCisMessageProgressTypeDef",
    {
        "errorChecks": NotRequired[int],
        "failedChecks": NotRequired[int],
        "informationalChecks": NotRequired[int],
        "notApplicableChecks": NotRequired[int],
        "notEvaluatedChecks": NotRequired[int],
        "successfulChecks": NotRequired[int],
        "totalChecks": NotRequired[int],
        "unknownChecks": NotRequired[int],
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
UpdateCisTargetsTypeDef = TypedDict(
    "UpdateCisTargetsTypeDef",
    {
        "accountIds": NotRequired[Sequence[str]],
        "targetResourceTags": NotRequired[Mapping[str, Sequence[str]]],
    },
)
UpdateEc2DeepInspectionConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateEc2DeepInspectionConfigurationRequestRequestTypeDef",
    {
        "activateDeepInspection": NotRequired[bool],
        "packagePaths": NotRequired[Sequence[str]],
    },
)
UpdateEncryptionKeyRequestRequestTypeDef = TypedDict(
    "UpdateEncryptionKeyRequestRequestTypeDef",
    {
        "kmsKeyId": str,
        "resourceType": ResourceTypeType,
        "scanType": ScanTypeType,
    },
)
UpdateOrgEc2DeepInspectionConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateOrgEc2DeepInspectionConfigurationRequestRequestTypeDef",
    {
        "orgPackagePaths": Sequence[str],
    },
)
UsageTypeDef = TypedDict(
    "UsageTypeDef",
    {
        "currency": NotRequired[Literal["USD"]],
        "estimatedMonthlyCost": NotRequired[float],
        "total": NotRequired[float],
        "type": NotRequired[UsageTypeType],
    },
)
AccountAggregationResponseTypeDef = TypedDict(
    "AccountAggregationResponseTypeDef",
    {
        "accountId": NotRequired[str],
        "exploitAvailableCount": NotRequired[int],
        "fixAvailableCount": NotRequired[int],
        "severityCounts": NotRequired[SeverityCountsTypeDef],
    },
)
AmiAggregationResponseTypeDef = TypedDict(
    "AmiAggregationResponseTypeDef",
    {
        "ami": str,
        "accountId": NotRequired[str],
        "affectedInstances": NotRequired[int],
        "severityCounts": NotRequired[SeverityCountsTypeDef],
    },
)
AwsEcrContainerAggregationResponseTypeDef = TypedDict(
    "AwsEcrContainerAggregationResponseTypeDef",
    {
        "resourceId": str,
        "accountId": NotRequired[str],
        "architecture": NotRequired[str],
        "imageSha": NotRequired[str],
        "imageTags": NotRequired[List[str]],
        "repository": NotRequired[str],
        "severityCounts": NotRequired[SeverityCountsTypeDef],
    },
)
Ec2InstanceAggregationResponseTypeDef = TypedDict(
    "Ec2InstanceAggregationResponseTypeDef",
    {
        "instanceId": str,
        "accountId": NotRequired[str],
        "ami": NotRequired[str],
        "instanceTags": NotRequired[Dict[str, str]],
        "networkFindings": NotRequired[int],
        "operatingSystem": NotRequired[str],
        "severityCounts": NotRequired[SeverityCountsTypeDef],
    },
)
FindingTypeAggregationResponseTypeDef = TypedDict(
    "FindingTypeAggregationResponseTypeDef",
    {
        "accountId": NotRequired[str],
        "exploitAvailableCount": NotRequired[int],
        "fixAvailableCount": NotRequired[int],
        "severityCounts": NotRequired[SeverityCountsTypeDef],
    },
)
ImageLayerAggregationResponseTypeDef = TypedDict(
    "ImageLayerAggregationResponseTypeDef",
    {
        "accountId": str,
        "layerHash": str,
        "repository": str,
        "resourceId": str,
        "severityCounts": NotRequired[SeverityCountsTypeDef],
    },
)
LambdaFunctionAggregationResponseTypeDef = TypedDict(
    "LambdaFunctionAggregationResponseTypeDef",
    {
        "resourceId": str,
        "accountId": NotRequired[str],
        "functionName": NotRequired[str],
        "lambdaTags": NotRequired[Dict[str, str]],
        "lastModifiedAt": NotRequired[datetime],
        "runtime": NotRequired[str],
        "severityCounts": NotRequired[SeverityCountsTypeDef],
    },
)
LambdaLayerAggregationResponseTypeDef = TypedDict(
    "LambdaLayerAggregationResponseTypeDef",
    {
        "accountId": str,
        "functionName": str,
        "layerArn": str,
        "resourceId": str,
        "severityCounts": NotRequired[SeverityCountsTypeDef],
    },
)
PackageAggregationResponseTypeDef = TypedDict(
    "PackageAggregationResponseTypeDef",
    {
        "packageName": str,
        "accountId": NotRequired[str],
        "severityCounts": NotRequired[SeverityCountsTypeDef],
    },
)
RepositoryAggregationResponseTypeDef = TypedDict(
    "RepositoryAggregationResponseTypeDef",
    {
        "repository": str,
        "accountId": NotRequired[str],
        "affectedImages": NotRequired[int],
        "severityCounts": NotRequired[SeverityCountsTypeDef],
    },
)
TitleAggregationResponseTypeDef = TypedDict(
    "TitleAggregationResponseTypeDef",
    {
        "title": str,
        "accountId": NotRequired[str],
        "severityCounts": NotRequired[SeverityCountsTypeDef],
        "vulnerabilityId": NotRequired[str],
    },
)
ResourceStateTypeDef = TypedDict(
    "ResourceStateTypeDef",
    {
        "ec2": StateTypeDef,
        "ecr": StateTypeDef,
        "lambda": NotRequired[StateTypeDef],
        "lambdaCode": NotRequired[StateTypeDef],
    },
)
AccountTypeDef = TypedDict(
    "AccountTypeDef",
    {
        "accountId": str,
        "resourceStatus": ResourceStatusTypeDef,
        "status": StatusType,
    },
)
FailedAccountTypeDef = TypedDict(
    "FailedAccountTypeDef",
    {
        "accountId": str,
        "errorCode": ErrorCodeType,
        "errorMessage": str,
        "resourceStatus": NotRequired[ResourceStatusTypeDef],
        "status": NotRequired[StatusType],
    },
)
AmiAggregationTypeDef = TypedDict(
    "AmiAggregationTypeDef",
    {
        "amis": NotRequired[Sequence[StringFilterTypeDef]],
        "sortBy": NotRequired[AmiSortByType],
        "sortOrder": NotRequired[SortOrderType],
    },
)
AwsEcrContainerAggregationTypeDef = TypedDict(
    "AwsEcrContainerAggregationTypeDef",
    {
        "architectures": NotRequired[Sequence[StringFilterTypeDef]],
        "imageShas": NotRequired[Sequence[StringFilterTypeDef]],
        "imageTags": NotRequired[Sequence[StringFilterTypeDef]],
        "repositories": NotRequired[Sequence[StringFilterTypeDef]],
        "resourceIds": NotRequired[Sequence[StringFilterTypeDef]],
        "sortBy": NotRequired[AwsEcrContainerSortByType],
        "sortOrder": NotRequired[SortOrderType],
    },
)
ImageLayerAggregationTypeDef = TypedDict(
    "ImageLayerAggregationTypeDef",
    {
        "layerHashes": NotRequired[Sequence[StringFilterTypeDef]],
        "repositories": NotRequired[Sequence[StringFilterTypeDef]],
        "resourceIds": NotRequired[Sequence[StringFilterTypeDef]],
        "sortBy": NotRequired[ImageLayerSortByType],
        "sortOrder": NotRequired[SortOrderType],
    },
)
LambdaLayerAggregationTypeDef = TypedDict(
    "LambdaLayerAggregationTypeDef",
    {
        "functionNames": NotRequired[Sequence[StringFilterTypeDef]],
        "layerArns": NotRequired[Sequence[StringFilterTypeDef]],
        "resourceIds": NotRequired[Sequence[StringFilterTypeDef]],
        "sortBy": NotRequired[LambdaLayerSortByType],
        "sortOrder": NotRequired[SortOrderType],
    },
)
PackageAggregationTypeDef = TypedDict(
    "PackageAggregationTypeDef",
    {
        "packageNames": NotRequired[Sequence[StringFilterTypeDef]],
        "sortBy": NotRequired[PackageSortByType],
        "sortOrder": NotRequired[SortOrderType],
    },
)
RepositoryAggregationTypeDef = TypedDict(
    "RepositoryAggregationTypeDef",
    {
        "repositories": NotRequired[Sequence[StringFilterTypeDef]],
        "sortBy": NotRequired[RepositorySortByType],
        "sortOrder": NotRequired[SortOrderType],
    },
)
TitleAggregationTypeDef = TypedDict(
    "TitleAggregationTypeDef",
    {
        "findingType": NotRequired[AggregationFindingTypeType],
        "resourceType": NotRequired[AggregationResourceTypeType],
        "sortBy": NotRequired[TitleSortByType],
        "sortOrder": NotRequired[SortOrderType],
        "titles": NotRequired[Sequence[StringFilterTypeDef]],
        "vulnerabilityIds": NotRequired[Sequence[StringFilterTypeDef]],
    },
)
AssociateMemberResponseTypeDef = TypedDict(
    "AssociateMemberResponseTypeDef",
    {
        "accountId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CancelFindingsReportResponseTypeDef = TypedDict(
    "CancelFindingsReportResponseTypeDef",
    {
        "reportId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CancelSbomExportResponseTypeDef = TypedDict(
    "CancelSbomExportResponseTypeDef",
    {
        "reportId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCisScanConfigurationResponseTypeDef = TypedDict(
    "CreateCisScanConfigurationResponseTypeDef",
    {
        "scanConfigurationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFilterResponseTypeDef = TypedDict(
    "CreateFilterResponseTypeDef",
    {
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFindingsReportResponseTypeDef = TypedDict(
    "CreateFindingsReportResponseTypeDef",
    {
        "reportId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSbomExportResponseTypeDef = TypedDict(
    "CreateSbomExportResponseTypeDef",
    {
        "reportId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteCisScanConfigurationResponseTypeDef = TypedDict(
    "DeleteCisScanConfigurationResponseTypeDef",
    {
        "scanConfigurationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteFilterResponseTypeDef = TypedDict(
    "DeleteFilterResponseTypeDef",
    {
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisableDelegatedAdminAccountResponseTypeDef = TypedDict(
    "DisableDelegatedAdminAccountResponseTypeDef",
    {
        "delegatedAdminAccountId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateMemberResponseTypeDef = TypedDict(
    "DisassociateMemberResponseTypeDef",
    {
        "accountId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableDelegatedAdminAccountResponseTypeDef = TypedDict(
    "EnableDelegatedAdminAccountResponseTypeDef",
    {
        "delegatedAdminAccountId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCisScanReportResponseTypeDef = TypedDict(
    "GetCisScanReportResponseTypeDef",
    {
        "status": CisReportStatusType,
        "url": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEc2DeepInspectionConfigurationResponseTypeDef = TypedDict(
    "GetEc2DeepInspectionConfigurationResponseTypeDef",
    {
        "errorMessage": str,
        "orgPackagePaths": List[str],
        "packagePaths": List[str],
        "status": Ec2DeepInspectionStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEncryptionKeyResponseTypeDef = TypedDict(
    "GetEncryptionKeyResponseTypeDef",
    {
        "kmsKeyId": str,
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
UpdateCisScanConfigurationResponseTypeDef = TypedDict(
    "UpdateCisScanConfigurationResponseTypeDef",
    {
        "scanConfigurationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEc2DeepInspectionConfigurationResponseTypeDef = TypedDict(
    "UpdateEc2DeepInspectionConfigurationResponseTypeDef",
    {
        "errorMessage": str,
        "orgPackagePaths": List[str],
        "packagePaths": List[str],
        "status": Ec2DeepInspectionStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFilterResponseTypeDef = TypedDict(
    "UpdateFilterResponseTypeDef",
    {
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeOrganizationConfigurationResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigurationResponseTypeDef",
    {
        "autoEnable": AutoEnableTypeDef,
        "maxAccountLimitReached": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
    {
        "autoEnable": AutoEnableTypeDef,
    },
)
UpdateOrganizationConfigurationResponseTypeDef = TypedDict(
    "UpdateOrganizationConfigurationResponseTypeDef",
    {
        "autoEnable": AutoEnableTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AwsLambdaFunctionDetailsTypeDef = TypedDict(
    "AwsLambdaFunctionDetailsTypeDef",
    {
        "codeSha256": str,
        "executionRoleArn": str,
        "functionName": str,
        "runtime": RuntimeType,
        "version": str,
        "architectures": NotRequired[List[ArchitectureType]],
        "lastModifiedAt": NotRequired[datetime],
        "layers": NotRequired[List[str]],
        "packageType": NotRequired[PackageTypeType],
        "vpcConfig": NotRequired[LambdaVpcConfigTypeDef],
    },
)
BatchGetMemberEc2DeepInspectionStatusResponseTypeDef = TypedDict(
    "BatchGetMemberEc2DeepInspectionStatusResponseTypeDef",
    {
        "accountIds": List[MemberAccountEc2DeepInspectionStatusStateTypeDef],
        "failedAccountIds": List[FailedMemberAccountEc2DeepInspectionStatusStateTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchUpdateMemberEc2DeepInspectionStatusResponseTypeDef = TypedDict(
    "BatchUpdateMemberEc2DeepInspectionStatusResponseTypeDef",
    {
        "accountIds": List[MemberAccountEc2DeepInspectionStatusStateTypeDef],
        "failedAccountIds": List[FailedMemberAccountEc2DeepInspectionStatusStateTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchUpdateMemberEc2DeepInspectionStatusRequestRequestTypeDef = TypedDict(
    "BatchUpdateMemberEc2DeepInspectionStatusRequestRequestTypeDef",
    {
        "accountIds": Sequence[MemberAccountEc2DeepInspectionStatusTypeDef],
    },
)
CisSessionMessageTypeDef = TypedDict(
    "CisSessionMessageTypeDef",
    {
        "cisRuleDetails": BlobTypeDef,
        "ruleId": str,
        "status": CisRuleStatusType,
    },
)
CisCheckAggregationTypeDef = TypedDict(
    "CisCheckAggregationTypeDef",
    {
        "scanArn": str,
        "accountId": NotRequired[str],
        "checkDescription": NotRequired[str],
        "checkId": NotRequired[str],
        "level": NotRequired[CisSecurityLevelType],
        "platform": NotRequired[str],
        "statusCounts": NotRequired[StatusCountsTypeDef],
        "title": NotRequired[str],
    },
)
CisTargetResourceAggregationTypeDef = TypedDict(
    "CisTargetResourceAggregationTypeDef",
    {
        "scanArn": str,
        "accountId": NotRequired[str],
        "platform": NotRequired[str],
        "statusCounts": NotRequired[StatusCountsTypeDef],
        "targetResourceId": NotRequired[str],
        "targetResourceTags": NotRequired[Dict[str, List[str]]],
        "targetStatus": NotRequired[CisTargetStatusType],
        "targetStatusReason": NotRequired[CisTargetStatusReasonType],
    },
)
CisDateFilterTypeDef = TypedDict(
    "CisDateFilterTypeDef",
    {
        "earliestScanStartTime": NotRequired[TimestampTypeDef],
        "latestScanStartTime": NotRequired[TimestampTypeDef],
    },
)
CoverageDateFilterTypeDef = TypedDict(
    "CoverageDateFilterTypeDef",
    {
        "endInclusive": NotRequired[TimestampTypeDef],
        "startInclusive": NotRequired[TimestampTypeDef],
    },
)
DateFilterTypeDef = TypedDict(
    "DateFilterTypeDef",
    {
        "endInclusive": NotRequired[TimestampTypeDef],
        "startInclusive": NotRequired[TimestampTypeDef],
    },
)
CisScanTypeDef = TypedDict(
    "CisScanTypeDef",
    {
        "scanArn": str,
        "scanConfigurationArn": str,
        "failedChecks": NotRequired[int],
        "scanDate": NotRequired[datetime],
        "scanName": NotRequired[str],
        "scheduledBy": NotRequired[str],
        "securityLevel": NotRequired[CisSecurityLevelType],
        "status": NotRequired[CisScanStatusType],
        "targets": NotRequired[CisTargetsTypeDef],
        "totalChecks": NotRequired[int],
    },
)
CisScanResultDetailsFilterCriteriaTypeDef = TypedDict(
    "CisScanResultDetailsFilterCriteriaTypeDef",
    {
        "checkIdFilters": NotRequired[Sequence[CisStringFilterTypeDef]],
        "findingArnFilters": NotRequired[Sequence[CisStringFilterTypeDef]],
        "findingStatusFilters": NotRequired[Sequence[CisFindingStatusFilterTypeDef]],
        "securityLevelFilters": NotRequired[Sequence[CisSecurityLevelFilterTypeDef]],
        "titleFilters": NotRequired[Sequence[CisStringFilterTypeDef]],
    },
)
CisScanResultsAggregatedByChecksFilterCriteriaTypeDef = TypedDict(
    "CisScanResultsAggregatedByChecksFilterCriteriaTypeDef",
    {
        "accountIdFilters": NotRequired[Sequence[CisStringFilterTypeDef]],
        "checkIdFilters": NotRequired[Sequence[CisStringFilterTypeDef]],
        "failedResourcesFilters": NotRequired[Sequence[CisNumberFilterTypeDef]],
        "platformFilters": NotRequired[Sequence[CisStringFilterTypeDef]],
        "securityLevelFilters": NotRequired[Sequence[CisSecurityLevelFilterTypeDef]],
        "titleFilters": NotRequired[Sequence[CisStringFilterTypeDef]],
    },
)
GetCisScanResultDetailsResponseTypeDef = TypedDict(
    "GetCisScanResultDetailsResponseTypeDef",
    {
        "nextToken": str,
        "scanResultDetails": List[CisScanResultDetailsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CisScanResultsAggregatedByTargetResourceFilterCriteriaTypeDef = TypedDict(
    "CisScanResultsAggregatedByTargetResourceFilterCriteriaTypeDef",
    {
        "accountIdFilters": NotRequired[Sequence[CisStringFilterTypeDef]],
        "checkIdFilters": NotRequired[Sequence[CisStringFilterTypeDef]],
        "failedChecksFilters": NotRequired[Sequence[CisNumberFilterTypeDef]],
        "platformFilters": NotRequired[Sequence[CisStringFilterTypeDef]],
        "statusFilters": NotRequired[Sequence[CisResultStatusFilterTypeDef]],
        "targetResourceIdFilters": NotRequired[Sequence[CisStringFilterTypeDef]],
        "targetResourceTagFilters": NotRequired[Sequence[TagFilterTypeDef]],
        "targetStatusFilters": NotRequired[Sequence[CisTargetStatusFilterTypeDef]],
        "targetStatusReasonFilters": NotRequired[Sequence[CisTargetStatusReasonFilterTypeDef]],
    },
)
ListCisScanConfigurationsFilterCriteriaTypeDef = TypedDict(
    "ListCisScanConfigurationsFilterCriteriaTypeDef",
    {
        "scanConfigurationArnFilters": NotRequired[Sequence[CisStringFilterTypeDef]],
        "scanNameFilters": NotRequired[Sequence[CisStringFilterTypeDef]],
        "targetResourceTagFilters": NotRequired[Sequence[TagFilterTypeDef]],
    },
)
CodeVulnerabilityDetailsTypeDef = TypedDict(
    "CodeVulnerabilityDetailsTypeDef",
    {
        "cwes": List[str],
        "detectorId": str,
        "detectorName": str,
        "filePath": CodeFilePathTypeDef,
        "detectorTags": NotRequired[List[str]],
        "referenceUrls": NotRequired[List[str]],
        "ruleId": NotRequired[str],
        "sourceLambdaLayerArn": NotRequired[str],
    },
)
CodeSnippetResultTypeDef = TypedDict(
    "CodeSnippetResultTypeDef",
    {
        "codeSnippet": NotRequired[List[CodeLineTypeDef]],
        "endLine": NotRequired[int],
        "findingArn": NotRequired[str],
        "startLine": NotRequired[int],
        "suggestedFixes": NotRequired[List[SuggestedFixTypeDef]],
    },
)
ListCoverageStatisticsResponseTypeDef = TypedDict(
    "ListCoverageStatisticsResponseTypeDef",
    {
        "countsByGroup": List[CountsTypeDef],
        "nextToken": str,
        "totalCounts": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CvssScoreDetailsTypeDef = TypedDict(
    "CvssScoreDetailsTypeDef",
    {
        "score": float,
        "scoreSource": str,
        "scoringVector": str,
        "version": str,
        "adjustments": NotRequired[List[CvssScoreAdjustmentTypeDef]],
        "cvssSource": NotRequired[str],
    },
)
DailyScheduleTypeDef = TypedDict(
    "DailyScheduleTypeDef",
    {
        "startTime": TimeTypeDef,
    },
)
MonthlyScheduleTypeDef = TypedDict(
    "MonthlyScheduleTypeDef",
    {
        "day": DayType,
        "startTime": TimeTypeDef,
    },
)
WeeklyScheduleOutputTypeDef = TypedDict(
    "WeeklyScheduleOutputTypeDef",
    {
        "days": List[DayType],
        "startTime": TimeTypeDef,
    },
)
WeeklyScheduleTypeDef = TypedDict(
    "WeeklyScheduleTypeDef",
    {
        "days": Sequence[DayType],
        "startTime": TimeTypeDef,
    },
)
ListDelegatedAdminAccountsResponseTypeDef = TypedDict(
    "ListDelegatedAdminAccountsResponseTypeDef",
    {
        "delegatedAdminAccounts": List[DelegatedAdminAccountTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDelegatedAdminAccountResponseTypeDef = TypedDict(
    "GetDelegatedAdminAccountResponseTypeDef",
    {
        "delegatedAdmin": DelegatedAdminTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
Ec2ConfigurationStateTypeDef = TypedDict(
    "Ec2ConfigurationStateTypeDef",
    {
        "scanModeState": NotRequired[Ec2ScanModeStateTypeDef],
    },
)
Ec2InstanceAggregationTypeDef = TypedDict(
    "Ec2InstanceAggregationTypeDef",
    {
        "amis": NotRequired[Sequence[StringFilterTypeDef]],
        "instanceIds": NotRequired[Sequence[StringFilterTypeDef]],
        "instanceTags": NotRequired[Sequence[MapFilterTypeDef]],
        "operatingSystems": NotRequired[Sequence[StringFilterTypeDef]],
        "sortBy": NotRequired[Ec2InstanceSortByType],
        "sortOrder": NotRequired[SortOrderType],
    },
)
LambdaFunctionAggregationTypeDef = TypedDict(
    "LambdaFunctionAggregationTypeDef",
    {
        "functionNames": NotRequired[Sequence[StringFilterTypeDef]],
        "functionTags": NotRequired[Sequence[MapFilterTypeDef]],
        "resourceIds": NotRequired[Sequence[StringFilterTypeDef]],
        "runtimes": NotRequired[Sequence[StringFilterTypeDef]],
        "sortBy": NotRequired[LambdaFunctionSortByType],
        "sortOrder": NotRequired[SortOrderType],
    },
)
EcrConfigurationStateTypeDef = TypedDict(
    "EcrConfigurationStateTypeDef",
    {
        "rescanDurationState": NotRequired[EcrRescanDurationStateTypeDef],
    },
)
UpdateConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateConfigurationRequestRequestTypeDef",
    {
        "ec2Configuration": NotRequired[Ec2ConfigurationTypeDef],
        "ecrConfiguration": NotRequired[EcrConfigurationTypeDef],
    },
)
FindingDetailTypeDef = TypedDict(
    "FindingDetailTypeDef",
    {
        "cisaData": NotRequired[CisaDataTypeDef],
        "cwes": NotRequired[List[str]],
        "epssScore": NotRequired[float],
        "evidences": NotRequired[List[EvidenceTypeDef]],
        "exploitObserved": NotRequired[ExploitObservedTypeDef],
        "findingArn": NotRequired[str],
        "referenceUrls": NotRequired[List[str]],
        "riskScore": NotRequired[int],
        "tools": NotRequired[List[str]],
        "ttps": NotRequired[List[str]],
    },
)
VulnerabilityTypeDef = TypedDict(
    "VulnerabilityTypeDef",
    {
        "id": str,
        "atigData": NotRequired[AtigDataTypeDef],
        "cisaData": NotRequired[CisaDataTypeDef],
        "cvss2": NotRequired[Cvss2TypeDef],
        "cvss3": NotRequired[Cvss3TypeDef],
        "cwes": NotRequired[List[str]],
        "description": NotRequired[str],
        "detectionPlatforms": NotRequired[List[str]],
        "epss": NotRequired[EpssTypeDef],
        "exploitObserved": NotRequired[ExploitObservedTypeDef],
        "referenceUrls": NotRequired[List[str]],
        "relatedVulnerabilities": NotRequired[List[str]],
        "source": NotRequired[Literal["NVD"]],
        "sourceUrl": NotRequired[str],
        "vendorCreatedAt": NotRequired[datetime],
        "vendorSeverity": NotRequired[str],
        "vendorUpdatedAt": NotRequired[datetime],
    },
)
PackageFilterTypeDef = TypedDict(
    "PackageFilterTypeDef",
    {
        "architecture": NotRequired[StringFilterTypeDef],
        "epoch": NotRequired[NumberFilterTypeDef],
        "name": NotRequired[StringFilterTypeDef],
        "release": NotRequired[StringFilterTypeDef],
        "sourceLambdaLayerArn": NotRequired[StringFilterTypeDef],
        "sourceLayerHash": NotRequired[StringFilterTypeDef],
        "version": NotRequired[StringFilterTypeDef],
    },
)
FreeTrialAccountInfoTypeDef = TypedDict(
    "FreeTrialAccountInfoTypeDef",
    {
        "accountId": str,
        "freeTrialInfo": List[FreeTrialInfoTypeDef],
    },
)
ListAccountPermissionsRequestListAccountPermissionsPaginateTypeDef = TypedDict(
    "ListAccountPermissionsRequestListAccountPermissionsPaginateTypeDef",
    {
        "service": NotRequired[ServiceType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDelegatedAdminAccountsRequestListDelegatedAdminAccountsPaginateTypeDef = TypedDict(
    "ListDelegatedAdminAccountsRequestListDelegatedAdminAccountsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFiltersRequestListFiltersPaginateTypeDef = TypedDict(
    "ListFiltersRequestListFiltersPaginateTypeDef",
    {
        "action": NotRequired[FilterActionType],
        "arns": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMembersRequestListMembersPaginateTypeDef = TypedDict(
    "ListMembersRequestListMembersPaginateTypeDef",
    {
        "onlyAssociated": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListUsageTotalsRequestListUsageTotalsPaginateTypeDef = TypedDict(
    "ListUsageTotalsRequestListUsageTotalsPaginateTypeDef",
    {
        "accountIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetMemberResponseTypeDef = TypedDict(
    "GetMemberResponseTypeDef",
    {
        "member": MemberTypeDef,
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
ResourceScanMetadataTypeDef = TypedDict(
    "ResourceScanMetadataTypeDef",
    {
        "ec2": NotRequired[Ec2MetadataTypeDef],
        "ecrImage": NotRequired[EcrContainerImageMetadataTypeDef],
        "ecrRepository": NotRequired[EcrRepositoryMetadataTypeDef],
        "lambdaFunction": NotRequired[LambdaFunctionMetadataTypeDef],
    },
)
ListAccountPermissionsResponseTypeDef = TypedDict(
    "ListAccountPermissionsResponseTypeDef",
    {
        "nextToken": str,
        "permissions": List[PermissionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NetworkPathTypeDef = TypedDict(
    "NetworkPathTypeDef",
    {
        "steps": NotRequired[List[StepTypeDef]],
    },
)
PackageVulnerabilityDetailsTypeDef = TypedDict(
    "PackageVulnerabilityDetailsTypeDef",
    {
        "source": str,
        "vulnerabilityId": str,
        "cvss": NotRequired[List[CvssScoreTypeDef]],
        "referenceUrls": NotRequired[List[str]],
        "relatedVulnerabilities": NotRequired[List[str]],
        "sourceUrl": NotRequired[str],
        "vendorCreatedAt": NotRequired[datetime],
        "vendorSeverity": NotRequired[str],
        "vendorUpdatedAt": NotRequired[datetime],
        "vulnerablePackages": NotRequired[List[VulnerablePackageTypeDef]],
    },
)
RemediationTypeDef = TypedDict(
    "RemediationTypeDef",
    {
        "recommendation": NotRequired[RecommendationTypeDef],
    },
)
ResourceFilterCriteriaOutputTypeDef = TypedDict(
    "ResourceFilterCriteriaOutputTypeDef",
    {
        "accountId": NotRequired[List[ResourceStringFilterTypeDef]],
        "ec2InstanceTags": NotRequired[List[ResourceMapFilterTypeDef]],
        "ecrImageTags": NotRequired[List[ResourceStringFilterTypeDef]],
        "ecrRepositoryName": NotRequired[List[ResourceStringFilterTypeDef]],
        "lambdaFunctionName": NotRequired[List[ResourceStringFilterTypeDef]],
        "lambdaFunctionTags": NotRequired[List[ResourceMapFilterTypeDef]],
        "resourceId": NotRequired[List[ResourceStringFilterTypeDef]],
        "resourceType": NotRequired[List[ResourceStringFilterTypeDef]],
    },
)
ResourceFilterCriteriaTypeDef = TypedDict(
    "ResourceFilterCriteriaTypeDef",
    {
        "accountId": NotRequired[Sequence[ResourceStringFilterTypeDef]],
        "ec2InstanceTags": NotRequired[Sequence[ResourceMapFilterTypeDef]],
        "ecrImageTags": NotRequired[Sequence[ResourceStringFilterTypeDef]],
        "ecrRepositoryName": NotRequired[Sequence[ResourceStringFilterTypeDef]],
        "lambdaFunctionName": NotRequired[Sequence[ResourceStringFilterTypeDef]],
        "lambdaFunctionTags": NotRequired[Sequence[ResourceMapFilterTypeDef]],
        "resourceId": NotRequired[Sequence[ResourceStringFilterTypeDef]],
        "resourceType": NotRequired[Sequence[ResourceStringFilterTypeDef]],
    },
)
SearchVulnerabilitiesRequestRequestTypeDef = TypedDict(
    "SearchVulnerabilitiesRequestRequestTypeDef",
    {
        "filterCriteria": SearchVulnerabilitiesFilterCriteriaTypeDef,
        "nextToken": NotRequired[str],
    },
)
SearchVulnerabilitiesRequestSearchVulnerabilitiesPaginateTypeDef = TypedDict(
    "SearchVulnerabilitiesRequestSearchVulnerabilitiesPaginateTypeDef",
    {
        "filterCriteria": SearchVulnerabilitiesFilterCriteriaTypeDef,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
StartCisSessionRequestRequestTypeDef = TypedDict(
    "StartCisSessionRequestRequestTypeDef",
    {
        "message": StartCisSessionMessageTypeDef,
        "scanJobId": str,
    },
)
StopCisSessionMessageTypeDef = TypedDict(
    "StopCisSessionMessageTypeDef",
    {
        "progress": StopCisMessageProgressTypeDef,
        "status": StopCisSessionStatusType,
        "benchmarkProfile": NotRequired[str],
        "benchmarkVersion": NotRequired[str],
        "computePlatform": NotRequired[ComputePlatformTypeDef],
        "reason": NotRequired[str],
    },
)
UsageTotalTypeDef = TypedDict(
    "UsageTotalTypeDef",
    {
        "accountId": NotRequired[str],
        "usage": NotRequired[List[UsageTypeDef]],
    },
)
AggregationResponseTypeDef = TypedDict(
    "AggregationResponseTypeDef",
    {
        "accountAggregation": NotRequired[AccountAggregationResponseTypeDef],
        "amiAggregation": NotRequired[AmiAggregationResponseTypeDef],
        "awsEcrContainerAggregation": NotRequired[AwsEcrContainerAggregationResponseTypeDef],
        "ec2InstanceAggregation": NotRequired[Ec2InstanceAggregationResponseTypeDef],
        "findingTypeAggregation": NotRequired[FindingTypeAggregationResponseTypeDef],
        "imageLayerAggregation": NotRequired[ImageLayerAggregationResponseTypeDef],
        "lambdaFunctionAggregation": NotRequired[LambdaFunctionAggregationResponseTypeDef],
        "lambdaLayerAggregation": NotRequired[LambdaLayerAggregationResponseTypeDef],
        "packageAggregation": NotRequired[PackageAggregationResponseTypeDef],
        "repositoryAggregation": NotRequired[RepositoryAggregationResponseTypeDef],
        "titleAggregation": NotRequired[TitleAggregationResponseTypeDef],
    },
)
AccountStateTypeDef = TypedDict(
    "AccountStateTypeDef",
    {
        "accountId": str,
        "resourceState": ResourceStateTypeDef,
        "state": StateTypeDef,
    },
)
DisableResponseTypeDef = TypedDict(
    "DisableResponseTypeDef",
    {
        "accounts": List[AccountTypeDef],
        "failedAccounts": List[FailedAccountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnableResponseTypeDef = TypedDict(
    "EnableResponseTypeDef",
    {
        "accounts": List[AccountTypeDef],
        "failedAccounts": List[FailedAccountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResourceDetailsTypeDef = TypedDict(
    "ResourceDetailsTypeDef",
    {
        "awsEc2Instance": NotRequired[AwsEc2InstanceDetailsTypeDef],
        "awsEcrContainerImage": NotRequired[AwsEcrContainerImageDetailsTypeDef],
        "awsLambdaFunction": NotRequired[AwsLambdaFunctionDetailsTypeDef],
    },
)
SendCisSessionTelemetryRequestRequestTypeDef = TypedDict(
    "SendCisSessionTelemetryRequestRequestTypeDef",
    {
        "messages": Sequence[CisSessionMessageTypeDef],
        "scanJobId": str,
        "sessionToken": str,
    },
)
ListCisScanResultsAggregatedByChecksResponseTypeDef = TypedDict(
    "ListCisScanResultsAggregatedByChecksResponseTypeDef",
    {
        "checkAggregations": List[CisCheckAggregationTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCisScanResultsAggregatedByTargetResourceResponseTypeDef = TypedDict(
    "ListCisScanResultsAggregatedByTargetResourceResponseTypeDef",
    {
        "nextToken": str,
        "targetResourceAggregations": List[CisTargetResourceAggregationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCisScansFilterCriteriaTypeDef = TypedDict(
    "ListCisScansFilterCriteriaTypeDef",
    {
        "failedChecksFilters": NotRequired[Sequence[CisNumberFilterTypeDef]],
        "scanArnFilters": NotRequired[Sequence[CisStringFilterTypeDef]],
        "scanAtFilters": NotRequired[Sequence[CisDateFilterTypeDef]],
        "scanConfigurationArnFilters": NotRequired[Sequence[CisStringFilterTypeDef]],
        "scanNameFilters": NotRequired[Sequence[CisStringFilterTypeDef]],
        "scanStatusFilters": NotRequired[Sequence[CisScanStatusFilterTypeDef]],
        "scheduledByFilters": NotRequired[Sequence[CisStringFilterTypeDef]],
        "targetAccountIdFilters": NotRequired[Sequence[CisStringFilterTypeDef]],
        "targetResourceIdFilters": NotRequired[Sequence[CisStringFilterTypeDef]],
        "targetResourceTagFilters": NotRequired[Sequence[TagFilterTypeDef]],
    },
)
CoverageFilterCriteriaTypeDef = TypedDict(
    "CoverageFilterCriteriaTypeDef",
    {
        "accountId": NotRequired[Sequence[CoverageStringFilterTypeDef]],
        "ec2InstanceTags": NotRequired[Sequence[CoverageMapFilterTypeDef]],
        "ecrImageTags": NotRequired[Sequence[CoverageStringFilterTypeDef]],
        "ecrRepositoryName": NotRequired[Sequence[CoverageStringFilterTypeDef]],
        "imagePulledAt": NotRequired[Sequence[CoverageDateFilterTypeDef]],
        "lambdaFunctionName": NotRequired[Sequence[CoverageStringFilterTypeDef]],
        "lambdaFunctionRuntime": NotRequired[Sequence[CoverageStringFilterTypeDef]],
        "lambdaFunctionTags": NotRequired[Sequence[CoverageMapFilterTypeDef]],
        "lastScannedAt": NotRequired[Sequence[CoverageDateFilterTypeDef]],
        "resourceId": NotRequired[Sequence[CoverageStringFilterTypeDef]],
        "resourceType": NotRequired[Sequence[CoverageStringFilterTypeDef]],
        "scanMode": NotRequired[Sequence[CoverageStringFilterTypeDef]],
        "scanStatusCode": NotRequired[Sequence[CoverageStringFilterTypeDef]],
        "scanStatusReason": NotRequired[Sequence[CoverageStringFilterTypeDef]],
        "scanType": NotRequired[Sequence[CoverageStringFilterTypeDef]],
    },
)
DateFilterUnionTypeDef = Union[DateFilterTypeDef, DateFilterOutputTypeDef]
ListCisScansResponseTypeDef = TypedDict(
    "ListCisScansResponseTypeDef",
    {
        "nextToken": str,
        "scans": List[CisScanTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCisScanResultDetailsRequestGetCisScanResultDetailsPaginateTypeDef = TypedDict(
    "GetCisScanResultDetailsRequestGetCisScanResultDetailsPaginateTypeDef",
    {
        "accountId": str,
        "scanArn": str,
        "targetResourceId": str,
        "filterCriteria": NotRequired[CisScanResultDetailsFilterCriteriaTypeDef],
        "sortBy": NotRequired[CisScanResultDetailsSortByType],
        "sortOrder": NotRequired[CisSortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetCisScanResultDetailsRequestRequestTypeDef = TypedDict(
    "GetCisScanResultDetailsRequestRequestTypeDef",
    {
        "accountId": str,
        "scanArn": str,
        "targetResourceId": str,
        "filterCriteria": NotRequired[CisScanResultDetailsFilterCriteriaTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortBy": NotRequired[CisScanResultDetailsSortByType],
        "sortOrder": NotRequired[CisSortOrderType],
    },
)
ListCisScanResultsAggregatedByChecksRequestListCisScanResultsAggregatedByChecksPaginateTypeDef = TypedDict(
    "ListCisScanResultsAggregatedByChecksRequestListCisScanResultsAggregatedByChecksPaginateTypeDef",
    {
        "scanArn": str,
        "filterCriteria": NotRequired[CisScanResultsAggregatedByChecksFilterCriteriaTypeDef],
        "sortBy": NotRequired[CisScanResultsAggregatedByChecksSortByType],
        "sortOrder": NotRequired[CisSortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCisScanResultsAggregatedByChecksRequestRequestTypeDef = TypedDict(
    "ListCisScanResultsAggregatedByChecksRequestRequestTypeDef",
    {
        "scanArn": str,
        "filterCriteria": NotRequired[CisScanResultsAggregatedByChecksFilterCriteriaTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortBy": NotRequired[CisScanResultsAggregatedByChecksSortByType],
        "sortOrder": NotRequired[CisSortOrderType],
    },
)
ListCisScanResultsAggregatedByTargetResourceRequestListCisScanResultsAggregatedByTargetResourcePaginateTypeDef = TypedDict(
    "ListCisScanResultsAggregatedByTargetResourceRequestListCisScanResultsAggregatedByTargetResourcePaginateTypeDef",
    {
        "scanArn": str,
        "filterCriteria": NotRequired[
            CisScanResultsAggregatedByTargetResourceFilterCriteriaTypeDef
        ],
        "sortBy": NotRequired[CisScanResultsAggregatedByTargetResourceSortByType],
        "sortOrder": NotRequired[CisSortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCisScanResultsAggregatedByTargetResourceRequestRequestTypeDef = TypedDict(
    "ListCisScanResultsAggregatedByTargetResourceRequestRequestTypeDef",
    {
        "scanArn": str,
        "filterCriteria": NotRequired[
            CisScanResultsAggregatedByTargetResourceFilterCriteriaTypeDef
        ],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortBy": NotRequired[CisScanResultsAggregatedByTargetResourceSortByType],
        "sortOrder": NotRequired[CisSortOrderType],
    },
)
ListCisScanConfigurationsRequestListCisScanConfigurationsPaginateTypeDef = TypedDict(
    "ListCisScanConfigurationsRequestListCisScanConfigurationsPaginateTypeDef",
    {
        "filterCriteria": NotRequired[ListCisScanConfigurationsFilterCriteriaTypeDef],
        "sortBy": NotRequired[CisScanConfigurationsSortByType],
        "sortOrder": NotRequired[CisSortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCisScanConfigurationsRequestRequestTypeDef = TypedDict(
    "ListCisScanConfigurationsRequestRequestTypeDef",
    {
        "filterCriteria": NotRequired[ListCisScanConfigurationsFilterCriteriaTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortBy": NotRequired[CisScanConfigurationsSortByType],
        "sortOrder": NotRequired[CisSortOrderType],
    },
)
BatchGetCodeSnippetResponseTypeDef = TypedDict(
    "BatchGetCodeSnippetResponseTypeDef",
    {
        "codeSnippetResults": List[CodeSnippetResultTypeDef],
        "errors": List[CodeSnippetErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InspectorScoreDetailsTypeDef = TypedDict(
    "InspectorScoreDetailsTypeDef",
    {
        "adjustedCvss": NotRequired[CvssScoreDetailsTypeDef],
    },
)
ScheduleOutputTypeDef = TypedDict(
    "ScheduleOutputTypeDef",
    {
        "daily": NotRequired[DailyScheduleTypeDef],
        "monthly": NotRequired[MonthlyScheduleTypeDef],
        "oneTime": NotRequired[Dict[str, Any]],
        "weekly": NotRequired[WeeklyScheduleOutputTypeDef],
    },
)
WeeklyScheduleUnionTypeDef = Union[WeeklyScheduleTypeDef, WeeklyScheduleOutputTypeDef]
AggregationRequestTypeDef = TypedDict(
    "AggregationRequestTypeDef",
    {
        "accountAggregation": NotRequired[AccountAggregationTypeDef],
        "amiAggregation": NotRequired[AmiAggregationTypeDef],
        "awsEcrContainerAggregation": NotRequired[AwsEcrContainerAggregationTypeDef],
        "ec2InstanceAggregation": NotRequired[Ec2InstanceAggregationTypeDef],
        "findingTypeAggregation": NotRequired[FindingTypeAggregationTypeDef],
        "imageLayerAggregation": NotRequired[ImageLayerAggregationTypeDef],
        "lambdaFunctionAggregation": NotRequired[LambdaFunctionAggregationTypeDef],
        "lambdaLayerAggregation": NotRequired[LambdaLayerAggregationTypeDef],
        "packageAggregation": NotRequired[PackageAggregationTypeDef],
        "repositoryAggregation": NotRequired[RepositoryAggregationTypeDef],
        "titleAggregation": NotRequired[TitleAggregationTypeDef],
    },
)
GetConfigurationResponseTypeDef = TypedDict(
    "GetConfigurationResponseTypeDef",
    {
        "ec2Configuration": Ec2ConfigurationStateTypeDef,
        "ecrConfiguration": EcrConfigurationStateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetFindingDetailsResponseTypeDef = TypedDict(
    "BatchGetFindingDetailsResponseTypeDef",
    {
        "errors": List[FindingDetailsErrorTypeDef],
        "findingDetails": List[FindingDetailTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchVulnerabilitiesResponseTypeDef = TypedDict(
    "SearchVulnerabilitiesResponseTypeDef",
    {
        "nextToken": str,
        "vulnerabilities": List[VulnerabilityTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FilterCriteriaOutputTypeDef = TypedDict(
    "FilterCriteriaOutputTypeDef",
    {
        "awsAccountId": NotRequired[List[StringFilterTypeDef]],
        "codeVulnerabilityDetectorName": NotRequired[List[StringFilterTypeDef]],
        "codeVulnerabilityDetectorTags": NotRequired[List[StringFilterTypeDef]],
        "codeVulnerabilityFilePath": NotRequired[List[StringFilterTypeDef]],
        "componentId": NotRequired[List[StringFilterTypeDef]],
        "componentType": NotRequired[List[StringFilterTypeDef]],
        "ec2InstanceImageId": NotRequired[List[StringFilterTypeDef]],
        "ec2InstanceSubnetId": NotRequired[List[StringFilterTypeDef]],
        "ec2InstanceVpcId": NotRequired[List[StringFilterTypeDef]],
        "ecrImageArchitecture": NotRequired[List[StringFilterTypeDef]],
        "ecrImageHash": NotRequired[List[StringFilterTypeDef]],
        "ecrImagePushedAt": NotRequired[List[DateFilterOutputTypeDef]],
        "ecrImageRegistry": NotRequired[List[StringFilterTypeDef]],
        "ecrImageRepositoryName": NotRequired[List[StringFilterTypeDef]],
        "ecrImageTags": NotRequired[List[StringFilterTypeDef]],
        "epssScore": NotRequired[List[NumberFilterTypeDef]],
        "exploitAvailable": NotRequired[List[StringFilterTypeDef]],
        "findingArn": NotRequired[List[StringFilterTypeDef]],
        "findingStatus": NotRequired[List[StringFilterTypeDef]],
        "findingType": NotRequired[List[StringFilterTypeDef]],
        "firstObservedAt": NotRequired[List[DateFilterOutputTypeDef]],
        "fixAvailable": NotRequired[List[StringFilterTypeDef]],
        "inspectorScore": NotRequired[List[NumberFilterTypeDef]],
        "lambdaFunctionExecutionRoleArn": NotRequired[List[StringFilterTypeDef]],
        "lambdaFunctionLastModifiedAt": NotRequired[List[DateFilterOutputTypeDef]],
        "lambdaFunctionLayers": NotRequired[List[StringFilterTypeDef]],
        "lambdaFunctionName": NotRequired[List[StringFilterTypeDef]],
        "lambdaFunctionRuntime": NotRequired[List[StringFilterTypeDef]],
        "lastObservedAt": NotRequired[List[DateFilterOutputTypeDef]],
        "networkProtocol": NotRequired[List[StringFilterTypeDef]],
        "portRange": NotRequired[List[PortRangeFilterTypeDef]],
        "relatedVulnerabilities": NotRequired[List[StringFilterTypeDef]],
        "resourceId": NotRequired[List[StringFilterTypeDef]],
        "resourceTags": NotRequired[List[MapFilterTypeDef]],
        "resourceType": NotRequired[List[StringFilterTypeDef]],
        "severity": NotRequired[List[StringFilterTypeDef]],
        "title": NotRequired[List[StringFilterTypeDef]],
        "updatedAt": NotRequired[List[DateFilterOutputTypeDef]],
        "vendorSeverity": NotRequired[List[StringFilterTypeDef]],
        "vulnerabilityId": NotRequired[List[StringFilterTypeDef]],
        "vulnerabilitySource": NotRequired[List[StringFilterTypeDef]],
        "vulnerablePackages": NotRequired[List[PackageFilterTypeDef]],
    },
)
BatchGetFreeTrialInfoResponseTypeDef = TypedDict(
    "BatchGetFreeTrialInfoResponseTypeDef",
    {
        "accounts": List[FreeTrialAccountInfoTypeDef],
        "failedAccounts": List[FreeTrialInfoErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CoveredResourceTypeDef = TypedDict(
    "CoveredResourceTypeDef",
    {
        "accountId": str,
        "resourceId": str,
        "resourceType": CoverageResourceTypeType,
        "scanType": ScanTypeType,
        "lastScannedAt": NotRequired[datetime],
        "resourceMetadata": NotRequired[ResourceScanMetadataTypeDef],
        "scanMode": NotRequired[ScanModeType],
        "scanStatus": NotRequired[ScanStatusTypeDef],
    },
)
NetworkReachabilityDetailsTypeDef = TypedDict(
    "NetworkReachabilityDetailsTypeDef",
    {
        "networkPath": NetworkPathTypeDef,
        "openPortRange": PortRangeTypeDef,
        "protocol": NetworkProtocolType,
    },
)
GetSbomExportResponseTypeDef = TypedDict(
    "GetSbomExportResponseTypeDef",
    {
        "errorCode": ReportingErrorCodeType,
        "errorMessage": str,
        "filterCriteria": ResourceFilterCriteriaOutputTypeDef,
        "format": SbomReportFormatType,
        "reportId": str,
        "s3Destination": DestinationTypeDef,
        "status": ExternalReportStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSbomExportRequestRequestTypeDef = TypedDict(
    "CreateSbomExportRequestRequestTypeDef",
    {
        "reportFormat": SbomReportFormatType,
        "s3Destination": DestinationTypeDef,
        "resourceFilterCriteria": NotRequired[ResourceFilterCriteriaTypeDef],
    },
)
StopCisSessionRequestRequestTypeDef = TypedDict(
    "StopCisSessionRequestRequestTypeDef",
    {
        "message": StopCisSessionMessageTypeDef,
        "scanJobId": str,
        "sessionToken": str,
    },
)
ListUsageTotalsResponseTypeDef = TypedDict(
    "ListUsageTotalsResponseTypeDef",
    {
        "nextToken": str,
        "totals": List[UsageTotalTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListFindingAggregationsResponseTypeDef = TypedDict(
    "ListFindingAggregationsResponseTypeDef",
    {
        "aggregationType": AggregationTypeType,
        "nextToken": str,
        "responses": List[AggregationResponseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetAccountStatusResponseTypeDef = TypedDict(
    "BatchGetAccountStatusResponseTypeDef",
    {
        "accounts": List[AccountStateTypeDef],
        "failedAccounts": List[FailedAccountTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "id": str,
        "type": ResourceTypeType,
        "details": NotRequired[ResourceDetailsTypeDef],
        "partition": NotRequired[str],
        "region": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)
ListCisScansRequestListCisScansPaginateTypeDef = TypedDict(
    "ListCisScansRequestListCisScansPaginateTypeDef",
    {
        "detailLevel": NotRequired[ListCisScansDetailLevelType],
        "filterCriteria": NotRequired[ListCisScansFilterCriteriaTypeDef],
        "sortBy": NotRequired[ListCisScansSortByType],
        "sortOrder": NotRequired[CisSortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCisScansRequestRequestTypeDef = TypedDict(
    "ListCisScansRequestRequestTypeDef",
    {
        "detailLevel": NotRequired[ListCisScansDetailLevelType],
        "filterCriteria": NotRequired[ListCisScansFilterCriteriaTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortBy": NotRequired[ListCisScansSortByType],
        "sortOrder": NotRequired[CisSortOrderType],
    },
)
ListCoverageRequestListCoveragePaginateTypeDef = TypedDict(
    "ListCoverageRequestListCoveragePaginateTypeDef",
    {
        "filterCriteria": NotRequired[CoverageFilterCriteriaTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCoverageRequestRequestTypeDef = TypedDict(
    "ListCoverageRequestRequestTypeDef",
    {
        "filterCriteria": NotRequired[CoverageFilterCriteriaTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListCoverageStatisticsRequestListCoverageStatisticsPaginateTypeDef = TypedDict(
    "ListCoverageStatisticsRequestListCoverageStatisticsPaginateTypeDef",
    {
        "filterCriteria": NotRequired[CoverageFilterCriteriaTypeDef],
        "groupBy": NotRequired[GroupKeyType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCoverageStatisticsRequestRequestTypeDef = TypedDict(
    "ListCoverageStatisticsRequestRequestTypeDef",
    {
        "filterCriteria": NotRequired[CoverageFilterCriteriaTypeDef],
        "groupBy": NotRequired[GroupKeyType],
        "nextToken": NotRequired[str],
    },
)
FilterCriteriaTypeDef = TypedDict(
    "FilterCriteriaTypeDef",
    {
        "awsAccountId": NotRequired[Sequence[StringFilterTypeDef]],
        "codeVulnerabilityDetectorName": NotRequired[Sequence[StringFilterTypeDef]],
        "codeVulnerabilityDetectorTags": NotRequired[Sequence[StringFilterTypeDef]],
        "codeVulnerabilityFilePath": NotRequired[Sequence[StringFilterTypeDef]],
        "componentId": NotRequired[Sequence[StringFilterTypeDef]],
        "componentType": NotRequired[Sequence[StringFilterTypeDef]],
        "ec2InstanceImageId": NotRequired[Sequence[StringFilterTypeDef]],
        "ec2InstanceSubnetId": NotRequired[Sequence[StringFilterTypeDef]],
        "ec2InstanceVpcId": NotRequired[Sequence[StringFilterTypeDef]],
        "ecrImageArchitecture": NotRequired[Sequence[StringFilterTypeDef]],
        "ecrImageHash": NotRequired[Sequence[StringFilterTypeDef]],
        "ecrImagePushedAt": NotRequired[Sequence[DateFilterUnionTypeDef]],
        "ecrImageRegistry": NotRequired[Sequence[StringFilterTypeDef]],
        "ecrImageRepositoryName": NotRequired[Sequence[StringFilterTypeDef]],
        "ecrImageTags": NotRequired[Sequence[StringFilterTypeDef]],
        "epssScore": NotRequired[Sequence[NumberFilterTypeDef]],
        "exploitAvailable": NotRequired[Sequence[StringFilterTypeDef]],
        "findingArn": NotRequired[Sequence[StringFilterTypeDef]],
        "findingStatus": NotRequired[Sequence[StringFilterTypeDef]],
        "findingType": NotRequired[Sequence[StringFilterTypeDef]],
        "firstObservedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "fixAvailable": NotRequired[Sequence[StringFilterTypeDef]],
        "inspectorScore": NotRequired[Sequence[NumberFilterTypeDef]],
        "lambdaFunctionExecutionRoleArn": NotRequired[Sequence[StringFilterTypeDef]],
        "lambdaFunctionLastModifiedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "lambdaFunctionLayers": NotRequired[Sequence[StringFilterTypeDef]],
        "lambdaFunctionName": NotRequired[Sequence[StringFilterTypeDef]],
        "lambdaFunctionRuntime": NotRequired[Sequence[StringFilterTypeDef]],
        "lastObservedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "networkProtocol": NotRequired[Sequence[StringFilterTypeDef]],
        "portRange": NotRequired[Sequence[PortRangeFilterTypeDef]],
        "relatedVulnerabilities": NotRequired[Sequence[StringFilterTypeDef]],
        "resourceId": NotRequired[Sequence[StringFilterTypeDef]],
        "resourceTags": NotRequired[Sequence[MapFilterTypeDef]],
        "resourceType": NotRequired[Sequence[StringFilterTypeDef]],
        "severity": NotRequired[Sequence[StringFilterTypeDef]],
        "title": NotRequired[Sequence[StringFilterTypeDef]],
        "updatedAt": NotRequired[Sequence[DateFilterTypeDef]],
        "vendorSeverity": NotRequired[Sequence[StringFilterTypeDef]],
        "vulnerabilityId": NotRequired[Sequence[StringFilterTypeDef]],
        "vulnerabilitySource": NotRequired[Sequence[StringFilterTypeDef]],
        "vulnerablePackages": NotRequired[Sequence[PackageFilterTypeDef]],
    },
)
CisScanConfigurationTypeDef = TypedDict(
    "CisScanConfigurationTypeDef",
    {
        "scanConfigurationArn": str,
        "ownerId": NotRequired[str],
        "scanName": NotRequired[str],
        "schedule": NotRequired[ScheduleOutputTypeDef],
        "securityLevel": NotRequired[CisSecurityLevelType],
        "tags": NotRequired[Dict[str, str]],
        "targets": NotRequired[CisTargetsTypeDef],
    },
)
ScheduleTypeDef = TypedDict(
    "ScheduleTypeDef",
    {
        "daily": NotRequired[DailyScheduleTypeDef],
        "monthly": NotRequired[MonthlyScheduleTypeDef],
        "oneTime": NotRequired[Mapping[str, Any]],
        "weekly": NotRequired[WeeklyScheduleUnionTypeDef],
    },
)
ListFindingAggregationsRequestListFindingAggregationsPaginateTypeDef = TypedDict(
    "ListFindingAggregationsRequestListFindingAggregationsPaginateTypeDef",
    {
        "aggregationType": AggregationTypeType,
        "accountIds": NotRequired[Sequence[StringFilterTypeDef]],
        "aggregationRequest": NotRequired[AggregationRequestTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFindingAggregationsRequestRequestTypeDef = TypedDict(
    "ListFindingAggregationsRequestRequestTypeDef",
    {
        "aggregationType": AggregationTypeType,
        "accountIds": NotRequired[Sequence[StringFilterTypeDef]],
        "aggregationRequest": NotRequired[AggregationRequestTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "action": FilterActionType,
        "arn": str,
        "createdAt": datetime,
        "criteria": FilterCriteriaOutputTypeDef,
        "name": str,
        "ownerId": str,
        "updatedAt": datetime,
        "description": NotRequired[str],
        "reason": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)
GetFindingsReportStatusResponseTypeDef = TypedDict(
    "GetFindingsReportStatusResponseTypeDef",
    {
        "destination": DestinationTypeDef,
        "errorCode": ReportingErrorCodeType,
        "errorMessage": str,
        "filterCriteria": FilterCriteriaOutputTypeDef,
        "reportId": str,
        "status": ExternalReportStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCoverageResponseTypeDef = TypedDict(
    "ListCoverageResponseTypeDef",
    {
        "coveredResources": List[CoveredResourceTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FindingTypeDef = TypedDict(
    "FindingTypeDef",
    {
        "awsAccountId": str,
        "description": str,
        "findingArn": str,
        "firstObservedAt": datetime,
        "lastObservedAt": datetime,
        "remediation": RemediationTypeDef,
        "resources": List[ResourceTypeDef],
        "severity": SeverityType,
        "status": FindingStatusType,
        "type": FindingTypeType,
        "codeVulnerabilityDetails": NotRequired[CodeVulnerabilityDetailsTypeDef],
        "epss": NotRequired[EpssDetailsTypeDef],
        "exploitAvailable": NotRequired[ExploitAvailableType],
        "exploitabilityDetails": NotRequired[ExploitabilityDetailsTypeDef],
        "fixAvailable": NotRequired[FixAvailableType],
        "inspectorScore": NotRequired[float],
        "inspectorScoreDetails": NotRequired[InspectorScoreDetailsTypeDef],
        "networkReachabilityDetails": NotRequired[NetworkReachabilityDetailsTypeDef],
        "packageVulnerabilityDetails": NotRequired[PackageVulnerabilityDetailsTypeDef],
        "title": NotRequired[str],
        "updatedAt": NotRequired[datetime],
    },
)
CreateFilterRequestRequestTypeDef = TypedDict(
    "CreateFilterRequestRequestTypeDef",
    {
        "action": FilterActionType,
        "filterCriteria": FilterCriteriaTypeDef,
        "name": str,
        "description": NotRequired[str],
        "reason": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateFindingsReportRequestRequestTypeDef = TypedDict(
    "CreateFindingsReportRequestRequestTypeDef",
    {
        "reportFormat": ReportFormatType,
        "s3Destination": DestinationTypeDef,
        "filterCriteria": NotRequired[FilterCriteriaTypeDef],
    },
)
ListFindingsRequestListFindingsPaginateTypeDef = TypedDict(
    "ListFindingsRequestListFindingsPaginateTypeDef",
    {
        "filterCriteria": NotRequired[FilterCriteriaTypeDef],
        "sortCriteria": NotRequired[SortCriteriaTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFindingsRequestRequestTypeDef = TypedDict(
    "ListFindingsRequestRequestTypeDef",
    {
        "filterCriteria": NotRequired[FilterCriteriaTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortCriteria": NotRequired[SortCriteriaTypeDef],
    },
)
UpdateFilterRequestRequestTypeDef = TypedDict(
    "UpdateFilterRequestRequestTypeDef",
    {
        "filterArn": str,
        "action": NotRequired[FilterActionType],
        "description": NotRequired[str],
        "filterCriteria": NotRequired[FilterCriteriaTypeDef],
        "name": NotRequired[str],
        "reason": NotRequired[str],
    },
)
ListCisScanConfigurationsResponseTypeDef = TypedDict(
    "ListCisScanConfigurationsResponseTypeDef",
    {
        "nextToken": str,
        "scanConfigurations": List[CisScanConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCisScanConfigurationRequestRequestTypeDef = TypedDict(
    "CreateCisScanConfigurationRequestRequestTypeDef",
    {
        "scanName": str,
        "schedule": ScheduleTypeDef,
        "securityLevel": CisSecurityLevelType,
        "targets": CreateCisTargetsTypeDef,
        "tags": NotRequired[Mapping[str, str]],
    },
)
UpdateCisScanConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateCisScanConfigurationRequestRequestTypeDef",
    {
        "scanConfigurationArn": str,
        "scanName": NotRequired[str],
        "schedule": NotRequired[ScheduleTypeDef],
        "securityLevel": NotRequired[CisSecurityLevelType],
        "targets": NotRequired[UpdateCisTargetsTypeDef],
    },
)
ListFiltersResponseTypeDef = TypedDict(
    "ListFiltersResponseTypeDef",
    {
        "filters": List[FilterTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListFindingsResponseTypeDef = TypedDict(
    "ListFindingsResponseTypeDef",
    {
        "findings": List[FindingTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
