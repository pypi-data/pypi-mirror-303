# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EvaluationEvaluateDatasetParams", "DatasetID", "Model", "ModelModelID"]


class EvaluationEvaluateDatasetParams(TypedDict, total=False):
    dataset_id: Required[Annotated[DatasetID, PropertyInfo(alias="datasetId")]]

    models: Required[Iterable[Model]]


class DatasetID(TypedDict, total=False):
    value: Required[str]


class ModelModelID(TypedDict, total=False):
    value: Required[str]


class Model(TypedDict, total=False):
    metric: Required[str]

    model_id: Required[Annotated[ModelModelID, PropertyInfo(alias="modelId")]]
