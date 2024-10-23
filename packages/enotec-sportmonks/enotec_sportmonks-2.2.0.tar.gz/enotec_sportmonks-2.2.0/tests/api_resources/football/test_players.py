# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sportmonks import Sportmonks, AsyncSportmonks
from tests.utils import assert_matches_type
from sportmonks.pagination import SyncPaginatedAPICall, AsyncPaginatedAPICall
from sportmonks.types.football import (
    Player,
    PlayerLatestResponse,
    PlayerSearchResponse,
    PlayerRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPlayers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Sportmonks) -> None:
        player = client.football.players.retrieve(
            player_id="14",
            version="v3",
            sport="football",
        )
        assert_matches_type(PlayerRetrieveResponse, player, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Sportmonks) -> None:
        response = client.football.players.with_raw_response.retrieve(
            player_id="14",
            version="v3",
            sport="football",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        player = response.parse()
        assert_matches_type(PlayerRetrieveResponse, player, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Sportmonks) -> None:
        with client.football.players.with_streaming_response.retrieve(
            player_id="14",
            version="v3",
            sport="football",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            player = response.parse()
            assert_matches_type(PlayerRetrieveResponse, player, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Sportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.football.players.with_raw_response.retrieve(
                player_id="14",
                version="",
                sport="football",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            client.football.players.with_raw_response.retrieve(
                player_id="14",
                version="v3",
                sport="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `player_id` but received ''"):
            client.football.players.with_raw_response.retrieve(
                player_id="",
                version="v3",
                sport="football",
            )

    @parametrize
    def test_method_list(self, client: Sportmonks) -> None:
        player = client.football.players.list(
            sport="football",
            version="v3",
        )
        assert_matches_type(SyncPaginatedAPICall[Player], player, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Sportmonks) -> None:
        player = client.football.players.list(
            sport="football",
            version="v3",
            order="asc",
            page=1,
            per_page=25,
        )
        assert_matches_type(SyncPaginatedAPICall[Player], player, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Sportmonks) -> None:
        response = client.football.players.with_raw_response.list(
            sport="football",
            version="v3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        player = response.parse()
        assert_matches_type(SyncPaginatedAPICall[Player], player, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Sportmonks) -> None:
        with client.football.players.with_streaming_response.list(
            sport="football",
            version="v3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            player = response.parse()
            assert_matches_type(SyncPaginatedAPICall[Player], player, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Sportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.football.players.with_raw_response.list(
                sport="football",
                version="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            client.football.players.with_raw_response.list(
                sport="",
                version="v3",
            )

    @parametrize
    def test_method_latest(self, client: Sportmonks) -> None:
        player = client.football.players.latest(
            sport="football",
            version="v3",
        )
        assert_matches_type(PlayerLatestResponse, player, path=["response"])

    @parametrize
    def test_raw_response_latest(self, client: Sportmonks) -> None:
        response = client.football.players.with_raw_response.latest(
            sport="football",
            version="v3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        player = response.parse()
        assert_matches_type(PlayerLatestResponse, player, path=["response"])

    @parametrize
    def test_streaming_response_latest(self, client: Sportmonks) -> None:
        with client.football.players.with_streaming_response.latest(
            sport="football",
            version="v3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            player = response.parse()
            assert_matches_type(PlayerLatestResponse, player, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_latest(self, client: Sportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.football.players.with_raw_response.latest(
                sport="football",
                version="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            client.football.players.with_raw_response.latest(
                sport="",
                version="v3",
            )

    @parametrize
    def test_method_list_by_country(self, client: Sportmonks) -> None:
        player = client.football.players.list_by_country(
            country_id="320",
            version="v3",
            sport="football",
        )
        assert_matches_type(SyncPaginatedAPICall[Player], player, path=["response"])

    @parametrize
    def test_method_list_by_country_with_all_params(self, client: Sportmonks) -> None:
        player = client.football.players.list_by_country(
            country_id="320",
            version="v3",
            sport="football",
            order="asc",
            page=1,
            per_page=25,
        )
        assert_matches_type(SyncPaginatedAPICall[Player], player, path=["response"])

    @parametrize
    def test_raw_response_list_by_country(self, client: Sportmonks) -> None:
        response = client.football.players.with_raw_response.list_by_country(
            country_id="320",
            version="v3",
            sport="football",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        player = response.parse()
        assert_matches_type(SyncPaginatedAPICall[Player], player, path=["response"])

    @parametrize
    def test_streaming_response_list_by_country(self, client: Sportmonks) -> None:
        with client.football.players.with_streaming_response.list_by_country(
            country_id="320",
            version="v3",
            sport="football",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            player = response.parse()
            assert_matches_type(SyncPaginatedAPICall[Player], player, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_by_country(self, client: Sportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.football.players.with_raw_response.list_by_country(
                country_id="320",
                version="",
                sport="football",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            client.football.players.with_raw_response.list_by_country(
                country_id="320",
                version="v3",
                sport="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `country_id` but received ''"):
            client.football.players.with_raw_response.list_by_country(
                country_id="",
                version="v3",
                sport="football",
            )

    @parametrize
    def test_method_search(self, client: Sportmonks) -> None:
        player = client.football.players.search(
            name="Agg",
            version="v3",
            sport="football",
        )
        assert_matches_type(PlayerSearchResponse, player, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Sportmonks) -> None:
        response = client.football.players.with_raw_response.search(
            name="Agg",
            version="v3",
            sport="football",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        player = response.parse()
        assert_matches_type(PlayerSearchResponse, player, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Sportmonks) -> None:
        with client.football.players.with_streaming_response.search(
            name="Agg",
            version="v3",
            sport="football",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            player = response.parse()
            assert_matches_type(PlayerSearchResponse, player, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_search(self, client: Sportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.football.players.with_raw_response.search(
                name="Agg",
                version="",
                sport="football",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            client.football.players.with_raw_response.search(
                name="Agg",
                version="v3",
                sport="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.football.players.with_raw_response.search(
                name="",
                version="v3",
                sport="football",
            )


class TestAsyncPlayers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSportmonks) -> None:
        player = await async_client.football.players.retrieve(
            player_id="14",
            version="v3",
            sport="football",
        )
        assert_matches_type(PlayerRetrieveResponse, player, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSportmonks) -> None:
        response = await async_client.football.players.with_raw_response.retrieve(
            player_id="14",
            version="v3",
            sport="football",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        player = await response.parse()
        assert_matches_type(PlayerRetrieveResponse, player, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSportmonks) -> None:
        async with async_client.football.players.with_streaming_response.retrieve(
            player_id="14",
            version="v3",
            sport="football",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            player = await response.parse()
            assert_matches_type(PlayerRetrieveResponse, player, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.football.players.with_raw_response.retrieve(
                player_id="14",
                version="",
                sport="football",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            await async_client.football.players.with_raw_response.retrieve(
                player_id="14",
                version="v3",
                sport="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `player_id` but received ''"):
            await async_client.football.players.with_raw_response.retrieve(
                player_id="",
                version="v3",
                sport="football",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSportmonks) -> None:
        player = await async_client.football.players.list(
            sport="football",
            version="v3",
        )
        assert_matches_type(AsyncPaginatedAPICall[Player], player, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSportmonks) -> None:
        player = await async_client.football.players.list(
            sport="football",
            version="v3",
            order="asc",
            page=1,
            per_page=25,
        )
        assert_matches_type(AsyncPaginatedAPICall[Player], player, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSportmonks) -> None:
        response = await async_client.football.players.with_raw_response.list(
            sport="football",
            version="v3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        player = await response.parse()
        assert_matches_type(AsyncPaginatedAPICall[Player], player, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSportmonks) -> None:
        async with async_client.football.players.with_streaming_response.list(
            sport="football",
            version="v3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            player = await response.parse()
            assert_matches_type(AsyncPaginatedAPICall[Player], player, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncSportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.football.players.with_raw_response.list(
                sport="football",
                version="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            await async_client.football.players.with_raw_response.list(
                sport="",
                version="v3",
            )

    @parametrize
    async def test_method_latest(self, async_client: AsyncSportmonks) -> None:
        player = await async_client.football.players.latest(
            sport="football",
            version="v3",
        )
        assert_matches_type(PlayerLatestResponse, player, path=["response"])

    @parametrize
    async def test_raw_response_latest(self, async_client: AsyncSportmonks) -> None:
        response = await async_client.football.players.with_raw_response.latest(
            sport="football",
            version="v3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        player = await response.parse()
        assert_matches_type(PlayerLatestResponse, player, path=["response"])

    @parametrize
    async def test_streaming_response_latest(self, async_client: AsyncSportmonks) -> None:
        async with async_client.football.players.with_streaming_response.latest(
            sport="football",
            version="v3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            player = await response.parse()
            assert_matches_type(PlayerLatestResponse, player, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_latest(self, async_client: AsyncSportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.football.players.with_raw_response.latest(
                sport="football",
                version="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            await async_client.football.players.with_raw_response.latest(
                sport="",
                version="v3",
            )

    @parametrize
    async def test_method_list_by_country(self, async_client: AsyncSportmonks) -> None:
        player = await async_client.football.players.list_by_country(
            country_id="320",
            version="v3",
            sport="football",
        )
        assert_matches_type(AsyncPaginatedAPICall[Player], player, path=["response"])

    @parametrize
    async def test_method_list_by_country_with_all_params(self, async_client: AsyncSportmonks) -> None:
        player = await async_client.football.players.list_by_country(
            country_id="320",
            version="v3",
            sport="football",
            order="asc",
            page=1,
            per_page=25,
        )
        assert_matches_type(AsyncPaginatedAPICall[Player], player, path=["response"])

    @parametrize
    async def test_raw_response_list_by_country(self, async_client: AsyncSportmonks) -> None:
        response = await async_client.football.players.with_raw_response.list_by_country(
            country_id="320",
            version="v3",
            sport="football",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        player = await response.parse()
        assert_matches_type(AsyncPaginatedAPICall[Player], player, path=["response"])

    @parametrize
    async def test_streaming_response_list_by_country(self, async_client: AsyncSportmonks) -> None:
        async with async_client.football.players.with_streaming_response.list_by_country(
            country_id="320",
            version="v3",
            sport="football",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            player = await response.parse()
            assert_matches_type(AsyncPaginatedAPICall[Player], player, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_by_country(self, async_client: AsyncSportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.football.players.with_raw_response.list_by_country(
                country_id="320",
                version="",
                sport="football",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            await async_client.football.players.with_raw_response.list_by_country(
                country_id="320",
                version="v3",
                sport="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `country_id` but received ''"):
            await async_client.football.players.with_raw_response.list_by_country(
                country_id="",
                version="v3",
                sport="football",
            )

    @parametrize
    async def test_method_search(self, async_client: AsyncSportmonks) -> None:
        player = await async_client.football.players.search(
            name="Agg",
            version="v3",
            sport="football",
        )
        assert_matches_type(PlayerSearchResponse, player, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncSportmonks) -> None:
        response = await async_client.football.players.with_raw_response.search(
            name="Agg",
            version="v3",
            sport="football",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        player = await response.parse()
        assert_matches_type(PlayerSearchResponse, player, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncSportmonks) -> None:
        async with async_client.football.players.with_streaming_response.search(
            name="Agg",
            version="v3",
            sport="football",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            player = await response.parse()
            assert_matches_type(PlayerSearchResponse, player, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_search(self, async_client: AsyncSportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.football.players.with_raw_response.search(
                name="Agg",
                version="",
                sport="football",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            await async_client.football.players.with_raw_response.search(
                name="Agg",
                version="v3",
                sport="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.football.players.with_raw_response.search(
                name="",
                version="v3",
                sport="football",
            )
