"""
Type annotations for codeguru-reviewer service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/type_defs/)

Usage::

    ```python
    from mypy_boto3_codeguru_reviewer.type_defs import KMSKeyDetailsTypeDef

    data: KMSKeyDetailsTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AnalysisTypeType,
    ConfigFileStateType,
    EncryptionOptionType,
    JobStateType,
    ProviderTypeType,
    ReactionType,
    RecommendationCategoryType,
    RepositoryAssociationStateType,
    SeverityType,
    TypeType,
    VendorNameType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "KMSKeyDetailsTypeDef",
    "ResponseMetadataTypeDef",
    "BranchDiffSourceCodeTypeTypeDef",
    "CodeArtifactsTypeDef",
    "CodeCommitRepositoryTypeDef",
    "MetricsSummaryTypeDef",
    "MetricsTypeDef",
    "CommitDiffSourceCodeTypeTypeDef",
    "WaiterConfigTypeDef",
    "DescribeCodeReviewRequestRequestTypeDef",
    "DescribeRecommendationFeedbackRequestRequestTypeDef",
    "RecommendationFeedbackTypeDef",
    "DescribeRepositoryAssociationRequestRequestTypeDef",
    "DisassociateRepositoryRequestRequestTypeDef",
    "EventInfoTypeDef",
    "ListCodeReviewsRequestRequestTypeDef",
    "ListRecommendationFeedbackRequestRequestTypeDef",
    "RecommendationFeedbackSummaryTypeDef",
    "ListRecommendationsRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListRepositoryAssociationsRequestRequestTypeDef",
    "RepositoryAssociationSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "PutRecommendationFeedbackRequestRequestTypeDef",
    "RuleMetadataTypeDef",
    "RepositoryHeadSourceCodeTypeTypeDef",
    "S3RepositoryTypeDef",
    "ThirdPartySourceRepositoryTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "S3RepositoryDetailsTypeDef",
    "DescribeCodeReviewRequestCodeReviewCompletedWaitTypeDef",
    "DescribeRepositoryAssociationRequestRepositoryAssociationSucceededWaitTypeDef",
    "DescribeRecommendationFeedbackResponseTypeDef",
    "RequestMetadataTypeDef",
    "ListRecommendationFeedbackResponseTypeDef",
    "ListRepositoryAssociationsRequestListRepositoryAssociationsPaginateTypeDef",
    "ListRepositoryAssociationsResponseTypeDef",
    "RecommendationSummaryTypeDef",
    "RepositoryTypeDef",
    "RepositoryAssociationTypeDef",
    "S3BucketRepositoryTypeDef",
    "ListRecommendationsResponseTypeDef",
    "AssociateRepositoryRequestRequestTypeDef",
    "AssociateRepositoryResponseTypeDef",
    "DescribeRepositoryAssociationResponseTypeDef",
    "DisassociateRepositoryResponseTypeDef",
    "SourceCodeTypeTypeDef",
    "CodeReviewSummaryTypeDef",
    "CodeReviewTypeDef",
    "RepositoryAnalysisTypeDef",
    "ListCodeReviewsResponseTypeDef",
    "CreateCodeReviewResponseTypeDef",
    "DescribeCodeReviewResponseTypeDef",
    "CodeReviewTypeTypeDef",
    "CreateCodeReviewRequestRequestTypeDef",
)

KMSKeyDetailsTypeDef = TypedDict(
    "KMSKeyDetailsTypeDef",
    {
        "KMSKeyId": NotRequired[str],
        "EncryptionOption": NotRequired[EncryptionOptionType],
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
BranchDiffSourceCodeTypeTypeDef = TypedDict(
    "BranchDiffSourceCodeTypeTypeDef",
    {
        "SourceBranchName": str,
        "DestinationBranchName": str,
    },
)
CodeArtifactsTypeDef = TypedDict(
    "CodeArtifactsTypeDef",
    {
        "SourceCodeArtifactsObjectKey": str,
        "BuildArtifactsObjectKey": NotRequired[str],
    },
)
CodeCommitRepositoryTypeDef = TypedDict(
    "CodeCommitRepositoryTypeDef",
    {
        "Name": str,
    },
)
MetricsSummaryTypeDef = TypedDict(
    "MetricsSummaryTypeDef",
    {
        "MeteredLinesOfCodeCount": NotRequired[int],
        "SuppressedLinesOfCodeCount": NotRequired[int],
        "FindingsCount": NotRequired[int],
    },
)
MetricsTypeDef = TypedDict(
    "MetricsTypeDef",
    {
        "MeteredLinesOfCodeCount": NotRequired[int],
        "SuppressedLinesOfCodeCount": NotRequired[int],
        "FindingsCount": NotRequired[int],
    },
)
CommitDiffSourceCodeTypeTypeDef = TypedDict(
    "CommitDiffSourceCodeTypeTypeDef",
    {
        "SourceCommit": NotRequired[str],
        "DestinationCommit": NotRequired[str],
        "MergeBaseCommit": NotRequired[str],
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
DescribeCodeReviewRequestRequestTypeDef = TypedDict(
    "DescribeCodeReviewRequestRequestTypeDef",
    {
        "CodeReviewArn": str,
    },
)
DescribeRecommendationFeedbackRequestRequestTypeDef = TypedDict(
    "DescribeRecommendationFeedbackRequestRequestTypeDef",
    {
        "CodeReviewArn": str,
        "RecommendationId": str,
        "UserId": NotRequired[str],
    },
)
RecommendationFeedbackTypeDef = TypedDict(
    "RecommendationFeedbackTypeDef",
    {
        "CodeReviewArn": NotRequired[str],
        "RecommendationId": NotRequired[str],
        "Reactions": NotRequired[List[ReactionType]],
        "UserId": NotRequired[str],
        "CreatedTimeStamp": NotRequired[datetime],
        "LastUpdatedTimeStamp": NotRequired[datetime],
    },
)
DescribeRepositoryAssociationRequestRequestTypeDef = TypedDict(
    "DescribeRepositoryAssociationRequestRequestTypeDef",
    {
        "AssociationArn": str,
    },
)
DisassociateRepositoryRequestRequestTypeDef = TypedDict(
    "DisassociateRepositoryRequestRequestTypeDef",
    {
        "AssociationArn": str,
    },
)
EventInfoTypeDef = TypedDict(
    "EventInfoTypeDef",
    {
        "Name": NotRequired[str],
        "State": NotRequired[str],
    },
)
ListCodeReviewsRequestRequestTypeDef = TypedDict(
    "ListCodeReviewsRequestRequestTypeDef",
    {
        "Type": TypeType,
        "ProviderTypes": NotRequired[Sequence[ProviderTypeType]],
        "States": NotRequired[Sequence[JobStateType]],
        "RepositoryNames": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListRecommendationFeedbackRequestRequestTypeDef = TypedDict(
    "ListRecommendationFeedbackRequestRequestTypeDef",
    {
        "CodeReviewArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "UserIds": NotRequired[Sequence[str]],
        "RecommendationIds": NotRequired[Sequence[str]],
    },
)
RecommendationFeedbackSummaryTypeDef = TypedDict(
    "RecommendationFeedbackSummaryTypeDef",
    {
        "RecommendationId": NotRequired[str],
        "Reactions": NotRequired[List[ReactionType]],
        "UserId": NotRequired[str],
    },
)
ListRecommendationsRequestRequestTypeDef = TypedDict(
    "ListRecommendationsRequestRequestTypeDef",
    {
        "CodeReviewArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
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
ListRepositoryAssociationsRequestRequestTypeDef = TypedDict(
    "ListRepositoryAssociationsRequestRequestTypeDef",
    {
        "ProviderTypes": NotRequired[Sequence[ProviderTypeType]],
        "States": NotRequired[Sequence[RepositoryAssociationStateType]],
        "Names": NotRequired[Sequence[str]],
        "Owners": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
RepositoryAssociationSummaryTypeDef = TypedDict(
    "RepositoryAssociationSummaryTypeDef",
    {
        "AssociationArn": NotRequired[str],
        "ConnectionArn": NotRequired[str],
        "LastUpdatedTimeStamp": NotRequired[datetime],
        "AssociationId": NotRequired[str],
        "Name": NotRequired[str],
        "Owner": NotRequired[str],
        "ProviderType": NotRequired[ProviderTypeType],
        "State": NotRequired[RepositoryAssociationStateType],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
PutRecommendationFeedbackRequestRequestTypeDef = TypedDict(
    "PutRecommendationFeedbackRequestRequestTypeDef",
    {
        "CodeReviewArn": str,
        "RecommendationId": str,
        "Reactions": Sequence[ReactionType],
    },
)
RuleMetadataTypeDef = TypedDict(
    "RuleMetadataTypeDef",
    {
        "RuleId": NotRequired[str],
        "RuleName": NotRequired[str],
        "ShortDescription": NotRequired[str],
        "LongDescription": NotRequired[str],
        "RuleTags": NotRequired[List[str]],
    },
)
RepositoryHeadSourceCodeTypeTypeDef = TypedDict(
    "RepositoryHeadSourceCodeTypeTypeDef",
    {
        "BranchName": str,
    },
)
S3RepositoryTypeDef = TypedDict(
    "S3RepositoryTypeDef",
    {
        "Name": str,
        "BucketName": str,
    },
)
ThirdPartySourceRepositoryTypeDef = TypedDict(
    "ThirdPartySourceRepositoryTypeDef",
    {
        "Name": str,
        "ConnectionArn": str,
        "Owner": str,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "Tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "TagKeys": Sequence[str],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
S3RepositoryDetailsTypeDef = TypedDict(
    "S3RepositoryDetailsTypeDef",
    {
        "BucketName": NotRequired[str],
        "CodeArtifacts": NotRequired[CodeArtifactsTypeDef],
    },
)
DescribeCodeReviewRequestCodeReviewCompletedWaitTypeDef = TypedDict(
    "DescribeCodeReviewRequestCodeReviewCompletedWaitTypeDef",
    {
        "CodeReviewArn": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeRepositoryAssociationRequestRepositoryAssociationSucceededWaitTypeDef = TypedDict(
    "DescribeRepositoryAssociationRequestRepositoryAssociationSucceededWaitTypeDef",
    {
        "AssociationArn": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeRecommendationFeedbackResponseTypeDef = TypedDict(
    "DescribeRecommendationFeedbackResponseTypeDef",
    {
        "RecommendationFeedback": RecommendationFeedbackTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RequestMetadataTypeDef = TypedDict(
    "RequestMetadataTypeDef",
    {
        "RequestId": NotRequired[str],
        "Requester": NotRequired[str],
        "EventInfo": NotRequired[EventInfoTypeDef],
        "VendorName": NotRequired[VendorNameType],
    },
)
ListRecommendationFeedbackResponseTypeDef = TypedDict(
    "ListRecommendationFeedbackResponseTypeDef",
    {
        "RecommendationFeedbackSummaries": List[RecommendationFeedbackSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListRepositoryAssociationsRequestListRepositoryAssociationsPaginateTypeDef = TypedDict(
    "ListRepositoryAssociationsRequestListRepositoryAssociationsPaginateTypeDef",
    {
        "ProviderTypes": NotRequired[Sequence[ProviderTypeType]],
        "States": NotRequired[Sequence[RepositoryAssociationStateType]],
        "Names": NotRequired[Sequence[str]],
        "Owners": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRepositoryAssociationsResponseTypeDef = TypedDict(
    "ListRepositoryAssociationsResponseTypeDef",
    {
        "RepositoryAssociationSummaries": List[RepositoryAssociationSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
RecommendationSummaryTypeDef = TypedDict(
    "RecommendationSummaryTypeDef",
    {
        "FilePath": NotRequired[str],
        "RecommendationId": NotRequired[str],
        "StartLine": NotRequired[int],
        "EndLine": NotRequired[int],
        "Description": NotRequired[str],
        "RecommendationCategory": NotRequired[RecommendationCategoryType],
        "RuleMetadata": NotRequired[RuleMetadataTypeDef],
        "Severity": NotRequired[SeverityType],
    },
)
RepositoryTypeDef = TypedDict(
    "RepositoryTypeDef",
    {
        "CodeCommit": NotRequired[CodeCommitRepositoryTypeDef],
        "Bitbucket": NotRequired[ThirdPartySourceRepositoryTypeDef],
        "GitHubEnterpriseServer": NotRequired[ThirdPartySourceRepositoryTypeDef],
        "S3Bucket": NotRequired[S3RepositoryTypeDef],
    },
)
RepositoryAssociationTypeDef = TypedDict(
    "RepositoryAssociationTypeDef",
    {
        "AssociationId": NotRequired[str],
        "AssociationArn": NotRequired[str],
        "ConnectionArn": NotRequired[str],
        "Name": NotRequired[str],
        "Owner": NotRequired[str],
        "ProviderType": NotRequired[ProviderTypeType],
        "State": NotRequired[RepositoryAssociationStateType],
        "StateReason": NotRequired[str],
        "LastUpdatedTimeStamp": NotRequired[datetime],
        "CreatedTimeStamp": NotRequired[datetime],
        "KMSKeyDetails": NotRequired[KMSKeyDetailsTypeDef],
        "S3RepositoryDetails": NotRequired[S3RepositoryDetailsTypeDef],
    },
)
S3BucketRepositoryTypeDef = TypedDict(
    "S3BucketRepositoryTypeDef",
    {
        "Name": str,
        "Details": NotRequired[S3RepositoryDetailsTypeDef],
    },
)
ListRecommendationsResponseTypeDef = TypedDict(
    "ListRecommendationsResponseTypeDef",
    {
        "RecommendationSummaries": List[RecommendationSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
AssociateRepositoryRequestRequestTypeDef = TypedDict(
    "AssociateRepositoryRequestRequestTypeDef",
    {
        "Repository": RepositoryTypeDef,
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "KMSKeyDetails": NotRequired[KMSKeyDetailsTypeDef],
    },
)
AssociateRepositoryResponseTypeDef = TypedDict(
    "AssociateRepositoryResponseTypeDef",
    {
        "RepositoryAssociation": RepositoryAssociationTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRepositoryAssociationResponseTypeDef = TypedDict(
    "DescribeRepositoryAssociationResponseTypeDef",
    {
        "RepositoryAssociation": RepositoryAssociationTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateRepositoryResponseTypeDef = TypedDict(
    "DisassociateRepositoryResponseTypeDef",
    {
        "RepositoryAssociation": RepositoryAssociationTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SourceCodeTypeTypeDef = TypedDict(
    "SourceCodeTypeTypeDef",
    {
        "CommitDiff": NotRequired[CommitDiffSourceCodeTypeTypeDef],
        "RepositoryHead": NotRequired[RepositoryHeadSourceCodeTypeTypeDef],
        "BranchDiff": NotRequired[BranchDiffSourceCodeTypeTypeDef],
        "S3BucketRepository": NotRequired[S3BucketRepositoryTypeDef],
        "RequestMetadata": NotRequired[RequestMetadataTypeDef],
    },
)
CodeReviewSummaryTypeDef = TypedDict(
    "CodeReviewSummaryTypeDef",
    {
        "Name": NotRequired[str],
        "CodeReviewArn": NotRequired[str],
        "RepositoryName": NotRequired[str],
        "Owner": NotRequired[str],
        "ProviderType": NotRequired[ProviderTypeType],
        "State": NotRequired[JobStateType],
        "CreatedTimeStamp": NotRequired[datetime],
        "LastUpdatedTimeStamp": NotRequired[datetime],
        "Type": NotRequired[TypeType],
        "PullRequestId": NotRequired[str],
        "MetricsSummary": NotRequired[MetricsSummaryTypeDef],
        "SourceCodeType": NotRequired[SourceCodeTypeTypeDef],
    },
)
CodeReviewTypeDef = TypedDict(
    "CodeReviewTypeDef",
    {
        "Name": NotRequired[str],
        "CodeReviewArn": NotRequired[str],
        "RepositoryName": NotRequired[str],
        "Owner": NotRequired[str],
        "ProviderType": NotRequired[ProviderTypeType],
        "State": NotRequired[JobStateType],
        "StateReason": NotRequired[str],
        "CreatedTimeStamp": NotRequired[datetime],
        "LastUpdatedTimeStamp": NotRequired[datetime],
        "Type": NotRequired[TypeType],
        "PullRequestId": NotRequired[str],
        "SourceCodeType": NotRequired[SourceCodeTypeTypeDef],
        "AssociationArn": NotRequired[str],
        "Metrics": NotRequired[MetricsTypeDef],
        "AnalysisTypes": NotRequired[List[AnalysisTypeType]],
        "ConfigFileState": NotRequired[ConfigFileStateType],
    },
)
RepositoryAnalysisTypeDef = TypedDict(
    "RepositoryAnalysisTypeDef",
    {
        "RepositoryHead": NotRequired[RepositoryHeadSourceCodeTypeTypeDef],
        "SourceCodeType": NotRequired[SourceCodeTypeTypeDef],
    },
)
ListCodeReviewsResponseTypeDef = TypedDict(
    "ListCodeReviewsResponseTypeDef",
    {
        "CodeReviewSummaries": List[CodeReviewSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateCodeReviewResponseTypeDef = TypedDict(
    "CreateCodeReviewResponseTypeDef",
    {
        "CodeReview": CodeReviewTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeCodeReviewResponseTypeDef = TypedDict(
    "DescribeCodeReviewResponseTypeDef",
    {
        "CodeReview": CodeReviewTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CodeReviewTypeTypeDef = TypedDict(
    "CodeReviewTypeTypeDef",
    {
        "RepositoryAnalysis": RepositoryAnalysisTypeDef,
        "AnalysisTypes": NotRequired[Sequence[AnalysisTypeType]],
    },
)
CreateCodeReviewRequestRequestTypeDef = TypedDict(
    "CreateCodeReviewRequestRequestTypeDef",
    {
        "Name": str,
        "RepositoryAssociationArn": str,
        "Type": CodeReviewTypeTypeDef,
        "ClientRequestToken": NotRequired[str],
    },
)
