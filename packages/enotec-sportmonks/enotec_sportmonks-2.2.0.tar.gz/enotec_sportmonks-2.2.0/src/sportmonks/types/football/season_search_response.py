# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .season import Season
from ..._models import BaseModel
from ..shared.timezone import Timezone
from ..shared.pagination import Pagination
from ..shared.rate_limit import RateLimit
from ..shared.subscription import Subscription

__all__ = ["SeasonSearchResponse"]


class SeasonSearchResponse(BaseModel):
    data: Optional[List[Season]] = None

    pagination: Optional[Pagination] = None

    rate_limit: Optional[RateLimit] = None

    subscription: Optional[Subscription] = None

    timezone: Optional[Timezone] = None
