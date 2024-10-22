# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DatasetUploadSplitFilesResponse"]


class DatasetUploadSplitFilesResponse(BaseModel):
    s3_pre_signed_upload_urls: List[str] = FieldInfo(alias="s3PreSignedUploadUrls")
    """Upload URLs, one for each split label in the input, parallel to the inputs."""
