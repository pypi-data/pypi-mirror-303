# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "PseudoLabelJobConfigureParams",
    "JobID",
    "PseudoLabelJobConfig",
    "PseudoLabelJobConfigChatCompletionConfig",
    "PseudoLabelJobConfigChatCompletionConfigMessage",
    "PseudoLabelJobConfigDatasetID",
    "PseudoLabelJobConfigPromptTemplate",
    "PseudoLabelJobConfigActiveLabeledDatasetID",
    "PseudoLabelJobConfigFewShotDatasetID",
]


class PseudoLabelJobConfigureParams(TypedDict, total=False):
    job_id: Required[Annotated[JobID, PropertyInfo(alias="jobId")]]

    pseudo_label_job_config: Required[Annotated[PseudoLabelJobConfig, PropertyInfo(alias="pseudoLabelJobConfig")]]
    """
    Subset of columns to be used in pseudo-labeling. Expected columns: input,
    output, ground_truth For example, a summarization task might not need an input
    column. TODO: Should this be repeated EvaluationMetricParameter enum?
    """


class JobID(TypedDict, total=False):
    value: Required[str]


class PseudoLabelJobConfigChatCompletionConfigMessage(TypedDict, total=False):
    content: Required[str]
    """The content of the message."""

    role: Required[str]
    """Role can be 'system', 'user', or 'assistant'."""


class PseudoLabelJobConfigChatCompletionConfig(TypedDict, total=False):
    max_tokens: Required[Annotated[int, PropertyInfo(alias="maxTokens")]]
    """The maximum number of tokens to generate."""

    messages: Required[Iterable[PseudoLabelJobConfigChatCompletionConfigMessage]]
    """The list of messages in the conversation so far."""

    model: Required[str]
    """The ID of the model to use for the completion."""

    temperature: Required[float]
    """The temperature to use for the completion."""

    top_p: Required[Annotated[float, PropertyInfo(alias="topP")]]
    """The top_p value to use for the completion."""

    vendor: Required[str]


class PseudoLabelJobConfigDatasetID(TypedDict, total=False):
    value: Required[str]


class PseudoLabelJobConfigPromptTemplate(TypedDict, total=False):
    id: Required[str]

    template: Required[str]
    """The template string that defines the prompt"""


class PseudoLabelJobConfigActiveLabeledDatasetID(TypedDict, total=False):
    value: Required[str]


class PseudoLabelJobConfigFewShotDatasetID(TypedDict, total=False):
    value: Required[str]


class PseudoLabelJobConfig(TypedDict, total=False):
    base_evaluation_metric: Required[Annotated[str, PropertyInfo(alias="baseEvaluationMetric")]]
    """
    TODO: @Ankush flesh out default prompt templates or "Base Metric" representation
    of prompt templates.
    """

    chat_completion_config: Required[
        Annotated[PseudoLabelJobConfigChatCompletionConfig, PropertyInfo(alias="chatCompletionConfig")]
    ]
    """The list of messages in the conversation so far."""

    dataset_id: Required[Annotated[PseudoLabelJobConfigDatasetID, PropertyInfo(alias="datasetId")]]

    prompt_template: Required[Annotated[PseudoLabelJobConfigPromptTemplate, PropertyInfo(alias="promptTemplate")]]

    selected_columns: Required[Annotated[List[str], PropertyInfo(alias="selectedColumns")]]
    """
    Subset of columns to be used in pseudo-labeling. Expected columns: input,
    output, ground_truth For example, a summarization task might not need an input
    column. TODO: Should this be repeated EvaluationMetricParameter enum?
    """

    active_labeled_dataset_id: Annotated[
        PseudoLabelJobConfigActiveLabeledDatasetID, PropertyInfo(alias="activeLabeledDatasetId")
    ]

    description: str
    """Optional description for the job."""

    few_shot_dataset_id: Annotated[PseudoLabelJobConfigFewShotDatasetID, PropertyInfo(alias="fewShotDatasetId")]

    name: str
    """Optional name for the job."""
