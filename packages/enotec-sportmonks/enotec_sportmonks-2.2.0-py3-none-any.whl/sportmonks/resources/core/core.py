# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .types import (
    TypesResource,
    AsyncTypesResource,
    TypesResourceWithRawResponse,
    AsyncTypesResourceWithRawResponse,
    TypesResourceWithStreamingResponse,
    AsyncTypesResourceWithStreamingResponse,
)
from .regions import (
    RegionsResource,
    AsyncRegionsResource,
    RegionsResourceWithRawResponse,
    AsyncRegionsResourceWithRawResponse,
    RegionsResourceWithStreamingResponse,
    AsyncRegionsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .countries import (
    CountriesResource,
    AsyncCountriesResource,
    CountriesResourceWithRawResponse,
    AsyncCountriesResourceWithRawResponse,
    CountriesResourceWithStreamingResponse,
    AsyncCountriesResourceWithStreamingResponse,
)
from .timezones import (
    TimezonesResource,
    AsyncTimezonesResource,
    TimezonesResourceWithRawResponse,
    AsyncTimezonesResourceWithRawResponse,
    TimezonesResourceWithStreamingResponse,
    AsyncTimezonesResourceWithStreamingResponse,
)
from .continents import (
    ContinentsResource,
    AsyncContinentsResource,
    ContinentsResourceWithRawResponse,
    AsyncContinentsResourceWithRawResponse,
    ContinentsResourceWithStreamingResponse,
    AsyncContinentsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["CoreResource", "AsyncCoreResource"]


class CoreResource(SyncAPIResource):
    @cached_property
    def continents(self) -> ContinentsResource:
        return ContinentsResource(self._client)

    @cached_property
    def countries(self) -> CountriesResource:
        return CountriesResource(self._client)

    @cached_property
    def regions(self) -> RegionsResource:
        return RegionsResource(self._client)

    @cached_property
    def types(self) -> TypesResource:
        return TypesResource(self._client)

    @cached_property
    def timezones(self) -> TimezonesResource:
        return TimezonesResource(self._client)

    @cached_property
    def with_raw_response(self) -> CoreResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CoreResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CoreResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#with_streaming_response
        """
        return CoreResourceWithStreamingResponse(self)


class AsyncCoreResource(AsyncAPIResource):
    @cached_property
    def continents(self) -> AsyncContinentsResource:
        return AsyncContinentsResource(self._client)

    @cached_property
    def countries(self) -> AsyncCountriesResource:
        return AsyncCountriesResource(self._client)

    @cached_property
    def regions(self) -> AsyncRegionsResource:
        return AsyncRegionsResource(self._client)

    @cached_property
    def types(self) -> AsyncTypesResource:
        return AsyncTypesResource(self._client)

    @cached_property
    def timezones(self) -> AsyncTimezonesResource:
        return AsyncTimezonesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCoreResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCoreResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCoreResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/enotec/sportmonks-sdk-python#with_streaming_response
        """
        return AsyncCoreResourceWithStreamingResponse(self)


class CoreResourceWithRawResponse:
    def __init__(self, core: CoreResource) -> None:
        self._core = core

    @cached_property
    def continents(self) -> ContinentsResourceWithRawResponse:
        return ContinentsResourceWithRawResponse(self._core.continents)

    @cached_property
    def countries(self) -> CountriesResourceWithRawResponse:
        return CountriesResourceWithRawResponse(self._core.countries)

    @cached_property
    def regions(self) -> RegionsResourceWithRawResponse:
        return RegionsResourceWithRawResponse(self._core.regions)

    @cached_property
    def types(self) -> TypesResourceWithRawResponse:
        return TypesResourceWithRawResponse(self._core.types)

    @cached_property
    def timezones(self) -> TimezonesResourceWithRawResponse:
        return TimezonesResourceWithRawResponse(self._core.timezones)


class AsyncCoreResourceWithRawResponse:
    def __init__(self, core: AsyncCoreResource) -> None:
        self._core = core

    @cached_property
    def continents(self) -> AsyncContinentsResourceWithRawResponse:
        return AsyncContinentsResourceWithRawResponse(self._core.continents)

    @cached_property
    def countries(self) -> AsyncCountriesResourceWithRawResponse:
        return AsyncCountriesResourceWithRawResponse(self._core.countries)

    @cached_property
    def regions(self) -> AsyncRegionsResourceWithRawResponse:
        return AsyncRegionsResourceWithRawResponse(self._core.regions)

    @cached_property
    def types(self) -> AsyncTypesResourceWithRawResponse:
        return AsyncTypesResourceWithRawResponse(self._core.types)

    @cached_property
    def timezones(self) -> AsyncTimezonesResourceWithRawResponse:
        return AsyncTimezonesResourceWithRawResponse(self._core.timezones)


class CoreResourceWithStreamingResponse:
    def __init__(self, core: CoreResource) -> None:
        self._core = core

    @cached_property
    def continents(self) -> ContinentsResourceWithStreamingResponse:
        return ContinentsResourceWithStreamingResponse(self._core.continents)

    @cached_property
    def countries(self) -> CountriesResourceWithStreamingResponse:
        return CountriesResourceWithStreamingResponse(self._core.countries)

    @cached_property
    def regions(self) -> RegionsResourceWithStreamingResponse:
        return RegionsResourceWithStreamingResponse(self._core.regions)

    @cached_property
    def types(self) -> TypesResourceWithStreamingResponse:
        return TypesResourceWithStreamingResponse(self._core.types)

    @cached_property
    def timezones(self) -> TimezonesResourceWithStreamingResponse:
        return TimezonesResourceWithStreamingResponse(self._core.timezones)


class AsyncCoreResourceWithStreamingResponse:
    def __init__(self, core: AsyncCoreResource) -> None:
        self._core = core

    @cached_property
    def continents(self) -> AsyncContinentsResourceWithStreamingResponse:
        return AsyncContinentsResourceWithStreamingResponse(self._core.continents)

    @cached_property
    def countries(self) -> AsyncCountriesResourceWithStreamingResponse:
        return AsyncCountriesResourceWithStreamingResponse(self._core.countries)

    @cached_property
    def regions(self) -> AsyncRegionsResourceWithStreamingResponse:
        return AsyncRegionsResourceWithStreamingResponse(self._core.regions)

    @cached_property
    def types(self) -> AsyncTypesResourceWithStreamingResponse:
        return AsyncTypesResourceWithStreamingResponse(self._core.types)

    @cached_property
    def timezones(self) -> AsyncTimezonesResourceWithStreamingResponse:
        return AsyncTimezonesResourceWithStreamingResponse(self._core.timezones)
