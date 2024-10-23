# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.timezone import Timezone
from ..shared.pagination import Pagination
from ..shared.rate_limit import RateLimit
from ..shared.subscription import Subscription

__all__ = ["CountrySearchResponse", "Data"]


class Data(BaseModel):
    id: Optional[float] = None

    borders: Optional[List[str]] = None

    continent_id: Optional[float] = None

    fifa_name: Optional[str] = None

    image_path: Optional[str] = None

    iso2: Optional[str] = None

    iso3: Optional[str] = None

    latitude: Optional[float] = None

    longitude: Optional[float] = None

    name: Optional[str] = None

    official_name: Optional[str] = None


class CountrySearchResponse(BaseModel):
    data: Optional[List[Data]] = None

    pagination: Optional[Pagination] = None

    rate_limit: Optional[RateLimit] = None

    subscription: Optional[Subscription] = None

    timezone: Optional[Timezone] = None
