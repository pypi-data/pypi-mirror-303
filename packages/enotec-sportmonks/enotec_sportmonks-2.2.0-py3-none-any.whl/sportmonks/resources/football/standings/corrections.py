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
from ....types.football.standings.correction_list_by_season_response import CorrectionListBySeasonResponse

__all__ = ["CorrectionsResource", "AsyncCorrectionsResource"]


class CorrectionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CorrectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CorrectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CorrectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#with_streaming_response
        """
        return CorrectionsResourceWithStreamingResponse(self)

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
    ) -> CorrectionListBySeasonResponse:
        """
        Correction by Season ID

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
            f"/{version}/{sport}/standings/corrections/seasons/{season_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CorrectionListBySeasonResponse,
        )


class AsyncCorrectionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCorrectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCorrectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCorrectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#with_streaming_response
        """
        return AsyncCorrectionsResourceWithStreamingResponse(self)

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
    ) -> CorrectionListBySeasonResponse:
        """
        Correction by Season ID

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
            f"/{version}/{sport}/standings/corrections/seasons/{season_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CorrectionListBySeasonResponse,
        )


class CorrectionsResourceWithRawResponse:
    def __init__(self, corrections: CorrectionsResource) -> None:
        self._corrections = corrections

        self.list_by_season = to_raw_response_wrapper(
            corrections.list_by_season,
        )


class AsyncCorrectionsResourceWithRawResponse:
    def __init__(self, corrections: AsyncCorrectionsResource) -> None:
        self._corrections = corrections

        self.list_by_season = async_to_raw_response_wrapper(
            corrections.list_by_season,
        )


class CorrectionsResourceWithStreamingResponse:
    def __init__(self, corrections: CorrectionsResource) -> None:
        self._corrections = corrections

        self.list_by_season = to_streamed_response_wrapper(
            corrections.list_by_season,
        )


class AsyncCorrectionsResourceWithStreamingResponse:
    def __init__(self, corrections: AsyncCorrectionsResource) -> None:
        self._corrections = corrections

        self.list_by_season = async_to_streamed_response_wrapper(
            corrections.list_by_season,
        )
