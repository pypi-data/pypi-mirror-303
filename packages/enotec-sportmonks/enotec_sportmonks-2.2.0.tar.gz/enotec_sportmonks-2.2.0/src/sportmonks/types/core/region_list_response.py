# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RegionListResponse"]


class RegionListResponse(BaseModel):
    id: Optional[float] = None

    country_id: Optional[float] = None

    name: Optional[str] = None
