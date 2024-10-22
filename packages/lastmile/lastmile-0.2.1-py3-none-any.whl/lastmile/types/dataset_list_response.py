# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DatasetListResponse", "Dataset", "DatasetID", "DatasetColumn", "DatasetColumnID", "DatasetOwnerUserID"]


class DatasetID(BaseModel):
    value: str


class DatasetColumnID(BaseModel):
    value: str


class DatasetColumn(BaseModel):
    id: DatasetColumnID

    created_at: datetime = FieldInfo(alias="createdAt")

    index: int
    """Index of the column within the dataset file."""

    literal_name: str = FieldInfo(alias="literalName")
    """The literal name for the column."""

    updated_at: datetime = FieldInfo(alias="updatedAt")

    dtype: Optional[str] = None


class DatasetOwnerUserID(BaseModel):
    value: str


class Dataset(BaseModel):
    id: DatasetID

    columns: List[DatasetColumn]
    """The columns present in the latest DatasetFile for this dataset"""

    created_at: datetime = FieldInfo(alias="createdAt")

    initialization_status: str = FieldInfo(alias="initializationStatus")

    num_cols: int = FieldInfo(alias="numCols")

    num_rows: int = FieldInfo(alias="numRows")

    owner_user_id: DatasetOwnerUserID = FieldInfo(alias="ownerUserId")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    description: Optional[str] = None
    """Human-readable description of the dataset, if one exists."""

    initialization_error: Optional[str] = FieldInfo(alias="initializationError", default=None)

    labeling_status: Optional[str] = FieldInfo(alias="labelingStatus", default=None)
    """The status of the latest general pseudo-labeling job for the dataset"""

    name: Optional[str] = None
    """Human-readable name for the dataset, if one exists."""


class DatasetListResponse(BaseModel):
    datasets: List[Dataset]

    total_count: int = FieldInfo(alias="totalCount")
    """
    Total count of datasets which can be listed with applicable filters, regardless
    of page size
    """
