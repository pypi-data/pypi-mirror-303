# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Team"]


class Team(BaseModel):
    id: Optional[float] = None

    country_id: Optional[float] = None

    founded: Optional[float] = None

    gender: Optional[str] = None

    image_path: Optional[str] = None

    last_played_at: Optional[str] = None

    name: Optional[str] = None

    placeholder: Optional[bool] = None

    short_code: Optional[str] = None

    sport_id: Optional[float] = None

    type: Optional[str] = None

    venue_id: Optional[float] = None
