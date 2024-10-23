# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Pagination"]


class Pagination(BaseModel):
    count: Optional[float] = None

    current_page: Optional[float] = None

    has_more: Optional[bool] = None

    next_page: Optional[str] = None

    per_page: Optional[float] = None
