# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Player"]


class Player(BaseModel):
    id: Optional[float] = None

    city_id: Optional[object] = None

    common_name: Optional[str] = None

    country_id: Optional[float] = None

    date_of_birth: Optional[str] = None

    detailed_position_id: Optional[float] = None

    display_name: Optional[str] = None

    firstname: Optional[str] = None

    gender: Optional[str] = None

    height: Optional[float] = None

    image_path: Optional[str] = None

    lastname: Optional[str] = None

    name: Optional[str] = None

    nationality_id: Optional[float] = None

    position_id: Optional[float] = None

    sport_id: Optional[float] = None

    type_id: Optional[float] = None

    weight: Optional[float] = None
