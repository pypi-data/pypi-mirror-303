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
from ...types.core import continent_list_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.core.continent_list_response import ContinentListResponse
from ...types.core.continent_retrieve_response import ContinentRetrieveResponse

__all__ = ["ContinentsResource", "AsyncContinentsResource"]


class ContinentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContinentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ContinentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContinentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#with_streaming_response
        """
        return ContinentsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        continent_id: str,
        *,
        version: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContinentRetrieveResponse:
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
        if not continent_id:
            raise ValueError(f"Expected a non-empty value for `continent_id` but received {continent_id!r}")
        return self._get(
            f"/{version}/core/continents/{continent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContinentRetrieveResponse,
        )

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
    ) -> SyncPaginatedAPICall[ContinentListResponse]:
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
            f"/{version}/core/continents",
            page=SyncPaginatedAPICall[ContinentListResponse],
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
                    continent_list_params.ContinentListParams,
                ),
            ),
            model=ContinentListResponse,
        )


class AsyncContinentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContinentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContinentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContinentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#with_streaming_response
        """
        return AsyncContinentsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        continent_id: str,
        *,
        version: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContinentRetrieveResponse:
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
        if not continent_id:
            raise ValueError(f"Expected a non-empty value for `continent_id` but received {continent_id!r}")
        return await self._get(
            f"/{version}/core/continents/{continent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContinentRetrieveResponse,
        )

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
    ) -> AsyncPaginator[ContinentListResponse, AsyncPaginatedAPICall[ContinentListResponse]]:
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
            f"/{version}/core/continents",
            page=AsyncPaginatedAPICall[ContinentListResponse],
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
                    continent_list_params.ContinentListParams,
                ),
            ),
            model=ContinentListResponse,
        )


class ContinentsResourceWithRawResponse:
    def __init__(self, continents: ContinentsResource) -> None:
        self._continents = continents

        self.retrieve = to_raw_response_wrapper(
            continents.retrieve,
        )
        self.list = to_raw_response_wrapper(
            continents.list,
        )


class AsyncContinentsResourceWithRawResponse:
    def __init__(self, continents: AsyncContinentsResource) -> None:
        self._continents = continents

        self.retrieve = async_to_raw_response_wrapper(
            continents.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            continents.list,
        )


class ContinentsResourceWithStreamingResponse:
    def __init__(self, continents: ContinentsResource) -> None:
        self._continents = continents

        self.retrieve = to_streamed_response_wrapper(
            continents.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            continents.list,
        )


class AsyncContinentsResourceWithStreamingResponse:
    def __init__(self, continents: AsyncContinentsResource) -> None:
        self._continents = continents

        self.retrieve = async_to_streamed_response_wrapper(
            continents.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            continents.list,
        )
