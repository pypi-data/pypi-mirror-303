# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lastmile import Lastmile, AsyncLastmile
from tests.utils import assert_matches_type
from lastmile.types import (
    PseudoLabelJobCreateResponse,
    PseudoLabelJobSubmitResponse,
    PseudoLabelJobConfigureResponse,
    PseudoLabelJobGetStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPseudoLabelJobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Lastmile) -> None:
        pseudo_label_job = client.pseudo_label_jobs.create(
            pseudo_label_job_config={
                "base_evaluation_metric": "baseEvaluationMetric",
                "chat_completion_config": {
                    "max_tokens": -2147483648,
                    "messages": [
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                    ],
                    "model": "model",
                    "temperature": 0,
                    "top_p": 0,
                    "vendor": "vendor",
                },
                "dataset_id": {"value": "value"},
                "prompt_template": {
                    "id": "id",
                    "template": "template",
                },
                "selected_columns": ["string", "string", "string"],
            },
        )
        assert_matches_type(PseudoLabelJobCreateResponse, pseudo_label_job, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Lastmile) -> None:
        pseudo_label_job = client.pseudo_label_jobs.create(
            pseudo_label_job_config={
                "base_evaluation_metric": "baseEvaluationMetric",
                "chat_completion_config": {
                    "max_tokens": -2147483648,
                    "messages": [
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                    ],
                    "model": "model",
                    "temperature": 0,
                    "top_p": 0,
                    "vendor": "vendor",
                },
                "dataset_id": {"value": "value"},
                "prompt_template": {
                    "id": "id",
                    "template": "template",
                },
                "selected_columns": ["string", "string", "string"],
                "active_labeled_dataset_id": {"value": "value"},
                "description": "description",
                "few_shot_dataset_id": {"value": "value"},
                "name": "name",
            },
        )
        assert_matches_type(PseudoLabelJobCreateResponse, pseudo_label_job, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Lastmile) -> None:
        response = client.pseudo_label_jobs.with_raw_response.create(
            pseudo_label_job_config={
                "base_evaluation_metric": "baseEvaluationMetric",
                "chat_completion_config": {
                    "max_tokens": -2147483648,
                    "messages": [
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                    ],
                    "model": "model",
                    "temperature": 0,
                    "top_p": 0,
                    "vendor": "vendor",
                },
                "dataset_id": {"value": "value"},
                "prompt_template": {
                    "id": "id",
                    "template": "template",
                },
                "selected_columns": ["string", "string", "string"],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pseudo_label_job = response.parse()
        assert_matches_type(PseudoLabelJobCreateResponse, pseudo_label_job, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Lastmile) -> None:
        with client.pseudo_label_jobs.with_streaming_response.create(
            pseudo_label_job_config={
                "base_evaluation_metric": "baseEvaluationMetric",
                "chat_completion_config": {
                    "max_tokens": -2147483648,
                    "messages": [
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                    ],
                    "model": "model",
                    "temperature": 0,
                    "top_p": 0,
                    "vendor": "vendor",
                },
                "dataset_id": {"value": "value"},
                "prompt_template": {
                    "id": "id",
                    "template": "template",
                },
                "selected_columns": ["string", "string", "string"],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pseudo_label_job = response.parse()
            assert_matches_type(PseudoLabelJobCreateResponse, pseudo_label_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_configure(self, client: Lastmile) -> None:
        pseudo_label_job = client.pseudo_label_jobs.configure(
            job_id={"value": "value"},
            pseudo_label_job_config={
                "base_evaluation_metric": "baseEvaluationMetric",
                "chat_completion_config": {
                    "max_tokens": -2147483648,
                    "messages": [
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                    ],
                    "model": "model",
                    "temperature": 0,
                    "top_p": 0,
                    "vendor": "vendor",
                },
                "dataset_id": {"value": "value"},
                "prompt_template": {
                    "id": "id",
                    "template": "template",
                },
                "selected_columns": ["string", "string", "string"],
            },
        )
        assert_matches_type(PseudoLabelJobConfigureResponse, pseudo_label_job, path=["response"])

    @parametrize
    def test_method_configure_with_all_params(self, client: Lastmile) -> None:
        pseudo_label_job = client.pseudo_label_jobs.configure(
            job_id={"value": "value"},
            pseudo_label_job_config={
                "base_evaluation_metric": "baseEvaluationMetric",
                "chat_completion_config": {
                    "max_tokens": -2147483648,
                    "messages": [
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                    ],
                    "model": "model",
                    "temperature": 0,
                    "top_p": 0,
                    "vendor": "vendor",
                },
                "dataset_id": {"value": "value"},
                "prompt_template": {
                    "id": "id",
                    "template": "template",
                },
                "selected_columns": ["string", "string", "string"],
                "active_labeled_dataset_id": {"value": "value"},
                "description": "description",
                "few_shot_dataset_id": {"value": "value"},
                "name": "name",
            },
        )
        assert_matches_type(PseudoLabelJobConfigureResponse, pseudo_label_job, path=["response"])

    @parametrize
    def test_raw_response_configure(self, client: Lastmile) -> None:
        response = client.pseudo_label_jobs.with_raw_response.configure(
            job_id={"value": "value"},
            pseudo_label_job_config={
                "base_evaluation_metric": "baseEvaluationMetric",
                "chat_completion_config": {
                    "max_tokens": -2147483648,
                    "messages": [
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                    ],
                    "model": "model",
                    "temperature": 0,
                    "top_p": 0,
                    "vendor": "vendor",
                },
                "dataset_id": {"value": "value"},
                "prompt_template": {
                    "id": "id",
                    "template": "template",
                },
                "selected_columns": ["string", "string", "string"],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pseudo_label_job = response.parse()
        assert_matches_type(PseudoLabelJobConfigureResponse, pseudo_label_job, path=["response"])

    @parametrize
    def test_streaming_response_configure(self, client: Lastmile) -> None:
        with client.pseudo_label_jobs.with_streaming_response.configure(
            job_id={"value": "value"},
            pseudo_label_job_config={
                "base_evaluation_metric": "baseEvaluationMetric",
                "chat_completion_config": {
                    "max_tokens": -2147483648,
                    "messages": [
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                    ],
                    "model": "model",
                    "temperature": 0,
                    "top_p": 0,
                    "vendor": "vendor",
                },
                "dataset_id": {"value": "value"},
                "prompt_template": {
                    "id": "id",
                    "template": "template",
                },
                "selected_columns": ["string", "string", "string"],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pseudo_label_job = response.parse()
            assert_matches_type(PseudoLabelJobConfigureResponse, pseudo_label_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_status(self, client: Lastmile) -> None:
        pseudo_label_job = client.pseudo_label_jobs.get_status(
            job_id={"value": "value"},
        )
        assert_matches_type(PseudoLabelJobGetStatusResponse, pseudo_label_job, path=["response"])

    @parametrize
    def test_raw_response_get_status(self, client: Lastmile) -> None:
        response = client.pseudo_label_jobs.with_raw_response.get_status(
            job_id={"value": "value"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pseudo_label_job = response.parse()
        assert_matches_type(PseudoLabelJobGetStatusResponse, pseudo_label_job, path=["response"])

    @parametrize
    def test_streaming_response_get_status(self, client: Lastmile) -> None:
        with client.pseudo_label_jobs.with_streaming_response.get_status(
            job_id={"value": "value"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pseudo_label_job = response.parse()
            assert_matches_type(PseudoLabelJobGetStatusResponse, pseudo_label_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_submit(self, client: Lastmile) -> None:
        pseudo_label_job = client.pseudo_label_jobs.submit(
            job_id={"value": "value"},
            pseudo_label_job_config={
                "base_evaluation_metric": "baseEvaluationMetric",
                "chat_completion_config": {
                    "max_tokens": -2147483648,
                    "messages": [
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                    ],
                    "model": "model",
                    "temperature": 0,
                    "top_p": 0,
                    "vendor": "vendor",
                },
                "dataset_id": {"value": "value"},
                "prompt_template": {
                    "id": "id",
                    "template": "template",
                },
                "selected_columns": ["string", "string", "string"],
            },
        )
        assert_matches_type(PseudoLabelJobSubmitResponse, pseudo_label_job, path=["response"])

    @parametrize
    def test_method_submit_with_all_params(self, client: Lastmile) -> None:
        pseudo_label_job = client.pseudo_label_jobs.submit(
            job_id={"value": "value"},
            pseudo_label_job_config={
                "base_evaluation_metric": "baseEvaluationMetric",
                "chat_completion_config": {
                    "max_tokens": -2147483648,
                    "messages": [
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                    ],
                    "model": "model",
                    "temperature": 0,
                    "top_p": 0,
                    "vendor": "vendor",
                },
                "dataset_id": {"value": "value"},
                "prompt_template": {
                    "id": "id",
                    "template": "template",
                },
                "selected_columns": ["string", "string", "string"],
                "active_labeled_dataset_id": {"value": "value"},
                "description": "description",
                "few_shot_dataset_id": {"value": "value"},
                "name": "name",
            },
        )
        assert_matches_type(PseudoLabelJobSubmitResponse, pseudo_label_job, path=["response"])

    @parametrize
    def test_raw_response_submit(self, client: Lastmile) -> None:
        response = client.pseudo_label_jobs.with_raw_response.submit(
            job_id={"value": "value"},
            pseudo_label_job_config={
                "base_evaluation_metric": "baseEvaluationMetric",
                "chat_completion_config": {
                    "max_tokens": -2147483648,
                    "messages": [
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                    ],
                    "model": "model",
                    "temperature": 0,
                    "top_p": 0,
                    "vendor": "vendor",
                },
                "dataset_id": {"value": "value"},
                "prompt_template": {
                    "id": "id",
                    "template": "template",
                },
                "selected_columns": ["string", "string", "string"],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pseudo_label_job = response.parse()
        assert_matches_type(PseudoLabelJobSubmitResponse, pseudo_label_job, path=["response"])

    @parametrize
    def test_streaming_response_submit(self, client: Lastmile) -> None:
        with client.pseudo_label_jobs.with_streaming_response.submit(
            job_id={"value": "value"},
            pseudo_label_job_config={
                "base_evaluation_metric": "baseEvaluationMetric",
                "chat_completion_config": {
                    "max_tokens": -2147483648,
                    "messages": [
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                    ],
                    "model": "model",
                    "temperature": 0,
                    "top_p": 0,
                    "vendor": "vendor",
                },
                "dataset_id": {"value": "value"},
                "prompt_template": {
                    "id": "id",
                    "template": "template",
                },
                "selected_columns": ["string", "string", "string"],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pseudo_label_job = response.parse()
            assert_matches_type(PseudoLabelJobSubmitResponse, pseudo_label_job, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPseudoLabelJobs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLastmile) -> None:
        pseudo_label_job = await async_client.pseudo_label_jobs.create(
            pseudo_label_job_config={
                "base_evaluation_metric": "baseEvaluationMetric",
                "chat_completion_config": {
                    "max_tokens": -2147483648,
                    "messages": [
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                    ],
                    "model": "model",
                    "temperature": 0,
                    "top_p": 0,
                    "vendor": "vendor",
                },
                "dataset_id": {"value": "value"},
                "prompt_template": {
                    "id": "id",
                    "template": "template",
                },
                "selected_columns": ["string", "string", "string"],
            },
        )
        assert_matches_type(PseudoLabelJobCreateResponse, pseudo_label_job, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLastmile) -> None:
        pseudo_label_job = await async_client.pseudo_label_jobs.create(
            pseudo_label_job_config={
                "base_evaluation_metric": "baseEvaluationMetric",
                "chat_completion_config": {
                    "max_tokens": -2147483648,
                    "messages": [
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                    ],
                    "model": "model",
                    "temperature": 0,
                    "top_p": 0,
                    "vendor": "vendor",
                },
                "dataset_id": {"value": "value"},
                "prompt_template": {
                    "id": "id",
                    "template": "template",
                },
                "selected_columns": ["string", "string", "string"],
                "active_labeled_dataset_id": {"value": "value"},
                "description": "description",
                "few_shot_dataset_id": {"value": "value"},
                "name": "name",
            },
        )
        assert_matches_type(PseudoLabelJobCreateResponse, pseudo_label_job, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLastmile) -> None:
        response = await async_client.pseudo_label_jobs.with_raw_response.create(
            pseudo_label_job_config={
                "base_evaluation_metric": "baseEvaluationMetric",
                "chat_completion_config": {
                    "max_tokens": -2147483648,
                    "messages": [
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                    ],
                    "model": "model",
                    "temperature": 0,
                    "top_p": 0,
                    "vendor": "vendor",
                },
                "dataset_id": {"value": "value"},
                "prompt_template": {
                    "id": "id",
                    "template": "template",
                },
                "selected_columns": ["string", "string", "string"],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pseudo_label_job = await response.parse()
        assert_matches_type(PseudoLabelJobCreateResponse, pseudo_label_job, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLastmile) -> None:
        async with async_client.pseudo_label_jobs.with_streaming_response.create(
            pseudo_label_job_config={
                "base_evaluation_metric": "baseEvaluationMetric",
                "chat_completion_config": {
                    "max_tokens": -2147483648,
                    "messages": [
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                    ],
                    "model": "model",
                    "temperature": 0,
                    "top_p": 0,
                    "vendor": "vendor",
                },
                "dataset_id": {"value": "value"},
                "prompt_template": {
                    "id": "id",
                    "template": "template",
                },
                "selected_columns": ["string", "string", "string"],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pseudo_label_job = await response.parse()
            assert_matches_type(PseudoLabelJobCreateResponse, pseudo_label_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_configure(self, async_client: AsyncLastmile) -> None:
        pseudo_label_job = await async_client.pseudo_label_jobs.configure(
            job_id={"value": "value"},
            pseudo_label_job_config={
                "base_evaluation_metric": "baseEvaluationMetric",
                "chat_completion_config": {
                    "max_tokens": -2147483648,
                    "messages": [
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                    ],
                    "model": "model",
                    "temperature": 0,
                    "top_p": 0,
                    "vendor": "vendor",
                },
                "dataset_id": {"value": "value"},
                "prompt_template": {
                    "id": "id",
                    "template": "template",
                },
                "selected_columns": ["string", "string", "string"],
            },
        )
        assert_matches_type(PseudoLabelJobConfigureResponse, pseudo_label_job, path=["response"])

    @parametrize
    async def test_method_configure_with_all_params(self, async_client: AsyncLastmile) -> None:
        pseudo_label_job = await async_client.pseudo_label_jobs.configure(
            job_id={"value": "value"},
            pseudo_label_job_config={
                "base_evaluation_metric": "baseEvaluationMetric",
                "chat_completion_config": {
                    "max_tokens": -2147483648,
                    "messages": [
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                    ],
                    "model": "model",
                    "temperature": 0,
                    "top_p": 0,
                    "vendor": "vendor",
                },
                "dataset_id": {"value": "value"},
                "prompt_template": {
                    "id": "id",
                    "template": "template",
                },
                "selected_columns": ["string", "string", "string"],
                "active_labeled_dataset_id": {"value": "value"},
                "description": "description",
                "few_shot_dataset_id": {"value": "value"},
                "name": "name",
            },
        )
        assert_matches_type(PseudoLabelJobConfigureResponse, pseudo_label_job, path=["response"])

    @parametrize
    async def test_raw_response_configure(self, async_client: AsyncLastmile) -> None:
        response = await async_client.pseudo_label_jobs.with_raw_response.configure(
            job_id={"value": "value"},
            pseudo_label_job_config={
                "base_evaluation_metric": "baseEvaluationMetric",
                "chat_completion_config": {
                    "max_tokens": -2147483648,
                    "messages": [
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                    ],
                    "model": "model",
                    "temperature": 0,
                    "top_p": 0,
                    "vendor": "vendor",
                },
                "dataset_id": {"value": "value"},
                "prompt_template": {
                    "id": "id",
                    "template": "template",
                },
                "selected_columns": ["string", "string", "string"],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pseudo_label_job = await response.parse()
        assert_matches_type(PseudoLabelJobConfigureResponse, pseudo_label_job, path=["response"])

    @parametrize
    async def test_streaming_response_configure(self, async_client: AsyncLastmile) -> None:
        async with async_client.pseudo_label_jobs.with_streaming_response.configure(
            job_id={"value": "value"},
            pseudo_label_job_config={
                "base_evaluation_metric": "baseEvaluationMetric",
                "chat_completion_config": {
                    "max_tokens": -2147483648,
                    "messages": [
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                    ],
                    "model": "model",
                    "temperature": 0,
                    "top_p": 0,
                    "vendor": "vendor",
                },
                "dataset_id": {"value": "value"},
                "prompt_template": {
                    "id": "id",
                    "template": "template",
                },
                "selected_columns": ["string", "string", "string"],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pseudo_label_job = await response.parse()
            assert_matches_type(PseudoLabelJobConfigureResponse, pseudo_label_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_status(self, async_client: AsyncLastmile) -> None:
        pseudo_label_job = await async_client.pseudo_label_jobs.get_status(
            job_id={"value": "value"},
        )
        assert_matches_type(PseudoLabelJobGetStatusResponse, pseudo_label_job, path=["response"])

    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncLastmile) -> None:
        response = await async_client.pseudo_label_jobs.with_raw_response.get_status(
            job_id={"value": "value"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pseudo_label_job = await response.parse()
        assert_matches_type(PseudoLabelJobGetStatusResponse, pseudo_label_job, path=["response"])

    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncLastmile) -> None:
        async with async_client.pseudo_label_jobs.with_streaming_response.get_status(
            job_id={"value": "value"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pseudo_label_job = await response.parse()
            assert_matches_type(PseudoLabelJobGetStatusResponse, pseudo_label_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_submit(self, async_client: AsyncLastmile) -> None:
        pseudo_label_job = await async_client.pseudo_label_jobs.submit(
            job_id={"value": "value"},
            pseudo_label_job_config={
                "base_evaluation_metric": "baseEvaluationMetric",
                "chat_completion_config": {
                    "max_tokens": -2147483648,
                    "messages": [
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                    ],
                    "model": "model",
                    "temperature": 0,
                    "top_p": 0,
                    "vendor": "vendor",
                },
                "dataset_id": {"value": "value"},
                "prompt_template": {
                    "id": "id",
                    "template": "template",
                },
                "selected_columns": ["string", "string", "string"],
            },
        )
        assert_matches_type(PseudoLabelJobSubmitResponse, pseudo_label_job, path=["response"])

    @parametrize
    async def test_method_submit_with_all_params(self, async_client: AsyncLastmile) -> None:
        pseudo_label_job = await async_client.pseudo_label_jobs.submit(
            job_id={"value": "value"},
            pseudo_label_job_config={
                "base_evaluation_metric": "baseEvaluationMetric",
                "chat_completion_config": {
                    "max_tokens": -2147483648,
                    "messages": [
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                    ],
                    "model": "model",
                    "temperature": 0,
                    "top_p": 0,
                    "vendor": "vendor",
                },
                "dataset_id": {"value": "value"},
                "prompt_template": {
                    "id": "id",
                    "template": "template",
                },
                "selected_columns": ["string", "string", "string"],
                "active_labeled_dataset_id": {"value": "value"},
                "description": "description",
                "few_shot_dataset_id": {"value": "value"},
                "name": "name",
            },
        )
        assert_matches_type(PseudoLabelJobSubmitResponse, pseudo_label_job, path=["response"])

    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncLastmile) -> None:
        response = await async_client.pseudo_label_jobs.with_raw_response.submit(
            job_id={"value": "value"},
            pseudo_label_job_config={
                "base_evaluation_metric": "baseEvaluationMetric",
                "chat_completion_config": {
                    "max_tokens": -2147483648,
                    "messages": [
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                    ],
                    "model": "model",
                    "temperature": 0,
                    "top_p": 0,
                    "vendor": "vendor",
                },
                "dataset_id": {"value": "value"},
                "prompt_template": {
                    "id": "id",
                    "template": "template",
                },
                "selected_columns": ["string", "string", "string"],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pseudo_label_job = await response.parse()
        assert_matches_type(PseudoLabelJobSubmitResponse, pseudo_label_job, path=["response"])

    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncLastmile) -> None:
        async with async_client.pseudo_label_jobs.with_streaming_response.submit(
            job_id={"value": "value"},
            pseudo_label_job_config={
                "base_evaluation_metric": "baseEvaluationMetric",
                "chat_completion_config": {
                    "max_tokens": -2147483648,
                    "messages": [
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                        {
                            "content": "content",
                            "role": "role",
                        },
                    ],
                    "model": "model",
                    "temperature": 0,
                    "top_p": 0,
                    "vendor": "vendor",
                },
                "dataset_id": {"value": "value"},
                "prompt_template": {
                    "id": "id",
                    "template": "template",
                },
                "selected_columns": ["string", "string", "string"],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pseudo_label_job = await response.parse()
            assert_matches_type(PseudoLabelJobSubmitResponse, pseudo_label_job, path=["response"])

        assert cast(Any, response.is_closed) is True
