"""
Type annotations for quicksight service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_quicksight.client import QuickSightClient

    session = Session()
    client: QuickSightClient = session.client("quicksight")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    DescribeFolderPermissionsPaginator,
    DescribeFolderResolvedPermissionsPaginator,
    ListAnalysesPaginator,
    ListAssetBundleExportJobsPaginator,
    ListAssetBundleImportJobsPaginator,
    ListDashboardsPaginator,
    ListDashboardVersionsPaginator,
    ListDataSetsPaginator,
    ListDataSourcesPaginator,
    ListFolderMembersPaginator,
    ListFoldersForResourcePaginator,
    ListFoldersPaginator,
    ListGroupMembershipsPaginator,
    ListGroupsPaginator,
    ListIAMPolicyAssignmentsForUserPaginator,
    ListIAMPolicyAssignmentsPaginator,
    ListIngestionsPaginator,
    ListNamespacesPaginator,
    ListRoleMembershipsPaginator,
    ListTemplateAliasesPaginator,
    ListTemplatesPaginator,
    ListTemplateVersionsPaginator,
    ListThemesPaginator,
    ListThemeVersionsPaginator,
    ListUserGroupsPaginator,
    ListUsersPaginator,
    SearchAnalysesPaginator,
    SearchDashboardsPaginator,
    SearchDataSetsPaginator,
    SearchDataSourcesPaginator,
    SearchFoldersPaginator,
    SearchGroupsPaginator,
)
from .type_defs import (
    BatchCreateTopicReviewedAnswerRequestRequestTypeDef,
    BatchCreateTopicReviewedAnswerResponseTypeDef,
    BatchDeleteTopicReviewedAnswerRequestRequestTypeDef,
    BatchDeleteTopicReviewedAnswerResponseTypeDef,
    CancelIngestionRequestRequestTypeDef,
    CancelIngestionResponseTypeDef,
    CreateAccountCustomizationRequestRequestTypeDef,
    CreateAccountCustomizationResponseTypeDef,
    CreateAccountSubscriptionRequestRequestTypeDef,
    CreateAccountSubscriptionResponseTypeDef,
    CreateAnalysisRequestRequestTypeDef,
    CreateAnalysisResponseTypeDef,
    CreateDashboardRequestRequestTypeDef,
    CreateDashboardResponseTypeDef,
    CreateDataSetRequestRequestTypeDef,
    CreateDataSetResponseTypeDef,
    CreateDataSourceRequestRequestTypeDef,
    CreateDataSourceResponseTypeDef,
    CreateFolderMembershipRequestRequestTypeDef,
    CreateFolderMembershipResponseTypeDef,
    CreateFolderRequestRequestTypeDef,
    CreateFolderResponseTypeDef,
    CreateGroupMembershipRequestRequestTypeDef,
    CreateGroupMembershipResponseTypeDef,
    CreateGroupRequestRequestTypeDef,
    CreateGroupResponseTypeDef,
    CreateIAMPolicyAssignmentRequestRequestTypeDef,
    CreateIAMPolicyAssignmentResponseTypeDef,
    CreateIngestionRequestRequestTypeDef,
    CreateIngestionResponseTypeDef,
    CreateNamespaceRequestRequestTypeDef,
    CreateNamespaceResponseTypeDef,
    CreateRefreshScheduleRequestRequestTypeDef,
    CreateRefreshScheduleResponseTypeDef,
    CreateRoleMembershipRequestRequestTypeDef,
    CreateRoleMembershipResponseTypeDef,
    CreateTemplateAliasRequestRequestTypeDef,
    CreateTemplateAliasResponseTypeDef,
    CreateTemplateRequestRequestTypeDef,
    CreateTemplateResponseTypeDef,
    CreateThemeAliasRequestRequestTypeDef,
    CreateThemeAliasResponseTypeDef,
    CreateThemeRequestRequestTypeDef,
    CreateThemeResponseTypeDef,
    CreateTopicRefreshScheduleRequestRequestTypeDef,
    CreateTopicRefreshScheduleResponseTypeDef,
    CreateTopicRequestRequestTypeDef,
    CreateTopicResponseTypeDef,
    CreateVPCConnectionRequestRequestTypeDef,
    CreateVPCConnectionResponseTypeDef,
    DeleteAccountCustomizationRequestRequestTypeDef,
    DeleteAccountCustomizationResponseTypeDef,
    DeleteAccountSubscriptionRequestRequestTypeDef,
    DeleteAccountSubscriptionResponseTypeDef,
    DeleteAnalysisRequestRequestTypeDef,
    DeleteAnalysisResponseTypeDef,
    DeleteDashboardRequestRequestTypeDef,
    DeleteDashboardResponseTypeDef,
    DeleteDataSetRefreshPropertiesRequestRequestTypeDef,
    DeleteDataSetRefreshPropertiesResponseTypeDef,
    DeleteDataSetRequestRequestTypeDef,
    DeleteDataSetResponseTypeDef,
    DeleteDataSourceRequestRequestTypeDef,
    DeleteDataSourceResponseTypeDef,
    DeleteFolderMembershipRequestRequestTypeDef,
    DeleteFolderMembershipResponseTypeDef,
    DeleteFolderRequestRequestTypeDef,
    DeleteFolderResponseTypeDef,
    DeleteGroupMembershipRequestRequestTypeDef,
    DeleteGroupMembershipResponseTypeDef,
    DeleteGroupRequestRequestTypeDef,
    DeleteGroupResponseTypeDef,
    DeleteIAMPolicyAssignmentRequestRequestTypeDef,
    DeleteIAMPolicyAssignmentResponseTypeDef,
    DeleteIdentityPropagationConfigRequestRequestTypeDef,
    DeleteIdentityPropagationConfigResponseTypeDef,
    DeleteNamespaceRequestRequestTypeDef,
    DeleteNamespaceResponseTypeDef,
    DeleteRefreshScheduleRequestRequestTypeDef,
    DeleteRefreshScheduleResponseTypeDef,
    DeleteRoleCustomPermissionRequestRequestTypeDef,
    DeleteRoleCustomPermissionResponseTypeDef,
    DeleteRoleMembershipRequestRequestTypeDef,
    DeleteRoleMembershipResponseTypeDef,
    DeleteTemplateAliasRequestRequestTypeDef,
    DeleteTemplateAliasResponseTypeDef,
    DeleteTemplateRequestRequestTypeDef,
    DeleteTemplateResponseTypeDef,
    DeleteThemeAliasRequestRequestTypeDef,
    DeleteThemeAliasResponseTypeDef,
    DeleteThemeRequestRequestTypeDef,
    DeleteThemeResponseTypeDef,
    DeleteTopicRefreshScheduleRequestRequestTypeDef,
    DeleteTopicRefreshScheduleResponseTypeDef,
    DeleteTopicRequestRequestTypeDef,
    DeleteTopicResponseTypeDef,
    DeleteUserByPrincipalIdRequestRequestTypeDef,
    DeleteUserByPrincipalIdResponseTypeDef,
    DeleteUserRequestRequestTypeDef,
    DeleteUserResponseTypeDef,
    DeleteVPCConnectionRequestRequestTypeDef,
    DeleteVPCConnectionResponseTypeDef,
    DescribeAccountCustomizationRequestRequestTypeDef,
    DescribeAccountCustomizationResponseTypeDef,
    DescribeAccountSettingsRequestRequestTypeDef,
    DescribeAccountSettingsResponseTypeDef,
    DescribeAccountSubscriptionRequestRequestTypeDef,
    DescribeAccountSubscriptionResponseTypeDef,
    DescribeAnalysisDefinitionRequestRequestTypeDef,
    DescribeAnalysisDefinitionResponseTypeDef,
    DescribeAnalysisPermissionsRequestRequestTypeDef,
    DescribeAnalysisPermissionsResponseTypeDef,
    DescribeAnalysisRequestRequestTypeDef,
    DescribeAnalysisResponseTypeDef,
    DescribeAssetBundleExportJobRequestRequestTypeDef,
    DescribeAssetBundleExportJobResponseTypeDef,
    DescribeAssetBundleImportJobRequestRequestTypeDef,
    DescribeAssetBundleImportJobResponseTypeDef,
    DescribeDashboardDefinitionRequestRequestTypeDef,
    DescribeDashboardDefinitionResponseTypeDef,
    DescribeDashboardPermissionsRequestRequestTypeDef,
    DescribeDashboardPermissionsResponseTypeDef,
    DescribeDashboardRequestRequestTypeDef,
    DescribeDashboardResponseTypeDef,
    DescribeDashboardSnapshotJobRequestRequestTypeDef,
    DescribeDashboardSnapshotJobResponseTypeDef,
    DescribeDashboardSnapshotJobResultRequestRequestTypeDef,
    DescribeDashboardSnapshotJobResultResponseTypeDef,
    DescribeDataSetPermissionsRequestRequestTypeDef,
    DescribeDataSetPermissionsResponseTypeDef,
    DescribeDataSetRefreshPropertiesRequestRequestTypeDef,
    DescribeDataSetRefreshPropertiesResponseTypeDef,
    DescribeDataSetRequestRequestTypeDef,
    DescribeDataSetResponseTypeDef,
    DescribeDataSourcePermissionsRequestRequestTypeDef,
    DescribeDataSourcePermissionsResponseTypeDef,
    DescribeDataSourceRequestRequestTypeDef,
    DescribeDataSourceResponseTypeDef,
    DescribeFolderPermissionsRequestRequestTypeDef,
    DescribeFolderPermissionsResponseTypeDef,
    DescribeFolderRequestRequestTypeDef,
    DescribeFolderResolvedPermissionsRequestRequestTypeDef,
    DescribeFolderResolvedPermissionsResponseTypeDef,
    DescribeFolderResponseTypeDef,
    DescribeGroupMembershipRequestRequestTypeDef,
    DescribeGroupMembershipResponseTypeDef,
    DescribeGroupRequestRequestTypeDef,
    DescribeGroupResponseTypeDef,
    DescribeIAMPolicyAssignmentRequestRequestTypeDef,
    DescribeIAMPolicyAssignmentResponseTypeDef,
    DescribeIngestionRequestRequestTypeDef,
    DescribeIngestionResponseTypeDef,
    DescribeIpRestrictionRequestRequestTypeDef,
    DescribeIpRestrictionResponseTypeDef,
    DescribeKeyRegistrationRequestRequestTypeDef,
    DescribeKeyRegistrationResponseTypeDef,
    DescribeNamespaceRequestRequestTypeDef,
    DescribeNamespaceResponseTypeDef,
    DescribeQPersonalizationConfigurationRequestRequestTypeDef,
    DescribeQPersonalizationConfigurationResponseTypeDef,
    DescribeRefreshScheduleRequestRequestTypeDef,
    DescribeRefreshScheduleResponseTypeDef,
    DescribeRoleCustomPermissionRequestRequestTypeDef,
    DescribeRoleCustomPermissionResponseTypeDef,
    DescribeTemplateAliasRequestRequestTypeDef,
    DescribeTemplateAliasResponseTypeDef,
    DescribeTemplateDefinitionRequestRequestTypeDef,
    DescribeTemplateDefinitionResponseTypeDef,
    DescribeTemplatePermissionsRequestRequestTypeDef,
    DescribeTemplatePermissionsResponseTypeDef,
    DescribeTemplateRequestRequestTypeDef,
    DescribeTemplateResponseTypeDef,
    DescribeThemeAliasRequestRequestTypeDef,
    DescribeThemeAliasResponseTypeDef,
    DescribeThemePermissionsRequestRequestTypeDef,
    DescribeThemePermissionsResponseTypeDef,
    DescribeThemeRequestRequestTypeDef,
    DescribeThemeResponseTypeDef,
    DescribeTopicPermissionsRequestRequestTypeDef,
    DescribeTopicPermissionsResponseTypeDef,
    DescribeTopicRefreshRequestRequestTypeDef,
    DescribeTopicRefreshResponseTypeDef,
    DescribeTopicRefreshScheduleRequestRequestTypeDef,
    DescribeTopicRefreshScheduleResponseTypeDef,
    DescribeTopicRequestRequestTypeDef,
    DescribeTopicResponseTypeDef,
    DescribeUserRequestRequestTypeDef,
    DescribeUserResponseTypeDef,
    DescribeVPCConnectionRequestRequestTypeDef,
    DescribeVPCConnectionResponseTypeDef,
    GenerateEmbedUrlForAnonymousUserRequestRequestTypeDef,
    GenerateEmbedUrlForAnonymousUserResponseTypeDef,
    GenerateEmbedUrlForRegisteredUserRequestRequestTypeDef,
    GenerateEmbedUrlForRegisteredUserResponseTypeDef,
    GetDashboardEmbedUrlRequestRequestTypeDef,
    GetDashboardEmbedUrlResponseTypeDef,
    GetSessionEmbedUrlRequestRequestTypeDef,
    GetSessionEmbedUrlResponseTypeDef,
    ListAnalysesRequestRequestTypeDef,
    ListAnalysesResponseTypeDef,
    ListAssetBundleExportJobsRequestRequestTypeDef,
    ListAssetBundleExportJobsResponseTypeDef,
    ListAssetBundleImportJobsRequestRequestTypeDef,
    ListAssetBundleImportJobsResponseTypeDef,
    ListDashboardsRequestRequestTypeDef,
    ListDashboardsResponseTypeDef,
    ListDashboardVersionsRequestRequestTypeDef,
    ListDashboardVersionsResponseTypeDef,
    ListDataSetsRequestRequestTypeDef,
    ListDataSetsResponseTypeDef,
    ListDataSourcesRequestRequestTypeDef,
    ListDataSourcesResponseTypeDef,
    ListFolderMembersRequestRequestTypeDef,
    ListFolderMembersResponseTypeDef,
    ListFoldersForResourceRequestRequestTypeDef,
    ListFoldersForResourceResponseTypeDef,
    ListFoldersRequestRequestTypeDef,
    ListFoldersResponseTypeDef,
    ListGroupMembershipsRequestRequestTypeDef,
    ListGroupMembershipsResponseTypeDef,
    ListGroupsRequestRequestTypeDef,
    ListGroupsResponseTypeDef,
    ListIAMPolicyAssignmentsForUserRequestRequestTypeDef,
    ListIAMPolicyAssignmentsForUserResponseTypeDef,
    ListIAMPolicyAssignmentsRequestRequestTypeDef,
    ListIAMPolicyAssignmentsResponseTypeDef,
    ListIdentityPropagationConfigsRequestRequestTypeDef,
    ListIdentityPropagationConfigsResponseTypeDef,
    ListIngestionsRequestRequestTypeDef,
    ListIngestionsResponseTypeDef,
    ListNamespacesRequestRequestTypeDef,
    ListNamespacesResponseTypeDef,
    ListRefreshSchedulesRequestRequestTypeDef,
    ListRefreshSchedulesResponseTypeDef,
    ListRoleMembershipsRequestRequestTypeDef,
    ListRoleMembershipsResponseTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTemplateAliasesRequestRequestTypeDef,
    ListTemplateAliasesResponseTypeDef,
    ListTemplatesRequestRequestTypeDef,
    ListTemplatesResponseTypeDef,
    ListTemplateVersionsRequestRequestTypeDef,
    ListTemplateVersionsResponseTypeDef,
    ListThemeAliasesRequestRequestTypeDef,
    ListThemeAliasesResponseTypeDef,
    ListThemesRequestRequestTypeDef,
    ListThemesResponseTypeDef,
    ListThemeVersionsRequestRequestTypeDef,
    ListThemeVersionsResponseTypeDef,
    ListTopicRefreshSchedulesRequestRequestTypeDef,
    ListTopicRefreshSchedulesResponseTypeDef,
    ListTopicReviewedAnswersRequestRequestTypeDef,
    ListTopicReviewedAnswersResponseTypeDef,
    ListTopicsRequestRequestTypeDef,
    ListTopicsResponseTypeDef,
    ListUserGroupsRequestRequestTypeDef,
    ListUserGroupsResponseTypeDef,
    ListUsersRequestRequestTypeDef,
    ListUsersResponseTypeDef,
    ListVPCConnectionsRequestRequestTypeDef,
    ListVPCConnectionsResponseTypeDef,
    PutDataSetRefreshPropertiesRequestRequestTypeDef,
    PutDataSetRefreshPropertiesResponseTypeDef,
    RegisterUserRequestRequestTypeDef,
    RegisterUserResponseTypeDef,
    RestoreAnalysisRequestRequestTypeDef,
    RestoreAnalysisResponseTypeDef,
    SearchAnalysesRequestRequestTypeDef,
    SearchAnalysesResponseTypeDef,
    SearchDashboardsRequestRequestTypeDef,
    SearchDashboardsResponseTypeDef,
    SearchDataSetsRequestRequestTypeDef,
    SearchDataSetsResponseTypeDef,
    SearchDataSourcesRequestRequestTypeDef,
    SearchDataSourcesResponseTypeDef,
    SearchFoldersRequestRequestTypeDef,
    SearchFoldersResponseTypeDef,
    SearchGroupsRequestRequestTypeDef,
    SearchGroupsResponseTypeDef,
    StartAssetBundleExportJobRequestRequestTypeDef,
    StartAssetBundleExportJobResponseTypeDef,
    StartAssetBundleImportJobRequestRequestTypeDef,
    StartAssetBundleImportJobResponseTypeDef,
    StartDashboardSnapshotJobRequestRequestTypeDef,
    StartDashboardSnapshotJobResponseTypeDef,
    StartDashboardSnapshotJobScheduleRequestRequestTypeDef,
    StartDashboardSnapshotJobScheduleResponseTypeDef,
    TagResourceRequestRequestTypeDef,
    TagResourceResponseTypeDef,
    UntagResourceRequestRequestTypeDef,
    UntagResourceResponseTypeDef,
    UpdateAccountCustomizationRequestRequestTypeDef,
    UpdateAccountCustomizationResponseTypeDef,
    UpdateAccountSettingsRequestRequestTypeDef,
    UpdateAccountSettingsResponseTypeDef,
    UpdateAnalysisPermissionsRequestRequestTypeDef,
    UpdateAnalysisPermissionsResponseTypeDef,
    UpdateAnalysisRequestRequestTypeDef,
    UpdateAnalysisResponseTypeDef,
    UpdateDashboardLinksRequestRequestTypeDef,
    UpdateDashboardLinksResponseTypeDef,
    UpdateDashboardPermissionsRequestRequestTypeDef,
    UpdateDashboardPermissionsResponseTypeDef,
    UpdateDashboardPublishedVersionRequestRequestTypeDef,
    UpdateDashboardPublishedVersionResponseTypeDef,
    UpdateDashboardRequestRequestTypeDef,
    UpdateDashboardResponseTypeDef,
    UpdateDataSetPermissionsRequestRequestTypeDef,
    UpdateDataSetPermissionsResponseTypeDef,
    UpdateDataSetRequestRequestTypeDef,
    UpdateDataSetResponseTypeDef,
    UpdateDataSourcePermissionsRequestRequestTypeDef,
    UpdateDataSourcePermissionsResponseTypeDef,
    UpdateDataSourceRequestRequestTypeDef,
    UpdateDataSourceResponseTypeDef,
    UpdateFolderPermissionsRequestRequestTypeDef,
    UpdateFolderPermissionsResponseTypeDef,
    UpdateFolderRequestRequestTypeDef,
    UpdateFolderResponseTypeDef,
    UpdateGroupRequestRequestTypeDef,
    UpdateGroupResponseTypeDef,
    UpdateIAMPolicyAssignmentRequestRequestTypeDef,
    UpdateIAMPolicyAssignmentResponseTypeDef,
    UpdateIdentityPropagationConfigRequestRequestTypeDef,
    UpdateIdentityPropagationConfigResponseTypeDef,
    UpdateIpRestrictionRequestRequestTypeDef,
    UpdateIpRestrictionResponseTypeDef,
    UpdateKeyRegistrationRequestRequestTypeDef,
    UpdateKeyRegistrationResponseTypeDef,
    UpdatePublicSharingSettingsRequestRequestTypeDef,
    UpdatePublicSharingSettingsResponseTypeDef,
    UpdateQPersonalizationConfigurationRequestRequestTypeDef,
    UpdateQPersonalizationConfigurationResponseTypeDef,
    UpdateRefreshScheduleRequestRequestTypeDef,
    UpdateRefreshScheduleResponseTypeDef,
    UpdateRoleCustomPermissionRequestRequestTypeDef,
    UpdateRoleCustomPermissionResponseTypeDef,
    UpdateSPICECapacityConfigurationRequestRequestTypeDef,
    UpdateSPICECapacityConfigurationResponseTypeDef,
    UpdateTemplateAliasRequestRequestTypeDef,
    UpdateTemplateAliasResponseTypeDef,
    UpdateTemplatePermissionsRequestRequestTypeDef,
    UpdateTemplatePermissionsResponseTypeDef,
    UpdateTemplateRequestRequestTypeDef,
    UpdateTemplateResponseTypeDef,
    UpdateThemeAliasRequestRequestTypeDef,
    UpdateThemeAliasResponseTypeDef,
    UpdateThemePermissionsRequestRequestTypeDef,
    UpdateThemePermissionsResponseTypeDef,
    UpdateThemeRequestRequestTypeDef,
    UpdateThemeResponseTypeDef,
    UpdateTopicPermissionsRequestRequestTypeDef,
    UpdateTopicPermissionsResponseTypeDef,
    UpdateTopicRefreshScheduleRequestRequestTypeDef,
    UpdateTopicRefreshScheduleResponseTypeDef,
    UpdateTopicRequestRequestTypeDef,
    UpdateTopicResponseTypeDef,
    UpdateUserRequestRequestTypeDef,
    UpdateUserResponseTypeDef,
    UpdateVPCConnectionRequestRequestTypeDef,
    UpdateVPCConnectionResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("QuickSightClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentUpdatingException: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    CustomerManagedKeyUnavailableException: Type[BotocoreClientError]
    DomainNotWhitelistedException: Type[BotocoreClientError]
    IdentityTypeNotSupportedException: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    PreconditionNotMetException: Type[BotocoreClientError]
    QuickSightUserNotFoundException: Type[BotocoreClientError]
    ResourceExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceUnavailableException: Type[BotocoreClientError]
    SessionLifetimeInMinutesInvalidException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnsupportedPricingPlanException: Type[BotocoreClientError]
    UnsupportedUserEditionException: Type[BotocoreClientError]

class QuickSightClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        QuickSightClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#exceptions)
        """

    def batch_create_topic_reviewed_answer(
        self, **kwargs: Unpack[BatchCreateTopicReviewedAnswerRequestRequestTypeDef]
    ) -> BatchCreateTopicReviewedAnswerResponseTypeDef:
        """
        Creates new reviewed answers for a Q Topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.batch_create_topic_reviewed_answer)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#batch_create_topic_reviewed_answer)
        """

    def batch_delete_topic_reviewed_answer(
        self, **kwargs: Unpack[BatchDeleteTopicReviewedAnswerRequestRequestTypeDef]
    ) -> BatchDeleteTopicReviewedAnswerResponseTypeDef:
        """
        Deletes reviewed answers for Q Topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.batch_delete_topic_reviewed_answer)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#batch_delete_topic_reviewed_answer)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#can_paginate)
        """

    def cancel_ingestion(
        self, **kwargs: Unpack[CancelIngestionRequestRequestTypeDef]
    ) -> CancelIngestionResponseTypeDef:
        """
        Cancels an ongoing ingestion of data into SPICE.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.cancel_ingestion)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#cancel_ingestion)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#close)
        """

    def create_account_customization(
        self, **kwargs: Unpack[CreateAccountCustomizationRequestRequestTypeDef]
    ) -> CreateAccountCustomizationResponseTypeDef:
        """
        Creates Amazon QuickSight customizations for the current Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_account_customization)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#create_account_customization)
        """

    def create_account_subscription(
        self, **kwargs: Unpack[CreateAccountSubscriptionRequestRequestTypeDef]
    ) -> CreateAccountSubscriptionResponseTypeDef:
        """
        Creates an Amazon QuickSight account, or subscribes to Amazon QuickSight Q.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_account_subscription)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#create_account_subscription)
        """

    def create_analysis(
        self, **kwargs: Unpack[CreateAnalysisRequestRequestTypeDef]
    ) -> CreateAnalysisResponseTypeDef:
        """
        Creates an analysis in Amazon QuickSight.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_analysis)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#create_analysis)
        """

    def create_dashboard(
        self, **kwargs: Unpack[CreateDashboardRequestRequestTypeDef]
    ) -> CreateDashboardResponseTypeDef:
        """
        Creates a dashboard from either a template or directly with a
        `DashboardDefinition`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_dashboard)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#create_dashboard)
        """

    def create_data_set(
        self, **kwargs: Unpack[CreateDataSetRequestRequestTypeDef]
    ) -> CreateDataSetResponseTypeDef:
        """
        Creates a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_data_set)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#create_data_set)
        """

    def create_data_source(
        self, **kwargs: Unpack[CreateDataSourceRequestRequestTypeDef]
    ) -> CreateDataSourceResponseTypeDef:
        """
        Creates a data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_data_source)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#create_data_source)
        """

    def create_folder(
        self, **kwargs: Unpack[CreateFolderRequestRequestTypeDef]
    ) -> CreateFolderResponseTypeDef:
        """
        Creates an empty shared folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_folder)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#create_folder)
        """

    def create_folder_membership(
        self, **kwargs: Unpack[CreateFolderMembershipRequestRequestTypeDef]
    ) -> CreateFolderMembershipResponseTypeDef:
        """
        Adds an asset, such as a dashboard, analysis, or dataset into a folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_folder_membership)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#create_folder_membership)
        """

    def create_group(
        self, **kwargs: Unpack[CreateGroupRequestRequestTypeDef]
    ) -> CreateGroupResponseTypeDef:
        """
        Use the `CreateGroup` operation to create a group in Amazon QuickSight.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#create_group)
        """

    def create_group_membership(
        self, **kwargs: Unpack[CreateGroupMembershipRequestRequestTypeDef]
    ) -> CreateGroupMembershipResponseTypeDef:
        """
        Adds an Amazon QuickSight user to an Amazon QuickSight group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_group_membership)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#create_group_membership)
        """

    def create_iam_policy_assignment(
        self, **kwargs: Unpack[CreateIAMPolicyAssignmentRequestRequestTypeDef]
    ) -> CreateIAMPolicyAssignmentResponseTypeDef:
        """
        Creates an assignment with one specified IAM policy, identified by its Amazon
        Resource Name
        (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_iam_policy_assignment)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#create_iam_policy_assignment)
        """

    def create_ingestion(
        self, **kwargs: Unpack[CreateIngestionRequestRequestTypeDef]
    ) -> CreateIngestionResponseTypeDef:
        """
        Creates and starts a new SPICE ingestion for a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_ingestion)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#create_ingestion)
        """

    def create_namespace(
        self, **kwargs: Unpack[CreateNamespaceRequestRequestTypeDef]
    ) -> CreateNamespaceResponseTypeDef:
        """
        (Enterprise edition only) Creates a new namespace for you to use with Amazon
        QuickSight.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_namespace)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#create_namespace)
        """

    def create_refresh_schedule(
        self, **kwargs: Unpack[CreateRefreshScheduleRequestRequestTypeDef]
    ) -> CreateRefreshScheduleResponseTypeDef:
        """
        Creates a refresh schedule for a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_refresh_schedule)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#create_refresh_schedule)
        """

    def create_role_membership(
        self, **kwargs: Unpack[CreateRoleMembershipRequestRequestTypeDef]
    ) -> CreateRoleMembershipResponseTypeDef:
        """
        Use `CreateRoleMembership` to add an existing Amazon QuickSight group to an
        existing
        role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_role_membership)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#create_role_membership)
        """

    def create_template(
        self, **kwargs: Unpack[CreateTemplateRequestRequestTypeDef]
    ) -> CreateTemplateResponseTypeDef:
        """
        Creates a template either from a `TemplateDefinition` or from an existing
        Amazon QuickSight analysis or
        template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_template)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#create_template)
        """

    def create_template_alias(
        self, **kwargs: Unpack[CreateTemplateAliasRequestRequestTypeDef]
    ) -> CreateTemplateAliasResponseTypeDef:
        """
        Creates a template alias for a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_template_alias)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#create_template_alias)
        """

    def create_theme(
        self, **kwargs: Unpack[CreateThemeRequestRequestTypeDef]
    ) -> CreateThemeResponseTypeDef:
        """
        Creates a theme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_theme)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#create_theme)
        """

    def create_theme_alias(
        self, **kwargs: Unpack[CreateThemeAliasRequestRequestTypeDef]
    ) -> CreateThemeAliasResponseTypeDef:
        """
        Creates a theme alias for a theme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_theme_alias)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#create_theme_alias)
        """

    def create_topic(
        self, **kwargs: Unpack[CreateTopicRequestRequestTypeDef]
    ) -> CreateTopicResponseTypeDef:
        """
        Creates a new Q topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_topic)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#create_topic)
        """

    def create_topic_refresh_schedule(
        self, **kwargs: Unpack[CreateTopicRefreshScheduleRequestRequestTypeDef]
    ) -> CreateTopicRefreshScheduleResponseTypeDef:
        """
        Creates a topic refresh schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_topic_refresh_schedule)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#create_topic_refresh_schedule)
        """

    def create_vpc_connection(
        self, **kwargs: Unpack[CreateVPCConnectionRequestRequestTypeDef]
    ) -> CreateVPCConnectionResponseTypeDef:
        """
        Creates a new VPC connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.create_vpc_connection)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#create_vpc_connection)
        """

    def delete_account_customization(
        self, **kwargs: Unpack[DeleteAccountCustomizationRequestRequestTypeDef]
    ) -> DeleteAccountCustomizationResponseTypeDef:
        """
        Deletes all Amazon QuickSight customizations in this Amazon Web Services Region
        for the specified Amazon Web Services account and Amazon QuickSight
        namespace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_account_customization)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#delete_account_customization)
        """

    def delete_account_subscription(
        self, **kwargs: Unpack[DeleteAccountSubscriptionRequestRequestTypeDef]
    ) -> DeleteAccountSubscriptionResponseTypeDef:
        """
        Use the `DeleteAccountSubscription` operation to delete an Amazon QuickSight
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_account_subscription)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#delete_account_subscription)
        """

    def delete_analysis(
        self, **kwargs: Unpack[DeleteAnalysisRequestRequestTypeDef]
    ) -> DeleteAnalysisResponseTypeDef:
        """
        Deletes an analysis from Amazon QuickSight.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_analysis)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#delete_analysis)
        """

    def delete_dashboard(
        self, **kwargs: Unpack[DeleteDashboardRequestRequestTypeDef]
    ) -> DeleteDashboardResponseTypeDef:
        """
        Deletes a dashboard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_dashboard)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#delete_dashboard)
        """

    def delete_data_set(
        self, **kwargs: Unpack[DeleteDataSetRequestRequestTypeDef]
    ) -> DeleteDataSetResponseTypeDef:
        """
        Deletes a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_data_set)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#delete_data_set)
        """

    def delete_data_set_refresh_properties(
        self, **kwargs: Unpack[DeleteDataSetRefreshPropertiesRequestRequestTypeDef]
    ) -> DeleteDataSetRefreshPropertiesResponseTypeDef:
        """
        Deletes the dataset refresh properties of the dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_data_set_refresh_properties)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#delete_data_set_refresh_properties)
        """

    def delete_data_source(
        self, **kwargs: Unpack[DeleteDataSourceRequestRequestTypeDef]
    ) -> DeleteDataSourceResponseTypeDef:
        """
        Deletes the data source permanently.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_data_source)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#delete_data_source)
        """

    def delete_folder(
        self, **kwargs: Unpack[DeleteFolderRequestRequestTypeDef]
    ) -> DeleteFolderResponseTypeDef:
        """
        Deletes an empty folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_folder)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#delete_folder)
        """

    def delete_folder_membership(
        self, **kwargs: Unpack[DeleteFolderMembershipRequestRequestTypeDef]
    ) -> DeleteFolderMembershipResponseTypeDef:
        """
        Removes an asset, such as a dashboard, analysis, or dataset, from a folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_folder_membership)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#delete_folder_membership)
        """

    def delete_group(
        self, **kwargs: Unpack[DeleteGroupRequestRequestTypeDef]
    ) -> DeleteGroupResponseTypeDef:
        """
        Removes a user group from Amazon QuickSight.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#delete_group)
        """

    def delete_group_membership(
        self, **kwargs: Unpack[DeleteGroupMembershipRequestRequestTypeDef]
    ) -> DeleteGroupMembershipResponseTypeDef:
        """
        Removes a user from a group so that the user is no longer a member of the group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_group_membership)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#delete_group_membership)
        """

    def delete_iam_policy_assignment(
        self, **kwargs: Unpack[DeleteIAMPolicyAssignmentRequestRequestTypeDef]
    ) -> DeleteIAMPolicyAssignmentResponseTypeDef:
        """
        Deletes an existing IAM policy assignment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_iam_policy_assignment)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#delete_iam_policy_assignment)
        """

    def delete_identity_propagation_config(
        self, **kwargs: Unpack[DeleteIdentityPropagationConfigRequestRequestTypeDef]
    ) -> DeleteIdentityPropagationConfigResponseTypeDef:
        """
        Deletes all access scopes and authorized targets that are associated with a
        service from the Amazon QuickSight IAM Identity Center
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_identity_propagation_config)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#delete_identity_propagation_config)
        """

    def delete_namespace(
        self, **kwargs: Unpack[DeleteNamespaceRequestRequestTypeDef]
    ) -> DeleteNamespaceResponseTypeDef:
        """
        Deletes a namespace and the users and groups that are associated with the
        namespace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_namespace)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#delete_namespace)
        """

    def delete_refresh_schedule(
        self, **kwargs: Unpack[DeleteRefreshScheduleRequestRequestTypeDef]
    ) -> DeleteRefreshScheduleResponseTypeDef:
        """
        Deletes a refresh schedule from a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_refresh_schedule)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#delete_refresh_schedule)
        """

    def delete_role_custom_permission(
        self, **kwargs: Unpack[DeleteRoleCustomPermissionRequestRequestTypeDef]
    ) -> DeleteRoleCustomPermissionResponseTypeDef:
        """
        Removes custom permissions from the role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_role_custom_permission)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#delete_role_custom_permission)
        """

    def delete_role_membership(
        self, **kwargs: Unpack[DeleteRoleMembershipRequestRequestTypeDef]
    ) -> DeleteRoleMembershipResponseTypeDef:
        """
        Removes a group from a role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_role_membership)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#delete_role_membership)
        """

    def delete_template(
        self, **kwargs: Unpack[DeleteTemplateRequestRequestTypeDef]
    ) -> DeleteTemplateResponseTypeDef:
        """
        Deletes a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_template)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#delete_template)
        """

    def delete_template_alias(
        self, **kwargs: Unpack[DeleteTemplateAliasRequestRequestTypeDef]
    ) -> DeleteTemplateAliasResponseTypeDef:
        """
        Deletes the item that the specified template alias points to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_template_alias)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#delete_template_alias)
        """

    def delete_theme(
        self, **kwargs: Unpack[DeleteThemeRequestRequestTypeDef]
    ) -> DeleteThemeResponseTypeDef:
        """
        Deletes a theme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_theme)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#delete_theme)
        """

    def delete_theme_alias(
        self, **kwargs: Unpack[DeleteThemeAliasRequestRequestTypeDef]
    ) -> DeleteThemeAliasResponseTypeDef:
        """
        Deletes the version of the theme that the specified theme alias points to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_theme_alias)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#delete_theme_alias)
        """

    def delete_topic(
        self, **kwargs: Unpack[DeleteTopicRequestRequestTypeDef]
    ) -> DeleteTopicResponseTypeDef:
        """
        Deletes a topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_topic)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#delete_topic)
        """

    def delete_topic_refresh_schedule(
        self, **kwargs: Unpack[DeleteTopicRefreshScheduleRequestRequestTypeDef]
    ) -> DeleteTopicRefreshScheduleResponseTypeDef:
        """
        Deletes a topic refresh schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_topic_refresh_schedule)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#delete_topic_refresh_schedule)
        """

    def delete_user(
        self, **kwargs: Unpack[DeleteUserRequestRequestTypeDef]
    ) -> DeleteUserResponseTypeDef:
        """
        Deletes the Amazon QuickSight user that is associated with the identity of the
        IAM user or role that's making the
        call.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_user)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#delete_user)
        """

    def delete_user_by_principal_id(
        self, **kwargs: Unpack[DeleteUserByPrincipalIdRequestRequestTypeDef]
    ) -> DeleteUserByPrincipalIdResponseTypeDef:
        """
        Deletes a user identified by its principal ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_user_by_principal_id)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#delete_user_by_principal_id)
        """

    def delete_vpc_connection(
        self, **kwargs: Unpack[DeleteVPCConnectionRequestRequestTypeDef]
    ) -> DeleteVPCConnectionResponseTypeDef:
        """
        Deletes a VPC connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.delete_vpc_connection)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#delete_vpc_connection)
        """

    def describe_account_customization(
        self, **kwargs: Unpack[DescribeAccountCustomizationRequestRequestTypeDef]
    ) -> DescribeAccountCustomizationResponseTypeDef:
        """
        Describes the customizations associated with the provided Amazon Web Services
        account and Amazon Amazon QuickSight namespace in an Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_account_customization)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_account_customization)
        """

    def describe_account_settings(
        self, **kwargs: Unpack[DescribeAccountSettingsRequestRequestTypeDef]
    ) -> DescribeAccountSettingsResponseTypeDef:
        """
        Describes the settings that were used when your Amazon QuickSight subscription
        was first created in this Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_account_settings)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_account_settings)
        """

    def describe_account_subscription(
        self, **kwargs: Unpack[DescribeAccountSubscriptionRequestRequestTypeDef]
    ) -> DescribeAccountSubscriptionResponseTypeDef:
        """
        Use the DescribeAccountSubscription operation to receive a description of an
        Amazon QuickSight account's
        subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_account_subscription)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_account_subscription)
        """

    def describe_analysis(
        self, **kwargs: Unpack[DescribeAnalysisRequestRequestTypeDef]
    ) -> DescribeAnalysisResponseTypeDef:
        """
        Provides a summary of the metadata for an analysis.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_analysis)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_analysis)
        """

    def describe_analysis_definition(
        self, **kwargs: Unpack[DescribeAnalysisDefinitionRequestRequestTypeDef]
    ) -> DescribeAnalysisDefinitionResponseTypeDef:
        """
        Provides a detailed description of the definition of an analysis.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_analysis_definition)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_analysis_definition)
        """

    def describe_analysis_permissions(
        self, **kwargs: Unpack[DescribeAnalysisPermissionsRequestRequestTypeDef]
    ) -> DescribeAnalysisPermissionsResponseTypeDef:
        """
        Provides the read and write permissions for an analysis.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_analysis_permissions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_analysis_permissions)
        """

    def describe_asset_bundle_export_job(
        self, **kwargs: Unpack[DescribeAssetBundleExportJobRequestRequestTypeDef]
    ) -> DescribeAssetBundleExportJobResponseTypeDef:
        """
        Describes an existing export job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_asset_bundle_export_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_asset_bundle_export_job)
        """

    def describe_asset_bundle_import_job(
        self, **kwargs: Unpack[DescribeAssetBundleImportJobRequestRequestTypeDef]
    ) -> DescribeAssetBundleImportJobResponseTypeDef:
        """
        Describes an existing import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_asset_bundle_import_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_asset_bundle_import_job)
        """

    def describe_dashboard(
        self, **kwargs: Unpack[DescribeDashboardRequestRequestTypeDef]
    ) -> DescribeDashboardResponseTypeDef:
        """
        Provides a summary for a dashboard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_dashboard)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_dashboard)
        """

    def describe_dashboard_definition(
        self, **kwargs: Unpack[DescribeDashboardDefinitionRequestRequestTypeDef]
    ) -> DescribeDashboardDefinitionResponseTypeDef:
        """
        Provides a detailed description of the definition of a dashboard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_dashboard_definition)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_dashboard_definition)
        """

    def describe_dashboard_permissions(
        self, **kwargs: Unpack[DescribeDashboardPermissionsRequestRequestTypeDef]
    ) -> DescribeDashboardPermissionsResponseTypeDef:
        """
        Describes read and write permissions for a dashboard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_dashboard_permissions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_dashboard_permissions)
        """

    def describe_dashboard_snapshot_job(
        self, **kwargs: Unpack[DescribeDashboardSnapshotJobRequestRequestTypeDef]
    ) -> DescribeDashboardSnapshotJobResponseTypeDef:
        """
        Describes an existing snapshot job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_dashboard_snapshot_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_dashboard_snapshot_job)
        """

    def describe_dashboard_snapshot_job_result(
        self, **kwargs: Unpack[DescribeDashboardSnapshotJobResultRequestRequestTypeDef]
    ) -> DescribeDashboardSnapshotJobResultResponseTypeDef:
        """
        Describes the result of an existing snapshot job that has finished running.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_dashboard_snapshot_job_result)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_dashboard_snapshot_job_result)
        """

    def describe_data_set(
        self, **kwargs: Unpack[DescribeDataSetRequestRequestTypeDef]
    ) -> DescribeDataSetResponseTypeDef:
        """
        Describes a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_data_set)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_data_set)
        """

    def describe_data_set_permissions(
        self, **kwargs: Unpack[DescribeDataSetPermissionsRequestRequestTypeDef]
    ) -> DescribeDataSetPermissionsResponseTypeDef:
        """
        Describes the permissions on a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_data_set_permissions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_data_set_permissions)
        """

    def describe_data_set_refresh_properties(
        self, **kwargs: Unpack[DescribeDataSetRefreshPropertiesRequestRequestTypeDef]
    ) -> DescribeDataSetRefreshPropertiesResponseTypeDef:
        """
        Describes the refresh properties of a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_data_set_refresh_properties)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_data_set_refresh_properties)
        """

    def describe_data_source(
        self, **kwargs: Unpack[DescribeDataSourceRequestRequestTypeDef]
    ) -> DescribeDataSourceResponseTypeDef:
        """
        Describes a data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_data_source)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_data_source)
        """

    def describe_data_source_permissions(
        self, **kwargs: Unpack[DescribeDataSourcePermissionsRequestRequestTypeDef]
    ) -> DescribeDataSourcePermissionsResponseTypeDef:
        """
        Describes the resource permissions for a data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_data_source_permissions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_data_source_permissions)
        """

    def describe_folder(
        self, **kwargs: Unpack[DescribeFolderRequestRequestTypeDef]
    ) -> DescribeFolderResponseTypeDef:
        """
        Describes a folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_folder)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_folder)
        """

    def describe_folder_permissions(
        self, **kwargs: Unpack[DescribeFolderPermissionsRequestRequestTypeDef]
    ) -> DescribeFolderPermissionsResponseTypeDef:
        """
        Describes permissions for a folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_folder_permissions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_folder_permissions)
        """

    def describe_folder_resolved_permissions(
        self, **kwargs: Unpack[DescribeFolderResolvedPermissionsRequestRequestTypeDef]
    ) -> DescribeFolderResolvedPermissionsResponseTypeDef:
        """
        Describes the folder resolved permissions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_folder_resolved_permissions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_folder_resolved_permissions)
        """

    def describe_group(
        self, **kwargs: Unpack[DescribeGroupRequestRequestTypeDef]
    ) -> DescribeGroupResponseTypeDef:
        """
        Returns an Amazon QuickSight group's description and Amazon Resource Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_group)
        """

    def describe_group_membership(
        self, **kwargs: Unpack[DescribeGroupMembershipRequestRequestTypeDef]
    ) -> DescribeGroupMembershipResponseTypeDef:
        """
        Use the `DescribeGroupMembership` operation to determine if a user is a member
        of the specified
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_group_membership)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_group_membership)
        """

    def describe_iam_policy_assignment(
        self, **kwargs: Unpack[DescribeIAMPolicyAssignmentRequestRequestTypeDef]
    ) -> DescribeIAMPolicyAssignmentResponseTypeDef:
        """
        Describes an existing IAM policy assignment, as specified by the assignment
        name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_iam_policy_assignment)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_iam_policy_assignment)
        """

    def describe_ingestion(
        self, **kwargs: Unpack[DescribeIngestionRequestRequestTypeDef]
    ) -> DescribeIngestionResponseTypeDef:
        """
        Describes a SPICE ingestion.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_ingestion)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_ingestion)
        """

    def describe_ip_restriction(
        self, **kwargs: Unpack[DescribeIpRestrictionRequestRequestTypeDef]
    ) -> DescribeIpRestrictionResponseTypeDef:
        """
        Provides a summary and status of IP rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_ip_restriction)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_ip_restriction)
        """

    def describe_key_registration(
        self, **kwargs: Unpack[DescribeKeyRegistrationRequestRequestTypeDef]
    ) -> DescribeKeyRegistrationResponseTypeDef:
        """
        Describes all customer managed key registrations in a Amazon QuickSight account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_key_registration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_key_registration)
        """

    def describe_namespace(
        self, **kwargs: Unpack[DescribeNamespaceRequestRequestTypeDef]
    ) -> DescribeNamespaceResponseTypeDef:
        """
        Describes the current namespace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_namespace)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_namespace)
        """

    def describe_q_personalization_configuration(
        self, **kwargs: Unpack[DescribeQPersonalizationConfigurationRequestRequestTypeDef]
    ) -> DescribeQPersonalizationConfigurationResponseTypeDef:
        """
        Describes a personalization configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_q_personalization_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_q_personalization_configuration)
        """

    def describe_refresh_schedule(
        self, **kwargs: Unpack[DescribeRefreshScheduleRequestRequestTypeDef]
    ) -> DescribeRefreshScheduleResponseTypeDef:
        """
        Provides a summary of a refresh schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_refresh_schedule)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_refresh_schedule)
        """

    def describe_role_custom_permission(
        self, **kwargs: Unpack[DescribeRoleCustomPermissionRequestRequestTypeDef]
    ) -> DescribeRoleCustomPermissionResponseTypeDef:
        """
        Describes all custom permissions that are mapped to a role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_role_custom_permission)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_role_custom_permission)
        """

    def describe_template(
        self, **kwargs: Unpack[DescribeTemplateRequestRequestTypeDef]
    ) -> DescribeTemplateResponseTypeDef:
        """
        Describes a template's metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_template)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_template)
        """

    def describe_template_alias(
        self, **kwargs: Unpack[DescribeTemplateAliasRequestRequestTypeDef]
    ) -> DescribeTemplateAliasResponseTypeDef:
        """
        Describes the template alias for a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_template_alias)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_template_alias)
        """

    def describe_template_definition(
        self, **kwargs: Unpack[DescribeTemplateDefinitionRequestRequestTypeDef]
    ) -> DescribeTemplateDefinitionResponseTypeDef:
        """
        Provides a detailed description of the definition of a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_template_definition)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_template_definition)
        """

    def describe_template_permissions(
        self, **kwargs: Unpack[DescribeTemplatePermissionsRequestRequestTypeDef]
    ) -> DescribeTemplatePermissionsResponseTypeDef:
        """
        Describes read and write permissions on a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_template_permissions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_template_permissions)
        """

    def describe_theme(
        self, **kwargs: Unpack[DescribeThemeRequestRequestTypeDef]
    ) -> DescribeThemeResponseTypeDef:
        """
        Describes a theme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_theme)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_theme)
        """

    def describe_theme_alias(
        self, **kwargs: Unpack[DescribeThemeAliasRequestRequestTypeDef]
    ) -> DescribeThemeAliasResponseTypeDef:
        """
        Describes the alias for a theme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_theme_alias)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_theme_alias)
        """

    def describe_theme_permissions(
        self, **kwargs: Unpack[DescribeThemePermissionsRequestRequestTypeDef]
    ) -> DescribeThemePermissionsResponseTypeDef:
        """
        Describes the read and write permissions for a theme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_theme_permissions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_theme_permissions)
        """

    def describe_topic(
        self, **kwargs: Unpack[DescribeTopicRequestRequestTypeDef]
    ) -> DescribeTopicResponseTypeDef:
        """
        Describes a topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_topic)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_topic)
        """

    def describe_topic_permissions(
        self, **kwargs: Unpack[DescribeTopicPermissionsRequestRequestTypeDef]
    ) -> DescribeTopicPermissionsResponseTypeDef:
        """
        Describes the permissions of a topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_topic_permissions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_topic_permissions)
        """

    def describe_topic_refresh(
        self, **kwargs: Unpack[DescribeTopicRefreshRequestRequestTypeDef]
    ) -> DescribeTopicRefreshResponseTypeDef:
        """
        Describes the status of a topic refresh.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_topic_refresh)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_topic_refresh)
        """

    def describe_topic_refresh_schedule(
        self, **kwargs: Unpack[DescribeTopicRefreshScheduleRequestRequestTypeDef]
    ) -> DescribeTopicRefreshScheduleResponseTypeDef:
        """
        Deletes a topic refresh schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_topic_refresh_schedule)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_topic_refresh_schedule)
        """

    def describe_user(
        self, **kwargs: Unpack[DescribeUserRequestRequestTypeDef]
    ) -> DescribeUserResponseTypeDef:
        """
        Returns information about a user, given the user name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_user)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_user)
        """

    def describe_vpc_connection(
        self, **kwargs: Unpack[DescribeVPCConnectionRequestRequestTypeDef]
    ) -> DescribeVPCConnectionResponseTypeDef:
        """
        Describes a VPC connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.describe_vpc_connection)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#describe_vpc_connection)
        """

    def generate_embed_url_for_anonymous_user(
        self, **kwargs: Unpack[GenerateEmbedUrlForAnonymousUserRequestRequestTypeDef]
    ) -> GenerateEmbedUrlForAnonymousUserResponseTypeDef:
        """
        Generates an embed URL that you can use to embed an Amazon QuickSight dashboard
        or visual in your website, without having to register any reader
        users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.generate_embed_url_for_anonymous_user)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#generate_embed_url_for_anonymous_user)
        """

    def generate_embed_url_for_registered_user(
        self, **kwargs: Unpack[GenerateEmbedUrlForRegisteredUserRequestRequestTypeDef]
    ) -> GenerateEmbedUrlForRegisteredUserResponseTypeDef:
        """
        Generates an embed URL that you can use to embed an Amazon QuickSight
        experience in your
        website.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.generate_embed_url_for_registered_user)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#generate_embed_url_for_registered_user)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#generate_presigned_url)
        """

    def get_dashboard_embed_url(
        self, **kwargs: Unpack[GetDashboardEmbedUrlRequestRequestTypeDef]
    ) -> GetDashboardEmbedUrlResponseTypeDef:
        """
        Generates a temporary session URL and authorization code(bearer token) that you
        can use to embed an Amazon QuickSight read-only dashboard in your website or
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_dashboard_embed_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_dashboard_embed_url)
        """

    def get_session_embed_url(
        self, **kwargs: Unpack[GetSessionEmbedUrlRequestRequestTypeDef]
    ) -> GetSessionEmbedUrlResponseTypeDef:
        """
        Generates a session URL and authorization code that you can use to embed the
        Amazon Amazon QuickSight console in your web server
        code.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_session_embed_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_session_embed_url)
        """

    def list_analyses(
        self, **kwargs: Unpack[ListAnalysesRequestRequestTypeDef]
    ) -> ListAnalysesResponseTypeDef:
        """
        Lists Amazon QuickSight analyses that exist in the specified Amazon Web
        Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_analyses)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#list_analyses)
        """

    def list_asset_bundle_export_jobs(
        self, **kwargs: Unpack[ListAssetBundleExportJobsRequestRequestTypeDef]
    ) -> ListAssetBundleExportJobsResponseTypeDef:
        """
        Lists all asset bundle export jobs that have been taken place in the last 14
        days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_asset_bundle_export_jobs)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#list_asset_bundle_export_jobs)
        """

    def list_asset_bundle_import_jobs(
        self, **kwargs: Unpack[ListAssetBundleImportJobsRequestRequestTypeDef]
    ) -> ListAssetBundleImportJobsResponseTypeDef:
        """
        Lists all asset bundle import jobs that have taken place in the last 14 days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_asset_bundle_import_jobs)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#list_asset_bundle_import_jobs)
        """

    def list_dashboard_versions(
        self, **kwargs: Unpack[ListDashboardVersionsRequestRequestTypeDef]
    ) -> ListDashboardVersionsResponseTypeDef:
        """
        Lists all the versions of the dashboards in the Amazon QuickSight subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_dashboard_versions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#list_dashboard_versions)
        """

    def list_dashboards(
        self, **kwargs: Unpack[ListDashboardsRequestRequestTypeDef]
    ) -> ListDashboardsResponseTypeDef:
        """
        Lists dashboards in an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_dashboards)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#list_dashboards)
        """

    def list_data_sets(
        self, **kwargs: Unpack[ListDataSetsRequestRequestTypeDef]
    ) -> ListDataSetsResponseTypeDef:
        """
        Lists all of the datasets belonging to the current Amazon Web Services account
        in an Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_data_sets)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#list_data_sets)
        """

    def list_data_sources(
        self, **kwargs: Unpack[ListDataSourcesRequestRequestTypeDef]
    ) -> ListDataSourcesResponseTypeDef:
        """
        Lists data sources in current Amazon Web Services Region that belong to this
        Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_data_sources)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#list_data_sources)
        """

    def list_folder_members(
        self, **kwargs: Unpack[ListFolderMembersRequestRequestTypeDef]
    ) -> ListFolderMembersResponseTypeDef:
        """
        List all assets ( `DASHBOARD`, `ANALYSIS`, and `DATASET`) in a folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_folder_members)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#list_folder_members)
        """

    def list_folders(
        self, **kwargs: Unpack[ListFoldersRequestRequestTypeDef]
    ) -> ListFoldersResponseTypeDef:
        """
        Lists all folders in an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_folders)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#list_folders)
        """

    def list_folders_for_resource(
        self, **kwargs: Unpack[ListFoldersForResourceRequestRequestTypeDef]
    ) -> ListFoldersForResourceResponseTypeDef:
        """
        List all folders that a resource is a member of.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_folders_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#list_folders_for_resource)
        """

    def list_group_memberships(
        self, **kwargs: Unpack[ListGroupMembershipsRequestRequestTypeDef]
    ) -> ListGroupMembershipsResponseTypeDef:
        """
        Lists member users in a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_group_memberships)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#list_group_memberships)
        """

    def list_groups(
        self, **kwargs: Unpack[ListGroupsRequestRequestTypeDef]
    ) -> ListGroupsResponseTypeDef:
        """
        Lists all user groups in Amazon QuickSight.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_groups)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#list_groups)
        """

    def list_iam_policy_assignments(
        self, **kwargs: Unpack[ListIAMPolicyAssignmentsRequestRequestTypeDef]
    ) -> ListIAMPolicyAssignmentsResponseTypeDef:
        """
        Lists the IAM policy assignments in the current Amazon QuickSight account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_iam_policy_assignments)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#list_iam_policy_assignments)
        """

    def list_iam_policy_assignments_for_user(
        self, **kwargs: Unpack[ListIAMPolicyAssignmentsForUserRequestRequestTypeDef]
    ) -> ListIAMPolicyAssignmentsForUserResponseTypeDef:
        """
        Lists all of the IAM policy assignments, including the Amazon Resource Names
        (ARNs), for the IAM policies assigned to the specified user and group, or
        groups that the user belongs
        to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_iam_policy_assignments_for_user)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#list_iam_policy_assignments_for_user)
        """

    def list_identity_propagation_configs(
        self, **kwargs: Unpack[ListIdentityPropagationConfigsRequestRequestTypeDef]
    ) -> ListIdentityPropagationConfigsResponseTypeDef:
        """
        Lists all services and authorized targets that the Amazon QuickSight IAM
        Identity Center application can
        access.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_identity_propagation_configs)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#list_identity_propagation_configs)
        """

    def list_ingestions(
        self, **kwargs: Unpack[ListIngestionsRequestRequestTypeDef]
    ) -> ListIngestionsResponseTypeDef:
        """
        Lists the history of SPICE ingestions for a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_ingestions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#list_ingestions)
        """

    def list_namespaces(
        self, **kwargs: Unpack[ListNamespacesRequestRequestTypeDef]
    ) -> ListNamespacesResponseTypeDef:
        """
        Lists the namespaces for the specified Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_namespaces)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#list_namespaces)
        """

    def list_refresh_schedules(
        self, **kwargs: Unpack[ListRefreshSchedulesRequestRequestTypeDef]
    ) -> ListRefreshSchedulesResponseTypeDef:
        """
        Lists the refresh schedules of a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_refresh_schedules)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#list_refresh_schedules)
        """

    def list_role_memberships(
        self, **kwargs: Unpack[ListRoleMembershipsRequestRequestTypeDef]
    ) -> ListRoleMembershipsResponseTypeDef:
        """
        Lists all groups that are associated with a role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_role_memberships)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#list_role_memberships)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags assigned to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_tags_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#list_tags_for_resource)
        """

    def list_template_aliases(
        self, **kwargs: Unpack[ListTemplateAliasesRequestRequestTypeDef]
    ) -> ListTemplateAliasesResponseTypeDef:
        """
        Lists all the aliases of a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_template_aliases)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#list_template_aliases)
        """

    def list_template_versions(
        self, **kwargs: Unpack[ListTemplateVersionsRequestRequestTypeDef]
    ) -> ListTemplateVersionsResponseTypeDef:
        """
        Lists all the versions of the templates in the current Amazon QuickSight
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_template_versions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#list_template_versions)
        """

    def list_templates(
        self, **kwargs: Unpack[ListTemplatesRequestRequestTypeDef]
    ) -> ListTemplatesResponseTypeDef:
        """
        Lists all the templates in the current Amazon QuickSight account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_templates)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#list_templates)
        """

    def list_theme_aliases(
        self, **kwargs: Unpack[ListThemeAliasesRequestRequestTypeDef]
    ) -> ListThemeAliasesResponseTypeDef:
        """
        Lists all the aliases of a theme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_theme_aliases)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#list_theme_aliases)
        """

    def list_theme_versions(
        self, **kwargs: Unpack[ListThemeVersionsRequestRequestTypeDef]
    ) -> ListThemeVersionsResponseTypeDef:
        """
        Lists all the versions of the themes in the current Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_theme_versions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#list_theme_versions)
        """

    def list_themes(
        self, **kwargs: Unpack[ListThemesRequestRequestTypeDef]
    ) -> ListThemesResponseTypeDef:
        """
        Lists all the themes in the current Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_themes)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#list_themes)
        """

    def list_topic_refresh_schedules(
        self, **kwargs: Unpack[ListTopicRefreshSchedulesRequestRequestTypeDef]
    ) -> ListTopicRefreshSchedulesResponseTypeDef:
        """
        Lists all of the refresh schedules for a topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_topic_refresh_schedules)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#list_topic_refresh_schedules)
        """

    def list_topic_reviewed_answers(
        self, **kwargs: Unpack[ListTopicReviewedAnswersRequestRequestTypeDef]
    ) -> ListTopicReviewedAnswersResponseTypeDef:
        """
        Lists all reviewed answers for a Q Topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_topic_reviewed_answers)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#list_topic_reviewed_answers)
        """

    def list_topics(
        self, **kwargs: Unpack[ListTopicsRequestRequestTypeDef]
    ) -> ListTopicsResponseTypeDef:
        """
        Lists all of the topics within an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_topics)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#list_topics)
        """

    def list_user_groups(
        self, **kwargs: Unpack[ListUserGroupsRequestRequestTypeDef]
    ) -> ListUserGroupsResponseTypeDef:
        """
        Lists the Amazon QuickSight groups that an Amazon QuickSight user is a member
        of.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_user_groups)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#list_user_groups)
        """

    def list_users(
        self, **kwargs: Unpack[ListUsersRequestRequestTypeDef]
    ) -> ListUsersResponseTypeDef:
        """
        Returns a list of all of the Amazon QuickSight users belonging to this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_users)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#list_users)
        """

    def list_vpc_connections(
        self, **kwargs: Unpack[ListVPCConnectionsRequestRequestTypeDef]
    ) -> ListVPCConnectionsResponseTypeDef:
        """
        Lists all of the VPC connections in the current set Amazon Web Services Region
        of an Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.list_vpc_connections)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#list_vpc_connections)
        """

    def put_data_set_refresh_properties(
        self, **kwargs: Unpack[PutDataSetRefreshPropertiesRequestRequestTypeDef]
    ) -> PutDataSetRefreshPropertiesResponseTypeDef:
        """
        Creates or updates the dataset refresh properties for the dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.put_data_set_refresh_properties)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#put_data_set_refresh_properties)
        """

    def register_user(
        self, **kwargs: Unpack[RegisterUserRequestRequestTypeDef]
    ) -> RegisterUserResponseTypeDef:
        """
        Creates an Amazon QuickSight user whose identity is associated with the
        Identity and Access Management (IAM) identity or role specified in the
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.register_user)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#register_user)
        """

    def restore_analysis(
        self, **kwargs: Unpack[RestoreAnalysisRequestRequestTypeDef]
    ) -> RestoreAnalysisResponseTypeDef:
        """
        Restores an analysis.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.restore_analysis)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#restore_analysis)
        """

    def search_analyses(
        self, **kwargs: Unpack[SearchAnalysesRequestRequestTypeDef]
    ) -> SearchAnalysesResponseTypeDef:
        """
        Searches for analyses that belong to the user specified in the filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.search_analyses)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#search_analyses)
        """

    def search_dashboards(
        self, **kwargs: Unpack[SearchDashboardsRequestRequestTypeDef]
    ) -> SearchDashboardsResponseTypeDef:
        """
        Searches for dashboards that belong to a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.search_dashboards)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#search_dashboards)
        """

    def search_data_sets(
        self, **kwargs: Unpack[SearchDataSetsRequestRequestTypeDef]
    ) -> SearchDataSetsResponseTypeDef:
        """
        Use the `SearchDataSets` operation to search for datasets that belong to an
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.search_data_sets)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#search_data_sets)
        """

    def search_data_sources(
        self, **kwargs: Unpack[SearchDataSourcesRequestRequestTypeDef]
    ) -> SearchDataSourcesResponseTypeDef:
        """
        Use the `SearchDataSources` operation to search for data sources that belong to
        an
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.search_data_sources)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#search_data_sources)
        """

    def search_folders(
        self, **kwargs: Unpack[SearchFoldersRequestRequestTypeDef]
    ) -> SearchFoldersResponseTypeDef:
        """
        Searches the subfolders in a folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.search_folders)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#search_folders)
        """

    def search_groups(
        self, **kwargs: Unpack[SearchGroupsRequestRequestTypeDef]
    ) -> SearchGroupsResponseTypeDef:
        """
        Use the `SearchGroups` operation to search groups in a specified Amazon
        QuickSight namespace using the supplied
        filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.search_groups)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#search_groups)
        """

    def start_asset_bundle_export_job(
        self, **kwargs: Unpack[StartAssetBundleExportJobRequestRequestTypeDef]
    ) -> StartAssetBundleExportJobResponseTypeDef:
        """
        Starts an Asset Bundle export job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.start_asset_bundle_export_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#start_asset_bundle_export_job)
        """

    def start_asset_bundle_import_job(
        self, **kwargs: Unpack[StartAssetBundleImportJobRequestRequestTypeDef]
    ) -> StartAssetBundleImportJobResponseTypeDef:
        """
        Starts an Asset Bundle import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.start_asset_bundle_import_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#start_asset_bundle_import_job)
        """

    def start_dashboard_snapshot_job(
        self, **kwargs: Unpack[StartDashboardSnapshotJobRequestRequestTypeDef]
    ) -> StartDashboardSnapshotJobResponseTypeDef:
        """
        Starts an asynchronous job that generates a snapshot of a dashboard's output.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.start_dashboard_snapshot_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#start_dashboard_snapshot_job)
        """

    def start_dashboard_snapshot_job_schedule(
        self, **kwargs: Unpack[StartDashboardSnapshotJobScheduleRequestRequestTypeDef]
    ) -> StartDashboardSnapshotJobScheduleResponseTypeDef:
        """
        Starts an asynchronous job that runs an existing dashboard schedule and sends
        the dashboard snapshot through
        email.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.start_dashboard_snapshot_job_schedule)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#start_dashboard_snapshot_job_schedule)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]
    ) -> TagResourceResponseTypeDef:
        """
        Assigns one or more tags (key-value pairs) to the specified Amazon QuickSight
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> UntagResourceResponseTypeDef:
        """
        Removes a tag or tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#untag_resource)
        """

    def update_account_customization(
        self, **kwargs: Unpack[UpdateAccountCustomizationRequestRequestTypeDef]
    ) -> UpdateAccountCustomizationResponseTypeDef:
        """
        Updates Amazon QuickSight customizations for the current Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_account_customization)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_account_customization)
        """

    def update_account_settings(
        self, **kwargs: Unpack[UpdateAccountSettingsRequestRequestTypeDef]
    ) -> UpdateAccountSettingsResponseTypeDef:
        """
        Updates the Amazon QuickSight settings in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_account_settings)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_account_settings)
        """

    def update_analysis(
        self, **kwargs: Unpack[UpdateAnalysisRequestRequestTypeDef]
    ) -> UpdateAnalysisResponseTypeDef:
        """
        Updates an analysis in Amazon QuickSight See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/UpdateAnalysis).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_analysis)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_analysis)
        """

    def update_analysis_permissions(
        self, **kwargs: Unpack[UpdateAnalysisPermissionsRequestRequestTypeDef]
    ) -> UpdateAnalysisPermissionsResponseTypeDef:
        """
        Updates the read and write permissions for an analysis.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_analysis_permissions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_analysis_permissions)
        """

    def update_dashboard(
        self, **kwargs: Unpack[UpdateDashboardRequestRequestTypeDef]
    ) -> UpdateDashboardResponseTypeDef:
        """
        Updates a dashboard in an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_dashboard)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_dashboard)
        """

    def update_dashboard_links(
        self, **kwargs: Unpack[UpdateDashboardLinksRequestRequestTypeDef]
    ) -> UpdateDashboardLinksResponseTypeDef:
        """
        Updates the linked analyses on a dashboard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_dashboard_links)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_dashboard_links)
        """

    def update_dashboard_permissions(
        self, **kwargs: Unpack[UpdateDashboardPermissionsRequestRequestTypeDef]
    ) -> UpdateDashboardPermissionsResponseTypeDef:
        """
        Updates read and write permissions on a dashboard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_dashboard_permissions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_dashboard_permissions)
        """

    def update_dashboard_published_version(
        self, **kwargs: Unpack[UpdateDashboardPublishedVersionRequestRequestTypeDef]
    ) -> UpdateDashboardPublishedVersionResponseTypeDef:
        """
        Updates the published version of a dashboard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_dashboard_published_version)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_dashboard_published_version)
        """

    def update_data_set(
        self, **kwargs: Unpack[UpdateDataSetRequestRequestTypeDef]
    ) -> UpdateDataSetResponseTypeDef:
        """
        Updates a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_data_set)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_data_set)
        """

    def update_data_set_permissions(
        self, **kwargs: Unpack[UpdateDataSetPermissionsRequestRequestTypeDef]
    ) -> UpdateDataSetPermissionsResponseTypeDef:
        """
        Updates the permissions on a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_data_set_permissions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_data_set_permissions)
        """

    def update_data_source(
        self, **kwargs: Unpack[UpdateDataSourceRequestRequestTypeDef]
    ) -> UpdateDataSourceResponseTypeDef:
        """
        Updates a data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_data_source)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_data_source)
        """

    def update_data_source_permissions(
        self, **kwargs: Unpack[UpdateDataSourcePermissionsRequestRequestTypeDef]
    ) -> UpdateDataSourcePermissionsResponseTypeDef:
        """
        Updates the permissions to a data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_data_source_permissions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_data_source_permissions)
        """

    def update_folder(
        self, **kwargs: Unpack[UpdateFolderRequestRequestTypeDef]
    ) -> UpdateFolderResponseTypeDef:
        """
        Updates the name of a folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_folder)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_folder)
        """

    def update_folder_permissions(
        self, **kwargs: Unpack[UpdateFolderPermissionsRequestRequestTypeDef]
    ) -> UpdateFolderPermissionsResponseTypeDef:
        """
        Updates permissions of a folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_folder_permissions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_folder_permissions)
        """

    def update_group(
        self, **kwargs: Unpack[UpdateGroupRequestRequestTypeDef]
    ) -> UpdateGroupResponseTypeDef:
        """
        Changes a group description.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_group)
        """

    def update_iam_policy_assignment(
        self, **kwargs: Unpack[UpdateIAMPolicyAssignmentRequestRequestTypeDef]
    ) -> UpdateIAMPolicyAssignmentResponseTypeDef:
        """
        Updates an existing IAM policy assignment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_iam_policy_assignment)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_iam_policy_assignment)
        """

    def update_identity_propagation_config(
        self, **kwargs: Unpack[UpdateIdentityPropagationConfigRequestRequestTypeDef]
    ) -> UpdateIdentityPropagationConfigResponseTypeDef:
        """
        Adds or updates services and authorized targets to configure what the Amazon
        QuickSight IAM Identity Center application can
        access.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_identity_propagation_config)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_identity_propagation_config)
        """

    def update_ip_restriction(
        self, **kwargs: Unpack[UpdateIpRestrictionRequestRequestTypeDef]
    ) -> UpdateIpRestrictionResponseTypeDef:
        """
        Updates the content and status of IP rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_ip_restriction)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_ip_restriction)
        """

    def update_key_registration(
        self, **kwargs: Unpack[UpdateKeyRegistrationRequestRequestTypeDef]
    ) -> UpdateKeyRegistrationResponseTypeDef:
        """
        Updates a customer managed key in a Amazon QuickSight account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_key_registration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_key_registration)
        """

    def update_public_sharing_settings(
        self, **kwargs: Unpack[UpdatePublicSharingSettingsRequestRequestTypeDef]
    ) -> UpdatePublicSharingSettingsResponseTypeDef:
        """
        Use the `UpdatePublicSharingSettings` operation to turn on or turn off the
        public sharing settings of an Amazon QuickSight
        dashboard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_public_sharing_settings)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_public_sharing_settings)
        """

    def update_q_personalization_configuration(
        self, **kwargs: Unpack[UpdateQPersonalizationConfigurationRequestRequestTypeDef]
    ) -> UpdateQPersonalizationConfigurationResponseTypeDef:
        """
        Updates a personalization configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_q_personalization_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_q_personalization_configuration)
        """

    def update_refresh_schedule(
        self, **kwargs: Unpack[UpdateRefreshScheduleRequestRequestTypeDef]
    ) -> UpdateRefreshScheduleResponseTypeDef:
        """
        Updates a refresh schedule for a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_refresh_schedule)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_refresh_schedule)
        """

    def update_role_custom_permission(
        self, **kwargs: Unpack[UpdateRoleCustomPermissionRequestRequestTypeDef]
    ) -> UpdateRoleCustomPermissionResponseTypeDef:
        """
        Updates the custom permissions that are associated with a role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_role_custom_permission)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_role_custom_permission)
        """

    def update_spice_capacity_configuration(
        self, **kwargs: Unpack[UpdateSPICECapacityConfigurationRequestRequestTypeDef]
    ) -> UpdateSPICECapacityConfigurationResponseTypeDef:
        """
        Updates the SPICE capacity configuration for a Amazon QuickSight account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_spice_capacity_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_spice_capacity_configuration)
        """

    def update_template(
        self, **kwargs: Unpack[UpdateTemplateRequestRequestTypeDef]
    ) -> UpdateTemplateResponseTypeDef:
        """
        Updates a template from an existing Amazon QuickSight analysis or another
        template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_template)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_template)
        """

    def update_template_alias(
        self, **kwargs: Unpack[UpdateTemplateAliasRequestRequestTypeDef]
    ) -> UpdateTemplateAliasResponseTypeDef:
        """
        Updates the template alias of a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_template_alias)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_template_alias)
        """

    def update_template_permissions(
        self, **kwargs: Unpack[UpdateTemplatePermissionsRequestRequestTypeDef]
    ) -> UpdateTemplatePermissionsResponseTypeDef:
        """
        Updates the resource permissions for a template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_template_permissions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_template_permissions)
        """

    def update_theme(
        self, **kwargs: Unpack[UpdateThemeRequestRequestTypeDef]
    ) -> UpdateThemeResponseTypeDef:
        """
        Updates a theme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_theme)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_theme)
        """

    def update_theme_alias(
        self, **kwargs: Unpack[UpdateThemeAliasRequestRequestTypeDef]
    ) -> UpdateThemeAliasResponseTypeDef:
        """
        Updates an alias of a theme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_theme_alias)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_theme_alias)
        """

    def update_theme_permissions(
        self, **kwargs: Unpack[UpdateThemePermissionsRequestRequestTypeDef]
    ) -> UpdateThemePermissionsResponseTypeDef:
        """
        Updates the resource permissions for a theme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_theme_permissions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_theme_permissions)
        """

    def update_topic(
        self, **kwargs: Unpack[UpdateTopicRequestRequestTypeDef]
    ) -> UpdateTopicResponseTypeDef:
        """
        Updates a topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_topic)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_topic)
        """

    def update_topic_permissions(
        self, **kwargs: Unpack[UpdateTopicPermissionsRequestRequestTypeDef]
    ) -> UpdateTopicPermissionsResponseTypeDef:
        """
        Updates the permissions of a topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_topic_permissions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_topic_permissions)
        """

    def update_topic_refresh_schedule(
        self, **kwargs: Unpack[UpdateTopicRefreshScheduleRequestRequestTypeDef]
    ) -> UpdateTopicRefreshScheduleResponseTypeDef:
        """
        Updates a topic refresh schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_topic_refresh_schedule)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_topic_refresh_schedule)
        """

    def update_user(
        self, **kwargs: Unpack[UpdateUserRequestRequestTypeDef]
    ) -> UpdateUserResponseTypeDef:
        """
        Updates an Amazon QuickSight user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_user)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_user)
        """

    def update_vpc_connection(
        self, **kwargs: Unpack[UpdateVPCConnectionRequestRequestTypeDef]
    ) -> UpdateVPCConnectionResponseTypeDef:
        """
        Updates a VPC connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.update_vpc_connection)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#update_vpc_connection)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_folder_permissions"]
    ) -> DescribeFolderPermissionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_folder_resolved_permissions"]
    ) -> DescribeFolderResolvedPermissionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_analyses"]) -> ListAnalysesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_asset_bundle_export_jobs"]
    ) -> ListAssetBundleExportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_asset_bundle_import_jobs"]
    ) -> ListAssetBundleImportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dashboard_versions"]
    ) -> ListDashboardVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_dashboards"]) -> ListDashboardsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_data_sets"]) -> ListDataSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_sources"]
    ) -> ListDataSourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_folder_members"]
    ) -> ListFolderMembersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_folders"]) -> ListFoldersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_folders_for_resource"]
    ) -> ListFoldersForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_group_memberships"]
    ) -> ListGroupMembershipsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_groups"]) -> ListGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_iam_policy_assignments"]
    ) -> ListIAMPolicyAssignmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_iam_policy_assignments_for_user"]
    ) -> ListIAMPolicyAssignmentsForUserPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_ingestions"]) -> ListIngestionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_namespaces"]) -> ListNamespacesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_role_memberships"]
    ) -> ListRoleMembershipsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_template_aliases"]
    ) -> ListTemplateAliasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_template_versions"]
    ) -> ListTemplateVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_templates"]) -> ListTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_theme_versions"]
    ) -> ListThemeVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_themes"]) -> ListThemesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_user_groups"]) -> ListUserGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_users"]) -> ListUsersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_analyses"]) -> SearchAnalysesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_dashboards"]
    ) -> SearchDashboardsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_data_sets"]) -> SearchDataSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_data_sources"]
    ) -> SearchDataSourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_folders"]) -> SearchFoldersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_groups"]) -> SearchGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/quicksight.html#QuickSight.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/client/#get_paginator)
        """
