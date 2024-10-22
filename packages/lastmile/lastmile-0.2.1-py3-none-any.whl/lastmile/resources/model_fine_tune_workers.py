# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import model_fine_tune_worker_execute_fine_tune_job_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.model_fine_tune_worker_execute_fine_tune_job_response import ModelFineTuneWorkerExecuteFineTuneJobResponse

__all__ = ["ModelFineTuneWorkersResource", "AsyncModelFineTuneWorkersResource"]


class ModelFineTuneWorkersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ModelFineTuneWorkersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lastmile-ai/lastmile-python#accessing-raw-response-data-eg-headers
        """
        return ModelFineTuneWorkersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModelFineTuneWorkersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lastmile-ai/lastmile-python#with_streaming_response
        """
        return ModelFineTuneWorkersResourceWithStreamingResponse(self)

    def execute_fine_tune_job(
        self,
        *,
        fine_tune_job_id: model_fine_tune_worker_execute_fine_tune_job_params.FineTuneJobID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelFineTuneWorkerExecuteFineTuneJobResponse:
        """
        Description of execute_fine_tune_job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/2/auto_eval/model_fine_tune_worker/execute_fine_tune_job",
            body=maybe_transform(
                {"fine_tune_job_id": fine_tune_job_id},
                model_fine_tune_worker_execute_fine_tune_job_params.ModelFineTuneWorkerExecuteFineTuneJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelFineTuneWorkerExecuteFineTuneJobResponse,
        )


class AsyncModelFineTuneWorkersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncModelFineTuneWorkersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lastmile-ai/lastmile-python#accessing-raw-response-data-eg-headers
        """
        return AsyncModelFineTuneWorkersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModelFineTuneWorkersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lastmile-ai/lastmile-python#with_streaming_response
        """
        return AsyncModelFineTuneWorkersResourceWithStreamingResponse(self)

    async def execute_fine_tune_job(
        self,
        *,
        fine_tune_job_id: model_fine_tune_worker_execute_fine_tune_job_params.FineTuneJobID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelFineTuneWorkerExecuteFineTuneJobResponse:
        """
        Description of execute_fine_tune_job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/2/auto_eval/model_fine_tune_worker/execute_fine_tune_job",
            body=await async_maybe_transform(
                {"fine_tune_job_id": fine_tune_job_id},
                model_fine_tune_worker_execute_fine_tune_job_params.ModelFineTuneWorkerExecuteFineTuneJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelFineTuneWorkerExecuteFineTuneJobResponse,
        )


class ModelFineTuneWorkersResourceWithRawResponse:
    def __init__(self, model_fine_tune_workers: ModelFineTuneWorkersResource) -> None:
        self._model_fine_tune_workers = model_fine_tune_workers

        self.execute_fine_tune_job = to_raw_response_wrapper(
            model_fine_tune_workers.execute_fine_tune_job,
        )


class AsyncModelFineTuneWorkersResourceWithRawResponse:
    def __init__(self, model_fine_tune_workers: AsyncModelFineTuneWorkersResource) -> None:
        self._model_fine_tune_workers = model_fine_tune_workers

        self.execute_fine_tune_job = async_to_raw_response_wrapper(
            model_fine_tune_workers.execute_fine_tune_job,
        )


class ModelFineTuneWorkersResourceWithStreamingResponse:
    def __init__(self, model_fine_tune_workers: ModelFineTuneWorkersResource) -> None:
        self._model_fine_tune_workers = model_fine_tune_workers

        self.execute_fine_tune_job = to_streamed_response_wrapper(
            model_fine_tune_workers.execute_fine_tune_job,
        )


class AsyncModelFineTuneWorkersResourceWithStreamingResponse:
    def __init__(self, model_fine_tune_workers: AsyncModelFineTuneWorkersResource) -> None:
        self._model_fine_tune_workers = model_fine_tune_workers

        self.execute_fine_tune_job = async_to_streamed_response_wrapper(
            model_fine_tune_workers.execute_fine_tune_job,
        )
