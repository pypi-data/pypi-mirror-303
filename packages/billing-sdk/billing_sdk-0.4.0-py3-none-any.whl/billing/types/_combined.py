from typing import List

from billing.types._invoice import InvoiceWithItemsBundle
from billing.types._offer import Offer
from billing.types._offer_product_plan import OfferProductPlan
from billing.types._order import Order
from billing.types._product import Product
from billing.types._product_plan import ProductPlan


class OfferPlansBundle(Offer):
    offer_product_plans: List[OfferProductPlan]


class OfferInvoicesBundle(Offer):
    invoices: List[InvoiceWithItemsBundle]


class OrderOffersBundle(Order):
    offers: List[OfferPlansBundle]


class OrderWithOffersAndInvoicesBundle(Order):
    offers: List[OfferInvoicesBundle]


class ProductPlanWithImagesBundle(Product):
    product_plans: List[ProductPlan]
