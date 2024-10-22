# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PseudoLabelJobConfigureResponse", "JobID"]


class JobID(BaseModel):
    value: str


class PseudoLabelJobConfigureResponse(BaseModel):
    job_id: JobID = FieldInfo(alias="jobId")
