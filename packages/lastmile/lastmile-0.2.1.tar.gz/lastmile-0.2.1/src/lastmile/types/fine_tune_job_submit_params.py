# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "FineTuneJobSubmitParams",
    "FineTuneJobConfig",
    "FineTuneJobConfigBaselineModelID",
    "FineTuneJobConfigHyperparameters",
    "FineTuneJobConfigHyperparametersParam",
    "FineTuneJobConfigTestDatasetID",
    "FineTuneJobConfigTrainDatasetID",
    "JobID",
]


class FineTuneJobSubmitParams(TypedDict, total=False):
    fine_tune_job_config: Required[Annotated[FineTuneJobConfig, PropertyInfo(alias="fineTuneJobConfig")]]
    """See repos/lastmile/prisma/schema.prisma:AEFineTuneJobConfig"""

    job_id: Required[Annotated[JobID, PropertyInfo(alias="jobId")]]


class FineTuneJobConfigBaselineModelID(TypedDict, total=False):
    value: Required[str]


class FineTuneJobConfigHyperparametersParam(TypedDict, total=False):
    key: Required[str]

    value: Required[str]


class FineTuneJobConfigHyperparameters(TypedDict, total=False):
    params: Required[Iterable[FineTuneJobConfigHyperparametersParam]]
    """Key-value pairs of hyperparameters."""


class FineTuneJobConfigTestDatasetID(TypedDict, total=False):
    value: Required[str]


class FineTuneJobConfigTrainDatasetID(TypedDict, total=False):
    value: Required[str]


class FineTuneJobConfig(TypedDict, total=False):
    baseline_model_id: Required[Annotated[FineTuneJobConfigBaselineModelID, PropertyInfo(alias="baselineModelId")]]

    hyperparameters: Required[FineTuneJobConfigHyperparameters]
    """Key-value pairs of hyperparameters."""

    test_dataset_id: Required[Annotated[FineTuneJobConfigTestDatasetID, PropertyInfo(alias="testDatasetId")]]

    train_dataset_id: Required[Annotated[FineTuneJobConfigTrainDatasetID, PropertyInfo(alias="trainDatasetId")]]

    description: str
    """Optional description for the job."""

    name: str
    """Optional name for the job."""


class JobID(TypedDict, total=False):
    value: Required[str]
