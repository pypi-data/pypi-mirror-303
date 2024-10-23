# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .team import Team
from ..._models import BaseModel
from ..shared.timezone import Timezone
from ..shared.pagination import Pagination
from ..shared.rate_limit import RateLimit
from ..shared.subscription import Subscription

__all__ = ["TeamSearchResponse"]


class TeamSearchResponse(BaseModel):
    data: Optional[List[Team]] = None

    pagination: Optional[Pagination] = None

    rate_limit: Optional[RateLimit] = None

    subscription: Optional[Subscription] = None

    timezone: Optional[Timezone] = None
