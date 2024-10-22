"""
Type annotations for kendra service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_kendra.client import KendraClient

    session = Session()
    client: KendraClient = session.client("kendra")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
    AssociateEntitiesToExperienceRequestRequestTypeDef,
    AssociateEntitiesToExperienceResponseTypeDef,
    AssociatePersonasToEntitiesRequestRequestTypeDef,
    AssociatePersonasToEntitiesResponseTypeDef,
    BatchDeleteDocumentRequestRequestTypeDef,
    BatchDeleteDocumentResponseTypeDef,
    BatchDeleteFeaturedResultsSetRequestRequestTypeDef,
    BatchDeleteFeaturedResultsSetResponseTypeDef,
    BatchGetDocumentStatusRequestRequestTypeDef,
    BatchGetDocumentStatusResponseTypeDef,
    BatchPutDocumentRequestRequestTypeDef,
    BatchPutDocumentResponseTypeDef,
    ClearQuerySuggestionsRequestRequestTypeDef,
    CreateAccessControlConfigurationRequestRequestTypeDef,
    CreateAccessControlConfigurationResponseTypeDef,
    CreateDataSourceRequestRequestTypeDef,
    CreateDataSourceResponseTypeDef,
    CreateExperienceRequestRequestTypeDef,
    CreateExperienceResponseTypeDef,
    CreateFaqRequestRequestTypeDef,
    CreateFaqResponseTypeDef,
    CreateFeaturedResultsSetRequestRequestTypeDef,
    CreateFeaturedResultsSetResponseTypeDef,
    CreateIndexRequestRequestTypeDef,
    CreateIndexResponseTypeDef,
    CreateQuerySuggestionsBlockListRequestRequestTypeDef,
    CreateQuerySuggestionsBlockListResponseTypeDef,
    CreateThesaurusRequestRequestTypeDef,
    CreateThesaurusResponseTypeDef,
    DeleteAccessControlConfigurationRequestRequestTypeDef,
    DeleteDataSourceRequestRequestTypeDef,
    DeleteExperienceRequestRequestTypeDef,
    DeleteFaqRequestRequestTypeDef,
    DeleteIndexRequestRequestTypeDef,
    DeletePrincipalMappingRequestRequestTypeDef,
    DeleteQuerySuggestionsBlockListRequestRequestTypeDef,
    DeleteThesaurusRequestRequestTypeDef,
    DescribeAccessControlConfigurationRequestRequestTypeDef,
    DescribeAccessControlConfigurationResponseTypeDef,
    DescribeDataSourceRequestRequestTypeDef,
    DescribeDataSourceResponseTypeDef,
    DescribeExperienceRequestRequestTypeDef,
    DescribeExperienceResponseTypeDef,
    DescribeFaqRequestRequestTypeDef,
    DescribeFaqResponseTypeDef,
    DescribeFeaturedResultsSetRequestRequestTypeDef,
    DescribeFeaturedResultsSetResponseTypeDef,
    DescribeIndexRequestRequestTypeDef,
    DescribeIndexResponseTypeDef,
    DescribePrincipalMappingRequestRequestTypeDef,
    DescribePrincipalMappingResponseTypeDef,
    DescribeQuerySuggestionsBlockListRequestRequestTypeDef,
    DescribeQuerySuggestionsBlockListResponseTypeDef,
    DescribeQuerySuggestionsConfigRequestRequestTypeDef,
    DescribeQuerySuggestionsConfigResponseTypeDef,
    DescribeThesaurusRequestRequestTypeDef,
    DescribeThesaurusResponseTypeDef,
    DisassociateEntitiesFromExperienceRequestRequestTypeDef,
    DisassociateEntitiesFromExperienceResponseTypeDef,
    DisassociatePersonasFromEntitiesRequestRequestTypeDef,
    DisassociatePersonasFromEntitiesResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    GetQuerySuggestionsRequestRequestTypeDef,
    GetQuerySuggestionsResponseTypeDef,
    GetSnapshotsRequestRequestTypeDef,
    GetSnapshotsResponseTypeDef,
    ListAccessControlConfigurationsRequestRequestTypeDef,
    ListAccessControlConfigurationsResponseTypeDef,
    ListDataSourcesRequestRequestTypeDef,
    ListDataSourcesResponseTypeDef,
    ListDataSourceSyncJobsRequestRequestTypeDef,
    ListDataSourceSyncJobsResponseTypeDef,
    ListEntityPersonasRequestRequestTypeDef,
    ListEntityPersonasResponseTypeDef,
    ListExperienceEntitiesRequestRequestTypeDef,
    ListExperienceEntitiesResponseTypeDef,
    ListExperiencesRequestRequestTypeDef,
    ListExperiencesResponseTypeDef,
    ListFaqsRequestRequestTypeDef,
    ListFaqsResponseTypeDef,
    ListFeaturedResultsSetsRequestRequestTypeDef,
    ListFeaturedResultsSetsResponseTypeDef,
    ListGroupsOlderThanOrderingIdRequestRequestTypeDef,
    ListGroupsOlderThanOrderingIdResponseTypeDef,
    ListIndicesRequestRequestTypeDef,
    ListIndicesResponseTypeDef,
    ListQuerySuggestionsBlockListsRequestRequestTypeDef,
    ListQuerySuggestionsBlockListsResponseTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListThesauriRequestRequestTypeDef,
    ListThesauriResponseTypeDef,
    PutPrincipalMappingRequestRequestTypeDef,
    QueryRequestRequestTypeDef,
    QueryResultTypeDef,
    RetrieveRequestRequestTypeDef,
    RetrieveResultTypeDef,
    StartDataSourceSyncJobRequestRequestTypeDef,
    StartDataSourceSyncJobResponseTypeDef,
    StopDataSourceSyncJobRequestRequestTypeDef,
    SubmitFeedbackRequestRequestTypeDef,
    TagResourceRequestRequestTypeDef,
    UntagResourceRequestRequestTypeDef,
    UpdateAccessControlConfigurationRequestRequestTypeDef,
    UpdateDataSourceRequestRequestTypeDef,
    UpdateExperienceRequestRequestTypeDef,
    UpdateFeaturedResultsSetRequestRequestTypeDef,
    UpdateFeaturedResultsSetResponseTypeDef,
    UpdateIndexRequestRequestTypeDef,
    UpdateQuerySuggestionsBlockListRequestRequestTypeDef,
    UpdateQuerySuggestionsConfigRequestRequestTypeDef,
    UpdateThesaurusRequestRequestTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack


__all__ = ("KendraClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    FeaturedResultsConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    ResourceAlreadyExistException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceUnavailableException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class KendraClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        KendraClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#exceptions)
        """

    def associate_entities_to_experience(
        self, **kwargs: Unpack[AssociateEntitiesToExperienceRequestRequestTypeDef]
    ) -> AssociateEntitiesToExperienceResponseTypeDef:
        """
        Grants users or groups in your IAM Identity Center identity source access to
        your Amazon Kendra
        experience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.associate_entities_to_experience)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#associate_entities_to_experience)
        """

    def associate_personas_to_entities(
        self, **kwargs: Unpack[AssociatePersonasToEntitiesRequestRequestTypeDef]
    ) -> AssociatePersonasToEntitiesResponseTypeDef:
        """
        Defines the specific permissions of users or groups in your IAM Identity Center
        identity source with access to your Amazon Kendra
        experience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.associate_personas_to_entities)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#associate_personas_to_entities)
        """

    def batch_delete_document(
        self, **kwargs: Unpack[BatchDeleteDocumentRequestRequestTypeDef]
    ) -> BatchDeleteDocumentResponseTypeDef:
        """
        Removes one or more documents from an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.batch_delete_document)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#batch_delete_document)
        """

    def batch_delete_featured_results_set(
        self, **kwargs: Unpack[BatchDeleteFeaturedResultsSetRequestRequestTypeDef]
    ) -> BatchDeleteFeaturedResultsSetResponseTypeDef:
        """
        Removes one or more sets of featured results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.batch_delete_featured_results_set)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#batch_delete_featured_results_set)
        """

    def batch_get_document_status(
        self, **kwargs: Unpack[BatchGetDocumentStatusRequestRequestTypeDef]
    ) -> BatchGetDocumentStatusResponseTypeDef:
        """
        Returns the indexing status for one or more documents submitted with the
        [BatchPutDocument](https://docs.aws.amazon.com/kendra/latest/dg/API_BatchPutDocument.html)
        API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.batch_get_document_status)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#batch_get_document_status)
        """

    def batch_put_document(
        self, **kwargs: Unpack[BatchPutDocumentRequestRequestTypeDef]
    ) -> BatchPutDocumentResponseTypeDef:
        """
        Adds one or more documents to an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.batch_put_document)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#batch_put_document)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#can_paginate)
        """

    def clear_query_suggestions(
        self, **kwargs: Unpack[ClearQuerySuggestionsRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Clears existing query suggestions from an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.clear_query_suggestions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#clear_query_suggestions)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#close)
        """

    def create_access_control_configuration(
        self, **kwargs: Unpack[CreateAccessControlConfigurationRequestRequestTypeDef]
    ) -> CreateAccessControlConfigurationResponseTypeDef:
        """
        Creates an access configuration for your documents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.create_access_control_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#create_access_control_configuration)
        """

    def create_data_source(
        self, **kwargs: Unpack[CreateDataSourceRequestRequestTypeDef]
    ) -> CreateDataSourceResponseTypeDef:
        """
        Creates a data source connector that you want to use with an Amazon Kendra
        index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.create_data_source)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#create_data_source)
        """

    def create_experience(
        self, **kwargs: Unpack[CreateExperienceRequestRequestTypeDef]
    ) -> CreateExperienceResponseTypeDef:
        """
        Creates an Amazon Kendra experience such as a search application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.create_experience)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#create_experience)
        """

    def create_faq(
        self, **kwargs: Unpack[CreateFaqRequestRequestTypeDef]
    ) -> CreateFaqResponseTypeDef:
        """
        Creates a set of frequently ask questions (FAQs) using a specified FAQ file
        stored in an Amazon S3
        bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.create_faq)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#create_faq)
        """

    def create_featured_results_set(
        self, **kwargs: Unpack[CreateFeaturedResultsSetRequestRequestTypeDef]
    ) -> CreateFeaturedResultsSetResponseTypeDef:
        """
        Creates a set of featured results to display at the top of the search results
        page.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.create_featured_results_set)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#create_featured_results_set)
        """

    def create_index(
        self, **kwargs: Unpack[CreateIndexRequestRequestTypeDef]
    ) -> CreateIndexResponseTypeDef:
        """
        Creates an Amazon Kendra index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.create_index)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#create_index)
        """

    def create_query_suggestions_block_list(
        self, **kwargs: Unpack[CreateQuerySuggestionsBlockListRequestRequestTypeDef]
    ) -> CreateQuerySuggestionsBlockListResponseTypeDef:
        """
        Creates a block list to exlcude certain queries from suggestions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.create_query_suggestions_block_list)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#create_query_suggestions_block_list)
        """

    def create_thesaurus(
        self, **kwargs: Unpack[CreateThesaurusRequestRequestTypeDef]
    ) -> CreateThesaurusResponseTypeDef:
        """
        Creates a thesaurus for an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.create_thesaurus)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#create_thesaurus)
        """

    def delete_access_control_configuration(
        self, **kwargs: Unpack[DeleteAccessControlConfigurationRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an access control configuration that you created for your documents in
        an
        index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.delete_access_control_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#delete_access_control_configuration)
        """

    def delete_data_source(
        self, **kwargs: Unpack[DeleteDataSourceRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an Amazon Kendra data source connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.delete_data_source)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#delete_data_source)
        """

    def delete_experience(
        self, **kwargs: Unpack[DeleteExperienceRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes your Amazon Kendra experience such as a search application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.delete_experience)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#delete_experience)
        """

    def delete_faq(
        self, **kwargs: Unpack[DeleteFaqRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes an FAQ from an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.delete_faq)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#delete_faq)
        """

    def delete_index(
        self, **kwargs: Unpack[DeleteIndexRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an Amazon Kendra index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.delete_index)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#delete_index)
        """

    def delete_principal_mapping(
        self, **kwargs: Unpack[DeletePrincipalMappingRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a group so that all users and sub groups that belong to the group can
        no longer access documents only available to that
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.delete_principal_mapping)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#delete_principal_mapping)
        """

    def delete_query_suggestions_block_list(
        self, **kwargs: Unpack[DeleteQuerySuggestionsBlockListRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a block list used for query suggestions for an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.delete_query_suggestions_block_list)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#delete_query_suggestions_block_list)
        """

    def delete_thesaurus(
        self, **kwargs: Unpack[DeleteThesaurusRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an Amazon Kendra thesaurus.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.delete_thesaurus)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#delete_thesaurus)
        """

    def describe_access_control_configuration(
        self, **kwargs: Unpack[DescribeAccessControlConfigurationRequestRequestTypeDef]
    ) -> DescribeAccessControlConfigurationResponseTypeDef:
        """
        Gets information about an access control configuration that you created for
        your documents in an
        index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.describe_access_control_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#describe_access_control_configuration)
        """

    def describe_data_source(
        self, **kwargs: Unpack[DescribeDataSourceRequestRequestTypeDef]
    ) -> DescribeDataSourceResponseTypeDef:
        """
        Gets information about an Amazon Kendra data source connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.describe_data_source)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#describe_data_source)
        """

    def describe_experience(
        self, **kwargs: Unpack[DescribeExperienceRequestRequestTypeDef]
    ) -> DescribeExperienceResponseTypeDef:
        """
        Gets information about your Amazon Kendra experience such as a search
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.describe_experience)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#describe_experience)
        """

    def describe_faq(
        self, **kwargs: Unpack[DescribeFaqRequestRequestTypeDef]
    ) -> DescribeFaqResponseTypeDef:
        """
        Gets information about an FAQ list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.describe_faq)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#describe_faq)
        """

    def describe_featured_results_set(
        self, **kwargs: Unpack[DescribeFeaturedResultsSetRequestRequestTypeDef]
    ) -> DescribeFeaturedResultsSetResponseTypeDef:
        """
        Gets information about a set of featured results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.describe_featured_results_set)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#describe_featured_results_set)
        """

    def describe_index(
        self, **kwargs: Unpack[DescribeIndexRequestRequestTypeDef]
    ) -> DescribeIndexResponseTypeDef:
        """
        Gets information about an Amazon Kendra index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.describe_index)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#describe_index)
        """

    def describe_principal_mapping(
        self, **kwargs: Unpack[DescribePrincipalMappingRequestRequestTypeDef]
    ) -> DescribePrincipalMappingResponseTypeDef:
        """
        Describes the processing of `PUT` and `DELETE` actions for mapping users to
        their
        groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.describe_principal_mapping)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#describe_principal_mapping)
        """

    def describe_query_suggestions_block_list(
        self, **kwargs: Unpack[DescribeQuerySuggestionsBlockListRequestRequestTypeDef]
    ) -> DescribeQuerySuggestionsBlockListResponseTypeDef:
        """
        Gets information about a block list used for query suggestions for an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.describe_query_suggestions_block_list)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#describe_query_suggestions_block_list)
        """

    def describe_query_suggestions_config(
        self, **kwargs: Unpack[DescribeQuerySuggestionsConfigRequestRequestTypeDef]
    ) -> DescribeQuerySuggestionsConfigResponseTypeDef:
        """
        Gets information on the settings of query suggestions for an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.describe_query_suggestions_config)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#describe_query_suggestions_config)
        """

    def describe_thesaurus(
        self, **kwargs: Unpack[DescribeThesaurusRequestRequestTypeDef]
    ) -> DescribeThesaurusResponseTypeDef:
        """
        Gets information about an Amazon Kendra thesaurus.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.describe_thesaurus)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#describe_thesaurus)
        """

    def disassociate_entities_from_experience(
        self, **kwargs: Unpack[DisassociateEntitiesFromExperienceRequestRequestTypeDef]
    ) -> DisassociateEntitiesFromExperienceResponseTypeDef:
        """
        Prevents users or groups in your IAM Identity Center identity source from
        accessing your Amazon Kendra
        experience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.disassociate_entities_from_experience)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#disassociate_entities_from_experience)
        """

    def disassociate_personas_from_entities(
        self, **kwargs: Unpack[DisassociatePersonasFromEntitiesRequestRequestTypeDef]
    ) -> DisassociatePersonasFromEntitiesResponseTypeDef:
        """
        Removes the specific permissions of users or groups in your IAM Identity Center
        identity source with access to your Amazon Kendra
        experience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.disassociate_personas_from_entities)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#disassociate_personas_from_entities)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#generate_presigned_url)
        """

    def get_query_suggestions(
        self, **kwargs: Unpack[GetQuerySuggestionsRequestRequestTypeDef]
    ) -> GetQuerySuggestionsResponseTypeDef:
        """
        Fetches the queries that are suggested to your users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.get_query_suggestions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#get_query_suggestions)
        """

    def get_snapshots(
        self, **kwargs: Unpack[GetSnapshotsRequestRequestTypeDef]
    ) -> GetSnapshotsResponseTypeDef:
        """
        Retrieves search metrics data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.get_snapshots)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#get_snapshots)
        """

    def list_access_control_configurations(
        self, **kwargs: Unpack[ListAccessControlConfigurationsRequestRequestTypeDef]
    ) -> ListAccessControlConfigurationsResponseTypeDef:
        """
        Lists one or more access control configurations for an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.list_access_control_configurations)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#list_access_control_configurations)
        """

    def list_data_source_sync_jobs(
        self, **kwargs: Unpack[ListDataSourceSyncJobsRequestRequestTypeDef]
    ) -> ListDataSourceSyncJobsResponseTypeDef:
        """
        Gets statistics about synchronizing a data source connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.list_data_source_sync_jobs)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#list_data_source_sync_jobs)
        """

    def list_data_sources(
        self, **kwargs: Unpack[ListDataSourcesRequestRequestTypeDef]
    ) -> ListDataSourcesResponseTypeDef:
        """
        Lists the data source connectors that you have created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.list_data_sources)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#list_data_sources)
        """

    def list_entity_personas(
        self, **kwargs: Unpack[ListEntityPersonasRequestRequestTypeDef]
    ) -> ListEntityPersonasResponseTypeDef:
        """
        Lists specific permissions of users and groups with access to your Amazon
        Kendra
        experience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.list_entity_personas)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#list_entity_personas)
        """

    def list_experience_entities(
        self, **kwargs: Unpack[ListExperienceEntitiesRequestRequestTypeDef]
    ) -> ListExperienceEntitiesResponseTypeDef:
        """
        Lists users or groups in your IAM Identity Center identity source that are
        granted access to your Amazon Kendra
        experience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.list_experience_entities)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#list_experience_entities)
        """

    def list_experiences(
        self, **kwargs: Unpack[ListExperiencesRequestRequestTypeDef]
    ) -> ListExperiencesResponseTypeDef:
        """
        Lists one or more Amazon Kendra experiences.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.list_experiences)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#list_experiences)
        """

    def list_faqs(self, **kwargs: Unpack[ListFaqsRequestRequestTypeDef]) -> ListFaqsResponseTypeDef:
        """
        Gets a list of FAQ lists associated with an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.list_faqs)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#list_faqs)
        """

    def list_featured_results_sets(
        self, **kwargs: Unpack[ListFeaturedResultsSetsRequestRequestTypeDef]
    ) -> ListFeaturedResultsSetsResponseTypeDef:
        """
        Lists all your sets of featured results for a given index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.list_featured_results_sets)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#list_featured_results_sets)
        """

    def list_groups_older_than_ordering_id(
        self, **kwargs: Unpack[ListGroupsOlderThanOrderingIdRequestRequestTypeDef]
    ) -> ListGroupsOlderThanOrderingIdResponseTypeDef:
        """
        Provides a list of groups that are mapped to users before a given ordering or
        timestamp
        identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.list_groups_older_than_ordering_id)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#list_groups_older_than_ordering_id)
        """

    def list_indices(
        self, **kwargs: Unpack[ListIndicesRequestRequestTypeDef]
    ) -> ListIndicesResponseTypeDef:
        """
        Lists the Amazon Kendra indexes that you created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.list_indices)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#list_indices)
        """

    def list_query_suggestions_block_lists(
        self, **kwargs: Unpack[ListQuerySuggestionsBlockListsRequestRequestTypeDef]
    ) -> ListQuerySuggestionsBlockListsResponseTypeDef:
        """
        Lists the block lists used for query suggestions for an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.list_query_suggestions_block_lists)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#list_query_suggestions_block_lists)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Gets a list of tags associated with a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.list_tags_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#list_tags_for_resource)
        """

    def list_thesauri(
        self, **kwargs: Unpack[ListThesauriRequestRequestTypeDef]
    ) -> ListThesauriResponseTypeDef:
        """
        Lists the thesauri for an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.list_thesauri)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#list_thesauri)
        """

    def put_principal_mapping(
        self, **kwargs: Unpack[PutPrincipalMappingRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Maps users to their groups so that you only need to provide the user ID when
        you issue the
        query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.put_principal_mapping)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#put_principal_mapping)
        """

    def query(self, **kwargs: Unpack[QueryRequestRequestTypeDef]) -> QueryResultTypeDef:
        """
        Searches an index given an input query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.query)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#query)
        """

    def retrieve(self, **kwargs: Unpack[RetrieveRequestRequestTypeDef]) -> RetrieveResultTypeDef:
        """
        Retrieves relevant passages or text excerpts given an input query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.retrieve)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#retrieve)
        """

    def start_data_source_sync_job(
        self, **kwargs: Unpack[StartDataSourceSyncJobRequestRequestTypeDef]
    ) -> StartDataSourceSyncJobResponseTypeDef:
        """
        Starts a synchronization job for a data source connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.start_data_source_sync_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#start_data_source_sync_job)
        """

    def stop_data_source_sync_job(
        self, **kwargs: Unpack[StopDataSourceSyncJobRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Stops a synchronization job that is currently running.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.stop_data_source_sync_job)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#stop_data_source_sync_job)
        """

    def submit_feedback(
        self, **kwargs: Unpack[SubmitFeedbackRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Enables you to provide feedback to Amazon Kendra to improve the performance of
        your
        index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.submit_feedback)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#submit_feedback)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds the specified tag to the specified index, FAQ, or data source resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes a tag from an index, FAQ, or a data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#untag_resource)
        """

    def update_access_control_configuration(
        self, **kwargs: Unpack[UpdateAccessControlConfigurationRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates an access control configuration for your documents in an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.update_access_control_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#update_access_control_configuration)
        """

    def update_data_source(
        self, **kwargs: Unpack[UpdateDataSourceRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates an Amazon Kendra data source connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.update_data_source)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#update_data_source)
        """

    def update_experience(
        self, **kwargs: Unpack[UpdateExperienceRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates your Amazon Kendra experience such as a search application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.update_experience)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#update_experience)
        """

    def update_featured_results_set(
        self, **kwargs: Unpack[UpdateFeaturedResultsSetRequestRequestTypeDef]
    ) -> UpdateFeaturedResultsSetResponseTypeDef:
        """
        Updates a set of featured results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.update_featured_results_set)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#update_featured_results_set)
        """

    def update_index(
        self, **kwargs: Unpack[UpdateIndexRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates an Amazon Kendra index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.update_index)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#update_index)
        """

    def update_query_suggestions_block_list(
        self, **kwargs: Unpack[UpdateQuerySuggestionsBlockListRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates a block list used for query suggestions for an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.update_query_suggestions_block_list)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#update_query_suggestions_block_list)
        """

    def update_query_suggestions_config(
        self, **kwargs: Unpack[UpdateQuerySuggestionsConfigRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the settings of query suggestions for an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.update_query_suggestions_config)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#update_query_suggestions_config)
        """

    def update_thesaurus(
        self, **kwargs: Unpack[UpdateThesaurusRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates a thesaurus for an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kendra.html#Kendra.Client.update_thesaurus)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra/client/#update_thesaurus)
        """
