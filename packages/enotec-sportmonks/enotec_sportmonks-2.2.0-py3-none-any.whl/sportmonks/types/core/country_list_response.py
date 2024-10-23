# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["CountryListResponse"]


class CountryListResponse(BaseModel):
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
