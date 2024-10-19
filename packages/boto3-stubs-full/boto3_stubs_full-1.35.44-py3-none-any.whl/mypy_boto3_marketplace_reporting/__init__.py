"""
Main interface for marketplace-reporting service.

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_marketplace_reporting import (
        Client,
        MarketplaceReportingServiceClient,
    )

    session = Session()
    client: MarketplaceReportingServiceClient = session.client("marketplace-reporting")
    ```
"""

from .client import MarketplaceReportingServiceClient

Client = MarketplaceReportingServiceClient


__all__ = ("Client", "MarketplaceReportingServiceClient")
