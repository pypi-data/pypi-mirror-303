# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.football.standings.live_list_by_league_response import LiveListByLeagueResponse

__all__ = ["LiveResource", "AsyncLiveResource"]


class LiveResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LiveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return LiveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LiveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#with_streaming_response
        """
        return LiveResourceWithStreamingResponse(self)

    def list_by_league(
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
    ) -> LiveListByLeagueResponse:
        """
        By League ID

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
            f"/{version}/{sport}/standings/live/leagues/{league_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveListByLeagueResponse,
        )


class AsyncLiveResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLiveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLiveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLiveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#with_streaming_response
        """
        return AsyncLiveResourceWithStreamingResponse(self)

    async def list_by_league(
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
    ) -> LiveListByLeagueResponse:
        """
        By League ID

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
            f"/{version}/{sport}/standings/live/leagues/{league_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveListByLeagueResponse,
        )


class LiveResourceWithRawResponse:
    def __init__(self, live: LiveResource) -> None:
        self._live = live

        self.list_by_league = to_raw_response_wrapper(
            live.list_by_league,
        )


class AsyncLiveResourceWithRawResponse:
    def __init__(self, live: AsyncLiveResource) -> None:
        self._live = live

        self.list_by_league = async_to_raw_response_wrapper(
            live.list_by_league,
        )


class LiveResourceWithStreamingResponse:
    def __init__(self, live: LiveResource) -> None:
        self._live = live

        self.list_by_league = to_streamed_response_wrapper(
            live.list_by_league,
        )


class AsyncLiveResourceWithStreamingResponse:
    def __init__(self, live: AsyncLiveResource) -> None:
        self._live = live

        self.list_by_league = async_to_streamed_response_wrapper(
            live.list_by_league,
        )
