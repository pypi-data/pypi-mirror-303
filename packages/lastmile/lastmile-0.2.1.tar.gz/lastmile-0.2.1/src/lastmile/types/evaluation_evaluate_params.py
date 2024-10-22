# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EvaluationEvaluateParams", "Model", "ModelModelID"]


class EvaluationEvaluateParams(TypedDict, total=False):
    ground_truth: Required[Annotated[List[str], PropertyInfo(alias="groundTruth")]]

    input: Required[List[str]]

    models: Required[Iterable[Model]]

    output: Required[List[str]]


class ModelModelID(TypedDict, total=False):
    value: Required[str]


class Model(TypedDict, total=False):
    metric: Required[str]

    model_id: Required[Annotated[ModelModelID, PropertyInfo(alias="modelId")]]
