"""
Type annotations for datazone service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_datazone.client import DataZoneClient

    session = Session()
    client: DataZoneClient = session.client("datazone")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    ListAssetFiltersPaginator,
    ListAssetRevisionsPaginator,
    ListDataProductRevisionsPaginator,
    ListDataSourceRunActivitiesPaginator,
    ListDataSourceRunsPaginator,
    ListDataSourcesPaginator,
    ListDomainsPaginator,
    ListDomainUnitsForParentPaginator,
    ListEntityOwnersPaginator,
    ListEnvironmentActionsPaginator,
    ListEnvironmentBlueprintConfigurationsPaginator,
    ListEnvironmentBlueprintsPaginator,
    ListEnvironmentProfilesPaginator,
    ListEnvironmentsPaginator,
    ListLineageNodeHistoryPaginator,
    ListMetadataGenerationRunsPaginator,
    ListNotificationsPaginator,
    ListPolicyGrantsPaginator,
    ListProjectMembershipsPaginator,
    ListProjectsPaginator,
    ListSubscriptionGrantsPaginator,
    ListSubscriptionRequestsPaginator,
    ListSubscriptionsPaginator,
    ListSubscriptionTargetsPaginator,
    ListTimeSeriesDataPointsPaginator,
    SearchGroupProfilesPaginator,
    SearchListingsPaginator,
    SearchPaginator,
    SearchTypesPaginator,
    SearchUserProfilesPaginator,
)
from .type_defs import (
    AcceptPredictionsInputRequestTypeDef,
    AcceptPredictionsOutputTypeDef,
    AcceptSubscriptionRequestInputRequestTypeDef,
    AcceptSubscriptionRequestOutputTypeDef,
    AddEntityOwnerInputRequestTypeDef,
    AddPolicyGrantInputRequestTypeDef,
    AssociateEnvironmentRoleInputRequestTypeDef,
    CancelMetadataGenerationRunInputRequestTypeDef,
    CancelSubscriptionInputRequestTypeDef,
    CancelSubscriptionOutputTypeDef,
    CreateAssetFilterInputRequestTypeDef,
    CreateAssetFilterOutputTypeDef,
    CreateAssetInputRequestTypeDef,
    CreateAssetOutputTypeDef,
    CreateAssetRevisionInputRequestTypeDef,
    CreateAssetRevisionOutputTypeDef,
    CreateAssetTypeInputRequestTypeDef,
    CreateAssetTypeOutputTypeDef,
    CreateDataProductInputRequestTypeDef,
    CreateDataProductOutputTypeDef,
    CreateDataProductRevisionInputRequestTypeDef,
    CreateDataProductRevisionOutputTypeDef,
    CreateDataSourceInputRequestTypeDef,
    CreateDataSourceOutputTypeDef,
    CreateDomainInputRequestTypeDef,
    CreateDomainOutputTypeDef,
    CreateDomainUnitInputRequestTypeDef,
    CreateDomainUnitOutputTypeDef,
    CreateEnvironmentActionInputRequestTypeDef,
    CreateEnvironmentActionOutputTypeDef,
    CreateEnvironmentInputRequestTypeDef,
    CreateEnvironmentOutputTypeDef,
    CreateEnvironmentProfileInputRequestTypeDef,
    CreateEnvironmentProfileOutputTypeDef,
    CreateFormTypeInputRequestTypeDef,
    CreateFormTypeOutputTypeDef,
    CreateGlossaryInputRequestTypeDef,
    CreateGlossaryOutputTypeDef,
    CreateGlossaryTermInputRequestTypeDef,
    CreateGlossaryTermOutputTypeDef,
    CreateGroupProfileInputRequestTypeDef,
    CreateGroupProfileOutputTypeDef,
    CreateListingChangeSetInputRequestTypeDef,
    CreateListingChangeSetOutputTypeDef,
    CreateProjectInputRequestTypeDef,
    CreateProjectMembershipInputRequestTypeDef,
    CreateProjectOutputTypeDef,
    CreateSubscriptionGrantInputRequestTypeDef,
    CreateSubscriptionGrantOutputTypeDef,
    CreateSubscriptionRequestInputRequestTypeDef,
    CreateSubscriptionRequestOutputTypeDef,
    CreateSubscriptionTargetInputRequestTypeDef,
    CreateSubscriptionTargetOutputTypeDef,
    CreateUserProfileInputRequestTypeDef,
    CreateUserProfileOutputTypeDef,
    DeleteAssetFilterInputRequestTypeDef,
    DeleteAssetInputRequestTypeDef,
    DeleteAssetTypeInputRequestTypeDef,
    DeleteDataProductInputRequestTypeDef,
    DeleteDataSourceInputRequestTypeDef,
    DeleteDataSourceOutputTypeDef,
    DeleteDomainInputRequestTypeDef,
    DeleteDomainOutputTypeDef,
    DeleteDomainUnitInputRequestTypeDef,
    DeleteEnvironmentActionInputRequestTypeDef,
    DeleteEnvironmentBlueprintConfigurationInputRequestTypeDef,
    DeleteEnvironmentInputRequestTypeDef,
    DeleteEnvironmentProfileInputRequestTypeDef,
    DeleteFormTypeInputRequestTypeDef,
    DeleteGlossaryInputRequestTypeDef,
    DeleteGlossaryTermInputRequestTypeDef,
    DeleteListingInputRequestTypeDef,
    DeleteProjectInputRequestTypeDef,
    DeleteProjectMembershipInputRequestTypeDef,
    DeleteSubscriptionGrantInputRequestTypeDef,
    DeleteSubscriptionGrantOutputTypeDef,
    DeleteSubscriptionRequestInputRequestTypeDef,
    DeleteSubscriptionTargetInputRequestTypeDef,
    DeleteTimeSeriesDataPointsInputRequestTypeDef,
    DisassociateEnvironmentRoleInputRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    GetAssetFilterInputRequestTypeDef,
    GetAssetFilterOutputTypeDef,
    GetAssetInputRequestTypeDef,
    GetAssetOutputTypeDef,
    GetAssetTypeInputRequestTypeDef,
    GetAssetTypeOutputTypeDef,
    GetDataProductInputRequestTypeDef,
    GetDataProductOutputTypeDef,
    GetDataSourceInputRequestTypeDef,
    GetDataSourceOutputTypeDef,
    GetDataSourceRunInputRequestTypeDef,
    GetDataSourceRunOutputTypeDef,
    GetDomainInputRequestTypeDef,
    GetDomainOutputTypeDef,
    GetDomainUnitInputRequestTypeDef,
    GetDomainUnitOutputTypeDef,
    GetEnvironmentActionInputRequestTypeDef,
    GetEnvironmentActionOutputTypeDef,
    GetEnvironmentBlueprintConfigurationInputRequestTypeDef,
    GetEnvironmentBlueprintConfigurationOutputTypeDef,
    GetEnvironmentBlueprintInputRequestTypeDef,
    GetEnvironmentBlueprintOutputTypeDef,
    GetEnvironmentCredentialsInputRequestTypeDef,
    GetEnvironmentCredentialsOutputTypeDef,
    GetEnvironmentInputRequestTypeDef,
    GetEnvironmentOutputTypeDef,
    GetEnvironmentProfileInputRequestTypeDef,
    GetEnvironmentProfileOutputTypeDef,
    GetFormTypeInputRequestTypeDef,
    GetFormTypeOutputTypeDef,
    GetGlossaryInputRequestTypeDef,
    GetGlossaryOutputTypeDef,
    GetGlossaryTermInputRequestTypeDef,
    GetGlossaryTermOutputTypeDef,
    GetGroupProfileInputRequestTypeDef,
    GetGroupProfileOutputTypeDef,
    GetIamPortalLoginUrlInputRequestTypeDef,
    GetIamPortalLoginUrlOutputTypeDef,
    GetLineageNodeInputRequestTypeDef,
    GetLineageNodeOutputTypeDef,
    GetListingInputRequestTypeDef,
    GetListingOutputTypeDef,
    GetMetadataGenerationRunInputRequestTypeDef,
    GetMetadataGenerationRunOutputTypeDef,
    GetProjectInputRequestTypeDef,
    GetProjectOutputTypeDef,
    GetSubscriptionGrantInputRequestTypeDef,
    GetSubscriptionGrantOutputTypeDef,
    GetSubscriptionInputRequestTypeDef,
    GetSubscriptionOutputTypeDef,
    GetSubscriptionRequestDetailsInputRequestTypeDef,
    GetSubscriptionRequestDetailsOutputTypeDef,
    GetSubscriptionTargetInputRequestTypeDef,
    GetSubscriptionTargetOutputTypeDef,
    GetTimeSeriesDataPointInputRequestTypeDef,
    GetTimeSeriesDataPointOutputTypeDef,
    GetUserProfileInputRequestTypeDef,
    GetUserProfileOutputTypeDef,
    ListAssetFiltersInputRequestTypeDef,
    ListAssetFiltersOutputTypeDef,
    ListAssetRevisionsInputRequestTypeDef,
    ListAssetRevisionsOutputTypeDef,
    ListDataProductRevisionsInputRequestTypeDef,
    ListDataProductRevisionsOutputTypeDef,
    ListDataSourceRunActivitiesInputRequestTypeDef,
    ListDataSourceRunActivitiesOutputTypeDef,
    ListDataSourceRunsInputRequestTypeDef,
    ListDataSourceRunsOutputTypeDef,
    ListDataSourcesInputRequestTypeDef,
    ListDataSourcesOutputTypeDef,
    ListDomainsInputRequestTypeDef,
    ListDomainsOutputTypeDef,
    ListDomainUnitsForParentInputRequestTypeDef,
    ListDomainUnitsForParentOutputTypeDef,
    ListEntityOwnersInputRequestTypeDef,
    ListEntityOwnersOutputTypeDef,
    ListEnvironmentActionsInputRequestTypeDef,
    ListEnvironmentActionsOutputTypeDef,
    ListEnvironmentBlueprintConfigurationsInputRequestTypeDef,
    ListEnvironmentBlueprintConfigurationsOutputTypeDef,
    ListEnvironmentBlueprintsInputRequestTypeDef,
    ListEnvironmentBlueprintsOutputTypeDef,
    ListEnvironmentProfilesInputRequestTypeDef,
    ListEnvironmentProfilesOutputTypeDef,
    ListEnvironmentsInputRequestTypeDef,
    ListEnvironmentsOutputTypeDef,
    ListLineageNodeHistoryInputRequestTypeDef,
    ListLineageNodeHistoryOutputTypeDef,
    ListMetadataGenerationRunsInputRequestTypeDef,
    ListMetadataGenerationRunsOutputTypeDef,
    ListNotificationsInputRequestTypeDef,
    ListNotificationsOutputTypeDef,
    ListPolicyGrantsInputRequestTypeDef,
    ListPolicyGrantsOutputTypeDef,
    ListProjectMembershipsInputRequestTypeDef,
    ListProjectMembershipsOutputTypeDef,
    ListProjectsInputRequestTypeDef,
    ListProjectsOutputTypeDef,
    ListSubscriptionGrantsInputRequestTypeDef,
    ListSubscriptionGrantsOutputTypeDef,
    ListSubscriptionRequestsInputRequestTypeDef,
    ListSubscriptionRequestsOutputTypeDef,
    ListSubscriptionsInputRequestTypeDef,
    ListSubscriptionsOutputTypeDef,
    ListSubscriptionTargetsInputRequestTypeDef,
    ListSubscriptionTargetsOutputTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTimeSeriesDataPointsInputRequestTypeDef,
    ListTimeSeriesDataPointsOutputTypeDef,
    PostLineageEventInputRequestTypeDef,
    PostTimeSeriesDataPointsInputRequestTypeDef,
    PostTimeSeriesDataPointsOutputTypeDef,
    PutEnvironmentBlueprintConfigurationInputRequestTypeDef,
    PutEnvironmentBlueprintConfigurationOutputTypeDef,
    RejectPredictionsInputRequestTypeDef,
    RejectPredictionsOutputTypeDef,
    RejectSubscriptionRequestInputRequestTypeDef,
    RejectSubscriptionRequestOutputTypeDef,
    RemoveEntityOwnerInputRequestTypeDef,
    RemovePolicyGrantInputRequestTypeDef,
    RevokeSubscriptionInputRequestTypeDef,
    RevokeSubscriptionOutputTypeDef,
    SearchGroupProfilesInputRequestTypeDef,
    SearchGroupProfilesOutputTypeDef,
    SearchInputRequestTypeDef,
    SearchListingsInputRequestTypeDef,
    SearchListingsOutputTypeDef,
    SearchOutputTypeDef,
    SearchTypesInputRequestTypeDef,
    SearchTypesOutputTypeDef,
    SearchUserProfilesInputRequestTypeDef,
    SearchUserProfilesOutputTypeDef,
    StartDataSourceRunInputRequestTypeDef,
    StartDataSourceRunOutputTypeDef,
    StartMetadataGenerationRunInputRequestTypeDef,
    StartMetadataGenerationRunOutputTypeDef,
    TagResourceRequestRequestTypeDef,
    UntagResourceRequestRequestTypeDef,
    UpdateAssetFilterInputRequestTypeDef,
    UpdateAssetFilterOutputTypeDef,
    UpdateDataSourceInputRequestTypeDef,
    UpdateDataSourceOutputTypeDef,
    UpdateDomainInputRequestTypeDef,
    UpdateDomainOutputTypeDef,
    UpdateDomainUnitInputRequestTypeDef,
    UpdateDomainUnitOutputTypeDef,
    UpdateEnvironmentActionInputRequestTypeDef,
    UpdateEnvironmentActionOutputTypeDef,
    UpdateEnvironmentInputRequestTypeDef,
    UpdateEnvironmentOutputTypeDef,
    UpdateEnvironmentProfileInputRequestTypeDef,
    UpdateEnvironmentProfileOutputTypeDef,
    UpdateGlossaryInputRequestTypeDef,
    UpdateGlossaryOutputTypeDef,
    UpdateGlossaryTermInputRequestTypeDef,
    UpdateGlossaryTermOutputTypeDef,
    UpdateGroupProfileInputRequestTypeDef,
    UpdateGroupProfileOutputTypeDef,
    UpdateProjectInputRequestTypeDef,
    UpdateProjectOutputTypeDef,
    UpdateSubscriptionGrantStatusInputRequestTypeDef,
    UpdateSubscriptionGrantStatusOutputTypeDef,
    UpdateSubscriptionRequestInputRequestTypeDef,
    UpdateSubscriptionRequestOutputTypeDef,
    UpdateSubscriptionTargetInputRequestTypeDef,
    UpdateSubscriptionTargetOutputTypeDef,
    UpdateUserProfileInputRequestTypeDef,
    UpdateUserProfileOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("DataZoneClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class DataZoneClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DataZoneClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#exceptions)
        """

    def accept_predictions(
        self, **kwargs: Unpack[AcceptPredictionsInputRequestTypeDef]
    ) -> AcceptPredictionsOutputTypeDef:
        """
        Accepts automatically generated business-friendly metadata for your Amazon
        DataZone
        assets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.accept_predictions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#accept_predictions)
        """

    def accept_subscription_request(
        self, **kwargs: Unpack[AcceptSubscriptionRequestInputRequestTypeDef]
    ) -> AcceptSubscriptionRequestOutputTypeDef:
        """
        Accepts a subscription request to a specific asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.accept_subscription_request)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#accept_subscription_request)
        """

    def add_entity_owner(
        self, **kwargs: Unpack[AddEntityOwnerInputRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Adds the owner of an entity (a domain unit).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.add_entity_owner)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#add_entity_owner)
        """

    def add_policy_grant(
        self, **kwargs: Unpack[AddPolicyGrantInputRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Adds a policy grant (an authorization policy) to a specified entity, including
        domain units, environment blueprint configurations, or environment
        profiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.add_policy_grant)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#add_policy_grant)
        """

    def associate_environment_role(
        self, **kwargs: Unpack[AssociateEnvironmentRoleInputRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Associates the environment role in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.associate_environment_role)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#associate_environment_role)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#can_paginate)
        """

    def cancel_metadata_generation_run(
        self, **kwargs: Unpack[CancelMetadataGenerationRunInputRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Cancels the metadata generation run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.cancel_metadata_generation_run)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#cancel_metadata_generation_run)
        """

    def cancel_subscription(
        self, **kwargs: Unpack[CancelSubscriptionInputRequestTypeDef]
    ) -> CancelSubscriptionOutputTypeDef:
        """
        Cancels the subscription to the specified asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.cancel_subscription)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#cancel_subscription)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#close)
        """

    def create_asset(
        self, **kwargs: Unpack[CreateAssetInputRequestTypeDef]
    ) -> CreateAssetOutputTypeDef:
        """
        Creates an asset in Amazon DataZone catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_asset)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_asset)
        """

    def create_asset_filter(
        self, **kwargs: Unpack[CreateAssetFilterInputRequestTypeDef]
    ) -> CreateAssetFilterOutputTypeDef:
        """
        Creates a data asset filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_asset_filter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_asset_filter)
        """

    def create_asset_revision(
        self, **kwargs: Unpack[CreateAssetRevisionInputRequestTypeDef]
    ) -> CreateAssetRevisionOutputTypeDef:
        """
        Creates a revision of the asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_asset_revision)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_asset_revision)
        """

    def create_asset_type(
        self, **kwargs: Unpack[CreateAssetTypeInputRequestTypeDef]
    ) -> CreateAssetTypeOutputTypeDef:
        """
        Creates a custom asset type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_asset_type)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_asset_type)
        """

    def create_data_product(
        self, **kwargs: Unpack[CreateDataProductInputRequestTypeDef]
    ) -> CreateDataProductOutputTypeDef:
        """
        Creates a data product.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_data_product)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_data_product)
        """

    def create_data_product_revision(
        self, **kwargs: Unpack[CreateDataProductRevisionInputRequestTypeDef]
    ) -> CreateDataProductRevisionOutputTypeDef:
        """
        Creates a data product revision.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_data_product_revision)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_data_product_revision)
        """

    def create_data_source(
        self, **kwargs: Unpack[CreateDataSourceInputRequestTypeDef]
    ) -> CreateDataSourceOutputTypeDef:
        """
        Creates an Amazon DataZone data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_data_source)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_data_source)
        """

    def create_domain(
        self, **kwargs: Unpack[CreateDomainInputRequestTypeDef]
    ) -> CreateDomainOutputTypeDef:
        """
        Creates an Amazon DataZone domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_domain)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_domain)
        """

    def create_domain_unit(
        self, **kwargs: Unpack[CreateDomainUnitInputRequestTypeDef]
    ) -> CreateDomainUnitOutputTypeDef:
        """
        Creates a domain unit in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_domain_unit)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_domain_unit)
        """

    def create_environment(
        self, **kwargs: Unpack[CreateEnvironmentInputRequestTypeDef]
    ) -> CreateEnvironmentOutputTypeDef:
        """
        Create an Amazon DataZone environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_environment)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_environment)
        """

    def create_environment_action(
        self, **kwargs: Unpack[CreateEnvironmentActionInputRequestTypeDef]
    ) -> CreateEnvironmentActionOutputTypeDef:
        """
        Creates an action for the environment, for example, creates a console link for
        an analytics tool that is available in this
        environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_environment_action)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_environment_action)
        """

    def create_environment_profile(
        self, **kwargs: Unpack[CreateEnvironmentProfileInputRequestTypeDef]
    ) -> CreateEnvironmentProfileOutputTypeDef:
        """
        Creates an Amazon DataZone environment profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_environment_profile)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_environment_profile)
        """

    def create_form_type(
        self, **kwargs: Unpack[CreateFormTypeInputRequestTypeDef]
    ) -> CreateFormTypeOutputTypeDef:
        """
        Creates a metadata form type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_form_type)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_form_type)
        """

    def create_glossary(
        self, **kwargs: Unpack[CreateGlossaryInputRequestTypeDef]
    ) -> CreateGlossaryOutputTypeDef:
        """
        Creates an Amazon DataZone business glossary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_glossary)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_glossary)
        """

    def create_glossary_term(
        self, **kwargs: Unpack[CreateGlossaryTermInputRequestTypeDef]
    ) -> CreateGlossaryTermOutputTypeDef:
        """
        Creates a business glossary term.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_glossary_term)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_glossary_term)
        """

    def create_group_profile(
        self, **kwargs: Unpack[CreateGroupProfileInputRequestTypeDef]
    ) -> CreateGroupProfileOutputTypeDef:
        """
        Creates a group profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_group_profile)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_group_profile)
        """

    def create_listing_change_set(
        self, **kwargs: Unpack[CreateListingChangeSetInputRequestTypeDef]
    ) -> CreateListingChangeSetOutputTypeDef:
        """
        Publishes a listing (a record of an asset at a given time) or removes a listing
        from the
        catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_listing_change_set)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_listing_change_set)
        """

    def create_project(
        self, **kwargs: Unpack[CreateProjectInputRequestTypeDef]
    ) -> CreateProjectOutputTypeDef:
        """
        Creates an Amazon DataZone project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_project)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_project)
        """

    def create_project_membership(
        self, **kwargs: Unpack[CreateProjectMembershipInputRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates a project membership in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_project_membership)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_project_membership)
        """

    def create_subscription_grant(
        self, **kwargs: Unpack[CreateSubscriptionGrantInputRequestTypeDef]
    ) -> CreateSubscriptionGrantOutputTypeDef:
        """
        Creates a subsscription grant in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_subscription_grant)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_subscription_grant)
        """

    def create_subscription_request(
        self, **kwargs: Unpack[CreateSubscriptionRequestInputRequestTypeDef]
    ) -> CreateSubscriptionRequestOutputTypeDef:
        """
        Creates a subscription request in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_subscription_request)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_subscription_request)
        """

    def create_subscription_target(
        self, **kwargs: Unpack[CreateSubscriptionTargetInputRequestTypeDef]
    ) -> CreateSubscriptionTargetOutputTypeDef:
        """
        Creates a subscription target in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_subscription_target)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_subscription_target)
        """

    def create_user_profile(
        self, **kwargs: Unpack[CreateUserProfileInputRequestTypeDef]
    ) -> CreateUserProfileOutputTypeDef:
        """
        Creates a user profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_user_profile)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_user_profile)
        """

    def delete_asset(self, **kwargs: Unpack[DeleteAssetInputRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes an asset in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_asset)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_asset)
        """

    def delete_asset_filter(
        self, **kwargs: Unpack[DeleteAssetFilterInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an asset filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_asset_filter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_asset_filter)
        """

    def delete_asset_type(
        self, **kwargs: Unpack[DeleteAssetTypeInputRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an asset type in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_asset_type)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_asset_type)
        """

    def delete_data_product(
        self, **kwargs: Unpack[DeleteDataProductInputRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a data product in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_data_product)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_data_product)
        """

    def delete_data_source(
        self, **kwargs: Unpack[DeleteDataSourceInputRequestTypeDef]
    ) -> DeleteDataSourceOutputTypeDef:
        """
        Deletes a data source in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_data_source)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_data_source)
        """

    def delete_domain(
        self, **kwargs: Unpack[DeleteDomainInputRequestTypeDef]
    ) -> DeleteDomainOutputTypeDef:
        """
        Deletes a Amazon DataZone domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_domain)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_domain)
        """

    def delete_domain_unit(
        self, **kwargs: Unpack[DeleteDomainUnitInputRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a domain unit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_domain_unit)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_domain_unit)
        """

    def delete_environment(
        self, **kwargs: Unpack[DeleteEnvironmentInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an environment in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_environment)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_environment)
        """

    def delete_environment_action(
        self, **kwargs: Unpack[DeleteEnvironmentActionInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an action for the environment, for example, deletes a console link for
        an analytics tool that is available in this
        environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_environment_action)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_environment_action)
        """

    def delete_environment_blueprint_configuration(
        self, **kwargs: Unpack[DeleteEnvironmentBlueprintConfigurationInputRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the blueprint configuration in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_environment_blueprint_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_environment_blueprint_configuration)
        """

    def delete_environment_profile(
        self, **kwargs: Unpack[DeleteEnvironmentProfileInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an environment profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_environment_profile)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_environment_profile)
        """

    def delete_form_type(
        self, **kwargs: Unpack[DeleteFormTypeInputRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Delets and metadata form type in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_form_type)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_form_type)
        """

    def delete_glossary(
        self, **kwargs: Unpack[DeleteGlossaryInputRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a business glossary in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_glossary)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_glossary)
        """

    def delete_glossary_term(
        self, **kwargs: Unpack[DeleteGlossaryTermInputRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a business glossary term in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_glossary_term)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_glossary_term)
        """

    def delete_listing(self, **kwargs: Unpack[DeleteListingInputRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a listing (a record of an asset at a given time).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_listing)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_listing)
        """

    def delete_project(self, **kwargs: Unpack[DeleteProjectInputRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a project in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_project)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_project)
        """

    def delete_project_membership(
        self, **kwargs: Unpack[DeleteProjectMembershipInputRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes project membership in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_project_membership)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_project_membership)
        """

    def delete_subscription_grant(
        self, **kwargs: Unpack[DeleteSubscriptionGrantInputRequestTypeDef]
    ) -> DeleteSubscriptionGrantOutputTypeDef:
        """
        Deletes and subscription grant in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_subscription_grant)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_subscription_grant)
        """

    def delete_subscription_request(
        self, **kwargs: Unpack[DeleteSubscriptionRequestInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a subscription request in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_subscription_request)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_subscription_request)
        """

    def delete_subscription_target(
        self, **kwargs: Unpack[DeleteSubscriptionTargetInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a subscription target in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_subscription_target)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_subscription_target)
        """

    def delete_time_series_data_points(
        self, **kwargs: Unpack[DeleteTimeSeriesDataPointsInputRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified time series form for the specified asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_time_series_data_points)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_time_series_data_points)
        """

    def disassociate_environment_role(
        self, **kwargs: Unpack[DisassociateEnvironmentRoleInputRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates the environment role in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.disassociate_environment_role)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#disassociate_environment_role)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#generate_presigned_url)
        """

    def get_asset(self, **kwargs: Unpack[GetAssetInputRequestTypeDef]) -> GetAssetOutputTypeDef:
        """
        Gets an Amazon DataZone asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_asset)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_asset)
        """

    def get_asset_filter(
        self, **kwargs: Unpack[GetAssetFilterInputRequestTypeDef]
    ) -> GetAssetFilterOutputTypeDef:
        """
        Gets an asset filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_asset_filter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_asset_filter)
        """

    def get_asset_type(
        self, **kwargs: Unpack[GetAssetTypeInputRequestTypeDef]
    ) -> GetAssetTypeOutputTypeDef:
        """
        Gets an Amazon DataZone asset type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_asset_type)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_asset_type)
        """

    def get_data_product(
        self, **kwargs: Unpack[GetDataProductInputRequestTypeDef]
    ) -> GetDataProductOutputTypeDef:
        """
        Gets the data product.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_data_product)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_data_product)
        """

    def get_data_source(
        self, **kwargs: Unpack[GetDataSourceInputRequestTypeDef]
    ) -> GetDataSourceOutputTypeDef:
        """
        Gets an Amazon DataZone data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_data_source)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_data_source)
        """

    def get_data_source_run(
        self, **kwargs: Unpack[GetDataSourceRunInputRequestTypeDef]
    ) -> GetDataSourceRunOutputTypeDef:
        """
        Gets an Amazon DataZone data source run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_data_source_run)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_data_source_run)
        """

    def get_domain(self, **kwargs: Unpack[GetDomainInputRequestTypeDef]) -> GetDomainOutputTypeDef:
        """
        Gets an Amazon DataZone domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_domain)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_domain)
        """

    def get_domain_unit(
        self, **kwargs: Unpack[GetDomainUnitInputRequestTypeDef]
    ) -> GetDomainUnitOutputTypeDef:
        """
        Gets the details of the specified domain unit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_domain_unit)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_domain_unit)
        """

    def get_environment(
        self, **kwargs: Unpack[GetEnvironmentInputRequestTypeDef]
    ) -> GetEnvironmentOutputTypeDef:
        """
        Gets an Amazon DataZone environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_environment)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_environment)
        """

    def get_environment_action(
        self, **kwargs: Unpack[GetEnvironmentActionInputRequestTypeDef]
    ) -> GetEnvironmentActionOutputTypeDef:
        """
        Gets the specified environment action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_environment_action)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_environment_action)
        """

    def get_environment_blueprint(
        self, **kwargs: Unpack[GetEnvironmentBlueprintInputRequestTypeDef]
    ) -> GetEnvironmentBlueprintOutputTypeDef:
        """
        Gets an Amazon DataZone blueprint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_environment_blueprint)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_environment_blueprint)
        """

    def get_environment_blueprint_configuration(
        self, **kwargs: Unpack[GetEnvironmentBlueprintConfigurationInputRequestTypeDef]
    ) -> GetEnvironmentBlueprintConfigurationOutputTypeDef:
        """
        Gets the blueprint configuration in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_environment_blueprint_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_environment_blueprint_configuration)
        """

    def get_environment_credentials(
        self, **kwargs: Unpack[GetEnvironmentCredentialsInputRequestTypeDef]
    ) -> GetEnvironmentCredentialsOutputTypeDef:
        """
        Gets the credentials of an environment in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_environment_credentials)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_environment_credentials)
        """

    def get_environment_profile(
        self, **kwargs: Unpack[GetEnvironmentProfileInputRequestTypeDef]
    ) -> GetEnvironmentProfileOutputTypeDef:
        """
        Gets an evinronment profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_environment_profile)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_environment_profile)
        """

    def get_form_type(
        self, **kwargs: Unpack[GetFormTypeInputRequestTypeDef]
    ) -> GetFormTypeOutputTypeDef:
        """
        Gets a metadata form type in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_form_type)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_form_type)
        """

    def get_glossary(
        self, **kwargs: Unpack[GetGlossaryInputRequestTypeDef]
    ) -> GetGlossaryOutputTypeDef:
        """
        Gets a business glossary in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_glossary)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_glossary)
        """

    def get_glossary_term(
        self, **kwargs: Unpack[GetGlossaryTermInputRequestTypeDef]
    ) -> GetGlossaryTermOutputTypeDef:
        """
        Gets a business glossary term in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_glossary_term)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_glossary_term)
        """

    def get_group_profile(
        self, **kwargs: Unpack[GetGroupProfileInputRequestTypeDef]
    ) -> GetGroupProfileOutputTypeDef:
        """
        Gets a group profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_group_profile)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_group_profile)
        """

    def get_iam_portal_login_url(
        self, **kwargs: Unpack[GetIamPortalLoginUrlInputRequestTypeDef]
    ) -> GetIamPortalLoginUrlOutputTypeDef:
        """
        Gets the data portal URL for the specified Amazon DataZone domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_iam_portal_login_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_iam_portal_login_url)
        """

    def get_lineage_node(
        self, **kwargs: Unpack[GetLineageNodeInputRequestTypeDef]
    ) -> GetLineageNodeOutputTypeDef:
        """
        Gets the data lineage node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_lineage_node)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_lineage_node)
        """

    def get_listing(
        self, **kwargs: Unpack[GetListingInputRequestTypeDef]
    ) -> GetListingOutputTypeDef:
        """
        Gets a listing (a record of an asset at a given time).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_listing)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_listing)
        """

    def get_metadata_generation_run(
        self, **kwargs: Unpack[GetMetadataGenerationRunInputRequestTypeDef]
    ) -> GetMetadataGenerationRunOutputTypeDef:
        """
        Gets a metadata generation run in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_metadata_generation_run)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_metadata_generation_run)
        """

    def get_project(
        self, **kwargs: Unpack[GetProjectInputRequestTypeDef]
    ) -> GetProjectOutputTypeDef:
        """
        Gets a project in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_project)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_project)
        """

    def get_subscription(
        self, **kwargs: Unpack[GetSubscriptionInputRequestTypeDef]
    ) -> GetSubscriptionOutputTypeDef:
        """
        Gets a subscription in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_subscription)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_subscription)
        """

    def get_subscription_grant(
        self, **kwargs: Unpack[GetSubscriptionGrantInputRequestTypeDef]
    ) -> GetSubscriptionGrantOutputTypeDef:
        """
        Gets the subscription grant in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_subscription_grant)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_subscription_grant)
        """

    def get_subscription_request_details(
        self, **kwargs: Unpack[GetSubscriptionRequestDetailsInputRequestTypeDef]
    ) -> GetSubscriptionRequestDetailsOutputTypeDef:
        """
        Gets the details of the specified subscription request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_subscription_request_details)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_subscription_request_details)
        """

    def get_subscription_target(
        self, **kwargs: Unpack[GetSubscriptionTargetInputRequestTypeDef]
    ) -> GetSubscriptionTargetOutputTypeDef:
        """
        Gets the subscription target in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_subscription_target)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_subscription_target)
        """

    def get_time_series_data_point(
        self, **kwargs: Unpack[GetTimeSeriesDataPointInputRequestTypeDef]
    ) -> GetTimeSeriesDataPointOutputTypeDef:
        """
        Gets the existing data point for the asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_time_series_data_point)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_time_series_data_point)
        """

    def get_user_profile(
        self, **kwargs: Unpack[GetUserProfileInputRequestTypeDef]
    ) -> GetUserProfileOutputTypeDef:
        """
        Gets a user profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_user_profile)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_user_profile)
        """

    def list_asset_filters(
        self, **kwargs: Unpack[ListAssetFiltersInputRequestTypeDef]
    ) -> ListAssetFiltersOutputTypeDef:
        """
        Lists asset filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_asset_filters)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_asset_filters)
        """

    def list_asset_revisions(
        self, **kwargs: Unpack[ListAssetRevisionsInputRequestTypeDef]
    ) -> ListAssetRevisionsOutputTypeDef:
        """
        Lists the revisions for the asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_asset_revisions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_asset_revisions)
        """

    def list_data_product_revisions(
        self, **kwargs: Unpack[ListDataProductRevisionsInputRequestTypeDef]
    ) -> ListDataProductRevisionsOutputTypeDef:
        """
        Lists data product revisions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_data_product_revisions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_data_product_revisions)
        """

    def list_data_source_run_activities(
        self, **kwargs: Unpack[ListDataSourceRunActivitiesInputRequestTypeDef]
    ) -> ListDataSourceRunActivitiesOutputTypeDef:
        """
        Lists data source run activities.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_data_source_run_activities)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_data_source_run_activities)
        """

    def list_data_source_runs(
        self, **kwargs: Unpack[ListDataSourceRunsInputRequestTypeDef]
    ) -> ListDataSourceRunsOutputTypeDef:
        """
        Lists data source runs in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_data_source_runs)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_data_source_runs)
        """

    def list_data_sources(
        self, **kwargs: Unpack[ListDataSourcesInputRequestTypeDef]
    ) -> ListDataSourcesOutputTypeDef:
        """
        Lists data sources in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_data_sources)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_data_sources)
        """

    def list_domain_units_for_parent(
        self, **kwargs: Unpack[ListDomainUnitsForParentInputRequestTypeDef]
    ) -> ListDomainUnitsForParentOutputTypeDef:
        """
        Lists child domain units for the specified parent domain unit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_domain_units_for_parent)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_domain_units_for_parent)
        """

    def list_domains(
        self, **kwargs: Unpack[ListDomainsInputRequestTypeDef]
    ) -> ListDomainsOutputTypeDef:
        """
        Lists Amazon DataZone domains.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_domains)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_domains)
        """

    def list_entity_owners(
        self, **kwargs: Unpack[ListEntityOwnersInputRequestTypeDef]
    ) -> ListEntityOwnersOutputTypeDef:
        """
        Lists the entity (domain units) owners.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_entity_owners)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_entity_owners)
        """

    def list_environment_actions(
        self, **kwargs: Unpack[ListEnvironmentActionsInputRequestTypeDef]
    ) -> ListEnvironmentActionsOutputTypeDef:
        """
        Lists existing environment actions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_environment_actions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_environment_actions)
        """

    def list_environment_blueprint_configurations(
        self, **kwargs: Unpack[ListEnvironmentBlueprintConfigurationsInputRequestTypeDef]
    ) -> ListEnvironmentBlueprintConfigurationsOutputTypeDef:
        """
        Lists blueprint configurations for a Amazon DataZone environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_environment_blueprint_configurations)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_environment_blueprint_configurations)
        """

    def list_environment_blueprints(
        self, **kwargs: Unpack[ListEnvironmentBlueprintsInputRequestTypeDef]
    ) -> ListEnvironmentBlueprintsOutputTypeDef:
        """
        Lists blueprints in an Amazon DataZone environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_environment_blueprints)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_environment_blueprints)
        """

    def list_environment_profiles(
        self, **kwargs: Unpack[ListEnvironmentProfilesInputRequestTypeDef]
    ) -> ListEnvironmentProfilesOutputTypeDef:
        """
        Lists Amazon DataZone environment profiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_environment_profiles)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_environment_profiles)
        """

    def list_environments(
        self, **kwargs: Unpack[ListEnvironmentsInputRequestTypeDef]
    ) -> ListEnvironmentsOutputTypeDef:
        """
        Lists Amazon DataZone environments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_environments)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_environments)
        """

    def list_lineage_node_history(
        self, **kwargs: Unpack[ListLineageNodeHistoryInputRequestTypeDef]
    ) -> ListLineageNodeHistoryOutputTypeDef:
        """
        Lists the history of the specified data lineage node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_lineage_node_history)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_lineage_node_history)
        """

    def list_metadata_generation_runs(
        self, **kwargs: Unpack[ListMetadataGenerationRunsInputRequestTypeDef]
    ) -> ListMetadataGenerationRunsOutputTypeDef:
        """
        Lists all metadata generation runs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_metadata_generation_runs)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_metadata_generation_runs)
        """

    def list_notifications(
        self, **kwargs: Unpack[ListNotificationsInputRequestTypeDef]
    ) -> ListNotificationsOutputTypeDef:
        """
        Lists all Amazon DataZone notifications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_notifications)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_notifications)
        """

    def list_policy_grants(
        self, **kwargs: Unpack[ListPolicyGrantsInputRequestTypeDef]
    ) -> ListPolicyGrantsOutputTypeDef:
        """
        Lists policy grants.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_policy_grants)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_policy_grants)
        """

    def list_project_memberships(
        self, **kwargs: Unpack[ListProjectMembershipsInputRequestTypeDef]
    ) -> ListProjectMembershipsOutputTypeDef:
        """
        Lists all members of the specified project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_project_memberships)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_project_memberships)
        """

    def list_projects(
        self, **kwargs: Unpack[ListProjectsInputRequestTypeDef]
    ) -> ListProjectsOutputTypeDef:
        """
        Lists Amazon DataZone projects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_projects)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_projects)
        """

    def list_subscription_grants(
        self, **kwargs: Unpack[ListSubscriptionGrantsInputRequestTypeDef]
    ) -> ListSubscriptionGrantsOutputTypeDef:
        """
        Lists subscription grants.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_subscription_grants)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_subscription_grants)
        """

    def list_subscription_requests(
        self, **kwargs: Unpack[ListSubscriptionRequestsInputRequestTypeDef]
    ) -> ListSubscriptionRequestsOutputTypeDef:
        """
        Lists Amazon DataZone subscription requests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_subscription_requests)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_subscription_requests)
        """

    def list_subscription_targets(
        self, **kwargs: Unpack[ListSubscriptionTargetsInputRequestTypeDef]
    ) -> ListSubscriptionTargetsOutputTypeDef:
        """
        Lists subscription targets in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_subscription_targets)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_subscription_targets)
        """

    def list_subscriptions(
        self, **kwargs: Unpack[ListSubscriptionsInputRequestTypeDef]
    ) -> ListSubscriptionsOutputTypeDef:
        """
        Lists subscriptions in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_subscriptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_subscriptions)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists tags for the specified resource in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_tags_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_tags_for_resource)
        """

    def list_time_series_data_points(
        self, **kwargs: Unpack[ListTimeSeriesDataPointsInputRequestTypeDef]
    ) -> ListTimeSeriesDataPointsOutputTypeDef:
        """
        Lists time series data points.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_time_series_data_points)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_time_series_data_points)
        """

    def post_lineage_event(
        self, **kwargs: Unpack[PostLineageEventInputRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Posts a data lineage event.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.post_lineage_event)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#post_lineage_event)
        """

    def post_time_series_data_points(
        self, **kwargs: Unpack[PostTimeSeriesDataPointsInputRequestTypeDef]
    ) -> PostTimeSeriesDataPointsOutputTypeDef:
        """
        Posts time series data points to Amazon DataZone for the specified asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.post_time_series_data_points)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#post_time_series_data_points)
        """

    def put_environment_blueprint_configuration(
        self, **kwargs: Unpack[PutEnvironmentBlueprintConfigurationInputRequestTypeDef]
    ) -> PutEnvironmentBlueprintConfigurationOutputTypeDef:
        """
        Writes the configuration for the specified environment blueprint in Amazon
        DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.put_environment_blueprint_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#put_environment_blueprint_configuration)
        """

    def reject_predictions(
        self, **kwargs: Unpack[RejectPredictionsInputRequestTypeDef]
    ) -> RejectPredictionsOutputTypeDef:
        """
        Rejects automatically generated business-friendly metadata for your Amazon
        DataZone
        assets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.reject_predictions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#reject_predictions)
        """

    def reject_subscription_request(
        self, **kwargs: Unpack[RejectSubscriptionRequestInputRequestTypeDef]
    ) -> RejectSubscriptionRequestOutputTypeDef:
        """
        Rejects the specified subscription request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.reject_subscription_request)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#reject_subscription_request)
        """

    def remove_entity_owner(
        self, **kwargs: Unpack[RemoveEntityOwnerInputRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes an owner from an entity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.remove_entity_owner)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#remove_entity_owner)
        """

    def remove_policy_grant(
        self, **kwargs: Unpack[RemovePolicyGrantInputRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes a policy grant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.remove_policy_grant)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#remove_policy_grant)
        """

    def revoke_subscription(
        self, **kwargs: Unpack[RevokeSubscriptionInputRequestTypeDef]
    ) -> RevokeSubscriptionOutputTypeDef:
        """
        Revokes a specified subscription in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.revoke_subscription)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#revoke_subscription)
        """

    def search(self, **kwargs: Unpack[SearchInputRequestTypeDef]) -> SearchOutputTypeDef:
        """
        Searches for assets in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.search)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#search)
        """

    def search_group_profiles(
        self, **kwargs: Unpack[SearchGroupProfilesInputRequestTypeDef]
    ) -> SearchGroupProfilesOutputTypeDef:
        """
        Searches group profiles in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.search_group_profiles)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#search_group_profiles)
        """

    def search_listings(
        self, **kwargs: Unpack[SearchListingsInputRequestTypeDef]
    ) -> SearchListingsOutputTypeDef:
        """
        Searches listings (records of an asset at a given time) in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.search_listings)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#search_listings)
        """

    def search_types(
        self, **kwargs: Unpack[SearchTypesInputRequestTypeDef]
    ) -> SearchTypesOutputTypeDef:
        """
        Searches for types in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.search_types)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#search_types)
        """

    def search_user_profiles(
        self, **kwargs: Unpack[SearchUserProfilesInputRequestTypeDef]
    ) -> SearchUserProfilesOutputTypeDef:
        """
        Searches user profiles in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.search_user_profiles)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#search_user_profiles)
        """

    def start_data_source_run(
        self, **kwargs: Unpack[StartDataSourceRunInputRequestTypeDef]
    ) -> StartDataSourceRunOutputTypeDef:
        """
        Start the run of the specified data source in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.start_data_source_run)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#start_data_source_run)
        """

    def start_metadata_generation_run(
        self, **kwargs: Unpack[StartMetadataGenerationRunInputRequestTypeDef]
    ) -> StartMetadataGenerationRunOutputTypeDef:
        """
        Starts the metadata generation run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.start_metadata_generation_run)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#start_metadata_generation_run)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Tags a resource in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Untags a resource in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#untag_resource)
        """

    def update_asset_filter(
        self, **kwargs: Unpack[UpdateAssetFilterInputRequestTypeDef]
    ) -> UpdateAssetFilterOutputTypeDef:
        """
        Updates an asset filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.update_asset_filter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_asset_filter)
        """

    def update_data_source(
        self, **kwargs: Unpack[UpdateDataSourceInputRequestTypeDef]
    ) -> UpdateDataSourceOutputTypeDef:
        """
        Updates the specified data source in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.update_data_source)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_data_source)
        """

    def update_domain(
        self, **kwargs: Unpack[UpdateDomainInputRequestTypeDef]
    ) -> UpdateDomainOutputTypeDef:
        """
        Updates a Amazon DataZone domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.update_domain)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_domain)
        """

    def update_domain_unit(
        self, **kwargs: Unpack[UpdateDomainUnitInputRequestTypeDef]
    ) -> UpdateDomainUnitOutputTypeDef:
        """
        Updates the domain unit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.update_domain_unit)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_domain_unit)
        """

    def update_environment(
        self, **kwargs: Unpack[UpdateEnvironmentInputRequestTypeDef]
    ) -> UpdateEnvironmentOutputTypeDef:
        """
        Updates the specified environment in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.update_environment)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_environment)
        """

    def update_environment_action(
        self, **kwargs: Unpack[UpdateEnvironmentActionInputRequestTypeDef]
    ) -> UpdateEnvironmentActionOutputTypeDef:
        """
        Updates an environment action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.update_environment_action)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_environment_action)
        """

    def update_environment_profile(
        self, **kwargs: Unpack[UpdateEnvironmentProfileInputRequestTypeDef]
    ) -> UpdateEnvironmentProfileOutputTypeDef:
        """
        Updates the specified environment profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.update_environment_profile)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_environment_profile)
        """

    def update_glossary(
        self, **kwargs: Unpack[UpdateGlossaryInputRequestTypeDef]
    ) -> UpdateGlossaryOutputTypeDef:
        """
        Updates the business glossary in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.update_glossary)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_glossary)
        """

    def update_glossary_term(
        self, **kwargs: Unpack[UpdateGlossaryTermInputRequestTypeDef]
    ) -> UpdateGlossaryTermOutputTypeDef:
        """
        Updates a business glossary term in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.update_glossary_term)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_glossary_term)
        """

    def update_group_profile(
        self, **kwargs: Unpack[UpdateGroupProfileInputRequestTypeDef]
    ) -> UpdateGroupProfileOutputTypeDef:
        """
        Updates the specified group profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.update_group_profile)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_group_profile)
        """

    def update_project(
        self, **kwargs: Unpack[UpdateProjectInputRequestTypeDef]
    ) -> UpdateProjectOutputTypeDef:
        """
        Updates the specified project in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.update_project)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_project)
        """

    def update_subscription_grant_status(
        self, **kwargs: Unpack[UpdateSubscriptionGrantStatusInputRequestTypeDef]
    ) -> UpdateSubscriptionGrantStatusOutputTypeDef:
        """
        Updates the status of the specified subscription grant status in Amazon
        DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.update_subscription_grant_status)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_subscription_grant_status)
        """

    def update_subscription_request(
        self, **kwargs: Unpack[UpdateSubscriptionRequestInputRequestTypeDef]
    ) -> UpdateSubscriptionRequestOutputTypeDef:
        """
        Updates a specified subscription request in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.update_subscription_request)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_subscription_request)
        """

    def update_subscription_target(
        self, **kwargs: Unpack[UpdateSubscriptionTargetInputRequestTypeDef]
    ) -> UpdateSubscriptionTargetOutputTypeDef:
        """
        Updates the specified subscription target in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.update_subscription_target)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_subscription_target)
        """

    def update_user_profile(
        self, **kwargs: Unpack[UpdateUserProfileInputRequestTypeDef]
    ) -> UpdateUserProfileOutputTypeDef:
        """
        Updates the specified user profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.update_user_profile)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_user_profile)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_asset_filters"]
    ) -> ListAssetFiltersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_asset_revisions"]
    ) -> ListAssetRevisionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_product_revisions"]
    ) -> ListDataProductRevisionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_source_run_activities"]
    ) -> ListDataSourceRunActivitiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_source_runs"]
    ) -> ListDataSourceRunsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_sources"]
    ) -> ListDataSourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_domain_units_for_parent"]
    ) -> ListDomainUnitsForParentPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_domains"]) -> ListDomainsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_entity_owners"]
    ) -> ListEntityOwnersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_environment_actions"]
    ) -> ListEnvironmentActionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_environment_blueprint_configurations"]
    ) -> ListEnvironmentBlueprintConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_environment_blueprints"]
    ) -> ListEnvironmentBlueprintsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_environment_profiles"]
    ) -> ListEnvironmentProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_environments"]
    ) -> ListEnvironmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_lineage_node_history"]
    ) -> ListLineageNodeHistoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_metadata_generation_runs"]
    ) -> ListMetadataGenerationRunsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_notifications"]
    ) -> ListNotificationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_policy_grants"]
    ) -> ListPolicyGrantsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_project_memberships"]
    ) -> ListProjectMembershipsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_projects"]) -> ListProjectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_subscription_grants"]
    ) -> ListSubscriptionGrantsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_subscription_requests"]
    ) -> ListSubscriptionRequestsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_subscription_targets"]
    ) -> ListSubscriptionTargetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_subscriptions"]
    ) -> ListSubscriptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_time_series_data_points"]
    ) -> ListTimeSeriesDataPointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search"]) -> SearchPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_group_profiles"]
    ) -> SearchGroupProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_listings"]) -> SearchListingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_types"]) -> SearchTypesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_user_profiles"]
    ) -> SearchUserProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """
