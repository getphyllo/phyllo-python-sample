from __future__ import annotations

import json
import requests
from fastapi import HTTPException
from requests.auth import HTTPBasicAuth

from app.utils.phyllo_config import CLIENT_ID, CLIENT_SECRET, BASE_URL, WEBHOOK_NAME, WEBHOOK_URL, SUPPORTED_WEBHOOK_EVENTS

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


def get_all_webhooks():
    try:
        response = requests.get(BASE_URL + "/v1/webhooks", auth=HTTPBasicAuth(CLIENT_ID,
                                                                              CLIENT_SECRET))
        return response.json()

    except requests.exceptions.RequestException as err:
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")


def create_webhook():
    try:
        request_body = {
            "url": WEBHOOK_URL,
            "events": SUPPORTED_WEBHOOK_EVENTS,
            "name": WEBHOOK_NAME
        }
        response = requests.post(BASE_URL + "/v1/webhooks", auth=HTTPBasicAuth(CLIENT_ID,
                                                                               CLIENT_SECRET), json=request_body)
        return response.json()

    except requests.exceptions.RequestException as err:
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")


def update_webhook(id: str):
    try:
        request_body = {
            "url": WEBHOOK_URL,
            "events": SUPPORTED_WEBHOOK_EVENTS,
            "name": WEBHOOK_NAME
        }
        response = requests.put(BASE_URL + f"/v1/webhooks/{id}", auth=HTTPBasicAuth(CLIENT_ID,
                                                                                    CLIENT_SECRET), json=request_body)
        return response.json()

    except requests.exceptions.RequestException as err:
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")


async def analyse_and_store_webhook(request: Request):
    signature = request.headers.get("Phyllo-Signature")
    body = await request.json()
    flag: bool = Utility().verify_signature(json.dumps(body), signature=signature,
                                            key=CLIENT_SECRET)
    # Do check whether this flag is true or not
    if not flag:
        raise Exception("Unauthorised webhook event")

    webhook_payload: WebhookPayload = WebhookPayload(**body)
    if webhook_payload.event == "ACCOUNTS.CONNECTED":
        account_id = webhook_payload.data['account_id']
        account = get_account_by_id(id=account_id)
        log.info(account)
    if webhook_payload.event == "PROFILES.ADDED":
        # Fetch Profile info
        pass

    # Add other events check which you wish to receive and call corresponding APIs



    # Store the webhook info into db
    return webhook_payload.data


