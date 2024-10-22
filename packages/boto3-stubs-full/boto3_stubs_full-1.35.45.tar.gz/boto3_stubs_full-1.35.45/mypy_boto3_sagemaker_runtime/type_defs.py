"""
Type annotations for sagemaker-runtime service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_runtime/type_defs/)

Usage::

    ```python
    from mypy_boto3_sagemaker_runtime.type_defs import BlobTypeDef

    data: BlobTypeDef = ...
    ```
"""

import sys
from typing import IO, Any, Dict, Union

from botocore.eventstream import EventStream
from botocore.response import StreamingBody

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "BlobTypeDef",
    "InternalStreamFailureTypeDef",
    "InvokeEndpointAsyncInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "ModelStreamErrorTypeDef",
    "PayloadPartTypeDef",
    "InvokeEndpointInputRequestTypeDef",
    "InvokeEndpointWithResponseStreamInputRequestTypeDef",
    "InvokeEndpointAsyncOutputTypeDef",
    "InvokeEndpointOutputTypeDef",
    "ResponseStreamTypeDef",
    "InvokeEndpointWithResponseStreamOutputTypeDef",
)

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
InternalStreamFailureTypeDef = TypedDict(
    "InternalStreamFailureTypeDef",
    {
        "Message": NotRequired[str],
    },
)
InvokeEndpointAsyncInputRequestTypeDef = TypedDict(
    "InvokeEndpointAsyncInputRequestTypeDef",
    {
        "EndpointName": str,
        "InputLocation": str,
        "ContentType": NotRequired[str],
        "Accept": NotRequired[str],
        "CustomAttributes": NotRequired[str],
        "InferenceId": NotRequired[str],
        "RequestTTLSeconds": NotRequired[int],
        "InvocationTimeoutSeconds": NotRequired[int],
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
ModelStreamErrorTypeDef = TypedDict(
    "ModelStreamErrorTypeDef",
    {
        "Message": NotRequired[str],
        "ErrorCode": NotRequired[str],
    },
)
PayloadPartTypeDef = TypedDict(
    "PayloadPartTypeDef",
    {
        "Bytes": NotRequired[bytes],
    },
)
InvokeEndpointInputRequestTypeDef = TypedDict(
    "InvokeEndpointInputRequestTypeDef",
    {
        "EndpointName": str,
        "Body": BlobTypeDef,
        "ContentType": NotRequired[str],
        "Accept": NotRequired[str],
        "CustomAttributes": NotRequired[str],
        "TargetModel": NotRequired[str],
        "TargetVariant": NotRequired[str],
        "TargetContainerHostname": NotRequired[str],
        "InferenceId": NotRequired[str],
        "EnableExplanations": NotRequired[str],
        "InferenceComponentName": NotRequired[str],
        "SessionId": NotRequired[str],
    },
)
InvokeEndpointWithResponseStreamInputRequestTypeDef = TypedDict(
    "InvokeEndpointWithResponseStreamInputRequestTypeDef",
    {
        "EndpointName": str,
        "Body": BlobTypeDef,
        "ContentType": NotRequired[str],
        "Accept": NotRequired[str],
        "CustomAttributes": NotRequired[str],
        "TargetVariant": NotRequired[str],
        "TargetContainerHostname": NotRequired[str],
        "InferenceId": NotRequired[str],
        "InferenceComponentName": NotRequired[str],
        "SessionId": NotRequired[str],
    },
)
InvokeEndpointAsyncOutputTypeDef = TypedDict(
    "InvokeEndpointAsyncOutputTypeDef",
    {
        "InferenceId": str,
        "OutputLocation": str,
        "FailureLocation": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InvokeEndpointOutputTypeDef = TypedDict(
    "InvokeEndpointOutputTypeDef",
    {
        "Body": StreamingBody,
        "ContentType": str,
        "InvokedProductionVariant": str,
        "CustomAttributes": str,
        "NewSessionId": str,
        "ClosedSessionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResponseStreamTypeDef = TypedDict(
    "ResponseStreamTypeDef",
    {
        "PayloadPart": NotRequired[PayloadPartTypeDef],
        "ModelStreamError": NotRequired[ModelStreamErrorTypeDef],
        "InternalStreamFailure": NotRequired[InternalStreamFailureTypeDef],
    },
)
InvokeEndpointWithResponseStreamOutputTypeDef = TypedDict(
    "InvokeEndpointWithResponseStreamOutputTypeDef",
    {
        "Body": "EventStream[ResponseStreamTypeDef]",
        "ContentType": str,
        "InvokedProductionVariant": str,
        "CustomAttributes": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
