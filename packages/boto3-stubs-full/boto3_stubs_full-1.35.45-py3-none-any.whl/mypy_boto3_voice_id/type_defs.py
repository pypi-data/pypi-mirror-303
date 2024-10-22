"""
Type annotations for voice-id service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_voice_id/type_defs/)

Usage::

    ```python
    from mypy_boto3_voice_id.type_defs import AssociateFraudsterRequestRequestTypeDef

    data: AssociateFraudsterRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    AuthenticationDecisionType,
    DomainStatusType,
    DuplicateRegistrationActionType,
    ExistingEnrollmentActionType,
    FraudDetectionActionType,
    FraudDetectionDecisionType,
    FraudDetectionReasonType,
    FraudsterRegistrationJobStatusType,
    ServerSideEncryptionUpdateStatusType,
    SpeakerEnrollmentJobStatusType,
    SpeakerStatusType,
    StreamingStatusType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "AssociateFraudsterRequestRequestTypeDef",
    "FraudsterTypeDef",
    "ResponseMetadataTypeDef",
    "AuthenticationConfigurationTypeDef",
    "ServerSideEncryptionConfigurationTypeDef",
    "TagTypeDef",
    "CreateWatchlistRequestRequestTypeDef",
    "WatchlistTypeDef",
    "DeleteDomainRequestRequestTypeDef",
    "DeleteFraudsterRequestRequestTypeDef",
    "DeleteSpeakerRequestRequestTypeDef",
    "DeleteWatchlistRequestRequestTypeDef",
    "DescribeDomainRequestRequestTypeDef",
    "DescribeFraudsterRegistrationJobRequestRequestTypeDef",
    "DescribeFraudsterRequestRequestTypeDef",
    "DescribeSpeakerEnrollmentJobRequestRequestTypeDef",
    "DescribeSpeakerRequestRequestTypeDef",
    "SpeakerTypeDef",
    "DescribeWatchlistRequestRequestTypeDef",
    "DisassociateFraudsterRequestRequestTypeDef",
    "ServerSideEncryptionUpdateDetailsTypeDef",
    "WatchlistDetailsTypeDef",
    "EnrollmentJobFraudDetectionConfigOutputTypeDef",
    "EnrollmentJobFraudDetectionConfigTypeDef",
    "EvaluateSessionRequestRequestTypeDef",
    "FailureDetailsTypeDef",
    "FraudDetectionConfigurationTypeDef",
    "KnownFraudsterRiskTypeDef",
    "VoiceSpoofingRiskTypeDef",
    "JobProgressTypeDef",
    "InputDataConfigTypeDef",
    "OutputDataConfigTypeDef",
    "RegistrationConfigOutputTypeDef",
    "FraudsterSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "ListDomainsRequestRequestTypeDef",
    "ListFraudsterRegistrationJobsRequestRequestTypeDef",
    "ListFraudstersRequestRequestTypeDef",
    "ListSpeakerEnrollmentJobsRequestRequestTypeDef",
    "ListSpeakersRequestRequestTypeDef",
    "SpeakerSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListWatchlistsRequestRequestTypeDef",
    "WatchlistSummaryTypeDef",
    "OptOutSpeakerRequestRequestTypeDef",
    "RegistrationConfigTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateWatchlistRequestRequestTypeDef",
    "AssociateFraudsterResponseTypeDef",
    "DescribeFraudsterResponseTypeDef",
    "DisassociateFraudsterResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "AuthenticationResultTypeDef",
    "UpdateDomainRequestRequestTypeDef",
    "CreateDomainRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateWatchlistResponseTypeDef",
    "DescribeWatchlistResponseTypeDef",
    "UpdateWatchlistResponseTypeDef",
    "DescribeSpeakerResponseTypeDef",
    "OptOutSpeakerResponseTypeDef",
    "DomainSummaryTypeDef",
    "DomainTypeDef",
    "EnrollmentConfigOutputTypeDef",
    "EnrollmentJobFraudDetectionConfigUnionTypeDef",
    "FraudRiskDetailsTypeDef",
    "FraudsterRegistrationJobSummaryTypeDef",
    "SpeakerEnrollmentJobSummaryTypeDef",
    "FraudsterRegistrationJobTypeDef",
    "ListFraudstersResponseTypeDef",
    "ListDomainsRequestListDomainsPaginateTypeDef",
    "ListFraudsterRegistrationJobsRequestListFraudsterRegistrationJobsPaginateTypeDef",
    "ListFraudstersRequestListFraudstersPaginateTypeDef",
    "ListSpeakerEnrollmentJobsRequestListSpeakerEnrollmentJobsPaginateTypeDef",
    "ListSpeakersRequestListSpeakersPaginateTypeDef",
    "ListWatchlistsRequestListWatchlistsPaginateTypeDef",
    "ListSpeakersResponseTypeDef",
    "ListWatchlistsResponseTypeDef",
    "StartFraudsterRegistrationJobRequestRequestTypeDef",
    "ListDomainsResponseTypeDef",
    "CreateDomainResponseTypeDef",
    "DescribeDomainResponseTypeDef",
    "UpdateDomainResponseTypeDef",
    "SpeakerEnrollmentJobTypeDef",
    "EnrollmentConfigTypeDef",
    "FraudDetectionResultTypeDef",
    "ListFraudsterRegistrationJobsResponseTypeDef",
    "ListSpeakerEnrollmentJobsResponseTypeDef",
    "DescribeFraudsterRegistrationJobResponseTypeDef",
    "StartFraudsterRegistrationJobResponseTypeDef",
    "DescribeSpeakerEnrollmentJobResponseTypeDef",
    "StartSpeakerEnrollmentJobResponseTypeDef",
    "StartSpeakerEnrollmentJobRequestRequestTypeDef",
    "EvaluateSessionResponseTypeDef",
)

AssociateFraudsterRequestRequestTypeDef = TypedDict(
    "AssociateFraudsterRequestRequestTypeDef",
    {
        "DomainId": str,
        "FraudsterId": str,
        "WatchlistId": str,
    },
)
FraudsterTypeDef = TypedDict(
    "FraudsterTypeDef",
    {
        "CreatedAt": NotRequired[datetime],
        "DomainId": NotRequired[str],
        "GeneratedFraudsterId": NotRequired[str],
        "WatchlistIds": NotRequired[List[str]],
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
AuthenticationConfigurationTypeDef = TypedDict(
    "AuthenticationConfigurationTypeDef",
    {
        "AcceptanceThreshold": int,
    },
)
ServerSideEncryptionConfigurationTypeDef = TypedDict(
    "ServerSideEncryptionConfigurationTypeDef",
    {
        "KmsKeyId": str,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
CreateWatchlistRequestRequestTypeDef = TypedDict(
    "CreateWatchlistRequestRequestTypeDef",
    {
        "DomainId": str,
        "Name": str,
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
    },
)
WatchlistTypeDef = TypedDict(
    "WatchlistTypeDef",
    {
        "CreatedAt": NotRequired[datetime],
        "DefaultWatchlist": NotRequired[bool],
        "Description": NotRequired[str],
        "DomainId": NotRequired[str],
        "Name": NotRequired[str],
        "UpdatedAt": NotRequired[datetime],
        "WatchlistId": NotRequired[str],
    },
)
DeleteDomainRequestRequestTypeDef = TypedDict(
    "DeleteDomainRequestRequestTypeDef",
    {
        "DomainId": str,
    },
)
DeleteFraudsterRequestRequestTypeDef = TypedDict(
    "DeleteFraudsterRequestRequestTypeDef",
    {
        "DomainId": str,
        "FraudsterId": str,
    },
)
DeleteSpeakerRequestRequestTypeDef = TypedDict(
    "DeleteSpeakerRequestRequestTypeDef",
    {
        "DomainId": str,
        "SpeakerId": str,
    },
)
DeleteWatchlistRequestRequestTypeDef = TypedDict(
    "DeleteWatchlistRequestRequestTypeDef",
    {
        "DomainId": str,
        "WatchlistId": str,
    },
)
DescribeDomainRequestRequestTypeDef = TypedDict(
    "DescribeDomainRequestRequestTypeDef",
    {
        "DomainId": str,
    },
)
DescribeFraudsterRegistrationJobRequestRequestTypeDef = TypedDict(
    "DescribeFraudsterRegistrationJobRequestRequestTypeDef",
    {
        "DomainId": str,
        "JobId": str,
    },
)
DescribeFraudsterRequestRequestTypeDef = TypedDict(
    "DescribeFraudsterRequestRequestTypeDef",
    {
        "DomainId": str,
        "FraudsterId": str,
    },
)
DescribeSpeakerEnrollmentJobRequestRequestTypeDef = TypedDict(
    "DescribeSpeakerEnrollmentJobRequestRequestTypeDef",
    {
        "DomainId": str,
        "JobId": str,
    },
)
DescribeSpeakerRequestRequestTypeDef = TypedDict(
    "DescribeSpeakerRequestRequestTypeDef",
    {
        "DomainId": str,
        "SpeakerId": str,
    },
)
SpeakerTypeDef = TypedDict(
    "SpeakerTypeDef",
    {
        "CreatedAt": NotRequired[datetime],
        "CustomerSpeakerId": NotRequired[str],
        "DomainId": NotRequired[str],
        "GeneratedSpeakerId": NotRequired[str],
        "LastAccessedAt": NotRequired[datetime],
        "Status": NotRequired[SpeakerStatusType],
        "UpdatedAt": NotRequired[datetime],
    },
)
DescribeWatchlistRequestRequestTypeDef = TypedDict(
    "DescribeWatchlistRequestRequestTypeDef",
    {
        "DomainId": str,
        "WatchlistId": str,
    },
)
DisassociateFraudsterRequestRequestTypeDef = TypedDict(
    "DisassociateFraudsterRequestRequestTypeDef",
    {
        "DomainId": str,
        "FraudsterId": str,
        "WatchlistId": str,
    },
)
ServerSideEncryptionUpdateDetailsTypeDef = TypedDict(
    "ServerSideEncryptionUpdateDetailsTypeDef",
    {
        "Message": NotRequired[str],
        "OldKmsKeyId": NotRequired[str],
        "UpdateStatus": NotRequired[ServerSideEncryptionUpdateStatusType],
    },
)
WatchlistDetailsTypeDef = TypedDict(
    "WatchlistDetailsTypeDef",
    {
        "DefaultWatchlistId": str,
    },
)
EnrollmentJobFraudDetectionConfigOutputTypeDef = TypedDict(
    "EnrollmentJobFraudDetectionConfigOutputTypeDef",
    {
        "FraudDetectionAction": NotRequired[FraudDetectionActionType],
        "RiskThreshold": NotRequired[int],
        "WatchlistIds": NotRequired[List[str]],
    },
)
EnrollmentJobFraudDetectionConfigTypeDef = TypedDict(
    "EnrollmentJobFraudDetectionConfigTypeDef",
    {
        "FraudDetectionAction": NotRequired[FraudDetectionActionType],
        "RiskThreshold": NotRequired[int],
        "WatchlistIds": NotRequired[Sequence[str]],
    },
)
EvaluateSessionRequestRequestTypeDef = TypedDict(
    "EvaluateSessionRequestRequestTypeDef",
    {
        "DomainId": str,
        "SessionNameOrId": str,
    },
)
FailureDetailsTypeDef = TypedDict(
    "FailureDetailsTypeDef",
    {
        "Message": NotRequired[str],
        "StatusCode": NotRequired[int],
    },
)
FraudDetectionConfigurationTypeDef = TypedDict(
    "FraudDetectionConfigurationTypeDef",
    {
        "RiskThreshold": NotRequired[int],
        "WatchlistId": NotRequired[str],
    },
)
KnownFraudsterRiskTypeDef = TypedDict(
    "KnownFraudsterRiskTypeDef",
    {
        "RiskScore": int,
        "GeneratedFraudsterId": NotRequired[str],
    },
)
VoiceSpoofingRiskTypeDef = TypedDict(
    "VoiceSpoofingRiskTypeDef",
    {
        "RiskScore": int,
    },
)
JobProgressTypeDef = TypedDict(
    "JobProgressTypeDef",
    {
        "PercentComplete": NotRequired[int],
    },
)
InputDataConfigTypeDef = TypedDict(
    "InputDataConfigTypeDef",
    {
        "S3Uri": str,
    },
)
OutputDataConfigTypeDef = TypedDict(
    "OutputDataConfigTypeDef",
    {
        "S3Uri": str,
        "KmsKeyId": NotRequired[str],
    },
)
RegistrationConfigOutputTypeDef = TypedDict(
    "RegistrationConfigOutputTypeDef",
    {
        "DuplicateRegistrationAction": NotRequired[DuplicateRegistrationActionType],
        "FraudsterSimilarityThreshold": NotRequired[int],
        "WatchlistIds": NotRequired[List[str]],
    },
)
FraudsterSummaryTypeDef = TypedDict(
    "FraudsterSummaryTypeDef",
    {
        "CreatedAt": NotRequired[datetime],
        "DomainId": NotRequired[str],
        "GeneratedFraudsterId": NotRequired[str],
        "WatchlistIds": NotRequired[List[str]],
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
ListDomainsRequestRequestTypeDef = TypedDict(
    "ListDomainsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListFraudsterRegistrationJobsRequestRequestTypeDef = TypedDict(
    "ListFraudsterRegistrationJobsRequestRequestTypeDef",
    {
        "DomainId": str,
        "JobStatus": NotRequired[FraudsterRegistrationJobStatusType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListFraudstersRequestRequestTypeDef = TypedDict(
    "ListFraudstersRequestRequestTypeDef",
    {
        "DomainId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "WatchlistId": NotRequired[str],
    },
)
ListSpeakerEnrollmentJobsRequestRequestTypeDef = TypedDict(
    "ListSpeakerEnrollmentJobsRequestRequestTypeDef",
    {
        "DomainId": str,
        "JobStatus": NotRequired[SpeakerEnrollmentJobStatusType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListSpeakersRequestRequestTypeDef = TypedDict(
    "ListSpeakersRequestRequestTypeDef",
    {
        "DomainId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
SpeakerSummaryTypeDef = TypedDict(
    "SpeakerSummaryTypeDef",
    {
        "CreatedAt": NotRequired[datetime],
        "CustomerSpeakerId": NotRequired[str],
        "DomainId": NotRequired[str],
        "GeneratedSpeakerId": NotRequired[str],
        "LastAccessedAt": NotRequired[datetime],
        "Status": NotRequired[SpeakerStatusType],
        "UpdatedAt": NotRequired[datetime],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
ListWatchlistsRequestRequestTypeDef = TypedDict(
    "ListWatchlistsRequestRequestTypeDef",
    {
        "DomainId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
WatchlistSummaryTypeDef = TypedDict(
    "WatchlistSummaryTypeDef",
    {
        "CreatedAt": NotRequired[datetime],
        "DefaultWatchlist": NotRequired[bool],
        "Description": NotRequired[str],
        "DomainId": NotRequired[str],
        "Name": NotRequired[str],
        "UpdatedAt": NotRequired[datetime],
        "WatchlistId": NotRequired[str],
    },
)
OptOutSpeakerRequestRequestTypeDef = TypedDict(
    "OptOutSpeakerRequestRequestTypeDef",
    {
        "DomainId": str,
        "SpeakerId": str,
    },
)
RegistrationConfigTypeDef = TypedDict(
    "RegistrationConfigTypeDef",
    {
        "DuplicateRegistrationAction": NotRequired[DuplicateRegistrationActionType],
        "FraudsterSimilarityThreshold": NotRequired[int],
        "WatchlistIds": NotRequired[Sequence[str]],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateWatchlistRequestRequestTypeDef = TypedDict(
    "UpdateWatchlistRequestRequestTypeDef",
    {
        "DomainId": str,
        "WatchlistId": str,
        "Description": NotRequired[str],
        "Name": NotRequired[str],
    },
)
AssociateFraudsterResponseTypeDef = TypedDict(
    "AssociateFraudsterResponseTypeDef",
    {
        "Fraudster": FraudsterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeFraudsterResponseTypeDef = TypedDict(
    "DescribeFraudsterResponseTypeDef",
    {
        "Fraudster": FraudsterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateFraudsterResponseTypeDef = TypedDict(
    "DisassociateFraudsterResponseTypeDef",
    {
        "Fraudster": FraudsterTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AuthenticationResultTypeDef = TypedDict(
    "AuthenticationResultTypeDef",
    {
        "AudioAggregationEndedAt": NotRequired[datetime],
        "AudioAggregationStartedAt": NotRequired[datetime],
        "AuthenticationResultId": NotRequired[str],
        "Configuration": NotRequired[AuthenticationConfigurationTypeDef],
        "CustomerSpeakerId": NotRequired[str],
        "Decision": NotRequired[AuthenticationDecisionType],
        "GeneratedSpeakerId": NotRequired[str],
        "Score": NotRequired[int],
    },
)
UpdateDomainRequestRequestTypeDef = TypedDict(
    "UpdateDomainRequestRequestTypeDef",
    {
        "DomainId": str,
        "Name": str,
        "ServerSideEncryptionConfiguration": ServerSideEncryptionConfigurationTypeDef,
        "Description": NotRequired[str],
    },
)
CreateDomainRequestRequestTypeDef = TypedDict(
    "CreateDomainRequestRequestTypeDef",
    {
        "Name": str,
        "ServerSideEncryptionConfiguration": ServerSideEncryptionConfigurationTypeDef,
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
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
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CreateWatchlistResponseTypeDef = TypedDict(
    "CreateWatchlistResponseTypeDef",
    {
        "Watchlist": WatchlistTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeWatchlistResponseTypeDef = TypedDict(
    "DescribeWatchlistResponseTypeDef",
    {
        "Watchlist": WatchlistTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateWatchlistResponseTypeDef = TypedDict(
    "UpdateWatchlistResponseTypeDef",
    {
        "Watchlist": WatchlistTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSpeakerResponseTypeDef = TypedDict(
    "DescribeSpeakerResponseTypeDef",
    {
        "Speaker": SpeakerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OptOutSpeakerResponseTypeDef = TypedDict(
    "OptOutSpeakerResponseTypeDef",
    {
        "Speaker": SpeakerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DomainSummaryTypeDef = TypedDict(
    "DomainSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "Description": NotRequired[str],
        "DomainId": NotRequired[str],
        "DomainStatus": NotRequired[DomainStatusType],
        "Name": NotRequired[str],
        "ServerSideEncryptionConfiguration": NotRequired[ServerSideEncryptionConfigurationTypeDef],
        "ServerSideEncryptionUpdateDetails": NotRequired[ServerSideEncryptionUpdateDetailsTypeDef],
        "UpdatedAt": NotRequired[datetime],
        "WatchlistDetails": NotRequired[WatchlistDetailsTypeDef],
    },
)
DomainTypeDef = TypedDict(
    "DomainTypeDef",
    {
        "Arn": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "Description": NotRequired[str],
        "DomainId": NotRequired[str],
        "DomainStatus": NotRequired[DomainStatusType],
        "Name": NotRequired[str],
        "ServerSideEncryptionConfiguration": NotRequired[ServerSideEncryptionConfigurationTypeDef],
        "ServerSideEncryptionUpdateDetails": NotRequired[ServerSideEncryptionUpdateDetailsTypeDef],
        "UpdatedAt": NotRequired[datetime],
        "WatchlistDetails": NotRequired[WatchlistDetailsTypeDef],
    },
)
EnrollmentConfigOutputTypeDef = TypedDict(
    "EnrollmentConfigOutputTypeDef",
    {
        "ExistingEnrollmentAction": NotRequired[ExistingEnrollmentActionType],
        "FraudDetectionConfig": NotRequired[EnrollmentJobFraudDetectionConfigOutputTypeDef],
    },
)
EnrollmentJobFraudDetectionConfigUnionTypeDef = Union[
    EnrollmentJobFraudDetectionConfigTypeDef, EnrollmentJobFraudDetectionConfigOutputTypeDef
]
FraudRiskDetailsTypeDef = TypedDict(
    "FraudRiskDetailsTypeDef",
    {
        "KnownFraudsterRisk": KnownFraudsterRiskTypeDef,
        "VoiceSpoofingRisk": VoiceSpoofingRiskTypeDef,
    },
)
FraudsterRegistrationJobSummaryTypeDef = TypedDict(
    "FraudsterRegistrationJobSummaryTypeDef",
    {
        "CreatedAt": NotRequired[datetime],
        "DomainId": NotRequired[str],
        "EndedAt": NotRequired[datetime],
        "FailureDetails": NotRequired[FailureDetailsTypeDef],
        "JobId": NotRequired[str],
        "JobName": NotRequired[str],
        "JobProgress": NotRequired[JobProgressTypeDef],
        "JobStatus": NotRequired[FraudsterRegistrationJobStatusType],
    },
)
SpeakerEnrollmentJobSummaryTypeDef = TypedDict(
    "SpeakerEnrollmentJobSummaryTypeDef",
    {
        "CreatedAt": NotRequired[datetime],
        "DomainId": NotRequired[str],
        "EndedAt": NotRequired[datetime],
        "FailureDetails": NotRequired[FailureDetailsTypeDef],
        "JobId": NotRequired[str],
        "JobName": NotRequired[str],
        "JobProgress": NotRequired[JobProgressTypeDef],
        "JobStatus": NotRequired[SpeakerEnrollmentJobStatusType],
    },
)
FraudsterRegistrationJobTypeDef = TypedDict(
    "FraudsterRegistrationJobTypeDef",
    {
        "CreatedAt": NotRequired[datetime],
        "DataAccessRoleArn": NotRequired[str],
        "DomainId": NotRequired[str],
        "EndedAt": NotRequired[datetime],
        "FailureDetails": NotRequired[FailureDetailsTypeDef],
        "InputDataConfig": NotRequired[InputDataConfigTypeDef],
        "JobId": NotRequired[str],
        "JobName": NotRequired[str],
        "JobProgress": NotRequired[JobProgressTypeDef],
        "JobStatus": NotRequired[FraudsterRegistrationJobStatusType],
        "OutputDataConfig": NotRequired[OutputDataConfigTypeDef],
        "RegistrationConfig": NotRequired[RegistrationConfigOutputTypeDef],
    },
)
ListFraudstersResponseTypeDef = TypedDict(
    "ListFraudstersResponseTypeDef",
    {
        "FraudsterSummaries": List[FraudsterSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListDomainsRequestListDomainsPaginateTypeDef = TypedDict(
    "ListDomainsRequestListDomainsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFraudsterRegistrationJobsRequestListFraudsterRegistrationJobsPaginateTypeDef = TypedDict(
    "ListFraudsterRegistrationJobsRequestListFraudsterRegistrationJobsPaginateTypeDef",
    {
        "DomainId": str,
        "JobStatus": NotRequired[FraudsterRegistrationJobStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFraudstersRequestListFraudstersPaginateTypeDef = TypedDict(
    "ListFraudstersRequestListFraudstersPaginateTypeDef",
    {
        "DomainId": str,
        "WatchlistId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSpeakerEnrollmentJobsRequestListSpeakerEnrollmentJobsPaginateTypeDef = TypedDict(
    "ListSpeakerEnrollmentJobsRequestListSpeakerEnrollmentJobsPaginateTypeDef",
    {
        "DomainId": str,
        "JobStatus": NotRequired[SpeakerEnrollmentJobStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSpeakersRequestListSpeakersPaginateTypeDef = TypedDict(
    "ListSpeakersRequestListSpeakersPaginateTypeDef",
    {
        "DomainId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWatchlistsRequestListWatchlistsPaginateTypeDef = TypedDict(
    "ListWatchlistsRequestListWatchlistsPaginateTypeDef",
    {
        "DomainId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSpeakersResponseTypeDef = TypedDict(
    "ListSpeakersResponseTypeDef",
    {
        "SpeakerSummaries": List[SpeakerSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListWatchlistsResponseTypeDef = TypedDict(
    "ListWatchlistsResponseTypeDef",
    {
        "WatchlistSummaries": List[WatchlistSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
StartFraudsterRegistrationJobRequestRequestTypeDef = TypedDict(
    "StartFraudsterRegistrationJobRequestRequestTypeDef",
    {
        "DataAccessRoleArn": str,
        "DomainId": str,
        "InputDataConfig": InputDataConfigTypeDef,
        "OutputDataConfig": OutputDataConfigTypeDef,
        "ClientToken": NotRequired[str],
        "JobName": NotRequired[str],
        "RegistrationConfig": NotRequired[RegistrationConfigTypeDef],
    },
)
ListDomainsResponseTypeDef = TypedDict(
    "ListDomainsResponseTypeDef",
    {
        "DomainSummaries": List[DomainSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateDomainResponseTypeDef = TypedDict(
    "CreateDomainResponseTypeDef",
    {
        "Domain": DomainTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDomainResponseTypeDef = TypedDict(
    "DescribeDomainResponseTypeDef",
    {
        "Domain": DomainTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDomainResponseTypeDef = TypedDict(
    "UpdateDomainResponseTypeDef",
    {
        "Domain": DomainTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SpeakerEnrollmentJobTypeDef = TypedDict(
    "SpeakerEnrollmentJobTypeDef",
    {
        "CreatedAt": NotRequired[datetime],
        "DataAccessRoleArn": NotRequired[str],
        "DomainId": NotRequired[str],
        "EndedAt": NotRequired[datetime],
        "EnrollmentConfig": NotRequired[EnrollmentConfigOutputTypeDef],
        "FailureDetails": NotRequired[FailureDetailsTypeDef],
        "InputDataConfig": NotRequired[InputDataConfigTypeDef],
        "JobId": NotRequired[str],
        "JobName": NotRequired[str],
        "JobProgress": NotRequired[JobProgressTypeDef],
        "JobStatus": NotRequired[SpeakerEnrollmentJobStatusType],
        "OutputDataConfig": NotRequired[OutputDataConfigTypeDef],
    },
)
EnrollmentConfigTypeDef = TypedDict(
    "EnrollmentConfigTypeDef",
    {
        "ExistingEnrollmentAction": NotRequired[ExistingEnrollmentActionType],
        "FraudDetectionConfig": NotRequired[EnrollmentJobFraudDetectionConfigUnionTypeDef],
    },
)
FraudDetectionResultTypeDef = TypedDict(
    "FraudDetectionResultTypeDef",
    {
        "AudioAggregationEndedAt": NotRequired[datetime],
        "AudioAggregationStartedAt": NotRequired[datetime],
        "Configuration": NotRequired[FraudDetectionConfigurationTypeDef],
        "Decision": NotRequired[FraudDetectionDecisionType],
        "FraudDetectionResultId": NotRequired[str],
        "Reasons": NotRequired[List[FraudDetectionReasonType]],
        "RiskDetails": NotRequired[FraudRiskDetailsTypeDef],
    },
)
ListFraudsterRegistrationJobsResponseTypeDef = TypedDict(
    "ListFraudsterRegistrationJobsResponseTypeDef",
    {
        "JobSummaries": List[FraudsterRegistrationJobSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListSpeakerEnrollmentJobsResponseTypeDef = TypedDict(
    "ListSpeakerEnrollmentJobsResponseTypeDef",
    {
        "JobSummaries": List[SpeakerEnrollmentJobSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeFraudsterRegistrationJobResponseTypeDef = TypedDict(
    "DescribeFraudsterRegistrationJobResponseTypeDef",
    {
        "Job": FraudsterRegistrationJobTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartFraudsterRegistrationJobResponseTypeDef = TypedDict(
    "StartFraudsterRegistrationJobResponseTypeDef",
    {
        "Job": FraudsterRegistrationJobTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSpeakerEnrollmentJobResponseTypeDef = TypedDict(
    "DescribeSpeakerEnrollmentJobResponseTypeDef",
    {
        "Job": SpeakerEnrollmentJobTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartSpeakerEnrollmentJobResponseTypeDef = TypedDict(
    "StartSpeakerEnrollmentJobResponseTypeDef",
    {
        "Job": SpeakerEnrollmentJobTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartSpeakerEnrollmentJobRequestRequestTypeDef = TypedDict(
    "StartSpeakerEnrollmentJobRequestRequestTypeDef",
    {
        "DataAccessRoleArn": str,
        "DomainId": str,
        "InputDataConfig": InputDataConfigTypeDef,
        "OutputDataConfig": OutputDataConfigTypeDef,
        "ClientToken": NotRequired[str],
        "EnrollmentConfig": NotRequired[EnrollmentConfigTypeDef],
        "JobName": NotRequired[str],
    },
)
EvaluateSessionResponseTypeDef = TypedDict(
    "EvaluateSessionResponseTypeDef",
    {
        "AuthenticationResult": AuthenticationResultTypeDef,
        "DomainId": str,
        "FraudDetectionResult": FraudDetectionResultTypeDef,
        "SessionId": str,
        "SessionName": str,
        "StreamingStatus": StreamingStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
