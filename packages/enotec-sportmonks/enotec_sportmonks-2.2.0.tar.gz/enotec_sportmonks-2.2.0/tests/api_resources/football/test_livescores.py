# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sportmonks import Sportmonks, AsyncSportmonks
from tests.utils import assert_matches_type
from sportmonks.types.football import LivescoreListResponse, LivescoreInplayResponse, LivescoreLatestResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLivescores:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Sportmonks) -> None:
        livescore = client.football.livescores.list(
            sport="football",
            version="v3",
        )
        assert_matches_type(LivescoreListResponse, livescore, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Sportmonks) -> None:
        response = client.football.livescores.with_raw_response.list(
            sport="football",
            version="v3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        livescore = response.parse()
        assert_matches_type(LivescoreListResponse, livescore, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Sportmonks) -> None:
        with client.football.livescores.with_streaming_response.list(
            sport="football",
            version="v3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            livescore = response.parse()
            assert_matches_type(LivescoreListResponse, livescore, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Sportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.football.livescores.with_raw_response.list(
                sport="football",
                version="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            client.football.livescores.with_raw_response.list(
                sport="",
                version="v3",
            )

    @parametrize
    def test_method_inplay(self, client: Sportmonks) -> None:
        livescore = client.football.livescores.inplay(
            sport="football",
            version="v3",
        )
        assert_matches_type(LivescoreInplayResponse, livescore, path=["response"])

    @parametrize
    def test_raw_response_inplay(self, client: Sportmonks) -> None:
        response = client.football.livescores.with_raw_response.inplay(
            sport="football",
            version="v3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        livescore = response.parse()
        assert_matches_type(LivescoreInplayResponse, livescore, path=["response"])

    @parametrize
    def test_streaming_response_inplay(self, client: Sportmonks) -> None:
        with client.football.livescores.with_streaming_response.inplay(
            sport="football",
            version="v3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            livescore = response.parse()
            assert_matches_type(LivescoreInplayResponse, livescore, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_inplay(self, client: Sportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.football.livescores.with_raw_response.inplay(
                sport="football",
                version="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            client.football.livescores.with_raw_response.inplay(
                sport="",
                version="v3",
            )

    @parametrize
    def test_method_latest(self, client: Sportmonks) -> None:
        livescore = client.football.livescores.latest(
            sport="football",
            version="v3",
        )
        assert_matches_type(LivescoreLatestResponse, livescore, path=["response"])

    @parametrize
    def test_raw_response_latest(self, client: Sportmonks) -> None:
        response = client.football.livescores.with_raw_response.latest(
            sport="football",
            version="v3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        livescore = response.parse()
        assert_matches_type(LivescoreLatestResponse, livescore, path=["response"])

    @parametrize
    def test_streaming_response_latest(self, client: Sportmonks) -> None:
        with client.football.livescores.with_streaming_response.latest(
            sport="football",
            version="v3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            livescore = response.parse()
            assert_matches_type(LivescoreLatestResponse, livescore, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_latest(self, client: Sportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.football.livescores.with_raw_response.latest(
                sport="football",
                version="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            client.football.livescores.with_raw_response.latest(
                sport="",
                version="v3",
            )


class TestAsyncLivescores:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncSportmonks) -> None:
        livescore = await async_client.football.livescores.list(
            sport="football",
            version="v3",
        )
        assert_matches_type(LivescoreListResponse, livescore, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSportmonks) -> None:
        response = await async_client.football.livescores.with_raw_response.list(
            sport="football",
            version="v3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        livescore = await response.parse()
        assert_matches_type(LivescoreListResponse, livescore, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSportmonks) -> None:
        async with async_client.football.livescores.with_streaming_response.list(
            sport="football",
            version="v3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            livescore = await response.parse()
            assert_matches_type(LivescoreListResponse, livescore, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncSportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.football.livescores.with_raw_response.list(
                sport="football",
                version="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            await async_client.football.livescores.with_raw_response.list(
                sport="",
                version="v3",
            )

    @parametrize
    async def test_method_inplay(self, async_client: AsyncSportmonks) -> None:
        livescore = await async_client.football.livescores.inplay(
            sport="football",
            version="v3",
        )
        assert_matches_type(LivescoreInplayResponse, livescore, path=["response"])

    @parametrize
    async def test_raw_response_inplay(self, async_client: AsyncSportmonks) -> None:
        response = await async_client.football.livescores.with_raw_response.inplay(
            sport="football",
            version="v3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        livescore = await response.parse()
        assert_matches_type(LivescoreInplayResponse, livescore, path=["response"])

    @parametrize
    async def test_streaming_response_inplay(self, async_client: AsyncSportmonks) -> None:
        async with async_client.football.livescores.with_streaming_response.inplay(
            sport="football",
            version="v3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            livescore = await response.parse()
            assert_matches_type(LivescoreInplayResponse, livescore, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_inplay(self, async_client: AsyncSportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.football.livescores.with_raw_response.inplay(
                sport="football",
                version="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            await async_client.football.livescores.with_raw_response.inplay(
                sport="",
                version="v3",
            )

    @parametrize
    async def test_method_latest(self, async_client: AsyncSportmonks) -> None:
        livescore = await async_client.football.livescores.latest(
            sport="football",
            version="v3",
        )
        assert_matches_type(LivescoreLatestResponse, livescore, path=["response"])

    @parametrize
    async def test_raw_response_latest(self, async_client: AsyncSportmonks) -> None:
        response = await async_client.football.livescores.with_raw_response.latest(
            sport="football",
            version="v3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        livescore = await response.parse()
        assert_matches_type(LivescoreLatestResponse, livescore, path=["response"])

    @parametrize
    async def test_streaming_response_latest(self, async_client: AsyncSportmonks) -> None:
        async with async_client.football.livescores.with_streaming_response.latest(
            sport="football",
            version="v3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            livescore = await response.parse()
            assert_matches_type(LivescoreLatestResponse, livescore, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_latest(self, async_client: AsyncSportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.football.livescores.with_raw_response.latest(
                sport="football",
                version="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            await async_client.football.livescores.with_raw_response.latest(
                sport="",
                version="v3",
            )
