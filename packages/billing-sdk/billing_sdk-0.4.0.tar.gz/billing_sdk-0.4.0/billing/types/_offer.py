from datetime import datetime
from typing import Optional, TypedDict

from typing_extensions import NotRequired

from billing.types._billing_entity import BillingEntityWithTimestamps
from billing.types._common import CancellationFeedback


class Offer(BillingEntityWithTimestamps):
    order_id: str
    cancel_at: Optional[datetime]
    cancellation_requested_at: Optional[datetime]
    cancellation_feedback: Optional[CancellationFeedback]
    cancellation_comment: Optional[str]


class OfferCancelPayload(TypedDict):
    cancel_at: NotRequired[datetime]
    cancellation_feedback: NotRequired[CancellationFeedback]
    cancellation_comment: NotRequired[str]
