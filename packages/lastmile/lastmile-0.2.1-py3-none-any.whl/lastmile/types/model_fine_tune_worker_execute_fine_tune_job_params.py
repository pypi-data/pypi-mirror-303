# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ModelFineTuneWorkerExecuteFineTuneJobParams", "FineTuneJobID"]


class ModelFineTuneWorkerExecuteFineTuneJobParams(TypedDict, total=False):
    fine_tune_job_id: Required[Annotated[FineTuneJobID, PropertyInfo(alias="fineTuneJobId")]]


class FineTuneJobID(TypedDict, total=False):
    value: Required[str]
