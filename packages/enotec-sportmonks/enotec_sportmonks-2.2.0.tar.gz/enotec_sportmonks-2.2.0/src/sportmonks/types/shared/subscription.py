# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["Subscription", "SubscriptionItem", "SubscriptionItemPlan"]


class SubscriptionItemPlan(BaseModel):
    category: Optional[str] = None

    plan: Optional[str] = None

    sport: Optional[str] = None


class SubscriptionItem(BaseModel):
    add_ons: Optional[List[object]] = None

    meta: Optional[List[object]] = None

    plans: Optional[List[SubscriptionItemPlan]] = None

    widgets: Optional[List[object]] = None


Subscription: TypeAlias = List[SubscriptionItem]
