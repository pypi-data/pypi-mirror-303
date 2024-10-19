"""
Type annotations for marketplace-deployment service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_deployment/type_defs/)

Usage::

    ```python
    from mypy_boto3_marketplace_deployment.type_defs import DeploymentParameterInputTypeDef

    data: DeploymentParameterInputTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, Mapping, Sequence, Union

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "DeploymentParameterInputTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "TimestampTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PutDeploymentParameterResponseTypeDef",
    "PutDeploymentParameterRequestRequestTypeDef",
)

DeploymentParameterInputTypeDef = TypedDict(
    "DeploymentParameterInputTypeDef",
    {
        "name": str,
        "secretString": str,
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
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
TimestampTypeDef = Union[datetime, str]
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": NotRequired[Mapping[str, str]],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutDeploymentParameterResponseTypeDef = TypedDict(
    "PutDeploymentParameterResponseTypeDef",
    {
        "agreementId": str,
        "deploymentParameterId": str,
        "resourceArn": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutDeploymentParameterRequestRequestTypeDef = TypedDict(
    "PutDeploymentParameterRequestRequestTypeDef",
    {
        "agreementId": str,
        "catalog": str,
        "deploymentParameter": DeploymentParameterInputTypeDef,
        "productId": str,
        "clientToken": NotRequired[str],
        "expirationDate": NotRequired[TimestampTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
