"""
Type annotations for rekognition service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/type_defs/)

Usage::

    ```python
    from mypy_boto3_rekognition.type_defs import AgeRangeTypeDef

    data: AgeRangeTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    AttributeType,
    BodyPartType,
    CelebrityRecognitionSortByType,
    ContentClassifierType,
    ContentModerationAggregateByType,
    ContentModerationSortByType,
    CustomizationFeatureType,
    DatasetStatusMessageCodeType,
    DatasetStatusType,
    DatasetTypeType,
    DetectLabelsFeatureNameType,
    EmotionNameType,
    FaceAttributesType,
    FaceSearchSortByType,
    GenderTypeType,
    KnownGenderTypeType,
    LabelDetectionAggregateByType,
    LabelDetectionSortByType,
    LandmarkTypeType,
    LivenessSessionStatusType,
    MediaAnalysisJobFailureCodeType,
    MediaAnalysisJobStatusType,
    OrientationCorrectionType,
    PersonTrackingSortByType,
    ProjectAutoUpdateType,
    ProjectStatusType,
    ProjectVersionStatusType,
    ProtectiveEquipmentTypeType,
    QualityFilterType,
    ReasonType,
    SegmentTypeType,
    StreamProcessorParameterToDeleteType,
    StreamProcessorStatusType,
    TechnicalCueTypeType,
    TextTypesType,
    UnsearchedFaceReasonType,
    UnsuccessfulFaceAssociationReasonType,
    UnsuccessfulFaceDeletionReasonType,
    UnsuccessfulFaceDisassociationReasonType,
    UserStatusType,
    VideoColorRangeType,
    VideoJobStatusType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AgeRangeTypeDef",
    "AssociateFacesRequestRequestTypeDef",
    "AssociatedFaceTypeDef",
    "ResponseMetadataTypeDef",
    "UnsuccessfulFaceAssociationTypeDef",
    "AudioMetadataTypeDef",
    "BoundingBoxTypeDef",
    "S3ObjectTypeDef",
    "BeardTypeDef",
    "BlackFrameTypeDef",
    "BlobTypeDef",
    "KnownGenderTypeDef",
    "EmotionTypeDef",
    "ImageQualityTypeDef",
    "LandmarkTypeDef",
    "PoseTypeDef",
    "SmileTypeDef",
    "ConnectedHomeSettingsForUpdateTypeDef",
    "ConnectedHomeSettingsOutputTypeDef",
    "ConnectedHomeSettingsTypeDef",
    "ContentTypeTypeDef",
    "ModerationLabelTypeDef",
    "OutputConfigTypeDef",
    "CoversBodyPartTypeDef",
    "CreateCollectionRequestRequestTypeDef",
    "LivenessOutputConfigTypeDef",
    "CreateProjectRequestRequestTypeDef",
    "StreamProcessorDataSharingPreferenceTypeDef",
    "StreamProcessorNotificationChannelTypeDef",
    "CreateUserRequestRequestTypeDef",
    "CustomizationFeatureContentModerationConfigTypeDef",
    "DatasetStatsTypeDef",
    "DatasetLabelStatsTypeDef",
    "DatasetMetadataTypeDef",
    "DeleteCollectionRequestRequestTypeDef",
    "DeleteDatasetRequestRequestTypeDef",
    "DeleteFacesRequestRequestTypeDef",
    "UnsuccessfulFaceDeletionTypeDef",
    "DeleteProjectPolicyRequestRequestTypeDef",
    "DeleteProjectRequestRequestTypeDef",
    "DeleteProjectVersionRequestRequestTypeDef",
    "DeleteStreamProcessorRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DescribeCollectionRequestRequestTypeDef",
    "DescribeDatasetRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "WaiterConfigTypeDef",
    "DescribeProjectVersionsRequestRequestTypeDef",
    "DescribeProjectsRequestRequestTypeDef",
    "DescribeStreamProcessorRequestRequestTypeDef",
    "DetectLabelsImageQualityTypeDef",
    "DominantColorTypeDef",
    "DetectLabelsImagePropertiesSettingsTypeDef",
    "GeneralLabelsSettingsTypeDef",
    "HumanLoopActivationOutputTypeDef",
    "ProtectiveEquipmentSummarizationAttributesTypeDef",
    "ProtectiveEquipmentSummaryTypeDef",
    "DetectionFilterTypeDef",
    "DisassociateFacesRequestRequestTypeDef",
    "DisassociatedFaceTypeDef",
    "UnsuccessfulFaceDisassociationTypeDef",
    "DistributeDatasetTypeDef",
    "EyeDirectionTypeDef",
    "EyeOpenTypeDef",
    "EyeglassesTypeDef",
    "FaceOccludedTypeDef",
    "GenderTypeDef",
    "MouthOpenTypeDef",
    "MustacheTypeDef",
    "SunglassesTypeDef",
    "FaceSearchSettingsTypeDef",
    "PointTypeDef",
    "GetCelebrityInfoRequestRequestTypeDef",
    "GetCelebrityRecognitionRequestRequestTypeDef",
    "VideoMetadataTypeDef",
    "GetContentModerationRequestMetadataTypeDef",
    "GetContentModerationRequestRequestTypeDef",
    "GetFaceDetectionRequestRequestTypeDef",
    "GetFaceLivenessSessionResultsRequestRequestTypeDef",
    "GetFaceSearchRequestRequestTypeDef",
    "GetLabelDetectionRequestMetadataTypeDef",
    "GetLabelDetectionRequestRequestTypeDef",
    "GetMediaAnalysisJobRequestRequestTypeDef",
    "MediaAnalysisJobFailureDetailsTypeDef",
    "MediaAnalysisOutputConfigTypeDef",
    "GetPersonTrackingRequestRequestTypeDef",
    "GetSegmentDetectionRequestRequestTypeDef",
    "SegmentTypeInfoTypeDef",
    "GetTextDetectionRequestRequestTypeDef",
    "HumanLoopDataAttributesTypeDef",
    "KinesisDataStreamTypeDef",
    "KinesisVideoStreamStartSelectorTypeDef",
    "KinesisVideoStreamTypeDef",
    "LabelAliasTypeDef",
    "LabelCategoryTypeDef",
    "ParentTypeDef",
    "ListCollectionsRequestRequestTypeDef",
    "ListDatasetEntriesRequestRequestTypeDef",
    "ListDatasetLabelsRequestRequestTypeDef",
    "ListFacesRequestRequestTypeDef",
    "ListMediaAnalysisJobsRequestRequestTypeDef",
    "ListProjectPoliciesRequestRequestTypeDef",
    "ProjectPolicyTypeDef",
    "ListStreamProcessorsRequestRequestTypeDef",
    "StreamProcessorTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListUsersRequestRequestTypeDef",
    "UserTypeDef",
    "MatchedUserTypeDef",
    "MediaAnalysisDetectModerationLabelsConfigTypeDef",
    "MediaAnalysisModelVersionsTypeDef",
    "NotificationChannelTypeDef",
    "PutProjectPolicyRequestRequestTypeDef",
    "S3DestinationTypeDef",
    "SearchFacesRequestRequestTypeDef",
    "SearchUsersRequestRequestTypeDef",
    "SearchedFaceTypeDef",
    "SearchedUserTypeDef",
    "ShotSegmentTypeDef",
    "TechnicalCueSegmentTypeDef",
    "StartProjectVersionRequestRequestTypeDef",
    "StartShotDetectionFilterTypeDef",
    "StreamProcessingStopSelectorTypeDef",
    "StopProjectVersionRequestRequestTypeDef",
    "StopStreamProcessorRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "CopyProjectVersionResponseTypeDef",
    "CreateCollectionResponseTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateFaceLivenessSessionResponseTypeDef",
    "CreateProjectResponseTypeDef",
    "CreateProjectVersionResponseTypeDef",
    "CreateStreamProcessorResponseTypeDef",
    "DeleteCollectionResponseTypeDef",
    "DeleteProjectResponseTypeDef",
    "DeleteProjectVersionResponseTypeDef",
    "DescribeCollectionResponseTypeDef",
    "ListCollectionsResponseTypeDef",
    "ListDatasetEntriesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PutProjectPolicyResponseTypeDef",
    "StartCelebrityRecognitionResponseTypeDef",
    "StartContentModerationResponseTypeDef",
    "StartFaceDetectionResponseTypeDef",
    "StartFaceSearchResponseTypeDef",
    "StartLabelDetectionResponseTypeDef",
    "StartMediaAnalysisJobResponseTypeDef",
    "StartPersonTrackingResponseTypeDef",
    "StartProjectVersionResponseTypeDef",
    "StartSegmentDetectionResponseTypeDef",
    "StartStreamProcessorResponseTypeDef",
    "StartTextDetectionResponseTypeDef",
    "StopProjectVersionResponseTypeDef",
    "AssociateFacesResponseTypeDef",
    "ComparedSourceImageFaceTypeDef",
    "FaceTypeDef",
    "AuditImageTypeDef",
    "GroundTruthManifestTypeDef",
    "MediaAnalysisInputTypeDef",
    "MediaAnalysisManifestSummaryTypeDef",
    "SummaryTypeDef",
    "VideoTypeDef",
    "StartTechnicalCueDetectionFilterTypeDef",
    "DatasetChangesTypeDef",
    "ImageTypeDef",
    "GetCelebrityInfoResponseTypeDef",
    "ComparedFaceTypeDef",
    "StreamProcessorSettingsForUpdateTypeDef",
    "ConnectedHomeSettingsUnionTypeDef",
    "ContentModerationDetectionTypeDef",
    "CopyProjectVersionRequestRequestTypeDef",
    "EquipmentDetectionTypeDef",
    "CreateFaceLivenessSessionRequestSettingsTypeDef",
    "CustomizationFeatureConfigTypeDef",
    "DatasetDescriptionTypeDef",
    "DatasetLabelDescriptionTypeDef",
    "ProjectDescriptionTypeDef",
    "DeleteFacesResponseTypeDef",
    "DescribeProjectVersionsRequestDescribeProjectVersionsPaginateTypeDef",
    "DescribeProjectsRequestDescribeProjectsPaginateTypeDef",
    "ListCollectionsRequestListCollectionsPaginateTypeDef",
    "ListDatasetEntriesRequestListDatasetEntriesPaginateTypeDef",
    "ListDatasetLabelsRequestListDatasetLabelsPaginateTypeDef",
    "ListFacesRequestListFacesPaginateTypeDef",
    "ListProjectPoliciesRequestListProjectPoliciesPaginateTypeDef",
    "ListStreamProcessorsRequestListStreamProcessorsPaginateTypeDef",
    "ListUsersRequestListUsersPaginateTypeDef",
    "DescribeProjectVersionsRequestProjectVersionRunningWaitTypeDef",
    "DescribeProjectVersionsRequestProjectVersionTrainingCompletedWaitTypeDef",
    "DetectLabelsImageBackgroundTypeDef",
    "DetectLabelsImageForegroundTypeDef",
    "InstanceTypeDef",
    "DetectLabelsSettingsTypeDef",
    "LabelDetectionSettingsTypeDef",
    "DetectModerationLabelsResponseTypeDef",
    "DisassociateFacesResponseTypeDef",
    "DistributeDatasetEntriesRequestRequestTypeDef",
    "FaceDetailTypeDef",
    "StreamProcessorSettingsOutputTypeDef",
    "GeometryTypeDef",
    "RegionOfInterestOutputTypeDef",
    "RegionOfInterestTypeDef",
    "HumanLoopConfigTypeDef",
    "StreamProcessingStartSelectorTypeDef",
    "StreamProcessorInputTypeDef",
    "ListProjectPoliciesResponseTypeDef",
    "ListStreamProcessorsResponseTypeDef",
    "ListUsersResponseTypeDef",
    "UserMatchTypeDef",
    "MediaAnalysisOperationsConfigTypeDef",
    "MediaAnalysisResultsTypeDef",
    "StreamProcessorOutputTypeDef",
    "SegmentDetectionTypeDef",
    "FaceMatchTypeDef",
    "ListFacesResponseTypeDef",
    "GetFaceLivenessSessionResultsResponseTypeDef",
    "AssetTypeDef",
    "DatasetSourceTypeDef",
    "EvaluationResultTypeDef",
    "StartCelebrityRecognitionRequestRequestTypeDef",
    "StartContentModerationRequestRequestTypeDef",
    "StartFaceDetectionRequestRequestTypeDef",
    "StartFaceSearchRequestRequestTypeDef",
    "StartPersonTrackingRequestRequestTypeDef",
    "StartSegmentDetectionFiltersTypeDef",
    "UpdateDatasetEntriesRequestRequestTypeDef",
    "CompareFacesRequestRequestTypeDef",
    "DetectCustomLabelsRequestRequestTypeDef",
    "DetectFacesRequestRequestTypeDef",
    "DetectProtectiveEquipmentRequestRequestTypeDef",
    "IndexFacesRequestRequestTypeDef",
    "RecognizeCelebritiesRequestRequestTypeDef",
    "SearchFacesByImageRequestRequestTypeDef",
    "SearchUsersByImageRequestRequestTypeDef",
    "CelebrityTypeDef",
    "CompareFacesMatchTypeDef",
    "StreamProcessorSettingsTypeDef",
    "GetContentModerationResponseTypeDef",
    "ProtectiveEquipmentBodyPartTypeDef",
    "CreateFaceLivenessSessionRequestRequestTypeDef",
    "DescribeDatasetResponseTypeDef",
    "ListDatasetLabelsResponseTypeDef",
    "DescribeProjectsResponseTypeDef",
    "DetectLabelsImagePropertiesTypeDef",
    "LabelTypeDef",
    "DetectLabelsRequestRequestTypeDef",
    "StartLabelDetectionRequestRequestTypeDef",
    "CelebrityDetailTypeDef",
    "DetectFacesResponseTypeDef",
    "FaceDetectionTypeDef",
    "FaceRecordTypeDef",
    "PersonDetailTypeDef",
    "SearchedFaceDetailsTypeDef",
    "UnindexedFaceTypeDef",
    "UnsearchedFaceTypeDef",
    "CustomLabelTypeDef",
    "TextDetectionTypeDef",
    "RegionOfInterestUnionTypeDef",
    "UpdateStreamProcessorRequestRequestTypeDef",
    "DetectModerationLabelsRequestRequestTypeDef",
    "StartStreamProcessorRequestRequestTypeDef",
    "SearchUsersResponseTypeDef",
    "StartMediaAnalysisJobRequestRequestTypeDef",
    "GetMediaAnalysisJobResponseTypeDef",
    "MediaAnalysisJobDescriptionTypeDef",
    "DescribeStreamProcessorResponseTypeDef",
    "GetSegmentDetectionResponseTypeDef",
    "SearchFacesByImageResponseTypeDef",
    "SearchFacesResponseTypeDef",
    "TestingDataOutputTypeDef",
    "TestingDataTypeDef",
    "TrainingDataOutputTypeDef",
    "TrainingDataTypeDef",
    "ValidationDataTypeDef",
    "CreateDatasetRequestRequestTypeDef",
    "StartSegmentDetectionRequestRequestTypeDef",
    "RecognizeCelebritiesResponseTypeDef",
    "CompareFacesResponseTypeDef",
    "ProtectiveEquipmentPersonTypeDef",
    "DetectLabelsResponseTypeDef",
    "LabelDetectionTypeDef",
    "CelebrityRecognitionTypeDef",
    "GetFaceDetectionResponseTypeDef",
    "PersonDetectionTypeDef",
    "PersonMatchTypeDef",
    "IndexFacesResponseTypeDef",
    "SearchUsersByImageResponseTypeDef",
    "DetectCustomLabelsResponseTypeDef",
    "DetectTextResponseTypeDef",
    "TextDetectionResultTypeDef",
    "CreateStreamProcessorRequestRequestTypeDef",
    "DetectTextFiltersTypeDef",
    "StartTextDetectionFiltersTypeDef",
    "ListMediaAnalysisJobsResponseTypeDef",
    "CreateProjectVersionRequestRequestTypeDef",
    "TestingDataResultTypeDef",
    "TrainingDataResultTypeDef",
    "DetectProtectiveEquipmentResponseTypeDef",
    "GetLabelDetectionResponseTypeDef",
    "GetCelebrityRecognitionResponseTypeDef",
    "GetPersonTrackingResponseTypeDef",
    "GetFaceSearchResponseTypeDef",
    "GetTextDetectionResponseTypeDef",
    "DetectTextRequestRequestTypeDef",
    "StartTextDetectionRequestRequestTypeDef",
    "ProjectVersionDescriptionTypeDef",
    "DescribeProjectVersionsResponseTypeDef",
)

AgeRangeTypeDef = TypedDict(
    "AgeRangeTypeDef",
    {
        "Low": NotRequired[int],
        "High": NotRequired[int],
    },
)
AssociateFacesRequestRequestTypeDef = TypedDict(
    "AssociateFacesRequestRequestTypeDef",
    {
        "CollectionId": str,
        "UserId": str,
        "FaceIds": Sequence[str],
        "UserMatchThreshold": NotRequired[float],
        "ClientRequestToken": NotRequired[str],
    },
)
AssociatedFaceTypeDef = TypedDict(
    "AssociatedFaceTypeDef",
    {
        "FaceId": NotRequired[str],
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
UnsuccessfulFaceAssociationTypeDef = TypedDict(
    "UnsuccessfulFaceAssociationTypeDef",
    {
        "FaceId": NotRequired[str],
        "UserId": NotRequired[str],
        "Confidence": NotRequired[float],
        "Reasons": NotRequired[List[UnsuccessfulFaceAssociationReasonType]],
    },
)
AudioMetadataTypeDef = TypedDict(
    "AudioMetadataTypeDef",
    {
        "Codec": NotRequired[str],
        "DurationMillis": NotRequired[int],
        "SampleRate": NotRequired[int],
        "NumberOfChannels": NotRequired[int],
    },
)
BoundingBoxTypeDef = TypedDict(
    "BoundingBoxTypeDef",
    {
        "Width": NotRequired[float],
        "Height": NotRequired[float],
        "Left": NotRequired[float],
        "Top": NotRequired[float],
    },
)
S3ObjectTypeDef = TypedDict(
    "S3ObjectTypeDef",
    {
        "Bucket": NotRequired[str],
        "Name": NotRequired[str],
        "Version": NotRequired[str],
    },
)
BeardTypeDef = TypedDict(
    "BeardTypeDef",
    {
        "Value": NotRequired[bool],
        "Confidence": NotRequired[float],
    },
)
BlackFrameTypeDef = TypedDict(
    "BlackFrameTypeDef",
    {
        "MaxPixelThreshold": NotRequired[float],
        "MinCoveragePercentage": NotRequired[float],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
KnownGenderTypeDef = TypedDict(
    "KnownGenderTypeDef",
    {
        "Type": NotRequired[KnownGenderTypeType],
    },
)
EmotionTypeDef = TypedDict(
    "EmotionTypeDef",
    {
        "Type": NotRequired[EmotionNameType],
        "Confidence": NotRequired[float],
    },
)
ImageQualityTypeDef = TypedDict(
    "ImageQualityTypeDef",
    {
        "Brightness": NotRequired[float],
        "Sharpness": NotRequired[float],
    },
)
LandmarkTypeDef = TypedDict(
    "LandmarkTypeDef",
    {
        "Type": NotRequired[LandmarkTypeType],
        "X": NotRequired[float],
        "Y": NotRequired[float],
    },
)
PoseTypeDef = TypedDict(
    "PoseTypeDef",
    {
        "Roll": NotRequired[float],
        "Yaw": NotRequired[float],
        "Pitch": NotRequired[float],
    },
)
SmileTypeDef = TypedDict(
    "SmileTypeDef",
    {
        "Value": NotRequired[bool],
        "Confidence": NotRequired[float],
    },
)
ConnectedHomeSettingsForUpdateTypeDef = TypedDict(
    "ConnectedHomeSettingsForUpdateTypeDef",
    {
        "Labels": NotRequired[Sequence[str]],
        "MinConfidence": NotRequired[float],
    },
)
ConnectedHomeSettingsOutputTypeDef = TypedDict(
    "ConnectedHomeSettingsOutputTypeDef",
    {
        "Labels": List[str],
        "MinConfidence": NotRequired[float],
    },
)
ConnectedHomeSettingsTypeDef = TypedDict(
    "ConnectedHomeSettingsTypeDef",
    {
        "Labels": Sequence[str],
        "MinConfidence": NotRequired[float],
    },
)
ContentTypeTypeDef = TypedDict(
    "ContentTypeTypeDef",
    {
        "Confidence": NotRequired[float],
        "Name": NotRequired[str],
    },
)
ModerationLabelTypeDef = TypedDict(
    "ModerationLabelTypeDef",
    {
        "Confidence": NotRequired[float],
        "Name": NotRequired[str],
        "ParentName": NotRequired[str],
        "TaxonomyLevel": NotRequired[int],
    },
)
OutputConfigTypeDef = TypedDict(
    "OutputConfigTypeDef",
    {
        "S3Bucket": NotRequired[str],
        "S3KeyPrefix": NotRequired[str],
    },
)
CoversBodyPartTypeDef = TypedDict(
    "CoversBodyPartTypeDef",
    {
        "Confidence": NotRequired[float],
        "Value": NotRequired[bool],
    },
)
CreateCollectionRequestRequestTypeDef = TypedDict(
    "CreateCollectionRequestRequestTypeDef",
    {
        "CollectionId": str,
        "Tags": NotRequired[Mapping[str, str]],
    },
)
LivenessOutputConfigTypeDef = TypedDict(
    "LivenessOutputConfigTypeDef",
    {
        "S3Bucket": str,
        "S3KeyPrefix": NotRequired[str],
    },
)
CreateProjectRequestRequestTypeDef = TypedDict(
    "CreateProjectRequestRequestTypeDef",
    {
        "ProjectName": str,
        "Feature": NotRequired[CustomizationFeatureType],
        "AutoUpdate": NotRequired[ProjectAutoUpdateType],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
StreamProcessorDataSharingPreferenceTypeDef = TypedDict(
    "StreamProcessorDataSharingPreferenceTypeDef",
    {
        "OptIn": bool,
    },
)
StreamProcessorNotificationChannelTypeDef = TypedDict(
    "StreamProcessorNotificationChannelTypeDef",
    {
        "SNSTopicArn": str,
    },
)
CreateUserRequestRequestTypeDef = TypedDict(
    "CreateUserRequestRequestTypeDef",
    {
        "CollectionId": str,
        "UserId": str,
        "ClientRequestToken": NotRequired[str],
    },
)
CustomizationFeatureContentModerationConfigTypeDef = TypedDict(
    "CustomizationFeatureContentModerationConfigTypeDef",
    {
        "ConfidenceThreshold": NotRequired[float],
    },
)
DatasetStatsTypeDef = TypedDict(
    "DatasetStatsTypeDef",
    {
        "LabeledEntries": NotRequired[int],
        "TotalEntries": NotRequired[int],
        "TotalLabels": NotRequired[int],
        "ErrorEntries": NotRequired[int],
    },
)
DatasetLabelStatsTypeDef = TypedDict(
    "DatasetLabelStatsTypeDef",
    {
        "EntryCount": NotRequired[int],
        "BoundingBoxCount": NotRequired[int],
    },
)
DatasetMetadataTypeDef = TypedDict(
    "DatasetMetadataTypeDef",
    {
        "CreationTimestamp": NotRequired[datetime],
        "DatasetType": NotRequired[DatasetTypeType],
        "DatasetArn": NotRequired[str],
        "Status": NotRequired[DatasetStatusType],
        "StatusMessage": NotRequired[str],
        "StatusMessageCode": NotRequired[DatasetStatusMessageCodeType],
    },
)
DeleteCollectionRequestRequestTypeDef = TypedDict(
    "DeleteCollectionRequestRequestTypeDef",
    {
        "CollectionId": str,
    },
)
DeleteDatasetRequestRequestTypeDef = TypedDict(
    "DeleteDatasetRequestRequestTypeDef",
    {
        "DatasetArn": str,
    },
)
DeleteFacesRequestRequestTypeDef = TypedDict(
    "DeleteFacesRequestRequestTypeDef",
    {
        "CollectionId": str,
        "FaceIds": Sequence[str],
    },
)
UnsuccessfulFaceDeletionTypeDef = TypedDict(
    "UnsuccessfulFaceDeletionTypeDef",
    {
        "FaceId": NotRequired[str],
        "UserId": NotRequired[str],
        "Reasons": NotRequired[List[UnsuccessfulFaceDeletionReasonType]],
    },
)
DeleteProjectPolicyRequestRequestTypeDef = TypedDict(
    "DeleteProjectPolicyRequestRequestTypeDef",
    {
        "ProjectArn": str,
        "PolicyName": str,
        "PolicyRevisionId": NotRequired[str],
    },
)
DeleteProjectRequestRequestTypeDef = TypedDict(
    "DeleteProjectRequestRequestTypeDef",
    {
        "ProjectArn": str,
    },
)
DeleteProjectVersionRequestRequestTypeDef = TypedDict(
    "DeleteProjectVersionRequestRequestTypeDef",
    {
        "ProjectVersionArn": str,
    },
)
DeleteStreamProcessorRequestRequestTypeDef = TypedDict(
    "DeleteStreamProcessorRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "CollectionId": str,
        "UserId": str,
        "ClientRequestToken": NotRequired[str],
    },
)
DescribeCollectionRequestRequestTypeDef = TypedDict(
    "DescribeCollectionRequestRequestTypeDef",
    {
        "CollectionId": str,
    },
)
DescribeDatasetRequestRequestTypeDef = TypedDict(
    "DescribeDatasetRequestRequestTypeDef",
    {
        "DatasetArn": str,
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
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
DescribeProjectVersionsRequestRequestTypeDef = TypedDict(
    "DescribeProjectVersionsRequestRequestTypeDef",
    {
        "ProjectArn": str,
        "VersionNames": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeProjectsRequestRequestTypeDef = TypedDict(
    "DescribeProjectsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ProjectNames": NotRequired[Sequence[str]],
        "Features": NotRequired[Sequence[CustomizationFeatureType]],
    },
)
DescribeStreamProcessorRequestRequestTypeDef = TypedDict(
    "DescribeStreamProcessorRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DetectLabelsImageQualityTypeDef = TypedDict(
    "DetectLabelsImageQualityTypeDef",
    {
        "Brightness": NotRequired[float],
        "Sharpness": NotRequired[float],
        "Contrast": NotRequired[float],
    },
)
DominantColorTypeDef = TypedDict(
    "DominantColorTypeDef",
    {
        "Red": NotRequired[int],
        "Blue": NotRequired[int],
        "Green": NotRequired[int],
        "HexCode": NotRequired[str],
        "CSSColor": NotRequired[str],
        "SimplifiedColor": NotRequired[str],
        "PixelPercent": NotRequired[float],
    },
)
DetectLabelsImagePropertiesSettingsTypeDef = TypedDict(
    "DetectLabelsImagePropertiesSettingsTypeDef",
    {
        "MaxDominantColors": NotRequired[int],
    },
)
GeneralLabelsSettingsTypeDef = TypedDict(
    "GeneralLabelsSettingsTypeDef",
    {
        "LabelInclusionFilters": NotRequired[Sequence[str]],
        "LabelExclusionFilters": NotRequired[Sequence[str]],
        "LabelCategoryInclusionFilters": NotRequired[Sequence[str]],
        "LabelCategoryExclusionFilters": NotRequired[Sequence[str]],
    },
)
HumanLoopActivationOutputTypeDef = TypedDict(
    "HumanLoopActivationOutputTypeDef",
    {
        "HumanLoopArn": NotRequired[str],
        "HumanLoopActivationReasons": NotRequired[List[str]],
        "HumanLoopActivationConditionsEvaluationResults": NotRequired[str],
    },
)
ProtectiveEquipmentSummarizationAttributesTypeDef = TypedDict(
    "ProtectiveEquipmentSummarizationAttributesTypeDef",
    {
        "MinConfidence": float,
        "RequiredEquipmentTypes": Sequence[ProtectiveEquipmentTypeType],
    },
)
ProtectiveEquipmentSummaryTypeDef = TypedDict(
    "ProtectiveEquipmentSummaryTypeDef",
    {
        "PersonsWithRequiredEquipment": NotRequired[List[int]],
        "PersonsWithoutRequiredEquipment": NotRequired[List[int]],
        "PersonsIndeterminate": NotRequired[List[int]],
    },
)
DetectionFilterTypeDef = TypedDict(
    "DetectionFilterTypeDef",
    {
        "MinConfidence": NotRequired[float],
        "MinBoundingBoxHeight": NotRequired[float],
        "MinBoundingBoxWidth": NotRequired[float],
    },
)
DisassociateFacesRequestRequestTypeDef = TypedDict(
    "DisassociateFacesRequestRequestTypeDef",
    {
        "CollectionId": str,
        "UserId": str,
        "FaceIds": Sequence[str],
        "ClientRequestToken": NotRequired[str],
    },
)
DisassociatedFaceTypeDef = TypedDict(
    "DisassociatedFaceTypeDef",
    {
        "FaceId": NotRequired[str],
    },
)
UnsuccessfulFaceDisassociationTypeDef = TypedDict(
    "UnsuccessfulFaceDisassociationTypeDef",
    {
        "FaceId": NotRequired[str],
        "UserId": NotRequired[str],
        "Reasons": NotRequired[List[UnsuccessfulFaceDisassociationReasonType]],
    },
)
DistributeDatasetTypeDef = TypedDict(
    "DistributeDatasetTypeDef",
    {
        "Arn": str,
    },
)
EyeDirectionTypeDef = TypedDict(
    "EyeDirectionTypeDef",
    {
        "Yaw": NotRequired[float],
        "Pitch": NotRequired[float],
        "Confidence": NotRequired[float],
    },
)
EyeOpenTypeDef = TypedDict(
    "EyeOpenTypeDef",
    {
        "Value": NotRequired[bool],
        "Confidence": NotRequired[float],
    },
)
EyeglassesTypeDef = TypedDict(
    "EyeglassesTypeDef",
    {
        "Value": NotRequired[bool],
        "Confidence": NotRequired[float],
    },
)
FaceOccludedTypeDef = TypedDict(
    "FaceOccludedTypeDef",
    {
        "Value": NotRequired[bool],
        "Confidence": NotRequired[float],
    },
)
GenderTypeDef = TypedDict(
    "GenderTypeDef",
    {
        "Value": NotRequired[GenderTypeType],
        "Confidence": NotRequired[float],
    },
)
MouthOpenTypeDef = TypedDict(
    "MouthOpenTypeDef",
    {
        "Value": NotRequired[bool],
        "Confidence": NotRequired[float],
    },
)
MustacheTypeDef = TypedDict(
    "MustacheTypeDef",
    {
        "Value": NotRequired[bool],
        "Confidence": NotRequired[float],
    },
)
SunglassesTypeDef = TypedDict(
    "SunglassesTypeDef",
    {
        "Value": NotRequired[bool],
        "Confidence": NotRequired[float],
    },
)
FaceSearchSettingsTypeDef = TypedDict(
    "FaceSearchSettingsTypeDef",
    {
        "CollectionId": NotRequired[str],
        "FaceMatchThreshold": NotRequired[float],
    },
)
PointTypeDef = TypedDict(
    "PointTypeDef",
    {
        "X": NotRequired[float],
        "Y": NotRequired[float],
    },
)
GetCelebrityInfoRequestRequestTypeDef = TypedDict(
    "GetCelebrityInfoRequestRequestTypeDef",
    {
        "Id": str,
    },
)
GetCelebrityRecognitionRequestRequestTypeDef = TypedDict(
    "GetCelebrityRecognitionRequestRequestTypeDef",
    {
        "JobId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "SortBy": NotRequired[CelebrityRecognitionSortByType],
    },
)
VideoMetadataTypeDef = TypedDict(
    "VideoMetadataTypeDef",
    {
        "Codec": NotRequired[str],
        "DurationMillis": NotRequired[int],
        "Format": NotRequired[str],
        "FrameRate": NotRequired[float],
        "FrameHeight": NotRequired[int],
        "FrameWidth": NotRequired[int],
        "ColorRange": NotRequired[VideoColorRangeType],
    },
)
GetContentModerationRequestMetadataTypeDef = TypedDict(
    "GetContentModerationRequestMetadataTypeDef",
    {
        "SortBy": NotRequired[ContentModerationSortByType],
        "AggregateBy": NotRequired[ContentModerationAggregateByType],
    },
)
GetContentModerationRequestRequestTypeDef = TypedDict(
    "GetContentModerationRequestRequestTypeDef",
    {
        "JobId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "SortBy": NotRequired[ContentModerationSortByType],
        "AggregateBy": NotRequired[ContentModerationAggregateByType],
    },
)
GetFaceDetectionRequestRequestTypeDef = TypedDict(
    "GetFaceDetectionRequestRequestTypeDef",
    {
        "JobId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetFaceLivenessSessionResultsRequestRequestTypeDef = TypedDict(
    "GetFaceLivenessSessionResultsRequestRequestTypeDef",
    {
        "SessionId": str,
    },
)
GetFaceSearchRequestRequestTypeDef = TypedDict(
    "GetFaceSearchRequestRequestTypeDef",
    {
        "JobId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "SortBy": NotRequired[FaceSearchSortByType],
    },
)
GetLabelDetectionRequestMetadataTypeDef = TypedDict(
    "GetLabelDetectionRequestMetadataTypeDef",
    {
        "SortBy": NotRequired[LabelDetectionSortByType],
        "AggregateBy": NotRequired[LabelDetectionAggregateByType],
    },
)
GetLabelDetectionRequestRequestTypeDef = TypedDict(
    "GetLabelDetectionRequestRequestTypeDef",
    {
        "JobId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "SortBy": NotRequired[LabelDetectionSortByType],
        "AggregateBy": NotRequired[LabelDetectionAggregateByType],
    },
)
GetMediaAnalysisJobRequestRequestTypeDef = TypedDict(
    "GetMediaAnalysisJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
MediaAnalysisJobFailureDetailsTypeDef = TypedDict(
    "MediaAnalysisJobFailureDetailsTypeDef",
    {
        "Code": NotRequired[MediaAnalysisJobFailureCodeType],
        "Message": NotRequired[str],
    },
)
MediaAnalysisOutputConfigTypeDef = TypedDict(
    "MediaAnalysisOutputConfigTypeDef",
    {
        "S3Bucket": str,
        "S3KeyPrefix": NotRequired[str],
    },
)
GetPersonTrackingRequestRequestTypeDef = TypedDict(
    "GetPersonTrackingRequestRequestTypeDef",
    {
        "JobId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "SortBy": NotRequired[PersonTrackingSortByType],
    },
)
GetSegmentDetectionRequestRequestTypeDef = TypedDict(
    "GetSegmentDetectionRequestRequestTypeDef",
    {
        "JobId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
SegmentTypeInfoTypeDef = TypedDict(
    "SegmentTypeInfoTypeDef",
    {
        "Type": NotRequired[SegmentTypeType],
        "ModelVersion": NotRequired[str],
    },
)
GetTextDetectionRequestRequestTypeDef = TypedDict(
    "GetTextDetectionRequestRequestTypeDef",
    {
        "JobId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
HumanLoopDataAttributesTypeDef = TypedDict(
    "HumanLoopDataAttributesTypeDef",
    {
        "ContentClassifiers": NotRequired[Sequence[ContentClassifierType]],
    },
)
KinesisDataStreamTypeDef = TypedDict(
    "KinesisDataStreamTypeDef",
    {
        "Arn": NotRequired[str],
    },
)
KinesisVideoStreamStartSelectorTypeDef = TypedDict(
    "KinesisVideoStreamStartSelectorTypeDef",
    {
        "ProducerTimestamp": NotRequired[int],
        "FragmentNumber": NotRequired[str],
    },
)
KinesisVideoStreamTypeDef = TypedDict(
    "KinesisVideoStreamTypeDef",
    {
        "Arn": NotRequired[str],
    },
)
LabelAliasTypeDef = TypedDict(
    "LabelAliasTypeDef",
    {
        "Name": NotRequired[str],
    },
)
LabelCategoryTypeDef = TypedDict(
    "LabelCategoryTypeDef",
    {
        "Name": NotRequired[str],
    },
)
ParentTypeDef = TypedDict(
    "ParentTypeDef",
    {
        "Name": NotRequired[str],
    },
)
ListCollectionsRequestRequestTypeDef = TypedDict(
    "ListCollectionsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListDatasetEntriesRequestRequestTypeDef = TypedDict(
    "ListDatasetEntriesRequestRequestTypeDef",
    {
        "DatasetArn": str,
        "ContainsLabels": NotRequired[Sequence[str]],
        "Labeled": NotRequired[bool],
        "SourceRefContains": NotRequired[str],
        "HasErrors": NotRequired[bool],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListDatasetLabelsRequestRequestTypeDef = TypedDict(
    "ListDatasetLabelsRequestRequestTypeDef",
    {
        "DatasetArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListFacesRequestRequestTypeDef = TypedDict(
    "ListFacesRequestRequestTypeDef",
    {
        "CollectionId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "UserId": NotRequired[str],
        "FaceIds": NotRequired[Sequence[str]],
    },
)
ListMediaAnalysisJobsRequestRequestTypeDef = TypedDict(
    "ListMediaAnalysisJobsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListProjectPoliciesRequestRequestTypeDef = TypedDict(
    "ListProjectPoliciesRequestRequestTypeDef",
    {
        "ProjectArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ProjectPolicyTypeDef = TypedDict(
    "ProjectPolicyTypeDef",
    {
        "ProjectArn": NotRequired[str],
        "PolicyName": NotRequired[str],
        "PolicyRevisionId": NotRequired[str],
        "PolicyDocument": NotRequired[str],
        "CreationTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
    },
)
ListStreamProcessorsRequestRequestTypeDef = TypedDict(
    "ListStreamProcessorsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
StreamProcessorTypeDef = TypedDict(
    "StreamProcessorTypeDef",
    {
        "Name": NotRequired[str],
        "Status": NotRequired[StreamProcessorStatusType],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
ListUsersRequestRequestTypeDef = TypedDict(
    "ListUsersRequestRequestTypeDef",
    {
        "CollectionId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "UserId": NotRequired[str],
        "UserStatus": NotRequired[UserStatusType],
    },
)
MatchedUserTypeDef = TypedDict(
    "MatchedUserTypeDef",
    {
        "UserId": NotRequired[str],
        "UserStatus": NotRequired[UserStatusType],
    },
)
MediaAnalysisDetectModerationLabelsConfigTypeDef = TypedDict(
    "MediaAnalysisDetectModerationLabelsConfigTypeDef",
    {
        "MinConfidence": NotRequired[float],
        "ProjectVersion": NotRequired[str],
    },
)
MediaAnalysisModelVersionsTypeDef = TypedDict(
    "MediaAnalysisModelVersionsTypeDef",
    {
        "Moderation": NotRequired[str],
    },
)
NotificationChannelTypeDef = TypedDict(
    "NotificationChannelTypeDef",
    {
        "SNSTopicArn": str,
        "RoleArn": str,
    },
)
PutProjectPolicyRequestRequestTypeDef = TypedDict(
    "PutProjectPolicyRequestRequestTypeDef",
    {
        "ProjectArn": str,
        "PolicyName": str,
        "PolicyDocument": str,
        "PolicyRevisionId": NotRequired[str],
    },
)
S3DestinationTypeDef = TypedDict(
    "S3DestinationTypeDef",
    {
        "Bucket": NotRequired[str],
        "KeyPrefix": NotRequired[str],
    },
)
SearchFacesRequestRequestTypeDef = TypedDict(
    "SearchFacesRequestRequestTypeDef",
    {
        "CollectionId": str,
        "FaceId": str,
        "MaxFaces": NotRequired[int],
        "FaceMatchThreshold": NotRequired[float],
    },
)
SearchUsersRequestRequestTypeDef = TypedDict(
    "SearchUsersRequestRequestTypeDef",
    {
        "CollectionId": str,
        "UserId": NotRequired[str],
        "FaceId": NotRequired[str],
        "UserMatchThreshold": NotRequired[float],
        "MaxUsers": NotRequired[int],
    },
)
SearchedFaceTypeDef = TypedDict(
    "SearchedFaceTypeDef",
    {
        "FaceId": NotRequired[str],
    },
)
SearchedUserTypeDef = TypedDict(
    "SearchedUserTypeDef",
    {
        "UserId": NotRequired[str],
    },
)
ShotSegmentTypeDef = TypedDict(
    "ShotSegmentTypeDef",
    {
        "Index": NotRequired[int],
        "Confidence": NotRequired[float],
    },
)
TechnicalCueSegmentTypeDef = TypedDict(
    "TechnicalCueSegmentTypeDef",
    {
        "Type": NotRequired[TechnicalCueTypeType],
        "Confidence": NotRequired[float],
    },
)
StartProjectVersionRequestRequestTypeDef = TypedDict(
    "StartProjectVersionRequestRequestTypeDef",
    {
        "ProjectVersionArn": str,
        "MinInferenceUnits": int,
        "MaxInferenceUnits": NotRequired[int],
    },
)
StartShotDetectionFilterTypeDef = TypedDict(
    "StartShotDetectionFilterTypeDef",
    {
        "MinSegmentConfidence": NotRequired[float],
    },
)
StreamProcessingStopSelectorTypeDef = TypedDict(
    "StreamProcessingStopSelectorTypeDef",
    {
        "MaxDurationInSeconds": NotRequired[int],
    },
)
StopProjectVersionRequestRequestTypeDef = TypedDict(
    "StopProjectVersionRequestRequestTypeDef",
    {
        "ProjectVersionArn": str,
    },
)
StopStreamProcessorRequestRequestTypeDef = TypedDict(
    "StopStreamProcessorRequestRequestTypeDef",
    {
        "Name": str,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
CopyProjectVersionResponseTypeDef = TypedDict(
    "CopyProjectVersionResponseTypeDef",
    {
        "ProjectVersionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCollectionResponseTypeDef = TypedDict(
    "CreateCollectionResponseTypeDef",
    {
        "StatusCode": int,
        "CollectionArn": str,
        "FaceModelVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDatasetResponseTypeDef = TypedDict(
    "CreateDatasetResponseTypeDef",
    {
        "DatasetArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFaceLivenessSessionResponseTypeDef = TypedDict(
    "CreateFaceLivenessSessionResponseTypeDef",
    {
        "SessionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProjectResponseTypeDef = TypedDict(
    "CreateProjectResponseTypeDef",
    {
        "ProjectArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProjectVersionResponseTypeDef = TypedDict(
    "CreateProjectVersionResponseTypeDef",
    {
        "ProjectVersionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateStreamProcessorResponseTypeDef = TypedDict(
    "CreateStreamProcessorResponseTypeDef",
    {
        "StreamProcessorArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteCollectionResponseTypeDef = TypedDict(
    "DeleteCollectionResponseTypeDef",
    {
        "StatusCode": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteProjectResponseTypeDef = TypedDict(
    "DeleteProjectResponseTypeDef",
    {
        "Status": ProjectStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteProjectVersionResponseTypeDef = TypedDict(
    "DeleteProjectVersionResponseTypeDef",
    {
        "Status": ProjectVersionStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeCollectionResponseTypeDef = TypedDict(
    "DescribeCollectionResponseTypeDef",
    {
        "FaceCount": int,
        "FaceModelVersion": str,
        "CollectionARN": str,
        "CreationTimestamp": datetime,
        "UserCount": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCollectionsResponseTypeDef = TypedDict(
    "ListCollectionsResponseTypeDef",
    {
        "CollectionIds": List[str],
        "FaceModelVersions": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListDatasetEntriesResponseTypeDef = TypedDict(
    "ListDatasetEntriesResponseTypeDef",
    {
        "DatasetEntries": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutProjectPolicyResponseTypeDef = TypedDict(
    "PutProjectPolicyResponseTypeDef",
    {
        "PolicyRevisionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartCelebrityRecognitionResponseTypeDef = TypedDict(
    "StartCelebrityRecognitionResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartContentModerationResponseTypeDef = TypedDict(
    "StartContentModerationResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartFaceDetectionResponseTypeDef = TypedDict(
    "StartFaceDetectionResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartFaceSearchResponseTypeDef = TypedDict(
    "StartFaceSearchResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartLabelDetectionResponseTypeDef = TypedDict(
    "StartLabelDetectionResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartMediaAnalysisJobResponseTypeDef = TypedDict(
    "StartMediaAnalysisJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartPersonTrackingResponseTypeDef = TypedDict(
    "StartPersonTrackingResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartProjectVersionResponseTypeDef = TypedDict(
    "StartProjectVersionResponseTypeDef",
    {
        "Status": ProjectVersionStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartSegmentDetectionResponseTypeDef = TypedDict(
    "StartSegmentDetectionResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartStreamProcessorResponseTypeDef = TypedDict(
    "StartStreamProcessorResponseTypeDef",
    {
        "SessionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartTextDetectionResponseTypeDef = TypedDict(
    "StartTextDetectionResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopProjectVersionResponseTypeDef = TypedDict(
    "StopProjectVersionResponseTypeDef",
    {
        "Status": ProjectVersionStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateFacesResponseTypeDef = TypedDict(
    "AssociateFacesResponseTypeDef",
    {
        "AssociatedFaces": List[AssociatedFaceTypeDef],
        "UnsuccessfulFaceAssociations": List[UnsuccessfulFaceAssociationTypeDef],
        "UserStatus": UserStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ComparedSourceImageFaceTypeDef = TypedDict(
    "ComparedSourceImageFaceTypeDef",
    {
        "BoundingBox": NotRequired[BoundingBoxTypeDef],
        "Confidence": NotRequired[float],
    },
)
FaceTypeDef = TypedDict(
    "FaceTypeDef",
    {
        "FaceId": NotRequired[str],
        "BoundingBox": NotRequired[BoundingBoxTypeDef],
        "ImageId": NotRequired[str],
        "ExternalImageId": NotRequired[str],
        "Confidence": NotRequired[float],
        "IndexFacesModelVersion": NotRequired[str],
        "UserId": NotRequired[str],
    },
)
AuditImageTypeDef = TypedDict(
    "AuditImageTypeDef",
    {
        "Bytes": NotRequired[bytes],
        "S3Object": NotRequired[S3ObjectTypeDef],
        "BoundingBox": NotRequired[BoundingBoxTypeDef],
    },
)
GroundTruthManifestTypeDef = TypedDict(
    "GroundTruthManifestTypeDef",
    {
        "S3Object": NotRequired[S3ObjectTypeDef],
    },
)
MediaAnalysisInputTypeDef = TypedDict(
    "MediaAnalysisInputTypeDef",
    {
        "S3Object": S3ObjectTypeDef,
    },
)
MediaAnalysisManifestSummaryTypeDef = TypedDict(
    "MediaAnalysisManifestSummaryTypeDef",
    {
        "S3Object": NotRequired[S3ObjectTypeDef],
    },
)
SummaryTypeDef = TypedDict(
    "SummaryTypeDef",
    {
        "S3Object": NotRequired[S3ObjectTypeDef],
    },
)
VideoTypeDef = TypedDict(
    "VideoTypeDef",
    {
        "S3Object": NotRequired[S3ObjectTypeDef],
    },
)
StartTechnicalCueDetectionFilterTypeDef = TypedDict(
    "StartTechnicalCueDetectionFilterTypeDef",
    {
        "MinSegmentConfidence": NotRequired[float],
        "BlackFrame": NotRequired[BlackFrameTypeDef],
    },
)
DatasetChangesTypeDef = TypedDict(
    "DatasetChangesTypeDef",
    {
        "GroundTruth": BlobTypeDef,
    },
)
ImageTypeDef = TypedDict(
    "ImageTypeDef",
    {
        "Bytes": NotRequired[BlobTypeDef],
        "S3Object": NotRequired[S3ObjectTypeDef],
    },
)
GetCelebrityInfoResponseTypeDef = TypedDict(
    "GetCelebrityInfoResponseTypeDef",
    {
        "Urls": List[str],
        "Name": str,
        "KnownGender": KnownGenderTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ComparedFaceTypeDef = TypedDict(
    "ComparedFaceTypeDef",
    {
        "BoundingBox": NotRequired[BoundingBoxTypeDef],
        "Confidence": NotRequired[float],
        "Landmarks": NotRequired[List[LandmarkTypeDef]],
        "Pose": NotRequired[PoseTypeDef],
        "Quality": NotRequired[ImageQualityTypeDef],
        "Emotions": NotRequired[List[EmotionTypeDef]],
        "Smile": NotRequired[SmileTypeDef],
    },
)
StreamProcessorSettingsForUpdateTypeDef = TypedDict(
    "StreamProcessorSettingsForUpdateTypeDef",
    {
        "ConnectedHomeForUpdate": NotRequired[ConnectedHomeSettingsForUpdateTypeDef],
    },
)
ConnectedHomeSettingsUnionTypeDef = Union[
    ConnectedHomeSettingsTypeDef, ConnectedHomeSettingsOutputTypeDef
]
ContentModerationDetectionTypeDef = TypedDict(
    "ContentModerationDetectionTypeDef",
    {
        "Timestamp": NotRequired[int],
        "ModerationLabel": NotRequired[ModerationLabelTypeDef],
        "StartTimestampMillis": NotRequired[int],
        "EndTimestampMillis": NotRequired[int],
        "DurationMillis": NotRequired[int],
        "ContentTypes": NotRequired[List[ContentTypeTypeDef]],
    },
)
CopyProjectVersionRequestRequestTypeDef = TypedDict(
    "CopyProjectVersionRequestRequestTypeDef",
    {
        "SourceProjectArn": str,
        "SourceProjectVersionArn": str,
        "DestinationProjectArn": str,
        "VersionName": str,
        "OutputConfig": OutputConfigTypeDef,
        "Tags": NotRequired[Mapping[str, str]],
        "KmsKeyId": NotRequired[str],
    },
)
EquipmentDetectionTypeDef = TypedDict(
    "EquipmentDetectionTypeDef",
    {
        "BoundingBox": NotRequired[BoundingBoxTypeDef],
        "Confidence": NotRequired[float],
        "Type": NotRequired[ProtectiveEquipmentTypeType],
        "CoversBodyPart": NotRequired[CoversBodyPartTypeDef],
    },
)
CreateFaceLivenessSessionRequestSettingsTypeDef = TypedDict(
    "CreateFaceLivenessSessionRequestSettingsTypeDef",
    {
        "OutputConfig": NotRequired[LivenessOutputConfigTypeDef],
        "AuditImagesLimit": NotRequired[int],
    },
)
CustomizationFeatureConfigTypeDef = TypedDict(
    "CustomizationFeatureConfigTypeDef",
    {
        "ContentModeration": NotRequired[CustomizationFeatureContentModerationConfigTypeDef],
    },
)
DatasetDescriptionTypeDef = TypedDict(
    "DatasetDescriptionTypeDef",
    {
        "CreationTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
        "Status": NotRequired[DatasetStatusType],
        "StatusMessage": NotRequired[str],
        "StatusMessageCode": NotRequired[DatasetStatusMessageCodeType],
        "DatasetStats": NotRequired[DatasetStatsTypeDef],
    },
)
DatasetLabelDescriptionTypeDef = TypedDict(
    "DatasetLabelDescriptionTypeDef",
    {
        "LabelName": NotRequired[str],
        "LabelStats": NotRequired[DatasetLabelStatsTypeDef],
    },
)
ProjectDescriptionTypeDef = TypedDict(
    "ProjectDescriptionTypeDef",
    {
        "ProjectArn": NotRequired[str],
        "CreationTimestamp": NotRequired[datetime],
        "Status": NotRequired[ProjectStatusType],
        "Datasets": NotRequired[List[DatasetMetadataTypeDef]],
        "Feature": NotRequired[CustomizationFeatureType],
        "AutoUpdate": NotRequired[ProjectAutoUpdateType],
    },
)
DeleteFacesResponseTypeDef = TypedDict(
    "DeleteFacesResponseTypeDef",
    {
        "DeletedFaces": List[str],
        "UnsuccessfulFaceDeletions": List[UnsuccessfulFaceDeletionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeProjectVersionsRequestDescribeProjectVersionsPaginateTypeDef = TypedDict(
    "DescribeProjectVersionsRequestDescribeProjectVersionsPaginateTypeDef",
    {
        "ProjectArn": str,
        "VersionNames": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeProjectsRequestDescribeProjectsPaginateTypeDef = TypedDict(
    "DescribeProjectsRequestDescribeProjectsPaginateTypeDef",
    {
        "ProjectNames": NotRequired[Sequence[str]],
        "Features": NotRequired[Sequence[CustomizationFeatureType]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCollectionsRequestListCollectionsPaginateTypeDef = TypedDict(
    "ListCollectionsRequestListCollectionsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDatasetEntriesRequestListDatasetEntriesPaginateTypeDef = TypedDict(
    "ListDatasetEntriesRequestListDatasetEntriesPaginateTypeDef",
    {
        "DatasetArn": str,
        "ContainsLabels": NotRequired[Sequence[str]],
        "Labeled": NotRequired[bool],
        "SourceRefContains": NotRequired[str],
        "HasErrors": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDatasetLabelsRequestListDatasetLabelsPaginateTypeDef = TypedDict(
    "ListDatasetLabelsRequestListDatasetLabelsPaginateTypeDef",
    {
        "DatasetArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFacesRequestListFacesPaginateTypeDef = TypedDict(
    "ListFacesRequestListFacesPaginateTypeDef",
    {
        "CollectionId": str,
        "UserId": NotRequired[str],
        "FaceIds": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProjectPoliciesRequestListProjectPoliciesPaginateTypeDef = TypedDict(
    "ListProjectPoliciesRequestListProjectPoliciesPaginateTypeDef",
    {
        "ProjectArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListStreamProcessorsRequestListStreamProcessorsPaginateTypeDef = TypedDict(
    "ListStreamProcessorsRequestListStreamProcessorsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListUsersRequestListUsersPaginateTypeDef = TypedDict(
    "ListUsersRequestListUsersPaginateTypeDef",
    {
        "CollectionId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeProjectVersionsRequestProjectVersionRunningWaitTypeDef = TypedDict(
    "DescribeProjectVersionsRequestProjectVersionRunningWaitTypeDef",
    {
        "ProjectArn": str,
        "VersionNames": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeProjectVersionsRequestProjectVersionTrainingCompletedWaitTypeDef = TypedDict(
    "DescribeProjectVersionsRequestProjectVersionTrainingCompletedWaitTypeDef",
    {
        "ProjectArn": str,
        "VersionNames": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DetectLabelsImageBackgroundTypeDef = TypedDict(
    "DetectLabelsImageBackgroundTypeDef",
    {
        "Quality": NotRequired[DetectLabelsImageQualityTypeDef],
        "DominantColors": NotRequired[List[DominantColorTypeDef]],
    },
)
DetectLabelsImageForegroundTypeDef = TypedDict(
    "DetectLabelsImageForegroundTypeDef",
    {
        "Quality": NotRequired[DetectLabelsImageQualityTypeDef],
        "DominantColors": NotRequired[List[DominantColorTypeDef]],
    },
)
InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "BoundingBox": NotRequired[BoundingBoxTypeDef],
        "Confidence": NotRequired[float],
        "DominantColors": NotRequired[List[DominantColorTypeDef]],
    },
)
DetectLabelsSettingsTypeDef = TypedDict(
    "DetectLabelsSettingsTypeDef",
    {
        "GeneralLabels": NotRequired[GeneralLabelsSettingsTypeDef],
        "ImageProperties": NotRequired[DetectLabelsImagePropertiesSettingsTypeDef],
    },
)
LabelDetectionSettingsTypeDef = TypedDict(
    "LabelDetectionSettingsTypeDef",
    {
        "GeneralLabels": NotRequired[GeneralLabelsSettingsTypeDef],
    },
)
DetectModerationLabelsResponseTypeDef = TypedDict(
    "DetectModerationLabelsResponseTypeDef",
    {
        "ModerationLabels": List[ModerationLabelTypeDef],
        "ModerationModelVersion": str,
        "HumanLoopActivationOutput": HumanLoopActivationOutputTypeDef,
        "ProjectVersion": str,
        "ContentTypes": List[ContentTypeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateFacesResponseTypeDef = TypedDict(
    "DisassociateFacesResponseTypeDef",
    {
        "DisassociatedFaces": List[DisassociatedFaceTypeDef],
        "UnsuccessfulFaceDisassociations": List[UnsuccessfulFaceDisassociationTypeDef],
        "UserStatus": UserStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DistributeDatasetEntriesRequestRequestTypeDef = TypedDict(
    "DistributeDatasetEntriesRequestRequestTypeDef",
    {
        "Datasets": Sequence[DistributeDatasetTypeDef],
    },
)
FaceDetailTypeDef = TypedDict(
    "FaceDetailTypeDef",
    {
        "BoundingBox": NotRequired[BoundingBoxTypeDef],
        "AgeRange": NotRequired[AgeRangeTypeDef],
        "Smile": NotRequired[SmileTypeDef],
        "Eyeglasses": NotRequired[EyeglassesTypeDef],
        "Sunglasses": NotRequired[SunglassesTypeDef],
        "Gender": NotRequired[GenderTypeDef],
        "Beard": NotRequired[BeardTypeDef],
        "Mustache": NotRequired[MustacheTypeDef],
        "EyesOpen": NotRequired[EyeOpenTypeDef],
        "MouthOpen": NotRequired[MouthOpenTypeDef],
        "Emotions": NotRequired[List[EmotionTypeDef]],
        "Landmarks": NotRequired[List[LandmarkTypeDef]],
        "Pose": NotRequired[PoseTypeDef],
        "Quality": NotRequired[ImageQualityTypeDef],
        "Confidence": NotRequired[float],
        "FaceOccluded": NotRequired[FaceOccludedTypeDef],
        "EyeDirection": NotRequired[EyeDirectionTypeDef],
    },
)
StreamProcessorSettingsOutputTypeDef = TypedDict(
    "StreamProcessorSettingsOutputTypeDef",
    {
        "FaceSearch": NotRequired[FaceSearchSettingsTypeDef],
        "ConnectedHome": NotRequired[ConnectedHomeSettingsOutputTypeDef],
    },
)
GeometryTypeDef = TypedDict(
    "GeometryTypeDef",
    {
        "BoundingBox": NotRequired[BoundingBoxTypeDef],
        "Polygon": NotRequired[List[PointTypeDef]],
    },
)
RegionOfInterestOutputTypeDef = TypedDict(
    "RegionOfInterestOutputTypeDef",
    {
        "BoundingBox": NotRequired[BoundingBoxTypeDef],
        "Polygon": NotRequired[List[PointTypeDef]],
    },
)
RegionOfInterestTypeDef = TypedDict(
    "RegionOfInterestTypeDef",
    {
        "BoundingBox": NotRequired[BoundingBoxTypeDef],
        "Polygon": NotRequired[Sequence[PointTypeDef]],
    },
)
HumanLoopConfigTypeDef = TypedDict(
    "HumanLoopConfigTypeDef",
    {
        "HumanLoopName": str,
        "FlowDefinitionArn": str,
        "DataAttributes": NotRequired[HumanLoopDataAttributesTypeDef],
    },
)
StreamProcessingStartSelectorTypeDef = TypedDict(
    "StreamProcessingStartSelectorTypeDef",
    {
        "KVSStreamStartSelector": NotRequired[KinesisVideoStreamStartSelectorTypeDef],
    },
)
StreamProcessorInputTypeDef = TypedDict(
    "StreamProcessorInputTypeDef",
    {
        "KinesisVideoStream": NotRequired[KinesisVideoStreamTypeDef],
    },
)
ListProjectPoliciesResponseTypeDef = TypedDict(
    "ListProjectPoliciesResponseTypeDef",
    {
        "ProjectPolicies": List[ProjectPolicyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListStreamProcessorsResponseTypeDef = TypedDict(
    "ListStreamProcessorsResponseTypeDef",
    {
        "StreamProcessors": List[StreamProcessorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "Users": List[UserTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UserMatchTypeDef = TypedDict(
    "UserMatchTypeDef",
    {
        "Similarity": NotRequired[float],
        "User": NotRequired[MatchedUserTypeDef],
    },
)
MediaAnalysisOperationsConfigTypeDef = TypedDict(
    "MediaAnalysisOperationsConfigTypeDef",
    {
        "DetectModerationLabels": NotRequired[MediaAnalysisDetectModerationLabelsConfigTypeDef],
    },
)
MediaAnalysisResultsTypeDef = TypedDict(
    "MediaAnalysisResultsTypeDef",
    {
        "S3Object": NotRequired[S3ObjectTypeDef],
        "ModelVersions": NotRequired[MediaAnalysisModelVersionsTypeDef],
    },
)
StreamProcessorOutputTypeDef = TypedDict(
    "StreamProcessorOutputTypeDef",
    {
        "KinesisDataStream": NotRequired[KinesisDataStreamTypeDef],
        "S3Destination": NotRequired[S3DestinationTypeDef],
    },
)
SegmentDetectionTypeDef = TypedDict(
    "SegmentDetectionTypeDef",
    {
        "Type": NotRequired[SegmentTypeType],
        "StartTimestampMillis": NotRequired[int],
        "EndTimestampMillis": NotRequired[int],
        "DurationMillis": NotRequired[int],
        "StartTimecodeSMPTE": NotRequired[str],
        "EndTimecodeSMPTE": NotRequired[str],
        "DurationSMPTE": NotRequired[str],
        "TechnicalCueSegment": NotRequired[TechnicalCueSegmentTypeDef],
        "ShotSegment": NotRequired[ShotSegmentTypeDef],
        "StartFrameNumber": NotRequired[int],
        "EndFrameNumber": NotRequired[int],
        "DurationFrames": NotRequired[int],
    },
)
FaceMatchTypeDef = TypedDict(
    "FaceMatchTypeDef",
    {
        "Similarity": NotRequired[float],
        "Face": NotRequired[FaceTypeDef],
    },
)
ListFacesResponseTypeDef = TypedDict(
    "ListFacesResponseTypeDef",
    {
        "Faces": List[FaceTypeDef],
        "FaceModelVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetFaceLivenessSessionResultsResponseTypeDef = TypedDict(
    "GetFaceLivenessSessionResultsResponseTypeDef",
    {
        "SessionId": str,
        "Status": LivenessSessionStatusType,
        "Confidence": float,
        "ReferenceImage": AuditImageTypeDef,
        "AuditImages": List[AuditImageTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssetTypeDef = TypedDict(
    "AssetTypeDef",
    {
        "GroundTruthManifest": NotRequired[GroundTruthManifestTypeDef],
    },
)
DatasetSourceTypeDef = TypedDict(
    "DatasetSourceTypeDef",
    {
        "GroundTruthManifest": NotRequired[GroundTruthManifestTypeDef],
        "DatasetArn": NotRequired[str],
    },
)
EvaluationResultTypeDef = TypedDict(
    "EvaluationResultTypeDef",
    {
        "F1Score": NotRequired[float],
        "Summary": NotRequired[SummaryTypeDef],
    },
)
StartCelebrityRecognitionRequestRequestTypeDef = TypedDict(
    "StartCelebrityRecognitionRequestRequestTypeDef",
    {
        "Video": VideoTypeDef,
        "ClientRequestToken": NotRequired[str],
        "NotificationChannel": NotRequired[NotificationChannelTypeDef],
        "JobTag": NotRequired[str],
    },
)
StartContentModerationRequestRequestTypeDef = TypedDict(
    "StartContentModerationRequestRequestTypeDef",
    {
        "Video": VideoTypeDef,
        "MinConfidence": NotRequired[float],
        "ClientRequestToken": NotRequired[str],
        "NotificationChannel": NotRequired[NotificationChannelTypeDef],
        "JobTag": NotRequired[str],
    },
)
StartFaceDetectionRequestRequestTypeDef = TypedDict(
    "StartFaceDetectionRequestRequestTypeDef",
    {
        "Video": VideoTypeDef,
        "ClientRequestToken": NotRequired[str],
        "NotificationChannel": NotRequired[NotificationChannelTypeDef],
        "FaceAttributes": NotRequired[FaceAttributesType],
        "JobTag": NotRequired[str],
    },
)
StartFaceSearchRequestRequestTypeDef = TypedDict(
    "StartFaceSearchRequestRequestTypeDef",
    {
        "Video": VideoTypeDef,
        "CollectionId": str,
        "ClientRequestToken": NotRequired[str],
        "FaceMatchThreshold": NotRequired[float],
        "NotificationChannel": NotRequired[NotificationChannelTypeDef],
        "JobTag": NotRequired[str],
    },
)
StartPersonTrackingRequestRequestTypeDef = TypedDict(
    "StartPersonTrackingRequestRequestTypeDef",
    {
        "Video": VideoTypeDef,
        "ClientRequestToken": NotRequired[str],
        "NotificationChannel": NotRequired[NotificationChannelTypeDef],
        "JobTag": NotRequired[str],
    },
)
StartSegmentDetectionFiltersTypeDef = TypedDict(
    "StartSegmentDetectionFiltersTypeDef",
    {
        "TechnicalCueFilter": NotRequired[StartTechnicalCueDetectionFilterTypeDef],
        "ShotFilter": NotRequired[StartShotDetectionFilterTypeDef],
    },
)
UpdateDatasetEntriesRequestRequestTypeDef = TypedDict(
    "UpdateDatasetEntriesRequestRequestTypeDef",
    {
        "DatasetArn": str,
        "Changes": DatasetChangesTypeDef,
    },
)
CompareFacesRequestRequestTypeDef = TypedDict(
    "CompareFacesRequestRequestTypeDef",
    {
        "SourceImage": ImageTypeDef,
        "TargetImage": ImageTypeDef,
        "SimilarityThreshold": NotRequired[float],
        "QualityFilter": NotRequired[QualityFilterType],
    },
)
DetectCustomLabelsRequestRequestTypeDef = TypedDict(
    "DetectCustomLabelsRequestRequestTypeDef",
    {
        "ProjectVersionArn": str,
        "Image": ImageTypeDef,
        "MaxResults": NotRequired[int],
        "MinConfidence": NotRequired[float],
    },
)
DetectFacesRequestRequestTypeDef = TypedDict(
    "DetectFacesRequestRequestTypeDef",
    {
        "Image": ImageTypeDef,
        "Attributes": NotRequired[Sequence[AttributeType]],
    },
)
DetectProtectiveEquipmentRequestRequestTypeDef = TypedDict(
    "DetectProtectiveEquipmentRequestRequestTypeDef",
    {
        "Image": ImageTypeDef,
        "SummarizationAttributes": NotRequired[ProtectiveEquipmentSummarizationAttributesTypeDef],
    },
)
IndexFacesRequestRequestTypeDef = TypedDict(
    "IndexFacesRequestRequestTypeDef",
    {
        "CollectionId": str,
        "Image": ImageTypeDef,
        "ExternalImageId": NotRequired[str],
        "DetectionAttributes": NotRequired[Sequence[AttributeType]],
        "MaxFaces": NotRequired[int],
        "QualityFilter": NotRequired[QualityFilterType],
    },
)
RecognizeCelebritiesRequestRequestTypeDef = TypedDict(
    "RecognizeCelebritiesRequestRequestTypeDef",
    {
        "Image": ImageTypeDef,
    },
)
SearchFacesByImageRequestRequestTypeDef = TypedDict(
    "SearchFacesByImageRequestRequestTypeDef",
    {
        "CollectionId": str,
        "Image": ImageTypeDef,
        "MaxFaces": NotRequired[int],
        "FaceMatchThreshold": NotRequired[float],
        "QualityFilter": NotRequired[QualityFilterType],
    },
)
SearchUsersByImageRequestRequestTypeDef = TypedDict(
    "SearchUsersByImageRequestRequestTypeDef",
    {
        "CollectionId": str,
        "Image": ImageTypeDef,
        "UserMatchThreshold": NotRequired[float],
        "MaxUsers": NotRequired[int],
        "QualityFilter": NotRequired[QualityFilterType],
    },
)
CelebrityTypeDef = TypedDict(
    "CelebrityTypeDef",
    {
        "Urls": NotRequired[List[str]],
        "Name": NotRequired[str],
        "Id": NotRequired[str],
        "Face": NotRequired[ComparedFaceTypeDef],
        "MatchConfidence": NotRequired[float],
        "KnownGender": NotRequired[KnownGenderTypeDef],
    },
)
CompareFacesMatchTypeDef = TypedDict(
    "CompareFacesMatchTypeDef",
    {
        "Similarity": NotRequired[float],
        "Face": NotRequired[ComparedFaceTypeDef],
    },
)
StreamProcessorSettingsTypeDef = TypedDict(
    "StreamProcessorSettingsTypeDef",
    {
        "FaceSearch": NotRequired[FaceSearchSettingsTypeDef],
        "ConnectedHome": NotRequired[ConnectedHomeSettingsUnionTypeDef],
    },
)
GetContentModerationResponseTypeDef = TypedDict(
    "GetContentModerationResponseTypeDef",
    {
        "JobStatus": VideoJobStatusType,
        "StatusMessage": str,
        "VideoMetadata": VideoMetadataTypeDef,
        "ModerationLabels": List[ContentModerationDetectionTypeDef],
        "ModerationModelVersion": str,
        "JobId": str,
        "Video": VideoTypeDef,
        "JobTag": str,
        "GetRequestMetadata": GetContentModerationRequestMetadataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ProtectiveEquipmentBodyPartTypeDef = TypedDict(
    "ProtectiveEquipmentBodyPartTypeDef",
    {
        "Name": NotRequired[BodyPartType],
        "Confidence": NotRequired[float],
        "EquipmentDetections": NotRequired[List[EquipmentDetectionTypeDef]],
    },
)
CreateFaceLivenessSessionRequestRequestTypeDef = TypedDict(
    "CreateFaceLivenessSessionRequestRequestTypeDef",
    {
        "KmsKeyId": NotRequired[str],
        "Settings": NotRequired[CreateFaceLivenessSessionRequestSettingsTypeDef],
        "ClientRequestToken": NotRequired[str],
    },
)
DescribeDatasetResponseTypeDef = TypedDict(
    "DescribeDatasetResponseTypeDef",
    {
        "DatasetDescription": DatasetDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDatasetLabelsResponseTypeDef = TypedDict(
    "ListDatasetLabelsResponseTypeDef",
    {
        "DatasetLabelDescriptions": List[DatasetLabelDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeProjectsResponseTypeDef = TypedDict(
    "DescribeProjectsResponseTypeDef",
    {
        "ProjectDescriptions": List[ProjectDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DetectLabelsImagePropertiesTypeDef = TypedDict(
    "DetectLabelsImagePropertiesTypeDef",
    {
        "Quality": NotRequired[DetectLabelsImageQualityTypeDef],
        "DominantColors": NotRequired[List[DominantColorTypeDef]],
        "Foreground": NotRequired[DetectLabelsImageForegroundTypeDef],
        "Background": NotRequired[DetectLabelsImageBackgroundTypeDef],
    },
)
LabelTypeDef = TypedDict(
    "LabelTypeDef",
    {
        "Name": NotRequired[str],
        "Confidence": NotRequired[float],
        "Instances": NotRequired[List[InstanceTypeDef]],
        "Parents": NotRequired[List[ParentTypeDef]],
        "Aliases": NotRequired[List[LabelAliasTypeDef]],
        "Categories": NotRequired[List[LabelCategoryTypeDef]],
    },
)
DetectLabelsRequestRequestTypeDef = TypedDict(
    "DetectLabelsRequestRequestTypeDef",
    {
        "Image": ImageTypeDef,
        "MaxLabels": NotRequired[int],
        "MinConfidence": NotRequired[float],
        "Features": NotRequired[Sequence[DetectLabelsFeatureNameType]],
        "Settings": NotRequired[DetectLabelsSettingsTypeDef],
    },
)
StartLabelDetectionRequestRequestTypeDef = TypedDict(
    "StartLabelDetectionRequestRequestTypeDef",
    {
        "Video": VideoTypeDef,
        "ClientRequestToken": NotRequired[str],
        "MinConfidence": NotRequired[float],
        "NotificationChannel": NotRequired[NotificationChannelTypeDef],
        "JobTag": NotRequired[str],
        "Features": NotRequired[Sequence[Literal["GENERAL_LABELS"]]],
        "Settings": NotRequired[LabelDetectionSettingsTypeDef],
    },
)
CelebrityDetailTypeDef = TypedDict(
    "CelebrityDetailTypeDef",
    {
        "Urls": NotRequired[List[str]],
        "Name": NotRequired[str],
        "Id": NotRequired[str],
        "Confidence": NotRequired[float],
        "BoundingBox": NotRequired[BoundingBoxTypeDef],
        "Face": NotRequired[FaceDetailTypeDef],
        "KnownGender": NotRequired[KnownGenderTypeDef],
    },
)
DetectFacesResponseTypeDef = TypedDict(
    "DetectFacesResponseTypeDef",
    {
        "FaceDetails": List[FaceDetailTypeDef],
        "OrientationCorrection": OrientationCorrectionType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FaceDetectionTypeDef = TypedDict(
    "FaceDetectionTypeDef",
    {
        "Timestamp": NotRequired[int],
        "Face": NotRequired[FaceDetailTypeDef],
    },
)
FaceRecordTypeDef = TypedDict(
    "FaceRecordTypeDef",
    {
        "Face": NotRequired[FaceTypeDef],
        "FaceDetail": NotRequired[FaceDetailTypeDef],
    },
)
PersonDetailTypeDef = TypedDict(
    "PersonDetailTypeDef",
    {
        "Index": NotRequired[int],
        "BoundingBox": NotRequired[BoundingBoxTypeDef],
        "Face": NotRequired[FaceDetailTypeDef],
    },
)
SearchedFaceDetailsTypeDef = TypedDict(
    "SearchedFaceDetailsTypeDef",
    {
        "FaceDetail": NotRequired[FaceDetailTypeDef],
    },
)
UnindexedFaceTypeDef = TypedDict(
    "UnindexedFaceTypeDef",
    {
        "Reasons": NotRequired[List[ReasonType]],
        "FaceDetail": NotRequired[FaceDetailTypeDef],
    },
)
UnsearchedFaceTypeDef = TypedDict(
    "UnsearchedFaceTypeDef",
    {
        "FaceDetails": NotRequired[FaceDetailTypeDef],
        "Reasons": NotRequired[List[UnsearchedFaceReasonType]],
    },
)
CustomLabelTypeDef = TypedDict(
    "CustomLabelTypeDef",
    {
        "Name": NotRequired[str],
        "Confidence": NotRequired[float],
        "Geometry": NotRequired[GeometryTypeDef],
    },
)
TextDetectionTypeDef = TypedDict(
    "TextDetectionTypeDef",
    {
        "DetectedText": NotRequired[str],
        "Type": NotRequired[TextTypesType],
        "Id": NotRequired[int],
        "ParentId": NotRequired[int],
        "Confidence": NotRequired[float],
        "Geometry": NotRequired[GeometryTypeDef],
    },
)
RegionOfInterestUnionTypeDef = Union[RegionOfInterestTypeDef, RegionOfInterestOutputTypeDef]
UpdateStreamProcessorRequestRequestTypeDef = TypedDict(
    "UpdateStreamProcessorRequestRequestTypeDef",
    {
        "Name": str,
        "SettingsForUpdate": NotRequired[StreamProcessorSettingsForUpdateTypeDef],
        "RegionsOfInterestForUpdate": NotRequired[Sequence[RegionOfInterestTypeDef]],
        "DataSharingPreferenceForUpdate": NotRequired[StreamProcessorDataSharingPreferenceTypeDef],
        "ParametersToDelete": NotRequired[Sequence[StreamProcessorParameterToDeleteType]],
    },
)
DetectModerationLabelsRequestRequestTypeDef = TypedDict(
    "DetectModerationLabelsRequestRequestTypeDef",
    {
        "Image": ImageTypeDef,
        "MinConfidence": NotRequired[float],
        "HumanLoopConfig": NotRequired[HumanLoopConfigTypeDef],
        "ProjectVersion": NotRequired[str],
    },
)
StartStreamProcessorRequestRequestTypeDef = TypedDict(
    "StartStreamProcessorRequestRequestTypeDef",
    {
        "Name": str,
        "StartSelector": NotRequired[StreamProcessingStartSelectorTypeDef],
        "StopSelector": NotRequired[StreamProcessingStopSelectorTypeDef],
    },
)
SearchUsersResponseTypeDef = TypedDict(
    "SearchUsersResponseTypeDef",
    {
        "UserMatches": List[UserMatchTypeDef],
        "FaceModelVersion": str,
        "SearchedFace": SearchedFaceTypeDef,
        "SearchedUser": SearchedUserTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartMediaAnalysisJobRequestRequestTypeDef = TypedDict(
    "StartMediaAnalysisJobRequestRequestTypeDef",
    {
        "OperationsConfig": MediaAnalysisOperationsConfigTypeDef,
        "Input": MediaAnalysisInputTypeDef,
        "OutputConfig": MediaAnalysisOutputConfigTypeDef,
        "ClientRequestToken": NotRequired[str],
        "JobName": NotRequired[str],
        "KmsKeyId": NotRequired[str],
    },
)
GetMediaAnalysisJobResponseTypeDef = TypedDict(
    "GetMediaAnalysisJobResponseTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "OperationsConfig": MediaAnalysisOperationsConfigTypeDef,
        "Status": MediaAnalysisJobStatusType,
        "FailureDetails": MediaAnalysisJobFailureDetailsTypeDef,
        "CreationTimestamp": datetime,
        "CompletionTimestamp": datetime,
        "Input": MediaAnalysisInputTypeDef,
        "OutputConfig": MediaAnalysisOutputConfigTypeDef,
        "KmsKeyId": str,
        "Results": MediaAnalysisResultsTypeDef,
        "ManifestSummary": MediaAnalysisManifestSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MediaAnalysisJobDescriptionTypeDef = TypedDict(
    "MediaAnalysisJobDescriptionTypeDef",
    {
        "JobId": str,
        "OperationsConfig": MediaAnalysisOperationsConfigTypeDef,
        "Status": MediaAnalysisJobStatusType,
        "CreationTimestamp": datetime,
        "Input": MediaAnalysisInputTypeDef,
        "OutputConfig": MediaAnalysisOutputConfigTypeDef,
        "JobName": NotRequired[str],
        "FailureDetails": NotRequired[MediaAnalysisJobFailureDetailsTypeDef],
        "CompletionTimestamp": NotRequired[datetime],
        "KmsKeyId": NotRequired[str],
        "Results": NotRequired[MediaAnalysisResultsTypeDef],
        "ManifestSummary": NotRequired[MediaAnalysisManifestSummaryTypeDef],
    },
)
DescribeStreamProcessorResponseTypeDef = TypedDict(
    "DescribeStreamProcessorResponseTypeDef",
    {
        "Name": str,
        "StreamProcessorArn": str,
        "Status": StreamProcessorStatusType,
        "StatusMessage": str,
        "CreationTimestamp": datetime,
        "LastUpdateTimestamp": datetime,
        "Input": StreamProcessorInputTypeDef,
        "Output": StreamProcessorOutputTypeDef,
        "RoleArn": str,
        "Settings": StreamProcessorSettingsOutputTypeDef,
        "NotificationChannel": StreamProcessorNotificationChannelTypeDef,
        "KmsKeyId": str,
        "RegionsOfInterest": List[RegionOfInterestOutputTypeDef],
        "DataSharingPreference": StreamProcessorDataSharingPreferenceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSegmentDetectionResponseTypeDef = TypedDict(
    "GetSegmentDetectionResponseTypeDef",
    {
        "JobStatus": VideoJobStatusType,
        "StatusMessage": str,
        "VideoMetadata": List[VideoMetadataTypeDef],
        "AudioMetadata": List[AudioMetadataTypeDef],
        "Segments": List[SegmentDetectionTypeDef],
        "SelectedSegmentTypes": List[SegmentTypeInfoTypeDef],
        "JobId": str,
        "Video": VideoTypeDef,
        "JobTag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
SearchFacesByImageResponseTypeDef = TypedDict(
    "SearchFacesByImageResponseTypeDef",
    {
        "SearchedFaceBoundingBox": BoundingBoxTypeDef,
        "SearchedFaceConfidence": float,
        "FaceMatches": List[FaceMatchTypeDef],
        "FaceModelVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchFacesResponseTypeDef = TypedDict(
    "SearchFacesResponseTypeDef",
    {
        "SearchedFaceId": str,
        "FaceMatches": List[FaceMatchTypeDef],
        "FaceModelVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TestingDataOutputTypeDef = TypedDict(
    "TestingDataOutputTypeDef",
    {
        "Assets": NotRequired[List[AssetTypeDef]],
        "AutoCreate": NotRequired[bool],
    },
)
TestingDataTypeDef = TypedDict(
    "TestingDataTypeDef",
    {
        "Assets": NotRequired[Sequence[AssetTypeDef]],
        "AutoCreate": NotRequired[bool],
    },
)
TrainingDataOutputTypeDef = TypedDict(
    "TrainingDataOutputTypeDef",
    {
        "Assets": NotRequired[List[AssetTypeDef]],
    },
)
TrainingDataTypeDef = TypedDict(
    "TrainingDataTypeDef",
    {
        "Assets": NotRequired[Sequence[AssetTypeDef]],
    },
)
ValidationDataTypeDef = TypedDict(
    "ValidationDataTypeDef",
    {
        "Assets": NotRequired[List[AssetTypeDef]],
    },
)
CreateDatasetRequestRequestTypeDef = TypedDict(
    "CreateDatasetRequestRequestTypeDef",
    {
        "DatasetType": DatasetTypeType,
        "ProjectArn": str,
        "DatasetSource": NotRequired[DatasetSourceTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
StartSegmentDetectionRequestRequestTypeDef = TypedDict(
    "StartSegmentDetectionRequestRequestTypeDef",
    {
        "Video": VideoTypeDef,
        "SegmentTypes": Sequence[SegmentTypeType],
        "ClientRequestToken": NotRequired[str],
        "NotificationChannel": NotRequired[NotificationChannelTypeDef],
        "JobTag": NotRequired[str],
        "Filters": NotRequired[StartSegmentDetectionFiltersTypeDef],
    },
)
RecognizeCelebritiesResponseTypeDef = TypedDict(
    "RecognizeCelebritiesResponseTypeDef",
    {
        "CelebrityFaces": List[CelebrityTypeDef],
        "UnrecognizedFaces": List[ComparedFaceTypeDef],
        "OrientationCorrection": OrientationCorrectionType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CompareFacesResponseTypeDef = TypedDict(
    "CompareFacesResponseTypeDef",
    {
        "SourceImageFace": ComparedSourceImageFaceTypeDef,
        "FaceMatches": List[CompareFacesMatchTypeDef],
        "UnmatchedFaces": List[ComparedFaceTypeDef],
        "SourceImageOrientationCorrection": OrientationCorrectionType,
        "TargetImageOrientationCorrection": OrientationCorrectionType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProtectiveEquipmentPersonTypeDef = TypedDict(
    "ProtectiveEquipmentPersonTypeDef",
    {
        "BodyParts": NotRequired[List[ProtectiveEquipmentBodyPartTypeDef]],
        "BoundingBox": NotRequired[BoundingBoxTypeDef],
        "Confidence": NotRequired[float],
        "Id": NotRequired[int],
    },
)
DetectLabelsResponseTypeDef = TypedDict(
    "DetectLabelsResponseTypeDef",
    {
        "Labels": List[LabelTypeDef],
        "OrientationCorrection": OrientationCorrectionType,
        "LabelModelVersion": str,
        "ImageProperties": DetectLabelsImagePropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LabelDetectionTypeDef = TypedDict(
    "LabelDetectionTypeDef",
    {
        "Timestamp": NotRequired[int],
        "Label": NotRequired[LabelTypeDef],
        "StartTimestampMillis": NotRequired[int],
        "EndTimestampMillis": NotRequired[int],
        "DurationMillis": NotRequired[int],
    },
)
CelebrityRecognitionTypeDef = TypedDict(
    "CelebrityRecognitionTypeDef",
    {
        "Timestamp": NotRequired[int],
        "Celebrity": NotRequired[CelebrityDetailTypeDef],
    },
)
GetFaceDetectionResponseTypeDef = TypedDict(
    "GetFaceDetectionResponseTypeDef",
    {
        "JobStatus": VideoJobStatusType,
        "StatusMessage": str,
        "VideoMetadata": VideoMetadataTypeDef,
        "Faces": List[FaceDetectionTypeDef],
        "JobId": str,
        "Video": VideoTypeDef,
        "JobTag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PersonDetectionTypeDef = TypedDict(
    "PersonDetectionTypeDef",
    {
        "Timestamp": NotRequired[int],
        "Person": NotRequired[PersonDetailTypeDef],
    },
)
PersonMatchTypeDef = TypedDict(
    "PersonMatchTypeDef",
    {
        "Timestamp": NotRequired[int],
        "Person": NotRequired[PersonDetailTypeDef],
        "FaceMatches": NotRequired[List[FaceMatchTypeDef]],
    },
)
IndexFacesResponseTypeDef = TypedDict(
    "IndexFacesResponseTypeDef",
    {
        "FaceRecords": List[FaceRecordTypeDef],
        "OrientationCorrection": OrientationCorrectionType,
        "FaceModelVersion": str,
        "UnindexedFaces": List[UnindexedFaceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchUsersByImageResponseTypeDef = TypedDict(
    "SearchUsersByImageResponseTypeDef",
    {
        "UserMatches": List[UserMatchTypeDef],
        "FaceModelVersion": str,
        "SearchedFace": SearchedFaceDetailsTypeDef,
        "UnsearchedFaces": List[UnsearchedFaceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DetectCustomLabelsResponseTypeDef = TypedDict(
    "DetectCustomLabelsResponseTypeDef",
    {
        "CustomLabels": List[CustomLabelTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DetectTextResponseTypeDef = TypedDict(
    "DetectTextResponseTypeDef",
    {
        "TextDetections": List[TextDetectionTypeDef],
        "TextModelVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TextDetectionResultTypeDef = TypedDict(
    "TextDetectionResultTypeDef",
    {
        "Timestamp": NotRequired[int],
        "TextDetection": NotRequired[TextDetectionTypeDef],
    },
)
CreateStreamProcessorRequestRequestTypeDef = TypedDict(
    "CreateStreamProcessorRequestRequestTypeDef",
    {
        "Input": StreamProcessorInputTypeDef,
        "Output": StreamProcessorOutputTypeDef,
        "Name": str,
        "Settings": StreamProcessorSettingsTypeDef,
        "RoleArn": str,
        "Tags": NotRequired[Mapping[str, str]],
        "NotificationChannel": NotRequired[StreamProcessorNotificationChannelTypeDef],
        "KmsKeyId": NotRequired[str],
        "RegionsOfInterest": NotRequired[Sequence[RegionOfInterestUnionTypeDef]],
        "DataSharingPreference": NotRequired[StreamProcessorDataSharingPreferenceTypeDef],
    },
)
DetectTextFiltersTypeDef = TypedDict(
    "DetectTextFiltersTypeDef",
    {
        "WordFilter": NotRequired[DetectionFilterTypeDef],
        "RegionsOfInterest": NotRequired[Sequence[RegionOfInterestUnionTypeDef]],
    },
)
StartTextDetectionFiltersTypeDef = TypedDict(
    "StartTextDetectionFiltersTypeDef",
    {
        "WordFilter": NotRequired[DetectionFilterTypeDef],
        "RegionsOfInterest": NotRequired[Sequence[RegionOfInterestUnionTypeDef]],
    },
)
ListMediaAnalysisJobsResponseTypeDef = TypedDict(
    "ListMediaAnalysisJobsResponseTypeDef",
    {
        "MediaAnalysisJobs": List[MediaAnalysisJobDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateProjectVersionRequestRequestTypeDef = TypedDict(
    "CreateProjectVersionRequestRequestTypeDef",
    {
        "ProjectArn": str,
        "VersionName": str,
        "OutputConfig": OutputConfigTypeDef,
        "TrainingData": NotRequired[TrainingDataTypeDef],
        "TestingData": NotRequired[TestingDataTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
        "KmsKeyId": NotRequired[str],
        "VersionDescription": NotRequired[str],
        "FeatureConfig": NotRequired[CustomizationFeatureConfigTypeDef],
    },
)
TestingDataResultTypeDef = TypedDict(
    "TestingDataResultTypeDef",
    {
        "Input": NotRequired[TestingDataOutputTypeDef],
        "Output": NotRequired[TestingDataOutputTypeDef],
        "Validation": NotRequired[ValidationDataTypeDef],
    },
)
TrainingDataResultTypeDef = TypedDict(
    "TrainingDataResultTypeDef",
    {
        "Input": NotRequired[TrainingDataOutputTypeDef],
        "Output": NotRequired[TrainingDataOutputTypeDef],
        "Validation": NotRequired[ValidationDataTypeDef],
    },
)
DetectProtectiveEquipmentResponseTypeDef = TypedDict(
    "DetectProtectiveEquipmentResponseTypeDef",
    {
        "ProtectiveEquipmentModelVersion": str,
        "Persons": List[ProtectiveEquipmentPersonTypeDef],
        "Summary": ProtectiveEquipmentSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLabelDetectionResponseTypeDef = TypedDict(
    "GetLabelDetectionResponseTypeDef",
    {
        "JobStatus": VideoJobStatusType,
        "StatusMessage": str,
        "VideoMetadata": VideoMetadataTypeDef,
        "Labels": List[LabelDetectionTypeDef],
        "LabelModelVersion": str,
        "JobId": str,
        "Video": VideoTypeDef,
        "JobTag": str,
        "GetRequestMetadata": GetLabelDetectionRequestMetadataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetCelebrityRecognitionResponseTypeDef = TypedDict(
    "GetCelebrityRecognitionResponseTypeDef",
    {
        "JobStatus": VideoJobStatusType,
        "StatusMessage": str,
        "VideoMetadata": VideoMetadataTypeDef,
        "Celebrities": List[CelebrityRecognitionTypeDef],
        "JobId": str,
        "Video": VideoTypeDef,
        "JobTag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetPersonTrackingResponseTypeDef = TypedDict(
    "GetPersonTrackingResponseTypeDef",
    {
        "JobStatus": VideoJobStatusType,
        "StatusMessage": str,
        "VideoMetadata": VideoMetadataTypeDef,
        "Persons": List[PersonDetectionTypeDef],
        "JobId": str,
        "Video": VideoTypeDef,
        "JobTag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetFaceSearchResponseTypeDef = TypedDict(
    "GetFaceSearchResponseTypeDef",
    {
        "JobStatus": VideoJobStatusType,
        "StatusMessage": str,
        "VideoMetadata": VideoMetadataTypeDef,
        "Persons": List[PersonMatchTypeDef],
        "JobId": str,
        "Video": VideoTypeDef,
        "JobTag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetTextDetectionResponseTypeDef = TypedDict(
    "GetTextDetectionResponseTypeDef",
    {
        "JobStatus": VideoJobStatusType,
        "StatusMessage": str,
        "VideoMetadata": VideoMetadataTypeDef,
        "TextDetections": List[TextDetectionResultTypeDef],
        "TextModelVersion": str,
        "JobId": str,
        "Video": VideoTypeDef,
        "JobTag": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DetectTextRequestRequestTypeDef = TypedDict(
    "DetectTextRequestRequestTypeDef",
    {
        "Image": ImageTypeDef,
        "Filters": NotRequired[DetectTextFiltersTypeDef],
    },
)
StartTextDetectionRequestRequestTypeDef = TypedDict(
    "StartTextDetectionRequestRequestTypeDef",
    {
        "Video": VideoTypeDef,
        "ClientRequestToken": NotRequired[str],
        "NotificationChannel": NotRequired[NotificationChannelTypeDef],
        "JobTag": NotRequired[str],
        "Filters": NotRequired[StartTextDetectionFiltersTypeDef],
    },
)
ProjectVersionDescriptionTypeDef = TypedDict(
    "ProjectVersionDescriptionTypeDef",
    {
        "ProjectVersionArn": NotRequired[str],
        "CreationTimestamp": NotRequired[datetime],
        "MinInferenceUnits": NotRequired[int],
        "Status": NotRequired[ProjectVersionStatusType],
        "StatusMessage": NotRequired[str],
        "BillableTrainingTimeInSeconds": NotRequired[int],
        "TrainingEndTimestamp": NotRequired[datetime],
        "OutputConfig": NotRequired[OutputConfigTypeDef],
        "TrainingDataResult": NotRequired[TrainingDataResultTypeDef],
        "TestingDataResult": NotRequired[TestingDataResultTypeDef],
        "EvaluationResult": NotRequired[EvaluationResultTypeDef],
        "ManifestSummary": NotRequired[GroundTruthManifestTypeDef],
        "KmsKeyId": NotRequired[str],
        "MaxInferenceUnits": NotRequired[int],
        "SourceProjectVersionArn": NotRequired[str],
        "VersionDescription": NotRequired[str],
        "Feature": NotRequired[CustomizationFeatureType],
        "BaseModelVersion": NotRequired[str],
        "FeatureConfig": NotRequired[CustomizationFeatureConfigTypeDef],
    },
)
DescribeProjectVersionsResponseTypeDef = TypedDict(
    "DescribeProjectVersionsResponseTypeDef",
    {
        "ProjectVersionDescriptions": List[ProjectVersionDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
