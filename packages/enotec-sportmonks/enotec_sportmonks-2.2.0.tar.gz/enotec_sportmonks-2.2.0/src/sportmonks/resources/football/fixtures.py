# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncPaginatedAPICall, AsyncPaginatedAPICall
from ..._base_client import AsyncPaginator, make_request_options
from ...types.football import (
    fixture_list_params,
    fixture_head_to_head_params,
    fixture_list_by_date_params,
    fixture_list_between_dates_params,
    fixture_list_between_dates_for_team_params,
)
from ...types.football.fixture import Fixture
from ...types.football.fixture_latest_response import FixtureLatestResponse
from ...types.football.fixture_search_response import FixtureSearchResponse
from ...types.football.fixture_retrieve_response import FixtureRetrieveResponse
from ...types.football.fixture_list_by_ids_response import FixtureListByIDsResponse
from ...types.football.fixture_head_to_head_response import FixtureHeadToHeadResponse

__all__ = ["FixturesResource", "AsyncFixturesResource"]


class FixturesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FixturesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FixturesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FixturesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#with_streaming_response
        """
        return FixturesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        fixture_id: str,
        *,
        version: str,
        sport: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FixtureRetrieveResponse:
        """
        Fixture ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        if not sport:
            raise ValueError(f"Expected a non-empty value for `sport` but received {sport!r}")
        if not fixture_id:
            raise ValueError(f"Expected a non-empty value for `fixture_id` but received {fixture_id!r}")
        return self._get(
            f"/{version}/{sport}/fixtures/{fixture_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FixtureRetrieveResponse,
        )

    def list(
        self,
        sport: str,
        *,
        version: str,
        order: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPaginatedAPICall[Fixture]:
        """
        All

        Args:
          order: The order you want to retrieve the items in

          page: The page number you want to retrieve

          per_page: The number of items per page you want to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        if not sport:
            raise ValueError(f"Expected a non-empty value for `sport` but received {sport!r}")
        return self._get_api_list(
            f"/{version}/{sport}/fixtures",
            page=SyncPaginatedAPICall[Fixture],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    fixture_list_params.FixtureListParams,
                ),
            ),
            model=Fixture,
        )

    def head_to_head(
        self,
        second_team: str,
        *,
        version: str,
        sport: str,
        first_team: str,
        order: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FixtureHeadToHeadResponse:
        """
        Head to Head

        Args:
          order: The order you want to retrieve the items in

          page: The page number you want to retrieve

          per_page: The number of items per page you want to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        if not sport:
            raise ValueError(f"Expected a non-empty value for `sport` but received {sport!r}")
        if not first_team:
            raise ValueError(f"Expected a non-empty value for `first_team` but received {first_team!r}")
        if not second_team:
            raise ValueError(f"Expected a non-empty value for `second_team` but received {second_team!r}")
        return self._get(
            f"/{version}/{sport}/fixtures/head-to-head/{first_team}/{second_team}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    fixture_head_to_head_params.FixtureHeadToHeadParams,
                ),
            ),
            cast_to=FixtureHeadToHeadResponse,
        )

    def latest(
        self,
        sport: str,
        *,
        version: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FixtureLatestResponse:
        """
        Last Updated

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        if not sport:
            raise ValueError(f"Expected a non-empty value for `sport` but received {sport!r}")
        return self._get(
            f"/{version}/{sport}/fixtures/latest",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FixtureLatestResponse,
        )

    def list_between_dates(
        self,
        end_date: str,
        *,
        version: str,
        sport: str,
        start_date: str,
        order: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPaginatedAPICall[Fixture]:
        """
        By Date Range

        Args:
          order: The order you want to retrieve the items in

          page: The page number you want to retrieve

          per_page: The number of items per page you want to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        if not sport:
            raise ValueError(f"Expected a non-empty value for `sport` but received {sport!r}")
        if not start_date:
            raise ValueError(f"Expected a non-empty value for `start_date` but received {start_date!r}")
        if not end_date:
            raise ValueError(f"Expected a non-empty value for `end_date` but received {end_date!r}")
        return self._get_api_list(
            f"/{version}/{sport}/fixtures/between/{start_date}/{end_date}",
            page=SyncPaginatedAPICall[Fixture],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    fixture_list_between_dates_params.FixtureListBetweenDatesParams,
                ),
            ),
            model=Fixture,
        )

    def list_between_dates_for_team(
        self,
        team_id: str,
        *,
        version: str,
        sport: str,
        start_date: str,
        end_date: str,
        order: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPaginatedAPICall[Fixture]:
        """
        By Date Range for Team

        Args:
          order: The order you want to retrieve the items in

          page: The page number you want to retrieve

          per_page: The number of items per page you want to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        if not sport:
            raise ValueError(f"Expected a non-empty value for `sport` but received {sport!r}")
        if not start_date:
            raise ValueError(f"Expected a non-empty value for `start_date` but received {start_date!r}")
        if not end_date:
            raise ValueError(f"Expected a non-empty value for `end_date` but received {end_date!r}")
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        return self._get_api_list(
            f"/{version}/{sport}/fixtures/between/{start_date}/{end_date}/{team_id}",
            page=SyncPaginatedAPICall[Fixture],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    fixture_list_between_dates_for_team_params.FixtureListBetweenDatesForTeamParams,
                ),
            ),
            model=Fixture,
        )

    def list_by_date(
        self,
        date: str,
        *,
        version: str,
        sport: str,
        order: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPaginatedAPICall[Fixture]:
        """
        By Date

        Args:
          order: The order you want to retrieve the items in

          page: The page number you want to retrieve

          per_page: The number of items per page you want to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        if not sport:
            raise ValueError(f"Expected a non-empty value for `sport` but received {sport!r}")
        if not date:
            raise ValueError(f"Expected a non-empty value for `date` but received {date!r}")
        return self._get_api_list(
            f"/{version}/{sport}/fixtures/date/{date}",
            page=SyncPaginatedAPICall[Fixture],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    fixture_list_by_date_params.FixtureListByDateParams,
                ),
            ),
            model=Fixture,
        )

    def list_by_ids(
        self,
        fixture_ids: str,
        *,
        version: str,
        sport: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FixtureListByIDsResponse:
        """
        By IDs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        if not sport:
            raise ValueError(f"Expected a non-empty value for `sport` but received {sport!r}")
        if not fixture_ids:
            raise ValueError(f"Expected a non-empty value for `fixture_ids` but received {fixture_ids!r}")
        return self._get(
            f"/{version}/{sport}/fixtures/multi/{fixture_ids}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FixtureListByIDsResponse,
        )

    def search(
        self,
        name: str,
        *,
        version: str,
        sport: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FixtureSearchResponse:
        """
        Search

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        if not sport:
            raise ValueError(f"Expected a non-empty value for `sport` but received {sport!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            f"/{version}/{sport}/fixtures/search/{name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FixtureSearchResponse,
        )


class AsyncFixturesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFixturesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFixturesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFixturesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#with_streaming_response
        """
        return AsyncFixturesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        fixture_id: str,
        *,
        version: str,
        sport: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FixtureRetrieveResponse:
        """
        Fixture ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        if not sport:
            raise ValueError(f"Expected a non-empty value for `sport` but received {sport!r}")
        if not fixture_id:
            raise ValueError(f"Expected a non-empty value for `fixture_id` but received {fixture_id!r}")
        return await self._get(
            f"/{version}/{sport}/fixtures/{fixture_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FixtureRetrieveResponse,
        )

    def list(
        self,
        sport: str,
        *,
        version: str,
        order: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Fixture, AsyncPaginatedAPICall[Fixture]]:
        """
        All

        Args:
          order: The order you want to retrieve the items in

          page: The page number you want to retrieve

          per_page: The number of items per page you want to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        if not sport:
            raise ValueError(f"Expected a non-empty value for `sport` but received {sport!r}")
        return self._get_api_list(
            f"/{version}/{sport}/fixtures",
            page=AsyncPaginatedAPICall[Fixture],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    fixture_list_params.FixtureListParams,
                ),
            ),
            model=Fixture,
        )

    async def head_to_head(
        self,
        second_team: str,
        *,
        version: str,
        sport: str,
        first_team: str,
        order: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FixtureHeadToHeadResponse:
        """
        Head to Head

        Args:
          order: The order you want to retrieve the items in

          page: The page number you want to retrieve

          per_page: The number of items per page you want to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        if not sport:
            raise ValueError(f"Expected a non-empty value for `sport` but received {sport!r}")
        if not first_team:
            raise ValueError(f"Expected a non-empty value for `first_team` but received {first_team!r}")
        if not second_team:
            raise ValueError(f"Expected a non-empty value for `second_team` but received {second_team!r}")
        return await self._get(
            f"/{version}/{sport}/fixtures/head-to-head/{first_team}/{second_team}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    fixture_head_to_head_params.FixtureHeadToHeadParams,
                ),
            ),
            cast_to=FixtureHeadToHeadResponse,
        )

    async def latest(
        self,
        sport: str,
        *,
        version: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FixtureLatestResponse:
        """
        Last Updated

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        if not sport:
            raise ValueError(f"Expected a non-empty value for `sport` but received {sport!r}")
        return await self._get(
            f"/{version}/{sport}/fixtures/latest",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FixtureLatestResponse,
        )

    def list_between_dates(
        self,
        end_date: str,
        *,
        version: str,
        sport: str,
        start_date: str,
        order: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Fixture, AsyncPaginatedAPICall[Fixture]]:
        """
        By Date Range

        Args:
          order: The order you want to retrieve the items in

          page: The page number you want to retrieve

          per_page: The number of items per page you want to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        if not sport:
            raise ValueError(f"Expected a non-empty value for `sport` but received {sport!r}")
        if not start_date:
            raise ValueError(f"Expected a non-empty value for `start_date` but received {start_date!r}")
        if not end_date:
            raise ValueError(f"Expected a non-empty value for `end_date` but received {end_date!r}")
        return self._get_api_list(
            f"/{version}/{sport}/fixtures/between/{start_date}/{end_date}",
            page=AsyncPaginatedAPICall[Fixture],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    fixture_list_between_dates_params.FixtureListBetweenDatesParams,
                ),
            ),
            model=Fixture,
        )

    def list_between_dates_for_team(
        self,
        team_id: str,
        *,
        version: str,
        sport: str,
        start_date: str,
        end_date: str,
        order: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Fixture, AsyncPaginatedAPICall[Fixture]]:
        """
        By Date Range for Team

        Args:
          order: The order you want to retrieve the items in

          page: The page number you want to retrieve

          per_page: The number of items per page you want to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        if not sport:
            raise ValueError(f"Expected a non-empty value for `sport` but received {sport!r}")
        if not start_date:
            raise ValueError(f"Expected a non-empty value for `start_date` but received {start_date!r}")
        if not end_date:
            raise ValueError(f"Expected a non-empty value for `end_date` but received {end_date!r}")
        if not team_id:
            raise ValueError(f"Expected a non-empty value for `team_id` but received {team_id!r}")
        return self._get_api_list(
            f"/{version}/{sport}/fixtures/between/{start_date}/{end_date}/{team_id}",
            page=AsyncPaginatedAPICall[Fixture],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    fixture_list_between_dates_for_team_params.FixtureListBetweenDatesForTeamParams,
                ),
            ),
            model=Fixture,
        )

    def list_by_date(
        self,
        date: str,
        *,
        version: str,
        sport: str,
        order: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Fixture, AsyncPaginatedAPICall[Fixture]]:
        """
        By Date

        Args:
          order: The order you want to retrieve the items in

          page: The page number you want to retrieve

          per_page: The number of items per page you want to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        if not sport:
            raise ValueError(f"Expected a non-empty value for `sport` but received {sport!r}")
        if not date:
            raise ValueError(f"Expected a non-empty value for `date` but received {date!r}")
        return self._get_api_list(
            f"/{version}/{sport}/fixtures/date/{date}",
            page=AsyncPaginatedAPICall[Fixture],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    fixture_list_by_date_params.FixtureListByDateParams,
                ),
            ),
            model=Fixture,
        )

    async def list_by_ids(
        self,
        fixture_ids: str,
        *,
        version: str,
        sport: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FixtureListByIDsResponse:
        """
        By IDs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        if not sport:
            raise ValueError(f"Expected a non-empty value for `sport` but received {sport!r}")
        if not fixture_ids:
            raise ValueError(f"Expected a non-empty value for `fixture_ids` but received {fixture_ids!r}")
        return await self._get(
            f"/{version}/{sport}/fixtures/multi/{fixture_ids}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FixtureListByIDsResponse,
        )

    async def search(
        self,
        name: str,
        *,
        version: str,
        sport: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FixtureSearchResponse:
        """
        Search

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        if not sport:
            raise ValueError(f"Expected a non-empty value for `sport` but received {sport!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            f"/{version}/{sport}/fixtures/search/{name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FixtureSearchResponse,
        )


class FixturesResourceWithRawResponse:
    def __init__(self, fixtures: FixturesResource) -> None:
        self._fixtures = fixtures

        self.retrieve = to_raw_response_wrapper(
            fixtures.retrieve,
        )
        self.list = to_raw_response_wrapper(
            fixtures.list,
        )
        self.head_to_head = to_raw_response_wrapper(
            fixtures.head_to_head,
        )
        self.latest = to_raw_response_wrapper(
            fixtures.latest,
        )
        self.list_between_dates = to_raw_response_wrapper(
            fixtures.list_between_dates,
        )
        self.list_between_dates_for_team = to_raw_response_wrapper(
            fixtures.list_between_dates_for_team,
        )
        self.list_by_date = to_raw_response_wrapper(
            fixtures.list_by_date,
        )
        self.list_by_ids = to_raw_response_wrapper(
            fixtures.list_by_ids,
        )
        self.search = to_raw_response_wrapper(
            fixtures.search,
        )


class AsyncFixturesResourceWithRawResponse:
    def __init__(self, fixtures: AsyncFixturesResource) -> None:
        self._fixtures = fixtures

        self.retrieve = async_to_raw_response_wrapper(
            fixtures.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            fixtures.list,
        )
        self.head_to_head = async_to_raw_response_wrapper(
            fixtures.head_to_head,
        )
        self.latest = async_to_raw_response_wrapper(
            fixtures.latest,
        )
        self.list_between_dates = async_to_raw_response_wrapper(
            fixtures.list_between_dates,
        )
        self.list_between_dates_for_team = async_to_raw_response_wrapper(
            fixtures.list_between_dates_for_team,
        )
        self.list_by_date = async_to_raw_response_wrapper(
            fixtures.list_by_date,
        )
        self.list_by_ids = async_to_raw_response_wrapper(
            fixtures.list_by_ids,
        )
        self.search = async_to_raw_response_wrapper(
            fixtures.search,
        )


class FixturesResourceWithStreamingResponse:
    def __init__(self, fixtures: FixturesResource) -> None:
        self._fixtures = fixtures

        self.retrieve = to_streamed_response_wrapper(
            fixtures.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            fixtures.list,
        )
        self.head_to_head = to_streamed_response_wrapper(
            fixtures.head_to_head,
        )
        self.latest = to_streamed_response_wrapper(
            fixtures.latest,
        )
        self.list_between_dates = to_streamed_response_wrapper(
            fixtures.list_between_dates,
        )
        self.list_between_dates_for_team = to_streamed_response_wrapper(
            fixtures.list_between_dates_for_team,
        )
        self.list_by_date = to_streamed_response_wrapper(
            fixtures.list_by_date,
        )
        self.list_by_ids = to_streamed_response_wrapper(
            fixtures.list_by_ids,
        )
        self.search = to_streamed_response_wrapper(
            fixtures.search,
        )


class AsyncFixturesResourceWithStreamingResponse:
    def __init__(self, fixtures: AsyncFixturesResource) -> None:
        self._fixtures = fixtures

        self.retrieve = async_to_streamed_response_wrapper(
            fixtures.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            fixtures.list,
        )
        self.head_to_head = async_to_streamed_response_wrapper(
            fixtures.head_to_head,
        )
        self.latest = async_to_streamed_response_wrapper(
            fixtures.latest,
        )
        self.list_between_dates = async_to_streamed_response_wrapper(
            fixtures.list_between_dates,
        )
        self.list_between_dates_for_team = async_to_streamed_response_wrapper(
            fixtures.list_between_dates_for_team,
        )
        self.list_by_date = async_to_streamed_response_wrapper(
            fixtures.list_by_date,
        )
        self.list_by_ids = async_to_streamed_response_wrapper(
            fixtures.list_by_ids,
        )
        self.search = async_to_streamed_response_wrapper(
            fixtures.search,
        )
