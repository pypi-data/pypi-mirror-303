# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Season"]


class Season(BaseModel):
    id: Optional[float] = None

    ending_at: Optional[str] = None

    finished: Optional[bool] = None

    games_in_current_week: Optional[bool] = None

    is_current: Optional[bool] = None

    league_id: Optional[float] = None

    name: Optional[str] = None

    pending: Optional[bool] = None

    sport_id: Optional[float] = None

    standings_recalculated_at: Optional[str] = None

    starting_at: Optional[str] = None

    tie_breaker_rule_id: Optional[float] = None
