"""
Type annotations for ec2-instance-connect service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2_instance_connect/type_defs/)

Usage::

    ```python
    from mypy_boto3_ec2_instance_connect.type_defs import ResponseMetadataTypeDef

    data: ResponseMetadataTypeDef = ...
    ```
"""

import sys
from typing import Dict

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict


__all__ = (
    "ResponseMetadataTypeDef",
    "SendSSHPublicKeyRequestRequestTypeDef",
    "SendSerialConsoleSSHPublicKeyRequestRequestTypeDef",
    "SendSSHPublicKeyResponseTypeDef",
    "SendSerialConsoleSSHPublicKeyResponseTypeDef",
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
SendSSHPublicKeyRequestRequestTypeDef = TypedDict(
    "SendSSHPublicKeyRequestRequestTypeDef",
    {
        "InstanceId": str,
        "InstanceOSUser": str,
        "SSHPublicKey": str,
        "AvailabilityZone": NotRequired[str],
    },
)
SendSerialConsoleSSHPublicKeyRequestRequestTypeDef = TypedDict(
    "SendSerialConsoleSSHPublicKeyRequestRequestTypeDef",
    {
        "InstanceId": str,
        "SSHPublicKey": str,
        "SerialPort": NotRequired[int],
    },
)
SendSSHPublicKeyResponseTypeDef = TypedDict(
    "SendSSHPublicKeyResponseTypeDef",
    {
        "RequestId": str,
        "Success": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendSerialConsoleSSHPublicKeyResponseTypeDef = TypedDict(
    "SendSerialConsoleSSHPublicKeyResponseTypeDef",
    {
        "RequestId": str,
        "Success": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
