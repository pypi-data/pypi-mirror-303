"""
Type annotations for transcribe service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_transcribe/type_defs/)

Usage::

    ```python
    from mypy_boto3_transcribe.type_defs import AbsoluteTimeRangeTypeDef

    data: AbsoluteTimeRangeTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    BaseModelNameType,
    CallAnalyticsJobStatusType,
    CallAnalyticsSkippedReasonCodeType,
    CLMLanguageCodeType,
    InputTypeType,
    LanguageCodeType,
    MediaFormatType,
    MedicalScribeJobStatusType,
    MedicalScribeParticipantRoleType,
    ModelStatusType,
    OutputLocationTypeType,
    ParticipantRoleType,
    PiiEntityTypeType,
    RedactionOutputType,
    SentimentValueType,
    SubtitleFormatType,
    TranscriptionJobStatusType,
    TypeType,
    VocabularyFilterMethodType,
    VocabularyStateType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AbsoluteTimeRangeTypeDef",
    "CallAnalyticsSkippedFeatureTypeDef",
    "ContentRedactionOutputTypeDef",
    "LanguageIdSettingsTypeDef",
    "SummarizationTypeDef",
    "ChannelDefinitionTypeDef",
    "MediaTypeDef",
    "TranscriptTypeDef",
    "ContentRedactionTypeDef",
    "ResponseMetadataTypeDef",
    "InputDataConfigTypeDef",
    "TagTypeDef",
    "DeleteCallAnalyticsCategoryRequestRequestTypeDef",
    "DeleteCallAnalyticsJobRequestRequestTypeDef",
    "DeleteLanguageModelRequestRequestTypeDef",
    "DeleteMedicalScribeJobRequestRequestTypeDef",
    "DeleteMedicalTranscriptionJobRequestRequestTypeDef",
    "DeleteMedicalVocabularyRequestRequestTypeDef",
    "DeleteTranscriptionJobRequestRequestTypeDef",
    "DeleteVocabularyFilterRequestRequestTypeDef",
    "DeleteVocabularyRequestRequestTypeDef",
    "DescribeLanguageModelRequestRequestTypeDef",
    "GetCallAnalyticsCategoryRequestRequestTypeDef",
    "GetCallAnalyticsJobRequestRequestTypeDef",
    "GetMedicalScribeJobRequestRequestTypeDef",
    "GetMedicalTranscriptionJobRequestRequestTypeDef",
    "GetMedicalVocabularyRequestRequestTypeDef",
    "GetTranscriptionJobRequestRequestTypeDef",
    "GetVocabularyFilterRequestRequestTypeDef",
    "GetVocabularyRequestRequestTypeDef",
    "RelativeTimeRangeTypeDef",
    "JobExecutionSettingsTypeDef",
    "LanguageCodeItemTypeDef",
    "ListCallAnalyticsCategoriesRequestRequestTypeDef",
    "ListCallAnalyticsJobsRequestRequestTypeDef",
    "ListLanguageModelsRequestRequestTypeDef",
    "ListMedicalScribeJobsRequestRequestTypeDef",
    "MedicalScribeJobSummaryTypeDef",
    "ListMedicalTranscriptionJobsRequestRequestTypeDef",
    "MedicalTranscriptionJobSummaryTypeDef",
    "ListMedicalVocabulariesRequestRequestTypeDef",
    "VocabularyInfoTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTranscriptionJobsRequestRequestTypeDef",
    "ListVocabulariesRequestRequestTypeDef",
    "ListVocabularyFiltersRequestRequestTypeDef",
    "VocabularyFilterInfoTypeDef",
    "MedicalScribeChannelDefinitionTypeDef",
    "MedicalScribeOutputTypeDef",
    "MedicalScribeSettingsTypeDef",
    "MedicalTranscriptTypeDef",
    "MedicalTranscriptionSettingTypeDef",
    "ModelSettingsTypeDef",
    "SettingsTypeDef",
    "SubtitlesTypeDef",
    "SubtitlesOutputTypeDef",
    "ToxicityDetectionSettingsOutputTypeDef",
    "ToxicityDetectionSettingsTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateMedicalVocabularyRequestRequestTypeDef",
    "UpdateVocabularyFilterRequestRequestTypeDef",
    "UpdateVocabularyRequestRequestTypeDef",
    "CallAnalyticsJobDetailsTypeDef",
    "CallAnalyticsJobSettingsOutputTypeDef",
    "ContentRedactionUnionTypeDef",
    "CreateMedicalVocabularyResponseTypeDef",
    "CreateVocabularyFilterResponseTypeDef",
    "CreateVocabularyResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetMedicalVocabularyResponseTypeDef",
    "GetVocabularyFilterResponseTypeDef",
    "GetVocabularyResponseTypeDef",
    "UpdateMedicalVocabularyResponseTypeDef",
    "UpdateVocabularyFilterResponseTypeDef",
    "UpdateVocabularyResponseTypeDef",
    "CreateLanguageModelResponseTypeDef",
    "LanguageModelTypeDef",
    "CreateLanguageModelRequestRequestTypeDef",
    "CreateMedicalVocabularyRequestRequestTypeDef",
    "CreateVocabularyFilterRequestRequestTypeDef",
    "CreateVocabularyRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "InterruptionFilterTypeDef",
    "NonTalkTimeFilterTypeDef",
    "SentimentFilterOutputTypeDef",
    "SentimentFilterTypeDef",
    "TranscriptFilterOutputTypeDef",
    "TranscriptFilterTypeDef",
    "ListMedicalScribeJobsResponseTypeDef",
    "ListMedicalTranscriptionJobsResponseTypeDef",
    "ListMedicalVocabulariesResponseTypeDef",
    "ListVocabulariesResponseTypeDef",
    "ListVocabularyFiltersResponseTypeDef",
    "MedicalScribeJobTypeDef",
    "StartMedicalScribeJobRequestRequestTypeDef",
    "MedicalTranscriptionJobTypeDef",
    "StartMedicalTranscriptionJobRequestRequestTypeDef",
    "TranscriptionJobSummaryTypeDef",
    "TranscriptionJobTypeDef",
    "ToxicityDetectionSettingsUnionTypeDef",
    "CallAnalyticsJobSummaryTypeDef",
    "CallAnalyticsJobTypeDef",
    "CallAnalyticsJobSettingsTypeDef",
    "DescribeLanguageModelResponseTypeDef",
    "ListLanguageModelsResponseTypeDef",
    "SentimentFilterUnionTypeDef",
    "RuleOutputTypeDef",
    "TranscriptFilterUnionTypeDef",
    "GetMedicalScribeJobResponseTypeDef",
    "StartMedicalScribeJobResponseTypeDef",
    "GetMedicalTranscriptionJobResponseTypeDef",
    "StartMedicalTranscriptionJobResponseTypeDef",
    "ListTranscriptionJobsResponseTypeDef",
    "GetTranscriptionJobResponseTypeDef",
    "StartTranscriptionJobResponseTypeDef",
    "StartTranscriptionJobRequestRequestTypeDef",
    "ListCallAnalyticsJobsResponseTypeDef",
    "GetCallAnalyticsJobResponseTypeDef",
    "StartCallAnalyticsJobResponseTypeDef",
    "StartCallAnalyticsJobRequestRequestTypeDef",
    "CategoryPropertiesTypeDef",
    "RuleTypeDef",
    "CreateCallAnalyticsCategoryResponseTypeDef",
    "GetCallAnalyticsCategoryResponseTypeDef",
    "ListCallAnalyticsCategoriesResponseTypeDef",
    "UpdateCallAnalyticsCategoryResponseTypeDef",
    "RuleUnionTypeDef",
    "UpdateCallAnalyticsCategoryRequestRequestTypeDef",
    "CreateCallAnalyticsCategoryRequestRequestTypeDef",
)

AbsoluteTimeRangeTypeDef = TypedDict(
    "AbsoluteTimeRangeTypeDef",
    {
        "StartTime": NotRequired[int],
        "EndTime": NotRequired[int],
        "First": NotRequired[int],
        "Last": NotRequired[int],
    },
)
CallAnalyticsSkippedFeatureTypeDef = TypedDict(
    "CallAnalyticsSkippedFeatureTypeDef",
    {
        "Feature": NotRequired[Literal["GENERATIVE_SUMMARIZATION"]],
        "ReasonCode": NotRequired[CallAnalyticsSkippedReasonCodeType],
        "Message": NotRequired[str],
    },
)
ContentRedactionOutputTypeDef = TypedDict(
    "ContentRedactionOutputTypeDef",
    {
        "RedactionType": Literal["PII"],
        "RedactionOutput": RedactionOutputType,
        "PiiEntityTypes": NotRequired[List[PiiEntityTypeType]],
    },
)
LanguageIdSettingsTypeDef = TypedDict(
    "LanguageIdSettingsTypeDef",
    {
        "VocabularyName": NotRequired[str],
        "VocabularyFilterName": NotRequired[str],
        "LanguageModelName": NotRequired[str],
    },
)
SummarizationTypeDef = TypedDict(
    "SummarizationTypeDef",
    {
        "GenerateAbstractiveSummary": bool,
    },
)
ChannelDefinitionTypeDef = TypedDict(
    "ChannelDefinitionTypeDef",
    {
        "ChannelId": NotRequired[int],
        "ParticipantRole": NotRequired[ParticipantRoleType],
    },
)
MediaTypeDef = TypedDict(
    "MediaTypeDef",
    {
        "MediaFileUri": NotRequired[str],
        "RedactedMediaFileUri": NotRequired[str],
    },
)
TranscriptTypeDef = TypedDict(
    "TranscriptTypeDef",
    {
        "TranscriptFileUri": NotRequired[str],
        "RedactedTranscriptFileUri": NotRequired[str],
    },
)
ContentRedactionTypeDef = TypedDict(
    "ContentRedactionTypeDef",
    {
        "RedactionType": Literal["PII"],
        "RedactionOutput": RedactionOutputType,
        "PiiEntityTypes": NotRequired[Sequence[PiiEntityTypeType]],
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
InputDataConfigTypeDef = TypedDict(
    "InputDataConfigTypeDef",
    {
        "S3Uri": str,
        "DataAccessRoleArn": str,
        "TuningDataS3Uri": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
DeleteCallAnalyticsCategoryRequestRequestTypeDef = TypedDict(
    "DeleteCallAnalyticsCategoryRequestRequestTypeDef",
    {
        "CategoryName": str,
    },
)
DeleteCallAnalyticsJobRequestRequestTypeDef = TypedDict(
    "DeleteCallAnalyticsJobRequestRequestTypeDef",
    {
        "CallAnalyticsJobName": str,
    },
)
DeleteLanguageModelRequestRequestTypeDef = TypedDict(
    "DeleteLanguageModelRequestRequestTypeDef",
    {
        "ModelName": str,
    },
)
DeleteMedicalScribeJobRequestRequestTypeDef = TypedDict(
    "DeleteMedicalScribeJobRequestRequestTypeDef",
    {
        "MedicalScribeJobName": str,
    },
)
DeleteMedicalTranscriptionJobRequestRequestTypeDef = TypedDict(
    "DeleteMedicalTranscriptionJobRequestRequestTypeDef",
    {
        "MedicalTranscriptionJobName": str,
    },
)
DeleteMedicalVocabularyRequestRequestTypeDef = TypedDict(
    "DeleteMedicalVocabularyRequestRequestTypeDef",
    {
        "VocabularyName": str,
    },
)
DeleteTranscriptionJobRequestRequestTypeDef = TypedDict(
    "DeleteTranscriptionJobRequestRequestTypeDef",
    {
        "TranscriptionJobName": str,
    },
)
DeleteVocabularyFilterRequestRequestTypeDef = TypedDict(
    "DeleteVocabularyFilterRequestRequestTypeDef",
    {
        "VocabularyFilterName": str,
    },
)
DeleteVocabularyRequestRequestTypeDef = TypedDict(
    "DeleteVocabularyRequestRequestTypeDef",
    {
        "VocabularyName": str,
    },
)
DescribeLanguageModelRequestRequestTypeDef = TypedDict(
    "DescribeLanguageModelRequestRequestTypeDef",
    {
        "ModelName": str,
    },
)
GetCallAnalyticsCategoryRequestRequestTypeDef = TypedDict(
    "GetCallAnalyticsCategoryRequestRequestTypeDef",
    {
        "CategoryName": str,
    },
)
GetCallAnalyticsJobRequestRequestTypeDef = TypedDict(
    "GetCallAnalyticsJobRequestRequestTypeDef",
    {
        "CallAnalyticsJobName": str,
    },
)
GetMedicalScribeJobRequestRequestTypeDef = TypedDict(
    "GetMedicalScribeJobRequestRequestTypeDef",
    {
        "MedicalScribeJobName": str,
    },
)
GetMedicalTranscriptionJobRequestRequestTypeDef = TypedDict(
    "GetMedicalTranscriptionJobRequestRequestTypeDef",
    {
        "MedicalTranscriptionJobName": str,
    },
)
GetMedicalVocabularyRequestRequestTypeDef = TypedDict(
    "GetMedicalVocabularyRequestRequestTypeDef",
    {
        "VocabularyName": str,
    },
)
GetTranscriptionJobRequestRequestTypeDef = TypedDict(
    "GetTranscriptionJobRequestRequestTypeDef",
    {
        "TranscriptionJobName": str,
    },
)
GetVocabularyFilterRequestRequestTypeDef = TypedDict(
    "GetVocabularyFilterRequestRequestTypeDef",
    {
        "VocabularyFilterName": str,
    },
)
GetVocabularyRequestRequestTypeDef = TypedDict(
    "GetVocabularyRequestRequestTypeDef",
    {
        "VocabularyName": str,
    },
)
RelativeTimeRangeTypeDef = TypedDict(
    "RelativeTimeRangeTypeDef",
    {
        "StartPercentage": NotRequired[int],
        "EndPercentage": NotRequired[int],
        "First": NotRequired[int],
        "Last": NotRequired[int],
    },
)
JobExecutionSettingsTypeDef = TypedDict(
    "JobExecutionSettingsTypeDef",
    {
        "AllowDeferredExecution": NotRequired[bool],
        "DataAccessRoleArn": NotRequired[str],
    },
)
LanguageCodeItemTypeDef = TypedDict(
    "LanguageCodeItemTypeDef",
    {
        "LanguageCode": NotRequired[LanguageCodeType],
        "DurationInSeconds": NotRequired[float],
    },
)
ListCallAnalyticsCategoriesRequestRequestTypeDef = TypedDict(
    "ListCallAnalyticsCategoriesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListCallAnalyticsJobsRequestRequestTypeDef = TypedDict(
    "ListCallAnalyticsJobsRequestRequestTypeDef",
    {
        "Status": NotRequired[CallAnalyticsJobStatusType],
        "JobNameContains": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListLanguageModelsRequestRequestTypeDef = TypedDict(
    "ListLanguageModelsRequestRequestTypeDef",
    {
        "StatusEquals": NotRequired[ModelStatusType],
        "NameContains": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListMedicalScribeJobsRequestRequestTypeDef = TypedDict(
    "ListMedicalScribeJobsRequestRequestTypeDef",
    {
        "Status": NotRequired[MedicalScribeJobStatusType],
        "JobNameContains": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
MedicalScribeJobSummaryTypeDef = TypedDict(
    "MedicalScribeJobSummaryTypeDef",
    {
        "MedicalScribeJobName": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "StartTime": NotRequired[datetime],
        "CompletionTime": NotRequired[datetime],
        "LanguageCode": NotRequired[Literal["en-US"]],
        "MedicalScribeJobStatus": NotRequired[MedicalScribeJobStatusType],
        "FailureReason": NotRequired[str],
    },
)
ListMedicalTranscriptionJobsRequestRequestTypeDef = TypedDict(
    "ListMedicalTranscriptionJobsRequestRequestTypeDef",
    {
        "Status": NotRequired[TranscriptionJobStatusType],
        "JobNameContains": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
MedicalTranscriptionJobSummaryTypeDef = TypedDict(
    "MedicalTranscriptionJobSummaryTypeDef",
    {
        "MedicalTranscriptionJobName": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "StartTime": NotRequired[datetime],
        "CompletionTime": NotRequired[datetime],
        "LanguageCode": NotRequired[LanguageCodeType],
        "TranscriptionJobStatus": NotRequired[TranscriptionJobStatusType],
        "FailureReason": NotRequired[str],
        "OutputLocationType": NotRequired[OutputLocationTypeType],
        "Specialty": NotRequired[Literal["PRIMARYCARE"]],
        "ContentIdentificationType": NotRequired[Literal["PHI"]],
        "Type": NotRequired[TypeType],
    },
)
ListMedicalVocabulariesRequestRequestTypeDef = TypedDict(
    "ListMedicalVocabulariesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "StateEquals": NotRequired[VocabularyStateType],
        "NameContains": NotRequired[str],
    },
)
VocabularyInfoTypeDef = TypedDict(
    "VocabularyInfoTypeDef",
    {
        "VocabularyName": NotRequired[str],
        "LanguageCode": NotRequired[LanguageCodeType],
        "LastModifiedTime": NotRequired[datetime],
        "VocabularyState": NotRequired[VocabularyStateType],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
ListTranscriptionJobsRequestRequestTypeDef = TypedDict(
    "ListTranscriptionJobsRequestRequestTypeDef",
    {
        "Status": NotRequired[TranscriptionJobStatusType],
        "JobNameContains": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListVocabulariesRequestRequestTypeDef = TypedDict(
    "ListVocabulariesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "StateEquals": NotRequired[VocabularyStateType],
        "NameContains": NotRequired[str],
    },
)
ListVocabularyFiltersRequestRequestTypeDef = TypedDict(
    "ListVocabularyFiltersRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NameContains": NotRequired[str],
    },
)
VocabularyFilterInfoTypeDef = TypedDict(
    "VocabularyFilterInfoTypeDef",
    {
        "VocabularyFilterName": NotRequired[str],
        "LanguageCode": NotRequired[LanguageCodeType],
        "LastModifiedTime": NotRequired[datetime],
    },
)
MedicalScribeChannelDefinitionTypeDef = TypedDict(
    "MedicalScribeChannelDefinitionTypeDef",
    {
        "ChannelId": int,
        "ParticipantRole": MedicalScribeParticipantRoleType,
    },
)
MedicalScribeOutputTypeDef = TypedDict(
    "MedicalScribeOutputTypeDef",
    {
        "TranscriptFileUri": str,
        "ClinicalDocumentUri": str,
    },
)
MedicalScribeSettingsTypeDef = TypedDict(
    "MedicalScribeSettingsTypeDef",
    {
        "ShowSpeakerLabels": NotRequired[bool],
        "MaxSpeakerLabels": NotRequired[int],
        "ChannelIdentification": NotRequired[bool],
        "VocabularyName": NotRequired[str],
        "VocabularyFilterName": NotRequired[str],
        "VocabularyFilterMethod": NotRequired[VocabularyFilterMethodType],
    },
)
MedicalTranscriptTypeDef = TypedDict(
    "MedicalTranscriptTypeDef",
    {
        "TranscriptFileUri": NotRequired[str],
    },
)
MedicalTranscriptionSettingTypeDef = TypedDict(
    "MedicalTranscriptionSettingTypeDef",
    {
        "ShowSpeakerLabels": NotRequired[bool],
        "MaxSpeakerLabels": NotRequired[int],
        "ChannelIdentification": NotRequired[bool],
        "ShowAlternatives": NotRequired[bool],
        "MaxAlternatives": NotRequired[int],
        "VocabularyName": NotRequired[str],
    },
)
ModelSettingsTypeDef = TypedDict(
    "ModelSettingsTypeDef",
    {
        "LanguageModelName": NotRequired[str],
    },
)
SettingsTypeDef = TypedDict(
    "SettingsTypeDef",
    {
        "VocabularyName": NotRequired[str],
        "ShowSpeakerLabels": NotRequired[bool],
        "MaxSpeakerLabels": NotRequired[int],
        "ChannelIdentification": NotRequired[bool],
        "ShowAlternatives": NotRequired[bool],
        "MaxAlternatives": NotRequired[int],
        "VocabularyFilterName": NotRequired[str],
        "VocabularyFilterMethod": NotRequired[VocabularyFilterMethodType],
    },
)
SubtitlesTypeDef = TypedDict(
    "SubtitlesTypeDef",
    {
        "Formats": NotRequired[Sequence[SubtitleFormatType]],
        "OutputStartIndex": NotRequired[int],
    },
)
SubtitlesOutputTypeDef = TypedDict(
    "SubtitlesOutputTypeDef",
    {
        "Formats": NotRequired[List[SubtitleFormatType]],
        "SubtitleFileUris": NotRequired[List[str]],
        "OutputStartIndex": NotRequired[int],
    },
)
ToxicityDetectionSettingsOutputTypeDef = TypedDict(
    "ToxicityDetectionSettingsOutputTypeDef",
    {
        "ToxicityCategories": List[Literal["ALL"]],
    },
)
ToxicityDetectionSettingsTypeDef = TypedDict(
    "ToxicityDetectionSettingsTypeDef",
    {
        "ToxicityCategories": Sequence[Literal["ALL"]],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateMedicalVocabularyRequestRequestTypeDef = TypedDict(
    "UpdateMedicalVocabularyRequestRequestTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "VocabularyFileUri": str,
    },
)
UpdateVocabularyFilterRequestRequestTypeDef = TypedDict(
    "UpdateVocabularyFilterRequestRequestTypeDef",
    {
        "VocabularyFilterName": str,
        "Words": NotRequired[Sequence[str]],
        "VocabularyFilterFileUri": NotRequired[str],
        "DataAccessRoleArn": NotRequired[str],
    },
)
UpdateVocabularyRequestRequestTypeDef = TypedDict(
    "UpdateVocabularyRequestRequestTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "Phrases": NotRequired[Sequence[str]],
        "VocabularyFileUri": NotRequired[str],
        "DataAccessRoleArn": NotRequired[str],
    },
)
CallAnalyticsJobDetailsTypeDef = TypedDict(
    "CallAnalyticsJobDetailsTypeDef",
    {
        "Skipped": NotRequired[List[CallAnalyticsSkippedFeatureTypeDef]],
    },
)
CallAnalyticsJobSettingsOutputTypeDef = TypedDict(
    "CallAnalyticsJobSettingsOutputTypeDef",
    {
        "VocabularyName": NotRequired[str],
        "VocabularyFilterName": NotRequired[str],
        "VocabularyFilterMethod": NotRequired[VocabularyFilterMethodType],
        "LanguageModelName": NotRequired[str],
        "ContentRedaction": NotRequired[ContentRedactionOutputTypeDef],
        "LanguageOptions": NotRequired[List[LanguageCodeType]],
        "LanguageIdSettings": NotRequired[Dict[LanguageCodeType, LanguageIdSettingsTypeDef]],
        "Summarization": NotRequired[SummarizationTypeDef],
    },
)
ContentRedactionUnionTypeDef = Union[ContentRedactionTypeDef, ContentRedactionOutputTypeDef]
CreateMedicalVocabularyResponseTypeDef = TypedDict(
    "CreateMedicalVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "VocabularyState": VocabularyStateType,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateVocabularyFilterResponseTypeDef = TypedDict(
    "CreateVocabularyFilterResponseTypeDef",
    {
        "VocabularyFilterName": str,
        "LanguageCode": LanguageCodeType,
        "LastModifiedTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateVocabularyResponseTypeDef = TypedDict(
    "CreateVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "VocabularyState": VocabularyStateType,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMedicalVocabularyResponseTypeDef = TypedDict(
    "GetMedicalVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "VocabularyState": VocabularyStateType,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "DownloadUri": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetVocabularyFilterResponseTypeDef = TypedDict(
    "GetVocabularyFilterResponseTypeDef",
    {
        "VocabularyFilterName": str,
        "LanguageCode": LanguageCodeType,
        "LastModifiedTime": datetime,
        "DownloadUri": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetVocabularyResponseTypeDef = TypedDict(
    "GetVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "VocabularyState": VocabularyStateType,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "DownloadUri": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateMedicalVocabularyResponseTypeDef = TypedDict(
    "UpdateMedicalVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "LastModifiedTime": datetime,
        "VocabularyState": VocabularyStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateVocabularyFilterResponseTypeDef = TypedDict(
    "UpdateVocabularyFilterResponseTypeDef",
    {
        "VocabularyFilterName": str,
        "LanguageCode": LanguageCodeType,
        "LastModifiedTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateVocabularyResponseTypeDef = TypedDict(
    "UpdateVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "LastModifiedTime": datetime,
        "VocabularyState": VocabularyStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateLanguageModelResponseTypeDef = TypedDict(
    "CreateLanguageModelResponseTypeDef",
    {
        "LanguageCode": CLMLanguageCodeType,
        "BaseModelName": BaseModelNameType,
        "ModelName": str,
        "InputDataConfig": InputDataConfigTypeDef,
        "ModelStatus": ModelStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LanguageModelTypeDef = TypedDict(
    "LanguageModelTypeDef",
    {
        "ModelName": NotRequired[str],
        "CreateTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
        "LanguageCode": NotRequired[CLMLanguageCodeType],
        "BaseModelName": NotRequired[BaseModelNameType],
        "ModelStatus": NotRequired[ModelStatusType],
        "UpgradeAvailability": NotRequired[bool],
        "FailureReason": NotRequired[str],
        "InputDataConfig": NotRequired[InputDataConfigTypeDef],
    },
)
CreateLanguageModelRequestRequestTypeDef = TypedDict(
    "CreateLanguageModelRequestRequestTypeDef",
    {
        "LanguageCode": CLMLanguageCodeType,
        "BaseModelName": BaseModelNameType,
        "ModelName": str,
        "InputDataConfig": InputDataConfigTypeDef,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateMedicalVocabularyRequestRequestTypeDef = TypedDict(
    "CreateMedicalVocabularyRequestRequestTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "VocabularyFileUri": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateVocabularyFilterRequestRequestTypeDef = TypedDict(
    "CreateVocabularyFilterRequestRequestTypeDef",
    {
        "VocabularyFilterName": str,
        "LanguageCode": LanguageCodeType,
        "Words": NotRequired[Sequence[str]],
        "VocabularyFilterFileUri": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "DataAccessRoleArn": NotRequired[str],
    },
)
CreateVocabularyRequestRequestTypeDef = TypedDict(
    "CreateVocabularyRequestRequestTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "Phrases": NotRequired[Sequence[str]],
        "VocabularyFileUri": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "DataAccessRoleArn": NotRequired[str],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "ResourceArn": str,
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
InterruptionFilterTypeDef = TypedDict(
    "InterruptionFilterTypeDef",
    {
        "Threshold": NotRequired[int],
        "ParticipantRole": NotRequired[ParticipantRoleType],
        "AbsoluteTimeRange": NotRequired[AbsoluteTimeRangeTypeDef],
        "RelativeTimeRange": NotRequired[RelativeTimeRangeTypeDef],
        "Negate": NotRequired[bool],
    },
)
NonTalkTimeFilterTypeDef = TypedDict(
    "NonTalkTimeFilterTypeDef",
    {
        "Threshold": NotRequired[int],
        "AbsoluteTimeRange": NotRequired[AbsoluteTimeRangeTypeDef],
        "RelativeTimeRange": NotRequired[RelativeTimeRangeTypeDef],
        "Negate": NotRequired[bool],
    },
)
SentimentFilterOutputTypeDef = TypedDict(
    "SentimentFilterOutputTypeDef",
    {
        "Sentiments": List[SentimentValueType],
        "AbsoluteTimeRange": NotRequired[AbsoluteTimeRangeTypeDef],
        "RelativeTimeRange": NotRequired[RelativeTimeRangeTypeDef],
        "ParticipantRole": NotRequired[ParticipantRoleType],
        "Negate": NotRequired[bool],
    },
)
SentimentFilterTypeDef = TypedDict(
    "SentimentFilterTypeDef",
    {
        "Sentiments": Sequence[SentimentValueType],
        "AbsoluteTimeRange": NotRequired[AbsoluteTimeRangeTypeDef],
        "RelativeTimeRange": NotRequired[RelativeTimeRangeTypeDef],
        "ParticipantRole": NotRequired[ParticipantRoleType],
        "Negate": NotRequired[bool],
    },
)
TranscriptFilterOutputTypeDef = TypedDict(
    "TranscriptFilterOutputTypeDef",
    {
        "TranscriptFilterType": Literal["EXACT"],
        "Targets": List[str],
        "AbsoluteTimeRange": NotRequired[AbsoluteTimeRangeTypeDef],
        "RelativeTimeRange": NotRequired[RelativeTimeRangeTypeDef],
        "ParticipantRole": NotRequired[ParticipantRoleType],
        "Negate": NotRequired[bool],
    },
)
TranscriptFilterTypeDef = TypedDict(
    "TranscriptFilterTypeDef",
    {
        "TranscriptFilterType": Literal["EXACT"],
        "Targets": Sequence[str],
        "AbsoluteTimeRange": NotRequired[AbsoluteTimeRangeTypeDef],
        "RelativeTimeRange": NotRequired[RelativeTimeRangeTypeDef],
        "ParticipantRole": NotRequired[ParticipantRoleType],
        "Negate": NotRequired[bool],
    },
)
ListMedicalScribeJobsResponseTypeDef = TypedDict(
    "ListMedicalScribeJobsResponseTypeDef",
    {
        "Status": MedicalScribeJobStatusType,
        "MedicalScribeJobSummaries": List[MedicalScribeJobSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListMedicalTranscriptionJobsResponseTypeDef = TypedDict(
    "ListMedicalTranscriptionJobsResponseTypeDef",
    {
        "Status": TranscriptionJobStatusType,
        "MedicalTranscriptionJobSummaries": List[MedicalTranscriptionJobSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListMedicalVocabulariesResponseTypeDef = TypedDict(
    "ListMedicalVocabulariesResponseTypeDef",
    {
        "Status": VocabularyStateType,
        "Vocabularies": List[VocabularyInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListVocabulariesResponseTypeDef = TypedDict(
    "ListVocabulariesResponseTypeDef",
    {
        "Status": VocabularyStateType,
        "Vocabularies": List[VocabularyInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListVocabularyFiltersResponseTypeDef = TypedDict(
    "ListVocabularyFiltersResponseTypeDef",
    {
        "VocabularyFilters": List[VocabularyFilterInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
MedicalScribeJobTypeDef = TypedDict(
    "MedicalScribeJobTypeDef",
    {
        "MedicalScribeJobName": NotRequired[str],
        "MedicalScribeJobStatus": NotRequired[MedicalScribeJobStatusType],
        "LanguageCode": NotRequired[Literal["en-US"]],
        "Media": NotRequired[MediaTypeDef],
        "MedicalScribeOutput": NotRequired[MedicalScribeOutputTypeDef],
        "StartTime": NotRequired[datetime],
        "CreationTime": NotRequired[datetime],
        "CompletionTime": NotRequired[datetime],
        "FailureReason": NotRequired[str],
        "Settings": NotRequired[MedicalScribeSettingsTypeDef],
        "DataAccessRoleArn": NotRequired[str],
        "ChannelDefinitions": NotRequired[List[MedicalScribeChannelDefinitionTypeDef]],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
StartMedicalScribeJobRequestRequestTypeDef = TypedDict(
    "StartMedicalScribeJobRequestRequestTypeDef",
    {
        "MedicalScribeJobName": str,
        "Media": MediaTypeDef,
        "OutputBucketName": str,
        "DataAccessRoleArn": str,
        "Settings": MedicalScribeSettingsTypeDef,
        "OutputEncryptionKMSKeyId": NotRequired[str],
        "KMSEncryptionContext": NotRequired[Mapping[str, str]],
        "ChannelDefinitions": NotRequired[Sequence[MedicalScribeChannelDefinitionTypeDef]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
MedicalTranscriptionJobTypeDef = TypedDict(
    "MedicalTranscriptionJobTypeDef",
    {
        "MedicalTranscriptionJobName": NotRequired[str],
        "TranscriptionJobStatus": NotRequired[TranscriptionJobStatusType],
        "LanguageCode": NotRequired[LanguageCodeType],
        "MediaSampleRateHertz": NotRequired[int],
        "MediaFormat": NotRequired[MediaFormatType],
        "Media": NotRequired[MediaTypeDef],
        "Transcript": NotRequired[MedicalTranscriptTypeDef],
        "StartTime": NotRequired[datetime],
        "CreationTime": NotRequired[datetime],
        "CompletionTime": NotRequired[datetime],
        "FailureReason": NotRequired[str],
        "Settings": NotRequired[MedicalTranscriptionSettingTypeDef],
        "ContentIdentificationType": NotRequired[Literal["PHI"]],
        "Specialty": NotRequired[Literal["PRIMARYCARE"]],
        "Type": NotRequired[TypeType],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
StartMedicalTranscriptionJobRequestRequestTypeDef = TypedDict(
    "StartMedicalTranscriptionJobRequestRequestTypeDef",
    {
        "MedicalTranscriptionJobName": str,
        "LanguageCode": LanguageCodeType,
        "Media": MediaTypeDef,
        "OutputBucketName": str,
        "Specialty": Literal["PRIMARYCARE"],
        "Type": TypeType,
        "MediaSampleRateHertz": NotRequired[int],
        "MediaFormat": NotRequired[MediaFormatType],
        "OutputKey": NotRequired[str],
        "OutputEncryptionKMSKeyId": NotRequired[str],
        "KMSEncryptionContext": NotRequired[Mapping[str, str]],
        "Settings": NotRequired[MedicalTranscriptionSettingTypeDef],
        "ContentIdentificationType": NotRequired[Literal["PHI"]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
TranscriptionJobSummaryTypeDef = TypedDict(
    "TranscriptionJobSummaryTypeDef",
    {
        "TranscriptionJobName": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "StartTime": NotRequired[datetime],
        "CompletionTime": NotRequired[datetime],
        "LanguageCode": NotRequired[LanguageCodeType],
        "TranscriptionJobStatus": NotRequired[TranscriptionJobStatusType],
        "FailureReason": NotRequired[str],
        "OutputLocationType": NotRequired[OutputLocationTypeType],
        "ContentRedaction": NotRequired[ContentRedactionOutputTypeDef],
        "ModelSettings": NotRequired[ModelSettingsTypeDef],
        "IdentifyLanguage": NotRequired[bool],
        "IdentifyMultipleLanguages": NotRequired[bool],
        "IdentifiedLanguageScore": NotRequired[float],
        "LanguageCodes": NotRequired[List[LanguageCodeItemTypeDef]],
        "ToxicityDetection": NotRequired[List[ToxicityDetectionSettingsOutputTypeDef]],
    },
)
TranscriptionJobTypeDef = TypedDict(
    "TranscriptionJobTypeDef",
    {
        "TranscriptionJobName": NotRequired[str],
        "TranscriptionJobStatus": NotRequired[TranscriptionJobStatusType],
        "LanguageCode": NotRequired[LanguageCodeType],
        "MediaSampleRateHertz": NotRequired[int],
        "MediaFormat": NotRequired[MediaFormatType],
        "Media": NotRequired[MediaTypeDef],
        "Transcript": NotRequired[TranscriptTypeDef],
        "StartTime": NotRequired[datetime],
        "CreationTime": NotRequired[datetime],
        "CompletionTime": NotRequired[datetime],
        "FailureReason": NotRequired[str],
        "Settings": NotRequired[SettingsTypeDef],
        "ModelSettings": NotRequired[ModelSettingsTypeDef],
        "JobExecutionSettings": NotRequired[JobExecutionSettingsTypeDef],
        "ContentRedaction": NotRequired[ContentRedactionOutputTypeDef],
        "IdentifyLanguage": NotRequired[bool],
        "IdentifyMultipleLanguages": NotRequired[bool],
        "LanguageOptions": NotRequired[List[LanguageCodeType]],
        "IdentifiedLanguageScore": NotRequired[float],
        "LanguageCodes": NotRequired[List[LanguageCodeItemTypeDef]],
        "Tags": NotRequired[List[TagTypeDef]],
        "Subtitles": NotRequired[SubtitlesOutputTypeDef],
        "LanguageIdSettings": NotRequired[Dict[LanguageCodeType, LanguageIdSettingsTypeDef]],
        "ToxicityDetection": NotRequired[List[ToxicityDetectionSettingsOutputTypeDef]],
    },
)
ToxicityDetectionSettingsUnionTypeDef = Union[
    ToxicityDetectionSettingsTypeDef, ToxicityDetectionSettingsOutputTypeDef
]
CallAnalyticsJobSummaryTypeDef = TypedDict(
    "CallAnalyticsJobSummaryTypeDef",
    {
        "CallAnalyticsJobName": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "StartTime": NotRequired[datetime],
        "CompletionTime": NotRequired[datetime],
        "LanguageCode": NotRequired[LanguageCodeType],
        "CallAnalyticsJobStatus": NotRequired[CallAnalyticsJobStatusType],
        "CallAnalyticsJobDetails": NotRequired[CallAnalyticsJobDetailsTypeDef],
        "FailureReason": NotRequired[str],
    },
)
CallAnalyticsJobTypeDef = TypedDict(
    "CallAnalyticsJobTypeDef",
    {
        "CallAnalyticsJobName": NotRequired[str],
        "CallAnalyticsJobStatus": NotRequired[CallAnalyticsJobStatusType],
        "CallAnalyticsJobDetails": NotRequired[CallAnalyticsJobDetailsTypeDef],
        "LanguageCode": NotRequired[LanguageCodeType],
        "MediaSampleRateHertz": NotRequired[int],
        "MediaFormat": NotRequired[MediaFormatType],
        "Media": NotRequired[MediaTypeDef],
        "Transcript": NotRequired[TranscriptTypeDef],
        "StartTime": NotRequired[datetime],
        "CreationTime": NotRequired[datetime],
        "CompletionTime": NotRequired[datetime],
        "FailureReason": NotRequired[str],
        "DataAccessRoleArn": NotRequired[str],
        "IdentifiedLanguageScore": NotRequired[float],
        "Settings": NotRequired[CallAnalyticsJobSettingsOutputTypeDef],
        "ChannelDefinitions": NotRequired[List[ChannelDefinitionTypeDef]],
    },
)
CallAnalyticsJobSettingsTypeDef = TypedDict(
    "CallAnalyticsJobSettingsTypeDef",
    {
        "VocabularyName": NotRequired[str],
        "VocabularyFilterName": NotRequired[str],
        "VocabularyFilterMethod": NotRequired[VocabularyFilterMethodType],
        "LanguageModelName": NotRequired[str],
        "ContentRedaction": NotRequired[ContentRedactionUnionTypeDef],
        "LanguageOptions": NotRequired[Sequence[LanguageCodeType]],
        "LanguageIdSettings": NotRequired[Mapping[LanguageCodeType, LanguageIdSettingsTypeDef]],
        "Summarization": NotRequired[SummarizationTypeDef],
    },
)
DescribeLanguageModelResponseTypeDef = TypedDict(
    "DescribeLanguageModelResponseTypeDef",
    {
        "LanguageModel": LanguageModelTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListLanguageModelsResponseTypeDef = TypedDict(
    "ListLanguageModelsResponseTypeDef",
    {
        "Models": List[LanguageModelTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
SentimentFilterUnionTypeDef = Union[SentimentFilterTypeDef, SentimentFilterOutputTypeDef]
RuleOutputTypeDef = TypedDict(
    "RuleOutputTypeDef",
    {
        "NonTalkTimeFilter": NotRequired[NonTalkTimeFilterTypeDef],
        "InterruptionFilter": NotRequired[InterruptionFilterTypeDef],
        "TranscriptFilter": NotRequired[TranscriptFilterOutputTypeDef],
        "SentimentFilter": NotRequired[SentimentFilterOutputTypeDef],
    },
)
TranscriptFilterUnionTypeDef = Union[TranscriptFilterTypeDef, TranscriptFilterOutputTypeDef]
GetMedicalScribeJobResponseTypeDef = TypedDict(
    "GetMedicalScribeJobResponseTypeDef",
    {
        "MedicalScribeJob": MedicalScribeJobTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartMedicalScribeJobResponseTypeDef = TypedDict(
    "StartMedicalScribeJobResponseTypeDef",
    {
        "MedicalScribeJob": MedicalScribeJobTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMedicalTranscriptionJobResponseTypeDef = TypedDict(
    "GetMedicalTranscriptionJobResponseTypeDef",
    {
        "MedicalTranscriptionJob": MedicalTranscriptionJobTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartMedicalTranscriptionJobResponseTypeDef = TypedDict(
    "StartMedicalTranscriptionJobResponseTypeDef",
    {
        "MedicalTranscriptionJob": MedicalTranscriptionJobTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTranscriptionJobsResponseTypeDef = TypedDict(
    "ListTranscriptionJobsResponseTypeDef",
    {
        "Status": TranscriptionJobStatusType,
        "TranscriptionJobSummaries": List[TranscriptionJobSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetTranscriptionJobResponseTypeDef = TypedDict(
    "GetTranscriptionJobResponseTypeDef",
    {
        "TranscriptionJob": TranscriptionJobTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartTranscriptionJobResponseTypeDef = TypedDict(
    "StartTranscriptionJobResponseTypeDef",
    {
        "TranscriptionJob": TranscriptionJobTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartTranscriptionJobRequestRequestTypeDef = TypedDict(
    "StartTranscriptionJobRequestRequestTypeDef",
    {
        "TranscriptionJobName": str,
        "Media": MediaTypeDef,
        "LanguageCode": NotRequired[LanguageCodeType],
        "MediaSampleRateHertz": NotRequired[int],
        "MediaFormat": NotRequired[MediaFormatType],
        "OutputBucketName": NotRequired[str],
        "OutputKey": NotRequired[str],
        "OutputEncryptionKMSKeyId": NotRequired[str],
        "KMSEncryptionContext": NotRequired[Mapping[str, str]],
        "Settings": NotRequired[SettingsTypeDef],
        "ModelSettings": NotRequired[ModelSettingsTypeDef],
        "JobExecutionSettings": NotRequired[JobExecutionSettingsTypeDef],
        "ContentRedaction": NotRequired[ContentRedactionTypeDef],
        "IdentifyLanguage": NotRequired[bool],
        "IdentifyMultipleLanguages": NotRequired[bool],
        "LanguageOptions": NotRequired[Sequence[LanguageCodeType]],
        "Subtitles": NotRequired[SubtitlesTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "LanguageIdSettings": NotRequired[Mapping[LanguageCodeType, LanguageIdSettingsTypeDef]],
        "ToxicityDetection": NotRequired[Sequence[ToxicityDetectionSettingsUnionTypeDef]],
    },
)
ListCallAnalyticsJobsResponseTypeDef = TypedDict(
    "ListCallAnalyticsJobsResponseTypeDef",
    {
        "Status": CallAnalyticsJobStatusType,
        "CallAnalyticsJobSummaries": List[CallAnalyticsJobSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetCallAnalyticsJobResponseTypeDef = TypedDict(
    "GetCallAnalyticsJobResponseTypeDef",
    {
        "CallAnalyticsJob": CallAnalyticsJobTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartCallAnalyticsJobResponseTypeDef = TypedDict(
    "StartCallAnalyticsJobResponseTypeDef",
    {
        "CallAnalyticsJob": CallAnalyticsJobTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartCallAnalyticsJobRequestRequestTypeDef = TypedDict(
    "StartCallAnalyticsJobRequestRequestTypeDef",
    {
        "CallAnalyticsJobName": str,
        "Media": MediaTypeDef,
        "OutputLocation": NotRequired[str],
        "OutputEncryptionKMSKeyId": NotRequired[str],
        "DataAccessRoleArn": NotRequired[str],
        "Settings": NotRequired[CallAnalyticsJobSettingsTypeDef],
        "ChannelDefinitions": NotRequired[Sequence[ChannelDefinitionTypeDef]],
    },
)
CategoryPropertiesTypeDef = TypedDict(
    "CategoryPropertiesTypeDef",
    {
        "CategoryName": NotRequired[str],
        "Rules": NotRequired[List[RuleOutputTypeDef]],
        "CreateTime": NotRequired[datetime],
        "LastUpdateTime": NotRequired[datetime],
        "InputType": NotRequired[InputTypeType],
    },
)
RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "NonTalkTimeFilter": NotRequired[NonTalkTimeFilterTypeDef],
        "InterruptionFilter": NotRequired[InterruptionFilterTypeDef],
        "TranscriptFilter": NotRequired[TranscriptFilterUnionTypeDef],
        "SentimentFilter": NotRequired[SentimentFilterUnionTypeDef],
    },
)
CreateCallAnalyticsCategoryResponseTypeDef = TypedDict(
    "CreateCallAnalyticsCategoryResponseTypeDef",
    {
        "CategoryProperties": CategoryPropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCallAnalyticsCategoryResponseTypeDef = TypedDict(
    "GetCallAnalyticsCategoryResponseTypeDef",
    {
        "CategoryProperties": CategoryPropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCallAnalyticsCategoriesResponseTypeDef = TypedDict(
    "ListCallAnalyticsCategoriesResponseTypeDef",
    {
        "Categories": List[CategoryPropertiesTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateCallAnalyticsCategoryResponseTypeDef = TypedDict(
    "UpdateCallAnalyticsCategoryResponseTypeDef",
    {
        "CategoryProperties": CategoryPropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RuleUnionTypeDef = Union[RuleTypeDef, RuleOutputTypeDef]
UpdateCallAnalyticsCategoryRequestRequestTypeDef = TypedDict(
    "UpdateCallAnalyticsCategoryRequestRequestTypeDef",
    {
        "CategoryName": str,
        "Rules": Sequence[RuleTypeDef],
        "InputType": NotRequired[InputTypeType],
    },
)
CreateCallAnalyticsCategoryRequestRequestTypeDef = TypedDict(
    "CreateCallAnalyticsCategoryRequestRequestTypeDef",
    {
        "CategoryName": str,
        "Rules": Sequence[RuleUnionTypeDef],
        "InputType": NotRequired[InputTypeType],
    },
)
