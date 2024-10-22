# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ModelPseudoLabelWorkerExecutePseudoLabelJobParams", "PseudoLabelJobID"]


class ModelPseudoLabelWorkerExecutePseudoLabelJobParams(TypedDict, total=False):
    pseudo_label_job_id: Required[Annotated[PseudoLabelJobID, PropertyInfo(alias="pseudoLabelJobId")]]


class PseudoLabelJobID(TypedDict, total=False):
    value: Required[str]
