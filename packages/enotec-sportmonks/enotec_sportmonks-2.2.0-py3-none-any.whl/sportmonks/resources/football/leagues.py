# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
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
from ...types.football import league_list_params, league_list_by_date_params, league_list_by_country_params
from ...types.football.league import League
from ...types.football.league_live_response import LeagueLiveResponse
from ...types.football.league_search_response import LeagueSearchResponse
from ...types.football.league_retrieve_response import LeagueRetrieveResponse

__all__ = ["LeaguesResource", "AsyncLeaguesResource"]


class LeaguesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LeaguesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return LeaguesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LeaguesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#with_streaming_response
        """
        return LeaguesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        league_id: str,
        *,
        version: str,
        sport: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LeagueRetrieveResponse:
        """
        By ID

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
        if not league_id:
            raise ValueError(f"Expected a non-empty value for `league_id` but received {league_id!r}")
        return self._get(
            f"/{version}/{sport}/leagues/{league_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LeagueRetrieveResponse,
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
    ) -> SyncPaginatedAPICall[League]:
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
            f"/{version}/{sport}/leagues",
            page=SyncPaginatedAPICall[League],
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
                    league_list_params.LeagueListParams,
                ),
            ),
            model=League,
        )

    def list_by_country(
        self,
        country_id: str,
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
    ) -> SyncPaginatedAPICall[League]:
        """
        By Country ID

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
        if not country_id:
            raise ValueError(f"Expected a non-empty value for `country_id` but received {country_id!r}")
        return self._get_api_list(
            f"/{version}/{sport}/leagues/countries/{country_id}",
            page=SyncPaginatedAPICall[League],
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
                    league_list_by_country_params.LeagueListByCountryParams,
                ),
            ),
            model=League,
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
    ) -> SyncPaginatedAPICall[League]:
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
            f"/{version}/{sport}/leagues/date/{date}",
            page=SyncPaginatedAPICall[League],
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
                    league_list_by_date_params.LeagueListByDateParams,
                ),
            ),
            model=League,
        )

    def live(
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
    ) -> LeagueLiveResponse:
        """
        Live

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
            f"/{version}/{sport}/leagues/live",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LeagueLiveResponse,
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
    ) -> LeagueSearchResponse:
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
            f"/{version}/{sport}/leagues/search/{name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LeagueSearchResponse,
        )


class AsyncLeaguesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLeaguesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLeaguesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLeaguesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#with_streaming_response
        """
        return AsyncLeaguesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        league_id: str,
        *,
        version: str,
        sport: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LeagueRetrieveResponse:
        """
        By ID

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
        if not league_id:
            raise ValueError(f"Expected a non-empty value for `league_id` but received {league_id!r}")
        return await self._get(
            f"/{version}/{sport}/leagues/{league_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LeagueRetrieveResponse,
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
    ) -> AsyncPaginator[League, AsyncPaginatedAPICall[League]]:
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
            f"/{version}/{sport}/leagues",
            page=AsyncPaginatedAPICall[League],
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
                    league_list_params.LeagueListParams,
                ),
            ),
            model=League,
        )

    def list_by_country(
        self,
        country_id: str,
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
    ) -> AsyncPaginator[League, AsyncPaginatedAPICall[League]]:
        """
        By Country ID

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
        if not country_id:
            raise ValueError(f"Expected a non-empty value for `country_id` but received {country_id!r}")
        return self._get_api_list(
            f"/{version}/{sport}/leagues/countries/{country_id}",
            page=AsyncPaginatedAPICall[League],
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
                    league_list_by_country_params.LeagueListByCountryParams,
                ),
            ),
            model=League,
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
    ) -> AsyncPaginator[League, AsyncPaginatedAPICall[League]]:
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
            f"/{version}/{sport}/leagues/date/{date}",
            page=AsyncPaginatedAPICall[League],
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
                    league_list_by_date_params.LeagueListByDateParams,
                ),
            ),
            model=League,
        )

    async def live(
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
    ) -> LeagueLiveResponse:
        """
        Live

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
            f"/{version}/{sport}/leagues/live",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LeagueLiveResponse,
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
    ) -> LeagueSearchResponse:
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
            f"/{version}/{sport}/leagues/search/{name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LeagueSearchResponse,
        )


class LeaguesResourceWithRawResponse:
    def __init__(self, leagues: LeaguesResource) -> None:
        self._leagues = leagues

        self.retrieve = to_raw_response_wrapper(
            leagues.retrieve,
        )
        self.list = to_raw_response_wrapper(
            leagues.list,
        )
        self.list_by_country = to_raw_response_wrapper(
            leagues.list_by_country,
        )
        self.list_by_date = to_raw_response_wrapper(
            leagues.list_by_date,
        )
        self.live = to_raw_response_wrapper(
            leagues.live,
        )
        self.search = to_raw_response_wrapper(
            leagues.search,
        )


class AsyncLeaguesResourceWithRawResponse:
    def __init__(self, leagues: AsyncLeaguesResource) -> None:
        self._leagues = leagues

        self.retrieve = async_to_raw_response_wrapper(
            leagues.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            leagues.list,
        )
        self.list_by_country = async_to_raw_response_wrapper(
            leagues.list_by_country,
        )
        self.list_by_date = async_to_raw_response_wrapper(
            leagues.list_by_date,
        )
        self.live = async_to_raw_response_wrapper(
            leagues.live,
        )
        self.search = async_to_raw_response_wrapper(
            leagues.search,
        )


class LeaguesResourceWithStreamingResponse:
    def __init__(self, leagues: LeaguesResource) -> None:
        self._leagues = leagues

        self.retrieve = to_streamed_response_wrapper(
            leagues.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            leagues.list,
        )
        self.list_by_country = to_streamed_response_wrapper(
            leagues.list_by_country,
        )
        self.list_by_date = to_streamed_response_wrapper(
            leagues.list_by_date,
        )
        self.live = to_streamed_response_wrapper(
            leagues.live,
        )
        self.search = to_streamed_response_wrapper(
            leagues.search,
        )


class AsyncLeaguesResourceWithStreamingResponse:
    def __init__(self, leagues: AsyncLeaguesResource) -> None:
        self._leagues = leagues

        self.retrieve = async_to_streamed_response_wrapper(
            leagues.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            leagues.list,
        )
        self.list_by_country = async_to_streamed_response_wrapper(
            leagues.list_by_country,
        )
        self.list_by_date = async_to_streamed_response_wrapper(
            leagues.list_by_date,
        )
        self.live = async_to_streamed_response_wrapper(
            leagues.live,
        )
        self.search = async_to_streamed_response_wrapper(
            leagues.search,
        )
