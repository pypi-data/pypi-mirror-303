"""
Type annotations for amplifyuibuilder service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplifyuibuilder/type_defs/)

Usage::

    ```python
    from mypy_boto3_amplifyuibuilder.type_defs import GraphQLRenderConfigTypeDef

    data: GraphQLRenderConfigTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    CodegenGenericDataFieldDataTypeType,
    CodegenJobStatusType,
    FormActionTypeType,
    FormButtonsPositionType,
    FormDataSourceTypeType,
    GenericDataRelationshipTypeType,
    JSModuleType,
    JSScriptType,
    JSTargetType,
    LabelDecoratorType,
    SortDirectionType,
    StorageAccessLevelType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "GraphQLRenderConfigTypeDef",
    "CodegenDependencyTypeDef",
    "CodegenFeatureFlagsTypeDef",
    "CodegenGenericDataEnumOutputTypeDef",
    "CodegenGenericDataEnumTypeDef",
    "CodegenGenericDataRelationshipTypeOutputTypeDef",
    "CodegenGenericDataRelationshipTypeTypeDef",
    "CodegenJobAssetTypeDef",
    "CodegenJobSummaryTypeDef",
    "PredicateOutputTypeDef",
    "PredicatePaginatorTypeDef",
    "ComponentConditionPropertyOutputTypeDef",
    "ComponentConditionPropertyPaginatorTypeDef",
    "ComponentConditionPropertyTypeDef",
    "SortPropertyTypeDef",
    "ComponentVariantOutputTypeDef",
    "ComponentPropertyBindingPropertiesTypeDef",
    "FormBindingElementTypeDef",
    "ComponentSummaryTypeDef",
    "ComponentVariantTypeDef",
    "ResponseMetadataTypeDef",
    "FormDataTypeConfigTypeDef",
    "DeleteComponentRequestRequestTypeDef",
    "DeleteFormRequestRequestTypeDef",
    "DeleteThemeRequestRequestTypeDef",
    "ExchangeCodeForTokenRequestBodyTypeDef",
    "PaginatorConfigTypeDef",
    "ExportComponentsRequestRequestTypeDef",
    "ExportFormsRequestRequestTypeDef",
    "ExportThemesRequestRequestTypeDef",
    "FieldPositionTypeDef",
    "FieldValidationConfigurationOutputTypeDef",
    "FileUploaderFieldConfigOutputTypeDef",
    "FieldValidationConfigurationTypeDef",
    "FileUploaderFieldConfigTypeDef",
    "FormInputBindingPropertiesValuePropertiesTypeDef",
    "FormInputValuePropertyBindingPropertiesTypeDef",
    "FormStyleConfigTypeDef",
    "GetCodegenJobRequestRequestTypeDef",
    "GetComponentRequestRequestTypeDef",
    "GetFormRequestRequestTypeDef",
    "GetMetadataRequestRequestTypeDef",
    "GetThemeRequestRequestTypeDef",
    "ListCodegenJobsRequestRequestTypeDef",
    "ListComponentsRequestRequestTypeDef",
    "ListFormsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListThemesRequestRequestTypeDef",
    "ThemeSummaryTypeDef",
    "PredicateTypeDef",
    "PutMetadataFlagBodyTypeDef",
    "RefreshTokenRequestBodyTypeDef",
    "TagResourceRequestRequestTypeDef",
    "ThemeValueOutputTypeDef",
    "ThemeValuePaginatorTypeDef",
    "ThemeValueTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "ApiConfigurationOutputTypeDef",
    "ApiConfigurationTypeDef",
    "CodegenGenericDataEnumUnionTypeDef",
    "CodegenGenericDataFieldOutputTypeDef",
    "CodegenGenericDataRelationshipTypeUnionTypeDef",
    "ComponentBindingPropertiesValuePropertiesOutputTypeDef",
    "ComponentBindingPropertiesValuePropertiesPaginatorTypeDef",
    "ComponentConditionPropertyUnionTypeDef",
    "ComponentDataConfigurationOutputTypeDef",
    "ComponentDataConfigurationPaginatorTypeDef",
    "ComponentPropertyOutputTypeDef",
    "ComponentPropertyPaginatorTypeDef",
    "ComponentVariantUnionTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ExchangeCodeForTokenResponseTypeDef",
    "GetMetadataResponseTypeDef",
    "ListCodegenJobsResponseTypeDef",
    "ListComponentsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "RefreshTokenResponseTypeDef",
    "FormSummaryTypeDef",
    "ExchangeCodeForTokenRequestRequestTypeDef",
    "ExportComponentsRequestExportComponentsPaginateTypeDef",
    "ExportFormsRequestExportFormsPaginateTypeDef",
    "ExportThemesRequestExportThemesPaginateTypeDef",
    "ListCodegenJobsRequestListCodegenJobsPaginateTypeDef",
    "ListComponentsRequestListComponentsPaginateTypeDef",
    "ListFormsRequestListFormsPaginateTypeDef",
    "ListThemesRequestListThemesPaginateTypeDef",
    "FormButtonTypeDef",
    "SectionalElementTypeDef",
    "FieldValidationConfigurationUnionTypeDef",
    "FileUploaderFieldConfigUnionTypeDef",
    "FormInputBindingPropertiesValueTypeDef",
    "FormInputValuePropertyOutputTypeDef",
    "FormInputValuePropertyPaginatorTypeDef",
    "FormInputValuePropertyTypeDef",
    "FormStyleTypeDef",
    "ListThemesResponseTypeDef",
    "PredicateUnionTypeDef",
    "PutMetadataFlagRequestRequestTypeDef",
    "RefreshTokenRequestRequestTypeDef",
    "ThemeValuesOutputTypeDef",
    "ThemeValuesPaginatorTypeDef",
    "ThemeValueUnionTypeDef",
    "ReactStartCodegenJobDataOutputTypeDef",
    "ApiConfigurationUnionTypeDef",
    "CodegenGenericDataModelOutputTypeDef",
    "CodegenGenericDataNonModelOutputTypeDef",
    "CodegenGenericDataFieldTypeDef",
    "ComponentBindingPropertiesValueOutputTypeDef",
    "ComponentBindingPropertiesValuePaginatorTypeDef",
    "ComponentPropertyTypeDef",
    "MutationActionSetStateParameterOutputTypeDef",
    "MutationActionSetStateParameterPaginatorTypeDef",
    "ListFormsResponseTypeDef",
    "FormCTATypeDef",
    "ValueMappingOutputTypeDef",
    "ValueMappingPaginatorTypeDef",
    "FormInputValuePropertyUnionTypeDef",
    "ComponentBindingPropertiesValuePropertiesTypeDef",
    "ComponentDataConfigurationTypeDef",
    "ThemeTypeDef",
    "ThemePaginatorTypeDef",
    "ThemeValuesTypeDef",
    "CodegenJobRenderConfigOutputTypeDef",
    "ReactStartCodegenJobDataTypeDef",
    "CodegenJobGenericDataSchemaOutputTypeDef",
    "CodegenGenericDataFieldUnionTypeDef",
    "CodegenGenericDataNonModelTypeDef",
    "ComponentPropertyUnionTypeDef",
    "ActionParametersOutputTypeDef",
    "ActionParametersPaginatorTypeDef",
    "ValueMappingsOutputTypeDef",
    "ValueMappingsPaginatorTypeDef",
    "ValueMappingTypeDef",
    "ComponentBindingPropertiesValuePropertiesUnionTypeDef",
    "ComponentDataConfigurationUnionTypeDef",
    "CreateThemeResponseTypeDef",
    "ExportThemesResponseTypeDef",
    "GetThemeResponseTypeDef",
    "UpdateThemeResponseTypeDef",
    "ExportThemesResponsePaginatorTypeDef",
    "ThemeValuesUnionTypeDef",
    "ReactStartCodegenJobDataUnionTypeDef",
    "CodegenJobTypeDef",
    "CodegenGenericDataModelTypeDef",
    "CodegenGenericDataNonModelUnionTypeDef",
    "MutationActionSetStateParameterTypeDef",
    "ComponentEventOutputTypeDef",
    "ComponentEventPaginatorTypeDef",
    "FieldInputConfigOutputTypeDef",
    "FieldInputConfigPaginatorTypeDef",
    "ValueMappingUnionTypeDef",
    "ComponentBindingPropertiesValueTypeDef",
    "CreateThemeDataTypeDef",
    "UpdateThemeDataTypeDef",
    "CodegenJobRenderConfigTypeDef",
    "GetCodegenJobResponseTypeDef",
    "StartCodegenJobResponseTypeDef",
    "CodegenGenericDataModelUnionTypeDef",
    "MutationActionSetStateParameterUnionTypeDef",
    "ComponentChildOutputTypeDef",
    "ComponentChildPaginatorTypeDef",
    "FieldConfigOutputTypeDef",
    "FieldConfigPaginatorTypeDef",
    "ValueMappingsTypeDef",
    "ComponentBindingPropertiesValueUnionTypeDef",
    "CreateThemeRequestRequestTypeDef",
    "UpdateThemeRequestRequestTypeDef",
    "CodegenJobRenderConfigUnionTypeDef",
    "CodegenJobGenericDataSchemaTypeDef",
    "ActionParametersTypeDef",
    "ComponentTypeDef",
    "ComponentPaginatorTypeDef",
    "FormTypeDef",
    "FormPaginatorTypeDef",
    "ValueMappingsUnionTypeDef",
    "CodegenJobGenericDataSchemaUnionTypeDef",
    "ActionParametersUnionTypeDef",
    "CreateComponentResponseTypeDef",
    "ExportComponentsResponseTypeDef",
    "GetComponentResponseTypeDef",
    "UpdateComponentResponseTypeDef",
    "ExportComponentsResponsePaginatorTypeDef",
    "CreateFormResponseTypeDef",
    "ExportFormsResponseTypeDef",
    "GetFormResponseTypeDef",
    "UpdateFormResponseTypeDef",
    "ExportFormsResponsePaginatorTypeDef",
    "FieldInputConfigTypeDef",
    "StartCodegenJobDataTypeDef",
    "ComponentEventTypeDef",
    "FieldInputConfigUnionTypeDef",
    "StartCodegenJobRequestRequestTypeDef",
    "ComponentEventUnionTypeDef",
    "FieldConfigTypeDef",
    "ComponentChildTypeDef",
    "FieldConfigUnionTypeDef",
    "ComponentChildUnionTypeDef",
    "CreateFormDataTypeDef",
    "UpdateFormDataTypeDef",
    "CreateComponentDataTypeDef",
    "UpdateComponentDataTypeDef",
    "CreateFormRequestRequestTypeDef",
    "UpdateFormRequestRequestTypeDef",
    "CreateComponentRequestRequestTypeDef",
    "UpdateComponentRequestRequestTypeDef",
)

GraphQLRenderConfigTypeDef = TypedDict(
    "GraphQLRenderConfigTypeDef",
    {
        "typesFilePath": str,
        "queriesFilePath": str,
        "mutationsFilePath": str,
        "subscriptionsFilePath": str,
        "fragmentsFilePath": str,
    },
)
CodegenDependencyTypeDef = TypedDict(
    "CodegenDependencyTypeDef",
    {
        "name": NotRequired[str],
        "supportedVersion": NotRequired[str],
        "isSemVer": NotRequired[bool],
        "reason": NotRequired[str],
    },
)
CodegenFeatureFlagsTypeDef = TypedDict(
    "CodegenFeatureFlagsTypeDef",
    {
        "isRelationshipSupported": NotRequired[bool],
        "isNonModelSupported": NotRequired[bool],
    },
)
CodegenGenericDataEnumOutputTypeDef = TypedDict(
    "CodegenGenericDataEnumOutputTypeDef",
    {
        "values": List[str],
    },
)
CodegenGenericDataEnumTypeDef = TypedDict(
    "CodegenGenericDataEnumTypeDef",
    {
        "values": Sequence[str],
    },
)
CodegenGenericDataRelationshipTypeOutputTypeDef = TypedDict(
    "CodegenGenericDataRelationshipTypeOutputTypeDef",
    {
        "type": GenericDataRelationshipTypeType,
        "relatedModelName": str,
        "relatedModelFields": NotRequired[List[str]],
        "canUnlinkAssociatedModel": NotRequired[bool],
        "relatedJoinFieldName": NotRequired[str],
        "relatedJoinTableName": NotRequired[str],
        "belongsToFieldOnRelatedModel": NotRequired[str],
        "associatedFields": NotRequired[List[str]],
        "isHasManyIndex": NotRequired[bool],
    },
)
CodegenGenericDataRelationshipTypeTypeDef = TypedDict(
    "CodegenGenericDataRelationshipTypeTypeDef",
    {
        "type": GenericDataRelationshipTypeType,
        "relatedModelName": str,
        "relatedModelFields": NotRequired[Sequence[str]],
        "canUnlinkAssociatedModel": NotRequired[bool],
        "relatedJoinFieldName": NotRequired[str],
        "relatedJoinTableName": NotRequired[str],
        "belongsToFieldOnRelatedModel": NotRequired[str],
        "associatedFields": NotRequired[Sequence[str]],
        "isHasManyIndex": NotRequired[bool],
    },
)
CodegenJobAssetTypeDef = TypedDict(
    "CodegenJobAssetTypeDef",
    {
        "downloadUrl": NotRequired[str],
    },
)
CodegenJobSummaryTypeDef = TypedDict(
    "CodegenJobSummaryTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "createdAt": NotRequired[datetime],
        "modifiedAt": NotRequired[datetime],
    },
)
PredicateOutputTypeDef = TypedDict(
    "PredicateOutputTypeDef",
    {
        "or": NotRequired[List[Dict[str, Any]]],
        "and": NotRequired[List[Dict[str, Any]]],
        "field": NotRequired[str],
        "operator": NotRequired[str],
        "operand": NotRequired[str],
        "operandType": NotRequired[str],
    },
)
PredicatePaginatorTypeDef = TypedDict(
    "PredicatePaginatorTypeDef",
    {
        "or": NotRequired[List[Dict[str, Any]]],
        "and": NotRequired[List[Dict[str, Any]]],
        "field": NotRequired[str],
        "operator": NotRequired[str],
        "operand": NotRequired[str],
        "operandType": NotRequired[str],
    },
)
ComponentConditionPropertyOutputTypeDef = TypedDict(
    "ComponentConditionPropertyOutputTypeDef",
    {
        "property": NotRequired[str],
        "field": NotRequired[str],
        "operator": NotRequired[str],
        "operand": NotRequired[str],
        "then": NotRequired[Dict[str, Any]],
        "else": NotRequired[Dict[str, Any]],
        "operandType": NotRequired[str],
    },
)
ComponentConditionPropertyPaginatorTypeDef = TypedDict(
    "ComponentConditionPropertyPaginatorTypeDef",
    {
        "property": NotRequired[str],
        "field": NotRequired[str],
        "operator": NotRequired[str],
        "operand": NotRequired[str],
        "then": NotRequired[Dict[str, Any]],
        "else": NotRequired[Dict[str, Any]],
        "operandType": NotRequired[str],
    },
)
ComponentConditionPropertyTypeDef = TypedDict(
    "ComponentConditionPropertyTypeDef",
    {
        "property": NotRequired[str],
        "field": NotRequired[str],
        "operator": NotRequired[str],
        "operand": NotRequired[str],
        "then": NotRequired[Mapping[str, Any]],
        "else": NotRequired[Mapping[str, Any]],
        "operandType": NotRequired[str],
    },
)
SortPropertyTypeDef = TypedDict(
    "SortPropertyTypeDef",
    {
        "field": str,
        "direction": SortDirectionType,
    },
)
ComponentVariantOutputTypeDef = TypedDict(
    "ComponentVariantOutputTypeDef",
    {
        "variantValues": NotRequired[Dict[str, str]],
        "overrides": NotRequired[Dict[str, Dict[str, str]]],
    },
)
ComponentPropertyBindingPropertiesTypeDef = TypedDict(
    "ComponentPropertyBindingPropertiesTypeDef",
    {
        "property": str,
        "field": NotRequired[str],
    },
)
FormBindingElementTypeDef = TypedDict(
    "FormBindingElementTypeDef",
    {
        "element": str,
        "property": str,
    },
)
ComponentSummaryTypeDef = TypedDict(
    "ComponentSummaryTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "name": str,
        "componentType": str,
    },
)
ComponentVariantTypeDef = TypedDict(
    "ComponentVariantTypeDef",
    {
        "variantValues": NotRequired[Mapping[str, str]],
        "overrides": NotRequired[Mapping[str, Mapping[str, str]]],
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
FormDataTypeConfigTypeDef = TypedDict(
    "FormDataTypeConfigTypeDef",
    {
        "dataSourceType": FormDataSourceTypeType,
        "dataTypeName": str,
    },
)
DeleteComponentRequestRequestTypeDef = TypedDict(
    "DeleteComponentRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)
DeleteFormRequestRequestTypeDef = TypedDict(
    "DeleteFormRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)
DeleteThemeRequestRequestTypeDef = TypedDict(
    "DeleteThemeRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)
ExchangeCodeForTokenRequestBodyTypeDef = TypedDict(
    "ExchangeCodeForTokenRequestBodyTypeDef",
    {
        "code": str,
        "redirectUri": str,
        "clientId": NotRequired[str],
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
ExportComponentsRequestRequestTypeDef = TypedDict(
    "ExportComponentsRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "nextToken": NotRequired[str],
    },
)
ExportFormsRequestRequestTypeDef = TypedDict(
    "ExportFormsRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "nextToken": NotRequired[str],
    },
)
ExportThemesRequestRequestTypeDef = TypedDict(
    "ExportThemesRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "nextToken": NotRequired[str],
    },
)
FieldPositionTypeDef = TypedDict(
    "FieldPositionTypeDef",
    {
        "fixed": NotRequired[Literal["first"]],
        "rightOf": NotRequired[str],
        "below": NotRequired[str],
    },
)
FieldValidationConfigurationOutputTypeDef = TypedDict(
    "FieldValidationConfigurationOutputTypeDef",
    {
        "type": str,
        "strValues": NotRequired[List[str]],
        "numValues": NotRequired[List[int]],
        "validationMessage": NotRequired[str],
    },
)
FileUploaderFieldConfigOutputTypeDef = TypedDict(
    "FileUploaderFieldConfigOutputTypeDef",
    {
        "accessLevel": StorageAccessLevelType,
        "acceptedFileTypes": List[str],
        "showThumbnails": NotRequired[bool],
        "isResumable": NotRequired[bool],
        "maxFileCount": NotRequired[int],
        "maxSize": NotRequired[int],
    },
)
FieldValidationConfigurationTypeDef = TypedDict(
    "FieldValidationConfigurationTypeDef",
    {
        "type": str,
        "strValues": NotRequired[Sequence[str]],
        "numValues": NotRequired[Sequence[int]],
        "validationMessage": NotRequired[str],
    },
)
FileUploaderFieldConfigTypeDef = TypedDict(
    "FileUploaderFieldConfigTypeDef",
    {
        "accessLevel": StorageAccessLevelType,
        "acceptedFileTypes": Sequence[str],
        "showThumbnails": NotRequired[bool],
        "isResumable": NotRequired[bool],
        "maxFileCount": NotRequired[int],
        "maxSize": NotRequired[int],
    },
)
FormInputBindingPropertiesValuePropertiesTypeDef = TypedDict(
    "FormInputBindingPropertiesValuePropertiesTypeDef",
    {
        "model": NotRequired[str],
    },
)
FormInputValuePropertyBindingPropertiesTypeDef = TypedDict(
    "FormInputValuePropertyBindingPropertiesTypeDef",
    {
        "property": str,
        "field": NotRequired[str],
    },
)
FormStyleConfigTypeDef = TypedDict(
    "FormStyleConfigTypeDef",
    {
        "tokenReference": NotRequired[str],
        "value": NotRequired[str],
    },
)
GetCodegenJobRequestRequestTypeDef = TypedDict(
    "GetCodegenJobRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)
GetComponentRequestRequestTypeDef = TypedDict(
    "GetComponentRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)
GetFormRequestRequestTypeDef = TypedDict(
    "GetFormRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)
GetMetadataRequestRequestTypeDef = TypedDict(
    "GetMetadataRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)
GetThemeRequestRequestTypeDef = TypedDict(
    "GetThemeRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)
ListCodegenJobsRequestRequestTypeDef = TypedDict(
    "ListCodegenJobsRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListComponentsRequestRequestTypeDef = TypedDict(
    "ListComponentsRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListFormsRequestRequestTypeDef = TypedDict(
    "ListFormsRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
ListThemesRequestRequestTypeDef = TypedDict(
    "ListThemesRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ThemeSummaryTypeDef = TypedDict(
    "ThemeSummaryTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "name": str,
    },
)
PredicateTypeDef = TypedDict(
    "PredicateTypeDef",
    {
        "or": NotRequired[Sequence[Mapping[str, Any]]],
        "and": NotRequired[Sequence[Mapping[str, Any]]],
        "field": NotRequired[str],
        "operator": NotRequired[str],
        "operand": NotRequired[str],
        "operandType": NotRequired[str],
    },
)
PutMetadataFlagBodyTypeDef = TypedDict(
    "PutMetadataFlagBodyTypeDef",
    {
        "newValue": str,
    },
)
RefreshTokenRequestBodyTypeDef = TypedDict(
    "RefreshTokenRequestBodyTypeDef",
    {
        "token": str,
        "clientId": NotRequired[str],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)
ThemeValueOutputTypeDef = TypedDict(
    "ThemeValueOutputTypeDef",
    {
        "value": NotRequired[str],
        "children": NotRequired[List[Dict[str, Any]]],
    },
)
ThemeValuePaginatorTypeDef = TypedDict(
    "ThemeValuePaginatorTypeDef",
    {
        "value": NotRequired[str],
        "children": NotRequired[List[Dict[str, Any]]],
    },
)
ThemeValueTypeDef = TypedDict(
    "ThemeValueTypeDef",
    {
        "value": NotRequired[str],
        "children": NotRequired[Sequence[Mapping[str, Any]]],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
ApiConfigurationOutputTypeDef = TypedDict(
    "ApiConfigurationOutputTypeDef",
    {
        "graphQLConfig": NotRequired[GraphQLRenderConfigTypeDef],
        "dataStoreConfig": NotRequired[Dict[str, Any]],
        "noApiConfig": NotRequired[Dict[str, Any]],
    },
)
ApiConfigurationTypeDef = TypedDict(
    "ApiConfigurationTypeDef",
    {
        "graphQLConfig": NotRequired[GraphQLRenderConfigTypeDef],
        "dataStoreConfig": NotRequired[Mapping[str, Any]],
        "noApiConfig": NotRequired[Mapping[str, Any]],
    },
)
CodegenGenericDataEnumUnionTypeDef = Union[
    CodegenGenericDataEnumTypeDef, CodegenGenericDataEnumOutputTypeDef
]
CodegenGenericDataFieldOutputTypeDef = TypedDict(
    "CodegenGenericDataFieldOutputTypeDef",
    {
        "dataType": CodegenGenericDataFieldDataTypeType,
        "dataTypeValue": str,
        "required": bool,
        "readOnly": bool,
        "isArray": bool,
        "relationship": NotRequired[CodegenGenericDataRelationshipTypeOutputTypeDef],
    },
)
CodegenGenericDataRelationshipTypeUnionTypeDef = Union[
    CodegenGenericDataRelationshipTypeTypeDef, CodegenGenericDataRelationshipTypeOutputTypeDef
]
ComponentBindingPropertiesValuePropertiesOutputTypeDef = TypedDict(
    "ComponentBindingPropertiesValuePropertiesOutputTypeDef",
    {
        "model": NotRequired[str],
        "field": NotRequired[str],
        "predicates": NotRequired[List[PredicateOutputTypeDef]],
        "userAttribute": NotRequired[str],
        "bucket": NotRequired[str],
        "key": NotRequired[str],
        "defaultValue": NotRequired[str],
        "slotName": NotRequired[str],
    },
)
ComponentBindingPropertiesValuePropertiesPaginatorTypeDef = TypedDict(
    "ComponentBindingPropertiesValuePropertiesPaginatorTypeDef",
    {
        "model": NotRequired[str],
        "field": NotRequired[str],
        "predicates": NotRequired[List[PredicatePaginatorTypeDef]],
        "userAttribute": NotRequired[str],
        "bucket": NotRequired[str],
        "key": NotRequired[str],
        "defaultValue": NotRequired[str],
        "slotName": NotRequired[str],
    },
)
ComponentConditionPropertyUnionTypeDef = Union[
    ComponentConditionPropertyTypeDef, ComponentConditionPropertyOutputTypeDef
]
ComponentDataConfigurationOutputTypeDef = TypedDict(
    "ComponentDataConfigurationOutputTypeDef",
    {
        "model": str,
        "sort": NotRequired[List[SortPropertyTypeDef]],
        "predicate": NotRequired[PredicateOutputTypeDef],
        "identifiers": NotRequired[List[str]],
    },
)
ComponentDataConfigurationPaginatorTypeDef = TypedDict(
    "ComponentDataConfigurationPaginatorTypeDef",
    {
        "model": str,
        "sort": NotRequired[List[SortPropertyTypeDef]],
        "predicate": NotRequired[PredicatePaginatorTypeDef],
        "identifiers": NotRequired[List[str]],
    },
)
ComponentPropertyOutputTypeDef = TypedDict(
    "ComponentPropertyOutputTypeDef",
    {
        "value": NotRequired[str],
        "bindingProperties": NotRequired[ComponentPropertyBindingPropertiesTypeDef],
        "collectionBindingProperties": NotRequired[ComponentPropertyBindingPropertiesTypeDef],
        "defaultValue": NotRequired[str],
        "model": NotRequired[str],
        "bindings": NotRequired[Dict[str, FormBindingElementTypeDef]],
        "event": NotRequired[str],
        "userAttribute": NotRequired[str],
        "concat": NotRequired[List[Dict[str, Any]]],
        "condition": NotRequired[ComponentConditionPropertyOutputTypeDef],
        "configured": NotRequired[bool],
        "type": NotRequired[str],
        "importedValue": NotRequired[str],
        "componentName": NotRequired[str],
        "property": NotRequired[str],
    },
)
ComponentPropertyPaginatorTypeDef = TypedDict(
    "ComponentPropertyPaginatorTypeDef",
    {
        "value": NotRequired[str],
        "bindingProperties": NotRequired[ComponentPropertyBindingPropertiesTypeDef],
        "collectionBindingProperties": NotRequired[ComponentPropertyBindingPropertiesTypeDef],
        "defaultValue": NotRequired[str],
        "model": NotRequired[str],
        "bindings": NotRequired[Dict[str, FormBindingElementTypeDef]],
        "event": NotRequired[str],
        "userAttribute": NotRequired[str],
        "concat": NotRequired[List[Dict[str, Any]]],
        "condition": NotRequired[ComponentConditionPropertyPaginatorTypeDef],
        "configured": NotRequired[bool],
        "type": NotRequired[str],
        "importedValue": NotRequired[str],
        "componentName": NotRequired[str],
        "property": NotRequired[str],
    },
)
ComponentVariantUnionTypeDef = Union[ComponentVariantTypeDef, ComponentVariantOutputTypeDef]
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExchangeCodeForTokenResponseTypeDef = TypedDict(
    "ExchangeCodeForTokenResponseTypeDef",
    {
        "accessToken": str,
        "expiresIn": int,
        "refreshToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMetadataResponseTypeDef = TypedDict(
    "GetMetadataResponseTypeDef",
    {
        "features": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCodegenJobsResponseTypeDef = TypedDict(
    "ListCodegenJobsResponseTypeDef",
    {
        "entities": List[CodegenJobSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListComponentsResponseTypeDef = TypedDict(
    "ListComponentsResponseTypeDef",
    {
        "entities": List[ComponentSummaryTypeDef],
        "nextToken": str,
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
RefreshTokenResponseTypeDef = TypedDict(
    "RefreshTokenResponseTypeDef",
    {
        "accessToken": str,
        "expiresIn": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FormSummaryTypeDef = TypedDict(
    "FormSummaryTypeDef",
    {
        "appId": str,
        "dataType": FormDataTypeConfigTypeDef,
        "environmentName": str,
        "formActionType": FormActionTypeType,
        "id": str,
        "name": str,
    },
)
ExchangeCodeForTokenRequestRequestTypeDef = TypedDict(
    "ExchangeCodeForTokenRequestRequestTypeDef",
    {
        "provider": Literal["figma"],
        "request": ExchangeCodeForTokenRequestBodyTypeDef,
    },
)
ExportComponentsRequestExportComponentsPaginateTypeDef = TypedDict(
    "ExportComponentsRequestExportComponentsPaginateTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ExportFormsRequestExportFormsPaginateTypeDef = TypedDict(
    "ExportFormsRequestExportFormsPaginateTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ExportThemesRequestExportThemesPaginateTypeDef = TypedDict(
    "ExportThemesRequestExportThemesPaginateTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCodegenJobsRequestListCodegenJobsPaginateTypeDef = TypedDict(
    "ListCodegenJobsRequestListCodegenJobsPaginateTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListComponentsRequestListComponentsPaginateTypeDef = TypedDict(
    "ListComponentsRequestListComponentsPaginateTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFormsRequestListFormsPaginateTypeDef = TypedDict(
    "ListFormsRequestListFormsPaginateTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListThemesRequestListThemesPaginateTypeDef = TypedDict(
    "ListThemesRequestListThemesPaginateTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
FormButtonTypeDef = TypedDict(
    "FormButtonTypeDef",
    {
        "excluded": NotRequired[bool],
        "children": NotRequired[str],
        "position": NotRequired[FieldPositionTypeDef],
    },
)
SectionalElementTypeDef = TypedDict(
    "SectionalElementTypeDef",
    {
        "type": str,
        "position": NotRequired[FieldPositionTypeDef],
        "text": NotRequired[str],
        "level": NotRequired[int],
        "orientation": NotRequired[str],
        "excluded": NotRequired[bool],
    },
)
FieldValidationConfigurationUnionTypeDef = Union[
    FieldValidationConfigurationTypeDef, FieldValidationConfigurationOutputTypeDef
]
FileUploaderFieldConfigUnionTypeDef = Union[
    FileUploaderFieldConfigTypeDef, FileUploaderFieldConfigOutputTypeDef
]
FormInputBindingPropertiesValueTypeDef = TypedDict(
    "FormInputBindingPropertiesValueTypeDef",
    {
        "type": NotRequired[str],
        "bindingProperties": NotRequired[FormInputBindingPropertiesValuePropertiesTypeDef],
    },
)
FormInputValuePropertyOutputTypeDef = TypedDict(
    "FormInputValuePropertyOutputTypeDef",
    {
        "value": NotRequired[str],
        "bindingProperties": NotRequired[FormInputValuePropertyBindingPropertiesTypeDef],
        "concat": NotRequired[List[Dict[str, Any]]],
    },
)
FormInputValuePropertyPaginatorTypeDef = TypedDict(
    "FormInputValuePropertyPaginatorTypeDef",
    {
        "value": NotRequired[str],
        "bindingProperties": NotRequired[FormInputValuePropertyBindingPropertiesTypeDef],
        "concat": NotRequired[List[Dict[str, Any]]],
    },
)
FormInputValuePropertyTypeDef = TypedDict(
    "FormInputValuePropertyTypeDef",
    {
        "value": NotRequired[str],
        "bindingProperties": NotRequired[FormInputValuePropertyBindingPropertiesTypeDef],
        "concat": NotRequired[Sequence[Mapping[str, Any]]],
    },
)
FormStyleTypeDef = TypedDict(
    "FormStyleTypeDef",
    {
        "horizontalGap": NotRequired[FormStyleConfigTypeDef],
        "verticalGap": NotRequired[FormStyleConfigTypeDef],
        "outerPadding": NotRequired[FormStyleConfigTypeDef],
    },
)
ListThemesResponseTypeDef = TypedDict(
    "ListThemesResponseTypeDef",
    {
        "entities": List[ThemeSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PredicateUnionTypeDef = Union[PredicateTypeDef, PredicateOutputTypeDef]
PutMetadataFlagRequestRequestTypeDef = TypedDict(
    "PutMetadataFlagRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "featureName": str,
        "body": PutMetadataFlagBodyTypeDef,
    },
)
RefreshTokenRequestRequestTypeDef = TypedDict(
    "RefreshTokenRequestRequestTypeDef",
    {
        "provider": Literal["figma"],
        "refreshTokenBody": RefreshTokenRequestBodyTypeDef,
    },
)
ThemeValuesOutputTypeDef = TypedDict(
    "ThemeValuesOutputTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[ThemeValueOutputTypeDef],
    },
)
ThemeValuesPaginatorTypeDef = TypedDict(
    "ThemeValuesPaginatorTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[ThemeValuePaginatorTypeDef],
    },
)
ThemeValueUnionTypeDef = Union[ThemeValueTypeDef, ThemeValueOutputTypeDef]
ReactStartCodegenJobDataOutputTypeDef = TypedDict(
    "ReactStartCodegenJobDataOutputTypeDef",
    {
        "module": NotRequired[JSModuleType],
        "target": NotRequired[JSTargetType],
        "script": NotRequired[JSScriptType],
        "renderTypeDeclarations": NotRequired[bool],
        "inlineSourceMap": NotRequired[bool],
        "apiConfiguration": NotRequired[ApiConfigurationOutputTypeDef],
        "dependencies": NotRequired[Dict[str, str]],
    },
)
ApiConfigurationUnionTypeDef = Union[ApiConfigurationTypeDef, ApiConfigurationOutputTypeDef]
CodegenGenericDataModelOutputTypeDef = TypedDict(
    "CodegenGenericDataModelOutputTypeDef",
    {
        "fields": Dict[str, CodegenGenericDataFieldOutputTypeDef],
        "primaryKeys": List[str],
        "isJoinTable": NotRequired[bool],
    },
)
CodegenGenericDataNonModelOutputTypeDef = TypedDict(
    "CodegenGenericDataNonModelOutputTypeDef",
    {
        "fields": Dict[str, CodegenGenericDataFieldOutputTypeDef],
    },
)
CodegenGenericDataFieldTypeDef = TypedDict(
    "CodegenGenericDataFieldTypeDef",
    {
        "dataType": CodegenGenericDataFieldDataTypeType,
        "dataTypeValue": str,
        "required": bool,
        "readOnly": bool,
        "isArray": bool,
        "relationship": NotRequired[CodegenGenericDataRelationshipTypeUnionTypeDef],
    },
)
ComponentBindingPropertiesValueOutputTypeDef = TypedDict(
    "ComponentBindingPropertiesValueOutputTypeDef",
    {
        "type": NotRequired[str],
        "bindingProperties": NotRequired[ComponentBindingPropertiesValuePropertiesOutputTypeDef],
        "defaultValue": NotRequired[str],
    },
)
ComponentBindingPropertiesValuePaginatorTypeDef = TypedDict(
    "ComponentBindingPropertiesValuePaginatorTypeDef",
    {
        "type": NotRequired[str],
        "bindingProperties": NotRequired[ComponentBindingPropertiesValuePropertiesPaginatorTypeDef],
        "defaultValue": NotRequired[str],
    },
)
ComponentPropertyTypeDef = TypedDict(
    "ComponentPropertyTypeDef",
    {
        "value": NotRequired[str],
        "bindingProperties": NotRequired[ComponentPropertyBindingPropertiesTypeDef],
        "collectionBindingProperties": NotRequired[ComponentPropertyBindingPropertiesTypeDef],
        "defaultValue": NotRequired[str],
        "model": NotRequired[str],
        "bindings": NotRequired[Mapping[str, FormBindingElementTypeDef]],
        "event": NotRequired[str],
        "userAttribute": NotRequired[str],
        "concat": NotRequired[Sequence[Mapping[str, Any]]],
        "condition": NotRequired[ComponentConditionPropertyUnionTypeDef],
        "configured": NotRequired[bool],
        "type": NotRequired[str],
        "importedValue": NotRequired[str],
        "componentName": NotRequired[str],
        "property": NotRequired[str],
    },
)
MutationActionSetStateParameterOutputTypeDef = TypedDict(
    "MutationActionSetStateParameterOutputTypeDef",
    {
        "componentName": str,
        "property": str,
        "set": ComponentPropertyOutputTypeDef,
    },
)
MutationActionSetStateParameterPaginatorTypeDef = TypedDict(
    "MutationActionSetStateParameterPaginatorTypeDef",
    {
        "componentName": str,
        "property": str,
        "set": ComponentPropertyPaginatorTypeDef,
    },
)
ListFormsResponseTypeDef = TypedDict(
    "ListFormsResponseTypeDef",
    {
        "entities": List[FormSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FormCTATypeDef = TypedDict(
    "FormCTATypeDef",
    {
        "position": NotRequired[FormButtonsPositionType],
        "clear": NotRequired[FormButtonTypeDef],
        "cancel": NotRequired[FormButtonTypeDef],
        "submit": NotRequired[FormButtonTypeDef],
    },
)
ValueMappingOutputTypeDef = TypedDict(
    "ValueMappingOutputTypeDef",
    {
        "value": FormInputValuePropertyOutputTypeDef,
        "displayValue": NotRequired[FormInputValuePropertyOutputTypeDef],
    },
)
ValueMappingPaginatorTypeDef = TypedDict(
    "ValueMappingPaginatorTypeDef",
    {
        "value": FormInputValuePropertyPaginatorTypeDef,
        "displayValue": NotRequired[FormInputValuePropertyPaginatorTypeDef],
    },
)
FormInputValuePropertyUnionTypeDef = Union[
    FormInputValuePropertyTypeDef, FormInputValuePropertyOutputTypeDef
]
ComponentBindingPropertiesValuePropertiesTypeDef = TypedDict(
    "ComponentBindingPropertiesValuePropertiesTypeDef",
    {
        "model": NotRequired[str],
        "field": NotRequired[str],
        "predicates": NotRequired[Sequence[PredicateUnionTypeDef]],
        "userAttribute": NotRequired[str],
        "bucket": NotRequired[str],
        "key": NotRequired[str],
        "defaultValue": NotRequired[str],
        "slotName": NotRequired[str],
    },
)
ComponentDataConfigurationTypeDef = TypedDict(
    "ComponentDataConfigurationTypeDef",
    {
        "model": str,
        "sort": NotRequired[Sequence[SortPropertyTypeDef]],
        "predicate": NotRequired[PredicateUnionTypeDef],
        "identifiers": NotRequired[Sequence[str]],
    },
)
ThemeTypeDef = TypedDict(
    "ThemeTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "name": str,
        "createdAt": datetime,
        "values": List[ThemeValuesOutputTypeDef],
        "modifiedAt": NotRequired[datetime],
        "overrides": NotRequired[List[ThemeValuesOutputTypeDef]],
        "tags": NotRequired[Dict[str, str]],
    },
)
ThemePaginatorTypeDef = TypedDict(
    "ThemePaginatorTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "name": str,
        "createdAt": datetime,
        "values": List[ThemeValuesPaginatorTypeDef],
        "modifiedAt": NotRequired[datetime],
        "overrides": NotRequired[List[ThemeValuesPaginatorTypeDef]],
        "tags": NotRequired[Dict[str, str]],
    },
)
ThemeValuesTypeDef = TypedDict(
    "ThemeValuesTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[ThemeValueUnionTypeDef],
    },
)
CodegenJobRenderConfigOutputTypeDef = TypedDict(
    "CodegenJobRenderConfigOutputTypeDef",
    {
        "react": NotRequired[ReactStartCodegenJobDataOutputTypeDef],
    },
)
ReactStartCodegenJobDataTypeDef = TypedDict(
    "ReactStartCodegenJobDataTypeDef",
    {
        "module": NotRequired[JSModuleType],
        "target": NotRequired[JSTargetType],
        "script": NotRequired[JSScriptType],
        "renderTypeDeclarations": NotRequired[bool],
        "inlineSourceMap": NotRequired[bool],
        "apiConfiguration": NotRequired[ApiConfigurationUnionTypeDef],
        "dependencies": NotRequired[Mapping[str, str]],
    },
)
CodegenJobGenericDataSchemaOutputTypeDef = TypedDict(
    "CodegenJobGenericDataSchemaOutputTypeDef",
    {
        "dataSourceType": Literal["DataStore"],
        "models": Dict[str, CodegenGenericDataModelOutputTypeDef],
        "enums": Dict[str, CodegenGenericDataEnumOutputTypeDef],
        "nonModels": Dict[str, CodegenGenericDataNonModelOutputTypeDef],
    },
)
CodegenGenericDataFieldUnionTypeDef = Union[
    CodegenGenericDataFieldTypeDef, CodegenGenericDataFieldOutputTypeDef
]
CodegenGenericDataNonModelTypeDef = TypedDict(
    "CodegenGenericDataNonModelTypeDef",
    {
        "fields": Mapping[str, CodegenGenericDataFieldTypeDef],
    },
)
ComponentPropertyUnionTypeDef = Union[ComponentPropertyTypeDef, ComponentPropertyOutputTypeDef]
ActionParametersOutputTypeDef = TypedDict(
    "ActionParametersOutputTypeDef",
    {
        "type": NotRequired[ComponentPropertyOutputTypeDef],
        "url": NotRequired[ComponentPropertyOutputTypeDef],
        "anchor": NotRequired[ComponentPropertyOutputTypeDef],
        "target": NotRequired[ComponentPropertyOutputTypeDef],
        "global": NotRequired[ComponentPropertyOutputTypeDef],
        "model": NotRequired[str],
        "id": NotRequired[ComponentPropertyOutputTypeDef],
        "fields": NotRequired[Dict[str, ComponentPropertyOutputTypeDef]],
        "state": NotRequired[MutationActionSetStateParameterOutputTypeDef],
    },
)
ActionParametersPaginatorTypeDef = TypedDict(
    "ActionParametersPaginatorTypeDef",
    {
        "type": NotRequired[ComponentPropertyPaginatorTypeDef],
        "url": NotRequired[ComponentPropertyPaginatorTypeDef],
        "anchor": NotRequired[ComponentPropertyPaginatorTypeDef],
        "target": NotRequired[ComponentPropertyPaginatorTypeDef],
        "global": NotRequired[ComponentPropertyPaginatorTypeDef],
        "model": NotRequired[str],
        "id": NotRequired[ComponentPropertyPaginatorTypeDef],
        "fields": NotRequired[Dict[str, ComponentPropertyPaginatorTypeDef]],
        "state": NotRequired[MutationActionSetStateParameterPaginatorTypeDef],
    },
)
ValueMappingsOutputTypeDef = TypedDict(
    "ValueMappingsOutputTypeDef",
    {
        "values": List[ValueMappingOutputTypeDef],
        "bindingProperties": NotRequired[Dict[str, FormInputBindingPropertiesValueTypeDef]],
    },
)
ValueMappingsPaginatorTypeDef = TypedDict(
    "ValueMappingsPaginatorTypeDef",
    {
        "values": List[ValueMappingPaginatorTypeDef],
        "bindingProperties": NotRequired[Dict[str, FormInputBindingPropertiesValueTypeDef]],
    },
)
ValueMappingTypeDef = TypedDict(
    "ValueMappingTypeDef",
    {
        "value": FormInputValuePropertyUnionTypeDef,
        "displayValue": NotRequired[FormInputValuePropertyUnionTypeDef],
    },
)
ComponentBindingPropertiesValuePropertiesUnionTypeDef = Union[
    ComponentBindingPropertiesValuePropertiesTypeDef,
    ComponentBindingPropertiesValuePropertiesOutputTypeDef,
]
ComponentDataConfigurationUnionTypeDef = Union[
    ComponentDataConfigurationTypeDef, ComponentDataConfigurationOutputTypeDef
]
CreateThemeResponseTypeDef = TypedDict(
    "CreateThemeResponseTypeDef",
    {
        "entity": ThemeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportThemesResponseTypeDef = TypedDict(
    "ExportThemesResponseTypeDef",
    {
        "entities": List[ThemeTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetThemeResponseTypeDef = TypedDict(
    "GetThemeResponseTypeDef",
    {
        "theme": ThemeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateThemeResponseTypeDef = TypedDict(
    "UpdateThemeResponseTypeDef",
    {
        "entity": ThemeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportThemesResponsePaginatorTypeDef = TypedDict(
    "ExportThemesResponsePaginatorTypeDef",
    {
        "entities": List[ThemePaginatorTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ThemeValuesUnionTypeDef = Union[ThemeValuesTypeDef, ThemeValuesOutputTypeDef]
ReactStartCodegenJobDataUnionTypeDef = Union[
    ReactStartCodegenJobDataTypeDef, ReactStartCodegenJobDataOutputTypeDef
]
CodegenJobTypeDef = TypedDict(
    "CodegenJobTypeDef",
    {
        "id": str,
        "appId": str,
        "environmentName": str,
        "renderConfig": NotRequired[CodegenJobRenderConfigOutputTypeDef],
        "genericDataSchema": NotRequired[CodegenJobGenericDataSchemaOutputTypeDef],
        "autoGenerateForms": NotRequired[bool],
        "features": NotRequired[CodegenFeatureFlagsTypeDef],
        "status": NotRequired[CodegenJobStatusType],
        "statusMessage": NotRequired[str],
        "asset": NotRequired[CodegenJobAssetTypeDef],
        "tags": NotRequired[Dict[str, str]],
        "createdAt": NotRequired[datetime],
        "modifiedAt": NotRequired[datetime],
        "dependencies": NotRequired[List[CodegenDependencyTypeDef]],
    },
)
CodegenGenericDataModelTypeDef = TypedDict(
    "CodegenGenericDataModelTypeDef",
    {
        "fields": Mapping[str, CodegenGenericDataFieldUnionTypeDef],
        "primaryKeys": Sequence[str],
        "isJoinTable": NotRequired[bool],
    },
)
CodegenGenericDataNonModelUnionTypeDef = Union[
    CodegenGenericDataNonModelTypeDef, CodegenGenericDataNonModelOutputTypeDef
]
MutationActionSetStateParameterTypeDef = TypedDict(
    "MutationActionSetStateParameterTypeDef",
    {
        "componentName": str,
        "property": str,
        "set": ComponentPropertyUnionTypeDef,
    },
)
ComponentEventOutputTypeDef = TypedDict(
    "ComponentEventOutputTypeDef",
    {
        "action": NotRequired[str],
        "parameters": NotRequired[ActionParametersOutputTypeDef],
        "bindingEvent": NotRequired[str],
    },
)
ComponentEventPaginatorTypeDef = TypedDict(
    "ComponentEventPaginatorTypeDef",
    {
        "action": NotRequired[str],
        "parameters": NotRequired[ActionParametersPaginatorTypeDef],
        "bindingEvent": NotRequired[str],
    },
)
FieldInputConfigOutputTypeDef = TypedDict(
    "FieldInputConfigOutputTypeDef",
    {
        "type": str,
        "required": NotRequired[bool],
        "readOnly": NotRequired[bool],
        "placeholder": NotRequired[str],
        "defaultValue": NotRequired[str],
        "descriptiveText": NotRequired[str],
        "defaultChecked": NotRequired[bool],
        "defaultCountryCode": NotRequired[str],
        "valueMappings": NotRequired[ValueMappingsOutputTypeDef],
        "name": NotRequired[str],
        "minValue": NotRequired[float],
        "maxValue": NotRequired[float],
        "step": NotRequired[float],
        "value": NotRequired[str],
        "isArray": NotRequired[bool],
        "fileUploaderConfig": NotRequired[FileUploaderFieldConfigOutputTypeDef],
    },
)
FieldInputConfigPaginatorTypeDef = TypedDict(
    "FieldInputConfigPaginatorTypeDef",
    {
        "type": str,
        "required": NotRequired[bool],
        "readOnly": NotRequired[bool],
        "placeholder": NotRequired[str],
        "defaultValue": NotRequired[str],
        "descriptiveText": NotRequired[str],
        "defaultChecked": NotRequired[bool],
        "defaultCountryCode": NotRequired[str],
        "valueMappings": NotRequired[ValueMappingsPaginatorTypeDef],
        "name": NotRequired[str],
        "minValue": NotRequired[float],
        "maxValue": NotRequired[float],
        "step": NotRequired[float],
        "value": NotRequired[str],
        "isArray": NotRequired[bool],
        "fileUploaderConfig": NotRequired[FileUploaderFieldConfigOutputTypeDef],
    },
)
ValueMappingUnionTypeDef = Union[ValueMappingTypeDef, ValueMappingOutputTypeDef]
ComponentBindingPropertiesValueTypeDef = TypedDict(
    "ComponentBindingPropertiesValueTypeDef",
    {
        "type": NotRequired[str],
        "bindingProperties": NotRequired[ComponentBindingPropertiesValuePropertiesUnionTypeDef],
        "defaultValue": NotRequired[str],
    },
)
CreateThemeDataTypeDef = TypedDict(
    "CreateThemeDataTypeDef",
    {
        "name": str,
        "values": Sequence[ThemeValuesUnionTypeDef],
        "overrides": NotRequired[Sequence[ThemeValuesTypeDef]],
        "tags": NotRequired[Mapping[str, str]],
    },
)
UpdateThemeDataTypeDef = TypedDict(
    "UpdateThemeDataTypeDef",
    {
        "values": Sequence[ThemeValuesUnionTypeDef],
        "id": NotRequired[str],
        "name": NotRequired[str],
        "overrides": NotRequired[Sequence[ThemeValuesTypeDef]],
    },
)
CodegenJobRenderConfigTypeDef = TypedDict(
    "CodegenJobRenderConfigTypeDef",
    {
        "react": NotRequired[ReactStartCodegenJobDataUnionTypeDef],
    },
)
GetCodegenJobResponseTypeDef = TypedDict(
    "GetCodegenJobResponseTypeDef",
    {
        "job": CodegenJobTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartCodegenJobResponseTypeDef = TypedDict(
    "StartCodegenJobResponseTypeDef",
    {
        "entity": CodegenJobTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CodegenGenericDataModelUnionTypeDef = Union[
    CodegenGenericDataModelTypeDef, CodegenGenericDataModelOutputTypeDef
]
MutationActionSetStateParameterUnionTypeDef = Union[
    MutationActionSetStateParameterTypeDef, MutationActionSetStateParameterOutputTypeDef
]
ComponentChildOutputTypeDef = TypedDict(
    "ComponentChildOutputTypeDef",
    {
        "componentType": str,
        "name": str,
        "properties": Dict[str, ComponentPropertyOutputTypeDef],
        "children": NotRequired[List[Dict[str, Any]]],
        "events": NotRequired[Dict[str, ComponentEventOutputTypeDef]],
        "sourceId": NotRequired[str],
    },
)
ComponentChildPaginatorTypeDef = TypedDict(
    "ComponentChildPaginatorTypeDef",
    {
        "componentType": str,
        "name": str,
        "properties": Dict[str, ComponentPropertyPaginatorTypeDef],
        "children": NotRequired[List[Dict[str, Any]]],
        "events": NotRequired[Dict[str, ComponentEventPaginatorTypeDef]],
        "sourceId": NotRequired[str],
    },
)
FieldConfigOutputTypeDef = TypedDict(
    "FieldConfigOutputTypeDef",
    {
        "label": NotRequired[str],
        "position": NotRequired[FieldPositionTypeDef],
        "excluded": NotRequired[bool],
        "inputType": NotRequired[FieldInputConfigOutputTypeDef],
        "validations": NotRequired[List[FieldValidationConfigurationOutputTypeDef]],
    },
)
FieldConfigPaginatorTypeDef = TypedDict(
    "FieldConfigPaginatorTypeDef",
    {
        "label": NotRequired[str],
        "position": NotRequired[FieldPositionTypeDef],
        "excluded": NotRequired[bool],
        "inputType": NotRequired[FieldInputConfigPaginatorTypeDef],
        "validations": NotRequired[List[FieldValidationConfigurationOutputTypeDef]],
    },
)
ValueMappingsTypeDef = TypedDict(
    "ValueMappingsTypeDef",
    {
        "values": Sequence[ValueMappingUnionTypeDef],
        "bindingProperties": NotRequired[Mapping[str, FormInputBindingPropertiesValueTypeDef]],
    },
)
ComponentBindingPropertiesValueUnionTypeDef = Union[
    ComponentBindingPropertiesValueTypeDef, ComponentBindingPropertiesValueOutputTypeDef
]
CreateThemeRequestRequestTypeDef = TypedDict(
    "CreateThemeRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "themeToCreate": CreateThemeDataTypeDef,
        "clientToken": NotRequired[str],
    },
)
UpdateThemeRequestRequestTypeDef = TypedDict(
    "UpdateThemeRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "updatedTheme": UpdateThemeDataTypeDef,
        "clientToken": NotRequired[str],
    },
)
CodegenJobRenderConfigUnionTypeDef = Union[
    CodegenJobRenderConfigTypeDef, CodegenJobRenderConfigOutputTypeDef
]
CodegenJobGenericDataSchemaTypeDef = TypedDict(
    "CodegenJobGenericDataSchemaTypeDef",
    {
        "dataSourceType": Literal["DataStore"],
        "models": Mapping[str, CodegenGenericDataModelUnionTypeDef],
        "enums": Mapping[str, CodegenGenericDataEnumUnionTypeDef],
        "nonModels": Mapping[str, CodegenGenericDataNonModelUnionTypeDef],
    },
)
ActionParametersTypeDef = TypedDict(
    "ActionParametersTypeDef",
    {
        "type": NotRequired[ComponentPropertyUnionTypeDef],
        "url": NotRequired[ComponentPropertyUnionTypeDef],
        "anchor": NotRequired[ComponentPropertyUnionTypeDef],
        "target": NotRequired[ComponentPropertyUnionTypeDef],
        "global": NotRequired[ComponentPropertyUnionTypeDef],
        "model": NotRequired[str],
        "id": NotRequired[ComponentPropertyUnionTypeDef],
        "fields": NotRequired[Mapping[str, ComponentPropertyTypeDef]],
        "state": NotRequired[MutationActionSetStateParameterUnionTypeDef],
    },
)
ComponentTypeDef = TypedDict(
    "ComponentTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "name": str,
        "componentType": str,
        "properties": Dict[str, ComponentPropertyOutputTypeDef],
        "variants": List[ComponentVariantOutputTypeDef],
        "overrides": Dict[str, Dict[str, str]],
        "bindingProperties": Dict[str, ComponentBindingPropertiesValueOutputTypeDef],
        "createdAt": datetime,
        "sourceId": NotRequired[str],
        "children": NotRequired[List[ComponentChildOutputTypeDef]],
        "collectionProperties": NotRequired[Dict[str, ComponentDataConfigurationOutputTypeDef]],
        "modifiedAt": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
        "events": NotRequired[Dict[str, ComponentEventOutputTypeDef]],
        "schemaVersion": NotRequired[str],
    },
)
ComponentPaginatorTypeDef = TypedDict(
    "ComponentPaginatorTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "name": str,
        "componentType": str,
        "properties": Dict[str, ComponentPropertyPaginatorTypeDef],
        "variants": List[ComponentVariantOutputTypeDef],
        "overrides": Dict[str, Dict[str, str]],
        "bindingProperties": Dict[str, ComponentBindingPropertiesValuePaginatorTypeDef],
        "createdAt": datetime,
        "sourceId": NotRequired[str],
        "children": NotRequired[List[ComponentChildPaginatorTypeDef]],
        "collectionProperties": NotRequired[Dict[str, ComponentDataConfigurationPaginatorTypeDef]],
        "modifiedAt": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
        "events": NotRequired[Dict[str, ComponentEventPaginatorTypeDef]],
        "schemaVersion": NotRequired[str],
    },
)
FormTypeDef = TypedDict(
    "FormTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "name": str,
        "formActionType": FormActionTypeType,
        "style": FormStyleTypeDef,
        "dataType": FormDataTypeConfigTypeDef,
        "fields": Dict[str, FieldConfigOutputTypeDef],
        "sectionalElements": Dict[str, SectionalElementTypeDef],
        "schemaVersion": str,
        "tags": NotRequired[Dict[str, str]],
        "cta": NotRequired[FormCTATypeDef],
        "labelDecorator": NotRequired[LabelDecoratorType],
    },
)
FormPaginatorTypeDef = TypedDict(
    "FormPaginatorTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "name": str,
        "formActionType": FormActionTypeType,
        "style": FormStyleTypeDef,
        "dataType": FormDataTypeConfigTypeDef,
        "fields": Dict[str, FieldConfigPaginatorTypeDef],
        "sectionalElements": Dict[str, SectionalElementTypeDef],
        "schemaVersion": str,
        "tags": NotRequired[Dict[str, str]],
        "cta": NotRequired[FormCTATypeDef],
        "labelDecorator": NotRequired[LabelDecoratorType],
    },
)
ValueMappingsUnionTypeDef = Union[ValueMappingsTypeDef, ValueMappingsOutputTypeDef]
CodegenJobGenericDataSchemaUnionTypeDef = Union[
    CodegenJobGenericDataSchemaTypeDef, CodegenJobGenericDataSchemaOutputTypeDef
]
ActionParametersUnionTypeDef = Union[ActionParametersTypeDef, ActionParametersOutputTypeDef]
CreateComponentResponseTypeDef = TypedDict(
    "CreateComponentResponseTypeDef",
    {
        "entity": ComponentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportComponentsResponseTypeDef = TypedDict(
    "ExportComponentsResponseTypeDef",
    {
        "entities": List[ComponentTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetComponentResponseTypeDef = TypedDict(
    "GetComponentResponseTypeDef",
    {
        "component": ComponentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateComponentResponseTypeDef = TypedDict(
    "UpdateComponentResponseTypeDef",
    {
        "entity": ComponentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportComponentsResponsePaginatorTypeDef = TypedDict(
    "ExportComponentsResponsePaginatorTypeDef",
    {
        "entities": List[ComponentPaginatorTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFormResponseTypeDef = TypedDict(
    "CreateFormResponseTypeDef",
    {
        "entity": FormTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportFormsResponseTypeDef = TypedDict(
    "ExportFormsResponseTypeDef",
    {
        "entities": List[FormTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFormResponseTypeDef = TypedDict(
    "GetFormResponseTypeDef",
    {
        "form": FormTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFormResponseTypeDef = TypedDict(
    "UpdateFormResponseTypeDef",
    {
        "entity": FormTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportFormsResponsePaginatorTypeDef = TypedDict(
    "ExportFormsResponsePaginatorTypeDef",
    {
        "entities": List[FormPaginatorTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FieldInputConfigTypeDef = TypedDict(
    "FieldInputConfigTypeDef",
    {
        "type": str,
        "required": NotRequired[bool],
        "readOnly": NotRequired[bool],
        "placeholder": NotRequired[str],
        "defaultValue": NotRequired[str],
        "descriptiveText": NotRequired[str],
        "defaultChecked": NotRequired[bool],
        "defaultCountryCode": NotRequired[str],
        "valueMappings": NotRequired[ValueMappingsUnionTypeDef],
        "name": NotRequired[str],
        "minValue": NotRequired[float],
        "maxValue": NotRequired[float],
        "step": NotRequired[float],
        "value": NotRequired[str],
        "isArray": NotRequired[bool],
        "fileUploaderConfig": NotRequired[FileUploaderFieldConfigUnionTypeDef],
    },
)
StartCodegenJobDataTypeDef = TypedDict(
    "StartCodegenJobDataTypeDef",
    {
        "renderConfig": CodegenJobRenderConfigUnionTypeDef,
        "genericDataSchema": NotRequired[CodegenJobGenericDataSchemaUnionTypeDef],
        "autoGenerateForms": NotRequired[bool],
        "features": NotRequired[CodegenFeatureFlagsTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
ComponentEventTypeDef = TypedDict(
    "ComponentEventTypeDef",
    {
        "action": NotRequired[str],
        "parameters": NotRequired[ActionParametersUnionTypeDef],
        "bindingEvent": NotRequired[str],
    },
)
FieldInputConfigUnionTypeDef = Union[FieldInputConfigTypeDef, FieldInputConfigOutputTypeDef]
StartCodegenJobRequestRequestTypeDef = TypedDict(
    "StartCodegenJobRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "codegenJobToCreate": StartCodegenJobDataTypeDef,
        "clientToken": NotRequired[str],
    },
)
ComponentEventUnionTypeDef = Union[ComponentEventTypeDef, ComponentEventOutputTypeDef]
FieldConfigTypeDef = TypedDict(
    "FieldConfigTypeDef",
    {
        "label": NotRequired[str],
        "position": NotRequired[FieldPositionTypeDef],
        "excluded": NotRequired[bool],
        "inputType": NotRequired[FieldInputConfigUnionTypeDef],
        "validations": NotRequired[Sequence[FieldValidationConfigurationUnionTypeDef]],
    },
)
ComponentChildTypeDef = TypedDict(
    "ComponentChildTypeDef",
    {
        "componentType": str,
        "name": str,
        "properties": Mapping[str, ComponentPropertyTypeDef],
        "children": NotRequired[Sequence[Mapping[str, Any]]],
        "events": NotRequired[Mapping[str, ComponentEventUnionTypeDef]],
        "sourceId": NotRequired[str],
    },
)
FieldConfigUnionTypeDef = Union[FieldConfigTypeDef, FieldConfigOutputTypeDef]
ComponentChildUnionTypeDef = Union[ComponentChildTypeDef, ComponentChildOutputTypeDef]
CreateFormDataTypeDef = TypedDict(
    "CreateFormDataTypeDef",
    {
        "name": str,
        "dataType": FormDataTypeConfigTypeDef,
        "formActionType": FormActionTypeType,
        "fields": Mapping[str, FieldConfigUnionTypeDef],
        "style": FormStyleTypeDef,
        "sectionalElements": Mapping[str, SectionalElementTypeDef],
        "schemaVersion": str,
        "cta": NotRequired[FormCTATypeDef],
        "tags": NotRequired[Mapping[str, str]],
        "labelDecorator": NotRequired[LabelDecoratorType],
    },
)
UpdateFormDataTypeDef = TypedDict(
    "UpdateFormDataTypeDef",
    {
        "name": NotRequired[str],
        "dataType": NotRequired[FormDataTypeConfigTypeDef],
        "formActionType": NotRequired[FormActionTypeType],
        "fields": NotRequired[Mapping[str, FieldConfigUnionTypeDef]],
        "style": NotRequired[FormStyleTypeDef],
        "sectionalElements": NotRequired[Mapping[str, SectionalElementTypeDef]],
        "schemaVersion": NotRequired[str],
        "cta": NotRequired[FormCTATypeDef],
        "labelDecorator": NotRequired[LabelDecoratorType],
    },
)
CreateComponentDataTypeDef = TypedDict(
    "CreateComponentDataTypeDef",
    {
        "name": str,
        "componentType": str,
        "properties": Mapping[str, ComponentPropertyUnionTypeDef],
        "variants": Sequence[ComponentVariantUnionTypeDef],
        "overrides": Mapping[str, Mapping[str, str]],
        "bindingProperties": Mapping[str, ComponentBindingPropertiesValueUnionTypeDef],
        "sourceId": NotRequired[str],
        "children": NotRequired[Sequence[ComponentChildUnionTypeDef]],
        "collectionProperties": NotRequired[Mapping[str, ComponentDataConfigurationUnionTypeDef]],
        "tags": NotRequired[Mapping[str, str]],
        "events": NotRequired[Mapping[str, ComponentEventTypeDef]],
        "schemaVersion": NotRequired[str],
    },
)
UpdateComponentDataTypeDef = TypedDict(
    "UpdateComponentDataTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "sourceId": NotRequired[str],
        "componentType": NotRequired[str],
        "properties": NotRequired[Mapping[str, ComponentPropertyUnionTypeDef]],
        "children": NotRequired[Sequence[ComponentChildUnionTypeDef]],
        "variants": NotRequired[Sequence[ComponentVariantUnionTypeDef]],
        "overrides": NotRequired[Mapping[str, Mapping[str, str]]],
        "bindingProperties": NotRequired[Mapping[str, ComponentBindingPropertiesValueUnionTypeDef]],
        "collectionProperties": NotRequired[Mapping[str, ComponentDataConfigurationUnionTypeDef]],
        "events": NotRequired[Mapping[str, ComponentEventUnionTypeDef]],
        "schemaVersion": NotRequired[str],
    },
)
CreateFormRequestRequestTypeDef = TypedDict(
    "CreateFormRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "formToCreate": CreateFormDataTypeDef,
        "clientToken": NotRequired[str],
    },
)
UpdateFormRequestRequestTypeDef = TypedDict(
    "UpdateFormRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "updatedForm": UpdateFormDataTypeDef,
        "clientToken": NotRequired[str],
    },
)
CreateComponentRequestRequestTypeDef = TypedDict(
    "CreateComponentRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "componentToCreate": CreateComponentDataTypeDef,
        "clientToken": NotRequired[str],
    },
)
UpdateComponentRequestRequestTypeDef = TypedDict(
    "UpdateComponentRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "updatedComponent": UpdateComponentDataTypeDef,
        "clientToken": NotRequired[str],
    },
)
