"""
Type annotations for trustedadvisor service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_trustedadvisor.client import TrustedAdvisorPublicAPIClient

    session = Session()
    client: TrustedAdvisorPublicAPIClient = session.client("trustedadvisor")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    ListChecksPaginator,
    ListOrganizationRecommendationAccountsPaginator,
    ListOrganizationRecommendationResourcesPaginator,
    ListOrganizationRecommendationsPaginator,
    ListRecommendationResourcesPaginator,
    ListRecommendationsPaginator,
)
from .type_defs import (
    BatchUpdateRecommendationResourceExclusionRequestRequestTypeDef,
    BatchUpdateRecommendationResourceExclusionResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    GetOrganizationRecommendationRequestRequestTypeDef,
    GetOrganizationRecommendationResponseTypeDef,
    GetRecommendationRequestRequestTypeDef,
    GetRecommendationResponseTypeDef,
    ListChecksRequestRequestTypeDef,
    ListChecksResponseTypeDef,
    ListOrganizationRecommendationAccountsRequestRequestTypeDef,
    ListOrganizationRecommendationAccountsResponseTypeDef,
    ListOrganizationRecommendationResourcesRequestRequestTypeDef,
    ListOrganizationRecommendationResourcesResponseTypeDef,
    ListOrganizationRecommendationsRequestRequestTypeDef,
    ListOrganizationRecommendationsResponseTypeDef,
    ListRecommendationResourcesRequestRequestTypeDef,
    ListRecommendationResourcesResponseTypeDef,
    ListRecommendationsRequestRequestTypeDef,
    ListRecommendationsResponseTypeDef,
    UpdateOrganizationRecommendationLifecycleRequestRequestTypeDef,
    UpdateRecommendationLifecycleRequestRequestTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("TrustedAdvisorPublicAPIClient",)

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
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class TrustedAdvisorPublicAPIClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        TrustedAdvisorPublicAPIClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#exceptions)
        """

    def batch_update_recommendation_resource_exclusion(
        self, **kwargs: Unpack[BatchUpdateRecommendationResourceExclusionRequestRequestTypeDef]
    ) -> BatchUpdateRecommendationResourceExclusionResponseTypeDef:
        """
        Update one or more exclusion status for a list of recommendation resources See
        also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/trustedadvisor-2022-09-15/BatchUpdateRecommendationResourceExclusion).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.batch_update_recommendation_resource_exclusion)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#batch_update_recommendation_resource_exclusion)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#close)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#generate_presigned_url)
        """

    def get_organization_recommendation(
        self, **kwargs: Unpack[GetOrganizationRecommendationRequestRequestTypeDef]
    ) -> GetOrganizationRecommendationResponseTypeDef:
        """
        Get a specific recommendation within an AWS Organizations organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.get_organization_recommendation)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#get_organization_recommendation)
        """

    def get_recommendation(
        self, **kwargs: Unpack[GetRecommendationRequestRequestTypeDef]
    ) -> GetRecommendationResponseTypeDef:
        """
        Get a specific Recommendation See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/trustedadvisor-2022-09-15/GetRecommendation).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.get_recommendation)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#get_recommendation)
        """

    def list_checks(
        self, **kwargs: Unpack[ListChecksRequestRequestTypeDef]
    ) -> ListChecksResponseTypeDef:
        """
        List a filterable set of Checks See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/trustedadvisor-2022-09-15/ListChecks).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.list_checks)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#list_checks)
        """

    def list_organization_recommendation_accounts(
        self, **kwargs: Unpack[ListOrganizationRecommendationAccountsRequestRequestTypeDef]
    ) -> ListOrganizationRecommendationAccountsResponseTypeDef:
        """
        Lists the accounts that own the resources for an organization aggregate
        recommendation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.list_organization_recommendation_accounts)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#list_organization_recommendation_accounts)
        """

    def list_organization_recommendation_resources(
        self, **kwargs: Unpack[ListOrganizationRecommendationResourcesRequestRequestTypeDef]
    ) -> ListOrganizationRecommendationResourcesResponseTypeDef:
        """
        List Resources of a Recommendation within an Organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.list_organization_recommendation_resources)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#list_organization_recommendation_resources)
        """

    def list_organization_recommendations(
        self, **kwargs: Unpack[ListOrganizationRecommendationsRequestRequestTypeDef]
    ) -> ListOrganizationRecommendationsResponseTypeDef:
        """
        List a filterable set of Recommendations within an Organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.list_organization_recommendations)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#list_organization_recommendations)
        """

    def list_recommendation_resources(
        self, **kwargs: Unpack[ListRecommendationResourcesRequestRequestTypeDef]
    ) -> ListRecommendationResourcesResponseTypeDef:
        """
        List Resources of a Recommendation See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/trustedadvisor-2022-09-15/ListRecommendationResources).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.list_recommendation_resources)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#list_recommendation_resources)
        """

    def list_recommendations(
        self, **kwargs: Unpack[ListRecommendationsRequestRequestTypeDef]
    ) -> ListRecommendationsResponseTypeDef:
        """
        List a filterable set of Recommendations See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/trustedadvisor-2022-09-15/ListRecommendations).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.list_recommendations)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#list_recommendations)
        """

    def update_organization_recommendation_lifecycle(
        self, **kwargs: Unpack[UpdateOrganizationRecommendationLifecycleRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Update the lifecycle of a Recommendation within an Organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.update_organization_recommendation_lifecycle)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#update_organization_recommendation_lifecycle)
        """

    def update_recommendation_lifecycle(
        self, **kwargs: Unpack[UpdateRecommendationLifecycleRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Update the lifecyle of a Recommendation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.update_recommendation_lifecycle)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#update_recommendation_lifecycle)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_checks"]) -> ListChecksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_organization_recommendation_accounts"]
    ) -> ListOrganizationRecommendationAccountsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_organization_recommendation_resources"]
    ) -> ListOrganizationRecommendationResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_organization_recommendations"]
    ) -> ListOrganizationRecommendationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_recommendation_resources"]
    ) -> ListRecommendationResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_recommendations"]
    ) -> ListRecommendationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#get_paginator)
        """
