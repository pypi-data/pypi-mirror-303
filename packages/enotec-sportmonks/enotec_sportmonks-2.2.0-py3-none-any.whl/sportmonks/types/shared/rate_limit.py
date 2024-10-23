# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RateLimit"]


class RateLimit(BaseModel):
    remaining: Optional[float] = None

    requested_entity: Optional[str] = None

    resets_in_seconds: Optional[float] = None
