# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DatasetUploadSplitFilesParams", "DatasetID"]


class DatasetUploadSplitFilesParams(TypedDict, total=False):
    dataset_id: Required[Annotated[DatasetID, PropertyInfo(alias="datasetId")]]

    split_labels: Required[Annotated[List[str], PropertyInfo(alias="splitLabels")]]
    """
    A sequence of labels for the dataset splits, for which we will generate a
    parallel list of upload destination URLs.
    """


class DatasetID(TypedDict, total=False):
    value: Required[str]
