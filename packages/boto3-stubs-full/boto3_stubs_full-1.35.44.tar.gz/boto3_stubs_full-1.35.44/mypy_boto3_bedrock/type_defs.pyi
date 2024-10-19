"""
Type annotations for bedrock service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/type_defs/)

Usage::

    ```python
    from mypy_boto3_bedrock.type_defs import BatchDeleteEvaluationJobErrorTypeDef

    data: BatchDeleteEvaluationJobErrorTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    CommitmentDurationType,
    CustomizationTypeType,
    EvaluationJobStatusType,
    EvaluationJobTypeType,
    EvaluationTaskTypeType,
    FineTuningJobStatusType,
    FoundationModelLifecycleStatusType,
    GuardrailContentFilterTypeType,
    GuardrailContextualGroundingFilterTypeType,
    GuardrailFilterStrengthType,
    GuardrailPiiEntityTypeType,
    GuardrailSensitiveInformationActionType,
    GuardrailStatusType,
    InferenceTypeType,
    ModelCopyJobStatusType,
    ModelCustomizationJobStatusType,
    ModelCustomizationType,
    ModelImportJobStatusType,
    ModelInvocationJobStatusType,
    ModelModalityType,
    ProvisionedModelStatusType,
    SortOrderType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "BatchDeleteEvaluationJobErrorTypeDef",
    "BatchDeleteEvaluationJobItemTypeDef",
    "BatchDeleteEvaluationJobRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "S3ConfigTypeDef",
    "EvaluationOutputDataConfigTypeDef",
    "TagTypeDef",
    "CreateGuardrailVersionRequestRequestTypeDef",
    "OutputDataConfigTypeDef",
    "TrainingDataConfigTypeDef",
    "VpcConfigTypeDef",
    "CustomModelSummaryTypeDef",
    "DeleteCustomModelRequestRequestTypeDef",
    "DeleteGuardrailRequestRequestTypeDef",
    "DeleteImportedModelRequestRequestTypeDef",
    "DeleteProvisionedModelThroughputRequestRequestTypeDef",
    "EvaluationBedrockModelTypeDef",
    "EvaluationDatasetLocationTypeDef",
    "EvaluationSummaryTypeDef",
    "FoundationModelLifecycleTypeDef",
    "GetCustomModelRequestRequestTypeDef",
    "TrainingMetricsTypeDef",
    "ValidatorMetricTypeDef",
    "GetEvaluationJobRequestRequestTypeDef",
    "GetFoundationModelRequestRequestTypeDef",
    "GetGuardrailRequestRequestTypeDef",
    "GetImportedModelRequestRequestTypeDef",
    "GetInferenceProfileRequestRequestTypeDef",
    "InferenceProfileModelTypeDef",
    "GetModelCopyJobRequestRequestTypeDef",
    "GetModelCustomizationJobRequestRequestTypeDef",
    "VpcConfigOutputTypeDef",
    "GetModelImportJobRequestRequestTypeDef",
    "GetModelInvocationJobRequestRequestTypeDef",
    "GetProvisionedModelThroughputRequestRequestTypeDef",
    "GuardrailContentFilterConfigTypeDef",
    "GuardrailContentFilterTypeDef",
    "GuardrailContextualGroundingFilterConfigTypeDef",
    "GuardrailContextualGroundingFilterTypeDef",
    "GuardrailManagedWordsConfigTypeDef",
    "GuardrailManagedWordsTypeDef",
    "GuardrailPiiEntityConfigTypeDef",
    "GuardrailPiiEntityTypeDef",
    "GuardrailRegexConfigTypeDef",
    "GuardrailRegexTypeDef",
    "GuardrailSummaryTypeDef",
    "GuardrailTopicConfigTypeDef",
    "GuardrailTopicTypeDef",
    "GuardrailWordConfigTypeDef",
    "GuardrailWordTypeDef",
    "HumanEvaluationCustomMetricTypeDef",
    "HumanWorkflowConfigTypeDef",
    "ImportedModelSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "TimestampTypeDef",
    "ListFoundationModelsRequestRequestTypeDef",
    "ListGuardrailsRequestRequestTypeDef",
    "ListInferenceProfilesRequestRequestTypeDef",
    "ModelCustomizationJobSummaryTypeDef",
    "ModelImportJobSummaryTypeDef",
    "ProvisionedModelSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "S3DataSourceTypeDef",
    "ModelInvocationJobS3InputDataConfigTypeDef",
    "ModelInvocationJobS3OutputDataConfigTypeDef",
    "StopEvaluationJobRequestRequestTypeDef",
    "StopModelCustomizationJobRequestRequestTypeDef",
    "StopModelInvocationJobRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateProvisionedModelThroughputRequestRequestTypeDef",
    "ValidatorTypeDef",
    "BatchDeleteEvaluationJobResponseTypeDef",
    "CreateEvaluationJobResponseTypeDef",
    "CreateGuardrailResponseTypeDef",
    "CreateGuardrailVersionResponseTypeDef",
    "CreateModelCopyJobResponseTypeDef",
    "CreateModelCustomizationJobResponseTypeDef",
    "CreateModelImportJobResponseTypeDef",
    "CreateModelInvocationJobResponseTypeDef",
    "CreateProvisionedModelThroughputResponseTypeDef",
    "GetProvisionedModelThroughputResponseTypeDef",
    "UpdateGuardrailResponseTypeDef",
    "CloudWatchConfigTypeDef",
    "CreateModelCopyJobRequestRequestTypeDef",
    "CreateProvisionedModelThroughputRequestRequestTypeDef",
    "GetModelCopyJobResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ModelCopyJobSummaryTypeDef",
    "TagResourceRequestRequestTypeDef",
    "ListCustomModelsResponseTypeDef",
    "EvaluationModelConfigTypeDef",
    "EvaluationDatasetTypeDef",
    "ListEvaluationJobsResponseTypeDef",
    "FoundationModelDetailsTypeDef",
    "FoundationModelSummaryTypeDef",
    "GetInferenceProfileResponseTypeDef",
    "InferenceProfileSummaryTypeDef",
    "GuardrailContentPolicyConfigTypeDef",
    "GuardrailContentPolicyTypeDef",
    "GuardrailContextualGroundingPolicyConfigTypeDef",
    "GuardrailContextualGroundingPolicyTypeDef",
    "GuardrailSensitiveInformationPolicyConfigTypeDef",
    "GuardrailSensitiveInformationPolicyTypeDef",
    "ListGuardrailsResponseTypeDef",
    "GuardrailTopicPolicyConfigTypeDef",
    "GuardrailTopicPolicyTypeDef",
    "GuardrailWordPolicyConfigTypeDef",
    "GuardrailWordPolicyTypeDef",
    "ListImportedModelsResponseTypeDef",
    "ListGuardrailsRequestListGuardrailsPaginateTypeDef",
    "ListInferenceProfilesRequestListInferenceProfilesPaginateTypeDef",
    "ListCustomModelsRequestListCustomModelsPaginateTypeDef",
    "ListCustomModelsRequestRequestTypeDef",
    "ListEvaluationJobsRequestListEvaluationJobsPaginateTypeDef",
    "ListEvaluationJobsRequestRequestTypeDef",
    "ListImportedModelsRequestListImportedModelsPaginateTypeDef",
    "ListImportedModelsRequestRequestTypeDef",
    "ListModelCopyJobsRequestListModelCopyJobsPaginateTypeDef",
    "ListModelCopyJobsRequestRequestTypeDef",
    "ListModelCustomizationJobsRequestListModelCustomizationJobsPaginateTypeDef",
    "ListModelCustomizationJobsRequestRequestTypeDef",
    "ListModelImportJobsRequestListModelImportJobsPaginateTypeDef",
    "ListModelImportJobsRequestRequestTypeDef",
    "ListModelInvocationJobsRequestListModelInvocationJobsPaginateTypeDef",
    "ListModelInvocationJobsRequestRequestTypeDef",
    "ListProvisionedModelThroughputsRequestListProvisionedModelThroughputsPaginateTypeDef",
    "ListProvisionedModelThroughputsRequestRequestTypeDef",
    "ListModelCustomizationJobsResponseTypeDef",
    "ListModelImportJobsResponseTypeDef",
    "ListProvisionedModelThroughputsResponseTypeDef",
    "ModelDataSourceTypeDef",
    "ModelInvocationJobInputDataConfigTypeDef",
    "ModelInvocationJobOutputDataConfigTypeDef",
    "ValidationDataConfigOutputTypeDef",
    "ValidationDataConfigTypeDef",
    "LoggingConfigTypeDef",
    "ListModelCopyJobsResponseTypeDef",
    "EvaluationInferenceConfigOutputTypeDef",
    "EvaluationInferenceConfigTypeDef",
    "EvaluationDatasetMetricConfigOutputTypeDef",
    "EvaluationDatasetMetricConfigTypeDef",
    "GetFoundationModelResponseTypeDef",
    "ListFoundationModelsResponseTypeDef",
    "ListInferenceProfilesResponseTypeDef",
    "CreateGuardrailRequestRequestTypeDef",
    "UpdateGuardrailRequestRequestTypeDef",
    "GetGuardrailResponseTypeDef",
    "CreateModelImportJobRequestRequestTypeDef",
    "GetImportedModelResponseTypeDef",
    "GetModelImportJobResponseTypeDef",
    "CreateModelInvocationJobRequestRequestTypeDef",
    "GetModelInvocationJobResponseTypeDef",
    "ModelInvocationJobSummaryTypeDef",
    "GetCustomModelResponseTypeDef",
    "GetModelCustomizationJobResponseTypeDef",
    "CreateModelCustomizationJobRequestRequestTypeDef",
    "GetModelInvocationLoggingConfigurationResponseTypeDef",
    "PutModelInvocationLoggingConfigurationRequestRequestTypeDef",
    "AutomatedEvaluationConfigOutputTypeDef",
    "HumanEvaluationConfigOutputTypeDef",
    "EvaluationDatasetMetricConfigUnionTypeDef",
    "HumanEvaluationConfigTypeDef",
    "ListModelInvocationJobsResponseTypeDef",
    "EvaluationConfigOutputTypeDef",
    "AutomatedEvaluationConfigTypeDef",
    "HumanEvaluationConfigUnionTypeDef",
    "GetEvaluationJobResponseTypeDef",
    "AutomatedEvaluationConfigUnionTypeDef",
    "EvaluationConfigTypeDef",
    "CreateEvaluationJobRequestRequestTypeDef",
)

BatchDeleteEvaluationJobErrorTypeDef = TypedDict(
    "BatchDeleteEvaluationJobErrorTypeDef",
    {
        "jobIdentifier": str,
        "code": str,
        "message": NotRequired[str],
    },
)
BatchDeleteEvaluationJobItemTypeDef = TypedDict(
    "BatchDeleteEvaluationJobItemTypeDef",
    {
        "jobIdentifier": str,
        "jobStatus": EvaluationJobStatusType,
    },
)
BatchDeleteEvaluationJobRequestRequestTypeDef = TypedDict(
    "BatchDeleteEvaluationJobRequestRequestTypeDef",
    {
        "jobIdentifiers": Sequence[str],
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
S3ConfigTypeDef = TypedDict(
    "S3ConfigTypeDef",
    {
        "bucketName": str,
        "keyPrefix": NotRequired[str],
    },
)
EvaluationOutputDataConfigTypeDef = TypedDict(
    "EvaluationOutputDataConfigTypeDef",
    {
        "s3Uri": str,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)
CreateGuardrailVersionRequestRequestTypeDef = TypedDict(
    "CreateGuardrailVersionRequestRequestTypeDef",
    {
        "guardrailIdentifier": str,
        "description": NotRequired[str],
        "clientRequestToken": NotRequired[str],
    },
)
OutputDataConfigTypeDef = TypedDict(
    "OutputDataConfigTypeDef",
    {
        "s3Uri": str,
    },
)
TrainingDataConfigTypeDef = TypedDict(
    "TrainingDataConfigTypeDef",
    {
        "s3Uri": str,
    },
)
VpcConfigTypeDef = TypedDict(
    "VpcConfigTypeDef",
    {
        "subnetIds": Sequence[str],
        "securityGroupIds": Sequence[str],
    },
)
CustomModelSummaryTypeDef = TypedDict(
    "CustomModelSummaryTypeDef",
    {
        "modelArn": str,
        "modelName": str,
        "creationTime": datetime,
        "baseModelArn": str,
        "baseModelName": str,
        "customizationType": NotRequired[CustomizationTypeType],
        "ownerAccountId": NotRequired[str],
    },
)
DeleteCustomModelRequestRequestTypeDef = TypedDict(
    "DeleteCustomModelRequestRequestTypeDef",
    {
        "modelIdentifier": str,
    },
)
DeleteGuardrailRequestRequestTypeDef = TypedDict(
    "DeleteGuardrailRequestRequestTypeDef",
    {
        "guardrailIdentifier": str,
        "guardrailVersion": NotRequired[str],
    },
)
DeleteImportedModelRequestRequestTypeDef = TypedDict(
    "DeleteImportedModelRequestRequestTypeDef",
    {
        "modelIdentifier": str,
    },
)
DeleteProvisionedModelThroughputRequestRequestTypeDef = TypedDict(
    "DeleteProvisionedModelThroughputRequestRequestTypeDef",
    {
        "provisionedModelId": str,
    },
)
EvaluationBedrockModelTypeDef = TypedDict(
    "EvaluationBedrockModelTypeDef",
    {
        "modelIdentifier": str,
        "inferenceParams": str,
    },
)
EvaluationDatasetLocationTypeDef = TypedDict(
    "EvaluationDatasetLocationTypeDef",
    {
        "s3Uri": NotRequired[str],
    },
)
EvaluationSummaryTypeDef = TypedDict(
    "EvaluationSummaryTypeDef",
    {
        "jobArn": str,
        "jobName": str,
        "status": EvaluationJobStatusType,
        "creationTime": datetime,
        "jobType": EvaluationJobTypeType,
        "evaluationTaskTypes": List[EvaluationTaskTypeType],
        "modelIdentifiers": List[str],
    },
)
FoundationModelLifecycleTypeDef = TypedDict(
    "FoundationModelLifecycleTypeDef",
    {
        "status": FoundationModelLifecycleStatusType,
    },
)
GetCustomModelRequestRequestTypeDef = TypedDict(
    "GetCustomModelRequestRequestTypeDef",
    {
        "modelIdentifier": str,
    },
)
TrainingMetricsTypeDef = TypedDict(
    "TrainingMetricsTypeDef",
    {
        "trainingLoss": NotRequired[float],
    },
)
ValidatorMetricTypeDef = TypedDict(
    "ValidatorMetricTypeDef",
    {
        "validationLoss": NotRequired[float],
    },
)
GetEvaluationJobRequestRequestTypeDef = TypedDict(
    "GetEvaluationJobRequestRequestTypeDef",
    {
        "jobIdentifier": str,
    },
)
GetFoundationModelRequestRequestTypeDef = TypedDict(
    "GetFoundationModelRequestRequestTypeDef",
    {
        "modelIdentifier": str,
    },
)
GetGuardrailRequestRequestTypeDef = TypedDict(
    "GetGuardrailRequestRequestTypeDef",
    {
        "guardrailIdentifier": str,
        "guardrailVersion": NotRequired[str],
    },
)
GetImportedModelRequestRequestTypeDef = TypedDict(
    "GetImportedModelRequestRequestTypeDef",
    {
        "modelIdentifier": str,
    },
)
GetInferenceProfileRequestRequestTypeDef = TypedDict(
    "GetInferenceProfileRequestRequestTypeDef",
    {
        "inferenceProfileIdentifier": str,
    },
)
InferenceProfileModelTypeDef = TypedDict(
    "InferenceProfileModelTypeDef",
    {
        "modelArn": NotRequired[str],
    },
)
GetModelCopyJobRequestRequestTypeDef = TypedDict(
    "GetModelCopyJobRequestRequestTypeDef",
    {
        "jobArn": str,
    },
)
GetModelCustomizationJobRequestRequestTypeDef = TypedDict(
    "GetModelCustomizationJobRequestRequestTypeDef",
    {
        "jobIdentifier": str,
    },
)
VpcConfigOutputTypeDef = TypedDict(
    "VpcConfigOutputTypeDef",
    {
        "subnetIds": List[str],
        "securityGroupIds": List[str],
    },
)
GetModelImportJobRequestRequestTypeDef = TypedDict(
    "GetModelImportJobRequestRequestTypeDef",
    {
        "jobIdentifier": str,
    },
)
GetModelInvocationJobRequestRequestTypeDef = TypedDict(
    "GetModelInvocationJobRequestRequestTypeDef",
    {
        "jobIdentifier": str,
    },
)
GetProvisionedModelThroughputRequestRequestTypeDef = TypedDict(
    "GetProvisionedModelThroughputRequestRequestTypeDef",
    {
        "provisionedModelId": str,
    },
)
GuardrailContentFilterConfigTypeDef = TypedDict(
    "GuardrailContentFilterConfigTypeDef",
    {
        "type": GuardrailContentFilterTypeType,
        "inputStrength": GuardrailFilterStrengthType,
        "outputStrength": GuardrailFilterStrengthType,
    },
)
GuardrailContentFilterTypeDef = TypedDict(
    "GuardrailContentFilterTypeDef",
    {
        "type": GuardrailContentFilterTypeType,
        "inputStrength": GuardrailFilterStrengthType,
        "outputStrength": GuardrailFilterStrengthType,
    },
)
GuardrailContextualGroundingFilterConfigTypeDef = TypedDict(
    "GuardrailContextualGroundingFilterConfigTypeDef",
    {
        "type": GuardrailContextualGroundingFilterTypeType,
        "threshold": float,
    },
)
GuardrailContextualGroundingFilterTypeDef = TypedDict(
    "GuardrailContextualGroundingFilterTypeDef",
    {
        "type": GuardrailContextualGroundingFilterTypeType,
        "threshold": float,
    },
)
GuardrailManagedWordsConfigTypeDef = TypedDict(
    "GuardrailManagedWordsConfigTypeDef",
    {
        "type": Literal["PROFANITY"],
    },
)
GuardrailManagedWordsTypeDef = TypedDict(
    "GuardrailManagedWordsTypeDef",
    {
        "type": Literal["PROFANITY"],
    },
)
GuardrailPiiEntityConfigTypeDef = TypedDict(
    "GuardrailPiiEntityConfigTypeDef",
    {
        "type": GuardrailPiiEntityTypeType,
        "action": GuardrailSensitiveInformationActionType,
    },
)
GuardrailPiiEntityTypeDef = TypedDict(
    "GuardrailPiiEntityTypeDef",
    {
        "type": GuardrailPiiEntityTypeType,
        "action": GuardrailSensitiveInformationActionType,
    },
)
GuardrailRegexConfigTypeDef = TypedDict(
    "GuardrailRegexConfigTypeDef",
    {
        "name": str,
        "pattern": str,
        "action": GuardrailSensitiveInformationActionType,
        "description": NotRequired[str],
    },
)
GuardrailRegexTypeDef = TypedDict(
    "GuardrailRegexTypeDef",
    {
        "name": str,
        "pattern": str,
        "action": GuardrailSensitiveInformationActionType,
        "description": NotRequired[str],
    },
)
GuardrailSummaryTypeDef = TypedDict(
    "GuardrailSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "status": GuardrailStatusType,
        "name": str,
        "version": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "description": NotRequired[str],
    },
)
GuardrailTopicConfigTypeDef = TypedDict(
    "GuardrailTopicConfigTypeDef",
    {
        "name": str,
        "definition": str,
        "type": Literal["DENY"],
        "examples": NotRequired[Sequence[str]],
    },
)
GuardrailTopicTypeDef = TypedDict(
    "GuardrailTopicTypeDef",
    {
        "name": str,
        "definition": str,
        "examples": NotRequired[List[str]],
        "type": NotRequired[Literal["DENY"]],
    },
)
GuardrailWordConfigTypeDef = TypedDict(
    "GuardrailWordConfigTypeDef",
    {
        "text": str,
    },
)
GuardrailWordTypeDef = TypedDict(
    "GuardrailWordTypeDef",
    {
        "text": str,
    },
)
HumanEvaluationCustomMetricTypeDef = TypedDict(
    "HumanEvaluationCustomMetricTypeDef",
    {
        "name": str,
        "ratingMethod": str,
        "description": NotRequired[str],
    },
)
HumanWorkflowConfigTypeDef = TypedDict(
    "HumanWorkflowConfigTypeDef",
    {
        "flowDefinitionArn": str,
        "instructions": NotRequired[str],
    },
)
ImportedModelSummaryTypeDef = TypedDict(
    "ImportedModelSummaryTypeDef",
    {
        "modelArn": str,
        "modelName": str,
        "creationTime": datetime,
        "instructSupported": NotRequired[bool],
        "modelArchitecture": NotRequired[str],
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
TimestampTypeDef = Union[datetime, str]
ListFoundationModelsRequestRequestTypeDef = TypedDict(
    "ListFoundationModelsRequestRequestTypeDef",
    {
        "byProvider": NotRequired[str],
        "byCustomizationType": NotRequired[ModelCustomizationType],
        "byOutputModality": NotRequired[ModelModalityType],
        "byInferenceType": NotRequired[InferenceTypeType],
    },
)
ListGuardrailsRequestRequestTypeDef = TypedDict(
    "ListGuardrailsRequestRequestTypeDef",
    {
        "guardrailIdentifier": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListInferenceProfilesRequestRequestTypeDef = TypedDict(
    "ListInferenceProfilesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ModelCustomizationJobSummaryTypeDef = TypedDict(
    "ModelCustomizationJobSummaryTypeDef",
    {
        "jobArn": str,
        "baseModelArn": str,
        "jobName": str,
        "status": ModelCustomizationJobStatusType,
        "creationTime": datetime,
        "lastModifiedTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
        "customModelArn": NotRequired[str],
        "customModelName": NotRequired[str],
        "customizationType": NotRequired[CustomizationTypeType],
    },
)
ModelImportJobSummaryTypeDef = TypedDict(
    "ModelImportJobSummaryTypeDef",
    {
        "jobArn": str,
        "jobName": str,
        "status": ModelImportJobStatusType,
        "creationTime": datetime,
        "lastModifiedTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
        "importedModelArn": NotRequired[str],
        "importedModelName": NotRequired[str],
    },
)
ProvisionedModelSummaryTypeDef = TypedDict(
    "ProvisionedModelSummaryTypeDef",
    {
        "provisionedModelName": str,
        "provisionedModelArn": str,
        "modelArn": str,
        "desiredModelArn": str,
        "foundationModelArn": str,
        "modelUnits": int,
        "desiredModelUnits": int,
        "status": ProvisionedModelStatusType,
        "creationTime": datetime,
        "lastModifiedTime": datetime,
        "commitmentDuration": NotRequired[CommitmentDurationType],
        "commitmentExpirationTime": NotRequired[datetime],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
    },
)
S3DataSourceTypeDef = TypedDict(
    "S3DataSourceTypeDef",
    {
        "s3Uri": str,
    },
)
ModelInvocationJobS3InputDataConfigTypeDef = TypedDict(
    "ModelInvocationJobS3InputDataConfigTypeDef",
    {
        "s3Uri": str,
        "s3InputFormat": NotRequired[Literal["JSONL"]],
        "s3BucketOwner": NotRequired[str],
    },
)
ModelInvocationJobS3OutputDataConfigTypeDef = TypedDict(
    "ModelInvocationJobS3OutputDataConfigTypeDef",
    {
        "s3Uri": str,
        "s3EncryptionKeyId": NotRequired[str],
        "s3BucketOwner": NotRequired[str],
    },
)
StopEvaluationJobRequestRequestTypeDef = TypedDict(
    "StopEvaluationJobRequestRequestTypeDef",
    {
        "jobIdentifier": str,
    },
)
StopModelCustomizationJobRequestRequestTypeDef = TypedDict(
    "StopModelCustomizationJobRequestRequestTypeDef",
    {
        "jobIdentifier": str,
    },
)
StopModelInvocationJobRequestRequestTypeDef = TypedDict(
    "StopModelInvocationJobRequestRequestTypeDef",
    {
        "jobIdentifier": str,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
        "tagKeys": Sequence[str],
    },
)
UpdateProvisionedModelThroughputRequestRequestTypeDef = TypedDict(
    "UpdateProvisionedModelThroughputRequestRequestTypeDef",
    {
        "provisionedModelId": str,
        "desiredProvisionedModelName": NotRequired[str],
        "desiredModelId": NotRequired[str],
    },
)
ValidatorTypeDef = TypedDict(
    "ValidatorTypeDef",
    {
        "s3Uri": str,
    },
)
BatchDeleteEvaluationJobResponseTypeDef = TypedDict(
    "BatchDeleteEvaluationJobResponseTypeDef",
    {
        "errors": List[BatchDeleteEvaluationJobErrorTypeDef],
        "evaluationJobs": List[BatchDeleteEvaluationJobItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEvaluationJobResponseTypeDef = TypedDict(
    "CreateEvaluationJobResponseTypeDef",
    {
        "jobArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGuardrailResponseTypeDef = TypedDict(
    "CreateGuardrailResponseTypeDef",
    {
        "guardrailId": str,
        "guardrailArn": str,
        "version": str,
        "createdAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGuardrailVersionResponseTypeDef = TypedDict(
    "CreateGuardrailVersionResponseTypeDef",
    {
        "guardrailId": str,
        "version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateModelCopyJobResponseTypeDef = TypedDict(
    "CreateModelCopyJobResponseTypeDef",
    {
        "jobArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateModelCustomizationJobResponseTypeDef = TypedDict(
    "CreateModelCustomizationJobResponseTypeDef",
    {
        "jobArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateModelImportJobResponseTypeDef = TypedDict(
    "CreateModelImportJobResponseTypeDef",
    {
        "jobArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateModelInvocationJobResponseTypeDef = TypedDict(
    "CreateModelInvocationJobResponseTypeDef",
    {
        "jobArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProvisionedModelThroughputResponseTypeDef = TypedDict(
    "CreateProvisionedModelThroughputResponseTypeDef",
    {
        "provisionedModelArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetProvisionedModelThroughputResponseTypeDef = TypedDict(
    "GetProvisionedModelThroughputResponseTypeDef",
    {
        "modelUnits": int,
        "desiredModelUnits": int,
        "provisionedModelName": str,
        "provisionedModelArn": str,
        "modelArn": str,
        "desiredModelArn": str,
        "foundationModelArn": str,
        "status": ProvisionedModelStatusType,
        "creationTime": datetime,
        "lastModifiedTime": datetime,
        "failureMessage": str,
        "commitmentDuration": CommitmentDurationType,
        "commitmentExpirationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateGuardrailResponseTypeDef = TypedDict(
    "UpdateGuardrailResponseTypeDef",
    {
        "guardrailId": str,
        "guardrailArn": str,
        "version": str,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CloudWatchConfigTypeDef = TypedDict(
    "CloudWatchConfigTypeDef",
    {
        "logGroupName": str,
        "roleArn": str,
        "largeDataDeliveryS3Config": NotRequired[S3ConfigTypeDef],
    },
)
CreateModelCopyJobRequestRequestTypeDef = TypedDict(
    "CreateModelCopyJobRequestRequestTypeDef",
    {
        "sourceModelArn": str,
        "targetModelName": str,
        "modelKmsKeyId": NotRequired[str],
        "targetModelTags": NotRequired[Sequence[TagTypeDef]],
        "clientRequestToken": NotRequired[str],
    },
)
CreateProvisionedModelThroughputRequestRequestTypeDef = TypedDict(
    "CreateProvisionedModelThroughputRequestRequestTypeDef",
    {
        "modelUnits": int,
        "provisionedModelName": str,
        "modelId": str,
        "clientRequestToken": NotRequired[str],
        "commitmentDuration": NotRequired[CommitmentDurationType],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
GetModelCopyJobResponseTypeDef = TypedDict(
    "GetModelCopyJobResponseTypeDef",
    {
        "jobArn": str,
        "status": ModelCopyJobStatusType,
        "creationTime": datetime,
        "targetModelArn": str,
        "targetModelName": str,
        "sourceAccountId": str,
        "sourceModelArn": str,
        "targetModelKmsKeyArn": str,
        "targetModelTags": List[TagTypeDef],
        "failureMessage": str,
        "sourceModelName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModelCopyJobSummaryTypeDef = TypedDict(
    "ModelCopyJobSummaryTypeDef",
    {
        "jobArn": str,
        "status": ModelCopyJobStatusType,
        "creationTime": datetime,
        "targetModelArn": str,
        "sourceAccountId": str,
        "sourceModelArn": str,
        "targetModelName": NotRequired[str],
        "targetModelKmsKeyArn": NotRequired[str],
        "targetModelTags": NotRequired[List[TagTypeDef]],
        "failureMessage": NotRequired[str],
        "sourceModelName": NotRequired[str],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
        "tags": Sequence[TagTypeDef],
    },
)
ListCustomModelsResponseTypeDef = TypedDict(
    "ListCustomModelsResponseTypeDef",
    {
        "nextToken": str,
        "modelSummaries": List[CustomModelSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EvaluationModelConfigTypeDef = TypedDict(
    "EvaluationModelConfigTypeDef",
    {
        "bedrockModel": NotRequired[EvaluationBedrockModelTypeDef],
    },
)
EvaluationDatasetTypeDef = TypedDict(
    "EvaluationDatasetTypeDef",
    {
        "name": str,
        "datasetLocation": NotRequired[EvaluationDatasetLocationTypeDef],
    },
)
ListEvaluationJobsResponseTypeDef = TypedDict(
    "ListEvaluationJobsResponseTypeDef",
    {
        "nextToken": str,
        "jobSummaries": List[EvaluationSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FoundationModelDetailsTypeDef = TypedDict(
    "FoundationModelDetailsTypeDef",
    {
        "modelArn": str,
        "modelId": str,
        "modelName": NotRequired[str],
        "providerName": NotRequired[str],
        "inputModalities": NotRequired[List[ModelModalityType]],
        "outputModalities": NotRequired[List[ModelModalityType]],
        "responseStreamingSupported": NotRequired[bool],
        "customizationsSupported": NotRequired[List[ModelCustomizationType]],
        "inferenceTypesSupported": NotRequired[List[InferenceTypeType]],
        "modelLifecycle": NotRequired[FoundationModelLifecycleTypeDef],
    },
)
FoundationModelSummaryTypeDef = TypedDict(
    "FoundationModelSummaryTypeDef",
    {
        "modelArn": str,
        "modelId": str,
        "modelName": NotRequired[str],
        "providerName": NotRequired[str],
        "inputModalities": NotRequired[List[ModelModalityType]],
        "outputModalities": NotRequired[List[ModelModalityType]],
        "responseStreamingSupported": NotRequired[bool],
        "customizationsSupported": NotRequired[List[ModelCustomizationType]],
        "inferenceTypesSupported": NotRequired[List[InferenceTypeType]],
        "modelLifecycle": NotRequired[FoundationModelLifecycleTypeDef],
    },
)
GetInferenceProfileResponseTypeDef = TypedDict(
    "GetInferenceProfileResponseTypeDef",
    {
        "inferenceProfileName": str,
        "models": List[InferenceProfileModelTypeDef],
        "description": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "inferenceProfileArn": str,
        "inferenceProfileId": str,
        "status": Literal["ACTIVE"],
        "type": Literal["SYSTEM_DEFINED"],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InferenceProfileSummaryTypeDef = TypedDict(
    "InferenceProfileSummaryTypeDef",
    {
        "inferenceProfileName": str,
        "models": List[InferenceProfileModelTypeDef],
        "inferenceProfileArn": str,
        "inferenceProfileId": str,
        "status": Literal["ACTIVE"],
        "type": Literal["SYSTEM_DEFINED"],
        "description": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
    },
)
GuardrailContentPolicyConfigTypeDef = TypedDict(
    "GuardrailContentPolicyConfigTypeDef",
    {
        "filtersConfig": Sequence[GuardrailContentFilterConfigTypeDef],
    },
)
GuardrailContentPolicyTypeDef = TypedDict(
    "GuardrailContentPolicyTypeDef",
    {
        "filters": NotRequired[List[GuardrailContentFilterTypeDef]],
    },
)
GuardrailContextualGroundingPolicyConfigTypeDef = TypedDict(
    "GuardrailContextualGroundingPolicyConfigTypeDef",
    {
        "filtersConfig": Sequence[GuardrailContextualGroundingFilterConfigTypeDef],
    },
)
GuardrailContextualGroundingPolicyTypeDef = TypedDict(
    "GuardrailContextualGroundingPolicyTypeDef",
    {
        "filters": List[GuardrailContextualGroundingFilterTypeDef],
    },
)
GuardrailSensitiveInformationPolicyConfigTypeDef = TypedDict(
    "GuardrailSensitiveInformationPolicyConfigTypeDef",
    {
        "piiEntitiesConfig": NotRequired[Sequence[GuardrailPiiEntityConfigTypeDef]],
        "regexesConfig": NotRequired[Sequence[GuardrailRegexConfigTypeDef]],
    },
)
GuardrailSensitiveInformationPolicyTypeDef = TypedDict(
    "GuardrailSensitiveInformationPolicyTypeDef",
    {
        "piiEntities": NotRequired[List[GuardrailPiiEntityTypeDef]],
        "regexes": NotRequired[List[GuardrailRegexTypeDef]],
    },
)
ListGuardrailsResponseTypeDef = TypedDict(
    "ListGuardrailsResponseTypeDef",
    {
        "guardrails": List[GuardrailSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GuardrailTopicPolicyConfigTypeDef = TypedDict(
    "GuardrailTopicPolicyConfigTypeDef",
    {
        "topicsConfig": Sequence[GuardrailTopicConfigTypeDef],
    },
)
GuardrailTopicPolicyTypeDef = TypedDict(
    "GuardrailTopicPolicyTypeDef",
    {
        "topics": List[GuardrailTopicTypeDef],
    },
)
GuardrailWordPolicyConfigTypeDef = TypedDict(
    "GuardrailWordPolicyConfigTypeDef",
    {
        "wordsConfig": NotRequired[Sequence[GuardrailWordConfigTypeDef]],
        "managedWordListsConfig": NotRequired[Sequence[GuardrailManagedWordsConfigTypeDef]],
    },
)
GuardrailWordPolicyTypeDef = TypedDict(
    "GuardrailWordPolicyTypeDef",
    {
        "words": NotRequired[List[GuardrailWordTypeDef]],
        "managedWordLists": NotRequired[List[GuardrailManagedWordsTypeDef]],
    },
)
ListImportedModelsResponseTypeDef = TypedDict(
    "ListImportedModelsResponseTypeDef",
    {
        "nextToken": str,
        "modelSummaries": List[ImportedModelSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListGuardrailsRequestListGuardrailsPaginateTypeDef = TypedDict(
    "ListGuardrailsRequestListGuardrailsPaginateTypeDef",
    {
        "guardrailIdentifier": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListInferenceProfilesRequestListInferenceProfilesPaginateTypeDef = TypedDict(
    "ListInferenceProfilesRequestListInferenceProfilesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCustomModelsRequestListCustomModelsPaginateTypeDef = TypedDict(
    "ListCustomModelsRequestListCustomModelsPaginateTypeDef",
    {
        "creationTimeBefore": NotRequired[TimestampTypeDef],
        "creationTimeAfter": NotRequired[TimestampTypeDef],
        "nameContains": NotRequired[str],
        "baseModelArnEquals": NotRequired[str],
        "foundationModelArnEquals": NotRequired[str],
        "sortBy": NotRequired[Literal["CreationTime"]],
        "sortOrder": NotRequired[SortOrderType],
        "isOwned": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCustomModelsRequestRequestTypeDef = TypedDict(
    "ListCustomModelsRequestRequestTypeDef",
    {
        "creationTimeBefore": NotRequired[TimestampTypeDef],
        "creationTimeAfter": NotRequired[TimestampTypeDef],
        "nameContains": NotRequired[str],
        "baseModelArnEquals": NotRequired[str],
        "foundationModelArnEquals": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortBy": NotRequired[Literal["CreationTime"]],
        "sortOrder": NotRequired[SortOrderType],
        "isOwned": NotRequired[bool],
    },
)
ListEvaluationJobsRequestListEvaluationJobsPaginateTypeDef = TypedDict(
    "ListEvaluationJobsRequestListEvaluationJobsPaginateTypeDef",
    {
        "creationTimeAfter": NotRequired[TimestampTypeDef],
        "creationTimeBefore": NotRequired[TimestampTypeDef],
        "statusEquals": NotRequired[EvaluationJobStatusType],
        "nameContains": NotRequired[str],
        "sortBy": NotRequired[Literal["CreationTime"]],
        "sortOrder": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEvaluationJobsRequestRequestTypeDef = TypedDict(
    "ListEvaluationJobsRequestRequestTypeDef",
    {
        "creationTimeAfter": NotRequired[TimestampTypeDef],
        "creationTimeBefore": NotRequired[TimestampTypeDef],
        "statusEquals": NotRequired[EvaluationJobStatusType],
        "nameContains": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortBy": NotRequired[Literal["CreationTime"]],
        "sortOrder": NotRequired[SortOrderType],
    },
)
ListImportedModelsRequestListImportedModelsPaginateTypeDef = TypedDict(
    "ListImportedModelsRequestListImportedModelsPaginateTypeDef",
    {
        "creationTimeBefore": NotRequired[TimestampTypeDef],
        "creationTimeAfter": NotRequired[TimestampTypeDef],
        "nameContains": NotRequired[str],
        "sortBy": NotRequired[Literal["CreationTime"]],
        "sortOrder": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListImportedModelsRequestRequestTypeDef = TypedDict(
    "ListImportedModelsRequestRequestTypeDef",
    {
        "creationTimeBefore": NotRequired[TimestampTypeDef],
        "creationTimeAfter": NotRequired[TimestampTypeDef],
        "nameContains": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortBy": NotRequired[Literal["CreationTime"]],
        "sortOrder": NotRequired[SortOrderType],
    },
)
ListModelCopyJobsRequestListModelCopyJobsPaginateTypeDef = TypedDict(
    "ListModelCopyJobsRequestListModelCopyJobsPaginateTypeDef",
    {
        "creationTimeAfter": NotRequired[TimestampTypeDef],
        "creationTimeBefore": NotRequired[TimestampTypeDef],
        "statusEquals": NotRequired[ModelCopyJobStatusType],
        "sourceAccountEquals": NotRequired[str],
        "sourceModelArnEquals": NotRequired[str],
        "targetModelNameContains": NotRequired[str],
        "sortBy": NotRequired[Literal["CreationTime"]],
        "sortOrder": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListModelCopyJobsRequestRequestTypeDef = TypedDict(
    "ListModelCopyJobsRequestRequestTypeDef",
    {
        "creationTimeAfter": NotRequired[TimestampTypeDef],
        "creationTimeBefore": NotRequired[TimestampTypeDef],
        "statusEquals": NotRequired[ModelCopyJobStatusType],
        "sourceAccountEquals": NotRequired[str],
        "sourceModelArnEquals": NotRequired[str],
        "targetModelNameContains": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortBy": NotRequired[Literal["CreationTime"]],
        "sortOrder": NotRequired[SortOrderType],
    },
)
ListModelCustomizationJobsRequestListModelCustomizationJobsPaginateTypeDef = TypedDict(
    "ListModelCustomizationJobsRequestListModelCustomizationJobsPaginateTypeDef",
    {
        "creationTimeAfter": NotRequired[TimestampTypeDef],
        "creationTimeBefore": NotRequired[TimestampTypeDef],
        "statusEquals": NotRequired[FineTuningJobStatusType],
        "nameContains": NotRequired[str],
        "sortBy": NotRequired[Literal["CreationTime"]],
        "sortOrder": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListModelCustomizationJobsRequestRequestTypeDef = TypedDict(
    "ListModelCustomizationJobsRequestRequestTypeDef",
    {
        "creationTimeAfter": NotRequired[TimestampTypeDef],
        "creationTimeBefore": NotRequired[TimestampTypeDef],
        "statusEquals": NotRequired[FineTuningJobStatusType],
        "nameContains": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortBy": NotRequired[Literal["CreationTime"]],
        "sortOrder": NotRequired[SortOrderType],
    },
)
ListModelImportJobsRequestListModelImportJobsPaginateTypeDef = TypedDict(
    "ListModelImportJobsRequestListModelImportJobsPaginateTypeDef",
    {
        "creationTimeAfter": NotRequired[TimestampTypeDef],
        "creationTimeBefore": NotRequired[TimestampTypeDef],
        "statusEquals": NotRequired[ModelImportJobStatusType],
        "nameContains": NotRequired[str],
        "sortBy": NotRequired[Literal["CreationTime"]],
        "sortOrder": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListModelImportJobsRequestRequestTypeDef = TypedDict(
    "ListModelImportJobsRequestRequestTypeDef",
    {
        "creationTimeAfter": NotRequired[TimestampTypeDef],
        "creationTimeBefore": NotRequired[TimestampTypeDef],
        "statusEquals": NotRequired[ModelImportJobStatusType],
        "nameContains": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortBy": NotRequired[Literal["CreationTime"]],
        "sortOrder": NotRequired[SortOrderType],
    },
)
ListModelInvocationJobsRequestListModelInvocationJobsPaginateTypeDef = TypedDict(
    "ListModelInvocationJobsRequestListModelInvocationJobsPaginateTypeDef",
    {
        "submitTimeAfter": NotRequired[TimestampTypeDef],
        "submitTimeBefore": NotRequired[TimestampTypeDef],
        "statusEquals": NotRequired[ModelInvocationJobStatusType],
        "nameContains": NotRequired[str],
        "sortBy": NotRequired[Literal["CreationTime"]],
        "sortOrder": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListModelInvocationJobsRequestRequestTypeDef = TypedDict(
    "ListModelInvocationJobsRequestRequestTypeDef",
    {
        "submitTimeAfter": NotRequired[TimestampTypeDef],
        "submitTimeBefore": NotRequired[TimestampTypeDef],
        "statusEquals": NotRequired[ModelInvocationJobStatusType],
        "nameContains": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortBy": NotRequired[Literal["CreationTime"]],
        "sortOrder": NotRequired[SortOrderType],
    },
)
ListProvisionedModelThroughputsRequestListProvisionedModelThroughputsPaginateTypeDef = TypedDict(
    "ListProvisionedModelThroughputsRequestListProvisionedModelThroughputsPaginateTypeDef",
    {
        "creationTimeAfter": NotRequired[TimestampTypeDef],
        "creationTimeBefore": NotRequired[TimestampTypeDef],
        "statusEquals": NotRequired[ProvisionedModelStatusType],
        "modelArnEquals": NotRequired[str],
        "nameContains": NotRequired[str],
        "sortBy": NotRequired[Literal["CreationTime"]],
        "sortOrder": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProvisionedModelThroughputsRequestRequestTypeDef = TypedDict(
    "ListProvisionedModelThroughputsRequestRequestTypeDef",
    {
        "creationTimeAfter": NotRequired[TimestampTypeDef],
        "creationTimeBefore": NotRequired[TimestampTypeDef],
        "statusEquals": NotRequired[ProvisionedModelStatusType],
        "modelArnEquals": NotRequired[str],
        "nameContains": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortBy": NotRequired[Literal["CreationTime"]],
        "sortOrder": NotRequired[SortOrderType],
    },
)
ListModelCustomizationJobsResponseTypeDef = TypedDict(
    "ListModelCustomizationJobsResponseTypeDef",
    {
        "nextToken": str,
        "modelCustomizationJobSummaries": List[ModelCustomizationJobSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListModelImportJobsResponseTypeDef = TypedDict(
    "ListModelImportJobsResponseTypeDef",
    {
        "nextToken": str,
        "modelImportJobSummaries": List[ModelImportJobSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListProvisionedModelThroughputsResponseTypeDef = TypedDict(
    "ListProvisionedModelThroughputsResponseTypeDef",
    {
        "nextToken": str,
        "provisionedModelSummaries": List[ProvisionedModelSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModelDataSourceTypeDef = TypedDict(
    "ModelDataSourceTypeDef",
    {
        "s3DataSource": NotRequired[S3DataSourceTypeDef],
    },
)
ModelInvocationJobInputDataConfigTypeDef = TypedDict(
    "ModelInvocationJobInputDataConfigTypeDef",
    {
        "s3InputDataConfig": NotRequired[ModelInvocationJobS3InputDataConfigTypeDef],
    },
)
ModelInvocationJobOutputDataConfigTypeDef = TypedDict(
    "ModelInvocationJobOutputDataConfigTypeDef",
    {
        "s3OutputDataConfig": NotRequired[ModelInvocationJobS3OutputDataConfigTypeDef],
    },
)
ValidationDataConfigOutputTypeDef = TypedDict(
    "ValidationDataConfigOutputTypeDef",
    {
        "validators": List[ValidatorTypeDef],
    },
)
ValidationDataConfigTypeDef = TypedDict(
    "ValidationDataConfigTypeDef",
    {
        "validators": Sequence[ValidatorTypeDef],
    },
)
LoggingConfigTypeDef = TypedDict(
    "LoggingConfigTypeDef",
    {
        "cloudWatchConfig": NotRequired[CloudWatchConfigTypeDef],
        "s3Config": NotRequired[S3ConfigTypeDef],
        "textDataDeliveryEnabled": NotRequired[bool],
        "imageDataDeliveryEnabled": NotRequired[bool],
        "embeddingDataDeliveryEnabled": NotRequired[bool],
    },
)
ListModelCopyJobsResponseTypeDef = TypedDict(
    "ListModelCopyJobsResponseTypeDef",
    {
        "nextToken": str,
        "modelCopyJobSummaries": List[ModelCopyJobSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EvaluationInferenceConfigOutputTypeDef = TypedDict(
    "EvaluationInferenceConfigOutputTypeDef",
    {
        "models": NotRequired[List[EvaluationModelConfigTypeDef]],
    },
)
EvaluationInferenceConfigTypeDef = TypedDict(
    "EvaluationInferenceConfigTypeDef",
    {
        "models": NotRequired[Sequence[EvaluationModelConfigTypeDef]],
    },
)
EvaluationDatasetMetricConfigOutputTypeDef = TypedDict(
    "EvaluationDatasetMetricConfigOutputTypeDef",
    {
        "taskType": EvaluationTaskTypeType,
        "dataset": EvaluationDatasetTypeDef,
        "metricNames": List[str],
    },
)
EvaluationDatasetMetricConfigTypeDef = TypedDict(
    "EvaluationDatasetMetricConfigTypeDef",
    {
        "taskType": EvaluationTaskTypeType,
        "dataset": EvaluationDatasetTypeDef,
        "metricNames": Sequence[str],
    },
)
GetFoundationModelResponseTypeDef = TypedDict(
    "GetFoundationModelResponseTypeDef",
    {
        "modelDetails": FoundationModelDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListFoundationModelsResponseTypeDef = TypedDict(
    "ListFoundationModelsResponseTypeDef",
    {
        "modelSummaries": List[FoundationModelSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListInferenceProfilesResponseTypeDef = TypedDict(
    "ListInferenceProfilesResponseTypeDef",
    {
        "inferenceProfileSummaries": List[InferenceProfileSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGuardrailRequestRequestTypeDef = TypedDict(
    "CreateGuardrailRequestRequestTypeDef",
    {
        "name": str,
        "blockedInputMessaging": str,
        "blockedOutputsMessaging": str,
        "description": NotRequired[str],
        "topicPolicyConfig": NotRequired[GuardrailTopicPolicyConfigTypeDef],
        "contentPolicyConfig": NotRequired[GuardrailContentPolicyConfigTypeDef],
        "wordPolicyConfig": NotRequired[GuardrailWordPolicyConfigTypeDef],
        "sensitiveInformationPolicyConfig": NotRequired[
            GuardrailSensitiveInformationPolicyConfigTypeDef
        ],
        "contextualGroundingPolicyConfig": NotRequired[
            GuardrailContextualGroundingPolicyConfigTypeDef
        ],
        "kmsKeyId": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "clientRequestToken": NotRequired[str],
    },
)
UpdateGuardrailRequestRequestTypeDef = TypedDict(
    "UpdateGuardrailRequestRequestTypeDef",
    {
        "guardrailIdentifier": str,
        "name": str,
        "blockedInputMessaging": str,
        "blockedOutputsMessaging": str,
        "description": NotRequired[str],
        "topicPolicyConfig": NotRequired[GuardrailTopicPolicyConfigTypeDef],
        "contentPolicyConfig": NotRequired[GuardrailContentPolicyConfigTypeDef],
        "wordPolicyConfig": NotRequired[GuardrailWordPolicyConfigTypeDef],
        "sensitiveInformationPolicyConfig": NotRequired[
            GuardrailSensitiveInformationPolicyConfigTypeDef
        ],
        "contextualGroundingPolicyConfig": NotRequired[
            GuardrailContextualGroundingPolicyConfigTypeDef
        ],
        "kmsKeyId": NotRequired[str],
    },
)
GetGuardrailResponseTypeDef = TypedDict(
    "GetGuardrailResponseTypeDef",
    {
        "name": str,
        "description": str,
        "guardrailId": str,
        "guardrailArn": str,
        "version": str,
        "status": GuardrailStatusType,
        "topicPolicy": GuardrailTopicPolicyTypeDef,
        "contentPolicy": GuardrailContentPolicyTypeDef,
        "wordPolicy": GuardrailWordPolicyTypeDef,
        "sensitiveInformationPolicy": GuardrailSensitiveInformationPolicyTypeDef,
        "contextualGroundingPolicy": GuardrailContextualGroundingPolicyTypeDef,
        "createdAt": datetime,
        "updatedAt": datetime,
        "statusReasons": List[str],
        "failureRecommendations": List[str],
        "blockedInputMessaging": str,
        "blockedOutputsMessaging": str,
        "kmsKeyArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateModelImportJobRequestRequestTypeDef = TypedDict(
    "CreateModelImportJobRequestRequestTypeDef",
    {
        "jobName": str,
        "importedModelName": str,
        "roleArn": str,
        "modelDataSource": ModelDataSourceTypeDef,
        "jobTags": NotRequired[Sequence[TagTypeDef]],
        "importedModelTags": NotRequired[Sequence[TagTypeDef]],
        "clientRequestToken": NotRequired[str],
        "vpcConfig": NotRequired[VpcConfigTypeDef],
        "importedModelKmsKeyId": NotRequired[str],
    },
)
GetImportedModelResponseTypeDef = TypedDict(
    "GetImportedModelResponseTypeDef",
    {
        "modelArn": str,
        "modelName": str,
        "jobName": str,
        "jobArn": str,
        "modelDataSource": ModelDataSourceTypeDef,
        "creationTime": datetime,
        "modelArchitecture": str,
        "modelKmsKeyArn": str,
        "instructSupported": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetModelImportJobResponseTypeDef = TypedDict(
    "GetModelImportJobResponseTypeDef",
    {
        "jobArn": str,
        "jobName": str,
        "importedModelName": str,
        "importedModelArn": str,
        "roleArn": str,
        "modelDataSource": ModelDataSourceTypeDef,
        "status": ModelImportJobStatusType,
        "failureMessage": str,
        "creationTime": datetime,
        "lastModifiedTime": datetime,
        "endTime": datetime,
        "vpcConfig": VpcConfigOutputTypeDef,
        "importedModelKmsKeyArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateModelInvocationJobRequestRequestTypeDef = TypedDict(
    "CreateModelInvocationJobRequestRequestTypeDef",
    {
        "jobName": str,
        "roleArn": str,
        "modelId": str,
        "inputDataConfig": ModelInvocationJobInputDataConfigTypeDef,
        "outputDataConfig": ModelInvocationJobOutputDataConfigTypeDef,
        "clientRequestToken": NotRequired[str],
        "vpcConfig": NotRequired[VpcConfigTypeDef],
        "timeoutDurationInHours": NotRequired[int],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
GetModelInvocationJobResponseTypeDef = TypedDict(
    "GetModelInvocationJobResponseTypeDef",
    {
        "jobArn": str,
        "jobName": str,
        "modelId": str,
        "clientRequestToken": str,
        "roleArn": str,
        "status": ModelInvocationJobStatusType,
        "message": str,
        "submitTime": datetime,
        "lastModifiedTime": datetime,
        "endTime": datetime,
        "inputDataConfig": ModelInvocationJobInputDataConfigTypeDef,
        "outputDataConfig": ModelInvocationJobOutputDataConfigTypeDef,
        "vpcConfig": VpcConfigOutputTypeDef,
        "timeoutDurationInHours": int,
        "jobExpirationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModelInvocationJobSummaryTypeDef = TypedDict(
    "ModelInvocationJobSummaryTypeDef",
    {
        "jobArn": str,
        "jobName": str,
        "modelId": str,
        "roleArn": str,
        "submitTime": datetime,
        "inputDataConfig": ModelInvocationJobInputDataConfigTypeDef,
        "outputDataConfig": ModelInvocationJobOutputDataConfigTypeDef,
        "clientRequestToken": NotRequired[str],
        "status": NotRequired[ModelInvocationJobStatusType],
        "message": NotRequired[str],
        "lastModifiedTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
        "vpcConfig": NotRequired[VpcConfigOutputTypeDef],
        "timeoutDurationInHours": NotRequired[int],
        "jobExpirationTime": NotRequired[datetime],
    },
)
GetCustomModelResponseTypeDef = TypedDict(
    "GetCustomModelResponseTypeDef",
    {
        "modelArn": str,
        "modelName": str,
        "jobName": str,
        "jobArn": str,
        "baseModelArn": str,
        "customizationType": CustomizationTypeType,
        "modelKmsKeyArn": str,
        "hyperParameters": Dict[str, str],
        "trainingDataConfig": TrainingDataConfigTypeDef,
        "validationDataConfig": ValidationDataConfigOutputTypeDef,
        "outputDataConfig": OutputDataConfigTypeDef,
        "trainingMetrics": TrainingMetricsTypeDef,
        "validationMetrics": List[ValidatorMetricTypeDef],
        "creationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetModelCustomizationJobResponseTypeDef = TypedDict(
    "GetModelCustomizationJobResponseTypeDef",
    {
        "jobArn": str,
        "jobName": str,
        "outputModelName": str,
        "outputModelArn": str,
        "clientRequestToken": str,
        "roleArn": str,
        "status": ModelCustomizationJobStatusType,
        "failureMessage": str,
        "creationTime": datetime,
        "lastModifiedTime": datetime,
        "endTime": datetime,
        "baseModelArn": str,
        "hyperParameters": Dict[str, str],
        "trainingDataConfig": TrainingDataConfigTypeDef,
        "validationDataConfig": ValidationDataConfigOutputTypeDef,
        "outputDataConfig": OutputDataConfigTypeDef,
        "customizationType": CustomizationTypeType,
        "outputModelKmsKeyArn": str,
        "trainingMetrics": TrainingMetricsTypeDef,
        "validationMetrics": List[ValidatorMetricTypeDef],
        "vpcConfig": VpcConfigOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateModelCustomizationJobRequestRequestTypeDef = TypedDict(
    "CreateModelCustomizationJobRequestRequestTypeDef",
    {
        "jobName": str,
        "customModelName": str,
        "roleArn": str,
        "baseModelIdentifier": str,
        "trainingDataConfig": TrainingDataConfigTypeDef,
        "outputDataConfig": OutputDataConfigTypeDef,
        "hyperParameters": Mapping[str, str],
        "clientRequestToken": NotRequired[str],
        "customizationType": NotRequired[CustomizationTypeType],
        "customModelKmsKeyId": NotRequired[str],
        "jobTags": NotRequired[Sequence[TagTypeDef]],
        "customModelTags": NotRequired[Sequence[TagTypeDef]],
        "validationDataConfig": NotRequired[ValidationDataConfigTypeDef],
        "vpcConfig": NotRequired[VpcConfigTypeDef],
    },
)
GetModelInvocationLoggingConfigurationResponseTypeDef = TypedDict(
    "GetModelInvocationLoggingConfigurationResponseTypeDef",
    {
        "loggingConfig": LoggingConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutModelInvocationLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "PutModelInvocationLoggingConfigurationRequestRequestTypeDef",
    {
        "loggingConfig": LoggingConfigTypeDef,
    },
)
AutomatedEvaluationConfigOutputTypeDef = TypedDict(
    "AutomatedEvaluationConfigOutputTypeDef",
    {
        "datasetMetricConfigs": List[EvaluationDatasetMetricConfigOutputTypeDef],
    },
)
HumanEvaluationConfigOutputTypeDef = TypedDict(
    "HumanEvaluationConfigOutputTypeDef",
    {
        "datasetMetricConfigs": List[EvaluationDatasetMetricConfigOutputTypeDef],
        "humanWorkflowConfig": NotRequired[HumanWorkflowConfigTypeDef],
        "customMetrics": NotRequired[List[HumanEvaluationCustomMetricTypeDef]],
    },
)
EvaluationDatasetMetricConfigUnionTypeDef = Union[
    EvaluationDatasetMetricConfigTypeDef, EvaluationDatasetMetricConfigOutputTypeDef
]
HumanEvaluationConfigTypeDef = TypedDict(
    "HumanEvaluationConfigTypeDef",
    {
        "datasetMetricConfigs": Sequence[EvaluationDatasetMetricConfigTypeDef],
        "humanWorkflowConfig": NotRequired[HumanWorkflowConfigTypeDef],
        "customMetrics": NotRequired[Sequence[HumanEvaluationCustomMetricTypeDef]],
    },
)
ListModelInvocationJobsResponseTypeDef = TypedDict(
    "ListModelInvocationJobsResponseTypeDef",
    {
        "nextToken": str,
        "invocationJobSummaries": List[ModelInvocationJobSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EvaluationConfigOutputTypeDef = TypedDict(
    "EvaluationConfigOutputTypeDef",
    {
        "automated": NotRequired[AutomatedEvaluationConfigOutputTypeDef],
        "human": NotRequired[HumanEvaluationConfigOutputTypeDef],
    },
)
AutomatedEvaluationConfigTypeDef = TypedDict(
    "AutomatedEvaluationConfigTypeDef",
    {
        "datasetMetricConfigs": Sequence[EvaluationDatasetMetricConfigUnionTypeDef],
    },
)
HumanEvaluationConfigUnionTypeDef = Union[
    HumanEvaluationConfigTypeDef, HumanEvaluationConfigOutputTypeDef
]
GetEvaluationJobResponseTypeDef = TypedDict(
    "GetEvaluationJobResponseTypeDef",
    {
        "jobName": str,
        "status": EvaluationJobStatusType,
        "jobArn": str,
        "jobDescription": str,
        "roleArn": str,
        "customerEncryptionKeyId": str,
        "jobType": EvaluationJobTypeType,
        "evaluationConfig": EvaluationConfigOutputTypeDef,
        "inferenceConfig": EvaluationInferenceConfigOutputTypeDef,
        "outputDataConfig": EvaluationOutputDataConfigTypeDef,
        "creationTime": datetime,
        "lastModifiedTime": datetime,
        "failureMessages": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AutomatedEvaluationConfigUnionTypeDef = Union[
    AutomatedEvaluationConfigTypeDef, AutomatedEvaluationConfigOutputTypeDef
]
EvaluationConfigTypeDef = TypedDict(
    "EvaluationConfigTypeDef",
    {
        "automated": NotRequired[AutomatedEvaluationConfigUnionTypeDef],
        "human": NotRequired[HumanEvaluationConfigUnionTypeDef],
    },
)
CreateEvaluationJobRequestRequestTypeDef = TypedDict(
    "CreateEvaluationJobRequestRequestTypeDef",
    {
        "jobName": str,
        "roleArn": str,
        "evaluationConfig": EvaluationConfigTypeDef,
        "inferenceConfig": EvaluationInferenceConfigTypeDef,
        "outputDataConfig": EvaluationOutputDataConfigTypeDef,
        "jobDescription": NotRequired[str],
        "clientRequestToken": NotRequired[str],
        "customerEncryptionKeyId": NotRequired[str],
        "jobTags": NotRequired[Sequence[TagTypeDef]],
    },
)
