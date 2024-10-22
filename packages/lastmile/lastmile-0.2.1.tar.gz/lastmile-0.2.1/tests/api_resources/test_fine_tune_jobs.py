# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lastmile import Lastmile, AsyncLastmile
from tests.utils import assert_matches_type
from lastmile.types import (
    FineTuneJobCreateResponse,
    FineTuneJobSubmitResponse,
    FineTuneJobConfigureResponse,
    FineTuneJobGetStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFineTuneJobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Lastmile) -> None:
        fine_tune_job = client.fine_tune_jobs.create(
            fine_tune_job_config={
                "baseline_model_id": {"value": "value"},
                "hyperparameters": {
                    "params": [
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                    ]
                },
                "test_dataset_id": {"value": "value"},
                "train_dataset_id": {"value": "value"},
            },
        )
        assert_matches_type(FineTuneJobCreateResponse, fine_tune_job, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Lastmile) -> None:
        fine_tune_job = client.fine_tune_jobs.create(
            fine_tune_job_config={
                "baseline_model_id": {"value": "value"},
                "hyperparameters": {
                    "params": [
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                    ]
                },
                "test_dataset_id": {"value": "value"},
                "train_dataset_id": {"value": "value"},
                "description": "description",
                "name": "name",
            },
        )
        assert_matches_type(FineTuneJobCreateResponse, fine_tune_job, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Lastmile) -> None:
        response = client.fine_tune_jobs.with_raw_response.create(
            fine_tune_job_config={
                "baseline_model_id": {"value": "value"},
                "hyperparameters": {
                    "params": [
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                    ]
                },
                "test_dataset_id": {"value": "value"},
                "train_dataset_id": {"value": "value"},
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fine_tune_job = response.parse()
        assert_matches_type(FineTuneJobCreateResponse, fine_tune_job, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Lastmile) -> None:
        with client.fine_tune_jobs.with_streaming_response.create(
            fine_tune_job_config={
                "baseline_model_id": {"value": "value"},
                "hyperparameters": {
                    "params": [
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                    ]
                },
                "test_dataset_id": {"value": "value"},
                "train_dataset_id": {"value": "value"},
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fine_tune_job = response.parse()
            assert_matches_type(FineTuneJobCreateResponse, fine_tune_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_configure(self, client: Lastmile) -> None:
        fine_tune_job = client.fine_tune_jobs.configure(
            fine_tune_job_config={
                "baseline_model_id": {"value": "value"},
                "hyperparameters": {
                    "params": [
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                    ]
                },
                "test_dataset_id": {"value": "value"},
                "train_dataset_id": {"value": "value"},
            },
            job_id={"value": "value"},
        )
        assert_matches_type(FineTuneJobConfigureResponse, fine_tune_job, path=["response"])

    @parametrize
    def test_method_configure_with_all_params(self, client: Lastmile) -> None:
        fine_tune_job = client.fine_tune_jobs.configure(
            fine_tune_job_config={
                "baseline_model_id": {"value": "value"},
                "hyperparameters": {
                    "params": [
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                    ]
                },
                "test_dataset_id": {"value": "value"},
                "train_dataset_id": {"value": "value"},
                "description": "description",
                "name": "name",
            },
            job_id={"value": "value"},
        )
        assert_matches_type(FineTuneJobConfigureResponse, fine_tune_job, path=["response"])

    @parametrize
    def test_raw_response_configure(self, client: Lastmile) -> None:
        response = client.fine_tune_jobs.with_raw_response.configure(
            fine_tune_job_config={
                "baseline_model_id": {"value": "value"},
                "hyperparameters": {
                    "params": [
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                    ]
                },
                "test_dataset_id": {"value": "value"},
                "train_dataset_id": {"value": "value"},
            },
            job_id={"value": "value"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fine_tune_job = response.parse()
        assert_matches_type(FineTuneJobConfigureResponse, fine_tune_job, path=["response"])

    @parametrize
    def test_streaming_response_configure(self, client: Lastmile) -> None:
        with client.fine_tune_jobs.with_streaming_response.configure(
            fine_tune_job_config={
                "baseline_model_id": {"value": "value"},
                "hyperparameters": {
                    "params": [
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                    ]
                },
                "test_dataset_id": {"value": "value"},
                "train_dataset_id": {"value": "value"},
            },
            job_id={"value": "value"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fine_tune_job = response.parse()
            assert_matches_type(FineTuneJobConfigureResponse, fine_tune_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_status(self, client: Lastmile) -> None:
        fine_tune_job = client.fine_tune_jobs.get_status(
            job_id={"value": "value"},
        )
        assert_matches_type(FineTuneJobGetStatusResponse, fine_tune_job, path=["response"])

    @parametrize
    def test_raw_response_get_status(self, client: Lastmile) -> None:
        response = client.fine_tune_jobs.with_raw_response.get_status(
            job_id={"value": "value"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fine_tune_job = response.parse()
        assert_matches_type(FineTuneJobGetStatusResponse, fine_tune_job, path=["response"])

    @parametrize
    def test_streaming_response_get_status(self, client: Lastmile) -> None:
        with client.fine_tune_jobs.with_streaming_response.get_status(
            job_id={"value": "value"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fine_tune_job = response.parse()
            assert_matches_type(FineTuneJobGetStatusResponse, fine_tune_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_submit(self, client: Lastmile) -> None:
        fine_tune_job = client.fine_tune_jobs.submit(
            fine_tune_job_config={
                "baseline_model_id": {"value": "value"},
                "hyperparameters": {
                    "params": [
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                    ]
                },
                "test_dataset_id": {"value": "value"},
                "train_dataset_id": {"value": "value"},
            },
            job_id={"value": "value"},
        )
        assert_matches_type(FineTuneJobSubmitResponse, fine_tune_job, path=["response"])

    @parametrize
    def test_method_submit_with_all_params(self, client: Lastmile) -> None:
        fine_tune_job = client.fine_tune_jobs.submit(
            fine_tune_job_config={
                "baseline_model_id": {"value": "value"},
                "hyperparameters": {
                    "params": [
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                    ]
                },
                "test_dataset_id": {"value": "value"},
                "train_dataset_id": {"value": "value"},
                "description": "description",
                "name": "name",
            },
            job_id={"value": "value"},
        )
        assert_matches_type(FineTuneJobSubmitResponse, fine_tune_job, path=["response"])

    @parametrize
    def test_raw_response_submit(self, client: Lastmile) -> None:
        response = client.fine_tune_jobs.with_raw_response.submit(
            fine_tune_job_config={
                "baseline_model_id": {"value": "value"},
                "hyperparameters": {
                    "params": [
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                    ]
                },
                "test_dataset_id": {"value": "value"},
                "train_dataset_id": {"value": "value"},
            },
            job_id={"value": "value"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fine_tune_job = response.parse()
        assert_matches_type(FineTuneJobSubmitResponse, fine_tune_job, path=["response"])

    @parametrize
    def test_streaming_response_submit(self, client: Lastmile) -> None:
        with client.fine_tune_jobs.with_streaming_response.submit(
            fine_tune_job_config={
                "baseline_model_id": {"value": "value"},
                "hyperparameters": {
                    "params": [
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                    ]
                },
                "test_dataset_id": {"value": "value"},
                "train_dataset_id": {"value": "value"},
            },
            job_id={"value": "value"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fine_tune_job = response.parse()
            assert_matches_type(FineTuneJobSubmitResponse, fine_tune_job, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFineTuneJobs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLastmile) -> None:
        fine_tune_job = await async_client.fine_tune_jobs.create(
            fine_tune_job_config={
                "baseline_model_id": {"value": "value"},
                "hyperparameters": {
                    "params": [
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                    ]
                },
                "test_dataset_id": {"value": "value"},
                "train_dataset_id": {"value": "value"},
            },
        )
        assert_matches_type(FineTuneJobCreateResponse, fine_tune_job, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLastmile) -> None:
        fine_tune_job = await async_client.fine_tune_jobs.create(
            fine_tune_job_config={
                "baseline_model_id": {"value": "value"},
                "hyperparameters": {
                    "params": [
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                    ]
                },
                "test_dataset_id": {"value": "value"},
                "train_dataset_id": {"value": "value"},
                "description": "description",
                "name": "name",
            },
        )
        assert_matches_type(FineTuneJobCreateResponse, fine_tune_job, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLastmile) -> None:
        response = await async_client.fine_tune_jobs.with_raw_response.create(
            fine_tune_job_config={
                "baseline_model_id": {"value": "value"},
                "hyperparameters": {
                    "params": [
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                    ]
                },
                "test_dataset_id": {"value": "value"},
                "train_dataset_id": {"value": "value"},
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fine_tune_job = await response.parse()
        assert_matches_type(FineTuneJobCreateResponse, fine_tune_job, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLastmile) -> None:
        async with async_client.fine_tune_jobs.with_streaming_response.create(
            fine_tune_job_config={
                "baseline_model_id": {"value": "value"},
                "hyperparameters": {
                    "params": [
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                    ]
                },
                "test_dataset_id": {"value": "value"},
                "train_dataset_id": {"value": "value"},
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fine_tune_job = await response.parse()
            assert_matches_type(FineTuneJobCreateResponse, fine_tune_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_configure(self, async_client: AsyncLastmile) -> None:
        fine_tune_job = await async_client.fine_tune_jobs.configure(
            fine_tune_job_config={
                "baseline_model_id": {"value": "value"},
                "hyperparameters": {
                    "params": [
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                    ]
                },
                "test_dataset_id": {"value": "value"},
                "train_dataset_id": {"value": "value"},
            },
            job_id={"value": "value"},
        )
        assert_matches_type(FineTuneJobConfigureResponse, fine_tune_job, path=["response"])

    @parametrize
    async def test_method_configure_with_all_params(self, async_client: AsyncLastmile) -> None:
        fine_tune_job = await async_client.fine_tune_jobs.configure(
            fine_tune_job_config={
                "baseline_model_id": {"value": "value"},
                "hyperparameters": {
                    "params": [
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                    ]
                },
                "test_dataset_id": {"value": "value"},
                "train_dataset_id": {"value": "value"},
                "description": "description",
                "name": "name",
            },
            job_id={"value": "value"},
        )
        assert_matches_type(FineTuneJobConfigureResponse, fine_tune_job, path=["response"])

    @parametrize
    async def test_raw_response_configure(self, async_client: AsyncLastmile) -> None:
        response = await async_client.fine_tune_jobs.with_raw_response.configure(
            fine_tune_job_config={
                "baseline_model_id": {"value": "value"},
                "hyperparameters": {
                    "params": [
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                    ]
                },
                "test_dataset_id": {"value": "value"},
                "train_dataset_id": {"value": "value"},
            },
            job_id={"value": "value"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fine_tune_job = await response.parse()
        assert_matches_type(FineTuneJobConfigureResponse, fine_tune_job, path=["response"])

    @parametrize
    async def test_streaming_response_configure(self, async_client: AsyncLastmile) -> None:
        async with async_client.fine_tune_jobs.with_streaming_response.configure(
            fine_tune_job_config={
                "baseline_model_id": {"value": "value"},
                "hyperparameters": {
                    "params": [
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                    ]
                },
                "test_dataset_id": {"value": "value"},
                "train_dataset_id": {"value": "value"},
            },
            job_id={"value": "value"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fine_tune_job = await response.parse()
            assert_matches_type(FineTuneJobConfigureResponse, fine_tune_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_status(self, async_client: AsyncLastmile) -> None:
        fine_tune_job = await async_client.fine_tune_jobs.get_status(
            job_id={"value": "value"},
        )
        assert_matches_type(FineTuneJobGetStatusResponse, fine_tune_job, path=["response"])

    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncLastmile) -> None:
        response = await async_client.fine_tune_jobs.with_raw_response.get_status(
            job_id={"value": "value"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fine_tune_job = await response.parse()
        assert_matches_type(FineTuneJobGetStatusResponse, fine_tune_job, path=["response"])

    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncLastmile) -> None:
        async with async_client.fine_tune_jobs.with_streaming_response.get_status(
            job_id={"value": "value"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fine_tune_job = await response.parse()
            assert_matches_type(FineTuneJobGetStatusResponse, fine_tune_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_submit(self, async_client: AsyncLastmile) -> None:
        fine_tune_job = await async_client.fine_tune_jobs.submit(
            fine_tune_job_config={
                "baseline_model_id": {"value": "value"},
                "hyperparameters": {
                    "params": [
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                    ]
                },
                "test_dataset_id": {"value": "value"},
                "train_dataset_id": {"value": "value"},
            },
            job_id={"value": "value"},
        )
        assert_matches_type(FineTuneJobSubmitResponse, fine_tune_job, path=["response"])

    @parametrize
    async def test_method_submit_with_all_params(self, async_client: AsyncLastmile) -> None:
        fine_tune_job = await async_client.fine_tune_jobs.submit(
            fine_tune_job_config={
                "baseline_model_id": {"value": "value"},
                "hyperparameters": {
                    "params": [
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                    ]
                },
                "test_dataset_id": {"value": "value"},
                "train_dataset_id": {"value": "value"},
                "description": "description",
                "name": "name",
            },
            job_id={"value": "value"},
        )
        assert_matches_type(FineTuneJobSubmitResponse, fine_tune_job, path=["response"])

    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncLastmile) -> None:
        response = await async_client.fine_tune_jobs.with_raw_response.submit(
            fine_tune_job_config={
                "baseline_model_id": {"value": "value"},
                "hyperparameters": {
                    "params": [
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                    ]
                },
                "test_dataset_id": {"value": "value"},
                "train_dataset_id": {"value": "value"},
            },
            job_id={"value": "value"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fine_tune_job = await response.parse()
        assert_matches_type(FineTuneJobSubmitResponse, fine_tune_job, path=["response"])

    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncLastmile) -> None:
        async with async_client.fine_tune_jobs.with_streaming_response.submit(
            fine_tune_job_config={
                "baseline_model_id": {"value": "value"},
                "hyperparameters": {
                    "params": [
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                        {
                            "key": "key",
                            "value": "value",
                        },
                    ]
                },
                "test_dataset_id": {"value": "value"},
                "train_dataset_id": {"value": "value"},
            },
            job_id={"value": "value"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fine_tune_job = await response.parse()
            assert_matches_type(FineTuneJobSubmitResponse, fine_tune_job, path=["response"])

        assert cast(Any, response.is_closed) is True
