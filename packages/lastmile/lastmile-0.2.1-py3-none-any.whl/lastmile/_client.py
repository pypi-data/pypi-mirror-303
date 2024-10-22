# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import LastmileError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "Lastmile",
    "AsyncLastmile",
    "Client",
    "AsyncClient",
]


class Lastmile(SyncAPIClient):
    model_pseudo_label_workers: resources.ModelPseudoLabelWorkersResource
    model_fine_tune_workers: resources.ModelFineTuneWorkersResource
    datasets: resources.DatasetsResource
    deployments: resources.DeploymentsResource
    evaluations: resources.EvaluationsResource
    fine_tune_jobs: resources.FineTuneJobsResource
    models: resources.ModelsResource
    pseudo_label_jobs: resources.PseudoLabelJobsResource
    with_raw_response: LastmileWithRawResponse
    with_streaming_response: LastmileWithStreamedResponse

    # client options
    bearer_token: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous lastmile client instance.

        This automatically infers the `bearer_token` argument from the `LASTMILE_API_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("LASTMILE_API_TOKEN")
        if bearer_token is None:
            raise LastmileError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the LASTMILE_API_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("LASTMILE_BASE_URL")
        if base_url is None:
            base_url = f"https://lastmileai.dev"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.model_pseudo_label_workers = resources.ModelPseudoLabelWorkersResource(self)
        self.model_fine_tune_workers = resources.ModelFineTuneWorkersResource(self)
        self.datasets = resources.DatasetsResource(self)
        self.deployments = resources.DeploymentsResource(self)
        self.evaluations = resources.EvaluationsResource(self)
        self.fine_tune_jobs = resources.FineTuneJobsResource(self)
        self.models = resources.ModelsResource(self)
        self.pseudo_label_jobs = resources.PseudoLabelJobsResource(self)
        self.with_raw_response = LastmileWithRawResponse(self)
        self.with_streaming_response = LastmileWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncLastmile(AsyncAPIClient):
    model_pseudo_label_workers: resources.AsyncModelPseudoLabelWorkersResource
    model_fine_tune_workers: resources.AsyncModelFineTuneWorkersResource
    datasets: resources.AsyncDatasetsResource
    deployments: resources.AsyncDeploymentsResource
    evaluations: resources.AsyncEvaluationsResource
    fine_tune_jobs: resources.AsyncFineTuneJobsResource
    models: resources.AsyncModelsResource
    pseudo_label_jobs: resources.AsyncPseudoLabelJobsResource
    with_raw_response: AsyncLastmileWithRawResponse
    with_streaming_response: AsyncLastmileWithStreamedResponse

    # client options
    bearer_token: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async lastmile client instance.

        This automatically infers the `bearer_token` argument from the `LASTMILE_API_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("LASTMILE_API_TOKEN")
        if bearer_token is None:
            raise LastmileError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the LASTMILE_API_TOKEN environment variable"
            )
        self.bearer_token = bearer_token
            
        if base_url is None:
            base_url = os.environ.get("LASTMILE_BASE_URL")
        if base_url is None:
            base_url = f"https://lastmileai.dev"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.model_pseudo_label_workers = resources.AsyncModelPseudoLabelWorkersResource(self)
        self.model_fine_tune_workers = resources.AsyncModelFineTuneWorkersResource(self)
        self.datasets = resources.AsyncDatasetsResource(self)
        self.deployments = resources.AsyncDeploymentsResource(self)
        self.evaluations = resources.AsyncEvaluationsResource(self)
        self.fine_tune_jobs = resources.AsyncFineTuneJobsResource(self)
        self.models = resources.AsyncModelsResource(self)
        self.pseudo_label_jobs = resources.AsyncPseudoLabelJobsResource(self)
        self.with_raw_response = AsyncLastmileWithRawResponse(self)
        self.with_streaming_response = AsyncLastmileWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class LastmileWithRawResponse:
    def __init__(self, client: Lastmile) -> None:
        self.model_pseudo_label_workers = resources.ModelPseudoLabelWorkersResourceWithRawResponse(
            client.model_pseudo_label_workers
        )
        self.model_fine_tune_workers = resources.ModelFineTuneWorkersResourceWithRawResponse(
            client.model_fine_tune_workers
        )
        self.datasets = resources.DatasetsResourceWithRawResponse(client.datasets)
        self.deployments = resources.DeploymentsResourceWithRawResponse(client.deployments)
        self.evaluations = resources.EvaluationsResourceWithRawResponse(client.evaluations)
        self.fine_tune_jobs = resources.FineTuneJobsResourceWithRawResponse(client.fine_tune_jobs)
        self.models = resources.ModelsResourceWithRawResponse(client.models)
        self.pseudo_label_jobs = resources.PseudoLabelJobsResourceWithRawResponse(client.pseudo_label_jobs)


