# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from ...shared.timezone import Timezone
from ...shared.rate_limit import RateLimit
from ...shared.subscription import Subscription

__all__ = ["LiveListByLeagueResponse", "Data"]


class Data(BaseModel):
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


class LiveListByLeagueResponse(BaseModel):
    data: Optional[List[Data]] = None

    rate_limit: Optional[RateLimit] = None

    subscription: Optional[Subscription] = None

    timezone: Optional[Timezone] = None
