"""
Type annotations for apptest service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apptest/type_defs/)

Usage::

    ```python
    from mypy_boto3_apptest.type_defs import BatchOutputTypeDef

    data: BatchOutputTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    CaptureToolType,
    CloudFormationActionTypeType,
    ComparisonStatusEnumType,
    FormatType,
    M2ManagedActionTypeType,
    M2NonManagedActionTypeType,
    StepRunStatusType,
    TestCaseLifecycleType,
    TestCaseRunStatusType,
    TestConfigurationLifecycleType,
    TestRunStatusType,
    TestSuiteLifecycleType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "BatchOutputTypeDef",
    "MainframeActionPropertiesTypeDef",
    "DataSetTypeDef",
    "BatchTypeDef",
    "CloudFormationActionTypeDef",
    "CloudFormationOutputTypeDef",
    "CloudFormationTypeDef",
    "CompareDataSetsStepOutputTypeDef",
    "SourceDatabaseMetadataTypeDef",
    "TargetDatabaseMetadataTypeDef",
    "CompareDatabaseCDCStepOutputTypeDef",
    "CreateCloudFormationStepInputTypeDef",
    "CreateCloudFormationStepOutputTypeDef",
    "ResponseMetadataTypeDef",
    "ServiceSettingsTypeDef",
    "TestCasesTypeDef",
    "DeleteCloudFormationStepInputTypeDef",
    "DeleteTestCaseRequestRequestTypeDef",
    "DeleteTestConfigurationRequestRequestTypeDef",
    "DeleteTestRunRequestRequestTypeDef",
    "DeleteTestSuiteRequestRequestTypeDef",
    "GetTestCaseRequestRequestTypeDef",
    "TestCaseLatestVersionTypeDef",
    "GetTestConfigurationRequestRequestTypeDef",
    "TestConfigurationLatestVersionTypeDef",
    "GetTestRunStepRequestRequestTypeDef",
    "GetTestSuiteRequestRequestTypeDef",
    "TestCasesOutputTypeDef",
    "TestSuiteLatestVersionTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListTestCasesRequestRequestTypeDef",
    "TestCaseSummaryTypeDef",
    "ListTestConfigurationsRequestRequestTypeDef",
    "TestConfigurationSummaryTypeDef",
    "ListTestRunStepsRequestRequestTypeDef",
    "TestRunStepSummaryTypeDef",
    "ListTestRunTestCasesRequestRequestTypeDef",
    "TestCaseRunSummaryTypeDef",
    "ListTestRunsRequestRequestTypeDef",
    "TestRunSummaryTypeDef",
    "ListTestSuitesRequestRequestTypeDef",
    "TestSuiteSummaryTypeDef",
    "M2ManagedActionPropertiesTypeDef",
    "M2ManagedApplicationStepOutputTypeDef",
    "M2ManagedApplicationSummaryTypeDef",
    "M2ManagedApplicationTypeDef",
    "M2NonManagedApplicationActionTypeDef",
    "M2NonManagedApplicationStepInputTypeDef",
    "M2NonManagedApplicationSummaryTypeDef",
    "M2NonManagedApplicationTypeDef",
    "OutputFileTypeDef",
    "ScriptSummaryTypeDef",
    "ScriptTypeDef",
    "StartTestRunRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "BatchStepOutputTypeDef",
    "CompareDataSetsStepInputTypeDef",
    "TN3270StepOutputTypeDef",
    "BatchUnionTypeDef",
    "CloudFormationUnionTypeDef",
    "CompareDatabaseCDCStepInputTypeDef",
    "DatabaseCDCTypeDef",
    "CreateCloudFormationSummaryTypeDef",
    "CreateTestCaseResponseTypeDef",
    "CreateTestConfigurationResponseTypeDef",
    "CreateTestSuiteResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartTestRunResponseTypeDef",
    "UpdateTestCaseResponseTypeDef",
    "UpdateTestConfigurationResponseTypeDef",
    "UpdateTestSuiteResponseTypeDef",
    "DeleteCloudFormationSummaryTypeDef",
    "ListTestCasesRequestListTestCasesPaginateTypeDef",
    "ListTestConfigurationsRequestListTestConfigurationsPaginateTypeDef",
    "ListTestRunStepsRequestListTestRunStepsPaginateTypeDef",
    "ListTestRunTestCasesRequestListTestRunTestCasesPaginateTypeDef",
    "ListTestRunsRequestListTestRunsPaginateTypeDef",
    "ListTestSuitesRequestListTestSuitesPaginateTypeDef",
    "ListTestCasesResponseTypeDef",
    "ListTestConfigurationsResponseTypeDef",
    "ListTestRunStepsResponseTypeDef",
    "ListTestRunTestCasesResponseTypeDef",
    "ListTestRunsResponseTypeDef",
    "ListTestSuitesResponseTypeDef",
    "M2ManagedApplicationActionTypeDef",
    "M2ManagedApplicationStepInputTypeDef",
    "M2NonManagedApplicationStepSummaryTypeDef",
    "MainframeResourceSummaryTypeDef",
    "ResourceTypeOutputTypeDef",
    "OutputTypeDef",
    "TN3270OutputTypeDef",
    "TN3270TypeDef",
    "CompareDataSetsSummaryTypeDef",
    "ResourceTypeTypeDef",
    "CompareDatabaseCDCSummaryTypeDef",
    "FileMetadataOutputTypeDef",
    "FileMetadataTypeDef",
    "CloudFormationStepSummaryTypeDef",
    "ResourceActionTypeDef",
    "M2ManagedApplicationStepSummaryTypeDef",
    "BatchStepInputTypeDef",
    "TN3270StepInputTypeDef",
    "ResourceOutputTypeDef",
    "MainframeActionTypeOutputTypeDef",
    "TN3270UnionTypeDef",
    "ResourceTypeUnionTypeDef",
    "CompareFileTypeTypeDef",
    "InputFileOutputTypeDef",
    "FileMetadataUnionTypeDef",
    "ResourceActionSummaryTypeDef",
    "BatchSummaryTypeDef",
    "TN3270SummaryTypeDef",
    "GetTestConfigurationResponseTypeDef",
    "MainframeActionOutputTypeDef",
    "MainframeActionTypeTypeDef",
    "ResourceTypeDef",
    "FileTypeDef",
    "InputOutputTypeDef",
    "InputFileTypeDef",
    "MainframeActionSummaryTypeDef",
    "MainframeActionTypeUnionTypeDef",
    "ResourceUnionTypeDef",
    "UpdateTestConfigurationRequestRequestTypeDef",
    "CompareActionSummaryTypeDef",
    "CompareActionOutputTypeDef",
    "InputFileUnionTypeDef",
    "MainframeActionTypeDef",
    "CreateTestConfigurationRequestRequestTypeDef",
    "StepRunSummaryTypeDef",
    "StepActionOutputTypeDef",
    "InputTypeDef",
    "MainframeActionUnionTypeDef",
    "GetTestRunStepResponseTypeDef",
    "StepOutputTypeDef",
    "InputUnionTypeDef",
    "GetTestCaseResponseTypeDef",
    "GetTestSuiteResponseTypeDef",
    "CompareActionTypeDef",
    "CompareActionUnionTypeDef",
    "StepActionTypeDef",
    "StepActionUnionTypeDef",
    "StepTypeDef",
    "CreateTestSuiteRequestRequestTypeDef",
    "StepUnionTypeDef",
    "UpdateTestCaseRequestRequestTypeDef",
    "UpdateTestSuiteRequestRequestTypeDef",
    "CreateTestCaseRequestRequestTypeDef",
)

BatchOutputTypeDef = TypedDict(
    "BatchOutputTypeDef",
    {
        "batchJobName": str,
        "batchJobParameters": NotRequired[Dict[str, str]],
        "exportDataSetNames": NotRequired[List[str]],
    },
)
MainframeActionPropertiesTypeDef = TypedDict(
    "MainframeActionPropertiesTypeDef",
    {
        "dmsTaskArn": NotRequired[str],
    },
)
DataSetTypeDef = TypedDict(
    "DataSetTypeDef",
    {
        "type": Literal["PS"],
        "name": str,
        "ccsid": str,
        "format": FormatType,
        "length": int,
    },
)
BatchTypeDef = TypedDict(
    "BatchTypeDef",
    {
        "batchJobName": str,
        "batchJobParameters": NotRequired[Mapping[str, str]],
        "exportDataSetNames": NotRequired[Sequence[str]],
    },
)
CloudFormationActionTypeDef = TypedDict(
    "CloudFormationActionTypeDef",
    {
        "resource": str,
        "actionType": NotRequired[CloudFormationActionTypeType],
    },
)
CloudFormationOutputTypeDef = TypedDict(
    "CloudFormationOutputTypeDef",
    {
        "templateLocation": str,
        "parameters": NotRequired[Dict[str, str]],
    },
)
CloudFormationTypeDef = TypedDict(
    "CloudFormationTypeDef",
    {
        "templateLocation": str,
        "parameters": NotRequired[Mapping[str, str]],
    },
)
CompareDataSetsStepOutputTypeDef = TypedDict(
    "CompareDataSetsStepOutputTypeDef",
    {
        "comparisonOutputLocation": str,
        "comparisonStatus": ComparisonStatusEnumType,
    },
)
SourceDatabaseMetadataTypeDef = TypedDict(
    "SourceDatabaseMetadataTypeDef",
    {
        "type": Literal["z/OS-DB2"],
        "captureTool": CaptureToolType,
    },
)
TargetDatabaseMetadataTypeDef = TypedDict(
    "TargetDatabaseMetadataTypeDef",
    {
        "type": Literal["PostgreSQL"],
        "captureTool": CaptureToolType,
    },
)
CompareDatabaseCDCStepOutputTypeDef = TypedDict(
    "CompareDatabaseCDCStepOutputTypeDef",
    {
        "comparisonOutputLocation": str,
        "comparisonStatus": ComparisonStatusEnumType,
    },
)
CreateCloudFormationStepInputTypeDef = TypedDict(
    "CreateCloudFormationStepInputTypeDef",
    {
        "templateLocation": str,
        "parameters": NotRequired[Dict[str, str]],
    },
)
CreateCloudFormationStepOutputTypeDef = TypedDict(
    "CreateCloudFormationStepOutputTypeDef",
    {
        "stackId": str,
        "exports": NotRequired[Dict[str, str]],
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
ServiceSettingsTypeDef = TypedDict(
    "ServiceSettingsTypeDef",
    {
        "kmsKeyId": NotRequired[str],
    },
)
TestCasesTypeDef = TypedDict(
    "TestCasesTypeDef",
    {
        "sequential": NotRequired[Sequence[str]],
    },
)
DeleteCloudFormationStepInputTypeDef = TypedDict(
    "DeleteCloudFormationStepInputTypeDef",
    {
        "stackId": str,
    },
)
DeleteTestCaseRequestRequestTypeDef = TypedDict(
    "DeleteTestCaseRequestRequestTypeDef",
    {
        "testCaseId": str,
    },
)
DeleteTestConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteTestConfigurationRequestRequestTypeDef",
    {
        "testConfigurationId": str,
    },
)
DeleteTestRunRequestRequestTypeDef = TypedDict(
    "DeleteTestRunRequestRequestTypeDef",
    {
        "testRunId": str,
    },
)
DeleteTestSuiteRequestRequestTypeDef = TypedDict(
    "DeleteTestSuiteRequestRequestTypeDef",
    {
        "testSuiteId": str,
    },
)
GetTestCaseRequestRequestTypeDef = TypedDict(
    "GetTestCaseRequestRequestTypeDef",
    {
        "testCaseId": str,
        "testCaseVersion": NotRequired[int],
    },
)
TestCaseLatestVersionTypeDef = TypedDict(
    "TestCaseLatestVersionTypeDef",
    {
        "version": int,
        "status": TestCaseLifecycleType,
        "statusReason": NotRequired[str],
    },
)
GetTestConfigurationRequestRequestTypeDef = TypedDict(
    "GetTestConfigurationRequestRequestTypeDef",
    {
        "testConfigurationId": str,
        "testConfigurationVersion": NotRequired[int],
    },
)
TestConfigurationLatestVersionTypeDef = TypedDict(
    "TestConfigurationLatestVersionTypeDef",
    {
        "version": int,
        "status": TestConfigurationLifecycleType,
        "statusReason": NotRequired[str],
    },
)
GetTestRunStepRequestRequestTypeDef = TypedDict(
    "GetTestRunStepRequestRequestTypeDef",
    {
        "testRunId": str,
        "stepName": str,
        "testCaseId": NotRequired[str],
        "testSuiteId": NotRequired[str],
    },
)
GetTestSuiteRequestRequestTypeDef = TypedDict(
    "GetTestSuiteRequestRequestTypeDef",
    {
        "testSuiteId": str,
        "testSuiteVersion": NotRequired[int],
    },
)
TestCasesOutputTypeDef = TypedDict(
    "TestCasesOutputTypeDef",
    {
        "sequential": NotRequired[List[str]],
    },
)
TestSuiteLatestVersionTypeDef = TypedDict(
    "TestSuiteLatestVersionTypeDef",
    {
        "version": int,
        "status": TestSuiteLifecycleType,
        "statusReason": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
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
ListTestCasesRequestRequestTypeDef = TypedDict(
    "ListTestCasesRequestRequestTypeDef",
    {
        "testCaseIds": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
TestCaseSummaryTypeDef = TypedDict(
    "TestCaseSummaryTypeDef",
    {
        "testCaseId": str,
        "testCaseArn": str,
        "name": str,
        "latestVersion": int,
        "status": TestCaseLifecycleType,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "statusReason": NotRequired[str],
    },
)
ListTestConfigurationsRequestRequestTypeDef = TypedDict(
    "ListTestConfigurationsRequestRequestTypeDef",
    {
        "testConfigurationIds": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
TestConfigurationSummaryTypeDef = TypedDict(
    "TestConfigurationSummaryTypeDef",
    {
        "testConfigurationId": str,
        "name": str,
        "latestVersion": int,
        "testConfigurationArn": str,
        "status": TestConfigurationLifecycleType,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "statusReason": NotRequired[str],
    },
)
ListTestRunStepsRequestRequestTypeDef = TypedDict(
    "ListTestRunStepsRequestRequestTypeDef",
    {
        "testRunId": str,
        "testCaseId": NotRequired[str],
        "testSuiteId": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
TestRunStepSummaryTypeDef = TypedDict(
    "TestRunStepSummaryTypeDef",
    {
        "stepName": str,
        "testRunId": str,
        "status": StepRunStatusType,
        "runStartTime": datetime,
        "testCaseId": NotRequired[str],
        "testCaseVersion": NotRequired[int],
        "testSuiteId": NotRequired[str],
        "testSuiteVersion": NotRequired[int],
        "beforeStep": NotRequired[bool],
        "afterStep": NotRequired[bool],
        "statusReason": NotRequired[str],
        "runEndTime": NotRequired[datetime],
    },
)
ListTestRunTestCasesRequestRequestTypeDef = TypedDict(
    "ListTestRunTestCasesRequestRequestTypeDef",
    {
        "testRunId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
TestCaseRunSummaryTypeDef = TypedDict(
    "TestCaseRunSummaryTypeDef",
    {
        "testCaseId": str,
        "testCaseVersion": int,
        "testRunId": str,
        "status": TestCaseRunStatusType,
        "runStartTime": datetime,
        "statusReason": NotRequired[str],
        "runEndTime": NotRequired[datetime],
    },
)
ListTestRunsRequestRequestTypeDef = TypedDict(
    "ListTestRunsRequestRequestTypeDef",
    {
        "testSuiteId": NotRequired[str],
        "testRunIds": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
TestRunSummaryTypeDef = TypedDict(
    "TestRunSummaryTypeDef",
    {
        "testRunId": str,
        "testRunArn": str,
        "testSuiteId": str,
        "testSuiteVersion": int,
        "status": TestRunStatusType,
        "runStartTime": datetime,
        "testConfigurationId": NotRequired[str],
        "testConfigurationVersion": NotRequired[int],
        "statusReason": NotRequired[str],
        "runEndTime": NotRequired[datetime],
    },
)
ListTestSuitesRequestRequestTypeDef = TypedDict(
    "ListTestSuitesRequestRequestTypeDef",
    {
        "testSuiteIds": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
TestSuiteSummaryTypeDef = TypedDict(
    "TestSuiteSummaryTypeDef",
    {
        "testSuiteId": str,
        "name": str,
        "latestVersion": int,
        "testSuiteArn": str,
        "status": TestSuiteLifecycleType,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "statusReason": NotRequired[str],
    },
)
M2ManagedActionPropertiesTypeDef = TypedDict(
    "M2ManagedActionPropertiesTypeDef",
    {
        "forceStop": NotRequired[bool],
        "importDataSetLocation": NotRequired[str],
    },
)
M2ManagedApplicationStepOutputTypeDef = TypedDict(
    "M2ManagedApplicationStepOutputTypeDef",
    {
        "importDataSetSummary": NotRequired[Dict[str, str]],
    },
)
M2ManagedApplicationSummaryTypeDef = TypedDict(
    "M2ManagedApplicationSummaryTypeDef",
    {
        "applicationId": str,
        "runtime": Literal["MicroFocus"],
        "listenerPort": NotRequired[int],
    },
)
M2ManagedApplicationTypeDef = TypedDict(
    "M2ManagedApplicationTypeDef",
    {
        "applicationId": str,
        "runtime": Literal["MicroFocus"],
        "vpcEndpointServiceName": NotRequired[str],
        "listenerPort": NotRequired[str],
    },
)
M2NonManagedApplicationActionTypeDef = TypedDict(
    "M2NonManagedApplicationActionTypeDef",
    {
        "resource": str,
        "actionType": M2NonManagedActionTypeType,
    },
)
M2NonManagedApplicationStepInputTypeDef = TypedDict(
    "M2NonManagedApplicationStepInputTypeDef",
    {
        "vpcEndpointServiceName": str,
        "listenerPort": int,
        "runtime": Literal["BluAge"],
        "actionType": M2NonManagedActionTypeType,
        "webAppName": NotRequired[str],
    },
)
M2NonManagedApplicationSummaryTypeDef = TypedDict(
    "M2NonManagedApplicationSummaryTypeDef",
    {
        "vpcEndpointServiceName": str,
        "listenerPort": int,
        "runtime": Literal["BluAge"],
        "webAppName": NotRequired[str],
    },
)
M2NonManagedApplicationTypeDef = TypedDict(
    "M2NonManagedApplicationTypeDef",
    {
        "vpcEndpointServiceName": str,
        "listenerPort": str,
        "runtime": Literal["BluAge"],
        "webAppName": NotRequired[str],
    },
)
OutputFileTypeDef = TypedDict(
    "OutputFileTypeDef",
    {
        "fileLocation": NotRequired[str],
    },
)
ScriptSummaryTypeDef = TypedDict(
    "ScriptSummaryTypeDef",
    {
        "scriptLocation": str,
        "type": Literal["Selenium"],
    },
)
ScriptTypeDef = TypedDict(
    "ScriptTypeDef",
    {
        "scriptLocation": str,
        "type": Literal["Selenium"],
    },
)
StartTestRunRequestRequestTypeDef = TypedDict(
    "StartTestRunRequestRequestTypeDef",
    {
        "testSuiteId": str,
        "testConfigurationId": NotRequired[str],
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
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
BatchStepOutputTypeDef = TypedDict(
    "BatchStepOutputTypeDef",
    {
        "dataSetExportLocation": NotRequired[str],
        "dmsOutputLocation": NotRequired[str],
        "dataSetDetails": NotRequired[List[DataSetTypeDef]],
    },
)
CompareDataSetsStepInputTypeDef = TypedDict(
    "CompareDataSetsStepInputTypeDef",
    {
        "sourceLocation": str,
        "targetLocation": str,
        "sourceDataSets": List[DataSetTypeDef],
        "targetDataSets": List[DataSetTypeDef],
    },
)
TN3270StepOutputTypeDef = TypedDict(
    "TN3270StepOutputTypeDef",
    {
        "scriptOutputLocation": str,
        "dataSetExportLocation": NotRequired[str],
        "dmsOutputLocation": NotRequired[str],
        "dataSetDetails": NotRequired[List[DataSetTypeDef]],
    },
)
BatchUnionTypeDef = Union[BatchTypeDef, BatchOutputTypeDef]
CloudFormationUnionTypeDef = Union[CloudFormationTypeDef, CloudFormationOutputTypeDef]
CompareDatabaseCDCStepInputTypeDef = TypedDict(
    "CompareDatabaseCDCStepInputTypeDef",
    {
        "sourceLocation": str,
        "targetLocation": str,
        "sourceMetadata": SourceDatabaseMetadataTypeDef,
        "targetMetadata": TargetDatabaseMetadataTypeDef,
        "outputLocation": NotRequired[str],
    },
)
DatabaseCDCTypeDef = TypedDict(
    "DatabaseCDCTypeDef",
    {
        "sourceMetadata": SourceDatabaseMetadataTypeDef,
        "targetMetadata": TargetDatabaseMetadataTypeDef,
    },
)
CreateCloudFormationSummaryTypeDef = TypedDict(
    "CreateCloudFormationSummaryTypeDef",
    {
        "stepInput": CreateCloudFormationStepInputTypeDef,
        "stepOutput": NotRequired[CreateCloudFormationStepOutputTypeDef],
    },
)
CreateTestCaseResponseTypeDef = TypedDict(
    "CreateTestCaseResponseTypeDef",
    {
        "testCaseId": str,
        "testCaseVersion": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTestConfigurationResponseTypeDef = TypedDict(
    "CreateTestConfigurationResponseTypeDef",
    {
        "testConfigurationId": str,
        "testConfigurationVersion": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTestSuiteResponseTypeDef = TypedDict(
    "CreateTestSuiteResponseTypeDef",
    {
        "testSuiteId": str,
        "testSuiteVersion": int,
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
StartTestRunResponseTypeDef = TypedDict(
    "StartTestRunResponseTypeDef",
    {
        "testRunId": str,
        "testRunStatus": TestRunStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTestCaseResponseTypeDef = TypedDict(
    "UpdateTestCaseResponseTypeDef",
    {
        "testCaseId": str,
        "testCaseVersion": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTestConfigurationResponseTypeDef = TypedDict(
    "UpdateTestConfigurationResponseTypeDef",
    {
        "testConfigurationId": str,
        "testConfigurationVersion": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTestSuiteResponseTypeDef = TypedDict(
    "UpdateTestSuiteResponseTypeDef",
    {
        "testSuiteId": str,
        "testSuiteVersion": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteCloudFormationSummaryTypeDef = TypedDict(
    "DeleteCloudFormationSummaryTypeDef",
    {
        "stepInput": DeleteCloudFormationStepInputTypeDef,
        "stepOutput": NotRequired[Dict[str, Any]],
    },
)
ListTestCasesRequestListTestCasesPaginateTypeDef = TypedDict(
    "ListTestCasesRequestListTestCasesPaginateTypeDef",
    {
        "testCaseIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTestConfigurationsRequestListTestConfigurationsPaginateTypeDef = TypedDict(
    "ListTestConfigurationsRequestListTestConfigurationsPaginateTypeDef",
    {
        "testConfigurationIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTestRunStepsRequestListTestRunStepsPaginateTypeDef = TypedDict(
    "ListTestRunStepsRequestListTestRunStepsPaginateTypeDef",
    {
        "testRunId": str,
        "testCaseId": NotRequired[str],
        "testSuiteId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTestRunTestCasesRequestListTestRunTestCasesPaginateTypeDef = TypedDict(
    "ListTestRunTestCasesRequestListTestRunTestCasesPaginateTypeDef",
    {
        "testRunId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTestRunsRequestListTestRunsPaginateTypeDef = TypedDict(
    "ListTestRunsRequestListTestRunsPaginateTypeDef",
    {
        "testSuiteId": NotRequired[str],
        "testRunIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTestSuitesRequestListTestSuitesPaginateTypeDef = TypedDict(
    "ListTestSuitesRequestListTestSuitesPaginateTypeDef",
    {
        "testSuiteIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTestCasesResponseTypeDef = TypedDict(
    "ListTestCasesResponseTypeDef",
    {
        "testCases": List[TestCaseSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTestConfigurationsResponseTypeDef = TypedDict(
    "ListTestConfigurationsResponseTypeDef",
    {
        "testConfigurations": List[TestConfigurationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTestRunStepsResponseTypeDef = TypedDict(
    "ListTestRunStepsResponseTypeDef",
    {
        "testRunSteps": List[TestRunStepSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTestRunTestCasesResponseTypeDef = TypedDict(
    "ListTestRunTestCasesResponseTypeDef",
    {
        "testRunTestCases": List[TestCaseRunSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTestRunsResponseTypeDef = TypedDict(
    "ListTestRunsResponseTypeDef",
    {
        "testRuns": List[TestRunSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTestSuitesResponseTypeDef = TypedDict(
    "ListTestSuitesResponseTypeDef",
    {
        "testSuites": List[TestSuiteSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
M2ManagedApplicationActionTypeDef = TypedDict(
    "M2ManagedApplicationActionTypeDef",
    {
        "resource": str,
        "actionType": M2ManagedActionTypeType,
        "properties": NotRequired[M2ManagedActionPropertiesTypeDef],
    },
)
M2ManagedApplicationStepInputTypeDef = TypedDict(
    "M2ManagedApplicationStepInputTypeDef",
    {
        "applicationId": str,
        "runtime": str,
        "actionType": M2ManagedActionTypeType,
        "vpcEndpointServiceName": NotRequired[str],
        "listenerPort": NotRequired[int],
        "properties": NotRequired[M2ManagedActionPropertiesTypeDef],
    },
)
M2NonManagedApplicationStepSummaryTypeDef = TypedDict(
    "M2NonManagedApplicationStepSummaryTypeDef",
    {
        "stepInput": M2NonManagedApplicationStepInputTypeDef,
        "stepOutput": NotRequired[Dict[str, Any]],
    },
)
MainframeResourceSummaryTypeDef = TypedDict(
    "MainframeResourceSummaryTypeDef",
    {
        "m2ManagedApplication": NotRequired[M2ManagedApplicationSummaryTypeDef],
        "m2NonManagedApplication": NotRequired[M2NonManagedApplicationSummaryTypeDef],
    },
)
ResourceTypeOutputTypeDef = TypedDict(
    "ResourceTypeOutputTypeDef",
    {
        "cloudFormation": NotRequired[CloudFormationOutputTypeDef],
        "m2ManagedApplication": NotRequired[M2ManagedApplicationTypeDef],
        "m2NonManagedApplication": NotRequired[M2NonManagedApplicationTypeDef],
    },
)
OutputTypeDef = TypedDict(
    "OutputTypeDef",
    {
        "file": NotRequired[OutputFileTypeDef],
    },
)
TN3270OutputTypeDef = TypedDict(
    "TN3270OutputTypeDef",
    {
        "script": ScriptTypeDef,
        "exportDataSetNames": NotRequired[List[str]],
    },
)
TN3270TypeDef = TypedDict(
    "TN3270TypeDef",
    {
        "script": ScriptTypeDef,
        "exportDataSetNames": NotRequired[Sequence[str]],
    },
)
CompareDataSetsSummaryTypeDef = TypedDict(
    "CompareDataSetsSummaryTypeDef",
    {
        "stepInput": CompareDataSetsStepInputTypeDef,
        "stepOutput": NotRequired[CompareDataSetsStepOutputTypeDef],
    },
)
ResourceTypeTypeDef = TypedDict(
    "ResourceTypeTypeDef",
    {
        "cloudFormation": NotRequired[CloudFormationUnionTypeDef],
        "m2ManagedApplication": NotRequired[M2ManagedApplicationTypeDef],
        "m2NonManagedApplication": NotRequired[M2NonManagedApplicationTypeDef],
    },
)
CompareDatabaseCDCSummaryTypeDef = TypedDict(
    "CompareDatabaseCDCSummaryTypeDef",
    {
        "stepInput": CompareDatabaseCDCStepInputTypeDef,
        "stepOutput": NotRequired[CompareDatabaseCDCStepOutputTypeDef],
    },
)
FileMetadataOutputTypeDef = TypedDict(
    "FileMetadataOutputTypeDef",
    {
        "dataSets": NotRequired[List[DataSetTypeDef]],
        "databaseCDC": NotRequired[DatabaseCDCTypeDef],
    },
)
FileMetadataTypeDef = TypedDict(
    "FileMetadataTypeDef",
    {
        "dataSets": NotRequired[Sequence[DataSetTypeDef]],
        "databaseCDC": NotRequired[DatabaseCDCTypeDef],
    },
)
CloudFormationStepSummaryTypeDef = TypedDict(
    "CloudFormationStepSummaryTypeDef",
    {
        "createCloudformation": NotRequired[CreateCloudFormationSummaryTypeDef],
        "deleteCloudformation": NotRequired[DeleteCloudFormationSummaryTypeDef],
    },
)
ResourceActionTypeDef = TypedDict(
    "ResourceActionTypeDef",
    {
        "m2ManagedApplicationAction": NotRequired[M2ManagedApplicationActionTypeDef],
        "m2NonManagedApplicationAction": NotRequired[M2NonManagedApplicationActionTypeDef],
        "cloudFormationAction": NotRequired[CloudFormationActionTypeDef],
    },
)
M2ManagedApplicationStepSummaryTypeDef = TypedDict(
    "M2ManagedApplicationStepSummaryTypeDef",
    {
        "stepInput": M2ManagedApplicationStepInputTypeDef,
        "stepOutput": NotRequired[M2ManagedApplicationStepOutputTypeDef],
    },
)
BatchStepInputTypeDef = TypedDict(
    "BatchStepInputTypeDef",
    {
        "resource": MainframeResourceSummaryTypeDef,
        "batchJobName": str,
        "batchJobParameters": NotRequired[Dict[str, str]],
        "exportDataSetNames": NotRequired[List[str]],
        "properties": NotRequired[MainframeActionPropertiesTypeDef],
    },
)
TN3270StepInputTypeDef = TypedDict(
    "TN3270StepInputTypeDef",
    {
        "resource": MainframeResourceSummaryTypeDef,
        "script": ScriptSummaryTypeDef,
        "exportDataSetNames": NotRequired[List[str]],
        "properties": NotRequired[MainframeActionPropertiesTypeDef],
    },
)
ResourceOutputTypeDef = TypedDict(
    "ResourceOutputTypeDef",
    {
        "name": str,
        "type": ResourceTypeOutputTypeDef,
    },
)
MainframeActionTypeOutputTypeDef = TypedDict(
    "MainframeActionTypeOutputTypeDef",
    {
        "batch": NotRequired[BatchOutputTypeDef],
        "tn3270": NotRequired[TN3270OutputTypeDef],
    },
)
TN3270UnionTypeDef = Union[TN3270TypeDef, TN3270OutputTypeDef]
ResourceTypeUnionTypeDef = Union[ResourceTypeTypeDef, ResourceTypeOutputTypeDef]
CompareFileTypeTypeDef = TypedDict(
    "CompareFileTypeTypeDef",
    {
        "datasets": NotRequired[CompareDataSetsSummaryTypeDef],
        "databaseCDC": NotRequired[CompareDatabaseCDCSummaryTypeDef],
    },
)
InputFileOutputTypeDef = TypedDict(
    "InputFileOutputTypeDef",
    {
        "sourceLocation": str,
        "targetLocation": str,
        "fileMetadata": FileMetadataOutputTypeDef,
    },
)
FileMetadataUnionTypeDef = Union[FileMetadataTypeDef, FileMetadataOutputTypeDef]
ResourceActionSummaryTypeDef = TypedDict(
    "ResourceActionSummaryTypeDef",
    {
        "cloudFormation": NotRequired[CloudFormationStepSummaryTypeDef],
        "m2ManagedApplication": NotRequired[M2ManagedApplicationStepSummaryTypeDef],
        "m2NonManagedApplication": NotRequired[M2NonManagedApplicationStepSummaryTypeDef],
    },
)
BatchSummaryTypeDef = TypedDict(
    "BatchSummaryTypeDef",
    {
        "stepInput": BatchStepInputTypeDef,
        "stepOutput": NotRequired[BatchStepOutputTypeDef],
    },
)
TN3270SummaryTypeDef = TypedDict(
    "TN3270SummaryTypeDef",
    {
        "stepInput": TN3270StepInputTypeDef,
        "stepOutput": NotRequired[TN3270StepOutputTypeDef],
    },
)
GetTestConfigurationResponseTypeDef = TypedDict(
    "GetTestConfigurationResponseTypeDef",
    {
        "testConfigurationId": str,
        "name": str,
        "testConfigurationArn": str,
        "latestVersion": TestConfigurationLatestVersionTypeDef,
        "testConfigurationVersion": int,
        "status": TestConfigurationLifecycleType,
        "statusReason": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "description": str,
        "resources": List[ResourceOutputTypeDef],
        "properties": Dict[str, str],
        "tags": Dict[str, str],
        "serviceSettings": ServiceSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MainframeActionOutputTypeDef = TypedDict(
    "MainframeActionOutputTypeDef",
    {
        "resource": str,
        "actionType": MainframeActionTypeOutputTypeDef,
        "properties": NotRequired[MainframeActionPropertiesTypeDef],
    },
)
MainframeActionTypeTypeDef = TypedDict(
    "MainframeActionTypeTypeDef",
    {
        "batch": NotRequired[BatchUnionTypeDef],
        "tn3270": NotRequired[TN3270UnionTypeDef],
    },
)
ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "name": str,
        "type": ResourceTypeUnionTypeDef,
    },
)
FileTypeDef = TypedDict(
    "FileTypeDef",
    {
        "fileType": NotRequired[CompareFileTypeTypeDef],
    },
)
InputOutputTypeDef = TypedDict(
    "InputOutputTypeDef",
    {
        "file": NotRequired[InputFileOutputTypeDef],
    },
)
InputFileTypeDef = TypedDict(
    "InputFileTypeDef",
    {
        "sourceLocation": str,
        "targetLocation": str,
        "fileMetadata": FileMetadataUnionTypeDef,
    },
)
MainframeActionSummaryTypeDef = TypedDict(
    "MainframeActionSummaryTypeDef",
    {
        "batch": NotRequired[BatchSummaryTypeDef],
        "tn3270": NotRequired[TN3270SummaryTypeDef],
    },
)
MainframeActionTypeUnionTypeDef = Union[
    MainframeActionTypeTypeDef, MainframeActionTypeOutputTypeDef
]
ResourceUnionTypeDef = Union[ResourceTypeDef, ResourceOutputTypeDef]
UpdateTestConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateTestConfigurationRequestRequestTypeDef",
    {
        "testConfigurationId": str,
        "description": NotRequired[str],
        "resources": NotRequired[Sequence[ResourceTypeDef]],
        "properties": NotRequired[Mapping[str, str]],
        "serviceSettings": NotRequired[ServiceSettingsTypeDef],
    },
)
CompareActionSummaryTypeDef = TypedDict(
    "CompareActionSummaryTypeDef",
    {
        "type": FileTypeDef,
    },
)
CompareActionOutputTypeDef = TypedDict(
    "CompareActionOutputTypeDef",
    {
        "input": InputOutputTypeDef,
        "output": NotRequired[OutputTypeDef],
    },
)
InputFileUnionTypeDef = Union[InputFileTypeDef, InputFileOutputTypeDef]
MainframeActionTypeDef = TypedDict(
    "MainframeActionTypeDef",
    {
        "resource": str,
        "actionType": MainframeActionTypeUnionTypeDef,
        "properties": NotRequired[MainframeActionPropertiesTypeDef],
    },
)
CreateTestConfigurationRequestRequestTypeDef = TypedDict(
    "CreateTestConfigurationRequestRequestTypeDef",
    {
        "name": str,
        "resources": Sequence[ResourceUnionTypeDef],
        "description": NotRequired[str],
        "properties": NotRequired[Mapping[str, str]],
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "serviceSettings": NotRequired[ServiceSettingsTypeDef],
    },
)
StepRunSummaryTypeDef = TypedDict(
    "StepRunSummaryTypeDef",
    {
        "mainframeAction": NotRequired[MainframeActionSummaryTypeDef],
        "compareAction": NotRequired[CompareActionSummaryTypeDef],
        "resourceAction": NotRequired[ResourceActionSummaryTypeDef],
    },
)
StepActionOutputTypeDef = TypedDict(
    "StepActionOutputTypeDef",
    {
        "resourceAction": NotRequired[ResourceActionTypeDef],
        "mainframeAction": NotRequired[MainframeActionOutputTypeDef],
        "compareAction": NotRequired[CompareActionOutputTypeDef],
    },
)
InputTypeDef = TypedDict(
    "InputTypeDef",
    {
        "file": NotRequired[InputFileUnionTypeDef],
    },
)
MainframeActionUnionTypeDef = Union[MainframeActionTypeDef, MainframeActionOutputTypeDef]
GetTestRunStepResponseTypeDef = TypedDict(
    "GetTestRunStepResponseTypeDef",
    {
        "stepName": str,
        "testRunId": str,
        "testCaseId": str,
        "testCaseVersion": int,
        "testSuiteId": str,
        "testSuiteVersion": int,
        "beforeStep": bool,
        "afterStep": bool,
        "status": StepRunStatusType,
        "statusReason": str,
        "runStartTime": datetime,
        "runEndTime": datetime,
        "stepRunSummary": StepRunSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StepOutputTypeDef = TypedDict(
    "StepOutputTypeDef",
    {
        "name": str,
        "action": StepActionOutputTypeDef,
        "description": NotRequired[str],
    },
)
InputUnionTypeDef = Union[InputTypeDef, InputOutputTypeDef]
GetTestCaseResponseTypeDef = TypedDict(
    "GetTestCaseResponseTypeDef",
    {
        "testCaseId": str,
        "testCaseArn": str,
        "name": str,
        "description": str,
        "latestVersion": TestCaseLatestVersionTypeDef,
        "testCaseVersion": int,
        "status": TestCaseLifecycleType,
        "statusReason": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "steps": List[StepOutputTypeDef],
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTestSuiteResponseTypeDef = TypedDict(
    "GetTestSuiteResponseTypeDef",
    {
        "testSuiteId": str,
        "name": str,
        "latestVersion": TestSuiteLatestVersionTypeDef,
        "testSuiteVersion": int,
        "status": TestSuiteLifecycleType,
        "statusReason": str,
        "testSuiteArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "description": str,
        "beforeSteps": List[StepOutputTypeDef],
        "afterSteps": List[StepOutputTypeDef],
        "testCases": TestCasesOutputTypeDef,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CompareActionTypeDef = TypedDict(
    "CompareActionTypeDef",
    {
        "input": InputUnionTypeDef,
        "output": NotRequired[OutputTypeDef],
    },
)
CompareActionUnionTypeDef = Union[CompareActionTypeDef, CompareActionOutputTypeDef]
StepActionTypeDef = TypedDict(
    "StepActionTypeDef",
    {
        "resourceAction": NotRequired[ResourceActionTypeDef],
        "mainframeAction": NotRequired[MainframeActionUnionTypeDef],
        "compareAction": NotRequired[CompareActionUnionTypeDef],
    },
)
StepActionUnionTypeDef = Union[StepActionTypeDef, StepActionOutputTypeDef]
StepTypeDef = TypedDict(
    "StepTypeDef",
    {
        "name": str,
        "action": StepActionUnionTypeDef,
        "description": NotRequired[str],
    },
)
CreateTestSuiteRequestRequestTypeDef = TypedDict(
    "CreateTestSuiteRequestRequestTypeDef",
    {
        "name": str,
        "testCases": TestCasesTypeDef,
        "description": NotRequired[str],
        "beforeSteps": NotRequired[Sequence[StepTypeDef]],
        "afterSteps": NotRequired[Sequence[StepTypeDef]],
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
StepUnionTypeDef = Union[StepTypeDef, StepOutputTypeDef]
UpdateTestCaseRequestRequestTypeDef = TypedDict(
    "UpdateTestCaseRequestRequestTypeDef",
    {
        "testCaseId": str,
        "description": NotRequired[str],
        "steps": NotRequired[Sequence[StepTypeDef]],
    },
)
UpdateTestSuiteRequestRequestTypeDef = TypedDict(
    "UpdateTestSuiteRequestRequestTypeDef",
    {
        "testSuiteId": str,
        "description": NotRequired[str],
        "beforeSteps": NotRequired[Sequence[StepTypeDef]],
        "afterSteps": NotRequired[Sequence[StepTypeDef]],
        "testCases": NotRequired[TestCasesTypeDef],
    },
)
CreateTestCaseRequestRequestTypeDef = TypedDict(
    "CreateTestCaseRequestRequestTypeDef",
    {
        "name": str,
        "steps": Sequence[StepUnionTypeDef],
        "description": NotRequired[str],
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
