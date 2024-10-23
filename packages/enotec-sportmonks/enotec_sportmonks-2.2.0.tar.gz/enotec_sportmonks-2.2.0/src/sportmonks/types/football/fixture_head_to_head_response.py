# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .fixture import Fixture
from ..._models import BaseModel
from ..shared.timezone import Timezone
from ..shared.subscription import Subscription

__all__ = ["FixtureHeadToHeadResponse", "RateLimit"]


class RateLimit(BaseModel):
    remaining: Optional[float] = None

    requested_entity: Optional[str] = None

    resets_in_seconds: Optional[float] = None


class FixtureHeadToHeadResponse(BaseModel):
    data: Optional[List[Fixture]] = None

    rate_limit: Optional[RateLimit] = None

    subscription: Optional[Subscription] = None

    timezone: Optional[Timezone] = None
