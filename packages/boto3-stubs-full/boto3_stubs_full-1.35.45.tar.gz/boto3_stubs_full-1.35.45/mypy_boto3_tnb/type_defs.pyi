"""
Type annotations for tnb service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/type_defs/)

Usage::

    ```python
    from mypy_boto3_tnb.type_defs import BlobTypeDef

    data: BlobTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    LcmOperationTypeType,
    NsdOnboardingStateType,
    NsdOperationalStateType,
    NsdUsageStateType,
    NsLcmOperationStateType,
    NsStateType,
    OnboardingStateType,
    OperationalStateType,
    TaskStatusType,
    UpdateSolNetworkTypeType,
    UsageStateType,
    VnfInstantiationStateType,
    VnfOperationalStateType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "BlobTypeDef",
    "CancelSolNetworkOperationInputRequestTypeDef",
    "CreateSolFunctionPackageInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CreateSolNetworkInstanceInputRequestTypeDef",
    "CreateSolNetworkPackageInputRequestTypeDef",
    "DeleteSolFunctionPackageInputRequestTypeDef",
    "DeleteSolNetworkInstanceInputRequestTypeDef",
    "DeleteSolNetworkPackageInputRequestTypeDef",
    "ErrorInfoTypeDef",
    "ToscaOverrideTypeDef",
    "GetSolFunctionInstanceInputRequestTypeDef",
    "GetSolFunctionInstanceMetadataTypeDef",
    "GetSolFunctionPackageContentInputRequestTypeDef",
    "GetSolFunctionPackageDescriptorInputRequestTypeDef",
    "GetSolFunctionPackageInputRequestTypeDef",
    "GetSolInstantiatedVnfInfoTypeDef",
    "GetSolNetworkInstanceInputRequestTypeDef",
    "GetSolNetworkInstanceMetadataTypeDef",
    "LcmOperationInfoTypeDef",
    "GetSolNetworkOperationInputRequestTypeDef",
    "InstantiateMetadataTypeDef",
    "ModifyVnfInfoMetadataTypeDef",
    "UpdateNsMetadataTypeDef",
    "ProblemDetailsTypeDef",
    "GetSolNetworkPackageContentInputRequestTypeDef",
    "GetSolNetworkPackageDescriptorInputRequestTypeDef",
    "GetSolNetworkPackageInputRequestTypeDef",
    "GetSolVnfcResourceInfoMetadataTypeDef",
    "InstantiateSolNetworkInstanceInputRequestTypeDef",
    "ListSolFunctionInstanceMetadataTypeDef",
    "PaginatorConfigTypeDef",
    "ListSolFunctionInstancesInputRequestTypeDef",
    "ListSolFunctionPackageMetadataTypeDef",
    "ListSolFunctionPackagesInputRequestTypeDef",
    "ListSolNetworkInstanceMetadataTypeDef",
    "ListSolNetworkInstancesInputRequestTypeDef",
    "ListSolNetworkOperationsMetadataTypeDef",
    "ListSolNetworkOperationsInputRequestTypeDef",
    "ListSolNetworkPackageMetadataTypeDef",
    "ListSolNetworkPackagesInputRequestTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "TerminateSolNetworkInstanceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateSolFunctionPackageInputRequestTypeDef",
    "UpdateSolNetworkModifyTypeDef",
    "UpdateSolNetworkServiceDataTypeDef",
    "UpdateSolNetworkPackageInputRequestTypeDef",
    "PutSolFunctionPackageContentInputRequestTypeDef",
    "PutSolNetworkPackageContentInputRequestTypeDef",
    "ValidateSolFunctionPackageContentInputRequestTypeDef",
    "ValidateSolNetworkPackageContentInputRequestTypeDef",
    "CreateSolFunctionPackageOutputTypeDef",
    "CreateSolNetworkInstanceOutputTypeDef",
    "CreateSolNetworkPackageOutputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetSolFunctionPackageContentOutputTypeDef",
    "GetSolFunctionPackageDescriptorOutputTypeDef",
    "GetSolNetworkPackageContentOutputTypeDef",
    "GetSolNetworkPackageDescriptorOutputTypeDef",
    "InstantiateSolNetworkInstanceOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "TerminateSolNetworkInstanceOutputTypeDef",
    "UpdateSolFunctionPackageOutputTypeDef",
    "UpdateSolNetworkInstanceOutputTypeDef",
    "UpdateSolNetworkPackageOutputTypeDef",
    "GetSolNetworkOperationTaskDetailsTypeDef",
    "FunctionArtifactMetaTypeDef",
    "NetworkArtifactMetaTypeDef",
    "GetSolNetworkInstanceOutputTypeDef",
    "GetSolNetworkOperationMetadataTypeDef",
    "GetSolVnfcResourceInfoTypeDef",
    "ListSolFunctionInstanceInfoTypeDef",
    "ListSolFunctionInstancesInputListSolFunctionInstancesPaginateTypeDef",
    "ListSolFunctionPackagesInputListSolFunctionPackagesPaginateTypeDef",
    "ListSolNetworkInstancesInputListSolNetworkInstancesPaginateTypeDef",
    "ListSolNetworkOperationsInputListSolNetworkOperationsPaginateTypeDef",
    "ListSolNetworkPackagesInputListSolNetworkPackagesPaginateTypeDef",
    "ListSolFunctionPackageInfoTypeDef",
    "ListSolNetworkInstanceInfoTypeDef",
    "ListSolNetworkOperationsInfoTypeDef",
    "ListSolNetworkPackageInfoTypeDef",
    "UpdateSolNetworkInstanceInputRequestTypeDef",
    "GetSolFunctionPackageMetadataTypeDef",
    "PutSolFunctionPackageContentMetadataTypeDef",
    "ValidateSolFunctionPackageContentMetadataTypeDef",
    "GetSolNetworkPackageMetadataTypeDef",
    "PutSolNetworkPackageContentMetadataTypeDef",
    "ValidateSolNetworkPackageContentMetadataTypeDef",
    "GetSolNetworkOperationOutputTypeDef",
    "GetSolVnfInfoTypeDef",
    "ListSolFunctionInstancesOutputTypeDef",
    "ListSolFunctionPackagesOutputTypeDef",
    "ListSolNetworkInstancesOutputTypeDef",
    "ListSolNetworkOperationsOutputTypeDef",
    "ListSolNetworkPackagesOutputTypeDef",
    "GetSolFunctionPackageOutputTypeDef",
    "PutSolFunctionPackageContentOutputTypeDef",
    "ValidateSolFunctionPackageContentOutputTypeDef",
    "GetSolNetworkPackageOutputTypeDef",
    "PutSolNetworkPackageContentOutputTypeDef",
    "ValidateSolNetworkPackageContentOutputTypeDef",
    "GetSolFunctionInstanceOutputTypeDef",
)

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
CancelSolNetworkOperationInputRequestTypeDef = TypedDict(
    "CancelSolNetworkOperationInputRequestTypeDef",
    {
        "nsLcmOpOccId": str,
    },
)
CreateSolFunctionPackageInputRequestTypeDef = TypedDict(
    "CreateSolFunctionPackageInputRequestTypeDef",
    {
        "tags": NotRequired[Mapping[str, str]],
    },
)
ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
        "HostId": NotRequired[str],
    },
)
CreateSolNetworkInstanceInputRequestTypeDef = TypedDict(
    "CreateSolNetworkInstanceInputRequestTypeDef",
    {
        "nsName": str,
        "nsdInfoId": str,
        "nsDescription": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateSolNetworkPackageInputRequestTypeDef = TypedDict(
    "CreateSolNetworkPackageInputRequestTypeDef",
    {
        "tags": NotRequired[Mapping[str, str]],
    },
)
DeleteSolFunctionPackageInputRequestTypeDef = TypedDict(
    "DeleteSolFunctionPackageInputRequestTypeDef",
    {
        "vnfPkgId": str,
    },
)
DeleteSolNetworkInstanceInputRequestTypeDef = TypedDict(
    "DeleteSolNetworkInstanceInputRequestTypeDef",
    {
        "nsInstanceId": str,
    },
)
DeleteSolNetworkPackageInputRequestTypeDef = TypedDict(
    "DeleteSolNetworkPackageInputRequestTypeDef",
    {
        "nsdInfoId": str,
    },
)
ErrorInfoTypeDef = TypedDict(
    "ErrorInfoTypeDef",
    {
        "cause": NotRequired[str],
        "details": NotRequired[str],
    },
)
ToscaOverrideTypeDef = TypedDict(
    "ToscaOverrideTypeDef",
    {
        "defaultValue": NotRequired[str],
        "name": NotRequired[str],
    },
)
GetSolFunctionInstanceInputRequestTypeDef = TypedDict(
    "GetSolFunctionInstanceInputRequestTypeDef",
    {
        "vnfInstanceId": str,
    },
)
GetSolFunctionInstanceMetadataTypeDef = TypedDict(
    "GetSolFunctionInstanceMetadataTypeDef",
    {
        "createdAt": datetime,
        "lastModified": datetime,
    },
)
GetSolFunctionPackageContentInputRequestTypeDef = TypedDict(
    "GetSolFunctionPackageContentInputRequestTypeDef",
    {
        "accept": Literal["application/zip"],
        "vnfPkgId": str,
    },
)
GetSolFunctionPackageDescriptorInputRequestTypeDef = TypedDict(
    "GetSolFunctionPackageDescriptorInputRequestTypeDef",
    {
        "accept": Literal["text/plain"],
        "vnfPkgId": str,
    },
)
GetSolFunctionPackageInputRequestTypeDef = TypedDict(
    "GetSolFunctionPackageInputRequestTypeDef",
    {
        "vnfPkgId": str,
    },
)
GetSolInstantiatedVnfInfoTypeDef = TypedDict(
    "GetSolInstantiatedVnfInfoTypeDef",
    {
        "vnfState": NotRequired[VnfOperationalStateType],
    },
)
GetSolNetworkInstanceInputRequestTypeDef = TypedDict(
    "GetSolNetworkInstanceInputRequestTypeDef",
    {
        "nsInstanceId": str,
    },
)
GetSolNetworkInstanceMetadataTypeDef = TypedDict(
    "GetSolNetworkInstanceMetadataTypeDef",
    {
        "createdAt": datetime,
        "lastModified": datetime,
    },
)
LcmOperationInfoTypeDef = TypedDict(
    "LcmOperationInfoTypeDef",
    {
        "nsLcmOpOccId": str,
    },
)
GetSolNetworkOperationInputRequestTypeDef = TypedDict(
    "GetSolNetworkOperationInputRequestTypeDef",
    {
        "nsLcmOpOccId": str,
    },
)
InstantiateMetadataTypeDef = TypedDict(
    "InstantiateMetadataTypeDef",
    {
        "nsdInfoId": str,
        "additionalParamsForNs": NotRequired[Dict[str, Any]],
    },
)
ModifyVnfInfoMetadataTypeDef = TypedDict(
    "ModifyVnfInfoMetadataTypeDef",
    {
        "vnfConfigurableProperties": Dict[str, Any],
        "vnfInstanceId": str,
    },
)
UpdateNsMetadataTypeDef = TypedDict(
    "UpdateNsMetadataTypeDef",
    {
        "nsdInfoId": str,
        "additionalParamsForNs": NotRequired[Dict[str, Any]],
    },
)
ProblemDetailsTypeDef = TypedDict(
    "ProblemDetailsTypeDef",
    {
        "detail": str,
        "title": NotRequired[str],
    },
)
GetSolNetworkPackageContentInputRequestTypeDef = TypedDict(
    "GetSolNetworkPackageContentInputRequestTypeDef",
    {
        "accept": Literal["application/zip"],
        "nsdInfoId": str,
    },
)
GetSolNetworkPackageDescriptorInputRequestTypeDef = TypedDict(
    "GetSolNetworkPackageDescriptorInputRequestTypeDef",
    {
        "nsdInfoId": str,
    },
)
GetSolNetworkPackageInputRequestTypeDef = TypedDict(
    "GetSolNetworkPackageInputRequestTypeDef",
    {
        "nsdInfoId": str,
    },
)
GetSolVnfcResourceInfoMetadataTypeDef = TypedDict(
    "GetSolVnfcResourceInfoMetadataTypeDef",
    {
        "cluster": NotRequired[str],
        "helmChart": NotRequired[str],
        "nodeGroup": NotRequired[str],
    },
)
InstantiateSolNetworkInstanceInputRequestTypeDef = TypedDict(
    "InstantiateSolNetworkInstanceInputRequestTypeDef",
    {
        "nsInstanceId": str,
        "additionalParamsForNs": NotRequired[Mapping[str, Any]],
        "dryRun": NotRequired[bool],
        "tags": NotRequired[Mapping[str, str]],
    },
)
ListSolFunctionInstanceMetadataTypeDef = TypedDict(
    "ListSolFunctionInstanceMetadataTypeDef",
    {
        "createdAt": datetime,
        "lastModified": datetime,
    },
)
PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
    },
)
ListSolFunctionInstancesInputRequestTypeDef = TypedDict(
    "ListSolFunctionInstancesInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListSolFunctionPackageMetadataTypeDef = TypedDict(
    "ListSolFunctionPackageMetadataTypeDef",
    {
        "createdAt": datetime,
        "lastModified": datetime,
    },
)
ListSolFunctionPackagesInputRequestTypeDef = TypedDict(
    "ListSolFunctionPackagesInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListSolNetworkInstanceMetadataTypeDef = TypedDict(
    "ListSolNetworkInstanceMetadataTypeDef",
    {
        "createdAt": datetime,
        "lastModified": datetime,
    },
)
ListSolNetworkInstancesInputRequestTypeDef = TypedDict(
    "ListSolNetworkInstancesInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListSolNetworkOperationsMetadataTypeDef = TypedDict(
    "ListSolNetworkOperationsMetadataTypeDef",
    {
        "createdAt": datetime,
        "lastModified": datetime,
        "nsdInfoId": NotRequired[str],
        "vnfInstanceId": NotRequired[str],
    },
)
ListSolNetworkOperationsInputRequestTypeDef = TypedDict(
    "ListSolNetworkOperationsInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "nsInstanceId": NotRequired[str],
    },
)
ListSolNetworkPackageMetadataTypeDef = TypedDict(
    "ListSolNetworkPackageMetadataTypeDef",
    {
        "createdAt": datetime,
        "lastModified": datetime,
    },
)
ListSolNetworkPackagesInputRequestTypeDef = TypedDict(
    "ListSolNetworkPackagesInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)
TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)
TerminateSolNetworkInstanceInputRequestTypeDef = TypedDict(
    "TerminateSolNetworkInstanceInputRequestTypeDef",
    {
        "nsInstanceId": str,
        "tags": NotRequired[Mapping[str, str]],
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UpdateSolFunctionPackageInputRequestTypeDef = TypedDict(
    "UpdateSolFunctionPackageInputRequestTypeDef",
    {
        "operationalState": OperationalStateType,
        "vnfPkgId": str,
    },
)
UpdateSolNetworkModifyTypeDef = TypedDict(
    "UpdateSolNetworkModifyTypeDef",
    {
        "vnfConfigurableProperties": Mapping[str, Any],
        "vnfInstanceId": str,
    },
)
UpdateSolNetworkServiceDataTypeDef = TypedDict(
    "UpdateSolNetworkServiceDataTypeDef",
    {
        "nsdInfoId": str,
        "additionalParamsForNs": NotRequired[Mapping[str, Any]],
    },
)
UpdateSolNetworkPackageInputRequestTypeDef = TypedDict(
    "UpdateSolNetworkPackageInputRequestTypeDef",
    {
        "nsdInfoId": str,
        "nsdOperationalState": NsdOperationalStateType,
    },
)
PutSolFunctionPackageContentInputRequestTypeDef = TypedDict(
    "PutSolFunctionPackageContentInputRequestTypeDef",
    {
        "file": BlobTypeDef,
        "vnfPkgId": str,
        "contentType": NotRequired[Literal["application/zip"]],
    },
)
PutSolNetworkPackageContentInputRequestTypeDef = TypedDict(
    "PutSolNetworkPackageContentInputRequestTypeDef",
    {
        "file": BlobTypeDef,
        "nsdInfoId": str,
        "contentType": NotRequired[Literal["application/zip"]],
    },
)
ValidateSolFunctionPackageContentInputRequestTypeDef = TypedDict(
    "ValidateSolFunctionPackageContentInputRequestTypeDef",
    {
        "file": BlobTypeDef,
        "vnfPkgId": str,
        "contentType": NotRequired[Literal["application/zip"]],
    },
)
ValidateSolNetworkPackageContentInputRequestTypeDef = TypedDict(
    "ValidateSolNetworkPackageContentInputRequestTypeDef",
    {
        "file": BlobTypeDef,
        "nsdInfoId": str,
        "contentType": NotRequired[Literal["application/zip"]],
    },
)
CreateSolFunctionPackageOutputTypeDef = TypedDict(
    "CreateSolFunctionPackageOutputTypeDef",
    {
        "arn": str,
        "id": str,
        "onboardingState": OnboardingStateType,
        "operationalState": OperationalStateType,
        "tags": Dict[str, str],
        "usageState": UsageStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSolNetworkInstanceOutputTypeDef = TypedDict(
    "CreateSolNetworkInstanceOutputTypeDef",
    {
        "arn": str,
        "id": str,
        "nsInstanceName": str,
        "nsdInfoId": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSolNetworkPackageOutputTypeDef = TypedDict(
    "CreateSolNetworkPackageOutputTypeDef",
    {
        "arn": str,
        "id": str,
        "nsdOnboardingState": NsdOnboardingStateType,
        "nsdOperationalState": NsdOperationalStateType,
        "nsdUsageState": NsdUsageStateType,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSolFunctionPackageContentOutputTypeDef = TypedDict(
    "GetSolFunctionPackageContentOutputTypeDef",
    {
        "contentType": Literal["application/zip"],
        "packageContent": StreamingBody,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSolFunctionPackageDescriptorOutputTypeDef = TypedDict(
    "GetSolFunctionPackageDescriptorOutputTypeDef",
    {
        "contentType": Literal["text/plain"],
        "vnfd": StreamingBody,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSolNetworkPackageContentOutputTypeDef = TypedDict(
    "GetSolNetworkPackageContentOutputTypeDef",
    {
        "contentType": Literal["application/zip"],
        "nsdContent": StreamingBody,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSolNetworkPackageDescriptorOutputTypeDef = TypedDict(
    "GetSolNetworkPackageDescriptorOutputTypeDef",
    {
        "contentType": Literal["text/plain"],
        "nsd": StreamingBody,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InstantiateSolNetworkInstanceOutputTypeDef = TypedDict(
    "InstantiateSolNetworkInstanceOutputTypeDef",
    {
        "nsLcmOpOccId": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TerminateSolNetworkInstanceOutputTypeDef = TypedDict(
    "TerminateSolNetworkInstanceOutputTypeDef",
    {
        "nsLcmOpOccId": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSolFunctionPackageOutputTypeDef = TypedDict(
    "UpdateSolFunctionPackageOutputTypeDef",
    {
        "operationalState": OperationalStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSolNetworkInstanceOutputTypeDef = TypedDict(
    "UpdateSolNetworkInstanceOutputTypeDef",
    {
        "nsLcmOpOccId": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSolNetworkPackageOutputTypeDef = TypedDict(
    "UpdateSolNetworkPackageOutputTypeDef",
    {
        "nsdOperationalState": NsdOperationalStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSolNetworkOperationTaskDetailsTypeDef = TypedDict(
    "GetSolNetworkOperationTaskDetailsTypeDef",
    {
        "taskContext": NotRequired[Dict[str, str]],
        "taskEndTime": NotRequired[datetime],
        "taskErrorDetails": NotRequired[ErrorInfoTypeDef],
        "taskName": NotRequired[str],
        "taskStartTime": NotRequired[datetime],
        "taskStatus": NotRequired[TaskStatusType],
    },
)
FunctionArtifactMetaTypeDef = TypedDict(
    "FunctionArtifactMetaTypeDef",
    {
        "overrides": NotRequired[List[ToscaOverrideTypeDef]],
    },
)
NetworkArtifactMetaTypeDef = TypedDict(
    "NetworkArtifactMetaTypeDef",
    {
        "overrides": NotRequired[List[ToscaOverrideTypeDef]],
    },
)
GetSolNetworkInstanceOutputTypeDef = TypedDict(
    "GetSolNetworkInstanceOutputTypeDef",
    {
        "arn": str,
        "id": str,
        "lcmOpInfo": LcmOperationInfoTypeDef,
        "metadata": GetSolNetworkInstanceMetadataTypeDef,
        "nsInstanceDescription": str,
        "nsInstanceName": str,
        "nsState": NsStateType,
        "nsdId": str,
        "nsdInfoId": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSolNetworkOperationMetadataTypeDef = TypedDict(
    "GetSolNetworkOperationMetadataTypeDef",
    {
        "createdAt": datetime,
        "lastModified": datetime,
        "instantiateMetadata": NotRequired[InstantiateMetadataTypeDef],
        "modifyVnfInfoMetadata": NotRequired[ModifyVnfInfoMetadataTypeDef],
        "updateNsMetadata": NotRequired[UpdateNsMetadataTypeDef],
    },
)
GetSolVnfcResourceInfoTypeDef = TypedDict(
    "GetSolVnfcResourceInfoTypeDef",
    {
        "metadata": NotRequired[GetSolVnfcResourceInfoMetadataTypeDef],
    },
)
ListSolFunctionInstanceInfoTypeDef = TypedDict(
    "ListSolFunctionInstanceInfoTypeDef",
    {
        "arn": str,
        "id": str,
        "instantiationState": VnfInstantiationStateType,
        "metadata": ListSolFunctionInstanceMetadataTypeDef,
        "nsInstanceId": str,
        "vnfPkgId": str,
        "instantiatedVnfInfo": NotRequired[GetSolInstantiatedVnfInfoTypeDef],
        "vnfPkgName": NotRequired[str],
    },
)
ListSolFunctionInstancesInputListSolFunctionInstancesPaginateTypeDef = TypedDict(
    "ListSolFunctionInstancesInputListSolFunctionInstancesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSolFunctionPackagesInputListSolFunctionPackagesPaginateTypeDef = TypedDict(
    "ListSolFunctionPackagesInputListSolFunctionPackagesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSolNetworkInstancesInputListSolNetworkInstancesPaginateTypeDef = TypedDict(
    "ListSolNetworkInstancesInputListSolNetworkInstancesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSolNetworkOperationsInputListSolNetworkOperationsPaginateTypeDef = TypedDict(
    "ListSolNetworkOperationsInputListSolNetworkOperationsPaginateTypeDef",
    {
        "nsInstanceId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSolNetworkPackagesInputListSolNetworkPackagesPaginateTypeDef = TypedDict(
    "ListSolNetworkPackagesInputListSolNetworkPackagesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSolFunctionPackageInfoTypeDef = TypedDict(
    "ListSolFunctionPackageInfoTypeDef",
    {
        "arn": str,
        "id": str,
        "onboardingState": OnboardingStateType,
        "operationalState": OperationalStateType,
        "usageState": UsageStateType,
        "metadata": NotRequired[ListSolFunctionPackageMetadataTypeDef],
        "vnfProductName": NotRequired[str],
        "vnfProvider": NotRequired[str],
        "vnfdId": NotRequired[str],
        "vnfdVersion": NotRequired[str],
    },
)
ListSolNetworkInstanceInfoTypeDef = TypedDict(
    "ListSolNetworkInstanceInfoTypeDef",
    {
        "arn": str,
        "id": str,
        "metadata": ListSolNetworkInstanceMetadataTypeDef,
        "nsInstanceDescription": str,
        "nsInstanceName": str,
        "nsState": NsStateType,
        "nsdId": str,
        "nsdInfoId": str,
    },
)
ListSolNetworkOperationsInfoTypeDef = TypedDict(
    "ListSolNetworkOperationsInfoTypeDef",
    {
        "arn": str,
        "id": str,
        "lcmOperationType": LcmOperationTypeType,
        "nsInstanceId": str,
        "operationState": NsLcmOperationStateType,
        "error": NotRequired[ProblemDetailsTypeDef],
        "metadata": NotRequired[ListSolNetworkOperationsMetadataTypeDef],
        "updateType": NotRequired[UpdateSolNetworkTypeType],
    },
)
ListSolNetworkPackageInfoTypeDef = TypedDict(
    "ListSolNetworkPackageInfoTypeDef",
    {
        "arn": str,
        "id": str,
        "metadata": ListSolNetworkPackageMetadataTypeDef,
        "nsdOnboardingState": NsdOnboardingStateType,
        "nsdOperationalState": NsdOperationalStateType,
        "nsdUsageState": NsdUsageStateType,
        "nsdDesigner": NotRequired[str],
        "nsdId": NotRequired[str],
        "nsdInvariantId": NotRequired[str],
        "nsdName": NotRequired[str],
        "nsdVersion": NotRequired[str],
        "vnfPkgIds": NotRequired[List[str]],
    },
)
UpdateSolNetworkInstanceInputRequestTypeDef = TypedDict(
    "UpdateSolNetworkInstanceInputRequestTypeDef",
    {
        "nsInstanceId": str,
        "updateType": UpdateSolNetworkTypeType,
        "modifyVnfInfoData": NotRequired[UpdateSolNetworkModifyTypeDef],
        "tags": NotRequired[Mapping[str, str]],
        "updateNs": NotRequired[UpdateSolNetworkServiceDataTypeDef],
    },
)
GetSolFunctionPackageMetadataTypeDef = TypedDict(
    "GetSolFunctionPackageMetadataTypeDef",
    {
        "createdAt": datetime,
        "lastModified": datetime,
        "vnfd": NotRequired[FunctionArtifactMetaTypeDef],
    },
)
PutSolFunctionPackageContentMetadataTypeDef = TypedDict(
    "PutSolFunctionPackageContentMetadataTypeDef",
    {
        "vnfd": NotRequired[FunctionArtifactMetaTypeDef],
    },
)
ValidateSolFunctionPackageContentMetadataTypeDef = TypedDict(
    "ValidateSolFunctionPackageContentMetadataTypeDef",
    {
        "vnfd": NotRequired[FunctionArtifactMetaTypeDef],
    },
)
GetSolNetworkPackageMetadataTypeDef = TypedDict(
    "GetSolNetworkPackageMetadataTypeDef",
    {
        "createdAt": datetime,
        "lastModified": datetime,
        "nsd": NotRequired[NetworkArtifactMetaTypeDef],
    },
)
PutSolNetworkPackageContentMetadataTypeDef = TypedDict(
    "PutSolNetworkPackageContentMetadataTypeDef",
    {
        "nsd": NotRequired[NetworkArtifactMetaTypeDef],
    },
)
ValidateSolNetworkPackageContentMetadataTypeDef = TypedDict(
    "ValidateSolNetworkPackageContentMetadataTypeDef",
    {
        "nsd": NotRequired[NetworkArtifactMetaTypeDef],
    },
)
GetSolNetworkOperationOutputTypeDef = TypedDict(
    "GetSolNetworkOperationOutputTypeDef",
    {
        "arn": str,
        "error": ProblemDetailsTypeDef,
        "id": str,
        "lcmOperationType": LcmOperationTypeType,
        "metadata": GetSolNetworkOperationMetadataTypeDef,
        "nsInstanceId": str,
        "operationState": NsLcmOperationStateType,
        "tags": Dict[str, str],
        "tasks": List[GetSolNetworkOperationTaskDetailsTypeDef],
        "updateType": UpdateSolNetworkTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSolVnfInfoTypeDef = TypedDict(
    "GetSolVnfInfoTypeDef",
    {
        "vnfState": NotRequired[VnfOperationalStateType],
        "vnfcResourceInfo": NotRequired[List[GetSolVnfcResourceInfoTypeDef]],
    },
)
ListSolFunctionInstancesOutputTypeDef = TypedDict(
    "ListSolFunctionInstancesOutputTypeDef",
    {
        "functionInstances": List[ListSolFunctionInstanceInfoTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSolFunctionPackagesOutputTypeDef = TypedDict(
    "ListSolFunctionPackagesOutputTypeDef",
    {
        "functionPackages": List[ListSolFunctionPackageInfoTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSolNetworkInstancesOutputTypeDef = TypedDict(
    "ListSolNetworkInstancesOutputTypeDef",
    {
        "networkInstances": List[ListSolNetworkInstanceInfoTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSolNetworkOperationsOutputTypeDef = TypedDict(
    "ListSolNetworkOperationsOutputTypeDef",
    {
        "networkOperations": List[ListSolNetworkOperationsInfoTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSolNetworkPackagesOutputTypeDef = TypedDict(
    "ListSolNetworkPackagesOutputTypeDef",
    {
        "networkPackages": List[ListSolNetworkPackageInfoTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSolFunctionPackageOutputTypeDef = TypedDict(
    "GetSolFunctionPackageOutputTypeDef",
    {
        "arn": str,
        "id": str,
        "metadata": GetSolFunctionPackageMetadataTypeDef,
        "onboardingState": OnboardingStateType,
        "operationalState": OperationalStateType,
        "tags": Dict[str, str],
        "usageState": UsageStateType,
        "vnfProductName": str,
        "vnfProvider": str,
        "vnfdId": str,
        "vnfdVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutSolFunctionPackageContentOutputTypeDef = TypedDict(
    "PutSolFunctionPackageContentOutputTypeDef",
    {
        "id": str,
        "metadata": PutSolFunctionPackageContentMetadataTypeDef,
        "vnfProductName": str,
        "vnfProvider": str,
        "vnfdId": str,
        "vnfdVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ValidateSolFunctionPackageContentOutputTypeDef = TypedDict(
    "ValidateSolFunctionPackageContentOutputTypeDef",
    {
        "id": str,
        "metadata": ValidateSolFunctionPackageContentMetadataTypeDef,
        "vnfProductName": str,
        "vnfProvider": str,
        "vnfdId": str,
        "vnfdVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSolNetworkPackageOutputTypeDef = TypedDict(
    "GetSolNetworkPackageOutputTypeDef",
    {
        "arn": str,
        "id": str,
        "metadata": GetSolNetworkPackageMetadataTypeDef,
        "nsdId": str,
        "nsdName": str,
        "nsdOnboardingState": NsdOnboardingStateType,
        "nsdOperationalState": NsdOperationalStateType,
        "nsdUsageState": NsdUsageStateType,
        "nsdVersion": str,
        "tags": Dict[str, str],
        "vnfPkgIds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutSolNetworkPackageContentOutputTypeDef = TypedDict(
    "PutSolNetworkPackageContentOutputTypeDef",
    {
        "arn": str,
        "id": str,
        "metadata": PutSolNetworkPackageContentMetadataTypeDef,
        "nsdId": str,
        "nsdName": str,
        "nsdVersion": str,
        "vnfPkgIds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ValidateSolNetworkPackageContentOutputTypeDef = TypedDict(
    "ValidateSolNetworkPackageContentOutputTypeDef",
    {
        "arn": str,
        "id": str,
        "metadata": ValidateSolNetworkPackageContentMetadataTypeDef,
        "nsdId": str,
        "nsdName": str,
        "nsdVersion": str,
        "vnfPkgIds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSolFunctionInstanceOutputTypeDef = TypedDict(
    "GetSolFunctionInstanceOutputTypeDef",
    {
        "arn": str,
        "id": str,
        "instantiatedVnfInfo": GetSolVnfInfoTypeDef,
        "instantiationState": VnfInstantiationStateType,
        "metadata": GetSolFunctionInstanceMetadataTypeDef,
        "nsInstanceId": str,
        "tags": Dict[str, str],
        "vnfPkgId": str,
        "vnfProductName": str,
        "vnfProvider": str,
        "vnfdId": str,
        "vnfdVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
