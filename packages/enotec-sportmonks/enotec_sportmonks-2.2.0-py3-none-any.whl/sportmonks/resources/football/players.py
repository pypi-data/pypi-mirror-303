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
from ...types.football import player_list_params, player_list_by_country_params
from ...types.football.player import Player
from ...types.football.player_latest_response import PlayerLatestResponse
from ...types.football.player_search_response import PlayerSearchResponse
from ...types.football.player_retrieve_response import PlayerRetrieveResponse

__all__ = ["PlayersResource", "AsyncPlayersResource"]


class PlayersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PlayersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PlayersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PlayersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#with_streaming_response
        """
        return PlayersResourceWithStreamingResponse(self)

    def retrieve(
        self,
        player_id: str,
        *,
        version: str,
        sport: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PlayerRetrieveResponse:
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
        if not player_id:
            raise ValueError(f"Expected a non-empty value for `player_id` but received {player_id!r}")
        return self._get(
            f"/{version}/{sport}/players/{player_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlayerRetrieveResponse,
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
    ) -> SyncPaginatedAPICall[Player]:
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
            f"/{version}/{sport}/players",
            page=SyncPaginatedAPICall[Player],
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
                    player_list_params.PlayerListParams,
                ),
            ),
            model=Player,
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
    ) -> PlayerLatestResponse:
        """
        Latest Updated

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
            f"/{version}/{sport}/players/latest",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlayerLatestResponse,
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
    ) -> SyncPaginatedAPICall[Player]:
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
            f"/{version}/{sport}/players/countries/{country_id}",
            page=SyncPaginatedAPICall[Player],
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
                    player_list_by_country_params.PlayerListByCountryParams,
                ),
            ),
            model=Player,
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
    ) -> PlayerSearchResponse:
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
            f"/{version}/{sport}/players/search/{name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlayerSearchResponse,
        )


class AsyncPlayersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPlayersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPlayersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPlayersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#with_streaming_response
        """
        return AsyncPlayersResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        player_id: str,
        *,
        version: str,
        sport: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PlayerRetrieveResponse:
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
        if not player_id:
            raise ValueError(f"Expected a non-empty value for `player_id` but received {player_id!r}")
        return await self._get(
            f"/{version}/{sport}/players/{player_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlayerRetrieveResponse,
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
    ) -> AsyncPaginator[Player, AsyncPaginatedAPICall[Player]]:
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
            f"/{version}/{sport}/players",
            page=AsyncPaginatedAPICall[Player],
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
                    player_list_params.PlayerListParams,
                ),
            ),
            model=Player,
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
    ) -> PlayerLatestResponse:
        """
        Latest Updated

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
            f"/{version}/{sport}/players/latest",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlayerLatestResponse,
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
    ) -> AsyncPaginator[Player, AsyncPaginatedAPICall[Player]]:
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
            f"/{version}/{sport}/players/countries/{country_id}",
            page=AsyncPaginatedAPICall[Player],
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
                    player_list_by_country_params.PlayerListByCountryParams,
                ),
            ),
            model=Player,
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
    ) -> PlayerSearchResponse:
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
            f"/{version}/{sport}/players/search/{name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlayerSearchResponse,
        )


class PlayersResourceWithRawResponse:
    def __init__(self, players: PlayersResource) -> None:
        self._players = players

        self.retrieve = to_raw_response_wrapper(
            players.retrieve,
        )
        self.list = to_raw_response_wrapper(
            players.list,
        )
        self.latest = to_raw_response_wrapper(
            players.latest,
        )
        self.list_by_country = to_raw_response_wrapper(
            players.list_by_country,
        )
        self.search = to_raw_response_wrapper(
            players.search,
        )


class AsyncPlayersResourceWithRawResponse:
    def __init__(self, players: AsyncPlayersResource) -> None:
        self._players = players

        self.retrieve = async_to_raw_response_wrapper(
            players.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            players.list,
        )
        self.latest = async_to_raw_response_wrapper(
            players.latest,
        )
        self.list_by_country = async_to_raw_response_wrapper(
            players.list_by_country,
        )
        self.search = async_to_raw_response_wrapper(
            players.search,
        )


class PlayersResourceWithStreamingResponse:
    def __init__(self, players: PlayersResource) -> None:
        self._players = players

        self.retrieve = to_streamed_response_wrapper(
            players.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            players.list,
        )
        self.latest = to_streamed_response_wrapper(
            players.latest,
        )
        self.list_by_country = to_streamed_response_wrapper(
            players.list_by_country,
        )
        self.search = to_streamed_response_wrapper(
            players.search,
        )


class AsyncPlayersResourceWithStreamingResponse:
    def __init__(self, players: AsyncPlayersResource) -> None:
        self._players = players

        self.retrieve = async_to_streamed_response_wrapper(
            players.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            players.list,
        )
        self.latest = async_to_streamed_response_wrapper(
            players.latest,
        )
        self.list_by_country = async_to_streamed_response_wrapper(
            players.list_by_country,
        )
        self.search = async_to_streamed_response_wrapper(
            players.search,
        )