class AsyncLastmileWithRawResponse:
    def __init__(self, client: AsyncLastmile) -> None:
        self.model_pseudo_label_workers = resources.AsyncModelPseudoLabelWorkersResourceWithRawResponse(
            client.model_pseudo_label_workers
        )
        self.model_fine_tune_workers = resources.AsyncModelFineTuneWorkersResourceWithRawResponse(
            client.model_fine_tune_workers
        )
        self.datasets = resources.AsyncDatasetsResourceWithRawResponse(client.datasets)
        self.deployments = resources.AsyncDeploymentsResourceWithRawResponse(client.deployments)
        self.evaluations = resources.AsyncEvaluationsResourceWithRawResponse(client.evaluations)
        self.fine_tune_jobs = resources.AsyncFineTuneJobsResourceWithRawResponse(client.fine_tune_jobs)
        self.models = resources.AsyncModelsResourceWithRawResponse(client.models)
        self.pseudo_label_jobs = resources.AsyncPseudoLabelJobsResourceWithRawResponse(client.pseudo_label_jobs)


class LastmileWithStreamedResponse:
    def __init__(self, client: Lastmile) -> None:
        self.model_pseudo_label_workers = resources.ModelPseudoLabelWorkersResourceWithStreamingResponse(
            client.model_pseudo_label_workers
        )
        self.model_fine_tune_workers = resources.ModelFineTuneWorkersResourceWithStreamingResponse(
            client.model_fine_tune_workers
        )
        self.datasets = resources.DatasetsResourceWithStreamingResponse(client.datasets)
        self.deployments = resources.DeploymentsResourceWithStreamingResponse(client.deployments)
        self.evaluations = resources.EvaluationsResourceWithStreamingResponse(client.evaluations)
        self.fine_tune_jobs = resources.FineTuneJobsResourceWithStreamingResponse(client.fine_tune_jobs)
        self.models = resources.ModelsResourceWithStreamingResponse(client.models)
        self.pseudo_label_jobs = resources.PseudoLabelJobsResourceWithStreamingResponse(client.pseudo_label_jobs)


class AsyncLastmileWithStreamedResponse:
    def __init__(self, client: AsyncLastmile) -> None:
        self.model_pseudo_label_workers = resources.AsyncModelPseudoLabelWorkersResourceWithStreamingResponse(
            client.model_pseudo_label_workers
        )
        self.model_fine_tune_workers = resources.AsyncModelFineTuneWorkersResourceWithStreamingResponse(
            client.model_fine_tune_workers
        )
        self.datasets = resources.AsyncDatasetsResourceWithStreamingResponse(client.datasets)
        self.deployments = resources.AsyncDeploymentsResourceWithStreamingResponse(client.deployments)
        self.evaluations = resources.AsyncEvaluationsResourceWithStreamingResponse(client.evaluations)
        self.fine_tune_jobs = resources.AsyncFineTuneJobsResourceWithStreamingResponse(client.fine_tune_jobs)
        self.models = resources.AsyncModelsResourceWithStreamingResponse(client.models)
        self.pseudo_label_jobs = resources.AsyncPseudoLabelJobsResourceWithStreamingResponse(client.pseudo_label_jobs)


Client = Lastmile

AsyncClient = AsyncLastmile
