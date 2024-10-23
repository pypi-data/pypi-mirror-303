# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .livescore import Livescore
from ..shared.timezone import Timezone
from ..shared.rate_limit import RateLimit
from ..shared.subscription import Subscription

__all__ = ["LivescoreInplayResponse"]


class LivescoreInplayResponse(BaseModel):
    data: Optional[List[Livescore]] = None

    rate_limit: Optional[RateLimit] = None

    subscription: Optional[Subscription] = None

    timezone: Optional[Timezone] = None
