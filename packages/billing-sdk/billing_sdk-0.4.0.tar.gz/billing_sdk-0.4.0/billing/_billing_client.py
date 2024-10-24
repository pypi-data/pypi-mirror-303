from typing import Optional

from httpx import AsyncClient, Client

from billing._constants import DEFAULT_API_URL, TERMINAL_SECRET_KEY_PREFIX
from billing._http_client import HTTPClient
from billing.services import (
    AgreementAPIService,
    FeatureAPIService,
    InvoiceAPIService,
    OfferAPIService,
    OrderAPIService,
    ProductAPIService,
)


class BillingClient:
    def __init__(
        self,
        terminal_secret_key: str,
        terminal_id: str,
        *,
        billing_base_url: str = DEFAULT_API_URL,
        max_network_retries: int = 0,
        setup_sync_client: bool = False,
        setup_async_client: bool = True,
        sync_client: Optional[Client] = None,
        async_client: Optional[AsyncClient] = None,
    ) -> None:
        if not terminal_secret_key.startswith(TERMINAL_SECRET_KEY_PREFIX):
            raise ValueError(f"Invalid terminal secret key. Must starts with `{TERMINAL_SECRET_KEY_PREFIX}`.")

        self._http_client = HTTPClient(
            terminal_secret_key=terminal_secret_key,
            terminal_id=terminal_id,
            base_url=billing_base_url,
            max_network_retries=max_network_retries,
            setup_sync_client=setup_sync_client,
            setup_async_client=setup_async_client,
            sync_client=sync_client,
            async_client=async_client,
        )

        self._agreements = AgreementAPIService(http_client=self._http_client)
        self._features = FeatureAPIService(http_client=self._http_client)
        self._invoices = InvoiceAPIService(http_client=self._http_client)
        self._offers = OfferAPIService(http_client=self._http_client)
        self._orders = OrderAPIService(http_client=self._http_client)
        self._products = ProductAPIService(http_client=self._http_client)

    @property
    def agreements(self) -> AgreementAPIService:
        return self._agreements

    @property
    def features(self) -> FeatureAPIService:
        return self._features

    @property
    def invoices(self) -> InvoiceAPIService:
        return self._invoices

    @property
    def offers(self) -> OfferAPIService:
        return self._offers

    @property
    def orders(self) -> OrderAPIService:
        return self._orders

    @property
    def products(self) -> ProductAPIService:
        return self._products

    def close_sync_client(self) -> None:
        self._http_client.close_sync_client()

    async def close_async_client(self) -> None:
        await self._http_client.close_async_client()
