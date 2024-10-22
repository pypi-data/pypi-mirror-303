# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    fine_tune_job_create_params,
    fine_tune_job_submit_params,
    fine_tune_job_configure_params,
    fine_tune_job_get_status_params,
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
from ..types.fine_tune_job_create_response import FineTuneJobCreateResponse
from ..types.fine_tune_job_submit_response import FineTuneJobSubmitResponse
from ..types.fine_tune_job_configure_response import FineTuneJobConfigureResponse
from ..types.fine_tune_job_get_status_response import FineTuneJobGetStatusResponse

__all__ = ["FineTuneJobsResource", "AsyncFineTuneJobsResource"]


class FineTuneJobsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FineTuneJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lastmile-ai/lastmile-python#accessing-raw-response-data-eg-headers
        """
        return FineTuneJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FineTuneJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lastmile-ai/lastmile-python#with_streaming_response
        """
        return FineTuneJobsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        fine_tune_job_config: fine_tune_job_create_params.FineTuneJobConfig,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FineTuneJobCreateResponse:
        """
        Description of create

        Args:
          fine_tune_job_config: See repos/lastmile/prisma/schema.prisma:AEFineTuneJobConfig

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/2/auto_eval/fine_tune_job/create",
            body=maybe_transform(
                {"fine_tune_job_config": fine_tune_job_config}, fine_tune_job_create_params.FineTuneJobCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FineTuneJobCreateResponse,
        )

    def configure(
        self,
        *,
        fine_tune_job_config: fine_tune_job_configure_params.FineTuneJobConfig,
        job_id: fine_tune_job_configure_params.JobID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FineTuneJobConfigureResponse:
        """
        Description of configure

        Args:
          fine_tune_job_config: See repos/lastmile/prisma/schema.prisma:AEFineTuneJobConfig

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/api/2/auto_eval/fine_tune_job/configure",
            body=maybe_transform(
                {
                    "fine_tune_job_config": fine_tune_job_config,
                    "job_id": job_id,
                },
                fine_tune_job_configure_params.FineTuneJobConfigureParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FineTuneJobConfigureResponse,
        )

    def get_status(
        self,
        *,
        job_id: fine_tune_job_get_status_params.JobID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FineTuneJobGetStatusResponse:
        """
        Description of get_status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/2/auto_eval/fine_tune_job/get_status",
            body=maybe_transform({"job_id": job_id}, fine_tune_job_get_status_params.FineTuneJobGetStatusParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FineTuneJobGetStatusResponse,
        )

    def submit(
        self,
        *,
        fine_tune_job_config: fine_tune_job_submit_params.FineTuneJobConfig,
        job_id: fine_tune_job_submit_params.JobID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FineTuneJobSubmitResponse:
        """
        Description of submit

        Args:
          fine_tune_job_config: See repos/lastmile/prisma/schema.prisma:AEFineTuneJobConfig

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/2/auto_eval/fine_tune_job/submit",
            body=maybe_transform(
                {
                    "fine_tune_job_config": fine_tune_job_config,
                    "job_id": job_id,
                },
                fine_tune_job_submit_params.FineTuneJobSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FineTuneJobSubmitResponse,
        )


class AsyncFineTuneJobsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFineTuneJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lastmile-ai/lastmile-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFineTuneJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFineTuneJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lastmile-ai/lastmile-python#with_streaming_response
        """
        return AsyncFineTuneJobsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        fine_tune_job_config: fine_tune_job_create_params.FineTuneJobConfig,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FineTuneJobCreateResponse:
        """
        Description of create

        Args:
          fine_tune_job_config: See repos/lastmile/prisma/schema.prisma:AEFineTuneJobConfig

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/2/auto_eval/fine_tune_job/create",
            body=await async_maybe_transform(
                {"fine_tune_job_config": fine_tune_job_config}, fine_tune_job_create_params.FineTuneJobCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FineTuneJobCreateResponse,
        )

    async def configure(
        self,
        *,
        fine_tune_job_config: fine_tune_job_configure_params.FineTuneJobConfig,
        job_id: fine_tune_job_configure_params.JobID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FineTuneJobConfigureResponse:
        """
        Description of configure

        Args:
          fine_tune_job_config: See repos/lastmile/prisma/schema.prisma:AEFineTuneJobConfig

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/api/2/auto_eval/fine_tune_job/configure",
            body=await async_maybe_transform(
                {
                    "fine_tune_job_config": fine_tune_job_config,
                    "job_id": job_id,
                },
                fine_tune_job_configure_params.FineTuneJobConfigureParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FineTuneJobConfigureResponse,
        )

    async def get_status(
        self,
        *,
        job_id: fine_tune_job_get_status_params.JobID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FineTuneJobGetStatusResponse:
        """
        Description of get_status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/2/auto_eval/fine_tune_job/get_status",
            body=await async_maybe_transform(
                {"job_id": job_id}, fine_tune_job_get_status_params.FineTuneJobGetStatusParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FineTuneJobGetStatusResponse,
        )

    async def submit(
        self,
        *,
        fine_tune_job_config: fine_tune_job_submit_params.FineTuneJobConfig,
        job_id: fine_tune_job_submit_params.JobID,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FineTuneJobSubmitResponse:
        """
        Description of submit

        Args:
          fine_tune_job_config: See repos/lastmile/prisma/schema.prisma:AEFineTuneJobConfig

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/2/auto_eval/fine_tune_job/submit",
            body=await async_maybe_transform(
                {
                    "fine_tune_job_config": fine_tune_job_config,
                    "job_id": job_id,
                },
                fine_tune_job_submit_params.FineTuneJobSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FineTuneJobSubmitResponse,
        )


class FineTuneJobsResourceWithRawResponse:
    def __init__(self, fine_tune_jobs: FineTuneJobsResource) -> None:
        self._fine_tune_jobs = fine_tune_jobs

        self.create = to_raw_response_wrapper(
            fine_tune_jobs.create,
        )
        self.configure = to_raw_response_wrapper(
            fine_tune_jobs.configure,
        )
        self.get_status = to_raw_response_wrapper(
            fine_tune_jobs.get_status,
        )
        self.submit = to_raw_response_wrapper(
            fine_tune_jobs.submit,
        )


class AsyncFineTuneJobsResourceWithRawResponse:
    def __init__(self, fine_tune_jobs: AsyncFineTuneJobsResource) -> None:
        self._fine_tune_jobs = fine_tune_jobs

        self.create = async_to_raw_response_wrapper(
            fine_tune_jobs.create,
        )
        self.configure = async_to_raw_response_wrapper(
            fine_tune_jobs.configure,
        )
        self.get_status = async_to_raw_response_wrapper(
            fine_tune_jobs.get_status,
        )
        self.submit = async_to_raw_response_wrapper(
            fine_tune_jobs.submit,
        )


class FineTuneJobsResourceWithStreamingResponse:
    def __init__(self, fine_tune_jobs: FineTuneJobsResource) -> None:
        self._fine_tune_jobs = fine_tune_jobs

        self.create = to_streamed_response_wrapper(
            fine_tune_jobs.create,
        )
        self.configure = to_streamed_response_wrapper(
            fine_tune_jobs.configure,
        )
        self.get_status = to_streamed_response_wrapper(
            fine_tune_jobs.get_status,
        )
        self.submit = to_streamed_response_wrapper(
            fine_tune_jobs.submit,
        )


class AsyncFineTuneJobsResourceWithStreamingResponse:
    def __init__(self, fine_tune_jobs: AsyncFineTuneJobsResource) -> None:
        self._fine_tune_jobs = fine_tune_jobs

        self.create = async_to_streamed_response_wrapper(
            fine_tune_jobs.create,
        )
        self.configure = async_to_streamed_response_wrapper(
            fine_tune_jobs.configure,
        )
        self.get_status = async_to_streamed_response_wrapper(
            fine_tune_jobs.get_status,
        )
        self.submit = async_to_streamed_response_wrapper(
            fine_tune_jobs.submit,
        )
