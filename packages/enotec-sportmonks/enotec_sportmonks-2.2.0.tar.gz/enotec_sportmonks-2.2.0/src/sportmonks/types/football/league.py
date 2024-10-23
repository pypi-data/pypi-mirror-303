# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["League"]


class League(BaseModel):
    id: Optional[float] = None

    active: Optional[bool] = None

    category: Optional[float] = None

    country_id: Optional[float] = None

    has_jerseys: Optional[bool] = None

    image_path: Optional[str] = None

    last_played_at: Optional[str] = None

    name: Optional[str] = None

    short_code: Optional[str] = None

    sport_id: Optional[float] = None

    sub_type: Optional[str] = None

    type: Optional[str] = None
