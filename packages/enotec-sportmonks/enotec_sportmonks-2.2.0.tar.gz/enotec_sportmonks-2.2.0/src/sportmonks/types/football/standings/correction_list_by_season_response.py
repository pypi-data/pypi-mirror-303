# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from ...shared.timezone import Timezone
from ...shared.rate_limit import RateLimit
from ...shared.subscription import Subscription

__all__ = ["CorrectionListBySeasonResponse", "Data"]


class Data(BaseModel):
    id: Optional[float] = None

    active: Optional[bool] = None

    calc_type: Optional[str] = None

    group_id: Optional[object] = None

    participant_id: Optional[float] = None

    participant_type: Optional[str] = None

    season_id: Optional[float] = None

    stage_id: Optional[float] = None

    type_id: Optional[float] = None

    value: Optional[float] = None


class CorrectionListBySeasonResponse(BaseModel):
    data: Optional[List[Data]] = None

    rate_limit: Optional[RateLimit] = None

    subscription: Optional[Subscription] = None

    timezone: Optional[Timezone] = None
