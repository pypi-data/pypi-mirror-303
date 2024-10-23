"""
Type annotations for lexv2-models service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_lexv2_models.client import LexModelsV2Client

    session = Session()
    client: LexModelsV2Client = session.client("lexv2-models")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
    BatchCreateCustomVocabularyItemRequestRequestTypeDef,
    BatchCreateCustomVocabularyItemResponseTypeDef,
    BatchDeleteCustomVocabularyItemRequestRequestTypeDef,
    BatchDeleteCustomVocabularyItemResponseTypeDef,
    BatchUpdateCustomVocabularyItemRequestRequestTypeDef,
    BatchUpdateCustomVocabularyItemResponseTypeDef,
    BuildBotLocaleRequestRequestTypeDef,
    BuildBotLocaleResponseTypeDef,
    CreateBotAliasRequestRequestTypeDef,
    CreateBotAliasResponseTypeDef,
    CreateBotLocaleRequestRequestTypeDef,
    CreateBotLocaleResponseTypeDef,
    CreateBotReplicaRequestRequestTypeDef,
    CreateBotReplicaResponseTypeDef,
    CreateBotRequestRequestTypeDef,
    CreateBotResponseTypeDef,
    CreateBotVersionRequestRequestTypeDef,
    CreateBotVersionResponseTypeDef,
    CreateExportRequestRequestTypeDef,
    CreateExportResponseTypeDef,
    CreateIntentRequestRequestTypeDef,
    CreateIntentResponseTypeDef,
    CreateResourcePolicyRequestRequestTypeDef,
    CreateResourcePolicyResponseTypeDef,
    CreateResourcePolicyStatementRequestRequestTypeDef,
    CreateResourcePolicyStatementResponseTypeDef,
    CreateSlotRequestRequestTypeDef,
    CreateSlotResponseTypeDef,
    CreateSlotTypeRequestRequestTypeDef,
    CreateSlotTypeResponseTypeDef,
    CreateTestSetDiscrepancyReportRequestRequestTypeDef,
    CreateTestSetDiscrepancyReportResponseTypeDef,
    CreateUploadUrlResponseTypeDef,
    DeleteBotAliasRequestRequestTypeDef,
    DeleteBotAliasResponseTypeDef,
    DeleteBotLocaleRequestRequestTypeDef,
    DeleteBotLocaleResponseTypeDef,
    DeleteBotReplicaRequestRequestTypeDef,
    DeleteBotReplicaResponseTypeDef,
    DeleteBotRequestRequestTypeDef,
    DeleteBotResponseTypeDef,
    DeleteBotVersionRequestRequestTypeDef,
    DeleteBotVersionResponseTypeDef,
    DeleteCustomVocabularyRequestRequestTypeDef,
    DeleteCustomVocabularyResponseTypeDef,
    DeleteExportRequestRequestTypeDef,
    DeleteExportResponseTypeDef,
    DeleteImportRequestRequestTypeDef,
    DeleteImportResponseTypeDef,
    DeleteIntentRequestRequestTypeDef,
    DeleteResourcePolicyRequestRequestTypeDef,
    DeleteResourcePolicyResponseTypeDef,
    DeleteResourcePolicyStatementRequestRequestTypeDef,
    DeleteResourcePolicyStatementResponseTypeDef,
    DeleteSlotRequestRequestTypeDef,
    DeleteSlotTypeRequestRequestTypeDef,
    DeleteTestSetRequestRequestTypeDef,
    DeleteUtterancesRequestRequestTypeDef,
    DescribeBotAliasRequestRequestTypeDef,
    DescribeBotAliasResponseTypeDef,
    DescribeBotLocaleRequestRequestTypeDef,
    DescribeBotLocaleResponseTypeDef,
    DescribeBotRecommendationRequestRequestTypeDef,
    DescribeBotRecommendationResponseTypeDef,
    DescribeBotReplicaRequestRequestTypeDef,
    DescribeBotReplicaResponseTypeDef,
    DescribeBotRequestRequestTypeDef,
    DescribeBotResourceGenerationRequestRequestTypeDef,
    DescribeBotResourceGenerationResponseTypeDef,
    DescribeBotResponseTypeDef,
    DescribeBotVersionRequestRequestTypeDef,
    DescribeBotVersionResponseTypeDef,
    DescribeCustomVocabularyMetadataRequestRequestTypeDef,
    DescribeCustomVocabularyMetadataResponseTypeDef,
    DescribeExportRequestRequestTypeDef,
    DescribeExportResponseTypeDef,
    DescribeImportRequestRequestTypeDef,
    DescribeImportResponseTypeDef,
    DescribeIntentRequestRequestTypeDef,
    DescribeIntentResponseTypeDef,
    DescribeResourcePolicyRequestRequestTypeDef,
    DescribeResourcePolicyResponseTypeDef,
    DescribeSlotRequestRequestTypeDef,
    DescribeSlotResponseTypeDef,
    DescribeSlotTypeRequestRequestTypeDef,
    DescribeSlotTypeResponseTypeDef,
    DescribeTestExecutionRequestRequestTypeDef,
    DescribeTestExecutionResponseTypeDef,
    DescribeTestSetDiscrepancyReportRequestRequestTypeDef,
    DescribeTestSetDiscrepancyReportResponseTypeDef,
    DescribeTestSetGenerationRequestRequestTypeDef,
    DescribeTestSetGenerationResponseTypeDef,
    DescribeTestSetRequestRequestTypeDef,
    DescribeTestSetResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    GenerateBotElementRequestRequestTypeDef,
    GenerateBotElementResponseTypeDef,
    GetTestExecutionArtifactsUrlRequestRequestTypeDef,
    GetTestExecutionArtifactsUrlResponseTypeDef,
    ListAggregatedUtterancesRequestRequestTypeDef,
    ListAggregatedUtterancesResponseTypeDef,
    ListBotAliasesRequestRequestTypeDef,
    ListBotAliasesResponseTypeDef,
    ListBotAliasReplicasRequestRequestTypeDef,
    ListBotAliasReplicasResponseTypeDef,
    ListBotLocalesRequestRequestTypeDef,
    ListBotLocalesResponseTypeDef,
    ListBotRecommendationsRequestRequestTypeDef,
    ListBotRecommendationsResponseTypeDef,
    ListBotReplicasRequestRequestTypeDef,
    ListBotReplicasResponseTypeDef,
    ListBotResourceGenerationsRequestRequestTypeDef,
    ListBotResourceGenerationsResponseTypeDef,
    ListBotsRequestRequestTypeDef,
    ListBotsResponseTypeDef,
    ListBotVersionReplicasRequestRequestTypeDef,
    ListBotVersionReplicasResponseTypeDef,
    ListBotVersionsRequestRequestTypeDef,
    ListBotVersionsResponseTypeDef,
    ListBuiltInIntentsRequestRequestTypeDef,
    ListBuiltInIntentsResponseTypeDef,
    ListBuiltInSlotTypesRequestRequestTypeDef,
    ListBuiltInSlotTypesResponseTypeDef,
    ListCustomVocabularyItemsRequestRequestTypeDef,
    ListCustomVocabularyItemsResponseTypeDef,
    ListExportsRequestRequestTypeDef,
    ListExportsResponseTypeDef,
    ListImportsRequestRequestTypeDef,
    ListImportsResponseTypeDef,
    ListIntentMetricsRequestRequestTypeDef,
    ListIntentMetricsResponseTypeDef,
    ListIntentPathsRequestRequestTypeDef,
    ListIntentPathsResponseTypeDef,
    ListIntentsRequestRequestTypeDef,
    ListIntentsResponseTypeDef,
    ListIntentStageMetricsRequestRequestTypeDef,
    ListIntentStageMetricsResponseTypeDef,
    ListRecommendedIntentsRequestRequestTypeDef,
    ListRecommendedIntentsResponseTypeDef,
    ListSessionAnalyticsDataRequestRequestTypeDef,
    ListSessionAnalyticsDataResponseTypeDef,
    ListSessionMetricsRequestRequestTypeDef,
    ListSessionMetricsResponseTypeDef,
    ListSlotsRequestRequestTypeDef,
    ListSlotsResponseTypeDef,
    ListSlotTypesRequestRequestTypeDef,
    ListSlotTypesResponseTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTestExecutionResultItemsRequestRequestTypeDef,
    ListTestExecutionResultItemsResponseTypeDef,
    ListTestExecutionsRequestRequestTypeDef,
    ListTestExecutionsResponseTypeDef,
    ListTestSetRecordsRequestRequestTypeDef,
    ListTestSetRecordsResponseTypeDef,
    ListTestSetsRequestRequestTypeDef,
    ListTestSetsResponseTypeDef,
    ListUtteranceAnalyticsDataRequestRequestTypeDef,
    ListUtteranceAnalyticsDataResponseTypeDef,
    ListUtteranceMetricsRequestRequestTypeDef,
    ListUtteranceMetricsResponseTypeDef,
    SearchAssociatedTranscriptsRequestRequestTypeDef,
    SearchAssociatedTranscriptsResponseTypeDef,
    StartBotRecommendationRequestRequestTypeDef,
    StartBotRecommendationResponseTypeDef,
    StartBotResourceGenerationRequestRequestTypeDef,
    StartBotResourceGenerationResponseTypeDef,
    StartImportRequestRequestTypeDef,
    StartImportResponseTypeDef,
    StartTestExecutionRequestRequestTypeDef,
    StartTestExecutionResponseTypeDef,
    StartTestSetGenerationRequestRequestTypeDef,
    StartTestSetGenerationResponseTypeDef,
    StopBotRecommendationRequestRequestTypeDef,
    StopBotRecommendationResponseTypeDef,
    TagResourceRequestRequestTypeDef,
    UntagResourceRequestRequestTypeDef,
    UpdateBotAliasRequestRequestTypeDef,
    UpdateBotAliasResponseTypeDef,
    UpdateBotLocaleRequestRequestTypeDef,
    UpdateBotLocaleResponseTypeDef,
    UpdateBotRecommendationRequestRequestTypeDef,
    UpdateBotRecommendationResponseTypeDef,
    UpdateBotRequestRequestTypeDef,
    UpdateBotResponseTypeDef,
    UpdateExportRequestRequestTypeDef,
    UpdateExportResponseTypeDef,
    UpdateIntentRequestRequestTypeDef,
    UpdateIntentResponseTypeDef,
    UpdateResourcePolicyRequestRequestTypeDef,
    UpdateResourcePolicyResponseTypeDef,
    UpdateSlotRequestRequestTypeDef,
    UpdateSlotResponseTypeDef,
    UpdateSlotTypeRequestRequestTypeDef,
    UpdateSlotTypeResponseTypeDef,
    UpdateTestSetRequestRequestTypeDef,
    UpdateTestSetResponseTypeDef,
)
from .waiter import (
    BotAliasAvailableWaiter,
    BotAvailableWaiter,
    BotExportCompletedWaiter,
    BotImportCompletedWaiter,
    BotLocaleBuiltWaiter,
    BotLocaleCreatedWaiter,
    BotLocaleExpressTestingAvailableWaiter,
    BotVersionAvailableWaiter,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack


__all__ = ("LexModelsV2Client",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    PreconditionFailedException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class LexModelsV2Client(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        LexModelsV2Client exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#exceptions)
        """

    def batch_create_custom_vocabulary_item(
        self, **kwargs: Unpack[BatchCreateCustomVocabularyItemRequestRequestTypeDef]
    ) -> BatchCreateCustomVocabularyItemResponseTypeDef:
        """
        Create a batch of custom vocabulary items for a given bot locale's custom
        vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.batch_create_custom_vocabulary_item)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#batch_create_custom_vocabulary_item)
        """

    def batch_delete_custom_vocabulary_item(
        self, **kwargs: Unpack[BatchDeleteCustomVocabularyItemRequestRequestTypeDef]
    ) -> BatchDeleteCustomVocabularyItemResponseTypeDef:
        """
        Delete a batch of custom vocabulary items for a given bot locale's custom
        vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.batch_delete_custom_vocabulary_item)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#batch_delete_custom_vocabulary_item)
        """

    def batch_update_custom_vocabulary_item(
        self, **kwargs: Unpack[BatchUpdateCustomVocabularyItemRequestRequestTypeDef]
    ) -> BatchUpdateCustomVocabularyItemResponseTypeDef:
        """
        Update a batch of custom vocabulary items for a given bot locale's custom
        vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.batch_update_custom_vocabulary_item)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#batch_update_custom_vocabulary_item)
        """

    def build_bot_locale(
        self, **kwargs: Unpack[BuildBotLocaleRequestRequestTypeDef]
    ) -> BuildBotLocaleResponseTypeDef:
        """
        Builds a bot, its intents, and its slot types into a specific locale.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.build_bot_locale)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#build_bot_locale)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#close)
        """

    def create_bot(
        self, **kwargs: Unpack[CreateBotRequestRequestTypeDef]
    ) -> CreateBotResponseTypeDef:
        """
        Creates an Amazon Lex conversational bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.create_bot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#create_bot)
        """

    def create_bot_alias(
        self, **kwargs: Unpack[CreateBotAliasRequestRequestTypeDef]
    ) -> CreateBotAliasResponseTypeDef:
        """
        Creates an alias for the specified version of a bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.create_bot_alias)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#create_bot_alias)
        """

    def create_bot_locale(
        self, **kwargs: Unpack[CreateBotLocaleRequestRequestTypeDef]
    ) -> CreateBotLocaleResponseTypeDef:
        """
        Creates a locale in the bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.create_bot_locale)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#create_bot_locale)
        """

    def create_bot_replica(
        self, **kwargs: Unpack[CreateBotReplicaRequestRequestTypeDef]
    ) -> CreateBotReplicaResponseTypeDef:
        """
        Action to create a replication of the source bot in the secondary region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.create_bot_replica)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#create_bot_replica)
        """

    def create_bot_version(
        self, **kwargs: Unpack[CreateBotVersionRequestRequestTypeDef]
    ) -> CreateBotVersionResponseTypeDef:
        """
        Creates an immutable version of the bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.create_bot_version)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#create_bot_version)
        """

    def create_export(
        self, **kwargs: Unpack[CreateExportRequestRequestTypeDef]
    ) -> CreateExportResponseTypeDef:
        """
        Creates a zip archive containing the contents of a bot or a bot locale.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.create_export)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#create_export)
        """

    def create_intent(
        self, **kwargs: Unpack[CreateIntentRequestRequestTypeDef]
    ) -> CreateIntentResponseTypeDef:
        """
        Creates an intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.create_intent)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#create_intent)
        """

    def create_resource_policy(
        self, **kwargs: Unpack[CreateResourcePolicyRequestRequestTypeDef]
    ) -> CreateResourcePolicyResponseTypeDef:
        """
        Creates a new resource policy with the specified policy statements.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.create_resource_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#create_resource_policy)
        """

    def create_resource_policy_statement(
        self, **kwargs: Unpack[CreateResourcePolicyStatementRequestRequestTypeDef]
    ) -> CreateResourcePolicyStatementResponseTypeDef:
        """
        Adds a new resource policy statement to a bot or bot alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.create_resource_policy_statement)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#create_resource_policy_statement)
        """

    def create_slot(
        self, **kwargs: Unpack[CreateSlotRequestRequestTypeDef]
    ) -> CreateSlotResponseTypeDef:
        """
        Creates a slot in an intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.create_slot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#create_slot)
        """

    def create_slot_type(
        self, **kwargs: Unpack[CreateSlotTypeRequestRequestTypeDef]
    ) -> CreateSlotTypeResponseTypeDef:
        """
        Creates a custom slot type To create a custom slot type, specify a name for the
        slot type and a set of enumeration values, the values that a slot of this type
        can
        assume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.create_slot_type)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#create_slot_type)
        """

    def create_test_set_discrepancy_report(
        self, **kwargs: Unpack[CreateTestSetDiscrepancyReportRequestRequestTypeDef]
    ) -> CreateTestSetDiscrepancyReportResponseTypeDef:
        """
        Create a report that describes the differences between the bot and the test set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.create_test_set_discrepancy_report)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#create_test_set_discrepancy_report)
        """

    def create_upload_url(self) -> CreateUploadUrlResponseTypeDef:
        """
        Gets a pre-signed S3 write URL that you use to upload the zip archive when
        importing a bot or a bot
        locale.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.create_upload_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#create_upload_url)
        """

    def delete_bot(
        self, **kwargs: Unpack[DeleteBotRequestRequestTypeDef]
    ) -> DeleteBotResponseTypeDef:
        """
        Deletes all versions of a bot, including the `Draft` version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_bot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#delete_bot)
        """

    def delete_bot_alias(
        self, **kwargs: Unpack[DeleteBotAliasRequestRequestTypeDef]
    ) -> DeleteBotAliasResponseTypeDef:
        """
        Deletes the specified bot alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_bot_alias)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#delete_bot_alias)
        """

    def delete_bot_locale(
        self, **kwargs: Unpack[DeleteBotLocaleRequestRequestTypeDef]
    ) -> DeleteBotLocaleResponseTypeDef:
        """
        Removes a locale from a bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_bot_locale)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#delete_bot_locale)
        """

    def delete_bot_replica(
        self, **kwargs: Unpack[DeleteBotReplicaRequestRequestTypeDef]
    ) -> DeleteBotReplicaResponseTypeDef:
        """
        The action to delete the replicated bot in the secondary region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_bot_replica)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#delete_bot_replica)
        """

    def delete_bot_version(
        self, **kwargs: Unpack[DeleteBotVersionRequestRequestTypeDef]
    ) -> DeleteBotVersionResponseTypeDef:
        """
        Deletes a specific version of a bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_bot_version)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#delete_bot_version)
        """

    def delete_custom_vocabulary(
        self, **kwargs: Unpack[DeleteCustomVocabularyRequestRequestTypeDef]
    ) -> DeleteCustomVocabularyResponseTypeDef:
        """
        Removes a custom vocabulary from the specified locale in the specified bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_custom_vocabulary)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#delete_custom_vocabulary)
        """

    def delete_export(
        self, **kwargs: Unpack[DeleteExportRequestRequestTypeDef]
    ) -> DeleteExportResponseTypeDef:
        """
        Removes a previous export and the associated files stored in an S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_export)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#delete_export)
        """

    def delete_import(
        self, **kwargs: Unpack[DeleteImportRequestRequestTypeDef]
    ) -> DeleteImportResponseTypeDef:
        """
        Removes a previous import and the associated file stored in an S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_import)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#delete_import)
        """

    def delete_intent(
        self, **kwargs: Unpack[DeleteIntentRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the specified intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_intent)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#delete_intent)
        """

    def delete_resource_policy(
        self, **kwargs: Unpack[DeleteResourcePolicyRequestRequestTypeDef]
    ) -> DeleteResourcePolicyResponseTypeDef:
        """
        Removes an existing policy from a bot or bot alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_resource_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#delete_resource_policy)
        """

    def delete_resource_policy_statement(
        self, **kwargs: Unpack[DeleteResourcePolicyStatementRequestRequestTypeDef]
    ) -> DeleteResourcePolicyStatementResponseTypeDef:
        """
        Deletes a policy statement from a resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_resource_policy_statement)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#delete_resource_policy_statement)
        """

    def delete_slot(
        self, **kwargs: Unpack[DeleteSlotRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified slot from an intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_slot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#delete_slot)
        """

    def delete_slot_type(
        self, **kwargs: Unpack[DeleteSlotTypeRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a slot type from a bot locale.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_slot_type)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#delete_slot_type)
        """

    def delete_test_set(
        self, **kwargs: Unpack[DeleteTestSetRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        The action to delete the selected test set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_test_set)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#delete_test_set)
        """

    def delete_utterances(
        self, **kwargs: Unpack[DeleteUtterancesRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes stored utterances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.delete_utterances)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#delete_utterances)
        """

    def describe_bot(
        self, **kwargs: Unpack[DescribeBotRequestRequestTypeDef]
    ) -> DescribeBotResponseTypeDef:
        """
        Provides metadata information about a bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#describe_bot)
        """

    def describe_bot_alias(
        self, **kwargs: Unpack[DescribeBotAliasRequestRequestTypeDef]
    ) -> DescribeBotAliasResponseTypeDef:
        """
        Get information about a specific bot alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot_alias)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#describe_bot_alias)
        """

    def describe_bot_locale(
        self, **kwargs: Unpack[DescribeBotLocaleRequestRequestTypeDef]
    ) -> DescribeBotLocaleResponseTypeDef:
        """
        Describes the settings that a bot has for a specific locale.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot_locale)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#describe_bot_locale)
        """

    def describe_bot_recommendation(
        self, **kwargs: Unpack[DescribeBotRecommendationRequestRequestTypeDef]
    ) -> DescribeBotRecommendationResponseTypeDef:
        """
        Provides metadata information about a bot recommendation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot_recommendation)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#describe_bot_recommendation)
        """

    def describe_bot_replica(
        self, **kwargs: Unpack[DescribeBotReplicaRequestRequestTypeDef]
    ) -> DescribeBotReplicaResponseTypeDef:
        """
        Monitors the bot replication status through the UI console.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot_replica)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#describe_bot_replica)
        """

    def describe_bot_resource_generation(
        self, **kwargs: Unpack[DescribeBotResourceGenerationRequestRequestTypeDef]
    ) -> DescribeBotResourceGenerationResponseTypeDef:
        """
        Returns information about a request to generate a bot through natural language
        description, made through the `StartBotResource`
        API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot_resource_generation)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#describe_bot_resource_generation)
        """

    def describe_bot_version(
        self, **kwargs: Unpack[DescribeBotVersionRequestRequestTypeDef]
    ) -> DescribeBotVersionResponseTypeDef:
        """
        Provides metadata about a version of a bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot_version)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#describe_bot_version)
        """

    def describe_custom_vocabulary_metadata(
        self, **kwargs: Unpack[DescribeCustomVocabularyMetadataRequestRequestTypeDef]
    ) -> DescribeCustomVocabularyMetadataResponseTypeDef:
        """
        Provides metadata information about a custom vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_custom_vocabulary_metadata)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#describe_custom_vocabulary_metadata)
        """

    def describe_export(
        self, **kwargs: Unpack[DescribeExportRequestRequestTypeDef]
    ) -> DescribeExportResponseTypeDef:
        """
        Gets information about a specific export.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_export)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#describe_export)
        """

    def describe_import(
        self, **kwargs: Unpack[DescribeImportRequestRequestTypeDef]
    ) -> DescribeImportResponseTypeDef:
        """
        Gets information about a specific import.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_import)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#describe_import)
        """

    def describe_intent(
        self, **kwargs: Unpack[DescribeIntentRequestRequestTypeDef]
    ) -> DescribeIntentResponseTypeDef:
        """
        Returns metadata about an intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_intent)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#describe_intent)
        """

    def describe_resource_policy(
        self, **kwargs: Unpack[DescribeResourcePolicyRequestRequestTypeDef]
    ) -> DescribeResourcePolicyResponseTypeDef:
        """
        Gets the resource policy and policy revision for a bot or bot alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_resource_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#describe_resource_policy)
        """

    def describe_slot(
        self, **kwargs: Unpack[DescribeSlotRequestRequestTypeDef]
    ) -> DescribeSlotResponseTypeDef:
        """
        Gets metadata information about a slot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_slot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#describe_slot)
        """

    def describe_slot_type(
        self, **kwargs: Unpack[DescribeSlotTypeRequestRequestTypeDef]
    ) -> DescribeSlotTypeResponseTypeDef:
        """
        Gets metadata information about a slot type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_slot_type)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#describe_slot_type)
        """

    def describe_test_execution(
        self, **kwargs: Unpack[DescribeTestExecutionRequestRequestTypeDef]
    ) -> DescribeTestExecutionResponseTypeDef:
        """
        Gets metadata information about the test execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_test_execution)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#describe_test_execution)
        """

    def describe_test_set(
        self, **kwargs: Unpack[DescribeTestSetRequestRequestTypeDef]
    ) -> DescribeTestSetResponseTypeDef:
        """
        Gets metadata information about the test set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_test_set)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#describe_test_set)
        """

    def describe_test_set_discrepancy_report(
        self, **kwargs: Unpack[DescribeTestSetDiscrepancyReportRequestRequestTypeDef]
    ) -> DescribeTestSetDiscrepancyReportResponseTypeDef:
        """
        Gets metadata information about the test set discrepancy report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_test_set_discrepancy_report)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#describe_test_set_discrepancy_report)
        """

    def describe_test_set_generation(
        self, **kwargs: Unpack[DescribeTestSetGenerationRequestRequestTypeDef]
    ) -> DescribeTestSetGenerationResponseTypeDef:
        """
        Gets metadata information about the test set generation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.describe_test_set_generation)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#describe_test_set_generation)
        """

    def generate_bot_element(
        self, **kwargs: Unpack[GenerateBotElementRequestRequestTypeDef]
    ) -> GenerateBotElementResponseTypeDef:
        """
        Generates sample utterances for an intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.generate_bot_element)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#generate_bot_element)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#generate_presigned_url)
        """

    def get_test_execution_artifacts_url(
        self, **kwargs: Unpack[GetTestExecutionArtifactsUrlRequestRequestTypeDef]
    ) -> GetTestExecutionArtifactsUrlResponseTypeDef:
        """
        The pre-signed Amazon S3 URL to download the test execution result artifacts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.get_test_execution_artifacts_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#get_test_execution_artifacts_url)
        """

    def list_aggregated_utterances(
        self, **kwargs: Unpack[ListAggregatedUtterancesRequestRequestTypeDef]
    ) -> ListAggregatedUtterancesResponseTypeDef:
        """
        Provides a list of utterances that users have sent to the bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_aggregated_utterances)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#list_aggregated_utterances)
        """

    def list_bot_alias_replicas(
        self, **kwargs: Unpack[ListBotAliasReplicasRequestRequestTypeDef]
    ) -> ListBotAliasReplicasResponseTypeDef:
        """
        The action to list the replicated bots created from the source bot alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_bot_alias_replicas)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#list_bot_alias_replicas)
        """

    def list_bot_aliases(
        self, **kwargs: Unpack[ListBotAliasesRequestRequestTypeDef]
    ) -> ListBotAliasesResponseTypeDef:
        """
        Gets a list of aliases for the specified bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_bot_aliases)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#list_bot_aliases)
        """

    def list_bot_locales(
        self, **kwargs: Unpack[ListBotLocalesRequestRequestTypeDef]
    ) -> ListBotLocalesResponseTypeDef:
        """
        Gets a list of locales for the specified bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_bot_locales)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#list_bot_locales)
        """

    def list_bot_recommendations(
        self, **kwargs: Unpack[ListBotRecommendationsRequestRequestTypeDef]
    ) -> ListBotRecommendationsResponseTypeDef:
        """
        Get a list of bot recommendations that meet the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_bot_recommendations)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#list_bot_recommendations)
        """

    def list_bot_replicas(
        self, **kwargs: Unpack[ListBotReplicasRequestRequestTypeDef]
    ) -> ListBotReplicasResponseTypeDef:
        """
        The action to list the replicated bots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_bot_replicas)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#list_bot_replicas)
        """

    def list_bot_resource_generations(
        self, **kwargs: Unpack[ListBotResourceGenerationsRequestRequestTypeDef]
    ) -> ListBotResourceGenerationsResponseTypeDef:
        """
        Lists the generation requests made for a bot locale.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_bot_resource_generations)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#list_bot_resource_generations)
        """

    def list_bot_version_replicas(
        self, **kwargs: Unpack[ListBotVersionReplicasRequestRequestTypeDef]
    ) -> ListBotVersionReplicasResponseTypeDef:
        """
        Contains information about all the versions replication statuses applicable for
        Global
        Resiliency.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_bot_version_replicas)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#list_bot_version_replicas)
        """

    def list_bot_versions(
        self, **kwargs: Unpack[ListBotVersionsRequestRequestTypeDef]
    ) -> ListBotVersionsResponseTypeDef:
        """
        Gets information about all of the versions of a bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_bot_versions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#list_bot_versions)
        """

    def list_bots(self, **kwargs: Unpack[ListBotsRequestRequestTypeDef]) -> ListBotsResponseTypeDef:
        """
        Gets a list of available bots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_bots)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#list_bots)
        """

    def list_built_in_intents(
        self, **kwargs: Unpack[ListBuiltInIntentsRequestRequestTypeDef]
    ) -> ListBuiltInIntentsResponseTypeDef:
        """
        Gets a list of built-in intents provided by Amazon Lex that you can use in your
        bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_built_in_intents)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#list_built_in_intents)
        """

    def list_built_in_slot_types(
        self, **kwargs: Unpack[ListBuiltInSlotTypesRequestRequestTypeDef]
    ) -> ListBuiltInSlotTypesResponseTypeDef:
        """
        Gets a list of built-in slot types that meet the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_built_in_slot_types)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#list_built_in_slot_types)
        """

    def list_custom_vocabulary_items(
        self, **kwargs: Unpack[ListCustomVocabularyItemsRequestRequestTypeDef]
    ) -> ListCustomVocabularyItemsResponseTypeDef:
        """
        Paginated list of custom vocabulary items for a given bot locale's custom
        vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_custom_vocabulary_items)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#list_custom_vocabulary_items)
        """

    def list_exports(
        self, **kwargs: Unpack[ListExportsRequestRequestTypeDef]
    ) -> ListExportsResponseTypeDef:
        """
        Lists the exports for a bot, bot locale, or custom vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_exports)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#list_exports)
        """

    def list_imports(
        self, **kwargs: Unpack[ListImportsRequestRequestTypeDef]
    ) -> ListImportsResponseTypeDef:
        """
        Lists the imports for a bot, bot locale, or custom vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_imports)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#list_imports)
        """

    def list_intent_metrics(
        self, **kwargs: Unpack[ListIntentMetricsRequestRequestTypeDef]
    ) -> ListIntentMetricsResponseTypeDef:
        """
        Retrieves summary metrics for the intents in your bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_intent_metrics)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#list_intent_metrics)
        """

    def list_intent_paths(
        self, **kwargs: Unpack[ListIntentPathsRequestRequestTypeDef]
    ) -> ListIntentPathsResponseTypeDef:
        """
        Retrieves summary statistics for a path of intents that users take over
        sessions with your
        bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_intent_paths)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#list_intent_paths)
        """

    def list_intent_stage_metrics(
        self, **kwargs: Unpack[ListIntentStageMetricsRequestRequestTypeDef]
    ) -> ListIntentStageMetricsResponseTypeDef:
        """
        Retrieves summary metrics for the stages within intents in your bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_intent_stage_metrics)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#list_intent_stage_metrics)
        """

    def list_intents(
        self, **kwargs: Unpack[ListIntentsRequestRequestTypeDef]
    ) -> ListIntentsResponseTypeDef:
        """
        Get a list of intents that meet the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_intents)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#list_intents)
        """

    def list_recommended_intents(
        self, **kwargs: Unpack[ListRecommendedIntentsRequestRequestTypeDef]
    ) -> ListRecommendedIntentsResponseTypeDef:
        """
        Gets a list of recommended intents provided by the bot recommendation that you
        can use in your
        bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_recommended_intents)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#list_recommended_intents)
        """

    def list_session_analytics_data(
        self, **kwargs: Unpack[ListSessionAnalyticsDataRequestRequestTypeDef]
    ) -> ListSessionAnalyticsDataResponseTypeDef:
        """
        Retrieves a list of metadata for individual user sessions with your bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_session_analytics_data)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#list_session_analytics_data)
        """

    def list_session_metrics(
        self, **kwargs: Unpack[ListSessionMetricsRequestRequestTypeDef]
    ) -> ListSessionMetricsResponseTypeDef:
        """
        Retrieves summary metrics for the user sessions with your bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_session_metrics)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#list_session_metrics)
        """

    def list_slot_types(
        self, **kwargs: Unpack[ListSlotTypesRequestRequestTypeDef]
    ) -> ListSlotTypesResponseTypeDef:
        """
        Gets a list of slot types that match the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_slot_types)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#list_slot_types)
        """

    def list_slots(
        self, **kwargs: Unpack[ListSlotsRequestRequestTypeDef]
    ) -> ListSlotsResponseTypeDef:
        """
        Gets a list of slots that match the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_slots)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#list_slots)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Gets a list of tags associated with a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_tags_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#list_tags_for_resource)
        """

    def list_test_execution_result_items(
        self, **kwargs: Unpack[ListTestExecutionResultItemsRequestRequestTypeDef]
    ) -> ListTestExecutionResultItemsResponseTypeDef:
        """
        Gets a list of test execution result items.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_test_execution_result_items)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#list_test_execution_result_items)
        """

    def list_test_executions(
        self, **kwargs: Unpack[ListTestExecutionsRequestRequestTypeDef]
    ) -> ListTestExecutionsResponseTypeDef:
        """
        The list of test set executions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_test_executions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#list_test_executions)
        """

    def list_test_set_records(
        self, **kwargs: Unpack[ListTestSetRecordsRequestRequestTypeDef]
    ) -> ListTestSetRecordsResponseTypeDef:
        """
        The list of test set records.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_test_set_records)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#list_test_set_records)
        """

    def list_test_sets(
        self, **kwargs: Unpack[ListTestSetsRequestRequestTypeDef]
    ) -> ListTestSetsResponseTypeDef:
        """
        The list of the test sets See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/models.lex.v2-2020-08-07/ListTestSets).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_test_sets)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#list_test_sets)
        """

    def list_utterance_analytics_data(
        self, **kwargs: Unpack[ListUtteranceAnalyticsDataRequestRequestTypeDef]
    ) -> ListUtteranceAnalyticsDataResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_utterance_analytics_data)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#list_utterance_analytics_data)
        """

    def list_utterance_metrics(
        self, **kwargs: Unpack[ListUtteranceMetricsRequestRequestTypeDef]
    ) -> ListUtteranceMetricsResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.list_utterance_metrics)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#list_utterance_metrics)
        """

    def search_associated_transcripts(
        self, **kwargs: Unpack[SearchAssociatedTranscriptsRequestRequestTypeDef]
    ) -> SearchAssociatedTranscriptsResponseTypeDef:
        """
        Search for associated transcripts that meet the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.search_associated_transcripts)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#search_associated_transcripts)
        """

    def start_bot_recommendation(
        self, **kwargs: Unpack[StartBotRecommendationRequestRequestTypeDef]
    ) -> StartBotRecommendationResponseTypeDef:
        """
        Use this to provide your transcript data, and to start the bot recommendation
        process.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.start_bot_recommendation)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#start_bot_recommendation)
        """

    def start_bot_resource_generation(
        self, **kwargs: Unpack[StartBotResourceGenerationRequestRequestTypeDef]
    ) -> StartBotResourceGenerationResponseTypeDef:
        """
        Starts a request for the descriptive bot builder to generate a bot locale
        configuration based on the prompt you provide
        it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.start_bot_resource_generation)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#start_bot_resource_generation)
        """

    def start_import(
        self, **kwargs: Unpack[StartImportRequestRequestTypeDef]
    ) -> StartImportResponseTypeDef:
        """
        Starts importing a bot, bot locale, or custom vocabulary from a zip archive
        that you uploaded to an S3
        bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.start_import)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#start_import)
        """

    def start_test_execution(
        self, **kwargs: Unpack[StartTestExecutionRequestRequestTypeDef]
    ) -> StartTestExecutionResponseTypeDef:
        """
        The action to start test set execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.start_test_execution)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#start_test_execution)
        """

    def start_test_set_generation(
        self, **kwargs: Unpack[StartTestSetGenerationRequestRequestTypeDef]
    ) -> StartTestSetGenerationResponseTypeDef:
        """
        The action to start the generation of test set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.start_test_set_generation)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#start_test_set_generation)
        """

    def stop_bot_recommendation(
        self, **kwargs: Unpack[StopBotRecommendationRequestRequestTypeDef]
    ) -> StopBotRecommendationResponseTypeDef:
        """
        Stop an already running Bot Recommendation request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.stop_bot_recommendation)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#stop_bot_recommendation)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds the specified tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes tags from a bot, bot alias, or bot channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#untag_resource)
        """

    def update_bot(
        self, **kwargs: Unpack[UpdateBotRequestRequestTypeDef]
    ) -> UpdateBotResponseTypeDef:
        """
        Updates the configuration of an existing bot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.update_bot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#update_bot)
        """

    def update_bot_alias(
        self, **kwargs: Unpack[UpdateBotAliasRequestRequestTypeDef]
    ) -> UpdateBotAliasResponseTypeDef:
        """
        Updates the configuration of an existing bot alias.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.update_bot_alias)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#update_bot_alias)
        """

    def update_bot_locale(
        self, **kwargs: Unpack[UpdateBotLocaleRequestRequestTypeDef]
    ) -> UpdateBotLocaleResponseTypeDef:
        """
        Updates the settings that a bot has for a specific locale.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.update_bot_locale)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#update_bot_locale)
        """

    def update_bot_recommendation(
        self, **kwargs: Unpack[UpdateBotRecommendationRequestRequestTypeDef]
    ) -> UpdateBotRecommendationResponseTypeDef:
        """
        Updates an existing bot recommendation request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.update_bot_recommendation)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#update_bot_recommendation)
        """

    def update_export(
        self, **kwargs: Unpack[UpdateExportRequestRequestTypeDef]
    ) -> UpdateExportResponseTypeDef:
        """
        Updates the password used to protect an export zip archive.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.update_export)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#update_export)
        """

    def update_intent(
        self, **kwargs: Unpack[UpdateIntentRequestRequestTypeDef]
    ) -> UpdateIntentResponseTypeDef:
        """
        Updates the settings for an intent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.update_intent)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#update_intent)
        """

    def update_resource_policy(
        self, **kwargs: Unpack[UpdateResourcePolicyRequestRequestTypeDef]
    ) -> UpdateResourcePolicyResponseTypeDef:
        """
        Replaces the existing resource policy for a bot or bot alias with a new one.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.update_resource_policy)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#update_resource_policy)
        """

    def update_slot(
        self, **kwargs: Unpack[UpdateSlotRequestRequestTypeDef]
    ) -> UpdateSlotResponseTypeDef:
        """
        Updates the settings for a slot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.update_slot)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#update_slot)
        """

    def update_slot_type(
        self, **kwargs: Unpack[UpdateSlotTypeRequestRequestTypeDef]
    ) -> UpdateSlotTypeResponseTypeDef:
        """
        Updates the configuration of an existing slot type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.update_slot_type)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#update_slot_type)
        """

    def update_test_set(
        self, **kwargs: Unpack[UpdateTestSetRequestRequestTypeDef]
    ) -> UpdateTestSetResponseTypeDef:
        """
        The action to update the test set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.update_test_set)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#update_test_set)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["bot_alias_available"]) -> BotAliasAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["bot_available"]) -> BotAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["bot_export_completed"]) -> BotExportCompletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["bot_import_completed"]) -> BotImportCompletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["bot_locale_built"]) -> BotLocaleBuiltWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["bot_locale_created"]) -> BotLocaleCreatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["bot_locale_express_testing_available"]
    ) -> BotLocaleExpressTestingAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["bot_version_available"]
    ) -> BotVersionAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html#LexModelsV2.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client/#get_waiter)
        """
