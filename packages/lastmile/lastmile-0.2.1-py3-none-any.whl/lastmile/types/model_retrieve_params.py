# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ModelRetrieveParams", "ModelID"]


class ModelRetrieveParams(TypedDict, total=False):
    model_id: Required[Annotated[ModelID, PropertyInfo(alias="modelId")]]


class ModelID(TypedDict, total=False):
    value: Required[str]
