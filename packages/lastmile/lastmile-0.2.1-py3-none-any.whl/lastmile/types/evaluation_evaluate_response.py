# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EvaluationEvaluateResponse", "Model", "ModelModelID", "Score"]


class ModelModelID(BaseModel):
    value: str


class Model(BaseModel):
    metric: str

    model_id: ModelModelID = FieldInfo(alias="modelId")


class Score(BaseModel):
    values: List[float]


class EvaluationEvaluateResponse(BaseModel):
    models: List[Model]

    scores: List[Score]
