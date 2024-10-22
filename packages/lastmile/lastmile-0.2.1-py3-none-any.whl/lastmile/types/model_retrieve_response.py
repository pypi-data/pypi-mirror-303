# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ModelRetrieveResponse",
    "Model",
    "ModelID",
    "ModelMetricBaseModel",
    "ModelMetricBaseModelID",
    "ModelMetricBaseModelModelID",
    "ModelModelCard",
    "ModelModelCardHyperparameters",
    "ModelModelCardHyperparametersParam",
    "ModelModelCardModelID",
    "ModelModelCardTrainingProgress",
    "ModelModelCardTrainingProgressJobID",
    "ModelModelCardValue",
    "ModelUserID",
]


class ModelID(BaseModel):
    value: str


class ModelMetricBaseModelID(BaseModel):
    value: str


class ModelMetricBaseModelModelID(BaseModel):
    value: str


class ModelMetricBaseModel(BaseModel):
    id: ModelMetricBaseModelID

    base_evaluation_metric: str = FieldInfo(alias="baseEvaluationMetric")

    base_model_architecture: str = FieldInfo(alias="baseModelArchitecture")

    model_id: ModelMetricBaseModelModelID = FieldInfo(alias="modelId")


class ModelModelCardHyperparametersParam(BaseModel):
    key: str

    value: str


class ModelModelCardHyperparameters(BaseModel):
    params: List[ModelModelCardHyperparametersParam]
    """Key-value pairs of hyperparameters."""


class ModelModelCardModelID(BaseModel):
    value: str


class ModelModelCardTrainingProgressJobID(BaseModel):
    value: str


class ModelModelCardTrainingProgress(BaseModel):
    accuracy: float

    epoch: int

    job_id: ModelModelCardTrainingProgressJobID = FieldInfo(alias="jobId")

    loss: float

    progress: float

    timestamp: datetime


class ModelModelCardValue(BaseModel):
    key: str

    value: str


class ModelModelCard(BaseModel):
    base_evaluation_metric: str = FieldInfo(alias="baseEvaluationMetric")

    base_model_architecture: str = FieldInfo(alias="baseModelArchitecture")

    created_at: datetime = FieldInfo(alias="createdAt")

    deployment_status: str = FieldInfo(alias="deploymentStatus")

    description: str

    hyperparameters: ModelModelCardHyperparameters
    """Key-value pairs of hyperparameters."""

    model_id: ModelModelCardModelID = FieldInfo(alias="modelId")

    model_size: int = FieldInfo(alias="modelSize")

    name: str

    purpose: str

    tags: List[str]

    training_progress: ModelModelCardTrainingProgress = FieldInfo(alias="trainingProgress")
    """Progress metrics from model training."""

    updated_at: datetime = FieldInfo(alias="updatedAt")

    values: List[ModelModelCardValue]


class ModelUserID(BaseModel):
    value: str


class Model(BaseModel):
    id: ModelID

    created_at: datetime = FieldInfo(alias="createdAt")

    is_base_model: bool = FieldInfo(alias="isBaseModel")

    metric_base_model: ModelMetricBaseModel = FieldInfo(alias="metricBaseModel")
    """
    Information about a base model corresponding to a metric See
    repos/lastmile/prisma/schema.prisma:AEBaseModelInfo
    """

    updated_at: datetime = FieldInfo(alias="updatedAt")

    deleted_at: Optional[datetime] = FieldInfo(alias="deletedAt", default=None)

    model_card: Optional[ModelModelCard] = FieldInfo(alias="modelCard", default=None)

    user_id: Optional[ModelUserID] = FieldInfo(alias="userId", default=None)


class ModelRetrieveResponse(BaseModel):
    model: Model
    """Definition for the model See repos/lastmile/prisma/schema.prisma:AEModel"""
