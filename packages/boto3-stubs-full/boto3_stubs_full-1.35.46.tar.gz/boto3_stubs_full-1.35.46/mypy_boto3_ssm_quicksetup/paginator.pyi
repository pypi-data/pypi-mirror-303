"""
Type annotations for ssm-quicksetup service client paginators.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_quicksetup/paginators/)

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_ssm_quicksetup.client import SystemsManagerQuickSetupClient
    from mypy_boto3_ssm_quicksetup.paginator import (
        ListConfigurationManagersPaginator,
    )

    session = Session()
    client: SystemsManagerQuickSetupClient = session.client("ssm-quicksetup")

    list_configuration_managers_paginator: ListConfigurationManagersPaginator = client.get_paginator("list_configuration_managers")
    ```
"""

import sys
from typing import Generic, Iterator, TypeVar

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListConfigurationManagersInputListConfigurationManagersPaginateTypeDef,
    ListConfigurationManagersOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListConfigurationManagersPaginator",)

_ItemTypeDef = TypeVar("_ItemTypeDef")

class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """

class ListConfigurationManagersPaginator(Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-quicksetup.html#SystemsManagerQuickSetup.Paginator.ListConfigurationManagers)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_quicksetup/paginators/#listconfigurationmanagerspaginator)
    """
    def paginate(
        self,
        **kwargs: Unpack[ListConfigurationManagersInputListConfigurationManagersPaginateTypeDef],
    ) -> _PageIterator[ListConfigurationManagersOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-quicksetup.html#SystemsManagerQuickSetup.Paginator.ListConfigurationManagers.paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_quicksetup/paginators/#listconfigurationmanagerspaginator)
        """
