"""
Type annotations for iotdeviceadvisor service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/type_defs/)

Usage::

    ```python
    from mypy_boto3_iotdeviceadvisor.type_defs import ResponseMetadataTypeDef

    data: ResponseMetadataTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AuthenticationMethodType,
    ProtocolType,
    StatusType,
    SuiteRunStatusType,
    TestCaseScenarioStatusType,
    TestCaseScenarioTypeType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "ResponseMetadataTypeDef",
    "DeleteSuiteDefinitionRequestRequestTypeDef",
    "DeviceUnderTestTypeDef",
    "GetEndpointRequestRequestTypeDef",
    "GetSuiteDefinitionRequestRequestTypeDef",
    "GetSuiteRunReportRequestRequestTypeDef",
    "GetSuiteRunRequestRequestTypeDef",
    "ListSuiteDefinitionsRequestRequestTypeDef",
    "ListSuiteRunsRequestRequestTypeDef",
    "SuiteRunInformationTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "StopSuiteRunRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TestCaseScenarioTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "CreateSuiteDefinitionResponseTypeDef",
    "GetEndpointResponseTypeDef",
    "GetSuiteRunReportResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartSuiteRunResponseTypeDef",
    "UpdateSuiteDefinitionResponseTypeDef",
    "SuiteDefinitionConfigurationOutputTypeDef",
    "SuiteDefinitionConfigurationTypeDef",
    "SuiteDefinitionInformationTypeDef",
    "SuiteRunConfigurationOutputTypeDef",
    "SuiteRunConfigurationTypeDef",
    "ListSuiteRunsResponseTypeDef",
    "TestCaseRunTypeDef",
    "GetSuiteDefinitionResponseTypeDef",
    "CreateSuiteDefinitionRequestRequestTypeDef",
    "UpdateSuiteDefinitionRequestRequestTypeDef",
    "ListSuiteDefinitionsResponseTypeDef",
    "StartSuiteRunRequestRequestTypeDef",
    "GroupResultTypeDef",
    "TestResultTypeDef",
    "GetSuiteRunResponseTypeDef",
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
DeleteSuiteDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteSuiteDefinitionRequestRequestTypeDef",
    {
        "suiteDefinitionId": str,
    },
)
DeviceUnderTestTypeDef = TypedDict(
    "DeviceUnderTestTypeDef",
    {
        "thingArn": NotRequired[str],
        "certificateArn": NotRequired[str],
        "deviceRoleArn": NotRequired[str],
    },
)
GetEndpointRequestRequestTypeDef = TypedDict(
    "GetEndpointRequestRequestTypeDef",
    {
        "thingArn": NotRequired[str],
        "certificateArn": NotRequired[str],
        "deviceRoleArn": NotRequired[str],
        "authenticationMethod": NotRequired[AuthenticationMethodType],
    },
)
GetSuiteDefinitionRequestRequestTypeDef = TypedDict(
    "GetSuiteDefinitionRequestRequestTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteDefinitionVersion": NotRequired[str],
    },
)
GetSuiteRunReportRequestRequestTypeDef = TypedDict(
    "GetSuiteRunReportRequestRequestTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteRunId": str,
    },
)
GetSuiteRunRequestRequestTypeDef = TypedDict(
    "GetSuiteRunRequestRequestTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteRunId": str,
    },
)
ListSuiteDefinitionsRequestRequestTypeDef = TypedDict(
    "ListSuiteDefinitionsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListSuiteRunsRequestRequestTypeDef = TypedDict(
    "ListSuiteRunsRequestRequestTypeDef",
    {
        "suiteDefinitionId": NotRequired[str],
        "suiteDefinitionVersion": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
SuiteRunInformationTypeDef = TypedDict(
    "SuiteRunInformationTypeDef",
    {
        "suiteDefinitionId": NotRequired[str],
        "suiteDefinitionVersion": NotRequired[str],
        "suiteDefinitionName": NotRequired[str],
        "suiteRunId": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "startedAt": NotRequired[datetime],
        "endAt": NotRequired[datetime],
        "status": NotRequired[SuiteRunStatusType],
        "passed": NotRequired[int],
        "failed": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
StopSuiteRunRequestRequestTypeDef = TypedDict(
    "StopSuiteRunRequestRequestTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteRunId": str,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)
TestCaseScenarioTypeDef = TypedDict(
    "TestCaseScenarioTypeDef",
    {
        "testCaseScenarioId": NotRequired[str],
        "testCaseScenarioType": NotRequired[TestCaseScenarioTypeType],
        "status": NotRequired[TestCaseScenarioStatusType],
        "failure": NotRequired[str],
        "systemMessage": NotRequired[str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
CreateSuiteDefinitionResponseTypeDef = TypedDict(
    "CreateSuiteDefinitionResponseTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteDefinitionArn": str,
        "suiteDefinitionName": str,
        "createdAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEndpointResponseTypeDef = TypedDict(
    "GetEndpointResponseTypeDef",
    {
        "endpoint": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSuiteRunReportResponseTypeDef = TypedDict(
    "GetSuiteRunReportResponseTypeDef",
    {
        "qualificationReportDownloadUrl": str,
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
StartSuiteRunResponseTypeDef = TypedDict(
    "StartSuiteRunResponseTypeDef",
    {
        "suiteRunId": str,
        "suiteRunArn": str,
        "createdAt": datetime,
        "endpoint": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSuiteDefinitionResponseTypeDef = TypedDict(
    "UpdateSuiteDefinitionResponseTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteDefinitionArn": str,
        "suiteDefinitionName": str,
        "suiteDefinitionVersion": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SuiteDefinitionConfigurationOutputTypeDef = TypedDict(
    "SuiteDefinitionConfigurationOutputTypeDef",
    {
        "suiteDefinitionName": str,
        "rootGroup": str,
        "devicePermissionRoleArn": str,
        "devices": NotRequired[List[DeviceUnderTestTypeDef]],
        "intendedForQualification": NotRequired[bool],
        "isLongDurationTest": NotRequired[bool],
        "protocol": NotRequired[ProtocolType],
    },
)
SuiteDefinitionConfigurationTypeDef = TypedDict(
    "SuiteDefinitionConfigurationTypeDef",
    {
        "suiteDefinitionName": str,
        "rootGroup": str,
        "devicePermissionRoleArn": str,
        "devices": NotRequired[Sequence[DeviceUnderTestTypeDef]],
        "intendedForQualification": NotRequired[bool],
        "isLongDurationTest": NotRequired[bool],
        "protocol": NotRequired[ProtocolType],
    },
)
SuiteDefinitionInformationTypeDef = TypedDict(
    "SuiteDefinitionInformationTypeDef",
    {
        "suiteDefinitionId": NotRequired[str],
        "suiteDefinitionName": NotRequired[str],
        "defaultDevices": NotRequired[List[DeviceUnderTestTypeDef]],
        "intendedForQualification": NotRequired[bool],
        "isLongDurationTest": NotRequired[bool],
        "protocol": NotRequired[ProtocolType],
        "createdAt": NotRequired[datetime],
    },
)
SuiteRunConfigurationOutputTypeDef = TypedDict(
    "SuiteRunConfigurationOutputTypeDef",
    {
        "primaryDevice": DeviceUnderTestTypeDef,
        "selectedTestList": NotRequired[List[str]],
        "parallelRun": NotRequired[bool],
    },
)
SuiteRunConfigurationTypeDef = TypedDict(
    "SuiteRunConfigurationTypeDef",
    {
        "primaryDevice": DeviceUnderTestTypeDef,
        "selectedTestList": NotRequired[Sequence[str]],
        "parallelRun": NotRequired[bool],
    },
)
ListSuiteRunsResponseTypeDef = TypedDict(
    "ListSuiteRunsResponseTypeDef",
    {
        "suiteRunsList": List[SuiteRunInformationTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TestCaseRunTypeDef = TypedDict(
    "TestCaseRunTypeDef",
    {
        "testCaseRunId": NotRequired[str],
        "testCaseDefinitionId": NotRequired[str],
        "testCaseDefinitionName": NotRequired[str],
        "status": NotRequired[StatusType],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
        "logUrl": NotRequired[str],
        "warnings": NotRequired[str],
        "failure": NotRequired[str],
        "testScenarios": NotRequired[List[TestCaseScenarioTypeDef]],
    },
)
GetSuiteDefinitionResponseTypeDef = TypedDict(
    "GetSuiteDefinitionResponseTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteDefinitionArn": str,
        "suiteDefinitionVersion": str,
        "latestVersion": str,
        "suiteDefinitionConfiguration": SuiteDefinitionConfigurationOutputTypeDef,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSuiteDefinitionRequestRequestTypeDef = TypedDict(
    "CreateSuiteDefinitionRequestRequestTypeDef",
    {
        "suiteDefinitionConfiguration": SuiteDefinitionConfigurationTypeDef,
        "tags": NotRequired[Mapping[str, str]],
        "clientToken": NotRequired[str],
    },
)
UpdateSuiteDefinitionRequestRequestTypeDef = TypedDict(
    "UpdateSuiteDefinitionRequestRequestTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteDefinitionConfiguration": SuiteDefinitionConfigurationTypeDef,
    },
)
ListSuiteDefinitionsResponseTypeDef = TypedDict(
    "ListSuiteDefinitionsResponseTypeDef",
    {
        "suiteDefinitionInformationList": List[SuiteDefinitionInformationTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartSuiteRunRequestRequestTypeDef = TypedDict(
    "StartSuiteRunRequestRequestTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteRunConfiguration": SuiteRunConfigurationTypeDef,
        "suiteDefinitionVersion": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
GroupResultTypeDef = TypedDict(
    "GroupResultTypeDef",
    {
        "groupId": NotRequired[str],
        "groupName": NotRequired[str],
        "tests": NotRequired[List[TestCaseRunTypeDef]],
    },
)
TestResultTypeDef = TypedDict(
    "TestResultTypeDef",
    {
        "groups": NotRequired[List[GroupResultTypeDef]],
    },
)
GetSuiteRunResponseTypeDef = TypedDict(
    "GetSuiteRunResponseTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteDefinitionVersion": str,
        "suiteRunId": str,
        "suiteRunArn": str,
        "suiteRunConfiguration": SuiteRunConfigurationOutputTypeDef,
        "testResult": TestResultTypeDef,
        "startTime": datetime,
        "endTime": datetime,
        "status": SuiteRunStatusType,
        "errorReason": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
