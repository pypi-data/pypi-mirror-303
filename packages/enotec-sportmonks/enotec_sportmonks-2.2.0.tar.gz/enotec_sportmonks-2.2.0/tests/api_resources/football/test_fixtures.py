# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sportmonks import Sportmonks, AsyncSportmonks
from tests.utils import assert_matches_type
from sportmonks.pagination import SyncPaginatedAPICall, AsyncPaginatedAPICall
from sportmonks.types.football import (
    Fixture,
    FixtureLatestResponse,
    FixtureSearchResponse,
    FixtureRetrieveResponse,
    FixtureListByIDsResponse,
    FixtureHeadToHeadResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFixtures:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Sportmonks) -> None:
        fixture = client.football.fixtures.retrieve(
            fixture_id="18528480",
            version="v3",
            sport="football",
        )
        assert_matches_type(FixtureRetrieveResponse, fixture, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Sportmonks) -> None:
        response = client.football.fixtures.with_raw_response.retrieve(
            fixture_id="18528480",
            version="v3",
            sport="football",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fixture = response.parse()
        assert_matches_type(FixtureRetrieveResponse, fixture, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Sportmonks) -> None:
        with client.football.fixtures.with_streaming_response.retrieve(
            fixture_id="18528480",
            version="v3",
            sport="football",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fixture = response.parse()
            assert_matches_type(FixtureRetrieveResponse, fixture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Sportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.football.fixtures.with_raw_response.retrieve(
                fixture_id="18528480",
                version="",
                sport="football",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            client.football.fixtures.with_raw_response.retrieve(
                fixture_id="18528480",
                version="v3",
                sport="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fixture_id` but received ''"):
            client.football.fixtures.with_raw_response.retrieve(
                fixture_id="",
                version="v3",
                sport="football",
            )

    @parametrize
    def test_method_list(self, client: Sportmonks) -> None:
        fixture = client.football.fixtures.list(
            sport="football",
            version="v3",
        )
        assert_matches_type(SyncPaginatedAPICall[Fixture], fixture, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Sportmonks) -> None:
        fixture = client.football.fixtures.list(
            sport="football",
            version="v3",
            order="asc",
            page=1,
            per_page=25,
        )
        assert_matches_type(SyncPaginatedAPICall[Fixture], fixture, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Sportmonks) -> None:
        response = client.football.fixtures.with_raw_response.list(
            sport="football",
            version="v3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fixture = response.parse()
        assert_matches_type(SyncPaginatedAPICall[Fixture], fixture, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Sportmonks) -> None:
        with client.football.fixtures.with_streaming_response.list(
            sport="football",
            version="v3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fixture = response.parse()
            assert_matches_type(SyncPaginatedAPICall[Fixture], fixture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Sportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.football.fixtures.with_raw_response.list(
                sport="football",
                version="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            client.football.fixtures.with_raw_response.list(
                sport="",
                version="v3",
            )

    @parametrize
    def test_method_head_to_head(self, client: Sportmonks) -> None:
        fixture = client.football.fixtures.head_to_head(
            second_team="86",
            version="v3",
            sport="football",
            first_team="2650",
        )
        assert_matches_type(FixtureHeadToHeadResponse, fixture, path=["response"])

    @parametrize
    def test_method_head_to_head_with_all_params(self, client: Sportmonks) -> None:
        fixture = client.football.fixtures.head_to_head(
            second_team="86",
            version="v3",
            sport="football",
            first_team="2650",
            order="asc",
            page=1,
            per_page=25,
        )
        assert_matches_type(FixtureHeadToHeadResponse, fixture, path=["response"])

    @parametrize
    def test_raw_response_head_to_head(self, client: Sportmonks) -> None:
        response = client.football.fixtures.with_raw_response.head_to_head(
            second_team="86",
            version="v3",
            sport="football",
            first_team="2650",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fixture = response.parse()
        assert_matches_type(FixtureHeadToHeadResponse, fixture, path=["response"])

    @parametrize
    def test_streaming_response_head_to_head(self, client: Sportmonks) -> None:
        with client.football.fixtures.with_streaming_response.head_to_head(
            second_team="86",
            version="v3",
            sport="football",
            first_team="2650",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fixture = response.parse()
            assert_matches_type(FixtureHeadToHeadResponse, fixture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_head_to_head(self, client: Sportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.football.fixtures.with_raw_response.head_to_head(
                second_team="86",
                version="",
                sport="football",
                first_team="2650",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            client.football.fixtures.with_raw_response.head_to_head(
                second_team="86",
                version="v3",
                sport="",
                first_team="2650",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `first_team` but received ''"):
            client.football.fixtures.with_raw_response.head_to_head(
                second_team="86",
                version="v3",
                sport="football",
                first_team="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `second_team` but received ''"):
            client.football.fixtures.with_raw_response.head_to_head(
                second_team="",
                version="v3",
                sport="football",
                first_team="2650",
            )

    @parametrize
    def test_method_latest(self, client: Sportmonks) -> None:
        fixture = client.football.fixtures.latest(
            sport="football",
            version="v3",
        )
        assert_matches_type(FixtureLatestResponse, fixture, path=["response"])

    @parametrize
    def test_raw_response_latest(self, client: Sportmonks) -> None:
        response = client.football.fixtures.with_raw_response.latest(
            sport="football",
            version="v3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fixture = response.parse()
        assert_matches_type(FixtureLatestResponse, fixture, path=["response"])

    @parametrize
    def test_streaming_response_latest(self, client: Sportmonks) -> None:
        with client.football.fixtures.with_streaming_response.latest(
            sport="football",
            version="v3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fixture = response.parse()
            assert_matches_type(FixtureLatestResponse, fixture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_latest(self, client: Sportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.football.fixtures.with_raw_response.latest(
                sport="football",
                version="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            client.football.fixtures.with_raw_response.latest(
                sport="",
                version="v3",
            )

    @parametrize
    def test_method_list_between_dates(self, client: Sportmonks) -> None:
        fixture = client.football.fixtures.list_between_dates(
            end_date="2022-07-25",
            version="v3",
            sport="football",
            start_date="2022-07-17",
        )
        assert_matches_type(SyncPaginatedAPICall[Fixture], fixture, path=["response"])

    @parametrize
    def test_method_list_between_dates_with_all_params(self, client: Sportmonks) -> None:
        fixture = client.football.fixtures.list_between_dates(
            end_date="2022-07-25",
            version="v3",
            sport="football",
            start_date="2022-07-17",
            order="asc",
            page=1,
            per_page=25,
        )
        assert_matches_type(SyncPaginatedAPICall[Fixture], fixture, path=["response"])

    @parametrize
    def test_raw_response_list_between_dates(self, client: Sportmonks) -> None:
        response = client.football.fixtures.with_raw_response.list_between_dates(
            end_date="2022-07-25",
            version="v3",
            sport="football",
            start_date="2022-07-17",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fixture = response.parse()
        assert_matches_type(SyncPaginatedAPICall[Fixture], fixture, path=["response"])

    @parametrize
    def test_streaming_response_list_between_dates(self, client: Sportmonks) -> None:
        with client.football.fixtures.with_streaming_response.list_between_dates(
            end_date="2022-07-25",
            version="v3",
            sport="football",
            start_date="2022-07-17",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fixture = response.parse()
            assert_matches_type(SyncPaginatedAPICall[Fixture], fixture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_between_dates(self, client: Sportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.football.fixtures.with_raw_response.list_between_dates(
                end_date="2022-07-25",
                version="",
                sport="football",
                start_date="2022-07-17",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            client.football.fixtures.with_raw_response.list_between_dates(
                end_date="2022-07-25",
                version="v3",
                sport="",
                start_date="2022-07-17",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `start_date` but received ''"):
            client.football.fixtures.with_raw_response.list_between_dates(
                end_date="2022-07-25",
                version="v3",
                sport="football",
                start_date="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `end_date` but received ''"):
            client.football.fixtures.with_raw_response.list_between_dates(
                end_date="",
                version="v3",
                sport="football",
                start_date="2022-07-17",
            )

    @parametrize
    def test_method_list_between_dates_for_team(self, client: Sportmonks) -> None:
        fixture = client.football.fixtures.list_between_dates_for_team(
            team_id="ut",
            version="v3",
            sport="football",
            start_date="maiores",
            end_date="voluptates",
        )
        assert_matches_type(SyncPaginatedAPICall[Fixture], fixture, path=["response"])

    @parametrize
    def test_method_list_between_dates_for_team_with_all_params(self, client: Sportmonks) -> None:
        fixture = client.football.fixtures.list_between_dates_for_team(
            team_id="ut",
            version="v3",
            sport="football",
            start_date="maiores",
            end_date="voluptates",
            order="asc",
            page=1,
            per_page=25,
        )
        assert_matches_type(SyncPaginatedAPICall[Fixture], fixture, path=["response"])

    @parametrize
    def test_raw_response_list_between_dates_for_team(self, client: Sportmonks) -> None:
        response = client.football.fixtures.with_raw_response.list_between_dates_for_team(
            team_id="ut",
            version="v3",
            sport="football",
            start_date="maiores",
            end_date="voluptates",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fixture = response.parse()
        assert_matches_type(SyncPaginatedAPICall[Fixture], fixture, path=["response"])

    @parametrize
    def test_streaming_response_list_between_dates_for_team(self, client: Sportmonks) -> None:
        with client.football.fixtures.with_streaming_response.list_between_dates_for_team(
            team_id="ut",
            version="v3",
            sport="football",
            start_date="maiores",
            end_date="voluptates",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fixture = response.parse()
            assert_matches_type(SyncPaginatedAPICall[Fixture], fixture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_between_dates_for_team(self, client: Sportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.football.fixtures.with_raw_response.list_between_dates_for_team(
                team_id="ut",
                version="",
                sport="football",
                start_date="maiores",
                end_date="voluptates",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            client.football.fixtures.with_raw_response.list_between_dates_for_team(
                team_id="ut",
                version="v3",
                sport="",
                start_date="maiores",
                end_date="voluptates",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `start_date` but received ''"):
            client.football.fixtures.with_raw_response.list_between_dates_for_team(
                team_id="ut",
                version="v3",
                sport="football",
                start_date="",
                end_date="voluptates",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `end_date` but received ''"):
            client.football.fixtures.with_raw_response.list_between_dates_for_team(
                team_id="ut",
                version="v3",
                sport="football",
                start_date="maiores",
                end_date="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            client.football.fixtures.with_raw_response.list_between_dates_for_team(
                team_id="",
                version="v3",
                sport="football",
                start_date="maiores",
                end_date="voluptates",
            )

    @parametrize
    def test_method_list_by_date(self, client: Sportmonks) -> None:
        fixture = client.football.fixtures.list_by_date(
            date="2022-07-24",
            version="v3",
            sport="football",
        )
        assert_matches_type(SyncPaginatedAPICall[Fixture], fixture, path=["response"])

    @parametrize
    def test_method_list_by_date_with_all_params(self, client: Sportmonks) -> None:
        fixture = client.football.fixtures.list_by_date(
            date="2022-07-24",
            version="v3",
            sport="football",
            order="asc",
            page=1,
            per_page=25,
        )
        assert_matches_type(SyncPaginatedAPICall[Fixture], fixture, path=["response"])

    @parametrize
    def test_raw_response_list_by_date(self, client: Sportmonks) -> None:
        response = client.football.fixtures.with_raw_response.list_by_date(
            date="2022-07-24",
            version="v3",
            sport="football",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fixture = response.parse()
        assert_matches_type(SyncPaginatedAPICall[Fixture], fixture, path=["response"])

    @parametrize
    def test_streaming_response_list_by_date(self, client: Sportmonks) -> None:
        with client.football.fixtures.with_streaming_response.list_by_date(
            date="2022-07-24",
            version="v3",
            sport="football",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fixture = response.parse()
            assert_matches_type(SyncPaginatedAPICall[Fixture], fixture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_by_date(self, client: Sportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.football.fixtures.with_raw_response.list_by_date(
                date="2022-07-24",
                version="",
                sport="football",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            client.football.fixtures.with_raw_response.list_by_date(
                date="2022-07-24",
                version="v3",
                sport="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `date` but received ''"):
            client.football.fixtures.with_raw_response.list_by_date(
                date="",
                version="v3",
                sport="football",
            )

    @parametrize
    def test_method_list_by_ids(self, client: Sportmonks) -> None:
        fixture = client.football.fixtures.list_by_ids(
            fixture_ids="18528484%2C18531140",
            version="v3",
            sport="football",
        )
        assert_matches_type(FixtureListByIDsResponse, fixture, path=["response"])

    @parametrize
    def test_raw_response_list_by_ids(self, client: Sportmonks) -> None:
        response = client.football.fixtures.with_raw_response.list_by_ids(
            fixture_ids="18528484%2C18531140",
            version="v3",
            sport="football",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fixture = response.parse()
        assert_matches_type(FixtureListByIDsResponse, fixture, path=["response"])

    @parametrize
    def test_streaming_response_list_by_ids(self, client: Sportmonks) -> None:
        with client.football.fixtures.with_streaming_response.list_by_ids(
            fixture_ids="18528484%2C18531140",
            version="v3",
            sport="football",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fixture = response.parse()
            assert_matches_type(FixtureListByIDsResponse, fixture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_by_ids(self, client: Sportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.football.fixtures.with_raw_response.list_by_ids(
                fixture_ids="18528484%2C18531140",
                version="",
                sport="football",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            client.football.fixtures.with_raw_response.list_by_ids(
                fixture_ids="18528484%2C18531140",
                version="v3",
                sport="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fixture_ids` but received ''"):
            client.football.fixtures.with_raw_response.list_by_ids(
                fixture_ids="",
                version="v3",
                sport="football",
            )

    @parametrize
    def test_method_search(self, client: Sportmonks) -> None:
        fixture = client.football.fixtures.search(
            name="havn",
            version="v3",
            sport="football",
        )
        assert_matches_type(FixtureSearchResponse, fixture, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Sportmonks) -> None:
        response = client.football.fixtures.with_raw_response.search(
            name="havn",
            version="v3",
            sport="football",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fixture = response.parse()
        assert_matches_type(FixtureSearchResponse, fixture, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Sportmonks) -> None:
        with client.football.fixtures.with_streaming_response.search(
            name="havn",
            version="v3",
            sport="football",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fixture = response.parse()
            assert_matches_type(FixtureSearchResponse, fixture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_search(self, client: Sportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            client.football.fixtures.with_raw_response.search(
                name="havn",
                version="",
                sport="football",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            client.football.fixtures.with_raw_response.search(
                name="havn",
                version="v3",
                sport="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.football.fixtures.with_raw_response.search(
                name="",
                version="v3",
                sport="football",
            )


class TestAsyncFixtures:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSportmonks) -> None:
        fixture = await async_client.football.fixtures.retrieve(
            fixture_id="18528480",
            version="v3",
            sport="football",
        )
        assert_matches_type(FixtureRetrieveResponse, fixture, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSportmonks) -> None:
        response = await async_client.football.fixtures.with_raw_response.retrieve(
            fixture_id="18528480",
            version="v3",
            sport="football",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fixture = await response.parse()
        assert_matches_type(FixtureRetrieveResponse, fixture, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSportmonks) -> None:
        async with async_client.football.fixtures.with_streaming_response.retrieve(
            fixture_id="18528480",
            version="v3",
            sport="football",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fixture = await response.parse()
            assert_matches_type(FixtureRetrieveResponse, fixture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.football.fixtures.with_raw_response.retrieve(
                fixture_id="18528480",
                version="",
                sport="football",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            await async_client.football.fixtures.with_raw_response.retrieve(
                fixture_id="18528480",
                version="v3",
                sport="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fixture_id` but received ''"):
            await async_client.football.fixtures.with_raw_response.retrieve(
                fixture_id="",
                version="v3",
                sport="football",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSportmonks) -> None:
        fixture = await async_client.football.fixtures.list(
            sport="football",
            version="v3",
        )
        assert_matches_type(AsyncPaginatedAPICall[Fixture], fixture, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSportmonks) -> None:
        fixture = await async_client.football.fixtures.list(
            sport="football",
            version="v3",
            order="asc",
            page=1,
            per_page=25,
        )
        assert_matches_type(AsyncPaginatedAPICall[Fixture], fixture, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSportmonks) -> None:
        response = await async_client.football.fixtures.with_raw_response.list(
            sport="football",
            version="v3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fixture = await response.parse()
        assert_matches_type(AsyncPaginatedAPICall[Fixture], fixture, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSportmonks) -> None:
        async with async_client.football.fixtures.with_streaming_response.list(
            sport="football",
            version="v3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fixture = await response.parse()
            assert_matches_type(AsyncPaginatedAPICall[Fixture], fixture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncSportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.football.fixtures.with_raw_response.list(
                sport="football",
                version="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            await async_client.football.fixtures.with_raw_response.list(
                sport="",
                version="v3",
            )

    @parametrize
    async def test_method_head_to_head(self, async_client: AsyncSportmonks) -> None:
        fixture = await async_client.football.fixtures.head_to_head(
            second_team="86",
            version="v3",
            sport="football",
            first_team="2650",
        )
        assert_matches_type(FixtureHeadToHeadResponse, fixture, path=["response"])

    @parametrize
    async def test_method_head_to_head_with_all_params(self, async_client: AsyncSportmonks) -> None:
        fixture = await async_client.football.fixtures.head_to_head(
            second_team="86",
            version="v3",
            sport="football",
            first_team="2650",
            order="asc",
            page=1,
            per_page=25,
        )
        assert_matches_type(FixtureHeadToHeadResponse, fixture, path=["response"])

    @parametrize
    async def test_raw_response_head_to_head(self, async_client: AsyncSportmonks) -> None:
        response = await async_client.football.fixtures.with_raw_response.head_to_head(
            second_team="86",
            version="v3",
            sport="football",
            first_team="2650",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fixture = await response.parse()
        assert_matches_type(FixtureHeadToHeadResponse, fixture, path=["response"])

    @parametrize
    async def test_streaming_response_head_to_head(self, async_client: AsyncSportmonks) -> None:
        async with async_client.football.fixtures.with_streaming_response.head_to_head(
            second_team="86",
            version="v3",
            sport="football",
            first_team="2650",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fixture = await response.parse()
            assert_matches_type(FixtureHeadToHeadResponse, fixture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_head_to_head(self, async_client: AsyncSportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.football.fixtures.with_raw_response.head_to_head(
                second_team="86",
                version="",
                sport="football",
                first_team="2650",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            await async_client.football.fixtures.with_raw_response.head_to_head(
                second_team="86",
                version="v3",
                sport="",
                first_team="2650",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `first_team` but received ''"):
            await async_client.football.fixtures.with_raw_response.head_to_head(
                second_team="86",
                version="v3",
                sport="football",
                first_team="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `second_team` but received ''"):
            await async_client.football.fixtures.with_raw_response.head_to_head(
                second_team="",
                version="v3",
                sport="football",
                first_team="2650",
            )

    @parametrize
    async def test_method_latest(self, async_client: AsyncSportmonks) -> None:
        fixture = await async_client.football.fixtures.latest(
            sport="football",
            version="v3",
        )
        assert_matches_type(FixtureLatestResponse, fixture, path=["response"])

    @parametrize
    async def test_raw_response_latest(self, async_client: AsyncSportmonks) -> None:
        response = await async_client.football.fixtures.with_raw_response.latest(
            sport="football",
            version="v3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fixture = await response.parse()
        assert_matches_type(FixtureLatestResponse, fixture, path=["response"])

    @parametrize
    async def test_streaming_response_latest(self, async_client: AsyncSportmonks) -> None:
        async with async_client.football.fixtures.with_streaming_response.latest(
            sport="football",
            version="v3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fixture = await response.parse()
            assert_matches_type(FixtureLatestResponse, fixture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_latest(self, async_client: AsyncSportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.football.fixtures.with_raw_response.latest(
                sport="football",
                version="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            await async_client.football.fixtures.with_raw_response.latest(
                sport="",
                version="v3",
            )

    @parametrize
    async def test_method_list_between_dates(self, async_client: AsyncSportmonks) -> None:
        fixture = await async_client.football.fixtures.list_between_dates(
            end_date="2022-07-25",
            version="v3",
            sport="football",
            start_date="2022-07-17",
        )
        assert_matches_type(AsyncPaginatedAPICall[Fixture], fixture, path=["response"])

    @parametrize
    async def test_method_list_between_dates_with_all_params(self, async_client: AsyncSportmonks) -> None:
        fixture = await async_client.football.fixtures.list_between_dates(
            end_date="2022-07-25",
            version="v3",
            sport="football",
            start_date="2022-07-17",
            order="asc",
            page=1,
            per_page=25,
        )
        assert_matches_type(AsyncPaginatedAPICall[Fixture], fixture, path=["response"])

    @parametrize
    async def test_raw_response_list_between_dates(self, async_client: AsyncSportmonks) -> None:
        response = await async_client.football.fixtures.with_raw_response.list_between_dates(
            end_date="2022-07-25",
            version="v3",
            sport="football",
            start_date="2022-07-17",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fixture = await response.parse()
        assert_matches_type(AsyncPaginatedAPICall[Fixture], fixture, path=["response"])

    @parametrize
    async def test_streaming_response_list_between_dates(self, async_client: AsyncSportmonks) -> None:
        async with async_client.football.fixtures.with_streaming_response.list_between_dates(
            end_date="2022-07-25",
            version="v3",
            sport="football",
            start_date="2022-07-17",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fixture = await response.parse()
            assert_matches_type(AsyncPaginatedAPICall[Fixture], fixture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_between_dates(self, async_client: AsyncSportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.football.fixtures.with_raw_response.list_between_dates(
                end_date="2022-07-25",
                version="",
                sport="football",
                start_date="2022-07-17",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            await async_client.football.fixtures.with_raw_response.list_between_dates(
                end_date="2022-07-25",
                version="v3",
                sport="",
                start_date="2022-07-17",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `start_date` but received ''"):
            await async_client.football.fixtures.with_raw_response.list_between_dates(
                end_date="2022-07-25",
                version="v3",
                sport="football",
                start_date="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `end_date` but received ''"):
            await async_client.football.fixtures.with_raw_response.list_between_dates(
                end_date="",
                version="v3",
                sport="football",
                start_date="2022-07-17",
            )

    @parametrize
    async def test_method_list_between_dates_for_team(self, async_client: AsyncSportmonks) -> None:
        fixture = await async_client.football.fixtures.list_between_dates_for_team(
            team_id="ut",
            version="v3",
            sport="football",
            start_date="maiores",
            end_date="voluptates",
        )
        assert_matches_type(AsyncPaginatedAPICall[Fixture], fixture, path=["response"])

    @parametrize
    async def test_method_list_between_dates_for_team_with_all_params(self, async_client: AsyncSportmonks) -> None:
        fixture = await async_client.football.fixtures.list_between_dates_for_team(
            team_id="ut",
            version="v3",
            sport="football",
            start_date="maiores",
            end_date="voluptates",
            order="asc",
            page=1,
            per_page=25,
        )
        assert_matches_type(AsyncPaginatedAPICall[Fixture], fixture, path=["response"])

    @parametrize
    async def test_raw_response_list_between_dates_for_team(self, async_client: AsyncSportmonks) -> None:
        response = await async_client.football.fixtures.with_raw_response.list_between_dates_for_team(
            team_id="ut",
            version="v3",
            sport="football",
            start_date="maiores",
            end_date="voluptates",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fixture = await response.parse()
        assert_matches_type(AsyncPaginatedAPICall[Fixture], fixture, path=["response"])

    @parametrize
    async def test_streaming_response_list_between_dates_for_team(self, async_client: AsyncSportmonks) -> None:
        async with async_client.football.fixtures.with_streaming_response.list_between_dates_for_team(
            team_id="ut",
            version="v3",
            sport="football",
            start_date="maiores",
            end_date="voluptates",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fixture = await response.parse()
            assert_matches_type(AsyncPaginatedAPICall[Fixture], fixture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_between_dates_for_team(self, async_client: AsyncSportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.football.fixtures.with_raw_response.list_between_dates_for_team(
                team_id="ut",
                version="",
                sport="football",
                start_date="maiores",
                end_date="voluptates",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            await async_client.football.fixtures.with_raw_response.list_between_dates_for_team(
                team_id="ut",
                version="v3",
                sport="",
                start_date="maiores",
                end_date="voluptates",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `start_date` but received ''"):
            await async_client.football.fixtures.with_raw_response.list_between_dates_for_team(
                team_id="ut",
                version="v3",
                sport="football",
                start_date="",
                end_date="voluptates",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `end_date` but received ''"):
            await async_client.football.fixtures.with_raw_response.list_between_dates_for_team(
                team_id="ut",
                version="v3",
                sport="football",
                start_date="maiores",
                end_date="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            await async_client.football.fixtures.with_raw_response.list_between_dates_for_team(
                team_id="",
                version="v3",
                sport="football",
                start_date="maiores",
                end_date="voluptates",
            )

    @parametrize
    async def test_method_list_by_date(self, async_client: AsyncSportmonks) -> None:
        fixture = await async_client.football.fixtures.list_by_date(
            date="2022-07-24",
            version="v3",
            sport="football",
        )
        assert_matches_type(AsyncPaginatedAPICall[Fixture], fixture, path=["response"])

    @parametrize
    async def test_method_list_by_date_with_all_params(self, async_client: AsyncSportmonks) -> None:
        fixture = await async_client.football.fixtures.list_by_date(
            date="2022-07-24",
            version="v3",
            sport="football",
            order="asc",
            page=1,
            per_page=25,
        )
        assert_matches_type(AsyncPaginatedAPICall[Fixture], fixture, path=["response"])

    @parametrize
    async def test_raw_response_list_by_date(self, async_client: AsyncSportmonks) -> None:
        response = await async_client.football.fixtures.with_raw_response.list_by_date(
            date="2022-07-24",
            version="v3",
            sport="football",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fixture = await response.parse()
        assert_matches_type(AsyncPaginatedAPICall[Fixture], fixture, path=["response"])

    @parametrize
    async def test_streaming_response_list_by_date(self, async_client: AsyncSportmonks) -> None:
        async with async_client.football.fixtures.with_streaming_response.list_by_date(
            date="2022-07-24",
            version="v3",
            sport="football",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fixture = await response.parse()
            assert_matches_type(AsyncPaginatedAPICall[Fixture], fixture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_by_date(self, async_client: AsyncSportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.football.fixtures.with_raw_response.list_by_date(
                date="2022-07-24",
                version="",
                sport="football",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            await async_client.football.fixtures.with_raw_response.list_by_date(
                date="2022-07-24",
                version="v3",
                sport="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `date` but received ''"):
            await async_client.football.fixtures.with_raw_response.list_by_date(
                date="",
                version="v3",
                sport="football",
            )

    @parametrize
    async def test_method_list_by_ids(self, async_client: AsyncSportmonks) -> None:
        fixture = await async_client.football.fixtures.list_by_ids(
            fixture_ids="18528484%2C18531140",
            version="v3",
            sport="football",
        )
        assert_matches_type(FixtureListByIDsResponse, fixture, path=["response"])

    @parametrize
    async def test_raw_response_list_by_ids(self, async_client: AsyncSportmonks) -> None:
        response = await async_client.football.fixtures.with_raw_response.list_by_ids(
            fixture_ids="18528484%2C18531140",
            version="v3",
            sport="football",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fixture = await response.parse()
        assert_matches_type(FixtureListByIDsResponse, fixture, path=["response"])

    @parametrize
    async def test_streaming_response_list_by_ids(self, async_client: AsyncSportmonks) -> None:
        async with async_client.football.fixtures.with_streaming_response.list_by_ids(
            fixture_ids="18528484%2C18531140",
            version="v3",
            sport="football",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fixture = await response.parse()
            assert_matches_type(FixtureListByIDsResponse, fixture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_by_ids(self, async_client: AsyncSportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.football.fixtures.with_raw_response.list_by_ids(
                fixture_ids="18528484%2C18531140",
                version="",
                sport="football",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            await async_client.football.fixtures.with_raw_response.list_by_ids(
                fixture_ids="18528484%2C18531140",
                version="v3",
                sport="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fixture_ids` but received ''"):
            await async_client.football.fixtures.with_raw_response.list_by_ids(
                fixture_ids="",
                version="v3",
                sport="football",
            )

    @parametrize
    async def test_method_search(self, async_client: AsyncSportmonks) -> None:
        fixture = await async_client.football.fixtures.search(
            name="havn",
            version="v3",
            sport="football",
        )
        assert_matches_type(FixtureSearchResponse, fixture, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncSportmonks) -> None:
        response = await async_client.football.fixtures.with_raw_response.search(
            name="havn",
            version="v3",
            sport="football",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fixture = await response.parse()
        assert_matches_type(FixtureSearchResponse, fixture, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncSportmonks) -> None:
        async with async_client.football.fixtures.with_streaming_response.search(
            name="havn",
            version="v3",
            sport="football",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fixture = await response.parse()
            assert_matches_type(FixtureSearchResponse, fixture, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_search(self, async_client: AsyncSportmonks) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version` but received ''"):
            await async_client.football.fixtures.with_raw_response.search(
                name="havn",
                version="",
                sport="football",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sport` but received ''"):
            await async_client.football.fixtures.with_raw_response.search(
                name="havn",
                version="v3",
                sport="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.football.fixtures.with_raw_response.search(
                name="",
                version="v3",
                sport="football",
            )
