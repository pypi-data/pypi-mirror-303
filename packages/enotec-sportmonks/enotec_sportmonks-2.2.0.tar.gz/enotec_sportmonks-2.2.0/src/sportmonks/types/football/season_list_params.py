# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SeasonListParams"]


class SeasonListParams(TypedDict, total=False):
    version: Required[str]

    order: str
    """The order you want to retrieve the items in"""

    page: int
    """The page number you want to retrieve"""

    per_page: int
    """The number of items per page you want to retrieve"""
