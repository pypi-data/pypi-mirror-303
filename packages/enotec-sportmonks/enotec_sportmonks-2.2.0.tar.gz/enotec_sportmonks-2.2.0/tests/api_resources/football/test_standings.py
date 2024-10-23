# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sportmonks import Sportmonks, AsyncSportmonks
from tests.utils import assert_matches_type
from sportmonks.pagination import SyncPaginatedAPICall, AsyncPaginatedAPICall
from sportmonks.types.football import StandingListResponse, StandingListBySeasonResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStandings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Sportmonks) -> None:
        standing = client.football.standings.list(
            sport="football",
            version="v3",
        )
        assert_matches_type(SyncPaginatedAPICall[StandingListResponse], standing, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Sportmonks) -> None:
        standing = client.football.standings.list(
            sport="football",
            version="v3",
            order="asc",
            page=1,
            per_page=25,
        )
        assert_matches_type(SyncPaginatedAPICall[StandingListResponse], standing, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Sportmonks) -> None:
        response = client.football.standings.with_raw_response.list(
            sport="football",
            version="v3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        standing = response.parse()
        assert_matches_type(SyncPaginatedAPICall[StandingListResponse], standing, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Sportmonks) -> None:
        with client.football.standings.with_streaming_response.list(
            sport="football",
            version="v3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            standing = response.parse()
            assert_matches_type(SyncPaginatedAPICall[StandingListResponse], standing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Sportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.football.standings.with_raw_response.list(
                sport="football",
                version="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            client.football.standings.with_raw_response.list(
                sport="",
                version="v3",
            )

    @parametrize
    def test_method_list_by_season(self, client: Sportmonks) -> None:
        standing = client.football.standings.list_by_season(
            season_id="19686",
            version="v3",
            sport="football",
        )
        assert_matches_type(StandingListBySeasonResponse, standing, path=["response"])

    @parametrize
    def test_raw_response_list_by_season(self, client: Sportmonks) -> None:
        response = client.football.standings.with_raw_response.list_by_season(
            season_id="19686",
            version="v3",
            sport="football",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        standing = response.parse()
        assert_matches_type(StandingListBySeasonResponse, standing, path=["response"])

    @parametrize
    def test_streaming_response_list_by_season(self, client: Sportmonks) -> None:
        with client.football.standings.with_streaming_response.list_by_season(
            season_id="19686",
            version="v3",
            sport="football",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            standing = response.parse()
            assert_matches_type(StandingListBySeasonResponse, standing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_by_season(self, client: Sportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.football.standings.with_raw_response.list_by_season(
                season_id="19686",
                version="",
                sport="football",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            client.football.standings.with_raw_response.list_by_season(
                season_id="19686",
                version="v3",
                sport="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `season_id` but received ''"):
            client.football.standings.with_raw_response.list_by_season(
                season_id="",
                version="v3",
                sport="football",
            )


class TestAsyncStandings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncSportmonks) -> None:
        standing = await async_client.football.standings.list(
            sport="football",
            version="v3",
        )
        assert_matches_type(AsyncPaginatedAPICall[StandingListResponse], standing, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSportmonks) -> None:
        standing = await async_client.football.standings.list(
            sport="football",
            version="v3",
            order="asc",
            page=1,
            per_page=25,
        )
        assert_matches_type(AsyncPaginatedAPICall[StandingListResponse], standing, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSportmonks) -> None:
        response = await async_client.football.standings.with_raw_response.list(
            sport="football",
            version="v3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        standing = await response.parse()
        assert_matches_type(AsyncPaginatedAPICall[StandingListResponse], standing, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSportmonks) -> None:
        async with async_client.football.standings.with_streaming_response.list(
            sport="football",
            version="v3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            standing = await response.parse()
            assert_matches_type(AsyncPaginatedAPICall[StandingListResponse], standing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncSportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.football.standings.with_raw_response.list(
                sport="football",
                version="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            await async_client.football.standings.with_raw_response.list(
                sport="",
                version="v3",
            )

    @parametrize
    async def test_method_list_by_season(self, async_client: AsyncSportmonks) -> None:
        standing = await async_client.football.standings.list_by_season(
            season_id="19686",
            version="v3",
            sport="football",
        )
        assert_matches_type(StandingListBySeasonResponse, standing, path=["response"])

    @parametrize
    async def test_raw_response_list_by_season(self, async_client: AsyncSportmonks) -> None:
        response = await async_client.football.standings.with_raw_response.list_by_season(
            season_id="19686",
            version="v3",
            sport="football",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        standing = await response.parse()
        assert_matches_type(StandingListBySeasonResponse, standing, path=["response"])

    @parametrize
    async def test_streaming_response_list_by_season(self, async_client: AsyncSportmonks) -> None:
        async with async_client.football.standings.with_streaming_response.list_by_season(
            season_id="19686",
            version="v3",
            sport="football",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            standing = await response.parse()
            assert_matches_type(StandingListBySeasonResponse, standing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_by_season(self, async_client: AsyncSportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.football.standings.with_raw_response.list_by_season(
                season_id="19686",
                version="",
                sport="football",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            await async_client.football.standings.with_raw_response.list_by_season(
                season_id="19686",
                version="v3",
                sport="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `season_id` but received ''"):
            await async_client.football.standings.with_raw_response.list_by_season(
                season_id="",
                version="v3",
                sport="football",
            )
