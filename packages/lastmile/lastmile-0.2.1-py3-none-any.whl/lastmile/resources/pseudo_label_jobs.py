# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    pseudo_label_job_create_params,
    pseudo_label_job_submit_params,
    pseudo_label_job_configure_params,
    pseudo_label_job_get_status_params,
)
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
from ..types.pseudo_label_job_create_response import PseudoLabelJobCreateResponse
from ..types.pseudo_label_job_submit_response import PseudoLabelJobSubmitResponse
from ..types.pseudo_label_job_configure_response import PseudoLabelJobConfigureResponse
from ..types.pseudo_label_job_get_status_response import PseudoLabelJobGetStatusResponse

__all__ = ["PseudoLabelJobsResource", "AsyncPseudoLabelJobsResource"]


class PseudoLabelJobsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PseudoLabelJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lastmile-ai/lastmile-python#accessing-raw-response-data-eg-headers
        """
        return PseudoLabelJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PseudoLabelJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lastmile-ai/lastmile-python#with_streaming_response
        """
        return PseudoLabelJobsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        pseudo_label_job_config: pseudo_label_job_create_params.PseudoLabelJobConfig,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PseudoLabelJobCreateResponse:
        """
        Description of create

        Args:
          pseudo_label_job_config: Subset of columns to be used in pseudo-labeling. Expected columns: input,
              output, ground_truth For example, a summarization task might not need an input
              column. TODO: Should this be repeated EvaluationMetricParameter enum?

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/2/auto_eval/pseudo_label_job/create",
            body=maybe_transform(
                {"pseudo_label_job_config": pseudo_label_job_config},
                pseudo_label_job_create_params.PseudoLabelJobCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PseudoLabelJobCreateResponse,
        )

    def configure(
        self,
        *,
        job_id: pseudo_label_job_configure_params.JobID,
        pseudo_label_job_config: pseudo_label_job_configure_params.PseudoLabelJobConfig,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PseudoLabelJobConfigureResponse:
        """
        Description of configure

        Args:
          pseudo_label_job_config: Subset of columns to be used in pseudo-labeling. Expected columns: input,
              output, ground_truth For example, a summarization task might not need an input
              column. TODO: Should this be repeated EvaluationMetricParameter enum?

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/api/2/auto_eval/pseudo_label_job/configure",
            body=maybe_transform(
                {
                    "job_id": job_id,
                    "pseudo_label_job_config": pseudo_label_job_config,
                },
                pseudo_label_job_configure_params.PseudoLabelJobConfigureParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PseudoLabelJobConfigureResponse,
        )

    def get_status(
        self,
        *,
        job_id: pseudo_label_job_get_status_params.JobID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PseudoLabelJobGetStatusResponse:
        """
        Description of get_status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/2/auto_eval/pseudo_label_job/get_status",
            body=maybe_transform({"job_id": job_id}, pseudo_label_job_get_status_params.PseudoLabelJobGetStatusParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PseudoLabelJobGetStatusResponse,
        )

    def submit(
        self,
        *,
        job_id: pseudo_label_job_submit_params.JobID,
        pseudo_label_job_config: pseudo_label_job_submit_params.PseudoLabelJobConfig,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PseudoLabelJobSubmitResponse:
        """
        Description of submit

        Args:
          pseudo_label_job_config: Subset of columns to be used in pseudo-labeling. Expected columns: input,
              output, ground_truth For example, a summarization task might not need an input
              column. TODO: Should this be repeated EvaluationMetricParameter enum?

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/2/auto_eval/pseudo_label_job/submit",
            body=maybe_transform(
                {
                    "job_id": job_id,
                    "pseudo_label_job_config": pseudo_label_job_config,
                },
                pseudo_label_job_submit_params.PseudoLabelJobSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PseudoLabelJobSubmitResponse,
        )


class AsyncPseudoLabelJobsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPseudoLabelJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lastmile-ai/lastmile-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPseudoLabelJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPseudoLabelJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lastmile-ai/lastmile-python#with_streaming_response
        """
        return AsyncPseudoLabelJobsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        pseudo_label_job_config: pseudo_label_job_create_params.PseudoLabelJobConfig,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PseudoLabelJobCreateResponse:
        """
        Description of create

        Args:
          pseudo_label_job_config: Subset of columns to be used in pseudo-labeling. Expected columns: input,
              output, ground_truth For example, a summarization task might not need an input
              column. TODO: Should this be repeated EvaluationMetricParameter enum?

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/2/auto_eval/pseudo_label_job/create",
            body=await async_maybe_transform(
                {"pseudo_label_job_config": pseudo_label_job_config},
                pseudo_label_job_create_params.PseudoLabelJobCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PseudoLabelJobCreateResponse,
        )

    async def configure(
        self,
        *,
        job_id: pseudo_label_job_configure_params.JobID,
        pseudo_label_job_config: pseudo_label_job_configure_params.PseudoLabelJobConfig,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PseudoLabelJobConfigureResponse:
        """
        Description of configure

        Args:
          pseudo_label_job_config: Subset of columns to be used in pseudo-labeling. Expected columns: input,
              output, ground_truth For example, a summarization task might not need an input
              column. TODO: Should this be repeated EvaluationMetricParameter enum?

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/api/2/auto_eval/pseudo_label_job/configure",
            body=await async_maybe_transform(
                {
                    "job_id": job_id,
                    "pseudo_label_job_config": pseudo_label_job_config,
                },
                pseudo_label_job_configure_params.PseudoLabelJobConfigureParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PseudoLabelJobConfigureResponse,
        )

    async def get_status(
        self,
        *,
        job_id: pseudo_label_job_get_status_params.JobID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PseudoLabelJobGetStatusResponse:
        """
        Description of get_status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/2/auto_eval/pseudo_label_job/get_status",
            body=await async_maybe_transform(
                {"job_id": job_id}, pseudo_label_job_get_status_params.PseudoLabelJobGetStatusParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PseudoLabelJobGetStatusResponse,
        )

    async def submit(
        self,
        *,
        job_id: pseudo_label_job_submit_params.JobID,
        pseudo_label_job_config: pseudo_label_job_submit_params.PseudoLabelJobConfig,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PseudoLabelJobSubmitResponse:
        """
        Description of submit

        Args:
          pseudo_label_job_config: Subset of columns to be used in pseudo-labeling. Expected columns: input,
              output, ground_truth For example, a summarization task might not need an input
              column. TODO: Should this be repeated EvaluationMetricParameter enum?

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/2/auto_eval/pseudo_label_job/submit",
            body=await async_maybe_transform(
                {
                    "job_id": job_id,
                    "pseudo_label_job_config": pseudo_label_job_config,
                },
                pseudo_label_job_submit_params.PseudoLabelJobSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PseudoLabelJobSubmitResponse,
        )


class PseudoLabelJobsResourceWithRawResponse:
    def __init__(self, pseudo_label_jobs: PseudoLabelJobsResource) -> None:
        self._pseudo_label_jobs = pseudo_label_jobs

        self.create = to_raw_response_wrapper(
            pseudo_label_jobs.create,
        )
        self.configure = to_raw_response_wrapper(
            pseudo_label_jobs.configure,
        )
        self.get_status = to_raw_response_wrapper(
            pseudo_label_jobs.get_status,
        )
        self.submit = to_raw_response_wrapper(
            pseudo_label_jobs.submit,
        )


class AsyncPseudoLabelJobsResourceWithRawResponse:
    def __init__(self, pseudo_label_jobs: AsyncPseudoLabelJobsResource) -> None:
        self._pseudo_label_jobs = pseudo_label_jobs

        self.create = async_to_raw_response_wrapper(
            pseudo_label_jobs.create,
        )
        self.configure = async_to_raw_response_wrapper(
            pseudo_label_jobs.configure,
        )
        self.get_status = async_to_raw_response_wrapper(
            pseudo_label_jobs.get_status,
        )
        self.submit = async_to_raw_response_wrapper(
            pseudo_label_jobs.submit,
        )


class PseudoLabelJobsResourceWithStreamingResponse:
    def __init__(self, pseudo_label_jobs: PseudoLabelJobsResource) -> None:
        self._pseudo_label_jobs = pseudo_label_jobs

        self.create = to_streamed_response_wrapper(
            pseudo_label_jobs.create,
        )
        self.configure = to_streamed_response_wrapper(
            pseudo_label_jobs.configure,
        )
        self.get_status = to_streamed_response_wrapper(
            pseudo_label_jobs.get_status,
        )
        self.submit = to_streamed_response_wrapper(
            pseudo_label_jobs.submit,
        )


class AsyncPseudoLabelJobsResourceWithStreamingResponse:
    def __init__(self, pseudo_label_jobs: AsyncPseudoLabelJobsResource) -> None:
        self._pseudo_label_jobs = pseudo_label_jobs

        self.create = async_to_streamed_response_wrapper(
            pseudo_label_jobs.create,
        )
        self.configure = async_to_streamed_response_wrapper(
            pseudo_label_jobs.configure,
        )
        self.get_status = async_to_streamed_response_wrapper(
            pseudo_label_jobs.get_status,
        )
        self.submit = async_to_streamed_response_wrapper(
            pseudo_label_jobs.submit,
        )
