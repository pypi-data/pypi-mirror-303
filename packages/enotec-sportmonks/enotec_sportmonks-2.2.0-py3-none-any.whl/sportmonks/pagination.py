# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional, cast
from typing_extensions import override

from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["PaginatedAPICallPagination", "PaginatedAPICallRateLimit", "SyncPaginatedAPICall", "AsyncPaginatedAPICall"]

_T = TypeVar("_T")


class PaginatedAPICallPagination(BaseModel):
    count: Optional[int] = None
    """The total number of items."""

    current_page: Optional[int] = None
    """The current page number."""

    has_more: Optional[bool] = None
    """Whether there are more pages."""

    next_page: Optional[str] = None
    """The URL for the next page."""

    per_page: Optional[int] = None
    """The number of items per page."""


class PaginatedAPICallRateLimit(BaseModel):
    remaining: Optional[int] = None
    """The number of requests remaining in the current period."""

    requested_entity: Optional[str] = None
    """The entity that was requested."""

    resets_in_seconds: Optional[int] = None
    """The number of seconds until the rate limit resets."""


class SyncPaginatedAPICall(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    pagination: Optional[PaginatedAPICallPagination] = None
    subscription: Optional[List[object]] = None
    rate_limit: Optional[PaginatedAPICallRateLimit] = None
    timezone: Optional[str] = None
    """The timezone to use for the response."""

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page")) or 1

        return PageInfo(params={"page": last_page + 1})


class AsyncPaginatedAPICall(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    pagination: Optional[PaginatedAPICallPagination] = None
    subscription: Optional[List[object]] = None
    rate_limit: Optional[PaginatedAPICallRateLimit] = None
    timezone: Optional[str] = None
    """The timezone to use for the response."""

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page")) or 1

        return PageInfo(params={"page": last_page + 1})
