# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PseudoLabelJobSubmitResponse", "JobID"]


class JobID(BaseModel):
    value: str


class PseudoLabelJobSubmitResponse(BaseModel):
    job_id: JobID = FieldInfo(alias="jobId")
