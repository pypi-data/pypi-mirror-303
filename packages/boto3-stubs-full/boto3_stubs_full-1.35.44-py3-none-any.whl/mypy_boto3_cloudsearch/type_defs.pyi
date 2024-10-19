"""
Type annotations for cloudsearch service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/type_defs/)

Usage::

    ```python
    from mypy_boto3_cloudsearch.type_defs import OptionStatusTypeDef

    data: OptionStatusTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import (
    AlgorithmicStemmingType,
    AnalysisSchemeLanguageType,
    IndexFieldTypeType,
    OptionStateType,
    PartitionInstanceTypeType,
    SuggesterFuzzyMatchingType,
    TLSSecurityPolicyType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "OptionStatusTypeDef",
    "AnalysisOptionsTypeDef",
    "BuildSuggestersRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CreateDomainRequestRequestTypeDef",
    "DateArrayOptionsTypeDef",
    "DateOptionsTypeDef",
    "ExpressionTypeDef",
    "DeleteAnalysisSchemeRequestRequestTypeDef",
    "DeleteDomainRequestRequestTypeDef",
    "DeleteExpressionRequestRequestTypeDef",
    "DeleteIndexFieldRequestRequestTypeDef",
    "DeleteSuggesterRequestRequestTypeDef",
    "DescribeAnalysisSchemesRequestRequestTypeDef",
    "DescribeAvailabilityOptionsRequestRequestTypeDef",
    "DescribeDomainEndpointOptionsRequestRequestTypeDef",
    "DescribeDomainsRequestRequestTypeDef",
    "DescribeExpressionsRequestRequestTypeDef",
    "DescribeIndexFieldsRequestRequestTypeDef",
    "DescribeScalingParametersRequestRequestTypeDef",
    "DescribeServiceAccessPoliciesRequestRequestTypeDef",
    "DescribeSuggestersRequestRequestTypeDef",
    "DocumentSuggesterOptionsTypeDef",
    "DomainEndpointOptionsTypeDef",
    "LimitsTypeDef",
    "ServiceEndpointTypeDef",
    "DoubleArrayOptionsTypeDef",
    "DoubleOptionsTypeDef",
    "IndexDocumentsRequestRequestTypeDef",
    "IntArrayOptionsTypeDef",
    "IntOptionsTypeDef",
    "LatLonOptionsTypeDef",
    "LiteralArrayOptionsTypeDef",
    "LiteralOptionsTypeDef",
    "TextArrayOptionsTypeDef",
    "TextOptionsTypeDef",
    "ScalingParametersTypeDef",
    "UpdateAvailabilityOptionsRequestRequestTypeDef",
    "UpdateServiceAccessPoliciesRequestRequestTypeDef",
    "AccessPoliciesStatusTypeDef",
    "AvailabilityOptionsStatusTypeDef",
    "AnalysisSchemeTypeDef",
    "BuildSuggestersResponseTypeDef",
    "IndexDocumentsResponseTypeDef",
    "ListDomainNamesResponseTypeDef",
    "DefineExpressionRequestRequestTypeDef",
    "ExpressionStatusTypeDef",
    "SuggesterTypeDef",
    "DomainEndpointOptionsStatusTypeDef",
    "UpdateDomainEndpointOptionsRequestRequestTypeDef",
    "DomainStatusTypeDef",
    "IndexFieldTypeDef",
    "ScalingParametersStatusTypeDef",
    "UpdateScalingParametersRequestRequestTypeDef",
    "DescribeServiceAccessPoliciesResponseTypeDef",
    "UpdateServiceAccessPoliciesResponseTypeDef",
    "DescribeAvailabilityOptionsResponseTypeDef",
    "UpdateAvailabilityOptionsResponseTypeDef",
    "AnalysisSchemeStatusTypeDef",
    "DefineAnalysisSchemeRequestRequestTypeDef",
    "DefineExpressionResponseTypeDef",
    "DeleteExpressionResponseTypeDef",
    "DescribeExpressionsResponseTypeDef",
    "DefineSuggesterRequestRequestTypeDef",
    "SuggesterStatusTypeDef",
    "DescribeDomainEndpointOptionsResponseTypeDef",
    "UpdateDomainEndpointOptionsResponseTypeDef",
    "CreateDomainResponseTypeDef",
    "DeleteDomainResponseTypeDef",
    "DescribeDomainsResponseTypeDef",
    "DefineIndexFieldRequestRequestTypeDef",
    "IndexFieldStatusTypeDef",
    "DescribeScalingParametersResponseTypeDef",
    "UpdateScalingParametersResponseTypeDef",
    "DefineAnalysisSchemeResponseTypeDef",
    "DeleteAnalysisSchemeResponseTypeDef",
    "DescribeAnalysisSchemesResponseTypeDef",
    "DefineSuggesterResponseTypeDef",
    "DeleteSuggesterResponseTypeDef",
    "DescribeSuggestersResponseTypeDef",
    "DefineIndexFieldResponseTypeDef",
    "DeleteIndexFieldResponseTypeDef",
    "DescribeIndexFieldsResponseTypeDef",
)

OptionStatusTypeDef = TypedDict(
    "OptionStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "State": OptionStateType,
        "UpdateVersion": NotRequired[int],
        "PendingDeletion": NotRequired[bool],
    },
)
AnalysisOptionsTypeDef = TypedDict(
    "AnalysisOptionsTypeDef",
    {
        "Synonyms": NotRequired[str],
        "Stopwords": NotRequired[str],
        "StemmingDictionary": NotRequired[str],
        "JapaneseTokenizationDictionary": NotRequired[str],
        "AlgorithmicStemming": NotRequired[AlgorithmicStemmingType],
    },
)
BuildSuggestersRequestRequestTypeDef = TypedDict(
    "BuildSuggestersRequestRequestTypeDef",
    {
        "DomainName": str,
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
CreateDomainRequestRequestTypeDef = TypedDict(
    "CreateDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
DateArrayOptionsTypeDef = TypedDict(
    "DateArrayOptionsTypeDef",
    {
        "DefaultValue": NotRequired[str],
        "SourceFields": NotRequired[str],
        "FacetEnabled": NotRequired[bool],
        "SearchEnabled": NotRequired[bool],
        "ReturnEnabled": NotRequired[bool],
    },
)
DateOptionsTypeDef = TypedDict(
    "DateOptionsTypeDef",
    {
        "DefaultValue": NotRequired[str],
        "SourceField": NotRequired[str],
        "FacetEnabled": NotRequired[bool],
        "SearchEnabled": NotRequired[bool],
        "ReturnEnabled": NotRequired[bool],
        "SortEnabled": NotRequired[bool],
    },
)
ExpressionTypeDef = TypedDict(
    "ExpressionTypeDef",
    {
        "ExpressionName": str,
        "ExpressionValue": str,
    },
)
DeleteAnalysisSchemeRequestRequestTypeDef = TypedDict(
    "DeleteAnalysisSchemeRequestRequestTypeDef",
    {
        "DomainName": str,
        "AnalysisSchemeName": str,
    },
)
DeleteDomainRequestRequestTypeDef = TypedDict(
    "DeleteDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
DeleteExpressionRequestRequestTypeDef = TypedDict(
    "DeleteExpressionRequestRequestTypeDef",
    {
        "DomainName": str,
        "ExpressionName": str,
    },
)
DeleteIndexFieldRequestRequestTypeDef = TypedDict(
    "DeleteIndexFieldRequestRequestTypeDef",
    {
        "DomainName": str,
        "IndexFieldName": str,
    },
)
DeleteSuggesterRequestRequestTypeDef = TypedDict(
    "DeleteSuggesterRequestRequestTypeDef",
    {
        "DomainName": str,
        "SuggesterName": str,
    },
)
DescribeAnalysisSchemesRequestRequestTypeDef = TypedDict(
    "DescribeAnalysisSchemesRequestRequestTypeDef",
    {
        "DomainName": str,
        "AnalysisSchemeNames": NotRequired[Sequence[str]],
        "Deployed": NotRequired[bool],
    },
)
DescribeAvailabilityOptionsRequestRequestTypeDef = TypedDict(
    "DescribeAvailabilityOptionsRequestRequestTypeDef",
    {
        "DomainName": str,
        "Deployed": NotRequired[bool],
    },
)
DescribeDomainEndpointOptionsRequestRequestTypeDef = TypedDict(
    "DescribeDomainEndpointOptionsRequestRequestTypeDef",
    {
        "DomainName": str,
        "Deployed": NotRequired[bool],
    },
)
DescribeDomainsRequestRequestTypeDef = TypedDict(
    "DescribeDomainsRequestRequestTypeDef",
    {
        "DomainNames": NotRequired[Sequence[str]],
    },
)
DescribeExpressionsRequestRequestTypeDef = TypedDict(
    "DescribeExpressionsRequestRequestTypeDef",
    {
        "DomainName": str,
        "ExpressionNames": NotRequired[Sequence[str]],
        "Deployed": NotRequired[bool],
    },
)
DescribeIndexFieldsRequestRequestTypeDef = TypedDict(
    "DescribeIndexFieldsRequestRequestTypeDef",
    {
        "DomainName": str,
        "FieldNames": NotRequired[Sequence[str]],
        "Deployed": NotRequired[bool],
    },
)
DescribeScalingParametersRequestRequestTypeDef = TypedDict(
    "DescribeScalingParametersRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
DescribeServiceAccessPoliciesRequestRequestTypeDef = TypedDict(
    "DescribeServiceAccessPoliciesRequestRequestTypeDef",
    {
        "DomainName": str,
        "Deployed": NotRequired[bool],
    },
)
DescribeSuggestersRequestRequestTypeDef = TypedDict(
    "DescribeSuggestersRequestRequestTypeDef",
    {
        "DomainName": str,
        "SuggesterNames": NotRequired[Sequence[str]],
        "Deployed": NotRequired[bool],
    },
)
DocumentSuggesterOptionsTypeDef = TypedDict(
    "DocumentSuggesterOptionsTypeDef",
    {
        "SourceField": str,
        "FuzzyMatching": NotRequired[SuggesterFuzzyMatchingType],
        "SortExpression": NotRequired[str],
    },
)
DomainEndpointOptionsTypeDef = TypedDict(
    "DomainEndpointOptionsTypeDef",
    {
        "EnforceHTTPS": NotRequired[bool],
        "TLSSecurityPolicy": NotRequired[TLSSecurityPolicyType],
    },
)
LimitsTypeDef = TypedDict(
    "LimitsTypeDef",
    {
        "MaximumReplicationCount": int,
        "MaximumPartitionCount": int,
    },
)
ServiceEndpointTypeDef = TypedDict(
    "ServiceEndpointTypeDef",
    {
        "Endpoint": NotRequired[str],
    },
)
DoubleArrayOptionsTypeDef = TypedDict(
    "DoubleArrayOptionsTypeDef",
    {
        "DefaultValue": NotRequired[float],
        "SourceFields": NotRequired[str],
        "FacetEnabled": NotRequired[bool],
        "SearchEnabled": NotRequired[bool],
        "ReturnEnabled": NotRequired[bool],
    },
)
DoubleOptionsTypeDef = TypedDict(
    "DoubleOptionsTypeDef",
    {
        "DefaultValue": NotRequired[float],
        "SourceField": NotRequired[str],
        "FacetEnabled": NotRequired[bool],
        "SearchEnabled": NotRequired[bool],
        "ReturnEnabled": NotRequired[bool],
        "SortEnabled": NotRequired[bool],
    },
)
IndexDocumentsRequestRequestTypeDef = TypedDict(
    "IndexDocumentsRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
IntArrayOptionsTypeDef = TypedDict(
    "IntArrayOptionsTypeDef",
    {
        "DefaultValue": NotRequired[int],
        "SourceFields": NotRequired[str],
        "FacetEnabled": NotRequired[bool],
        "SearchEnabled": NotRequired[bool],
        "ReturnEnabled": NotRequired[bool],
    },
)
IntOptionsTypeDef = TypedDict(
    "IntOptionsTypeDef",
    {
        "DefaultValue": NotRequired[int],
        "SourceField": NotRequired[str],
        "FacetEnabled": NotRequired[bool],
        "SearchEnabled": NotRequired[bool],
        "ReturnEnabled": NotRequired[bool],
        "SortEnabled": NotRequired[bool],
    },
)
LatLonOptionsTypeDef = TypedDict(
    "LatLonOptionsTypeDef",
    {
        "DefaultValue": NotRequired[str],
        "SourceField": NotRequired[str],
        "FacetEnabled": NotRequired[bool],
        "SearchEnabled": NotRequired[bool],
        "ReturnEnabled": NotRequired[bool],
        "SortEnabled": NotRequired[bool],
    },
)
LiteralArrayOptionsTypeDef = TypedDict(
    "LiteralArrayOptionsTypeDef",
    {
        "DefaultValue": NotRequired[str],
        "SourceFields": NotRequired[str],
        "FacetEnabled": NotRequired[bool],
        "SearchEnabled": NotRequired[bool],
        "ReturnEnabled": NotRequired[bool],
    },
)
LiteralOptionsTypeDef = TypedDict(
    "LiteralOptionsTypeDef",
    {
        "DefaultValue": NotRequired[str],
        "SourceField": NotRequired[str],
        "FacetEnabled": NotRequired[bool],
        "SearchEnabled": NotRequired[bool],
        "ReturnEnabled": NotRequired[bool],
        "SortEnabled": NotRequired[bool],
    },
)
TextArrayOptionsTypeDef = TypedDict(
    "TextArrayOptionsTypeDef",
    {
        "DefaultValue": NotRequired[str],
        "SourceFields": NotRequired[str],
        "ReturnEnabled": NotRequired[bool],
        "HighlightEnabled": NotRequired[bool],
        "AnalysisScheme": NotRequired[str],
    },
)
TextOptionsTypeDef = TypedDict(
    "TextOptionsTypeDef",
    {
        "DefaultValue": NotRequired[str],
        "SourceField": NotRequired[str],
        "ReturnEnabled": NotRequired[bool],
        "SortEnabled": NotRequired[bool],
        "HighlightEnabled": NotRequired[bool],
        "AnalysisScheme": NotRequired[str],
    },
)
ScalingParametersTypeDef = TypedDict(
    "ScalingParametersTypeDef",
    {
        "DesiredInstanceType": NotRequired[PartitionInstanceTypeType],
        "DesiredReplicationCount": NotRequired[int],
        "DesiredPartitionCount": NotRequired[int],
    },
)
UpdateAvailabilityOptionsRequestRequestTypeDef = TypedDict(
    "UpdateAvailabilityOptionsRequestRequestTypeDef",
    {
        "DomainName": str,
        "MultiAZ": bool,
    },
)
UpdateServiceAccessPoliciesRequestRequestTypeDef = TypedDict(
    "UpdateServiceAccessPoliciesRequestRequestTypeDef",
    {
        "DomainName": str,
        "AccessPolicies": str,
    },
)
AccessPoliciesStatusTypeDef = TypedDict(
    "AccessPoliciesStatusTypeDef",
    {
        "Options": str,
        "Status": OptionStatusTypeDef,
    },
)
AvailabilityOptionsStatusTypeDef = TypedDict(
    "AvailabilityOptionsStatusTypeDef",
    {
        "Options": bool,
        "Status": OptionStatusTypeDef,
    },
)
AnalysisSchemeTypeDef = TypedDict(
    "AnalysisSchemeTypeDef",
    {
        "AnalysisSchemeName": str,
        "AnalysisSchemeLanguage": AnalysisSchemeLanguageType,
        "AnalysisOptions": NotRequired[AnalysisOptionsTypeDef],
    },
)
BuildSuggestersResponseTypeDef = TypedDict(
    "BuildSuggestersResponseTypeDef",
    {
        "FieldNames": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IndexDocumentsResponseTypeDef = TypedDict(
    "IndexDocumentsResponseTypeDef",
    {
        "FieldNames": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDomainNamesResponseTypeDef = TypedDict(
    "ListDomainNamesResponseTypeDef",
    {
        "DomainNames": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DefineExpressionRequestRequestTypeDef = TypedDict(
    "DefineExpressionRequestRequestTypeDef",
    {
        "DomainName": str,
        "Expression": ExpressionTypeDef,
    },
)
ExpressionStatusTypeDef = TypedDict(
    "ExpressionStatusTypeDef",
    {
        "Options": ExpressionTypeDef,
        "Status": OptionStatusTypeDef,
    },
)
SuggesterTypeDef = TypedDict(
    "SuggesterTypeDef",
    {
        "SuggesterName": str,
        "DocumentSuggesterOptions": DocumentSuggesterOptionsTypeDef,
    },
)
DomainEndpointOptionsStatusTypeDef = TypedDict(
    "DomainEndpointOptionsStatusTypeDef",
    {
        "Options": DomainEndpointOptionsTypeDef,
        "Status": OptionStatusTypeDef,
    },
)
UpdateDomainEndpointOptionsRequestRequestTypeDef = TypedDict(
    "UpdateDomainEndpointOptionsRequestRequestTypeDef",
    {
        "DomainName": str,
        "DomainEndpointOptions": DomainEndpointOptionsTypeDef,
    },
)
DomainStatusTypeDef = TypedDict(
    "DomainStatusTypeDef",
    {
        "DomainId": str,
        "DomainName": str,
        "RequiresIndexDocuments": bool,
        "ARN": NotRequired[str],
        "Created": NotRequired[bool],
        "Deleted": NotRequired[bool],
        "DocService": NotRequired[ServiceEndpointTypeDef],
        "SearchService": NotRequired[ServiceEndpointTypeDef],
        "Processing": NotRequired[bool],
        "SearchInstanceType": NotRequired[str],
        "SearchPartitionCount": NotRequired[int],
        "SearchInstanceCount": NotRequired[int],
        "Limits": NotRequired[LimitsTypeDef],
    },
)
IndexFieldTypeDef = TypedDict(
    "IndexFieldTypeDef",
    {
        "IndexFieldName": str,
        "IndexFieldType": IndexFieldTypeType,
        "IntOptions": NotRequired[IntOptionsTypeDef],
        "DoubleOptions": NotRequired[DoubleOptionsTypeDef],
        "LiteralOptions": NotRequired[LiteralOptionsTypeDef],
        "TextOptions": NotRequired[TextOptionsTypeDef],
        "DateOptions": NotRequired[DateOptionsTypeDef],
        "LatLonOptions": NotRequired[LatLonOptionsTypeDef],
        "IntArrayOptions": NotRequired[IntArrayOptionsTypeDef],
        "DoubleArrayOptions": NotRequired[DoubleArrayOptionsTypeDef],
        "LiteralArrayOptions": NotRequired[LiteralArrayOptionsTypeDef],
        "TextArrayOptions": NotRequired[TextArrayOptionsTypeDef],
        "DateArrayOptions": NotRequired[DateArrayOptionsTypeDef],
    },
)
ScalingParametersStatusTypeDef = TypedDict(
    "ScalingParametersStatusTypeDef",
    {
        "Options": ScalingParametersTypeDef,
        "Status": OptionStatusTypeDef,
    },
)
UpdateScalingParametersRequestRequestTypeDef = TypedDict(
    "UpdateScalingParametersRequestRequestTypeDef",
    {
        "DomainName": str,
        "ScalingParameters": ScalingParametersTypeDef,
    },
)
DescribeServiceAccessPoliciesResponseTypeDef = TypedDict(
    "DescribeServiceAccessPoliciesResponseTypeDef",
    {
        "AccessPolicies": AccessPoliciesStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateServiceAccessPoliciesResponseTypeDef = TypedDict(
    "UpdateServiceAccessPoliciesResponseTypeDef",
    {
        "AccessPolicies": AccessPoliciesStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAvailabilityOptionsResponseTypeDef = TypedDict(
    "DescribeAvailabilityOptionsResponseTypeDef",
    {
        "AvailabilityOptions": AvailabilityOptionsStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAvailabilityOptionsResponseTypeDef = TypedDict(
    "UpdateAvailabilityOptionsResponseTypeDef",
    {
        "AvailabilityOptions": AvailabilityOptionsStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AnalysisSchemeStatusTypeDef = TypedDict(
    "AnalysisSchemeStatusTypeDef",
    {
        "Options": AnalysisSchemeTypeDef,
        "Status": OptionStatusTypeDef,
    },
)
DefineAnalysisSchemeRequestRequestTypeDef = TypedDict(
    "DefineAnalysisSchemeRequestRequestTypeDef",
    {
        "DomainName": str,
        "AnalysisScheme": AnalysisSchemeTypeDef,
    },
)
DefineExpressionResponseTypeDef = TypedDict(
    "DefineExpressionResponseTypeDef",
    {
        "Expression": ExpressionStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteExpressionResponseTypeDef = TypedDict(
    "DeleteExpressionResponseTypeDef",
    {
        "Expression": ExpressionStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeExpressionsResponseTypeDef = TypedDict(
    "DescribeExpressionsResponseTypeDef",
    {
        "Expressions": List[ExpressionStatusTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DefineSuggesterRequestRequestTypeDef = TypedDict(
    "DefineSuggesterRequestRequestTypeDef",
    {
        "DomainName": str,
        "Suggester": SuggesterTypeDef,
    },
)
SuggesterStatusTypeDef = TypedDict(
    "SuggesterStatusTypeDef",
    {
        "Options": SuggesterTypeDef,
        "Status": OptionStatusTypeDef,
    },
)
DescribeDomainEndpointOptionsResponseTypeDef = TypedDict(
    "DescribeDomainEndpointOptionsResponseTypeDef",
    {
        "DomainEndpointOptions": DomainEndpointOptionsStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDomainEndpointOptionsResponseTypeDef = TypedDict(
    "UpdateDomainEndpointOptionsResponseTypeDef",
    {
        "DomainEndpointOptions": DomainEndpointOptionsStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDomainResponseTypeDef = TypedDict(
    "CreateDomainResponseTypeDef",
    {
        "DomainStatus": DomainStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDomainResponseTypeDef = TypedDict(
    "DeleteDomainResponseTypeDef",
    {
        "DomainStatus": DomainStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDomainsResponseTypeDef = TypedDict(
    "DescribeDomainsResponseTypeDef",
    {
        "DomainStatusList": List[DomainStatusTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DefineIndexFieldRequestRequestTypeDef = TypedDict(
    "DefineIndexFieldRequestRequestTypeDef",
    {
        "DomainName": str,
        "IndexField": IndexFieldTypeDef,
    },
)
IndexFieldStatusTypeDef = TypedDict(
    "IndexFieldStatusTypeDef",
    {
        "Options": IndexFieldTypeDef,
        "Status": OptionStatusTypeDef,
    },
)
DescribeScalingParametersResponseTypeDef = TypedDict(
    "DescribeScalingParametersResponseTypeDef",
    {
        "ScalingParameters": ScalingParametersStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateScalingParametersResponseTypeDef = TypedDict(
    "UpdateScalingParametersResponseTypeDef",
    {
        "ScalingParameters": ScalingParametersStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DefineAnalysisSchemeResponseTypeDef = TypedDict(
    "DefineAnalysisSchemeResponseTypeDef",
    {
        "AnalysisScheme": AnalysisSchemeStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteAnalysisSchemeResponseTypeDef = TypedDict(
    "DeleteAnalysisSchemeResponseTypeDef",
    {
        "AnalysisScheme": AnalysisSchemeStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAnalysisSchemesResponseTypeDef = TypedDict(
    "DescribeAnalysisSchemesResponseTypeDef",
    {
        "AnalysisSchemes": List[AnalysisSchemeStatusTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DefineSuggesterResponseTypeDef = TypedDict(
    "DefineSuggesterResponseTypeDef",
    {
        "Suggester": SuggesterStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteSuggesterResponseTypeDef = TypedDict(
    "DeleteSuggesterResponseTypeDef",
    {
        "Suggester": SuggesterStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSuggestersResponseTypeDef = TypedDict(
    "DescribeSuggestersResponseTypeDef",
    {
        "Suggesters": List[SuggesterStatusTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DefineIndexFieldResponseTypeDef = TypedDict(
    "DefineIndexFieldResponseTypeDef",
    {
        "IndexField": IndexFieldStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteIndexFieldResponseTypeDef = TypedDict(
    "DeleteIndexFieldResponseTypeDef",
    {
        "IndexField": IndexFieldStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeIndexFieldsResponseTypeDef = TypedDict(
    "DescribeIndexFieldsResponseTypeDef",
    {
        "IndexFields": List[IndexFieldStatusTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
