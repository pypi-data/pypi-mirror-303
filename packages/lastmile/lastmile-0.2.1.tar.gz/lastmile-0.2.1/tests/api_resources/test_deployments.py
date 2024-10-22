# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lastmile import Lastmile, AsyncLastmile
from tests.utils import assert_matches_type
from lastmile.types import DeploymentDeployInferenceEndpointResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDeployments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_deploy_inference_endpoint(self, client: Lastmile) -> None:
        deployment = client.deployments.deploy_inference_endpoint(
            model_file_id={"value": "value"},
        )
        assert_matches_type(DeploymentDeployInferenceEndpointResponse, deployment, path=["response"])

    @parametrize
    def test_raw_response_deploy_inference_endpoint(self, client: Lastmile) -> None:
        response = client.deployments.with_raw_response.deploy_inference_endpoint(
            model_file_id={"value": "value"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = response.parse()
        assert_matches_type(DeploymentDeployInferenceEndpointResponse, deployment, path=["response"])

    @parametrize
    def test_streaming_response_deploy_inference_endpoint(self, client: Lastmile) -> None:
        with client.deployments.with_streaming_response.deploy_inference_endpoint(
            model_file_id={"value": "value"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = response.parse()
            assert_matches_type(DeploymentDeployInferenceEndpointResponse, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDeployments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_deploy_inference_endpoint(self, async_client: AsyncLastmile) -> None:
        deployment = await async_client.deployments.deploy_inference_endpoint(
            model_file_id={"value": "value"},
        )
        assert_matches_type(DeploymentDeployInferenceEndpointResponse, deployment, path=["response"])

    @parametrize
    async def test_raw_response_deploy_inference_endpoint(self, async_client: AsyncLastmile) -> None:
        response = await async_client.deployments.with_raw_response.deploy_inference_endpoint(
            model_file_id={"value": "value"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deployment = await response.parse()
        assert_matches_type(DeploymentDeployInferenceEndpointResponse, deployment, path=["response"])

    @parametrize
    async def test_streaming_response_deploy_inference_endpoint(self, async_client: AsyncLastmile) -> None:
        async with async_client.deployments.with_streaming_response.deploy_inference_endpoint(
            model_file_id={"value": "value"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deployment = await response.parse()
            assert_matches_type(DeploymentDeployInferenceEndpointResponse, deployment, path=["response"])

        assert cast(Any, response.is_closed) is True
