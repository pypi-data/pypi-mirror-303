# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EvaluationListMetricsResponse", "Model", "ModelModelID"]


class ModelModelID(BaseModel):
    value: str


class Model(BaseModel):
    metric: str

    model_id: ModelModelID = FieldInfo(alias="modelId")


class EvaluationListMetricsResponse(BaseModel):
    models: List[Model]
    """These models will have model_specifier.metric set"""
