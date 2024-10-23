"""
Type annotations for appstream service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_appstream.client import AppStreamClient

    session = Session()
    client: AppStreamClient = session.client("appstream")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    DescribeDirectoryConfigsPaginator,
    DescribeFleetsPaginator,
    DescribeImageBuildersPaginator,
    DescribeImagesPaginator,
    DescribeSessionsPaginator,
    DescribeStacksPaginator,
    DescribeUsersPaginator,
    DescribeUserStackAssociationsPaginator,
    ListAssociatedFleetsPaginator,
    ListAssociatedStacksPaginator,
)
from .type_defs import (
    AssociateAppBlockBuilderAppBlockRequestRequestTypeDef,
    AssociateAppBlockBuilderAppBlockResultTypeDef,
    AssociateApplicationFleetRequestRequestTypeDef,
    AssociateApplicationFleetResultTypeDef,
    AssociateApplicationToEntitlementRequestRequestTypeDef,
    AssociateFleetRequestRequestTypeDef,
    BatchAssociateUserStackRequestRequestTypeDef,
    BatchAssociateUserStackResultTypeDef,
    BatchDisassociateUserStackRequestRequestTypeDef,
    BatchDisassociateUserStackResultTypeDef,
    CopyImageRequestRequestTypeDef,
    CopyImageResponseTypeDef,
    CreateAppBlockBuilderRequestRequestTypeDef,
    CreateAppBlockBuilderResultTypeDef,
    CreateAppBlockBuilderStreamingURLRequestRequestTypeDef,
    CreateAppBlockBuilderStreamingURLResultTypeDef,
    CreateAppBlockRequestRequestTypeDef,
    CreateAppBlockResultTypeDef,
    CreateApplicationRequestRequestTypeDef,
    CreateApplicationResultTypeDef,
    CreateDirectoryConfigRequestRequestTypeDef,
    CreateDirectoryConfigResultTypeDef,
    CreateEntitlementRequestRequestTypeDef,
    CreateEntitlementResultTypeDef,
    CreateFleetRequestRequestTypeDef,
    CreateFleetResultTypeDef,
    CreateImageBuilderRequestRequestTypeDef,
    CreateImageBuilderResultTypeDef,
    CreateImageBuilderStreamingURLRequestRequestTypeDef,
    CreateImageBuilderStreamingURLResultTypeDef,
    CreateStackRequestRequestTypeDef,
    CreateStackResultTypeDef,
    CreateStreamingURLRequestRequestTypeDef,
    CreateStreamingURLResultTypeDef,
    CreateThemeForStackRequestRequestTypeDef,
    CreateThemeForStackResultTypeDef,
    CreateUpdatedImageRequestRequestTypeDef,
    CreateUpdatedImageResultTypeDef,
    CreateUsageReportSubscriptionResultTypeDef,
    CreateUserRequestRequestTypeDef,
    DeleteAppBlockBuilderRequestRequestTypeDef,
    DeleteAppBlockRequestRequestTypeDef,
    DeleteApplicationRequestRequestTypeDef,
    DeleteDirectoryConfigRequestRequestTypeDef,
    DeleteEntitlementRequestRequestTypeDef,
    DeleteFleetRequestRequestTypeDef,
    DeleteImageBuilderRequestRequestTypeDef,
    DeleteImageBuilderResultTypeDef,
    DeleteImagePermissionsRequestRequestTypeDef,
    DeleteImageRequestRequestTypeDef,
    DeleteImageResultTypeDef,
    DeleteStackRequestRequestTypeDef,
    DeleteThemeForStackRequestRequestTypeDef,
    DeleteUserRequestRequestTypeDef,
    DescribeAppBlockBuilderAppBlockAssociationsRequestRequestTypeDef,
    DescribeAppBlockBuilderAppBlockAssociationsResultTypeDef,
    DescribeAppBlockBuildersRequestRequestTypeDef,
    DescribeAppBlockBuildersResultTypeDef,
    DescribeAppBlocksRequestRequestTypeDef,
    DescribeAppBlocksResultTypeDef,
    DescribeApplicationFleetAssociationsRequestRequestTypeDef,
    DescribeApplicationFleetAssociationsResultTypeDef,
    DescribeApplicationsRequestRequestTypeDef,
    DescribeApplicationsResultTypeDef,
    DescribeDirectoryConfigsRequestRequestTypeDef,
    DescribeDirectoryConfigsResultTypeDef,
    DescribeEntitlementsRequestRequestTypeDef,
    DescribeEntitlementsResultTypeDef,
    DescribeFleetsRequestRequestTypeDef,
    DescribeFleetsResultTypeDef,
    DescribeImageBuildersRequestRequestTypeDef,
    DescribeImageBuildersResultTypeDef,
    DescribeImagePermissionsRequestRequestTypeDef,
    DescribeImagePermissionsResultTypeDef,
    DescribeImagesRequestRequestTypeDef,
    DescribeImagesResultTypeDef,
    DescribeSessionsRequestRequestTypeDef,
    DescribeSessionsResultTypeDef,
    DescribeStacksRequestRequestTypeDef,
    DescribeStacksResultTypeDef,
    DescribeThemeForStackRequestRequestTypeDef,
    DescribeThemeForStackResultTypeDef,
    DescribeUsageReportSubscriptionsRequestRequestTypeDef,
    DescribeUsageReportSubscriptionsResultTypeDef,
    DescribeUsersRequestRequestTypeDef,
    DescribeUsersResultTypeDef,
    DescribeUserStackAssociationsRequestRequestTypeDef,
    DescribeUserStackAssociationsResultTypeDef,
    DisableUserRequestRequestTypeDef,
    DisassociateAppBlockBuilderAppBlockRequestRequestTypeDef,
    DisassociateApplicationFleetRequestRequestTypeDef,
    DisassociateApplicationFromEntitlementRequestRequestTypeDef,
    DisassociateFleetRequestRequestTypeDef,
    EnableUserRequestRequestTypeDef,
    ExpireSessionRequestRequestTypeDef,
    ListAssociatedFleetsRequestRequestTypeDef,
    ListAssociatedFleetsResultTypeDef,
    ListAssociatedStacksRequestRequestTypeDef,
    ListAssociatedStacksResultTypeDef,
    ListEntitledApplicationsRequestRequestTypeDef,
    ListEntitledApplicationsResultTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    StartAppBlockBuilderRequestRequestTypeDef,
    StartAppBlockBuilderResultTypeDef,
    StartFleetRequestRequestTypeDef,
    StartImageBuilderRequestRequestTypeDef,
    StartImageBuilderResultTypeDef,
    StopAppBlockBuilderRequestRequestTypeDef,
    StopAppBlockBuilderResultTypeDef,
    StopFleetRequestRequestTypeDef,
    StopImageBuilderRequestRequestTypeDef,
    StopImageBuilderResultTypeDef,
    TagResourceRequestRequestTypeDef,
    UntagResourceRequestRequestTypeDef,
    UpdateAppBlockBuilderRequestRequestTypeDef,
    UpdateAppBlockBuilderResultTypeDef,
    UpdateApplicationRequestRequestTypeDef,
    UpdateApplicationResultTypeDef,
    UpdateDirectoryConfigRequestRequestTypeDef,
    UpdateDirectoryConfigResultTypeDef,
    UpdateEntitlementRequestRequestTypeDef,
    UpdateEntitlementResultTypeDef,
    UpdateFleetRequestRequestTypeDef,
    UpdateFleetResultTypeDef,
    UpdateImagePermissionsRequestRequestTypeDef,
    UpdateStackRequestRequestTypeDef,
    UpdateStackResultTypeDef,
    UpdateThemeForStackRequestRequestTypeDef,
    UpdateThemeForStackResultTypeDef,
)
from .waiter import FleetStartedWaiter, FleetStoppedWaiter

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("AppStreamClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    EntitlementAlreadyExistsException: Type[BotocoreClientError]
    EntitlementNotFoundException: Type[BotocoreClientError]
    IncompatibleImageException: Type[BotocoreClientError]
    InvalidAccountStatusException: Type[BotocoreClientError]
    InvalidParameterCombinationException: Type[BotocoreClientError]
    InvalidRoleException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    OperationNotPermittedException: Type[BotocoreClientError]
    RequestLimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotAvailableException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]

class AppStreamClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AppStreamClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#exceptions)
        """

    def associate_app_block_builder_app_block(
        self, **kwargs: Unpack[AssociateAppBlockBuilderAppBlockRequestRequestTypeDef]
    ) -> AssociateAppBlockBuilderAppBlockResultTypeDef:
        """
        Associates the specified app block builder with the specified app block.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.associate_app_block_builder_app_block)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#associate_app_block_builder_app_block)
        """

    def associate_application_fleet(
        self, **kwargs: Unpack[AssociateApplicationFleetRequestRequestTypeDef]
    ) -> AssociateApplicationFleetResultTypeDef:
        """
        Associates the specified application with the specified fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.associate_application_fleet)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#associate_application_fleet)
        """

    def associate_application_to_entitlement(
        self, **kwargs: Unpack[AssociateApplicationToEntitlementRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Associates an application to entitle.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.associate_application_to_entitlement)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#associate_application_to_entitlement)
        """

    def associate_fleet(
        self, **kwargs: Unpack[AssociateFleetRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Associates the specified fleet with the specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.associate_fleet)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#associate_fleet)
        """

    def batch_associate_user_stack(
        self, **kwargs: Unpack[BatchAssociateUserStackRequestRequestTypeDef]
    ) -> BatchAssociateUserStackResultTypeDef:
        """
        Associates the specified users with the specified stacks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.batch_associate_user_stack)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#batch_associate_user_stack)
        """

    def batch_disassociate_user_stack(
        self, **kwargs: Unpack[BatchDisassociateUserStackRequestRequestTypeDef]
    ) -> BatchDisassociateUserStackResultTypeDef:
        """
        Disassociates the specified users from the specified stacks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.batch_disassociate_user_stack)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#batch_disassociate_user_stack)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#close)
        """

    def copy_image(
        self, **kwargs: Unpack[CopyImageRequestRequestTypeDef]
    ) -> CopyImageResponseTypeDef:
        """
        Copies the image within the same region or to a new region within the same AWS
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.copy_image)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#copy_image)
        """

    def create_app_block(
        self, **kwargs: Unpack[CreateAppBlockRequestRequestTypeDef]
    ) -> CreateAppBlockResultTypeDef:
        """
        Creates an app block.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.create_app_block)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#create_app_block)
        """

    def create_app_block_builder(
        self, **kwargs: Unpack[CreateAppBlockBuilderRequestRequestTypeDef]
    ) -> CreateAppBlockBuilderResultTypeDef:
        """
        Creates an app block builder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.create_app_block_builder)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#create_app_block_builder)
        """

    def create_app_block_builder_streaming_url(
        self, **kwargs: Unpack[CreateAppBlockBuilderStreamingURLRequestRequestTypeDef]
    ) -> CreateAppBlockBuilderStreamingURLResultTypeDef:
        """
        Creates a URL to start a create app block builder streaming session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.create_app_block_builder_streaming_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#create_app_block_builder_streaming_url)
        """

    def create_application(
        self, **kwargs: Unpack[CreateApplicationRequestRequestTypeDef]
    ) -> CreateApplicationResultTypeDef:
        """
        Creates an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.create_application)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#create_application)
        """

    def create_directory_config(
        self, **kwargs: Unpack[CreateDirectoryConfigRequestRequestTypeDef]
    ) -> CreateDirectoryConfigResultTypeDef:
        """
        Creates a Directory Config object in AppStream 2.0.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.create_directory_config)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#create_directory_config)
        """

    def create_entitlement(
        self, **kwargs: Unpack[CreateEntitlementRequestRequestTypeDef]
    ) -> CreateEntitlementResultTypeDef:
        """
        Creates a new entitlement.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.create_entitlement)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#create_entitlement)
        """

    def create_fleet(
        self, **kwargs: Unpack[CreateFleetRequestRequestTypeDef]
    ) -> CreateFleetResultTypeDef:
        """
        Creates a fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.create_fleet)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#create_fleet)
        """

    def create_image_builder(
        self, **kwargs: Unpack[CreateImageBuilderRequestRequestTypeDef]
    ) -> CreateImageBuilderResultTypeDef:
        """
        Creates an image builder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.create_image_builder)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#create_image_builder)
        """

    def create_image_builder_streaming_url(
        self, **kwargs: Unpack[CreateImageBuilderStreamingURLRequestRequestTypeDef]
    ) -> CreateImageBuilderStreamingURLResultTypeDef:
        """
        Creates a URL to start an image builder streaming session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.create_image_builder_streaming_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#create_image_builder_streaming_url)
        """

    def create_stack(
        self, **kwargs: Unpack[CreateStackRequestRequestTypeDef]
    ) -> CreateStackResultTypeDef:
        """
        Creates a stack to start streaming applications to users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.create_stack)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#create_stack)
        """

    def create_streaming_url(
        self, **kwargs: Unpack[CreateStreamingURLRequestRequestTypeDef]
    ) -> CreateStreamingURLResultTypeDef:
        """
        Creates a temporary URL to start an AppStream 2.0 streaming session for the
        specified
        user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.create_streaming_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#create_streaming_url)
        """

    def create_theme_for_stack(
        self, **kwargs: Unpack[CreateThemeForStackRequestRequestTypeDef]
    ) -> CreateThemeForStackResultTypeDef:
        """
        Creates custom branding that customizes the appearance of the streaming
        application catalog
        page.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.create_theme_for_stack)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#create_theme_for_stack)
        """

    def create_updated_image(
        self, **kwargs: Unpack[CreateUpdatedImageRequestRequestTypeDef]
    ) -> CreateUpdatedImageResultTypeDef:
        """
        Creates a new image with the latest Windows operating system updates, driver
        updates, and AppStream 2.0 agent
        software.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.create_updated_image)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#create_updated_image)
        """

    def create_usage_report_subscription(self) -> CreateUsageReportSubscriptionResultTypeDef:
        """
        Creates a usage report subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.create_usage_report_subscription)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#create_usage_report_subscription)
        """

    def create_user(self, **kwargs: Unpack[CreateUserRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Creates a new user in the user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.create_user)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#create_user)
        """

    def delete_app_block(
        self, **kwargs: Unpack[DeleteAppBlockRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an app block.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.delete_app_block)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#delete_app_block)
        """

    def delete_app_block_builder(
        self, **kwargs: Unpack[DeleteAppBlockBuilderRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an app block builder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.delete_app_block_builder)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#delete_app_block_builder)
        """

    def delete_application(
        self, **kwargs: Unpack[DeleteApplicationRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.delete_application)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#delete_application)
        """

    def delete_directory_config(
        self, **kwargs: Unpack[DeleteDirectoryConfigRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified Directory Config object from AppStream 2.0.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.delete_directory_config)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#delete_directory_config)
        """

    def delete_entitlement(
        self, **kwargs: Unpack[DeleteEntitlementRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified entitlement.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.delete_entitlement)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#delete_entitlement)
        """

    def delete_fleet(self, **kwargs: Unpack[DeleteFleetRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.delete_fleet)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#delete_fleet)
        """

    def delete_image(
        self, **kwargs: Unpack[DeleteImageRequestRequestTypeDef]
    ) -> DeleteImageResultTypeDef:
        """
        Deletes the specified image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.delete_image)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#delete_image)
        """

    def delete_image_builder(
        self, **kwargs: Unpack[DeleteImageBuilderRequestRequestTypeDef]
    ) -> DeleteImageBuilderResultTypeDef:
        """
        Deletes the specified image builder and releases the capacity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.delete_image_builder)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#delete_image_builder)
        """

    def delete_image_permissions(
        self, **kwargs: Unpack[DeleteImagePermissionsRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes permissions for the specified private image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.delete_image_permissions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#delete_image_permissions)
        """

    def delete_stack(self, **kwargs: Unpack[DeleteStackRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.delete_stack)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#delete_stack)
        """

    def delete_theme_for_stack(
        self, **kwargs: Unpack[DeleteThemeForStackRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes custom branding that customizes the appearance of the streaming
        application catalog
        page.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.delete_theme_for_stack)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#delete_theme_for_stack)
        """

    def delete_usage_report_subscription(self) -> Dict[str, Any]:
        """
        Disables usage report generation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.delete_usage_report_subscription)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#delete_usage_report_subscription)
        """

    def delete_user(self, **kwargs: Unpack[DeleteUserRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a user from the user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.delete_user)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#delete_user)
        """

    def describe_app_block_builder_app_block_associations(
        self, **kwargs: Unpack[DescribeAppBlockBuilderAppBlockAssociationsRequestRequestTypeDef]
    ) -> DescribeAppBlockBuilderAppBlockAssociationsResultTypeDef:
        """
        Retrieves a list that describes one or more app block builder associations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.describe_app_block_builder_app_block_associations)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#describe_app_block_builder_app_block_associations)
        """

    def describe_app_block_builders(
        self, **kwargs: Unpack[DescribeAppBlockBuildersRequestRequestTypeDef]
    ) -> DescribeAppBlockBuildersResultTypeDef:
        """
        Retrieves a list that describes one or more app block builders.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.describe_app_block_builders)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#describe_app_block_builders)
        """

    def describe_app_blocks(
        self, **kwargs: Unpack[DescribeAppBlocksRequestRequestTypeDef]
    ) -> DescribeAppBlocksResultTypeDef:
        """
        Retrieves a list that describes one or more app blocks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.describe_app_blocks)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#describe_app_blocks)
        """

    def describe_application_fleet_associations(
        self, **kwargs: Unpack[DescribeApplicationFleetAssociationsRequestRequestTypeDef]
    ) -> DescribeApplicationFleetAssociationsResultTypeDef:
        """
        Retrieves a list that describes one or more application fleet associations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.describe_application_fleet_associations)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#describe_application_fleet_associations)
        """

    def describe_applications(
        self, **kwargs: Unpack[DescribeApplicationsRequestRequestTypeDef]
    ) -> DescribeApplicationsResultTypeDef:
        """
        Retrieves a list that describes one or more applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.describe_applications)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#describe_applications)
        """

    def describe_directory_configs(
        self, **kwargs: Unpack[DescribeDirectoryConfigsRequestRequestTypeDef]
    ) -> DescribeDirectoryConfigsResultTypeDef:
        """
        Retrieves a list that describes one or more specified Directory Config objects
        for AppStream 2.0, if the names for these objects are
        provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.describe_directory_configs)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#describe_directory_configs)
        """

    def describe_entitlements(
        self, **kwargs: Unpack[DescribeEntitlementsRequestRequestTypeDef]
    ) -> DescribeEntitlementsResultTypeDef:
        """
        Retrieves a list that describes one of more entitlements.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.describe_entitlements)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#describe_entitlements)
        """

    def describe_fleets(
        self, **kwargs: Unpack[DescribeFleetsRequestRequestTypeDef]
    ) -> DescribeFleetsResultTypeDef:
        """
        Retrieves a list that describes one or more specified fleets, if the fleet
        names are
        provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.describe_fleets)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#describe_fleets)
        """

    def describe_image_builders(
        self, **kwargs: Unpack[DescribeImageBuildersRequestRequestTypeDef]
    ) -> DescribeImageBuildersResultTypeDef:
        """
        Retrieves a list that describes one or more specified image builders, if the
        image builder names are
        provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.describe_image_builders)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#describe_image_builders)
        """

    def describe_image_permissions(
        self, **kwargs: Unpack[DescribeImagePermissionsRequestRequestTypeDef]
    ) -> DescribeImagePermissionsResultTypeDef:
        """
        Retrieves a list that describes the permissions for shared AWS account IDs on a
        private image that you
        own.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.describe_image_permissions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#describe_image_permissions)
        """

    def describe_images(
        self, **kwargs: Unpack[DescribeImagesRequestRequestTypeDef]
    ) -> DescribeImagesResultTypeDef:
        """
        Retrieves a list that describes one or more specified images, if the image
        names or image ARNs are
        provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.describe_images)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#describe_images)
        """

    def describe_sessions(
        self, **kwargs: Unpack[DescribeSessionsRequestRequestTypeDef]
    ) -> DescribeSessionsResultTypeDef:
        """
        Retrieves a list that describes the streaming sessions for a specified stack
        and
        fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.describe_sessions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#describe_sessions)
        """

    def describe_stacks(
        self, **kwargs: Unpack[DescribeStacksRequestRequestTypeDef]
    ) -> DescribeStacksResultTypeDef:
        """
        Retrieves a list that describes one or more specified stacks, if the stack
        names are
        provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.describe_stacks)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#describe_stacks)
        """

    def describe_theme_for_stack(
        self, **kwargs: Unpack[DescribeThemeForStackRequestRequestTypeDef]
    ) -> DescribeThemeForStackResultTypeDef:
        """
        Retrieves a list that describes the theme for a specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.describe_theme_for_stack)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#describe_theme_for_stack)
        """

    def describe_usage_report_subscriptions(
        self, **kwargs: Unpack[DescribeUsageReportSubscriptionsRequestRequestTypeDef]
    ) -> DescribeUsageReportSubscriptionsResultTypeDef:
        """
        Retrieves a list that describes one or more usage report subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.describe_usage_report_subscriptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#describe_usage_report_subscriptions)
        """

    def describe_user_stack_associations(
        self, **kwargs: Unpack[DescribeUserStackAssociationsRequestRequestTypeDef]
    ) -> DescribeUserStackAssociationsResultTypeDef:
        """
        Retrieves a list that describes the UserStackAssociation objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.describe_user_stack_associations)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#describe_user_stack_associations)
        """

    def describe_users(
        self, **kwargs: Unpack[DescribeUsersRequestRequestTypeDef]
    ) -> DescribeUsersResultTypeDef:
        """
        Retrieves a list that describes one or more specified users in the user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.describe_users)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#describe_users)
        """

    def disable_user(self, **kwargs: Unpack[DisableUserRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Disables the specified user in the user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.disable_user)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#disable_user)
        """

    def disassociate_app_block_builder_app_block(
        self, **kwargs: Unpack[DisassociateAppBlockBuilderAppBlockRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates a specified app block builder from a specified app block.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.disassociate_app_block_builder_app_block)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#disassociate_app_block_builder_app_block)
        """

    def disassociate_application_fleet(
        self, **kwargs: Unpack[DisassociateApplicationFleetRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates the specified application from the fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.disassociate_application_fleet)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#disassociate_application_fleet)
        """

    def disassociate_application_from_entitlement(
        self, **kwargs: Unpack[DisassociateApplicationFromEntitlementRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified application from the specified entitlement.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.disassociate_application_from_entitlement)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#disassociate_application_from_entitlement)
        """

    def disassociate_fleet(
        self, **kwargs: Unpack[DisassociateFleetRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates the specified fleet from the specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.disassociate_fleet)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#disassociate_fleet)
        """

    def enable_user(self, **kwargs: Unpack[EnableUserRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Enables a user in the user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.enable_user)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#enable_user)
        """

    def expire_session(
        self, **kwargs: Unpack[ExpireSessionRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Immediately stops the specified streaming session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.expire_session)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#expire_session)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#generate_presigned_url)
        """

    def list_associated_fleets(
        self, **kwargs: Unpack[ListAssociatedFleetsRequestRequestTypeDef]
    ) -> ListAssociatedFleetsResultTypeDef:
        """
        Retrieves the name of the fleet that is associated with the specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.list_associated_fleets)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#list_associated_fleets)
        """

    def list_associated_stacks(
        self, **kwargs: Unpack[ListAssociatedStacksRequestRequestTypeDef]
    ) -> ListAssociatedStacksResultTypeDef:
        """
        Retrieves the name of the stack with which the specified fleet is associated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.list_associated_stacks)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#list_associated_stacks)
        """

    def list_entitled_applications(
        self, **kwargs: Unpack[ListEntitledApplicationsRequestRequestTypeDef]
    ) -> ListEntitledApplicationsResultTypeDef:
        """
        Retrieves a list of entitled applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.list_entitled_applications)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#list_entitled_applications)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves a list of all tags for the specified AppStream 2.0 resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.list_tags_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#list_tags_for_resource)
        """

    def start_app_block_builder(
        self, **kwargs: Unpack[StartAppBlockBuilderRequestRequestTypeDef]
    ) -> StartAppBlockBuilderResultTypeDef:
        """
        Starts an app block builder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.start_app_block_builder)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#start_app_block_builder)
        """

    def start_fleet(self, **kwargs: Unpack[StartFleetRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Starts the specified fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.start_fleet)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#start_fleet)
        """

    def start_image_builder(
        self, **kwargs: Unpack[StartImageBuilderRequestRequestTypeDef]
    ) -> StartImageBuilderResultTypeDef:
        """
        Starts the specified image builder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.start_image_builder)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#start_image_builder)
        """

    def stop_app_block_builder(
        self, **kwargs: Unpack[StopAppBlockBuilderRequestRequestTypeDef]
    ) -> StopAppBlockBuilderResultTypeDef:
        """
        Stops an app block builder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.stop_app_block_builder)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#stop_app_block_builder)
        """

    def stop_fleet(self, **kwargs: Unpack[StopFleetRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Stops the specified fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.stop_fleet)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#stop_fleet)
        """

    def stop_image_builder(
        self, **kwargs: Unpack[StopImageBuilderRequestRequestTypeDef]
    ) -> StopImageBuilderResultTypeDef:
        """
        Stops the specified image builder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.stop_image_builder)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#stop_image_builder)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds or overwrites one or more tags for the specified AppStream 2.0 resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates one or more specified tags from the specified AppStream 2.0
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#untag_resource)
        """

    def update_app_block_builder(
        self, **kwargs: Unpack[UpdateAppBlockBuilderRequestRequestTypeDef]
    ) -> UpdateAppBlockBuilderResultTypeDef:
        """
        Updates an app block builder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.update_app_block_builder)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#update_app_block_builder)
        """

    def update_application(
        self, **kwargs: Unpack[UpdateApplicationRequestRequestTypeDef]
    ) -> UpdateApplicationResultTypeDef:
        """
        Updates the specified application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.update_application)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#update_application)
        """

    def update_directory_config(
        self, **kwargs: Unpack[UpdateDirectoryConfigRequestRequestTypeDef]
    ) -> UpdateDirectoryConfigResultTypeDef:
        """
        Updates the specified Directory Config object in AppStream 2.0.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.update_directory_config)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#update_directory_config)
        """

    def update_entitlement(
        self, **kwargs: Unpack[UpdateEntitlementRequestRequestTypeDef]
    ) -> UpdateEntitlementResultTypeDef:
        """
        Updates the specified entitlement.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.update_entitlement)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#update_entitlement)
        """

    def update_fleet(
        self, **kwargs: Unpack[UpdateFleetRequestRequestTypeDef]
    ) -> UpdateFleetResultTypeDef:
        """
        Updates the specified fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.update_fleet)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#update_fleet)
        """

    def update_image_permissions(
        self, **kwargs: Unpack[UpdateImagePermissionsRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Adds or updates permissions for the specified private image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.update_image_permissions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#update_image_permissions)
        """

    def update_stack(
        self, **kwargs: Unpack[UpdateStackRequestRequestTypeDef]
    ) -> UpdateStackResultTypeDef:
        """
        Updates the specified fields for the specified stack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.update_stack)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#update_stack)
        """

    def update_theme_for_stack(
        self, **kwargs: Unpack[UpdateThemeForStackRequestRequestTypeDef]
    ) -> UpdateThemeForStackResultTypeDef:
        """
        Updates custom branding that customizes the appearance of the streaming
        application catalog
        page.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.update_theme_for_stack)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#update_theme_for_stack)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_directory_configs"]
    ) -> DescribeDirectoryConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_fleets"]) -> DescribeFleetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_image_builders"]
    ) -> DescribeImageBuildersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_images"]) -> DescribeImagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_sessions"]
    ) -> DescribeSessionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_stacks"]) -> DescribeStacksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_user_stack_associations"]
    ) -> DescribeUserStackAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_users"]) -> DescribeUsersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_associated_fleets"]
    ) -> ListAssociatedFleetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_associated_stacks"]
    ) -> ListAssociatedStacksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#get_paginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["fleet_started"]) -> FleetStartedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#get_waiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["fleet_stopped"]) -> FleetStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appstream.html#AppStream.Client.get_waiter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appstream/client/#get_waiter)
        """
