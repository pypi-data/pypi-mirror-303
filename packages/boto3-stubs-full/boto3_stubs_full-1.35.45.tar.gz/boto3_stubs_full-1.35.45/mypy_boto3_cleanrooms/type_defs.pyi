"""
Type annotations for cleanrooms service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cleanrooms/type_defs/)

Usage::

    ```python
    from mypy_boto3_cleanrooms.type_defs import AggregateColumnOutputTypeDef

    data: AggregateColumnOutputTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    AdditionalAnalysesType,
    AggregateFunctionNameType,
    AnalysisRuleTypeType,
    AnalysisTemplateValidationStatusType,
    AnalysisTypeType,
    CollaborationQueryLogStatusType,
    ConfiguredTableAnalysisRuleTypeType,
    ConfiguredTableAssociationAnalysisRuleTypeType,
    DifferentialPrivacyAggregationTypeType,
    FilterableMemberStatusType,
    IdNamespaceTypeType,
    JoinOperatorType,
    MemberAbilityType,
    MembershipQueryLogStatusType,
    MembershipStatusType,
    MemberStatusType,
    ParameterTypeType,
    PrivacyBudgetTemplateAutoRefreshType,
    ProtectedQueryStatusType,
    ResultFormatType,
    ScalarFunctionsType,
    SchemaStatusReasonCodeType,
    SchemaStatusType,
    SchemaTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AggregateColumnOutputTypeDef",
    "AggregateColumnTypeDef",
    "AggregationConstraintTypeDef",
    "AnalysisParameterTypeDef",
    "AnalysisRuleListOutputTypeDef",
    "AnalysisRuleListTypeDef",
    "AnalysisSchemaTypeDef",
    "AnalysisSourceTypeDef",
    "AnalysisTemplateSummaryTypeDef",
    "AnalysisTemplateValidationStatusReasonTypeDef",
    "BatchGetCollaborationAnalysisTemplateErrorTypeDef",
    "BatchGetCollaborationAnalysisTemplateInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "BatchGetSchemaAnalysisRuleErrorTypeDef",
    "SchemaAnalysisRuleRequestTypeDef",
    "BatchGetSchemaErrorTypeDef",
    "BatchGetSchemaInputRequestTypeDef",
    "CollaborationAnalysisTemplateSummaryTypeDef",
    "CollaborationConfiguredAudienceModelAssociationSummaryTypeDef",
    "CollaborationConfiguredAudienceModelAssociationTypeDef",
    "IdNamespaceAssociationInputReferenceConfigTypeDef",
    "IdNamespaceAssociationInputReferencePropertiesSummaryTypeDef",
    "IdMappingConfigTypeDef",
    "IdNamespaceAssociationInputReferencePropertiesTypeDef",
    "CollaborationPrivacyBudgetTemplateSummaryTypeDef",
    "CollaborationSummaryTypeDef",
    "DataEncryptionMetadataTypeDef",
    "ColumnTypeDef",
    "DirectAnalysisConfigurationDetailsTypeDef",
    "ConfiguredAudienceModelAssociationSummaryTypeDef",
    "ConfiguredAudienceModelAssociationTypeDef",
    "ConfiguredTableAssociationAnalysisRuleAggregationOutputTypeDef",
    "ConfiguredTableAssociationAnalysisRuleAggregationTypeDef",
    "ConfiguredTableAssociationAnalysisRuleCustomOutputTypeDef",
    "ConfiguredTableAssociationAnalysisRuleCustomTypeDef",
    "ConfiguredTableAssociationAnalysisRuleListOutputTypeDef",
    "ConfiguredTableAssociationAnalysisRuleListTypeDef",
    "ConfiguredTableAssociationSummaryTypeDef",
    "ConfiguredTableAssociationTypeDef",
    "ConfiguredTableSummaryTypeDef",
    "CreateConfiguredAudienceModelAssociationInputRequestTypeDef",
    "CreateConfiguredTableAssociationInputRequestTypeDef",
    "IdMappingTableInputReferenceConfigTypeDef",
    "DeleteAnalysisTemplateInputRequestTypeDef",
    "DeleteCollaborationInputRequestTypeDef",
    "DeleteConfiguredAudienceModelAssociationInputRequestTypeDef",
    "DeleteConfiguredTableAnalysisRuleInputRequestTypeDef",
    "DeleteConfiguredTableAssociationAnalysisRuleInputRequestTypeDef",
    "DeleteConfiguredTableAssociationInputRequestTypeDef",
    "DeleteConfiguredTableInputRequestTypeDef",
    "DeleteIdMappingTableInputRequestTypeDef",
    "DeleteIdNamespaceAssociationInputRequestTypeDef",
    "DeleteMemberInputRequestTypeDef",
    "DeleteMembershipInputRequestTypeDef",
    "DeletePrivacyBudgetTemplateInputRequestTypeDef",
    "DifferentialPrivacyColumnTypeDef",
    "DifferentialPrivacySensitivityParametersTypeDef",
    "DifferentialPrivacyPreviewAggregationTypeDef",
    "DifferentialPrivacyPreviewParametersInputTypeDef",
    "DifferentialPrivacyPrivacyBudgetAggregationTypeDef",
    "DifferentialPrivacyTemplateParametersInputTypeDef",
    "DifferentialPrivacyTemplateParametersOutputTypeDef",
    "DifferentialPrivacyTemplateUpdateParametersTypeDef",
    "GetAnalysisTemplateInputRequestTypeDef",
    "GetCollaborationAnalysisTemplateInputRequestTypeDef",
    "GetCollaborationConfiguredAudienceModelAssociationInputRequestTypeDef",
    "GetCollaborationIdNamespaceAssociationInputRequestTypeDef",
    "GetCollaborationInputRequestTypeDef",
    "GetCollaborationPrivacyBudgetTemplateInputRequestTypeDef",
    "GetConfiguredAudienceModelAssociationInputRequestTypeDef",
    "GetConfiguredTableAnalysisRuleInputRequestTypeDef",
    "GetConfiguredTableAssociationAnalysisRuleInputRequestTypeDef",
    "GetConfiguredTableAssociationInputRequestTypeDef",
    "GetConfiguredTableInputRequestTypeDef",
    "GetIdMappingTableInputRequestTypeDef",
    "GetIdNamespaceAssociationInputRequestTypeDef",
    "GetMembershipInputRequestTypeDef",
    "GetPrivacyBudgetTemplateInputRequestTypeDef",
    "GetProtectedQueryInputRequestTypeDef",
    "GetSchemaAnalysisRuleInputRequestTypeDef",
    "GetSchemaInputRequestTypeDef",
    "GlueTableReferenceTypeDef",
    "IdMappingTableInputSourceTypeDef",
    "PaginatorConfigTypeDef",
    "ListAnalysisTemplatesInputRequestTypeDef",
    "ListCollaborationAnalysisTemplatesInputRequestTypeDef",
    "ListCollaborationConfiguredAudienceModelAssociationsInputRequestTypeDef",
    "ListCollaborationIdNamespaceAssociationsInputRequestTypeDef",
    "ListCollaborationPrivacyBudgetTemplatesInputRequestTypeDef",
    "ListCollaborationPrivacyBudgetsInputRequestTypeDef",
    "ListCollaborationsInputRequestTypeDef",
    "ListConfiguredAudienceModelAssociationsInputRequestTypeDef",
    "ListConfiguredTableAssociationsInputRequestTypeDef",
    "ListConfiguredTablesInputRequestTypeDef",
    "ListIdMappingTablesInputRequestTypeDef",
    "ListIdNamespaceAssociationsInputRequestTypeDef",
    "ListMembersInputRequestTypeDef",
    "ListMembershipsInputRequestTypeDef",
    "ListPrivacyBudgetTemplatesInputRequestTypeDef",
    "PrivacyBudgetTemplateSummaryTypeDef",
    "ListPrivacyBudgetsInputRequestTypeDef",
    "ListProtectedQueriesInputRequestTypeDef",
    "ListSchemasInputRequestTypeDef",
    "SchemaSummaryTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "MembershipQueryComputePaymentConfigTypeDef",
    "ProtectedQueryS3OutputConfigurationTypeDef",
    "QueryComputePaymentConfigTypeDef",
    "PopulateIdMappingTableInputRequestTypeDef",
    "ProtectedQueryErrorTypeDef",
    "ProtectedQueryMemberOutputConfigurationTypeDef",
    "ProtectedQueryS3OutputTypeDef",
    "ProtectedQuerySingleMemberOutputTypeDef",
    "ProtectedQuerySQLParametersOutputTypeDef",
    "ProtectedQuerySQLParametersTypeDef",
    "ProtectedQueryStatisticsTypeDef",
    "QueryConstraintRequireOverlapTypeDef",
    "SchemaStatusReasonTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateAnalysisTemplateInputRequestTypeDef",
    "UpdateCollaborationInputRequestTypeDef",
    "UpdateConfiguredAudienceModelAssociationInputRequestTypeDef",
    "UpdateConfiguredTableAssociationInputRequestTypeDef",
    "UpdateConfiguredTableInputRequestTypeDef",
    "UpdateIdMappingTableInputRequestTypeDef",
    "UpdateProtectedQueryInputRequestTypeDef",
    "AggregateColumnUnionTypeDef",
    "AnalysisRuleAggregationOutputTypeDef",
    "AnalysisRuleListUnionTypeDef",
    "CreateAnalysisTemplateInputRequestTypeDef",
    "AnalysisTemplateValidationStatusDetailTypeDef",
    "ListAnalysisTemplatesOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "PopulateIdMappingTableOutputTypeDef",
    "BatchGetSchemaAnalysisRuleInputRequestTypeDef",
    "ListCollaborationAnalysisTemplatesOutputTypeDef",
    "ListCollaborationConfiguredAudienceModelAssociationsOutputTypeDef",
    "GetCollaborationConfiguredAudienceModelAssociationOutputTypeDef",
    "CollaborationIdNamespaceAssociationSummaryTypeDef",
    "IdNamespaceAssociationSummaryTypeDef",
    "CreateIdNamespaceAssociationInputRequestTypeDef",
    "UpdateIdNamespaceAssociationInputRequestTypeDef",
    "CollaborationIdNamespaceAssociationTypeDef",
    "IdNamespaceAssociationTypeDef",
    "ListCollaborationPrivacyBudgetTemplatesOutputTypeDef",
    "ListCollaborationsOutputTypeDef",
    "CollaborationTypeDef",
    "ConfigurationDetailsTypeDef",
    "ListConfiguredAudienceModelAssociationsOutputTypeDef",
    "CreateConfiguredAudienceModelAssociationOutputTypeDef",
    "GetConfiguredAudienceModelAssociationOutputTypeDef",
    "UpdateConfiguredAudienceModelAssociationOutputTypeDef",
    "ConfiguredTableAssociationAnalysisRuleAggregationUnionTypeDef",
    "ConfiguredTableAssociationAnalysisRuleCustomUnionTypeDef",
    "ConfiguredTableAssociationAnalysisRulePolicyV1OutputTypeDef",
    "ConfiguredTableAssociationAnalysisRuleListUnionTypeDef",
    "ListConfiguredTableAssociationsOutputTypeDef",
    "CreateConfiguredTableAssociationOutputTypeDef",
    "GetConfiguredTableAssociationOutputTypeDef",
    "UpdateConfiguredTableAssociationOutputTypeDef",
    "ListConfiguredTablesOutputTypeDef",
    "CreateIdMappingTableInputRequestTypeDef",
    "IdMappingTableSummaryTypeDef",
    "DifferentialPrivacyConfigurationOutputTypeDef",
    "DifferentialPrivacyConfigurationTypeDef",
    "DifferentialPrivacyParametersTypeDef",
    "DifferentialPrivacyPrivacyImpactTypeDef",
    "PreviewPrivacyImpactParametersInputTypeDef",
    "DifferentialPrivacyPrivacyBudgetTypeDef",
    "PrivacyBudgetTemplateParametersInputTypeDef",
    "PrivacyBudgetTemplateParametersOutputTypeDef",
    "PrivacyBudgetTemplateUpdateParametersTypeDef",
    "TableReferenceTypeDef",
    "IdMappingTableInputReferencePropertiesTypeDef",
    "IdMappingTableSchemaTypePropertiesTypeDef",
    "ListAnalysisTemplatesInputListAnalysisTemplatesPaginateTypeDef",
    "ListCollaborationAnalysisTemplatesInputListCollaborationAnalysisTemplatesPaginateTypeDef",
    "ListCollaborationConfiguredAudienceModelAssociationsInputListCollaborationConfiguredAudienceModelAssociationsPaginateTypeDef",
    "ListCollaborationIdNamespaceAssociationsInputListCollaborationIdNamespaceAssociationsPaginateTypeDef",
    "ListCollaborationPrivacyBudgetTemplatesInputListCollaborationPrivacyBudgetTemplatesPaginateTypeDef",
    "ListCollaborationPrivacyBudgetsInputListCollaborationPrivacyBudgetsPaginateTypeDef",
    "ListCollaborationsInputListCollaborationsPaginateTypeDef",
    "ListConfiguredAudienceModelAssociationsInputListConfiguredAudienceModelAssociationsPaginateTypeDef",
    "ListConfiguredTableAssociationsInputListConfiguredTableAssociationsPaginateTypeDef",
    "ListConfiguredTablesInputListConfiguredTablesPaginateTypeDef",
    "ListIdMappingTablesInputListIdMappingTablesPaginateTypeDef",
    "ListIdNamespaceAssociationsInputListIdNamespaceAssociationsPaginateTypeDef",
    "ListMembersInputListMembersPaginateTypeDef",
    "ListMembershipsInputListMembershipsPaginateTypeDef",
    "ListPrivacyBudgetTemplatesInputListPrivacyBudgetTemplatesPaginateTypeDef",
    "ListPrivacyBudgetsInputListPrivacyBudgetsPaginateTypeDef",
    "ListProtectedQueriesInputListProtectedQueriesPaginateTypeDef",
    "ListSchemasInputListSchemasPaginateTypeDef",
    "ListPrivacyBudgetTemplatesOutputTypeDef",
    "ListSchemasOutputTypeDef",
    "MembershipPaymentConfigurationTypeDef",
    "MembershipProtectedQueryOutputConfigurationTypeDef",
    "PaymentConfigurationTypeDef",
    "ProtectedQueryOutputConfigurationTypeDef",
    "ProtectedQueryOutputTypeDef",
    "QueryConstraintTypeDef",
    "SchemaStatusDetailTypeDef",
    "AnalysisRuleAggregationTypeDef",
    "AnalysisTemplateTypeDef",
    "CollaborationAnalysisTemplateTypeDef",
    "ListCollaborationIdNamespaceAssociationsOutputTypeDef",
    "ListIdNamespaceAssociationsOutputTypeDef",
    "GetCollaborationIdNamespaceAssociationOutputTypeDef",
    "CreateIdNamespaceAssociationOutputTypeDef",
    "GetIdNamespaceAssociationOutputTypeDef",
    "UpdateIdNamespaceAssociationOutputTypeDef",
    "CreateCollaborationOutputTypeDef",
    "GetCollaborationOutputTypeDef",
    "UpdateCollaborationOutputTypeDef",
    "ReceiverConfigurationTypeDef",
    "ConfiguredTableAssociationAnalysisRulePolicyOutputTypeDef",
    "ConfiguredTableAssociationAnalysisRulePolicyV1TypeDef",
    "ListIdMappingTablesOutputTypeDef",
    "AnalysisRuleCustomOutputTypeDef",
    "DifferentialPrivacyConfigurationUnionTypeDef",
    "PrivacyImpactTypeDef",
    "PreviewPrivacyImpactInputRequestTypeDef",
    "PrivacyBudgetTypeDef",
    "CreatePrivacyBudgetTemplateInputRequestTypeDef",
    "CollaborationPrivacyBudgetTemplateTypeDef",
    "PrivacyBudgetTemplateTypeDef",
    "UpdatePrivacyBudgetTemplateInputRequestTypeDef",
    "ConfiguredTableTypeDef",
    "CreateConfiguredTableInputRequestTypeDef",
    "IdMappingTableTypeDef",
    "SchemaTypePropertiesTypeDef",
    "MembershipSummaryTypeDef",
    "MembershipProtectedQueryResultConfigurationTypeDef",
    "MemberSpecificationTypeDef",
    "MemberSummaryTypeDef",
    "ProtectedQueryResultConfigurationTypeDef",
    "ProtectedQueryResultTypeDef",
    "AnalysisRuleIdMappingTableTypeDef",
    "AnalysisRuleAggregationUnionTypeDef",
    "CreateAnalysisTemplateOutputTypeDef",
    "GetAnalysisTemplateOutputTypeDef",
    "UpdateAnalysisTemplateOutputTypeDef",
    "BatchGetCollaborationAnalysisTemplateOutputTypeDef",
    "GetCollaborationAnalysisTemplateOutputTypeDef",
    "ProtectedQuerySummaryTypeDef",
    "ConfiguredTableAssociationAnalysisRuleTypeDef",
    "ConfiguredTableAssociationAnalysisRulePolicyV1UnionTypeDef",
    "ConfiguredTableAnalysisRulePolicyV1OutputTypeDef",
    "AnalysisRuleCustomTypeDef",
    "PreviewPrivacyImpactOutputTypeDef",
    "CollaborationPrivacyBudgetSummaryTypeDef",
    "PrivacyBudgetSummaryTypeDef",
    "GetCollaborationPrivacyBudgetTemplateOutputTypeDef",
    "CreatePrivacyBudgetTemplateOutputTypeDef",
    "GetPrivacyBudgetTemplateOutputTypeDef",
    "UpdatePrivacyBudgetTemplateOutputTypeDef",
    "CreateConfiguredTableOutputTypeDef",
    "GetConfiguredTableOutputTypeDef",
    "UpdateConfiguredTableOutputTypeDef",
    "CreateIdMappingTableOutputTypeDef",
    "GetIdMappingTableOutputTypeDef",
    "UpdateIdMappingTableOutputTypeDef",
    "SchemaTypeDef",
    "ListMembershipsOutputTypeDef",
    "CreateMembershipInputRequestTypeDef",
    "MembershipTypeDef",
    "UpdateMembershipInputRequestTypeDef",
    "CreateCollaborationInputRequestTypeDef",
    "ListMembersOutputTypeDef",
    "StartProtectedQueryInputRequestTypeDef",
    "ProtectedQueryTypeDef",
    "AnalysisRulePolicyV1TypeDef",
    "ListProtectedQueriesOutputTypeDef",
    "CreateConfiguredTableAssociationAnalysisRuleOutputTypeDef",
    "GetConfiguredTableAssociationAnalysisRuleOutputTypeDef",
    "UpdateConfiguredTableAssociationAnalysisRuleOutputTypeDef",
    "ConfiguredTableAssociationAnalysisRulePolicyTypeDef",
    "ConfiguredTableAnalysisRulePolicyOutputTypeDef",
    "AnalysisRuleCustomUnionTypeDef",
    "ListCollaborationPrivacyBudgetsOutputTypeDef",
    "ListPrivacyBudgetsOutputTypeDef",
    "BatchGetSchemaOutputTypeDef",
    "GetSchemaOutputTypeDef",
    "CreateMembershipOutputTypeDef",
    "GetMembershipOutputTypeDef",
    "UpdateMembershipOutputTypeDef",
    "GetProtectedQueryOutputTypeDef",
    "StartProtectedQueryOutputTypeDef",
    "UpdateProtectedQueryOutputTypeDef",
    "AnalysisRulePolicyTypeDef",
    "CreateConfiguredTableAssociationAnalysisRuleInputRequestTypeDef",
    "UpdateConfiguredTableAssociationAnalysisRuleInputRequestTypeDef",
    "ConfiguredTableAnalysisRuleTypeDef",
    "ConfiguredTableAnalysisRulePolicyV1TypeDef",
    "AnalysisRuleTypeDef",
    "CreateConfiguredTableAnalysisRuleOutputTypeDef",
    "GetConfiguredTableAnalysisRuleOutputTypeDef",
    "UpdateConfiguredTableAnalysisRuleOutputTypeDef",
    "ConfiguredTableAnalysisRulePolicyV1UnionTypeDef",
    "BatchGetSchemaAnalysisRuleOutputTypeDef",
    "GetSchemaAnalysisRuleOutputTypeDef",
    "ConfiguredTableAnalysisRulePolicyTypeDef",
    "CreateConfiguredTableAnalysisRuleInputRequestTypeDef",
    "UpdateConfiguredTableAnalysisRuleInputRequestTypeDef",
)

AggregateColumnOutputTypeDef = TypedDict(
    "AggregateColumnOutputTypeDef",
    {
        "columnNames": List[str],
        "function": AggregateFunctionNameType,
    },
)
AggregateColumnTypeDef = TypedDict(
    "AggregateColumnTypeDef",
    {
        "columnNames": Sequence[str],
        "function": AggregateFunctionNameType,
    },
)
AggregationConstraintTypeDef = TypedDict(
    "AggregationConstraintTypeDef",
    {
        "columnName": str,
        "minimum": int,
        "type": Literal["COUNT_DISTINCT"],
    },
)
AnalysisParameterTypeDef = TypedDict(
    "AnalysisParameterTypeDef",
    {
        "name": str,
        "type": ParameterTypeType,
        "defaultValue": NotRequired[str],
    },
)
AnalysisRuleListOutputTypeDef = TypedDict(
    "AnalysisRuleListOutputTypeDef",
    {
        "joinColumns": List[str],
        "listColumns": List[str],
        "allowedJoinOperators": NotRequired[List[JoinOperatorType]],
        "additionalAnalyses": NotRequired[AdditionalAnalysesType],
    },
)
AnalysisRuleListTypeDef = TypedDict(
    "AnalysisRuleListTypeDef",
    {
        "joinColumns": Sequence[str],
        "listColumns": Sequence[str],
        "allowedJoinOperators": NotRequired[Sequence[JoinOperatorType]],
        "additionalAnalyses": NotRequired[AdditionalAnalysesType],
    },
)
AnalysisSchemaTypeDef = TypedDict(
    "AnalysisSchemaTypeDef",
    {
        "referencedTables": NotRequired[List[str]],
    },
)
AnalysisSourceTypeDef = TypedDict(
    "AnalysisSourceTypeDef",
    {
        "text": NotRequired[str],
    },
)
AnalysisTemplateSummaryTypeDef = TypedDict(
    "AnalysisTemplateSummaryTypeDef",
    {
        "arn": str,
        "createTime": datetime,
        "id": str,
        "name": str,
        "updateTime": datetime,
        "membershipArn": str,
        "membershipId": str,
        "collaborationArn": str,
        "collaborationId": str,
        "description": NotRequired[str],
    },
)
AnalysisTemplateValidationStatusReasonTypeDef = TypedDict(
    "AnalysisTemplateValidationStatusReasonTypeDef",
    {
        "message": str,
    },
)
BatchGetCollaborationAnalysisTemplateErrorTypeDef = TypedDict(
    "BatchGetCollaborationAnalysisTemplateErrorTypeDef",
    {
        "arn": str,
        "code": str,
        "message": str,
    },
)
BatchGetCollaborationAnalysisTemplateInputRequestTypeDef = TypedDict(
    "BatchGetCollaborationAnalysisTemplateInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
        "analysisTemplateArns": Sequence[str],
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
BatchGetSchemaAnalysisRuleErrorTypeDef = TypedDict(
    "BatchGetSchemaAnalysisRuleErrorTypeDef",
    {
        "name": str,
        "type": AnalysisRuleTypeType,
        "code": str,
        "message": str,
    },
)
SchemaAnalysisRuleRequestTypeDef = TypedDict(
    "SchemaAnalysisRuleRequestTypeDef",
    {
        "name": str,
        "type": AnalysisRuleTypeType,
    },
)
BatchGetSchemaErrorTypeDef = TypedDict(
    "BatchGetSchemaErrorTypeDef",
    {
        "name": str,
        "code": str,
        "message": str,
    },
)
BatchGetSchemaInputRequestTypeDef = TypedDict(
    "BatchGetSchemaInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
        "names": Sequence[str],
    },
)
CollaborationAnalysisTemplateSummaryTypeDef = TypedDict(
    "CollaborationAnalysisTemplateSummaryTypeDef",
    {
        "arn": str,
        "createTime": datetime,
        "id": str,
        "name": str,
        "updateTime": datetime,
        "collaborationArn": str,
        "collaborationId": str,
        "creatorAccountId": str,
        "description": NotRequired[str],
    },
)
CollaborationConfiguredAudienceModelAssociationSummaryTypeDef = TypedDict(
    "CollaborationConfiguredAudienceModelAssociationSummaryTypeDef",
    {
        "arn": str,
        "createTime": datetime,
        "id": str,
        "name": str,
        "updateTime": datetime,
        "collaborationArn": str,
        "collaborationId": str,
        "creatorAccountId": str,
        "description": NotRequired[str],
    },
)
CollaborationConfiguredAudienceModelAssociationTypeDef = TypedDict(
    "CollaborationConfiguredAudienceModelAssociationTypeDef",
    {
        "id": str,
        "arn": str,
        "collaborationId": str,
        "collaborationArn": str,
        "configuredAudienceModelArn": str,
        "name": str,
        "creatorAccountId": str,
        "createTime": datetime,
        "updateTime": datetime,
        "description": NotRequired[str],
    },
)
IdNamespaceAssociationInputReferenceConfigTypeDef = TypedDict(
    "IdNamespaceAssociationInputReferenceConfigTypeDef",
    {
        "inputReferenceArn": str,
        "manageResourcePolicies": bool,
    },
)
IdNamespaceAssociationInputReferencePropertiesSummaryTypeDef = TypedDict(
    "IdNamespaceAssociationInputReferencePropertiesSummaryTypeDef",
    {
        "idNamespaceType": IdNamespaceTypeType,
    },
)
IdMappingConfigTypeDef = TypedDict(
    "IdMappingConfigTypeDef",
    {
        "allowUseAsDimensionColumn": bool,
    },
)
IdNamespaceAssociationInputReferencePropertiesTypeDef = TypedDict(
    "IdNamespaceAssociationInputReferencePropertiesTypeDef",
    {
        "idNamespaceType": IdNamespaceTypeType,
        "idMappingWorkflowsSupported": List[Dict[str, Any]],
    },
)
CollaborationPrivacyBudgetTemplateSummaryTypeDef = TypedDict(
    "CollaborationPrivacyBudgetTemplateSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "collaborationId": str,
        "collaborationArn": str,
        "creatorAccountId": str,
        "privacyBudgetType": Literal["DIFFERENTIAL_PRIVACY"],
        "createTime": datetime,
        "updateTime": datetime,
    },
)
CollaborationSummaryTypeDef = TypedDict(
    "CollaborationSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "creatorAccountId": str,
        "creatorDisplayName": str,
        "createTime": datetime,
        "updateTime": datetime,
        "memberStatus": MemberStatusType,
        "membershipId": NotRequired[str],
        "membershipArn": NotRequired[str],
    },
)
DataEncryptionMetadataTypeDef = TypedDict(
    "DataEncryptionMetadataTypeDef",
    {
        "allowCleartext": bool,
        "allowDuplicates": bool,
        "allowJoinsOnColumnsWithDifferentNames": bool,
        "preserveNulls": bool,
    },
)
ColumnTypeDef = TypedDict(
    "ColumnTypeDef",
    {
        "name": str,
        "type": str,
    },
)
DirectAnalysisConfigurationDetailsTypeDef = TypedDict(
    "DirectAnalysisConfigurationDetailsTypeDef",
    {
        "receiverAccountIds": NotRequired[List[str]],
    },
)
ConfiguredAudienceModelAssociationSummaryTypeDef = TypedDict(
    "ConfiguredAudienceModelAssociationSummaryTypeDef",
    {
        "membershipId": str,
        "membershipArn": str,
        "collaborationArn": str,
        "collaborationId": str,
        "createTime": datetime,
        "updateTime": datetime,
        "id": str,
        "arn": str,
        "name": str,
        "configuredAudienceModelArn": str,
        "description": NotRequired[str],
    },
)
ConfiguredAudienceModelAssociationTypeDef = TypedDict(
    "ConfiguredAudienceModelAssociationTypeDef",
    {
        "id": str,
        "arn": str,
        "configuredAudienceModelArn": str,
        "membershipId": str,
        "membershipArn": str,
        "collaborationId": str,
        "collaborationArn": str,
        "name": str,
        "manageResourcePolicies": bool,
        "createTime": datetime,
        "updateTime": datetime,
        "description": NotRequired[str],
    },
)
ConfiguredTableAssociationAnalysisRuleAggregationOutputTypeDef = TypedDict(
    "ConfiguredTableAssociationAnalysisRuleAggregationOutputTypeDef",
    {
        "allowedResultReceivers": NotRequired[List[str]],
        "allowedAdditionalAnalyses": NotRequired[List[str]],
    },
)
ConfiguredTableAssociationAnalysisRuleAggregationTypeDef = TypedDict(
    "ConfiguredTableAssociationAnalysisRuleAggregationTypeDef",
    {
        "allowedResultReceivers": NotRequired[Sequence[str]],
        "allowedAdditionalAnalyses": NotRequired[Sequence[str]],
    },
)
ConfiguredTableAssociationAnalysisRuleCustomOutputTypeDef = TypedDict(
    "ConfiguredTableAssociationAnalysisRuleCustomOutputTypeDef",
    {
        "allowedResultReceivers": NotRequired[List[str]],
        "allowedAdditionalAnalyses": NotRequired[List[str]],
    },
)
ConfiguredTableAssociationAnalysisRuleCustomTypeDef = TypedDict(
    "ConfiguredTableAssociationAnalysisRuleCustomTypeDef",
    {
        "allowedResultReceivers": NotRequired[Sequence[str]],
        "allowedAdditionalAnalyses": NotRequired[Sequence[str]],
    },
)
ConfiguredTableAssociationAnalysisRuleListOutputTypeDef = TypedDict(
    "ConfiguredTableAssociationAnalysisRuleListOutputTypeDef",
    {
        "allowedResultReceivers": NotRequired[List[str]],
        "allowedAdditionalAnalyses": NotRequired[List[str]],
    },
)
ConfiguredTableAssociationAnalysisRuleListTypeDef = TypedDict(
    "ConfiguredTableAssociationAnalysisRuleListTypeDef",
    {
        "allowedResultReceivers": NotRequired[Sequence[str]],
        "allowedAdditionalAnalyses": NotRequired[Sequence[str]],
    },
)
ConfiguredTableAssociationSummaryTypeDef = TypedDict(
    "ConfiguredTableAssociationSummaryTypeDef",
    {
        "configuredTableId": str,
        "membershipId": str,
        "membershipArn": str,
        "name": str,
        "createTime": datetime,
        "updateTime": datetime,
        "id": str,
        "arn": str,
    },
)
ConfiguredTableAssociationTypeDef = TypedDict(
    "ConfiguredTableAssociationTypeDef",
    {
        "arn": str,
        "id": str,
        "configuredTableId": str,
        "configuredTableArn": str,
        "membershipId": str,
        "membershipArn": str,
        "roleArn": str,
        "name": str,
        "createTime": datetime,
        "updateTime": datetime,
        "description": NotRequired[str],
        "analysisRuleTypes": NotRequired[List[ConfiguredTableAssociationAnalysisRuleTypeType]],
    },
)
ConfiguredTableSummaryTypeDef = TypedDict(
    "ConfiguredTableSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "createTime": datetime,
        "updateTime": datetime,
        "analysisRuleTypes": List[ConfiguredTableAnalysisRuleTypeType],
        "analysisMethod": Literal["DIRECT_QUERY"],
    },
)
CreateConfiguredAudienceModelAssociationInputRequestTypeDef = TypedDict(
    "CreateConfiguredAudienceModelAssociationInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "configuredAudienceModelArn": str,
        "configuredAudienceModelAssociationName": str,
        "manageResourcePolicies": bool,
        "tags": NotRequired[Mapping[str, str]],
        "description": NotRequired[str],
    },
)
CreateConfiguredTableAssociationInputRequestTypeDef = TypedDict(
    "CreateConfiguredTableAssociationInputRequestTypeDef",
    {
        "name": str,
        "membershipIdentifier": str,
        "configuredTableIdentifier": str,
        "roleArn": str,
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
IdMappingTableInputReferenceConfigTypeDef = TypedDict(
    "IdMappingTableInputReferenceConfigTypeDef",
    {
        "inputReferenceArn": str,
        "manageResourcePolicies": bool,
    },
)
DeleteAnalysisTemplateInputRequestTypeDef = TypedDict(
    "DeleteAnalysisTemplateInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "analysisTemplateIdentifier": str,
    },
)
DeleteCollaborationInputRequestTypeDef = TypedDict(
    "DeleteCollaborationInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
    },
)
DeleteConfiguredAudienceModelAssociationInputRequestTypeDef = TypedDict(
    "DeleteConfiguredAudienceModelAssociationInputRequestTypeDef",
    {
        "configuredAudienceModelAssociationIdentifier": str,
        "membershipIdentifier": str,
    },
)
DeleteConfiguredTableAnalysisRuleInputRequestTypeDef = TypedDict(
    "DeleteConfiguredTableAnalysisRuleInputRequestTypeDef",
    {
        "configuredTableIdentifier": str,
        "analysisRuleType": ConfiguredTableAnalysisRuleTypeType,
    },
)
DeleteConfiguredTableAssociationAnalysisRuleInputRequestTypeDef = TypedDict(
    "DeleteConfiguredTableAssociationAnalysisRuleInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "configuredTableAssociationIdentifier": str,
        "analysisRuleType": ConfiguredTableAssociationAnalysisRuleTypeType,
    },
)
DeleteConfiguredTableAssociationInputRequestTypeDef = TypedDict(
    "DeleteConfiguredTableAssociationInputRequestTypeDef",
    {
        "configuredTableAssociationIdentifier": str,
        "membershipIdentifier": str,
    },
)
DeleteConfiguredTableInputRequestTypeDef = TypedDict(
    "DeleteConfiguredTableInputRequestTypeDef",
    {
        "configuredTableIdentifier": str,
    },
)
DeleteIdMappingTableInputRequestTypeDef = TypedDict(
    "DeleteIdMappingTableInputRequestTypeDef",
    {
        "idMappingTableIdentifier": str,
        "membershipIdentifier": str,
    },
)
DeleteIdNamespaceAssociationInputRequestTypeDef = TypedDict(
    "DeleteIdNamespaceAssociationInputRequestTypeDef",
    {
        "idNamespaceAssociationIdentifier": str,
        "membershipIdentifier": str,
    },
)
DeleteMemberInputRequestTypeDef = TypedDict(
    "DeleteMemberInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
        "accountId": str,
    },
)
DeleteMembershipInputRequestTypeDef = TypedDict(
    "DeleteMembershipInputRequestTypeDef",
    {
        "membershipIdentifier": str,
    },
)
DeletePrivacyBudgetTemplateInputRequestTypeDef = TypedDict(
    "DeletePrivacyBudgetTemplateInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "privacyBudgetTemplateIdentifier": str,
    },
)
DifferentialPrivacyColumnTypeDef = TypedDict(
    "DifferentialPrivacyColumnTypeDef",
    {
        "name": str,
    },
)
DifferentialPrivacySensitivityParametersTypeDef = TypedDict(
    "DifferentialPrivacySensitivityParametersTypeDef",
    {
        "aggregationType": DifferentialPrivacyAggregationTypeType,
        "aggregationExpression": str,
        "userContributionLimit": int,
        "minColumnValue": NotRequired[float],
        "maxColumnValue": NotRequired[float],
    },
)
DifferentialPrivacyPreviewAggregationTypeDef = TypedDict(
    "DifferentialPrivacyPreviewAggregationTypeDef",
    {
        "type": DifferentialPrivacyAggregationTypeType,
        "maxCount": int,
    },
)
DifferentialPrivacyPreviewParametersInputTypeDef = TypedDict(
    "DifferentialPrivacyPreviewParametersInputTypeDef",
    {
        "epsilon": int,
        "usersNoisePerQuery": int,
    },
)
DifferentialPrivacyPrivacyBudgetAggregationTypeDef = TypedDict(
    "DifferentialPrivacyPrivacyBudgetAggregationTypeDef",
    {
        "type": DifferentialPrivacyAggregationTypeType,
        "maxCount": int,
        "remainingCount": int,
    },
)
DifferentialPrivacyTemplateParametersInputTypeDef = TypedDict(
    "DifferentialPrivacyTemplateParametersInputTypeDef",
    {
        "epsilon": int,
        "usersNoisePerQuery": int,
    },
)
DifferentialPrivacyTemplateParametersOutputTypeDef = TypedDict(
    "DifferentialPrivacyTemplateParametersOutputTypeDef",
    {
        "epsilon": int,
        "usersNoisePerQuery": int,
    },
)
DifferentialPrivacyTemplateUpdateParametersTypeDef = TypedDict(
    "DifferentialPrivacyTemplateUpdateParametersTypeDef",
    {
        "epsilon": NotRequired[int],
        "usersNoisePerQuery": NotRequired[int],
    },
)
GetAnalysisTemplateInputRequestTypeDef = TypedDict(
    "GetAnalysisTemplateInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "analysisTemplateIdentifier": str,
    },
)
GetCollaborationAnalysisTemplateInputRequestTypeDef = TypedDict(
    "GetCollaborationAnalysisTemplateInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
        "analysisTemplateArn": str,
    },
)
GetCollaborationConfiguredAudienceModelAssociationInputRequestTypeDef = TypedDict(
    "GetCollaborationConfiguredAudienceModelAssociationInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
        "configuredAudienceModelAssociationIdentifier": str,
    },
)
GetCollaborationIdNamespaceAssociationInputRequestTypeDef = TypedDict(
    "GetCollaborationIdNamespaceAssociationInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
        "idNamespaceAssociationIdentifier": str,
    },
)
GetCollaborationInputRequestTypeDef = TypedDict(
    "GetCollaborationInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
    },
)
GetCollaborationPrivacyBudgetTemplateInputRequestTypeDef = TypedDict(
    "GetCollaborationPrivacyBudgetTemplateInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
        "privacyBudgetTemplateIdentifier": str,
    },
)
GetConfiguredAudienceModelAssociationInputRequestTypeDef = TypedDict(
    "GetConfiguredAudienceModelAssociationInputRequestTypeDef",
    {
        "configuredAudienceModelAssociationIdentifier": str,
        "membershipIdentifier": str,
    },
)
GetConfiguredTableAnalysisRuleInputRequestTypeDef = TypedDict(
    "GetConfiguredTableAnalysisRuleInputRequestTypeDef",
    {
        "configuredTableIdentifier": str,
        "analysisRuleType": ConfiguredTableAnalysisRuleTypeType,
    },
)
GetConfiguredTableAssociationAnalysisRuleInputRequestTypeDef = TypedDict(
    "GetConfiguredTableAssociationAnalysisRuleInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "configuredTableAssociationIdentifier": str,
        "analysisRuleType": ConfiguredTableAssociationAnalysisRuleTypeType,
    },
)
GetConfiguredTableAssociationInputRequestTypeDef = TypedDict(
    "GetConfiguredTableAssociationInputRequestTypeDef",
    {
        "configuredTableAssociationIdentifier": str,
        "membershipIdentifier": str,
    },
)
GetConfiguredTableInputRequestTypeDef = TypedDict(
    "GetConfiguredTableInputRequestTypeDef",
    {
        "configuredTableIdentifier": str,
    },
)
GetIdMappingTableInputRequestTypeDef = TypedDict(
    "GetIdMappingTableInputRequestTypeDef",
    {
        "idMappingTableIdentifier": str,
        "membershipIdentifier": str,
    },
)
GetIdNamespaceAssociationInputRequestTypeDef = TypedDict(
    "GetIdNamespaceAssociationInputRequestTypeDef",
    {
        "idNamespaceAssociationIdentifier": str,
        "membershipIdentifier": str,
    },
)
GetMembershipInputRequestTypeDef = TypedDict(
    "GetMembershipInputRequestTypeDef",
    {
        "membershipIdentifier": str,
    },
)
GetPrivacyBudgetTemplateInputRequestTypeDef = TypedDict(
    "GetPrivacyBudgetTemplateInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "privacyBudgetTemplateIdentifier": str,
    },
)
GetProtectedQueryInputRequestTypeDef = TypedDict(
    "GetProtectedQueryInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "protectedQueryIdentifier": str,
    },
)
GetSchemaAnalysisRuleInputRequestTypeDef = TypedDict(
    "GetSchemaAnalysisRuleInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
        "name": str,
        "type": AnalysisRuleTypeType,
    },
)
GetSchemaInputRequestTypeDef = TypedDict(
    "GetSchemaInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
        "name": str,
    },
)
GlueTableReferenceTypeDef = TypedDict(
    "GlueTableReferenceTypeDef",
    {
        "tableName": str,
        "databaseName": str,
    },
)
IdMappingTableInputSourceTypeDef = TypedDict(
    "IdMappingTableInputSourceTypeDef",
    {
        "idNamespaceAssociationId": str,
        "type": IdNamespaceTypeType,
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
ListAnalysisTemplatesInputRequestTypeDef = TypedDict(
    "ListAnalysisTemplatesInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListCollaborationAnalysisTemplatesInputRequestTypeDef = TypedDict(
    "ListCollaborationAnalysisTemplatesInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListCollaborationConfiguredAudienceModelAssociationsInputRequestTypeDef = TypedDict(
    "ListCollaborationConfiguredAudienceModelAssociationsInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListCollaborationIdNamespaceAssociationsInputRequestTypeDef = TypedDict(
    "ListCollaborationIdNamespaceAssociationsInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListCollaborationPrivacyBudgetTemplatesInputRequestTypeDef = TypedDict(
    "ListCollaborationPrivacyBudgetTemplatesInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListCollaborationPrivacyBudgetsInputRequestTypeDef = TypedDict(
    "ListCollaborationPrivacyBudgetsInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
        "privacyBudgetType": Literal["DIFFERENTIAL_PRIVACY"],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListCollaborationsInputRequestTypeDef = TypedDict(
    "ListCollaborationsInputRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "memberStatus": NotRequired[FilterableMemberStatusType],
    },
)
ListConfiguredAudienceModelAssociationsInputRequestTypeDef = TypedDict(
    "ListConfiguredAudienceModelAssociationsInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListConfiguredTableAssociationsInputRequestTypeDef = TypedDict(
    "ListConfiguredTableAssociationsInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListConfiguredTablesInputRequestTypeDef = TypedDict(
    "ListConfiguredTablesInputRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListIdMappingTablesInputRequestTypeDef = TypedDict(
    "ListIdMappingTablesInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListIdNamespaceAssociationsInputRequestTypeDef = TypedDict(
    "ListIdNamespaceAssociationsInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListMembersInputRequestTypeDef = TypedDict(
    "ListMembersInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListMembershipsInputRequestTypeDef = TypedDict(
    "ListMembershipsInputRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "status": NotRequired[MembershipStatusType],
    },
)
ListPrivacyBudgetTemplatesInputRequestTypeDef = TypedDict(
    "ListPrivacyBudgetTemplatesInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
PrivacyBudgetTemplateSummaryTypeDef = TypedDict(
    "PrivacyBudgetTemplateSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "membershipId": str,
        "membershipArn": str,
        "collaborationId": str,
        "collaborationArn": str,
        "privacyBudgetType": Literal["DIFFERENTIAL_PRIVACY"],
        "createTime": datetime,
        "updateTime": datetime,
    },
)
ListPrivacyBudgetsInputRequestTypeDef = TypedDict(
    "ListPrivacyBudgetsInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "privacyBudgetType": Literal["DIFFERENTIAL_PRIVACY"],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListProtectedQueriesInputRequestTypeDef = TypedDict(
    "ListProtectedQueriesInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "status": NotRequired[ProtectedQueryStatusType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListSchemasInputRequestTypeDef = TypedDict(
    "ListSchemasInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
        "schemaType": NotRequired[SchemaTypeType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
SchemaSummaryTypeDef = TypedDict(
    "SchemaSummaryTypeDef",
    {
        "name": str,
        "type": SchemaTypeType,
        "creatorAccountId": str,
        "createTime": datetime,
        "updateTime": datetime,
        "collaborationId": str,
        "collaborationArn": str,
        "analysisRuleTypes": List[AnalysisRuleTypeType],
        "analysisMethod": NotRequired[Literal["DIRECT_QUERY"]],
    },
)
ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)
MembershipQueryComputePaymentConfigTypeDef = TypedDict(
    "MembershipQueryComputePaymentConfigTypeDef",
    {
        "isResponsible": bool,
    },
)
ProtectedQueryS3OutputConfigurationTypeDef = TypedDict(
    "ProtectedQueryS3OutputConfigurationTypeDef",
    {
        "resultFormat": ResultFormatType,
        "bucket": str,
        "keyPrefix": NotRequired[str],
    },
)
QueryComputePaymentConfigTypeDef = TypedDict(
    "QueryComputePaymentConfigTypeDef",
    {
        "isResponsible": bool,
    },
)
PopulateIdMappingTableInputRequestTypeDef = TypedDict(
    "PopulateIdMappingTableInputRequestTypeDef",
    {
        "idMappingTableIdentifier": str,
        "membershipIdentifier": str,
    },
)
ProtectedQueryErrorTypeDef = TypedDict(
    "ProtectedQueryErrorTypeDef",
    {
        "message": str,
        "code": str,
    },
)
ProtectedQueryMemberOutputConfigurationTypeDef = TypedDict(
    "ProtectedQueryMemberOutputConfigurationTypeDef",
    {
        "accountId": str,
    },
)
ProtectedQueryS3OutputTypeDef = TypedDict(
    "ProtectedQueryS3OutputTypeDef",
    {
        "location": str,
    },
)
ProtectedQuerySingleMemberOutputTypeDef = TypedDict(
    "ProtectedQuerySingleMemberOutputTypeDef",
    {
        "accountId": str,
    },
)
ProtectedQuerySQLParametersOutputTypeDef = TypedDict(
    "ProtectedQuerySQLParametersOutputTypeDef",
    {
        "queryString": NotRequired[str],
        "analysisTemplateArn": NotRequired[str],
        "parameters": NotRequired[Dict[str, str]],
    },
)
ProtectedQuerySQLParametersTypeDef = TypedDict(
    "ProtectedQuerySQLParametersTypeDef",
    {
        "queryString": NotRequired[str],
        "analysisTemplateArn": NotRequired[str],
        "parameters": NotRequired[Mapping[str, str]],
    },
)
ProtectedQueryStatisticsTypeDef = TypedDict(
    "ProtectedQueryStatisticsTypeDef",
    {
        "totalDurationInMillis": NotRequired[int],
    },
)
QueryConstraintRequireOverlapTypeDef = TypedDict(
    "QueryConstraintRequireOverlapTypeDef",
    {
        "columns": NotRequired[List[str]],
    },
)
SchemaStatusReasonTypeDef = TypedDict(
    "SchemaStatusReasonTypeDef",
    {
        "code": SchemaStatusReasonCodeType,
        "message": str,
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
UpdateAnalysisTemplateInputRequestTypeDef = TypedDict(
    "UpdateAnalysisTemplateInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "analysisTemplateIdentifier": str,
        "description": NotRequired[str],
    },
)
UpdateCollaborationInputRequestTypeDef = TypedDict(
    "UpdateCollaborationInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
    },
)
UpdateConfiguredAudienceModelAssociationInputRequestTypeDef = TypedDict(
    "UpdateConfiguredAudienceModelAssociationInputRequestTypeDef",
    {
        "configuredAudienceModelAssociationIdentifier": str,
        "membershipIdentifier": str,
        "description": NotRequired[str],
        "name": NotRequired[str],
    },
)
UpdateConfiguredTableAssociationInputRequestTypeDef = TypedDict(
    "UpdateConfiguredTableAssociationInputRequestTypeDef",
    {
        "configuredTableAssociationIdentifier": str,
        "membershipIdentifier": str,
        "description": NotRequired[str],
        "roleArn": NotRequired[str],
    },
)
UpdateConfiguredTableInputRequestTypeDef = TypedDict(
    "UpdateConfiguredTableInputRequestTypeDef",
    {
        "configuredTableIdentifier": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
    },
)
UpdateIdMappingTableInputRequestTypeDef = TypedDict(
    "UpdateIdMappingTableInputRequestTypeDef",
    {
        "idMappingTableIdentifier": str,
        "membershipIdentifier": str,
        "description": NotRequired[str],
        "kmsKeyArn": NotRequired[str],
    },
)
UpdateProtectedQueryInputRequestTypeDef = TypedDict(
    "UpdateProtectedQueryInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "protectedQueryIdentifier": str,
        "targetStatus": Literal["CANCELLED"],
    },
)
AggregateColumnUnionTypeDef = Union[AggregateColumnTypeDef, AggregateColumnOutputTypeDef]
AnalysisRuleAggregationOutputTypeDef = TypedDict(
    "AnalysisRuleAggregationOutputTypeDef",
    {
        "aggregateColumns": List[AggregateColumnOutputTypeDef],
        "joinColumns": List[str],
        "dimensionColumns": List[str],
        "scalarFunctions": List[ScalarFunctionsType],
        "outputConstraints": List[AggregationConstraintTypeDef],
        "joinRequired": NotRequired[Literal["QUERY_RUNNER"]],
        "allowedJoinOperators": NotRequired[List[JoinOperatorType]],
        "additionalAnalyses": NotRequired[AdditionalAnalysesType],
    },
)
AnalysisRuleListUnionTypeDef = Union[AnalysisRuleListTypeDef, AnalysisRuleListOutputTypeDef]
CreateAnalysisTemplateInputRequestTypeDef = TypedDict(
    "CreateAnalysisTemplateInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "name": str,
        "format": Literal["SQL"],
        "source": AnalysisSourceTypeDef,
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "analysisParameters": NotRequired[Sequence[AnalysisParameterTypeDef]],
    },
)
AnalysisTemplateValidationStatusDetailTypeDef = TypedDict(
    "AnalysisTemplateValidationStatusDetailTypeDef",
    {
        "type": Literal["DIFFERENTIAL_PRIVACY"],
        "status": AnalysisTemplateValidationStatusType,
        "reasons": NotRequired[List[AnalysisTemplateValidationStatusReasonTypeDef]],
    },
)
ListAnalysisTemplatesOutputTypeDef = TypedDict(
    "ListAnalysisTemplatesOutputTypeDef",
    {
        "nextToken": str,
        "analysisTemplateSummaries": List[AnalysisTemplateSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PopulateIdMappingTableOutputTypeDef = TypedDict(
    "PopulateIdMappingTableOutputTypeDef",
    {
        "idMappingJobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetSchemaAnalysisRuleInputRequestTypeDef = TypedDict(
    "BatchGetSchemaAnalysisRuleInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
        "schemaAnalysisRuleRequests": Sequence[SchemaAnalysisRuleRequestTypeDef],
    },
)
ListCollaborationAnalysisTemplatesOutputTypeDef = TypedDict(
    "ListCollaborationAnalysisTemplatesOutputTypeDef",
    {
        "nextToken": str,
        "collaborationAnalysisTemplateSummaries": List[CollaborationAnalysisTemplateSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCollaborationConfiguredAudienceModelAssociationsOutputTypeDef = TypedDict(
    "ListCollaborationConfiguredAudienceModelAssociationsOutputTypeDef",
    {
        "collaborationConfiguredAudienceModelAssociationSummaries": List[
            CollaborationConfiguredAudienceModelAssociationSummaryTypeDef
        ],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCollaborationConfiguredAudienceModelAssociationOutputTypeDef = TypedDict(
    "GetCollaborationConfiguredAudienceModelAssociationOutputTypeDef",
    {
        "collaborationConfiguredAudienceModelAssociation": CollaborationConfiguredAudienceModelAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CollaborationIdNamespaceAssociationSummaryTypeDef = TypedDict(
    "CollaborationIdNamespaceAssociationSummaryTypeDef",
    {
        "arn": str,
        "createTime": datetime,
        "id": str,
        "updateTime": datetime,
        "collaborationArn": str,
        "collaborationId": str,
        "creatorAccountId": str,
        "inputReferenceConfig": IdNamespaceAssociationInputReferenceConfigTypeDef,
        "name": str,
        "inputReferenceProperties": IdNamespaceAssociationInputReferencePropertiesSummaryTypeDef,
        "description": NotRequired[str],
    },
)
IdNamespaceAssociationSummaryTypeDef = TypedDict(
    "IdNamespaceAssociationSummaryTypeDef",
    {
        "membershipId": str,
        "membershipArn": str,
        "collaborationArn": str,
        "collaborationId": str,
        "createTime": datetime,
        "updateTime": datetime,
        "id": str,
        "arn": str,
        "inputReferenceConfig": IdNamespaceAssociationInputReferenceConfigTypeDef,
        "name": str,
        "inputReferenceProperties": IdNamespaceAssociationInputReferencePropertiesSummaryTypeDef,
        "description": NotRequired[str],
    },
)
CreateIdNamespaceAssociationInputRequestTypeDef = TypedDict(
    "CreateIdNamespaceAssociationInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "inputReferenceConfig": IdNamespaceAssociationInputReferenceConfigTypeDef,
        "name": str,
        "tags": NotRequired[Mapping[str, str]],
        "description": NotRequired[str],
        "idMappingConfig": NotRequired[IdMappingConfigTypeDef],
    },
)
UpdateIdNamespaceAssociationInputRequestTypeDef = TypedDict(
    "UpdateIdNamespaceAssociationInputRequestTypeDef",
    {
        "idNamespaceAssociationIdentifier": str,
        "membershipIdentifier": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "idMappingConfig": NotRequired[IdMappingConfigTypeDef],
    },
)
CollaborationIdNamespaceAssociationTypeDef = TypedDict(
    "CollaborationIdNamespaceAssociationTypeDef",
    {
        "id": str,
        "arn": str,
        "collaborationId": str,
        "collaborationArn": str,
        "name": str,
        "creatorAccountId": str,
        "createTime": datetime,
        "updateTime": datetime,
        "inputReferenceConfig": IdNamespaceAssociationInputReferenceConfigTypeDef,
        "inputReferenceProperties": IdNamespaceAssociationInputReferencePropertiesTypeDef,
        "description": NotRequired[str],
        "idMappingConfig": NotRequired[IdMappingConfigTypeDef],
    },
)
IdNamespaceAssociationTypeDef = TypedDict(
    "IdNamespaceAssociationTypeDef",
    {
        "id": str,
        "arn": str,
        "membershipId": str,
        "membershipArn": str,
        "collaborationId": str,
        "collaborationArn": str,
        "name": str,
        "createTime": datetime,
        "updateTime": datetime,
        "inputReferenceConfig": IdNamespaceAssociationInputReferenceConfigTypeDef,
        "inputReferenceProperties": IdNamespaceAssociationInputReferencePropertiesTypeDef,
        "description": NotRequired[str],
        "idMappingConfig": NotRequired[IdMappingConfigTypeDef],
    },
)
ListCollaborationPrivacyBudgetTemplatesOutputTypeDef = TypedDict(
    "ListCollaborationPrivacyBudgetTemplatesOutputTypeDef",
    {
        "nextToken": str,
        "collaborationPrivacyBudgetTemplateSummaries": List[
            CollaborationPrivacyBudgetTemplateSummaryTypeDef
        ],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCollaborationsOutputTypeDef = TypedDict(
    "ListCollaborationsOutputTypeDef",
    {
        "nextToken": str,
        "collaborationList": List[CollaborationSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CollaborationTypeDef = TypedDict(
    "CollaborationTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "creatorAccountId": str,
        "creatorDisplayName": str,
        "createTime": datetime,
        "updateTime": datetime,
        "memberStatus": MemberStatusType,
        "queryLogStatus": CollaborationQueryLogStatusType,
        "description": NotRequired[str],
        "membershipId": NotRequired[str],
        "membershipArn": NotRequired[str],
        "dataEncryptionMetadata": NotRequired[DataEncryptionMetadataTypeDef],
    },
)
ConfigurationDetailsTypeDef = TypedDict(
    "ConfigurationDetailsTypeDef",
    {
        "directAnalysisConfigurationDetails": NotRequired[
            DirectAnalysisConfigurationDetailsTypeDef
        ],
    },
)
ListConfiguredAudienceModelAssociationsOutputTypeDef = TypedDict(
    "ListConfiguredAudienceModelAssociationsOutputTypeDef",
    {
        "configuredAudienceModelAssociationSummaries": List[
            ConfiguredAudienceModelAssociationSummaryTypeDef
        ],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateConfiguredAudienceModelAssociationOutputTypeDef = TypedDict(
    "CreateConfiguredAudienceModelAssociationOutputTypeDef",
    {
        "configuredAudienceModelAssociation": ConfiguredAudienceModelAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetConfiguredAudienceModelAssociationOutputTypeDef = TypedDict(
    "GetConfiguredAudienceModelAssociationOutputTypeDef",
    {
        "configuredAudienceModelAssociation": ConfiguredAudienceModelAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateConfiguredAudienceModelAssociationOutputTypeDef = TypedDict(
    "UpdateConfiguredAudienceModelAssociationOutputTypeDef",
    {
        "configuredAudienceModelAssociation": ConfiguredAudienceModelAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConfiguredTableAssociationAnalysisRuleAggregationUnionTypeDef = Union[
    ConfiguredTableAssociationAnalysisRuleAggregationTypeDef,
    ConfiguredTableAssociationAnalysisRuleAggregationOutputTypeDef,
]
ConfiguredTableAssociationAnalysisRuleCustomUnionTypeDef = Union[
    ConfiguredTableAssociationAnalysisRuleCustomTypeDef,
    ConfiguredTableAssociationAnalysisRuleCustomOutputTypeDef,
]
ConfiguredTableAssociationAnalysisRulePolicyV1OutputTypeDef = TypedDict(
    "ConfiguredTableAssociationAnalysisRulePolicyV1OutputTypeDef",
    {
        "list": NotRequired[ConfiguredTableAssociationAnalysisRuleListOutputTypeDef],
        "aggregation": NotRequired[ConfiguredTableAssociationAnalysisRuleAggregationOutputTypeDef],
        "custom": NotRequired[ConfiguredTableAssociationAnalysisRuleCustomOutputTypeDef],
    },
)
ConfiguredTableAssociationAnalysisRuleListUnionTypeDef = Union[
    ConfiguredTableAssociationAnalysisRuleListTypeDef,
    ConfiguredTableAssociationAnalysisRuleListOutputTypeDef,
]
ListConfiguredTableAssociationsOutputTypeDef = TypedDict(
    "ListConfiguredTableAssociationsOutputTypeDef",
    {
        "configuredTableAssociationSummaries": List[ConfiguredTableAssociationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateConfiguredTableAssociationOutputTypeDef = TypedDict(
    "CreateConfiguredTableAssociationOutputTypeDef",
    {
        "configuredTableAssociation": ConfiguredTableAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetConfiguredTableAssociationOutputTypeDef = TypedDict(
    "GetConfiguredTableAssociationOutputTypeDef",
    {
        "configuredTableAssociation": ConfiguredTableAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateConfiguredTableAssociationOutputTypeDef = TypedDict(
    "UpdateConfiguredTableAssociationOutputTypeDef",
    {
        "configuredTableAssociation": ConfiguredTableAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListConfiguredTablesOutputTypeDef = TypedDict(
    "ListConfiguredTablesOutputTypeDef",
    {
        "configuredTableSummaries": List[ConfiguredTableSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateIdMappingTableInputRequestTypeDef = TypedDict(
    "CreateIdMappingTableInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "name": str,
        "inputReferenceConfig": IdMappingTableInputReferenceConfigTypeDef,
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "kmsKeyArn": NotRequired[str],
    },
)
IdMappingTableSummaryTypeDef = TypedDict(
    "IdMappingTableSummaryTypeDef",
    {
        "collaborationArn": str,
        "collaborationId": str,
        "membershipId": str,
        "membershipArn": str,
        "createTime": datetime,
        "updateTime": datetime,
        "id": str,
        "arn": str,
        "inputReferenceConfig": IdMappingTableInputReferenceConfigTypeDef,
        "name": str,
        "description": NotRequired[str],
    },
)
DifferentialPrivacyConfigurationOutputTypeDef = TypedDict(
    "DifferentialPrivacyConfigurationOutputTypeDef",
    {
        "columns": List[DifferentialPrivacyColumnTypeDef],
    },
)
DifferentialPrivacyConfigurationTypeDef = TypedDict(
    "DifferentialPrivacyConfigurationTypeDef",
    {
        "columns": Sequence[DifferentialPrivacyColumnTypeDef],
    },
)
DifferentialPrivacyParametersTypeDef = TypedDict(
    "DifferentialPrivacyParametersTypeDef",
    {
        "sensitivityParameters": List[DifferentialPrivacySensitivityParametersTypeDef],
    },
)
DifferentialPrivacyPrivacyImpactTypeDef = TypedDict(
    "DifferentialPrivacyPrivacyImpactTypeDef",
    {
        "aggregations": List[DifferentialPrivacyPreviewAggregationTypeDef],
    },
)
PreviewPrivacyImpactParametersInputTypeDef = TypedDict(
    "PreviewPrivacyImpactParametersInputTypeDef",
    {
        "differentialPrivacy": NotRequired[DifferentialPrivacyPreviewParametersInputTypeDef],
    },
)
DifferentialPrivacyPrivacyBudgetTypeDef = TypedDict(
    "DifferentialPrivacyPrivacyBudgetTypeDef",
    {
        "aggregations": List[DifferentialPrivacyPrivacyBudgetAggregationTypeDef],
        "epsilon": int,
    },
)
PrivacyBudgetTemplateParametersInputTypeDef = TypedDict(
    "PrivacyBudgetTemplateParametersInputTypeDef",
    {
        "differentialPrivacy": NotRequired[DifferentialPrivacyTemplateParametersInputTypeDef],
    },
)
PrivacyBudgetTemplateParametersOutputTypeDef = TypedDict(
    "PrivacyBudgetTemplateParametersOutputTypeDef",
    {
        "differentialPrivacy": NotRequired[DifferentialPrivacyTemplateParametersOutputTypeDef],
    },
)
PrivacyBudgetTemplateUpdateParametersTypeDef = TypedDict(
    "PrivacyBudgetTemplateUpdateParametersTypeDef",
    {
        "differentialPrivacy": NotRequired[DifferentialPrivacyTemplateUpdateParametersTypeDef],
    },
)
TableReferenceTypeDef = TypedDict(
    "TableReferenceTypeDef",
    {
        "glue": NotRequired[GlueTableReferenceTypeDef],
    },
)
IdMappingTableInputReferencePropertiesTypeDef = TypedDict(
    "IdMappingTableInputReferencePropertiesTypeDef",
    {
        "idMappingTableInputSource": List[IdMappingTableInputSourceTypeDef],
    },
)
IdMappingTableSchemaTypePropertiesTypeDef = TypedDict(
    "IdMappingTableSchemaTypePropertiesTypeDef",
    {
        "idMappingTableInputSource": List[IdMappingTableInputSourceTypeDef],
    },
)
ListAnalysisTemplatesInputListAnalysisTemplatesPaginateTypeDef = TypedDict(
    "ListAnalysisTemplatesInputListAnalysisTemplatesPaginateTypeDef",
    {
        "membershipIdentifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCollaborationAnalysisTemplatesInputListCollaborationAnalysisTemplatesPaginateTypeDef = (
    TypedDict(
        "ListCollaborationAnalysisTemplatesInputListCollaborationAnalysisTemplatesPaginateTypeDef",
        {
            "collaborationIdentifier": str,
            "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
        },
    )
)
ListCollaborationConfiguredAudienceModelAssociationsInputListCollaborationConfiguredAudienceModelAssociationsPaginateTypeDef = TypedDict(
    "ListCollaborationConfiguredAudienceModelAssociationsInputListCollaborationConfiguredAudienceModelAssociationsPaginateTypeDef",
    {
        "collaborationIdentifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCollaborationIdNamespaceAssociationsInputListCollaborationIdNamespaceAssociationsPaginateTypeDef = TypedDict(
    "ListCollaborationIdNamespaceAssociationsInputListCollaborationIdNamespaceAssociationsPaginateTypeDef",
    {
        "collaborationIdentifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCollaborationPrivacyBudgetTemplatesInputListCollaborationPrivacyBudgetTemplatesPaginateTypeDef = TypedDict(
    "ListCollaborationPrivacyBudgetTemplatesInputListCollaborationPrivacyBudgetTemplatesPaginateTypeDef",
    {
        "collaborationIdentifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCollaborationPrivacyBudgetsInputListCollaborationPrivacyBudgetsPaginateTypeDef = TypedDict(
    "ListCollaborationPrivacyBudgetsInputListCollaborationPrivacyBudgetsPaginateTypeDef",
    {
        "collaborationIdentifier": str,
        "privacyBudgetType": Literal["DIFFERENTIAL_PRIVACY"],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCollaborationsInputListCollaborationsPaginateTypeDef = TypedDict(
    "ListCollaborationsInputListCollaborationsPaginateTypeDef",
    {
        "memberStatus": NotRequired[FilterableMemberStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListConfiguredAudienceModelAssociationsInputListConfiguredAudienceModelAssociationsPaginateTypeDef = TypedDict(
    "ListConfiguredAudienceModelAssociationsInputListConfiguredAudienceModelAssociationsPaginateTypeDef",
    {
        "membershipIdentifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListConfiguredTableAssociationsInputListConfiguredTableAssociationsPaginateTypeDef = TypedDict(
    "ListConfiguredTableAssociationsInputListConfiguredTableAssociationsPaginateTypeDef",
    {
        "membershipIdentifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListConfiguredTablesInputListConfiguredTablesPaginateTypeDef = TypedDict(
    "ListConfiguredTablesInputListConfiguredTablesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListIdMappingTablesInputListIdMappingTablesPaginateTypeDef = TypedDict(
    "ListIdMappingTablesInputListIdMappingTablesPaginateTypeDef",
    {
        "membershipIdentifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListIdNamespaceAssociationsInputListIdNamespaceAssociationsPaginateTypeDef = TypedDict(
    "ListIdNamespaceAssociationsInputListIdNamespaceAssociationsPaginateTypeDef",
    {
        "membershipIdentifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMembersInputListMembersPaginateTypeDef = TypedDict(
    "ListMembersInputListMembersPaginateTypeDef",
    {
        "collaborationIdentifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMembershipsInputListMembershipsPaginateTypeDef = TypedDict(
    "ListMembershipsInputListMembershipsPaginateTypeDef",
    {
        "status": NotRequired[MembershipStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPrivacyBudgetTemplatesInputListPrivacyBudgetTemplatesPaginateTypeDef = TypedDict(
    "ListPrivacyBudgetTemplatesInputListPrivacyBudgetTemplatesPaginateTypeDef",
    {
        "membershipIdentifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPrivacyBudgetsInputListPrivacyBudgetsPaginateTypeDef = TypedDict(
    "ListPrivacyBudgetsInputListPrivacyBudgetsPaginateTypeDef",
    {
        "membershipIdentifier": str,
        "privacyBudgetType": Literal["DIFFERENTIAL_PRIVACY"],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProtectedQueriesInputListProtectedQueriesPaginateTypeDef = TypedDict(
    "ListProtectedQueriesInputListProtectedQueriesPaginateTypeDef",
    {
        "membershipIdentifier": str,
        "status": NotRequired[ProtectedQueryStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSchemasInputListSchemasPaginateTypeDef = TypedDict(
    "ListSchemasInputListSchemasPaginateTypeDef",
    {
        "collaborationIdentifier": str,
        "schemaType": NotRequired[SchemaTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPrivacyBudgetTemplatesOutputTypeDef = TypedDict(
    "ListPrivacyBudgetTemplatesOutputTypeDef",
    {
        "nextToken": str,
        "privacyBudgetTemplateSummaries": List[PrivacyBudgetTemplateSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSchemasOutputTypeDef = TypedDict(
    "ListSchemasOutputTypeDef",
    {
        "schemaSummaries": List[SchemaSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MembershipPaymentConfigurationTypeDef = TypedDict(
    "MembershipPaymentConfigurationTypeDef",
    {
        "queryCompute": MembershipQueryComputePaymentConfigTypeDef,
    },
)
MembershipProtectedQueryOutputConfigurationTypeDef = TypedDict(
    "MembershipProtectedQueryOutputConfigurationTypeDef",
    {
        "s3": NotRequired[ProtectedQueryS3OutputConfigurationTypeDef],
    },
)
PaymentConfigurationTypeDef = TypedDict(
    "PaymentConfigurationTypeDef",
    {
        "queryCompute": QueryComputePaymentConfigTypeDef,
    },
)
ProtectedQueryOutputConfigurationTypeDef = TypedDict(
    "ProtectedQueryOutputConfigurationTypeDef",
    {
        "s3": NotRequired[ProtectedQueryS3OutputConfigurationTypeDef],
        "member": NotRequired[ProtectedQueryMemberOutputConfigurationTypeDef],
    },
)
ProtectedQueryOutputTypeDef = TypedDict(
    "ProtectedQueryOutputTypeDef",
    {
        "s3": NotRequired[ProtectedQueryS3OutputTypeDef],
        "memberList": NotRequired[List[ProtectedQuerySingleMemberOutputTypeDef]],
    },
)
QueryConstraintTypeDef = TypedDict(
    "QueryConstraintTypeDef",
    {
        "requireOverlap": NotRequired[QueryConstraintRequireOverlapTypeDef],
    },
)
SchemaStatusDetailTypeDef = TypedDict(
    "SchemaStatusDetailTypeDef",
    {
        "status": SchemaStatusType,
        "analysisType": AnalysisTypeType,
        "reasons": NotRequired[List[SchemaStatusReasonTypeDef]],
        "analysisRuleType": NotRequired[AnalysisRuleTypeType],
        "configurations": NotRequired[List[Literal["DIFFERENTIAL_PRIVACY"]]],
    },
)
AnalysisRuleAggregationTypeDef = TypedDict(
    "AnalysisRuleAggregationTypeDef",
    {
        "aggregateColumns": Sequence[AggregateColumnUnionTypeDef],
        "joinColumns": Sequence[str],
        "dimensionColumns": Sequence[str],
        "scalarFunctions": Sequence[ScalarFunctionsType],
        "outputConstraints": Sequence[AggregationConstraintTypeDef],
        "joinRequired": NotRequired[Literal["QUERY_RUNNER"]],
        "allowedJoinOperators": NotRequired[Sequence[JoinOperatorType]],
        "additionalAnalyses": NotRequired[AdditionalAnalysesType],
    },
)
AnalysisTemplateTypeDef = TypedDict(
    "AnalysisTemplateTypeDef",
    {
        "id": str,
        "arn": str,
        "collaborationId": str,
        "collaborationArn": str,
        "membershipId": str,
        "membershipArn": str,
        "name": str,
        "createTime": datetime,
        "updateTime": datetime,
        "schema": AnalysisSchemaTypeDef,
        "format": Literal["SQL"],
        "source": AnalysisSourceTypeDef,
        "description": NotRequired[str],
        "analysisParameters": NotRequired[List[AnalysisParameterTypeDef]],
        "validations": NotRequired[List[AnalysisTemplateValidationStatusDetailTypeDef]],
    },
)
CollaborationAnalysisTemplateTypeDef = TypedDict(
    "CollaborationAnalysisTemplateTypeDef",
    {
        "id": str,
        "arn": str,
        "collaborationId": str,
        "collaborationArn": str,
        "creatorAccountId": str,
        "name": str,
        "createTime": datetime,
        "updateTime": datetime,
        "schema": AnalysisSchemaTypeDef,
        "format": Literal["SQL"],
        "source": AnalysisSourceTypeDef,
        "description": NotRequired[str],
        "analysisParameters": NotRequired[List[AnalysisParameterTypeDef]],
        "validations": NotRequired[List[AnalysisTemplateValidationStatusDetailTypeDef]],
    },
)
ListCollaborationIdNamespaceAssociationsOutputTypeDef = TypedDict(
    "ListCollaborationIdNamespaceAssociationsOutputTypeDef",
    {
        "nextToken": str,
        "collaborationIdNamespaceAssociationSummaries": List[
            CollaborationIdNamespaceAssociationSummaryTypeDef
        ],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListIdNamespaceAssociationsOutputTypeDef = TypedDict(
    "ListIdNamespaceAssociationsOutputTypeDef",
    {
        "nextToken": str,
        "idNamespaceAssociationSummaries": List[IdNamespaceAssociationSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCollaborationIdNamespaceAssociationOutputTypeDef = TypedDict(
    "GetCollaborationIdNamespaceAssociationOutputTypeDef",
    {
        "collaborationIdNamespaceAssociation": CollaborationIdNamespaceAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateIdNamespaceAssociationOutputTypeDef = TypedDict(
    "CreateIdNamespaceAssociationOutputTypeDef",
    {
        "idNamespaceAssociation": IdNamespaceAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIdNamespaceAssociationOutputTypeDef = TypedDict(
    "GetIdNamespaceAssociationOutputTypeDef",
    {
        "idNamespaceAssociation": IdNamespaceAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateIdNamespaceAssociationOutputTypeDef = TypedDict(
    "UpdateIdNamespaceAssociationOutputTypeDef",
    {
        "idNamespaceAssociation": IdNamespaceAssociationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateCollaborationOutputTypeDef = TypedDict(
    "CreateCollaborationOutputTypeDef",
    {
        "collaboration": CollaborationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCollaborationOutputTypeDef = TypedDict(
    "GetCollaborationOutputTypeDef",
    {
        "collaboration": CollaborationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateCollaborationOutputTypeDef = TypedDict(
    "UpdateCollaborationOutputTypeDef",
    {
        "collaboration": CollaborationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReceiverConfigurationTypeDef = TypedDict(
    "ReceiverConfigurationTypeDef",
    {
        "analysisType": AnalysisTypeType,
        "configurationDetails": NotRequired[ConfigurationDetailsTypeDef],
    },
)
ConfiguredTableAssociationAnalysisRulePolicyOutputTypeDef = TypedDict(
    "ConfiguredTableAssociationAnalysisRulePolicyOutputTypeDef",
    {
        "v1": NotRequired[ConfiguredTableAssociationAnalysisRulePolicyV1OutputTypeDef],
    },
)
ConfiguredTableAssociationAnalysisRulePolicyV1TypeDef = TypedDict(
    "ConfiguredTableAssociationAnalysisRulePolicyV1TypeDef",
    {
        "list": NotRequired[ConfiguredTableAssociationAnalysisRuleListUnionTypeDef],
        "aggregation": NotRequired[ConfiguredTableAssociationAnalysisRuleAggregationUnionTypeDef],
        "custom": NotRequired[ConfiguredTableAssociationAnalysisRuleCustomUnionTypeDef],
    },
)
ListIdMappingTablesOutputTypeDef = TypedDict(
    "ListIdMappingTablesOutputTypeDef",
    {
        "idMappingTableSummaries": List[IdMappingTableSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AnalysisRuleCustomOutputTypeDef = TypedDict(
    "AnalysisRuleCustomOutputTypeDef",
    {
        "allowedAnalyses": List[str],
        "allowedAnalysisProviders": NotRequired[List[str]],
        "additionalAnalyses": NotRequired[AdditionalAnalysesType],
        "disallowedOutputColumns": NotRequired[List[str]],
        "differentialPrivacy": NotRequired[DifferentialPrivacyConfigurationOutputTypeDef],
    },
)
DifferentialPrivacyConfigurationUnionTypeDef = Union[
    DifferentialPrivacyConfigurationTypeDef, DifferentialPrivacyConfigurationOutputTypeDef
]
PrivacyImpactTypeDef = TypedDict(
    "PrivacyImpactTypeDef",
    {
        "differentialPrivacy": NotRequired[DifferentialPrivacyPrivacyImpactTypeDef],
    },
)
PreviewPrivacyImpactInputRequestTypeDef = TypedDict(
    "PreviewPrivacyImpactInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "parameters": PreviewPrivacyImpactParametersInputTypeDef,
    },
)
PrivacyBudgetTypeDef = TypedDict(
    "PrivacyBudgetTypeDef",
    {
        "differentialPrivacy": NotRequired[DifferentialPrivacyPrivacyBudgetTypeDef],
    },
)
CreatePrivacyBudgetTemplateInputRequestTypeDef = TypedDict(
    "CreatePrivacyBudgetTemplateInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "autoRefresh": PrivacyBudgetTemplateAutoRefreshType,
        "privacyBudgetType": Literal["DIFFERENTIAL_PRIVACY"],
        "parameters": PrivacyBudgetTemplateParametersInputTypeDef,
        "tags": NotRequired[Mapping[str, str]],
    },
)
CollaborationPrivacyBudgetTemplateTypeDef = TypedDict(
    "CollaborationPrivacyBudgetTemplateTypeDef",
    {
        "id": str,
        "arn": str,
        "collaborationId": str,
        "collaborationArn": str,
        "creatorAccountId": str,
        "createTime": datetime,
        "updateTime": datetime,
        "privacyBudgetType": Literal["DIFFERENTIAL_PRIVACY"],
        "autoRefresh": PrivacyBudgetTemplateAutoRefreshType,
        "parameters": PrivacyBudgetTemplateParametersOutputTypeDef,
    },
)
PrivacyBudgetTemplateTypeDef = TypedDict(
    "PrivacyBudgetTemplateTypeDef",
    {
        "id": str,
        "arn": str,
        "membershipId": str,
        "membershipArn": str,
        "collaborationId": str,
        "collaborationArn": str,
        "createTime": datetime,
        "updateTime": datetime,
        "privacyBudgetType": Literal["DIFFERENTIAL_PRIVACY"],
        "autoRefresh": PrivacyBudgetTemplateAutoRefreshType,
        "parameters": PrivacyBudgetTemplateParametersOutputTypeDef,
    },
)
UpdatePrivacyBudgetTemplateInputRequestTypeDef = TypedDict(
    "UpdatePrivacyBudgetTemplateInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "privacyBudgetTemplateIdentifier": str,
        "privacyBudgetType": Literal["DIFFERENTIAL_PRIVACY"],
        "parameters": NotRequired[PrivacyBudgetTemplateUpdateParametersTypeDef],
    },
)
ConfiguredTableTypeDef = TypedDict(
    "ConfiguredTableTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "tableReference": TableReferenceTypeDef,
        "createTime": datetime,
        "updateTime": datetime,
        "analysisRuleTypes": List[ConfiguredTableAnalysisRuleTypeType],
        "analysisMethod": Literal["DIRECT_QUERY"],
        "allowedColumns": List[str],
        "description": NotRequired[str],
    },
)
CreateConfiguredTableInputRequestTypeDef = TypedDict(
    "CreateConfiguredTableInputRequestTypeDef",
    {
        "name": str,
        "tableReference": TableReferenceTypeDef,
        "allowedColumns": Sequence[str],
        "analysisMethod": Literal["DIRECT_QUERY"],
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
IdMappingTableTypeDef = TypedDict(
    "IdMappingTableTypeDef",
    {
        "id": str,
        "arn": str,
        "inputReferenceConfig": IdMappingTableInputReferenceConfigTypeDef,
        "membershipId": str,
        "membershipArn": str,
        "collaborationId": str,
        "collaborationArn": str,
        "name": str,
        "createTime": datetime,
        "updateTime": datetime,
        "inputReferenceProperties": IdMappingTableInputReferencePropertiesTypeDef,
        "description": NotRequired[str],
        "kmsKeyArn": NotRequired[str],
    },
)
SchemaTypePropertiesTypeDef = TypedDict(
    "SchemaTypePropertiesTypeDef",
    {
        "idMappingTable": NotRequired[IdMappingTableSchemaTypePropertiesTypeDef],
    },
)
MembershipSummaryTypeDef = TypedDict(
    "MembershipSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "collaborationArn": str,
        "collaborationId": str,
        "collaborationCreatorAccountId": str,
        "collaborationCreatorDisplayName": str,
        "collaborationName": str,
        "createTime": datetime,
        "updateTime": datetime,
        "status": MembershipStatusType,
        "memberAbilities": List[MemberAbilityType],
        "paymentConfiguration": MembershipPaymentConfigurationTypeDef,
    },
)
MembershipProtectedQueryResultConfigurationTypeDef = TypedDict(
    "MembershipProtectedQueryResultConfigurationTypeDef",
    {
        "outputConfiguration": MembershipProtectedQueryOutputConfigurationTypeDef,
        "roleArn": NotRequired[str],
    },
)
MemberSpecificationTypeDef = TypedDict(
    "MemberSpecificationTypeDef",
    {
        "accountId": str,
        "memberAbilities": Sequence[MemberAbilityType],
        "displayName": str,
        "paymentConfiguration": NotRequired[PaymentConfigurationTypeDef],
    },
)
MemberSummaryTypeDef = TypedDict(
    "MemberSummaryTypeDef",
    {
        "accountId": str,
        "status": MemberStatusType,
        "displayName": str,
        "abilities": List[MemberAbilityType],
        "createTime": datetime,
        "updateTime": datetime,
        "paymentConfiguration": PaymentConfigurationTypeDef,
        "membershipId": NotRequired[str],
        "membershipArn": NotRequired[str],
    },
)
ProtectedQueryResultConfigurationTypeDef = TypedDict(
    "ProtectedQueryResultConfigurationTypeDef",
    {
        "outputConfiguration": ProtectedQueryOutputConfigurationTypeDef,
    },
)
ProtectedQueryResultTypeDef = TypedDict(
    "ProtectedQueryResultTypeDef",
    {
        "output": ProtectedQueryOutputTypeDef,
    },
)
AnalysisRuleIdMappingTableTypeDef = TypedDict(
    "AnalysisRuleIdMappingTableTypeDef",
    {
        "joinColumns": List[str],
        "queryConstraints": List[QueryConstraintTypeDef],
        "dimensionColumns": NotRequired[List[str]],
    },
)
AnalysisRuleAggregationUnionTypeDef = Union[
    AnalysisRuleAggregationTypeDef, AnalysisRuleAggregationOutputTypeDef
]
CreateAnalysisTemplateOutputTypeDef = TypedDict(
    "CreateAnalysisTemplateOutputTypeDef",
    {
        "analysisTemplate": AnalysisTemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAnalysisTemplateOutputTypeDef = TypedDict(
    "GetAnalysisTemplateOutputTypeDef",
    {
        "analysisTemplate": AnalysisTemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAnalysisTemplateOutputTypeDef = TypedDict(
    "UpdateAnalysisTemplateOutputTypeDef",
    {
        "analysisTemplate": AnalysisTemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetCollaborationAnalysisTemplateOutputTypeDef = TypedDict(
    "BatchGetCollaborationAnalysisTemplateOutputTypeDef",
    {
        "collaborationAnalysisTemplates": List[CollaborationAnalysisTemplateTypeDef],
        "errors": List[BatchGetCollaborationAnalysisTemplateErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCollaborationAnalysisTemplateOutputTypeDef = TypedDict(
    "GetCollaborationAnalysisTemplateOutputTypeDef",
    {
        "collaborationAnalysisTemplate": CollaborationAnalysisTemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProtectedQuerySummaryTypeDef = TypedDict(
    "ProtectedQuerySummaryTypeDef",
    {
        "id": str,
        "membershipId": str,
        "membershipArn": str,
        "createTime": datetime,
        "status": ProtectedQueryStatusType,
        "receiverConfigurations": List[ReceiverConfigurationTypeDef],
    },
)
ConfiguredTableAssociationAnalysisRuleTypeDef = TypedDict(
    "ConfiguredTableAssociationAnalysisRuleTypeDef",
    {
        "membershipIdentifier": str,
        "configuredTableAssociationId": str,
        "configuredTableAssociationArn": str,
        "policy": ConfiguredTableAssociationAnalysisRulePolicyOutputTypeDef,
        "type": ConfiguredTableAssociationAnalysisRuleTypeType,
        "createTime": datetime,
        "updateTime": datetime,
    },
)
ConfiguredTableAssociationAnalysisRulePolicyV1UnionTypeDef = Union[
    ConfiguredTableAssociationAnalysisRulePolicyV1TypeDef,
    ConfiguredTableAssociationAnalysisRulePolicyV1OutputTypeDef,
]
ConfiguredTableAnalysisRulePolicyV1OutputTypeDef = TypedDict(
    "ConfiguredTableAnalysisRulePolicyV1OutputTypeDef",
    {
        "list": NotRequired[AnalysisRuleListOutputTypeDef],
        "aggregation": NotRequired[AnalysisRuleAggregationOutputTypeDef],
        "custom": NotRequired[AnalysisRuleCustomOutputTypeDef],
    },
)
AnalysisRuleCustomTypeDef = TypedDict(
    "AnalysisRuleCustomTypeDef",
    {
        "allowedAnalyses": Sequence[str],
        "allowedAnalysisProviders": NotRequired[Sequence[str]],
        "additionalAnalyses": NotRequired[AdditionalAnalysesType],
        "disallowedOutputColumns": NotRequired[Sequence[str]],
        "differentialPrivacy": NotRequired[DifferentialPrivacyConfigurationUnionTypeDef],
    },
)
PreviewPrivacyImpactOutputTypeDef = TypedDict(
    "PreviewPrivacyImpactOutputTypeDef",
    {
        "privacyImpact": PrivacyImpactTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CollaborationPrivacyBudgetSummaryTypeDef = TypedDict(
    "CollaborationPrivacyBudgetSummaryTypeDef",
    {
        "id": str,
        "privacyBudgetTemplateId": str,
        "privacyBudgetTemplateArn": str,
        "collaborationId": str,
        "collaborationArn": str,
        "creatorAccountId": str,
        "type": Literal["DIFFERENTIAL_PRIVACY"],
        "createTime": datetime,
        "updateTime": datetime,
        "budget": PrivacyBudgetTypeDef,
    },
)
PrivacyBudgetSummaryTypeDef = TypedDict(
    "PrivacyBudgetSummaryTypeDef",
    {
        "id": str,
        "privacyBudgetTemplateId": str,
        "privacyBudgetTemplateArn": str,
        "membershipId": str,
        "membershipArn": str,
        "collaborationId": str,
        "collaborationArn": str,
        "type": Literal["DIFFERENTIAL_PRIVACY"],
        "createTime": datetime,
        "updateTime": datetime,
        "budget": PrivacyBudgetTypeDef,
    },
)
GetCollaborationPrivacyBudgetTemplateOutputTypeDef = TypedDict(
    "GetCollaborationPrivacyBudgetTemplateOutputTypeDef",
    {
        "collaborationPrivacyBudgetTemplate": CollaborationPrivacyBudgetTemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePrivacyBudgetTemplateOutputTypeDef = TypedDict(
    "CreatePrivacyBudgetTemplateOutputTypeDef",
    {
        "privacyBudgetTemplate": PrivacyBudgetTemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPrivacyBudgetTemplateOutputTypeDef = TypedDict(
    "GetPrivacyBudgetTemplateOutputTypeDef",
    {
        "privacyBudgetTemplate": PrivacyBudgetTemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePrivacyBudgetTemplateOutputTypeDef = TypedDict(
    "UpdatePrivacyBudgetTemplateOutputTypeDef",
    {
        "privacyBudgetTemplate": PrivacyBudgetTemplateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateConfiguredTableOutputTypeDef = TypedDict(
    "CreateConfiguredTableOutputTypeDef",
    {
        "configuredTable": ConfiguredTableTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetConfiguredTableOutputTypeDef = TypedDict(
    "GetConfiguredTableOutputTypeDef",
    {
        "configuredTable": ConfiguredTableTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateConfiguredTableOutputTypeDef = TypedDict(
    "UpdateConfiguredTableOutputTypeDef",
    {
        "configuredTable": ConfiguredTableTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateIdMappingTableOutputTypeDef = TypedDict(
    "CreateIdMappingTableOutputTypeDef",
    {
        "idMappingTable": IdMappingTableTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIdMappingTableOutputTypeDef = TypedDict(
    "GetIdMappingTableOutputTypeDef",
    {
        "idMappingTable": IdMappingTableTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateIdMappingTableOutputTypeDef = TypedDict(
    "UpdateIdMappingTableOutputTypeDef",
    {
        "idMappingTable": IdMappingTableTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SchemaTypeDef = TypedDict(
    "SchemaTypeDef",
    {
        "columns": List[ColumnTypeDef],
        "partitionKeys": List[ColumnTypeDef],
        "analysisRuleTypes": List[AnalysisRuleTypeType],
        "creatorAccountId": str,
        "name": str,
        "collaborationId": str,
        "collaborationArn": str,
        "description": str,
        "createTime": datetime,
        "updateTime": datetime,
        "type": SchemaTypeType,
        "schemaStatusDetails": List[SchemaStatusDetailTypeDef],
        "analysisMethod": NotRequired[Literal["DIRECT_QUERY"]],
        "schemaTypeProperties": NotRequired[SchemaTypePropertiesTypeDef],
    },
)
ListMembershipsOutputTypeDef = TypedDict(
    "ListMembershipsOutputTypeDef",
    {
        "nextToken": str,
        "membershipSummaries": List[MembershipSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMembershipInputRequestTypeDef = TypedDict(
    "CreateMembershipInputRequestTypeDef",
    {
        "collaborationIdentifier": str,
        "queryLogStatus": MembershipQueryLogStatusType,
        "tags": NotRequired[Mapping[str, str]],
        "defaultResultConfiguration": NotRequired[
            MembershipProtectedQueryResultConfigurationTypeDef
        ],
        "paymentConfiguration": NotRequired[MembershipPaymentConfigurationTypeDef],
    },
)
MembershipTypeDef = TypedDict(
    "MembershipTypeDef",
    {
        "id": str,
        "arn": str,
        "collaborationArn": str,
        "collaborationId": str,
        "collaborationCreatorAccountId": str,
        "collaborationCreatorDisplayName": str,
        "collaborationName": str,
        "createTime": datetime,
        "updateTime": datetime,
        "status": MembershipStatusType,
        "memberAbilities": List[MemberAbilityType],
        "queryLogStatus": MembershipQueryLogStatusType,
        "paymentConfiguration": MembershipPaymentConfigurationTypeDef,
        "defaultResultConfiguration": NotRequired[
            MembershipProtectedQueryResultConfigurationTypeDef
        ],
    },
)
UpdateMembershipInputRequestTypeDef = TypedDict(
    "UpdateMembershipInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "queryLogStatus": NotRequired[MembershipQueryLogStatusType],
        "defaultResultConfiguration": NotRequired[
            MembershipProtectedQueryResultConfigurationTypeDef
        ],
    },
)
CreateCollaborationInputRequestTypeDef = TypedDict(
    "CreateCollaborationInputRequestTypeDef",
    {
        "members": Sequence[MemberSpecificationTypeDef],
        "name": str,
        "description": str,
        "creatorMemberAbilities": Sequence[MemberAbilityType],
        "creatorDisplayName": str,
        "queryLogStatus": CollaborationQueryLogStatusType,
        "dataEncryptionMetadata": NotRequired[DataEncryptionMetadataTypeDef],
        "tags": NotRequired[Mapping[str, str]],
        "creatorPaymentConfiguration": NotRequired[PaymentConfigurationTypeDef],
    },
)
ListMembersOutputTypeDef = TypedDict(
    "ListMembersOutputTypeDef",
    {
        "nextToken": str,
        "memberSummaries": List[MemberSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartProtectedQueryInputRequestTypeDef = TypedDict(
    "StartProtectedQueryInputRequestTypeDef",
    {
        "type": Literal["SQL"],
        "membershipIdentifier": str,
        "sqlParameters": ProtectedQuerySQLParametersTypeDef,
        "resultConfiguration": NotRequired[ProtectedQueryResultConfigurationTypeDef],
    },
)
ProtectedQueryTypeDef = TypedDict(
    "ProtectedQueryTypeDef",
    {
        "id": str,
        "membershipId": str,
        "membershipArn": str,
        "createTime": datetime,
        "status": ProtectedQueryStatusType,
        "sqlParameters": NotRequired[ProtectedQuerySQLParametersOutputTypeDef],
        "resultConfiguration": NotRequired[ProtectedQueryResultConfigurationTypeDef],
        "statistics": NotRequired[ProtectedQueryStatisticsTypeDef],
        "result": NotRequired[ProtectedQueryResultTypeDef],
        "error": NotRequired[ProtectedQueryErrorTypeDef],
        "differentialPrivacy": NotRequired[DifferentialPrivacyParametersTypeDef],
    },
)
AnalysisRulePolicyV1TypeDef = TypedDict(
    "AnalysisRulePolicyV1TypeDef",
    {
        "list": NotRequired[AnalysisRuleListOutputTypeDef],
        "aggregation": NotRequired[AnalysisRuleAggregationOutputTypeDef],
        "custom": NotRequired[AnalysisRuleCustomOutputTypeDef],
        "idMappingTable": NotRequired[AnalysisRuleIdMappingTableTypeDef],
    },
)
ListProtectedQueriesOutputTypeDef = TypedDict(
    "ListProtectedQueriesOutputTypeDef",
    {
        "nextToken": str,
        "protectedQueries": List[ProtectedQuerySummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateConfiguredTableAssociationAnalysisRuleOutputTypeDef = TypedDict(
    "CreateConfiguredTableAssociationAnalysisRuleOutputTypeDef",
    {
        "analysisRule": ConfiguredTableAssociationAnalysisRuleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetConfiguredTableAssociationAnalysisRuleOutputTypeDef = TypedDict(
    "GetConfiguredTableAssociationAnalysisRuleOutputTypeDef",
    {
        "analysisRule": ConfiguredTableAssociationAnalysisRuleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateConfiguredTableAssociationAnalysisRuleOutputTypeDef = TypedDict(
    "UpdateConfiguredTableAssociationAnalysisRuleOutputTypeDef",
    {
        "analysisRule": ConfiguredTableAssociationAnalysisRuleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConfiguredTableAssociationAnalysisRulePolicyTypeDef = TypedDict(
    "ConfiguredTableAssociationAnalysisRulePolicyTypeDef",
    {
        "v1": NotRequired[ConfiguredTableAssociationAnalysisRulePolicyV1UnionTypeDef],
    },
)
ConfiguredTableAnalysisRulePolicyOutputTypeDef = TypedDict(
    "ConfiguredTableAnalysisRulePolicyOutputTypeDef",
    {
        "v1": NotRequired[ConfiguredTableAnalysisRulePolicyV1OutputTypeDef],
    },
)
AnalysisRuleCustomUnionTypeDef = Union[AnalysisRuleCustomTypeDef, AnalysisRuleCustomOutputTypeDef]
ListCollaborationPrivacyBudgetsOutputTypeDef = TypedDict(
    "ListCollaborationPrivacyBudgetsOutputTypeDef",
    {
        "collaborationPrivacyBudgetSummaries": List[CollaborationPrivacyBudgetSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPrivacyBudgetsOutputTypeDef = TypedDict(
    "ListPrivacyBudgetsOutputTypeDef",
    {
        "privacyBudgetSummaries": List[PrivacyBudgetSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetSchemaOutputTypeDef = TypedDict(
    "BatchGetSchemaOutputTypeDef",
    {
        "schemas": List[SchemaTypeDef],
        "errors": List[BatchGetSchemaErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSchemaOutputTypeDef = TypedDict(
    "GetSchemaOutputTypeDef",
    {
        "schema": SchemaTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMembershipOutputTypeDef = TypedDict(
    "CreateMembershipOutputTypeDef",
    {
        "membership": MembershipTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMembershipOutputTypeDef = TypedDict(
    "GetMembershipOutputTypeDef",
    {
        "membership": MembershipTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateMembershipOutputTypeDef = TypedDict(
    "UpdateMembershipOutputTypeDef",
    {
        "membership": MembershipTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetProtectedQueryOutputTypeDef = TypedDict(
    "GetProtectedQueryOutputTypeDef",
    {
        "protectedQuery": ProtectedQueryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartProtectedQueryOutputTypeDef = TypedDict(
    "StartProtectedQueryOutputTypeDef",
    {
        "protectedQuery": ProtectedQueryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateProtectedQueryOutputTypeDef = TypedDict(
    "UpdateProtectedQueryOutputTypeDef",
    {
        "protectedQuery": ProtectedQueryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AnalysisRulePolicyTypeDef = TypedDict(
    "AnalysisRulePolicyTypeDef",
    {
        "v1": NotRequired[AnalysisRulePolicyV1TypeDef],
    },
)
CreateConfiguredTableAssociationAnalysisRuleInputRequestTypeDef = TypedDict(
    "CreateConfiguredTableAssociationAnalysisRuleInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "configuredTableAssociationIdentifier": str,
        "analysisRuleType": ConfiguredTableAssociationAnalysisRuleTypeType,
        "analysisRulePolicy": ConfiguredTableAssociationAnalysisRulePolicyTypeDef,
    },
)
UpdateConfiguredTableAssociationAnalysisRuleInputRequestTypeDef = TypedDict(
    "UpdateConfiguredTableAssociationAnalysisRuleInputRequestTypeDef",
    {
        "membershipIdentifier": str,
        "configuredTableAssociationIdentifier": str,
        "analysisRuleType": ConfiguredTableAssociationAnalysisRuleTypeType,
        "analysisRulePolicy": ConfiguredTableAssociationAnalysisRulePolicyTypeDef,
    },
)
ConfiguredTableAnalysisRuleTypeDef = TypedDict(
    "ConfiguredTableAnalysisRuleTypeDef",
    {
        "configuredTableId": str,
        "configuredTableArn": str,
        "policy": ConfiguredTableAnalysisRulePolicyOutputTypeDef,
        "type": ConfiguredTableAnalysisRuleTypeType,
        "createTime": datetime,
        "updateTime": datetime,
    },
)
ConfiguredTableAnalysisRulePolicyV1TypeDef = TypedDict(
    "ConfiguredTableAnalysisRulePolicyV1TypeDef",
    {
        "list": NotRequired[AnalysisRuleListUnionTypeDef],
        "aggregation": NotRequired[AnalysisRuleAggregationUnionTypeDef],
        "custom": NotRequired[AnalysisRuleCustomUnionTypeDef],
    },
)
AnalysisRuleTypeDef = TypedDict(
    "AnalysisRuleTypeDef",
    {
        "collaborationId": str,
        "type": AnalysisRuleTypeType,
        "name": str,
        "createTime": datetime,
        "updateTime": datetime,
        "policy": AnalysisRulePolicyTypeDef,
    },
)
CreateConfiguredTableAnalysisRuleOutputTypeDef = TypedDict(
    "CreateConfiguredTableAnalysisRuleOutputTypeDef",
    {
        "analysisRule": ConfiguredTableAnalysisRuleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetConfiguredTableAnalysisRuleOutputTypeDef = TypedDict(
    "GetConfiguredTableAnalysisRuleOutputTypeDef",
    {
        "analysisRule": ConfiguredTableAnalysisRuleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateConfiguredTableAnalysisRuleOutputTypeDef = TypedDict(
    "UpdateConfiguredTableAnalysisRuleOutputTypeDef",
    {
        "analysisRule": ConfiguredTableAnalysisRuleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConfiguredTableAnalysisRulePolicyV1UnionTypeDef = Union[
    ConfiguredTableAnalysisRulePolicyV1TypeDef, ConfiguredTableAnalysisRulePolicyV1OutputTypeDef
]
BatchGetSchemaAnalysisRuleOutputTypeDef = TypedDict(
    "BatchGetSchemaAnalysisRuleOutputTypeDef",
    {
        "analysisRules": List[AnalysisRuleTypeDef],
        "errors": List[BatchGetSchemaAnalysisRuleErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSchemaAnalysisRuleOutputTypeDef = TypedDict(
    "GetSchemaAnalysisRuleOutputTypeDef",
    {
        "analysisRule": AnalysisRuleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ConfiguredTableAnalysisRulePolicyTypeDef = TypedDict(
    "ConfiguredTableAnalysisRulePolicyTypeDef",
    {
        "v1": NotRequired[ConfiguredTableAnalysisRulePolicyV1UnionTypeDef],
    },
)
CreateConfiguredTableAnalysisRuleInputRequestTypeDef = TypedDict(
    "CreateConfiguredTableAnalysisRuleInputRequestTypeDef",
    {
        "configuredTableIdentifier": str,
        "analysisRuleType": ConfiguredTableAnalysisRuleTypeType,
        "analysisRulePolicy": ConfiguredTableAnalysisRulePolicyTypeDef,
    },
)
UpdateConfiguredTableAnalysisRuleInputRequestTypeDef = TypedDict(
    "UpdateConfiguredTableAnalysisRuleInputRequestTypeDef",
    {
        "configuredTableIdentifier": str,
        "analysisRuleType": ConfiguredTableAnalysisRuleTypeType,
        "analysisRulePolicy": ConfiguredTableAnalysisRulePolicyTypeDef,
    },
)
