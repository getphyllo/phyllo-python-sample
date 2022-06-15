from __future__ import annotations

from pydantic import BaseModel


class WebhookPayload(BaseModel):
    event: str
    name: str
    data: dict

    def __str__(self) -> str:
        return super().__str__()


def analyse_and_store_webhook(webhook_payload: WebhookPayload):
    if webhook_payload.event == "ACCOUNTS.CONNECTED":
        account_id = webhook_payload.data['account_id']
        # Fetch account info from account id
    if webhook_payload.event == "PROFILES.ADDED":
        # Fetch Profile info
        pass

    # Store the webhook info into db
    return webhook_payload.data
