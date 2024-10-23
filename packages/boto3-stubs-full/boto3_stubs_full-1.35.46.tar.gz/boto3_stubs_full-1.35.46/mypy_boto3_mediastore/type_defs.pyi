"""
Type annotations for mediastore service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore/type_defs/)

Usage::

    ```python
    from mypy_boto3_mediastore.type_defs import ContainerTypeDef

    data: ContainerTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import ContainerLevelMetricsType, ContainerStatusType, MethodNameType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "ContainerTypeDef",
    "CorsRuleOutputTypeDef",
    "CorsRuleTypeDef",
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "DeleteContainerInputRequestTypeDef",
    "DeleteContainerPolicyInputRequestTypeDef",
    "DeleteCorsPolicyInputRequestTypeDef",
    "DeleteLifecyclePolicyInputRequestTypeDef",
    "DeleteMetricPolicyInputRequestTypeDef",
    "DescribeContainerInputRequestTypeDef",
    "GetContainerPolicyInputRequestTypeDef",
    "GetCorsPolicyInputRequestTypeDef",
    "GetLifecyclePolicyInputRequestTypeDef",
    "GetMetricPolicyInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListContainersInputRequestTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "MetricPolicyRuleTypeDef",
    "PutContainerPolicyInputRequestTypeDef",
    "PutLifecyclePolicyInputRequestTypeDef",
    "StartAccessLoggingInputRequestTypeDef",
    "StopAccessLoggingInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "CorsRuleUnionTypeDef",
    "CreateContainerInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "CreateContainerOutputTypeDef",
    "DescribeContainerOutputTypeDef",
    "GetContainerPolicyOutputTypeDef",
    "GetCorsPolicyOutputTypeDef",
    "GetLifecyclePolicyOutputTypeDef",
    "ListContainersOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListContainersInputListContainersPaginateTypeDef",
    "MetricPolicyOutputTypeDef",
    "MetricPolicyTypeDef",
    "PutCorsPolicyInputRequestTypeDef",
    "GetMetricPolicyOutputTypeDef",
    "PutMetricPolicyInputRequestTypeDef",
)

ContainerTypeDef = TypedDict(
    "ContainerTypeDef",
    {
        "Endpoint": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "ARN": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired[ContainerStatusType],
        "AccessLoggingEnabled": NotRequired[bool],
    },
)
CorsRuleOutputTypeDef = TypedDict(
    "CorsRuleOutputTypeDef",
    {
        "AllowedOrigins": List[str],
        "AllowedHeaders": List[str],
        "AllowedMethods": NotRequired[List[MethodNameType]],
        "MaxAgeSeconds": NotRequired[int],
        "ExposeHeaders": NotRequired[List[str]],
    },
)
CorsRuleTypeDef = TypedDict(
    "CorsRuleTypeDef",
    {
        "AllowedOrigins": Sequence[str],
        "AllowedHeaders": Sequence[str],
        "AllowedMethods": NotRequired[Sequence[MethodNameType]],
        "MaxAgeSeconds": NotRequired[int],
        "ExposeHeaders": NotRequired[Sequence[str]],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": NotRequired[str],
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
DeleteContainerInputRequestTypeDef = TypedDict(
    "DeleteContainerInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)
DeleteContainerPolicyInputRequestTypeDef = TypedDict(
    "DeleteContainerPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)
DeleteCorsPolicyInputRequestTypeDef = TypedDict(
    "DeleteCorsPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)
DeleteLifecyclePolicyInputRequestTypeDef = TypedDict(
    "DeleteLifecyclePolicyInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)
DeleteMetricPolicyInputRequestTypeDef = TypedDict(
    "DeleteMetricPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)
DescribeContainerInputRequestTypeDef = TypedDict(
    "DescribeContainerInputRequestTypeDef",
    {
        "ContainerName": NotRequired[str],
    },
)
GetContainerPolicyInputRequestTypeDef = TypedDict(
    "GetContainerPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)
GetCorsPolicyInputRequestTypeDef = TypedDict(
    "GetCorsPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)
GetLifecyclePolicyInputRequestTypeDef = TypedDict(
    "GetLifecyclePolicyInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)
GetMetricPolicyInputRequestTypeDef = TypedDict(
    "GetMetricPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
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
ListContainersInputRequestTypeDef = TypedDict(
    "ListContainersInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "Resource": str,
    },
)
MetricPolicyRuleTypeDef = TypedDict(
    "MetricPolicyRuleTypeDef",
    {
        "ObjectGroup": str,
        "ObjectGroupName": str,
    },
)
PutContainerPolicyInputRequestTypeDef = TypedDict(
    "PutContainerPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
        "Policy": str,
    },
)
PutLifecyclePolicyInputRequestTypeDef = TypedDict(
    "PutLifecyclePolicyInputRequestTypeDef",
    {
        "ContainerName": str,
        "LifecyclePolicy": str,
    },
)
StartAccessLoggingInputRequestTypeDef = TypedDict(
    "StartAccessLoggingInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)
StopAccessLoggingInputRequestTypeDef = TypedDict(
    "StopAccessLoggingInputRequestTypeDef",
    {
        "ContainerName": str,
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "Resource": str,
        "TagKeys": Sequence[str],
    },
)
CorsRuleUnionTypeDef = Union[CorsRuleTypeDef, CorsRuleOutputTypeDef]
CreateContainerInputRequestTypeDef = TypedDict(
    "CreateContainerInputRequestTypeDef",
    {
        "ContainerName": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "Resource": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CreateContainerOutputTypeDef = TypedDict(
    "CreateContainerOutputTypeDef",
    {
        "Container": ContainerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeContainerOutputTypeDef = TypedDict(
    "DescribeContainerOutputTypeDef",
    {
        "Container": ContainerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetContainerPolicyOutputTypeDef = TypedDict(
    "GetContainerPolicyOutputTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCorsPolicyOutputTypeDef = TypedDict(
    "GetCorsPolicyOutputTypeDef",
    {
        "CorsPolicy": List[CorsRuleOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLifecyclePolicyOutputTypeDef = TypedDict(
    "GetLifecyclePolicyOutputTypeDef",
    {
        "LifecyclePolicy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListContainersOutputTypeDef = TypedDict(
    "ListContainersOutputTypeDef",
    {
        "Containers": List[ContainerTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListContainersInputListContainersPaginateTypeDef = TypedDict(
    "ListContainersInputListContainersPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
MetricPolicyOutputTypeDef = TypedDict(
    "MetricPolicyOutputTypeDef",
    {
        "ContainerLevelMetrics": ContainerLevelMetricsType,
        "MetricPolicyRules": NotRequired[List[MetricPolicyRuleTypeDef]],
    },
)
MetricPolicyTypeDef = TypedDict(
    "MetricPolicyTypeDef",
    {
        "ContainerLevelMetrics": ContainerLevelMetricsType,
        "MetricPolicyRules": NotRequired[Sequence[MetricPolicyRuleTypeDef]],
    },
)
PutCorsPolicyInputRequestTypeDef = TypedDict(
    "PutCorsPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
        "CorsPolicy": Sequence[CorsRuleUnionTypeDef],
    },
)
GetMetricPolicyOutputTypeDef = TypedDict(
    "GetMetricPolicyOutputTypeDef",
    {
        "MetricPolicy": MetricPolicyOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutMetricPolicyInputRequestTypeDef = TypedDict(
    "PutMetricPolicyInputRequestTypeDef",
    {
        "ContainerName": str,
        "MetricPolicy": MetricPolicyTypeDef,
    },
)
