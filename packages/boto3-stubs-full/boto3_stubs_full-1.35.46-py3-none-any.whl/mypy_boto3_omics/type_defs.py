"""
Type annotations for omics service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_omics/type_defs/)

Usage::

    ```python
    from mypy_boto3_omics.type_defs import AbortMultipartReadSetUploadRequestRequestTypeDef

    data: AbortMultipartReadSetUploadRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    AnnotationTypeType,
    CreationTypeType,
    ETagAlgorithmFamilyType,
    ETagAlgorithmType,
    FileTypeType,
    FormatToHeaderKeyType,
    JobStatusType,
    ReadSetActivationJobItemStatusType,
    ReadSetActivationJobStatusType,
    ReadSetExportJobItemStatusType,
    ReadSetExportJobStatusType,
    ReadSetFileType,
    ReadSetImportJobItemStatusType,
    ReadSetImportJobStatusType,
    ReadSetPartSourceType,
    ReadSetStatusType,
    ReferenceFileType,
    ReferenceImportJobItemStatusType,
    ReferenceImportJobStatusType,
    ReferenceStatusType,
    ResourceOwnerType,
    RunLogLevelType,
    RunRetentionModeType,
    RunStatusType,
    SchemaValueTypeType,
    ShareResourceTypeType,
    ShareStatusType,
    StorageTypeType,
    StoreFormatType,
    StoreStatusType,
    TaskStatusType,
    VersionStatusType,
    WorkflowEngineType,
    WorkflowStatusType,
    WorkflowTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AbortMultipartReadSetUploadRequestRequestTypeDef",
    "AcceptShareRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "TimestampTypeDef",
    "ActivateReadSetJobItemTypeDef",
    "ActivateReadSetSourceItemTypeDef",
    "AnnotationImportItemDetailTypeDef",
    "AnnotationImportItemSourceTypeDef",
    "AnnotationImportJobItemTypeDef",
    "ReferenceItemTypeDef",
    "SseConfigTypeDef",
    "AnnotationStoreVersionItemTypeDef",
    "BatchDeleteReadSetRequestRequestTypeDef",
    "ReadSetBatchErrorTypeDef",
    "BlobTypeDef",
    "CancelAnnotationImportRequestRequestTypeDef",
    "CancelRunRequestRequestTypeDef",
    "CancelVariantImportRequestRequestTypeDef",
    "CompleteReadSetUploadPartListItemTypeDef",
    "CreateMultipartReadSetUploadRequestRequestTypeDef",
    "CreateRunGroupRequestRequestTypeDef",
    "CreateShareRequestRequestTypeDef",
    "WorkflowParameterTypeDef",
    "DeleteAnnotationStoreRequestRequestTypeDef",
    "DeleteAnnotationStoreVersionsRequestRequestTypeDef",
    "VersionDeleteErrorTypeDef",
    "DeleteReferenceRequestRequestTypeDef",
    "DeleteReferenceStoreRequestRequestTypeDef",
    "DeleteRunGroupRequestRequestTypeDef",
    "DeleteRunRequestRequestTypeDef",
    "DeleteSequenceStoreRequestRequestTypeDef",
    "DeleteShareRequestRequestTypeDef",
    "DeleteVariantStoreRequestRequestTypeDef",
    "DeleteWorkflowRequestRequestTypeDef",
    "ETagTypeDef",
    "ExportReadSetDetailTypeDef",
    "ExportReadSetJobDetailTypeDef",
    "ExportReadSetTypeDef",
    "ReadSetS3AccessTypeDef",
    "FilterTypeDef",
    "VcfOptionsTypeDef",
    "WaiterConfigTypeDef",
    "GetAnnotationImportRequestRequestTypeDef",
    "GetAnnotationStoreRequestRequestTypeDef",
    "GetAnnotationStoreVersionRequestRequestTypeDef",
    "GetReadSetActivationJobRequestRequestTypeDef",
    "GetReadSetExportJobRequestRequestTypeDef",
    "GetReadSetImportJobRequestRequestTypeDef",
    "GetReadSetMetadataRequestRequestTypeDef",
    "SequenceInformationTypeDef",
    "GetReadSetRequestRequestTypeDef",
    "GetReferenceImportJobRequestRequestTypeDef",
    "ImportReferenceSourceItemTypeDef",
    "GetReferenceMetadataRequestRequestTypeDef",
    "GetReferenceRequestRequestTypeDef",
    "GetReferenceStoreRequestRequestTypeDef",
    "GetRunGroupRequestRequestTypeDef",
    "GetRunRequestRequestTypeDef",
    "RunLogLocationTypeDef",
    "GetRunTaskRequestRequestTypeDef",
    "GetSequenceStoreRequestRequestTypeDef",
    "SequenceStoreS3AccessTypeDef",
    "GetShareRequestRequestTypeDef",
    "ShareDetailsTypeDef",
    "GetVariantImportRequestRequestTypeDef",
    "VariantImportItemDetailTypeDef",
    "GetVariantStoreRequestRequestTypeDef",
    "GetWorkflowRequestRequestTypeDef",
    "ImportReadSetJobItemTypeDef",
    "SourceFilesTypeDef",
    "ImportReferenceJobItemTypeDef",
    "ListAnnotationImportJobsFilterTypeDef",
    "PaginatorConfigTypeDef",
    "ListAnnotationStoreVersionsFilterTypeDef",
    "ListAnnotationStoresFilterTypeDef",
    "ListMultipartReadSetUploadsRequestRequestTypeDef",
    "MultipartReadSetUploadListItemTypeDef",
    "ReadSetUploadPartListItemTypeDef",
    "ReferenceListItemTypeDef",
    "ListRunGroupsRequestRequestTypeDef",
    "RunGroupListItemTypeDef",
    "ListRunTasksRequestRequestTypeDef",
    "TaskListItemTypeDef",
    "ListRunsRequestRequestTypeDef",
    "RunListItemTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListVariantImportJobsFilterTypeDef",
    "VariantImportJobItemTypeDef",
    "ListVariantStoresFilterTypeDef",
    "ListWorkflowsRequestRequestTypeDef",
    "WorkflowListItemTypeDef",
    "ReadOptionsTypeDef",
    "StartReadSetActivationJobSourceItemTypeDef",
    "StartReferenceImportJobSourceItemTypeDef",
    "StartRunRequestRequestTypeDef",
    "VariantImportItemSourceTypeDef",
    "TsvStoreOptionsOutputTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TsvStoreOptionsTypeDef",
    "TsvVersionOptionsOutputTypeDef",
    "TsvVersionOptionsTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAnnotationStoreRequestRequestTypeDef",
    "UpdateAnnotationStoreVersionRequestRequestTypeDef",
    "UpdateRunGroupRequestRequestTypeDef",
    "UpdateVariantStoreRequestRequestTypeDef",
    "UpdateWorkflowRequestRequestTypeDef",
    "AcceptShareResponseTypeDef",
    "CompleteMultipartReadSetUploadResponseTypeDef",
    "CreateMultipartReadSetUploadResponseTypeDef",
    "CreateRunGroupResponseTypeDef",
    "CreateShareResponseTypeDef",
    "CreateWorkflowResponseTypeDef",
    "DeleteAnnotationStoreResponseTypeDef",
    "DeleteShareResponseTypeDef",
    "DeleteVariantStoreResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetReadSetResponseTypeDef",
    "GetReferenceResponseTypeDef",
    "GetRunGroupResponseTypeDef",
    "GetRunTaskResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartAnnotationImportResponseTypeDef",
    "StartReadSetActivationJobResponseTypeDef",
    "StartReadSetExportJobResponseTypeDef",
    "StartReadSetImportJobResponseTypeDef",
    "StartReferenceImportJobResponseTypeDef",
    "StartRunResponseTypeDef",
    "StartVariantImportResponseTypeDef",
    "UpdateAnnotationStoreVersionResponseTypeDef",
    "UploadReadSetPartResponseTypeDef",
    "ActivateReadSetFilterTypeDef",
    "ExportReadSetFilterTypeDef",
    "ImportReadSetFilterTypeDef",
    "ImportReferenceFilterTypeDef",
    "ReadSetFilterTypeDef",
    "ReadSetUploadPartListFilterTypeDef",
    "ReferenceFilterTypeDef",
    "ReferenceStoreFilterTypeDef",
    "SequenceStoreFilterTypeDef",
    "ListReadSetActivationJobsResponseTypeDef",
    "GetReadSetActivationJobResponseTypeDef",
    "ListAnnotationImportJobsResponseTypeDef",
    "CreateVariantStoreResponseTypeDef",
    "UpdateVariantStoreResponseTypeDef",
    "AnnotationStoreItemTypeDef",
    "CreateReferenceStoreRequestRequestTypeDef",
    "CreateReferenceStoreResponseTypeDef",
    "CreateSequenceStoreRequestRequestTypeDef",
    "CreateSequenceStoreResponseTypeDef",
    "CreateVariantStoreRequestRequestTypeDef",
    "GetReferenceStoreResponseTypeDef",
    "GetVariantStoreResponseTypeDef",
    "ReferenceStoreDetailTypeDef",
    "SequenceStoreDetailTypeDef",
    "VariantStoreItemTypeDef",
    "ListAnnotationStoreVersionsResponseTypeDef",
    "BatchDeleteReadSetResponseTypeDef",
    "UploadReadSetPartRequestRequestTypeDef",
    "CompleteMultipartReadSetUploadRequestRequestTypeDef",
    "CreateWorkflowRequestRequestTypeDef",
    "GetWorkflowResponseTypeDef",
    "DeleteAnnotationStoreVersionsResponseTypeDef",
    "GetReadSetExportJobResponseTypeDef",
    "ListReadSetExportJobsResponseTypeDef",
    "StartReadSetExportJobRequestRequestTypeDef",
    "FileInformationTypeDef",
    "ListSharesRequestRequestTypeDef",
    "GetAnnotationImportRequestAnnotationImportJobCreatedWaitTypeDef",
    "GetAnnotationStoreRequestAnnotationStoreCreatedWaitTypeDef",
    "GetAnnotationStoreRequestAnnotationStoreDeletedWaitTypeDef",
    "GetAnnotationStoreVersionRequestAnnotationStoreVersionCreatedWaitTypeDef",
    "GetAnnotationStoreVersionRequestAnnotationStoreVersionDeletedWaitTypeDef",
    "GetReadSetActivationJobRequestReadSetActivationJobCompletedWaitTypeDef",
    "GetReadSetExportJobRequestReadSetExportJobCompletedWaitTypeDef",
    "GetReadSetImportJobRequestReadSetImportJobCompletedWaitTypeDef",
    "GetReferenceImportJobRequestReferenceImportJobCompletedWaitTypeDef",
    "GetRunRequestRunCompletedWaitTypeDef",
    "GetRunRequestRunRunningWaitTypeDef",
    "GetRunTaskRequestTaskCompletedWaitTypeDef",
    "GetRunTaskRequestTaskRunningWaitTypeDef",
    "GetVariantImportRequestVariantImportJobCreatedWaitTypeDef",
    "GetVariantStoreRequestVariantStoreCreatedWaitTypeDef",
    "GetVariantStoreRequestVariantStoreDeletedWaitTypeDef",
    "GetWorkflowRequestWorkflowActiveWaitTypeDef",
    "ReadSetListItemTypeDef",
    "GetReferenceImportJobResponseTypeDef",
    "GetRunResponseTypeDef",
    "GetSequenceStoreResponseTypeDef",
    "GetShareResponseTypeDef",
    "ListSharesResponseTypeDef",
    "GetVariantImportResponseTypeDef",
    "ListReadSetImportJobsResponseTypeDef",
    "ImportReadSetSourceItemTypeDef",
    "StartReadSetImportJobSourceItemTypeDef",
    "ListReferenceImportJobsResponseTypeDef",
    "ListAnnotationImportJobsRequestRequestTypeDef",
    "ListAnnotationImportJobsRequestListAnnotationImportJobsPaginateTypeDef",
    "ListMultipartReadSetUploadsRequestListMultipartReadSetUploadsPaginateTypeDef",
    "ListRunGroupsRequestListRunGroupsPaginateTypeDef",
    "ListRunTasksRequestListRunTasksPaginateTypeDef",
    "ListRunsRequestListRunsPaginateTypeDef",
    "ListSharesRequestListSharesPaginateTypeDef",
    "ListWorkflowsRequestListWorkflowsPaginateTypeDef",
    "ListAnnotationStoreVersionsRequestListAnnotationStoreVersionsPaginateTypeDef",
    "ListAnnotationStoreVersionsRequestRequestTypeDef",
    "ListAnnotationStoresRequestListAnnotationStoresPaginateTypeDef",
    "ListAnnotationStoresRequestRequestTypeDef",
    "ListMultipartReadSetUploadsResponseTypeDef",
    "ListReadSetUploadPartsResponseTypeDef",
    "ListReferencesResponseTypeDef",
    "ListRunGroupsResponseTypeDef",
    "ListRunTasksResponseTypeDef",
    "ListRunsResponseTypeDef",
    "ListVariantImportJobsRequestListVariantImportJobsPaginateTypeDef",
    "ListVariantImportJobsRequestRequestTypeDef",
    "ListVariantImportJobsResponseTypeDef",
    "ListVariantStoresRequestListVariantStoresPaginateTypeDef",
    "ListVariantStoresRequestRequestTypeDef",
    "ListWorkflowsResponseTypeDef",
    "TsvOptionsTypeDef",
    "StartReadSetActivationJobRequestRequestTypeDef",
    "StartReferenceImportJobRequestRequestTypeDef",
    "StartVariantImportRequestRequestTypeDef",
    "StoreOptionsOutputTypeDef",
    "TsvStoreOptionsUnionTypeDef",
    "VersionOptionsOutputTypeDef",
    "TsvVersionOptionsUnionTypeDef",
    "ListReadSetActivationJobsRequestListReadSetActivationJobsPaginateTypeDef",
    "ListReadSetActivationJobsRequestRequestTypeDef",
    "ListReadSetExportJobsRequestListReadSetExportJobsPaginateTypeDef",
    "ListReadSetExportJobsRequestRequestTypeDef",
    "ListReadSetImportJobsRequestListReadSetImportJobsPaginateTypeDef",
    "ListReadSetImportJobsRequestRequestTypeDef",
    "ListReferenceImportJobsRequestListReferenceImportJobsPaginateTypeDef",
    "ListReferenceImportJobsRequestRequestTypeDef",
    "ListReadSetsRequestListReadSetsPaginateTypeDef",
    "ListReadSetsRequestRequestTypeDef",
    "ListReadSetUploadPartsRequestListReadSetUploadPartsPaginateTypeDef",
    "ListReadSetUploadPartsRequestRequestTypeDef",
    "ListReferencesRequestListReferencesPaginateTypeDef",
    "ListReferencesRequestRequestTypeDef",
    "ListReferenceStoresRequestListReferenceStoresPaginateTypeDef",
    "ListReferenceStoresRequestRequestTypeDef",
    "ListSequenceStoresRequestListSequenceStoresPaginateTypeDef",
    "ListSequenceStoresRequestRequestTypeDef",
    "ListAnnotationStoresResponseTypeDef",
    "ListReferenceStoresResponseTypeDef",
    "ListSequenceStoresResponseTypeDef",
    "ListVariantStoresResponseTypeDef",
    "ReadSetFilesTypeDef",
    "ReferenceFilesTypeDef",
    "ListReadSetsResponseTypeDef",
    "GetReadSetImportJobResponseTypeDef",
    "StartReadSetImportJobRequestRequestTypeDef",
    "FormatOptionsTypeDef",
    "CreateAnnotationStoreResponseTypeDef",
    "GetAnnotationStoreResponseTypeDef",
    "UpdateAnnotationStoreResponseTypeDef",
    "StoreOptionsTypeDef",
    "CreateAnnotationStoreVersionResponseTypeDef",
    "GetAnnotationStoreVersionResponseTypeDef",
    "VersionOptionsTypeDef",
    "GetReadSetMetadataResponseTypeDef",
    "GetReferenceMetadataResponseTypeDef",
    "GetAnnotationImportResponseTypeDef",
    "StartAnnotationImportRequestRequestTypeDef",
    "CreateAnnotationStoreRequestRequestTypeDef",
    "CreateAnnotationStoreVersionRequestRequestTypeDef",
)

AbortMultipartReadSetUploadRequestRequestTypeDef = TypedDict(
    "AbortMultipartReadSetUploadRequestRequestTypeDef",
    {
        "sequenceStoreId": str,
        "uploadId": str,
    },
)
AcceptShareRequestRequestTypeDef = TypedDict(
    "AcceptShareRequestRequestTypeDef",
    {
        "shareId": str,
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
TimestampTypeDef = Union[datetime, str]
ActivateReadSetJobItemTypeDef = TypedDict(
    "ActivateReadSetJobItemTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
        "status": ReadSetActivationJobStatusType,
        "creationTime": datetime,
        "completionTime": NotRequired[datetime],
    },
)
ActivateReadSetSourceItemTypeDef = TypedDict(
    "ActivateReadSetSourceItemTypeDef",
    {
        "readSetId": str,
        "status": ReadSetActivationJobItemStatusType,
        "statusMessage": NotRequired[str],
    },
)
AnnotationImportItemDetailTypeDef = TypedDict(
    "AnnotationImportItemDetailTypeDef",
    {
        "source": str,
        "jobStatus": JobStatusType,
    },
)
AnnotationImportItemSourceTypeDef = TypedDict(
    "AnnotationImportItemSourceTypeDef",
    {
        "source": str,
    },
)
AnnotationImportJobItemTypeDef = TypedDict(
    "AnnotationImportJobItemTypeDef",
    {
        "id": str,
        "destinationName": str,
        "versionName": str,
        "roleArn": str,
        "status": JobStatusType,
        "creationTime": datetime,
        "updateTime": datetime,
        "completionTime": NotRequired[datetime],
        "runLeftNormalization": NotRequired[bool],
        "annotationFields": NotRequired[Dict[str, str]],
    },
)
ReferenceItemTypeDef = TypedDict(
    "ReferenceItemTypeDef",
    {
        "referenceArn": NotRequired[str],
    },
)
SseConfigTypeDef = TypedDict(
    "SseConfigTypeDef",
    {
        "type": Literal["KMS"],
        "keyArn": NotRequired[str],
    },
)
AnnotationStoreVersionItemTypeDef = TypedDict(
    "AnnotationStoreVersionItemTypeDef",
    {
        "storeId": str,
        "id": str,
        "status": VersionStatusType,
        "versionArn": str,
        "name": str,
        "versionName": str,
        "description": str,
        "creationTime": datetime,
        "updateTime": datetime,
        "statusMessage": str,
        "versionSizeBytes": int,
    },
)
BatchDeleteReadSetRequestRequestTypeDef = TypedDict(
    "BatchDeleteReadSetRequestRequestTypeDef",
    {
        "ids": Sequence[str],
        "sequenceStoreId": str,
    },
)
ReadSetBatchErrorTypeDef = TypedDict(
    "ReadSetBatchErrorTypeDef",
    {
        "id": str,
        "code": str,
        "message": str,
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
CancelAnnotationImportRequestRequestTypeDef = TypedDict(
    "CancelAnnotationImportRequestRequestTypeDef",
    {
        "jobId": str,
    },
)
CancelRunRequestRequestTypeDef = TypedDict(
    "CancelRunRequestRequestTypeDef",
    {
        "id": str,
    },
)
CancelVariantImportRequestRequestTypeDef = TypedDict(
    "CancelVariantImportRequestRequestTypeDef",
    {
        "jobId": str,
    },
)
CompleteReadSetUploadPartListItemTypeDef = TypedDict(
    "CompleteReadSetUploadPartListItemTypeDef",
    {
        "partNumber": int,
        "partSource": ReadSetPartSourceType,
        "checksum": str,
    },
)
CreateMultipartReadSetUploadRequestRequestTypeDef = TypedDict(
    "CreateMultipartReadSetUploadRequestRequestTypeDef",
    {
        "sequenceStoreId": str,
        "sourceFileType": FileTypeType,
        "subjectId": str,
        "sampleId": str,
        "name": str,
        "clientToken": NotRequired[str],
        "generatedFrom": NotRequired[str],
        "referenceArn": NotRequired[str],
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateRunGroupRequestRequestTypeDef = TypedDict(
    "CreateRunGroupRequestRequestTypeDef",
    {
        "requestId": str,
        "name": NotRequired[str],
        "maxCpus": NotRequired[int],
        "maxRuns": NotRequired[int],
        "maxDuration": NotRequired[int],
        "tags": NotRequired[Mapping[str, str]],
        "maxGpus": NotRequired[int],
    },
)
CreateShareRequestRequestTypeDef = TypedDict(
    "CreateShareRequestRequestTypeDef",
    {
        "resourceArn": str,
        "principalSubscriber": str,
        "shareName": NotRequired[str],
    },
)
WorkflowParameterTypeDef = TypedDict(
    "WorkflowParameterTypeDef",
    {
        "description": NotRequired[str],
        "optional": NotRequired[bool],
    },
)
DeleteAnnotationStoreRequestRequestTypeDef = TypedDict(
    "DeleteAnnotationStoreRequestRequestTypeDef",
    {
        "name": str,
        "force": NotRequired[bool],
    },
)
DeleteAnnotationStoreVersionsRequestRequestTypeDef = TypedDict(
    "DeleteAnnotationStoreVersionsRequestRequestTypeDef",
    {
        "name": str,
        "versions": Sequence[str],
        "force": NotRequired[bool],
    },
)
VersionDeleteErrorTypeDef = TypedDict(
    "VersionDeleteErrorTypeDef",
    {
        "versionName": str,
        "message": str,
    },
)
DeleteReferenceRequestRequestTypeDef = TypedDict(
    "DeleteReferenceRequestRequestTypeDef",
    {
        "id": str,
        "referenceStoreId": str,
    },
)
DeleteReferenceStoreRequestRequestTypeDef = TypedDict(
    "DeleteReferenceStoreRequestRequestTypeDef",
    {
        "id": str,
    },
)
DeleteRunGroupRequestRequestTypeDef = TypedDict(
    "DeleteRunGroupRequestRequestTypeDef",
    {
        "id": str,
    },
)
DeleteRunRequestRequestTypeDef = TypedDict(
    "DeleteRunRequestRequestTypeDef",
    {
        "id": str,
    },
)
DeleteSequenceStoreRequestRequestTypeDef = TypedDict(
    "DeleteSequenceStoreRequestRequestTypeDef",
    {
        "id": str,
    },
)
DeleteShareRequestRequestTypeDef = TypedDict(
    "DeleteShareRequestRequestTypeDef",
    {
        "shareId": str,
    },
)
DeleteVariantStoreRequestRequestTypeDef = TypedDict(
    "DeleteVariantStoreRequestRequestTypeDef",
    {
        "name": str,
        "force": NotRequired[bool],
    },
)
DeleteWorkflowRequestRequestTypeDef = TypedDict(
    "DeleteWorkflowRequestRequestTypeDef",
    {
        "id": str,
    },
)
ETagTypeDef = TypedDict(
    "ETagTypeDef",
    {
        "algorithm": NotRequired[ETagAlgorithmType],
        "source1": NotRequired[str],
        "source2": NotRequired[str],
    },
)
ExportReadSetDetailTypeDef = TypedDict(
    "ExportReadSetDetailTypeDef",
    {
        "id": str,
        "status": ReadSetExportJobItemStatusType,
        "statusMessage": NotRequired[str],
    },
)
ExportReadSetJobDetailTypeDef = TypedDict(
    "ExportReadSetJobDetailTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
        "destination": str,
        "status": ReadSetExportJobStatusType,
        "creationTime": datetime,
        "completionTime": NotRequired[datetime],
    },
)
ExportReadSetTypeDef = TypedDict(
    "ExportReadSetTypeDef",
    {
        "readSetId": str,
    },
)
ReadSetS3AccessTypeDef = TypedDict(
    "ReadSetS3AccessTypeDef",
    {
        "s3Uri": NotRequired[str],
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "resourceArns": NotRequired[Sequence[str]],
        "status": NotRequired[Sequence[ShareStatusType]],
        "type": NotRequired[Sequence[ShareResourceTypeType]],
    },
)
VcfOptionsTypeDef = TypedDict(
    "VcfOptionsTypeDef",
    {
        "ignoreQualField": NotRequired[bool],
        "ignoreFilterField": NotRequired[bool],
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
GetAnnotationImportRequestRequestTypeDef = TypedDict(
    "GetAnnotationImportRequestRequestTypeDef",
    {
        "jobId": str,
    },
)
GetAnnotationStoreRequestRequestTypeDef = TypedDict(
    "GetAnnotationStoreRequestRequestTypeDef",
    {
        "name": str,
    },
)
GetAnnotationStoreVersionRequestRequestTypeDef = TypedDict(
    "GetAnnotationStoreVersionRequestRequestTypeDef",
    {
        "name": str,
        "versionName": str,
    },
)
GetReadSetActivationJobRequestRequestTypeDef = TypedDict(
    "GetReadSetActivationJobRequestRequestTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
    },
)
GetReadSetExportJobRequestRequestTypeDef = TypedDict(
    "GetReadSetExportJobRequestRequestTypeDef",
    {
        "sequenceStoreId": str,
        "id": str,
    },
)
GetReadSetImportJobRequestRequestTypeDef = TypedDict(
    "GetReadSetImportJobRequestRequestTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
    },
)
GetReadSetMetadataRequestRequestTypeDef = TypedDict(
    "GetReadSetMetadataRequestRequestTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
    },
)
SequenceInformationTypeDef = TypedDict(
    "SequenceInformationTypeDef",
    {
        "totalReadCount": NotRequired[int],
        "totalBaseCount": NotRequired[int],
        "generatedFrom": NotRequired[str],
        "alignment": NotRequired[str],
    },
)
GetReadSetRequestRequestTypeDef = TypedDict(
    "GetReadSetRequestRequestTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
        "partNumber": int,
        "file": NotRequired[ReadSetFileType],
    },
)
GetReferenceImportJobRequestRequestTypeDef = TypedDict(
    "GetReferenceImportJobRequestRequestTypeDef",
    {
        "id": str,
        "referenceStoreId": str,
    },
)
ImportReferenceSourceItemTypeDef = TypedDict(
    "ImportReferenceSourceItemTypeDef",
    {
        "status": ReferenceImportJobItemStatusType,
        "sourceFile": NotRequired[str],
        "statusMessage": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "referenceId": NotRequired[str],
    },
)
GetReferenceMetadataRequestRequestTypeDef = TypedDict(
    "GetReferenceMetadataRequestRequestTypeDef",
    {
        "id": str,
        "referenceStoreId": str,
    },
)
GetReferenceRequestRequestTypeDef = TypedDict(
    "GetReferenceRequestRequestTypeDef",
    {
        "id": str,
        "referenceStoreId": str,
        "partNumber": int,
        "range": NotRequired[str],
        "file": NotRequired[ReferenceFileType],
    },
)
GetReferenceStoreRequestRequestTypeDef = TypedDict(
    "GetReferenceStoreRequestRequestTypeDef",
    {
        "id": str,
    },
)
GetRunGroupRequestRequestTypeDef = TypedDict(
    "GetRunGroupRequestRequestTypeDef",
    {
        "id": str,
    },
)
GetRunRequestRequestTypeDef = TypedDict(
    "GetRunRequestRequestTypeDef",
    {
        "id": str,
        "export": NotRequired[Sequence[Literal["DEFINITION"]]],
    },
)
RunLogLocationTypeDef = TypedDict(
    "RunLogLocationTypeDef",
    {
        "engineLogStream": NotRequired[str],
        "runLogStream": NotRequired[str],
    },
)
GetRunTaskRequestRequestTypeDef = TypedDict(
    "GetRunTaskRequestRequestTypeDef",
    {
        "id": str,
        "taskId": str,
    },
)
GetSequenceStoreRequestRequestTypeDef = TypedDict(
    "GetSequenceStoreRequestRequestTypeDef",
    {
        "id": str,
    },
)
SequenceStoreS3AccessTypeDef = TypedDict(
    "SequenceStoreS3AccessTypeDef",
    {
        "s3Uri": NotRequired[str],
        "s3AccessPointArn": NotRequired[str],
    },
)
GetShareRequestRequestTypeDef = TypedDict(
    "GetShareRequestRequestTypeDef",
    {
        "shareId": str,
    },
)
ShareDetailsTypeDef = TypedDict(
    "ShareDetailsTypeDef",
    {
        "shareId": NotRequired[str],
        "resourceArn": NotRequired[str],
        "resourceId": NotRequired[str],
        "principalSubscriber": NotRequired[str],
        "ownerId": NotRequired[str],
        "status": NotRequired[ShareStatusType],
        "statusMessage": NotRequired[str],
        "shareName": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "updateTime": NotRequired[datetime],
    },
)
GetVariantImportRequestRequestTypeDef = TypedDict(
    "GetVariantImportRequestRequestTypeDef",
    {
        "jobId": str,
    },
)
VariantImportItemDetailTypeDef = TypedDict(
    "VariantImportItemDetailTypeDef",
    {
        "source": str,
        "jobStatus": JobStatusType,
        "statusMessage": NotRequired[str],
    },
)
GetVariantStoreRequestRequestTypeDef = TypedDict(
    "GetVariantStoreRequestRequestTypeDef",
    {
        "name": str,
    },
)
GetWorkflowRequestRequestTypeDef = TypedDict(
    "GetWorkflowRequestRequestTypeDef",
    {
        "id": str,
        "type": NotRequired[WorkflowTypeType],
        "export": NotRequired[Sequence[Literal["DEFINITION"]]],
        "workflowOwnerId": NotRequired[str],
    },
)
ImportReadSetJobItemTypeDef = TypedDict(
    "ImportReadSetJobItemTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
        "roleArn": str,
        "status": ReadSetImportJobStatusType,
        "creationTime": datetime,
        "completionTime": NotRequired[datetime],
    },
)
SourceFilesTypeDef = TypedDict(
    "SourceFilesTypeDef",
    {
        "source1": str,
        "source2": NotRequired[str],
    },
)
ImportReferenceJobItemTypeDef = TypedDict(
    "ImportReferenceJobItemTypeDef",
    {
        "id": str,
        "referenceStoreId": str,
        "roleArn": str,
        "status": ReferenceImportJobStatusType,
        "creationTime": datetime,
        "completionTime": NotRequired[datetime],
    },
)
ListAnnotationImportJobsFilterTypeDef = TypedDict(
    "ListAnnotationImportJobsFilterTypeDef",
    {
        "status": NotRequired[JobStatusType],
        "storeName": NotRequired[str],
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
ListAnnotationStoreVersionsFilterTypeDef = TypedDict(
    "ListAnnotationStoreVersionsFilterTypeDef",
    {
        "status": NotRequired[VersionStatusType],
    },
)
ListAnnotationStoresFilterTypeDef = TypedDict(
    "ListAnnotationStoresFilterTypeDef",
    {
        "status": NotRequired[StoreStatusType],
    },
)
ListMultipartReadSetUploadsRequestRequestTypeDef = TypedDict(
    "ListMultipartReadSetUploadsRequestRequestTypeDef",
    {
        "sequenceStoreId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
MultipartReadSetUploadListItemTypeDef = TypedDict(
    "MultipartReadSetUploadListItemTypeDef",
    {
        "sequenceStoreId": str,
        "uploadId": str,
        "sourceFileType": FileTypeType,
        "subjectId": str,
        "sampleId": str,
        "generatedFrom": str,
        "referenceArn": str,
        "creationTime": datetime,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)
ReadSetUploadPartListItemTypeDef = TypedDict(
    "ReadSetUploadPartListItemTypeDef",
    {
        "partNumber": int,
        "partSize": int,
        "partSource": ReadSetPartSourceType,
        "checksum": str,
        "creationTime": NotRequired[datetime],
        "lastUpdatedTime": NotRequired[datetime],
    },
)
ReferenceListItemTypeDef = TypedDict(
    "ReferenceListItemTypeDef",
    {
        "id": str,
        "arn": str,
        "referenceStoreId": str,
        "md5": str,
        "creationTime": datetime,
        "updateTime": datetime,
        "status": NotRequired[ReferenceStatusType],
        "name": NotRequired[str],
        "description": NotRequired[str],
    },
)
ListRunGroupsRequestRequestTypeDef = TypedDict(
    "ListRunGroupsRequestRequestTypeDef",
    {
        "name": NotRequired[str],
        "startingToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
RunGroupListItemTypeDef = TypedDict(
    "RunGroupListItemTypeDef",
    {
        "arn": NotRequired[str],
        "id": NotRequired[str],
        "name": NotRequired[str],
        "maxCpus": NotRequired[int],
        "maxRuns": NotRequired[int],
        "maxDuration": NotRequired[int],
        "creationTime": NotRequired[datetime],
        "maxGpus": NotRequired[int],
    },
)
ListRunTasksRequestRequestTypeDef = TypedDict(
    "ListRunTasksRequestRequestTypeDef",
    {
        "id": str,
        "status": NotRequired[TaskStatusType],
        "startingToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
TaskListItemTypeDef = TypedDict(
    "TaskListItemTypeDef",
    {
        "taskId": NotRequired[str],
        "status": NotRequired[TaskStatusType],
        "name": NotRequired[str],
        "cpus": NotRequired[int],
        "memory": NotRequired[int],
        "creationTime": NotRequired[datetime],
        "startTime": NotRequired[datetime],
        "stopTime": NotRequired[datetime],
        "gpus": NotRequired[int],
        "instanceType": NotRequired[str],
    },
)
ListRunsRequestRequestTypeDef = TypedDict(
    "ListRunsRequestRequestTypeDef",
    {
        "name": NotRequired[str],
        "runGroupId": NotRequired[str],
        "startingToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "status": NotRequired[RunStatusType],
    },
)
RunListItemTypeDef = TypedDict(
    "RunListItemTypeDef",
    {
        "arn": NotRequired[str],
        "id": NotRequired[str],
        "status": NotRequired[RunStatusType],
        "workflowId": NotRequired[str],
        "name": NotRequired[str],
        "priority": NotRequired[int],
        "storageCapacity": NotRequired[int],
        "creationTime": NotRequired[datetime],
        "startTime": NotRequired[datetime],
        "stopTime": NotRequired[datetime],
        "storageType": NotRequired[StorageTypeType],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
ListVariantImportJobsFilterTypeDef = TypedDict(
    "ListVariantImportJobsFilterTypeDef",
    {
        "status": NotRequired[JobStatusType],
        "storeName": NotRequired[str],
    },
)
VariantImportJobItemTypeDef = TypedDict(
    "VariantImportJobItemTypeDef",
    {
        "id": str,
        "destinationName": str,
        "roleArn": str,
        "status": JobStatusType,
        "creationTime": datetime,
        "updateTime": datetime,
        "completionTime": NotRequired[datetime],
        "runLeftNormalization": NotRequired[bool],
        "annotationFields": NotRequired[Dict[str, str]],
    },
)
ListVariantStoresFilterTypeDef = TypedDict(
    "ListVariantStoresFilterTypeDef",
    {
        "status": NotRequired[StoreStatusType],
    },
)
ListWorkflowsRequestRequestTypeDef = TypedDict(
    "ListWorkflowsRequestRequestTypeDef",
    {
        "type": NotRequired[WorkflowTypeType],
        "name": NotRequired[str],
        "startingToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
WorkflowListItemTypeDef = TypedDict(
    "WorkflowListItemTypeDef",
    {
        "arn": NotRequired[str],
        "id": NotRequired[str],
        "name": NotRequired[str],
        "status": NotRequired[WorkflowStatusType],
        "type": NotRequired[WorkflowTypeType],
        "digest": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "metadata": NotRequired[Dict[str, str]],
    },
)
ReadOptionsTypeDef = TypedDict(
    "ReadOptionsTypeDef",
    {
        "sep": NotRequired[str],
        "encoding": NotRequired[str],
        "quote": NotRequired[str],
        "quoteAll": NotRequired[bool],
        "escape": NotRequired[str],
        "escapeQuotes": NotRequired[bool],
        "comment": NotRequired[str],
        "header": NotRequired[bool],
        "lineSep": NotRequired[str],
    },
)
StartReadSetActivationJobSourceItemTypeDef = TypedDict(
    "StartReadSetActivationJobSourceItemTypeDef",
    {
        "readSetId": str,
    },
)
StartReferenceImportJobSourceItemTypeDef = TypedDict(
    "StartReferenceImportJobSourceItemTypeDef",
    {
        "sourceFile": str,
        "name": str,
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
StartRunRequestRequestTypeDef = TypedDict(
    "StartRunRequestRequestTypeDef",
    {
        "roleArn": str,
        "requestId": str,
        "workflowId": NotRequired[str],
        "workflowType": NotRequired[WorkflowTypeType],
        "runId": NotRequired[str],
        "name": NotRequired[str],
        "runGroupId": NotRequired[str],
        "priority": NotRequired[int],
        "parameters": NotRequired[Mapping[str, Any]],
        "storageCapacity": NotRequired[int],
        "outputUri": NotRequired[str],
        "logLevel": NotRequired[RunLogLevelType],
        "tags": NotRequired[Mapping[str, str]],
        "retentionMode": NotRequired[RunRetentionModeType],
        "storageType": NotRequired[StorageTypeType],
        "workflowOwnerId": NotRequired[str],
    },
)
VariantImportItemSourceTypeDef = TypedDict(
    "VariantImportItemSourceTypeDef",
    {
        "source": str,
    },
)
TsvStoreOptionsOutputTypeDef = TypedDict(
    "TsvStoreOptionsOutputTypeDef",
    {
        "annotationType": NotRequired[AnnotationTypeType],
        "formatToHeader": NotRequired[Dict[FormatToHeaderKeyType, str]],
        "schema": NotRequired[List[Dict[str, SchemaValueTypeType]]],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)
TsvStoreOptionsTypeDef = TypedDict(
    "TsvStoreOptionsTypeDef",
    {
        "annotationType": NotRequired[AnnotationTypeType],
        "formatToHeader": NotRequired[Mapping[FormatToHeaderKeyType, str]],
        "schema": NotRequired[Sequence[Mapping[str, SchemaValueTypeType]]],
    },
)
TsvVersionOptionsOutputTypeDef = TypedDict(
    "TsvVersionOptionsOutputTypeDef",
    {
        "annotationType": NotRequired[AnnotationTypeType],
        "formatToHeader": NotRequired[Dict[FormatToHeaderKeyType, str]],
        "schema": NotRequired[List[Dict[str, SchemaValueTypeType]]],
    },
)
TsvVersionOptionsTypeDef = TypedDict(
    "TsvVersionOptionsTypeDef",
    {
        "annotationType": NotRequired[AnnotationTypeType],
        "formatToHeader": NotRequired[Mapping[FormatToHeaderKeyType, str]],
        "schema": NotRequired[Sequence[Mapping[str, SchemaValueTypeType]]],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UpdateAnnotationStoreRequestRequestTypeDef = TypedDict(
    "UpdateAnnotationStoreRequestRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
    },
)
UpdateAnnotationStoreVersionRequestRequestTypeDef = TypedDict(
    "UpdateAnnotationStoreVersionRequestRequestTypeDef",
    {
        "name": str,
        "versionName": str,
        "description": NotRequired[str],
    },
)
UpdateRunGroupRequestRequestTypeDef = TypedDict(
    "UpdateRunGroupRequestRequestTypeDef",
    {
        "id": str,
        "name": NotRequired[str],
        "maxCpus": NotRequired[int],
        "maxRuns": NotRequired[int],
        "maxDuration": NotRequired[int],
        "maxGpus": NotRequired[int],
    },
)
UpdateVariantStoreRequestRequestTypeDef = TypedDict(
    "UpdateVariantStoreRequestRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
    },
)
UpdateWorkflowRequestRequestTypeDef = TypedDict(
    "UpdateWorkflowRequestRequestTypeDef",
    {
        "id": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
    },
)
AcceptShareResponseTypeDef = TypedDict(
    "AcceptShareResponseTypeDef",
    {
        "status": ShareStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CompleteMultipartReadSetUploadResponseTypeDef = TypedDict(
    "CompleteMultipartReadSetUploadResponseTypeDef",
    {
        "readSetId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMultipartReadSetUploadResponseTypeDef = TypedDict(
    "CreateMultipartReadSetUploadResponseTypeDef",
    {
        "sequenceStoreId": str,
        "uploadId": str,
        "sourceFileType": FileTypeType,
        "subjectId": str,
        "sampleId": str,
        "generatedFrom": str,
        "referenceArn": str,
        "name": str,
        "description": str,
        "tags": Dict[str, str],
        "creationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRunGroupResponseTypeDef = TypedDict(
    "CreateRunGroupResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateShareResponseTypeDef = TypedDict(
    "CreateShareResponseTypeDef",
    {
        "shareId": str,
        "status": ShareStatusType,
        "shareName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWorkflowResponseTypeDef = TypedDict(
    "CreateWorkflowResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "status": WorkflowStatusType,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteAnnotationStoreResponseTypeDef = TypedDict(
    "DeleteAnnotationStoreResponseTypeDef",
    {
        "status": StoreStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteShareResponseTypeDef = TypedDict(
    "DeleteShareResponseTypeDef",
    {
        "status": ShareStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteVariantStoreResponseTypeDef = TypedDict(
    "DeleteVariantStoreResponseTypeDef",
    {
        "status": StoreStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetReadSetResponseTypeDef = TypedDict(
    "GetReadSetResponseTypeDef",
    {
        "payload": StreamingBody,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetReferenceResponseTypeDef = TypedDict(
    "GetReferenceResponseTypeDef",
    {
        "payload": StreamingBody,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRunGroupResponseTypeDef = TypedDict(
    "GetRunGroupResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "maxCpus": int,
        "maxRuns": int,
        "maxDuration": int,
        "creationTime": datetime,
        "tags": Dict[str, str],
        "maxGpus": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRunTaskResponseTypeDef = TypedDict(
    "GetRunTaskResponseTypeDef",
    {
        "taskId": str,
        "status": TaskStatusType,
        "name": str,
        "cpus": int,
        "memory": int,
        "creationTime": datetime,
        "startTime": datetime,
        "stopTime": datetime,
        "statusMessage": str,
        "logStream": str,
        "gpus": int,
        "instanceType": str,
        "failureReason": str,
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
StartAnnotationImportResponseTypeDef = TypedDict(
    "StartAnnotationImportResponseTypeDef",
    {
        "jobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartReadSetActivationJobResponseTypeDef = TypedDict(
    "StartReadSetActivationJobResponseTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
        "status": ReadSetActivationJobStatusType,
        "creationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartReadSetExportJobResponseTypeDef = TypedDict(
    "StartReadSetExportJobResponseTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
        "destination": str,
        "status": ReadSetExportJobStatusType,
        "creationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartReadSetImportJobResponseTypeDef = TypedDict(
    "StartReadSetImportJobResponseTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
        "roleArn": str,
        "status": ReadSetImportJobStatusType,
        "creationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartReferenceImportJobResponseTypeDef = TypedDict(
    "StartReferenceImportJobResponseTypeDef",
    {
        "id": str,
        "referenceStoreId": str,
        "roleArn": str,
        "status": ReferenceImportJobStatusType,
        "creationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartRunResponseTypeDef = TypedDict(
    "StartRunResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "status": RunStatusType,
        "tags": Dict[str, str],
        "uuid": str,
        "runOutputUri": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartVariantImportResponseTypeDef = TypedDict(
    "StartVariantImportResponseTypeDef",
    {
        "jobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAnnotationStoreVersionResponseTypeDef = TypedDict(
    "UpdateAnnotationStoreVersionResponseTypeDef",
    {
        "storeId": str,
        "id": str,
        "status": VersionStatusType,
        "name": str,
        "versionName": str,
        "description": str,
        "creationTime": datetime,
        "updateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UploadReadSetPartResponseTypeDef = TypedDict(
    "UploadReadSetPartResponseTypeDef",
    {
        "checksum": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ActivateReadSetFilterTypeDef = TypedDict(
    "ActivateReadSetFilterTypeDef",
    {
        "status": NotRequired[ReadSetActivationJobStatusType],
        "createdAfter": NotRequired[TimestampTypeDef],
        "createdBefore": NotRequired[TimestampTypeDef],
    },
)
ExportReadSetFilterTypeDef = TypedDict(
    "ExportReadSetFilterTypeDef",
    {
        "status": NotRequired[ReadSetExportJobStatusType],
        "createdAfter": NotRequired[TimestampTypeDef],
        "createdBefore": NotRequired[TimestampTypeDef],
    },
)
ImportReadSetFilterTypeDef = TypedDict(
    "ImportReadSetFilterTypeDef",
    {
        "status": NotRequired[ReadSetImportJobStatusType],
        "createdAfter": NotRequired[TimestampTypeDef],
        "createdBefore": NotRequired[TimestampTypeDef],
    },
)
ImportReferenceFilterTypeDef = TypedDict(
    "ImportReferenceFilterTypeDef",
    {
        "status": NotRequired[ReferenceImportJobStatusType],
        "createdAfter": NotRequired[TimestampTypeDef],
        "createdBefore": NotRequired[TimestampTypeDef],
    },
)
ReadSetFilterTypeDef = TypedDict(
    "ReadSetFilterTypeDef",
    {
        "name": NotRequired[str],
        "status": NotRequired[ReadSetStatusType],
        "referenceArn": NotRequired[str],
        "createdAfter": NotRequired[TimestampTypeDef],
        "createdBefore": NotRequired[TimestampTypeDef],
        "sampleId": NotRequired[str],
        "subjectId": NotRequired[str],
        "generatedFrom": NotRequired[str],
        "creationType": NotRequired[CreationTypeType],
    },
)
ReadSetUploadPartListFilterTypeDef = TypedDict(
    "ReadSetUploadPartListFilterTypeDef",
    {
        "createdAfter": NotRequired[TimestampTypeDef],
        "createdBefore": NotRequired[TimestampTypeDef],
    },
)
ReferenceFilterTypeDef = TypedDict(
    "ReferenceFilterTypeDef",
    {
        "name": NotRequired[str],
        "md5": NotRequired[str],
        "createdAfter": NotRequired[TimestampTypeDef],
        "createdBefore": NotRequired[TimestampTypeDef],
    },
)
ReferenceStoreFilterTypeDef = TypedDict(
    "ReferenceStoreFilterTypeDef",
    {
        "name": NotRequired[str],
        "createdAfter": NotRequired[TimestampTypeDef],
        "createdBefore": NotRequired[TimestampTypeDef],
    },
)
SequenceStoreFilterTypeDef = TypedDict(
    "SequenceStoreFilterTypeDef",
    {
        "name": NotRequired[str],
        "createdAfter": NotRequired[TimestampTypeDef],
        "createdBefore": NotRequired[TimestampTypeDef],
    },
)
ListReadSetActivationJobsResponseTypeDef = TypedDict(
    "ListReadSetActivationJobsResponseTypeDef",
    {
        "nextToken": str,
        "activationJobs": List[ActivateReadSetJobItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetReadSetActivationJobResponseTypeDef = TypedDict(
    "GetReadSetActivationJobResponseTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
        "status": ReadSetActivationJobStatusType,
        "statusMessage": str,
        "creationTime": datetime,
        "completionTime": datetime,
        "sources": List[ActivateReadSetSourceItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAnnotationImportJobsResponseTypeDef = TypedDict(
    "ListAnnotationImportJobsResponseTypeDef",
    {
        "annotationImportJobs": List[AnnotationImportJobItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateVariantStoreResponseTypeDef = TypedDict(
    "CreateVariantStoreResponseTypeDef",
    {
        "id": str,
        "reference": ReferenceItemTypeDef,
        "status": StoreStatusType,
        "name": str,
        "creationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateVariantStoreResponseTypeDef = TypedDict(
    "UpdateVariantStoreResponseTypeDef",
    {
        "id": str,
        "reference": ReferenceItemTypeDef,
        "status": StoreStatusType,
        "name": str,
        "description": str,
        "creationTime": datetime,
        "updateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AnnotationStoreItemTypeDef = TypedDict(
    "AnnotationStoreItemTypeDef",
    {
        "id": str,
        "reference": ReferenceItemTypeDef,
        "status": StoreStatusType,
        "storeArn": str,
        "name": str,
        "storeFormat": StoreFormatType,
        "description": str,
        "sseConfig": SseConfigTypeDef,
        "creationTime": datetime,
        "updateTime": datetime,
        "statusMessage": str,
        "storeSizeBytes": int,
    },
)
CreateReferenceStoreRequestRequestTypeDef = TypedDict(
    "CreateReferenceStoreRequestRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "sseConfig": NotRequired[SseConfigTypeDef],
        "tags": NotRequired[Mapping[str, str]],
        "clientToken": NotRequired[str],
    },
)
CreateReferenceStoreResponseTypeDef = TypedDict(
    "CreateReferenceStoreResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "sseConfig": SseConfigTypeDef,
        "creationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSequenceStoreRequestRequestTypeDef = TypedDict(
    "CreateSequenceStoreRequestRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "sseConfig": NotRequired[SseConfigTypeDef],
        "tags": NotRequired[Mapping[str, str]],
        "clientToken": NotRequired[str],
        "fallbackLocation": NotRequired[str],
        "eTagAlgorithmFamily": NotRequired[ETagAlgorithmFamilyType],
    },
)
CreateSequenceStoreResponseTypeDef = TypedDict(
    "CreateSequenceStoreResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "sseConfig": SseConfigTypeDef,
        "creationTime": datetime,
        "fallbackLocation": str,
        "eTagAlgorithmFamily": ETagAlgorithmFamilyType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateVariantStoreRequestRequestTypeDef = TypedDict(
    "CreateVariantStoreRequestRequestTypeDef",
    {
        "reference": ReferenceItemTypeDef,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "sseConfig": NotRequired[SseConfigTypeDef],
    },
)
GetReferenceStoreResponseTypeDef = TypedDict(
    "GetReferenceStoreResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "sseConfig": SseConfigTypeDef,
        "creationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetVariantStoreResponseTypeDef = TypedDict(
    "GetVariantStoreResponseTypeDef",
    {
        "id": str,
        "reference": ReferenceItemTypeDef,
        "status": StoreStatusType,
        "storeArn": str,
        "name": str,
        "description": str,
        "sseConfig": SseConfigTypeDef,
        "creationTime": datetime,
        "updateTime": datetime,
        "tags": Dict[str, str],
        "statusMessage": str,
        "storeSizeBytes": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReferenceStoreDetailTypeDef = TypedDict(
    "ReferenceStoreDetailTypeDef",
    {
        "arn": str,
        "id": str,
        "creationTime": datetime,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "sseConfig": NotRequired[SseConfigTypeDef],
    },
)
SequenceStoreDetailTypeDef = TypedDict(
    "SequenceStoreDetailTypeDef",
    {
        "arn": str,
        "id": str,
        "creationTime": datetime,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "sseConfig": NotRequired[SseConfigTypeDef],
        "fallbackLocation": NotRequired[str],
        "eTagAlgorithmFamily": NotRequired[ETagAlgorithmFamilyType],
    },
)
VariantStoreItemTypeDef = TypedDict(
    "VariantStoreItemTypeDef",
    {
        "id": str,
        "reference": ReferenceItemTypeDef,
        "status": StoreStatusType,
        "storeArn": str,
        "name": str,
        "description": str,
        "sseConfig": SseConfigTypeDef,
        "creationTime": datetime,
        "updateTime": datetime,
        "statusMessage": str,
        "storeSizeBytes": int,
    },
)
ListAnnotationStoreVersionsResponseTypeDef = TypedDict(
    "ListAnnotationStoreVersionsResponseTypeDef",
    {
        "annotationStoreVersions": List[AnnotationStoreVersionItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDeleteReadSetResponseTypeDef = TypedDict(
    "BatchDeleteReadSetResponseTypeDef",
    {
        "errors": List[ReadSetBatchErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UploadReadSetPartRequestRequestTypeDef = TypedDict(
    "UploadReadSetPartRequestRequestTypeDef",
    {
        "sequenceStoreId": str,
        "uploadId": str,
        "partSource": ReadSetPartSourceType,
        "partNumber": int,
        "payload": BlobTypeDef,
    },
)
CompleteMultipartReadSetUploadRequestRequestTypeDef = TypedDict(
    "CompleteMultipartReadSetUploadRequestRequestTypeDef",
    {
        "sequenceStoreId": str,
        "uploadId": str,
        "parts": Sequence[CompleteReadSetUploadPartListItemTypeDef],
    },
)
CreateWorkflowRequestRequestTypeDef = TypedDict(
    "CreateWorkflowRequestRequestTypeDef",
    {
        "requestId": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "engine": NotRequired[WorkflowEngineType],
        "definitionZip": NotRequired[BlobTypeDef],
        "definitionUri": NotRequired[str],
        "main": NotRequired[str],
        "parameterTemplate": NotRequired[Mapping[str, WorkflowParameterTypeDef]],
        "storageCapacity": NotRequired[int],
        "tags": NotRequired[Mapping[str, str]],
        "accelerators": NotRequired[Literal["GPU"]],
    },
)
GetWorkflowResponseTypeDef = TypedDict(
    "GetWorkflowResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "status": WorkflowStatusType,
        "type": WorkflowTypeType,
        "name": str,
        "description": str,
        "engine": WorkflowEngineType,
        "definition": str,
        "main": str,
        "digest": str,
        "parameterTemplate": Dict[str, WorkflowParameterTypeDef],
        "storageCapacity": int,
        "creationTime": datetime,
        "statusMessage": str,
        "tags": Dict[str, str],
        "metadata": Dict[str, str],
        "accelerators": Literal["GPU"],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteAnnotationStoreVersionsResponseTypeDef = TypedDict(
    "DeleteAnnotationStoreVersionsResponseTypeDef",
    {
        "errors": List[VersionDeleteErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetReadSetExportJobResponseTypeDef = TypedDict(
    "GetReadSetExportJobResponseTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
        "destination": str,
        "status": ReadSetExportJobStatusType,
        "statusMessage": str,
        "creationTime": datetime,
        "completionTime": datetime,
        "readSets": List[ExportReadSetDetailTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListReadSetExportJobsResponseTypeDef = TypedDict(
    "ListReadSetExportJobsResponseTypeDef",
    {
        "nextToken": str,
        "exportJobs": List[ExportReadSetJobDetailTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartReadSetExportJobRequestRequestTypeDef = TypedDict(
    "StartReadSetExportJobRequestRequestTypeDef",
    {
        "sequenceStoreId": str,
        "destination": str,
        "roleArn": str,
        "sources": Sequence[ExportReadSetTypeDef],
        "clientToken": NotRequired[str],
    },
)
FileInformationTypeDef = TypedDict(
    "FileInformationTypeDef",
    {
        "totalParts": NotRequired[int],
        "partSize": NotRequired[int],
        "contentLength": NotRequired[int],
        "s3Access": NotRequired[ReadSetS3AccessTypeDef],
    },
)
ListSharesRequestRequestTypeDef = TypedDict(
    "ListSharesRequestRequestTypeDef",
    {
        "resourceOwner": ResourceOwnerType,
        "filter": NotRequired[FilterTypeDef],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
GetAnnotationImportRequestAnnotationImportJobCreatedWaitTypeDef = TypedDict(
    "GetAnnotationImportRequestAnnotationImportJobCreatedWaitTypeDef",
    {
        "jobId": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetAnnotationStoreRequestAnnotationStoreCreatedWaitTypeDef = TypedDict(
    "GetAnnotationStoreRequestAnnotationStoreCreatedWaitTypeDef",
    {
        "name": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetAnnotationStoreRequestAnnotationStoreDeletedWaitTypeDef = TypedDict(
    "GetAnnotationStoreRequestAnnotationStoreDeletedWaitTypeDef",
    {
        "name": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetAnnotationStoreVersionRequestAnnotationStoreVersionCreatedWaitTypeDef = TypedDict(
    "GetAnnotationStoreVersionRequestAnnotationStoreVersionCreatedWaitTypeDef",
    {
        "name": str,
        "versionName": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetAnnotationStoreVersionRequestAnnotationStoreVersionDeletedWaitTypeDef = TypedDict(
    "GetAnnotationStoreVersionRequestAnnotationStoreVersionDeletedWaitTypeDef",
    {
        "name": str,
        "versionName": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetReadSetActivationJobRequestReadSetActivationJobCompletedWaitTypeDef = TypedDict(
    "GetReadSetActivationJobRequestReadSetActivationJobCompletedWaitTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetReadSetExportJobRequestReadSetExportJobCompletedWaitTypeDef = TypedDict(
    "GetReadSetExportJobRequestReadSetExportJobCompletedWaitTypeDef",
    {
        "sequenceStoreId": str,
        "id": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetReadSetImportJobRequestReadSetImportJobCompletedWaitTypeDef = TypedDict(
    "GetReadSetImportJobRequestReadSetImportJobCompletedWaitTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetReferenceImportJobRequestReferenceImportJobCompletedWaitTypeDef = TypedDict(
    "GetReferenceImportJobRequestReferenceImportJobCompletedWaitTypeDef",
    {
        "id": str,
        "referenceStoreId": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetRunRequestRunCompletedWaitTypeDef = TypedDict(
    "GetRunRequestRunCompletedWaitTypeDef",
    {
        "id": str,
        "export": NotRequired[Sequence[Literal["DEFINITION"]]],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetRunRequestRunRunningWaitTypeDef = TypedDict(
    "GetRunRequestRunRunningWaitTypeDef",
    {
        "id": str,
        "export": NotRequired[Sequence[Literal["DEFINITION"]]],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetRunTaskRequestTaskCompletedWaitTypeDef = TypedDict(
    "GetRunTaskRequestTaskCompletedWaitTypeDef",
    {
        "id": str,
        "taskId": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetRunTaskRequestTaskRunningWaitTypeDef = TypedDict(
    "GetRunTaskRequestTaskRunningWaitTypeDef",
    {
        "id": str,
        "taskId": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetVariantImportRequestVariantImportJobCreatedWaitTypeDef = TypedDict(
    "GetVariantImportRequestVariantImportJobCreatedWaitTypeDef",
    {
        "jobId": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetVariantStoreRequestVariantStoreCreatedWaitTypeDef = TypedDict(
    "GetVariantStoreRequestVariantStoreCreatedWaitTypeDef",
    {
        "name": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetVariantStoreRequestVariantStoreDeletedWaitTypeDef = TypedDict(
    "GetVariantStoreRequestVariantStoreDeletedWaitTypeDef",
    {
        "name": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetWorkflowRequestWorkflowActiveWaitTypeDef = TypedDict(
    "GetWorkflowRequestWorkflowActiveWaitTypeDef",
    {
        "id": str,
        "type": NotRequired[WorkflowTypeType],
        "export": NotRequired[Sequence[Literal["DEFINITION"]]],
        "workflowOwnerId": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
ReadSetListItemTypeDef = TypedDict(
    "ReadSetListItemTypeDef",
    {
        "id": str,
        "arn": str,
        "sequenceStoreId": str,
        "status": ReadSetStatusType,
        "fileType": FileTypeType,
        "creationTime": datetime,
        "subjectId": NotRequired[str],
        "sampleId": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "referenceArn": NotRequired[str],
        "sequenceInformation": NotRequired[SequenceInformationTypeDef],
        "statusMessage": NotRequired[str],
        "creationType": NotRequired[CreationTypeType],
        "etag": NotRequired[ETagTypeDef],
    },
)
GetReferenceImportJobResponseTypeDef = TypedDict(
    "GetReferenceImportJobResponseTypeDef",
    {
        "id": str,
        "referenceStoreId": str,
        "roleArn": str,
        "status": ReferenceImportJobStatusType,
        "statusMessage": str,
        "creationTime": datetime,
        "completionTime": datetime,
        "sources": List[ImportReferenceSourceItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRunResponseTypeDef = TypedDict(
    "GetRunResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "status": RunStatusType,
        "workflowId": str,
        "workflowType": WorkflowTypeType,
        "runId": str,
        "roleArn": str,
        "name": str,
        "runGroupId": str,
        "priority": int,
        "definition": str,
        "digest": str,
        "parameters": Dict[str, Any],
        "storageCapacity": int,
        "outputUri": str,
        "logLevel": RunLogLevelType,
        "resourceDigests": Dict[str, str],
        "startedBy": str,
        "creationTime": datetime,
        "startTime": datetime,
        "stopTime": datetime,
        "statusMessage": str,
        "tags": Dict[str, str],
        "accelerators": Literal["GPU"],
        "retentionMode": RunRetentionModeType,
        "failureReason": str,
        "logLocation": RunLogLocationTypeDef,
        "uuid": str,
        "runOutputUri": str,
        "storageType": StorageTypeType,
        "workflowOwnerId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSequenceStoreResponseTypeDef = TypedDict(
    "GetSequenceStoreResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "sseConfig": SseConfigTypeDef,
        "creationTime": datetime,
        "fallbackLocation": str,
        "s3Access": SequenceStoreS3AccessTypeDef,
        "eTagAlgorithmFamily": ETagAlgorithmFamilyType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetShareResponseTypeDef = TypedDict(
    "GetShareResponseTypeDef",
    {
        "share": ShareDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSharesResponseTypeDef = TypedDict(
    "ListSharesResponseTypeDef",
    {
        "shares": List[ShareDetailsTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetVariantImportResponseTypeDef = TypedDict(
    "GetVariantImportResponseTypeDef",
    {
        "id": str,
        "destinationName": str,
        "roleArn": str,
        "status": JobStatusType,
        "statusMessage": str,
        "creationTime": datetime,
        "updateTime": datetime,
        "completionTime": datetime,
        "items": List[VariantImportItemDetailTypeDef],
        "runLeftNormalization": bool,
        "annotationFields": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListReadSetImportJobsResponseTypeDef = TypedDict(
    "ListReadSetImportJobsResponseTypeDef",
    {
        "nextToken": str,
        "importJobs": List[ImportReadSetJobItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportReadSetSourceItemTypeDef = TypedDict(
    "ImportReadSetSourceItemTypeDef",
    {
        "sourceFiles": SourceFilesTypeDef,
        "sourceFileType": FileTypeType,
        "status": ReadSetImportJobItemStatusType,
        "subjectId": str,
        "sampleId": str,
        "statusMessage": NotRequired[str],
        "generatedFrom": NotRequired[str],
        "referenceArn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "readSetId": NotRequired[str],
    },
)
StartReadSetImportJobSourceItemTypeDef = TypedDict(
    "StartReadSetImportJobSourceItemTypeDef",
    {
        "sourceFiles": SourceFilesTypeDef,
        "sourceFileType": FileTypeType,
        "subjectId": str,
        "sampleId": str,
        "generatedFrom": NotRequired[str],
        "referenceArn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
ListReferenceImportJobsResponseTypeDef = TypedDict(
    "ListReferenceImportJobsResponseTypeDef",
    {
        "nextToken": str,
        "importJobs": List[ImportReferenceJobItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAnnotationImportJobsRequestRequestTypeDef = TypedDict(
    "ListAnnotationImportJobsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "ids": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "filter": NotRequired[ListAnnotationImportJobsFilterTypeDef],
    },
)
ListAnnotationImportJobsRequestListAnnotationImportJobsPaginateTypeDef = TypedDict(
    "ListAnnotationImportJobsRequestListAnnotationImportJobsPaginateTypeDef",
    {
        "ids": NotRequired[Sequence[str]],
        "filter": NotRequired[ListAnnotationImportJobsFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMultipartReadSetUploadsRequestListMultipartReadSetUploadsPaginateTypeDef = TypedDict(
    "ListMultipartReadSetUploadsRequestListMultipartReadSetUploadsPaginateTypeDef",
    {
        "sequenceStoreId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRunGroupsRequestListRunGroupsPaginateTypeDef = TypedDict(
    "ListRunGroupsRequestListRunGroupsPaginateTypeDef",
    {
        "name": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRunTasksRequestListRunTasksPaginateTypeDef = TypedDict(
    "ListRunTasksRequestListRunTasksPaginateTypeDef",
    {
        "id": str,
        "status": NotRequired[TaskStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRunsRequestListRunsPaginateTypeDef = TypedDict(
    "ListRunsRequestListRunsPaginateTypeDef",
    {
        "name": NotRequired[str],
        "runGroupId": NotRequired[str],
        "status": NotRequired[RunStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSharesRequestListSharesPaginateTypeDef = TypedDict(
    "ListSharesRequestListSharesPaginateTypeDef",
    {
        "resourceOwner": ResourceOwnerType,
        "filter": NotRequired[FilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWorkflowsRequestListWorkflowsPaginateTypeDef = TypedDict(
    "ListWorkflowsRequestListWorkflowsPaginateTypeDef",
    {
        "type": NotRequired[WorkflowTypeType],
        "name": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAnnotationStoreVersionsRequestListAnnotationStoreVersionsPaginateTypeDef = TypedDict(
    "ListAnnotationStoreVersionsRequestListAnnotationStoreVersionsPaginateTypeDef",
    {
        "name": str,
        "filter": NotRequired[ListAnnotationStoreVersionsFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAnnotationStoreVersionsRequestRequestTypeDef = TypedDict(
    "ListAnnotationStoreVersionsRequestRequestTypeDef",
    {
        "name": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "filter": NotRequired[ListAnnotationStoreVersionsFilterTypeDef],
    },
)
ListAnnotationStoresRequestListAnnotationStoresPaginateTypeDef = TypedDict(
    "ListAnnotationStoresRequestListAnnotationStoresPaginateTypeDef",
    {
        "ids": NotRequired[Sequence[str]],
        "filter": NotRequired[ListAnnotationStoresFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAnnotationStoresRequestRequestTypeDef = TypedDict(
    "ListAnnotationStoresRequestRequestTypeDef",
    {
        "ids": NotRequired[Sequence[str]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "filter": NotRequired[ListAnnotationStoresFilterTypeDef],
    },
)
ListMultipartReadSetUploadsResponseTypeDef = TypedDict(
    "ListMultipartReadSetUploadsResponseTypeDef",
    {
        "nextToken": str,
        "uploads": List[MultipartReadSetUploadListItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListReadSetUploadPartsResponseTypeDef = TypedDict(
    "ListReadSetUploadPartsResponseTypeDef",
    {
        "nextToken": str,
        "parts": List[ReadSetUploadPartListItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListReferencesResponseTypeDef = TypedDict(
    "ListReferencesResponseTypeDef",
    {
        "nextToken": str,
        "references": List[ReferenceListItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRunGroupsResponseTypeDef = TypedDict(
    "ListRunGroupsResponseTypeDef",
    {
        "items": List[RunGroupListItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRunTasksResponseTypeDef = TypedDict(
    "ListRunTasksResponseTypeDef",
    {
        "items": List[TaskListItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRunsResponseTypeDef = TypedDict(
    "ListRunsResponseTypeDef",
    {
        "items": List[RunListItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListVariantImportJobsRequestListVariantImportJobsPaginateTypeDef = TypedDict(
    "ListVariantImportJobsRequestListVariantImportJobsPaginateTypeDef",
    {
        "ids": NotRequired[Sequence[str]],
        "filter": NotRequired[ListVariantImportJobsFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListVariantImportJobsRequestRequestTypeDef = TypedDict(
    "ListVariantImportJobsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "ids": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "filter": NotRequired[ListVariantImportJobsFilterTypeDef],
    },
)
ListVariantImportJobsResponseTypeDef = TypedDict(
    "ListVariantImportJobsResponseTypeDef",
    {
        "variantImportJobs": List[VariantImportJobItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListVariantStoresRequestListVariantStoresPaginateTypeDef = TypedDict(
    "ListVariantStoresRequestListVariantStoresPaginateTypeDef",
    {
        "ids": NotRequired[Sequence[str]],
        "filter": NotRequired[ListVariantStoresFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListVariantStoresRequestRequestTypeDef = TypedDict(
    "ListVariantStoresRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "ids": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "filter": NotRequired[ListVariantStoresFilterTypeDef],
    },
)
ListWorkflowsResponseTypeDef = TypedDict(
    "ListWorkflowsResponseTypeDef",
    {
        "items": List[WorkflowListItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TsvOptionsTypeDef = TypedDict(
    "TsvOptionsTypeDef",
    {
        "readOptions": NotRequired[ReadOptionsTypeDef],
    },
)
StartReadSetActivationJobRequestRequestTypeDef = TypedDict(
    "StartReadSetActivationJobRequestRequestTypeDef",
    {
        "sequenceStoreId": str,
        "sources": Sequence[StartReadSetActivationJobSourceItemTypeDef],
        "clientToken": NotRequired[str],
    },
)
StartReferenceImportJobRequestRequestTypeDef = TypedDict(
    "StartReferenceImportJobRequestRequestTypeDef",
    {
        "referenceStoreId": str,
        "roleArn": str,
        "sources": Sequence[StartReferenceImportJobSourceItemTypeDef],
        "clientToken": NotRequired[str],
    },
)
StartVariantImportRequestRequestTypeDef = TypedDict(
    "StartVariantImportRequestRequestTypeDef",
    {
        "destinationName": str,
        "roleArn": str,
        "items": Sequence[VariantImportItemSourceTypeDef],
        "runLeftNormalization": NotRequired[bool],
        "annotationFields": NotRequired[Mapping[str, str]],
    },
)
StoreOptionsOutputTypeDef = TypedDict(
    "StoreOptionsOutputTypeDef",
    {
        "tsvStoreOptions": NotRequired[TsvStoreOptionsOutputTypeDef],
    },
)
TsvStoreOptionsUnionTypeDef = Union[TsvStoreOptionsTypeDef, TsvStoreOptionsOutputTypeDef]
VersionOptionsOutputTypeDef = TypedDict(
    "VersionOptionsOutputTypeDef",
    {
        "tsvVersionOptions": NotRequired[TsvVersionOptionsOutputTypeDef],
    },
)
TsvVersionOptionsUnionTypeDef = Union[TsvVersionOptionsTypeDef, TsvVersionOptionsOutputTypeDef]
ListReadSetActivationJobsRequestListReadSetActivationJobsPaginateTypeDef = TypedDict(
    "ListReadSetActivationJobsRequestListReadSetActivationJobsPaginateTypeDef",
    {
        "sequenceStoreId": str,
        "filter": NotRequired[ActivateReadSetFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListReadSetActivationJobsRequestRequestTypeDef = TypedDict(
    "ListReadSetActivationJobsRequestRequestTypeDef",
    {
        "sequenceStoreId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "filter": NotRequired[ActivateReadSetFilterTypeDef],
    },
)
ListReadSetExportJobsRequestListReadSetExportJobsPaginateTypeDef = TypedDict(
    "ListReadSetExportJobsRequestListReadSetExportJobsPaginateTypeDef",
    {
        "sequenceStoreId": str,
        "filter": NotRequired[ExportReadSetFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListReadSetExportJobsRequestRequestTypeDef = TypedDict(
    "ListReadSetExportJobsRequestRequestTypeDef",
    {
        "sequenceStoreId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "filter": NotRequired[ExportReadSetFilterTypeDef],
    },
)
ListReadSetImportJobsRequestListReadSetImportJobsPaginateTypeDef = TypedDict(
    "ListReadSetImportJobsRequestListReadSetImportJobsPaginateTypeDef",
    {
        "sequenceStoreId": str,
        "filter": NotRequired[ImportReadSetFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListReadSetImportJobsRequestRequestTypeDef = TypedDict(
    "ListReadSetImportJobsRequestRequestTypeDef",
    {
        "sequenceStoreId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "filter": NotRequired[ImportReadSetFilterTypeDef],
    },
)
ListReferenceImportJobsRequestListReferenceImportJobsPaginateTypeDef = TypedDict(
    "ListReferenceImportJobsRequestListReferenceImportJobsPaginateTypeDef",
    {
        "referenceStoreId": str,
        "filter": NotRequired[ImportReferenceFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListReferenceImportJobsRequestRequestTypeDef = TypedDict(
    "ListReferenceImportJobsRequestRequestTypeDef",
    {
        "referenceStoreId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "filter": NotRequired[ImportReferenceFilterTypeDef],
    },
)
ListReadSetsRequestListReadSetsPaginateTypeDef = TypedDict(
    "ListReadSetsRequestListReadSetsPaginateTypeDef",
    {
        "sequenceStoreId": str,
        "filter": NotRequired[ReadSetFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListReadSetsRequestRequestTypeDef = TypedDict(
    "ListReadSetsRequestRequestTypeDef",
    {
        "sequenceStoreId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "filter": NotRequired[ReadSetFilterTypeDef],
    },
)
ListReadSetUploadPartsRequestListReadSetUploadPartsPaginateTypeDef = TypedDict(
    "ListReadSetUploadPartsRequestListReadSetUploadPartsPaginateTypeDef",
    {
        "sequenceStoreId": str,
        "uploadId": str,
        "partSource": ReadSetPartSourceType,
        "filter": NotRequired[ReadSetUploadPartListFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListReadSetUploadPartsRequestRequestTypeDef = TypedDict(
    "ListReadSetUploadPartsRequestRequestTypeDef",
    {
        "sequenceStoreId": str,
        "uploadId": str,
        "partSource": ReadSetPartSourceType,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "filter": NotRequired[ReadSetUploadPartListFilterTypeDef],
    },
)
ListReferencesRequestListReferencesPaginateTypeDef = TypedDict(
    "ListReferencesRequestListReferencesPaginateTypeDef",
    {
        "referenceStoreId": str,
        "filter": NotRequired[ReferenceFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListReferencesRequestRequestTypeDef = TypedDict(
    "ListReferencesRequestRequestTypeDef",
    {
        "referenceStoreId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "filter": NotRequired[ReferenceFilterTypeDef],
    },
)
ListReferenceStoresRequestListReferenceStoresPaginateTypeDef = TypedDict(
    "ListReferenceStoresRequestListReferenceStoresPaginateTypeDef",
    {
        "filter": NotRequired[ReferenceStoreFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListReferenceStoresRequestRequestTypeDef = TypedDict(
    "ListReferenceStoresRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "filter": NotRequired[ReferenceStoreFilterTypeDef],
    },
)
ListSequenceStoresRequestListSequenceStoresPaginateTypeDef = TypedDict(
    "ListSequenceStoresRequestListSequenceStoresPaginateTypeDef",
    {
        "filter": NotRequired[SequenceStoreFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSequenceStoresRequestRequestTypeDef = TypedDict(
    "ListSequenceStoresRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "filter": NotRequired[SequenceStoreFilterTypeDef],
    },
)
ListAnnotationStoresResponseTypeDef = TypedDict(
    "ListAnnotationStoresResponseTypeDef",
    {
        "annotationStores": List[AnnotationStoreItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListReferenceStoresResponseTypeDef = TypedDict(
    "ListReferenceStoresResponseTypeDef",
    {
        "nextToken": str,
        "referenceStores": List[ReferenceStoreDetailTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSequenceStoresResponseTypeDef = TypedDict(
    "ListSequenceStoresResponseTypeDef",
    {
        "nextToken": str,
        "sequenceStores": List[SequenceStoreDetailTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListVariantStoresResponseTypeDef = TypedDict(
    "ListVariantStoresResponseTypeDef",
    {
        "variantStores": List[VariantStoreItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ReadSetFilesTypeDef = TypedDict(
    "ReadSetFilesTypeDef",
    {
        "source1": NotRequired[FileInformationTypeDef],
        "source2": NotRequired[FileInformationTypeDef],
        "index": NotRequired[FileInformationTypeDef],
    },
)
ReferenceFilesTypeDef = TypedDict(
    "ReferenceFilesTypeDef",
    {
        "source": NotRequired[FileInformationTypeDef],
        "index": NotRequired[FileInformationTypeDef],
    },
)
ListReadSetsResponseTypeDef = TypedDict(
    "ListReadSetsResponseTypeDef",
    {
        "nextToken": str,
        "readSets": List[ReadSetListItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetReadSetImportJobResponseTypeDef = TypedDict(
    "GetReadSetImportJobResponseTypeDef",
    {
        "id": str,
        "sequenceStoreId": str,
        "roleArn": str,
        "status": ReadSetImportJobStatusType,
        "statusMessage": str,
        "creationTime": datetime,
        "completionTime": datetime,
        "sources": List[ImportReadSetSourceItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartReadSetImportJobRequestRequestTypeDef = TypedDict(
    "StartReadSetImportJobRequestRequestTypeDef",
    {
        "sequenceStoreId": str,
        "roleArn": str,
        "sources": Sequence[StartReadSetImportJobSourceItemTypeDef],
        "clientToken": NotRequired[str],
    },
)
FormatOptionsTypeDef = TypedDict(
    "FormatOptionsTypeDef",
    {
        "tsvOptions": NotRequired[TsvOptionsTypeDef],
        "vcfOptions": NotRequired[VcfOptionsTypeDef],
    },
)
CreateAnnotationStoreResponseTypeDef = TypedDict(
    "CreateAnnotationStoreResponseTypeDef",
    {
        "id": str,
        "reference": ReferenceItemTypeDef,
        "storeFormat": StoreFormatType,
        "storeOptions": StoreOptionsOutputTypeDef,
        "status": StoreStatusType,
        "name": str,
        "versionName": str,
        "creationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAnnotationStoreResponseTypeDef = TypedDict(
    "GetAnnotationStoreResponseTypeDef",
    {
        "id": str,
        "reference": ReferenceItemTypeDef,
        "status": StoreStatusType,
        "storeArn": str,
        "name": str,
        "description": str,
        "sseConfig": SseConfigTypeDef,
        "creationTime": datetime,
        "updateTime": datetime,
        "tags": Dict[str, str],
        "storeOptions": StoreOptionsOutputTypeDef,
        "storeFormat": StoreFormatType,
        "statusMessage": str,
        "storeSizeBytes": int,
        "numVersions": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAnnotationStoreResponseTypeDef = TypedDict(
    "UpdateAnnotationStoreResponseTypeDef",
    {
        "id": str,
        "reference": ReferenceItemTypeDef,
        "status": StoreStatusType,
        "name": str,
        "description": str,
        "creationTime": datetime,
        "updateTime": datetime,
        "storeOptions": StoreOptionsOutputTypeDef,
        "storeFormat": StoreFormatType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StoreOptionsTypeDef = TypedDict(
    "StoreOptionsTypeDef",
    {
        "tsvStoreOptions": NotRequired[TsvStoreOptionsUnionTypeDef],
    },
)
CreateAnnotationStoreVersionResponseTypeDef = TypedDict(
    "CreateAnnotationStoreVersionResponseTypeDef",
    {
        "id": str,
        "versionName": str,
        "storeId": str,
        "versionOptions": VersionOptionsOutputTypeDef,
        "name": str,
        "status": VersionStatusType,
        "creationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAnnotationStoreVersionResponseTypeDef = TypedDict(
    "GetAnnotationStoreVersionResponseTypeDef",
    {
        "storeId": str,
        "id": str,
        "status": VersionStatusType,
        "versionArn": str,
        "name": str,
        "versionName": str,
        "description": str,
        "creationTime": datetime,
        "updateTime": datetime,
        "tags": Dict[str, str],
        "versionOptions": VersionOptionsOutputTypeDef,
        "statusMessage": str,
        "versionSizeBytes": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VersionOptionsTypeDef = TypedDict(
    "VersionOptionsTypeDef",
    {
        "tsvVersionOptions": NotRequired[TsvVersionOptionsUnionTypeDef],
    },
)
GetReadSetMetadataResponseTypeDef = TypedDict(
    "GetReadSetMetadataResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "sequenceStoreId": str,
        "subjectId": str,
        "sampleId": str,
        "status": ReadSetStatusType,
        "name": str,
        "description": str,
        "fileType": FileTypeType,
        "creationTime": datetime,
        "sequenceInformation": SequenceInformationTypeDef,
        "referenceArn": str,
        "files": ReadSetFilesTypeDef,
        "statusMessage": str,
        "creationType": CreationTypeType,
        "etag": ETagTypeDef,
        "creationJobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetReferenceMetadataResponseTypeDef = TypedDict(
    "GetReferenceMetadataResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "referenceStoreId": str,
        "md5": str,
        "status": ReferenceStatusType,
        "name": str,
        "description": str,
        "creationTime": datetime,
        "updateTime": datetime,
        "files": ReferenceFilesTypeDef,
        "creationType": Literal["IMPORT"],
        "creationJobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAnnotationImportResponseTypeDef = TypedDict(
    "GetAnnotationImportResponseTypeDef",
    {
        "id": str,
        "destinationName": str,
        "versionName": str,
        "roleArn": str,
        "status": JobStatusType,
        "statusMessage": str,
        "creationTime": datetime,
        "updateTime": datetime,
        "completionTime": datetime,
        "items": List[AnnotationImportItemDetailTypeDef],
        "runLeftNormalization": bool,
        "formatOptions": FormatOptionsTypeDef,
        "annotationFields": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartAnnotationImportRequestRequestTypeDef = TypedDict(
    "StartAnnotationImportRequestRequestTypeDef",
    {
        "destinationName": str,
        "roleArn": str,
        "items": Sequence[AnnotationImportItemSourceTypeDef],
        "versionName": NotRequired[str],
        "formatOptions": NotRequired[FormatOptionsTypeDef],
        "runLeftNormalization": NotRequired[bool],
        "annotationFields": NotRequired[Mapping[str, str]],
    },
)
CreateAnnotationStoreRequestRequestTypeDef = TypedDict(
    "CreateAnnotationStoreRequestRequestTypeDef",
    {
        "storeFormat": StoreFormatType,
        "reference": NotRequired[ReferenceItemTypeDef],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "versionName": NotRequired[str],
        "sseConfig": NotRequired[SseConfigTypeDef],
        "storeOptions": NotRequired[StoreOptionsTypeDef],
    },
)
CreateAnnotationStoreVersionRequestRequestTypeDef = TypedDict(
    "CreateAnnotationStoreVersionRequestRequestTypeDef",
    {
        "name": str,
        "versionName": str,
        "description": NotRequired[str],
        "versionOptions": NotRequired[VersionOptionsTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
