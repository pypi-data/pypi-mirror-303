# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lastmile import Lastmile, AsyncLastmile
from tests.utils import assert_matches_type
from lastmile.types import (
    ModelFineTuneWorkerExecuteFineTuneJobResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestModelFineTuneWorkers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_execute_fine_tune_job(self, client: Lastmile) -> None:
        model_fine_tune_worker = client.model_fine_tune_workers.execute_fine_tune_job(
            fine_tune_job_id={"value": "value"},
        )
        assert_matches_type(ModelFineTuneWorkerExecuteFineTuneJobResponse, model_fine_tune_worker, path=["response"])

    @parametrize
    def test_raw_response_execute_fine_tune_job(self, client: Lastmile) -> None:
        response = client.model_fine_tune_workers.with_raw_response.execute_fine_tune_job(
            fine_tune_job_id={"value": "value"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model_fine_tune_worker = response.parse()
        assert_matches_type(ModelFineTuneWorkerExecuteFineTuneJobResponse, model_fine_tune_worker, path=["response"])

    @parametrize
    def test_streaming_response_execute_fine_tune_job(self, client: Lastmile) -> None:
        with client.model_fine_tune_workers.with_streaming_response.execute_fine_tune_job(
            fine_tune_job_id={"value": "value"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model_fine_tune_worker = response.parse()
            assert_matches_type(
                ModelFineTuneWorkerExecuteFineTuneJobResponse, model_fine_tune_worker, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncModelFineTuneWorkers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_execute_fine_tune_job(self, async_client: AsyncLastmile) -> None:
        model_fine_tune_worker = await async_client.model_fine_tune_workers.execute_fine_tune_job(
            fine_tune_job_id={"value": "value"},
        )
        assert_matches_type(ModelFineTuneWorkerExecuteFineTuneJobResponse, model_fine_tune_worker, path=["response"])

    @parametrize
    async def test_raw_response_execute_fine_tune_job(self, async_client: AsyncLastmile) -> None:
        response = await async_client.model_fine_tune_workers.with_raw_response.execute_fine_tune_job(
            fine_tune_job_id={"value": "value"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model_fine_tune_worker = await response.parse()
        assert_matches_type(ModelFineTuneWorkerExecuteFineTuneJobResponse, model_fine_tune_worker, path=["response"])

    @parametrize
    async def test_streaming_response_execute_fine_tune_job(self, async_client: AsyncLastmile) -> None:
        async with async_client.model_fine_tune_workers.with_streaming_response.execute_fine_tune_job(
            fine_tune_job_id={"value": "value"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model_fine_tune_worker = await response.parse()
            assert_matches_type(
                ModelFineTuneWorkerExecuteFineTuneJobResponse, model_fine_tune_worker, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
