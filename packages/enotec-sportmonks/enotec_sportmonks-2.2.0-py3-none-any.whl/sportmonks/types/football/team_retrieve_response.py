# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .team import Team
from ..._models import BaseModel
from ..shared.timezone import Timezone
from ..shared.rate_limit import RateLimit
from ..shared.subscription import Subscription

__all__ = ["TeamRetrieveResponse"]


class TeamRetrieveResponse(BaseModel):
    data: Optional[Team] = None

    rate_limit: Optional[RateLimit] = None

    subscription: Optional[Subscription] = None

    timezone: Optional[Timezone] = None
