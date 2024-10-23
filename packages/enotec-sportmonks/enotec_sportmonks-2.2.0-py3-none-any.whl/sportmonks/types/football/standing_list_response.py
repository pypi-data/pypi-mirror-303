# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["StandingListResponse"]


class StandingListResponse(BaseModel):
    id: Optional[float] = None

    group_id: Optional[object] = None

    league_id: Optional[float] = None

    participant_id: Optional[float] = None

    points: Optional[float] = None

    position: Optional[float] = None

    result: Optional[str] = None

    round_id: Optional[float] = None

    season_id: Optional[float] = None

    sport_id: Optional[float] = None

    stage_id: Optional[float] = None

    standing_rule_id: Optional[float] = None
