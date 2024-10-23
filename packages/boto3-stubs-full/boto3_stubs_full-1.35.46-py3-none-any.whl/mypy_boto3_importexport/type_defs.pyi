"""
Type annotations for importexport service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_importexport/type_defs/)

Usage::

    ```python
    from mypy_boto3_importexport.type_defs import ArtifactTypeDef

    data: ArtifactTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import JobTypeType

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "ArtifactTypeDef",
    "CancelJobInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CreateJobInputRequestTypeDef",
    "GetShippingLabelInputRequestTypeDef",
    "GetStatusInputRequestTypeDef",
    "JobTypeDef",
    "PaginatorConfigTypeDef",
    "ListJobsInputRequestTypeDef",
    "UpdateJobInputRequestTypeDef",
    "CancelJobOutputTypeDef",
    "CreateJobOutputTypeDef",
    "GetShippingLabelOutputTypeDef",
    "GetStatusOutputTypeDef",
    "UpdateJobOutputTypeDef",
    "ListJobsOutputTypeDef",
    "ListJobsInputListJobsPaginateTypeDef",
)

ArtifactTypeDef = TypedDict(
    "ArtifactTypeDef",
    {
        "Description": NotRequired[str],
        "URL": NotRequired[str],
    },
)
CancelJobInputRequestTypeDef = TypedDict(
    "CancelJobInputRequestTypeDef",
    {
        "JobId": str,
        "APIVersion": NotRequired[str],
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
CreateJobInputRequestTypeDef = TypedDict(
    "CreateJobInputRequestTypeDef",
    {
        "JobType": JobTypeType,
        "Manifest": str,
        "ValidateOnly": bool,
        "ManifestAddendum": NotRequired[str],
        "APIVersion": NotRequired[str],
    },
)
GetShippingLabelInputRequestTypeDef = TypedDict(
    "GetShippingLabelInputRequestTypeDef",
    {
        "jobIds": Sequence[str],
        "name": NotRequired[str],
        "company": NotRequired[str],
        "phoneNumber": NotRequired[str],
        "country": NotRequired[str],
        "stateOrProvince": NotRequired[str],
        "city": NotRequired[str],
        "postalCode": NotRequired[str],
        "street1": NotRequired[str],
        "street2": NotRequired[str],
        "street3": NotRequired[str],
        "APIVersion": NotRequired[str],
    },
)
GetStatusInputRequestTypeDef = TypedDict(
    "GetStatusInputRequestTypeDef",
    {
        "JobId": str,
        "APIVersion": NotRequired[str],
    },
)
JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "JobId": NotRequired[str],
        "CreationDate": NotRequired[datetime],
        "IsCanceled": NotRequired[bool],
        "JobType": NotRequired[JobTypeType],
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
ListJobsInputRequestTypeDef = TypedDict(
    "ListJobsInputRequestTypeDef",
    {
        "MaxJobs": NotRequired[int],
        "Marker": NotRequired[str],
        "APIVersion": NotRequired[str],
    },
)
UpdateJobInputRequestTypeDef = TypedDict(
    "UpdateJobInputRequestTypeDef",
    {
        "JobId": str,
        "Manifest": str,
        "JobType": JobTypeType,
        "ValidateOnly": bool,
        "APIVersion": NotRequired[str],
    },
)
CancelJobOutputTypeDef = TypedDict(
    "CancelJobOutputTypeDef",
    {
        "Success": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateJobOutputTypeDef = TypedDict(
    "CreateJobOutputTypeDef",
    {
        "JobId": str,
        "JobType": JobTypeType,
        "Signature": str,
        "SignatureFileContents": str,
        "WarningMessage": str,
        "ArtifactList": List[ArtifactTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetShippingLabelOutputTypeDef = TypedDict(
    "GetShippingLabelOutputTypeDef",
    {
        "ShippingLabelURL": str,
        "Warning": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetStatusOutputTypeDef = TypedDict(
    "GetStatusOutputTypeDef",
    {
        "JobId": str,
        "JobType": JobTypeType,
        "LocationCode": str,
        "LocationMessage": str,
        "ProgressCode": str,
        "ProgressMessage": str,
        "Carrier": str,
        "TrackingNumber": str,
        "LogBucket": str,
        "LogKey": str,
        "ErrorCount": int,
        "Signature": str,
        "SignatureFileContents": str,
        "CurrentManifest": str,
        "CreationDate": datetime,
        "ArtifactList": List[ArtifactTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateJobOutputTypeDef = TypedDict(
    "UpdateJobOutputTypeDef",
    {
        "Success": bool,
        "WarningMessage": str,
        "ArtifactList": List[ArtifactTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListJobsOutputTypeDef = TypedDict(
    "ListJobsOutputTypeDef",
    {
        "Jobs": List[JobTypeDef],
        "IsTruncated": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListJobsInputListJobsPaginateTypeDef = TypedDict(
    "ListJobsInputListJobsPaginateTypeDef",
    {
        "APIVersion": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
