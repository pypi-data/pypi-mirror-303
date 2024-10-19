"""
Type annotations for bedrock-runtime service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_runtime/type_defs/)

Usage::

    ```python
    from mypy_boto3_bedrock_runtime.type_defs import GuardrailOutputContentTypeDef

    data: GuardrailOutputContentTypeDef = ...
    ```
"""

import sys
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.eventstream import EventStream
from botocore.response import StreamingBody

from .literals import (
    ConversationRoleType,
    DocumentFormatType,
    GuardrailActionType,
    GuardrailContentFilterConfidenceType,
    GuardrailContentFilterStrengthType,
    GuardrailContentFilterTypeType,
    GuardrailContentQualifierType,
    GuardrailContentSourceType,
    GuardrailContextualGroundingFilterTypeType,
    GuardrailContextualGroundingPolicyActionType,
    GuardrailConverseContentQualifierType,
    GuardrailPiiEntityTypeType,
    GuardrailSensitiveInformationPolicyActionType,
    GuardrailStreamProcessingModeType,
    GuardrailTraceType,
    ImageFormatType,
    StopReasonType,
    ToolResultStatusType,
    TraceType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "GuardrailOutputContentTypeDef",
    "GuardrailUsageTypeDef",
    "ResponseMetadataTypeDef",
    "BlobTypeDef",
    "ToolUseBlockDeltaTypeDef",
    "ToolUseBlockOutputTypeDef",
    "ToolUseBlockStartTypeDef",
    "ContentBlockStopEventTypeDef",
    "ConverseMetricsTypeDef",
    "GuardrailConfigurationTypeDef",
    "InferenceConfigurationTypeDef",
    "TokenUsageTypeDef",
    "ConverseStreamMetricsTypeDef",
    "InternalServerExceptionTypeDef",
    "MessageStartEventTypeDef",
    "MessageStopEventTypeDef",
    "ModelStreamErrorExceptionTypeDef",
    "ServiceUnavailableExceptionTypeDef",
    "ThrottlingExceptionTypeDef",
    "ValidationExceptionTypeDef",
    "GuardrailStreamConfigurationTypeDef",
    "DocumentSourceOutputTypeDef",
    "GuardrailTextBlockTypeDef",
    "GuardrailContentFilterTypeDef",
    "GuardrailContextualGroundingFilterTypeDef",
    "GuardrailConverseTextBlockOutputTypeDef",
    "GuardrailConverseTextBlockTypeDef",
    "GuardrailTextCharactersCoverageTypeDef",
    "GuardrailCustomWordTypeDef",
    "GuardrailManagedWordTypeDef",
    "GuardrailPiiEntityFilterTypeDef",
    "GuardrailRegexFilterTypeDef",
    "GuardrailTopicTypeDef",
    "ImageSourceOutputTypeDef",
    "ModelTimeoutExceptionTypeDef",
    "PayloadPartTypeDef",
    "SpecificToolChoiceTypeDef",
    "ToolInputSchemaTypeDef",
    "ToolUseBlockTypeDef",
    "InvokeModelResponseTypeDef",
    "DocumentSourceTypeDef",
    "ImageSourceTypeDef",
    "InvokeModelRequestRequestTypeDef",
    "InvokeModelWithResponseStreamRequestRequestTypeDef",
    "ContentBlockDeltaTypeDef",
    "ContentBlockStartTypeDef",
    "DocumentBlockOutputTypeDef",
    "GuardrailContentBlockTypeDef",
    "GuardrailContentPolicyAssessmentTypeDef",
    "GuardrailContextualGroundingPolicyAssessmentTypeDef",
    "GuardrailConverseContentBlockOutputTypeDef",
    "GuardrailConverseTextBlockUnionTypeDef",
    "GuardrailCoverageTypeDef",
    "GuardrailWordPolicyAssessmentTypeDef",
    "GuardrailSensitiveInformationPolicyAssessmentTypeDef",
    "GuardrailTopicPolicyAssessmentTypeDef",
    "ImageBlockOutputTypeDef",
    "ResponseStreamTypeDef",
    "ToolChoiceTypeDef",
    "ToolSpecificationTypeDef",
    "ToolUseBlockUnionTypeDef",
    "DocumentSourceUnionTypeDef",
    "ImageSourceUnionTypeDef",
    "ContentBlockDeltaEventTypeDef",
    "ContentBlockStartEventTypeDef",
    "ApplyGuardrailRequestRequestTypeDef",
    "GuardrailConverseContentBlockTypeDef",
    "GuardrailInvocationMetricsTypeDef",
    "ToolResultContentBlockOutputTypeDef",
    "InvokeModelWithResponseStreamResponseTypeDef",
    "ToolTypeDef",
    "DocumentBlockTypeDef",
    "ImageBlockTypeDef",
    "GuardrailConverseContentBlockUnionTypeDef",
    "GuardrailAssessmentTypeDef",
    "ToolResultBlockOutputTypeDef",
    "ToolConfigurationTypeDef",
    "DocumentBlockUnionTypeDef",
    "ImageBlockUnionTypeDef",
    "SystemContentBlockTypeDef",
    "ApplyGuardrailResponseTypeDef",
    "GuardrailTraceAssessmentTypeDef",
    "ContentBlockOutputTypeDef",
    "ToolResultContentBlockTypeDef",
    "ConverseStreamTraceTypeDef",
    "ConverseTraceTypeDef",
    "MessageOutputTypeDef",
    "ToolResultContentBlockUnionTypeDef",
    "ConverseStreamMetadataEventTypeDef",
    "ConverseOutputTypeDef",
    "ToolResultBlockTypeDef",
    "ConverseStreamOutputTypeDef",
    "ConverseResponseTypeDef",
    "ToolResultBlockUnionTypeDef",
    "ConverseStreamResponseTypeDef",
    "ContentBlockTypeDef",
    "ContentBlockUnionTypeDef",
    "MessageTypeDef",
    "ConverseStreamRequestRequestTypeDef",
    "MessageUnionTypeDef",
    "ConverseRequestRequestTypeDef",
)

