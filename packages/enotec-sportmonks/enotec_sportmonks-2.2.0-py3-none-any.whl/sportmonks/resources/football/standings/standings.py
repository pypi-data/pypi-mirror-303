# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .live import (
    LiveResource,
    AsyncLiveResource,
    LiveResourceWithRawResponse,
    AsyncLiveResourceWithRawResponse,
    LiveResourceWithStreamingResponse,
    AsyncLiveResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from .corrections import (
    CorrectionsResource,
    AsyncCorrectionsResource,
    CorrectionsResourceWithRawResponse,
    AsyncCorrectionsResourceWithRawResponse,
    CorrectionsResourceWithStreamingResponse,
    AsyncCorrectionsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncPaginatedAPICall, AsyncPaginatedAPICall
from ...._base_client import AsyncPaginator, make_request_options
from ....types.football import standing_list_params
from ....types.football.standing_list_response import StandingListResponse
from ....types.football.standing_list_by_season_response import StandingListBySeasonResponse

__all__ = ["StandingsResource", "AsyncStandingsResource"]


class StandingsResource(SyncAPIResource):
    @cached_property
    def corrections(self) -> CorrectionsResource:
        return CorrectionsResource(self._client)

    @cached_property
    def live(self) -> LiveResource:
        return LiveResource(self._client)

    @cached_property
    def with_raw_response(self) -> StandingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return StandingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StandingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#with_streaming_response
        """
        return StandingsResourceWithStreamingResponse(self)

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
    ) -> SyncPaginatedAPICall[StandingListResponse]:
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
            f"/{version}/{sport}/standings",
            page=SyncPaginatedAPICall[StandingListResponse],
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
                    standing_list_params.StandingListParams,
                ),
            ),
            model=StandingListResponse,
        )

    def list_by_season(
        self,
        season_id: str,
        *,
        version: str,
        sport: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StandingListBySeasonResponse:
        """
        By Season ID

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
        if not season_id:
            raise ValueError(f"Expected a non-empty value for `season_id` but received {season_id!r}")
        return self._get(
            f"/{version}/{sport}/standings/seasons/{season_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StandingListBySeasonResponse,
        )


class AsyncStandingsResource(AsyncAPIResource):
    @cached_property
    def corrections(self) -> AsyncCorrectionsResource:
        return AsyncCorrectionsResource(self._client)

    @cached_property
    def live(self) -> AsyncLiveResource:
        return AsyncLiveResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncStandingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStandingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStandingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#with_streaming_response
        """
        return AsyncStandingsResourceWithStreamingResponse(self)

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
    ) -> AsyncPaginator[StandingListResponse, AsyncPaginatedAPICall[StandingListResponse]]:
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
            f"/{version}/{sport}/standings",
            page=AsyncPaginatedAPICall[StandingListResponse],
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
                    standing_list_params.StandingListParams,
                ),
            ),
            model=StandingListResponse,
        )

    async def list_by_season(
        self,
        season_id: str,
        *,
        version: str,
        sport: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StandingListBySeasonResponse:
        """
        By Season ID

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
        if not season_id:
            raise ValueError(f"Expected a non-empty value for `season_id` but received {season_id!r}")
        return await self._get(
            f"/{version}/{sport}/standings/seasons/{season_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StandingListBySeasonResponse,
        )


class StandingsResourceWithRawResponse:
    def __init__(self, standings: StandingsResource) -> None:
        self._standings = standings

        self.list = to_raw_response_wrapper(
            standings.list,
        )
        self.list_by_season = to_raw_response_wrapper(
            standings.list_by_season,
        )

    @cached_property
    def corrections(self) -> CorrectionsResourceWithRawResponse:
        return CorrectionsResourceWithRawResponse(self._standings.corrections)

    @cached_property
    def live(self) -> LiveResourceWithRawResponse:
        return LiveResourceWithRawResponse(self._standings.live)


class AsyncStandingsResourceWithRawResponse:
    def __init__(self, standings: AsyncStandingsResource) -> None:
        self._standings = standings

        self.list = async_to_raw_response_wrapper(
            standings.list,
        )
        self.list_by_season = async_to_raw_response_wrapper(
            standings.list_by_season,
        )

    @cached_property
    def corrections(self) -> AsyncCorrectionsResourceWithRawResponse:
        return AsyncCorrectionsResourceWithRawResponse(self._standings.corrections)

    @cached_property
    def live(self) -> AsyncLiveResourceWithRawResponse:
        return AsyncLiveResourceWithRawResponse(self._standings.live)


class StandingsResourceWithStreamingResponse:
    def __init__(self, standings: StandingsResource) -> None:
        self._standings = standings

        self.list = to_streamed_response_wrapper(
            standings.list,
        )
        self.list_by_season = to_streamed_response_wrapper(
            standings.list_by_season,
        )

    @cached_property
    def corrections(self) -> CorrectionsResourceWithStreamingResponse:
        return CorrectionsResourceWithStreamingResponse(self._standings.corrections)

    @cached_property
    def live(self) -> LiveResourceWithStreamingResponse:
        return LiveResourceWithStreamingResponse(self._standings.live)


class AsyncStandingsResourceWithStreamingResponse:
    def __init__(self, standings: AsyncStandingsResource) -> None:
        self._standings = standings

        self.list = async_to_streamed_response_wrapper(
            standings.list,
        )
        self.list_by_season = async_to_streamed_response_wrapper(
            standings.list_by_season,
        )

    @cached_property
    def corrections(self) -> AsyncCorrectionsResourceWithStreamingResponse:
        return AsyncCorrectionsResourceWithStreamingResponse(self._standings.corrections)

    @cached_property
    def live(self) -> AsyncLiveResourceWithStreamingResponse:
        return AsyncLiveResourceWithStreamingResponse(self._standings.live)
