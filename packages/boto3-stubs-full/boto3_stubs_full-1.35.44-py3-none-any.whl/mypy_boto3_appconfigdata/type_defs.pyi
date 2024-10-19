"""
Type annotations for appconfigdata service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfigdata/type_defs/)

Usage::

    ```python
    from mypy_boto3_appconfigdata.type_defs import GetLatestConfigurationRequestRequestTypeDef

    data: GetLatestConfigurationRequestRequestTypeDef = ...
    ```
"""

import sys
from typing import Dict

from botocore.response import StreamingBody

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "GetLatestConfigurationRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "StartConfigurationSessionRequestRequestTypeDef",
    "GetLatestConfigurationResponseTypeDef",
    "StartConfigurationSessionResponseTypeDef",
)

GetLatestConfigurationRequestRequestTypeDef = TypedDict(
    "GetLatestConfigurationRequestRequestTypeDef",
    {
        "ConfigurationToken": str,
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
StartConfigurationSessionRequestRequestTypeDef = TypedDict(
    "StartConfigurationSessionRequestRequestTypeDef",
    {
        "ApplicationIdentifier": str,
        "EnvironmentIdentifier": str,
        "ConfigurationProfileIdentifier": str,
        "RequiredMinimumPollIntervalInSeconds": NotRequired[int],
    },
)
GetLatestConfigurationResponseTypeDef = TypedDict(
    "GetLatestConfigurationResponseTypeDef",
    {
        "NextPollConfigurationToken": str,
        "NextPollIntervalInSeconds": int,
        "ContentType": str,
        "Configuration": StreamingBody,
        "VersionLabel": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartConfigurationSessionResponseTypeDef = TypedDict(
    "StartConfigurationSessionResponseTypeDef",
    {
        "InitialConfigurationToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
