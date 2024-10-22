# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable

import httpx

from ..types import evaluation_evaluate_params, evaluation_evaluate_dataset_params
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
from ..types.evaluation_evaluate_response import EvaluationEvaluateResponse
from ..types.evaluation_list_metrics_response import EvaluationListMetricsResponse
from ..types.evaluation_evaluate_dataset_response import EvaluationEvaluateDatasetResponse

__all__ = ["EvaluationsResource", "AsyncEvaluationsResource"]


class EvaluationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EvaluationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lastmile-ai/lastmile-python#accessing-raw-response-data-eg-headers
        """
        return EvaluationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvaluationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lastmile-ai/lastmile-python#with_streaming_response
        """
        return EvaluationsResourceWithStreamingResponse(self)

    def evaluate(
        self,
        *,
        ground_truth: List[str],
        input: List[str],
        models: Iterable[evaluation_evaluate_params.Model],
        output: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationEvaluateResponse:
        """
        Description of evaluate

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/2/auto_eval/evaluation/evaluate",
            body=maybe_transform(
                {
                    "ground_truth": ground_truth,
                    "input": input,
                    "models": models,
                    "output": output,
                },
                evaluation_evaluate_params.EvaluationEvaluateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationEvaluateResponse,
        )

    def evaluate_dataset(
        self,
        *,
        dataset_id: evaluation_evaluate_dataset_params.DatasetID,
        models: Iterable[evaluation_evaluate_dataset_params.Model],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationEvaluateDatasetResponse:
        """
        Description of evaluate_dataset

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/2/auto_eval/evaluation/evaluate_dataset",
            body=maybe_transform(
                {
                    "dataset_id": dataset_id,
                    "models": models,
                },
                evaluation_evaluate_dataset_params.EvaluationEvaluateDatasetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationEvaluateDatasetResponse,
        )

    def list_metrics(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationListMetricsResponse:
        """Description of list_metrics"""
        return self._post(
            "/api/2/auto_eval/evaluation/list_metrics",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationListMetricsResponse,
        )


class AsyncEvaluationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEvaluationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lastmile-ai/lastmile-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvaluationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvaluationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lastmile-ai/lastmile-python#with_streaming_response
        """
        return AsyncEvaluationsResourceWithStreamingResponse(self)

    async def evaluate(
        self,
        *,
        ground_truth: List[str],
        input: List[str],
        models: Iterable[evaluation_evaluate_params.Model],
        output: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationEvaluateResponse:
        """
        Description of evaluate

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/2/auto_eval/evaluation/evaluate",
            body=await async_maybe_transform(
                {
                    "ground_truth": ground_truth,
                    "input": input,
                    "models": models,
                    "output": output,
                },
                evaluation_evaluate_params.EvaluationEvaluateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationEvaluateResponse,
        )

    async def evaluate_dataset(
        self,
        *,
        dataset_id: evaluation_evaluate_dataset_params.DatasetID,
        models: Iterable[evaluation_evaluate_dataset_params.Model],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationEvaluateDatasetResponse:
        """
        Description of evaluate_dataset

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/2/auto_eval/evaluation/evaluate_dataset",
            body=await async_maybe_transform(
                {
                    "dataset_id": dataset_id,
                    "models": models,
                },
                evaluation_evaluate_dataset_params.EvaluationEvaluateDatasetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationEvaluateDatasetResponse,
        )

    async def list_metrics(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationListMetricsResponse:
        """Description of list_metrics"""
        return await self._post(
            "/api/2/auto_eval/evaluation/list_metrics",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationListMetricsResponse,
        )


class EvaluationsResourceWithRawResponse:
    def __init__(self, evaluations: EvaluationsResource) -> None:
        self._evaluations = evaluations

        self.evaluate = to_raw_response_wrapper(
            evaluations.evaluate,
        )
        self.evaluate_dataset = to_raw_response_wrapper(
            evaluations.evaluate_dataset,
        )
        self.list_metrics = to_raw_response_wrapper(
            evaluations.list_metrics,
        )


class AsyncEvaluationsResourceWithRawResponse:
    def __init__(self, evaluations: AsyncEvaluationsResource) -> None:
        self._evaluations = evaluations

        self.evaluate = async_to_raw_response_wrapper(
            evaluations.evaluate,
        )
        self.evaluate_dataset = async_to_raw_response_wrapper(
            evaluations.evaluate_dataset,
        )
        self.list_metrics = async_to_raw_response_wrapper(
            evaluations.list_metrics,
        )


class EvaluationsResourceWithStreamingResponse:
    def __init__(self, evaluations: EvaluationsResource) -> None:
        self._evaluations = evaluations

        self.evaluate = to_streamed_response_wrapper(
            evaluations.evaluate,
        )
        self.evaluate_dataset = to_streamed_response_wrapper(
            evaluations.evaluate_dataset,
        )
        self.list_metrics = to_streamed_response_wrapper(
            evaluations.list_metrics,
        )


class AsyncEvaluationsResourceWithStreamingResponse:
    def __init__(self, evaluations: AsyncEvaluationsResource) -> None:
        self._evaluations = evaluations

        self.evaluate = async_to_streamed_response_wrapper(
            evaluations.evaluate,
        )
        self.evaluate_dataset = async_to_streamed_response_wrapper(
            evaluations.evaluate_dataset,
        )
        self.list_metrics = async_to_streamed_response_wrapper(
            evaluations.list_metrics,
        )
