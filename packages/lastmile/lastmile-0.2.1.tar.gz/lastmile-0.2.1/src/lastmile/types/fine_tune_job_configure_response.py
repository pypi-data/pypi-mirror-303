# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "FineTuneJobConfigureResponse",
    "FineTuneJobConfig",
    "FineTuneJobConfigBaselineModelID",
    "FineTuneJobConfigHyperparameters",
    "FineTuneJobConfigHyperparametersParam",
    "FineTuneJobConfigTestDatasetID",
    "FineTuneJobConfigTrainDatasetID",
]


class FineTuneJobConfigBaselineModelID(BaseModel):
    value: str


class FineTuneJobConfigHyperparametersParam(BaseModel):
    key: str

    value: str


class FineTuneJobConfigHyperparameters(BaseModel):
    params: List[FineTuneJobConfigHyperparametersParam]
    """Key-value pairs of hyperparameters."""


class FineTuneJobConfigTestDatasetID(BaseModel):
    value: str


class FineTuneJobConfigTrainDatasetID(BaseModel):
    value: str


class FineTuneJobConfig(BaseModel):
    baseline_model_id: FineTuneJobConfigBaselineModelID = FieldInfo(alias="baselineModelId")

    hyperparameters: FineTuneJobConfigHyperparameters
    """Key-value pairs of hyperparameters."""

    test_dataset_id: FineTuneJobConfigTestDatasetID = FieldInfo(alias="testDatasetId")

    train_dataset_id: FineTuneJobConfigTrainDatasetID = FieldInfo(alias="trainDatasetId")

    description: Optional[str] = None
    """Optional description for the job."""

    name: Optional[str] = None
    """Optional name for the job."""


class FineTuneJobConfigureResponse(BaseModel):
    fine_tune_job_config: FineTuneJobConfig = FieldInfo(alias="fineTuneJobConfig")
    """See repos/lastmile/prisma/schema.prisma:AEFineTuneJobConfig"""
