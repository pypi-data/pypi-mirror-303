"""
Type annotations for elastic-inference service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elastic_inference/type_defs/)

Usage::

    ```python
    from mypy_boto3_elastic_inference.type_defs import AcceleratorTypeOfferingTypeDef

    data: AcceleratorTypeOfferingTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Mapping, Sequence

from .literals import LocationTypeType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "AcceleratorTypeOfferingTypeDef",
    "KeyValuePairTypeDef",
    "MemoryInfoTypeDef",
    "DescribeAcceleratorOfferingsRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "FilterTypeDef",
    "PaginatorConfigTypeDef",
    "ElasticInferenceAcceleratorHealthTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "AcceleratorTypeTypeDef",
    "DescribeAcceleratorOfferingsResponseTypeDef",
    "ListTagsForResourceResultTypeDef",
    "DescribeAcceleratorsRequestRequestTypeDef",
    "DescribeAcceleratorsRequestDescribeAcceleratorsPaginateTypeDef",
    "ElasticInferenceAcceleratorTypeDef",
    "DescribeAcceleratorTypesResponseTypeDef",
    "DescribeAcceleratorsResponseTypeDef",
)

AcceleratorTypeOfferingTypeDef = TypedDict(
    "AcceleratorTypeOfferingTypeDef",
    {
        "acceleratorType": NotRequired[str],
        "locationType": NotRequired[LocationTypeType],
        "location": NotRequired[str],
    },
)
KeyValuePairTypeDef = TypedDict(
    "KeyValuePairTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[int],
    },
)
MemoryInfoTypeDef = TypedDict(
    "MemoryInfoTypeDef",
    {
        "sizeInMiB": NotRequired[int],
    },
)
DescribeAcceleratorOfferingsRequestRequestTypeDef = TypedDict(
    "DescribeAcceleratorOfferingsRequestRequestTypeDef",
    {
        "locationType": LocationTypeType,
        "acceleratorTypes": NotRequired[Sequence[str]],
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
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "name": NotRequired[str],
        "values": NotRequired[Sequence[str]],
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
ElasticInferenceAcceleratorHealthTypeDef = TypedDict(
    "ElasticInferenceAcceleratorHealthTypeDef",
    {
        "status": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
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
AcceleratorTypeTypeDef = TypedDict(
    "AcceleratorTypeTypeDef",
    {
        "acceleratorTypeName": NotRequired[str],
        "memoryInfo": NotRequired[MemoryInfoTypeDef],
        "throughputInfo": NotRequired[List[KeyValuePairTypeDef]],
    },
)
DescribeAcceleratorOfferingsResponseTypeDef = TypedDict(
    "DescribeAcceleratorOfferingsResponseTypeDef",
    {
        "acceleratorTypeOfferings": List[AcceleratorTypeOfferingTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAcceleratorsRequestRequestTypeDef = TypedDict(
    "DescribeAcceleratorsRequestRequestTypeDef",
    {
        "acceleratorIds": NotRequired[Sequence[str]],
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
DescribeAcceleratorsRequestDescribeAcceleratorsPaginateTypeDef = TypedDict(
    "DescribeAcceleratorsRequestDescribeAcceleratorsPaginateTypeDef",
    {
        "acceleratorIds": NotRequired[Sequence[str]],
        "filters": NotRequired[Sequence[FilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ElasticInferenceAcceleratorTypeDef = TypedDict(
    "ElasticInferenceAcceleratorTypeDef",
    {
        "acceleratorHealth": NotRequired[ElasticInferenceAcceleratorHealthTypeDef],
        "acceleratorType": NotRequired[str],
        "acceleratorId": NotRequired[str],
        "availabilityZone": NotRequired[str],
        "attachedResource": NotRequired[str],
    },
)
DescribeAcceleratorTypesResponseTypeDef = TypedDict(
    "DescribeAcceleratorTypesResponseTypeDef",
    {
        "acceleratorTypes": List[AcceleratorTypeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAcceleratorsResponseTypeDef = TypedDict(
    "DescribeAcceleratorsResponseTypeDef",
    {
        "acceleratorSet": List[ElasticInferenceAcceleratorTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
