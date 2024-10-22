"""
Type annotations for migrationhubstrategy service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/type_defs/)

Usage::

    ```python
    from mypy_boto3_migrationhubstrategy.type_defs import AnalysisStatusUnionTypeDef

    data: AnalysisStatusUnionTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    AnalysisTypeType,
    AntipatternReportStatusType,
    ApplicationComponentCriteriaType,
    ApplicationModeType,
    AppTypeType,
    AppUnitErrorCategoryType,
    AssessmentDataSourceTypeType,
    AssessmentStatusType,
    AuthTypeType,
    AwsManagedTargetDestinationType,
    BinaryAnalyzerNameType,
    CollectorHealthType,
    ConditionType,
    DatabaseManagementPreferenceType,
    DataSourceTypeType,
    GroupNameType,
    HeterogeneousTargetDatabaseEngineType,
    ImportFileTaskStatusType,
    InclusionStatusType,
    NoPreferenceTargetDestinationType,
    OSTypeType,
    OutputFormatType,
    RecommendationReportStatusType,
    ResourceSubTypeType,
    RuntimeAnalysisStatusType,
    RunTimeAnalyzerNameType,
    RunTimeAssessmentStatusType,
    SelfManageTargetDestinationType,
    ServerCriteriaType,
    ServerErrorCategoryType,
    ServerOsTypeType,
    SeverityType,
    SortOrderType,
    SourceCodeAnalyzerNameType,
    SrcCodeOrDbAnalysisStatusType,
    StrategyRecommendationType,
    StrategyType,
    TargetDatabaseEngineType,
    TargetDestinationType,
    TransformationToolNameType,
    VersionControlType,
    VersionControlTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AnalysisStatusUnionTypeDef",
    "AnalyzableServerSummaryTypeDef",
    "AnalyzerNameUnionTypeDef",
    "S3ObjectTypeDef",
    "AntipatternSeveritySummaryTypeDef",
    "AppUnitErrorTypeDef",
    "DatabaseConfigDetailTypeDef",
    "SourceCodeRepositoryTypeDef",
    "ApplicationComponentStatusSummaryTypeDef",
    "ApplicationComponentSummaryTypeDef",
    "ServerStatusSummaryTypeDef",
    "ServerSummaryTypeDef",
    "StrategySummaryTypeDef",
    "AssessmentTargetOutputTypeDef",
    "AssessmentTargetTypeDef",
    "AssociatedApplicationTypeDef",
    "AwsManagedResourcesOutputTypeDef",
    "AwsManagedResourcesTypeDef",
    "BusinessGoalsTypeDef",
    "IPAddressBasedRemoteInfoTypeDef",
    "PipelineInfoTypeDef",
    "RemoteSourceCodeAnalysisServerInfoTypeDef",
    "VcenterBasedRemoteInfoTypeDef",
    "VersionControlInfoTypeDef",
    "DataCollectionDetailsTypeDef",
    "HeterogeneousOutputTypeDef",
    "HomogeneousOutputTypeDef",
    "NoDatabaseMigrationPreferenceOutputTypeDef",
    "GetApplicationComponentDetailsRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "GetApplicationComponentStrategiesRequestRequestTypeDef",
    "GetAssessmentRequestRequestTypeDef",
    "GetImportFileTaskRequestRequestTypeDef",
    "GetRecommendationReportDetailsRequestRequestTypeDef",
    "RecommendationReportDetailsTypeDef",
    "PaginatorConfigTypeDef",
    "GetServerDetailsRequestRequestTypeDef",
    "GetServerStrategiesRequestRequestTypeDef",
    "GroupTypeDef",
    "HeterogeneousTypeDef",
    "HomogeneousTypeDef",
    "ImportFileTaskInformationTypeDef",
    "ListAnalyzableServersRequestRequestTypeDef",
    "ListCollectorsRequestRequestTypeDef",
    "ListImportFileTaskRequestRequestTypeDef",
    "NoManagementPreferenceOutputTypeDef",
    "SelfManageResourcesOutputTypeDef",
    "NetworkInfoTypeDef",
    "NoDatabaseMigrationPreferenceTypeDef",
    "NoManagementPreferenceTypeDef",
    "OSInfoTypeDef",
    "TransformationToolTypeDef",
    "SelfManageResourcesTypeDef",
    "ServerErrorTypeDef",
    "SourceCodeTypeDef",
    "StopAssessmentRequestRequestTypeDef",
    "StrategyOptionTypeDef",
    "AntipatternReportResultTypeDef",
    "AssessmentSummaryTypeDef",
    "AssessmentTargetUnionTypeDef",
    "AwsManagedResourcesUnionTypeDef",
    "PrioritizeBusinessGoalsTypeDef",
    "ConfigurationSummaryTypeDef",
    "DatabaseMigrationPreferenceOutputTypeDef",
    "GetAssessmentResponseTypeDef",
    "GetImportFileTaskResponseTypeDef",
    "GetLatestAssessmentIdResponseTypeDef",
    "ListAnalyzableServersResponseTypeDef",
    "StartAssessmentResponseTypeDef",
    "StartImportFileTaskResponseTypeDef",
    "StartRecommendationReportGenerationResponseTypeDef",
    "GetRecommendationReportDetailsResponseTypeDef",
    "GetServerDetailsRequestGetServerDetailsPaginateTypeDef",
    "ListAnalyzableServersRequestListAnalyzableServersPaginateTypeDef",
    "ListCollectorsRequestListCollectorsPaginateTypeDef",
    "ListImportFileTaskRequestListImportFileTaskPaginateTypeDef",
    "ListApplicationComponentsRequestListApplicationComponentsPaginateTypeDef",
    "ListApplicationComponentsRequestRequestTypeDef",
    "ListServersRequestListServersPaginateTypeDef",
    "ListServersRequestRequestTypeDef",
    "StartImportFileTaskRequestRequestTypeDef",
    "StartRecommendationReportGenerationRequestRequestTypeDef",
    "HeterogeneousUnionTypeDef",
    "HomogeneousUnionTypeDef",
    "ListImportFileTaskResponseTypeDef",
    "ManagementPreferenceOutputTypeDef",
    "NoDatabaseMigrationPreferenceUnionTypeDef",
    "NoManagementPreferenceUnionTypeDef",
    "SystemInfoTypeDef",
    "RecommendationSetTypeDef",
    "SelfManageResourcesUnionTypeDef",
    "UpdateApplicationComponentConfigRequestRequestTypeDef",
    "UpdateServerConfigRequestRequestTypeDef",
    "ResultTypeDef",
    "GetPortfolioSummaryResponseTypeDef",
    "StartAssessmentRequestRequestTypeDef",
    "CollectorTypeDef",
    "DatabasePreferencesOutputTypeDef",
    "ApplicationPreferencesOutputTypeDef",
    "DatabaseMigrationPreferenceTypeDef",
    "ApplicationComponentStrategyTypeDef",
    "ServerDetailTypeDef",
    "ServerStrategyTypeDef",
    "ManagementPreferenceTypeDef",
    "ApplicationComponentDetailTypeDef",
    "ListCollectorsResponseTypeDef",
    "GetPortfolioPreferencesResponseTypeDef",
    "DatabaseMigrationPreferenceUnionTypeDef",
    "GetApplicationComponentStrategiesResponseTypeDef",
    "GetServerDetailsResponseTypeDef",
    "ListServersResponseTypeDef",
    "GetServerStrategiesResponseTypeDef",
    "ManagementPreferenceUnionTypeDef",
    "GetApplicationComponentDetailsResponseTypeDef",
    "ListApplicationComponentsResponseTypeDef",
    "DatabasePreferencesTypeDef",
    "ApplicationPreferencesTypeDef",
    "PutPortfolioPreferencesRequestRequestTypeDef",
)

AnalysisStatusUnionTypeDef = TypedDict(
    "AnalysisStatusUnionTypeDef",
    {
        "runtimeAnalysisStatus": NotRequired[RuntimeAnalysisStatusType],
        "srcCodeOrDbAnalysisStatus": NotRequired[SrcCodeOrDbAnalysisStatusType],
    },
)
AnalyzableServerSummaryTypeDef = TypedDict(
    "AnalyzableServerSummaryTypeDef",
    {
        "hostname": NotRequired[str],
        "ipAddress": NotRequired[str],
        "source": NotRequired[str],
        "vmId": NotRequired[str],
    },
)
AnalyzerNameUnionTypeDef = TypedDict(
    "AnalyzerNameUnionTypeDef",
    {
        "binaryAnalyzerName": NotRequired[BinaryAnalyzerNameType],
        "runTimeAnalyzerName": NotRequired[RunTimeAnalyzerNameType],
        "sourceCodeAnalyzerName": NotRequired[SourceCodeAnalyzerNameType],
    },
)
S3ObjectTypeDef = TypedDict(
    "S3ObjectTypeDef",
    {
        "s3Bucket": NotRequired[str],
        "s3key": NotRequired[str],
    },
)
AntipatternSeveritySummaryTypeDef = TypedDict(
    "AntipatternSeveritySummaryTypeDef",
    {
        "count": NotRequired[int],
        "severity": NotRequired[SeverityType],
    },
)
AppUnitErrorTypeDef = TypedDict(
    "AppUnitErrorTypeDef",
    {
        "appUnitErrorCategory": NotRequired[AppUnitErrorCategoryType],
    },
)
DatabaseConfigDetailTypeDef = TypedDict(
    "DatabaseConfigDetailTypeDef",
    {
        "secretName": NotRequired[str],
    },
)
SourceCodeRepositoryTypeDef = TypedDict(
    "SourceCodeRepositoryTypeDef",
    {
        "branch": NotRequired[str],
        "projectName": NotRequired[str],
        "repository": NotRequired[str],
        "versionControlType": NotRequired[str],
    },
)
ApplicationComponentStatusSummaryTypeDef = TypedDict(
    "ApplicationComponentStatusSummaryTypeDef",
    {
        "count": NotRequired[int],
        "srcCodeOrDbAnalysisStatus": NotRequired[SrcCodeOrDbAnalysisStatusType],
    },
)
ApplicationComponentSummaryTypeDef = TypedDict(
    "ApplicationComponentSummaryTypeDef",
    {
        "appType": NotRequired[AppTypeType],
        "count": NotRequired[int],
    },
)
ServerStatusSummaryTypeDef = TypedDict(
    "ServerStatusSummaryTypeDef",
    {
        "count": NotRequired[int],
        "runTimeAssessmentStatus": NotRequired[RunTimeAssessmentStatusType],
    },
)
ServerSummaryTypeDef = TypedDict(
    "ServerSummaryTypeDef",
    {
        "ServerOsType": NotRequired[ServerOsTypeType],
        "count": NotRequired[int],
    },
)
StrategySummaryTypeDef = TypedDict(
    "StrategySummaryTypeDef",
    {
        "count": NotRequired[int],
        "strategy": NotRequired[StrategyType],
    },
)
AssessmentTargetOutputTypeDef = TypedDict(
    "AssessmentTargetOutputTypeDef",
    {
        "condition": ConditionType,
        "name": str,
        "values": List[str],
    },
)
AssessmentTargetTypeDef = TypedDict(
    "AssessmentTargetTypeDef",
    {
        "condition": ConditionType,
        "name": str,
        "values": Sequence[str],
    },
)
AssociatedApplicationTypeDef = TypedDict(
    "AssociatedApplicationTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
    },
)
AwsManagedResourcesOutputTypeDef = TypedDict(
    "AwsManagedResourcesOutputTypeDef",
    {
        "targetDestination": List[AwsManagedTargetDestinationType],
    },
)
AwsManagedResourcesTypeDef = TypedDict(
    "AwsManagedResourcesTypeDef",
    {
        "targetDestination": Sequence[AwsManagedTargetDestinationType],
    },
)
BusinessGoalsTypeDef = TypedDict(
    "BusinessGoalsTypeDef",
    {
        "licenseCostReduction": NotRequired[int],
        "modernizeInfrastructureWithCloudNativeTechnologies": NotRequired[int],
        "reduceOperationalOverheadWithManagedServices": NotRequired[int],
        "speedOfMigration": NotRequired[int],
    },
)
IPAddressBasedRemoteInfoTypeDef = TypedDict(
    "IPAddressBasedRemoteInfoTypeDef",
    {
        "authType": NotRequired[AuthTypeType],
        "ipAddressConfigurationTimeStamp": NotRequired[str],
        "osType": NotRequired[OSTypeType],
    },
)
PipelineInfoTypeDef = TypedDict(
    "PipelineInfoTypeDef",
    {
        "pipelineConfigurationTimeStamp": NotRequired[str],
        "pipelineType": NotRequired[Literal["AZURE_DEVOPS"]],
    },
)
RemoteSourceCodeAnalysisServerInfoTypeDef = TypedDict(
    "RemoteSourceCodeAnalysisServerInfoTypeDef",
    {
        "remoteSourceCodeAnalysisServerConfigurationTimestamp": NotRequired[str],
    },
)
VcenterBasedRemoteInfoTypeDef = TypedDict(
    "VcenterBasedRemoteInfoTypeDef",
    {
        "osType": NotRequired[OSTypeType],
        "vcenterConfigurationTimeStamp": NotRequired[str],
    },
)
VersionControlInfoTypeDef = TypedDict(
    "VersionControlInfoTypeDef",
    {
        "versionControlConfigurationTimeStamp": NotRequired[str],
        "versionControlType": NotRequired[VersionControlTypeType],
    },
)
DataCollectionDetailsTypeDef = TypedDict(
    "DataCollectionDetailsTypeDef",
    {
        "completionTime": NotRequired[datetime],
        "failed": NotRequired[int],
        "inProgress": NotRequired[int],
        "servers": NotRequired[int],
        "startTime": NotRequired[datetime],
        "status": NotRequired[AssessmentStatusType],
        "statusMessage": NotRequired[str],
        "success": NotRequired[int],
    },
)
HeterogeneousOutputTypeDef = TypedDict(
    "HeterogeneousOutputTypeDef",
    {
        "targetDatabaseEngine": List[HeterogeneousTargetDatabaseEngineType],
    },
)
HomogeneousOutputTypeDef = TypedDict(
    "HomogeneousOutputTypeDef",
    {
        "targetDatabaseEngine": NotRequired[List[Literal["None specified"]]],
    },
)
NoDatabaseMigrationPreferenceOutputTypeDef = TypedDict(
    "NoDatabaseMigrationPreferenceOutputTypeDef",
    {
        "targetDatabaseEngine": List[TargetDatabaseEngineType],
    },
)
GetApplicationComponentDetailsRequestRequestTypeDef = TypedDict(
    "GetApplicationComponentDetailsRequestRequestTypeDef",
    {
        "applicationComponentId": str,
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
GetApplicationComponentStrategiesRequestRequestTypeDef = TypedDict(
    "GetApplicationComponentStrategiesRequestRequestTypeDef",
    {
        "applicationComponentId": str,
    },
)
GetAssessmentRequestRequestTypeDef = TypedDict(
    "GetAssessmentRequestRequestTypeDef",
    {
        "id": str,
    },
)
GetImportFileTaskRequestRequestTypeDef = TypedDict(
    "GetImportFileTaskRequestRequestTypeDef",
    {
        "id": str,
    },
)
GetRecommendationReportDetailsRequestRequestTypeDef = TypedDict(
    "GetRecommendationReportDetailsRequestRequestTypeDef",
    {
        "id": str,
    },
)
RecommendationReportDetailsTypeDef = TypedDict(
    "RecommendationReportDetailsTypeDef",
    {
        "completionTime": NotRequired[datetime],
        "s3Bucket": NotRequired[str],
        "s3Keys": NotRequired[List[str]],
        "startTime": NotRequired[datetime],
        "status": NotRequired[RecommendationReportStatusType],
        "statusMessage": NotRequired[str],
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
GetServerDetailsRequestRequestTypeDef = TypedDict(
    "GetServerDetailsRequestRequestTypeDef",
    {
        "serverId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
GetServerStrategiesRequestRequestTypeDef = TypedDict(
    "GetServerStrategiesRequestRequestTypeDef",
    {
        "serverId": str,
    },
)
GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "name": NotRequired[GroupNameType],
        "value": NotRequired[str],
    },
)
HeterogeneousTypeDef = TypedDict(
    "HeterogeneousTypeDef",
    {
        "targetDatabaseEngine": Sequence[HeterogeneousTargetDatabaseEngineType],
    },
)
HomogeneousTypeDef = TypedDict(
    "HomogeneousTypeDef",
    {
        "targetDatabaseEngine": NotRequired[Sequence[Literal["None specified"]]],
    },
)
ImportFileTaskInformationTypeDef = TypedDict(
    "ImportFileTaskInformationTypeDef",
    {
        "completionTime": NotRequired[datetime],
        "id": NotRequired[str],
        "importName": NotRequired[str],
        "inputS3Bucket": NotRequired[str],
        "inputS3Key": NotRequired[str],
        "numberOfRecordsFailed": NotRequired[int],
        "numberOfRecordsSuccess": NotRequired[int],
        "startTime": NotRequired[datetime],
        "status": NotRequired[ImportFileTaskStatusType],
        "statusReportS3Bucket": NotRequired[str],
        "statusReportS3Key": NotRequired[str],
    },
)
ListAnalyzableServersRequestRequestTypeDef = TypedDict(
    "ListAnalyzableServersRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sort": NotRequired[SortOrderType],
    },
)
ListCollectorsRequestRequestTypeDef = TypedDict(
    "ListCollectorsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListImportFileTaskRequestRequestTypeDef = TypedDict(
    "ListImportFileTaskRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
NoManagementPreferenceOutputTypeDef = TypedDict(
    "NoManagementPreferenceOutputTypeDef",
    {
        "targetDestination": List[NoPreferenceTargetDestinationType],
    },
)
SelfManageResourcesOutputTypeDef = TypedDict(
    "SelfManageResourcesOutputTypeDef",
    {
        "targetDestination": List[SelfManageTargetDestinationType],
    },
)
NetworkInfoTypeDef = TypedDict(
    "NetworkInfoTypeDef",
    {
        "interfaceName": str,
        "ipAddress": str,
        "macAddress": str,
        "netMask": str,
    },
)
NoDatabaseMigrationPreferenceTypeDef = TypedDict(
    "NoDatabaseMigrationPreferenceTypeDef",
    {
        "targetDatabaseEngine": Sequence[TargetDatabaseEngineType],
    },
)
NoManagementPreferenceTypeDef = TypedDict(
    "NoManagementPreferenceTypeDef",
    {
        "targetDestination": Sequence[NoPreferenceTargetDestinationType],
    },
)
OSInfoTypeDef = TypedDict(
    "OSInfoTypeDef",
    {
        "type": NotRequired[OSTypeType],
        "version": NotRequired[str],
    },
)
TransformationToolTypeDef = TypedDict(
    "TransformationToolTypeDef",
    {
        "description": NotRequired[str],
        "name": NotRequired[TransformationToolNameType],
        "tranformationToolInstallationLink": NotRequired[str],
    },
)
SelfManageResourcesTypeDef = TypedDict(
    "SelfManageResourcesTypeDef",
    {
        "targetDestination": Sequence[SelfManageTargetDestinationType],
    },
)
ServerErrorTypeDef = TypedDict(
    "ServerErrorTypeDef",
    {
        "serverErrorCategory": NotRequired[ServerErrorCategoryType],
    },
)
SourceCodeTypeDef = TypedDict(
    "SourceCodeTypeDef",
    {
        "location": NotRequired[str],
        "projectName": NotRequired[str],
        "sourceVersion": NotRequired[str],
        "versionControl": NotRequired[VersionControlType],
    },
)
StopAssessmentRequestRequestTypeDef = TypedDict(
    "StopAssessmentRequestRequestTypeDef",
    {
        "assessmentId": str,
    },
)
StrategyOptionTypeDef = TypedDict(
    "StrategyOptionTypeDef",
    {
        "isPreferred": NotRequired[bool],
        "strategy": NotRequired[StrategyType],
        "targetDestination": NotRequired[TargetDestinationType],
        "toolName": NotRequired[TransformationToolNameType],
    },
)
AntipatternReportResultTypeDef = TypedDict(
    "AntipatternReportResultTypeDef",
    {
        "analyzerName": NotRequired[AnalyzerNameUnionTypeDef],
        "antiPatternReportS3Object": NotRequired[S3ObjectTypeDef],
        "antipatternReportStatus": NotRequired[AntipatternReportStatusType],
        "antipatternReportStatusMessage": NotRequired[str],
    },
)
AssessmentSummaryTypeDef = TypedDict(
    "AssessmentSummaryTypeDef",
    {
        "antipatternReportS3Object": NotRequired[S3ObjectTypeDef],
        "antipatternReportStatus": NotRequired[AntipatternReportStatusType],
        "antipatternReportStatusMessage": NotRequired[str],
        "lastAnalyzedTimestamp": NotRequired[datetime],
        "listAntipatternSeveritySummary": NotRequired[List[AntipatternSeveritySummaryTypeDef]],
        "listApplicationComponentStatusSummary": NotRequired[
            List[ApplicationComponentStatusSummaryTypeDef]
        ],
        "listApplicationComponentStrategySummary": NotRequired[List[StrategySummaryTypeDef]],
        "listApplicationComponentSummary": NotRequired[List[ApplicationComponentSummaryTypeDef]],
        "listServerStatusSummary": NotRequired[List[ServerStatusSummaryTypeDef]],
        "listServerStrategySummary": NotRequired[List[StrategySummaryTypeDef]],
        "listServerSummary": NotRequired[List[ServerSummaryTypeDef]],
    },
)
AssessmentTargetUnionTypeDef = Union[AssessmentTargetTypeDef, AssessmentTargetOutputTypeDef]
AwsManagedResourcesUnionTypeDef = Union[
    AwsManagedResourcesTypeDef, AwsManagedResourcesOutputTypeDef
]
PrioritizeBusinessGoalsTypeDef = TypedDict(
    "PrioritizeBusinessGoalsTypeDef",
    {
        "businessGoals": NotRequired[BusinessGoalsTypeDef],
    },
)
ConfigurationSummaryTypeDef = TypedDict(
    "ConfigurationSummaryTypeDef",
    {
        "ipAddressBasedRemoteInfoList": NotRequired[List[IPAddressBasedRemoteInfoTypeDef]],
        "pipelineInfoList": NotRequired[List[PipelineInfoTypeDef]],
        "remoteSourceCodeAnalysisServerInfo": NotRequired[
            RemoteSourceCodeAnalysisServerInfoTypeDef
        ],
        "vcenterBasedRemoteInfoList": NotRequired[List[VcenterBasedRemoteInfoTypeDef]],
        "versionControlInfoList": NotRequired[List[VersionControlInfoTypeDef]],
    },
)
DatabaseMigrationPreferenceOutputTypeDef = TypedDict(
    "DatabaseMigrationPreferenceOutputTypeDef",
    {
        "heterogeneous": NotRequired[HeterogeneousOutputTypeDef],
        "homogeneous": NotRequired[HomogeneousOutputTypeDef],
        "noPreference": NotRequired[NoDatabaseMigrationPreferenceOutputTypeDef],
    },
)
GetAssessmentResponseTypeDef = TypedDict(
    "GetAssessmentResponseTypeDef",
    {
        "assessmentTargets": List[AssessmentTargetOutputTypeDef],
        "dataCollectionDetails": DataCollectionDetailsTypeDef,
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetImportFileTaskResponseTypeDef = TypedDict(
    "GetImportFileTaskResponseTypeDef",
    {
        "completionTime": datetime,
        "id": str,
        "importName": str,
        "inputS3Bucket": str,
        "inputS3Key": str,
        "numberOfRecordsFailed": int,
        "numberOfRecordsSuccess": int,
        "startTime": datetime,
        "status": ImportFileTaskStatusType,
        "statusReportS3Bucket": str,
        "statusReportS3Key": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLatestAssessmentIdResponseTypeDef = TypedDict(
    "GetLatestAssessmentIdResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAnalyzableServersResponseTypeDef = TypedDict(
    "ListAnalyzableServersResponseTypeDef",
    {
        "analyzableServers": List[AnalyzableServerSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartAssessmentResponseTypeDef = TypedDict(
    "StartAssessmentResponseTypeDef",
    {
        "assessmentId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartImportFileTaskResponseTypeDef = TypedDict(
    "StartImportFileTaskResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartRecommendationReportGenerationResponseTypeDef = TypedDict(
    "StartRecommendationReportGenerationResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRecommendationReportDetailsResponseTypeDef = TypedDict(
    "GetRecommendationReportDetailsResponseTypeDef",
    {
        "id": str,
        "recommendationReportDetails": RecommendationReportDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServerDetailsRequestGetServerDetailsPaginateTypeDef = TypedDict(
    "GetServerDetailsRequestGetServerDetailsPaginateTypeDef",
    {
        "serverId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAnalyzableServersRequestListAnalyzableServersPaginateTypeDef = TypedDict(
    "ListAnalyzableServersRequestListAnalyzableServersPaginateTypeDef",
    {
        "sort": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCollectorsRequestListCollectorsPaginateTypeDef = TypedDict(
    "ListCollectorsRequestListCollectorsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListImportFileTaskRequestListImportFileTaskPaginateTypeDef = TypedDict(
    "ListImportFileTaskRequestListImportFileTaskPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListApplicationComponentsRequestListApplicationComponentsPaginateTypeDef = TypedDict(
    "ListApplicationComponentsRequestListApplicationComponentsPaginateTypeDef",
    {
        "applicationComponentCriteria": NotRequired[ApplicationComponentCriteriaType],
        "filterValue": NotRequired[str],
        "groupIdFilter": NotRequired[Sequence[GroupTypeDef]],
        "sort": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListApplicationComponentsRequestRequestTypeDef = TypedDict(
    "ListApplicationComponentsRequestRequestTypeDef",
    {
        "applicationComponentCriteria": NotRequired[ApplicationComponentCriteriaType],
        "filterValue": NotRequired[str],
        "groupIdFilter": NotRequired[Sequence[GroupTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sort": NotRequired[SortOrderType],
    },
)
ListServersRequestListServersPaginateTypeDef = TypedDict(
    "ListServersRequestListServersPaginateTypeDef",
    {
        "filterValue": NotRequired[str],
        "groupIdFilter": NotRequired[Sequence[GroupTypeDef]],
        "serverCriteria": NotRequired[ServerCriteriaType],
        "sort": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListServersRequestRequestTypeDef = TypedDict(
    "ListServersRequestRequestTypeDef",
    {
        "filterValue": NotRequired[str],
        "groupIdFilter": NotRequired[Sequence[GroupTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "serverCriteria": NotRequired[ServerCriteriaType],
        "sort": NotRequired[SortOrderType],
    },
)
StartImportFileTaskRequestRequestTypeDef = TypedDict(
    "StartImportFileTaskRequestRequestTypeDef",
    {
        "S3Bucket": str,
        "name": str,
        "s3key": str,
        "dataSourceType": NotRequired[DataSourceTypeType],
        "groupId": NotRequired[Sequence[GroupTypeDef]],
        "s3bucketForReportData": NotRequired[str],
    },
)
StartRecommendationReportGenerationRequestRequestTypeDef = TypedDict(
    "StartRecommendationReportGenerationRequestRequestTypeDef",
    {
        "groupIdFilter": NotRequired[Sequence[GroupTypeDef]],
        "outputFormat": NotRequired[OutputFormatType],
    },
)
HeterogeneousUnionTypeDef = Union[HeterogeneousTypeDef, HeterogeneousOutputTypeDef]
HomogeneousUnionTypeDef = Union[HomogeneousTypeDef, HomogeneousOutputTypeDef]
ListImportFileTaskResponseTypeDef = TypedDict(
    "ListImportFileTaskResponseTypeDef",
    {
        "nextToken": str,
        "taskInfos": List[ImportFileTaskInformationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ManagementPreferenceOutputTypeDef = TypedDict(
    "ManagementPreferenceOutputTypeDef",
    {
        "awsManagedResources": NotRequired[AwsManagedResourcesOutputTypeDef],
        "noPreference": NotRequired[NoManagementPreferenceOutputTypeDef],
        "selfManageResources": NotRequired[SelfManageResourcesOutputTypeDef],
    },
)
NoDatabaseMigrationPreferenceUnionTypeDef = Union[
    NoDatabaseMigrationPreferenceTypeDef, NoDatabaseMigrationPreferenceOutputTypeDef
]
NoManagementPreferenceUnionTypeDef = Union[
    NoManagementPreferenceTypeDef, NoManagementPreferenceOutputTypeDef
]
SystemInfoTypeDef = TypedDict(
    "SystemInfoTypeDef",
    {
        "cpuArchitecture": NotRequired[str],
        "fileSystemType": NotRequired[str],
        "networkInfoList": NotRequired[List[NetworkInfoTypeDef]],
        "osInfo": NotRequired[OSInfoTypeDef],
    },
)
RecommendationSetTypeDef = TypedDict(
    "RecommendationSetTypeDef",
    {
        "strategy": NotRequired[StrategyType],
        "targetDestination": NotRequired[TargetDestinationType],
        "transformationTool": NotRequired[TransformationToolTypeDef],
    },
)
SelfManageResourcesUnionTypeDef = Union[
    SelfManageResourcesTypeDef, SelfManageResourcesOutputTypeDef
]
UpdateApplicationComponentConfigRequestRequestTypeDef = TypedDict(
    "UpdateApplicationComponentConfigRequestRequestTypeDef",
    {
        "applicationComponentId": str,
        "appType": NotRequired[AppTypeType],
        "configureOnly": NotRequired[bool],
        "inclusionStatus": NotRequired[InclusionStatusType],
        "secretsManagerKey": NotRequired[str],
        "sourceCodeList": NotRequired[Sequence[SourceCodeTypeDef]],
        "strategyOption": NotRequired[StrategyOptionTypeDef],
    },
)
UpdateServerConfigRequestRequestTypeDef = TypedDict(
    "UpdateServerConfigRequestRequestTypeDef",
    {
        "serverId": str,
        "strategyOption": NotRequired[StrategyOptionTypeDef],
    },
)
ResultTypeDef = TypedDict(
    "ResultTypeDef",
    {
        "analysisStatus": NotRequired[AnalysisStatusUnionTypeDef],
        "analysisType": NotRequired[AnalysisTypeType],
        "antipatternReportResultList": NotRequired[List[AntipatternReportResultTypeDef]],
        "statusMessage": NotRequired[str],
    },
)
GetPortfolioSummaryResponseTypeDef = TypedDict(
    "GetPortfolioSummaryResponseTypeDef",
    {
        "assessmentSummary": AssessmentSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartAssessmentRequestRequestTypeDef = TypedDict(
    "StartAssessmentRequestRequestTypeDef",
    {
        "assessmentDataSourceType": NotRequired[AssessmentDataSourceTypeType],
        "assessmentTargets": NotRequired[Sequence[AssessmentTargetUnionTypeDef]],
        "s3bucketForAnalysisData": NotRequired[str],
        "s3bucketForReportData": NotRequired[str],
    },
)
CollectorTypeDef = TypedDict(
    "CollectorTypeDef",
    {
        "collectorHealth": NotRequired[CollectorHealthType],
        "collectorId": NotRequired[str],
        "collectorVersion": NotRequired[str],
        "configurationSummary": NotRequired[ConfigurationSummaryTypeDef],
        "hostName": NotRequired[str],
        "ipAddress": NotRequired[str],
        "lastActivityTimeStamp": NotRequired[str],
        "registeredTimeStamp": NotRequired[str],
    },
)
DatabasePreferencesOutputTypeDef = TypedDict(
    "DatabasePreferencesOutputTypeDef",
    {
        "databaseManagementPreference": NotRequired[DatabaseManagementPreferenceType],
        "databaseMigrationPreference": NotRequired[DatabaseMigrationPreferenceOutputTypeDef],
    },
)
ApplicationPreferencesOutputTypeDef = TypedDict(
    "ApplicationPreferencesOutputTypeDef",
    {
        "managementPreference": NotRequired[ManagementPreferenceOutputTypeDef],
    },
)
DatabaseMigrationPreferenceTypeDef = TypedDict(
    "DatabaseMigrationPreferenceTypeDef",
    {
        "heterogeneous": NotRequired[HeterogeneousUnionTypeDef],
        "homogeneous": NotRequired[HomogeneousUnionTypeDef],
        "noPreference": NotRequired[NoDatabaseMigrationPreferenceUnionTypeDef],
    },
)
ApplicationComponentStrategyTypeDef = TypedDict(
    "ApplicationComponentStrategyTypeDef",
    {
        "isPreferred": NotRequired[bool],
        "recommendation": NotRequired[RecommendationSetTypeDef],
        "status": NotRequired[StrategyRecommendationType],
    },
)
ServerDetailTypeDef = TypedDict(
    "ServerDetailTypeDef",
    {
        "antipatternReportS3Object": NotRequired[S3ObjectTypeDef],
        "antipatternReportStatus": NotRequired[AntipatternReportStatusType],
        "antipatternReportStatusMessage": NotRequired[str],
        "applicationComponentStrategySummary": NotRequired[List[StrategySummaryTypeDef]],
        "dataCollectionStatus": NotRequired[RunTimeAssessmentStatusType],
        "id": NotRequired[str],
        "lastAnalyzedTimestamp": NotRequired[datetime],
        "listAntipatternSeveritySummary": NotRequired[List[AntipatternSeveritySummaryTypeDef]],
        "name": NotRequired[str],
        "recommendationSet": NotRequired[RecommendationSetTypeDef],
        "serverError": NotRequired[ServerErrorTypeDef],
        "serverType": NotRequired[str],
        "statusMessage": NotRequired[str],
        "systemInfo": NotRequired[SystemInfoTypeDef],
    },
)
ServerStrategyTypeDef = TypedDict(
    "ServerStrategyTypeDef",
    {
        "isPreferred": NotRequired[bool],
        "numberOfApplicationComponents": NotRequired[int],
        "recommendation": NotRequired[RecommendationSetTypeDef],
        "status": NotRequired[StrategyRecommendationType],
    },
)
ManagementPreferenceTypeDef = TypedDict(
    "ManagementPreferenceTypeDef",
    {
        "awsManagedResources": NotRequired[AwsManagedResourcesUnionTypeDef],
        "noPreference": NotRequired[NoManagementPreferenceUnionTypeDef],
        "selfManageResources": NotRequired[SelfManageResourcesUnionTypeDef],
    },
)
ApplicationComponentDetailTypeDef = TypedDict(
    "ApplicationComponentDetailTypeDef",
    {
        "analysisStatus": NotRequired[SrcCodeOrDbAnalysisStatusType],
        "antipatternReportS3Object": NotRequired[S3ObjectTypeDef],
        "antipatternReportStatus": NotRequired[AntipatternReportStatusType],
        "antipatternReportStatusMessage": NotRequired[str],
        "appType": NotRequired[AppTypeType],
        "appUnitError": NotRequired[AppUnitErrorTypeDef],
        "associatedServerId": NotRequired[str],
        "databaseConfigDetail": NotRequired[DatabaseConfigDetailTypeDef],
        "id": NotRequired[str],
        "inclusionStatus": NotRequired[InclusionStatusType],
        "lastAnalyzedTimestamp": NotRequired[datetime],
        "listAntipatternSeveritySummary": NotRequired[List[AntipatternSeveritySummaryTypeDef]],
        "moreServerAssociationExists": NotRequired[bool],
        "name": NotRequired[str],
        "osDriver": NotRequired[str],
        "osVersion": NotRequired[str],
        "recommendationSet": NotRequired[RecommendationSetTypeDef],
        "resourceSubType": NotRequired[ResourceSubTypeType],
        "resultList": NotRequired[List[ResultTypeDef]],
        "runtimeStatus": NotRequired[RuntimeAnalysisStatusType],
        "runtimeStatusMessage": NotRequired[str],
        "sourceCodeRepositories": NotRequired[List[SourceCodeRepositoryTypeDef]],
        "statusMessage": NotRequired[str],
    },
)
ListCollectorsResponseTypeDef = TypedDict(
    "ListCollectorsResponseTypeDef",
    {
        "Collectors": List[CollectorTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPortfolioPreferencesResponseTypeDef = TypedDict(
    "GetPortfolioPreferencesResponseTypeDef",
    {
        "applicationMode": ApplicationModeType,
        "applicationPreferences": ApplicationPreferencesOutputTypeDef,
        "databasePreferences": DatabasePreferencesOutputTypeDef,
        "prioritizeBusinessGoals": PrioritizeBusinessGoalsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DatabaseMigrationPreferenceUnionTypeDef = Union[
    DatabaseMigrationPreferenceTypeDef, DatabaseMigrationPreferenceOutputTypeDef
]
GetApplicationComponentStrategiesResponseTypeDef = TypedDict(
    "GetApplicationComponentStrategiesResponseTypeDef",
    {
        "applicationComponentStrategies": List[ApplicationComponentStrategyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServerDetailsResponseTypeDef = TypedDict(
    "GetServerDetailsResponseTypeDef",
    {
        "associatedApplications": List[AssociatedApplicationTypeDef],
        "nextToken": str,
        "serverDetail": ServerDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListServersResponseTypeDef = TypedDict(
    "ListServersResponseTypeDef",
    {
        "nextToken": str,
        "serverInfos": List[ServerDetailTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServerStrategiesResponseTypeDef = TypedDict(
    "GetServerStrategiesResponseTypeDef",
    {
        "serverStrategies": List[ServerStrategyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ManagementPreferenceUnionTypeDef = Union[
    ManagementPreferenceTypeDef, ManagementPreferenceOutputTypeDef
]
GetApplicationComponentDetailsResponseTypeDef = TypedDict(
    "GetApplicationComponentDetailsResponseTypeDef",
    {
        "applicationComponentDetail": ApplicationComponentDetailTypeDef,
        "associatedApplications": List[AssociatedApplicationTypeDef],
        "associatedServerIds": List[str],
        "moreApplicationResource": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListApplicationComponentsResponseTypeDef = TypedDict(
    "ListApplicationComponentsResponseTypeDef",
    {
        "applicationComponentInfos": List[ApplicationComponentDetailTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DatabasePreferencesTypeDef = TypedDict(
    "DatabasePreferencesTypeDef",
    {
        "databaseManagementPreference": NotRequired[DatabaseManagementPreferenceType],
        "databaseMigrationPreference": NotRequired[DatabaseMigrationPreferenceUnionTypeDef],
    },
)
ApplicationPreferencesTypeDef = TypedDict(
    "ApplicationPreferencesTypeDef",
    {
        "managementPreference": NotRequired[ManagementPreferenceUnionTypeDef],
    },
)
PutPortfolioPreferencesRequestRequestTypeDef = TypedDict(
    "PutPortfolioPreferencesRequestRequestTypeDef",
    {
        "applicationMode": NotRequired[ApplicationModeType],
        "applicationPreferences": NotRequired[ApplicationPreferencesTypeDef],
        "databasePreferences": NotRequired[DatabasePreferencesTypeDef],
        "prioritizeBusinessGoals": NotRequired[PrioritizeBusinessGoalsTypeDef],
    },
)
