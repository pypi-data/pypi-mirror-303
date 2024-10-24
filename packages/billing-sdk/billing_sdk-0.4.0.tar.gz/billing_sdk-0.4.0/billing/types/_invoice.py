from datetime import datetime
from decimal import Decimal
from typing import List, Literal, Optional, TypedDict

from typing_extensions import NotRequired

from billing.types._billing_entity import BillingEntityWithTimestamps
from billing.types._invoice_item import InvoiceItemWithProduct


class Invoice(BillingEntityWithTimestamps):
    total: Decimal
    currency: str
    issued_at: Optional[datetime]
    expired_at: datetime
    paid_at: Optional[datetime]
    refunded_at: Optional[datetime]
    payment_method: Literal["stripe", "telegram_stars"]
    receipt_url: str
    failed_reason: str
    checkout_session_url: Optional[str]


class InvoiceWithItemsBundle(Invoice):
    items: List[InvoiceItemWithProduct]


class InvoiceListParams(TypedDict):
    order_id: NotRequired[str]
    customer_auth_service_id: NotRequired[str]
