# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "FineTuneJobGetStatusResponse",
    "FineTuneJobResult",
    "FineTuneJobResultProgress",
    "FineTuneJobResultProgressJobID",
    "FineTuneJobResultTrainedModelFile",
    "FineTuneJobResultTrainedModelFileID",
    "FineTuneJobResultTrainedModelFileModelID",
]


class FineTuneJobResultProgressJobID(BaseModel):
    value: str


class FineTuneJobResultProgress(BaseModel):
    accuracy: float

    epoch: int

    job_id: FineTuneJobResultProgressJobID = FieldInfo(alias="jobId")

    loss: float

    progress: float

    timestamp: datetime


class FineTuneJobResultTrainedModelFileID(BaseModel):
    value: str


class FineTuneJobResultTrainedModelFileModelID(BaseModel):
    value: str


class FineTuneJobResultTrainedModelFile(BaseModel):
    id: FineTuneJobResultTrainedModelFileID

    content_md5_hash: str = FieldInfo(alias="contentMd5Hash")

    created_at: datetime = FieldInfo(alias="createdAt")

    file_size_bytes: int = FieldInfo(alias="fileSizeBytes")

    model_id: FineTuneJobResultTrainedModelFileModelID = FieldInfo(alias="modelId")

    updated_at: datetime = FieldInfo(alias="updatedAt")


class FineTuneJobResult(BaseModel):
    progress: List[FineTuneJobResultProgress]
    """Sequential snapshots of training metrics."""

    trained_model_file: Optional[FineTuneJobResultTrainedModelFile] = FieldInfo(alias="trainedModelFile", default=None)
    """
    Actual file asset corresponding to a model See
    repos/lastmile/prisma/schema.prisma:AEModelFile
    """


class FineTuneJobGetStatusResponse(BaseModel):
    fine_tune_job_result: FineTuneJobResult = FieldInfo(alias="fineTuneJobResult")
    """Sequential snapshots of training metrics."""

    status: str
