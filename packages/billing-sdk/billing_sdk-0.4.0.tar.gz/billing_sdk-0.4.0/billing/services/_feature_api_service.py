import uuid
from typing import List

from typing_extensions import Unpack

from billing.services._billing_api_service import BillingAPIService
from billing.types import FeatureRecordPayload, FeatureUsageEvent, FeatureUsageSummary


class FeatureAPIService(BillingAPIService):
    def retrieve_usage_summary(
        self,
        codename: str,
        customer_auth_service_id: uuid.UUID,
    ) -> FeatureUsageSummary:
        return self._request(
            "GET",
            f"/v1/features/{codename}/usage/summary/",
            params={"customer_auth_service_id": customer_auth_service_id},
            data_model=FeatureUsageSummary,
        )

    async def retrieve_usage_summary_async(
        self,
        codename: str,
        customer_auth_service_id: uuid.UUID,
    ) -> FeatureUsageSummary:
        return await self._request_async(
            "GET",
            f"/v1/features/{codename}/usage/summary/",
            params={"customer_auth_service_id": customer_auth_service_id},
            data_model=FeatureUsageSummary,
        )

    def list_usage_summary(
        self,
        customer_auth_service_id: uuid.UUID,
        page_number: int = 1,
        page_size: int = 50,
    ) -> List[FeatureUsageSummary]:
        return self._request(
            "GET",
            "/v1/features/usage/summary/",
            params={
                "page": page_number,
                "page_size": page_size,
                "customer_auth_service_id": customer_auth_service_id,
            },
            data_model=FeatureUsageSummary,
            batch_mode=True,
        )

    async def list_usage_summary_async(
        self,
        customer_auth_service_id: uuid.UUID,
        page_number: int = 1,
        page_size: int = 50,
    ) -> List[FeatureUsageSummary]:
        return await self._request_async(
            "GET",
            "/v1/features/usage/summary/",
            params={
                "page": page_number,
                "page_size": page_size,
                "customer_auth_service_id": customer_auth_service_id,
            },
            data_model=FeatureUsageSummary,
            batch_mode=True,
        )

    def record_usage(
        self,
        codename: str,
        **payload: Unpack[FeatureRecordPayload],
    ) -> FeatureUsageEvent:
        return self._request(
            "POST",
            f"/v1/features/{codename}/usage/record/",
            json=payload,
            data_model=FeatureUsageEvent,
        )

    async def record_usage_async(
        self,
        codename: str,
        **payload: Unpack[FeatureRecordPayload],
    ) -> FeatureUsageEvent:
        return await self._request_async(
            "POST",
            f"/v1/features/{codename}/usage/record/",
            json=payload,
            data_model=FeatureUsageEvent,
        )

    def refund_usage(self, feature_usage_event_id: str) -> FeatureUsageEvent:
        return self._request(
            "POST",
            f"/v1/features/usage/{feature_usage_event_id}/refund/",
            data_model=FeatureUsageEvent,
        )

    async def refund_usage_async(self, feature_usage_event_id: str) -> FeatureUsageEvent:
        return await self._request_async(
            "POST",
            f"/v1/features/usage/{feature_usage_event_id}/refund/",
            data_model=FeatureUsageEvent,
        )
