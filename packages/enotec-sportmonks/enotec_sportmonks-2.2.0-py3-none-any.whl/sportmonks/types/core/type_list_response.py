# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["TypeListResponse"]


class TypeListResponse(BaseModel):
    id: Optional[float] = None

    code: Optional[str] = None

    developer_name: Optional[str] = None

    name: Optional[str] = None

    type_of_model: Optional[str] = None
