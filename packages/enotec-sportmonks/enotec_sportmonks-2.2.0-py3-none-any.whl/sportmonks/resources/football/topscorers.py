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
from ...types.football import topscorer_list_by_season_params
from ...types.football.topscorer_list_by_season_response import TopscorerListBySeasonResponse

__all__ = ["TopscorersResource", "AsyncTopscorersResource"]


class TopscorersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TopscorersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return TopscorersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TopscorersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#with_streaming_response
        """
        return TopscorersResourceWithStreamingResponse(self)

    def list_by_season(
        self,
        season_id: str,
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
    ) -> SyncPaginatedAPICall[TopscorerListBySeasonResponse]:
        """
        By Season ID

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
        if not season_id:
            raise ValueError(f"Expected a non-empty value for `season_id` but received {season_id!r}")
        return self._get_api_list(
            f"/{version}/{sport}/topscorers/seasons/{season_id}",
            page=SyncPaginatedAPICall[TopscorerListBySeasonResponse],
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
                    topscorer_list_by_season_params.TopscorerListBySeasonParams,
                ),
            ),
            model=TopscorerListBySeasonResponse,
        )


class AsyncTopscorersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTopscorersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTopscorersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTopscorersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#with_streaming_response
        """
        return AsyncTopscorersResourceWithStreamingResponse(self)

    def list_by_season(
        self,
        season_id: str,
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
    ) -> AsyncPaginator[TopscorerListBySeasonResponse, AsyncPaginatedAPICall[TopscorerListBySeasonResponse]]:
        """
        By Season ID

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
        if not season_id:
            raise ValueError(f"Expected a non-empty value for `season_id` but received {season_id!r}")
        return self._get_api_list(
            f"/{version}/{sport}/topscorers/seasons/{season_id}",
            page=AsyncPaginatedAPICall[TopscorerListBySeasonResponse],
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
                    topscorer_list_by_season_params.TopscorerListBySeasonParams,
                ),
            ),
            model=TopscorerListBySeasonResponse,
        )


class TopscorersResourceWithRawResponse:
    def __init__(self, topscorers: TopscorersResource) -> None:
        self._topscorers = topscorers

        self.list_by_season = to_raw_response_wrapper(
            topscorers.list_by_season,
        )


class AsyncTopscorersResourceWithRawResponse:
    def __init__(self, topscorers: AsyncTopscorersResource) -> None:
        self._topscorers = topscorers

        self.list_by_season = async_to_raw_response_wrapper(
            topscorers.list_by_season,
        )


class TopscorersResourceWithStreamingResponse:
    def __init__(self, topscorers: TopscorersResource) -> None:
        self._topscorers = topscorers

        self.list_by_season = to_streamed_response_wrapper(
            topscorers.list_by_season,
        )


class AsyncTopscorersResourceWithStreamingResponse:
    def __init__(self, topscorers: AsyncTopscorersResource) -> None:
        self._topscorers = topscorers

        self.list_by_season = async_to_streamed_response_wrapper(
            topscorers.list_by_season,
        )
