# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["TopscorerListBySeasonResponse"]


class TopscorerListBySeasonResponse(BaseModel):
    participant_id: Optional[float] = None

    player_id: Optional[float] = None

    position: Optional[float] = None

    season_id: Optional[float] = None

    total: Optional[float] = None

    type_id: Optional[float] = None
