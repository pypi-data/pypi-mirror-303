"""
Type annotations for connectcampaigns service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcampaigns/type_defs/)

Usage::

    ```python
    from mypy_boto3_connectcampaigns.type_defs import AgentlessDialerConfigTypeDef

    data: AgentlessDialerConfigTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    CampaignStateType,
    FailureCodeType,
    GetCampaignStateBatchFailureCodeType,
    InstanceOnboardingJobFailureCodeType,
    InstanceOnboardingJobStatusCodeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AgentlessDialerConfigTypeDef",
    "AnswerMachineDetectionConfigTypeDef",
    "InstanceIdFilterTypeDef",
    "CampaignSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "DeleteCampaignRequestRequestTypeDef",
    "DeleteConnectInstanceConfigRequestRequestTypeDef",
    "DeleteInstanceOnboardingJobRequestRequestTypeDef",
    "DescribeCampaignRequestRequestTypeDef",
    "TimestampTypeDef",
    "PredictiveDialerConfigTypeDef",
    "ProgressiveDialerConfigTypeDef",
    "EncryptionConfigTypeDef",
    "FailedCampaignStateResponseTypeDef",
    "FailedRequestTypeDef",
    "GetCampaignStateBatchRequestRequestTypeDef",
    "SuccessfulCampaignStateResponseTypeDef",
    "GetCampaignStateRequestRequestTypeDef",
    "GetConnectInstanceConfigRequestRequestTypeDef",
    "GetInstanceOnboardingJobStatusRequestRequestTypeDef",
    "InstanceOnboardingJobStatusTypeDef",
    "PaginatorConfigTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "PauseCampaignRequestRequestTypeDef",
    "SuccessfulRequestTypeDef",
    "ResumeCampaignRequestRequestTypeDef",
    "StartCampaignRequestRequestTypeDef",
    "StopCampaignRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateCampaignNameRequestRequestTypeDef",
    "OutboundCallConfigTypeDef",
    "UpdateCampaignOutboundCallConfigRequestRequestTypeDef",
    "CampaignFiltersTypeDef",
    "CreateCampaignResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetCampaignStateResponseTypeDef",
    "ListCampaignsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "DialRequestTypeDef",
    "DialerConfigTypeDef",
    "InstanceConfigTypeDef",
    "StartInstanceOnboardingJobRequestRequestTypeDef",
    "GetCampaignStateBatchResponseTypeDef",
    "GetInstanceOnboardingJobStatusResponseTypeDef",
    "StartInstanceOnboardingJobResponseTypeDef",
    "PutDialRequestBatchResponseTypeDef",
    "ListCampaignsRequestListCampaignsPaginateTypeDef",
    "ListCampaignsRequestRequestTypeDef",
    "PutDialRequestBatchRequestRequestTypeDef",
    "CampaignTypeDef",
    "CreateCampaignRequestRequestTypeDef",
    "UpdateCampaignDialerConfigRequestRequestTypeDef",
    "GetConnectInstanceConfigResponseTypeDef",
    "DescribeCampaignResponseTypeDef",
)

AgentlessDialerConfigTypeDef = TypedDict(
    "AgentlessDialerConfigTypeDef",
    {
        "dialingCapacity": NotRequired[float],
    },
)
AnswerMachineDetectionConfigTypeDef = TypedDict(
    "AnswerMachineDetectionConfigTypeDef",
    {
        "enableAnswerMachineDetection": bool,
        "awaitAnswerMachinePrompt": NotRequired[bool],
    },
)
InstanceIdFilterTypeDef = TypedDict(
    "InstanceIdFilterTypeDef",
    {
        "value": str,
        "operator": Literal["Eq"],
    },
)
CampaignSummaryTypeDef = TypedDict(
    "CampaignSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "connectInstanceId": str,
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
DeleteCampaignRequestRequestTypeDef = TypedDict(
    "DeleteCampaignRequestRequestTypeDef",
    {
        "id": str,
    },
)
DeleteConnectInstanceConfigRequestRequestTypeDef = TypedDict(
    "DeleteConnectInstanceConfigRequestRequestTypeDef",
    {
        "connectInstanceId": str,
    },
)
DeleteInstanceOnboardingJobRequestRequestTypeDef = TypedDict(
    "DeleteInstanceOnboardingJobRequestRequestTypeDef",
    {
        "connectInstanceId": str,
    },
)
DescribeCampaignRequestRequestTypeDef = TypedDict(
    "DescribeCampaignRequestRequestTypeDef",
    {
        "id": str,
    },
)
TimestampTypeDef = Union[datetime, str]
PredictiveDialerConfigTypeDef = TypedDict(
    "PredictiveDialerConfigTypeDef",
    {
        "bandwidthAllocation": float,
        "dialingCapacity": NotRequired[float],
    },
)
ProgressiveDialerConfigTypeDef = TypedDict(
    "ProgressiveDialerConfigTypeDef",
    {
        "bandwidthAllocation": float,
        "dialingCapacity": NotRequired[float],
    },
)
EncryptionConfigTypeDef = TypedDict(
    "EncryptionConfigTypeDef",
    {
        "enabled": bool,
        "encryptionType": NotRequired[Literal["KMS"]],
        "keyArn": NotRequired[str],
    },
)
FailedCampaignStateResponseTypeDef = TypedDict(
    "FailedCampaignStateResponseTypeDef",
    {
        "campaignId": NotRequired[str],
        "failureCode": NotRequired[GetCampaignStateBatchFailureCodeType],
    },
)
FailedRequestTypeDef = TypedDict(
    "FailedRequestTypeDef",
    {
        "clientToken": NotRequired[str],
        "id": NotRequired[str],
        "failureCode": NotRequired[FailureCodeType],
    },
)
GetCampaignStateBatchRequestRequestTypeDef = TypedDict(
    "GetCampaignStateBatchRequestRequestTypeDef",
    {
        "campaignIds": Sequence[str],
    },
)
SuccessfulCampaignStateResponseTypeDef = TypedDict(
    "SuccessfulCampaignStateResponseTypeDef",
    {
        "campaignId": NotRequired[str],
        "state": NotRequired[CampaignStateType],
    },
)
GetCampaignStateRequestRequestTypeDef = TypedDict(
    "GetCampaignStateRequestRequestTypeDef",
    {
        "id": str,
    },
)
GetConnectInstanceConfigRequestRequestTypeDef = TypedDict(
    "GetConnectInstanceConfigRequestRequestTypeDef",
    {
        "connectInstanceId": str,
    },
)
GetInstanceOnboardingJobStatusRequestRequestTypeDef = TypedDict(
    "GetInstanceOnboardingJobStatusRequestRequestTypeDef",
    {
        "connectInstanceId": str,
    },
)
InstanceOnboardingJobStatusTypeDef = TypedDict(
    "InstanceOnboardingJobStatusTypeDef",
    {
        "connectInstanceId": str,
        "status": InstanceOnboardingJobStatusCodeType,
        "failureCode": NotRequired[InstanceOnboardingJobFailureCodeType],
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
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "arn": str,
    },
)
PauseCampaignRequestRequestTypeDef = TypedDict(
    "PauseCampaignRequestRequestTypeDef",
    {
        "id": str,
    },
)
SuccessfulRequestTypeDef = TypedDict(
    "SuccessfulRequestTypeDef",
    {
        "clientToken": NotRequired[str],
        "id": NotRequired[str],
    },
)
ResumeCampaignRequestRequestTypeDef = TypedDict(
    "ResumeCampaignRequestRequestTypeDef",
    {
        "id": str,
    },
)
StartCampaignRequestRequestTypeDef = TypedDict(
    "StartCampaignRequestRequestTypeDef",
    {
        "id": str,
    },
)
StopCampaignRequestRequestTypeDef = TypedDict(
    "StopCampaignRequestRequestTypeDef",
    {
        "id": str,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "arn": str,
        "tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "arn": str,
        "tagKeys": Sequence[str],
    },
)
UpdateCampaignNameRequestRequestTypeDef = TypedDict(
    "UpdateCampaignNameRequestRequestTypeDef",
    {
        "id": str,
        "name": str,
    },
)
OutboundCallConfigTypeDef = TypedDict(
    "OutboundCallConfigTypeDef",
    {
        "connectContactFlowId": str,
        "connectSourcePhoneNumber": NotRequired[str],
        "connectQueueId": NotRequired[str],
        "answerMachineDetectionConfig": NotRequired[AnswerMachineDetectionConfigTypeDef],
    },
)
UpdateCampaignOutboundCallConfigRequestRequestTypeDef = TypedDict(
    "UpdateCampaignOutboundCallConfigRequestRequestTypeDef",
    {
        "id": str,
        "connectContactFlowId": NotRequired[str],
        "connectSourcePhoneNumber": NotRequired[str],
        "answerMachineDetectionConfig": NotRequired[AnswerMachineDetectionConfigTypeDef],
    },
)
CampaignFiltersTypeDef = TypedDict(
    "CampaignFiltersTypeDef",
    {
        "instanceIdFilter": NotRequired[InstanceIdFilterTypeDef],
    },
)
CreateCampaignResponseTypeDef = TypedDict(
    "CreateCampaignResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCampaignStateResponseTypeDef = TypedDict(
    "GetCampaignStateResponseTypeDef",
    {
        "state": CampaignStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCampaignsResponseTypeDef = TypedDict(
    "ListCampaignsResponseTypeDef",
    {
        "nextToken": str,
        "campaignSummaryList": List[CampaignSummaryTypeDef],
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
DialRequestTypeDef = TypedDict(
    "DialRequestTypeDef",
    {
        "clientToken": str,
        "phoneNumber": str,
        "expirationTime": TimestampTypeDef,
        "attributes": Mapping[str, str],
    },
)
DialerConfigTypeDef = TypedDict(
    "DialerConfigTypeDef",
    {
        "progressiveDialerConfig": NotRequired[ProgressiveDialerConfigTypeDef],
        "predictiveDialerConfig": NotRequired[PredictiveDialerConfigTypeDef],
        "agentlessDialerConfig": NotRequired[AgentlessDialerConfigTypeDef],
    },
)
InstanceConfigTypeDef = TypedDict(
    "InstanceConfigTypeDef",
    {
        "connectInstanceId": str,
        "serviceLinkedRoleArn": str,
        "encryptionConfig": EncryptionConfigTypeDef,
    },
)
StartInstanceOnboardingJobRequestRequestTypeDef = TypedDict(
    "StartInstanceOnboardingJobRequestRequestTypeDef",
    {
        "connectInstanceId": str,
        "encryptionConfig": EncryptionConfigTypeDef,
    },
)
GetCampaignStateBatchResponseTypeDef = TypedDict(
    "GetCampaignStateBatchResponseTypeDef",
    {
        "successfulRequests": List[SuccessfulCampaignStateResponseTypeDef],
        "failedRequests": List[FailedCampaignStateResponseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetInstanceOnboardingJobStatusResponseTypeDef = TypedDict(
    "GetInstanceOnboardingJobStatusResponseTypeDef",
    {
        "connectInstanceOnboardingJobStatus": InstanceOnboardingJobStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartInstanceOnboardingJobResponseTypeDef = TypedDict(
    "StartInstanceOnboardingJobResponseTypeDef",
    {
        "connectInstanceOnboardingJobStatus": InstanceOnboardingJobStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutDialRequestBatchResponseTypeDef = TypedDict(
    "PutDialRequestBatchResponseTypeDef",
    {
        "successfulRequests": List[SuccessfulRequestTypeDef],
        "failedRequests": List[FailedRequestTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCampaignsRequestListCampaignsPaginateTypeDef = TypedDict(
    "ListCampaignsRequestListCampaignsPaginateTypeDef",
    {
        "filters": NotRequired[CampaignFiltersTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCampaignsRequestRequestTypeDef = TypedDict(
    "ListCampaignsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "filters": NotRequired[CampaignFiltersTypeDef],
    },
)
PutDialRequestBatchRequestRequestTypeDef = TypedDict(
    "PutDialRequestBatchRequestRequestTypeDef",
    {
        "id": str,
        "dialRequests": Sequence[DialRequestTypeDef],
    },
)
CampaignTypeDef = TypedDict(
    "CampaignTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "connectInstanceId": str,
        "dialerConfig": DialerConfigTypeDef,
        "outboundCallConfig": OutboundCallConfigTypeDef,
        "tags": NotRequired[Dict[str, str]],
    },
)
CreateCampaignRequestRequestTypeDef = TypedDict(
    "CreateCampaignRequestRequestTypeDef",
    {
        "name": str,
        "connectInstanceId": str,
        "dialerConfig": DialerConfigTypeDef,
        "outboundCallConfig": OutboundCallConfigTypeDef,
        "tags": NotRequired[Mapping[str, str]],
    },
)
UpdateCampaignDialerConfigRequestRequestTypeDef = TypedDict(
    "UpdateCampaignDialerConfigRequestRequestTypeDef",
    {
        "id": str,
        "dialerConfig": DialerConfigTypeDef,
    },
)
GetConnectInstanceConfigResponseTypeDef = TypedDict(
    "GetConnectInstanceConfigResponseTypeDef",
    {
        "connectInstanceConfig": InstanceConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeCampaignResponseTypeDef = TypedDict(
    "DescribeCampaignResponseTypeDef",
    {
        "campaign": CampaignTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
