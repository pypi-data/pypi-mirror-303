"""
Type annotations for quicksight service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_quicksight/type_defs/)

Usage::

    ```python
    from mypy_boto3_quicksight.type_defs import AccountCustomizationTypeDef

    data: AccountCustomizationTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    AggTypeType,
    AnalysisErrorTypeType,
    AnalysisFilterAttributeType,
    ArcThicknessOptionsType,
    ArcThicknessType,
    AssetBundleExportFormatType,
    AssetBundleExportJobDataSourcePropertyToOverrideType,
    AssetBundleExportJobFolderPropertyToOverrideType,
    AssetBundleExportJobStatusType,
    AssetBundleExportJobVPCConnectionPropertyToOverrideType,
    AssetBundleImportFailureActionType,
    AssetBundleImportJobStatusType,
    AssignmentStatusType,
    AuthenticationMethodOptionType,
    AuthorSpecifiedAggregationType,
    AxisBindingType,
    BarChartOrientationType,
    BarsArrangementType,
    BaseMapStyleTypeType,
    BoxPlotFillStyleType,
    CategoricalAggregationFunctionType,
    CategoryFilterFunctionType,
    CategoryFilterMatchOperatorType,
    CategoryFilterTypeType,
    ColorFillTypeType,
    ColumnDataRoleType,
    ColumnDataSubTypeType,
    ColumnDataTypeType,
    ColumnOrderingTypeType,
    ColumnRoleType,
    ColumnTagNameType,
    CommitModeType,
    ComparisonMethodType,
    ComparisonMethodTypeType,
    ConditionalFormattingIconSetTypeType,
    ConstantTypeType,
    ContributionAnalysisDirectionType,
    ContributionAnalysisSortTypeType,
    CrossDatasetTypesType,
    CustomContentImageScalingConfigurationType,
    CustomContentTypeType,
    DashboardBehaviorType,
    DashboardErrorTypeType,
    DashboardFilterAttributeType,
    DashboardUIStateType,
    DataLabelContentType,
    DataLabelOverlapType,
    DataLabelPositionType,
    DataSetFilterAttributeType,
    DataSetImportModeType,
    DatasetParameterValueTypeType,
    DataSourceErrorInfoTypeType,
    DataSourceFilterAttributeType,
    DataSourceTypeType,
    DateAggregationFunctionType,
    DayOfTheWeekType,
    DayOfWeekType,
    DefaultAggregationType,
    DisplayFormatType,
    EditionType,
    EmbeddingIdentityTypeType,
    FileFormatType,
    FilterClassType,
    FilterNullOptionType,
    FilterOperatorType,
    FilterVisualScopeType,
    FolderFilterAttributeType,
    FolderTypeType,
    FontDecorationType,
    FontStyleType,
    FontWeightNameType,
    ForecastComputationSeasonalityType,
    FunnelChartMeasureDataLabelStyleType,
    GeoSpatialDataRoleType,
    GeospatialSelectedPointStyleType,
    HistogramBinTypeType,
    HorizontalTextAlignmentType,
    IconType,
    IdentityTypeType,
    IncludeFolderMembersType,
    IngestionErrorTypeType,
    IngestionRequestSourceType,
    IngestionRequestTypeType,
    IngestionStatusType,
    IngestionTypeType,
    InputColumnDataTypeType,
    JoinTypeType,
    KPISparklineTypeType,
    KPIVisualStandardLayoutTypeType,
    LayoutElementTypeType,
    LegendPositionType,
    LineChartLineStyleType,
    LineChartMarkerShapeType,
    LineChartTypeType,
    LineInterpolationType,
    LookbackWindowSizeUnitType,
    MapZoomModeType,
    MaximumMinimumComputationTypeType,
    MemberTypeType,
    MissingDataTreatmentOptionType,
    NamedEntityAggTypeType,
    NamedFilterAggTypeType,
    NamedFilterTypeType,
    NamespaceErrorTypeType,
    NamespaceStatusType,
    NegativeValueDisplayModeType,
    NetworkInterfaceStatusType,
    NullFilterOptionType,
    NumberScaleType,
    NumericEqualityMatchOperatorType,
    NumericSeparatorSymbolType,
    OtherCategoriesType,
    PanelBorderStyleType,
    PaperOrientationType,
    PaperSizeType,
    ParameterValueTypeType,
    PersonalizationModeType,
    PivotTableConditionalFormattingScopeRoleType,
    PivotTableDataPathTypeType,
    PivotTableFieldCollapseStateType,
    PivotTableMetricPlacementType,
    PivotTableRowsLayoutType,
    PivotTableSubtotalLevelType,
    PrimaryValueDisplayTypeType,
    PropertyRoleType,
    PropertyUsageType,
    PurchaseModeType,
    QueryExecutionModeType,
    RadarChartAxesRangeScaleType,
    RadarChartShapeType,
    ReferenceLineLabelHorizontalPositionType,
    ReferenceLineLabelVerticalPositionType,
    ReferenceLinePatternTypeType,
    ReferenceLineSeriesTypeType,
    ReferenceLineValueLabelRelativePositionType,
    RefreshIntervalType,
    RelativeDateTypeType,
    RelativeFontSizeType,
    ResizeOptionType,
    ResourceStatusType,
    ReviewedAnswerErrorCodeType,
    RoleType,
    RowLevelPermissionFormatVersionType,
    RowLevelPermissionPolicyType,
    SectionPageBreakStatusType,
    SelectedTooltipTypeType,
    SharingModelType,
    SheetContentTypeType,
    SheetControlDateTimePickerTypeType,
    SheetControlListTypeType,
    SheetControlSliderTypeType,
    SimpleNumericalAggregationFunctionType,
    SimpleTotalAggregationFunctionType,
    SmallMultiplesAxisPlacementType,
    SmallMultiplesAxisScaleType,
    SnapshotFileFormatTypeType,
    SnapshotFileSheetSelectionScopeType,
    SnapshotJobStatusType,
    SortDirectionType,
    SpecialValueType,
    StarburstProductTypeType,
    StatusType,
    StyledCellTypeType,
    TableBorderStyleType,
    TableCellImageScalingConfigurationType,
    TableOrientationType,
    TableTotalsPlacementType,
    TableTotalsScrollStatusType,
    TemplateErrorTypeType,
    TextQualifierType,
    TextWrapType,
    ThemeTypeType,
    TimeGranularityType,
    TooltipTargetType,
    TooltipTitleTypeType,
    TopBottomComputationTypeType,
    TopBottomSortOrderType,
    TopicIRFilterFunctionType,
    TopicIRFilterTypeType,
    TopicNumericSeparatorSymbolType,
    TopicRefreshStatusType,
    TopicRelativeDateFilterFunctionType,
    TopicScheduleTypeType,
    TopicSortDirectionType,
    TopicTimeGranularityType,
    TopicUserExperienceVersionType,
    UndefinedSpecifiedValueTypeType,
    URLTargetConfigurationType,
    UserRoleType,
    ValidationStrategyModeType,
    ValueWhenUnsetOptionType,
    VerticalTextAlignmentType,
    VisibilityType,
    VisualCustomActionTriggerType,
    VisualRoleType,
    VPCConnectionAvailabilityStatusType,
    VPCConnectionResourceStatusType,
    WidgetStatusType,
    WordCloudCloudLayoutType,
    WordCloudWordCasingType,
    WordCloudWordOrientationType,
    WordCloudWordPaddingType,
    WordCloudWordScalingType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AccountCustomizationTypeDef",
    "AccountInfoTypeDef",
    "AccountSettingsTypeDef",
    "ActiveIAMPolicyAssignmentTypeDef",
    "AdHocFilteringOptionTypeDef",
    "AggFunctionOutputTypeDef",
    "AggFunctionTypeDef",
    "AttributeAggregationFunctionTypeDef",
    "AggregationPartitionByTypeDef",
    "ColumnIdentifierTypeDef",
    "AmazonElasticsearchParametersTypeDef",
    "AmazonOpenSearchParametersTypeDef",
    "AssetOptionsTypeDef",
    "CalculatedFieldTypeDef",
    "DataSetIdentifierDeclarationTypeDef",
    "QueryExecutionOptionsTypeDef",
    "EntityTypeDef",
    "AnalysisSearchFilterTypeDef",
    "DataSetReferenceTypeDef",
    "AnalysisSummaryTypeDef",
    "SheetTypeDef",
    "AnchorDateConfigurationTypeDef",
    "AnchorTypeDef",
    "SharedViewConfigurationsTypeDef",
    "DashboardVisualIdTypeDef",
    "AnonymousUserGenerativeQnAEmbeddingConfigurationTypeDef",
    "AnonymousUserQSearchBarEmbeddingConfigurationTypeDef",
    "ArcAxisDisplayRangeTypeDef",
    "ArcConfigurationTypeDef",
    "ArcOptionsTypeDef",
    "AssetBundleExportJobAnalysisOverridePropertiesOutputTypeDef",
    "AssetBundleExportJobDashboardOverridePropertiesOutputTypeDef",
    "AssetBundleExportJobDataSetOverridePropertiesOutputTypeDef",
    "AssetBundleExportJobDataSourceOverridePropertiesOutputTypeDef",
    "AssetBundleExportJobFolderOverridePropertiesOutputTypeDef",
    "AssetBundleExportJobRefreshScheduleOverridePropertiesOutputTypeDef",
    "AssetBundleExportJobResourceIdOverrideConfigurationTypeDef",
    "AssetBundleExportJobThemeOverridePropertiesOutputTypeDef",
    "AssetBundleExportJobVPCConnectionOverridePropertiesOutputTypeDef",
    "AssetBundleExportJobAnalysisOverridePropertiesTypeDef",
    "AssetBundleExportJobDashboardOverridePropertiesTypeDef",
    "AssetBundleExportJobDataSetOverridePropertiesTypeDef",
    "AssetBundleExportJobDataSourceOverridePropertiesTypeDef",
    "AssetBundleExportJobErrorTypeDef",
    "AssetBundleExportJobFolderOverridePropertiesTypeDef",
    "AssetBundleExportJobRefreshScheduleOverridePropertiesTypeDef",
    "AssetBundleExportJobSummaryTypeDef",
    "AssetBundleExportJobThemeOverridePropertiesTypeDef",
    "AssetBundleExportJobVPCConnectionOverridePropertiesTypeDef",
    "AssetBundleExportJobValidationStrategyTypeDef",
    "AssetBundleExportJobWarningTypeDef",
    "AssetBundleImportJobAnalysisOverrideParametersTypeDef",
    "AssetBundleResourcePermissionsOutputTypeDef",
    "TagTypeDef",
    "AssetBundleImportJobDashboardOverrideParametersTypeDef",
    "AssetBundleImportJobDataSetOverrideParametersTypeDef",
    "AssetBundleImportJobDataSourceCredentialPairTypeDef",
    "SslPropertiesTypeDef",
    "VpcConnectionPropertiesTypeDef",
    "AssetBundleImportJobErrorTypeDef",
    "AssetBundleImportJobFolderOverrideParametersTypeDef",
    "AssetBundleImportJobRefreshScheduleOverrideParametersOutputTypeDef",
    "AssetBundleImportJobResourceIdOverrideConfigurationTypeDef",
    "AssetBundleImportJobThemeOverrideParametersTypeDef",
    "AssetBundleImportJobVPCConnectionOverrideParametersOutputTypeDef",
    "AssetBundleImportJobOverrideValidationStrategyTypeDef",
    "TimestampTypeDef",
    "AssetBundleImportJobSummaryTypeDef",
    "AssetBundleImportJobVPCConnectionOverrideParametersTypeDef",
    "AssetBundleImportJobWarningTypeDef",
    "AssetBundleImportSourceDescriptionTypeDef",
    "BlobTypeDef",
    "AssetBundleResourcePermissionsTypeDef",
    "AthenaParametersTypeDef",
    "AuroraParametersTypeDef",
    "AuroraPostgreSqlParametersTypeDef",
    "AuthorizedTargetsByServiceTypeDef",
    "AwsIotAnalyticsParametersTypeDef",
    "DateAxisOptionsTypeDef",
    "AxisDisplayMinMaxRangeTypeDef",
    "AxisLinearScaleTypeDef",
    "AxisLogarithmicScaleTypeDef",
    "ItemsLimitConfigurationTypeDef",
    "InvalidTopicReviewedAnswerTypeDef",
    "ResponseMetadataTypeDef",
    "SucceededTopicReviewedAnswerTypeDef",
    "BatchDeleteTopicReviewedAnswerRequestRequestTypeDef",
    "BigQueryParametersTypeDef",
    "BinCountOptionsTypeDef",
    "BinWidthOptionsTypeDef",
    "SectionAfterPageBreakTypeDef",
    "BookmarksConfigurationsTypeDef",
    "BorderStyleTypeDef",
    "BoxPlotStyleOptionsTypeDef",
    "PaginationConfigurationTypeDef",
    "CalculatedColumnTypeDef",
    "CalculatedMeasureFieldTypeDef",
    "CancelIngestionRequestRequestTypeDef",
    "CastColumnTypeOperationTypeDef",
    "CustomFilterConfigurationTypeDef",
    "CustomFilterListConfigurationOutputTypeDef",
    "FilterListConfigurationOutputTypeDef",
    "CellValueSynonymOutputTypeDef",
    "CellValueSynonymTypeDef",
    "SimpleClusterMarkerTypeDef",
    "CollectiveConstantEntryTypeDef",
    "CollectiveConstantOutputTypeDef",
    "CollectiveConstantTypeDef",
    "DataColorTypeDef",
    "CustomColorTypeDef",
    "ColumnDescriptionTypeDef",
    "ColumnGroupColumnSchemaTypeDef",
    "GeoSpatialColumnGroupOutputTypeDef",
    "ColumnLevelPermissionRuleOutputTypeDef",
    "ColumnLevelPermissionRuleTypeDef",
    "ColumnSchemaTypeDef",
    "ComparativeOrderOutputTypeDef",
    "ComparativeOrderTypeDef",
    "ConditionalFormattingSolidColorTypeDef",
    "ConditionalFormattingCustomIconOptionsTypeDef",
    "ConditionalFormattingIconDisplayConfigurationTypeDef",
    "ConditionalFormattingIconSetTypeDef",
    "ContextMenuOptionTypeDef",
    "ContributionAnalysisFactorTypeDef",
    "CreateAccountSubscriptionRequestRequestTypeDef",
    "SignupResponseTypeDef",
    "ValidationStrategyTypeDef",
    "ResourcePermissionTypeDef",
    "DataSetUsageConfigurationTypeDef",
    "RowLevelPermissionDataSetTypeDef",
    "CreateFolderMembershipRequestRequestTypeDef",
    "FolderMemberTypeDef",
    "CreateGroupMembershipRequestRequestTypeDef",
    "GroupMemberTypeDef",
    "CreateGroupRequestRequestTypeDef",
    "GroupTypeDef",
    "CreateIAMPolicyAssignmentRequestRequestTypeDef",
    "CreateIngestionRequestRequestTypeDef",
    "CreateRoleMembershipRequestRequestTypeDef",
    "CreateTemplateAliasRequestRequestTypeDef",
    "TemplateAliasTypeDef",
    "CreateThemeAliasRequestRequestTypeDef",
    "ThemeAliasTypeDef",
    "DecimalPlacesConfigurationTypeDef",
    "NegativeValueConfigurationTypeDef",
    "NullValueFormatConfigurationTypeDef",
    "LocalNavigationConfigurationTypeDef",
    "CustomActionURLOperationTypeDef",
    "CustomFilterListConfigurationTypeDef",
    "CustomNarrativeOptionsTypeDef",
    "CustomParameterValuesOutputTypeDef",
    "InputColumnTypeDef",
    "DataPointDrillUpDownOptionTypeDef",
    "DataPointMenuLabelOptionTypeDef",
    "DataPointTooltipOptionTypeDef",
    "ExportToCSVOptionTypeDef",
    "ExportWithHiddenFieldsOptionTypeDef",
    "SheetControlsOptionTypeDef",
    "SheetLayoutElementMaximizationOptionTypeDef",
    "VisualAxisSortOptionTypeDef",
    "VisualMenuOptionTypeDef",
    "DashboardSearchFilterTypeDef",
    "DashboardSummaryTypeDef",
    "DashboardVersionSummaryTypeDef",
    "ExportHiddenFieldsOptionTypeDef",
    "DataAggregationTypeDef",
    "DataBarsOptionsTypeDef",
    "DataColorPaletteOutputTypeDef",
    "DataColorPaletteTypeDef",
    "DataPathLabelTypeTypeDef",
    "FieldLabelTypeTypeDef",
    "MaximumLabelTypeTypeDef",
    "MinimumLabelTypeTypeDef",
    "RangeEndsLabelTypeTypeDef",
    "DataPathTypeTypeDef",
    "DataSetSearchFilterTypeDef",
    "FieldFolderOutputTypeDef",
    "OutputColumnTypeDef",
    "DataSourceErrorInfoTypeDef",
    "DatabricksParametersTypeDef",
    "ExasolParametersTypeDef",
    "JiraParametersTypeDef",
    "MariaDbParametersTypeDef",
    "MySqlParametersTypeDef",
    "OracleParametersTypeDef",
    "PostgreSqlParametersTypeDef",
    "PrestoParametersTypeDef",
    "RdsParametersTypeDef",
    "ServiceNowParametersTypeDef",
    "SnowflakeParametersTypeDef",
    "SparkParametersTypeDef",
    "SqlServerParametersTypeDef",
    "StarburstParametersTypeDef",
    "TeradataParametersTypeDef",
    "TrinoParametersTypeDef",
    "TwitterParametersTypeDef",
    "DataSourceSearchFilterTypeDef",
    "DataSourceSummaryTypeDef",
    "DateTimeDatasetParameterDefaultValuesOutputTypeDef",
    "RollingDateConfigurationTypeDef",
    "DateTimeValueWhenUnsetConfigurationOutputTypeDef",
    "MappedDataSetParameterTypeDef",
    "DateTimeParameterOutputTypeDef",
    "SheetControlInfoIconLabelOptionsTypeDef",
    "DecimalDatasetParameterDefaultValuesOutputTypeDef",
    "DecimalDatasetParameterDefaultValuesTypeDef",
    "DecimalValueWhenUnsetConfigurationTypeDef",
    "DecimalParameterOutputTypeDef",
    "DecimalParameterTypeDef",
    "FilterSelectableValuesOutputTypeDef",
    "DeleteAccountCustomizationRequestRequestTypeDef",
    "DeleteAccountSubscriptionRequestRequestTypeDef",
    "DeleteAnalysisRequestRequestTypeDef",
    "DeleteDashboardRequestRequestTypeDef",
    "DeleteDataSetRefreshPropertiesRequestRequestTypeDef",
    "DeleteDataSetRequestRequestTypeDef",
    "DeleteDataSourceRequestRequestTypeDef",
    "DeleteFolderMembershipRequestRequestTypeDef",
    "DeleteFolderRequestRequestTypeDef",
    "DeleteGroupMembershipRequestRequestTypeDef",
    "DeleteGroupRequestRequestTypeDef",
    "DeleteIAMPolicyAssignmentRequestRequestTypeDef",
    "DeleteIdentityPropagationConfigRequestRequestTypeDef",
    "DeleteNamespaceRequestRequestTypeDef",
    "DeleteRefreshScheduleRequestRequestTypeDef",
    "DeleteRoleCustomPermissionRequestRequestTypeDef",
    "DeleteRoleMembershipRequestRequestTypeDef",
    "DeleteTemplateAliasRequestRequestTypeDef",
    "DeleteTemplateRequestRequestTypeDef",
    "DeleteThemeAliasRequestRequestTypeDef",
    "DeleteThemeRequestRequestTypeDef",
    "DeleteTopicRefreshScheduleRequestRequestTypeDef",
    "DeleteTopicRequestRequestTypeDef",
    "DeleteUserByPrincipalIdRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DeleteVPCConnectionRequestRequestTypeDef",
    "DescribeAccountCustomizationRequestRequestTypeDef",
    "DescribeAccountSettingsRequestRequestTypeDef",
    "DescribeAccountSubscriptionRequestRequestTypeDef",
    "DescribeAnalysisDefinitionRequestRequestTypeDef",
    "DescribeAnalysisPermissionsRequestRequestTypeDef",
    "ResourcePermissionOutputTypeDef",
    "DescribeAnalysisRequestRequestTypeDef",
    "DescribeAssetBundleExportJobRequestRequestTypeDef",
    "DescribeAssetBundleImportJobRequestRequestTypeDef",
    "DescribeDashboardDefinitionRequestRequestTypeDef",
    "DescribeDashboardPermissionsRequestRequestTypeDef",
    "DescribeDashboardRequestRequestTypeDef",
    "DescribeDashboardSnapshotJobRequestRequestTypeDef",
    "DescribeDashboardSnapshotJobResultRequestRequestTypeDef",
    "SnapshotJobErrorInfoTypeDef",
    "DescribeDataSetPermissionsRequestRequestTypeDef",
    "DescribeDataSetRefreshPropertiesRequestRequestTypeDef",
    "DescribeDataSetRequestRequestTypeDef",
    "DescribeDataSourcePermissionsRequestRequestTypeDef",
    "DescribeDataSourceRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeFolderPermissionsRequestRequestTypeDef",
    "DescribeFolderRequestRequestTypeDef",
    "DescribeFolderResolvedPermissionsRequestRequestTypeDef",
    "FolderTypeDef",
    "DescribeGroupMembershipRequestRequestTypeDef",
    "DescribeGroupRequestRequestTypeDef",
    "DescribeIAMPolicyAssignmentRequestRequestTypeDef",
    "IAMPolicyAssignmentTypeDef",
    "DescribeIngestionRequestRequestTypeDef",
    "DescribeIpRestrictionRequestRequestTypeDef",
    "DescribeKeyRegistrationRequestRequestTypeDef",
    "RegisteredCustomerManagedKeyTypeDef",
    "DescribeNamespaceRequestRequestTypeDef",
    "DescribeQPersonalizationConfigurationRequestRequestTypeDef",
    "DescribeRefreshScheduleRequestRequestTypeDef",
    "DescribeRoleCustomPermissionRequestRequestTypeDef",
    "DescribeTemplateAliasRequestRequestTypeDef",
    "DescribeTemplateDefinitionRequestRequestTypeDef",
    "DescribeTemplatePermissionsRequestRequestTypeDef",
    "DescribeTemplateRequestRequestTypeDef",
    "DescribeThemeAliasRequestRequestTypeDef",
    "DescribeThemePermissionsRequestRequestTypeDef",
    "DescribeThemeRequestRequestTypeDef",
    "DescribeTopicPermissionsRequestRequestTypeDef",
    "DescribeTopicRefreshRequestRequestTypeDef",
    "TopicRefreshDetailsTypeDef",
    "DescribeTopicRefreshScheduleRequestRequestTypeDef",
    "TopicRefreshScheduleOutputTypeDef",
    "DescribeTopicRequestRequestTypeDef",
    "DescribeUserRequestRequestTypeDef",
    "UserTypeDef",
    "DescribeVPCConnectionRequestRequestTypeDef",
    "NegativeFormatTypeDef",
    "DonutCenterOptionsTypeDef",
    "ListControlSelectAllOptionsTypeDef",
    "ErrorInfoTypeDef",
    "ExcludePeriodConfigurationTypeDef",
    "FailedKeyRegistrationEntryTypeDef",
    "FieldFolderTypeDef",
    "FieldSortTypeDef",
    "FieldTooltipItemTypeDef",
    "GeospatialMapStyleOptionsTypeDef",
    "IdentifierTypeDef",
    "FilterListConfigurationTypeDef",
    "SameSheetTargetVisualConfigurationOutputTypeDef",
    "FilterOperationTypeDef",
    "FilterSelectableValuesTypeDef",
    "FolderSearchFilterTypeDef",
    "FolderSummaryTypeDef",
    "FontSizeTypeDef",
    "FontWeightTypeDef",
    "FontTypeDef",
    "TimeBasedForecastPropertiesTypeDef",
    "WhatIfPointScenarioOutputTypeDef",
    "WhatIfRangeScenarioOutputTypeDef",
    "FreeFormLayoutScreenCanvasSizeOptionsTypeDef",
    "FreeFormLayoutElementBackgroundStyleTypeDef",
    "FreeFormLayoutElementBorderStyleTypeDef",
    "LoadingAnimationTypeDef",
    "GaugeChartColorConfigurationTypeDef",
    "SessionTagTypeDef",
    "GeoSpatialColumnGroupTypeDef",
    "GeospatialCoordinateBoundsTypeDef",
    "GeospatialHeatmapDataColorTypeDef",
    "GetDashboardEmbedUrlRequestRequestTypeDef",
    "GetSessionEmbedUrlRequestRequestTypeDef",
    "TableBorderOptionsTypeDef",
    "GradientStopTypeDef",
    "GridLayoutScreenCanvasSizeOptionsTypeDef",
    "GridLayoutElementTypeDef",
    "GroupSearchFilterTypeDef",
    "GutterStyleTypeDef",
    "IAMPolicyAssignmentSummaryTypeDef",
    "IdentityCenterConfigurationTypeDef",
    "LookbackWindowTypeDef",
    "QueueInfoTypeDef",
    "RowInfoTypeDef",
    "IntegerDatasetParameterDefaultValuesOutputTypeDef",
    "IntegerDatasetParameterDefaultValuesTypeDef",
    "IntegerValueWhenUnsetConfigurationTypeDef",
    "IntegerParameterOutputTypeDef",
    "IntegerParameterTypeDef",
    "JoinKeyPropertiesTypeDef",
    "KPISparklineOptionsTypeDef",
    "ProgressBarOptionsTypeDef",
    "SecondaryValueOptionsTypeDef",
    "TrendArrowOptionsTypeDef",
    "KPIVisualStandardLayoutTypeDef",
    "LineChartLineStyleSettingsTypeDef",
    "LineChartMarkerStyleSettingsTypeDef",
    "MissingDataConfigurationTypeDef",
    "ListAnalysesRequestRequestTypeDef",
    "ListAssetBundleExportJobsRequestRequestTypeDef",
    "ListAssetBundleImportJobsRequestRequestTypeDef",
    "ListControlSearchOptionsTypeDef",
    "ListDashboardVersionsRequestRequestTypeDef",
    "ListDashboardsRequestRequestTypeDef",
    "ListDataSetsRequestRequestTypeDef",
    "ListDataSourcesRequestRequestTypeDef",
    "ListFolderMembersRequestRequestTypeDef",
    "MemberIdArnPairTypeDef",
    "ListFoldersForResourceRequestRequestTypeDef",
    "ListFoldersRequestRequestTypeDef",
    "ListGroupMembershipsRequestRequestTypeDef",
    "ListGroupsRequestRequestTypeDef",
    "ListIAMPolicyAssignmentsForUserRequestRequestTypeDef",
    "ListIAMPolicyAssignmentsRequestRequestTypeDef",
    "ListIdentityPropagationConfigsRequestRequestTypeDef",
    "ListIngestionsRequestRequestTypeDef",
    "ListNamespacesRequestRequestTypeDef",
    "ListRefreshSchedulesRequestRequestTypeDef",
    "ListRoleMembershipsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTemplateAliasesRequestRequestTypeDef",
    "ListTemplateVersionsRequestRequestTypeDef",
    "TemplateVersionSummaryTypeDef",
    "ListTemplatesRequestRequestTypeDef",
    "TemplateSummaryTypeDef",
    "ListThemeAliasesRequestRequestTypeDef",
    "ListThemeVersionsRequestRequestTypeDef",
    "ThemeVersionSummaryTypeDef",
    "ListThemesRequestRequestTypeDef",
    "ThemeSummaryTypeDef",
    "ListTopicRefreshSchedulesRequestRequestTypeDef",
    "ListTopicReviewedAnswersRequestRequestTypeDef",
    "ListTopicsRequestRequestTypeDef",
    "TopicSummaryTypeDef",
    "ListUserGroupsRequestRequestTypeDef",
    "ListUsersRequestRequestTypeDef",
    "ListVPCConnectionsRequestRequestTypeDef",
    "LongFormatTextTypeDef",
    "ManifestFileLocationTypeDef",
    "MarginStyleTypeDef",
    "NamedEntityDefinitionMetricOutputTypeDef",
    "NamedEntityDefinitionMetricTypeDef",
    "NamedEntityRefTypeDef",
    "NamespaceErrorTypeDef",
    "NetworkInterfaceTypeDef",
    "NewDefaultValuesOutputTypeDef",
    "NumericRangeFilterValueTypeDef",
    "ThousandSeparatorOptionsTypeDef",
    "PercentileAggregationTypeDef",
    "StringParameterOutputTypeDef",
    "PercentVisibleRangeTypeDef",
    "PivotTableConditionalFormattingScopeTypeDef",
    "PivotTablePaginatedReportOptionsTypeDef",
    "PivotTableFieldOptionTypeDef",
    "PivotTableFieldSubtotalOptionsTypeDef",
    "PivotTableRowsLabelOptionsTypeDef",
    "RowAlternateColorOptionsOutputTypeDef",
    "ProjectOperationOutputTypeDef",
    "ProjectOperationTypeDef",
    "RadarChartAreaStyleSettingsTypeDef",
    "RangeConstantTypeDef",
    "RedshiftIAMParametersOutputTypeDef",
    "RedshiftIAMParametersTypeDef",
    "ReferenceLineCustomLabelConfigurationTypeDef",
    "ReferenceLineStaticDataConfigurationTypeDef",
    "ReferenceLineStyleConfigurationTypeDef",
    "ScheduleRefreshOnEntityTypeDef",
    "StatePersistenceConfigurationsTypeDef",
    "RegisteredUserGenerativeQnAEmbeddingConfigurationTypeDef",
    "RegisteredUserQSearchBarEmbeddingConfigurationTypeDef",
    "RenameColumnOperationTypeDef",
    "RestoreAnalysisRequestRequestTypeDef",
    "RowAlternateColorOptionsTypeDef",
    "RowLevelPermissionTagRuleTypeDef",
    "S3BucketConfigurationTypeDef",
    "UploadSettingsTypeDef",
    "SameSheetTargetVisualConfigurationTypeDef",
    "SpacingTypeDef",
    "SheetVisualScopingConfigurationOutputTypeDef",
    "SemanticEntityTypeOutputTypeDef",
    "SemanticEntityTypeTypeDef",
    "SemanticTypeOutputTypeDef",
    "SemanticTypeTypeDef",
    "SheetTextBoxTypeDef",
    "SheetElementConfigurationOverridesTypeDef",
    "SheetVisualScopingConfigurationTypeDef",
    "ShortFormatTextTypeDef",
    "YAxisOptionsTypeDef",
    "SlotTypeDef",
    "SmallMultiplesAxisPropertiesTypeDef",
    "SnapshotAnonymousUserRedactedTypeDef",
    "SnapshotFileSheetSelectionOutputTypeDef",
    "SnapshotFileSheetSelectionTypeDef",
    "SnapshotJobResultErrorInfoTypeDef",
    "StartDashboardSnapshotJobScheduleRequestRequestTypeDef",
    "StringDatasetParameterDefaultValuesOutputTypeDef",
    "StringDatasetParameterDefaultValuesTypeDef",
    "StringValueWhenUnsetConfigurationTypeDef",
    "StringParameterTypeDef",
    "TableStyleTargetTypeDef",
    "SuccessfulKeyRegistrationEntryTypeDef",
    "TableCellImageSizingConfigurationTypeDef",
    "TablePaginatedReportOptionsTypeDef",
    "TableFieldCustomIconContentTypeDef",
    "TablePinnedFieldOptionsOutputTypeDef",
    "TablePinnedFieldOptionsTypeDef",
    "TemplateSourceTemplateTypeDef",
    "TextControlPlaceholderOptionsTypeDef",
    "UIColorPaletteTypeDef",
    "ThemeErrorTypeDef",
    "TopicConfigOptionsTypeDef",
    "TopicIRComparisonMethodTypeDef",
    "VisualOptionsTypeDef",
    "TopicSingularFilterConstantTypeDef",
    "TotalAggregationFunctionTypeDef",
    "UntagColumnOperationOutputTypeDef",
    "UntagColumnOperationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAccountSettingsRequestRequestTypeDef",
    "UpdateDashboardLinksRequestRequestTypeDef",
    "UpdateDashboardPublishedVersionRequestRequestTypeDef",
    "UpdateFolderRequestRequestTypeDef",
    "UpdateGroupRequestRequestTypeDef",
    "UpdateIAMPolicyAssignmentRequestRequestTypeDef",
    "UpdateIdentityPropagationConfigRequestRequestTypeDef",
    "UpdateIpRestrictionRequestRequestTypeDef",
    "UpdatePublicSharingSettingsRequestRequestTypeDef",
    "UpdateQPersonalizationConfigurationRequestRequestTypeDef",
    "UpdateRoleCustomPermissionRequestRequestTypeDef",
    "UpdateSPICECapacityConfigurationRequestRequestTypeDef",
    "UpdateTemplateAliasRequestRequestTypeDef",
    "UpdateThemeAliasRequestRequestTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "UpdateVPCConnectionRequestRequestTypeDef",
    "WaterfallChartGroupColorConfigurationTypeDef",
    "WaterfallChartOptionsTypeDef",
    "WordCloudOptionsTypeDef",
    "UpdateAccountCustomizationRequestRequestTypeDef",
    "AggFunctionUnionTypeDef",
    "AxisLabelReferenceOptionsTypeDef",
    "CascadingControlSourceTypeDef",
    "CategoryDrillDownFilterOutputTypeDef",
    "CategoryDrillDownFilterTypeDef",
    "ContributionAnalysisDefaultOutputTypeDef",
    "ContributionAnalysisDefaultTypeDef",
    "DynamicDefaultValueTypeDef",
    "FilterOperationSelectedFieldsConfigurationOutputTypeDef",
    "FilterOperationSelectedFieldsConfigurationTypeDef",
    "NumericEqualityDrillDownFilterTypeDef",
    "ParameterSelectableValuesOutputTypeDef",
    "ParameterSelectableValuesTypeDef",
    "TimeRangeDrillDownFilterOutputTypeDef",
    "AnalysisErrorTypeDef",
    "DashboardErrorTypeDef",
    "TemplateErrorTypeDef",
    "SearchAnalysesRequestRequestTypeDef",
    "AnalysisSourceTemplateTypeDef",
    "DashboardSourceTemplateTypeDef",
    "TemplateSourceAnalysisTypeDef",
    "AnonymousUserDashboardFeatureConfigurationsTypeDef",
    "AnonymousUserDashboardVisualEmbeddingConfigurationTypeDef",
    "RegisteredUserDashboardVisualEmbeddingConfigurationTypeDef",
    "ArcAxisConfigurationTypeDef",
    "AssetBundleCloudFormationOverridePropertyConfigurationOutputTypeDef",
    "AssetBundleExportJobAnalysisOverridePropertiesUnionTypeDef",
    "AssetBundleExportJobDashboardOverridePropertiesUnionTypeDef",
    "AssetBundleExportJobDataSetOverridePropertiesUnionTypeDef",
    "AssetBundleExportJobDataSourceOverridePropertiesUnionTypeDef",
    "AssetBundleExportJobFolderOverridePropertiesUnionTypeDef",
    "AssetBundleExportJobRefreshScheduleOverridePropertiesUnionTypeDef",
    "AssetBundleExportJobThemeOverridePropertiesUnionTypeDef",
    "AssetBundleExportJobVPCConnectionOverridePropertiesUnionTypeDef",
    "AssetBundleImportJobAnalysisOverridePermissionsOutputTypeDef",
    "AssetBundleImportJobDataSetOverridePermissionsOutputTypeDef",
    "AssetBundleImportJobDataSourceOverridePermissionsOutputTypeDef",
    "AssetBundleImportJobFolderOverridePermissionsOutputTypeDef",
    "AssetBundleImportJobThemeOverridePermissionsOutputTypeDef",
    "AssetBundleResourceLinkSharingConfigurationOutputTypeDef",
    "AssetBundleImportJobAnalysisOverrideTagsOutputTypeDef",
    "AssetBundleImportJobAnalysisOverrideTagsTypeDef",
    "AssetBundleImportJobDashboardOverrideTagsOutputTypeDef",
    "AssetBundleImportJobDashboardOverrideTagsTypeDef",
    "AssetBundleImportJobDataSetOverrideTagsOutputTypeDef",
    "AssetBundleImportJobDataSetOverrideTagsTypeDef",
    "AssetBundleImportJobDataSourceOverrideTagsOutputTypeDef",
    "AssetBundleImportJobDataSourceOverrideTagsTypeDef",
    "AssetBundleImportJobFolderOverrideTagsOutputTypeDef",
    "AssetBundleImportJobFolderOverrideTagsTypeDef",
    "AssetBundleImportJobThemeOverrideTagsOutputTypeDef",
    "AssetBundleImportJobThemeOverrideTagsTypeDef",
    "AssetBundleImportJobVPCConnectionOverrideTagsOutputTypeDef",
    "AssetBundleImportJobVPCConnectionOverrideTagsTypeDef",
    "CreateAccountCustomizationRequestRequestTypeDef",
    "CreateNamespaceRequestRequestTypeDef",
    "CreateVPCConnectionRequestRequestTypeDef",
    "RegisterUserRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "AssetBundleImportJobDataSourceCredentialsTypeDef",
    "AssetBundleImportJobRefreshScheduleOverrideParametersTypeDef",
    "CustomParameterValuesTypeDef",
    "DateTimeDatasetParameterDefaultValuesTypeDef",
    "DateTimeParameterTypeDef",
    "DateTimeValueWhenUnsetConfigurationTypeDef",
    "NewDefaultValuesTypeDef",
    "TimeRangeDrillDownFilterTypeDef",
    "TopicRefreshScheduleTypeDef",
    "WhatIfPointScenarioTypeDef",
    "WhatIfRangeScenarioTypeDef",
    "AssetBundleImportJobVPCConnectionOverrideParametersUnionTypeDef",
    "AssetBundleImportSourceTypeDef",
    "AssetBundleResourcePermissionsUnionTypeDef",
    "AxisDisplayRangeOutputTypeDef",
    "AxisDisplayRangeTypeDef",
    "AxisScaleTypeDef",
    "ScatterPlotSortConfigurationTypeDef",
    "CancelIngestionResponseTypeDef",
    "CreateAccountCustomizationResponseTypeDef",
    "CreateAnalysisResponseTypeDef",
    "CreateDashboardResponseTypeDef",
    "CreateDataSetResponseTypeDef",
    "CreateDataSourceResponseTypeDef",
    "CreateFolderResponseTypeDef",
    "CreateIAMPolicyAssignmentResponseTypeDef",
    "CreateIngestionResponseTypeDef",
    "CreateNamespaceResponseTypeDef",
    "CreateRefreshScheduleResponseTypeDef",
    "CreateRoleMembershipResponseTypeDef",
    "CreateTemplateResponseTypeDef",
    "CreateThemeResponseTypeDef",
    "CreateTopicRefreshScheduleResponseTypeDef",
    "CreateTopicResponseTypeDef",
    "CreateVPCConnectionResponseTypeDef",
    "DeleteAccountCustomizationResponseTypeDef",
    "DeleteAccountSubscriptionResponseTypeDef",
    "DeleteAnalysisResponseTypeDef",
    "DeleteDashboardResponseTypeDef",
    "DeleteDataSetRefreshPropertiesResponseTypeDef",
    "DeleteDataSetResponseTypeDef",
    "DeleteDataSourceResponseTypeDef",
    "DeleteFolderMembershipResponseTypeDef",
    "DeleteFolderResponseTypeDef",
    "DeleteGroupMembershipResponseTypeDef",
    "DeleteGroupResponseTypeDef",
    "DeleteIAMPolicyAssignmentResponseTypeDef",
    "DeleteIdentityPropagationConfigResponseTypeDef",
    "DeleteNamespaceResponseTypeDef",
    "DeleteRefreshScheduleResponseTypeDef",
    "DeleteRoleCustomPermissionResponseTypeDef",
    "DeleteRoleMembershipResponseTypeDef",
    "DeleteTemplateAliasResponseTypeDef",
    "DeleteTemplateResponseTypeDef",
    "DeleteThemeAliasResponseTypeDef",
    "DeleteThemeResponseTypeDef",
    "DeleteTopicRefreshScheduleResponseTypeDef",
    "DeleteTopicResponseTypeDef",
    "DeleteUserByPrincipalIdResponseTypeDef",
    "DeleteUserResponseTypeDef",
    "DeleteVPCConnectionResponseTypeDef",
    "DescribeAccountCustomizationResponseTypeDef",
    "DescribeAccountSettingsResponseTypeDef",
    "DescribeAccountSubscriptionResponseTypeDef",
    "DescribeIpRestrictionResponseTypeDef",
    "DescribeQPersonalizationConfigurationResponseTypeDef",
    "DescribeRoleCustomPermissionResponseTypeDef",
    "GenerateEmbedUrlForAnonymousUserResponseTypeDef",
    "GenerateEmbedUrlForRegisteredUserResponseTypeDef",
    "GetDashboardEmbedUrlResponseTypeDef",
    "GetSessionEmbedUrlResponseTypeDef",
    "ListAnalysesResponseTypeDef",
    "ListAssetBundleExportJobsResponseTypeDef",
    "ListAssetBundleImportJobsResponseTypeDef",
    "ListFoldersForResourceResponseTypeDef",
    "ListIAMPolicyAssignmentsForUserResponseTypeDef",
    "ListIdentityPropagationConfigsResponseTypeDef",
    "ListRoleMembershipsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PutDataSetRefreshPropertiesResponseTypeDef",
    "RestoreAnalysisResponseTypeDef",
    "SearchAnalysesResponseTypeDef",
    "StartAssetBundleExportJobResponseTypeDef",
    "StartAssetBundleImportJobResponseTypeDef",
    "StartDashboardSnapshotJobResponseTypeDef",
    "StartDashboardSnapshotJobScheduleResponseTypeDef",
    "TagResourceResponseTypeDef",
    "UntagResourceResponseTypeDef",
    "UpdateAccountCustomizationResponseTypeDef",
    "UpdateAccountSettingsResponseTypeDef",
    "UpdateAnalysisResponseTypeDef",
    "UpdateDashboardLinksResponseTypeDef",
    "UpdateDashboardPublishedVersionResponseTypeDef",
    "UpdateDashboardResponseTypeDef",
    "UpdateDataSetPermissionsResponseTypeDef",
    "UpdateDataSetResponseTypeDef",
    "UpdateDataSourcePermissionsResponseTypeDef",
    "UpdateDataSourceResponseTypeDef",
    "UpdateFolderResponseTypeDef",
    "UpdateIAMPolicyAssignmentResponseTypeDef",
    "UpdateIdentityPropagationConfigResponseTypeDef",
    "UpdateIpRestrictionResponseTypeDef",
    "UpdatePublicSharingSettingsResponseTypeDef",
    "UpdateQPersonalizationConfigurationResponseTypeDef",
    "UpdateRefreshScheduleResponseTypeDef",
    "UpdateRoleCustomPermissionResponseTypeDef",
    "UpdateSPICECapacityConfigurationResponseTypeDef",
    "UpdateTemplateResponseTypeDef",
    "UpdateThemeResponseTypeDef",
    "UpdateTopicRefreshScheduleResponseTypeDef",
    "UpdateTopicResponseTypeDef",
    "UpdateVPCConnectionResponseTypeDef",
    "BatchCreateTopicReviewedAnswerResponseTypeDef",
    "BatchDeleteTopicReviewedAnswerResponseTypeDef",
    "HistogramBinOptionsTypeDef",
    "BodySectionRepeatPageBreakConfigurationTypeDef",
    "SectionPageBreakConfigurationTypeDef",
    "TileStyleTypeDef",
    "BoxPlotOptionsTypeDef",
    "CreateColumnsOperationOutputTypeDef",
    "CreateColumnsOperationTypeDef",
    "CategoryFilterConfigurationOutputTypeDef",
    "CellValueSynonymUnionTypeDef",
    "ClusterMarkerTypeDef",
    "TopicConstantValueOutputTypeDef",
    "TopicConstantValueTypeDef",
    "TopicCategoryFilterConstantOutputTypeDef",
    "CollectiveConstantUnionTypeDef",
    "ColorScaleOutputTypeDef",
    "ColorScaleTypeDef",
    "ColorsConfigurationOutputTypeDef",
    "ColorsConfigurationTypeDef",
    "ColumnTagTypeDef",
    "ColumnGroupSchemaOutputTypeDef",
    "ColumnGroupSchemaTypeDef",
    "ColumnGroupOutputTypeDef",
    "ColumnLevelPermissionRuleUnionTypeDef",
    "DataSetSchemaOutputTypeDef",
    "DataSetSchemaTypeDef",
    "ComparativeOrderUnionTypeDef",
    "ConditionalFormattingCustomIconConditionTypeDef",
    "CreateAccountSubscriptionResponseTypeDef",
    "CreateFolderRequestRequestTypeDef",
    "UpdateAnalysisPermissionsRequestRequestTypeDef",
    "UpdateDashboardPermissionsRequestRequestTypeDef",
    "UpdateDataSetPermissionsRequestRequestTypeDef",
    "UpdateDataSourcePermissionsRequestRequestTypeDef",
    "UpdateFolderPermissionsRequestRequestTypeDef",
    "UpdateTemplatePermissionsRequestRequestTypeDef",
    "UpdateThemePermissionsRequestRequestTypeDef",
    "UpdateTopicPermissionsRequestRequestTypeDef",
    "DataSetSummaryTypeDef",
    "CreateFolderMembershipResponseTypeDef",
    "CreateGroupMembershipResponseTypeDef",
    "DescribeGroupMembershipResponseTypeDef",
    "ListGroupMembershipsResponseTypeDef",
    "CreateGroupResponseTypeDef",
    "DescribeGroupResponseTypeDef",
    "ListGroupsResponseTypeDef",
    "ListUserGroupsResponseTypeDef",
    "SearchGroupsResponseTypeDef",
    "UpdateGroupResponseTypeDef",
    "CreateTemplateAliasResponseTypeDef",
    "DescribeTemplateAliasResponseTypeDef",
    "ListTemplateAliasesResponseTypeDef",
    "UpdateTemplateAliasResponseTypeDef",
    "CreateThemeAliasResponseTypeDef",
    "DescribeThemeAliasResponseTypeDef",
    "ListThemeAliasesResponseTypeDef",
    "UpdateThemeAliasResponseTypeDef",
    "CustomActionNavigationOperationTypeDef",
    "CustomFilterListConfigurationUnionTypeDef",
    "CustomValuesConfigurationOutputTypeDef",
    "CustomSqlOutputTypeDef",
    "CustomSqlTypeDef",
    "RelationalTableOutputTypeDef",
    "RelationalTableTypeDef",
    "VisualInteractionOptionsTypeDef",
    "SearchDashboardsRequestRequestTypeDef",
    "ListDashboardsResponseTypeDef",
    "SearchDashboardsResponseTypeDef",
    "ListDashboardVersionsResponseTypeDef",
    "DashboardVisualPublishOptionsTypeDef",
    "TableInlineVisualizationTypeDef",
    "DataColorPaletteUnionTypeDef",
    "DataLabelTypeTypeDef",
    "DataPathValueTypeDef",
    "SearchDataSetsRequestRequestTypeDef",
    "SearchDataSourcesRequestRequestTypeDef",
    "SearchDataSourcesResponseTypeDef",
    "DateTimeDatasetParameterOutputTypeDef",
    "TimeRangeFilterValueOutputTypeDef",
    "TimeRangeFilterValueTypeDef",
    "DecimalDatasetParameterOutputTypeDef",
    "DecimalDatasetParameterDefaultValuesUnionTypeDef",
    "DecimalParameterUnionTypeDef",
    "DescribeAnalysisPermissionsResponseTypeDef",
    "DescribeDataSetPermissionsResponseTypeDef",
    "DescribeDataSourcePermissionsResponseTypeDef",
    "DescribeFolderPermissionsResponseTypeDef",
    "DescribeFolderResolvedPermissionsResponseTypeDef",
    "DescribeTemplatePermissionsResponseTypeDef",
    "DescribeThemePermissionsResponseTypeDef",
    "DescribeTopicPermissionsResponseTypeDef",
    "LinkSharingConfigurationOutputTypeDef",
    "ResourcePermissionUnionTypeDef",
    "UpdateAnalysisPermissionsResponseTypeDef",
    "UpdateFolderPermissionsResponseTypeDef",
    "UpdateTemplatePermissionsResponseTypeDef",
    "UpdateThemePermissionsResponseTypeDef",
    "UpdateTopicPermissionsResponseTypeDef",
    "DescribeFolderPermissionsRequestDescribeFolderPermissionsPaginateTypeDef",
    "DescribeFolderResolvedPermissionsRequestDescribeFolderResolvedPermissionsPaginateTypeDef",
    "ListAnalysesRequestListAnalysesPaginateTypeDef",
    "ListAssetBundleExportJobsRequestListAssetBundleExportJobsPaginateTypeDef",
    "ListAssetBundleImportJobsRequestListAssetBundleImportJobsPaginateTypeDef",
    "ListDashboardVersionsRequestListDashboardVersionsPaginateTypeDef",
    "ListDashboardsRequestListDashboardsPaginateTypeDef",
    "ListDataSetsRequestListDataSetsPaginateTypeDef",
    "ListDataSourcesRequestListDataSourcesPaginateTypeDef",
    "ListFolderMembersRequestListFolderMembersPaginateTypeDef",
    "ListFoldersForResourceRequestListFoldersForResourcePaginateTypeDef",
    "ListFoldersRequestListFoldersPaginateTypeDef",
    "ListGroupMembershipsRequestListGroupMembershipsPaginateTypeDef",
    "ListGroupsRequestListGroupsPaginateTypeDef",
    "ListIAMPolicyAssignmentsForUserRequestListIAMPolicyAssignmentsForUserPaginateTypeDef",
    "ListIAMPolicyAssignmentsRequestListIAMPolicyAssignmentsPaginateTypeDef",
    "ListIngestionsRequestListIngestionsPaginateTypeDef",
    "ListNamespacesRequestListNamespacesPaginateTypeDef",
    "ListRoleMembershipsRequestListRoleMembershipsPaginateTypeDef",
    "ListTemplateAliasesRequestListTemplateAliasesPaginateTypeDef",
    "ListTemplateVersionsRequestListTemplateVersionsPaginateTypeDef",
    "ListTemplatesRequestListTemplatesPaginateTypeDef",
    "ListThemeVersionsRequestListThemeVersionsPaginateTypeDef",
    "ListThemesRequestListThemesPaginateTypeDef",
    "ListUserGroupsRequestListUserGroupsPaginateTypeDef",
    "ListUsersRequestListUsersPaginateTypeDef",
    "SearchAnalysesRequestSearchAnalysesPaginateTypeDef",
    "SearchDashboardsRequestSearchDashboardsPaginateTypeDef",
    "SearchDataSetsRequestSearchDataSetsPaginateTypeDef",
    "SearchDataSourcesRequestSearchDataSourcesPaginateTypeDef",
    "DescribeFolderResponseTypeDef",
    "DescribeIAMPolicyAssignmentResponseTypeDef",
    "DescribeKeyRegistrationResponseTypeDef",
    "UpdateKeyRegistrationRequestRequestTypeDef",
    "DescribeTopicRefreshResponseTypeDef",
    "DescribeTopicRefreshScheduleResponseTypeDef",
    "TopicRefreshScheduleSummaryTypeDef",
    "DescribeUserResponseTypeDef",
    "ListUsersResponseTypeDef",
    "RegisterUserResponseTypeDef",
    "UpdateUserResponseTypeDef",
    "DisplayFormatOptionsTypeDef",
    "DonutOptionsTypeDef",
    "FieldFolderUnionTypeDef",
    "FilterAggMetricsTypeDef",
    "TopicSortClauseTypeDef",
    "FilterListConfigurationUnionTypeDef",
    "FilterOperationTargetVisualsConfigurationOutputTypeDef",
    "FilterSelectableValuesUnionTypeDef",
    "SearchFoldersRequestRequestTypeDef",
    "SearchFoldersRequestSearchFoldersPaginateTypeDef",
    "ListFoldersResponseTypeDef",
    "SearchFoldersResponseTypeDef",
    "FontConfigurationTypeDef",
    "TypographyOutputTypeDef",
    "TypographyTypeDef",
    "ForecastScenarioOutputTypeDef",
    "FreeFormLayoutCanvasSizeOptionsTypeDef",
    "SnapshotAnonymousUserTypeDef",
    "GeoSpatialColumnGroupUnionTypeDef",
    "GeospatialWindowOptionsTypeDef",
    "GeospatialHeatmapColorScaleOutputTypeDef",
    "GeospatialHeatmapColorScaleTypeDef",
    "TableSideBorderOptionsTypeDef",
    "GradientColorOutputTypeDef",
    "GradientColorTypeDef",
    "GridLayoutCanvasSizeOptionsTypeDef",
    "SearchGroupsRequestRequestTypeDef",
    "SearchGroupsRequestSearchGroupsPaginateTypeDef",
    "ListIAMPolicyAssignmentsResponseTypeDef",
    "IncrementalRefreshTypeDef",
    "IngestionTypeDef",
    "IntegerDatasetParameterOutputTypeDef",
    "IntegerDatasetParameterDefaultValuesUnionTypeDef",
    "IntegerParameterUnionTypeDef",
    "JoinInstructionTypeDef",
    "KPIVisualLayoutOptionsTypeDef",
    "LineChartDefaultSeriesSettingsTypeDef",
    "LineChartSeriesSettingsTypeDef",
    "ListFolderMembersResponseTypeDef",
    "ListTemplateVersionsResponseTypeDef",
    "ListTemplatesResponseTypeDef",
    "ListThemeVersionsResponseTypeDef",
    "ListThemesResponseTypeDef",
    "ListTopicsResponseTypeDef",
    "VisualSubtitleLabelOptionsTypeDef",
    "S3ParametersTypeDef",
    "TileLayoutStyleTypeDef",
    "NamedEntityDefinitionOutputTypeDef",
    "NamedEntityDefinitionMetricUnionTypeDef",
    "NamespaceInfoV2TypeDef",
    "VPCConnectionSummaryTypeDef",
    "VPCConnectionTypeDef",
    "OverrideDatasetParameterOperationOutputTypeDef",
    "NumericSeparatorConfigurationTypeDef",
    "NumericalAggregationFunctionTypeDef",
    "ParametersOutputTypeDef",
    "VisibleRangeOptionsTypeDef",
    "ProjectOperationUnionTypeDef",
    "RadarChartSeriesSettingsTypeDef",
    "TopicRangeFilterConstantTypeDef",
    "RedshiftParametersOutputTypeDef",
    "RedshiftIAMParametersUnionTypeDef",
    "RefreshFrequencyTypeDef",
    "RegisteredUserConsoleFeatureConfigurationsTypeDef",
    "RegisteredUserDashboardFeatureConfigurationsTypeDef",
    "RowAlternateColorOptionsUnionTypeDef",
    "RowLevelPermissionTagConfigurationOutputTypeDef",
    "RowLevelPermissionTagConfigurationTypeDef",
    "SnapshotS3DestinationConfigurationTypeDef",
    "S3SourceOutputTypeDef",
    "S3SourceTypeDef",
    "SameSheetTargetVisualConfigurationUnionTypeDef",
    "SectionBasedLayoutPaperCanvasSizeOptionsTypeDef",
    "SectionStyleTypeDef",
    "SelectedSheetsFilterScopeConfigurationOutputTypeDef",
    "SemanticEntityTypeUnionTypeDef",
    "SemanticTypeUnionTypeDef",
    "SheetElementRenderingRuleTypeDef",
    "SheetVisualScopingConfigurationUnionTypeDef",
    "VisualTitleLabelOptionsTypeDef",
    "SingleAxisOptionsTypeDef",
    "TopicTemplateOutputTypeDef",
    "TopicTemplateTypeDef",
    "SnapshotUserConfigurationRedactedTypeDef",
    "SnapshotFileOutputTypeDef",
    "SnapshotFileSheetSelectionUnionTypeDef",
    "StringDatasetParameterOutputTypeDef",
    "StringDatasetParameterDefaultValuesUnionTypeDef",
    "StringParameterUnionTypeDef",
    "UpdateKeyRegistrationResponseTypeDef",
    "TableFieldImageConfigurationTypeDef",
    "TablePinnedFieldOptionsUnionTypeDef",
    "TopicNumericEqualityFilterTypeDef",
    "TopicRelativeDateFilterTypeDef",
    "TotalAggregationOptionTypeDef",
    "UntagColumnOperationUnionTypeDef",
    "WaterfallChartColorConfigurationTypeDef",
    "CascadingControlConfigurationOutputTypeDef",
    "CascadingControlConfigurationTypeDef",
    "CategoryDrillDownFilterUnionTypeDef",
    "ContributionAnalysisDefaultUnionTypeDef",
    "DateTimeDefaultValuesOutputTypeDef",
    "DateTimeDefaultValuesTypeDef",
    "DecimalDefaultValuesOutputTypeDef",
    "DecimalDefaultValuesTypeDef",
    "IntegerDefaultValuesOutputTypeDef",
    "IntegerDefaultValuesTypeDef",
    "StringDefaultValuesOutputTypeDef",
    "StringDefaultValuesTypeDef",
    "FilterOperationSelectedFieldsConfigurationUnionTypeDef",
    "ParameterSelectableValuesUnionTypeDef",
    "DrillDownFilterOutputTypeDef",
    "AnalysisTypeDef",
    "DashboardVersionTypeDef",
    "AnalysisSourceEntityTypeDef",
    "DashboardSourceEntityTypeDef",
    "TemplateSourceEntityTypeDef",
    "AnonymousUserDashboardEmbeddingConfigurationTypeDef",
    "DescribeAssetBundleExportJobResponseTypeDef",
    "AssetBundleCloudFormationOverridePropertyConfigurationTypeDef",
    "AssetBundleImportJobDashboardOverridePermissionsOutputTypeDef",
    "AssetBundleImportJobAnalysisOverrideTagsUnionTypeDef",
    "AssetBundleImportJobDashboardOverrideTagsUnionTypeDef",
    "AssetBundleImportJobDataSetOverrideTagsUnionTypeDef",
    "AssetBundleImportJobDataSourceOverrideTagsUnionTypeDef",
    "AssetBundleImportJobFolderOverrideTagsUnionTypeDef",
    "AssetBundleImportJobThemeOverrideTagsUnionTypeDef",
    "AssetBundleImportJobOverrideTagsOutputTypeDef",
    "AssetBundleImportJobVPCConnectionOverrideTagsUnionTypeDef",
    "AssetBundleImportJobRefreshScheduleOverrideParametersUnionTypeDef",
    "CustomParameterValuesUnionTypeDef",
    "DateTimeDatasetParameterDefaultValuesUnionTypeDef",
    "DateTimeParameterUnionTypeDef",
    "DateTimeValueWhenUnsetConfigurationUnionTypeDef",
    "NewDefaultValuesUnionTypeDef",
    "TimeRangeDrillDownFilterUnionTypeDef",
    "CreateTopicRefreshScheduleRequestRequestTypeDef",
    "UpdateTopicRefreshScheduleRequestRequestTypeDef",
    "WhatIfPointScenarioUnionTypeDef",
    "WhatIfRangeScenarioUnionTypeDef",
    "AssetBundleImportJobAnalysisOverridePermissionsTypeDef",
    "AssetBundleImportJobDataSetOverridePermissionsTypeDef",
    "AssetBundleImportJobDataSourceOverridePermissionsTypeDef",
    "AssetBundleImportJobFolderOverridePermissionsTypeDef",
    "AssetBundleImportJobThemeOverridePermissionsTypeDef",
    "AssetBundleResourceLinkSharingConfigurationTypeDef",
    "AxisDisplayRangeUnionTypeDef",
    "NumericAxisOptionsOutputTypeDef",
    "CreateColumnsOperationUnionTypeDef",
    "ClusterMarkerConfigurationTypeDef",
    "TopicConstantValueUnionTypeDef",
    "TopicCategoryFilterOutputTypeDef",
    "TopicCategoryFilterConstantTypeDef",
    "ColorScaleUnionTypeDef",
    "ColorsConfigurationUnionTypeDef",
    "TagColumnOperationOutputTypeDef",
    "TagColumnOperationTypeDef",
    "ColumnGroupSchemaUnionTypeDef",
    "DataSetConfigurationOutputTypeDef",
    "DataSetSchemaUnionTypeDef",
    "ConditionalFormattingIconTypeDef",
    "ListDataSetsResponseTypeDef",
    "SearchDataSetsResponseTypeDef",
    "DestinationParameterValueConfigurationOutputTypeDef",
    "CustomSqlUnionTypeDef",
    "RelationalTableUnionTypeDef",
    "CustomContentConfigurationTypeDef",
    "DashboardPublishOptionsTypeDef",
    "DataPathColorTypeDef",
    "DataPathSortOutputTypeDef",
    "DataPathSortTypeDef",
    "PivotTableDataPathOptionOutputTypeDef",
    "PivotTableDataPathOptionTypeDef",
    "PivotTableFieldCollapseStateTargetOutputTypeDef",
    "PivotTableFieldCollapseStateTargetTypeDef",
    "TimeRangeFilterValueUnionTypeDef",
    "DecimalDatasetParameterTypeDef",
    "DescribeDashboardPermissionsResponseTypeDef",
    "UpdateDashboardPermissionsResponseTypeDef",
    "LinkSharingConfigurationTypeDef",
    "ListTopicRefreshSchedulesResponseTypeDef",
    "DefaultFormattingTypeDef",
    "TopicIRMetricOutputTypeDef",
    "TopicIRMetricTypeDef",
    "TopicIRFilterOptionOutputTypeDef",
    "TopicIRGroupByTypeDef",
    "CategoryFilterConfigurationTypeDef",
    "CustomActionFilterOperationOutputTypeDef",
    "AxisLabelOptionsTypeDef",
    "DataLabelOptionsOutputTypeDef",
    "DataLabelOptionsTypeDef",
    "FunnelChartDataLabelOptionsTypeDef",
    "LabelOptionsTypeDef",
    "PanelTitleOptionsTypeDef",
    "TableFieldCustomTextContentTypeDef",
    "TypographyUnionTypeDef",
    "ForecastConfigurationOutputTypeDef",
    "DefaultFreeFormLayoutConfigurationTypeDef",
    "SnapshotUserConfigurationTypeDef",
    "ColumnGroupTypeDef",
    "GeospatialHeatmapConfigurationOutputTypeDef",
    "GeospatialHeatmapColorScaleUnionTypeDef",
    "GlobalTableBorderOptionsTypeDef",
    "ConditionalFormattingGradientColorOutputTypeDef",
    "GradientColorUnionTypeDef",
    "DefaultGridLayoutConfigurationTypeDef",
    "GridLayoutConfigurationOutputTypeDef",
    "GridLayoutConfigurationTypeDef",
    "RefreshConfigurationTypeDef",
    "DescribeIngestionResponseTypeDef",
    "ListIngestionsResponseTypeDef",
    "IntegerDatasetParameterTypeDef",
    "LogicalTableSourceTypeDef",
    "DataFieldSeriesItemTypeDef",
    "FieldSeriesItemTypeDef",
    "SheetStyleTypeDef",
    "TopicNamedEntityOutputTypeDef",
    "NamedEntityDefinitionTypeDef",
    "DescribeNamespaceResponseTypeDef",
    "ListNamespacesResponseTypeDef",
    "ListVPCConnectionsResponseTypeDef",
    "DescribeVPCConnectionResponseTypeDef",
    "CurrencyDisplayFormatConfigurationTypeDef",
    "NumberDisplayFormatConfigurationTypeDef",
    "PercentageDisplayFormatConfigurationTypeDef",
    "AggregationFunctionTypeDef",
    "ScrollBarOptionsTypeDef",
    "TopicDateRangeFilterTypeDef",
    "TopicNumericRangeFilterTypeDef",
    "DataSourceParametersOutputTypeDef",
    "RedshiftParametersTypeDef",
    "RefreshScheduleOutputTypeDef",
    "RefreshScheduleTypeDef",
    "RegisteredUserQuickSightConsoleEmbeddingConfigurationTypeDef",
    "RegisteredUserDashboardEmbeddingConfigurationTypeDef",
    "SnapshotDestinationConfigurationOutputTypeDef",
    "SnapshotDestinationConfigurationTypeDef",
    "SnapshotJobS3ResultTypeDef",
    "PhysicalTableOutputTypeDef",
    "S3SourceUnionTypeDef",
    "FilterOperationTargetVisualsConfigurationTypeDef",
    "SectionBasedLayoutCanvasSizeOptionsTypeDef",
    "FilterScopeConfigurationOutputTypeDef",
    "FreeFormLayoutElementOutputTypeDef",
    "FreeFormLayoutElementTypeDef",
    "SelectedSheetsFilterScopeConfigurationTypeDef",
    "TopicTemplateUnionTypeDef",
    "SnapshotFileGroupOutputTypeDef",
    "SnapshotFileTypeDef",
    "DatasetParameterOutputTypeDef",
    "StringDatasetParameterTypeDef",
    "FilterCrossSheetControlOutputTypeDef",
    "CascadingControlConfigurationUnionTypeDef",
    "DateTimeParameterDeclarationOutputTypeDef",
    "DateTimeDefaultValuesUnionTypeDef",
    "DecimalParameterDeclarationOutputTypeDef",
    "DecimalDefaultValuesUnionTypeDef",
    "IntegerParameterDeclarationOutputTypeDef",
    "IntegerDefaultValuesUnionTypeDef",
    "StringParameterDeclarationOutputTypeDef",
    "StringDefaultValuesUnionTypeDef",
    "DateTimeHierarchyOutputTypeDef",
    "ExplicitHierarchyOutputTypeDef",
    "PredefinedHierarchyOutputTypeDef",
    "DescribeAnalysisResponseTypeDef",
    "DashboardTypeDef",
    "AnonymousUserEmbeddingExperienceConfigurationTypeDef",
    "StartAssetBundleExportJobRequestRequestTypeDef",
    "AssetBundleImportJobOverridePermissionsOutputTypeDef",
    "AssetBundleImportJobOverrideTagsTypeDef",
    "CustomValuesConfigurationTypeDef",
    "DateTimeDatasetParameterTypeDef",
    "ParametersTypeDef",
    "OverrideDatasetParameterOperationTypeDef",
    "DrillDownFilterTypeDef",
    "ForecastScenarioTypeDef",
    "AssetBundleImportJobAnalysisOverridePermissionsUnionTypeDef",
    "AssetBundleImportJobDataSetOverridePermissionsUnionTypeDef",
    "AssetBundleImportJobDataSourceOverridePermissionsUnionTypeDef",
    "AssetBundleImportJobFolderOverridePermissionsUnionTypeDef",
    "AssetBundleImportJobThemeOverridePermissionsUnionTypeDef",
    "AssetBundleResourceLinkSharingConfigurationUnionTypeDef",
    "NumericAxisOptionsTypeDef",
    "AxisDataOptionsOutputTypeDef",
    "TopicIRFilterOptionTypeDef",
    "TopicCategoryFilterConstantUnionTypeDef",
    "TransformOperationOutputTypeDef",
    "TagColumnOperationUnionTypeDef",
    "TemplateVersionTypeDef",
    "DataSetConfigurationTypeDef",
    "SetParameterValueConfigurationOutputTypeDef",
    "VisualPaletteOutputTypeDef",
    "VisualPaletteTypeDef",
    "DataPathSortUnionTypeDef",
    "PivotTableDataPathOptionUnionTypeDef",
    "PivotTableFieldCollapseStateOptionOutputTypeDef",
    "PivotTableFieldCollapseStateTargetUnionTypeDef",
    "DecimalDatasetParameterUnionTypeDef",
    "TopicCalculatedFieldOutputTypeDef",
    "TopicCalculatedFieldTypeDef",
    "TopicColumnOutputTypeDef",
    "TopicColumnTypeDef",
    "TopicIRMetricUnionTypeDef",
    "ContributionAnalysisTimeRangesOutputTypeDef",
    "CategoryFilterConfigurationUnionTypeDef",
    "ChartAxisLabelOptionsOutputTypeDef",
    "ChartAxisLabelOptionsTypeDef",
    "DataLabelOptionsUnionTypeDef",
    "AxisTickLabelOptionsTypeDef",
    "DateTimePickerControlDisplayOptionsTypeDef",
    "DropDownControlDisplayOptionsTypeDef",
    "LegendOptionsTypeDef",
    "ListControlDisplayOptionsTypeDef",
    "RelativeDateTimeControlDisplayOptionsTypeDef",
    "SliderControlDisplayOptionsTypeDef",
    "TextAreaControlDisplayOptionsTypeDef",
    "TextFieldControlDisplayOptionsTypeDef",
    "PanelConfigurationTypeDef",
    "TableFieldLinkContentConfigurationTypeDef",
    "ColumnGroupUnionTypeDef",
    "GeospatialPointStyleOptionsOutputTypeDef",
    "GeospatialHeatmapConfigurationTypeDef",
    "TableCellStyleTypeDef",
    "ConditionalFormattingColorOutputTypeDef",
    "ConditionalFormattingGradientColorTypeDef",
    "DefaultInteractiveLayoutConfigurationTypeDef",
    "SheetControlLayoutConfigurationOutputTypeDef",
    "GridLayoutConfigurationUnionTypeDef",
    "DataSetRefreshPropertiesTypeDef",
    "IntegerDatasetParameterUnionTypeDef",
    "SeriesItemTypeDef",
    "ThemeConfigurationOutputTypeDef",
    "ThemeConfigurationTypeDef",
    "NamedEntityDefinitionUnionTypeDef",
    "ComparisonFormatConfigurationTypeDef",
    "NumericFormatConfigurationTypeDef",
    "AggregationSortConfigurationTypeDef",
    "ColumnSortTypeDef",
    "ColumnTooltipItemTypeDef",
    "ReferenceLineDynamicDataConfigurationTypeDef",
    "TopicFilterOutputTypeDef",
    "AssetBundleImportJobDataSourceOverrideParametersOutputTypeDef",
    "DataSourceTypeDef",
    "RedshiftParametersUnionTypeDef",
    "DescribeRefreshScheduleResponseTypeDef",
    "ListRefreshSchedulesResponseTypeDef",
    "CreateRefreshScheduleRequestRequestTypeDef",
    "UpdateRefreshScheduleRequestRequestTypeDef",
    "RegisteredUserEmbeddingExperienceConfigurationTypeDef",
    "SnapshotDestinationConfigurationUnionTypeDef",
    "SnapshotJobResultFileGroupTypeDef",
    "PhysicalTableTypeDef",
    "FilterOperationTargetVisualsConfigurationUnionTypeDef",
    "DefaultSectionBasedLayoutConfigurationTypeDef",
    "FreeFormLayoutConfigurationOutputTypeDef",
    "FreeFormSectionLayoutConfigurationOutputTypeDef",
    "FreeFormLayoutElementUnionTypeDef",
    "SelectedSheetsFilterScopeConfigurationUnionTypeDef",
    "SnapshotConfigurationOutputTypeDef",
    "SnapshotFileUnionTypeDef",
    "StringDatasetParameterUnionTypeDef",
    "FilterCrossSheetControlTypeDef",
    "DateTimeParameterDeclarationTypeDef",
    "DecimalParameterDeclarationTypeDef",
    "IntegerParameterDeclarationTypeDef",
    "ParameterDeclarationOutputTypeDef",
    "StringParameterDeclarationTypeDef",
    "ColumnHierarchyOutputTypeDef",
    "DescribeDashboardResponseTypeDef",
    "GenerateEmbedUrlForAnonymousUserRequestRequestTypeDef",
    "CustomValuesConfigurationUnionTypeDef",
    "DateTimeDatasetParameterUnionTypeDef",
    "ParametersUnionTypeDef",
    "OverrideDatasetParameterOperationUnionTypeDef",
    "DrillDownFilterUnionTypeDef",
    "ForecastScenarioUnionTypeDef",
    "AssetBundleImportJobDashboardOverridePermissionsTypeDef",
    "NumericAxisOptionsUnionTypeDef",
    "TopicIRFilterOptionUnionTypeDef",
    "TopicCategoryFilterTypeDef",
    "LogicalTableOutputTypeDef",
    "TemplateTypeDef",
    "DataSetConfigurationUnionTypeDef",
    "CustomActionSetParametersOperationOutputTypeDef",
    "VisualPaletteUnionTypeDef",
    "PivotTableFieldOptionsOutputTypeDef",
    "PivotTableFieldCollapseStateOptionTypeDef",
    "TopicCalculatedFieldUnionTypeDef",
    "TopicColumnUnionTypeDef",
    "TopicIRContributionAnalysisOutputTypeDef",
    "ChartAxisLabelOptionsUnionTypeDef",
    "AxisDisplayOptionsOutputTypeDef",
    "DefaultDateTimePickerControlOptionsTypeDef",
    "FilterDateTimePickerControlTypeDef",
    "ParameterDateTimePickerControlTypeDef",
    "DefaultFilterDropDownControlOptionsOutputTypeDef",
    "DefaultFilterDropDownControlOptionsTypeDef",
    "FilterDropDownControlOutputTypeDef",
    "FilterDropDownControlTypeDef",
    "ParameterDropDownControlOutputTypeDef",
    "ParameterDropDownControlTypeDef",
    "DefaultFilterListControlOptionsOutputTypeDef",
    "DefaultFilterListControlOptionsTypeDef",
    "FilterListControlOutputTypeDef",
    "FilterListControlTypeDef",
    "ParameterListControlOutputTypeDef",
    "ParameterListControlTypeDef",
    "DefaultRelativeDateTimeControlOptionsTypeDef",
    "FilterRelativeDateTimeControlTypeDef",
    "DefaultSliderControlOptionsTypeDef",
    "FilterSliderControlTypeDef",
    "ParameterSliderControlTypeDef",
    "DefaultTextAreaControlOptionsTypeDef",
    "FilterTextAreaControlTypeDef",
    "ParameterTextAreaControlTypeDef",
    "DefaultTextFieldControlOptionsTypeDef",
    "FilterTextFieldControlTypeDef",
    "ParameterTextFieldControlTypeDef",
    "SmallMultiplesOptionsTypeDef",
    "TableFieldLinkConfigurationTypeDef",
    "GeospatialHeatmapConfigurationUnionTypeDef",
    "PivotTableOptionsOutputTypeDef",
    "PivotTableOptionsTypeDef",
    "PivotTotalOptionsOutputTypeDef",
    "PivotTotalOptionsTypeDef",
    "SubtotalOptionsOutputTypeDef",
    "SubtotalOptionsTypeDef",
    "TableOptionsOutputTypeDef",
    "TableOptionsTypeDef",
    "TotalOptionsOutputTypeDef",
    "TotalOptionsTypeDef",
    "GaugeChartArcConditionalFormattingOutputTypeDef",
    "GaugeChartPrimaryValueConditionalFormattingOutputTypeDef",
    "KPIActualValueConditionalFormattingOutputTypeDef",
    "KPIComparisonValueConditionalFormattingOutputTypeDef",
    "KPIPrimaryValueConditionalFormattingOutputTypeDef",
    "KPIProgressBarConditionalFormattingOutputTypeDef",
    "ShapeConditionalFormatOutputTypeDef",
    "TableRowConditionalFormattingOutputTypeDef",
    "TextConditionalFormatOutputTypeDef",
    "ConditionalFormattingGradientColorUnionTypeDef",
    "SheetControlLayoutOutputTypeDef",
    "SheetControlLayoutConfigurationTypeDef",
    "DescribeDataSetRefreshPropertiesResponseTypeDef",
    "PutDataSetRefreshPropertiesRequestRequestTypeDef",
    "ThemeVersionTypeDef",
    "CreateThemeRequestRequestTypeDef",
    "UpdateThemeRequestRequestTypeDef",
    "TopicNamedEntityTypeDef",
    "ComparisonConfigurationTypeDef",
    "DateTimeFormatConfigurationTypeDef",
    "NumberFormatConfigurationTypeDef",
    "ReferenceLineValueLabelConfigurationTypeDef",
    "StringFormatConfigurationTypeDef",
    "BodySectionDynamicCategoryDimensionConfigurationOutputTypeDef",
    "BodySectionDynamicCategoryDimensionConfigurationTypeDef",
    "BodySectionDynamicNumericDimensionConfigurationOutputTypeDef",
    "BodySectionDynamicNumericDimensionConfigurationTypeDef",
    "FieldSortOptionsTypeDef",
    "PivotTableSortByOutputTypeDef",
    "PivotTableSortByTypeDef",
    "TooltipItemTypeDef",
    "ReferenceLineDataConfigurationTypeDef",
    "DatasetMetadataOutputTypeDef",
    "AssetBundleImportJobOverrideParametersOutputTypeDef",
    "DescribeDataSourceResponseTypeDef",
    "ListDataSourcesResponseTypeDef",
    "DataSourceParametersTypeDef",
    "GenerateEmbedUrlForRegisteredUserRequestRequestTypeDef",
    "AnonymousUserSnapshotJobResultTypeDef",
    "PhysicalTableUnionTypeDef",
    "CustomActionFilterOperationTypeDef",
    "DefaultPaginatedLayoutConfigurationTypeDef",
    "SectionLayoutConfigurationOutputTypeDef",
    "FreeFormLayoutConfigurationTypeDef",
    "FreeFormSectionLayoutConfigurationTypeDef",
    "FilterScopeConfigurationTypeDef",
    "DescribeDashboardSnapshotJobResponseTypeDef",
    "SnapshotFileGroupTypeDef",
    "FilterCrossSheetControlUnionTypeDef",
    "DateTimeParameterDeclarationUnionTypeDef",
    "DecimalParameterDeclarationUnionTypeDef",
    "IntegerParameterDeclarationUnionTypeDef",
    "StringParameterDeclarationUnionTypeDef",
    "DestinationParameterValueConfigurationTypeDef",
    "DatasetParameterTypeDef",
    "TransformOperationTypeDef",
    "DateTimeHierarchyTypeDef",
    "ExplicitHierarchyTypeDef",
    "PredefinedHierarchyTypeDef",
    "ForecastConfigurationTypeDef",
    "AssetBundleImportJobDashboardOverridePermissionsUnionTypeDef",
    "AxisDataOptionsTypeDef",
    "ContributionAnalysisTimeRangesTypeDef",
    "TopicCategoryFilterUnionTypeDef",
    "DataSetTypeDef",
    "DescribeTemplateResponseTypeDef",
    "VisualCustomActionOperationOutputTypeDef",
    "PivotTableFieldCollapseStateOptionUnionTypeDef",
    "TopicIROutputTypeDef",
    "LineSeriesAxisDisplayOptionsOutputTypeDef",
    "DefaultFilterDropDownControlOptionsUnionTypeDef",
    "FilterDropDownControlUnionTypeDef",
    "ParameterDropDownControlUnionTypeDef",
    "DefaultFilterListControlOptionsUnionTypeDef",
    "FilterListControlUnionTypeDef",
    "ParameterListControlUnionTypeDef",
    "DefaultFilterControlOptionsOutputTypeDef",
    "FilterControlOutputTypeDef",
    "ParameterControlOutputTypeDef",
    "TableFieldURLConfigurationTypeDef",
    "GeospatialPointStyleOptionsTypeDef",
    "PivotTableOptionsUnionTypeDef",
    "PivotTotalOptionsUnionTypeDef",
    "PivotTableTotalOptionsOutputTypeDef",
    "SubtotalOptionsUnionTypeDef",
    "TableOptionsUnionTypeDef",
    "TotalOptionsUnionTypeDef",
    "GaugeChartConditionalFormattingOptionOutputTypeDef",
    "KPIConditionalFormattingOptionOutputTypeDef",
    "FilledMapShapeConditionalFormattingOutputTypeDef",
    "PivotTableCellConditionalFormattingOutputTypeDef",
    "TableCellConditionalFormattingOutputTypeDef",
    "ConditionalFormattingColorTypeDef",
    "SheetControlLayoutConfigurationUnionTypeDef",
    "ThemeTypeDef",
    "TopicNamedEntityUnionTypeDef",
    "GaugeChartOptionsTypeDef",
    "KPIOptionsTypeDef",
    "DateDimensionFieldTypeDef",
    "DateMeasureFieldTypeDef",
    "NumericalDimensionFieldTypeDef",
    "NumericalMeasureFieldTypeDef",
    "ReferenceLineLabelConfigurationTypeDef",
    "CategoricalDimensionFieldTypeDef",
    "CategoricalMeasureFieldTypeDef",
    "FormatConfigurationTypeDef",
    "BodySectionDynamicCategoryDimensionConfigurationUnionTypeDef",
    "BodySectionRepeatDimensionConfigurationOutputTypeDef",
    "BodySectionDynamicNumericDimensionConfigurationUnionTypeDef",
    "BarChartSortConfigurationOutputTypeDef",
    "BarChartSortConfigurationTypeDef",
    "BoxPlotSortConfigurationOutputTypeDef",
    "BoxPlotSortConfigurationTypeDef",
    "ComboChartSortConfigurationOutputTypeDef",
    "ComboChartSortConfigurationTypeDef",
    "FilledMapSortConfigurationOutputTypeDef",
    "FilledMapSortConfigurationTypeDef",
    "FunnelChartSortConfigurationOutputTypeDef",
    "FunnelChartSortConfigurationTypeDef",
    "HeatMapSortConfigurationOutputTypeDef",
    "HeatMapSortConfigurationTypeDef",
    "KPISortConfigurationOutputTypeDef",
    "KPISortConfigurationTypeDef",
    "LineChartSortConfigurationOutputTypeDef",
    "LineChartSortConfigurationTypeDef",
    "PieChartSortConfigurationOutputTypeDef",
    "PieChartSortConfigurationTypeDef",
    "RadarChartSortConfigurationOutputTypeDef",
    "RadarChartSortConfigurationTypeDef",
    "SankeyDiagramSortConfigurationOutputTypeDef",
    "SankeyDiagramSortConfigurationTypeDef",
    "TableSortConfigurationOutputTypeDef",
    "TableSortConfigurationTypeDef",
    "TreeMapSortConfigurationOutputTypeDef",
    "TreeMapSortConfigurationTypeDef",
    "WaterfallChartSortConfigurationOutputTypeDef",
    "WaterfallChartSortConfigurationTypeDef",
    "WordCloudSortConfigurationOutputTypeDef",
    "WordCloudSortConfigurationTypeDef",
    "PivotFieldSortOptionsOutputTypeDef",
    "PivotTableSortByUnionTypeDef",
    "FieldBasedTooltipOutputTypeDef",
    "FieldBasedTooltipTypeDef",
    "TopicDetailsOutputTypeDef",
    "DescribeAssetBundleImportJobResponseTypeDef",
    "DataSourceParametersUnionTypeDef",
    "SnapshotJobResultTypeDef",
    "CustomActionFilterOperationUnionTypeDef",
    "DefaultNewSheetConfigurationTypeDef",
    "BodySectionContentOutputTypeDef",
    "HeaderFooterSectionConfigurationOutputTypeDef",
    "FreeFormLayoutConfigurationUnionTypeDef",
    "FreeFormSectionLayoutConfigurationUnionTypeDef",
    "FilterScopeConfigurationUnionTypeDef",
    "SnapshotFileGroupUnionTypeDef",
    "ParameterDeclarationTypeDef",
    "DestinationParameterValueConfigurationUnionTypeDef",
    "DatasetParameterUnionTypeDef",
    "TransformOperationUnionTypeDef",
    "DateTimeHierarchyUnionTypeDef",
    "ExplicitHierarchyUnionTypeDef",
    "PredefinedHierarchyUnionTypeDef",
    "ForecastConfigurationUnionTypeDef",
    "AssetBundleImportJobOverridePermissionsTypeDef",
    "AxisDataOptionsUnionTypeDef",
    "ContributionAnalysisTimeRangesUnionTypeDef",
    "TopicFilterTypeDef",
    "DescribeDataSetResponseTypeDef",
    "VisualCustomActionOutputTypeDef",
    "PivotTableFieldOptionsTypeDef",
    "TopicVisualOutputTypeDef",
    "DefaultFilterControlOptionsTypeDef",
    "FilterControlTypeDef",
    "ParameterControlTypeDef",
    "DefaultFilterControlConfigurationOutputTypeDef",
    "TableFieldOptionTypeDef",
    "GeospatialPointStyleOptionsUnionTypeDef",
    "PivotTableTotalOptionsTypeDef",
    "GaugeChartConditionalFormattingOutputTypeDef",
    "KPIConditionalFormattingOutputTypeDef",
    "FilledMapConditionalFormattingOptionOutputTypeDef",
    "PivotTableConditionalFormattingOptionOutputTypeDef",
    "TableConditionalFormattingOptionOutputTypeDef",
    "ConditionalFormattingColorUnionTypeDef",
    "SheetControlLayoutTypeDef",
    "DescribeThemeResponseTypeDef",
    "ReferenceLineTypeDef",
    "DimensionFieldTypeDef",
    "MeasureFieldTypeDef",
    "ColumnConfigurationOutputTypeDef",
    "ColumnConfigurationTypeDef",
    "UnaggregatedFieldTypeDef",
    "BodySectionRepeatConfigurationOutputTypeDef",
    "BodySectionRepeatDimensionConfigurationTypeDef",
    "BarChartSortConfigurationUnionTypeDef",
    "BoxPlotSortConfigurationUnionTypeDef",
    "ComboChartSortConfigurationUnionTypeDef",
    "FilledMapSortConfigurationUnionTypeDef",
    "FunnelChartSortConfigurationUnionTypeDef",
    "HeatMapSortConfigurationUnionTypeDef",
    "KPISortConfigurationUnionTypeDef",
    "LineChartSortConfigurationUnionTypeDef",
    "PieChartSortConfigurationUnionTypeDef",
    "RadarChartSortConfigurationUnionTypeDef",
    "SankeyDiagramSortConfigurationUnionTypeDef",
    "TableSortConfigurationUnionTypeDef",
    "TreeMapSortConfigurationUnionTypeDef",
    "WaterfallChartSortConfigurationUnionTypeDef",
    "WordCloudSortConfigurationUnionTypeDef",
    "PivotTableSortConfigurationOutputTypeDef",
    "PivotFieldSortOptionsTypeDef",
    "TooltipOptionsOutputTypeDef",
    "FieldBasedTooltipUnionTypeDef",
    "DescribeTopicResponseTypeDef",
    "AssetBundleImportJobDataSourceOverrideParametersTypeDef",
    "CredentialPairTypeDef",
    "DescribeDashboardSnapshotJobResultResponseTypeDef",
    "AnalysisDefaultsTypeDef",
    "SectionLayoutConfigurationTypeDef",
    "SnapshotConfigurationTypeDef",
    "ParameterDeclarationUnionTypeDef",
    "SetParameterValueConfigurationTypeDef",
    "LogicalTableTypeDef",
    "ColumnHierarchyTypeDef",
    "AxisDisplayOptionsTypeDef",
    "TopicIRContributionAnalysisTypeDef",
    "TopicFilterUnionTypeDef",
    "CustomContentVisualOutputTypeDef",
    "EmptyVisualOutputTypeDef",
    "PivotTableFieldOptionsUnionTypeDef",
    "TopicReviewedAnswerTypeDef",
    "DefaultFilterControlOptionsUnionTypeDef",
    "FilterControlUnionTypeDef",
    "ParameterControlUnionTypeDef",
    "CategoryFilterOutputTypeDef",
    "CategoryInnerFilterOutputTypeDef",
    "NumericEqualityFilterOutputTypeDef",
    "NumericRangeFilterOutputTypeDef",
    "RelativeDatesFilterOutputTypeDef",
    "TimeEqualityFilterOutputTypeDef",
    "TimeRangeFilterOutputTypeDef",
    "TopBottomFilterOutputTypeDef",
    "TableFieldOptionsOutputTypeDef",
    "TableFieldOptionsTypeDef",
    "PivotTableTotalOptionsUnionTypeDef",
    "FilledMapConditionalFormattingOutputTypeDef",
    "PivotTableConditionalFormattingOutputTypeDef",
    "TableConditionalFormattingOutputTypeDef",
    "GaugeChartArcConditionalFormattingTypeDef",
    "GaugeChartPrimaryValueConditionalFormattingTypeDef",
    "KPIActualValueConditionalFormattingTypeDef",
    "KPIComparisonValueConditionalFormattingTypeDef",
    "KPIPrimaryValueConditionalFormattingTypeDef",
    "KPIProgressBarConditionalFormattingTypeDef",
    "ShapeConditionalFormatTypeDef",
    "TableRowConditionalFormattingTypeDef",
    "TextConditionalFormatTypeDef",
    "SheetControlLayoutUnionTypeDef",
    "UniqueValuesComputationTypeDef",
    "BarChartAggregatedFieldWellsOutputTypeDef",
    "BarChartAggregatedFieldWellsTypeDef",
    "BoxPlotAggregatedFieldWellsOutputTypeDef",
    "BoxPlotAggregatedFieldWellsTypeDef",
    "ComboChartAggregatedFieldWellsOutputTypeDef",
    "ComboChartAggregatedFieldWellsTypeDef",
    "FilledMapAggregatedFieldWellsOutputTypeDef",
    "FilledMapAggregatedFieldWellsTypeDef",
    "ForecastComputationTypeDef",
    "FunnelChartAggregatedFieldWellsOutputTypeDef",
    "FunnelChartAggregatedFieldWellsTypeDef",
    "GaugeChartFieldWellsOutputTypeDef",
    "GaugeChartFieldWellsTypeDef",
    "GeospatialMapAggregatedFieldWellsOutputTypeDef",
    "GeospatialMapAggregatedFieldWellsTypeDef",
    "GrowthRateComputationTypeDef",
    "HeatMapAggregatedFieldWellsOutputTypeDef",
    "HeatMapAggregatedFieldWellsTypeDef",
    "HistogramAggregatedFieldWellsOutputTypeDef",
    "HistogramAggregatedFieldWellsTypeDef",
    "KPIFieldWellsOutputTypeDef",
    "KPIFieldWellsTypeDef",
    "LineChartAggregatedFieldWellsOutputTypeDef",
    "LineChartAggregatedFieldWellsTypeDef",
    "MaximumMinimumComputationTypeDef",
    "MetricComparisonComputationTypeDef",
    "PeriodOverPeriodComputationTypeDef",
    "PeriodToDateComputationTypeDef",
    "PieChartAggregatedFieldWellsOutputTypeDef",
    "PieChartAggregatedFieldWellsTypeDef",
    "PivotTableAggregatedFieldWellsOutputTypeDef",
    "PivotTableAggregatedFieldWellsTypeDef",
    "RadarChartAggregatedFieldWellsOutputTypeDef",
    "RadarChartAggregatedFieldWellsTypeDef",
    "SankeyDiagramAggregatedFieldWellsOutputTypeDef",
    "SankeyDiagramAggregatedFieldWellsTypeDef",
    "ScatterPlotCategoricallyAggregatedFieldWellsOutputTypeDef",
    "ScatterPlotCategoricallyAggregatedFieldWellsTypeDef",
    "ScatterPlotUnaggregatedFieldWellsOutputTypeDef",
    "ScatterPlotUnaggregatedFieldWellsTypeDef",
    "TableAggregatedFieldWellsOutputTypeDef",
    "TableAggregatedFieldWellsTypeDef",
    "TopBottomMoversComputationTypeDef",
    "TopBottomRankedComputationTypeDef",
    "TotalAggregationComputationTypeDef",
    "TreeMapAggregatedFieldWellsOutputTypeDef",
    "TreeMapAggregatedFieldWellsTypeDef",
    "WaterfallChartAggregatedFieldWellsOutputTypeDef",
    "WaterfallChartAggregatedFieldWellsTypeDef",
    "WordCloudAggregatedFieldWellsOutputTypeDef",
    "WordCloudAggregatedFieldWellsTypeDef",
    "ColumnConfigurationUnionTypeDef",
    "TableUnaggregatedFieldWellsOutputTypeDef",
    "TableUnaggregatedFieldWellsTypeDef",
    "BodySectionConfigurationOutputTypeDef",
    "BodySectionRepeatDimensionConfigurationUnionTypeDef",
    "PivotFieldSortOptionsUnionTypeDef",
    "TooltipOptionsTypeDef",
    "AssetBundleImportJobDataSourceOverrideParametersUnionTypeDef",
    "DataSourceCredentialsTypeDef",
    "SectionLayoutConfigurationUnionTypeDef",
    "StartDashboardSnapshotJobRequestRequestTypeDef",
    "SetParameterValueConfigurationUnionTypeDef",
    "LogicalTableUnionTypeDef",
    "UpdateDataSetRequestRequestTypeDef",
    "ColumnHierarchyUnionTypeDef",
    "AxisDisplayOptionsUnionTypeDef",
    "TopicIRContributionAnalysisUnionTypeDef",
    "DatasetMetadataTypeDef",
    "ListTopicReviewedAnswersResponseTypeDef",
    "DefaultFilterControlConfigurationTypeDef",
    "InnerFilterOutputTypeDef",
    "TableFieldOptionsUnionTypeDef",
    "GaugeChartArcConditionalFormattingUnionTypeDef",
    "GaugeChartPrimaryValueConditionalFormattingUnionTypeDef",
    "KPIActualValueConditionalFormattingUnionTypeDef",
    "KPIComparisonValueConditionalFormattingUnionTypeDef",
    "KPIPrimaryValueConditionalFormattingUnionTypeDef",
    "KPIProgressBarConditionalFormattingUnionTypeDef",
    "ShapeConditionalFormatUnionTypeDef",
    "TableRowConditionalFormattingUnionTypeDef",
    "TextConditionalFormatUnionTypeDef",
    "BarChartFieldWellsOutputTypeDef",
    "BarChartAggregatedFieldWellsUnionTypeDef",
    "BoxPlotFieldWellsOutputTypeDef",
    "BoxPlotAggregatedFieldWellsUnionTypeDef",
    "ComboChartFieldWellsOutputTypeDef",
    "ComboChartAggregatedFieldWellsUnionTypeDef",
    "FilledMapFieldWellsOutputTypeDef",
    "FilledMapAggregatedFieldWellsUnionTypeDef",
    "FunnelChartFieldWellsOutputTypeDef",
    "FunnelChartAggregatedFieldWellsUnionTypeDef",
    "GaugeChartConfigurationOutputTypeDef",
    "GaugeChartFieldWellsUnionTypeDef",
    "GeospatialMapFieldWellsOutputTypeDef",
    "GeospatialMapAggregatedFieldWellsUnionTypeDef",
    "HeatMapFieldWellsOutputTypeDef",
    "HeatMapAggregatedFieldWellsUnionTypeDef",
    "HistogramFieldWellsOutputTypeDef",
    "HistogramAggregatedFieldWellsUnionTypeDef",
    "KPIConfigurationOutputTypeDef",
    "KPIFieldWellsUnionTypeDef",
    "LineChartFieldWellsOutputTypeDef",
    "LineChartAggregatedFieldWellsUnionTypeDef",
    "PieChartFieldWellsOutputTypeDef",
    "PieChartAggregatedFieldWellsUnionTypeDef",
    "PivotTableFieldWellsOutputTypeDef",
    "PivotTableAggregatedFieldWellsUnionTypeDef",
    "RadarChartFieldWellsOutputTypeDef",
    "RadarChartAggregatedFieldWellsUnionTypeDef",
    "SankeyDiagramFieldWellsOutputTypeDef",
    "SankeyDiagramAggregatedFieldWellsUnionTypeDef",
    "ScatterPlotCategoricallyAggregatedFieldWellsUnionTypeDef",
    "ScatterPlotFieldWellsOutputTypeDef",
    "ScatterPlotUnaggregatedFieldWellsUnionTypeDef",
    "TableAggregatedFieldWellsUnionTypeDef",
    "ComputationTypeDef",
    "TreeMapFieldWellsOutputTypeDef",
    "TreeMapAggregatedFieldWellsUnionTypeDef",
    "WaterfallChartFieldWellsOutputTypeDef",
    "WaterfallChartAggregatedFieldWellsUnionTypeDef",
    "WordCloudFieldWellsOutputTypeDef",
    "WordCloudAggregatedFieldWellsUnionTypeDef",
    "TableFieldWellsOutputTypeDef",
    "TableUnaggregatedFieldWellsUnionTypeDef",
    "SectionBasedLayoutConfigurationOutputTypeDef",
    "BodySectionRepeatConfigurationTypeDef",
    "PivotTableSortConfigurationTypeDef",
    "TooltipOptionsUnionTypeDef",
    "AssetBundleImportJobOverrideParametersTypeDef",
    "CreateDataSourceRequestRequestTypeDef",
    "UpdateDataSourceRequestRequestTypeDef",
    "BodySectionContentTypeDef",
    "HeaderFooterSectionConfigurationTypeDef",
    "CustomActionSetParametersOperationTypeDef",
    "CreateDataSetRequestRequestTypeDef",
    "LineSeriesAxisDisplayOptionsTypeDef",
    "TopicIRTypeDef",
    "DatasetMetadataUnionTypeDef",
    "DefaultFilterControlConfigurationUnionTypeDef",
    "NestedFilterOutputTypeDef",
    "GaugeChartConditionalFormattingOptionTypeDef",
    "KPIConditionalFormattingOptionTypeDef",
    "FilledMapShapeConditionalFormattingTypeDef",
    "PivotTableCellConditionalFormattingTypeDef",
    "TableCellConditionalFormattingTypeDef",
    "BarChartConfigurationOutputTypeDef",
    "BarChartFieldWellsTypeDef",
    "BoxPlotChartConfigurationOutputTypeDef",
    "BoxPlotFieldWellsTypeDef",
    "ComboChartConfigurationOutputTypeDef",
    "ComboChartFieldWellsTypeDef",
    "FilledMapConfigurationOutputTypeDef",
    "FilledMapFieldWellsTypeDef",
    "FunnelChartConfigurationOutputTypeDef",
    "FunnelChartFieldWellsTypeDef",
    "GaugeChartVisualOutputTypeDef",
    "GeospatialMapConfigurationOutputTypeDef",
    "GeospatialMapFieldWellsTypeDef",
    "HeatMapConfigurationOutputTypeDef",
    "HeatMapFieldWellsTypeDef",
    "HistogramConfigurationOutputTypeDef",
    "HistogramFieldWellsTypeDef",
    "KPIVisualOutputTypeDef",
    "KPIConfigurationTypeDef",
    "LineChartConfigurationOutputTypeDef",
    "LineChartFieldWellsTypeDef",
    "PieChartConfigurationOutputTypeDef",
    "PieChartFieldWellsTypeDef",
    "PivotTableConfigurationOutputTypeDef",
    "PivotTableFieldWellsTypeDef",
    "RadarChartConfigurationOutputTypeDef",
    "RadarChartFieldWellsTypeDef",
    "SankeyDiagramChartConfigurationOutputTypeDef",
    "SankeyDiagramFieldWellsTypeDef",
    "ScatterPlotConfigurationOutputTypeDef",
    "ScatterPlotFieldWellsTypeDef",
    "InsightConfigurationOutputTypeDef",
    "InsightConfigurationTypeDef",
    "TreeMapConfigurationOutputTypeDef",
    "TreeMapFieldWellsTypeDef",
    "WaterfallChartConfigurationOutputTypeDef",
    "WaterfallChartFieldWellsTypeDef",
    "WordCloudChartConfigurationOutputTypeDef",
    "WordCloudFieldWellsTypeDef",
    "TableConfigurationOutputTypeDef",
    "TableFieldWellsTypeDef",
    "LayoutConfigurationOutputTypeDef",
    "BodySectionRepeatConfigurationUnionTypeDef",
    "PivotTableSortConfigurationUnionTypeDef",
    "GaugeChartConfigurationTypeDef",
    "StartAssetBundleImportJobRequestRequestTypeDef",
    "BodySectionContentUnionTypeDef",
    "HeaderFooterSectionConfigurationUnionTypeDef",
    "CustomActionSetParametersOperationUnionTypeDef",
    "LineSeriesAxisDisplayOptionsUnionTypeDef",
    "TopicIRUnionTypeDef",
    "TopicDetailsTypeDef",
    "CategoryFilterTypeDef",
    "CategoryInnerFilterTypeDef",
    "NumericEqualityFilterTypeDef",
    "NumericRangeFilterTypeDef",
    "RelativeDatesFilterTypeDef",
    "TimeEqualityFilterTypeDef",
    "TimeRangeFilterTypeDef",
    "TopBottomFilterTypeDef",
    "FilterOutputTypeDef",
    "GaugeChartConditionalFormattingOptionUnionTypeDef",
    "KPIConditionalFormattingOptionUnionTypeDef",
    "FilledMapShapeConditionalFormattingUnionTypeDef",
    "PivotTableCellConditionalFormattingUnionTypeDef",
    "TableCellConditionalFormattingUnionTypeDef",
    "BarChartVisualOutputTypeDef",
    "BarChartFieldWellsUnionTypeDef",
    "BoxPlotVisualOutputTypeDef",
    "BoxPlotFieldWellsUnionTypeDef",
    "ComboChartVisualOutputTypeDef",
    "ComboChartFieldWellsUnionTypeDef",
    "FilledMapVisualOutputTypeDef",
    "FilledMapFieldWellsUnionTypeDef",
    "FunnelChartVisualOutputTypeDef",
    "FunnelChartFieldWellsUnionTypeDef",
    "GeospatialMapVisualOutputTypeDef",
    "GeospatialMapFieldWellsUnionTypeDef",
    "HeatMapVisualOutputTypeDef",
    "HeatMapFieldWellsUnionTypeDef",
    "HistogramVisualOutputTypeDef",
    "HistogramFieldWellsUnionTypeDef",
    "KPIConfigurationUnionTypeDef",
    "LineChartVisualOutputTypeDef",
    "LineChartFieldWellsUnionTypeDef",
    "PieChartVisualOutputTypeDef",
    "PieChartFieldWellsUnionTypeDef",
    "PivotTableVisualOutputTypeDef",
    "PivotTableFieldWellsUnionTypeDef",
    "RadarChartVisualOutputTypeDef",
    "RadarChartFieldWellsUnionTypeDef",
    "SankeyDiagramVisualOutputTypeDef",
    "SankeyDiagramFieldWellsUnionTypeDef",
    "ScatterPlotVisualOutputTypeDef",
    "ScatterPlotFieldWellsUnionTypeDef",
    "InsightVisualOutputTypeDef",
    "InsightConfigurationUnionTypeDef",
    "TreeMapVisualOutputTypeDef",
    "TreeMapFieldWellsUnionTypeDef",
    "WaterfallVisualOutputTypeDef",
    "WaterfallChartFieldWellsUnionTypeDef",
    "WordCloudVisualOutputTypeDef",
    "WordCloudFieldWellsUnionTypeDef",
    "TableVisualOutputTypeDef",
    "TableFieldWellsUnionTypeDef",
    "LayoutOutputTypeDef",
    "GaugeChartConfigurationUnionTypeDef",
    "BodySectionConfigurationTypeDef",
    "VisualCustomActionOperationTypeDef",
    "TopicVisualTypeDef",
    "CreateTopicRequestRequestTypeDef",
    "UpdateTopicRequestRequestTypeDef",
    "CategoryFilterUnionTypeDef",
    "CategoryInnerFilterUnionTypeDef",
    "NumericEqualityFilterUnionTypeDef",
    "NumericRangeFilterUnionTypeDef",
    "RelativeDatesFilterUnionTypeDef",
    "TimeEqualityFilterUnionTypeDef",
    "TimeRangeFilterUnionTypeDef",
    "TopBottomFilterUnionTypeDef",
    "FilterGroupOutputTypeDef",
    "GaugeChartConditionalFormattingTypeDef",
    "KPIConditionalFormattingTypeDef",
    "FilledMapConditionalFormattingOptionTypeDef",
    "PivotTableConditionalFormattingOptionTypeDef",
    "TableConditionalFormattingOptionTypeDef",
    "BarChartConfigurationTypeDef",
    "BoxPlotChartConfigurationTypeDef",
    "ComboChartConfigurationTypeDef",
    "FilledMapConfigurationTypeDef",
    "FunnelChartConfigurationTypeDef",
    "GeospatialMapConfigurationTypeDef",
    "HeatMapConfigurationTypeDef",
    "HistogramConfigurationTypeDef",
    "LineChartConfigurationTypeDef",
    "PieChartConfigurationTypeDef",
    "PivotTableConfigurationTypeDef",
    "RadarChartConfigurationTypeDef",
    "SankeyDiagramChartConfigurationTypeDef",
    "ScatterPlotConfigurationTypeDef",
    "TreeMapConfigurationTypeDef",
    "WaterfallChartConfigurationTypeDef",
    "WordCloudChartConfigurationTypeDef",
    "VisualOutputTypeDef",
    "TableConfigurationTypeDef",
    "BodySectionConfigurationUnionTypeDef",
    "VisualCustomActionOperationUnionTypeDef",
    "TopicVisualUnionTypeDef",
    "InnerFilterTypeDef",
    "GaugeChartConditionalFormattingUnionTypeDef",
    "KPIConditionalFormattingUnionTypeDef",
    "FilledMapConditionalFormattingOptionUnionTypeDef",
    "PivotTableConditionalFormattingOptionUnionTypeDef",
    "TableConditionalFormattingOptionUnionTypeDef",
    "BarChartConfigurationUnionTypeDef",
    "BoxPlotChartConfigurationUnionTypeDef",
    "ComboChartConfigurationUnionTypeDef",
    "FilledMapConfigurationUnionTypeDef",
    "FunnelChartConfigurationUnionTypeDef",
    "GeospatialMapConfigurationUnionTypeDef",
    "HeatMapConfigurationUnionTypeDef",
    "HistogramConfigurationUnionTypeDef",
    "LineChartConfigurationUnionTypeDef",
    "PieChartConfigurationUnionTypeDef",
    "PivotTableConfigurationUnionTypeDef",
    "RadarChartConfigurationUnionTypeDef",
    "SankeyDiagramChartConfigurationUnionTypeDef",
    "ScatterPlotConfigurationUnionTypeDef",
    "TreeMapConfigurationUnionTypeDef",
    "WaterfallChartConfigurationUnionTypeDef",
    "WordCloudChartConfigurationUnionTypeDef",
    "SheetDefinitionOutputTypeDef",
    "TableConfigurationUnionTypeDef",
    "SectionBasedLayoutConfigurationTypeDef",
    "VisualCustomActionTypeDef",
    "CreateTopicReviewedAnswerTypeDef",
    "InnerFilterUnionTypeDef",
    "FilledMapConditionalFormattingTypeDef",
    "PivotTableConditionalFormattingTypeDef",
    "TableConditionalFormattingTypeDef",
    "AnalysisDefinitionOutputTypeDef",
    "DashboardVersionDefinitionOutputTypeDef",
    "TemplateVersionDefinitionOutputTypeDef",
    "SectionBasedLayoutConfigurationUnionTypeDef",
    "BoxPlotVisualTypeDef",
    "ComboChartVisualTypeDef",
    "CustomContentVisualTypeDef",
    "EmptyVisualTypeDef",
    "FunnelChartVisualTypeDef",
    "GaugeChartVisualTypeDef",
    "GeospatialMapVisualTypeDef",
    "HeatMapVisualTypeDef",
    "HistogramVisualTypeDef",
    "InsightVisualTypeDef",
    "KPIVisualTypeDef",
    "LineChartVisualTypeDef",
    "PieChartVisualTypeDef",
    "RadarChartVisualTypeDef",
    "SankeyDiagramVisualTypeDef",
    "ScatterPlotVisualTypeDef",
    "TreeMapVisualTypeDef",
    "VisualCustomActionUnionTypeDef",
    "WaterfallVisualTypeDef",
    "WordCloudVisualTypeDef",
    "BatchCreateTopicReviewedAnswerRequestRequestTypeDef",
    "NestedFilterTypeDef",
    "FilledMapConditionalFormattingUnionTypeDef",
    "PivotTableConditionalFormattingUnionTypeDef",
    "TableConditionalFormattingUnionTypeDef",
    "DescribeAnalysisDefinitionResponseTypeDef",
    "DescribeDashboardDefinitionResponseTypeDef",
    "DescribeTemplateDefinitionResponseTypeDef",
    "LayoutConfigurationTypeDef",
    "BoxPlotVisualUnionTypeDef",
    "ComboChartVisualUnionTypeDef",
    "CustomContentVisualUnionTypeDef",
    "EmptyVisualUnionTypeDef",
    "FunnelChartVisualUnionTypeDef",
    "GaugeChartVisualUnionTypeDef",
    "GeospatialMapVisualUnionTypeDef",
    "HeatMapVisualUnionTypeDef",
    "HistogramVisualUnionTypeDef",
    "InsightVisualUnionTypeDef",
    "KPIVisualUnionTypeDef",
    "LineChartVisualUnionTypeDef",
    "PieChartVisualUnionTypeDef",
    "RadarChartVisualUnionTypeDef",
    "SankeyDiagramVisualUnionTypeDef",
    "ScatterPlotVisualUnionTypeDef",
    "TreeMapVisualUnionTypeDef",
    "BarChartVisualTypeDef",
    "WaterfallVisualUnionTypeDef",
    "WordCloudVisualUnionTypeDef",
    "NestedFilterUnionTypeDef",
    "FilledMapVisualTypeDef",
    "PivotTableVisualTypeDef",
    "TableVisualTypeDef",
    "LayoutConfigurationUnionTypeDef",
    "BarChartVisualUnionTypeDef",
    "FilterTypeDef",
    "FilledMapVisualUnionTypeDef",
    "PivotTableVisualUnionTypeDef",
    "TableVisualUnionTypeDef",
    "LayoutTypeDef",
    "FilterUnionTypeDef",
    "VisualTypeDef",
    "LayoutUnionTypeDef",
    "FilterGroupTypeDef",
    "VisualUnionTypeDef",
    "FilterGroupUnionTypeDef",
    "SheetDefinitionTypeDef",
    "SheetDefinitionUnionTypeDef",
    "AnalysisDefinitionTypeDef",
    "DashboardVersionDefinitionTypeDef",
    "TemplateVersionDefinitionTypeDef",
    "CreateAnalysisRequestRequestTypeDef",
    "UpdateAnalysisRequestRequestTypeDef",
    "CreateDashboardRequestRequestTypeDef",
    "UpdateDashboardRequestRequestTypeDef",
    "CreateTemplateRequestRequestTypeDef",
    "UpdateTemplateRequestRequestTypeDef",
)

AccountCustomizationTypeDef = TypedDict(
    "AccountCustomizationTypeDef",
    {
        "DefaultTheme": NotRequired[str],
        "DefaultEmailCustomizationTemplate": NotRequired[str],
    },
)
AccountInfoTypeDef = TypedDict(
    "AccountInfoTypeDef",
    {
        "AccountName": NotRequired[str],
        "Edition": NotRequired[EditionType],
        "NotificationEmail": NotRequired[str],
        "AuthenticationType": NotRequired[str],
        "AccountSubscriptionStatus": NotRequired[str],
        "IAMIdentityCenterInstanceArn": NotRequired[str],
    },
)
AccountSettingsTypeDef = TypedDict(
    "AccountSettingsTypeDef",
    {
        "AccountName": NotRequired[str],
        "Edition": NotRequired[EditionType],
        "DefaultNamespace": NotRequired[str],
        "NotificationEmail": NotRequired[str],
        "PublicSharingEnabled": NotRequired[bool],
        "TerminationProtectionEnabled": NotRequired[bool],
    },
)
ActiveIAMPolicyAssignmentTypeDef = TypedDict(
    "ActiveIAMPolicyAssignmentTypeDef",
    {
        "AssignmentName": NotRequired[str],
        "PolicyArn": NotRequired[str],
    },
)
AdHocFilteringOptionTypeDef = TypedDict(
    "AdHocFilteringOptionTypeDef",
    {
        "AvailabilityStatus": NotRequired[DashboardBehaviorType],
    },
)
AggFunctionOutputTypeDef = TypedDict(
    "AggFunctionOutputTypeDef",
    {
        "Aggregation": NotRequired[AggTypeType],
        "AggregationFunctionParameters": NotRequired[Dict[str, str]],
        "Period": NotRequired[TopicTimeGranularityType],
        "PeriodField": NotRequired[str],
    },
)
AggFunctionTypeDef = TypedDict(
    "AggFunctionTypeDef",
    {
        "Aggregation": NotRequired[AggTypeType],
        "AggregationFunctionParameters": NotRequired[Mapping[str, str]],
        "Period": NotRequired[TopicTimeGranularityType],
        "PeriodField": NotRequired[str],
    },
)
AttributeAggregationFunctionTypeDef = TypedDict(
    "AttributeAggregationFunctionTypeDef",
    {
        "SimpleAttributeAggregation": NotRequired[Literal["UNIQUE_VALUE"]],
        "ValueForMultipleValues": NotRequired[str],
    },
)
AggregationPartitionByTypeDef = TypedDict(
    "AggregationPartitionByTypeDef",
    {
        "FieldName": NotRequired[str],
        "TimeGranularity": NotRequired[TimeGranularityType],
    },
)
ColumnIdentifierTypeDef = TypedDict(
    "ColumnIdentifierTypeDef",
    {
        "DataSetIdentifier": str,
        "ColumnName": str,
    },
)
AmazonElasticsearchParametersTypeDef = TypedDict(
    "AmazonElasticsearchParametersTypeDef",
    {
        "Domain": str,
    },
)
AmazonOpenSearchParametersTypeDef = TypedDict(
    "AmazonOpenSearchParametersTypeDef",
    {
        "Domain": str,
    },
)
AssetOptionsTypeDef = TypedDict(
    "AssetOptionsTypeDef",
    {
        "Timezone": NotRequired[str],
        "WeekStart": NotRequired[DayOfTheWeekType],
    },
)
CalculatedFieldTypeDef = TypedDict(
    "CalculatedFieldTypeDef",
    {
        "DataSetIdentifier": str,
        "Name": str,
        "Expression": str,
    },
)
DataSetIdentifierDeclarationTypeDef = TypedDict(
    "DataSetIdentifierDeclarationTypeDef",
    {
        "Identifier": str,
        "DataSetArn": str,
    },
)
QueryExecutionOptionsTypeDef = TypedDict(
    "QueryExecutionOptionsTypeDef",
    {
        "QueryExecutionMode": NotRequired[QueryExecutionModeType],
    },
)
EntityTypeDef = TypedDict(
    "EntityTypeDef",
    {
        "Path": NotRequired[str],
    },
)
AnalysisSearchFilterTypeDef = TypedDict(
    "AnalysisSearchFilterTypeDef",
    {
        "Operator": NotRequired[FilterOperatorType],
        "Name": NotRequired[AnalysisFilterAttributeType],
        "Value": NotRequired[str],
    },
)
DataSetReferenceTypeDef = TypedDict(
    "DataSetReferenceTypeDef",
    {
        "DataSetPlaceholder": str,
        "DataSetArn": str,
    },
)
AnalysisSummaryTypeDef = TypedDict(
    "AnalysisSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "AnalysisId": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired[ResourceStatusType],
        "CreatedTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
    },
)
SheetTypeDef = TypedDict(
    "SheetTypeDef",
    {
        "SheetId": NotRequired[str],
        "Name": NotRequired[str],
    },
)
AnchorDateConfigurationTypeDef = TypedDict(
    "AnchorDateConfigurationTypeDef",
    {
        "AnchorOption": NotRequired[Literal["NOW"]],
        "ParameterName": NotRequired[str],
    },
)
AnchorTypeDef = TypedDict(
    "AnchorTypeDef",
    {
        "AnchorType": NotRequired[Literal["TODAY"]],
        "TimeGranularity": NotRequired[TimeGranularityType],
        "Offset": NotRequired[int],
    },
)
SharedViewConfigurationsTypeDef = TypedDict(
    "SharedViewConfigurationsTypeDef",
    {
        "Enabled": bool,
    },
)
DashboardVisualIdTypeDef = TypedDict(
    "DashboardVisualIdTypeDef",
    {
        "DashboardId": str,
        "SheetId": str,
        "VisualId": str,
    },
)
AnonymousUserGenerativeQnAEmbeddingConfigurationTypeDef = TypedDict(
    "AnonymousUserGenerativeQnAEmbeddingConfigurationTypeDef",
    {
        "InitialTopicId": str,
    },
)
AnonymousUserQSearchBarEmbeddingConfigurationTypeDef = TypedDict(
    "AnonymousUserQSearchBarEmbeddingConfigurationTypeDef",
    {
        "InitialTopicId": str,
    },
)
ArcAxisDisplayRangeTypeDef = TypedDict(
    "ArcAxisDisplayRangeTypeDef",
    {
        "Min": NotRequired[float],
        "Max": NotRequired[float],
    },
)
ArcConfigurationTypeDef = TypedDict(
    "ArcConfigurationTypeDef",
    {
        "ArcAngle": NotRequired[float],
        "ArcThickness": NotRequired[ArcThicknessOptionsType],
    },
)
ArcOptionsTypeDef = TypedDict(
    "ArcOptionsTypeDef",
    {
        "ArcThickness": NotRequired[ArcThicknessType],
    },
)
AssetBundleExportJobAnalysisOverridePropertiesOutputTypeDef = TypedDict(
    "AssetBundleExportJobAnalysisOverridePropertiesOutputTypeDef",
    {
        "Arn": str,
        "Properties": List[Literal["Name"]],
    },
)
AssetBundleExportJobDashboardOverridePropertiesOutputTypeDef = TypedDict(
    "AssetBundleExportJobDashboardOverridePropertiesOutputTypeDef",
    {
        "Arn": str,
        "Properties": List[Literal["Name"]],
    },
)
AssetBundleExportJobDataSetOverridePropertiesOutputTypeDef = TypedDict(
    "AssetBundleExportJobDataSetOverridePropertiesOutputTypeDef",
    {
        "Arn": str,
        "Properties": List[Literal["Name"]],
    },
)
AssetBundleExportJobDataSourceOverridePropertiesOutputTypeDef = TypedDict(
    "AssetBundleExportJobDataSourceOverridePropertiesOutputTypeDef",
    {
        "Arn": str,
        "Properties": List[AssetBundleExportJobDataSourcePropertyToOverrideType],
    },
)
AssetBundleExportJobFolderOverridePropertiesOutputTypeDef = TypedDict(
    "AssetBundleExportJobFolderOverridePropertiesOutputTypeDef",
    {
        "Arn": str,
        "Properties": List[AssetBundleExportJobFolderPropertyToOverrideType],
    },
)
AssetBundleExportJobRefreshScheduleOverridePropertiesOutputTypeDef = TypedDict(
    "AssetBundleExportJobRefreshScheduleOverridePropertiesOutputTypeDef",
    {
        "Arn": str,
        "Properties": List[Literal["StartAfterDateTime"]],
    },
)
AssetBundleExportJobResourceIdOverrideConfigurationTypeDef = TypedDict(
    "AssetBundleExportJobResourceIdOverrideConfigurationTypeDef",
    {
        "PrefixForAllResources": NotRequired[bool],
    },
)
AssetBundleExportJobThemeOverridePropertiesOutputTypeDef = TypedDict(
    "AssetBundleExportJobThemeOverridePropertiesOutputTypeDef",
    {
        "Arn": str,
        "Properties": List[Literal["Name"]],
    },
)
AssetBundleExportJobVPCConnectionOverridePropertiesOutputTypeDef = TypedDict(
    "AssetBundleExportJobVPCConnectionOverridePropertiesOutputTypeDef",
    {
        "Arn": str,
        "Properties": List[AssetBundleExportJobVPCConnectionPropertyToOverrideType],
    },
)
AssetBundleExportJobAnalysisOverridePropertiesTypeDef = TypedDict(
    "AssetBundleExportJobAnalysisOverridePropertiesTypeDef",
    {
        "Arn": str,
        "Properties": Sequence[Literal["Name"]],
    },
)
AssetBundleExportJobDashboardOverridePropertiesTypeDef = TypedDict(
    "AssetBundleExportJobDashboardOverridePropertiesTypeDef",
    {
        "Arn": str,
        "Properties": Sequence[Literal["Name"]],
    },
)
AssetBundleExportJobDataSetOverridePropertiesTypeDef = TypedDict(
    "AssetBundleExportJobDataSetOverridePropertiesTypeDef",
    {
        "Arn": str,
        "Properties": Sequence[Literal["Name"]],
    },
)
AssetBundleExportJobDataSourceOverridePropertiesTypeDef = TypedDict(
    "AssetBundleExportJobDataSourceOverridePropertiesTypeDef",
    {
        "Arn": str,
        "Properties": Sequence[AssetBundleExportJobDataSourcePropertyToOverrideType],
    },
)
AssetBundleExportJobErrorTypeDef = TypedDict(
    "AssetBundleExportJobErrorTypeDef",
    {
        "Arn": NotRequired[str],
        "Type": NotRequired[str],
        "Message": NotRequired[str],
    },
)
AssetBundleExportJobFolderOverridePropertiesTypeDef = TypedDict(
    "AssetBundleExportJobFolderOverridePropertiesTypeDef",
    {
        "Arn": str,
        "Properties": Sequence[AssetBundleExportJobFolderPropertyToOverrideType],
    },
)
AssetBundleExportJobRefreshScheduleOverridePropertiesTypeDef = TypedDict(
    "AssetBundleExportJobRefreshScheduleOverridePropertiesTypeDef",
    {
        "Arn": str,
        "Properties": Sequence[Literal["StartAfterDateTime"]],
    },
)
AssetBundleExportJobSummaryTypeDef = TypedDict(
    "AssetBundleExportJobSummaryTypeDef",
    {
        "JobStatus": NotRequired[AssetBundleExportJobStatusType],
        "Arn": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "AssetBundleExportJobId": NotRequired[str],
        "IncludeAllDependencies": NotRequired[bool],
        "ExportFormat": NotRequired[AssetBundleExportFormatType],
        "IncludePermissions": NotRequired[bool],
        "IncludeTags": NotRequired[bool],
    },
)
AssetBundleExportJobThemeOverridePropertiesTypeDef = TypedDict(
    "AssetBundleExportJobThemeOverridePropertiesTypeDef",
    {
        "Arn": str,
        "Properties": Sequence[Literal["Name"]],
    },
)
AssetBundleExportJobVPCConnectionOverridePropertiesTypeDef = TypedDict(
    "AssetBundleExportJobVPCConnectionOverridePropertiesTypeDef",
    {
        "Arn": str,
        "Properties": Sequence[AssetBundleExportJobVPCConnectionPropertyToOverrideType],
    },
)
AssetBundleExportJobValidationStrategyTypeDef = TypedDict(
    "AssetBundleExportJobValidationStrategyTypeDef",
    {
        "StrictModeForAllResources": NotRequired[bool],
    },
)
AssetBundleExportJobWarningTypeDef = TypedDict(
    "AssetBundleExportJobWarningTypeDef",
    {
        "Arn": NotRequired[str],
        "Message": NotRequired[str],
    },
)
AssetBundleImportJobAnalysisOverrideParametersTypeDef = TypedDict(
    "AssetBundleImportJobAnalysisOverrideParametersTypeDef",
    {
        "AnalysisId": str,
        "Name": NotRequired[str],
    },
)
AssetBundleResourcePermissionsOutputTypeDef = TypedDict(
    "AssetBundleResourcePermissionsOutputTypeDef",
    {
        "Principals": List[str],
        "Actions": List[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
AssetBundleImportJobDashboardOverrideParametersTypeDef = TypedDict(
    "AssetBundleImportJobDashboardOverrideParametersTypeDef",
    {
        "DashboardId": str,
        "Name": NotRequired[str],
    },
)
AssetBundleImportJobDataSetOverrideParametersTypeDef = TypedDict(
    "AssetBundleImportJobDataSetOverrideParametersTypeDef",
    {
        "DataSetId": str,
        "Name": NotRequired[str],
    },
)
AssetBundleImportJobDataSourceCredentialPairTypeDef = TypedDict(
    "AssetBundleImportJobDataSourceCredentialPairTypeDef",
    {
        "Username": str,
        "Password": str,
    },
)
SslPropertiesTypeDef = TypedDict(
    "SslPropertiesTypeDef",
    {
        "DisableSsl": NotRequired[bool],
    },
)
VpcConnectionPropertiesTypeDef = TypedDict(
    "VpcConnectionPropertiesTypeDef",
    {
        "VpcConnectionArn": str,
    },
)
AssetBundleImportJobErrorTypeDef = TypedDict(
    "AssetBundleImportJobErrorTypeDef",
    {
        "Arn": NotRequired[str],
        "Type": NotRequired[str],
        "Message": NotRequired[str],
    },
)
AssetBundleImportJobFolderOverrideParametersTypeDef = TypedDict(
    "AssetBundleImportJobFolderOverrideParametersTypeDef",
    {
        "FolderId": str,
        "Name": NotRequired[str],
        "ParentFolderArn": NotRequired[str],
    },
)
AssetBundleImportJobRefreshScheduleOverrideParametersOutputTypeDef = TypedDict(
    "AssetBundleImportJobRefreshScheduleOverrideParametersOutputTypeDef",
    {
        "DataSetId": str,
        "ScheduleId": str,
        "StartAfterDateTime": NotRequired[datetime],
    },
)
AssetBundleImportJobResourceIdOverrideConfigurationTypeDef = TypedDict(
    "AssetBundleImportJobResourceIdOverrideConfigurationTypeDef",
    {
        "PrefixForAllResources": NotRequired[str],
    },
)
AssetBundleImportJobThemeOverrideParametersTypeDef = TypedDict(
    "AssetBundleImportJobThemeOverrideParametersTypeDef",
    {
        "ThemeId": str,
        "Name": NotRequired[str],
    },
)
AssetBundleImportJobVPCConnectionOverrideParametersOutputTypeDef = TypedDict(
    "AssetBundleImportJobVPCConnectionOverrideParametersOutputTypeDef",
    {
        "VPCConnectionId": str,
        "Name": NotRequired[str],
        "SubnetIds": NotRequired[List[str]],
        "SecurityGroupIds": NotRequired[List[str]],
        "DnsResolvers": NotRequired[List[str]],
        "RoleArn": NotRequired[str],
    },
)
AssetBundleImportJobOverrideValidationStrategyTypeDef = TypedDict(
    "AssetBundleImportJobOverrideValidationStrategyTypeDef",
    {
        "StrictModeForAllResources": NotRequired[bool],
    },
)
TimestampTypeDef = Union[datetime, str]
AssetBundleImportJobSummaryTypeDef = TypedDict(
    "AssetBundleImportJobSummaryTypeDef",
    {
        "JobStatus": NotRequired[AssetBundleImportJobStatusType],
        "Arn": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "AssetBundleImportJobId": NotRequired[str],
        "FailureAction": NotRequired[AssetBundleImportFailureActionType],
    },
)
AssetBundleImportJobVPCConnectionOverrideParametersTypeDef = TypedDict(
    "AssetBundleImportJobVPCConnectionOverrideParametersTypeDef",
    {
        "VPCConnectionId": str,
        "Name": NotRequired[str],
        "SubnetIds": NotRequired[Sequence[str]],
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "DnsResolvers": NotRequired[Sequence[str]],
        "RoleArn": NotRequired[str],
    },
)
AssetBundleImportJobWarningTypeDef = TypedDict(
    "AssetBundleImportJobWarningTypeDef",
    {
        "Arn": NotRequired[str],
        "Message": NotRequired[str],
    },
)
AssetBundleImportSourceDescriptionTypeDef = TypedDict(
    "AssetBundleImportSourceDescriptionTypeDef",
    {
        "Body": NotRequired[str],
        "S3Uri": NotRequired[str],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
AssetBundleResourcePermissionsTypeDef = TypedDict(
    "AssetBundleResourcePermissionsTypeDef",
    {
        "Principals": Sequence[str],
        "Actions": Sequence[str],
    },
)
AthenaParametersTypeDef = TypedDict(
    "AthenaParametersTypeDef",
    {
        "WorkGroup": NotRequired[str],
        "RoleArn": NotRequired[str],
    },
)
AuroraParametersTypeDef = TypedDict(
    "AuroraParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)
AuroraPostgreSqlParametersTypeDef = TypedDict(
    "AuroraPostgreSqlParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)
AuthorizedTargetsByServiceTypeDef = TypedDict(
    "AuthorizedTargetsByServiceTypeDef",
    {
        "Service": NotRequired[Literal["REDSHIFT"]],
        "AuthorizedTargets": NotRequired[List[str]],
    },
)
AwsIotAnalyticsParametersTypeDef = TypedDict(
    "AwsIotAnalyticsParametersTypeDef",
    {
        "DataSetName": str,
    },
)
DateAxisOptionsTypeDef = TypedDict(
    "DateAxisOptionsTypeDef",
    {
        "MissingDateVisibility": NotRequired[VisibilityType],
    },
)
AxisDisplayMinMaxRangeTypeDef = TypedDict(
    "AxisDisplayMinMaxRangeTypeDef",
    {
        "Minimum": NotRequired[float],
        "Maximum": NotRequired[float],
    },
)
AxisLinearScaleTypeDef = TypedDict(
    "AxisLinearScaleTypeDef",
    {
        "StepCount": NotRequired[int],
        "StepSize": NotRequired[float],
    },
)
AxisLogarithmicScaleTypeDef = TypedDict(
    "AxisLogarithmicScaleTypeDef",
    {
        "Base": NotRequired[float],
    },
)
ItemsLimitConfigurationTypeDef = TypedDict(
    "ItemsLimitConfigurationTypeDef",
    {
        "ItemsLimit": NotRequired[int],
        "OtherCategories": NotRequired[OtherCategoriesType],
    },
)
InvalidTopicReviewedAnswerTypeDef = TypedDict(
    "InvalidTopicReviewedAnswerTypeDef",
    {
        "AnswerId": NotRequired[str],
        "Error": NotRequired[ReviewedAnswerErrorCodeType],
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
SucceededTopicReviewedAnswerTypeDef = TypedDict(
    "SucceededTopicReviewedAnswerTypeDef",
    {
        "AnswerId": NotRequired[str],
    },
)
BatchDeleteTopicReviewedAnswerRequestRequestTypeDef = TypedDict(
    "BatchDeleteTopicReviewedAnswerRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TopicId": str,
        "AnswerIds": NotRequired[Sequence[str]],
    },
)
BigQueryParametersTypeDef = TypedDict(
    "BigQueryParametersTypeDef",
    {
        "ProjectId": str,
        "DataSetRegion": NotRequired[str],
    },
)
BinCountOptionsTypeDef = TypedDict(
    "BinCountOptionsTypeDef",
    {
        "Value": NotRequired[int],
    },
)
BinWidthOptionsTypeDef = TypedDict(
    "BinWidthOptionsTypeDef",
    {
        "Value": NotRequired[float],
        "BinCountLimit": NotRequired[int],
    },
)
SectionAfterPageBreakTypeDef = TypedDict(
    "SectionAfterPageBreakTypeDef",
    {
        "Status": NotRequired[SectionPageBreakStatusType],
    },
)
BookmarksConfigurationsTypeDef = TypedDict(
    "BookmarksConfigurationsTypeDef",
    {
        "Enabled": bool,
    },
)
BorderStyleTypeDef = TypedDict(
    "BorderStyleTypeDef",
    {
        "Show": NotRequired[bool],
    },
)
BoxPlotStyleOptionsTypeDef = TypedDict(
    "BoxPlotStyleOptionsTypeDef",
    {
        "FillStyle": NotRequired[BoxPlotFillStyleType],
    },
)
PaginationConfigurationTypeDef = TypedDict(
    "PaginationConfigurationTypeDef",
    {
        "PageSize": int,
        "PageNumber": int,
    },
)
CalculatedColumnTypeDef = TypedDict(
    "CalculatedColumnTypeDef",
    {
        "ColumnName": str,
        "ColumnId": str,
        "Expression": str,
    },
)
CalculatedMeasureFieldTypeDef = TypedDict(
    "CalculatedMeasureFieldTypeDef",
    {
        "FieldId": str,
        "Expression": str,
    },
)
CancelIngestionRequestRequestTypeDef = TypedDict(
    "CancelIngestionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
        "IngestionId": str,
    },
)
CastColumnTypeOperationTypeDef = TypedDict(
    "CastColumnTypeOperationTypeDef",
    {
        "ColumnName": str,
        "NewColumnType": ColumnDataTypeType,
        "SubType": NotRequired[ColumnDataSubTypeType],
        "Format": NotRequired[str],
    },
)
CustomFilterConfigurationTypeDef = TypedDict(
    "CustomFilterConfigurationTypeDef",
    {
        "MatchOperator": CategoryFilterMatchOperatorType,
        "NullOption": FilterNullOptionType,
        "CategoryValue": NotRequired[str],
        "SelectAllOptions": NotRequired[Literal["FILTER_ALL_VALUES"]],
        "ParameterName": NotRequired[str],
    },
)
CustomFilterListConfigurationOutputTypeDef = TypedDict(
    "CustomFilterListConfigurationOutputTypeDef",
    {
        "MatchOperator": CategoryFilterMatchOperatorType,
        "NullOption": FilterNullOptionType,
        "CategoryValues": NotRequired[List[str]],
        "SelectAllOptions": NotRequired[Literal["FILTER_ALL_VALUES"]],
    },
)
FilterListConfigurationOutputTypeDef = TypedDict(
    "FilterListConfigurationOutputTypeDef",
    {
        "MatchOperator": CategoryFilterMatchOperatorType,
        "CategoryValues": NotRequired[List[str]],
        "SelectAllOptions": NotRequired[Literal["FILTER_ALL_VALUES"]],
        "NullOption": NotRequired[FilterNullOptionType],
    },
)
CellValueSynonymOutputTypeDef = TypedDict(
    "CellValueSynonymOutputTypeDef",
    {
        "CellValue": NotRequired[str],
        "Synonyms": NotRequired[List[str]],
    },
)
CellValueSynonymTypeDef = TypedDict(
    "CellValueSynonymTypeDef",
    {
        "CellValue": NotRequired[str],
        "Synonyms": NotRequired[Sequence[str]],
    },
)
SimpleClusterMarkerTypeDef = TypedDict(
    "SimpleClusterMarkerTypeDef",
    {
        "Color": NotRequired[str],
    },
)
CollectiveConstantEntryTypeDef = TypedDict(
    "CollectiveConstantEntryTypeDef",
    {
        "ConstantType": NotRequired[ConstantTypeType],
        "Value": NotRequired[str],
    },
)
CollectiveConstantOutputTypeDef = TypedDict(
    "CollectiveConstantOutputTypeDef",
    {
        "ValueList": NotRequired[List[str]],
    },
)
CollectiveConstantTypeDef = TypedDict(
    "CollectiveConstantTypeDef",
    {
        "ValueList": NotRequired[Sequence[str]],
    },
)
DataColorTypeDef = TypedDict(
    "DataColorTypeDef",
    {
        "Color": NotRequired[str],
        "DataValue": NotRequired[float],
    },
)
CustomColorTypeDef = TypedDict(
    "CustomColorTypeDef",
    {
        "Color": str,
        "FieldValue": NotRequired[str],
        "SpecialValue": NotRequired[SpecialValueType],
    },
)
ColumnDescriptionTypeDef = TypedDict(
    "ColumnDescriptionTypeDef",
    {
        "Text": NotRequired[str],
    },
)
ColumnGroupColumnSchemaTypeDef = TypedDict(
    "ColumnGroupColumnSchemaTypeDef",
    {
        "Name": NotRequired[str],
    },
)
GeoSpatialColumnGroupOutputTypeDef = TypedDict(
    "GeoSpatialColumnGroupOutputTypeDef",
    {
        "Name": str,
        "Columns": List[str],
        "CountryCode": NotRequired[Literal["US"]],
    },
)
ColumnLevelPermissionRuleOutputTypeDef = TypedDict(
    "ColumnLevelPermissionRuleOutputTypeDef",
    {
        "Principals": NotRequired[List[str]],
        "ColumnNames": NotRequired[List[str]],
    },
)
ColumnLevelPermissionRuleTypeDef = TypedDict(
    "ColumnLevelPermissionRuleTypeDef",
    {
        "Principals": NotRequired[Sequence[str]],
        "ColumnNames": NotRequired[Sequence[str]],
    },
)
ColumnSchemaTypeDef = TypedDict(
    "ColumnSchemaTypeDef",
    {
        "Name": NotRequired[str],
        "DataType": NotRequired[str],
        "GeographicRole": NotRequired[str],
    },
)
ComparativeOrderOutputTypeDef = TypedDict(
    "ComparativeOrderOutputTypeDef",
    {
        "UseOrdering": NotRequired[ColumnOrderingTypeType],
        "SpecifedOrder": NotRequired[List[str]],
        "TreatUndefinedSpecifiedValues": NotRequired[UndefinedSpecifiedValueTypeType],
    },
)
ComparativeOrderTypeDef = TypedDict(
    "ComparativeOrderTypeDef",
    {
        "UseOrdering": NotRequired[ColumnOrderingTypeType],
        "SpecifedOrder": NotRequired[Sequence[str]],
        "TreatUndefinedSpecifiedValues": NotRequired[UndefinedSpecifiedValueTypeType],
    },
)
ConditionalFormattingSolidColorTypeDef = TypedDict(
    "ConditionalFormattingSolidColorTypeDef",
    {
        "Expression": str,
        "Color": NotRequired[str],
    },
)
ConditionalFormattingCustomIconOptionsTypeDef = TypedDict(
    "ConditionalFormattingCustomIconOptionsTypeDef",
    {
        "Icon": NotRequired[IconType],
        "UnicodeIcon": NotRequired[str],
    },
)
ConditionalFormattingIconDisplayConfigurationTypeDef = TypedDict(
    "ConditionalFormattingIconDisplayConfigurationTypeDef",
    {
        "IconDisplayOption": NotRequired[Literal["ICON_ONLY"]],
    },
)
ConditionalFormattingIconSetTypeDef = TypedDict(
    "ConditionalFormattingIconSetTypeDef",
    {
        "Expression": str,
        "IconSetType": NotRequired[ConditionalFormattingIconSetTypeType],
    },
)
ContextMenuOptionTypeDef = TypedDict(
    "ContextMenuOptionTypeDef",
    {
        "AvailabilityStatus": NotRequired[DashboardBehaviorType],
    },
)
ContributionAnalysisFactorTypeDef = TypedDict(
    "ContributionAnalysisFactorTypeDef",
    {
        "FieldName": NotRequired[str],
    },
)
CreateAccountSubscriptionRequestRequestTypeDef = TypedDict(
    "CreateAccountSubscriptionRequestRequestTypeDef",
    {
        "AuthenticationMethod": AuthenticationMethodOptionType,
        "AwsAccountId": str,
        "AccountName": str,
        "NotificationEmail": str,
        "Edition": NotRequired[EditionType],
        "ActiveDirectoryName": NotRequired[str],
        "Realm": NotRequired[str],
        "DirectoryId": NotRequired[str],
        "AdminGroup": NotRequired[Sequence[str]],
        "AuthorGroup": NotRequired[Sequence[str]],
        "ReaderGroup": NotRequired[Sequence[str]],
        "AdminProGroup": NotRequired[Sequence[str]],
        "AuthorProGroup": NotRequired[Sequence[str]],
        "ReaderProGroup": NotRequired[Sequence[str]],
        "FirstName": NotRequired[str],
        "LastName": NotRequired[str],
        "EmailAddress": NotRequired[str],
        "ContactNumber": NotRequired[str],
        "IAMIdentityCenterInstanceArn": NotRequired[str],
    },
)
SignupResponseTypeDef = TypedDict(
    "SignupResponseTypeDef",
    {
        "IAMUser": NotRequired[bool],
        "userLoginName": NotRequired[str],
        "accountName": NotRequired[str],
        "directoryType": NotRequired[str],
    },
)
ValidationStrategyTypeDef = TypedDict(
    "ValidationStrategyTypeDef",
    {
        "Mode": ValidationStrategyModeType,
    },
)
ResourcePermissionTypeDef = TypedDict(
    "ResourcePermissionTypeDef",
    {
        "Principal": str,
        "Actions": Sequence[str],
    },
)
DataSetUsageConfigurationTypeDef = TypedDict(
    "DataSetUsageConfigurationTypeDef",
    {
        "DisableUseAsDirectQuerySource": NotRequired[bool],
        "DisableUseAsImportedSource": NotRequired[bool],
    },
)
RowLevelPermissionDataSetTypeDef = TypedDict(
    "RowLevelPermissionDataSetTypeDef",
    {
        "Arn": str,
        "PermissionPolicy": RowLevelPermissionPolicyType,
        "Namespace": NotRequired[str],
        "FormatVersion": NotRequired[RowLevelPermissionFormatVersionType],
        "Status": NotRequired[StatusType],
    },
)
CreateFolderMembershipRequestRequestTypeDef = TypedDict(
    "CreateFolderMembershipRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
        "MemberId": str,
        "MemberType": MemberTypeType,
    },
)
FolderMemberTypeDef = TypedDict(
    "FolderMemberTypeDef",
    {
        "MemberId": NotRequired[str],
        "MemberType": NotRequired[MemberTypeType],
    },
)
CreateGroupMembershipRequestRequestTypeDef = TypedDict(
    "CreateGroupMembershipRequestRequestTypeDef",
    {
        "MemberName": str,
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)
GroupMemberTypeDef = TypedDict(
    "GroupMemberTypeDef",
    {
        "Arn": NotRequired[str],
        "MemberName": NotRequired[str],
    },
)
CreateGroupRequestRequestTypeDef = TypedDict(
    "CreateGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
        "Description": NotRequired[str],
    },
)
GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "Arn": NotRequired[str],
        "GroupName": NotRequired[str],
        "Description": NotRequired[str],
        "PrincipalId": NotRequired[str],
    },
)
CreateIAMPolicyAssignmentRequestRequestTypeDef = TypedDict(
    "CreateIAMPolicyAssignmentRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AssignmentName": str,
        "AssignmentStatus": AssignmentStatusType,
        "Namespace": str,
        "PolicyArn": NotRequired[str],
        "Identities": NotRequired[Mapping[str, Sequence[str]]],
    },
)
CreateIngestionRequestRequestTypeDef = TypedDict(
    "CreateIngestionRequestRequestTypeDef",
    {
        "DataSetId": str,
        "IngestionId": str,
        "AwsAccountId": str,
        "IngestionType": NotRequired[IngestionTypeType],
    },
)
CreateRoleMembershipRequestRequestTypeDef = TypedDict(
    "CreateRoleMembershipRequestRequestTypeDef",
    {
        "MemberName": str,
        "AwsAccountId": str,
        "Namespace": str,
        "Role": RoleType,
    },
)
CreateTemplateAliasRequestRequestTypeDef = TypedDict(
    "CreateTemplateAliasRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "AliasName": str,
        "TemplateVersionNumber": int,
    },
)
TemplateAliasTypeDef = TypedDict(
    "TemplateAliasTypeDef",
    {
        "AliasName": NotRequired[str],
        "Arn": NotRequired[str],
        "TemplateVersionNumber": NotRequired[int],
    },
)
CreateThemeAliasRequestRequestTypeDef = TypedDict(
    "CreateThemeAliasRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "AliasName": str,
        "ThemeVersionNumber": int,
    },
)
ThemeAliasTypeDef = TypedDict(
    "ThemeAliasTypeDef",
    {
        "Arn": NotRequired[str],
        "AliasName": NotRequired[str],
        "ThemeVersionNumber": NotRequired[int],
    },
)
DecimalPlacesConfigurationTypeDef = TypedDict(
    "DecimalPlacesConfigurationTypeDef",
    {
        "DecimalPlaces": int,
    },
)
NegativeValueConfigurationTypeDef = TypedDict(
    "NegativeValueConfigurationTypeDef",
    {
        "DisplayMode": NegativeValueDisplayModeType,
    },
)
NullValueFormatConfigurationTypeDef = TypedDict(
    "NullValueFormatConfigurationTypeDef",
    {
        "NullString": str,
    },
)
LocalNavigationConfigurationTypeDef = TypedDict(
    "LocalNavigationConfigurationTypeDef",
    {
        "TargetSheetId": str,
    },
)
CustomActionURLOperationTypeDef = TypedDict(
    "CustomActionURLOperationTypeDef",
    {
        "URLTemplate": str,
        "URLTarget": URLTargetConfigurationType,
    },
)
CustomFilterListConfigurationTypeDef = TypedDict(
    "CustomFilterListConfigurationTypeDef",
    {
        "MatchOperator": CategoryFilterMatchOperatorType,
        "NullOption": FilterNullOptionType,
        "CategoryValues": NotRequired[Sequence[str]],
        "SelectAllOptions": NotRequired[Literal["FILTER_ALL_VALUES"]],
    },
)
CustomNarrativeOptionsTypeDef = TypedDict(
    "CustomNarrativeOptionsTypeDef",
    {
        "Narrative": str,
    },
)
CustomParameterValuesOutputTypeDef = TypedDict(
    "CustomParameterValuesOutputTypeDef",
    {
        "StringValues": NotRequired[List[str]],
        "IntegerValues": NotRequired[List[int]],
        "DecimalValues": NotRequired[List[float]],
        "DateTimeValues": NotRequired[List[datetime]],
    },
)
InputColumnTypeDef = TypedDict(
    "InputColumnTypeDef",
    {
        "Name": str,
        "Type": InputColumnDataTypeType,
        "SubType": NotRequired[ColumnDataSubTypeType],
    },
)
DataPointDrillUpDownOptionTypeDef = TypedDict(
    "DataPointDrillUpDownOptionTypeDef",
    {
        "AvailabilityStatus": NotRequired[DashboardBehaviorType],
    },
)
DataPointMenuLabelOptionTypeDef = TypedDict(
    "DataPointMenuLabelOptionTypeDef",
    {
        "AvailabilityStatus": NotRequired[DashboardBehaviorType],
    },
)
DataPointTooltipOptionTypeDef = TypedDict(
    "DataPointTooltipOptionTypeDef",
    {
        "AvailabilityStatus": NotRequired[DashboardBehaviorType],
    },
)
ExportToCSVOptionTypeDef = TypedDict(
    "ExportToCSVOptionTypeDef",
    {
        "AvailabilityStatus": NotRequired[DashboardBehaviorType],
    },
)
ExportWithHiddenFieldsOptionTypeDef = TypedDict(
    "ExportWithHiddenFieldsOptionTypeDef",
    {
        "AvailabilityStatus": NotRequired[DashboardBehaviorType],
    },
)
SheetControlsOptionTypeDef = TypedDict(
    "SheetControlsOptionTypeDef",
    {
        "VisibilityState": NotRequired[DashboardUIStateType],
    },
)
SheetLayoutElementMaximizationOptionTypeDef = TypedDict(
    "SheetLayoutElementMaximizationOptionTypeDef",
    {
        "AvailabilityStatus": NotRequired[DashboardBehaviorType],
    },
)
VisualAxisSortOptionTypeDef = TypedDict(
    "VisualAxisSortOptionTypeDef",
    {
        "AvailabilityStatus": NotRequired[DashboardBehaviorType],
    },
)
VisualMenuOptionTypeDef = TypedDict(
    "VisualMenuOptionTypeDef",
    {
        "AvailabilityStatus": NotRequired[DashboardBehaviorType],
    },
)
DashboardSearchFilterTypeDef = TypedDict(
    "DashboardSearchFilterTypeDef",
    {
        "Operator": FilterOperatorType,
        "Name": NotRequired[DashboardFilterAttributeType],
        "Value": NotRequired[str],
    },
)
DashboardSummaryTypeDef = TypedDict(
    "DashboardSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "DashboardId": NotRequired[str],
        "Name": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "PublishedVersionNumber": NotRequired[int],
        "LastPublishedTime": NotRequired[datetime],
    },
)
DashboardVersionSummaryTypeDef = TypedDict(
    "DashboardVersionSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "VersionNumber": NotRequired[int],
        "Status": NotRequired[ResourceStatusType],
        "SourceEntityArn": NotRequired[str],
        "Description": NotRequired[str],
    },
)
ExportHiddenFieldsOptionTypeDef = TypedDict(
    "ExportHiddenFieldsOptionTypeDef",
    {
        "AvailabilityStatus": NotRequired[DashboardBehaviorType],
    },
)
DataAggregationTypeDef = TypedDict(
    "DataAggregationTypeDef",
    {
        "DatasetRowDateGranularity": NotRequired[TopicTimeGranularityType],
        "DefaultDateColumnName": NotRequired[str],
    },
)
DataBarsOptionsTypeDef = TypedDict(
    "DataBarsOptionsTypeDef",
    {
        "FieldId": str,
        "PositiveColor": NotRequired[str],
        "NegativeColor": NotRequired[str],
    },
)
DataColorPaletteOutputTypeDef = TypedDict(
    "DataColorPaletteOutputTypeDef",
    {
        "Colors": NotRequired[List[str]],
        "MinMaxGradient": NotRequired[List[str]],
        "EmptyFillColor": NotRequired[str],
    },
)
DataColorPaletteTypeDef = TypedDict(
    "DataColorPaletteTypeDef",
    {
        "Colors": NotRequired[Sequence[str]],
        "MinMaxGradient": NotRequired[Sequence[str]],
        "EmptyFillColor": NotRequired[str],
    },
)
DataPathLabelTypeTypeDef = TypedDict(
    "DataPathLabelTypeTypeDef",
    {
        "FieldId": NotRequired[str],
        "FieldValue": NotRequired[str],
        "Visibility": NotRequired[VisibilityType],
    },
)
FieldLabelTypeTypeDef = TypedDict(
    "FieldLabelTypeTypeDef",
    {
        "FieldId": NotRequired[str],
        "Visibility": NotRequired[VisibilityType],
    },
)
MaximumLabelTypeTypeDef = TypedDict(
    "MaximumLabelTypeTypeDef",
    {
        "Visibility": NotRequired[VisibilityType],
    },
)
MinimumLabelTypeTypeDef = TypedDict(
    "MinimumLabelTypeTypeDef",
    {
        "Visibility": NotRequired[VisibilityType],
    },
)
RangeEndsLabelTypeTypeDef = TypedDict(
    "RangeEndsLabelTypeTypeDef",
    {
        "Visibility": NotRequired[VisibilityType],
    },
)
DataPathTypeTypeDef = TypedDict(
    "DataPathTypeTypeDef",
    {
        "PivotTableDataPathType": NotRequired[PivotTableDataPathTypeType],
    },
)
DataSetSearchFilterTypeDef = TypedDict(
    "DataSetSearchFilterTypeDef",
    {
        "Operator": FilterOperatorType,
        "Name": DataSetFilterAttributeType,
        "Value": str,
    },
)
FieldFolderOutputTypeDef = TypedDict(
    "FieldFolderOutputTypeDef",
    {
        "description": NotRequired[str],
        "columns": NotRequired[List[str]],
    },
)
OutputColumnTypeDef = TypedDict(
    "OutputColumnTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Type": NotRequired[ColumnDataTypeType],
        "SubType": NotRequired[ColumnDataSubTypeType],
    },
)
DataSourceErrorInfoTypeDef = TypedDict(
    "DataSourceErrorInfoTypeDef",
    {
        "Type": NotRequired[DataSourceErrorInfoTypeType],
        "Message": NotRequired[str],
    },
)
DatabricksParametersTypeDef = TypedDict(
    "DatabricksParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "SqlEndpointPath": str,
    },
)
ExasolParametersTypeDef = TypedDict(
    "ExasolParametersTypeDef",
    {
        "Host": str,
        "Port": int,
    },
)
JiraParametersTypeDef = TypedDict(
    "JiraParametersTypeDef",
    {
        "SiteBaseUrl": str,
    },
)
MariaDbParametersTypeDef = TypedDict(
    "MariaDbParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)
MySqlParametersTypeDef = TypedDict(
    "MySqlParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)
OracleParametersTypeDef = TypedDict(
    "OracleParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)
PostgreSqlParametersTypeDef = TypedDict(
    "PostgreSqlParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)
PrestoParametersTypeDef = TypedDict(
    "PrestoParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Catalog": str,
    },
)
RdsParametersTypeDef = TypedDict(
    "RdsParametersTypeDef",
    {
        "InstanceId": str,
        "Database": str,
    },
)
ServiceNowParametersTypeDef = TypedDict(
    "ServiceNowParametersTypeDef",
    {
        "SiteBaseUrl": str,
    },
)
SnowflakeParametersTypeDef = TypedDict(
    "SnowflakeParametersTypeDef",
    {
        "Host": str,
        "Database": str,
        "Warehouse": str,
    },
)
SparkParametersTypeDef = TypedDict(
    "SparkParametersTypeDef",
    {
        "Host": str,
        "Port": int,
    },
)
SqlServerParametersTypeDef = TypedDict(
    "SqlServerParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)
StarburstParametersTypeDef = TypedDict(
    "StarburstParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Catalog": str,
        "ProductType": NotRequired[StarburstProductTypeType],
    },
)
TeradataParametersTypeDef = TypedDict(
    "TeradataParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Database": str,
    },
)
TrinoParametersTypeDef = TypedDict(
    "TrinoParametersTypeDef",
    {
        "Host": str,
        "Port": int,
        "Catalog": str,
    },
)
TwitterParametersTypeDef = TypedDict(
    "TwitterParametersTypeDef",
    {
        "Query": str,
        "MaxRows": int,
    },
)
DataSourceSearchFilterTypeDef = TypedDict(
    "DataSourceSearchFilterTypeDef",
    {
        "Operator": FilterOperatorType,
        "Name": DataSourceFilterAttributeType,
        "Value": str,
    },
)
DataSourceSummaryTypeDef = TypedDict(
    "DataSourceSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "DataSourceId": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[DataSourceTypeType],
        "CreatedTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
    },
)
DateTimeDatasetParameterDefaultValuesOutputTypeDef = TypedDict(
    "DateTimeDatasetParameterDefaultValuesOutputTypeDef",
    {
        "StaticValues": NotRequired[List[datetime]],
    },
)
RollingDateConfigurationTypeDef = TypedDict(
    "RollingDateConfigurationTypeDef",
    {
        "Expression": str,
        "DataSetIdentifier": NotRequired[str],
    },
)
DateTimeValueWhenUnsetConfigurationOutputTypeDef = TypedDict(
    "DateTimeValueWhenUnsetConfigurationOutputTypeDef",
    {
        "ValueWhenUnsetOption": NotRequired[ValueWhenUnsetOptionType],
        "CustomValue": NotRequired[datetime],
    },
)
MappedDataSetParameterTypeDef = TypedDict(
    "MappedDataSetParameterTypeDef",
    {
        "DataSetIdentifier": str,
        "DataSetParameterName": str,
    },
)
DateTimeParameterOutputTypeDef = TypedDict(
    "DateTimeParameterOutputTypeDef",
    {
        "Name": str,
        "Values": List[datetime],
    },
)
SheetControlInfoIconLabelOptionsTypeDef = TypedDict(
    "SheetControlInfoIconLabelOptionsTypeDef",
    {
        "Visibility": NotRequired[VisibilityType],
        "InfoIconText": NotRequired[str],
    },
)
DecimalDatasetParameterDefaultValuesOutputTypeDef = TypedDict(
    "DecimalDatasetParameterDefaultValuesOutputTypeDef",
    {
        "StaticValues": NotRequired[List[float]],
    },
)
DecimalDatasetParameterDefaultValuesTypeDef = TypedDict(
    "DecimalDatasetParameterDefaultValuesTypeDef",
    {
        "StaticValues": NotRequired[Sequence[float]],
    },
)
DecimalValueWhenUnsetConfigurationTypeDef = TypedDict(
    "DecimalValueWhenUnsetConfigurationTypeDef",
    {
        "ValueWhenUnsetOption": NotRequired[ValueWhenUnsetOptionType],
        "CustomValue": NotRequired[float],
    },
)
DecimalParameterOutputTypeDef = TypedDict(
    "DecimalParameterOutputTypeDef",
    {
        "Name": str,
        "Values": List[float],
    },
)
DecimalParameterTypeDef = TypedDict(
    "DecimalParameterTypeDef",
    {
        "Name": str,
        "Values": Sequence[float],
    },
)
FilterSelectableValuesOutputTypeDef = TypedDict(
    "FilterSelectableValuesOutputTypeDef",
    {
        "Values": NotRequired[List[str]],
    },
)
DeleteAccountCustomizationRequestRequestTypeDef = TypedDict(
    "DeleteAccountCustomizationRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": NotRequired[str],
    },
)
DeleteAccountSubscriptionRequestRequestTypeDef = TypedDict(
    "DeleteAccountSubscriptionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
DeleteAnalysisRequestRequestTypeDef = TypedDict(
    "DeleteAnalysisRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
        "RecoveryWindowInDays": NotRequired[int],
        "ForceDeleteWithoutRecovery": NotRequired[bool],
    },
)
DeleteDashboardRequestRequestTypeDef = TypedDict(
    "DeleteDashboardRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "VersionNumber": NotRequired[int],
    },
)
DeleteDataSetRefreshPropertiesRequestRequestTypeDef = TypedDict(
    "DeleteDataSetRefreshPropertiesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
    },
)
DeleteDataSetRequestRequestTypeDef = TypedDict(
    "DeleteDataSetRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
    },
)
DeleteDataSourceRequestRequestTypeDef = TypedDict(
    "DeleteDataSourceRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSourceId": str,
    },
)
DeleteFolderMembershipRequestRequestTypeDef = TypedDict(
    "DeleteFolderMembershipRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
        "MemberId": str,
        "MemberType": MemberTypeType,
    },
)
DeleteFolderRequestRequestTypeDef = TypedDict(
    "DeleteFolderRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
    },
)
DeleteGroupMembershipRequestRequestTypeDef = TypedDict(
    "DeleteGroupMembershipRequestRequestTypeDef",
    {
        "MemberName": str,
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)
DeleteGroupRequestRequestTypeDef = TypedDict(
    "DeleteGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)
DeleteIAMPolicyAssignmentRequestRequestTypeDef = TypedDict(
    "DeleteIAMPolicyAssignmentRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AssignmentName": str,
        "Namespace": str,
    },
)
DeleteIdentityPropagationConfigRequestRequestTypeDef = TypedDict(
    "DeleteIdentityPropagationConfigRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Service": Literal["REDSHIFT"],
    },
)
DeleteNamespaceRequestRequestTypeDef = TypedDict(
    "DeleteNamespaceRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
    },
)
DeleteRefreshScheduleRequestRequestTypeDef = TypedDict(
    "DeleteRefreshScheduleRequestRequestTypeDef",
    {
        "DataSetId": str,
        "AwsAccountId": str,
        "ScheduleId": str,
    },
)
DeleteRoleCustomPermissionRequestRequestTypeDef = TypedDict(
    "DeleteRoleCustomPermissionRequestRequestTypeDef",
    {
        "Role": RoleType,
        "AwsAccountId": str,
        "Namespace": str,
    },
)
DeleteRoleMembershipRequestRequestTypeDef = TypedDict(
    "DeleteRoleMembershipRequestRequestTypeDef",
    {
        "MemberName": str,
        "Role": RoleType,
        "AwsAccountId": str,
        "Namespace": str,
    },
)
DeleteTemplateAliasRequestRequestTypeDef = TypedDict(
    "DeleteTemplateAliasRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "AliasName": str,
    },
)
DeleteTemplateRequestRequestTypeDef = TypedDict(
    "DeleteTemplateRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "VersionNumber": NotRequired[int],
    },
)
DeleteThemeAliasRequestRequestTypeDef = TypedDict(
    "DeleteThemeAliasRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "AliasName": str,
    },
)
DeleteThemeRequestRequestTypeDef = TypedDict(
    "DeleteThemeRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "VersionNumber": NotRequired[int],
    },
)
DeleteTopicRefreshScheduleRequestRequestTypeDef = TypedDict(
    "DeleteTopicRefreshScheduleRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TopicId": str,
        "DatasetId": str,
    },
)
DeleteTopicRequestRequestTypeDef = TypedDict(
    "DeleteTopicRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TopicId": str,
    },
)
DeleteUserByPrincipalIdRequestRequestTypeDef = TypedDict(
    "DeleteUserByPrincipalIdRequestRequestTypeDef",
    {
        "PrincipalId": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)
DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "UserName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)
DeleteVPCConnectionRequestRequestTypeDef = TypedDict(
    "DeleteVPCConnectionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "VPCConnectionId": str,
    },
)
DescribeAccountCustomizationRequestRequestTypeDef = TypedDict(
    "DescribeAccountCustomizationRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": NotRequired[str],
        "Resolved": NotRequired[bool],
    },
)
DescribeAccountSettingsRequestRequestTypeDef = TypedDict(
    "DescribeAccountSettingsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
DescribeAccountSubscriptionRequestRequestTypeDef = TypedDict(
    "DescribeAccountSubscriptionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
DescribeAnalysisDefinitionRequestRequestTypeDef = TypedDict(
    "DescribeAnalysisDefinitionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
    },
)
DescribeAnalysisPermissionsRequestRequestTypeDef = TypedDict(
    "DescribeAnalysisPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
    },
)
ResourcePermissionOutputTypeDef = TypedDict(
    "ResourcePermissionOutputTypeDef",
    {
        "Principal": str,
        "Actions": List[str],
    },
)
DescribeAnalysisRequestRequestTypeDef = TypedDict(
    "DescribeAnalysisRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
    },
)
DescribeAssetBundleExportJobRequestRequestTypeDef = TypedDict(
    "DescribeAssetBundleExportJobRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AssetBundleExportJobId": str,
    },
)
DescribeAssetBundleImportJobRequestRequestTypeDef = TypedDict(
    "DescribeAssetBundleImportJobRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AssetBundleImportJobId": str,
    },
)
DescribeDashboardDefinitionRequestRequestTypeDef = TypedDict(
    "DescribeDashboardDefinitionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "VersionNumber": NotRequired[int],
        "AliasName": NotRequired[str],
    },
)
DescribeDashboardPermissionsRequestRequestTypeDef = TypedDict(
    "DescribeDashboardPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
    },
)
DescribeDashboardRequestRequestTypeDef = TypedDict(
    "DescribeDashboardRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "VersionNumber": NotRequired[int],
        "AliasName": NotRequired[str],
    },
)
DescribeDashboardSnapshotJobRequestRequestTypeDef = TypedDict(
    "DescribeDashboardSnapshotJobRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "SnapshotJobId": str,
    },
)
DescribeDashboardSnapshotJobResultRequestRequestTypeDef = TypedDict(
    "DescribeDashboardSnapshotJobResultRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "SnapshotJobId": str,
    },
)
SnapshotJobErrorInfoTypeDef = TypedDict(
    "SnapshotJobErrorInfoTypeDef",
    {
        "ErrorMessage": NotRequired[str],
        "ErrorType": NotRequired[str],
    },
)
DescribeDataSetPermissionsRequestRequestTypeDef = TypedDict(
    "DescribeDataSetPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
    },
)
DescribeDataSetRefreshPropertiesRequestRequestTypeDef = TypedDict(
    "DescribeDataSetRefreshPropertiesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
    },
)
DescribeDataSetRequestRequestTypeDef = TypedDict(
    "DescribeDataSetRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
    },
)
DescribeDataSourcePermissionsRequestRequestTypeDef = TypedDict(
    "DescribeDataSourcePermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSourceId": str,
    },
)
DescribeDataSourceRequestRequestTypeDef = TypedDict(
    "DescribeDataSourceRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSourceId": str,
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
DescribeFolderPermissionsRequestRequestTypeDef = TypedDict(
    "DescribeFolderPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
        "Namespace": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
DescribeFolderRequestRequestTypeDef = TypedDict(
    "DescribeFolderRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
    },
)
DescribeFolderResolvedPermissionsRequestRequestTypeDef = TypedDict(
    "DescribeFolderResolvedPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
        "Namespace": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
FolderTypeDef = TypedDict(
    "FolderTypeDef",
    {
        "FolderId": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "FolderType": NotRequired[FolderTypeType],
        "FolderPath": NotRequired[List[str]],
        "CreatedTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "SharingModel": NotRequired[SharingModelType],
    },
)
DescribeGroupMembershipRequestRequestTypeDef = TypedDict(
    "DescribeGroupMembershipRequestRequestTypeDef",
    {
        "MemberName": str,
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)
DescribeGroupRequestRequestTypeDef = TypedDict(
    "DescribeGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)
DescribeIAMPolicyAssignmentRequestRequestTypeDef = TypedDict(
    "DescribeIAMPolicyAssignmentRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AssignmentName": str,
        "Namespace": str,
    },
)
IAMPolicyAssignmentTypeDef = TypedDict(
    "IAMPolicyAssignmentTypeDef",
    {
        "AwsAccountId": NotRequired[str],
        "AssignmentId": NotRequired[str],
        "AssignmentName": NotRequired[str],
        "PolicyArn": NotRequired[str],
        "Identities": NotRequired[Dict[str, List[str]]],
        "AssignmentStatus": NotRequired[AssignmentStatusType],
    },
)
DescribeIngestionRequestRequestTypeDef = TypedDict(
    "DescribeIngestionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
        "IngestionId": str,
    },
)
DescribeIpRestrictionRequestRequestTypeDef = TypedDict(
    "DescribeIpRestrictionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
DescribeKeyRegistrationRequestRequestTypeDef = TypedDict(
    "DescribeKeyRegistrationRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DefaultKeyOnly": NotRequired[bool],
    },
)
RegisteredCustomerManagedKeyTypeDef = TypedDict(
    "RegisteredCustomerManagedKeyTypeDef",
    {
        "KeyArn": NotRequired[str],
        "DefaultKey": NotRequired[bool],
    },
)
DescribeNamespaceRequestRequestTypeDef = TypedDict(
    "DescribeNamespaceRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
    },
)
DescribeQPersonalizationConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeQPersonalizationConfigurationRequestRequestTypeDef",
    {
        "AwsAccountId": str,
    },
)
DescribeRefreshScheduleRequestRequestTypeDef = TypedDict(
    "DescribeRefreshScheduleRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
        "ScheduleId": str,
    },
)
DescribeRoleCustomPermissionRequestRequestTypeDef = TypedDict(
    "DescribeRoleCustomPermissionRequestRequestTypeDef",
    {
        "Role": RoleType,
        "AwsAccountId": str,
        "Namespace": str,
    },
)
DescribeTemplateAliasRequestRequestTypeDef = TypedDict(
    "DescribeTemplateAliasRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "AliasName": str,
    },
)
DescribeTemplateDefinitionRequestRequestTypeDef = TypedDict(
    "DescribeTemplateDefinitionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "VersionNumber": NotRequired[int],
        "AliasName": NotRequired[str],
    },
)
DescribeTemplatePermissionsRequestRequestTypeDef = TypedDict(
    "DescribeTemplatePermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
    },
)
DescribeTemplateRequestRequestTypeDef = TypedDict(
    "DescribeTemplateRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "VersionNumber": NotRequired[int],
        "AliasName": NotRequired[str],
    },
)
DescribeThemeAliasRequestRequestTypeDef = TypedDict(
    "DescribeThemeAliasRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "AliasName": str,
    },
)
DescribeThemePermissionsRequestRequestTypeDef = TypedDict(
    "DescribeThemePermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
    },
)
DescribeThemeRequestRequestTypeDef = TypedDict(
    "DescribeThemeRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "VersionNumber": NotRequired[int],
        "AliasName": NotRequired[str],
    },
)
DescribeTopicPermissionsRequestRequestTypeDef = TypedDict(
    "DescribeTopicPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TopicId": str,
    },
)
DescribeTopicRefreshRequestRequestTypeDef = TypedDict(
    "DescribeTopicRefreshRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TopicId": str,
        "RefreshId": str,
    },
)
TopicRefreshDetailsTypeDef = TypedDict(
    "TopicRefreshDetailsTypeDef",
    {
        "RefreshArn": NotRequired[str],
        "RefreshId": NotRequired[str],
        "RefreshStatus": NotRequired[TopicRefreshStatusType],
    },
)
DescribeTopicRefreshScheduleRequestRequestTypeDef = TypedDict(
    "DescribeTopicRefreshScheduleRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TopicId": str,
        "DatasetId": str,
    },
)
TopicRefreshScheduleOutputTypeDef = TypedDict(
    "TopicRefreshScheduleOutputTypeDef",
    {
        "IsEnabled": bool,
        "BasedOnSpiceSchedule": bool,
        "StartingAt": NotRequired[datetime],
        "Timezone": NotRequired[str],
        "RepeatAt": NotRequired[str],
        "TopicScheduleType": NotRequired[TopicScheduleTypeType],
    },
)
DescribeTopicRequestRequestTypeDef = TypedDict(
    "DescribeTopicRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TopicId": str,
    },
)
DescribeUserRequestRequestTypeDef = TypedDict(
    "DescribeUserRequestRequestTypeDef",
    {
        "UserName": str,
        "AwsAccountId": str,
        "Namespace": str,
    },
)
UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "Arn": NotRequired[str],
        "UserName": NotRequired[str],
        "Email": NotRequired[str],
        "Role": NotRequired[UserRoleType],
        "IdentityType": NotRequired[IdentityTypeType],
        "Active": NotRequired[bool],
        "PrincipalId": NotRequired[str],
        "CustomPermissionsName": NotRequired[str],
        "ExternalLoginFederationProviderType": NotRequired[str],
        "ExternalLoginFederationProviderUrl": NotRequired[str],
        "ExternalLoginId": NotRequired[str],
    },
)
DescribeVPCConnectionRequestRequestTypeDef = TypedDict(
    "DescribeVPCConnectionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "VPCConnectionId": str,
    },
)
NegativeFormatTypeDef = TypedDict(
    "NegativeFormatTypeDef",
    {
        "Prefix": NotRequired[str],
        "Suffix": NotRequired[str],
    },
)
DonutCenterOptionsTypeDef = TypedDict(
    "DonutCenterOptionsTypeDef",
    {
        "LabelVisibility": NotRequired[VisibilityType],
    },
)
ListControlSelectAllOptionsTypeDef = TypedDict(
    "ListControlSelectAllOptionsTypeDef",
    {
        "Visibility": NotRequired[VisibilityType],
    },
)
ErrorInfoTypeDef = TypedDict(
    "ErrorInfoTypeDef",
    {
        "Type": NotRequired[IngestionErrorTypeType],
        "Message": NotRequired[str],
    },
)
ExcludePeriodConfigurationTypeDef = TypedDict(
    "ExcludePeriodConfigurationTypeDef",
    {
        "Amount": int,
        "Granularity": TimeGranularityType,
        "Status": NotRequired[WidgetStatusType],
    },
)
FailedKeyRegistrationEntryTypeDef = TypedDict(
    "FailedKeyRegistrationEntryTypeDef",
    {
        "Message": str,
        "StatusCode": int,
        "SenderFault": bool,
        "KeyArn": NotRequired[str],
    },
)
FieldFolderTypeDef = TypedDict(
    "FieldFolderTypeDef",
    {
        "description": NotRequired[str],
        "columns": NotRequired[Sequence[str]],
    },
)
FieldSortTypeDef = TypedDict(
    "FieldSortTypeDef",
    {
        "FieldId": str,
        "Direction": SortDirectionType,
    },
)
FieldTooltipItemTypeDef = TypedDict(
    "FieldTooltipItemTypeDef",
    {
        "FieldId": str,
        "Label": NotRequired[str],
        "Visibility": NotRequired[VisibilityType],
        "TooltipTarget": NotRequired[TooltipTargetType],
    },
)
GeospatialMapStyleOptionsTypeDef = TypedDict(
    "GeospatialMapStyleOptionsTypeDef",
    {
        "BaseMapStyle": NotRequired[BaseMapStyleTypeType],
    },
)
IdentifierTypeDef = TypedDict(
    "IdentifierTypeDef",
    {
        "Identity": str,
    },
)
FilterListConfigurationTypeDef = TypedDict(
    "FilterListConfigurationTypeDef",
    {
        "MatchOperator": CategoryFilterMatchOperatorType,
        "CategoryValues": NotRequired[Sequence[str]],
        "SelectAllOptions": NotRequired[Literal["FILTER_ALL_VALUES"]],
        "NullOption": NotRequired[FilterNullOptionType],
    },
)
SameSheetTargetVisualConfigurationOutputTypeDef = TypedDict(
    "SameSheetTargetVisualConfigurationOutputTypeDef",
    {
        "TargetVisuals": NotRequired[List[str]],
        "TargetVisualOptions": NotRequired[Literal["ALL_VISUALS"]],
    },
)
FilterOperationTypeDef = TypedDict(
    "FilterOperationTypeDef",
    {
        "ConditionExpression": str,
    },
)
FilterSelectableValuesTypeDef = TypedDict(
    "FilterSelectableValuesTypeDef",
    {
        "Values": NotRequired[Sequence[str]],
    },
)
FolderSearchFilterTypeDef = TypedDict(
    "FolderSearchFilterTypeDef",
    {
        "Operator": NotRequired[FilterOperatorType],
        "Name": NotRequired[FolderFilterAttributeType],
        "Value": NotRequired[str],
    },
)
FolderSummaryTypeDef = TypedDict(
    "FolderSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "FolderId": NotRequired[str],
        "Name": NotRequired[str],
        "FolderType": NotRequired[FolderTypeType],
        "CreatedTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "SharingModel": NotRequired[SharingModelType],
    },
)
FontSizeTypeDef = TypedDict(
    "FontSizeTypeDef",
    {
        "Relative": NotRequired[RelativeFontSizeType],
    },
)
FontWeightTypeDef = TypedDict(
    "FontWeightTypeDef",
    {
        "Name": NotRequired[FontWeightNameType],
    },
)
FontTypeDef = TypedDict(
    "FontTypeDef",
    {
        "FontFamily": NotRequired[str],
    },
)
TimeBasedForecastPropertiesTypeDef = TypedDict(
    "TimeBasedForecastPropertiesTypeDef",
    {
        "PeriodsForward": NotRequired[int],
        "PeriodsBackward": NotRequired[int],
        "UpperBoundary": NotRequired[float],
        "LowerBoundary": NotRequired[float],
        "PredictionInterval": NotRequired[int],
        "Seasonality": NotRequired[int],
    },
)
WhatIfPointScenarioOutputTypeDef = TypedDict(
    "WhatIfPointScenarioOutputTypeDef",
    {
        "Date": datetime,
        "Value": float,
    },
)
WhatIfRangeScenarioOutputTypeDef = TypedDict(
    "WhatIfRangeScenarioOutputTypeDef",
    {
        "StartDate": datetime,
        "EndDate": datetime,
        "Value": float,
    },
)
FreeFormLayoutScreenCanvasSizeOptionsTypeDef = TypedDict(
    "FreeFormLayoutScreenCanvasSizeOptionsTypeDef",
    {
        "OptimizedViewPortWidth": str,
    },
)
FreeFormLayoutElementBackgroundStyleTypeDef = TypedDict(
    "FreeFormLayoutElementBackgroundStyleTypeDef",
    {
        "Visibility": NotRequired[VisibilityType],
        "Color": NotRequired[str],
    },
)
FreeFormLayoutElementBorderStyleTypeDef = TypedDict(
    "FreeFormLayoutElementBorderStyleTypeDef",
    {
        "Visibility": NotRequired[VisibilityType],
        "Color": NotRequired[str],
    },
)
LoadingAnimationTypeDef = TypedDict(
    "LoadingAnimationTypeDef",
    {
        "Visibility": NotRequired[VisibilityType],
    },
)
GaugeChartColorConfigurationTypeDef = TypedDict(
    "GaugeChartColorConfigurationTypeDef",
    {
        "ForegroundColor": NotRequired[str],
        "BackgroundColor": NotRequired[str],
    },
)
SessionTagTypeDef = TypedDict(
    "SessionTagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
GeoSpatialColumnGroupTypeDef = TypedDict(
    "GeoSpatialColumnGroupTypeDef",
    {
        "Name": str,
        "Columns": Sequence[str],
        "CountryCode": NotRequired[Literal["US"]],
    },
)
GeospatialCoordinateBoundsTypeDef = TypedDict(
    "GeospatialCoordinateBoundsTypeDef",
    {
        "North": float,
        "South": float,
        "West": float,
        "East": float,
    },
)
GeospatialHeatmapDataColorTypeDef = TypedDict(
    "GeospatialHeatmapDataColorTypeDef",
    {
        "Color": str,
    },
)
GetDashboardEmbedUrlRequestRequestTypeDef = TypedDict(
    "GetDashboardEmbedUrlRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "IdentityType": EmbeddingIdentityTypeType,
        "SessionLifetimeInMinutes": NotRequired[int],
        "UndoRedoDisabled": NotRequired[bool],
        "ResetDisabled": NotRequired[bool],
        "StatePersistenceEnabled": NotRequired[bool],
        "UserArn": NotRequired[str],
        "Namespace": NotRequired[str],
        "AdditionalDashboardIds": NotRequired[Sequence[str]],
    },
)
GetSessionEmbedUrlRequestRequestTypeDef = TypedDict(
    "GetSessionEmbedUrlRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "EntryPoint": NotRequired[str],
        "SessionLifetimeInMinutes": NotRequired[int],
        "UserArn": NotRequired[str],
    },
)
TableBorderOptionsTypeDef = TypedDict(
    "TableBorderOptionsTypeDef",
    {
        "Color": NotRequired[str],
        "Thickness": NotRequired[int],
        "Style": NotRequired[TableBorderStyleType],
    },
)
GradientStopTypeDef = TypedDict(
    "GradientStopTypeDef",
    {
        "GradientOffset": float,
        "DataValue": NotRequired[float],
        "Color": NotRequired[str],
    },
)
GridLayoutScreenCanvasSizeOptionsTypeDef = TypedDict(
    "GridLayoutScreenCanvasSizeOptionsTypeDef",
    {
        "ResizeOption": ResizeOptionType,
        "OptimizedViewPortWidth": NotRequired[str],
    },
)
GridLayoutElementTypeDef = TypedDict(
    "GridLayoutElementTypeDef",
    {
        "ElementId": str,
        "ElementType": LayoutElementTypeType,
        "ColumnSpan": int,
        "RowSpan": int,
        "ColumnIndex": NotRequired[int],
        "RowIndex": NotRequired[int],
    },
)
GroupSearchFilterTypeDef = TypedDict(
    "GroupSearchFilterTypeDef",
    {
        "Operator": Literal["StartsWith"],
        "Name": Literal["GROUP_NAME"],
        "Value": str,
    },
)
GutterStyleTypeDef = TypedDict(
    "GutterStyleTypeDef",
    {
        "Show": NotRequired[bool],
    },
)
IAMPolicyAssignmentSummaryTypeDef = TypedDict(
    "IAMPolicyAssignmentSummaryTypeDef",
    {
        "AssignmentName": NotRequired[str],
        "AssignmentStatus": NotRequired[AssignmentStatusType],
    },
)
IdentityCenterConfigurationTypeDef = TypedDict(
    "IdentityCenterConfigurationTypeDef",
    {
        "EnableIdentityPropagation": NotRequired[bool],
    },
)
LookbackWindowTypeDef = TypedDict(
    "LookbackWindowTypeDef",
    {
        "ColumnName": str,
        "Size": int,
        "SizeUnit": LookbackWindowSizeUnitType,
    },
)
QueueInfoTypeDef = TypedDict(
    "QueueInfoTypeDef",
    {
        "WaitingOnIngestion": str,
        "QueuedIngestion": str,
    },
)
RowInfoTypeDef = TypedDict(
    "RowInfoTypeDef",
    {
        "RowsIngested": NotRequired[int],
        "RowsDropped": NotRequired[int],
        "TotalRowsInDataset": NotRequired[int],
    },
)
IntegerDatasetParameterDefaultValuesOutputTypeDef = TypedDict(
    "IntegerDatasetParameterDefaultValuesOutputTypeDef",
    {
        "StaticValues": NotRequired[List[int]],
    },
)
IntegerDatasetParameterDefaultValuesTypeDef = TypedDict(
    "IntegerDatasetParameterDefaultValuesTypeDef",
    {
        "StaticValues": NotRequired[Sequence[int]],
    },
)
IntegerValueWhenUnsetConfigurationTypeDef = TypedDict(
    "IntegerValueWhenUnsetConfigurationTypeDef",
    {
        "ValueWhenUnsetOption": NotRequired[ValueWhenUnsetOptionType],
        "CustomValue": NotRequired[int],
    },
)
IntegerParameterOutputTypeDef = TypedDict(
    "IntegerParameterOutputTypeDef",
    {
        "Name": str,
        "Values": List[int],
    },
)
IntegerParameterTypeDef = TypedDict(
    "IntegerParameterTypeDef",
    {
        "Name": str,
        "Values": Sequence[int],
    },
)
JoinKeyPropertiesTypeDef = TypedDict(
    "JoinKeyPropertiesTypeDef",
    {
        "UniqueKey": NotRequired[bool],
    },
)
KPISparklineOptionsTypeDef = TypedDict(
    "KPISparklineOptionsTypeDef",
    {
        "Type": KPISparklineTypeType,
        "Visibility": NotRequired[VisibilityType],
        "Color": NotRequired[str],
        "TooltipVisibility": NotRequired[VisibilityType],
    },
)
ProgressBarOptionsTypeDef = TypedDict(
    "ProgressBarOptionsTypeDef",
    {
        "Visibility": NotRequired[VisibilityType],
    },
)
SecondaryValueOptionsTypeDef = TypedDict(
    "SecondaryValueOptionsTypeDef",
    {
        "Visibility": NotRequired[VisibilityType],
    },
)
TrendArrowOptionsTypeDef = TypedDict(
    "TrendArrowOptionsTypeDef",
    {
        "Visibility": NotRequired[VisibilityType],
    },
)
KPIVisualStandardLayoutTypeDef = TypedDict(
    "KPIVisualStandardLayoutTypeDef",
    {
        "Type": KPIVisualStandardLayoutTypeType,
    },
)
LineChartLineStyleSettingsTypeDef = TypedDict(
    "LineChartLineStyleSettingsTypeDef",
    {
        "LineVisibility": NotRequired[VisibilityType],
        "LineInterpolation": NotRequired[LineInterpolationType],
        "LineStyle": NotRequired[LineChartLineStyleType],
        "LineWidth": NotRequired[str],
    },
)
LineChartMarkerStyleSettingsTypeDef = TypedDict(
    "LineChartMarkerStyleSettingsTypeDef",
    {
        "MarkerVisibility": NotRequired[VisibilityType],
        "MarkerShape": NotRequired[LineChartMarkerShapeType],
        "MarkerSize": NotRequired[str],
        "MarkerColor": NotRequired[str],
    },
)
MissingDataConfigurationTypeDef = TypedDict(
    "MissingDataConfigurationTypeDef",
    {
        "TreatmentOption": NotRequired[MissingDataTreatmentOptionType],
    },
)
ListAnalysesRequestRequestTypeDef = TypedDict(
    "ListAnalysesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListAssetBundleExportJobsRequestRequestTypeDef = TypedDict(
    "ListAssetBundleExportJobsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListAssetBundleImportJobsRequestRequestTypeDef = TypedDict(
    "ListAssetBundleImportJobsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListControlSearchOptionsTypeDef = TypedDict(
    "ListControlSearchOptionsTypeDef",
    {
        "Visibility": NotRequired[VisibilityType],
    },
)
ListDashboardVersionsRequestRequestTypeDef = TypedDict(
    "ListDashboardVersionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListDashboardsRequestRequestTypeDef = TypedDict(
    "ListDashboardsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListDataSetsRequestRequestTypeDef = TypedDict(
    "ListDataSetsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListDataSourcesRequestRequestTypeDef = TypedDict(
    "ListDataSourcesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListFolderMembersRequestRequestTypeDef = TypedDict(
    "ListFolderMembersRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
MemberIdArnPairTypeDef = TypedDict(
    "MemberIdArnPairTypeDef",
    {
        "MemberId": NotRequired[str],
        "MemberArn": NotRequired[str],
    },
)
ListFoldersForResourceRequestRequestTypeDef = TypedDict(
    "ListFoldersForResourceRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ResourceArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListFoldersRequestRequestTypeDef = TypedDict(
    "ListFoldersRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListGroupMembershipsRequestRequestTypeDef = TypedDict(
    "ListGroupMembershipsRequestRequestTypeDef",
    {
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListGroupsRequestRequestTypeDef = TypedDict(
    "ListGroupsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListIAMPolicyAssignmentsForUserRequestRequestTypeDef = TypedDict(
    "ListIAMPolicyAssignmentsForUserRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "UserName": str,
        "Namespace": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListIAMPolicyAssignmentsRequestRequestTypeDef = TypedDict(
    "ListIAMPolicyAssignmentsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
        "AssignmentStatus": NotRequired[AssignmentStatusType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListIdentityPropagationConfigsRequestRequestTypeDef = TypedDict(
    "ListIdentityPropagationConfigsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListIngestionsRequestRequestTypeDef = TypedDict(
    "ListIngestionsRequestRequestTypeDef",
    {
        "DataSetId": str,
        "AwsAccountId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListNamespacesRequestRequestTypeDef = TypedDict(
    "ListNamespacesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListRefreshSchedulesRequestRequestTypeDef = TypedDict(
    "ListRefreshSchedulesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
    },
)
ListRoleMembershipsRequestRequestTypeDef = TypedDict(
    "ListRoleMembershipsRequestRequestTypeDef",
    {
        "Role": RoleType,
        "AwsAccountId": str,
        "Namespace": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
ListTemplateAliasesRequestRequestTypeDef = TypedDict(
    "ListTemplateAliasesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListTemplateVersionsRequestRequestTypeDef = TypedDict(
    "ListTemplateVersionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
TemplateVersionSummaryTypeDef = TypedDict(
    "TemplateVersionSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "VersionNumber": NotRequired[int],
        "CreatedTime": NotRequired[datetime],
        "Status": NotRequired[ResourceStatusType],
        "Description": NotRequired[str],
    },
)
ListTemplatesRequestRequestTypeDef = TypedDict(
    "ListTemplatesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
TemplateSummaryTypeDef = TypedDict(
    "TemplateSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "TemplateId": NotRequired[str],
        "Name": NotRequired[str],
        "LatestVersionNumber": NotRequired[int],
        "CreatedTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
    },
)
ListThemeAliasesRequestRequestTypeDef = TypedDict(
    "ListThemeAliasesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListThemeVersionsRequestRequestTypeDef = TypedDict(
    "ListThemeVersionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ThemeVersionSummaryTypeDef = TypedDict(
    "ThemeVersionSummaryTypeDef",
    {
        "VersionNumber": NotRequired[int],
        "Arn": NotRequired[str],
        "Description": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "Status": NotRequired[ResourceStatusType],
    },
)
ListThemesRequestRequestTypeDef = TypedDict(
    "ListThemesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Type": NotRequired[ThemeTypeType],
    },
)
ThemeSummaryTypeDef = TypedDict(
    "ThemeSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "ThemeId": NotRequired[str],
        "LatestVersionNumber": NotRequired[int],
        "CreatedTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
    },
)
ListTopicRefreshSchedulesRequestRequestTypeDef = TypedDict(
    "ListTopicRefreshSchedulesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TopicId": str,
    },
)
ListTopicReviewedAnswersRequestRequestTypeDef = TypedDict(
    "ListTopicReviewedAnswersRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TopicId": str,
    },
)
ListTopicsRequestRequestTypeDef = TypedDict(
    "ListTopicsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
TopicSummaryTypeDef = TypedDict(
    "TopicSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "TopicId": NotRequired[str],
        "Name": NotRequired[str],
        "UserExperienceVersion": NotRequired[TopicUserExperienceVersionType],
    },
)
ListUserGroupsRequestRequestTypeDef = TypedDict(
    "ListUserGroupsRequestRequestTypeDef",
    {
        "UserName": str,
        "AwsAccountId": str,
        "Namespace": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListUsersRequestRequestTypeDef = TypedDict(
    "ListUsersRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListVPCConnectionsRequestRequestTypeDef = TypedDict(
    "ListVPCConnectionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
LongFormatTextTypeDef = TypedDict(
    "LongFormatTextTypeDef",
    {
        "PlainText": NotRequired[str],
        "RichText": NotRequired[str],
    },
)
ManifestFileLocationTypeDef = TypedDict(
    "ManifestFileLocationTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
MarginStyleTypeDef = TypedDict(
    "MarginStyleTypeDef",
    {
        "Show": NotRequired[bool],
    },
)
NamedEntityDefinitionMetricOutputTypeDef = TypedDict(
    "NamedEntityDefinitionMetricOutputTypeDef",
    {
        "Aggregation": NotRequired[NamedEntityAggTypeType],
        "AggregationFunctionParameters": NotRequired[Dict[str, str]],
    },
)
NamedEntityDefinitionMetricTypeDef = TypedDict(
    "NamedEntityDefinitionMetricTypeDef",
    {
        "Aggregation": NotRequired[NamedEntityAggTypeType],
        "AggregationFunctionParameters": NotRequired[Mapping[str, str]],
    },
)
NamedEntityRefTypeDef = TypedDict(
    "NamedEntityRefTypeDef",
    {
        "NamedEntityName": NotRequired[str],
    },
)
NamespaceErrorTypeDef = TypedDict(
    "NamespaceErrorTypeDef",
    {
        "Type": NotRequired[NamespaceErrorTypeType],
        "Message": NotRequired[str],
    },
)
NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "SubnetId": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "ErrorMessage": NotRequired[str],
        "Status": NotRequired[NetworkInterfaceStatusType],
        "NetworkInterfaceId": NotRequired[str],
    },
)
NewDefaultValuesOutputTypeDef = TypedDict(
    "NewDefaultValuesOutputTypeDef",
    {
        "StringStaticValues": NotRequired[List[str]],
        "DecimalStaticValues": NotRequired[List[float]],
        "DateTimeStaticValues": NotRequired[List[datetime]],
        "IntegerStaticValues": NotRequired[List[int]],
    },
)
NumericRangeFilterValueTypeDef = TypedDict(
    "NumericRangeFilterValueTypeDef",
    {
        "StaticValue": NotRequired[float],
        "Parameter": NotRequired[str],
    },
)
ThousandSeparatorOptionsTypeDef = TypedDict(
    "ThousandSeparatorOptionsTypeDef",
    {
        "Symbol": NotRequired[NumericSeparatorSymbolType],
        "Visibility": NotRequired[VisibilityType],
    },
)
PercentileAggregationTypeDef = TypedDict(
    "PercentileAggregationTypeDef",
    {
        "PercentileValue": NotRequired[float],
    },
)
StringParameterOutputTypeDef = TypedDict(
    "StringParameterOutputTypeDef",
    {
        "Name": str,
        "Values": List[str],
    },
)
PercentVisibleRangeTypeDef = TypedDict(
    "PercentVisibleRangeTypeDef",
    {
        "From": NotRequired[float],
        "To": NotRequired[float],
    },
)
PivotTableConditionalFormattingScopeTypeDef = TypedDict(
    "PivotTableConditionalFormattingScopeTypeDef",
    {
        "Role": NotRequired[PivotTableConditionalFormattingScopeRoleType],
    },
)
PivotTablePaginatedReportOptionsTypeDef = TypedDict(
    "PivotTablePaginatedReportOptionsTypeDef",
    {
        "VerticalOverflowVisibility": NotRequired[VisibilityType],
        "OverflowColumnHeaderVisibility": NotRequired[VisibilityType],
    },
)
PivotTableFieldOptionTypeDef = TypedDict(
    "PivotTableFieldOptionTypeDef",
    {
        "FieldId": str,
        "CustomLabel": NotRequired[str],
        "Visibility": NotRequired[VisibilityType],
    },
)
PivotTableFieldSubtotalOptionsTypeDef = TypedDict(
    "PivotTableFieldSubtotalOptionsTypeDef",
    {
        "FieldId": NotRequired[str],
    },
)
PivotTableRowsLabelOptionsTypeDef = TypedDict(
    "PivotTableRowsLabelOptionsTypeDef",
    {
        "Visibility": NotRequired[VisibilityType],
        "CustomLabel": NotRequired[str],
    },
)
RowAlternateColorOptionsOutputTypeDef = TypedDict(
    "RowAlternateColorOptionsOutputTypeDef",
    {
        "Status": NotRequired[WidgetStatusType],
        "RowAlternateColors": NotRequired[List[str]],
        "UsePrimaryBackgroundColor": NotRequired[WidgetStatusType],
    },
)
ProjectOperationOutputTypeDef = TypedDict(
    "ProjectOperationOutputTypeDef",
    {
        "ProjectedColumns": List[str],
    },
)
ProjectOperationTypeDef = TypedDict(
    "ProjectOperationTypeDef",
    {
        "ProjectedColumns": Sequence[str],
    },
)
RadarChartAreaStyleSettingsTypeDef = TypedDict(
    "RadarChartAreaStyleSettingsTypeDef",
    {
        "Visibility": NotRequired[VisibilityType],
    },
)
RangeConstantTypeDef = TypedDict(
    "RangeConstantTypeDef",
    {
        "Minimum": NotRequired[str],
        "Maximum": NotRequired[str],
    },
)
RedshiftIAMParametersOutputTypeDef = TypedDict(
    "RedshiftIAMParametersOutputTypeDef",
    {
        "RoleArn": str,
        "DatabaseUser": NotRequired[str],
        "DatabaseGroups": NotRequired[List[str]],
        "AutoCreateDatabaseUser": NotRequired[bool],
    },
)
RedshiftIAMParametersTypeDef = TypedDict(
    "RedshiftIAMParametersTypeDef",
    {
        "RoleArn": str,
        "DatabaseUser": NotRequired[str],
        "DatabaseGroups": NotRequired[Sequence[str]],
        "AutoCreateDatabaseUser": NotRequired[bool],
    },
)
ReferenceLineCustomLabelConfigurationTypeDef = TypedDict(
    "ReferenceLineCustomLabelConfigurationTypeDef",
    {
        "CustomLabel": str,
    },
)
ReferenceLineStaticDataConfigurationTypeDef = TypedDict(
    "ReferenceLineStaticDataConfigurationTypeDef",
    {
        "Value": float,
    },
)
ReferenceLineStyleConfigurationTypeDef = TypedDict(
    "ReferenceLineStyleConfigurationTypeDef",
    {
        "Pattern": NotRequired[ReferenceLinePatternTypeType],
        "Color": NotRequired[str],
    },
)
ScheduleRefreshOnEntityTypeDef = TypedDict(
    "ScheduleRefreshOnEntityTypeDef",
    {
        "DayOfWeek": NotRequired[DayOfWeekType],
        "DayOfMonth": NotRequired[str],
    },
)
StatePersistenceConfigurationsTypeDef = TypedDict(
    "StatePersistenceConfigurationsTypeDef",
    {
        "Enabled": bool,
    },
)
RegisteredUserGenerativeQnAEmbeddingConfigurationTypeDef = TypedDict(
    "RegisteredUserGenerativeQnAEmbeddingConfigurationTypeDef",
    {
        "InitialTopicId": NotRequired[str],
    },
)
RegisteredUserQSearchBarEmbeddingConfigurationTypeDef = TypedDict(
    "RegisteredUserQSearchBarEmbeddingConfigurationTypeDef",
    {
        "InitialTopicId": NotRequired[str],
    },
)
RenameColumnOperationTypeDef = TypedDict(
    "RenameColumnOperationTypeDef",
    {
        "ColumnName": str,
        "NewColumnName": str,
    },
)
RestoreAnalysisRequestRequestTypeDef = TypedDict(
    "RestoreAnalysisRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
        "RestoreToFolders": NotRequired[bool],
    },
)
RowAlternateColorOptionsTypeDef = TypedDict(
    "RowAlternateColorOptionsTypeDef",
    {
        "Status": NotRequired[WidgetStatusType],
        "RowAlternateColors": NotRequired[Sequence[str]],
        "UsePrimaryBackgroundColor": NotRequired[WidgetStatusType],
    },
)
RowLevelPermissionTagRuleTypeDef = TypedDict(
    "RowLevelPermissionTagRuleTypeDef",
    {
        "TagKey": str,
        "ColumnName": str,
        "TagMultiValueDelimiter": NotRequired[str],
        "MatchAllValue": NotRequired[str],
    },
)
S3BucketConfigurationTypeDef = TypedDict(
    "S3BucketConfigurationTypeDef",
    {
        "BucketName": str,
        "BucketPrefix": str,
        "BucketRegion": str,
    },
)
UploadSettingsTypeDef = TypedDict(
    "UploadSettingsTypeDef",
    {
        "Format": NotRequired[FileFormatType],
        "StartFromRow": NotRequired[int],
        "ContainsHeader": NotRequired[bool],
        "TextQualifier": NotRequired[TextQualifierType],
        "Delimiter": NotRequired[str],
    },
)
SameSheetTargetVisualConfigurationTypeDef = TypedDict(
    "SameSheetTargetVisualConfigurationTypeDef",
    {
        "TargetVisuals": NotRequired[Sequence[str]],
        "TargetVisualOptions": NotRequired[Literal["ALL_VISUALS"]],
    },
)
SpacingTypeDef = TypedDict(
    "SpacingTypeDef",
    {
        "Top": NotRequired[str],
        "Bottom": NotRequired[str],
        "Left": NotRequired[str],
        "Right": NotRequired[str],
    },
)
SheetVisualScopingConfigurationOutputTypeDef = TypedDict(
    "SheetVisualScopingConfigurationOutputTypeDef",
    {
        "SheetId": str,
        "Scope": FilterVisualScopeType,
        "VisualIds": NotRequired[List[str]],
    },
)
SemanticEntityTypeOutputTypeDef = TypedDict(
    "SemanticEntityTypeOutputTypeDef",
    {
        "TypeName": NotRequired[str],
        "SubTypeName": NotRequired[str],
        "TypeParameters": NotRequired[Dict[str, str]],
    },
)
SemanticEntityTypeTypeDef = TypedDict(
    "SemanticEntityTypeTypeDef",
    {
        "TypeName": NotRequired[str],
        "SubTypeName": NotRequired[str],
        "TypeParameters": NotRequired[Mapping[str, str]],
    },
)
SemanticTypeOutputTypeDef = TypedDict(
    "SemanticTypeOutputTypeDef",
    {
        "TypeName": NotRequired[str],
        "SubTypeName": NotRequired[str],
        "TypeParameters": NotRequired[Dict[str, str]],
        "TruthyCellValue": NotRequired[str],
        "TruthyCellValueSynonyms": NotRequired[List[str]],
        "FalseyCellValue": NotRequired[str],
        "FalseyCellValueSynonyms": NotRequired[List[str]],
    },
)
SemanticTypeTypeDef = TypedDict(
    "SemanticTypeTypeDef",
    {
        "TypeName": NotRequired[str],
        "SubTypeName": NotRequired[str],
        "TypeParameters": NotRequired[Mapping[str, str]],
        "TruthyCellValue": NotRequired[str],
        "TruthyCellValueSynonyms": NotRequired[Sequence[str]],
        "FalseyCellValue": NotRequired[str],
        "FalseyCellValueSynonyms": NotRequired[Sequence[str]],
    },
)
SheetTextBoxTypeDef = TypedDict(
    "SheetTextBoxTypeDef",
    {
        "SheetTextBoxId": str,
        "Content": NotRequired[str],
    },
)
SheetElementConfigurationOverridesTypeDef = TypedDict(
    "SheetElementConfigurationOverridesTypeDef",
    {
        "Visibility": NotRequired[VisibilityType],
    },
)
SheetVisualScopingConfigurationTypeDef = TypedDict(
    "SheetVisualScopingConfigurationTypeDef",
    {
        "SheetId": str,
        "Scope": FilterVisualScopeType,
        "VisualIds": NotRequired[Sequence[str]],
    },
)
ShortFormatTextTypeDef = TypedDict(
    "ShortFormatTextTypeDef",
    {
        "PlainText": NotRequired[str],
        "RichText": NotRequired[str],
    },
)
YAxisOptionsTypeDef = TypedDict(
    "YAxisOptionsTypeDef",
    {
        "YAxis": Literal["PRIMARY_Y_AXIS"],
    },
)
SlotTypeDef = TypedDict(
    "SlotTypeDef",
    {
        "SlotId": NotRequired[str],
        "VisualId": NotRequired[str],
    },
)
SmallMultiplesAxisPropertiesTypeDef = TypedDict(
    "SmallMultiplesAxisPropertiesTypeDef",
    {
        "Scale": NotRequired[SmallMultiplesAxisScaleType],
        "Placement": NotRequired[SmallMultiplesAxisPlacementType],
    },
)
SnapshotAnonymousUserRedactedTypeDef = TypedDict(
    "SnapshotAnonymousUserRedactedTypeDef",
    {
        "RowLevelPermissionTagKeys": NotRequired[List[str]],
    },
)
SnapshotFileSheetSelectionOutputTypeDef = TypedDict(
    "SnapshotFileSheetSelectionOutputTypeDef",
    {
        "SheetId": str,
        "SelectionScope": SnapshotFileSheetSelectionScopeType,
        "VisualIds": NotRequired[List[str]],
    },
)
SnapshotFileSheetSelectionTypeDef = TypedDict(
    "SnapshotFileSheetSelectionTypeDef",
    {
        "SheetId": str,
        "SelectionScope": SnapshotFileSheetSelectionScopeType,
        "VisualIds": NotRequired[Sequence[str]],
    },
)
SnapshotJobResultErrorInfoTypeDef = TypedDict(
    "SnapshotJobResultErrorInfoTypeDef",
    {
        "ErrorMessage": NotRequired[str],
        "ErrorType": NotRequired[str],
    },
)
StartDashboardSnapshotJobScheduleRequestRequestTypeDef = TypedDict(
    "StartDashboardSnapshotJobScheduleRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "ScheduleId": str,
    },
)
StringDatasetParameterDefaultValuesOutputTypeDef = TypedDict(
    "StringDatasetParameterDefaultValuesOutputTypeDef",
    {
        "StaticValues": NotRequired[List[str]],
    },
)
StringDatasetParameterDefaultValuesTypeDef = TypedDict(
    "StringDatasetParameterDefaultValuesTypeDef",
    {
        "StaticValues": NotRequired[Sequence[str]],
    },
)
StringValueWhenUnsetConfigurationTypeDef = TypedDict(
    "StringValueWhenUnsetConfigurationTypeDef",
    {
        "ValueWhenUnsetOption": NotRequired[ValueWhenUnsetOptionType],
        "CustomValue": NotRequired[str],
    },
)
StringParameterTypeDef = TypedDict(
    "StringParameterTypeDef",
    {
        "Name": str,
        "Values": Sequence[str],
    },
)
TableStyleTargetTypeDef = TypedDict(
    "TableStyleTargetTypeDef",
    {
        "CellType": StyledCellTypeType,
    },
)
SuccessfulKeyRegistrationEntryTypeDef = TypedDict(
    "SuccessfulKeyRegistrationEntryTypeDef",
    {
        "KeyArn": str,
        "StatusCode": int,
    },
)
TableCellImageSizingConfigurationTypeDef = TypedDict(
    "TableCellImageSizingConfigurationTypeDef",
    {
        "TableCellImageScalingConfiguration": NotRequired[TableCellImageScalingConfigurationType],
    },
)
TablePaginatedReportOptionsTypeDef = TypedDict(
    "TablePaginatedReportOptionsTypeDef",
    {
        "VerticalOverflowVisibility": NotRequired[VisibilityType],
        "OverflowColumnHeaderVisibility": NotRequired[VisibilityType],
    },
)
TableFieldCustomIconContentTypeDef = TypedDict(
    "TableFieldCustomIconContentTypeDef",
    {
        "Icon": NotRequired[Literal["LINK"]],
    },
)
TablePinnedFieldOptionsOutputTypeDef = TypedDict(
    "TablePinnedFieldOptionsOutputTypeDef",
    {
        "PinnedLeftFields": NotRequired[List[str]],
    },
)
TablePinnedFieldOptionsTypeDef = TypedDict(
    "TablePinnedFieldOptionsTypeDef",
    {
        "PinnedLeftFields": NotRequired[Sequence[str]],
    },
)
TemplateSourceTemplateTypeDef = TypedDict(
    "TemplateSourceTemplateTypeDef",
    {
        "Arn": str,
    },
)
TextControlPlaceholderOptionsTypeDef = TypedDict(
    "TextControlPlaceholderOptionsTypeDef",
    {
        "Visibility": NotRequired[VisibilityType],
    },
)
UIColorPaletteTypeDef = TypedDict(
    "UIColorPaletteTypeDef",
    {
        "PrimaryForeground": NotRequired[str],
        "PrimaryBackground": NotRequired[str],
        "SecondaryForeground": NotRequired[str],
        "SecondaryBackground": NotRequired[str],
        "Accent": NotRequired[str],
        "AccentForeground": NotRequired[str],
        "Danger": NotRequired[str],
        "DangerForeground": NotRequired[str],
        "Warning": NotRequired[str],
        "WarningForeground": NotRequired[str],
        "Success": NotRequired[str],
        "SuccessForeground": NotRequired[str],
        "Dimension": NotRequired[str],
        "DimensionForeground": NotRequired[str],
        "Measure": NotRequired[str],
        "MeasureForeground": NotRequired[str],
    },
)
ThemeErrorTypeDef = TypedDict(
    "ThemeErrorTypeDef",
    {
        "Type": NotRequired[Literal["INTERNAL_FAILURE"]],
        "Message": NotRequired[str],
    },
)
TopicConfigOptionsTypeDef = TypedDict(
    "TopicConfigOptionsTypeDef",
    {
        "QBusinessInsightsEnabled": NotRequired[bool],
    },
)
TopicIRComparisonMethodTypeDef = TypedDict(
    "TopicIRComparisonMethodTypeDef",
    {
        "Type": NotRequired[ComparisonMethodTypeType],
        "Period": NotRequired[TopicTimeGranularityType],
        "WindowSize": NotRequired[int],
    },
)
VisualOptionsTypeDef = TypedDict(
    "VisualOptionsTypeDef",
    {
        "type": NotRequired[str],
    },
)
TopicSingularFilterConstantTypeDef = TypedDict(
    "TopicSingularFilterConstantTypeDef",
    {
        "ConstantType": NotRequired[ConstantTypeType],
        "SingularConstant": NotRequired[str],
    },
)
TotalAggregationFunctionTypeDef = TypedDict(
    "TotalAggregationFunctionTypeDef",
    {
        "SimpleTotalAggregationFunction": NotRequired[SimpleTotalAggregationFunctionType],
    },
)
UntagColumnOperationOutputTypeDef = TypedDict(
    "UntagColumnOperationOutputTypeDef",
    {
        "ColumnName": str,
        "TagNames": List[ColumnTagNameType],
    },
)
UntagColumnOperationTypeDef = TypedDict(
    "UntagColumnOperationTypeDef",
    {
        "ColumnName": str,
        "TagNames": Sequence[ColumnTagNameType],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateAccountSettingsRequestRequestTypeDef = TypedDict(
    "UpdateAccountSettingsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DefaultNamespace": str,
        "NotificationEmail": NotRequired[str],
        "TerminationProtectionEnabled": NotRequired[bool],
    },
)
UpdateDashboardLinksRequestRequestTypeDef = TypedDict(
    "UpdateDashboardLinksRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "LinkEntities": Sequence[str],
    },
)
UpdateDashboardPublishedVersionRequestRequestTypeDef = TypedDict(
    "UpdateDashboardPublishedVersionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "VersionNumber": int,
    },
)
UpdateFolderRequestRequestTypeDef = TypedDict(
    "UpdateFolderRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
        "Name": str,
    },
)
UpdateGroupRequestRequestTypeDef = TypedDict(
    "UpdateGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
        "Description": NotRequired[str],
    },
)
UpdateIAMPolicyAssignmentRequestRequestTypeDef = TypedDict(
    "UpdateIAMPolicyAssignmentRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AssignmentName": str,
        "Namespace": str,
        "AssignmentStatus": NotRequired[AssignmentStatusType],
        "PolicyArn": NotRequired[str],
        "Identities": NotRequired[Mapping[str, Sequence[str]]],
    },
)
UpdateIdentityPropagationConfigRequestRequestTypeDef = TypedDict(
    "UpdateIdentityPropagationConfigRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Service": Literal["REDSHIFT"],
        "AuthorizedTargets": NotRequired[Sequence[str]],
    },
)
UpdateIpRestrictionRequestRequestTypeDef = TypedDict(
    "UpdateIpRestrictionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "IpRestrictionRuleMap": NotRequired[Mapping[str, str]],
        "VpcIdRestrictionRuleMap": NotRequired[Mapping[str, str]],
        "VpcEndpointIdRestrictionRuleMap": NotRequired[Mapping[str, str]],
        "Enabled": NotRequired[bool],
    },
)
UpdatePublicSharingSettingsRequestRequestTypeDef = TypedDict(
    "UpdatePublicSharingSettingsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "PublicSharingEnabled": NotRequired[bool],
    },
)
UpdateQPersonalizationConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateQPersonalizationConfigurationRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "PersonalizationMode": PersonalizationModeType,
    },
)
UpdateRoleCustomPermissionRequestRequestTypeDef = TypedDict(
    "UpdateRoleCustomPermissionRequestRequestTypeDef",
    {
        "CustomPermissionsName": str,
        "Role": RoleType,
        "AwsAccountId": str,
        "Namespace": str,
    },
)
UpdateSPICECapacityConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateSPICECapacityConfigurationRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "PurchaseMode": PurchaseModeType,
    },
)
UpdateTemplateAliasRequestRequestTypeDef = TypedDict(
    "UpdateTemplateAliasRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "AliasName": str,
        "TemplateVersionNumber": int,
    },
)
UpdateThemeAliasRequestRequestTypeDef = TypedDict(
    "UpdateThemeAliasRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "AliasName": str,
        "ThemeVersionNumber": int,
    },
)
UpdateUserRequestRequestTypeDef = TypedDict(
    "UpdateUserRequestRequestTypeDef",
    {
        "UserName": str,
        "AwsAccountId": str,
        "Namespace": str,
        "Email": str,
        "Role": UserRoleType,
        "CustomPermissionsName": NotRequired[str],
        "UnapplyCustomPermissions": NotRequired[bool],
        "ExternalLoginFederationProviderType": NotRequired[str],
        "CustomFederationProviderUrl": NotRequired[str],
        "ExternalLoginId": NotRequired[str],
    },
)
UpdateVPCConnectionRequestRequestTypeDef = TypedDict(
    "UpdateVPCConnectionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "VPCConnectionId": str,
        "Name": str,
        "SubnetIds": Sequence[str],
        "SecurityGroupIds": Sequence[str],
        "RoleArn": str,
        "DnsResolvers": NotRequired[Sequence[str]],
    },
)
WaterfallChartGroupColorConfigurationTypeDef = TypedDict(
    "WaterfallChartGroupColorConfigurationTypeDef",
    {
        "PositiveBarColor": NotRequired[str],
        "NegativeBarColor": NotRequired[str],
        "TotalBarColor": NotRequired[str],
    },
)
WaterfallChartOptionsTypeDef = TypedDict(
    "WaterfallChartOptionsTypeDef",
    {
        "TotalBarLabel": NotRequired[str],
    },
)
WordCloudOptionsTypeDef = TypedDict(
    "WordCloudOptionsTypeDef",
    {
        "WordOrientation": NotRequired[WordCloudWordOrientationType],
        "WordScaling": NotRequired[WordCloudWordScalingType],
        "CloudLayout": NotRequired[WordCloudCloudLayoutType],
        "WordCasing": NotRequired[WordCloudWordCasingType],
        "WordPadding": NotRequired[WordCloudWordPaddingType],
        "MaximumStringLength": NotRequired[int],
    },
)
UpdateAccountCustomizationRequestRequestTypeDef = TypedDict(
    "UpdateAccountCustomizationRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AccountCustomization": AccountCustomizationTypeDef,
        "Namespace": NotRequired[str],
    },
)
AggFunctionUnionTypeDef = Union[AggFunctionTypeDef, AggFunctionOutputTypeDef]
AxisLabelReferenceOptionsTypeDef = TypedDict(
    "AxisLabelReferenceOptionsTypeDef",
    {
        "FieldId": str,
        "Column": ColumnIdentifierTypeDef,
    },
)
CascadingControlSourceTypeDef = TypedDict(
    "CascadingControlSourceTypeDef",
    {
        "SourceSheetControlId": NotRequired[str],
        "ColumnToMatch": NotRequired[ColumnIdentifierTypeDef],
    },
)
CategoryDrillDownFilterOutputTypeDef = TypedDict(
    "CategoryDrillDownFilterOutputTypeDef",
    {
        "Column": ColumnIdentifierTypeDef,
        "CategoryValues": List[str],
    },
)
CategoryDrillDownFilterTypeDef = TypedDict(
    "CategoryDrillDownFilterTypeDef",
    {
        "Column": ColumnIdentifierTypeDef,
        "CategoryValues": Sequence[str],
    },
)
ContributionAnalysisDefaultOutputTypeDef = TypedDict(
    "ContributionAnalysisDefaultOutputTypeDef",
    {
        "MeasureFieldId": str,
        "ContributorDimensions": List[ColumnIdentifierTypeDef],
    },
)
ContributionAnalysisDefaultTypeDef = TypedDict(
    "ContributionAnalysisDefaultTypeDef",
    {
        "MeasureFieldId": str,
        "ContributorDimensions": Sequence[ColumnIdentifierTypeDef],
    },
)
DynamicDefaultValueTypeDef = TypedDict(
    "DynamicDefaultValueTypeDef",
    {
        "DefaultValueColumn": ColumnIdentifierTypeDef,
        "UserNameColumn": NotRequired[ColumnIdentifierTypeDef],
        "GroupNameColumn": NotRequired[ColumnIdentifierTypeDef],
    },
)
FilterOperationSelectedFieldsConfigurationOutputTypeDef = TypedDict(
    "FilterOperationSelectedFieldsConfigurationOutputTypeDef",
    {
        "SelectedFields": NotRequired[List[str]],
        "SelectedFieldOptions": NotRequired[Literal["ALL_FIELDS"]],
        "SelectedColumns": NotRequired[List[ColumnIdentifierTypeDef]],
    },
)
FilterOperationSelectedFieldsConfigurationTypeDef = TypedDict(
    "FilterOperationSelectedFieldsConfigurationTypeDef",
    {
        "SelectedFields": NotRequired[Sequence[str]],
        "SelectedFieldOptions": NotRequired[Literal["ALL_FIELDS"]],
        "SelectedColumns": NotRequired[Sequence[ColumnIdentifierTypeDef]],
    },
)
NumericEqualityDrillDownFilterTypeDef = TypedDict(
    "NumericEqualityDrillDownFilterTypeDef",
    {
        "Column": ColumnIdentifierTypeDef,
        "Value": float,
    },
)
ParameterSelectableValuesOutputTypeDef = TypedDict(
    "ParameterSelectableValuesOutputTypeDef",
    {
        "Values": NotRequired[List[str]],
        "LinkToDataSetColumn": NotRequired[ColumnIdentifierTypeDef],
    },
)
ParameterSelectableValuesTypeDef = TypedDict(
    "ParameterSelectableValuesTypeDef",
    {
        "Values": NotRequired[Sequence[str]],
        "LinkToDataSetColumn": NotRequired[ColumnIdentifierTypeDef],
    },
)
TimeRangeDrillDownFilterOutputTypeDef = TypedDict(
    "TimeRangeDrillDownFilterOutputTypeDef",
    {
        "Column": ColumnIdentifierTypeDef,
        "RangeMinimum": datetime,
        "RangeMaximum": datetime,
        "TimeGranularity": TimeGranularityType,
    },
)
AnalysisErrorTypeDef = TypedDict(
    "AnalysisErrorTypeDef",
    {
        "Type": NotRequired[AnalysisErrorTypeType],
        "Message": NotRequired[str],
        "ViolatedEntities": NotRequired[List[EntityTypeDef]],
    },
)
DashboardErrorTypeDef = TypedDict(
    "DashboardErrorTypeDef",
    {
        "Type": NotRequired[DashboardErrorTypeType],
        "Message": NotRequired[str],
        "ViolatedEntities": NotRequired[List[EntityTypeDef]],
    },
)
TemplateErrorTypeDef = TypedDict(
    "TemplateErrorTypeDef",
    {
        "Type": NotRequired[TemplateErrorTypeType],
        "Message": NotRequired[str],
        "ViolatedEntities": NotRequired[List[EntityTypeDef]],
    },
)
SearchAnalysesRequestRequestTypeDef = TypedDict(
    "SearchAnalysesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Filters": Sequence[AnalysisSearchFilterTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
AnalysisSourceTemplateTypeDef = TypedDict(
    "AnalysisSourceTemplateTypeDef",
    {
        "DataSetReferences": Sequence[DataSetReferenceTypeDef],
        "Arn": str,
    },
)
DashboardSourceTemplateTypeDef = TypedDict(
    "DashboardSourceTemplateTypeDef",
    {
        "DataSetReferences": Sequence[DataSetReferenceTypeDef],
        "Arn": str,
    },
)
TemplateSourceAnalysisTypeDef = TypedDict(
    "TemplateSourceAnalysisTypeDef",
    {
        "Arn": str,
        "DataSetReferences": Sequence[DataSetReferenceTypeDef],
    },
)
AnonymousUserDashboardFeatureConfigurationsTypeDef = TypedDict(
    "AnonymousUserDashboardFeatureConfigurationsTypeDef",
    {
        "SharedView": NotRequired[SharedViewConfigurationsTypeDef],
    },
)
AnonymousUserDashboardVisualEmbeddingConfigurationTypeDef = TypedDict(
    "AnonymousUserDashboardVisualEmbeddingConfigurationTypeDef",
    {
        "InitialDashboardVisualId": DashboardVisualIdTypeDef,
    },
)
RegisteredUserDashboardVisualEmbeddingConfigurationTypeDef = TypedDict(
    "RegisteredUserDashboardVisualEmbeddingConfigurationTypeDef",
    {
        "InitialDashboardVisualId": DashboardVisualIdTypeDef,
    },
)
ArcAxisConfigurationTypeDef = TypedDict(
    "ArcAxisConfigurationTypeDef",
    {
        "Range": NotRequired[ArcAxisDisplayRangeTypeDef],
        "ReserveRange": NotRequired[int],
    },
)
AssetBundleCloudFormationOverridePropertyConfigurationOutputTypeDef = TypedDict(
    "AssetBundleCloudFormationOverridePropertyConfigurationOutputTypeDef",
    {
        "ResourceIdOverrideConfiguration": NotRequired[
            AssetBundleExportJobResourceIdOverrideConfigurationTypeDef
        ],
        "VPCConnections": NotRequired[
            List[AssetBundleExportJobVPCConnectionOverridePropertiesOutputTypeDef]
        ],
        "RefreshSchedules": NotRequired[
            List[AssetBundleExportJobRefreshScheduleOverridePropertiesOutputTypeDef]
        ],
        "DataSources": NotRequired[
            List[AssetBundleExportJobDataSourceOverridePropertiesOutputTypeDef]
        ],
        "DataSets": NotRequired[List[AssetBundleExportJobDataSetOverridePropertiesOutputTypeDef]],
        "Themes": NotRequired[List[AssetBundleExportJobThemeOverridePropertiesOutputTypeDef]],
        "Analyses": NotRequired[List[AssetBundleExportJobAnalysisOverridePropertiesOutputTypeDef]],
        "Dashboards": NotRequired[
            List[AssetBundleExportJobDashboardOverridePropertiesOutputTypeDef]
        ],
        "Folders": NotRequired[List[AssetBundleExportJobFolderOverridePropertiesOutputTypeDef]],
    },
)
AssetBundleExportJobAnalysisOverridePropertiesUnionTypeDef = Union[
    AssetBundleExportJobAnalysisOverridePropertiesTypeDef,
    AssetBundleExportJobAnalysisOverridePropertiesOutputTypeDef,
]
AssetBundleExportJobDashboardOverridePropertiesUnionTypeDef = Union[
    AssetBundleExportJobDashboardOverridePropertiesTypeDef,
    AssetBundleExportJobDashboardOverridePropertiesOutputTypeDef,
]
AssetBundleExportJobDataSetOverridePropertiesUnionTypeDef = Union[
    AssetBundleExportJobDataSetOverridePropertiesTypeDef,
    AssetBundleExportJobDataSetOverridePropertiesOutputTypeDef,
]
AssetBundleExportJobDataSourceOverridePropertiesUnionTypeDef = Union[
    AssetBundleExportJobDataSourceOverridePropertiesTypeDef,
    AssetBundleExportJobDataSourceOverridePropertiesOutputTypeDef,
]
AssetBundleExportJobFolderOverridePropertiesUnionTypeDef = Union[
    AssetBundleExportJobFolderOverridePropertiesTypeDef,
    AssetBundleExportJobFolderOverridePropertiesOutputTypeDef,
]
AssetBundleExportJobRefreshScheduleOverridePropertiesUnionTypeDef = Union[
    AssetBundleExportJobRefreshScheduleOverridePropertiesTypeDef,
    AssetBundleExportJobRefreshScheduleOverridePropertiesOutputTypeDef,
]
AssetBundleExportJobThemeOverridePropertiesUnionTypeDef = Union[
    AssetBundleExportJobThemeOverridePropertiesTypeDef,
    AssetBundleExportJobThemeOverridePropertiesOutputTypeDef,
]
AssetBundleExportJobVPCConnectionOverridePropertiesUnionTypeDef = Union[
    AssetBundleExportJobVPCConnectionOverridePropertiesTypeDef,
    AssetBundleExportJobVPCConnectionOverridePropertiesOutputTypeDef,
]
AssetBundleImportJobAnalysisOverridePermissionsOutputTypeDef = TypedDict(
    "AssetBundleImportJobAnalysisOverridePermissionsOutputTypeDef",
    {
        "AnalysisIds": List[str],
        "Permissions": AssetBundleResourcePermissionsOutputTypeDef,
    },
)
AssetBundleImportJobDataSetOverridePermissionsOutputTypeDef = TypedDict(
    "AssetBundleImportJobDataSetOverridePermissionsOutputTypeDef",
    {
        "DataSetIds": List[str],
        "Permissions": AssetBundleResourcePermissionsOutputTypeDef,
    },
)
AssetBundleImportJobDataSourceOverridePermissionsOutputTypeDef = TypedDict(
    "AssetBundleImportJobDataSourceOverridePermissionsOutputTypeDef",
    {
        "DataSourceIds": List[str],
        "Permissions": AssetBundleResourcePermissionsOutputTypeDef,
    },
)
AssetBundleImportJobFolderOverridePermissionsOutputTypeDef = TypedDict(
    "AssetBundleImportJobFolderOverridePermissionsOutputTypeDef",
    {
        "FolderIds": List[str],
        "Permissions": NotRequired[AssetBundleResourcePermissionsOutputTypeDef],
    },
)
AssetBundleImportJobThemeOverridePermissionsOutputTypeDef = TypedDict(
    "AssetBundleImportJobThemeOverridePermissionsOutputTypeDef",
    {
        "ThemeIds": List[str],
        "Permissions": AssetBundleResourcePermissionsOutputTypeDef,
    },
)
AssetBundleResourceLinkSharingConfigurationOutputTypeDef = TypedDict(
    "AssetBundleResourceLinkSharingConfigurationOutputTypeDef",
    {
        "Permissions": NotRequired[AssetBundleResourcePermissionsOutputTypeDef],
    },
)
AssetBundleImportJobAnalysisOverrideTagsOutputTypeDef = TypedDict(
    "AssetBundleImportJobAnalysisOverrideTagsOutputTypeDef",
    {
        "AnalysisIds": List[str],
        "Tags": List[TagTypeDef],
    },
)
AssetBundleImportJobAnalysisOverrideTagsTypeDef = TypedDict(
    "AssetBundleImportJobAnalysisOverrideTagsTypeDef",
    {
        "AnalysisIds": Sequence[str],
        "Tags": Sequence[TagTypeDef],
    },
)
AssetBundleImportJobDashboardOverrideTagsOutputTypeDef = TypedDict(
    "AssetBundleImportJobDashboardOverrideTagsOutputTypeDef",
    {
        "DashboardIds": List[str],
        "Tags": List[TagTypeDef],
    },
)
AssetBundleImportJobDashboardOverrideTagsTypeDef = TypedDict(
    "AssetBundleImportJobDashboardOverrideTagsTypeDef",
    {
        "DashboardIds": Sequence[str],
        "Tags": Sequence[TagTypeDef],
    },
)
AssetBundleImportJobDataSetOverrideTagsOutputTypeDef = TypedDict(
    "AssetBundleImportJobDataSetOverrideTagsOutputTypeDef",
    {
        "DataSetIds": List[str],
        "Tags": List[TagTypeDef],
    },
)
AssetBundleImportJobDataSetOverrideTagsTypeDef = TypedDict(
    "AssetBundleImportJobDataSetOverrideTagsTypeDef",
    {
        "DataSetIds": Sequence[str],
        "Tags": Sequence[TagTypeDef],
    },
)
AssetBundleImportJobDataSourceOverrideTagsOutputTypeDef = TypedDict(
    "AssetBundleImportJobDataSourceOverrideTagsOutputTypeDef",
    {
        "DataSourceIds": List[str],
        "Tags": List[TagTypeDef],
    },
)
AssetBundleImportJobDataSourceOverrideTagsTypeDef = TypedDict(
    "AssetBundleImportJobDataSourceOverrideTagsTypeDef",
    {
        "DataSourceIds": Sequence[str],
        "Tags": Sequence[TagTypeDef],
    },
)
AssetBundleImportJobFolderOverrideTagsOutputTypeDef = TypedDict(
    "AssetBundleImportJobFolderOverrideTagsOutputTypeDef",
    {
        "FolderIds": List[str],
        "Tags": List[TagTypeDef],
    },
)
AssetBundleImportJobFolderOverrideTagsTypeDef = TypedDict(
    "AssetBundleImportJobFolderOverrideTagsTypeDef",
    {
        "FolderIds": Sequence[str],
        "Tags": Sequence[TagTypeDef],
    },
)
AssetBundleImportJobThemeOverrideTagsOutputTypeDef = TypedDict(
    "AssetBundleImportJobThemeOverrideTagsOutputTypeDef",
    {
        "ThemeIds": List[str],
        "Tags": List[TagTypeDef],
    },
)
AssetBundleImportJobThemeOverrideTagsTypeDef = TypedDict(
    "AssetBundleImportJobThemeOverrideTagsTypeDef",
    {
        "ThemeIds": Sequence[str],
        "Tags": Sequence[TagTypeDef],
    },
)
AssetBundleImportJobVPCConnectionOverrideTagsOutputTypeDef = TypedDict(
    "AssetBundleImportJobVPCConnectionOverrideTagsOutputTypeDef",
    {
        "VPCConnectionIds": List[str],
        "Tags": List[TagTypeDef],
    },
)
AssetBundleImportJobVPCConnectionOverrideTagsTypeDef = TypedDict(
    "AssetBundleImportJobVPCConnectionOverrideTagsTypeDef",
    {
        "VPCConnectionIds": Sequence[str],
        "Tags": Sequence[TagTypeDef],
    },
)
CreateAccountCustomizationRequestRequestTypeDef = TypedDict(
    "CreateAccountCustomizationRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AccountCustomization": AccountCustomizationTypeDef,
        "Namespace": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateNamespaceRequestRequestTypeDef = TypedDict(
    "CreateNamespaceRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
        "IdentityStore": Literal["QUICKSIGHT"],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateVPCConnectionRequestRequestTypeDef = TypedDict(
    "CreateVPCConnectionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "VPCConnectionId": str,
        "Name": str,
        "SubnetIds": Sequence[str],
        "SecurityGroupIds": Sequence[str],
        "RoleArn": str,
        "DnsResolvers": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
RegisterUserRequestRequestTypeDef = TypedDict(
    "RegisterUserRequestRequestTypeDef",
    {
        "IdentityType": IdentityTypeType,
        "Email": str,
        "UserRole": UserRoleType,
        "AwsAccountId": str,
        "Namespace": str,
        "IamArn": NotRequired[str],
        "SessionName": NotRequired[str],
        "UserName": NotRequired[str],
        "CustomPermissionsName": NotRequired[str],
        "ExternalLoginFederationProviderType": NotRequired[str],
        "CustomFederationProviderUrl": NotRequired[str],
        "ExternalLoginId": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
AssetBundleImportJobDataSourceCredentialsTypeDef = TypedDict(
    "AssetBundleImportJobDataSourceCredentialsTypeDef",
    {
        "CredentialPair": NotRequired[AssetBundleImportJobDataSourceCredentialPairTypeDef],
        "SecretArn": NotRequired[str],
    },
)
AssetBundleImportJobRefreshScheduleOverrideParametersTypeDef = TypedDict(
    "AssetBundleImportJobRefreshScheduleOverrideParametersTypeDef",
    {
        "DataSetId": str,
        "ScheduleId": str,
        "StartAfterDateTime": NotRequired[TimestampTypeDef],
    },
)
CustomParameterValuesTypeDef = TypedDict(
    "CustomParameterValuesTypeDef",
    {
        "StringValues": NotRequired[Sequence[str]],
        "IntegerValues": NotRequired[Sequence[int]],
        "DecimalValues": NotRequired[Sequence[float]],
        "DateTimeValues": NotRequired[Sequence[TimestampTypeDef]],
    },
)
DateTimeDatasetParameterDefaultValuesTypeDef = TypedDict(
    "DateTimeDatasetParameterDefaultValuesTypeDef",
    {
        "StaticValues": NotRequired[Sequence[TimestampTypeDef]],
    },
)
DateTimeParameterTypeDef = TypedDict(
    "DateTimeParameterTypeDef",
    {
        "Name": str,
        "Values": Sequence[TimestampTypeDef],
    },
)
DateTimeValueWhenUnsetConfigurationTypeDef = TypedDict(
    "DateTimeValueWhenUnsetConfigurationTypeDef",
    {
        "ValueWhenUnsetOption": NotRequired[ValueWhenUnsetOptionType],
        "CustomValue": NotRequired[TimestampTypeDef],
    },
)
NewDefaultValuesTypeDef = TypedDict(
    "NewDefaultValuesTypeDef",
    {
        "StringStaticValues": NotRequired[Sequence[str]],
        "DecimalStaticValues": NotRequired[Sequence[float]],
        "DateTimeStaticValues": NotRequired[Sequence[TimestampTypeDef]],
        "IntegerStaticValues": NotRequired[Sequence[int]],
    },
)
TimeRangeDrillDownFilterTypeDef = TypedDict(
    "TimeRangeDrillDownFilterTypeDef",
    {
        "Column": ColumnIdentifierTypeDef,
        "RangeMinimum": TimestampTypeDef,
        "RangeMaximum": TimestampTypeDef,
        "TimeGranularity": TimeGranularityType,
    },
)
TopicRefreshScheduleTypeDef = TypedDict(
    "TopicRefreshScheduleTypeDef",
    {
        "IsEnabled": bool,
        "BasedOnSpiceSchedule": bool,
        "StartingAt": NotRequired[TimestampTypeDef],
        "Timezone": NotRequired[str],
        "RepeatAt": NotRequired[str],
        "TopicScheduleType": NotRequired[TopicScheduleTypeType],
    },
)
WhatIfPointScenarioTypeDef = TypedDict(
    "WhatIfPointScenarioTypeDef",
    {
        "Date": TimestampTypeDef,
        "Value": float,
    },
)
WhatIfRangeScenarioTypeDef = TypedDict(
    "WhatIfRangeScenarioTypeDef",
    {
        "StartDate": TimestampTypeDef,
        "EndDate": TimestampTypeDef,
        "Value": float,
    },
)
AssetBundleImportJobVPCConnectionOverrideParametersUnionTypeDef = Union[
    AssetBundleImportJobVPCConnectionOverrideParametersTypeDef,
    AssetBundleImportJobVPCConnectionOverrideParametersOutputTypeDef,
]
AssetBundleImportSourceTypeDef = TypedDict(
    "AssetBundleImportSourceTypeDef",
    {
        "Body": NotRequired[BlobTypeDef],
        "S3Uri": NotRequired[str],
    },
)
AssetBundleResourcePermissionsUnionTypeDef = Union[
    AssetBundleResourcePermissionsTypeDef, AssetBundleResourcePermissionsOutputTypeDef
]
AxisDisplayRangeOutputTypeDef = TypedDict(
    "AxisDisplayRangeOutputTypeDef",
    {
        "MinMax": NotRequired[AxisDisplayMinMaxRangeTypeDef],
        "DataDriven": NotRequired[Dict[str, Any]],
    },
)
AxisDisplayRangeTypeDef = TypedDict(
    "AxisDisplayRangeTypeDef",
    {
        "MinMax": NotRequired[AxisDisplayMinMaxRangeTypeDef],
        "DataDriven": NotRequired[Mapping[str, Any]],
    },
)
AxisScaleTypeDef = TypedDict(
    "AxisScaleTypeDef",
    {
        "Linear": NotRequired[AxisLinearScaleTypeDef],
        "Logarithmic": NotRequired[AxisLogarithmicScaleTypeDef],
    },
)
ScatterPlotSortConfigurationTypeDef = TypedDict(
    "ScatterPlotSortConfigurationTypeDef",
    {
        "ScatterPlotLimitConfiguration": NotRequired[ItemsLimitConfigurationTypeDef],
    },
)
CancelIngestionResponseTypeDef = TypedDict(
    "CancelIngestionResponseTypeDef",
    {
        "Arn": str,
        "IngestionId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAccountCustomizationResponseTypeDef = TypedDict(
    "CreateAccountCustomizationResponseTypeDef",
    {
        "Arn": str,
        "AwsAccountId": str,
        "Namespace": str,
        "AccountCustomization": AccountCustomizationTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAnalysisResponseTypeDef = TypedDict(
    "CreateAnalysisResponseTypeDef",
    {
        "Arn": str,
        "AnalysisId": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDashboardResponseTypeDef = TypedDict(
    "CreateDashboardResponseTypeDef",
    {
        "Arn": str,
        "VersionArn": str,
        "DashboardId": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDataSetResponseTypeDef = TypedDict(
    "CreateDataSetResponseTypeDef",
    {
        "Arn": str,
        "DataSetId": str,
        "IngestionArn": str,
        "IngestionId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDataSourceResponseTypeDef = TypedDict(
    "CreateDataSourceResponseTypeDef",
    {
        "Arn": str,
        "DataSourceId": str,
        "CreationStatus": ResourceStatusType,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFolderResponseTypeDef = TypedDict(
    "CreateFolderResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "FolderId": str,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateIAMPolicyAssignmentResponseTypeDef = TypedDict(
    "CreateIAMPolicyAssignmentResponseTypeDef",
    {
        "AssignmentName": str,
        "AssignmentId": str,
        "AssignmentStatus": AssignmentStatusType,
        "PolicyArn": str,
        "Identities": Dict[str, List[str]],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateIngestionResponseTypeDef = TypedDict(
    "CreateIngestionResponseTypeDef",
    {
        "Arn": str,
        "IngestionId": str,
        "IngestionStatus": IngestionStatusType,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateNamespaceResponseTypeDef = TypedDict(
    "CreateNamespaceResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "CapacityRegion": str,
        "CreationStatus": NamespaceStatusType,
        "IdentityStore": Literal["QUICKSIGHT"],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRefreshScheduleResponseTypeDef = TypedDict(
    "CreateRefreshScheduleResponseTypeDef",
    {
        "Status": int,
        "RequestId": str,
        "ScheduleId": str,
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRoleMembershipResponseTypeDef = TypedDict(
    "CreateRoleMembershipResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTemplateResponseTypeDef = TypedDict(
    "CreateTemplateResponseTypeDef",
    {
        "Arn": str,
        "VersionArn": str,
        "TemplateId": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateThemeResponseTypeDef = TypedDict(
    "CreateThemeResponseTypeDef",
    {
        "Arn": str,
        "VersionArn": str,
        "ThemeId": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTopicRefreshScheduleResponseTypeDef = TypedDict(
    "CreateTopicRefreshScheduleResponseTypeDef",
    {
        "TopicId": str,
        "TopicArn": str,
        "DatasetArn": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTopicResponseTypeDef = TypedDict(
    "CreateTopicResponseTypeDef",
    {
        "Arn": str,
        "TopicId": str,
        "RefreshArn": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateVPCConnectionResponseTypeDef = TypedDict(
    "CreateVPCConnectionResponseTypeDef",
    {
        "Arn": str,
        "VPCConnectionId": str,
        "CreationStatus": VPCConnectionResourceStatusType,
        "AvailabilityStatus": VPCConnectionAvailabilityStatusType,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteAccountCustomizationResponseTypeDef = TypedDict(
    "DeleteAccountCustomizationResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteAccountSubscriptionResponseTypeDef = TypedDict(
    "DeleteAccountSubscriptionResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteAnalysisResponseTypeDef = TypedDict(
    "DeleteAnalysisResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "AnalysisId": str,
        "DeletionTime": datetime,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDashboardResponseTypeDef = TypedDict(
    "DeleteDashboardResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "DashboardId": str,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDataSetRefreshPropertiesResponseTypeDef = TypedDict(
    "DeleteDataSetRefreshPropertiesResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDataSetResponseTypeDef = TypedDict(
    "DeleteDataSetResponseTypeDef",
    {
        "Arn": str,
        "DataSetId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDataSourceResponseTypeDef = TypedDict(
    "DeleteDataSourceResponseTypeDef",
    {
        "Arn": str,
        "DataSourceId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteFolderMembershipResponseTypeDef = TypedDict(
    "DeleteFolderMembershipResponseTypeDef",
    {
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteFolderResponseTypeDef = TypedDict(
    "DeleteFolderResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "FolderId": str,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteGroupMembershipResponseTypeDef = TypedDict(
    "DeleteGroupMembershipResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteGroupResponseTypeDef = TypedDict(
    "DeleteGroupResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteIAMPolicyAssignmentResponseTypeDef = TypedDict(
    "DeleteIAMPolicyAssignmentResponseTypeDef",
    {
        "AssignmentName": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteIdentityPropagationConfigResponseTypeDef = TypedDict(
    "DeleteIdentityPropagationConfigResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteNamespaceResponseTypeDef = TypedDict(
    "DeleteNamespaceResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteRefreshScheduleResponseTypeDef = TypedDict(
    "DeleteRefreshScheduleResponseTypeDef",
    {
        "Status": int,
        "RequestId": str,
        "ScheduleId": str,
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteRoleCustomPermissionResponseTypeDef = TypedDict(
    "DeleteRoleCustomPermissionResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteRoleMembershipResponseTypeDef = TypedDict(
    "DeleteRoleMembershipResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTemplateAliasResponseTypeDef = TypedDict(
    "DeleteTemplateAliasResponseTypeDef",
    {
        "Status": int,
        "TemplateId": str,
        "AliasName": str,
        "Arn": str,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTemplateResponseTypeDef = TypedDict(
    "DeleteTemplateResponseTypeDef",
    {
        "RequestId": str,
        "Arn": str,
        "TemplateId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteThemeAliasResponseTypeDef = TypedDict(
    "DeleteThemeAliasResponseTypeDef",
    {
        "AliasName": str,
        "Arn": str,
        "RequestId": str,
        "Status": int,
        "ThemeId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteThemeResponseTypeDef = TypedDict(
    "DeleteThemeResponseTypeDef",
    {
        "Arn": str,
        "RequestId": str,
        "Status": int,
        "ThemeId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTopicRefreshScheduleResponseTypeDef = TypedDict(
    "DeleteTopicRefreshScheduleResponseTypeDef",
    {
        "TopicId": str,
        "TopicArn": str,
        "DatasetArn": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTopicResponseTypeDef = TypedDict(
    "DeleteTopicResponseTypeDef",
    {
        "Arn": str,
        "TopicId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteUserByPrincipalIdResponseTypeDef = TypedDict(
    "DeleteUserByPrincipalIdResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteUserResponseTypeDef = TypedDict(
    "DeleteUserResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteVPCConnectionResponseTypeDef = TypedDict(
    "DeleteVPCConnectionResponseTypeDef",
    {
        "Arn": str,
        "VPCConnectionId": str,
        "DeletionStatus": VPCConnectionResourceStatusType,
        "AvailabilityStatus": VPCConnectionAvailabilityStatusType,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAccountCustomizationResponseTypeDef = TypedDict(
    "DescribeAccountCustomizationResponseTypeDef",
    {
        "Arn": str,
        "AwsAccountId": str,
        "Namespace": str,
        "AccountCustomization": AccountCustomizationTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAccountSettingsResponseTypeDef = TypedDict(
    "DescribeAccountSettingsResponseTypeDef",
    {
        "AccountSettings": AccountSettingsTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAccountSubscriptionResponseTypeDef = TypedDict(
    "DescribeAccountSubscriptionResponseTypeDef",
    {
        "AccountInfo": AccountInfoTypeDef,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeIpRestrictionResponseTypeDef = TypedDict(
    "DescribeIpRestrictionResponseTypeDef",
    {
        "AwsAccountId": str,
        "IpRestrictionRuleMap": Dict[str, str],
        "VpcIdRestrictionRuleMap": Dict[str, str],
        "VpcEndpointIdRestrictionRuleMap": Dict[str, str],
        "Enabled": bool,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeQPersonalizationConfigurationResponseTypeDef = TypedDict(
    "DescribeQPersonalizationConfigurationResponseTypeDef",
    {
        "PersonalizationMode": PersonalizationModeType,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRoleCustomPermissionResponseTypeDef = TypedDict(
    "DescribeRoleCustomPermissionResponseTypeDef",
    {
        "CustomPermissionsName": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GenerateEmbedUrlForAnonymousUserResponseTypeDef = TypedDict(
    "GenerateEmbedUrlForAnonymousUserResponseTypeDef",
    {
        "EmbedUrl": str,
        "Status": int,
        "RequestId": str,
        "AnonymousUserArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GenerateEmbedUrlForRegisteredUserResponseTypeDef = TypedDict(
    "GenerateEmbedUrlForRegisteredUserResponseTypeDef",
    {
        "EmbedUrl": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDashboardEmbedUrlResponseTypeDef = TypedDict(
    "GetDashboardEmbedUrlResponseTypeDef",
    {
        "EmbedUrl": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSessionEmbedUrlResponseTypeDef = TypedDict(
    "GetSessionEmbedUrlResponseTypeDef",
    {
        "EmbedUrl": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAnalysesResponseTypeDef = TypedDict(
    "ListAnalysesResponseTypeDef",
    {
        "AnalysisSummaryList": List[AnalysisSummaryTypeDef],
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListAssetBundleExportJobsResponseTypeDef = TypedDict(
    "ListAssetBundleExportJobsResponseTypeDef",
    {
        "AssetBundleExportJobSummaryList": List[AssetBundleExportJobSummaryTypeDef],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListAssetBundleImportJobsResponseTypeDef = TypedDict(
    "ListAssetBundleImportJobsResponseTypeDef",
    {
        "AssetBundleImportJobSummaryList": List[AssetBundleImportJobSummaryTypeDef],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListFoldersForResourceResponseTypeDef = TypedDict(
    "ListFoldersForResourceResponseTypeDef",
    {
        "Status": int,
        "Folders": List[str],
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListIAMPolicyAssignmentsForUserResponseTypeDef = TypedDict(
    "ListIAMPolicyAssignmentsForUserResponseTypeDef",
    {
        "ActiveAssignments": List[ActiveIAMPolicyAssignmentTypeDef],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListIdentityPropagationConfigsResponseTypeDef = TypedDict(
    "ListIdentityPropagationConfigsResponseTypeDef",
    {
        "Services": List[AuthorizedTargetsByServiceTypeDef],
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListRoleMembershipsResponseTypeDef = TypedDict(
    "ListRoleMembershipsResponseTypeDef",
    {
        "MembersList": List[str],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutDataSetRefreshPropertiesResponseTypeDef = TypedDict(
    "PutDataSetRefreshPropertiesResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreAnalysisResponseTypeDef = TypedDict(
    "RestoreAnalysisResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "AnalysisId": str,
        "RequestId": str,
        "RestorationFailedFolderArns": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchAnalysesResponseTypeDef = TypedDict(
    "SearchAnalysesResponseTypeDef",
    {
        "AnalysisSummaryList": List[AnalysisSummaryTypeDef],
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
StartAssetBundleExportJobResponseTypeDef = TypedDict(
    "StartAssetBundleExportJobResponseTypeDef",
    {
        "Arn": str,
        "AssetBundleExportJobId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartAssetBundleImportJobResponseTypeDef = TypedDict(
    "StartAssetBundleImportJobResponseTypeDef",
    {
        "Arn": str,
        "AssetBundleImportJobId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartDashboardSnapshotJobResponseTypeDef = TypedDict(
    "StartDashboardSnapshotJobResponseTypeDef",
    {
        "Arn": str,
        "SnapshotJobId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartDashboardSnapshotJobScheduleResponseTypeDef = TypedDict(
    "StartDashboardSnapshotJobScheduleResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceResponseTypeDef = TypedDict(
    "TagResourceResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UntagResourceResponseTypeDef = TypedDict(
    "UntagResourceResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAccountCustomizationResponseTypeDef = TypedDict(
    "UpdateAccountCustomizationResponseTypeDef",
    {
        "Arn": str,
        "AwsAccountId": str,
        "Namespace": str,
        "AccountCustomization": AccountCustomizationTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAccountSettingsResponseTypeDef = TypedDict(
    "UpdateAccountSettingsResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAnalysisResponseTypeDef = TypedDict(
    "UpdateAnalysisResponseTypeDef",
    {
        "Arn": str,
        "AnalysisId": str,
        "UpdateStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDashboardLinksResponseTypeDef = TypedDict(
    "UpdateDashboardLinksResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "DashboardArn": str,
        "LinkEntities": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDashboardPublishedVersionResponseTypeDef = TypedDict(
    "UpdateDashboardPublishedVersionResponseTypeDef",
    {
        "DashboardId": str,
        "DashboardArn": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDashboardResponseTypeDef = TypedDict(
    "UpdateDashboardResponseTypeDef",
    {
        "Arn": str,
        "VersionArn": str,
        "DashboardId": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDataSetPermissionsResponseTypeDef = TypedDict(
    "UpdateDataSetPermissionsResponseTypeDef",
    {
        "DataSetArn": str,
        "DataSetId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDataSetResponseTypeDef = TypedDict(
    "UpdateDataSetResponseTypeDef",
    {
        "Arn": str,
        "DataSetId": str,
        "IngestionArn": str,
        "IngestionId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDataSourcePermissionsResponseTypeDef = TypedDict(
    "UpdateDataSourcePermissionsResponseTypeDef",
    {
        "DataSourceArn": str,
        "DataSourceId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDataSourceResponseTypeDef = TypedDict(
    "UpdateDataSourceResponseTypeDef",
    {
        "Arn": str,
        "DataSourceId": str,
        "UpdateStatus": ResourceStatusType,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFolderResponseTypeDef = TypedDict(
    "UpdateFolderResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "FolderId": str,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateIAMPolicyAssignmentResponseTypeDef = TypedDict(
    "UpdateIAMPolicyAssignmentResponseTypeDef",
    {
        "AssignmentName": str,
        "AssignmentId": str,
        "PolicyArn": str,
        "Identities": Dict[str, List[str]],
        "AssignmentStatus": AssignmentStatusType,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateIdentityPropagationConfigResponseTypeDef = TypedDict(
    "UpdateIdentityPropagationConfigResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateIpRestrictionResponseTypeDef = TypedDict(
    "UpdateIpRestrictionResponseTypeDef",
    {
        "AwsAccountId": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePublicSharingSettingsResponseTypeDef = TypedDict(
    "UpdatePublicSharingSettingsResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateQPersonalizationConfigurationResponseTypeDef = TypedDict(
    "UpdateQPersonalizationConfigurationResponseTypeDef",
    {
        "PersonalizationMode": PersonalizationModeType,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRefreshScheduleResponseTypeDef = TypedDict(
    "UpdateRefreshScheduleResponseTypeDef",
    {
        "Status": int,
        "RequestId": str,
        "ScheduleId": str,
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRoleCustomPermissionResponseTypeDef = TypedDict(
    "UpdateRoleCustomPermissionResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSPICECapacityConfigurationResponseTypeDef = TypedDict(
    "UpdateSPICECapacityConfigurationResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTemplateResponseTypeDef = TypedDict(
    "UpdateTemplateResponseTypeDef",
    {
        "TemplateId": str,
        "Arn": str,
        "VersionArn": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateThemeResponseTypeDef = TypedDict(
    "UpdateThemeResponseTypeDef",
    {
        "ThemeId": str,
        "Arn": str,
        "VersionArn": str,
        "CreationStatus": ResourceStatusType,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTopicRefreshScheduleResponseTypeDef = TypedDict(
    "UpdateTopicRefreshScheduleResponseTypeDef",
    {
        "TopicId": str,
        "TopicArn": str,
        "DatasetArn": str,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTopicResponseTypeDef = TypedDict(
    "UpdateTopicResponseTypeDef",
    {
        "TopicId": str,
        "Arn": str,
        "RefreshArn": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateVPCConnectionResponseTypeDef = TypedDict(
    "UpdateVPCConnectionResponseTypeDef",
    {
        "Arn": str,
        "VPCConnectionId": str,
        "UpdateStatus": VPCConnectionResourceStatusType,
        "AvailabilityStatus": VPCConnectionAvailabilityStatusType,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchCreateTopicReviewedAnswerResponseTypeDef = TypedDict(
    "BatchCreateTopicReviewedAnswerResponseTypeDef",
    {
        "TopicId": str,
        "TopicArn": str,
        "SucceededAnswers": List[SucceededTopicReviewedAnswerTypeDef],
        "InvalidAnswers": List[InvalidTopicReviewedAnswerTypeDef],
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDeleteTopicReviewedAnswerResponseTypeDef = TypedDict(
    "BatchDeleteTopicReviewedAnswerResponseTypeDef",
    {
        "TopicId": str,
        "TopicArn": str,
        "SucceededAnswers": List[SucceededTopicReviewedAnswerTypeDef],
        "InvalidAnswers": List[InvalidTopicReviewedAnswerTypeDef],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
HistogramBinOptionsTypeDef = TypedDict(
    "HistogramBinOptionsTypeDef",
    {
        "SelectedBinType": NotRequired[HistogramBinTypeType],
        "BinCount": NotRequired[BinCountOptionsTypeDef],
        "BinWidth": NotRequired[BinWidthOptionsTypeDef],
        "StartValue": NotRequired[float],
    },
)
BodySectionRepeatPageBreakConfigurationTypeDef = TypedDict(
    "BodySectionRepeatPageBreakConfigurationTypeDef",
    {
        "After": NotRequired[SectionAfterPageBreakTypeDef],
    },
)
SectionPageBreakConfigurationTypeDef = TypedDict(
    "SectionPageBreakConfigurationTypeDef",
    {
        "After": NotRequired[SectionAfterPageBreakTypeDef],
    },
)
TileStyleTypeDef = TypedDict(
    "TileStyleTypeDef",
    {
        "Border": NotRequired[BorderStyleTypeDef],
    },
)
BoxPlotOptionsTypeDef = TypedDict(
    "BoxPlotOptionsTypeDef",
    {
        "StyleOptions": NotRequired[BoxPlotStyleOptionsTypeDef],
        "OutlierVisibility": NotRequired[VisibilityType],
        "AllDataPointsVisibility": NotRequired[VisibilityType],
    },
)
CreateColumnsOperationOutputTypeDef = TypedDict(
    "CreateColumnsOperationOutputTypeDef",
    {
        "Columns": List[CalculatedColumnTypeDef],
    },
)
CreateColumnsOperationTypeDef = TypedDict(
    "CreateColumnsOperationTypeDef",
    {
        "Columns": Sequence[CalculatedColumnTypeDef],
    },
)
CategoryFilterConfigurationOutputTypeDef = TypedDict(
    "CategoryFilterConfigurationOutputTypeDef",
    {
        "FilterListConfiguration": NotRequired[FilterListConfigurationOutputTypeDef],
        "CustomFilterListConfiguration": NotRequired[CustomFilterListConfigurationOutputTypeDef],
        "CustomFilterConfiguration": NotRequired[CustomFilterConfigurationTypeDef],
    },
)
CellValueSynonymUnionTypeDef = Union[CellValueSynonymTypeDef, CellValueSynonymOutputTypeDef]
ClusterMarkerTypeDef = TypedDict(
    "ClusterMarkerTypeDef",
    {
        "SimpleClusterMarker": NotRequired[SimpleClusterMarkerTypeDef],
    },
)
TopicConstantValueOutputTypeDef = TypedDict(
    "TopicConstantValueOutputTypeDef",
    {
        "ConstantType": NotRequired[ConstantTypeType],
        "Value": NotRequired[str],
        "Minimum": NotRequired[str],
        "Maximum": NotRequired[str],
        "ValueList": NotRequired[List[CollectiveConstantEntryTypeDef]],
    },
)
TopicConstantValueTypeDef = TypedDict(
    "TopicConstantValueTypeDef",
    {
        "ConstantType": NotRequired[ConstantTypeType],
        "Value": NotRequired[str],
        "Minimum": NotRequired[str],
        "Maximum": NotRequired[str],
        "ValueList": NotRequired[Sequence[CollectiveConstantEntryTypeDef]],
    },
)
TopicCategoryFilterConstantOutputTypeDef = TypedDict(
    "TopicCategoryFilterConstantOutputTypeDef",
    {
        "ConstantType": NotRequired[ConstantTypeType],
        "SingularConstant": NotRequired[str],
        "CollectiveConstant": NotRequired[CollectiveConstantOutputTypeDef],
    },
)
CollectiveConstantUnionTypeDef = Union[CollectiveConstantTypeDef, CollectiveConstantOutputTypeDef]
ColorScaleOutputTypeDef = TypedDict(
    "ColorScaleOutputTypeDef",
    {
        "Colors": List[DataColorTypeDef],
        "ColorFillType": ColorFillTypeType,
        "NullValueColor": NotRequired[DataColorTypeDef],
    },
)
ColorScaleTypeDef = TypedDict(
    "ColorScaleTypeDef",
    {
        "Colors": Sequence[DataColorTypeDef],
        "ColorFillType": ColorFillTypeType,
        "NullValueColor": NotRequired[DataColorTypeDef],
    },
)
ColorsConfigurationOutputTypeDef = TypedDict(
    "ColorsConfigurationOutputTypeDef",
    {
        "CustomColors": NotRequired[List[CustomColorTypeDef]],
    },
)
ColorsConfigurationTypeDef = TypedDict(
    "ColorsConfigurationTypeDef",
    {
        "CustomColors": NotRequired[Sequence[CustomColorTypeDef]],
    },
)
ColumnTagTypeDef = TypedDict(
    "ColumnTagTypeDef",
    {
        "ColumnGeographicRole": NotRequired[GeoSpatialDataRoleType],
        "ColumnDescription": NotRequired[ColumnDescriptionTypeDef],
    },
)
ColumnGroupSchemaOutputTypeDef = TypedDict(
    "ColumnGroupSchemaOutputTypeDef",
    {
        "Name": NotRequired[str],
        "ColumnGroupColumnSchemaList": NotRequired[List[ColumnGroupColumnSchemaTypeDef]],
    },
)
ColumnGroupSchemaTypeDef = TypedDict(
    "ColumnGroupSchemaTypeDef",
    {
        "Name": NotRequired[str],
        "ColumnGroupColumnSchemaList": NotRequired[Sequence[ColumnGroupColumnSchemaTypeDef]],
    },
)
ColumnGroupOutputTypeDef = TypedDict(
    "ColumnGroupOutputTypeDef",
    {
        "GeoSpatialColumnGroup": NotRequired[GeoSpatialColumnGroupOutputTypeDef],
    },
)
ColumnLevelPermissionRuleUnionTypeDef = Union[
    ColumnLevelPermissionRuleTypeDef, ColumnLevelPermissionRuleOutputTypeDef
]
DataSetSchemaOutputTypeDef = TypedDict(
    "DataSetSchemaOutputTypeDef",
    {
        "ColumnSchemaList": NotRequired[List[ColumnSchemaTypeDef]],
    },
)
DataSetSchemaTypeDef = TypedDict(
    "DataSetSchemaTypeDef",
    {
        "ColumnSchemaList": NotRequired[Sequence[ColumnSchemaTypeDef]],
    },
)
ComparativeOrderUnionTypeDef = Union[ComparativeOrderTypeDef, ComparativeOrderOutputTypeDef]
ConditionalFormattingCustomIconConditionTypeDef = TypedDict(
    "ConditionalFormattingCustomIconConditionTypeDef",
    {
        "Expression": str,
        "IconOptions": ConditionalFormattingCustomIconOptionsTypeDef,
        "Color": NotRequired[str],
        "DisplayConfiguration": NotRequired[ConditionalFormattingIconDisplayConfigurationTypeDef],
    },
)
CreateAccountSubscriptionResponseTypeDef = TypedDict(
    "CreateAccountSubscriptionResponseTypeDef",
    {
        "SignupResponse": SignupResponseTypeDef,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFolderRequestRequestTypeDef = TypedDict(
    "CreateFolderRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
        "Name": NotRequired[str],
        "FolderType": NotRequired[FolderTypeType],
        "ParentFolderArn": NotRequired[str],
        "Permissions": NotRequired[Sequence[ResourcePermissionTypeDef]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "SharingModel": NotRequired[SharingModelType],
    },
)
UpdateAnalysisPermissionsRequestRequestTypeDef = TypedDict(
    "UpdateAnalysisPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
        "GrantPermissions": NotRequired[Sequence[ResourcePermissionTypeDef]],
        "RevokePermissions": NotRequired[Sequence[ResourcePermissionTypeDef]],
    },
)
UpdateDashboardPermissionsRequestRequestTypeDef = TypedDict(
    "UpdateDashboardPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "GrantPermissions": NotRequired[Sequence[ResourcePermissionTypeDef]],
        "RevokePermissions": NotRequired[Sequence[ResourcePermissionTypeDef]],
        "GrantLinkPermissions": NotRequired[Sequence[ResourcePermissionTypeDef]],
        "RevokeLinkPermissions": NotRequired[Sequence[ResourcePermissionTypeDef]],
    },
)
UpdateDataSetPermissionsRequestRequestTypeDef = TypedDict(
    "UpdateDataSetPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
        "GrantPermissions": NotRequired[Sequence[ResourcePermissionTypeDef]],
        "RevokePermissions": NotRequired[Sequence[ResourcePermissionTypeDef]],
    },
)
UpdateDataSourcePermissionsRequestRequestTypeDef = TypedDict(
    "UpdateDataSourcePermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSourceId": str,
        "GrantPermissions": NotRequired[Sequence[ResourcePermissionTypeDef]],
        "RevokePermissions": NotRequired[Sequence[ResourcePermissionTypeDef]],
    },
)
UpdateFolderPermissionsRequestRequestTypeDef = TypedDict(
    "UpdateFolderPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
        "GrantPermissions": NotRequired[Sequence[ResourcePermissionTypeDef]],
        "RevokePermissions": NotRequired[Sequence[ResourcePermissionTypeDef]],
    },
)
UpdateTemplatePermissionsRequestRequestTypeDef = TypedDict(
    "UpdateTemplatePermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "GrantPermissions": NotRequired[Sequence[ResourcePermissionTypeDef]],
        "RevokePermissions": NotRequired[Sequence[ResourcePermissionTypeDef]],
    },
)
UpdateThemePermissionsRequestRequestTypeDef = TypedDict(
    "UpdateThemePermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "GrantPermissions": NotRequired[Sequence[ResourcePermissionTypeDef]],
        "RevokePermissions": NotRequired[Sequence[ResourcePermissionTypeDef]],
    },
)
UpdateTopicPermissionsRequestRequestTypeDef = TypedDict(
    "UpdateTopicPermissionsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TopicId": str,
        "GrantPermissions": NotRequired[Sequence[ResourcePermissionTypeDef]],
        "RevokePermissions": NotRequired[Sequence[ResourcePermissionTypeDef]],
    },
)
DataSetSummaryTypeDef = TypedDict(
    "DataSetSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "DataSetId": NotRequired[str],
        "Name": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "ImportMode": NotRequired[DataSetImportModeType],
        "RowLevelPermissionDataSet": NotRequired[RowLevelPermissionDataSetTypeDef],
        "RowLevelPermissionTagConfigurationApplied": NotRequired[bool],
        "ColumnLevelPermissionRulesApplied": NotRequired[bool],
    },
)
CreateFolderMembershipResponseTypeDef = TypedDict(
    "CreateFolderMembershipResponseTypeDef",
    {
        "Status": int,
        "FolderMember": FolderMemberTypeDef,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGroupMembershipResponseTypeDef = TypedDict(
    "CreateGroupMembershipResponseTypeDef",
    {
        "GroupMember": GroupMemberTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeGroupMembershipResponseTypeDef = TypedDict(
    "DescribeGroupMembershipResponseTypeDef",
    {
        "GroupMember": GroupMemberTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListGroupMembershipsResponseTypeDef = TypedDict(
    "ListGroupMembershipsResponseTypeDef",
    {
        "GroupMemberList": List[GroupMemberTypeDef],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
CreateGroupResponseTypeDef = TypedDict(
    "CreateGroupResponseTypeDef",
    {
        "Group": GroupTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeGroupResponseTypeDef = TypedDict(
    "DescribeGroupResponseTypeDef",
    {
        "Group": GroupTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListGroupsResponseTypeDef = TypedDict(
    "ListGroupsResponseTypeDef",
    {
        "GroupList": List[GroupTypeDef],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListUserGroupsResponseTypeDef = TypedDict(
    "ListUserGroupsResponseTypeDef",
    {
        "GroupList": List[GroupTypeDef],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
SearchGroupsResponseTypeDef = TypedDict(
    "SearchGroupsResponseTypeDef",
    {
        "GroupList": List[GroupTypeDef],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateGroupResponseTypeDef = TypedDict(
    "UpdateGroupResponseTypeDef",
    {
        "Group": GroupTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTemplateAliasResponseTypeDef = TypedDict(
    "CreateTemplateAliasResponseTypeDef",
    {
        "TemplateAlias": TemplateAliasTypeDef,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTemplateAliasResponseTypeDef = TypedDict(
    "DescribeTemplateAliasResponseTypeDef",
    {
        "TemplateAlias": TemplateAliasTypeDef,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTemplateAliasesResponseTypeDef = TypedDict(
    "ListTemplateAliasesResponseTypeDef",
    {
        "TemplateAliasList": List[TemplateAliasTypeDef],
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateTemplateAliasResponseTypeDef = TypedDict(
    "UpdateTemplateAliasResponseTypeDef",
    {
        "TemplateAlias": TemplateAliasTypeDef,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateThemeAliasResponseTypeDef = TypedDict(
    "CreateThemeAliasResponseTypeDef",
    {
        "ThemeAlias": ThemeAliasTypeDef,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeThemeAliasResponseTypeDef = TypedDict(
    "DescribeThemeAliasResponseTypeDef",
    {
        "ThemeAlias": ThemeAliasTypeDef,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListThemeAliasesResponseTypeDef = TypedDict(
    "ListThemeAliasesResponseTypeDef",
    {
        "ThemeAliasList": List[ThemeAliasTypeDef],
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
UpdateThemeAliasResponseTypeDef = TypedDict(
    "UpdateThemeAliasResponseTypeDef",
    {
        "ThemeAlias": ThemeAliasTypeDef,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CustomActionNavigationOperationTypeDef = TypedDict(
    "CustomActionNavigationOperationTypeDef",
    {
        "LocalNavigationConfiguration": NotRequired[LocalNavigationConfigurationTypeDef],
    },
)
CustomFilterListConfigurationUnionTypeDef = Union[
    CustomFilterListConfigurationTypeDef, CustomFilterListConfigurationOutputTypeDef
]
CustomValuesConfigurationOutputTypeDef = TypedDict(
    "CustomValuesConfigurationOutputTypeDef",
    {
        "CustomValues": CustomParameterValuesOutputTypeDef,
        "IncludeNullValue": NotRequired[bool],
    },
)
CustomSqlOutputTypeDef = TypedDict(
    "CustomSqlOutputTypeDef",
    {
        "DataSourceArn": str,
        "Name": str,
        "SqlQuery": str,
        "Columns": NotRequired[List[InputColumnTypeDef]],
    },
)
CustomSqlTypeDef = TypedDict(
    "CustomSqlTypeDef",
    {
        "DataSourceArn": str,
        "Name": str,
        "SqlQuery": str,
        "Columns": NotRequired[Sequence[InputColumnTypeDef]],
    },
)
RelationalTableOutputTypeDef = TypedDict(
    "RelationalTableOutputTypeDef",
    {
        "DataSourceArn": str,
        "Name": str,
        "InputColumns": List[InputColumnTypeDef],
        "Catalog": NotRequired[str],
        "Schema": NotRequired[str],
    },
)
RelationalTableTypeDef = TypedDict(
    "RelationalTableTypeDef",
    {
        "DataSourceArn": str,
        "Name": str,
        "InputColumns": Sequence[InputColumnTypeDef],
        "Catalog": NotRequired[str],
        "Schema": NotRequired[str],
    },
)
VisualInteractionOptionsTypeDef = TypedDict(
    "VisualInteractionOptionsTypeDef",
    {
        "VisualMenuOption": NotRequired[VisualMenuOptionTypeDef],
        "ContextMenuOption": NotRequired[ContextMenuOptionTypeDef],
    },
)
SearchDashboardsRequestRequestTypeDef = TypedDict(
    "SearchDashboardsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Filters": Sequence[DashboardSearchFilterTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListDashboardsResponseTypeDef = TypedDict(
    "ListDashboardsResponseTypeDef",
    {
        "DashboardSummaryList": List[DashboardSummaryTypeDef],
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
SearchDashboardsResponseTypeDef = TypedDict(
    "SearchDashboardsResponseTypeDef",
    {
        "DashboardSummaryList": List[DashboardSummaryTypeDef],
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListDashboardVersionsResponseTypeDef = TypedDict(
    "ListDashboardVersionsResponseTypeDef",
    {
        "DashboardVersionSummaryList": List[DashboardVersionSummaryTypeDef],
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DashboardVisualPublishOptionsTypeDef = TypedDict(
    "DashboardVisualPublishOptionsTypeDef",
    {
        "ExportHiddenFieldsOption": NotRequired[ExportHiddenFieldsOptionTypeDef],
    },
)
TableInlineVisualizationTypeDef = TypedDict(
    "TableInlineVisualizationTypeDef",
    {
        "DataBars": NotRequired[DataBarsOptionsTypeDef],
    },
)
DataColorPaletteUnionTypeDef = Union[DataColorPaletteTypeDef, DataColorPaletteOutputTypeDef]
DataLabelTypeTypeDef = TypedDict(
    "DataLabelTypeTypeDef",
    {
        "FieldLabelType": NotRequired[FieldLabelTypeTypeDef],
        "DataPathLabelType": NotRequired[DataPathLabelTypeTypeDef],
        "RangeEndsLabelType": NotRequired[RangeEndsLabelTypeTypeDef],
        "MinimumLabelType": NotRequired[MinimumLabelTypeTypeDef],
        "MaximumLabelType": NotRequired[MaximumLabelTypeTypeDef],
    },
)
DataPathValueTypeDef = TypedDict(
    "DataPathValueTypeDef",
    {
        "FieldId": NotRequired[str],
        "FieldValue": NotRequired[str],
        "DataPathType": NotRequired[DataPathTypeTypeDef],
    },
)
SearchDataSetsRequestRequestTypeDef = TypedDict(
    "SearchDataSetsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Filters": Sequence[DataSetSearchFilterTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
SearchDataSourcesRequestRequestTypeDef = TypedDict(
    "SearchDataSourcesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Filters": Sequence[DataSourceSearchFilterTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
SearchDataSourcesResponseTypeDef = TypedDict(
    "SearchDataSourcesResponseTypeDef",
    {
        "DataSourceSummaries": List[DataSourceSummaryTypeDef],
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DateTimeDatasetParameterOutputTypeDef = TypedDict(
    "DateTimeDatasetParameterOutputTypeDef",
    {
        "Id": str,
        "Name": str,
        "ValueType": DatasetParameterValueTypeType,
        "TimeGranularity": NotRequired[TimeGranularityType],
        "DefaultValues": NotRequired[DateTimeDatasetParameterDefaultValuesOutputTypeDef],
    },
)
TimeRangeFilterValueOutputTypeDef = TypedDict(
    "TimeRangeFilterValueOutputTypeDef",
    {
        "StaticValue": NotRequired[datetime],
        "RollingDate": NotRequired[RollingDateConfigurationTypeDef],
        "Parameter": NotRequired[str],
    },
)
TimeRangeFilterValueTypeDef = TypedDict(
    "TimeRangeFilterValueTypeDef",
    {
        "StaticValue": NotRequired[TimestampTypeDef],
        "RollingDate": NotRequired[RollingDateConfigurationTypeDef],
        "Parameter": NotRequired[str],
    },
)
DecimalDatasetParameterOutputTypeDef = TypedDict(
    "DecimalDatasetParameterOutputTypeDef",
    {
        "Id": str,
        "Name": str,
        "ValueType": DatasetParameterValueTypeType,
        "DefaultValues": NotRequired[DecimalDatasetParameterDefaultValuesOutputTypeDef],
    },
)
DecimalDatasetParameterDefaultValuesUnionTypeDef = Union[
    DecimalDatasetParameterDefaultValuesTypeDef, DecimalDatasetParameterDefaultValuesOutputTypeDef
]
DecimalParameterUnionTypeDef = Union[DecimalParameterTypeDef, DecimalParameterOutputTypeDef]
DescribeAnalysisPermissionsResponseTypeDef = TypedDict(
    "DescribeAnalysisPermissionsResponseTypeDef",
    {
        "AnalysisId": str,
        "AnalysisArn": str,
        "Permissions": List[ResourcePermissionOutputTypeDef],
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDataSetPermissionsResponseTypeDef = TypedDict(
    "DescribeDataSetPermissionsResponseTypeDef",
    {
        "DataSetArn": str,
        "DataSetId": str,
        "Permissions": List[ResourcePermissionOutputTypeDef],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDataSourcePermissionsResponseTypeDef = TypedDict(
    "DescribeDataSourcePermissionsResponseTypeDef",
    {
        "DataSourceArn": str,
        "DataSourceId": str,
        "Permissions": List[ResourcePermissionOutputTypeDef],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeFolderPermissionsResponseTypeDef = TypedDict(
    "DescribeFolderPermissionsResponseTypeDef",
    {
        "Status": int,
        "FolderId": str,
        "Arn": str,
        "Permissions": List[ResourcePermissionOutputTypeDef],
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeFolderResolvedPermissionsResponseTypeDef = TypedDict(
    "DescribeFolderResolvedPermissionsResponseTypeDef",
    {
        "Status": int,
        "FolderId": str,
        "Arn": str,
        "Permissions": List[ResourcePermissionOutputTypeDef],
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeTemplatePermissionsResponseTypeDef = TypedDict(
    "DescribeTemplatePermissionsResponseTypeDef",
    {
        "TemplateId": str,
        "TemplateArn": str,
        "Permissions": List[ResourcePermissionOutputTypeDef],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeThemePermissionsResponseTypeDef = TypedDict(
    "DescribeThemePermissionsResponseTypeDef",
    {
        "ThemeId": str,
        "ThemeArn": str,
        "Permissions": List[ResourcePermissionOutputTypeDef],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTopicPermissionsResponseTypeDef = TypedDict(
    "DescribeTopicPermissionsResponseTypeDef",
    {
        "TopicId": str,
        "TopicArn": str,
        "Permissions": List[ResourcePermissionOutputTypeDef],
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LinkSharingConfigurationOutputTypeDef = TypedDict(
    "LinkSharingConfigurationOutputTypeDef",
    {
        "Permissions": NotRequired[List[ResourcePermissionOutputTypeDef]],
    },
)
ResourcePermissionUnionTypeDef = Union[ResourcePermissionTypeDef, ResourcePermissionOutputTypeDef]
UpdateAnalysisPermissionsResponseTypeDef = TypedDict(
    "UpdateAnalysisPermissionsResponseTypeDef",
    {
        "AnalysisArn": str,
        "AnalysisId": str,
        "Permissions": List[ResourcePermissionOutputTypeDef],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFolderPermissionsResponseTypeDef = TypedDict(
    "UpdateFolderPermissionsResponseTypeDef",
    {
        "Status": int,
        "Arn": str,
        "FolderId": str,
        "Permissions": List[ResourcePermissionOutputTypeDef],
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTemplatePermissionsResponseTypeDef = TypedDict(
    "UpdateTemplatePermissionsResponseTypeDef",
    {
        "TemplateId": str,
        "TemplateArn": str,
        "Permissions": List[ResourcePermissionOutputTypeDef],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateThemePermissionsResponseTypeDef = TypedDict(
    "UpdateThemePermissionsResponseTypeDef",
    {
        "ThemeId": str,
        "ThemeArn": str,
        "Permissions": List[ResourcePermissionOutputTypeDef],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTopicPermissionsResponseTypeDef = TypedDict(
    "UpdateTopicPermissionsResponseTypeDef",
    {
        "TopicId": str,
        "TopicArn": str,
        "Permissions": List[ResourcePermissionOutputTypeDef],
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeFolderPermissionsRequestDescribeFolderPermissionsPaginateTypeDef = TypedDict(
    "DescribeFolderPermissionsRequestDescribeFolderPermissionsPaginateTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
        "Namespace": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeFolderResolvedPermissionsRequestDescribeFolderResolvedPermissionsPaginateTypeDef = (
    TypedDict(
        "DescribeFolderResolvedPermissionsRequestDescribeFolderResolvedPermissionsPaginateTypeDef",
        {
            "AwsAccountId": str,
            "FolderId": str,
            "Namespace": NotRequired[str],
            "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
        },
    )
)
ListAnalysesRequestListAnalysesPaginateTypeDef = TypedDict(
    "ListAnalysesRequestListAnalysesPaginateTypeDef",
    {
        "AwsAccountId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAssetBundleExportJobsRequestListAssetBundleExportJobsPaginateTypeDef = TypedDict(
    "ListAssetBundleExportJobsRequestListAssetBundleExportJobsPaginateTypeDef",
    {
        "AwsAccountId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAssetBundleImportJobsRequestListAssetBundleImportJobsPaginateTypeDef = TypedDict(
    "ListAssetBundleImportJobsRequestListAssetBundleImportJobsPaginateTypeDef",
    {
        "AwsAccountId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDashboardVersionsRequestListDashboardVersionsPaginateTypeDef = TypedDict(
    "ListDashboardVersionsRequestListDashboardVersionsPaginateTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDashboardsRequestListDashboardsPaginateTypeDef = TypedDict(
    "ListDashboardsRequestListDashboardsPaginateTypeDef",
    {
        "AwsAccountId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDataSetsRequestListDataSetsPaginateTypeDef = TypedDict(
    "ListDataSetsRequestListDataSetsPaginateTypeDef",
    {
        "AwsAccountId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDataSourcesRequestListDataSourcesPaginateTypeDef = TypedDict(
    "ListDataSourcesRequestListDataSourcesPaginateTypeDef",
    {
        "AwsAccountId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFolderMembersRequestListFolderMembersPaginateTypeDef = TypedDict(
    "ListFolderMembersRequestListFolderMembersPaginateTypeDef",
    {
        "AwsAccountId": str,
        "FolderId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFoldersForResourceRequestListFoldersForResourcePaginateTypeDef = TypedDict(
    "ListFoldersForResourceRequestListFoldersForResourcePaginateTypeDef",
    {
        "AwsAccountId": str,
        "ResourceArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFoldersRequestListFoldersPaginateTypeDef = TypedDict(
    "ListFoldersRequestListFoldersPaginateTypeDef",
    {
        "AwsAccountId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGroupMembershipsRequestListGroupMembershipsPaginateTypeDef = TypedDict(
    "ListGroupMembershipsRequestListGroupMembershipsPaginateTypeDef",
    {
        "GroupName": str,
        "AwsAccountId": str,
        "Namespace": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGroupsRequestListGroupsPaginateTypeDef = TypedDict(
    "ListGroupsRequestListGroupsPaginateTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListIAMPolicyAssignmentsForUserRequestListIAMPolicyAssignmentsForUserPaginateTypeDef = TypedDict(
    "ListIAMPolicyAssignmentsForUserRequestListIAMPolicyAssignmentsForUserPaginateTypeDef",
    {
        "AwsAccountId": str,
        "UserName": str,
        "Namespace": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListIAMPolicyAssignmentsRequestListIAMPolicyAssignmentsPaginateTypeDef = TypedDict(
    "ListIAMPolicyAssignmentsRequestListIAMPolicyAssignmentsPaginateTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
        "AssignmentStatus": NotRequired[AssignmentStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListIngestionsRequestListIngestionsPaginateTypeDef = TypedDict(
    "ListIngestionsRequestListIngestionsPaginateTypeDef",
    {
        "DataSetId": str,
        "AwsAccountId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListNamespacesRequestListNamespacesPaginateTypeDef = TypedDict(
    "ListNamespacesRequestListNamespacesPaginateTypeDef",
    {
        "AwsAccountId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRoleMembershipsRequestListRoleMembershipsPaginateTypeDef = TypedDict(
    "ListRoleMembershipsRequestListRoleMembershipsPaginateTypeDef",
    {
        "Role": RoleType,
        "AwsAccountId": str,
        "Namespace": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTemplateAliasesRequestListTemplateAliasesPaginateTypeDef = TypedDict(
    "ListTemplateAliasesRequestListTemplateAliasesPaginateTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTemplateVersionsRequestListTemplateVersionsPaginateTypeDef = TypedDict(
    "ListTemplateVersionsRequestListTemplateVersionsPaginateTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTemplatesRequestListTemplatesPaginateTypeDef = TypedDict(
    "ListTemplatesRequestListTemplatesPaginateTypeDef",
    {
        "AwsAccountId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListThemeVersionsRequestListThemeVersionsPaginateTypeDef = TypedDict(
    "ListThemeVersionsRequestListThemeVersionsPaginateTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListThemesRequestListThemesPaginateTypeDef = TypedDict(
    "ListThemesRequestListThemesPaginateTypeDef",
    {
        "AwsAccountId": str,
        "Type": NotRequired[ThemeTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListUserGroupsRequestListUserGroupsPaginateTypeDef = TypedDict(
    "ListUserGroupsRequestListUserGroupsPaginateTypeDef",
    {
        "UserName": str,
        "AwsAccountId": str,
        "Namespace": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListUsersRequestListUsersPaginateTypeDef = TypedDict(
    "ListUsersRequestListUsersPaginateTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchAnalysesRequestSearchAnalysesPaginateTypeDef = TypedDict(
    "SearchAnalysesRequestSearchAnalysesPaginateTypeDef",
    {
        "AwsAccountId": str,
        "Filters": Sequence[AnalysisSearchFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchDashboardsRequestSearchDashboardsPaginateTypeDef = TypedDict(
    "SearchDashboardsRequestSearchDashboardsPaginateTypeDef",
    {
        "AwsAccountId": str,
        "Filters": Sequence[DashboardSearchFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchDataSetsRequestSearchDataSetsPaginateTypeDef = TypedDict(
    "SearchDataSetsRequestSearchDataSetsPaginateTypeDef",
    {
        "AwsAccountId": str,
        "Filters": Sequence[DataSetSearchFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchDataSourcesRequestSearchDataSourcesPaginateTypeDef = TypedDict(
    "SearchDataSourcesRequestSearchDataSourcesPaginateTypeDef",
    {
        "AwsAccountId": str,
        "Filters": Sequence[DataSourceSearchFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeFolderResponseTypeDef = TypedDict(
    "DescribeFolderResponseTypeDef",
    {
        "Status": int,
        "Folder": FolderTypeDef,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeIAMPolicyAssignmentResponseTypeDef = TypedDict(
    "DescribeIAMPolicyAssignmentResponseTypeDef",
    {
        "IAMPolicyAssignment": IAMPolicyAssignmentTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeKeyRegistrationResponseTypeDef = TypedDict(
    "DescribeKeyRegistrationResponseTypeDef",
    {
        "AwsAccountId": str,
        "KeyRegistration": List[RegisteredCustomerManagedKeyTypeDef],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateKeyRegistrationRequestRequestTypeDef = TypedDict(
    "UpdateKeyRegistrationRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "KeyRegistration": Sequence[RegisteredCustomerManagedKeyTypeDef],
    },
)
DescribeTopicRefreshResponseTypeDef = TypedDict(
    "DescribeTopicRefreshResponseTypeDef",
    {
        "RefreshDetails": TopicRefreshDetailsTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTopicRefreshScheduleResponseTypeDef = TypedDict(
    "DescribeTopicRefreshScheduleResponseTypeDef",
    {
        "TopicId": str,
        "TopicArn": str,
        "DatasetArn": str,
        "RefreshSchedule": TopicRefreshScheduleOutputTypeDef,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TopicRefreshScheduleSummaryTypeDef = TypedDict(
    "TopicRefreshScheduleSummaryTypeDef",
    {
        "DatasetId": NotRequired[str],
        "DatasetArn": NotRequired[str],
        "DatasetName": NotRequired[str],
        "RefreshSchedule": NotRequired[TopicRefreshScheduleOutputTypeDef],
    },
)
DescribeUserResponseTypeDef = TypedDict(
    "DescribeUserResponseTypeDef",
    {
        "User": UserTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "UserList": List[UserTypeDef],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
RegisterUserResponseTypeDef = TypedDict(
    "RegisterUserResponseTypeDef",
    {
        "User": UserTypeDef,
        "UserInvitationUrl": str,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateUserResponseTypeDef = TypedDict(
    "UpdateUserResponseTypeDef",
    {
        "User": UserTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisplayFormatOptionsTypeDef = TypedDict(
    "DisplayFormatOptionsTypeDef",
    {
        "UseBlankCellFormat": NotRequired[bool],
        "BlankCellFormat": NotRequired[str],
        "DateFormat": NotRequired[str],
        "DecimalSeparator": NotRequired[TopicNumericSeparatorSymbolType],
        "GroupingSeparator": NotRequired[str],
        "UseGrouping": NotRequired[bool],
        "FractionDigits": NotRequired[int],
        "Prefix": NotRequired[str],
        "Suffix": NotRequired[str],
        "UnitScaler": NotRequired[NumberScaleType],
        "NegativeFormat": NotRequired[NegativeFormatTypeDef],
        "CurrencySymbol": NotRequired[str],
    },
)
DonutOptionsTypeDef = TypedDict(
    "DonutOptionsTypeDef",
    {
        "ArcOptions": NotRequired[ArcOptionsTypeDef],
        "DonutCenterOptions": NotRequired[DonutCenterOptionsTypeDef],
    },
)
FieldFolderUnionTypeDef = Union[FieldFolderTypeDef, FieldFolderOutputTypeDef]
FilterAggMetricsTypeDef = TypedDict(
    "FilterAggMetricsTypeDef",
    {
        "MetricOperand": NotRequired[IdentifierTypeDef],
        "Function": NotRequired[AggTypeType],
        "SortDirection": NotRequired[TopicSortDirectionType],
    },
)
TopicSortClauseTypeDef = TypedDict(
    "TopicSortClauseTypeDef",
    {
        "Operand": NotRequired[IdentifierTypeDef],
        "SortDirection": NotRequired[TopicSortDirectionType],
    },
)
FilterListConfigurationUnionTypeDef = Union[
    FilterListConfigurationTypeDef, FilterListConfigurationOutputTypeDef
]
FilterOperationTargetVisualsConfigurationOutputTypeDef = TypedDict(
    "FilterOperationTargetVisualsConfigurationOutputTypeDef",
    {
        "SameSheetTargetVisualConfiguration": NotRequired[
            SameSheetTargetVisualConfigurationOutputTypeDef
        ],
    },
)
FilterSelectableValuesUnionTypeDef = Union[
    FilterSelectableValuesTypeDef, FilterSelectableValuesOutputTypeDef
]
SearchFoldersRequestRequestTypeDef = TypedDict(
    "SearchFoldersRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Filters": Sequence[FolderSearchFilterTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
SearchFoldersRequestSearchFoldersPaginateTypeDef = TypedDict(
    "SearchFoldersRequestSearchFoldersPaginateTypeDef",
    {
        "AwsAccountId": str,
        "Filters": Sequence[FolderSearchFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFoldersResponseTypeDef = TypedDict(
    "ListFoldersResponseTypeDef",
    {
        "Status": int,
        "FolderSummaryList": List[FolderSummaryTypeDef],
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
SearchFoldersResponseTypeDef = TypedDict(
    "SearchFoldersResponseTypeDef",
    {
        "Status": int,
        "FolderSummaryList": List[FolderSummaryTypeDef],
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
FontConfigurationTypeDef = TypedDict(
    "FontConfigurationTypeDef",
    {
        "FontSize": NotRequired[FontSizeTypeDef],
        "FontDecoration": NotRequired[FontDecorationType],
        "FontColor": NotRequired[str],
        "FontWeight": NotRequired[FontWeightTypeDef],
        "FontStyle": NotRequired[FontStyleType],
    },
)
TypographyOutputTypeDef = TypedDict(
    "TypographyOutputTypeDef",
    {
        "FontFamilies": NotRequired[List[FontTypeDef]],
    },
)
TypographyTypeDef = TypedDict(
    "TypographyTypeDef",
    {
        "FontFamilies": NotRequired[Sequence[FontTypeDef]],
    },
)
ForecastScenarioOutputTypeDef = TypedDict(
    "ForecastScenarioOutputTypeDef",
    {
        "WhatIfPointScenario": NotRequired[WhatIfPointScenarioOutputTypeDef],
        "WhatIfRangeScenario": NotRequired[WhatIfRangeScenarioOutputTypeDef],
    },
)
FreeFormLayoutCanvasSizeOptionsTypeDef = TypedDict(
    "FreeFormLayoutCanvasSizeOptionsTypeDef",
    {
        "ScreenCanvasSizeOptions": NotRequired[FreeFormLayoutScreenCanvasSizeOptionsTypeDef],
    },
)
SnapshotAnonymousUserTypeDef = TypedDict(
    "SnapshotAnonymousUserTypeDef",
    {
        "RowLevelPermissionTags": NotRequired[Sequence[SessionTagTypeDef]],
    },
)
GeoSpatialColumnGroupUnionTypeDef = Union[
    GeoSpatialColumnGroupTypeDef, GeoSpatialColumnGroupOutputTypeDef
]
GeospatialWindowOptionsTypeDef = TypedDict(
    "GeospatialWindowOptionsTypeDef",
    {
        "Bounds": NotRequired[GeospatialCoordinateBoundsTypeDef],
        "MapZoomMode": NotRequired[MapZoomModeType],
    },
)
GeospatialHeatmapColorScaleOutputTypeDef = TypedDict(
    "GeospatialHeatmapColorScaleOutputTypeDef",
    {
        "Colors": NotRequired[List[GeospatialHeatmapDataColorTypeDef]],
    },
)
GeospatialHeatmapColorScaleTypeDef = TypedDict(
    "GeospatialHeatmapColorScaleTypeDef",
    {
        "Colors": NotRequired[Sequence[GeospatialHeatmapDataColorTypeDef]],
    },
)
TableSideBorderOptionsTypeDef = TypedDict(
    "TableSideBorderOptionsTypeDef",
    {
        "InnerVertical": NotRequired[TableBorderOptionsTypeDef],
        "InnerHorizontal": NotRequired[TableBorderOptionsTypeDef],
        "Left": NotRequired[TableBorderOptionsTypeDef],
        "Right": NotRequired[TableBorderOptionsTypeDef],
        "Top": NotRequired[TableBorderOptionsTypeDef],
        "Bottom": NotRequired[TableBorderOptionsTypeDef],
    },
)
GradientColorOutputTypeDef = TypedDict(
    "GradientColorOutputTypeDef",
    {
        "Stops": NotRequired[List[GradientStopTypeDef]],
    },
)
GradientColorTypeDef = TypedDict(
    "GradientColorTypeDef",
    {
        "Stops": NotRequired[Sequence[GradientStopTypeDef]],
    },
)
GridLayoutCanvasSizeOptionsTypeDef = TypedDict(
    "GridLayoutCanvasSizeOptionsTypeDef",
    {
        "ScreenCanvasSizeOptions": NotRequired[GridLayoutScreenCanvasSizeOptionsTypeDef],
    },
)
SearchGroupsRequestRequestTypeDef = TypedDict(
    "SearchGroupsRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
        "Filters": Sequence[GroupSearchFilterTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
SearchGroupsRequestSearchGroupsPaginateTypeDef = TypedDict(
    "SearchGroupsRequestSearchGroupsPaginateTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
        "Filters": Sequence[GroupSearchFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListIAMPolicyAssignmentsResponseTypeDef = TypedDict(
    "ListIAMPolicyAssignmentsResponseTypeDef",
    {
        "IAMPolicyAssignments": List[IAMPolicyAssignmentSummaryTypeDef],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
IncrementalRefreshTypeDef = TypedDict(
    "IncrementalRefreshTypeDef",
    {
        "LookbackWindow": LookbackWindowTypeDef,
    },
)
IngestionTypeDef = TypedDict(
    "IngestionTypeDef",
    {
        "Arn": str,
        "IngestionStatus": IngestionStatusType,
        "CreatedTime": datetime,
        "IngestionId": NotRequired[str],
        "ErrorInfo": NotRequired[ErrorInfoTypeDef],
        "RowInfo": NotRequired[RowInfoTypeDef],
        "QueueInfo": NotRequired[QueueInfoTypeDef],
        "IngestionTimeInSeconds": NotRequired[int],
        "IngestionSizeInBytes": NotRequired[int],
        "RequestSource": NotRequired[IngestionRequestSourceType],
        "RequestType": NotRequired[IngestionRequestTypeType],
    },
)
IntegerDatasetParameterOutputTypeDef = TypedDict(
    "IntegerDatasetParameterOutputTypeDef",
    {
        "Id": str,
        "Name": str,
        "ValueType": DatasetParameterValueTypeType,
        "DefaultValues": NotRequired[IntegerDatasetParameterDefaultValuesOutputTypeDef],
    },
)
IntegerDatasetParameterDefaultValuesUnionTypeDef = Union[
    IntegerDatasetParameterDefaultValuesTypeDef, IntegerDatasetParameterDefaultValuesOutputTypeDef
]
IntegerParameterUnionTypeDef = Union[IntegerParameterTypeDef, IntegerParameterOutputTypeDef]
JoinInstructionTypeDef = TypedDict(
    "JoinInstructionTypeDef",
    {
        "LeftOperand": str,
        "RightOperand": str,
        "Type": JoinTypeType,
        "OnClause": str,
        "LeftJoinKeyProperties": NotRequired[JoinKeyPropertiesTypeDef],
        "RightJoinKeyProperties": NotRequired[JoinKeyPropertiesTypeDef],
    },
)
KPIVisualLayoutOptionsTypeDef = TypedDict(
    "KPIVisualLayoutOptionsTypeDef",
    {
        "StandardLayout": NotRequired[KPIVisualStandardLayoutTypeDef],
    },
)
LineChartDefaultSeriesSettingsTypeDef = TypedDict(
    "LineChartDefaultSeriesSettingsTypeDef",
    {
        "AxisBinding": NotRequired[AxisBindingType],
        "LineStyleSettings": NotRequired[LineChartLineStyleSettingsTypeDef],
        "MarkerStyleSettings": NotRequired[LineChartMarkerStyleSettingsTypeDef],
    },
)
LineChartSeriesSettingsTypeDef = TypedDict(
    "LineChartSeriesSettingsTypeDef",
    {
        "LineStyleSettings": NotRequired[LineChartLineStyleSettingsTypeDef],
        "MarkerStyleSettings": NotRequired[LineChartMarkerStyleSettingsTypeDef],
    },
)
ListFolderMembersResponseTypeDef = TypedDict(
    "ListFolderMembersResponseTypeDef",
    {
        "Status": int,
        "FolderMemberList": List[MemberIdArnPairTypeDef],
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTemplateVersionsResponseTypeDef = TypedDict(
    "ListTemplateVersionsResponseTypeDef",
    {
        "TemplateVersionSummaryList": List[TemplateVersionSummaryTypeDef],
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTemplatesResponseTypeDef = TypedDict(
    "ListTemplatesResponseTypeDef",
    {
        "TemplateSummaryList": List[TemplateSummaryTypeDef],
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListThemeVersionsResponseTypeDef = TypedDict(
    "ListThemeVersionsResponseTypeDef",
    {
        "ThemeVersionSummaryList": List[ThemeVersionSummaryTypeDef],
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListThemesResponseTypeDef = TypedDict(
    "ListThemesResponseTypeDef",
    {
        "ThemeSummaryList": List[ThemeSummaryTypeDef],
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTopicsResponseTypeDef = TypedDict(
    "ListTopicsResponseTypeDef",
    {
        "TopicsSummaries": List[TopicSummaryTypeDef],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
VisualSubtitleLabelOptionsTypeDef = TypedDict(
    "VisualSubtitleLabelOptionsTypeDef",
    {
        "Visibility": NotRequired[VisibilityType],
        "FormatText": NotRequired[LongFormatTextTypeDef],
    },
)
S3ParametersTypeDef = TypedDict(
    "S3ParametersTypeDef",
    {
        "ManifestFileLocation": ManifestFileLocationTypeDef,
        "RoleArn": NotRequired[str],
    },
)
TileLayoutStyleTypeDef = TypedDict(
    "TileLayoutStyleTypeDef",
    {
        "Gutter": NotRequired[GutterStyleTypeDef],
        "Margin": NotRequired[MarginStyleTypeDef],
    },
)
NamedEntityDefinitionOutputTypeDef = TypedDict(
    "NamedEntityDefinitionOutputTypeDef",
    {
        "FieldName": NotRequired[str],
        "PropertyName": NotRequired[str],
        "PropertyRole": NotRequired[PropertyRoleType],
        "PropertyUsage": NotRequired[PropertyUsageType],
        "Metric": NotRequired[NamedEntityDefinitionMetricOutputTypeDef],
    },
)
NamedEntityDefinitionMetricUnionTypeDef = Union[
    NamedEntityDefinitionMetricTypeDef, NamedEntityDefinitionMetricOutputTypeDef
]
NamespaceInfoV2TypeDef = TypedDict(
    "NamespaceInfoV2TypeDef",
    {
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "CapacityRegion": NotRequired[str],
        "CreationStatus": NotRequired[NamespaceStatusType],
        "IdentityStore": NotRequired[Literal["QUICKSIGHT"]],
        "NamespaceError": NotRequired[NamespaceErrorTypeDef],
    },
)
VPCConnectionSummaryTypeDef = TypedDict(
    "VPCConnectionSummaryTypeDef",
    {
        "VPCConnectionId": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "VPCId": NotRequired[str],
        "SecurityGroupIds": NotRequired[List[str]],
        "DnsResolvers": NotRequired[List[str]],
        "Status": NotRequired[VPCConnectionResourceStatusType],
        "AvailabilityStatus": NotRequired[VPCConnectionAvailabilityStatusType],
        "NetworkInterfaces": NotRequired[List[NetworkInterfaceTypeDef]],
        "RoleArn": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
    },
)
VPCConnectionTypeDef = TypedDict(
    "VPCConnectionTypeDef",
    {
        "VPCConnectionId": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "VPCId": NotRequired[str],
        "SecurityGroupIds": NotRequired[List[str]],
        "DnsResolvers": NotRequired[List[str]],
        "Status": NotRequired[VPCConnectionResourceStatusType],
        "AvailabilityStatus": NotRequired[VPCConnectionAvailabilityStatusType],
        "NetworkInterfaces": NotRequired[List[NetworkInterfaceTypeDef]],
        "RoleArn": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
    },
)
OverrideDatasetParameterOperationOutputTypeDef = TypedDict(
    "OverrideDatasetParameterOperationOutputTypeDef",
    {
        "ParameterName": str,
        "NewParameterName": NotRequired[str],
        "NewDefaultValues": NotRequired[NewDefaultValuesOutputTypeDef],
    },
)
NumericSeparatorConfigurationTypeDef = TypedDict(
    "NumericSeparatorConfigurationTypeDef",
    {
        "DecimalSeparator": NotRequired[NumericSeparatorSymbolType],
        "ThousandsSeparator": NotRequired[ThousandSeparatorOptionsTypeDef],
    },
)
NumericalAggregationFunctionTypeDef = TypedDict(
    "NumericalAggregationFunctionTypeDef",
    {
        "SimpleNumericalAggregation": NotRequired[SimpleNumericalAggregationFunctionType],
        "PercentileAggregation": NotRequired[PercentileAggregationTypeDef],
    },
)
ParametersOutputTypeDef = TypedDict(
    "ParametersOutputTypeDef",
    {
        "StringParameters": NotRequired[List[StringParameterOutputTypeDef]],
        "IntegerParameters": NotRequired[List[IntegerParameterOutputTypeDef]],
        "DecimalParameters": NotRequired[List[DecimalParameterOutputTypeDef]],
        "DateTimeParameters": NotRequired[List[DateTimeParameterOutputTypeDef]],
    },
)
VisibleRangeOptionsTypeDef = TypedDict(
    "VisibleRangeOptionsTypeDef",
    {
        "PercentRange": NotRequired[PercentVisibleRangeTypeDef],
    },
)
ProjectOperationUnionTypeDef = Union[ProjectOperationTypeDef, ProjectOperationOutputTypeDef]
RadarChartSeriesSettingsTypeDef = TypedDict(
    "RadarChartSeriesSettingsTypeDef",
    {
        "AreaStyleSettings": NotRequired[RadarChartAreaStyleSettingsTypeDef],
    },
)
TopicRangeFilterConstantTypeDef = TypedDict(
    "TopicRangeFilterConstantTypeDef",
    {
        "ConstantType": NotRequired[ConstantTypeType],
        "RangeConstant": NotRequired[RangeConstantTypeDef],
    },
)
RedshiftParametersOutputTypeDef = TypedDict(
    "RedshiftParametersOutputTypeDef",
    {
        "Database": str,
        "Host": NotRequired[str],
        "Port": NotRequired[int],
        "ClusterId": NotRequired[str],
        "IAMParameters": NotRequired[RedshiftIAMParametersOutputTypeDef],
        "IdentityCenterConfiguration": NotRequired[IdentityCenterConfigurationTypeDef],
    },
)
RedshiftIAMParametersUnionTypeDef = Union[
    RedshiftIAMParametersTypeDef, RedshiftIAMParametersOutputTypeDef
]
RefreshFrequencyTypeDef = TypedDict(
    "RefreshFrequencyTypeDef",
    {
        "Interval": RefreshIntervalType,
        "RefreshOnDay": NotRequired[ScheduleRefreshOnEntityTypeDef],
        "Timezone": NotRequired[str],
        "TimeOfTheDay": NotRequired[str],
    },
)
RegisteredUserConsoleFeatureConfigurationsTypeDef = TypedDict(
    "RegisteredUserConsoleFeatureConfigurationsTypeDef",
    {
        "StatePersistence": NotRequired[StatePersistenceConfigurationsTypeDef],
        "SharedView": NotRequired[SharedViewConfigurationsTypeDef],
    },
)
RegisteredUserDashboardFeatureConfigurationsTypeDef = TypedDict(
    "RegisteredUserDashboardFeatureConfigurationsTypeDef",
    {
        "StatePersistence": NotRequired[StatePersistenceConfigurationsTypeDef],
        "SharedView": NotRequired[SharedViewConfigurationsTypeDef],
        "Bookmarks": NotRequired[BookmarksConfigurationsTypeDef],
    },
)
RowAlternateColorOptionsUnionTypeDef = Union[
    RowAlternateColorOptionsTypeDef, RowAlternateColorOptionsOutputTypeDef
]
RowLevelPermissionTagConfigurationOutputTypeDef = TypedDict(
    "RowLevelPermissionTagConfigurationOutputTypeDef",
    {
        "TagRules": List[RowLevelPermissionTagRuleTypeDef],
        "Status": NotRequired[StatusType],
        "TagRuleConfigurations": NotRequired[List[List[str]]],
    },
)
RowLevelPermissionTagConfigurationTypeDef = TypedDict(
    "RowLevelPermissionTagConfigurationTypeDef",
    {
        "TagRules": Sequence[RowLevelPermissionTagRuleTypeDef],
        "Status": NotRequired[StatusType],
        "TagRuleConfigurations": NotRequired[Sequence[Sequence[str]]],
    },
)
SnapshotS3DestinationConfigurationTypeDef = TypedDict(
    "SnapshotS3DestinationConfigurationTypeDef",
    {
        "BucketConfiguration": S3BucketConfigurationTypeDef,
    },
)
S3SourceOutputTypeDef = TypedDict(
    "S3SourceOutputTypeDef",
    {
        "DataSourceArn": str,
        "InputColumns": List[InputColumnTypeDef],
        "UploadSettings": NotRequired[UploadSettingsTypeDef],
    },
)
S3SourceTypeDef = TypedDict(
    "S3SourceTypeDef",
    {
        "DataSourceArn": str,
        "InputColumns": Sequence[InputColumnTypeDef],
        "UploadSettings": NotRequired[UploadSettingsTypeDef],
    },
)
SameSheetTargetVisualConfigurationUnionTypeDef = Union[
    SameSheetTargetVisualConfigurationTypeDef, SameSheetTargetVisualConfigurationOutputTypeDef
]
SectionBasedLayoutPaperCanvasSizeOptionsTypeDef = TypedDict(
    "SectionBasedLayoutPaperCanvasSizeOptionsTypeDef",
    {
        "PaperSize": NotRequired[PaperSizeType],
        "PaperOrientation": NotRequired[PaperOrientationType],
        "PaperMargin": NotRequired[SpacingTypeDef],
    },
)
SectionStyleTypeDef = TypedDict(
    "SectionStyleTypeDef",
    {
        "Height": NotRequired[str],
        "Padding": NotRequired[SpacingTypeDef],
    },
)
SelectedSheetsFilterScopeConfigurationOutputTypeDef = TypedDict(
    "SelectedSheetsFilterScopeConfigurationOutputTypeDef",
    {
        "SheetVisualScopingConfigurations": NotRequired[
            List[SheetVisualScopingConfigurationOutputTypeDef]
        ],
    },
)
SemanticEntityTypeUnionTypeDef = Union[SemanticEntityTypeTypeDef, SemanticEntityTypeOutputTypeDef]
SemanticTypeUnionTypeDef = Union[SemanticTypeTypeDef, SemanticTypeOutputTypeDef]
SheetElementRenderingRuleTypeDef = TypedDict(
    "SheetElementRenderingRuleTypeDef",
    {
        "Expression": str,
        "ConfigurationOverrides": SheetElementConfigurationOverridesTypeDef,
    },
)
SheetVisualScopingConfigurationUnionTypeDef = Union[
    SheetVisualScopingConfigurationTypeDef, SheetVisualScopingConfigurationOutputTypeDef
]
VisualTitleLabelOptionsTypeDef = TypedDict(
    "VisualTitleLabelOptionsTypeDef",
    {
        "Visibility": NotRequired[VisibilityType],
        "FormatText": NotRequired[ShortFormatTextTypeDef],
    },
)
SingleAxisOptionsTypeDef = TypedDict(
    "SingleAxisOptionsTypeDef",
    {
        "YAxisOptions": NotRequired[YAxisOptionsTypeDef],
    },
)
TopicTemplateOutputTypeDef = TypedDict(
    "TopicTemplateOutputTypeDef",
    {
        "TemplateType": NotRequired[str],
        "Slots": NotRequired[List[SlotTypeDef]],
    },
)
TopicTemplateTypeDef = TypedDict(
    "TopicTemplateTypeDef",
    {
        "TemplateType": NotRequired[str],
        "Slots": NotRequired[Sequence[SlotTypeDef]],
    },
)
SnapshotUserConfigurationRedactedTypeDef = TypedDict(
    "SnapshotUserConfigurationRedactedTypeDef",
    {
        "AnonymousUsers": NotRequired[List[SnapshotAnonymousUserRedactedTypeDef]],
    },
)
SnapshotFileOutputTypeDef = TypedDict(
    "SnapshotFileOutputTypeDef",
    {
        "SheetSelections": List[SnapshotFileSheetSelectionOutputTypeDef],
        "FormatType": SnapshotFileFormatTypeType,
    },
)
SnapshotFileSheetSelectionUnionTypeDef = Union[
    SnapshotFileSheetSelectionTypeDef, SnapshotFileSheetSelectionOutputTypeDef
]
StringDatasetParameterOutputTypeDef = TypedDict(
    "StringDatasetParameterOutputTypeDef",
    {
        "Id": str,
        "Name": str,
        "ValueType": DatasetParameterValueTypeType,
        "DefaultValues": NotRequired[StringDatasetParameterDefaultValuesOutputTypeDef],
    },
)
StringDatasetParameterDefaultValuesUnionTypeDef = Union[
    StringDatasetParameterDefaultValuesTypeDef, StringDatasetParameterDefaultValuesOutputTypeDef
]
StringParameterUnionTypeDef = Union[StringParameterTypeDef, StringParameterOutputTypeDef]
UpdateKeyRegistrationResponseTypeDef = TypedDict(
    "UpdateKeyRegistrationResponseTypeDef",
    {
        "FailedKeyRegistration": List[FailedKeyRegistrationEntryTypeDef],
        "SuccessfulKeyRegistration": List[SuccessfulKeyRegistrationEntryTypeDef],
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TableFieldImageConfigurationTypeDef = TypedDict(
    "TableFieldImageConfigurationTypeDef",
    {
        "SizingOptions": NotRequired[TableCellImageSizingConfigurationTypeDef],
    },
)
TablePinnedFieldOptionsUnionTypeDef = Union[
    TablePinnedFieldOptionsTypeDef, TablePinnedFieldOptionsOutputTypeDef
]
TopicNumericEqualityFilterTypeDef = TypedDict(
    "TopicNumericEqualityFilterTypeDef",
    {
        "Constant": NotRequired[TopicSingularFilterConstantTypeDef],
        "Aggregation": NotRequired[NamedFilterAggTypeType],
    },
)
TopicRelativeDateFilterTypeDef = TypedDict(
    "TopicRelativeDateFilterTypeDef",
    {
        "TimeGranularity": NotRequired[TopicTimeGranularityType],
        "RelativeDateFilterFunction": NotRequired[TopicRelativeDateFilterFunctionType],
        "Constant": NotRequired[TopicSingularFilterConstantTypeDef],
    },
)
TotalAggregationOptionTypeDef = TypedDict(
    "TotalAggregationOptionTypeDef",
    {
        "FieldId": str,
        "TotalAggregationFunction": TotalAggregationFunctionTypeDef,
    },
)
UntagColumnOperationUnionTypeDef = Union[
    UntagColumnOperationTypeDef, UntagColumnOperationOutputTypeDef
]
WaterfallChartColorConfigurationTypeDef = TypedDict(
    "WaterfallChartColorConfigurationTypeDef",
    {
        "GroupColorConfiguration": NotRequired[WaterfallChartGroupColorConfigurationTypeDef],
    },
)
CascadingControlConfigurationOutputTypeDef = TypedDict(
    "CascadingControlConfigurationOutputTypeDef",
    {
        "SourceControls": NotRequired[List[CascadingControlSourceTypeDef]],
    },
)
CascadingControlConfigurationTypeDef = TypedDict(
    "CascadingControlConfigurationTypeDef",
    {
        "SourceControls": NotRequired[Sequence[CascadingControlSourceTypeDef]],
    },
)
CategoryDrillDownFilterUnionTypeDef = Union[
    CategoryDrillDownFilterTypeDef, CategoryDrillDownFilterOutputTypeDef
]
ContributionAnalysisDefaultUnionTypeDef = Union[
    ContributionAnalysisDefaultTypeDef, ContributionAnalysisDefaultOutputTypeDef
]
DateTimeDefaultValuesOutputTypeDef = TypedDict(
    "DateTimeDefaultValuesOutputTypeDef",
    {
        "DynamicValue": NotRequired[DynamicDefaultValueTypeDef],
        "StaticValues": NotRequired[List[datetime]],
        "RollingDate": NotRequired[RollingDateConfigurationTypeDef],
    },
)
DateTimeDefaultValuesTypeDef = TypedDict(
    "DateTimeDefaultValuesTypeDef",
    {
        "DynamicValue": NotRequired[DynamicDefaultValueTypeDef],
        "StaticValues": NotRequired[Sequence[TimestampTypeDef]],
        "RollingDate": NotRequired[RollingDateConfigurationTypeDef],
    },
)
DecimalDefaultValuesOutputTypeDef = TypedDict(
    "DecimalDefaultValuesOutputTypeDef",
    {
        "DynamicValue": NotRequired[DynamicDefaultValueTypeDef],
        "StaticValues": NotRequired[List[float]],
    },
)
DecimalDefaultValuesTypeDef = TypedDict(
    "DecimalDefaultValuesTypeDef",
    {
        "DynamicValue": NotRequired[DynamicDefaultValueTypeDef],
        "StaticValues": NotRequired[Sequence[float]],
    },
)
IntegerDefaultValuesOutputTypeDef = TypedDict(
    "IntegerDefaultValuesOutputTypeDef",
    {
        "DynamicValue": NotRequired[DynamicDefaultValueTypeDef],
        "StaticValues": NotRequired[List[int]],
    },
)
IntegerDefaultValuesTypeDef = TypedDict(
    "IntegerDefaultValuesTypeDef",
    {
        "DynamicValue": NotRequired[DynamicDefaultValueTypeDef],
        "StaticValues": NotRequired[Sequence[int]],
    },
)
StringDefaultValuesOutputTypeDef = TypedDict(
    "StringDefaultValuesOutputTypeDef",
    {
        "DynamicValue": NotRequired[DynamicDefaultValueTypeDef],
        "StaticValues": NotRequired[List[str]],
    },
)
StringDefaultValuesTypeDef = TypedDict(
    "StringDefaultValuesTypeDef",
    {
        "DynamicValue": NotRequired[DynamicDefaultValueTypeDef],
        "StaticValues": NotRequired[Sequence[str]],
    },
)
FilterOperationSelectedFieldsConfigurationUnionTypeDef = Union[
    FilterOperationSelectedFieldsConfigurationTypeDef,
    FilterOperationSelectedFieldsConfigurationOutputTypeDef,
]
ParameterSelectableValuesUnionTypeDef = Union[
    ParameterSelectableValuesTypeDef, ParameterSelectableValuesOutputTypeDef
]
DrillDownFilterOutputTypeDef = TypedDict(
    "DrillDownFilterOutputTypeDef",
    {
        "NumericEqualityFilter": NotRequired[NumericEqualityDrillDownFilterTypeDef],
        "CategoryFilter": NotRequired[CategoryDrillDownFilterOutputTypeDef],
        "TimeRangeFilter": NotRequired[TimeRangeDrillDownFilterOutputTypeDef],
    },
)
AnalysisTypeDef = TypedDict(
    "AnalysisTypeDef",
    {
        "AnalysisId": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired[ResourceStatusType],
        "Errors": NotRequired[List[AnalysisErrorTypeDef]],
        "DataSetArns": NotRequired[List[str]],
        "ThemeArn": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "Sheets": NotRequired[List[SheetTypeDef]],
    },
)
DashboardVersionTypeDef = TypedDict(
    "DashboardVersionTypeDef",
    {
        "CreatedTime": NotRequired[datetime],
        "Errors": NotRequired[List[DashboardErrorTypeDef]],
        "VersionNumber": NotRequired[int],
        "Status": NotRequired[ResourceStatusType],
        "Arn": NotRequired[str],
        "SourceEntityArn": NotRequired[str],
        "DataSetArns": NotRequired[List[str]],
        "Description": NotRequired[str],
        "ThemeArn": NotRequired[str],
        "Sheets": NotRequired[List[SheetTypeDef]],
    },
)
AnalysisSourceEntityTypeDef = TypedDict(
    "AnalysisSourceEntityTypeDef",
    {
        "SourceTemplate": NotRequired[AnalysisSourceTemplateTypeDef],
    },
)
DashboardSourceEntityTypeDef = TypedDict(
    "DashboardSourceEntityTypeDef",
    {
        "SourceTemplate": NotRequired[DashboardSourceTemplateTypeDef],
    },
)
TemplateSourceEntityTypeDef = TypedDict(
    "TemplateSourceEntityTypeDef",
    {
        "SourceAnalysis": NotRequired[TemplateSourceAnalysisTypeDef],
        "SourceTemplate": NotRequired[TemplateSourceTemplateTypeDef],
    },
)
AnonymousUserDashboardEmbeddingConfigurationTypeDef = TypedDict(
    "AnonymousUserDashboardEmbeddingConfigurationTypeDef",
    {
        "InitialDashboardId": str,
        "EnabledFeatures": NotRequired[Sequence[Literal["SHARED_VIEW"]]],
        "DisabledFeatures": NotRequired[Sequence[Literal["SHARED_VIEW"]]],
        "FeatureConfigurations": NotRequired[AnonymousUserDashboardFeatureConfigurationsTypeDef],
    },
)
DescribeAssetBundleExportJobResponseTypeDef = TypedDict(
    "DescribeAssetBundleExportJobResponseTypeDef",
    {
        "JobStatus": AssetBundleExportJobStatusType,
        "DownloadUrl": str,
        "Errors": List[AssetBundleExportJobErrorTypeDef],
        "Arn": str,
        "CreatedTime": datetime,
        "AssetBundleExportJobId": str,
        "AwsAccountId": str,
        "ResourceArns": List[str],
        "IncludeAllDependencies": bool,
        "ExportFormat": AssetBundleExportFormatType,
        "CloudFormationOverridePropertyConfiguration": AssetBundleCloudFormationOverridePropertyConfigurationOutputTypeDef,
        "RequestId": str,
        "Status": int,
        "IncludePermissions": bool,
        "IncludeTags": bool,
        "ValidationStrategy": AssetBundleExportJobValidationStrategyTypeDef,
        "Warnings": List[AssetBundleExportJobWarningTypeDef],
        "IncludeFolderMemberships": bool,
        "IncludeFolderMembers": IncludeFolderMembersType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssetBundleCloudFormationOverridePropertyConfigurationTypeDef = TypedDict(
    "AssetBundleCloudFormationOverridePropertyConfigurationTypeDef",
    {
        "ResourceIdOverrideConfiguration": NotRequired[
            AssetBundleExportJobResourceIdOverrideConfigurationTypeDef
        ],
        "VPCConnections": NotRequired[
            Sequence[AssetBundleExportJobVPCConnectionOverridePropertiesUnionTypeDef]
        ],
        "RefreshSchedules": NotRequired[
            Sequence[AssetBundleExportJobRefreshScheduleOverridePropertiesUnionTypeDef]
        ],
        "DataSources": NotRequired[
            Sequence[AssetBundleExportJobDataSourceOverridePropertiesUnionTypeDef]
        ],
        "DataSets": NotRequired[
            Sequence[AssetBundleExportJobDataSetOverridePropertiesUnionTypeDef]
        ],
        "Themes": NotRequired[Sequence[AssetBundleExportJobThemeOverridePropertiesUnionTypeDef]],
        "Analyses": NotRequired[
            Sequence[AssetBundleExportJobAnalysisOverridePropertiesUnionTypeDef]
        ],
        "Dashboards": NotRequired[
            Sequence[AssetBundleExportJobDashboardOverridePropertiesUnionTypeDef]
        ],
        "Folders": NotRequired[Sequence[AssetBundleExportJobFolderOverridePropertiesUnionTypeDef]],
    },
)
AssetBundleImportJobDashboardOverridePermissionsOutputTypeDef = TypedDict(
    "AssetBundleImportJobDashboardOverridePermissionsOutputTypeDef",
    {
        "DashboardIds": List[str],
        "Permissions": NotRequired[AssetBundleResourcePermissionsOutputTypeDef],
        "LinkSharingConfiguration": NotRequired[
            AssetBundleResourceLinkSharingConfigurationOutputTypeDef
        ],
    },
)
AssetBundleImportJobAnalysisOverrideTagsUnionTypeDef = Union[
    AssetBundleImportJobAnalysisOverrideTagsTypeDef,
    AssetBundleImportJobAnalysisOverrideTagsOutputTypeDef,
]
AssetBundleImportJobDashboardOverrideTagsUnionTypeDef = Union[
    AssetBundleImportJobDashboardOverrideTagsTypeDef,
    AssetBundleImportJobDashboardOverrideTagsOutputTypeDef,
]
AssetBundleImportJobDataSetOverrideTagsUnionTypeDef = Union[
    AssetBundleImportJobDataSetOverrideTagsTypeDef,
    AssetBundleImportJobDataSetOverrideTagsOutputTypeDef,
]
AssetBundleImportJobDataSourceOverrideTagsUnionTypeDef = Union[
    AssetBundleImportJobDataSourceOverrideTagsTypeDef,
    AssetBundleImportJobDataSourceOverrideTagsOutputTypeDef,
]
AssetBundleImportJobFolderOverrideTagsUnionTypeDef = Union[
    AssetBundleImportJobFolderOverrideTagsTypeDef,
    AssetBundleImportJobFolderOverrideTagsOutputTypeDef,
]
AssetBundleImportJobThemeOverrideTagsUnionTypeDef = Union[
    AssetBundleImportJobThemeOverrideTagsTypeDef, AssetBundleImportJobThemeOverrideTagsOutputTypeDef
]
AssetBundleImportJobOverrideTagsOutputTypeDef = TypedDict(
    "AssetBundleImportJobOverrideTagsOutputTypeDef",
    {
        "VPCConnections": NotRequired[
            List[AssetBundleImportJobVPCConnectionOverrideTagsOutputTypeDef]
        ],
        "DataSources": NotRequired[List[AssetBundleImportJobDataSourceOverrideTagsOutputTypeDef]],
        "DataSets": NotRequired[List[AssetBundleImportJobDataSetOverrideTagsOutputTypeDef]],
        "Themes": NotRequired[List[AssetBundleImportJobThemeOverrideTagsOutputTypeDef]],
        "Analyses": NotRequired[List[AssetBundleImportJobAnalysisOverrideTagsOutputTypeDef]],
        "Dashboards": NotRequired[List[AssetBundleImportJobDashboardOverrideTagsOutputTypeDef]],
        "Folders": NotRequired[List[AssetBundleImportJobFolderOverrideTagsOutputTypeDef]],
    },
)
AssetBundleImportJobVPCConnectionOverrideTagsUnionTypeDef = Union[
    AssetBundleImportJobVPCConnectionOverrideTagsTypeDef,
    AssetBundleImportJobVPCConnectionOverrideTagsOutputTypeDef,
]
AssetBundleImportJobRefreshScheduleOverrideParametersUnionTypeDef = Union[
    AssetBundleImportJobRefreshScheduleOverrideParametersTypeDef,
    AssetBundleImportJobRefreshScheduleOverrideParametersOutputTypeDef,
]
CustomParameterValuesUnionTypeDef = Union[
    CustomParameterValuesTypeDef, CustomParameterValuesOutputTypeDef
]
DateTimeDatasetParameterDefaultValuesUnionTypeDef = Union[
    DateTimeDatasetParameterDefaultValuesTypeDef, DateTimeDatasetParameterDefaultValuesOutputTypeDef
]
DateTimeParameterUnionTypeDef = Union[DateTimeParameterTypeDef, DateTimeParameterOutputTypeDef]
DateTimeValueWhenUnsetConfigurationUnionTypeDef = Union[
    DateTimeValueWhenUnsetConfigurationTypeDef, DateTimeValueWhenUnsetConfigurationOutputTypeDef
]
NewDefaultValuesUnionTypeDef = Union[NewDefaultValuesTypeDef, NewDefaultValuesOutputTypeDef]
TimeRangeDrillDownFilterUnionTypeDef = Union[
    TimeRangeDrillDownFilterTypeDef, TimeRangeDrillDownFilterOutputTypeDef
]
CreateTopicRefreshScheduleRequestRequestTypeDef = TypedDict(
    "CreateTopicRefreshScheduleRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TopicId": str,
        "DatasetArn": str,
        "RefreshSchedule": TopicRefreshScheduleTypeDef,
        "DatasetName": NotRequired[str],
    },
)
UpdateTopicRefreshScheduleRequestRequestTypeDef = TypedDict(
    "UpdateTopicRefreshScheduleRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TopicId": str,
        "DatasetId": str,
        "RefreshSchedule": TopicRefreshScheduleTypeDef,
    },
)
WhatIfPointScenarioUnionTypeDef = Union[
    WhatIfPointScenarioTypeDef, WhatIfPointScenarioOutputTypeDef
]
WhatIfRangeScenarioUnionTypeDef = Union[
    WhatIfRangeScenarioTypeDef, WhatIfRangeScenarioOutputTypeDef
]
AssetBundleImportJobAnalysisOverridePermissionsTypeDef = TypedDict(
    "AssetBundleImportJobAnalysisOverridePermissionsTypeDef",
    {
        "AnalysisIds": Sequence[str],
        "Permissions": AssetBundleResourcePermissionsUnionTypeDef,
    },
)
AssetBundleImportJobDataSetOverridePermissionsTypeDef = TypedDict(
    "AssetBundleImportJobDataSetOverridePermissionsTypeDef",
    {
        "DataSetIds": Sequence[str],
        "Permissions": AssetBundleResourcePermissionsUnionTypeDef,
    },
)
AssetBundleImportJobDataSourceOverridePermissionsTypeDef = TypedDict(
    "AssetBundleImportJobDataSourceOverridePermissionsTypeDef",
    {
        "DataSourceIds": Sequence[str],
        "Permissions": AssetBundleResourcePermissionsUnionTypeDef,
    },
)
AssetBundleImportJobFolderOverridePermissionsTypeDef = TypedDict(
    "AssetBundleImportJobFolderOverridePermissionsTypeDef",
    {
        "FolderIds": Sequence[str],
        "Permissions": NotRequired[AssetBundleResourcePermissionsUnionTypeDef],
    },
)
AssetBundleImportJobThemeOverridePermissionsTypeDef = TypedDict(
    "AssetBundleImportJobThemeOverridePermissionsTypeDef",
    {
        "ThemeIds": Sequence[str],
        "Permissions": AssetBundleResourcePermissionsUnionTypeDef,
    },
)
AssetBundleResourceLinkSharingConfigurationTypeDef = TypedDict(
    "AssetBundleResourceLinkSharingConfigurationTypeDef",
    {
        "Permissions": NotRequired[AssetBundleResourcePermissionsUnionTypeDef],
    },
)
AxisDisplayRangeUnionTypeDef = Union[AxisDisplayRangeTypeDef, AxisDisplayRangeOutputTypeDef]
NumericAxisOptionsOutputTypeDef = TypedDict(
    "NumericAxisOptionsOutputTypeDef",
    {
        "Scale": NotRequired[AxisScaleTypeDef],
        "Range": NotRequired[AxisDisplayRangeOutputTypeDef],
    },
)
CreateColumnsOperationUnionTypeDef = Union[
    CreateColumnsOperationTypeDef, CreateColumnsOperationOutputTypeDef
]
ClusterMarkerConfigurationTypeDef = TypedDict(
    "ClusterMarkerConfigurationTypeDef",
    {
        "ClusterMarker": NotRequired[ClusterMarkerTypeDef],
    },
)
TopicConstantValueUnionTypeDef = Union[TopicConstantValueTypeDef, TopicConstantValueOutputTypeDef]
TopicCategoryFilterOutputTypeDef = TypedDict(
    "TopicCategoryFilterOutputTypeDef",
    {
        "CategoryFilterFunction": NotRequired[CategoryFilterFunctionType],
        "CategoryFilterType": NotRequired[CategoryFilterTypeType],
        "Constant": NotRequired[TopicCategoryFilterConstantOutputTypeDef],
        "Inverse": NotRequired[bool],
    },
)
TopicCategoryFilterConstantTypeDef = TypedDict(
    "TopicCategoryFilterConstantTypeDef",
    {
        "ConstantType": NotRequired[ConstantTypeType],
        "SingularConstant": NotRequired[str],
        "CollectiveConstant": NotRequired[CollectiveConstantUnionTypeDef],
    },
)
ColorScaleUnionTypeDef = Union[ColorScaleTypeDef, ColorScaleOutputTypeDef]
ColorsConfigurationUnionTypeDef = Union[
    ColorsConfigurationTypeDef, ColorsConfigurationOutputTypeDef
]
TagColumnOperationOutputTypeDef = TypedDict(
    "TagColumnOperationOutputTypeDef",
    {
        "ColumnName": str,
        "Tags": List[ColumnTagTypeDef],
    },
)
TagColumnOperationTypeDef = TypedDict(
    "TagColumnOperationTypeDef",
    {
        "ColumnName": str,
        "Tags": Sequence[ColumnTagTypeDef],
    },
)
ColumnGroupSchemaUnionTypeDef = Union[ColumnGroupSchemaTypeDef, ColumnGroupSchemaOutputTypeDef]
DataSetConfigurationOutputTypeDef = TypedDict(
    "DataSetConfigurationOutputTypeDef",
    {
        "Placeholder": NotRequired[str],
        "DataSetSchema": NotRequired[DataSetSchemaOutputTypeDef],
        "ColumnGroupSchemaList": NotRequired[List[ColumnGroupSchemaOutputTypeDef]],
    },
)
DataSetSchemaUnionTypeDef = Union[DataSetSchemaTypeDef, DataSetSchemaOutputTypeDef]
ConditionalFormattingIconTypeDef = TypedDict(
    "ConditionalFormattingIconTypeDef",
    {
        "IconSet": NotRequired[ConditionalFormattingIconSetTypeDef],
        "CustomCondition": NotRequired[ConditionalFormattingCustomIconConditionTypeDef],
    },
)
ListDataSetsResponseTypeDef = TypedDict(
    "ListDataSetsResponseTypeDef",
    {
        "DataSetSummaries": List[DataSetSummaryTypeDef],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
SearchDataSetsResponseTypeDef = TypedDict(
    "SearchDataSetsResponseTypeDef",
    {
        "DataSetSummaries": List[DataSetSummaryTypeDef],
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DestinationParameterValueConfigurationOutputTypeDef = TypedDict(
    "DestinationParameterValueConfigurationOutputTypeDef",
    {
        "CustomValuesConfiguration": NotRequired[CustomValuesConfigurationOutputTypeDef],
        "SelectAllValueOptions": NotRequired[Literal["ALL_VALUES"]],
        "SourceParameterName": NotRequired[str],
        "SourceField": NotRequired[str],
        "SourceColumn": NotRequired[ColumnIdentifierTypeDef],
    },
)
CustomSqlUnionTypeDef = Union[CustomSqlTypeDef, CustomSqlOutputTypeDef]
RelationalTableUnionTypeDef = Union[RelationalTableTypeDef, RelationalTableOutputTypeDef]
CustomContentConfigurationTypeDef = TypedDict(
    "CustomContentConfigurationTypeDef",
    {
        "ContentUrl": NotRequired[str],
        "ContentType": NotRequired[CustomContentTypeType],
        "ImageScaling": NotRequired[CustomContentImageScalingConfigurationType],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
DashboardPublishOptionsTypeDef = TypedDict(
    "DashboardPublishOptionsTypeDef",
    {
        "AdHocFilteringOption": NotRequired[AdHocFilteringOptionTypeDef],
        "ExportToCSVOption": NotRequired[ExportToCSVOptionTypeDef],
        "SheetControlsOption": NotRequired[SheetControlsOptionTypeDef],
        "VisualPublishOptions": NotRequired[DashboardVisualPublishOptionsTypeDef],
        "SheetLayoutElementMaximizationOption": NotRequired[
            SheetLayoutElementMaximizationOptionTypeDef
        ],
        "VisualMenuOption": NotRequired[VisualMenuOptionTypeDef],
        "VisualAxisSortOption": NotRequired[VisualAxisSortOptionTypeDef],
        "ExportWithHiddenFieldsOption": NotRequired[ExportWithHiddenFieldsOptionTypeDef],
        "DataPointDrillUpDownOption": NotRequired[DataPointDrillUpDownOptionTypeDef],
        "DataPointMenuLabelOption": NotRequired[DataPointMenuLabelOptionTypeDef],
        "DataPointTooltipOption": NotRequired[DataPointTooltipOptionTypeDef],
    },
)
DataPathColorTypeDef = TypedDict(
    "DataPathColorTypeDef",
    {
        "Element": DataPathValueTypeDef,
        "Color": str,
        "TimeGranularity": NotRequired[TimeGranularityType],
    },
)
DataPathSortOutputTypeDef = TypedDict(
    "DataPathSortOutputTypeDef",
    {
        "Direction": SortDirectionType,
        "SortPaths": List[DataPathValueTypeDef],
    },
)
DataPathSortTypeDef = TypedDict(
    "DataPathSortTypeDef",
    {
        "Direction": SortDirectionType,
        "SortPaths": Sequence[DataPathValueTypeDef],
    },
)
PivotTableDataPathOptionOutputTypeDef = TypedDict(
    "PivotTableDataPathOptionOutputTypeDef",
    {
        "DataPathList": List[DataPathValueTypeDef],
        "Width": NotRequired[str],
    },
)
PivotTableDataPathOptionTypeDef = TypedDict(
    "PivotTableDataPathOptionTypeDef",
    {
        "DataPathList": Sequence[DataPathValueTypeDef],
        "Width": NotRequired[str],
    },
)
PivotTableFieldCollapseStateTargetOutputTypeDef = TypedDict(
    "PivotTableFieldCollapseStateTargetOutputTypeDef",
    {
        "FieldId": NotRequired[str],
        "FieldDataPathValues": NotRequired[List[DataPathValueTypeDef]],
    },
)
PivotTableFieldCollapseStateTargetTypeDef = TypedDict(
    "PivotTableFieldCollapseStateTargetTypeDef",
    {
        "FieldId": NotRequired[str],
        "FieldDataPathValues": NotRequired[Sequence[DataPathValueTypeDef]],
    },
)
TimeRangeFilterValueUnionTypeDef = Union[
    TimeRangeFilterValueTypeDef, TimeRangeFilterValueOutputTypeDef
]
DecimalDatasetParameterTypeDef = TypedDict(
    "DecimalDatasetParameterTypeDef",
    {
        "Id": str,
        "Name": str,
        "ValueType": DatasetParameterValueTypeType,
        "DefaultValues": NotRequired[DecimalDatasetParameterDefaultValuesUnionTypeDef],
    },
)
DescribeDashboardPermissionsResponseTypeDef = TypedDict(
    "DescribeDashboardPermissionsResponseTypeDef",
    {
        "DashboardId": str,
        "DashboardArn": str,
        "Permissions": List[ResourcePermissionOutputTypeDef],
        "Status": int,
        "RequestId": str,
        "LinkSharingConfiguration": LinkSharingConfigurationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDashboardPermissionsResponseTypeDef = TypedDict(
    "UpdateDashboardPermissionsResponseTypeDef",
    {
        "DashboardArn": str,
        "DashboardId": str,
        "Permissions": List[ResourcePermissionOutputTypeDef],
        "RequestId": str,
        "Status": int,
        "LinkSharingConfiguration": LinkSharingConfigurationOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LinkSharingConfigurationTypeDef = TypedDict(
    "LinkSharingConfigurationTypeDef",
    {
        "Permissions": NotRequired[Sequence[ResourcePermissionUnionTypeDef]],
    },
)
ListTopicRefreshSchedulesResponseTypeDef = TypedDict(
    "ListTopicRefreshSchedulesResponseTypeDef",
    {
        "TopicId": str,
        "TopicArn": str,
        "RefreshSchedules": List[TopicRefreshScheduleSummaryTypeDef],
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DefaultFormattingTypeDef = TypedDict(
    "DefaultFormattingTypeDef",
    {
        "DisplayFormat": NotRequired[DisplayFormatType],
        "DisplayFormatOptions": NotRequired[DisplayFormatOptionsTypeDef],
    },
)
TopicIRMetricOutputTypeDef = TypedDict(
    "TopicIRMetricOutputTypeDef",
    {
        "MetricId": NotRequired[IdentifierTypeDef],
        "Function": NotRequired[AggFunctionOutputTypeDef],
        "Operands": NotRequired[List[IdentifierTypeDef]],
        "ComparisonMethod": NotRequired[TopicIRComparisonMethodTypeDef],
        "Expression": NotRequired[str],
        "CalculatedFieldReferences": NotRequired[List[IdentifierTypeDef]],
        "DisplayFormat": NotRequired[DisplayFormatType],
        "DisplayFormatOptions": NotRequired[DisplayFormatOptionsTypeDef],
        "NamedEntity": NotRequired[NamedEntityRefTypeDef],
    },
)
TopicIRMetricTypeDef = TypedDict(
    "TopicIRMetricTypeDef",
    {
        "MetricId": NotRequired[IdentifierTypeDef],
        "Function": NotRequired[AggFunctionUnionTypeDef],
        "Operands": NotRequired[Sequence[IdentifierTypeDef]],
        "ComparisonMethod": NotRequired[TopicIRComparisonMethodTypeDef],
        "Expression": NotRequired[str],
        "CalculatedFieldReferences": NotRequired[Sequence[IdentifierTypeDef]],
        "DisplayFormat": NotRequired[DisplayFormatType],
        "DisplayFormatOptions": NotRequired[DisplayFormatOptionsTypeDef],
        "NamedEntity": NotRequired[NamedEntityRefTypeDef],
    },
)
TopicIRFilterOptionOutputTypeDef = TypedDict(
    "TopicIRFilterOptionOutputTypeDef",
    {
        "FilterType": NotRequired[TopicIRFilterTypeType],
        "FilterClass": NotRequired[FilterClassType],
        "OperandField": NotRequired[IdentifierTypeDef],
        "Function": NotRequired[TopicIRFilterFunctionType],
        "Constant": NotRequired[TopicConstantValueOutputTypeDef],
        "Inverse": NotRequired[bool],
        "NullFilter": NotRequired[NullFilterOptionType],
        "Aggregation": NotRequired[AggTypeType],
        "AggregationFunctionParameters": NotRequired[Dict[str, str]],
        "AggregationPartitionBy": NotRequired[List[AggregationPartitionByTypeDef]],
        "Range": NotRequired[TopicConstantValueOutputTypeDef],
        "Inclusive": NotRequired[bool],
        "TimeGranularity": NotRequired[TimeGranularityType],
        "LastNextOffset": NotRequired[TopicConstantValueOutputTypeDef],
        "AggMetrics": NotRequired[List[FilterAggMetricsTypeDef]],
        "TopBottomLimit": NotRequired[TopicConstantValueOutputTypeDef],
        "SortDirection": NotRequired[TopicSortDirectionType],
        "Anchor": NotRequired[AnchorTypeDef],
    },
)
TopicIRGroupByTypeDef = TypedDict(
    "TopicIRGroupByTypeDef",
    {
        "FieldName": NotRequired[IdentifierTypeDef],
        "TimeGranularity": NotRequired[TopicTimeGranularityType],
        "Sort": NotRequired[TopicSortClauseTypeDef],
        "DisplayFormat": NotRequired[DisplayFormatType],
        "DisplayFormatOptions": NotRequired[DisplayFormatOptionsTypeDef],
        "NamedEntity": NotRequired[NamedEntityRefTypeDef],
    },
)
CategoryFilterConfigurationTypeDef = TypedDict(
    "CategoryFilterConfigurationTypeDef",
    {
        "FilterListConfiguration": NotRequired[FilterListConfigurationUnionTypeDef],
        "CustomFilterListConfiguration": NotRequired[CustomFilterListConfigurationUnionTypeDef],
        "CustomFilterConfiguration": NotRequired[CustomFilterConfigurationTypeDef],
    },
)
CustomActionFilterOperationOutputTypeDef = TypedDict(
    "CustomActionFilterOperationOutputTypeDef",
    {
        "SelectedFieldsConfiguration": FilterOperationSelectedFieldsConfigurationOutputTypeDef,
        "TargetVisualsConfiguration": FilterOperationTargetVisualsConfigurationOutputTypeDef,
    },
)
AxisLabelOptionsTypeDef = TypedDict(
    "AxisLabelOptionsTypeDef",
    {
        "FontConfiguration": NotRequired[FontConfigurationTypeDef],
        "CustomLabel": NotRequired[str],
        "ApplyTo": NotRequired[AxisLabelReferenceOptionsTypeDef],
    },
)
DataLabelOptionsOutputTypeDef = TypedDict(
    "DataLabelOptionsOutputTypeDef",
    {
        "Visibility": NotRequired[VisibilityType],
        "CategoryLabelVisibility": NotRequired[VisibilityType],
        "MeasureLabelVisibility": NotRequired[VisibilityType],
        "DataLabelTypes": NotRequired[List[DataLabelTypeTypeDef]],
        "Position": NotRequired[DataLabelPositionType],
        "LabelContent": NotRequired[DataLabelContentType],
        "LabelFontConfiguration": NotRequired[FontConfigurationTypeDef],
        "LabelColor": NotRequired[str],
        "Overlap": NotRequired[DataLabelOverlapType],
        "TotalsVisibility": NotRequired[VisibilityType],
    },
)
DataLabelOptionsTypeDef = TypedDict(
    "DataLabelOptionsTypeDef",
    {
        "Visibility": NotRequired[VisibilityType],
        "CategoryLabelVisibility": NotRequired[VisibilityType],
        "MeasureLabelVisibility": NotRequired[VisibilityType],
        "DataLabelTypes": NotRequired[Sequence[DataLabelTypeTypeDef]],
        "Position": NotRequired[DataLabelPositionType],
        "LabelContent": NotRequired[DataLabelContentType],
        "LabelFontConfiguration": NotRequired[FontConfigurationTypeDef],
        "LabelColor": NotRequired[str],
        "Overlap": NotRequired[DataLabelOverlapType],
        "TotalsVisibility": NotRequired[VisibilityType],
    },
)
FunnelChartDataLabelOptionsTypeDef = TypedDict(
    "FunnelChartDataLabelOptionsTypeDef",
    {
        "Visibility": NotRequired[VisibilityType],
        "CategoryLabelVisibility": NotRequired[VisibilityType],
        "MeasureLabelVisibility": NotRequired[VisibilityType],
        "Position": NotRequired[DataLabelPositionType],
        "LabelFontConfiguration": NotRequired[FontConfigurationTypeDef],
        "LabelColor": NotRequired[str],
        "MeasureDataLabelStyle": NotRequired[FunnelChartMeasureDataLabelStyleType],
    },
)
LabelOptionsTypeDef = TypedDict(
    "LabelOptionsTypeDef",
    {
        "Visibility": NotRequired[VisibilityType],
        "FontConfiguration": NotRequired[FontConfigurationTypeDef],
        "CustomLabel": NotRequired[str],
    },
)
PanelTitleOptionsTypeDef = TypedDict(
    "PanelTitleOptionsTypeDef",
    {
        "Visibility": NotRequired[VisibilityType],
        "FontConfiguration": NotRequired[FontConfigurationTypeDef],
        "HorizontalTextAlignment": NotRequired[HorizontalTextAlignmentType],
    },
)
TableFieldCustomTextContentTypeDef = TypedDict(
    "TableFieldCustomTextContentTypeDef",
    {
        "FontConfiguration": FontConfigurationTypeDef,
        "Value": NotRequired[str],
    },
)
TypographyUnionTypeDef = Union[TypographyTypeDef, TypographyOutputTypeDef]
ForecastConfigurationOutputTypeDef = TypedDict(
    "ForecastConfigurationOutputTypeDef",
    {
        "ForecastProperties": NotRequired[TimeBasedForecastPropertiesTypeDef],
        "Scenario": NotRequired[ForecastScenarioOutputTypeDef],
    },
)
DefaultFreeFormLayoutConfigurationTypeDef = TypedDict(
    "DefaultFreeFormLayoutConfigurationTypeDef",
    {
        "CanvasSizeOptions": FreeFormLayoutCanvasSizeOptionsTypeDef,
    },
)
SnapshotUserConfigurationTypeDef = TypedDict(
    "SnapshotUserConfigurationTypeDef",
    {
        "AnonymousUsers": NotRequired[Sequence[SnapshotAnonymousUserTypeDef]],
    },
)
ColumnGroupTypeDef = TypedDict(
    "ColumnGroupTypeDef",
    {
        "GeoSpatialColumnGroup": NotRequired[GeoSpatialColumnGroupUnionTypeDef],
    },
)
GeospatialHeatmapConfigurationOutputTypeDef = TypedDict(
    "GeospatialHeatmapConfigurationOutputTypeDef",
    {
        "HeatmapColor": NotRequired[GeospatialHeatmapColorScaleOutputTypeDef],
    },
)
GeospatialHeatmapColorScaleUnionTypeDef = Union[
    GeospatialHeatmapColorScaleTypeDef, GeospatialHeatmapColorScaleOutputTypeDef
]
GlobalTableBorderOptionsTypeDef = TypedDict(
    "GlobalTableBorderOptionsTypeDef",
    {
        "UniformBorder": NotRequired[TableBorderOptionsTypeDef],
        "SideSpecificBorder": NotRequired[TableSideBorderOptionsTypeDef],
    },
)
ConditionalFormattingGradientColorOutputTypeDef = TypedDict(
    "ConditionalFormattingGradientColorOutputTypeDef",
    {
        "Expression": str,
        "Color": GradientColorOutputTypeDef,
    },
)
GradientColorUnionTypeDef = Union[GradientColorTypeDef, GradientColorOutputTypeDef]
DefaultGridLayoutConfigurationTypeDef = TypedDict(
    "DefaultGridLayoutConfigurationTypeDef",
    {
        "CanvasSizeOptions": GridLayoutCanvasSizeOptionsTypeDef,
    },
)
GridLayoutConfigurationOutputTypeDef = TypedDict(
    "GridLayoutConfigurationOutputTypeDef",
    {
        "Elements": List[GridLayoutElementTypeDef],
        "CanvasSizeOptions": NotRequired[GridLayoutCanvasSizeOptionsTypeDef],
    },
)
GridLayoutConfigurationTypeDef = TypedDict(
    "GridLayoutConfigurationTypeDef",
    {
        "Elements": Sequence[GridLayoutElementTypeDef],
        "CanvasSizeOptions": NotRequired[GridLayoutCanvasSizeOptionsTypeDef],
    },
)
RefreshConfigurationTypeDef = TypedDict(
    "RefreshConfigurationTypeDef",
    {
        "IncrementalRefresh": IncrementalRefreshTypeDef,
    },
)
DescribeIngestionResponseTypeDef = TypedDict(
    "DescribeIngestionResponseTypeDef",
    {
        "Ingestion": IngestionTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListIngestionsResponseTypeDef = TypedDict(
    "ListIngestionsResponseTypeDef",
    {
        "Ingestions": List[IngestionTypeDef],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
IntegerDatasetParameterTypeDef = TypedDict(
    "IntegerDatasetParameterTypeDef",
    {
        "Id": str,
        "Name": str,
        "ValueType": DatasetParameterValueTypeType,
        "DefaultValues": NotRequired[IntegerDatasetParameterDefaultValuesUnionTypeDef],
    },
)
LogicalTableSourceTypeDef = TypedDict(
    "LogicalTableSourceTypeDef",
    {
        "JoinInstruction": NotRequired[JoinInstructionTypeDef],
        "PhysicalTableId": NotRequired[str],
        "DataSetArn": NotRequired[str],
    },
)
DataFieldSeriesItemTypeDef = TypedDict(
    "DataFieldSeriesItemTypeDef",
    {
        "FieldId": str,
        "AxisBinding": AxisBindingType,
        "FieldValue": NotRequired[str],
        "Settings": NotRequired[LineChartSeriesSettingsTypeDef],
    },
)
FieldSeriesItemTypeDef = TypedDict(
    "FieldSeriesItemTypeDef",
    {
        "FieldId": str,
        "AxisBinding": AxisBindingType,
        "Settings": NotRequired[LineChartSeriesSettingsTypeDef],
    },
)
SheetStyleTypeDef = TypedDict(
    "SheetStyleTypeDef",
    {
        "Tile": NotRequired[TileStyleTypeDef],
        "TileLayout": NotRequired[TileLayoutStyleTypeDef],
    },
)
TopicNamedEntityOutputTypeDef = TypedDict(
    "TopicNamedEntityOutputTypeDef",
    {
        "EntityName": str,
        "EntityDescription": NotRequired[str],
        "EntitySynonyms": NotRequired[List[str]],
        "SemanticEntityType": NotRequired[SemanticEntityTypeOutputTypeDef],
        "Definition": NotRequired[List[NamedEntityDefinitionOutputTypeDef]],
    },
)
NamedEntityDefinitionTypeDef = TypedDict(
    "NamedEntityDefinitionTypeDef",
    {
        "FieldName": NotRequired[str],
        "PropertyName": NotRequired[str],
        "PropertyRole": NotRequired[PropertyRoleType],
        "PropertyUsage": NotRequired[PropertyUsageType],
        "Metric": NotRequired[NamedEntityDefinitionMetricUnionTypeDef],
    },
)
DescribeNamespaceResponseTypeDef = TypedDict(
    "DescribeNamespaceResponseTypeDef",
    {
        "Namespace": NamespaceInfoV2TypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListNamespacesResponseTypeDef = TypedDict(
    "ListNamespacesResponseTypeDef",
    {
        "Namespaces": List[NamespaceInfoV2TypeDef],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListVPCConnectionsResponseTypeDef = TypedDict(
    "ListVPCConnectionsResponseTypeDef",
    {
        "VPCConnectionSummaries": List[VPCConnectionSummaryTypeDef],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeVPCConnectionResponseTypeDef = TypedDict(
    "DescribeVPCConnectionResponseTypeDef",
    {
        "VPCConnection": VPCConnectionTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CurrencyDisplayFormatConfigurationTypeDef = TypedDict(
    "CurrencyDisplayFormatConfigurationTypeDef",
    {
        "Prefix": NotRequired[str],
        "Suffix": NotRequired[str],
        "SeparatorConfiguration": NotRequired[NumericSeparatorConfigurationTypeDef],
        "Symbol": NotRequired[str],
        "DecimalPlacesConfiguration": NotRequired[DecimalPlacesConfigurationTypeDef],
        "NumberScale": NotRequired[NumberScaleType],
        "NegativeValueConfiguration": NotRequired[NegativeValueConfigurationTypeDef],
        "NullValueFormatConfiguration": NotRequired[NullValueFormatConfigurationTypeDef],
    },
)
NumberDisplayFormatConfigurationTypeDef = TypedDict(
    "NumberDisplayFormatConfigurationTypeDef",
    {
        "Prefix": NotRequired[str],
        "Suffix": NotRequired[str],
        "SeparatorConfiguration": NotRequired[NumericSeparatorConfigurationTypeDef],
        "DecimalPlacesConfiguration": NotRequired[DecimalPlacesConfigurationTypeDef],
        "NumberScale": NotRequired[NumberScaleType],
        "NegativeValueConfiguration": NotRequired[NegativeValueConfigurationTypeDef],
        "NullValueFormatConfiguration": NotRequired[NullValueFormatConfigurationTypeDef],
    },
)
PercentageDisplayFormatConfigurationTypeDef = TypedDict(
    "PercentageDisplayFormatConfigurationTypeDef",
    {
        "Prefix": NotRequired[str],
        "Suffix": NotRequired[str],
        "SeparatorConfiguration": NotRequired[NumericSeparatorConfigurationTypeDef],
        "DecimalPlacesConfiguration": NotRequired[DecimalPlacesConfigurationTypeDef],
        "NegativeValueConfiguration": NotRequired[NegativeValueConfigurationTypeDef],
        "NullValueFormatConfiguration": NotRequired[NullValueFormatConfigurationTypeDef],
    },
)
AggregationFunctionTypeDef = TypedDict(
    "AggregationFunctionTypeDef",
    {
        "NumericalAggregationFunction": NotRequired[NumericalAggregationFunctionTypeDef],
        "CategoricalAggregationFunction": NotRequired[CategoricalAggregationFunctionType],
        "DateAggregationFunction": NotRequired[DateAggregationFunctionType],
        "AttributeAggregationFunction": NotRequired[AttributeAggregationFunctionTypeDef],
    },
)
ScrollBarOptionsTypeDef = TypedDict(
    "ScrollBarOptionsTypeDef",
    {
        "Visibility": NotRequired[VisibilityType],
        "VisibleRange": NotRequired[VisibleRangeOptionsTypeDef],
    },
)
TopicDateRangeFilterTypeDef = TypedDict(
    "TopicDateRangeFilterTypeDef",
    {
        "Inclusive": NotRequired[bool],
        "Constant": NotRequired[TopicRangeFilterConstantTypeDef],
    },
)
TopicNumericRangeFilterTypeDef = TypedDict(
    "TopicNumericRangeFilterTypeDef",
    {
        "Inclusive": NotRequired[bool],
        "Constant": NotRequired[TopicRangeFilterConstantTypeDef],
        "Aggregation": NotRequired[NamedFilterAggTypeType],
    },
)
DataSourceParametersOutputTypeDef = TypedDict(
    "DataSourceParametersOutputTypeDef",
    {
        "AmazonElasticsearchParameters": NotRequired[AmazonElasticsearchParametersTypeDef],
        "AthenaParameters": NotRequired[AthenaParametersTypeDef],
        "AuroraParameters": NotRequired[AuroraParametersTypeDef],
        "AuroraPostgreSqlParameters": NotRequired[AuroraPostgreSqlParametersTypeDef],
        "AwsIotAnalyticsParameters": NotRequired[AwsIotAnalyticsParametersTypeDef],
        "JiraParameters": NotRequired[JiraParametersTypeDef],
        "MariaDbParameters": NotRequired[MariaDbParametersTypeDef],
        "MySqlParameters": NotRequired[MySqlParametersTypeDef],
        "OracleParameters": NotRequired[OracleParametersTypeDef],
        "PostgreSqlParameters": NotRequired[PostgreSqlParametersTypeDef],
        "PrestoParameters": NotRequired[PrestoParametersTypeDef],
        "RdsParameters": NotRequired[RdsParametersTypeDef],
        "RedshiftParameters": NotRequired[RedshiftParametersOutputTypeDef],
        "S3Parameters": NotRequired[S3ParametersTypeDef],
        "ServiceNowParameters": NotRequired[ServiceNowParametersTypeDef],
        "SnowflakeParameters": NotRequired[SnowflakeParametersTypeDef],
        "SparkParameters": NotRequired[SparkParametersTypeDef],
        "SqlServerParameters": NotRequired[SqlServerParametersTypeDef],
        "TeradataParameters": NotRequired[TeradataParametersTypeDef],
        "TwitterParameters": NotRequired[TwitterParametersTypeDef],
        "AmazonOpenSearchParameters": NotRequired[AmazonOpenSearchParametersTypeDef],
        "ExasolParameters": NotRequired[ExasolParametersTypeDef],
        "DatabricksParameters": NotRequired[DatabricksParametersTypeDef],
        "StarburstParameters": NotRequired[StarburstParametersTypeDef],
        "TrinoParameters": NotRequired[TrinoParametersTypeDef],
        "BigQueryParameters": NotRequired[BigQueryParametersTypeDef],
    },
)
RedshiftParametersTypeDef = TypedDict(
    "RedshiftParametersTypeDef",
    {
        "Database": str,
        "Host": NotRequired[str],
        "Port": NotRequired[int],
        "ClusterId": NotRequired[str],
        "IAMParameters": NotRequired[RedshiftIAMParametersUnionTypeDef],
        "IdentityCenterConfiguration": NotRequired[IdentityCenterConfigurationTypeDef],
    },
)
RefreshScheduleOutputTypeDef = TypedDict(
    "RefreshScheduleOutputTypeDef",
    {
        "ScheduleId": str,
        "ScheduleFrequency": RefreshFrequencyTypeDef,
        "RefreshType": IngestionTypeType,
        "StartAfterDateTime": NotRequired[datetime],
        "Arn": NotRequired[str],
    },
)
RefreshScheduleTypeDef = TypedDict(
    "RefreshScheduleTypeDef",
    {
        "ScheduleId": str,
        "ScheduleFrequency": RefreshFrequencyTypeDef,
        "RefreshType": IngestionTypeType,
        "StartAfterDateTime": NotRequired[TimestampTypeDef],
        "Arn": NotRequired[str],
    },
)
RegisteredUserQuickSightConsoleEmbeddingConfigurationTypeDef = TypedDict(
    "RegisteredUserQuickSightConsoleEmbeddingConfigurationTypeDef",
    {
        "InitialPath": NotRequired[str],
        "FeatureConfigurations": NotRequired[RegisteredUserConsoleFeatureConfigurationsTypeDef],
    },
)
RegisteredUserDashboardEmbeddingConfigurationTypeDef = TypedDict(
    "RegisteredUserDashboardEmbeddingConfigurationTypeDef",
    {
        "InitialDashboardId": str,
        "FeatureConfigurations": NotRequired[RegisteredUserDashboardFeatureConfigurationsTypeDef],
    },
)
SnapshotDestinationConfigurationOutputTypeDef = TypedDict(
    "SnapshotDestinationConfigurationOutputTypeDef",
    {
        "S3Destinations": NotRequired[List[SnapshotS3DestinationConfigurationTypeDef]],
    },
)
SnapshotDestinationConfigurationTypeDef = TypedDict(
    "SnapshotDestinationConfigurationTypeDef",
    {
        "S3Destinations": NotRequired[Sequence[SnapshotS3DestinationConfigurationTypeDef]],
    },
)
SnapshotJobS3ResultTypeDef = TypedDict(
    "SnapshotJobS3ResultTypeDef",
    {
        "S3DestinationConfiguration": NotRequired[SnapshotS3DestinationConfigurationTypeDef],
        "S3Uri": NotRequired[str],
        "ErrorInfo": NotRequired[List[SnapshotJobResultErrorInfoTypeDef]],
    },
)
PhysicalTableOutputTypeDef = TypedDict(
    "PhysicalTableOutputTypeDef",
    {
        "RelationalTable": NotRequired[RelationalTableOutputTypeDef],
        "CustomSql": NotRequired[CustomSqlOutputTypeDef],
        "S3Source": NotRequired[S3SourceOutputTypeDef],
    },
)
S3SourceUnionTypeDef = Union[S3SourceTypeDef, S3SourceOutputTypeDef]
FilterOperationTargetVisualsConfigurationTypeDef = TypedDict(
    "FilterOperationTargetVisualsConfigurationTypeDef",
    {
        "SameSheetTargetVisualConfiguration": NotRequired[
            SameSheetTargetVisualConfigurationUnionTypeDef
        ],
    },
)
SectionBasedLayoutCanvasSizeOptionsTypeDef = TypedDict(
    "SectionBasedLayoutCanvasSizeOptionsTypeDef",
    {
        "PaperCanvasSizeOptions": NotRequired[SectionBasedLayoutPaperCanvasSizeOptionsTypeDef],
    },
)
FilterScopeConfigurationOutputTypeDef = TypedDict(
    "FilterScopeConfigurationOutputTypeDef",
    {
        "SelectedSheets": NotRequired[SelectedSheetsFilterScopeConfigurationOutputTypeDef],
        "AllSheets": NotRequired[Dict[str, Any]],
    },
)
FreeFormLayoutElementOutputTypeDef = TypedDict(
    "FreeFormLayoutElementOutputTypeDef",
    {
        "ElementId": str,
        "ElementType": LayoutElementTypeType,
        "XAxisLocation": str,
        "YAxisLocation": str,
        "Width": str,
        "Height": str,
        "Visibility": NotRequired[VisibilityType],
        "RenderingRules": NotRequired[List[SheetElementRenderingRuleTypeDef]],
        "BorderStyle": NotRequired[FreeFormLayoutElementBorderStyleTypeDef],
        "SelectedBorderStyle": NotRequired[FreeFormLayoutElementBorderStyleTypeDef],
        "BackgroundStyle": NotRequired[FreeFormLayoutElementBackgroundStyleTypeDef],
        "LoadingAnimation": NotRequired[LoadingAnimationTypeDef],
    },
)
FreeFormLayoutElementTypeDef = TypedDict(
    "FreeFormLayoutElementTypeDef",
    {
        "ElementId": str,
        "ElementType": LayoutElementTypeType,
        "XAxisLocation": str,
        "YAxisLocation": str,
        "Width": str,
        "Height": str,
        "Visibility": NotRequired[VisibilityType],
        "RenderingRules": NotRequired[Sequence[SheetElementRenderingRuleTypeDef]],
        "BorderStyle": NotRequired[FreeFormLayoutElementBorderStyleTypeDef],
        "SelectedBorderStyle": NotRequired[FreeFormLayoutElementBorderStyleTypeDef],
        "BackgroundStyle": NotRequired[FreeFormLayoutElementBackgroundStyleTypeDef],
        "LoadingAnimation": NotRequired[LoadingAnimationTypeDef],
    },
)
SelectedSheetsFilterScopeConfigurationTypeDef = TypedDict(
    "SelectedSheetsFilterScopeConfigurationTypeDef",
    {
        "SheetVisualScopingConfigurations": NotRequired[
            Sequence[SheetVisualScopingConfigurationUnionTypeDef]
        ],
    },
)
TopicTemplateUnionTypeDef = Union[TopicTemplateTypeDef, TopicTemplateOutputTypeDef]
SnapshotFileGroupOutputTypeDef = TypedDict(
    "SnapshotFileGroupOutputTypeDef",
    {
        "Files": NotRequired[List[SnapshotFileOutputTypeDef]],
    },
)
SnapshotFileTypeDef = TypedDict(
    "SnapshotFileTypeDef",
    {
        "SheetSelections": Sequence[SnapshotFileSheetSelectionUnionTypeDef],
        "FormatType": SnapshotFileFormatTypeType,
    },
)
DatasetParameterOutputTypeDef = TypedDict(
    "DatasetParameterOutputTypeDef",
    {
        "StringDatasetParameter": NotRequired[StringDatasetParameterOutputTypeDef],
        "DecimalDatasetParameter": NotRequired[DecimalDatasetParameterOutputTypeDef],
        "IntegerDatasetParameter": NotRequired[IntegerDatasetParameterOutputTypeDef],
        "DateTimeDatasetParameter": NotRequired[DateTimeDatasetParameterOutputTypeDef],
    },
)
StringDatasetParameterTypeDef = TypedDict(
    "StringDatasetParameterTypeDef",
    {
        "Id": str,
        "Name": str,
        "ValueType": DatasetParameterValueTypeType,
        "DefaultValues": NotRequired[StringDatasetParameterDefaultValuesUnionTypeDef],
    },
)
FilterCrossSheetControlOutputTypeDef = TypedDict(
    "FilterCrossSheetControlOutputTypeDef",
    {
        "FilterControlId": str,
        "SourceFilterId": str,
        "CascadingControlConfiguration": NotRequired[CascadingControlConfigurationOutputTypeDef],
    },
)
CascadingControlConfigurationUnionTypeDef = Union[
    CascadingControlConfigurationTypeDef, CascadingControlConfigurationOutputTypeDef
]
DateTimeParameterDeclarationOutputTypeDef = TypedDict(
    "DateTimeParameterDeclarationOutputTypeDef",
    {
        "Name": str,
        "DefaultValues": NotRequired[DateTimeDefaultValuesOutputTypeDef],
        "TimeGranularity": NotRequired[TimeGranularityType],
        "ValueWhenUnset": NotRequired[DateTimeValueWhenUnsetConfigurationOutputTypeDef],
        "MappedDataSetParameters": NotRequired[List[MappedDataSetParameterTypeDef]],
    },
)
DateTimeDefaultValuesUnionTypeDef = Union[
    DateTimeDefaultValuesTypeDef, DateTimeDefaultValuesOutputTypeDef
]
DecimalParameterDeclarationOutputTypeDef = TypedDict(
    "DecimalParameterDeclarationOutputTypeDef",
    {
        "ParameterValueType": ParameterValueTypeType,
        "Name": str,
        "DefaultValues": NotRequired[DecimalDefaultValuesOutputTypeDef],
        "ValueWhenUnset": NotRequired[DecimalValueWhenUnsetConfigurationTypeDef],
        "MappedDataSetParameters": NotRequired[List[MappedDataSetParameterTypeDef]],
    },
)
DecimalDefaultValuesUnionTypeDef = Union[
    DecimalDefaultValuesTypeDef, DecimalDefaultValuesOutputTypeDef
]
IntegerParameterDeclarationOutputTypeDef = TypedDict(
    "IntegerParameterDeclarationOutputTypeDef",
    {
        "ParameterValueType": ParameterValueTypeType,
        "Name": str,
        "DefaultValues": NotRequired[IntegerDefaultValuesOutputTypeDef],
        "ValueWhenUnset": NotRequired[IntegerValueWhenUnsetConfigurationTypeDef],
        "MappedDataSetParameters": NotRequired[List[MappedDataSetParameterTypeDef]],
    },
)
IntegerDefaultValuesUnionTypeDef = Union[
    IntegerDefaultValuesTypeDef, IntegerDefaultValuesOutputTypeDef
]
StringParameterDeclarationOutputTypeDef = TypedDict(
    "StringParameterDeclarationOutputTypeDef",
    {
        "ParameterValueType": ParameterValueTypeType,
        "Name": str,
        "DefaultValues": NotRequired[StringDefaultValuesOutputTypeDef],
        "ValueWhenUnset": NotRequired[StringValueWhenUnsetConfigurationTypeDef],
        "MappedDataSetParameters": NotRequired[List[MappedDataSetParameterTypeDef]],
    },
)
StringDefaultValuesUnionTypeDef = Union[
    StringDefaultValuesTypeDef, StringDefaultValuesOutputTypeDef
]
DateTimeHierarchyOutputTypeDef = TypedDict(
    "DateTimeHierarchyOutputTypeDef",
    {
        "HierarchyId": str,
        "DrillDownFilters": NotRequired[List[DrillDownFilterOutputTypeDef]],
    },
)
ExplicitHierarchyOutputTypeDef = TypedDict(
    "ExplicitHierarchyOutputTypeDef",
    {
        "HierarchyId": str,
        "Columns": List[ColumnIdentifierTypeDef],
        "DrillDownFilters": NotRequired[List[DrillDownFilterOutputTypeDef]],
    },
)
PredefinedHierarchyOutputTypeDef = TypedDict(
    "PredefinedHierarchyOutputTypeDef",
    {
        "HierarchyId": str,
        "Columns": List[ColumnIdentifierTypeDef],
        "DrillDownFilters": NotRequired[List[DrillDownFilterOutputTypeDef]],
    },
)
DescribeAnalysisResponseTypeDef = TypedDict(
    "DescribeAnalysisResponseTypeDef",
    {
        "Analysis": AnalysisTypeDef,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DashboardTypeDef = TypedDict(
    "DashboardTypeDef",
    {
        "DashboardId": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Version": NotRequired[DashboardVersionTypeDef],
        "CreatedTime": NotRequired[datetime],
        "LastPublishedTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "LinkEntities": NotRequired[List[str]],
    },
)
AnonymousUserEmbeddingExperienceConfigurationTypeDef = TypedDict(
    "AnonymousUserEmbeddingExperienceConfigurationTypeDef",
    {
        "Dashboard": NotRequired[AnonymousUserDashboardEmbeddingConfigurationTypeDef],
        "DashboardVisual": NotRequired[AnonymousUserDashboardVisualEmbeddingConfigurationTypeDef],
        "QSearchBar": NotRequired[AnonymousUserQSearchBarEmbeddingConfigurationTypeDef],
        "GenerativeQnA": NotRequired[AnonymousUserGenerativeQnAEmbeddingConfigurationTypeDef],
    },
)
StartAssetBundleExportJobRequestRequestTypeDef = TypedDict(
    "StartAssetBundleExportJobRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AssetBundleExportJobId": str,
        "ResourceArns": Sequence[str],
        "ExportFormat": AssetBundleExportFormatType,
        "IncludeAllDependencies": NotRequired[bool],
        "CloudFormationOverridePropertyConfiguration": NotRequired[
            AssetBundleCloudFormationOverridePropertyConfigurationTypeDef
        ],
        "IncludePermissions": NotRequired[bool],
        "IncludeTags": NotRequired[bool],
        "ValidationStrategy": NotRequired[AssetBundleExportJobValidationStrategyTypeDef],
        "IncludeFolderMemberships": NotRequired[bool],
        "IncludeFolderMembers": NotRequired[IncludeFolderMembersType],
    },
)
AssetBundleImportJobOverridePermissionsOutputTypeDef = TypedDict(
    "AssetBundleImportJobOverridePermissionsOutputTypeDef",
    {
        "DataSources": NotRequired[
            List[AssetBundleImportJobDataSourceOverridePermissionsOutputTypeDef]
        ],
        "DataSets": NotRequired[List[AssetBundleImportJobDataSetOverridePermissionsOutputTypeDef]],
        "Themes": NotRequired[List[AssetBundleImportJobThemeOverridePermissionsOutputTypeDef]],
        "Analyses": NotRequired[List[AssetBundleImportJobAnalysisOverridePermissionsOutputTypeDef]],
        "Dashboards": NotRequired[
            List[AssetBundleImportJobDashboardOverridePermissionsOutputTypeDef]
        ],
        "Folders": NotRequired[List[AssetBundleImportJobFolderOverridePermissionsOutputTypeDef]],
    },
)
AssetBundleImportJobOverrideTagsTypeDef = TypedDict(
    "AssetBundleImportJobOverrideTagsTypeDef",
    {
        "VPCConnections": NotRequired[
            Sequence[AssetBundleImportJobVPCConnectionOverrideTagsUnionTypeDef]
        ],
        "DataSources": NotRequired[
            Sequence[AssetBundleImportJobDataSourceOverrideTagsUnionTypeDef]
        ],
        "DataSets": NotRequired[Sequence[AssetBundleImportJobDataSetOverrideTagsUnionTypeDef]],
        "Themes": NotRequired[Sequence[AssetBundleImportJobThemeOverrideTagsUnionTypeDef]],
        "Analyses": NotRequired[Sequence[AssetBundleImportJobAnalysisOverrideTagsUnionTypeDef]],
        "Dashboards": NotRequired[Sequence[AssetBundleImportJobDashboardOverrideTagsUnionTypeDef]],
        "Folders": NotRequired[Sequence[AssetBundleImportJobFolderOverrideTagsUnionTypeDef]],
    },
)
CustomValuesConfigurationTypeDef = TypedDict(
    "CustomValuesConfigurationTypeDef",
    {
        "CustomValues": CustomParameterValuesUnionTypeDef,
        "IncludeNullValue": NotRequired[bool],
    },
)
DateTimeDatasetParameterTypeDef = TypedDict(
    "DateTimeDatasetParameterTypeDef",
    {
        "Id": str,
        "Name": str,
        "ValueType": DatasetParameterValueTypeType,
        "TimeGranularity": NotRequired[TimeGranularityType],
        "DefaultValues": NotRequired[DateTimeDatasetParameterDefaultValuesUnionTypeDef],
    },
)
ParametersTypeDef = TypedDict(
    "ParametersTypeDef",
    {
        "StringParameters": NotRequired[Sequence[StringParameterUnionTypeDef]],
        "IntegerParameters": NotRequired[Sequence[IntegerParameterUnionTypeDef]],
        "DecimalParameters": NotRequired[Sequence[DecimalParameterUnionTypeDef]],
        "DateTimeParameters": NotRequired[Sequence[DateTimeParameterUnionTypeDef]],
    },
)
OverrideDatasetParameterOperationTypeDef = TypedDict(
    "OverrideDatasetParameterOperationTypeDef",
    {
        "ParameterName": str,
        "NewParameterName": NotRequired[str],
        "NewDefaultValues": NotRequired[NewDefaultValuesUnionTypeDef],
    },
)
DrillDownFilterTypeDef = TypedDict(
    "DrillDownFilterTypeDef",
    {
        "NumericEqualityFilter": NotRequired[NumericEqualityDrillDownFilterTypeDef],
        "CategoryFilter": NotRequired[CategoryDrillDownFilterUnionTypeDef],
        "TimeRangeFilter": NotRequired[TimeRangeDrillDownFilterUnionTypeDef],
    },
)
ForecastScenarioTypeDef = TypedDict(
    "ForecastScenarioTypeDef",
    {
        "WhatIfPointScenario": NotRequired[WhatIfPointScenarioUnionTypeDef],
        "WhatIfRangeScenario": NotRequired[WhatIfRangeScenarioUnionTypeDef],
    },
)
AssetBundleImportJobAnalysisOverridePermissionsUnionTypeDef = Union[
    AssetBundleImportJobAnalysisOverridePermissionsTypeDef,
    AssetBundleImportJobAnalysisOverridePermissionsOutputTypeDef,
]
AssetBundleImportJobDataSetOverridePermissionsUnionTypeDef = Union[
    AssetBundleImportJobDataSetOverridePermissionsTypeDef,
    AssetBundleImportJobDataSetOverridePermissionsOutputTypeDef,
]
AssetBundleImportJobDataSourceOverridePermissionsUnionTypeDef = Union[
    AssetBundleImportJobDataSourceOverridePermissionsTypeDef,
    AssetBundleImportJobDataSourceOverridePermissionsOutputTypeDef,
]
AssetBundleImportJobFolderOverridePermissionsUnionTypeDef = Union[
    AssetBundleImportJobFolderOverridePermissionsTypeDef,
    AssetBundleImportJobFolderOverridePermissionsOutputTypeDef,
]
AssetBundleImportJobThemeOverridePermissionsUnionTypeDef = Union[
    AssetBundleImportJobThemeOverridePermissionsTypeDef,
    AssetBundleImportJobThemeOverridePermissionsOutputTypeDef,
]
AssetBundleResourceLinkSharingConfigurationUnionTypeDef = Union[
    AssetBundleResourceLinkSharingConfigurationTypeDef,
    AssetBundleResourceLinkSharingConfigurationOutputTypeDef,
]
NumericAxisOptionsTypeDef = TypedDict(
    "NumericAxisOptionsTypeDef",
    {
        "Scale": NotRequired[AxisScaleTypeDef],
        "Range": NotRequired[AxisDisplayRangeUnionTypeDef],
    },
)
AxisDataOptionsOutputTypeDef = TypedDict(
    "AxisDataOptionsOutputTypeDef",
    {
        "NumericAxisOptions": NotRequired[NumericAxisOptionsOutputTypeDef],
        "DateAxisOptions": NotRequired[DateAxisOptionsTypeDef],
    },
)
TopicIRFilterOptionTypeDef = TypedDict(
    "TopicIRFilterOptionTypeDef",
    {
        "FilterType": NotRequired[TopicIRFilterTypeType],
        "FilterClass": NotRequired[FilterClassType],
        "OperandField": NotRequired[IdentifierTypeDef],
        "Function": NotRequired[TopicIRFilterFunctionType],
        "Constant": NotRequired[TopicConstantValueUnionTypeDef],
        "Inverse": NotRequired[bool],
        "NullFilter": NotRequired[NullFilterOptionType],
        "Aggregation": NotRequired[AggTypeType],
        "AggregationFunctionParameters": NotRequired[Mapping[str, str]],
        "AggregationPartitionBy": NotRequired[Sequence[AggregationPartitionByTypeDef]],
        "Range": NotRequired[TopicConstantValueUnionTypeDef],
        "Inclusive": NotRequired[bool],
        "TimeGranularity": NotRequired[TimeGranularityType],
        "LastNextOffset": NotRequired[TopicConstantValueUnionTypeDef],
        "AggMetrics": NotRequired[Sequence[FilterAggMetricsTypeDef]],
        "TopBottomLimit": NotRequired[TopicConstantValueUnionTypeDef],
        "SortDirection": NotRequired[TopicSortDirectionType],
        "Anchor": NotRequired[AnchorTypeDef],
    },
)
TopicCategoryFilterConstantUnionTypeDef = Union[
    TopicCategoryFilterConstantTypeDef, TopicCategoryFilterConstantOutputTypeDef
]
TransformOperationOutputTypeDef = TypedDict(
    "TransformOperationOutputTypeDef",
    {
        "ProjectOperation": NotRequired[ProjectOperationOutputTypeDef],
        "FilterOperation": NotRequired[FilterOperationTypeDef],
        "CreateColumnsOperation": NotRequired[CreateColumnsOperationOutputTypeDef],
        "RenameColumnOperation": NotRequired[RenameColumnOperationTypeDef],
        "CastColumnTypeOperation": NotRequired[CastColumnTypeOperationTypeDef],
        "TagColumnOperation": NotRequired[TagColumnOperationOutputTypeDef],
        "UntagColumnOperation": NotRequired[UntagColumnOperationOutputTypeDef],
        "OverrideDatasetParameterOperation": NotRequired[
            OverrideDatasetParameterOperationOutputTypeDef
        ],
    },
)
TagColumnOperationUnionTypeDef = Union[TagColumnOperationTypeDef, TagColumnOperationOutputTypeDef]
TemplateVersionTypeDef = TypedDict(
    "TemplateVersionTypeDef",
    {
        "CreatedTime": NotRequired[datetime],
        "Errors": NotRequired[List[TemplateErrorTypeDef]],
        "VersionNumber": NotRequired[int],
        "Status": NotRequired[ResourceStatusType],
        "DataSetConfigurations": NotRequired[List[DataSetConfigurationOutputTypeDef]],
        "Description": NotRequired[str],
        "SourceEntityArn": NotRequired[str],
        "ThemeArn": NotRequired[str],
        "Sheets": NotRequired[List[SheetTypeDef]],
    },
)
DataSetConfigurationTypeDef = TypedDict(
    "DataSetConfigurationTypeDef",
    {
        "Placeholder": NotRequired[str],
        "DataSetSchema": NotRequired[DataSetSchemaUnionTypeDef],
        "ColumnGroupSchemaList": NotRequired[Sequence[ColumnGroupSchemaUnionTypeDef]],
    },
)
SetParameterValueConfigurationOutputTypeDef = TypedDict(
    "SetParameterValueConfigurationOutputTypeDef",
    {
        "DestinationParameterName": str,
        "Value": DestinationParameterValueConfigurationOutputTypeDef,
    },
)
VisualPaletteOutputTypeDef = TypedDict(
    "VisualPaletteOutputTypeDef",
    {
        "ChartColor": NotRequired[str],
        "ColorMap": NotRequired[List[DataPathColorTypeDef]],
    },
)
VisualPaletteTypeDef = TypedDict(
    "VisualPaletteTypeDef",
    {
        "ChartColor": NotRequired[str],
        "ColorMap": NotRequired[Sequence[DataPathColorTypeDef]],
    },
)
DataPathSortUnionTypeDef = Union[DataPathSortTypeDef, DataPathSortOutputTypeDef]
PivotTableDataPathOptionUnionTypeDef = Union[
    PivotTableDataPathOptionTypeDef, PivotTableDataPathOptionOutputTypeDef
]
PivotTableFieldCollapseStateOptionOutputTypeDef = TypedDict(
    "PivotTableFieldCollapseStateOptionOutputTypeDef",
    {
        "Target": PivotTableFieldCollapseStateTargetOutputTypeDef,
        "State": NotRequired[PivotTableFieldCollapseStateType],
    },
)
PivotTableFieldCollapseStateTargetUnionTypeDef = Union[
    PivotTableFieldCollapseStateTargetTypeDef, PivotTableFieldCollapseStateTargetOutputTypeDef
]
DecimalDatasetParameterUnionTypeDef = Union[
    DecimalDatasetParameterTypeDef, DecimalDatasetParameterOutputTypeDef
]
TopicCalculatedFieldOutputTypeDef = TypedDict(
    "TopicCalculatedFieldOutputTypeDef",
    {
        "CalculatedFieldName": str,
        "Expression": str,
        "CalculatedFieldDescription": NotRequired[str],
        "CalculatedFieldSynonyms": NotRequired[List[str]],
        "IsIncludedInTopic": NotRequired[bool],
        "DisableIndexing": NotRequired[bool],
        "ColumnDataRole": NotRequired[ColumnDataRoleType],
        "TimeGranularity": NotRequired[TopicTimeGranularityType],
        "DefaultFormatting": NotRequired[DefaultFormattingTypeDef],
        "Aggregation": NotRequired[DefaultAggregationType],
        "ComparativeOrder": NotRequired[ComparativeOrderOutputTypeDef],
        "SemanticType": NotRequired[SemanticTypeOutputTypeDef],
        "AllowedAggregations": NotRequired[List[AuthorSpecifiedAggregationType]],
        "NotAllowedAggregations": NotRequired[List[AuthorSpecifiedAggregationType]],
        "NeverAggregateInFilter": NotRequired[bool],
        "CellValueSynonyms": NotRequired[List[CellValueSynonymOutputTypeDef]],
        "NonAdditive": NotRequired[bool],
    },
)
TopicCalculatedFieldTypeDef = TypedDict(
    "TopicCalculatedFieldTypeDef",
    {
        "CalculatedFieldName": str,
        "Expression": str,
        "CalculatedFieldDescription": NotRequired[str],
        "CalculatedFieldSynonyms": NotRequired[Sequence[str]],
        "IsIncludedInTopic": NotRequired[bool],
        "DisableIndexing": NotRequired[bool],
        "ColumnDataRole": NotRequired[ColumnDataRoleType],
        "TimeGranularity": NotRequired[TopicTimeGranularityType],
        "DefaultFormatting": NotRequired[DefaultFormattingTypeDef],
        "Aggregation": NotRequired[DefaultAggregationType],
        "ComparativeOrder": NotRequired[ComparativeOrderUnionTypeDef],
        "SemanticType": NotRequired[SemanticTypeUnionTypeDef],
        "AllowedAggregations": NotRequired[Sequence[AuthorSpecifiedAggregationType]],
        "NotAllowedAggregations": NotRequired[Sequence[AuthorSpecifiedAggregationType]],
        "NeverAggregateInFilter": NotRequired[bool],
        "CellValueSynonyms": NotRequired[Sequence[CellValueSynonymTypeDef]],
        "NonAdditive": NotRequired[bool],
    },
)
TopicColumnOutputTypeDef = TypedDict(
    "TopicColumnOutputTypeDef",
    {
        "ColumnName": str,
        "ColumnFriendlyName": NotRequired[str],
        "ColumnDescription": NotRequired[str],
        "ColumnSynonyms": NotRequired[List[str]],
        "ColumnDataRole": NotRequired[ColumnDataRoleType],
        "Aggregation": NotRequired[DefaultAggregationType],
        "IsIncludedInTopic": NotRequired[bool],
        "DisableIndexing": NotRequired[bool],
        "ComparativeOrder": NotRequired[ComparativeOrderOutputTypeDef],
        "SemanticType": NotRequired[SemanticTypeOutputTypeDef],
        "TimeGranularity": NotRequired[TopicTimeGranularityType],
        "AllowedAggregations": NotRequired[List[AuthorSpecifiedAggregationType]],
        "NotAllowedAggregations": NotRequired[List[AuthorSpecifiedAggregationType]],
        "DefaultFormatting": NotRequired[DefaultFormattingTypeDef],
        "NeverAggregateInFilter": NotRequired[bool],
        "CellValueSynonyms": NotRequired[List[CellValueSynonymOutputTypeDef]],
        "NonAdditive": NotRequired[bool],
    },
)
TopicColumnTypeDef = TypedDict(
    "TopicColumnTypeDef",
    {
        "ColumnName": str,
        "ColumnFriendlyName": NotRequired[str],
        "ColumnDescription": NotRequired[str],
        "ColumnSynonyms": NotRequired[Sequence[str]],
        "ColumnDataRole": NotRequired[ColumnDataRoleType],
        "Aggregation": NotRequired[DefaultAggregationType],
        "IsIncludedInTopic": NotRequired[bool],
        "DisableIndexing": NotRequired[bool],
        "ComparativeOrder": NotRequired[ComparativeOrderUnionTypeDef],
        "SemanticType": NotRequired[SemanticTypeUnionTypeDef],
        "TimeGranularity": NotRequired[TopicTimeGranularityType],
        "AllowedAggregations": NotRequired[Sequence[AuthorSpecifiedAggregationType]],
        "NotAllowedAggregations": NotRequired[Sequence[AuthorSpecifiedAggregationType]],
        "DefaultFormatting": NotRequired[DefaultFormattingTypeDef],
        "NeverAggregateInFilter": NotRequired[bool],
        "CellValueSynonyms": NotRequired[Sequence[CellValueSynonymUnionTypeDef]],
        "NonAdditive": NotRequired[bool],
    },
)
TopicIRMetricUnionTypeDef = Union[TopicIRMetricTypeDef, TopicIRMetricOutputTypeDef]
ContributionAnalysisTimeRangesOutputTypeDef = TypedDict(
    "ContributionAnalysisTimeRangesOutputTypeDef",
    {
        "StartRange": NotRequired[TopicIRFilterOptionOutputTypeDef],
        "EndRange": NotRequired[TopicIRFilterOptionOutputTypeDef],
    },
)
CategoryFilterConfigurationUnionTypeDef = Union[
    CategoryFilterConfigurationTypeDef, CategoryFilterConfigurationOutputTypeDef
]
ChartAxisLabelOptionsOutputTypeDef = TypedDict(
    "ChartAxisLabelOptionsOutputTypeDef",
    {
        "Visibility": NotRequired[VisibilityType],
        "SortIconVisibility": NotRequired[VisibilityType],
        "AxisLabelOptions": NotRequired[List[AxisLabelOptionsTypeDef]],
    },
)
ChartAxisLabelOptionsTypeDef = TypedDict(
    "ChartAxisLabelOptionsTypeDef",
    {
        "Visibility": NotRequired[VisibilityType],
        "SortIconVisibility": NotRequired[VisibilityType],
        "AxisLabelOptions": NotRequired[Sequence[AxisLabelOptionsTypeDef]],
    },
)
DataLabelOptionsUnionTypeDef = Union[DataLabelOptionsTypeDef, DataLabelOptionsOutputTypeDef]
AxisTickLabelOptionsTypeDef = TypedDict(
    "AxisTickLabelOptionsTypeDef",
    {
        "LabelOptions": NotRequired[LabelOptionsTypeDef],
        "RotationAngle": NotRequired[float],
    },
)
DateTimePickerControlDisplayOptionsTypeDef = TypedDict(
    "DateTimePickerControlDisplayOptionsTypeDef",
    {
        "TitleOptions": NotRequired[LabelOptionsTypeDef],
        "DateTimeFormat": NotRequired[str],
        "InfoIconLabelOptions": NotRequired[SheetControlInfoIconLabelOptionsTypeDef],
        "HelperTextVisibility": NotRequired[VisibilityType],
        "DateIconVisibility": NotRequired[VisibilityType],
    },
)
DropDownControlDisplayOptionsTypeDef = TypedDict(
    "DropDownControlDisplayOptionsTypeDef",
    {
        "SelectAllOptions": NotRequired[ListControlSelectAllOptionsTypeDef],
        "TitleOptions": NotRequired[LabelOptionsTypeDef],
        "InfoIconLabelOptions": NotRequired[SheetControlInfoIconLabelOptionsTypeDef],
    },
)
LegendOptionsTypeDef = TypedDict(
    "LegendOptionsTypeDef",
    {
        "Visibility": NotRequired[VisibilityType],
        "Title": NotRequired[LabelOptionsTypeDef],
        "Position": NotRequired[LegendPositionType],
        "Width": NotRequired[str],
        "Height": NotRequired[str],
    },
)
ListControlDisplayOptionsTypeDef = TypedDict(
    "ListControlDisplayOptionsTypeDef",
    {
        "SearchOptions": NotRequired[ListControlSearchOptionsTypeDef],
        "SelectAllOptions": NotRequired[ListControlSelectAllOptionsTypeDef],
        "TitleOptions": NotRequired[LabelOptionsTypeDef],
        "InfoIconLabelOptions": NotRequired[SheetControlInfoIconLabelOptionsTypeDef],
    },
)
RelativeDateTimeControlDisplayOptionsTypeDef = TypedDict(
    "RelativeDateTimeControlDisplayOptionsTypeDef",
    {
        "TitleOptions": NotRequired[LabelOptionsTypeDef],
        "DateTimeFormat": NotRequired[str],
        "InfoIconLabelOptions": NotRequired[SheetControlInfoIconLabelOptionsTypeDef],
    },
)
SliderControlDisplayOptionsTypeDef = TypedDict(
    "SliderControlDisplayOptionsTypeDef",
    {
        "TitleOptions": NotRequired[LabelOptionsTypeDef],
        "InfoIconLabelOptions": NotRequired[SheetControlInfoIconLabelOptionsTypeDef],
    },
)
TextAreaControlDisplayOptionsTypeDef = TypedDict(
    "TextAreaControlDisplayOptionsTypeDef",
    {
        "TitleOptions": NotRequired[LabelOptionsTypeDef],
        "PlaceholderOptions": NotRequired[TextControlPlaceholderOptionsTypeDef],
        "InfoIconLabelOptions": NotRequired[SheetControlInfoIconLabelOptionsTypeDef],
    },
)
TextFieldControlDisplayOptionsTypeDef = TypedDict(
    "TextFieldControlDisplayOptionsTypeDef",
    {
        "TitleOptions": NotRequired[LabelOptionsTypeDef],
        "PlaceholderOptions": NotRequired[TextControlPlaceholderOptionsTypeDef],
        "InfoIconLabelOptions": NotRequired[SheetControlInfoIconLabelOptionsTypeDef],
    },
)
PanelConfigurationTypeDef = TypedDict(
    "PanelConfigurationTypeDef",
    {
        "Title": NotRequired[PanelTitleOptionsTypeDef],
        "BorderVisibility": NotRequired[VisibilityType],
        "BorderThickness": NotRequired[str],
        "BorderStyle": NotRequired[PanelBorderStyleType],
        "BorderColor": NotRequired[str],
        "GutterVisibility": NotRequired[VisibilityType],
        "GutterSpacing": NotRequired[str],
        "BackgroundVisibility": NotRequired[VisibilityType],
        "BackgroundColor": NotRequired[str],
    },
)
TableFieldLinkContentConfigurationTypeDef = TypedDict(
    "TableFieldLinkContentConfigurationTypeDef",
    {
        "CustomTextContent": NotRequired[TableFieldCustomTextContentTypeDef],
        "CustomIconContent": NotRequired[TableFieldCustomIconContentTypeDef],
    },
)
ColumnGroupUnionTypeDef = Union[ColumnGroupTypeDef, ColumnGroupOutputTypeDef]
GeospatialPointStyleOptionsOutputTypeDef = TypedDict(
    "GeospatialPointStyleOptionsOutputTypeDef",
    {
        "SelectedPointStyle": NotRequired[GeospatialSelectedPointStyleType],
        "ClusterMarkerConfiguration": NotRequired[ClusterMarkerConfigurationTypeDef],
        "HeatmapConfiguration": NotRequired[GeospatialHeatmapConfigurationOutputTypeDef],
    },
)
GeospatialHeatmapConfigurationTypeDef = TypedDict(
    "GeospatialHeatmapConfigurationTypeDef",
    {
        "HeatmapColor": NotRequired[GeospatialHeatmapColorScaleUnionTypeDef],
    },
)
TableCellStyleTypeDef = TypedDict(
    "TableCellStyleTypeDef",
    {
        "Visibility": NotRequired[VisibilityType],
        "FontConfiguration": NotRequired[FontConfigurationTypeDef],
        "TextWrap": NotRequired[TextWrapType],
        "HorizontalTextAlignment": NotRequired[HorizontalTextAlignmentType],
        "VerticalTextAlignment": NotRequired[VerticalTextAlignmentType],
        "BackgroundColor": NotRequired[str],
        "Height": NotRequired[int],
        "Border": NotRequired[GlobalTableBorderOptionsTypeDef],
    },
)
ConditionalFormattingColorOutputTypeDef = TypedDict(
    "ConditionalFormattingColorOutputTypeDef",
    {
        "Solid": NotRequired[ConditionalFormattingSolidColorTypeDef],
        "Gradient": NotRequired[ConditionalFormattingGradientColorOutputTypeDef],
    },
)
ConditionalFormattingGradientColorTypeDef = TypedDict(
    "ConditionalFormattingGradientColorTypeDef",
    {
        "Expression": str,
        "Color": GradientColorUnionTypeDef,
    },
)
DefaultInteractiveLayoutConfigurationTypeDef = TypedDict(
    "DefaultInteractiveLayoutConfigurationTypeDef",
    {
        "Grid": NotRequired[DefaultGridLayoutConfigurationTypeDef],
        "FreeForm": NotRequired[DefaultFreeFormLayoutConfigurationTypeDef],
    },
)
SheetControlLayoutConfigurationOutputTypeDef = TypedDict(
    "SheetControlLayoutConfigurationOutputTypeDef",
    {
        "GridLayout": NotRequired[GridLayoutConfigurationOutputTypeDef],
    },
)
GridLayoutConfigurationUnionTypeDef = Union[
    GridLayoutConfigurationTypeDef, GridLayoutConfigurationOutputTypeDef
]
DataSetRefreshPropertiesTypeDef = TypedDict(
    "DataSetRefreshPropertiesTypeDef",
    {
        "RefreshConfiguration": RefreshConfigurationTypeDef,
    },
)
IntegerDatasetParameterUnionTypeDef = Union[
    IntegerDatasetParameterTypeDef, IntegerDatasetParameterOutputTypeDef
]
SeriesItemTypeDef = TypedDict(
    "SeriesItemTypeDef",
    {
        "FieldSeriesItem": NotRequired[FieldSeriesItemTypeDef],
        "DataFieldSeriesItem": NotRequired[DataFieldSeriesItemTypeDef],
    },
)
ThemeConfigurationOutputTypeDef = TypedDict(
    "ThemeConfigurationOutputTypeDef",
    {
        "DataColorPalette": NotRequired[DataColorPaletteOutputTypeDef],
        "UIColorPalette": NotRequired[UIColorPaletteTypeDef],
        "Sheet": NotRequired[SheetStyleTypeDef],
        "Typography": NotRequired[TypographyOutputTypeDef],
    },
)
ThemeConfigurationTypeDef = TypedDict(
    "ThemeConfigurationTypeDef",
    {
        "DataColorPalette": NotRequired[DataColorPaletteUnionTypeDef],
        "UIColorPalette": NotRequired[UIColorPaletteTypeDef],
        "Sheet": NotRequired[SheetStyleTypeDef],
        "Typography": NotRequired[TypographyUnionTypeDef],
    },
)
NamedEntityDefinitionUnionTypeDef = Union[
    NamedEntityDefinitionTypeDef, NamedEntityDefinitionOutputTypeDef
]
ComparisonFormatConfigurationTypeDef = TypedDict(
    "ComparisonFormatConfigurationTypeDef",
    {
        "NumberDisplayFormatConfiguration": NotRequired[NumberDisplayFormatConfigurationTypeDef],
        "PercentageDisplayFormatConfiguration": NotRequired[
            PercentageDisplayFormatConfigurationTypeDef
        ],
    },
)
NumericFormatConfigurationTypeDef = TypedDict(
    "NumericFormatConfigurationTypeDef",
    {
        "NumberDisplayFormatConfiguration": NotRequired[NumberDisplayFormatConfigurationTypeDef],
        "CurrencyDisplayFormatConfiguration": NotRequired[
            CurrencyDisplayFormatConfigurationTypeDef
        ],
        "PercentageDisplayFormatConfiguration": NotRequired[
            PercentageDisplayFormatConfigurationTypeDef
        ],
    },
)
AggregationSortConfigurationTypeDef = TypedDict(
    "AggregationSortConfigurationTypeDef",
    {
        "Column": ColumnIdentifierTypeDef,
        "SortDirection": SortDirectionType,
        "AggregationFunction": NotRequired[AggregationFunctionTypeDef],
    },
)
ColumnSortTypeDef = TypedDict(
    "ColumnSortTypeDef",
    {
        "SortBy": ColumnIdentifierTypeDef,
        "Direction": SortDirectionType,
        "AggregationFunction": NotRequired[AggregationFunctionTypeDef],
    },
)
ColumnTooltipItemTypeDef = TypedDict(
    "ColumnTooltipItemTypeDef",
    {
        "Column": ColumnIdentifierTypeDef,
        "Label": NotRequired[str],
        "Visibility": NotRequired[VisibilityType],
        "Aggregation": NotRequired[AggregationFunctionTypeDef],
        "TooltipTarget": NotRequired[TooltipTargetType],
    },
)
ReferenceLineDynamicDataConfigurationTypeDef = TypedDict(
    "ReferenceLineDynamicDataConfigurationTypeDef",
    {
        "Column": ColumnIdentifierTypeDef,
        "Calculation": NumericalAggregationFunctionTypeDef,
        "MeasureAggregationFunction": NotRequired[AggregationFunctionTypeDef],
    },
)
TopicFilterOutputTypeDef = TypedDict(
    "TopicFilterOutputTypeDef",
    {
        "FilterName": str,
        "OperandFieldName": str,
        "FilterDescription": NotRequired[str],
        "FilterClass": NotRequired[FilterClassType],
        "FilterSynonyms": NotRequired[List[str]],
        "FilterType": NotRequired[NamedFilterTypeType],
        "CategoryFilter": NotRequired[TopicCategoryFilterOutputTypeDef],
        "NumericEqualityFilter": NotRequired[TopicNumericEqualityFilterTypeDef],
        "NumericRangeFilter": NotRequired[TopicNumericRangeFilterTypeDef],
        "DateRangeFilter": NotRequired[TopicDateRangeFilterTypeDef],
        "RelativeDateFilter": NotRequired[TopicRelativeDateFilterTypeDef],
    },
)
AssetBundleImportJobDataSourceOverrideParametersOutputTypeDef = TypedDict(
    "AssetBundleImportJobDataSourceOverrideParametersOutputTypeDef",
    {
        "DataSourceId": str,
        "Name": NotRequired[str],
        "DataSourceParameters": NotRequired[DataSourceParametersOutputTypeDef],
        "VpcConnectionProperties": NotRequired[VpcConnectionPropertiesTypeDef],
        "SslProperties": NotRequired[SslPropertiesTypeDef],
        "Credentials": NotRequired[AssetBundleImportJobDataSourceCredentialsTypeDef],
    },
)
DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "Arn": NotRequired[str],
        "DataSourceId": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[DataSourceTypeType],
        "Status": NotRequired[ResourceStatusType],
        "CreatedTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "DataSourceParameters": NotRequired[DataSourceParametersOutputTypeDef],
        "AlternateDataSourceParameters": NotRequired[List[DataSourceParametersOutputTypeDef]],
        "VpcConnectionProperties": NotRequired[VpcConnectionPropertiesTypeDef],
        "SslProperties": NotRequired[SslPropertiesTypeDef],
        "ErrorInfo": NotRequired[DataSourceErrorInfoTypeDef],
        "SecretArn": NotRequired[str],
    },
)
RedshiftParametersUnionTypeDef = Union[RedshiftParametersTypeDef, RedshiftParametersOutputTypeDef]
DescribeRefreshScheduleResponseTypeDef = TypedDict(
    "DescribeRefreshScheduleResponseTypeDef",
    {
        "RefreshSchedule": RefreshScheduleOutputTypeDef,
        "Status": int,
        "RequestId": str,
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRefreshSchedulesResponseTypeDef = TypedDict(
    "ListRefreshSchedulesResponseTypeDef",
    {
        "RefreshSchedules": List[RefreshScheduleOutputTypeDef],
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRefreshScheduleRequestRequestTypeDef = TypedDict(
    "CreateRefreshScheduleRequestRequestTypeDef",
    {
        "DataSetId": str,
        "AwsAccountId": str,
        "Schedule": RefreshScheduleTypeDef,
    },
)
UpdateRefreshScheduleRequestRequestTypeDef = TypedDict(
    "UpdateRefreshScheduleRequestRequestTypeDef",
    {
        "DataSetId": str,
        "AwsAccountId": str,
        "Schedule": RefreshScheduleTypeDef,
    },
)
RegisteredUserEmbeddingExperienceConfigurationTypeDef = TypedDict(
    "RegisteredUserEmbeddingExperienceConfigurationTypeDef",
    {
        "Dashboard": NotRequired[RegisteredUserDashboardEmbeddingConfigurationTypeDef],
        "QuickSightConsole": NotRequired[
            RegisteredUserQuickSightConsoleEmbeddingConfigurationTypeDef
        ],
        "QSearchBar": NotRequired[RegisteredUserQSearchBarEmbeddingConfigurationTypeDef],
        "DashboardVisual": NotRequired[RegisteredUserDashboardVisualEmbeddingConfigurationTypeDef],
        "GenerativeQnA": NotRequired[RegisteredUserGenerativeQnAEmbeddingConfigurationTypeDef],
    },
)
SnapshotDestinationConfigurationUnionTypeDef = Union[
    SnapshotDestinationConfigurationTypeDef, SnapshotDestinationConfigurationOutputTypeDef
]
SnapshotJobResultFileGroupTypeDef = TypedDict(
    "SnapshotJobResultFileGroupTypeDef",
    {
        "Files": NotRequired[List[SnapshotFileOutputTypeDef]],
        "S3Results": NotRequired[List[SnapshotJobS3ResultTypeDef]],
    },
)
PhysicalTableTypeDef = TypedDict(
    "PhysicalTableTypeDef",
    {
        "RelationalTable": NotRequired[RelationalTableUnionTypeDef],
        "CustomSql": NotRequired[CustomSqlUnionTypeDef],
        "S3Source": NotRequired[S3SourceUnionTypeDef],
    },
)
FilterOperationTargetVisualsConfigurationUnionTypeDef = Union[
    FilterOperationTargetVisualsConfigurationTypeDef,
    FilterOperationTargetVisualsConfigurationOutputTypeDef,
]
DefaultSectionBasedLayoutConfigurationTypeDef = TypedDict(
    "DefaultSectionBasedLayoutConfigurationTypeDef",
    {
        "CanvasSizeOptions": SectionBasedLayoutCanvasSizeOptionsTypeDef,
    },
)
FreeFormLayoutConfigurationOutputTypeDef = TypedDict(
    "FreeFormLayoutConfigurationOutputTypeDef",
    {
        "Elements": List[FreeFormLayoutElementOutputTypeDef],
        "CanvasSizeOptions": NotRequired[FreeFormLayoutCanvasSizeOptionsTypeDef],
    },
)
FreeFormSectionLayoutConfigurationOutputTypeDef = TypedDict(
    "FreeFormSectionLayoutConfigurationOutputTypeDef",
    {
        "Elements": List[FreeFormLayoutElementOutputTypeDef],
    },
)
FreeFormLayoutElementUnionTypeDef = Union[
    FreeFormLayoutElementTypeDef, FreeFormLayoutElementOutputTypeDef
]
SelectedSheetsFilterScopeConfigurationUnionTypeDef = Union[
    SelectedSheetsFilterScopeConfigurationTypeDef,
    SelectedSheetsFilterScopeConfigurationOutputTypeDef,
]
SnapshotConfigurationOutputTypeDef = TypedDict(
    "SnapshotConfigurationOutputTypeDef",
    {
        "FileGroups": List[SnapshotFileGroupOutputTypeDef],
        "DestinationConfiguration": NotRequired[SnapshotDestinationConfigurationOutputTypeDef],
        "Parameters": NotRequired[ParametersOutputTypeDef],
    },
)
SnapshotFileUnionTypeDef = Union[SnapshotFileTypeDef, SnapshotFileOutputTypeDef]
StringDatasetParameterUnionTypeDef = Union[
    StringDatasetParameterTypeDef, StringDatasetParameterOutputTypeDef
]
FilterCrossSheetControlTypeDef = TypedDict(
    "FilterCrossSheetControlTypeDef",
    {
        "FilterControlId": str,
        "SourceFilterId": str,
        "CascadingControlConfiguration": NotRequired[CascadingControlConfigurationUnionTypeDef],
    },
)
DateTimeParameterDeclarationTypeDef = TypedDict(
    "DateTimeParameterDeclarationTypeDef",
    {
        "Name": str,
        "DefaultValues": NotRequired[DateTimeDefaultValuesUnionTypeDef],
        "TimeGranularity": NotRequired[TimeGranularityType],
        "ValueWhenUnset": NotRequired[DateTimeValueWhenUnsetConfigurationUnionTypeDef],
        "MappedDataSetParameters": NotRequired[Sequence[MappedDataSetParameterTypeDef]],
    },
)
DecimalParameterDeclarationTypeDef = TypedDict(
    "DecimalParameterDeclarationTypeDef",
    {
        "ParameterValueType": ParameterValueTypeType,
        "Name": str,
        "DefaultValues": NotRequired[DecimalDefaultValuesUnionTypeDef],
        "ValueWhenUnset": NotRequired[DecimalValueWhenUnsetConfigurationTypeDef],
        "MappedDataSetParameters": NotRequired[Sequence[MappedDataSetParameterTypeDef]],
    },
)
IntegerParameterDeclarationTypeDef = TypedDict(
    "IntegerParameterDeclarationTypeDef",
    {
        "ParameterValueType": ParameterValueTypeType,
        "Name": str,
        "DefaultValues": NotRequired[IntegerDefaultValuesUnionTypeDef],
        "ValueWhenUnset": NotRequired[IntegerValueWhenUnsetConfigurationTypeDef],
        "MappedDataSetParameters": NotRequired[Sequence[MappedDataSetParameterTypeDef]],
    },
)
ParameterDeclarationOutputTypeDef = TypedDict(
    "ParameterDeclarationOutputTypeDef",
    {
        "StringParameterDeclaration": NotRequired[StringParameterDeclarationOutputTypeDef],
        "DecimalParameterDeclaration": NotRequired[DecimalParameterDeclarationOutputTypeDef],
        "IntegerParameterDeclaration": NotRequired[IntegerParameterDeclarationOutputTypeDef],
        "DateTimeParameterDeclaration": NotRequired[DateTimeParameterDeclarationOutputTypeDef],
    },
)
StringParameterDeclarationTypeDef = TypedDict(
    "StringParameterDeclarationTypeDef",
    {
        "ParameterValueType": ParameterValueTypeType,
        "Name": str,
        "DefaultValues": NotRequired[StringDefaultValuesUnionTypeDef],
        "ValueWhenUnset": NotRequired[StringValueWhenUnsetConfigurationTypeDef],
        "MappedDataSetParameters": NotRequired[Sequence[MappedDataSetParameterTypeDef]],
    },
)
ColumnHierarchyOutputTypeDef = TypedDict(
    "ColumnHierarchyOutputTypeDef",
    {
        "ExplicitHierarchy": NotRequired[ExplicitHierarchyOutputTypeDef],
        "DateTimeHierarchy": NotRequired[DateTimeHierarchyOutputTypeDef],
        "PredefinedHierarchy": NotRequired[PredefinedHierarchyOutputTypeDef],
    },
)
DescribeDashboardResponseTypeDef = TypedDict(
    "DescribeDashboardResponseTypeDef",
    {
        "Dashboard": DashboardTypeDef,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GenerateEmbedUrlForAnonymousUserRequestRequestTypeDef = TypedDict(
    "GenerateEmbedUrlForAnonymousUserRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "Namespace": str,
        "AuthorizedResourceArns": Sequence[str],
        "ExperienceConfiguration": AnonymousUserEmbeddingExperienceConfigurationTypeDef,
        "SessionLifetimeInMinutes": NotRequired[int],
        "SessionTags": NotRequired[Sequence[SessionTagTypeDef]],
        "AllowedDomains": NotRequired[Sequence[str]],
    },
)
CustomValuesConfigurationUnionTypeDef = Union[
    CustomValuesConfigurationTypeDef, CustomValuesConfigurationOutputTypeDef
]
DateTimeDatasetParameterUnionTypeDef = Union[
    DateTimeDatasetParameterTypeDef, DateTimeDatasetParameterOutputTypeDef
]
ParametersUnionTypeDef = Union[ParametersTypeDef, ParametersOutputTypeDef]
OverrideDatasetParameterOperationUnionTypeDef = Union[
    OverrideDatasetParameterOperationTypeDef, OverrideDatasetParameterOperationOutputTypeDef
]
DrillDownFilterUnionTypeDef = Union[DrillDownFilterTypeDef, DrillDownFilterOutputTypeDef]
ForecastScenarioUnionTypeDef = Union[ForecastScenarioTypeDef, ForecastScenarioOutputTypeDef]
AssetBundleImportJobDashboardOverridePermissionsTypeDef = TypedDict(
    "AssetBundleImportJobDashboardOverridePermissionsTypeDef",
    {
        "DashboardIds": Sequence[str],
        "Permissions": NotRequired[AssetBundleResourcePermissionsUnionTypeDef],
        "LinkSharingConfiguration": NotRequired[
            AssetBundleResourceLinkSharingConfigurationUnionTypeDef
        ],
    },
)
NumericAxisOptionsUnionTypeDef = Union[NumericAxisOptionsTypeDef, NumericAxisOptionsOutputTypeDef]
TopicIRFilterOptionUnionTypeDef = Union[
    TopicIRFilterOptionTypeDef, TopicIRFilterOptionOutputTypeDef
]
TopicCategoryFilterTypeDef = TypedDict(
    "TopicCategoryFilterTypeDef",
    {
        "CategoryFilterFunction": NotRequired[CategoryFilterFunctionType],
        "CategoryFilterType": NotRequired[CategoryFilterTypeType],
        "Constant": NotRequired[TopicCategoryFilterConstantUnionTypeDef],
        "Inverse": NotRequired[bool],
    },
)
LogicalTableOutputTypeDef = TypedDict(
    "LogicalTableOutputTypeDef",
    {
        "Alias": str,
        "Source": LogicalTableSourceTypeDef,
        "DataTransforms": NotRequired[List[TransformOperationOutputTypeDef]],
    },
)
TemplateTypeDef = TypedDict(
    "TemplateTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Version": NotRequired[TemplateVersionTypeDef],
        "TemplateId": NotRequired[str],
        "LastUpdatedTime": NotRequired[datetime],
        "CreatedTime": NotRequired[datetime],
    },
)
DataSetConfigurationUnionTypeDef = Union[
    DataSetConfigurationTypeDef, DataSetConfigurationOutputTypeDef
]
CustomActionSetParametersOperationOutputTypeDef = TypedDict(
    "CustomActionSetParametersOperationOutputTypeDef",
    {
        "ParameterValueConfigurations": List[SetParameterValueConfigurationOutputTypeDef],
    },
)
VisualPaletteUnionTypeDef = Union[VisualPaletteTypeDef, VisualPaletteOutputTypeDef]
PivotTableFieldOptionsOutputTypeDef = TypedDict(
    "PivotTableFieldOptionsOutputTypeDef",
    {
        "SelectedFieldOptions": NotRequired[List[PivotTableFieldOptionTypeDef]],
        "DataPathOptions": NotRequired[List[PivotTableDataPathOptionOutputTypeDef]],
        "CollapseStateOptions": NotRequired[List[PivotTableFieldCollapseStateOptionOutputTypeDef]],
    },
)
PivotTableFieldCollapseStateOptionTypeDef = TypedDict(
    "PivotTableFieldCollapseStateOptionTypeDef",
    {
        "Target": PivotTableFieldCollapseStateTargetUnionTypeDef,
        "State": NotRequired[PivotTableFieldCollapseStateType],
    },
)
TopicCalculatedFieldUnionTypeDef = Union[
    TopicCalculatedFieldTypeDef, TopicCalculatedFieldOutputTypeDef
]
TopicColumnUnionTypeDef = Union[TopicColumnTypeDef, TopicColumnOutputTypeDef]
TopicIRContributionAnalysisOutputTypeDef = TypedDict(
    "TopicIRContributionAnalysisOutputTypeDef",
    {
        "Factors": NotRequired[List[ContributionAnalysisFactorTypeDef]],
        "TimeRanges": NotRequired[ContributionAnalysisTimeRangesOutputTypeDef],
        "Direction": NotRequired[ContributionAnalysisDirectionType],
        "SortType": NotRequired[ContributionAnalysisSortTypeType],
    },
)
ChartAxisLabelOptionsUnionTypeDef = Union[
    ChartAxisLabelOptionsTypeDef, ChartAxisLabelOptionsOutputTypeDef
]
AxisDisplayOptionsOutputTypeDef = TypedDict(
    "AxisDisplayOptionsOutputTypeDef",
    {
        "TickLabelOptions": NotRequired[AxisTickLabelOptionsTypeDef],
        "AxisLineVisibility": NotRequired[VisibilityType],
        "GridLineVisibility": NotRequired[VisibilityType],
        "DataOptions": NotRequired[AxisDataOptionsOutputTypeDef],
        "ScrollbarOptions": NotRequired[ScrollBarOptionsTypeDef],
        "AxisOffset": NotRequired[str],
    },
)
DefaultDateTimePickerControlOptionsTypeDef = TypedDict(
    "DefaultDateTimePickerControlOptionsTypeDef",
    {
        "Type": NotRequired[SheetControlDateTimePickerTypeType],
        "DisplayOptions": NotRequired[DateTimePickerControlDisplayOptionsTypeDef],
        "CommitMode": NotRequired[CommitModeType],
    },
)
FilterDateTimePickerControlTypeDef = TypedDict(
    "FilterDateTimePickerControlTypeDef",
    {
        "FilterControlId": str,
        "Title": str,
        "SourceFilterId": str,
        "DisplayOptions": NotRequired[DateTimePickerControlDisplayOptionsTypeDef],
        "Type": NotRequired[SheetControlDateTimePickerTypeType],
        "CommitMode": NotRequired[CommitModeType],
    },
)
ParameterDateTimePickerControlTypeDef = TypedDict(
    "ParameterDateTimePickerControlTypeDef",
    {
        "ParameterControlId": str,
        "Title": str,
        "SourceParameterName": str,
        "DisplayOptions": NotRequired[DateTimePickerControlDisplayOptionsTypeDef],
    },
)
DefaultFilterDropDownControlOptionsOutputTypeDef = TypedDict(
    "DefaultFilterDropDownControlOptionsOutputTypeDef",
    {
        "DisplayOptions": NotRequired[DropDownControlDisplayOptionsTypeDef],
        "Type": NotRequired[SheetControlListTypeType],
        "SelectableValues": NotRequired[FilterSelectableValuesOutputTypeDef],
        "CommitMode": NotRequired[CommitModeType],
    },
)
DefaultFilterDropDownControlOptionsTypeDef = TypedDict(
    "DefaultFilterDropDownControlOptionsTypeDef",
    {
        "DisplayOptions": NotRequired[DropDownControlDisplayOptionsTypeDef],
        "Type": NotRequired[SheetControlListTypeType],
        "SelectableValues": NotRequired[FilterSelectableValuesUnionTypeDef],
        "CommitMode": NotRequired[CommitModeType],
    },
)
FilterDropDownControlOutputTypeDef = TypedDict(
    "FilterDropDownControlOutputTypeDef",
    {
        "FilterControlId": str,
        "Title": str,
        "SourceFilterId": str,
        "DisplayOptions": NotRequired[DropDownControlDisplayOptionsTypeDef],
        "Type": NotRequired[SheetControlListTypeType],
        "SelectableValues": NotRequired[FilterSelectableValuesOutputTypeDef],
        "CascadingControlConfiguration": NotRequired[CascadingControlConfigurationOutputTypeDef],
        "CommitMode": NotRequired[CommitModeType],
    },
)
FilterDropDownControlTypeDef = TypedDict(
    "FilterDropDownControlTypeDef",
    {
        "FilterControlId": str,
        "Title": str,
        "SourceFilterId": str,
        "DisplayOptions": NotRequired[DropDownControlDisplayOptionsTypeDef],
        "Type": NotRequired[SheetControlListTypeType],
        "SelectableValues": NotRequired[FilterSelectableValuesUnionTypeDef],
        "CascadingControlConfiguration": NotRequired[CascadingControlConfigurationUnionTypeDef],
        "CommitMode": NotRequired[CommitModeType],
    },
)
ParameterDropDownControlOutputTypeDef = TypedDict(
    "ParameterDropDownControlOutputTypeDef",
    {
        "ParameterControlId": str,
        "Title": str,
        "SourceParameterName": str,
        "DisplayOptions": NotRequired[DropDownControlDisplayOptionsTypeDef],
        "Type": NotRequired[SheetControlListTypeType],
        "SelectableValues": NotRequired[ParameterSelectableValuesOutputTypeDef],
        "CascadingControlConfiguration": NotRequired[CascadingControlConfigurationOutputTypeDef],
        "CommitMode": NotRequired[CommitModeType],
    },
)
ParameterDropDownControlTypeDef = TypedDict(
    "ParameterDropDownControlTypeDef",
    {
        "ParameterControlId": str,
        "Title": str,
        "SourceParameterName": str,
        "DisplayOptions": NotRequired[DropDownControlDisplayOptionsTypeDef],
        "Type": NotRequired[SheetControlListTypeType],
        "SelectableValues": NotRequired[ParameterSelectableValuesUnionTypeDef],
        "CascadingControlConfiguration": NotRequired[CascadingControlConfigurationUnionTypeDef],
        "CommitMode": NotRequired[CommitModeType],
    },
)
DefaultFilterListControlOptionsOutputTypeDef = TypedDict(
    "DefaultFilterListControlOptionsOutputTypeDef",
    {
        "DisplayOptions": NotRequired[ListControlDisplayOptionsTypeDef],
        "Type": NotRequired[SheetControlListTypeType],
        "SelectableValues": NotRequired[FilterSelectableValuesOutputTypeDef],
    },
)
DefaultFilterListControlOptionsTypeDef = TypedDict(
    "DefaultFilterListControlOptionsTypeDef",
    {
        "DisplayOptions": NotRequired[ListControlDisplayOptionsTypeDef],
        "Type": NotRequired[SheetControlListTypeType],
        "SelectableValues": NotRequired[FilterSelectableValuesUnionTypeDef],
    },
)
FilterListControlOutputTypeDef = TypedDict(
    "FilterListControlOutputTypeDef",
    {
        "FilterControlId": str,
        "Title": str,
        "SourceFilterId": str,
        "DisplayOptions": NotRequired[ListControlDisplayOptionsTypeDef],
        "Type": NotRequired[SheetControlListTypeType],
        "SelectableValues": NotRequired[FilterSelectableValuesOutputTypeDef],
        "CascadingControlConfiguration": NotRequired[CascadingControlConfigurationOutputTypeDef],
    },
)
FilterListControlTypeDef = TypedDict(
    "FilterListControlTypeDef",
    {
        "FilterControlId": str,
        "Title": str,
        "SourceFilterId": str,
        "DisplayOptions": NotRequired[ListControlDisplayOptionsTypeDef],
        "Type": NotRequired[SheetControlListTypeType],
        "SelectableValues": NotRequired[FilterSelectableValuesUnionTypeDef],
        "CascadingControlConfiguration": NotRequired[CascadingControlConfigurationUnionTypeDef],
    },
)
ParameterListControlOutputTypeDef = TypedDict(
    "ParameterListControlOutputTypeDef",
    {
        "ParameterControlId": str,
        "Title": str,
        "SourceParameterName": str,
        "DisplayOptions": NotRequired[ListControlDisplayOptionsTypeDef],
        "Type": NotRequired[SheetControlListTypeType],
        "SelectableValues": NotRequired[ParameterSelectableValuesOutputTypeDef],
        "CascadingControlConfiguration": NotRequired[CascadingControlConfigurationOutputTypeDef],
    },
)
ParameterListControlTypeDef = TypedDict(
    "ParameterListControlTypeDef",
    {
        "ParameterControlId": str,
        "Title": str,
        "SourceParameterName": str,
        "DisplayOptions": NotRequired[ListControlDisplayOptionsTypeDef],
        "Type": NotRequired[SheetControlListTypeType],
        "SelectableValues": NotRequired[ParameterSelectableValuesUnionTypeDef],
        "CascadingControlConfiguration": NotRequired[CascadingControlConfigurationUnionTypeDef],
    },
)
DefaultRelativeDateTimeControlOptionsTypeDef = TypedDict(
    "DefaultRelativeDateTimeControlOptionsTypeDef",
    {
        "DisplayOptions": NotRequired[RelativeDateTimeControlDisplayOptionsTypeDef],
        "CommitMode": NotRequired[CommitModeType],
    },
)
FilterRelativeDateTimeControlTypeDef = TypedDict(
    "FilterRelativeDateTimeControlTypeDef",
    {
        "FilterControlId": str,
        "Title": str,
        "SourceFilterId": str,
        "DisplayOptions": NotRequired[RelativeDateTimeControlDisplayOptionsTypeDef],
        "CommitMode": NotRequired[CommitModeType],
    },
)
DefaultSliderControlOptionsTypeDef = TypedDict(
    "DefaultSliderControlOptionsTypeDef",
    {
        "MaximumValue": float,
        "MinimumValue": float,
        "StepSize": float,
        "DisplayOptions": NotRequired[SliderControlDisplayOptionsTypeDef],
        "Type": NotRequired[SheetControlSliderTypeType],
    },
)
FilterSliderControlTypeDef = TypedDict(
    "FilterSliderControlTypeDef",
    {
        "FilterControlId": str,
        "Title": str,
        "SourceFilterId": str,
        "MaximumValue": float,
        "MinimumValue": float,
        "StepSize": float,
        "DisplayOptions": NotRequired[SliderControlDisplayOptionsTypeDef],
        "Type": NotRequired[SheetControlSliderTypeType],
    },
)
ParameterSliderControlTypeDef = TypedDict(
    "ParameterSliderControlTypeDef",
    {
        "ParameterControlId": str,
        "Title": str,
        "SourceParameterName": str,
        "MaximumValue": float,
        "MinimumValue": float,
        "StepSize": float,
        "DisplayOptions": NotRequired[SliderControlDisplayOptionsTypeDef],
    },
)
DefaultTextAreaControlOptionsTypeDef = TypedDict(
    "DefaultTextAreaControlOptionsTypeDef",
    {
        "Delimiter": NotRequired[str],
        "DisplayOptions": NotRequired[TextAreaControlDisplayOptionsTypeDef],
    },
)
FilterTextAreaControlTypeDef = TypedDict(
    "FilterTextAreaControlTypeDef",
    {
        "FilterControlId": str,
        "Title": str,
        "SourceFilterId": str,
        "Delimiter": NotRequired[str],
        "DisplayOptions": NotRequired[TextAreaControlDisplayOptionsTypeDef],
    },
)
ParameterTextAreaControlTypeDef = TypedDict(
    "ParameterTextAreaControlTypeDef",
    {
        "ParameterControlId": str,
        "Title": str,
        "SourceParameterName": str,
        "Delimiter": NotRequired[str],
        "DisplayOptions": NotRequired[TextAreaControlDisplayOptionsTypeDef],
    },
)
DefaultTextFieldControlOptionsTypeDef = TypedDict(
    "DefaultTextFieldControlOptionsTypeDef",
    {
        "DisplayOptions": NotRequired[TextFieldControlDisplayOptionsTypeDef],
    },
)
FilterTextFieldControlTypeDef = TypedDict(
    "FilterTextFieldControlTypeDef",
    {
        "FilterControlId": str,
        "Title": str,
        "SourceFilterId": str,
        "DisplayOptions": NotRequired[TextFieldControlDisplayOptionsTypeDef],
    },
)
ParameterTextFieldControlTypeDef = TypedDict(
    "ParameterTextFieldControlTypeDef",
    {
        "ParameterControlId": str,
        "Title": str,
        "SourceParameterName": str,
        "DisplayOptions": NotRequired[TextFieldControlDisplayOptionsTypeDef],
    },
)
SmallMultiplesOptionsTypeDef = TypedDict(
    "SmallMultiplesOptionsTypeDef",
    {
        "MaxVisibleRows": NotRequired[int],
        "MaxVisibleColumns": NotRequired[int],
        "PanelConfiguration": NotRequired[PanelConfigurationTypeDef],
        "XAxis": NotRequired[SmallMultiplesAxisPropertiesTypeDef],
        "YAxis": NotRequired[SmallMultiplesAxisPropertiesTypeDef],
    },
)
TableFieldLinkConfigurationTypeDef = TypedDict(
    "TableFieldLinkConfigurationTypeDef",
    {
        "Target": URLTargetConfigurationType,
        "Content": TableFieldLinkContentConfigurationTypeDef,
    },
)
GeospatialHeatmapConfigurationUnionTypeDef = Union[
    GeospatialHeatmapConfigurationTypeDef, GeospatialHeatmapConfigurationOutputTypeDef
]
PivotTableOptionsOutputTypeDef = TypedDict(
    "PivotTableOptionsOutputTypeDef",
    {
        "MetricPlacement": NotRequired[PivotTableMetricPlacementType],
        "SingleMetricVisibility": NotRequired[VisibilityType],
        "ColumnNamesVisibility": NotRequired[VisibilityType],
        "ToggleButtonsVisibility": NotRequired[VisibilityType],
        "ColumnHeaderStyle": NotRequired[TableCellStyleTypeDef],
        "RowHeaderStyle": NotRequired[TableCellStyleTypeDef],
        "CellStyle": NotRequired[TableCellStyleTypeDef],
        "RowFieldNamesStyle": NotRequired[TableCellStyleTypeDef],
        "RowAlternateColorOptions": NotRequired[RowAlternateColorOptionsOutputTypeDef],
        "CollapsedRowDimensionsVisibility": NotRequired[VisibilityType],
        "RowsLayout": NotRequired[PivotTableRowsLayoutType],
        "RowsLabelOptions": NotRequired[PivotTableRowsLabelOptionsTypeDef],
        "DefaultCellWidth": NotRequired[str],
    },
)
PivotTableOptionsTypeDef = TypedDict(
    "PivotTableOptionsTypeDef",
    {
        "MetricPlacement": NotRequired[PivotTableMetricPlacementType],
        "SingleMetricVisibility": NotRequired[VisibilityType],
        "ColumnNamesVisibility": NotRequired[VisibilityType],
        "ToggleButtonsVisibility": NotRequired[VisibilityType],
        "ColumnHeaderStyle": NotRequired[TableCellStyleTypeDef],
        "RowHeaderStyle": NotRequired[TableCellStyleTypeDef],
        "CellStyle": NotRequired[TableCellStyleTypeDef],
        "RowFieldNamesStyle": NotRequired[TableCellStyleTypeDef],
        "RowAlternateColorOptions": NotRequired[RowAlternateColorOptionsUnionTypeDef],
        "CollapsedRowDimensionsVisibility": NotRequired[VisibilityType],
        "RowsLayout": NotRequired[PivotTableRowsLayoutType],
        "RowsLabelOptions": NotRequired[PivotTableRowsLabelOptionsTypeDef],
        "DefaultCellWidth": NotRequired[str],
    },
)
PivotTotalOptionsOutputTypeDef = TypedDict(
    "PivotTotalOptionsOutputTypeDef",
    {
        "TotalsVisibility": NotRequired[VisibilityType],
        "Placement": NotRequired[TableTotalsPlacementType],
        "ScrollStatus": NotRequired[TableTotalsScrollStatusType],
        "CustomLabel": NotRequired[str],
        "TotalCellStyle": NotRequired[TableCellStyleTypeDef],
        "ValueCellStyle": NotRequired[TableCellStyleTypeDef],
        "MetricHeaderCellStyle": NotRequired[TableCellStyleTypeDef],
        "TotalAggregationOptions": NotRequired[List[TotalAggregationOptionTypeDef]],
    },
)
PivotTotalOptionsTypeDef = TypedDict(
    "PivotTotalOptionsTypeDef",
    {
        "TotalsVisibility": NotRequired[VisibilityType],
        "Placement": NotRequired[TableTotalsPlacementType],
        "ScrollStatus": NotRequired[TableTotalsScrollStatusType],
        "CustomLabel": NotRequired[str],
        "TotalCellStyle": NotRequired[TableCellStyleTypeDef],
        "ValueCellStyle": NotRequired[TableCellStyleTypeDef],
        "MetricHeaderCellStyle": NotRequired[TableCellStyleTypeDef],
        "TotalAggregationOptions": NotRequired[Sequence[TotalAggregationOptionTypeDef]],
    },
)
SubtotalOptionsOutputTypeDef = TypedDict(
    "SubtotalOptionsOutputTypeDef",
    {
        "TotalsVisibility": NotRequired[VisibilityType],
        "CustomLabel": NotRequired[str],
        "FieldLevel": NotRequired[PivotTableSubtotalLevelType],
        "FieldLevelOptions": NotRequired[List[PivotTableFieldSubtotalOptionsTypeDef]],
        "TotalCellStyle": NotRequired[TableCellStyleTypeDef],
        "ValueCellStyle": NotRequired[TableCellStyleTypeDef],
        "MetricHeaderCellStyle": NotRequired[TableCellStyleTypeDef],
        "StyleTargets": NotRequired[List[TableStyleTargetTypeDef]],
    },
)
SubtotalOptionsTypeDef = TypedDict(
    "SubtotalOptionsTypeDef",
    {
        "TotalsVisibility": NotRequired[VisibilityType],
        "CustomLabel": NotRequired[str],
        "FieldLevel": NotRequired[PivotTableSubtotalLevelType],
        "FieldLevelOptions": NotRequired[Sequence[PivotTableFieldSubtotalOptionsTypeDef]],
        "TotalCellStyle": NotRequired[TableCellStyleTypeDef],
        "ValueCellStyle": NotRequired[TableCellStyleTypeDef],
        "MetricHeaderCellStyle": NotRequired[TableCellStyleTypeDef],
        "StyleTargets": NotRequired[Sequence[TableStyleTargetTypeDef]],
    },
)
TableOptionsOutputTypeDef = TypedDict(
    "TableOptionsOutputTypeDef",
    {
        "Orientation": NotRequired[TableOrientationType],
        "HeaderStyle": NotRequired[TableCellStyleTypeDef],
        "CellStyle": NotRequired[TableCellStyleTypeDef],
        "RowAlternateColorOptions": NotRequired[RowAlternateColorOptionsOutputTypeDef],
    },
)
TableOptionsTypeDef = TypedDict(
    "TableOptionsTypeDef",
    {
        "Orientation": NotRequired[TableOrientationType],
        "HeaderStyle": NotRequired[TableCellStyleTypeDef],
        "CellStyle": NotRequired[TableCellStyleTypeDef],
        "RowAlternateColorOptions": NotRequired[RowAlternateColorOptionsUnionTypeDef],
    },
)
TotalOptionsOutputTypeDef = TypedDict(
    "TotalOptionsOutputTypeDef",
    {
        "TotalsVisibility": NotRequired[VisibilityType],
        "Placement": NotRequired[TableTotalsPlacementType],
        "ScrollStatus": NotRequired[TableTotalsScrollStatusType],
        "CustomLabel": NotRequired[str],
        "TotalCellStyle": NotRequired[TableCellStyleTypeDef],
        "TotalAggregationOptions": NotRequired[List[TotalAggregationOptionTypeDef]],
    },
)
TotalOptionsTypeDef = TypedDict(
    "TotalOptionsTypeDef",
    {
        "TotalsVisibility": NotRequired[VisibilityType],
        "Placement": NotRequired[TableTotalsPlacementType],
        "ScrollStatus": NotRequired[TableTotalsScrollStatusType],
        "CustomLabel": NotRequired[str],
        "TotalCellStyle": NotRequired[TableCellStyleTypeDef],
        "TotalAggregationOptions": NotRequired[Sequence[TotalAggregationOptionTypeDef]],
    },
)
GaugeChartArcConditionalFormattingOutputTypeDef = TypedDict(
    "GaugeChartArcConditionalFormattingOutputTypeDef",
    {
        "ForegroundColor": NotRequired[ConditionalFormattingColorOutputTypeDef],
    },
)
GaugeChartPrimaryValueConditionalFormattingOutputTypeDef = TypedDict(
    "GaugeChartPrimaryValueConditionalFormattingOutputTypeDef",
    {
        "TextColor": NotRequired[ConditionalFormattingColorOutputTypeDef],
        "Icon": NotRequired[ConditionalFormattingIconTypeDef],
    },
)
KPIActualValueConditionalFormattingOutputTypeDef = TypedDict(
    "KPIActualValueConditionalFormattingOutputTypeDef",
    {
        "TextColor": NotRequired[ConditionalFormattingColorOutputTypeDef],
        "Icon": NotRequired[ConditionalFormattingIconTypeDef],
    },
)
KPIComparisonValueConditionalFormattingOutputTypeDef = TypedDict(
    "KPIComparisonValueConditionalFormattingOutputTypeDef",
    {
        "TextColor": NotRequired[ConditionalFormattingColorOutputTypeDef],
        "Icon": NotRequired[ConditionalFormattingIconTypeDef],
    },
)
KPIPrimaryValueConditionalFormattingOutputTypeDef = TypedDict(
    "KPIPrimaryValueConditionalFormattingOutputTypeDef",
    {
        "TextColor": NotRequired[ConditionalFormattingColorOutputTypeDef],
        "Icon": NotRequired[ConditionalFormattingIconTypeDef],
    },
)
KPIProgressBarConditionalFormattingOutputTypeDef = TypedDict(
    "KPIProgressBarConditionalFormattingOutputTypeDef",
    {
        "ForegroundColor": NotRequired[ConditionalFormattingColorOutputTypeDef],
    },
)
ShapeConditionalFormatOutputTypeDef = TypedDict(
    "ShapeConditionalFormatOutputTypeDef",
    {
        "BackgroundColor": ConditionalFormattingColorOutputTypeDef,
    },
)
TableRowConditionalFormattingOutputTypeDef = TypedDict(
    "TableRowConditionalFormattingOutputTypeDef",
    {
        "BackgroundColor": NotRequired[ConditionalFormattingColorOutputTypeDef],
        "TextColor": NotRequired[ConditionalFormattingColorOutputTypeDef],
    },
)
TextConditionalFormatOutputTypeDef = TypedDict(
    "TextConditionalFormatOutputTypeDef",
    {
        "BackgroundColor": NotRequired[ConditionalFormattingColorOutputTypeDef],
        "TextColor": NotRequired[ConditionalFormattingColorOutputTypeDef],
        "Icon": NotRequired[ConditionalFormattingIconTypeDef],
    },
)
ConditionalFormattingGradientColorUnionTypeDef = Union[
    ConditionalFormattingGradientColorTypeDef, ConditionalFormattingGradientColorOutputTypeDef
]
SheetControlLayoutOutputTypeDef = TypedDict(
    "SheetControlLayoutOutputTypeDef",
    {
        "Configuration": SheetControlLayoutConfigurationOutputTypeDef,
    },
)
SheetControlLayoutConfigurationTypeDef = TypedDict(
    "SheetControlLayoutConfigurationTypeDef",
    {
        "GridLayout": NotRequired[GridLayoutConfigurationUnionTypeDef],
    },
)
DescribeDataSetRefreshPropertiesResponseTypeDef = TypedDict(
    "DescribeDataSetRefreshPropertiesResponseTypeDef",
    {
        "RequestId": str,
        "Status": int,
        "DataSetRefreshProperties": DataSetRefreshPropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutDataSetRefreshPropertiesRequestRequestTypeDef = TypedDict(
    "PutDataSetRefreshPropertiesRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
        "DataSetRefreshProperties": DataSetRefreshPropertiesTypeDef,
    },
)
ThemeVersionTypeDef = TypedDict(
    "ThemeVersionTypeDef",
    {
        "VersionNumber": NotRequired[int],
        "Arn": NotRequired[str],
        "Description": NotRequired[str],
        "BaseThemeId": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "Configuration": NotRequired[ThemeConfigurationOutputTypeDef],
        "Errors": NotRequired[List[ThemeErrorTypeDef]],
        "Status": NotRequired[ResourceStatusType],
    },
)
CreateThemeRequestRequestTypeDef = TypedDict(
    "CreateThemeRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "Name": str,
        "BaseThemeId": str,
        "Configuration": ThemeConfigurationTypeDef,
        "VersionDescription": NotRequired[str],
        "Permissions": NotRequired[Sequence[ResourcePermissionTypeDef]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
UpdateThemeRequestRequestTypeDef = TypedDict(
    "UpdateThemeRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "ThemeId": str,
        "BaseThemeId": str,
        "Name": NotRequired[str],
        "VersionDescription": NotRequired[str],
        "Configuration": NotRequired[ThemeConfigurationTypeDef],
    },
)
TopicNamedEntityTypeDef = TypedDict(
    "TopicNamedEntityTypeDef",
    {
        "EntityName": str,
        "EntityDescription": NotRequired[str],
        "EntitySynonyms": NotRequired[Sequence[str]],
        "SemanticEntityType": NotRequired[SemanticEntityTypeUnionTypeDef],
        "Definition": NotRequired[Sequence[NamedEntityDefinitionUnionTypeDef]],
    },
)
ComparisonConfigurationTypeDef = TypedDict(
    "ComparisonConfigurationTypeDef",
    {
        "ComparisonMethod": NotRequired[ComparisonMethodType],
        "ComparisonFormat": NotRequired[ComparisonFormatConfigurationTypeDef],
    },
)
DateTimeFormatConfigurationTypeDef = TypedDict(
    "DateTimeFormatConfigurationTypeDef",
    {
        "DateTimeFormat": NotRequired[str],
        "NullValueFormatConfiguration": NotRequired[NullValueFormatConfigurationTypeDef],
        "NumericFormatConfiguration": NotRequired[NumericFormatConfigurationTypeDef],
    },
)
NumberFormatConfigurationTypeDef = TypedDict(
    "NumberFormatConfigurationTypeDef",
    {
        "FormatConfiguration": NotRequired[NumericFormatConfigurationTypeDef],
    },
)
ReferenceLineValueLabelConfigurationTypeDef = TypedDict(
    "ReferenceLineValueLabelConfigurationTypeDef",
    {
        "RelativePosition": NotRequired[ReferenceLineValueLabelRelativePositionType],
        "FormatConfiguration": NotRequired[NumericFormatConfigurationTypeDef],
    },
)
StringFormatConfigurationTypeDef = TypedDict(
    "StringFormatConfigurationTypeDef",
    {
        "NullValueFormatConfiguration": NotRequired[NullValueFormatConfigurationTypeDef],
        "NumericFormatConfiguration": NotRequired[NumericFormatConfigurationTypeDef],
    },
)
BodySectionDynamicCategoryDimensionConfigurationOutputTypeDef = TypedDict(
    "BodySectionDynamicCategoryDimensionConfigurationOutputTypeDef",
    {
        "Column": ColumnIdentifierTypeDef,
        "Limit": NotRequired[int],
        "SortByMetrics": NotRequired[List[ColumnSortTypeDef]],
    },
)
BodySectionDynamicCategoryDimensionConfigurationTypeDef = TypedDict(
    "BodySectionDynamicCategoryDimensionConfigurationTypeDef",
    {
        "Column": ColumnIdentifierTypeDef,
        "Limit": NotRequired[int],
        "SortByMetrics": NotRequired[Sequence[ColumnSortTypeDef]],
    },
)
BodySectionDynamicNumericDimensionConfigurationOutputTypeDef = TypedDict(
    "BodySectionDynamicNumericDimensionConfigurationOutputTypeDef",
    {
        "Column": ColumnIdentifierTypeDef,
        "Limit": NotRequired[int],
        "SortByMetrics": NotRequired[List[ColumnSortTypeDef]],
    },
)
BodySectionDynamicNumericDimensionConfigurationTypeDef = TypedDict(
    "BodySectionDynamicNumericDimensionConfigurationTypeDef",
    {
        "Column": ColumnIdentifierTypeDef,
        "Limit": NotRequired[int],
        "SortByMetrics": NotRequired[Sequence[ColumnSortTypeDef]],
    },
)
FieldSortOptionsTypeDef = TypedDict(
    "FieldSortOptionsTypeDef",
    {
        "FieldSort": NotRequired[FieldSortTypeDef],
        "ColumnSort": NotRequired[ColumnSortTypeDef],
    },
)
PivotTableSortByOutputTypeDef = TypedDict(
    "PivotTableSortByOutputTypeDef",
    {
        "Field": NotRequired[FieldSortTypeDef],
        "Column": NotRequired[ColumnSortTypeDef],
        "DataPath": NotRequired[DataPathSortOutputTypeDef],
    },
)
PivotTableSortByTypeDef = TypedDict(
    "PivotTableSortByTypeDef",
    {
        "Field": NotRequired[FieldSortTypeDef],
        "Column": NotRequired[ColumnSortTypeDef],
        "DataPath": NotRequired[DataPathSortUnionTypeDef],
    },
)
TooltipItemTypeDef = TypedDict(
    "TooltipItemTypeDef",
    {
        "FieldTooltipItem": NotRequired[FieldTooltipItemTypeDef],
        "ColumnTooltipItem": NotRequired[ColumnTooltipItemTypeDef],
    },
)
ReferenceLineDataConfigurationTypeDef = TypedDict(
    "ReferenceLineDataConfigurationTypeDef",
    {
        "StaticConfiguration": NotRequired[ReferenceLineStaticDataConfigurationTypeDef],
        "DynamicConfiguration": NotRequired[ReferenceLineDynamicDataConfigurationTypeDef],
        "AxisBinding": NotRequired[AxisBindingType],
        "SeriesType": NotRequired[ReferenceLineSeriesTypeType],
    },
)
DatasetMetadataOutputTypeDef = TypedDict(
    "DatasetMetadataOutputTypeDef",
    {
        "DatasetArn": str,
        "DatasetName": NotRequired[str],
        "DatasetDescription": NotRequired[str],
        "DataAggregation": NotRequired[DataAggregationTypeDef],
        "Filters": NotRequired[List[TopicFilterOutputTypeDef]],
        "Columns": NotRequired[List[TopicColumnOutputTypeDef]],
        "CalculatedFields": NotRequired[List[TopicCalculatedFieldOutputTypeDef]],
        "NamedEntities": NotRequired[List[TopicNamedEntityOutputTypeDef]],
    },
)
AssetBundleImportJobOverrideParametersOutputTypeDef = TypedDict(
    "AssetBundleImportJobOverrideParametersOutputTypeDef",
    {
        "ResourceIdOverrideConfiguration": NotRequired[
            AssetBundleImportJobResourceIdOverrideConfigurationTypeDef
        ],
        "VPCConnections": NotRequired[
            List[AssetBundleImportJobVPCConnectionOverrideParametersOutputTypeDef]
        ],
        "RefreshSchedules": NotRequired[
            List[AssetBundleImportJobRefreshScheduleOverrideParametersOutputTypeDef]
        ],
        "DataSources": NotRequired[
            List[AssetBundleImportJobDataSourceOverrideParametersOutputTypeDef]
        ],
        "DataSets": NotRequired[List[AssetBundleImportJobDataSetOverrideParametersTypeDef]],
        "Themes": NotRequired[List[AssetBundleImportJobThemeOverrideParametersTypeDef]],
        "Analyses": NotRequired[List[AssetBundleImportJobAnalysisOverrideParametersTypeDef]],
        "Dashboards": NotRequired[List[AssetBundleImportJobDashboardOverrideParametersTypeDef]],
        "Folders": NotRequired[List[AssetBundleImportJobFolderOverrideParametersTypeDef]],
    },
)
DescribeDataSourceResponseTypeDef = TypedDict(
    "DescribeDataSourceResponseTypeDef",
    {
        "DataSource": DataSourceTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDataSourcesResponseTypeDef = TypedDict(
    "ListDataSourcesResponseTypeDef",
    {
        "DataSources": List[DataSourceTypeDef],
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DataSourceParametersTypeDef = TypedDict(
    "DataSourceParametersTypeDef",
    {
        "AmazonElasticsearchParameters": NotRequired[AmazonElasticsearchParametersTypeDef],
        "AthenaParameters": NotRequired[AthenaParametersTypeDef],
        "AuroraParameters": NotRequired[AuroraParametersTypeDef],
        "AuroraPostgreSqlParameters": NotRequired[AuroraPostgreSqlParametersTypeDef],
        "AwsIotAnalyticsParameters": NotRequired[AwsIotAnalyticsParametersTypeDef],
        "JiraParameters": NotRequired[JiraParametersTypeDef],
        "MariaDbParameters": NotRequired[MariaDbParametersTypeDef],
        "MySqlParameters": NotRequired[MySqlParametersTypeDef],
        "OracleParameters": NotRequired[OracleParametersTypeDef],
        "PostgreSqlParameters": NotRequired[PostgreSqlParametersTypeDef],
        "PrestoParameters": NotRequired[PrestoParametersTypeDef],
        "RdsParameters": NotRequired[RdsParametersTypeDef],
        "RedshiftParameters": NotRequired[RedshiftParametersUnionTypeDef],
        "S3Parameters": NotRequired[S3ParametersTypeDef],
        "ServiceNowParameters": NotRequired[ServiceNowParametersTypeDef],
        "SnowflakeParameters": NotRequired[SnowflakeParametersTypeDef],
        "SparkParameters": NotRequired[SparkParametersTypeDef],
        "SqlServerParameters": NotRequired[SqlServerParametersTypeDef],
        "TeradataParameters": NotRequired[TeradataParametersTypeDef],
        "TwitterParameters": NotRequired[TwitterParametersTypeDef],
        "AmazonOpenSearchParameters": NotRequired[AmazonOpenSearchParametersTypeDef],
        "ExasolParameters": NotRequired[ExasolParametersTypeDef],
        "DatabricksParameters": NotRequired[DatabricksParametersTypeDef],
        "StarburstParameters": NotRequired[StarburstParametersTypeDef],
        "TrinoParameters": NotRequired[TrinoParametersTypeDef],
        "BigQueryParameters": NotRequired[BigQueryParametersTypeDef],
    },
)
GenerateEmbedUrlForRegisteredUserRequestRequestTypeDef = TypedDict(
    "GenerateEmbedUrlForRegisteredUserRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "UserArn": str,
        "ExperienceConfiguration": RegisteredUserEmbeddingExperienceConfigurationTypeDef,
        "SessionLifetimeInMinutes": NotRequired[int],
        "AllowedDomains": NotRequired[Sequence[str]],
    },
)
AnonymousUserSnapshotJobResultTypeDef = TypedDict(
    "AnonymousUserSnapshotJobResultTypeDef",
    {
        "FileGroups": NotRequired[List[SnapshotJobResultFileGroupTypeDef]],
    },
)
PhysicalTableUnionTypeDef = Union[PhysicalTableTypeDef, PhysicalTableOutputTypeDef]
CustomActionFilterOperationTypeDef = TypedDict(
    "CustomActionFilterOperationTypeDef",
    {
        "SelectedFieldsConfiguration": FilterOperationSelectedFieldsConfigurationUnionTypeDef,
        "TargetVisualsConfiguration": FilterOperationTargetVisualsConfigurationUnionTypeDef,
    },
)
DefaultPaginatedLayoutConfigurationTypeDef = TypedDict(
    "DefaultPaginatedLayoutConfigurationTypeDef",
    {
        "SectionBased": NotRequired[DefaultSectionBasedLayoutConfigurationTypeDef],
    },
)
SectionLayoutConfigurationOutputTypeDef = TypedDict(
    "SectionLayoutConfigurationOutputTypeDef",
    {
        "FreeFormLayout": FreeFormSectionLayoutConfigurationOutputTypeDef,
    },
)
FreeFormLayoutConfigurationTypeDef = TypedDict(
    "FreeFormLayoutConfigurationTypeDef",
    {
        "Elements": Sequence[FreeFormLayoutElementUnionTypeDef],
        "CanvasSizeOptions": NotRequired[FreeFormLayoutCanvasSizeOptionsTypeDef],
    },
)
FreeFormSectionLayoutConfigurationTypeDef = TypedDict(
    "FreeFormSectionLayoutConfigurationTypeDef",
    {
        "Elements": Sequence[FreeFormLayoutElementUnionTypeDef],
    },
)
FilterScopeConfigurationTypeDef = TypedDict(
    "FilterScopeConfigurationTypeDef",
    {
        "SelectedSheets": NotRequired[SelectedSheetsFilterScopeConfigurationUnionTypeDef],
        "AllSheets": NotRequired[Mapping[str, Any]],
    },
)
DescribeDashboardSnapshotJobResponseTypeDef = TypedDict(
    "DescribeDashboardSnapshotJobResponseTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "SnapshotJobId": str,
        "UserConfiguration": SnapshotUserConfigurationRedactedTypeDef,
        "SnapshotConfiguration": SnapshotConfigurationOutputTypeDef,
        "Arn": str,
        "JobStatus": SnapshotJobStatusType,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SnapshotFileGroupTypeDef = TypedDict(
    "SnapshotFileGroupTypeDef",
    {
        "Files": NotRequired[Sequence[SnapshotFileUnionTypeDef]],
    },
)
FilterCrossSheetControlUnionTypeDef = Union[
    FilterCrossSheetControlTypeDef, FilterCrossSheetControlOutputTypeDef
]
DateTimeParameterDeclarationUnionTypeDef = Union[
    DateTimeParameterDeclarationTypeDef, DateTimeParameterDeclarationOutputTypeDef
]
DecimalParameterDeclarationUnionTypeDef = Union[
    DecimalParameterDeclarationTypeDef, DecimalParameterDeclarationOutputTypeDef
]
IntegerParameterDeclarationUnionTypeDef = Union[
    IntegerParameterDeclarationTypeDef, IntegerParameterDeclarationOutputTypeDef
]
StringParameterDeclarationUnionTypeDef = Union[
    StringParameterDeclarationTypeDef, StringParameterDeclarationOutputTypeDef
]
DestinationParameterValueConfigurationTypeDef = TypedDict(
    "DestinationParameterValueConfigurationTypeDef",
    {
        "CustomValuesConfiguration": NotRequired[CustomValuesConfigurationUnionTypeDef],
        "SelectAllValueOptions": NotRequired[Literal["ALL_VALUES"]],
        "SourceParameterName": NotRequired[str],
        "SourceField": NotRequired[str],
        "SourceColumn": NotRequired[ColumnIdentifierTypeDef],
    },
)
DatasetParameterTypeDef = TypedDict(
    "DatasetParameterTypeDef",
    {
        "StringDatasetParameter": NotRequired[StringDatasetParameterUnionTypeDef],
        "DecimalDatasetParameter": NotRequired[DecimalDatasetParameterUnionTypeDef],
        "IntegerDatasetParameter": NotRequired[IntegerDatasetParameterUnionTypeDef],
        "DateTimeDatasetParameter": NotRequired[DateTimeDatasetParameterUnionTypeDef],
    },
)
TransformOperationTypeDef = TypedDict(
    "TransformOperationTypeDef",
    {
        "ProjectOperation": NotRequired[ProjectOperationUnionTypeDef],
        "FilterOperation": NotRequired[FilterOperationTypeDef],
        "CreateColumnsOperation": NotRequired[CreateColumnsOperationUnionTypeDef],
        "RenameColumnOperation": NotRequired[RenameColumnOperationTypeDef],
        "CastColumnTypeOperation": NotRequired[CastColumnTypeOperationTypeDef],
        "TagColumnOperation": NotRequired[TagColumnOperationUnionTypeDef],
        "UntagColumnOperation": NotRequired[UntagColumnOperationUnionTypeDef],
        "OverrideDatasetParameterOperation": NotRequired[
            OverrideDatasetParameterOperationUnionTypeDef
        ],
    },
)
DateTimeHierarchyTypeDef = TypedDict(
    "DateTimeHierarchyTypeDef",
    {
        "HierarchyId": str,
        "DrillDownFilters": NotRequired[Sequence[DrillDownFilterUnionTypeDef]],
    },
)
ExplicitHierarchyTypeDef = TypedDict(
    "ExplicitHierarchyTypeDef",
    {
        "HierarchyId": str,
        "Columns": Sequence[ColumnIdentifierTypeDef],
        "DrillDownFilters": NotRequired[Sequence[DrillDownFilterUnionTypeDef]],
    },
)
PredefinedHierarchyTypeDef = TypedDict(
    "PredefinedHierarchyTypeDef",
    {
        "HierarchyId": str,
        "Columns": Sequence[ColumnIdentifierTypeDef],
        "DrillDownFilters": NotRequired[Sequence[DrillDownFilterUnionTypeDef]],
    },
)
ForecastConfigurationTypeDef = TypedDict(
    "ForecastConfigurationTypeDef",
    {
        "ForecastProperties": NotRequired[TimeBasedForecastPropertiesTypeDef],
        "Scenario": NotRequired[ForecastScenarioUnionTypeDef],
    },
)
AssetBundleImportJobDashboardOverridePermissionsUnionTypeDef = Union[
    AssetBundleImportJobDashboardOverridePermissionsTypeDef,
    AssetBundleImportJobDashboardOverridePermissionsOutputTypeDef,
]
AxisDataOptionsTypeDef = TypedDict(
    "AxisDataOptionsTypeDef",
    {
        "NumericAxisOptions": NotRequired[NumericAxisOptionsUnionTypeDef],
        "DateAxisOptions": NotRequired[DateAxisOptionsTypeDef],
    },
)
ContributionAnalysisTimeRangesTypeDef = TypedDict(
    "ContributionAnalysisTimeRangesTypeDef",
    {
        "StartRange": NotRequired[TopicIRFilterOptionUnionTypeDef],
        "EndRange": NotRequired[TopicIRFilterOptionUnionTypeDef],
    },
)
TopicCategoryFilterUnionTypeDef = Union[
    TopicCategoryFilterTypeDef, TopicCategoryFilterOutputTypeDef
]
DataSetTypeDef = TypedDict(
    "DataSetTypeDef",
    {
        "Arn": NotRequired[str],
        "DataSetId": NotRequired[str],
        "Name": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "PhysicalTableMap": NotRequired[Dict[str, PhysicalTableOutputTypeDef]],
        "LogicalTableMap": NotRequired[Dict[str, LogicalTableOutputTypeDef]],
        "OutputColumns": NotRequired[List[OutputColumnTypeDef]],
        "ImportMode": NotRequired[DataSetImportModeType],
        "ConsumedSpiceCapacityInBytes": NotRequired[int],
        "ColumnGroups": NotRequired[List[ColumnGroupOutputTypeDef]],
        "FieldFolders": NotRequired[Dict[str, FieldFolderOutputTypeDef]],
        "RowLevelPermissionDataSet": NotRequired[RowLevelPermissionDataSetTypeDef],
        "RowLevelPermissionTagConfiguration": NotRequired[
            RowLevelPermissionTagConfigurationOutputTypeDef
        ],
        "ColumnLevelPermissionRules": NotRequired[List[ColumnLevelPermissionRuleOutputTypeDef]],
        "DataSetUsageConfiguration": NotRequired[DataSetUsageConfigurationTypeDef],
        "DatasetParameters": NotRequired[List[DatasetParameterOutputTypeDef]],
    },
)
DescribeTemplateResponseTypeDef = TypedDict(
    "DescribeTemplateResponseTypeDef",
    {
        "Template": TemplateTypeDef,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VisualCustomActionOperationOutputTypeDef = TypedDict(
    "VisualCustomActionOperationOutputTypeDef",
    {
        "FilterOperation": NotRequired[CustomActionFilterOperationOutputTypeDef],
        "NavigationOperation": NotRequired[CustomActionNavigationOperationTypeDef],
        "URLOperation": NotRequired[CustomActionURLOperationTypeDef],
        "SetParametersOperation": NotRequired[CustomActionSetParametersOperationOutputTypeDef],
    },
)
PivotTableFieldCollapseStateOptionUnionTypeDef = Union[
    PivotTableFieldCollapseStateOptionTypeDef, PivotTableFieldCollapseStateOptionOutputTypeDef
]
TopicIROutputTypeDef = TypedDict(
    "TopicIROutputTypeDef",
    {
        "Metrics": NotRequired[List[TopicIRMetricOutputTypeDef]],
        "GroupByList": NotRequired[List[TopicIRGroupByTypeDef]],
        "Filters": NotRequired[List[List[TopicIRFilterOptionOutputTypeDef]]],
        "Sort": NotRequired[TopicSortClauseTypeDef],
        "ContributionAnalysis": NotRequired[TopicIRContributionAnalysisOutputTypeDef],
        "Visual": NotRequired[VisualOptionsTypeDef],
    },
)
LineSeriesAxisDisplayOptionsOutputTypeDef = TypedDict(
    "LineSeriesAxisDisplayOptionsOutputTypeDef",
    {
        "AxisOptions": NotRequired[AxisDisplayOptionsOutputTypeDef],
        "MissingDataConfigurations": NotRequired[List[MissingDataConfigurationTypeDef]],
    },
)
DefaultFilterDropDownControlOptionsUnionTypeDef = Union[
    DefaultFilterDropDownControlOptionsTypeDef, DefaultFilterDropDownControlOptionsOutputTypeDef
]
FilterDropDownControlUnionTypeDef = Union[
    FilterDropDownControlTypeDef, FilterDropDownControlOutputTypeDef
]
ParameterDropDownControlUnionTypeDef = Union[
    ParameterDropDownControlTypeDef, ParameterDropDownControlOutputTypeDef
]
DefaultFilterListControlOptionsUnionTypeDef = Union[
    DefaultFilterListControlOptionsTypeDef, DefaultFilterListControlOptionsOutputTypeDef
]
FilterListControlUnionTypeDef = Union[FilterListControlTypeDef, FilterListControlOutputTypeDef]
ParameterListControlUnionTypeDef = Union[
    ParameterListControlTypeDef, ParameterListControlOutputTypeDef
]
DefaultFilterControlOptionsOutputTypeDef = TypedDict(
    "DefaultFilterControlOptionsOutputTypeDef",
    {
        "DefaultDateTimePickerOptions": NotRequired[DefaultDateTimePickerControlOptionsTypeDef],
        "DefaultListOptions": NotRequired[DefaultFilterListControlOptionsOutputTypeDef],
        "DefaultDropdownOptions": NotRequired[DefaultFilterDropDownControlOptionsOutputTypeDef],
        "DefaultTextFieldOptions": NotRequired[DefaultTextFieldControlOptionsTypeDef],
        "DefaultTextAreaOptions": NotRequired[DefaultTextAreaControlOptionsTypeDef],
        "DefaultSliderOptions": NotRequired[DefaultSliderControlOptionsTypeDef],
        "DefaultRelativeDateTimeOptions": NotRequired[DefaultRelativeDateTimeControlOptionsTypeDef],
    },
)
FilterControlOutputTypeDef = TypedDict(
    "FilterControlOutputTypeDef",
    {
        "DateTimePicker": NotRequired[FilterDateTimePickerControlTypeDef],
        "List": NotRequired[FilterListControlOutputTypeDef],
        "Dropdown": NotRequired[FilterDropDownControlOutputTypeDef],
        "TextField": NotRequired[FilterTextFieldControlTypeDef],
        "TextArea": NotRequired[FilterTextAreaControlTypeDef],
        "Slider": NotRequired[FilterSliderControlTypeDef],
        "RelativeDateTime": NotRequired[FilterRelativeDateTimeControlTypeDef],
        "CrossSheet": NotRequired[FilterCrossSheetControlOutputTypeDef],
    },
)
ParameterControlOutputTypeDef = TypedDict(
    "ParameterControlOutputTypeDef",
    {
        "DateTimePicker": NotRequired[ParameterDateTimePickerControlTypeDef],
        "List": NotRequired[ParameterListControlOutputTypeDef],
        "Dropdown": NotRequired[ParameterDropDownControlOutputTypeDef],
        "TextField": NotRequired[ParameterTextFieldControlTypeDef],
        "TextArea": NotRequired[ParameterTextAreaControlTypeDef],
        "Slider": NotRequired[ParameterSliderControlTypeDef],
    },
)
TableFieldURLConfigurationTypeDef = TypedDict(
    "TableFieldURLConfigurationTypeDef",
    {
        "LinkConfiguration": NotRequired[TableFieldLinkConfigurationTypeDef],
        "ImageConfiguration": NotRequired[TableFieldImageConfigurationTypeDef],
    },
)
GeospatialPointStyleOptionsTypeDef = TypedDict(
    "GeospatialPointStyleOptionsTypeDef",
    {
        "SelectedPointStyle": NotRequired[GeospatialSelectedPointStyleType],
        "ClusterMarkerConfiguration": NotRequired[ClusterMarkerConfigurationTypeDef],
        "HeatmapConfiguration": NotRequired[GeospatialHeatmapConfigurationUnionTypeDef],
    },
)
PivotTableOptionsUnionTypeDef = Union[PivotTableOptionsTypeDef, PivotTableOptionsOutputTypeDef]
PivotTotalOptionsUnionTypeDef = Union[PivotTotalOptionsTypeDef, PivotTotalOptionsOutputTypeDef]
PivotTableTotalOptionsOutputTypeDef = TypedDict(
    "PivotTableTotalOptionsOutputTypeDef",
    {
        "RowSubtotalOptions": NotRequired[SubtotalOptionsOutputTypeDef],
        "ColumnSubtotalOptions": NotRequired[SubtotalOptionsOutputTypeDef],
        "RowTotalOptions": NotRequired[PivotTotalOptionsOutputTypeDef],
        "ColumnTotalOptions": NotRequired[PivotTotalOptionsOutputTypeDef],
    },
)
SubtotalOptionsUnionTypeDef = Union[SubtotalOptionsTypeDef, SubtotalOptionsOutputTypeDef]
TableOptionsUnionTypeDef = Union[TableOptionsTypeDef, TableOptionsOutputTypeDef]
TotalOptionsUnionTypeDef = Union[TotalOptionsTypeDef, TotalOptionsOutputTypeDef]
GaugeChartConditionalFormattingOptionOutputTypeDef = TypedDict(
    "GaugeChartConditionalFormattingOptionOutputTypeDef",
    {
        "PrimaryValue": NotRequired[GaugeChartPrimaryValueConditionalFormattingOutputTypeDef],
        "Arc": NotRequired[GaugeChartArcConditionalFormattingOutputTypeDef],
    },
)
KPIConditionalFormattingOptionOutputTypeDef = TypedDict(
    "KPIConditionalFormattingOptionOutputTypeDef",
    {
        "PrimaryValue": NotRequired[KPIPrimaryValueConditionalFormattingOutputTypeDef],
        "ProgressBar": NotRequired[KPIProgressBarConditionalFormattingOutputTypeDef],
        "ActualValue": NotRequired[KPIActualValueConditionalFormattingOutputTypeDef],
        "ComparisonValue": NotRequired[KPIComparisonValueConditionalFormattingOutputTypeDef],
    },
)
FilledMapShapeConditionalFormattingOutputTypeDef = TypedDict(
    "FilledMapShapeConditionalFormattingOutputTypeDef",
    {
        "FieldId": str,
        "Format": NotRequired[ShapeConditionalFormatOutputTypeDef],
    },
)
PivotTableCellConditionalFormattingOutputTypeDef = TypedDict(
    "PivotTableCellConditionalFormattingOutputTypeDef",
    {
        "FieldId": str,
        "TextFormat": NotRequired[TextConditionalFormatOutputTypeDef],
        "Scope": NotRequired[PivotTableConditionalFormattingScopeTypeDef],
        "Scopes": NotRequired[List[PivotTableConditionalFormattingScopeTypeDef]],
    },
)
TableCellConditionalFormattingOutputTypeDef = TypedDict(
    "TableCellConditionalFormattingOutputTypeDef",
    {
        "FieldId": str,
        "TextFormat": NotRequired[TextConditionalFormatOutputTypeDef],
    },
)
ConditionalFormattingColorTypeDef = TypedDict(
    "ConditionalFormattingColorTypeDef",
    {
        "Solid": NotRequired[ConditionalFormattingSolidColorTypeDef],
        "Gradient": NotRequired[ConditionalFormattingGradientColorUnionTypeDef],
    },
)
SheetControlLayoutConfigurationUnionTypeDef = Union[
    SheetControlLayoutConfigurationTypeDef, SheetControlLayoutConfigurationOutputTypeDef
]
ThemeTypeDef = TypedDict(
    "ThemeTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "ThemeId": NotRequired[str],
        "Version": NotRequired[ThemeVersionTypeDef],
        "CreatedTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "Type": NotRequired[ThemeTypeType],
    },
)
TopicNamedEntityUnionTypeDef = Union[TopicNamedEntityTypeDef, TopicNamedEntityOutputTypeDef]
GaugeChartOptionsTypeDef = TypedDict(
    "GaugeChartOptionsTypeDef",
    {
        "PrimaryValueDisplayType": NotRequired[PrimaryValueDisplayTypeType],
        "Comparison": NotRequired[ComparisonConfigurationTypeDef],
        "ArcAxis": NotRequired[ArcAxisConfigurationTypeDef],
        "Arc": NotRequired[ArcConfigurationTypeDef],
        "PrimaryValueFontConfiguration": NotRequired[FontConfigurationTypeDef],
    },
)
KPIOptionsTypeDef = TypedDict(
    "KPIOptionsTypeDef",
    {
        "ProgressBar": NotRequired[ProgressBarOptionsTypeDef],
        "TrendArrows": NotRequired[TrendArrowOptionsTypeDef],
        "SecondaryValue": NotRequired[SecondaryValueOptionsTypeDef],
        "Comparison": NotRequired[ComparisonConfigurationTypeDef],
        "PrimaryValueDisplayType": NotRequired[PrimaryValueDisplayTypeType],
        "PrimaryValueFontConfiguration": NotRequired[FontConfigurationTypeDef],
        "SecondaryValueFontConfiguration": NotRequired[FontConfigurationTypeDef],
        "Sparkline": NotRequired[KPISparklineOptionsTypeDef],
        "VisualLayoutOptions": NotRequired[KPIVisualLayoutOptionsTypeDef],
    },
)
DateDimensionFieldTypeDef = TypedDict(
    "DateDimensionFieldTypeDef",
    {
        "FieldId": str,
        "Column": ColumnIdentifierTypeDef,
        "DateGranularity": NotRequired[TimeGranularityType],
        "HierarchyId": NotRequired[str],
        "FormatConfiguration": NotRequired[DateTimeFormatConfigurationTypeDef],
    },
)
DateMeasureFieldTypeDef = TypedDict(
    "DateMeasureFieldTypeDef",
    {
        "FieldId": str,
        "Column": ColumnIdentifierTypeDef,
        "AggregationFunction": NotRequired[DateAggregationFunctionType],
        "FormatConfiguration": NotRequired[DateTimeFormatConfigurationTypeDef],
    },
)
NumericalDimensionFieldTypeDef = TypedDict(
    "NumericalDimensionFieldTypeDef",
    {
        "FieldId": str,
        "Column": ColumnIdentifierTypeDef,
        "HierarchyId": NotRequired[str],
        "FormatConfiguration": NotRequired[NumberFormatConfigurationTypeDef],
    },
)
NumericalMeasureFieldTypeDef = TypedDict(
    "NumericalMeasureFieldTypeDef",
    {
        "FieldId": str,
        "Column": ColumnIdentifierTypeDef,
        "AggregationFunction": NotRequired[NumericalAggregationFunctionTypeDef],
        "FormatConfiguration": NotRequired[NumberFormatConfigurationTypeDef],
    },
)
ReferenceLineLabelConfigurationTypeDef = TypedDict(
    "ReferenceLineLabelConfigurationTypeDef",
    {
        "ValueLabelConfiguration": NotRequired[ReferenceLineValueLabelConfigurationTypeDef],
        "CustomLabelConfiguration": NotRequired[ReferenceLineCustomLabelConfigurationTypeDef],
        "FontConfiguration": NotRequired[FontConfigurationTypeDef],
        "FontColor": NotRequired[str],
        "HorizontalPosition": NotRequired[ReferenceLineLabelHorizontalPositionType],
        "VerticalPosition": NotRequired[ReferenceLineLabelVerticalPositionType],
    },
)
CategoricalDimensionFieldTypeDef = TypedDict(
    "CategoricalDimensionFieldTypeDef",
    {
        "FieldId": str,
        "Column": ColumnIdentifierTypeDef,
        "HierarchyId": NotRequired[str],
        "FormatConfiguration": NotRequired[StringFormatConfigurationTypeDef],
    },
)
CategoricalMeasureFieldTypeDef = TypedDict(
    "CategoricalMeasureFieldTypeDef",
    {
        "FieldId": str,
        "Column": ColumnIdentifierTypeDef,
        "AggregationFunction": NotRequired[CategoricalAggregationFunctionType],
        "FormatConfiguration": NotRequired[StringFormatConfigurationTypeDef],
    },
)
FormatConfigurationTypeDef = TypedDict(
    "FormatConfigurationTypeDef",
    {
        "StringFormatConfiguration": NotRequired[StringFormatConfigurationTypeDef],
        "NumberFormatConfiguration": NotRequired[NumberFormatConfigurationTypeDef],
        "DateTimeFormatConfiguration": NotRequired[DateTimeFormatConfigurationTypeDef],
    },
)
BodySectionDynamicCategoryDimensionConfigurationUnionTypeDef = Union[
    BodySectionDynamicCategoryDimensionConfigurationTypeDef,
    BodySectionDynamicCategoryDimensionConfigurationOutputTypeDef,
]
BodySectionRepeatDimensionConfigurationOutputTypeDef = TypedDict(
    "BodySectionRepeatDimensionConfigurationOutputTypeDef",
    {
        "DynamicCategoryDimensionConfiguration": NotRequired[
            BodySectionDynamicCategoryDimensionConfigurationOutputTypeDef
        ],
        "DynamicNumericDimensionConfiguration": NotRequired[
            BodySectionDynamicNumericDimensionConfigurationOutputTypeDef
        ],
    },
)
BodySectionDynamicNumericDimensionConfigurationUnionTypeDef = Union[
    BodySectionDynamicNumericDimensionConfigurationTypeDef,
    BodySectionDynamicNumericDimensionConfigurationOutputTypeDef,
]
BarChartSortConfigurationOutputTypeDef = TypedDict(
    "BarChartSortConfigurationOutputTypeDef",
    {
        "CategorySort": NotRequired[List[FieldSortOptionsTypeDef]],
        "CategoryItemsLimit": NotRequired[ItemsLimitConfigurationTypeDef],
        "ColorSort": NotRequired[List[FieldSortOptionsTypeDef]],
        "ColorItemsLimit": NotRequired[ItemsLimitConfigurationTypeDef],
        "SmallMultiplesSort": NotRequired[List[FieldSortOptionsTypeDef]],
        "SmallMultiplesLimitConfiguration": NotRequired[ItemsLimitConfigurationTypeDef],
    },
)
BarChartSortConfigurationTypeDef = TypedDict(
    "BarChartSortConfigurationTypeDef",
    {
        "CategorySort": NotRequired[Sequence[FieldSortOptionsTypeDef]],
        "CategoryItemsLimit": NotRequired[ItemsLimitConfigurationTypeDef],
        "ColorSort": NotRequired[Sequence[FieldSortOptionsTypeDef]],
        "ColorItemsLimit": NotRequired[ItemsLimitConfigurationTypeDef],
        "SmallMultiplesSort": NotRequired[Sequence[FieldSortOptionsTypeDef]],
        "SmallMultiplesLimitConfiguration": NotRequired[ItemsLimitConfigurationTypeDef],
    },
)
BoxPlotSortConfigurationOutputTypeDef = TypedDict(
    "BoxPlotSortConfigurationOutputTypeDef",
    {
        "CategorySort": NotRequired[List[FieldSortOptionsTypeDef]],
        "PaginationConfiguration": NotRequired[PaginationConfigurationTypeDef],
    },
)
BoxPlotSortConfigurationTypeDef = TypedDict(
    "BoxPlotSortConfigurationTypeDef",
    {
        "CategorySort": NotRequired[Sequence[FieldSortOptionsTypeDef]],
        "PaginationConfiguration": NotRequired[PaginationConfigurationTypeDef],
    },
)
ComboChartSortConfigurationOutputTypeDef = TypedDict(
    "ComboChartSortConfigurationOutputTypeDef",
    {
        "CategorySort": NotRequired[List[FieldSortOptionsTypeDef]],
        "CategoryItemsLimit": NotRequired[ItemsLimitConfigurationTypeDef],
        "ColorSort": NotRequired[List[FieldSortOptionsTypeDef]],
        "ColorItemsLimit": NotRequired[ItemsLimitConfigurationTypeDef],
    },
)
ComboChartSortConfigurationTypeDef = TypedDict(
    "ComboChartSortConfigurationTypeDef",
    {
        "CategorySort": NotRequired[Sequence[FieldSortOptionsTypeDef]],
        "CategoryItemsLimit": NotRequired[ItemsLimitConfigurationTypeDef],
        "ColorSort": NotRequired[Sequence[FieldSortOptionsTypeDef]],
        "ColorItemsLimit": NotRequired[ItemsLimitConfigurationTypeDef],
    },
)
FilledMapSortConfigurationOutputTypeDef = TypedDict(
    "FilledMapSortConfigurationOutputTypeDef",
    {
        "CategorySort": NotRequired[List[FieldSortOptionsTypeDef]],
    },
)
FilledMapSortConfigurationTypeDef = TypedDict(
    "FilledMapSortConfigurationTypeDef",
    {
        "CategorySort": NotRequired[Sequence[FieldSortOptionsTypeDef]],
    },
)
FunnelChartSortConfigurationOutputTypeDef = TypedDict(
    "FunnelChartSortConfigurationOutputTypeDef",
    {
        "CategorySort": NotRequired[List[FieldSortOptionsTypeDef]],
        "CategoryItemsLimit": NotRequired[ItemsLimitConfigurationTypeDef],
    },
)
FunnelChartSortConfigurationTypeDef = TypedDict(
    "FunnelChartSortConfigurationTypeDef",
    {
        "CategorySort": NotRequired[Sequence[FieldSortOptionsTypeDef]],
        "CategoryItemsLimit": NotRequired[ItemsLimitConfigurationTypeDef],
    },
)
HeatMapSortConfigurationOutputTypeDef = TypedDict(
    "HeatMapSortConfigurationOutputTypeDef",
    {
        "HeatMapRowSort": NotRequired[List[FieldSortOptionsTypeDef]],
        "HeatMapColumnSort": NotRequired[List[FieldSortOptionsTypeDef]],
        "HeatMapRowItemsLimitConfiguration": NotRequired[ItemsLimitConfigurationTypeDef],
        "HeatMapColumnItemsLimitConfiguration": NotRequired[ItemsLimitConfigurationTypeDef],
    },
)
HeatMapSortConfigurationTypeDef = TypedDict(
    "HeatMapSortConfigurationTypeDef",
    {
        "HeatMapRowSort": NotRequired[Sequence[FieldSortOptionsTypeDef]],
        "HeatMapColumnSort": NotRequired[Sequence[FieldSortOptionsTypeDef]],
        "HeatMapRowItemsLimitConfiguration": NotRequired[ItemsLimitConfigurationTypeDef],
        "HeatMapColumnItemsLimitConfiguration": NotRequired[ItemsLimitConfigurationTypeDef],
    },
)
KPISortConfigurationOutputTypeDef = TypedDict(
    "KPISortConfigurationOutputTypeDef",
    {
        "TrendGroupSort": NotRequired[List[FieldSortOptionsTypeDef]],
    },
)
KPISortConfigurationTypeDef = TypedDict(
    "KPISortConfigurationTypeDef",
    {
        "TrendGroupSort": NotRequired[Sequence[FieldSortOptionsTypeDef]],
    },
)
LineChartSortConfigurationOutputTypeDef = TypedDict(
    "LineChartSortConfigurationOutputTypeDef",
    {
        "CategorySort": NotRequired[List[FieldSortOptionsTypeDef]],
        "CategoryItemsLimitConfiguration": NotRequired[ItemsLimitConfigurationTypeDef],
        "ColorItemsLimitConfiguration": NotRequired[ItemsLimitConfigurationTypeDef],
        "SmallMultiplesSort": NotRequired[List[FieldSortOptionsTypeDef]],
        "SmallMultiplesLimitConfiguration": NotRequired[ItemsLimitConfigurationTypeDef],
    },
)
LineChartSortConfigurationTypeDef = TypedDict(
    "LineChartSortConfigurationTypeDef",
    {
        "CategorySort": NotRequired[Sequence[FieldSortOptionsTypeDef]],
        "CategoryItemsLimitConfiguration": NotRequired[ItemsLimitConfigurationTypeDef],
        "ColorItemsLimitConfiguration": NotRequired[ItemsLimitConfigurationTypeDef],
        "SmallMultiplesSort": NotRequired[Sequence[FieldSortOptionsTypeDef]],
        "SmallMultiplesLimitConfiguration": NotRequired[ItemsLimitConfigurationTypeDef],
    },
)
PieChartSortConfigurationOutputTypeDef = TypedDict(
    "PieChartSortConfigurationOutputTypeDef",
    {
        "CategorySort": NotRequired[List[FieldSortOptionsTypeDef]],
        "CategoryItemsLimit": NotRequired[ItemsLimitConfigurationTypeDef],
        "SmallMultiplesSort": NotRequired[List[FieldSortOptionsTypeDef]],
        "SmallMultiplesLimitConfiguration": NotRequired[ItemsLimitConfigurationTypeDef],
    },
)
PieChartSortConfigurationTypeDef = TypedDict(
    "PieChartSortConfigurationTypeDef",
    {
        "CategorySort": NotRequired[Sequence[FieldSortOptionsTypeDef]],
        "CategoryItemsLimit": NotRequired[ItemsLimitConfigurationTypeDef],
        "SmallMultiplesSort": NotRequired[Sequence[FieldSortOptionsTypeDef]],
        "SmallMultiplesLimitConfiguration": NotRequired[ItemsLimitConfigurationTypeDef],
    },
)
RadarChartSortConfigurationOutputTypeDef = TypedDict(
    "RadarChartSortConfigurationOutputTypeDef",
    {
        "CategorySort": NotRequired[List[FieldSortOptionsTypeDef]],
        "CategoryItemsLimit": NotRequired[ItemsLimitConfigurationTypeDef],
        "ColorSort": NotRequired[List[FieldSortOptionsTypeDef]],
        "ColorItemsLimit": NotRequired[ItemsLimitConfigurationTypeDef],
    },
)
RadarChartSortConfigurationTypeDef = TypedDict(
    "RadarChartSortConfigurationTypeDef",
    {
        "CategorySort": NotRequired[Sequence[FieldSortOptionsTypeDef]],
        "CategoryItemsLimit": NotRequired[ItemsLimitConfigurationTypeDef],
        "ColorSort": NotRequired[Sequence[FieldSortOptionsTypeDef]],
        "ColorItemsLimit": NotRequired[ItemsLimitConfigurationTypeDef],
    },
)
SankeyDiagramSortConfigurationOutputTypeDef = TypedDict(
    "SankeyDiagramSortConfigurationOutputTypeDef",
    {
        "WeightSort": NotRequired[List[FieldSortOptionsTypeDef]],
        "SourceItemsLimit": NotRequired[ItemsLimitConfigurationTypeDef],
        "DestinationItemsLimit": NotRequired[ItemsLimitConfigurationTypeDef],
    },
)
SankeyDiagramSortConfigurationTypeDef = TypedDict(
    "SankeyDiagramSortConfigurationTypeDef",
    {
        "WeightSort": NotRequired[Sequence[FieldSortOptionsTypeDef]],
        "SourceItemsLimit": NotRequired[ItemsLimitConfigurationTypeDef],
        "DestinationItemsLimit": NotRequired[ItemsLimitConfigurationTypeDef],
    },
)
TableSortConfigurationOutputTypeDef = TypedDict(
    "TableSortConfigurationOutputTypeDef",
    {
        "RowSort": NotRequired[List[FieldSortOptionsTypeDef]],
        "PaginationConfiguration": NotRequired[PaginationConfigurationTypeDef],
    },
)
TableSortConfigurationTypeDef = TypedDict(
    "TableSortConfigurationTypeDef",
    {
        "RowSort": NotRequired[Sequence[FieldSortOptionsTypeDef]],
        "PaginationConfiguration": NotRequired[PaginationConfigurationTypeDef],
    },
)
TreeMapSortConfigurationOutputTypeDef = TypedDict(
    "TreeMapSortConfigurationOutputTypeDef",
    {
        "TreeMapSort": NotRequired[List[FieldSortOptionsTypeDef]],
        "TreeMapGroupItemsLimitConfiguration": NotRequired[ItemsLimitConfigurationTypeDef],
    },
)
TreeMapSortConfigurationTypeDef = TypedDict(
    "TreeMapSortConfigurationTypeDef",
    {
        "TreeMapSort": NotRequired[Sequence[FieldSortOptionsTypeDef]],
        "TreeMapGroupItemsLimitConfiguration": NotRequired[ItemsLimitConfigurationTypeDef],
    },
)
WaterfallChartSortConfigurationOutputTypeDef = TypedDict(
    "WaterfallChartSortConfigurationOutputTypeDef",
    {
        "CategorySort": NotRequired[List[FieldSortOptionsTypeDef]],
        "BreakdownItemsLimit": NotRequired[ItemsLimitConfigurationTypeDef],
    },
)
WaterfallChartSortConfigurationTypeDef = TypedDict(
    "WaterfallChartSortConfigurationTypeDef",
    {
        "CategorySort": NotRequired[Sequence[FieldSortOptionsTypeDef]],
        "BreakdownItemsLimit": NotRequired[ItemsLimitConfigurationTypeDef],
    },
)
WordCloudSortConfigurationOutputTypeDef = TypedDict(
    "WordCloudSortConfigurationOutputTypeDef",
    {
        "CategoryItemsLimit": NotRequired[ItemsLimitConfigurationTypeDef],
        "CategorySort": NotRequired[List[FieldSortOptionsTypeDef]],
    },
)
WordCloudSortConfigurationTypeDef = TypedDict(
    "WordCloudSortConfigurationTypeDef",
    {
        "CategoryItemsLimit": NotRequired[ItemsLimitConfigurationTypeDef],
        "CategorySort": NotRequired[Sequence[FieldSortOptionsTypeDef]],
    },
)
PivotFieldSortOptionsOutputTypeDef = TypedDict(
    "PivotFieldSortOptionsOutputTypeDef",
    {
        "FieldId": str,
        "SortBy": PivotTableSortByOutputTypeDef,
    },
)
PivotTableSortByUnionTypeDef = Union[PivotTableSortByTypeDef, PivotTableSortByOutputTypeDef]
FieldBasedTooltipOutputTypeDef = TypedDict(
    "FieldBasedTooltipOutputTypeDef",
    {
        "AggregationVisibility": NotRequired[VisibilityType],
        "TooltipTitleType": NotRequired[TooltipTitleTypeType],
        "TooltipFields": NotRequired[List[TooltipItemTypeDef]],
    },
)
FieldBasedTooltipTypeDef = TypedDict(
    "FieldBasedTooltipTypeDef",
    {
        "AggregationVisibility": NotRequired[VisibilityType],
        "TooltipTitleType": NotRequired[TooltipTitleTypeType],
        "TooltipFields": NotRequired[Sequence[TooltipItemTypeDef]],
    },
)
TopicDetailsOutputTypeDef = TypedDict(
    "TopicDetailsOutputTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "UserExperienceVersion": NotRequired[TopicUserExperienceVersionType],
        "DataSets": NotRequired[List[DatasetMetadataOutputTypeDef]],
        "ConfigOptions": NotRequired[TopicConfigOptionsTypeDef],
    },
)
DescribeAssetBundleImportJobResponseTypeDef = TypedDict(
    "DescribeAssetBundleImportJobResponseTypeDef",
    {
        "JobStatus": AssetBundleImportJobStatusType,
        "Errors": List[AssetBundleImportJobErrorTypeDef],
        "RollbackErrors": List[AssetBundleImportJobErrorTypeDef],
        "Arn": str,
        "CreatedTime": datetime,
        "AssetBundleImportJobId": str,
        "AwsAccountId": str,
        "AssetBundleImportSource": AssetBundleImportSourceDescriptionTypeDef,
        "OverrideParameters": AssetBundleImportJobOverrideParametersOutputTypeDef,
        "FailureAction": AssetBundleImportFailureActionType,
        "RequestId": str,
        "Status": int,
        "OverridePermissions": AssetBundleImportJobOverridePermissionsOutputTypeDef,
        "OverrideTags": AssetBundleImportJobOverrideTagsOutputTypeDef,
        "OverrideValidationStrategy": AssetBundleImportJobOverrideValidationStrategyTypeDef,
        "Warnings": List[AssetBundleImportJobWarningTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DataSourceParametersUnionTypeDef = Union[
    DataSourceParametersTypeDef, DataSourceParametersOutputTypeDef
]
SnapshotJobResultTypeDef = TypedDict(
    "SnapshotJobResultTypeDef",
    {
        "AnonymousUsers": NotRequired[List[AnonymousUserSnapshotJobResultTypeDef]],
    },
)
CustomActionFilterOperationUnionTypeDef = Union[
    CustomActionFilterOperationTypeDef, CustomActionFilterOperationOutputTypeDef
]
DefaultNewSheetConfigurationTypeDef = TypedDict(
    "DefaultNewSheetConfigurationTypeDef",
    {
        "InteractiveLayoutConfiguration": NotRequired[DefaultInteractiveLayoutConfigurationTypeDef],
        "PaginatedLayoutConfiguration": NotRequired[DefaultPaginatedLayoutConfigurationTypeDef],
        "SheetContentType": NotRequired[SheetContentTypeType],
    },
)
BodySectionContentOutputTypeDef = TypedDict(
    "BodySectionContentOutputTypeDef",
    {
        "Layout": NotRequired[SectionLayoutConfigurationOutputTypeDef],
    },
)
HeaderFooterSectionConfigurationOutputTypeDef = TypedDict(
    "HeaderFooterSectionConfigurationOutputTypeDef",
    {
        "SectionId": str,
        "Layout": SectionLayoutConfigurationOutputTypeDef,
        "Style": NotRequired[SectionStyleTypeDef],
    },
)
FreeFormLayoutConfigurationUnionTypeDef = Union[
    FreeFormLayoutConfigurationTypeDef, FreeFormLayoutConfigurationOutputTypeDef
]
FreeFormSectionLayoutConfigurationUnionTypeDef = Union[
    FreeFormSectionLayoutConfigurationTypeDef, FreeFormSectionLayoutConfigurationOutputTypeDef
]
FilterScopeConfigurationUnionTypeDef = Union[
    FilterScopeConfigurationTypeDef, FilterScopeConfigurationOutputTypeDef
]
SnapshotFileGroupUnionTypeDef = Union[SnapshotFileGroupTypeDef, SnapshotFileGroupOutputTypeDef]
ParameterDeclarationTypeDef = TypedDict(
    "ParameterDeclarationTypeDef",
    {
        "StringParameterDeclaration": NotRequired[StringParameterDeclarationUnionTypeDef],
        "DecimalParameterDeclaration": NotRequired[DecimalParameterDeclarationUnionTypeDef],
        "IntegerParameterDeclaration": NotRequired[IntegerParameterDeclarationUnionTypeDef],
        "DateTimeParameterDeclaration": NotRequired[DateTimeParameterDeclarationUnionTypeDef],
    },
)
DestinationParameterValueConfigurationUnionTypeDef = Union[
    DestinationParameterValueConfigurationTypeDef,
    DestinationParameterValueConfigurationOutputTypeDef,
]
DatasetParameterUnionTypeDef = Union[DatasetParameterTypeDef, DatasetParameterOutputTypeDef]
TransformOperationUnionTypeDef = Union[TransformOperationTypeDef, TransformOperationOutputTypeDef]
DateTimeHierarchyUnionTypeDef = Union[DateTimeHierarchyTypeDef, DateTimeHierarchyOutputTypeDef]
ExplicitHierarchyUnionTypeDef = Union[ExplicitHierarchyTypeDef, ExplicitHierarchyOutputTypeDef]
PredefinedHierarchyUnionTypeDef = Union[
    PredefinedHierarchyTypeDef, PredefinedHierarchyOutputTypeDef
]
ForecastConfigurationUnionTypeDef = Union[
    ForecastConfigurationTypeDef, ForecastConfigurationOutputTypeDef
]
AssetBundleImportJobOverridePermissionsTypeDef = TypedDict(
    "AssetBundleImportJobOverridePermissionsTypeDef",
    {
        "DataSources": NotRequired[
            Sequence[AssetBundleImportJobDataSourceOverridePermissionsUnionTypeDef]
        ],
        "DataSets": NotRequired[
            Sequence[AssetBundleImportJobDataSetOverridePermissionsUnionTypeDef]
        ],
        "Themes": NotRequired[Sequence[AssetBundleImportJobThemeOverridePermissionsUnionTypeDef]],
        "Analyses": NotRequired[
            Sequence[AssetBundleImportJobAnalysisOverridePermissionsUnionTypeDef]
        ],
        "Dashboards": NotRequired[
            Sequence[AssetBundleImportJobDashboardOverridePermissionsUnionTypeDef]
        ],
        "Folders": NotRequired[Sequence[AssetBundleImportJobFolderOverridePermissionsUnionTypeDef]],
    },
)
AxisDataOptionsUnionTypeDef = Union[AxisDataOptionsTypeDef, AxisDataOptionsOutputTypeDef]
ContributionAnalysisTimeRangesUnionTypeDef = Union[
    ContributionAnalysisTimeRangesTypeDef, ContributionAnalysisTimeRangesOutputTypeDef
]
TopicFilterTypeDef = TypedDict(
    "TopicFilterTypeDef",
    {
        "FilterName": str,
        "OperandFieldName": str,
        "FilterDescription": NotRequired[str],
        "FilterClass": NotRequired[FilterClassType],
        "FilterSynonyms": NotRequired[Sequence[str]],
        "FilterType": NotRequired[NamedFilterTypeType],
        "CategoryFilter": NotRequired[TopicCategoryFilterUnionTypeDef],
        "NumericEqualityFilter": NotRequired[TopicNumericEqualityFilterTypeDef],
        "NumericRangeFilter": NotRequired[TopicNumericRangeFilterTypeDef],
        "DateRangeFilter": NotRequired[TopicDateRangeFilterTypeDef],
        "RelativeDateFilter": NotRequired[TopicRelativeDateFilterTypeDef],
    },
)
DescribeDataSetResponseTypeDef = TypedDict(
    "DescribeDataSetResponseTypeDef",
    {
        "DataSet": DataSetTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VisualCustomActionOutputTypeDef = TypedDict(
    "VisualCustomActionOutputTypeDef",
    {
        "CustomActionId": str,
        "Name": str,
        "Trigger": VisualCustomActionTriggerType,
        "ActionOperations": List[VisualCustomActionOperationOutputTypeDef],
        "Status": NotRequired[WidgetStatusType],
    },
)
PivotTableFieldOptionsTypeDef = TypedDict(
    "PivotTableFieldOptionsTypeDef",
    {
        "SelectedFieldOptions": NotRequired[Sequence[PivotTableFieldOptionTypeDef]],
        "DataPathOptions": NotRequired[Sequence[PivotTableDataPathOptionUnionTypeDef]],
        "CollapseStateOptions": NotRequired[
            Sequence[PivotTableFieldCollapseStateOptionUnionTypeDef]
        ],
    },
)
TopicVisualOutputTypeDef = TypedDict(
    "TopicVisualOutputTypeDef",
    {
        "VisualId": NotRequired[str],
        "Role": NotRequired[VisualRoleType],
        "Ir": NotRequired[TopicIROutputTypeDef],
        "SupportingVisuals": NotRequired[List[Dict[str, Any]]],
    },
)
DefaultFilterControlOptionsTypeDef = TypedDict(
    "DefaultFilterControlOptionsTypeDef",
    {
        "DefaultDateTimePickerOptions": NotRequired[DefaultDateTimePickerControlOptionsTypeDef],
        "DefaultListOptions": NotRequired[DefaultFilterListControlOptionsUnionTypeDef],
        "DefaultDropdownOptions": NotRequired[DefaultFilterDropDownControlOptionsUnionTypeDef],
        "DefaultTextFieldOptions": NotRequired[DefaultTextFieldControlOptionsTypeDef],
        "DefaultTextAreaOptions": NotRequired[DefaultTextAreaControlOptionsTypeDef],
        "DefaultSliderOptions": NotRequired[DefaultSliderControlOptionsTypeDef],
        "DefaultRelativeDateTimeOptions": NotRequired[DefaultRelativeDateTimeControlOptionsTypeDef],
    },
)
FilterControlTypeDef = TypedDict(
    "FilterControlTypeDef",
    {
        "DateTimePicker": NotRequired[FilterDateTimePickerControlTypeDef],
        "List": NotRequired[FilterListControlUnionTypeDef],
        "Dropdown": NotRequired[FilterDropDownControlUnionTypeDef],
        "TextField": NotRequired[FilterTextFieldControlTypeDef],
        "TextArea": NotRequired[FilterTextAreaControlTypeDef],
        "Slider": NotRequired[FilterSliderControlTypeDef],
        "RelativeDateTime": NotRequired[FilterRelativeDateTimeControlTypeDef],
        "CrossSheet": NotRequired[FilterCrossSheetControlUnionTypeDef],
    },
)
ParameterControlTypeDef = TypedDict(
    "ParameterControlTypeDef",
    {
        "DateTimePicker": NotRequired[ParameterDateTimePickerControlTypeDef],
        "List": NotRequired[ParameterListControlUnionTypeDef],
        "Dropdown": NotRequired[ParameterDropDownControlUnionTypeDef],
        "TextField": NotRequired[ParameterTextFieldControlTypeDef],
        "TextArea": NotRequired[ParameterTextAreaControlTypeDef],
        "Slider": NotRequired[ParameterSliderControlTypeDef],
    },
)
DefaultFilterControlConfigurationOutputTypeDef = TypedDict(
    "DefaultFilterControlConfigurationOutputTypeDef",
    {
        "Title": str,
        "ControlOptions": DefaultFilterControlOptionsOutputTypeDef,
    },
)
TableFieldOptionTypeDef = TypedDict(
    "TableFieldOptionTypeDef",
    {
        "FieldId": str,
        "Width": NotRequired[str],
        "CustomLabel": NotRequired[str],
        "Visibility": NotRequired[VisibilityType],
        "URLStyling": NotRequired[TableFieldURLConfigurationTypeDef],
    },
)
GeospatialPointStyleOptionsUnionTypeDef = Union[
    GeospatialPointStyleOptionsTypeDef, GeospatialPointStyleOptionsOutputTypeDef
]
PivotTableTotalOptionsTypeDef = TypedDict(
    "PivotTableTotalOptionsTypeDef",
    {
        "RowSubtotalOptions": NotRequired[SubtotalOptionsUnionTypeDef],
        "ColumnSubtotalOptions": NotRequired[SubtotalOptionsUnionTypeDef],
        "RowTotalOptions": NotRequired[PivotTotalOptionsUnionTypeDef],
        "ColumnTotalOptions": NotRequired[PivotTotalOptionsUnionTypeDef],
    },
)
GaugeChartConditionalFormattingOutputTypeDef = TypedDict(
    "GaugeChartConditionalFormattingOutputTypeDef",
    {
        "ConditionalFormattingOptions": NotRequired[
            List[GaugeChartConditionalFormattingOptionOutputTypeDef]
        ],
    },
)
KPIConditionalFormattingOutputTypeDef = TypedDict(
    "KPIConditionalFormattingOutputTypeDef",
    {
        "ConditionalFormattingOptions": NotRequired[
            List[KPIConditionalFormattingOptionOutputTypeDef]
        ],
    },
)
FilledMapConditionalFormattingOptionOutputTypeDef = TypedDict(
    "FilledMapConditionalFormattingOptionOutputTypeDef",
    {
        "Shape": FilledMapShapeConditionalFormattingOutputTypeDef,
    },
)
PivotTableConditionalFormattingOptionOutputTypeDef = TypedDict(
    "PivotTableConditionalFormattingOptionOutputTypeDef",
    {
        "Cell": NotRequired[PivotTableCellConditionalFormattingOutputTypeDef],
    },
)
TableConditionalFormattingOptionOutputTypeDef = TypedDict(
    "TableConditionalFormattingOptionOutputTypeDef",
    {
        "Cell": NotRequired[TableCellConditionalFormattingOutputTypeDef],
        "Row": NotRequired[TableRowConditionalFormattingOutputTypeDef],
    },
)
ConditionalFormattingColorUnionTypeDef = Union[
    ConditionalFormattingColorTypeDef, ConditionalFormattingColorOutputTypeDef
]
SheetControlLayoutTypeDef = TypedDict(
    "SheetControlLayoutTypeDef",
    {
        "Configuration": SheetControlLayoutConfigurationUnionTypeDef,
    },
)
DescribeThemeResponseTypeDef = TypedDict(
    "DescribeThemeResponseTypeDef",
    {
        "Theme": ThemeTypeDef,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReferenceLineTypeDef = TypedDict(
    "ReferenceLineTypeDef",
    {
        "DataConfiguration": ReferenceLineDataConfigurationTypeDef,
        "Status": NotRequired[WidgetStatusType],
        "StyleConfiguration": NotRequired[ReferenceLineStyleConfigurationTypeDef],
        "LabelConfiguration": NotRequired[ReferenceLineLabelConfigurationTypeDef],
    },
)
DimensionFieldTypeDef = TypedDict(
    "DimensionFieldTypeDef",
    {
        "NumericalDimensionField": NotRequired[NumericalDimensionFieldTypeDef],
        "CategoricalDimensionField": NotRequired[CategoricalDimensionFieldTypeDef],
        "DateDimensionField": NotRequired[DateDimensionFieldTypeDef],
    },
)
MeasureFieldTypeDef = TypedDict(
    "MeasureFieldTypeDef",
    {
        "NumericalMeasureField": NotRequired[NumericalMeasureFieldTypeDef],
        "CategoricalMeasureField": NotRequired[CategoricalMeasureFieldTypeDef],
        "DateMeasureField": NotRequired[DateMeasureFieldTypeDef],
        "CalculatedMeasureField": NotRequired[CalculatedMeasureFieldTypeDef],
    },
)
ColumnConfigurationOutputTypeDef = TypedDict(
    "ColumnConfigurationOutputTypeDef",
    {
        "Column": ColumnIdentifierTypeDef,
        "FormatConfiguration": NotRequired[FormatConfigurationTypeDef],
        "Role": NotRequired[ColumnRoleType],
        "ColorsConfiguration": NotRequired[ColorsConfigurationOutputTypeDef],
    },
)
ColumnConfigurationTypeDef = TypedDict(
    "ColumnConfigurationTypeDef",
    {
        "Column": ColumnIdentifierTypeDef,
        "FormatConfiguration": NotRequired[FormatConfigurationTypeDef],
        "Role": NotRequired[ColumnRoleType],
        "ColorsConfiguration": NotRequired[ColorsConfigurationUnionTypeDef],
    },
)
UnaggregatedFieldTypeDef = TypedDict(
    "UnaggregatedFieldTypeDef",
    {
        "FieldId": str,
        "Column": ColumnIdentifierTypeDef,
        "FormatConfiguration": NotRequired[FormatConfigurationTypeDef],
    },
)
BodySectionRepeatConfigurationOutputTypeDef = TypedDict(
    "BodySectionRepeatConfigurationOutputTypeDef",
    {
        "DimensionConfigurations": NotRequired[
            List[BodySectionRepeatDimensionConfigurationOutputTypeDef]
        ],
        "PageBreakConfiguration": NotRequired[BodySectionRepeatPageBreakConfigurationTypeDef],
        "NonRepeatingVisuals": NotRequired[List[str]],
    },
)
BodySectionRepeatDimensionConfigurationTypeDef = TypedDict(
    "BodySectionRepeatDimensionConfigurationTypeDef",
    {
        "DynamicCategoryDimensionConfiguration": NotRequired[
            BodySectionDynamicCategoryDimensionConfigurationUnionTypeDef
        ],
        "DynamicNumericDimensionConfiguration": NotRequired[
            BodySectionDynamicNumericDimensionConfigurationUnionTypeDef
        ],
    },
)
BarChartSortConfigurationUnionTypeDef = Union[
    BarChartSortConfigurationTypeDef, BarChartSortConfigurationOutputTypeDef
]
BoxPlotSortConfigurationUnionTypeDef = Union[
    BoxPlotSortConfigurationTypeDef, BoxPlotSortConfigurationOutputTypeDef
]
ComboChartSortConfigurationUnionTypeDef = Union[
    ComboChartSortConfigurationTypeDef, ComboChartSortConfigurationOutputTypeDef
]
FilledMapSortConfigurationUnionTypeDef = Union[
    FilledMapSortConfigurationTypeDef, FilledMapSortConfigurationOutputTypeDef
]
FunnelChartSortConfigurationUnionTypeDef = Union[
    FunnelChartSortConfigurationTypeDef, FunnelChartSortConfigurationOutputTypeDef
]
HeatMapSortConfigurationUnionTypeDef = Union[
    HeatMapSortConfigurationTypeDef, HeatMapSortConfigurationOutputTypeDef
]
KPISortConfigurationUnionTypeDef = Union[
    KPISortConfigurationTypeDef, KPISortConfigurationOutputTypeDef
]
LineChartSortConfigurationUnionTypeDef = Union[
    LineChartSortConfigurationTypeDef, LineChartSortConfigurationOutputTypeDef
]
PieChartSortConfigurationUnionTypeDef = Union[
    PieChartSortConfigurationTypeDef, PieChartSortConfigurationOutputTypeDef
]
RadarChartSortConfigurationUnionTypeDef = Union[
    RadarChartSortConfigurationTypeDef, RadarChartSortConfigurationOutputTypeDef
]
SankeyDiagramSortConfigurationUnionTypeDef = Union[
    SankeyDiagramSortConfigurationTypeDef, SankeyDiagramSortConfigurationOutputTypeDef
]
TableSortConfigurationUnionTypeDef = Union[
    TableSortConfigurationTypeDef, TableSortConfigurationOutputTypeDef
]
TreeMapSortConfigurationUnionTypeDef = Union[
    TreeMapSortConfigurationTypeDef, TreeMapSortConfigurationOutputTypeDef
]
WaterfallChartSortConfigurationUnionTypeDef = Union[
    WaterfallChartSortConfigurationTypeDef, WaterfallChartSortConfigurationOutputTypeDef
]
WordCloudSortConfigurationUnionTypeDef = Union[
    WordCloudSortConfigurationTypeDef, WordCloudSortConfigurationOutputTypeDef
]
PivotTableSortConfigurationOutputTypeDef = TypedDict(
    "PivotTableSortConfigurationOutputTypeDef",
    {
        "FieldSortOptions": NotRequired[List[PivotFieldSortOptionsOutputTypeDef]],
    },
)
PivotFieldSortOptionsTypeDef = TypedDict(
    "PivotFieldSortOptionsTypeDef",
    {
        "FieldId": str,
        "SortBy": PivotTableSortByUnionTypeDef,
    },
)
TooltipOptionsOutputTypeDef = TypedDict(
    "TooltipOptionsOutputTypeDef",
    {
        "TooltipVisibility": NotRequired[VisibilityType],
        "SelectedTooltipType": NotRequired[SelectedTooltipTypeType],
        "FieldBasedTooltip": NotRequired[FieldBasedTooltipOutputTypeDef],
    },
)
FieldBasedTooltipUnionTypeDef = Union[FieldBasedTooltipTypeDef, FieldBasedTooltipOutputTypeDef]
DescribeTopicResponseTypeDef = TypedDict(
    "DescribeTopicResponseTypeDef",
    {
        "Arn": str,
        "TopicId": str,
        "Topic": TopicDetailsOutputTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssetBundleImportJobDataSourceOverrideParametersTypeDef = TypedDict(
    "AssetBundleImportJobDataSourceOverrideParametersTypeDef",
    {
        "DataSourceId": str,
        "Name": NotRequired[str],
        "DataSourceParameters": NotRequired[DataSourceParametersUnionTypeDef],
        "VpcConnectionProperties": NotRequired[VpcConnectionPropertiesTypeDef],
        "SslProperties": NotRequired[SslPropertiesTypeDef],
        "Credentials": NotRequired[AssetBundleImportJobDataSourceCredentialsTypeDef],
    },
)
CredentialPairTypeDef = TypedDict(
    "CredentialPairTypeDef",
    {
        "Username": str,
        "Password": str,
        "AlternateDataSourceParameters": NotRequired[Sequence[DataSourceParametersUnionTypeDef]],
    },
)
DescribeDashboardSnapshotJobResultResponseTypeDef = TypedDict(
    "DescribeDashboardSnapshotJobResultResponseTypeDef",
    {
        "Arn": str,
        "JobStatus": SnapshotJobStatusType,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "Result": SnapshotJobResultTypeDef,
        "ErrorInfo": SnapshotJobErrorInfoTypeDef,
        "RequestId": str,
        "Status": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AnalysisDefaultsTypeDef = TypedDict(
    "AnalysisDefaultsTypeDef",
    {
        "DefaultNewSheetConfiguration": DefaultNewSheetConfigurationTypeDef,
    },
)
SectionLayoutConfigurationTypeDef = TypedDict(
    "SectionLayoutConfigurationTypeDef",
    {
        "FreeFormLayout": FreeFormSectionLayoutConfigurationUnionTypeDef,
    },
)
SnapshotConfigurationTypeDef = TypedDict(
    "SnapshotConfigurationTypeDef",
    {
        "FileGroups": Sequence[SnapshotFileGroupUnionTypeDef],
        "DestinationConfiguration": NotRequired[SnapshotDestinationConfigurationUnionTypeDef],
        "Parameters": NotRequired[ParametersUnionTypeDef],
    },
)
ParameterDeclarationUnionTypeDef = Union[
    ParameterDeclarationTypeDef, ParameterDeclarationOutputTypeDef
]
SetParameterValueConfigurationTypeDef = TypedDict(
    "SetParameterValueConfigurationTypeDef",
    {
        "DestinationParameterName": str,
        "Value": DestinationParameterValueConfigurationUnionTypeDef,
    },
)
LogicalTableTypeDef = TypedDict(
    "LogicalTableTypeDef",
    {
        "Alias": str,
        "Source": LogicalTableSourceTypeDef,
        "DataTransforms": NotRequired[Sequence[TransformOperationUnionTypeDef]],
    },
)
ColumnHierarchyTypeDef = TypedDict(
    "ColumnHierarchyTypeDef",
    {
        "ExplicitHierarchy": NotRequired[ExplicitHierarchyUnionTypeDef],
        "DateTimeHierarchy": NotRequired[DateTimeHierarchyUnionTypeDef],
        "PredefinedHierarchy": NotRequired[PredefinedHierarchyUnionTypeDef],
    },
)
AxisDisplayOptionsTypeDef = TypedDict(
    "AxisDisplayOptionsTypeDef",
    {
        "TickLabelOptions": NotRequired[AxisTickLabelOptionsTypeDef],
        "AxisLineVisibility": NotRequired[VisibilityType],
        "GridLineVisibility": NotRequired[VisibilityType],
        "DataOptions": NotRequired[AxisDataOptionsUnionTypeDef],
        "ScrollbarOptions": NotRequired[ScrollBarOptionsTypeDef],
        "AxisOffset": NotRequired[str],
    },
)
TopicIRContributionAnalysisTypeDef = TypedDict(
    "TopicIRContributionAnalysisTypeDef",
    {
        "Factors": NotRequired[Sequence[ContributionAnalysisFactorTypeDef]],
        "TimeRanges": NotRequired[ContributionAnalysisTimeRangesUnionTypeDef],
        "Direction": NotRequired[ContributionAnalysisDirectionType],
        "SortType": NotRequired[ContributionAnalysisSortTypeType],
    },
)
TopicFilterUnionTypeDef = Union[TopicFilterTypeDef, TopicFilterOutputTypeDef]
CustomContentVisualOutputTypeDef = TypedDict(
    "CustomContentVisualOutputTypeDef",
    {
        "VisualId": str,
        "DataSetIdentifier": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[CustomContentConfigurationTypeDef],
        "Actions": NotRequired[List[VisualCustomActionOutputTypeDef]],
    },
)
EmptyVisualOutputTypeDef = TypedDict(
    "EmptyVisualOutputTypeDef",
    {
        "VisualId": str,
        "DataSetIdentifier": str,
        "Actions": NotRequired[List[VisualCustomActionOutputTypeDef]],
    },
)
PivotTableFieldOptionsUnionTypeDef = Union[
    PivotTableFieldOptionsTypeDef, PivotTableFieldOptionsOutputTypeDef
]
TopicReviewedAnswerTypeDef = TypedDict(
    "TopicReviewedAnswerTypeDef",
    {
        "AnswerId": str,
        "DatasetArn": str,
        "Question": str,
        "Arn": NotRequired[str],
        "Mir": NotRequired[TopicIROutputTypeDef],
        "PrimaryVisual": NotRequired[TopicVisualOutputTypeDef],
        "Template": NotRequired[TopicTemplateOutputTypeDef],
    },
)
DefaultFilterControlOptionsUnionTypeDef = Union[
    DefaultFilterControlOptionsTypeDef, DefaultFilterControlOptionsOutputTypeDef
]
FilterControlUnionTypeDef = Union[FilterControlTypeDef, FilterControlOutputTypeDef]
ParameterControlUnionTypeDef = Union[ParameterControlTypeDef, ParameterControlOutputTypeDef]
CategoryFilterOutputTypeDef = TypedDict(
    "CategoryFilterOutputTypeDef",
    {
        "FilterId": str,
        "Column": ColumnIdentifierTypeDef,
        "Configuration": CategoryFilterConfigurationOutputTypeDef,
        "DefaultFilterControlConfiguration": NotRequired[
            DefaultFilterControlConfigurationOutputTypeDef
        ],
    },
)
CategoryInnerFilterOutputTypeDef = TypedDict(
    "CategoryInnerFilterOutputTypeDef",
    {
        "Column": ColumnIdentifierTypeDef,
        "Configuration": CategoryFilterConfigurationOutputTypeDef,
        "DefaultFilterControlConfiguration": NotRequired[
            DefaultFilterControlConfigurationOutputTypeDef
        ],
    },
)
NumericEqualityFilterOutputTypeDef = TypedDict(
    "NumericEqualityFilterOutputTypeDef",
    {
        "FilterId": str,
        "Column": ColumnIdentifierTypeDef,
        "MatchOperator": NumericEqualityMatchOperatorType,
        "NullOption": FilterNullOptionType,
        "Value": NotRequired[float],
        "SelectAllOptions": NotRequired[Literal["FILTER_ALL_VALUES"]],
        "AggregationFunction": NotRequired[AggregationFunctionTypeDef],
        "ParameterName": NotRequired[str],
        "DefaultFilterControlConfiguration": NotRequired[
            DefaultFilterControlConfigurationOutputTypeDef
        ],
    },
)
NumericRangeFilterOutputTypeDef = TypedDict(
    "NumericRangeFilterOutputTypeDef",
    {
        "FilterId": str,
        "Column": ColumnIdentifierTypeDef,
        "NullOption": FilterNullOptionType,
        "IncludeMinimum": NotRequired[bool],
        "IncludeMaximum": NotRequired[bool],
        "RangeMinimum": NotRequired[NumericRangeFilterValueTypeDef],
        "RangeMaximum": NotRequired[NumericRangeFilterValueTypeDef],
        "SelectAllOptions": NotRequired[Literal["FILTER_ALL_VALUES"]],
        "AggregationFunction": NotRequired[AggregationFunctionTypeDef],
        "DefaultFilterControlConfiguration": NotRequired[
            DefaultFilterControlConfigurationOutputTypeDef
        ],
    },
)
RelativeDatesFilterOutputTypeDef = TypedDict(
    "RelativeDatesFilterOutputTypeDef",
    {
        "FilterId": str,
        "Column": ColumnIdentifierTypeDef,
        "AnchorDateConfiguration": AnchorDateConfigurationTypeDef,
        "TimeGranularity": TimeGranularityType,
        "RelativeDateType": RelativeDateTypeType,
        "NullOption": FilterNullOptionType,
        "MinimumGranularity": NotRequired[TimeGranularityType],
        "RelativeDateValue": NotRequired[int],
        "ParameterName": NotRequired[str],
        "ExcludePeriodConfiguration": NotRequired[ExcludePeriodConfigurationTypeDef],
        "DefaultFilterControlConfiguration": NotRequired[
            DefaultFilterControlConfigurationOutputTypeDef
        ],
    },
)
TimeEqualityFilterOutputTypeDef = TypedDict(
    "TimeEqualityFilterOutputTypeDef",
    {
        "FilterId": str,
        "Column": ColumnIdentifierTypeDef,
        "Value": NotRequired[datetime],
        "ParameterName": NotRequired[str],
        "TimeGranularity": NotRequired[TimeGranularityType],
        "RollingDate": NotRequired[RollingDateConfigurationTypeDef],
        "DefaultFilterControlConfiguration": NotRequired[
            DefaultFilterControlConfigurationOutputTypeDef
        ],
    },
)
TimeRangeFilterOutputTypeDef = TypedDict(
    "TimeRangeFilterOutputTypeDef",
    {
        "FilterId": str,
        "Column": ColumnIdentifierTypeDef,
        "NullOption": FilterNullOptionType,
        "IncludeMinimum": NotRequired[bool],
        "IncludeMaximum": NotRequired[bool],
        "RangeMinimumValue": NotRequired[TimeRangeFilterValueOutputTypeDef],
        "RangeMaximumValue": NotRequired[TimeRangeFilterValueOutputTypeDef],
        "ExcludePeriodConfiguration": NotRequired[ExcludePeriodConfigurationTypeDef],
        "TimeGranularity": NotRequired[TimeGranularityType],
        "DefaultFilterControlConfiguration": NotRequired[
            DefaultFilterControlConfigurationOutputTypeDef
        ],
    },
)
TopBottomFilterOutputTypeDef = TypedDict(
    "TopBottomFilterOutputTypeDef",
    {
        "FilterId": str,
        "Column": ColumnIdentifierTypeDef,
        "AggregationSortConfigurations": List[AggregationSortConfigurationTypeDef],
        "Limit": NotRequired[int],
        "TimeGranularity": NotRequired[TimeGranularityType],
        "ParameterName": NotRequired[str],
        "DefaultFilterControlConfiguration": NotRequired[
            DefaultFilterControlConfigurationOutputTypeDef
        ],
    },
)
TableFieldOptionsOutputTypeDef = TypedDict(
    "TableFieldOptionsOutputTypeDef",
    {
        "SelectedFieldOptions": NotRequired[List[TableFieldOptionTypeDef]],
        "Order": NotRequired[List[str]],
        "PinnedFieldOptions": NotRequired[TablePinnedFieldOptionsOutputTypeDef],
    },
)
TableFieldOptionsTypeDef = TypedDict(
    "TableFieldOptionsTypeDef",
    {
        "SelectedFieldOptions": NotRequired[Sequence[TableFieldOptionTypeDef]],
        "Order": NotRequired[Sequence[str]],
        "PinnedFieldOptions": NotRequired[TablePinnedFieldOptionsUnionTypeDef],
    },
)
PivotTableTotalOptionsUnionTypeDef = Union[
    PivotTableTotalOptionsTypeDef, PivotTableTotalOptionsOutputTypeDef
]
FilledMapConditionalFormattingOutputTypeDef = TypedDict(
    "FilledMapConditionalFormattingOutputTypeDef",
    {
        "ConditionalFormattingOptions": List[FilledMapConditionalFormattingOptionOutputTypeDef],
    },
)
PivotTableConditionalFormattingOutputTypeDef = TypedDict(
    "PivotTableConditionalFormattingOutputTypeDef",
    {
        "ConditionalFormattingOptions": NotRequired[
            List[PivotTableConditionalFormattingOptionOutputTypeDef]
        ],
    },
)
TableConditionalFormattingOutputTypeDef = TypedDict(
    "TableConditionalFormattingOutputTypeDef",
    {
        "ConditionalFormattingOptions": NotRequired[
            List[TableConditionalFormattingOptionOutputTypeDef]
        ],
    },
)
GaugeChartArcConditionalFormattingTypeDef = TypedDict(
    "GaugeChartArcConditionalFormattingTypeDef",
    {
        "ForegroundColor": NotRequired[ConditionalFormattingColorUnionTypeDef],
    },
)
GaugeChartPrimaryValueConditionalFormattingTypeDef = TypedDict(
    "GaugeChartPrimaryValueConditionalFormattingTypeDef",
    {
        "TextColor": NotRequired[ConditionalFormattingColorUnionTypeDef],
        "Icon": NotRequired[ConditionalFormattingIconTypeDef],
    },
)
KPIActualValueConditionalFormattingTypeDef = TypedDict(
    "KPIActualValueConditionalFormattingTypeDef",
    {
        "TextColor": NotRequired[ConditionalFormattingColorUnionTypeDef],
        "Icon": NotRequired[ConditionalFormattingIconTypeDef],
    },
)
KPIComparisonValueConditionalFormattingTypeDef = TypedDict(
    "KPIComparisonValueConditionalFormattingTypeDef",
    {
        "TextColor": NotRequired[ConditionalFormattingColorUnionTypeDef],
        "Icon": NotRequired[ConditionalFormattingIconTypeDef],
    },
)
KPIPrimaryValueConditionalFormattingTypeDef = TypedDict(
    "KPIPrimaryValueConditionalFormattingTypeDef",
    {
        "TextColor": NotRequired[ConditionalFormattingColorUnionTypeDef],
        "Icon": NotRequired[ConditionalFormattingIconTypeDef],
    },
)
KPIProgressBarConditionalFormattingTypeDef = TypedDict(
    "KPIProgressBarConditionalFormattingTypeDef",
    {
        "ForegroundColor": NotRequired[ConditionalFormattingColorUnionTypeDef],
    },
)
ShapeConditionalFormatTypeDef = TypedDict(
    "ShapeConditionalFormatTypeDef",
    {
        "BackgroundColor": ConditionalFormattingColorUnionTypeDef,
    },
)
TableRowConditionalFormattingTypeDef = TypedDict(
    "TableRowConditionalFormattingTypeDef",
    {
        "BackgroundColor": NotRequired[ConditionalFormattingColorUnionTypeDef],
        "TextColor": NotRequired[ConditionalFormattingColorUnionTypeDef],
    },
)
TextConditionalFormatTypeDef = TypedDict(
    "TextConditionalFormatTypeDef",
    {
        "BackgroundColor": NotRequired[ConditionalFormattingColorUnionTypeDef],
        "TextColor": NotRequired[ConditionalFormattingColorUnionTypeDef],
        "Icon": NotRequired[ConditionalFormattingIconTypeDef],
    },
)
SheetControlLayoutUnionTypeDef = Union[SheetControlLayoutTypeDef, SheetControlLayoutOutputTypeDef]
UniqueValuesComputationTypeDef = TypedDict(
    "UniqueValuesComputationTypeDef",
    {
        "ComputationId": str,
        "Name": NotRequired[str],
        "Category": NotRequired[DimensionFieldTypeDef],
    },
)
BarChartAggregatedFieldWellsOutputTypeDef = TypedDict(
    "BarChartAggregatedFieldWellsOutputTypeDef",
    {
        "Category": NotRequired[List[DimensionFieldTypeDef]],
        "Values": NotRequired[List[MeasureFieldTypeDef]],
        "Colors": NotRequired[List[DimensionFieldTypeDef]],
        "SmallMultiples": NotRequired[List[DimensionFieldTypeDef]],
    },
)
BarChartAggregatedFieldWellsTypeDef = TypedDict(
    "BarChartAggregatedFieldWellsTypeDef",
    {
        "Category": NotRequired[Sequence[DimensionFieldTypeDef]],
        "Values": NotRequired[Sequence[MeasureFieldTypeDef]],
        "Colors": NotRequired[Sequence[DimensionFieldTypeDef]],
        "SmallMultiples": NotRequired[Sequence[DimensionFieldTypeDef]],
    },
)
BoxPlotAggregatedFieldWellsOutputTypeDef = TypedDict(
    "BoxPlotAggregatedFieldWellsOutputTypeDef",
    {
        "GroupBy": NotRequired[List[DimensionFieldTypeDef]],
        "Values": NotRequired[List[MeasureFieldTypeDef]],
    },
)
BoxPlotAggregatedFieldWellsTypeDef = TypedDict(
    "BoxPlotAggregatedFieldWellsTypeDef",
    {
        "GroupBy": NotRequired[Sequence[DimensionFieldTypeDef]],
        "Values": NotRequired[Sequence[MeasureFieldTypeDef]],
    },
)
ComboChartAggregatedFieldWellsOutputTypeDef = TypedDict(
    "ComboChartAggregatedFieldWellsOutputTypeDef",
    {
        "Category": NotRequired[List[DimensionFieldTypeDef]],
        "BarValues": NotRequired[List[MeasureFieldTypeDef]],
        "Colors": NotRequired[List[DimensionFieldTypeDef]],
        "LineValues": NotRequired[List[MeasureFieldTypeDef]],
    },
)
ComboChartAggregatedFieldWellsTypeDef = TypedDict(
    "ComboChartAggregatedFieldWellsTypeDef",
    {
        "Category": NotRequired[Sequence[DimensionFieldTypeDef]],
        "BarValues": NotRequired[Sequence[MeasureFieldTypeDef]],
        "Colors": NotRequired[Sequence[DimensionFieldTypeDef]],
        "LineValues": NotRequired[Sequence[MeasureFieldTypeDef]],
    },
)
FilledMapAggregatedFieldWellsOutputTypeDef = TypedDict(
    "FilledMapAggregatedFieldWellsOutputTypeDef",
    {
        "Geospatial": NotRequired[List[DimensionFieldTypeDef]],
        "Values": NotRequired[List[MeasureFieldTypeDef]],
    },
)
FilledMapAggregatedFieldWellsTypeDef = TypedDict(
    "FilledMapAggregatedFieldWellsTypeDef",
    {
        "Geospatial": NotRequired[Sequence[DimensionFieldTypeDef]],
        "Values": NotRequired[Sequence[MeasureFieldTypeDef]],
    },
)
ForecastComputationTypeDef = TypedDict(
    "ForecastComputationTypeDef",
    {
        "ComputationId": str,
        "Name": NotRequired[str],
        "Time": NotRequired[DimensionFieldTypeDef],
        "Value": NotRequired[MeasureFieldTypeDef],
        "PeriodsForward": NotRequired[int],
        "PeriodsBackward": NotRequired[int],
        "UpperBoundary": NotRequired[float],
        "LowerBoundary": NotRequired[float],
        "PredictionInterval": NotRequired[int],
        "Seasonality": NotRequired[ForecastComputationSeasonalityType],
        "CustomSeasonalityValue": NotRequired[int],
    },
)
FunnelChartAggregatedFieldWellsOutputTypeDef = TypedDict(
    "FunnelChartAggregatedFieldWellsOutputTypeDef",
    {
        "Category": NotRequired[List[DimensionFieldTypeDef]],
        "Values": NotRequired[List[MeasureFieldTypeDef]],
    },
)
FunnelChartAggregatedFieldWellsTypeDef = TypedDict(
    "FunnelChartAggregatedFieldWellsTypeDef",
    {
        "Category": NotRequired[Sequence[DimensionFieldTypeDef]],
        "Values": NotRequired[Sequence[MeasureFieldTypeDef]],
    },
)
GaugeChartFieldWellsOutputTypeDef = TypedDict(
    "GaugeChartFieldWellsOutputTypeDef",
    {
        "Values": NotRequired[List[MeasureFieldTypeDef]],
        "TargetValues": NotRequired[List[MeasureFieldTypeDef]],
    },
)
GaugeChartFieldWellsTypeDef = TypedDict(
    "GaugeChartFieldWellsTypeDef",
    {
        "Values": NotRequired[Sequence[MeasureFieldTypeDef]],
        "TargetValues": NotRequired[Sequence[MeasureFieldTypeDef]],
    },
)
GeospatialMapAggregatedFieldWellsOutputTypeDef = TypedDict(
    "GeospatialMapAggregatedFieldWellsOutputTypeDef",
    {
        "Geospatial": NotRequired[List[DimensionFieldTypeDef]],
        "Values": NotRequired[List[MeasureFieldTypeDef]],
        "Colors": NotRequired[List[DimensionFieldTypeDef]],
    },
)
GeospatialMapAggregatedFieldWellsTypeDef = TypedDict(
    "GeospatialMapAggregatedFieldWellsTypeDef",
    {
        "Geospatial": NotRequired[Sequence[DimensionFieldTypeDef]],
        "Values": NotRequired[Sequence[MeasureFieldTypeDef]],
        "Colors": NotRequired[Sequence[DimensionFieldTypeDef]],
    },
)
GrowthRateComputationTypeDef = TypedDict(
    "GrowthRateComputationTypeDef",
    {
        "ComputationId": str,
        "Name": NotRequired[str],
        "Time": NotRequired[DimensionFieldTypeDef],
        "Value": NotRequired[MeasureFieldTypeDef],
        "PeriodSize": NotRequired[int],
    },
)
HeatMapAggregatedFieldWellsOutputTypeDef = TypedDict(
    "HeatMapAggregatedFieldWellsOutputTypeDef",
    {
        "Rows": NotRequired[List[DimensionFieldTypeDef]],
        "Columns": NotRequired[List[DimensionFieldTypeDef]],
        "Values": NotRequired[List[MeasureFieldTypeDef]],
    },
)
HeatMapAggregatedFieldWellsTypeDef = TypedDict(
    "HeatMapAggregatedFieldWellsTypeDef",
    {
        "Rows": NotRequired[Sequence[DimensionFieldTypeDef]],
        "Columns": NotRequired[Sequence[DimensionFieldTypeDef]],
        "Values": NotRequired[Sequence[MeasureFieldTypeDef]],
    },
)
HistogramAggregatedFieldWellsOutputTypeDef = TypedDict(
    "HistogramAggregatedFieldWellsOutputTypeDef",
    {
        "Values": NotRequired[List[MeasureFieldTypeDef]],
    },
)
HistogramAggregatedFieldWellsTypeDef = TypedDict(
    "HistogramAggregatedFieldWellsTypeDef",
    {
        "Values": NotRequired[Sequence[MeasureFieldTypeDef]],
    },
)
KPIFieldWellsOutputTypeDef = TypedDict(
    "KPIFieldWellsOutputTypeDef",
    {
        "Values": NotRequired[List[MeasureFieldTypeDef]],
        "TargetValues": NotRequired[List[MeasureFieldTypeDef]],
        "TrendGroups": NotRequired[List[DimensionFieldTypeDef]],
    },
)
KPIFieldWellsTypeDef = TypedDict(
    "KPIFieldWellsTypeDef",
    {
        "Values": NotRequired[Sequence[MeasureFieldTypeDef]],
        "TargetValues": NotRequired[Sequence[MeasureFieldTypeDef]],
        "TrendGroups": NotRequired[Sequence[DimensionFieldTypeDef]],
    },
)
LineChartAggregatedFieldWellsOutputTypeDef = TypedDict(
    "LineChartAggregatedFieldWellsOutputTypeDef",
    {
        "Category": NotRequired[List[DimensionFieldTypeDef]],
        "Values": NotRequired[List[MeasureFieldTypeDef]],
        "Colors": NotRequired[List[DimensionFieldTypeDef]],
        "SmallMultiples": NotRequired[List[DimensionFieldTypeDef]],
    },
)
LineChartAggregatedFieldWellsTypeDef = TypedDict(
    "LineChartAggregatedFieldWellsTypeDef",
    {
        "Category": NotRequired[Sequence[DimensionFieldTypeDef]],
        "Values": NotRequired[Sequence[MeasureFieldTypeDef]],
        "Colors": NotRequired[Sequence[DimensionFieldTypeDef]],
        "SmallMultiples": NotRequired[Sequence[DimensionFieldTypeDef]],
    },
)
MaximumMinimumComputationTypeDef = TypedDict(
    "MaximumMinimumComputationTypeDef",
    {
        "ComputationId": str,
        "Type": MaximumMinimumComputationTypeType,
        "Name": NotRequired[str],
        "Time": NotRequired[DimensionFieldTypeDef],
        "Value": NotRequired[MeasureFieldTypeDef],
    },
)
MetricComparisonComputationTypeDef = TypedDict(
    "MetricComparisonComputationTypeDef",
    {
        "ComputationId": str,
        "Name": NotRequired[str],
        "Time": NotRequired[DimensionFieldTypeDef],
        "FromValue": NotRequired[MeasureFieldTypeDef],
        "TargetValue": NotRequired[MeasureFieldTypeDef],
    },
)
PeriodOverPeriodComputationTypeDef = TypedDict(
    "PeriodOverPeriodComputationTypeDef",
    {
        "ComputationId": str,
        "Name": NotRequired[str],
        "Time": NotRequired[DimensionFieldTypeDef],
        "Value": NotRequired[MeasureFieldTypeDef],
    },
)
PeriodToDateComputationTypeDef = TypedDict(
    "PeriodToDateComputationTypeDef",
    {
        "ComputationId": str,
        "Name": NotRequired[str],
        "Time": NotRequired[DimensionFieldTypeDef],
        "Value": NotRequired[MeasureFieldTypeDef],
        "PeriodTimeGranularity": NotRequired[TimeGranularityType],
    },
)
PieChartAggregatedFieldWellsOutputTypeDef = TypedDict(
    "PieChartAggregatedFieldWellsOutputTypeDef",
    {
        "Category": NotRequired[List[DimensionFieldTypeDef]],
        "Values": NotRequired[List[MeasureFieldTypeDef]],
        "SmallMultiples": NotRequired[List[DimensionFieldTypeDef]],
    },
)
PieChartAggregatedFieldWellsTypeDef = TypedDict(
    "PieChartAggregatedFieldWellsTypeDef",
    {
        "Category": NotRequired[Sequence[DimensionFieldTypeDef]],
        "Values": NotRequired[Sequence[MeasureFieldTypeDef]],
        "SmallMultiples": NotRequired[Sequence[DimensionFieldTypeDef]],
    },
)
PivotTableAggregatedFieldWellsOutputTypeDef = TypedDict(
    "PivotTableAggregatedFieldWellsOutputTypeDef",
    {
        "Rows": NotRequired[List[DimensionFieldTypeDef]],
        "Columns": NotRequired[List[DimensionFieldTypeDef]],
        "Values": NotRequired[List[MeasureFieldTypeDef]],
    },
)
PivotTableAggregatedFieldWellsTypeDef = TypedDict(
    "PivotTableAggregatedFieldWellsTypeDef",
    {
        "Rows": NotRequired[Sequence[DimensionFieldTypeDef]],
        "Columns": NotRequired[Sequence[DimensionFieldTypeDef]],
        "Values": NotRequired[Sequence[MeasureFieldTypeDef]],
    },
)
RadarChartAggregatedFieldWellsOutputTypeDef = TypedDict(
    "RadarChartAggregatedFieldWellsOutputTypeDef",
    {
        "Category": NotRequired[List[DimensionFieldTypeDef]],
        "Color": NotRequired[List[DimensionFieldTypeDef]],
        "Values": NotRequired[List[MeasureFieldTypeDef]],
    },
)
RadarChartAggregatedFieldWellsTypeDef = TypedDict(
    "RadarChartAggregatedFieldWellsTypeDef",
    {
        "Category": NotRequired[Sequence[DimensionFieldTypeDef]],
        "Color": NotRequired[Sequence[DimensionFieldTypeDef]],
        "Values": NotRequired[Sequence[MeasureFieldTypeDef]],
    },
)
SankeyDiagramAggregatedFieldWellsOutputTypeDef = TypedDict(
    "SankeyDiagramAggregatedFieldWellsOutputTypeDef",
    {
        "Source": NotRequired[List[DimensionFieldTypeDef]],
        "Destination": NotRequired[List[DimensionFieldTypeDef]],
        "Weight": NotRequired[List[MeasureFieldTypeDef]],
    },
)
SankeyDiagramAggregatedFieldWellsTypeDef = TypedDict(
    "SankeyDiagramAggregatedFieldWellsTypeDef",
    {
        "Source": NotRequired[Sequence[DimensionFieldTypeDef]],
        "Destination": NotRequired[Sequence[DimensionFieldTypeDef]],
        "Weight": NotRequired[Sequence[MeasureFieldTypeDef]],
    },
)
ScatterPlotCategoricallyAggregatedFieldWellsOutputTypeDef = TypedDict(
    "ScatterPlotCategoricallyAggregatedFieldWellsOutputTypeDef",
    {
        "XAxis": NotRequired[List[MeasureFieldTypeDef]],
        "YAxis": NotRequired[List[MeasureFieldTypeDef]],
        "Category": NotRequired[List[DimensionFieldTypeDef]],
        "Size": NotRequired[List[MeasureFieldTypeDef]],
        "Label": NotRequired[List[DimensionFieldTypeDef]],
    },
)
ScatterPlotCategoricallyAggregatedFieldWellsTypeDef = TypedDict(
    "ScatterPlotCategoricallyAggregatedFieldWellsTypeDef",
    {
        "XAxis": NotRequired[Sequence[MeasureFieldTypeDef]],
        "YAxis": NotRequired[Sequence[MeasureFieldTypeDef]],
        "Category": NotRequired[Sequence[DimensionFieldTypeDef]],
        "Size": NotRequired[Sequence[MeasureFieldTypeDef]],
        "Label": NotRequired[Sequence[DimensionFieldTypeDef]],
    },
)
ScatterPlotUnaggregatedFieldWellsOutputTypeDef = TypedDict(
    "ScatterPlotUnaggregatedFieldWellsOutputTypeDef",
    {
        "XAxis": NotRequired[List[DimensionFieldTypeDef]],
        "YAxis": NotRequired[List[DimensionFieldTypeDef]],
        "Size": NotRequired[List[MeasureFieldTypeDef]],
        "Category": NotRequired[List[DimensionFieldTypeDef]],
        "Label": NotRequired[List[DimensionFieldTypeDef]],
    },
)
ScatterPlotUnaggregatedFieldWellsTypeDef = TypedDict(
    "ScatterPlotUnaggregatedFieldWellsTypeDef",
    {
        "XAxis": NotRequired[Sequence[DimensionFieldTypeDef]],
        "YAxis": NotRequired[Sequence[DimensionFieldTypeDef]],
        "Size": NotRequired[Sequence[MeasureFieldTypeDef]],
        "Category": NotRequired[Sequence[DimensionFieldTypeDef]],
        "Label": NotRequired[Sequence[DimensionFieldTypeDef]],
    },
)
TableAggregatedFieldWellsOutputTypeDef = TypedDict(
    "TableAggregatedFieldWellsOutputTypeDef",
    {
        "GroupBy": NotRequired[List[DimensionFieldTypeDef]],
        "Values": NotRequired[List[MeasureFieldTypeDef]],
    },
)
TableAggregatedFieldWellsTypeDef = TypedDict(
    "TableAggregatedFieldWellsTypeDef",
    {
        "GroupBy": NotRequired[Sequence[DimensionFieldTypeDef]],
        "Values": NotRequired[Sequence[MeasureFieldTypeDef]],
    },
)
TopBottomMoversComputationTypeDef = TypedDict(
    "TopBottomMoversComputationTypeDef",
    {
        "ComputationId": str,
        "Type": TopBottomComputationTypeType,
        "Name": NotRequired[str],
        "Time": NotRequired[DimensionFieldTypeDef],
        "Category": NotRequired[DimensionFieldTypeDef],
        "Value": NotRequired[MeasureFieldTypeDef],
        "MoverSize": NotRequired[int],
        "SortOrder": NotRequired[TopBottomSortOrderType],
    },
)
TopBottomRankedComputationTypeDef = TypedDict(
    "TopBottomRankedComputationTypeDef",
    {
        "ComputationId": str,
        "Type": TopBottomComputationTypeType,
        "Name": NotRequired[str],
        "Category": NotRequired[DimensionFieldTypeDef],
        "Value": NotRequired[MeasureFieldTypeDef],
        "ResultSize": NotRequired[int],
    },
)
TotalAggregationComputationTypeDef = TypedDict(
    "TotalAggregationComputationTypeDef",
    {
        "ComputationId": str,
        "Name": NotRequired[str],
        "Value": NotRequired[MeasureFieldTypeDef],
    },
)
TreeMapAggregatedFieldWellsOutputTypeDef = TypedDict(
    "TreeMapAggregatedFieldWellsOutputTypeDef",
    {
        "Groups": NotRequired[List[DimensionFieldTypeDef]],
        "Sizes": NotRequired[List[MeasureFieldTypeDef]],
        "Colors": NotRequired[List[MeasureFieldTypeDef]],
    },
)
TreeMapAggregatedFieldWellsTypeDef = TypedDict(
    "TreeMapAggregatedFieldWellsTypeDef",
    {
        "Groups": NotRequired[Sequence[DimensionFieldTypeDef]],
        "Sizes": NotRequired[Sequence[MeasureFieldTypeDef]],
        "Colors": NotRequired[Sequence[MeasureFieldTypeDef]],
    },
)
WaterfallChartAggregatedFieldWellsOutputTypeDef = TypedDict(
    "WaterfallChartAggregatedFieldWellsOutputTypeDef",
    {
        "Categories": NotRequired[List[DimensionFieldTypeDef]],
        "Values": NotRequired[List[MeasureFieldTypeDef]],
        "Breakdowns": NotRequired[List[DimensionFieldTypeDef]],
    },
)
WaterfallChartAggregatedFieldWellsTypeDef = TypedDict(
    "WaterfallChartAggregatedFieldWellsTypeDef",
    {
        "Categories": NotRequired[Sequence[DimensionFieldTypeDef]],
        "Values": NotRequired[Sequence[MeasureFieldTypeDef]],
        "Breakdowns": NotRequired[Sequence[DimensionFieldTypeDef]],
    },
)
WordCloudAggregatedFieldWellsOutputTypeDef = TypedDict(
    "WordCloudAggregatedFieldWellsOutputTypeDef",
    {
        "GroupBy": NotRequired[List[DimensionFieldTypeDef]],
        "Size": NotRequired[List[MeasureFieldTypeDef]],
    },
)
WordCloudAggregatedFieldWellsTypeDef = TypedDict(
    "WordCloudAggregatedFieldWellsTypeDef",
    {
        "GroupBy": NotRequired[Sequence[DimensionFieldTypeDef]],
        "Size": NotRequired[Sequence[MeasureFieldTypeDef]],
    },
)
ColumnConfigurationUnionTypeDef = Union[
    ColumnConfigurationTypeDef, ColumnConfigurationOutputTypeDef
]
TableUnaggregatedFieldWellsOutputTypeDef = TypedDict(
    "TableUnaggregatedFieldWellsOutputTypeDef",
    {
        "Values": NotRequired[List[UnaggregatedFieldTypeDef]],
    },
)
TableUnaggregatedFieldWellsTypeDef = TypedDict(
    "TableUnaggregatedFieldWellsTypeDef",
    {
        "Values": NotRequired[Sequence[UnaggregatedFieldTypeDef]],
    },
)
BodySectionConfigurationOutputTypeDef = TypedDict(
    "BodySectionConfigurationOutputTypeDef",
    {
        "SectionId": str,
        "Content": BodySectionContentOutputTypeDef,
        "Style": NotRequired[SectionStyleTypeDef],
        "PageBreakConfiguration": NotRequired[SectionPageBreakConfigurationTypeDef],
        "RepeatConfiguration": NotRequired[BodySectionRepeatConfigurationOutputTypeDef],
    },
)
BodySectionRepeatDimensionConfigurationUnionTypeDef = Union[
    BodySectionRepeatDimensionConfigurationTypeDef,
    BodySectionRepeatDimensionConfigurationOutputTypeDef,
]
PivotFieldSortOptionsUnionTypeDef = Union[
    PivotFieldSortOptionsTypeDef, PivotFieldSortOptionsOutputTypeDef
]
TooltipOptionsTypeDef = TypedDict(
    "TooltipOptionsTypeDef",
    {
        "TooltipVisibility": NotRequired[VisibilityType],
        "SelectedTooltipType": NotRequired[SelectedTooltipTypeType],
        "FieldBasedTooltip": NotRequired[FieldBasedTooltipUnionTypeDef],
    },
)
AssetBundleImportJobDataSourceOverrideParametersUnionTypeDef = Union[
    AssetBundleImportJobDataSourceOverrideParametersTypeDef,
    AssetBundleImportJobDataSourceOverrideParametersOutputTypeDef,
]
DataSourceCredentialsTypeDef = TypedDict(
    "DataSourceCredentialsTypeDef",
    {
        "CredentialPair": NotRequired[CredentialPairTypeDef],
        "CopySourceArn": NotRequired[str],
        "SecretArn": NotRequired[str],
    },
)
SectionLayoutConfigurationUnionTypeDef = Union[
    SectionLayoutConfigurationTypeDef, SectionLayoutConfigurationOutputTypeDef
]
StartDashboardSnapshotJobRequestRequestTypeDef = TypedDict(
    "StartDashboardSnapshotJobRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "SnapshotJobId": str,
        "UserConfiguration": SnapshotUserConfigurationTypeDef,
        "SnapshotConfiguration": SnapshotConfigurationTypeDef,
    },
)
SetParameterValueConfigurationUnionTypeDef = Union[
    SetParameterValueConfigurationTypeDef, SetParameterValueConfigurationOutputTypeDef
]
LogicalTableUnionTypeDef = Union[LogicalTableTypeDef, LogicalTableOutputTypeDef]
UpdateDataSetRequestRequestTypeDef = TypedDict(
    "UpdateDataSetRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
        "Name": str,
        "PhysicalTableMap": Mapping[str, PhysicalTableTypeDef],
        "ImportMode": DataSetImportModeType,
        "LogicalTableMap": NotRequired[Mapping[str, LogicalTableTypeDef]],
        "ColumnGroups": NotRequired[Sequence[ColumnGroupTypeDef]],
        "FieldFolders": NotRequired[Mapping[str, FieldFolderTypeDef]],
        "RowLevelPermissionDataSet": NotRequired[RowLevelPermissionDataSetTypeDef],
        "RowLevelPermissionTagConfiguration": NotRequired[
            RowLevelPermissionTagConfigurationTypeDef
        ],
        "ColumnLevelPermissionRules": NotRequired[Sequence[ColumnLevelPermissionRuleTypeDef]],
        "DataSetUsageConfiguration": NotRequired[DataSetUsageConfigurationTypeDef],
        "DatasetParameters": NotRequired[Sequence[DatasetParameterTypeDef]],
    },
)
ColumnHierarchyUnionTypeDef = Union[ColumnHierarchyTypeDef, ColumnHierarchyOutputTypeDef]
AxisDisplayOptionsUnionTypeDef = Union[AxisDisplayOptionsTypeDef, AxisDisplayOptionsOutputTypeDef]
TopicIRContributionAnalysisUnionTypeDef = Union[
    TopicIRContributionAnalysisTypeDef, TopicIRContributionAnalysisOutputTypeDef
]
DatasetMetadataTypeDef = TypedDict(
    "DatasetMetadataTypeDef",
    {
        "DatasetArn": str,
        "DatasetName": NotRequired[str],
        "DatasetDescription": NotRequired[str],
        "DataAggregation": NotRequired[DataAggregationTypeDef],
        "Filters": NotRequired[Sequence[TopicFilterUnionTypeDef]],
        "Columns": NotRequired[Sequence[TopicColumnUnionTypeDef]],
        "CalculatedFields": NotRequired[Sequence[TopicCalculatedFieldUnionTypeDef]],
        "NamedEntities": NotRequired[Sequence[TopicNamedEntityUnionTypeDef]],
    },
)
ListTopicReviewedAnswersResponseTypeDef = TypedDict(
    "ListTopicReviewedAnswersResponseTypeDef",
    {
        "TopicId": str,
        "TopicArn": str,
        "Answers": List[TopicReviewedAnswerTypeDef],
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DefaultFilterControlConfigurationTypeDef = TypedDict(
    "DefaultFilterControlConfigurationTypeDef",
    {
        "Title": str,
        "ControlOptions": DefaultFilterControlOptionsUnionTypeDef,
    },
)
InnerFilterOutputTypeDef = TypedDict(
    "InnerFilterOutputTypeDef",
    {
        "CategoryInnerFilter": NotRequired[CategoryInnerFilterOutputTypeDef],
    },
)
TableFieldOptionsUnionTypeDef = Union[TableFieldOptionsTypeDef, TableFieldOptionsOutputTypeDef]
GaugeChartArcConditionalFormattingUnionTypeDef = Union[
    GaugeChartArcConditionalFormattingTypeDef, GaugeChartArcConditionalFormattingOutputTypeDef
]
GaugeChartPrimaryValueConditionalFormattingUnionTypeDef = Union[
    GaugeChartPrimaryValueConditionalFormattingTypeDef,
    GaugeChartPrimaryValueConditionalFormattingOutputTypeDef,
]
KPIActualValueConditionalFormattingUnionTypeDef = Union[
    KPIActualValueConditionalFormattingTypeDef, KPIActualValueConditionalFormattingOutputTypeDef
]
KPIComparisonValueConditionalFormattingUnionTypeDef = Union[
    KPIComparisonValueConditionalFormattingTypeDef,
    KPIComparisonValueConditionalFormattingOutputTypeDef,
]
KPIPrimaryValueConditionalFormattingUnionTypeDef = Union[
    KPIPrimaryValueConditionalFormattingTypeDef, KPIPrimaryValueConditionalFormattingOutputTypeDef
]
KPIProgressBarConditionalFormattingUnionTypeDef = Union[
    KPIProgressBarConditionalFormattingTypeDef, KPIProgressBarConditionalFormattingOutputTypeDef
]
ShapeConditionalFormatUnionTypeDef = Union[
    ShapeConditionalFormatTypeDef, ShapeConditionalFormatOutputTypeDef
]
TableRowConditionalFormattingUnionTypeDef = Union[
    TableRowConditionalFormattingTypeDef, TableRowConditionalFormattingOutputTypeDef
]
TextConditionalFormatUnionTypeDef = Union[
    TextConditionalFormatTypeDef, TextConditionalFormatOutputTypeDef
]
BarChartFieldWellsOutputTypeDef = TypedDict(
    "BarChartFieldWellsOutputTypeDef",
    {
        "BarChartAggregatedFieldWells": NotRequired[BarChartAggregatedFieldWellsOutputTypeDef],
    },
)
BarChartAggregatedFieldWellsUnionTypeDef = Union[
    BarChartAggregatedFieldWellsTypeDef, BarChartAggregatedFieldWellsOutputTypeDef
]
BoxPlotFieldWellsOutputTypeDef = TypedDict(
    "BoxPlotFieldWellsOutputTypeDef",
    {
        "BoxPlotAggregatedFieldWells": NotRequired[BoxPlotAggregatedFieldWellsOutputTypeDef],
    },
)
BoxPlotAggregatedFieldWellsUnionTypeDef = Union[
    BoxPlotAggregatedFieldWellsTypeDef, BoxPlotAggregatedFieldWellsOutputTypeDef
]
ComboChartFieldWellsOutputTypeDef = TypedDict(
    "ComboChartFieldWellsOutputTypeDef",
    {
        "ComboChartAggregatedFieldWells": NotRequired[ComboChartAggregatedFieldWellsOutputTypeDef],
    },
)
ComboChartAggregatedFieldWellsUnionTypeDef = Union[
    ComboChartAggregatedFieldWellsTypeDef, ComboChartAggregatedFieldWellsOutputTypeDef
]
FilledMapFieldWellsOutputTypeDef = TypedDict(
    "FilledMapFieldWellsOutputTypeDef",
    {
        "FilledMapAggregatedFieldWells": NotRequired[FilledMapAggregatedFieldWellsOutputTypeDef],
    },
)
FilledMapAggregatedFieldWellsUnionTypeDef = Union[
    FilledMapAggregatedFieldWellsTypeDef, FilledMapAggregatedFieldWellsOutputTypeDef
]
FunnelChartFieldWellsOutputTypeDef = TypedDict(
    "FunnelChartFieldWellsOutputTypeDef",
    {
        "FunnelChartAggregatedFieldWells": NotRequired[
            FunnelChartAggregatedFieldWellsOutputTypeDef
        ],
    },
)
FunnelChartAggregatedFieldWellsUnionTypeDef = Union[
    FunnelChartAggregatedFieldWellsTypeDef, FunnelChartAggregatedFieldWellsOutputTypeDef
]
GaugeChartConfigurationOutputTypeDef = TypedDict(
    "GaugeChartConfigurationOutputTypeDef",
    {
        "FieldWells": NotRequired[GaugeChartFieldWellsOutputTypeDef],
        "GaugeChartOptions": NotRequired[GaugeChartOptionsTypeDef],
        "DataLabels": NotRequired[DataLabelOptionsOutputTypeDef],
        "TooltipOptions": NotRequired[TooltipOptionsOutputTypeDef],
        "VisualPalette": NotRequired[VisualPaletteOutputTypeDef],
        "ColorConfiguration": NotRequired[GaugeChartColorConfigurationTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
GaugeChartFieldWellsUnionTypeDef = Union[
    GaugeChartFieldWellsTypeDef, GaugeChartFieldWellsOutputTypeDef
]
GeospatialMapFieldWellsOutputTypeDef = TypedDict(
    "GeospatialMapFieldWellsOutputTypeDef",
    {
        "GeospatialMapAggregatedFieldWells": NotRequired[
            GeospatialMapAggregatedFieldWellsOutputTypeDef
        ],
    },
)
GeospatialMapAggregatedFieldWellsUnionTypeDef = Union[
    GeospatialMapAggregatedFieldWellsTypeDef, GeospatialMapAggregatedFieldWellsOutputTypeDef
]
HeatMapFieldWellsOutputTypeDef = TypedDict(
    "HeatMapFieldWellsOutputTypeDef",
    {
        "HeatMapAggregatedFieldWells": NotRequired[HeatMapAggregatedFieldWellsOutputTypeDef],
    },
)
HeatMapAggregatedFieldWellsUnionTypeDef = Union[
    HeatMapAggregatedFieldWellsTypeDef, HeatMapAggregatedFieldWellsOutputTypeDef
]
HistogramFieldWellsOutputTypeDef = TypedDict(
    "HistogramFieldWellsOutputTypeDef",
    {
        "HistogramAggregatedFieldWells": NotRequired[HistogramAggregatedFieldWellsOutputTypeDef],
    },
)
HistogramAggregatedFieldWellsUnionTypeDef = Union[
    HistogramAggregatedFieldWellsTypeDef, HistogramAggregatedFieldWellsOutputTypeDef
]
KPIConfigurationOutputTypeDef = TypedDict(
    "KPIConfigurationOutputTypeDef",
    {
        "FieldWells": NotRequired[KPIFieldWellsOutputTypeDef],
        "SortConfiguration": NotRequired[KPISortConfigurationOutputTypeDef],
        "KPIOptions": NotRequired[KPIOptionsTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
KPIFieldWellsUnionTypeDef = Union[KPIFieldWellsTypeDef, KPIFieldWellsOutputTypeDef]
LineChartFieldWellsOutputTypeDef = TypedDict(
    "LineChartFieldWellsOutputTypeDef",
    {
        "LineChartAggregatedFieldWells": NotRequired[LineChartAggregatedFieldWellsOutputTypeDef],
    },
)
LineChartAggregatedFieldWellsUnionTypeDef = Union[
    LineChartAggregatedFieldWellsTypeDef, LineChartAggregatedFieldWellsOutputTypeDef
]
PieChartFieldWellsOutputTypeDef = TypedDict(
    "PieChartFieldWellsOutputTypeDef",
    {
        "PieChartAggregatedFieldWells": NotRequired[PieChartAggregatedFieldWellsOutputTypeDef],
    },
)
PieChartAggregatedFieldWellsUnionTypeDef = Union[
    PieChartAggregatedFieldWellsTypeDef, PieChartAggregatedFieldWellsOutputTypeDef
]
PivotTableFieldWellsOutputTypeDef = TypedDict(
    "PivotTableFieldWellsOutputTypeDef",
    {
        "PivotTableAggregatedFieldWells": NotRequired[PivotTableAggregatedFieldWellsOutputTypeDef],
    },
)
PivotTableAggregatedFieldWellsUnionTypeDef = Union[
    PivotTableAggregatedFieldWellsTypeDef, PivotTableAggregatedFieldWellsOutputTypeDef
]
RadarChartFieldWellsOutputTypeDef = TypedDict(
    "RadarChartFieldWellsOutputTypeDef",
    {
        "RadarChartAggregatedFieldWells": NotRequired[RadarChartAggregatedFieldWellsOutputTypeDef],
    },
)
RadarChartAggregatedFieldWellsUnionTypeDef = Union[
    RadarChartAggregatedFieldWellsTypeDef, RadarChartAggregatedFieldWellsOutputTypeDef
]
SankeyDiagramFieldWellsOutputTypeDef = TypedDict(
    "SankeyDiagramFieldWellsOutputTypeDef",
    {
        "SankeyDiagramAggregatedFieldWells": NotRequired[
            SankeyDiagramAggregatedFieldWellsOutputTypeDef
        ],
    },
)
SankeyDiagramAggregatedFieldWellsUnionTypeDef = Union[
    SankeyDiagramAggregatedFieldWellsTypeDef, SankeyDiagramAggregatedFieldWellsOutputTypeDef
]
ScatterPlotCategoricallyAggregatedFieldWellsUnionTypeDef = Union[
    ScatterPlotCategoricallyAggregatedFieldWellsTypeDef,
    ScatterPlotCategoricallyAggregatedFieldWellsOutputTypeDef,
]
ScatterPlotFieldWellsOutputTypeDef = TypedDict(
    "ScatterPlotFieldWellsOutputTypeDef",
    {
        "ScatterPlotCategoricallyAggregatedFieldWells": NotRequired[
            ScatterPlotCategoricallyAggregatedFieldWellsOutputTypeDef
        ],
        "ScatterPlotUnaggregatedFieldWells": NotRequired[
            ScatterPlotUnaggregatedFieldWellsOutputTypeDef
        ],
    },
)
ScatterPlotUnaggregatedFieldWellsUnionTypeDef = Union[
    ScatterPlotUnaggregatedFieldWellsTypeDef, ScatterPlotUnaggregatedFieldWellsOutputTypeDef
]
TableAggregatedFieldWellsUnionTypeDef = Union[
    TableAggregatedFieldWellsTypeDef, TableAggregatedFieldWellsOutputTypeDef
]
ComputationTypeDef = TypedDict(
    "ComputationTypeDef",
    {
        "TopBottomRanked": NotRequired[TopBottomRankedComputationTypeDef],
        "TopBottomMovers": NotRequired[TopBottomMoversComputationTypeDef],
        "TotalAggregation": NotRequired[TotalAggregationComputationTypeDef],
        "MaximumMinimum": NotRequired[MaximumMinimumComputationTypeDef],
        "MetricComparison": NotRequired[MetricComparisonComputationTypeDef],
        "PeriodOverPeriod": NotRequired[PeriodOverPeriodComputationTypeDef],
        "PeriodToDate": NotRequired[PeriodToDateComputationTypeDef],
        "GrowthRate": NotRequired[GrowthRateComputationTypeDef],
        "UniqueValues": NotRequired[UniqueValuesComputationTypeDef],
        "Forecast": NotRequired[ForecastComputationTypeDef],
    },
)
TreeMapFieldWellsOutputTypeDef = TypedDict(
    "TreeMapFieldWellsOutputTypeDef",
    {
        "TreeMapAggregatedFieldWells": NotRequired[TreeMapAggregatedFieldWellsOutputTypeDef],
    },
)
TreeMapAggregatedFieldWellsUnionTypeDef = Union[
    TreeMapAggregatedFieldWellsTypeDef, TreeMapAggregatedFieldWellsOutputTypeDef
]
WaterfallChartFieldWellsOutputTypeDef = TypedDict(
    "WaterfallChartFieldWellsOutputTypeDef",
    {
        "WaterfallChartAggregatedFieldWells": NotRequired[
            WaterfallChartAggregatedFieldWellsOutputTypeDef
        ],
    },
)
WaterfallChartAggregatedFieldWellsUnionTypeDef = Union[
    WaterfallChartAggregatedFieldWellsTypeDef, WaterfallChartAggregatedFieldWellsOutputTypeDef
]
WordCloudFieldWellsOutputTypeDef = TypedDict(
    "WordCloudFieldWellsOutputTypeDef",
    {
        "WordCloudAggregatedFieldWells": NotRequired[WordCloudAggregatedFieldWellsOutputTypeDef],
    },
)
WordCloudAggregatedFieldWellsUnionTypeDef = Union[
    WordCloudAggregatedFieldWellsTypeDef, WordCloudAggregatedFieldWellsOutputTypeDef
]
TableFieldWellsOutputTypeDef = TypedDict(
    "TableFieldWellsOutputTypeDef",
    {
        "TableAggregatedFieldWells": NotRequired[TableAggregatedFieldWellsOutputTypeDef],
        "TableUnaggregatedFieldWells": NotRequired[TableUnaggregatedFieldWellsOutputTypeDef],
    },
)
TableUnaggregatedFieldWellsUnionTypeDef = Union[
    TableUnaggregatedFieldWellsTypeDef, TableUnaggregatedFieldWellsOutputTypeDef
]
SectionBasedLayoutConfigurationOutputTypeDef = TypedDict(
    "SectionBasedLayoutConfigurationOutputTypeDef",
    {
        "HeaderSections": List[HeaderFooterSectionConfigurationOutputTypeDef],
        "BodySections": List[BodySectionConfigurationOutputTypeDef],
        "FooterSections": List[HeaderFooterSectionConfigurationOutputTypeDef],
        "CanvasSizeOptions": SectionBasedLayoutCanvasSizeOptionsTypeDef,
    },
)
BodySectionRepeatConfigurationTypeDef = TypedDict(
    "BodySectionRepeatConfigurationTypeDef",
    {
        "DimensionConfigurations": NotRequired[
            Sequence[BodySectionRepeatDimensionConfigurationUnionTypeDef]
        ],
        "PageBreakConfiguration": NotRequired[BodySectionRepeatPageBreakConfigurationTypeDef],
        "NonRepeatingVisuals": NotRequired[Sequence[str]],
    },
)
PivotTableSortConfigurationTypeDef = TypedDict(
    "PivotTableSortConfigurationTypeDef",
    {
        "FieldSortOptions": NotRequired[Sequence[PivotFieldSortOptionsUnionTypeDef]],
    },
)
TooltipOptionsUnionTypeDef = Union[TooltipOptionsTypeDef, TooltipOptionsOutputTypeDef]
AssetBundleImportJobOverrideParametersTypeDef = TypedDict(
    "AssetBundleImportJobOverrideParametersTypeDef",
    {
        "ResourceIdOverrideConfiguration": NotRequired[
            AssetBundleImportJobResourceIdOverrideConfigurationTypeDef
        ],
        "VPCConnections": NotRequired[
            Sequence[AssetBundleImportJobVPCConnectionOverrideParametersUnionTypeDef]
        ],
        "RefreshSchedules": NotRequired[
            Sequence[AssetBundleImportJobRefreshScheduleOverrideParametersUnionTypeDef]
        ],
        "DataSources": NotRequired[
            Sequence[AssetBundleImportJobDataSourceOverrideParametersUnionTypeDef]
        ],
        "DataSets": NotRequired[Sequence[AssetBundleImportJobDataSetOverrideParametersTypeDef]],
        "Themes": NotRequired[Sequence[AssetBundleImportJobThemeOverrideParametersTypeDef]],
        "Analyses": NotRequired[Sequence[AssetBundleImportJobAnalysisOverrideParametersTypeDef]],
        "Dashboards": NotRequired[Sequence[AssetBundleImportJobDashboardOverrideParametersTypeDef]],
        "Folders": NotRequired[Sequence[AssetBundleImportJobFolderOverrideParametersTypeDef]],
    },
)
CreateDataSourceRequestRequestTypeDef = TypedDict(
    "CreateDataSourceRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSourceId": str,
        "Name": str,
        "Type": DataSourceTypeType,
        "DataSourceParameters": NotRequired[DataSourceParametersTypeDef],
        "Credentials": NotRequired[DataSourceCredentialsTypeDef],
        "Permissions": NotRequired[Sequence[ResourcePermissionTypeDef]],
        "VpcConnectionProperties": NotRequired[VpcConnectionPropertiesTypeDef],
        "SslProperties": NotRequired[SslPropertiesTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "FolderArns": NotRequired[Sequence[str]],
    },
)
UpdateDataSourceRequestRequestTypeDef = TypedDict(
    "UpdateDataSourceRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSourceId": str,
        "Name": str,
        "DataSourceParameters": NotRequired[DataSourceParametersTypeDef],
        "Credentials": NotRequired[DataSourceCredentialsTypeDef],
        "VpcConnectionProperties": NotRequired[VpcConnectionPropertiesTypeDef],
        "SslProperties": NotRequired[SslPropertiesTypeDef],
    },
)
BodySectionContentTypeDef = TypedDict(
    "BodySectionContentTypeDef",
    {
        "Layout": NotRequired[SectionLayoutConfigurationUnionTypeDef],
    },
)
HeaderFooterSectionConfigurationTypeDef = TypedDict(
    "HeaderFooterSectionConfigurationTypeDef",
    {
        "SectionId": str,
        "Layout": SectionLayoutConfigurationUnionTypeDef,
        "Style": NotRequired[SectionStyleTypeDef],
    },
)
CustomActionSetParametersOperationTypeDef = TypedDict(
    "CustomActionSetParametersOperationTypeDef",
    {
        "ParameterValueConfigurations": Sequence[SetParameterValueConfigurationUnionTypeDef],
    },
)
CreateDataSetRequestRequestTypeDef = TypedDict(
    "CreateDataSetRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DataSetId": str,
        "Name": str,
        "PhysicalTableMap": Mapping[str, PhysicalTableUnionTypeDef],
        "ImportMode": DataSetImportModeType,
        "LogicalTableMap": NotRequired[Mapping[str, LogicalTableUnionTypeDef]],
        "ColumnGroups": NotRequired[Sequence[ColumnGroupUnionTypeDef]],
        "FieldFolders": NotRequired[Mapping[str, FieldFolderUnionTypeDef]],
        "Permissions": NotRequired[Sequence[ResourcePermissionTypeDef]],
        "RowLevelPermissionDataSet": NotRequired[RowLevelPermissionDataSetTypeDef],
        "RowLevelPermissionTagConfiguration": NotRequired[
            RowLevelPermissionTagConfigurationTypeDef
        ],
        "ColumnLevelPermissionRules": NotRequired[Sequence[ColumnLevelPermissionRuleUnionTypeDef]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "DataSetUsageConfiguration": NotRequired[DataSetUsageConfigurationTypeDef],
        "DatasetParameters": NotRequired[Sequence[DatasetParameterUnionTypeDef]],
        "FolderArns": NotRequired[Sequence[str]],
    },
)
LineSeriesAxisDisplayOptionsTypeDef = TypedDict(
    "LineSeriesAxisDisplayOptionsTypeDef",
    {
        "AxisOptions": NotRequired[AxisDisplayOptionsUnionTypeDef],
        "MissingDataConfigurations": NotRequired[Sequence[MissingDataConfigurationTypeDef]],
    },
)
TopicIRTypeDef = TypedDict(
    "TopicIRTypeDef",
    {
        "Metrics": NotRequired[Sequence[TopicIRMetricUnionTypeDef]],
        "GroupByList": NotRequired[Sequence[TopicIRGroupByTypeDef]],
        "Filters": NotRequired[Sequence[Sequence[TopicIRFilterOptionUnionTypeDef]]],
        "Sort": NotRequired[TopicSortClauseTypeDef],
        "ContributionAnalysis": NotRequired[TopicIRContributionAnalysisUnionTypeDef],
        "Visual": NotRequired[VisualOptionsTypeDef],
    },
)
DatasetMetadataUnionTypeDef = Union[DatasetMetadataTypeDef, DatasetMetadataOutputTypeDef]
DefaultFilterControlConfigurationUnionTypeDef = Union[
    DefaultFilterControlConfigurationTypeDef, DefaultFilterControlConfigurationOutputTypeDef
]
NestedFilterOutputTypeDef = TypedDict(
    "NestedFilterOutputTypeDef",
    {
        "FilterId": str,
        "Column": ColumnIdentifierTypeDef,
        "IncludeInnerSet": bool,
        "InnerFilter": InnerFilterOutputTypeDef,
    },
)
GaugeChartConditionalFormattingOptionTypeDef = TypedDict(
    "GaugeChartConditionalFormattingOptionTypeDef",
    {
        "PrimaryValue": NotRequired[GaugeChartPrimaryValueConditionalFormattingUnionTypeDef],
        "Arc": NotRequired[GaugeChartArcConditionalFormattingUnionTypeDef],
    },
)
KPIConditionalFormattingOptionTypeDef = TypedDict(
    "KPIConditionalFormattingOptionTypeDef",
    {
        "PrimaryValue": NotRequired[KPIPrimaryValueConditionalFormattingUnionTypeDef],
        "ProgressBar": NotRequired[KPIProgressBarConditionalFormattingUnionTypeDef],
        "ActualValue": NotRequired[KPIActualValueConditionalFormattingUnionTypeDef],
        "ComparisonValue": NotRequired[KPIComparisonValueConditionalFormattingUnionTypeDef],
    },
)
FilledMapShapeConditionalFormattingTypeDef = TypedDict(
    "FilledMapShapeConditionalFormattingTypeDef",
    {
        "FieldId": str,
        "Format": NotRequired[ShapeConditionalFormatUnionTypeDef],
    },
)
PivotTableCellConditionalFormattingTypeDef = TypedDict(
    "PivotTableCellConditionalFormattingTypeDef",
    {
        "FieldId": str,
        "TextFormat": NotRequired[TextConditionalFormatUnionTypeDef],
        "Scope": NotRequired[PivotTableConditionalFormattingScopeTypeDef],
        "Scopes": NotRequired[Sequence[PivotTableConditionalFormattingScopeTypeDef]],
    },
)
TableCellConditionalFormattingTypeDef = TypedDict(
    "TableCellConditionalFormattingTypeDef",
    {
        "FieldId": str,
        "TextFormat": NotRequired[TextConditionalFormatUnionTypeDef],
    },
)
BarChartConfigurationOutputTypeDef = TypedDict(
    "BarChartConfigurationOutputTypeDef",
    {
        "FieldWells": NotRequired[BarChartFieldWellsOutputTypeDef],
        "SortConfiguration": NotRequired[BarChartSortConfigurationOutputTypeDef],
        "Orientation": NotRequired[BarChartOrientationType],
        "BarsArrangement": NotRequired[BarsArrangementType],
        "VisualPalette": NotRequired[VisualPaletteOutputTypeDef],
        "SmallMultiplesOptions": NotRequired[SmallMultiplesOptionsTypeDef],
        "CategoryAxis": NotRequired[AxisDisplayOptionsOutputTypeDef],
        "CategoryLabelOptions": NotRequired[ChartAxisLabelOptionsOutputTypeDef],
        "ValueAxis": NotRequired[AxisDisplayOptionsOutputTypeDef],
        "ValueLabelOptions": NotRequired[ChartAxisLabelOptionsOutputTypeDef],
        "ColorLabelOptions": NotRequired[ChartAxisLabelOptionsOutputTypeDef],
        "Legend": NotRequired[LegendOptionsTypeDef],
        "DataLabels": NotRequired[DataLabelOptionsOutputTypeDef],
        "Tooltip": NotRequired[TooltipOptionsOutputTypeDef],
        "ReferenceLines": NotRequired[List[ReferenceLineTypeDef]],
        "ContributionAnalysisDefaults": NotRequired[List[ContributionAnalysisDefaultOutputTypeDef]],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
BarChartFieldWellsTypeDef = TypedDict(
    "BarChartFieldWellsTypeDef",
    {
        "BarChartAggregatedFieldWells": NotRequired[BarChartAggregatedFieldWellsUnionTypeDef],
    },
)
BoxPlotChartConfigurationOutputTypeDef = TypedDict(
    "BoxPlotChartConfigurationOutputTypeDef",
    {
        "FieldWells": NotRequired[BoxPlotFieldWellsOutputTypeDef],
        "SortConfiguration": NotRequired[BoxPlotSortConfigurationOutputTypeDef],
        "BoxPlotOptions": NotRequired[BoxPlotOptionsTypeDef],
        "CategoryAxis": NotRequired[AxisDisplayOptionsOutputTypeDef],
        "CategoryLabelOptions": NotRequired[ChartAxisLabelOptionsOutputTypeDef],
        "PrimaryYAxisDisplayOptions": NotRequired[AxisDisplayOptionsOutputTypeDef],
        "PrimaryYAxisLabelOptions": NotRequired[ChartAxisLabelOptionsOutputTypeDef],
        "Legend": NotRequired[LegendOptionsTypeDef],
        "Tooltip": NotRequired[TooltipOptionsOutputTypeDef],
        "ReferenceLines": NotRequired[List[ReferenceLineTypeDef]],
        "VisualPalette": NotRequired[VisualPaletteOutputTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
BoxPlotFieldWellsTypeDef = TypedDict(
    "BoxPlotFieldWellsTypeDef",
    {
        "BoxPlotAggregatedFieldWells": NotRequired[BoxPlotAggregatedFieldWellsUnionTypeDef],
    },
)
ComboChartConfigurationOutputTypeDef = TypedDict(
    "ComboChartConfigurationOutputTypeDef",
    {
        "FieldWells": NotRequired[ComboChartFieldWellsOutputTypeDef],
        "SortConfiguration": NotRequired[ComboChartSortConfigurationOutputTypeDef],
        "BarsArrangement": NotRequired[BarsArrangementType],
        "CategoryAxis": NotRequired[AxisDisplayOptionsOutputTypeDef],
        "CategoryLabelOptions": NotRequired[ChartAxisLabelOptionsOutputTypeDef],
        "PrimaryYAxisDisplayOptions": NotRequired[AxisDisplayOptionsOutputTypeDef],
        "PrimaryYAxisLabelOptions": NotRequired[ChartAxisLabelOptionsOutputTypeDef],
        "SecondaryYAxisDisplayOptions": NotRequired[AxisDisplayOptionsOutputTypeDef],
        "SecondaryYAxisLabelOptions": NotRequired[ChartAxisLabelOptionsOutputTypeDef],
        "SingleAxisOptions": NotRequired[SingleAxisOptionsTypeDef],
        "ColorLabelOptions": NotRequired[ChartAxisLabelOptionsOutputTypeDef],
        "Legend": NotRequired[LegendOptionsTypeDef],
        "BarDataLabels": NotRequired[DataLabelOptionsOutputTypeDef],
        "LineDataLabels": NotRequired[DataLabelOptionsOutputTypeDef],
        "Tooltip": NotRequired[TooltipOptionsOutputTypeDef],
        "ReferenceLines": NotRequired[List[ReferenceLineTypeDef]],
        "VisualPalette": NotRequired[VisualPaletteOutputTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
ComboChartFieldWellsTypeDef = TypedDict(
    "ComboChartFieldWellsTypeDef",
    {
        "ComboChartAggregatedFieldWells": NotRequired[ComboChartAggregatedFieldWellsUnionTypeDef],
    },
)
FilledMapConfigurationOutputTypeDef = TypedDict(
    "FilledMapConfigurationOutputTypeDef",
    {
        "FieldWells": NotRequired[FilledMapFieldWellsOutputTypeDef],
        "SortConfiguration": NotRequired[FilledMapSortConfigurationOutputTypeDef],
        "Legend": NotRequired[LegendOptionsTypeDef],
        "Tooltip": NotRequired[TooltipOptionsOutputTypeDef],
        "WindowOptions": NotRequired[GeospatialWindowOptionsTypeDef],
        "MapStyleOptions": NotRequired[GeospatialMapStyleOptionsTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
FilledMapFieldWellsTypeDef = TypedDict(
    "FilledMapFieldWellsTypeDef",
    {
        "FilledMapAggregatedFieldWells": NotRequired[FilledMapAggregatedFieldWellsUnionTypeDef],
    },
)
FunnelChartConfigurationOutputTypeDef = TypedDict(
    "FunnelChartConfigurationOutputTypeDef",
    {
        "FieldWells": NotRequired[FunnelChartFieldWellsOutputTypeDef],
        "SortConfiguration": NotRequired[FunnelChartSortConfigurationOutputTypeDef],
        "CategoryLabelOptions": NotRequired[ChartAxisLabelOptionsOutputTypeDef],
        "ValueLabelOptions": NotRequired[ChartAxisLabelOptionsOutputTypeDef],
        "Tooltip": NotRequired[TooltipOptionsOutputTypeDef],
        "DataLabelOptions": NotRequired[FunnelChartDataLabelOptionsTypeDef],
        "VisualPalette": NotRequired[VisualPaletteOutputTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
FunnelChartFieldWellsTypeDef = TypedDict(
    "FunnelChartFieldWellsTypeDef",
    {
        "FunnelChartAggregatedFieldWells": NotRequired[FunnelChartAggregatedFieldWellsUnionTypeDef],
    },
)
GaugeChartVisualOutputTypeDef = TypedDict(
    "GaugeChartVisualOutputTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[GaugeChartConfigurationOutputTypeDef],
        "ConditionalFormatting": NotRequired[GaugeChartConditionalFormattingOutputTypeDef],
        "Actions": NotRequired[List[VisualCustomActionOutputTypeDef]],
    },
)
GeospatialMapConfigurationOutputTypeDef = TypedDict(
    "GeospatialMapConfigurationOutputTypeDef",
    {
        "FieldWells": NotRequired[GeospatialMapFieldWellsOutputTypeDef],
        "Legend": NotRequired[LegendOptionsTypeDef],
        "Tooltip": NotRequired[TooltipOptionsOutputTypeDef],
        "WindowOptions": NotRequired[GeospatialWindowOptionsTypeDef],
        "MapStyleOptions": NotRequired[GeospatialMapStyleOptionsTypeDef],
        "PointStyleOptions": NotRequired[GeospatialPointStyleOptionsOutputTypeDef],
        "VisualPalette": NotRequired[VisualPaletteOutputTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
GeospatialMapFieldWellsTypeDef = TypedDict(
    "GeospatialMapFieldWellsTypeDef",
    {
        "GeospatialMapAggregatedFieldWells": NotRequired[
            GeospatialMapAggregatedFieldWellsUnionTypeDef
        ],
    },
)
HeatMapConfigurationOutputTypeDef = TypedDict(
    "HeatMapConfigurationOutputTypeDef",
    {
        "FieldWells": NotRequired[HeatMapFieldWellsOutputTypeDef],
        "SortConfiguration": NotRequired[HeatMapSortConfigurationOutputTypeDef],
        "RowLabelOptions": NotRequired[ChartAxisLabelOptionsOutputTypeDef],
        "ColumnLabelOptions": NotRequired[ChartAxisLabelOptionsOutputTypeDef],
        "ColorScale": NotRequired[ColorScaleOutputTypeDef],
        "Legend": NotRequired[LegendOptionsTypeDef],
        "DataLabels": NotRequired[DataLabelOptionsOutputTypeDef],
        "Tooltip": NotRequired[TooltipOptionsOutputTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
HeatMapFieldWellsTypeDef = TypedDict(
    "HeatMapFieldWellsTypeDef",
    {
        "HeatMapAggregatedFieldWells": NotRequired[HeatMapAggregatedFieldWellsUnionTypeDef],
    },
)
HistogramConfigurationOutputTypeDef = TypedDict(
    "HistogramConfigurationOutputTypeDef",
    {
        "FieldWells": NotRequired[HistogramFieldWellsOutputTypeDef],
        "XAxisDisplayOptions": NotRequired[AxisDisplayOptionsOutputTypeDef],
        "XAxisLabelOptions": NotRequired[ChartAxisLabelOptionsOutputTypeDef],
        "YAxisDisplayOptions": NotRequired[AxisDisplayOptionsOutputTypeDef],
        "BinOptions": NotRequired[HistogramBinOptionsTypeDef],
        "DataLabels": NotRequired[DataLabelOptionsOutputTypeDef],
        "Tooltip": NotRequired[TooltipOptionsOutputTypeDef],
        "VisualPalette": NotRequired[VisualPaletteOutputTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
HistogramFieldWellsTypeDef = TypedDict(
    "HistogramFieldWellsTypeDef",
    {
        "HistogramAggregatedFieldWells": NotRequired[HistogramAggregatedFieldWellsUnionTypeDef],
    },
)
KPIVisualOutputTypeDef = TypedDict(
    "KPIVisualOutputTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[KPIConfigurationOutputTypeDef],
        "ConditionalFormatting": NotRequired[KPIConditionalFormattingOutputTypeDef],
        "Actions": NotRequired[List[VisualCustomActionOutputTypeDef]],
        "ColumnHierarchies": NotRequired[List[ColumnHierarchyOutputTypeDef]],
    },
)
KPIConfigurationTypeDef = TypedDict(
    "KPIConfigurationTypeDef",
    {
        "FieldWells": NotRequired[KPIFieldWellsUnionTypeDef],
        "SortConfiguration": NotRequired[KPISortConfigurationUnionTypeDef],
        "KPIOptions": NotRequired[KPIOptionsTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
LineChartConfigurationOutputTypeDef = TypedDict(
    "LineChartConfigurationOutputTypeDef",
    {
        "FieldWells": NotRequired[LineChartFieldWellsOutputTypeDef],
        "SortConfiguration": NotRequired[LineChartSortConfigurationOutputTypeDef],
        "ForecastConfigurations": NotRequired[List[ForecastConfigurationOutputTypeDef]],
        "Type": NotRequired[LineChartTypeType],
        "SmallMultiplesOptions": NotRequired[SmallMultiplesOptionsTypeDef],
        "XAxisDisplayOptions": NotRequired[AxisDisplayOptionsOutputTypeDef],
        "XAxisLabelOptions": NotRequired[ChartAxisLabelOptionsOutputTypeDef],
        "PrimaryYAxisDisplayOptions": NotRequired[LineSeriesAxisDisplayOptionsOutputTypeDef],
        "PrimaryYAxisLabelOptions": NotRequired[ChartAxisLabelOptionsOutputTypeDef],
        "SecondaryYAxisDisplayOptions": NotRequired[LineSeriesAxisDisplayOptionsOutputTypeDef],
        "SecondaryYAxisLabelOptions": NotRequired[ChartAxisLabelOptionsOutputTypeDef],
        "SingleAxisOptions": NotRequired[SingleAxisOptionsTypeDef],
        "DefaultSeriesSettings": NotRequired[LineChartDefaultSeriesSettingsTypeDef],
        "Series": NotRequired[List[SeriesItemTypeDef]],
        "Legend": NotRequired[LegendOptionsTypeDef],
        "DataLabels": NotRequired[DataLabelOptionsOutputTypeDef],
        "ReferenceLines": NotRequired[List[ReferenceLineTypeDef]],
        "Tooltip": NotRequired[TooltipOptionsOutputTypeDef],
        "ContributionAnalysisDefaults": NotRequired[List[ContributionAnalysisDefaultOutputTypeDef]],
        "VisualPalette": NotRequired[VisualPaletteOutputTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
LineChartFieldWellsTypeDef = TypedDict(
    "LineChartFieldWellsTypeDef",
    {
        "LineChartAggregatedFieldWells": NotRequired[LineChartAggregatedFieldWellsUnionTypeDef],
    },
)
PieChartConfigurationOutputTypeDef = TypedDict(
    "PieChartConfigurationOutputTypeDef",
    {
        "FieldWells": NotRequired[PieChartFieldWellsOutputTypeDef],
        "SortConfiguration": NotRequired[PieChartSortConfigurationOutputTypeDef],
        "DonutOptions": NotRequired[DonutOptionsTypeDef],
        "SmallMultiplesOptions": NotRequired[SmallMultiplesOptionsTypeDef],
        "CategoryLabelOptions": NotRequired[ChartAxisLabelOptionsOutputTypeDef],
        "ValueLabelOptions": NotRequired[ChartAxisLabelOptionsOutputTypeDef],
        "Legend": NotRequired[LegendOptionsTypeDef],
        "DataLabels": NotRequired[DataLabelOptionsOutputTypeDef],
        "Tooltip": NotRequired[TooltipOptionsOutputTypeDef],
        "VisualPalette": NotRequired[VisualPaletteOutputTypeDef],
        "ContributionAnalysisDefaults": NotRequired[List[ContributionAnalysisDefaultOutputTypeDef]],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
PieChartFieldWellsTypeDef = TypedDict(
    "PieChartFieldWellsTypeDef",
    {
        "PieChartAggregatedFieldWells": NotRequired[PieChartAggregatedFieldWellsUnionTypeDef],
    },
)
PivotTableConfigurationOutputTypeDef = TypedDict(
    "PivotTableConfigurationOutputTypeDef",
    {
        "FieldWells": NotRequired[PivotTableFieldWellsOutputTypeDef],
        "SortConfiguration": NotRequired[PivotTableSortConfigurationOutputTypeDef],
        "TableOptions": NotRequired[PivotTableOptionsOutputTypeDef],
        "TotalOptions": NotRequired[PivotTableTotalOptionsOutputTypeDef],
        "FieldOptions": NotRequired[PivotTableFieldOptionsOutputTypeDef],
        "PaginatedReportOptions": NotRequired[PivotTablePaginatedReportOptionsTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
PivotTableFieldWellsTypeDef = TypedDict(
    "PivotTableFieldWellsTypeDef",
    {
        "PivotTableAggregatedFieldWells": NotRequired[PivotTableAggregatedFieldWellsUnionTypeDef],
    },
)
RadarChartConfigurationOutputTypeDef = TypedDict(
    "RadarChartConfigurationOutputTypeDef",
    {
        "FieldWells": NotRequired[RadarChartFieldWellsOutputTypeDef],
        "SortConfiguration": NotRequired[RadarChartSortConfigurationOutputTypeDef],
        "Shape": NotRequired[RadarChartShapeType],
        "BaseSeriesSettings": NotRequired[RadarChartSeriesSettingsTypeDef],
        "StartAngle": NotRequired[float],
        "VisualPalette": NotRequired[VisualPaletteOutputTypeDef],
        "AlternateBandColorsVisibility": NotRequired[VisibilityType],
        "AlternateBandEvenColor": NotRequired[str],
        "AlternateBandOddColor": NotRequired[str],
        "CategoryAxis": NotRequired[AxisDisplayOptionsOutputTypeDef],
        "CategoryLabelOptions": NotRequired[ChartAxisLabelOptionsOutputTypeDef],
        "ColorAxis": NotRequired[AxisDisplayOptionsOutputTypeDef],
        "ColorLabelOptions": NotRequired[ChartAxisLabelOptionsOutputTypeDef],
        "Legend": NotRequired[LegendOptionsTypeDef],
        "AxesRangeScale": NotRequired[RadarChartAxesRangeScaleType],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
RadarChartFieldWellsTypeDef = TypedDict(
    "RadarChartFieldWellsTypeDef",
    {
        "RadarChartAggregatedFieldWells": NotRequired[RadarChartAggregatedFieldWellsUnionTypeDef],
    },
)
SankeyDiagramChartConfigurationOutputTypeDef = TypedDict(
    "SankeyDiagramChartConfigurationOutputTypeDef",
    {
        "FieldWells": NotRequired[SankeyDiagramFieldWellsOutputTypeDef],
        "SortConfiguration": NotRequired[SankeyDiagramSortConfigurationOutputTypeDef],
        "DataLabels": NotRequired[DataLabelOptionsOutputTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
SankeyDiagramFieldWellsTypeDef = TypedDict(
    "SankeyDiagramFieldWellsTypeDef",
    {
        "SankeyDiagramAggregatedFieldWells": NotRequired[
            SankeyDiagramAggregatedFieldWellsUnionTypeDef
        ],
    },
)
ScatterPlotConfigurationOutputTypeDef = TypedDict(
    "ScatterPlotConfigurationOutputTypeDef",
    {
        "FieldWells": NotRequired[ScatterPlotFieldWellsOutputTypeDef],
        "SortConfiguration": NotRequired[ScatterPlotSortConfigurationTypeDef],
        "XAxisLabelOptions": NotRequired[ChartAxisLabelOptionsOutputTypeDef],
        "XAxisDisplayOptions": NotRequired[AxisDisplayOptionsOutputTypeDef],
        "YAxisLabelOptions": NotRequired[ChartAxisLabelOptionsOutputTypeDef],
        "YAxisDisplayOptions": NotRequired[AxisDisplayOptionsOutputTypeDef],
        "Legend": NotRequired[LegendOptionsTypeDef],
        "DataLabels": NotRequired[DataLabelOptionsOutputTypeDef],
        "Tooltip": NotRequired[TooltipOptionsOutputTypeDef],
        "VisualPalette": NotRequired[VisualPaletteOutputTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
ScatterPlotFieldWellsTypeDef = TypedDict(
    "ScatterPlotFieldWellsTypeDef",
    {
        "ScatterPlotCategoricallyAggregatedFieldWells": NotRequired[
            ScatterPlotCategoricallyAggregatedFieldWellsUnionTypeDef
        ],
        "ScatterPlotUnaggregatedFieldWells": NotRequired[
            ScatterPlotUnaggregatedFieldWellsUnionTypeDef
        ],
    },
)
InsightConfigurationOutputTypeDef = TypedDict(
    "InsightConfigurationOutputTypeDef",
    {
        "Computations": NotRequired[List[ComputationTypeDef]],
        "CustomNarrative": NotRequired[CustomNarrativeOptionsTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
InsightConfigurationTypeDef = TypedDict(
    "InsightConfigurationTypeDef",
    {
        "Computations": NotRequired[Sequence[ComputationTypeDef]],
        "CustomNarrative": NotRequired[CustomNarrativeOptionsTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
TreeMapConfigurationOutputTypeDef = TypedDict(
    "TreeMapConfigurationOutputTypeDef",
    {
        "FieldWells": NotRequired[TreeMapFieldWellsOutputTypeDef],
        "SortConfiguration": NotRequired[TreeMapSortConfigurationOutputTypeDef],
        "GroupLabelOptions": NotRequired[ChartAxisLabelOptionsOutputTypeDef],
        "SizeLabelOptions": NotRequired[ChartAxisLabelOptionsOutputTypeDef],
        "ColorLabelOptions": NotRequired[ChartAxisLabelOptionsOutputTypeDef],
        "ColorScale": NotRequired[ColorScaleOutputTypeDef],
        "Legend": NotRequired[LegendOptionsTypeDef],
        "DataLabels": NotRequired[DataLabelOptionsOutputTypeDef],
        "Tooltip": NotRequired[TooltipOptionsOutputTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
TreeMapFieldWellsTypeDef = TypedDict(
    "TreeMapFieldWellsTypeDef",
    {
        "TreeMapAggregatedFieldWells": NotRequired[TreeMapAggregatedFieldWellsUnionTypeDef],
    },
)
WaterfallChartConfigurationOutputTypeDef = TypedDict(
    "WaterfallChartConfigurationOutputTypeDef",
    {
        "FieldWells": NotRequired[WaterfallChartFieldWellsOutputTypeDef],
        "SortConfiguration": NotRequired[WaterfallChartSortConfigurationOutputTypeDef],
        "WaterfallChartOptions": NotRequired[WaterfallChartOptionsTypeDef],
        "CategoryAxisLabelOptions": NotRequired[ChartAxisLabelOptionsOutputTypeDef],
        "CategoryAxisDisplayOptions": NotRequired[AxisDisplayOptionsOutputTypeDef],
        "PrimaryYAxisLabelOptions": NotRequired[ChartAxisLabelOptionsOutputTypeDef],
        "PrimaryYAxisDisplayOptions": NotRequired[AxisDisplayOptionsOutputTypeDef],
        "Legend": NotRequired[LegendOptionsTypeDef],
        "DataLabels": NotRequired[DataLabelOptionsOutputTypeDef],
        "VisualPalette": NotRequired[VisualPaletteOutputTypeDef],
        "ColorConfiguration": NotRequired[WaterfallChartColorConfigurationTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
WaterfallChartFieldWellsTypeDef = TypedDict(
    "WaterfallChartFieldWellsTypeDef",
    {
        "WaterfallChartAggregatedFieldWells": NotRequired[
            WaterfallChartAggregatedFieldWellsUnionTypeDef
        ],
    },
)
WordCloudChartConfigurationOutputTypeDef = TypedDict(
    "WordCloudChartConfigurationOutputTypeDef",
    {
        "FieldWells": NotRequired[WordCloudFieldWellsOutputTypeDef],
        "SortConfiguration": NotRequired[WordCloudSortConfigurationOutputTypeDef],
        "CategoryLabelOptions": NotRequired[ChartAxisLabelOptionsOutputTypeDef],
        "WordCloudOptions": NotRequired[WordCloudOptionsTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
WordCloudFieldWellsTypeDef = TypedDict(
    "WordCloudFieldWellsTypeDef",
    {
        "WordCloudAggregatedFieldWells": NotRequired[WordCloudAggregatedFieldWellsUnionTypeDef],
    },
)
TableConfigurationOutputTypeDef = TypedDict(
    "TableConfigurationOutputTypeDef",
    {
        "FieldWells": NotRequired[TableFieldWellsOutputTypeDef],
        "SortConfiguration": NotRequired[TableSortConfigurationOutputTypeDef],
        "TableOptions": NotRequired[TableOptionsOutputTypeDef],
        "TotalOptions": NotRequired[TotalOptionsOutputTypeDef],
        "FieldOptions": NotRequired[TableFieldOptionsOutputTypeDef],
        "PaginatedReportOptions": NotRequired[TablePaginatedReportOptionsTypeDef],
        "TableInlineVisualizations": NotRequired[List[TableInlineVisualizationTypeDef]],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
TableFieldWellsTypeDef = TypedDict(
    "TableFieldWellsTypeDef",
    {
        "TableAggregatedFieldWells": NotRequired[TableAggregatedFieldWellsUnionTypeDef],
        "TableUnaggregatedFieldWells": NotRequired[TableUnaggregatedFieldWellsUnionTypeDef],
    },
)
LayoutConfigurationOutputTypeDef = TypedDict(
    "LayoutConfigurationOutputTypeDef",
    {
        "GridLayout": NotRequired[GridLayoutConfigurationOutputTypeDef],
        "FreeFormLayout": NotRequired[FreeFormLayoutConfigurationOutputTypeDef],
        "SectionBasedLayout": NotRequired[SectionBasedLayoutConfigurationOutputTypeDef],
    },
)
BodySectionRepeatConfigurationUnionTypeDef = Union[
    BodySectionRepeatConfigurationTypeDef, BodySectionRepeatConfigurationOutputTypeDef
]
PivotTableSortConfigurationUnionTypeDef = Union[
    PivotTableSortConfigurationTypeDef, PivotTableSortConfigurationOutputTypeDef
]
GaugeChartConfigurationTypeDef = TypedDict(
    "GaugeChartConfigurationTypeDef",
    {
        "FieldWells": NotRequired[GaugeChartFieldWellsUnionTypeDef],
        "GaugeChartOptions": NotRequired[GaugeChartOptionsTypeDef],
        "DataLabels": NotRequired[DataLabelOptionsUnionTypeDef],
        "TooltipOptions": NotRequired[TooltipOptionsUnionTypeDef],
        "VisualPalette": NotRequired[VisualPaletteUnionTypeDef],
        "ColorConfiguration": NotRequired[GaugeChartColorConfigurationTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
StartAssetBundleImportJobRequestRequestTypeDef = TypedDict(
    "StartAssetBundleImportJobRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AssetBundleImportJobId": str,
        "AssetBundleImportSource": AssetBundleImportSourceTypeDef,
        "OverrideParameters": NotRequired[AssetBundleImportJobOverrideParametersTypeDef],
        "FailureAction": NotRequired[AssetBundleImportFailureActionType],
        "OverridePermissions": NotRequired[AssetBundleImportJobOverridePermissionsTypeDef],
        "OverrideTags": NotRequired[AssetBundleImportJobOverrideTagsTypeDef],
        "OverrideValidationStrategy": NotRequired[
            AssetBundleImportJobOverrideValidationStrategyTypeDef
        ],
    },
)
BodySectionContentUnionTypeDef = Union[BodySectionContentTypeDef, BodySectionContentOutputTypeDef]
HeaderFooterSectionConfigurationUnionTypeDef = Union[
    HeaderFooterSectionConfigurationTypeDef, HeaderFooterSectionConfigurationOutputTypeDef
]
CustomActionSetParametersOperationUnionTypeDef = Union[
    CustomActionSetParametersOperationTypeDef, CustomActionSetParametersOperationOutputTypeDef
]
LineSeriesAxisDisplayOptionsUnionTypeDef = Union[
    LineSeriesAxisDisplayOptionsTypeDef, LineSeriesAxisDisplayOptionsOutputTypeDef
]
TopicIRUnionTypeDef = Union[TopicIRTypeDef, TopicIROutputTypeDef]
TopicDetailsTypeDef = TypedDict(
    "TopicDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "UserExperienceVersion": NotRequired[TopicUserExperienceVersionType],
        "DataSets": NotRequired[Sequence[DatasetMetadataUnionTypeDef]],
        "ConfigOptions": NotRequired[TopicConfigOptionsTypeDef],
    },
)
CategoryFilterTypeDef = TypedDict(
    "CategoryFilterTypeDef",
    {
        "FilterId": str,
        "Column": ColumnIdentifierTypeDef,
        "Configuration": CategoryFilterConfigurationUnionTypeDef,
        "DefaultFilterControlConfiguration": NotRequired[
            DefaultFilterControlConfigurationUnionTypeDef
        ],
    },
)
CategoryInnerFilterTypeDef = TypedDict(
    "CategoryInnerFilterTypeDef",
    {
        "Column": ColumnIdentifierTypeDef,
        "Configuration": CategoryFilterConfigurationUnionTypeDef,
        "DefaultFilterControlConfiguration": NotRequired[
            DefaultFilterControlConfigurationUnionTypeDef
        ],
    },
)
NumericEqualityFilterTypeDef = TypedDict(
    "NumericEqualityFilterTypeDef",
    {
        "FilterId": str,
        "Column": ColumnIdentifierTypeDef,
        "MatchOperator": NumericEqualityMatchOperatorType,
        "NullOption": FilterNullOptionType,
        "Value": NotRequired[float],
        "SelectAllOptions": NotRequired[Literal["FILTER_ALL_VALUES"]],
        "AggregationFunction": NotRequired[AggregationFunctionTypeDef],
        "ParameterName": NotRequired[str],
        "DefaultFilterControlConfiguration": NotRequired[
            DefaultFilterControlConfigurationUnionTypeDef
        ],
    },
)
NumericRangeFilterTypeDef = TypedDict(
    "NumericRangeFilterTypeDef",
    {
        "FilterId": str,
        "Column": ColumnIdentifierTypeDef,
        "NullOption": FilterNullOptionType,
        "IncludeMinimum": NotRequired[bool],
        "IncludeMaximum": NotRequired[bool],
        "RangeMinimum": NotRequired[NumericRangeFilterValueTypeDef],
        "RangeMaximum": NotRequired[NumericRangeFilterValueTypeDef],
        "SelectAllOptions": NotRequired[Literal["FILTER_ALL_VALUES"]],
        "AggregationFunction": NotRequired[AggregationFunctionTypeDef],
        "DefaultFilterControlConfiguration": NotRequired[
            DefaultFilterControlConfigurationUnionTypeDef
        ],
    },
)
RelativeDatesFilterTypeDef = TypedDict(
    "RelativeDatesFilterTypeDef",
    {
        "FilterId": str,
        "Column": ColumnIdentifierTypeDef,
        "AnchorDateConfiguration": AnchorDateConfigurationTypeDef,
        "TimeGranularity": TimeGranularityType,
        "RelativeDateType": RelativeDateTypeType,
        "NullOption": FilterNullOptionType,
        "MinimumGranularity": NotRequired[TimeGranularityType],
        "RelativeDateValue": NotRequired[int],
        "ParameterName": NotRequired[str],
        "ExcludePeriodConfiguration": NotRequired[ExcludePeriodConfigurationTypeDef],
        "DefaultFilterControlConfiguration": NotRequired[
            DefaultFilterControlConfigurationUnionTypeDef
        ],
    },
)
TimeEqualityFilterTypeDef = TypedDict(
    "TimeEqualityFilterTypeDef",
    {
        "FilterId": str,
        "Column": ColumnIdentifierTypeDef,
        "Value": NotRequired[TimestampTypeDef],
        "ParameterName": NotRequired[str],
        "TimeGranularity": NotRequired[TimeGranularityType],
        "RollingDate": NotRequired[RollingDateConfigurationTypeDef],
        "DefaultFilterControlConfiguration": NotRequired[
            DefaultFilterControlConfigurationUnionTypeDef
        ],
    },
)
TimeRangeFilterTypeDef = TypedDict(
    "TimeRangeFilterTypeDef",
    {
        "FilterId": str,
        "Column": ColumnIdentifierTypeDef,
        "NullOption": FilterNullOptionType,
        "IncludeMinimum": NotRequired[bool],
        "IncludeMaximum": NotRequired[bool],
        "RangeMinimumValue": NotRequired[TimeRangeFilterValueUnionTypeDef],
        "RangeMaximumValue": NotRequired[TimeRangeFilterValueUnionTypeDef],
        "ExcludePeriodConfiguration": NotRequired[ExcludePeriodConfigurationTypeDef],
        "TimeGranularity": NotRequired[TimeGranularityType],
        "DefaultFilterControlConfiguration": NotRequired[
            DefaultFilterControlConfigurationUnionTypeDef
        ],
    },
)
TopBottomFilterTypeDef = TypedDict(
    "TopBottomFilterTypeDef",
    {
        "FilterId": str,
        "Column": ColumnIdentifierTypeDef,
        "AggregationSortConfigurations": Sequence[AggregationSortConfigurationTypeDef],
        "Limit": NotRequired[int],
        "TimeGranularity": NotRequired[TimeGranularityType],
        "ParameterName": NotRequired[str],
        "DefaultFilterControlConfiguration": NotRequired[
            DefaultFilterControlConfigurationUnionTypeDef
        ],
    },
)
FilterOutputTypeDef = TypedDict(
    "FilterOutputTypeDef",
    {
        "CategoryFilter": NotRequired[CategoryFilterOutputTypeDef],
        "NumericRangeFilter": NotRequired[NumericRangeFilterOutputTypeDef],
        "NumericEqualityFilter": NotRequired[NumericEqualityFilterOutputTypeDef],
        "TimeEqualityFilter": NotRequired[TimeEqualityFilterOutputTypeDef],
        "TimeRangeFilter": NotRequired[TimeRangeFilterOutputTypeDef],
        "RelativeDatesFilter": NotRequired[RelativeDatesFilterOutputTypeDef],
        "TopBottomFilter": NotRequired[TopBottomFilterOutputTypeDef],
        "NestedFilter": NotRequired[NestedFilterOutputTypeDef],
    },
)
GaugeChartConditionalFormattingOptionUnionTypeDef = Union[
    GaugeChartConditionalFormattingOptionTypeDef, GaugeChartConditionalFormattingOptionOutputTypeDef
]
KPIConditionalFormattingOptionUnionTypeDef = Union[
    KPIConditionalFormattingOptionTypeDef, KPIConditionalFormattingOptionOutputTypeDef
]
FilledMapShapeConditionalFormattingUnionTypeDef = Union[
    FilledMapShapeConditionalFormattingTypeDef, FilledMapShapeConditionalFormattingOutputTypeDef
]
PivotTableCellConditionalFormattingUnionTypeDef = Union[
    PivotTableCellConditionalFormattingTypeDef, PivotTableCellConditionalFormattingOutputTypeDef
]
TableCellConditionalFormattingUnionTypeDef = Union[
    TableCellConditionalFormattingTypeDef, TableCellConditionalFormattingOutputTypeDef
]
BarChartVisualOutputTypeDef = TypedDict(
    "BarChartVisualOutputTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[BarChartConfigurationOutputTypeDef],
        "Actions": NotRequired[List[VisualCustomActionOutputTypeDef]],
        "ColumnHierarchies": NotRequired[List[ColumnHierarchyOutputTypeDef]],
    },
)
BarChartFieldWellsUnionTypeDef = Union[BarChartFieldWellsTypeDef, BarChartFieldWellsOutputTypeDef]
BoxPlotVisualOutputTypeDef = TypedDict(
    "BoxPlotVisualOutputTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[BoxPlotChartConfigurationOutputTypeDef],
        "Actions": NotRequired[List[VisualCustomActionOutputTypeDef]],
        "ColumnHierarchies": NotRequired[List[ColumnHierarchyOutputTypeDef]],
    },
)
BoxPlotFieldWellsUnionTypeDef = Union[BoxPlotFieldWellsTypeDef, BoxPlotFieldWellsOutputTypeDef]
ComboChartVisualOutputTypeDef = TypedDict(
    "ComboChartVisualOutputTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[ComboChartConfigurationOutputTypeDef],
        "Actions": NotRequired[List[VisualCustomActionOutputTypeDef]],
        "ColumnHierarchies": NotRequired[List[ColumnHierarchyOutputTypeDef]],
    },
)
ComboChartFieldWellsUnionTypeDef = Union[
    ComboChartFieldWellsTypeDef, ComboChartFieldWellsOutputTypeDef
]
FilledMapVisualOutputTypeDef = TypedDict(
    "FilledMapVisualOutputTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[FilledMapConfigurationOutputTypeDef],
        "ConditionalFormatting": NotRequired[FilledMapConditionalFormattingOutputTypeDef],
        "ColumnHierarchies": NotRequired[List[ColumnHierarchyOutputTypeDef]],
        "Actions": NotRequired[List[VisualCustomActionOutputTypeDef]],
    },
)
FilledMapFieldWellsUnionTypeDef = Union[
    FilledMapFieldWellsTypeDef, FilledMapFieldWellsOutputTypeDef
]
FunnelChartVisualOutputTypeDef = TypedDict(
    "FunnelChartVisualOutputTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[FunnelChartConfigurationOutputTypeDef],
        "Actions": NotRequired[List[VisualCustomActionOutputTypeDef]],
        "ColumnHierarchies": NotRequired[List[ColumnHierarchyOutputTypeDef]],
    },
)
FunnelChartFieldWellsUnionTypeDef = Union[
    FunnelChartFieldWellsTypeDef, FunnelChartFieldWellsOutputTypeDef
]
GeospatialMapVisualOutputTypeDef = TypedDict(
    "GeospatialMapVisualOutputTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[GeospatialMapConfigurationOutputTypeDef],
        "ColumnHierarchies": NotRequired[List[ColumnHierarchyOutputTypeDef]],
        "Actions": NotRequired[List[VisualCustomActionOutputTypeDef]],
    },
)
GeospatialMapFieldWellsUnionTypeDef = Union[
    GeospatialMapFieldWellsTypeDef, GeospatialMapFieldWellsOutputTypeDef
]
HeatMapVisualOutputTypeDef = TypedDict(
    "HeatMapVisualOutputTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[HeatMapConfigurationOutputTypeDef],
        "ColumnHierarchies": NotRequired[List[ColumnHierarchyOutputTypeDef]],
        "Actions": NotRequired[List[VisualCustomActionOutputTypeDef]],
    },
)
HeatMapFieldWellsUnionTypeDef = Union[HeatMapFieldWellsTypeDef, HeatMapFieldWellsOutputTypeDef]
HistogramVisualOutputTypeDef = TypedDict(
    "HistogramVisualOutputTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[HistogramConfigurationOutputTypeDef],
        "Actions": NotRequired[List[VisualCustomActionOutputTypeDef]],
    },
)
HistogramFieldWellsUnionTypeDef = Union[
    HistogramFieldWellsTypeDef, HistogramFieldWellsOutputTypeDef
]
KPIConfigurationUnionTypeDef = Union[KPIConfigurationTypeDef, KPIConfigurationOutputTypeDef]
LineChartVisualOutputTypeDef = TypedDict(
    "LineChartVisualOutputTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[LineChartConfigurationOutputTypeDef],
        "Actions": NotRequired[List[VisualCustomActionOutputTypeDef]],
        "ColumnHierarchies": NotRequired[List[ColumnHierarchyOutputTypeDef]],
    },
)
LineChartFieldWellsUnionTypeDef = Union[
    LineChartFieldWellsTypeDef, LineChartFieldWellsOutputTypeDef
]
PieChartVisualOutputTypeDef = TypedDict(
    "PieChartVisualOutputTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[PieChartConfigurationOutputTypeDef],
        "Actions": NotRequired[List[VisualCustomActionOutputTypeDef]],
        "ColumnHierarchies": NotRequired[List[ColumnHierarchyOutputTypeDef]],
    },
)
PieChartFieldWellsUnionTypeDef = Union[PieChartFieldWellsTypeDef, PieChartFieldWellsOutputTypeDef]
PivotTableVisualOutputTypeDef = TypedDict(
    "PivotTableVisualOutputTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[PivotTableConfigurationOutputTypeDef],
        "ConditionalFormatting": NotRequired[PivotTableConditionalFormattingOutputTypeDef],
        "Actions": NotRequired[List[VisualCustomActionOutputTypeDef]],
    },
)
PivotTableFieldWellsUnionTypeDef = Union[
    PivotTableFieldWellsTypeDef, PivotTableFieldWellsOutputTypeDef
]
RadarChartVisualOutputTypeDef = TypedDict(
    "RadarChartVisualOutputTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[RadarChartConfigurationOutputTypeDef],
        "Actions": NotRequired[List[VisualCustomActionOutputTypeDef]],
        "ColumnHierarchies": NotRequired[List[ColumnHierarchyOutputTypeDef]],
    },
)
RadarChartFieldWellsUnionTypeDef = Union[
    RadarChartFieldWellsTypeDef, RadarChartFieldWellsOutputTypeDef
]
SankeyDiagramVisualOutputTypeDef = TypedDict(
    "SankeyDiagramVisualOutputTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[SankeyDiagramChartConfigurationOutputTypeDef],
        "Actions": NotRequired[List[VisualCustomActionOutputTypeDef]],
    },
)
SankeyDiagramFieldWellsUnionTypeDef = Union[
    SankeyDiagramFieldWellsTypeDef, SankeyDiagramFieldWellsOutputTypeDef
]
ScatterPlotVisualOutputTypeDef = TypedDict(
    "ScatterPlotVisualOutputTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[ScatterPlotConfigurationOutputTypeDef],
        "Actions": NotRequired[List[VisualCustomActionOutputTypeDef]],
        "ColumnHierarchies": NotRequired[List[ColumnHierarchyOutputTypeDef]],
    },
)
ScatterPlotFieldWellsUnionTypeDef = Union[
    ScatterPlotFieldWellsTypeDef, ScatterPlotFieldWellsOutputTypeDef
]
InsightVisualOutputTypeDef = TypedDict(
    "InsightVisualOutputTypeDef",
    {
        "VisualId": str,
        "DataSetIdentifier": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "InsightConfiguration": NotRequired[InsightConfigurationOutputTypeDef],
        "Actions": NotRequired[List[VisualCustomActionOutputTypeDef]],
    },
)
InsightConfigurationUnionTypeDef = Union[
    InsightConfigurationTypeDef, InsightConfigurationOutputTypeDef
]
TreeMapVisualOutputTypeDef = TypedDict(
    "TreeMapVisualOutputTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[TreeMapConfigurationOutputTypeDef],
        "Actions": NotRequired[List[VisualCustomActionOutputTypeDef]],
        "ColumnHierarchies": NotRequired[List[ColumnHierarchyOutputTypeDef]],
    },
)
TreeMapFieldWellsUnionTypeDef = Union[TreeMapFieldWellsTypeDef, TreeMapFieldWellsOutputTypeDef]
WaterfallVisualOutputTypeDef = TypedDict(
    "WaterfallVisualOutputTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[WaterfallChartConfigurationOutputTypeDef],
        "Actions": NotRequired[List[VisualCustomActionOutputTypeDef]],
        "ColumnHierarchies": NotRequired[List[ColumnHierarchyOutputTypeDef]],
    },
)
WaterfallChartFieldWellsUnionTypeDef = Union[
    WaterfallChartFieldWellsTypeDef, WaterfallChartFieldWellsOutputTypeDef
]
WordCloudVisualOutputTypeDef = TypedDict(
    "WordCloudVisualOutputTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[WordCloudChartConfigurationOutputTypeDef],
        "Actions": NotRequired[List[VisualCustomActionOutputTypeDef]],
        "ColumnHierarchies": NotRequired[List[ColumnHierarchyOutputTypeDef]],
    },
)
WordCloudFieldWellsUnionTypeDef = Union[
    WordCloudFieldWellsTypeDef, WordCloudFieldWellsOutputTypeDef
]
TableVisualOutputTypeDef = TypedDict(
    "TableVisualOutputTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[TableConfigurationOutputTypeDef],
        "ConditionalFormatting": NotRequired[TableConditionalFormattingOutputTypeDef],
        "Actions": NotRequired[List[VisualCustomActionOutputTypeDef]],
    },
)
TableFieldWellsUnionTypeDef = Union[TableFieldWellsTypeDef, TableFieldWellsOutputTypeDef]
LayoutOutputTypeDef = TypedDict(
    "LayoutOutputTypeDef",
    {
        "Configuration": LayoutConfigurationOutputTypeDef,
    },
)
GaugeChartConfigurationUnionTypeDef = Union[
    GaugeChartConfigurationTypeDef, GaugeChartConfigurationOutputTypeDef
]
BodySectionConfigurationTypeDef = TypedDict(
    "BodySectionConfigurationTypeDef",
    {
        "SectionId": str,
        "Content": BodySectionContentUnionTypeDef,
        "Style": NotRequired[SectionStyleTypeDef],
        "PageBreakConfiguration": NotRequired[SectionPageBreakConfigurationTypeDef],
        "RepeatConfiguration": NotRequired[BodySectionRepeatConfigurationUnionTypeDef],
    },
)
VisualCustomActionOperationTypeDef = TypedDict(
    "VisualCustomActionOperationTypeDef",
    {
        "FilterOperation": NotRequired[CustomActionFilterOperationUnionTypeDef],
        "NavigationOperation": NotRequired[CustomActionNavigationOperationTypeDef],
        "URLOperation": NotRequired[CustomActionURLOperationTypeDef],
        "SetParametersOperation": NotRequired[CustomActionSetParametersOperationUnionTypeDef],
    },
)
TopicVisualTypeDef = TypedDict(
    "TopicVisualTypeDef",
    {
        "VisualId": NotRequired[str],
        "Role": NotRequired[VisualRoleType],
        "Ir": NotRequired[TopicIRUnionTypeDef],
        "SupportingVisuals": NotRequired[Sequence[Mapping[str, Any]]],
    },
)
CreateTopicRequestRequestTypeDef = TypedDict(
    "CreateTopicRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TopicId": str,
        "Topic": TopicDetailsTypeDef,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
UpdateTopicRequestRequestTypeDef = TypedDict(
    "UpdateTopicRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TopicId": str,
        "Topic": TopicDetailsTypeDef,
    },
)
CategoryFilterUnionTypeDef = Union[CategoryFilterTypeDef, CategoryFilterOutputTypeDef]
CategoryInnerFilterUnionTypeDef = Union[
    CategoryInnerFilterTypeDef, CategoryInnerFilterOutputTypeDef
]
NumericEqualityFilterUnionTypeDef = Union[
    NumericEqualityFilterTypeDef, NumericEqualityFilterOutputTypeDef
]
NumericRangeFilterUnionTypeDef = Union[NumericRangeFilterTypeDef, NumericRangeFilterOutputTypeDef]
RelativeDatesFilterUnionTypeDef = Union[
    RelativeDatesFilterTypeDef, RelativeDatesFilterOutputTypeDef
]
TimeEqualityFilterUnionTypeDef = Union[TimeEqualityFilterTypeDef, TimeEqualityFilterOutputTypeDef]
TimeRangeFilterUnionTypeDef = Union[TimeRangeFilterTypeDef, TimeRangeFilterOutputTypeDef]
TopBottomFilterUnionTypeDef = Union[TopBottomFilterTypeDef, TopBottomFilterOutputTypeDef]
FilterGroupOutputTypeDef = TypedDict(
    "FilterGroupOutputTypeDef",
    {
        "FilterGroupId": str,
        "Filters": List[FilterOutputTypeDef],
        "ScopeConfiguration": FilterScopeConfigurationOutputTypeDef,
        "CrossDataset": CrossDatasetTypesType,
        "Status": NotRequired[WidgetStatusType],
    },
)
GaugeChartConditionalFormattingTypeDef = TypedDict(
    "GaugeChartConditionalFormattingTypeDef",
    {
        "ConditionalFormattingOptions": NotRequired[
            Sequence[GaugeChartConditionalFormattingOptionUnionTypeDef]
        ],
    },
)
KPIConditionalFormattingTypeDef = TypedDict(
    "KPIConditionalFormattingTypeDef",
    {
        "ConditionalFormattingOptions": NotRequired[
            Sequence[KPIConditionalFormattingOptionUnionTypeDef]
        ],
    },
)
FilledMapConditionalFormattingOptionTypeDef = TypedDict(
    "FilledMapConditionalFormattingOptionTypeDef",
    {
        "Shape": FilledMapShapeConditionalFormattingUnionTypeDef,
    },
)
PivotTableConditionalFormattingOptionTypeDef = TypedDict(
    "PivotTableConditionalFormattingOptionTypeDef",
    {
        "Cell": NotRequired[PivotTableCellConditionalFormattingUnionTypeDef],
    },
)
TableConditionalFormattingOptionTypeDef = TypedDict(
    "TableConditionalFormattingOptionTypeDef",
    {
        "Cell": NotRequired[TableCellConditionalFormattingUnionTypeDef],
        "Row": NotRequired[TableRowConditionalFormattingUnionTypeDef],
    },
)
BarChartConfigurationTypeDef = TypedDict(
    "BarChartConfigurationTypeDef",
    {
        "FieldWells": NotRequired[BarChartFieldWellsUnionTypeDef],
        "SortConfiguration": NotRequired[BarChartSortConfigurationUnionTypeDef],
        "Orientation": NotRequired[BarChartOrientationType],
        "BarsArrangement": NotRequired[BarsArrangementType],
        "VisualPalette": NotRequired[VisualPaletteUnionTypeDef],
        "SmallMultiplesOptions": NotRequired[SmallMultiplesOptionsTypeDef],
        "CategoryAxis": NotRequired[AxisDisplayOptionsUnionTypeDef],
        "CategoryLabelOptions": NotRequired[ChartAxisLabelOptionsUnionTypeDef],
        "ValueAxis": NotRequired[AxisDisplayOptionsUnionTypeDef],
        "ValueLabelOptions": NotRequired[ChartAxisLabelOptionsUnionTypeDef],
        "ColorLabelOptions": NotRequired[ChartAxisLabelOptionsUnionTypeDef],
        "Legend": NotRequired[LegendOptionsTypeDef],
        "DataLabels": NotRequired[DataLabelOptionsUnionTypeDef],
        "Tooltip": NotRequired[TooltipOptionsUnionTypeDef],
        "ReferenceLines": NotRequired[Sequence[ReferenceLineTypeDef]],
        "ContributionAnalysisDefaults": NotRequired[
            Sequence[ContributionAnalysisDefaultUnionTypeDef]
        ],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
BoxPlotChartConfigurationTypeDef = TypedDict(
    "BoxPlotChartConfigurationTypeDef",
    {
        "FieldWells": NotRequired[BoxPlotFieldWellsUnionTypeDef],
        "SortConfiguration": NotRequired[BoxPlotSortConfigurationUnionTypeDef],
        "BoxPlotOptions": NotRequired[BoxPlotOptionsTypeDef],
        "CategoryAxis": NotRequired[AxisDisplayOptionsUnionTypeDef],
        "CategoryLabelOptions": NotRequired[ChartAxisLabelOptionsUnionTypeDef],
        "PrimaryYAxisDisplayOptions": NotRequired[AxisDisplayOptionsUnionTypeDef],
        "PrimaryYAxisLabelOptions": NotRequired[ChartAxisLabelOptionsUnionTypeDef],
        "Legend": NotRequired[LegendOptionsTypeDef],
        "Tooltip": NotRequired[TooltipOptionsUnionTypeDef],
        "ReferenceLines": NotRequired[Sequence[ReferenceLineTypeDef]],
        "VisualPalette": NotRequired[VisualPaletteUnionTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
ComboChartConfigurationTypeDef = TypedDict(
    "ComboChartConfigurationTypeDef",
    {
        "FieldWells": NotRequired[ComboChartFieldWellsUnionTypeDef],
        "SortConfiguration": NotRequired[ComboChartSortConfigurationUnionTypeDef],
        "BarsArrangement": NotRequired[BarsArrangementType],
        "CategoryAxis": NotRequired[AxisDisplayOptionsUnionTypeDef],
        "CategoryLabelOptions": NotRequired[ChartAxisLabelOptionsUnionTypeDef],
        "PrimaryYAxisDisplayOptions": NotRequired[AxisDisplayOptionsUnionTypeDef],
        "PrimaryYAxisLabelOptions": NotRequired[ChartAxisLabelOptionsUnionTypeDef],
        "SecondaryYAxisDisplayOptions": NotRequired[AxisDisplayOptionsUnionTypeDef],
        "SecondaryYAxisLabelOptions": NotRequired[ChartAxisLabelOptionsUnionTypeDef],
        "SingleAxisOptions": NotRequired[SingleAxisOptionsTypeDef],
        "ColorLabelOptions": NotRequired[ChartAxisLabelOptionsUnionTypeDef],
        "Legend": NotRequired[LegendOptionsTypeDef],
        "BarDataLabels": NotRequired[DataLabelOptionsUnionTypeDef],
        "LineDataLabels": NotRequired[DataLabelOptionsUnionTypeDef],
        "Tooltip": NotRequired[TooltipOptionsUnionTypeDef],
        "ReferenceLines": NotRequired[Sequence[ReferenceLineTypeDef]],
        "VisualPalette": NotRequired[VisualPaletteUnionTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
FilledMapConfigurationTypeDef = TypedDict(
    "FilledMapConfigurationTypeDef",
    {
        "FieldWells": NotRequired[FilledMapFieldWellsUnionTypeDef],
        "SortConfiguration": NotRequired[FilledMapSortConfigurationUnionTypeDef],
        "Legend": NotRequired[LegendOptionsTypeDef],
        "Tooltip": NotRequired[TooltipOptionsUnionTypeDef],
        "WindowOptions": NotRequired[GeospatialWindowOptionsTypeDef],
        "MapStyleOptions": NotRequired[GeospatialMapStyleOptionsTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
FunnelChartConfigurationTypeDef = TypedDict(
    "FunnelChartConfigurationTypeDef",
    {
        "FieldWells": NotRequired[FunnelChartFieldWellsUnionTypeDef],
        "SortConfiguration": NotRequired[FunnelChartSortConfigurationUnionTypeDef],
        "CategoryLabelOptions": NotRequired[ChartAxisLabelOptionsUnionTypeDef],
        "ValueLabelOptions": NotRequired[ChartAxisLabelOptionsUnionTypeDef],
        "Tooltip": NotRequired[TooltipOptionsUnionTypeDef],
        "DataLabelOptions": NotRequired[FunnelChartDataLabelOptionsTypeDef],
        "VisualPalette": NotRequired[VisualPaletteUnionTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
GeospatialMapConfigurationTypeDef = TypedDict(
    "GeospatialMapConfigurationTypeDef",
    {
        "FieldWells": NotRequired[GeospatialMapFieldWellsUnionTypeDef],
        "Legend": NotRequired[LegendOptionsTypeDef],
        "Tooltip": NotRequired[TooltipOptionsUnionTypeDef],
        "WindowOptions": NotRequired[GeospatialWindowOptionsTypeDef],
        "MapStyleOptions": NotRequired[GeospatialMapStyleOptionsTypeDef],
        "PointStyleOptions": NotRequired[GeospatialPointStyleOptionsUnionTypeDef],
        "VisualPalette": NotRequired[VisualPaletteUnionTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
HeatMapConfigurationTypeDef = TypedDict(
    "HeatMapConfigurationTypeDef",
    {
        "FieldWells": NotRequired[HeatMapFieldWellsUnionTypeDef],
        "SortConfiguration": NotRequired[HeatMapSortConfigurationUnionTypeDef],
        "RowLabelOptions": NotRequired[ChartAxisLabelOptionsUnionTypeDef],
        "ColumnLabelOptions": NotRequired[ChartAxisLabelOptionsUnionTypeDef],
        "ColorScale": NotRequired[ColorScaleUnionTypeDef],
        "Legend": NotRequired[LegendOptionsTypeDef],
        "DataLabels": NotRequired[DataLabelOptionsUnionTypeDef],
        "Tooltip": NotRequired[TooltipOptionsUnionTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
HistogramConfigurationTypeDef = TypedDict(
    "HistogramConfigurationTypeDef",
    {
        "FieldWells": NotRequired[HistogramFieldWellsUnionTypeDef],
        "XAxisDisplayOptions": NotRequired[AxisDisplayOptionsUnionTypeDef],
        "XAxisLabelOptions": NotRequired[ChartAxisLabelOptionsUnionTypeDef],
        "YAxisDisplayOptions": NotRequired[AxisDisplayOptionsUnionTypeDef],
        "BinOptions": NotRequired[HistogramBinOptionsTypeDef],
        "DataLabels": NotRequired[DataLabelOptionsUnionTypeDef],
        "Tooltip": NotRequired[TooltipOptionsUnionTypeDef],
        "VisualPalette": NotRequired[VisualPaletteUnionTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
LineChartConfigurationTypeDef = TypedDict(
    "LineChartConfigurationTypeDef",
    {
        "FieldWells": NotRequired[LineChartFieldWellsUnionTypeDef],
        "SortConfiguration": NotRequired[LineChartSortConfigurationUnionTypeDef],
        "ForecastConfigurations": NotRequired[Sequence[ForecastConfigurationUnionTypeDef]],
        "Type": NotRequired[LineChartTypeType],
        "SmallMultiplesOptions": NotRequired[SmallMultiplesOptionsTypeDef],
        "XAxisDisplayOptions": NotRequired[AxisDisplayOptionsUnionTypeDef],
        "XAxisLabelOptions": NotRequired[ChartAxisLabelOptionsUnionTypeDef],
        "PrimaryYAxisDisplayOptions": NotRequired[LineSeriesAxisDisplayOptionsUnionTypeDef],
        "PrimaryYAxisLabelOptions": NotRequired[ChartAxisLabelOptionsUnionTypeDef],
        "SecondaryYAxisDisplayOptions": NotRequired[LineSeriesAxisDisplayOptionsUnionTypeDef],
        "SecondaryYAxisLabelOptions": NotRequired[ChartAxisLabelOptionsUnionTypeDef],
        "SingleAxisOptions": NotRequired[SingleAxisOptionsTypeDef],
        "DefaultSeriesSettings": NotRequired[LineChartDefaultSeriesSettingsTypeDef],
        "Series": NotRequired[Sequence[SeriesItemTypeDef]],
        "Legend": NotRequired[LegendOptionsTypeDef],
        "DataLabels": NotRequired[DataLabelOptionsUnionTypeDef],
        "ReferenceLines": NotRequired[Sequence[ReferenceLineTypeDef]],
        "Tooltip": NotRequired[TooltipOptionsUnionTypeDef],
        "ContributionAnalysisDefaults": NotRequired[
            Sequence[ContributionAnalysisDefaultUnionTypeDef]
        ],
        "VisualPalette": NotRequired[VisualPaletteUnionTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
PieChartConfigurationTypeDef = TypedDict(
    "PieChartConfigurationTypeDef",
    {
        "FieldWells": NotRequired[PieChartFieldWellsUnionTypeDef],
        "SortConfiguration": NotRequired[PieChartSortConfigurationUnionTypeDef],
        "DonutOptions": NotRequired[DonutOptionsTypeDef],
        "SmallMultiplesOptions": NotRequired[SmallMultiplesOptionsTypeDef],
        "CategoryLabelOptions": NotRequired[ChartAxisLabelOptionsUnionTypeDef],
        "ValueLabelOptions": NotRequired[ChartAxisLabelOptionsUnionTypeDef],
        "Legend": NotRequired[LegendOptionsTypeDef],
        "DataLabels": NotRequired[DataLabelOptionsUnionTypeDef],
        "Tooltip": NotRequired[TooltipOptionsUnionTypeDef],
        "VisualPalette": NotRequired[VisualPaletteUnionTypeDef],
        "ContributionAnalysisDefaults": NotRequired[
            Sequence[ContributionAnalysisDefaultUnionTypeDef]
        ],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
PivotTableConfigurationTypeDef = TypedDict(
    "PivotTableConfigurationTypeDef",
    {
        "FieldWells": NotRequired[PivotTableFieldWellsUnionTypeDef],
        "SortConfiguration": NotRequired[PivotTableSortConfigurationUnionTypeDef],
        "TableOptions": NotRequired[PivotTableOptionsUnionTypeDef],
        "TotalOptions": NotRequired[PivotTableTotalOptionsUnionTypeDef],
        "FieldOptions": NotRequired[PivotTableFieldOptionsUnionTypeDef],
        "PaginatedReportOptions": NotRequired[PivotTablePaginatedReportOptionsTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
RadarChartConfigurationTypeDef = TypedDict(
    "RadarChartConfigurationTypeDef",
    {
        "FieldWells": NotRequired[RadarChartFieldWellsUnionTypeDef],
        "SortConfiguration": NotRequired[RadarChartSortConfigurationUnionTypeDef],
        "Shape": NotRequired[RadarChartShapeType],
        "BaseSeriesSettings": NotRequired[RadarChartSeriesSettingsTypeDef],
        "StartAngle": NotRequired[float],
        "VisualPalette": NotRequired[VisualPaletteUnionTypeDef],
        "AlternateBandColorsVisibility": NotRequired[VisibilityType],
        "AlternateBandEvenColor": NotRequired[str],
        "AlternateBandOddColor": NotRequired[str],
        "CategoryAxis": NotRequired[AxisDisplayOptionsUnionTypeDef],
        "CategoryLabelOptions": NotRequired[ChartAxisLabelOptionsUnionTypeDef],
        "ColorAxis": NotRequired[AxisDisplayOptionsUnionTypeDef],
        "ColorLabelOptions": NotRequired[ChartAxisLabelOptionsUnionTypeDef],
        "Legend": NotRequired[LegendOptionsTypeDef],
        "AxesRangeScale": NotRequired[RadarChartAxesRangeScaleType],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
SankeyDiagramChartConfigurationTypeDef = TypedDict(
    "SankeyDiagramChartConfigurationTypeDef",
    {
        "FieldWells": NotRequired[SankeyDiagramFieldWellsUnionTypeDef],
        "SortConfiguration": NotRequired[SankeyDiagramSortConfigurationUnionTypeDef],
        "DataLabels": NotRequired[DataLabelOptionsUnionTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
ScatterPlotConfigurationTypeDef = TypedDict(
    "ScatterPlotConfigurationTypeDef",
    {
        "FieldWells": NotRequired[ScatterPlotFieldWellsUnionTypeDef],
        "SortConfiguration": NotRequired[ScatterPlotSortConfigurationTypeDef],
        "XAxisLabelOptions": NotRequired[ChartAxisLabelOptionsUnionTypeDef],
        "XAxisDisplayOptions": NotRequired[AxisDisplayOptionsUnionTypeDef],
        "YAxisLabelOptions": NotRequired[ChartAxisLabelOptionsUnionTypeDef],
        "YAxisDisplayOptions": NotRequired[AxisDisplayOptionsUnionTypeDef],
        "Legend": NotRequired[LegendOptionsTypeDef],
        "DataLabels": NotRequired[DataLabelOptionsUnionTypeDef],
        "Tooltip": NotRequired[TooltipOptionsUnionTypeDef],
        "VisualPalette": NotRequired[VisualPaletteUnionTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
TreeMapConfigurationTypeDef = TypedDict(
    "TreeMapConfigurationTypeDef",
    {
        "FieldWells": NotRequired[TreeMapFieldWellsUnionTypeDef],
        "SortConfiguration": NotRequired[TreeMapSortConfigurationUnionTypeDef],
        "GroupLabelOptions": NotRequired[ChartAxisLabelOptionsUnionTypeDef],
        "SizeLabelOptions": NotRequired[ChartAxisLabelOptionsUnionTypeDef],
        "ColorLabelOptions": NotRequired[ChartAxisLabelOptionsUnionTypeDef],
        "ColorScale": NotRequired[ColorScaleUnionTypeDef],
        "Legend": NotRequired[LegendOptionsTypeDef],
        "DataLabels": NotRequired[DataLabelOptionsUnionTypeDef],
        "Tooltip": NotRequired[TooltipOptionsUnionTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
WaterfallChartConfigurationTypeDef = TypedDict(
    "WaterfallChartConfigurationTypeDef",
    {
        "FieldWells": NotRequired[WaterfallChartFieldWellsUnionTypeDef],
        "SortConfiguration": NotRequired[WaterfallChartSortConfigurationUnionTypeDef],
        "WaterfallChartOptions": NotRequired[WaterfallChartOptionsTypeDef],
        "CategoryAxisLabelOptions": NotRequired[ChartAxisLabelOptionsUnionTypeDef],
        "CategoryAxisDisplayOptions": NotRequired[AxisDisplayOptionsUnionTypeDef],
        "PrimaryYAxisLabelOptions": NotRequired[ChartAxisLabelOptionsUnionTypeDef],
        "PrimaryYAxisDisplayOptions": NotRequired[AxisDisplayOptionsUnionTypeDef],
        "Legend": NotRequired[LegendOptionsTypeDef],
        "DataLabels": NotRequired[DataLabelOptionsUnionTypeDef],
        "VisualPalette": NotRequired[VisualPaletteUnionTypeDef],
        "ColorConfiguration": NotRequired[WaterfallChartColorConfigurationTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
WordCloudChartConfigurationTypeDef = TypedDict(
    "WordCloudChartConfigurationTypeDef",
    {
        "FieldWells": NotRequired[WordCloudFieldWellsUnionTypeDef],
        "SortConfiguration": NotRequired[WordCloudSortConfigurationUnionTypeDef],
        "CategoryLabelOptions": NotRequired[ChartAxisLabelOptionsUnionTypeDef],
        "WordCloudOptions": NotRequired[WordCloudOptionsTypeDef],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
VisualOutputTypeDef = TypedDict(
    "VisualOutputTypeDef",
    {
        "TableVisual": NotRequired[TableVisualOutputTypeDef],
        "PivotTableVisual": NotRequired[PivotTableVisualOutputTypeDef],
        "BarChartVisual": NotRequired[BarChartVisualOutputTypeDef],
        "KPIVisual": NotRequired[KPIVisualOutputTypeDef],
        "PieChartVisual": NotRequired[PieChartVisualOutputTypeDef],
        "GaugeChartVisual": NotRequired[GaugeChartVisualOutputTypeDef],
        "LineChartVisual": NotRequired[LineChartVisualOutputTypeDef],
        "HeatMapVisual": NotRequired[HeatMapVisualOutputTypeDef],
        "TreeMapVisual": NotRequired[TreeMapVisualOutputTypeDef],
        "GeospatialMapVisual": NotRequired[GeospatialMapVisualOutputTypeDef],
        "FilledMapVisual": NotRequired[FilledMapVisualOutputTypeDef],
        "FunnelChartVisual": NotRequired[FunnelChartVisualOutputTypeDef],
        "ScatterPlotVisual": NotRequired[ScatterPlotVisualOutputTypeDef],
        "ComboChartVisual": NotRequired[ComboChartVisualOutputTypeDef],
        "BoxPlotVisual": NotRequired[BoxPlotVisualOutputTypeDef],
        "WaterfallVisual": NotRequired[WaterfallVisualOutputTypeDef],
        "HistogramVisual": NotRequired[HistogramVisualOutputTypeDef],
        "WordCloudVisual": NotRequired[WordCloudVisualOutputTypeDef],
        "InsightVisual": NotRequired[InsightVisualOutputTypeDef],
        "SankeyDiagramVisual": NotRequired[SankeyDiagramVisualOutputTypeDef],
        "CustomContentVisual": NotRequired[CustomContentVisualOutputTypeDef],
        "EmptyVisual": NotRequired[EmptyVisualOutputTypeDef],
        "RadarChartVisual": NotRequired[RadarChartVisualOutputTypeDef],
    },
)
TableConfigurationTypeDef = TypedDict(
    "TableConfigurationTypeDef",
    {
        "FieldWells": NotRequired[TableFieldWellsUnionTypeDef],
        "SortConfiguration": NotRequired[TableSortConfigurationUnionTypeDef],
        "TableOptions": NotRequired[TableOptionsUnionTypeDef],
        "TotalOptions": NotRequired[TotalOptionsUnionTypeDef],
        "FieldOptions": NotRequired[TableFieldOptionsUnionTypeDef],
        "PaginatedReportOptions": NotRequired[TablePaginatedReportOptionsTypeDef],
        "TableInlineVisualizations": NotRequired[Sequence[TableInlineVisualizationTypeDef]],
        "Interactions": NotRequired[VisualInteractionOptionsTypeDef],
    },
)
BodySectionConfigurationUnionTypeDef = Union[
    BodySectionConfigurationTypeDef, BodySectionConfigurationOutputTypeDef
]
VisualCustomActionOperationUnionTypeDef = Union[
    VisualCustomActionOperationTypeDef, VisualCustomActionOperationOutputTypeDef
]
TopicVisualUnionTypeDef = Union[TopicVisualTypeDef, TopicVisualOutputTypeDef]
InnerFilterTypeDef = TypedDict(
    "InnerFilterTypeDef",
    {
        "CategoryInnerFilter": NotRequired[CategoryInnerFilterUnionTypeDef],
    },
)
GaugeChartConditionalFormattingUnionTypeDef = Union[
    GaugeChartConditionalFormattingTypeDef, GaugeChartConditionalFormattingOutputTypeDef
]
KPIConditionalFormattingUnionTypeDef = Union[
    KPIConditionalFormattingTypeDef, KPIConditionalFormattingOutputTypeDef
]
FilledMapConditionalFormattingOptionUnionTypeDef = Union[
    FilledMapConditionalFormattingOptionTypeDef, FilledMapConditionalFormattingOptionOutputTypeDef
]
PivotTableConditionalFormattingOptionUnionTypeDef = Union[
    PivotTableConditionalFormattingOptionTypeDef, PivotTableConditionalFormattingOptionOutputTypeDef
]
TableConditionalFormattingOptionUnionTypeDef = Union[
    TableConditionalFormattingOptionTypeDef, TableConditionalFormattingOptionOutputTypeDef
]
BarChartConfigurationUnionTypeDef = Union[
    BarChartConfigurationTypeDef, BarChartConfigurationOutputTypeDef
]
BoxPlotChartConfigurationUnionTypeDef = Union[
    BoxPlotChartConfigurationTypeDef, BoxPlotChartConfigurationOutputTypeDef
]
ComboChartConfigurationUnionTypeDef = Union[
    ComboChartConfigurationTypeDef, ComboChartConfigurationOutputTypeDef
]
FilledMapConfigurationUnionTypeDef = Union[
    FilledMapConfigurationTypeDef, FilledMapConfigurationOutputTypeDef
]
FunnelChartConfigurationUnionTypeDef = Union[
    FunnelChartConfigurationTypeDef, FunnelChartConfigurationOutputTypeDef
]
GeospatialMapConfigurationUnionTypeDef = Union[
    GeospatialMapConfigurationTypeDef, GeospatialMapConfigurationOutputTypeDef
]
HeatMapConfigurationUnionTypeDef = Union[
    HeatMapConfigurationTypeDef, HeatMapConfigurationOutputTypeDef
]
HistogramConfigurationUnionTypeDef = Union[
    HistogramConfigurationTypeDef, HistogramConfigurationOutputTypeDef
]
LineChartConfigurationUnionTypeDef = Union[
    LineChartConfigurationTypeDef, LineChartConfigurationOutputTypeDef
]
PieChartConfigurationUnionTypeDef = Union[
    PieChartConfigurationTypeDef, PieChartConfigurationOutputTypeDef
]
PivotTableConfigurationUnionTypeDef = Union[
    PivotTableConfigurationTypeDef, PivotTableConfigurationOutputTypeDef
]
RadarChartConfigurationUnionTypeDef = Union[
    RadarChartConfigurationTypeDef, RadarChartConfigurationOutputTypeDef
]
SankeyDiagramChartConfigurationUnionTypeDef = Union[
    SankeyDiagramChartConfigurationTypeDef, SankeyDiagramChartConfigurationOutputTypeDef
]
ScatterPlotConfigurationUnionTypeDef = Union[
    ScatterPlotConfigurationTypeDef, ScatterPlotConfigurationOutputTypeDef
]
TreeMapConfigurationUnionTypeDef = Union[
    TreeMapConfigurationTypeDef, TreeMapConfigurationOutputTypeDef
]
WaterfallChartConfigurationUnionTypeDef = Union[
    WaterfallChartConfigurationTypeDef, WaterfallChartConfigurationOutputTypeDef
]
WordCloudChartConfigurationUnionTypeDef = Union[
    WordCloudChartConfigurationTypeDef, WordCloudChartConfigurationOutputTypeDef
]
SheetDefinitionOutputTypeDef = TypedDict(
    "SheetDefinitionOutputTypeDef",
    {
        "SheetId": str,
        "Title": NotRequired[str],
        "Description": NotRequired[str],
        "Name": NotRequired[str],
        "ParameterControls": NotRequired[List[ParameterControlOutputTypeDef]],
        "FilterControls": NotRequired[List[FilterControlOutputTypeDef]],
        "Visuals": NotRequired[List[VisualOutputTypeDef]],
        "TextBoxes": NotRequired[List[SheetTextBoxTypeDef]],
        "Layouts": NotRequired[List[LayoutOutputTypeDef]],
        "SheetControlLayouts": NotRequired[List[SheetControlLayoutOutputTypeDef]],
        "ContentType": NotRequired[SheetContentTypeType],
    },
)
TableConfigurationUnionTypeDef = Union[TableConfigurationTypeDef, TableConfigurationOutputTypeDef]
SectionBasedLayoutConfigurationTypeDef = TypedDict(
    "SectionBasedLayoutConfigurationTypeDef",
    {
        "HeaderSections": Sequence[HeaderFooterSectionConfigurationUnionTypeDef],
        "BodySections": Sequence[BodySectionConfigurationUnionTypeDef],
        "FooterSections": Sequence[HeaderFooterSectionConfigurationUnionTypeDef],
        "CanvasSizeOptions": SectionBasedLayoutCanvasSizeOptionsTypeDef,
    },
)
VisualCustomActionTypeDef = TypedDict(
    "VisualCustomActionTypeDef",
    {
        "CustomActionId": str,
        "Name": str,
        "Trigger": VisualCustomActionTriggerType,
        "ActionOperations": Sequence[VisualCustomActionOperationUnionTypeDef],
        "Status": NotRequired[WidgetStatusType],
    },
)
CreateTopicReviewedAnswerTypeDef = TypedDict(
    "CreateTopicReviewedAnswerTypeDef",
    {
        "AnswerId": str,
        "DatasetArn": str,
        "Question": str,
        "Mir": NotRequired[TopicIRUnionTypeDef],
        "PrimaryVisual": NotRequired[TopicVisualUnionTypeDef],
        "Template": NotRequired[TopicTemplateUnionTypeDef],
    },
)
InnerFilterUnionTypeDef = Union[InnerFilterTypeDef, InnerFilterOutputTypeDef]
FilledMapConditionalFormattingTypeDef = TypedDict(
    "FilledMapConditionalFormattingTypeDef",
    {
        "ConditionalFormattingOptions": Sequence[FilledMapConditionalFormattingOptionUnionTypeDef],
    },
)
PivotTableConditionalFormattingTypeDef = TypedDict(
    "PivotTableConditionalFormattingTypeDef",
    {
        "ConditionalFormattingOptions": NotRequired[
            Sequence[PivotTableConditionalFormattingOptionUnionTypeDef]
        ],
    },
)
TableConditionalFormattingTypeDef = TypedDict(
    "TableConditionalFormattingTypeDef",
    {
        "ConditionalFormattingOptions": NotRequired[
            Sequence[TableConditionalFormattingOptionUnionTypeDef]
        ],
    },
)
AnalysisDefinitionOutputTypeDef = TypedDict(
    "AnalysisDefinitionOutputTypeDef",
    {
        "DataSetIdentifierDeclarations": List[DataSetIdentifierDeclarationTypeDef],
        "Sheets": NotRequired[List[SheetDefinitionOutputTypeDef]],
        "CalculatedFields": NotRequired[List[CalculatedFieldTypeDef]],
        "ParameterDeclarations": NotRequired[List[ParameterDeclarationOutputTypeDef]],
        "FilterGroups": NotRequired[List[FilterGroupOutputTypeDef]],
        "ColumnConfigurations": NotRequired[List[ColumnConfigurationOutputTypeDef]],
        "AnalysisDefaults": NotRequired[AnalysisDefaultsTypeDef],
        "Options": NotRequired[AssetOptionsTypeDef],
        "QueryExecutionOptions": NotRequired[QueryExecutionOptionsTypeDef],
    },
)
DashboardVersionDefinitionOutputTypeDef = TypedDict(
    "DashboardVersionDefinitionOutputTypeDef",
    {
        "DataSetIdentifierDeclarations": List[DataSetIdentifierDeclarationTypeDef],
        "Sheets": NotRequired[List[SheetDefinitionOutputTypeDef]],
        "CalculatedFields": NotRequired[List[CalculatedFieldTypeDef]],
        "ParameterDeclarations": NotRequired[List[ParameterDeclarationOutputTypeDef]],
        "FilterGroups": NotRequired[List[FilterGroupOutputTypeDef]],
        "ColumnConfigurations": NotRequired[List[ColumnConfigurationOutputTypeDef]],
        "AnalysisDefaults": NotRequired[AnalysisDefaultsTypeDef],
        "Options": NotRequired[AssetOptionsTypeDef],
    },
)
TemplateVersionDefinitionOutputTypeDef = TypedDict(
    "TemplateVersionDefinitionOutputTypeDef",
    {
        "DataSetConfigurations": List[DataSetConfigurationOutputTypeDef],
        "Sheets": NotRequired[List[SheetDefinitionOutputTypeDef]],
        "CalculatedFields": NotRequired[List[CalculatedFieldTypeDef]],
        "ParameterDeclarations": NotRequired[List[ParameterDeclarationOutputTypeDef]],
        "FilterGroups": NotRequired[List[FilterGroupOutputTypeDef]],
        "ColumnConfigurations": NotRequired[List[ColumnConfigurationOutputTypeDef]],
        "AnalysisDefaults": NotRequired[AnalysisDefaultsTypeDef],
        "Options": NotRequired[AssetOptionsTypeDef],
        "QueryExecutionOptions": NotRequired[QueryExecutionOptionsTypeDef],
    },
)
SectionBasedLayoutConfigurationUnionTypeDef = Union[
    SectionBasedLayoutConfigurationTypeDef, SectionBasedLayoutConfigurationOutputTypeDef
]
BoxPlotVisualTypeDef = TypedDict(
    "BoxPlotVisualTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[BoxPlotChartConfigurationUnionTypeDef],
        "Actions": NotRequired[Sequence[VisualCustomActionTypeDef]],
        "ColumnHierarchies": NotRequired[Sequence[ColumnHierarchyTypeDef]],
    },
)
ComboChartVisualTypeDef = TypedDict(
    "ComboChartVisualTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[ComboChartConfigurationUnionTypeDef],
        "Actions": NotRequired[Sequence[VisualCustomActionTypeDef]],
        "ColumnHierarchies": NotRequired[Sequence[ColumnHierarchyTypeDef]],
    },
)
CustomContentVisualTypeDef = TypedDict(
    "CustomContentVisualTypeDef",
    {
        "VisualId": str,
        "DataSetIdentifier": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[CustomContentConfigurationTypeDef],
        "Actions": NotRequired[Sequence[VisualCustomActionTypeDef]],
    },
)
EmptyVisualTypeDef = TypedDict(
    "EmptyVisualTypeDef",
    {
        "VisualId": str,
        "DataSetIdentifier": str,
        "Actions": NotRequired[Sequence[VisualCustomActionTypeDef]],
    },
)
FunnelChartVisualTypeDef = TypedDict(
    "FunnelChartVisualTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[FunnelChartConfigurationUnionTypeDef],
        "Actions": NotRequired[Sequence[VisualCustomActionTypeDef]],
        "ColumnHierarchies": NotRequired[Sequence[ColumnHierarchyTypeDef]],
    },
)
GaugeChartVisualTypeDef = TypedDict(
    "GaugeChartVisualTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[GaugeChartConfigurationUnionTypeDef],
        "ConditionalFormatting": NotRequired[GaugeChartConditionalFormattingUnionTypeDef],
        "Actions": NotRequired[Sequence[VisualCustomActionTypeDef]],
    },
)
GeospatialMapVisualTypeDef = TypedDict(
    "GeospatialMapVisualTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[GeospatialMapConfigurationUnionTypeDef],
        "ColumnHierarchies": NotRequired[Sequence[ColumnHierarchyTypeDef]],
        "Actions": NotRequired[Sequence[VisualCustomActionTypeDef]],
    },
)
HeatMapVisualTypeDef = TypedDict(
    "HeatMapVisualTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[HeatMapConfigurationUnionTypeDef],
        "ColumnHierarchies": NotRequired[Sequence[ColumnHierarchyTypeDef]],
        "Actions": NotRequired[Sequence[VisualCustomActionTypeDef]],
    },
)
HistogramVisualTypeDef = TypedDict(
    "HistogramVisualTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[HistogramConfigurationUnionTypeDef],
        "Actions": NotRequired[Sequence[VisualCustomActionTypeDef]],
    },
)
InsightVisualTypeDef = TypedDict(
    "InsightVisualTypeDef",
    {
        "VisualId": str,
        "DataSetIdentifier": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "InsightConfiguration": NotRequired[InsightConfigurationUnionTypeDef],
        "Actions": NotRequired[Sequence[VisualCustomActionTypeDef]],
    },
)
KPIVisualTypeDef = TypedDict(
    "KPIVisualTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[KPIConfigurationUnionTypeDef],
        "ConditionalFormatting": NotRequired[KPIConditionalFormattingUnionTypeDef],
        "Actions": NotRequired[Sequence[VisualCustomActionTypeDef]],
        "ColumnHierarchies": NotRequired[Sequence[ColumnHierarchyUnionTypeDef]],
    },
)
LineChartVisualTypeDef = TypedDict(
    "LineChartVisualTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[LineChartConfigurationUnionTypeDef],
        "Actions": NotRequired[Sequence[VisualCustomActionTypeDef]],
        "ColumnHierarchies": NotRequired[Sequence[ColumnHierarchyTypeDef]],
    },
)
PieChartVisualTypeDef = TypedDict(
    "PieChartVisualTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[PieChartConfigurationUnionTypeDef],
        "Actions": NotRequired[Sequence[VisualCustomActionTypeDef]],
        "ColumnHierarchies": NotRequired[Sequence[ColumnHierarchyUnionTypeDef]],
    },
)
RadarChartVisualTypeDef = TypedDict(
    "RadarChartVisualTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[RadarChartConfigurationUnionTypeDef],
        "Actions": NotRequired[Sequence[VisualCustomActionTypeDef]],
        "ColumnHierarchies": NotRequired[Sequence[ColumnHierarchyTypeDef]],
    },
)
SankeyDiagramVisualTypeDef = TypedDict(
    "SankeyDiagramVisualTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[SankeyDiagramChartConfigurationUnionTypeDef],
        "Actions": NotRequired[Sequence[VisualCustomActionTypeDef]],
    },
)
ScatterPlotVisualTypeDef = TypedDict(
    "ScatterPlotVisualTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[ScatterPlotConfigurationUnionTypeDef],
        "Actions": NotRequired[Sequence[VisualCustomActionTypeDef]],
        "ColumnHierarchies": NotRequired[Sequence[ColumnHierarchyTypeDef]],
    },
)
TreeMapVisualTypeDef = TypedDict(
    "TreeMapVisualTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[TreeMapConfigurationUnionTypeDef],
        "Actions": NotRequired[Sequence[VisualCustomActionTypeDef]],
        "ColumnHierarchies": NotRequired[Sequence[ColumnHierarchyTypeDef]],
    },
)
VisualCustomActionUnionTypeDef = Union[VisualCustomActionTypeDef, VisualCustomActionOutputTypeDef]
WaterfallVisualTypeDef = TypedDict(
    "WaterfallVisualTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[WaterfallChartConfigurationUnionTypeDef],
        "Actions": NotRequired[Sequence[VisualCustomActionTypeDef]],
        "ColumnHierarchies": NotRequired[Sequence[ColumnHierarchyTypeDef]],
    },
)
WordCloudVisualTypeDef = TypedDict(
    "WordCloudVisualTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[WordCloudChartConfigurationUnionTypeDef],
        "Actions": NotRequired[Sequence[VisualCustomActionTypeDef]],
        "ColumnHierarchies": NotRequired[Sequence[ColumnHierarchyTypeDef]],
    },
)
BatchCreateTopicReviewedAnswerRequestRequestTypeDef = TypedDict(
    "BatchCreateTopicReviewedAnswerRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TopicId": str,
        "Answers": Sequence[CreateTopicReviewedAnswerTypeDef],
    },
)
NestedFilterTypeDef = TypedDict(
    "NestedFilterTypeDef",
    {
        "FilterId": str,
        "Column": ColumnIdentifierTypeDef,
        "IncludeInnerSet": bool,
        "InnerFilter": InnerFilterUnionTypeDef,
    },
)
FilledMapConditionalFormattingUnionTypeDef = Union[
    FilledMapConditionalFormattingTypeDef, FilledMapConditionalFormattingOutputTypeDef
]
PivotTableConditionalFormattingUnionTypeDef = Union[
    PivotTableConditionalFormattingTypeDef, PivotTableConditionalFormattingOutputTypeDef
]
TableConditionalFormattingUnionTypeDef = Union[
    TableConditionalFormattingTypeDef, TableConditionalFormattingOutputTypeDef
]
DescribeAnalysisDefinitionResponseTypeDef = TypedDict(
    "DescribeAnalysisDefinitionResponseTypeDef",
    {
        "AnalysisId": str,
        "Name": str,
        "Errors": List[AnalysisErrorTypeDef],
        "ResourceStatus": ResourceStatusType,
        "ThemeArn": str,
        "Definition": AnalysisDefinitionOutputTypeDef,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDashboardDefinitionResponseTypeDef = TypedDict(
    "DescribeDashboardDefinitionResponseTypeDef",
    {
        "DashboardId": str,
        "Errors": List[DashboardErrorTypeDef],
        "Name": str,
        "ResourceStatus": ResourceStatusType,
        "ThemeArn": str,
        "Definition": DashboardVersionDefinitionOutputTypeDef,
        "Status": int,
        "RequestId": str,
        "DashboardPublishOptions": DashboardPublishOptionsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTemplateDefinitionResponseTypeDef = TypedDict(
    "DescribeTemplateDefinitionResponseTypeDef",
    {
        "Name": str,
        "TemplateId": str,
        "Errors": List[TemplateErrorTypeDef],
        "ResourceStatus": ResourceStatusType,
        "ThemeArn": str,
        "Definition": TemplateVersionDefinitionOutputTypeDef,
        "Status": int,
        "RequestId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LayoutConfigurationTypeDef = TypedDict(
    "LayoutConfigurationTypeDef",
    {
        "GridLayout": NotRequired[GridLayoutConfigurationUnionTypeDef],
        "FreeFormLayout": NotRequired[FreeFormLayoutConfigurationUnionTypeDef],
        "SectionBasedLayout": NotRequired[SectionBasedLayoutConfigurationUnionTypeDef],
    },
)
BoxPlotVisualUnionTypeDef = Union[BoxPlotVisualTypeDef, BoxPlotVisualOutputTypeDef]
ComboChartVisualUnionTypeDef = Union[ComboChartVisualTypeDef, ComboChartVisualOutputTypeDef]
CustomContentVisualUnionTypeDef = Union[
    CustomContentVisualTypeDef, CustomContentVisualOutputTypeDef
]
EmptyVisualUnionTypeDef = Union[EmptyVisualTypeDef, EmptyVisualOutputTypeDef]
FunnelChartVisualUnionTypeDef = Union[FunnelChartVisualTypeDef, FunnelChartVisualOutputTypeDef]
GaugeChartVisualUnionTypeDef = Union[GaugeChartVisualTypeDef, GaugeChartVisualOutputTypeDef]
GeospatialMapVisualUnionTypeDef = Union[
    GeospatialMapVisualTypeDef, GeospatialMapVisualOutputTypeDef
]
HeatMapVisualUnionTypeDef = Union[HeatMapVisualTypeDef, HeatMapVisualOutputTypeDef]
HistogramVisualUnionTypeDef = Union[HistogramVisualTypeDef, HistogramVisualOutputTypeDef]
InsightVisualUnionTypeDef = Union[InsightVisualTypeDef, InsightVisualOutputTypeDef]
KPIVisualUnionTypeDef = Union[KPIVisualTypeDef, KPIVisualOutputTypeDef]
LineChartVisualUnionTypeDef = Union[LineChartVisualTypeDef, LineChartVisualOutputTypeDef]
PieChartVisualUnionTypeDef = Union[PieChartVisualTypeDef, PieChartVisualOutputTypeDef]
RadarChartVisualUnionTypeDef = Union[RadarChartVisualTypeDef, RadarChartVisualOutputTypeDef]
SankeyDiagramVisualUnionTypeDef = Union[
    SankeyDiagramVisualTypeDef, SankeyDiagramVisualOutputTypeDef
]
ScatterPlotVisualUnionTypeDef = Union[ScatterPlotVisualTypeDef, ScatterPlotVisualOutputTypeDef]
TreeMapVisualUnionTypeDef = Union[TreeMapVisualTypeDef, TreeMapVisualOutputTypeDef]
BarChartVisualTypeDef = TypedDict(
    "BarChartVisualTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[BarChartConfigurationUnionTypeDef],
        "Actions": NotRequired[Sequence[VisualCustomActionUnionTypeDef]],
        "ColumnHierarchies": NotRequired[Sequence[ColumnHierarchyUnionTypeDef]],
    },
)
WaterfallVisualUnionTypeDef = Union[WaterfallVisualTypeDef, WaterfallVisualOutputTypeDef]
WordCloudVisualUnionTypeDef = Union[WordCloudVisualTypeDef, WordCloudVisualOutputTypeDef]
NestedFilterUnionTypeDef = Union[NestedFilterTypeDef, NestedFilterOutputTypeDef]
FilledMapVisualTypeDef = TypedDict(
    "FilledMapVisualTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[FilledMapConfigurationUnionTypeDef],
        "ConditionalFormatting": NotRequired[FilledMapConditionalFormattingUnionTypeDef],
        "ColumnHierarchies": NotRequired[Sequence[ColumnHierarchyTypeDef]],
        "Actions": NotRequired[Sequence[VisualCustomActionTypeDef]],
    },
)
PivotTableVisualTypeDef = TypedDict(
    "PivotTableVisualTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[PivotTableConfigurationUnionTypeDef],
        "ConditionalFormatting": NotRequired[PivotTableConditionalFormattingUnionTypeDef],
        "Actions": NotRequired[Sequence[VisualCustomActionUnionTypeDef]],
    },
)
TableVisualTypeDef = TypedDict(
    "TableVisualTypeDef",
    {
        "VisualId": str,
        "Title": NotRequired[VisualTitleLabelOptionsTypeDef],
        "Subtitle": NotRequired[VisualSubtitleLabelOptionsTypeDef],
        "ChartConfiguration": NotRequired[TableConfigurationUnionTypeDef],
        "ConditionalFormatting": NotRequired[TableConditionalFormattingUnionTypeDef],
        "Actions": NotRequired[Sequence[VisualCustomActionUnionTypeDef]],
    },
)
LayoutConfigurationUnionTypeDef = Union[
    LayoutConfigurationTypeDef, LayoutConfigurationOutputTypeDef
]
BarChartVisualUnionTypeDef = Union[BarChartVisualTypeDef, BarChartVisualOutputTypeDef]
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "CategoryFilter": NotRequired[CategoryFilterUnionTypeDef],
        "NumericRangeFilter": NotRequired[NumericRangeFilterUnionTypeDef],
        "NumericEqualityFilter": NotRequired[NumericEqualityFilterUnionTypeDef],
        "TimeEqualityFilter": NotRequired[TimeEqualityFilterUnionTypeDef],
        "TimeRangeFilter": NotRequired[TimeRangeFilterUnionTypeDef],
        "RelativeDatesFilter": NotRequired[RelativeDatesFilterUnionTypeDef],
        "TopBottomFilter": NotRequired[TopBottomFilterUnionTypeDef],
        "NestedFilter": NotRequired[NestedFilterUnionTypeDef],
    },
)
FilledMapVisualUnionTypeDef = Union[FilledMapVisualTypeDef, FilledMapVisualOutputTypeDef]
PivotTableVisualUnionTypeDef = Union[PivotTableVisualTypeDef, PivotTableVisualOutputTypeDef]
TableVisualUnionTypeDef = Union[TableVisualTypeDef, TableVisualOutputTypeDef]
LayoutTypeDef = TypedDict(
    "LayoutTypeDef",
    {
        "Configuration": LayoutConfigurationUnionTypeDef,
    },
)
FilterUnionTypeDef = Union[FilterTypeDef, FilterOutputTypeDef]
VisualTypeDef = TypedDict(
    "VisualTypeDef",
    {
        "TableVisual": NotRequired[TableVisualUnionTypeDef],
        "PivotTableVisual": NotRequired[PivotTableVisualUnionTypeDef],
        "BarChartVisual": NotRequired[BarChartVisualUnionTypeDef],
        "KPIVisual": NotRequired[KPIVisualUnionTypeDef],
        "PieChartVisual": NotRequired[PieChartVisualUnionTypeDef],
        "GaugeChartVisual": NotRequired[GaugeChartVisualUnionTypeDef],
        "LineChartVisual": NotRequired[LineChartVisualUnionTypeDef],
        "HeatMapVisual": NotRequired[HeatMapVisualUnionTypeDef],
        "TreeMapVisual": NotRequired[TreeMapVisualUnionTypeDef],
        "GeospatialMapVisual": NotRequired[GeospatialMapVisualUnionTypeDef],
        "FilledMapVisual": NotRequired[FilledMapVisualUnionTypeDef],
        "FunnelChartVisual": NotRequired[FunnelChartVisualUnionTypeDef],
        "ScatterPlotVisual": NotRequired[ScatterPlotVisualUnionTypeDef],
        "ComboChartVisual": NotRequired[ComboChartVisualUnionTypeDef],
        "BoxPlotVisual": NotRequired[BoxPlotVisualUnionTypeDef],
        "WaterfallVisual": NotRequired[WaterfallVisualUnionTypeDef],
        "HistogramVisual": NotRequired[HistogramVisualUnionTypeDef],
        "WordCloudVisual": NotRequired[WordCloudVisualUnionTypeDef],
        "InsightVisual": NotRequired[InsightVisualUnionTypeDef],
        "SankeyDiagramVisual": NotRequired[SankeyDiagramVisualUnionTypeDef],
        "CustomContentVisual": NotRequired[CustomContentVisualUnionTypeDef],
        "EmptyVisual": NotRequired[EmptyVisualUnionTypeDef],
        "RadarChartVisual": NotRequired[RadarChartVisualUnionTypeDef],
    },
)
LayoutUnionTypeDef = Union[LayoutTypeDef, LayoutOutputTypeDef]
FilterGroupTypeDef = TypedDict(
    "FilterGroupTypeDef",
    {
        "FilterGroupId": str,
        "Filters": Sequence[FilterUnionTypeDef],
        "ScopeConfiguration": FilterScopeConfigurationUnionTypeDef,
        "CrossDataset": CrossDatasetTypesType,
        "Status": NotRequired[WidgetStatusType],
    },
)
VisualUnionTypeDef = Union[VisualTypeDef, VisualOutputTypeDef]
FilterGroupUnionTypeDef = Union[FilterGroupTypeDef, FilterGroupOutputTypeDef]
SheetDefinitionTypeDef = TypedDict(
    "SheetDefinitionTypeDef",
    {
        "SheetId": str,
        "Title": NotRequired[str],
        "Description": NotRequired[str],
        "Name": NotRequired[str],
        "ParameterControls": NotRequired[Sequence[ParameterControlUnionTypeDef]],
        "FilterControls": NotRequired[Sequence[FilterControlUnionTypeDef]],
        "Visuals": NotRequired[Sequence[VisualUnionTypeDef]],
        "TextBoxes": NotRequired[Sequence[SheetTextBoxTypeDef]],
        "Layouts": NotRequired[Sequence[LayoutUnionTypeDef]],
        "SheetControlLayouts": NotRequired[Sequence[SheetControlLayoutUnionTypeDef]],
        "ContentType": NotRequired[SheetContentTypeType],
    },
)
SheetDefinitionUnionTypeDef = Union[SheetDefinitionTypeDef, SheetDefinitionOutputTypeDef]
AnalysisDefinitionTypeDef = TypedDict(
    "AnalysisDefinitionTypeDef",
    {
        "DataSetIdentifierDeclarations": Sequence[DataSetIdentifierDeclarationTypeDef],
        "Sheets": NotRequired[Sequence[SheetDefinitionUnionTypeDef]],
        "CalculatedFields": NotRequired[Sequence[CalculatedFieldTypeDef]],
        "ParameterDeclarations": NotRequired[Sequence[ParameterDeclarationUnionTypeDef]],
        "FilterGroups": NotRequired[Sequence[FilterGroupUnionTypeDef]],
        "ColumnConfigurations": NotRequired[Sequence[ColumnConfigurationUnionTypeDef]],
        "AnalysisDefaults": NotRequired[AnalysisDefaultsTypeDef],
        "Options": NotRequired[AssetOptionsTypeDef],
        "QueryExecutionOptions": NotRequired[QueryExecutionOptionsTypeDef],
    },
)
DashboardVersionDefinitionTypeDef = TypedDict(
    "DashboardVersionDefinitionTypeDef",
    {
        "DataSetIdentifierDeclarations": Sequence[DataSetIdentifierDeclarationTypeDef],
        "Sheets": NotRequired[Sequence[SheetDefinitionUnionTypeDef]],
        "CalculatedFields": NotRequired[Sequence[CalculatedFieldTypeDef]],
        "ParameterDeclarations": NotRequired[Sequence[ParameterDeclarationUnionTypeDef]],
        "FilterGroups": NotRequired[Sequence[FilterGroupUnionTypeDef]],
        "ColumnConfigurations": NotRequired[Sequence[ColumnConfigurationUnionTypeDef]],
        "AnalysisDefaults": NotRequired[AnalysisDefaultsTypeDef],
        "Options": NotRequired[AssetOptionsTypeDef],
    },
)
TemplateVersionDefinitionTypeDef = TypedDict(
    "TemplateVersionDefinitionTypeDef",
    {
        "DataSetConfigurations": Sequence[DataSetConfigurationUnionTypeDef],
        "Sheets": NotRequired[Sequence[SheetDefinitionUnionTypeDef]],
        "CalculatedFields": NotRequired[Sequence[CalculatedFieldTypeDef]],
        "ParameterDeclarations": NotRequired[Sequence[ParameterDeclarationUnionTypeDef]],
        "FilterGroups": NotRequired[Sequence[FilterGroupUnionTypeDef]],
        "ColumnConfigurations": NotRequired[Sequence[ColumnConfigurationUnionTypeDef]],
        "AnalysisDefaults": NotRequired[AnalysisDefaultsTypeDef],
        "Options": NotRequired[AssetOptionsTypeDef],
        "QueryExecutionOptions": NotRequired[QueryExecutionOptionsTypeDef],
    },
)
CreateAnalysisRequestRequestTypeDef = TypedDict(
    "CreateAnalysisRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
        "Name": str,
        "Parameters": NotRequired[ParametersTypeDef],
        "Permissions": NotRequired[Sequence[ResourcePermissionUnionTypeDef]],
        "SourceEntity": NotRequired[AnalysisSourceEntityTypeDef],
        "ThemeArn": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "Definition": NotRequired[AnalysisDefinitionTypeDef],
        "ValidationStrategy": NotRequired[ValidationStrategyTypeDef],
        "FolderArns": NotRequired[Sequence[str]],
    },
)
UpdateAnalysisRequestRequestTypeDef = TypedDict(
    "UpdateAnalysisRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AnalysisId": str,
        "Name": str,
        "Parameters": NotRequired[ParametersTypeDef],
        "SourceEntity": NotRequired[AnalysisSourceEntityTypeDef],
        "ThemeArn": NotRequired[str],
        "Definition": NotRequired[AnalysisDefinitionTypeDef],
        "ValidationStrategy": NotRequired[ValidationStrategyTypeDef],
    },
)
CreateDashboardRequestRequestTypeDef = TypedDict(
    "CreateDashboardRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "Name": str,
        "Parameters": NotRequired[ParametersTypeDef],
        "Permissions": NotRequired[Sequence[ResourcePermissionTypeDef]],
        "SourceEntity": NotRequired[DashboardSourceEntityTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "VersionDescription": NotRequired[str],
        "DashboardPublishOptions": NotRequired[DashboardPublishOptionsTypeDef],
        "ThemeArn": NotRequired[str],
        "Definition": NotRequired[DashboardVersionDefinitionTypeDef],
        "ValidationStrategy": NotRequired[ValidationStrategyTypeDef],
        "FolderArns": NotRequired[Sequence[str]],
        "LinkSharingConfiguration": NotRequired[LinkSharingConfigurationTypeDef],
        "LinkEntities": NotRequired[Sequence[str]],
    },
)
UpdateDashboardRequestRequestTypeDef = TypedDict(
    "UpdateDashboardRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "DashboardId": str,
        "Name": str,
        "SourceEntity": NotRequired[DashboardSourceEntityTypeDef],
        "Parameters": NotRequired[ParametersTypeDef],
        "VersionDescription": NotRequired[str],
        "DashboardPublishOptions": NotRequired[DashboardPublishOptionsTypeDef],
        "ThemeArn": NotRequired[str],
        "Definition": NotRequired[DashboardVersionDefinitionTypeDef],
        "ValidationStrategy": NotRequired[ValidationStrategyTypeDef],
    },
)
CreateTemplateRequestRequestTypeDef = TypedDict(
    "CreateTemplateRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "Name": NotRequired[str],
        "Permissions": NotRequired[Sequence[ResourcePermissionTypeDef]],
        "SourceEntity": NotRequired[TemplateSourceEntityTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "VersionDescription": NotRequired[str],
        "Definition": NotRequired[TemplateVersionDefinitionTypeDef],
        "ValidationStrategy": NotRequired[ValidationStrategyTypeDef],
    },
)
UpdateTemplateRequestRequestTypeDef = TypedDict(
    "UpdateTemplateRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "TemplateId": str,
        "SourceEntity": NotRequired[TemplateSourceEntityTypeDef],
        "VersionDescription": NotRequired[str],
        "Name": NotRequired[str],
        "Definition": NotRequired[TemplateVersionDefinitionTypeDef],
        "ValidationStrategy": NotRequired[ValidationStrategyTypeDef],
    },
)
