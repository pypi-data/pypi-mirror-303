"""
Type annotations for account service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_account/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_account.client import AccountClient

    session = Session()
    client: AccountClient = session.client("account")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type

from botocore.client import BaseClient, ClientMeta

from .paginator import ListRegionsPaginator
from .type_defs import (
    AcceptPrimaryEmailUpdateRequestRequestTypeDef,
    AcceptPrimaryEmailUpdateResponseTypeDef,
    DeleteAlternateContactRequestRequestTypeDef,
    DisableRegionRequestRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    EnableRegionRequestRequestTypeDef,
    GetAlternateContactRequestRequestTypeDef,
    GetAlternateContactResponseTypeDef,
    GetContactInformationRequestRequestTypeDef,
    GetContactInformationResponseTypeDef,
    GetPrimaryEmailRequestRequestTypeDef,
    GetPrimaryEmailResponseTypeDef,
    GetRegionOptStatusRequestRequestTypeDef,
    GetRegionOptStatusResponseTypeDef,
    ListRegionsRequestRequestTypeDef,
    ListRegionsResponseTypeDef,
    PutAlternateContactRequestRequestTypeDef,
    PutContactInformationRequestRequestTypeDef,
    StartPrimaryEmailUpdateRequestRequestTypeDef,
    StartPrimaryEmailUpdateResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("AccountClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class AccountClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_account/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AccountClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_account/client/#exceptions)
        """

    def accept_primary_email_update(
        self, **kwargs: Unpack[AcceptPrimaryEmailUpdateRequestRequestTypeDef]
    ) -> AcceptPrimaryEmailUpdateResponseTypeDef:
        """
        Accepts the request that originated from  StartPrimaryEmailUpdate to update the
        primary email address (also known as the root user email address) for the
        specified
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client.accept_primary_email_update)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_account/client/#accept_primary_email_update)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_account/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_account/client/#close)
        """

    def delete_alternate_contact(
        self, **kwargs: Unpack[DeleteAlternateContactRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified alternate contact from an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client.delete_alternate_contact)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_account/client/#delete_alternate_contact)
        """

    def disable_region(
        self, **kwargs: Unpack[DisableRegionRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Disables (opts-out) a particular Region for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client.disable_region)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_account/client/#disable_region)
        """

    def enable_region(
        self, **kwargs: Unpack[EnableRegionRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Enables (opts-in) a particular Region for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client.enable_region)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_account/client/#enable_region)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_account/client/#generate_presigned_url)
        """

    def get_alternate_contact(
        self, **kwargs: Unpack[GetAlternateContactRequestRequestTypeDef]
    ) -> GetAlternateContactResponseTypeDef:
        """
        Retrieves the specified alternate contact attached to an Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client.get_alternate_contact)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_account/client/#get_alternate_contact)
        """

    def get_contact_information(
        self, **kwargs: Unpack[GetContactInformationRequestRequestTypeDef]
    ) -> GetContactInformationResponseTypeDef:
        """
        Retrieves the primary contact information of an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client.get_contact_information)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_account/client/#get_contact_information)
        """

    def get_primary_email(
        self, **kwargs: Unpack[GetPrimaryEmailRequestRequestTypeDef]
    ) -> GetPrimaryEmailResponseTypeDef:
        """
        Retrieves the primary email address for the specified account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client.get_primary_email)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_account/client/#get_primary_email)
        """

    def get_region_opt_status(
        self, **kwargs: Unpack[GetRegionOptStatusRequestRequestTypeDef]
    ) -> GetRegionOptStatusResponseTypeDef:
        """
        Retrieves the opt-in status of a particular Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client.get_region_opt_status)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_account/client/#get_region_opt_status)
        """

    def list_regions(
        self, **kwargs: Unpack[ListRegionsRequestRequestTypeDef]
    ) -> ListRegionsResponseTypeDef:
        """
        Lists all the Regions for a given account and their respective opt-in statuses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client.list_regions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_account/client/#list_regions)
        """

    def put_alternate_contact(
        self, **kwargs: Unpack[PutAlternateContactRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Modifies the specified alternate contact attached to an Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client.put_alternate_contact)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_account/client/#put_alternate_contact)
        """

    def put_contact_information(
        self, **kwargs: Unpack[PutContactInformationRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the primary contact information of an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client.put_contact_information)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_account/client/#put_contact_information)
        """

    def start_primary_email_update(
        self, **kwargs: Unpack[StartPrimaryEmailUpdateRequestRequestTypeDef]
    ) -> StartPrimaryEmailUpdateResponseTypeDef:
        """
        Starts the process to update the primary email address for the specified
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client.start_primary_email_update)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_account/client/#start_primary_email_update)
        """

    def get_paginator(self, operation_name: Literal["list_regions"]) -> ListRegionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account.html#Account.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_account/client/#get_paginator)
        """
