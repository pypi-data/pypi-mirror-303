# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .fixture import Fixture
from ..._models import BaseModel
from ..shared.timezone import Timezone
from ..shared.rate_limit import RateLimit
from ..shared.subscription import Subscription

__all__ = ["FixtureListByIDsResponse"]


class FixtureListByIDsResponse(BaseModel):
    data: Optional[List[Fixture]] = None

    rate_limit: Optional[RateLimit] = None

    subscription: Optional[Subscription] = None

    timezone: Optional[Timezone] = None
