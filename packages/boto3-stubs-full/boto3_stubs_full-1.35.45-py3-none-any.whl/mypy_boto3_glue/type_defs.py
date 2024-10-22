"""
Type annotations for glue service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/type_defs/)

Usage::

    ```python
    from mypy_boto3_glue.type_defs import NotificationPropertyTypeDef

    data: NotificationPropertyTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    AdditionalOptionKeysType,
    AggFunctionType,
    AuthenticationTypeType,
    BackfillErrorCodeType,
    BlueprintRunStateType,
    BlueprintStatusType,
    CatalogEncryptionModeType,
    CloudWatchEncryptionModeType,
    ColumnStatisticsStateType,
    ColumnStatisticsTypeType,
    ComparatorType,
    CompatibilityType,
    CompressionTypeType,
    ConnectionPropertyKeyType,
    ConnectionStatusType,
    ConnectionTypeType,
    CrawlerHistoryStateType,
    CrawlerLineageSettingsType,
    CrawlerStateType,
    CrawlStateType,
    CsvHeaderOptionType,
    CsvSerdeOptionType,
    DataFormatType,
    DataQualityModelStatusType,
    DataQualityRuleResultStatusType,
    DeleteBehaviorType,
    DeltaTargetCompressionTypeType,
    DQCompositeRuleEvaluationMethodType,
    DQStopJobOnFailureTimingType,
    DQTransformOutputType,
    EnableHybridValuesType,
    ExecutionClassType,
    ExistConditionType,
    FieldNameType,
    FilterLogicalOperatorType,
    FilterOperationType,
    FilterOperatorType,
    FilterValueTypeType,
    GlueRecordTypeType,
    HudiTargetCompressionTypeType,
    InclusionAnnotationValueType,
    JDBCConnectionTypeType,
    JDBCDataTypeType,
    JdbcMetadataEntryType,
    JobBookmarksEncryptionModeType,
    JobModeType,
    JobRunStateType,
    JoinTypeType,
    LanguageType,
    LastCrawlStatusType,
    LogicalType,
    MLUserDataEncryptionModeStringType,
    NodeTypeType,
    OAuth2GrantTypeType,
    ParamTypeType,
    ParquetCompressionTypeType,
    PartitionIndexStatusType,
    PermissionType,
    PermissionTypeType,
    PiiTypeType,
    PrincipalTypeType,
    QuoteCharType,
    RecrawlBehaviorType,
    RegistryStatusType,
    ResourceActionType,
    ResourceShareTypeType,
    ResourceStateType,
    ResourceTypeType,
    S3EncryptionModeType,
    ScheduleStateType,
    SchemaStatusType,
    SchemaVersionStatusType,
    SeparatorType,
    SessionStatusType,
    SortDirectionTypeType,
    SortType,
    SourceControlAuthStrategyType,
    SourceControlProviderType,
    StartingPositionType,
    StatementStateType,
    StatisticEvaluationLevelType,
    TableAttributesType,
    TableOptimizerEventTypeType,
    TableOptimizerTypeType,
    TargetFormatType,
    TaskRunSortColumnTypeType,
    TaskStatusTypeType,
    TaskTypeType,
    TransformSortColumnTypeType,
    TransformStatusTypeType,
    TriggerStateType,
    TriggerTypeType,
    UnionTypeType,
    UpdateBehaviorType,
    UpdateCatalogBehaviorType,
    ViewDialectType,
    ViewUpdateActionType,
    WorkerTypeType,
    WorkflowRunStatusType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "NotificationPropertyTypeDef",
    "AggregateOperationOutputTypeDef",
    "AggregateOperationTypeDef",
    "AmazonRedshiftAdvancedOptionTypeDef",
    "OptionTypeDef",
    "AnnotationErrorTypeDef",
    "MappingOutputTypeDef",
    "MappingPaginatorTypeDef",
    "AuditContextTypeDef",
    "AuthorizationCodePropertiesTypeDef",
    "PartitionValueListOutputTypeDef",
    "BasicCatalogTargetOutputTypeDef",
    "BasicCatalogTargetTypeDef",
    "ResponseMetadataTypeDef",
    "BatchDeleteConnectionRequestRequestTypeDef",
    "ErrorDetailTypeDef",
    "BatchDeleteTableRequestRequestTypeDef",
    "BatchDeleteTableVersionRequestRequestTypeDef",
    "BatchGetBlueprintsRequestRequestTypeDef",
    "BatchGetCrawlersRequestRequestTypeDef",
    "BatchGetCustomEntityTypesRequestRequestTypeDef",
    "CustomEntityTypeTypeDef",
    "BatchGetDataQualityResultRequestRequestTypeDef",
    "BatchGetDevEndpointsRequestRequestTypeDef",
    "DevEndpointTypeDef",
    "BatchGetJobsRequestRequestTypeDef",
    "PartitionValueListTypeDef",
    "BatchGetTableOptimizerEntryTypeDef",
    "BatchGetTriggersRequestRequestTypeDef",
    "BatchGetWorkflowsRequestRequestTypeDef",
    "DatapointInclusionAnnotationTypeDef",
    "BatchStopJobRunRequestRequestTypeDef",
    "BatchStopJobRunSuccessfulSubmissionTypeDef",
    "BinaryColumnStatisticsDataTypeDef",
    "BlobTypeDef",
    "BlueprintDetailsTypeDef",
    "BlueprintRunTypeDef",
    "LastActiveDefinitionTypeDef",
    "BooleanColumnStatisticsDataTypeDef",
    "CancelDataQualityRuleRecommendationRunRequestRequestTypeDef",
    "CancelDataQualityRulesetEvaluationRunRequestRequestTypeDef",
    "CancelMLTaskRunRequestRequestTypeDef",
    "CancelStatementRequestRequestTypeDef",
    "CatalogEntryTypeDef",
    "CatalogImportStatusTypeDef",
    "KafkaStreamingSourceOptionsOutputTypeDef",
    "StreamingDataPreviewOptionsTypeDef",
    "KinesisStreamingSourceOptionsOutputTypeDef",
    "CatalogSchemaChangePolicyTypeDef",
    "CatalogSourceTypeDef",
    "CatalogTargetOutputTypeDef",
    "CatalogTargetTypeDef",
    "CheckSchemaVersionValidityInputRequestTypeDef",
    "CsvClassifierTypeDef",
    "GrokClassifierTypeDef",
    "JsonClassifierTypeDef",
    "XMLClassifierTypeDef",
    "CloudWatchEncryptionTypeDef",
    "ConnectorDataTargetOutputTypeDef",
    "DirectJDBCSourceTypeDef",
    "DropDuplicatesOutputTypeDef",
    "DropFieldsOutputTypeDef",
    "DynamoDBCatalogSourceTypeDef",
    "FillMissingValuesOutputTypeDef",
    "MergeOutputTypeDef",
    "MicrosoftSQLServerCatalogSourceTypeDef",
    "MicrosoftSQLServerCatalogTargetOutputTypeDef",
    "MySQLCatalogSourceTypeDef",
    "MySQLCatalogTargetOutputTypeDef",
    "OracleSQLCatalogSourceTypeDef",
    "OracleSQLCatalogTargetOutputTypeDef",
    "PIIDetectionOutputTypeDef",
    "PostgreSQLCatalogSourceTypeDef",
    "PostgreSQLCatalogTargetOutputTypeDef",
    "RedshiftSourceTypeDef",
    "RelationalCatalogSourceTypeDef",
    "RenameFieldOutputTypeDef",
    "SelectFieldsOutputTypeDef",
    "SelectFromCollectionOutputTypeDef",
    "SpigotOutputTypeDef",
    "SplitFieldsOutputTypeDef",
    "UnionOutputTypeDef",
    "CodeGenEdgeTypeDef",
    "CodeGenNodeArgTypeDef",
    "ColumnImportanceTypeDef",
    "ColumnOutputTypeDef",
    "ColumnRowFilterTypeDef",
    "DateColumnStatisticsDataOutputTypeDef",
    "DoubleColumnStatisticsDataTypeDef",
    "LongColumnStatisticsDataTypeDef",
    "StringColumnStatisticsDataTypeDef",
    "ColumnStatisticsTaskRunTypeDef",
    "TimestampTypeDef",
    "ColumnTypeDef",
    "IcebergCompactionMetricsTypeDef",
    "ConditionExpressionTypeDef",
    "ConditionTypeDef",
    "ConfigurationObjectOutputTypeDef",
    "ConfigurationObjectTypeDef",
    "ConfusionMatrixTypeDef",
    "ConnectionPasswordEncryptionTypeDef",
    "PhysicalConnectionRequirementsOutputTypeDef",
    "ConnectionsListOutputTypeDef",
    "ConnectionsListTypeDef",
    "ConnectorDataTargetTypeDef",
    "CrawlTypeDef",
    "CrawlerHistoryTypeDef",
    "CrawlerMetricsTypeDef",
    "DeltaTargetOutputTypeDef",
    "DynamoDBTargetTypeDef",
    "HudiTargetOutputTypeDef",
    "IcebergTargetOutputTypeDef",
    "JdbcTargetOutputTypeDef",
    "MongoDBTargetTypeDef",
    "S3TargetOutputTypeDef",
    "LakeFormationConfigurationTypeDef",
    "LastCrawlInfoTypeDef",
    "LineageConfigurationTypeDef",
    "RecrawlPolicyTypeDef",
    "ScheduleTypeDef",
    "SchemaChangePolicyTypeDef",
    "CrawlsFilterTypeDef",
    "CreateBlueprintRequestRequestTypeDef",
    "CreateCsvClassifierRequestTypeDef",
    "CreateGrokClassifierRequestTypeDef",
    "CreateJsonClassifierRequestTypeDef",
    "CreateXMLClassifierRequestTypeDef",
    "CreateCustomEntityTypeRequestRequestTypeDef",
    "DataQualityTargetTableTypeDef",
    "CreateDevEndpointRequestRequestTypeDef",
    "ExecutionPropertyTypeDef",
    "JobCommandTypeDef",
    "SourceControlDetailsTypeDef",
    "PartitionIndexTypeDef",
    "CreateRegistryInputRequestTypeDef",
    "RegistryIdTypeDef",
    "SessionCommandTypeDef",
    "EventBatchingConditionTypeDef",
    "CreateWorkflowRequestRequestTypeDef",
    "DQResultsPublishingOptionsTypeDef",
    "DQStopJobOnFailureOptionsTypeDef",
    "EncryptionAtRestTypeDef",
    "DataLakePrincipalTypeDef",
    "DataQualityAnalyzerResultTypeDef",
    "DataQualityEvaluationRunAdditionalRunOptionsTypeDef",
    "DataQualityMetricValuesTypeDef",
    "DataQualityRuleResultTypeDef",
    "GlueTableOutputTypeDef",
    "DatabaseIdentifierTypeDef",
    "FederatedDatabaseTypeDef",
    "DatatypeTypeDef",
    "DecimalNumberOutputTypeDef",
    "DeleteBlueprintRequestRequestTypeDef",
    "DeleteClassifierRequestRequestTypeDef",
    "DeleteColumnStatisticsForPartitionRequestRequestTypeDef",
    "DeleteColumnStatisticsForTableRequestRequestTypeDef",
    "DeleteConnectionRequestRequestTypeDef",
    "DeleteCrawlerRequestRequestTypeDef",
    "DeleteCustomEntityTypeRequestRequestTypeDef",
    "DeleteDataQualityRulesetRequestRequestTypeDef",
    "DeleteDatabaseRequestRequestTypeDef",
    "DeleteDevEndpointRequestRequestTypeDef",
    "DeleteJobRequestRequestTypeDef",
    "DeleteMLTransformRequestRequestTypeDef",
    "DeletePartitionIndexRequestRequestTypeDef",
    "DeletePartitionRequestRequestTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "SchemaIdTypeDef",
    "DeleteSecurityConfigurationRequestRequestTypeDef",
    "DeleteSessionRequestRequestTypeDef",
    "DeleteTableOptimizerRequestRequestTypeDef",
    "DeleteTableRequestRequestTypeDef",
    "DeleteTableVersionRequestRequestTypeDef",
    "DeleteTriggerRequestRequestTypeDef",
    "DeleteUsageProfileRequestRequestTypeDef",
    "DeleteUserDefinedFunctionRequestRequestTypeDef",
    "DeleteWorkflowRequestRequestTypeDef",
    "DeltaTargetTypeDef",
    "DevEndpointCustomLibrariesTypeDef",
    "DirectSchemaChangePolicyTypeDef",
    "DropDuplicatesTypeDef",
    "DropFieldsTypeDef",
    "NullCheckBoxListTypeDef",
    "TransformConfigParameterOutputTypeDef",
    "EdgeTypeDef",
    "JobBookmarksEncryptionTypeDef",
    "S3EncryptionTypeDef",
    "ErrorDetailsTypeDef",
    "ExportLabelsTaskRunPropertiesTypeDef",
    "FederatedTableTypeDef",
    "FillMissingValuesTypeDef",
    "FilterValueOutputTypeDef",
    "FilterValueTypeDef",
    "FindMatchesParametersTypeDef",
    "FindMatchesTaskRunPropertiesTypeDef",
    "GetBlueprintRequestRequestTypeDef",
    "GetBlueprintRunRequestRequestTypeDef",
    "GetBlueprintRunsRequestRequestTypeDef",
    "GetCatalogImportStatusRequestRequestTypeDef",
    "GetClassifierRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "GetClassifiersRequestRequestTypeDef",
    "GetColumnStatisticsForPartitionRequestRequestTypeDef",
    "GetColumnStatisticsForTableRequestRequestTypeDef",
    "GetColumnStatisticsTaskRunRequestRequestTypeDef",
    "GetColumnStatisticsTaskRunsRequestRequestTypeDef",
    "GetConnectionRequestRequestTypeDef",
    "GetConnectionsFilterTypeDef",
    "GetCrawlerMetricsRequestRequestTypeDef",
    "GetCrawlerRequestRequestTypeDef",
    "GetCrawlersRequestRequestTypeDef",
    "GetCustomEntityTypeRequestRequestTypeDef",
    "GetDataCatalogEncryptionSettingsRequestRequestTypeDef",
    "GetDataQualityModelRequestRequestTypeDef",
    "GetDataQualityModelResultRequestRequestTypeDef",
    "StatisticModelResultTypeDef",
    "GetDataQualityResultRequestRequestTypeDef",
    "GetDataQualityRuleRecommendationRunRequestRequestTypeDef",
    "GetDataQualityRulesetEvaluationRunRequestRequestTypeDef",
    "GetDataQualityRulesetRequestRequestTypeDef",
    "GetDatabaseRequestRequestTypeDef",
    "GetDatabasesRequestRequestTypeDef",
    "GetDataflowGraphRequestRequestTypeDef",
    "GetDevEndpointRequestRequestTypeDef",
    "GetDevEndpointsRequestRequestTypeDef",
    "GetJobBookmarkRequestRequestTypeDef",
    "JobBookmarkEntryTypeDef",
    "GetJobRequestRequestTypeDef",
    "GetJobRunRequestRequestTypeDef",
    "GetJobRunsRequestRequestTypeDef",
    "GetJobsRequestRequestTypeDef",
    "GetMLTaskRunRequestRequestTypeDef",
    "TaskRunSortCriteriaTypeDef",
    "GetMLTransformRequestRequestTypeDef",
    "SchemaColumnTypeDef",
    "TransformSortCriteriaTypeDef",
    "MappingEntryTypeDef",
    "GetPartitionIndexesRequestRequestTypeDef",
    "GetPartitionRequestRequestTypeDef",
    "SegmentTypeDef",
    "GetResourcePoliciesRequestRequestTypeDef",
    "GluePolicyTypeDef",
    "GetResourcePolicyRequestRequestTypeDef",
    "SchemaVersionNumberTypeDef",
    "GetSecurityConfigurationRequestRequestTypeDef",
    "GetSecurityConfigurationsRequestRequestTypeDef",
    "GetSessionRequestRequestTypeDef",
    "GetStatementRequestRequestTypeDef",
    "GetTableOptimizerRequestRequestTypeDef",
    "GetTableVersionRequestRequestTypeDef",
    "GetTableVersionsRequestRequestTypeDef",
    "GetTagsRequestRequestTypeDef",
    "GetTriggerRequestRequestTypeDef",
    "GetTriggersRequestRequestTypeDef",
    "SupportedDialectTypeDef",
    "GetUsageProfileRequestRequestTypeDef",
    "GetUserDefinedFunctionRequestRequestTypeDef",
    "GetUserDefinedFunctionsRequestRequestTypeDef",
    "GetWorkflowRequestRequestTypeDef",
    "GetWorkflowRunPropertiesRequestRequestTypeDef",
    "GetWorkflowRunRequestRequestTypeDef",
    "GetWorkflowRunsRequestRequestTypeDef",
    "GlueStudioSchemaColumnTypeDef",
    "GlueTableTypeDef",
    "S3SourceAdditionalOptionsTypeDef",
    "HudiTargetTypeDef",
    "IcebergInputTypeDef",
    "IcebergOrphanFileDeletionConfigurationTypeDef",
    "IcebergOrphanFileDeletionMetricsTypeDef",
    "IcebergRetentionConfigurationTypeDef",
    "IcebergRetentionMetricsTypeDef",
    "IcebergTargetTypeDef",
    "ImportCatalogToGlueRequestRequestTypeDef",
    "ImportLabelsTaskRunPropertiesTypeDef",
    "JDBCConnectorOptionsOutputTypeDef",
    "JDBCConnectorOptionsTypeDef",
    "JdbcTargetTypeDef",
    "PredecessorTypeDef",
    "JoinColumnOutputTypeDef",
    "JoinColumnTypeDef",
    "KeySchemaElementTypeDef",
    "LabelingSetGenerationTaskRunPropertiesTypeDef",
    "ListBlueprintsRequestRequestTypeDef",
    "ListColumnStatisticsTaskRunsRequestRequestTypeDef",
    "ListCrawlersRequestRequestTypeDef",
    "ListCustomEntityTypesRequestRequestTypeDef",
    "ListDevEndpointsRequestRequestTypeDef",
    "ListJobsRequestRequestTypeDef",
    "ListRegistriesInputRequestTypeDef",
    "RegistryListItemTypeDef",
    "SchemaVersionListItemTypeDef",
    "SchemaListItemTypeDef",
    "ListSessionsRequestRequestTypeDef",
    "ListStatementsRequestRequestTypeDef",
    "ListTableOptimizerRunsRequestRequestTypeDef",
    "ListTriggersRequestRequestTypeDef",
    "ListUsageProfilesRequestRequestTypeDef",
    "UsageProfileDefinitionTypeDef",
    "ListWorkflowsRequestRequestTypeDef",
    "MLUserDataEncryptionTypeDef",
    "MappingTypeDef",
    "MergeTypeDef",
    "OtherMetadataValueListItemTypeDef",
    "MetadataKeyValuePairTypeDef",
    "MicrosoftSQLServerCatalogTargetTypeDef",
    "MySQLCatalogTargetTypeDef",
    "OAuth2ClientApplicationTypeDef",
    "OracleSQLCatalogTargetTypeDef",
    "OrderTypeDef",
    "PIIDetectionTypeDef",
    "PhysicalConnectionRequirementsTypeDef",
    "PostgreSQLCatalogTargetTypeDef",
    "PropertyPredicateTypeDef",
    "PutDataQualityProfileAnnotationRequestRequestTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "PutWorkflowRunPropertiesRequestRequestTypeDef",
    "RecipeActionOutputTypeDef",
    "RecipeActionTypeDef",
    "RecipeReferenceTypeDef",
    "UpsertRedshiftTargetOptionsOutputTypeDef",
    "RenameFieldTypeDef",
    "ResetJobBookmarkRequestRequestTypeDef",
    "ResourceUriTypeDef",
    "ResumeWorkflowRunRequestRequestTypeDef",
    "RunIdentifierTypeDef",
    "RunMetricsTypeDef",
    "RunStatementRequestRequestTypeDef",
    "S3DirectSourceAdditionalOptionsTypeDef",
    "S3TargetTypeDef",
    "SortCriterionTypeDef",
    "SelectFieldsTypeDef",
    "SelectFromCollectionTypeDef",
    "SerDeInfoOutputTypeDef",
    "SerDeInfoTypeDef",
    "SkewedInfoOutputTypeDef",
    "SkewedInfoTypeDef",
    "SqlAliasTypeDef",
    "SpigotTypeDef",
    "SplitFieldsTypeDef",
    "StartBlueprintRunRequestRequestTypeDef",
    "StartColumnStatisticsTaskRunRequestRequestTypeDef",
    "StartCrawlerRequestRequestTypeDef",
    "StartCrawlerScheduleRequestRequestTypeDef",
    "StartExportLabelsTaskRunRequestRequestTypeDef",
    "StartImportLabelsTaskRunRequestRequestTypeDef",
    "StartMLEvaluationTaskRunRequestRequestTypeDef",
    "StartMLLabelingSetGenerationTaskRunRequestRequestTypeDef",
    "StartTriggerRequestRequestTypeDef",
    "StartWorkflowRunRequestRequestTypeDef",
    "StartingEventBatchConditionTypeDef",
    "StatementOutputDataTypeDef",
    "TimestampedInclusionAnnotationTypeDef",
    "StopColumnStatisticsTaskRunRequestRequestTypeDef",
    "StopCrawlerRequestRequestTypeDef",
    "StopCrawlerScheduleRequestRequestTypeDef",
    "StopSessionRequestRequestTypeDef",
    "StopTriggerRequestRequestTypeDef",
    "StopWorkflowRunRequestRequestTypeDef",
    "TableIdentifierTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TransformConfigParameterTypeDef",
    "UnionTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateBlueprintRequestRequestTypeDef",
    "UpdateCsvClassifierRequestTypeDef",
    "UpdateGrokClassifierRequestTypeDef",
    "UpdateJsonClassifierRequestTypeDef",
    "UpdateXMLClassifierRequestTypeDef",
    "UpdateCrawlerScheduleRequestRequestTypeDef",
    "UpdateDataQualityRulesetRequestRequestTypeDef",
    "UpdateJobFromSourceControlRequestRequestTypeDef",
    "UpdateSourceControlFromJobRequestRequestTypeDef",
    "UpdateWorkflowRequestRequestTypeDef",
    "UpsertRedshiftTargetOptionsTypeDef",
    "ViewRepresentationInputTypeDef",
    "ViewRepresentationTypeDef",
    "WorkflowRunStatisticsTypeDef",
    "ActionOutputTypeDef",
    "ActionTypeDef",
    "StartJobRunRequestRequestTypeDef",
    "AggregateOutputTypeDef",
    "AggregateOperationUnionTypeDef",
    "AmazonRedshiftNodeDataOutputTypeDef",
    "AmazonRedshiftNodeDataTypeDef",
    "SnowflakeNodeDataOutputTypeDef",
    "SnowflakeNodeDataTypeDef",
    "ApplyMappingOutputTypeDef",
    "ApplyMappingPaginatorTypeDef",
    "BackfillErrorTypeDef",
    "BasicCatalogTargetUnionTypeDef",
    "BatchPutDataQualityStatisticAnnotationResponseTypeDef",
    "CancelMLTaskRunResponseTypeDef",
    "CheckSchemaVersionValidityResponseTypeDef",
    "CreateBlueprintResponseTypeDef",
    "CreateConnectionResponseTypeDef",
    "CreateCustomEntityTypeResponseTypeDef",
    "CreateDataQualityRulesetResponseTypeDef",
    "CreateDevEndpointResponseTypeDef",
    "CreateJobResponseTypeDef",
    "CreateMLTransformResponseTypeDef",
    "CreateRegistryResponseTypeDef",
    "CreateSchemaResponseTypeDef",
    "CreateScriptResponseTypeDef",
    "CreateSecurityConfigurationResponseTypeDef",
    "CreateTriggerResponseTypeDef",
    "CreateUsageProfileResponseTypeDef",
    "CreateWorkflowResponseTypeDef",
    "DeleteBlueprintResponseTypeDef",
    "DeleteCustomEntityTypeResponseTypeDef",
    "DeleteJobResponseTypeDef",
    "DeleteMLTransformResponseTypeDef",
    "DeleteRegistryResponseTypeDef",
    "DeleteSchemaResponseTypeDef",
    "DeleteSessionResponseTypeDef",
    "DeleteTriggerResponseTypeDef",
    "DeleteWorkflowResponseTypeDef",
    "GetCustomEntityTypeResponseTypeDef",
    "GetDataQualityModelResponseTypeDef",
    "GetPlanResponseTypeDef",
    "GetRegistryResponseTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "GetSchemaByDefinitionResponseTypeDef",
    "GetSchemaResponseTypeDef",
    "GetSchemaVersionResponseTypeDef",
    "GetSchemaVersionsDiffResponseTypeDef",
    "GetTagsResponseTypeDef",
    "GetWorkflowRunPropertiesResponseTypeDef",
    "ListBlueprintsResponseTypeDef",
    "ListColumnStatisticsTaskRunsResponseTypeDef",
    "ListCrawlersResponseTypeDef",
    "ListDevEndpointsResponseTypeDef",
    "ListJobsResponseTypeDef",
    "ListMLTransformsResponseTypeDef",
    "ListTriggersResponseTypeDef",
    "ListWorkflowsResponseTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "PutSchemaVersionMetadataResponseTypeDef",
    "RegisterSchemaVersionResponseTypeDef",
    "RemoveSchemaVersionMetadataResponseTypeDef",
    "ResumeWorkflowRunResponseTypeDef",
    "RunStatementResponseTypeDef",
    "StartBlueprintRunResponseTypeDef",
    "StartColumnStatisticsTaskRunResponseTypeDef",
    "StartDataQualityRuleRecommendationRunResponseTypeDef",
    "StartDataQualityRulesetEvaluationRunResponseTypeDef",
    "StartExportLabelsTaskRunResponseTypeDef",
    "StartImportLabelsTaskRunResponseTypeDef",
    "StartJobRunResponseTypeDef",
    "StartMLEvaluationTaskRunResponseTypeDef",
    "StartMLLabelingSetGenerationTaskRunResponseTypeDef",
    "StartTriggerResponseTypeDef",
    "StartWorkflowRunResponseTypeDef",
    "StopSessionResponseTypeDef",
    "StopTriggerResponseTypeDef",
    "UpdateBlueprintResponseTypeDef",
    "UpdateDataQualityRulesetResponseTypeDef",
    "UpdateJobFromSourceControlResponseTypeDef",
    "UpdateJobResponseTypeDef",
    "UpdateMLTransformResponseTypeDef",
    "UpdateRegistryResponseTypeDef",
    "UpdateSchemaResponseTypeDef",
    "UpdateSourceControlFromJobResponseTypeDef",
    "UpdateUsageProfileResponseTypeDef",
    "UpdateWorkflowResponseTypeDef",
    "BatchDeleteConnectionResponseTypeDef",
    "BatchGetTableOptimizerErrorTypeDef",
    "BatchStopJobRunErrorTypeDef",
    "BatchUpdatePartitionFailureEntryTypeDef",
    "ColumnErrorTypeDef",
    "PartitionErrorTypeDef",
    "TableErrorTypeDef",
    "TableVersionErrorTypeDef",
    "ViewValidationTypeDef",
    "BatchGetCustomEntityTypesResponseTypeDef",
    "ListCustomEntityTypesResponseTypeDef",
    "BatchGetDevEndpointsResponseTypeDef",
    "GetDevEndpointResponseTypeDef",
    "GetDevEndpointsResponseTypeDef",
    "BatchGetPartitionRequestRequestTypeDef",
    "PartitionValueListUnionTypeDef",
    "BatchGetTableOptimizerRequestRequestTypeDef",
    "BatchPutDataQualityStatisticAnnotationRequestRequestTypeDef",
    "DecimalNumberTypeDef",
    "GetBlueprintRunResponseTypeDef",
    "GetBlueprintRunsResponseTypeDef",
    "BlueprintTypeDef",
    "GetCatalogImportStatusResponseTypeDef",
    "CatalogKafkaSourceOutputTypeDef",
    "DirectKafkaSourceOutputTypeDef",
    "CatalogKinesisSourceOutputTypeDef",
    "DirectKinesisSourceOutputTypeDef",
    "GovernedCatalogTargetOutputTypeDef",
    "GovernedCatalogTargetTypeDef",
    "S3CatalogTargetOutputTypeDef",
    "S3CatalogTargetTypeDef",
    "S3DeltaCatalogTargetOutputTypeDef",
    "S3DeltaCatalogTargetTypeDef",
    "S3HudiCatalogTargetOutputTypeDef",
    "S3HudiCatalogTargetTypeDef",
    "CatalogTargetUnionTypeDef",
    "ClassifierTypeDef",
    "CodeGenNodeOutputTypeDef",
    "CodeGenNodeTypeDef",
    "LocationTypeDef",
    "GetColumnStatisticsTaskRunResponseTypeDef",
    "GetColumnStatisticsTaskRunsResponseTypeDef",
    "DateColumnStatisticsDataTypeDef",
    "GetTableRequestRequestTypeDef",
    "GetTablesRequestRequestTypeDef",
    "KafkaStreamingSourceOptionsTypeDef",
    "KinesisStreamingSourceOptionsTypeDef",
    "QuerySessionContextTypeDef",
    "TaskRunFilterCriteriaTypeDef",
    "TimestampFilterTypeDef",
    "ColumnUnionTypeDef",
    "CompactionMetricsTypeDef",
    "PredicateOutputTypeDef",
    "PredicateTypeDef",
    "ProfileConfigurationOutputTypeDef",
    "ConfigurationObjectUnionTypeDef",
    "FindMatchesMetricsTypeDef",
    "ConnectionsListUnionTypeDef",
    "ConnectorDataTargetUnionTypeDef",
    "CrawlerNodeDetailsTypeDef",
    "ListCrawlsResponseTypeDef",
    "GetCrawlerMetricsResponseTypeDef",
    "CrawlerTargetsOutputTypeDef",
    "ListCrawlsRequestRequestTypeDef",
    "CreateClassifierRequestRequestTypeDef",
    "CreateDataQualityRulesetRequestRequestTypeDef",
    "DataQualityRulesetFilterCriteriaTypeDef",
    "DataQualityRulesetListDetailsTypeDef",
    "GetDataQualityRulesetResponseTypeDef",
    "CreatePartitionIndexRequestRequestTypeDef",
    "CreateSchemaInputRequestTypeDef",
    "DeleteRegistryInputRequestTypeDef",
    "GetRegistryInputRequestTypeDef",
    "ListSchemasInputRequestTypeDef",
    "UpdateRegistryInputRequestTypeDef",
    "CreateSessionRequestRequestTypeDef",
    "SessionTypeDef",
    "EvaluateDataQualityMultiFrameOutputTypeDef",
    "EvaluateDataQualityMultiFrameTypeDef",
    "EvaluateDataQualityOutputTypeDef",
    "EvaluateDataQualityTypeDef",
    "DataCatalogEncryptionSettingsTypeDef",
    "PrincipalPermissionsOutputTypeDef",
    "PrincipalPermissionsTypeDef",
    "MetricBasedObservationTypeDef",
    "DataSourceOutputTypeDef",
    "NullValueFieldTypeDef",
    "DecimalColumnStatisticsDataOutputTypeDef",
    "DeleteSchemaInputRequestTypeDef",
    "DeleteSchemaVersionsInputRequestTypeDef",
    "GetSchemaByDefinitionInputRequestTypeDef",
    "GetSchemaInputRequestTypeDef",
    "ListSchemaVersionsInputRequestTypeDef",
    "RegisterSchemaVersionInputRequestTypeDef",
    "SchemaReferenceTypeDef",
    "DeltaTargetUnionTypeDef",
    "UpdateDevEndpointRequestRequestTypeDef",
    "S3DeltaDirectTargetOutputTypeDef",
    "S3DeltaDirectTargetTypeDef",
    "S3DirectTargetOutputTypeDef",
    "S3DirectTargetTypeDef",
    "S3GlueParquetTargetOutputTypeDef",
    "S3GlueParquetTargetTypeDef",
    "S3HudiDirectTargetOutputTypeDef",
    "S3HudiDirectTargetTypeDef",
    "DropDuplicatesUnionTypeDef",
    "DropFieldsUnionTypeDef",
    "EncryptionConfigurationOutputTypeDef",
    "EncryptionConfigurationTypeDef",
    "SchemaVersionErrorItemTypeDef",
    "FillMissingValuesUnionTypeDef",
    "FilterExpressionOutputTypeDef",
    "FilterValueUnionTypeDef",
    "TransformParametersTypeDef",
    "GetClassifiersRequestGetClassifiersPaginateTypeDef",
    "GetCrawlerMetricsRequestGetCrawlerMetricsPaginateTypeDef",
    "GetCrawlersRequestGetCrawlersPaginateTypeDef",
    "GetDatabasesRequestGetDatabasesPaginateTypeDef",
    "GetDevEndpointsRequestGetDevEndpointsPaginateTypeDef",
    "GetJobRunsRequestGetJobRunsPaginateTypeDef",
    "GetJobsRequestGetJobsPaginateTypeDef",
    "GetPartitionIndexesRequestGetPartitionIndexesPaginateTypeDef",
    "GetResourcePoliciesRequestGetResourcePoliciesPaginateTypeDef",
    "GetSecurityConfigurationsRequestGetSecurityConfigurationsPaginateTypeDef",
    "GetTableVersionsRequestGetTableVersionsPaginateTypeDef",
    "GetTablesRequestGetTablesPaginateTypeDef",
    "GetTriggersRequestGetTriggersPaginateTypeDef",
    "GetUserDefinedFunctionsRequestGetUserDefinedFunctionsPaginateTypeDef",
    "GetWorkflowRunsRequestGetWorkflowRunsPaginateTypeDef",
    "ListBlueprintsRequestListBlueprintsPaginateTypeDef",
    "ListJobsRequestListJobsPaginateTypeDef",
    "ListRegistriesInputListRegistriesPaginateTypeDef",
    "ListSchemaVersionsInputListSchemaVersionsPaginateTypeDef",
    "ListSchemasInputListSchemasPaginateTypeDef",
    "ListTableOptimizerRunsRequestListTableOptimizerRunsPaginateTypeDef",
    "ListTriggersRequestListTriggersPaginateTypeDef",
    "ListUsageProfilesRequestListUsageProfilesPaginateTypeDef",
    "ListWorkflowsRequestListWorkflowsPaginateTypeDef",
    "GetConnectionsRequestGetConnectionsPaginateTypeDef",
    "GetConnectionsRequestRequestTypeDef",
    "GetDataQualityModelResultResponseTypeDef",
    "GetJobBookmarkResponseTypeDef",
    "ResetJobBookmarkResponseTypeDef",
    "TransformFilterCriteriaTypeDef",
    "GetMappingResponseTypeDef",
    "GetPartitionsRequestGetPartitionsPaginateTypeDef",
    "GetPartitionsRequestRequestTypeDef",
    "GetResourcePoliciesResponseTypeDef",
    "GetSchemaVersionInputRequestTypeDef",
    "GetSchemaVersionsDiffInputRequestTypeDef",
    "UpdateSchemaInputRequestTypeDef",
    "GlueSchemaOutputTypeDef",
    "GlueSchemaTypeDef",
    "GlueTableUnionTypeDef",
    "GovernedCatalogSourceTypeDef",
    "S3CatalogSourceTypeDef",
    "HudiTargetUnionTypeDef",
    "OpenTableFormatInputTypeDef",
    "OrphanFileDeletionConfigurationTypeDef",
    "OrphanFileDeletionMetricsTypeDef",
    "RetentionConfigurationTypeDef",
    "RetentionMetricsTypeDef",
    "IcebergTargetUnionTypeDef",
    "JDBCConnectorOptionsUnionTypeDef",
    "JdbcTargetUnionTypeDef",
    "JobRunTypeDef",
    "JoinOutputTypeDef",
    "JoinColumnUnionTypeDef",
    "TaskRunPropertiesTypeDef",
    "ListRegistriesResponseTypeDef",
    "ListSchemaVersionsResponseTypeDef",
    "ListSchemasResponseTypeDef",
    "ListUsageProfilesResponseTypeDef",
    "TransformEncryptionTypeDef",
    "MappingUnionTypeDef",
    "MergeUnionTypeDef",
    "MetadataInfoTypeDef",
    "PutSchemaVersionMetadataInputRequestTypeDef",
    "QuerySchemaVersionMetadataInputRequestTypeDef",
    "RemoveSchemaVersionMetadataInputRequestTypeDef",
    "MicrosoftSQLServerCatalogTargetUnionTypeDef",
    "MySQLCatalogTargetUnionTypeDef",
    "OAuth2PropertiesInputTypeDef",
    "OAuth2PropertiesTypeDef",
    "OracleSQLCatalogTargetUnionTypeDef",
    "PIIDetectionUnionTypeDef",
    "PhysicalConnectionRequirementsUnionTypeDef",
    "PostgreSQLCatalogTargetUnionTypeDef",
    "RecipeStepOutputTypeDef",
    "RecipeActionUnionTypeDef",
    "RedshiftTargetOutputTypeDef",
    "RenameFieldUnionTypeDef",
    "UserDefinedFunctionInputTypeDef",
    "UserDefinedFunctionTypeDef",
    "S3TargetUnionTypeDef",
    "SearchTablesRequestRequestTypeDef",
    "SelectFieldsUnionTypeDef",
    "SelectFromCollectionUnionTypeDef",
    "SerDeInfoUnionTypeDef",
    "SkewedInfoUnionTypeDef",
    "SpigotUnionTypeDef",
    "SplitFieldsUnionTypeDef",
    "StatementOutputTypeDef",
    "StatisticAnnotationTypeDef",
    "StatisticSummaryTypeDef",
    "TransformConfigParameterUnionTypeDef",
    "UnionUnionTypeDef",
    "UpdateClassifierRequestRequestTypeDef",
    "UpsertRedshiftTargetOptionsUnionTypeDef",
    "ViewDefinitionInputTypeDef",
    "ViewDefinitionTypeDef",
    "ActionUnionTypeDef",
    "AggregateTypeDef",
    "AmazonRedshiftSourceOutputTypeDef",
    "AmazonRedshiftTargetOutputTypeDef",
    "AmazonRedshiftNodeDataUnionTypeDef",
    "SnowflakeTargetOutputTypeDef",
    "SnowflakeNodeDataUnionTypeDef",
    "PartitionIndexDescriptorTypeDef",
    "BatchStopJobRunResponseTypeDef",
    "BatchUpdatePartitionResponseTypeDef",
    "BatchCreatePartitionResponseTypeDef",
    "BatchDeletePartitionResponseTypeDef",
    "BatchDeleteTableResponseTypeDef",
    "BatchDeleteTableVersionResponseTypeDef",
    "StatusDetailsPaginatorTypeDef",
    "StatusDetailsTypeDef",
    "BatchDeletePartitionRequestRequestTypeDef",
    "DecimalNumberUnionTypeDef",
    "BatchGetBlueprintsResponseTypeDef",
    "GetBlueprintResponseTypeDef",
    "GovernedCatalogTargetUnionTypeDef",
    "S3CatalogTargetUnionTypeDef",
    "S3DeltaCatalogTargetUnionTypeDef",
    "S3HudiCatalogTargetUnionTypeDef",
    "GetClassifierResponseTypeDef",
    "GetClassifiersResponseTypeDef",
    "GetDataflowGraphResponseTypeDef",
    "CodeGenNodeUnionTypeDef",
    "GetMappingRequestRequestTypeDef",
    "GetPlanRequestRequestTypeDef",
    "DateColumnStatisticsDataUnionTypeDef",
    "KafkaStreamingSourceOptionsUnionTypeDef",
    "KinesisStreamingSourceOptionsUnionTypeDef",
    "GetUnfilteredPartitionMetadataRequestRequestTypeDef",
    "GetUnfilteredPartitionsMetadataRequestRequestTypeDef",
    "GetUnfilteredTableMetadataRequestRequestTypeDef",
    "GetMLTaskRunsRequestRequestTypeDef",
    "ListDataQualityStatisticAnnotationsRequestRequestTypeDef",
    "ListDataQualityStatisticsRequestRequestTypeDef",
    "TriggerTypeDef",
    "PredicateUnionTypeDef",
    "GetUsageProfileResponseTypeDef",
    "ProfileConfigurationTypeDef",
    "EvaluationMetricsTypeDef",
    "CrawlerTypeDef",
    "ListDataQualityRulesetsRequestRequestTypeDef",
    "ListDataQualityRulesetsResponseTypeDef",
    "CreateSessionResponseTypeDef",
    "GetSessionResponseTypeDef",
    "ListSessionsResponseTypeDef",
    "EvaluateDataQualityMultiFrameUnionTypeDef",
    "EvaluateDataQualityUnionTypeDef",
    "GetDataCatalogEncryptionSettingsResponseTypeDef",
    "PutDataCatalogEncryptionSettingsRequestRequestTypeDef",
    "DatabaseTypeDef",
    "PrincipalPermissionsUnionTypeDef",
    "DataQualityObservationTypeDef",
    "DataQualityResultDescriptionTypeDef",
    "DataQualityRuleRecommendationRunDescriptionTypeDef",
    "DataQualityRulesetEvaluationRunDescriptionTypeDef",
    "GetDataQualityRuleRecommendationRunResponseTypeDef",
    "GetDataQualityRulesetEvaluationRunResponseTypeDef",
    "DropNullFieldsOutputTypeDef",
    "DropNullFieldsTypeDef",
    "ColumnStatisticsDataOutputTypeDef",
    "StorageDescriptorOutputTypeDef",
    "S3DeltaDirectTargetUnionTypeDef",
    "S3DirectTargetUnionTypeDef",
    "S3GlueParquetTargetUnionTypeDef",
    "S3HudiDirectTargetUnionTypeDef",
    "SecurityConfigurationTypeDef",
    "CreateSecurityConfigurationRequestRequestTypeDef",
    "DeleteSchemaVersionsResponseTypeDef",
    "FilterOutputTypeDef",
    "FilterExpressionTypeDef",
    "UpdateMLTransformRequestRequestTypeDef",
    "GetMLTransformsRequestRequestTypeDef",
    "ListMLTransformsRequestRequestTypeDef",
    "AthenaConnectorSourceOutputTypeDef",
    "CatalogDeltaSourceOutputTypeDef",
    "CatalogHudiSourceOutputTypeDef",
    "ConnectorDataSourceOutputTypeDef",
    "CustomCodeOutputTypeDef",
    "DynamicTransformOutputTypeDef",
    "JDBCConnectorSourceOutputTypeDef",
    "JDBCConnectorTargetOutputTypeDef",
    "S3CatalogDeltaSourceOutputTypeDef",
    "S3CatalogHudiSourceOutputTypeDef",
    "S3CsvSourceOutputTypeDef",
    "S3DeltaSourceOutputTypeDef",
    "S3HudiSourceOutputTypeDef",
    "S3JsonSourceOutputTypeDef",
    "S3ParquetSourceOutputTypeDef",
    "SnowflakeSourceOutputTypeDef",
    "SparkConnectorSourceOutputTypeDef",
    "SparkConnectorTargetOutputTypeDef",
    "SparkSQLOutputTypeDef",
    "CatalogDeltaSourceTypeDef",
    "CatalogHudiSourceTypeDef",
    "ConnectorDataSourceTypeDef",
    "CustomCodeTypeDef",
    "GlueSchemaUnionTypeDef",
    "JDBCConnectorTargetTypeDef",
    "S3CatalogDeltaSourceTypeDef",
    "S3CatalogHudiSourceTypeDef",
    "S3CsvSourceTypeDef",
    "S3DeltaSourceTypeDef",
    "S3HudiSourceTypeDef",
    "S3JsonSourceTypeDef",
    "S3ParquetSourceTypeDef",
    "SparkConnectorSourceTypeDef",
    "SparkConnectorTargetTypeDef",
    "SparkSQLTypeDef",
    "DataSourceTypeDef",
    "TableOptimizerConfigurationTypeDef",
    "TableOptimizerRunTypeDef",
    "GetJobRunResponseTypeDef",
    "GetJobRunsResponseTypeDef",
    "JobNodeDetailsTypeDef",
    "JoinTypeDef",
    "GetMLTaskRunResponseTypeDef",
    "TaskRunTypeDef",
    "CreateMLTransformRequestRequestTypeDef",
    "ApplyMappingTypeDef",
    "QuerySchemaVersionMetadataResponseTypeDef",
    "AuthenticationConfigurationInputTypeDef",
    "AuthenticationConfigurationTypeDef",
    "RecipeOutputTypeDef",
    "RecipeStepTypeDef",
    "CreateUserDefinedFunctionRequestRequestTypeDef",
    "UpdateUserDefinedFunctionRequestRequestTypeDef",
    "GetUserDefinedFunctionResponseTypeDef",
    "GetUserDefinedFunctionsResponseTypeDef",
    "CrawlerTargetsTypeDef",
    "StorageDescriptorTypeDef",
    "StatementTypeDef",
    "ListDataQualityStatisticAnnotationsResponseTypeDef",
    "ListDataQualityStatisticsResponseTypeDef",
    "DynamicTransformTypeDef",
    "RedshiftTargetTypeDef",
    "CreateTriggerRequestRequestTypeDef",
    "AggregateUnionTypeDef",
    "AmazonRedshiftSourceTypeDef",
    "AmazonRedshiftTargetTypeDef",
    "SnowflakeSourceTypeDef",
    "SnowflakeTargetTypeDef",
    "GetPartitionIndexesResponseTypeDef",
    "TableStatusPaginatorTypeDef",
    "TableStatusTypeDef",
    "DecimalColumnStatisticsDataTypeDef",
    "CreateScriptRequestRequestTypeDef",
    "CatalogKafkaSourceTypeDef",
    "DirectKafkaSourceTypeDef",
    "CatalogKinesisSourceTypeDef",
    "DirectKinesisSourceTypeDef",
    "BatchGetTriggersResponseTypeDef",
    "GetTriggerResponseTypeDef",
    "GetTriggersResponseTypeDef",
    "TriggerNodeDetailsTypeDef",
    "UpdateTriggerResponseTypeDef",
    "TriggerUpdateTypeDef",
    "CreateUsageProfileRequestRequestTypeDef",
    "UpdateUsageProfileRequestRequestTypeDef",
    "GetMLTransformResponseTypeDef",
    "MLTransformTypeDef",
    "BatchGetCrawlersResponseTypeDef",
    "GetCrawlerResponseTypeDef",
    "GetCrawlersResponseTypeDef",
    "GetDatabaseResponseTypeDef",
    "GetDatabasesResponseTypeDef",
    "DatabaseInputTypeDef",
    "DataQualityResultTypeDef",
    "GetDataQualityResultResponseTypeDef",
    "ListDataQualityResultsResponseTypeDef",
    "ListDataQualityRuleRecommendationRunsResponseTypeDef",
    "ListDataQualityRulesetEvaluationRunsResponseTypeDef",
    "DropNullFieldsUnionTypeDef",
    "ColumnStatisticsOutputTypeDef",
    "PartitionTypeDef",
    "GetSecurityConfigurationResponseTypeDef",
    "GetSecurityConfigurationsResponseTypeDef",
    "FilterExpressionUnionTypeDef",
    "CatalogDeltaSourceUnionTypeDef",
    "CatalogHudiSourceUnionTypeDef",
    "ConnectorDataSourceUnionTypeDef",
    "CustomCodeUnionTypeDef",
    "AthenaConnectorSourceTypeDef",
    "JDBCConnectorSourceTypeDef",
    "JDBCConnectorTargetUnionTypeDef",
    "S3CatalogDeltaSourceUnionTypeDef",
    "S3CatalogHudiSourceUnionTypeDef",
    "S3CsvSourceUnionTypeDef",
    "S3DeltaSourceUnionTypeDef",
    "S3HudiSourceUnionTypeDef",
    "S3JsonSourceUnionTypeDef",
    "S3ParquetSourceUnionTypeDef",
    "SparkConnectorSourceUnionTypeDef",
    "SparkConnectorTargetUnionTypeDef",
    "SparkSQLUnionTypeDef",
    "DataSourceUnionTypeDef",
    "StartDataQualityRuleRecommendationRunRequestRequestTypeDef",
    "CreateTableOptimizerRequestRequestTypeDef",
    "UpdateTableOptimizerRequestRequestTypeDef",
    "ListTableOptimizerRunsResponseTypeDef",
    "TableOptimizerTypeDef",
    "JoinUnionTypeDef",
    "GetMLTaskRunsResponseTypeDef",
    "ApplyMappingUnionTypeDef",
    "ConnectionInputTypeDef",
    "TestConnectionInputTypeDef",
    "ConnectionTypeDef",
    "CodeGenConfigurationNodeOutputTypeDef",
    "CodeGenConfigurationNodePaginatorTypeDef",
    "RecipeStepUnionTypeDef",
    "CreateCrawlerRequestRequestTypeDef",
    "UpdateCrawlerRequestRequestTypeDef",
    "StorageDescriptorUnionTypeDef",
    "GetStatementResponseTypeDef",
    "ListStatementsResponseTypeDef",
    "DynamicTransformUnionTypeDef",
    "RedshiftTargetUnionTypeDef",
    "AmazonRedshiftSourceUnionTypeDef",
    "AmazonRedshiftTargetUnionTypeDef",
    "SnowflakeSourceUnionTypeDef",
    "SnowflakeTargetUnionTypeDef",
    "TablePaginatorTypeDef",
    "TableTypeDef",
    "DecimalColumnStatisticsDataUnionTypeDef",
    "CatalogKafkaSourceUnionTypeDef",
    "DirectKafkaSourceUnionTypeDef",
    "CatalogKinesisSourceUnionTypeDef",
    "DirectKinesisSourceUnionTypeDef",
    "NodeTypeDef",
    "UpdateTriggerRequestRequestTypeDef",
    "GetMLTransformsResponseTypeDef",
    "CreateDatabaseRequestRequestTypeDef",
    "UpdateDatabaseRequestRequestTypeDef",
    "BatchGetDataQualityResultResponseTypeDef",
    "ColumnStatisticsErrorTypeDef",
    "GetColumnStatisticsForPartitionResponseTypeDef",
    "GetColumnStatisticsForTableResponseTypeDef",
    "BatchGetPartitionResponseTypeDef",
    "GetPartitionResponseTypeDef",
    "GetPartitionsResponseTypeDef",
    "GetUnfilteredPartitionMetadataResponseTypeDef",
    "UnfilteredPartitionTypeDef",
    "FilterTypeDef",
    "AthenaConnectorSourceUnionTypeDef",
    "JDBCConnectorSourceUnionTypeDef",
    "DataQualityResultFilterCriteriaTypeDef",
    "DataQualityRuleRecommendationRunFilterTypeDef",
    "DataQualityRulesetEvaluationRunFilterTypeDef",
    "StartDataQualityRulesetEvaluationRunRequestRequestTypeDef",
    "BatchTableOptimizerTypeDef",
    "GetTableOptimizerResponseTypeDef",
    "CreateConnectionRequestRequestTypeDef",
    "UpdateConnectionRequestRequestTypeDef",
    "TestConnectionRequestRequestTypeDef",
    "GetConnectionResponseTypeDef",
    "GetConnectionsResponseTypeDef",
    "JobTypeDef",
    "JobPaginatorTypeDef",
    "RecipeTypeDef",
    "PartitionInputTypeDef",
    "TableInputTypeDef",
    "GetTablesResponsePaginatorTypeDef",
    "TableVersionPaginatorTypeDef",
    "GetTableResponseTypeDef",
    "GetTablesResponseTypeDef",
    "GetUnfilteredTableMetadataResponseTypeDef",
    "SearchTablesResponseTypeDef",
    "TableVersionTypeDef",
    "ColumnStatisticsDataTypeDef",
    "WorkflowGraphTypeDef",
    "UpdateColumnStatisticsForPartitionResponseTypeDef",
    "UpdateColumnStatisticsForTableResponseTypeDef",
    "GetUnfilteredPartitionsMetadataResponseTypeDef",
    "FilterUnionTypeDef",
    "ListDataQualityResultsRequestRequestTypeDef",
    "ListDataQualityRuleRecommendationRunsRequestRequestTypeDef",
    "ListDataQualityRulesetEvaluationRunsRequestRequestTypeDef",
    "BatchGetTableOptimizerResponseTypeDef",
    "BatchGetJobsResponseTypeDef",
    "GetJobResponseTypeDef",
    "GetJobsResponseTypeDef",
    "GetJobsResponsePaginatorTypeDef",
    "RecipeUnionTypeDef",
    "BatchCreatePartitionRequestRequestTypeDef",
    "BatchUpdatePartitionRequestEntryTypeDef",
    "CreatePartitionRequestRequestTypeDef",
    "UpdatePartitionRequestRequestTypeDef",
    "CreateTableRequestRequestTypeDef",
    "UpdateTableRequestRequestTypeDef",
    "GetTableVersionsResponsePaginatorTypeDef",
    "GetTableVersionResponseTypeDef",
    "GetTableVersionsResponseTypeDef",
    "ColumnStatisticsDataUnionTypeDef",
    "WorkflowRunTypeDef",
    "CodeGenConfigurationNodeTypeDef",
    "BatchUpdatePartitionRequestRequestTypeDef",
    "ColumnStatisticsTypeDef",
    "GetWorkflowRunResponseTypeDef",
    "GetWorkflowRunsResponseTypeDef",
    "WorkflowTypeDef",
    "CodeGenConfigurationNodeUnionTypeDef",
    "ColumnStatisticsUnionTypeDef",
    "UpdateColumnStatisticsForTableRequestRequestTypeDef",
    "BatchGetWorkflowsResponseTypeDef",
    "GetWorkflowResponseTypeDef",
    "CreateJobRequestRequestTypeDef",
    "JobUpdateTypeDef",
    "UpdateColumnStatisticsForPartitionRequestRequestTypeDef",
    "UpdateJobRequestRequestTypeDef",
)

NotificationPropertyTypeDef = TypedDict(
    "NotificationPropertyTypeDef",
    {
        "NotifyDelayAfter": NotRequired[int],
    },
)
AggregateOperationOutputTypeDef = TypedDict(
    "AggregateOperationOutputTypeDef",
    {
        "Column": List[str],
        "AggFunc": AggFunctionType,
    },
)
AggregateOperationTypeDef = TypedDict(
    "AggregateOperationTypeDef",
    {
        "Column": Sequence[str],
        "AggFunc": AggFunctionType,
    },
)
AmazonRedshiftAdvancedOptionTypeDef = TypedDict(
    "AmazonRedshiftAdvancedOptionTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
OptionTypeDef = TypedDict(
    "OptionTypeDef",
    {
        "Value": NotRequired[str],
        "Label": NotRequired[str],
        "Description": NotRequired[str],
    },
)
AnnotationErrorTypeDef = TypedDict(
    "AnnotationErrorTypeDef",
    {
        "ProfileId": NotRequired[str],
        "StatisticId": NotRequired[str],
        "FailureReason": NotRequired[str],
    },
)
MappingOutputTypeDef = TypedDict(
    "MappingOutputTypeDef",
    {
        "ToKey": NotRequired[str],
        "FromPath": NotRequired[List[str]],
        "FromType": NotRequired[str],
        "ToType": NotRequired[str],
        "Dropped": NotRequired[bool],
        "Children": NotRequired[List[Dict[str, Any]]],
    },
)
MappingPaginatorTypeDef = TypedDict(
    "MappingPaginatorTypeDef",
    {
        "ToKey": NotRequired[str],
        "FromPath": NotRequired[List[str]],
        "FromType": NotRequired[str],
        "ToType": NotRequired[str],
        "Dropped": NotRequired[bool],
        "Children": NotRequired[List[Dict[str, Any]]],
    },
)
AuditContextTypeDef = TypedDict(
    "AuditContextTypeDef",
    {
        "AdditionalAuditContext": NotRequired[str],
        "RequestedColumns": NotRequired[Sequence[str]],
        "AllColumnsRequested": NotRequired[bool],
    },
)
AuthorizationCodePropertiesTypeDef = TypedDict(
    "AuthorizationCodePropertiesTypeDef",
    {
        "AuthorizationCode": NotRequired[str],
        "RedirectUri": NotRequired[str],
    },
)
PartitionValueListOutputTypeDef = TypedDict(
    "PartitionValueListOutputTypeDef",
    {
        "Values": List[str],
    },
)
BasicCatalogTargetOutputTypeDef = TypedDict(
    "BasicCatalogTargetOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Database": str,
        "Table": str,
        "PartitionKeys": NotRequired[List[List[str]]],
    },
)
BasicCatalogTargetTypeDef = TypedDict(
    "BasicCatalogTargetTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "Database": str,
        "Table": str,
        "PartitionKeys": NotRequired[Sequence[Sequence[str]]],
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
BatchDeleteConnectionRequestRequestTypeDef = TypedDict(
    "BatchDeleteConnectionRequestRequestTypeDef",
    {
        "ConnectionNameList": Sequence[str],
        "CatalogId": NotRequired[str],
    },
)
ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef",
    {
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)
BatchDeleteTableRequestRequestTypeDef = TypedDict(
    "BatchDeleteTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TablesToDelete": Sequence[str],
        "CatalogId": NotRequired[str],
        "TransactionId": NotRequired[str],
    },
)
BatchDeleteTableVersionRequestRequestTypeDef = TypedDict(
    "BatchDeleteTableVersionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "VersionIds": Sequence[str],
        "CatalogId": NotRequired[str],
    },
)
BatchGetBlueprintsRequestRequestTypeDef = TypedDict(
    "BatchGetBlueprintsRequestRequestTypeDef",
    {
        "Names": Sequence[str],
        "IncludeBlueprint": NotRequired[bool],
        "IncludeParameterSpec": NotRequired[bool],
    },
)
BatchGetCrawlersRequestRequestTypeDef = TypedDict(
    "BatchGetCrawlersRequestRequestTypeDef",
    {
        "CrawlerNames": Sequence[str],
    },
)
BatchGetCustomEntityTypesRequestRequestTypeDef = TypedDict(
    "BatchGetCustomEntityTypesRequestRequestTypeDef",
    {
        "Names": Sequence[str],
    },
)
CustomEntityTypeTypeDef = TypedDict(
    "CustomEntityTypeTypeDef",
    {
        "Name": str,
        "RegexString": str,
        "ContextWords": NotRequired[List[str]],
    },
)
BatchGetDataQualityResultRequestRequestTypeDef = TypedDict(
    "BatchGetDataQualityResultRequestRequestTypeDef",
    {
        "ResultIds": Sequence[str],
    },
)
BatchGetDevEndpointsRequestRequestTypeDef = TypedDict(
    "BatchGetDevEndpointsRequestRequestTypeDef",
    {
        "DevEndpointNames": Sequence[str],
    },
)
DevEndpointTypeDef = TypedDict(
    "DevEndpointTypeDef",
    {
        "EndpointName": NotRequired[str],
        "RoleArn": NotRequired[str],
        "SecurityGroupIds": NotRequired[List[str]],
        "SubnetId": NotRequired[str],
        "YarnEndpointAddress": NotRequired[str],
        "PrivateAddress": NotRequired[str],
        "ZeppelinRemoteSparkInterpreterPort": NotRequired[int],
        "PublicAddress": NotRequired[str],
        "Status": NotRequired[str],
        "WorkerType": NotRequired[WorkerTypeType],
        "GlueVersion": NotRequired[str],
        "NumberOfWorkers": NotRequired[int],
        "NumberOfNodes": NotRequired[int],
        "AvailabilityZone": NotRequired[str],
        "VpcId": NotRequired[str],
        "ExtraPythonLibsS3Path": NotRequired[str],
        "ExtraJarsS3Path": NotRequired[str],
        "FailureReason": NotRequired[str],
        "LastUpdateStatus": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "LastModifiedTimestamp": NotRequired[datetime],
        "PublicKey": NotRequired[str],
        "PublicKeys": NotRequired[List[str]],
        "SecurityConfiguration": NotRequired[str],
        "Arguments": NotRequired[Dict[str, str]],
    },
)
BatchGetJobsRequestRequestTypeDef = TypedDict(
    "BatchGetJobsRequestRequestTypeDef",
    {
        "JobNames": Sequence[str],
    },
)
PartitionValueListTypeDef = TypedDict(
    "PartitionValueListTypeDef",
    {
        "Values": Sequence[str],
    },
)
BatchGetTableOptimizerEntryTypeDef = TypedDict(
    "BatchGetTableOptimizerEntryTypeDef",
    {
        "catalogId": NotRequired[str],
        "databaseName": NotRequired[str],
        "tableName": NotRequired[str],
        "type": NotRequired[TableOptimizerTypeType],
    },
)
BatchGetTriggersRequestRequestTypeDef = TypedDict(
    "BatchGetTriggersRequestRequestTypeDef",
    {
        "TriggerNames": Sequence[str],
    },
)
BatchGetWorkflowsRequestRequestTypeDef = TypedDict(
    "BatchGetWorkflowsRequestRequestTypeDef",
    {
        "Names": Sequence[str],
        "IncludeGraph": NotRequired[bool],
    },
)
DatapointInclusionAnnotationTypeDef = TypedDict(
    "DatapointInclusionAnnotationTypeDef",
    {
        "ProfileId": NotRequired[str],
        "StatisticId": NotRequired[str],
        "InclusionAnnotation": NotRequired[InclusionAnnotationValueType],
    },
)
BatchStopJobRunRequestRequestTypeDef = TypedDict(
    "BatchStopJobRunRequestRequestTypeDef",
    {
        "JobName": str,
        "JobRunIds": Sequence[str],
    },
)
BatchStopJobRunSuccessfulSubmissionTypeDef = TypedDict(
    "BatchStopJobRunSuccessfulSubmissionTypeDef",
    {
        "JobName": NotRequired[str],
        "JobRunId": NotRequired[str],
    },
)
BinaryColumnStatisticsDataTypeDef = TypedDict(
    "BinaryColumnStatisticsDataTypeDef",
    {
        "MaximumLength": int,
        "AverageLength": float,
        "NumberOfNulls": int,
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
BlueprintDetailsTypeDef = TypedDict(
    "BlueprintDetailsTypeDef",
    {
        "BlueprintName": NotRequired[str],
        "RunId": NotRequired[str],
    },
)
BlueprintRunTypeDef = TypedDict(
    "BlueprintRunTypeDef",
    {
        "BlueprintName": NotRequired[str],
        "RunId": NotRequired[str],
        "WorkflowName": NotRequired[str],
        "State": NotRequired[BlueprintRunStateType],
        "StartedOn": NotRequired[datetime],
        "CompletedOn": NotRequired[datetime],
        "ErrorMessage": NotRequired[str],
        "RollbackErrorMessage": NotRequired[str],
        "Parameters": NotRequired[str],
        "RoleArn": NotRequired[str],
    },
)
LastActiveDefinitionTypeDef = TypedDict(
    "LastActiveDefinitionTypeDef",
    {
        "Description": NotRequired[str],
        "LastModifiedOn": NotRequired[datetime],
        "ParameterSpec": NotRequired[str],
        "BlueprintLocation": NotRequired[str],
        "BlueprintServiceLocation": NotRequired[str],
    },
)
BooleanColumnStatisticsDataTypeDef = TypedDict(
    "BooleanColumnStatisticsDataTypeDef",
    {
        "NumberOfTrues": int,
        "NumberOfFalses": int,
        "NumberOfNulls": int,
    },
)
CancelDataQualityRuleRecommendationRunRequestRequestTypeDef = TypedDict(
    "CancelDataQualityRuleRecommendationRunRequestRequestTypeDef",
    {
        "RunId": str,
    },
)
CancelDataQualityRulesetEvaluationRunRequestRequestTypeDef = TypedDict(
    "CancelDataQualityRulesetEvaluationRunRequestRequestTypeDef",
    {
        "RunId": str,
    },
)
CancelMLTaskRunRequestRequestTypeDef = TypedDict(
    "CancelMLTaskRunRequestRequestTypeDef",
    {
        "TransformId": str,
        "TaskRunId": str,
    },
)
CancelStatementRequestRequestTypeDef = TypedDict(
    "CancelStatementRequestRequestTypeDef",
    {
        "SessionId": str,
        "Id": int,
        "RequestOrigin": NotRequired[str],
    },
)
CatalogEntryTypeDef = TypedDict(
    "CatalogEntryTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)
CatalogImportStatusTypeDef = TypedDict(
    "CatalogImportStatusTypeDef",
    {
        "ImportCompleted": NotRequired[bool],
        "ImportTime": NotRequired[datetime],
        "ImportedBy": NotRequired[str],
    },
)
KafkaStreamingSourceOptionsOutputTypeDef = TypedDict(
    "KafkaStreamingSourceOptionsOutputTypeDef",
    {
        "BootstrapServers": NotRequired[str],
        "SecurityProtocol": NotRequired[str],
        "ConnectionName": NotRequired[str],
        "TopicName": NotRequired[str],
        "Assign": NotRequired[str],
        "SubscribePattern": NotRequired[str],
        "Classification": NotRequired[str],
        "Delimiter": NotRequired[str],
        "StartingOffsets": NotRequired[str],
        "EndingOffsets": NotRequired[str],
        "PollTimeoutMs": NotRequired[int],
        "NumRetries": NotRequired[int],
        "RetryIntervalMs": NotRequired[int],
        "MaxOffsetsPerTrigger": NotRequired[int],
        "MinPartitions": NotRequired[int],
        "IncludeHeaders": NotRequired[bool],
        "AddRecordTimestamp": NotRequired[str],
        "EmitConsumerLagMetrics": NotRequired[str],
        "StartingTimestamp": NotRequired[datetime],
    },
)
StreamingDataPreviewOptionsTypeDef = TypedDict(
    "StreamingDataPreviewOptionsTypeDef",
    {
        "PollingTime": NotRequired[int],
        "RecordPollingLimit": NotRequired[int],
    },
)
KinesisStreamingSourceOptionsOutputTypeDef = TypedDict(
    "KinesisStreamingSourceOptionsOutputTypeDef",
    {
        "EndpointUrl": NotRequired[str],
        "StreamName": NotRequired[str],
        "Classification": NotRequired[str],
        "Delimiter": NotRequired[str],
        "StartingPosition": NotRequired[StartingPositionType],
        "MaxFetchTimeInMs": NotRequired[int],
        "MaxFetchRecordsPerShard": NotRequired[int],
        "MaxRecordPerRead": NotRequired[int],
        "AddIdleTimeBetweenReads": NotRequired[bool],
        "IdleTimeBetweenReadsInMs": NotRequired[int],
        "DescribeShardInterval": NotRequired[int],
        "NumRetries": NotRequired[int],
        "RetryIntervalMs": NotRequired[int],
        "MaxRetryIntervalMs": NotRequired[int],
        "AvoidEmptyBatches": NotRequired[bool],
        "StreamArn": NotRequired[str],
        "RoleArn": NotRequired[str],
        "RoleSessionName": NotRequired[str],
        "AddRecordTimestamp": NotRequired[str],
        "EmitConsumerLagMetrics": NotRequired[str],
        "StartingTimestamp": NotRequired[datetime],
    },
)
CatalogSchemaChangePolicyTypeDef = TypedDict(
    "CatalogSchemaChangePolicyTypeDef",
    {
        "EnableUpdateCatalog": NotRequired[bool],
        "UpdateBehavior": NotRequired[UpdateCatalogBehaviorType],
    },
)
CatalogSourceTypeDef = TypedDict(
    "CatalogSourceTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
    },
)
CatalogTargetOutputTypeDef = TypedDict(
    "CatalogTargetOutputTypeDef",
    {
        "DatabaseName": str,
        "Tables": List[str],
        "ConnectionName": NotRequired[str],
        "EventQueueArn": NotRequired[str],
        "DlqEventQueueArn": NotRequired[str],
    },
)
CatalogTargetTypeDef = TypedDict(
    "CatalogTargetTypeDef",
    {
        "DatabaseName": str,
        "Tables": Sequence[str],
        "ConnectionName": NotRequired[str],
        "EventQueueArn": NotRequired[str],
        "DlqEventQueueArn": NotRequired[str],
    },
)
CheckSchemaVersionValidityInputRequestTypeDef = TypedDict(
    "CheckSchemaVersionValidityInputRequestTypeDef",
    {
        "DataFormat": DataFormatType,
        "SchemaDefinition": str,
    },
)
CsvClassifierTypeDef = TypedDict(
    "CsvClassifierTypeDef",
    {
        "Name": str,
        "CreationTime": NotRequired[datetime],
        "LastUpdated": NotRequired[datetime],
        "Version": NotRequired[int],
        "Delimiter": NotRequired[str],
        "QuoteSymbol": NotRequired[str],
        "ContainsHeader": NotRequired[CsvHeaderOptionType],
        "Header": NotRequired[List[str]],
        "DisableValueTrimming": NotRequired[bool],
        "AllowSingleColumn": NotRequired[bool],
        "CustomDatatypeConfigured": NotRequired[bool],
        "CustomDatatypes": NotRequired[List[str]],
        "Serde": NotRequired[CsvSerdeOptionType],
    },
)
GrokClassifierTypeDef = TypedDict(
    "GrokClassifierTypeDef",
    {
        "Name": str,
        "Classification": str,
        "GrokPattern": str,
        "CreationTime": NotRequired[datetime],
        "LastUpdated": NotRequired[datetime],
        "Version": NotRequired[int],
        "CustomPatterns": NotRequired[str],
    },
)
JsonClassifierTypeDef = TypedDict(
    "JsonClassifierTypeDef",
    {
        "Name": str,
        "JsonPath": str,
        "CreationTime": NotRequired[datetime],
        "LastUpdated": NotRequired[datetime],
        "Version": NotRequired[int],
    },
)
XMLClassifierTypeDef = TypedDict(
    "XMLClassifierTypeDef",
    {
        "Name": str,
        "Classification": str,
        "CreationTime": NotRequired[datetime],
        "LastUpdated": NotRequired[datetime],
        "Version": NotRequired[int],
        "RowTag": NotRequired[str],
    },
)
CloudWatchEncryptionTypeDef = TypedDict(
    "CloudWatchEncryptionTypeDef",
    {
        "CloudWatchEncryptionMode": NotRequired[CloudWatchEncryptionModeType],
        "KmsKeyArn": NotRequired[str],
    },
)
ConnectorDataTargetOutputTypeDef = TypedDict(
    "ConnectorDataTargetOutputTypeDef",
    {
        "Name": str,
        "ConnectionType": str,
        "Data": Dict[str, str],
        "Inputs": NotRequired[List[str]],
    },
)
DirectJDBCSourceTypeDef = TypedDict(
    "DirectJDBCSourceTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
        "ConnectionName": str,
        "ConnectionType": JDBCConnectionTypeType,
        "RedshiftTmpDir": NotRequired[str],
    },
)
DropDuplicatesOutputTypeDef = TypedDict(
    "DropDuplicatesOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Columns": NotRequired[List[List[str]]],
    },
)
DropFieldsOutputTypeDef = TypedDict(
    "DropFieldsOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Paths": List[List[str]],
    },
)
DynamoDBCatalogSourceTypeDef = TypedDict(
    "DynamoDBCatalogSourceTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
    },
)
FillMissingValuesOutputTypeDef = TypedDict(
    "FillMissingValuesOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "ImputedPath": str,
        "FilledPath": NotRequired[str],
    },
)
MergeOutputTypeDef = TypedDict(
    "MergeOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Source": str,
        "PrimaryKeys": List[List[str]],
    },
)
MicrosoftSQLServerCatalogSourceTypeDef = TypedDict(
    "MicrosoftSQLServerCatalogSourceTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
    },
)
MicrosoftSQLServerCatalogTargetOutputTypeDef = TypedDict(
    "MicrosoftSQLServerCatalogTargetOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Database": str,
        "Table": str,
    },
)
MySQLCatalogSourceTypeDef = TypedDict(
    "MySQLCatalogSourceTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
    },
)
MySQLCatalogTargetOutputTypeDef = TypedDict(
    "MySQLCatalogTargetOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Database": str,
        "Table": str,
    },
)
OracleSQLCatalogSourceTypeDef = TypedDict(
    "OracleSQLCatalogSourceTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
    },
)
OracleSQLCatalogTargetOutputTypeDef = TypedDict(
    "OracleSQLCatalogTargetOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Database": str,
        "Table": str,
    },
)
PIIDetectionOutputTypeDef = TypedDict(
    "PIIDetectionOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "PiiType": PiiTypeType,
        "EntityTypesToDetect": List[str],
        "OutputColumnName": NotRequired[str],
        "SampleFraction": NotRequired[float],
        "ThresholdFraction": NotRequired[float],
        "MaskValue": NotRequired[str],
    },
)
PostgreSQLCatalogSourceTypeDef = TypedDict(
    "PostgreSQLCatalogSourceTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
    },
)
PostgreSQLCatalogTargetOutputTypeDef = TypedDict(
    "PostgreSQLCatalogTargetOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Database": str,
        "Table": str,
    },
)
RedshiftSourceTypeDef = TypedDict(
    "RedshiftSourceTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
        "RedshiftTmpDir": NotRequired[str],
        "TmpDirIAMRole": NotRequired[str],
    },
)
RelationalCatalogSourceTypeDef = TypedDict(
    "RelationalCatalogSourceTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
    },
)
RenameFieldOutputTypeDef = TypedDict(
    "RenameFieldOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "SourcePath": List[str],
        "TargetPath": List[str],
    },
)
SelectFieldsOutputTypeDef = TypedDict(
    "SelectFieldsOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Paths": List[List[str]],
    },
)
SelectFromCollectionOutputTypeDef = TypedDict(
    "SelectFromCollectionOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Index": int,
    },
)
SpigotOutputTypeDef = TypedDict(
    "SpigotOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Path": str,
        "Topk": NotRequired[int],
        "Prob": NotRequired[float],
    },
)
SplitFieldsOutputTypeDef = TypedDict(
    "SplitFieldsOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Paths": List[List[str]],
    },
)
UnionOutputTypeDef = TypedDict(
    "UnionOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "UnionType": UnionTypeType,
    },
)
CodeGenEdgeTypeDef = TypedDict(
    "CodeGenEdgeTypeDef",
    {
        "Source": str,
        "Target": str,
        "TargetParameter": NotRequired[str],
    },
)
CodeGenNodeArgTypeDef = TypedDict(
    "CodeGenNodeArgTypeDef",
    {
        "Name": str,
        "Value": str,
        "Param": NotRequired[bool],
    },
)
ColumnImportanceTypeDef = TypedDict(
    "ColumnImportanceTypeDef",
    {
        "ColumnName": NotRequired[str],
        "Importance": NotRequired[float],
    },
)
ColumnOutputTypeDef = TypedDict(
    "ColumnOutputTypeDef",
    {
        "Name": str,
        "Type": NotRequired[str],
        "Comment": NotRequired[str],
        "Parameters": NotRequired[Dict[str, str]],
    },
)
ColumnRowFilterTypeDef = TypedDict(
    "ColumnRowFilterTypeDef",
    {
        "ColumnName": NotRequired[str],
        "RowFilterExpression": NotRequired[str],
    },
)
DateColumnStatisticsDataOutputTypeDef = TypedDict(
    "DateColumnStatisticsDataOutputTypeDef",
    {
        "NumberOfNulls": int,
        "NumberOfDistinctValues": int,
        "MinimumValue": NotRequired[datetime],
        "MaximumValue": NotRequired[datetime],
    },
)
DoubleColumnStatisticsDataTypeDef = TypedDict(
    "DoubleColumnStatisticsDataTypeDef",
    {
        "NumberOfNulls": int,
        "NumberOfDistinctValues": int,
        "MinimumValue": NotRequired[float],
        "MaximumValue": NotRequired[float],
    },
)
LongColumnStatisticsDataTypeDef = TypedDict(
    "LongColumnStatisticsDataTypeDef",
    {
        "NumberOfNulls": int,
        "NumberOfDistinctValues": int,
        "MinimumValue": NotRequired[int],
        "MaximumValue": NotRequired[int],
    },
)
StringColumnStatisticsDataTypeDef = TypedDict(
    "StringColumnStatisticsDataTypeDef",
    {
        "MaximumLength": int,
        "AverageLength": float,
        "NumberOfNulls": int,
        "NumberOfDistinctValues": int,
    },
)
ColumnStatisticsTaskRunTypeDef = TypedDict(
    "ColumnStatisticsTaskRunTypeDef",
    {
        "CustomerId": NotRequired[str],
        "ColumnStatisticsTaskRunId": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "TableName": NotRequired[str],
        "ColumnNameList": NotRequired[List[str]],
        "CatalogID": NotRequired[str],
        "Role": NotRequired[str],
        "SampleSize": NotRequired[float],
        "SecurityConfiguration": NotRequired[str],
        "NumberOfWorkers": NotRequired[int],
        "WorkerType": NotRequired[str],
        "Status": NotRequired[ColumnStatisticsStateType],
        "CreationTime": NotRequired[datetime],
        "LastUpdated": NotRequired[datetime],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "ErrorMessage": NotRequired[str],
        "DPUSeconds": NotRequired[float],
    },
)
TimestampTypeDef = Union[datetime, str]
ColumnTypeDef = TypedDict(
    "ColumnTypeDef",
    {
        "Name": str,
        "Type": NotRequired[str],
        "Comment": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, str]],
    },
)
IcebergCompactionMetricsTypeDef = TypedDict(
    "IcebergCompactionMetricsTypeDef",
    {
        "NumberOfBytesCompacted": NotRequired[int],
        "NumberOfFilesCompacted": NotRequired[int],
        "NumberOfDpus": NotRequired[int],
        "JobDurationInHour": NotRequired[float],
    },
)
ConditionExpressionTypeDef = TypedDict(
    "ConditionExpressionTypeDef",
    {
        "Condition": str,
        "TargetColumn": str,
        "Value": NotRequired[str],
    },
)
ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "LogicalOperator": NotRequired[Literal["EQUALS"]],
        "JobName": NotRequired[str],
        "State": NotRequired[JobRunStateType],
        "CrawlerName": NotRequired[str],
        "CrawlState": NotRequired[CrawlStateType],
    },
)
ConfigurationObjectOutputTypeDef = TypedDict(
    "ConfigurationObjectOutputTypeDef",
    {
        "DefaultValue": NotRequired[str],
        "AllowedValues": NotRequired[List[str]],
        "MinValue": NotRequired[str],
        "MaxValue": NotRequired[str],
    },
)
ConfigurationObjectTypeDef = TypedDict(
    "ConfigurationObjectTypeDef",
    {
        "DefaultValue": NotRequired[str],
        "AllowedValues": NotRequired[Sequence[str]],
        "MinValue": NotRequired[str],
        "MaxValue": NotRequired[str],
    },
)
ConfusionMatrixTypeDef = TypedDict(
    "ConfusionMatrixTypeDef",
    {
        "NumTruePositives": NotRequired[int],
        "NumFalsePositives": NotRequired[int],
        "NumTrueNegatives": NotRequired[int],
        "NumFalseNegatives": NotRequired[int],
    },
)
ConnectionPasswordEncryptionTypeDef = TypedDict(
    "ConnectionPasswordEncryptionTypeDef",
    {
        "ReturnConnectionPasswordEncrypted": bool,
        "AwsKmsKeyId": NotRequired[str],
    },
)
PhysicalConnectionRequirementsOutputTypeDef = TypedDict(
    "PhysicalConnectionRequirementsOutputTypeDef",
    {
        "SubnetId": NotRequired[str],
        "SecurityGroupIdList": NotRequired[List[str]],
        "AvailabilityZone": NotRequired[str],
    },
)
ConnectionsListOutputTypeDef = TypedDict(
    "ConnectionsListOutputTypeDef",
    {
        "Connections": NotRequired[List[str]],
    },
)
ConnectionsListTypeDef = TypedDict(
    "ConnectionsListTypeDef",
    {
        "Connections": NotRequired[Sequence[str]],
    },
)
ConnectorDataTargetTypeDef = TypedDict(
    "ConnectorDataTargetTypeDef",
    {
        "Name": str,
        "ConnectionType": str,
        "Data": Mapping[str, str],
        "Inputs": NotRequired[Sequence[str]],
    },
)
CrawlTypeDef = TypedDict(
    "CrawlTypeDef",
    {
        "State": NotRequired[CrawlStateType],
        "StartedOn": NotRequired[datetime],
        "CompletedOn": NotRequired[datetime],
        "ErrorMessage": NotRequired[str],
        "LogGroup": NotRequired[str],
        "LogStream": NotRequired[str],
    },
)
CrawlerHistoryTypeDef = TypedDict(
    "CrawlerHistoryTypeDef",
    {
        "CrawlId": NotRequired[str],
        "State": NotRequired[CrawlerHistoryStateType],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "Summary": NotRequired[str],
        "ErrorMessage": NotRequired[str],
        "LogGroup": NotRequired[str],
        "LogStream": NotRequired[str],
        "MessagePrefix": NotRequired[str],
        "DPUHour": NotRequired[float],
    },
)
CrawlerMetricsTypeDef = TypedDict(
    "CrawlerMetricsTypeDef",
    {
        "CrawlerName": NotRequired[str],
        "TimeLeftSeconds": NotRequired[float],
        "StillEstimating": NotRequired[bool],
        "LastRuntimeSeconds": NotRequired[float],
        "MedianRuntimeSeconds": NotRequired[float],
        "TablesCreated": NotRequired[int],
        "TablesUpdated": NotRequired[int],
        "TablesDeleted": NotRequired[int],
    },
)
DeltaTargetOutputTypeDef = TypedDict(
    "DeltaTargetOutputTypeDef",
    {
        "DeltaTables": NotRequired[List[str]],
        "ConnectionName": NotRequired[str],
        "WriteManifest": NotRequired[bool],
        "CreateNativeDeltaTable": NotRequired[bool],
    },
)
DynamoDBTargetTypeDef = TypedDict(
    "DynamoDBTargetTypeDef",
    {
        "Path": NotRequired[str],
        "scanAll": NotRequired[bool],
        "scanRate": NotRequired[float],
    },
)
HudiTargetOutputTypeDef = TypedDict(
    "HudiTargetOutputTypeDef",
    {
        "Paths": NotRequired[List[str]],
        "ConnectionName": NotRequired[str],
        "Exclusions": NotRequired[List[str]],
        "MaximumTraversalDepth": NotRequired[int],
    },
)
IcebergTargetOutputTypeDef = TypedDict(
    "IcebergTargetOutputTypeDef",
    {
        "Paths": NotRequired[List[str]],
        "ConnectionName": NotRequired[str],
        "Exclusions": NotRequired[List[str]],
        "MaximumTraversalDepth": NotRequired[int],
    },
)
JdbcTargetOutputTypeDef = TypedDict(
    "JdbcTargetOutputTypeDef",
    {
        "ConnectionName": NotRequired[str],
        "Path": NotRequired[str],
        "Exclusions": NotRequired[List[str]],
        "EnableAdditionalMetadata": NotRequired[List[JdbcMetadataEntryType]],
    },
)
MongoDBTargetTypeDef = TypedDict(
    "MongoDBTargetTypeDef",
    {
        "ConnectionName": NotRequired[str],
        "Path": NotRequired[str],
        "ScanAll": NotRequired[bool],
    },
)
S3TargetOutputTypeDef = TypedDict(
    "S3TargetOutputTypeDef",
    {
        "Path": NotRequired[str],
        "Exclusions": NotRequired[List[str]],
        "ConnectionName": NotRequired[str],
        "SampleSize": NotRequired[int],
        "EventQueueArn": NotRequired[str],
        "DlqEventQueueArn": NotRequired[str],
    },
)
LakeFormationConfigurationTypeDef = TypedDict(
    "LakeFormationConfigurationTypeDef",
    {
        "UseLakeFormationCredentials": NotRequired[bool],
        "AccountId": NotRequired[str],
    },
)
LastCrawlInfoTypeDef = TypedDict(
    "LastCrawlInfoTypeDef",
    {
        "Status": NotRequired[LastCrawlStatusType],
        "ErrorMessage": NotRequired[str],
        "LogGroup": NotRequired[str],
        "LogStream": NotRequired[str],
        "MessagePrefix": NotRequired[str],
        "StartTime": NotRequired[datetime],
    },
)
LineageConfigurationTypeDef = TypedDict(
    "LineageConfigurationTypeDef",
    {
        "CrawlerLineageSettings": NotRequired[CrawlerLineageSettingsType],
    },
)
RecrawlPolicyTypeDef = TypedDict(
    "RecrawlPolicyTypeDef",
    {
        "RecrawlBehavior": NotRequired[RecrawlBehaviorType],
    },
)
ScheduleTypeDef = TypedDict(
    "ScheduleTypeDef",
    {
        "ScheduleExpression": NotRequired[str],
        "State": NotRequired[ScheduleStateType],
    },
)
SchemaChangePolicyTypeDef = TypedDict(
    "SchemaChangePolicyTypeDef",
    {
        "UpdateBehavior": NotRequired[UpdateBehaviorType],
        "DeleteBehavior": NotRequired[DeleteBehaviorType],
    },
)
CrawlsFilterTypeDef = TypedDict(
    "CrawlsFilterTypeDef",
    {
        "FieldName": NotRequired[FieldNameType],
        "FilterOperator": NotRequired[FilterOperatorType],
        "FieldValue": NotRequired[str],
    },
)
CreateBlueprintRequestRequestTypeDef = TypedDict(
    "CreateBlueprintRequestRequestTypeDef",
    {
        "Name": str,
        "BlueprintLocation": str,
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CreateCsvClassifierRequestTypeDef = TypedDict(
    "CreateCsvClassifierRequestTypeDef",
    {
        "Name": str,
        "Delimiter": NotRequired[str],
        "QuoteSymbol": NotRequired[str],
        "ContainsHeader": NotRequired[CsvHeaderOptionType],
        "Header": NotRequired[Sequence[str]],
        "DisableValueTrimming": NotRequired[bool],
        "AllowSingleColumn": NotRequired[bool],
        "CustomDatatypeConfigured": NotRequired[bool],
        "CustomDatatypes": NotRequired[Sequence[str]],
        "Serde": NotRequired[CsvSerdeOptionType],
    },
)
CreateGrokClassifierRequestTypeDef = TypedDict(
    "CreateGrokClassifierRequestTypeDef",
    {
        "Classification": str,
        "Name": str,
        "GrokPattern": str,
        "CustomPatterns": NotRequired[str],
    },
)
CreateJsonClassifierRequestTypeDef = TypedDict(
    "CreateJsonClassifierRequestTypeDef",
    {
        "Name": str,
        "JsonPath": str,
    },
)
CreateXMLClassifierRequestTypeDef = TypedDict(
    "CreateXMLClassifierRequestTypeDef",
    {
        "Classification": str,
        "Name": str,
        "RowTag": NotRequired[str],
    },
)
CreateCustomEntityTypeRequestRequestTypeDef = TypedDict(
    "CreateCustomEntityTypeRequestRequestTypeDef",
    {
        "Name": str,
        "RegexString": str,
        "ContextWords": NotRequired[Sequence[str]],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
DataQualityTargetTableTypeDef = TypedDict(
    "DataQualityTargetTableTypeDef",
    {
        "TableName": str,
        "DatabaseName": str,
        "CatalogId": NotRequired[str],
    },
)
CreateDevEndpointRequestRequestTypeDef = TypedDict(
    "CreateDevEndpointRequestRequestTypeDef",
    {
        "EndpointName": str,
        "RoleArn": str,
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "SubnetId": NotRequired[str],
        "PublicKey": NotRequired[str],
        "PublicKeys": NotRequired[Sequence[str]],
        "NumberOfNodes": NotRequired[int],
        "WorkerType": NotRequired[WorkerTypeType],
        "GlueVersion": NotRequired[str],
        "NumberOfWorkers": NotRequired[int],
        "ExtraPythonLibsS3Path": NotRequired[str],
        "ExtraJarsS3Path": NotRequired[str],
        "SecurityConfiguration": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "Arguments": NotRequired[Mapping[str, str]],
    },
)
ExecutionPropertyTypeDef = TypedDict(
    "ExecutionPropertyTypeDef",
    {
        "MaxConcurrentRuns": NotRequired[int],
    },
)
JobCommandTypeDef = TypedDict(
    "JobCommandTypeDef",
    {
        "Name": NotRequired[str],
        "ScriptLocation": NotRequired[str],
        "PythonVersion": NotRequired[str],
        "Runtime": NotRequired[str],
    },
)
SourceControlDetailsTypeDef = TypedDict(
    "SourceControlDetailsTypeDef",
    {
        "Provider": NotRequired[SourceControlProviderType],
        "Repository": NotRequired[str],
        "Owner": NotRequired[str],
        "Branch": NotRequired[str],
        "Folder": NotRequired[str],
        "LastCommitId": NotRequired[str],
        "AuthStrategy": NotRequired[SourceControlAuthStrategyType],
        "AuthToken": NotRequired[str],
    },
)
PartitionIndexTypeDef = TypedDict(
    "PartitionIndexTypeDef",
    {
        "Keys": Sequence[str],
        "IndexName": str,
    },
)
CreateRegistryInputRequestTypeDef = TypedDict(
    "CreateRegistryInputRequestTypeDef",
    {
        "RegistryName": str,
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
RegistryIdTypeDef = TypedDict(
    "RegistryIdTypeDef",
    {
        "RegistryName": NotRequired[str],
        "RegistryArn": NotRequired[str],
    },
)
SessionCommandTypeDef = TypedDict(
    "SessionCommandTypeDef",
    {
        "Name": NotRequired[str],
        "PythonVersion": NotRequired[str],
    },
)
EventBatchingConditionTypeDef = TypedDict(
    "EventBatchingConditionTypeDef",
    {
        "BatchSize": int,
        "BatchWindow": NotRequired[int],
    },
)
CreateWorkflowRequestRequestTypeDef = TypedDict(
    "CreateWorkflowRequestRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "DefaultRunProperties": NotRequired[Mapping[str, str]],
        "Tags": NotRequired[Mapping[str, str]],
        "MaxConcurrentRuns": NotRequired[int],
    },
)
DQResultsPublishingOptionsTypeDef = TypedDict(
    "DQResultsPublishingOptionsTypeDef",
    {
        "EvaluationContext": NotRequired[str],
        "ResultsS3Prefix": NotRequired[str],
        "CloudWatchMetricsEnabled": NotRequired[bool],
        "ResultsPublishingEnabled": NotRequired[bool],
    },
)
DQStopJobOnFailureOptionsTypeDef = TypedDict(
    "DQStopJobOnFailureOptionsTypeDef",
    {
        "StopJobOnFailureTiming": NotRequired[DQStopJobOnFailureTimingType],
    },
)
EncryptionAtRestTypeDef = TypedDict(
    "EncryptionAtRestTypeDef",
    {
        "CatalogEncryptionMode": CatalogEncryptionModeType,
        "SseAwsKmsKeyId": NotRequired[str],
        "CatalogEncryptionServiceRole": NotRequired[str],
    },
)
DataLakePrincipalTypeDef = TypedDict(
    "DataLakePrincipalTypeDef",
    {
        "DataLakePrincipalIdentifier": NotRequired[str],
    },
)
DataQualityAnalyzerResultTypeDef = TypedDict(
    "DataQualityAnalyzerResultTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "EvaluationMessage": NotRequired[str],
        "EvaluatedMetrics": NotRequired[Dict[str, float]],
    },
)
DataQualityEvaluationRunAdditionalRunOptionsTypeDef = TypedDict(
    "DataQualityEvaluationRunAdditionalRunOptionsTypeDef",
    {
        "CloudWatchMetricsEnabled": NotRequired[bool],
        "ResultsS3Prefix": NotRequired[str],
        "CompositeRuleEvaluationMethod": NotRequired[DQCompositeRuleEvaluationMethodType],
    },
)
DataQualityMetricValuesTypeDef = TypedDict(
    "DataQualityMetricValuesTypeDef",
    {
        "ActualValue": NotRequired[float],
        "ExpectedValue": NotRequired[float],
        "LowerLimit": NotRequired[float],
        "UpperLimit": NotRequired[float],
    },
)
DataQualityRuleResultTypeDef = TypedDict(
    "DataQualityRuleResultTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "EvaluationMessage": NotRequired[str],
        "Result": NotRequired[DataQualityRuleResultStatusType],
        "EvaluatedMetrics": NotRequired[Dict[str, float]],
        "EvaluatedRule": NotRequired[str],
    },
)
GlueTableOutputTypeDef = TypedDict(
    "GlueTableOutputTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "CatalogId": NotRequired[str],
        "ConnectionName": NotRequired[str],
        "AdditionalOptions": NotRequired[Dict[str, str]],
    },
)
DatabaseIdentifierTypeDef = TypedDict(
    "DatabaseIdentifierTypeDef",
    {
        "CatalogId": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "Region": NotRequired[str],
    },
)
FederatedDatabaseTypeDef = TypedDict(
    "FederatedDatabaseTypeDef",
    {
        "Identifier": NotRequired[str],
        "ConnectionName": NotRequired[str],
    },
)
DatatypeTypeDef = TypedDict(
    "DatatypeTypeDef",
    {
        "Id": str,
        "Label": str,
    },
)
DecimalNumberOutputTypeDef = TypedDict(
    "DecimalNumberOutputTypeDef",
    {
        "UnscaledValue": bytes,
        "Scale": int,
    },
)
DeleteBlueprintRequestRequestTypeDef = TypedDict(
    "DeleteBlueprintRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteClassifierRequestRequestTypeDef = TypedDict(
    "DeleteClassifierRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteColumnStatisticsForPartitionRequestRequestTypeDef = TypedDict(
    "DeleteColumnStatisticsForPartitionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionValues": Sequence[str],
        "ColumnName": str,
        "CatalogId": NotRequired[str],
    },
)
DeleteColumnStatisticsForTableRequestRequestTypeDef = TypedDict(
    "DeleteColumnStatisticsForTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "ColumnName": str,
        "CatalogId": NotRequired[str],
    },
)
DeleteConnectionRequestRequestTypeDef = TypedDict(
    "DeleteConnectionRequestRequestTypeDef",
    {
        "ConnectionName": str,
        "CatalogId": NotRequired[str],
    },
)
DeleteCrawlerRequestRequestTypeDef = TypedDict(
    "DeleteCrawlerRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteCustomEntityTypeRequestRequestTypeDef = TypedDict(
    "DeleteCustomEntityTypeRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteDataQualityRulesetRequestRequestTypeDef = TypedDict(
    "DeleteDataQualityRulesetRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteDatabaseRequestRequestTypeDef = TypedDict(
    "DeleteDatabaseRequestRequestTypeDef",
    {
        "Name": str,
        "CatalogId": NotRequired[str],
    },
)
DeleteDevEndpointRequestRequestTypeDef = TypedDict(
    "DeleteDevEndpointRequestRequestTypeDef",
    {
        "EndpointName": str,
    },
)
DeleteJobRequestRequestTypeDef = TypedDict(
    "DeleteJobRequestRequestTypeDef",
    {
        "JobName": str,
    },
)
DeleteMLTransformRequestRequestTypeDef = TypedDict(
    "DeleteMLTransformRequestRequestTypeDef",
    {
        "TransformId": str,
    },
)
DeletePartitionIndexRequestRequestTypeDef = TypedDict(
    "DeletePartitionIndexRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "IndexName": str,
        "CatalogId": NotRequired[str],
    },
)
DeletePartitionRequestRequestTypeDef = TypedDict(
    "DeletePartitionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionValues": Sequence[str],
        "CatalogId": NotRequired[str],
    },
)
DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "PolicyHashCondition": NotRequired[str],
        "ResourceArn": NotRequired[str],
    },
)
SchemaIdTypeDef = TypedDict(
    "SchemaIdTypeDef",
    {
        "SchemaArn": NotRequired[str],
        "SchemaName": NotRequired[str],
        "RegistryName": NotRequired[str],
    },
)
DeleteSecurityConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteSecurityConfigurationRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteSessionRequestRequestTypeDef = TypedDict(
    "DeleteSessionRequestRequestTypeDef",
    {
        "Id": str,
        "RequestOrigin": NotRequired[str],
    },
)
DeleteTableOptimizerRequestRequestTypeDef = TypedDict(
    "DeleteTableOptimizerRequestRequestTypeDef",
    {
        "CatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "Type": TableOptimizerTypeType,
    },
)
DeleteTableRequestRequestTypeDef = TypedDict(
    "DeleteTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "CatalogId": NotRequired[str],
        "TransactionId": NotRequired[str],
    },
)
DeleteTableVersionRequestRequestTypeDef = TypedDict(
    "DeleteTableVersionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "VersionId": str,
        "CatalogId": NotRequired[str],
    },
)
DeleteTriggerRequestRequestTypeDef = TypedDict(
    "DeleteTriggerRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteUsageProfileRequestRequestTypeDef = TypedDict(
    "DeleteUsageProfileRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteUserDefinedFunctionRequestRequestTypeDef = TypedDict(
    "DeleteUserDefinedFunctionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "FunctionName": str,
        "CatalogId": NotRequired[str],
    },
)
DeleteWorkflowRequestRequestTypeDef = TypedDict(
    "DeleteWorkflowRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeltaTargetTypeDef = TypedDict(
    "DeltaTargetTypeDef",
    {
        "DeltaTables": NotRequired[Sequence[str]],
        "ConnectionName": NotRequired[str],
        "WriteManifest": NotRequired[bool],
        "CreateNativeDeltaTable": NotRequired[bool],
    },
)
DevEndpointCustomLibrariesTypeDef = TypedDict(
    "DevEndpointCustomLibrariesTypeDef",
    {
        "ExtraPythonLibsS3Path": NotRequired[str],
        "ExtraJarsS3Path": NotRequired[str],
    },
)
DirectSchemaChangePolicyTypeDef = TypedDict(
    "DirectSchemaChangePolicyTypeDef",
    {
        "EnableUpdateCatalog": NotRequired[bool],
        "UpdateBehavior": NotRequired[UpdateCatalogBehaviorType],
        "Table": NotRequired[str],
        "Database": NotRequired[str],
    },
)
DropDuplicatesTypeDef = TypedDict(
    "DropDuplicatesTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "Columns": NotRequired[Sequence[Sequence[str]]],
    },
)
DropFieldsTypeDef = TypedDict(
    "DropFieldsTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "Paths": Sequence[Sequence[str]],
    },
)
NullCheckBoxListTypeDef = TypedDict(
    "NullCheckBoxListTypeDef",
    {
        "IsEmpty": NotRequired[bool],
        "IsNullString": NotRequired[bool],
        "IsNegOne": NotRequired[bool],
    },
)
TransformConfigParameterOutputTypeDef = TypedDict(
    "TransformConfigParameterOutputTypeDef",
    {
        "Name": str,
        "Type": ParamTypeType,
        "ValidationRule": NotRequired[str],
        "ValidationMessage": NotRequired[str],
        "Value": NotRequired[List[str]],
        "ListType": NotRequired[ParamTypeType],
        "IsOptional": NotRequired[bool],
    },
)
EdgeTypeDef = TypedDict(
    "EdgeTypeDef",
    {
        "SourceId": NotRequired[str],
        "DestinationId": NotRequired[str],
    },
)
JobBookmarksEncryptionTypeDef = TypedDict(
    "JobBookmarksEncryptionTypeDef",
    {
        "JobBookmarksEncryptionMode": NotRequired[JobBookmarksEncryptionModeType],
        "KmsKeyArn": NotRequired[str],
    },
)
S3EncryptionTypeDef = TypedDict(
    "S3EncryptionTypeDef",
    {
        "S3EncryptionMode": NotRequired[S3EncryptionModeType],
        "KmsKeyArn": NotRequired[str],
    },
)
ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef",
    {
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)
ExportLabelsTaskRunPropertiesTypeDef = TypedDict(
    "ExportLabelsTaskRunPropertiesTypeDef",
    {
        "OutputS3Path": NotRequired[str],
    },
)
FederatedTableTypeDef = TypedDict(
    "FederatedTableTypeDef",
    {
        "Identifier": NotRequired[str],
        "DatabaseIdentifier": NotRequired[str],
        "ConnectionName": NotRequired[str],
    },
)
FillMissingValuesTypeDef = TypedDict(
    "FillMissingValuesTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "ImputedPath": str,
        "FilledPath": NotRequired[str],
    },
)
FilterValueOutputTypeDef = TypedDict(
    "FilterValueOutputTypeDef",
    {
        "Type": FilterValueTypeType,
        "Value": List[str],
    },
)
FilterValueTypeDef = TypedDict(
    "FilterValueTypeDef",
    {
        "Type": FilterValueTypeType,
        "Value": Sequence[str],
    },
)
FindMatchesParametersTypeDef = TypedDict(
    "FindMatchesParametersTypeDef",
    {
        "PrimaryKeyColumnName": NotRequired[str],
        "PrecisionRecallTradeoff": NotRequired[float],
        "AccuracyCostTradeoff": NotRequired[float],
        "EnforceProvidedLabels": NotRequired[bool],
    },
)
FindMatchesTaskRunPropertiesTypeDef = TypedDict(
    "FindMatchesTaskRunPropertiesTypeDef",
    {
        "JobId": NotRequired[str],
        "JobName": NotRequired[str],
        "JobRunId": NotRequired[str],
    },
)
GetBlueprintRequestRequestTypeDef = TypedDict(
    "GetBlueprintRequestRequestTypeDef",
    {
        "Name": str,
        "IncludeBlueprint": NotRequired[bool],
        "IncludeParameterSpec": NotRequired[bool],
    },
)
GetBlueprintRunRequestRequestTypeDef = TypedDict(
    "GetBlueprintRunRequestRequestTypeDef",
    {
        "BlueprintName": str,
        "RunId": str,
    },
)
GetBlueprintRunsRequestRequestTypeDef = TypedDict(
    "GetBlueprintRunsRequestRequestTypeDef",
    {
        "BlueprintName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GetCatalogImportStatusRequestRequestTypeDef = TypedDict(
    "GetCatalogImportStatusRequestRequestTypeDef",
    {
        "CatalogId": NotRequired[str],
    },
)
GetClassifierRequestRequestTypeDef = TypedDict(
    "GetClassifierRequestRequestTypeDef",
    {
        "Name": str,
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
GetClassifiersRequestRequestTypeDef = TypedDict(
    "GetClassifiersRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetColumnStatisticsForPartitionRequestRequestTypeDef = TypedDict(
    "GetColumnStatisticsForPartitionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionValues": Sequence[str],
        "ColumnNames": Sequence[str],
        "CatalogId": NotRequired[str],
    },
)
GetColumnStatisticsForTableRequestRequestTypeDef = TypedDict(
    "GetColumnStatisticsForTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "ColumnNames": Sequence[str],
        "CatalogId": NotRequired[str],
    },
)
GetColumnStatisticsTaskRunRequestRequestTypeDef = TypedDict(
    "GetColumnStatisticsTaskRunRequestRequestTypeDef",
    {
        "ColumnStatisticsTaskRunId": str,
    },
)
GetColumnStatisticsTaskRunsRequestRequestTypeDef = TypedDict(
    "GetColumnStatisticsTaskRunsRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetConnectionRequestRequestTypeDef = TypedDict(
    "GetConnectionRequestRequestTypeDef",
    {
        "Name": str,
        "CatalogId": NotRequired[str],
        "HidePassword": NotRequired[bool],
    },
)
GetConnectionsFilterTypeDef = TypedDict(
    "GetConnectionsFilterTypeDef",
    {
        "MatchCriteria": NotRequired[Sequence[str]],
        "ConnectionType": NotRequired[ConnectionTypeType],
    },
)
GetCrawlerMetricsRequestRequestTypeDef = TypedDict(
    "GetCrawlerMetricsRequestRequestTypeDef",
    {
        "CrawlerNameList": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetCrawlerRequestRequestTypeDef = TypedDict(
    "GetCrawlerRequestRequestTypeDef",
    {
        "Name": str,
    },
)
GetCrawlersRequestRequestTypeDef = TypedDict(
    "GetCrawlersRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetCustomEntityTypeRequestRequestTypeDef = TypedDict(
    "GetCustomEntityTypeRequestRequestTypeDef",
    {
        "Name": str,
    },
)
GetDataCatalogEncryptionSettingsRequestRequestTypeDef = TypedDict(
    "GetDataCatalogEncryptionSettingsRequestRequestTypeDef",
    {
        "CatalogId": NotRequired[str],
    },
)
GetDataQualityModelRequestRequestTypeDef = TypedDict(
    "GetDataQualityModelRequestRequestTypeDef",
    {
        "ProfileId": str,
        "StatisticId": NotRequired[str],
    },
)
GetDataQualityModelResultRequestRequestTypeDef = TypedDict(
    "GetDataQualityModelResultRequestRequestTypeDef",
    {
        "StatisticId": str,
        "ProfileId": str,
    },
)
StatisticModelResultTypeDef = TypedDict(
    "StatisticModelResultTypeDef",
    {
        "LowerBound": NotRequired[float],
        "UpperBound": NotRequired[float],
        "PredictedValue": NotRequired[float],
        "ActualValue": NotRequired[float],
        "Date": NotRequired[datetime],
        "InclusionAnnotation": NotRequired[InclusionAnnotationValueType],
    },
)
GetDataQualityResultRequestRequestTypeDef = TypedDict(
    "GetDataQualityResultRequestRequestTypeDef",
    {
        "ResultId": str,
    },
)
GetDataQualityRuleRecommendationRunRequestRequestTypeDef = TypedDict(
    "GetDataQualityRuleRecommendationRunRequestRequestTypeDef",
    {
        "RunId": str,
    },
)
GetDataQualityRulesetEvaluationRunRequestRequestTypeDef = TypedDict(
    "GetDataQualityRulesetEvaluationRunRequestRequestTypeDef",
    {
        "RunId": str,
    },
)
GetDataQualityRulesetRequestRequestTypeDef = TypedDict(
    "GetDataQualityRulesetRequestRequestTypeDef",
    {
        "Name": str,
    },
)
GetDatabaseRequestRequestTypeDef = TypedDict(
    "GetDatabaseRequestRequestTypeDef",
    {
        "Name": str,
        "CatalogId": NotRequired[str],
    },
)
GetDatabasesRequestRequestTypeDef = TypedDict(
    "GetDatabasesRequestRequestTypeDef",
    {
        "CatalogId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ResourceShareType": NotRequired[ResourceShareTypeType],
        "AttributesToGet": NotRequired[Sequence[Literal["NAME"]]],
    },
)
GetDataflowGraphRequestRequestTypeDef = TypedDict(
    "GetDataflowGraphRequestRequestTypeDef",
    {
        "PythonScript": NotRequired[str],
    },
)
GetDevEndpointRequestRequestTypeDef = TypedDict(
    "GetDevEndpointRequestRequestTypeDef",
    {
        "EndpointName": str,
    },
)
GetDevEndpointsRequestRequestTypeDef = TypedDict(
    "GetDevEndpointsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetJobBookmarkRequestRequestTypeDef = TypedDict(
    "GetJobBookmarkRequestRequestTypeDef",
    {
        "JobName": str,
        "RunId": NotRequired[str],
    },
)
JobBookmarkEntryTypeDef = TypedDict(
    "JobBookmarkEntryTypeDef",
    {
        "JobName": NotRequired[str],
        "Version": NotRequired[int],
        "Run": NotRequired[int],
        "Attempt": NotRequired[int],
        "PreviousRunId": NotRequired[str],
        "RunId": NotRequired[str],
        "JobBookmark": NotRequired[str],
    },
)
GetJobRequestRequestTypeDef = TypedDict(
    "GetJobRequestRequestTypeDef",
    {
        "JobName": str,
    },
)
GetJobRunRequestRequestTypeDef = TypedDict(
    "GetJobRunRequestRequestTypeDef",
    {
        "JobName": str,
        "RunId": str,
        "PredecessorsIncluded": NotRequired[bool],
    },
)
GetJobRunsRequestRequestTypeDef = TypedDict(
    "GetJobRunsRequestRequestTypeDef",
    {
        "JobName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GetJobsRequestRequestTypeDef = TypedDict(
    "GetJobsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GetMLTaskRunRequestRequestTypeDef = TypedDict(
    "GetMLTaskRunRequestRequestTypeDef",
    {
        "TransformId": str,
        "TaskRunId": str,
    },
)
TaskRunSortCriteriaTypeDef = TypedDict(
    "TaskRunSortCriteriaTypeDef",
    {
        "Column": TaskRunSortColumnTypeType,
        "SortDirection": SortDirectionTypeType,
    },
)
GetMLTransformRequestRequestTypeDef = TypedDict(
    "GetMLTransformRequestRequestTypeDef",
    {
        "TransformId": str,
    },
)
SchemaColumnTypeDef = TypedDict(
    "SchemaColumnTypeDef",
    {
        "Name": NotRequired[str],
        "DataType": NotRequired[str],
    },
)
TransformSortCriteriaTypeDef = TypedDict(
    "TransformSortCriteriaTypeDef",
    {
        "Column": TransformSortColumnTypeType,
        "SortDirection": SortDirectionTypeType,
    },
)
MappingEntryTypeDef = TypedDict(
    "MappingEntryTypeDef",
    {
        "SourceTable": NotRequired[str],
        "SourcePath": NotRequired[str],
        "SourceType": NotRequired[str],
        "TargetTable": NotRequired[str],
        "TargetPath": NotRequired[str],
        "TargetType": NotRequired[str],
    },
)
GetPartitionIndexesRequestRequestTypeDef = TypedDict(
    "GetPartitionIndexesRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "CatalogId": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
GetPartitionRequestRequestTypeDef = TypedDict(
    "GetPartitionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionValues": Sequence[str],
        "CatalogId": NotRequired[str],
    },
)
SegmentTypeDef = TypedDict(
    "SegmentTypeDef",
    {
        "SegmentNumber": int,
        "TotalSegments": int,
    },
)
GetResourcePoliciesRequestRequestTypeDef = TypedDict(
    "GetResourcePoliciesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GluePolicyTypeDef = TypedDict(
    "GluePolicyTypeDef",
    {
        "PolicyInJson": NotRequired[str],
        "PolicyHash": NotRequired[str],
        "CreateTime": NotRequired[datetime],
        "UpdateTime": NotRequired[datetime],
    },
)
GetResourcePolicyRequestRequestTypeDef = TypedDict(
    "GetResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": NotRequired[str],
    },
)
SchemaVersionNumberTypeDef = TypedDict(
    "SchemaVersionNumberTypeDef",
    {
        "LatestVersion": NotRequired[bool],
        "VersionNumber": NotRequired[int],
    },
)
GetSecurityConfigurationRequestRequestTypeDef = TypedDict(
    "GetSecurityConfigurationRequestRequestTypeDef",
    {
        "Name": str,
    },
)
GetSecurityConfigurationsRequestRequestTypeDef = TypedDict(
    "GetSecurityConfigurationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetSessionRequestRequestTypeDef = TypedDict(
    "GetSessionRequestRequestTypeDef",
    {
        "Id": str,
        "RequestOrigin": NotRequired[str],
    },
)
GetStatementRequestRequestTypeDef = TypedDict(
    "GetStatementRequestRequestTypeDef",
    {
        "SessionId": str,
        "Id": int,
        "RequestOrigin": NotRequired[str],
    },
)
GetTableOptimizerRequestRequestTypeDef = TypedDict(
    "GetTableOptimizerRequestRequestTypeDef",
    {
        "CatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "Type": TableOptimizerTypeType,
    },
)
GetTableVersionRequestRequestTypeDef = TypedDict(
    "GetTableVersionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "CatalogId": NotRequired[str],
        "VersionId": NotRequired[str],
    },
)
GetTableVersionsRequestRequestTypeDef = TypedDict(
    "GetTableVersionsRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "CatalogId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GetTagsRequestRequestTypeDef = TypedDict(
    "GetTagsRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
GetTriggerRequestRequestTypeDef = TypedDict(
    "GetTriggerRequestRequestTypeDef",
    {
        "Name": str,
    },
)
GetTriggersRequestRequestTypeDef = TypedDict(
    "GetTriggersRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "DependentJobName": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
SupportedDialectTypeDef = TypedDict(
    "SupportedDialectTypeDef",
    {
        "Dialect": NotRequired[ViewDialectType],
        "DialectVersion": NotRequired[str],
    },
)
GetUsageProfileRequestRequestTypeDef = TypedDict(
    "GetUsageProfileRequestRequestTypeDef",
    {
        "Name": str,
    },
)
GetUserDefinedFunctionRequestRequestTypeDef = TypedDict(
    "GetUserDefinedFunctionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "FunctionName": str,
        "CatalogId": NotRequired[str],
    },
)
GetUserDefinedFunctionsRequestRequestTypeDef = TypedDict(
    "GetUserDefinedFunctionsRequestRequestTypeDef",
    {
        "Pattern": str,
        "CatalogId": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GetWorkflowRequestRequestTypeDef = TypedDict(
    "GetWorkflowRequestRequestTypeDef",
    {
        "Name": str,
        "IncludeGraph": NotRequired[bool],
    },
)
GetWorkflowRunPropertiesRequestRequestTypeDef = TypedDict(
    "GetWorkflowRunPropertiesRequestRequestTypeDef",
    {
        "Name": str,
        "RunId": str,
    },
)
GetWorkflowRunRequestRequestTypeDef = TypedDict(
    "GetWorkflowRunRequestRequestTypeDef",
    {
        "Name": str,
        "RunId": str,
        "IncludeGraph": NotRequired[bool],
    },
)
GetWorkflowRunsRequestRequestTypeDef = TypedDict(
    "GetWorkflowRunsRequestRequestTypeDef",
    {
        "Name": str,
        "IncludeGraph": NotRequired[bool],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GlueStudioSchemaColumnTypeDef = TypedDict(
    "GlueStudioSchemaColumnTypeDef",
    {
        "Name": str,
        "Type": NotRequired[str],
    },
)
GlueTableTypeDef = TypedDict(
    "GlueTableTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "CatalogId": NotRequired[str],
        "ConnectionName": NotRequired[str],
        "AdditionalOptions": NotRequired[Mapping[str, str]],
    },
)
S3SourceAdditionalOptionsTypeDef = TypedDict(
    "S3SourceAdditionalOptionsTypeDef",
    {
        "BoundedSize": NotRequired[int],
        "BoundedFiles": NotRequired[int],
    },
)
HudiTargetTypeDef = TypedDict(
    "HudiTargetTypeDef",
    {
        "Paths": NotRequired[Sequence[str]],
        "ConnectionName": NotRequired[str],
        "Exclusions": NotRequired[Sequence[str]],
        "MaximumTraversalDepth": NotRequired[int],
    },
)
IcebergInputTypeDef = TypedDict(
    "IcebergInputTypeDef",
    {
        "MetadataOperation": Literal["CREATE"],
        "Version": NotRequired[str],
    },
)
IcebergOrphanFileDeletionConfigurationTypeDef = TypedDict(
    "IcebergOrphanFileDeletionConfigurationTypeDef",
    {
        "orphanFileRetentionPeriodInDays": NotRequired[int],
        "location": NotRequired[str],
    },
)
IcebergOrphanFileDeletionMetricsTypeDef = TypedDict(
    "IcebergOrphanFileDeletionMetricsTypeDef",
    {
        "NumberOfOrphanFilesDeleted": NotRequired[int],
        "NumberOfDpus": NotRequired[int],
        "JobDurationInHour": NotRequired[float],
    },
)
IcebergRetentionConfigurationTypeDef = TypedDict(
    "IcebergRetentionConfigurationTypeDef",
    {
        "snapshotRetentionPeriodInDays": NotRequired[int],
        "numberOfSnapshotsToRetain": NotRequired[int],
        "cleanExpiredFiles": NotRequired[bool],
    },
)
IcebergRetentionMetricsTypeDef = TypedDict(
    "IcebergRetentionMetricsTypeDef",
    {
        "NumberOfDataFilesDeleted": NotRequired[int],
        "NumberOfManifestFilesDeleted": NotRequired[int],
        "NumberOfManifestListsDeleted": NotRequired[int],
        "NumberOfDpus": NotRequired[int],
        "JobDurationInHour": NotRequired[float],
    },
)
IcebergTargetTypeDef = TypedDict(
    "IcebergTargetTypeDef",
    {
        "Paths": NotRequired[Sequence[str]],
        "ConnectionName": NotRequired[str],
        "Exclusions": NotRequired[Sequence[str]],
        "MaximumTraversalDepth": NotRequired[int],
    },
)
ImportCatalogToGlueRequestRequestTypeDef = TypedDict(
    "ImportCatalogToGlueRequestRequestTypeDef",
    {
        "CatalogId": NotRequired[str],
    },
)
ImportLabelsTaskRunPropertiesTypeDef = TypedDict(
    "ImportLabelsTaskRunPropertiesTypeDef",
    {
        "InputS3Path": NotRequired[str],
        "Replace": NotRequired[bool],
    },
)
JDBCConnectorOptionsOutputTypeDef = TypedDict(
    "JDBCConnectorOptionsOutputTypeDef",
    {
        "FilterPredicate": NotRequired[str],
        "PartitionColumn": NotRequired[str],
        "LowerBound": NotRequired[int],
        "UpperBound": NotRequired[int],
        "NumPartitions": NotRequired[int],
        "JobBookmarkKeys": NotRequired[List[str]],
        "JobBookmarkKeysSortOrder": NotRequired[str],
        "DataTypeMapping": NotRequired[Dict[JDBCDataTypeType, GlueRecordTypeType]],
    },
)
JDBCConnectorOptionsTypeDef = TypedDict(
    "JDBCConnectorOptionsTypeDef",
    {
        "FilterPredicate": NotRequired[str],
        "PartitionColumn": NotRequired[str],
        "LowerBound": NotRequired[int],
        "UpperBound": NotRequired[int],
        "NumPartitions": NotRequired[int],
        "JobBookmarkKeys": NotRequired[Sequence[str]],
        "JobBookmarkKeysSortOrder": NotRequired[str],
        "DataTypeMapping": NotRequired[Mapping[JDBCDataTypeType, GlueRecordTypeType]],
    },
)
JdbcTargetTypeDef = TypedDict(
    "JdbcTargetTypeDef",
    {
        "ConnectionName": NotRequired[str],
        "Path": NotRequired[str],
        "Exclusions": NotRequired[Sequence[str]],
        "EnableAdditionalMetadata": NotRequired[Sequence[JdbcMetadataEntryType]],
    },
)
PredecessorTypeDef = TypedDict(
    "PredecessorTypeDef",
    {
        "JobName": NotRequired[str],
        "RunId": NotRequired[str],
    },
)
JoinColumnOutputTypeDef = TypedDict(
    "JoinColumnOutputTypeDef",
    {
        "From": str,
        "Keys": List[List[str]],
    },
)
JoinColumnTypeDef = TypedDict(
    "JoinColumnTypeDef",
    {
        "From": str,
        "Keys": Sequence[Sequence[str]],
    },
)
KeySchemaElementTypeDef = TypedDict(
    "KeySchemaElementTypeDef",
    {
        "Name": str,
        "Type": str,
    },
)
LabelingSetGenerationTaskRunPropertiesTypeDef = TypedDict(
    "LabelingSetGenerationTaskRunPropertiesTypeDef",
    {
        "OutputS3Path": NotRequired[str],
    },
)
ListBlueprintsRequestRequestTypeDef = TypedDict(
    "ListBlueprintsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
ListColumnStatisticsTaskRunsRequestRequestTypeDef = TypedDict(
    "ListColumnStatisticsTaskRunsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListCrawlersRequestRequestTypeDef = TypedDict(
    "ListCrawlersRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
ListCustomEntityTypesRequestRequestTypeDef = TypedDict(
    "ListCustomEntityTypesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
ListDevEndpointsRequestRequestTypeDef = TypedDict(
    "ListDevEndpointsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
ListJobsRequestRequestTypeDef = TypedDict(
    "ListJobsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
ListRegistriesInputRequestTypeDef = TypedDict(
    "ListRegistriesInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
RegistryListItemTypeDef = TypedDict(
    "RegistryListItemTypeDef",
    {
        "RegistryName": NotRequired[str],
        "RegistryArn": NotRequired[str],
        "Description": NotRequired[str],
        "Status": NotRequired[RegistryStatusType],
        "CreatedTime": NotRequired[str],
        "UpdatedTime": NotRequired[str],
    },
)
SchemaVersionListItemTypeDef = TypedDict(
    "SchemaVersionListItemTypeDef",
    {
        "SchemaArn": NotRequired[str],
        "SchemaVersionId": NotRequired[str],
        "VersionNumber": NotRequired[int],
        "Status": NotRequired[SchemaVersionStatusType],
        "CreatedTime": NotRequired[str],
    },
)
SchemaListItemTypeDef = TypedDict(
    "SchemaListItemTypeDef",
    {
        "RegistryName": NotRequired[str],
        "SchemaName": NotRequired[str],
        "SchemaArn": NotRequired[str],
        "Description": NotRequired[str],
        "SchemaStatus": NotRequired[SchemaStatusType],
        "CreatedTime": NotRequired[str],
        "UpdatedTime": NotRequired[str],
    },
)
ListSessionsRequestRequestTypeDef = TypedDict(
    "ListSessionsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Tags": NotRequired[Mapping[str, str]],
        "RequestOrigin": NotRequired[str],
    },
)
ListStatementsRequestRequestTypeDef = TypedDict(
    "ListStatementsRequestRequestTypeDef",
    {
        "SessionId": str,
        "RequestOrigin": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
ListTableOptimizerRunsRequestRequestTypeDef = TypedDict(
    "ListTableOptimizerRunsRequestRequestTypeDef",
    {
        "CatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "Type": TableOptimizerTypeType,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTriggersRequestRequestTypeDef = TypedDict(
    "ListTriggersRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "DependentJobName": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
ListUsageProfilesRequestRequestTypeDef = TypedDict(
    "ListUsageProfilesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
UsageProfileDefinitionTypeDef = TypedDict(
    "UsageProfileDefinitionTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "CreatedOn": NotRequired[datetime],
        "LastModifiedOn": NotRequired[datetime],
    },
)
ListWorkflowsRequestRequestTypeDef = TypedDict(
    "ListWorkflowsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
MLUserDataEncryptionTypeDef = TypedDict(
    "MLUserDataEncryptionTypeDef",
    {
        "MlUserDataEncryptionMode": MLUserDataEncryptionModeStringType,
        "KmsKeyId": NotRequired[str],
    },
)
MappingTypeDef = TypedDict(
    "MappingTypeDef",
    {
        "ToKey": NotRequired[str],
        "FromPath": NotRequired[Sequence[str]],
        "FromType": NotRequired[str],
        "ToType": NotRequired[str],
        "Dropped": NotRequired[bool],
        "Children": NotRequired[Sequence[Mapping[str, Any]]],
    },
)
MergeTypeDef = TypedDict(
    "MergeTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "Source": str,
        "PrimaryKeys": Sequence[Sequence[str]],
    },
)
OtherMetadataValueListItemTypeDef = TypedDict(
    "OtherMetadataValueListItemTypeDef",
    {
        "MetadataValue": NotRequired[str],
        "CreatedTime": NotRequired[str],
    },
)
MetadataKeyValuePairTypeDef = TypedDict(
    "MetadataKeyValuePairTypeDef",
    {
        "MetadataKey": NotRequired[str],
        "MetadataValue": NotRequired[str],
    },
)
MicrosoftSQLServerCatalogTargetTypeDef = TypedDict(
    "MicrosoftSQLServerCatalogTargetTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "Database": str,
        "Table": str,
    },
)
MySQLCatalogTargetTypeDef = TypedDict(
    "MySQLCatalogTargetTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "Database": str,
        "Table": str,
    },
)
OAuth2ClientApplicationTypeDef = TypedDict(
    "OAuth2ClientApplicationTypeDef",
    {
        "UserManagedClientApplicationClientId": NotRequired[str],
        "AWSManagedClientApplicationReference": NotRequired[str],
    },
)
OracleSQLCatalogTargetTypeDef = TypedDict(
    "OracleSQLCatalogTargetTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "Database": str,
        "Table": str,
    },
)
OrderTypeDef = TypedDict(
    "OrderTypeDef",
    {
        "Column": str,
        "SortOrder": int,
    },
)
PIIDetectionTypeDef = TypedDict(
    "PIIDetectionTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "PiiType": PiiTypeType,
        "EntityTypesToDetect": Sequence[str],
        "OutputColumnName": NotRequired[str],
        "SampleFraction": NotRequired[float],
        "ThresholdFraction": NotRequired[float],
        "MaskValue": NotRequired[str],
    },
)
PhysicalConnectionRequirementsTypeDef = TypedDict(
    "PhysicalConnectionRequirementsTypeDef",
    {
        "SubnetId": NotRequired[str],
        "SecurityGroupIdList": NotRequired[Sequence[str]],
        "AvailabilityZone": NotRequired[str],
    },
)
PostgreSQLCatalogTargetTypeDef = TypedDict(
    "PostgreSQLCatalogTargetTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "Database": str,
        "Table": str,
    },
)
PropertyPredicateTypeDef = TypedDict(
    "PropertyPredicateTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
        "Comparator": NotRequired[ComparatorType],
    },
)
PutDataQualityProfileAnnotationRequestRequestTypeDef = TypedDict(
    "PutDataQualityProfileAnnotationRequestRequestTypeDef",
    {
        "ProfileId": str,
        "InclusionAnnotation": InclusionAnnotationValueType,
    },
)
PutResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestRequestTypeDef",
    {
        "PolicyInJson": str,
        "ResourceArn": NotRequired[str],
        "PolicyHashCondition": NotRequired[str],
        "PolicyExistsCondition": NotRequired[ExistConditionType],
        "EnableHybrid": NotRequired[EnableHybridValuesType],
    },
)
PutWorkflowRunPropertiesRequestRequestTypeDef = TypedDict(
    "PutWorkflowRunPropertiesRequestRequestTypeDef",
    {
        "Name": str,
        "RunId": str,
        "RunProperties": Mapping[str, str],
    },
)
RecipeActionOutputTypeDef = TypedDict(
    "RecipeActionOutputTypeDef",
    {
        "Operation": str,
        "Parameters": NotRequired[Dict[str, str]],
    },
)
RecipeActionTypeDef = TypedDict(
    "RecipeActionTypeDef",
    {
        "Operation": str,
        "Parameters": NotRequired[Mapping[str, str]],
    },
)
RecipeReferenceTypeDef = TypedDict(
    "RecipeReferenceTypeDef",
    {
        "RecipeArn": str,
        "RecipeVersion": str,
    },
)
UpsertRedshiftTargetOptionsOutputTypeDef = TypedDict(
    "UpsertRedshiftTargetOptionsOutputTypeDef",
    {
        "TableLocation": NotRequired[str],
        "ConnectionName": NotRequired[str],
        "UpsertKeys": NotRequired[List[str]],
    },
)
RenameFieldTypeDef = TypedDict(
    "RenameFieldTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "SourcePath": Sequence[str],
        "TargetPath": Sequence[str],
    },
)
ResetJobBookmarkRequestRequestTypeDef = TypedDict(
    "ResetJobBookmarkRequestRequestTypeDef",
    {
        "JobName": str,
        "RunId": NotRequired[str],
    },
)
ResourceUriTypeDef = TypedDict(
    "ResourceUriTypeDef",
    {
        "ResourceType": NotRequired[ResourceTypeType],
        "Uri": NotRequired[str],
    },
)
ResumeWorkflowRunRequestRequestTypeDef = TypedDict(
    "ResumeWorkflowRunRequestRequestTypeDef",
    {
        "Name": str,
        "RunId": str,
        "NodeIds": Sequence[str],
    },
)
RunIdentifierTypeDef = TypedDict(
    "RunIdentifierTypeDef",
    {
        "RunId": NotRequired[str],
        "JobRunId": NotRequired[str],
    },
)
RunMetricsTypeDef = TypedDict(
    "RunMetricsTypeDef",
    {
        "NumberOfBytesCompacted": NotRequired[str],
        "NumberOfFilesCompacted": NotRequired[str],
        "NumberOfDpus": NotRequired[str],
        "JobDurationInHour": NotRequired[str],
    },
)
RunStatementRequestRequestTypeDef = TypedDict(
    "RunStatementRequestRequestTypeDef",
    {
        "SessionId": str,
        "Code": str,
        "RequestOrigin": NotRequired[str],
    },
)
S3DirectSourceAdditionalOptionsTypeDef = TypedDict(
    "S3DirectSourceAdditionalOptionsTypeDef",
    {
        "BoundedSize": NotRequired[int],
        "BoundedFiles": NotRequired[int],
        "EnableSamplePath": NotRequired[bool],
        "SamplePath": NotRequired[str],
    },
)
S3TargetTypeDef = TypedDict(
    "S3TargetTypeDef",
    {
        "Path": NotRequired[str],
        "Exclusions": NotRequired[Sequence[str]],
        "ConnectionName": NotRequired[str],
        "SampleSize": NotRequired[int],
        "EventQueueArn": NotRequired[str],
        "DlqEventQueueArn": NotRequired[str],
    },
)
SortCriterionTypeDef = TypedDict(
    "SortCriterionTypeDef",
    {
        "FieldName": NotRequired[str],
        "Sort": NotRequired[SortType],
    },
)
SelectFieldsTypeDef = TypedDict(
    "SelectFieldsTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "Paths": Sequence[Sequence[str]],
    },
)
SelectFromCollectionTypeDef = TypedDict(
    "SelectFromCollectionTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "Index": int,
    },
)
SerDeInfoOutputTypeDef = TypedDict(
    "SerDeInfoOutputTypeDef",
    {
        "Name": NotRequired[str],
        "SerializationLibrary": NotRequired[str],
        "Parameters": NotRequired[Dict[str, str]],
    },
)
SerDeInfoTypeDef = TypedDict(
    "SerDeInfoTypeDef",
    {
        "Name": NotRequired[str],
        "SerializationLibrary": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, str]],
    },
)
SkewedInfoOutputTypeDef = TypedDict(
    "SkewedInfoOutputTypeDef",
    {
        "SkewedColumnNames": NotRequired[List[str]],
        "SkewedColumnValues": NotRequired[List[str]],
        "SkewedColumnValueLocationMaps": NotRequired[Dict[str, str]],
    },
)
SkewedInfoTypeDef = TypedDict(
    "SkewedInfoTypeDef",
    {
        "SkewedColumnNames": NotRequired[Sequence[str]],
        "SkewedColumnValues": NotRequired[Sequence[str]],
        "SkewedColumnValueLocationMaps": NotRequired[Mapping[str, str]],
    },
)
SqlAliasTypeDef = TypedDict(
    "SqlAliasTypeDef",
    {
        "From": str,
        "Alias": str,
    },
)
SpigotTypeDef = TypedDict(
    "SpigotTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "Path": str,
        "Topk": NotRequired[int],
        "Prob": NotRequired[float],
    },
)
SplitFieldsTypeDef = TypedDict(
    "SplitFieldsTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "Paths": Sequence[Sequence[str]],
    },
)
StartBlueprintRunRequestRequestTypeDef = TypedDict(
    "StartBlueprintRunRequestRequestTypeDef",
    {
        "BlueprintName": str,
        "RoleArn": str,
        "Parameters": NotRequired[str],
    },
)
StartColumnStatisticsTaskRunRequestRequestTypeDef = TypedDict(
    "StartColumnStatisticsTaskRunRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "Role": str,
        "ColumnNameList": NotRequired[Sequence[str]],
        "SampleSize": NotRequired[float],
        "CatalogID": NotRequired[str],
        "SecurityConfiguration": NotRequired[str],
    },
)
StartCrawlerRequestRequestTypeDef = TypedDict(
    "StartCrawlerRequestRequestTypeDef",
    {
        "Name": str,
    },
)
StartCrawlerScheduleRequestRequestTypeDef = TypedDict(
    "StartCrawlerScheduleRequestRequestTypeDef",
    {
        "CrawlerName": str,
    },
)
StartExportLabelsTaskRunRequestRequestTypeDef = TypedDict(
    "StartExportLabelsTaskRunRequestRequestTypeDef",
    {
        "TransformId": str,
        "OutputS3Path": str,
    },
)
StartImportLabelsTaskRunRequestRequestTypeDef = TypedDict(
    "StartImportLabelsTaskRunRequestRequestTypeDef",
    {
        "TransformId": str,
        "InputS3Path": str,
        "ReplaceAllLabels": NotRequired[bool],
    },
)
StartMLEvaluationTaskRunRequestRequestTypeDef = TypedDict(
    "StartMLEvaluationTaskRunRequestRequestTypeDef",
    {
        "TransformId": str,
    },
)
StartMLLabelingSetGenerationTaskRunRequestRequestTypeDef = TypedDict(
    "StartMLLabelingSetGenerationTaskRunRequestRequestTypeDef",
    {
        "TransformId": str,
        "OutputS3Path": str,
    },
)
StartTriggerRequestRequestTypeDef = TypedDict(
    "StartTriggerRequestRequestTypeDef",
    {
        "Name": str,
    },
)
StartWorkflowRunRequestRequestTypeDef = TypedDict(
    "StartWorkflowRunRequestRequestTypeDef",
    {
        "Name": str,
        "RunProperties": NotRequired[Mapping[str, str]],
    },
)
StartingEventBatchConditionTypeDef = TypedDict(
    "StartingEventBatchConditionTypeDef",
    {
        "BatchSize": NotRequired[int],
        "BatchWindow": NotRequired[int],
    },
)
StatementOutputDataTypeDef = TypedDict(
    "StatementOutputDataTypeDef",
    {
        "TextPlain": NotRequired[str],
    },
)
TimestampedInclusionAnnotationTypeDef = TypedDict(
    "TimestampedInclusionAnnotationTypeDef",
    {
        "Value": NotRequired[InclusionAnnotationValueType],
        "LastModifiedOn": NotRequired[datetime],
    },
)
StopColumnStatisticsTaskRunRequestRequestTypeDef = TypedDict(
    "StopColumnStatisticsTaskRunRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)
StopCrawlerRequestRequestTypeDef = TypedDict(
    "StopCrawlerRequestRequestTypeDef",
    {
        "Name": str,
    },
)
StopCrawlerScheduleRequestRequestTypeDef = TypedDict(
    "StopCrawlerScheduleRequestRequestTypeDef",
    {
        "CrawlerName": str,
    },
)
StopSessionRequestRequestTypeDef = TypedDict(
    "StopSessionRequestRequestTypeDef",
    {
        "Id": str,
        "RequestOrigin": NotRequired[str],
    },
)
StopTriggerRequestRequestTypeDef = TypedDict(
    "StopTriggerRequestRequestTypeDef",
    {
        "Name": str,
    },
)
StopWorkflowRunRequestRequestTypeDef = TypedDict(
    "StopWorkflowRunRequestRequestTypeDef",
    {
        "Name": str,
        "RunId": str,
    },
)
TableIdentifierTypeDef = TypedDict(
    "TableIdentifierTypeDef",
    {
        "CatalogId": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "Name": NotRequired[str],
        "Region": NotRequired[str],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagsToAdd": Mapping[str, str],
    },
)
TransformConfigParameterTypeDef = TypedDict(
    "TransformConfigParameterTypeDef",
    {
        "Name": str,
        "Type": ParamTypeType,
        "ValidationRule": NotRequired[str],
        "ValidationMessage": NotRequired[str],
        "Value": NotRequired[Sequence[str]],
        "ListType": NotRequired[ParamTypeType],
        "IsOptional": NotRequired[bool],
    },
)
UnionTypeDef = TypedDict(
    "UnionTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "UnionType": UnionTypeType,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagsToRemove": Sequence[str],
    },
)
UpdateBlueprintRequestRequestTypeDef = TypedDict(
    "UpdateBlueprintRequestRequestTypeDef",
    {
        "Name": str,
        "BlueprintLocation": str,
        "Description": NotRequired[str],
    },
)
UpdateCsvClassifierRequestTypeDef = TypedDict(
    "UpdateCsvClassifierRequestTypeDef",
    {
        "Name": str,
        "Delimiter": NotRequired[str],
        "QuoteSymbol": NotRequired[str],
        "ContainsHeader": NotRequired[CsvHeaderOptionType],
        "Header": NotRequired[Sequence[str]],
        "DisableValueTrimming": NotRequired[bool],
        "AllowSingleColumn": NotRequired[bool],
        "CustomDatatypeConfigured": NotRequired[bool],
        "CustomDatatypes": NotRequired[Sequence[str]],
        "Serde": NotRequired[CsvSerdeOptionType],
    },
)
UpdateGrokClassifierRequestTypeDef = TypedDict(
    "UpdateGrokClassifierRequestTypeDef",
    {
        "Name": str,
        "Classification": NotRequired[str],
        "GrokPattern": NotRequired[str],
        "CustomPatterns": NotRequired[str],
    },
)
UpdateJsonClassifierRequestTypeDef = TypedDict(
    "UpdateJsonClassifierRequestTypeDef",
    {
        "Name": str,
        "JsonPath": NotRequired[str],
    },
)
UpdateXMLClassifierRequestTypeDef = TypedDict(
    "UpdateXMLClassifierRequestTypeDef",
    {
        "Name": str,
        "Classification": NotRequired[str],
        "RowTag": NotRequired[str],
    },
)
UpdateCrawlerScheduleRequestRequestTypeDef = TypedDict(
    "UpdateCrawlerScheduleRequestRequestTypeDef",
    {
        "CrawlerName": str,
        "Schedule": NotRequired[str],
    },
)
UpdateDataQualityRulesetRequestRequestTypeDef = TypedDict(
    "UpdateDataQualityRulesetRequestRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "Ruleset": NotRequired[str],
    },
)
UpdateJobFromSourceControlRequestRequestTypeDef = TypedDict(
    "UpdateJobFromSourceControlRequestRequestTypeDef",
    {
        "JobName": NotRequired[str],
        "Provider": NotRequired[SourceControlProviderType],
        "RepositoryName": NotRequired[str],
        "RepositoryOwner": NotRequired[str],
        "BranchName": NotRequired[str],
        "Folder": NotRequired[str],
        "CommitId": NotRequired[str],
        "AuthStrategy": NotRequired[SourceControlAuthStrategyType],
        "AuthToken": NotRequired[str],
    },
)
UpdateSourceControlFromJobRequestRequestTypeDef = TypedDict(
    "UpdateSourceControlFromJobRequestRequestTypeDef",
    {
        "JobName": NotRequired[str],
        "Provider": NotRequired[SourceControlProviderType],
        "RepositoryName": NotRequired[str],
        "RepositoryOwner": NotRequired[str],
        "BranchName": NotRequired[str],
        "Folder": NotRequired[str],
        "CommitId": NotRequired[str],
        "AuthStrategy": NotRequired[SourceControlAuthStrategyType],
        "AuthToken": NotRequired[str],
    },
)
UpdateWorkflowRequestRequestTypeDef = TypedDict(
    "UpdateWorkflowRequestRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "DefaultRunProperties": NotRequired[Mapping[str, str]],
        "MaxConcurrentRuns": NotRequired[int],
    },
)
UpsertRedshiftTargetOptionsTypeDef = TypedDict(
    "UpsertRedshiftTargetOptionsTypeDef",
    {
        "TableLocation": NotRequired[str],
        "ConnectionName": NotRequired[str],
        "UpsertKeys": NotRequired[Sequence[str]],
    },
)
ViewRepresentationInputTypeDef = TypedDict(
    "ViewRepresentationInputTypeDef",
    {
        "Dialect": NotRequired[ViewDialectType],
        "DialectVersion": NotRequired[str],
        "ViewOriginalText": NotRequired[str],
        "ValidationConnection": NotRequired[str],
        "ViewExpandedText": NotRequired[str],
    },
)
ViewRepresentationTypeDef = TypedDict(
    "ViewRepresentationTypeDef",
    {
        "Dialect": NotRequired[ViewDialectType],
        "DialectVersion": NotRequired[str],
        "ViewOriginalText": NotRequired[str],
        "ViewExpandedText": NotRequired[str],
        "ValidationConnection": NotRequired[str],
        "IsStale": NotRequired[bool],
    },
)
WorkflowRunStatisticsTypeDef = TypedDict(
    "WorkflowRunStatisticsTypeDef",
    {
        "TotalActions": NotRequired[int],
        "TimeoutActions": NotRequired[int],
        "FailedActions": NotRequired[int],
        "StoppedActions": NotRequired[int],
        "SucceededActions": NotRequired[int],
        "RunningActions": NotRequired[int],
        "ErroredActions": NotRequired[int],
        "WaitingActions": NotRequired[int],
    },
)
ActionOutputTypeDef = TypedDict(
    "ActionOutputTypeDef",
    {
        "JobName": NotRequired[str],
        "Arguments": NotRequired[Dict[str, str]],
        "Timeout": NotRequired[int],
        "SecurityConfiguration": NotRequired[str],
        "NotificationProperty": NotRequired[NotificationPropertyTypeDef],
        "CrawlerName": NotRequired[str],
    },
)
ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "JobName": NotRequired[str],
        "Arguments": NotRequired[Mapping[str, str]],
        "Timeout": NotRequired[int],
        "SecurityConfiguration": NotRequired[str],
        "NotificationProperty": NotRequired[NotificationPropertyTypeDef],
        "CrawlerName": NotRequired[str],
    },
)
StartJobRunRequestRequestTypeDef = TypedDict(
    "StartJobRunRequestRequestTypeDef",
    {
        "JobName": str,
        "JobRunQueuingEnabled": NotRequired[bool],
        "JobRunId": NotRequired[str],
        "Arguments": NotRequired[Mapping[str, str]],
        "AllocatedCapacity": NotRequired[int],
        "Timeout": NotRequired[int],
        "MaxCapacity": NotRequired[float],
        "SecurityConfiguration": NotRequired[str],
        "NotificationProperty": NotRequired[NotificationPropertyTypeDef],
        "WorkerType": NotRequired[WorkerTypeType],
        "NumberOfWorkers": NotRequired[int],
        "ExecutionClass": NotRequired[ExecutionClassType],
    },
)
AggregateOutputTypeDef = TypedDict(
    "AggregateOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Groups": List[List[str]],
        "Aggs": List[AggregateOperationOutputTypeDef],
    },
)
AggregateOperationUnionTypeDef = Union[AggregateOperationTypeDef, AggregateOperationOutputTypeDef]
AmazonRedshiftNodeDataOutputTypeDef = TypedDict(
    "AmazonRedshiftNodeDataOutputTypeDef",
    {
        "AccessType": NotRequired[str],
        "SourceType": NotRequired[str],
        "Connection": NotRequired[OptionTypeDef],
        "Schema": NotRequired[OptionTypeDef],
        "Table": NotRequired[OptionTypeDef],
        "CatalogDatabase": NotRequired[OptionTypeDef],
        "CatalogTable": NotRequired[OptionTypeDef],
        "CatalogRedshiftSchema": NotRequired[str],
        "CatalogRedshiftTable": NotRequired[str],
        "TempDir": NotRequired[str],
        "IamRole": NotRequired[OptionTypeDef],
        "AdvancedOptions": NotRequired[List[AmazonRedshiftAdvancedOptionTypeDef]],
        "SampleQuery": NotRequired[str],
        "PreAction": NotRequired[str],
        "PostAction": NotRequired[str],
        "Action": NotRequired[str],
        "TablePrefix": NotRequired[str],
        "Upsert": NotRequired[bool],
        "MergeAction": NotRequired[str],
        "MergeWhenMatched": NotRequired[str],
        "MergeWhenNotMatched": NotRequired[str],
        "MergeClause": NotRequired[str],
        "CrawlerConnection": NotRequired[str],
        "TableSchema": NotRequired[List[OptionTypeDef]],
        "StagingTable": NotRequired[str],
        "SelectedColumns": NotRequired[List[OptionTypeDef]],
    },
)
AmazonRedshiftNodeDataTypeDef = TypedDict(
    "AmazonRedshiftNodeDataTypeDef",
    {
        "AccessType": NotRequired[str],
        "SourceType": NotRequired[str],
        "Connection": NotRequired[OptionTypeDef],
        "Schema": NotRequired[OptionTypeDef],
        "Table": NotRequired[OptionTypeDef],
        "CatalogDatabase": NotRequired[OptionTypeDef],
        "CatalogTable": NotRequired[OptionTypeDef],
        "CatalogRedshiftSchema": NotRequired[str],
        "CatalogRedshiftTable": NotRequired[str],
        "TempDir": NotRequired[str],
        "IamRole": NotRequired[OptionTypeDef],
        "AdvancedOptions": NotRequired[Sequence[AmazonRedshiftAdvancedOptionTypeDef]],
        "SampleQuery": NotRequired[str],
        "PreAction": NotRequired[str],
        "PostAction": NotRequired[str],
        "Action": NotRequired[str],
        "TablePrefix": NotRequired[str],
        "Upsert": NotRequired[bool],
        "MergeAction": NotRequired[str],
        "MergeWhenMatched": NotRequired[str],
        "MergeWhenNotMatched": NotRequired[str],
        "MergeClause": NotRequired[str],
        "CrawlerConnection": NotRequired[str],
        "TableSchema": NotRequired[Sequence[OptionTypeDef]],
        "StagingTable": NotRequired[str],
        "SelectedColumns": NotRequired[Sequence[OptionTypeDef]],
    },
)
SnowflakeNodeDataOutputTypeDef = TypedDict(
    "SnowflakeNodeDataOutputTypeDef",
    {
        "SourceType": NotRequired[str],
        "Connection": NotRequired[OptionTypeDef],
        "Schema": NotRequired[str],
        "Table": NotRequired[str],
        "Database": NotRequired[str],
        "TempDir": NotRequired[str],
        "IamRole": NotRequired[OptionTypeDef],
        "AdditionalOptions": NotRequired[Dict[str, str]],
        "SampleQuery": NotRequired[str],
        "PreAction": NotRequired[str],
        "PostAction": NotRequired[str],
        "Action": NotRequired[str],
        "Upsert": NotRequired[bool],
        "MergeAction": NotRequired[str],
        "MergeWhenMatched": NotRequired[str],
        "MergeWhenNotMatched": NotRequired[str],
        "MergeClause": NotRequired[str],
        "StagingTable": NotRequired[str],
        "SelectedColumns": NotRequired[List[OptionTypeDef]],
        "AutoPushdown": NotRequired[bool],
        "TableSchema": NotRequired[List[OptionTypeDef]],
    },
)
SnowflakeNodeDataTypeDef = TypedDict(
    "SnowflakeNodeDataTypeDef",
    {
        "SourceType": NotRequired[str],
        "Connection": NotRequired[OptionTypeDef],
        "Schema": NotRequired[str],
        "Table": NotRequired[str],
        "Database": NotRequired[str],
        "TempDir": NotRequired[str],
        "IamRole": NotRequired[OptionTypeDef],
        "AdditionalOptions": NotRequired[Mapping[str, str]],
        "SampleQuery": NotRequired[str],
        "PreAction": NotRequired[str],
        "PostAction": NotRequired[str],
        "Action": NotRequired[str],
        "Upsert": NotRequired[bool],
        "MergeAction": NotRequired[str],
        "MergeWhenMatched": NotRequired[str],
        "MergeWhenNotMatched": NotRequired[str],
        "MergeClause": NotRequired[str],
        "StagingTable": NotRequired[str],
        "SelectedColumns": NotRequired[Sequence[OptionTypeDef]],
        "AutoPushdown": NotRequired[bool],
        "TableSchema": NotRequired[Sequence[OptionTypeDef]],
    },
)
ApplyMappingOutputTypeDef = TypedDict(
    "ApplyMappingOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Mapping": List[MappingOutputTypeDef],
    },
)
ApplyMappingPaginatorTypeDef = TypedDict(
    "ApplyMappingPaginatorTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Mapping": List[MappingPaginatorTypeDef],
    },
)
BackfillErrorTypeDef = TypedDict(
    "BackfillErrorTypeDef",
    {
        "Code": NotRequired[BackfillErrorCodeType],
        "Partitions": NotRequired[List[PartitionValueListOutputTypeDef]],
    },
)
BasicCatalogTargetUnionTypeDef = Union[BasicCatalogTargetTypeDef, BasicCatalogTargetOutputTypeDef]
BatchPutDataQualityStatisticAnnotationResponseTypeDef = TypedDict(
    "BatchPutDataQualityStatisticAnnotationResponseTypeDef",
    {
        "FailedInclusionAnnotations": List[AnnotationErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CancelMLTaskRunResponseTypeDef = TypedDict(
    "CancelMLTaskRunResponseTypeDef",
    {
        "TransformId": str,
        "TaskRunId": str,
        "Status": TaskStatusTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CheckSchemaVersionValidityResponseTypeDef = TypedDict(
    "CheckSchemaVersionValidityResponseTypeDef",
    {
        "Valid": bool,
        "Error": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateBlueprintResponseTypeDef = TypedDict(
    "CreateBlueprintResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateConnectionResponseTypeDef = TypedDict(
    "CreateConnectionResponseTypeDef",
    {
        "CreateConnectionStatus": ConnectionStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCustomEntityTypeResponseTypeDef = TypedDict(
    "CreateCustomEntityTypeResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDataQualityRulesetResponseTypeDef = TypedDict(
    "CreateDataQualityRulesetResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDevEndpointResponseTypeDef = TypedDict(
    "CreateDevEndpointResponseTypeDef",
    {
        "EndpointName": str,
        "Status": str,
        "SecurityGroupIds": List[str],
        "SubnetId": str,
        "RoleArn": str,
        "YarnEndpointAddress": str,
        "ZeppelinRemoteSparkInterpreterPort": int,
        "NumberOfNodes": int,
        "WorkerType": WorkerTypeType,
        "GlueVersion": str,
        "NumberOfWorkers": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "ExtraPythonLibsS3Path": str,
        "ExtraJarsS3Path": str,
        "FailureReason": str,
        "SecurityConfiguration": str,
        "CreatedTimestamp": datetime,
        "Arguments": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateJobResponseTypeDef = TypedDict(
    "CreateJobResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMLTransformResponseTypeDef = TypedDict(
    "CreateMLTransformResponseTypeDef",
    {
        "TransformId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRegistryResponseTypeDef = TypedDict(
    "CreateRegistryResponseTypeDef",
    {
        "RegistryArn": str,
        "RegistryName": str,
        "Description": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSchemaResponseTypeDef = TypedDict(
    "CreateSchemaResponseTypeDef",
    {
        "RegistryName": str,
        "RegistryArn": str,
        "SchemaName": str,
        "SchemaArn": str,
        "Description": str,
        "DataFormat": DataFormatType,
        "Compatibility": CompatibilityType,
        "SchemaCheckpoint": int,
        "LatestSchemaVersion": int,
        "NextSchemaVersion": int,
        "SchemaStatus": SchemaStatusType,
        "Tags": Dict[str, str],
        "SchemaVersionId": str,
        "SchemaVersionStatus": SchemaVersionStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateScriptResponseTypeDef = TypedDict(
    "CreateScriptResponseTypeDef",
    {
        "PythonScript": str,
        "ScalaCode": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSecurityConfigurationResponseTypeDef = TypedDict(
    "CreateSecurityConfigurationResponseTypeDef",
    {
        "Name": str,
        "CreatedTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTriggerResponseTypeDef = TypedDict(
    "CreateTriggerResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateUsageProfileResponseTypeDef = TypedDict(
    "CreateUsageProfileResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWorkflowResponseTypeDef = TypedDict(
    "CreateWorkflowResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteBlueprintResponseTypeDef = TypedDict(
    "DeleteBlueprintResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteCustomEntityTypeResponseTypeDef = TypedDict(
    "DeleteCustomEntityTypeResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteJobResponseTypeDef = TypedDict(
    "DeleteJobResponseTypeDef",
    {
        "JobName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteMLTransformResponseTypeDef = TypedDict(
    "DeleteMLTransformResponseTypeDef",
    {
        "TransformId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteRegistryResponseTypeDef = TypedDict(
    "DeleteRegistryResponseTypeDef",
    {
        "RegistryName": str,
        "RegistryArn": str,
        "Status": RegistryStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteSchemaResponseTypeDef = TypedDict(
    "DeleteSchemaResponseTypeDef",
    {
        "SchemaArn": str,
        "SchemaName": str,
        "Status": SchemaStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteSessionResponseTypeDef = TypedDict(
    "DeleteSessionResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTriggerResponseTypeDef = TypedDict(
    "DeleteTriggerResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteWorkflowResponseTypeDef = TypedDict(
    "DeleteWorkflowResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCustomEntityTypeResponseTypeDef = TypedDict(
    "GetCustomEntityTypeResponseTypeDef",
    {
        "Name": str,
        "RegexString": str,
        "ContextWords": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDataQualityModelResponseTypeDef = TypedDict(
    "GetDataQualityModelResponseTypeDef",
    {
        "Status": DataQualityModelStatusType,
        "StartedOn": datetime,
        "CompletedOn": datetime,
        "FailureReason": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPlanResponseTypeDef = TypedDict(
    "GetPlanResponseTypeDef",
    {
        "PythonScript": str,
        "ScalaCode": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRegistryResponseTypeDef = TypedDict(
    "GetRegistryResponseTypeDef",
    {
        "RegistryName": str,
        "RegistryArn": str,
        "Description": str,
        "Status": RegistryStatusType,
        "CreatedTime": str,
        "UpdatedTime": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResourcePolicyResponseTypeDef = TypedDict(
    "GetResourcePolicyResponseTypeDef",
    {
        "PolicyInJson": str,
        "PolicyHash": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSchemaByDefinitionResponseTypeDef = TypedDict(
    "GetSchemaByDefinitionResponseTypeDef",
    {
        "SchemaVersionId": str,
        "SchemaArn": str,
        "DataFormat": DataFormatType,
        "Status": SchemaVersionStatusType,
        "CreatedTime": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSchemaResponseTypeDef = TypedDict(
    "GetSchemaResponseTypeDef",
    {
        "RegistryName": str,
        "RegistryArn": str,
        "SchemaName": str,
        "SchemaArn": str,
        "Description": str,
        "DataFormat": DataFormatType,
        "Compatibility": CompatibilityType,
        "SchemaCheckpoint": int,
        "LatestSchemaVersion": int,
        "NextSchemaVersion": int,
        "SchemaStatus": SchemaStatusType,
        "CreatedTime": str,
        "UpdatedTime": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSchemaVersionResponseTypeDef = TypedDict(
    "GetSchemaVersionResponseTypeDef",
    {
        "SchemaVersionId": str,
        "SchemaDefinition": str,
        "DataFormat": DataFormatType,
        "SchemaArn": str,
        "VersionNumber": int,
        "Status": SchemaVersionStatusType,
        "CreatedTime": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSchemaVersionsDiffResponseTypeDef = TypedDict(
    "GetSchemaVersionsDiffResponseTypeDef",
    {
        "Diff": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTagsResponseTypeDef = TypedDict(
    "GetTagsResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetWorkflowRunPropertiesResponseTypeDef = TypedDict(
    "GetWorkflowRunPropertiesResponseTypeDef",
    {
        "RunProperties": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListBlueprintsResponseTypeDef = TypedDict(
    "ListBlueprintsResponseTypeDef",
    {
        "Blueprints": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListColumnStatisticsTaskRunsResponseTypeDef = TypedDict(
    "ListColumnStatisticsTaskRunsResponseTypeDef",
    {
        "ColumnStatisticsTaskRunIds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListCrawlersResponseTypeDef = TypedDict(
    "ListCrawlersResponseTypeDef",
    {
        "CrawlerNames": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListDevEndpointsResponseTypeDef = TypedDict(
    "ListDevEndpointsResponseTypeDef",
    {
        "DevEndpointNames": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListJobsResponseTypeDef = TypedDict(
    "ListJobsResponseTypeDef",
    {
        "JobNames": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListMLTransformsResponseTypeDef = TypedDict(
    "ListMLTransformsResponseTypeDef",
    {
        "TransformIds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTriggersResponseTypeDef = TypedDict(
    "ListTriggersResponseTypeDef",
    {
        "TriggerNames": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListWorkflowsResponseTypeDef = TypedDict(
    "ListWorkflowsResponseTypeDef",
    {
        "Workflows": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PutResourcePolicyResponseTypeDef = TypedDict(
    "PutResourcePolicyResponseTypeDef",
    {
        "PolicyHash": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutSchemaVersionMetadataResponseTypeDef = TypedDict(
    "PutSchemaVersionMetadataResponseTypeDef",
    {
        "SchemaArn": str,
        "SchemaName": str,
        "RegistryName": str,
        "LatestVersion": bool,
        "VersionNumber": int,
        "SchemaVersionId": str,
        "MetadataKey": str,
        "MetadataValue": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterSchemaVersionResponseTypeDef = TypedDict(
    "RegisterSchemaVersionResponseTypeDef",
    {
        "SchemaVersionId": str,
        "VersionNumber": int,
        "Status": SchemaVersionStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RemoveSchemaVersionMetadataResponseTypeDef = TypedDict(
    "RemoveSchemaVersionMetadataResponseTypeDef",
    {
        "SchemaArn": str,
        "SchemaName": str,
        "RegistryName": str,
        "LatestVersion": bool,
        "VersionNumber": int,
        "SchemaVersionId": str,
        "MetadataKey": str,
        "MetadataValue": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResumeWorkflowRunResponseTypeDef = TypedDict(
    "ResumeWorkflowRunResponseTypeDef",
    {
        "RunId": str,
        "NodeIds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RunStatementResponseTypeDef = TypedDict(
    "RunStatementResponseTypeDef",
    {
        "Id": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartBlueprintRunResponseTypeDef = TypedDict(
    "StartBlueprintRunResponseTypeDef",
    {
        "RunId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartColumnStatisticsTaskRunResponseTypeDef = TypedDict(
    "StartColumnStatisticsTaskRunResponseTypeDef",
    {
        "ColumnStatisticsTaskRunId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartDataQualityRuleRecommendationRunResponseTypeDef = TypedDict(
    "StartDataQualityRuleRecommendationRunResponseTypeDef",
    {
        "RunId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartDataQualityRulesetEvaluationRunResponseTypeDef = TypedDict(
    "StartDataQualityRulesetEvaluationRunResponseTypeDef",
    {
        "RunId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartExportLabelsTaskRunResponseTypeDef = TypedDict(
    "StartExportLabelsTaskRunResponseTypeDef",
    {
        "TaskRunId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartImportLabelsTaskRunResponseTypeDef = TypedDict(
    "StartImportLabelsTaskRunResponseTypeDef",
    {
        "TaskRunId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartJobRunResponseTypeDef = TypedDict(
    "StartJobRunResponseTypeDef",
    {
        "JobRunId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartMLEvaluationTaskRunResponseTypeDef = TypedDict(
    "StartMLEvaluationTaskRunResponseTypeDef",
    {
        "TaskRunId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartMLLabelingSetGenerationTaskRunResponseTypeDef = TypedDict(
    "StartMLLabelingSetGenerationTaskRunResponseTypeDef",
    {
        "TaskRunId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartTriggerResponseTypeDef = TypedDict(
    "StartTriggerResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartWorkflowRunResponseTypeDef = TypedDict(
    "StartWorkflowRunResponseTypeDef",
    {
        "RunId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopSessionResponseTypeDef = TypedDict(
    "StopSessionResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopTriggerResponseTypeDef = TypedDict(
    "StopTriggerResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateBlueprintResponseTypeDef = TypedDict(
    "UpdateBlueprintResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDataQualityRulesetResponseTypeDef = TypedDict(
    "UpdateDataQualityRulesetResponseTypeDef",
    {
        "Name": str,
        "Description": str,
        "Ruleset": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateJobFromSourceControlResponseTypeDef = TypedDict(
    "UpdateJobFromSourceControlResponseTypeDef",
    {
        "JobName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateJobResponseTypeDef = TypedDict(
    "UpdateJobResponseTypeDef",
    {
        "JobName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateMLTransformResponseTypeDef = TypedDict(
    "UpdateMLTransformResponseTypeDef",
    {
        "TransformId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRegistryResponseTypeDef = TypedDict(
    "UpdateRegistryResponseTypeDef",
    {
        "RegistryName": str,
        "RegistryArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSchemaResponseTypeDef = TypedDict(
    "UpdateSchemaResponseTypeDef",
    {
        "SchemaArn": str,
        "SchemaName": str,
        "RegistryName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSourceControlFromJobResponseTypeDef = TypedDict(
    "UpdateSourceControlFromJobResponseTypeDef",
    {
        "JobName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateUsageProfileResponseTypeDef = TypedDict(
    "UpdateUsageProfileResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateWorkflowResponseTypeDef = TypedDict(
    "UpdateWorkflowResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDeleteConnectionResponseTypeDef = TypedDict(
    "BatchDeleteConnectionResponseTypeDef",
    {
        "Succeeded": List[str],
        "Errors": Dict[str, ErrorDetailTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetTableOptimizerErrorTypeDef = TypedDict(
    "BatchGetTableOptimizerErrorTypeDef",
    {
        "error": NotRequired[ErrorDetailTypeDef],
        "catalogId": NotRequired[str],
        "databaseName": NotRequired[str],
        "tableName": NotRequired[str],
        "type": NotRequired[TableOptimizerTypeType],
    },
)
BatchStopJobRunErrorTypeDef = TypedDict(
    "BatchStopJobRunErrorTypeDef",
    {
        "JobName": NotRequired[str],
        "JobRunId": NotRequired[str],
        "ErrorDetail": NotRequired[ErrorDetailTypeDef],
    },
)
BatchUpdatePartitionFailureEntryTypeDef = TypedDict(
    "BatchUpdatePartitionFailureEntryTypeDef",
    {
        "PartitionValueList": NotRequired[List[str]],
        "ErrorDetail": NotRequired[ErrorDetailTypeDef],
    },
)
ColumnErrorTypeDef = TypedDict(
    "ColumnErrorTypeDef",
    {
        "ColumnName": NotRequired[str],
        "Error": NotRequired[ErrorDetailTypeDef],
    },
)
PartitionErrorTypeDef = TypedDict(
    "PartitionErrorTypeDef",
    {
        "PartitionValues": NotRequired[List[str]],
        "ErrorDetail": NotRequired[ErrorDetailTypeDef],
    },
)
TableErrorTypeDef = TypedDict(
    "TableErrorTypeDef",
    {
        "TableName": NotRequired[str],
        "ErrorDetail": NotRequired[ErrorDetailTypeDef],
    },
)
TableVersionErrorTypeDef = TypedDict(
    "TableVersionErrorTypeDef",
    {
        "TableName": NotRequired[str],
        "VersionId": NotRequired[str],
        "ErrorDetail": NotRequired[ErrorDetailTypeDef],
    },
)
ViewValidationTypeDef = TypedDict(
    "ViewValidationTypeDef",
    {
        "Dialect": NotRequired[ViewDialectType],
        "DialectVersion": NotRequired[str],
        "ViewValidationText": NotRequired[str],
        "UpdateTime": NotRequired[datetime],
        "State": NotRequired[ResourceStateType],
        "Error": NotRequired[ErrorDetailTypeDef],
    },
)
BatchGetCustomEntityTypesResponseTypeDef = TypedDict(
    "BatchGetCustomEntityTypesResponseTypeDef",
    {
        "CustomEntityTypes": List[CustomEntityTypeTypeDef],
        "CustomEntityTypesNotFound": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCustomEntityTypesResponseTypeDef = TypedDict(
    "ListCustomEntityTypesResponseTypeDef",
    {
        "CustomEntityTypes": List[CustomEntityTypeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
BatchGetDevEndpointsResponseTypeDef = TypedDict(
    "BatchGetDevEndpointsResponseTypeDef",
    {
        "DevEndpoints": List[DevEndpointTypeDef],
        "DevEndpointsNotFound": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDevEndpointResponseTypeDef = TypedDict(
    "GetDevEndpointResponseTypeDef",
    {
        "DevEndpoint": DevEndpointTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDevEndpointsResponseTypeDef = TypedDict(
    "GetDevEndpointsResponseTypeDef",
    {
        "DevEndpoints": List[DevEndpointTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
BatchGetPartitionRequestRequestTypeDef = TypedDict(
    "BatchGetPartitionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionsToGet": Sequence[PartitionValueListTypeDef],
        "CatalogId": NotRequired[str],
    },
)
PartitionValueListUnionTypeDef = Union[PartitionValueListTypeDef, PartitionValueListOutputTypeDef]
BatchGetTableOptimizerRequestRequestTypeDef = TypedDict(
    "BatchGetTableOptimizerRequestRequestTypeDef",
    {
        "Entries": Sequence[BatchGetTableOptimizerEntryTypeDef],
    },
)
BatchPutDataQualityStatisticAnnotationRequestRequestTypeDef = TypedDict(
    "BatchPutDataQualityStatisticAnnotationRequestRequestTypeDef",
    {
        "InclusionAnnotations": Sequence[DatapointInclusionAnnotationTypeDef],
        "ClientToken": NotRequired[str],
    },
)
DecimalNumberTypeDef = TypedDict(
    "DecimalNumberTypeDef",
    {
        "UnscaledValue": BlobTypeDef,
        "Scale": int,
    },
)
GetBlueprintRunResponseTypeDef = TypedDict(
    "GetBlueprintRunResponseTypeDef",
    {
        "BlueprintRun": BlueprintRunTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBlueprintRunsResponseTypeDef = TypedDict(
    "GetBlueprintRunsResponseTypeDef",
    {
        "BlueprintRuns": List[BlueprintRunTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
BlueprintTypeDef = TypedDict(
    "BlueprintTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "CreatedOn": NotRequired[datetime],
        "LastModifiedOn": NotRequired[datetime],
        "ParameterSpec": NotRequired[str],
        "BlueprintLocation": NotRequired[str],
        "BlueprintServiceLocation": NotRequired[str],
        "Status": NotRequired[BlueprintStatusType],
        "ErrorMessage": NotRequired[str],
        "LastActiveDefinition": NotRequired[LastActiveDefinitionTypeDef],
    },
)
GetCatalogImportStatusResponseTypeDef = TypedDict(
    "GetCatalogImportStatusResponseTypeDef",
    {
        "ImportStatus": CatalogImportStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CatalogKafkaSourceOutputTypeDef = TypedDict(
    "CatalogKafkaSourceOutputTypeDef",
    {
        "Name": str,
        "Table": str,
        "Database": str,
        "WindowSize": NotRequired[int],
        "DetectSchema": NotRequired[bool],
        "StreamingOptions": NotRequired[KafkaStreamingSourceOptionsOutputTypeDef],
        "DataPreviewOptions": NotRequired[StreamingDataPreviewOptionsTypeDef],
    },
)
DirectKafkaSourceOutputTypeDef = TypedDict(
    "DirectKafkaSourceOutputTypeDef",
    {
        "Name": str,
        "StreamingOptions": NotRequired[KafkaStreamingSourceOptionsOutputTypeDef],
        "WindowSize": NotRequired[int],
        "DetectSchema": NotRequired[bool],
        "DataPreviewOptions": NotRequired[StreamingDataPreviewOptionsTypeDef],
    },
)
CatalogKinesisSourceOutputTypeDef = TypedDict(
    "CatalogKinesisSourceOutputTypeDef",
    {
        "Name": str,
        "Table": str,
        "Database": str,
        "WindowSize": NotRequired[int],
        "DetectSchema": NotRequired[bool],
        "StreamingOptions": NotRequired[KinesisStreamingSourceOptionsOutputTypeDef],
        "DataPreviewOptions": NotRequired[StreamingDataPreviewOptionsTypeDef],
    },
)
DirectKinesisSourceOutputTypeDef = TypedDict(
    "DirectKinesisSourceOutputTypeDef",
    {
        "Name": str,
        "WindowSize": NotRequired[int],
        "DetectSchema": NotRequired[bool],
        "StreamingOptions": NotRequired[KinesisStreamingSourceOptionsOutputTypeDef],
        "DataPreviewOptions": NotRequired[StreamingDataPreviewOptionsTypeDef],
    },
)
GovernedCatalogTargetOutputTypeDef = TypedDict(
    "GovernedCatalogTargetOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Table": str,
        "Database": str,
        "PartitionKeys": NotRequired[List[List[str]]],
        "SchemaChangePolicy": NotRequired[CatalogSchemaChangePolicyTypeDef],
    },
)
GovernedCatalogTargetTypeDef = TypedDict(
    "GovernedCatalogTargetTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "Table": str,
        "Database": str,
        "PartitionKeys": NotRequired[Sequence[Sequence[str]]],
        "SchemaChangePolicy": NotRequired[CatalogSchemaChangePolicyTypeDef],
    },
)
S3CatalogTargetOutputTypeDef = TypedDict(
    "S3CatalogTargetOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Table": str,
        "Database": str,
        "PartitionKeys": NotRequired[List[List[str]]],
        "SchemaChangePolicy": NotRequired[CatalogSchemaChangePolicyTypeDef],
    },
)
S3CatalogTargetTypeDef = TypedDict(
    "S3CatalogTargetTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "Table": str,
        "Database": str,
        "PartitionKeys": NotRequired[Sequence[Sequence[str]]],
        "SchemaChangePolicy": NotRequired[CatalogSchemaChangePolicyTypeDef],
    },
)
S3DeltaCatalogTargetOutputTypeDef = TypedDict(
    "S3DeltaCatalogTargetOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Table": str,
        "Database": str,
        "PartitionKeys": NotRequired[List[List[str]]],
        "AdditionalOptions": NotRequired[Dict[str, str]],
        "SchemaChangePolicy": NotRequired[CatalogSchemaChangePolicyTypeDef],
    },
)
S3DeltaCatalogTargetTypeDef = TypedDict(
    "S3DeltaCatalogTargetTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "Table": str,
        "Database": str,
        "PartitionKeys": NotRequired[Sequence[Sequence[str]]],
        "AdditionalOptions": NotRequired[Mapping[str, str]],
        "SchemaChangePolicy": NotRequired[CatalogSchemaChangePolicyTypeDef],
    },
)
S3HudiCatalogTargetOutputTypeDef = TypedDict(
    "S3HudiCatalogTargetOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Table": str,
        "Database": str,
        "AdditionalOptions": Dict[str, str],
        "PartitionKeys": NotRequired[List[List[str]]],
        "SchemaChangePolicy": NotRequired[CatalogSchemaChangePolicyTypeDef],
    },
)
S3HudiCatalogTargetTypeDef = TypedDict(
    "S3HudiCatalogTargetTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "Table": str,
        "Database": str,
        "AdditionalOptions": Mapping[str, str],
        "PartitionKeys": NotRequired[Sequence[Sequence[str]]],
        "SchemaChangePolicy": NotRequired[CatalogSchemaChangePolicyTypeDef],
    },
)
CatalogTargetUnionTypeDef = Union[CatalogTargetTypeDef, CatalogTargetOutputTypeDef]
ClassifierTypeDef = TypedDict(
    "ClassifierTypeDef",
    {
        "GrokClassifier": NotRequired[GrokClassifierTypeDef],
        "XMLClassifier": NotRequired[XMLClassifierTypeDef],
        "JsonClassifier": NotRequired[JsonClassifierTypeDef],
        "CsvClassifier": NotRequired[CsvClassifierTypeDef],
    },
)
CodeGenNodeOutputTypeDef = TypedDict(
    "CodeGenNodeOutputTypeDef",
    {
        "Id": str,
        "NodeType": str,
        "Args": List[CodeGenNodeArgTypeDef],
        "LineNumber": NotRequired[int],
    },
)
CodeGenNodeTypeDef = TypedDict(
    "CodeGenNodeTypeDef",
    {
        "Id": str,
        "NodeType": str,
        "Args": Sequence[CodeGenNodeArgTypeDef],
        "LineNumber": NotRequired[int],
    },
)
LocationTypeDef = TypedDict(
    "LocationTypeDef",
    {
        "Jdbc": NotRequired[Sequence[CodeGenNodeArgTypeDef]],
        "S3": NotRequired[Sequence[CodeGenNodeArgTypeDef]],
        "DynamoDB": NotRequired[Sequence[CodeGenNodeArgTypeDef]],
    },
)
GetColumnStatisticsTaskRunResponseTypeDef = TypedDict(
    "GetColumnStatisticsTaskRunResponseTypeDef",
    {
        "ColumnStatisticsTaskRun": ColumnStatisticsTaskRunTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetColumnStatisticsTaskRunsResponseTypeDef = TypedDict(
    "GetColumnStatisticsTaskRunsResponseTypeDef",
    {
        "ColumnStatisticsTaskRuns": List[ColumnStatisticsTaskRunTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DateColumnStatisticsDataTypeDef = TypedDict(
    "DateColumnStatisticsDataTypeDef",
    {
        "NumberOfNulls": int,
        "NumberOfDistinctValues": int,
        "MinimumValue": NotRequired[TimestampTypeDef],
        "MaximumValue": NotRequired[TimestampTypeDef],
    },
)
GetTableRequestRequestTypeDef = TypedDict(
    "GetTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "CatalogId": NotRequired[str],
        "TransactionId": NotRequired[str],
        "QueryAsOfTime": NotRequired[TimestampTypeDef],
        "IncludeStatusDetails": NotRequired[bool],
    },
)
GetTablesRequestRequestTypeDef = TypedDict(
    "GetTablesRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "CatalogId": NotRequired[str],
        "Expression": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "TransactionId": NotRequired[str],
        "QueryAsOfTime": NotRequired[TimestampTypeDef],
        "IncludeStatusDetails": NotRequired[bool],
        "AttributesToGet": NotRequired[Sequence[TableAttributesType]],
    },
)
KafkaStreamingSourceOptionsTypeDef = TypedDict(
    "KafkaStreamingSourceOptionsTypeDef",
    {
        "BootstrapServers": NotRequired[str],
        "SecurityProtocol": NotRequired[str],
        "ConnectionName": NotRequired[str],
        "TopicName": NotRequired[str],
        "Assign": NotRequired[str],
        "SubscribePattern": NotRequired[str],
        "Classification": NotRequired[str],
        "Delimiter": NotRequired[str],
        "StartingOffsets": NotRequired[str],
        "EndingOffsets": NotRequired[str],
        "PollTimeoutMs": NotRequired[int],
        "NumRetries": NotRequired[int],
        "RetryIntervalMs": NotRequired[int],
        "MaxOffsetsPerTrigger": NotRequired[int],
        "MinPartitions": NotRequired[int],
        "IncludeHeaders": NotRequired[bool],
        "AddRecordTimestamp": NotRequired[str],
        "EmitConsumerLagMetrics": NotRequired[str],
        "StartingTimestamp": NotRequired[TimestampTypeDef],
    },
)
KinesisStreamingSourceOptionsTypeDef = TypedDict(
    "KinesisStreamingSourceOptionsTypeDef",
    {
        "EndpointUrl": NotRequired[str],
        "StreamName": NotRequired[str],
        "Classification": NotRequired[str],
        "Delimiter": NotRequired[str],
        "StartingPosition": NotRequired[StartingPositionType],
        "MaxFetchTimeInMs": NotRequired[int],
        "MaxFetchRecordsPerShard": NotRequired[int],
        "MaxRecordPerRead": NotRequired[int],
        "AddIdleTimeBetweenReads": NotRequired[bool],
        "IdleTimeBetweenReadsInMs": NotRequired[int],
        "DescribeShardInterval": NotRequired[int],
        "NumRetries": NotRequired[int],
        "RetryIntervalMs": NotRequired[int],
        "MaxRetryIntervalMs": NotRequired[int],
        "AvoidEmptyBatches": NotRequired[bool],
        "StreamArn": NotRequired[str],
        "RoleArn": NotRequired[str],
        "RoleSessionName": NotRequired[str],
        "AddRecordTimestamp": NotRequired[str],
        "EmitConsumerLagMetrics": NotRequired[str],
        "StartingTimestamp": NotRequired[TimestampTypeDef],
    },
)
QuerySessionContextTypeDef = TypedDict(
    "QuerySessionContextTypeDef",
    {
        "QueryId": NotRequired[str],
        "QueryStartTime": NotRequired[TimestampTypeDef],
        "ClusterId": NotRequired[str],
        "QueryAuthorizationId": NotRequired[str],
        "AdditionalContext": NotRequired[Mapping[str, str]],
    },
)
TaskRunFilterCriteriaTypeDef = TypedDict(
    "TaskRunFilterCriteriaTypeDef",
    {
        "TaskRunType": NotRequired[TaskTypeType],
        "Status": NotRequired[TaskStatusTypeType],
        "StartedBefore": NotRequired[TimestampTypeDef],
        "StartedAfter": NotRequired[TimestampTypeDef],
    },
)
TimestampFilterTypeDef = TypedDict(
    "TimestampFilterTypeDef",
    {
        "RecordedBefore": NotRequired[TimestampTypeDef],
        "RecordedAfter": NotRequired[TimestampTypeDef],
    },
)
ColumnUnionTypeDef = Union[ColumnTypeDef, ColumnOutputTypeDef]
CompactionMetricsTypeDef = TypedDict(
    "CompactionMetricsTypeDef",
    {
        "IcebergMetrics": NotRequired[IcebergCompactionMetricsTypeDef],
    },
)
PredicateOutputTypeDef = TypedDict(
    "PredicateOutputTypeDef",
    {
        "Logical": NotRequired[LogicalType],
        "Conditions": NotRequired[List[ConditionTypeDef]],
    },
)
PredicateTypeDef = TypedDict(
    "PredicateTypeDef",
    {
        "Logical": NotRequired[LogicalType],
        "Conditions": NotRequired[Sequence[ConditionTypeDef]],
    },
)
ProfileConfigurationOutputTypeDef = TypedDict(
    "ProfileConfigurationOutputTypeDef",
    {
        "SessionConfiguration": NotRequired[Dict[str, ConfigurationObjectOutputTypeDef]],
        "JobConfiguration": NotRequired[Dict[str, ConfigurationObjectOutputTypeDef]],
    },
)
ConfigurationObjectUnionTypeDef = Union[
    ConfigurationObjectTypeDef, ConfigurationObjectOutputTypeDef
]
FindMatchesMetricsTypeDef = TypedDict(
    "FindMatchesMetricsTypeDef",
    {
        "AreaUnderPRCurve": NotRequired[float],
        "Precision": NotRequired[float],
        "Recall": NotRequired[float],
        "F1": NotRequired[float],
        "ConfusionMatrix": NotRequired[ConfusionMatrixTypeDef],
        "ColumnImportances": NotRequired[List[ColumnImportanceTypeDef]],
    },
)
ConnectionsListUnionTypeDef = Union[ConnectionsListTypeDef, ConnectionsListOutputTypeDef]
ConnectorDataTargetUnionTypeDef = Union[
    ConnectorDataTargetTypeDef, ConnectorDataTargetOutputTypeDef
]
CrawlerNodeDetailsTypeDef = TypedDict(
    "CrawlerNodeDetailsTypeDef",
    {
        "Crawls": NotRequired[List[CrawlTypeDef]],
    },
)
ListCrawlsResponseTypeDef = TypedDict(
    "ListCrawlsResponseTypeDef",
    {
        "Crawls": List[CrawlerHistoryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetCrawlerMetricsResponseTypeDef = TypedDict(
    "GetCrawlerMetricsResponseTypeDef",
    {
        "CrawlerMetricsList": List[CrawlerMetricsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CrawlerTargetsOutputTypeDef = TypedDict(
    "CrawlerTargetsOutputTypeDef",
    {
        "S3Targets": NotRequired[List[S3TargetOutputTypeDef]],
        "JdbcTargets": NotRequired[List[JdbcTargetOutputTypeDef]],
        "MongoDBTargets": NotRequired[List[MongoDBTargetTypeDef]],
        "DynamoDBTargets": NotRequired[List[DynamoDBTargetTypeDef]],
        "CatalogTargets": NotRequired[List[CatalogTargetOutputTypeDef]],
        "DeltaTargets": NotRequired[List[DeltaTargetOutputTypeDef]],
        "IcebergTargets": NotRequired[List[IcebergTargetOutputTypeDef]],
        "HudiTargets": NotRequired[List[HudiTargetOutputTypeDef]],
    },
)
ListCrawlsRequestRequestTypeDef = TypedDict(
    "ListCrawlsRequestRequestTypeDef",
    {
        "CrawlerName": str,
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence[CrawlsFilterTypeDef]],
        "NextToken": NotRequired[str],
    },
)
CreateClassifierRequestRequestTypeDef = TypedDict(
    "CreateClassifierRequestRequestTypeDef",
    {
        "GrokClassifier": NotRequired[CreateGrokClassifierRequestTypeDef],
        "XMLClassifier": NotRequired[CreateXMLClassifierRequestTypeDef],
        "JsonClassifier": NotRequired[CreateJsonClassifierRequestTypeDef],
        "CsvClassifier": NotRequired[CreateCsvClassifierRequestTypeDef],
    },
)
CreateDataQualityRulesetRequestRequestTypeDef = TypedDict(
    "CreateDataQualityRulesetRequestRequestTypeDef",
    {
        "Name": str,
        "Ruleset": str,
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "TargetTable": NotRequired[DataQualityTargetTableTypeDef],
        "DataQualitySecurityConfiguration": NotRequired[str],
        "ClientToken": NotRequired[str],
    },
)
DataQualityRulesetFilterCriteriaTypeDef = TypedDict(
    "DataQualityRulesetFilterCriteriaTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "CreatedBefore": NotRequired[TimestampTypeDef],
        "CreatedAfter": NotRequired[TimestampTypeDef],
        "LastModifiedBefore": NotRequired[TimestampTypeDef],
        "LastModifiedAfter": NotRequired[TimestampTypeDef],
        "TargetTable": NotRequired[DataQualityTargetTableTypeDef],
    },
)
DataQualityRulesetListDetailsTypeDef = TypedDict(
    "DataQualityRulesetListDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "CreatedOn": NotRequired[datetime],
        "LastModifiedOn": NotRequired[datetime],
        "TargetTable": NotRequired[DataQualityTargetTableTypeDef],
        "RecommendationRunId": NotRequired[str],
        "RuleCount": NotRequired[int],
    },
)
GetDataQualityRulesetResponseTypeDef = TypedDict(
    "GetDataQualityRulesetResponseTypeDef",
    {
        "Name": str,
        "Description": str,
        "Ruleset": str,
        "TargetTable": DataQualityTargetTableTypeDef,
        "CreatedOn": datetime,
        "LastModifiedOn": datetime,
        "RecommendationRunId": str,
        "DataQualitySecurityConfiguration": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePartitionIndexRequestRequestTypeDef = TypedDict(
    "CreatePartitionIndexRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionIndex": PartitionIndexTypeDef,
        "CatalogId": NotRequired[str],
    },
)
CreateSchemaInputRequestTypeDef = TypedDict(
    "CreateSchemaInputRequestTypeDef",
    {
        "SchemaName": str,
        "DataFormat": DataFormatType,
        "RegistryId": NotRequired[RegistryIdTypeDef],
        "Compatibility": NotRequired[CompatibilityType],
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "SchemaDefinition": NotRequired[str],
    },
)
DeleteRegistryInputRequestTypeDef = TypedDict(
    "DeleteRegistryInputRequestTypeDef",
    {
        "RegistryId": RegistryIdTypeDef,
    },
)
GetRegistryInputRequestTypeDef = TypedDict(
    "GetRegistryInputRequestTypeDef",
    {
        "RegistryId": RegistryIdTypeDef,
    },
)
ListSchemasInputRequestTypeDef = TypedDict(
    "ListSchemasInputRequestTypeDef",
    {
        "RegistryId": NotRequired[RegistryIdTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
UpdateRegistryInputRequestTypeDef = TypedDict(
    "UpdateRegistryInputRequestTypeDef",
    {
        "RegistryId": RegistryIdTypeDef,
        "Description": str,
    },
)
CreateSessionRequestRequestTypeDef = TypedDict(
    "CreateSessionRequestRequestTypeDef",
    {
        "Id": str,
        "Role": str,
        "Command": SessionCommandTypeDef,
        "Description": NotRequired[str],
        "Timeout": NotRequired[int],
        "IdleTimeout": NotRequired[int],
        "DefaultArguments": NotRequired[Mapping[str, str]],
        "Connections": NotRequired[ConnectionsListTypeDef],
        "MaxCapacity": NotRequired[float],
        "NumberOfWorkers": NotRequired[int],
        "WorkerType": NotRequired[WorkerTypeType],
        "SecurityConfiguration": NotRequired[str],
        "GlueVersion": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "RequestOrigin": NotRequired[str],
    },
)
SessionTypeDef = TypedDict(
    "SessionTypeDef",
    {
        "Id": NotRequired[str],
        "CreatedOn": NotRequired[datetime],
        "Status": NotRequired[SessionStatusType],
        "ErrorMessage": NotRequired[str],
        "Description": NotRequired[str],
        "Role": NotRequired[str],
        "Command": NotRequired[SessionCommandTypeDef],
        "DefaultArguments": NotRequired[Dict[str, str]],
        "Connections": NotRequired[ConnectionsListOutputTypeDef],
        "Progress": NotRequired[float],
        "MaxCapacity": NotRequired[float],
        "SecurityConfiguration": NotRequired[str],
        "GlueVersion": NotRequired[str],
        "NumberOfWorkers": NotRequired[int],
        "WorkerType": NotRequired[WorkerTypeType],
        "CompletedOn": NotRequired[datetime],
        "ExecutionTime": NotRequired[float],
        "DPUSeconds": NotRequired[float],
        "IdleTimeout": NotRequired[int],
        "ProfileName": NotRequired[str],
    },
)
EvaluateDataQualityMultiFrameOutputTypeDef = TypedDict(
    "EvaluateDataQualityMultiFrameOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Ruleset": str,
        "AdditionalDataSources": NotRequired[Dict[str, str]],
        "PublishingOptions": NotRequired[DQResultsPublishingOptionsTypeDef],
        "AdditionalOptions": NotRequired[Dict[AdditionalOptionKeysType, str]],
        "StopJobOnFailureOptions": NotRequired[DQStopJobOnFailureOptionsTypeDef],
    },
)
EvaluateDataQualityMultiFrameTypeDef = TypedDict(
    "EvaluateDataQualityMultiFrameTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "Ruleset": str,
        "AdditionalDataSources": NotRequired[Mapping[str, str]],
        "PublishingOptions": NotRequired[DQResultsPublishingOptionsTypeDef],
        "AdditionalOptions": NotRequired[Mapping[AdditionalOptionKeysType, str]],
        "StopJobOnFailureOptions": NotRequired[DQStopJobOnFailureOptionsTypeDef],
    },
)
EvaluateDataQualityOutputTypeDef = TypedDict(
    "EvaluateDataQualityOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Ruleset": str,
        "Output": NotRequired[DQTransformOutputType],
        "PublishingOptions": NotRequired[DQResultsPublishingOptionsTypeDef],
        "StopJobOnFailureOptions": NotRequired[DQStopJobOnFailureOptionsTypeDef],
    },
)
EvaluateDataQualityTypeDef = TypedDict(
    "EvaluateDataQualityTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "Ruleset": str,
        "Output": NotRequired[DQTransformOutputType],
        "PublishingOptions": NotRequired[DQResultsPublishingOptionsTypeDef],
        "StopJobOnFailureOptions": NotRequired[DQStopJobOnFailureOptionsTypeDef],
    },
)
DataCatalogEncryptionSettingsTypeDef = TypedDict(
    "DataCatalogEncryptionSettingsTypeDef",
    {
        "EncryptionAtRest": NotRequired[EncryptionAtRestTypeDef],
        "ConnectionPasswordEncryption": NotRequired[ConnectionPasswordEncryptionTypeDef],
    },
)
PrincipalPermissionsOutputTypeDef = TypedDict(
    "PrincipalPermissionsOutputTypeDef",
    {
        "Principal": NotRequired[DataLakePrincipalTypeDef],
        "Permissions": NotRequired[List[PermissionType]],
    },
)
PrincipalPermissionsTypeDef = TypedDict(
    "PrincipalPermissionsTypeDef",
    {
        "Principal": NotRequired[DataLakePrincipalTypeDef],
        "Permissions": NotRequired[Sequence[PermissionType]],
    },
)
MetricBasedObservationTypeDef = TypedDict(
    "MetricBasedObservationTypeDef",
    {
        "MetricName": NotRequired[str],
        "StatisticId": NotRequired[str],
        "MetricValues": NotRequired[DataQualityMetricValuesTypeDef],
        "NewRules": NotRequired[List[str]],
    },
)
DataSourceOutputTypeDef = TypedDict(
    "DataSourceOutputTypeDef",
    {
        "GlueTable": GlueTableOutputTypeDef,
    },
)
NullValueFieldTypeDef = TypedDict(
    "NullValueFieldTypeDef",
    {
        "Value": str,
        "Datatype": DatatypeTypeDef,
    },
)
DecimalColumnStatisticsDataOutputTypeDef = TypedDict(
    "DecimalColumnStatisticsDataOutputTypeDef",
    {
        "NumberOfNulls": int,
        "NumberOfDistinctValues": int,
        "MinimumValue": NotRequired[DecimalNumberOutputTypeDef],
        "MaximumValue": NotRequired[DecimalNumberOutputTypeDef],
    },
)
DeleteSchemaInputRequestTypeDef = TypedDict(
    "DeleteSchemaInputRequestTypeDef",
    {
        "SchemaId": SchemaIdTypeDef,
    },
)
DeleteSchemaVersionsInputRequestTypeDef = TypedDict(
    "DeleteSchemaVersionsInputRequestTypeDef",
    {
        "SchemaId": SchemaIdTypeDef,
        "Versions": str,
    },
)
GetSchemaByDefinitionInputRequestTypeDef = TypedDict(
    "GetSchemaByDefinitionInputRequestTypeDef",
    {
        "SchemaId": SchemaIdTypeDef,
        "SchemaDefinition": str,
    },
)
GetSchemaInputRequestTypeDef = TypedDict(
    "GetSchemaInputRequestTypeDef",
    {
        "SchemaId": SchemaIdTypeDef,
    },
)
ListSchemaVersionsInputRequestTypeDef = TypedDict(
    "ListSchemaVersionsInputRequestTypeDef",
    {
        "SchemaId": SchemaIdTypeDef,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
RegisterSchemaVersionInputRequestTypeDef = TypedDict(
    "RegisterSchemaVersionInputRequestTypeDef",
    {
        "SchemaId": SchemaIdTypeDef,
        "SchemaDefinition": str,
    },
)
SchemaReferenceTypeDef = TypedDict(
    "SchemaReferenceTypeDef",
    {
        "SchemaId": NotRequired[SchemaIdTypeDef],
        "SchemaVersionId": NotRequired[str],
        "SchemaVersionNumber": NotRequired[int],
    },
)
DeltaTargetUnionTypeDef = Union[DeltaTargetTypeDef, DeltaTargetOutputTypeDef]
UpdateDevEndpointRequestRequestTypeDef = TypedDict(
    "UpdateDevEndpointRequestRequestTypeDef",
    {
        "EndpointName": str,
        "PublicKey": NotRequired[str],
        "AddPublicKeys": NotRequired[Sequence[str]],
        "DeletePublicKeys": NotRequired[Sequence[str]],
        "CustomLibraries": NotRequired[DevEndpointCustomLibrariesTypeDef],
        "UpdateEtlLibraries": NotRequired[bool],
        "DeleteArguments": NotRequired[Sequence[str]],
        "AddArguments": NotRequired[Mapping[str, str]],
    },
)
S3DeltaDirectTargetOutputTypeDef = TypedDict(
    "S3DeltaDirectTargetOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Path": str,
        "Compression": DeltaTargetCompressionTypeType,
        "Format": TargetFormatType,
        "PartitionKeys": NotRequired[List[List[str]]],
        "AdditionalOptions": NotRequired[Dict[str, str]],
        "SchemaChangePolicy": NotRequired[DirectSchemaChangePolicyTypeDef],
    },
)
S3DeltaDirectTargetTypeDef = TypedDict(
    "S3DeltaDirectTargetTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "Path": str,
        "Compression": DeltaTargetCompressionTypeType,
        "Format": TargetFormatType,
        "PartitionKeys": NotRequired[Sequence[Sequence[str]]],
        "AdditionalOptions": NotRequired[Mapping[str, str]],
        "SchemaChangePolicy": NotRequired[DirectSchemaChangePolicyTypeDef],
    },
)
S3DirectTargetOutputTypeDef = TypedDict(
    "S3DirectTargetOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Path": str,
        "Format": TargetFormatType,
        "PartitionKeys": NotRequired[List[List[str]]],
        "Compression": NotRequired[str],
        "SchemaChangePolicy": NotRequired[DirectSchemaChangePolicyTypeDef],
    },
)
S3DirectTargetTypeDef = TypedDict(
    "S3DirectTargetTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "Path": str,
        "Format": TargetFormatType,
        "PartitionKeys": NotRequired[Sequence[Sequence[str]]],
        "Compression": NotRequired[str],
        "SchemaChangePolicy": NotRequired[DirectSchemaChangePolicyTypeDef],
    },
)
S3GlueParquetTargetOutputTypeDef = TypedDict(
    "S3GlueParquetTargetOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Path": str,
        "PartitionKeys": NotRequired[List[List[str]]],
        "Compression": NotRequired[ParquetCompressionTypeType],
        "SchemaChangePolicy": NotRequired[DirectSchemaChangePolicyTypeDef],
    },
)
S3GlueParquetTargetTypeDef = TypedDict(
    "S3GlueParquetTargetTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "Path": str,
        "PartitionKeys": NotRequired[Sequence[Sequence[str]]],
        "Compression": NotRequired[ParquetCompressionTypeType],
        "SchemaChangePolicy": NotRequired[DirectSchemaChangePolicyTypeDef],
    },
)
S3HudiDirectTargetOutputTypeDef = TypedDict(
    "S3HudiDirectTargetOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Path": str,
        "Compression": HudiTargetCompressionTypeType,
        "Format": TargetFormatType,
        "AdditionalOptions": Dict[str, str],
        "PartitionKeys": NotRequired[List[List[str]]],
        "SchemaChangePolicy": NotRequired[DirectSchemaChangePolicyTypeDef],
    },
)
S3HudiDirectTargetTypeDef = TypedDict(
    "S3HudiDirectTargetTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "Path": str,
        "Compression": HudiTargetCompressionTypeType,
        "Format": TargetFormatType,
        "AdditionalOptions": Mapping[str, str],
        "PartitionKeys": NotRequired[Sequence[Sequence[str]]],
        "SchemaChangePolicy": NotRequired[DirectSchemaChangePolicyTypeDef],
    },
)
DropDuplicatesUnionTypeDef = Union[DropDuplicatesTypeDef, DropDuplicatesOutputTypeDef]
DropFieldsUnionTypeDef = Union[DropFieldsTypeDef, DropFieldsOutputTypeDef]
EncryptionConfigurationOutputTypeDef = TypedDict(
    "EncryptionConfigurationOutputTypeDef",
    {
        "S3Encryption": NotRequired[List[S3EncryptionTypeDef]],
        "CloudWatchEncryption": NotRequired[CloudWatchEncryptionTypeDef],
        "JobBookmarksEncryption": NotRequired[JobBookmarksEncryptionTypeDef],
    },
)
EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "S3Encryption": NotRequired[Sequence[S3EncryptionTypeDef]],
        "CloudWatchEncryption": NotRequired[CloudWatchEncryptionTypeDef],
        "JobBookmarksEncryption": NotRequired[JobBookmarksEncryptionTypeDef],
    },
)
SchemaVersionErrorItemTypeDef = TypedDict(
    "SchemaVersionErrorItemTypeDef",
    {
        "VersionNumber": NotRequired[int],
        "ErrorDetails": NotRequired[ErrorDetailsTypeDef],
    },
)
FillMissingValuesUnionTypeDef = Union[FillMissingValuesTypeDef, FillMissingValuesOutputTypeDef]
FilterExpressionOutputTypeDef = TypedDict(
    "FilterExpressionOutputTypeDef",
    {
        "Operation": FilterOperationType,
        "Values": List[FilterValueOutputTypeDef],
        "Negated": NotRequired[bool],
    },
)
FilterValueUnionTypeDef = Union[FilterValueTypeDef, FilterValueOutputTypeDef]
TransformParametersTypeDef = TypedDict(
    "TransformParametersTypeDef",
    {
        "TransformType": Literal["FIND_MATCHES"],
        "FindMatchesParameters": NotRequired[FindMatchesParametersTypeDef],
    },
)
GetClassifiersRequestGetClassifiersPaginateTypeDef = TypedDict(
    "GetClassifiersRequestGetClassifiersPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetCrawlerMetricsRequestGetCrawlerMetricsPaginateTypeDef = TypedDict(
    "GetCrawlerMetricsRequestGetCrawlerMetricsPaginateTypeDef",
    {
        "CrawlerNameList": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetCrawlersRequestGetCrawlersPaginateTypeDef = TypedDict(
    "GetCrawlersRequestGetCrawlersPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetDatabasesRequestGetDatabasesPaginateTypeDef = TypedDict(
    "GetDatabasesRequestGetDatabasesPaginateTypeDef",
    {
        "CatalogId": NotRequired[str],
        "ResourceShareType": NotRequired[ResourceShareTypeType],
        "AttributesToGet": NotRequired[Sequence[Literal["NAME"]]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetDevEndpointsRequestGetDevEndpointsPaginateTypeDef = TypedDict(
    "GetDevEndpointsRequestGetDevEndpointsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetJobRunsRequestGetJobRunsPaginateTypeDef = TypedDict(
    "GetJobRunsRequestGetJobRunsPaginateTypeDef",
    {
        "JobName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetJobsRequestGetJobsPaginateTypeDef = TypedDict(
    "GetJobsRequestGetJobsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetPartitionIndexesRequestGetPartitionIndexesPaginateTypeDef = TypedDict(
    "GetPartitionIndexesRequestGetPartitionIndexesPaginateTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "CatalogId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetResourcePoliciesRequestGetResourcePoliciesPaginateTypeDef = TypedDict(
    "GetResourcePoliciesRequestGetResourcePoliciesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetSecurityConfigurationsRequestGetSecurityConfigurationsPaginateTypeDef = TypedDict(
    "GetSecurityConfigurationsRequestGetSecurityConfigurationsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetTableVersionsRequestGetTableVersionsPaginateTypeDef = TypedDict(
    "GetTableVersionsRequestGetTableVersionsPaginateTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "CatalogId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetTablesRequestGetTablesPaginateTypeDef = TypedDict(
    "GetTablesRequestGetTablesPaginateTypeDef",
    {
        "DatabaseName": str,
        "CatalogId": NotRequired[str],
        "Expression": NotRequired[str],
        "TransactionId": NotRequired[str],
        "QueryAsOfTime": NotRequired[TimestampTypeDef],
        "IncludeStatusDetails": NotRequired[bool],
        "AttributesToGet": NotRequired[Sequence[TableAttributesType]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetTriggersRequestGetTriggersPaginateTypeDef = TypedDict(
    "GetTriggersRequestGetTriggersPaginateTypeDef",
    {
        "DependentJobName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetUserDefinedFunctionsRequestGetUserDefinedFunctionsPaginateTypeDef = TypedDict(
    "GetUserDefinedFunctionsRequestGetUserDefinedFunctionsPaginateTypeDef",
    {
        "Pattern": str,
        "CatalogId": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetWorkflowRunsRequestGetWorkflowRunsPaginateTypeDef = TypedDict(
    "GetWorkflowRunsRequestGetWorkflowRunsPaginateTypeDef",
    {
        "Name": str,
        "IncludeGraph": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListBlueprintsRequestListBlueprintsPaginateTypeDef = TypedDict(
    "ListBlueprintsRequestListBlueprintsPaginateTypeDef",
    {
        "Tags": NotRequired[Mapping[str, str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListJobsRequestListJobsPaginateTypeDef = TypedDict(
    "ListJobsRequestListJobsPaginateTypeDef",
    {
        "Tags": NotRequired[Mapping[str, str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRegistriesInputListRegistriesPaginateTypeDef = TypedDict(
    "ListRegistriesInputListRegistriesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSchemaVersionsInputListSchemaVersionsPaginateTypeDef = TypedDict(
    "ListSchemaVersionsInputListSchemaVersionsPaginateTypeDef",
    {
        "SchemaId": SchemaIdTypeDef,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSchemasInputListSchemasPaginateTypeDef = TypedDict(
    "ListSchemasInputListSchemasPaginateTypeDef",
    {
        "RegistryId": NotRequired[RegistryIdTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTableOptimizerRunsRequestListTableOptimizerRunsPaginateTypeDef = TypedDict(
    "ListTableOptimizerRunsRequestListTableOptimizerRunsPaginateTypeDef",
    {
        "CatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "Type": TableOptimizerTypeType,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTriggersRequestListTriggersPaginateTypeDef = TypedDict(
    "ListTriggersRequestListTriggersPaginateTypeDef",
    {
        "DependentJobName": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListUsageProfilesRequestListUsageProfilesPaginateTypeDef = TypedDict(
    "ListUsageProfilesRequestListUsageProfilesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWorkflowsRequestListWorkflowsPaginateTypeDef = TypedDict(
    "ListWorkflowsRequestListWorkflowsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetConnectionsRequestGetConnectionsPaginateTypeDef = TypedDict(
    "GetConnectionsRequestGetConnectionsPaginateTypeDef",
    {
        "CatalogId": NotRequired[str],
        "Filter": NotRequired[GetConnectionsFilterTypeDef],
        "HidePassword": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetConnectionsRequestRequestTypeDef = TypedDict(
    "GetConnectionsRequestRequestTypeDef",
    {
        "CatalogId": NotRequired[str],
        "Filter": NotRequired[GetConnectionsFilterTypeDef],
        "HidePassword": NotRequired[bool],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GetDataQualityModelResultResponseTypeDef = TypedDict(
    "GetDataQualityModelResultResponseTypeDef",
    {
        "CompletedOn": datetime,
        "Model": List[StatisticModelResultTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetJobBookmarkResponseTypeDef = TypedDict(
    "GetJobBookmarkResponseTypeDef",
    {
        "JobBookmarkEntry": JobBookmarkEntryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResetJobBookmarkResponseTypeDef = TypedDict(
    "ResetJobBookmarkResponseTypeDef",
    {
        "JobBookmarkEntry": JobBookmarkEntryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TransformFilterCriteriaTypeDef = TypedDict(
    "TransformFilterCriteriaTypeDef",
    {
        "Name": NotRequired[str],
        "TransformType": NotRequired[Literal["FIND_MATCHES"]],
        "Status": NotRequired[TransformStatusTypeType],
        "GlueVersion": NotRequired[str],
        "CreatedBefore": NotRequired[TimestampTypeDef],
        "CreatedAfter": NotRequired[TimestampTypeDef],
        "LastModifiedBefore": NotRequired[TimestampTypeDef],
        "LastModifiedAfter": NotRequired[TimestampTypeDef],
        "Schema": NotRequired[Sequence[SchemaColumnTypeDef]],
    },
)
GetMappingResponseTypeDef = TypedDict(
    "GetMappingResponseTypeDef",
    {
        "Mapping": List[MappingEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPartitionsRequestGetPartitionsPaginateTypeDef = TypedDict(
    "GetPartitionsRequestGetPartitionsPaginateTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "CatalogId": NotRequired[str],
        "Expression": NotRequired[str],
        "Segment": NotRequired[SegmentTypeDef],
        "ExcludeColumnSchema": NotRequired[bool],
        "TransactionId": NotRequired[str],
        "QueryAsOfTime": NotRequired[TimestampTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetPartitionsRequestRequestTypeDef = TypedDict(
    "GetPartitionsRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "CatalogId": NotRequired[str],
        "Expression": NotRequired[str],
        "NextToken": NotRequired[str],
        "Segment": NotRequired[SegmentTypeDef],
        "MaxResults": NotRequired[int],
        "ExcludeColumnSchema": NotRequired[bool],
        "TransactionId": NotRequired[str],
        "QueryAsOfTime": NotRequired[TimestampTypeDef],
    },
)
GetResourcePoliciesResponseTypeDef = TypedDict(
    "GetResourcePoliciesResponseTypeDef",
    {
        "GetResourcePoliciesResponseList": List[GluePolicyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetSchemaVersionInputRequestTypeDef = TypedDict(
    "GetSchemaVersionInputRequestTypeDef",
    {
        "SchemaId": NotRequired[SchemaIdTypeDef],
        "SchemaVersionId": NotRequired[str],
        "SchemaVersionNumber": NotRequired[SchemaVersionNumberTypeDef],
    },
)
GetSchemaVersionsDiffInputRequestTypeDef = TypedDict(
    "GetSchemaVersionsDiffInputRequestTypeDef",
    {
        "SchemaId": SchemaIdTypeDef,
        "FirstSchemaVersionNumber": SchemaVersionNumberTypeDef,
        "SecondSchemaVersionNumber": SchemaVersionNumberTypeDef,
        "SchemaDiffType": Literal["SYNTAX_DIFF"],
    },
)
UpdateSchemaInputRequestTypeDef = TypedDict(
    "UpdateSchemaInputRequestTypeDef",
    {
        "SchemaId": SchemaIdTypeDef,
        "SchemaVersionNumber": NotRequired[SchemaVersionNumberTypeDef],
        "Compatibility": NotRequired[CompatibilityType],
        "Description": NotRequired[str],
    },
)
GlueSchemaOutputTypeDef = TypedDict(
    "GlueSchemaOutputTypeDef",
    {
        "Columns": NotRequired[List[GlueStudioSchemaColumnTypeDef]],
    },
)
GlueSchemaTypeDef = TypedDict(
    "GlueSchemaTypeDef",
    {
        "Columns": NotRequired[Sequence[GlueStudioSchemaColumnTypeDef]],
    },
)
GlueTableUnionTypeDef = Union[GlueTableTypeDef, GlueTableOutputTypeDef]
GovernedCatalogSourceTypeDef = TypedDict(
    "GovernedCatalogSourceTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
        "PartitionPredicate": NotRequired[str],
        "AdditionalOptions": NotRequired[S3SourceAdditionalOptionsTypeDef],
    },
)
S3CatalogSourceTypeDef = TypedDict(
    "S3CatalogSourceTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
        "PartitionPredicate": NotRequired[str],
        "AdditionalOptions": NotRequired[S3SourceAdditionalOptionsTypeDef],
    },
)
HudiTargetUnionTypeDef = Union[HudiTargetTypeDef, HudiTargetOutputTypeDef]
OpenTableFormatInputTypeDef = TypedDict(
    "OpenTableFormatInputTypeDef",
    {
        "IcebergInput": NotRequired[IcebergInputTypeDef],
    },
)
OrphanFileDeletionConfigurationTypeDef = TypedDict(
    "OrphanFileDeletionConfigurationTypeDef",
    {
        "icebergConfiguration": NotRequired[IcebergOrphanFileDeletionConfigurationTypeDef],
    },
)
OrphanFileDeletionMetricsTypeDef = TypedDict(
    "OrphanFileDeletionMetricsTypeDef",
    {
        "IcebergMetrics": NotRequired[IcebergOrphanFileDeletionMetricsTypeDef],
    },
)
RetentionConfigurationTypeDef = TypedDict(
    "RetentionConfigurationTypeDef",
    {
        "icebergConfiguration": NotRequired[IcebergRetentionConfigurationTypeDef],
    },
)
RetentionMetricsTypeDef = TypedDict(
    "RetentionMetricsTypeDef",
    {
        "IcebergMetrics": NotRequired[IcebergRetentionMetricsTypeDef],
    },
)
IcebergTargetUnionTypeDef = Union[IcebergTargetTypeDef, IcebergTargetOutputTypeDef]
JDBCConnectorOptionsUnionTypeDef = Union[
    JDBCConnectorOptionsTypeDef, JDBCConnectorOptionsOutputTypeDef
]
JdbcTargetUnionTypeDef = Union[JdbcTargetTypeDef, JdbcTargetOutputTypeDef]
JobRunTypeDef = TypedDict(
    "JobRunTypeDef",
    {
        "Id": NotRequired[str],
        "Attempt": NotRequired[int],
        "PreviousRunId": NotRequired[str],
        "TriggerName": NotRequired[str],
        "JobName": NotRequired[str],
        "JobMode": NotRequired[JobModeType],
        "JobRunQueuingEnabled": NotRequired[bool],
        "StartedOn": NotRequired[datetime],
        "LastModifiedOn": NotRequired[datetime],
        "CompletedOn": NotRequired[datetime],
        "JobRunState": NotRequired[JobRunStateType],
        "Arguments": NotRequired[Dict[str, str]],
        "ErrorMessage": NotRequired[str],
        "PredecessorRuns": NotRequired[List[PredecessorTypeDef]],
        "AllocatedCapacity": NotRequired[int],
        "ExecutionTime": NotRequired[int],
        "Timeout": NotRequired[int],
        "MaxCapacity": NotRequired[float],
        "WorkerType": NotRequired[WorkerTypeType],
        "NumberOfWorkers": NotRequired[int],
        "SecurityConfiguration": NotRequired[str],
        "LogGroupName": NotRequired[str],
        "NotificationProperty": NotRequired[NotificationPropertyTypeDef],
        "GlueVersion": NotRequired[str],
        "DPUSeconds": NotRequired[float],
        "ExecutionClass": NotRequired[ExecutionClassType],
        "MaintenanceWindow": NotRequired[str],
        "ProfileName": NotRequired[str],
        "StateDetail": NotRequired[str],
    },
)
JoinOutputTypeDef = TypedDict(
    "JoinOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "JoinType": JoinTypeType,
        "Columns": List[JoinColumnOutputTypeDef],
    },
)
JoinColumnUnionTypeDef = Union[JoinColumnTypeDef, JoinColumnOutputTypeDef]
TaskRunPropertiesTypeDef = TypedDict(
    "TaskRunPropertiesTypeDef",
    {
        "TaskType": NotRequired[TaskTypeType],
        "ImportLabelsTaskRunProperties": NotRequired[ImportLabelsTaskRunPropertiesTypeDef],
        "ExportLabelsTaskRunProperties": NotRequired[ExportLabelsTaskRunPropertiesTypeDef],
        "LabelingSetGenerationTaskRunProperties": NotRequired[
            LabelingSetGenerationTaskRunPropertiesTypeDef
        ],
        "FindMatchesTaskRunProperties": NotRequired[FindMatchesTaskRunPropertiesTypeDef],
    },
)
ListRegistriesResponseTypeDef = TypedDict(
    "ListRegistriesResponseTypeDef",
    {
        "Registries": List[RegistryListItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListSchemaVersionsResponseTypeDef = TypedDict(
    "ListSchemaVersionsResponseTypeDef",
    {
        "Schemas": List[SchemaVersionListItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListSchemasResponseTypeDef = TypedDict(
    "ListSchemasResponseTypeDef",
    {
        "Schemas": List[SchemaListItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListUsageProfilesResponseTypeDef = TypedDict(
    "ListUsageProfilesResponseTypeDef",
    {
        "Profiles": List[UsageProfileDefinitionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
TransformEncryptionTypeDef = TypedDict(
    "TransformEncryptionTypeDef",
    {
        "MlUserDataEncryption": NotRequired[MLUserDataEncryptionTypeDef],
        "TaskRunSecurityConfigurationName": NotRequired[str],
    },
)
MappingUnionTypeDef = Union[MappingTypeDef, MappingOutputTypeDef]
MergeUnionTypeDef = Union[MergeTypeDef, MergeOutputTypeDef]
MetadataInfoTypeDef = TypedDict(
    "MetadataInfoTypeDef",
    {
        "MetadataValue": NotRequired[str],
        "CreatedTime": NotRequired[str],
        "OtherMetadataValueList": NotRequired[List[OtherMetadataValueListItemTypeDef]],
    },
)
PutSchemaVersionMetadataInputRequestTypeDef = TypedDict(
    "PutSchemaVersionMetadataInputRequestTypeDef",
    {
        "MetadataKeyValue": MetadataKeyValuePairTypeDef,
        "SchemaId": NotRequired[SchemaIdTypeDef],
        "SchemaVersionNumber": NotRequired[SchemaVersionNumberTypeDef],
        "SchemaVersionId": NotRequired[str],
    },
)
QuerySchemaVersionMetadataInputRequestTypeDef = TypedDict(
    "QuerySchemaVersionMetadataInputRequestTypeDef",
    {
        "SchemaId": NotRequired[SchemaIdTypeDef],
        "SchemaVersionNumber": NotRequired[SchemaVersionNumberTypeDef],
        "SchemaVersionId": NotRequired[str],
        "MetadataList": NotRequired[Sequence[MetadataKeyValuePairTypeDef]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
RemoveSchemaVersionMetadataInputRequestTypeDef = TypedDict(
    "RemoveSchemaVersionMetadataInputRequestTypeDef",
    {
        "MetadataKeyValue": MetadataKeyValuePairTypeDef,
        "SchemaId": NotRequired[SchemaIdTypeDef],
        "SchemaVersionNumber": NotRequired[SchemaVersionNumberTypeDef],
        "SchemaVersionId": NotRequired[str],
    },
)
MicrosoftSQLServerCatalogTargetUnionTypeDef = Union[
    MicrosoftSQLServerCatalogTargetTypeDef, MicrosoftSQLServerCatalogTargetOutputTypeDef
]
MySQLCatalogTargetUnionTypeDef = Union[MySQLCatalogTargetTypeDef, MySQLCatalogTargetOutputTypeDef]
OAuth2PropertiesInputTypeDef = TypedDict(
    "OAuth2PropertiesInputTypeDef",
    {
        "OAuth2GrantType": NotRequired[OAuth2GrantTypeType],
        "OAuth2ClientApplication": NotRequired[OAuth2ClientApplicationTypeDef],
        "TokenUrl": NotRequired[str],
        "TokenUrlParametersMap": NotRequired[Mapping[str, str]],
        "AuthorizationCodeProperties": NotRequired[AuthorizationCodePropertiesTypeDef],
    },
)
OAuth2PropertiesTypeDef = TypedDict(
    "OAuth2PropertiesTypeDef",
    {
        "OAuth2GrantType": NotRequired[OAuth2GrantTypeType],
        "OAuth2ClientApplication": NotRequired[OAuth2ClientApplicationTypeDef],
        "TokenUrl": NotRequired[str],
        "TokenUrlParametersMap": NotRequired[Dict[str, str]],
    },
)
OracleSQLCatalogTargetUnionTypeDef = Union[
    OracleSQLCatalogTargetTypeDef, OracleSQLCatalogTargetOutputTypeDef
]
PIIDetectionUnionTypeDef = Union[PIIDetectionTypeDef, PIIDetectionOutputTypeDef]
PhysicalConnectionRequirementsUnionTypeDef = Union[
    PhysicalConnectionRequirementsTypeDef, PhysicalConnectionRequirementsOutputTypeDef
]
PostgreSQLCatalogTargetUnionTypeDef = Union[
    PostgreSQLCatalogTargetTypeDef, PostgreSQLCatalogTargetOutputTypeDef
]
RecipeStepOutputTypeDef = TypedDict(
    "RecipeStepOutputTypeDef",
    {
        "Action": RecipeActionOutputTypeDef,
        "ConditionExpressions": NotRequired[List[ConditionExpressionTypeDef]],
    },
)
RecipeActionUnionTypeDef = Union[RecipeActionTypeDef, RecipeActionOutputTypeDef]
RedshiftTargetOutputTypeDef = TypedDict(
    "RedshiftTargetOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Database": str,
        "Table": str,
        "RedshiftTmpDir": NotRequired[str],
        "TmpDirIAMRole": NotRequired[str],
        "UpsertRedshiftOptions": NotRequired[UpsertRedshiftTargetOptionsOutputTypeDef],
    },
)
RenameFieldUnionTypeDef = Union[RenameFieldTypeDef, RenameFieldOutputTypeDef]
UserDefinedFunctionInputTypeDef = TypedDict(
    "UserDefinedFunctionInputTypeDef",
    {
        "FunctionName": NotRequired[str],
        "ClassName": NotRequired[str],
        "OwnerName": NotRequired[str],
        "OwnerType": NotRequired[PrincipalTypeType],
        "ResourceUris": NotRequired[Sequence[ResourceUriTypeDef]],
    },
)
UserDefinedFunctionTypeDef = TypedDict(
    "UserDefinedFunctionTypeDef",
    {
        "FunctionName": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "ClassName": NotRequired[str],
        "OwnerName": NotRequired[str],
        "OwnerType": NotRequired[PrincipalTypeType],
        "CreateTime": NotRequired[datetime],
        "ResourceUris": NotRequired[List[ResourceUriTypeDef]],
        "CatalogId": NotRequired[str],
    },
)
S3TargetUnionTypeDef = Union[S3TargetTypeDef, S3TargetOutputTypeDef]
SearchTablesRequestRequestTypeDef = TypedDict(
    "SearchTablesRequestRequestTypeDef",
    {
        "CatalogId": NotRequired[str],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence[PropertyPredicateTypeDef]],
        "SearchText": NotRequired[str],
        "SortCriteria": NotRequired[Sequence[SortCriterionTypeDef]],
        "MaxResults": NotRequired[int],
        "ResourceShareType": NotRequired[ResourceShareTypeType],
        "IncludeStatusDetails": NotRequired[bool],
    },
)
SelectFieldsUnionTypeDef = Union[SelectFieldsTypeDef, SelectFieldsOutputTypeDef]
SelectFromCollectionUnionTypeDef = Union[
    SelectFromCollectionTypeDef, SelectFromCollectionOutputTypeDef
]
SerDeInfoUnionTypeDef = Union[SerDeInfoTypeDef, SerDeInfoOutputTypeDef]
SkewedInfoUnionTypeDef = Union[SkewedInfoTypeDef, SkewedInfoOutputTypeDef]
SpigotUnionTypeDef = Union[SpigotTypeDef, SpigotOutputTypeDef]
SplitFieldsUnionTypeDef = Union[SplitFieldsTypeDef, SplitFieldsOutputTypeDef]
StatementOutputTypeDef = TypedDict(
    "StatementOutputTypeDef",
    {
        "Data": NotRequired[StatementOutputDataTypeDef],
        "ExecutionCount": NotRequired[int],
        "Status": NotRequired[StatementStateType],
        "ErrorName": NotRequired[str],
        "ErrorValue": NotRequired[str],
        "Traceback": NotRequired[List[str]],
    },
)
StatisticAnnotationTypeDef = TypedDict(
    "StatisticAnnotationTypeDef",
    {
        "ProfileId": NotRequired[str],
        "StatisticId": NotRequired[str],
        "StatisticRecordedOn": NotRequired[datetime],
        "InclusionAnnotation": NotRequired[TimestampedInclusionAnnotationTypeDef],
    },
)
StatisticSummaryTypeDef = TypedDict(
    "StatisticSummaryTypeDef",
    {
        "StatisticId": NotRequired[str],
        "ProfileId": NotRequired[str],
        "RunIdentifier": NotRequired[RunIdentifierTypeDef],
        "StatisticName": NotRequired[str],
        "DoubleValue": NotRequired[float],
        "EvaluationLevel": NotRequired[StatisticEvaluationLevelType],
        "ColumnsReferenced": NotRequired[List[str]],
        "ReferencedDatasets": NotRequired[List[str]],
        "StatisticProperties": NotRequired[Dict[str, str]],
        "RecordedOn": NotRequired[datetime],
        "InclusionAnnotation": NotRequired[TimestampedInclusionAnnotationTypeDef],
    },
)
TransformConfigParameterUnionTypeDef = Union[
    TransformConfigParameterTypeDef, TransformConfigParameterOutputTypeDef
]
UnionUnionTypeDef = Union[UnionTypeDef, UnionOutputTypeDef]
UpdateClassifierRequestRequestTypeDef = TypedDict(
    "UpdateClassifierRequestRequestTypeDef",
    {
        "GrokClassifier": NotRequired[UpdateGrokClassifierRequestTypeDef],
        "XMLClassifier": NotRequired[UpdateXMLClassifierRequestTypeDef],
        "JsonClassifier": NotRequired[UpdateJsonClassifierRequestTypeDef],
        "CsvClassifier": NotRequired[UpdateCsvClassifierRequestTypeDef],
    },
)
UpsertRedshiftTargetOptionsUnionTypeDef = Union[
    UpsertRedshiftTargetOptionsTypeDef, UpsertRedshiftTargetOptionsOutputTypeDef
]
ViewDefinitionInputTypeDef = TypedDict(
    "ViewDefinitionInputTypeDef",
    {
        "IsProtected": NotRequired[bool],
        "Definer": NotRequired[str],
        "Representations": NotRequired[Sequence[ViewRepresentationInputTypeDef]],
        "SubObjects": NotRequired[Sequence[str]],
    },
)
ViewDefinitionTypeDef = TypedDict(
    "ViewDefinitionTypeDef",
    {
        "IsProtected": NotRequired[bool],
        "Definer": NotRequired[str],
        "SubObjects": NotRequired[List[str]],
        "Representations": NotRequired[List[ViewRepresentationTypeDef]],
    },
)
ActionUnionTypeDef = Union[ActionTypeDef, ActionOutputTypeDef]
AggregateTypeDef = TypedDict(
    "AggregateTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "Groups": Sequence[Sequence[str]],
        "Aggs": Sequence[AggregateOperationUnionTypeDef],
    },
)
AmazonRedshiftSourceOutputTypeDef = TypedDict(
    "AmazonRedshiftSourceOutputTypeDef",
    {
        "Name": NotRequired[str],
        "Data": NotRequired[AmazonRedshiftNodeDataOutputTypeDef],
    },
)
AmazonRedshiftTargetOutputTypeDef = TypedDict(
    "AmazonRedshiftTargetOutputTypeDef",
    {
        "Name": NotRequired[str],
        "Data": NotRequired[AmazonRedshiftNodeDataOutputTypeDef],
        "Inputs": NotRequired[List[str]],
    },
)
AmazonRedshiftNodeDataUnionTypeDef = Union[
    AmazonRedshiftNodeDataTypeDef, AmazonRedshiftNodeDataOutputTypeDef
]
SnowflakeTargetOutputTypeDef = TypedDict(
    "SnowflakeTargetOutputTypeDef",
    {
        "Name": str,
        "Data": SnowflakeNodeDataOutputTypeDef,
        "Inputs": NotRequired[List[str]],
    },
)
SnowflakeNodeDataUnionTypeDef = Union[SnowflakeNodeDataTypeDef, SnowflakeNodeDataOutputTypeDef]
PartitionIndexDescriptorTypeDef = TypedDict(
    "PartitionIndexDescriptorTypeDef",
    {
        "IndexName": str,
        "Keys": List[KeySchemaElementTypeDef],
        "IndexStatus": PartitionIndexStatusType,
        "BackfillErrors": NotRequired[List[BackfillErrorTypeDef]],
    },
)
BatchStopJobRunResponseTypeDef = TypedDict(
    "BatchStopJobRunResponseTypeDef",
    {
        "SuccessfulSubmissions": List[BatchStopJobRunSuccessfulSubmissionTypeDef],
        "Errors": List[BatchStopJobRunErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchUpdatePartitionResponseTypeDef = TypedDict(
    "BatchUpdatePartitionResponseTypeDef",
    {
        "Errors": List[BatchUpdatePartitionFailureEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchCreatePartitionResponseTypeDef = TypedDict(
    "BatchCreatePartitionResponseTypeDef",
    {
        "Errors": List[PartitionErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDeletePartitionResponseTypeDef = TypedDict(
    "BatchDeletePartitionResponseTypeDef",
    {
        "Errors": List[PartitionErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDeleteTableResponseTypeDef = TypedDict(
    "BatchDeleteTableResponseTypeDef",
    {
        "Errors": List[TableErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDeleteTableVersionResponseTypeDef = TypedDict(
    "BatchDeleteTableVersionResponseTypeDef",
    {
        "Errors": List[TableVersionErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StatusDetailsPaginatorTypeDef = TypedDict(
    "StatusDetailsPaginatorTypeDef",
    {
        "RequestedChange": NotRequired[Dict[str, Any]],
        "ViewValidations": NotRequired[List[ViewValidationTypeDef]],
    },
)
StatusDetailsTypeDef = TypedDict(
    "StatusDetailsTypeDef",
    {
        "RequestedChange": NotRequired[Dict[str, Any]],
        "ViewValidations": NotRequired[List[ViewValidationTypeDef]],
    },
)
BatchDeletePartitionRequestRequestTypeDef = TypedDict(
    "BatchDeletePartitionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionsToDelete": Sequence[PartitionValueListUnionTypeDef],
        "CatalogId": NotRequired[str],
    },
)
DecimalNumberUnionTypeDef = Union[DecimalNumberTypeDef, DecimalNumberOutputTypeDef]
BatchGetBlueprintsResponseTypeDef = TypedDict(
    "BatchGetBlueprintsResponseTypeDef",
    {
        "Blueprints": List[BlueprintTypeDef],
        "MissingBlueprints": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetBlueprintResponseTypeDef = TypedDict(
    "GetBlueprintResponseTypeDef",
    {
        "Blueprint": BlueprintTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GovernedCatalogTargetUnionTypeDef = Union[
    GovernedCatalogTargetTypeDef, GovernedCatalogTargetOutputTypeDef
]
S3CatalogTargetUnionTypeDef = Union[S3CatalogTargetTypeDef, S3CatalogTargetOutputTypeDef]
S3DeltaCatalogTargetUnionTypeDef = Union[
    S3DeltaCatalogTargetTypeDef, S3DeltaCatalogTargetOutputTypeDef
]
S3HudiCatalogTargetUnionTypeDef = Union[
    S3HudiCatalogTargetTypeDef, S3HudiCatalogTargetOutputTypeDef
]
GetClassifierResponseTypeDef = TypedDict(
    "GetClassifierResponseTypeDef",
    {
        "Classifier": ClassifierTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetClassifiersResponseTypeDef = TypedDict(
    "GetClassifiersResponseTypeDef",
    {
        "Classifiers": List[ClassifierTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetDataflowGraphResponseTypeDef = TypedDict(
    "GetDataflowGraphResponseTypeDef",
    {
        "DagNodes": List[CodeGenNodeOutputTypeDef],
        "DagEdges": List[CodeGenEdgeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CodeGenNodeUnionTypeDef = Union[CodeGenNodeTypeDef, CodeGenNodeOutputTypeDef]
GetMappingRequestRequestTypeDef = TypedDict(
    "GetMappingRequestRequestTypeDef",
    {
        "Source": CatalogEntryTypeDef,
        "Sinks": NotRequired[Sequence[CatalogEntryTypeDef]],
        "Location": NotRequired[LocationTypeDef],
    },
)
GetPlanRequestRequestTypeDef = TypedDict(
    "GetPlanRequestRequestTypeDef",
    {
        "Mapping": Sequence[MappingEntryTypeDef],
        "Source": CatalogEntryTypeDef,
        "Sinks": NotRequired[Sequence[CatalogEntryTypeDef]],
        "Location": NotRequired[LocationTypeDef],
        "Language": NotRequired[LanguageType],
        "AdditionalPlanOptionsMap": NotRequired[Mapping[str, str]],
    },
)
DateColumnStatisticsDataUnionTypeDef = Union[
    DateColumnStatisticsDataTypeDef, DateColumnStatisticsDataOutputTypeDef
]
KafkaStreamingSourceOptionsUnionTypeDef = Union[
    KafkaStreamingSourceOptionsTypeDef, KafkaStreamingSourceOptionsOutputTypeDef
]
KinesisStreamingSourceOptionsUnionTypeDef = Union[
    KinesisStreamingSourceOptionsTypeDef, KinesisStreamingSourceOptionsOutputTypeDef
]
GetUnfilteredPartitionMetadataRequestRequestTypeDef = TypedDict(
    "GetUnfilteredPartitionMetadataRequestRequestTypeDef",
    {
        "CatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "PartitionValues": Sequence[str],
        "SupportedPermissionTypes": Sequence[PermissionTypeType],
        "Region": NotRequired[str],
        "AuditContext": NotRequired[AuditContextTypeDef],
        "QuerySessionContext": NotRequired[QuerySessionContextTypeDef],
    },
)
GetUnfilteredPartitionsMetadataRequestRequestTypeDef = TypedDict(
    "GetUnfilteredPartitionsMetadataRequestRequestTypeDef",
    {
        "CatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "SupportedPermissionTypes": Sequence[PermissionTypeType],
        "Region": NotRequired[str],
        "Expression": NotRequired[str],
        "AuditContext": NotRequired[AuditContextTypeDef],
        "NextToken": NotRequired[str],
        "Segment": NotRequired[SegmentTypeDef],
        "MaxResults": NotRequired[int],
        "QuerySessionContext": NotRequired[QuerySessionContextTypeDef],
    },
)
GetUnfilteredTableMetadataRequestRequestTypeDef = TypedDict(
    "GetUnfilteredTableMetadataRequestRequestTypeDef",
    {
        "CatalogId": str,
        "DatabaseName": str,
        "Name": str,
        "SupportedPermissionTypes": Sequence[PermissionTypeType],
        "Region": NotRequired[str],
        "AuditContext": NotRequired[AuditContextTypeDef],
        "ParentResourceArn": NotRequired[str],
        "RootResourceArn": NotRequired[str],
        "SupportedDialect": NotRequired[SupportedDialectTypeDef],
        "Permissions": NotRequired[Sequence[PermissionType]],
        "QuerySessionContext": NotRequired[QuerySessionContextTypeDef],
    },
)
GetMLTaskRunsRequestRequestTypeDef = TypedDict(
    "GetMLTaskRunsRequestRequestTypeDef",
    {
        "TransformId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filter": NotRequired[TaskRunFilterCriteriaTypeDef],
        "Sort": NotRequired[TaskRunSortCriteriaTypeDef],
    },
)
ListDataQualityStatisticAnnotationsRequestRequestTypeDef = TypedDict(
    "ListDataQualityStatisticAnnotationsRequestRequestTypeDef",
    {
        "StatisticId": NotRequired[str],
        "ProfileId": NotRequired[str],
        "TimestampFilter": NotRequired[TimestampFilterTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListDataQualityStatisticsRequestRequestTypeDef = TypedDict(
    "ListDataQualityStatisticsRequestRequestTypeDef",
    {
        "StatisticId": NotRequired[str],
        "ProfileId": NotRequired[str],
        "TimestampFilter": NotRequired[TimestampFilterTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
TriggerTypeDef = TypedDict(
    "TriggerTypeDef",
    {
        "Name": NotRequired[str],
        "WorkflowName": NotRequired[str],
        "Id": NotRequired[str],
        "Type": NotRequired[TriggerTypeType],
        "State": NotRequired[TriggerStateType],
        "Description": NotRequired[str],
        "Schedule": NotRequired[str],
        "Actions": NotRequired[List[ActionOutputTypeDef]],
        "Predicate": NotRequired[PredicateOutputTypeDef],
        "EventBatchingCondition": NotRequired[EventBatchingConditionTypeDef],
    },
)
PredicateUnionTypeDef = Union[PredicateTypeDef, PredicateOutputTypeDef]
GetUsageProfileResponseTypeDef = TypedDict(
    "GetUsageProfileResponseTypeDef",
    {
        "Name": str,
        "Description": str,
        "Configuration": ProfileConfigurationOutputTypeDef,
        "CreatedOn": datetime,
        "LastModifiedOn": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProfileConfigurationTypeDef = TypedDict(
    "ProfileConfigurationTypeDef",
    {
        "SessionConfiguration": NotRequired[Mapping[str, ConfigurationObjectUnionTypeDef]],
        "JobConfiguration": NotRequired[Mapping[str, ConfigurationObjectTypeDef]],
    },
)
EvaluationMetricsTypeDef = TypedDict(
    "EvaluationMetricsTypeDef",
    {
        "TransformType": Literal["FIND_MATCHES"],
        "FindMatchesMetrics": NotRequired[FindMatchesMetricsTypeDef],
    },
)
CrawlerTypeDef = TypedDict(
    "CrawlerTypeDef",
    {
        "Name": NotRequired[str],
        "Role": NotRequired[str],
        "Targets": NotRequired[CrawlerTargetsOutputTypeDef],
        "DatabaseName": NotRequired[str],
        "Description": NotRequired[str],
        "Classifiers": NotRequired[List[str]],
        "RecrawlPolicy": NotRequired[RecrawlPolicyTypeDef],
        "SchemaChangePolicy": NotRequired[SchemaChangePolicyTypeDef],
        "LineageConfiguration": NotRequired[LineageConfigurationTypeDef],
        "State": NotRequired[CrawlerStateType],
        "TablePrefix": NotRequired[str],
        "Schedule": NotRequired[ScheduleTypeDef],
        "CrawlElapsedTime": NotRequired[int],
        "CreationTime": NotRequired[datetime],
        "LastUpdated": NotRequired[datetime],
        "LastCrawl": NotRequired[LastCrawlInfoTypeDef],
        "Version": NotRequired[int],
        "Configuration": NotRequired[str],
        "CrawlerSecurityConfiguration": NotRequired[str],
        "LakeFormationConfiguration": NotRequired[LakeFormationConfigurationTypeDef],
    },
)
ListDataQualityRulesetsRequestRequestTypeDef = TypedDict(
    "ListDataQualityRulesetsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filter": NotRequired[DataQualityRulesetFilterCriteriaTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
ListDataQualityRulesetsResponseTypeDef = TypedDict(
    "ListDataQualityRulesetsResponseTypeDef",
    {
        "Rulesets": List[DataQualityRulesetListDetailsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateSessionResponseTypeDef = TypedDict(
    "CreateSessionResponseTypeDef",
    {
        "Session": SessionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSessionResponseTypeDef = TypedDict(
    "GetSessionResponseTypeDef",
    {
        "Session": SessionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSessionsResponseTypeDef = TypedDict(
    "ListSessionsResponseTypeDef",
    {
        "Ids": List[str],
        "Sessions": List[SessionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
EvaluateDataQualityMultiFrameUnionTypeDef = Union[
    EvaluateDataQualityMultiFrameTypeDef, EvaluateDataQualityMultiFrameOutputTypeDef
]
EvaluateDataQualityUnionTypeDef = Union[
    EvaluateDataQualityTypeDef, EvaluateDataQualityOutputTypeDef
]
GetDataCatalogEncryptionSettingsResponseTypeDef = TypedDict(
    "GetDataCatalogEncryptionSettingsResponseTypeDef",
    {
        "DataCatalogEncryptionSettings": DataCatalogEncryptionSettingsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutDataCatalogEncryptionSettingsRequestRequestTypeDef = TypedDict(
    "PutDataCatalogEncryptionSettingsRequestRequestTypeDef",
    {
        "DataCatalogEncryptionSettings": DataCatalogEncryptionSettingsTypeDef,
        "CatalogId": NotRequired[str],
    },
)
DatabaseTypeDef = TypedDict(
    "DatabaseTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "LocationUri": NotRequired[str],
        "Parameters": NotRequired[Dict[str, str]],
        "CreateTime": NotRequired[datetime],
        "CreateTableDefaultPermissions": NotRequired[List[PrincipalPermissionsOutputTypeDef]],
        "TargetDatabase": NotRequired[DatabaseIdentifierTypeDef],
        "CatalogId": NotRequired[str],
        "FederatedDatabase": NotRequired[FederatedDatabaseTypeDef],
    },
)
PrincipalPermissionsUnionTypeDef = Union[
    PrincipalPermissionsTypeDef, PrincipalPermissionsOutputTypeDef
]
DataQualityObservationTypeDef = TypedDict(
    "DataQualityObservationTypeDef",
    {
        "Description": NotRequired[str],
        "MetricBasedObservation": NotRequired[MetricBasedObservationTypeDef],
    },
)
DataQualityResultDescriptionTypeDef = TypedDict(
    "DataQualityResultDescriptionTypeDef",
    {
        "ResultId": NotRequired[str],
        "DataSource": NotRequired[DataSourceOutputTypeDef],
        "JobName": NotRequired[str],
        "JobRunId": NotRequired[str],
        "StartedOn": NotRequired[datetime],
    },
)
DataQualityRuleRecommendationRunDescriptionTypeDef = TypedDict(
    "DataQualityRuleRecommendationRunDescriptionTypeDef",
    {
        "RunId": NotRequired[str],
        "Status": NotRequired[TaskStatusTypeType],
        "StartedOn": NotRequired[datetime],
        "DataSource": NotRequired[DataSourceOutputTypeDef],
    },
)
DataQualityRulesetEvaluationRunDescriptionTypeDef = TypedDict(
    "DataQualityRulesetEvaluationRunDescriptionTypeDef",
    {
        "RunId": NotRequired[str],
        "Status": NotRequired[TaskStatusTypeType],
        "StartedOn": NotRequired[datetime],
        "DataSource": NotRequired[DataSourceOutputTypeDef],
    },
)
GetDataQualityRuleRecommendationRunResponseTypeDef = TypedDict(
    "GetDataQualityRuleRecommendationRunResponseTypeDef",
    {
        "RunId": str,
        "DataSource": DataSourceOutputTypeDef,
        "Role": str,
        "NumberOfWorkers": int,
        "Timeout": int,
        "Status": TaskStatusTypeType,
        "ErrorString": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "ExecutionTime": int,
        "RecommendedRuleset": str,
        "CreatedRulesetName": str,
        "DataQualitySecurityConfiguration": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDataQualityRulesetEvaluationRunResponseTypeDef = TypedDict(
    "GetDataQualityRulesetEvaluationRunResponseTypeDef",
    {
        "RunId": str,
        "DataSource": DataSourceOutputTypeDef,
        "Role": str,
        "NumberOfWorkers": int,
        "Timeout": int,
        "AdditionalRunOptions": DataQualityEvaluationRunAdditionalRunOptionsTypeDef,
        "Status": TaskStatusTypeType,
        "ErrorString": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "ExecutionTime": int,
        "RulesetNames": List[str],
        "ResultIds": List[str],
        "AdditionalDataSources": Dict[str, DataSourceOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DropNullFieldsOutputTypeDef = TypedDict(
    "DropNullFieldsOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "NullCheckBoxList": NotRequired[NullCheckBoxListTypeDef],
        "NullTextList": NotRequired[List[NullValueFieldTypeDef]],
    },
)
DropNullFieldsTypeDef = TypedDict(
    "DropNullFieldsTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "NullCheckBoxList": NotRequired[NullCheckBoxListTypeDef],
        "NullTextList": NotRequired[Sequence[NullValueFieldTypeDef]],
    },
)
ColumnStatisticsDataOutputTypeDef = TypedDict(
    "ColumnStatisticsDataOutputTypeDef",
    {
        "Type": ColumnStatisticsTypeType,
        "BooleanColumnStatisticsData": NotRequired[BooleanColumnStatisticsDataTypeDef],
        "DateColumnStatisticsData": NotRequired[DateColumnStatisticsDataOutputTypeDef],
        "DecimalColumnStatisticsData": NotRequired[DecimalColumnStatisticsDataOutputTypeDef],
        "DoubleColumnStatisticsData": NotRequired[DoubleColumnStatisticsDataTypeDef],
        "LongColumnStatisticsData": NotRequired[LongColumnStatisticsDataTypeDef],
        "StringColumnStatisticsData": NotRequired[StringColumnStatisticsDataTypeDef],
        "BinaryColumnStatisticsData": NotRequired[BinaryColumnStatisticsDataTypeDef],
    },
)
StorageDescriptorOutputTypeDef = TypedDict(
    "StorageDescriptorOutputTypeDef",
    {
        "Columns": NotRequired[List[ColumnOutputTypeDef]],
        "Location": NotRequired[str],
        "AdditionalLocations": NotRequired[List[str]],
        "InputFormat": NotRequired[str],
        "OutputFormat": NotRequired[str],
        "Compressed": NotRequired[bool],
        "NumberOfBuckets": NotRequired[int],
        "SerdeInfo": NotRequired[SerDeInfoOutputTypeDef],
        "BucketColumns": NotRequired[List[str]],
        "SortColumns": NotRequired[List[OrderTypeDef]],
        "Parameters": NotRequired[Dict[str, str]],
        "SkewedInfo": NotRequired[SkewedInfoOutputTypeDef],
        "StoredAsSubDirectories": NotRequired[bool],
        "SchemaReference": NotRequired[SchemaReferenceTypeDef],
    },
)
S3DeltaDirectTargetUnionTypeDef = Union[
    S3DeltaDirectTargetTypeDef, S3DeltaDirectTargetOutputTypeDef
]
S3DirectTargetUnionTypeDef = Union[S3DirectTargetTypeDef, S3DirectTargetOutputTypeDef]
S3GlueParquetTargetUnionTypeDef = Union[
    S3GlueParquetTargetTypeDef, S3GlueParquetTargetOutputTypeDef
]
S3HudiDirectTargetUnionTypeDef = Union[S3HudiDirectTargetTypeDef, S3HudiDirectTargetOutputTypeDef]
SecurityConfigurationTypeDef = TypedDict(
    "SecurityConfigurationTypeDef",
    {
        "Name": NotRequired[str],
        "CreatedTimeStamp": NotRequired[datetime],
        "EncryptionConfiguration": NotRequired[EncryptionConfigurationOutputTypeDef],
    },
)
CreateSecurityConfigurationRequestRequestTypeDef = TypedDict(
    "CreateSecurityConfigurationRequestRequestTypeDef",
    {
        "Name": str,
        "EncryptionConfiguration": EncryptionConfigurationTypeDef,
    },
)
DeleteSchemaVersionsResponseTypeDef = TypedDict(
    "DeleteSchemaVersionsResponseTypeDef",
    {
        "SchemaVersionErrors": List[SchemaVersionErrorItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FilterOutputTypeDef = TypedDict(
    "FilterOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "LogicalOperator": FilterLogicalOperatorType,
        "Filters": List[FilterExpressionOutputTypeDef],
    },
)
FilterExpressionTypeDef = TypedDict(
    "FilterExpressionTypeDef",
    {
        "Operation": FilterOperationType,
        "Values": Sequence[FilterValueUnionTypeDef],
        "Negated": NotRequired[bool],
    },
)
UpdateMLTransformRequestRequestTypeDef = TypedDict(
    "UpdateMLTransformRequestRequestTypeDef",
    {
        "TransformId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Parameters": NotRequired[TransformParametersTypeDef],
        "Role": NotRequired[str],
        "GlueVersion": NotRequired[str],
        "MaxCapacity": NotRequired[float],
        "WorkerType": NotRequired[WorkerTypeType],
        "NumberOfWorkers": NotRequired[int],
        "Timeout": NotRequired[int],
        "MaxRetries": NotRequired[int],
    },
)
GetMLTransformsRequestRequestTypeDef = TypedDict(
    "GetMLTransformsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filter": NotRequired[TransformFilterCriteriaTypeDef],
        "Sort": NotRequired[TransformSortCriteriaTypeDef],
    },
)
ListMLTransformsRequestRequestTypeDef = TypedDict(
    "ListMLTransformsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filter": NotRequired[TransformFilterCriteriaTypeDef],
        "Sort": NotRequired[TransformSortCriteriaTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
AthenaConnectorSourceOutputTypeDef = TypedDict(
    "AthenaConnectorSourceOutputTypeDef",
    {
        "Name": str,
        "ConnectionName": str,
        "ConnectorName": str,
        "ConnectionType": str,
        "SchemaName": str,
        "ConnectionTable": NotRequired[str],
        "OutputSchemas": NotRequired[List[GlueSchemaOutputTypeDef]],
    },
)
CatalogDeltaSourceOutputTypeDef = TypedDict(
    "CatalogDeltaSourceOutputTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
        "AdditionalDeltaOptions": NotRequired[Dict[str, str]],
        "OutputSchemas": NotRequired[List[GlueSchemaOutputTypeDef]],
    },
)
CatalogHudiSourceOutputTypeDef = TypedDict(
    "CatalogHudiSourceOutputTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
        "AdditionalHudiOptions": NotRequired[Dict[str, str]],
        "OutputSchemas": NotRequired[List[GlueSchemaOutputTypeDef]],
    },
)
ConnectorDataSourceOutputTypeDef = TypedDict(
    "ConnectorDataSourceOutputTypeDef",
    {
        "Name": str,
        "ConnectionType": str,
        "Data": Dict[str, str],
        "OutputSchemas": NotRequired[List[GlueSchemaOutputTypeDef]],
    },
)
CustomCodeOutputTypeDef = TypedDict(
    "CustomCodeOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Code": str,
        "ClassName": str,
        "OutputSchemas": NotRequired[List[GlueSchemaOutputTypeDef]],
    },
)
DynamicTransformOutputTypeDef = TypedDict(
    "DynamicTransformOutputTypeDef",
    {
        "Name": str,
        "TransformName": str,
        "Inputs": List[str],
        "FunctionName": str,
        "Path": str,
        "Parameters": NotRequired[List[TransformConfigParameterOutputTypeDef]],
        "Version": NotRequired[str],
        "OutputSchemas": NotRequired[List[GlueSchemaOutputTypeDef]],
    },
)
JDBCConnectorSourceOutputTypeDef = TypedDict(
    "JDBCConnectorSourceOutputTypeDef",
    {
        "Name": str,
        "ConnectionName": str,
        "ConnectorName": str,
        "ConnectionType": str,
        "AdditionalOptions": NotRequired[JDBCConnectorOptionsOutputTypeDef],
        "ConnectionTable": NotRequired[str],
        "Query": NotRequired[str],
        "OutputSchemas": NotRequired[List[GlueSchemaOutputTypeDef]],
    },
)
JDBCConnectorTargetOutputTypeDef = TypedDict(
    "JDBCConnectorTargetOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "ConnectionName": str,
        "ConnectionTable": str,
        "ConnectorName": str,
        "ConnectionType": str,
        "AdditionalOptions": NotRequired[Dict[str, str]],
        "OutputSchemas": NotRequired[List[GlueSchemaOutputTypeDef]],
    },
)
S3CatalogDeltaSourceOutputTypeDef = TypedDict(
    "S3CatalogDeltaSourceOutputTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
        "AdditionalDeltaOptions": NotRequired[Dict[str, str]],
        "OutputSchemas": NotRequired[List[GlueSchemaOutputTypeDef]],
    },
)
S3CatalogHudiSourceOutputTypeDef = TypedDict(
    "S3CatalogHudiSourceOutputTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
        "AdditionalHudiOptions": NotRequired[Dict[str, str]],
        "OutputSchemas": NotRequired[List[GlueSchemaOutputTypeDef]],
    },
)
S3CsvSourceOutputTypeDef = TypedDict(
    "S3CsvSourceOutputTypeDef",
    {
        "Name": str,
        "Paths": List[str],
        "Separator": SeparatorType,
        "QuoteChar": QuoteCharType,
        "CompressionType": NotRequired[CompressionTypeType],
        "Exclusions": NotRequired[List[str]],
        "GroupSize": NotRequired[str],
        "GroupFiles": NotRequired[str],
        "Recurse": NotRequired[bool],
        "MaxBand": NotRequired[int],
        "MaxFilesInBand": NotRequired[int],
        "AdditionalOptions": NotRequired[S3DirectSourceAdditionalOptionsTypeDef],
        "Escaper": NotRequired[str],
        "Multiline": NotRequired[bool],
        "WithHeader": NotRequired[bool],
        "WriteHeader": NotRequired[bool],
        "SkipFirst": NotRequired[bool],
        "OptimizePerformance": NotRequired[bool],
        "OutputSchemas": NotRequired[List[GlueSchemaOutputTypeDef]],
    },
)
S3DeltaSourceOutputTypeDef = TypedDict(
    "S3DeltaSourceOutputTypeDef",
    {
        "Name": str,
        "Paths": List[str],
        "AdditionalDeltaOptions": NotRequired[Dict[str, str]],
        "AdditionalOptions": NotRequired[S3DirectSourceAdditionalOptionsTypeDef],
        "OutputSchemas": NotRequired[List[GlueSchemaOutputTypeDef]],
    },
)
S3HudiSourceOutputTypeDef = TypedDict(
    "S3HudiSourceOutputTypeDef",
    {
        "Name": str,
        "Paths": List[str],
        "AdditionalHudiOptions": NotRequired[Dict[str, str]],
        "AdditionalOptions": NotRequired[S3DirectSourceAdditionalOptionsTypeDef],
        "OutputSchemas": NotRequired[List[GlueSchemaOutputTypeDef]],
    },
)
S3JsonSourceOutputTypeDef = TypedDict(
    "S3JsonSourceOutputTypeDef",
    {
        "Name": str,
        "Paths": List[str],
        "CompressionType": NotRequired[CompressionTypeType],
        "Exclusions": NotRequired[List[str]],
        "GroupSize": NotRequired[str],
        "GroupFiles": NotRequired[str],
        "Recurse": NotRequired[bool],
        "MaxBand": NotRequired[int],
        "MaxFilesInBand": NotRequired[int],
        "AdditionalOptions": NotRequired[S3DirectSourceAdditionalOptionsTypeDef],
        "JsonPath": NotRequired[str],
        "Multiline": NotRequired[bool],
        "OutputSchemas": NotRequired[List[GlueSchemaOutputTypeDef]],
    },
)
S3ParquetSourceOutputTypeDef = TypedDict(
    "S3ParquetSourceOutputTypeDef",
    {
        "Name": str,
        "Paths": List[str],
        "CompressionType": NotRequired[ParquetCompressionTypeType],
        "Exclusions": NotRequired[List[str]],
        "GroupSize": NotRequired[str],
        "GroupFiles": NotRequired[str],
        "Recurse": NotRequired[bool],
        "MaxBand": NotRequired[int],
        "MaxFilesInBand": NotRequired[int],
        "AdditionalOptions": NotRequired[S3DirectSourceAdditionalOptionsTypeDef],
        "OutputSchemas": NotRequired[List[GlueSchemaOutputTypeDef]],
    },
)
SnowflakeSourceOutputTypeDef = TypedDict(
    "SnowflakeSourceOutputTypeDef",
    {
        "Name": str,
        "Data": SnowflakeNodeDataOutputTypeDef,
        "OutputSchemas": NotRequired[List[GlueSchemaOutputTypeDef]],
    },
)
SparkConnectorSourceOutputTypeDef = TypedDict(
    "SparkConnectorSourceOutputTypeDef",
    {
        "Name": str,
        "ConnectionName": str,
        "ConnectorName": str,
        "ConnectionType": str,
        "AdditionalOptions": NotRequired[Dict[str, str]],
        "OutputSchemas": NotRequired[List[GlueSchemaOutputTypeDef]],
    },
)
SparkConnectorTargetOutputTypeDef = TypedDict(
    "SparkConnectorTargetOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "ConnectionName": str,
        "ConnectorName": str,
        "ConnectionType": str,
        "AdditionalOptions": NotRequired[Dict[str, str]],
        "OutputSchemas": NotRequired[List[GlueSchemaOutputTypeDef]],
    },
)
SparkSQLOutputTypeDef = TypedDict(
    "SparkSQLOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "SqlQuery": str,
        "SqlAliases": List[SqlAliasTypeDef],
        "OutputSchemas": NotRequired[List[GlueSchemaOutputTypeDef]],
    },
)
CatalogDeltaSourceTypeDef = TypedDict(
    "CatalogDeltaSourceTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
        "AdditionalDeltaOptions": NotRequired[Mapping[str, str]],
        "OutputSchemas": NotRequired[Sequence[GlueSchemaTypeDef]],
    },
)
CatalogHudiSourceTypeDef = TypedDict(
    "CatalogHudiSourceTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
        "AdditionalHudiOptions": NotRequired[Mapping[str, str]],
        "OutputSchemas": NotRequired[Sequence[GlueSchemaTypeDef]],
    },
)
ConnectorDataSourceTypeDef = TypedDict(
    "ConnectorDataSourceTypeDef",
    {
        "Name": str,
        "ConnectionType": str,
        "Data": Mapping[str, str],
        "OutputSchemas": NotRequired[Sequence[GlueSchemaTypeDef]],
    },
)
CustomCodeTypeDef = TypedDict(
    "CustomCodeTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "Code": str,
        "ClassName": str,
        "OutputSchemas": NotRequired[Sequence[GlueSchemaTypeDef]],
    },
)
GlueSchemaUnionTypeDef = Union[GlueSchemaTypeDef, GlueSchemaOutputTypeDef]
JDBCConnectorTargetTypeDef = TypedDict(
    "JDBCConnectorTargetTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "ConnectionName": str,
        "ConnectionTable": str,
        "ConnectorName": str,
        "ConnectionType": str,
        "AdditionalOptions": NotRequired[Mapping[str, str]],
        "OutputSchemas": NotRequired[Sequence[GlueSchemaTypeDef]],
    },
)
S3CatalogDeltaSourceTypeDef = TypedDict(
    "S3CatalogDeltaSourceTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
        "AdditionalDeltaOptions": NotRequired[Mapping[str, str]],
        "OutputSchemas": NotRequired[Sequence[GlueSchemaTypeDef]],
    },
)
S3CatalogHudiSourceTypeDef = TypedDict(
    "S3CatalogHudiSourceTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
        "AdditionalHudiOptions": NotRequired[Mapping[str, str]],
        "OutputSchemas": NotRequired[Sequence[GlueSchemaTypeDef]],
    },
)
S3CsvSourceTypeDef = TypedDict(
    "S3CsvSourceTypeDef",
    {
        "Name": str,
        "Paths": Sequence[str],
        "Separator": SeparatorType,
        "QuoteChar": QuoteCharType,
        "CompressionType": NotRequired[CompressionTypeType],
        "Exclusions": NotRequired[Sequence[str]],
        "GroupSize": NotRequired[str],
        "GroupFiles": NotRequired[str],
        "Recurse": NotRequired[bool],
        "MaxBand": NotRequired[int],
        "MaxFilesInBand": NotRequired[int],
        "AdditionalOptions": NotRequired[S3DirectSourceAdditionalOptionsTypeDef],
        "Escaper": NotRequired[str],
        "Multiline": NotRequired[bool],
        "WithHeader": NotRequired[bool],
        "WriteHeader": NotRequired[bool],
        "SkipFirst": NotRequired[bool],
        "OptimizePerformance": NotRequired[bool],
        "OutputSchemas": NotRequired[Sequence[GlueSchemaTypeDef]],
    },
)
S3DeltaSourceTypeDef = TypedDict(
    "S3DeltaSourceTypeDef",
    {
        "Name": str,
        "Paths": Sequence[str],
        "AdditionalDeltaOptions": NotRequired[Mapping[str, str]],
        "AdditionalOptions": NotRequired[S3DirectSourceAdditionalOptionsTypeDef],
        "OutputSchemas": NotRequired[Sequence[GlueSchemaTypeDef]],
    },
)
S3HudiSourceTypeDef = TypedDict(
    "S3HudiSourceTypeDef",
    {
        "Name": str,
        "Paths": Sequence[str],
        "AdditionalHudiOptions": NotRequired[Mapping[str, str]],
        "AdditionalOptions": NotRequired[S3DirectSourceAdditionalOptionsTypeDef],
        "OutputSchemas": NotRequired[Sequence[GlueSchemaTypeDef]],
    },
)
S3JsonSourceTypeDef = TypedDict(
    "S3JsonSourceTypeDef",
    {
        "Name": str,
        "Paths": Sequence[str],
        "CompressionType": NotRequired[CompressionTypeType],
        "Exclusions": NotRequired[Sequence[str]],
        "GroupSize": NotRequired[str],
        "GroupFiles": NotRequired[str],
        "Recurse": NotRequired[bool],
        "MaxBand": NotRequired[int],
        "MaxFilesInBand": NotRequired[int],
        "AdditionalOptions": NotRequired[S3DirectSourceAdditionalOptionsTypeDef],
        "JsonPath": NotRequired[str],
        "Multiline": NotRequired[bool],
        "OutputSchemas": NotRequired[Sequence[GlueSchemaTypeDef]],
    },
)
S3ParquetSourceTypeDef = TypedDict(
    "S3ParquetSourceTypeDef",
    {
        "Name": str,
        "Paths": Sequence[str],
        "CompressionType": NotRequired[ParquetCompressionTypeType],
        "Exclusions": NotRequired[Sequence[str]],
        "GroupSize": NotRequired[str],
        "GroupFiles": NotRequired[str],
        "Recurse": NotRequired[bool],
        "MaxBand": NotRequired[int],
        "MaxFilesInBand": NotRequired[int],
        "AdditionalOptions": NotRequired[S3DirectSourceAdditionalOptionsTypeDef],
        "OutputSchemas": NotRequired[Sequence[GlueSchemaTypeDef]],
    },
)
SparkConnectorSourceTypeDef = TypedDict(
    "SparkConnectorSourceTypeDef",
    {
        "Name": str,
        "ConnectionName": str,
        "ConnectorName": str,
        "ConnectionType": str,
        "AdditionalOptions": NotRequired[Mapping[str, str]],
        "OutputSchemas": NotRequired[Sequence[GlueSchemaTypeDef]],
    },
)
SparkConnectorTargetTypeDef = TypedDict(
    "SparkConnectorTargetTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "ConnectionName": str,
        "ConnectorName": str,
        "ConnectionType": str,
        "AdditionalOptions": NotRequired[Mapping[str, str]],
        "OutputSchemas": NotRequired[Sequence[GlueSchemaTypeDef]],
    },
)
SparkSQLTypeDef = TypedDict(
    "SparkSQLTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "SqlQuery": str,
        "SqlAliases": Sequence[SqlAliasTypeDef],
        "OutputSchemas": NotRequired[Sequence[GlueSchemaTypeDef]],
    },
)
DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "GlueTable": GlueTableUnionTypeDef,
    },
)
TableOptimizerConfigurationTypeDef = TypedDict(
    "TableOptimizerConfigurationTypeDef",
    {
        "roleArn": NotRequired[str],
        "enabled": NotRequired[bool],
        "retentionConfiguration": NotRequired[RetentionConfigurationTypeDef],
        "orphanFileDeletionConfiguration": NotRequired[OrphanFileDeletionConfigurationTypeDef],
    },
)
TableOptimizerRunTypeDef = TypedDict(
    "TableOptimizerRunTypeDef",
    {
        "eventType": NotRequired[TableOptimizerEventTypeType],
        "startTimestamp": NotRequired[datetime],
        "endTimestamp": NotRequired[datetime],
        "metrics": NotRequired[RunMetricsTypeDef],
        "error": NotRequired[str],
        "compactionMetrics": NotRequired[CompactionMetricsTypeDef],
        "retentionMetrics": NotRequired[RetentionMetricsTypeDef],
        "orphanFileDeletionMetrics": NotRequired[OrphanFileDeletionMetricsTypeDef],
    },
)
GetJobRunResponseTypeDef = TypedDict(
    "GetJobRunResponseTypeDef",
    {
        "JobRun": JobRunTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetJobRunsResponseTypeDef = TypedDict(
    "GetJobRunsResponseTypeDef",
    {
        "JobRuns": List[JobRunTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
JobNodeDetailsTypeDef = TypedDict(
    "JobNodeDetailsTypeDef",
    {
        "JobRuns": NotRequired[List[JobRunTypeDef]],
    },
)
JoinTypeDef = TypedDict(
    "JoinTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "JoinType": JoinTypeType,
        "Columns": Sequence[JoinColumnUnionTypeDef],
    },
)
GetMLTaskRunResponseTypeDef = TypedDict(
    "GetMLTaskRunResponseTypeDef",
    {
        "TransformId": str,
        "TaskRunId": str,
        "Status": TaskStatusTypeType,
        "LogGroupName": str,
        "Properties": TaskRunPropertiesTypeDef,
        "ErrorString": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "ExecutionTime": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TaskRunTypeDef = TypedDict(
    "TaskRunTypeDef",
    {
        "TransformId": NotRequired[str],
        "TaskRunId": NotRequired[str],
        "Status": NotRequired[TaskStatusTypeType],
        "LogGroupName": NotRequired[str],
        "Properties": NotRequired[TaskRunPropertiesTypeDef],
        "ErrorString": NotRequired[str],
        "StartedOn": NotRequired[datetime],
        "LastModifiedOn": NotRequired[datetime],
        "CompletedOn": NotRequired[datetime],
        "ExecutionTime": NotRequired[int],
    },
)
CreateMLTransformRequestRequestTypeDef = TypedDict(
    "CreateMLTransformRequestRequestTypeDef",
    {
        "Name": str,
        "InputRecordTables": Sequence[GlueTableUnionTypeDef],
        "Parameters": TransformParametersTypeDef,
        "Role": str,
        "Description": NotRequired[str],
        "GlueVersion": NotRequired[str],
        "MaxCapacity": NotRequired[float],
        "WorkerType": NotRequired[WorkerTypeType],
        "NumberOfWorkers": NotRequired[int],
        "Timeout": NotRequired[int],
        "MaxRetries": NotRequired[int],
        "Tags": NotRequired[Mapping[str, str]],
        "TransformEncryption": NotRequired[TransformEncryptionTypeDef],
    },
)
ApplyMappingTypeDef = TypedDict(
    "ApplyMappingTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "Mapping": Sequence[MappingUnionTypeDef],
    },
)
QuerySchemaVersionMetadataResponseTypeDef = TypedDict(
    "QuerySchemaVersionMetadataResponseTypeDef",
    {
        "MetadataInfoMap": Dict[str, MetadataInfoTypeDef],
        "SchemaVersionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
AuthenticationConfigurationInputTypeDef = TypedDict(
    "AuthenticationConfigurationInputTypeDef",
    {
        "AuthenticationType": NotRequired[AuthenticationTypeType],
        "OAuth2Properties": NotRequired[OAuth2PropertiesInputTypeDef],
        "SecretArn": NotRequired[str],
    },
)
AuthenticationConfigurationTypeDef = TypedDict(
    "AuthenticationConfigurationTypeDef",
    {
        "AuthenticationType": NotRequired[AuthenticationTypeType],
        "SecretArn": NotRequired[str],
        "OAuth2Properties": NotRequired[OAuth2PropertiesTypeDef],
    },
)
RecipeOutputTypeDef = TypedDict(
    "RecipeOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "RecipeReference": NotRequired[RecipeReferenceTypeDef],
        "RecipeSteps": NotRequired[List[RecipeStepOutputTypeDef]],
    },
)
RecipeStepTypeDef = TypedDict(
    "RecipeStepTypeDef",
    {
        "Action": RecipeActionUnionTypeDef,
        "ConditionExpressions": NotRequired[Sequence[ConditionExpressionTypeDef]],
    },
)
CreateUserDefinedFunctionRequestRequestTypeDef = TypedDict(
    "CreateUserDefinedFunctionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "FunctionInput": UserDefinedFunctionInputTypeDef,
        "CatalogId": NotRequired[str],
    },
)
UpdateUserDefinedFunctionRequestRequestTypeDef = TypedDict(
    "UpdateUserDefinedFunctionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "FunctionName": str,
        "FunctionInput": UserDefinedFunctionInputTypeDef,
        "CatalogId": NotRequired[str],
    },
)
GetUserDefinedFunctionResponseTypeDef = TypedDict(
    "GetUserDefinedFunctionResponseTypeDef",
    {
        "UserDefinedFunction": UserDefinedFunctionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetUserDefinedFunctionsResponseTypeDef = TypedDict(
    "GetUserDefinedFunctionsResponseTypeDef",
    {
        "UserDefinedFunctions": List[UserDefinedFunctionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CrawlerTargetsTypeDef = TypedDict(
    "CrawlerTargetsTypeDef",
    {
        "S3Targets": NotRequired[Sequence[S3TargetUnionTypeDef]],
        "JdbcTargets": NotRequired[Sequence[JdbcTargetUnionTypeDef]],
        "MongoDBTargets": NotRequired[Sequence[MongoDBTargetTypeDef]],
        "DynamoDBTargets": NotRequired[Sequence[DynamoDBTargetTypeDef]],
        "CatalogTargets": NotRequired[Sequence[CatalogTargetUnionTypeDef]],
        "DeltaTargets": NotRequired[Sequence[DeltaTargetUnionTypeDef]],
        "IcebergTargets": NotRequired[Sequence[IcebergTargetUnionTypeDef]],
        "HudiTargets": NotRequired[Sequence[HudiTargetUnionTypeDef]],
    },
)
StorageDescriptorTypeDef = TypedDict(
    "StorageDescriptorTypeDef",
    {
        "Columns": NotRequired[Sequence[ColumnUnionTypeDef]],
        "Location": NotRequired[str],
        "AdditionalLocations": NotRequired[Sequence[str]],
        "InputFormat": NotRequired[str],
        "OutputFormat": NotRequired[str],
        "Compressed": NotRequired[bool],
        "NumberOfBuckets": NotRequired[int],
        "SerdeInfo": NotRequired[SerDeInfoUnionTypeDef],
        "BucketColumns": NotRequired[Sequence[str]],
        "SortColumns": NotRequired[Sequence[OrderTypeDef]],
        "Parameters": NotRequired[Mapping[str, str]],
        "SkewedInfo": NotRequired[SkewedInfoUnionTypeDef],
        "StoredAsSubDirectories": NotRequired[bool],
        "SchemaReference": NotRequired[SchemaReferenceTypeDef],
    },
)
StatementTypeDef = TypedDict(
    "StatementTypeDef",
    {
        "Id": NotRequired[int],
        "Code": NotRequired[str],
        "State": NotRequired[StatementStateType],
        "Output": NotRequired[StatementOutputTypeDef],
        "Progress": NotRequired[float],
        "StartedOn": NotRequired[int],
        "CompletedOn": NotRequired[int],
    },
)
ListDataQualityStatisticAnnotationsResponseTypeDef = TypedDict(
    "ListDataQualityStatisticAnnotationsResponseTypeDef",
    {
        "Annotations": List[StatisticAnnotationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListDataQualityStatisticsResponseTypeDef = TypedDict(
    "ListDataQualityStatisticsResponseTypeDef",
    {
        "Statistics": List[StatisticSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DynamicTransformTypeDef = TypedDict(
    "DynamicTransformTypeDef",
    {
        "Name": str,
        "TransformName": str,
        "Inputs": Sequence[str],
        "FunctionName": str,
        "Path": str,
        "Parameters": NotRequired[Sequence[TransformConfigParameterUnionTypeDef]],
        "Version": NotRequired[str],
        "OutputSchemas": NotRequired[Sequence[GlueSchemaTypeDef]],
    },
)
RedshiftTargetTypeDef = TypedDict(
    "RedshiftTargetTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "Database": str,
        "Table": str,
        "RedshiftTmpDir": NotRequired[str],
        "TmpDirIAMRole": NotRequired[str],
        "UpsertRedshiftOptions": NotRequired[UpsertRedshiftTargetOptionsUnionTypeDef],
    },
)
CreateTriggerRequestRequestTypeDef = TypedDict(
    "CreateTriggerRequestRequestTypeDef",
    {
        "Name": str,
        "Type": TriggerTypeType,
        "Actions": Sequence[ActionUnionTypeDef],
        "WorkflowName": NotRequired[str],
        "Schedule": NotRequired[str],
        "Predicate": NotRequired[PredicateTypeDef],
        "Description": NotRequired[str],
        "StartOnCreation": NotRequired[bool],
        "Tags": NotRequired[Mapping[str, str]],
        "EventBatchingCondition": NotRequired[EventBatchingConditionTypeDef],
    },
)
AggregateUnionTypeDef = Union[AggregateTypeDef, AggregateOutputTypeDef]
AmazonRedshiftSourceTypeDef = TypedDict(
    "AmazonRedshiftSourceTypeDef",
    {
        "Name": NotRequired[str],
        "Data": NotRequired[AmazonRedshiftNodeDataUnionTypeDef],
    },
)
AmazonRedshiftTargetTypeDef = TypedDict(
    "AmazonRedshiftTargetTypeDef",
    {
        "Name": NotRequired[str],
        "Data": NotRequired[AmazonRedshiftNodeDataUnionTypeDef],
        "Inputs": NotRequired[Sequence[str]],
    },
)
SnowflakeSourceTypeDef = TypedDict(
    "SnowflakeSourceTypeDef",
    {
        "Name": str,
        "Data": SnowflakeNodeDataUnionTypeDef,
        "OutputSchemas": NotRequired[Sequence[GlueSchemaTypeDef]],
    },
)
SnowflakeTargetTypeDef = TypedDict(
    "SnowflakeTargetTypeDef",
    {
        "Name": str,
        "Data": SnowflakeNodeDataUnionTypeDef,
        "Inputs": NotRequired[Sequence[str]],
    },
)
GetPartitionIndexesResponseTypeDef = TypedDict(
    "GetPartitionIndexesResponseTypeDef",
    {
        "PartitionIndexDescriptorList": List[PartitionIndexDescriptorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
TableStatusPaginatorTypeDef = TypedDict(
    "TableStatusPaginatorTypeDef",
    {
        "RequestedBy": NotRequired[str],
        "UpdatedBy": NotRequired[str],
        "RequestTime": NotRequired[datetime],
        "UpdateTime": NotRequired[datetime],
        "Action": NotRequired[ResourceActionType],
        "State": NotRequired[ResourceStateType],
        "Error": NotRequired[ErrorDetailTypeDef],
        "Details": NotRequired[StatusDetailsPaginatorTypeDef],
    },
)
TableStatusTypeDef = TypedDict(
    "TableStatusTypeDef",
    {
        "RequestedBy": NotRequired[str],
        "UpdatedBy": NotRequired[str],
        "RequestTime": NotRequired[datetime],
        "UpdateTime": NotRequired[datetime],
        "Action": NotRequired[ResourceActionType],
        "State": NotRequired[ResourceStateType],
        "Error": NotRequired[ErrorDetailTypeDef],
        "Details": NotRequired[StatusDetailsTypeDef],
    },
)
DecimalColumnStatisticsDataTypeDef = TypedDict(
    "DecimalColumnStatisticsDataTypeDef",
    {
        "NumberOfNulls": int,
        "NumberOfDistinctValues": int,
        "MinimumValue": NotRequired[DecimalNumberUnionTypeDef],
        "MaximumValue": NotRequired[DecimalNumberUnionTypeDef],
    },
)
CreateScriptRequestRequestTypeDef = TypedDict(
    "CreateScriptRequestRequestTypeDef",
    {
        "DagNodes": NotRequired[Sequence[CodeGenNodeUnionTypeDef]],
        "DagEdges": NotRequired[Sequence[CodeGenEdgeTypeDef]],
        "Language": NotRequired[LanguageType],
    },
)
CatalogKafkaSourceTypeDef = TypedDict(
    "CatalogKafkaSourceTypeDef",
    {
        "Name": str,
        "Table": str,
        "Database": str,
        "WindowSize": NotRequired[int],
        "DetectSchema": NotRequired[bool],
        "StreamingOptions": NotRequired[KafkaStreamingSourceOptionsUnionTypeDef],
        "DataPreviewOptions": NotRequired[StreamingDataPreviewOptionsTypeDef],
    },
)
DirectKafkaSourceTypeDef = TypedDict(
    "DirectKafkaSourceTypeDef",
    {
        "Name": str,
        "StreamingOptions": NotRequired[KafkaStreamingSourceOptionsUnionTypeDef],
        "WindowSize": NotRequired[int],
        "DetectSchema": NotRequired[bool],
        "DataPreviewOptions": NotRequired[StreamingDataPreviewOptionsTypeDef],
    },
)
CatalogKinesisSourceTypeDef = TypedDict(
    "CatalogKinesisSourceTypeDef",
    {
        "Name": str,
        "Table": str,
        "Database": str,
        "WindowSize": NotRequired[int],
        "DetectSchema": NotRequired[bool],
        "StreamingOptions": NotRequired[KinesisStreamingSourceOptionsUnionTypeDef],
        "DataPreviewOptions": NotRequired[StreamingDataPreviewOptionsTypeDef],
    },
)
DirectKinesisSourceTypeDef = TypedDict(
    "DirectKinesisSourceTypeDef",
    {
        "Name": str,
        "WindowSize": NotRequired[int],
        "DetectSchema": NotRequired[bool],
        "StreamingOptions": NotRequired[KinesisStreamingSourceOptionsUnionTypeDef],
        "DataPreviewOptions": NotRequired[StreamingDataPreviewOptionsTypeDef],
    },
)
BatchGetTriggersResponseTypeDef = TypedDict(
    "BatchGetTriggersResponseTypeDef",
    {
        "Triggers": List[TriggerTypeDef],
        "TriggersNotFound": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTriggerResponseTypeDef = TypedDict(
    "GetTriggerResponseTypeDef",
    {
        "Trigger": TriggerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTriggersResponseTypeDef = TypedDict(
    "GetTriggersResponseTypeDef",
    {
        "Triggers": List[TriggerTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
TriggerNodeDetailsTypeDef = TypedDict(
    "TriggerNodeDetailsTypeDef",
    {
        "Trigger": NotRequired[TriggerTypeDef],
    },
)
UpdateTriggerResponseTypeDef = TypedDict(
    "UpdateTriggerResponseTypeDef",
    {
        "Trigger": TriggerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TriggerUpdateTypeDef = TypedDict(
    "TriggerUpdateTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Schedule": NotRequired[str],
        "Actions": NotRequired[Sequence[ActionUnionTypeDef]],
        "Predicate": NotRequired[PredicateUnionTypeDef],
        "EventBatchingCondition": NotRequired[EventBatchingConditionTypeDef],
    },
)
CreateUsageProfileRequestRequestTypeDef = TypedDict(
    "CreateUsageProfileRequestRequestTypeDef",
    {
        "Name": str,
        "Configuration": ProfileConfigurationTypeDef,
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
UpdateUsageProfileRequestRequestTypeDef = TypedDict(
    "UpdateUsageProfileRequestRequestTypeDef",
    {
        "Name": str,
        "Configuration": ProfileConfigurationTypeDef,
        "Description": NotRequired[str],
    },
)
GetMLTransformResponseTypeDef = TypedDict(
    "GetMLTransformResponseTypeDef",
    {
        "TransformId": str,
        "Name": str,
        "Description": str,
        "Status": TransformStatusTypeType,
        "CreatedOn": datetime,
        "LastModifiedOn": datetime,
        "InputRecordTables": List[GlueTableOutputTypeDef],
        "Parameters": TransformParametersTypeDef,
        "EvaluationMetrics": EvaluationMetricsTypeDef,
        "LabelCount": int,
        "Schema": List[SchemaColumnTypeDef],
        "Role": str,
        "GlueVersion": str,
        "MaxCapacity": float,
        "WorkerType": WorkerTypeType,
        "NumberOfWorkers": int,
        "Timeout": int,
        "MaxRetries": int,
        "TransformEncryption": TransformEncryptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MLTransformTypeDef = TypedDict(
    "MLTransformTypeDef",
    {
        "TransformId": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Status": NotRequired[TransformStatusTypeType],
        "CreatedOn": NotRequired[datetime],
        "LastModifiedOn": NotRequired[datetime],
        "InputRecordTables": NotRequired[List[GlueTableOutputTypeDef]],
        "Parameters": NotRequired[TransformParametersTypeDef],
        "EvaluationMetrics": NotRequired[EvaluationMetricsTypeDef],
        "LabelCount": NotRequired[int],
        "Schema": NotRequired[List[SchemaColumnTypeDef]],
        "Role": NotRequired[str],
        "GlueVersion": NotRequired[str],
        "MaxCapacity": NotRequired[float],
        "WorkerType": NotRequired[WorkerTypeType],
        "NumberOfWorkers": NotRequired[int],
        "Timeout": NotRequired[int],
        "MaxRetries": NotRequired[int],
        "TransformEncryption": NotRequired[TransformEncryptionTypeDef],
    },
)
BatchGetCrawlersResponseTypeDef = TypedDict(
    "BatchGetCrawlersResponseTypeDef",
    {
        "Crawlers": List[CrawlerTypeDef],
        "CrawlersNotFound": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCrawlerResponseTypeDef = TypedDict(
    "GetCrawlerResponseTypeDef",
    {
        "Crawler": CrawlerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCrawlersResponseTypeDef = TypedDict(
    "GetCrawlersResponseTypeDef",
    {
        "Crawlers": List[CrawlerTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetDatabaseResponseTypeDef = TypedDict(
    "GetDatabaseResponseTypeDef",
    {
        "Database": DatabaseTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDatabasesResponseTypeDef = TypedDict(
    "GetDatabasesResponseTypeDef",
    {
        "DatabaseList": List[DatabaseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DatabaseInputTypeDef = TypedDict(
    "DatabaseInputTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "LocationUri": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, str]],
        "CreateTableDefaultPermissions": NotRequired[Sequence[PrincipalPermissionsUnionTypeDef]],
        "TargetDatabase": NotRequired[DatabaseIdentifierTypeDef],
        "FederatedDatabase": NotRequired[FederatedDatabaseTypeDef],
    },
)
DataQualityResultTypeDef = TypedDict(
    "DataQualityResultTypeDef",
    {
        "ResultId": NotRequired[str],
        "ProfileId": NotRequired[str],
        "Score": NotRequired[float],
        "DataSource": NotRequired[DataSourceOutputTypeDef],
        "RulesetName": NotRequired[str],
        "EvaluationContext": NotRequired[str],
        "StartedOn": NotRequired[datetime],
        "CompletedOn": NotRequired[datetime],
        "JobName": NotRequired[str],
        "JobRunId": NotRequired[str],
        "RulesetEvaluationRunId": NotRequired[str],
        "RuleResults": NotRequired[List[DataQualityRuleResultTypeDef]],
        "AnalyzerResults": NotRequired[List[DataQualityAnalyzerResultTypeDef]],
        "Observations": NotRequired[List[DataQualityObservationTypeDef]],
    },
)
GetDataQualityResultResponseTypeDef = TypedDict(
    "GetDataQualityResultResponseTypeDef",
    {
        "ResultId": str,
        "ProfileId": str,
        "Score": float,
        "DataSource": DataSourceOutputTypeDef,
        "RulesetName": str,
        "EvaluationContext": str,
        "StartedOn": datetime,
        "CompletedOn": datetime,
        "JobName": str,
        "JobRunId": str,
        "RulesetEvaluationRunId": str,
        "RuleResults": List[DataQualityRuleResultTypeDef],
        "AnalyzerResults": List[DataQualityAnalyzerResultTypeDef],
        "Observations": List[DataQualityObservationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDataQualityResultsResponseTypeDef = TypedDict(
    "ListDataQualityResultsResponseTypeDef",
    {
        "Results": List[DataQualityResultDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListDataQualityRuleRecommendationRunsResponseTypeDef = TypedDict(
    "ListDataQualityRuleRecommendationRunsResponseTypeDef",
    {
        "Runs": List[DataQualityRuleRecommendationRunDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListDataQualityRulesetEvaluationRunsResponseTypeDef = TypedDict(
    "ListDataQualityRulesetEvaluationRunsResponseTypeDef",
    {
        "Runs": List[DataQualityRulesetEvaluationRunDescriptionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DropNullFieldsUnionTypeDef = Union[DropNullFieldsTypeDef, DropNullFieldsOutputTypeDef]
ColumnStatisticsOutputTypeDef = TypedDict(
    "ColumnStatisticsOutputTypeDef",
    {
        "ColumnName": str,
        "ColumnType": str,
        "AnalyzedTime": datetime,
        "StatisticsData": ColumnStatisticsDataOutputTypeDef,
    },
)
PartitionTypeDef = TypedDict(
    "PartitionTypeDef",
    {
        "Values": NotRequired[List[str]],
        "DatabaseName": NotRequired[str],
        "TableName": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastAccessTime": NotRequired[datetime],
        "StorageDescriptor": NotRequired[StorageDescriptorOutputTypeDef],
        "Parameters": NotRequired[Dict[str, str]],
        "LastAnalyzedTime": NotRequired[datetime],
        "CatalogId": NotRequired[str],
    },
)
GetSecurityConfigurationResponseTypeDef = TypedDict(
    "GetSecurityConfigurationResponseTypeDef",
    {
        "SecurityConfiguration": SecurityConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSecurityConfigurationsResponseTypeDef = TypedDict(
    "GetSecurityConfigurationsResponseTypeDef",
    {
        "SecurityConfigurations": List[SecurityConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
FilterExpressionUnionTypeDef = Union[FilterExpressionTypeDef, FilterExpressionOutputTypeDef]
CatalogDeltaSourceUnionTypeDef = Union[CatalogDeltaSourceTypeDef, CatalogDeltaSourceOutputTypeDef]
CatalogHudiSourceUnionTypeDef = Union[CatalogHudiSourceTypeDef, CatalogHudiSourceOutputTypeDef]
ConnectorDataSourceUnionTypeDef = Union[
    ConnectorDataSourceTypeDef, ConnectorDataSourceOutputTypeDef
]
CustomCodeUnionTypeDef = Union[CustomCodeTypeDef, CustomCodeOutputTypeDef]
AthenaConnectorSourceTypeDef = TypedDict(
    "AthenaConnectorSourceTypeDef",
    {
        "Name": str,
        "ConnectionName": str,
        "ConnectorName": str,
        "ConnectionType": str,
        "SchemaName": str,
        "ConnectionTable": NotRequired[str],
        "OutputSchemas": NotRequired[Sequence[GlueSchemaUnionTypeDef]],
    },
)
JDBCConnectorSourceTypeDef = TypedDict(
    "JDBCConnectorSourceTypeDef",
    {
        "Name": str,
        "ConnectionName": str,
        "ConnectorName": str,
        "ConnectionType": str,
        "AdditionalOptions": NotRequired[JDBCConnectorOptionsUnionTypeDef],
        "ConnectionTable": NotRequired[str],
        "Query": NotRequired[str],
        "OutputSchemas": NotRequired[Sequence[GlueSchemaUnionTypeDef]],
    },
)
JDBCConnectorTargetUnionTypeDef = Union[
    JDBCConnectorTargetTypeDef, JDBCConnectorTargetOutputTypeDef
]
S3CatalogDeltaSourceUnionTypeDef = Union[
    S3CatalogDeltaSourceTypeDef, S3CatalogDeltaSourceOutputTypeDef
]
S3CatalogHudiSourceUnionTypeDef = Union[
    S3CatalogHudiSourceTypeDef, S3CatalogHudiSourceOutputTypeDef
]
S3CsvSourceUnionTypeDef = Union[S3CsvSourceTypeDef, S3CsvSourceOutputTypeDef]
S3DeltaSourceUnionTypeDef = Union[S3DeltaSourceTypeDef, S3DeltaSourceOutputTypeDef]
S3HudiSourceUnionTypeDef = Union[S3HudiSourceTypeDef, S3HudiSourceOutputTypeDef]
S3JsonSourceUnionTypeDef = Union[S3JsonSourceTypeDef, S3JsonSourceOutputTypeDef]
S3ParquetSourceUnionTypeDef = Union[S3ParquetSourceTypeDef, S3ParquetSourceOutputTypeDef]
SparkConnectorSourceUnionTypeDef = Union[
    SparkConnectorSourceTypeDef, SparkConnectorSourceOutputTypeDef
]
SparkConnectorTargetUnionTypeDef = Union[
    SparkConnectorTargetTypeDef, SparkConnectorTargetOutputTypeDef
]
SparkSQLUnionTypeDef = Union[SparkSQLTypeDef, SparkSQLOutputTypeDef]
DataSourceUnionTypeDef = Union[DataSourceTypeDef, DataSourceOutputTypeDef]
StartDataQualityRuleRecommendationRunRequestRequestTypeDef = TypedDict(
    "StartDataQualityRuleRecommendationRunRequestRequestTypeDef",
    {
        "DataSource": DataSourceTypeDef,
        "Role": str,
        "NumberOfWorkers": NotRequired[int],
        "Timeout": NotRequired[int],
        "CreatedRulesetName": NotRequired[str],
        "DataQualitySecurityConfiguration": NotRequired[str],
        "ClientToken": NotRequired[str],
    },
)
CreateTableOptimizerRequestRequestTypeDef = TypedDict(
    "CreateTableOptimizerRequestRequestTypeDef",
    {
        "CatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "Type": TableOptimizerTypeType,
        "TableOptimizerConfiguration": TableOptimizerConfigurationTypeDef,
    },
)
UpdateTableOptimizerRequestRequestTypeDef = TypedDict(
    "UpdateTableOptimizerRequestRequestTypeDef",
    {
        "CatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "Type": TableOptimizerTypeType,
        "TableOptimizerConfiguration": TableOptimizerConfigurationTypeDef,
    },
)
ListTableOptimizerRunsResponseTypeDef = TypedDict(
    "ListTableOptimizerRunsResponseTypeDef",
    {
        "CatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "TableOptimizerRuns": List[TableOptimizerRunTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
TableOptimizerTypeDef = TypedDict(
    "TableOptimizerTypeDef",
    {
        "type": NotRequired[TableOptimizerTypeType],
        "configuration": NotRequired[TableOptimizerConfigurationTypeDef],
        "lastRun": NotRequired[TableOptimizerRunTypeDef],
    },
)
JoinUnionTypeDef = Union[JoinTypeDef, JoinOutputTypeDef]
GetMLTaskRunsResponseTypeDef = TypedDict(
    "GetMLTaskRunsResponseTypeDef",
    {
        "TaskRuns": List[TaskRunTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ApplyMappingUnionTypeDef = Union[ApplyMappingTypeDef, ApplyMappingOutputTypeDef]
ConnectionInputTypeDef = TypedDict(
    "ConnectionInputTypeDef",
    {
        "Name": str,
        "ConnectionType": ConnectionTypeType,
        "ConnectionProperties": Mapping[ConnectionPropertyKeyType, str],
        "Description": NotRequired[str],
        "MatchCriteria": NotRequired[Sequence[str]],
        "AthenaProperties": NotRequired[Mapping[str, str]],
        "PhysicalConnectionRequirements": NotRequired[PhysicalConnectionRequirementsUnionTypeDef],
        "AuthenticationConfiguration": NotRequired[AuthenticationConfigurationInputTypeDef],
        "ValidateCredentials": NotRequired[bool],
    },
)
TestConnectionInputTypeDef = TypedDict(
    "TestConnectionInputTypeDef",
    {
        "ConnectionType": ConnectionTypeType,
        "ConnectionProperties": Mapping[ConnectionPropertyKeyType, str],
        "AuthenticationConfiguration": NotRequired[AuthenticationConfigurationInputTypeDef],
    },
)
ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "ConnectionType": NotRequired[ConnectionTypeType],
        "MatchCriteria": NotRequired[List[str]],
        "ConnectionProperties": NotRequired[Dict[ConnectionPropertyKeyType, str]],
        "AthenaProperties": NotRequired[Dict[str, str]],
        "PhysicalConnectionRequirements": NotRequired[PhysicalConnectionRequirementsOutputTypeDef],
        "CreationTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "LastUpdatedBy": NotRequired[str],
        "Status": NotRequired[ConnectionStatusType],
        "StatusReason": NotRequired[str],
        "LastConnectionValidationTime": NotRequired[datetime],
        "AuthenticationConfiguration": NotRequired[AuthenticationConfigurationTypeDef],
    },
)
CodeGenConfigurationNodeOutputTypeDef = TypedDict(
    "CodeGenConfigurationNodeOutputTypeDef",
    {
        "AthenaConnectorSource": NotRequired[AthenaConnectorSourceOutputTypeDef],
        "JDBCConnectorSource": NotRequired[JDBCConnectorSourceOutputTypeDef],
        "SparkConnectorSource": NotRequired[SparkConnectorSourceOutputTypeDef],
        "CatalogSource": NotRequired[CatalogSourceTypeDef],
        "RedshiftSource": NotRequired[RedshiftSourceTypeDef],
        "S3CatalogSource": NotRequired[S3CatalogSourceTypeDef],
        "S3CsvSource": NotRequired[S3CsvSourceOutputTypeDef],
        "S3JsonSource": NotRequired[S3JsonSourceOutputTypeDef],
        "S3ParquetSource": NotRequired[S3ParquetSourceOutputTypeDef],
        "RelationalCatalogSource": NotRequired[RelationalCatalogSourceTypeDef],
        "DynamoDBCatalogSource": NotRequired[DynamoDBCatalogSourceTypeDef],
        "JDBCConnectorTarget": NotRequired[JDBCConnectorTargetOutputTypeDef],
        "SparkConnectorTarget": NotRequired[SparkConnectorTargetOutputTypeDef],
        "CatalogTarget": NotRequired[BasicCatalogTargetOutputTypeDef],
        "RedshiftTarget": NotRequired[RedshiftTargetOutputTypeDef],
        "S3CatalogTarget": NotRequired[S3CatalogTargetOutputTypeDef],
        "S3GlueParquetTarget": NotRequired[S3GlueParquetTargetOutputTypeDef],
        "S3DirectTarget": NotRequired[S3DirectTargetOutputTypeDef],
        "ApplyMapping": NotRequired[ApplyMappingOutputTypeDef],
        "SelectFields": NotRequired[SelectFieldsOutputTypeDef],
        "DropFields": NotRequired[DropFieldsOutputTypeDef],
        "RenameField": NotRequired[RenameFieldOutputTypeDef],
        "Spigot": NotRequired[SpigotOutputTypeDef],
        "Join": NotRequired[JoinOutputTypeDef],
        "SplitFields": NotRequired[SplitFieldsOutputTypeDef],
        "SelectFromCollection": NotRequired[SelectFromCollectionOutputTypeDef],
        "FillMissingValues": NotRequired[FillMissingValuesOutputTypeDef],
        "Filter": NotRequired[FilterOutputTypeDef],
        "CustomCode": NotRequired[CustomCodeOutputTypeDef],
        "SparkSQL": NotRequired[SparkSQLOutputTypeDef],
        "DirectKinesisSource": NotRequired[DirectKinesisSourceOutputTypeDef],
        "DirectKafkaSource": NotRequired[DirectKafkaSourceOutputTypeDef],
        "CatalogKinesisSource": NotRequired[CatalogKinesisSourceOutputTypeDef],
        "CatalogKafkaSource": NotRequired[CatalogKafkaSourceOutputTypeDef],
        "DropNullFields": NotRequired[DropNullFieldsOutputTypeDef],
        "Merge": NotRequired[MergeOutputTypeDef],
        "Union": NotRequired[UnionOutputTypeDef],
        "PIIDetection": NotRequired[PIIDetectionOutputTypeDef],
        "Aggregate": NotRequired[AggregateOutputTypeDef],
        "DropDuplicates": NotRequired[DropDuplicatesOutputTypeDef],
        "GovernedCatalogTarget": NotRequired[GovernedCatalogTargetOutputTypeDef],
        "GovernedCatalogSource": NotRequired[GovernedCatalogSourceTypeDef],
        "MicrosoftSQLServerCatalogSource": NotRequired[MicrosoftSQLServerCatalogSourceTypeDef],
        "MySQLCatalogSource": NotRequired[MySQLCatalogSourceTypeDef],
        "OracleSQLCatalogSource": NotRequired[OracleSQLCatalogSourceTypeDef],
        "PostgreSQLCatalogSource": NotRequired[PostgreSQLCatalogSourceTypeDef],
        "MicrosoftSQLServerCatalogTarget": NotRequired[
            MicrosoftSQLServerCatalogTargetOutputTypeDef
        ],
        "MySQLCatalogTarget": NotRequired[MySQLCatalogTargetOutputTypeDef],
        "OracleSQLCatalogTarget": NotRequired[OracleSQLCatalogTargetOutputTypeDef],
        "PostgreSQLCatalogTarget": NotRequired[PostgreSQLCatalogTargetOutputTypeDef],
        "DynamicTransform": NotRequired[DynamicTransformOutputTypeDef],
        "EvaluateDataQuality": NotRequired[EvaluateDataQualityOutputTypeDef],
        "S3CatalogHudiSource": NotRequired[S3CatalogHudiSourceOutputTypeDef],
        "CatalogHudiSource": NotRequired[CatalogHudiSourceOutputTypeDef],
        "S3HudiSource": NotRequired[S3HudiSourceOutputTypeDef],
        "S3HudiCatalogTarget": NotRequired[S3HudiCatalogTargetOutputTypeDef],
        "S3HudiDirectTarget": NotRequired[S3HudiDirectTargetOutputTypeDef],
        "DirectJDBCSource": NotRequired[DirectJDBCSourceTypeDef],
        "S3CatalogDeltaSource": NotRequired[S3CatalogDeltaSourceOutputTypeDef],
        "CatalogDeltaSource": NotRequired[CatalogDeltaSourceOutputTypeDef],
        "S3DeltaSource": NotRequired[S3DeltaSourceOutputTypeDef],
        "S3DeltaCatalogTarget": NotRequired[S3DeltaCatalogTargetOutputTypeDef],
        "S3DeltaDirectTarget": NotRequired[S3DeltaDirectTargetOutputTypeDef],
        "AmazonRedshiftSource": NotRequired[AmazonRedshiftSourceOutputTypeDef],
        "AmazonRedshiftTarget": NotRequired[AmazonRedshiftTargetOutputTypeDef],
        "EvaluateDataQualityMultiFrame": NotRequired[EvaluateDataQualityMultiFrameOutputTypeDef],
        "Recipe": NotRequired[RecipeOutputTypeDef],
        "SnowflakeSource": NotRequired[SnowflakeSourceOutputTypeDef],
        "SnowflakeTarget": NotRequired[SnowflakeTargetOutputTypeDef],
        "ConnectorDataSource": NotRequired[ConnectorDataSourceOutputTypeDef],
        "ConnectorDataTarget": NotRequired[ConnectorDataTargetOutputTypeDef],
    },
)
CodeGenConfigurationNodePaginatorTypeDef = TypedDict(
    "CodeGenConfigurationNodePaginatorTypeDef",
    {
        "AthenaConnectorSource": NotRequired[AthenaConnectorSourceOutputTypeDef],
        "JDBCConnectorSource": NotRequired[JDBCConnectorSourceOutputTypeDef],
        "SparkConnectorSource": NotRequired[SparkConnectorSourceOutputTypeDef],
        "CatalogSource": NotRequired[CatalogSourceTypeDef],
        "RedshiftSource": NotRequired[RedshiftSourceTypeDef],
        "S3CatalogSource": NotRequired[S3CatalogSourceTypeDef],
        "S3CsvSource": NotRequired[S3CsvSourceOutputTypeDef],
        "S3JsonSource": NotRequired[S3JsonSourceOutputTypeDef],
        "S3ParquetSource": NotRequired[S3ParquetSourceOutputTypeDef],
        "RelationalCatalogSource": NotRequired[RelationalCatalogSourceTypeDef],
        "DynamoDBCatalogSource": NotRequired[DynamoDBCatalogSourceTypeDef],
        "JDBCConnectorTarget": NotRequired[JDBCConnectorTargetOutputTypeDef],
        "SparkConnectorTarget": NotRequired[SparkConnectorTargetOutputTypeDef],
        "CatalogTarget": NotRequired[BasicCatalogTargetOutputTypeDef],
        "RedshiftTarget": NotRequired[RedshiftTargetOutputTypeDef],
        "S3CatalogTarget": NotRequired[S3CatalogTargetOutputTypeDef],
        "S3GlueParquetTarget": NotRequired[S3GlueParquetTargetOutputTypeDef],
        "S3DirectTarget": NotRequired[S3DirectTargetOutputTypeDef],
        "ApplyMapping": NotRequired[ApplyMappingPaginatorTypeDef],
        "SelectFields": NotRequired[SelectFieldsOutputTypeDef],
        "DropFields": NotRequired[DropFieldsOutputTypeDef],
        "RenameField": NotRequired[RenameFieldOutputTypeDef],
        "Spigot": NotRequired[SpigotOutputTypeDef],
        "Join": NotRequired[JoinOutputTypeDef],
        "SplitFields": NotRequired[SplitFieldsOutputTypeDef],
        "SelectFromCollection": NotRequired[SelectFromCollectionOutputTypeDef],
        "FillMissingValues": NotRequired[FillMissingValuesOutputTypeDef],
        "Filter": NotRequired[FilterOutputTypeDef],
        "CustomCode": NotRequired[CustomCodeOutputTypeDef],
        "SparkSQL": NotRequired[SparkSQLOutputTypeDef],
        "DirectKinesisSource": NotRequired[DirectKinesisSourceOutputTypeDef],
        "DirectKafkaSource": NotRequired[DirectKafkaSourceOutputTypeDef],
        "CatalogKinesisSource": NotRequired[CatalogKinesisSourceOutputTypeDef],
        "CatalogKafkaSource": NotRequired[CatalogKafkaSourceOutputTypeDef],
        "DropNullFields": NotRequired[DropNullFieldsOutputTypeDef],
        "Merge": NotRequired[MergeOutputTypeDef],
        "Union": NotRequired[UnionOutputTypeDef],
        "PIIDetection": NotRequired[PIIDetectionOutputTypeDef],
        "Aggregate": NotRequired[AggregateOutputTypeDef],
        "DropDuplicates": NotRequired[DropDuplicatesOutputTypeDef],
        "GovernedCatalogTarget": NotRequired[GovernedCatalogTargetOutputTypeDef],
        "GovernedCatalogSource": NotRequired[GovernedCatalogSourceTypeDef],
        "MicrosoftSQLServerCatalogSource": NotRequired[MicrosoftSQLServerCatalogSourceTypeDef],
        "MySQLCatalogSource": NotRequired[MySQLCatalogSourceTypeDef],
        "OracleSQLCatalogSource": NotRequired[OracleSQLCatalogSourceTypeDef],
        "PostgreSQLCatalogSource": NotRequired[PostgreSQLCatalogSourceTypeDef],
        "MicrosoftSQLServerCatalogTarget": NotRequired[
            MicrosoftSQLServerCatalogTargetOutputTypeDef
        ],
        "MySQLCatalogTarget": NotRequired[MySQLCatalogTargetOutputTypeDef],
        "OracleSQLCatalogTarget": NotRequired[OracleSQLCatalogTargetOutputTypeDef],
        "PostgreSQLCatalogTarget": NotRequired[PostgreSQLCatalogTargetOutputTypeDef],
        "DynamicTransform": NotRequired[DynamicTransformOutputTypeDef],
        "EvaluateDataQuality": NotRequired[EvaluateDataQualityOutputTypeDef],
        "S3CatalogHudiSource": NotRequired[S3CatalogHudiSourceOutputTypeDef],
        "CatalogHudiSource": NotRequired[CatalogHudiSourceOutputTypeDef],
        "S3HudiSource": NotRequired[S3HudiSourceOutputTypeDef],
        "S3HudiCatalogTarget": NotRequired[S3HudiCatalogTargetOutputTypeDef],
        "S3HudiDirectTarget": NotRequired[S3HudiDirectTargetOutputTypeDef],
        "DirectJDBCSource": NotRequired[DirectJDBCSourceTypeDef],
        "S3CatalogDeltaSource": NotRequired[S3CatalogDeltaSourceOutputTypeDef],
        "CatalogDeltaSource": NotRequired[CatalogDeltaSourceOutputTypeDef],
        "S3DeltaSource": NotRequired[S3DeltaSourceOutputTypeDef],
        "S3DeltaCatalogTarget": NotRequired[S3DeltaCatalogTargetOutputTypeDef],
        "S3DeltaDirectTarget": NotRequired[S3DeltaDirectTargetOutputTypeDef],
        "AmazonRedshiftSource": NotRequired[AmazonRedshiftSourceOutputTypeDef],
        "AmazonRedshiftTarget": NotRequired[AmazonRedshiftTargetOutputTypeDef],
        "EvaluateDataQualityMultiFrame": NotRequired[EvaluateDataQualityMultiFrameOutputTypeDef],
        "Recipe": NotRequired[RecipeOutputTypeDef],
        "SnowflakeSource": NotRequired[SnowflakeSourceOutputTypeDef],
        "SnowflakeTarget": NotRequired[SnowflakeTargetOutputTypeDef],
        "ConnectorDataSource": NotRequired[ConnectorDataSourceOutputTypeDef],
        "ConnectorDataTarget": NotRequired[ConnectorDataTargetOutputTypeDef],
    },
)
RecipeStepUnionTypeDef = Union[RecipeStepTypeDef, RecipeStepOutputTypeDef]
CreateCrawlerRequestRequestTypeDef = TypedDict(
    "CreateCrawlerRequestRequestTypeDef",
    {
        "Name": str,
        "Role": str,
        "Targets": CrawlerTargetsTypeDef,
        "DatabaseName": NotRequired[str],
        "Description": NotRequired[str],
        "Schedule": NotRequired[str],
        "Classifiers": NotRequired[Sequence[str]],
        "TablePrefix": NotRequired[str],
        "SchemaChangePolicy": NotRequired[SchemaChangePolicyTypeDef],
        "RecrawlPolicy": NotRequired[RecrawlPolicyTypeDef],
        "LineageConfiguration": NotRequired[LineageConfigurationTypeDef],
        "LakeFormationConfiguration": NotRequired[LakeFormationConfigurationTypeDef],
        "Configuration": NotRequired[str],
        "CrawlerSecurityConfiguration": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
UpdateCrawlerRequestRequestTypeDef = TypedDict(
    "UpdateCrawlerRequestRequestTypeDef",
    {
        "Name": str,
        "Role": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "Description": NotRequired[str],
        "Targets": NotRequired[CrawlerTargetsTypeDef],
        "Schedule": NotRequired[str],
        "Classifiers": NotRequired[Sequence[str]],
        "TablePrefix": NotRequired[str],
        "SchemaChangePolicy": NotRequired[SchemaChangePolicyTypeDef],
        "RecrawlPolicy": NotRequired[RecrawlPolicyTypeDef],
        "LineageConfiguration": NotRequired[LineageConfigurationTypeDef],
        "LakeFormationConfiguration": NotRequired[LakeFormationConfigurationTypeDef],
        "Configuration": NotRequired[str],
        "CrawlerSecurityConfiguration": NotRequired[str],
    },
)
StorageDescriptorUnionTypeDef = Union[StorageDescriptorTypeDef, StorageDescriptorOutputTypeDef]
GetStatementResponseTypeDef = TypedDict(
    "GetStatementResponseTypeDef",
    {
        "Statement": StatementTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListStatementsResponseTypeDef = TypedDict(
    "ListStatementsResponseTypeDef",
    {
        "Statements": List[StatementTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DynamicTransformUnionTypeDef = Union[DynamicTransformTypeDef, DynamicTransformOutputTypeDef]
RedshiftTargetUnionTypeDef = Union[RedshiftTargetTypeDef, RedshiftTargetOutputTypeDef]
AmazonRedshiftSourceUnionTypeDef = Union[
    AmazonRedshiftSourceTypeDef, AmazonRedshiftSourceOutputTypeDef
]
AmazonRedshiftTargetUnionTypeDef = Union[
    AmazonRedshiftTargetTypeDef, AmazonRedshiftTargetOutputTypeDef
]
SnowflakeSourceUnionTypeDef = Union[SnowflakeSourceTypeDef, SnowflakeSourceOutputTypeDef]
SnowflakeTargetUnionTypeDef = Union[SnowflakeTargetTypeDef, SnowflakeTargetOutputTypeDef]
TablePaginatorTypeDef = TypedDict(
    "TablePaginatorTypeDef",
    {
        "Name": str,
        "DatabaseName": NotRequired[str],
        "Description": NotRequired[str],
        "Owner": NotRequired[str],
        "CreateTime": NotRequired[datetime],
        "UpdateTime": NotRequired[datetime],
        "LastAccessTime": NotRequired[datetime],
        "LastAnalyzedTime": NotRequired[datetime],
        "Retention": NotRequired[int],
        "StorageDescriptor": NotRequired[StorageDescriptorOutputTypeDef],
        "PartitionKeys": NotRequired[List[ColumnOutputTypeDef]],
        "ViewOriginalText": NotRequired[str],
        "ViewExpandedText": NotRequired[str],
        "TableType": NotRequired[str],
        "Parameters": NotRequired[Dict[str, str]],
        "CreatedBy": NotRequired[str],
        "IsRegisteredWithLakeFormation": NotRequired[bool],
        "TargetTable": NotRequired[TableIdentifierTypeDef],
        "CatalogId": NotRequired[str],
        "VersionId": NotRequired[str],
        "FederatedTable": NotRequired[FederatedTableTypeDef],
        "ViewDefinition": NotRequired[ViewDefinitionTypeDef],
        "IsMultiDialectView": NotRequired[bool],
        "Status": NotRequired[TableStatusPaginatorTypeDef],
    },
)
TableTypeDef = TypedDict(
    "TableTypeDef",
    {
        "Name": str,
        "DatabaseName": NotRequired[str],
        "Description": NotRequired[str],
        "Owner": NotRequired[str],
        "CreateTime": NotRequired[datetime],
        "UpdateTime": NotRequired[datetime],
        "LastAccessTime": NotRequired[datetime],
        "LastAnalyzedTime": NotRequired[datetime],
        "Retention": NotRequired[int],
        "StorageDescriptor": NotRequired[StorageDescriptorOutputTypeDef],
        "PartitionKeys": NotRequired[List[ColumnOutputTypeDef]],
        "ViewOriginalText": NotRequired[str],
        "ViewExpandedText": NotRequired[str],
        "TableType": NotRequired[str],
        "Parameters": NotRequired[Dict[str, str]],
        "CreatedBy": NotRequired[str],
        "IsRegisteredWithLakeFormation": NotRequired[bool],
        "TargetTable": NotRequired[TableIdentifierTypeDef],
        "CatalogId": NotRequired[str],
        "VersionId": NotRequired[str],
        "FederatedTable": NotRequired[FederatedTableTypeDef],
        "ViewDefinition": NotRequired[ViewDefinitionTypeDef],
        "IsMultiDialectView": NotRequired[bool],
        "Status": NotRequired[TableStatusTypeDef],
    },
)
DecimalColumnStatisticsDataUnionTypeDef = Union[
    DecimalColumnStatisticsDataTypeDef, DecimalColumnStatisticsDataOutputTypeDef
]
CatalogKafkaSourceUnionTypeDef = Union[CatalogKafkaSourceTypeDef, CatalogKafkaSourceOutputTypeDef]
DirectKafkaSourceUnionTypeDef = Union[DirectKafkaSourceTypeDef, DirectKafkaSourceOutputTypeDef]
CatalogKinesisSourceUnionTypeDef = Union[
    CatalogKinesisSourceTypeDef, CatalogKinesisSourceOutputTypeDef
]
DirectKinesisSourceUnionTypeDef = Union[
    DirectKinesisSourceTypeDef, DirectKinesisSourceOutputTypeDef
]
NodeTypeDef = TypedDict(
    "NodeTypeDef",
    {
        "Type": NotRequired[NodeTypeType],
        "Name": NotRequired[str],
        "UniqueId": NotRequired[str],
        "TriggerDetails": NotRequired[TriggerNodeDetailsTypeDef],
        "JobDetails": NotRequired[JobNodeDetailsTypeDef],
        "CrawlerDetails": NotRequired[CrawlerNodeDetailsTypeDef],
    },
)
UpdateTriggerRequestRequestTypeDef = TypedDict(
    "UpdateTriggerRequestRequestTypeDef",
    {
        "Name": str,
        "TriggerUpdate": TriggerUpdateTypeDef,
    },
)
GetMLTransformsResponseTypeDef = TypedDict(
    "GetMLTransformsResponseTypeDef",
    {
        "Transforms": List[MLTransformTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateDatabaseRequestRequestTypeDef = TypedDict(
    "CreateDatabaseRequestRequestTypeDef",
    {
        "DatabaseInput": DatabaseInputTypeDef,
        "CatalogId": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
UpdateDatabaseRequestRequestTypeDef = TypedDict(
    "UpdateDatabaseRequestRequestTypeDef",
    {
        "Name": str,
        "DatabaseInput": DatabaseInputTypeDef,
        "CatalogId": NotRequired[str],
    },
)
BatchGetDataQualityResultResponseTypeDef = TypedDict(
    "BatchGetDataQualityResultResponseTypeDef",
    {
        "Results": List[DataQualityResultTypeDef],
        "ResultsNotFound": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ColumnStatisticsErrorTypeDef = TypedDict(
    "ColumnStatisticsErrorTypeDef",
    {
        "ColumnStatistics": NotRequired[ColumnStatisticsOutputTypeDef],
        "Error": NotRequired[ErrorDetailTypeDef],
    },
)
GetColumnStatisticsForPartitionResponseTypeDef = TypedDict(
    "GetColumnStatisticsForPartitionResponseTypeDef",
    {
        "ColumnStatisticsList": List[ColumnStatisticsOutputTypeDef],
        "Errors": List[ColumnErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetColumnStatisticsForTableResponseTypeDef = TypedDict(
    "GetColumnStatisticsForTableResponseTypeDef",
    {
        "ColumnStatisticsList": List[ColumnStatisticsOutputTypeDef],
        "Errors": List[ColumnErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetPartitionResponseTypeDef = TypedDict(
    "BatchGetPartitionResponseTypeDef",
    {
        "Partitions": List[PartitionTypeDef],
        "UnprocessedKeys": List[PartitionValueListOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPartitionResponseTypeDef = TypedDict(
    "GetPartitionResponseTypeDef",
    {
        "Partition": PartitionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPartitionsResponseTypeDef = TypedDict(
    "GetPartitionsResponseTypeDef",
    {
        "Partitions": List[PartitionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetUnfilteredPartitionMetadataResponseTypeDef = TypedDict(
    "GetUnfilteredPartitionMetadataResponseTypeDef",
    {
        "Partition": PartitionTypeDef,
        "AuthorizedColumns": List[str],
        "IsRegisteredWithLakeFormation": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UnfilteredPartitionTypeDef = TypedDict(
    "UnfilteredPartitionTypeDef",
    {
        "Partition": NotRequired[PartitionTypeDef],
        "AuthorizedColumns": NotRequired[List[str]],
        "IsRegisteredWithLakeFormation": NotRequired[bool],
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "LogicalOperator": FilterLogicalOperatorType,
        "Filters": Sequence[FilterExpressionUnionTypeDef],
    },
)
AthenaConnectorSourceUnionTypeDef = Union[
    AthenaConnectorSourceTypeDef, AthenaConnectorSourceOutputTypeDef
]
JDBCConnectorSourceUnionTypeDef = Union[
    JDBCConnectorSourceTypeDef, JDBCConnectorSourceOutputTypeDef
]
DataQualityResultFilterCriteriaTypeDef = TypedDict(
    "DataQualityResultFilterCriteriaTypeDef",
    {
        "DataSource": NotRequired[DataSourceUnionTypeDef],
        "JobName": NotRequired[str],
        "JobRunId": NotRequired[str],
        "StartedAfter": NotRequired[TimestampTypeDef],
        "StartedBefore": NotRequired[TimestampTypeDef],
    },
)
DataQualityRuleRecommendationRunFilterTypeDef = TypedDict(
    "DataQualityRuleRecommendationRunFilterTypeDef",
    {
        "DataSource": DataSourceUnionTypeDef,
        "StartedBefore": NotRequired[TimestampTypeDef],
        "StartedAfter": NotRequired[TimestampTypeDef],
    },
)
DataQualityRulesetEvaluationRunFilterTypeDef = TypedDict(
    "DataQualityRulesetEvaluationRunFilterTypeDef",
    {
        "DataSource": DataSourceUnionTypeDef,
        "StartedBefore": NotRequired[TimestampTypeDef],
        "StartedAfter": NotRequired[TimestampTypeDef],
    },
)
StartDataQualityRulesetEvaluationRunRequestRequestTypeDef = TypedDict(
    "StartDataQualityRulesetEvaluationRunRequestRequestTypeDef",
    {
        "DataSource": DataSourceTypeDef,
        "Role": str,
        "RulesetNames": Sequence[str],
        "NumberOfWorkers": NotRequired[int],
        "Timeout": NotRequired[int],
        "ClientToken": NotRequired[str],
        "AdditionalRunOptions": NotRequired[DataQualityEvaluationRunAdditionalRunOptionsTypeDef],
        "AdditionalDataSources": NotRequired[Mapping[str, DataSourceUnionTypeDef]],
    },
)
BatchTableOptimizerTypeDef = TypedDict(
    "BatchTableOptimizerTypeDef",
    {
        "catalogId": NotRequired[str],
        "databaseName": NotRequired[str],
        "tableName": NotRequired[str],
        "tableOptimizer": NotRequired[TableOptimizerTypeDef],
    },
)
GetTableOptimizerResponseTypeDef = TypedDict(
    "GetTableOptimizerResponseTypeDef",
    {
        "CatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "TableOptimizer": TableOptimizerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateConnectionRequestRequestTypeDef = TypedDict(
    "CreateConnectionRequestRequestTypeDef",
    {
        "ConnectionInput": ConnectionInputTypeDef,
        "CatalogId": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
UpdateConnectionRequestRequestTypeDef = TypedDict(
    "UpdateConnectionRequestRequestTypeDef",
    {
        "Name": str,
        "ConnectionInput": ConnectionInputTypeDef,
        "CatalogId": NotRequired[str],
    },
)
TestConnectionRequestRequestTypeDef = TypedDict(
    "TestConnectionRequestRequestTypeDef",
    {
        "ConnectionName": NotRequired[str],
        "TestConnectionInput": NotRequired[TestConnectionInputTypeDef],
    },
)
GetConnectionResponseTypeDef = TypedDict(
    "GetConnectionResponseTypeDef",
    {
        "Connection": ConnectionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetConnectionsResponseTypeDef = TypedDict(
    "GetConnectionsResponseTypeDef",
    {
        "ConnectionList": List[ConnectionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "Name": NotRequired[str],
        "JobMode": NotRequired[JobModeType],
        "JobRunQueuingEnabled": NotRequired[bool],
        "Description": NotRequired[str],
        "LogUri": NotRequired[str],
        "Role": NotRequired[str],
        "CreatedOn": NotRequired[datetime],
        "LastModifiedOn": NotRequired[datetime],
        "ExecutionProperty": NotRequired[ExecutionPropertyTypeDef],
        "Command": NotRequired[JobCommandTypeDef],
        "DefaultArguments": NotRequired[Dict[str, str]],
        "NonOverridableArguments": NotRequired[Dict[str, str]],
        "Connections": NotRequired[ConnectionsListOutputTypeDef],
        "MaxRetries": NotRequired[int],
        "AllocatedCapacity": NotRequired[int],
        "Timeout": NotRequired[int],
        "MaxCapacity": NotRequired[float],
        "WorkerType": NotRequired[WorkerTypeType],
        "NumberOfWorkers": NotRequired[int],
        "SecurityConfiguration": NotRequired[str],
        "NotificationProperty": NotRequired[NotificationPropertyTypeDef],
        "GlueVersion": NotRequired[str],
        "CodeGenConfigurationNodes": NotRequired[Dict[str, CodeGenConfigurationNodeOutputTypeDef]],
        "ExecutionClass": NotRequired[ExecutionClassType],
        "SourceControlDetails": NotRequired[SourceControlDetailsTypeDef],
        "MaintenanceWindow": NotRequired[str],
        "ProfileName": NotRequired[str],
    },
)
JobPaginatorTypeDef = TypedDict(
    "JobPaginatorTypeDef",
    {
        "Name": NotRequired[str],
        "JobMode": NotRequired[JobModeType],
        "JobRunQueuingEnabled": NotRequired[bool],
        "Description": NotRequired[str],
        "LogUri": NotRequired[str],
        "Role": NotRequired[str],
        "CreatedOn": NotRequired[datetime],
        "LastModifiedOn": NotRequired[datetime],
        "ExecutionProperty": NotRequired[ExecutionPropertyTypeDef],
        "Command": NotRequired[JobCommandTypeDef],
        "DefaultArguments": NotRequired[Dict[str, str]],
        "NonOverridableArguments": NotRequired[Dict[str, str]],
        "Connections": NotRequired[ConnectionsListOutputTypeDef],
        "MaxRetries": NotRequired[int],
        "AllocatedCapacity": NotRequired[int],
        "Timeout": NotRequired[int],
        "MaxCapacity": NotRequired[float],
        "WorkerType": NotRequired[WorkerTypeType],
        "NumberOfWorkers": NotRequired[int],
        "SecurityConfiguration": NotRequired[str],
        "NotificationProperty": NotRequired[NotificationPropertyTypeDef],
        "GlueVersion": NotRequired[str],
        "CodeGenConfigurationNodes": NotRequired[
            Dict[str, CodeGenConfigurationNodePaginatorTypeDef]
        ],
        "ExecutionClass": NotRequired[ExecutionClassType],
        "SourceControlDetails": NotRequired[SourceControlDetailsTypeDef],
        "MaintenanceWindow": NotRequired[str],
        "ProfileName": NotRequired[str],
    },
)
RecipeTypeDef = TypedDict(
    "RecipeTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "RecipeReference": NotRequired[RecipeReferenceTypeDef],
        "RecipeSteps": NotRequired[Sequence[RecipeStepUnionTypeDef]],
    },
)
PartitionInputTypeDef = TypedDict(
    "PartitionInputTypeDef",
    {
        "Values": NotRequired[Sequence[str]],
        "LastAccessTime": NotRequired[TimestampTypeDef],
        "StorageDescriptor": NotRequired[StorageDescriptorUnionTypeDef],
        "Parameters": NotRequired[Mapping[str, str]],
        "LastAnalyzedTime": NotRequired[TimestampTypeDef],
    },
)
TableInputTypeDef = TypedDict(
    "TableInputTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "Owner": NotRequired[str],
        "LastAccessTime": NotRequired[TimestampTypeDef],
        "LastAnalyzedTime": NotRequired[TimestampTypeDef],
        "Retention": NotRequired[int],
        "StorageDescriptor": NotRequired[StorageDescriptorUnionTypeDef],
        "PartitionKeys": NotRequired[Sequence[ColumnUnionTypeDef]],
        "ViewOriginalText": NotRequired[str],
        "ViewExpandedText": NotRequired[str],
        "TableType": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, str]],
        "TargetTable": NotRequired[TableIdentifierTypeDef],
        "ViewDefinition": NotRequired[ViewDefinitionInputTypeDef],
    },
)
GetTablesResponsePaginatorTypeDef = TypedDict(
    "GetTablesResponsePaginatorTypeDef",
    {
        "TableList": List[TablePaginatorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
TableVersionPaginatorTypeDef = TypedDict(
    "TableVersionPaginatorTypeDef",
    {
        "Table": NotRequired[TablePaginatorTypeDef],
        "VersionId": NotRequired[str],
    },
)
GetTableResponseTypeDef = TypedDict(
    "GetTableResponseTypeDef",
    {
        "Table": TableTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTablesResponseTypeDef = TypedDict(
    "GetTablesResponseTypeDef",
    {
        "TableList": List[TableTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetUnfilteredTableMetadataResponseTypeDef = TypedDict(
    "GetUnfilteredTableMetadataResponseTypeDef",
    {
        "Table": TableTypeDef,
        "AuthorizedColumns": List[str],
        "IsRegisteredWithLakeFormation": bool,
        "CellFilters": List[ColumnRowFilterTypeDef],
        "QueryAuthorizationId": str,
        "IsMultiDialectView": bool,
        "ResourceArn": str,
        "IsProtected": bool,
        "Permissions": List[PermissionType],
        "RowFilter": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchTablesResponseTypeDef = TypedDict(
    "SearchTablesResponseTypeDef",
    {
        "TableList": List[TableTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
TableVersionTypeDef = TypedDict(
    "TableVersionTypeDef",
    {
        "Table": NotRequired[TableTypeDef],
        "VersionId": NotRequired[str],
    },
)
ColumnStatisticsDataTypeDef = TypedDict(
    "ColumnStatisticsDataTypeDef",
    {
        "Type": ColumnStatisticsTypeType,
        "BooleanColumnStatisticsData": NotRequired[BooleanColumnStatisticsDataTypeDef],
        "DateColumnStatisticsData": NotRequired[DateColumnStatisticsDataUnionTypeDef],
        "DecimalColumnStatisticsData": NotRequired[DecimalColumnStatisticsDataUnionTypeDef],
        "DoubleColumnStatisticsData": NotRequired[DoubleColumnStatisticsDataTypeDef],
        "LongColumnStatisticsData": NotRequired[LongColumnStatisticsDataTypeDef],
        "StringColumnStatisticsData": NotRequired[StringColumnStatisticsDataTypeDef],
        "BinaryColumnStatisticsData": NotRequired[BinaryColumnStatisticsDataTypeDef],
    },
)
WorkflowGraphTypeDef = TypedDict(
    "WorkflowGraphTypeDef",
    {
        "Nodes": NotRequired[List[NodeTypeDef]],
        "Edges": NotRequired[List[EdgeTypeDef]],
    },
)
UpdateColumnStatisticsForPartitionResponseTypeDef = TypedDict(
    "UpdateColumnStatisticsForPartitionResponseTypeDef",
    {
        "Errors": List[ColumnStatisticsErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateColumnStatisticsForTableResponseTypeDef = TypedDict(
    "UpdateColumnStatisticsForTableResponseTypeDef",
    {
        "Errors": List[ColumnStatisticsErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetUnfilteredPartitionsMetadataResponseTypeDef = TypedDict(
    "GetUnfilteredPartitionsMetadataResponseTypeDef",
    {
        "UnfilteredPartitions": List[UnfilteredPartitionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
FilterUnionTypeDef = Union[FilterTypeDef, FilterOutputTypeDef]
ListDataQualityResultsRequestRequestTypeDef = TypedDict(
    "ListDataQualityResultsRequestRequestTypeDef",
    {
        "Filter": NotRequired[DataQualityResultFilterCriteriaTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListDataQualityRuleRecommendationRunsRequestRequestTypeDef = TypedDict(
    "ListDataQualityRuleRecommendationRunsRequestRequestTypeDef",
    {
        "Filter": NotRequired[DataQualityRuleRecommendationRunFilterTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListDataQualityRulesetEvaluationRunsRequestRequestTypeDef = TypedDict(
    "ListDataQualityRulesetEvaluationRunsRequestRequestTypeDef",
    {
        "Filter": NotRequired[DataQualityRulesetEvaluationRunFilterTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
BatchGetTableOptimizerResponseTypeDef = TypedDict(
    "BatchGetTableOptimizerResponseTypeDef",
    {
        "TableOptimizers": List[BatchTableOptimizerTypeDef],
        "Failures": List[BatchGetTableOptimizerErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetJobsResponseTypeDef = TypedDict(
    "BatchGetJobsResponseTypeDef",
    {
        "Jobs": List[JobTypeDef],
        "JobsNotFound": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetJobResponseTypeDef = TypedDict(
    "GetJobResponseTypeDef",
    {
        "Job": JobTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetJobsResponseTypeDef = TypedDict(
    "GetJobsResponseTypeDef",
    {
        "Jobs": List[JobTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetJobsResponsePaginatorTypeDef = TypedDict(
    "GetJobsResponsePaginatorTypeDef",
    {
        "Jobs": List[JobPaginatorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
RecipeUnionTypeDef = Union[RecipeTypeDef, RecipeOutputTypeDef]
BatchCreatePartitionRequestRequestTypeDef = TypedDict(
    "BatchCreatePartitionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionInputList": Sequence[PartitionInputTypeDef],
        "CatalogId": NotRequired[str],
    },
)
BatchUpdatePartitionRequestEntryTypeDef = TypedDict(
    "BatchUpdatePartitionRequestEntryTypeDef",
    {
        "PartitionValueList": Sequence[str],
        "PartitionInput": PartitionInputTypeDef,
    },
)
CreatePartitionRequestRequestTypeDef = TypedDict(
    "CreatePartitionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionInput": PartitionInputTypeDef,
        "CatalogId": NotRequired[str],
    },
)
UpdatePartitionRequestRequestTypeDef = TypedDict(
    "UpdatePartitionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionValueList": Sequence[str],
        "PartitionInput": PartitionInputTypeDef,
        "CatalogId": NotRequired[str],
    },
)
CreateTableRequestRequestTypeDef = TypedDict(
    "CreateTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableInput": TableInputTypeDef,
        "CatalogId": NotRequired[str],
        "PartitionIndexes": NotRequired[Sequence[PartitionIndexTypeDef]],
        "TransactionId": NotRequired[str],
        "OpenTableFormatInput": NotRequired[OpenTableFormatInputTypeDef],
    },
)
UpdateTableRequestRequestTypeDef = TypedDict(
    "UpdateTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableInput": TableInputTypeDef,
        "CatalogId": NotRequired[str],
        "SkipArchive": NotRequired[bool],
        "TransactionId": NotRequired[str],
        "VersionId": NotRequired[str],
        "ViewUpdateAction": NotRequired[ViewUpdateActionType],
        "Force": NotRequired[bool],
    },
)
GetTableVersionsResponsePaginatorTypeDef = TypedDict(
    "GetTableVersionsResponsePaginatorTypeDef",
    {
        "TableVersions": List[TableVersionPaginatorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetTableVersionResponseTypeDef = TypedDict(
    "GetTableVersionResponseTypeDef",
    {
        "TableVersion": TableVersionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTableVersionsResponseTypeDef = TypedDict(
    "GetTableVersionsResponseTypeDef",
    {
        "TableVersions": List[TableVersionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ColumnStatisticsDataUnionTypeDef = Union[
    ColumnStatisticsDataTypeDef, ColumnStatisticsDataOutputTypeDef
]
WorkflowRunTypeDef = TypedDict(
    "WorkflowRunTypeDef",
    {
        "Name": NotRequired[str],
        "WorkflowRunId": NotRequired[str],
        "PreviousRunId": NotRequired[str],
        "WorkflowRunProperties": NotRequired[Dict[str, str]],
        "StartedOn": NotRequired[datetime],
        "CompletedOn": NotRequired[datetime],
        "Status": NotRequired[WorkflowRunStatusType],
        "ErrorMessage": NotRequired[str],
        "Statistics": NotRequired[WorkflowRunStatisticsTypeDef],
        "Graph": NotRequired[WorkflowGraphTypeDef],
        "StartingEventBatchCondition": NotRequired[StartingEventBatchConditionTypeDef],
    },
)
CodeGenConfigurationNodeTypeDef = TypedDict(
    "CodeGenConfigurationNodeTypeDef",
    {
        "AthenaConnectorSource": NotRequired[AthenaConnectorSourceUnionTypeDef],
        "JDBCConnectorSource": NotRequired[JDBCConnectorSourceUnionTypeDef],
        "SparkConnectorSource": NotRequired[SparkConnectorSourceUnionTypeDef],
        "CatalogSource": NotRequired[CatalogSourceTypeDef],
        "RedshiftSource": NotRequired[RedshiftSourceTypeDef],
        "S3CatalogSource": NotRequired[S3CatalogSourceTypeDef],
        "S3CsvSource": NotRequired[S3CsvSourceUnionTypeDef],
        "S3JsonSource": NotRequired[S3JsonSourceUnionTypeDef],
        "S3ParquetSource": NotRequired[S3ParquetSourceUnionTypeDef],
        "RelationalCatalogSource": NotRequired[RelationalCatalogSourceTypeDef],
        "DynamoDBCatalogSource": NotRequired[DynamoDBCatalogSourceTypeDef],
        "JDBCConnectorTarget": NotRequired[JDBCConnectorTargetUnionTypeDef],
        "SparkConnectorTarget": NotRequired[SparkConnectorTargetUnionTypeDef],
        "CatalogTarget": NotRequired[BasicCatalogTargetUnionTypeDef],
        "RedshiftTarget": NotRequired[RedshiftTargetUnionTypeDef],
        "S3CatalogTarget": NotRequired[S3CatalogTargetUnionTypeDef],
        "S3GlueParquetTarget": NotRequired[S3GlueParquetTargetUnionTypeDef],
        "S3DirectTarget": NotRequired[S3DirectTargetUnionTypeDef],
        "ApplyMapping": NotRequired[ApplyMappingUnionTypeDef],
        "SelectFields": NotRequired[SelectFieldsUnionTypeDef],
        "DropFields": NotRequired[DropFieldsUnionTypeDef],
        "RenameField": NotRequired[RenameFieldUnionTypeDef],
        "Spigot": NotRequired[SpigotUnionTypeDef],
        "Join": NotRequired[JoinUnionTypeDef],
        "SplitFields": NotRequired[SplitFieldsUnionTypeDef],
        "SelectFromCollection": NotRequired[SelectFromCollectionUnionTypeDef],
        "FillMissingValues": NotRequired[FillMissingValuesUnionTypeDef],
        "Filter": NotRequired[FilterUnionTypeDef],
        "CustomCode": NotRequired[CustomCodeUnionTypeDef],
        "SparkSQL": NotRequired[SparkSQLUnionTypeDef],
        "DirectKinesisSource": NotRequired[DirectKinesisSourceUnionTypeDef],
        "DirectKafkaSource": NotRequired[DirectKafkaSourceUnionTypeDef],
        "CatalogKinesisSource": NotRequired[CatalogKinesisSourceUnionTypeDef],
        "CatalogKafkaSource": NotRequired[CatalogKafkaSourceUnionTypeDef],
        "DropNullFields": NotRequired[DropNullFieldsUnionTypeDef],
        "Merge": NotRequired[MergeUnionTypeDef],
        "Union": NotRequired[UnionUnionTypeDef],
        "PIIDetection": NotRequired[PIIDetectionUnionTypeDef],
        "Aggregate": NotRequired[AggregateUnionTypeDef],
        "DropDuplicates": NotRequired[DropDuplicatesUnionTypeDef],
        "GovernedCatalogTarget": NotRequired[GovernedCatalogTargetUnionTypeDef],
        "GovernedCatalogSource": NotRequired[GovernedCatalogSourceTypeDef],
        "MicrosoftSQLServerCatalogSource": NotRequired[MicrosoftSQLServerCatalogSourceTypeDef],
        "MySQLCatalogSource": NotRequired[MySQLCatalogSourceTypeDef],
        "OracleSQLCatalogSource": NotRequired[OracleSQLCatalogSourceTypeDef],
        "PostgreSQLCatalogSource": NotRequired[PostgreSQLCatalogSourceTypeDef],
        "MicrosoftSQLServerCatalogTarget": NotRequired[MicrosoftSQLServerCatalogTargetUnionTypeDef],
        "MySQLCatalogTarget": NotRequired[MySQLCatalogTargetUnionTypeDef],
        "OracleSQLCatalogTarget": NotRequired[OracleSQLCatalogTargetUnionTypeDef],
        "PostgreSQLCatalogTarget": NotRequired[PostgreSQLCatalogTargetUnionTypeDef],
        "DynamicTransform": NotRequired[DynamicTransformUnionTypeDef],
        "EvaluateDataQuality": NotRequired[EvaluateDataQualityUnionTypeDef],
        "S3CatalogHudiSource": NotRequired[S3CatalogHudiSourceUnionTypeDef],
        "CatalogHudiSource": NotRequired[CatalogHudiSourceUnionTypeDef],
        "S3HudiSource": NotRequired[S3HudiSourceUnionTypeDef],
        "S3HudiCatalogTarget": NotRequired[S3HudiCatalogTargetUnionTypeDef],
        "S3HudiDirectTarget": NotRequired[S3HudiDirectTargetUnionTypeDef],
        "DirectJDBCSource": NotRequired[DirectJDBCSourceTypeDef],
        "S3CatalogDeltaSource": NotRequired[S3CatalogDeltaSourceUnionTypeDef],
        "CatalogDeltaSource": NotRequired[CatalogDeltaSourceUnionTypeDef],
        "S3DeltaSource": NotRequired[S3DeltaSourceUnionTypeDef],
        "S3DeltaCatalogTarget": NotRequired[S3DeltaCatalogTargetUnionTypeDef],
        "S3DeltaDirectTarget": NotRequired[S3DeltaDirectTargetUnionTypeDef],
        "AmazonRedshiftSource": NotRequired[AmazonRedshiftSourceUnionTypeDef],
        "AmazonRedshiftTarget": NotRequired[AmazonRedshiftTargetUnionTypeDef],
        "EvaluateDataQualityMultiFrame": NotRequired[EvaluateDataQualityMultiFrameUnionTypeDef],
        "Recipe": NotRequired[RecipeUnionTypeDef],
        "SnowflakeSource": NotRequired[SnowflakeSourceUnionTypeDef],
        "SnowflakeTarget": NotRequired[SnowflakeTargetUnionTypeDef],
        "ConnectorDataSource": NotRequired[ConnectorDataSourceUnionTypeDef],
        "ConnectorDataTarget": NotRequired[ConnectorDataTargetUnionTypeDef],
    },
)
BatchUpdatePartitionRequestRequestTypeDef = TypedDict(
    "BatchUpdatePartitionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "Entries": Sequence[BatchUpdatePartitionRequestEntryTypeDef],
        "CatalogId": NotRequired[str],
    },
)
ColumnStatisticsTypeDef = TypedDict(
    "ColumnStatisticsTypeDef",
    {
        "ColumnName": str,
        "ColumnType": str,
        "AnalyzedTime": TimestampTypeDef,
        "StatisticsData": ColumnStatisticsDataUnionTypeDef,
    },
)
GetWorkflowRunResponseTypeDef = TypedDict(
    "GetWorkflowRunResponseTypeDef",
    {
        "Run": WorkflowRunTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetWorkflowRunsResponseTypeDef = TypedDict(
    "GetWorkflowRunsResponseTypeDef",
    {
        "Runs": List[WorkflowRunTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
WorkflowTypeDef = TypedDict(
    "WorkflowTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "DefaultRunProperties": NotRequired[Dict[str, str]],
        "CreatedOn": NotRequired[datetime],
        "LastModifiedOn": NotRequired[datetime],
        "LastRun": NotRequired[WorkflowRunTypeDef],
        "Graph": NotRequired[WorkflowGraphTypeDef],
        "MaxConcurrentRuns": NotRequired[int],
        "BlueprintDetails": NotRequired[BlueprintDetailsTypeDef],
    },
)
CodeGenConfigurationNodeUnionTypeDef = Union[
    CodeGenConfigurationNodeTypeDef, CodeGenConfigurationNodeOutputTypeDef
]
ColumnStatisticsUnionTypeDef = Union[ColumnStatisticsTypeDef, ColumnStatisticsOutputTypeDef]
UpdateColumnStatisticsForTableRequestRequestTypeDef = TypedDict(
    "UpdateColumnStatisticsForTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "ColumnStatisticsList": Sequence[ColumnStatisticsTypeDef],
        "CatalogId": NotRequired[str],
    },
)
BatchGetWorkflowsResponseTypeDef = TypedDict(
    "BatchGetWorkflowsResponseTypeDef",
    {
        "Workflows": List[WorkflowTypeDef],
        "MissingWorkflows": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetWorkflowResponseTypeDef = TypedDict(
    "GetWorkflowResponseTypeDef",
    {
        "Workflow": WorkflowTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateJobRequestRequestTypeDef = TypedDict(
    "CreateJobRequestRequestTypeDef",
    {
        "Name": str,
        "Role": str,
        "Command": JobCommandTypeDef,
        "JobMode": NotRequired[JobModeType],
        "JobRunQueuingEnabled": NotRequired[bool],
        "Description": NotRequired[str],
        "LogUri": NotRequired[str],
        "ExecutionProperty": NotRequired[ExecutionPropertyTypeDef],
        "DefaultArguments": NotRequired[Mapping[str, str]],
        "NonOverridableArguments": NotRequired[Mapping[str, str]],
        "Connections": NotRequired[ConnectionsListTypeDef],
        "MaxRetries": NotRequired[int],
        "AllocatedCapacity": NotRequired[int],
        "Timeout": NotRequired[int],
        "MaxCapacity": NotRequired[float],
        "SecurityConfiguration": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "NotificationProperty": NotRequired[NotificationPropertyTypeDef],
        "GlueVersion": NotRequired[str],
        "NumberOfWorkers": NotRequired[int],
        "WorkerType": NotRequired[WorkerTypeType],
        "CodeGenConfigurationNodes": NotRequired[
            Mapping[str, CodeGenConfigurationNodeUnionTypeDef]
        ],
        "ExecutionClass": NotRequired[ExecutionClassType],
        "SourceControlDetails": NotRequired[SourceControlDetailsTypeDef],
        "MaintenanceWindow": NotRequired[str],
    },
)
JobUpdateTypeDef = TypedDict(
    "JobUpdateTypeDef",
    {
        "JobMode": NotRequired[JobModeType],
        "JobRunQueuingEnabled": NotRequired[bool],
        "Description": NotRequired[str],
        "LogUri": NotRequired[str],
        "Role": NotRequired[str],
        "ExecutionProperty": NotRequired[ExecutionPropertyTypeDef],
        "Command": NotRequired[JobCommandTypeDef],
        "DefaultArguments": NotRequired[Mapping[str, str]],
        "NonOverridableArguments": NotRequired[Mapping[str, str]],
        "Connections": NotRequired[ConnectionsListUnionTypeDef],
        "MaxRetries": NotRequired[int],
        "AllocatedCapacity": NotRequired[int],
        "Timeout": NotRequired[int],
        "MaxCapacity": NotRequired[float],
        "WorkerType": NotRequired[WorkerTypeType],
        "NumberOfWorkers": NotRequired[int],
        "SecurityConfiguration": NotRequired[str],
        "NotificationProperty": NotRequired[NotificationPropertyTypeDef],
        "GlueVersion": NotRequired[str],
        "CodeGenConfigurationNodes": NotRequired[
            Mapping[str, CodeGenConfigurationNodeUnionTypeDef]
        ],
        "ExecutionClass": NotRequired[ExecutionClassType],
        "SourceControlDetails": NotRequired[SourceControlDetailsTypeDef],
        "MaintenanceWindow": NotRequired[str],
    },
)
UpdateColumnStatisticsForPartitionRequestRequestTypeDef = TypedDict(
    "UpdateColumnStatisticsForPartitionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionValues": Sequence[str],
        "ColumnStatisticsList": Sequence[ColumnStatisticsUnionTypeDef],
        "CatalogId": NotRequired[str],
    },
)
UpdateJobRequestRequestTypeDef = TypedDict(
    "UpdateJobRequestRequestTypeDef",
    {
        "JobName": str,
        "JobUpdate": JobUpdateTypeDef,
    },
)
