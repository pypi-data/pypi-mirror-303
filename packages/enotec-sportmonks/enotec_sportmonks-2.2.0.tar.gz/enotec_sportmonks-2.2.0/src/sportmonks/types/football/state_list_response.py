# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["StateListResponse"]


class StateListResponse(BaseModel):
    id: Optional[float] = None

    developer_name: Optional[str] = None

    name: Optional[str] = None

    short_name: Optional[str] = None

    state: Optional[str] = None
