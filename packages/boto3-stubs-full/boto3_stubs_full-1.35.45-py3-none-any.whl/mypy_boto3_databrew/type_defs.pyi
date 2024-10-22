"""
Type annotations for databrew service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_databrew/type_defs/)

Usage::

    ```python
    from mypy_boto3_databrew.type_defs import AllowedStatisticsOutputTypeDef

    data: AllowedStatisticsOutputTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AnalyticsModeType,
    CompressionFormatType,
    EncryptionModeType,
    InputFormatType,
    JobRunStateType,
    JobTypeType,
    LogSubscriptionType,
    OrderType,
    OutputFormatType,
    ParameterTypeType,
    SampleModeType,
    SampleTypeType,
    SessionStatusType,
    SourceType,
    ThresholdTypeType,
    ThresholdUnitType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AllowedStatisticsOutputTypeDef",
    "AllowedStatisticsTypeDef",
    "BatchDeleteRecipeVersionRequestRequestTypeDef",
    "RecipeVersionErrorDetailTypeDef",
    "ResponseMetadataTypeDef",
    "ColumnSelectorTypeDef",
    "ConditionExpressionTypeDef",
    "JobSampleTypeDef",
    "S3LocationTypeDef",
    "ValidationConfigurationTypeDef",
    "SampleTypeDef",
    "RecipeReferenceTypeDef",
    "CreateScheduleRequestRequestTypeDef",
    "CsvOptionsTypeDef",
    "CsvOutputOptionsTypeDef",
    "DatetimeOptionsTypeDef",
    "FilterExpressionOutputTypeDef",
    "DeleteDatasetRequestRequestTypeDef",
    "DeleteJobRequestRequestTypeDef",
    "DeleteProjectRequestRequestTypeDef",
    "DeleteRecipeVersionRequestRequestTypeDef",
    "DeleteRulesetRequestRequestTypeDef",
    "DeleteScheduleRequestRequestTypeDef",
    "DescribeDatasetRequestRequestTypeDef",
    "DescribeJobRequestRequestTypeDef",
    "DescribeJobRunRequestRequestTypeDef",
    "DescribeProjectRequestRequestTypeDef",
    "DescribeRecipeRequestRequestTypeDef",
    "DescribeRulesetRequestRequestTypeDef",
    "DescribeScheduleRequestRequestTypeDef",
    "ExcelOptionsOutputTypeDef",
    "ExcelOptionsTypeDef",
    "FilesLimitTypeDef",
    "FilterExpressionTypeDef",
    "JsonOptionsTypeDef",
    "MetadataTypeDef",
    "PaginatorConfigTypeDef",
    "ListDatasetsRequestRequestTypeDef",
    "ListJobRunsRequestRequestTypeDef",
    "ListJobsRequestRequestTypeDef",
    "ListProjectsRequestRequestTypeDef",
    "ListRecipeVersionsRequestRequestTypeDef",
    "ListRecipesRequestRequestTypeDef",
    "ListRulesetsRequestRequestTypeDef",
    "RulesetItemTypeDef",
    "ListSchedulesRequestRequestTypeDef",
    "ScheduleTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "PublishRecipeRequestRequestTypeDef",
    "RecipeActionOutputTypeDef",
    "RecipeActionTypeDef",
    "ThresholdTypeDef",
    "ViewFrameTypeDef",
    "StartJobRunRequestRequestTypeDef",
    "StartProjectSessionRequestRequestTypeDef",
    "StatisticOverrideOutputTypeDef",
    "StatisticOverrideTypeDef",
    "StopJobRunRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateScheduleRequestRequestTypeDef",
    "EntityDetectorConfigurationOutputTypeDef",
    "AllowedStatisticsUnionTypeDef",
    "BatchDeleteRecipeVersionResponseTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateProfileJobResponseTypeDef",
    "CreateProjectResponseTypeDef",
    "CreateRecipeJobResponseTypeDef",
    "CreateRecipeResponseTypeDef",
    "CreateRulesetResponseTypeDef",
    "CreateScheduleResponseTypeDef",
    "DeleteDatasetResponseTypeDef",
    "DeleteJobResponseTypeDef",
    "DeleteProjectResponseTypeDef",
    "DeleteRecipeVersionResponseTypeDef",
    "DeleteRulesetResponseTypeDef",
    "DeleteScheduleResponseTypeDef",
    "DescribeScheduleResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PublishRecipeResponseTypeDef",
    "SendProjectSessionActionResponseTypeDef",
    "StartJobRunResponseTypeDef",
    "StartProjectSessionResponseTypeDef",
    "StopJobRunResponseTypeDef",
    "UpdateDatasetResponseTypeDef",
    "UpdateProfileJobResponseTypeDef",
    "UpdateProjectResponseTypeDef",
    "UpdateRecipeJobResponseTypeDef",
    "UpdateRecipeResponseTypeDef",
    "UpdateRulesetResponseTypeDef",
    "UpdateScheduleResponseTypeDef",
    "DataCatalogInputDefinitionTypeDef",
    "DatabaseInputDefinitionTypeDef",
    "DatabaseTableOutputOptionsTypeDef",
    "S3TableOutputOptionsTypeDef",
    "CreateProjectRequestRequestTypeDef",
    "DescribeProjectResponseTypeDef",
    "ProjectTypeDef",
    "UpdateProjectRequestRequestTypeDef",
    "OutputFormatOptionsTypeDef",
    "DatasetParameterOutputTypeDef",
    "ExcelOptionsUnionTypeDef",
    "FilterExpressionUnionTypeDef",
    "FormatOptionsOutputTypeDef",
    "ListDatasetsRequestListDatasetsPaginateTypeDef",
    "ListJobRunsRequestListJobRunsPaginateTypeDef",
    "ListJobsRequestListJobsPaginateTypeDef",
    "ListProjectsRequestListProjectsPaginateTypeDef",
    "ListRecipeVersionsRequestListRecipeVersionsPaginateTypeDef",
    "ListRecipesRequestListRecipesPaginateTypeDef",
    "ListRulesetsRequestListRulesetsPaginateTypeDef",
    "ListSchedulesRequestListSchedulesPaginateTypeDef",
    "ListRulesetsResponseTypeDef",
    "ListSchedulesResponseTypeDef",
    "RecipeStepOutputTypeDef",
    "RecipeActionUnionTypeDef",
    "RuleOutputTypeDef",
    "RuleTypeDef",
    "StatisticsConfigurationOutputTypeDef",
    "StatisticOverrideUnionTypeDef",
    "EntityDetectorConfigurationTypeDef",
    "InputTypeDef",
    "DatabaseOutputTypeDef",
    "DataCatalogOutputTypeDef",
    "ListProjectsResponseTypeDef",
    "ExtraOutputTypeDef",
    "OutputTypeDef",
    "PathOptionsOutputTypeDef",
    "FormatOptionsTypeDef",
    "DatasetParameterTypeDef",
    "DescribeRecipeResponseTypeDef",
    "RecipeTypeDef",
    "RecipeStepTypeDef",
    "DescribeRulesetResponseTypeDef",
    "RuleUnionTypeDef",
    "UpdateRulesetRequestRequestTypeDef",
    "ColumnStatisticsConfigurationOutputTypeDef",
    "StatisticsConfigurationTypeDef",
    "EntityDetectorConfigurationUnionTypeDef",
    "JobRunTypeDef",
    "JobTypeDef",
    "UnionTypeDef",
    "UpdateRecipeJobRequestRequestTypeDef",
    "DatasetTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DatasetParameterUnionTypeDef",
    "ListRecipeVersionsResponseTypeDef",
    "ListRecipesResponseTypeDef",
    "RecipeStepUnionTypeDef",
    "SendProjectSessionActionRequestRequestTypeDef",
    "UpdateRecipeRequestRequestTypeDef",
    "CreateRulesetRequestRequestTypeDef",
    "ProfileConfigurationOutputTypeDef",
    "StatisticsConfigurationUnionTypeDef",
    "ListJobRunsResponseTypeDef",
    "ListJobsResponseTypeDef",
    "CreateRecipeJobRequestRequestTypeDef",
    "ListDatasetsResponseTypeDef",
    "PathOptionsTypeDef",
    "CreateRecipeRequestRequestTypeDef",
    "DescribeJobResponseTypeDef",
    "DescribeJobRunResponseTypeDef",
    "ColumnStatisticsConfigurationTypeDef",
    "CreateDatasetRequestRequestTypeDef",
    "UpdateDatasetRequestRequestTypeDef",
    "ColumnStatisticsConfigurationUnionTypeDef",
    "ProfileConfigurationTypeDef",
    "CreateProfileJobRequestRequestTypeDef",
    "UpdateProfileJobRequestRequestTypeDef",
)

AllowedStatisticsOutputTypeDef = TypedDict(
    "AllowedStatisticsOutputTypeDef",
    {
        "Statistics": List[str],
    },
)
AllowedStatisticsTypeDef = TypedDict(
    "AllowedStatisticsTypeDef",
    {
        "Statistics": Sequence[str],
    },
)
BatchDeleteRecipeVersionRequestRequestTypeDef = TypedDict(
    "BatchDeleteRecipeVersionRequestRequestTypeDef",
    {
        "Name": str,
        "RecipeVersions": Sequence[str],
    },
)
RecipeVersionErrorDetailTypeDef = TypedDict(
    "RecipeVersionErrorDetailTypeDef",
    {
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
        "RecipeVersion": NotRequired[str],
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
ColumnSelectorTypeDef = TypedDict(
    "ColumnSelectorTypeDef",
    {
        "Regex": NotRequired[str],
        "Name": NotRequired[str],
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
JobSampleTypeDef = TypedDict(
    "JobSampleTypeDef",
    {
        "Mode": NotRequired[SampleModeType],
        "Size": NotRequired[int],
    },
)
S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "Bucket": str,
        "Key": NotRequired[str],
        "BucketOwner": NotRequired[str],
    },
)
ValidationConfigurationTypeDef = TypedDict(
    "ValidationConfigurationTypeDef",
    {
        "RulesetArn": str,
        "ValidationMode": NotRequired[Literal["CHECK_ALL"]],
    },
)
SampleTypeDef = TypedDict(
    "SampleTypeDef",
    {
        "Type": SampleTypeType,
        "Size": NotRequired[int],
    },
)
RecipeReferenceTypeDef = TypedDict(
    "RecipeReferenceTypeDef",
    {
        "Name": str,
        "RecipeVersion": NotRequired[str],
    },
)
CreateScheduleRequestRequestTypeDef = TypedDict(
    "CreateScheduleRequestRequestTypeDef",
    {
        "CronExpression": str,
        "Name": str,
        "JobNames": NotRequired[Sequence[str]],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CsvOptionsTypeDef = TypedDict(
    "CsvOptionsTypeDef",
    {
        "Delimiter": NotRequired[str],
        "HeaderRow": NotRequired[bool],
    },
)
CsvOutputOptionsTypeDef = TypedDict(
    "CsvOutputOptionsTypeDef",
    {
        "Delimiter": NotRequired[str],
    },
)
DatetimeOptionsTypeDef = TypedDict(
    "DatetimeOptionsTypeDef",
    {
        "Format": str,
        "TimezoneOffset": NotRequired[str],
        "LocaleCode": NotRequired[str],
    },
)
FilterExpressionOutputTypeDef = TypedDict(
    "FilterExpressionOutputTypeDef",
    {
        "Expression": str,
        "ValuesMap": Dict[str, str],
    },
)
DeleteDatasetRequestRequestTypeDef = TypedDict(
    "DeleteDatasetRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteJobRequestRequestTypeDef = TypedDict(
    "DeleteJobRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteProjectRequestRequestTypeDef = TypedDict(
    "DeleteProjectRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteRecipeVersionRequestRequestTypeDef = TypedDict(
    "DeleteRecipeVersionRequestRequestTypeDef",
    {
        "Name": str,
        "RecipeVersion": str,
    },
)
DeleteRulesetRequestRequestTypeDef = TypedDict(
    "DeleteRulesetRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DeleteScheduleRequestRequestTypeDef = TypedDict(
    "DeleteScheduleRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DescribeDatasetRequestRequestTypeDef = TypedDict(
    "DescribeDatasetRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DescribeJobRequestRequestTypeDef = TypedDict(
    "DescribeJobRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DescribeJobRunRequestRequestTypeDef = TypedDict(
    "DescribeJobRunRequestRequestTypeDef",
    {
        "Name": str,
        "RunId": str,
    },
)
DescribeProjectRequestRequestTypeDef = TypedDict(
    "DescribeProjectRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DescribeRecipeRequestRequestTypeDef = TypedDict(
    "DescribeRecipeRequestRequestTypeDef",
    {
        "Name": str,
        "RecipeVersion": NotRequired[str],
    },
)
DescribeRulesetRequestRequestTypeDef = TypedDict(
    "DescribeRulesetRequestRequestTypeDef",
    {
        "Name": str,
    },
)
DescribeScheduleRequestRequestTypeDef = TypedDict(
    "DescribeScheduleRequestRequestTypeDef",
    {
        "Name": str,
    },
)
ExcelOptionsOutputTypeDef = TypedDict(
    "ExcelOptionsOutputTypeDef",
    {
        "SheetNames": NotRequired[List[str]],
        "SheetIndexes": NotRequired[List[int]],
        "HeaderRow": NotRequired[bool],
    },
)
ExcelOptionsTypeDef = TypedDict(
    "ExcelOptionsTypeDef",
    {
        "SheetNames": NotRequired[Sequence[str]],
        "SheetIndexes": NotRequired[Sequence[int]],
        "HeaderRow": NotRequired[bool],
    },
)
FilesLimitTypeDef = TypedDict(
    "FilesLimitTypeDef",
    {
        "MaxFiles": int,
        "OrderedBy": NotRequired[Literal["LAST_MODIFIED_DATE"]],
        "Order": NotRequired[OrderType],
    },
)
FilterExpressionTypeDef = TypedDict(
    "FilterExpressionTypeDef",
    {
        "Expression": str,
        "ValuesMap": Mapping[str, str],
    },
)
JsonOptionsTypeDef = TypedDict(
    "JsonOptionsTypeDef",
    {
        "MultiLine": NotRequired[bool],
    },
)
MetadataTypeDef = TypedDict(
    "MetadataTypeDef",
    {
        "SourceArn": NotRequired[str],
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
ListDatasetsRequestRequestTypeDef = TypedDict(
    "ListDatasetsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListJobRunsRequestRequestTypeDef = TypedDict(
    "ListJobRunsRequestRequestTypeDef",
    {
        "Name": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListJobsRequestRequestTypeDef = TypedDict(
    "ListJobsRequestRequestTypeDef",
    {
        "DatasetName": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ProjectName": NotRequired[str],
    },
)
ListProjectsRequestRequestTypeDef = TypedDict(
    "ListProjectsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListRecipeVersionsRequestRequestTypeDef = TypedDict(
    "ListRecipeVersionsRequestRequestTypeDef",
    {
        "Name": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListRecipesRequestRequestTypeDef = TypedDict(
    "ListRecipesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "RecipeVersion": NotRequired[str],
    },
)
ListRulesetsRequestRequestTypeDef = TypedDict(
    "ListRulesetsRequestRequestTypeDef",
    {
        "TargetArn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
RulesetItemTypeDef = TypedDict(
    "RulesetItemTypeDef",
    {
        "Name": str,
        "TargetArn": str,
        "AccountId": NotRequired[str],
        "CreatedBy": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "Description": NotRequired[str],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "ResourceArn": NotRequired[str],
        "RuleCount": NotRequired[int],
        "Tags": NotRequired[Dict[str, str]],
    },
)
ListSchedulesRequestRequestTypeDef = TypedDict(
    "ListSchedulesRequestRequestTypeDef",
    {
        "JobName": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ScheduleTypeDef = TypedDict(
    "ScheduleTypeDef",
    {
        "Name": str,
        "AccountId": NotRequired[str],
        "CreatedBy": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "JobNames": NotRequired[List[str]],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "ResourceArn": NotRequired[str],
        "CronExpression": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
PublishRecipeRequestRequestTypeDef = TypedDict(
    "PublishRecipeRequestRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
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
ThresholdTypeDef = TypedDict(
    "ThresholdTypeDef",
    {
        "Value": float,
        "Type": NotRequired[ThresholdTypeType],
        "Unit": NotRequired[ThresholdUnitType],
    },
)
ViewFrameTypeDef = TypedDict(
    "ViewFrameTypeDef",
    {
        "StartColumnIndex": int,
        "ColumnRange": NotRequired[int],
        "HiddenColumns": NotRequired[Sequence[str]],
        "StartRowIndex": NotRequired[int],
        "RowRange": NotRequired[int],
        "Analytics": NotRequired[AnalyticsModeType],
    },
)
StartJobRunRequestRequestTypeDef = TypedDict(
    "StartJobRunRequestRequestTypeDef",
    {
        "Name": str,
    },
)
StartProjectSessionRequestRequestTypeDef = TypedDict(
    "StartProjectSessionRequestRequestTypeDef",
    {
        "Name": str,
        "AssumeControl": NotRequired[bool],
    },
)
StatisticOverrideOutputTypeDef = TypedDict(
    "StatisticOverrideOutputTypeDef",
    {
        "Statistic": str,
        "Parameters": Dict[str, str],
    },
)
StatisticOverrideTypeDef = TypedDict(
    "StatisticOverrideTypeDef",
    {
        "Statistic": str,
        "Parameters": Mapping[str, str],
    },
)
StopJobRunRequestRequestTypeDef = TypedDict(
    "StopJobRunRequestRequestTypeDef",
    {
        "Name": str,
        "RunId": str,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateScheduleRequestRequestTypeDef = TypedDict(
    "UpdateScheduleRequestRequestTypeDef",
    {
        "CronExpression": str,
        "Name": str,
        "JobNames": NotRequired[Sequence[str]],
    },
)
EntityDetectorConfigurationOutputTypeDef = TypedDict(
    "EntityDetectorConfigurationOutputTypeDef",
    {
        "EntityTypes": List[str],
        "AllowedStatistics": NotRequired[List[AllowedStatisticsOutputTypeDef]],
    },
)
AllowedStatisticsUnionTypeDef = Union[AllowedStatisticsTypeDef, AllowedStatisticsOutputTypeDef]
BatchDeleteRecipeVersionResponseTypeDef = TypedDict(
    "BatchDeleteRecipeVersionResponseTypeDef",
    {
        "Name": str,
        "Errors": List[RecipeVersionErrorDetailTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDatasetResponseTypeDef = TypedDict(
    "CreateDatasetResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProfileJobResponseTypeDef = TypedDict(
    "CreateProfileJobResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProjectResponseTypeDef = TypedDict(
    "CreateProjectResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRecipeJobResponseTypeDef = TypedDict(
    "CreateRecipeJobResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRecipeResponseTypeDef = TypedDict(
    "CreateRecipeResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRulesetResponseTypeDef = TypedDict(
    "CreateRulesetResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateScheduleResponseTypeDef = TypedDict(
    "CreateScheduleResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDatasetResponseTypeDef = TypedDict(
    "DeleteDatasetResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteJobResponseTypeDef = TypedDict(
    "DeleteJobResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteProjectResponseTypeDef = TypedDict(
    "DeleteProjectResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteRecipeVersionResponseTypeDef = TypedDict(
    "DeleteRecipeVersionResponseTypeDef",
    {
        "Name": str,
        "RecipeVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteRulesetResponseTypeDef = TypedDict(
    "DeleteRulesetResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteScheduleResponseTypeDef = TypedDict(
    "DeleteScheduleResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeScheduleResponseTypeDef = TypedDict(
    "DescribeScheduleResponseTypeDef",
    {
        "CreateDate": datetime,
        "CreatedBy": str,
        "JobNames": List[str],
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "ResourceArn": str,
        "CronExpression": str,
        "Tags": Dict[str, str],
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PublishRecipeResponseTypeDef = TypedDict(
    "PublishRecipeResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendProjectSessionActionResponseTypeDef = TypedDict(
    "SendProjectSessionActionResponseTypeDef",
    {
        "Result": str,
        "Name": str,
        "ActionId": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartJobRunResponseTypeDef = TypedDict(
    "StartJobRunResponseTypeDef",
    {
        "RunId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartProjectSessionResponseTypeDef = TypedDict(
    "StartProjectSessionResponseTypeDef",
    {
        "Name": str,
        "ClientSessionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopJobRunResponseTypeDef = TypedDict(
    "StopJobRunResponseTypeDef",
    {
        "RunId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDatasetResponseTypeDef = TypedDict(
    "UpdateDatasetResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateProfileJobResponseTypeDef = TypedDict(
    "UpdateProfileJobResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateProjectResponseTypeDef = TypedDict(
    "UpdateProjectResponseTypeDef",
    {
        "LastModifiedDate": datetime,
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRecipeJobResponseTypeDef = TypedDict(
    "UpdateRecipeJobResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRecipeResponseTypeDef = TypedDict(
    "UpdateRecipeResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRulesetResponseTypeDef = TypedDict(
    "UpdateRulesetResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateScheduleResponseTypeDef = TypedDict(
    "UpdateScheduleResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DataCatalogInputDefinitionTypeDef = TypedDict(
    "DataCatalogInputDefinitionTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "CatalogId": NotRequired[str],
        "TempDirectory": NotRequired[S3LocationTypeDef],
    },
)
DatabaseInputDefinitionTypeDef = TypedDict(
    "DatabaseInputDefinitionTypeDef",
    {
        "GlueConnectionName": str,
        "DatabaseTableName": NotRequired[str],
        "TempDirectory": NotRequired[S3LocationTypeDef],
        "QueryString": NotRequired[str],
    },
)
DatabaseTableOutputOptionsTypeDef = TypedDict(
    "DatabaseTableOutputOptionsTypeDef",
    {
        "TableName": str,
        "TempDirectory": NotRequired[S3LocationTypeDef],
    },
)
S3TableOutputOptionsTypeDef = TypedDict(
    "S3TableOutputOptionsTypeDef",
    {
        "Location": S3LocationTypeDef,
    },
)
CreateProjectRequestRequestTypeDef = TypedDict(
    "CreateProjectRequestRequestTypeDef",
    {
        "DatasetName": str,
        "Name": str,
        "RecipeName": str,
        "RoleArn": str,
        "Sample": NotRequired[SampleTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
DescribeProjectResponseTypeDef = TypedDict(
    "DescribeProjectResponseTypeDef",
    {
        "CreateDate": datetime,
        "CreatedBy": str,
        "DatasetName": str,
        "LastModifiedDate": datetime,
        "LastModifiedBy": str,
        "Name": str,
        "RecipeName": str,
        "ResourceArn": str,
        "Sample": SampleTypeDef,
        "RoleArn": str,
        "Tags": Dict[str, str],
        "SessionStatus": SessionStatusType,
        "OpenedBy": str,
        "OpenDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProjectTypeDef = TypedDict(
    "ProjectTypeDef",
    {
        "Name": str,
        "RecipeName": str,
        "AccountId": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "CreatedBy": NotRequired[str],
        "DatasetName": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "LastModifiedBy": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "Sample": NotRequired[SampleTypeDef],
        "Tags": NotRequired[Dict[str, str]],
        "RoleArn": NotRequired[str],
        "OpenedBy": NotRequired[str],
        "OpenDate": NotRequired[datetime],
    },
)
UpdateProjectRequestRequestTypeDef = TypedDict(
    "UpdateProjectRequestRequestTypeDef",
    {
        "RoleArn": str,
        "Name": str,
        "Sample": NotRequired[SampleTypeDef],
    },
)
OutputFormatOptionsTypeDef = TypedDict(
    "OutputFormatOptionsTypeDef",
    {
        "Csv": NotRequired[CsvOutputOptionsTypeDef],
    },
)
DatasetParameterOutputTypeDef = TypedDict(
    "DatasetParameterOutputTypeDef",
    {
        "Name": str,
        "Type": ParameterTypeType,
        "DatetimeOptions": NotRequired[DatetimeOptionsTypeDef],
        "CreateColumn": NotRequired[bool],
        "Filter": NotRequired[FilterExpressionOutputTypeDef],
    },
)
ExcelOptionsUnionTypeDef = Union[ExcelOptionsTypeDef, ExcelOptionsOutputTypeDef]
FilterExpressionUnionTypeDef = Union[FilterExpressionTypeDef, FilterExpressionOutputTypeDef]
FormatOptionsOutputTypeDef = TypedDict(
    "FormatOptionsOutputTypeDef",
    {
        "Json": NotRequired[JsonOptionsTypeDef],
        "Excel": NotRequired[ExcelOptionsOutputTypeDef],
        "Csv": NotRequired[CsvOptionsTypeDef],
    },
)
ListDatasetsRequestListDatasetsPaginateTypeDef = TypedDict(
    "ListDatasetsRequestListDatasetsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListJobRunsRequestListJobRunsPaginateTypeDef = TypedDict(
    "ListJobRunsRequestListJobRunsPaginateTypeDef",
    {
        "Name": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListJobsRequestListJobsPaginateTypeDef = TypedDict(
    "ListJobsRequestListJobsPaginateTypeDef",
    {
        "DatasetName": NotRequired[str],
        "ProjectName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProjectsRequestListProjectsPaginateTypeDef = TypedDict(
    "ListProjectsRequestListProjectsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRecipeVersionsRequestListRecipeVersionsPaginateTypeDef = TypedDict(
    "ListRecipeVersionsRequestListRecipeVersionsPaginateTypeDef",
    {
        "Name": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRecipesRequestListRecipesPaginateTypeDef = TypedDict(
    "ListRecipesRequestListRecipesPaginateTypeDef",
    {
        "RecipeVersion": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRulesetsRequestListRulesetsPaginateTypeDef = TypedDict(
    "ListRulesetsRequestListRulesetsPaginateTypeDef",
    {
        "TargetArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSchedulesRequestListSchedulesPaginateTypeDef = TypedDict(
    "ListSchedulesRequestListSchedulesPaginateTypeDef",
    {
        "JobName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRulesetsResponseTypeDef = TypedDict(
    "ListRulesetsResponseTypeDef",
    {
        "Rulesets": List[RulesetItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListSchedulesResponseTypeDef = TypedDict(
    "ListSchedulesResponseTypeDef",
    {
        "Schedules": List[ScheduleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
RecipeStepOutputTypeDef = TypedDict(
    "RecipeStepOutputTypeDef",
    {
        "Action": RecipeActionOutputTypeDef,
        "ConditionExpressions": NotRequired[List[ConditionExpressionTypeDef]],
    },
)
RecipeActionUnionTypeDef = Union[RecipeActionTypeDef, RecipeActionOutputTypeDef]
RuleOutputTypeDef = TypedDict(
    "RuleOutputTypeDef",
    {
        "Name": str,
        "CheckExpression": str,
        "Disabled": NotRequired[bool],
        "SubstitutionMap": NotRequired[Dict[str, str]],
        "Threshold": NotRequired[ThresholdTypeDef],
        "ColumnSelectors": NotRequired[List[ColumnSelectorTypeDef]],
    },
)
RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "Name": str,
        "CheckExpression": str,
        "Disabled": NotRequired[bool],
        "SubstitutionMap": NotRequired[Mapping[str, str]],
        "Threshold": NotRequired[ThresholdTypeDef],
        "ColumnSelectors": NotRequired[Sequence[ColumnSelectorTypeDef]],
    },
)
StatisticsConfigurationOutputTypeDef = TypedDict(
    "StatisticsConfigurationOutputTypeDef",
    {
        "IncludedStatistics": NotRequired[List[str]],
        "Overrides": NotRequired[List[StatisticOverrideOutputTypeDef]],
    },
)
StatisticOverrideUnionTypeDef = Union[StatisticOverrideTypeDef, StatisticOverrideOutputTypeDef]
EntityDetectorConfigurationTypeDef = TypedDict(
    "EntityDetectorConfigurationTypeDef",
    {
        "EntityTypes": Sequence[str],
        "AllowedStatistics": NotRequired[Sequence[AllowedStatisticsUnionTypeDef]],
    },
)
InputTypeDef = TypedDict(
    "InputTypeDef",
    {
        "S3InputDefinition": NotRequired[S3LocationTypeDef],
        "DataCatalogInputDefinition": NotRequired[DataCatalogInputDefinitionTypeDef],
        "DatabaseInputDefinition": NotRequired[DatabaseInputDefinitionTypeDef],
        "Metadata": NotRequired[MetadataTypeDef],
    },
)
DatabaseOutputTypeDef = TypedDict(
    "DatabaseOutputTypeDef",
    {
        "GlueConnectionName": str,
        "DatabaseOptions": DatabaseTableOutputOptionsTypeDef,
        "DatabaseOutputMode": NotRequired[Literal["NEW_TABLE"]],
    },
)
DataCatalogOutputTypeDef = TypedDict(
    "DataCatalogOutputTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "CatalogId": NotRequired[str],
        "S3Options": NotRequired[S3TableOutputOptionsTypeDef],
        "DatabaseOptions": NotRequired[DatabaseTableOutputOptionsTypeDef],
        "Overwrite": NotRequired[bool],
    },
)
ListProjectsResponseTypeDef = TypedDict(
    "ListProjectsResponseTypeDef",
    {
        "Projects": List[ProjectTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ExtraOutputTypeDef = TypedDict(
    "ExtraOutputTypeDef",
    {
        "Location": S3LocationTypeDef,
        "CompressionFormat": NotRequired[CompressionFormatType],
        "Format": NotRequired[OutputFormatType],
        "PartitionColumns": NotRequired[List[str]],
        "Overwrite": NotRequired[bool],
        "FormatOptions": NotRequired[OutputFormatOptionsTypeDef],
        "MaxOutputFiles": NotRequired[int],
    },
)
OutputTypeDef = TypedDict(
    "OutputTypeDef",
    {
        "Location": S3LocationTypeDef,
        "CompressionFormat": NotRequired[CompressionFormatType],
        "Format": NotRequired[OutputFormatType],
        "PartitionColumns": NotRequired[Sequence[str]],
        "Overwrite": NotRequired[bool],
        "FormatOptions": NotRequired[OutputFormatOptionsTypeDef],
        "MaxOutputFiles": NotRequired[int],
    },
)
PathOptionsOutputTypeDef = TypedDict(
    "PathOptionsOutputTypeDef",
    {
        "LastModifiedDateCondition": NotRequired[FilterExpressionOutputTypeDef],
        "FilesLimit": NotRequired[FilesLimitTypeDef],
        "Parameters": NotRequired[Dict[str, DatasetParameterOutputTypeDef]],
    },
)
FormatOptionsTypeDef = TypedDict(
    "FormatOptionsTypeDef",
    {
        "Json": NotRequired[JsonOptionsTypeDef],
        "Excel": NotRequired[ExcelOptionsUnionTypeDef],
        "Csv": NotRequired[CsvOptionsTypeDef],
    },
)
DatasetParameterTypeDef = TypedDict(
    "DatasetParameterTypeDef",
    {
        "Name": str,
        "Type": ParameterTypeType,
        "DatetimeOptions": NotRequired[DatetimeOptionsTypeDef],
        "CreateColumn": NotRequired[bool],
        "Filter": NotRequired[FilterExpressionUnionTypeDef],
    },
)
DescribeRecipeResponseTypeDef = TypedDict(
    "DescribeRecipeResponseTypeDef",
    {
        "CreatedBy": str,
        "CreateDate": datetime,
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "ProjectName": str,
        "PublishedBy": str,
        "PublishedDate": datetime,
        "Description": str,
        "Name": str,
        "Steps": List[RecipeStepOutputTypeDef],
        "Tags": Dict[str, str],
        "ResourceArn": str,
        "RecipeVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RecipeTypeDef = TypedDict(
    "RecipeTypeDef",
    {
        "Name": str,
        "CreatedBy": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "ProjectName": NotRequired[str],
        "PublishedBy": NotRequired[str],
        "PublishedDate": NotRequired[datetime],
        "Description": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "Steps": NotRequired[List[RecipeStepOutputTypeDef]],
        "Tags": NotRequired[Dict[str, str]],
        "RecipeVersion": NotRequired[str],
    },
)
RecipeStepTypeDef = TypedDict(
    "RecipeStepTypeDef",
    {
        "Action": RecipeActionUnionTypeDef,
        "ConditionExpressions": NotRequired[Sequence[ConditionExpressionTypeDef]],
    },
)
DescribeRulesetResponseTypeDef = TypedDict(
    "DescribeRulesetResponseTypeDef",
    {
        "Name": str,
        "Description": str,
        "TargetArn": str,
        "Rules": List[RuleOutputTypeDef],
        "CreateDate": datetime,
        "CreatedBy": str,
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "ResourceArn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RuleUnionTypeDef = Union[RuleTypeDef, RuleOutputTypeDef]
UpdateRulesetRequestRequestTypeDef = TypedDict(
    "UpdateRulesetRequestRequestTypeDef",
    {
        "Name": str,
        "Rules": Sequence[RuleTypeDef],
        "Description": NotRequired[str],
    },
)
ColumnStatisticsConfigurationOutputTypeDef = TypedDict(
    "ColumnStatisticsConfigurationOutputTypeDef",
    {
        "Statistics": StatisticsConfigurationOutputTypeDef,
        "Selectors": NotRequired[List[ColumnSelectorTypeDef]],
    },
)
StatisticsConfigurationTypeDef = TypedDict(
    "StatisticsConfigurationTypeDef",
    {
        "IncludedStatistics": NotRequired[Sequence[str]],
        "Overrides": NotRequired[Sequence[StatisticOverrideUnionTypeDef]],
    },
)
EntityDetectorConfigurationUnionTypeDef = Union[
    EntityDetectorConfigurationTypeDef, EntityDetectorConfigurationOutputTypeDef
]
JobRunTypeDef = TypedDict(
    "JobRunTypeDef",
    {
        "Attempt": NotRequired[int],
        "CompletedOn": NotRequired[datetime],
        "DatasetName": NotRequired[str],
        "ErrorMessage": NotRequired[str],
        "ExecutionTime": NotRequired[int],
        "JobName": NotRequired[str],
        "RunId": NotRequired[str],
        "State": NotRequired[JobRunStateType],
        "LogSubscription": NotRequired[LogSubscriptionType],
        "LogGroupName": NotRequired[str],
        "Outputs": NotRequired[List[ExtraOutputTypeDef]],
        "DataCatalogOutputs": NotRequired[List[DataCatalogOutputTypeDef]],
        "DatabaseOutputs": NotRequired[List[DatabaseOutputTypeDef]],
        "RecipeReference": NotRequired[RecipeReferenceTypeDef],
        "StartedBy": NotRequired[str],
        "StartedOn": NotRequired[datetime],
        "JobSample": NotRequired[JobSampleTypeDef],
        "ValidationConfigurations": NotRequired[List[ValidationConfigurationTypeDef]],
    },
)
JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "Name": str,
        "AccountId": NotRequired[str],
        "CreatedBy": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "DatasetName": NotRequired[str],
        "EncryptionKeyArn": NotRequired[str],
        "EncryptionMode": NotRequired[EncryptionModeType],
        "Type": NotRequired[JobTypeType],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "LogSubscription": NotRequired[LogSubscriptionType],
        "MaxCapacity": NotRequired[int],
        "MaxRetries": NotRequired[int],
        "Outputs": NotRequired[List[ExtraOutputTypeDef]],
        "DataCatalogOutputs": NotRequired[List[DataCatalogOutputTypeDef]],
        "DatabaseOutputs": NotRequired[List[DatabaseOutputTypeDef]],
        "ProjectName": NotRequired[str],
        "RecipeReference": NotRequired[RecipeReferenceTypeDef],
        "ResourceArn": NotRequired[str],
        "RoleArn": NotRequired[str],
        "Timeout": NotRequired[int],
        "Tags": NotRequired[Dict[str, str]],
        "JobSample": NotRequired[JobSampleTypeDef],
        "ValidationConfigurations": NotRequired[List[ValidationConfigurationTypeDef]],
    },
)
UnionTypeDef = Union[OutputTypeDef, ExtraOutputTypeDef]
UpdateRecipeJobRequestRequestTypeDef = TypedDict(
    "UpdateRecipeJobRequestRequestTypeDef",
    {
        "Name": str,
        "RoleArn": str,
        "EncryptionKeyArn": NotRequired[str],
        "EncryptionMode": NotRequired[EncryptionModeType],
        "LogSubscription": NotRequired[LogSubscriptionType],
        "MaxCapacity": NotRequired[int],
        "MaxRetries": NotRequired[int],
        "Outputs": NotRequired[Sequence[OutputTypeDef]],
        "DataCatalogOutputs": NotRequired[Sequence[DataCatalogOutputTypeDef]],
        "DatabaseOutputs": NotRequired[Sequence[DatabaseOutputTypeDef]],
        "Timeout": NotRequired[int],
    },
)
DatasetTypeDef = TypedDict(
    "DatasetTypeDef",
    {
        "Name": str,
        "Input": InputTypeDef,
        "AccountId": NotRequired[str],
        "CreatedBy": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "Format": NotRequired[InputFormatType],
        "FormatOptions": NotRequired[FormatOptionsOutputTypeDef],
        "LastModifiedDate": NotRequired[datetime],
        "LastModifiedBy": NotRequired[str],
        "Source": NotRequired[SourceType],
        "PathOptions": NotRequired[PathOptionsOutputTypeDef],
        "Tags": NotRequired[Dict[str, str]],
        "ResourceArn": NotRequired[str],
    },
)
DescribeDatasetResponseTypeDef = TypedDict(
    "DescribeDatasetResponseTypeDef",
    {
        "CreatedBy": str,
        "CreateDate": datetime,
        "Name": str,
        "Format": InputFormatType,
        "FormatOptions": FormatOptionsOutputTypeDef,
        "Input": InputTypeDef,
        "LastModifiedDate": datetime,
        "LastModifiedBy": str,
        "Source": SourceType,
        "PathOptions": PathOptionsOutputTypeDef,
        "Tags": Dict[str, str],
        "ResourceArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DatasetParameterUnionTypeDef = Union[DatasetParameterTypeDef, DatasetParameterOutputTypeDef]
ListRecipeVersionsResponseTypeDef = TypedDict(
    "ListRecipeVersionsResponseTypeDef",
    {
        "Recipes": List[RecipeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListRecipesResponseTypeDef = TypedDict(
    "ListRecipesResponseTypeDef",
    {
        "Recipes": List[RecipeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
RecipeStepUnionTypeDef = Union[RecipeStepTypeDef, RecipeStepOutputTypeDef]
SendProjectSessionActionRequestRequestTypeDef = TypedDict(
    "SendProjectSessionActionRequestRequestTypeDef",
    {
        "Name": str,
        "Preview": NotRequired[bool],
        "RecipeStep": NotRequired[RecipeStepTypeDef],
        "StepIndex": NotRequired[int],
        "ClientSessionId": NotRequired[str],
        "ViewFrame": NotRequired[ViewFrameTypeDef],
    },
)
UpdateRecipeRequestRequestTypeDef = TypedDict(
    "UpdateRecipeRequestRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "Steps": NotRequired[Sequence[RecipeStepTypeDef]],
    },
)
CreateRulesetRequestRequestTypeDef = TypedDict(
    "CreateRulesetRequestRequestTypeDef",
    {
        "Name": str,
        "TargetArn": str,
        "Rules": Sequence[RuleUnionTypeDef],
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
ProfileConfigurationOutputTypeDef = TypedDict(
    "ProfileConfigurationOutputTypeDef",
    {
        "DatasetStatisticsConfiguration": NotRequired[StatisticsConfigurationOutputTypeDef],
        "ProfileColumns": NotRequired[List[ColumnSelectorTypeDef]],
        "ColumnStatisticsConfigurations": NotRequired[
            List[ColumnStatisticsConfigurationOutputTypeDef]
        ],
        "EntityDetectorConfiguration": NotRequired[EntityDetectorConfigurationOutputTypeDef],
    },
)
StatisticsConfigurationUnionTypeDef = Union[
    StatisticsConfigurationTypeDef, StatisticsConfigurationOutputTypeDef
]
ListJobRunsResponseTypeDef = TypedDict(
    "ListJobRunsResponseTypeDef",
    {
        "JobRuns": List[JobRunTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListJobsResponseTypeDef = TypedDict(
    "ListJobsResponseTypeDef",
    {
        "Jobs": List[JobTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateRecipeJobRequestRequestTypeDef = TypedDict(
    "CreateRecipeJobRequestRequestTypeDef",
    {
        "Name": str,
        "RoleArn": str,
        "DatasetName": NotRequired[str],
        "EncryptionKeyArn": NotRequired[str],
        "EncryptionMode": NotRequired[EncryptionModeType],
        "LogSubscription": NotRequired[LogSubscriptionType],
        "MaxCapacity": NotRequired[int],
        "MaxRetries": NotRequired[int],
        "Outputs": NotRequired[Sequence[UnionTypeDef]],
        "DataCatalogOutputs": NotRequired[Sequence[DataCatalogOutputTypeDef]],
        "DatabaseOutputs": NotRequired[Sequence[DatabaseOutputTypeDef]],
        "ProjectName": NotRequired[str],
        "RecipeReference": NotRequired[RecipeReferenceTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
        "Timeout": NotRequired[int],
    },
)
ListDatasetsResponseTypeDef = TypedDict(
    "ListDatasetsResponseTypeDef",
    {
        "Datasets": List[DatasetTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PathOptionsTypeDef = TypedDict(
    "PathOptionsTypeDef",
    {
        "LastModifiedDateCondition": NotRequired[FilterExpressionUnionTypeDef],
        "FilesLimit": NotRequired[FilesLimitTypeDef],
        "Parameters": NotRequired[Mapping[str, DatasetParameterUnionTypeDef]],
    },
)
CreateRecipeRequestRequestTypeDef = TypedDict(
    "CreateRecipeRequestRequestTypeDef",
    {
        "Name": str,
        "Steps": Sequence[RecipeStepUnionTypeDef],
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
DescribeJobResponseTypeDef = TypedDict(
    "DescribeJobResponseTypeDef",
    {
        "CreateDate": datetime,
        "CreatedBy": str,
        "DatasetName": str,
        "EncryptionKeyArn": str,
        "EncryptionMode": EncryptionModeType,
        "Name": str,
        "Type": JobTypeType,
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "LogSubscription": LogSubscriptionType,
        "MaxCapacity": int,
        "MaxRetries": int,
        "Outputs": List[ExtraOutputTypeDef],
        "DataCatalogOutputs": List[DataCatalogOutputTypeDef],
        "DatabaseOutputs": List[DatabaseOutputTypeDef],
        "ProjectName": str,
        "ProfileConfiguration": ProfileConfigurationOutputTypeDef,
        "ValidationConfigurations": List[ValidationConfigurationTypeDef],
        "RecipeReference": RecipeReferenceTypeDef,
        "ResourceArn": str,
        "RoleArn": str,
        "Tags": Dict[str, str],
        "Timeout": int,
        "JobSample": JobSampleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeJobRunResponseTypeDef = TypedDict(
    "DescribeJobRunResponseTypeDef",
    {
        "Attempt": int,
        "CompletedOn": datetime,
        "DatasetName": str,
        "ErrorMessage": str,
        "ExecutionTime": int,
        "JobName": str,
        "ProfileConfiguration": ProfileConfigurationOutputTypeDef,
        "ValidationConfigurations": List[ValidationConfigurationTypeDef],
        "RunId": str,
        "State": JobRunStateType,
        "LogSubscription": LogSubscriptionType,
        "LogGroupName": str,
        "Outputs": List[ExtraOutputTypeDef],
        "DataCatalogOutputs": List[DataCatalogOutputTypeDef],
        "DatabaseOutputs": List[DatabaseOutputTypeDef],
        "RecipeReference": RecipeReferenceTypeDef,
        "StartedBy": str,
        "StartedOn": datetime,
        "JobSample": JobSampleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ColumnStatisticsConfigurationTypeDef = TypedDict(
    "ColumnStatisticsConfigurationTypeDef",
    {
        "Statistics": StatisticsConfigurationUnionTypeDef,
        "Selectors": NotRequired[Sequence[ColumnSelectorTypeDef]],
    },
)
CreateDatasetRequestRequestTypeDef = TypedDict(
    "CreateDatasetRequestRequestTypeDef",
    {
        "Name": str,
        "Input": InputTypeDef,
        "Format": NotRequired[InputFormatType],
        "FormatOptions": NotRequired[FormatOptionsTypeDef],
        "PathOptions": NotRequired[PathOptionsTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
UpdateDatasetRequestRequestTypeDef = TypedDict(
    "UpdateDatasetRequestRequestTypeDef",
    {
        "Name": str,
        "Input": InputTypeDef,
        "Format": NotRequired[InputFormatType],
        "FormatOptions": NotRequired[FormatOptionsTypeDef],
        "PathOptions": NotRequired[PathOptionsTypeDef],
    },
)
ColumnStatisticsConfigurationUnionTypeDef = Union[
    ColumnStatisticsConfigurationTypeDef, ColumnStatisticsConfigurationOutputTypeDef
]
ProfileConfigurationTypeDef = TypedDict(
    "ProfileConfigurationTypeDef",
    {
        "DatasetStatisticsConfiguration": NotRequired[StatisticsConfigurationUnionTypeDef],
        "ProfileColumns": NotRequired[Sequence[ColumnSelectorTypeDef]],
        "ColumnStatisticsConfigurations": NotRequired[
            Sequence[ColumnStatisticsConfigurationUnionTypeDef]
        ],
        "EntityDetectorConfiguration": NotRequired[EntityDetectorConfigurationUnionTypeDef],
    },
)
CreateProfileJobRequestRequestTypeDef = TypedDict(
    "CreateProfileJobRequestRequestTypeDef",
    {
        "DatasetName": str,
        "Name": str,
        "OutputLocation": S3LocationTypeDef,
        "RoleArn": str,
        "EncryptionKeyArn": NotRequired[str],
        "EncryptionMode": NotRequired[EncryptionModeType],
        "LogSubscription": NotRequired[LogSubscriptionType],
        "MaxCapacity": NotRequired[int],
        "MaxRetries": NotRequired[int],
        "Configuration": NotRequired[ProfileConfigurationTypeDef],
        "ValidationConfigurations": NotRequired[Sequence[ValidationConfigurationTypeDef]],
        "Tags": NotRequired[Mapping[str, str]],
        "Timeout": NotRequired[int],
        "JobSample": NotRequired[JobSampleTypeDef],
    },
)
UpdateProfileJobRequestRequestTypeDef = TypedDict(
    "UpdateProfileJobRequestRequestTypeDef",
    {
        "Name": str,
        "OutputLocation": S3LocationTypeDef,
        "RoleArn": str,
        "Configuration": NotRequired[ProfileConfigurationTypeDef],
        "EncryptionKeyArn": NotRequired[str],
        "EncryptionMode": NotRequired[EncryptionModeType],
        "LogSubscription": NotRequired[LogSubscriptionType],
        "MaxCapacity": NotRequired[int],
        "MaxRetries": NotRequired[int],
        "ValidationConfigurations": NotRequired[Sequence[ValidationConfigurationTypeDef]],
        "Timeout": NotRequired[int],
        "JobSample": NotRequired[JobSampleTypeDef],
    },
)
