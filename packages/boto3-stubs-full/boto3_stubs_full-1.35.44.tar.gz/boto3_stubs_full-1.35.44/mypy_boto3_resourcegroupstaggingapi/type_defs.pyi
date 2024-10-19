"""
Type annotations for resourcegroupstaggingapi service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/type_defs/)

Usage::

    ```python
    from mypy_boto3_resourcegroupstaggingapi.type_defs import ComplianceDetailsTypeDef

    data: ComplianceDetailsTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Mapping, Sequence

from .literals import ErrorCodeType, GroupByAttributeType, TargetIdTypeType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "ComplianceDetailsTypeDef",
    "ResponseMetadataTypeDef",
    "FailureInfoTypeDef",
    "PaginatorConfigTypeDef",
    "GetComplianceSummaryInputRequestTypeDef",
    "SummaryTypeDef",
    "TagFilterTypeDef",
    "GetTagKeysInputRequestTypeDef",
    "GetTagValuesInputRequestTypeDef",
    "TagTypeDef",
    "StartReportCreationInputRequestTypeDef",
    "TagResourcesInputRequestTypeDef",
    "UntagResourcesInputRequestTypeDef",
    "DescribeReportCreationOutputTypeDef",
    "GetTagKeysOutputTypeDef",
    "GetTagValuesOutputTypeDef",
    "TagResourcesOutputTypeDef",
    "UntagResourcesOutputTypeDef",
    "GetComplianceSummaryInputGetComplianceSummaryPaginateTypeDef",
    "GetTagKeysInputGetTagKeysPaginateTypeDef",
    "GetTagValuesInputGetTagValuesPaginateTypeDef",
    "GetComplianceSummaryOutputTypeDef",
    "GetResourcesInputGetResourcesPaginateTypeDef",
    "GetResourcesInputRequestTypeDef",
    "ResourceTagMappingTypeDef",
    "GetResourcesOutputTypeDef",
)

ComplianceDetailsTypeDef = TypedDict(
    "ComplianceDetailsTypeDef",
    {
        "NoncompliantKeys": NotRequired[List[str]],
        "KeysWithNoncompliantValues": NotRequired[List[str]],
        "ComplianceStatus": NotRequired[bool],
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
FailureInfoTypeDef = TypedDict(
    "FailureInfoTypeDef",
    {
        "StatusCode": NotRequired[int],
        "ErrorCode": NotRequired[ErrorCodeType],
        "ErrorMessage": NotRequired[str],
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
GetComplianceSummaryInputRequestTypeDef = TypedDict(
    "GetComplianceSummaryInputRequestTypeDef",
    {
        "TargetIdFilters": NotRequired[Sequence[str]],
        "RegionFilters": NotRequired[Sequence[str]],
        "ResourceTypeFilters": NotRequired[Sequence[str]],
        "TagKeyFilters": NotRequired[Sequence[str]],
        "GroupBy": NotRequired[Sequence[GroupByAttributeType]],
        "MaxResults": NotRequired[int],
        "PaginationToken": NotRequired[str],
    },
)
SummaryTypeDef = TypedDict(
    "SummaryTypeDef",
    {
        "LastUpdated": NotRequired[str],
        "TargetId": NotRequired[str],
        "TargetIdType": NotRequired[TargetIdTypeType],
        "Region": NotRequired[str],
        "ResourceType": NotRequired[str],
        "NonCompliantResources": NotRequired[int],
    },
)
TagFilterTypeDef = TypedDict(
    "TagFilterTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)
GetTagKeysInputRequestTypeDef = TypedDict(
    "GetTagKeysInputRequestTypeDef",
    {
        "PaginationToken": NotRequired[str],
    },
)
GetTagValuesInputRequestTypeDef = TypedDict(
    "GetTagValuesInputRequestTypeDef",
    {
        "Key": str,
        "PaginationToken": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
StartReportCreationInputRequestTypeDef = TypedDict(
    "StartReportCreationInputRequestTypeDef",
    {
        "S3Bucket": str,
    },
)
TagResourcesInputRequestTypeDef = TypedDict(
    "TagResourcesInputRequestTypeDef",
    {
        "ResourceARNList": Sequence[str],
        "Tags": Mapping[str, str],
    },
)
UntagResourcesInputRequestTypeDef = TypedDict(
    "UntagResourcesInputRequestTypeDef",
    {
        "ResourceARNList": Sequence[str],
        "TagKeys": Sequence[str],
    },
)
DescribeReportCreationOutputTypeDef = TypedDict(
    "DescribeReportCreationOutputTypeDef",
    {
        "Status": str,
        "S3Location": str,
        "ErrorMessage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTagKeysOutputTypeDef = TypedDict(
    "GetTagKeysOutputTypeDef",
    {
        "PaginationToken": str,
        "TagKeys": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTagValuesOutputTypeDef = TypedDict(
    "GetTagValuesOutputTypeDef",
    {
        "PaginationToken": str,
        "TagValues": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourcesOutputTypeDef = TypedDict(
    "TagResourcesOutputTypeDef",
    {
        "FailedResourcesMap": Dict[str, FailureInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UntagResourcesOutputTypeDef = TypedDict(
    "UntagResourcesOutputTypeDef",
    {
        "FailedResourcesMap": Dict[str, FailureInfoTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetComplianceSummaryInputGetComplianceSummaryPaginateTypeDef = TypedDict(
    "GetComplianceSummaryInputGetComplianceSummaryPaginateTypeDef",
    {
        "TargetIdFilters": NotRequired[Sequence[str]],
        "RegionFilters": NotRequired[Sequence[str]],
        "ResourceTypeFilters": NotRequired[Sequence[str]],
        "TagKeyFilters": NotRequired[Sequence[str]],
        "GroupBy": NotRequired[Sequence[GroupByAttributeType]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetTagKeysInputGetTagKeysPaginateTypeDef = TypedDict(
    "GetTagKeysInputGetTagKeysPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetTagValuesInputGetTagValuesPaginateTypeDef = TypedDict(
    "GetTagValuesInputGetTagValuesPaginateTypeDef",
    {
        "Key": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetComplianceSummaryOutputTypeDef = TypedDict(
    "GetComplianceSummaryOutputTypeDef",
    {
        "SummaryList": List[SummaryTypeDef],
        "PaginationToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResourcesInputGetResourcesPaginateTypeDef = TypedDict(
    "GetResourcesInputGetResourcesPaginateTypeDef",
    {
        "TagFilters": NotRequired[Sequence[TagFilterTypeDef]],
        "TagsPerPage": NotRequired[int],
        "ResourceTypeFilters": NotRequired[Sequence[str]],
        "IncludeComplianceDetails": NotRequired[bool],
        "ExcludeCompliantResources": NotRequired[bool],
        "ResourceARNList": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetResourcesInputRequestTypeDef = TypedDict(
    "GetResourcesInputRequestTypeDef",
    {
        "PaginationToken": NotRequired[str],
        "TagFilters": NotRequired[Sequence[TagFilterTypeDef]],
        "ResourcesPerPage": NotRequired[int],
        "TagsPerPage": NotRequired[int],
        "ResourceTypeFilters": NotRequired[Sequence[str]],
        "IncludeComplianceDetails": NotRequired[bool],
        "ExcludeCompliantResources": NotRequired[bool],
        "ResourceARNList": NotRequired[Sequence[str]],
    },
)
ResourceTagMappingTypeDef = TypedDict(
    "ResourceTagMappingTypeDef",
    {
        "ResourceARN": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "ComplianceDetails": NotRequired[ComplianceDetailsTypeDef],
    },
)
GetResourcesOutputTypeDef = TypedDict(
    "GetResourcesOutputTypeDef",
    {
        "PaginationToken": str,
        "ResourceTagMappingList": List[ResourceTagMappingTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
