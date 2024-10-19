"""
Type annotations for codecommit service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecommit/type_defs/)

Usage::

    ```python
    from mypy_boto3_codecommit.type_defs import ApprovalRuleEventMetadataTypeDef

    data: ApprovalRuleEventMetadataTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    ApprovalStateType,
    BatchGetRepositoriesErrorCodeEnumType,
    ChangeTypeEnumType,
    ConflictDetailLevelTypeEnumType,
    ConflictResolutionStrategyTypeEnumType,
    FileModeTypeEnumType,
    MergeOptionTypeEnumType,
    ObjectTypeEnumType,
    OrderEnumType,
    OverrideStatusType,
    PullRequestEventTypeType,
    PullRequestStatusEnumType,
    RelativeFileVersionEnumType,
    ReplacementTypeEnumType,
    RepositoryTriggerEventEnumType,
    SortByEnumType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "ApprovalRuleEventMetadataTypeDef",
    "ApprovalRuleOverriddenEventMetadataTypeDef",
    "ApprovalRuleTemplateTypeDef",
    "OriginApprovalRuleTemplateTypeDef",
    "ApprovalStateChangedEventMetadataTypeDef",
    "ApprovalTypeDef",
    "AssociateApprovalRuleTemplateWithRepositoryInputRequestTypeDef",
    "BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef",
    "BatchAssociateApprovalRuleTemplateWithRepositoriesInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "BatchDescribeMergeConflictsErrorTypeDef",
    "BatchDescribeMergeConflictsInputRequestTypeDef",
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef",
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesInputRequestTypeDef",
    "BatchGetCommitsErrorTypeDef",
    "BatchGetCommitsInputRequestTypeDef",
    "BatchGetRepositoriesErrorTypeDef",
    "BatchGetRepositoriesInputRequestTypeDef",
    "RepositoryMetadataTypeDef",
    "BlobMetadataTypeDef",
    "BlobTypeDef",
    "BranchInfoTypeDef",
    "CommentTypeDef",
    "LocationTypeDef",
    "UserInfoTypeDef",
    "FileModesTypeDef",
    "FileSizesTypeDef",
    "IsBinaryFileTypeDef",
    "MergeOperationsTypeDef",
    "ObjectTypesTypeDef",
    "DeleteFileEntryTypeDef",
    "SetFileModeEntryTypeDef",
    "CreateApprovalRuleTemplateInputRequestTypeDef",
    "CreateBranchInputRequestTypeDef",
    "FileMetadataTypeDef",
    "CreatePullRequestApprovalRuleInputRequestTypeDef",
    "TargetTypeDef",
    "CreateRepositoryInputRequestTypeDef",
    "DeleteApprovalRuleTemplateInputRequestTypeDef",
    "DeleteBranchInputRequestTypeDef",
    "DeleteCommentContentInputRequestTypeDef",
    "DeleteFileInputRequestTypeDef",
    "DeletePullRequestApprovalRuleInputRequestTypeDef",
    "DeleteRepositoryInputRequestTypeDef",
    "DescribeMergeConflictsInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribePullRequestEventsInputRequestTypeDef",
    "DisassociateApprovalRuleTemplateFromRepositoryInputRequestTypeDef",
    "EvaluatePullRequestApprovalRulesInputRequestTypeDef",
    "EvaluationTypeDef",
    "FileTypeDef",
    "FolderTypeDef",
    "GetApprovalRuleTemplateInputRequestTypeDef",
    "GetBlobInputRequestTypeDef",
    "GetBranchInputRequestTypeDef",
    "GetCommentInputRequestTypeDef",
    "GetCommentReactionsInputRequestTypeDef",
    "GetCommentsForComparedCommitInputRequestTypeDef",
    "GetCommentsForPullRequestInputRequestTypeDef",
    "GetCommitInputRequestTypeDef",
    "GetDifferencesInputRequestTypeDef",
    "GetFileInputRequestTypeDef",
    "GetFolderInputRequestTypeDef",
    "SubModuleTypeDef",
    "SymbolicLinkTypeDef",
    "GetMergeCommitInputRequestTypeDef",
    "GetMergeConflictsInputRequestTypeDef",
    "GetMergeOptionsInputRequestTypeDef",
    "GetPullRequestApprovalStatesInputRequestTypeDef",
    "GetPullRequestInputRequestTypeDef",
    "GetPullRequestOverrideStateInputRequestTypeDef",
    "GetRepositoryInputRequestTypeDef",
    "GetRepositoryTriggersInputRequestTypeDef",
    "RepositoryTriggerOutputTypeDef",
    "ListApprovalRuleTemplatesInputRequestTypeDef",
    "ListAssociatedApprovalRuleTemplatesForRepositoryInputRequestTypeDef",
    "ListBranchesInputRequestTypeDef",
    "ListFileCommitHistoryRequestRequestTypeDef",
    "ListPullRequestsInputRequestTypeDef",
    "ListRepositoriesForApprovalRuleTemplateInputRequestTypeDef",
    "ListRepositoriesInputRequestTypeDef",
    "RepositoryNameIdPairTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "MergeBranchesByFastForwardInputRequestTypeDef",
    "MergeHunkDetailTypeDef",
    "MergeMetadataTypeDef",
    "MergePullRequestByFastForwardInputRequestTypeDef",
    "OverridePullRequestApprovalRulesInputRequestTypeDef",
    "PostCommentReplyInputRequestTypeDef",
    "PullRequestCreatedEventMetadataTypeDef",
    "PullRequestSourceReferenceUpdatedEventMetadataTypeDef",
    "PullRequestStatusChangedEventMetadataTypeDef",
    "PutCommentReactionInputRequestTypeDef",
    "SourceFileSpecifierTypeDef",
    "ReactionValueFormatsTypeDef",
    "RepositoryTriggerExecutionFailureTypeDef",
    "RepositoryTriggerTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateApprovalRuleTemplateContentInputRequestTypeDef",
    "UpdateApprovalRuleTemplateDescriptionInputRequestTypeDef",
    "UpdateApprovalRuleTemplateNameInputRequestTypeDef",
    "UpdateCommentInputRequestTypeDef",
    "UpdateDefaultBranchInputRequestTypeDef",
    "UpdatePullRequestApprovalRuleContentInputRequestTypeDef",
    "UpdatePullRequestApprovalStateInputRequestTypeDef",
    "UpdatePullRequestDescriptionInputRequestTypeDef",
    "UpdatePullRequestStatusInputRequestTypeDef",
    "UpdatePullRequestTitleInputRequestTypeDef",
    "UpdateRepositoryDescriptionInputRequestTypeDef",
    "UpdateRepositoryEncryptionKeyInputRequestTypeDef",
    "UpdateRepositoryNameInputRequestTypeDef",
    "ApprovalRuleTypeDef",
    "BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef",
    "CreateApprovalRuleTemplateOutputTypeDef",
    "CreateUnreferencedMergeCommitOutputTypeDef",
    "DeleteApprovalRuleTemplateOutputTypeDef",
    "DeleteFileOutputTypeDef",
    "DeletePullRequestApprovalRuleOutputTypeDef",
    "DeleteRepositoryOutputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetApprovalRuleTemplateOutputTypeDef",
    "GetBlobOutputTypeDef",
    "GetFileOutputTypeDef",
    "GetMergeCommitOutputTypeDef",
    "GetMergeOptionsOutputTypeDef",
    "GetPullRequestApprovalStatesOutputTypeDef",
    "GetPullRequestOverrideStateOutputTypeDef",
    "ListApprovalRuleTemplatesOutputTypeDef",
    "ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef",
    "ListBranchesOutputTypeDef",
    "ListPullRequestsOutputTypeDef",
    "ListRepositoriesForApprovalRuleTemplateOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "MergeBranchesByFastForwardOutputTypeDef",
    "MergeBranchesBySquashOutputTypeDef",
    "MergeBranchesByThreeWayOutputTypeDef",
    "PutFileOutputTypeDef",
    "PutRepositoryTriggersOutputTypeDef",
    "UpdateApprovalRuleTemplateContentOutputTypeDef",
    "UpdateApprovalRuleTemplateDescriptionOutputTypeDef",
    "UpdateApprovalRuleTemplateNameOutputTypeDef",
    "UpdateRepositoryEncryptionKeyOutputTypeDef",
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef",
    "BatchGetRepositoriesOutputTypeDef",
    "CreateRepositoryOutputTypeDef",
    "GetRepositoryOutputTypeDef",
    "DifferenceTypeDef",
    "PutFileInputRequestTypeDef",
    "ReplaceContentEntryTypeDef",
    "DeleteBranchOutputTypeDef",
    "GetBranchOutputTypeDef",
    "DeleteCommentContentOutputTypeDef",
    "GetCommentOutputTypeDef",
    "PostCommentReplyOutputTypeDef",
    "UpdateCommentOutputTypeDef",
    "CommentsForComparedCommitTypeDef",
    "CommentsForPullRequestTypeDef",
    "PostCommentForComparedCommitInputRequestTypeDef",
    "PostCommentForComparedCommitOutputTypeDef",
    "PostCommentForPullRequestInputRequestTypeDef",
    "PostCommentForPullRequestOutputTypeDef",
    "CommitTypeDef",
    "ConflictMetadataTypeDef",
    "CreateCommitOutputTypeDef",
    "CreatePullRequestInputRequestTypeDef",
    "DescribePullRequestEventsInputDescribePullRequestEventsPaginateTypeDef",
    "GetCommentsForComparedCommitInputGetCommentsForComparedCommitPaginateTypeDef",
    "GetCommentsForPullRequestInputGetCommentsForPullRequestPaginateTypeDef",
    "GetDifferencesInputGetDifferencesPaginateTypeDef",
    "ListBranchesInputListBranchesPaginateTypeDef",
    "ListPullRequestsInputListPullRequestsPaginateTypeDef",
    "ListRepositoriesInputListRepositoriesPaginateTypeDef",
    "EvaluatePullRequestApprovalRulesOutputTypeDef",
    "GetFolderOutputTypeDef",
    "GetRepositoryTriggersOutputTypeDef",
    "ListRepositoriesOutputTypeDef",
    "MergeHunkTypeDef",
    "PullRequestMergedStateChangedEventMetadataTypeDef",
    "PullRequestTargetTypeDef",
    "PutFileEntryTypeDef",
    "ReactionForCommentTypeDef",
    "TestRepositoryTriggersOutputTypeDef",
    "RepositoryTriggerUnionTypeDef",
    "TestRepositoryTriggersInputRequestTypeDef",
    "CreatePullRequestApprovalRuleOutputTypeDef",
    "UpdatePullRequestApprovalRuleContentOutputTypeDef",
    "GetDifferencesOutputTypeDef",
    "ConflictResolutionTypeDef",
    "GetCommentsForComparedCommitOutputTypeDef",
    "GetCommentsForPullRequestOutputTypeDef",
    "BatchGetCommitsOutputTypeDef",
    "FileVersionTypeDef",
    "GetCommitOutputTypeDef",
    "GetMergeConflictsOutputTypeDef",
    "ConflictTypeDef",
    "DescribeMergeConflictsOutputTypeDef",
    "PullRequestEventTypeDef",
    "PullRequestTypeDef",
    "CreateCommitInputRequestTypeDef",
    "GetCommentReactionsOutputTypeDef",
    "PutRepositoryTriggersInputRequestTypeDef",
    "CreateUnreferencedMergeCommitInputRequestTypeDef",
    "MergeBranchesBySquashInputRequestTypeDef",
    "MergeBranchesByThreeWayInputRequestTypeDef",
    "MergePullRequestBySquashInputRequestTypeDef",
    "MergePullRequestByThreeWayInputRequestTypeDef",
    "ListFileCommitHistoryResponseTypeDef",
    "BatchDescribeMergeConflictsOutputTypeDef",
    "DescribePullRequestEventsOutputTypeDef",
    "CreatePullRequestOutputTypeDef",
    "GetPullRequestOutputTypeDef",
    "MergePullRequestByFastForwardOutputTypeDef",
    "MergePullRequestBySquashOutputTypeDef",
    "MergePullRequestByThreeWayOutputTypeDef",
    "UpdatePullRequestDescriptionOutputTypeDef",
    "UpdatePullRequestStatusOutputTypeDef",
    "UpdatePullRequestTitleOutputTypeDef",
)

ApprovalRuleEventMetadataTypeDef = TypedDict(
    "ApprovalRuleEventMetadataTypeDef",
    {
        "approvalRuleName": NotRequired[str],
        "approvalRuleId": NotRequired[str],
        "approvalRuleContent": NotRequired[str],
    },
)
ApprovalRuleOverriddenEventMetadataTypeDef = TypedDict(
    "ApprovalRuleOverriddenEventMetadataTypeDef",
    {
        "revisionId": NotRequired[str],
        "overrideStatus": NotRequired[OverrideStatusType],
    },
)
ApprovalRuleTemplateTypeDef = TypedDict(
    "ApprovalRuleTemplateTypeDef",
    {
        "approvalRuleTemplateId": NotRequired[str],
        "approvalRuleTemplateName": NotRequired[str],
        "approvalRuleTemplateDescription": NotRequired[str],
        "approvalRuleTemplateContent": NotRequired[str],
        "ruleContentSha256": NotRequired[str],
        "lastModifiedDate": NotRequired[datetime],
        "creationDate": NotRequired[datetime],
        "lastModifiedUser": NotRequired[str],
    },
)
OriginApprovalRuleTemplateTypeDef = TypedDict(
    "OriginApprovalRuleTemplateTypeDef",
    {
        "approvalRuleTemplateId": NotRequired[str],
        "approvalRuleTemplateName": NotRequired[str],
    },
)
ApprovalStateChangedEventMetadataTypeDef = TypedDict(
    "ApprovalStateChangedEventMetadataTypeDef",
    {
        "revisionId": NotRequired[str],
        "approvalStatus": NotRequired[ApprovalStateType],
    },
)
ApprovalTypeDef = TypedDict(
    "ApprovalTypeDef",
    {
        "userArn": NotRequired[str],
        "approvalState": NotRequired[ApprovalStateType],
    },
)
AssociateApprovalRuleTemplateWithRepositoryInputRequestTypeDef = TypedDict(
    "AssociateApprovalRuleTemplateWithRepositoryInputRequestTypeDef",
    {
        "approvalRuleTemplateName": str,
        "repositoryName": str,
    },
)
BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef = TypedDict(
    "BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef",
    {
        "repositoryName": NotRequired[str],
        "errorCode": NotRequired[str],
        "errorMessage": NotRequired[str],
    },
)
BatchAssociateApprovalRuleTemplateWithRepositoriesInputRequestTypeDef = TypedDict(
    "BatchAssociateApprovalRuleTemplateWithRepositoriesInputRequestTypeDef",
    {
        "approvalRuleTemplateName": str,
        "repositoryNames": Sequence[str],
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
BatchDescribeMergeConflictsErrorTypeDef = TypedDict(
    "BatchDescribeMergeConflictsErrorTypeDef",
    {
        "filePath": str,
        "exceptionName": str,
        "message": str,
    },
)
BatchDescribeMergeConflictsInputRequestTypeDef = TypedDict(
    "BatchDescribeMergeConflictsInputRequestTypeDef",
    {
        "repositoryName": str,
        "destinationCommitSpecifier": str,
        "sourceCommitSpecifier": str,
        "mergeOption": MergeOptionTypeEnumType,
        "maxMergeHunks": NotRequired[int],
        "maxConflictFiles": NotRequired[int],
        "filePaths": NotRequired[Sequence[str]],
        "conflictDetailLevel": NotRequired[ConflictDetailLevelTypeEnumType],
        "conflictResolutionStrategy": NotRequired[ConflictResolutionStrategyTypeEnumType],
        "nextToken": NotRequired[str],
    },
)
BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef = TypedDict(
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef",
    {
        "repositoryName": NotRequired[str],
        "errorCode": NotRequired[str],
        "errorMessage": NotRequired[str],
    },
)
BatchDisassociateApprovalRuleTemplateFromRepositoriesInputRequestTypeDef = TypedDict(
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesInputRequestTypeDef",
    {
        "approvalRuleTemplateName": str,
        "repositoryNames": Sequence[str],
    },
)
BatchGetCommitsErrorTypeDef = TypedDict(
    "BatchGetCommitsErrorTypeDef",
    {
        "commitId": NotRequired[str],
        "errorCode": NotRequired[str],
        "errorMessage": NotRequired[str],
    },
)
BatchGetCommitsInputRequestTypeDef = TypedDict(
    "BatchGetCommitsInputRequestTypeDef",
    {
        "commitIds": Sequence[str],
        "repositoryName": str,
    },
)
BatchGetRepositoriesErrorTypeDef = TypedDict(
    "BatchGetRepositoriesErrorTypeDef",
    {
        "repositoryId": NotRequired[str],
        "repositoryName": NotRequired[str],
        "errorCode": NotRequired[BatchGetRepositoriesErrorCodeEnumType],
        "errorMessage": NotRequired[str],
    },
)
BatchGetRepositoriesInputRequestTypeDef = TypedDict(
    "BatchGetRepositoriesInputRequestTypeDef",
    {
        "repositoryNames": Sequence[str],
    },
)
RepositoryMetadataTypeDef = TypedDict(
    "RepositoryMetadataTypeDef",
    {
        "accountId": NotRequired[str],
        "repositoryId": NotRequired[str],
        "repositoryName": NotRequired[str],
        "repositoryDescription": NotRequired[str],
        "defaultBranch": NotRequired[str],
        "lastModifiedDate": NotRequired[datetime],
        "creationDate": NotRequired[datetime],
        "cloneUrlHttp": NotRequired[str],
        "cloneUrlSsh": NotRequired[str],
        "Arn": NotRequired[str],
        "kmsKeyId": NotRequired[str],
    },
)
BlobMetadataTypeDef = TypedDict(
    "BlobMetadataTypeDef",
    {
        "blobId": NotRequired[str],
        "path": NotRequired[str],
        "mode": NotRequired[str],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
BranchInfoTypeDef = TypedDict(
    "BranchInfoTypeDef",
    {
        "branchName": NotRequired[str],
        "commitId": NotRequired[str],
    },
)
CommentTypeDef = TypedDict(
    "CommentTypeDef",
    {
        "commentId": NotRequired[str],
        "content": NotRequired[str],
        "inReplyTo": NotRequired[str],
        "creationDate": NotRequired[datetime],
        "lastModifiedDate": NotRequired[datetime],
        "authorArn": NotRequired[str],
        "deleted": NotRequired[bool],
        "clientRequestToken": NotRequired[str],
        "callerReactions": NotRequired[List[str]],
        "reactionCounts": NotRequired[Dict[str, int]],
    },
)
LocationTypeDef = TypedDict(
    "LocationTypeDef",
    {
        "filePath": NotRequired[str],
        "filePosition": NotRequired[int],
        "relativeFileVersion": NotRequired[RelativeFileVersionEnumType],
    },
)
UserInfoTypeDef = TypedDict(
    "UserInfoTypeDef",
    {
        "name": NotRequired[str],
        "email": NotRequired[str],
        "date": NotRequired[str],
    },
)
FileModesTypeDef = TypedDict(
    "FileModesTypeDef",
    {
        "source": NotRequired[FileModeTypeEnumType],
        "destination": NotRequired[FileModeTypeEnumType],
        "base": NotRequired[FileModeTypeEnumType],
    },
)
FileSizesTypeDef = TypedDict(
    "FileSizesTypeDef",
    {
        "source": NotRequired[int],
        "destination": NotRequired[int],
        "base": NotRequired[int],
    },
)
IsBinaryFileTypeDef = TypedDict(
    "IsBinaryFileTypeDef",
    {
        "source": NotRequired[bool],
        "destination": NotRequired[bool],
        "base": NotRequired[bool],
    },
)
MergeOperationsTypeDef = TypedDict(
    "MergeOperationsTypeDef",
    {
        "source": NotRequired[ChangeTypeEnumType],
        "destination": NotRequired[ChangeTypeEnumType],
    },
)
ObjectTypesTypeDef = TypedDict(
    "ObjectTypesTypeDef",
    {
        "source": NotRequired[ObjectTypeEnumType],
        "destination": NotRequired[ObjectTypeEnumType],
        "base": NotRequired[ObjectTypeEnumType],
    },
)
DeleteFileEntryTypeDef = TypedDict(
    "DeleteFileEntryTypeDef",
    {
        "filePath": str,
    },
)
SetFileModeEntryTypeDef = TypedDict(
    "SetFileModeEntryTypeDef",
    {
        "filePath": str,
        "fileMode": FileModeTypeEnumType,
    },
)
CreateApprovalRuleTemplateInputRequestTypeDef = TypedDict(
    "CreateApprovalRuleTemplateInputRequestTypeDef",
    {
        "approvalRuleTemplateName": str,
        "approvalRuleTemplateContent": str,
        "approvalRuleTemplateDescription": NotRequired[str],
    },
)
CreateBranchInputRequestTypeDef = TypedDict(
    "CreateBranchInputRequestTypeDef",
    {
        "repositoryName": str,
        "branchName": str,
        "commitId": str,
    },
)
FileMetadataTypeDef = TypedDict(
    "FileMetadataTypeDef",
    {
        "absolutePath": NotRequired[str],
        "blobId": NotRequired[str],
        "fileMode": NotRequired[FileModeTypeEnumType],
    },
)
CreatePullRequestApprovalRuleInputRequestTypeDef = TypedDict(
    "CreatePullRequestApprovalRuleInputRequestTypeDef",
    {
        "pullRequestId": str,
        "approvalRuleName": str,
        "approvalRuleContent": str,
    },
)
TargetTypeDef = TypedDict(
    "TargetTypeDef",
    {
        "repositoryName": str,
        "sourceReference": str,
        "destinationReference": NotRequired[str],
    },
)
CreateRepositoryInputRequestTypeDef = TypedDict(
    "CreateRepositoryInputRequestTypeDef",
    {
        "repositoryName": str,
        "repositoryDescription": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "kmsKeyId": NotRequired[str],
    },
)
DeleteApprovalRuleTemplateInputRequestTypeDef = TypedDict(
    "DeleteApprovalRuleTemplateInputRequestTypeDef",
    {
        "approvalRuleTemplateName": str,
    },
)
DeleteBranchInputRequestTypeDef = TypedDict(
    "DeleteBranchInputRequestTypeDef",
    {
        "repositoryName": str,
        "branchName": str,
    },
)
DeleteCommentContentInputRequestTypeDef = TypedDict(
    "DeleteCommentContentInputRequestTypeDef",
    {
        "commentId": str,
    },
)
DeleteFileInputRequestTypeDef = TypedDict(
    "DeleteFileInputRequestTypeDef",
    {
        "repositoryName": str,
        "branchName": str,
        "filePath": str,
        "parentCommitId": str,
        "keepEmptyFolders": NotRequired[bool],
        "commitMessage": NotRequired[str],
        "name": NotRequired[str],
        "email": NotRequired[str],
    },
)
DeletePullRequestApprovalRuleInputRequestTypeDef = TypedDict(
    "DeletePullRequestApprovalRuleInputRequestTypeDef",
    {
        "pullRequestId": str,
        "approvalRuleName": str,
    },
)
DeleteRepositoryInputRequestTypeDef = TypedDict(
    "DeleteRepositoryInputRequestTypeDef",
    {
        "repositoryName": str,
    },
)
DescribeMergeConflictsInputRequestTypeDef = TypedDict(
    "DescribeMergeConflictsInputRequestTypeDef",
    {
        "repositoryName": str,
        "destinationCommitSpecifier": str,
        "sourceCommitSpecifier": str,
        "mergeOption": MergeOptionTypeEnumType,
        "filePath": str,
        "maxMergeHunks": NotRequired[int],
        "conflictDetailLevel": NotRequired[ConflictDetailLevelTypeEnumType],
        "conflictResolutionStrategy": NotRequired[ConflictResolutionStrategyTypeEnumType],
        "nextToken": NotRequired[str],
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
DescribePullRequestEventsInputRequestTypeDef = TypedDict(
    "DescribePullRequestEventsInputRequestTypeDef",
    {
        "pullRequestId": str,
        "pullRequestEventType": NotRequired[PullRequestEventTypeType],
        "actorArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
DisassociateApprovalRuleTemplateFromRepositoryInputRequestTypeDef = TypedDict(
    "DisassociateApprovalRuleTemplateFromRepositoryInputRequestTypeDef",
    {
        "approvalRuleTemplateName": str,
        "repositoryName": str,
    },
)
EvaluatePullRequestApprovalRulesInputRequestTypeDef = TypedDict(
    "EvaluatePullRequestApprovalRulesInputRequestTypeDef",
    {
        "pullRequestId": str,
        "revisionId": str,
    },
)
EvaluationTypeDef = TypedDict(
    "EvaluationTypeDef",
    {
        "approved": NotRequired[bool],
        "overridden": NotRequired[bool],
        "approvalRulesSatisfied": NotRequired[List[str]],
        "approvalRulesNotSatisfied": NotRequired[List[str]],
    },
)
FileTypeDef = TypedDict(
    "FileTypeDef",
    {
        "blobId": NotRequired[str],
        "absolutePath": NotRequired[str],
        "relativePath": NotRequired[str],
        "fileMode": NotRequired[FileModeTypeEnumType],
    },
)
FolderTypeDef = TypedDict(
    "FolderTypeDef",
    {
        "treeId": NotRequired[str],
        "absolutePath": NotRequired[str],
        "relativePath": NotRequired[str],
    },
)
GetApprovalRuleTemplateInputRequestTypeDef = TypedDict(
    "GetApprovalRuleTemplateInputRequestTypeDef",
    {
        "approvalRuleTemplateName": str,
    },
)
GetBlobInputRequestTypeDef = TypedDict(
    "GetBlobInputRequestTypeDef",
    {
        "repositoryName": str,
        "blobId": str,
    },
)
GetBranchInputRequestTypeDef = TypedDict(
    "GetBranchInputRequestTypeDef",
    {
        "repositoryName": NotRequired[str],
        "branchName": NotRequired[str],
    },
)
GetCommentInputRequestTypeDef = TypedDict(
    "GetCommentInputRequestTypeDef",
    {
        "commentId": str,
    },
)
GetCommentReactionsInputRequestTypeDef = TypedDict(
    "GetCommentReactionsInputRequestTypeDef",
    {
        "commentId": str,
        "reactionUserArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
GetCommentsForComparedCommitInputRequestTypeDef = TypedDict(
    "GetCommentsForComparedCommitInputRequestTypeDef",
    {
        "repositoryName": str,
        "afterCommitId": str,
        "beforeCommitId": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
GetCommentsForPullRequestInputRequestTypeDef = TypedDict(
    "GetCommentsForPullRequestInputRequestTypeDef",
    {
        "pullRequestId": str,
        "repositoryName": NotRequired[str],
        "beforeCommitId": NotRequired[str],
        "afterCommitId": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
GetCommitInputRequestTypeDef = TypedDict(
    "GetCommitInputRequestTypeDef",
    {
        "repositoryName": str,
        "commitId": str,
    },
)
GetDifferencesInputRequestTypeDef = TypedDict(
    "GetDifferencesInputRequestTypeDef",
    {
        "repositoryName": str,
        "afterCommitSpecifier": str,
        "beforeCommitSpecifier": NotRequired[str],
        "beforePath": NotRequired[str],
        "afterPath": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetFileInputRequestTypeDef = TypedDict(
    "GetFileInputRequestTypeDef",
    {
        "repositoryName": str,
        "filePath": str,
        "commitSpecifier": NotRequired[str],
    },
)
GetFolderInputRequestTypeDef = TypedDict(
    "GetFolderInputRequestTypeDef",
    {
        "repositoryName": str,
        "folderPath": str,
        "commitSpecifier": NotRequired[str],
    },
)
SubModuleTypeDef = TypedDict(
    "SubModuleTypeDef",
    {
        "commitId": NotRequired[str],
        "absolutePath": NotRequired[str],
        "relativePath": NotRequired[str],
    },
)
SymbolicLinkTypeDef = TypedDict(
    "SymbolicLinkTypeDef",
    {
        "blobId": NotRequired[str],
        "absolutePath": NotRequired[str],
        "relativePath": NotRequired[str],
        "fileMode": NotRequired[FileModeTypeEnumType],
    },
)
GetMergeCommitInputRequestTypeDef = TypedDict(
    "GetMergeCommitInputRequestTypeDef",
    {
        "repositoryName": str,
        "sourceCommitSpecifier": str,
        "destinationCommitSpecifier": str,
        "conflictDetailLevel": NotRequired[ConflictDetailLevelTypeEnumType],
        "conflictResolutionStrategy": NotRequired[ConflictResolutionStrategyTypeEnumType],
    },
)
GetMergeConflictsInputRequestTypeDef = TypedDict(
    "GetMergeConflictsInputRequestTypeDef",
    {
        "repositoryName": str,
        "destinationCommitSpecifier": str,
        "sourceCommitSpecifier": str,
        "mergeOption": MergeOptionTypeEnumType,
        "conflictDetailLevel": NotRequired[ConflictDetailLevelTypeEnumType],
        "maxConflictFiles": NotRequired[int],
        "conflictResolutionStrategy": NotRequired[ConflictResolutionStrategyTypeEnumType],
        "nextToken": NotRequired[str],
    },
)
GetMergeOptionsInputRequestTypeDef = TypedDict(
    "GetMergeOptionsInputRequestTypeDef",
    {
        "repositoryName": str,
        "sourceCommitSpecifier": str,
        "destinationCommitSpecifier": str,
        "conflictDetailLevel": NotRequired[ConflictDetailLevelTypeEnumType],
        "conflictResolutionStrategy": NotRequired[ConflictResolutionStrategyTypeEnumType],
    },
)
GetPullRequestApprovalStatesInputRequestTypeDef = TypedDict(
    "GetPullRequestApprovalStatesInputRequestTypeDef",
    {
        "pullRequestId": str,
        "revisionId": str,
    },
)
GetPullRequestInputRequestTypeDef = TypedDict(
    "GetPullRequestInputRequestTypeDef",
    {
        "pullRequestId": str,
    },
)
GetPullRequestOverrideStateInputRequestTypeDef = TypedDict(
    "GetPullRequestOverrideStateInputRequestTypeDef",
    {
        "pullRequestId": str,
        "revisionId": str,
    },
)
GetRepositoryInputRequestTypeDef = TypedDict(
    "GetRepositoryInputRequestTypeDef",
    {
        "repositoryName": str,
    },
)
GetRepositoryTriggersInputRequestTypeDef = TypedDict(
    "GetRepositoryTriggersInputRequestTypeDef",
    {
        "repositoryName": str,
    },
)
RepositoryTriggerOutputTypeDef = TypedDict(
    "RepositoryTriggerOutputTypeDef",
    {
        "name": str,
        "destinationArn": str,
        "events": List[RepositoryTriggerEventEnumType],
        "customData": NotRequired[str],
        "branches": NotRequired[List[str]],
    },
)
ListApprovalRuleTemplatesInputRequestTypeDef = TypedDict(
    "ListApprovalRuleTemplatesInputRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListAssociatedApprovalRuleTemplatesForRepositoryInputRequestTypeDef = TypedDict(
    "ListAssociatedApprovalRuleTemplatesForRepositoryInputRequestTypeDef",
    {
        "repositoryName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListBranchesInputRequestTypeDef = TypedDict(
    "ListBranchesInputRequestTypeDef",
    {
        "repositoryName": str,
        "nextToken": NotRequired[str],
    },
)
ListFileCommitHistoryRequestRequestTypeDef = TypedDict(
    "ListFileCommitHistoryRequestRequestTypeDef",
    {
        "repositoryName": str,
        "filePath": str,
        "commitSpecifier": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListPullRequestsInputRequestTypeDef = TypedDict(
    "ListPullRequestsInputRequestTypeDef",
    {
        "repositoryName": str,
        "authorArn": NotRequired[str],
        "pullRequestStatus": NotRequired[PullRequestStatusEnumType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListRepositoriesForApprovalRuleTemplateInputRequestTypeDef = TypedDict(
    "ListRepositoriesForApprovalRuleTemplateInputRequestTypeDef",
    {
        "approvalRuleTemplateName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListRepositoriesInputRequestTypeDef = TypedDict(
    "ListRepositoriesInputRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "sortBy": NotRequired[SortByEnumType],
        "order": NotRequired[OrderEnumType],
    },
)
RepositoryNameIdPairTypeDef = TypedDict(
    "RepositoryNameIdPairTypeDef",
    {
        "repositoryName": NotRequired[str],
        "repositoryId": NotRequired[str],
    },
)
ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "nextToken": NotRequired[str],
    },
)
MergeBranchesByFastForwardInputRequestTypeDef = TypedDict(
    "MergeBranchesByFastForwardInputRequestTypeDef",
    {
        "repositoryName": str,
        "sourceCommitSpecifier": str,
        "destinationCommitSpecifier": str,
        "targetBranch": NotRequired[str],
    },
)
MergeHunkDetailTypeDef = TypedDict(
    "MergeHunkDetailTypeDef",
    {
        "startLine": NotRequired[int],
        "endLine": NotRequired[int],
        "hunkContent": NotRequired[str],
    },
)
MergeMetadataTypeDef = TypedDict(
    "MergeMetadataTypeDef",
    {
        "isMerged": NotRequired[bool],
        "mergedBy": NotRequired[str],
        "mergeCommitId": NotRequired[str],
        "mergeOption": NotRequired[MergeOptionTypeEnumType],
    },
)
MergePullRequestByFastForwardInputRequestTypeDef = TypedDict(
    "MergePullRequestByFastForwardInputRequestTypeDef",
    {
        "pullRequestId": str,
        "repositoryName": str,
        "sourceCommitId": NotRequired[str],
    },
)
OverridePullRequestApprovalRulesInputRequestTypeDef = TypedDict(
    "OverridePullRequestApprovalRulesInputRequestTypeDef",
    {
        "pullRequestId": str,
        "revisionId": str,
        "overrideStatus": OverrideStatusType,
    },
)
PostCommentReplyInputRequestTypeDef = TypedDict(
    "PostCommentReplyInputRequestTypeDef",
    {
        "inReplyTo": str,
        "content": str,
        "clientRequestToken": NotRequired[str],
    },
)
PullRequestCreatedEventMetadataTypeDef = TypedDict(
    "PullRequestCreatedEventMetadataTypeDef",
    {
        "repositoryName": NotRequired[str],
        "sourceCommitId": NotRequired[str],
        "destinationCommitId": NotRequired[str],
        "mergeBase": NotRequired[str],
    },
)
PullRequestSourceReferenceUpdatedEventMetadataTypeDef = TypedDict(
    "PullRequestSourceReferenceUpdatedEventMetadataTypeDef",
    {
        "repositoryName": NotRequired[str],
        "beforeCommitId": NotRequired[str],
        "afterCommitId": NotRequired[str],
        "mergeBase": NotRequired[str],
    },
)
PullRequestStatusChangedEventMetadataTypeDef = TypedDict(
    "PullRequestStatusChangedEventMetadataTypeDef",
    {
        "pullRequestStatus": NotRequired[PullRequestStatusEnumType],
    },
)
PutCommentReactionInputRequestTypeDef = TypedDict(
    "PutCommentReactionInputRequestTypeDef",
    {
        "commentId": str,
        "reactionValue": str,
    },
)
SourceFileSpecifierTypeDef = TypedDict(
    "SourceFileSpecifierTypeDef",
    {
        "filePath": str,
        "isMove": NotRequired[bool],
    },
)
ReactionValueFormatsTypeDef = TypedDict(
    "ReactionValueFormatsTypeDef",
    {
        "emoji": NotRequired[str],
        "shortCode": NotRequired[str],
        "unicode": NotRequired[str],
    },
)
RepositoryTriggerExecutionFailureTypeDef = TypedDict(
    "RepositoryTriggerExecutionFailureTypeDef",
    {
        "trigger": NotRequired[str],
        "failureMessage": NotRequired[str],
    },
)
RepositoryTriggerTypeDef = TypedDict(
    "RepositoryTriggerTypeDef",
    {
        "name": str,
        "destinationArn": str,
        "events": Sequence[RepositoryTriggerEventEnumType],
        "customData": NotRequired[str],
        "branches": NotRequired[Sequence[str]],
    },
)
TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UpdateApprovalRuleTemplateContentInputRequestTypeDef = TypedDict(
    "UpdateApprovalRuleTemplateContentInputRequestTypeDef",
    {
        "approvalRuleTemplateName": str,
        "newRuleContent": str,
        "existingRuleContentSha256": NotRequired[str],
    },
)
UpdateApprovalRuleTemplateDescriptionInputRequestTypeDef = TypedDict(
    "UpdateApprovalRuleTemplateDescriptionInputRequestTypeDef",
    {
        "approvalRuleTemplateName": str,
        "approvalRuleTemplateDescription": str,
    },
)
UpdateApprovalRuleTemplateNameInputRequestTypeDef = TypedDict(
    "UpdateApprovalRuleTemplateNameInputRequestTypeDef",
    {
        "oldApprovalRuleTemplateName": str,
        "newApprovalRuleTemplateName": str,
    },
)
UpdateCommentInputRequestTypeDef = TypedDict(
    "UpdateCommentInputRequestTypeDef",
    {
        "commentId": str,
        "content": str,
    },
)
UpdateDefaultBranchInputRequestTypeDef = TypedDict(
    "UpdateDefaultBranchInputRequestTypeDef",
    {
        "repositoryName": str,
        "defaultBranchName": str,
    },
)
UpdatePullRequestApprovalRuleContentInputRequestTypeDef = TypedDict(
    "UpdatePullRequestApprovalRuleContentInputRequestTypeDef",
    {
        "pullRequestId": str,
        "approvalRuleName": str,
        "newRuleContent": str,
        "existingRuleContentSha256": NotRequired[str],
    },
)
UpdatePullRequestApprovalStateInputRequestTypeDef = TypedDict(
    "UpdatePullRequestApprovalStateInputRequestTypeDef",
    {
        "pullRequestId": str,
        "revisionId": str,
        "approvalState": ApprovalStateType,
    },
)
UpdatePullRequestDescriptionInputRequestTypeDef = TypedDict(
    "UpdatePullRequestDescriptionInputRequestTypeDef",
    {
        "pullRequestId": str,
        "description": str,
    },
)
UpdatePullRequestStatusInputRequestTypeDef = TypedDict(
    "UpdatePullRequestStatusInputRequestTypeDef",
    {
        "pullRequestId": str,
        "pullRequestStatus": PullRequestStatusEnumType,
    },
)
UpdatePullRequestTitleInputRequestTypeDef = TypedDict(
    "UpdatePullRequestTitleInputRequestTypeDef",
    {
        "pullRequestId": str,
        "title": str,
    },
)
UpdateRepositoryDescriptionInputRequestTypeDef = TypedDict(
    "UpdateRepositoryDescriptionInputRequestTypeDef",
    {
        "repositoryName": str,
        "repositoryDescription": NotRequired[str],
    },
)
UpdateRepositoryEncryptionKeyInputRequestTypeDef = TypedDict(
    "UpdateRepositoryEncryptionKeyInputRequestTypeDef",
    {
        "repositoryName": str,
        "kmsKeyId": str,
    },
)
UpdateRepositoryNameInputRequestTypeDef = TypedDict(
    "UpdateRepositoryNameInputRequestTypeDef",
    {
        "oldName": str,
        "newName": str,
    },
)
ApprovalRuleTypeDef = TypedDict(
    "ApprovalRuleTypeDef",
    {
        "approvalRuleId": NotRequired[str],
        "approvalRuleName": NotRequired[str],
        "approvalRuleContent": NotRequired[str],
        "ruleContentSha256": NotRequired[str],
        "lastModifiedDate": NotRequired[datetime],
        "creationDate": NotRequired[datetime],
        "lastModifiedUser": NotRequired[str],
        "originApprovalRuleTemplate": NotRequired[OriginApprovalRuleTemplateTypeDef],
    },
)
BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef = TypedDict(
    "BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef",
    {
        "associatedRepositoryNames": List[str],
        "errors": List[BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateApprovalRuleTemplateOutputTypeDef = TypedDict(
    "CreateApprovalRuleTemplateOutputTypeDef",
    {
        "approvalRuleTemplate": ApprovalRuleTemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateUnreferencedMergeCommitOutputTypeDef = TypedDict(
    "CreateUnreferencedMergeCommitOutputTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteApprovalRuleTemplateOutputTypeDef = TypedDict(
    "DeleteApprovalRuleTemplateOutputTypeDef",
    {
        "approvalRuleTemplateId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteFileOutputTypeDef = TypedDict(
    "DeleteFileOutputTypeDef",
    {
        "commitId": str,
        "blobId": str,
        "treeId": str,
        "filePath": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeletePullRequestApprovalRuleOutputTypeDef = TypedDict(
    "DeletePullRequestApprovalRuleOutputTypeDef",
    {
        "approvalRuleId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteRepositoryOutputTypeDef = TypedDict(
    "DeleteRepositoryOutputTypeDef",
    {
        "repositoryId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetApprovalRuleTemplateOutputTypeDef = TypedDict(
    "GetApprovalRuleTemplateOutputTypeDef",
    {
        "approvalRuleTemplate": ApprovalRuleTemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBlobOutputTypeDef = TypedDict(
    "GetBlobOutputTypeDef",
    {
        "content": bytes,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFileOutputTypeDef = TypedDict(
    "GetFileOutputTypeDef",
    {
        "commitId": str,
        "blobId": str,
        "filePath": str,
        "fileMode": FileModeTypeEnumType,
        "fileSize": int,
        "fileContent": bytes,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMergeCommitOutputTypeDef = TypedDict(
    "GetMergeCommitOutputTypeDef",
    {
        "sourceCommitId": str,
        "destinationCommitId": str,
        "baseCommitId": str,
        "mergedCommitId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMergeOptionsOutputTypeDef = TypedDict(
    "GetMergeOptionsOutputTypeDef",
    {
        "mergeOptions": List[MergeOptionTypeEnumType],
        "sourceCommitId": str,
        "destinationCommitId": str,
        "baseCommitId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPullRequestApprovalStatesOutputTypeDef = TypedDict(
    "GetPullRequestApprovalStatesOutputTypeDef",
    {
        "approvals": List[ApprovalTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPullRequestOverrideStateOutputTypeDef = TypedDict(
    "GetPullRequestOverrideStateOutputTypeDef",
    {
        "overridden": bool,
        "overrider": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListApprovalRuleTemplatesOutputTypeDef = TypedDict(
    "ListApprovalRuleTemplatesOutputTypeDef",
    {
        "approvalRuleTemplateNames": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef = TypedDict(
    "ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef",
    {
        "approvalRuleTemplateNames": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListBranchesOutputTypeDef = TypedDict(
    "ListBranchesOutputTypeDef",
    {
        "branches": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPullRequestsOutputTypeDef = TypedDict(
    "ListPullRequestsOutputTypeDef",
    {
        "pullRequestIds": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRepositoriesForApprovalRuleTemplateOutputTypeDef = TypedDict(
    "ListRepositoriesForApprovalRuleTemplateOutputTypeDef",
    {
        "repositoryNames": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "tags": Dict[str, str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MergeBranchesByFastForwardOutputTypeDef = TypedDict(
    "MergeBranchesByFastForwardOutputTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MergeBranchesBySquashOutputTypeDef = TypedDict(
    "MergeBranchesBySquashOutputTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MergeBranchesByThreeWayOutputTypeDef = TypedDict(
    "MergeBranchesByThreeWayOutputTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutFileOutputTypeDef = TypedDict(
    "PutFileOutputTypeDef",
    {
        "commitId": str,
        "blobId": str,
        "treeId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutRepositoryTriggersOutputTypeDef = TypedDict(
    "PutRepositoryTriggersOutputTypeDef",
    {
        "configurationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateApprovalRuleTemplateContentOutputTypeDef = TypedDict(
    "UpdateApprovalRuleTemplateContentOutputTypeDef",
    {
        "approvalRuleTemplate": ApprovalRuleTemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateApprovalRuleTemplateDescriptionOutputTypeDef = TypedDict(
    "UpdateApprovalRuleTemplateDescriptionOutputTypeDef",
    {
        "approvalRuleTemplate": ApprovalRuleTemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateApprovalRuleTemplateNameOutputTypeDef = TypedDict(
    "UpdateApprovalRuleTemplateNameOutputTypeDef",
    {
        "approvalRuleTemplate": ApprovalRuleTemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRepositoryEncryptionKeyOutputTypeDef = TypedDict(
    "UpdateRepositoryEncryptionKeyOutputTypeDef",
    {
        "repositoryId": str,
        "kmsKeyId": str,
        "originalKmsKeyId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef = TypedDict(
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef",
    {
        "disassociatedRepositoryNames": List[str],
        "errors": List[BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetRepositoriesOutputTypeDef = TypedDict(
    "BatchGetRepositoriesOutputTypeDef",
    {
        "repositories": List[RepositoryMetadataTypeDef],
        "repositoriesNotFound": List[str],
        "errors": List[BatchGetRepositoriesErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRepositoryOutputTypeDef = TypedDict(
    "CreateRepositoryOutputTypeDef",
    {
        "repositoryMetadata": RepositoryMetadataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRepositoryOutputTypeDef = TypedDict(
    "GetRepositoryOutputTypeDef",
    {
        "repositoryMetadata": RepositoryMetadataTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DifferenceTypeDef = TypedDict(
    "DifferenceTypeDef",
    {
        "beforeBlob": NotRequired[BlobMetadataTypeDef],
        "afterBlob": NotRequired[BlobMetadataTypeDef],
        "changeType": NotRequired[ChangeTypeEnumType],
    },
)
PutFileInputRequestTypeDef = TypedDict(
    "PutFileInputRequestTypeDef",
    {
        "repositoryName": str,
        "branchName": str,
        "fileContent": BlobTypeDef,
        "filePath": str,
        "fileMode": NotRequired[FileModeTypeEnumType],
        "parentCommitId": NotRequired[str],
        "commitMessage": NotRequired[str],
        "name": NotRequired[str],
        "email": NotRequired[str],
    },
)
ReplaceContentEntryTypeDef = TypedDict(
    "ReplaceContentEntryTypeDef",
    {
        "filePath": str,
        "replacementType": ReplacementTypeEnumType,
        "content": NotRequired[BlobTypeDef],
        "fileMode": NotRequired[FileModeTypeEnumType],
    },
)
DeleteBranchOutputTypeDef = TypedDict(
    "DeleteBranchOutputTypeDef",
    {
        "deletedBranch": BranchInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBranchOutputTypeDef = TypedDict(
    "GetBranchOutputTypeDef",
    {
        "branch": BranchInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteCommentContentOutputTypeDef = TypedDict(
    "DeleteCommentContentOutputTypeDef",
    {
        "comment": CommentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCommentOutputTypeDef = TypedDict(
    "GetCommentOutputTypeDef",
    {
        "comment": CommentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PostCommentReplyOutputTypeDef = TypedDict(
    "PostCommentReplyOutputTypeDef",
    {
        "comment": CommentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateCommentOutputTypeDef = TypedDict(
    "UpdateCommentOutputTypeDef",
    {
        "comment": CommentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CommentsForComparedCommitTypeDef = TypedDict(
    "CommentsForComparedCommitTypeDef",
    {
        "repositoryName": NotRequired[str],
        "beforeCommitId": NotRequired[str],
        "afterCommitId": NotRequired[str],
        "beforeBlobId": NotRequired[str],
        "afterBlobId": NotRequired[str],
        "location": NotRequired[LocationTypeDef],
        "comments": NotRequired[List[CommentTypeDef]],
    },
)
CommentsForPullRequestTypeDef = TypedDict(
    "CommentsForPullRequestTypeDef",
    {
        "pullRequestId": NotRequired[str],
        "repositoryName": NotRequired[str],
        "beforeCommitId": NotRequired[str],
        "afterCommitId": NotRequired[str],
        "beforeBlobId": NotRequired[str],
        "afterBlobId": NotRequired[str],
        "location": NotRequired[LocationTypeDef],
        "comments": NotRequired[List[CommentTypeDef]],
    },
)
PostCommentForComparedCommitInputRequestTypeDef = TypedDict(
    "PostCommentForComparedCommitInputRequestTypeDef",
    {
        "repositoryName": str,
        "afterCommitId": str,
        "content": str,
        "beforeCommitId": NotRequired[str],
        "location": NotRequired[LocationTypeDef],
        "clientRequestToken": NotRequired[str],
    },
)
PostCommentForComparedCommitOutputTypeDef = TypedDict(
    "PostCommentForComparedCommitOutputTypeDef",
    {
        "repositoryName": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "beforeBlobId": str,
        "afterBlobId": str,
        "location": LocationTypeDef,
        "comment": CommentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PostCommentForPullRequestInputRequestTypeDef = TypedDict(
    "PostCommentForPullRequestInputRequestTypeDef",
    {
        "pullRequestId": str,
        "repositoryName": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "content": str,
        "location": NotRequired[LocationTypeDef],
        "clientRequestToken": NotRequired[str],
    },
)
PostCommentForPullRequestOutputTypeDef = TypedDict(
    "PostCommentForPullRequestOutputTypeDef",
    {
        "repositoryName": str,
        "pullRequestId": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "beforeBlobId": str,
        "afterBlobId": str,
        "location": LocationTypeDef,
        "comment": CommentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CommitTypeDef = TypedDict(
    "CommitTypeDef",
    {
        "commitId": NotRequired[str],
        "treeId": NotRequired[str],
        "parents": NotRequired[List[str]],
        "message": NotRequired[str],
        "author": NotRequired[UserInfoTypeDef],
        "committer": NotRequired[UserInfoTypeDef],
        "additionalData": NotRequired[str],
    },
)
ConflictMetadataTypeDef = TypedDict(
    "ConflictMetadataTypeDef",
    {
        "filePath": NotRequired[str],
        "fileSizes": NotRequired[FileSizesTypeDef],
        "fileModes": NotRequired[FileModesTypeDef],
        "objectTypes": NotRequired[ObjectTypesTypeDef],
        "numberOfConflicts": NotRequired[int],
        "isBinaryFile": NotRequired[IsBinaryFileTypeDef],
        "contentConflict": NotRequired[bool],
        "fileModeConflict": NotRequired[bool],
        "objectTypeConflict": NotRequired[bool],
        "mergeOperations": NotRequired[MergeOperationsTypeDef],
    },
)
CreateCommitOutputTypeDef = TypedDict(
    "CreateCommitOutputTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "filesAdded": List[FileMetadataTypeDef],
        "filesUpdated": List[FileMetadataTypeDef],
        "filesDeleted": List[FileMetadataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePullRequestInputRequestTypeDef = TypedDict(
    "CreatePullRequestInputRequestTypeDef",
    {
        "title": str,
        "targets": Sequence[TargetTypeDef],
        "description": NotRequired[str],
        "clientRequestToken": NotRequired[str],
    },
)
DescribePullRequestEventsInputDescribePullRequestEventsPaginateTypeDef = TypedDict(
    "DescribePullRequestEventsInputDescribePullRequestEventsPaginateTypeDef",
    {
        "pullRequestId": str,
        "pullRequestEventType": NotRequired[PullRequestEventTypeType],
        "actorArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetCommentsForComparedCommitInputGetCommentsForComparedCommitPaginateTypeDef = TypedDict(
    "GetCommentsForComparedCommitInputGetCommentsForComparedCommitPaginateTypeDef",
    {
        "repositoryName": str,
        "afterCommitId": str,
        "beforeCommitId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetCommentsForPullRequestInputGetCommentsForPullRequestPaginateTypeDef = TypedDict(
    "GetCommentsForPullRequestInputGetCommentsForPullRequestPaginateTypeDef",
    {
        "pullRequestId": str,
        "repositoryName": NotRequired[str],
        "beforeCommitId": NotRequired[str],
        "afterCommitId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetDifferencesInputGetDifferencesPaginateTypeDef = TypedDict(
    "GetDifferencesInputGetDifferencesPaginateTypeDef",
    {
        "repositoryName": str,
        "afterCommitSpecifier": str,
        "beforeCommitSpecifier": NotRequired[str],
        "beforePath": NotRequired[str],
        "afterPath": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListBranchesInputListBranchesPaginateTypeDef = TypedDict(
    "ListBranchesInputListBranchesPaginateTypeDef",
    {
        "repositoryName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPullRequestsInputListPullRequestsPaginateTypeDef = TypedDict(
    "ListPullRequestsInputListPullRequestsPaginateTypeDef",
    {
        "repositoryName": str,
        "authorArn": NotRequired[str],
        "pullRequestStatus": NotRequired[PullRequestStatusEnumType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRepositoriesInputListRepositoriesPaginateTypeDef = TypedDict(
    "ListRepositoriesInputListRepositoriesPaginateTypeDef",
    {
        "sortBy": NotRequired[SortByEnumType],
        "order": NotRequired[OrderEnumType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
EvaluatePullRequestApprovalRulesOutputTypeDef = TypedDict(
    "EvaluatePullRequestApprovalRulesOutputTypeDef",
    {
        "evaluation": EvaluationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFolderOutputTypeDef = TypedDict(
    "GetFolderOutputTypeDef",
    {
        "commitId": str,
        "folderPath": str,
        "treeId": str,
        "subFolders": List[FolderTypeDef],
        "files": List[FileTypeDef],
        "symbolicLinks": List[SymbolicLinkTypeDef],
        "subModules": List[SubModuleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRepositoryTriggersOutputTypeDef = TypedDict(
    "GetRepositoryTriggersOutputTypeDef",
    {
        "configurationId": str,
        "triggers": List[RepositoryTriggerOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRepositoriesOutputTypeDef = TypedDict(
    "ListRepositoriesOutputTypeDef",
    {
        "repositories": List[RepositoryNameIdPairTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MergeHunkTypeDef = TypedDict(
    "MergeHunkTypeDef",
    {
        "isConflict": NotRequired[bool],
        "source": NotRequired[MergeHunkDetailTypeDef],
        "destination": NotRequired[MergeHunkDetailTypeDef],
        "base": NotRequired[MergeHunkDetailTypeDef],
    },
)
PullRequestMergedStateChangedEventMetadataTypeDef = TypedDict(
    "PullRequestMergedStateChangedEventMetadataTypeDef",
    {
        "repositoryName": NotRequired[str],
        "destinationReference": NotRequired[str],
        "mergeMetadata": NotRequired[MergeMetadataTypeDef],
    },
)
PullRequestTargetTypeDef = TypedDict(
    "PullRequestTargetTypeDef",
    {
        "repositoryName": NotRequired[str],
        "sourceReference": NotRequired[str],
        "destinationReference": NotRequired[str],
        "destinationCommit": NotRequired[str],
        "sourceCommit": NotRequired[str],
        "mergeBase": NotRequired[str],
        "mergeMetadata": NotRequired[MergeMetadataTypeDef],
    },
)
PutFileEntryTypeDef = TypedDict(
    "PutFileEntryTypeDef",
    {
        "filePath": str,
        "fileMode": NotRequired[FileModeTypeEnumType],
        "fileContent": NotRequired[BlobTypeDef],
        "sourceFile": NotRequired[SourceFileSpecifierTypeDef],
    },
)
ReactionForCommentTypeDef = TypedDict(
    "ReactionForCommentTypeDef",
    {
        "reaction": NotRequired[ReactionValueFormatsTypeDef],
        "reactionUsers": NotRequired[List[str]],
        "reactionsFromDeletedUsersCount": NotRequired[int],
    },
)
TestRepositoryTriggersOutputTypeDef = TypedDict(
    "TestRepositoryTriggersOutputTypeDef",
    {
        "successfulExecutions": List[str],
        "failedExecutions": List[RepositoryTriggerExecutionFailureTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RepositoryTriggerUnionTypeDef = Union[RepositoryTriggerTypeDef, RepositoryTriggerOutputTypeDef]
TestRepositoryTriggersInputRequestTypeDef = TypedDict(
    "TestRepositoryTriggersInputRequestTypeDef",
    {
        "repositoryName": str,
        "triggers": Sequence[RepositoryTriggerTypeDef],
    },
)
CreatePullRequestApprovalRuleOutputTypeDef = TypedDict(
    "CreatePullRequestApprovalRuleOutputTypeDef",
    {
        "approvalRule": ApprovalRuleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePullRequestApprovalRuleContentOutputTypeDef = TypedDict(
    "UpdatePullRequestApprovalRuleContentOutputTypeDef",
    {
        "approvalRule": ApprovalRuleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDifferencesOutputTypeDef = TypedDict(
    "GetDifferencesOutputTypeDef",
    {
        "differences": List[DifferenceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ConflictResolutionTypeDef = TypedDict(
    "ConflictResolutionTypeDef",
    {
        "replaceContents": NotRequired[Sequence[ReplaceContentEntryTypeDef]],
        "deleteFiles": NotRequired[Sequence[DeleteFileEntryTypeDef]],
        "setFileModes": NotRequired[Sequence[SetFileModeEntryTypeDef]],
    },
)
GetCommentsForComparedCommitOutputTypeDef = TypedDict(
    "GetCommentsForComparedCommitOutputTypeDef",
    {
        "commentsForComparedCommitData": List[CommentsForComparedCommitTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCommentsForPullRequestOutputTypeDef = TypedDict(
    "GetCommentsForPullRequestOutputTypeDef",
    {
        "commentsForPullRequestData": List[CommentsForPullRequestTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetCommitsOutputTypeDef = TypedDict(
    "BatchGetCommitsOutputTypeDef",
    {
        "commits": List[CommitTypeDef],
        "errors": List[BatchGetCommitsErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FileVersionTypeDef = TypedDict(
    "FileVersionTypeDef",
    {
        "commit": NotRequired[CommitTypeDef],
        "blobId": NotRequired[str],
        "path": NotRequired[str],
        "revisionChildren": NotRequired[List[str]],
    },
)
GetCommitOutputTypeDef = TypedDict(
    "GetCommitOutputTypeDef",
    {
        "commit": CommitTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMergeConflictsOutputTypeDef = TypedDict(
    "GetMergeConflictsOutputTypeDef",
    {
        "mergeable": bool,
        "destinationCommitId": str,
        "sourceCommitId": str,
        "baseCommitId": str,
        "conflictMetadataList": List[ConflictMetadataTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConflictTypeDef = TypedDict(
    "ConflictTypeDef",
    {
        "conflictMetadata": NotRequired[ConflictMetadataTypeDef],
        "mergeHunks": NotRequired[List[MergeHunkTypeDef]],
    },
)
DescribeMergeConflictsOutputTypeDef = TypedDict(
    "DescribeMergeConflictsOutputTypeDef",
    {
        "conflictMetadata": ConflictMetadataTypeDef,
        "mergeHunks": List[MergeHunkTypeDef],
        "nextToken": str,
        "destinationCommitId": str,
        "sourceCommitId": str,
        "baseCommitId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PullRequestEventTypeDef = TypedDict(
    "PullRequestEventTypeDef",
    {
        "pullRequestId": NotRequired[str],
        "eventDate": NotRequired[datetime],
        "pullRequestEventType": NotRequired[PullRequestEventTypeType],
        "actorArn": NotRequired[str],
        "pullRequestCreatedEventMetadata": NotRequired[PullRequestCreatedEventMetadataTypeDef],
        "pullRequestStatusChangedEventMetadata": NotRequired[
            PullRequestStatusChangedEventMetadataTypeDef
        ],
        "pullRequestSourceReferenceUpdatedEventMetadata": NotRequired[
            PullRequestSourceReferenceUpdatedEventMetadataTypeDef
        ],
        "pullRequestMergedStateChangedEventMetadata": NotRequired[
            PullRequestMergedStateChangedEventMetadataTypeDef
        ],
        "approvalRuleEventMetadata": NotRequired[ApprovalRuleEventMetadataTypeDef],
        "approvalStateChangedEventMetadata": NotRequired[ApprovalStateChangedEventMetadataTypeDef],
        "approvalRuleOverriddenEventMetadata": NotRequired[
            ApprovalRuleOverriddenEventMetadataTypeDef
        ],
    },
)
PullRequestTypeDef = TypedDict(
    "PullRequestTypeDef",
    {
        "pullRequestId": NotRequired[str],
        "title": NotRequired[str],
        "description": NotRequired[str],
        "lastActivityDate": NotRequired[datetime],
        "creationDate": NotRequired[datetime],
        "pullRequestStatus": NotRequired[PullRequestStatusEnumType],
        "authorArn": NotRequired[str],
        "pullRequestTargets": NotRequired[List[PullRequestTargetTypeDef]],
        "clientRequestToken": NotRequired[str],
        "revisionId": NotRequired[str],
        "approvalRules": NotRequired[List[ApprovalRuleTypeDef]],
    },
)
CreateCommitInputRequestTypeDef = TypedDict(
    "CreateCommitInputRequestTypeDef",
    {
        "repositoryName": str,
        "branchName": str,
        "parentCommitId": NotRequired[str],
        "authorName": NotRequired[str],
        "email": NotRequired[str],
        "commitMessage": NotRequired[str],
        "keepEmptyFolders": NotRequired[bool],
        "putFiles": NotRequired[Sequence[PutFileEntryTypeDef]],
        "deleteFiles": NotRequired[Sequence[DeleteFileEntryTypeDef]],
        "setFileModes": NotRequired[Sequence[SetFileModeEntryTypeDef]],
    },
)
GetCommentReactionsOutputTypeDef = TypedDict(
    "GetCommentReactionsOutputTypeDef",
    {
        "reactionsForComment": List[ReactionForCommentTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutRepositoryTriggersInputRequestTypeDef = TypedDict(
    "PutRepositoryTriggersInputRequestTypeDef",
    {
        "repositoryName": str,
        "triggers": Sequence[RepositoryTriggerUnionTypeDef],
    },
)
CreateUnreferencedMergeCommitInputRequestTypeDef = TypedDict(
    "CreateUnreferencedMergeCommitInputRequestTypeDef",
    {
        "repositoryName": str,
        "sourceCommitSpecifier": str,
        "destinationCommitSpecifier": str,
        "mergeOption": MergeOptionTypeEnumType,
        "conflictDetailLevel": NotRequired[ConflictDetailLevelTypeEnumType],
        "conflictResolutionStrategy": NotRequired[ConflictResolutionStrategyTypeEnumType],
        "authorName": NotRequired[str],
        "email": NotRequired[str],
        "commitMessage": NotRequired[str],
        "keepEmptyFolders": NotRequired[bool],
        "conflictResolution": NotRequired[ConflictResolutionTypeDef],
    },
)
MergeBranchesBySquashInputRequestTypeDef = TypedDict(
    "MergeBranchesBySquashInputRequestTypeDef",
    {
        "repositoryName": str,
        "sourceCommitSpecifier": str,
        "destinationCommitSpecifier": str,
        "targetBranch": NotRequired[str],
        "conflictDetailLevel": NotRequired[ConflictDetailLevelTypeEnumType],
        "conflictResolutionStrategy": NotRequired[ConflictResolutionStrategyTypeEnumType],
        "authorName": NotRequired[str],
        "email": NotRequired[str],
        "commitMessage": NotRequired[str],
        "keepEmptyFolders": NotRequired[bool],
        "conflictResolution": NotRequired[ConflictResolutionTypeDef],
    },
)
MergeBranchesByThreeWayInputRequestTypeDef = TypedDict(
    "MergeBranchesByThreeWayInputRequestTypeDef",
    {
        "repositoryName": str,
        "sourceCommitSpecifier": str,
        "destinationCommitSpecifier": str,
        "targetBranch": NotRequired[str],
        "conflictDetailLevel": NotRequired[ConflictDetailLevelTypeEnumType],
        "conflictResolutionStrategy": NotRequired[ConflictResolutionStrategyTypeEnumType],
        "authorName": NotRequired[str],
        "email": NotRequired[str],
        "commitMessage": NotRequired[str],
        "keepEmptyFolders": NotRequired[bool],
        "conflictResolution": NotRequired[ConflictResolutionTypeDef],
    },
)
MergePullRequestBySquashInputRequestTypeDef = TypedDict(
    "MergePullRequestBySquashInputRequestTypeDef",
    {
        "pullRequestId": str,
        "repositoryName": str,
        "sourceCommitId": NotRequired[str],
        "conflictDetailLevel": NotRequired[ConflictDetailLevelTypeEnumType],
        "conflictResolutionStrategy": NotRequired[ConflictResolutionStrategyTypeEnumType],
        "commitMessage": NotRequired[str],
        "authorName": NotRequired[str],
        "email": NotRequired[str],
        "keepEmptyFolders": NotRequired[bool],
        "conflictResolution": NotRequired[ConflictResolutionTypeDef],
    },
)
MergePullRequestByThreeWayInputRequestTypeDef = TypedDict(
    "MergePullRequestByThreeWayInputRequestTypeDef",
    {
        "pullRequestId": str,
        "repositoryName": str,
        "sourceCommitId": NotRequired[str],
        "conflictDetailLevel": NotRequired[ConflictDetailLevelTypeEnumType],
        "conflictResolutionStrategy": NotRequired[ConflictResolutionStrategyTypeEnumType],
        "commitMessage": NotRequired[str],
        "authorName": NotRequired[str],
        "email": NotRequired[str],
        "keepEmptyFolders": NotRequired[bool],
        "conflictResolution": NotRequired[ConflictResolutionTypeDef],
    },
)
ListFileCommitHistoryResponseTypeDef = TypedDict(
    "ListFileCommitHistoryResponseTypeDef",
    {
        "revisionDag": List[FileVersionTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDescribeMergeConflictsOutputTypeDef = TypedDict(
    "BatchDescribeMergeConflictsOutputTypeDef",
    {
        "conflicts": List[ConflictTypeDef],
        "nextToken": str,
        "errors": List[BatchDescribeMergeConflictsErrorTypeDef],
        "destinationCommitId": str,
        "sourceCommitId": str,
        "baseCommitId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePullRequestEventsOutputTypeDef = TypedDict(
    "DescribePullRequestEventsOutputTypeDef",
    {
        "pullRequestEvents": List[PullRequestEventTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePullRequestOutputTypeDef = TypedDict(
    "CreatePullRequestOutputTypeDef",
    {
        "pullRequest": PullRequestTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPullRequestOutputTypeDef = TypedDict(
    "GetPullRequestOutputTypeDef",
    {
        "pullRequest": PullRequestTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MergePullRequestByFastForwardOutputTypeDef = TypedDict(
    "MergePullRequestByFastForwardOutputTypeDef",
    {
        "pullRequest": PullRequestTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MergePullRequestBySquashOutputTypeDef = TypedDict(
    "MergePullRequestBySquashOutputTypeDef",
    {
        "pullRequest": PullRequestTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MergePullRequestByThreeWayOutputTypeDef = TypedDict(
    "MergePullRequestByThreeWayOutputTypeDef",
    {
        "pullRequest": PullRequestTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePullRequestDescriptionOutputTypeDef = TypedDict(
    "UpdatePullRequestDescriptionOutputTypeDef",
    {
        "pullRequest": PullRequestTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePullRequestStatusOutputTypeDef = TypedDict(
    "UpdatePullRequestStatusOutputTypeDef",
    {
        "pullRequest": PullRequestTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePullRequestTitleOutputTypeDef = TypedDict(
    "UpdatePullRequestTitleOutputTypeDef",
    {
        "pullRequest": PullRequestTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
