import uuid
from typing import List, TypedDict

from typing_extensions import NotRequired

from billing.types._billing_entity import BillingEntity


class Order(BillingEntity):
    pass


class OrderCreatePayload(TypedDict):
    customer_auth_service_id: uuid.UUID
    product_plan_ids: List[str]


class OrderListParams(TypedDict):
    customer_auth_service_id: NotRequired[uuid.UUID]
