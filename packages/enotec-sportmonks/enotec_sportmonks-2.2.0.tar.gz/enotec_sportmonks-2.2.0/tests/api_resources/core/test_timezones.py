# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sportmonks import Sportmonks, AsyncSportmonks
from tests.utils import assert_matches_type
from sportmonks.pagination import SyncPaginatedAPICall, AsyncPaginatedAPICall
from sportmonks.types.core import TimezoneListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTimezones:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Sportmonks) -> None:
        timezone = client.core.timezones.list(
            version="v3",
        )
        assert_matches_type(SyncPaginatedAPICall[TimezoneListResponse], timezone, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Sportmonks) -> None:
        timezone = client.core.timezones.list(
            version="v3",
            order="asc",
            page=1,
            per_page=25,
        )
        assert_matches_type(SyncPaginatedAPICall[TimezoneListResponse], timezone, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Sportmonks) -> None:
        response = client.core.timezones.with_raw_response.list(
            version="v3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timezone = response.parse()
        assert_matches_type(SyncPaginatedAPICall[TimezoneListResponse], timezone, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Sportmonks) -> None:
        with client.core.timezones.with_streaming_response.list(
            version="v3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timezone = response.parse()
            assert_matches_type(SyncPaginatedAPICall[TimezoneListResponse], timezone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Sportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.core.timezones.with_raw_response.list(
                version="",
            )


class TestAsyncTimezones:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncSportmonks) -> None:
        timezone = await async_client.core.timezones.list(
            version="v3",
        )
        assert_matches_type(AsyncPaginatedAPICall[TimezoneListResponse], timezone, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSportmonks) -> None:
        timezone = await async_client.core.timezones.list(
            version="v3",
            order="asc",
            page=1,
            per_page=25,
        )
        assert_matches_type(AsyncPaginatedAPICall[TimezoneListResponse], timezone, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSportmonks) -> None:
        response = await async_client.core.timezones.with_raw_response.list(
            version="v3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timezone = await response.parse()
        assert_matches_type(AsyncPaginatedAPICall[TimezoneListResponse], timezone, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSportmonks) -> None:
        async with async_client.core.timezones.with_streaming_response.list(
            version="v3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timezone = await response.parse()
            assert_matches_type(AsyncPaginatedAPICall[TimezoneListResponse], timezone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncSportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.core.timezones.with_raw_response.list(
                version="",
            )
