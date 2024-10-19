"""
Type annotations for qapps service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_qapps.client import QAppsClient

    session = Session()
    client: QAppsClient = session.client("qapps")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import ListLibraryItemsPaginator, ListQAppsPaginator
from .type_defs import (
    AssociateLibraryItemReviewInputRequestTypeDef,
    AssociateQAppWithUserInputRequestTypeDef,
    CreateLibraryItemInputRequestTypeDef,
    CreateLibraryItemOutputTypeDef,
    CreateQAppInputRequestTypeDef,
    CreateQAppOutputTypeDef,
    DeleteLibraryItemInputRequestTypeDef,
    DeleteQAppInputRequestTypeDef,
    DisassociateLibraryItemReviewInputRequestTypeDef,
    DisassociateQAppFromUserInputRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    GetLibraryItemInputRequestTypeDef,
    GetLibraryItemOutputTypeDef,
    GetQAppInputRequestTypeDef,
    GetQAppOutputTypeDef,
    GetQAppSessionInputRequestTypeDef,
    GetQAppSessionOutputTypeDef,
    ImportDocumentInputRequestTypeDef,
    ImportDocumentOutputTypeDef,
    ListLibraryItemsInputRequestTypeDef,
    ListLibraryItemsOutputTypeDef,
    ListQAppsInputRequestTypeDef,
    ListQAppsOutputTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    PredictQAppInputRequestTypeDef,
    PredictQAppOutputTypeDef,
    StartQAppSessionInputRequestTypeDef,
    StartQAppSessionOutputTypeDef,
    StopQAppSessionInputRequestTypeDef,
    TagResourceRequestRequestTypeDef,
    UntagResourceRequestRequestTypeDef,
    UpdateLibraryItemInputRequestTypeDef,
    UpdateLibraryItemMetadataInputRequestTypeDef,
    UpdateLibraryItemOutputTypeDef,
    UpdateQAppInputRequestTypeDef,
    UpdateQAppOutputTypeDef,
    UpdateQAppSessionInputRequestTypeDef,
    UpdateQAppSessionOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("QAppsClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ContentTooLargeException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class QAppsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps.html#QApps.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        QAppsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps.html#QApps.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#exceptions)
        """

    def associate_library_item_review(
        self, **kwargs: Unpack[AssociateLibraryItemReviewInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Associates a rating or review for a library item with the user submitting the
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps.html#QApps.Client.associate_library_item_review)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#associate_library_item_review)
        """

    def associate_q_app_with_user(
        self, **kwargs: Unpack[AssociateQAppWithUserInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation creates a link between the user's identity calling the operation
        and a specific Q
        App.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps.html#QApps.Client.associate_q_app_with_user)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#associate_q_app_with_user)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps.html#QApps.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps.html#QApps.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#close)
        """

    def create_library_item(
        self, **kwargs: Unpack[CreateLibraryItemInputRequestTypeDef]
    ) -> CreateLibraryItemOutputTypeDef:
        """
        Creates a new library item for an Amazon Q App, allowing it to be discovered
        and used by other allowed
        users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps.html#QApps.Client.create_library_item)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#create_library_item)
        """

    def create_q_app(
        self, **kwargs: Unpack[CreateQAppInputRequestTypeDef]
    ) -> CreateQAppOutputTypeDef:
        """
        Creates a new Amazon Q App based on the provided definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps.html#QApps.Client.create_q_app)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#create_q_app)
        """

    def delete_library_item(
        self, **kwargs: Unpack[DeleteLibraryItemInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a library item for an Amazon Q App, removing it from the library so it
        can no longer be discovered or used by other
        users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps.html#QApps.Client.delete_library_item)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#delete_library_item)
        """

    def delete_q_app(
        self, **kwargs: Unpack[DeleteQAppInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an Amazon Q App owned by the user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps.html#QApps.Client.delete_q_app)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#delete_q_app)
        """

    def disassociate_library_item_review(
        self, **kwargs: Unpack[DisassociateLibraryItemReviewInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes a rating or review previously submitted by the user for a library item.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps.html#QApps.Client.disassociate_library_item_review)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#disassociate_library_item_review)
        """

    def disassociate_q_app_from_user(
        self, **kwargs: Unpack[DisassociateQAppFromUserInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Disassociates a Q App from a user removing the user's access to run the Q App.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps.html#QApps.Client.disassociate_q_app_from_user)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#disassociate_q_app_from_user)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps.html#QApps.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#generate_presigned_url)
        """

    def get_library_item(
        self, **kwargs: Unpack[GetLibraryItemInputRequestTypeDef]
    ) -> GetLibraryItemOutputTypeDef:
        """
        Retrieves details about a library item for an Amazon Q App, including its
        metadata, categories, ratings, and usage
        statistics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps.html#QApps.Client.get_library_item)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#get_library_item)
        """

    def get_q_app(self, **kwargs: Unpack[GetQAppInputRequestTypeDef]) -> GetQAppOutputTypeDef:
        """
        Retrieves the full details of an Q App, including its definition specifying the
        cards and
        flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps.html#QApps.Client.get_q_app)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#get_q_app)
        """

    def get_q_app_session(
        self, **kwargs: Unpack[GetQAppSessionInputRequestTypeDef]
    ) -> GetQAppSessionOutputTypeDef:
        """
        Retrieves the current state and results for an active session of an Amazon Q
        App.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps.html#QApps.Client.get_q_app_session)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#get_q_app_session)
        """

    def import_document(
        self, **kwargs: Unpack[ImportDocumentInputRequestTypeDef]
    ) -> ImportDocumentOutputTypeDef:
        """
        Uploads a file that can then be used either as a default in a `FileUploadCard`
        from Q App definition or as a file that is used inside a single Q App
        run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps.html#QApps.Client.import_document)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#import_document)
        """

    def list_library_items(
        self, **kwargs: Unpack[ListLibraryItemsInputRequestTypeDef]
    ) -> ListLibraryItemsOutputTypeDef:
        """
        Lists the library items for Amazon Q Apps that are published and available for
        users in your Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps.html#QApps.Client.list_library_items)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#list_library_items)
        """

    def list_q_apps(self, **kwargs: Unpack[ListQAppsInputRequestTypeDef]) -> ListQAppsOutputTypeDef:
        """
        Lists the Amazon Q Apps owned by or associated with the user either because
        they created it or because they used it from the library in the
        past.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps.html#QApps.Client.list_q_apps)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#list_q_apps)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags associated with an Amazon Q Apps resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps.html#QApps.Client.list_tags_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#list_tags_for_resource)
        """

    def predict_q_app(
        self, **kwargs: Unpack[PredictQAppInputRequestTypeDef]
    ) -> PredictQAppOutputTypeDef:
        """
        Generates an Amazon Q App definition based on either a conversation or a
        problem statement provided as input.The resulting app definition can be used to
        call
        `CreateQApp`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps.html#QApps.Client.predict_q_app)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#predict_q_app)
        """

    def start_q_app_session(
        self, **kwargs: Unpack[StartQAppSessionInputRequestTypeDef]
    ) -> StartQAppSessionOutputTypeDef:
        """
        Starts a new session for an Amazon Q App, allowing inputs to be provided and
        the app to be
        run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps.html#QApps.Client.start_q_app_session)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#start_q_app_session)
        """

    def stop_q_app_session(
        self, **kwargs: Unpack[StopQAppSessionInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Stops an active session for an Amazon Q App.This deletes all data related to
        the session and makes it invalid for future
        uses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps.html#QApps.Client.stop_q_app_session)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#stop_q_app_session)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Associates tags with an Amazon Q Apps resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps.html#QApps.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates tags from an Amazon Q Apps resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps.html#QApps.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#untag_resource)
        """

    def update_library_item(
        self, **kwargs: Unpack[UpdateLibraryItemInputRequestTypeDef]
    ) -> UpdateLibraryItemOutputTypeDef:
        """
        Updates the library item for an Amazon Q App.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps.html#QApps.Client.update_library_item)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#update_library_item)
        """

    def update_library_item_metadata(
        self, **kwargs: Unpack[UpdateLibraryItemMetadataInputRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the verification status of a library item for an Amazon Q App.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps.html#QApps.Client.update_library_item_metadata)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#update_library_item_metadata)
        """

    def update_q_app(
        self, **kwargs: Unpack[UpdateQAppInputRequestTypeDef]
    ) -> UpdateQAppOutputTypeDef:
        """
        Updates an existing Amazon Q App, allowing modifications to its title,
        description, and
        definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps.html#QApps.Client.update_q_app)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#update_q_app)
        """

    def update_q_app_session(
        self, **kwargs: Unpack[UpdateQAppSessionInputRequestTypeDef]
    ) -> UpdateQAppSessionOutputTypeDef:
        """
        Updates the session for a given Q App `sessionId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps.html#QApps.Client.update_q_app_session)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#update_q_app_session)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_library_items"]
    ) -> ListLibraryItemsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps.html#QApps.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_q_apps"]) -> ListQAppsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps.html#QApps.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#get_paginator)
        """
