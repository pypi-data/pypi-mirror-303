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
from ...types.core import timezone_list_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.core.timezone_list_response import TimezoneListResponse

__all__ = ["TimezonesResource", "AsyncTimezonesResource"]


class TimezonesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TimezonesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return TimezonesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TimezonesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#with_streaming_response
        """
        return TimezonesResourceWithStreamingResponse(self)

    def list(
        self,
        version: str,
        *,
        order: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPaginatedAPICall[TimezoneListResponse]:
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
        return self._get_api_list(
            f"/{version}/core/timezones",
            page=SyncPaginatedAPICall[TimezoneListResponse],
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
                    timezone_list_params.TimezoneListParams,
                ),
            ),
            model=str,
        )


class AsyncTimezonesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTimezonesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTimezonesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTimezonesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#with_streaming_response
        """
        return AsyncTimezonesResourceWithStreamingResponse(self)

    def list(
        self,
        version: str,
        *,
        order: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[TimezoneListResponse, AsyncPaginatedAPICall[TimezoneListResponse]]:
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
        return self._get_api_list(
            f"/{version}/core/timezones",
            page=AsyncPaginatedAPICall[TimezoneListResponse],
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
                    timezone_list_params.TimezoneListParams,
                ),
            ),
            model=str,
        )


class TimezonesResourceWithRawResponse:
    def __init__(self, timezones: TimezonesResource) -> None:
        self._timezones = timezones

        self.list = to_raw_response_wrapper(
            timezones.list,
        )


class AsyncTimezonesResourceWithRawResponse:
    def __init__(self, timezones: AsyncTimezonesResource) -> None:
        self._timezones = timezones

        self.list = async_to_raw_response_wrapper(
            timezones.list,
        )


class TimezonesResourceWithStreamingResponse:
    def __init__(self, timezones: TimezonesResource) -> None:
        self._timezones = timezones

        self.list = to_streamed_response_wrapper(
            timezones.list,
        )


class AsyncTimezonesResourceWithStreamingResponse:
    def __init__(self, timezones: AsyncTimezonesResource) -> None:
        self._timezones = timezones

        self.list = async_to_streamed_response_wrapper(
            timezones.list,
        )
