"""
Type annotations for personalize-events service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_personalize_events.client import PersonalizeEventsClient

    session = Session()
    client: PersonalizeEventsClient = session.client("personalize-events")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
    EmptyResponseMetadataTypeDef,
    PutActionInteractionsRequestRequestTypeDef,
    PutActionsRequestRequestTypeDef,
    PutEventsRequestRequestTypeDef,
    PutItemsRequestRequestTypeDef,
    PutUsersRequestRequestTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("PersonalizeEventsClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]

class PersonalizeEventsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-events.html#PersonalizeEvents.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PersonalizeEventsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-events.html#PersonalizeEvents.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-events.html#PersonalizeEvents.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-events.html#PersonalizeEvents.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/client/#close)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-events.html#PersonalizeEvents.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/client/#generate_presigned_url)
        """

    def put_action_interactions(
        self, **kwargs: Unpack[PutActionInteractionsRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Records action interaction event data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-events.html#PersonalizeEvents.Client.put_action_interactions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/client/#put_action_interactions)
        """

    def put_actions(
        self, **kwargs: Unpack[PutActionsRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds one or more actions to an Actions dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-events.html#PersonalizeEvents.Client.put_actions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/client/#put_actions)
        """

    def put_events(
        self, **kwargs: Unpack[PutEventsRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Records item interaction event data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-events.html#PersonalizeEvents.Client.put_events)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/client/#put_events)
        """

    def put_items(
        self, **kwargs: Unpack[PutItemsRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds one or more items to an Items dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-events.html#PersonalizeEvents.Client.put_items)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/client/#put_items)
        """

    def put_users(
        self, **kwargs: Unpack[PutUsersRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds one or more users to a Users dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/personalize-events.html#PersonalizeEvents.Client.put_users)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/client/#put_users)
        """
