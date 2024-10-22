# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "DatasetFinalizeFileUploadsResponse",
    "DatasetFile",
    "DatasetFileID",
    "DatasetFileColumn",
    "DatasetFileColumnID",
    "DatasetFileDatasetID",
]


class DatasetFileID(BaseModel):
    value: str


class DatasetFileColumnID(BaseModel):
    value: str


class DatasetFileColumn(BaseModel):
    id: DatasetFileColumnID

    created_at: datetime = FieldInfo(alias="createdAt")

    index: int
    """Index of the column within the dataset file."""

    literal_name: str = FieldInfo(alias="literalName")
    """The literal name for the column."""

    updated_at: datetime = FieldInfo(alias="updatedAt")

    dtype: Optional[str] = None


class DatasetFileDatasetID(BaseModel):
    value: str


class DatasetFile(BaseModel):
    id: DatasetFileID

    columns: List[DatasetFileColumn]

    content_md5_hash: str = FieldInfo(alias="contentMd5Hash")

    created_at: datetime = FieldInfo(alias="createdAt")

    dataset_id: DatasetFileDatasetID = FieldInfo(alias="datasetId")

    file_size_bytes: int = FieldInfo(alias="fileSizeBytes")

    num_cols: int = FieldInfo(alias="numCols")

    num_rows: int = FieldInfo(alias="numRows")

    updated_at: datetime = FieldInfo(alias="updatedAt")


class DatasetFinalizeFileUploadsResponse(BaseModel):
    remaining_upload_urls: List[str] = FieldInfo(alias="remainingUploadUrls")
    """If there are remaining incomplete uploads, this represents those URLs."""

    dataset_file: Optional[DatasetFile] = FieldInfo(alias="datasetFile", default=None)
