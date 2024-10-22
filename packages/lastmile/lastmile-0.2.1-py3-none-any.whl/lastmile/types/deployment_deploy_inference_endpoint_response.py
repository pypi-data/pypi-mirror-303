# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "DeploymentDeployInferenceEndpointResponse",
    "ModelDeployment",
    "ModelDeploymentID",
    "ModelDeploymentModelID",
]


class ModelDeploymentID(BaseModel):
    value: str


class ModelDeploymentModelID(BaseModel):
    value: str


class ModelDeployment(BaseModel):
    id: ModelDeploymentID

    created_at: datetime = FieldInfo(alias="createdAt")

    model_id: ModelDeploymentModelID = FieldInfo(alias="modelId")

    status: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    deployed_api_url: Optional[str] = FieldInfo(alias="deployedApiUrl", default=None)

    job_id: Optional[str] = FieldInfo(alias="jobId", default=None)
    """The ID of the job coordinating the deployment, if one exists."""


class DeploymentDeployInferenceEndpointResponse(BaseModel):
    model_deployment: ModelDeployment = FieldInfo(alias="modelDeployment")
    """See repos/lastmile/prisma/schema.prisma:AEModelDeployment"""
