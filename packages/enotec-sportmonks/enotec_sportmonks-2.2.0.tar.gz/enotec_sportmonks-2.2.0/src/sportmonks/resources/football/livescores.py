# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.football.livescore_list_response import LivescoreListResponse
from ...types.football.livescore_inplay_response import LivescoreInplayResponse
from ...types.football.livescore_latest_response import LivescoreLatestResponse

__all__ = ["LivescoresResource", "AsyncLivescoresResource"]


class LivescoresResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LivescoresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return LivescoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LivescoresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#with_streaming_response
        """
        return LivescoresResourceWithStreamingResponse(self)

    def list(
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
    ) -> LivescoreListResponse:
        """
        All

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
            f"/{version}/{sport}/livescores",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LivescoreListResponse,
        )

    def inplay(
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
    ) -> LivescoreInplayResponse:
        """
        All In-play

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
            f"/{version}/{sport}/livescores/inplay",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LivescoreInplayResponse,
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
    ) -> LivescoreLatestResponse:
        """
        Last Updated In-play

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
            f"/{version}/{sport}/livescores/latest",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LivescoreLatestResponse,
        )


class AsyncLivescoresResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLivescoresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLivescoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLivescoresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#with_streaming_response
        """
        return AsyncLivescoresResourceWithStreamingResponse(self)

    async def list(
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
    ) -> LivescoreListResponse:
        """
        All

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
            f"/{version}/{sport}/livescores",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LivescoreListResponse,
        )

    async def inplay(
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
    ) -> LivescoreInplayResponse:
        """
        All In-play

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
            f"/{version}/{sport}/livescores/inplay",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LivescoreInplayResponse,
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
    ) -> LivescoreLatestResponse:
        """
        Last Updated In-play

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
            f"/{version}/{sport}/livescores/latest",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LivescoreLatestResponse,
        )


class LivescoresResourceWithRawResponse:
    def __init__(self, livescores: LivescoresResource) -> None:
        self._livescores = livescores

        self.list = to_raw_response_wrapper(
            livescores.list,
        )
        self.inplay = to_raw_response_wrapper(
            livescores.inplay,
        )
        self.latest = to_raw_response_wrapper(
            livescores.latest,
        )


class AsyncLivescoresResourceWithRawResponse:
    def __init__(self, livescores: AsyncLivescoresResource) -> None:
        self._livescores = livescores

        self.list = async_to_raw_response_wrapper(
            livescores.list,
        )
        self.inplay = async_to_raw_response_wrapper(
            livescores.inplay,
        )
        self.latest = async_to_raw_response_wrapper(
            livescores.latest,
        )


class LivescoresResourceWithStreamingResponse:
    def __init__(self, livescores: LivescoresResource) -> None:
        self._livescores = livescores

        self.list = to_streamed_response_wrapper(
            livescores.list,
        )
        self.inplay = to_streamed_response_wrapper(
            livescores.inplay,
        )
        self.latest = to_streamed_response_wrapper(
            livescores.latest,
        )


class AsyncLivescoresResourceWithStreamingResponse:
    def __init__(self, livescores: AsyncLivescoresResource) -> None:
        self._livescores = livescores

        self.list = async_to_streamed_response_wrapper(
            livescores.list,
        )
        self.inplay = async_to_streamed_response_wrapper(
            livescores.inplay,
        )
        self.latest = async_to_streamed_response_wrapper(
            livescores.latest,
        )
