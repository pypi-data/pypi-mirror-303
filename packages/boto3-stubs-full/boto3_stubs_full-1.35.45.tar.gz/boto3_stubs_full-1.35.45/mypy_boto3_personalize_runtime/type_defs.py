"""
Type annotations for personalize-runtime service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_runtime/type_defs/)

Usage::

    ```python
    from mypy_boto3_personalize_runtime.type_defs import GetActionRecommendationsRequestRequestTypeDef

    data: GetActionRecommendationsRequestRequestTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Mapping, Sequence

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "GetActionRecommendationsRequestRequestTypeDef",
    "PredictedActionTypeDef",
    "ResponseMetadataTypeDef",
    "GetPersonalizedRankingRequestRequestTypeDef",
    "PredictedItemTypeDef",
    "PromotionTypeDef",
    "GetActionRecommendationsResponseTypeDef",
    "GetPersonalizedRankingResponseTypeDef",
    "GetRecommendationsResponseTypeDef",
    "GetRecommendationsRequestRequestTypeDef",
)

GetActionRecommendationsRequestRequestTypeDef = TypedDict(
    "GetActionRecommendationsRequestRequestTypeDef",
    {
        "campaignArn": NotRequired[str],
        "userId": NotRequired[str],
        "numResults": NotRequired[int],
        "filterArn": NotRequired[str],
        "filterValues": NotRequired[Mapping[str, str]],
    },
)
PredictedActionTypeDef = TypedDict(
    "PredictedActionTypeDef",
    {
        "actionId": NotRequired[str],
        "score": NotRequired[float],
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
GetPersonalizedRankingRequestRequestTypeDef = TypedDict(
    "GetPersonalizedRankingRequestRequestTypeDef",
    {
        "campaignArn": str,
        "inputList": Sequence[str],
        "userId": str,
        "context": NotRequired[Mapping[str, str]],
        "filterArn": NotRequired[str],
        "filterValues": NotRequired[Mapping[str, str]],
        "metadataColumns": NotRequired[Mapping[str, Sequence[str]]],
    },
)
PredictedItemTypeDef = TypedDict(
    "PredictedItemTypeDef",
    {
        "itemId": NotRequired[str],
        "score": NotRequired[float],
        "promotionName": NotRequired[str],
        "metadata": NotRequired[Dict[str, str]],
        "reason": NotRequired[List[str]],
    },
)
PromotionTypeDef = TypedDict(
    "PromotionTypeDef",
    {
        "name": NotRequired[str],
        "percentPromotedItems": NotRequired[int],
        "filterArn": NotRequired[str],
        "filterValues": NotRequired[Mapping[str, str]],
    },
)
GetActionRecommendationsResponseTypeDef = TypedDict(
    "GetActionRecommendationsResponseTypeDef",
    {
        "actionList": List[PredictedActionTypeDef],
        "recommendationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPersonalizedRankingResponseTypeDef = TypedDict(
    "GetPersonalizedRankingResponseTypeDef",
    {
        "personalizedRanking": List[PredictedItemTypeDef],
        "recommendationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRecommendationsResponseTypeDef = TypedDict(
    "GetRecommendationsResponseTypeDef",
    {
        "itemList": List[PredictedItemTypeDef],
        "recommendationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRecommendationsRequestRequestTypeDef = TypedDict(
    "GetRecommendationsRequestRequestTypeDef",
    {
        "campaignArn": NotRequired[str],
        "itemId": NotRequired[str],
        "userId": NotRequired[str],
        "numResults": NotRequired[int],
        "context": NotRequired[Mapping[str, str]],
        "filterArn": NotRequired[str],
        "filterValues": NotRequired[Mapping[str, str]],
        "recommenderArn": NotRequired[str],
        "promotions": NotRequired[Sequence[PromotionTypeDef]],
        "metadataColumns": NotRequired[Mapping[str, Sequence[str]]],
    },
)
