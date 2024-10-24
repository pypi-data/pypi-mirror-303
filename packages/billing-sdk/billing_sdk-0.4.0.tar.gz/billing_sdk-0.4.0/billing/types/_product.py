from billing.types._billing_entity import BillingEntityWithTimestamps


class Product(BillingEntityWithTimestamps):
    name: str
    description: str
