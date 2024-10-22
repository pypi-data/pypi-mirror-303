# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DatasetFinalizeFileUploadsParams", "DatasetID"]


class DatasetFinalizeFileUploadsParams(TypedDict, total=False):
    dataset_id: Required[Annotated[DatasetID, PropertyInfo(alias="datasetId")]]

    s3_pre_signed_upload_urls: Required[Annotated[List[str], PropertyInfo(alias="s3PreSignedUploadUrls")]]
    """
    Upload URLs that have completed and whose uploaded files should be marked as
    ready for use.
    """

    split_labels: Required[Annotated[List[str], PropertyInfo(alias="splitLabels")]]
    """
    The sequence of labels for the dataset splits, parallel to the sequence of URLs.
    """


class DatasetID(TypedDict, total=False):
    value: Required[str]
