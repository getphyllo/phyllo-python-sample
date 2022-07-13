from __future__ import annotations

import json

from pydantic import BaseModel
from requests import Request
from sqlalchemy.testing.plugin.plugin_base import log

from app.utils.phyllo_api import get_account_by_id
from app.utils.phyllo_config import CLIENT_SECRET
from app.utils.webhook_utils import Utility


class WebhookPayload(BaseModel):
    event: str
    name: str
    data: dict

    def __str__(self) -> str:
        return super().__str__()


def analyse_and_store_webhook(webhook_payload: WebhookPayload, request: Request):
    signature = request.headers.get("Phyllo-Signature")
    flag: bool = Utility().verify_signature(json.dumps(webhook_payload), signature=signature,
                                            key=CLIENT_SECRET)

    print("*** flag == ", flag)
    if webhook_payload.event == "ACCOUNTS.CONNECTED":
        account_id = webhook_payload.data['account_id']
        account = get_account_by_id(id=account_id)
        log.info(account)
    if webhook_payload.event == "PROFILES.ADDED":
        # Fetch Profile info
        pass

    # Store the webhook info into db
    return webhook_payload.data
