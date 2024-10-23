# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..shared.timezone import Timezone
from ..shared.rate_limit import RateLimit
from ..shared.subscription import Subscription

__all__ = ["StateRetrieveResponse", "Data"]


class Data(BaseModel):
    id: Optional[float] = None

    developer_name: Optional[str] = None

    name: Optional[str] = None

    short_name: Optional[str] = None

    state: Optional[str] = None


class StateRetrieveResponse(BaseModel):
    data: Optional[Data] = None

    rate_limit: Optional[RateLimit] = None

    subscription: Optional[Subscription] = None

    timezone: Optional[Timezone] = None
