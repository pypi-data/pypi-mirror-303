# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Fixture"]


class Fixture(BaseModel):
    id: Optional[float] = None

    aggregate_id: Optional[object] = None

    details: Optional[object] = None

    group_id: Optional[object] = None

    has_odds: Optional[bool] = None

    league_id: Optional[float] = None

    leg: Optional[str] = None

    length: Optional[float] = None

    name: Optional[str] = None

    placeholder: Optional[bool] = None

    result_info: Optional[str] = None

    round_id: Optional[float] = None

    season_id: Optional[float] = None

    sport_id: Optional[float] = None

    stage_id: Optional[float] = None

    starting_at: Optional[str] = None

    starting_at_timestamp: Optional[float] = None

    state_id: Optional[float] = None

    venue_id: Optional[float] = None
