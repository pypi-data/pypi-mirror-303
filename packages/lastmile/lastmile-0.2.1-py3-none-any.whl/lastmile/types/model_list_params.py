# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ModelListParams", "Filters"]


class ModelListParams(TypedDict, total=False):
    filters: Filters


class Filters(TypedDict, total=False):
    is_base: Annotated[bool, PropertyInfo(alias="isBase")]
    """
    restrict to base (true) or fine-tune (false) models exclude to include both
    types of model
    """

    query: str
    """search query substring match for name and description"""
