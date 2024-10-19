"""
Type annotations for connect-contact-lens service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect_contact_lens/type_defs/)

Usage::

    ```python
    from mypy_boto3_connect_contact_lens.type_defs import PointOfInterestTypeDef

    data: PointOfInterestTypeDef = ...
    ```
"""

import sys
from typing import Dict, List

from .literals import (
    PostContactSummaryFailureCodeType,
    PostContactSummaryStatusType,
    SentimentValueType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "PointOfInterestTypeDef",
    "CharacterOffsetsTypeDef",
    "ListRealtimeContactAnalysisSegmentsRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "PostContactSummaryTypeDef",
    "CategoryDetailsTypeDef",
    "IssueDetectedTypeDef",
    "CategoriesTypeDef",
    "TranscriptTypeDef",
    "RealtimeContactAnalysisSegmentTypeDef",
    "ListRealtimeContactAnalysisSegmentsResponseTypeDef",
)

PointOfInterestTypeDef = TypedDict(
    "PointOfInterestTypeDef",
    {
        "BeginOffsetMillis": int,
        "EndOffsetMillis": int,
    },
)
CharacterOffsetsTypeDef = TypedDict(
    "CharacterOffsetsTypeDef",
    {
        "BeginOffsetChar": int,
        "EndOffsetChar": int,
    },
)
ListRealtimeContactAnalysisSegmentsRequestRequestTypeDef = TypedDict(
    "ListRealtimeContactAnalysisSegmentsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
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
PostContactSummaryTypeDef = TypedDict(
    "PostContactSummaryTypeDef",
    {
        "Status": PostContactSummaryStatusType,
        "Content": NotRequired[str],
        "FailureCode": NotRequired[PostContactSummaryFailureCodeType],
    },
)
CategoryDetailsTypeDef = TypedDict(
    "CategoryDetailsTypeDef",
    {
        "PointsOfInterest": List[PointOfInterestTypeDef],
    },
)
IssueDetectedTypeDef = TypedDict(
    "IssueDetectedTypeDef",
    {
        "CharacterOffsets": CharacterOffsetsTypeDef,
    },
)
CategoriesTypeDef = TypedDict(
    "CategoriesTypeDef",
    {
        "MatchedCategories": List[str],
        "MatchedDetails": Dict[str, CategoryDetailsTypeDef],
    },
)
TranscriptTypeDef = TypedDict(
    "TranscriptTypeDef",
    {
        "Id": str,
        "ParticipantId": str,
        "ParticipantRole": str,
        "Content": str,
        "BeginOffsetMillis": int,
        "EndOffsetMillis": int,
        "Sentiment": SentimentValueType,
        "IssuesDetected": NotRequired[List[IssueDetectedTypeDef]],
    },
)
RealtimeContactAnalysisSegmentTypeDef = TypedDict(
    "RealtimeContactAnalysisSegmentTypeDef",
    {
        "Transcript": NotRequired[TranscriptTypeDef],
        "Categories": NotRequired[CategoriesTypeDef],
        "PostContactSummary": NotRequired[PostContactSummaryTypeDef],
    },
)
ListRealtimeContactAnalysisSegmentsResponseTypeDef = TypedDict(
    "ListRealtimeContactAnalysisSegmentsResponseTypeDef",
    {
        "Segments": List[RealtimeContactAnalysisSegmentTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
