# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sportmonks import Sportmonks, AsyncSportmonks
from tests.utils import assert_matches_type
from sportmonks.pagination import SyncPaginatedAPICall, AsyncPaginatedAPICall
from sportmonks.types.core import ContinentListResponse, ContinentRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContinents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Sportmonks) -> None:
        continent = client.core.continents.retrieve(
            continent_id="1",
            version="v3",
        )
        assert_matches_type(ContinentRetrieveResponse, continent, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Sportmonks) -> None:
        response = client.core.continents.with_raw_response.retrieve(
            continent_id="1",
            version="v3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        continent = response.parse()
        assert_matches_type(ContinentRetrieveResponse, continent, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Sportmonks) -> None:
        with client.core.continents.with_streaming_response.retrieve(
            continent_id="1",
            version="v3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            continent = response.parse()
            assert_matches_type(ContinentRetrieveResponse, continent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Sportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.core.continents.with_raw_response.retrieve(
                continent_id="1",
                version="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `continent_id` but received ''"):
            client.core.continents.with_raw_response.retrieve(
                continent_id="",
                version="v3",
            )

    @parametrize
    def test_method_list(self, client: Sportmonks) -> None:
        continent = client.core.continents.list(
            version="v3",
        )
        assert_matches_type(SyncPaginatedAPICall[ContinentListResponse], continent, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Sportmonks) -> None:
        continent = client.core.continents.list(
            version="v3",
            order="asc",
            page=1,
            per_page=25,
        )
        assert_matches_type(SyncPaginatedAPICall[ContinentListResponse], continent, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Sportmonks) -> None:
        response = client.core.continents.with_raw_response.list(
            version="v3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        continent = response.parse()
        assert_matches_type(SyncPaginatedAPICall[ContinentListResponse], continent, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Sportmonks) -> None:
        with client.core.continents.with_streaming_response.list(
            version="v3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            continent = response.parse()
            assert_matches_type(SyncPaginatedAPICall[ContinentListResponse], continent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Sportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.core.continents.with_raw_response.list(
                version="",
            )


class TestAsyncContinents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSportmonks) -> None:
        continent = await async_client.core.continents.retrieve(
            continent_id="1",
            version="v3",
        )
        assert_matches_type(ContinentRetrieveResponse, continent, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSportmonks) -> None:
        response = await async_client.core.continents.with_raw_response.retrieve(
            continent_id="1",
            version="v3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        continent = await response.parse()
        assert_matches_type(ContinentRetrieveResponse, continent, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSportmonks) -> None:
        async with async_client.core.continents.with_streaming_response.retrieve(
            continent_id="1",
            version="v3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            continent = await response.parse()
            assert_matches_type(ContinentRetrieveResponse, continent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.core.continents.with_raw_response.retrieve(
                continent_id="1",
                version="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `continent_id` but received ''"):
            await async_client.core.continents.with_raw_response.retrieve(
                continent_id="",
                version="v3",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSportmonks) -> None:
        continent = await async_client.core.continents.list(
            version="v3",
        )
        assert_matches_type(AsyncPaginatedAPICall[ContinentListResponse], continent, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSportmonks) -> None:
        continent = await async_client.core.continents.list(
            version="v3",
            order="asc",
            page=1,
            per_page=25,
        )
        assert_matches_type(AsyncPaginatedAPICall[ContinentListResponse], continent, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSportmonks) -> None:
        response = await async_client.core.continents.with_raw_response.list(
            version="v3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        continent = await response.parse()
        assert_matches_type(AsyncPaginatedAPICall[ContinentListResponse], continent, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSportmonks) -> None:
        async with async_client.core.continents.with_streaming_response.list(
            version="v3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            continent = await response.parse()
            assert_matches_type(AsyncPaginatedAPICall[ContinentListResponse], continent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncSportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.core.continents.with_raw_response.list(
                version="",
            )
