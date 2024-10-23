# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..shared.timezone import Timezone
from ..shared.rate_limit import RateLimit
from ..shared.subscription import Subscription

__all__ = ["RegionRetrieveResponse", "Data"]


class Data(BaseModel):
    id: Optional[float] = None

    country_id: Optional[float] = None

    name: Optional[str] = None


class RegionRetrieveResponse(BaseModel):
    data: Optional[Data] = None

    rate_limit: Optional[RateLimit] = None

    subscription: Optional[Subscription] = None

    timezone: Optional[Timezone] = None
