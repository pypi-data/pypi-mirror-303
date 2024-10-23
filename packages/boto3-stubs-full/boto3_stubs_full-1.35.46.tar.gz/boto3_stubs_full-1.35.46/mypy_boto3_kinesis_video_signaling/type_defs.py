"""
Type annotations for kinesis-video-signaling service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_signaling/type_defs/)

Usage::

    ```python
    from mypy_boto3_kinesis_video_signaling.type_defs import GetIceServerConfigRequestRequestTypeDef

    data: GetIceServerConfigRequestRequestTypeDef = ...
    ```
"""

import sys
from typing import Dict, List

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "GetIceServerConfigRequestRequestTypeDef",
    "IceServerTypeDef",
    "ResponseMetadataTypeDef",
    "SendAlexaOfferToMasterRequestRequestTypeDef",
    "GetIceServerConfigResponseTypeDef",
    "SendAlexaOfferToMasterResponseTypeDef",
)

GetIceServerConfigRequestRequestTypeDef = TypedDict(
    "GetIceServerConfigRequestRequestTypeDef",
    {
        "ChannelARN": str,
        "ClientId": NotRequired[str],
        "Service": NotRequired[Literal["TURN"]],
        "Username": NotRequired[str],
    },
)
IceServerTypeDef = TypedDict(
    "IceServerTypeDef",
    {
        "Uris": NotRequired[List[str]],
        "Username": NotRequired[str],
        "Password": NotRequired[str],
        "Ttl": NotRequired[int],
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
SendAlexaOfferToMasterRequestRequestTypeDef = TypedDict(
    "SendAlexaOfferToMasterRequestRequestTypeDef",
    {
        "ChannelARN": str,
        "SenderClientId": str,
        "MessagePayload": str,
    },
)
GetIceServerConfigResponseTypeDef = TypedDict(
    "GetIceServerConfigResponseTypeDef",
    {
        "IceServerList": List[IceServerTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendAlexaOfferToMasterResponseTypeDef = TypedDict(
    "SendAlexaOfferToMasterResponseTypeDef",
    {
        "Answer": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
