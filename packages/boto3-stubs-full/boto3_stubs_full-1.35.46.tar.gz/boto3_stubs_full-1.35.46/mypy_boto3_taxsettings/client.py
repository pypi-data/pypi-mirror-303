"""
Type annotations for taxsettings service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_taxsettings.client import TaxSettingsClient

    session = Session()
    client: TaxSettingsClient = session.client("taxsettings")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type

from botocore.client import BaseClient, ClientMeta

from .paginator import ListTaxRegistrationsPaginator
from .type_defs import (
    BatchDeleteTaxRegistrationRequestRequestTypeDef,
    BatchDeleteTaxRegistrationResponseTypeDef,
    BatchPutTaxRegistrationRequestRequestTypeDef,
    BatchPutTaxRegistrationResponseTypeDef,
    DeleteTaxRegistrationRequestRequestTypeDef,
    GetTaxRegistrationDocumentRequestRequestTypeDef,
    GetTaxRegistrationDocumentResponseTypeDef,
    GetTaxRegistrationRequestRequestTypeDef,
    GetTaxRegistrationResponseTypeDef,
    ListTaxRegistrationsRequestRequestTypeDef,
    ListTaxRegistrationsResponseTypeDef,
    PutTaxRegistrationRequestRequestTypeDef,
    PutTaxRegistrationResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack


__all__ = ("TaxSettingsClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class TaxSettingsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings.html#TaxSettings.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        TaxSettingsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings.html#TaxSettings.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#exceptions)
        """

    def batch_delete_tax_registration(
        self, **kwargs: Unpack[BatchDeleteTaxRegistrationRequestRequestTypeDef]
    ) -> BatchDeleteTaxRegistrationResponseTypeDef:
        """
        Deletes tax registration for multiple accounts in batch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings.html#TaxSettings.Client.batch_delete_tax_registration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#batch_delete_tax_registration)
        """

    def batch_put_tax_registration(
        self, **kwargs: Unpack[BatchPutTaxRegistrationRequestRequestTypeDef]
    ) -> BatchPutTaxRegistrationResponseTypeDef:
        """
        Adds or updates tax registration for multiple accounts in batch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings.html#TaxSettings.Client.batch_put_tax_registration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#batch_put_tax_registration)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings.html#TaxSettings.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings.html#TaxSettings.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#close)
        """

    def delete_tax_registration(
        self, **kwargs: Unpack[DeleteTaxRegistrationRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes tax registration for a single account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings.html#TaxSettings.Client.delete_tax_registration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#delete_tax_registration)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings.html#TaxSettings.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#generate_presigned_url)
        """

    def get_tax_registration(
        self, **kwargs: Unpack[GetTaxRegistrationRequestRequestTypeDef]
    ) -> GetTaxRegistrationResponseTypeDef:
        """
        Retrieves tax registration for a single account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings.html#TaxSettings.Client.get_tax_registration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#get_tax_registration)
        """

    def get_tax_registration_document(
        self, **kwargs: Unpack[GetTaxRegistrationDocumentRequestRequestTypeDef]
    ) -> GetTaxRegistrationDocumentResponseTypeDef:
        """
        Downloads your tax documents to the Amazon S3 bucket that you specify in your
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings.html#TaxSettings.Client.get_tax_registration_document)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#get_tax_registration_document)
        """

    def list_tax_registrations(
        self, **kwargs: Unpack[ListTaxRegistrationsRequestRequestTypeDef]
    ) -> ListTaxRegistrationsResponseTypeDef:
        """
        Retrieves the tax registration of accounts listed in a consolidated billing
        family.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings.html#TaxSettings.Client.list_tax_registrations)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#list_tax_registrations)
        """

    def put_tax_registration(
        self, **kwargs: Unpack[PutTaxRegistrationRequestRequestTypeDef]
    ) -> PutTaxRegistrationResponseTypeDef:
        """
        Adds or updates tax registration for a single account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings.html#TaxSettings.Client.put_tax_registration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#put_tax_registration)
        """

    def get_paginator(
        self, operation_name: Literal["list_tax_registrations"]
    ) -> ListTaxRegistrationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/taxsettings.html#TaxSettings.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/client/#get_paginator)
        """
