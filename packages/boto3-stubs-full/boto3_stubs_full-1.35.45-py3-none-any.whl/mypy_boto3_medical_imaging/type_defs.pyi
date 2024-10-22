"""
Type annotations for medical-imaging service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_medical_imaging/type_defs/)

Usage::

    ```python
    from mypy_boto3_medical_imaging.type_defs import BlobTypeDef

    data: BlobTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    DatastoreStatusType,
    ImageSetStateType,
    ImageSetWorkflowStatusType,
    JobStatusType,
    OperatorType,
    SortFieldType,
    SortOrderType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "BlobTypeDef",
    "CopyDestinationImageSetPropertiesTypeDef",
    "CopyDestinationImageSetTypeDef",
    "CopySourceImageSetPropertiesTypeDef",
    "ResponseMetadataTypeDef",
    "MetadataCopiesTypeDef",
    "CreateDatastoreRequestRequestTypeDef",
    "DICOMImportJobPropertiesTypeDef",
    "DICOMImportJobSummaryTypeDef",
    "DICOMStudyDateAndTimeTypeDef",
    "DICOMTagsTypeDef",
    "DatastorePropertiesTypeDef",
    "DatastoreSummaryTypeDef",
    "DeleteDatastoreRequestRequestTypeDef",
    "DeleteImageSetRequestRequestTypeDef",
    "GetDICOMImportJobRequestRequestTypeDef",
    "GetDatastoreRequestRequestTypeDef",
    "ImageFrameInformationTypeDef",
    "GetImageSetMetadataRequestRequestTypeDef",
    "GetImageSetRequestRequestTypeDef",
    "OverridesTypeDef",
    "PaginatorConfigTypeDef",
    "ListDICOMImportJobsRequestRequestTypeDef",
    "ListDatastoresRequestRequestTypeDef",
    "ListImageSetVersionsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TimestampTypeDef",
    "SortTypeDef",
    "StartDICOMImportJobRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "DICOMUpdatesTypeDef",
    "CopyImageSetResponseTypeDef",
    "CreateDatastoreResponseTypeDef",
    "DeleteDatastoreResponseTypeDef",
    "DeleteImageSetResponseTypeDef",
    "GetImageFrameResponseTypeDef",
    "GetImageSetMetadataResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartDICOMImportJobResponseTypeDef",
    "UpdateImageSetMetadataResponseTypeDef",
    "CopySourceImageSetInformationTypeDef",
    "GetDICOMImportJobResponseTypeDef",
    "ListDICOMImportJobsResponseTypeDef",
    "ImageSetsMetadataSummaryTypeDef",
    "GetDatastoreResponseTypeDef",
    "ListDatastoresResponseTypeDef",
    "GetImageFrameRequestRequestTypeDef",
    "GetImageSetResponseTypeDef",
    "ImageSetPropertiesTypeDef",
    "ListDICOMImportJobsRequestListDICOMImportJobsPaginateTypeDef",
    "ListDatastoresRequestListDatastoresPaginateTypeDef",
    "ListImageSetVersionsRequestListImageSetVersionsPaginateTypeDef",
    "SearchByAttributeValueTypeDef",
    "MetadataUpdatesTypeDef",
    "CopyImageSetInformationTypeDef",
    "SearchImageSetsResponseTypeDef",
    "ListImageSetVersionsResponseTypeDef",
    "SearchFilterTypeDef",
    "UpdateImageSetMetadataRequestRequestTypeDef",
    "CopyImageSetRequestRequestTypeDef",
    "SearchCriteriaTypeDef",
    "SearchImageSetsRequestRequestTypeDef",
    "SearchImageSetsRequestSearchImageSetsPaginateTypeDef",
)

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
CopyDestinationImageSetPropertiesTypeDef = TypedDict(
    "CopyDestinationImageSetPropertiesTypeDef",
    {
        "imageSetId": str,
        "latestVersionId": str,
        "imageSetState": NotRequired[ImageSetStateType],
        "imageSetWorkflowStatus": NotRequired[ImageSetWorkflowStatusType],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
        "imageSetArn": NotRequired[str],
    },
)
CopyDestinationImageSetTypeDef = TypedDict(
    "CopyDestinationImageSetTypeDef",
    {
        "imageSetId": str,
        "latestVersionId": str,
    },
)
CopySourceImageSetPropertiesTypeDef = TypedDict(
    "CopySourceImageSetPropertiesTypeDef",
    {
        "imageSetId": str,
        "latestVersionId": str,
        "imageSetState": NotRequired[ImageSetStateType],
        "imageSetWorkflowStatus": NotRequired[ImageSetWorkflowStatusType],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
        "imageSetArn": NotRequired[str],
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
MetadataCopiesTypeDef = TypedDict(
    "MetadataCopiesTypeDef",
    {
        "copiableAttributes": str,
    },
)
CreateDatastoreRequestRequestTypeDef = TypedDict(
    "CreateDatastoreRequestRequestTypeDef",
    {
        "clientToken": str,
        "datastoreName": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "kmsKeyArn": NotRequired[str],
    },
)
DICOMImportJobPropertiesTypeDef = TypedDict(
    "DICOMImportJobPropertiesTypeDef",
    {
        "jobId": str,
        "jobName": str,
        "jobStatus": JobStatusType,
        "datastoreId": str,
        "dataAccessRoleArn": str,
        "inputS3Uri": str,
        "outputS3Uri": str,
        "endedAt": NotRequired[datetime],
        "submittedAt": NotRequired[datetime],
        "message": NotRequired[str],
    },
)
DICOMImportJobSummaryTypeDef = TypedDict(
    "DICOMImportJobSummaryTypeDef",
    {
        "jobId": str,
        "jobName": str,
        "jobStatus": JobStatusType,
        "datastoreId": str,
        "dataAccessRoleArn": NotRequired[str],
        "endedAt": NotRequired[datetime],
        "submittedAt": NotRequired[datetime],
        "message": NotRequired[str],
    },
)
DICOMStudyDateAndTimeTypeDef = TypedDict(
    "DICOMStudyDateAndTimeTypeDef",
    {
        "DICOMStudyDate": str,
        "DICOMStudyTime": NotRequired[str],
    },
)
DICOMTagsTypeDef = TypedDict(
    "DICOMTagsTypeDef",
    {
        "DICOMPatientId": NotRequired[str],
        "DICOMPatientName": NotRequired[str],
        "DICOMPatientBirthDate": NotRequired[str],
        "DICOMPatientSex": NotRequired[str],
        "DICOMStudyInstanceUID": NotRequired[str],
        "DICOMStudyId": NotRequired[str],
        "DICOMStudyDescription": NotRequired[str],
        "DICOMNumberOfStudyRelatedSeries": NotRequired[int],
        "DICOMNumberOfStudyRelatedInstances": NotRequired[int],
        "DICOMAccessionNumber": NotRequired[str],
        "DICOMSeriesInstanceUID": NotRequired[str],
        "DICOMSeriesModality": NotRequired[str],
        "DICOMSeriesBodyPart": NotRequired[str],
        "DICOMSeriesNumber": NotRequired[int],
        "DICOMStudyDate": NotRequired[str],
        "DICOMStudyTime": NotRequired[str],
    },
)
DatastorePropertiesTypeDef = TypedDict(
    "DatastorePropertiesTypeDef",
    {
        "datastoreId": str,
        "datastoreName": str,
        "datastoreStatus": DatastoreStatusType,
        "kmsKeyArn": NotRequired[str],
        "datastoreArn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
    },
)
DatastoreSummaryTypeDef = TypedDict(
    "DatastoreSummaryTypeDef",
    {
        "datastoreId": str,
        "datastoreName": str,
        "datastoreStatus": DatastoreStatusType,
        "datastoreArn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
    },
)
DeleteDatastoreRequestRequestTypeDef = TypedDict(
    "DeleteDatastoreRequestRequestTypeDef",
    {
        "datastoreId": str,
    },
)
DeleteImageSetRequestRequestTypeDef = TypedDict(
    "DeleteImageSetRequestRequestTypeDef",
    {
        "datastoreId": str,
        "imageSetId": str,
    },
)
GetDICOMImportJobRequestRequestTypeDef = TypedDict(
    "GetDICOMImportJobRequestRequestTypeDef",
    {
        "datastoreId": str,
        "jobId": str,
    },
)
GetDatastoreRequestRequestTypeDef = TypedDict(
    "GetDatastoreRequestRequestTypeDef",
    {
        "datastoreId": str,
    },
)
ImageFrameInformationTypeDef = TypedDict(
    "ImageFrameInformationTypeDef",
    {
        "imageFrameId": str,
    },
)
GetImageSetMetadataRequestRequestTypeDef = TypedDict(
    "GetImageSetMetadataRequestRequestTypeDef",
    {
        "datastoreId": str,
        "imageSetId": str,
        "versionId": NotRequired[str],
    },
)
GetImageSetRequestRequestTypeDef = TypedDict(
    "GetImageSetRequestRequestTypeDef",
    {
        "datastoreId": str,
        "imageSetId": str,
        "versionId": NotRequired[str],
    },
)
OverridesTypeDef = TypedDict(
    "OverridesTypeDef",
    {
        "forced": NotRequired[bool],
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
ListDICOMImportJobsRequestRequestTypeDef = TypedDict(
    "ListDICOMImportJobsRequestRequestTypeDef",
    {
        "datastoreId": str,
        "jobStatus": NotRequired[JobStatusType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListDatastoresRequestRequestTypeDef = TypedDict(
    "ListDatastoresRequestRequestTypeDef",
    {
        "datastoreStatus": NotRequired[DatastoreStatusType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListImageSetVersionsRequestRequestTypeDef = TypedDict(
    "ListImageSetVersionsRequestRequestTypeDef",
    {
        "datastoreId": str,
        "imageSetId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
TimestampTypeDef = Union[datetime, str]
SortTypeDef = TypedDict(
    "SortTypeDef",
    {
        "sortOrder": SortOrderType,
        "sortField": SortFieldType,
    },
)
StartDICOMImportJobRequestRequestTypeDef = TypedDict(
    "StartDICOMImportJobRequestRequestTypeDef",
    {
        "dataAccessRoleArn": str,
        "clientToken": str,
        "datastoreId": str,
        "inputS3Uri": str,
        "outputS3Uri": str,
        "jobName": NotRequired[str],
        "inputOwnerAccountId": NotRequired[str],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
DICOMUpdatesTypeDef = TypedDict(
    "DICOMUpdatesTypeDef",
    {
        "removableAttributes": NotRequired[BlobTypeDef],
        "updatableAttributes": NotRequired[BlobTypeDef],
    },
)
CopyImageSetResponseTypeDef = TypedDict(
    "CopyImageSetResponseTypeDef",
    {
        "datastoreId": str,
        "sourceImageSetProperties": CopySourceImageSetPropertiesTypeDef,
        "destinationImageSetProperties": CopyDestinationImageSetPropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDatastoreResponseTypeDef = TypedDict(
    "CreateDatastoreResponseTypeDef",
    {
        "datastoreId": str,
        "datastoreStatus": DatastoreStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDatastoreResponseTypeDef = TypedDict(
    "DeleteDatastoreResponseTypeDef",
    {
        "datastoreId": str,
        "datastoreStatus": DatastoreStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteImageSetResponseTypeDef = TypedDict(
    "DeleteImageSetResponseTypeDef",
    {
        "datastoreId": str,
        "imageSetId": str,
        "imageSetState": ImageSetStateType,
        "imageSetWorkflowStatus": ImageSetWorkflowStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetImageFrameResponseTypeDef = TypedDict(
    "GetImageFrameResponseTypeDef",
    {
        "imageFrameBlob": StreamingBody,
        "contentType": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetImageSetMetadataResponseTypeDef = TypedDict(
    "GetImageSetMetadataResponseTypeDef",
    {
        "imageSetMetadataBlob": StreamingBody,
        "contentType": str,
        "contentEncoding": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartDICOMImportJobResponseTypeDef = TypedDict(
    "StartDICOMImportJobResponseTypeDef",
    {
        "datastoreId": str,
        "jobId": str,
        "jobStatus": JobStatusType,
        "submittedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateImageSetMetadataResponseTypeDef = TypedDict(
    "UpdateImageSetMetadataResponseTypeDef",
    {
        "datastoreId": str,
        "imageSetId": str,
        "latestVersionId": str,
        "imageSetState": ImageSetStateType,
        "imageSetWorkflowStatus": ImageSetWorkflowStatusType,
        "createdAt": datetime,
        "updatedAt": datetime,
        "message": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CopySourceImageSetInformationTypeDef = TypedDict(
    "CopySourceImageSetInformationTypeDef",
    {
        "latestVersionId": str,
        "DICOMCopies": NotRequired[MetadataCopiesTypeDef],
    },
)
GetDICOMImportJobResponseTypeDef = TypedDict(
    "GetDICOMImportJobResponseTypeDef",
    {
        "jobProperties": DICOMImportJobPropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDICOMImportJobsResponseTypeDef = TypedDict(
    "ListDICOMImportJobsResponseTypeDef",
    {
        "jobSummaries": List[DICOMImportJobSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImageSetsMetadataSummaryTypeDef = TypedDict(
    "ImageSetsMetadataSummaryTypeDef",
    {
        "imageSetId": str,
        "version": NotRequired[int],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
        "DICOMTags": NotRequired[DICOMTagsTypeDef],
    },
)
GetDatastoreResponseTypeDef = TypedDict(
    "GetDatastoreResponseTypeDef",
    {
        "datastoreProperties": DatastorePropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDatastoresResponseTypeDef = TypedDict(
    "ListDatastoresResponseTypeDef",
    {
        "datastoreSummaries": List[DatastoreSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetImageFrameRequestRequestTypeDef = TypedDict(
    "GetImageFrameRequestRequestTypeDef",
    {
        "datastoreId": str,
        "imageSetId": str,
        "imageFrameInformation": ImageFrameInformationTypeDef,
    },
)
GetImageSetResponseTypeDef = TypedDict(
    "GetImageSetResponseTypeDef",
    {
        "datastoreId": str,
        "imageSetId": str,
        "versionId": str,
        "imageSetState": ImageSetStateType,
        "imageSetWorkflowStatus": ImageSetWorkflowStatusType,
        "createdAt": datetime,
        "updatedAt": datetime,
        "deletedAt": datetime,
        "message": str,
        "imageSetArn": str,
        "overrides": OverridesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImageSetPropertiesTypeDef = TypedDict(
    "ImageSetPropertiesTypeDef",
    {
        "imageSetId": str,
        "versionId": str,
        "imageSetState": ImageSetStateType,
        "ImageSetWorkflowStatus": NotRequired[ImageSetWorkflowStatusType],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
        "deletedAt": NotRequired[datetime],
        "message": NotRequired[str],
        "overrides": NotRequired[OverridesTypeDef],
    },
)
ListDICOMImportJobsRequestListDICOMImportJobsPaginateTypeDef = TypedDict(
    "ListDICOMImportJobsRequestListDICOMImportJobsPaginateTypeDef",
    {
        "datastoreId": str,
        "jobStatus": NotRequired[JobStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDatastoresRequestListDatastoresPaginateTypeDef = TypedDict(
    "ListDatastoresRequestListDatastoresPaginateTypeDef",
    {
        "datastoreStatus": NotRequired[DatastoreStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListImageSetVersionsRequestListImageSetVersionsPaginateTypeDef = TypedDict(
    "ListImageSetVersionsRequestListImageSetVersionsPaginateTypeDef",
    {
        "datastoreId": str,
        "imageSetId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchByAttributeValueTypeDef = TypedDict(
    "SearchByAttributeValueTypeDef",
    {
        "DICOMPatientId": NotRequired[str],
        "DICOMAccessionNumber": NotRequired[str],
        "DICOMStudyId": NotRequired[str],
        "DICOMStudyInstanceUID": NotRequired[str],
        "DICOMSeriesInstanceUID": NotRequired[str],
        "createdAt": NotRequired[TimestampTypeDef],
        "updatedAt": NotRequired[TimestampTypeDef],
        "DICOMStudyDateAndTime": NotRequired[DICOMStudyDateAndTimeTypeDef],
    },
)
MetadataUpdatesTypeDef = TypedDict(
    "MetadataUpdatesTypeDef",
    {
        "DICOMUpdates": NotRequired[DICOMUpdatesTypeDef],
        "revertToVersionId": NotRequired[str],
    },
)
CopyImageSetInformationTypeDef = TypedDict(
    "CopyImageSetInformationTypeDef",
    {
        "sourceImageSet": CopySourceImageSetInformationTypeDef,
        "destinationImageSet": NotRequired[CopyDestinationImageSetTypeDef],
    },
)
SearchImageSetsResponseTypeDef = TypedDict(
    "SearchImageSetsResponseTypeDef",
    {
        "imageSetsMetadataSummaries": List[ImageSetsMetadataSummaryTypeDef],
        "sort": SortTypeDef,
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListImageSetVersionsResponseTypeDef = TypedDict(
    "ListImageSetVersionsResponseTypeDef",
    {
        "imageSetPropertiesList": List[ImageSetPropertiesTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchFilterTypeDef = TypedDict(
    "SearchFilterTypeDef",
    {
        "values": Sequence[SearchByAttributeValueTypeDef],
        "operator": OperatorType,
    },
)
UpdateImageSetMetadataRequestRequestTypeDef = TypedDict(
    "UpdateImageSetMetadataRequestRequestTypeDef",
    {
        "datastoreId": str,
        "imageSetId": str,
        "latestVersionId": str,
        "updateImageSetMetadataUpdates": MetadataUpdatesTypeDef,
        "force": NotRequired[bool],
    },
)
CopyImageSetRequestRequestTypeDef = TypedDict(
    "CopyImageSetRequestRequestTypeDef",
    {
        "datastoreId": str,
        "sourceImageSetId": str,
        "copyImageSetInformation": CopyImageSetInformationTypeDef,
        "force": NotRequired[bool],
    },
)
SearchCriteriaTypeDef = TypedDict(
    "SearchCriteriaTypeDef",
    {
        "filters": NotRequired[Sequence[SearchFilterTypeDef]],
        "sort": NotRequired[SortTypeDef],
    },
)
SearchImageSetsRequestRequestTypeDef = TypedDict(
    "SearchImageSetsRequestRequestTypeDef",
    {
        "datastoreId": str,
        "searchCriteria": NotRequired[SearchCriteriaTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
SearchImageSetsRequestSearchImageSetsPaginateTypeDef = TypedDict(
    "SearchImageSetsRequestSearchImageSetsPaginateTypeDef",
    {
        "datastoreId": str,
        "searchCriteria": NotRequired[SearchCriteriaTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
