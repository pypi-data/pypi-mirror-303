"""
Type annotations for shield service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_shield.client import ShieldClient

    session = Session()
    client: ShieldClient = session.client("shield")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import ListAttacksPaginator, ListProtectionsPaginator
from .type_defs import (
    AssociateDRTLogBucketRequestRequestTypeDef,
    AssociateDRTRoleRequestRequestTypeDef,
    AssociateHealthCheckRequestRequestTypeDef,
    AssociateProactiveEngagementDetailsRequestRequestTypeDef,
    CreateProtectionGroupRequestRequestTypeDef,
    CreateProtectionRequestRequestTypeDef,
    CreateProtectionResponseTypeDef,
    DeleteProtectionGroupRequestRequestTypeDef,
    DeleteProtectionRequestRequestTypeDef,
    DescribeAttackRequestRequestTypeDef,
    DescribeAttackResponseTypeDef,
    DescribeAttackStatisticsResponseTypeDef,
    DescribeDRTAccessResponseTypeDef,
    DescribeEmergencyContactSettingsResponseTypeDef,
    DescribeProtectionGroupRequestRequestTypeDef,
    DescribeProtectionGroupResponseTypeDef,
    DescribeProtectionRequestRequestTypeDef,
    DescribeProtectionResponseTypeDef,
    DescribeSubscriptionResponseTypeDef,
    DisableApplicationLayerAutomaticResponseRequestRequestTypeDef,
    DisassociateDRTLogBucketRequestRequestTypeDef,
    DisassociateHealthCheckRequestRequestTypeDef,
    EnableApplicationLayerAutomaticResponseRequestRequestTypeDef,
    GetSubscriptionStateResponseTypeDef,
    ListAttacksRequestRequestTypeDef,
    ListAttacksResponseTypeDef,
    ListProtectionGroupsRequestRequestTypeDef,
    ListProtectionGroupsResponseTypeDef,
    ListProtectionsRequestRequestTypeDef,
    ListProtectionsResponseTypeDef,
    ListResourcesInProtectionGroupRequestRequestTypeDef,
    ListResourcesInProtectionGroupResponseTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    TagResourceRequestRequestTypeDef,
    UntagResourceRequestRequestTypeDef,
    UpdateApplicationLayerAutomaticResponseRequestRequestTypeDef,
    UpdateEmergencyContactSettingsRequestRequestTypeDef,
    UpdateProtectionGroupRequestRequestTypeDef,
    UpdateSubscriptionRequestRequestTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("ShieldClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    AccessDeniedForDependencyException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalErrorException: Type[BotocoreClientError]
    InvalidOperationException: Type[BotocoreClientError]
    InvalidPaginationTokenException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidResourceException: Type[BotocoreClientError]
    LimitsExceededException: Type[BotocoreClientError]
    LockedSubscriptionException: Type[BotocoreClientError]
    NoAssociatedRoleException: Type[BotocoreClientError]
    OptimisticLockException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]

class ShieldClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ShieldClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#exceptions)
        """

    def associate_drt_log_bucket(
        self, **kwargs: Unpack[AssociateDRTLogBucketRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Authorizes the Shield Response Team (SRT) to access the specified Amazon S3
        bucket containing log data such as Application Load Balancer access logs,
        CloudFront logs, or logs from third party
        sources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.associate_drt_log_bucket)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#associate_drt_log_bucket)
        """

    def associate_drt_role(
        self, **kwargs: Unpack[AssociateDRTRoleRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Authorizes the Shield Response Team (SRT) using the specified role, to access
        your Amazon Web Services account to assist with DDoS attack mitigation during
        potential
        attacks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.associate_drt_role)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#associate_drt_role)
        """

    def associate_health_check(
        self, **kwargs: Unpack[AssociateHealthCheckRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Adds health-based detection to the Shield Advanced protection for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.associate_health_check)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#associate_health_check)
        """

    def associate_proactive_engagement_details(
        self, **kwargs: Unpack[AssociateProactiveEngagementDetailsRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Initializes proactive engagement and sets the list of contacts for the Shield
        Response Team (SRT) to
        use.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.associate_proactive_engagement_details)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#associate_proactive_engagement_details)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#close)
        """

    def create_protection(
        self, **kwargs: Unpack[CreateProtectionRequestRequestTypeDef]
    ) -> CreateProtectionResponseTypeDef:
        """
        Enables Shield Advanced for a specific Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.create_protection)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#create_protection)
        """

    def create_protection_group(
        self, **kwargs: Unpack[CreateProtectionGroupRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates a grouping of protected resources so they can be handled as a
        collective.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.create_protection_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#create_protection_group)
        """

    def create_subscription(self) -> Dict[str, Any]:
        """
        Activates Shield Advanced for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.create_subscription)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#create_subscription)
        """

    def delete_protection(
        self, **kwargs: Unpack[DeleteProtectionRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an Shield Advanced  Protection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.delete_protection)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#delete_protection)
        """

    def delete_protection_group(
        self, **kwargs: Unpack[DeleteProtectionGroupRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes the specified protection group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.delete_protection_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#delete_protection_group)
        """

    def delete_subscription(self) -> Dict[str, Any]:
        """
        Removes Shield Advanced from an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.delete_subscription)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#delete_subscription)
        """

    def describe_attack(
        self, **kwargs: Unpack[DescribeAttackRequestRequestTypeDef]
    ) -> DescribeAttackResponseTypeDef:
        """
        Describes the details of a DDoS attack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.describe_attack)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#describe_attack)
        """

    def describe_attack_statistics(self) -> DescribeAttackStatisticsResponseTypeDef:
        """
        Provides information about the number and type of attacks Shield has detected
        in the last year for all resources that belong to your account, regardless of
        whether you've defined Shield protections for
        them.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.describe_attack_statistics)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#describe_attack_statistics)
        """

    def describe_drt_access(self) -> DescribeDRTAccessResponseTypeDef:
        """
        Returns the current role and list of Amazon S3 log buckets used by the Shield
        Response Team (SRT) to access your Amazon Web Services account while assisting
        with attack
        mitigation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.describe_drt_access)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#describe_drt_access)
        """

    def describe_emergency_contact_settings(
        self,
    ) -> DescribeEmergencyContactSettingsResponseTypeDef:
        """
        A list of email addresses and phone numbers that the Shield Response Team (SRT)
        can use to contact you if you have proactive engagement enabled, for
        escalations to the SRT and to initiate proactive customer
        support.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.describe_emergency_contact_settings)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#describe_emergency_contact_settings)
        """

    def describe_protection(
        self, **kwargs: Unpack[DescribeProtectionRequestRequestTypeDef]
    ) -> DescribeProtectionResponseTypeDef:
        """
        Lists the details of a  Protection object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.describe_protection)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#describe_protection)
        """

    def describe_protection_group(
        self, **kwargs: Unpack[DescribeProtectionGroupRequestRequestTypeDef]
    ) -> DescribeProtectionGroupResponseTypeDef:
        """
        Returns the specification for the specified protection group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.describe_protection_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#describe_protection_group)
        """

    def describe_subscription(self) -> DescribeSubscriptionResponseTypeDef:
        """
        Provides details about the Shield Advanced subscription for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.describe_subscription)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#describe_subscription)
        """

    def disable_application_layer_automatic_response(
        self, **kwargs: Unpack[DisableApplicationLayerAutomaticResponseRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disable the Shield Advanced automatic application layer DDoS mitigation feature
        for the protected
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.disable_application_layer_automatic_response)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#disable_application_layer_automatic_response)
        """

    def disable_proactive_engagement(self) -> Dict[str, Any]:
        """
        Removes authorization from the Shield Response Team (SRT) to notify contacts
        about escalations to the SRT and to initiate proactive customer
        support.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.disable_proactive_engagement)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#disable_proactive_engagement)
        """

    def disassociate_drt_log_bucket(
        self, **kwargs: Unpack[DisassociateDRTLogBucketRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes the Shield Response Team's (SRT) access to the specified Amazon S3
        bucket containing the logs that you shared
        previously.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.disassociate_drt_log_bucket)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#disassociate_drt_log_bucket)
        """

    def disassociate_drt_role(self) -> Dict[str, Any]:
        """
        Removes the Shield Response Team's (SRT) access to your Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.disassociate_drt_role)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#disassociate_drt_role)
        """

    def disassociate_health_check(
        self, **kwargs: Unpack[DisassociateHealthCheckRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes health-based detection from the Shield Advanced protection for a
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.disassociate_health_check)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#disassociate_health_check)
        """

    def enable_application_layer_automatic_response(
        self, **kwargs: Unpack[EnableApplicationLayerAutomaticResponseRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Enable the Shield Advanced automatic application layer DDoS mitigation for the
        protected
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.enable_application_layer_automatic_response)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#enable_application_layer_automatic_response)
        """

    def enable_proactive_engagement(self) -> Dict[str, Any]:
        """
        Authorizes the Shield Response Team (SRT) to use email and phone to notify
        contacts about escalations to the SRT and to initiate proactive customer
        support.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.enable_proactive_engagement)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#enable_proactive_engagement)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#generate_presigned_url)
        """

    def get_subscription_state(self) -> GetSubscriptionStateResponseTypeDef:
        """
        Returns the `SubscriptionState`, either `Active` or `Inactive`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.get_subscription_state)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#get_subscription_state)
        """

    def list_attacks(
        self, **kwargs: Unpack[ListAttacksRequestRequestTypeDef]
    ) -> ListAttacksResponseTypeDef:
        """
        Returns all ongoing DDoS attacks or all DDoS attacks during a specified time
        period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.list_attacks)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#list_attacks)
        """

    def list_protection_groups(
        self, **kwargs: Unpack[ListProtectionGroupsRequestRequestTypeDef]
    ) -> ListProtectionGroupsResponseTypeDef:
        """
        Retrieves  ProtectionGroup objects for the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.list_protection_groups)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#list_protection_groups)
        """

    def list_protections(
        self, **kwargs: Unpack[ListProtectionsRequestRequestTypeDef]
    ) -> ListProtectionsResponseTypeDef:
        """
        Retrieves  Protection objects for the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.list_protections)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#list_protections)
        """

    def list_resources_in_protection_group(
        self, **kwargs: Unpack[ListResourcesInProtectionGroupRequestRequestTypeDef]
    ) -> ListResourcesInProtectionGroupResponseTypeDef:
        """
        Retrieves the resources that are included in the protection group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.list_resources_in_protection_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#list_resources_in_protection_group)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Gets information about Amazon Web Services tags for a specified Amazon Resource
        Name (ARN) in
        Shield.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.list_tags_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#list_tags_for_resource)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds or updates tags for a resource in Shield.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes tags from a resource in Shield.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#untag_resource)
        """

    def update_application_layer_automatic_response(
        self, **kwargs: Unpack[UpdateApplicationLayerAutomaticResponseRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates an existing Shield Advanced automatic application layer DDoS mitigation
        configuration for the specified
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.update_application_layer_automatic_response)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#update_application_layer_automatic_response)
        """

    def update_emergency_contact_settings(
        self, **kwargs: Unpack[UpdateEmergencyContactSettingsRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the details of the list of email addresses and phone numbers that the
        Shield Response Team (SRT) can use to contact you if you have proactive
        engagement enabled, for escalations to the SRT and to initiate proactive
        customer
        support.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.update_emergency_contact_settings)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#update_emergency_contact_settings)
        """

    def update_protection_group(
        self, **kwargs: Unpack[UpdateProtectionGroupRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates an existing protection group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.update_protection_group)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#update_protection_group)
        """

    def update_subscription(
        self, **kwargs: Unpack[UpdateSubscriptionRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the details of an existing subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.update_subscription)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#update_subscription)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_attacks"]) -> ListAttacksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_protections"]
    ) -> ListProtectionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#get_paginator)
        """
