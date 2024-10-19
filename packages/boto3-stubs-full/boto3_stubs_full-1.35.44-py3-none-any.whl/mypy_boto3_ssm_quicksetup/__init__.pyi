"""
Main interface for ssm-quicksetup service.

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_ssm_quicksetup import (
        Client,
        ListConfigurationManagersPaginator,
        SystemsManagerQuickSetupClient,
    )

    session = Session()
    client: SystemsManagerQuickSetupClient = session.client("ssm-quicksetup")

    list_configuration_managers_paginator: ListConfigurationManagersPaginator = client.get_paginator("list_configuration_managers")
    ```
"""

from .client import SystemsManagerQuickSetupClient
from .paginator import ListConfigurationManagersPaginator

Client = SystemsManagerQuickSetupClient

__all__ = ("Client", "ListConfigurationManagersPaginator", "SystemsManagerQuickSetupClient")
