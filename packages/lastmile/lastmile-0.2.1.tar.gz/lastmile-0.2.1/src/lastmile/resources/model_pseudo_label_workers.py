# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import model_pseudo_label_worker_execute_pseudo_label_job_params
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
from ..types.model_pseudo_label_worker_execute_pseudo_label_job_response import (
    ModelPseudoLabelWorkerExecutePseudoLabelJobResponse,
)

__all__ = ["ModelPseudoLabelWorkersResource", "AsyncModelPseudoLabelWorkersResource"]


class ModelPseudoLabelWorkersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ModelPseudoLabelWorkersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lastmile-ai/lastmile-python#accessing-raw-response-data-eg-headers
        """
        return ModelPseudoLabelWorkersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModelPseudoLabelWorkersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lastmile-ai/lastmile-python#with_streaming_response
        """
        return ModelPseudoLabelWorkersResourceWithStreamingResponse(self)

    def execute_pseudo_label_job(
        self,
        *,
        pseudo_label_job_id: model_pseudo_label_worker_execute_pseudo_label_job_params.PseudoLabelJobID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelPseudoLabelWorkerExecutePseudoLabelJobResponse:
        """
        Description of execute_pseudo_label_job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/2/auto_eval/model_pseudo_label_worker/execute_pseudo_label_job",
            body=maybe_transform(
                {"pseudo_label_job_id": pseudo_label_job_id},
                model_pseudo_label_worker_execute_pseudo_label_job_params.ModelPseudoLabelWorkerExecutePseudoLabelJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelPseudoLabelWorkerExecutePseudoLabelJobResponse,
        )


class AsyncModelPseudoLabelWorkersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncModelPseudoLabelWorkersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lastmile-ai/lastmile-python#accessing-raw-response-data-eg-headers
        """
        return AsyncModelPseudoLabelWorkersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModelPseudoLabelWorkersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lastmile-ai/lastmile-python#with_streaming_response
        """
        return AsyncModelPseudoLabelWorkersResourceWithStreamingResponse(self)

    async def execute_pseudo_label_job(
        self,
        *,
        pseudo_label_job_id: model_pseudo_label_worker_execute_pseudo_label_job_params.PseudoLabelJobID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelPseudoLabelWorkerExecutePseudoLabelJobResponse:
        """
        Description of execute_pseudo_label_job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/2/auto_eval/model_pseudo_label_worker/execute_pseudo_label_job",
            body=await async_maybe_transform(
                {"pseudo_label_job_id": pseudo_label_job_id},
                model_pseudo_label_worker_execute_pseudo_label_job_params.ModelPseudoLabelWorkerExecutePseudoLabelJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelPseudoLabelWorkerExecutePseudoLabelJobResponse,
        )


class ModelPseudoLabelWorkersResourceWithRawResponse:
    def __init__(self, model_pseudo_label_workers: ModelPseudoLabelWorkersResource) -> None:
        self._model_pseudo_label_workers = model_pseudo_label_workers

        self.execute_pseudo_label_job = to_raw_response_wrapper(
            model_pseudo_label_workers.execute_pseudo_label_job,
        )


class AsyncModelPseudoLabelWorkersResourceWithRawResponse:
    def __init__(self, model_pseudo_label_workers: AsyncModelPseudoLabelWorkersResource) -> None:
        self._model_pseudo_label_workers = model_pseudo_label_workers

        self.execute_pseudo_label_job = async_to_raw_response_wrapper(
            model_pseudo_label_workers.execute_pseudo_label_job,
        )


class ModelPseudoLabelWorkersResourceWithStreamingResponse:
    def __init__(self, model_pseudo_label_workers: ModelPseudoLabelWorkersResource) -> None:
        self._model_pseudo_label_workers = model_pseudo_label_workers

        self.execute_pseudo_label_job = to_streamed_response_wrapper(
            model_pseudo_label_workers.execute_pseudo_label_job,
        )


class AsyncModelPseudoLabelWorkersResourceWithStreamingResponse:
    def __init__(self, model_pseudo_label_workers: AsyncModelPseudoLabelWorkersResource) -> None:
        self._model_pseudo_label_workers = model_pseudo_label_workers

        self.execute_pseudo_label_job = async_to_streamed_response_wrapper(
            model_pseudo_label_workers.execute_pseudo_label_job,
        )
