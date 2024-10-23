# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FixtureHeadToHeadParams"]


class FixtureHeadToHeadParams(TypedDict, total=False):
    version: Required[str]

    sport: Required[str]

    first_team: Required[Annotated[str, PropertyInfo(alias="firstTeam")]]

    order: str
    """The order you want to retrieve the items in"""

    page: int
    """The page number you want to retrieve"""

    per_page: int
    """The number of items per page you want to retrieve"""
