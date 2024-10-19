"""
Type annotations for datazone service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/type_defs/)

Usage::

    ```python
    from mypy_boto3_datazone.type_defs import AcceptChoiceTypeDef

    data: AcceptChoiceTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    AcceptRuleBehaviorType,
    AuthTypeType,
    ChangeActionType,
    ConfigurableActionTypeAuthorizationType,
    DataAssetActivityStatusType,
    DataProductStatusType,
    DataSourceErrorTypeType,
    DataSourceRunStatusType,
    DataSourceRunTypeType,
    DataSourceStatusType,
    DeploymentStatusType,
    DeploymentTypeType,
    DomainStatusType,
    EdgeDirectionType,
    EnableSettingType,
    EntityTypeType,
    EnvironmentStatusType,
    FilterExpressionTypeType,
    FilterStatusType,
    FormTypeStatusType,
    GlossaryStatusType,
    GlossaryTermStatusType,
    GroupProfileStatusType,
    GroupSearchTypeType,
    InventorySearchScopeType,
    ListingStatusType,
    ManagedPolicyTypeType,
    MetadataGenerationRunStatusType,
    NotificationRoleType,
    NotificationTypeType,
    ProjectDesignationType,
    ProjectStatusType,
    RejectRuleBehaviorType,
    SearchOutputAdditionalAttributeType,
    SelfGrantStatusType,
    SortKeyType,
    SortOrderType,
    SubscriptionGrantOverallStatusType,
    SubscriptionGrantStatusType,
    SubscriptionRequestStatusType,
    SubscriptionStatusType,
    TargetEntityTypeType,
    TaskStatusType,
    TimeSeriesEntityTypeType,
    TimezoneType,
    TypesSearchScopeType,
    UserAssignmentType,
    UserDesignationType,
    UserProfileStatusType,
    UserProfileTypeType,
    UserSearchTypeType,
    UserTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AcceptChoiceTypeDef",
    "AcceptRuleTypeDef",
    "ResponseMetadataTypeDef",
    "AcceptedAssetScopeTypeDef",
    "AwsConsoleLinkParametersTypeDef",
    "AddToProjectMemberPoolPolicyGrantDetailTypeDef",
    "ColumnFilterConfigurationOutputTypeDef",
    "AssetFilterSummaryTypeDef",
    "AssetInDataProductListingItemTypeDef",
    "FormOutputTypeDef",
    "TimeSeriesDataPointSummaryFormOutputTypeDef",
    "AssetListingDetailsTypeDef",
    "DetailedGlossaryTermTypeDef",
    "AssetRevisionTypeDef",
    "AssetScopeTypeDef",
    "AssetTargetNameMapTypeDef",
    "FormEntryOutputTypeDef",
    "AssociateEnvironmentRoleInputRequestTypeDef",
    "BlobTypeDef",
    "BusinessNameGenerationConfigurationTypeDef",
    "CancelMetadataGenerationRunInputRequestTypeDef",
    "CancelSubscriptionInputRequestTypeDef",
    "CloudFormationPropertiesTypeDef",
    "ColumnFilterConfigurationTypeDef",
    "ConfigurableActionParameterTypeDef",
    "FormInputTypeDef",
    "FormEntryInputTypeDef",
    "CreateAssetTypePolicyGrantDetailTypeDef",
    "DataProductItemOutputTypeDef",
    "DataProductItemTypeDef",
    "RecommendationConfigurationTypeDef",
    "ScheduleConfigurationTypeDef",
    "DataSourceErrorMessageTypeDef",
    "SingleSignOnTypeDef",
    "CreateDomainUnitInputRequestTypeDef",
    "CreateDomainUnitPolicyGrantDetailTypeDef",
    "EnvironmentParameterTypeDef",
    "CustomParameterTypeDef",
    "DeploymentPropertiesTypeDef",
    "ResourceTypeDef",
    "CreateEnvironmentProfilePolicyGrantDetailTypeDef",
    "ModelTypeDef",
    "CreateFormTypePolicyGrantDetailTypeDef",
    "CreateGlossaryInputRequestTypeDef",
    "CreateGlossaryPolicyGrantDetailTypeDef",
    "TermRelationsTypeDef",
    "TermRelationsOutputTypeDef",
    "CreateGroupProfileInputRequestTypeDef",
    "CreateListingChangeSetInputRequestTypeDef",
    "CreateProjectInputRequestTypeDef",
    "MemberTypeDef",
    "ProjectDeletionErrorTypeDef",
    "CreateProjectPolicyGrantDetailTypeDef",
    "SubscribedListingInputTypeDef",
    "SubscriptionTargetFormTypeDef",
    "CreateUserProfileInputRequestTypeDef",
    "DataProductListingItemAdditionalAttributesTypeDef",
    "DataProductResultItemTypeDef",
    "DataProductRevisionTypeDef",
    "RunStatisticsForAssetsTypeDef",
    "DeleteAssetFilterInputRequestTypeDef",
    "DeleteAssetInputRequestTypeDef",
    "DeleteAssetTypeInputRequestTypeDef",
    "DeleteDataProductInputRequestTypeDef",
    "DeleteDataSourceInputRequestTypeDef",
    "DeleteDomainInputRequestTypeDef",
    "DeleteDomainUnitInputRequestTypeDef",
    "DeleteEnvironmentActionInputRequestTypeDef",
    "DeleteEnvironmentBlueprintConfigurationInputRequestTypeDef",
    "DeleteEnvironmentInputRequestTypeDef",
    "DeleteEnvironmentProfileInputRequestTypeDef",
    "DeleteFormTypeInputRequestTypeDef",
    "DeleteGlossaryInputRequestTypeDef",
    "DeleteGlossaryTermInputRequestTypeDef",
    "DeleteListingInputRequestTypeDef",
    "DeleteProjectInputRequestTypeDef",
    "DeleteSubscriptionGrantInputRequestTypeDef",
    "DeleteSubscriptionRequestInputRequestTypeDef",
    "DeleteSubscriptionTargetInputRequestTypeDef",
    "DeleteTimeSeriesDataPointsInputRequestTypeDef",
    "EnvironmentErrorTypeDef",
    "DisassociateEnvironmentRoleInputRequestTypeDef",
    "DomainSummaryTypeDef",
    "DomainUnitFilterForProjectTypeDef",
    "DomainUnitGrantFilterOutputTypeDef",
    "DomainUnitGrantFilterTypeDef",
    "DomainUnitGroupPropertiesTypeDef",
    "DomainUnitUserPropertiesTypeDef",
    "DomainUnitSummaryTypeDef",
    "EnvironmentProfileSummaryTypeDef",
    "EnvironmentSummaryTypeDef",
    "EqualToExpressionTypeDef",
    "FailureCauseTypeDef",
    "FilterTypeDef",
    "FilterExpressionTypeDef",
    "ImportTypeDef",
    "GetAssetFilterInputRequestTypeDef",
    "GetAssetInputRequestTypeDef",
    "GetAssetTypeInputRequestTypeDef",
    "GetDataProductInputRequestTypeDef",
    "GetDataSourceInputRequestTypeDef",
    "GetDataSourceRunInputRequestTypeDef",
    "GetDomainInputRequestTypeDef",
    "GetDomainUnitInputRequestTypeDef",
    "GetEnvironmentActionInputRequestTypeDef",
    "GetEnvironmentBlueprintConfigurationInputRequestTypeDef",
    "GetEnvironmentBlueprintInputRequestTypeDef",
    "GetEnvironmentCredentialsInputRequestTypeDef",
    "GetEnvironmentInputRequestTypeDef",
    "GetEnvironmentProfileInputRequestTypeDef",
    "GetFormTypeInputRequestTypeDef",
    "GetGlossaryInputRequestTypeDef",
    "GetGlossaryTermInputRequestTypeDef",
    "GetGroupProfileInputRequestTypeDef",
    "GetIamPortalLoginUrlInputRequestTypeDef",
    "TimestampTypeDef",
    "LineageNodeReferenceTypeDef",
    "GetListingInputRequestTypeDef",
    "GetMetadataGenerationRunInputRequestTypeDef",
    "MetadataGenerationRunTargetTypeDef",
    "GetProjectInputRequestTypeDef",
    "GetSubscriptionGrantInputRequestTypeDef",
    "GetSubscriptionInputRequestTypeDef",
    "GetSubscriptionRequestDetailsInputRequestTypeDef",
    "GetSubscriptionTargetInputRequestTypeDef",
    "GetTimeSeriesDataPointInputRequestTypeDef",
    "TimeSeriesDataPointFormOutputTypeDef",
    "GetUserProfileInputRequestTypeDef",
    "GlossaryItemTypeDef",
    "SelfGrantStatusDetailTypeDef",
    "ListingRevisionInputTypeDef",
    "ListingRevisionTypeDef",
    "GreaterThanExpressionTypeDef",
    "GreaterThanOrEqualToExpressionTypeDef",
    "GroupDetailsTypeDef",
    "GroupPolicyGrantPrincipalTypeDef",
    "GroupProfileSummaryTypeDef",
    "IamUserProfileDetailsTypeDef",
    "InExpressionOutputTypeDef",
    "InExpressionTypeDef",
    "IsNotNullExpressionTypeDef",
    "IsNullExpressionTypeDef",
    "LakeFormationConfigurationOutputTypeDef",
    "LakeFormationConfigurationTypeDef",
    "LessThanExpressionTypeDef",
    "LessThanOrEqualToExpressionTypeDef",
    "LikeExpressionTypeDef",
    "LineageNodeSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "ListAssetFiltersInputRequestTypeDef",
    "ListAssetRevisionsInputRequestTypeDef",
    "ListDataProductRevisionsInputRequestTypeDef",
    "ListDataSourceRunActivitiesInputRequestTypeDef",
    "ListDataSourceRunsInputRequestTypeDef",
    "ListDataSourcesInputRequestTypeDef",
    "ListDomainUnitsForParentInputRequestTypeDef",
    "ListDomainsInputRequestTypeDef",
    "ListEntityOwnersInputRequestTypeDef",
    "ListEnvironmentActionsInputRequestTypeDef",
    "ListEnvironmentBlueprintConfigurationsInputRequestTypeDef",
    "ListEnvironmentBlueprintsInputRequestTypeDef",
    "ListEnvironmentProfilesInputRequestTypeDef",
    "ListEnvironmentsInputRequestTypeDef",
    "ListMetadataGenerationRunsInputRequestTypeDef",
    "ListPolicyGrantsInputRequestTypeDef",
    "ListProjectMembershipsInputRequestTypeDef",
    "ListProjectsInputRequestTypeDef",
    "ListSubscriptionGrantsInputRequestTypeDef",
    "ListSubscriptionRequestsInputRequestTypeDef",
    "ListSubscriptionTargetsInputRequestTypeDef",
    "ListSubscriptionsInputRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "UserDetailsTypeDef",
    "NotEqualToExpressionTypeDef",
    "NotInExpressionOutputTypeDef",
    "NotInExpressionTypeDef",
    "NotLikeExpressionTypeDef",
    "NotificationResourceTypeDef",
    "OverrideDomainUnitOwnersPolicyGrantDetailTypeDef",
    "OverrideProjectOwnersPolicyGrantDetailTypeDef",
    "OwnerGroupPropertiesOutputTypeDef",
    "OwnerGroupPropertiesTypeDef",
    "OwnerUserPropertiesOutputTypeDef",
    "OwnerUserPropertiesTypeDef",
    "UserPolicyGrantPrincipalOutputTypeDef",
    "RedshiftClusterStorageTypeDef",
    "RedshiftCredentialConfigurationTypeDef",
    "RedshiftServerlessStorageTypeDef",
    "RejectChoiceTypeDef",
    "RejectRuleTypeDef",
    "RejectSubscriptionRequestInputRequestTypeDef",
    "RevokeSubscriptionInputRequestTypeDef",
    "SearchGroupProfilesInputRequestTypeDef",
    "SearchInItemTypeDef",
    "SearchSortTypeDef",
    "SearchUserProfilesInputRequestTypeDef",
    "SsoUserProfileDetailsTypeDef",
    "StartDataSourceRunInputRequestTypeDef",
    "SubscribedProjectInputTypeDef",
    "SubscribedProjectTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDomainUnitInputRequestTypeDef",
    "UpdateEnvironmentInputRequestTypeDef",
    "UpdateGlossaryInputRequestTypeDef",
    "UpdateGroupProfileInputRequestTypeDef",
    "UpdateProjectInputRequestTypeDef",
    "UpdateSubscriptionRequestInputRequestTypeDef",
    "UpdateUserProfileInputRequestTypeDef",
    "UserPolicyGrantPrincipalTypeDef",
    "AcceptPredictionsInputRequestTypeDef",
    "AcceptPredictionsOutputTypeDef",
    "CreateFormTypeOutputTypeDef",
    "CreateGlossaryOutputTypeDef",
    "CreateGroupProfileOutputTypeDef",
    "CreateListingChangeSetOutputTypeDef",
    "DeleteDomainOutputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetEnvironmentCredentialsOutputTypeDef",
    "GetGlossaryOutputTypeDef",
    "GetGroupProfileOutputTypeDef",
    "GetIamPortalLoginUrlOutputTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "RejectPredictionsOutputTypeDef",
    "StartMetadataGenerationRunOutputTypeDef",
    "UpdateGlossaryOutputTypeDef",
    "UpdateGroupProfileOutputTypeDef",
    "AcceptSubscriptionRequestInputRequestTypeDef",
    "ActionParametersTypeDef",
    "ListAssetFiltersOutputTypeDef",
    "AssetItemAdditionalAttributesTypeDef",
    "AssetListingItemAdditionalAttributesTypeDef",
    "ListTimeSeriesDataPointsOutputTypeDef",
    "GetAssetOutputTypeDef",
    "AssetListingTypeDef",
    "ListingSummaryItemTypeDef",
    "ListingSummaryTypeDef",
    "SubscribedProductListingTypeDef",
    "ListAssetRevisionsOutputTypeDef",
    "SubscribedAssetListingTypeDef",
    "AssetTypeItemTypeDef",
    "CreateAssetTypeOutputTypeDef",
    "GetAssetTypeOutputTypeDef",
    "LineageNodeTypeItemTypeDef",
    "PostLineageEventInputRequestTypeDef",
    "PredictionConfigurationTypeDef",
    "ProvisioningPropertiesTypeDef",
    "ColumnFilterConfigurationUnionTypeDef",
    "ConfigurableEnvironmentActionTypeDef",
    "CreateAssetTypeInputRequestTypeDef",
    "CreateDataProductOutputTypeDef",
    "CreateDataProductRevisionOutputTypeDef",
    "GetDataProductOutputTypeDef",
    "CreateDataProductRevisionInputRequestTypeDef",
    "DataProductItemUnionTypeDef",
    "DataSourceRunActivityTypeDef",
    "DataSourceSummaryTypeDef",
    "CreateDomainInputRequestTypeDef",
    "CreateDomainOutputTypeDef",
    "GetDomainOutputTypeDef",
    "UpdateDomainInputRequestTypeDef",
    "UpdateDomainOutputTypeDef",
    "CreateEnvironmentInputRequestTypeDef",
    "CreateEnvironmentProfileInputRequestTypeDef",
    "UpdateEnvironmentProfileInputRequestTypeDef",
    "CreateEnvironmentProfileOutputTypeDef",
    "GetEnvironmentProfileOutputTypeDef",
    "UpdateEnvironmentProfileOutputTypeDef",
    "CreateFormTypeInputRequestTypeDef",
    "CreateGlossaryTermInputRequestTypeDef",
    "UpdateGlossaryTermInputRequestTypeDef",
    "CreateGlossaryTermOutputTypeDef",
    "GetGlossaryTermOutputTypeDef",
    "GlossaryTermItemTypeDef",
    "UpdateGlossaryTermOutputTypeDef",
    "CreateProjectMembershipInputRequestTypeDef",
    "DeleteProjectMembershipInputRequestTypeDef",
    "CreateProjectOutputTypeDef",
    "GetProjectOutputTypeDef",
    "ProjectSummaryTypeDef",
    "UpdateProjectOutputTypeDef",
    "CreateSubscriptionTargetInputRequestTypeDef",
    "CreateSubscriptionTargetOutputTypeDef",
    "GetSubscriptionTargetOutputTypeDef",
    "SubscriptionTargetSummaryTypeDef",
    "UpdateSubscriptionTargetInputRequestTypeDef",
    "UpdateSubscriptionTargetOutputTypeDef",
    "ListDataProductRevisionsOutputTypeDef",
    "DataSourceRunSummaryTypeDef",
    "GetDataSourceRunOutputTypeDef",
    "StartDataSourceRunOutputTypeDef",
    "DeploymentTypeDef",
    "ListDomainsOutputTypeDef",
    "ProjectGrantFilterTypeDef",
    "DomainUnitPolicyGrantPrincipalOutputTypeDef",
    "DomainUnitGrantFilterUnionTypeDef",
    "DomainUnitOwnerPropertiesTypeDef",
    "ListDomainUnitsForParentOutputTypeDef",
    "ListEnvironmentProfilesOutputTypeDef",
    "ListEnvironmentsOutputTypeDef",
    "SubscribedAssetTypeDef",
    "UpdateSubscriptionGrantStatusInputRequestTypeDef",
    "FilterClausePaginatorTypeDef",
    "FilterClauseTypeDef",
    "RelationalFilterConfigurationOutputTypeDef",
    "RelationalFilterConfigurationTypeDef",
    "FormTypeDataTypeDef",
    "GetFormTypeOutputTypeDef",
    "GetLineageNodeInputRequestTypeDef",
    "ListLineageNodeHistoryInputRequestTypeDef",
    "ListNotificationsInputRequestTypeDef",
    "ListTimeSeriesDataPointsInputRequestTypeDef",
    "TimeSeriesDataPointFormInputTypeDef",
    "GetLineageNodeOutputTypeDef",
    "GetMetadataGenerationRunOutputTypeDef",
    "MetadataGenerationRunItemTypeDef",
    "StartMetadataGenerationRunInputRequestTypeDef",
    "GetTimeSeriesDataPointOutputTypeDef",
    "PostTimeSeriesDataPointsOutputTypeDef",
    "GlueSelfGrantStatusOutputTypeDef",
    "RedshiftSelfGrantStatusOutputTypeDef",
    "GrantedEntityInputTypeDef",
    "GrantedEntityTypeDef",
    "SearchGroupProfilesOutputTypeDef",
    "InExpressionUnionTypeDef",
    "ProvisioningConfigurationOutputTypeDef",
    "LakeFormationConfigurationUnionTypeDef",
    "ListLineageNodeHistoryOutputTypeDef",
    "ListAssetFiltersInputListAssetFiltersPaginateTypeDef",
    "ListAssetRevisionsInputListAssetRevisionsPaginateTypeDef",
    "ListDataProductRevisionsInputListDataProductRevisionsPaginateTypeDef",
    "ListDataSourceRunActivitiesInputListDataSourceRunActivitiesPaginateTypeDef",
    "ListDataSourceRunsInputListDataSourceRunsPaginateTypeDef",
    "ListDataSourcesInputListDataSourcesPaginateTypeDef",
    "ListDomainUnitsForParentInputListDomainUnitsForParentPaginateTypeDef",
    "ListDomainsInputListDomainsPaginateTypeDef",
    "ListEntityOwnersInputListEntityOwnersPaginateTypeDef",
    "ListEnvironmentActionsInputListEnvironmentActionsPaginateTypeDef",
    "ListEnvironmentBlueprintConfigurationsInputListEnvironmentBlueprintConfigurationsPaginateTypeDef",
    "ListEnvironmentBlueprintsInputListEnvironmentBlueprintsPaginateTypeDef",
    "ListEnvironmentProfilesInputListEnvironmentProfilesPaginateTypeDef",
    "ListEnvironmentsInputListEnvironmentsPaginateTypeDef",
    "ListLineageNodeHistoryInputListLineageNodeHistoryPaginateTypeDef",
    "ListMetadataGenerationRunsInputListMetadataGenerationRunsPaginateTypeDef",
    "ListNotificationsInputListNotificationsPaginateTypeDef",
    "ListPolicyGrantsInputListPolicyGrantsPaginateTypeDef",
    "ListProjectMembershipsInputListProjectMembershipsPaginateTypeDef",
    "ListProjectsInputListProjectsPaginateTypeDef",
    "ListSubscriptionGrantsInputListSubscriptionGrantsPaginateTypeDef",
    "ListSubscriptionRequestsInputListSubscriptionRequestsPaginateTypeDef",
    "ListSubscriptionTargetsInputListSubscriptionTargetsPaginateTypeDef",
    "ListSubscriptionsInputListSubscriptionsPaginateTypeDef",
    "ListTimeSeriesDataPointsInputListTimeSeriesDataPointsPaginateTypeDef",
    "SearchGroupProfilesInputSearchGroupProfilesPaginateTypeDef",
    "SearchUserProfilesInputSearchUserProfilesPaginateTypeDef",
    "MemberDetailsTypeDef",
    "NotInExpressionUnionTypeDef",
    "RowFilterExpressionOutputTypeDef",
    "TopicTypeDef",
    "PolicyGrantDetailOutputTypeDef",
    "PolicyGrantDetailTypeDef",
    "OwnerPropertiesOutputTypeDef",
    "OwnerPropertiesTypeDef",
    "RedshiftStorageTypeDef",
    "RejectPredictionsInputRequestTypeDef",
    "UserProfileDetailsTypeDef",
    "SubscribedPrincipalInputTypeDef",
    "SubscribedPrincipalTypeDef",
    "UserPolicyGrantPrincipalUnionTypeDef",
    "CreateEnvironmentActionInputRequestTypeDef",
    "CreateEnvironmentActionOutputTypeDef",
    "EnvironmentActionSummaryTypeDef",
    "GetEnvironmentActionOutputTypeDef",
    "UpdateEnvironmentActionInputRequestTypeDef",
    "UpdateEnvironmentActionOutputTypeDef",
    "AssetItemTypeDef",
    "AssetListingItemTypeDef",
    "DataProductListingItemTypeDef",
    "DataProductListingTypeDef",
    "SubscribedListingItemTypeDef",
    "CreateAssetInputRequestTypeDef",
    "CreateAssetOutputTypeDef",
    "CreateAssetRevisionInputRequestTypeDef",
    "CreateAssetRevisionOutputTypeDef",
    "EnvironmentBlueprintSummaryTypeDef",
    "GetEnvironmentBlueprintOutputTypeDef",
    "CreateDataProductInputRequestTypeDef",
    "ListDataSourceRunActivitiesOutputTypeDef",
    "ListDataSourcesOutputTypeDef",
    "ListProjectsOutputTypeDef",
    "ListSubscriptionTargetsOutputTypeDef",
    "ListDataSourceRunsOutputTypeDef",
    "CreateEnvironmentOutputTypeDef",
    "GetEnvironmentOutputTypeDef",
    "UpdateEnvironmentOutputTypeDef",
    "ProjectPolicyGrantPrincipalTypeDef",
    "DomainUnitPolicyGrantPrincipalTypeDef",
    "CreateDomainUnitOutputTypeDef",
    "GetDomainUnitOutputTypeDef",
    "UpdateDomainUnitOutputTypeDef",
    "SearchInputSearchPaginateTypeDef",
    "SearchListingsInputSearchListingsPaginateTypeDef",
    "SearchTypesInputSearchTypesPaginateTypeDef",
    "SearchInputRequestTypeDef",
    "SearchListingsInputRequestTypeDef",
    "SearchTypesInputRequestTypeDef",
    "GlueRunConfigurationOutputTypeDef",
    "RelationalFilterConfigurationUnionTypeDef",
    "SearchTypesResultItemTypeDef",
    "PostTimeSeriesDataPointsInputRequestTypeDef",
    "ListMetadataGenerationRunsOutputTypeDef",
    "SelfGrantStatusOutputTypeDef",
    "CreateSubscriptionGrantInputRequestTypeDef",
    "CreateSubscriptionGrantOutputTypeDef",
    "DeleteSubscriptionGrantOutputTypeDef",
    "GetSubscriptionGrantOutputTypeDef",
    "SubscriptionGrantSummaryTypeDef",
    "UpdateSubscriptionGrantStatusOutputTypeDef",
    "EnvironmentBlueprintConfigurationItemTypeDef",
    "GetEnvironmentBlueprintConfigurationOutputTypeDef",
    "PutEnvironmentBlueprintConfigurationOutputTypeDef",
    "ProvisioningConfigurationTypeDef",
    "ProjectMemberTypeDef",
    "RowFilterExpressionTypeDef",
    "RowFilterOutputTypeDef",
    "NotificationOutputTypeDef",
    "ListEntityOwnersOutputTypeDef",
    "AddEntityOwnerInputRequestTypeDef",
    "RemoveEntityOwnerInputRequestTypeDef",
    "RedshiftRunConfigurationInputTypeDef",
    "RedshiftRunConfigurationOutputTypeDef",
    "CreateUserProfileOutputTypeDef",
    "GetUserProfileOutputTypeDef",
    "UpdateUserProfileOutputTypeDef",
    "UserProfileSummaryTypeDef",
    "CreateSubscriptionRequestInputRequestTypeDef",
    "ListEnvironmentActionsOutputTypeDef",
    "SearchInventoryResultItemTypeDef",
    "SearchResultItemTypeDef",
    "ListingItemTypeDef",
    "SubscribedListingTypeDef",
    "ListEnvironmentBlueprintsOutputTypeDef",
    "PolicyGrantPrincipalOutputTypeDef",
    "DomainUnitPolicyGrantPrincipalUnionTypeDef",
    "GlueRunConfigurationInputTypeDef",
    "SearchTypesOutputTypeDef",
    "ListSubscriptionGrantsOutputTypeDef",
    "ListEnvironmentBlueprintConfigurationsOutputTypeDef",
    "ProvisioningConfigurationUnionTypeDef",
    "ListProjectMembershipsOutputTypeDef",
    "RowFilterExpressionUnionTypeDef",
    "RowFilterConfigurationOutputTypeDef",
    "ListNotificationsOutputTypeDef",
    "DataSourceConfigurationOutputTypeDef",
    "SearchUserProfilesOutputTypeDef",
    "SearchOutputTypeDef",
    "SearchListingsOutputTypeDef",
    "GetListingOutputTypeDef",
    "AcceptSubscriptionRequestOutputTypeDef",
    "CancelSubscriptionOutputTypeDef",
    "CreateSubscriptionRequestOutputTypeDef",
    "GetSubscriptionOutputTypeDef",
    "GetSubscriptionRequestDetailsOutputTypeDef",
    "RejectSubscriptionRequestOutputTypeDef",
    "RevokeSubscriptionOutputTypeDef",
    "SubscriptionRequestSummaryTypeDef",
    "SubscriptionSummaryTypeDef",
    "UpdateSubscriptionRequestOutputTypeDef",
    "PolicyGrantMemberTypeDef",
    "PolicyGrantPrincipalTypeDef",
    "DataSourceConfigurationInputTypeDef",
    "PutEnvironmentBlueprintConfigurationInputRequestTypeDef",
    "RowFilterTypeDef",
    "AssetFilterConfigurationOutputTypeDef",
    "CreateDataSourceOutputTypeDef",
    "DeleteDataSourceOutputTypeDef",
    "GetDataSourceOutputTypeDef",
    "UpdateDataSourceOutputTypeDef",
    "ListSubscriptionRequestsOutputTypeDef",
    "ListSubscriptionsOutputTypeDef",
    "ListPolicyGrantsOutputTypeDef",
    "AddPolicyGrantInputRequestTypeDef",
    "RemovePolicyGrantInputRequestTypeDef",
    "CreateDataSourceInputRequestTypeDef",
    "UpdateDataSourceInputRequestTypeDef",
    "RowFilterUnionTypeDef",
    "CreateAssetFilterOutputTypeDef",
    "GetAssetFilterOutputTypeDef",
    "UpdateAssetFilterOutputTypeDef",
    "RowFilterConfigurationTypeDef",
    "RowFilterConfigurationUnionTypeDef",
    "AssetFilterConfigurationTypeDef",
    "CreateAssetFilterInputRequestTypeDef",
    "UpdateAssetFilterInputRequestTypeDef",
)

AcceptChoiceTypeDef = TypedDict(
    "AcceptChoiceTypeDef",
    {
        "predictionTarget": str,
        "editedValue": NotRequired[str],
        "predictionChoice": NotRequired[int],
    },
)
AcceptRuleTypeDef = TypedDict(
    "AcceptRuleTypeDef",
    {
        "rule": NotRequired[AcceptRuleBehaviorType],
        "threshold": NotRequired[float],
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
AcceptedAssetScopeTypeDef = TypedDict(
    "AcceptedAssetScopeTypeDef",
    {
        "assetId": str,
        "filterIds": Sequence[str],
    },
)
AwsConsoleLinkParametersTypeDef = TypedDict(
    "AwsConsoleLinkParametersTypeDef",
    {
        "uri": NotRequired[str],
    },
)
AddToProjectMemberPoolPolicyGrantDetailTypeDef = TypedDict(
    "AddToProjectMemberPoolPolicyGrantDetailTypeDef",
    {
        "includeChildDomainUnits": NotRequired[bool],
    },
)
ColumnFilterConfigurationOutputTypeDef = TypedDict(
    "ColumnFilterConfigurationOutputTypeDef",
    {
        "includedColumnNames": NotRequired[List[str]],
    },
)
AssetFilterSummaryTypeDef = TypedDict(
    "AssetFilterSummaryTypeDef",
    {
        "assetId": str,
        "domainId": str,
        "id": str,
        "name": str,
        "createdAt": NotRequired[datetime],
        "description": NotRequired[str],
        "effectiveColumnNames": NotRequired[List[str]],
        "effectiveRowFilter": NotRequired[str],
        "errorMessage": NotRequired[str],
        "status": NotRequired[FilterStatusType],
    },
)
AssetInDataProductListingItemTypeDef = TypedDict(
    "AssetInDataProductListingItemTypeDef",
    {
        "entityId": NotRequired[str],
        "entityRevision": NotRequired[str],
        "entityType": NotRequired[str],
    },
)
FormOutputTypeDef = TypedDict(
    "FormOutputTypeDef",
    {
        "formName": str,
        "content": NotRequired[str],
        "typeName": NotRequired[str],
        "typeRevision": NotRequired[str],
    },
)
TimeSeriesDataPointSummaryFormOutputTypeDef = TypedDict(
    "TimeSeriesDataPointSummaryFormOutputTypeDef",
    {
        "formName": str,
        "timestamp": datetime,
        "typeIdentifier": str,
        "contentSummary": NotRequired[str],
        "id": NotRequired[str],
        "typeRevision": NotRequired[str],
    },
)
AssetListingDetailsTypeDef = TypedDict(
    "AssetListingDetailsTypeDef",
    {
        "listingId": str,
        "listingStatus": ListingStatusType,
    },
)
DetailedGlossaryTermTypeDef = TypedDict(
    "DetailedGlossaryTermTypeDef",
    {
        "name": NotRequired[str],
        "shortDescription": NotRequired[str],
    },
)
AssetRevisionTypeDef = TypedDict(
    "AssetRevisionTypeDef",
    {
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "domainId": NotRequired[str],
        "id": NotRequired[str],
        "revision": NotRequired[str],
    },
)
AssetScopeTypeDef = TypedDict(
    "AssetScopeTypeDef",
    {
        "assetId": str,
        "filterIds": List[str],
        "status": str,
        "errorMessage": NotRequired[str],
    },
)
AssetTargetNameMapTypeDef = TypedDict(
    "AssetTargetNameMapTypeDef",
    {
        "assetId": str,
        "targetName": str,
    },
)
FormEntryOutputTypeDef = TypedDict(
    "FormEntryOutputTypeDef",
    {
        "typeName": str,
        "typeRevision": str,
        "required": NotRequired[bool],
    },
)
AssociateEnvironmentRoleInputRequestTypeDef = TypedDict(
    "AssociateEnvironmentRoleInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentIdentifier": str,
        "environmentRoleArn": str,
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
BusinessNameGenerationConfigurationTypeDef = TypedDict(
    "BusinessNameGenerationConfigurationTypeDef",
    {
        "enabled": NotRequired[bool],
    },
)
CancelMetadataGenerationRunInputRequestTypeDef = TypedDict(
    "CancelMetadataGenerationRunInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
CancelSubscriptionInputRequestTypeDef = TypedDict(
    "CancelSubscriptionInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
CloudFormationPropertiesTypeDef = TypedDict(
    "CloudFormationPropertiesTypeDef",
    {
        "templateUrl": str,
    },
)
ColumnFilterConfigurationTypeDef = TypedDict(
    "ColumnFilterConfigurationTypeDef",
    {
        "includedColumnNames": NotRequired[Sequence[str]],
    },
)
ConfigurableActionParameterTypeDef = TypedDict(
    "ConfigurableActionParameterTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[str],
    },
)
FormInputTypeDef = TypedDict(
    "FormInputTypeDef",
    {
        "formName": str,
        "content": NotRequired[str],
        "typeIdentifier": NotRequired[str],
        "typeRevision": NotRequired[str],
    },
)
FormEntryInputTypeDef = TypedDict(
    "FormEntryInputTypeDef",
    {
        "typeIdentifier": str,
        "typeRevision": str,
        "required": NotRequired[bool],
    },
)
CreateAssetTypePolicyGrantDetailTypeDef = TypedDict(
    "CreateAssetTypePolicyGrantDetailTypeDef",
    {
        "includeChildDomainUnits": NotRequired[bool],
    },
)
DataProductItemOutputTypeDef = TypedDict(
    "DataProductItemOutputTypeDef",
    {
        "identifier": str,
        "itemType": Literal["ASSET"],
        "glossaryTerms": NotRequired[List[str]],
        "revision": NotRequired[str],
    },
)
DataProductItemTypeDef = TypedDict(
    "DataProductItemTypeDef",
    {
        "identifier": str,
        "itemType": Literal["ASSET"],
        "glossaryTerms": NotRequired[Sequence[str]],
        "revision": NotRequired[str],
    },
)
RecommendationConfigurationTypeDef = TypedDict(
    "RecommendationConfigurationTypeDef",
    {
        "enableBusinessNameGeneration": NotRequired[bool],
    },
)
ScheduleConfigurationTypeDef = TypedDict(
    "ScheduleConfigurationTypeDef",
    {
        "schedule": NotRequired[str],
        "timezone": NotRequired[TimezoneType],
    },
)
DataSourceErrorMessageTypeDef = TypedDict(
    "DataSourceErrorMessageTypeDef",
    {
        "errorType": DataSourceErrorTypeType,
        "errorDetail": NotRequired[str],
    },
)
SingleSignOnTypeDef = TypedDict(
    "SingleSignOnTypeDef",
    {
        "type": NotRequired[AuthTypeType],
        "userAssignment": NotRequired[UserAssignmentType],
    },
)
CreateDomainUnitInputRequestTypeDef = TypedDict(
    "CreateDomainUnitInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "name": str,
        "parentDomainUnitIdentifier": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
    },
)
CreateDomainUnitPolicyGrantDetailTypeDef = TypedDict(
    "CreateDomainUnitPolicyGrantDetailTypeDef",
    {
        "includeChildDomainUnits": NotRequired[bool],
    },
)
EnvironmentParameterTypeDef = TypedDict(
    "EnvironmentParameterTypeDef",
    {
        "name": NotRequired[str],
        "value": NotRequired[str],
    },
)
CustomParameterTypeDef = TypedDict(
    "CustomParameterTypeDef",
    {
        "fieldType": str,
        "keyName": str,
        "defaultValue": NotRequired[str],
        "description": NotRequired[str],
        "isEditable": NotRequired[bool],
        "isOptional": NotRequired[bool],
    },
)
DeploymentPropertiesTypeDef = TypedDict(
    "DeploymentPropertiesTypeDef",
    {
        "endTimeoutMinutes": NotRequired[int],
        "startTimeoutMinutes": NotRequired[int],
    },
)
ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "type": str,
        "value": str,
        "name": NotRequired[str],
        "provider": NotRequired[str],
    },
)
CreateEnvironmentProfilePolicyGrantDetailTypeDef = TypedDict(
    "CreateEnvironmentProfilePolicyGrantDetailTypeDef",
    {
        "domainUnitId": NotRequired[str],
    },
)
ModelTypeDef = TypedDict(
    "ModelTypeDef",
    {
        "smithy": NotRequired[str],
    },
)
CreateFormTypePolicyGrantDetailTypeDef = TypedDict(
    "CreateFormTypePolicyGrantDetailTypeDef",
    {
        "includeChildDomainUnits": NotRequired[bool],
    },
)
CreateGlossaryInputRequestTypeDef = TypedDict(
    "CreateGlossaryInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "name": str,
        "owningProjectIdentifier": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "status": NotRequired[GlossaryStatusType],
    },
)
CreateGlossaryPolicyGrantDetailTypeDef = TypedDict(
    "CreateGlossaryPolicyGrantDetailTypeDef",
    {
        "includeChildDomainUnits": NotRequired[bool],
    },
)
TermRelationsTypeDef = TypedDict(
    "TermRelationsTypeDef",
    {
        "classifies": NotRequired[Sequence[str]],
        "isA": NotRequired[Sequence[str]],
    },
)
TermRelationsOutputTypeDef = TypedDict(
    "TermRelationsOutputTypeDef",
    {
        "classifies": NotRequired[List[str]],
        "isA": NotRequired[List[str]],
    },
)
CreateGroupProfileInputRequestTypeDef = TypedDict(
    "CreateGroupProfileInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "groupIdentifier": str,
        "clientToken": NotRequired[str],
    },
)
CreateListingChangeSetInputRequestTypeDef = TypedDict(
    "CreateListingChangeSetInputRequestTypeDef",
    {
        "action": ChangeActionType,
        "domainIdentifier": str,
        "entityIdentifier": str,
        "entityType": EntityTypeType,
        "clientToken": NotRequired[str],
        "entityRevision": NotRequired[str],
    },
)
CreateProjectInputRequestTypeDef = TypedDict(
    "CreateProjectInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "name": str,
        "description": NotRequired[str],
        "domainUnitId": NotRequired[str],
        "glossaryTerms": NotRequired[Sequence[str]],
    },
)
MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "groupIdentifier": NotRequired[str],
        "userIdentifier": NotRequired[str],
    },
)
ProjectDeletionErrorTypeDef = TypedDict(
    "ProjectDeletionErrorTypeDef",
    {
        "code": NotRequired[str],
        "message": NotRequired[str],
    },
)
CreateProjectPolicyGrantDetailTypeDef = TypedDict(
    "CreateProjectPolicyGrantDetailTypeDef",
    {
        "includeChildDomainUnits": NotRequired[bool],
    },
)
SubscribedListingInputTypeDef = TypedDict(
    "SubscribedListingInputTypeDef",
    {
        "identifier": str,
    },
)
SubscriptionTargetFormTypeDef = TypedDict(
    "SubscriptionTargetFormTypeDef",
    {
        "content": str,
        "formName": str,
    },
)
CreateUserProfileInputRequestTypeDef = TypedDict(
    "CreateUserProfileInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "userIdentifier": str,
        "clientToken": NotRequired[str],
        "userType": NotRequired[UserTypeType],
    },
)
DataProductListingItemAdditionalAttributesTypeDef = TypedDict(
    "DataProductListingItemAdditionalAttributesTypeDef",
    {
        "forms": NotRequired[str],
    },
)
DataProductResultItemTypeDef = TypedDict(
    "DataProductResultItemTypeDef",
    {
        "domainId": str,
        "id": str,
        "name": str,
        "owningProjectId": str,
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "description": NotRequired[str],
        "firstRevisionCreatedAt": NotRequired[datetime],
        "firstRevisionCreatedBy": NotRequired[str],
        "glossaryTerms": NotRequired[List[str]],
    },
)
DataProductRevisionTypeDef = TypedDict(
    "DataProductRevisionTypeDef",
    {
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "domainId": NotRequired[str],
        "id": NotRequired[str],
        "revision": NotRequired[str],
    },
)
RunStatisticsForAssetsTypeDef = TypedDict(
    "RunStatisticsForAssetsTypeDef",
    {
        "added": NotRequired[int],
        "failed": NotRequired[int],
        "skipped": NotRequired[int],
        "unchanged": NotRequired[int],
        "updated": NotRequired[int],
    },
)
DeleteAssetFilterInputRequestTypeDef = TypedDict(
    "DeleteAssetFilterInputRequestTypeDef",
    {
        "assetIdentifier": str,
        "domainIdentifier": str,
        "identifier": str,
    },
)
DeleteAssetInputRequestTypeDef = TypedDict(
    "DeleteAssetInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
DeleteAssetTypeInputRequestTypeDef = TypedDict(
    "DeleteAssetTypeInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
DeleteDataProductInputRequestTypeDef = TypedDict(
    "DeleteDataProductInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
DeleteDataSourceInputRequestTypeDef = TypedDict(
    "DeleteDataSourceInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "clientToken": NotRequired[str],
        "retainPermissionsOnRevokeFailure": NotRequired[bool],
    },
)
DeleteDomainInputRequestTypeDef = TypedDict(
    "DeleteDomainInputRequestTypeDef",
    {
        "identifier": str,
        "clientToken": NotRequired[str],
        "skipDeletionCheck": NotRequired[bool],
    },
)
DeleteDomainUnitInputRequestTypeDef = TypedDict(
    "DeleteDomainUnitInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
DeleteEnvironmentActionInputRequestTypeDef = TypedDict(
    "DeleteEnvironmentActionInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentIdentifier": str,
        "identifier": str,
    },
)
DeleteEnvironmentBlueprintConfigurationInputRequestTypeDef = TypedDict(
    "DeleteEnvironmentBlueprintConfigurationInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentBlueprintIdentifier": str,
    },
)
DeleteEnvironmentInputRequestTypeDef = TypedDict(
    "DeleteEnvironmentInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
DeleteEnvironmentProfileInputRequestTypeDef = TypedDict(
    "DeleteEnvironmentProfileInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
DeleteFormTypeInputRequestTypeDef = TypedDict(
    "DeleteFormTypeInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "formTypeIdentifier": str,
    },
)
DeleteGlossaryInputRequestTypeDef = TypedDict(
    "DeleteGlossaryInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
DeleteGlossaryTermInputRequestTypeDef = TypedDict(
    "DeleteGlossaryTermInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
DeleteListingInputRequestTypeDef = TypedDict(
    "DeleteListingInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
DeleteProjectInputRequestTypeDef = TypedDict(
    "DeleteProjectInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "skipDeletionCheck": NotRequired[bool],
    },
)
DeleteSubscriptionGrantInputRequestTypeDef = TypedDict(
    "DeleteSubscriptionGrantInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
DeleteSubscriptionRequestInputRequestTypeDef = TypedDict(
    "DeleteSubscriptionRequestInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
DeleteSubscriptionTargetInputRequestTypeDef = TypedDict(
    "DeleteSubscriptionTargetInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentIdentifier": str,
        "identifier": str,
    },
)
DeleteTimeSeriesDataPointsInputRequestTypeDef = TypedDict(
    "DeleteTimeSeriesDataPointsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "entityIdentifier": str,
        "entityType": TimeSeriesEntityTypeType,
        "formName": str,
        "clientToken": NotRequired[str],
    },
)
EnvironmentErrorTypeDef = TypedDict(
    "EnvironmentErrorTypeDef",
    {
        "message": str,
        "code": NotRequired[str],
    },
)
DisassociateEnvironmentRoleInputRequestTypeDef = TypedDict(
    "DisassociateEnvironmentRoleInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentIdentifier": str,
        "environmentRoleArn": str,
    },
)
DomainSummaryTypeDef = TypedDict(
    "DomainSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "id": str,
        "managedAccountId": str,
        "name": str,
        "status": DomainStatusType,
        "description": NotRequired[str],
        "lastUpdatedAt": NotRequired[datetime],
        "portalUrl": NotRequired[str],
    },
)
DomainUnitFilterForProjectTypeDef = TypedDict(
    "DomainUnitFilterForProjectTypeDef",
    {
        "domainUnit": str,
        "includeChildDomainUnits": NotRequired[bool],
    },
)
DomainUnitGrantFilterOutputTypeDef = TypedDict(
    "DomainUnitGrantFilterOutputTypeDef",
    {
        "allDomainUnitsGrantFilter": NotRequired[Dict[str, Any]],
    },
)
DomainUnitGrantFilterTypeDef = TypedDict(
    "DomainUnitGrantFilterTypeDef",
    {
        "allDomainUnitsGrantFilter": NotRequired[Mapping[str, Any]],
    },
)
DomainUnitGroupPropertiesTypeDef = TypedDict(
    "DomainUnitGroupPropertiesTypeDef",
    {
        "groupId": NotRequired[str],
    },
)
DomainUnitUserPropertiesTypeDef = TypedDict(
    "DomainUnitUserPropertiesTypeDef",
    {
        "userId": NotRequired[str],
    },
)
DomainUnitSummaryTypeDef = TypedDict(
    "DomainUnitSummaryTypeDef",
    {
        "id": str,
        "name": str,
    },
)
EnvironmentProfileSummaryTypeDef = TypedDict(
    "EnvironmentProfileSummaryTypeDef",
    {
        "createdBy": str,
        "domainId": str,
        "environmentBlueprintId": str,
        "id": str,
        "name": str,
        "awsAccountId": NotRequired[str],
        "awsAccountRegion": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "description": NotRequired[str],
        "projectId": NotRequired[str],
        "updatedAt": NotRequired[datetime],
    },
)
EnvironmentSummaryTypeDef = TypedDict(
    "EnvironmentSummaryTypeDef",
    {
        "createdBy": str,
        "domainId": str,
        "name": str,
        "projectId": str,
        "provider": str,
        "awsAccountId": NotRequired[str],
        "awsAccountRegion": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "description": NotRequired[str],
        "environmentProfileId": NotRequired[str],
        "id": NotRequired[str],
        "status": NotRequired[EnvironmentStatusType],
        "updatedAt": NotRequired[datetime],
    },
)
EqualToExpressionTypeDef = TypedDict(
    "EqualToExpressionTypeDef",
    {
        "columnName": str,
        "value": str,
    },
)
FailureCauseTypeDef = TypedDict(
    "FailureCauseTypeDef",
    {
        "message": NotRequired[str],
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "attribute": str,
        "value": str,
    },
)
FilterExpressionTypeDef = TypedDict(
    "FilterExpressionTypeDef",
    {
        "expression": str,
        "type": FilterExpressionTypeType,
    },
)
ImportTypeDef = TypedDict(
    "ImportTypeDef",
    {
        "name": str,
        "revision": str,
    },
)
GetAssetFilterInputRequestTypeDef = TypedDict(
    "GetAssetFilterInputRequestTypeDef",
    {
        "assetIdentifier": str,
        "domainIdentifier": str,
        "identifier": str,
    },
)
GetAssetInputRequestTypeDef = TypedDict(
    "GetAssetInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "revision": NotRequired[str],
    },
)
GetAssetTypeInputRequestTypeDef = TypedDict(
    "GetAssetTypeInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "revision": NotRequired[str],
    },
)
GetDataProductInputRequestTypeDef = TypedDict(
    "GetDataProductInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "revision": NotRequired[str],
    },
)
GetDataSourceInputRequestTypeDef = TypedDict(
    "GetDataSourceInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
GetDataSourceRunInputRequestTypeDef = TypedDict(
    "GetDataSourceRunInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
GetDomainInputRequestTypeDef = TypedDict(
    "GetDomainInputRequestTypeDef",
    {
        "identifier": str,
    },
)
GetDomainUnitInputRequestTypeDef = TypedDict(
    "GetDomainUnitInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
GetEnvironmentActionInputRequestTypeDef = TypedDict(
    "GetEnvironmentActionInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentIdentifier": str,
        "identifier": str,
    },
)
GetEnvironmentBlueprintConfigurationInputRequestTypeDef = TypedDict(
    "GetEnvironmentBlueprintConfigurationInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentBlueprintIdentifier": str,
    },
)
GetEnvironmentBlueprintInputRequestTypeDef = TypedDict(
    "GetEnvironmentBlueprintInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
GetEnvironmentCredentialsInputRequestTypeDef = TypedDict(
    "GetEnvironmentCredentialsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentIdentifier": str,
    },
)
GetEnvironmentInputRequestTypeDef = TypedDict(
    "GetEnvironmentInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
GetEnvironmentProfileInputRequestTypeDef = TypedDict(
    "GetEnvironmentProfileInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
GetFormTypeInputRequestTypeDef = TypedDict(
    "GetFormTypeInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "formTypeIdentifier": str,
        "revision": NotRequired[str],
    },
)
GetGlossaryInputRequestTypeDef = TypedDict(
    "GetGlossaryInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
GetGlossaryTermInputRequestTypeDef = TypedDict(
    "GetGlossaryTermInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
GetGroupProfileInputRequestTypeDef = TypedDict(
    "GetGroupProfileInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "groupIdentifier": str,
    },
)
GetIamPortalLoginUrlInputRequestTypeDef = TypedDict(
    "GetIamPortalLoginUrlInputRequestTypeDef",
    {
        "domainIdentifier": str,
    },
)
TimestampTypeDef = Union[datetime, str]
LineageNodeReferenceTypeDef = TypedDict(
    "LineageNodeReferenceTypeDef",
    {
        "eventTimestamp": NotRequired[datetime],
        "id": NotRequired[str],
    },
)
GetListingInputRequestTypeDef = TypedDict(
    "GetListingInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "listingRevision": NotRequired[str],
    },
)
GetMetadataGenerationRunInputRequestTypeDef = TypedDict(
    "GetMetadataGenerationRunInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
MetadataGenerationRunTargetTypeDef = TypedDict(
    "MetadataGenerationRunTargetTypeDef",
    {
        "identifier": str,
        "type": Literal["ASSET"],
        "revision": NotRequired[str],
    },
)
GetProjectInputRequestTypeDef = TypedDict(
    "GetProjectInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
GetSubscriptionGrantInputRequestTypeDef = TypedDict(
    "GetSubscriptionGrantInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
GetSubscriptionInputRequestTypeDef = TypedDict(
    "GetSubscriptionInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
GetSubscriptionRequestDetailsInputRequestTypeDef = TypedDict(
    "GetSubscriptionRequestDetailsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
GetSubscriptionTargetInputRequestTypeDef = TypedDict(
    "GetSubscriptionTargetInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentIdentifier": str,
        "identifier": str,
    },
)
GetTimeSeriesDataPointInputRequestTypeDef = TypedDict(
    "GetTimeSeriesDataPointInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "entityIdentifier": str,
        "entityType": TimeSeriesEntityTypeType,
        "formName": str,
        "identifier": str,
    },
)
TimeSeriesDataPointFormOutputTypeDef = TypedDict(
    "TimeSeriesDataPointFormOutputTypeDef",
    {
        "formName": str,
        "timestamp": datetime,
        "typeIdentifier": str,
        "content": NotRequired[str],
        "id": NotRequired[str],
        "typeRevision": NotRequired[str],
    },
)
GetUserProfileInputRequestTypeDef = TypedDict(
    "GetUserProfileInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "userIdentifier": str,
        "type": NotRequired[UserProfileTypeType],
    },
)
GlossaryItemTypeDef = TypedDict(
    "GlossaryItemTypeDef",
    {
        "domainId": str,
        "id": str,
        "name": str,
        "owningProjectId": str,
        "status": GlossaryStatusType,
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "description": NotRequired[str],
        "updatedAt": NotRequired[datetime],
        "updatedBy": NotRequired[str],
    },
)
SelfGrantStatusDetailTypeDef = TypedDict(
    "SelfGrantStatusDetailTypeDef",
    {
        "databaseName": str,
        "status": SelfGrantStatusType,
        "failureCause": NotRequired[str],
        "schemaName": NotRequired[str],
    },
)
ListingRevisionInputTypeDef = TypedDict(
    "ListingRevisionInputTypeDef",
    {
        "identifier": str,
        "revision": str,
    },
)
ListingRevisionTypeDef = TypedDict(
    "ListingRevisionTypeDef",
    {
        "id": str,
        "revision": str,
    },
)
GreaterThanExpressionTypeDef = TypedDict(
    "GreaterThanExpressionTypeDef",
    {
        "columnName": str,
        "value": str,
    },
)
GreaterThanOrEqualToExpressionTypeDef = TypedDict(
    "GreaterThanOrEqualToExpressionTypeDef",
    {
        "columnName": str,
        "value": str,
    },
)
GroupDetailsTypeDef = TypedDict(
    "GroupDetailsTypeDef",
    {
        "groupId": str,
    },
)
GroupPolicyGrantPrincipalTypeDef = TypedDict(
    "GroupPolicyGrantPrincipalTypeDef",
    {
        "groupIdentifier": NotRequired[str],
    },
)
GroupProfileSummaryTypeDef = TypedDict(
    "GroupProfileSummaryTypeDef",
    {
        "domainId": NotRequired[str],
        "groupName": NotRequired[str],
        "id": NotRequired[str],
        "status": NotRequired[GroupProfileStatusType],
    },
)
IamUserProfileDetailsTypeDef = TypedDict(
    "IamUserProfileDetailsTypeDef",
    {
        "arn": NotRequired[str],
    },
)
InExpressionOutputTypeDef = TypedDict(
    "InExpressionOutputTypeDef",
    {
        "columnName": str,
        "values": List[str],
    },
)
InExpressionTypeDef = TypedDict(
    "InExpressionTypeDef",
    {
        "columnName": str,
        "values": Sequence[str],
    },
)
IsNotNullExpressionTypeDef = TypedDict(
    "IsNotNullExpressionTypeDef",
    {
        "columnName": str,
    },
)
IsNullExpressionTypeDef = TypedDict(
    "IsNullExpressionTypeDef",
    {
        "columnName": str,
    },
)
LakeFormationConfigurationOutputTypeDef = TypedDict(
    "LakeFormationConfigurationOutputTypeDef",
    {
        "locationRegistrationExcludeS3Locations": NotRequired[List[str]],
        "locationRegistrationRole": NotRequired[str],
    },
)
LakeFormationConfigurationTypeDef = TypedDict(
    "LakeFormationConfigurationTypeDef",
    {
        "locationRegistrationExcludeS3Locations": NotRequired[Sequence[str]],
        "locationRegistrationRole": NotRequired[str],
    },
)
LessThanExpressionTypeDef = TypedDict(
    "LessThanExpressionTypeDef",
    {
        "columnName": str,
        "value": str,
    },
)
LessThanOrEqualToExpressionTypeDef = TypedDict(
    "LessThanOrEqualToExpressionTypeDef",
    {
        "columnName": str,
        "value": str,
    },
)
LikeExpressionTypeDef = TypedDict(
    "LikeExpressionTypeDef",
    {
        "columnName": str,
        "value": str,
    },
)
LineageNodeSummaryTypeDef = TypedDict(
    "LineageNodeSummaryTypeDef",
    {
        "domainId": str,
        "id": str,
        "typeName": str,
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "description": NotRequired[str],
        "eventTimestamp": NotRequired[datetime],
        "name": NotRequired[str],
        "sourceIdentifier": NotRequired[str],
        "typeRevision": NotRequired[str],
        "updatedAt": NotRequired[datetime],
        "updatedBy": NotRequired[str],
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
ListAssetFiltersInputRequestTypeDef = TypedDict(
    "ListAssetFiltersInputRequestTypeDef",
    {
        "assetIdentifier": str,
        "domainIdentifier": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "status": NotRequired[FilterStatusType],
    },
)
ListAssetRevisionsInputRequestTypeDef = TypedDict(
    "ListAssetRevisionsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListDataProductRevisionsInputRequestTypeDef = TypedDict(
    "ListDataProductRevisionsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListDataSourceRunActivitiesInputRequestTypeDef = TypedDict(
    "ListDataSourceRunActivitiesInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "status": NotRequired[DataAssetActivityStatusType],
    },
)
ListDataSourceRunsInputRequestTypeDef = TypedDict(
    "ListDataSourceRunsInputRequestTypeDef",
    {
        "dataSourceIdentifier": str,
        "domainIdentifier": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "status": NotRequired[DataSourceRunStatusType],
    },
)
ListDataSourcesInputRequestTypeDef = TypedDict(
    "ListDataSourcesInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "projectIdentifier": str,
        "environmentIdentifier": NotRequired[str],
        "maxResults": NotRequired[int],
        "name": NotRequired[str],
        "nextToken": NotRequired[str],
        "status": NotRequired[DataSourceStatusType],
        "type": NotRequired[str],
    },
)
ListDomainUnitsForParentInputRequestTypeDef = TypedDict(
    "ListDomainUnitsForParentInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "parentDomainUnitIdentifier": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListDomainsInputRequestTypeDef = TypedDict(
    "ListDomainsInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "status": NotRequired[DomainStatusType],
    },
)
ListEntityOwnersInputRequestTypeDef = TypedDict(
    "ListEntityOwnersInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "entityIdentifier": str,
        "entityType": Literal["DOMAIN_UNIT"],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListEnvironmentActionsInputRequestTypeDef = TypedDict(
    "ListEnvironmentActionsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentIdentifier": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListEnvironmentBlueprintConfigurationsInputRequestTypeDef = TypedDict(
    "ListEnvironmentBlueprintConfigurationsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListEnvironmentBlueprintsInputRequestTypeDef = TypedDict(
    "ListEnvironmentBlueprintsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "managed": NotRequired[bool],
        "maxResults": NotRequired[int],
        "name": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)
ListEnvironmentProfilesInputRequestTypeDef = TypedDict(
    "ListEnvironmentProfilesInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "awsAccountId": NotRequired[str],
        "awsAccountRegion": NotRequired[str],
        "environmentBlueprintIdentifier": NotRequired[str],
        "maxResults": NotRequired[int],
        "name": NotRequired[str],
        "nextToken": NotRequired[str],
        "projectIdentifier": NotRequired[str],
    },
)
ListEnvironmentsInputRequestTypeDef = TypedDict(
    "ListEnvironmentsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "projectIdentifier": str,
        "awsAccountId": NotRequired[str],
        "awsAccountRegion": NotRequired[str],
        "environmentBlueprintIdentifier": NotRequired[str],
        "environmentProfileIdentifier": NotRequired[str],
        "maxResults": NotRequired[int],
        "name": NotRequired[str],
        "nextToken": NotRequired[str],
        "provider": NotRequired[str],
        "status": NotRequired[EnvironmentStatusType],
    },
)
ListMetadataGenerationRunsInputRequestTypeDef = TypedDict(
    "ListMetadataGenerationRunsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "status": NotRequired[MetadataGenerationRunStatusType],
        "type": NotRequired[Literal["BUSINESS_DESCRIPTIONS"]],
    },
)
ListPolicyGrantsInputRequestTypeDef = TypedDict(
    "ListPolicyGrantsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "entityIdentifier": str,
        "entityType": TargetEntityTypeType,
        "policyType": ManagedPolicyTypeType,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListProjectMembershipsInputRequestTypeDef = TypedDict(
    "ListProjectMembershipsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "projectIdentifier": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortBy": NotRequired[Literal["NAME"]],
        "sortOrder": NotRequired[SortOrderType],
    },
)
ListProjectsInputRequestTypeDef = TypedDict(
    "ListProjectsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "groupIdentifier": NotRequired[str],
        "maxResults": NotRequired[int],
        "name": NotRequired[str],
        "nextToken": NotRequired[str],
        "userIdentifier": NotRequired[str],
    },
)
ListSubscriptionGrantsInputRequestTypeDef = TypedDict(
    "ListSubscriptionGrantsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentId": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "owningProjectId": NotRequired[str],
        "sortBy": NotRequired[SortKeyType],
        "sortOrder": NotRequired[SortOrderType],
        "subscribedListingId": NotRequired[str],
        "subscriptionId": NotRequired[str],
        "subscriptionTargetId": NotRequired[str],
    },
)
ListSubscriptionRequestsInputRequestTypeDef = TypedDict(
    "ListSubscriptionRequestsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "approverProjectId": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "owningProjectId": NotRequired[str],
        "sortBy": NotRequired[SortKeyType],
        "sortOrder": NotRequired[SortOrderType],
        "status": NotRequired[SubscriptionRequestStatusType],
        "subscribedListingId": NotRequired[str],
    },
)
ListSubscriptionTargetsInputRequestTypeDef = TypedDict(
    "ListSubscriptionTargetsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentIdentifier": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortBy": NotRequired[SortKeyType],
        "sortOrder": NotRequired[SortOrderType],
    },
)
ListSubscriptionsInputRequestTypeDef = TypedDict(
    "ListSubscriptionsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "approverProjectId": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "owningProjectId": NotRequired[str],
        "sortBy": NotRequired[SortKeyType],
        "sortOrder": NotRequired[SortOrderType],
        "status": NotRequired[SubscriptionStatusType],
        "subscribedListingId": NotRequired[str],
        "subscriptionRequestIdentifier": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
UserDetailsTypeDef = TypedDict(
    "UserDetailsTypeDef",
    {
        "userId": str,
    },
)
NotEqualToExpressionTypeDef = TypedDict(
    "NotEqualToExpressionTypeDef",
    {
        "columnName": str,
        "value": str,
    },
)
NotInExpressionOutputTypeDef = TypedDict(
    "NotInExpressionOutputTypeDef",
    {
        "columnName": str,
        "values": List[str],
    },
)
NotInExpressionTypeDef = TypedDict(
    "NotInExpressionTypeDef",
    {
        "columnName": str,
        "values": Sequence[str],
    },
)
NotLikeExpressionTypeDef = TypedDict(
    "NotLikeExpressionTypeDef",
    {
        "columnName": str,
        "value": str,
    },
)
NotificationResourceTypeDef = TypedDict(
    "NotificationResourceTypeDef",
    {
        "id": str,
        "type": Literal["PROJECT"],
        "name": NotRequired[str],
    },
)
OverrideDomainUnitOwnersPolicyGrantDetailTypeDef = TypedDict(
    "OverrideDomainUnitOwnersPolicyGrantDetailTypeDef",
    {
        "includeChildDomainUnits": NotRequired[bool],
    },
)
OverrideProjectOwnersPolicyGrantDetailTypeDef = TypedDict(
    "OverrideProjectOwnersPolicyGrantDetailTypeDef",
    {
        "includeChildDomainUnits": NotRequired[bool],
    },
)
OwnerGroupPropertiesOutputTypeDef = TypedDict(
    "OwnerGroupPropertiesOutputTypeDef",
    {
        "groupId": NotRequired[str],
    },
)
OwnerGroupPropertiesTypeDef = TypedDict(
    "OwnerGroupPropertiesTypeDef",
    {
        "groupIdentifier": str,
    },
)
OwnerUserPropertiesOutputTypeDef = TypedDict(
    "OwnerUserPropertiesOutputTypeDef",
    {
        "userId": NotRequired[str],
    },
)
OwnerUserPropertiesTypeDef = TypedDict(
    "OwnerUserPropertiesTypeDef",
    {
        "userIdentifier": str,
    },
)
UserPolicyGrantPrincipalOutputTypeDef = TypedDict(
    "UserPolicyGrantPrincipalOutputTypeDef",
    {
        "allUsersGrantFilter": NotRequired[Dict[str, Any]],
        "userIdentifier": NotRequired[str],
    },
)
RedshiftClusterStorageTypeDef = TypedDict(
    "RedshiftClusterStorageTypeDef",
    {
        "clusterName": str,
    },
)
RedshiftCredentialConfigurationTypeDef = TypedDict(
    "RedshiftCredentialConfigurationTypeDef",
    {
        "secretManagerArn": str,
    },
)
RedshiftServerlessStorageTypeDef = TypedDict(
    "RedshiftServerlessStorageTypeDef",
    {
        "workgroupName": str,
    },
)
RejectChoiceTypeDef = TypedDict(
    "RejectChoiceTypeDef",
    {
        "predictionTarget": str,
        "predictionChoices": NotRequired[Sequence[int]],
    },
)
RejectRuleTypeDef = TypedDict(
    "RejectRuleTypeDef",
    {
        "rule": NotRequired[RejectRuleBehaviorType],
        "threshold": NotRequired[float],
    },
)
RejectSubscriptionRequestInputRequestTypeDef = TypedDict(
    "RejectSubscriptionRequestInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "decisionComment": NotRequired[str],
    },
)
RevokeSubscriptionInputRequestTypeDef = TypedDict(
    "RevokeSubscriptionInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "retainPermissions": NotRequired[bool],
    },
)
SearchGroupProfilesInputRequestTypeDef = TypedDict(
    "SearchGroupProfilesInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "groupType": GroupSearchTypeType,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "searchText": NotRequired[str],
    },
)
SearchInItemTypeDef = TypedDict(
    "SearchInItemTypeDef",
    {
        "attribute": str,
    },
)
SearchSortTypeDef = TypedDict(
    "SearchSortTypeDef",
    {
        "attribute": str,
        "order": NotRequired[SortOrderType],
    },
)
SearchUserProfilesInputRequestTypeDef = TypedDict(
    "SearchUserProfilesInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "userType": UserSearchTypeType,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "searchText": NotRequired[str],
    },
)
SsoUserProfileDetailsTypeDef = TypedDict(
    "SsoUserProfileDetailsTypeDef",
    {
        "firstName": NotRequired[str],
        "lastName": NotRequired[str],
        "username": NotRequired[str],
    },
)
StartDataSourceRunInputRequestTypeDef = TypedDict(
    "StartDataSourceRunInputRequestTypeDef",
    {
        "dataSourceIdentifier": str,
        "domainIdentifier": str,
        "clientToken": NotRequired[str],
    },
)
SubscribedProjectInputTypeDef = TypedDict(
    "SubscribedProjectInputTypeDef",
    {
        "identifier": NotRequired[str],
    },
)
SubscribedProjectTypeDef = TypedDict(
    "SubscribedProjectTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
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
UpdateDomainUnitInputRequestTypeDef = TypedDict(
    "UpdateDomainUnitInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "description": NotRequired[str],
        "name": NotRequired[str],
    },
)
UpdateEnvironmentInputRequestTypeDef = TypedDict(
    "UpdateEnvironmentInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "description": NotRequired[str],
        "glossaryTerms": NotRequired[Sequence[str]],
        "name": NotRequired[str],
    },
)
UpdateGlossaryInputRequestTypeDef = TypedDict(
    "UpdateGlossaryInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "name": NotRequired[str],
        "status": NotRequired[GlossaryStatusType],
    },
)
UpdateGroupProfileInputRequestTypeDef = TypedDict(
    "UpdateGroupProfileInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "groupIdentifier": str,
        "status": GroupProfileStatusType,
    },
)
UpdateProjectInputRequestTypeDef = TypedDict(
    "UpdateProjectInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "description": NotRequired[str],
        "glossaryTerms": NotRequired[Sequence[str]],
        "name": NotRequired[str],
    },
)
UpdateSubscriptionRequestInputRequestTypeDef = TypedDict(
    "UpdateSubscriptionRequestInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "requestReason": str,
    },
)
UpdateUserProfileInputRequestTypeDef = TypedDict(
    "UpdateUserProfileInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "status": UserProfileStatusType,
        "userIdentifier": str,
        "type": NotRequired[UserProfileTypeType],
    },
)
UserPolicyGrantPrincipalTypeDef = TypedDict(
    "UserPolicyGrantPrincipalTypeDef",
    {
        "allUsersGrantFilter": NotRequired[Mapping[str, Any]],
        "userIdentifier": NotRequired[str],
    },
)
AcceptPredictionsInputRequestTypeDef = TypedDict(
    "AcceptPredictionsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "acceptChoices": NotRequired[Sequence[AcceptChoiceTypeDef]],
        "acceptRule": NotRequired[AcceptRuleTypeDef],
        "clientToken": NotRequired[str],
        "revision": NotRequired[str],
    },
)
AcceptPredictionsOutputTypeDef = TypedDict(
    "AcceptPredictionsOutputTypeDef",
    {
        "assetId": str,
        "domainId": str,
        "revision": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFormTypeOutputTypeDef = TypedDict(
    "CreateFormTypeOutputTypeDef",
    {
        "description": str,
        "domainId": str,
        "name": str,
        "originDomainId": str,
        "originProjectId": str,
        "owningProjectId": str,
        "revision": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGlossaryOutputTypeDef = TypedDict(
    "CreateGlossaryOutputTypeDef",
    {
        "description": str,
        "domainId": str,
        "id": str,
        "name": str,
        "owningProjectId": str,
        "status": GlossaryStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGroupProfileOutputTypeDef = TypedDict(
    "CreateGroupProfileOutputTypeDef",
    {
        "domainId": str,
        "groupName": str,
        "id": str,
        "status": GroupProfileStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateListingChangeSetOutputTypeDef = TypedDict(
    "CreateListingChangeSetOutputTypeDef",
    {
        "listingId": str,
        "listingRevision": str,
        "status": ListingStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDomainOutputTypeDef = TypedDict(
    "DeleteDomainOutputTypeDef",
    {
        "status": DomainStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEnvironmentCredentialsOutputTypeDef = TypedDict(
    "GetEnvironmentCredentialsOutputTypeDef",
    {
        "accessKeyId": str,
        "expiration": datetime,
        "secretAccessKey": str,
        "sessionToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetGlossaryOutputTypeDef = TypedDict(
    "GetGlossaryOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "id": str,
        "name": str,
        "owningProjectId": str,
        "status": GlossaryStatusType,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetGroupProfileOutputTypeDef = TypedDict(
    "GetGroupProfileOutputTypeDef",
    {
        "domainId": str,
        "groupName": str,
        "id": str,
        "status": GroupProfileStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIamPortalLoginUrlOutputTypeDef = TypedDict(
    "GetIamPortalLoginUrlOutputTypeDef",
    {
        "authCodeUrl": str,
        "userProfileId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RejectPredictionsOutputTypeDef = TypedDict(
    "RejectPredictionsOutputTypeDef",
    {
        "assetId": str,
        "assetRevision": str,
        "domainId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartMetadataGenerationRunOutputTypeDef = TypedDict(
    "StartMetadataGenerationRunOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "id": str,
        "owningProjectId": str,
        "status": MetadataGenerationRunStatusType,
        "type": Literal["BUSINESS_DESCRIPTIONS"],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateGlossaryOutputTypeDef = TypedDict(
    "UpdateGlossaryOutputTypeDef",
    {
        "description": str,
        "domainId": str,
        "id": str,
        "name": str,
        "owningProjectId": str,
        "status": GlossaryStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateGroupProfileOutputTypeDef = TypedDict(
    "UpdateGroupProfileOutputTypeDef",
    {
        "domainId": str,
        "groupName": str,
        "id": str,
        "status": GroupProfileStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AcceptSubscriptionRequestInputRequestTypeDef = TypedDict(
    "AcceptSubscriptionRequestInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "assetScopes": NotRequired[Sequence[AcceptedAssetScopeTypeDef]],
        "decisionComment": NotRequired[str],
    },
)
ActionParametersTypeDef = TypedDict(
    "ActionParametersTypeDef",
    {
        "awsConsoleLink": NotRequired[AwsConsoleLinkParametersTypeDef],
    },
)
ListAssetFiltersOutputTypeDef = TypedDict(
    "ListAssetFiltersOutputTypeDef",
    {
        "items": List[AssetFilterSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssetItemAdditionalAttributesTypeDef = TypedDict(
    "AssetItemAdditionalAttributesTypeDef",
    {
        "formsOutput": NotRequired[List[FormOutputTypeDef]],
        "latestTimeSeriesDataPointFormsOutput": NotRequired[
            List[TimeSeriesDataPointSummaryFormOutputTypeDef]
        ],
        "readOnlyFormsOutput": NotRequired[List[FormOutputTypeDef]],
    },
)
AssetListingItemAdditionalAttributesTypeDef = TypedDict(
    "AssetListingItemAdditionalAttributesTypeDef",
    {
        "forms": NotRequired[str],
        "latestTimeSeriesDataPointForms": NotRequired[
            List[TimeSeriesDataPointSummaryFormOutputTypeDef]
        ],
    },
)
ListTimeSeriesDataPointsOutputTypeDef = TypedDict(
    "ListTimeSeriesDataPointsOutputTypeDef",
    {
        "items": List[TimeSeriesDataPointSummaryFormOutputTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAssetOutputTypeDef = TypedDict(
    "GetAssetOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "externalIdentifier": str,
        "firstRevisionCreatedAt": datetime,
        "firstRevisionCreatedBy": str,
        "formsOutput": List[FormOutputTypeDef],
        "glossaryTerms": List[str],
        "id": str,
        "latestTimeSeriesDataPointFormsOutput": List[TimeSeriesDataPointSummaryFormOutputTypeDef],
        "listing": AssetListingDetailsTypeDef,
        "name": str,
        "owningProjectId": str,
        "readOnlyFormsOutput": List[FormOutputTypeDef],
        "revision": str,
        "typeIdentifier": str,
        "typeRevision": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssetListingTypeDef = TypedDict(
    "AssetListingTypeDef",
    {
        "assetId": NotRequired[str],
        "assetRevision": NotRequired[str],
        "assetType": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "forms": NotRequired[str],
        "glossaryTerms": NotRequired[List[DetailedGlossaryTermTypeDef]],
        "latestTimeSeriesDataPointForms": NotRequired[
            List[TimeSeriesDataPointSummaryFormOutputTypeDef]
        ],
        "owningProjectId": NotRequired[str],
    },
)
ListingSummaryItemTypeDef = TypedDict(
    "ListingSummaryItemTypeDef",
    {
        "glossaryTerms": NotRequired[List[DetailedGlossaryTermTypeDef]],
        "listingId": NotRequired[str],
        "listingRevision": NotRequired[str],
    },
)
ListingSummaryTypeDef = TypedDict(
    "ListingSummaryTypeDef",
    {
        "glossaryTerms": NotRequired[List[DetailedGlossaryTermTypeDef]],
        "listingId": NotRequired[str],
        "listingRevision": NotRequired[str],
    },
)
SubscribedProductListingTypeDef = TypedDict(
    "SubscribedProductListingTypeDef",
    {
        "assetListings": NotRequired[List[AssetInDataProductListingItemTypeDef]],
        "description": NotRequired[str],
        "entityId": NotRequired[str],
        "entityRevision": NotRequired[str],
        "glossaryTerms": NotRequired[List[DetailedGlossaryTermTypeDef]],
        "name": NotRequired[str],
    },
)
ListAssetRevisionsOutputTypeDef = TypedDict(
    "ListAssetRevisionsOutputTypeDef",
    {
        "items": List[AssetRevisionTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SubscribedAssetListingTypeDef = TypedDict(
    "SubscribedAssetListingTypeDef",
    {
        "assetScope": NotRequired[AssetScopeTypeDef],
        "entityId": NotRequired[str],
        "entityRevision": NotRequired[str],
        "entityType": NotRequired[str],
        "forms": NotRequired[str],
        "glossaryTerms": NotRequired[List[DetailedGlossaryTermTypeDef]],
    },
)
AssetTypeItemTypeDef = TypedDict(
    "AssetTypeItemTypeDef",
    {
        "domainId": str,
        "formsOutput": Dict[str, FormEntryOutputTypeDef],
        "name": str,
        "owningProjectId": str,
        "revision": str,
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "description": NotRequired[str],
        "originDomainId": NotRequired[str],
        "originProjectId": NotRequired[str],
        "updatedAt": NotRequired[datetime],
        "updatedBy": NotRequired[str],
    },
)
CreateAssetTypeOutputTypeDef = TypedDict(
    "CreateAssetTypeOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "formsOutput": Dict[str, FormEntryOutputTypeDef],
        "name": str,
        "originDomainId": str,
        "originProjectId": str,
        "owningProjectId": str,
        "revision": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAssetTypeOutputTypeDef = TypedDict(
    "GetAssetTypeOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "formsOutput": Dict[str, FormEntryOutputTypeDef],
        "name": str,
        "originDomainId": str,
        "originProjectId": str,
        "owningProjectId": str,
        "revision": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LineageNodeTypeItemTypeDef = TypedDict(
    "LineageNodeTypeItemTypeDef",
    {
        "domainId": str,
        "formsOutput": Dict[str, FormEntryOutputTypeDef],
        "revision": str,
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "description": NotRequired[str],
        "name": NotRequired[str],
        "updatedAt": NotRequired[datetime],
        "updatedBy": NotRequired[str],
    },
)
PostLineageEventInputRequestTypeDef = TypedDict(
    "PostLineageEventInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "event": BlobTypeDef,
        "clientToken": NotRequired[str],
    },
)
PredictionConfigurationTypeDef = TypedDict(
    "PredictionConfigurationTypeDef",
    {
        "businessNameGeneration": NotRequired[BusinessNameGenerationConfigurationTypeDef],
    },
)
ProvisioningPropertiesTypeDef = TypedDict(
    "ProvisioningPropertiesTypeDef",
    {
        "cloudFormation": NotRequired[CloudFormationPropertiesTypeDef],
    },
)
ColumnFilterConfigurationUnionTypeDef = Union[
    ColumnFilterConfigurationTypeDef, ColumnFilterConfigurationOutputTypeDef
]
ConfigurableEnvironmentActionTypeDef = TypedDict(
    "ConfigurableEnvironmentActionTypeDef",
    {
        "parameters": List[ConfigurableActionParameterTypeDef],
        "type": str,
        "auth": NotRequired[ConfigurableActionTypeAuthorizationType],
    },
)
CreateAssetTypeInputRequestTypeDef = TypedDict(
    "CreateAssetTypeInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "formsInput": Mapping[str, FormEntryInputTypeDef],
        "name": str,
        "owningProjectIdentifier": str,
        "description": NotRequired[str],
    },
)
CreateDataProductOutputTypeDef = TypedDict(
    "CreateDataProductOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "firstRevisionCreatedAt": datetime,
        "firstRevisionCreatedBy": str,
        "formsOutput": List[FormOutputTypeDef],
        "glossaryTerms": List[str],
        "id": str,
        "items": List[DataProductItemOutputTypeDef],
        "name": str,
        "owningProjectId": str,
        "revision": str,
        "status": DataProductStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDataProductRevisionOutputTypeDef = TypedDict(
    "CreateDataProductRevisionOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "firstRevisionCreatedAt": datetime,
        "firstRevisionCreatedBy": str,
        "formsOutput": List[FormOutputTypeDef],
        "glossaryTerms": List[str],
        "id": str,
        "items": List[DataProductItemOutputTypeDef],
        "name": str,
        "owningProjectId": str,
        "revision": str,
        "status": DataProductStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDataProductOutputTypeDef = TypedDict(
    "GetDataProductOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "firstRevisionCreatedAt": datetime,
        "firstRevisionCreatedBy": str,
        "formsOutput": List[FormOutputTypeDef],
        "glossaryTerms": List[str],
        "id": str,
        "items": List[DataProductItemOutputTypeDef],
        "name": str,
        "owningProjectId": str,
        "revision": str,
        "status": DataProductStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDataProductRevisionInputRequestTypeDef = TypedDict(
    "CreateDataProductRevisionInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "name": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "formsInput": NotRequired[Sequence[FormInputTypeDef]],
        "glossaryTerms": NotRequired[Sequence[str]],
        "items": NotRequired[Sequence[DataProductItemTypeDef]],
    },
)
DataProductItemUnionTypeDef = Union[DataProductItemTypeDef, DataProductItemOutputTypeDef]
DataSourceRunActivityTypeDef = TypedDict(
    "DataSourceRunActivityTypeDef",
    {
        "createdAt": datetime,
        "dataAssetStatus": DataAssetActivityStatusType,
        "dataSourceRunId": str,
        "database": str,
        "projectId": str,
        "technicalName": str,
        "updatedAt": datetime,
        "dataAssetId": NotRequired[str],
        "errorMessage": NotRequired[DataSourceErrorMessageTypeDef],
        "technicalDescription": NotRequired[str],
    },
)
DataSourceSummaryTypeDef = TypedDict(
    "DataSourceSummaryTypeDef",
    {
        "dataSourceId": str,
        "domainId": str,
        "environmentId": str,
        "name": str,
        "status": DataSourceStatusType,
        "type": str,
        "createdAt": NotRequired[datetime],
        "enableSetting": NotRequired[EnableSettingType],
        "lastRunAssetCount": NotRequired[int],
        "lastRunAt": NotRequired[datetime],
        "lastRunErrorMessage": NotRequired[DataSourceErrorMessageTypeDef],
        "lastRunStatus": NotRequired[DataSourceRunStatusType],
        "schedule": NotRequired[ScheduleConfigurationTypeDef],
        "updatedAt": NotRequired[datetime],
    },
)
CreateDomainInputRequestTypeDef = TypedDict(
    "CreateDomainInputRequestTypeDef",
    {
        "domainExecutionRole": str,
        "name": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "kmsKeyIdentifier": NotRequired[str],
        "singleSignOn": NotRequired[SingleSignOnTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateDomainOutputTypeDef = TypedDict(
    "CreateDomainOutputTypeDef",
    {
        "arn": str,
        "description": str,
        "domainExecutionRole": str,
        "id": str,
        "kmsKeyIdentifier": str,
        "name": str,
        "portalUrl": str,
        "rootDomainUnitId": str,
        "singleSignOn": SingleSignOnTypeDef,
        "status": DomainStatusType,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDomainOutputTypeDef = TypedDict(
    "GetDomainOutputTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "description": str,
        "domainExecutionRole": str,
        "id": str,
        "kmsKeyIdentifier": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "portalUrl": str,
        "rootDomainUnitId": str,
        "singleSignOn": SingleSignOnTypeDef,
        "status": DomainStatusType,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDomainInputRequestTypeDef = TypedDict(
    "UpdateDomainInputRequestTypeDef",
    {
        "identifier": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "domainExecutionRole": NotRequired[str],
        "name": NotRequired[str],
        "singleSignOn": NotRequired[SingleSignOnTypeDef],
    },
)
UpdateDomainOutputTypeDef = TypedDict(
    "UpdateDomainOutputTypeDef",
    {
        "description": str,
        "domainExecutionRole": str,
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "rootDomainUnitId": str,
        "singleSignOn": SingleSignOnTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEnvironmentInputRequestTypeDef = TypedDict(
    "CreateEnvironmentInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentProfileIdentifier": str,
        "name": str,
        "projectIdentifier": str,
        "description": NotRequired[str],
        "environmentAccountIdentifier": NotRequired[str],
        "environmentAccountRegion": NotRequired[str],
        "environmentBlueprintIdentifier": NotRequired[str],
        "glossaryTerms": NotRequired[Sequence[str]],
        "userParameters": NotRequired[Sequence[EnvironmentParameterTypeDef]],
    },
)
CreateEnvironmentProfileInputRequestTypeDef = TypedDict(
    "CreateEnvironmentProfileInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentBlueprintIdentifier": str,
        "name": str,
        "projectIdentifier": str,
        "awsAccountId": NotRequired[str],
        "awsAccountRegion": NotRequired[str],
        "description": NotRequired[str],
        "userParameters": NotRequired[Sequence[EnvironmentParameterTypeDef]],
    },
)
UpdateEnvironmentProfileInputRequestTypeDef = TypedDict(
    "UpdateEnvironmentProfileInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "awsAccountId": NotRequired[str],
        "awsAccountRegion": NotRequired[str],
        "description": NotRequired[str],
        "name": NotRequired[str],
        "userParameters": NotRequired[Sequence[EnvironmentParameterTypeDef]],
    },
)
CreateEnvironmentProfileOutputTypeDef = TypedDict(
    "CreateEnvironmentProfileOutputTypeDef",
    {
        "awsAccountId": str,
        "awsAccountRegion": str,
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "environmentBlueprintId": str,
        "id": str,
        "name": str,
        "projectId": str,
        "updatedAt": datetime,
        "userParameters": List[CustomParameterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEnvironmentProfileOutputTypeDef = TypedDict(
    "GetEnvironmentProfileOutputTypeDef",
    {
        "awsAccountId": str,
        "awsAccountRegion": str,
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "environmentBlueprintId": str,
        "id": str,
        "name": str,
        "projectId": str,
        "updatedAt": datetime,
        "userParameters": List[CustomParameterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEnvironmentProfileOutputTypeDef = TypedDict(
    "UpdateEnvironmentProfileOutputTypeDef",
    {
        "awsAccountId": str,
        "awsAccountRegion": str,
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "environmentBlueprintId": str,
        "id": str,
        "name": str,
        "projectId": str,
        "updatedAt": datetime,
        "userParameters": List[CustomParameterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFormTypeInputRequestTypeDef = TypedDict(
    "CreateFormTypeInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "model": ModelTypeDef,
        "name": str,
        "owningProjectIdentifier": str,
        "description": NotRequired[str],
        "status": NotRequired[FormTypeStatusType],
    },
)
CreateGlossaryTermInputRequestTypeDef = TypedDict(
    "CreateGlossaryTermInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "glossaryIdentifier": str,
        "name": str,
        "clientToken": NotRequired[str],
        "longDescription": NotRequired[str],
        "shortDescription": NotRequired[str],
        "status": NotRequired[GlossaryTermStatusType],
        "termRelations": NotRequired[TermRelationsTypeDef],
    },
)
UpdateGlossaryTermInputRequestTypeDef = TypedDict(
    "UpdateGlossaryTermInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "glossaryIdentifier": NotRequired[str],
        "longDescription": NotRequired[str],
        "name": NotRequired[str],
        "shortDescription": NotRequired[str],
        "status": NotRequired[GlossaryTermStatusType],
        "termRelations": NotRequired[TermRelationsTypeDef],
    },
)
CreateGlossaryTermOutputTypeDef = TypedDict(
    "CreateGlossaryTermOutputTypeDef",
    {
        "domainId": str,
        "glossaryId": str,
        "id": str,
        "longDescription": str,
        "name": str,
        "shortDescription": str,
        "status": GlossaryTermStatusType,
        "termRelations": TermRelationsOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetGlossaryTermOutputTypeDef = TypedDict(
    "GetGlossaryTermOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "glossaryId": str,
        "id": str,
        "longDescription": str,
        "name": str,
        "shortDescription": str,
        "status": GlossaryTermStatusType,
        "termRelations": TermRelationsOutputTypeDef,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GlossaryTermItemTypeDef = TypedDict(
    "GlossaryTermItemTypeDef",
    {
        "domainId": str,
        "glossaryId": str,
        "id": str,
        "name": str,
        "status": GlossaryTermStatusType,
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "longDescription": NotRequired[str],
        "shortDescription": NotRequired[str],
        "termRelations": NotRequired[TermRelationsOutputTypeDef],
        "updatedAt": NotRequired[datetime],
        "updatedBy": NotRequired[str],
    },
)
UpdateGlossaryTermOutputTypeDef = TypedDict(
    "UpdateGlossaryTermOutputTypeDef",
    {
        "domainId": str,
        "glossaryId": str,
        "id": str,
        "longDescription": str,
        "name": str,
        "shortDescription": str,
        "status": GlossaryTermStatusType,
        "termRelations": TermRelationsOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProjectMembershipInputRequestTypeDef = TypedDict(
    "CreateProjectMembershipInputRequestTypeDef",
    {
        "designation": UserDesignationType,
        "domainIdentifier": str,
        "member": MemberTypeDef,
        "projectIdentifier": str,
    },
)
DeleteProjectMembershipInputRequestTypeDef = TypedDict(
    "DeleteProjectMembershipInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "member": MemberTypeDef,
        "projectIdentifier": str,
    },
)
CreateProjectOutputTypeDef = TypedDict(
    "CreateProjectOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "domainUnitId": str,
        "failureReasons": List[ProjectDeletionErrorTypeDef],
        "glossaryTerms": List[str],
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "projectStatus": ProjectStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetProjectOutputTypeDef = TypedDict(
    "GetProjectOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "domainUnitId": str,
        "failureReasons": List[ProjectDeletionErrorTypeDef],
        "glossaryTerms": List[str],
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "projectStatus": ProjectStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProjectSummaryTypeDef = TypedDict(
    "ProjectSummaryTypeDef",
    {
        "createdBy": str,
        "domainId": str,
        "id": str,
        "name": str,
        "createdAt": NotRequired[datetime],
        "description": NotRequired[str],
        "domainUnitId": NotRequired[str],
        "failureReasons": NotRequired[List[ProjectDeletionErrorTypeDef]],
        "projectStatus": NotRequired[ProjectStatusType],
        "updatedAt": NotRequired[datetime],
    },
)
UpdateProjectOutputTypeDef = TypedDict(
    "UpdateProjectOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "domainUnitId": str,
        "failureReasons": List[ProjectDeletionErrorTypeDef],
        "glossaryTerms": List[str],
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "projectStatus": ProjectStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSubscriptionTargetInputRequestTypeDef = TypedDict(
    "CreateSubscriptionTargetInputRequestTypeDef",
    {
        "applicableAssetTypes": Sequence[str],
        "authorizedPrincipals": Sequence[str],
        "domainIdentifier": str,
        "environmentIdentifier": str,
        "manageAccessRole": str,
        "name": str,
        "subscriptionTargetConfig": Sequence[SubscriptionTargetFormTypeDef],
        "type": str,
        "clientToken": NotRequired[str],
        "provider": NotRequired[str],
    },
)
CreateSubscriptionTargetOutputTypeDef = TypedDict(
    "CreateSubscriptionTargetOutputTypeDef",
    {
        "applicableAssetTypes": List[str],
        "authorizedPrincipals": List[str],
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "environmentId": str,
        "id": str,
        "manageAccessRole": str,
        "name": str,
        "projectId": str,
        "provider": str,
        "subscriptionTargetConfig": List[SubscriptionTargetFormTypeDef],
        "type": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSubscriptionTargetOutputTypeDef = TypedDict(
    "GetSubscriptionTargetOutputTypeDef",
    {
        "applicableAssetTypes": List[str],
        "authorizedPrincipals": List[str],
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "environmentId": str,
        "id": str,
        "manageAccessRole": str,
        "name": str,
        "projectId": str,
        "provider": str,
        "subscriptionTargetConfig": List[SubscriptionTargetFormTypeDef],
        "type": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SubscriptionTargetSummaryTypeDef = TypedDict(
    "SubscriptionTargetSummaryTypeDef",
    {
        "applicableAssetTypes": List[str],
        "authorizedPrincipals": List[str],
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "environmentId": str,
        "id": str,
        "manageAccessRole": str,
        "name": str,
        "projectId": str,
        "provider": str,
        "subscriptionTargetConfig": List[SubscriptionTargetFormTypeDef],
        "type": str,
        "updatedAt": NotRequired[datetime],
        "updatedBy": NotRequired[str],
    },
)
UpdateSubscriptionTargetInputRequestTypeDef = TypedDict(
    "UpdateSubscriptionTargetInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentIdentifier": str,
        "identifier": str,
        "applicableAssetTypes": NotRequired[Sequence[str]],
        "authorizedPrincipals": NotRequired[Sequence[str]],
        "manageAccessRole": NotRequired[str],
        "name": NotRequired[str],
        "provider": NotRequired[str],
        "subscriptionTargetConfig": NotRequired[Sequence[SubscriptionTargetFormTypeDef]],
    },
)
UpdateSubscriptionTargetOutputTypeDef = TypedDict(
    "UpdateSubscriptionTargetOutputTypeDef",
    {
        "applicableAssetTypes": List[str],
        "authorizedPrincipals": List[str],
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "environmentId": str,
        "id": str,
        "manageAccessRole": str,
        "name": str,
        "projectId": str,
        "provider": str,
        "subscriptionTargetConfig": List[SubscriptionTargetFormTypeDef],
        "type": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDataProductRevisionsOutputTypeDef = TypedDict(
    "ListDataProductRevisionsOutputTypeDef",
    {
        "items": List[DataProductRevisionTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DataSourceRunSummaryTypeDef = TypedDict(
    "DataSourceRunSummaryTypeDef",
    {
        "createdAt": datetime,
        "dataSourceId": str,
        "id": str,
        "projectId": str,
        "status": DataSourceRunStatusType,
        "type": DataSourceRunTypeType,
        "updatedAt": datetime,
        "errorMessage": NotRequired[DataSourceErrorMessageTypeDef],
        "runStatisticsForAssets": NotRequired[RunStatisticsForAssetsTypeDef],
        "startedAt": NotRequired[datetime],
        "stoppedAt": NotRequired[datetime],
    },
)
GetDataSourceRunOutputTypeDef = TypedDict(
    "GetDataSourceRunOutputTypeDef",
    {
        "createdAt": datetime,
        "dataSourceConfigurationSnapshot": str,
        "dataSourceId": str,
        "domainId": str,
        "errorMessage": DataSourceErrorMessageTypeDef,
        "id": str,
        "projectId": str,
        "runStatisticsForAssets": RunStatisticsForAssetsTypeDef,
        "startedAt": datetime,
        "status": DataSourceRunStatusType,
        "stoppedAt": datetime,
        "type": DataSourceRunTypeType,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartDataSourceRunOutputTypeDef = TypedDict(
    "StartDataSourceRunOutputTypeDef",
    {
        "createdAt": datetime,
        "dataSourceConfigurationSnapshot": str,
        "dataSourceId": str,
        "domainId": str,
        "errorMessage": DataSourceErrorMessageTypeDef,
        "id": str,
        "projectId": str,
        "runStatisticsForAssets": RunStatisticsForAssetsTypeDef,
        "startedAt": datetime,
        "status": DataSourceRunStatusType,
        "stoppedAt": datetime,
        "type": DataSourceRunTypeType,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "deploymentId": NotRequired[str],
        "deploymentStatus": NotRequired[DeploymentStatusType],
        "deploymentType": NotRequired[DeploymentTypeType],
        "failureReason": NotRequired[EnvironmentErrorTypeDef],
        "isDeploymentComplete": NotRequired[bool],
        "messages": NotRequired[List[str]],
    },
)
ListDomainsOutputTypeDef = TypedDict(
    "ListDomainsOutputTypeDef",
    {
        "items": List[DomainSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProjectGrantFilterTypeDef = TypedDict(
    "ProjectGrantFilterTypeDef",
    {
        "domainUnitFilter": NotRequired[DomainUnitFilterForProjectTypeDef],
    },
)
DomainUnitPolicyGrantPrincipalOutputTypeDef = TypedDict(
    "DomainUnitPolicyGrantPrincipalOutputTypeDef",
    {
        "domainUnitDesignation": Literal["OWNER"],
        "domainUnitGrantFilter": NotRequired[DomainUnitGrantFilterOutputTypeDef],
        "domainUnitIdentifier": NotRequired[str],
    },
)
DomainUnitGrantFilterUnionTypeDef = Union[
    DomainUnitGrantFilterTypeDef, DomainUnitGrantFilterOutputTypeDef
]
DomainUnitOwnerPropertiesTypeDef = TypedDict(
    "DomainUnitOwnerPropertiesTypeDef",
    {
        "group": NotRequired[DomainUnitGroupPropertiesTypeDef],
        "user": NotRequired[DomainUnitUserPropertiesTypeDef],
    },
)
ListDomainUnitsForParentOutputTypeDef = TypedDict(
    "ListDomainUnitsForParentOutputTypeDef",
    {
        "items": List[DomainUnitSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEnvironmentProfilesOutputTypeDef = TypedDict(
    "ListEnvironmentProfilesOutputTypeDef",
    {
        "items": List[EnvironmentProfileSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEnvironmentsOutputTypeDef = TypedDict(
    "ListEnvironmentsOutputTypeDef",
    {
        "items": List[EnvironmentSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SubscribedAssetTypeDef = TypedDict(
    "SubscribedAssetTypeDef",
    {
        "assetId": str,
        "assetRevision": str,
        "status": SubscriptionGrantStatusType,
        "assetScope": NotRequired[AssetScopeTypeDef],
        "failureCause": NotRequired[FailureCauseTypeDef],
        "failureTimestamp": NotRequired[datetime],
        "grantedTimestamp": NotRequired[datetime],
        "targetName": NotRequired[str],
    },
)
UpdateSubscriptionGrantStatusInputRequestTypeDef = TypedDict(
    "UpdateSubscriptionGrantStatusInputRequestTypeDef",
    {
        "assetIdentifier": str,
        "domainIdentifier": str,
        "identifier": str,
        "status": SubscriptionGrantStatusType,
        "failureCause": NotRequired[FailureCauseTypeDef],
        "targetName": NotRequired[str],
    },
)
FilterClausePaginatorTypeDef = TypedDict(
    "FilterClausePaginatorTypeDef",
    {
        "and": NotRequired[Sequence[Mapping[str, Any]]],
        "filter": NotRequired[FilterTypeDef],
        "or": NotRequired[Sequence[Mapping[str, Any]]],
    },
)
FilterClauseTypeDef = TypedDict(
    "FilterClauseTypeDef",
    {
        "and": NotRequired[Sequence[Mapping[str, Any]]],
        "filter": NotRequired[FilterTypeDef],
        "or": NotRequired[Sequence[Mapping[str, Any]]],
    },
)
RelationalFilterConfigurationOutputTypeDef = TypedDict(
    "RelationalFilterConfigurationOutputTypeDef",
    {
        "databaseName": str,
        "filterExpressions": NotRequired[List[FilterExpressionTypeDef]],
        "schemaName": NotRequired[str],
    },
)
RelationalFilterConfigurationTypeDef = TypedDict(
    "RelationalFilterConfigurationTypeDef",
    {
        "databaseName": str,
        "filterExpressions": NotRequired[Sequence[FilterExpressionTypeDef]],
        "schemaName": NotRequired[str],
    },
)
FormTypeDataTypeDef = TypedDict(
    "FormTypeDataTypeDef",
    {
        "domainId": str,
        "name": str,
        "revision": str,
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "description": NotRequired[str],
        "imports": NotRequired[List[ImportTypeDef]],
        "model": NotRequired[ModelTypeDef],
        "originDomainId": NotRequired[str],
        "originProjectId": NotRequired[str],
        "owningProjectId": NotRequired[str],
        "status": NotRequired[FormTypeStatusType],
    },
)
GetFormTypeOutputTypeDef = TypedDict(
    "GetFormTypeOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "imports": List[ImportTypeDef],
        "model": ModelTypeDef,
        "name": str,
        "originDomainId": str,
        "originProjectId": str,
        "owningProjectId": str,
        "revision": str,
        "status": FormTypeStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLineageNodeInputRequestTypeDef = TypedDict(
    "GetLineageNodeInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "eventTimestamp": NotRequired[TimestampTypeDef],
    },
)
ListLineageNodeHistoryInputRequestTypeDef = TypedDict(
    "ListLineageNodeHistoryInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "direction": NotRequired[EdgeDirectionType],
        "eventTimestampGTE": NotRequired[TimestampTypeDef],
        "eventTimestampLTE": NotRequired[TimestampTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortOrder": NotRequired[SortOrderType],
    },
)
ListNotificationsInputRequestTypeDef = TypedDict(
    "ListNotificationsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "type": NotificationTypeType,
        "afterTimestamp": NotRequired[TimestampTypeDef],
        "beforeTimestamp": NotRequired[TimestampTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "subjects": NotRequired[Sequence[str]],
        "taskStatus": NotRequired[TaskStatusType],
    },
)
ListTimeSeriesDataPointsInputRequestTypeDef = TypedDict(
    "ListTimeSeriesDataPointsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "entityIdentifier": str,
        "entityType": TimeSeriesEntityTypeType,
        "formName": str,
        "endedAt": NotRequired[TimestampTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "startedAt": NotRequired[TimestampTypeDef],
    },
)
TimeSeriesDataPointFormInputTypeDef = TypedDict(
    "TimeSeriesDataPointFormInputTypeDef",
    {
        "formName": str,
        "timestamp": TimestampTypeDef,
        "typeIdentifier": str,
        "content": NotRequired[str],
        "typeRevision": NotRequired[str],
    },
)
GetLineageNodeOutputTypeDef = TypedDict(
    "GetLineageNodeOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "downstreamNodes": List[LineageNodeReferenceTypeDef],
        "eventTimestamp": datetime,
        "formsOutput": List[FormOutputTypeDef],
        "id": str,
        "name": str,
        "sourceIdentifier": str,
        "typeName": str,
        "typeRevision": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "upstreamNodes": List[LineageNodeReferenceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMetadataGenerationRunOutputTypeDef = TypedDict(
    "GetMetadataGenerationRunOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "id": str,
        "owningProjectId": str,
        "status": MetadataGenerationRunStatusType,
        "target": MetadataGenerationRunTargetTypeDef,
        "type": Literal["BUSINESS_DESCRIPTIONS"],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MetadataGenerationRunItemTypeDef = TypedDict(
    "MetadataGenerationRunItemTypeDef",
    {
        "domainId": str,
        "id": str,
        "owningProjectId": str,
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "status": NotRequired[MetadataGenerationRunStatusType],
        "target": NotRequired[MetadataGenerationRunTargetTypeDef],
        "type": NotRequired[Literal["BUSINESS_DESCRIPTIONS"]],
    },
)
StartMetadataGenerationRunInputRequestTypeDef = TypedDict(
    "StartMetadataGenerationRunInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "owningProjectIdentifier": str,
        "target": MetadataGenerationRunTargetTypeDef,
        "type": Literal["BUSINESS_DESCRIPTIONS"],
        "clientToken": NotRequired[str],
    },
)
GetTimeSeriesDataPointOutputTypeDef = TypedDict(
    "GetTimeSeriesDataPointOutputTypeDef",
    {
        "domainId": str,
        "entityId": str,
        "entityType": TimeSeriesEntityTypeType,
        "form": TimeSeriesDataPointFormOutputTypeDef,
        "formName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PostTimeSeriesDataPointsOutputTypeDef = TypedDict(
    "PostTimeSeriesDataPointsOutputTypeDef",
    {
        "domainId": str,
        "entityId": str,
        "entityType": TimeSeriesEntityTypeType,
        "forms": List[TimeSeriesDataPointFormOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GlueSelfGrantStatusOutputTypeDef = TypedDict(
    "GlueSelfGrantStatusOutputTypeDef",
    {
        "selfGrantStatusDetails": List[SelfGrantStatusDetailTypeDef],
    },
)
RedshiftSelfGrantStatusOutputTypeDef = TypedDict(
    "RedshiftSelfGrantStatusOutputTypeDef",
    {
        "selfGrantStatusDetails": List[SelfGrantStatusDetailTypeDef],
    },
)
GrantedEntityInputTypeDef = TypedDict(
    "GrantedEntityInputTypeDef",
    {
        "listing": NotRequired[ListingRevisionInputTypeDef],
    },
)
GrantedEntityTypeDef = TypedDict(
    "GrantedEntityTypeDef",
    {
        "listing": NotRequired[ListingRevisionTypeDef],
    },
)
SearchGroupProfilesOutputTypeDef = TypedDict(
    "SearchGroupProfilesOutputTypeDef",
    {
        "items": List[GroupProfileSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InExpressionUnionTypeDef = Union[InExpressionTypeDef, InExpressionOutputTypeDef]
ProvisioningConfigurationOutputTypeDef = TypedDict(
    "ProvisioningConfigurationOutputTypeDef",
    {
        "lakeFormationConfiguration": NotRequired[LakeFormationConfigurationOutputTypeDef],
    },
)
LakeFormationConfigurationUnionTypeDef = Union[
    LakeFormationConfigurationTypeDef, LakeFormationConfigurationOutputTypeDef
]
ListLineageNodeHistoryOutputTypeDef = TypedDict(
    "ListLineageNodeHistoryOutputTypeDef",
    {
        "nextToken": str,
        "nodes": List[LineageNodeSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssetFiltersInputListAssetFiltersPaginateTypeDef = TypedDict(
    "ListAssetFiltersInputListAssetFiltersPaginateTypeDef",
    {
        "assetIdentifier": str,
        "domainIdentifier": str,
        "status": NotRequired[FilterStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAssetRevisionsInputListAssetRevisionsPaginateTypeDef = TypedDict(
    "ListAssetRevisionsInputListAssetRevisionsPaginateTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDataProductRevisionsInputListDataProductRevisionsPaginateTypeDef = TypedDict(
    "ListDataProductRevisionsInputListDataProductRevisionsPaginateTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDataSourceRunActivitiesInputListDataSourceRunActivitiesPaginateTypeDef = TypedDict(
    "ListDataSourceRunActivitiesInputListDataSourceRunActivitiesPaginateTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "status": NotRequired[DataAssetActivityStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDataSourceRunsInputListDataSourceRunsPaginateTypeDef = TypedDict(
    "ListDataSourceRunsInputListDataSourceRunsPaginateTypeDef",
    {
        "dataSourceIdentifier": str,
        "domainIdentifier": str,
        "status": NotRequired[DataSourceRunStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDataSourcesInputListDataSourcesPaginateTypeDef = TypedDict(
    "ListDataSourcesInputListDataSourcesPaginateTypeDef",
    {
        "domainIdentifier": str,
        "projectIdentifier": str,
        "environmentIdentifier": NotRequired[str],
        "name": NotRequired[str],
        "status": NotRequired[DataSourceStatusType],
        "type": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDomainUnitsForParentInputListDomainUnitsForParentPaginateTypeDef = TypedDict(
    "ListDomainUnitsForParentInputListDomainUnitsForParentPaginateTypeDef",
    {
        "domainIdentifier": str,
        "parentDomainUnitIdentifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDomainsInputListDomainsPaginateTypeDef = TypedDict(
    "ListDomainsInputListDomainsPaginateTypeDef",
    {
        "status": NotRequired[DomainStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEntityOwnersInputListEntityOwnersPaginateTypeDef = TypedDict(
    "ListEntityOwnersInputListEntityOwnersPaginateTypeDef",
    {
        "domainIdentifier": str,
        "entityIdentifier": str,
        "entityType": Literal["DOMAIN_UNIT"],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEnvironmentActionsInputListEnvironmentActionsPaginateTypeDef = TypedDict(
    "ListEnvironmentActionsInputListEnvironmentActionsPaginateTypeDef",
    {
        "domainIdentifier": str,
        "environmentIdentifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEnvironmentBlueprintConfigurationsInputListEnvironmentBlueprintConfigurationsPaginateTypeDef = TypedDict(
    "ListEnvironmentBlueprintConfigurationsInputListEnvironmentBlueprintConfigurationsPaginateTypeDef",
    {
        "domainIdentifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEnvironmentBlueprintsInputListEnvironmentBlueprintsPaginateTypeDef = TypedDict(
    "ListEnvironmentBlueprintsInputListEnvironmentBlueprintsPaginateTypeDef",
    {
        "domainIdentifier": str,
        "managed": NotRequired[bool],
        "name": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEnvironmentProfilesInputListEnvironmentProfilesPaginateTypeDef = TypedDict(
    "ListEnvironmentProfilesInputListEnvironmentProfilesPaginateTypeDef",
    {
        "domainIdentifier": str,
        "awsAccountId": NotRequired[str],
        "awsAccountRegion": NotRequired[str],
        "environmentBlueprintIdentifier": NotRequired[str],
        "name": NotRequired[str],
        "projectIdentifier": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEnvironmentsInputListEnvironmentsPaginateTypeDef = TypedDict(
    "ListEnvironmentsInputListEnvironmentsPaginateTypeDef",
    {
        "domainIdentifier": str,
        "projectIdentifier": str,
        "awsAccountId": NotRequired[str],
        "awsAccountRegion": NotRequired[str],
        "environmentBlueprintIdentifier": NotRequired[str],
        "environmentProfileIdentifier": NotRequired[str],
        "name": NotRequired[str],
        "provider": NotRequired[str],
        "status": NotRequired[EnvironmentStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListLineageNodeHistoryInputListLineageNodeHistoryPaginateTypeDef = TypedDict(
    "ListLineageNodeHistoryInputListLineageNodeHistoryPaginateTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "direction": NotRequired[EdgeDirectionType],
        "eventTimestampGTE": NotRequired[TimestampTypeDef],
        "eventTimestampLTE": NotRequired[TimestampTypeDef],
        "sortOrder": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMetadataGenerationRunsInputListMetadataGenerationRunsPaginateTypeDef = TypedDict(
    "ListMetadataGenerationRunsInputListMetadataGenerationRunsPaginateTypeDef",
    {
        "domainIdentifier": str,
        "status": NotRequired[MetadataGenerationRunStatusType],
        "type": NotRequired[Literal["BUSINESS_DESCRIPTIONS"]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListNotificationsInputListNotificationsPaginateTypeDef = TypedDict(
    "ListNotificationsInputListNotificationsPaginateTypeDef",
    {
        "domainIdentifier": str,
        "type": NotificationTypeType,
        "afterTimestamp": NotRequired[TimestampTypeDef],
        "beforeTimestamp": NotRequired[TimestampTypeDef],
        "subjects": NotRequired[Sequence[str]],
        "taskStatus": NotRequired[TaskStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPolicyGrantsInputListPolicyGrantsPaginateTypeDef = TypedDict(
    "ListPolicyGrantsInputListPolicyGrantsPaginateTypeDef",
    {
        "domainIdentifier": str,
        "entityIdentifier": str,
        "entityType": TargetEntityTypeType,
        "policyType": ManagedPolicyTypeType,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProjectMembershipsInputListProjectMembershipsPaginateTypeDef = TypedDict(
    "ListProjectMembershipsInputListProjectMembershipsPaginateTypeDef",
    {
        "domainIdentifier": str,
        "projectIdentifier": str,
        "sortBy": NotRequired[Literal["NAME"]],
        "sortOrder": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProjectsInputListProjectsPaginateTypeDef = TypedDict(
    "ListProjectsInputListProjectsPaginateTypeDef",
    {
        "domainIdentifier": str,
        "groupIdentifier": NotRequired[str],
        "name": NotRequired[str],
        "userIdentifier": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSubscriptionGrantsInputListSubscriptionGrantsPaginateTypeDef = TypedDict(
    "ListSubscriptionGrantsInputListSubscriptionGrantsPaginateTypeDef",
    {
        "domainIdentifier": str,
        "environmentId": NotRequired[str],
        "owningProjectId": NotRequired[str],
        "sortBy": NotRequired[SortKeyType],
        "sortOrder": NotRequired[SortOrderType],
        "subscribedListingId": NotRequired[str],
        "subscriptionId": NotRequired[str],
        "subscriptionTargetId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSubscriptionRequestsInputListSubscriptionRequestsPaginateTypeDef = TypedDict(
    "ListSubscriptionRequestsInputListSubscriptionRequestsPaginateTypeDef",
    {
        "domainIdentifier": str,
        "approverProjectId": NotRequired[str],
        "owningProjectId": NotRequired[str],
        "sortBy": NotRequired[SortKeyType],
        "sortOrder": NotRequired[SortOrderType],
        "status": NotRequired[SubscriptionRequestStatusType],
        "subscribedListingId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSubscriptionTargetsInputListSubscriptionTargetsPaginateTypeDef = TypedDict(
    "ListSubscriptionTargetsInputListSubscriptionTargetsPaginateTypeDef",
    {
        "domainIdentifier": str,
        "environmentIdentifier": str,
        "sortBy": NotRequired[SortKeyType],
        "sortOrder": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSubscriptionsInputListSubscriptionsPaginateTypeDef = TypedDict(
    "ListSubscriptionsInputListSubscriptionsPaginateTypeDef",
    {
        "domainIdentifier": str,
        "approverProjectId": NotRequired[str],
        "owningProjectId": NotRequired[str],
        "sortBy": NotRequired[SortKeyType],
        "sortOrder": NotRequired[SortOrderType],
        "status": NotRequired[SubscriptionStatusType],
        "subscribedListingId": NotRequired[str],
        "subscriptionRequestIdentifier": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTimeSeriesDataPointsInputListTimeSeriesDataPointsPaginateTypeDef = TypedDict(
    "ListTimeSeriesDataPointsInputListTimeSeriesDataPointsPaginateTypeDef",
    {
        "domainIdentifier": str,
        "entityIdentifier": str,
        "entityType": TimeSeriesEntityTypeType,
        "formName": str,
        "endedAt": NotRequired[TimestampTypeDef],
        "startedAt": NotRequired[TimestampTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchGroupProfilesInputSearchGroupProfilesPaginateTypeDef = TypedDict(
    "SearchGroupProfilesInputSearchGroupProfilesPaginateTypeDef",
    {
        "domainIdentifier": str,
        "groupType": GroupSearchTypeType,
        "searchText": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchUserProfilesInputSearchUserProfilesPaginateTypeDef = TypedDict(
    "SearchUserProfilesInputSearchUserProfilesPaginateTypeDef",
    {
        "domainIdentifier": str,
        "userType": UserSearchTypeType,
        "searchText": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
MemberDetailsTypeDef = TypedDict(
    "MemberDetailsTypeDef",
    {
        "group": NotRequired[GroupDetailsTypeDef],
        "user": NotRequired[UserDetailsTypeDef],
    },
)
NotInExpressionUnionTypeDef = Union[NotInExpressionTypeDef, NotInExpressionOutputTypeDef]
RowFilterExpressionOutputTypeDef = TypedDict(
    "RowFilterExpressionOutputTypeDef",
    {
        "equalTo": NotRequired[EqualToExpressionTypeDef],
        "greaterThan": NotRequired[GreaterThanExpressionTypeDef],
        "greaterThanOrEqualTo": NotRequired[GreaterThanOrEqualToExpressionTypeDef],
        "in": NotRequired[InExpressionOutputTypeDef],
        "isNotNull": NotRequired[IsNotNullExpressionTypeDef],
        "isNull": NotRequired[IsNullExpressionTypeDef],
        "lessThan": NotRequired[LessThanExpressionTypeDef],
        "lessThanOrEqualTo": NotRequired[LessThanOrEqualToExpressionTypeDef],
        "like": NotRequired[LikeExpressionTypeDef],
        "notEqualTo": NotRequired[NotEqualToExpressionTypeDef],
        "notIn": NotRequired[NotInExpressionOutputTypeDef],
        "notLike": NotRequired[NotLikeExpressionTypeDef],
    },
)
TopicTypeDef = TypedDict(
    "TopicTypeDef",
    {
        "resource": NotificationResourceTypeDef,
        "role": NotificationRoleType,
        "subject": str,
    },
)
PolicyGrantDetailOutputTypeDef = TypedDict(
    "PolicyGrantDetailOutputTypeDef",
    {
        "addToProjectMemberPool": NotRequired[AddToProjectMemberPoolPolicyGrantDetailTypeDef],
        "createAssetType": NotRequired[CreateAssetTypePolicyGrantDetailTypeDef],
        "createDomainUnit": NotRequired[CreateDomainUnitPolicyGrantDetailTypeDef],
        "createEnvironment": NotRequired[Dict[str, Any]],
        "createEnvironmentProfile": NotRequired[CreateEnvironmentProfilePolicyGrantDetailTypeDef],
        "createFormType": NotRequired[CreateFormTypePolicyGrantDetailTypeDef],
        "createGlossary": NotRequired[CreateGlossaryPolicyGrantDetailTypeDef],
        "createProject": NotRequired[CreateProjectPolicyGrantDetailTypeDef],
        "delegateCreateEnvironmentProfile": NotRequired[Dict[str, Any]],
        "overrideDomainUnitOwners": NotRequired[OverrideDomainUnitOwnersPolicyGrantDetailTypeDef],
        "overrideProjectOwners": NotRequired[OverrideProjectOwnersPolicyGrantDetailTypeDef],
    },
)
PolicyGrantDetailTypeDef = TypedDict(
    "PolicyGrantDetailTypeDef",
    {
        "addToProjectMemberPool": NotRequired[AddToProjectMemberPoolPolicyGrantDetailTypeDef],
        "createAssetType": NotRequired[CreateAssetTypePolicyGrantDetailTypeDef],
        "createDomainUnit": NotRequired[CreateDomainUnitPolicyGrantDetailTypeDef],
        "createEnvironment": NotRequired[Mapping[str, Any]],
        "createEnvironmentProfile": NotRequired[CreateEnvironmentProfilePolicyGrantDetailTypeDef],
        "createFormType": NotRequired[CreateFormTypePolicyGrantDetailTypeDef],
        "createGlossary": NotRequired[CreateGlossaryPolicyGrantDetailTypeDef],
        "createProject": NotRequired[CreateProjectPolicyGrantDetailTypeDef],
        "delegateCreateEnvironmentProfile": NotRequired[Mapping[str, Any]],
        "overrideDomainUnitOwners": NotRequired[OverrideDomainUnitOwnersPolicyGrantDetailTypeDef],
        "overrideProjectOwners": NotRequired[OverrideProjectOwnersPolicyGrantDetailTypeDef],
    },
)
OwnerPropertiesOutputTypeDef = TypedDict(
    "OwnerPropertiesOutputTypeDef",
    {
        "group": NotRequired[OwnerGroupPropertiesOutputTypeDef],
        "user": NotRequired[OwnerUserPropertiesOutputTypeDef],
    },
)
OwnerPropertiesTypeDef = TypedDict(
    "OwnerPropertiesTypeDef",
    {
        "group": NotRequired[OwnerGroupPropertiesTypeDef],
        "user": NotRequired[OwnerUserPropertiesTypeDef],
    },
)
RedshiftStorageTypeDef = TypedDict(
    "RedshiftStorageTypeDef",
    {
        "redshiftClusterSource": NotRequired[RedshiftClusterStorageTypeDef],
        "redshiftServerlessSource": NotRequired[RedshiftServerlessStorageTypeDef],
    },
)
RejectPredictionsInputRequestTypeDef = TypedDict(
    "RejectPredictionsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "clientToken": NotRequired[str],
        "rejectChoices": NotRequired[Sequence[RejectChoiceTypeDef]],
        "rejectRule": NotRequired[RejectRuleTypeDef],
        "revision": NotRequired[str],
    },
)
UserProfileDetailsTypeDef = TypedDict(
    "UserProfileDetailsTypeDef",
    {
        "iam": NotRequired[IamUserProfileDetailsTypeDef],
        "sso": NotRequired[SsoUserProfileDetailsTypeDef],
    },
)
SubscribedPrincipalInputTypeDef = TypedDict(
    "SubscribedPrincipalInputTypeDef",
    {
        "project": NotRequired[SubscribedProjectInputTypeDef],
    },
)
SubscribedPrincipalTypeDef = TypedDict(
    "SubscribedPrincipalTypeDef",
    {
        "project": NotRequired[SubscribedProjectTypeDef],
    },
)
UserPolicyGrantPrincipalUnionTypeDef = Union[
    UserPolicyGrantPrincipalTypeDef, UserPolicyGrantPrincipalOutputTypeDef
]
CreateEnvironmentActionInputRequestTypeDef = TypedDict(
    "CreateEnvironmentActionInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentIdentifier": str,
        "name": str,
        "parameters": ActionParametersTypeDef,
        "description": NotRequired[str],
    },
)
CreateEnvironmentActionOutputTypeDef = TypedDict(
    "CreateEnvironmentActionOutputTypeDef",
    {
        "description": str,
        "domainId": str,
        "environmentId": str,
        "id": str,
        "name": str,
        "parameters": ActionParametersTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnvironmentActionSummaryTypeDef = TypedDict(
    "EnvironmentActionSummaryTypeDef",
    {
        "domainId": str,
        "environmentId": str,
        "id": str,
        "name": str,
        "parameters": ActionParametersTypeDef,
        "description": NotRequired[str],
    },
)
GetEnvironmentActionOutputTypeDef = TypedDict(
    "GetEnvironmentActionOutputTypeDef",
    {
        "description": str,
        "domainId": str,
        "environmentId": str,
        "id": str,
        "name": str,
        "parameters": ActionParametersTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEnvironmentActionInputRequestTypeDef = TypedDict(
    "UpdateEnvironmentActionInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentIdentifier": str,
        "identifier": str,
        "description": NotRequired[str],
        "name": NotRequired[str],
        "parameters": NotRequired[ActionParametersTypeDef],
    },
)
UpdateEnvironmentActionOutputTypeDef = TypedDict(
    "UpdateEnvironmentActionOutputTypeDef",
    {
        "description": str,
        "domainId": str,
        "environmentId": str,
        "id": str,
        "name": str,
        "parameters": ActionParametersTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssetItemTypeDef = TypedDict(
    "AssetItemTypeDef",
    {
        "domainId": str,
        "identifier": str,
        "name": str,
        "owningProjectId": str,
        "typeIdentifier": str,
        "typeRevision": str,
        "additionalAttributes": NotRequired[AssetItemAdditionalAttributesTypeDef],
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "description": NotRequired[str],
        "externalIdentifier": NotRequired[str],
        "firstRevisionCreatedAt": NotRequired[datetime],
        "firstRevisionCreatedBy": NotRequired[str],
        "glossaryTerms": NotRequired[List[str]],
    },
)
AssetListingItemTypeDef = TypedDict(
    "AssetListingItemTypeDef",
    {
        "additionalAttributes": NotRequired[AssetListingItemAdditionalAttributesTypeDef],
        "createdAt": NotRequired[datetime],
        "description": NotRequired[str],
        "entityId": NotRequired[str],
        "entityRevision": NotRequired[str],
        "entityType": NotRequired[str],
        "glossaryTerms": NotRequired[List[DetailedGlossaryTermTypeDef]],
        "listingCreatedBy": NotRequired[str],
        "listingId": NotRequired[str],
        "listingRevision": NotRequired[str],
        "listingUpdatedBy": NotRequired[str],
        "name": NotRequired[str],
        "owningProjectId": NotRequired[str],
    },
)
DataProductListingItemTypeDef = TypedDict(
    "DataProductListingItemTypeDef",
    {
        "additionalAttributes": NotRequired[DataProductListingItemAdditionalAttributesTypeDef],
        "createdAt": NotRequired[datetime],
        "description": NotRequired[str],
        "entityId": NotRequired[str],
        "entityRevision": NotRequired[str],
        "glossaryTerms": NotRequired[List[DetailedGlossaryTermTypeDef]],
        "items": NotRequired[List[ListingSummaryItemTypeDef]],
        "listingCreatedBy": NotRequired[str],
        "listingId": NotRequired[str],
        "listingRevision": NotRequired[str],
        "listingUpdatedBy": NotRequired[str],
        "name": NotRequired[str],
        "owningProjectId": NotRequired[str],
    },
)
DataProductListingTypeDef = TypedDict(
    "DataProductListingTypeDef",
    {
        "createdAt": NotRequired[datetime],
        "dataProductId": NotRequired[str],
        "dataProductRevision": NotRequired[str],
        "forms": NotRequired[str],
        "glossaryTerms": NotRequired[List[DetailedGlossaryTermTypeDef]],
        "items": NotRequired[List[ListingSummaryTypeDef]],
        "owningProjectId": NotRequired[str],
    },
)
SubscribedListingItemTypeDef = TypedDict(
    "SubscribedListingItemTypeDef",
    {
        "assetListing": NotRequired[SubscribedAssetListingTypeDef],
        "productListing": NotRequired[SubscribedProductListingTypeDef],
    },
)
CreateAssetInputRequestTypeDef = TypedDict(
    "CreateAssetInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "name": str,
        "owningProjectIdentifier": str,
        "typeIdentifier": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "externalIdentifier": NotRequired[str],
        "formsInput": NotRequired[Sequence[FormInputTypeDef]],
        "glossaryTerms": NotRequired[Sequence[str]],
        "predictionConfiguration": NotRequired[PredictionConfigurationTypeDef],
        "typeRevision": NotRequired[str],
    },
)
CreateAssetOutputTypeDef = TypedDict(
    "CreateAssetOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "externalIdentifier": str,
        "firstRevisionCreatedAt": datetime,
        "firstRevisionCreatedBy": str,
        "formsOutput": List[FormOutputTypeDef],
        "glossaryTerms": List[str],
        "id": str,
        "latestTimeSeriesDataPointFormsOutput": List[TimeSeriesDataPointSummaryFormOutputTypeDef],
        "listing": AssetListingDetailsTypeDef,
        "name": str,
        "owningProjectId": str,
        "predictionConfiguration": PredictionConfigurationTypeDef,
        "readOnlyFormsOutput": List[FormOutputTypeDef],
        "revision": str,
        "typeIdentifier": str,
        "typeRevision": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAssetRevisionInputRequestTypeDef = TypedDict(
    "CreateAssetRevisionInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "name": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "formsInput": NotRequired[Sequence[FormInputTypeDef]],
        "glossaryTerms": NotRequired[Sequence[str]],
        "predictionConfiguration": NotRequired[PredictionConfigurationTypeDef],
        "typeRevision": NotRequired[str],
    },
)
CreateAssetRevisionOutputTypeDef = TypedDict(
    "CreateAssetRevisionOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "externalIdentifier": str,
        "firstRevisionCreatedAt": datetime,
        "firstRevisionCreatedBy": str,
        "formsOutput": List[FormOutputTypeDef],
        "glossaryTerms": List[str],
        "id": str,
        "latestTimeSeriesDataPointFormsOutput": List[TimeSeriesDataPointSummaryFormOutputTypeDef],
        "listing": AssetListingDetailsTypeDef,
        "name": str,
        "owningProjectId": str,
        "predictionConfiguration": PredictionConfigurationTypeDef,
        "readOnlyFormsOutput": List[FormOutputTypeDef],
        "revision": str,
        "typeIdentifier": str,
        "typeRevision": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnvironmentBlueprintSummaryTypeDef = TypedDict(
    "EnvironmentBlueprintSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "provider": str,
        "provisioningProperties": ProvisioningPropertiesTypeDef,
        "createdAt": NotRequired[datetime],
        "description": NotRequired[str],
        "updatedAt": NotRequired[datetime],
    },
)
GetEnvironmentBlueprintOutputTypeDef = TypedDict(
    "GetEnvironmentBlueprintOutputTypeDef",
    {
        "createdAt": datetime,
        "deploymentProperties": DeploymentPropertiesTypeDef,
        "description": str,
        "glossaryTerms": List[str],
        "id": str,
        "name": str,
        "provider": str,
        "provisioningProperties": ProvisioningPropertiesTypeDef,
        "updatedAt": datetime,
        "userParameters": List[CustomParameterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDataProductInputRequestTypeDef = TypedDict(
    "CreateDataProductInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "name": str,
        "owningProjectIdentifier": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "formsInput": NotRequired[Sequence[FormInputTypeDef]],
        "glossaryTerms": NotRequired[Sequence[str]],
        "items": NotRequired[Sequence[DataProductItemUnionTypeDef]],
    },
)
ListDataSourceRunActivitiesOutputTypeDef = TypedDict(
    "ListDataSourceRunActivitiesOutputTypeDef",
    {
        "items": List[DataSourceRunActivityTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDataSourcesOutputTypeDef = TypedDict(
    "ListDataSourcesOutputTypeDef",
    {
        "items": List[DataSourceSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListProjectsOutputTypeDef = TypedDict(
    "ListProjectsOutputTypeDef",
    {
        "items": List[ProjectSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSubscriptionTargetsOutputTypeDef = TypedDict(
    "ListSubscriptionTargetsOutputTypeDef",
    {
        "items": List[SubscriptionTargetSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDataSourceRunsOutputTypeDef = TypedDict(
    "ListDataSourceRunsOutputTypeDef",
    {
        "items": List[DataSourceRunSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEnvironmentOutputTypeDef = TypedDict(
    "CreateEnvironmentOutputTypeDef",
    {
        "awsAccountId": str,
        "awsAccountRegion": str,
        "createdAt": datetime,
        "createdBy": str,
        "deploymentProperties": DeploymentPropertiesTypeDef,
        "description": str,
        "domainId": str,
        "environmentActions": List[ConfigurableEnvironmentActionTypeDef],
        "environmentBlueprintId": str,
        "environmentProfileId": str,
        "glossaryTerms": List[str],
        "id": str,
        "lastDeployment": DeploymentTypeDef,
        "name": str,
        "projectId": str,
        "provider": str,
        "provisionedResources": List[ResourceTypeDef],
        "provisioningProperties": ProvisioningPropertiesTypeDef,
        "status": EnvironmentStatusType,
        "updatedAt": datetime,
        "userParameters": List[CustomParameterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEnvironmentOutputTypeDef = TypedDict(
    "GetEnvironmentOutputTypeDef",
    {
        "awsAccountId": str,
        "awsAccountRegion": str,
        "createdAt": datetime,
        "createdBy": str,
        "deploymentProperties": DeploymentPropertiesTypeDef,
        "description": str,
        "domainId": str,
        "environmentActions": List[ConfigurableEnvironmentActionTypeDef],
        "environmentBlueprintId": str,
        "environmentProfileId": str,
        "glossaryTerms": List[str],
        "id": str,
        "lastDeployment": DeploymentTypeDef,
        "name": str,
        "projectId": str,
        "provider": str,
        "provisionedResources": List[ResourceTypeDef],
        "provisioningProperties": ProvisioningPropertiesTypeDef,
        "status": EnvironmentStatusType,
        "updatedAt": datetime,
        "userParameters": List[CustomParameterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEnvironmentOutputTypeDef = TypedDict(
    "UpdateEnvironmentOutputTypeDef",
    {
        "awsAccountId": str,
        "awsAccountRegion": str,
        "createdAt": datetime,
        "createdBy": str,
        "deploymentProperties": DeploymentPropertiesTypeDef,
        "description": str,
        "domainId": str,
        "environmentActions": List[ConfigurableEnvironmentActionTypeDef],
        "environmentBlueprintId": str,
        "environmentProfileId": str,
        "glossaryTerms": List[str],
        "id": str,
        "lastDeployment": DeploymentTypeDef,
        "name": str,
        "projectId": str,
        "provider": str,
        "provisionedResources": List[ResourceTypeDef],
        "provisioningProperties": ProvisioningPropertiesTypeDef,
        "status": EnvironmentStatusType,
        "updatedAt": datetime,
        "userParameters": List[CustomParameterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProjectPolicyGrantPrincipalTypeDef = TypedDict(
    "ProjectPolicyGrantPrincipalTypeDef",
    {
        "projectDesignation": ProjectDesignationType,
        "projectGrantFilter": NotRequired[ProjectGrantFilterTypeDef],
        "projectIdentifier": NotRequired[str],
    },
)
DomainUnitPolicyGrantPrincipalTypeDef = TypedDict(
    "DomainUnitPolicyGrantPrincipalTypeDef",
    {
        "domainUnitDesignation": Literal["OWNER"],
        "domainUnitGrantFilter": NotRequired[DomainUnitGrantFilterUnionTypeDef],
        "domainUnitIdentifier": NotRequired[str],
    },
)
CreateDomainUnitOutputTypeDef = TypedDict(
    "CreateDomainUnitOutputTypeDef",
    {
        "ancestorDomainUnitIds": List[str],
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "id": str,
        "name": str,
        "owners": List[DomainUnitOwnerPropertiesTypeDef],
        "parentDomainUnitId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDomainUnitOutputTypeDef = TypedDict(
    "GetDomainUnitOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "id": str,
        "lastUpdatedAt": datetime,
        "lastUpdatedBy": str,
        "name": str,
        "owners": List[DomainUnitOwnerPropertiesTypeDef],
        "parentDomainUnitId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDomainUnitOutputTypeDef = TypedDict(
    "UpdateDomainUnitOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "id": str,
        "lastUpdatedAt": datetime,
        "lastUpdatedBy": str,
        "name": str,
        "owners": List[DomainUnitOwnerPropertiesTypeDef],
        "parentDomainUnitId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchInputSearchPaginateTypeDef = TypedDict(
    "SearchInputSearchPaginateTypeDef",
    {
        "domainIdentifier": str,
        "searchScope": InventorySearchScopeType,
        "additionalAttributes": NotRequired[Sequence[SearchOutputAdditionalAttributeType]],
        "filters": NotRequired[FilterClausePaginatorTypeDef],
        "owningProjectIdentifier": NotRequired[str],
        "searchIn": NotRequired[Sequence[SearchInItemTypeDef]],
        "searchText": NotRequired[str],
        "sort": NotRequired[SearchSortTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchListingsInputSearchListingsPaginateTypeDef = TypedDict(
    "SearchListingsInputSearchListingsPaginateTypeDef",
    {
        "domainIdentifier": str,
        "additionalAttributes": NotRequired[Sequence[SearchOutputAdditionalAttributeType]],
        "filters": NotRequired[FilterClausePaginatorTypeDef],
        "searchIn": NotRequired[Sequence[SearchInItemTypeDef]],
        "searchText": NotRequired[str],
        "sort": NotRequired[SearchSortTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchTypesInputSearchTypesPaginateTypeDef = TypedDict(
    "SearchTypesInputSearchTypesPaginateTypeDef",
    {
        "domainIdentifier": str,
        "managed": bool,
        "searchScope": TypesSearchScopeType,
        "filters": NotRequired[FilterClausePaginatorTypeDef],
        "searchIn": NotRequired[Sequence[SearchInItemTypeDef]],
        "searchText": NotRequired[str],
        "sort": NotRequired[SearchSortTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchInputRequestTypeDef = TypedDict(
    "SearchInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "searchScope": InventorySearchScopeType,
        "additionalAttributes": NotRequired[Sequence[SearchOutputAdditionalAttributeType]],
        "filters": NotRequired[FilterClauseTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "owningProjectIdentifier": NotRequired[str],
        "searchIn": NotRequired[Sequence[SearchInItemTypeDef]],
        "searchText": NotRequired[str],
        "sort": NotRequired[SearchSortTypeDef],
    },
)
SearchListingsInputRequestTypeDef = TypedDict(
    "SearchListingsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "additionalAttributes": NotRequired[Sequence[SearchOutputAdditionalAttributeType]],
        "filters": NotRequired[FilterClauseTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "searchIn": NotRequired[Sequence[SearchInItemTypeDef]],
        "searchText": NotRequired[str],
        "sort": NotRequired[SearchSortTypeDef],
    },
)
SearchTypesInputRequestTypeDef = TypedDict(
    "SearchTypesInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "managed": bool,
        "searchScope": TypesSearchScopeType,
        "filters": NotRequired[FilterClauseTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "searchIn": NotRequired[Sequence[SearchInItemTypeDef]],
        "searchText": NotRequired[str],
        "sort": NotRequired[SearchSortTypeDef],
    },
)
GlueRunConfigurationOutputTypeDef = TypedDict(
    "GlueRunConfigurationOutputTypeDef",
    {
        "relationalFilterConfigurations": List[RelationalFilterConfigurationOutputTypeDef],
        "accountId": NotRequired[str],
        "autoImportDataQualityResult": NotRequired[bool],
        "dataAccessRole": NotRequired[str],
        "region": NotRequired[str],
    },
)
RelationalFilterConfigurationUnionTypeDef = Union[
    RelationalFilterConfigurationTypeDef, RelationalFilterConfigurationOutputTypeDef
]
SearchTypesResultItemTypeDef = TypedDict(
    "SearchTypesResultItemTypeDef",
    {
        "assetTypeItem": NotRequired[AssetTypeItemTypeDef],
        "formTypeItem": NotRequired[FormTypeDataTypeDef],
        "lineageNodeTypeItem": NotRequired[LineageNodeTypeItemTypeDef],
    },
)
PostTimeSeriesDataPointsInputRequestTypeDef = TypedDict(
    "PostTimeSeriesDataPointsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "entityIdentifier": str,
        "entityType": TimeSeriesEntityTypeType,
        "forms": Sequence[TimeSeriesDataPointFormInputTypeDef],
        "clientToken": NotRequired[str],
    },
)
ListMetadataGenerationRunsOutputTypeDef = TypedDict(
    "ListMetadataGenerationRunsOutputTypeDef",
    {
        "items": List[MetadataGenerationRunItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SelfGrantStatusOutputTypeDef = TypedDict(
    "SelfGrantStatusOutputTypeDef",
    {
        "glueSelfGrantStatus": NotRequired[GlueSelfGrantStatusOutputTypeDef],
        "redshiftSelfGrantStatus": NotRequired[RedshiftSelfGrantStatusOutputTypeDef],
    },
)
CreateSubscriptionGrantInputRequestTypeDef = TypedDict(
    "CreateSubscriptionGrantInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentIdentifier": str,
        "grantedEntity": GrantedEntityInputTypeDef,
        "subscriptionTargetIdentifier": str,
        "assetTargetNames": NotRequired[Sequence[AssetTargetNameMapTypeDef]],
        "clientToken": NotRequired[str],
    },
)
CreateSubscriptionGrantOutputTypeDef = TypedDict(
    "CreateSubscriptionGrantOutputTypeDef",
    {
        "assets": List[SubscribedAssetTypeDef],
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "grantedEntity": GrantedEntityTypeDef,
        "id": str,
        "status": SubscriptionGrantOverallStatusType,
        "subscriptionId": str,
        "subscriptionTargetId": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteSubscriptionGrantOutputTypeDef = TypedDict(
    "DeleteSubscriptionGrantOutputTypeDef",
    {
        "assets": List[SubscribedAssetTypeDef],
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "grantedEntity": GrantedEntityTypeDef,
        "id": str,
        "status": SubscriptionGrantOverallStatusType,
        "subscriptionId": str,
        "subscriptionTargetId": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSubscriptionGrantOutputTypeDef = TypedDict(
    "GetSubscriptionGrantOutputTypeDef",
    {
        "assets": List[SubscribedAssetTypeDef],
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "grantedEntity": GrantedEntityTypeDef,
        "id": str,
        "status": SubscriptionGrantOverallStatusType,
        "subscriptionId": str,
        "subscriptionTargetId": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SubscriptionGrantSummaryTypeDef = TypedDict(
    "SubscriptionGrantSummaryTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "grantedEntity": GrantedEntityTypeDef,
        "id": str,
        "status": SubscriptionGrantOverallStatusType,
        "subscriptionTargetId": str,
        "updatedAt": datetime,
        "assets": NotRequired[List[SubscribedAssetTypeDef]],
        "subscriptionId": NotRequired[str],
        "updatedBy": NotRequired[str],
    },
)
UpdateSubscriptionGrantStatusOutputTypeDef = TypedDict(
    "UpdateSubscriptionGrantStatusOutputTypeDef",
    {
        "assets": List[SubscribedAssetTypeDef],
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "grantedEntity": GrantedEntityTypeDef,
        "id": str,
        "status": SubscriptionGrantOverallStatusType,
        "subscriptionId": str,
        "subscriptionTargetId": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnvironmentBlueprintConfigurationItemTypeDef = TypedDict(
    "EnvironmentBlueprintConfigurationItemTypeDef",
    {
        "domainId": str,
        "environmentBlueprintId": str,
        "createdAt": NotRequired[datetime],
        "enabledRegions": NotRequired[List[str]],
        "manageAccessRoleArn": NotRequired[str],
        "provisioningConfigurations": NotRequired[List[ProvisioningConfigurationOutputTypeDef]],
        "provisioningRoleArn": NotRequired[str],
        "regionalParameters": NotRequired[Dict[str, Dict[str, str]]],
        "updatedAt": NotRequired[datetime],
    },
)
GetEnvironmentBlueprintConfigurationOutputTypeDef = TypedDict(
    "GetEnvironmentBlueprintConfigurationOutputTypeDef",
    {
        "createdAt": datetime,
        "domainId": str,
        "enabledRegions": List[str],
        "environmentBlueprintId": str,
        "manageAccessRoleArn": str,
        "provisioningConfigurations": List[ProvisioningConfigurationOutputTypeDef],
        "provisioningRoleArn": str,
        "regionalParameters": Dict[str, Dict[str, str]],
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutEnvironmentBlueprintConfigurationOutputTypeDef = TypedDict(
    "PutEnvironmentBlueprintConfigurationOutputTypeDef",
    {
        "createdAt": datetime,
        "domainId": str,
        "enabledRegions": List[str],
        "environmentBlueprintId": str,
        "manageAccessRoleArn": str,
        "provisioningConfigurations": List[ProvisioningConfigurationOutputTypeDef],
        "provisioningRoleArn": str,
        "regionalParameters": Dict[str, Dict[str, str]],
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProvisioningConfigurationTypeDef = TypedDict(
    "ProvisioningConfigurationTypeDef",
    {
        "lakeFormationConfiguration": NotRequired[LakeFormationConfigurationUnionTypeDef],
    },
)
ProjectMemberTypeDef = TypedDict(
    "ProjectMemberTypeDef",
    {
        "designation": UserDesignationType,
        "memberDetails": MemberDetailsTypeDef,
    },
)
RowFilterExpressionTypeDef = TypedDict(
    "RowFilterExpressionTypeDef",
    {
        "equalTo": NotRequired[EqualToExpressionTypeDef],
        "greaterThan": NotRequired[GreaterThanExpressionTypeDef],
        "greaterThanOrEqualTo": NotRequired[GreaterThanOrEqualToExpressionTypeDef],
        "in": NotRequired[InExpressionUnionTypeDef],
        "isNotNull": NotRequired[IsNotNullExpressionTypeDef],
        "isNull": NotRequired[IsNullExpressionTypeDef],
        "lessThan": NotRequired[LessThanExpressionTypeDef],
        "lessThanOrEqualTo": NotRequired[LessThanOrEqualToExpressionTypeDef],
        "like": NotRequired[LikeExpressionTypeDef],
        "notEqualTo": NotRequired[NotEqualToExpressionTypeDef],
        "notIn": NotRequired[NotInExpressionUnionTypeDef],
        "notLike": NotRequired[NotLikeExpressionTypeDef],
    },
)
RowFilterOutputTypeDef = TypedDict(
    "RowFilterOutputTypeDef",
    {
        "and": NotRequired[List[Dict[str, Any]]],
        "expression": NotRequired[RowFilterExpressionOutputTypeDef],
        "or": NotRequired[List[Dict[str, Any]]],
    },
)
NotificationOutputTypeDef = TypedDict(
    "NotificationOutputTypeDef",
    {
        "actionLink": str,
        "creationTimestamp": datetime,
        "domainIdentifier": str,
        "identifier": str,
        "lastUpdatedTimestamp": datetime,
        "message": str,
        "title": str,
        "topic": TopicTypeDef,
        "type": NotificationTypeType,
        "metadata": NotRequired[Dict[str, str]],
        "status": NotRequired[TaskStatusType],
    },
)
ListEntityOwnersOutputTypeDef = TypedDict(
    "ListEntityOwnersOutputTypeDef",
    {
        "nextToken": str,
        "owners": List[OwnerPropertiesOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AddEntityOwnerInputRequestTypeDef = TypedDict(
    "AddEntityOwnerInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "entityIdentifier": str,
        "entityType": Literal["DOMAIN_UNIT"],
        "owner": OwnerPropertiesTypeDef,
        "clientToken": NotRequired[str],
    },
)
RemoveEntityOwnerInputRequestTypeDef = TypedDict(
    "RemoveEntityOwnerInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "entityIdentifier": str,
        "entityType": Literal["DOMAIN_UNIT"],
        "owner": OwnerPropertiesTypeDef,
        "clientToken": NotRequired[str],
    },
)
RedshiftRunConfigurationInputTypeDef = TypedDict(
    "RedshiftRunConfigurationInputTypeDef",
    {
        "redshiftCredentialConfiguration": RedshiftCredentialConfigurationTypeDef,
        "redshiftStorage": RedshiftStorageTypeDef,
        "relationalFilterConfigurations": Sequence[RelationalFilterConfigurationTypeDef],
        "dataAccessRole": NotRequired[str],
    },
)
RedshiftRunConfigurationOutputTypeDef = TypedDict(
    "RedshiftRunConfigurationOutputTypeDef",
    {
        "redshiftCredentialConfiguration": RedshiftCredentialConfigurationTypeDef,
        "redshiftStorage": RedshiftStorageTypeDef,
        "relationalFilterConfigurations": List[RelationalFilterConfigurationOutputTypeDef],
        "accountId": NotRequired[str],
        "dataAccessRole": NotRequired[str],
        "region": NotRequired[str],
    },
)
CreateUserProfileOutputTypeDef = TypedDict(
    "CreateUserProfileOutputTypeDef",
    {
        "details": UserProfileDetailsTypeDef,
        "domainId": str,
        "id": str,
        "status": UserProfileStatusType,
        "type": UserProfileTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetUserProfileOutputTypeDef = TypedDict(
    "GetUserProfileOutputTypeDef",
    {
        "details": UserProfileDetailsTypeDef,
        "domainId": str,
        "id": str,
        "status": UserProfileStatusType,
        "type": UserProfileTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateUserProfileOutputTypeDef = TypedDict(
    "UpdateUserProfileOutputTypeDef",
    {
        "details": UserProfileDetailsTypeDef,
        "domainId": str,
        "id": str,
        "status": UserProfileStatusType,
        "type": UserProfileTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UserProfileSummaryTypeDef = TypedDict(
    "UserProfileSummaryTypeDef",
    {
        "details": NotRequired[UserProfileDetailsTypeDef],
        "domainId": NotRequired[str],
        "id": NotRequired[str],
        "status": NotRequired[UserProfileStatusType],
        "type": NotRequired[UserProfileTypeType],
    },
)
CreateSubscriptionRequestInputRequestTypeDef = TypedDict(
    "CreateSubscriptionRequestInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "requestReason": str,
        "subscribedListings": Sequence[SubscribedListingInputTypeDef],
        "subscribedPrincipals": Sequence[SubscribedPrincipalInputTypeDef],
        "clientToken": NotRequired[str],
    },
)
ListEnvironmentActionsOutputTypeDef = TypedDict(
    "ListEnvironmentActionsOutputTypeDef",
    {
        "items": List[EnvironmentActionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchInventoryResultItemTypeDef = TypedDict(
    "SearchInventoryResultItemTypeDef",
    {
        "assetItem": NotRequired[AssetItemTypeDef],
        "dataProductItem": NotRequired[DataProductResultItemTypeDef],
        "glossaryItem": NotRequired[GlossaryItemTypeDef],
        "glossaryTermItem": NotRequired[GlossaryTermItemTypeDef],
    },
)
SearchResultItemTypeDef = TypedDict(
    "SearchResultItemTypeDef",
    {
        "assetListing": NotRequired[AssetListingItemTypeDef],
        "dataProductListing": NotRequired[DataProductListingItemTypeDef],
    },
)
ListingItemTypeDef = TypedDict(
    "ListingItemTypeDef",
    {
        "assetListing": NotRequired[AssetListingTypeDef],
        "dataProductListing": NotRequired[DataProductListingTypeDef],
    },
)
SubscribedListingTypeDef = TypedDict(
    "SubscribedListingTypeDef",
    {
        "description": str,
        "id": str,
        "item": SubscribedListingItemTypeDef,
        "name": str,
        "ownerProjectId": str,
        "ownerProjectName": NotRequired[str],
        "revision": NotRequired[str],
    },
)
ListEnvironmentBlueprintsOutputTypeDef = TypedDict(
    "ListEnvironmentBlueprintsOutputTypeDef",
    {
        "items": List[EnvironmentBlueprintSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PolicyGrantPrincipalOutputTypeDef = TypedDict(
    "PolicyGrantPrincipalOutputTypeDef",
    {
        "domainUnit": NotRequired[DomainUnitPolicyGrantPrincipalOutputTypeDef],
        "group": NotRequired[GroupPolicyGrantPrincipalTypeDef],
        "project": NotRequired[ProjectPolicyGrantPrincipalTypeDef],
        "user": NotRequired[UserPolicyGrantPrincipalOutputTypeDef],
    },
)
DomainUnitPolicyGrantPrincipalUnionTypeDef = Union[
    DomainUnitPolicyGrantPrincipalTypeDef, DomainUnitPolicyGrantPrincipalOutputTypeDef
]
GlueRunConfigurationInputTypeDef = TypedDict(
    "GlueRunConfigurationInputTypeDef",
    {
        "relationalFilterConfigurations": Sequence[RelationalFilterConfigurationUnionTypeDef],
        "autoImportDataQualityResult": NotRequired[bool],
        "dataAccessRole": NotRequired[str],
    },
)
SearchTypesOutputTypeDef = TypedDict(
    "SearchTypesOutputTypeDef",
    {
        "items": List[SearchTypesResultItemTypeDef],
        "nextToken": str,
        "totalMatchCount": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSubscriptionGrantsOutputTypeDef = TypedDict(
    "ListSubscriptionGrantsOutputTypeDef",
    {
        "items": List[SubscriptionGrantSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEnvironmentBlueprintConfigurationsOutputTypeDef = TypedDict(
    "ListEnvironmentBlueprintConfigurationsOutputTypeDef",
    {
        "items": List[EnvironmentBlueprintConfigurationItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProvisioningConfigurationUnionTypeDef = Union[
    ProvisioningConfigurationTypeDef, ProvisioningConfigurationOutputTypeDef
]
ListProjectMembershipsOutputTypeDef = TypedDict(
    "ListProjectMembershipsOutputTypeDef",
    {
        "members": List[ProjectMemberTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RowFilterExpressionUnionTypeDef = Union[
    RowFilterExpressionTypeDef, RowFilterExpressionOutputTypeDef
]
RowFilterConfigurationOutputTypeDef = TypedDict(
    "RowFilterConfigurationOutputTypeDef",
    {
        "rowFilter": RowFilterOutputTypeDef,
        "sensitive": NotRequired[bool],
    },
)
ListNotificationsOutputTypeDef = TypedDict(
    "ListNotificationsOutputTypeDef",
    {
        "nextToken": str,
        "notifications": List[NotificationOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DataSourceConfigurationOutputTypeDef = TypedDict(
    "DataSourceConfigurationOutputTypeDef",
    {
        "glueRunConfiguration": NotRequired[GlueRunConfigurationOutputTypeDef],
        "redshiftRunConfiguration": NotRequired[RedshiftRunConfigurationOutputTypeDef],
    },
)
SearchUserProfilesOutputTypeDef = TypedDict(
    "SearchUserProfilesOutputTypeDef",
    {
        "items": List[UserProfileSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchOutputTypeDef = TypedDict(
    "SearchOutputTypeDef",
    {
        "items": List[SearchInventoryResultItemTypeDef],
        "nextToken": str,
        "totalMatchCount": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchListingsOutputTypeDef = TypedDict(
    "SearchListingsOutputTypeDef",
    {
        "items": List[SearchResultItemTypeDef],
        "nextToken": str,
        "totalMatchCount": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetListingOutputTypeDef = TypedDict(
    "GetListingOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "id": str,
        "item": ListingItemTypeDef,
        "listingRevision": str,
        "name": str,
        "status": ListingStatusType,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AcceptSubscriptionRequestOutputTypeDef = TypedDict(
    "AcceptSubscriptionRequestOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "decisionComment": str,
        "domainId": str,
        "id": str,
        "requestReason": str,
        "reviewerId": str,
        "status": SubscriptionRequestStatusType,
        "subscribedListings": List[SubscribedListingTypeDef],
        "subscribedPrincipals": List[SubscribedPrincipalTypeDef],
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CancelSubscriptionOutputTypeDef = TypedDict(
    "CancelSubscriptionOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "id": str,
        "retainPermissions": bool,
        "status": SubscriptionStatusType,
        "subscribedListing": SubscribedListingTypeDef,
        "subscribedPrincipal": SubscribedPrincipalTypeDef,
        "subscriptionRequestId": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSubscriptionRequestOutputTypeDef = TypedDict(
    "CreateSubscriptionRequestOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "decisionComment": str,
        "domainId": str,
        "id": str,
        "requestReason": str,
        "reviewerId": str,
        "status": SubscriptionRequestStatusType,
        "subscribedListings": List[SubscribedListingTypeDef],
        "subscribedPrincipals": List[SubscribedPrincipalTypeDef],
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSubscriptionOutputTypeDef = TypedDict(
    "GetSubscriptionOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "id": str,
        "retainPermissions": bool,
        "status": SubscriptionStatusType,
        "subscribedListing": SubscribedListingTypeDef,
        "subscribedPrincipal": SubscribedPrincipalTypeDef,
        "subscriptionRequestId": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSubscriptionRequestDetailsOutputTypeDef = TypedDict(
    "GetSubscriptionRequestDetailsOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "decisionComment": str,
        "domainId": str,
        "id": str,
        "requestReason": str,
        "reviewerId": str,
        "status": SubscriptionRequestStatusType,
        "subscribedListings": List[SubscribedListingTypeDef],
        "subscribedPrincipals": List[SubscribedPrincipalTypeDef],
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RejectSubscriptionRequestOutputTypeDef = TypedDict(
    "RejectSubscriptionRequestOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "decisionComment": str,
        "domainId": str,
        "id": str,
        "requestReason": str,
        "reviewerId": str,
        "status": SubscriptionRequestStatusType,
        "subscribedListings": List[SubscribedListingTypeDef],
        "subscribedPrincipals": List[SubscribedPrincipalTypeDef],
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RevokeSubscriptionOutputTypeDef = TypedDict(
    "RevokeSubscriptionOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "id": str,
        "retainPermissions": bool,
        "status": SubscriptionStatusType,
        "subscribedListing": SubscribedListingTypeDef,
        "subscribedPrincipal": SubscribedPrincipalTypeDef,
        "subscriptionRequestId": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SubscriptionRequestSummaryTypeDef = TypedDict(
    "SubscriptionRequestSummaryTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "id": str,
        "requestReason": str,
        "status": SubscriptionRequestStatusType,
        "subscribedListings": List[SubscribedListingTypeDef],
        "subscribedPrincipals": List[SubscribedPrincipalTypeDef],
        "updatedAt": datetime,
        "decisionComment": NotRequired[str],
        "reviewerId": NotRequired[str],
        "updatedBy": NotRequired[str],
    },
)
SubscriptionSummaryTypeDef = TypedDict(
    "SubscriptionSummaryTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "id": str,
        "status": SubscriptionStatusType,
        "subscribedListing": SubscribedListingTypeDef,
        "subscribedPrincipal": SubscribedPrincipalTypeDef,
        "updatedAt": datetime,
        "retainPermissions": NotRequired[bool],
        "subscriptionRequestId": NotRequired[str],
        "updatedBy": NotRequired[str],
    },
)
UpdateSubscriptionRequestOutputTypeDef = TypedDict(
    "UpdateSubscriptionRequestOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "decisionComment": str,
        "domainId": str,
        "id": str,
        "requestReason": str,
        "reviewerId": str,
        "status": SubscriptionRequestStatusType,
        "subscribedListings": List[SubscribedListingTypeDef],
        "subscribedPrincipals": List[SubscribedPrincipalTypeDef],
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PolicyGrantMemberTypeDef = TypedDict(
    "PolicyGrantMemberTypeDef",
    {
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "detail": NotRequired[PolicyGrantDetailOutputTypeDef],
        "principal": NotRequired[PolicyGrantPrincipalOutputTypeDef],
    },
)
PolicyGrantPrincipalTypeDef = TypedDict(
    "PolicyGrantPrincipalTypeDef",
    {
        "domainUnit": NotRequired[DomainUnitPolicyGrantPrincipalUnionTypeDef],
        "group": NotRequired[GroupPolicyGrantPrincipalTypeDef],
        "project": NotRequired[ProjectPolicyGrantPrincipalTypeDef],
        "user": NotRequired[UserPolicyGrantPrincipalUnionTypeDef],
    },
)
DataSourceConfigurationInputTypeDef = TypedDict(
    "DataSourceConfigurationInputTypeDef",
    {
        "glueRunConfiguration": NotRequired[GlueRunConfigurationInputTypeDef],
        "redshiftRunConfiguration": NotRequired[RedshiftRunConfigurationInputTypeDef],
    },
)
PutEnvironmentBlueprintConfigurationInputRequestTypeDef = TypedDict(
    "PutEnvironmentBlueprintConfigurationInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "enabledRegions": Sequence[str],
        "environmentBlueprintIdentifier": str,
        "manageAccessRoleArn": NotRequired[str],
        "provisioningConfigurations": NotRequired[Sequence[ProvisioningConfigurationUnionTypeDef]],
        "provisioningRoleArn": NotRequired[str],
        "regionalParameters": NotRequired[Mapping[str, Mapping[str, str]]],
    },
)
RowFilterTypeDef = TypedDict(
    "RowFilterTypeDef",
    {
        "and": NotRequired[Sequence[Mapping[str, Any]]],
        "expression": NotRequired[RowFilterExpressionUnionTypeDef],
        "or": NotRequired[Sequence[Mapping[str, Any]]],
    },
)
AssetFilterConfigurationOutputTypeDef = TypedDict(
    "AssetFilterConfigurationOutputTypeDef",
    {
        "columnConfiguration": NotRequired[ColumnFilterConfigurationOutputTypeDef],
        "rowConfiguration": NotRequired[RowFilterConfigurationOutputTypeDef],
    },
)
CreateDataSourceOutputTypeDef = TypedDict(
    "CreateDataSourceOutputTypeDef",
    {
        "assetFormsOutput": List[FormOutputTypeDef],
        "configuration": DataSourceConfigurationOutputTypeDef,
        "createdAt": datetime,
        "description": str,
        "domainId": str,
        "enableSetting": EnableSettingType,
        "environmentId": str,
        "errorMessage": DataSourceErrorMessageTypeDef,
        "id": str,
        "lastRunAt": datetime,
        "lastRunErrorMessage": DataSourceErrorMessageTypeDef,
        "lastRunStatus": DataSourceRunStatusType,
        "name": str,
        "projectId": str,
        "publishOnImport": bool,
        "recommendation": RecommendationConfigurationTypeDef,
        "schedule": ScheduleConfigurationTypeDef,
        "status": DataSourceStatusType,
        "type": str,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDataSourceOutputTypeDef = TypedDict(
    "DeleteDataSourceOutputTypeDef",
    {
        "assetFormsOutput": List[FormOutputTypeDef],
        "configuration": DataSourceConfigurationOutputTypeDef,
        "createdAt": datetime,
        "description": str,
        "domainId": str,
        "enableSetting": EnableSettingType,
        "environmentId": str,
        "errorMessage": DataSourceErrorMessageTypeDef,
        "id": str,
        "lastRunAt": datetime,
        "lastRunErrorMessage": DataSourceErrorMessageTypeDef,
        "lastRunStatus": DataSourceRunStatusType,
        "name": str,
        "projectId": str,
        "publishOnImport": bool,
        "retainPermissionsOnRevokeFailure": bool,
        "schedule": ScheduleConfigurationTypeDef,
        "selfGrantStatus": SelfGrantStatusOutputTypeDef,
        "status": DataSourceStatusType,
        "type": str,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDataSourceOutputTypeDef = TypedDict(
    "GetDataSourceOutputTypeDef",
    {
        "assetFormsOutput": List[FormOutputTypeDef],
        "configuration": DataSourceConfigurationOutputTypeDef,
        "createdAt": datetime,
        "description": str,
        "domainId": str,
        "enableSetting": EnableSettingType,
        "environmentId": str,
        "errorMessage": DataSourceErrorMessageTypeDef,
        "id": str,
        "lastRunAssetCount": int,
        "lastRunAt": datetime,
        "lastRunErrorMessage": DataSourceErrorMessageTypeDef,
        "lastRunStatus": DataSourceRunStatusType,
        "name": str,
        "projectId": str,
        "publishOnImport": bool,
        "recommendation": RecommendationConfigurationTypeDef,
        "schedule": ScheduleConfigurationTypeDef,
        "selfGrantStatus": SelfGrantStatusOutputTypeDef,
        "status": DataSourceStatusType,
        "type": str,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDataSourceOutputTypeDef = TypedDict(
    "UpdateDataSourceOutputTypeDef",
    {
        "assetFormsOutput": List[FormOutputTypeDef],
        "configuration": DataSourceConfigurationOutputTypeDef,
        "createdAt": datetime,
        "description": str,
        "domainId": str,
        "enableSetting": EnableSettingType,
        "environmentId": str,
        "errorMessage": DataSourceErrorMessageTypeDef,
        "id": str,
        "lastRunAt": datetime,
        "lastRunErrorMessage": DataSourceErrorMessageTypeDef,
        "lastRunStatus": DataSourceRunStatusType,
        "name": str,
        "projectId": str,
        "publishOnImport": bool,
        "recommendation": RecommendationConfigurationTypeDef,
        "retainPermissionsOnRevokeFailure": bool,
        "schedule": ScheduleConfigurationTypeDef,
        "selfGrantStatus": SelfGrantStatusOutputTypeDef,
        "status": DataSourceStatusType,
        "type": str,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSubscriptionRequestsOutputTypeDef = TypedDict(
    "ListSubscriptionRequestsOutputTypeDef",
    {
        "items": List[SubscriptionRequestSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSubscriptionsOutputTypeDef = TypedDict(
    "ListSubscriptionsOutputTypeDef",
    {
        "items": List[SubscriptionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPolicyGrantsOutputTypeDef = TypedDict(
    "ListPolicyGrantsOutputTypeDef",
    {
        "grantList": List[PolicyGrantMemberTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AddPolicyGrantInputRequestTypeDef = TypedDict(
    "AddPolicyGrantInputRequestTypeDef",
    {
        "detail": PolicyGrantDetailTypeDef,
        "domainIdentifier": str,
        "entityIdentifier": str,
        "entityType": TargetEntityTypeType,
        "policyType": ManagedPolicyTypeType,
        "principal": PolicyGrantPrincipalTypeDef,
        "clientToken": NotRequired[str],
    },
)
RemovePolicyGrantInputRequestTypeDef = TypedDict(
    "RemovePolicyGrantInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "entityIdentifier": str,
        "entityType": TargetEntityTypeType,
        "policyType": ManagedPolicyTypeType,
        "principal": PolicyGrantPrincipalTypeDef,
        "clientToken": NotRequired[str],
    },
)
CreateDataSourceInputRequestTypeDef = TypedDict(
    "CreateDataSourceInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentIdentifier": str,
        "name": str,
        "projectIdentifier": str,
        "type": str,
        "assetFormsInput": NotRequired[Sequence[FormInputTypeDef]],
        "clientToken": NotRequired[str],
        "configuration": NotRequired[DataSourceConfigurationInputTypeDef],
        "description": NotRequired[str],
        "enableSetting": NotRequired[EnableSettingType],
        "publishOnImport": NotRequired[bool],
        "recommendation": NotRequired[RecommendationConfigurationTypeDef],
        "schedule": NotRequired[ScheduleConfigurationTypeDef],
    },
)
UpdateDataSourceInputRequestTypeDef = TypedDict(
    "UpdateDataSourceInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "assetFormsInput": NotRequired[Sequence[FormInputTypeDef]],
        "configuration": NotRequired[DataSourceConfigurationInputTypeDef],
        "description": NotRequired[str],
        "enableSetting": NotRequired[EnableSettingType],
        "name": NotRequired[str],
        "publishOnImport": NotRequired[bool],
        "recommendation": NotRequired[RecommendationConfigurationTypeDef],
        "retainPermissionsOnRevokeFailure": NotRequired[bool],
        "schedule": NotRequired[ScheduleConfigurationTypeDef],
    },
)
RowFilterUnionTypeDef = Union[RowFilterTypeDef, RowFilterOutputTypeDef]
CreateAssetFilterOutputTypeDef = TypedDict(
    "CreateAssetFilterOutputTypeDef",
    {
        "assetId": str,
        "configuration": AssetFilterConfigurationOutputTypeDef,
        "createdAt": datetime,
        "description": str,
        "domainId": str,
        "effectiveColumnNames": List[str],
        "effectiveRowFilter": str,
        "errorMessage": str,
        "id": str,
        "name": str,
        "status": FilterStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAssetFilterOutputTypeDef = TypedDict(
    "GetAssetFilterOutputTypeDef",
    {
        "assetId": str,
        "configuration": AssetFilterConfigurationOutputTypeDef,
        "createdAt": datetime,
        "description": str,
        "domainId": str,
        "effectiveColumnNames": List[str],
        "effectiveRowFilter": str,
        "errorMessage": str,
        "id": str,
        "name": str,
        "status": FilterStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAssetFilterOutputTypeDef = TypedDict(
    "UpdateAssetFilterOutputTypeDef",
    {
        "assetId": str,
        "configuration": AssetFilterConfigurationOutputTypeDef,
        "createdAt": datetime,
        "description": str,
        "domainId": str,
        "effectiveColumnNames": List[str],
        "effectiveRowFilter": str,
        "errorMessage": str,
        "id": str,
        "name": str,
        "status": FilterStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RowFilterConfigurationTypeDef = TypedDict(
    "RowFilterConfigurationTypeDef",
    {
        "rowFilter": RowFilterUnionTypeDef,
        "sensitive": NotRequired[bool],
    },
)
RowFilterConfigurationUnionTypeDef = Union[
    RowFilterConfigurationTypeDef, RowFilterConfigurationOutputTypeDef
]
AssetFilterConfigurationTypeDef = TypedDict(
    "AssetFilterConfigurationTypeDef",
    {
        "columnConfiguration": NotRequired[ColumnFilterConfigurationUnionTypeDef],
        "rowConfiguration": NotRequired[RowFilterConfigurationUnionTypeDef],
    },
)
CreateAssetFilterInputRequestTypeDef = TypedDict(
    "CreateAssetFilterInputRequestTypeDef",
    {
        "assetIdentifier": str,
        "configuration": AssetFilterConfigurationTypeDef,
        "domainIdentifier": str,
        "name": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
    },
)
UpdateAssetFilterInputRequestTypeDef = TypedDict(
    "UpdateAssetFilterInputRequestTypeDef",
    {
        "assetIdentifier": str,
        "domainIdentifier": str,
        "identifier": str,
        "configuration": NotRequired[AssetFilterConfigurationTypeDef],
        "description": NotRequired[str],
        "name": NotRequired[str],
    },
)
