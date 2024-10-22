"""
Type annotations for devicefarm service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devicefarm/type_defs/)

Usage::

    ```python
    from mypy_boto3_devicefarm.type_defs import TrialMinutesTypeDef

    data: TrialMinutesTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    ArtifactCategoryType,
    ArtifactTypeType,
    BillingMethodType,
    DeviceAttributeType,
    DeviceAvailabilityType,
    DeviceFilterAttributeType,
    DeviceFormFactorType,
    DevicePlatformType,
    DevicePoolTypeType,
    ExecutionResultCodeType,
    ExecutionResultType,
    ExecutionStatusType,
    InstanceStatusType,
    InteractionModeType,
    NetworkProfileTypeType,
    OfferingTransactionTypeType,
    RuleOperatorType,
    SampleTypeType,
    TestGridSessionArtifactCategoryType,
    TestGridSessionArtifactTypeType,
    TestGridSessionStatusType,
    TestTypeType,
    UploadCategoryType,
    UploadStatusType,
    UploadTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "TrialMinutesTypeDef",
    "ArtifactTypeDef",
    "CPUTypeDef",
    "CountersTypeDef",
    "RuleTypeDef",
    "ResponseMetadataTypeDef",
    "CreateInstanceProfileRequestRequestTypeDef",
    "InstanceProfileTypeDef",
    "CreateNetworkProfileRequestRequestTypeDef",
    "NetworkProfileTypeDef",
    "VpcConfigTypeDef",
    "CreateRemoteAccessSessionConfigurationTypeDef",
    "TestGridVpcConfigTypeDef",
    "CreateTestGridUrlRequestRequestTypeDef",
    "CreateUploadRequestRequestTypeDef",
    "UploadTypeDef",
    "CreateVPCEConfigurationRequestRequestTypeDef",
    "VPCEConfigurationTypeDef",
    "CustomerArtifactPathsOutputTypeDef",
    "CustomerArtifactPathsTypeDef",
    "DeleteDevicePoolRequestRequestTypeDef",
    "DeleteInstanceProfileRequestRequestTypeDef",
    "DeleteNetworkProfileRequestRequestTypeDef",
    "DeleteProjectRequestRequestTypeDef",
    "DeleteRemoteAccessSessionRequestRequestTypeDef",
    "DeleteRunRequestRequestTypeDef",
    "DeleteTestGridProjectRequestRequestTypeDef",
    "DeleteUploadRequestRequestTypeDef",
    "DeleteVPCEConfigurationRequestRequestTypeDef",
    "DeviceFilterOutputTypeDef",
    "DeviceFilterTypeDef",
    "DeviceMinutesTypeDef",
    "IncompatibilityMessageTypeDef",
    "ResolutionTypeDef",
    "ExecutionConfigurationTypeDef",
    "GetDeviceInstanceRequestRequestTypeDef",
    "ScheduleRunTestTypeDef",
    "GetDevicePoolRequestRequestTypeDef",
    "GetDeviceRequestRequestTypeDef",
    "GetInstanceProfileRequestRequestTypeDef",
    "GetJobRequestRequestTypeDef",
    "GetNetworkProfileRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "GetOfferingStatusRequestRequestTypeDef",
    "GetProjectRequestRequestTypeDef",
    "GetRemoteAccessSessionRequestRequestTypeDef",
    "GetRunRequestRequestTypeDef",
    "GetSuiteRequestRequestTypeDef",
    "GetTestGridProjectRequestRequestTypeDef",
    "GetTestGridSessionRequestRequestTypeDef",
    "TestGridSessionTypeDef",
    "GetTestRequestRequestTypeDef",
    "GetUploadRequestRequestTypeDef",
    "GetVPCEConfigurationRequestRequestTypeDef",
    "InstallToRemoteAccessSessionRequestRequestTypeDef",
    "ListArtifactsRequestRequestTypeDef",
    "ListDeviceInstancesRequestRequestTypeDef",
    "ListDevicePoolsRequestRequestTypeDef",
    "ListInstanceProfilesRequestRequestTypeDef",
    "ListJobsRequestRequestTypeDef",
    "ListNetworkProfilesRequestRequestTypeDef",
    "ListOfferingPromotionsRequestRequestTypeDef",
    "OfferingPromotionTypeDef",
    "ListOfferingTransactionsRequestRequestTypeDef",
    "ListOfferingsRequestRequestTypeDef",
    "ListProjectsRequestRequestTypeDef",
    "ListRemoteAccessSessionsRequestRequestTypeDef",
    "ListRunsRequestRequestTypeDef",
    "ListSamplesRequestRequestTypeDef",
    "SampleTypeDef",
    "ListSuitesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagTypeDef",
    "ListTestGridProjectsRequestRequestTypeDef",
    "ListTestGridSessionActionsRequestRequestTypeDef",
    "TestGridSessionActionTypeDef",
    "ListTestGridSessionArtifactsRequestRequestTypeDef",
    "TestGridSessionArtifactTypeDef",
    "TimestampTypeDef",
    "ListTestsRequestRequestTypeDef",
    "ListUniqueProblemsRequestRequestTypeDef",
    "ListUploadsRequestRequestTypeDef",
    "ListVPCEConfigurationsRequestRequestTypeDef",
    "LocationTypeDef",
    "MonetaryAmountTypeDef",
    "ProblemDetailTypeDef",
    "VpcConfigOutputTypeDef",
    "PurchaseOfferingRequestRequestTypeDef",
    "RadiosTypeDef",
    "RenewOfferingRequestRequestTypeDef",
    "StopJobRequestRequestTypeDef",
    "StopRemoteAccessSessionRequestRequestTypeDef",
    "StopRunRequestRequestTypeDef",
    "TestGridVpcConfigOutputTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDeviceInstanceRequestRequestTypeDef",
    "UpdateInstanceProfileRequestRequestTypeDef",
    "UpdateNetworkProfileRequestRequestTypeDef",
    "UpdateUploadRequestRequestTypeDef",
    "UpdateVPCEConfigurationRequestRequestTypeDef",
    "AccountSettingsTypeDef",
    "CreateDevicePoolRequestRequestTypeDef",
    "DevicePoolTypeDef",
    "UpdateDevicePoolRequestRequestTypeDef",
    "CreateTestGridUrlResultTypeDef",
    "ListArtifactsResultTypeDef",
    "CreateInstanceProfileResultTypeDef",
    "DeviceInstanceTypeDef",
    "GetInstanceProfileResultTypeDef",
    "ListInstanceProfilesResultTypeDef",
    "UpdateInstanceProfileResultTypeDef",
    "CreateNetworkProfileResultTypeDef",
    "GetNetworkProfileResultTypeDef",
    "ListNetworkProfilesResultTypeDef",
    "UpdateNetworkProfileResultTypeDef",
    "CreateProjectRequestRequestTypeDef",
    "UpdateProjectRequestRequestTypeDef",
    "CreateRemoteAccessSessionRequestRequestTypeDef",
    "CreateTestGridProjectRequestRequestTypeDef",
    "UpdateTestGridProjectRequestRequestTypeDef",
    "CreateUploadResultTypeDef",
    "GetUploadResultTypeDef",
    "InstallToRemoteAccessSessionResultTypeDef",
    "ListUploadsResultTypeDef",
    "UpdateUploadResultTypeDef",
    "CreateVPCEConfigurationResultTypeDef",
    "GetVPCEConfigurationResultTypeDef",
    "ListVPCEConfigurationsResultTypeDef",
    "UpdateVPCEConfigurationResultTypeDef",
    "CustomerArtifactPathsUnionTypeDef",
    "DeviceSelectionResultTypeDef",
    "DeviceFilterUnionTypeDef",
    "SuiteTypeDef",
    "TestTypeDef",
    "GetOfferingStatusRequestGetOfferingStatusPaginateTypeDef",
    "ListArtifactsRequestListArtifactsPaginateTypeDef",
    "ListDeviceInstancesRequestListDeviceInstancesPaginateTypeDef",
    "ListDevicePoolsRequestListDevicePoolsPaginateTypeDef",
    "ListDevicesRequestListDevicesPaginateTypeDef",
    "ListInstanceProfilesRequestListInstanceProfilesPaginateTypeDef",
    "ListJobsRequestListJobsPaginateTypeDef",
    "ListNetworkProfilesRequestListNetworkProfilesPaginateTypeDef",
    "ListOfferingPromotionsRequestListOfferingPromotionsPaginateTypeDef",
    "ListOfferingTransactionsRequestListOfferingTransactionsPaginateTypeDef",
    "ListOfferingsRequestListOfferingsPaginateTypeDef",
    "ListProjectsRequestListProjectsPaginateTypeDef",
    "ListRemoteAccessSessionsRequestListRemoteAccessSessionsPaginateTypeDef",
    "ListRunsRequestListRunsPaginateTypeDef",
    "ListSamplesRequestListSamplesPaginateTypeDef",
    "ListSuitesRequestListSuitesPaginateTypeDef",
    "ListTestsRequestListTestsPaginateTypeDef",
    "ListUniqueProblemsRequestListUniqueProblemsPaginateTypeDef",
    "ListUploadsRequestListUploadsPaginateTypeDef",
    "ListVPCEConfigurationsRequestListVPCEConfigurationsPaginateTypeDef",
    "GetTestGridSessionResultTypeDef",
    "ListTestGridSessionsResultTypeDef",
    "ListOfferingPromotionsResultTypeDef",
    "ListSamplesResultTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "ListTestGridSessionActionsResultTypeDef",
    "ListTestGridSessionArtifactsResultTypeDef",
    "ListTestGridSessionsRequestRequestTypeDef",
    "RecurringChargeTypeDef",
    "ProjectTypeDef",
    "TestGridProjectTypeDef",
    "GetAccountSettingsResultTypeDef",
    "CreateDevicePoolResultTypeDef",
    "GetDevicePoolResultTypeDef",
    "ListDevicePoolsResultTypeDef",
    "UpdateDevicePoolResultTypeDef",
    "DeviceTypeDef",
    "GetDeviceInstanceResultTypeDef",
    "ListDeviceInstancesResultTypeDef",
    "UpdateDeviceInstanceResultTypeDef",
    "ScheduleRunConfigurationTypeDef",
    "RunTypeDef",
    "DeviceSelectionConfigurationTypeDef",
    "ListDevicesRequestRequestTypeDef",
    "GetSuiteResultTypeDef",
    "ListSuitesResultTypeDef",
    "GetTestResultTypeDef",
    "ListTestsResultTypeDef",
    "OfferingTypeDef",
    "CreateProjectResultTypeDef",
    "GetProjectResultTypeDef",
    "ListProjectsResultTypeDef",
    "UpdateProjectResultTypeDef",
    "CreateTestGridProjectResultTypeDef",
    "GetTestGridProjectResultTypeDef",
    "ListTestGridProjectsResultTypeDef",
    "UpdateTestGridProjectResultTypeDef",
    "DevicePoolCompatibilityResultTypeDef",
    "GetDeviceResultTypeDef",
    "JobTypeDef",
    "ListDevicesResultTypeDef",
    "ProblemTypeDef",
    "RemoteAccessSessionTypeDef",
    "GetDevicePoolCompatibilityRequestRequestTypeDef",
    "GetRunResultTypeDef",
    "ListRunsResultTypeDef",
    "ScheduleRunResultTypeDef",
    "StopRunResultTypeDef",
    "ScheduleRunRequestRequestTypeDef",
    "ListOfferingsResultTypeDef",
    "OfferingStatusTypeDef",
    "GetDevicePoolCompatibilityResultTypeDef",
    "GetJobResultTypeDef",
    "ListJobsResultTypeDef",
    "StopJobResultTypeDef",
    "UniqueProblemTypeDef",
    "CreateRemoteAccessSessionResultTypeDef",
    "GetRemoteAccessSessionResultTypeDef",
    "ListRemoteAccessSessionsResultTypeDef",
    "StopRemoteAccessSessionResultTypeDef",
    "GetOfferingStatusResultTypeDef",
    "OfferingTransactionTypeDef",
    "ListUniqueProblemsResultTypeDef",
    "ListOfferingTransactionsResultTypeDef",
    "PurchaseOfferingResultTypeDef",
    "RenewOfferingResultTypeDef",
)

TrialMinutesTypeDef = TypedDict(
    "TrialMinutesTypeDef",
    {
        "total": NotRequired[float],
        "remaining": NotRequired[float],
    },
)
ArtifactTypeDef = TypedDict(
    "ArtifactTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[ArtifactTypeType],
        "extension": NotRequired[str],
        "url": NotRequired[str],
    },
)
CPUTypeDef = TypedDict(
    "CPUTypeDef",
    {
        "frequency": NotRequired[str],
        "architecture": NotRequired[str],
        "clock": NotRequired[float],
    },
)
CountersTypeDef = TypedDict(
    "CountersTypeDef",
    {
        "total": NotRequired[int],
        "passed": NotRequired[int],
        "failed": NotRequired[int],
        "warned": NotRequired[int],
        "errored": NotRequired[int],
        "stopped": NotRequired[int],
        "skipped": NotRequired[int],
    },
)
RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "attribute": NotRequired[DeviceAttributeType],
        "operator": NotRequired[RuleOperatorType],
        "value": NotRequired[str],
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
CreateInstanceProfileRequestRequestTypeDef = TypedDict(
    "CreateInstanceProfileRequestRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "packageCleanup": NotRequired[bool],
        "excludeAppPackagesFromCleanup": NotRequired[Sequence[str]],
        "rebootAfterUse": NotRequired[bool],
    },
)
InstanceProfileTypeDef = TypedDict(
    "InstanceProfileTypeDef",
    {
        "arn": NotRequired[str],
        "packageCleanup": NotRequired[bool],
        "excludeAppPackagesFromCleanup": NotRequired[List[str]],
        "rebootAfterUse": NotRequired[bool],
        "name": NotRequired[str],
        "description": NotRequired[str],
    },
)
CreateNetworkProfileRequestRequestTypeDef = TypedDict(
    "CreateNetworkProfileRequestRequestTypeDef",
    {
        "projectArn": str,
        "name": str,
        "description": NotRequired[str],
        "type": NotRequired[NetworkProfileTypeType],
        "uplinkBandwidthBits": NotRequired[int],
        "downlinkBandwidthBits": NotRequired[int],
        "uplinkDelayMs": NotRequired[int],
        "downlinkDelayMs": NotRequired[int],
        "uplinkJitterMs": NotRequired[int],
        "downlinkJitterMs": NotRequired[int],
        "uplinkLossPercent": NotRequired[int],
        "downlinkLossPercent": NotRequired[int],
    },
)
NetworkProfileTypeDef = TypedDict(
    "NetworkProfileTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "type": NotRequired[NetworkProfileTypeType],
        "uplinkBandwidthBits": NotRequired[int],
        "downlinkBandwidthBits": NotRequired[int],
        "uplinkDelayMs": NotRequired[int],
        "downlinkDelayMs": NotRequired[int],
        "uplinkJitterMs": NotRequired[int],
        "downlinkJitterMs": NotRequired[int],
        "uplinkLossPercent": NotRequired[int],
        "downlinkLossPercent": NotRequired[int],
    },
)
VpcConfigTypeDef = TypedDict(
    "VpcConfigTypeDef",
    {
        "securityGroupIds": Sequence[str],
        "subnetIds": Sequence[str],
        "vpcId": str,
    },
)
CreateRemoteAccessSessionConfigurationTypeDef = TypedDict(
    "CreateRemoteAccessSessionConfigurationTypeDef",
    {
        "billingMethod": NotRequired[BillingMethodType],
        "vpceConfigurationArns": NotRequired[Sequence[str]],
    },
)
TestGridVpcConfigTypeDef = TypedDict(
    "TestGridVpcConfigTypeDef",
    {
        "securityGroupIds": Sequence[str],
        "subnetIds": Sequence[str],
        "vpcId": str,
    },
)
CreateTestGridUrlRequestRequestTypeDef = TypedDict(
    "CreateTestGridUrlRequestRequestTypeDef",
    {
        "projectArn": str,
        "expiresInSeconds": int,
    },
)
CreateUploadRequestRequestTypeDef = TypedDict(
    "CreateUploadRequestRequestTypeDef",
    {
        "projectArn": str,
        "name": str,
        "type": UploadTypeType,
        "contentType": NotRequired[str],
    },
)
UploadTypeDef = TypedDict(
    "UploadTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "created": NotRequired[datetime],
        "type": NotRequired[UploadTypeType],
        "status": NotRequired[UploadStatusType],
        "url": NotRequired[str],
        "metadata": NotRequired[str],
        "contentType": NotRequired[str],
        "message": NotRequired[str],
        "category": NotRequired[UploadCategoryType],
    },
)
CreateVPCEConfigurationRequestRequestTypeDef = TypedDict(
    "CreateVPCEConfigurationRequestRequestTypeDef",
    {
        "vpceConfigurationName": str,
        "vpceServiceName": str,
        "serviceDnsName": str,
        "vpceConfigurationDescription": NotRequired[str],
    },
)
VPCEConfigurationTypeDef = TypedDict(
    "VPCEConfigurationTypeDef",
    {
        "arn": NotRequired[str],
        "vpceConfigurationName": NotRequired[str],
        "vpceServiceName": NotRequired[str],
        "serviceDnsName": NotRequired[str],
        "vpceConfigurationDescription": NotRequired[str],
    },
)
CustomerArtifactPathsOutputTypeDef = TypedDict(
    "CustomerArtifactPathsOutputTypeDef",
    {
        "iosPaths": NotRequired[List[str]],
        "androidPaths": NotRequired[List[str]],
        "deviceHostPaths": NotRequired[List[str]],
    },
)
CustomerArtifactPathsTypeDef = TypedDict(
    "CustomerArtifactPathsTypeDef",
    {
        "iosPaths": NotRequired[Sequence[str]],
        "androidPaths": NotRequired[Sequence[str]],
        "deviceHostPaths": NotRequired[Sequence[str]],
    },
)
DeleteDevicePoolRequestRequestTypeDef = TypedDict(
    "DeleteDevicePoolRequestRequestTypeDef",
    {
        "arn": str,
    },
)
DeleteInstanceProfileRequestRequestTypeDef = TypedDict(
    "DeleteInstanceProfileRequestRequestTypeDef",
    {
        "arn": str,
    },
)
DeleteNetworkProfileRequestRequestTypeDef = TypedDict(
    "DeleteNetworkProfileRequestRequestTypeDef",
    {
        "arn": str,
    },
)
DeleteProjectRequestRequestTypeDef = TypedDict(
    "DeleteProjectRequestRequestTypeDef",
    {
        "arn": str,
    },
)
DeleteRemoteAccessSessionRequestRequestTypeDef = TypedDict(
    "DeleteRemoteAccessSessionRequestRequestTypeDef",
    {
        "arn": str,
    },
)
DeleteRunRequestRequestTypeDef = TypedDict(
    "DeleteRunRequestRequestTypeDef",
    {
        "arn": str,
    },
)
DeleteTestGridProjectRequestRequestTypeDef = TypedDict(
    "DeleteTestGridProjectRequestRequestTypeDef",
    {
        "projectArn": str,
    },
)
DeleteUploadRequestRequestTypeDef = TypedDict(
    "DeleteUploadRequestRequestTypeDef",
    {
        "arn": str,
    },
)
DeleteVPCEConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteVPCEConfigurationRequestRequestTypeDef",
    {
        "arn": str,
    },
)
DeviceFilterOutputTypeDef = TypedDict(
    "DeviceFilterOutputTypeDef",
    {
        "attribute": DeviceFilterAttributeType,
        "operator": RuleOperatorType,
        "values": List[str],
    },
)
DeviceFilterTypeDef = TypedDict(
    "DeviceFilterTypeDef",
    {
        "attribute": DeviceFilterAttributeType,
        "operator": RuleOperatorType,
        "values": Sequence[str],
    },
)
DeviceMinutesTypeDef = TypedDict(
    "DeviceMinutesTypeDef",
    {
        "total": NotRequired[float],
        "metered": NotRequired[float],
        "unmetered": NotRequired[float],
    },
)
IncompatibilityMessageTypeDef = TypedDict(
    "IncompatibilityMessageTypeDef",
    {
        "message": NotRequired[str],
        "type": NotRequired[DeviceAttributeType],
    },
)
ResolutionTypeDef = TypedDict(
    "ResolutionTypeDef",
    {
        "width": NotRequired[int],
        "height": NotRequired[int],
    },
)
ExecutionConfigurationTypeDef = TypedDict(
    "ExecutionConfigurationTypeDef",
    {
        "jobTimeoutMinutes": NotRequired[int],
        "accountsCleanup": NotRequired[bool],
        "appPackagesCleanup": NotRequired[bool],
        "videoCapture": NotRequired[bool],
        "skipAppResign": NotRequired[bool],
    },
)
GetDeviceInstanceRequestRequestTypeDef = TypedDict(
    "GetDeviceInstanceRequestRequestTypeDef",
    {
        "arn": str,
    },
)
ScheduleRunTestTypeDef = TypedDict(
    "ScheduleRunTestTypeDef",
    {
        "type": TestTypeType,
        "testPackageArn": NotRequired[str],
        "testSpecArn": NotRequired[str],
        "filter": NotRequired[str],
        "parameters": NotRequired[Mapping[str, str]],
    },
)
GetDevicePoolRequestRequestTypeDef = TypedDict(
    "GetDevicePoolRequestRequestTypeDef",
    {
        "arn": str,
    },
)
GetDeviceRequestRequestTypeDef = TypedDict(
    "GetDeviceRequestRequestTypeDef",
    {
        "arn": str,
    },
)
GetInstanceProfileRequestRequestTypeDef = TypedDict(
    "GetInstanceProfileRequestRequestTypeDef",
    {
        "arn": str,
    },
)
GetJobRequestRequestTypeDef = TypedDict(
    "GetJobRequestRequestTypeDef",
    {
        "arn": str,
    },
)
GetNetworkProfileRequestRequestTypeDef = TypedDict(
    "GetNetworkProfileRequestRequestTypeDef",
    {
        "arn": str,
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
GetOfferingStatusRequestRequestTypeDef = TypedDict(
    "GetOfferingStatusRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
    },
)
GetProjectRequestRequestTypeDef = TypedDict(
    "GetProjectRequestRequestTypeDef",
    {
        "arn": str,
    },
)
GetRemoteAccessSessionRequestRequestTypeDef = TypedDict(
    "GetRemoteAccessSessionRequestRequestTypeDef",
    {
        "arn": str,
    },
)
GetRunRequestRequestTypeDef = TypedDict(
    "GetRunRequestRequestTypeDef",
    {
        "arn": str,
    },
)
GetSuiteRequestRequestTypeDef = TypedDict(
    "GetSuiteRequestRequestTypeDef",
    {
        "arn": str,
    },
)
GetTestGridProjectRequestRequestTypeDef = TypedDict(
    "GetTestGridProjectRequestRequestTypeDef",
    {
        "projectArn": str,
    },
)
GetTestGridSessionRequestRequestTypeDef = TypedDict(
    "GetTestGridSessionRequestRequestTypeDef",
    {
        "projectArn": NotRequired[str],
        "sessionId": NotRequired[str],
        "sessionArn": NotRequired[str],
    },
)
TestGridSessionTypeDef = TypedDict(
    "TestGridSessionTypeDef",
    {
        "arn": NotRequired[str],
        "status": NotRequired[TestGridSessionStatusType],
        "created": NotRequired[datetime],
        "ended": NotRequired[datetime],
        "billingMinutes": NotRequired[float],
        "seleniumProperties": NotRequired[str],
    },
)
GetTestRequestRequestTypeDef = TypedDict(
    "GetTestRequestRequestTypeDef",
    {
        "arn": str,
    },
)
GetUploadRequestRequestTypeDef = TypedDict(
    "GetUploadRequestRequestTypeDef",
    {
        "arn": str,
    },
)
GetVPCEConfigurationRequestRequestTypeDef = TypedDict(
    "GetVPCEConfigurationRequestRequestTypeDef",
    {
        "arn": str,
    },
)
InstallToRemoteAccessSessionRequestRequestTypeDef = TypedDict(
    "InstallToRemoteAccessSessionRequestRequestTypeDef",
    {
        "remoteAccessSessionArn": str,
        "appArn": str,
    },
)
ListArtifactsRequestRequestTypeDef = TypedDict(
    "ListArtifactsRequestRequestTypeDef",
    {
        "arn": str,
        "type": ArtifactCategoryType,
        "nextToken": NotRequired[str],
    },
)
ListDeviceInstancesRequestRequestTypeDef = TypedDict(
    "ListDeviceInstancesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListDevicePoolsRequestRequestTypeDef = TypedDict(
    "ListDevicePoolsRequestRequestTypeDef",
    {
        "arn": str,
        "type": NotRequired[DevicePoolTypeType],
        "nextToken": NotRequired[str],
    },
)
ListInstanceProfilesRequestRequestTypeDef = TypedDict(
    "ListInstanceProfilesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListJobsRequestRequestTypeDef = TypedDict(
    "ListJobsRequestRequestTypeDef",
    {
        "arn": str,
        "nextToken": NotRequired[str],
    },
)
ListNetworkProfilesRequestRequestTypeDef = TypedDict(
    "ListNetworkProfilesRequestRequestTypeDef",
    {
        "arn": str,
        "type": NotRequired[NetworkProfileTypeType],
        "nextToken": NotRequired[str],
    },
)
ListOfferingPromotionsRequestRequestTypeDef = TypedDict(
    "ListOfferingPromotionsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
    },
)
OfferingPromotionTypeDef = TypedDict(
    "OfferingPromotionTypeDef",
    {
        "id": NotRequired[str],
        "description": NotRequired[str],
    },
)
ListOfferingTransactionsRequestRequestTypeDef = TypedDict(
    "ListOfferingTransactionsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
    },
)
ListOfferingsRequestRequestTypeDef = TypedDict(
    "ListOfferingsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
    },
)
ListProjectsRequestRequestTypeDef = TypedDict(
    "ListProjectsRequestRequestTypeDef",
    {
        "arn": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)
ListRemoteAccessSessionsRequestRequestTypeDef = TypedDict(
    "ListRemoteAccessSessionsRequestRequestTypeDef",
    {
        "arn": str,
        "nextToken": NotRequired[str],
    },
)
ListRunsRequestRequestTypeDef = TypedDict(
    "ListRunsRequestRequestTypeDef",
    {
        "arn": str,
        "nextToken": NotRequired[str],
    },
)
ListSamplesRequestRequestTypeDef = TypedDict(
    "ListSamplesRequestRequestTypeDef",
    {
        "arn": str,
        "nextToken": NotRequired[str],
    },
)
SampleTypeDef = TypedDict(
    "SampleTypeDef",
    {
        "arn": NotRequired[str],
        "type": NotRequired[SampleTypeType],
        "url": NotRequired[str],
    },
)
ListSuitesRequestRequestTypeDef = TypedDict(
    "ListSuitesRequestRequestTypeDef",
    {
        "arn": str,
        "nextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
ListTestGridProjectsRequestRequestTypeDef = TypedDict(
    "ListTestGridProjectsRequestRequestTypeDef",
    {
        "maxResult": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListTestGridSessionActionsRequestRequestTypeDef = TypedDict(
    "ListTestGridSessionActionsRequestRequestTypeDef",
    {
        "sessionArn": str,
        "maxResult": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
TestGridSessionActionTypeDef = TypedDict(
    "TestGridSessionActionTypeDef",
    {
        "action": NotRequired[str],
        "started": NotRequired[datetime],
        "duration": NotRequired[int],
        "statusCode": NotRequired[str],
        "requestMethod": NotRequired[str],
    },
)
ListTestGridSessionArtifactsRequestRequestTypeDef = TypedDict(
    "ListTestGridSessionArtifactsRequestRequestTypeDef",
    {
        "sessionArn": str,
        "type": NotRequired[TestGridSessionArtifactCategoryType],
        "maxResult": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
TestGridSessionArtifactTypeDef = TypedDict(
    "TestGridSessionArtifactTypeDef",
    {
        "filename": NotRequired[str],
        "type": NotRequired[TestGridSessionArtifactTypeType],
        "url": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
ListTestsRequestRequestTypeDef = TypedDict(
    "ListTestsRequestRequestTypeDef",
    {
        "arn": str,
        "nextToken": NotRequired[str],
    },
)
ListUniqueProblemsRequestRequestTypeDef = TypedDict(
    "ListUniqueProblemsRequestRequestTypeDef",
    {
        "arn": str,
        "nextToken": NotRequired[str],
    },
)
ListUploadsRequestRequestTypeDef = TypedDict(
    "ListUploadsRequestRequestTypeDef",
    {
        "arn": str,
        "type": NotRequired[UploadTypeType],
        "nextToken": NotRequired[str],
    },
)
ListVPCEConfigurationsRequestRequestTypeDef = TypedDict(
    "ListVPCEConfigurationsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
LocationTypeDef = TypedDict(
    "LocationTypeDef",
    {
        "latitude": float,
        "longitude": float,
    },
)
MonetaryAmountTypeDef = TypedDict(
    "MonetaryAmountTypeDef",
    {
        "amount": NotRequired[float],
        "currencyCode": NotRequired[Literal["USD"]],
    },
)
ProblemDetailTypeDef = TypedDict(
    "ProblemDetailTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
    },
)
VpcConfigOutputTypeDef = TypedDict(
    "VpcConfigOutputTypeDef",
    {
        "securityGroupIds": List[str],
        "subnetIds": List[str],
        "vpcId": str,
    },
)
PurchaseOfferingRequestRequestTypeDef = TypedDict(
    "PurchaseOfferingRequestRequestTypeDef",
    {
        "offeringId": str,
        "quantity": int,
        "offeringPromotionId": NotRequired[str],
    },
)
RadiosTypeDef = TypedDict(
    "RadiosTypeDef",
    {
        "wifi": NotRequired[bool],
        "bluetooth": NotRequired[bool],
        "nfc": NotRequired[bool],
        "gps": NotRequired[bool],
    },
)
RenewOfferingRequestRequestTypeDef = TypedDict(
    "RenewOfferingRequestRequestTypeDef",
    {
        "offeringId": str,
        "quantity": int,
    },
)
StopJobRequestRequestTypeDef = TypedDict(
    "StopJobRequestRequestTypeDef",
    {
        "arn": str,
    },
)
StopRemoteAccessSessionRequestRequestTypeDef = TypedDict(
    "StopRemoteAccessSessionRequestRequestTypeDef",
    {
        "arn": str,
    },
)
StopRunRequestRequestTypeDef = TypedDict(
    "StopRunRequestRequestTypeDef",
    {
        "arn": str,
    },
)
TestGridVpcConfigOutputTypeDef = TypedDict(
    "TestGridVpcConfigOutputTypeDef",
    {
        "securityGroupIds": List[str],
        "subnetIds": List[str],
        "vpcId": str,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
UpdateDeviceInstanceRequestRequestTypeDef = TypedDict(
    "UpdateDeviceInstanceRequestRequestTypeDef",
    {
        "arn": str,
        "profileArn": NotRequired[str],
        "labels": NotRequired[Sequence[str]],
    },
)
UpdateInstanceProfileRequestRequestTypeDef = TypedDict(
    "UpdateInstanceProfileRequestRequestTypeDef",
    {
        "arn": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "packageCleanup": NotRequired[bool],
        "excludeAppPackagesFromCleanup": NotRequired[Sequence[str]],
        "rebootAfterUse": NotRequired[bool],
    },
)
UpdateNetworkProfileRequestRequestTypeDef = TypedDict(
    "UpdateNetworkProfileRequestRequestTypeDef",
    {
        "arn": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "type": NotRequired[NetworkProfileTypeType],
        "uplinkBandwidthBits": NotRequired[int],
        "downlinkBandwidthBits": NotRequired[int],
        "uplinkDelayMs": NotRequired[int],
        "downlinkDelayMs": NotRequired[int],
        "uplinkJitterMs": NotRequired[int],
        "downlinkJitterMs": NotRequired[int],
        "uplinkLossPercent": NotRequired[int],
        "downlinkLossPercent": NotRequired[int],
    },
)
UpdateUploadRequestRequestTypeDef = TypedDict(
    "UpdateUploadRequestRequestTypeDef",
    {
        "arn": str,
        "name": NotRequired[str],
        "contentType": NotRequired[str],
        "editContent": NotRequired[bool],
    },
)
UpdateVPCEConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateVPCEConfigurationRequestRequestTypeDef",
    {
        "arn": str,
        "vpceConfigurationName": NotRequired[str],
        "vpceServiceName": NotRequired[str],
        "serviceDnsName": NotRequired[str],
        "vpceConfigurationDescription": NotRequired[str],
    },
)
AccountSettingsTypeDef = TypedDict(
    "AccountSettingsTypeDef",
    {
        "awsAccountNumber": NotRequired[str],
        "unmeteredDevices": NotRequired[Dict[DevicePlatformType, int]],
        "unmeteredRemoteAccessDevices": NotRequired[Dict[DevicePlatformType, int]],
        "maxJobTimeoutMinutes": NotRequired[int],
        "trialMinutes": NotRequired[TrialMinutesTypeDef],
        "maxSlots": NotRequired[Dict[str, int]],
        "defaultJobTimeoutMinutes": NotRequired[int],
        "skipAppResign": NotRequired[bool],
    },
)
CreateDevicePoolRequestRequestTypeDef = TypedDict(
    "CreateDevicePoolRequestRequestTypeDef",
    {
        "projectArn": str,
        "name": str,
        "rules": Sequence[RuleTypeDef],
        "description": NotRequired[str],
        "maxDevices": NotRequired[int],
    },
)
DevicePoolTypeDef = TypedDict(
    "DevicePoolTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "type": NotRequired[DevicePoolTypeType],
        "rules": NotRequired[List[RuleTypeDef]],
        "maxDevices": NotRequired[int],
    },
)
UpdateDevicePoolRequestRequestTypeDef = TypedDict(
    "UpdateDevicePoolRequestRequestTypeDef",
    {
        "arn": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "rules": NotRequired[Sequence[RuleTypeDef]],
        "maxDevices": NotRequired[int],
        "clearMaxDevices": NotRequired[bool],
    },
)
CreateTestGridUrlResultTypeDef = TypedDict(
    "CreateTestGridUrlResultTypeDef",
    {
        "url": str,
        "expires": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListArtifactsResultTypeDef = TypedDict(
    "ListArtifactsResultTypeDef",
    {
        "artifacts": List[ArtifactTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateInstanceProfileResultTypeDef = TypedDict(
    "CreateInstanceProfileResultTypeDef",
    {
        "instanceProfile": InstanceProfileTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeviceInstanceTypeDef = TypedDict(
    "DeviceInstanceTypeDef",
    {
        "arn": NotRequired[str],
        "deviceArn": NotRequired[str],
        "labels": NotRequired[List[str]],
        "status": NotRequired[InstanceStatusType],
        "udid": NotRequired[str],
        "instanceProfile": NotRequired[InstanceProfileTypeDef],
    },
)
GetInstanceProfileResultTypeDef = TypedDict(
    "GetInstanceProfileResultTypeDef",
    {
        "instanceProfile": InstanceProfileTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListInstanceProfilesResultTypeDef = TypedDict(
    "ListInstanceProfilesResultTypeDef",
    {
        "instanceProfiles": List[InstanceProfileTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateInstanceProfileResultTypeDef = TypedDict(
    "UpdateInstanceProfileResultTypeDef",
    {
        "instanceProfile": InstanceProfileTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateNetworkProfileResultTypeDef = TypedDict(
    "CreateNetworkProfileResultTypeDef",
    {
        "networkProfile": NetworkProfileTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetNetworkProfileResultTypeDef = TypedDict(
    "GetNetworkProfileResultTypeDef",
    {
        "networkProfile": NetworkProfileTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListNetworkProfilesResultTypeDef = TypedDict(
    "ListNetworkProfilesResultTypeDef",
    {
        "networkProfiles": List[NetworkProfileTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateNetworkProfileResultTypeDef = TypedDict(
    "UpdateNetworkProfileResultTypeDef",
    {
        "networkProfile": NetworkProfileTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProjectRequestRequestTypeDef = TypedDict(
    "CreateProjectRequestRequestTypeDef",
    {
        "name": str,
        "defaultJobTimeoutMinutes": NotRequired[int],
        "vpcConfig": NotRequired[VpcConfigTypeDef],
    },
)
UpdateProjectRequestRequestTypeDef = TypedDict(
    "UpdateProjectRequestRequestTypeDef",
    {
        "arn": str,
        "name": NotRequired[str],
        "defaultJobTimeoutMinutes": NotRequired[int],
        "vpcConfig": NotRequired[VpcConfigTypeDef],
    },
)
CreateRemoteAccessSessionRequestRequestTypeDef = TypedDict(
    "CreateRemoteAccessSessionRequestRequestTypeDef",
    {
        "projectArn": str,
        "deviceArn": str,
        "instanceArn": NotRequired[str],
        "sshPublicKey": NotRequired[str],
        "remoteDebugEnabled": NotRequired[bool],
        "remoteRecordEnabled": NotRequired[bool],
        "remoteRecordAppArn": NotRequired[str],
        "name": NotRequired[str],
        "clientId": NotRequired[str],
        "configuration": NotRequired[CreateRemoteAccessSessionConfigurationTypeDef],
        "interactionMode": NotRequired[InteractionModeType],
        "skipAppResign": NotRequired[bool],
    },
)
CreateTestGridProjectRequestRequestTypeDef = TypedDict(
    "CreateTestGridProjectRequestRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "vpcConfig": NotRequired[TestGridVpcConfigTypeDef],
    },
)
UpdateTestGridProjectRequestRequestTypeDef = TypedDict(
    "UpdateTestGridProjectRequestRequestTypeDef",
    {
        "projectArn": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "vpcConfig": NotRequired[TestGridVpcConfigTypeDef],
    },
)
CreateUploadResultTypeDef = TypedDict(
    "CreateUploadResultTypeDef",
    {
        "upload": UploadTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetUploadResultTypeDef = TypedDict(
    "GetUploadResultTypeDef",
    {
        "upload": UploadTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InstallToRemoteAccessSessionResultTypeDef = TypedDict(
    "InstallToRemoteAccessSessionResultTypeDef",
    {
        "appUpload": UploadTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListUploadsResultTypeDef = TypedDict(
    "ListUploadsResultTypeDef",
    {
        "uploads": List[UploadTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateUploadResultTypeDef = TypedDict(
    "UpdateUploadResultTypeDef",
    {
        "upload": UploadTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateVPCEConfigurationResultTypeDef = TypedDict(
    "CreateVPCEConfigurationResultTypeDef",
    {
        "vpceConfiguration": VPCEConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetVPCEConfigurationResultTypeDef = TypedDict(
    "GetVPCEConfigurationResultTypeDef",
    {
        "vpceConfiguration": VPCEConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListVPCEConfigurationsResultTypeDef = TypedDict(
    "ListVPCEConfigurationsResultTypeDef",
    {
        "vpceConfigurations": List[VPCEConfigurationTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateVPCEConfigurationResultTypeDef = TypedDict(
    "UpdateVPCEConfigurationResultTypeDef",
    {
        "vpceConfiguration": VPCEConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CustomerArtifactPathsUnionTypeDef = Union[
    CustomerArtifactPathsTypeDef, CustomerArtifactPathsOutputTypeDef
]
DeviceSelectionResultTypeDef = TypedDict(
    "DeviceSelectionResultTypeDef",
    {
        "filters": NotRequired[List[DeviceFilterOutputTypeDef]],
        "matchedDevicesCount": NotRequired[int],
        "maxDevices": NotRequired[int],
    },
)
DeviceFilterUnionTypeDef = Union[DeviceFilterTypeDef, DeviceFilterOutputTypeDef]
SuiteTypeDef = TypedDict(
    "SuiteTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[TestTypeType],
        "created": NotRequired[datetime],
        "status": NotRequired[ExecutionStatusType],
        "result": NotRequired[ExecutionResultType],
        "started": NotRequired[datetime],
        "stopped": NotRequired[datetime],
        "counters": NotRequired[CountersTypeDef],
        "message": NotRequired[str],
        "deviceMinutes": NotRequired[DeviceMinutesTypeDef],
    },
)
TestTypeDef = TypedDict(
    "TestTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[TestTypeType],
        "created": NotRequired[datetime],
        "status": NotRequired[ExecutionStatusType],
        "result": NotRequired[ExecutionResultType],
        "started": NotRequired[datetime],
        "stopped": NotRequired[datetime],
        "counters": NotRequired[CountersTypeDef],
        "message": NotRequired[str],
        "deviceMinutes": NotRequired[DeviceMinutesTypeDef],
    },
)
GetOfferingStatusRequestGetOfferingStatusPaginateTypeDef = TypedDict(
    "GetOfferingStatusRequestGetOfferingStatusPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListArtifactsRequestListArtifactsPaginateTypeDef = TypedDict(
    "ListArtifactsRequestListArtifactsPaginateTypeDef",
    {
        "arn": str,
        "type": ArtifactCategoryType,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDeviceInstancesRequestListDeviceInstancesPaginateTypeDef = TypedDict(
    "ListDeviceInstancesRequestListDeviceInstancesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDevicePoolsRequestListDevicePoolsPaginateTypeDef = TypedDict(
    "ListDevicePoolsRequestListDevicePoolsPaginateTypeDef",
    {
        "arn": str,
        "type": NotRequired[DevicePoolTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDevicesRequestListDevicesPaginateTypeDef = TypedDict(
    "ListDevicesRequestListDevicesPaginateTypeDef",
    {
        "arn": NotRequired[str],
        "filters": NotRequired[Sequence[DeviceFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListInstanceProfilesRequestListInstanceProfilesPaginateTypeDef = TypedDict(
    "ListInstanceProfilesRequestListInstanceProfilesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListJobsRequestListJobsPaginateTypeDef = TypedDict(
    "ListJobsRequestListJobsPaginateTypeDef",
    {
        "arn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListNetworkProfilesRequestListNetworkProfilesPaginateTypeDef = TypedDict(
    "ListNetworkProfilesRequestListNetworkProfilesPaginateTypeDef",
    {
        "arn": str,
        "type": NotRequired[NetworkProfileTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOfferingPromotionsRequestListOfferingPromotionsPaginateTypeDef = TypedDict(
    "ListOfferingPromotionsRequestListOfferingPromotionsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOfferingTransactionsRequestListOfferingTransactionsPaginateTypeDef = TypedDict(
    "ListOfferingTransactionsRequestListOfferingTransactionsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOfferingsRequestListOfferingsPaginateTypeDef = TypedDict(
    "ListOfferingsRequestListOfferingsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProjectsRequestListProjectsPaginateTypeDef = TypedDict(
    "ListProjectsRequestListProjectsPaginateTypeDef",
    {
        "arn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRemoteAccessSessionsRequestListRemoteAccessSessionsPaginateTypeDef = TypedDict(
    "ListRemoteAccessSessionsRequestListRemoteAccessSessionsPaginateTypeDef",
    {
        "arn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRunsRequestListRunsPaginateTypeDef = TypedDict(
    "ListRunsRequestListRunsPaginateTypeDef",
    {
        "arn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSamplesRequestListSamplesPaginateTypeDef = TypedDict(
    "ListSamplesRequestListSamplesPaginateTypeDef",
    {
        "arn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSuitesRequestListSuitesPaginateTypeDef = TypedDict(
    "ListSuitesRequestListSuitesPaginateTypeDef",
    {
        "arn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTestsRequestListTestsPaginateTypeDef = TypedDict(
    "ListTestsRequestListTestsPaginateTypeDef",
    {
        "arn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListUniqueProblemsRequestListUniqueProblemsPaginateTypeDef = TypedDict(
    "ListUniqueProblemsRequestListUniqueProblemsPaginateTypeDef",
    {
        "arn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListUploadsRequestListUploadsPaginateTypeDef = TypedDict(
    "ListUploadsRequestListUploadsPaginateTypeDef",
    {
        "arn": str,
        "type": NotRequired[UploadTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListVPCEConfigurationsRequestListVPCEConfigurationsPaginateTypeDef = TypedDict(
    "ListVPCEConfigurationsRequestListVPCEConfigurationsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetTestGridSessionResultTypeDef = TypedDict(
    "GetTestGridSessionResultTypeDef",
    {
        "testGridSession": TestGridSessionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTestGridSessionsResultTypeDef = TypedDict(
    "ListTestGridSessionsResultTypeDef",
    {
        "testGridSessions": List[TestGridSessionTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListOfferingPromotionsResultTypeDef = TypedDict(
    "ListOfferingPromotionsResultTypeDef",
    {
        "offeringPromotions": List[OfferingPromotionTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSamplesResultTypeDef = TypedDict(
    "ListSamplesResultTypeDef",
    {
        "samples": List[SampleTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
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
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)
ListTestGridSessionActionsResultTypeDef = TypedDict(
    "ListTestGridSessionActionsResultTypeDef",
    {
        "actions": List[TestGridSessionActionTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTestGridSessionArtifactsResultTypeDef = TypedDict(
    "ListTestGridSessionArtifactsResultTypeDef",
    {
        "artifacts": List[TestGridSessionArtifactTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTestGridSessionsRequestRequestTypeDef = TypedDict(
    "ListTestGridSessionsRequestRequestTypeDef",
    {
        "projectArn": str,
        "status": NotRequired[TestGridSessionStatusType],
        "creationTimeAfter": NotRequired[TimestampTypeDef],
        "creationTimeBefore": NotRequired[TimestampTypeDef],
        "endTimeAfter": NotRequired[TimestampTypeDef],
        "endTimeBefore": NotRequired[TimestampTypeDef],
        "maxResult": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
RecurringChargeTypeDef = TypedDict(
    "RecurringChargeTypeDef",
    {
        "cost": NotRequired[MonetaryAmountTypeDef],
        "frequency": NotRequired[Literal["MONTHLY"]],
    },
)
ProjectTypeDef = TypedDict(
    "ProjectTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "defaultJobTimeoutMinutes": NotRequired[int],
        "created": NotRequired[datetime],
        "vpcConfig": NotRequired[VpcConfigOutputTypeDef],
    },
)
TestGridProjectTypeDef = TypedDict(
    "TestGridProjectTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "vpcConfig": NotRequired[TestGridVpcConfigOutputTypeDef],
        "created": NotRequired[datetime],
    },
)
GetAccountSettingsResultTypeDef = TypedDict(
    "GetAccountSettingsResultTypeDef",
    {
        "accountSettings": AccountSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDevicePoolResultTypeDef = TypedDict(
    "CreateDevicePoolResultTypeDef",
    {
        "devicePool": DevicePoolTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDevicePoolResultTypeDef = TypedDict(
    "GetDevicePoolResultTypeDef",
    {
        "devicePool": DevicePoolTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDevicePoolsResultTypeDef = TypedDict(
    "ListDevicePoolsResultTypeDef",
    {
        "devicePools": List[DevicePoolTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDevicePoolResultTypeDef = TypedDict(
    "UpdateDevicePoolResultTypeDef",
    {
        "devicePool": DevicePoolTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "manufacturer": NotRequired[str],
        "model": NotRequired[str],
        "modelId": NotRequired[str],
        "formFactor": NotRequired[DeviceFormFactorType],
        "platform": NotRequired[DevicePlatformType],
        "os": NotRequired[str],
        "cpu": NotRequired[CPUTypeDef],
        "resolution": NotRequired[ResolutionTypeDef],
        "heapSize": NotRequired[int],
        "memory": NotRequired[int],
        "image": NotRequired[str],
        "carrier": NotRequired[str],
        "radio": NotRequired[str],
        "remoteAccessEnabled": NotRequired[bool],
        "remoteDebugEnabled": NotRequired[bool],
        "fleetType": NotRequired[str],
        "fleetName": NotRequired[str],
        "instances": NotRequired[List[DeviceInstanceTypeDef]],
        "availability": NotRequired[DeviceAvailabilityType],
    },
)
GetDeviceInstanceResultTypeDef = TypedDict(
    "GetDeviceInstanceResultTypeDef",
    {
        "deviceInstance": DeviceInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDeviceInstancesResultTypeDef = TypedDict(
    "ListDeviceInstancesResultTypeDef",
    {
        "deviceInstances": List[DeviceInstanceTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDeviceInstanceResultTypeDef = TypedDict(
    "UpdateDeviceInstanceResultTypeDef",
    {
        "deviceInstance": DeviceInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ScheduleRunConfigurationTypeDef = TypedDict(
    "ScheduleRunConfigurationTypeDef",
    {
        "extraDataPackageArn": NotRequired[str],
        "networkProfileArn": NotRequired[str],
        "locale": NotRequired[str],
        "location": NotRequired[LocationTypeDef],
        "vpceConfigurationArns": NotRequired[Sequence[str]],
        "customerArtifactPaths": NotRequired[CustomerArtifactPathsUnionTypeDef],
        "radios": NotRequired[RadiosTypeDef],
        "auxiliaryApps": NotRequired[Sequence[str]],
        "billingMethod": NotRequired[BillingMethodType],
    },
)
RunTypeDef = TypedDict(
    "RunTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[TestTypeType],
        "platform": NotRequired[DevicePlatformType],
        "created": NotRequired[datetime],
        "status": NotRequired[ExecutionStatusType],
        "result": NotRequired[ExecutionResultType],
        "started": NotRequired[datetime],
        "stopped": NotRequired[datetime],
        "counters": NotRequired[CountersTypeDef],
        "message": NotRequired[str],
        "totalJobs": NotRequired[int],
        "completedJobs": NotRequired[int],
        "billingMethod": NotRequired[BillingMethodType],
        "deviceMinutes": NotRequired[DeviceMinutesTypeDef],
        "networkProfile": NotRequired[NetworkProfileTypeDef],
        "parsingResultUrl": NotRequired[str],
        "resultCode": NotRequired[ExecutionResultCodeType],
        "seed": NotRequired[int],
        "appUpload": NotRequired[str],
        "eventCount": NotRequired[int],
        "jobTimeoutMinutes": NotRequired[int],
        "devicePoolArn": NotRequired[str],
        "locale": NotRequired[str],
        "radios": NotRequired[RadiosTypeDef],
        "location": NotRequired[LocationTypeDef],
        "customerArtifactPaths": NotRequired[CustomerArtifactPathsOutputTypeDef],
        "webUrl": NotRequired[str],
        "skipAppResign": NotRequired[bool],
        "testSpecArn": NotRequired[str],
        "deviceSelectionResult": NotRequired[DeviceSelectionResultTypeDef],
        "vpcConfig": NotRequired[VpcConfigOutputTypeDef],
    },
)
DeviceSelectionConfigurationTypeDef = TypedDict(
    "DeviceSelectionConfigurationTypeDef",
    {
        "filters": Sequence[DeviceFilterUnionTypeDef],
        "maxDevices": int,
    },
)
ListDevicesRequestRequestTypeDef = TypedDict(
    "ListDevicesRequestRequestTypeDef",
    {
        "arn": NotRequired[str],
        "nextToken": NotRequired[str],
        "filters": NotRequired[Sequence[DeviceFilterUnionTypeDef]],
    },
)
GetSuiteResultTypeDef = TypedDict(
    "GetSuiteResultTypeDef",
    {
        "suite": SuiteTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSuitesResultTypeDef = TypedDict(
    "ListSuitesResultTypeDef",
    {
        "suites": List[SuiteTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTestResultTypeDef = TypedDict(
    "GetTestResultTypeDef",
    {
        "test": TestTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTestsResultTypeDef = TypedDict(
    "ListTestsResultTypeDef",
    {
        "tests": List[TestTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OfferingTypeDef = TypedDict(
    "OfferingTypeDef",
    {
        "id": NotRequired[str],
        "description": NotRequired[str],
        "type": NotRequired[Literal["RECURRING"]],
        "platform": NotRequired[DevicePlatformType],
        "recurringCharges": NotRequired[List[RecurringChargeTypeDef]],
    },
)
CreateProjectResultTypeDef = TypedDict(
    "CreateProjectResultTypeDef",
    {
        "project": ProjectTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetProjectResultTypeDef = TypedDict(
    "GetProjectResultTypeDef",
    {
        "project": ProjectTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListProjectsResultTypeDef = TypedDict(
    "ListProjectsResultTypeDef",
    {
        "projects": List[ProjectTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateProjectResultTypeDef = TypedDict(
    "UpdateProjectResultTypeDef",
    {
        "project": ProjectTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTestGridProjectResultTypeDef = TypedDict(
    "CreateTestGridProjectResultTypeDef",
    {
        "testGridProject": TestGridProjectTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTestGridProjectResultTypeDef = TypedDict(
    "GetTestGridProjectResultTypeDef",
    {
        "testGridProject": TestGridProjectTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTestGridProjectsResultTypeDef = TypedDict(
    "ListTestGridProjectsResultTypeDef",
    {
        "testGridProjects": List[TestGridProjectTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTestGridProjectResultTypeDef = TypedDict(
    "UpdateTestGridProjectResultTypeDef",
    {
        "testGridProject": TestGridProjectTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DevicePoolCompatibilityResultTypeDef = TypedDict(
    "DevicePoolCompatibilityResultTypeDef",
    {
        "device": NotRequired[DeviceTypeDef],
        "compatible": NotRequired[bool],
        "incompatibilityMessages": NotRequired[List[IncompatibilityMessageTypeDef]],
    },
)
GetDeviceResultTypeDef = TypedDict(
    "GetDeviceResultTypeDef",
    {
        "device": DeviceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[TestTypeType],
        "created": NotRequired[datetime],
        "status": NotRequired[ExecutionStatusType],
        "result": NotRequired[ExecutionResultType],
        "started": NotRequired[datetime],
        "stopped": NotRequired[datetime],
        "counters": NotRequired[CountersTypeDef],
        "message": NotRequired[str],
        "device": NotRequired[DeviceTypeDef],
        "instanceArn": NotRequired[str],
        "deviceMinutes": NotRequired[DeviceMinutesTypeDef],
        "videoEndpoint": NotRequired[str],
        "videoCapture": NotRequired[bool],
    },
)
ListDevicesResultTypeDef = TypedDict(
    "ListDevicesResultTypeDef",
    {
        "devices": List[DeviceTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProblemTypeDef = TypedDict(
    "ProblemTypeDef",
    {
        "run": NotRequired[ProblemDetailTypeDef],
        "job": NotRequired[ProblemDetailTypeDef],
        "suite": NotRequired[ProblemDetailTypeDef],
        "test": NotRequired[ProblemDetailTypeDef],
        "device": NotRequired[DeviceTypeDef],
        "result": NotRequired[ExecutionResultType],
        "message": NotRequired[str],
    },
)
RemoteAccessSessionTypeDef = TypedDict(
    "RemoteAccessSessionTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "created": NotRequired[datetime],
        "status": NotRequired[ExecutionStatusType],
        "result": NotRequired[ExecutionResultType],
        "message": NotRequired[str],
        "started": NotRequired[datetime],
        "stopped": NotRequired[datetime],
        "device": NotRequired[DeviceTypeDef],
        "instanceArn": NotRequired[str],
        "remoteDebugEnabled": NotRequired[bool],
        "remoteRecordEnabled": NotRequired[bool],
        "remoteRecordAppArn": NotRequired[str],
        "hostAddress": NotRequired[str],
        "clientId": NotRequired[str],
        "billingMethod": NotRequired[BillingMethodType],
        "deviceMinutes": NotRequired[DeviceMinutesTypeDef],
        "endpoint": NotRequired[str],
        "deviceUdid": NotRequired[str],
        "interactionMode": NotRequired[InteractionModeType],
        "skipAppResign": NotRequired[bool],
        "vpcConfig": NotRequired[VpcConfigOutputTypeDef],
    },
)
GetDevicePoolCompatibilityRequestRequestTypeDef = TypedDict(
    "GetDevicePoolCompatibilityRequestRequestTypeDef",
    {
        "devicePoolArn": str,
        "appArn": NotRequired[str],
        "testType": NotRequired[TestTypeType],
        "test": NotRequired[ScheduleRunTestTypeDef],
        "configuration": NotRequired[ScheduleRunConfigurationTypeDef],
    },
)
GetRunResultTypeDef = TypedDict(
    "GetRunResultTypeDef",
    {
        "run": RunTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRunsResultTypeDef = TypedDict(
    "ListRunsResultTypeDef",
    {
        "runs": List[RunTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ScheduleRunResultTypeDef = TypedDict(
    "ScheduleRunResultTypeDef",
    {
        "run": RunTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopRunResultTypeDef = TypedDict(
    "StopRunResultTypeDef",
    {
        "run": RunTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ScheduleRunRequestRequestTypeDef = TypedDict(
    "ScheduleRunRequestRequestTypeDef",
    {
        "projectArn": str,
        "test": ScheduleRunTestTypeDef,
        "appArn": NotRequired[str],
        "devicePoolArn": NotRequired[str],
        "deviceSelectionConfiguration": NotRequired[DeviceSelectionConfigurationTypeDef],
        "name": NotRequired[str],
        "configuration": NotRequired[ScheduleRunConfigurationTypeDef],
        "executionConfiguration": NotRequired[ExecutionConfigurationTypeDef],
    },
)
ListOfferingsResultTypeDef = TypedDict(
    "ListOfferingsResultTypeDef",
    {
        "offerings": List[OfferingTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OfferingStatusTypeDef = TypedDict(
    "OfferingStatusTypeDef",
    {
        "type": NotRequired[OfferingTransactionTypeType],
        "offering": NotRequired[OfferingTypeDef],
        "quantity": NotRequired[int],
        "effectiveOn": NotRequired[datetime],
    },
)
GetDevicePoolCompatibilityResultTypeDef = TypedDict(
    "GetDevicePoolCompatibilityResultTypeDef",
    {
        "compatibleDevices": List[DevicePoolCompatibilityResultTypeDef],
        "incompatibleDevices": List[DevicePoolCompatibilityResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetJobResultTypeDef = TypedDict(
    "GetJobResultTypeDef",
    {
        "job": JobTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListJobsResultTypeDef = TypedDict(
    "ListJobsResultTypeDef",
    {
        "jobs": List[JobTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopJobResultTypeDef = TypedDict(
    "StopJobResultTypeDef",
    {
        "job": JobTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UniqueProblemTypeDef = TypedDict(
    "UniqueProblemTypeDef",
    {
        "message": NotRequired[str],
        "problems": NotRequired[List[ProblemTypeDef]],
    },
)
CreateRemoteAccessSessionResultTypeDef = TypedDict(
    "CreateRemoteAccessSessionResultTypeDef",
    {
        "remoteAccessSession": RemoteAccessSessionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRemoteAccessSessionResultTypeDef = TypedDict(
    "GetRemoteAccessSessionResultTypeDef",
    {
        "remoteAccessSession": RemoteAccessSessionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRemoteAccessSessionsResultTypeDef = TypedDict(
    "ListRemoteAccessSessionsResultTypeDef",
    {
        "remoteAccessSessions": List[RemoteAccessSessionTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopRemoteAccessSessionResultTypeDef = TypedDict(
    "StopRemoteAccessSessionResultTypeDef",
    {
        "remoteAccessSession": RemoteAccessSessionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetOfferingStatusResultTypeDef = TypedDict(
    "GetOfferingStatusResultTypeDef",
    {
        "current": Dict[str, OfferingStatusTypeDef],
        "nextPeriod": Dict[str, OfferingStatusTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OfferingTransactionTypeDef = TypedDict(
    "OfferingTransactionTypeDef",
    {
        "offeringStatus": NotRequired[OfferingStatusTypeDef],
        "transactionId": NotRequired[str],
        "offeringPromotionId": NotRequired[str],
        "createdOn": NotRequired[datetime],
        "cost": NotRequired[MonetaryAmountTypeDef],
    },
)
ListUniqueProblemsResultTypeDef = TypedDict(
    "ListUniqueProblemsResultTypeDef",
    {
        "uniqueProblems": Dict[ExecutionResultType, List[UniqueProblemTypeDef]],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListOfferingTransactionsResultTypeDef = TypedDict(
    "ListOfferingTransactionsResultTypeDef",
    {
        "offeringTransactions": List[OfferingTransactionTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PurchaseOfferingResultTypeDef = TypedDict(
    "PurchaseOfferingResultTypeDef",
    {
        "offeringTransaction": OfferingTransactionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RenewOfferingResultTypeDef = TypedDict(
    "RenewOfferingResultTypeDef",
    {
        "offeringTransaction": OfferingTransactionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
