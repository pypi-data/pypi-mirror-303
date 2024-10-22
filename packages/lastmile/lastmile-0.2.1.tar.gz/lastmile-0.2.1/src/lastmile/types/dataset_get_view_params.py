# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DatasetGetViewParams", "DatasetFileID", "DatasetID"]


class DatasetGetViewParams(TypedDict, total=False):
    dataset_file_id: Required[Annotated[DatasetFileID, PropertyInfo(alias="datasetFileId")]]

    dataset_id: Required[Annotated[DatasetID, PropertyInfo(alias="datasetId")]]

    after: int
    """Pagination: The index, by row-order, after which to query results."""

    limit: int
    """Pagination: The maximum number of results to return on this page."""


class DatasetFileID(TypedDict, total=False):
    value: Required[str]


class DatasetID(TypedDict, total=False):
    value: Required[str]