GuardrailOutputContentTypeDef = TypedDict(
    "GuardrailOutputContentTypeDef",
    {
        "text": NotRequired[str],
    },
)
GuardrailUsageTypeDef = TypedDict(
    "GuardrailUsageTypeDef",
    {
        "topicPolicyUnits": int,
        "contentPolicyUnits": int,
        "wordPolicyUnits": int,
        "sensitiveInformationPolicyUnits": int,
        "sensitiveInformationPolicyFreeUnits": int,
        "contextualGroundingPolicyUnits": int,
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
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
ToolUseBlockDeltaTypeDef = TypedDict(
    "ToolUseBlockDeltaTypeDef",
    {
        "input": str,
    },
)
ToolUseBlockOutputTypeDef = TypedDict(
    "ToolUseBlockOutputTypeDef",
    {
        "toolUseId": str,
        "name": str,
        "input": Dict[str, Any],
    },
)
ToolUseBlockStartTypeDef = TypedDict(
    "ToolUseBlockStartTypeDef",
    {
        "toolUseId": str,
        "name": str,
    },
)
ContentBlockStopEventTypeDef = TypedDict(
    "ContentBlockStopEventTypeDef",
    {
        "contentBlockIndex": int,
    },
)
ConverseMetricsTypeDef = TypedDict(
    "ConverseMetricsTypeDef",
    {
        "latencyMs": int,
    },
)
GuardrailConfigurationTypeDef = TypedDict(
    "GuardrailConfigurationTypeDef",
    {
        "guardrailIdentifier": str,
        "guardrailVersion": str,
        "trace": NotRequired[GuardrailTraceType],
    },
)
InferenceConfigurationTypeDef = TypedDict(
    "InferenceConfigurationTypeDef",
    {
        "maxTokens": NotRequired[int],
        "temperature": NotRequired[float],
        "topP": NotRequired[float],
        "stopSequences": NotRequired[Sequence[str]],
    },
)
TokenUsageTypeDef = TypedDict(
    "TokenUsageTypeDef",
    {
        "inputTokens": int,
        "outputTokens": int,
        "totalTokens": int,
    },
)
ConverseStreamMetricsTypeDef = TypedDict(
    "ConverseStreamMetricsTypeDef",
    {
        "latencyMs": int,
    },
)
InternalServerExceptionTypeDef = TypedDict(
    "InternalServerExceptionTypeDef",
    {
        "message": NotRequired[str],
    },
)
MessageStartEventTypeDef = TypedDict(
    "MessageStartEventTypeDef",
    {
        "role": ConversationRoleType,
    },
)
MessageStopEventTypeDef = TypedDict(
    "MessageStopEventTypeDef",
    {
        "stopReason": StopReasonType,
        "additionalModelResponseFields": NotRequired[Dict[str, Any]],
    },
)
ModelStreamErrorExceptionTypeDef = TypedDict(
    "ModelStreamErrorExceptionTypeDef",
    {
        "message": NotRequired[str],
        "originalStatusCode": NotRequired[int],
        "originalMessage": NotRequired[str],
    },
)
ServiceUnavailableExceptionTypeDef = TypedDict(
    "ServiceUnavailableExceptionTypeDef",
    {
        "message": NotRequired[str],
    },
)
ThrottlingExceptionTypeDef = TypedDict(
    "ThrottlingExceptionTypeDef",
    {
        "message": NotRequired[str],
    },
)
ValidationExceptionTypeDef = TypedDict(
    "ValidationExceptionTypeDef",
    {
        "message": NotRequired[str],
    },
)
GuardrailStreamConfigurationTypeDef = TypedDict(
    "GuardrailStreamConfigurationTypeDef",
    {
        "guardrailIdentifier": str,
        "guardrailVersion": str,
        "trace": NotRequired[GuardrailTraceType],
        "streamProcessingMode": NotRequired[GuardrailStreamProcessingModeType],
    },
)
DocumentSourceOutputTypeDef = TypedDict(
    "DocumentSourceOutputTypeDef",
    {
        "bytes": NotRequired[bytes],
    },
)
GuardrailTextBlockTypeDef = TypedDict(
    "GuardrailTextBlockTypeDef",
    {
        "text": str,
        "qualifiers": NotRequired[Sequence[GuardrailContentQualifierType]],
    },
)
GuardrailContentFilterTypeDef = TypedDict(
    "GuardrailContentFilterTypeDef",
    {
        "type": GuardrailContentFilterTypeType,
        "confidence": GuardrailContentFilterConfidenceType,
        "action": Literal["BLOCKED"],
        "filterStrength": NotRequired[GuardrailContentFilterStrengthType],
    },
)
GuardrailContextualGroundingFilterTypeDef = TypedDict(
    "GuardrailContextualGroundingFilterTypeDef",
    {
        "type": GuardrailContextualGroundingFilterTypeType,
        "threshold": float,
        "score": float,
        "action": GuardrailContextualGroundingPolicyActionType,
    },
)
GuardrailConverseTextBlockOutputTypeDef = TypedDict(
    "GuardrailConverseTextBlockOutputTypeDef",
    {
        "text": str,
        "qualifiers": NotRequired[List[GuardrailConverseContentQualifierType]],
    },
)
GuardrailConverseTextBlockTypeDef = TypedDict(
    "GuardrailConverseTextBlockTypeDef",
    {
        "text": str,
        "qualifiers": NotRequired[Sequence[GuardrailConverseContentQualifierType]],
    },
)
GuardrailTextCharactersCoverageTypeDef = TypedDict(
    "GuardrailTextCharactersCoverageTypeDef",
    {
        "guarded": NotRequired[int],
        "total": NotRequired[int],
    },
)
GuardrailCustomWordTypeDef = TypedDict(
    "GuardrailCustomWordTypeDef",
    {
        "match": str,
        "action": Literal["BLOCKED"],
    },
)
GuardrailManagedWordTypeDef = TypedDict(
    "GuardrailManagedWordTypeDef",
    {
        "match": str,
        "type": Literal["PROFANITY"],
        "action": Literal["BLOCKED"],
    },
)
GuardrailPiiEntityFilterTypeDef = TypedDict(
    "GuardrailPiiEntityFilterTypeDef",
    {
        "match": str,
        "type": GuardrailPiiEntityTypeType,
        "action": GuardrailSensitiveInformationPolicyActionType,
    },
)
GuardrailRegexFilterTypeDef = TypedDict(
    "GuardrailRegexFilterTypeDef",
    {
        "action": GuardrailSensitiveInformationPolicyActionType,
        "name": NotRequired[str],
        "match": NotRequired[str],
        "regex": NotRequired[str],
    },
)
GuardrailTopicTypeDef = TypedDict(
    "GuardrailTopicTypeDef",
    {
        "name": str,
        "type": Literal["DENY"],
        "action": Literal["BLOCKED"],
    },
)
ImageSourceOutputTypeDef = TypedDict(
    "ImageSourceOutputTypeDef",
    {
        "bytes": NotRequired[bytes],
    },
)
ModelTimeoutExceptionTypeDef = TypedDict(
    "ModelTimeoutExceptionTypeDef",
    {
        "message": NotRequired[str],
    },
)
PayloadPartTypeDef = TypedDict(
    "PayloadPartTypeDef",
    {
        "bytes": NotRequired[bytes],
    },
)
SpecificToolChoiceTypeDef = TypedDict(
    "SpecificToolChoiceTypeDef",
    {
        "name": str,
    },
)
ToolInputSchemaTypeDef = TypedDict(
    "ToolInputSchemaTypeDef",
    {
        "json": NotRequired[Mapping[str, Any]],
    },
)
ToolUseBlockTypeDef = TypedDict(
    "ToolUseBlockTypeDef",
    {
        "toolUseId": str,
        "name": str,
        "input": Mapping[str, Any],
    },
)
InvokeModelResponseTypeDef = TypedDict(
    "InvokeModelResponseTypeDef",
    {
        "body": StreamingBody,
        "contentType": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DocumentSourceTypeDef = TypedDict(
    "DocumentSourceTypeDef",
    {
        "bytes": NotRequired[BlobTypeDef],
    },
)
ImageSourceTypeDef = TypedDict(
    "ImageSourceTypeDef",
    {
        "bytes": NotRequired[BlobTypeDef],
    },
)
InvokeModelRequestRequestTypeDef = TypedDict(
    "InvokeModelRequestRequestTypeDef",
    {
        "body": BlobTypeDef,
        "modelId": str,
        "contentType": NotRequired[str],
        "accept": NotRequired[str],
        "trace": NotRequired[TraceType],
        "guardrailIdentifier": NotRequired[str],
        "guardrailVersion": NotRequired[str],
    },
)
InvokeModelWithResponseStreamRequestRequestTypeDef = TypedDict(
    "InvokeModelWithResponseStreamRequestRequestTypeDef",
    {
        "body": BlobTypeDef,
        "modelId": str,
        "contentType": NotRequired[str],
        "accept": NotRequired[str],
        "trace": NotRequired[TraceType],
        "guardrailIdentifier": NotRequired[str],
        "guardrailVersion": NotRequired[str],
    },
)
ContentBlockDeltaTypeDef = TypedDict(
    "ContentBlockDeltaTypeDef",
    {
        "text": NotRequired[str],
        "toolUse": NotRequired[ToolUseBlockDeltaTypeDef],
    },
)
ContentBlockStartTypeDef = TypedDict(
    "ContentBlockStartTypeDef",
    {
        "toolUse": NotRequired[ToolUseBlockStartTypeDef],
    },
)
DocumentBlockOutputTypeDef = TypedDict(
    "DocumentBlockOutputTypeDef",
    {
        "format": DocumentFormatType,
        "name": str,
        "source": DocumentSourceOutputTypeDef,
    },
)
GuardrailContentBlockTypeDef = TypedDict(
    "GuardrailContentBlockTypeDef",
    {
        "text": NotRequired[GuardrailTextBlockTypeDef],
    },
)
GuardrailContentPolicyAssessmentTypeDef = TypedDict(
    "GuardrailContentPolicyAssessmentTypeDef",
    {
        "filters": List[GuardrailContentFilterTypeDef],
    },
)
GuardrailContextualGroundingPolicyAssessmentTypeDef = TypedDict(
    "GuardrailContextualGroundingPolicyAssessmentTypeDef",
    {
        "filters": NotRequired[List[GuardrailContextualGroundingFilterTypeDef]],
    },
)
GuardrailConverseContentBlockOutputTypeDef = TypedDict(
    "GuardrailConverseContentBlockOutputTypeDef",
    {
        "text": NotRequired[GuardrailConverseTextBlockOutputTypeDef],
    },
)
GuardrailConverseTextBlockUnionTypeDef = Union[
    GuardrailConverseTextBlockTypeDef, GuardrailConverseTextBlockOutputTypeDef
]
GuardrailCoverageTypeDef = TypedDict(
    "GuardrailCoverageTypeDef",
    {
        "textCharacters": NotRequired[GuardrailTextCharactersCoverageTypeDef],
    },
)
GuardrailWordPolicyAssessmentTypeDef = TypedDict(
    "GuardrailWordPolicyAssessmentTypeDef",
    {
        "customWords": List[GuardrailCustomWordTypeDef],
        "managedWordLists": List[GuardrailManagedWordTypeDef],
    },
)
GuardrailSensitiveInformationPolicyAssessmentTypeDef = TypedDict(
    "GuardrailSensitiveInformationPolicyAssessmentTypeDef",
    {
        "piiEntities": List[GuardrailPiiEntityFilterTypeDef],
        "regexes": List[GuardrailRegexFilterTypeDef],
    },
)
GuardrailTopicPolicyAssessmentTypeDef = TypedDict(
    "GuardrailTopicPolicyAssessmentTypeDef",
    {
        "topics": List[GuardrailTopicTypeDef],
    },
)
ImageBlockOutputTypeDef = TypedDict(
    "ImageBlockOutputTypeDef",
    {
        "format": ImageFormatType,
        "source": ImageSourceOutputTypeDef,
    },
)
ResponseStreamTypeDef = TypedDict(
    "ResponseStreamTypeDef",
    {
        "chunk": NotRequired[PayloadPartTypeDef],
        "internalServerException": NotRequired[InternalServerExceptionTypeDef],
        "modelStreamErrorException": NotRequired[ModelStreamErrorExceptionTypeDef],
        "validationException": NotRequired[ValidationExceptionTypeDef],
        "throttlingException": NotRequired[ThrottlingExceptionTypeDef],
        "modelTimeoutException": NotRequired[ModelTimeoutExceptionTypeDef],
        "serviceUnavailableException": NotRequired[ServiceUnavailableExceptionTypeDef],
    },
)
ToolChoiceTypeDef = TypedDict(
    "ToolChoiceTypeDef",
    {
        "auto": NotRequired[Mapping[str, Any]],
        "any": NotRequired[Mapping[str, Any]],
        "tool": NotRequired[SpecificToolChoiceTypeDef],
    },
)
ToolSpecificationTypeDef = TypedDict(
    "ToolSpecificationTypeDef",
    {
        "name": str,
        "inputSchema": ToolInputSchemaTypeDef,
        "description": NotRequired[str],
    },
)
ToolUseBlockUnionTypeDef = Union[ToolUseBlockTypeDef, ToolUseBlockOutputTypeDef]
DocumentSourceUnionTypeDef = Union[DocumentSourceTypeDef, DocumentSourceOutputTypeDef]
ImageSourceUnionTypeDef = Union[ImageSourceTypeDef, ImageSourceOutputTypeDef]
ContentBlockDeltaEventTypeDef = TypedDict(
    "ContentBlockDeltaEventTypeDef",
    {
        "delta": ContentBlockDeltaTypeDef,
        "contentBlockIndex": int,
    },
)
ContentBlockStartEventTypeDef = TypedDict(
    "ContentBlockStartEventTypeDef",
    {
        "start": ContentBlockStartTypeDef,
        "contentBlockIndex": int,
    },
)
ApplyGuardrailRequestRequestTypeDef = TypedDict(
    "ApplyGuardrailRequestRequestTypeDef",
    {
        "guardrailIdentifier": str,
        "guardrailVersion": str,
        "source": GuardrailContentSourceType,
        "content": Sequence[GuardrailContentBlockTypeDef],
    },
)
GuardrailConverseContentBlockTypeDef = TypedDict(
    "GuardrailConverseContentBlockTypeDef",
    {
        "text": NotRequired[GuardrailConverseTextBlockUnionTypeDef],
    },
)
GuardrailInvocationMetricsTypeDef = TypedDict(
    "GuardrailInvocationMetricsTypeDef",
    {
        "guardrailProcessingLatency": NotRequired[int],
        "usage": NotRequired[GuardrailUsageTypeDef],
        "guardrailCoverage": NotRequired[GuardrailCoverageTypeDef],
    },
)
ToolResultContentBlockOutputTypeDef = TypedDict(
    "ToolResultContentBlockOutputTypeDef",
    {
        "json": NotRequired[Dict[str, Any]],
        "text": NotRequired[str],
        "image": NotRequired[ImageBlockOutputTypeDef],
        "document": NotRequired[DocumentBlockOutputTypeDef],
    },
)
InvokeModelWithResponseStreamResponseTypeDef = TypedDict(
    "InvokeModelWithResponseStreamResponseTypeDef",
    {
        "body": "EventStream[ResponseStreamTypeDef]",
        "contentType": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ToolTypeDef = TypedDict(
    "ToolTypeDef",
    {
        "toolSpec": NotRequired[ToolSpecificationTypeDef],
    },
)
DocumentBlockTypeDef = TypedDict(
    "DocumentBlockTypeDef",
    {
        "format": DocumentFormatType,
        "name": str,
        "source": DocumentSourceUnionTypeDef,
    },
)
ImageBlockTypeDef = TypedDict(
    "ImageBlockTypeDef",
    {
        "format": ImageFormatType,
        "source": ImageSourceUnionTypeDef,
    },
)
GuardrailConverseContentBlockUnionTypeDef = Union[
    GuardrailConverseContentBlockTypeDef, GuardrailConverseContentBlockOutputTypeDef
]
GuardrailAssessmentTypeDef = TypedDict(
    "GuardrailAssessmentTypeDef",
    {
        "topicPolicy": NotRequired[GuardrailTopicPolicyAssessmentTypeDef],
        "contentPolicy": NotRequired[GuardrailContentPolicyAssessmentTypeDef],
        "wordPolicy": NotRequired[GuardrailWordPolicyAssessmentTypeDef],
        "sensitiveInformationPolicy": NotRequired[
            GuardrailSensitiveInformationPolicyAssessmentTypeDef
        ],
        "contextualGroundingPolicy": NotRequired[
            GuardrailContextualGroundingPolicyAssessmentTypeDef
        ],
        "invocationMetrics": NotRequired[GuardrailInvocationMetricsTypeDef],
    },
)
ToolResultBlockOutputTypeDef = TypedDict(
    "ToolResultBlockOutputTypeDef",
    {
        "toolUseId": str,
        "content": List[ToolResultContentBlockOutputTypeDef],
        "status": NotRequired[ToolResultStatusType],
    },
)
ToolConfigurationTypeDef = TypedDict(
    "ToolConfigurationTypeDef",
    {
        "tools": Sequence[ToolTypeDef],
        "toolChoice": NotRequired[ToolChoiceTypeDef],
    },
)
DocumentBlockUnionTypeDef = Union[DocumentBlockTypeDef, DocumentBlockOutputTypeDef]
ImageBlockUnionTypeDef = Union[ImageBlockTypeDef, ImageBlockOutputTypeDef]
SystemContentBlockTypeDef = TypedDict(
    "SystemContentBlockTypeDef",
    {
        "text": NotRequired[str],
        "guardContent": NotRequired[GuardrailConverseContentBlockUnionTypeDef],
    },
)
ApplyGuardrailResponseTypeDef = TypedDict(
    "ApplyGuardrailResponseTypeDef",
    {
        "usage": GuardrailUsageTypeDef,
        "action": GuardrailActionType,
        "outputs": List[GuardrailOutputContentTypeDef],
        "assessments": List[GuardrailAssessmentTypeDef],
        "guardrailCoverage": GuardrailCoverageTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GuardrailTraceAssessmentTypeDef = TypedDict(
    "GuardrailTraceAssessmentTypeDef",
    {
        "modelOutput": NotRequired[List[str]],
        "inputAssessment": NotRequired[Dict[str, GuardrailAssessmentTypeDef]],
        "outputAssessments": NotRequired[Dict[str, List[GuardrailAssessmentTypeDef]]],
    },
)
ContentBlockOutputTypeDef = TypedDict(
    "ContentBlockOutputTypeDef",
    {
        "text": NotRequired[str],
        "image": NotRequired[ImageBlockOutputTypeDef],
        "document": NotRequired[DocumentBlockOutputTypeDef],
        "toolUse": NotRequired[ToolUseBlockOutputTypeDef],
        "toolResult": NotRequired[ToolResultBlockOutputTypeDef],
        "guardContent": NotRequired[GuardrailConverseContentBlockOutputTypeDef],
    },
)
ToolResultContentBlockTypeDef = TypedDict(
    "ToolResultContentBlockTypeDef",
    {
        "json": NotRequired[Mapping[str, Any]],
        "text": NotRequired[str],
        "image": NotRequired[ImageBlockUnionTypeDef],
        "document": NotRequired[DocumentBlockUnionTypeDef],
    },
)
ConverseStreamTraceTypeDef = TypedDict(
    "ConverseStreamTraceTypeDef",
    {
        "guardrail": NotRequired[GuardrailTraceAssessmentTypeDef],
    },
)
ConverseTraceTypeDef = TypedDict(
    "ConverseTraceTypeDef",
    {
        "guardrail": NotRequired[GuardrailTraceAssessmentTypeDef],
    },
)
MessageOutputTypeDef = TypedDict(
    "MessageOutputTypeDef",
    {
        "role": ConversationRoleType,
        "content": List[ContentBlockOutputTypeDef],
    },
)
ToolResultContentBlockUnionTypeDef = Union[
    ToolResultContentBlockTypeDef, ToolResultContentBlockOutputTypeDef
]
ConverseStreamMetadataEventTypeDef = TypedDict(
    "ConverseStreamMetadataEventTypeDef",
    {
        "usage": TokenUsageTypeDef,
        "metrics": ConverseStreamMetricsTypeDef,
        "trace": NotRequired[ConverseStreamTraceTypeDef],
    },
)
ConverseOutputTypeDef = TypedDict(
    "ConverseOutputTypeDef",
    {
        "message": NotRequired[MessageOutputTypeDef],
    },
)
ToolResultBlockTypeDef = TypedDict(
    "ToolResultBlockTypeDef",
    {
        "toolUseId": str,
        "content": Sequence[ToolResultContentBlockUnionTypeDef],
        "status": NotRequired[ToolResultStatusType],
    },
)
ConverseStreamOutputTypeDef = TypedDict(
    "ConverseStreamOutputTypeDef",
    {
        "messageStart": NotRequired[MessageStartEventTypeDef],
        "contentBlockStart": NotRequired[ContentBlockStartEventTypeDef],
        "contentBlockDelta": NotRequired[ContentBlockDeltaEventTypeDef],
        "contentBlockStop": NotRequired[ContentBlockStopEventTypeDef],
        "messageStop": NotRequired[MessageStopEventTypeDef],
        "metadata": NotRequired[ConverseStreamMetadataEventTypeDef],
        "internalServerException": NotRequired[InternalServerExceptionTypeDef],
        "modelStreamErrorException": NotRequired[ModelStreamErrorExceptionTypeDef],
        "validationException": NotRequired[ValidationExceptionTypeDef],
        "throttlingException": NotRequired[ThrottlingExceptionTypeDef],
        "serviceUnavailableException": NotRequired[ServiceUnavailableExceptionTypeDef],
    },
)
ConverseResponseTypeDef = TypedDict(
    "ConverseResponseTypeDef",
    {
        "output": ConverseOutputTypeDef,
        "stopReason": StopReasonType,
        "usage": TokenUsageTypeDef,
        "metrics": ConverseMetricsTypeDef,
        "additionalModelResponseFields": Dict[str, Any],
        "trace": ConverseTraceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ToolResultBlockUnionTypeDef = Union[ToolResultBlockTypeDef, ToolResultBlockOutputTypeDef]
ConverseStreamResponseTypeDef = TypedDict(
    "ConverseStreamResponseTypeDef",
    {
        "stream": "EventStream[ConverseStreamOutputTypeDef]",
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ContentBlockTypeDef = TypedDict(
    "ContentBlockTypeDef",
    {
        "text": NotRequired[str],
        "image": NotRequired[ImageBlockUnionTypeDef],
        "document": NotRequired[DocumentBlockUnionTypeDef],
        "toolUse": NotRequired[ToolUseBlockUnionTypeDef],
        "toolResult": NotRequired[ToolResultBlockUnionTypeDef],
        "guardContent": NotRequired[GuardrailConverseContentBlockUnionTypeDef],
    },
)
ContentBlockUnionTypeDef = Union[ContentBlockTypeDef, ContentBlockOutputTypeDef]
MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "role": ConversationRoleType,
        "content": Sequence[ContentBlockUnionTypeDef],
    },
)
ConverseStreamRequestRequestTypeDef = TypedDict(
    "ConverseStreamRequestRequestTypeDef",
    {
        "modelId": str,
        "messages": Sequence[MessageTypeDef],
        "system": NotRequired[Sequence[SystemContentBlockTypeDef]],
        "inferenceConfig": NotRequired[InferenceConfigurationTypeDef],
        "toolConfig": NotRequired[ToolConfigurationTypeDef],
        "guardrailConfig": NotRequired[GuardrailStreamConfigurationTypeDef],
        "additionalModelRequestFields": NotRequired[Mapping[str, Any]],
        "additionalModelResponseFieldPaths": NotRequired[Sequence[str]],
    },
)
MessageUnionTypeDef = Union[MessageTypeDef, MessageOutputTypeDef]
ConverseRequestRequestTypeDef = TypedDict(
    "ConverseRequestRequestTypeDef",
    {
        "modelId": str,
        "messages": Sequence[MessageUnionTypeDef],
        "system": NotRequired[Sequence[SystemContentBlockTypeDef]],
        "inferenceConfig": NotRequired[InferenceConfigurationTypeDef],
        "toolConfig": NotRequired[ToolConfigurationTypeDef],
        "guardrailConfig": NotRequired[GuardrailConfigurationTypeDef],
        "additionalModelRequestFields": NotRequired[Mapping[str, Any]],
        "additionalModelResponseFieldPaths": NotRequired[Sequence[str]],
    },
)
