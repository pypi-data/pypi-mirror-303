# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DatasetGetParams", "ID"]


class DatasetGetParams(TypedDict, total=False):
    id: Required[ID]


class ID(TypedDict, total=False):
    value: Required[str]
