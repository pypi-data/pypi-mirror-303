"""
Type annotations for inspector2 service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_inspector2.client import Inspector2Client

    session = Session()
    client: Inspector2Client = session.client("inspector2")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    GetCisScanResultDetailsPaginator,
    ListAccountPermissionsPaginator,
    ListCisScanConfigurationsPaginator,
    ListCisScanResultsAggregatedByChecksPaginator,
    ListCisScanResultsAggregatedByTargetResourcePaginator,
    ListCisScansPaginator,
    ListCoveragePaginator,
    ListCoverageStatisticsPaginator,
    ListDelegatedAdminAccountsPaginator,
    ListFiltersPaginator,
    ListFindingAggregationsPaginator,
    ListFindingsPaginator,
    ListMembersPaginator,
    ListUsageTotalsPaginator,
    SearchVulnerabilitiesPaginator,
)
from .type_defs import (
    AssociateMemberRequestRequestTypeDef,
    AssociateMemberResponseTypeDef,
    BatchGetAccountStatusRequestRequestTypeDef,
    BatchGetAccountStatusResponseTypeDef,
    BatchGetCodeSnippetRequestRequestTypeDef,
    BatchGetCodeSnippetResponseTypeDef,
    BatchGetFindingDetailsRequestRequestTypeDef,
    BatchGetFindingDetailsResponseTypeDef,
    BatchGetFreeTrialInfoRequestRequestTypeDef,
    BatchGetFreeTrialInfoResponseTypeDef,
    BatchGetMemberEc2DeepInspectionStatusRequestRequestTypeDef,
    BatchGetMemberEc2DeepInspectionStatusResponseTypeDef,
    BatchUpdateMemberEc2DeepInspectionStatusRequestRequestTypeDef,
    BatchUpdateMemberEc2DeepInspectionStatusResponseTypeDef,
    CancelFindingsReportRequestRequestTypeDef,
    CancelFindingsReportResponseTypeDef,
    CancelSbomExportRequestRequestTypeDef,
    CancelSbomExportResponseTypeDef,
    CreateCisScanConfigurationRequestRequestTypeDef,
    CreateCisScanConfigurationResponseTypeDef,
    CreateFilterRequestRequestTypeDef,
    CreateFilterResponseTypeDef,
    CreateFindingsReportRequestRequestTypeDef,
    CreateFindingsReportResponseTypeDef,
    CreateSbomExportRequestRequestTypeDef,
    CreateSbomExportResponseTypeDef,
    DeleteCisScanConfigurationRequestRequestTypeDef,
    DeleteCisScanConfigurationResponseTypeDef,
    DeleteFilterRequestRequestTypeDef,
    DeleteFilterResponseTypeDef,
    DescribeOrganizationConfigurationResponseTypeDef,
    DisableDelegatedAdminAccountRequestRequestTypeDef,
    DisableDelegatedAdminAccountResponseTypeDef,
    DisableRequestRequestTypeDef,
    DisableResponseTypeDef,
    DisassociateMemberRequestRequestTypeDef,
    DisassociateMemberResponseTypeDef,
    EnableDelegatedAdminAccountRequestRequestTypeDef,
    EnableDelegatedAdminAccountResponseTypeDef,
    EnableRequestRequestTypeDef,
    EnableResponseTypeDef,
    GetCisScanReportRequestRequestTypeDef,
    GetCisScanReportResponseTypeDef,
    GetCisScanResultDetailsRequestRequestTypeDef,
    GetCisScanResultDetailsResponseTypeDef,
    GetConfigurationResponseTypeDef,
    GetDelegatedAdminAccountResponseTypeDef,
    GetEc2DeepInspectionConfigurationResponseTypeDef,
    GetEncryptionKeyRequestRequestTypeDef,
    GetEncryptionKeyResponseTypeDef,
    GetFindingsReportStatusRequestRequestTypeDef,
    GetFindingsReportStatusResponseTypeDef,
    GetMemberRequestRequestTypeDef,
    GetMemberResponseTypeDef,
    GetSbomExportRequestRequestTypeDef,
    GetSbomExportResponseTypeDef,
    ListAccountPermissionsRequestRequestTypeDef,
    ListAccountPermissionsResponseTypeDef,
    ListCisScanConfigurationsRequestRequestTypeDef,
    ListCisScanConfigurationsResponseTypeDef,
    ListCisScanResultsAggregatedByChecksRequestRequestTypeDef,
    ListCisScanResultsAggregatedByChecksResponseTypeDef,
    ListCisScanResultsAggregatedByTargetResourceRequestRequestTypeDef,
    ListCisScanResultsAggregatedByTargetResourceResponseTypeDef,
    ListCisScansRequestRequestTypeDef,
    ListCisScansResponseTypeDef,
    ListCoverageRequestRequestTypeDef,
    ListCoverageResponseTypeDef,
    ListCoverageStatisticsRequestRequestTypeDef,
    ListCoverageStatisticsResponseTypeDef,
    ListDelegatedAdminAccountsRequestRequestTypeDef,
    ListDelegatedAdminAccountsResponseTypeDef,
    ListFiltersRequestRequestTypeDef,
    ListFiltersResponseTypeDef,
    ListFindingAggregationsRequestRequestTypeDef,
    ListFindingAggregationsResponseTypeDef,
    ListFindingsRequestRequestTypeDef,
    ListFindingsResponseTypeDef,
    ListMembersRequestRequestTypeDef,
    ListMembersResponseTypeDef,
    ListTagsForResourceRequestRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUsageTotalsRequestRequestTypeDef,
    ListUsageTotalsResponseTypeDef,
    ResetEncryptionKeyRequestRequestTypeDef,
    SearchVulnerabilitiesRequestRequestTypeDef,
    SearchVulnerabilitiesResponseTypeDef,
    SendCisSessionHealthRequestRequestTypeDef,
    SendCisSessionTelemetryRequestRequestTypeDef,
    StartCisSessionRequestRequestTypeDef,
    StopCisSessionRequestRequestTypeDef,
    TagResourceRequestRequestTypeDef,
    UntagResourceRequestRequestTypeDef,
    UpdateCisScanConfigurationRequestRequestTypeDef,
    UpdateCisScanConfigurationResponseTypeDef,
    UpdateConfigurationRequestRequestTypeDef,
    UpdateEc2DeepInspectionConfigurationRequestRequestTypeDef,
    UpdateEc2DeepInspectionConfigurationResponseTypeDef,
    UpdateEncryptionKeyRequestRequestTypeDef,
    UpdateFilterRequestRequestTypeDef,
    UpdateFilterResponseTypeDef,
    UpdateOrganizationConfigurationRequestRequestTypeDef,
    UpdateOrganizationConfigurationResponseTypeDef,
    UpdateOrgEc2DeepInspectionConfigurationRequestRequestTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("Inspector2Client",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class Inspector2Client(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client)
    [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        Inspector2Client exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.exceptions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#exceptions)
        """

    def associate_member(
        self, **kwargs: Unpack[AssociateMemberRequestRequestTypeDef]
    ) -> AssociateMemberResponseTypeDef:
        """
        Associates an Amazon Web Services account with an Amazon Inspector delegated
        administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.associate_member)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#associate_member)
        """

    def batch_get_account_status(
        self, **kwargs: Unpack[BatchGetAccountStatusRequestRequestTypeDef]
    ) -> BatchGetAccountStatusResponseTypeDef:
        """
        Retrieves the Amazon Inspector status of multiple Amazon Web Services accounts
        within your
        environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.batch_get_account_status)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#batch_get_account_status)
        """

    def batch_get_code_snippet(
        self, **kwargs: Unpack[BatchGetCodeSnippetRequestRequestTypeDef]
    ) -> BatchGetCodeSnippetResponseTypeDef:
        """
        Retrieves code snippets from findings that Amazon Inspector detected code
        vulnerabilities
        in.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.batch_get_code_snippet)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#batch_get_code_snippet)
        """

    def batch_get_finding_details(
        self, **kwargs: Unpack[BatchGetFindingDetailsRequestRequestTypeDef]
    ) -> BatchGetFindingDetailsResponseTypeDef:
        """
        Gets vulnerability details for findings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.batch_get_finding_details)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#batch_get_finding_details)
        """

    def batch_get_free_trial_info(
        self, **kwargs: Unpack[BatchGetFreeTrialInfoRequestRequestTypeDef]
    ) -> BatchGetFreeTrialInfoResponseTypeDef:
        """
        Gets free trial status for multiple Amazon Web Services accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.batch_get_free_trial_info)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#batch_get_free_trial_info)
        """

    def batch_get_member_ec2_deep_inspection_status(
        self, **kwargs: Unpack[BatchGetMemberEc2DeepInspectionStatusRequestRequestTypeDef]
    ) -> BatchGetMemberEc2DeepInspectionStatusResponseTypeDef:
        """
        Retrieves Amazon Inspector deep inspection activation status of multiple member
        accounts within your
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.batch_get_member_ec2_deep_inspection_status)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#batch_get_member_ec2_deep_inspection_status)
        """

    def batch_update_member_ec2_deep_inspection_status(
        self, **kwargs: Unpack[BatchUpdateMemberEc2DeepInspectionStatusRequestRequestTypeDef]
    ) -> BatchUpdateMemberEc2DeepInspectionStatusResponseTypeDef:
        """
        Activates or deactivates Amazon Inspector deep inspection for the provided
        member accounts in your
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.batch_update_member_ec2_deep_inspection_status)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#batch_update_member_ec2_deep_inspection_status)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.can_paginate)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#can_paginate)
        """

    def cancel_findings_report(
        self, **kwargs: Unpack[CancelFindingsReportRequestRequestTypeDef]
    ) -> CancelFindingsReportResponseTypeDef:
        """
        Cancels the given findings report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.cancel_findings_report)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#cancel_findings_report)
        """

    def cancel_sbom_export(
        self, **kwargs: Unpack[CancelSbomExportRequestRequestTypeDef]
    ) -> CancelSbomExportResponseTypeDef:
        """
        Cancels a software bill of materials (SBOM) report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.cancel_sbom_export)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#cancel_sbom_export)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.close)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#close)
        """

    def create_cis_scan_configuration(
        self, **kwargs: Unpack[CreateCisScanConfigurationRequestRequestTypeDef]
    ) -> CreateCisScanConfigurationResponseTypeDef:
        """
        Creates a CIS scan configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.create_cis_scan_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#create_cis_scan_configuration)
        """

    def create_filter(
        self, **kwargs: Unpack[CreateFilterRequestRequestTypeDef]
    ) -> CreateFilterResponseTypeDef:
        """
        Creates a filter resource using specified filter criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.create_filter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#create_filter)
        """

    def create_findings_report(
        self, **kwargs: Unpack[CreateFindingsReportRequestRequestTypeDef]
    ) -> CreateFindingsReportResponseTypeDef:
        """
        Creates a finding report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.create_findings_report)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#create_findings_report)
        """

    def create_sbom_export(
        self, **kwargs: Unpack[CreateSbomExportRequestRequestTypeDef]
    ) -> CreateSbomExportResponseTypeDef:
        """
        Creates a software bill of materials (SBOM) report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.create_sbom_export)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#create_sbom_export)
        """

    def delete_cis_scan_configuration(
        self, **kwargs: Unpack[DeleteCisScanConfigurationRequestRequestTypeDef]
    ) -> DeleteCisScanConfigurationResponseTypeDef:
        """
        Deletes a CIS scan configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.delete_cis_scan_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#delete_cis_scan_configuration)
        """

    def delete_filter(
        self, **kwargs: Unpack[DeleteFilterRequestRequestTypeDef]
    ) -> DeleteFilterResponseTypeDef:
        """
        Deletes a filter resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.delete_filter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#delete_filter)
        """

    def describe_organization_configuration(
        self,
    ) -> DescribeOrganizationConfigurationResponseTypeDef:
        """
        Describe Amazon Inspector configuration settings for an Amazon Web Services
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.describe_organization_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#describe_organization_configuration)
        """

    def disable(self, **kwargs: Unpack[DisableRequestRequestTypeDef]) -> DisableResponseTypeDef:
        """
        Disables Amazon Inspector scans for one or more Amazon Web Services accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.disable)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#disable)
        """

    def disable_delegated_admin_account(
        self, **kwargs: Unpack[DisableDelegatedAdminAccountRequestRequestTypeDef]
    ) -> DisableDelegatedAdminAccountResponseTypeDef:
        """
        Disables the Amazon Inspector delegated administrator for your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.disable_delegated_admin_account)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#disable_delegated_admin_account)
        """

    def disassociate_member(
        self, **kwargs: Unpack[DisassociateMemberRequestRequestTypeDef]
    ) -> DisassociateMemberResponseTypeDef:
        """
        Disassociates a member account from an Amazon Inspector delegated administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.disassociate_member)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#disassociate_member)
        """

    def enable(self, **kwargs: Unpack[EnableRequestRequestTypeDef]) -> EnableResponseTypeDef:
        """
        Enables Amazon Inspector scans for one or more Amazon Web Services accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.enable)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#enable)
        """

    def enable_delegated_admin_account(
        self, **kwargs: Unpack[EnableDelegatedAdminAccountRequestRequestTypeDef]
    ) -> EnableDelegatedAdminAccountResponseTypeDef:
        """
        Enables the Amazon Inspector delegated administrator for your Organizations
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.enable_delegated_admin_account)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#enable_delegated_admin_account)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.generate_presigned_url)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#generate_presigned_url)
        """

    def get_cis_scan_report(
        self, **kwargs: Unpack[GetCisScanReportRequestRequestTypeDef]
    ) -> GetCisScanReportResponseTypeDef:
        """
        Retrieves a CIS scan report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_cis_scan_report)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#get_cis_scan_report)
        """

    def get_cis_scan_result_details(
        self, **kwargs: Unpack[GetCisScanResultDetailsRequestRequestTypeDef]
    ) -> GetCisScanResultDetailsResponseTypeDef:
        """
        Retrieves CIS scan result details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_cis_scan_result_details)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#get_cis_scan_result_details)
        """

    def get_configuration(self) -> GetConfigurationResponseTypeDef:
        """
        Retrieves setting configurations for Inspector scans.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#get_configuration)
        """

    def get_delegated_admin_account(self) -> GetDelegatedAdminAccountResponseTypeDef:
        """
        Retrieves information about the Amazon Inspector delegated administrator for
        your
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_delegated_admin_account)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#get_delegated_admin_account)
        """

    def get_ec2_deep_inspection_configuration(
        self,
    ) -> GetEc2DeepInspectionConfigurationResponseTypeDef:
        """
        Retrieves the activation status of Amazon Inspector deep inspection and custom
        paths associated with your
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_ec2_deep_inspection_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#get_ec2_deep_inspection_configuration)
        """

    def get_encryption_key(
        self, **kwargs: Unpack[GetEncryptionKeyRequestRequestTypeDef]
    ) -> GetEncryptionKeyResponseTypeDef:
        """
        Gets an encryption key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_encryption_key)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#get_encryption_key)
        """

    def get_findings_report_status(
        self, **kwargs: Unpack[GetFindingsReportStatusRequestRequestTypeDef]
    ) -> GetFindingsReportStatusResponseTypeDef:
        """
        Gets the status of a findings report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_findings_report_status)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#get_findings_report_status)
        """

    def get_member(
        self, **kwargs: Unpack[GetMemberRequestRequestTypeDef]
    ) -> GetMemberResponseTypeDef:
        """
        Gets member information for your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_member)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#get_member)
        """

    def get_sbom_export(
        self, **kwargs: Unpack[GetSbomExportRequestRequestTypeDef]
    ) -> GetSbomExportResponseTypeDef:
        """
        Gets details of a software bill of materials (SBOM) report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_sbom_export)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#get_sbom_export)
        """

    def list_account_permissions(
        self, **kwargs: Unpack[ListAccountPermissionsRequestRequestTypeDef]
    ) -> ListAccountPermissionsResponseTypeDef:
        """
        Lists the permissions an account has to configure Amazon Inspector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.list_account_permissions)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#list_account_permissions)
        """

    def list_cis_scan_configurations(
        self, **kwargs: Unpack[ListCisScanConfigurationsRequestRequestTypeDef]
    ) -> ListCisScanConfigurationsResponseTypeDef:
        """
        Lists CIS scan configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.list_cis_scan_configurations)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#list_cis_scan_configurations)
        """

    def list_cis_scan_results_aggregated_by_checks(
        self, **kwargs: Unpack[ListCisScanResultsAggregatedByChecksRequestRequestTypeDef]
    ) -> ListCisScanResultsAggregatedByChecksResponseTypeDef:
        """
        Lists scan results aggregated by checks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.list_cis_scan_results_aggregated_by_checks)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#list_cis_scan_results_aggregated_by_checks)
        """

    def list_cis_scan_results_aggregated_by_target_resource(
        self, **kwargs: Unpack[ListCisScanResultsAggregatedByTargetResourceRequestRequestTypeDef]
    ) -> ListCisScanResultsAggregatedByTargetResourceResponseTypeDef:
        """
        Lists scan results aggregated by a target resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.list_cis_scan_results_aggregated_by_target_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#list_cis_scan_results_aggregated_by_target_resource)
        """

    def list_cis_scans(
        self, **kwargs: Unpack[ListCisScansRequestRequestTypeDef]
    ) -> ListCisScansResponseTypeDef:
        """
        Returns a CIS scan list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.list_cis_scans)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#list_cis_scans)
        """

    def list_coverage(
        self, **kwargs: Unpack[ListCoverageRequestRequestTypeDef]
    ) -> ListCoverageResponseTypeDef:
        """
        Lists coverage details for you environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.list_coverage)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#list_coverage)
        """

    def list_coverage_statistics(
        self, **kwargs: Unpack[ListCoverageStatisticsRequestRequestTypeDef]
    ) -> ListCoverageStatisticsResponseTypeDef:
        """
        Lists Amazon Inspector coverage statistics for your environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.list_coverage_statistics)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#list_coverage_statistics)
        """

    def list_delegated_admin_accounts(
        self, **kwargs: Unpack[ListDelegatedAdminAccountsRequestRequestTypeDef]
    ) -> ListDelegatedAdminAccountsResponseTypeDef:
        """
        Lists information about the Amazon Inspector delegated administrator of your
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.list_delegated_admin_accounts)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#list_delegated_admin_accounts)
        """

    def list_filters(
        self, **kwargs: Unpack[ListFiltersRequestRequestTypeDef]
    ) -> ListFiltersResponseTypeDef:
        """
        Lists the filters associated with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.list_filters)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#list_filters)
        """

    def list_finding_aggregations(
        self, **kwargs: Unpack[ListFindingAggregationsRequestRequestTypeDef]
    ) -> ListFindingAggregationsResponseTypeDef:
        """
        Lists aggregated finding data for your environment based on specific criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.list_finding_aggregations)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#list_finding_aggregations)
        """

    def list_findings(
        self, **kwargs: Unpack[ListFindingsRequestRequestTypeDef]
    ) -> ListFindingsResponseTypeDef:
        """
        Lists findings for your environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.list_findings)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#list_findings)
        """

    def list_members(
        self, **kwargs: Unpack[ListMembersRequestRequestTypeDef]
    ) -> ListMembersResponseTypeDef:
        """
        List members associated with the Amazon Inspector delegated administrator for
        your
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.list_members)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#list_members)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all tags attached to a given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.list_tags_for_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#list_tags_for_resource)
        """

    def list_usage_totals(
        self, **kwargs: Unpack[ListUsageTotalsRequestRequestTypeDef]
    ) -> ListUsageTotalsResponseTypeDef:
        """
        Lists the Amazon Inspector usage totals over the last 30 days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.list_usage_totals)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#list_usage_totals)
        """

    def reset_encryption_key(
        self, **kwargs: Unpack[ResetEncryptionKeyRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Resets an encryption key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.reset_encryption_key)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#reset_encryption_key)
        """

    def search_vulnerabilities(
        self, **kwargs: Unpack[SearchVulnerabilitiesRequestRequestTypeDef]
    ) -> SearchVulnerabilitiesResponseTypeDef:
        """
        Lists Amazon Inspector coverage details for a specific vulnerability.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.search_vulnerabilities)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#search_vulnerabilities)
        """

    def send_cis_session_health(
        self, **kwargs: Unpack[SendCisSessionHealthRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Sends a CIS session health.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.send_cis_session_health)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#send_cis_session_health)
        """

    def send_cis_session_telemetry(
        self, **kwargs: Unpack[SendCisSessionTelemetryRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Sends a CIS session telemetry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.send_cis_session_telemetry)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#send_cis_session_telemetry)
        """

    def start_cis_session(
        self, **kwargs: Unpack[StartCisSessionRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Starts a CIS session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.start_cis_session)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#start_cis_session)
        """

    def stop_cis_session(
        self, **kwargs: Unpack[StopCisSessionRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Stops a CIS session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.stop_cis_session)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#stop_cis_session)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.tag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.untag_resource)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#untag_resource)
        """

    def update_cis_scan_configuration(
        self, **kwargs: Unpack[UpdateCisScanConfigurationRequestRequestTypeDef]
    ) -> UpdateCisScanConfigurationResponseTypeDef:
        """
        Updates a CIS scan configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.update_cis_scan_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#update_cis_scan_configuration)
        """

    def update_configuration(
        self, **kwargs: Unpack[UpdateConfigurationRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates setting configurations for your Amazon Inspector account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.update_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#update_configuration)
        """

    def update_ec2_deep_inspection_configuration(
        self, **kwargs: Unpack[UpdateEc2DeepInspectionConfigurationRequestRequestTypeDef]
    ) -> UpdateEc2DeepInspectionConfigurationResponseTypeDef:
        """
        Activates, deactivates Amazon Inspector deep inspection, or updates custom
        paths for your
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.update_ec2_deep_inspection_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#update_ec2_deep_inspection_configuration)
        """

    def update_encryption_key(
        self, **kwargs: Unpack[UpdateEncryptionKeyRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates an encryption key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.update_encryption_key)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#update_encryption_key)
        """

    def update_filter(
        self, **kwargs: Unpack[UpdateFilterRequestRequestTypeDef]
    ) -> UpdateFilterResponseTypeDef:
        """
        Specifies the action that is to be applied to the findings that match the
        filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.update_filter)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#update_filter)
        """

    def update_org_ec2_deep_inspection_configuration(
        self, **kwargs: Unpack[UpdateOrgEc2DeepInspectionConfigurationRequestRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the Amazon Inspector deep inspection custom paths for your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.update_org_ec2_deep_inspection_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#update_org_ec2_deep_inspection_configuration)
        """

    def update_organization_configuration(
        self, **kwargs: Unpack[UpdateOrganizationConfigurationRequestRequestTypeDef]
    ) -> UpdateOrganizationConfigurationResponseTypeDef:
        """
        Updates the configurations for your Amazon Inspector organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.update_organization_configuration)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#update_organization_configuration)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_cis_scan_result_details"]
    ) -> GetCisScanResultDetailsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_account_permissions"]
    ) -> ListAccountPermissionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_cis_scan_configurations"]
    ) -> ListCisScanConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_cis_scan_results_aggregated_by_checks"]
    ) -> ListCisScanResultsAggregatedByChecksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_cis_scan_results_aggregated_by_target_resource"]
    ) -> ListCisScanResultsAggregatedByTargetResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_cis_scans"]) -> ListCisScansPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_coverage"]) -> ListCoveragePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_coverage_statistics"]
    ) -> ListCoverageStatisticsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_delegated_admin_accounts"]
    ) -> ListDelegatedAdminAccountsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_filters"]) -> ListFiltersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_finding_aggregations"]
    ) -> ListFindingAggregationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_findings"]) -> ListFindingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_members"]) -> ListMembersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_usage_totals"]
    ) -> ListUsageTotalsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_vulnerabilities"]
    ) -> SearchVulnerabilitiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector2.html#Inspector2.Client.get_paginator)
        [Show boto3-stubs-full documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector2/client/#get_paginator)
        """
