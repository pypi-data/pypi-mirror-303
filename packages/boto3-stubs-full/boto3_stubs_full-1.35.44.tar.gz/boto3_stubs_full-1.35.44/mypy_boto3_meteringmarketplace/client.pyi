"""
Type annotations for meteringmarketplace service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_meteringmarketplace/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_meteringmarketplace.client import MarketplaceMeteringClient

    session = Session()
    client: MarketplaceMeteringClient = session.client("meteringmarketplace")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
    BatchMeterUsageRequestRequestTypeDef,
    BatchMeterUsageResultTypeDef,
    MeterUsageRequestRequestTypeDef,
    MeterUsageResultTypeDef,
    RegisterUsageRequestRequestTypeDef,
    RegisterUsageResultTypeDef,
    ResolveCustomerRequestRequestTypeDef,
    ResolveCustomerResultTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("MarketplaceMeteringClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    CustomerNotEntitledException: Type[BotocoreClientError]
    DisabledApiException: Type[BotocoreClientError]
    DuplicateRequestException: Type[BotocoreClientError]
    ExpiredTokenException: Type[BotocoreClientError]
    InternalServiceErrorException: Type[BotocoreClientError]
    InvalidCustomerIdentifierException: Type[BotocoreClientError]
    InvalidEndpointRegionException: Type[BotocoreClientError]
    InvalidProductCodeException: Type[BotocoreClientError]
    InvalidPublicKeyVersionException: Type[BotocoreClientError]
    InvalidRegionException: Type[BotocoreClientError]
    InvalidTagException: Type[BotocoreClientError]
    InvalidTokenException: Type[BotocoreClientError]
    InvalidUsageAllocationsException: Type[BotocoreClientError]
    InvalidUsageDimensionException: Type[BotocoreClientError]
    PlatformNotSupportedException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TimestampOutOfBoundsException: Type[BotocoreClientError]

class MarketplaceMeteringClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/meteringmarketplace.html#MarketplaceMetering.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_meteringmarketplace/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MarketplaceMeteringClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_meteringmarketplace/client/#exceptions)
        """

    def batch_meter_usage(
        self, **kwargs: Unpack[BatchMeterUsageRequestRequestTypeDef]
    ) -> BatchMeterUsageResultTypeDef:
        """
        `BatchMeterUsage` is called from a SaaS application listed on AWS Marketplace
        to post metering records for a set of
        customers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.batch_meter_usage)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_meteringmarketplace/client/#batch_meter_usage)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_meteringmarketplace/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_meteringmarketplace/client/#close)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_meteringmarketplace/client/#generate_presigned_url)
        """

    def meter_usage(
        self, **kwargs: Unpack[MeterUsageRequestRequestTypeDef]
    ) -> MeterUsageResultTypeDef:
        """
        API to emit metering records.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.meter_usage)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_meteringmarketplace/client/#meter_usage)
        """

    def register_usage(
        self, **kwargs: Unpack[RegisterUsageRequestRequestTypeDef]
    ) -> RegisterUsageResultTypeDef:
        """
        Paid container software products sold through AWS Marketplace must integrate
        with the AWS Marketplace Metering Service and call the `RegisterUsage`
        operation for software entitlement and
        metering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.register_usage)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_meteringmarketplace/client/#register_usage)
        """

    def resolve_customer(
        self, **kwargs: Unpack[ResolveCustomerRequestRequestTypeDef]
    ) -> ResolveCustomerResultTypeDef:
        """
        `ResolveCustomer` is called by a SaaS application during the registration
        process.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/meteringmarketplace.html#MarketplaceMetering.Client.resolve_customer)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_meteringmarketplace/client/#resolve_customer)
        """
