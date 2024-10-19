"""
Type annotations for servicecatalog service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/type_defs/)

Usage::

    ```python
    from mypy_boto3_servicecatalog.type_defs import AcceptPortfolioShareInputRequestTypeDef

    data: AcceptPortfolioShareInputRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AccessLevelFilterKeyType,
    AccessStatusType,
    ChangeActionType,
    CopyProductStatusType,
    DescribePortfolioShareTypeType,
    EngineWorkflowStatusType,
    EvaluationTypeType,
    LastSyncStatusType,
    OrganizationNodeTypeType,
    PortfolioShareTypeType,
    PrincipalTypeType,
    ProductTypeType,
    ProductViewFilterByType,
    ProductViewSortByType,
    PropertyKeyType,
    ProvisionedProductPlanStatusType,
    ProvisionedProductStatusType,
    ProvisioningArtifactGuidanceType,
    ProvisioningArtifactTypeType,
    RecordStatusType,
    ReplacementType,
    RequiresRecreationType,
    ResourceAttributeType,
    ServiceActionAssociationErrorCodeType,
    ServiceActionDefinitionKeyType,
    ShareStatusType,
    SortOrderType,
    StackInstanceStatusType,
    StackSetOperationTypeType,
    StatusType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AcceptPortfolioShareInputRequestTypeDef",
    "AccessLevelFilterTypeDef",
    "AssociateBudgetWithResourceInputRequestTypeDef",
    "AssociatePrincipalWithPortfolioInputRequestTypeDef",
    "AssociateProductWithPortfolioInputRequestTypeDef",
    "AssociateServiceActionWithProvisioningArtifactInputRequestTypeDef",
    "AssociateTagOptionWithResourceInputRequestTypeDef",
    "ServiceActionAssociationTypeDef",
    "FailedServiceActionAssociationTypeDef",
    "ResponseMetadataTypeDef",
    "BudgetDetailTypeDef",
    "CloudWatchDashboardTypeDef",
    "CodeStarParametersTypeDef",
    "ConstraintDetailTypeDef",
    "ConstraintSummaryTypeDef",
    "CopyProductInputRequestTypeDef",
    "CreateConstraintInputRequestTypeDef",
    "TagTypeDef",
    "PortfolioDetailTypeDef",
    "OrganizationNodeTypeDef",
    "ProvisioningArtifactPropertiesTypeDef",
    "ProvisioningArtifactDetailTypeDef",
    "UpdateProvisioningParameterTypeDef",
    "CreateServiceActionInputRequestTypeDef",
    "CreateTagOptionInputRequestTypeDef",
    "TagOptionDetailTypeDef",
    "DeleteConstraintInputRequestTypeDef",
    "DeletePortfolioInputRequestTypeDef",
    "DeleteProductInputRequestTypeDef",
    "DeleteProvisionedProductPlanInputRequestTypeDef",
    "DeleteProvisioningArtifactInputRequestTypeDef",
    "DeleteServiceActionInputRequestTypeDef",
    "DeleteTagOptionInputRequestTypeDef",
    "DescribeConstraintInputRequestTypeDef",
    "DescribeCopyProductStatusInputRequestTypeDef",
    "DescribePortfolioInputRequestTypeDef",
    "DescribePortfolioShareStatusInputRequestTypeDef",
    "DescribePortfolioSharesInputRequestTypeDef",
    "PortfolioShareDetailTypeDef",
    "DescribeProductAsAdminInputRequestTypeDef",
    "ProvisioningArtifactSummaryTypeDef",
    "DescribeProductInputRequestTypeDef",
    "LaunchPathTypeDef",
    "ProductViewSummaryTypeDef",
    "ProvisioningArtifactTypeDef",
    "DescribeProductViewInputRequestTypeDef",
    "DescribeProvisionedProductInputRequestTypeDef",
    "ProvisionedProductDetailTypeDef",
    "DescribeProvisionedProductPlanInputRequestTypeDef",
    "DescribeProvisioningArtifactInputRequestTypeDef",
    "DescribeProvisioningParametersInputRequestTypeDef",
    "ProvisioningArtifactOutputTypeDef",
    "ProvisioningArtifactPreferencesTypeDef",
    "TagOptionSummaryTypeDef",
    "UsageInstructionTypeDef",
    "DescribeRecordInputRequestTypeDef",
    "RecordOutputTypeDef",
    "DescribeServiceActionExecutionParametersInputRequestTypeDef",
    "ExecutionParameterTypeDef",
    "DescribeServiceActionInputRequestTypeDef",
    "DescribeTagOptionInputRequestTypeDef",
    "DisassociateBudgetFromResourceInputRequestTypeDef",
    "DisassociatePrincipalFromPortfolioInputRequestTypeDef",
    "DisassociateProductFromPortfolioInputRequestTypeDef",
    "DisassociateServiceActionFromProvisioningArtifactInputRequestTypeDef",
    "DisassociateTagOptionFromResourceInputRequestTypeDef",
    "UniqueTagResourceIdentifierTypeDef",
    "ExecuteProvisionedProductPlanInputRequestTypeDef",
    "ExecuteProvisionedProductServiceActionInputRequestTypeDef",
    "GetProvisionedProductOutputsInputRequestTypeDef",
    "ImportAsProvisionedProductInputRequestTypeDef",
    "LastSyncTypeDef",
    "PaginatorConfigTypeDef",
    "ListAcceptedPortfolioSharesInputRequestTypeDef",
    "ListBudgetsForResourceInputRequestTypeDef",
    "ListConstraintsForPortfolioInputRequestTypeDef",
    "ListLaunchPathsInputRequestTypeDef",
    "ListOrganizationPortfolioAccessInputRequestTypeDef",
    "ListPortfolioAccessInputRequestTypeDef",
    "ListPortfoliosForProductInputRequestTypeDef",
    "ListPortfoliosInputRequestTypeDef",
    "ListPrincipalsForPortfolioInputRequestTypeDef",
    "PrincipalTypeDef",
    "ProvisionedProductPlanSummaryTypeDef",
    "ListProvisioningArtifactsForServiceActionInputRequestTypeDef",
    "ListProvisioningArtifactsInputRequestTypeDef",
    "ListRecordHistorySearchFilterTypeDef",
    "ListResourcesForTagOptionInputRequestTypeDef",
    "ResourceDetailTypeDef",
    "ListServiceActionsForProvisioningArtifactInputRequestTypeDef",
    "ServiceActionSummaryTypeDef",
    "ListServiceActionsInputRequestTypeDef",
    "ListStackInstancesForProvisionedProductInputRequestTypeDef",
    "StackInstanceTypeDef",
    "ListTagOptionsFiltersTypeDef",
    "NotifyTerminateProvisionedProductEngineWorkflowResultInputRequestTypeDef",
    "ParameterConstraintsTypeDef",
    "ProductViewAggregationValueTypeDef",
    "ProvisioningParameterTypeDef",
    "ProvisioningPreferencesTypeDef",
    "RecordErrorTypeDef",
    "RecordTagTypeDef",
    "RejectPortfolioShareInputRequestTypeDef",
    "ResourceTargetDefinitionTypeDef",
    "SearchProductsAsAdminInputRequestTypeDef",
    "SearchProductsInputRequestTypeDef",
    "ShareErrorTypeDef",
    "TerminateProvisionedProductInputRequestTypeDef",
    "UpdateConstraintInputRequestTypeDef",
    "UpdateProvisioningPreferencesTypeDef",
    "UpdateProvisionedProductPropertiesInputRequestTypeDef",
    "UpdateProvisioningArtifactInputRequestTypeDef",
    "UpdateServiceActionInputRequestTypeDef",
    "UpdateTagOptionInputRequestTypeDef",
    "ListProvisionedProductPlansInputRequestTypeDef",
    "ScanProvisionedProductsInputRequestTypeDef",
    "SearchProvisionedProductsInputRequestTypeDef",
    "BatchAssociateServiceActionWithProvisioningArtifactInputRequestTypeDef",
    "BatchDisassociateServiceActionFromProvisioningArtifactInputRequestTypeDef",
    "BatchAssociateServiceActionWithProvisioningArtifactOutputTypeDef",
    "BatchDisassociateServiceActionFromProvisioningArtifactOutputTypeDef",
    "CopyProductOutputTypeDef",
    "CreatePortfolioShareOutputTypeDef",
    "CreateProvisionedProductPlanOutputTypeDef",
    "DeletePortfolioShareOutputTypeDef",
    "DescribeCopyProductStatusOutputTypeDef",
    "GetAWSOrganizationsAccessStatusOutputTypeDef",
    "ListPortfolioAccessOutputTypeDef",
    "UpdatePortfolioShareOutputTypeDef",
    "UpdateProvisionedProductPropertiesOutputTypeDef",
    "ListBudgetsForResourceOutputTypeDef",
    "SourceConnectionParametersTypeDef",
    "CreateConstraintOutputTypeDef",
    "DescribeConstraintOutputTypeDef",
    "ListConstraintsForPortfolioOutputTypeDef",
    "UpdateConstraintOutputTypeDef",
    "CreatePortfolioInputRequestTypeDef",
    "LaunchPathSummaryTypeDef",
    "ProvisionedProductAttributeTypeDef",
    "UpdatePortfolioInputRequestTypeDef",
    "CreatePortfolioOutputTypeDef",
    "ListAcceptedPortfolioSharesOutputTypeDef",
    "ListPortfoliosForProductOutputTypeDef",
    "ListPortfoliosOutputTypeDef",
    "UpdatePortfolioOutputTypeDef",
    "CreatePortfolioShareInputRequestTypeDef",
    "DeletePortfolioShareInputRequestTypeDef",
    "ListOrganizationPortfolioAccessOutputTypeDef",
    "UpdatePortfolioShareInputRequestTypeDef",
    "CreateProvisioningArtifactInputRequestTypeDef",
    "CreateProvisioningArtifactOutputTypeDef",
    "ListProvisioningArtifactsOutputTypeDef",
    "UpdateProvisioningArtifactOutputTypeDef",
    "CreateProvisionedProductPlanInputRequestTypeDef",
    "ProvisionedProductPlanDetailsTypeDef",
    "CreateTagOptionOutputTypeDef",
    "DescribePortfolioOutputTypeDef",
    "DescribeTagOptionOutputTypeDef",
    "ListTagOptionsOutputTypeDef",
    "UpdateTagOptionOutputTypeDef",
    "DescribePortfolioSharesOutputTypeDef",
    "DescribeProductOutputTypeDef",
    "DescribeProductViewOutputTypeDef",
    "ProvisioningArtifactViewTypeDef",
    "DescribeProvisionedProductOutputTypeDef",
    "ScanProvisionedProductsOutputTypeDef",
    "GetProvisionedProductOutputsOutputTypeDef",
    "NotifyUpdateProvisionedProductEngineWorkflowResultInputRequestTypeDef",
    "DescribeServiceActionExecutionParametersOutputTypeDef",
    "EngineWorkflowResourceIdentifierTypeDef",
    "ListAcceptedPortfolioSharesInputListAcceptedPortfolioSharesPaginateTypeDef",
    "ListConstraintsForPortfolioInputListConstraintsForPortfolioPaginateTypeDef",
    "ListLaunchPathsInputListLaunchPathsPaginateTypeDef",
    "ListOrganizationPortfolioAccessInputListOrganizationPortfolioAccessPaginateTypeDef",
    "ListPortfoliosForProductInputListPortfoliosForProductPaginateTypeDef",
    "ListPortfoliosInputListPortfoliosPaginateTypeDef",
    "ListPrincipalsForPortfolioInputListPrincipalsForPortfolioPaginateTypeDef",
    "ListProvisionedProductPlansInputListProvisionedProductPlansPaginateTypeDef",
    "ListProvisioningArtifactsForServiceActionInputListProvisioningArtifactsForServiceActionPaginateTypeDef",
    "ListResourcesForTagOptionInputListResourcesForTagOptionPaginateTypeDef",
    "ListServiceActionsForProvisioningArtifactInputListServiceActionsForProvisioningArtifactPaginateTypeDef",
    "ListServiceActionsInputListServiceActionsPaginateTypeDef",
    "ScanProvisionedProductsInputScanProvisionedProductsPaginateTypeDef",
    "SearchProductsAsAdminInputSearchProductsAsAdminPaginateTypeDef",
    "ListPrincipalsForPortfolioOutputTypeDef",
    "ListProvisionedProductPlansOutputTypeDef",
    "ListRecordHistoryInputListRecordHistoryPaginateTypeDef",
    "ListRecordHistoryInputRequestTypeDef",
    "ListResourcesForTagOptionOutputTypeDef",
    "ListServiceActionsForProvisioningArtifactOutputTypeDef",
    "ListServiceActionsOutputTypeDef",
    "ServiceActionDetailTypeDef",
    "ListStackInstancesForProvisionedProductOutputTypeDef",
    "ListTagOptionsInputListTagOptionsPaginateTypeDef",
    "ListTagOptionsInputRequestTypeDef",
    "ProvisioningArtifactParameterTypeDef",
    "SearchProductsOutputTypeDef",
    "ProvisionProductInputRequestTypeDef",
    "RecordDetailTypeDef",
    "ResourceChangeDetailTypeDef",
    "ShareDetailsTypeDef",
    "UpdateProvisionedProductInputRequestTypeDef",
    "SourceConnectionDetailTypeDef",
    "SourceConnectionTypeDef",
    "ListLaunchPathsOutputTypeDef",
    "SearchProvisionedProductsOutputTypeDef",
    "ListProvisioningArtifactsForServiceActionOutputTypeDef",
    "NotifyProvisionProductEngineWorkflowResultInputRequestTypeDef",
    "CreateServiceActionOutputTypeDef",
    "DescribeServiceActionOutputTypeDef",
    "UpdateServiceActionOutputTypeDef",
    "DescribeProvisioningArtifactOutputTypeDef",
    "DescribeProvisioningParametersOutputTypeDef",
    "DescribeRecordOutputTypeDef",
    "ExecuteProvisionedProductPlanOutputTypeDef",
    "ExecuteProvisionedProductServiceActionOutputTypeDef",
    "ImportAsProvisionedProductOutputTypeDef",
    "ListRecordHistoryOutputTypeDef",
    "ProvisionProductOutputTypeDef",
    "TerminateProvisionedProductOutputTypeDef",
    "UpdateProvisionedProductOutputTypeDef",
    "ResourceChangeTypeDef",
    "DescribePortfolioShareStatusOutputTypeDef",
    "ProductViewDetailTypeDef",
    "CreateProductInputRequestTypeDef",
    "UpdateProductInputRequestTypeDef",
    "DescribeProvisionedProductPlanOutputTypeDef",
    "CreateProductOutputTypeDef",
    "DescribeProductAsAdminOutputTypeDef",
    "SearchProductsAsAdminOutputTypeDef",
    "UpdateProductOutputTypeDef",
)

AcceptPortfolioShareInputRequestTypeDef = TypedDict(
    "AcceptPortfolioShareInputRequestTypeDef",
    {
        "PortfolioId": str,
        "AcceptLanguage": NotRequired[str],
        "PortfolioShareType": NotRequired[PortfolioShareTypeType],
    },
)
AccessLevelFilterTypeDef = TypedDict(
    "AccessLevelFilterTypeDef",
    {
        "Key": NotRequired[AccessLevelFilterKeyType],
        "Value": NotRequired[str],
    },
)
AssociateBudgetWithResourceInputRequestTypeDef = TypedDict(
    "AssociateBudgetWithResourceInputRequestTypeDef",
    {
        "BudgetName": str,
        "ResourceId": str,
    },
)
AssociatePrincipalWithPortfolioInputRequestTypeDef = TypedDict(
    "AssociatePrincipalWithPortfolioInputRequestTypeDef",
    {
        "PortfolioId": str,
        "PrincipalARN": str,
        "PrincipalType": PrincipalTypeType,
        "AcceptLanguage": NotRequired[str],
    },
)
AssociateProductWithPortfolioInputRequestTypeDef = TypedDict(
    "AssociateProductWithPortfolioInputRequestTypeDef",
    {
        "ProductId": str,
        "PortfolioId": str,
        "AcceptLanguage": NotRequired[str],
        "SourcePortfolioId": NotRequired[str],
    },
)
AssociateServiceActionWithProvisioningArtifactInputRequestTypeDef = TypedDict(
    "AssociateServiceActionWithProvisioningArtifactInputRequestTypeDef",
    {
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "ServiceActionId": str,
        "AcceptLanguage": NotRequired[str],
        "IdempotencyToken": NotRequired[str],
    },
)
AssociateTagOptionWithResourceInputRequestTypeDef = TypedDict(
    "AssociateTagOptionWithResourceInputRequestTypeDef",
    {
        "ResourceId": str,
        "TagOptionId": str,
    },
)
ServiceActionAssociationTypeDef = TypedDict(
    "ServiceActionAssociationTypeDef",
    {
        "ServiceActionId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
    },
)
FailedServiceActionAssociationTypeDef = TypedDict(
    "FailedServiceActionAssociationTypeDef",
    {
        "ServiceActionId": NotRequired[str],
        "ProductId": NotRequired[str],
        "ProvisioningArtifactId": NotRequired[str],
        "ErrorCode": NotRequired[ServiceActionAssociationErrorCodeType],
        "ErrorMessage": NotRequired[str],
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
BudgetDetailTypeDef = TypedDict(
    "BudgetDetailTypeDef",
    {
        "BudgetName": NotRequired[str],
    },
)
CloudWatchDashboardTypeDef = TypedDict(
    "CloudWatchDashboardTypeDef",
    {
        "Name": NotRequired[str],
    },
)
CodeStarParametersTypeDef = TypedDict(
    "CodeStarParametersTypeDef",
    {
        "ConnectionArn": str,
        "Repository": str,
        "Branch": str,
        "ArtifactPath": str,
    },
)
ConstraintDetailTypeDef = TypedDict(
    "ConstraintDetailTypeDef",
    {
        "ConstraintId": NotRequired[str],
        "Type": NotRequired[str],
        "Description": NotRequired[str],
        "Owner": NotRequired[str],
        "ProductId": NotRequired[str],
        "PortfolioId": NotRequired[str],
    },
)
ConstraintSummaryTypeDef = TypedDict(
    "ConstraintSummaryTypeDef",
    {
        "Type": NotRequired[str],
        "Description": NotRequired[str],
    },
)
CopyProductInputRequestTypeDef = TypedDict(
    "CopyProductInputRequestTypeDef",
    {
        "SourceProductArn": str,
        "IdempotencyToken": str,
        "AcceptLanguage": NotRequired[str],
        "TargetProductId": NotRequired[str],
        "TargetProductName": NotRequired[str],
        "SourceProvisioningArtifactIdentifiers": NotRequired[Sequence[Mapping[Literal["Id"], str]]],
        "CopyOptions": NotRequired[Sequence[Literal["CopyTags"]]],
    },
)
CreateConstraintInputRequestTypeDef = TypedDict(
    "CreateConstraintInputRequestTypeDef",
    {
        "PortfolioId": str,
        "ProductId": str,
        "Parameters": str,
        "Type": str,
        "IdempotencyToken": str,
        "AcceptLanguage": NotRequired[str],
        "Description": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
PortfolioDetailTypeDef = TypedDict(
    "PortfolioDetailTypeDef",
    {
        "Id": NotRequired[str],
        "ARN": NotRequired[str],
        "DisplayName": NotRequired[str],
        "Description": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "ProviderName": NotRequired[str],
    },
)
OrganizationNodeTypeDef = TypedDict(
    "OrganizationNodeTypeDef",
    {
        "Type": NotRequired[OrganizationNodeTypeType],
        "Value": NotRequired[str],
    },
)
ProvisioningArtifactPropertiesTypeDef = TypedDict(
    "ProvisioningArtifactPropertiesTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Info": NotRequired[Mapping[str, str]],
        "Type": NotRequired[ProvisioningArtifactTypeType],
        "DisableTemplateValidation": NotRequired[bool],
    },
)
ProvisioningArtifactDetailTypeDef = TypedDict(
    "ProvisioningArtifactDetailTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Type": NotRequired[ProvisioningArtifactTypeType],
        "CreatedTime": NotRequired[datetime],
        "Active": NotRequired[bool],
        "Guidance": NotRequired[ProvisioningArtifactGuidanceType],
        "SourceRevision": NotRequired[str],
    },
)
UpdateProvisioningParameterTypeDef = TypedDict(
    "UpdateProvisioningParameterTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
        "UsePreviousValue": NotRequired[bool],
    },
)
CreateServiceActionInputRequestTypeDef = TypedDict(
    "CreateServiceActionInputRequestTypeDef",
    {
        "Name": str,
        "DefinitionType": Literal["SSM_AUTOMATION"],
        "Definition": Mapping[ServiceActionDefinitionKeyType, str],
        "IdempotencyToken": str,
        "Description": NotRequired[str],
        "AcceptLanguage": NotRequired[str],
    },
)
CreateTagOptionInputRequestTypeDef = TypedDict(
    "CreateTagOptionInputRequestTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
TagOptionDetailTypeDef = TypedDict(
    "TagOptionDetailTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
        "Active": NotRequired[bool],
        "Id": NotRequired[str],
        "Owner": NotRequired[str],
    },
)
DeleteConstraintInputRequestTypeDef = TypedDict(
    "DeleteConstraintInputRequestTypeDef",
    {
        "Id": str,
        "AcceptLanguage": NotRequired[str],
    },
)
DeletePortfolioInputRequestTypeDef = TypedDict(
    "DeletePortfolioInputRequestTypeDef",
    {
        "Id": str,
        "AcceptLanguage": NotRequired[str],
    },
)
DeleteProductInputRequestTypeDef = TypedDict(
    "DeleteProductInputRequestTypeDef",
    {
        "Id": str,
        "AcceptLanguage": NotRequired[str],
    },
)
DeleteProvisionedProductPlanInputRequestTypeDef = TypedDict(
    "DeleteProvisionedProductPlanInputRequestTypeDef",
    {
        "PlanId": str,
        "AcceptLanguage": NotRequired[str],
        "IgnoreErrors": NotRequired[bool],
    },
)
DeleteProvisioningArtifactInputRequestTypeDef = TypedDict(
    "DeleteProvisioningArtifactInputRequestTypeDef",
    {
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "AcceptLanguage": NotRequired[str],
    },
)
DeleteServiceActionInputRequestTypeDef = TypedDict(
    "DeleteServiceActionInputRequestTypeDef",
    {
        "Id": str,
        "AcceptLanguage": NotRequired[str],
        "IdempotencyToken": NotRequired[str],
    },
)
DeleteTagOptionInputRequestTypeDef = TypedDict(
    "DeleteTagOptionInputRequestTypeDef",
    {
        "Id": str,
    },
)
DescribeConstraintInputRequestTypeDef = TypedDict(
    "DescribeConstraintInputRequestTypeDef",
    {
        "Id": str,
        "AcceptLanguage": NotRequired[str],
    },
)
DescribeCopyProductStatusInputRequestTypeDef = TypedDict(
    "DescribeCopyProductStatusInputRequestTypeDef",
    {
        "CopyProductToken": str,
        "AcceptLanguage": NotRequired[str],
    },
)
DescribePortfolioInputRequestTypeDef = TypedDict(
    "DescribePortfolioInputRequestTypeDef",
    {
        "Id": str,
        "AcceptLanguage": NotRequired[str],
    },
)
DescribePortfolioShareStatusInputRequestTypeDef = TypedDict(
    "DescribePortfolioShareStatusInputRequestTypeDef",
    {
        "PortfolioShareToken": str,
    },
)
DescribePortfolioSharesInputRequestTypeDef = TypedDict(
    "DescribePortfolioSharesInputRequestTypeDef",
    {
        "PortfolioId": str,
        "Type": DescribePortfolioShareTypeType,
        "PageToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
PortfolioShareDetailTypeDef = TypedDict(
    "PortfolioShareDetailTypeDef",
    {
        "PrincipalId": NotRequired[str],
        "Type": NotRequired[DescribePortfolioShareTypeType],
        "Accepted": NotRequired[bool],
        "ShareTagOptions": NotRequired[bool],
        "SharePrincipals": NotRequired[bool],
    },
)
DescribeProductAsAdminInputRequestTypeDef = TypedDict(
    "DescribeProductAsAdminInputRequestTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "SourcePortfolioId": NotRequired[str],
    },
)
ProvisioningArtifactSummaryTypeDef = TypedDict(
    "ProvisioningArtifactSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "ProvisioningArtifactMetadata": NotRequired[Dict[str, str]],
    },
)
DescribeProductInputRequestTypeDef = TypedDict(
    "DescribeProductInputRequestTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
    },
)
LaunchPathTypeDef = TypedDict(
    "LaunchPathTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
    },
)
ProductViewSummaryTypeDef = TypedDict(
    "ProductViewSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "ProductId": NotRequired[str],
        "Name": NotRequired[str],
        "Owner": NotRequired[str],
        "ShortDescription": NotRequired[str],
        "Type": NotRequired[ProductTypeType],
        "Distributor": NotRequired[str],
        "HasDefaultPath": NotRequired[bool],
        "SupportEmail": NotRequired[str],
        "SupportDescription": NotRequired[str],
        "SupportUrl": NotRequired[str],
    },
)
ProvisioningArtifactTypeDef = TypedDict(
    "ProvisioningArtifactTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "Guidance": NotRequired[ProvisioningArtifactGuidanceType],
    },
)
DescribeProductViewInputRequestTypeDef = TypedDict(
    "DescribeProductViewInputRequestTypeDef",
    {
        "Id": str,
        "AcceptLanguage": NotRequired[str],
    },
)
DescribeProvisionedProductInputRequestTypeDef = TypedDict(
    "DescribeProvisionedProductInputRequestTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
    },
)
ProvisionedProductDetailTypeDef = TypedDict(
    "ProvisionedProductDetailTypeDef",
    {
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "Type": NotRequired[str],
        "Id": NotRequired[str],
        "Status": NotRequired[ProvisionedProductStatusType],
        "StatusMessage": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "IdempotencyToken": NotRequired[str],
        "LastRecordId": NotRequired[str],
        "LastProvisioningRecordId": NotRequired[str],
        "LastSuccessfulProvisioningRecordId": NotRequired[str],
        "ProductId": NotRequired[str],
        "ProvisioningArtifactId": NotRequired[str],
        "LaunchRoleArn": NotRequired[str],
    },
)
DescribeProvisionedProductPlanInputRequestTypeDef = TypedDict(
    "DescribeProvisionedProductPlanInputRequestTypeDef",
    {
        "PlanId": str,
        "AcceptLanguage": NotRequired[str],
        "PageSize": NotRequired[int],
        "PageToken": NotRequired[str],
    },
)
DescribeProvisioningArtifactInputRequestTypeDef = TypedDict(
    "DescribeProvisioningArtifactInputRequestTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "ProvisioningArtifactId": NotRequired[str],
        "ProductId": NotRequired[str],
        "ProvisioningArtifactName": NotRequired[str],
        "ProductName": NotRequired[str],
        "Verbose": NotRequired[bool],
        "IncludeProvisioningArtifactParameters": NotRequired[bool],
    },
)
DescribeProvisioningParametersInputRequestTypeDef = TypedDict(
    "DescribeProvisioningParametersInputRequestTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "ProductId": NotRequired[str],
        "ProductName": NotRequired[str],
        "ProvisioningArtifactId": NotRequired[str],
        "ProvisioningArtifactName": NotRequired[str],
        "PathId": NotRequired[str],
        "PathName": NotRequired[str],
    },
)
ProvisioningArtifactOutputTypeDef = TypedDict(
    "ProvisioningArtifactOutputTypeDef",
    {
        "Key": NotRequired[str],
        "Description": NotRequired[str],
    },
)
ProvisioningArtifactPreferencesTypeDef = TypedDict(
    "ProvisioningArtifactPreferencesTypeDef",
    {
        "StackSetAccounts": NotRequired[List[str]],
        "StackSetRegions": NotRequired[List[str]],
    },
)
TagOptionSummaryTypeDef = TypedDict(
    "TagOptionSummaryTypeDef",
    {
        "Key": NotRequired[str],
        "Values": NotRequired[List[str]],
    },
)
UsageInstructionTypeDef = TypedDict(
    "UsageInstructionTypeDef",
    {
        "Type": NotRequired[str],
        "Value": NotRequired[str],
    },
)
DescribeRecordInputRequestTypeDef = TypedDict(
    "DescribeRecordInputRequestTypeDef",
    {
        "Id": str,
        "AcceptLanguage": NotRequired[str],
        "PageToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
RecordOutputTypeDef = TypedDict(
    "RecordOutputTypeDef",
    {
        "OutputKey": NotRequired[str],
        "OutputValue": NotRequired[str],
        "Description": NotRequired[str],
    },
)
DescribeServiceActionExecutionParametersInputRequestTypeDef = TypedDict(
    "DescribeServiceActionExecutionParametersInputRequestTypeDef",
    {
        "ProvisionedProductId": str,
        "ServiceActionId": str,
        "AcceptLanguage": NotRequired[str],
    },
)
ExecutionParameterTypeDef = TypedDict(
    "ExecutionParameterTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
        "DefaultValues": NotRequired[List[str]],
    },
)
DescribeServiceActionInputRequestTypeDef = TypedDict(
    "DescribeServiceActionInputRequestTypeDef",
    {
        "Id": str,
        "AcceptLanguage": NotRequired[str],
    },
)
DescribeTagOptionInputRequestTypeDef = TypedDict(
    "DescribeTagOptionInputRequestTypeDef",
    {
        "Id": str,
    },
)
DisassociateBudgetFromResourceInputRequestTypeDef = TypedDict(
    "DisassociateBudgetFromResourceInputRequestTypeDef",
    {
        "BudgetName": str,
        "ResourceId": str,
    },
)
DisassociatePrincipalFromPortfolioInputRequestTypeDef = TypedDict(
    "DisassociatePrincipalFromPortfolioInputRequestTypeDef",
    {
        "PortfolioId": str,
        "PrincipalARN": str,
        "AcceptLanguage": NotRequired[str],
        "PrincipalType": NotRequired[PrincipalTypeType],
    },
)
DisassociateProductFromPortfolioInputRequestTypeDef = TypedDict(
    "DisassociateProductFromPortfolioInputRequestTypeDef",
    {
        "ProductId": str,
        "PortfolioId": str,
        "AcceptLanguage": NotRequired[str],
    },
)
DisassociateServiceActionFromProvisioningArtifactInputRequestTypeDef = TypedDict(
    "DisassociateServiceActionFromProvisioningArtifactInputRequestTypeDef",
    {
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "ServiceActionId": str,
        "AcceptLanguage": NotRequired[str],
        "IdempotencyToken": NotRequired[str],
    },
)
DisassociateTagOptionFromResourceInputRequestTypeDef = TypedDict(
    "DisassociateTagOptionFromResourceInputRequestTypeDef",
    {
        "ResourceId": str,
        "TagOptionId": str,
    },
)
UniqueTagResourceIdentifierTypeDef = TypedDict(
    "UniqueTagResourceIdentifierTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
ExecuteProvisionedProductPlanInputRequestTypeDef = TypedDict(
    "ExecuteProvisionedProductPlanInputRequestTypeDef",
    {
        "PlanId": str,
        "IdempotencyToken": str,
        "AcceptLanguage": NotRequired[str],
    },
)
ExecuteProvisionedProductServiceActionInputRequestTypeDef = TypedDict(
    "ExecuteProvisionedProductServiceActionInputRequestTypeDef",
    {
        "ProvisionedProductId": str,
        "ServiceActionId": str,
        "ExecuteToken": str,
        "AcceptLanguage": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, Sequence[str]]],
    },
)
GetProvisionedProductOutputsInputRequestTypeDef = TypedDict(
    "GetProvisionedProductOutputsInputRequestTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "ProvisionedProductId": NotRequired[str],
        "ProvisionedProductName": NotRequired[str],
        "OutputKeys": NotRequired[Sequence[str]],
        "PageSize": NotRequired[int],
        "PageToken": NotRequired[str],
    },
)
ImportAsProvisionedProductInputRequestTypeDef = TypedDict(
    "ImportAsProvisionedProductInputRequestTypeDef",
    {
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "ProvisionedProductName": str,
        "PhysicalId": str,
        "IdempotencyToken": str,
        "AcceptLanguage": NotRequired[str],
    },
)
LastSyncTypeDef = TypedDict(
    "LastSyncTypeDef",
    {
        "LastSyncTime": NotRequired[datetime],
        "LastSyncStatus": NotRequired[LastSyncStatusType],
        "LastSyncStatusMessage": NotRequired[str],
        "LastSuccessfulSyncTime": NotRequired[datetime],
        "LastSuccessfulSyncProvisioningArtifactId": NotRequired[str],
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
ListAcceptedPortfolioSharesInputRequestTypeDef = TypedDict(
    "ListAcceptedPortfolioSharesInputRequestTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "PageToken": NotRequired[str],
        "PageSize": NotRequired[int],
        "PortfolioShareType": NotRequired[PortfolioShareTypeType],
    },
)
ListBudgetsForResourceInputRequestTypeDef = TypedDict(
    "ListBudgetsForResourceInputRequestTypeDef",
    {
        "ResourceId": str,
        "AcceptLanguage": NotRequired[str],
        "PageSize": NotRequired[int],
        "PageToken": NotRequired[str],
    },
)
ListConstraintsForPortfolioInputRequestTypeDef = TypedDict(
    "ListConstraintsForPortfolioInputRequestTypeDef",
    {
        "PortfolioId": str,
        "AcceptLanguage": NotRequired[str],
        "ProductId": NotRequired[str],
        "PageSize": NotRequired[int],
        "PageToken": NotRequired[str],
    },
)
ListLaunchPathsInputRequestTypeDef = TypedDict(
    "ListLaunchPathsInputRequestTypeDef",
    {
        "ProductId": str,
        "AcceptLanguage": NotRequired[str],
        "PageSize": NotRequired[int],
        "PageToken": NotRequired[str],
    },
)
ListOrganizationPortfolioAccessInputRequestTypeDef = TypedDict(
    "ListOrganizationPortfolioAccessInputRequestTypeDef",
    {
        "PortfolioId": str,
        "OrganizationNodeType": OrganizationNodeTypeType,
        "AcceptLanguage": NotRequired[str],
        "PageToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
ListPortfolioAccessInputRequestTypeDef = TypedDict(
    "ListPortfolioAccessInputRequestTypeDef",
    {
        "PortfolioId": str,
        "AcceptLanguage": NotRequired[str],
        "OrganizationParentId": NotRequired[str],
        "PageToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
ListPortfoliosForProductInputRequestTypeDef = TypedDict(
    "ListPortfoliosForProductInputRequestTypeDef",
    {
        "ProductId": str,
        "AcceptLanguage": NotRequired[str],
        "PageToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
ListPortfoliosInputRequestTypeDef = TypedDict(
    "ListPortfoliosInputRequestTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "PageToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
ListPrincipalsForPortfolioInputRequestTypeDef = TypedDict(
    "ListPrincipalsForPortfolioInputRequestTypeDef",
    {
        "PortfolioId": str,
        "AcceptLanguage": NotRequired[str],
        "PageSize": NotRequired[int],
        "PageToken": NotRequired[str],
    },
)
PrincipalTypeDef = TypedDict(
    "PrincipalTypeDef",
    {
        "PrincipalARN": NotRequired[str],
        "PrincipalType": NotRequired[PrincipalTypeType],
    },
)
ProvisionedProductPlanSummaryTypeDef = TypedDict(
    "ProvisionedProductPlanSummaryTypeDef",
    {
        "PlanName": NotRequired[str],
        "PlanId": NotRequired[str],
        "ProvisionProductId": NotRequired[str],
        "ProvisionProductName": NotRequired[str],
        "PlanType": NotRequired[Literal["CLOUDFORMATION"]],
        "ProvisioningArtifactId": NotRequired[str],
    },
)
ListProvisioningArtifactsForServiceActionInputRequestTypeDef = TypedDict(
    "ListProvisioningArtifactsForServiceActionInputRequestTypeDef",
    {
        "ServiceActionId": str,
        "PageSize": NotRequired[int],
        "PageToken": NotRequired[str],
        "AcceptLanguage": NotRequired[str],
    },
)
ListProvisioningArtifactsInputRequestTypeDef = TypedDict(
    "ListProvisioningArtifactsInputRequestTypeDef",
    {
        "ProductId": str,
        "AcceptLanguage": NotRequired[str],
    },
)
ListRecordHistorySearchFilterTypeDef = TypedDict(
    "ListRecordHistorySearchFilterTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
ListResourcesForTagOptionInputRequestTypeDef = TypedDict(
    "ListResourcesForTagOptionInputRequestTypeDef",
    {
        "TagOptionId": str,
        "ResourceType": NotRequired[str],
        "PageSize": NotRequired[int],
        "PageToken": NotRequired[str],
    },
)
ResourceDetailTypeDef = TypedDict(
    "ResourceDetailTypeDef",
    {
        "Id": NotRequired[str],
        "ARN": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
    },
)
ListServiceActionsForProvisioningArtifactInputRequestTypeDef = TypedDict(
    "ListServiceActionsForProvisioningArtifactInputRequestTypeDef",
    {
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "PageSize": NotRequired[int],
        "PageToken": NotRequired[str],
        "AcceptLanguage": NotRequired[str],
    },
)
ServiceActionSummaryTypeDef = TypedDict(
    "ServiceActionSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "DefinitionType": NotRequired[Literal["SSM_AUTOMATION"]],
    },
)
ListServiceActionsInputRequestTypeDef = TypedDict(
    "ListServiceActionsInputRequestTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "PageSize": NotRequired[int],
        "PageToken": NotRequired[str],
    },
)
ListStackInstancesForProvisionedProductInputRequestTypeDef = TypedDict(
    "ListStackInstancesForProvisionedProductInputRequestTypeDef",
    {
        "ProvisionedProductId": str,
        "AcceptLanguage": NotRequired[str],
        "PageToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)
StackInstanceTypeDef = TypedDict(
    "StackInstanceTypeDef",
    {
        "Account": NotRequired[str],
        "Region": NotRequired[str],
        "StackInstanceStatus": NotRequired[StackInstanceStatusType],
    },
)
ListTagOptionsFiltersTypeDef = TypedDict(
    "ListTagOptionsFiltersTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
        "Active": NotRequired[bool],
    },
)
NotifyTerminateProvisionedProductEngineWorkflowResultInputRequestTypeDef = TypedDict(
    "NotifyTerminateProvisionedProductEngineWorkflowResultInputRequestTypeDef",
    {
        "WorkflowToken": str,
        "RecordId": str,
        "Status": EngineWorkflowStatusType,
        "IdempotencyToken": str,
        "FailureReason": NotRequired[str],
    },
)
ParameterConstraintsTypeDef = TypedDict(
    "ParameterConstraintsTypeDef",
    {
        "AllowedValues": NotRequired[List[str]],
        "AllowedPattern": NotRequired[str],
        "ConstraintDescription": NotRequired[str],
        "MaxLength": NotRequired[str],
        "MinLength": NotRequired[str],
        "MaxValue": NotRequired[str],
        "MinValue": NotRequired[str],
    },
)
ProductViewAggregationValueTypeDef = TypedDict(
    "ProductViewAggregationValueTypeDef",
    {
        "Value": NotRequired[str],
        "ApproximateCount": NotRequired[int],
    },
)
ProvisioningParameterTypeDef = TypedDict(
    "ProvisioningParameterTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
ProvisioningPreferencesTypeDef = TypedDict(
    "ProvisioningPreferencesTypeDef",
    {
        "StackSetAccounts": NotRequired[Sequence[str]],
        "StackSetRegions": NotRequired[Sequence[str]],
        "StackSetFailureToleranceCount": NotRequired[int],
        "StackSetFailureTolerancePercentage": NotRequired[int],
        "StackSetMaxConcurrencyCount": NotRequired[int],
        "StackSetMaxConcurrencyPercentage": NotRequired[int],
    },
)
RecordErrorTypeDef = TypedDict(
    "RecordErrorTypeDef",
    {
        "Code": NotRequired[str],
        "Description": NotRequired[str],
    },
)
RecordTagTypeDef = TypedDict(
    "RecordTagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
RejectPortfolioShareInputRequestTypeDef = TypedDict(
    "RejectPortfolioShareInputRequestTypeDef",
    {
        "PortfolioId": str,
        "AcceptLanguage": NotRequired[str],
        "PortfolioShareType": NotRequired[PortfolioShareTypeType],
    },
)
ResourceTargetDefinitionTypeDef = TypedDict(
    "ResourceTargetDefinitionTypeDef",
    {
        "Attribute": NotRequired[ResourceAttributeType],
        "Name": NotRequired[str],
        "RequiresRecreation": NotRequired[RequiresRecreationType],
    },
)
SearchProductsAsAdminInputRequestTypeDef = TypedDict(
    "SearchProductsAsAdminInputRequestTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "PortfolioId": NotRequired[str],
        "Filters": NotRequired[Mapping[ProductViewFilterByType, Sequence[str]]],
        "SortBy": NotRequired[ProductViewSortByType],
        "SortOrder": NotRequired[SortOrderType],
        "PageToken": NotRequired[str],
        "PageSize": NotRequired[int],
        "ProductSource": NotRequired[Literal["ACCOUNT"]],
    },
)
SearchProductsInputRequestTypeDef = TypedDict(
    "SearchProductsInputRequestTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "Filters": NotRequired[Mapping[ProductViewFilterByType, Sequence[str]]],
        "PageSize": NotRequired[int],
        "SortBy": NotRequired[ProductViewSortByType],
        "SortOrder": NotRequired[SortOrderType],
        "PageToken": NotRequired[str],
    },
)
ShareErrorTypeDef = TypedDict(
    "ShareErrorTypeDef",
    {
        "Accounts": NotRequired[List[str]],
        "Message": NotRequired[str],
        "Error": NotRequired[str],
    },
)
TerminateProvisionedProductInputRequestTypeDef = TypedDict(
    "TerminateProvisionedProductInputRequestTypeDef",
    {
        "TerminateToken": str,
        "ProvisionedProductName": NotRequired[str],
        "ProvisionedProductId": NotRequired[str],
        "IgnoreErrors": NotRequired[bool],
        "AcceptLanguage": NotRequired[str],
        "RetainPhysicalResources": NotRequired[bool],
    },
)
UpdateConstraintInputRequestTypeDef = TypedDict(
    "UpdateConstraintInputRequestTypeDef",
    {
        "Id": str,
        "AcceptLanguage": NotRequired[str],
        "Description": NotRequired[str],
        "Parameters": NotRequired[str],
    },
)
UpdateProvisioningPreferencesTypeDef = TypedDict(
    "UpdateProvisioningPreferencesTypeDef",
    {
        "StackSetAccounts": NotRequired[Sequence[str]],
        "StackSetRegions": NotRequired[Sequence[str]],
        "StackSetFailureToleranceCount": NotRequired[int],
        "StackSetFailureTolerancePercentage": NotRequired[int],
        "StackSetMaxConcurrencyCount": NotRequired[int],
        "StackSetMaxConcurrencyPercentage": NotRequired[int],
        "StackSetOperationType": NotRequired[StackSetOperationTypeType],
    },
)
UpdateProvisionedProductPropertiesInputRequestTypeDef = TypedDict(
    "UpdateProvisionedProductPropertiesInputRequestTypeDef",
    {
        "ProvisionedProductId": str,
        "ProvisionedProductProperties": Mapping[PropertyKeyType, str],
        "IdempotencyToken": str,
        "AcceptLanguage": NotRequired[str],
    },
)
UpdateProvisioningArtifactInputRequestTypeDef = TypedDict(
    "UpdateProvisioningArtifactInputRequestTypeDef",
    {
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "AcceptLanguage": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Active": NotRequired[bool],
        "Guidance": NotRequired[ProvisioningArtifactGuidanceType],
    },
)
UpdateServiceActionInputRequestTypeDef = TypedDict(
    "UpdateServiceActionInputRequestTypeDef",
    {
        "Id": str,
        "Name": NotRequired[str],
        "Definition": NotRequired[Mapping[ServiceActionDefinitionKeyType, str]],
        "Description": NotRequired[str],
        "AcceptLanguage": NotRequired[str],
    },
)
UpdateTagOptionInputRequestTypeDef = TypedDict(
    "UpdateTagOptionInputRequestTypeDef",
    {
        "Id": str,
        "Value": NotRequired[str],
        "Active": NotRequired[bool],
    },
)
ListProvisionedProductPlansInputRequestTypeDef = TypedDict(
    "ListProvisionedProductPlansInputRequestTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "ProvisionProductId": NotRequired[str],
        "PageSize": NotRequired[int],
        "PageToken": NotRequired[str],
        "AccessLevelFilter": NotRequired[AccessLevelFilterTypeDef],
    },
)
ScanProvisionedProductsInputRequestTypeDef = TypedDict(
    "ScanProvisionedProductsInputRequestTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "AccessLevelFilter": NotRequired[AccessLevelFilterTypeDef],
        "PageSize": NotRequired[int],
        "PageToken": NotRequired[str],
    },
)
SearchProvisionedProductsInputRequestTypeDef = TypedDict(
    "SearchProvisionedProductsInputRequestTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "AccessLevelFilter": NotRequired[AccessLevelFilterTypeDef],
        "Filters": NotRequired[Mapping[Literal["SearchQuery"], Sequence[str]]],
        "SortBy": NotRequired[str],
        "SortOrder": NotRequired[SortOrderType],
        "PageSize": NotRequired[int],
        "PageToken": NotRequired[str],
    },
)
BatchAssociateServiceActionWithProvisioningArtifactInputRequestTypeDef = TypedDict(
    "BatchAssociateServiceActionWithProvisioningArtifactInputRequestTypeDef",
    {
        "ServiceActionAssociations": Sequence[ServiceActionAssociationTypeDef],
        "AcceptLanguage": NotRequired[str],
    },
)
BatchDisassociateServiceActionFromProvisioningArtifactInputRequestTypeDef = TypedDict(
    "BatchDisassociateServiceActionFromProvisioningArtifactInputRequestTypeDef",
    {
        "ServiceActionAssociations": Sequence[ServiceActionAssociationTypeDef],
        "AcceptLanguage": NotRequired[str],
    },
)
BatchAssociateServiceActionWithProvisioningArtifactOutputTypeDef = TypedDict(
    "BatchAssociateServiceActionWithProvisioningArtifactOutputTypeDef",
    {
        "FailedServiceActionAssociations": List[FailedServiceActionAssociationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDisassociateServiceActionFromProvisioningArtifactOutputTypeDef = TypedDict(
    "BatchDisassociateServiceActionFromProvisioningArtifactOutputTypeDef",
    {
        "FailedServiceActionAssociations": List[FailedServiceActionAssociationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CopyProductOutputTypeDef = TypedDict(
    "CopyProductOutputTypeDef",
    {
        "CopyProductToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePortfolioShareOutputTypeDef = TypedDict(
    "CreatePortfolioShareOutputTypeDef",
    {
        "PortfolioShareToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProvisionedProductPlanOutputTypeDef = TypedDict(
    "CreateProvisionedProductPlanOutputTypeDef",
    {
        "PlanName": str,
        "PlanId": str,
        "ProvisionProductId": str,
        "ProvisionedProductName": str,
        "ProvisioningArtifactId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeletePortfolioShareOutputTypeDef = TypedDict(
    "DeletePortfolioShareOutputTypeDef",
    {
        "PortfolioShareToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeCopyProductStatusOutputTypeDef = TypedDict(
    "DescribeCopyProductStatusOutputTypeDef",
    {
        "CopyProductStatus": CopyProductStatusType,
        "TargetProductId": str,
        "StatusDetail": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAWSOrganizationsAccessStatusOutputTypeDef = TypedDict(
    "GetAWSOrganizationsAccessStatusOutputTypeDef",
    {
        "AccessStatus": AccessStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPortfolioAccessOutputTypeDef = TypedDict(
    "ListPortfolioAccessOutputTypeDef",
    {
        "AccountIds": List[str],
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePortfolioShareOutputTypeDef = TypedDict(
    "UpdatePortfolioShareOutputTypeDef",
    {
        "PortfolioShareToken": str,
        "Status": ShareStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateProvisionedProductPropertiesOutputTypeDef = TypedDict(
    "UpdateProvisionedProductPropertiesOutputTypeDef",
    {
        "ProvisionedProductId": str,
        "ProvisionedProductProperties": Dict[PropertyKeyType, str],
        "RecordId": str,
        "Status": RecordStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListBudgetsForResourceOutputTypeDef = TypedDict(
    "ListBudgetsForResourceOutputTypeDef",
    {
        "Budgets": List[BudgetDetailTypeDef],
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SourceConnectionParametersTypeDef = TypedDict(
    "SourceConnectionParametersTypeDef",
    {
        "CodeStar": NotRequired[CodeStarParametersTypeDef],
    },
)
CreateConstraintOutputTypeDef = TypedDict(
    "CreateConstraintOutputTypeDef",
    {
        "ConstraintDetail": ConstraintDetailTypeDef,
        "ConstraintParameters": str,
        "Status": StatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeConstraintOutputTypeDef = TypedDict(
    "DescribeConstraintOutputTypeDef",
    {
        "ConstraintDetail": ConstraintDetailTypeDef,
        "ConstraintParameters": str,
        "Status": StatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListConstraintsForPortfolioOutputTypeDef = TypedDict(
    "ListConstraintsForPortfolioOutputTypeDef",
    {
        "ConstraintDetails": List[ConstraintDetailTypeDef],
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateConstraintOutputTypeDef = TypedDict(
    "UpdateConstraintOutputTypeDef",
    {
        "ConstraintDetail": ConstraintDetailTypeDef,
        "ConstraintParameters": str,
        "Status": StatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePortfolioInputRequestTypeDef = TypedDict(
    "CreatePortfolioInputRequestTypeDef",
    {
        "DisplayName": str,
        "ProviderName": str,
        "IdempotencyToken": str,
        "AcceptLanguage": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
LaunchPathSummaryTypeDef = TypedDict(
    "LaunchPathSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "ConstraintSummaries": NotRequired[List[ConstraintSummaryTypeDef]],
        "Tags": NotRequired[List[TagTypeDef]],
        "Name": NotRequired[str],
    },
)
ProvisionedProductAttributeTypeDef = TypedDict(
    "ProvisionedProductAttributeTypeDef",
    {
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "Type": NotRequired[str],
        "Id": NotRequired[str],
        "Status": NotRequired[ProvisionedProductStatusType],
        "StatusMessage": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "IdempotencyToken": NotRequired[str],
        "LastRecordId": NotRequired[str],
        "LastProvisioningRecordId": NotRequired[str],
        "LastSuccessfulProvisioningRecordId": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "PhysicalId": NotRequired[str],
        "ProductId": NotRequired[str],
        "ProductName": NotRequired[str],
        "ProvisioningArtifactId": NotRequired[str],
        "ProvisioningArtifactName": NotRequired[str],
        "UserArn": NotRequired[str],
        "UserArnSession": NotRequired[str],
    },
)
UpdatePortfolioInputRequestTypeDef = TypedDict(
    "UpdatePortfolioInputRequestTypeDef",
    {
        "Id": str,
        "AcceptLanguage": NotRequired[str],
        "DisplayName": NotRequired[str],
        "Description": NotRequired[str],
        "ProviderName": NotRequired[str],
        "AddTags": NotRequired[Sequence[TagTypeDef]],
        "RemoveTags": NotRequired[Sequence[str]],
    },
)
CreatePortfolioOutputTypeDef = TypedDict(
    "CreatePortfolioOutputTypeDef",
    {
        "PortfolioDetail": PortfolioDetailTypeDef,
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAcceptedPortfolioSharesOutputTypeDef = TypedDict(
    "ListAcceptedPortfolioSharesOutputTypeDef",
    {
        "PortfolioDetails": List[PortfolioDetailTypeDef],
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPortfoliosForProductOutputTypeDef = TypedDict(
    "ListPortfoliosForProductOutputTypeDef",
    {
        "PortfolioDetails": List[PortfolioDetailTypeDef],
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPortfoliosOutputTypeDef = TypedDict(
    "ListPortfoliosOutputTypeDef",
    {
        "PortfolioDetails": List[PortfolioDetailTypeDef],
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePortfolioOutputTypeDef = TypedDict(
    "UpdatePortfolioOutputTypeDef",
    {
        "PortfolioDetail": PortfolioDetailTypeDef,
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePortfolioShareInputRequestTypeDef = TypedDict(
    "CreatePortfolioShareInputRequestTypeDef",
    {
        "PortfolioId": str,
        "AcceptLanguage": NotRequired[str],
        "AccountId": NotRequired[str],
        "OrganizationNode": NotRequired[OrganizationNodeTypeDef],
        "ShareTagOptions": NotRequired[bool],
        "SharePrincipals": NotRequired[bool],
    },
)
DeletePortfolioShareInputRequestTypeDef = TypedDict(
    "DeletePortfolioShareInputRequestTypeDef",
    {
        "PortfolioId": str,
        "AcceptLanguage": NotRequired[str],
        "AccountId": NotRequired[str],
        "OrganizationNode": NotRequired[OrganizationNodeTypeDef],
    },
)
ListOrganizationPortfolioAccessOutputTypeDef = TypedDict(
    "ListOrganizationPortfolioAccessOutputTypeDef",
    {
        "OrganizationNodes": List[OrganizationNodeTypeDef],
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePortfolioShareInputRequestTypeDef = TypedDict(
    "UpdatePortfolioShareInputRequestTypeDef",
    {
        "PortfolioId": str,
        "AcceptLanguage": NotRequired[str],
        "AccountId": NotRequired[str],
        "OrganizationNode": NotRequired[OrganizationNodeTypeDef],
        "ShareTagOptions": NotRequired[bool],
        "SharePrincipals": NotRequired[bool],
    },
)
CreateProvisioningArtifactInputRequestTypeDef = TypedDict(
    "CreateProvisioningArtifactInputRequestTypeDef",
    {
        "ProductId": str,
        "Parameters": ProvisioningArtifactPropertiesTypeDef,
        "IdempotencyToken": str,
        "AcceptLanguage": NotRequired[str],
    },
)
CreateProvisioningArtifactOutputTypeDef = TypedDict(
    "CreateProvisioningArtifactOutputTypeDef",
    {
        "ProvisioningArtifactDetail": ProvisioningArtifactDetailTypeDef,
        "Info": Dict[str, str],
        "Status": StatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListProvisioningArtifactsOutputTypeDef = TypedDict(
    "ListProvisioningArtifactsOutputTypeDef",
    {
        "ProvisioningArtifactDetails": List[ProvisioningArtifactDetailTypeDef],
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateProvisioningArtifactOutputTypeDef = TypedDict(
    "UpdateProvisioningArtifactOutputTypeDef",
    {
        "ProvisioningArtifactDetail": ProvisioningArtifactDetailTypeDef,
        "Info": Dict[str, str],
        "Status": StatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProvisionedProductPlanInputRequestTypeDef = TypedDict(
    "CreateProvisionedProductPlanInputRequestTypeDef",
    {
        "PlanName": str,
        "PlanType": Literal["CLOUDFORMATION"],
        "ProductId": str,
        "ProvisionedProductName": str,
        "ProvisioningArtifactId": str,
        "IdempotencyToken": str,
        "AcceptLanguage": NotRequired[str],
        "NotificationArns": NotRequired[Sequence[str]],
        "PathId": NotRequired[str],
        "ProvisioningParameters": NotRequired[Sequence[UpdateProvisioningParameterTypeDef]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ProvisionedProductPlanDetailsTypeDef = TypedDict(
    "ProvisionedProductPlanDetailsTypeDef",
    {
        "CreatedTime": NotRequired[datetime],
        "PathId": NotRequired[str],
        "ProductId": NotRequired[str],
        "PlanName": NotRequired[str],
        "PlanId": NotRequired[str],
        "ProvisionProductId": NotRequired[str],
        "ProvisionProductName": NotRequired[str],
        "PlanType": NotRequired[Literal["CLOUDFORMATION"]],
        "ProvisioningArtifactId": NotRequired[str],
        "Status": NotRequired[ProvisionedProductPlanStatusType],
        "UpdatedTime": NotRequired[datetime],
        "NotificationArns": NotRequired[List[str]],
        "ProvisioningParameters": NotRequired[List[UpdateProvisioningParameterTypeDef]],
        "Tags": NotRequired[List[TagTypeDef]],
        "StatusMessage": NotRequired[str],
    },
)
CreateTagOptionOutputTypeDef = TypedDict(
    "CreateTagOptionOutputTypeDef",
    {
        "TagOptionDetail": TagOptionDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePortfolioOutputTypeDef = TypedDict(
    "DescribePortfolioOutputTypeDef",
    {
        "PortfolioDetail": PortfolioDetailTypeDef,
        "Tags": List[TagTypeDef],
        "TagOptions": List[TagOptionDetailTypeDef],
        "Budgets": List[BudgetDetailTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTagOptionOutputTypeDef = TypedDict(
    "DescribeTagOptionOutputTypeDef",
    {
        "TagOptionDetail": TagOptionDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagOptionsOutputTypeDef = TypedDict(
    "ListTagOptionsOutputTypeDef",
    {
        "TagOptionDetails": List[TagOptionDetailTypeDef],
        "PageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTagOptionOutputTypeDef = TypedDict(
    "UpdateTagOptionOutputTypeDef",
    {
        "TagOptionDetail": TagOptionDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePortfolioSharesOutputTypeDef = TypedDict(
    "DescribePortfolioSharesOutputTypeDef",
    {
        "NextPageToken": str,
        "PortfolioShareDetails": List[PortfolioShareDetailTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeProductOutputTypeDef = TypedDict(
    "DescribeProductOutputTypeDef",
    {
        "ProductViewSummary": ProductViewSummaryTypeDef,
        "ProvisioningArtifacts": List[ProvisioningArtifactTypeDef],
        "Budgets": List[BudgetDetailTypeDef],
        "LaunchPaths": List[LaunchPathTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeProductViewOutputTypeDef = TypedDict(
    "DescribeProductViewOutputTypeDef",
    {
        "ProductViewSummary": ProductViewSummaryTypeDef,
        "ProvisioningArtifacts": List[ProvisioningArtifactTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProvisioningArtifactViewTypeDef = TypedDict(
    "ProvisioningArtifactViewTypeDef",
    {
        "ProductViewSummary": NotRequired[ProductViewSummaryTypeDef],
        "ProvisioningArtifact": NotRequired[ProvisioningArtifactTypeDef],
    },
)
DescribeProvisionedProductOutputTypeDef = TypedDict(
    "DescribeProvisionedProductOutputTypeDef",
    {
        "ProvisionedProductDetail": ProvisionedProductDetailTypeDef,
        "CloudWatchDashboards": List[CloudWatchDashboardTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ScanProvisionedProductsOutputTypeDef = TypedDict(
    "ScanProvisionedProductsOutputTypeDef",
    {
        "ProvisionedProducts": List[ProvisionedProductDetailTypeDef],
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetProvisionedProductOutputsOutputTypeDef = TypedDict(
    "GetProvisionedProductOutputsOutputTypeDef",
    {
        "Outputs": List[RecordOutputTypeDef],
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NotifyUpdateProvisionedProductEngineWorkflowResultInputRequestTypeDef = TypedDict(
    "NotifyUpdateProvisionedProductEngineWorkflowResultInputRequestTypeDef",
    {
        "WorkflowToken": str,
        "RecordId": str,
        "Status": EngineWorkflowStatusType,
        "IdempotencyToken": str,
        "FailureReason": NotRequired[str],
        "Outputs": NotRequired[Sequence[RecordOutputTypeDef]],
    },
)
DescribeServiceActionExecutionParametersOutputTypeDef = TypedDict(
    "DescribeServiceActionExecutionParametersOutputTypeDef",
    {
        "ServiceActionParameters": List[ExecutionParameterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EngineWorkflowResourceIdentifierTypeDef = TypedDict(
    "EngineWorkflowResourceIdentifierTypeDef",
    {
        "UniqueTag": NotRequired[UniqueTagResourceIdentifierTypeDef],
    },
)
ListAcceptedPortfolioSharesInputListAcceptedPortfolioSharesPaginateTypeDef = TypedDict(
    "ListAcceptedPortfolioSharesInputListAcceptedPortfolioSharesPaginateTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "PortfolioShareType": NotRequired[PortfolioShareTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListConstraintsForPortfolioInputListConstraintsForPortfolioPaginateTypeDef = TypedDict(
    "ListConstraintsForPortfolioInputListConstraintsForPortfolioPaginateTypeDef",
    {
        "PortfolioId": str,
        "AcceptLanguage": NotRequired[str],
        "ProductId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListLaunchPathsInputListLaunchPathsPaginateTypeDef = TypedDict(
    "ListLaunchPathsInputListLaunchPathsPaginateTypeDef",
    {
        "ProductId": str,
        "AcceptLanguage": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOrganizationPortfolioAccessInputListOrganizationPortfolioAccessPaginateTypeDef = TypedDict(
    "ListOrganizationPortfolioAccessInputListOrganizationPortfolioAccessPaginateTypeDef",
    {
        "PortfolioId": str,
        "OrganizationNodeType": OrganizationNodeTypeType,
        "AcceptLanguage": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPortfoliosForProductInputListPortfoliosForProductPaginateTypeDef = TypedDict(
    "ListPortfoliosForProductInputListPortfoliosForProductPaginateTypeDef",
    {
        "ProductId": str,
        "AcceptLanguage": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPortfoliosInputListPortfoliosPaginateTypeDef = TypedDict(
    "ListPortfoliosInputListPortfoliosPaginateTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPrincipalsForPortfolioInputListPrincipalsForPortfolioPaginateTypeDef = TypedDict(
    "ListPrincipalsForPortfolioInputListPrincipalsForPortfolioPaginateTypeDef",
    {
        "PortfolioId": str,
        "AcceptLanguage": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProvisionedProductPlansInputListProvisionedProductPlansPaginateTypeDef = TypedDict(
    "ListProvisionedProductPlansInputListProvisionedProductPlansPaginateTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "ProvisionProductId": NotRequired[str],
        "AccessLevelFilter": NotRequired[AccessLevelFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProvisioningArtifactsForServiceActionInputListProvisioningArtifactsForServiceActionPaginateTypeDef = TypedDict(
    "ListProvisioningArtifactsForServiceActionInputListProvisioningArtifactsForServiceActionPaginateTypeDef",
    {
        "ServiceActionId": str,
        "AcceptLanguage": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResourcesForTagOptionInputListResourcesForTagOptionPaginateTypeDef = TypedDict(
    "ListResourcesForTagOptionInputListResourcesForTagOptionPaginateTypeDef",
    {
        "TagOptionId": str,
        "ResourceType": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListServiceActionsForProvisioningArtifactInputListServiceActionsForProvisioningArtifactPaginateTypeDef = TypedDict(
    "ListServiceActionsForProvisioningArtifactInputListServiceActionsForProvisioningArtifactPaginateTypeDef",
    {
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "AcceptLanguage": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListServiceActionsInputListServiceActionsPaginateTypeDef = TypedDict(
    "ListServiceActionsInputListServiceActionsPaginateTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ScanProvisionedProductsInputScanProvisionedProductsPaginateTypeDef = TypedDict(
    "ScanProvisionedProductsInputScanProvisionedProductsPaginateTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "AccessLevelFilter": NotRequired[AccessLevelFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchProductsAsAdminInputSearchProductsAsAdminPaginateTypeDef = TypedDict(
    "SearchProductsAsAdminInputSearchProductsAsAdminPaginateTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "PortfolioId": NotRequired[str],
        "Filters": NotRequired[Mapping[ProductViewFilterByType, Sequence[str]]],
        "SortBy": NotRequired[ProductViewSortByType],
        "SortOrder": NotRequired[SortOrderType],
        "ProductSource": NotRequired[Literal["ACCOUNT"]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPrincipalsForPortfolioOutputTypeDef = TypedDict(
    "ListPrincipalsForPortfolioOutputTypeDef",
    {
        "Principals": List[PrincipalTypeDef],
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListProvisionedProductPlansOutputTypeDef = TypedDict(
    "ListProvisionedProductPlansOutputTypeDef",
    {
        "ProvisionedProductPlans": List[ProvisionedProductPlanSummaryTypeDef],
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRecordHistoryInputListRecordHistoryPaginateTypeDef = TypedDict(
    "ListRecordHistoryInputListRecordHistoryPaginateTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "AccessLevelFilter": NotRequired[AccessLevelFilterTypeDef],
        "SearchFilter": NotRequired[ListRecordHistorySearchFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRecordHistoryInputRequestTypeDef = TypedDict(
    "ListRecordHistoryInputRequestTypeDef",
    {
        "AcceptLanguage": NotRequired[str],
        "AccessLevelFilter": NotRequired[AccessLevelFilterTypeDef],
        "SearchFilter": NotRequired[ListRecordHistorySearchFilterTypeDef],
        "PageSize": NotRequired[int],
        "PageToken": NotRequired[str],
    },
)
ListResourcesForTagOptionOutputTypeDef = TypedDict(
    "ListResourcesForTagOptionOutputTypeDef",
    {
        "ResourceDetails": List[ResourceDetailTypeDef],
        "PageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListServiceActionsForProvisioningArtifactOutputTypeDef = TypedDict(
    "ListServiceActionsForProvisioningArtifactOutputTypeDef",
    {
        "ServiceActionSummaries": List[ServiceActionSummaryTypeDef],
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListServiceActionsOutputTypeDef = TypedDict(
    "ListServiceActionsOutputTypeDef",
    {
        "ServiceActionSummaries": List[ServiceActionSummaryTypeDef],
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ServiceActionDetailTypeDef = TypedDict(
    "ServiceActionDetailTypeDef",
    {
        "ServiceActionSummary": NotRequired[ServiceActionSummaryTypeDef],
        "Definition": NotRequired[Dict[ServiceActionDefinitionKeyType, str]],
    },
)
ListStackInstancesForProvisionedProductOutputTypeDef = TypedDict(
    "ListStackInstancesForProvisionedProductOutputTypeDef",
    {
        "StackInstances": List[StackInstanceTypeDef],
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagOptionsInputListTagOptionsPaginateTypeDef = TypedDict(
    "ListTagOptionsInputListTagOptionsPaginateTypeDef",
    {
        "Filters": NotRequired[ListTagOptionsFiltersTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTagOptionsInputRequestTypeDef = TypedDict(
    "ListTagOptionsInputRequestTypeDef",
    {
        "Filters": NotRequired[ListTagOptionsFiltersTypeDef],
        "PageSize": NotRequired[int],
        "PageToken": NotRequired[str],
    },
)
ProvisioningArtifactParameterTypeDef = TypedDict(
    "ProvisioningArtifactParameterTypeDef",
    {
        "ParameterKey": NotRequired[str],
        "DefaultValue": NotRequired[str],
        "ParameterType": NotRequired[str],
        "IsNoEcho": NotRequired[bool],
        "Description": NotRequired[str],
        "ParameterConstraints": NotRequired[ParameterConstraintsTypeDef],
    },
)
SearchProductsOutputTypeDef = TypedDict(
    "SearchProductsOutputTypeDef",
    {
        "ProductViewSummaries": List[ProductViewSummaryTypeDef],
        "ProductViewAggregations": Dict[str, List[ProductViewAggregationValueTypeDef]],
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProvisionProductInputRequestTypeDef = TypedDict(
    "ProvisionProductInputRequestTypeDef",
    {
        "ProvisionedProductName": str,
        "ProvisionToken": str,
        "AcceptLanguage": NotRequired[str],
        "ProductId": NotRequired[str],
        "ProductName": NotRequired[str],
        "ProvisioningArtifactId": NotRequired[str],
        "ProvisioningArtifactName": NotRequired[str],
        "PathId": NotRequired[str],
        "PathName": NotRequired[str],
        "ProvisioningParameters": NotRequired[Sequence[ProvisioningParameterTypeDef]],
        "ProvisioningPreferences": NotRequired[ProvisioningPreferencesTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "NotificationArns": NotRequired[Sequence[str]],
    },
)
RecordDetailTypeDef = TypedDict(
    "RecordDetailTypeDef",
    {
        "RecordId": NotRequired[str],
        "ProvisionedProductName": NotRequired[str],
        "Status": NotRequired[RecordStatusType],
        "CreatedTime": NotRequired[datetime],
        "UpdatedTime": NotRequired[datetime],
        "ProvisionedProductType": NotRequired[str],
        "RecordType": NotRequired[str],
        "ProvisionedProductId": NotRequired[str],
        "ProductId": NotRequired[str],
        "ProvisioningArtifactId": NotRequired[str],
        "PathId": NotRequired[str],
        "RecordErrors": NotRequired[List[RecordErrorTypeDef]],
        "RecordTags": NotRequired[List[RecordTagTypeDef]],
        "LaunchRoleArn": NotRequired[str],
    },
)
ResourceChangeDetailTypeDef = TypedDict(
    "ResourceChangeDetailTypeDef",
    {
        "Target": NotRequired[ResourceTargetDefinitionTypeDef],
        "Evaluation": NotRequired[EvaluationTypeType],
        "CausingEntity": NotRequired[str],
    },
)
ShareDetailsTypeDef = TypedDict(
    "ShareDetailsTypeDef",
    {
        "SuccessfulShares": NotRequired[List[str]],
        "ShareErrors": NotRequired[List[ShareErrorTypeDef]],
    },
)
UpdateProvisionedProductInputRequestTypeDef = TypedDict(
    "UpdateProvisionedProductInputRequestTypeDef",
    {
        "UpdateToken": str,
        "AcceptLanguage": NotRequired[str],
        "ProvisionedProductName": NotRequired[str],
        "ProvisionedProductId": NotRequired[str],
        "ProductId": NotRequired[str],
        "ProductName": NotRequired[str],
        "ProvisioningArtifactId": NotRequired[str],
        "ProvisioningArtifactName": NotRequired[str],
        "PathId": NotRequired[str],
        "PathName": NotRequired[str],
        "ProvisioningParameters": NotRequired[Sequence[UpdateProvisioningParameterTypeDef]],
        "ProvisioningPreferences": NotRequired[UpdateProvisioningPreferencesTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
SourceConnectionDetailTypeDef = TypedDict(
    "SourceConnectionDetailTypeDef",
    {
        "Type": NotRequired[Literal["CODESTAR"]],
        "ConnectionParameters": NotRequired[SourceConnectionParametersTypeDef],
        "LastSync": NotRequired[LastSyncTypeDef],
    },
)
SourceConnectionTypeDef = TypedDict(
    "SourceConnectionTypeDef",
    {
        "ConnectionParameters": SourceConnectionParametersTypeDef,
        "Type": NotRequired[Literal["CODESTAR"]],
    },
)
ListLaunchPathsOutputTypeDef = TypedDict(
    "ListLaunchPathsOutputTypeDef",
    {
        "LaunchPathSummaries": List[LaunchPathSummaryTypeDef],
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchProvisionedProductsOutputTypeDef = TypedDict(
    "SearchProvisionedProductsOutputTypeDef",
    {
        "ProvisionedProducts": List[ProvisionedProductAttributeTypeDef],
        "TotalResultsCount": int,
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListProvisioningArtifactsForServiceActionOutputTypeDef = TypedDict(
    "ListProvisioningArtifactsForServiceActionOutputTypeDef",
    {
        "ProvisioningArtifactViews": List[ProvisioningArtifactViewTypeDef],
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NotifyProvisionProductEngineWorkflowResultInputRequestTypeDef = TypedDict(
    "NotifyProvisionProductEngineWorkflowResultInputRequestTypeDef",
    {
        "WorkflowToken": str,
        "RecordId": str,
        "Status": EngineWorkflowStatusType,
        "IdempotencyToken": str,
        "FailureReason": NotRequired[str],
        "ResourceIdentifier": NotRequired[EngineWorkflowResourceIdentifierTypeDef],
        "Outputs": NotRequired[Sequence[RecordOutputTypeDef]],
    },
)
CreateServiceActionOutputTypeDef = TypedDict(
    "CreateServiceActionOutputTypeDef",
    {
        "ServiceActionDetail": ServiceActionDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeServiceActionOutputTypeDef = TypedDict(
    "DescribeServiceActionOutputTypeDef",
    {
        "ServiceActionDetail": ServiceActionDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateServiceActionOutputTypeDef = TypedDict(
    "UpdateServiceActionOutputTypeDef",
    {
        "ServiceActionDetail": ServiceActionDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeProvisioningArtifactOutputTypeDef = TypedDict(
    "DescribeProvisioningArtifactOutputTypeDef",
    {
        "ProvisioningArtifactDetail": ProvisioningArtifactDetailTypeDef,
        "Info": Dict[str, str],
        "Status": StatusType,
        "ProvisioningArtifactParameters": List[ProvisioningArtifactParameterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeProvisioningParametersOutputTypeDef = TypedDict(
    "DescribeProvisioningParametersOutputTypeDef",
    {
        "ProvisioningArtifactParameters": List[ProvisioningArtifactParameterTypeDef],
        "ConstraintSummaries": List[ConstraintSummaryTypeDef],
        "UsageInstructions": List[UsageInstructionTypeDef],
        "TagOptions": List[TagOptionSummaryTypeDef],
        "ProvisioningArtifactPreferences": ProvisioningArtifactPreferencesTypeDef,
        "ProvisioningArtifactOutputs": List[ProvisioningArtifactOutputTypeDef],
        "ProvisioningArtifactOutputKeys": List[ProvisioningArtifactOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRecordOutputTypeDef = TypedDict(
    "DescribeRecordOutputTypeDef",
    {
        "RecordDetail": RecordDetailTypeDef,
        "RecordOutputs": List[RecordOutputTypeDef],
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExecuteProvisionedProductPlanOutputTypeDef = TypedDict(
    "ExecuteProvisionedProductPlanOutputTypeDef",
    {
        "RecordDetail": RecordDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExecuteProvisionedProductServiceActionOutputTypeDef = TypedDict(
    "ExecuteProvisionedProductServiceActionOutputTypeDef",
    {
        "RecordDetail": RecordDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportAsProvisionedProductOutputTypeDef = TypedDict(
    "ImportAsProvisionedProductOutputTypeDef",
    {
        "RecordDetail": RecordDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRecordHistoryOutputTypeDef = TypedDict(
    "ListRecordHistoryOutputTypeDef",
    {
        "RecordDetails": List[RecordDetailTypeDef],
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProvisionProductOutputTypeDef = TypedDict(
    "ProvisionProductOutputTypeDef",
    {
        "RecordDetail": RecordDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TerminateProvisionedProductOutputTypeDef = TypedDict(
    "TerminateProvisionedProductOutputTypeDef",
    {
        "RecordDetail": RecordDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateProvisionedProductOutputTypeDef = TypedDict(
    "UpdateProvisionedProductOutputTypeDef",
    {
        "RecordDetail": RecordDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResourceChangeTypeDef = TypedDict(
    "ResourceChangeTypeDef",
    {
        "Action": NotRequired[ChangeActionType],
        "LogicalResourceId": NotRequired[str],
        "PhysicalResourceId": NotRequired[str],
        "ResourceType": NotRequired[str],
        "Replacement": NotRequired[ReplacementType],
        "Scope": NotRequired[List[ResourceAttributeType]],
        "Details": NotRequired[List[ResourceChangeDetailTypeDef]],
    },
)
DescribePortfolioShareStatusOutputTypeDef = TypedDict(
    "DescribePortfolioShareStatusOutputTypeDef",
    {
        "PortfolioShareToken": str,
        "PortfolioId": str,
        "OrganizationNodeValue": str,
        "Status": ShareStatusType,
        "ShareDetails": ShareDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProductViewDetailTypeDef = TypedDict(
    "ProductViewDetailTypeDef",
    {
        "ProductViewSummary": NotRequired[ProductViewSummaryTypeDef],
        "Status": NotRequired[StatusType],
        "ProductARN": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "SourceConnection": NotRequired[SourceConnectionDetailTypeDef],
    },
)
CreateProductInputRequestTypeDef = TypedDict(
    "CreateProductInputRequestTypeDef",
    {
        "Name": str,
        "Owner": str,
        "ProductType": ProductTypeType,
        "IdempotencyToken": str,
        "AcceptLanguage": NotRequired[str],
        "Description": NotRequired[str],
        "Distributor": NotRequired[str],
        "SupportDescription": NotRequired[str],
        "SupportEmail": NotRequired[str],
        "SupportUrl": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ProvisioningArtifactParameters": NotRequired[ProvisioningArtifactPropertiesTypeDef],
        "SourceConnection": NotRequired[SourceConnectionTypeDef],
    },
)
UpdateProductInputRequestTypeDef = TypedDict(
    "UpdateProductInputRequestTypeDef",
    {
        "Id": str,
        "AcceptLanguage": NotRequired[str],
        "Name": NotRequired[str],
        "Owner": NotRequired[str],
        "Description": NotRequired[str],
        "Distributor": NotRequired[str],
        "SupportDescription": NotRequired[str],
        "SupportEmail": NotRequired[str],
        "SupportUrl": NotRequired[str],
        "AddTags": NotRequired[Sequence[TagTypeDef]],
        "RemoveTags": NotRequired[Sequence[str]],
        "SourceConnection": NotRequired[SourceConnectionTypeDef],
    },
)
DescribeProvisionedProductPlanOutputTypeDef = TypedDict(
    "DescribeProvisionedProductPlanOutputTypeDef",
    {
        "ProvisionedProductPlanDetails": ProvisionedProductPlanDetailsTypeDef,
        "ResourceChanges": List[ResourceChangeTypeDef],
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProductOutputTypeDef = TypedDict(
    "CreateProductOutputTypeDef",
    {
        "ProductViewDetail": ProductViewDetailTypeDef,
        "ProvisioningArtifactDetail": ProvisioningArtifactDetailTypeDef,
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeProductAsAdminOutputTypeDef = TypedDict(
    "DescribeProductAsAdminOutputTypeDef",
    {
        "ProductViewDetail": ProductViewDetailTypeDef,
        "ProvisioningArtifactSummaries": List[ProvisioningArtifactSummaryTypeDef],
        "Tags": List[TagTypeDef],
        "TagOptions": List[TagOptionDetailTypeDef],
        "Budgets": List[BudgetDetailTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchProductsAsAdminOutputTypeDef = TypedDict(
    "SearchProductsAsAdminOutputTypeDef",
    {
        "ProductViewDetails": List[ProductViewDetailTypeDef],
        "NextPageToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateProductOutputTypeDef = TypedDict(
    "UpdateProductOutputTypeDef",
    {
        "ProductViewDetail": ProductViewDetailTypeDef,
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
