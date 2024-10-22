"""
Type annotations for sqs service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_sqs.client import SQSClient

    session = Session()
    client: SQSClient = session.client("sqs")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import ListDeadLetterSourceQueuesPaginator, ListQueuesPaginator
from .type_defs import (
    AddPermissionRequestRequestTypeDef,
    CancelMessageMoveTaskRequestRequestTypeDef,
    CancelMessageMoveTaskResultTypeDef,
    ChangeMessageVisibilityBatchRequestRequestTypeDef,
    ChangeMessageVisibilityBatchResultTypeDef,
    ChangeMessageVisibilityRequestRequestTypeDef,
    CreateQueueRequestRequestTypeDef,
    CreateQueueResultTypeDef,
    DeleteMessageBatchRequestRequestTypeDef,
    DeleteMessageBatchResultTypeDef,
    DeleteMessageRequestRequestTypeDef,
    DeleteQueueRequestRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    GetQueueAttributesRequestRequestTypeDef,
    GetQueueAttributesResultTypeDef,
    GetQueueUrlRequestRequestTypeDef,
    GetQueueUrlResultTypeDef,
    ListDeadLetterSourceQueuesRequestRequestTypeDef,
    ListDeadLetterSourceQueuesResultTypeDef,
    ListMessageMoveTasksRequestRequestTypeDef,
    ListMessageMoveTasksResultTypeDef,
    ListQueuesRequestRequestTypeDef,
    ListQueuesResultTypeDef,
    ListQueueTagsRequestRequestTypeDef,
    ListQueueTagsResultTypeDef,
    PurgeQueueRequestRequestTypeDef,
    ReceiveMessageRequestRequestTypeDef,
    ReceiveMessageResultTypeDef,
    RemovePermissionRequestRequestTypeDef,
    SendMessageBatchRequestRequestTypeDef,
    SendMessageBatchResultTypeDef,
    SendMessageRequestRequestTypeDef,
    SendMessageResultTypeDef,
    SetQueueAttributesRequestRequestTypeDef,
    StartMessageMoveTaskRequestRequestTypeDef,
    StartMessageMoveTaskResultTypeDef,
    TagQueueRequestRequestTypeDef,
    UntagQueueRequestRequestTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack


__all__ = ("SQSClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BatchEntryIdsNotDistinct: Type[BotocoreClientError]
    BatchRequestTooLong: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    EmptyBatchRequest: Type[BotocoreClientError]
    InvalidAddress: Type[BotocoreClientError]
    InvalidAttributeName: Type[BotocoreClientError]
    InvalidAttributeValue: Type[BotocoreClientError]
    InvalidBatchEntryId: Type[BotocoreClientError]
    InvalidIdFormat: Type[BotocoreClientError]
    InvalidMessageContents: Type[BotocoreClientError]
    InvalidSecurity: Type[BotocoreClientError]
    KmsAccessDenied: Type[BotocoreClientError]
    KmsDisabled: Type[BotocoreClientError]
    KmsInvalidKeyUsage: Type[BotocoreClientError]
    KmsInvalidState: Type[BotocoreClientError]
    KmsNotFound: Type[BotocoreClientError]
    KmsOptInRequired: Type[BotocoreClientError]
    KmsThrottled: Type[BotocoreClientError]
    MessageNotInflight: Type[BotocoreClientError]
    OverLimit: Type[BotocoreClientError]
    PurgeQueueInProgress: Type[BotocoreClientError]
    QueueDeletedRecently: Type[BotocoreClientError]
    QueueDoesNotExist: Type[BotocoreClientError]
    QueueNameExists: Type[BotocoreClientError]
    ReceiptHandleIsInvalid: Type[BotocoreClientError]
    RequestThrottled: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TooManyEntriesInBatchRequest: Type[BotocoreClientError]
    UnsupportedOperation: Type[BotocoreClientError]


class SQSClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SQSClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#exceptions)
        """

    def add_permission(
        self, **kwargs: Unpack[AddPermissionRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds a permission to a queue for a specific
        [principal](https://docs.aws.amazon.com/general/latest/gr/glos-chap.html#P).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.add_permission)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#add_permission)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#can_paginate)
        """

    def cancel_message_move_task(
        self, **kwargs: Unpack[CancelMessageMoveTaskRequestRequestTypeDef]
    ) -> CancelMessageMoveTaskResultTypeDef:
        """
        Cancels a specified message movement task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.cancel_message_move_task)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#cancel_message_move_task)
        """

    def change_message_visibility(
        self, **kwargs: Unpack[ChangeMessageVisibilityRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Changes the visibility timeout of a specified message in a queue to a new value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.change_message_visibility)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#change_message_visibility)
        """

    def change_message_visibility_batch(
        self, **kwargs: Unpack[ChangeMessageVisibilityBatchRequestRequestTypeDef]
    ) -> ChangeMessageVisibilityBatchResultTypeDef:
        """
        Changes the visibility timeout of multiple messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.change_message_visibility_batch)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#change_message_visibility_batch)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#close)
        """

    def create_queue(
        self, **kwargs: Unpack[CreateQueueRequestRequestTypeDef]
    ) -> CreateQueueResultTypeDef:
        """
        Creates a new standard or FIFO queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.create_queue)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#create_queue)
        """

    def delete_message(
        self, **kwargs: Unpack[DeleteMessageRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified message from the specified queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.delete_message)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#delete_message)
        """

    def delete_message_batch(
        self, **kwargs: Unpack[DeleteMessageBatchRequestRequestTypeDef]
    ) -> DeleteMessageBatchResultTypeDef:
        """
        Deletes up to ten messages from the specified queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.delete_message_batch)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#delete_message_batch)
        """

    def delete_queue(
        self, **kwargs: Unpack[DeleteQueueRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the queue specified by the `QueueUrl`, regardless of the queue's
        contents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.delete_queue)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#delete_queue)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#generate_presigned_url)
        """

    def get_queue_attributes(
        self, **kwargs: Unpack[GetQueueAttributesRequestRequestTypeDef]
    ) -> GetQueueAttributesResultTypeDef:
        """
        Gets attributes for the specified queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.get_queue_attributes)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#get_queue_attributes)
        """

    def get_queue_url(
        self, **kwargs: Unpack[GetQueueUrlRequestRequestTypeDef]
    ) -> GetQueueUrlResultTypeDef:
        """
        Returns the URL of an existing Amazon SQS queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.get_queue_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#get_queue_url)
        """

    def list_dead_letter_source_queues(
        self, **kwargs: Unpack[ListDeadLetterSourceQueuesRequestRequestTypeDef]
    ) -> ListDeadLetterSourceQueuesResultTypeDef:
        """
        Returns a list of your queues that have the `RedrivePolicy` queue attribute
        configured with a dead-letter
        queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.list_dead_letter_source_queues)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#list_dead_letter_source_queues)
        """

    def list_message_move_tasks(
        self, **kwargs: Unpack[ListMessageMoveTasksRequestRequestTypeDef]
    ) -> ListMessageMoveTasksResultTypeDef:
        """
        Gets the most recent message movement tasks (up to 10) under a specific source
        queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.list_message_move_tasks)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#list_message_move_tasks)
        """

    def list_queue_tags(
        self, **kwargs: Unpack[ListQueueTagsRequestRequestTypeDef]
    ) -> ListQueueTagsResultTypeDef:
        """
        List all cost allocation tags added to the specified Amazon SQS queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.list_queue_tags)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#list_queue_tags)
        """

    def list_queues(
        self, **kwargs: Unpack[ListQueuesRequestRequestTypeDef]
    ) -> ListQueuesResultTypeDef:
        """
        Returns a list of your queues in the current region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.list_queues)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#list_queues)
        """

    def purge_queue(
        self, **kwargs: Unpack[PurgeQueueRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes available messages in a queue (including in-flight messages) specified
        by the `QueueURL`
        parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.purge_queue)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#purge_queue)
        """

    def receive_message(
        self, **kwargs: Unpack[ReceiveMessageRequestRequestTypeDef]
    ) -> ReceiveMessageResultTypeDef:
        """
        Retrieves one or more messages (up to 10), from the specified queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.receive_message)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#receive_message)
        """

    def remove_permission(
        self, **kwargs: Unpack[RemovePermissionRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Revokes any permissions in the queue policy that matches the specified `Label`
        parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.remove_permission)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#remove_permission)
        """

    def send_message(
        self, **kwargs: Unpack[SendMessageRequestRequestTypeDef]
    ) -> SendMessageResultTypeDef:
        """
        Delivers a message to the specified queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.send_message)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#send_message)
        """

    def send_message_batch(
        self, **kwargs: Unpack[SendMessageBatchRequestRequestTypeDef]
    ) -> SendMessageBatchResultTypeDef:
        """
        You can use `SendMessageBatch` to send up to 10 messages to the specified queue
        by assigning either identical or different values to each message (or by not
        assigning values at
        all).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.send_message_batch)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#send_message_batch)
        """

    def set_queue_attributes(
        self, **kwargs: Unpack[SetQueueAttributesRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Sets the value of one or more queue attributes, like a policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.set_queue_attributes)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#set_queue_attributes)
        """

    def start_message_move_task(
        self, **kwargs: Unpack[StartMessageMoveTaskRequestRequestTypeDef]
    ) -> StartMessageMoveTaskResultTypeDef:
        """
        Starts an asynchronous task to move messages from a specified source queue to a
        specified destination
        queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.start_message_move_task)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#start_message_move_task)
        """

    def tag_queue(
        self, **kwargs: Unpack[TagQueueRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Add cost allocation tags to the specified Amazon SQS queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.tag_queue)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#tag_queue)
        """

    def untag_queue(
        self, **kwargs: Unpack[UntagQueueRequestRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Remove cost allocation tags from the specified Amazon SQS queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.untag_queue)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#untag_queue)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dead_letter_source_queues"]
    ) -> ListDeadLetterSourceQueuesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_queues"]) -> ListQueuesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#get_paginator)
        """
