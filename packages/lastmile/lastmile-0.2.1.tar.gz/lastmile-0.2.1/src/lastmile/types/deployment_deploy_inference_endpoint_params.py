# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DeploymentDeployInferenceEndpointParams", "ModelFileID"]


class DeploymentDeployInferenceEndpointParams(TypedDict, total=False):
    model_file_id: Required[Annotated[ModelFileID, PropertyInfo(alias="modelFileId")]]


class ModelFileID(TypedDict, total=False):
    value: Required[str]
