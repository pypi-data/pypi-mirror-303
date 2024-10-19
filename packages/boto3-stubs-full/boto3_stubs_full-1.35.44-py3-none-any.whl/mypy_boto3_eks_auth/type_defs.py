"""
Type annotations for eks-auth service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_eks_auth/type_defs/)

Usage::

    ```python
    from mypy_boto3_eks_auth.type_defs import AssumeRoleForPodIdentityRequestRequestTypeDef

    data: AssumeRoleForPodIdentityRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "AssumeRoleForPodIdentityRequestRequestTypeDef",
    "AssumedRoleUserTypeDef",
    "CredentialsTypeDef",
    "PodIdentityAssociationTypeDef",
    "ResponseMetadataTypeDef",
    "SubjectTypeDef",
    "AssumeRoleForPodIdentityResponseTypeDef",
)

AssumeRoleForPodIdentityRequestRequestTypeDef = TypedDict(
    "AssumeRoleForPodIdentityRequestRequestTypeDef",
    {
        "clusterName": str,
        "token": str,
    },
)
AssumedRoleUserTypeDef = TypedDict(
    "AssumedRoleUserTypeDef",
    {
        "arn": str,
        "assumeRoleId": str,
    },
)
CredentialsTypeDef = TypedDict(
    "CredentialsTypeDef",
    {
        "sessionToken": str,
        "secretAccessKey": str,
        "accessKeyId": str,
        "expiration": datetime,
    },
)
PodIdentityAssociationTypeDef = TypedDict(
    "PodIdentityAssociationTypeDef",
    {
        "associationArn": str,
        "associationId": str,
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
SubjectTypeDef = TypedDict(
    "SubjectTypeDef",
    {
        "namespace": str,
        "serviceAccount": str,
    },
)
AssumeRoleForPodIdentityResponseTypeDef = TypedDict(
    "AssumeRoleForPodIdentityResponseTypeDef",
    {
        "subject": SubjectTypeDef,
        "audience": str,
        "podIdentityAssociation": PodIdentityAssociationTypeDef,
        "assumedRoleUser": AssumedRoleUserTypeDef,
        "credentials": CredentialsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
