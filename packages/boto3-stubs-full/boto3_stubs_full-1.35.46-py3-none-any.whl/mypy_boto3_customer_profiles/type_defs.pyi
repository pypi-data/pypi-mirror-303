"""
Type annotations for customer-profiles service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_customer_profiles/type_defs/)

Usage::

    ```python
    from mypy_boto3_customer_profiles.type_defs import AddProfileKeyRequestRequestTypeDef

    data: AddProfileKeyRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AttributeMatchingModelType,
    ConflictResolvingModelType,
    DataPullModeType,
    EventStreamDestinationStatusType,
    EventStreamStateType,
    FieldContentTypeType,
    GenderType,
    IdentityResolutionJobStatusType,
    JobScheduleDayOfTheWeekType,
    LogicalOperatorType,
    MarketoConnectorOperatorType,
    MatchTypeType,
    OperatorPropertiesKeysType,
    OperatorType,
    PartyTypeType,
    RuleBasedMatchingStatusType,
    S3ConnectorOperatorType,
    SalesforceConnectorOperatorType,
    ServiceNowConnectorOperatorType,
    SourceConnectorTypeType,
    StandardIdentifierType,
    StatisticType,
    StatusType,
    TaskTypeType,
    TriggerTypeType,
    ZendeskConnectorOperatorType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AddProfileKeyRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "AdditionalSearchKeyTypeDef",
    "AddressTypeDef",
    "AppflowIntegrationWorkflowAttributesTypeDef",
    "AppflowIntegrationWorkflowMetricsTypeDef",
    "AppflowIntegrationWorkflowStepTypeDef",
    "AttributeItemTypeDef",
    "AttributeTypesSelectorOutputTypeDef",
    "AttributeTypesSelectorTypeDef",
    "ConflictResolutionTypeDef",
    "ConsolidationOutputTypeDef",
    "TimestampTypeDef",
    "RangeTypeDef",
    "ThresholdTypeDef",
    "ConnectorOperatorTypeDef",
    "ConsolidationTypeDef",
    "CreateEventStreamRequestRequestTypeDef",
    "DeleteCalculatedAttributeDefinitionRequestRequestTypeDef",
    "DeleteDomainRequestRequestTypeDef",
    "DeleteEventStreamRequestRequestTypeDef",
    "DeleteIntegrationRequestRequestTypeDef",
    "DeleteProfileKeyRequestRequestTypeDef",
    "DeleteProfileObjectRequestRequestTypeDef",
    "DeleteProfileObjectTypeRequestRequestTypeDef",
    "DeleteProfileRequestRequestTypeDef",
    "DeleteWorkflowRequestRequestTypeDef",
    "DestinationSummaryTypeDef",
    "DetectProfileObjectTypeRequestRequestTypeDef",
    "ObjectTypeFieldTypeDef",
    "ObjectTypeKeyOutputTypeDef",
    "DomainStatsTypeDef",
    "EventStreamDestinationDetailsTypeDef",
    "S3ExportingConfigTypeDef",
    "S3ExportingLocationTypeDef",
    "FieldSourceProfileIdsTypeDef",
    "FoundByKeyValueTypeDef",
    "GetCalculatedAttributeDefinitionRequestRequestTypeDef",
    "GetCalculatedAttributeForProfileRequestRequestTypeDef",
    "GetDomainRequestRequestTypeDef",
    "GetEventStreamRequestRequestTypeDef",
    "GetIdentityResolutionJobRequestRequestTypeDef",
    "JobStatsTypeDef",
    "GetIntegrationRequestRequestTypeDef",
    "GetMatchesRequestRequestTypeDef",
    "MatchItemTypeDef",
    "GetProfileObjectTypeRequestRequestTypeDef",
    "GetProfileObjectTypeTemplateRequestRequestTypeDef",
    "GetSimilarProfilesRequestRequestTypeDef",
    "GetWorkflowRequestRequestTypeDef",
    "GetWorkflowStepsRequestRequestTypeDef",
    "IncrementalPullConfigTypeDef",
    "JobScheduleTypeDef",
    "ListAccountIntegrationsRequestRequestTypeDef",
    "ListIntegrationItemTypeDef",
    "ListCalculatedAttributeDefinitionItemTypeDef",
    "ListCalculatedAttributeDefinitionsRequestRequestTypeDef",
    "ListCalculatedAttributeForProfileItemTypeDef",
    "ListCalculatedAttributesForProfileRequestRequestTypeDef",
    "ListDomainItemTypeDef",
    "ListDomainsRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListEventStreamsRequestRequestTypeDef",
    "ListIdentityResolutionJobsRequestRequestTypeDef",
    "ListIntegrationsRequestRequestTypeDef",
    "ListProfileObjectTypeItemTypeDef",
    "ListProfileObjectTypeTemplateItemTypeDef",
    "ListProfileObjectTypeTemplatesRequestRequestTypeDef",
    "ListProfileObjectTypesRequestRequestTypeDef",
    "ListProfileObjectsItemTypeDef",
    "ObjectFilterTypeDef",
    "ListRuleBasedMatchesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListWorkflowsItemTypeDef",
    "MarketoSourcePropertiesTypeDef",
    "MatchingRuleOutputTypeDef",
    "MatchingRuleTypeDef",
    "ObjectTypeKeyTypeDef",
    "PutProfileObjectRequestRequestTypeDef",
    "S3SourcePropertiesTypeDef",
    "SalesforceSourcePropertiesTypeDef",
    "ServiceNowSourcePropertiesTypeDef",
    "ZendeskSourcePropertiesTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAddressTypeDef",
    "AddProfileKeyResponseTypeDef",
    "CreateEventStreamResponseTypeDef",
    "CreateIntegrationWorkflowResponseTypeDef",
    "CreateProfileResponseTypeDef",
    "DeleteDomainResponseTypeDef",
    "DeleteIntegrationResponseTypeDef",
    "DeleteProfileKeyResponseTypeDef",
    "DeleteProfileObjectResponseTypeDef",
    "DeleteProfileObjectTypeResponseTypeDef",
    "DeleteProfileResponseTypeDef",
    "GetAutoMergingPreviewResponseTypeDef",
    "GetCalculatedAttributeForProfileResponseTypeDef",
    "GetIntegrationResponseTypeDef",
    "GetSimilarProfilesResponseTypeDef",
    "ListRuleBasedMatchesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MergeProfilesResponseTypeDef",
    "PutIntegrationResponseTypeDef",
    "PutProfileObjectResponseTypeDef",
    "UpdateProfileResponseTypeDef",
    "SearchProfilesRequestRequestTypeDef",
    "CreateProfileRequestRequestTypeDef",
    "WorkflowAttributesTypeDef",
    "WorkflowMetricsTypeDef",
    "WorkflowStepItemTypeDef",
    "AttributeDetailsOutputTypeDef",
    "AttributeDetailsTypeDef",
    "AttributeTypesSelectorUnionTypeDef",
    "AutoMergingOutputTypeDef",
    "BatchTypeDef",
    "ListWorkflowsRequestRequestTypeDef",
    "ScheduledTriggerPropertiesTypeDef",
    "ConditionsTypeDef",
    "TaskTypeDef",
    "ConsolidationUnionTypeDef",
    "GetAutoMergingPreviewRequestRequestTypeDef",
    "EventStreamSummaryTypeDef",
    "DetectedProfileObjectTypeTypeDef",
    "GetProfileObjectTypeResponseTypeDef",
    "GetProfileObjectTypeTemplateResponseTypeDef",
    "PutProfileObjectTypeResponseTypeDef",
    "GetEventStreamResponseTypeDef",
    "ExportingConfigTypeDef",
    "ExportingLocationTypeDef",
    "MergeProfilesRequestRequestTypeDef",
    "ProfileTypeDef",
    "GetMatchesResponseTypeDef",
    "ListAccountIntegrationsResponseTypeDef",
    "ListIntegrationsResponseTypeDef",
    "ListCalculatedAttributeDefinitionsResponseTypeDef",
    "ListCalculatedAttributesForProfileResponseTypeDef",
    "ListDomainsResponseTypeDef",
    "ListEventStreamsRequestListEventStreamsPaginateTypeDef",
    "ListProfileObjectTypesResponseTypeDef",
    "ListProfileObjectTypeTemplatesResponseTypeDef",
    "ListProfileObjectsResponseTypeDef",
    "ListProfileObjectsRequestRequestTypeDef",
    "ListWorkflowsResponseTypeDef",
    "MatchingRuleUnionTypeDef",
    "ObjectTypeKeyUnionTypeDef",
    "SourceConnectorPropertiesTypeDef",
    "UpdateProfileRequestRequestTypeDef",
    "GetWorkflowResponseTypeDef",
    "GetWorkflowStepsResponseTypeDef",
    "TriggerPropertiesTypeDef",
    "CreateCalculatedAttributeDefinitionRequestRequestTypeDef",
    "CreateCalculatedAttributeDefinitionResponseTypeDef",
    "GetCalculatedAttributeDefinitionResponseTypeDef",
    "UpdateCalculatedAttributeDefinitionRequestRequestTypeDef",
    "UpdateCalculatedAttributeDefinitionResponseTypeDef",
    "AutoMergingTypeDef",
    "ListEventStreamsResponseTypeDef",
    "DetectProfileObjectTypeResponseTypeDef",
    "MatchingResponseTypeDef",
    "RuleBasedMatchingResponseTypeDef",
    "GetIdentityResolutionJobResponseTypeDef",
    "IdentityResolutionJobTypeDef",
    "SearchProfilesResponseTypeDef",
    "RuleBasedMatchingRequestTypeDef",
    "PutProfileObjectTypeRequestRequestTypeDef",
    "SourceFlowConfigTypeDef",
    "TriggerConfigTypeDef",
    "AutoMergingUnionTypeDef",
    "CreateDomainResponseTypeDef",
    "GetDomainResponseTypeDef",
    "UpdateDomainResponseTypeDef",
    "ListIdentityResolutionJobsResponseTypeDef",
    "FlowDefinitionTypeDef",
    "MatchingRequestTypeDef",
    "AppflowIntegrationTypeDef",
    "PutIntegrationRequestRequestTypeDef",
    "CreateDomainRequestRequestTypeDef",
    "UpdateDomainRequestRequestTypeDef",
    "IntegrationConfigTypeDef",
    "CreateIntegrationWorkflowRequestRequestTypeDef",
)

AddProfileKeyRequestRequestTypeDef = TypedDict(
    "AddProfileKeyRequestRequestTypeDef",
    {
        "ProfileId": str,
        "KeyName": str,
        "Values": Sequence[str],
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
AdditionalSearchKeyTypeDef = TypedDict(
    "AdditionalSearchKeyTypeDef",
    {
        "KeyName": str,
        "Values": Sequence[str],
    },
)
AddressTypeDef = TypedDict(
    "AddressTypeDef",
    {
        "Address1": NotRequired[str],
        "Address2": NotRequired[str],
        "Address3": NotRequired[str],
        "Address4": NotRequired[str],
        "City": NotRequired[str],
        "County": NotRequired[str],
        "State": NotRequired[str],
        "Province": NotRequired[str],
        "Country": NotRequired[str],
        "PostalCode": NotRequired[str],
    },
)
AppflowIntegrationWorkflowAttributesTypeDef = TypedDict(
    "AppflowIntegrationWorkflowAttributesTypeDef",
    {
        "SourceConnectorType": SourceConnectorTypeType,
        "ConnectorProfileName": str,
        "RoleArn": NotRequired[str],
    },
)
AppflowIntegrationWorkflowMetricsTypeDef = TypedDict(
    "AppflowIntegrationWorkflowMetricsTypeDef",
    {
        "RecordsProcessed": int,
        "StepsCompleted": int,
        "TotalSteps": int,
    },
)
AppflowIntegrationWorkflowStepTypeDef = TypedDict(
    "AppflowIntegrationWorkflowStepTypeDef",
    {
        "FlowName": str,
        "Status": StatusType,
        "ExecutionMessage": str,
        "RecordsProcessed": int,
        "BatchRecordsStartTime": str,
        "BatchRecordsEndTime": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
)
AttributeItemTypeDef = TypedDict(
    "AttributeItemTypeDef",
    {
        "Name": str,
    },
)
AttributeTypesSelectorOutputTypeDef = TypedDict(
    "AttributeTypesSelectorOutputTypeDef",
    {
        "AttributeMatchingModel": AttributeMatchingModelType,
        "Address": NotRequired[List[str]],
        "PhoneNumber": NotRequired[List[str]],
        "EmailAddress": NotRequired[List[str]],
    },
)
AttributeTypesSelectorTypeDef = TypedDict(
    "AttributeTypesSelectorTypeDef",
    {
        "AttributeMatchingModel": AttributeMatchingModelType,
        "Address": NotRequired[Sequence[str]],
        "PhoneNumber": NotRequired[Sequence[str]],
        "EmailAddress": NotRequired[Sequence[str]],
    },
)
ConflictResolutionTypeDef = TypedDict(
    "ConflictResolutionTypeDef",
    {
        "ConflictResolvingModel": ConflictResolvingModelType,
        "SourceName": NotRequired[str],
    },
)
ConsolidationOutputTypeDef = TypedDict(
    "ConsolidationOutputTypeDef",
    {
        "MatchingAttributesList": List[List[str]],
    },
)
TimestampTypeDef = Union[datetime, str]
RangeTypeDef = TypedDict(
    "RangeTypeDef",
    {
        "Value": int,
        "Unit": Literal["DAYS"],
    },
)
ThresholdTypeDef = TypedDict(
    "ThresholdTypeDef",
    {
        "Value": str,
        "Operator": OperatorType,
    },
)
ConnectorOperatorTypeDef = TypedDict(
    "ConnectorOperatorTypeDef",
    {
        "Marketo": NotRequired[MarketoConnectorOperatorType],
        "S3": NotRequired[S3ConnectorOperatorType],
        "Salesforce": NotRequired[SalesforceConnectorOperatorType],
        "ServiceNow": NotRequired[ServiceNowConnectorOperatorType],
        "Zendesk": NotRequired[ZendeskConnectorOperatorType],
    },
)
ConsolidationTypeDef = TypedDict(
    "ConsolidationTypeDef",
    {
        "MatchingAttributesList": Sequence[Sequence[str]],
    },
)
CreateEventStreamRequestRequestTypeDef = TypedDict(
    "CreateEventStreamRequestRequestTypeDef",
    {
        "DomainName": str,
        "Uri": str,
        "EventStreamName": str,
        "Tags": NotRequired[Mapping[str, str]],
    },
)
DeleteCalculatedAttributeDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteCalculatedAttributeDefinitionRequestRequestTypeDef",
    {
        "DomainName": str,
        "CalculatedAttributeName": str,
    },
)
DeleteDomainRequestRequestTypeDef = TypedDict(
    "DeleteDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
DeleteEventStreamRequestRequestTypeDef = TypedDict(
    "DeleteEventStreamRequestRequestTypeDef",
    {
        "DomainName": str,
        "EventStreamName": str,
    },
)
DeleteIntegrationRequestRequestTypeDef = TypedDict(
    "DeleteIntegrationRequestRequestTypeDef",
    {
        "DomainName": str,
        "Uri": str,
    },
)
DeleteProfileKeyRequestRequestTypeDef = TypedDict(
    "DeleteProfileKeyRequestRequestTypeDef",
    {
        "ProfileId": str,
        "KeyName": str,
        "Values": Sequence[str],
        "DomainName": str,
    },
)
DeleteProfileObjectRequestRequestTypeDef = TypedDict(
    "DeleteProfileObjectRequestRequestTypeDef",
    {
        "ProfileId": str,
        "ProfileObjectUniqueKey": str,
        "ObjectTypeName": str,
        "DomainName": str,
    },
)
DeleteProfileObjectTypeRequestRequestTypeDef = TypedDict(
    "DeleteProfileObjectTypeRequestRequestTypeDef",
    {
        "DomainName": str,
        "ObjectTypeName": str,
    },
)
DeleteProfileRequestRequestTypeDef = TypedDict(
    "DeleteProfileRequestRequestTypeDef",
    {
        "ProfileId": str,
        "DomainName": str,
    },
)
DeleteWorkflowRequestRequestTypeDef = TypedDict(
    "DeleteWorkflowRequestRequestTypeDef",
    {
        "DomainName": str,
        "WorkflowId": str,
    },
)
DestinationSummaryTypeDef = TypedDict(
    "DestinationSummaryTypeDef",
    {
        "Uri": str,
        "Status": EventStreamDestinationStatusType,
        "UnhealthySince": NotRequired[datetime],
    },
)
DetectProfileObjectTypeRequestRequestTypeDef = TypedDict(
    "DetectProfileObjectTypeRequestRequestTypeDef",
    {
        "Objects": Sequence[str],
        "DomainName": str,
    },
)
ObjectTypeFieldTypeDef = TypedDict(
    "ObjectTypeFieldTypeDef",
    {
        "Source": NotRequired[str],
        "Target": NotRequired[str],
        "ContentType": NotRequired[FieldContentTypeType],
    },
)
ObjectTypeKeyOutputTypeDef = TypedDict(
    "ObjectTypeKeyOutputTypeDef",
    {
        "StandardIdentifiers": NotRequired[List[StandardIdentifierType]],
        "FieldNames": NotRequired[List[str]],
    },
)
DomainStatsTypeDef = TypedDict(
    "DomainStatsTypeDef",
    {
        "ProfileCount": NotRequired[int],
        "MeteringProfileCount": NotRequired[int],
        "ObjectCount": NotRequired[int],
        "TotalSize": NotRequired[int],
    },
)
EventStreamDestinationDetailsTypeDef = TypedDict(
    "EventStreamDestinationDetailsTypeDef",
    {
        "Uri": str,
        "Status": EventStreamDestinationStatusType,
        "UnhealthySince": NotRequired[datetime],
        "Message": NotRequired[str],
    },
)
S3ExportingConfigTypeDef = TypedDict(
    "S3ExportingConfigTypeDef",
    {
        "S3BucketName": str,
        "S3KeyName": NotRequired[str],
    },
)
S3ExportingLocationTypeDef = TypedDict(
    "S3ExportingLocationTypeDef",
    {
        "S3BucketName": NotRequired[str],
        "S3KeyName": NotRequired[str],
    },
)
FieldSourceProfileIdsTypeDef = TypedDict(
    "FieldSourceProfileIdsTypeDef",
    {
        "AccountNumber": NotRequired[str],
        "AdditionalInformation": NotRequired[str],
        "PartyType": NotRequired[str],
        "BusinessName": NotRequired[str],
        "FirstName": NotRequired[str],
        "MiddleName": NotRequired[str],
        "LastName": NotRequired[str],
        "BirthDate": NotRequired[str],
        "Gender": NotRequired[str],
        "PhoneNumber": NotRequired[str],
        "MobilePhoneNumber": NotRequired[str],
        "HomePhoneNumber": NotRequired[str],
        "BusinessPhoneNumber": NotRequired[str],
        "EmailAddress": NotRequired[str],
        "PersonalEmailAddress": NotRequired[str],
        "BusinessEmailAddress": NotRequired[str],
        "Address": NotRequired[str],
        "ShippingAddress": NotRequired[str],
        "MailingAddress": NotRequired[str],
        "BillingAddress": NotRequired[str],
        "Attributes": NotRequired[Mapping[str, str]],
    },
)
FoundByKeyValueTypeDef = TypedDict(
    "FoundByKeyValueTypeDef",
    {
        "KeyName": NotRequired[str],
        "Values": NotRequired[List[str]],
    },
)
GetCalculatedAttributeDefinitionRequestRequestTypeDef = TypedDict(
    "GetCalculatedAttributeDefinitionRequestRequestTypeDef",
    {
        "DomainName": str,
        "CalculatedAttributeName": str,
    },
)
GetCalculatedAttributeForProfileRequestRequestTypeDef = TypedDict(
    "GetCalculatedAttributeForProfileRequestRequestTypeDef",
    {
        "DomainName": str,
        "ProfileId": str,
        "CalculatedAttributeName": str,
    },
)
GetDomainRequestRequestTypeDef = TypedDict(
    "GetDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
GetEventStreamRequestRequestTypeDef = TypedDict(
    "GetEventStreamRequestRequestTypeDef",
    {
        "DomainName": str,
        "EventStreamName": str,
    },
)
GetIdentityResolutionJobRequestRequestTypeDef = TypedDict(
    "GetIdentityResolutionJobRequestRequestTypeDef",
    {
        "DomainName": str,
        "JobId": str,
    },
)
JobStatsTypeDef = TypedDict(
    "JobStatsTypeDef",
    {
        "NumberOfProfilesReviewed": NotRequired[int],
        "NumberOfMatchesFound": NotRequired[int],
        "NumberOfMergesDone": NotRequired[int],
    },
)
GetIntegrationRequestRequestTypeDef = TypedDict(
    "GetIntegrationRequestRequestTypeDef",
    {
        "DomainName": str,
        "Uri": str,
    },
)
GetMatchesRequestRequestTypeDef = TypedDict(
    "GetMatchesRequestRequestTypeDef",
    {
        "DomainName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
MatchItemTypeDef = TypedDict(
    "MatchItemTypeDef",
    {
        "MatchId": NotRequired[str],
        "ProfileIds": NotRequired[List[str]],
        "ConfidenceScore": NotRequired[float],
    },
)
GetProfileObjectTypeRequestRequestTypeDef = TypedDict(
    "GetProfileObjectTypeRequestRequestTypeDef",
    {
        "DomainName": str,
        "ObjectTypeName": str,
    },
)
GetProfileObjectTypeTemplateRequestRequestTypeDef = TypedDict(
    "GetProfileObjectTypeTemplateRequestRequestTypeDef",
    {
        "TemplateId": str,
    },
)
GetSimilarProfilesRequestRequestTypeDef = TypedDict(
    "GetSimilarProfilesRequestRequestTypeDef",
    {
        "DomainName": str,
        "MatchType": MatchTypeType,
        "SearchKey": str,
        "SearchValue": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GetWorkflowRequestRequestTypeDef = TypedDict(
    "GetWorkflowRequestRequestTypeDef",
    {
        "DomainName": str,
        "WorkflowId": str,
    },
)
GetWorkflowStepsRequestRequestTypeDef = TypedDict(
    "GetWorkflowStepsRequestRequestTypeDef",
    {
        "DomainName": str,
        "WorkflowId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
IncrementalPullConfigTypeDef = TypedDict(
    "IncrementalPullConfigTypeDef",
    {
        "DatetimeTypeFieldName": NotRequired[str],
    },
)
JobScheduleTypeDef = TypedDict(
    "JobScheduleTypeDef",
    {
        "DayOfTheWeek": JobScheduleDayOfTheWeekType,
        "Time": str,
    },
)
ListAccountIntegrationsRequestRequestTypeDef = TypedDict(
    "ListAccountIntegrationsRequestRequestTypeDef",
    {
        "Uri": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "IncludeHidden": NotRequired[bool],
    },
)
ListIntegrationItemTypeDef = TypedDict(
    "ListIntegrationItemTypeDef",
    {
        "DomainName": str,
        "Uri": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "ObjectTypeName": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
        "ObjectTypeNames": NotRequired[Dict[str, str]],
        "WorkflowId": NotRequired[str],
        "IsUnstructured": NotRequired[bool],
        "RoleArn": NotRequired[str],
    },
)
ListCalculatedAttributeDefinitionItemTypeDef = TypedDict(
    "ListCalculatedAttributeDefinitionItemTypeDef",
    {
        "CalculatedAttributeName": NotRequired[str],
        "DisplayName": NotRequired[str],
        "Description": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "LastUpdatedAt": NotRequired[datetime],
        "Tags": NotRequired[Dict[str, str]],
    },
)
ListCalculatedAttributeDefinitionsRequestRequestTypeDef = TypedDict(
    "ListCalculatedAttributeDefinitionsRequestRequestTypeDef",
    {
        "DomainName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListCalculatedAttributeForProfileItemTypeDef = TypedDict(
    "ListCalculatedAttributeForProfileItemTypeDef",
    {
        "CalculatedAttributeName": NotRequired[str],
        "DisplayName": NotRequired[str],
        "IsDataPartial": NotRequired[str],
        "Value": NotRequired[str],
    },
)
ListCalculatedAttributesForProfileRequestRequestTypeDef = TypedDict(
    "ListCalculatedAttributesForProfileRequestRequestTypeDef",
    {
        "DomainName": str,
        "ProfileId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListDomainItemTypeDef = TypedDict(
    "ListDomainItemTypeDef",
    {
        "DomainName": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": NotRequired[Dict[str, str]],
    },
)
ListDomainsRequestRequestTypeDef = TypedDict(
    "ListDomainsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
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
ListEventStreamsRequestRequestTypeDef = TypedDict(
    "ListEventStreamsRequestRequestTypeDef",
    {
        "DomainName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListIdentityResolutionJobsRequestRequestTypeDef = TypedDict(
    "ListIdentityResolutionJobsRequestRequestTypeDef",
    {
        "DomainName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListIntegrationsRequestRequestTypeDef = TypedDict(
    "ListIntegrationsRequestRequestTypeDef",
    {
        "DomainName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "IncludeHidden": NotRequired[bool],
    },
)
ListProfileObjectTypeItemTypeDef = TypedDict(
    "ListProfileObjectTypeItemTypeDef",
    {
        "ObjectTypeName": str,
        "Description": str,
        "CreatedAt": NotRequired[datetime],
        "LastUpdatedAt": NotRequired[datetime],
        "MaxProfileObjectCount": NotRequired[int],
        "MaxAvailableProfileObjectCount": NotRequired[int],
        "Tags": NotRequired[Dict[str, str]],
    },
)
ListProfileObjectTypeTemplateItemTypeDef = TypedDict(
    "ListProfileObjectTypeTemplateItemTypeDef",
    {
        "TemplateId": NotRequired[str],
        "SourceName": NotRequired[str],
        "SourceObject": NotRequired[str],
    },
)
ListProfileObjectTypeTemplatesRequestRequestTypeDef = TypedDict(
    "ListProfileObjectTypeTemplatesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListProfileObjectTypesRequestRequestTypeDef = TypedDict(
    "ListProfileObjectTypesRequestRequestTypeDef",
    {
        "DomainName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListProfileObjectsItemTypeDef = TypedDict(
    "ListProfileObjectsItemTypeDef",
    {
        "ObjectTypeName": NotRequired[str],
        "ProfileObjectUniqueKey": NotRequired[str],
        "Object": NotRequired[str],
    },
)
ObjectFilterTypeDef = TypedDict(
    "ObjectFilterTypeDef",
    {
        "KeyName": str,
        "Values": Sequence[str],
    },
)
ListRuleBasedMatchesRequestRequestTypeDef = TypedDict(
    "ListRuleBasedMatchesRequestRequestTypeDef",
    {
        "DomainName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
ListWorkflowsItemTypeDef = TypedDict(
    "ListWorkflowsItemTypeDef",
    {
        "WorkflowType": Literal["APPFLOW_INTEGRATION"],
        "WorkflowId": str,
        "Status": StatusType,
        "StatusDescription": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
)
MarketoSourcePropertiesTypeDef = TypedDict(
    "MarketoSourcePropertiesTypeDef",
    {
        "Object": str,
    },
)
MatchingRuleOutputTypeDef = TypedDict(
    "MatchingRuleOutputTypeDef",
    {
        "Rule": List[str],
    },
)
MatchingRuleTypeDef = TypedDict(
    "MatchingRuleTypeDef",
    {
        "Rule": Sequence[str],
    },
)
ObjectTypeKeyTypeDef = TypedDict(
    "ObjectTypeKeyTypeDef",
    {
        "StandardIdentifiers": NotRequired[Sequence[StandardIdentifierType]],
        "FieldNames": NotRequired[Sequence[str]],
    },
)
PutProfileObjectRequestRequestTypeDef = TypedDict(
    "PutProfileObjectRequestRequestTypeDef",
    {
        "ObjectTypeName": str,
        "Object": str,
        "DomainName": str,
    },
)
S3SourcePropertiesTypeDef = TypedDict(
    "S3SourcePropertiesTypeDef",
    {
        "BucketName": str,
        "BucketPrefix": NotRequired[str],
    },
)
SalesforceSourcePropertiesTypeDef = TypedDict(
    "SalesforceSourcePropertiesTypeDef",
    {
        "Object": str,
        "EnableDynamicFieldUpdate": NotRequired[bool],
        "IncludeDeletedRecords": NotRequired[bool],
    },
)
ServiceNowSourcePropertiesTypeDef = TypedDict(
    "ServiceNowSourcePropertiesTypeDef",
    {
        "Object": str,
    },
)
ZendeskSourcePropertiesTypeDef = TypedDict(
    "ZendeskSourcePropertiesTypeDef",
    {
        "Object": str,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UpdateAddressTypeDef = TypedDict(
    "UpdateAddressTypeDef",
    {
        "Address1": NotRequired[str],
        "Address2": NotRequired[str],
        "Address3": NotRequired[str],
        "Address4": NotRequired[str],
        "City": NotRequired[str],
        "County": NotRequired[str],
        "State": NotRequired[str],
        "Province": NotRequired[str],
        "Country": NotRequired[str],
        "PostalCode": NotRequired[str],
    },
)
AddProfileKeyResponseTypeDef = TypedDict(
    "AddProfileKeyResponseTypeDef",
    {
        "KeyName": str,
        "Values": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEventStreamResponseTypeDef = TypedDict(
    "CreateEventStreamResponseTypeDef",
    {
        "EventStreamArn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateIntegrationWorkflowResponseTypeDef = TypedDict(
    "CreateIntegrationWorkflowResponseTypeDef",
    {
        "WorkflowId": str,
        "Message": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProfileResponseTypeDef = TypedDict(
    "CreateProfileResponseTypeDef",
    {
        "ProfileId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDomainResponseTypeDef = TypedDict(
    "DeleteDomainResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteIntegrationResponseTypeDef = TypedDict(
    "DeleteIntegrationResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteProfileKeyResponseTypeDef = TypedDict(
    "DeleteProfileKeyResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteProfileObjectResponseTypeDef = TypedDict(
    "DeleteProfileObjectResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteProfileObjectTypeResponseTypeDef = TypedDict(
    "DeleteProfileObjectTypeResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteProfileResponseTypeDef = TypedDict(
    "DeleteProfileResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAutoMergingPreviewResponseTypeDef = TypedDict(
    "GetAutoMergingPreviewResponseTypeDef",
    {
        "DomainName": str,
        "NumberOfMatchesInSample": int,
        "NumberOfProfilesInSample": int,
        "NumberOfProfilesWillBeMerged": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCalculatedAttributeForProfileResponseTypeDef = TypedDict(
    "GetCalculatedAttributeForProfileResponseTypeDef",
    {
        "CalculatedAttributeName": str,
        "DisplayName": str,
        "IsDataPartial": str,
        "Value": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIntegrationResponseTypeDef = TypedDict(
    "GetIntegrationResponseTypeDef",
    {
        "DomainName": str,
        "Uri": str,
        "ObjectTypeName": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ObjectTypeNames": Dict[str, str],
        "WorkflowId": str,
        "IsUnstructured": bool,
        "RoleArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSimilarProfilesResponseTypeDef = TypedDict(
    "GetSimilarProfilesResponseTypeDef",
    {
        "ProfileIds": List[str],
        "MatchId": str,
        "MatchType": MatchTypeType,
        "RuleLevel": int,
        "ConfidenceScore": float,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListRuleBasedMatchesResponseTypeDef = TypedDict(
    "ListRuleBasedMatchesResponseTypeDef",
    {
        "MatchIds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MergeProfilesResponseTypeDef = TypedDict(
    "MergeProfilesResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutIntegrationResponseTypeDef = TypedDict(
    "PutIntegrationResponseTypeDef",
    {
        "DomainName": str,
        "Uri": str,
        "ObjectTypeName": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ObjectTypeNames": Dict[str, str],
        "WorkflowId": str,
        "IsUnstructured": bool,
        "RoleArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutProfileObjectResponseTypeDef = TypedDict(
    "PutProfileObjectResponseTypeDef",
    {
        "ProfileObjectUniqueKey": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateProfileResponseTypeDef = TypedDict(
    "UpdateProfileResponseTypeDef",
    {
        "ProfileId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchProfilesRequestRequestTypeDef = TypedDict(
    "SearchProfilesRequestRequestTypeDef",
    {
        "DomainName": str,
        "KeyName": str,
        "Values": Sequence[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "AdditionalSearchKeys": NotRequired[Sequence[AdditionalSearchKeyTypeDef]],
        "LogicalOperator": NotRequired[LogicalOperatorType],
    },
)
CreateProfileRequestRequestTypeDef = TypedDict(
    "CreateProfileRequestRequestTypeDef",
    {
        "DomainName": str,
        "AccountNumber": NotRequired[str],
        "AdditionalInformation": NotRequired[str],
        "PartyType": NotRequired[PartyTypeType],
        "BusinessName": NotRequired[str],
        "FirstName": NotRequired[str],
        "MiddleName": NotRequired[str],
        "LastName": NotRequired[str],
        "BirthDate": NotRequired[str],
        "Gender": NotRequired[GenderType],
        "PhoneNumber": NotRequired[str],
        "MobilePhoneNumber": NotRequired[str],
        "HomePhoneNumber": NotRequired[str],
        "BusinessPhoneNumber": NotRequired[str],
        "EmailAddress": NotRequired[str],
        "PersonalEmailAddress": NotRequired[str],
        "BusinessEmailAddress": NotRequired[str],
        "Address": NotRequired[AddressTypeDef],
        "ShippingAddress": NotRequired[AddressTypeDef],
        "MailingAddress": NotRequired[AddressTypeDef],
        "BillingAddress": NotRequired[AddressTypeDef],
        "Attributes": NotRequired[Mapping[str, str]],
        "PartyTypeString": NotRequired[str],
        "GenderString": NotRequired[str],
    },
)
WorkflowAttributesTypeDef = TypedDict(
    "WorkflowAttributesTypeDef",
    {
        "AppflowIntegration": NotRequired[AppflowIntegrationWorkflowAttributesTypeDef],
    },
)
WorkflowMetricsTypeDef = TypedDict(
    "WorkflowMetricsTypeDef",
    {
        "AppflowIntegration": NotRequired[AppflowIntegrationWorkflowMetricsTypeDef],
    },
)
WorkflowStepItemTypeDef = TypedDict(
    "WorkflowStepItemTypeDef",
    {
        "AppflowIntegration": NotRequired[AppflowIntegrationWorkflowStepTypeDef],
    },
)
AttributeDetailsOutputTypeDef = TypedDict(
    "AttributeDetailsOutputTypeDef",
    {
        "Attributes": List[AttributeItemTypeDef],
        "Expression": str,
    },
)
AttributeDetailsTypeDef = TypedDict(
    "AttributeDetailsTypeDef",
    {
        "Attributes": Sequence[AttributeItemTypeDef],
        "Expression": str,
    },
)
AttributeTypesSelectorUnionTypeDef = Union[
    AttributeTypesSelectorTypeDef, AttributeTypesSelectorOutputTypeDef
]
AutoMergingOutputTypeDef = TypedDict(
    "AutoMergingOutputTypeDef",
    {
        "Enabled": bool,
        "Consolidation": NotRequired[ConsolidationOutputTypeDef],
        "ConflictResolution": NotRequired[ConflictResolutionTypeDef],
        "MinAllowedConfidenceScoreForMerging": NotRequired[float],
    },
)
BatchTypeDef = TypedDict(
    "BatchTypeDef",
    {
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
    },
)
ListWorkflowsRequestRequestTypeDef = TypedDict(
    "ListWorkflowsRequestRequestTypeDef",
    {
        "DomainName": str,
        "WorkflowType": NotRequired[Literal["APPFLOW_INTEGRATION"]],
        "Status": NotRequired[StatusType],
        "QueryStartDate": NotRequired[TimestampTypeDef],
        "QueryEndDate": NotRequired[TimestampTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ScheduledTriggerPropertiesTypeDef = TypedDict(
    "ScheduledTriggerPropertiesTypeDef",
    {
        "ScheduleExpression": str,
        "DataPullMode": NotRequired[DataPullModeType],
        "ScheduleStartTime": NotRequired[TimestampTypeDef],
        "ScheduleEndTime": NotRequired[TimestampTypeDef],
        "Timezone": NotRequired[str],
        "ScheduleOffset": NotRequired[int],
        "FirstExecutionFrom": NotRequired[TimestampTypeDef],
    },
)
ConditionsTypeDef = TypedDict(
    "ConditionsTypeDef",
    {
        "Range": NotRequired[RangeTypeDef],
        "ObjectCount": NotRequired[int],
        "Threshold": NotRequired[ThresholdTypeDef],
    },
)
TaskTypeDef = TypedDict(
    "TaskTypeDef",
    {
        "SourceFields": Sequence[str],
        "TaskType": TaskTypeType,
        "ConnectorOperator": NotRequired[ConnectorOperatorTypeDef],
        "DestinationField": NotRequired[str],
        "TaskProperties": NotRequired[Mapping[OperatorPropertiesKeysType, str]],
    },
)
ConsolidationUnionTypeDef = Union[ConsolidationTypeDef, ConsolidationOutputTypeDef]
GetAutoMergingPreviewRequestRequestTypeDef = TypedDict(
    "GetAutoMergingPreviewRequestRequestTypeDef",
    {
        "DomainName": str,
        "Consolidation": ConsolidationTypeDef,
        "ConflictResolution": ConflictResolutionTypeDef,
        "MinAllowedConfidenceScoreForMerging": NotRequired[float],
    },
)
EventStreamSummaryTypeDef = TypedDict(
    "EventStreamSummaryTypeDef",
    {
        "DomainName": str,
        "EventStreamName": str,
        "EventStreamArn": str,
        "State": EventStreamStateType,
        "StoppedSince": NotRequired[datetime],
        "DestinationSummary": NotRequired[DestinationSummaryTypeDef],
        "Tags": NotRequired[Dict[str, str]],
    },
)
DetectedProfileObjectTypeTypeDef = TypedDict(
    "DetectedProfileObjectTypeTypeDef",
    {
        "SourceLastUpdatedTimestampFormat": NotRequired[str],
        "Fields": NotRequired[Dict[str, ObjectTypeFieldTypeDef]],
        "Keys": NotRequired[Dict[str, List[ObjectTypeKeyOutputTypeDef]]],
    },
)
GetProfileObjectTypeResponseTypeDef = TypedDict(
    "GetProfileObjectTypeResponseTypeDef",
    {
        "ObjectTypeName": str,
        "Description": str,
        "TemplateId": str,
        "ExpirationDays": int,
        "EncryptionKey": str,
        "AllowProfileCreation": bool,
        "SourceLastUpdatedTimestampFormat": str,
        "MaxAvailableProfileObjectCount": int,
        "MaxProfileObjectCount": int,
        "Fields": Dict[str, ObjectTypeFieldTypeDef],
        "Keys": Dict[str, List[ObjectTypeKeyOutputTypeDef]],
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetProfileObjectTypeTemplateResponseTypeDef = TypedDict(
    "GetProfileObjectTypeTemplateResponseTypeDef",
    {
        "TemplateId": str,
        "SourceName": str,
        "SourceObject": str,
        "AllowProfileCreation": bool,
        "SourceLastUpdatedTimestampFormat": str,
        "Fields": Dict[str, ObjectTypeFieldTypeDef],
        "Keys": Dict[str, List[ObjectTypeKeyOutputTypeDef]],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutProfileObjectTypeResponseTypeDef = TypedDict(
    "PutProfileObjectTypeResponseTypeDef",
    {
        "ObjectTypeName": str,
        "Description": str,
        "TemplateId": str,
        "ExpirationDays": int,
        "EncryptionKey": str,
        "AllowProfileCreation": bool,
        "SourceLastUpdatedTimestampFormat": str,
        "MaxProfileObjectCount": int,
        "MaxAvailableProfileObjectCount": int,
        "Fields": Dict[str, ObjectTypeFieldTypeDef],
        "Keys": Dict[str, List[ObjectTypeKeyOutputTypeDef]],
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEventStreamResponseTypeDef = TypedDict(
    "GetEventStreamResponseTypeDef",
    {
        "DomainName": str,
        "EventStreamArn": str,
        "CreatedAt": datetime,
        "State": EventStreamStateType,
        "StoppedSince": datetime,
        "DestinationDetails": EventStreamDestinationDetailsTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportingConfigTypeDef = TypedDict(
    "ExportingConfigTypeDef",
    {
        "S3Exporting": NotRequired[S3ExportingConfigTypeDef],
    },
)
ExportingLocationTypeDef = TypedDict(
    "ExportingLocationTypeDef",
    {
        "S3Exporting": NotRequired[S3ExportingLocationTypeDef],
    },
)
MergeProfilesRequestRequestTypeDef = TypedDict(
    "MergeProfilesRequestRequestTypeDef",
    {
        "DomainName": str,
        "MainProfileId": str,
        "ProfileIdsToBeMerged": Sequence[str],
        "FieldSourceProfileIds": NotRequired[FieldSourceProfileIdsTypeDef],
    },
)
ProfileTypeDef = TypedDict(
    "ProfileTypeDef",
    {
        "ProfileId": NotRequired[str],
        "AccountNumber": NotRequired[str],
        "AdditionalInformation": NotRequired[str],
        "PartyType": NotRequired[PartyTypeType],
        "BusinessName": NotRequired[str],
        "FirstName": NotRequired[str],
        "MiddleName": NotRequired[str],
        "LastName": NotRequired[str],
        "BirthDate": NotRequired[str],
        "Gender": NotRequired[GenderType],
        "PhoneNumber": NotRequired[str],
        "MobilePhoneNumber": NotRequired[str],
        "HomePhoneNumber": NotRequired[str],
        "BusinessPhoneNumber": NotRequired[str],
        "EmailAddress": NotRequired[str],
        "PersonalEmailAddress": NotRequired[str],
        "BusinessEmailAddress": NotRequired[str],
        "Address": NotRequired[AddressTypeDef],
        "ShippingAddress": NotRequired[AddressTypeDef],
        "MailingAddress": NotRequired[AddressTypeDef],
        "BillingAddress": NotRequired[AddressTypeDef],
        "Attributes": NotRequired[Dict[str, str]],
        "FoundByItems": NotRequired[List[FoundByKeyValueTypeDef]],
        "PartyTypeString": NotRequired[str],
        "GenderString": NotRequired[str],
    },
)
GetMatchesResponseTypeDef = TypedDict(
    "GetMatchesResponseTypeDef",
    {
        "MatchGenerationDate": datetime,
        "PotentialMatches": int,
        "Matches": List[MatchItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListAccountIntegrationsResponseTypeDef = TypedDict(
    "ListAccountIntegrationsResponseTypeDef",
    {
        "Items": List[ListIntegrationItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListIntegrationsResponseTypeDef = TypedDict(
    "ListIntegrationsResponseTypeDef",
    {
        "Items": List[ListIntegrationItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListCalculatedAttributeDefinitionsResponseTypeDef = TypedDict(
    "ListCalculatedAttributeDefinitionsResponseTypeDef",
    {
        "Items": List[ListCalculatedAttributeDefinitionItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListCalculatedAttributesForProfileResponseTypeDef = TypedDict(
    "ListCalculatedAttributesForProfileResponseTypeDef",
    {
        "Items": List[ListCalculatedAttributeForProfileItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListDomainsResponseTypeDef = TypedDict(
    "ListDomainsResponseTypeDef",
    {
        "Items": List[ListDomainItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListEventStreamsRequestListEventStreamsPaginateTypeDef = TypedDict(
    "ListEventStreamsRequestListEventStreamsPaginateTypeDef",
    {
        "DomainName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProfileObjectTypesResponseTypeDef = TypedDict(
    "ListProfileObjectTypesResponseTypeDef",
    {
        "Items": List[ListProfileObjectTypeItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListProfileObjectTypeTemplatesResponseTypeDef = TypedDict(
    "ListProfileObjectTypeTemplatesResponseTypeDef",
    {
        "Items": List[ListProfileObjectTypeTemplateItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListProfileObjectsResponseTypeDef = TypedDict(
    "ListProfileObjectsResponseTypeDef",
    {
        "Items": List[ListProfileObjectsItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListProfileObjectsRequestRequestTypeDef = TypedDict(
    "ListProfileObjectsRequestRequestTypeDef",
    {
        "DomainName": str,
        "ObjectTypeName": str,
        "ProfileId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ObjectFilter": NotRequired[ObjectFilterTypeDef],
    },
)
ListWorkflowsResponseTypeDef = TypedDict(
    "ListWorkflowsResponseTypeDef",
    {
        "Items": List[ListWorkflowsItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
MatchingRuleUnionTypeDef = Union[MatchingRuleTypeDef, MatchingRuleOutputTypeDef]
ObjectTypeKeyUnionTypeDef = Union[ObjectTypeKeyTypeDef, ObjectTypeKeyOutputTypeDef]
SourceConnectorPropertiesTypeDef = TypedDict(
    "SourceConnectorPropertiesTypeDef",
    {
        "Marketo": NotRequired[MarketoSourcePropertiesTypeDef],
        "S3": NotRequired[S3SourcePropertiesTypeDef],
        "Salesforce": NotRequired[SalesforceSourcePropertiesTypeDef],
        "ServiceNow": NotRequired[ServiceNowSourcePropertiesTypeDef],
        "Zendesk": NotRequired[ZendeskSourcePropertiesTypeDef],
    },
)
UpdateProfileRequestRequestTypeDef = TypedDict(
    "UpdateProfileRequestRequestTypeDef",
    {
        "DomainName": str,
        "ProfileId": str,
        "AdditionalInformation": NotRequired[str],
        "AccountNumber": NotRequired[str],
        "PartyType": NotRequired[PartyTypeType],
        "BusinessName": NotRequired[str],
        "FirstName": NotRequired[str],
        "MiddleName": NotRequired[str],
        "LastName": NotRequired[str],
        "BirthDate": NotRequired[str],
        "Gender": NotRequired[GenderType],
        "PhoneNumber": NotRequired[str],
        "MobilePhoneNumber": NotRequired[str],
        "HomePhoneNumber": NotRequired[str],
        "BusinessPhoneNumber": NotRequired[str],
        "EmailAddress": NotRequired[str],
        "PersonalEmailAddress": NotRequired[str],
        "BusinessEmailAddress": NotRequired[str],
        "Address": NotRequired[UpdateAddressTypeDef],
        "ShippingAddress": NotRequired[UpdateAddressTypeDef],
        "MailingAddress": NotRequired[UpdateAddressTypeDef],
        "BillingAddress": NotRequired[UpdateAddressTypeDef],
        "Attributes": NotRequired[Mapping[str, str]],
        "PartyTypeString": NotRequired[str],
        "GenderString": NotRequired[str],
    },
)
GetWorkflowResponseTypeDef = TypedDict(
    "GetWorkflowResponseTypeDef",
    {
        "WorkflowId": str,
        "WorkflowType": Literal["APPFLOW_INTEGRATION"],
        "Status": StatusType,
        "ErrorDescription": str,
        "StartDate": datetime,
        "LastUpdatedAt": datetime,
        "Attributes": WorkflowAttributesTypeDef,
        "Metrics": WorkflowMetricsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetWorkflowStepsResponseTypeDef = TypedDict(
    "GetWorkflowStepsResponseTypeDef",
    {
        "WorkflowId": str,
        "WorkflowType": Literal["APPFLOW_INTEGRATION"],
        "Items": List[WorkflowStepItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
TriggerPropertiesTypeDef = TypedDict(
    "TriggerPropertiesTypeDef",
    {
        "Scheduled": NotRequired[ScheduledTriggerPropertiesTypeDef],
    },
)
CreateCalculatedAttributeDefinitionRequestRequestTypeDef = TypedDict(
    "CreateCalculatedAttributeDefinitionRequestRequestTypeDef",
    {
        "DomainName": str,
        "CalculatedAttributeName": str,
        "AttributeDetails": AttributeDetailsTypeDef,
        "Statistic": StatisticType,
        "DisplayName": NotRequired[str],
        "Description": NotRequired[str],
        "Conditions": NotRequired[ConditionsTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CreateCalculatedAttributeDefinitionResponseTypeDef = TypedDict(
    "CreateCalculatedAttributeDefinitionResponseTypeDef",
    {
        "CalculatedAttributeName": str,
        "DisplayName": str,
        "Description": str,
        "AttributeDetails": AttributeDetailsOutputTypeDef,
        "Conditions": ConditionsTypeDef,
        "Statistic": StatisticType,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCalculatedAttributeDefinitionResponseTypeDef = TypedDict(
    "GetCalculatedAttributeDefinitionResponseTypeDef",
    {
        "CalculatedAttributeName": str,
        "DisplayName": str,
        "Description": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Statistic": StatisticType,
        "Conditions": ConditionsTypeDef,
        "AttributeDetails": AttributeDetailsOutputTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateCalculatedAttributeDefinitionRequestRequestTypeDef = TypedDict(
    "UpdateCalculatedAttributeDefinitionRequestRequestTypeDef",
    {
        "DomainName": str,
        "CalculatedAttributeName": str,
        "DisplayName": NotRequired[str],
        "Description": NotRequired[str],
        "Conditions": NotRequired[ConditionsTypeDef],
    },
)
UpdateCalculatedAttributeDefinitionResponseTypeDef = TypedDict(
    "UpdateCalculatedAttributeDefinitionResponseTypeDef",
    {
        "CalculatedAttributeName": str,
        "DisplayName": str,
        "Description": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Statistic": StatisticType,
        "Conditions": ConditionsTypeDef,
        "AttributeDetails": AttributeDetailsOutputTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AutoMergingTypeDef = TypedDict(
    "AutoMergingTypeDef",
    {
        "Enabled": bool,
        "Consolidation": NotRequired[ConsolidationUnionTypeDef],
        "ConflictResolution": NotRequired[ConflictResolutionTypeDef],
        "MinAllowedConfidenceScoreForMerging": NotRequired[float],
    },
)
ListEventStreamsResponseTypeDef = TypedDict(
    "ListEventStreamsResponseTypeDef",
    {
        "Items": List[EventStreamSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DetectProfileObjectTypeResponseTypeDef = TypedDict(
    "DetectProfileObjectTypeResponseTypeDef",
    {
        "DetectedProfileObjectTypes": List[DetectedProfileObjectTypeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MatchingResponseTypeDef = TypedDict(
    "MatchingResponseTypeDef",
    {
        "Enabled": NotRequired[bool],
        "JobSchedule": NotRequired[JobScheduleTypeDef],
        "AutoMerging": NotRequired[AutoMergingOutputTypeDef],
        "ExportingConfig": NotRequired[ExportingConfigTypeDef],
    },
)
RuleBasedMatchingResponseTypeDef = TypedDict(
    "RuleBasedMatchingResponseTypeDef",
    {
        "Enabled": NotRequired[bool],
        "MatchingRules": NotRequired[List[MatchingRuleOutputTypeDef]],
        "Status": NotRequired[RuleBasedMatchingStatusType],
        "MaxAllowedRuleLevelForMerging": NotRequired[int],
        "MaxAllowedRuleLevelForMatching": NotRequired[int],
        "AttributeTypesSelector": NotRequired[AttributeTypesSelectorOutputTypeDef],
        "ConflictResolution": NotRequired[ConflictResolutionTypeDef],
        "ExportingConfig": NotRequired[ExportingConfigTypeDef],
    },
)
GetIdentityResolutionJobResponseTypeDef = TypedDict(
    "GetIdentityResolutionJobResponseTypeDef",
    {
        "DomainName": str,
        "JobId": str,
        "Status": IdentityResolutionJobStatusType,
        "Message": str,
        "JobStartTime": datetime,
        "JobEndTime": datetime,
        "LastUpdatedAt": datetime,
        "JobExpirationTime": datetime,
        "AutoMerging": AutoMergingOutputTypeDef,
        "ExportingLocation": ExportingLocationTypeDef,
        "JobStats": JobStatsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IdentityResolutionJobTypeDef = TypedDict(
    "IdentityResolutionJobTypeDef",
    {
        "DomainName": NotRequired[str],
        "JobId": NotRequired[str],
        "Status": NotRequired[IdentityResolutionJobStatusType],
        "JobStartTime": NotRequired[datetime],
        "JobEndTime": NotRequired[datetime],
        "JobStats": NotRequired[JobStatsTypeDef],
        "ExportingLocation": NotRequired[ExportingLocationTypeDef],
        "Message": NotRequired[str],
    },
)
SearchProfilesResponseTypeDef = TypedDict(
    "SearchProfilesResponseTypeDef",
    {
        "Items": List[ProfileTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
RuleBasedMatchingRequestTypeDef = TypedDict(
    "RuleBasedMatchingRequestTypeDef",
    {
        "Enabled": bool,
        "MatchingRules": NotRequired[Sequence[MatchingRuleUnionTypeDef]],
        "MaxAllowedRuleLevelForMerging": NotRequired[int],
        "MaxAllowedRuleLevelForMatching": NotRequired[int],
        "AttributeTypesSelector": NotRequired[AttributeTypesSelectorUnionTypeDef],
        "ConflictResolution": NotRequired[ConflictResolutionTypeDef],
        "ExportingConfig": NotRequired[ExportingConfigTypeDef],
    },
)
PutProfileObjectTypeRequestRequestTypeDef = TypedDict(
    "PutProfileObjectTypeRequestRequestTypeDef",
    {
        "DomainName": str,
        "ObjectTypeName": str,
        "Description": str,
        "TemplateId": NotRequired[str],
        "ExpirationDays": NotRequired[int],
        "EncryptionKey": NotRequired[str],
        "AllowProfileCreation": NotRequired[bool],
        "SourceLastUpdatedTimestampFormat": NotRequired[str],
        "MaxProfileObjectCount": NotRequired[int],
        "Fields": NotRequired[Mapping[str, ObjectTypeFieldTypeDef]],
        "Keys": NotRequired[Mapping[str, Sequence[ObjectTypeKeyUnionTypeDef]]],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
SourceFlowConfigTypeDef = TypedDict(
    "SourceFlowConfigTypeDef",
    {
        "ConnectorType": SourceConnectorTypeType,
        "SourceConnectorProperties": SourceConnectorPropertiesTypeDef,
        "ConnectorProfileName": NotRequired[str],
        "IncrementalPullConfig": NotRequired[IncrementalPullConfigTypeDef],
    },
)
TriggerConfigTypeDef = TypedDict(
    "TriggerConfigTypeDef",
    {
        "TriggerType": TriggerTypeType,
        "TriggerProperties": NotRequired[TriggerPropertiesTypeDef],
    },
)
AutoMergingUnionTypeDef = Union[AutoMergingTypeDef, AutoMergingOutputTypeDef]
CreateDomainResponseTypeDef = TypedDict(
    "CreateDomainResponseTypeDef",
    {
        "DomainName": str,
        "DefaultExpirationDays": int,
        "DefaultEncryptionKey": str,
        "DeadLetterQueueUrl": str,
        "Matching": MatchingResponseTypeDef,
        "RuleBasedMatching": RuleBasedMatchingResponseTypeDef,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDomainResponseTypeDef = TypedDict(
    "GetDomainResponseTypeDef",
    {
        "DomainName": str,
        "DefaultExpirationDays": int,
        "DefaultEncryptionKey": str,
        "DeadLetterQueueUrl": str,
        "Stats": DomainStatsTypeDef,
        "Matching": MatchingResponseTypeDef,
        "RuleBasedMatching": RuleBasedMatchingResponseTypeDef,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDomainResponseTypeDef = TypedDict(
    "UpdateDomainResponseTypeDef",
    {
        "DomainName": str,
        "DefaultExpirationDays": int,
        "DefaultEncryptionKey": str,
        "DeadLetterQueueUrl": str,
        "Matching": MatchingResponseTypeDef,
        "RuleBasedMatching": RuleBasedMatchingResponseTypeDef,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListIdentityResolutionJobsResponseTypeDef = TypedDict(
    "ListIdentityResolutionJobsResponseTypeDef",
    {
        "IdentityResolutionJobsList": List[IdentityResolutionJobTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
FlowDefinitionTypeDef = TypedDict(
    "FlowDefinitionTypeDef",
    {
        "FlowName": str,
        "KmsArn": str,
        "SourceFlowConfig": SourceFlowConfigTypeDef,
        "Tasks": Sequence[TaskTypeDef],
        "TriggerConfig": TriggerConfigTypeDef,
        "Description": NotRequired[str],
    },
)
MatchingRequestTypeDef = TypedDict(
    "MatchingRequestTypeDef",
    {
        "Enabled": bool,
        "JobSchedule": NotRequired[JobScheduleTypeDef],
        "AutoMerging": NotRequired[AutoMergingUnionTypeDef],
        "ExportingConfig": NotRequired[ExportingConfigTypeDef],
    },
)
AppflowIntegrationTypeDef = TypedDict(
    "AppflowIntegrationTypeDef",
    {
        "FlowDefinition": FlowDefinitionTypeDef,
        "Batches": NotRequired[Sequence[BatchTypeDef]],
    },
)
PutIntegrationRequestRequestTypeDef = TypedDict(
    "PutIntegrationRequestRequestTypeDef",
    {
        "DomainName": str,
        "Uri": NotRequired[str],
        "ObjectTypeName": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "FlowDefinition": NotRequired[FlowDefinitionTypeDef],
        "ObjectTypeNames": NotRequired[Mapping[str, str]],
        "RoleArn": NotRequired[str],
    },
)
CreateDomainRequestRequestTypeDef = TypedDict(
    "CreateDomainRequestRequestTypeDef",
    {
        "DomainName": str,
        "DefaultExpirationDays": int,
        "DefaultEncryptionKey": NotRequired[str],
        "DeadLetterQueueUrl": NotRequired[str],
        "Matching": NotRequired[MatchingRequestTypeDef],
        "RuleBasedMatching": NotRequired[RuleBasedMatchingRequestTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
UpdateDomainRequestRequestTypeDef = TypedDict(
    "UpdateDomainRequestRequestTypeDef",
    {
        "DomainName": str,
        "DefaultExpirationDays": NotRequired[int],
        "DefaultEncryptionKey": NotRequired[str],
        "DeadLetterQueueUrl": NotRequired[str],
        "Matching": NotRequired[MatchingRequestTypeDef],
        "RuleBasedMatching": NotRequired[RuleBasedMatchingRequestTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
IntegrationConfigTypeDef = TypedDict(
    "IntegrationConfigTypeDef",
    {
        "AppflowIntegration": NotRequired[AppflowIntegrationTypeDef],
    },
)
CreateIntegrationWorkflowRequestRequestTypeDef = TypedDict(
    "CreateIntegrationWorkflowRequestRequestTypeDef",
    {
        "DomainName": str,
        "WorkflowType": Literal["APPFLOW_INTEGRATION"],
        "IntegrationConfig": IntegrationConfigTypeDef,
        "ObjectTypeName": str,
        "RoleArn": str,
        "Tags": NotRequired[Mapping[str, str]],
    },
)
