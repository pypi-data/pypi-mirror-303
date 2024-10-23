# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sportmonks import Sportmonks, AsyncSportmonks
from tests.utils import assert_matches_type
from sportmonks.types.football.standings import LiveListByLeagueResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLive:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list_by_league(self, client: Sportmonks) -> None:
        live = client.football.standings.live.list_by_league(
            league_id="271",
            version="v3",
            sport="football",
        )
        assert_matches_type(LiveListByLeagueResponse, live, path=["response"])

    @parametrize
    def test_raw_response_list_by_league(self, client: Sportmonks) -> None:
        response = client.football.standings.live.with_raw_response.list_by_league(
            league_id="271",
            version="v3",
            sport="football",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live = response.parse()
        assert_matches_type(LiveListByLeagueResponse, live, path=["response"])

    @parametrize
    def test_streaming_response_list_by_league(self, client: Sportmonks) -> None:
        with client.football.standings.live.with_streaming_response.list_by_league(
            league_id="271",
            version="v3",
            sport="football",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live = response.parse()
            assert_matches_type(LiveListByLeagueResponse, live, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_by_league(self, client: Sportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.football.standings.live.with_raw_response.list_by_league(
                league_id="271",
                version="",
                sport="football",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            client.football.standings.live.with_raw_response.list_by_league(
                league_id="271",
                version="v3",
                sport="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `league_id` but received ''"):
            client.football.standings.live.with_raw_response.list_by_league(
                league_id="",
                version="v3",
                sport="football",
            )


class TestAsyncLive:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list_by_league(self, async_client: AsyncSportmonks) -> None:
        live = await async_client.football.standings.live.list_by_league(
            league_id="271",
            version="v3",
            sport="football",
        )
        assert_matches_type(LiveListByLeagueResponse, live, path=["response"])

    @parametrize
    async def test_raw_response_list_by_league(self, async_client: AsyncSportmonks) -> None:
        response = await async_client.football.standings.live.with_raw_response.list_by_league(
            league_id="271",
            version="v3",
            sport="football",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live = await response.parse()
        assert_matches_type(LiveListByLeagueResponse, live, path=["response"])

    @parametrize
    async def test_streaming_response_list_by_league(self, async_client: AsyncSportmonks) -> None:
        async with async_client.football.standings.live.with_streaming_response.list_by_league(
            league_id="271",
            version="v3",
            sport="football",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live = await response.parse()
            assert_matches_type(LiveListByLeagueResponse, live, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_by_league(self, async_client: AsyncSportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.football.standings.live.with_raw_response.list_by_league(
                league_id="271",
                version="",
                sport="football",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            await async_client.football.standings.live.with_raw_response.list_by_league(
                league_id="271",
                version="v3",
                sport="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `league_id` but received ''"):
            await async_client.football.standings.live.with_raw_response.list_by_league(
                league_id="",
                version="v3",
                sport="football",
            )
