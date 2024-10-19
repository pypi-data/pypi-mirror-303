"""
Type annotations for comprehendmedical service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_comprehendmedical/type_defs/)

Usage::

    ```python
    from mypy_boto3_comprehendmedical.type_defs import TraitTypeDef

    data: TraitTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Union

from .literals import (
    AttributeNameType,
    EntitySubTypeType,
    EntityTypeType,
    ICD10CMAttributeTypeType,
    ICD10CMEntityTypeType,
    ICD10CMRelationshipTypeType,
    ICD10CMTraitNameType,
    JobStatusType,
    RelationshipTypeType,
    RxNormAttributeTypeType,
    RxNormEntityTypeType,
    RxNormTraitNameType,
    SNOMEDCTAttributeTypeType,
    SNOMEDCTEntityCategoryType,
    SNOMEDCTEntityTypeType,
    SNOMEDCTRelationshipTypeType,
    SNOMEDCTTraitNameType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "TraitTypeDef",
    "CharactersTypeDef",
    "TimestampTypeDef",
    "InputDataConfigTypeDef",
    "OutputDataConfigTypeDef",
    "DescribeEntitiesDetectionV2JobRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "DescribeICD10CMInferenceJobRequestRequestTypeDef",
    "DescribePHIDetectionJobRequestRequestTypeDef",
    "DescribeRxNormInferenceJobRequestRequestTypeDef",
    "DescribeSNOMEDCTInferenceJobRequestRequestTypeDef",
    "DetectEntitiesRequestRequestTypeDef",
    "DetectEntitiesV2RequestRequestTypeDef",
    "DetectPHIRequestRequestTypeDef",
    "ICD10CMTraitTypeDef",
    "ICD10CMConceptTypeDef",
    "InferICD10CMRequestRequestTypeDef",
    "InferRxNormRequestRequestTypeDef",
    "InferSNOMEDCTRequestRequestTypeDef",
    "SNOMEDCTDetailsTypeDef",
    "RxNormTraitTypeDef",
    "RxNormConceptTypeDef",
    "SNOMEDCTConceptTypeDef",
    "SNOMEDCTTraitTypeDef",
    "StopEntitiesDetectionV2JobRequestRequestTypeDef",
    "StopICD10CMInferenceJobRequestRequestTypeDef",
    "StopPHIDetectionJobRequestRequestTypeDef",
    "StopRxNormInferenceJobRequestRequestTypeDef",
    "StopSNOMEDCTInferenceJobRequestRequestTypeDef",
    "AttributeTypeDef",
    "ComprehendMedicalAsyncJobFilterTypeDef",
    "ComprehendMedicalAsyncJobPropertiesTypeDef",
    "StartEntitiesDetectionV2JobRequestRequestTypeDef",
    "StartICD10CMInferenceJobRequestRequestTypeDef",
    "StartPHIDetectionJobRequestRequestTypeDef",
    "StartRxNormInferenceJobRequestRequestTypeDef",
    "StartSNOMEDCTInferenceJobRequestRequestTypeDef",
    "StartEntitiesDetectionV2JobResponseTypeDef",
    "StartICD10CMInferenceJobResponseTypeDef",
    "StartPHIDetectionJobResponseTypeDef",
    "StartRxNormInferenceJobResponseTypeDef",
    "StartSNOMEDCTInferenceJobResponseTypeDef",
    "StopEntitiesDetectionV2JobResponseTypeDef",
    "StopICD10CMInferenceJobResponseTypeDef",
    "StopPHIDetectionJobResponseTypeDef",
    "StopRxNormInferenceJobResponseTypeDef",
    "StopSNOMEDCTInferenceJobResponseTypeDef",
    "ICD10CMAttributeTypeDef",
    "RxNormAttributeTypeDef",
    "SNOMEDCTAttributeTypeDef",
    "EntityTypeDef",
    "UnmappedAttributeTypeDef",
    "ListEntitiesDetectionV2JobsRequestRequestTypeDef",
    "ListICD10CMInferenceJobsRequestRequestTypeDef",
    "ListPHIDetectionJobsRequestRequestTypeDef",
    "ListRxNormInferenceJobsRequestRequestTypeDef",
    "ListSNOMEDCTInferenceJobsRequestRequestTypeDef",
    "DescribeEntitiesDetectionV2JobResponseTypeDef",
    "DescribeICD10CMInferenceJobResponseTypeDef",
    "DescribePHIDetectionJobResponseTypeDef",
    "DescribeRxNormInferenceJobResponseTypeDef",
    "DescribeSNOMEDCTInferenceJobResponseTypeDef",
    "ListEntitiesDetectionV2JobsResponseTypeDef",
    "ListICD10CMInferenceJobsResponseTypeDef",
    "ListPHIDetectionJobsResponseTypeDef",
    "ListRxNormInferenceJobsResponseTypeDef",
    "ListSNOMEDCTInferenceJobsResponseTypeDef",
    "ICD10CMEntityTypeDef",
    "RxNormEntityTypeDef",
    "SNOMEDCTEntityTypeDef",
    "DetectPHIResponseTypeDef",
    "DetectEntitiesResponseTypeDef",
    "DetectEntitiesV2ResponseTypeDef",
    "InferICD10CMResponseTypeDef",
    "InferRxNormResponseTypeDef",
    "InferSNOMEDCTResponseTypeDef",
)

TraitTypeDef = TypedDict(
    "TraitTypeDef",
    {
        "Name": NotRequired[AttributeNameType],
        "Score": NotRequired[float],
    },
)
CharactersTypeDef = TypedDict(
    "CharactersTypeDef",
    {
        "OriginalTextCharacters": NotRequired[int],
    },
)
TimestampTypeDef = Union[datetime, str]
InputDataConfigTypeDef = TypedDict(
    "InputDataConfigTypeDef",
    {
        "S3Bucket": str,
        "S3Key": NotRequired[str],
    },
)
OutputDataConfigTypeDef = TypedDict(
    "OutputDataConfigTypeDef",
    {
        "S3Bucket": str,
        "S3Key": NotRequired[str],
    },
)
DescribeEntitiesDetectionV2JobRequestRequestTypeDef = TypedDict(
    "DescribeEntitiesDetectionV2JobRequestRequestTypeDef",
    {
        "JobId": str,
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
DescribeICD10CMInferenceJobRequestRequestTypeDef = TypedDict(
    "DescribeICD10CMInferenceJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
DescribePHIDetectionJobRequestRequestTypeDef = TypedDict(
    "DescribePHIDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
DescribeRxNormInferenceJobRequestRequestTypeDef = TypedDict(
    "DescribeRxNormInferenceJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
DescribeSNOMEDCTInferenceJobRequestRequestTypeDef = TypedDict(
    "DescribeSNOMEDCTInferenceJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
DetectEntitiesRequestRequestTypeDef = TypedDict(
    "DetectEntitiesRequestRequestTypeDef",
    {
        "Text": str,
    },
)
DetectEntitiesV2RequestRequestTypeDef = TypedDict(
    "DetectEntitiesV2RequestRequestTypeDef",
    {
        "Text": str,
    },
)
DetectPHIRequestRequestTypeDef = TypedDict(
    "DetectPHIRequestRequestTypeDef",
    {
        "Text": str,
    },
)
ICD10CMTraitTypeDef = TypedDict(
    "ICD10CMTraitTypeDef",
    {
        "Name": NotRequired[ICD10CMTraitNameType],
        "Score": NotRequired[float],
    },
)
ICD10CMConceptTypeDef = TypedDict(
    "ICD10CMConceptTypeDef",
    {
        "Description": NotRequired[str],
        "Code": NotRequired[str],
        "Score": NotRequired[float],
    },
)
InferICD10CMRequestRequestTypeDef = TypedDict(
    "InferICD10CMRequestRequestTypeDef",
    {
        "Text": str,
    },
)
InferRxNormRequestRequestTypeDef = TypedDict(
    "InferRxNormRequestRequestTypeDef",
    {
        "Text": str,
    },
)
InferSNOMEDCTRequestRequestTypeDef = TypedDict(
    "InferSNOMEDCTRequestRequestTypeDef",
    {
        "Text": str,
    },
)
SNOMEDCTDetailsTypeDef = TypedDict(
    "SNOMEDCTDetailsTypeDef",
    {
        "Edition": NotRequired[str],
        "Language": NotRequired[str],
        "VersionDate": NotRequired[str],
    },
)
RxNormTraitTypeDef = TypedDict(
    "RxNormTraitTypeDef",
    {
        "Name": NotRequired[RxNormTraitNameType],
        "Score": NotRequired[float],
    },
)
RxNormConceptTypeDef = TypedDict(
    "RxNormConceptTypeDef",
    {
        "Description": NotRequired[str],
        "Code": NotRequired[str],
        "Score": NotRequired[float],
    },
)
SNOMEDCTConceptTypeDef = TypedDict(
    "SNOMEDCTConceptTypeDef",
    {
        "Description": NotRequired[str],
        "Code": NotRequired[str],
        "Score": NotRequired[float],
    },
)
SNOMEDCTTraitTypeDef = TypedDict(
    "SNOMEDCTTraitTypeDef",
    {
        "Name": NotRequired[SNOMEDCTTraitNameType],
        "Score": NotRequired[float],
    },
)
StopEntitiesDetectionV2JobRequestRequestTypeDef = TypedDict(
    "StopEntitiesDetectionV2JobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
StopICD10CMInferenceJobRequestRequestTypeDef = TypedDict(
    "StopICD10CMInferenceJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
StopPHIDetectionJobRequestRequestTypeDef = TypedDict(
    "StopPHIDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
StopRxNormInferenceJobRequestRequestTypeDef = TypedDict(
    "StopRxNormInferenceJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
StopSNOMEDCTInferenceJobRequestRequestTypeDef = TypedDict(
    "StopSNOMEDCTInferenceJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "Type": NotRequired[EntitySubTypeType],
        "Score": NotRequired[float],
        "RelationshipScore": NotRequired[float],
        "RelationshipType": NotRequired[RelationshipTypeType],
        "Id": NotRequired[int],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
        "Text": NotRequired[str],
        "Category": NotRequired[EntityTypeType],
        "Traits": NotRequired[List[TraitTypeDef]],
    },
)
ComprehendMedicalAsyncJobFilterTypeDef = TypedDict(
    "ComprehendMedicalAsyncJobFilterTypeDef",
    {
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "SubmitTimeBefore": NotRequired[TimestampTypeDef],
        "SubmitTimeAfter": NotRequired[TimestampTypeDef],
    },
)
ComprehendMedicalAsyncJobPropertiesTypeDef = TypedDict(
    "ComprehendMedicalAsyncJobPropertiesTypeDef",
    {
        "JobId": NotRequired[str],
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "Message": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "ExpirationTime": NotRequired[datetime],
        "InputDataConfig": NotRequired[InputDataConfigTypeDef],
        "OutputDataConfig": NotRequired[OutputDataConfigTypeDef],
        "LanguageCode": NotRequired[Literal["en"]],
        "DataAccessRoleArn": NotRequired[str],
        "ManifestFilePath": NotRequired[str],
        "KMSKey": NotRequired[str],
        "ModelVersion": NotRequired[str],
    },
)
StartEntitiesDetectionV2JobRequestRequestTypeDef = TypedDict(
    "StartEntitiesDetectionV2JobRequestRequestTypeDef",
    {
        "InputDataConfig": InputDataConfigTypeDef,
        "OutputDataConfig": OutputDataConfigTypeDef,
        "DataAccessRoleArn": str,
        "LanguageCode": Literal["en"],
        "JobName": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "KMSKey": NotRequired[str],
    },
)
StartICD10CMInferenceJobRequestRequestTypeDef = TypedDict(
    "StartICD10CMInferenceJobRequestRequestTypeDef",
    {
        "InputDataConfig": InputDataConfigTypeDef,
        "OutputDataConfig": OutputDataConfigTypeDef,
        "DataAccessRoleArn": str,
        "LanguageCode": Literal["en"],
        "JobName": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "KMSKey": NotRequired[str],
    },
)
StartPHIDetectionJobRequestRequestTypeDef = TypedDict(
    "StartPHIDetectionJobRequestRequestTypeDef",
    {
        "InputDataConfig": InputDataConfigTypeDef,
        "OutputDataConfig": OutputDataConfigTypeDef,
        "DataAccessRoleArn": str,
        "LanguageCode": Literal["en"],
        "JobName": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "KMSKey": NotRequired[str],
    },
)
StartRxNormInferenceJobRequestRequestTypeDef = TypedDict(
    "StartRxNormInferenceJobRequestRequestTypeDef",
    {
        "InputDataConfig": InputDataConfigTypeDef,
        "OutputDataConfig": OutputDataConfigTypeDef,
        "DataAccessRoleArn": str,
        "LanguageCode": Literal["en"],
        "JobName": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "KMSKey": NotRequired[str],
    },
)
StartSNOMEDCTInferenceJobRequestRequestTypeDef = TypedDict(
    "StartSNOMEDCTInferenceJobRequestRequestTypeDef",
    {
        "InputDataConfig": InputDataConfigTypeDef,
        "OutputDataConfig": OutputDataConfigTypeDef,
        "DataAccessRoleArn": str,
        "LanguageCode": Literal["en"],
        "JobName": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "KMSKey": NotRequired[str],
    },
)
StartEntitiesDetectionV2JobResponseTypeDef = TypedDict(
    "StartEntitiesDetectionV2JobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartICD10CMInferenceJobResponseTypeDef = TypedDict(
    "StartICD10CMInferenceJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartPHIDetectionJobResponseTypeDef = TypedDict(
    "StartPHIDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartRxNormInferenceJobResponseTypeDef = TypedDict(
    "StartRxNormInferenceJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartSNOMEDCTInferenceJobResponseTypeDef = TypedDict(
    "StartSNOMEDCTInferenceJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopEntitiesDetectionV2JobResponseTypeDef = TypedDict(
    "StopEntitiesDetectionV2JobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopICD10CMInferenceJobResponseTypeDef = TypedDict(
    "StopICD10CMInferenceJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopPHIDetectionJobResponseTypeDef = TypedDict(
    "StopPHIDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopRxNormInferenceJobResponseTypeDef = TypedDict(
    "StopRxNormInferenceJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopSNOMEDCTInferenceJobResponseTypeDef = TypedDict(
    "StopSNOMEDCTInferenceJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ICD10CMAttributeTypeDef = TypedDict(
    "ICD10CMAttributeTypeDef",
    {
        "Type": NotRequired[ICD10CMAttributeTypeType],
        "Score": NotRequired[float],
        "RelationshipScore": NotRequired[float],
        "Id": NotRequired[int],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
        "Text": NotRequired[str],
        "Traits": NotRequired[List[ICD10CMTraitTypeDef]],
        "Category": NotRequired[ICD10CMEntityTypeType],
        "RelationshipType": NotRequired[ICD10CMRelationshipTypeType],
    },
)
RxNormAttributeTypeDef = TypedDict(
    "RxNormAttributeTypeDef",
    {
        "Type": NotRequired[RxNormAttributeTypeType],
        "Score": NotRequired[float],
        "RelationshipScore": NotRequired[float],
        "Id": NotRequired[int],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
        "Text": NotRequired[str],
        "Traits": NotRequired[List[RxNormTraitTypeDef]],
    },
)
SNOMEDCTAttributeTypeDef = TypedDict(
    "SNOMEDCTAttributeTypeDef",
    {
        "Category": NotRequired[SNOMEDCTEntityCategoryType],
        "Type": NotRequired[SNOMEDCTAttributeTypeType],
        "Score": NotRequired[float],
        "RelationshipScore": NotRequired[float],
        "RelationshipType": NotRequired[SNOMEDCTRelationshipTypeType],
        "Id": NotRequired[int],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
        "Text": NotRequired[str],
        "Traits": NotRequired[List[SNOMEDCTTraitTypeDef]],
        "SNOMEDCTConcepts": NotRequired[List[SNOMEDCTConceptTypeDef]],
    },
)
EntityTypeDef = TypedDict(
    "EntityTypeDef",
    {
        "Id": NotRequired[int],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
        "Score": NotRequired[float],
        "Text": NotRequired[str],
        "Category": NotRequired[EntityTypeType],
        "Type": NotRequired[EntitySubTypeType],
        "Traits": NotRequired[List[TraitTypeDef]],
        "Attributes": NotRequired[List[AttributeTypeDef]],
    },
)
UnmappedAttributeTypeDef = TypedDict(
    "UnmappedAttributeTypeDef",
    {
        "Type": NotRequired[EntityTypeType],
        "Attribute": NotRequired[AttributeTypeDef],
    },
)
ListEntitiesDetectionV2JobsRequestRequestTypeDef = TypedDict(
    "ListEntitiesDetectionV2JobsRequestRequestTypeDef",
    {
        "Filter": NotRequired[ComprehendMedicalAsyncJobFilterTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListICD10CMInferenceJobsRequestRequestTypeDef = TypedDict(
    "ListICD10CMInferenceJobsRequestRequestTypeDef",
    {
        "Filter": NotRequired[ComprehendMedicalAsyncJobFilterTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListPHIDetectionJobsRequestRequestTypeDef = TypedDict(
    "ListPHIDetectionJobsRequestRequestTypeDef",
    {
        "Filter": NotRequired[ComprehendMedicalAsyncJobFilterTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListRxNormInferenceJobsRequestRequestTypeDef = TypedDict(
    "ListRxNormInferenceJobsRequestRequestTypeDef",
    {
        "Filter": NotRequired[ComprehendMedicalAsyncJobFilterTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListSNOMEDCTInferenceJobsRequestRequestTypeDef = TypedDict(
    "ListSNOMEDCTInferenceJobsRequestRequestTypeDef",
    {
        "Filter": NotRequired[ComprehendMedicalAsyncJobFilterTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeEntitiesDetectionV2JobResponseTypeDef = TypedDict(
    "DescribeEntitiesDetectionV2JobResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobProperties": ComprehendMedicalAsyncJobPropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeICD10CMInferenceJobResponseTypeDef = TypedDict(
    "DescribeICD10CMInferenceJobResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobProperties": ComprehendMedicalAsyncJobPropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePHIDetectionJobResponseTypeDef = TypedDict(
    "DescribePHIDetectionJobResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobProperties": ComprehendMedicalAsyncJobPropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRxNormInferenceJobResponseTypeDef = TypedDict(
    "DescribeRxNormInferenceJobResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobProperties": ComprehendMedicalAsyncJobPropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSNOMEDCTInferenceJobResponseTypeDef = TypedDict(
    "DescribeSNOMEDCTInferenceJobResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobProperties": ComprehendMedicalAsyncJobPropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEntitiesDetectionV2JobsResponseTypeDef = TypedDict(
    "ListEntitiesDetectionV2JobsResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobPropertiesList": List[ComprehendMedicalAsyncJobPropertiesTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListICD10CMInferenceJobsResponseTypeDef = TypedDict(
    "ListICD10CMInferenceJobsResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobPropertiesList": List[ComprehendMedicalAsyncJobPropertiesTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListPHIDetectionJobsResponseTypeDef = TypedDict(
    "ListPHIDetectionJobsResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobPropertiesList": List[ComprehendMedicalAsyncJobPropertiesTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListRxNormInferenceJobsResponseTypeDef = TypedDict(
    "ListRxNormInferenceJobsResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobPropertiesList": List[ComprehendMedicalAsyncJobPropertiesTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListSNOMEDCTInferenceJobsResponseTypeDef = TypedDict(
    "ListSNOMEDCTInferenceJobsResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobPropertiesList": List[ComprehendMedicalAsyncJobPropertiesTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ICD10CMEntityTypeDef = TypedDict(
    "ICD10CMEntityTypeDef",
    {
        "Id": NotRequired[int],
        "Text": NotRequired[str],
        "Category": NotRequired[Literal["MEDICAL_CONDITION"]],
        "Type": NotRequired[ICD10CMEntityTypeType],
        "Score": NotRequired[float],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
        "Attributes": NotRequired[List[ICD10CMAttributeTypeDef]],
        "Traits": NotRequired[List[ICD10CMTraitTypeDef]],
        "ICD10CMConcepts": NotRequired[List[ICD10CMConceptTypeDef]],
    },
)
RxNormEntityTypeDef = TypedDict(
    "RxNormEntityTypeDef",
    {
        "Id": NotRequired[int],
        "Text": NotRequired[str],
        "Category": NotRequired[Literal["MEDICATION"]],
        "Type": NotRequired[RxNormEntityTypeType],
        "Score": NotRequired[float],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
        "Attributes": NotRequired[List[RxNormAttributeTypeDef]],
        "Traits": NotRequired[List[RxNormTraitTypeDef]],
        "RxNormConcepts": NotRequired[List[RxNormConceptTypeDef]],
    },
)
SNOMEDCTEntityTypeDef = TypedDict(
    "SNOMEDCTEntityTypeDef",
    {
        "Id": NotRequired[int],
        "Text": NotRequired[str],
        "Category": NotRequired[SNOMEDCTEntityCategoryType],
        "Type": NotRequired[SNOMEDCTEntityTypeType],
        "Score": NotRequired[float],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
        "Attributes": NotRequired[List[SNOMEDCTAttributeTypeDef]],
        "Traits": NotRequired[List[SNOMEDCTTraitTypeDef]],
        "SNOMEDCTConcepts": NotRequired[List[SNOMEDCTConceptTypeDef]],
    },
)
DetectPHIResponseTypeDef = TypedDict(
    "DetectPHIResponseTypeDef",
    {
        "Entities": List[EntityTypeDef],
        "PaginationToken": str,
        "ModelVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DetectEntitiesResponseTypeDef = TypedDict(
    "DetectEntitiesResponseTypeDef",
    {
        "Entities": List[EntityTypeDef],
        "UnmappedAttributes": List[UnmappedAttributeTypeDef],
        "PaginationToken": str,
        "ModelVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DetectEntitiesV2ResponseTypeDef = TypedDict(
    "DetectEntitiesV2ResponseTypeDef",
    {
        "Entities": List[EntityTypeDef],
        "UnmappedAttributes": List[UnmappedAttributeTypeDef],
        "PaginationToken": str,
        "ModelVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InferICD10CMResponseTypeDef = TypedDict(
    "InferICD10CMResponseTypeDef",
    {
        "Entities": List[ICD10CMEntityTypeDef],
        "PaginationToken": str,
        "ModelVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InferRxNormResponseTypeDef = TypedDict(
    "InferRxNormResponseTypeDef",
    {
        "Entities": List[RxNormEntityTypeDef],
        "PaginationToken": str,
        "ModelVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InferSNOMEDCTResponseTypeDef = TypedDict(
    "InferSNOMEDCTResponseTypeDef",
    {
        "Entities": List[SNOMEDCTEntityTypeDef],
        "PaginationToken": str,
        "ModelVersion": str,
        "SNOMEDCTDetails": SNOMEDCTDetailsTypeDef,
        "Characters": CharactersTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
