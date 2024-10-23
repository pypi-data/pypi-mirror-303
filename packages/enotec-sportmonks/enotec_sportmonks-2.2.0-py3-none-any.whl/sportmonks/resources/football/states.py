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
from ...types.football import state_list_params
from ...types.football.state_list_response import StateListResponse
from ...types.football.state_retrieve_response import StateRetrieveResponse

__all__ = ["StatesResource", "AsyncStatesResource"]


class StatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return StatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#with_streaming_response
        """
        return StatesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        state_id: str,
        *,
        version: str,
        sport: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StateRetrieveResponse:
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
        if not state_id:
            raise ValueError(f"Expected a non-empty value for `state_id` but received {state_id!r}")
        return self._get(
            f"/{version}/{sport}/states/{state_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StateRetrieveResponse,
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
    ) -> SyncPaginatedAPICall[StateListResponse]:
        """
        By Sport

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
            f"/{version}/{sport}/states",
            page=SyncPaginatedAPICall[StateListResponse],
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
                    state_list_params.StateListParams,
                ),
            ),
            model=StateListResponse,
        )


class AsyncStatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#with_streaming_response
        """
        return AsyncStatesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        state_id: str,
        *,
        version: str,
        sport: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StateRetrieveResponse:
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
        if not state_id:
            raise ValueError(f"Expected a non-empty value for `state_id` but received {state_id!r}")
        return await self._get(
            f"/{version}/{sport}/states/{state_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StateRetrieveResponse,
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
    ) -> AsyncPaginator[StateListResponse, AsyncPaginatedAPICall[StateListResponse]]:
        """
        By Sport

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
            f"/{version}/{sport}/states",
            page=AsyncPaginatedAPICall[StateListResponse],
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
                    state_list_params.StateListParams,
                ),
            ),
            model=StateListResponse,
        )


class StatesResourceWithRawResponse:
    def __init__(self, states: StatesResource) -> None:
        self._states = states

        self.retrieve = to_raw_response_wrapper(
            states.retrieve,
        )
        self.list = to_raw_response_wrapper(
            states.list,
        )


class AsyncStatesResourceWithRawResponse:
    def __init__(self, states: AsyncStatesResource) -> None:
        self._states = states

        self.retrieve = async_to_raw_response_wrapper(
            states.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            states.list,
        )


class StatesResourceWithStreamingResponse:
    def __init__(self, states: StatesResource) -> None:
        self._states = states

        self.retrieve = to_streamed_response_wrapper(
            states.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            states.list,
        )


class AsyncStatesResourceWithStreamingResponse:
    def __init__(self, states: AsyncStatesResource) -> None:
        self._states = states

        self.retrieve = async_to_streamed_response_wrapper(
            states.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            states.list,
        )
