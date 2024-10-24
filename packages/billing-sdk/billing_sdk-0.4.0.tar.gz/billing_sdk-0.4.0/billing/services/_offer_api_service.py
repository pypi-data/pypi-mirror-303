from typing_extensions import Unpack

from billing.services._billing_api_service import BillingAPIService
from billing.types import OfferCancelPayload


class OfferAPIService(BillingAPIService):
    def cancel(
        self,
        object_id: str,
        **payload: Unpack[OfferCancelPayload],
    ) -> None:
        return self._request(
            "POST",
            f"/v1/offers/{object_id}/cancel/",
            json=payload,
        )

    async def cancel_async(
        self,
        object_id: str,
        **payload: Unpack[OfferCancelPayload],
    ) -> None:
        return await self._request_async(
            "POST",
            f"/v1/offers/{object_id}/cancel/",
            json=payload,
        )
